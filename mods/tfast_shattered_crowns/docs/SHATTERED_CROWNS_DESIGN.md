# Shattered Crowns - Design and Feature Matrix

Target: Crusader Kings III `release/1.20.0` (installed build, verified from
`logs/code_revisions.log`). Integration form: a **self-contained TFAST module**
(`tfast_shattered_crowns`) in the shared TFAST workspace, loaded alongside
`tfast_africa`, `tfast_ai_suite`, `tfast_funpack`, `tfast_history`,
`tfast_lategame`, `tfast_smarter_ai`, and `tfast_template` with zero shared IDs.

All new IDs use the `tfast_sc_` prefix; all events use the `tfast_sc.` namespace.

## 1. Feature matrix

| Build spec requirement | Status | Notes |
|---|---|---|
| Immortal Hollow Dynasty with single Supreme Immortal Overlord | Implemented | `tfast_sc.overlord` flag + `tfast_sc_hollow_immortal` trait (engine `immortal = yes`) |
| 10 original children, 5 dynastic personality blocs | Implemented | 5 sons / 5 daughters; bloc 0 Iron Crown, 1 Death Covenant, 2 Silent Court, 3 Eternal Keepers, 4 Ashen Conspiracy |
| Family ties fully recorded | Implemented | children created with `set_father` to the Overlord; house = Shattered Crown (Hollow dynasty) |
| Hollow descendants of both parents inherit both bloodlines | Implemented | `on_birth_child` hook + trait inheritance per parent |
| Expanded family-friendly game rule: chosen origin = designated player dynasty | Implemented (game rules) | origin is fixed by design (designated dynasty); the offered rules cover timing, difficulty, prophecy |
| appearance = late; either gender; succession = direct bloodline; hidden until awakening | Implemented | prophecy window opens only after the first Reckoning; gender-neutral `ordered_child`; direct descendants only; hidden variable only |
| No public trait before awakening | Implemented | `tfast_sc.0403` adds `tfast_sc_chosen_awakened`; before that only `tfast_sc_chosen` private variable |
| Overlord never permanently destroyed | Implemented | Overlord excluded in `tfast_sc_true_death_effect`; engine-death fallback re-raises him (`tfast_sc_overlord_reincarnate_effect`) |
| 10 children may be destroyed by awakened chosen; normal deaths = banishment, may return | Implemented | `tfast_sc_original_child_death_effect` + role registry + return pass |
| Grand Governor system / spawned conquest realms | Deliberately trimmed | not needed for the survival loop; the Ten hold baronies inside the strongholds instead. Documented as V2 |
| Custom government for the Hollow | Not used (deliberate) | vanilla feudal keeps the AI fully functional; a custom unplayable government is possible but untested against vassal contracts. Government support confirmed, withheld by design |
| Hollow immortals marry only within the dynasty | Implemented (faith) | Hollow faith: `doctrine_consanguinity_unrestricted` + `tenet_divine_marriage` |
| Inbreeding not assumed disabled | Documented | closed-bloodline marriage uses vanilla rules; inbred outcomes are possible and accepted (see COMPATIBILITY) |

## 2. Raid director (Sprint 2)

* Targets: `every_neighboring_top_liege_realm_owner` of the Overlord's realm
  (geographic feasibility is "can the Host walk there"), filtered by cooldown,
  exhaustion, war status and the Hollow flag.
* Scoring (`tfast_sc_raid_target_score`): wealth, distraction (at war),
  weakness (`max_military_strength`), exhaustion, walls, Hollow readiness.
* Budget: `tfast_sc_raid_budget` resets yearly to 2; the director ticks every
  180-300 days.
* Warning: real event `tfast_sc.0100` with a defense stance choice; AI has its
  own chances; resolution in `tfast_sc.0101` (hidden) with:
  * gold transfer (defended 5% / contested 20% / overrun 40%),
  * `change_county_control` (minor/major/extreme),
  * `tfast_sc_raided_modifier` county modifier (5/15 years),
  * prisoner raid (35%, house arrest) and Kaedryn frost (50%),
  * cooldown 4 years + exhaustion 7 years per target.
* Wall check first: a walled capital with an intact gate routes into
  `tfast_sc_wall_defense_effect` - scripted entry is blocked until breach.

## 3. Crisis director (Sprint 3)

Phase machine in `tfast_sc_crisis_phase`:
`0 dormant -> 1 predatory peace -> 2 foretold (2-year window) -> 3 Reckoning
-> 5 aftermath -> (cooldown 40y) -> 1 again`.

* The Reckoning is a **real war**: `tfast_sc_reckoning_war` (script-only CB,
  `ai = no`), declared by the Overlord on the human player's realm, plus at
  most one secondary neighboring front.
