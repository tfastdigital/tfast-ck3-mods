# Performance report

No timed observer campaign was run for the gold system. This file records the bounds that were written, not a benchmark.

## What runs

- Once per campaign, after the lobby: six explicit county titles. No loop over the map.
- Once a year, on the human player only: those same six titles, and only while a rumor cooldown flag is absent. One event at most.
- Decisions: evaluated for the player, with `ai_check_interval = 0` and `is_ai = no`.

## What was not built, because it would scan too much

Daily county sweeps, a knowledge flag on every character, caravans, workers, per-coin prices, and a bank entity per realm.

If a later phase adds a yearly check, it has to stay on the player or on the six titles until a scoped alternative is measured.
