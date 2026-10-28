# Shattered Crowns - Compatibility and Integration Report

## 1. TFAST workspace integration (Sprint 0 result)

The TFAST CK3 workspace is the shared mod directory:

```
Documents/Paradox Interactive/Crusader Kings III/mod/
    tfast_africa/        tfast_ai_suite/      tfast_funpack/
    tfast_history/       tfast_lategame/      tfast_smarter_ai/
    tfast_template/      tfast_shattered_crowns/   <-- this mod (V1)
```

Shared conventions confirmed from the existing modules and matched exactly:

* descriptor: `version`, `tags`, `name`, `supported_version = "1.20.*"`,
  `path` in the root `.mod` file;
* all script files and localization are **UTF-8 with BOM**;
* player-facing decisions use `is_ai = no` + `ai_check_interval = 0`;
* comments and headers in the same TFAST style (feature guarantees stated in
  the header of every file).

### Conflict map (checked by ID scan against every sibling module)

| ID space | Owner modules | Shattered Crowns |
|---|---|---|
| `tfast_sc_*` prefix | none existed (scan clean) | all new IDs |
| events namespace `tfast_sc.` | none existed | all new events |
| `tfast_africa_*`, `tfast_fun_*`, `tfast_hist_*`, `tfast_auto_*`, `tfast_cheat_*`, `tfast_grant_*` | sibling mods | untouched |
| vanilla on_actions `on_game_start`, `on_game_start_after_lobby`, `yearly_playable_pulse`, `on_birth_child`, `on_death` | base game | **chained**, never overridden |

### Load order

* Recommended: any position after the base game and DLC; tested target is the
  final position in the TFAST sequence.
* No file in this mod overwrites a base-game file path, so load order cannot
  break base content from this side.
* `on_action` chaining uses the game's documented pattern
  (`_on_actions.info`: `vanilla_on_action = { on_actions = { mod_action } }`),
  which appends without replacing the vanilla `effect`/`trigger` blocks.

## 2. Engine limits, stated plainly

1. **Map-impassable walls do not exist in CK3.** The Great Wall cannot
   redirect vanilla army pathfinding. What it does: blocks this mod's
   scripted raid director (the mod's only raiding path) until a breach, adds
   fort-level county modifiers that slow real sieges, and hosts the wall
   defense chain and Last Watch content.
2. **AI-only is enforced by construction, not by engine exclusion.** The
   Hollow are a separate dynasty that never enters player succession; the
   Overlord and the Ten are AI rulers. Debug consoles, observer switches and
   external character-switch mods can still switch into anyone - that is a
   tool-level fact of the engine, documented here per the build spec.
3. **Engine deaths are facts.** If the engine kills an original child outside
   True Death, the death itself cannot be undone. The mod records it as
   banishment and may later return a *new instance* with the same name,
   template and role (logged with `debug_log`). The Overlord is the exception:
   if the engine kills him, he is re-raised by the repair pass and the story
   is re-owned (`on_owner_death` -> `make_story_owner`).
4. **Native raiding is government-gated in 1.20** (tribal/nomadic-style
   governments). The Hollow therefore never rely on it; all raiding is the
   scripted director.
5. **Inbreeding remains vanilla.** The Hollow faith uses
   `doctrine_consanguinity_unrestricted` + `tenet_divine_marriage` so the
   closed bloodline can marry; the vanilla inbred risk for close-kin births is
   *not* disabled anywhere. Closed-bloodline children can carry the same
   penalties any mortal dynasty would earn.
6. **Faith and culture are cosmetically isolated on purpose.** The Hollow
   religion is a new, headless rf_pagan-family religion (no holy sites, no
   fervor interaction with any real faith), and the Hollow use the greek
   culture so that no cultural grouping is disturbed. Their county faith
   conversion affects only the stronghold counties they hold.

## 3. Save compatibility

* All persistent state lives in global variables (`tfast_sc_initialized`,
  `tfast_sc_overlord`, `tfast_sc_crisis_phase`, role registries, ...),
  character variables (council numbers, memories, wall data) and county
  variables/modifiers. All are removed or bounded by design; the mod adds no
  database references that outlive characters.
* The repair pass (`tfast_sc_repair_effect`) runs at game start (after lobby)
  and re-creates anything missing: overlord marks, aura modifier, the director
  story, a missing primary stronghold. Removing the mod mid-save is not
  recommended (standard for script mods), but nothing here writes state that
  blocks a vanilla load beyond unused flags/variables.
* Dead characters are never addressed from persistent state: the role
  registry uses plain integer globals (`tfast_sc_role_<name>_status`), which
  is why banished children can return without scope errors after centuries.

## 4. Other mods

* Any mod adding counties/titles in the same regions: the stronghold chooser
  only ever targets the five verified vanilla island counties
  (`c_bornholm`, `c_rugen`, `c_isle_of_man`, `c_osel`, `c_anglesey`), and it
  skips any county held by a human player, so it cannot seize map-mod content
  that is not vanilla.
* Total-conversion or religion overhaul mods: the Hollow religion is
  additive; it uses only base doctrine keys and no custom doctrine types.
* UI mods: none of this mod's content depends on GUI files.
* Other AI or raid mods: the raid director is self-contained; it never hooks
  vanilla raid systems, so AI mods cannot double-fire Hollow raids.
