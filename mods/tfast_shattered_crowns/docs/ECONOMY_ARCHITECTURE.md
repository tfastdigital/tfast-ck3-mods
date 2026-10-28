# Economy architecture

Phase 1 uses one accounting path: **CK3 county tax**. There is no parallel gold ledger.

```
fixed deposit list
  -> county variables (type, richness, knowledge)
  -> prospecting decisions
  -> discovered
  -> one county tax modifier (the working)
  -> vanilla tax collection
```

## What is stored

On the county title, and therefore in the save:

| Variable | Values |
|---|---|
| `tfast_sc_deposit_type` | `1` gold. Absent means no seeded deposit |
| `tfast_sc_deposit_richness` | `1` small, `2` ordinary, `3` great |
| `tfast_sc_deposit_knowledge` | `0` unknown, `1` rumored, `2` surveyed, `3` discovered, `4` developed |

Developed is the public state. The mine is a county modifier anyone can see. There is no per-character knowledge list.

On the campaign:

| Variable | Meaning |
|---|---|
| `tfast_sc_deposits_seeded` | The one-time seed has run |

Character variables `tfast_sc_survey_result` and `tfast_sc_rumor_county` exist only long enough to fill one event, then the option removes them.

## What is not stored

Personal gold, bank reserves, deposits, loans, trust principal, and shares are not implemented. They must not be invented by adding `add_gold` on top of the county tax.

## Ownership

The county holder controls the land. The tax modifier stays on the county, so it follows the title under ordinary succession. Mining leases, foreign concessions, and separate financial heirs are not in this phase.

## Interfaces

- `tfast_sc_seed_gold_deposits_effect` — once, after the lobby, if the game rule is on.
- `tfast_sc_prospect_county_effect` — one step of knowledge, or a miss.
- `tfast_sc_question_locals_effect` — unknown to rumor only.
- `tfast_sc_open_gold_working_effect` — discovered to developed, plus one tax modifier.
- `tfast_sc_gold_rumor_yearly_effect` — the player only, six named counties, at most one rumor.

Later phases must call these, or a successor with the same county variables. They must not create a second record of the same gold.
