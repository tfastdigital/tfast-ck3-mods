# TFAST Smarter AI

Makes the **Crusader Kings III** AI react faster and choose better. For
**1.20.x**.

## Read this before enabling

**This mod changes game balance on purpose.** Unlike `tfast_ai_suite` and
`tfast_history`, which only *add* things, this one rewrites a vanilla file.
Two consequences:

1. **It makes the game harder, not easier.** A more competent AI expands
   better, defends better, and fights on when it would previously have
   collapsed. Your vassals get smarter too.
2. **It is a file override.** See *Maintenance* below.

If you want an easier game, use `tfast_ai_suite` instead. This mod is the
opposite.

## What it changes

Only 16 settings inside `common/defines/ai/00_ai.txt`. Nothing grants the AI
free gold, troops or cheats — every change makes it **react sooner, weigh more
options, or stop clinging to a worse choice**.

### Reaction speed

The AI recalculates its plans on per-tier timers. Vanilla runs the low tiers
very slowly, which is why a barony- or county-tier AI feels asleep.

| Setting | Vanilla | Now |
|---|---|---|
| `SHORT_TASK_TICK` | 7 / **30** / 14 | 7 / **14** / 7 |
| `MEDIUM_TASK_TICK` | 30 / **180** / 60 | 30 / **90** / 30 |
| `LONG_TASK_TICK` | 60 / **1095** / 180 | 60 / **365** / 90 |
| `RARE_TASK_TICK` | 180 / **720** / 360 | 180 / **365** / 180 |
| `STRATEGY_TASK_TICK` | 180 / **720** / 360 | 180 / **365** / 180 |

*(values are barony / county for the bolded columns)*

### Military

| Setting | Vanilla | Now | Effect |
|---|---|---|---|
| `CHECK_ADMIN_ARMIES_COOLDOWN` | 360 | 180 | Administrative realms raise armies twice as often |
| `RAISE_LEVIES_COOLDOWN` | 180 | 90 | Raises levies twice as readily |
| `RAISE_TROOPS_MIN_RATIO_OF_ENEMY` | 0.5 | 0.35 | Fights on when outnumbered instead of passively losing |

### Threat assessment

| Setting | Vanilla | Now | Effect |
|---|---|---|---|
| `THREAT_MIN_POWER_RATIO` | 0.5 | 0.35 | Spots rising threats earlier, so it prepares sooner |

### Diplomacy and marriage

| Setting | Vanilla | Now | Effect |
|---|---|---|---|
| `MAX_NUMBER_OF_DIPLO_VALUES` | …6/8/10/12 | …12/16/20/24 | Weighs twice as many counterparties |
| `MAX_NUMBER_OF_COURTS_TO_SEARCH_FOR_SPOUSES` | …16/32/32/32 | …24/40/40/40 | Searches more courts for a match |
| `MAX_NUMBER_OF_SPOUSE_CANDIDATES` | …8/16/32/64 | …16/24/40/64 | Considers more candidates before deciding |

### Better decisions

| Setting | Vanilla | Now | Effect |
|---|---|---|---|
| `SCHEME_COUNTERMESURE_SWITCH_SCORE` | 1.25 | 1.1 | Switches countermeasures sooner when a scheme changes |
| `COUNCIL_TASK_SWITCH_SCORE` | 1.25 | 1.1 | Retasks councillors sooner instead of wasting them |
| `BUILDING_MIN_SCORE_COMPARED_TO_BEST` | 0.8 | 0.92 | Stops wasting gold on nearly-as-good buildings |
| `GOALS_PER_TYPE` | 0/0/1/2/3/3/3 | 0/0/2/3/4/5/5 | Pursues more goals at once |

## Maintenance — important

This mod ships a **partial** override: a new file, `common/defines/ai/tfast_smarter_ai.txt`,
declaring only the 16 tuned keys inside the `NAI` block.

That is safe because CK3 merges defines at the **key** level across files rather
than replacing whole files. **Vanilla proves this itself** by splitting five blocks
between `00_defines.txt` and `ai/00_ai.txt` — `NActivity`, `NCourtPositions`,
`NFaction`, `NInventory`, `NMigration` — with fully disjoint keys in each half. If
blocks replaced each other the game would silently lose half of every one of them.

**The practical benefit: this file cannot rot when the game patches.** Any new AI
setting a patch introduces is inherited automatically, because this file never
mentions it. The only way it can break is a tuned key being **renamed or removed**.

Check after every CK3 update:

```powershell
python c:\Games\ck3-ai-automation\tools\tune_ai_defines.py --check
```

It verifies all 16 keys still hold the intended values and still exist in vanilla,
and prints `[ROT]` for any key the game no longer defines. If one rots, delete its
line from the `TUNINGS` table and regenerate:

```powershell
python c:\Games\ck3-ai-automation\tools\tune_ai_defines.py --emit
```

## Note on late-game performance

Making the AI think more costs CPU, and the late game is when that costs most.
See `tfast_lategame` for the opposite trade, and the README there for how the two
interact.

## Files

```
tfast_smarter_ai.mod                                        launcher descriptor
tfast_smarter_ai/descriptor.mod                             mod descriptor
tfast_smarter_ai/common/defines/ai/tfast_smarter_ai.txt     16 tuned keys, nothing else
```

> Earlier versions shipped a full 65 KB copy of `00_ai.txt`. That worked but was
> fragile: any AI setting a patch added would have been missing from the copy.
> The partial file is 1.6 KB and cannot rot that way.

## Uninstalling

Remove it from the playset. Because it only overrides defines, disabling the mod
restores vanilla AI behaviour immediately — no save-format risk.
