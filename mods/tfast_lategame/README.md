# TFAST Late Game — Stability

Slows the rate at which the character population grows, so late campaigns stay
playable. For **Crusader Kings III 1.20.x**.

---

## Read this first: what this can and cannot do

**This mod does not "fix lag", and it is not a performance patch.** Late-game
slowdown in CK3 is dominated by engine cost: thousands of living characters, each
evaluated by the AI, plus large wars and their pathfinding. No mod can remove
that — it is a limitation of the simulation, not of your settings.

What this mod *can* do is reduce **one** input to that cost: how fast the
character population grows. That is the part which is actually moddable.

**Expect a modest improvement, not a transformation.** If you want a large
change, the effective levers are the game's own settings (turn down graphics,
reduce the number of active mods) and your hardware.

---

## What it changes

Only four settings, across three defines blocks. Every one is **non-destructive**:
nobody is removed, no character is deleted, no existing guest is evicted.

| Setting | Vanilla | Now | Why |
|---|---|---|---|
| `MAX_COURTIERS_AND_GUESTS_PER_TIER` | `0 0 6 8 12 20 36` | `0 0 5 6 9 14 24` | Caps how many courtiers/guests accumulate per tier |
| `GUEST_STAY_DURATION_MONTHS` | 36 | 24 | Guests leave sooner, so fewer are alive at once |
| `MAX_NUM_PENDING_COURT_EVENTS` | 3 | 2 | Less queued event state to evaluate |
| `COURT_EVENT_TIME_OUT` | 180 | 90 | Stale court events clear faster instead of piling up |

The courtier/guest cap is the big one, and it is **explicitly safe by vanilla's own
documentation**:

> "Maximum number of adult courtiers and guests, per ruler tier. **While it won't
> throw anyone out if the limit is exceeded, no new guests will arrive while at or
> above the cap.**"

So courts simply stop filling up. Nobody already present is affected. Large realms
are trimmed hardest, because they hold the most characters — an empire court drops
from 36 to 24.

`MIN_GUESTS_PER_TIER` is deliberately **left alone**, so you will never run out of
guests to recruit, marry or hire.

---

## Important: this fights with `TFAST Smarter AI`

These two mods pull in opposite directions and you should understand the trade:

| | `tfast_smarter_ai` | `tfast_lategame` |
|---|---|---|
| Goal | Better AI decisions | Lower CPU cost |
| AI tick frequency | **Raised** (thinks more often) | — |
| `GOALS_PER_TYPE` | Raised (3 → 5 at empire) | — |
| Character population | — | **Reduced** |

A smarter AI thinks more, and late game is exactly when that costs the most. So:

* **Performance is your priority** → use `tfast_lategame`, skip `tfast_smarter_ai`.
* **Challenge is your priority** → use `tfast_smarter_ai`, skip this.
* **Both** → they are compatible and can be enabled together, but you are asking
  for more AI work *and* fewer characters at the same time. The character
  reduction partly pays for the extra AI activity; the net effect depends on your
  machine and how large the world gets.

There is no honest way to claim both are free.

---

## Why a partial override is safe here

This mod ships a **new** file, `common/defines/tfast_lategame.txt`, declaring only
the four keys above. It does **not** copy vanilla's 122 KB `00_defines.txt`.

That is safe because CK3 merges defines at the **key** level across files rather
than replacing whole files. **Vanilla proves this itself:** it splits five blocks
between `00_defines.txt` and `ai/00_ai.txt` —

```
NActivity, NCourtPositions, NFaction, NInventory, NMigration
```

— and in every case the two halves have **fully disjoint keys**. If blocks replaced
each other, the game would silently lose half of every one of those five blocks. It
does not.

The practical benefit: this file **cannot rot when the game patches**. A new define
added by a patch is inherited automatically. The only failure mode is a key being
renamed or removed, which the validator reports.

---

## Maintenance

After a game patch:

```powershell
python c:\Games\ck3-ai-automation\tools\validate_mod.py "C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III\mod\tfast_lategame"
```

It checks that all four keys still exist in vanilla, plus the usual descriptor,
tag, BOM and script checks.

## Files

```
tfast_lategame.mod                                    launcher descriptor
tfast_lategame/descriptor.mod                         mod descriptor
tfast_lategame/common/defines/tfast_lategame.txt      4 tuned keys, nothing else
```

## Uninstalling

Remove it from the playset. Only defines are changed, so vanilla behaviour
returns immediately. Courts that were capped below the vanilla limit will start
filling again on their normal schedule — nobody was removed, so there is nothing
to repair.