* Waves: at most 3, sized by `tfast_sc_reckoning_wave_size_value`; wave 2
  includes Morvath's bounded reinforcement when his line is active.
* Resolution: victory (one bounded county taken, border devastated), white
  peace, defeat, invalidation, or forced retreat (`end_war = white_peace`) all
  route to the aftermath.
* The first Reckoning is fully resolvable with no Chosen Emperor.
* Global counters cap populations and story weight: `tfast_sc_story_budget`,
  `tfast_sc_raid_count`, `tfast_sc_reckoning_waves`, `tfast_sc_descendants_destroyed`.

## 4. Siege wall (Sprint 5)

* One project per sponsor; wall counties = sponsor's capital + up to 3 own
  counties in the same de jure duchy (only **existing** counties).
* Stages: planning -> towers -> rampart -> gates -> wards (decisions).
* Integrity variable + upkeep variable; yearly upkeep decay; breach at 0:
  gate modifier removed, county flagged, world notified (`tfast_sc.0302`).
* Wall defense: `tfast_sc_wall_defense_value` (stage, marshal, watchman,
  wards, integrity) vs Hollow raid power; three outcomes.
* Final defence node: a recruited Watch Commander (`tfast_sc_wall_watchman`)
  plus optional wards; the wall can be repaired and rehung.

## 5. Prophecy (Sprint 4)

* Window opens in the aftermath (`tfast_sc_prophecy_open` for 10 years).
* `on_birth_child` marks candidates in the designated dynasty; a randomized
  delay (`tfast_sc.0400`, 30-360 days) selects the hidden chosen.
* Awakening: at 16, or at 12+ in danger (war or prison), via the prophecy
  story. Only the dormant-watch story tracks them; no public marker before.
* One upgradeable power: three tiers (decision `tfast_sc_chosen_deepen_power`),
  improvements reaching both the modifier and True Death odds.
* Succession: living **direct descendants only** - children, then
  grandchildren, then great-grandchildren; eldest-first within each depth.
  Cousins and unrelated branches are never selected. Extinction is explicit
  (`tfast_sc.0404`) and final.
* True Death: only from an awakened chosen, only while at war with the
  Hollow; the Overlord seals instead of dying.

## 6. Signature abilities of the Ten (Sprint 6)

* Morvath - bounded reinforcement during a Reckoning (one extra wave of
  reanimated dead; hard cap through `tfast_sc_reckoning_waves`).
* Kaedryn - frost follows Hollow raids (50% county frost modifier).
* Vaelor, Draven, Tharion, Seralyth, Nyxara, Velmora, Eryndra, Malethra -
  declared in bloodline traits and council variables; **scaffolded** for V2
  (their hooks and data exist; only two signature effects are wired live, by
  design scope).
* All supernatural men-at-arms are Hollow-flag-gated with hard `max` caps;
  the player's countermeasures are pikes/heavy infantry vs knights and
  hordes, archers vs wraiths, and the Great Wall vs scripted entry.

## 7. Living world (Sprint 6)

* Eternal Court variables (loyalty, ambition, grievance, influence, readiness,
  bloc) with yearly drift, personality tempering, sibling-destruction grief.
* Rare rebellion: loyalty <= 20 AND grievance >= 60 AND readiness >= 50 AND
  landed AND no active rebellion AND 30-year cooldown; 2% roll per year.
  Fought as a real claim war (`claim_cb` pattern, vanilla-verified).
* Memory: raid-defeat, wall-defense, wall-breach, true-death and raided
  memories are stored as bounded variables; `tfast_sc_tell_the_tale` and
  `tfast_sc.0700` reference the actually-saved state (no invented recall).
* Refugees: `tfast_sc.0202` relief decisions spawn a refugee courtier with a
  pressed claim on a county the Hollow stripped.
* Crisis diplomacy: the captured-immortal event chain (`tfast_sc.0600`) is
  the only direct Hollow-mortal negotiation; tribute is never a service.
* Performance: director ticks are 60-300 days apart, every population is
  capped, dead-character scopes are never addressed from persistent state
  (role status globals), and no daily map scans exist anywhere.

## Deliberate non-goals (documented, not missing)

* No fabricated provinces, no new map, no new art assets (vanilla icons and
  illustrations only, so the mod cannot break on missing textures).
* No native-raiding hijack: 1.20 gates native raiding to tribal/nomadic-style
  governments; the scripted raid director is the mod's only raiding path.
* No routine Hollow diplomacy, no tribute-as-service, no permanent
  "unplayable" engine marker for AI-only enforcement.
