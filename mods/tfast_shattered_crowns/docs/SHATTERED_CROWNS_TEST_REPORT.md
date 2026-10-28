# Shattered Crowns - Validation and Test Report

Everything below is either **evidence** (a command run against the installed
game, with its result) or **explicitly marked as not tested**. Nothing is
claimed that was not executed or read.

## 0. Environment

| Item | Value | Source |
|---|---|---|
| Game install | `C:\Games\ckIII` | directory listing |
| Build | `release/1.20.0` | `logs/code_revisions.log`, `logs/game.log` |
| User dir | `C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III` | directory listing |
| TFAST workspace | the shared `mod/` directory (8 existing modules inventoried) | directory listing |
| Mod under test | `mod/tfast_shattered_crowns`, registered first in `dlc_load.json` (backup kept at `docs/dlc_load.backup.json`) | file edit |

Sprint 0 discovery also inventoried the existing TFAST modules for ID
collisions (`tfast_sc` prefix: zero matches before this mod) and read their
conventions (BOM, `ai_check_interval = 0`, header comments) to match them.

## 1. Syntax verification against the installed game (evidence)

Every API below was verified by reading the *installed* 1.20 data - not from
memory. Highlights (file -> what was proven):

* **on_action chaining** - `common/on_action/_on_actions.info`: the documented
  `vanilla = { on_actions = { mod } }` append pattern; `on_game_start`,
  `on_game_start_after_lobby`, `yearly_playable_pulse`, `on_birth_child`,
  `on_death` all confirmed as real on_action names.
* **Story cycles** - `_story_cycles.info` + `story_cycle_almohad_invasion.txt`:
  `create_story`, `make_story_owner`, `story_owner = var:x`, `on_owner_death`,
  `effect_group { days trigger triggered_effect }`, `end_story`.
* **Characters** - `10_dlc_tgp_japan_scripted_effects.txt`, `00_invader_templates.txt`,
  `bookmark_events.txt`, `birth_events.txt`: `create_character` param set
  (template/name bare string/location/employer/dynasty_house/rite),
  `create_dynasty`, `set_house_name`, `set_father = scope:x`,
  `set_immortal_age` (effect_localization), templates in
  `common/scripted_character_templates`.
* **Titles** - `00_almohad_invasion_effects.txt`, `00_decisions_effects.txt`:
  `create_title_and_vassal_change` (types `usurped`/`granted`/`independence`
  used peacetime), `change_title_holder { take_baronies }`,
  `becomes_independent { change }`, `change_liege`, `resolve_...`.
  Stronghold counties and baronies verified in `00_landed_titles.txt`:
  `c_bornholm`/`b_ronne`, `c_rugen`/`b_rugen`+`b_stralsund`,
  `c_isle_of_man`/`b_castletown`, `c_osel`, `c_anglesey`.
* **Global variables + lists** - `00_mongol_invasion_effects.txt`,
  `00_diarchy_scripted_effects.txt`, `07_ep3_wars.txt`:
  `set/change/remove_global_variable`, `set_variable` with `years`,
  `add_to_variable_list { name target }`, `clear_variable_list`,
  `is_target_in_variable_list { name target }`,
  `every/ordered/random_in_list { variable ... }`,
  `ordered_in_list { position order_by save_scope_as }`,
  `var:a >= var:b` comparisons, `value = var:` and `value = global_var:`.
* **War** - `00_invasion_war.txt` (mongol CB), `00_event_war.txt` (sons CB),
  `00_mongol_invasion_effects.txt`, `30_mongol_invasion_decisions.txt`:
  custom CB layout (`valid_to_start`, `should_invalidate`, `on_victory` with
  `random_in_list` of `target_titles`, `allowed_for_character`),
  `start_war { cb target target_title }`, `using_cb`, `any/every_character_war`,
  `end_war = white_peace` (war scope), `add_pressed_claim`,
  `random_neighboring_top_liege_realm_owner`.
* **Effects used one by one** (each found in installed script):
  `imprison { target type }`, `release_from_prison`, `death = natural`,
  `add_county_modifier { modifier years }`, `remove_county_modifier`,
  `has_county_modifier`, `change_county_control` with the verified script
  values (`miniscule/minor/medium/major/extreme_county_control_loss`),
  `change_development_level = n`, `add_gold = { value multiply }`,
  `add_stress = n`, `add_tyranny = medium_tyranny_value`, `add_opinion`,
  `stress_impact { base = medium_stress_impact_gain }`,
  `spawn_army { men_at_arms { type men { value } } levies }`,
  `create_maa_regiment` (pattern), `send_interface_toast { type title left_icon }`,
  `random = { chance = <script value> }`, `random_list`, `debug_log`.
