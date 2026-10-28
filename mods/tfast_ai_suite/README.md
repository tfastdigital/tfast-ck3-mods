# TFAST AI Suite — Cheats & Automation

A single-player convenience mod for **Crusader Kings III 1.20.x**.

Companion to the external AI harness at `C:\Games\ck3-ai-automation`.

## How to enable

1. This folder and `tfast_ai_suite.mod` are already in your CK3 mod directory.
2. Open the CK3 launcher → **Playsets** → add **TFAST AI Suite**.
3. Launch. In the **Decisions** tab under *Major Decisions*, click **TFAST Cheat Menu: Open**. The page tabs appear: **Resources**, **Domain**, **Military**, **Character**, **Realm**. Open one, click the cheats you want, then **Back** (or **Close** to hide everything). While the menu is closed, none of the cheats clutter the Decisions tab.

Landless adventurers get the full usable kit: gold, prestige, piety, renown, legitimacy, dread and the Golden Age on **Resources**; Sharpen Every Skill, Peace of Mind and Absolved of Tyranny on **Character**; Expand Men-at-Arms on **Military** (Golden Age's development pulse simply skips if you hold no land). Landed-only tools - walls, domain development, instant building, government switches, Raise a Host - keep their gates and stay hidden.

## What it adds

### Cheat menu (Daddy Pika-style)

All cheats and automation tools sit behind one flag menu on the player character:

| Step | Decision |
|---|---|
| Open the menu | **TFAST Cheat Menu: Open** |
| Pick a page | **Cheat Menu: Resources / Domain / Military / Character / Realm** |
| Return to the page list | **Cheat Menu: Back** |
| Hide everything | **TFAST Cheat Menu: Close** |

One page is open at a time. Menu state is plain character flags (`tfast_menu_open`, `tfast_menu_page_*`), so it dies with the character and never touches the AI, the map, or any save format.

### Cheats, by page

**Resources** — Windfall of Gold (+10000 gold) · Legendary Renown (+10000 prestige) · Divine Favour (+10000 piety) · Dynasty Renown (+10000 renown, or prestige if you carry no dynasty) · Unquestioned Right (+1000 legitimacy) · A Terrifying Reputation (+100 dread) · Political Influence (+1000 influence, *administrative governments only*) · **Golden Age** (all of it at once: +10000 gold/prestige/piety/renown, +1000 legitimacy, +150 dread, +2 development realm-wide, and a 20-year realm boon).

**Domain** — Enrich the Capital (+1 development there) · Develop the Realm (+1 development in every county you rule) · Auto: Develop Your Domain (+1 development in the counties you personally hold, without enriching your vassals) · Add Building Slots (+1 permanent slot per province in your held counties, repeatable, caps at 10) · Instant Building (finishes one brand-new building in every held barony that has a free slot) · **Upgrade Everything You Rule** (walks every county in your realm and drives each holding through its whole building chain — `castle_01`→`04`, `city_01`→`04`, `temple_01`→`04`, `temple_citadel_01`→`04` — then fills any free slots).

**Military** — **Expand Men-at-Arms, in one step** (every empty regiment slot is filled from a fixed type list, then every regiment is pushed to its maximum size; no repeat clicking) · **Create an Army** (a 4000-levy host with six men-at-arms regiments at your capital, existing regiments topped back up, levies refilled) · Raise a Host (2500 levies, footmen, and bowmen in the capital, plus a permanent armored horsemen regiment, levies refilled).

**Character** — Sharpen Every Skill (+2 to all five skills and prowess) · Peace of Mind (clears all stress) · Absolved of Tyranny (clears all tyranny).

**Realm** — Auto: Grant Excess Titles (hands surplus counties to freshly generated local nobles until you are back inside your domain limit, keeping your capital) · Become Feudal / Tribal / Clan / Administrative.

**Outside the menu** — the right-click grants (Grant Gold, Grant an Army, Grant a Building, Grant Standing, Grant Skill) stay on the character interaction menu, where the target belongs. So do the targeted cheats: **Cheat: Create an Army** and **Cheat: Upgrade Everything They Rule** can be aimed at a vassal instead of yourself.

### Fixed

* **Two decisions were exact duplicates.** `Develop the Realm` / `Auto: Develop
  the Realm` and `Expand Men-at-Arms` / `Enlarge All Regiments` had identical
  effects, so the list showed four entries doing two things. The first pair is
  now genuinely distinct — *Develop Your Domain* uses `every_held_county` (your
  counties only) rather than `every_sub_realm_county` (the whole realm) — and
  the second true duplicate was removed.
* **`Grant Excess Titles` could hang the game.** Its `while` loop had no ceiling,
  so if a title grant ever failed to reduce `domain_limit_available` it would
  spin forever. It now carries a 60-iteration guard, matching the counter pattern
  vanilla uses for its own while loops.
* **Building placement no longer logs `(no character)`.** Every vanilla building
  has an `on_complete` block, and several of them read `scope:character` — which
  nothing sets when script places a building directly. The county holder is now
  saved as `scope:character` before each `add_building` / `generate_building`,
  which is what the vanilla blocks expect.

## Harvested from the mods this replaced

This mod absorbed the useful ideas from the standalone mods that used to be
installed, so none of that functionality was lost:

| Came from | Now |
|---|---|
| *add building slot decision* (pdx_120177) | **Cheat: Add Building Slots** — rewritten to use only the vanilla `extra_building_slot` province modifier, so no custom modifier or GUI is needed |
| *Daddy Pika's Cheat Menu Fix* (pdx_62704) | **Cheat: Become Feudal / Tribal / Clan / Administrative** — the flag-driven submenu is replaced by one plain decision per government |
| *Mass Grant Titles* (3812891017) | **Auto: Grant Excess Titles** (same title-and-vassal-change ritual) |
| *Auto Realm Development* (pdx_153834) | **Auto: Develop the Realm** (the enable/mode flag design was dropped for a simpler one-click decision) |
| *Auto Construction Assistant* (3811920217) | not ported — it depends on ~20 MB of custom GUI resources |
| *Auto Education* (3807642051), *Council Automation* (3810883437) | not ported — both need generated on_action hooks and hidden events to work safely |
| *NoRestrictionsBuildings* (pdx_120195) | deliberately not ported — it works by overwriting whole vanilla building files, which is the fragile pattern this mod avoids |


## Why it is safe

* Every decision is `is_ai = no` — only a human can see it.
* Every decision is `ai_check_interval = 0` — the AI never evaluates it, so the
  AI economy and warfare are completely untouched.
* It is **purely additive**: no vanilla file is overwritten or replaced.
  Disabling the mod restores the game exactly.
* Every effect used is a vanilla effect verified against 1.20.0.3.

> **Achievements.** Using these decisions disables achievements for that save,
> exactly as the in-game debug console does. That is the game's own rule.

## Files

```
tfast_ai_suite.mod                                       launcher descriptor
tfast_ai_suite/descriptor.mod                            mod descriptor
tfast_ai_suite/common/decisions/00_tfast_cheats.txt      cheats
tfast_ai_suite/common/decisions/01_tfast_automation.txt  automation
tfast_ai_suite/common/decisions/02_tfast_harvested.txt   harvested cheats
tfast_ai_suite/common/decisions/03_tfast_grants.txt      self-use versions of the grant interactions
tfast_ai_suite/common/decisions/04_tfast_menu.txt        cheat-menu shell (open/close + five pages)
tfast_ai_suite/common/character_interactions/tfast_grants.txt  right-click grants
tfast_ai_suite/common/scripted_effects/tfast_effects.txt
tfast_ai_suite/common/scripted_effects/tfast_grant_effects.txt
tfast_ai_suite/common/scripted_triggers/tfast_triggers.txt
tfast_ai_suite/common/modifiers/tfast_modifiers.txt
tfast_ai_suite/gfx/interface/illustrations/decisions/tfast_menu_tab_*.dds  menu tab art
tfast_ai_suite/localization/english/tfast_l_english.yml
```

Rebuild the menu tab art with:

```powershell
python C:\Games\ck3-ai-automation\tools\build_menu_tabs.py
```

Validate any change with:

```powershell
python c:\Games\ck3-ai-automation\tools\validate_mod.py "C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III\mod\tfast_ai_suite"
```

## Uninstalling

Remove it from the playset, load the save, then save under a new name. Only
delete the folder once no save you care about was made with it active.
