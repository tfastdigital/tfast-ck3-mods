# Testing status

This page exists so nobody has to guess how much of this repository has actually
been played.

| Status                 | Meaning                                                                                                                                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `VERIFIED`             | Played through to the intended outcome, on a clean save, more than once.                                                                                                                                               |
| `RUNTIME_TESTED`       | Observed working in a launched game, but not driven to completion.                                                                                                                                                     |
| `STATICALLY_VALIDATED` | Every effect, trigger, scope, callback, modifier key, faith/rite/doctrine key, MAA field, CB field and event structure was checked against the installed 1.20 data files. No validator or load errors. **Not played.** |
| `POSTPONED`            | Designed, not built.                                                                                                                                                                                                   |
| `REJECTED`             | Considered and refused, with the reason recorded.                                                                                                                                                                      |

**Read this line before anything else: the bulk of the recent work in this
repository is `STATICALLY_VALIDATED`, not `VERIFIED`.** The mods load and parse
cleanly. Many of the newer systems have never been played through to their
intended outcome. That is the honest state of the project, and it is why
"play a campaign and report what breaks" is the first entry in
[CONTRIBUTING.md](../CONTRIBUTING.md).

---

## tfast_shattered_crowns

### Core systems

| System                                               | Status                 | Notes                                                                                                     |
| ---------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------- |
| Hollow Dominion, ten children, closed bloodline      | `RUNTIME_TESTED`       | Loaded without script errors; existence of all twelve rulers confirmed from title history                 |
| Hidden dynasty with its own faith (Hollow Communion) | `STATICALLY_VALIDATED` | Faith, rite and doctrines checked against 1.20 keys                                                       |
| Overlord is never permanently destroyed              | `STATICALLY_VALIDATED` | `on_death` registry restores the seat and the character                                                   |
| Hollow mutual war support                            | `STATICALLY_VALIDATED` | `on_war_started` hook; every landed Hollow joins the matching side, 150+ gold sends 100 to the war leader |
| Hollow vengeance wars against Targaryens             | `STATICALLY_VALIDATED` | 10-year cooldown, readiness ≥ 50                                                                          |
| Permanent seats, reclaimed quarterly                 | `STATICALLY_VALIDATED` | Runs at every start date; reclaims lost seat baronies                                                     |
| All Hollow castles driven to max building level      | `STATICALLY_VALIDATED` | Nine building chains, level 8, runs at start and quarterly                                                |
| Hollow −100 opinion of every Targaryen               | `STATICALLY_VALIDATED` | Applied to every Hollow-flagged character                                                                 |

### Targaryen systems

| System                                                 | Status                 | Notes                                                              |
| ------------------------------------------------------ | ---------------------- | ------------------------------------------------------------------ |
| Consolidation into one Targaryen house                 | `STATICALLY_VALIDATED` | Scattered Welsh houses folded; `set_house` on every flagged member |
| Numbered names II–X                                    | `STATICALLY_VALIDATED` | Collision counter per given name                                   |
| English + Targaryen female given names                 | `STATICALLY_VALIDATED` | 8 English, 10 Targaryen, shared male pool                          |
| Platinum-white hair gene                               | `STATICALLY_VALIDATED` | DNA data forces the hair colour; not visually confirmed in game    |
| Dynasty head keeps dynasty arms, others get house flag | `STATICALLY_VALIDATED` | `tfast_sc_targaryen_realm_flags_effect`                            |
| Dragon eggs and hatching                               | `STATICALLY_VALIDATED` | `tfast_sct.0001` / `.0002`                                         |
| Dragon Throne decision                                 | `STATICALLY_VALIDATED` | 500 gold, 200 prestige, kingdom tier, 20-year modifier             |

### Crisis systems

| System                                                      | Status                 | Notes                                                                   |
| ----------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------- |
| Scripted raids: warning, defence stance, prisoners, frost   | `RUNTIME_TESTED`       | Earlier session; not re-run since the world tick was added              |
| Great Reckoning: foretelling, real war, three bounded waves | `STATICALLY_VALIDATED` | Custom CB checked; **the CB accepting Targaryen targets is unverified** |
| Siege wall gate                                             | `STATICALLY_VALIDATED` | Blocks the mod's scripted raids only                                    |
| Great Wall project: five stages, upkeep, repair             | `STATICALLY_VALIDATED` | Wall refits and dismantle in the same file                              |
| Last Watch recruitment                                      | `STATICALLY_VALIDATED` |                                                                         |
| Chosen Emperor: hidden mark, awakening, three tiers         | `STATICALLY_VALIDATED` |                                                                         |
| True Death (awakened Chosen only)                           | `STATICALLY_VALIDATED` | Overlord can only be sealed                                             |
| The Long Dark and the uprising                              | `STATICALLY_VALIDATED` | Game rule gated; resistance thresholds 8 and 14                         |
| The Hollow Tide situation window                            | `STATICALLY_VALIDATED` | **Confirm it actually appears after the first yearly tick**             |
| Six Hollow men-at-arms                                      | `STATICALLY_VALIDATED` |                                                                         |
| Mercenaries: three gold-scaled tiers                        | `STATICALLY_VALIDATED` |                                                                         |
| Hollow goals: vendetta / hunt / blood / terror / treasure   | `STATICALLY_VALIDATED` |                                                                         |
| Hiding, and the hunt that finds you                         | `STATICALLY_VALIDATED` |                                                                         |

