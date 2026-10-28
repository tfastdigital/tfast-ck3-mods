# Compatibility

What each mod touches, and what it will fight with.

---

## At a glance

| Mod                      | Files touched                                                                                                          | Kind of change                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `tfast_shattered_crowns` | Many — characters, titles, faith, culture, decisions, events, on_actions, situations, men-at-arms, modifiers, GUI, art | **Additive, plus heavy use of the British Isles** |
| `tfast_africa`           | Decisions, traits, modifiers, localization                                                                             | Purely additive                                   |
| `tfast_history`          | Decisions, events, localization                                                                                        | Purely additive                                   |
| `tfast_funpack`          | Decisions, traits, modifiers, localization                                                                             | Purely additive                                   |
| `tfast_ai_suite`         | Decisions, events, GUI, localization                                                                                   | Purely additive; player-only                      |
| `tfast_lategame`         | `common/defines/` — 4 population-growth keys                                                                           | Partial define override                           |
| `tfast_performance`      | `common/defines/ai/zz_tfast_performance_ai.txt` — 16 AI keys                                                           | Partial define override                           |
| `tfast_smarter_ai`       | `common/defines/ai/00_ai.txt` — 16 AI keys                                                                             | **Rewrites a vanilla file**                       |
| `tfast_ui_readable`      | `gui/preload/fonts.gui` — 4 templates                                                                                  | **Rewrites a vanilla file**                       |
| `tfast_template`         | Nothing meaningful                                                                                                     | Scaffold                                          |

"Partial define override" means the file redefines specific keys and leaves
everything else to vanilla. Defines are merged at the key level, so a partial
override is safe and does not wipe the rest of the file.

---

## The one real conflict

### `tfast_performance` vs `tfast_smarter_ai`

These two tune **the same 16 AI keys in opposite directions**.

|                      | `tfast_performance` | `tfast_smarter_ai` |
| -------------------- | ------------------- | ------------------ |
| Recalculation timers | Longer              | Shorter            |
| Options weighed      | Fewer               | More               |
| Effect on the game   | Faster, dumber AI   | Slower, sharper AI |
| Difficulty           | Lower               | **Higher**         |

Enabling both produces whichever one merges last, which is not something you
want to reason about. **Enable exactly one.**

`tfast_performance` is written to `zz_tfast_performance_ai.txt` so it sorts last
within its load group, but load order inside a group is not a guarantee worth
relying on. Pick one.

---

## Additive mods

Everything else in this repository only **adds** game objects under its own ID
namespace (`tfast_`, `tfast_sc_`, `tfast_sct_`). None of them reuse vanilla IDs.
They can be enabled together in any combination and any order.

---

## Shattered Crowns and total conversions

`tfast_shattered_crowns` is where compatibility stops being trivial, because it
does not just add — it **places characters and titles in the British Isles** and
gives them history at multiple start dates.

### What it does to the map

- Creates twelve immortal Hollow rulers and gives them counties and higher titles.
- Creates a Targaryen ancestor line and consolidates scattered Welsh houses into
  one.
- Adds title history at `866.1.1`, `1066.9.14` and `1178.9.30`.
- Asserts permanent seats at every start date, reclaiming them quarterly.

### What that collides with

| Collision                                                                      | Result                                                                             |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Any mod that also rewrites Welsh or English title history at 866 / 1066 / 1178 | Last one loaded wins, and the loser's characters may end up landless or duplicated |
| Any mod that adds characters with the same IDs                                 | Duplicate definitions; one silently overwrites the other                           |
| Total conversions (AGOT, LotR, etc.)                                           | Expect title-history and character-ID collisions. **Test in a new save.**          |
| Mods that redefine `house_british_isles_mathrafal`                             | The Targaryen consolidation targets that house; redefining it breaks the merge     |

The mod does **not** require AGOT or any other mod. Those were read as reference
only — see [NOTICE.md](../NOTICE.md).

---

## Saves

| Situation                                                                | Safe?                                                                                                                                               |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adding an additive mod to an existing save                               | Yes                                                                                                                                                 |
| Removing an additive mod                                                 | Yes, though events in progress may linger                                                                                                           |
| Adding Shattered Crowns to an existing save                              | **Mostly** — the situation director starts itself once per world and covers existing saves. Permanent seats are asserted on the next quarterly tick |
| Removing Shattered Crowns                                                | Not recommended. Hollow characters and titles are now in the save                                                                                   |
| Changing between `tfast_performance` and `tfast_smarter_ai` mid-campaign | Yes; defines are re-read on load                                                                                                                    |

Ironman saves behave like any other save with mods — but mods disable
achievements regardless.

---

## Achievements

Any enabled mod disables achievements. There is no workaround, and this
repository does not claim one.

---

## Load order

There is no required order. If you want to be careful:

1. Base game
2. `tfast_shattered_crowns`
3. Additive content mods (Africa, History, Fun Pack, AI Suite)
4. Defines mods — **one** of `tfast_performance` / `tfast_smarter_ai`, plus
   `tfast_lategame` if wanted
5. `tfast_ui_readable` last (GUI overrides are safest on top)

---

## Reporting a compatibility problem

Include the full mod list from your playset, in order, plus the relevant
`error.log` lines. "It crashed with 40 mods" is not actionable; "it crashed when
`tfast_shattered_crowns` and _X_ were both enabled, here is the log" is.
