#!/usr/bin/env python3
"""Static validator for the TFAST CK3 mods.

Run from the repository root:

    python tools/validate.py

Exit code 0 = everything the game would choke on is clean.
Exit code 1 = at least one ERROR.

WARN entries are printed but do not fail the build; they are things that are
usually wrong but occasionally intentional.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODS = ROOT / "mods"

BOM = b"\xef\xbb\xbf"

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(p)


# --------------------------------------------------------------------------
# 1. Localization files: UTF-8 BOM + duplicate keys
# --------------------------------------------------------------------------

LOC_LINE = re.compile(r'^\s*([A-Za-z0-9_.\-]+)\s*:\d*\s*"')


def check_localization() -> None:
    for mod_dir in sorted(p for p in MODS.iterdir() if p.is_dir()):
        first_seen: dict[str, Path] = {}

        for yml in sorted(mod_dir.rglob("*.yml")):
            raw = yml.read_bytes()

            if not raw.startswith(BOM):
                err(f"{rel(yml)}: missing UTF-8 BOM (all localization keys will fail to load)")

            # Decode as UTF-8 with BOM tolerance
            try:
                text = raw.decode("utf-8-sig")
            except UnicodeDecodeError as exc:
                err(f"{rel(yml)}: not valid UTF-8 ({exc})")
                continue

            # CK3 allows blank lines and comments before the language header.
            header = ""
            for line in text.splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                header = stripped
                break
            if not header.startswith("l_english:"):
                warn(f"{rel(yml)}: no 'l_english:' header found (first content line is {header!r})")

            for lineno, line in enumerate(text.splitlines(), 1):
                if line.lstrip().startswith("#"):
                    continue
                m = LOC_LINE.match(line)
                if not m:
                    continue
                key = m.group(1)
                if key.lower() == "l_english":
                    continue
                if key in first_seen:
                    other = first_seen[key]
                    if other != yml:
                        err(
                            f"{rel(yml)}:{lineno}: duplicate localization key "
                            f"'{key}' (already in {rel(other)})"
                        )
                    else:
                        err(f"{rel(yml)}:{lineno}: duplicate localization key '{key}' in same file")
                else:
                    first_seen[key] = yml


# --------------------------------------------------------------------------
# 2. Script files: balanced braces
# --------------------------------------------------------------------------

COMMENT = re.compile(r"#.*$")


def check_braces() -> None:
    for mod_dir in sorted(p for p in MODS.iterdir() if p.is_dir()):
        for txt in sorted(mod_dir.rglob("*.txt")):
            try:
                text = txt.read_text(encoding="utf-8-sig", errors="replace")
            except OSError as exc:
                err(f"{rel(txt)}: cannot read ({exc})")
                continue

            depth = 0
            bad = False
            for lineno, line in enumerate(text.splitlines(), 1):
                stripped = COMMENT.sub("", line)
                # ignore quoted strings when counting
                stripped = re.sub(r'"[^"]*"', '""', stripped)
                for ch in stripped:
                    if ch == "{":
                        depth += 1
                    elif ch == "}":
                        depth -= 1
                        if depth < 0:
                            err(f"{rel(txt)}:{lineno}: closing brace with no opener")
                            bad = True
                            depth = 0
                if bad:
                    break
            if not bad and depth != 0:
                err(f"{rel(txt)}: {depth} unclosed '{{' at end of file")


# --------------------------------------------------------------------------
# 3. Descriptor files
# --------------------------------------------------------------------------

FIELD = re.compile(r'^\s*(version|name|supported_version)\s*=\s*"([^"]*)"', re.M)
PATH_FIELD = re.compile(r'^\s*path\s*=\s*"([^"]*)"', re.M)


def check_descriptors() -> None:
    for mod_dir in sorted(p for p in MODS.iterdir() if p.is_dir()):
        name = mod_dir.name
        inner = mod_dir / "descriptor.mod"
        outer = MODS / f"{name}.mod"

        if not inner.exists():
            err(f"mods/{name}/descriptor.mod: missing")
            continue
        if not outer.exists():
            err(f"mods/{name}.mod: missing launcher descriptor")
            continue

        inner_txt = inner.read_text(encoding="utf-8-sig", errors="replace")
        outer_txt = outer.read_text(encoding="utf-8-sig", errors="replace")

        inner_fields = dict(FIELD.findall(inner_txt))
        outer_fields = dict(FIELD.findall(outer_txt))

        for key in ("version", "name", "supported_version"):
            a, b = inner_fields.get(key), outer_fields.get(key)
            if a is None:
                err(f"mods/{name}/descriptor.mod: missing '{key}'")
            if b is None:
                err(f"mods/{name}.mod: missing '{key}'")
            if a is not None and b is not None and a != b:
                err(f"{name}: '{key}' differs — descriptor.mod='{a}' but {name}.mod='{b}'")

        # The in-folder descriptor must NOT carry a path field.
        if PATH_FIELD.search(inner_txt):
            warn(f"mods/{name}/descriptor.mod: contains a 'path=' field (should live only in {name}.mod)")

        # The launcher descriptor must use a relative path.
        m = PATH_FIELD.search(outer_txt)
        if not m:
            err(f"mods/{name}.mod: no 'path=' field")
        else:
            path = m.group(1)
            if re.match(r"^[A-Za-z]:", path):
                err(f"mods/{name}.mod: absolute path '{path}' will break on other machines")
            elif path.replace("\\", "/").rstrip("/") != f"mod/{name}":
                warn(f"mods/{name}.mod: path='{path}' (expected 'mod/{name}')")


# --------------------------------------------------------------------------
# 4. Referenced tfast_ art assets exist
# --------------------------------------------------------------------------

TEXTURE = re.compile(r'"(gfx/[^"]*\.(?:dds|tga|png))"', re.I)


def check_assets() -> None:
    for mod_dir in sorted(p for p in MODS.iterdir() if p.is_dir()):
        for txt in sorted(mod_dir.rglob("*.txt")):
            try:
                text = txt.read_text(encoding="utf-8-sig", errors="replace")
            except OSError:
                continue
            for match in TEXTURE.finditer(text):
                asset = match.group(1)
                if "tfast" not in asset.lower():
                    continue  # vanilla or third-party; cannot verify here
                if not (mod_dir / asset).exists():
                    err(f"{rel(txt)}: references missing asset '{asset}'")


# --------------------------------------------------------------------------
# 5. Stray files
# --------------------------------------------------------------------------

BAD_SUFFIXES = {".bak", ".orig", ".rej", ".tmp", ".log", ".ck3"}


def check_stray_files() -> None:
    for path in MODS.rglob("*"):
        if path.is_file() and path.suffix.lower() in BAD_SUFFIXES:
            err(f"{rel(path)}: should not be committed")


def main() -> int:
    if not MODS.is_dir():
        print(f"error: {MODS} not found — run this from the repository root", file=sys.stderr)
        return 1

    check_localization()
    check_braces()
    check_descriptors()
    check_assets()
    check_stray_files()

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"\nOK - 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
