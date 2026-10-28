# Contributing

Thanks for being here. This repository is public because CK3 modding gets better
when more people can read the scripts, argue about balance, and fix each other's
scope bugs.

You do not have to write code to help. Playing a campaign and writing down what
broke is genuinely one of the most valuable contributions available right now —
see [docs/TESTING_STATUS.md](docs/TESTING_STATUS.md) for how much is still
unplayed.

---

## Ways to contribute

|                     |                                                                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Play and report** | Start a campaign, enable a mod, and tell us what happened. Screenshots of `Documents/Paradox Interactive/Crusader Kings III/logs/error.log` are gold. |
| **Localization**    | Typos, tone, missing keys, better prose. These files are plain text.                                                                                  |
| **Balance**         | Any decision whose cost, cooldown, or reward feels wrong. Bring numbers.                                                                              |
| **Bug fixes**       | Script bugs, scope errors, invalid modifiers, missing loc keys.                                                                                       |
| **New content**     | New decisions, events, traits, systems. Open an issue first so nobody duplicates work.                                                                |
| **Art**             | Replacing the placeholder icons in [NOTICE.md](NOTICE.md) with original work would be a real improvement.                                             |

---

## Repository layout

```
mods/                     One folder per mod — this is a CK3 mod directory
  tfast_<name>/
    descriptor.mod        In-folder descriptor (no path= field)
    common/               Scripted content
    events/               Event files
    localization/english/ Localization
    gfx/                  Art (DDS)
    gui/                  GUI overrides
    history/              Characters and titles
    docs/                 Design notes for that mod
  tfast_<name>.mod        Launcher descriptor (relative path=)
docs/                     Repo-wide documentation
tools/                    Validation and helper scripts
```

`mods/` deliberately mirrors the real CK3 mod directory. Copy it in, and the
launcher sees everything. Never add a level of nesting there.

---

## Workflow

1. **Open an issue** describing the change, unless it is a one-line typo fix.
2. Fork, then branch: `feature/hollow-winter-tune`, `fix/scope-root-on-action`.
3. Make the change. Bump the mod's `version` in **both** `descriptor.mod` and
   `tfast_<name>.mod` if you changed behaviour.
4. Run the validator: `python tools/validate.py`
5. Add an entry to [CHANGELOG.md](CHANGELOG.md) under _Unreleased_.
6. Open a pull request. Describe **what you tested and how**, or say plainly
   that you did not test it.

---

## CK3 rules that will otherwise cost you an evening

These are the mistakes this project has already made, so you do not have to.

### Encoding

- **Localization `.yml` files must be saved as UTF-8 _with BOM_.** Without the
  BOM, every key in the file silently fails to load and the game shows raw
  `tfast_sc_...` keys. This is the single most common cause of "my text does not
  appear".
- Do not let an editor strip the BOM. `.gitattributes` in this repo sets
  `* -text` precisely so Git never rewrites line endings or encoding behind your
  back.
- Keep one localization file per mod per language, named
  `tfast_<prefix>_l_english.yml`, with `l_english:` as the first line.

### Scopes

- **`root` can be unset inside `on_action` effects.** If you need the acting
  character, `save_scope_as = x` first and use `scope:x`. This exact bug once
  silently broke every Hollow title grant in the mod.
- `becomes_vassal_of` does not exist. To change a liege use:
  ```txt
  change_liege = { liege = scope:new_liege change = root }
  ```
- Inside a great-project `on_plan_build`, the scope is the **project**, not the
  ruler. Save the sponsor earlier and refer to it.
- Effects and triggers that take `$PARAM$` should be assumed to run in an
  arbitrary scope. Never reference `root` inside a `scripted_effect` you exported
  for reuse.

### History

- **Negative years are invalid** in character history (`-99999133.1.1` will
  silently fail). Characters with impossible birth dates do not exist, and every
  title that points at them reports "no such character".
- `liege = ` inside title history expects a **title**, not a character. Use
  `liege = 0` for independent.
- Dynasty houses cannot be deleted through script. They can only be emptied or
  redefined.

### Localization

- Inside trait and modifier descriptions, use `[CHARACTER.GetHerHis]`, not
  `[ROOT.GetHerHis]`. `ROOT` is evaluated in the tooltip scope and produces
  thousands of log errors.
- A key may only be defined **once across all loaded files**. If you need to
  change a vanilla key, put the file under `localization/english/replace/`.
- Every `add_character_modifier`, `add_county_modifier`, trait, and decision
  needs a name **and** a description key, or the log fills with missing-key
  errors.

### Naming

| Prefix       | Used for                                               |
| ------------ | ------------------------------------------------------ |
| `tfast_`     | All game-object IDs in the TFAST mods                  |
| `tfast_sc_`  | Shattered Crowns scripts and objects                   |
| `tfast_sct_` | Shattered Crowns Targaryen / world-tier content        |
| namespace    | `tfast_sc` and `tfast_sct` are reserved; pick your own |

Never reuse a vanilla ID unless you are deliberately overriding it, and say so
in the pull request.

---

## Validation

```bash
python tools/validate.py
```

The script checks, for every file under `mods/`:

- `.yml` localization files are UTF-8 **with** BOM
- localization keys are not duplicated inside a mod
- `.txt` script files have balanced `{ }`
- no `\r\n\r\n\r\n` bloat or stray tab/space mixed indentation in `.txt`
- every referenced `gfx/...` path exists on disk
- `descriptor.mod` and `tfast_<name>.mod` agree on name and version

CI runs the same script on every pull request. It is intentionally conservative:
it fails only on things the game will actually choke on.

---

## Reporting a bug

Use the bug report template. Include:

1. Mod name and version (from `descriptor.mod`).
2. Game version and checksum.
3. What you expected, what happened.
4. Steps to reproduce — from a **new save** if possible.
5. The relevant lines from
   `Documents/Paradox Interactive/Crusader Kings III/logs/error.log`.

The last item is the one that turns a report into a fix. Errors in that log are
almost always a missing key, an unset scope, or an invalid modifier name, and
they are one-line fixes once they are visible.

---

## Commit messages

Conventional-ish, scoped by mod:

```
sc: fix unset root scope in crown grant
africa: add Nubian holy-site decision
ui: raise Font_Size_Medium to 20px
docs: correct testing status for Hollow winter
```

---

## Be decent

Assume good faith, criticise the code and not the person, and do not guess at
someone's intent when you can ask a question instead. Reports and pull requests
that violate this will be closed without discussion.
