# TFAST Fun Pack — Court Life & Character

Extra things to *do* in **Crusader Kings III 1.20.x** — the stuff of court and
personality rather than conquest or administration.

## How to enable

1. This folder and `tfast_funpack.mod` are already in your CK3 mod directory.
2. Open the CK3 launcher → **Playsets** → add **TFAST Fun Pack**.
3. Launch. The decisions appear in the **Decisions** tab under *Major Decisions*.

Independent of the other TFAST mods — enable any combination.

## What it adds

Six decisions, each with a real cost and a lasting mark. None of them are pure
upside: you pay in gold, prestige, dignity or goodwill.

| Decision | Cost | Cooldown | What you get |
|---|---|---|---|
| Host a Grand Tournament | 400 gold | 5 years | Tournament Champion trait, 400 prestige, 20 years of a Famous Tournament |
| Commission a Menagerie | 350 gold | 10 years | Menagerist trait, 25 years of a Wondrous Menagerie |
| Retain a Master Artisan | 300 gold | 10 years | Patron of the Arts trait, 25 years of an Artists' Court |
| Declare a Blood Feud | **free** | 10 years | Bloodfeud trait, +25 dread, **+15 tyranny**, −10 general opinion for 25 years |
| Amass a Private Hoard | 500 gold | 10 years | Hoarder trait, +15% income, **−10 general opinion** for 25 years |
| Take a Year of Pleasure | 200 prestige | 5 years | −150 stress, Bon Vivant trait, 15 years of reduced income |

**Traits** (all reappraisable, permanent):

`Tournament Champion` · `Menagerist` · `Patron of the Arts` · `Bloodfeud` ·
`Hoarder` · `Bon Vivant`

## Design notes

**Every choice has a downside.** A tournament costs a fortune. A blood feud buys
dread and tyranny in the same breath. A hoard enriches you and alienates your
court. A year of pleasure is the only real cure for stress that costs you
dignity and coin. That is deliberate — a decision with no cost is just a button.

**The traits are distinct from `tfast_history`.** That mod's `Patron of Letters`
is about scholarship and libraries; this mod's `Patron of the Arts` is about
craftsmen and ornament. They can be held together.

## Why it is safe

* **`is_ai = no`** — only you can ever see or take these. The AI's economy,
  wars and balance are untouched.
* **`ai_check_interval = 0`** — the AI never evaluates them.
* **Purely additive** — no vanilla file is overwritten. Disabling the mod
  restores the game exactly.
* **No new art.** All six trait icons and all six illustrations are reused from
  vanilla, so there is nothing to go missing and no texture conflicts.
* Every effect, trigger, modifier key, trait icon and illustration was verified
  against the installed 1.20.0.3 data before use.

> **Achievements.** As with any gameplay mod, using these decisions disables
> achievements for that save.

## A note on what was deliberately not built

A **game rule pack** was considered and rejected. CK3 game rules can only apply
a modifier to the player or set a flag from a short fixed list. A rule that
grants player bonuses would either duplicate the existing difficulty rules or
quietly dodge their `blocks_achievements` flag — and the flags that *are* useful
(`no_end_date`, `no_diplomatic_range`) are already used by vanilla rules, so
reusing them would conflict.

**Random events** were also skipped. Firing them correctly needs an `on_action`
hook, and that cannot be verified without running the game — so it would be
guesswork dressed up as content.

## Files

```
tfast_funpack.mod                                          launcher descriptor
tfast_funpack/descriptor.mod                               mod descriptor
tfast_funpack/common/decisions/00_tfast_fun_decisions.txt
tfast_funpack/common/traits/tfast_fun_traits.txt
tfast_funpack/common/modifiers/tfast_fun_modifiers.txt
tfast_funpack/localization/english/tfast_fun_l_english.yml
```

## Validate after editing

```powershell
python c:\Games\ck3-ai-automation\tools\validate_mod.py "C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III\mod\tfast_funpack"
```

## Uninstalling

Remove it from the playset, load the save, then save under a new name. The
traits will remain on characters in that save, so only delete the folder once no
save you care about was made with it active.
