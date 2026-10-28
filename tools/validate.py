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

# Filled by check_localization(), consumed by check_loc_references().
LOC_KEYS: set[str] = set()


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

# A language header must occupy its line on its own. CK3 does NOT accept
#     l_english: some_key:0 "text"
# on one line: it fails to open the language block, and every key after it is
# rejected with "Trying to import a localization key outside of a language".
# The result is raw keys showing in game, with no error about the header itself.
LANG_HEADER = re.compile(r"^\s*l_[a-z]{2,}(?:_[A-Za-z]+)?\s*:\s*(?P<rest>\S.*)?$")


def check_localization() -> None:
    global LOC_KEYS
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

            headers = 0
            for lineno, line in enumerate(text.splitlines(), 1):
                if line.lstrip().startswith("#"):
                    continue

                # --- language header must be alone on its line ---------------
                hm = None if LOC_LINE.match(line) else LANG_HEADER.match(line)
                if hm:
                    headers += 1
                    if hm.group("rest"):
                        err(
                            f"{rel(yml)}:{lineno}: language header must be alone on its "
                            f"line, found {hm.group('rest')!r} after it. CK3 then rejects "
                            f"every key in this file and the raw keys show in game."
                        )
                    continue

                m = LOC_LINE.match(line)
                if not m:
                    continue
                key = m.group(1)
                LOC_KEYS.add(key)
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

            if headers > 1:
                warn(f"{rel(yml)}: {headers} language header lines (expected exactly 1)")


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


# --------------------------------------------------------------------------
# 6. Localization references: every key a script asks for must exist
# --------------------------------------------------------------------------
# A missing key does not break the load, it just renders the raw key in game
# (an event with no story, a decision titled "tfast_thing"). That is invisible
# in error.log on a release build, so it is checked statically here.

EVENT_DECL = re.compile(r"^\s*([a-z][a-z0-9_]*\.\d+)\s*=\s*\{\s*$")
EVENT_OPTION = re.compile(r"^\s*name\s*=\s*([a-z][a-z0-9_]*\.\d+\.[a-z0-9]+)\b")
TOOLTIP_KEY = re.compile(r"^\s*custom_tooltip\s*=\s*(?:key\s*=\s*)?([A-Za-z0-9_.\-]+)")
DESC_TITLE = re.compile(r"^\s*(?:desc|title|desc_extra|selection_tooltip|effect_desc|cooldown_desc)\s*=\s*([A-Za-z0-9_.\-]+)\s*$")
SCRIPT_DIRS = ("events", "common/decisions", "common/character_interactions",
               "common/modifiers", "common/on_action", "common/scripted_triggers",
               "common/scripted_effects", "common/decisions_groups")


def _referenced_keys(path: Path, text: str):
    """Yield (lineno, key) pairs a script file references by name."""
    lines = text.splitlines()
    for lineno, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue

        m = EVENT_DECL.match(line)
        if m:
            ev = m.group(1)
            # A hidden event is never drawn, so it needs no title.
            if not _is_hidden_event(lines, lineno - 1):
                yield lineno, f"{ev}.t"
            continue

        m = EVENT_OPTION.match(line)
        if m:
            yield lineno, m.group(1)
            continue

        m = TOOLTIP_KEY.match(line)
        if m and m.group(1) not in ("yes", "no"):
            yield lineno, m.group(1)
            continue

        m = DESC_TITLE.match(line)
        if m:
            key = m.group(1)
            if key and key not in ("yes", "no") and not key.isdigit():
                yield lineno, key


def _is_hidden_event(lines: list[str], start: int) -> bool:
    """True when the event block opening at `start` declares hidden = yes."""
    depth = 0
    for line in lines[start:]:
        code = COMMENT.sub("", line)
        if re.match(r"^\s*hidden\s*=\s*yes\s*$", code):
            return True
        depth += code.count("{") - code.count("}")
        if depth <= 0 and line is not lines[start]:
            return False
    return False


def check_loc_references() -> None:
    seen: set[tuple[str, str]] = set()
    for mod_dir in sorted(p for p in MODS.iterdir() if p.is_dir()):
        for sub in SCRIPT_DIRS:
            d = mod_dir / sub
            if not d.is_dir():
                continue
            for script in sorted(d.rglob("*.txt")):
                try:
                    text = script.read_text(encoding="utf-8-sig")
                except (UnicodeDecodeError, OSError):
                    continue
                for lineno, key in _referenced_keys(script, text):
                    if key in LOC_KEYS:
                        continue
                    # Only flag mod-owned keys; vanilla keys are defined elsewhere.
                    if not key.startswith("tfast"):
                        continue
                    if (str(script), key) in seen:
                        continue
                    seen.add((str(script), key))
                    err(
                        f"{rel(script)}:{lineno}: no localization for '{key}' "
                        f"(the raw key will show in game)"
                    )
def _block_end(lines: list[str], start: int) -> int:
    """Index one past the closing brace of the block opened on `start`."""
    depth = 0
    for idx in range(start, len(lines)):
        code = COMMENT.sub("", lines[idx])
        depth += code.count("{") - code.count("}")
        if depth <= 0 and idx > start:
            return idx
        if depth <= 0 and idx == start and "}" in code:
            return idx
    return len(lines)


def check_event_descriptions() -> None:
    """A visible event with no `desc` renders an empty story panel.

    `hidden = yes` events never draw a window, so they legitimately have no
    text. Everything else must carry a description, whether as a plain key or
    as a `desc = { triggered_desc = ... }` block.
    """
    desc_line = re.compile(r"^\s*desc\s*=")
    for mod_dir in sorted(p for p in MODS.iterdir() if p.is_dir()):
        d = mod_dir / "events"
        if not d.is_dir():
            continue
        for script in sorted(d.rglob("*.txt")):
            try:
                text = script.read_text(encoding="utf-8-sig")
            except (UnicodeDecodeError, OSError):
                continue
            lines = text.splitlines()
            for idx, line in enumerate(lines):
                m = EVENT_DECL.match(line)
                if not m:
                    continue
                if _is_hidden_event(lines, idx):
                    continue
                end = _block_end(lines, idx)
                body = (COMMENT.sub("", ln) for ln in lines[idx + 1 : end])
                if any(desc_line.match(ln) for ln in body):
                    continue
                err(
                    f"{rel(script)}:{idx + 1}: event '{m.group(1)}' has no desc "
                    f"and is not hidden (it would show an empty story panel)"
                )


def main() -> int:
    if not MODS.is_dir():
        print(f"error: {MODS} not found — run this from the repository root", file=sys.stderr)
        return 1

    check_localization()
    check_loc_references()
    check_event_descriptions()
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