* **Traits** - `_traits.info` + `00_traits.txt`: `immortal = yes`,
  `no_prowess_loss_from_age`, `prowess = n`, `dread_baseline_add`,
  `shown_in_ruler_designer`, desc blocks, `TRAIT_FLAG_DESC_<flag>` loc rule.
* **Modifiers** - every key used appears in vanilla modifier files
  (`fort_level`, `defender_holding_advantage`, `county_opinion_add`,
  `development_growth_factor`, `monthly_county_control_*`,
  `knight_effectiveness_mult`, `dread_gain_mult`, `legitimacy` replaced by
  `monthly_legitimacy_add` after the check would have failed - see §4).
* **Men-at-arms** - `_men_at_arms_types.info` + `00_maa_types.txt`: field set,
  `can_recruit` gating, `max`, costs, counters, terrain_bonus, existing
  illustration names only.
* **Religion in 1.20 layout** - `religion/religion_types|rite_types|faith_types`
  `.info` files + `00_hellenism.txt` + `00_faith_types.txt` + `00_rite_types.txt`:
  religion-level doctrine lists, scripted main rite with tenets,
  `faith_details`, `cultures`; doctrine keys used (`doctrine_monogamy`,
  `doctrine_divorce_disallowed`, `doctrine_consanguinity_unrestricted`,
  `doctrine_gender_equal`, `doctrine_pilgrimage_forbidden`,
  `doctrine_no_head`, `doctrine_theocracy_temporal`,
  `pagan_hostility_doctrine`, ...) each located in `doctrine_types/`;
  tenets `tenet_divine_marriage`, `tenet_esotericism` located in
  `tenet_types/`; icon file `custom_faith_pentagram.dds` confirmed present.
* **Game rules** - `_game_rules.info` + `00_game_rules.txt` structure; the
  `has_game_rule = <setting>` shorthand exactly as used by vanilla in
  `on_action/game_start.txt`.
* **Events** - vanilla character-event layout, `hidden = yes` with `immediate`,
  required `theme` (the sibling TFAST log plainly shows the failure mode:
  *"Theme missing in event"*), valid themes list read from `00_event_themes.txt`.

## 2. Automated internal consistency checks (all executed, all passed)

| Check | Method | Result |
|---|---|---|
| Event IDs referenced vs defined | regex over all script + events | 24/24 defined, 0 dangling, 0 unused |
| Scripted effect/trigger calls vs definitions | regex `name = yes/no` + param calls | 52 calls, 0 missing definitions |
| Loc keys: traits (+flags), modifiers, MAA, decisions | generated key sets vs yml | 0 missing |
| Loc keys: events (titles/descs/options/toasts/tooltips) | regex vs yml | 0 missing |
| Loc keys: game rules, religion/rite/faith, casus belli | generated sets vs yml | 0 missing |
| Brace balance, every .txt file | count `{` vs `}` | 0 unbalanced |
| UTF-8 BOM, every .txt/.yml | byte check | 31/31 files BOM |
| ID collision scan vs sibling TFAST mods | `tfast_sc` search | 0 collisions |

Two real defects were found by these checks and fixed during the build:

1. `small_county_control_loss` did not exist - replaced with the verified
   `miniscule_county_control_loss` in the devastation effect.
2. `legitimacy = 5` is not a modifier key - replaced with the verified
   `monthly_legitimacy_add = 0.2` in the tale modifier.

Also fixed by review: saved-scope references in the repair path (now global
variable references), spawn-army stronghold assignment fallback, prophecy
cousin-exclusion rule (direct-descendant gate now uses the persistent
`tfast_sc_last_chosen`), and scope-order in the bootstrap dynasty creation.

## 3. In-game load test - attempted, INCONCLUSIVE (environment)

The attempt: launch `C:\Games\ckIII\binaries\ck3.exe -debug_mode` directly to
reach the main menu (which loads all databases, mods included) and read
`logs/error.log`.

Observed: the process started, opened its window, and then sat at full CPU for
more than ten minutes without writing a single byte to any log file
(`game.log`, `error.log`, `setup.log`, `code_revisions.log` all remained 0
bytes; the launch rotated/truncated these diagnostic logs, which is normal -
they refill on the next launch). The game never reached database loading, so
**no mod-related result can be drawn from this run**. It was stopped.

Interpretation: this is a **launch-path issue in this setup** - this install is
normally started through its launcher, and the bare-exe path stalls before
initialisation in this environment. It is not evidence about the mod either
way.

