# TFAST Shattered Crowns (v1.0.0)

A TFAST-integrated total-war survival mod for Crusader Kings III **1.20.x**.

The Hollow Dominion has always been down there. Now it is awake, it is
immortal, and it has decided the world is owed to it. Survive the raids, raise
the Great Wall, win or outlast the Great Reckoning - and if the bloodline is
willing, meet the prophecy when it wakes.

## What this mod adds

| System | Status | Where |
|---|---|---|
| Immortal Hollow Dominion (Overlord + 10 original children, closed bloodline) | **Implemented** | `common/scripted_effects/tfast_sc_bootstrap_effects.txt` |
| Hidden dynasty with its own faith/rite (Hollow Communion) | **Implemented** | `common/religion/` |
| AI-only Hollow rulers, never permanently destroyable Overlord | **Implemented** | bootstrap + `on_death` registry |
| Scripted raids: warning, defense stance, gold/control/raiders, prisoners, frost | **Implemented** | `tfast_sc_raid_effects.txt`, `tfast_sc.0100-0101` |
| Great Reckoning: foretelling, real war with a custom CB, 3 bounded waves, retreat | **Implemented** | `tfast_sc_crisis_effects.txt`, `tfast_sc_wars.txt`, story cycle |
| Siege wall gate (scripted raids blocked until breach) | **Implemented** | `tfast_sc_wall_effects.txt` |
| Great Wall project: 5 build stages + upkeep + repair | **Implemented** | decisions + `tfast_sc_wall_effects.txt` |
| Last Watch: recruited watch commander | **Implemented** | decision `tfast_sc_last_watch_recruit` |
| Chosen Emperor: hidden mark, awakening, 3-tier power, dynasty-only succession | **Implemented** | `tfast_sc_prophecy_effects.txt`, prophecy story |
| True Death (awakened chosen only; Overlord can only be sealed) | **Implemented** | decision + `tfast_sc.0500` |
| Captured immortal crisis diplomacy | **Implemented** | `tfast_sc.0600` |
| Eternal Court: loyalty/grievance/ambition/influence, blocs, rare rebellion | **Implemented** | `tfast_sc_yearly_effects.txt` |
| Dynasty memory + "Tell the Tale" | **Implemented** | memory variables + decision + `tfast_sc.0700` |
| Refugees / rebuilding after the Reckoning | **Implemented** | `tfast_sc.0202`, rebuild decision |
| The Long Dark: a Reckoning the world LOSES - world decay, Hollow tithe, uprising, comeback | **Implemented** | `tfast_sc_dark_age_effects.txt`, `tfast_sc.0900-0908`, game rule |
| Wall projects: reinforcement refits, blockades ("no routes in"), Hollow demolition, sponsor dismantle | **Implemented** | dark decisions + wall effects |
| Mercenaries for hire: three gold-scaled tiers, any landed ruler, anywhere | **Implemented** | `tfast_sc_merc_effects.txt` + decisions |
| Hollow goals: vendetta, hunt, blood, terror, treasure - the Host acts on them yearly | **Implemented** | `tfast_sc_goal_effects.txt`, `tfast_sc.0910-0912` |
| Hiding from the Host (and the hunt that finds you) | **Implemented** | hiding decisions + raid targeting weights |
| Automation menu: seven realm automations with open/close switches | **Implemented** | `tfast_sc_auto_decisions.txt`, `tfast_sc_automation_effects.txt` |
| In-game handbook: eight chapters of help, opened from the Decisions tab | **Implemented** | `tfast_sc_help_decisions.txt` |
| Randomized flavor pools (DeepSeek-generatable) and an unpredictable Host: raid moods, goal caprice, drawn omens | **Implemented** | `tfast_sc_flavor_generated_l_english.yml`, `events/tfast_sc_flavor_events.txt`, `tools/tfast_flavor_deepseek.py` |
| The Hollow Tide: a full Situations-window entry with six chapters (peace → escalation → Reckoning → aftermath/dark → uprising) | **Implemented** | `common/situation/situations/tfast_sc_hollow_tide.txt`, `tfast_sc_catalysts.txt` |
| 6 supernatural men-at-arms (Hollow-only, capped) | **Implemented** | `common/men_at_arms_types/tfast_sc_units.txt` |
| Signature abilities of the Ten | **Scaffolded** | Morvath (bounded reinforcements), Kaedryn (frost) live; others declared in the design doc |
| Artifact raids / stolen relics | **Scaffolded** | documented as V2 (no artifact types shipped) |
| Map-impassable wall border | **Not possible in-engine** | documented; the wall blocks the mod's scripted raids and slows sieges |
| Original Hollow heraldry, trait icons, and event paintings | **In the mod** | `gfx/interface/`, `common/event_backgrounds/` |

## Install

1. The mod folder already lives at
   `Documents/Paradox Interactive/Crusader Kings III/mod/tfast_shattered_crowns`.
2. The `.mod` descriptor is at `.../mod/tfast_shattered_crowns.mod`.
3. Enable **TFAST Shattered Crowns** in the playset (it has been registered in
   `dlc_load.json` alongside the other TFAST mods).
4. Load order: anywhere after the base game; it is designed to coexist with
   every other TFAST module (no shared IDs - see `docs/`).

## Game rules

* **Shattered Crowns: The Reckoning** - Early / Standard / Late pacing.
* **Shattered Crowns: Hollow Host Strength** - Lenient / Standard / Harrowing.
* **Shattered Crowns: The Chosen Emperor** - Enabled / Disabled.
* **Shattered Crowns: The Long Dark** - On / Off (whether a lost Reckoning becomes the Long Dark).

## Honest limitations (read this)

* **AI-only, without fooling the engine's UI.** The Hollow are AI rulers who
  never enter the player's dynasty; nothing in normal play lets you switch to
  them. The debug console and external mods can still do what debug tools do -
  that is documented, not hidden (`docs/SHATTERED_CROWNS_COMPATIBILITY.md`).
* **The Great Wall blocks the mod's scripted raids** (its own raiding path),
  and slows real sieges through fort-level county modifiers. Native CK3 army
  pathfinding cannot be walled off by any mod; no false claims here.
* **Engine deaths of an original child are banishment**, not destruction: the
  character returns as a new instance wearing the same name and face, with a
  log line explaining the engine fact (`docs/COMPATIBILITY.md`).
* **True Death on the Overlord seals him** - he is never permanently killed.
* Everything is capped on purpose: raids per year, waves per Reckoning, army
  sizes, council effects, memory retention. Nothing here scans the map daily.

## Verification

Every effect, trigger, callback, scope, modifier key, faith/rite/doctrine key,
MAA field, casus belli field and event structure used by this mod was checked
against the **installed 1.20 data files** before shipping - the checklist and
commands are in `docs/SHATTERED_CROWNS_TEST_REPORT.md`.
