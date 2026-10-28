## What this changes

<!-- One paragraph. What behaviour changes, and for which mod. -->

Mod(s) touched:
- [ ] `tfast_shattered_crowns`
- [ ] `tfast_africa`
- [ ] `tfast_history`
- [ ] `tfast_funpack`
- [ ] `tfast_ai_suite`
- [ ] `tfast_lategame`
- [ ] `tfast_performance`
- [ ] `tfast_smarter_ai`
- [ ] `tfast_ui_readable`
- [ ] `tfast_template`
- [ ] repository tooling / docs only

## Why

<!-- The problem. Link the issue if there is one: Closes #123 -->

## Testing

Be honest here — "not tested" is an acceptable answer and much more useful than a
vague claim.

- [ ] Ran `python tools/validate.py` — 0 errors
- [ ] Game loads with the mod enabled, no new `error.log` entries
- [ ] Played in game and observed the change (`RUNTIME_TESTED`)
- [ ] Played to the intended outcome on a clean save (`VERIFIED`)
- [ ] Not tested in game

If you tested in game, say what you did:

```txt

```

## Checklist

- [ ] `version` bumped in **both** `descriptor.mod` and `tfast_<name>.mod`, if behaviour changed
- [ ] New localization `.yml` files are UTF-8 **with BOM**
- [ ] New game-object IDs use the `tfast_` / `tfast_sc_` / `tfast_sct_` namespace
- [ ] No new `root` references inside `on_action` effects without `save_scope_as`
- [ ] `CHANGELOG.md` updated under *Unreleased*
- [ ] `docs/TESTING_STATUS.md` updated if a system's validation state changed
- [ ] No save files, logs, `.bak` files or absolute paths committed

## Breaking changes

<!--
Does this rename or remove an ID, change a variable's meaning, or otherwise
break an existing save? If yes, it needs a MAJOR version bump and a note here.
-->
