# Compatibility report

Inspected 12 October 2026.

## Game

`C:\Games\ckIII`, launcher `version` 1.20.0.3 (Crozier). Mod `supported_version` is `1.20.*`.

## This mod

Scripts live under `common/`, `events/`, and `localization/english/`. New gold files use the `tfast_sc_` prefix and new event ids `tfast_sc.1000` through `tfast_sc.1002`. They do not replace vanilla files.

The seed runs from the existing `on_game_start_after_lobby` hook, beside the dynasty capture. The yearly rumor runs from the existing player yearly effect. Neither adds a daily global loop.

## Other installed TFAST mods

`tfast_africa`, `tfast_ai_suite`, `tfast_funpack`, `tfast_history`, `tfast_lategame`, `tfast_smarter_ai`, `tfast_template`, `tfast_ui_readable`.

None of those descriptors is an economy, mining, or banking mod. No sibling file was edited.

## Vanilla mines

`generic_gold_mines_01` and its higher tiers are real buildings in `common/buildings/00_special_mines.txt`. `has_building_or_higher` is a real trigger. Counties that already have that building are not given a hidden deposit. Opening a working later checks again and refuses a second tax modifier.

## Hollow rules

No gold decision is available to AI. Nothing in this pass lets a mortal join the Hollow, kills the Overlord, or changes True Death.

## Known non-conflicts that the static checker still flags

The checker looks for trait icons only in the vanilla icon folder, so the mod's own `tfast_sc_icon_` files are reported missing. They are in the mod. `holy_sites_min` is a documented religion-type field in `_religion_types.info`, not a trigger. Those two reports are not gold-system faults.
