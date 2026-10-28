# TFAST Performance - Lean AI

Makes the **Crusader Kings III** AI do less work, so the game runs faster in
the long campaigns. For **1.20.x**.

## Read this first

**This is a trade, not a free fix.** The AI will recalculate its plans less
often and weigh fewer options. It becomes lazier and somewhat dumber. Use it
when the game crawls; disable it when you want sharper opponents.

**It conflicts with `tfast_smarter_ai` on purpose.** That mod tunes the same
keys the other way (faster reactions, wider searches, more CPU). Do not expect
both to apply. This file is named `zz_...` so it sorts last inside its load
group; for a guaranteed merge order, enable only one of the two.

What this mod cannot do: remove the engine cost of thousands of living
characters, large wars or pathfinding. For the character side, pair it with
`tfast_lategame` (population growth). For everything else, the graphics
settings and the number of active mods matter more than any define.

## What it changes

Only AI keys inside `common/defines/ai/zz_tfast_performance_ai.txt` - a
partial override merged at the key level (see `tfast_lategame`'s header for
why that is safe):

| Key | Vanilla | Here |
|---|---|---|
| SHORT/MEDIUM/LONG/RARE/STRATEGY task ticks | 7-180+ days per tier | roughly doubled |
| MINIMUM/MAXIMUM_TASKS_IN_TICK | 128 / 192 | 96 / 128 |
| GOALS_PER_TYPE | { 0 0 1 2 3 3 3 } | { 0 0 1 1 2 2 2 } |
| Spouse court/candidate and diplo search maxima | 8-64 | 3-40 |
| RAISE_LEVIES / CHECK_ADMIN_ARMIES cooldowns | 180 / 360 | 360 / 720 |
| Army target/stance/split-merge ticks | 7 / 14 / 30 | 14 / 21 / 45 |

## Files

```
tfast_performance.mod
tfast_performance/descriptor.mod
tfast_performance/common/defines/ai/zz_tfast_performance_ai.txt
tfast_performance/README.md
```
