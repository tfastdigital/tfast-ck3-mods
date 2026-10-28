# Mod versions

Every mod carries its version in **two** places, which must always agree:

- `mods/tfast_<name>/descriptor.mod` — read by the mod itself
- `mods/tfast_<name>.mod` — read by the launcher

All mods declare `supported_version="1.20.*"`.

---

## Current versions

| Mod                      | Launcher name                                | Version   | Games                                                         | Content                                                                                |
| ------------------------ | -------------------------------------------- | --------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `tfast_shattered_crowns` | TFAST Shattered Crowns                       | **1.1.0** | Gameplay, Events, Character Interactions, Decisions, Religion | Survival epic: Hollow Dominion, Great Wall, Great Reckoning, Long Dark, Chosen Emperor |
| `tfast_africa`           | TFAST Africa — Historical Depth              | **1.0.0** | Gameplay, Events, Decisions, Culture, Religion                | 12 decisions, 6 traits, 12 modifiers                                                   |
| `tfast_history`          | TFAST History — Historic Acts & Institutions | **1.0.0** | Gameplay, Events, Decisions                                   | 35 historically grounded decisions                                                     |
| `tfast_funpack`          | TFAST Fun Pack — Court Life & Character      | **1.0.0** | Gameplay, Events, Character Interactions                      | 6 court decisions with real trade-offs                                                 |
| `tfast_ai_suite`         | TFAST AI Suite — Cheats & Automation         | **1.2.0** | Gameplay, Utilities, Fixes                                    | 5-page flag cheat menu (25 cheats) + automation                                        |
| `tfast_lategame`         | TFAST Late Game — Stability                  | **1.0.0** | Gameplay, Balance, Utilities                                  | 4 population-growth defines                                                            |
| `tfast_performance`      | TFAST Performance — Lean AI                  | **1.0.0** | Gameplay, Utilities                                           | 16 AI defines, cheaper AI                                                              |
| `tfast_smarter_ai`       | TFAST Smarter AI                             | **1.0.0** | Gameplay, Balance                                             | 16 AI defines, sharper AI                                                              |
| `tfast_ui_readable`      | TFAST UI Readable Fonts                      | **1.0.0** | Utilities                                                     | 4 font templates, ~+11%                                                                |
| `tfast_template`         | TFAST Template Mod                           | **1.0.0** | Gameplay, Utilities                                           | Empty scaffold                                                                         |

---

## Version history

| Date    | Mod                      | From → To                        | Reason                                                                |
| ------- | ------------------------ | -------------------------------- | --------------------------------------------------------------------- |
| 2026-10 | `tfast_shattered_crowns` | `0.x` → `1.0.0`                  | First public release: Hollow Dominion, walls, prophecy, the Reckoning |
| 2026-10 | `tfast_ai_suite`         | `1.0.0` → `1.1.0`                | Flag-gated cheat menu replaces the flat list of decisions             |
| 2026-10 | `tfast_shattered_crowns` | `1.0.0` → `1.1.0`                | Targaryen consolidation, Hollow war support, world-level events       |
| 2026-10 | `tfast_ai_suite`         | `1.1.0` → `1.2.0`                | Create-an-army, one-step men-at-arms, upgrade-everything cheats       |

---

## Version numbering

`MAJOR.MINOR.PATCH`, per mod, independently.

| Bump      | When                                                                                        |
| --------- | ------------------------------------------------------------------------------------------- |
| **MAJOR** | A save-breaking change: renamed or removed IDs, changed variable semantics, deleted content |
| **MINOR** | New content that an existing save can absorb: new decisions, events, systems                |
| **PATCH** | Bug fixes, localization, balance, typo — no new IDs                                         |

A mod's version is independent of the others'. `tfast_ai_suite` can be at
`1.2.0` while everything else is at `1.0.0`.

### Claiming game-version support

`supported_version` is bumped **after** the scripts have been re-checked against
the new data files, never before. If Paradox ships 1.21 and this repository still
says `1.20.*`, that means the mods have not been reviewed yet — it does not mean
they are broken. The safest move is to test on the old version or wait.

---

## File inventory

| Mod                      | Files | Size     | Notes                                 |
| ------------------------ | ----- | -------- | ------------------------------------- |
| `tfast_shattered_crowns` | ~199  | ~34 MB   | Most of the size is generated DDS art |
| `tfast_ai_suite`         | 24    | ~0.8 MB  | Includes its own icons                |
| `tfast_history`          | 12    | ~0.09 MB |                                       |
| `tfast_africa`           | 7     | ~0.04 MB |                                       |
| `tfast_funpack`          | 6     | ~0.02 MB |                                       |
| `tfast_lategame`         | 3     | ~0.01 MB |                                       |
| `tfast_performance`      | 3     | ~0.00 MB |                                       |
| `tfast_smarter_ai`       | 3     | ~0.01 MB |                                       |
| `tfast_template`         | 3     | ~0.00 MB |                                       |
| `tfast_ui_readable`      | 3     | ~0.01 MB |                                       |
