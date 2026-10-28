# Feature risk register

Classification before implementation. Phase 1 is the only block with new script.

## GREEN — in Phase 1

| Feature | Why it is safe | Status |
|---|---|---|
| Hidden deposit variables on six fixed counties | County variables persist in saves. The title keys were read from `00_landed_titles.txt` | IMPLEMENTING |
| Knowledge steps 0–4 | Integer variable, no per-character map | IMPLEMENTING |
| Question locals / hire surveyors | Decisions, gold cost, cooldown, one event | IMPLEMENTING |
| One gold working as `tax_mult` | Same key as vanilla `oasis_modifier` | IMPLEMENTING |
| Skip counties with `generic_gold_mines` | Verified building and `has_building_or_higher` | IMPLEMENTING |
| Game rule on/off | Same `has_game_rule` pattern as the existing rules | IMPLEMENTING |

## YELLOW — simplified, not built yet

| Feature | Smaller version | Status |
|---|---|---|
| Eight prospecting methods | Two methods plus a rumor. Caves, records, abandoned mines, and merchant expeditions wait | POSTPONED |
| Mine stages up to a great complex | One working, three tax tiers from richness. No upgrade ladder | SIMPLIFIED in Phase 1 |
| Owner-known vs public | Developed modifier is the public state. No secret-per-ruler map | SIMPLIFIED in Phase 1 |
| Foreign concessions | One interaction and a timer, after Phase 1 is verified | POSTPONED |
| Trade | A contract modifier, not caravans | POSTPONED |
| Banking | One player house, one AI house, explicit debit and credit | POSTPONED |
| Financial heirs and trusts | Only after the bank ledger exists | POSTPONED |
| Workforce and famine | County modifiers on devastation, not people | POSTPONED |
| Economic espionage | One scheme with a cooldown, using existing intrigue if the target scope verifies | POSTPONED |

## RED — do not implement

| Feature | Why |
|---|---|
| Replace the world map, cultures, religions, or succession | Breaks the game and the Hollow setup |
| A second global currency or live commodity prices | Duplicates gold and has no verified market API |
| Per-worker, per-caravan, or per-coin simulation | Unbounded |
| Custom management windows | No verified GUI for this version was written |
| Banks as landless corporations with their own succession | The engine has no such object. A character treasury would double-count |
| Trusts that spend gold the founder still has | Duplicate money |
| Voluntary trade or service with the Hollow | Forbidden by the existing canon |
| Claiming the Winter Wall blocks vanilla pathfinding | Not verified. Scripted Hollow entry is a separate, already existing system |
| Daily scans of every county for deposits | Performance |

## Alternative for the postponed economy

Keep using county tax and county variables. Add iron, stone, timber, and grain as further fixed lists only after a campaign has actually opened one gold working and the error log is clean. Do not start banking in the same pass.