### World tier

| System                                     | Status                 | Notes                                                   |
| ------------------------------------------ | ---------------------- | ------------------------------------------------------- |
| Yearly world tick for every playable ruler | `STATICALLY_VALIDATED` | Resisting-the-Hollow modifier, dragon-at-court modifier |
| Pale riders (`tfast_sct.0050` / `.0051`)   | `STATICALLY_VALIDATED` | Readiness ≥ 40, 5-year flag                             |
| Hollow winter (`tfast_sct.0060`)           | `STATICALLY_VALIDATED` | Readiness ≥ 70, 30% chance, 30-year scale               |
| Coalition decision                         | `STATICALLY_VALIDATED` | 300 gold, 100 prestige, duchy tier, 10-year cooldown    |

### Facilities

| System                        | Status                 | Notes                                         |
| ----------------------------- | ---------------------- | --------------------------------------------- |
| Automation menu (7 switches)  | `STATICALLY_VALIDATED` | Player-only; open/close flags                 |
| In-game handbook (8 chapters) | `STATICALLY_VALIDATED` | Same flag-menu pattern                        |
| Generated flavor pool         | `STATICALLY_VALIDATED` | 24 lines via `tools/tfast_flavor_deepseek.py` |

---

## Economy and resources

| System                                        | Status                 | Notes                                                                                                           |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| Hidden gold deposits                          | `RUNTIME_TESTED`       | One-time seed only; debug log confirmed it during a campaign start                                              |
| Prospecting, one gold working                 | `STATICALLY_VALIDATED` | Not clicked in game                                                                                             |
| Iron, stone, timber, grain                    | `STATICALLY_VALIDATED` | Same tax path as gold; Aetherstone postponed                                                                    |
| Foreign scouting                              | `STATICALLY_VALIDATED` | One neighbouring county; no land taken                                                                          |
| Family chest, named keeper                    | `STATICALLY_VALIDATED` | Gold leaves the treasury and is paid once on death                                                              |
| Banking and loans                             | `REJECTED`             | Left to the Counting House workshop mod (pdx_156899), already installed — not copied, so it is not loaded twice |
| Population ledger                             | `REJECTED`             | Left to Population Foundation (pdx_162659)                                                                      |
| Workforce, famine, roads, currency, espionage | `POSTPONED`            | Phase 7                                                                                                         |
| Economy artwork                               | `POSTPONED`            | None generated                                                                                                  |

---

## Other mods

| Mod                 | Status                 | Notes                                                                   |
| ------------------- | ---------------------- | ----------------------------------------------------------------------- |
| `tfast_ai_suite`    | `STATICALLY_VALIDATED` | Validator exit 0; the 23 cheats have not been clicked in a running game |
| `tfast_africa`      | `STATICALLY_VALIDATED` | 12 decisions parse; not clicked                                         |
| `tfast_history`     | `STATICALLY_VALIDATED` | 35 decisions parse; not clicked                                         |
| `tfast_funpack`     | `STATICALLY_VALIDATED` | 6 decisions parse; not clicked                                          |
| `tfast_lategame`    | `STATICALLY_VALIDATED` | Defines are key-level overrides; not benchmarked                        |
| `tfast_performance` | `STATICALLY_VALIDATED` | Not benchmarked                                                         |
| `tfast_smarter_ai`  | `STATICALLY_VALIDATED` | Not benchmarked                                                         |
| `tfast_ui_readable` | `STATICALLY_VALIDATED` | Four templates raised; not opened in game                               |
| `tfast_template`    | `STATICALLY_VALIDATED` | Empty scaffold                                                          |

> **On the AI and performance mods:** none of them have been benchmarked. They
> change defines; nobody has measured the result. If you have frame-time or
> tick-time numbers, they would be genuinely valuable — see the performance issue
> template.

---

## Known open problems

Things that are known to be wrong or unconfirmed. These are not hidden.

| Problem                                                           | Severity | Notes                                                                                   |
| ----------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------- |
| `tfast_sc_reckoning_war` CB against a Targaryen target            | Medium   | Declares and resolves against non-Targaryens; the Targaryen-specific path is unverified |
| `tcastle_03` / `tcastle_04` build errors on holder-less provinces | Low      | Appears in `error.log` on some starts; cosmetic but noisy                               |
| `norse_building_gfx` sequence warning in Hollow culture           | Low      | Cosmetic                                                                                |
| `tfast_sct_dragon_egg.dds` modifier icon dimensions               | Low      | May not match the expected modifier icon size                                           |
| No benchmarking of any defines-only mod                           | Medium   | Unknown whether the performance mods actually help                                      |
| Hollow Tide situation may not appear on existing saves            | Medium   | Director is supposed to start it once per world; unconfirmed                            |

---

## How to help

The single most valuable contribution right now:

1. Start a **new** save on 1.20.x.
2. Enable **only** `tfast_shattered_crowns`.
3. Play until the first Great Reckoning.
4. Attach the relevant lines from
   `Documents/Paradox Interactive/Crusader Kings III/logs/error.log`, or say
   "no errors" — that is equally useful information.

That single report would move more rows from `STATICALLY_VALIDATED` to
`RUNTIME_TESTED` than any amount of code review.