### How to complete the verification (5 minutes, in-game)

1. Start CK3 the normal way (launcher) and enable **TFAST Shattered Crowns**
   (already in the playset).
2. New campaign, any start date; pause at day 1.
3. Expected within the first day:
   * `debug.log` contains `TFAST Shattered Crowns: the Hollow Dominion has
     been bootstrapped`;
   * three island counties (Bornholm / Rugen / Isle of Man, or the fallback
     islands) turn Hollow-violet and gain the *Hollow Stronghold* modifier;
   * the decisions list shows **Plan the Great Wall** and, if bootstrap
     failed for any reason, the one-time **Raise the Hollow Dominion** repair
     decision;
   * the game rules list shows the three *Shattered Crowns* rule groups.
4. Search `error.log`/`debug.log` for `tfast_sc` and for
   `Theme missing in event` - expected: no theme errors.
5. Fast-forward a few years unpaused: peacetime raids should produce the
   "The Host Comes for Your Stores" event against neighboring rulers,
   including the player when reachable.

## 4. Explicitly NOT verified (honest list)

These are judgment calls built on the documented patterns but **not observed
running** in this session:

* The `on_actions = { ... }` chaining actually merging at runtime (it is the
  game's own documented mechanism; the one-time `Raise the Hollow Dominion`
  decision exists specifically so a failure here cannot kill the campaign).
* `has_game_rule = <custom setting>` affecting script (failure mode is benign:
  standard/enabled defaults).
* `dynasty_house = global_var:x` accepting a runtime house scope (the almohad
  precedent uses a database house; the runtime-scope form is expected to work).
* `ordered_in_list { variable position order_by save_scope_as }` in the exact
  combined form (all features individually verified).
* `start_war { cb = claim_cb ... }` for the rare baron-vs-liege rebellion case.
* Multi-realm usurpation + independence sequencing in the stronghold seating
  (follows the verified almohad game-start pattern; the repair pass retries).
* Balance numbers (raid gold percentages, wave sizes, council drift rates):
  tuned by construction, not by playtesting.
* Multiplayer.

## 5. Acceptance criteria map (build spec section 8)

| Criterion | Status |
|---|---|
| Mod loads and runs in 1.20.0.3 with no database errors | **Static: yes** (all checks). In-game: see §3 - must be confirmed by one normal launch |
| Hollow AI-only in supported normal play paths | By construction; documented limits (§COMPATIBILITY 2.2) |
| Hollow dynasty has successors and its family persists | Implemented (birth bloodlines, awakening at 16, closed-bloodline faith) |
| Reckoning invades with real wars and waves, resolvable without the chosen | Implemented (script-only CB + 3-wave cap + explicit retreat) |
| Wall gates block scripted entry until breach; dev/test events cause breach; repair works | Implemented; breach path is the only bypass |
| Awakened chosen satisfies all lineage rules; no ordinary mortal can True Death | Implemented; enforced at the single kill site |
| Chosen line extinction is explicit | Implemented (`tfast_sc.0404`) |
| Saves remain stable | By design (bounded variables, role registries, no dead-scope references); not soak-tested |
| Unsupported versions fail safely | `supported_version = "1.20.*"`; the mod makes no removals, so an unsupported newer version can only lose functionality, not corrupt data |
| Conflicts documented | `docs/SHATTERED_CROWNS_COMPATIBILITY.md` |

## 6. Hidden gold — 12 October 2026

Static check: `validate_mod.py` against `C:\Games\ckIII`. The gold files added no new errors. The checker still fails the whole mod on the old trait-icon false positives (it only looks in the vanilla icon folder) and on `holy_sites_min`, which `_religion_types.info` documents as a religion field.

Runtime, one normal launch of `ck3.exe`, then a campaign start (the log shows `on_game_start` and an AI coronation activity):

* `debug.log` at 02:50:57 records `tfast_sc_seed_gold_deposits_effect`: "gold deposits seeded".
* `error.log` from that launch has no line naming the gold effects, the gold decisions, or events `tfast_sc.1000`–`tfast_sc.1002`.

Not done, so not passed: clicking Question the Capital's People, hiring surveyors, opening a working, saving and reloading, or an observer campaign of any length.

The same launch logged one pre-existing bootstrap fault: `create_dynasty` at `tfast_sc_bootstrap_effects.txt` line 42, "Head of the house trying to create a new dynasty," then an undefined `tfast_sc_hollow_dynasty` scope. A guard was added afterward so an Overlord who already heads a house keeps that dynasty and the house is renamed. That guard has not been loaded by the game yet.

