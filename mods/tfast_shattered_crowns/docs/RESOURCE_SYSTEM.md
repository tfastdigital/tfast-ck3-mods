# Resource system

Status: Phase 1 gold only. SIMPLIFIED relative to the full brief.

## Deposits

Seeded once, after the lobby, when `tfast_sc_economy` is On (the default). Off seeds nothing.

| County | Historical basis | Richness |
|---|---|---|
| `c_bambuk` | Bambuk goldfield | 3 |
| `c_bure` | Bure goldfield | 3 |
| `c_allaqi` | Wadi Allaqi | 2 |
| `c_altay` | Altai gold country | 2 |
| `c_carmarthenshire` | Dolaucothi | 1 |
| `c_astorga` | Nearest verified county to the León gold district | 2 |

A county that already has vanilla `generic_gold_mines_01` or a higher tier is skipped. No second yield is added there.

The list does not grow. Events do not create new deposits.

## Knowledge

Unknown deposits do nothing. A rumor can arrive once a year if the player personally holds the county, at a 20% chance, then a three-year silence. Questioning the capital's people can also raise unknown to rumored. Hiring surveyors advances rumor to surveyed, or surveyed to discovered. Each attempt can fail. Failure does not stamp the county as empty.

Discovery does not build anything. The player spends 200 gold to open the working.

## The working

One permanent county modifier, chosen from richness:

| Richness | Modifier | County tax |
|---|---|---|
| 1 | `tfast_sc_gold_working_small` | +5% |
| 2 | `tfast_sc_gold_working_developed` | +10% |
| 3 | `tfast_sc_gold_working_royal` | +15% |

That is the whole yield. It uses the vanilla tax path. If a vanilla gold mine is present at the moment of opening, the deposit is marked developed and no modifier is added.

## Not in this phase

Iron, stone, timber, grain, aetherstone, silver, copper, salt, horses, livestock, gems, and hollowstone have no scripts. Mine upgrades, depletion tiers, collapse events, leases, and foreign rights are not built.
