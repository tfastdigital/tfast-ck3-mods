# Roadmap

What is next, what is deliberately not next, and what will never happen.

Ordered by value-per-hour, not by ambition. Anything at the top of "Now" is fair
game to open a pull request against.

---

## Now — highest value

| Item                                                     | Why first                                                                                                                                                  |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Runtime test a full Reckoning**                        | Almost everything is `STATICALLY_VALIDATED`. One played campaign is worth more than any amount of code review. See [TESTING_STATUS.md](TESTING_STATUS.md). |
| **Verify the Targaryen war CB path**                     | The custom CB resolves against non-Targaryens. The Targaryen-specific branch is unconfirmed.                                                               |
| **Replace the two placeholder icons**                    | `tfast_sct_dragon_egg.dds` and `tfast_sct_dragon_throne_decision.dds` are derived from third-party art. See [NOTICE.md](../NOTICE.md).                     |
| **`tcastle_03` / `tcastle_04` on holder-less provinces** | Noisy `error.log` lines on some starts. A limit check on the build effect should clear it.                                                                 |
| **Confirm the Hollow Tide situation appears**            | The director is meant to start it once per world, including existing saves. Not confirmed.                                                                 |
| **Hollow Tide icon size**                                | Confirm it matches the situation-type icon dimensions.                                                                                                     |

---

## Next — content

### Shattered Crowns

| Item                                     | Notes                                                                                                                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Signature abilities for all ten children | Morvath (bounded reinforcements) and Kaedryn (frost) are live; the other eight are described in the design doc but not scripted |
| Artifact raids / stolen relics           | Documented as V2; no artifact types are shipped yet                                                                             |
| More Hollow men-at-arms                  | Six exist, capped; there is room for two or three with distinct roles                                                           |
| Targaryen cadet branches                 | Currently one house with a house flag for non-heads. A proper cadet-house system would be better history and better gameplay    |
| Dragon growth stages                     | Eggs and hatching exist; a growth path from hatchling to adult does not                                                         |
| Second wall line                         | The Wall is one project. A southern or eastern line would change the Reckoning materially                                       |

### Africa

| Item                                                       | Notes                                                 |
| ---------------------------------------------------------- | ----------------------------------------------------- |
| Holy-site content for the seven vanilla African holy sites | The sites exist; almost nothing references them       |
| Sub-Saharan building chains                                | Vanilla has no dedicated script file for Africa       |
| More cultures covered                                      | 16 vanilla African cultures; the mod touches a subset |

### History

| Item              | Notes                                                                        |
| ----------------- | ---------------------------------------------------------------------------- |
| More institutions | 35 exist; the two obvious gaps are Islamic and Chinese institutional history |
| Regional variants | The same decision should read differently in Scandinavia and in Persia       |

---

## Later — infrastructure

| Item                                   | Notes                                                                                                                                             |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Benchmark harness for the defines mods | Nobody has measured whether `tfast_performance`, `tfast_smarter_ai` or `tfast_lategame` help. Tick-time and frame-time numbers, before and after. |
| Localization: more languages           | Everything is English today                                                                                                                       |
| Automated in-game smoke test           | Even a scripted "load a save, advance one year, dump `error.log`" would catch a whole class of regressions                                        |

---

## Deliberately rejected

Recorded so the same arguments do not have to be had twice.

| Idea                                                  | Why not                                                                                                                                                                                                   |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A map-impassable wall**                             | Not possible in the engine. CK3 army pathfinding cannot be walled off by any mod. The wall gates the mod's own scripted raids and slows real sieges through fort-level county modifiers. No false claims. |
| **Playable Hollow**                                   | The Hollow are AI rulers created by script. Making them playable means redesigning the whole crisis, and it removes the thing that makes them frightening.                                                |
| **"Fixes lag"**                                       | No mod fixes late-game slowdown. It is thousands of living characters, each evaluated by the AI, plus pathfinding. `tfast_lategame` reduces one input to that cost and says so in its own README.         |
| **Banking and loans**                                 | Left to the Counting House workshop mod (pdx_156899), which already does it. Shipping a second implementation means loading both.                                                                         |
| **Population ledger**                                 | Left to Population Foundation (pdx_162659). Same reasoning.                                                                                                                                               |
| **Workforce / famine / roads / currency / espionage** | Phase 7, postponed. Each is a system, not a decision, and none of them would be testable at the current validation level.                                                                                 |
| **Cheats in the historical mods**                     | `tfast_ai_suite` exists so you can enable historical content without also enabling cheats. Keeping them separate was the point.                                                                           |

---

## Not planned at all

- Anything that deletes or replaces vanilla characters outside the British Isles.
- Anything that silently changes save format.
- Anything that requires a specific DLC.
- Anything that grants the AI free gold, troops, or cheats rather than changing
  how it chooses.

---

## How to propose something

Open an issue with the **feature request** template and say:

1. What the player does.
2. What changes in the world because of it.
3. What it costs them.
4. How we would know it works.

Item 4 is the one that usually decides whether a feature gets built. A feature
nobody can verify is a feature that becomes another `STATICALLY_VALIDATED` row
forever.
