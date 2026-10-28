# Shattered Crowns - Changelog

## 1.5.1 - adventurers can see the menus

### Fixed
* Landless adventurers could not open the handbook or the automation menu
  (and could not see the AI Suite cheat menu), because the menu shells were
  hidden behind `is_landed = yes` - found from a live 1066 adventurer
  campaign. The shells, the automation switches and the handbook are now
  player-gated only.
* The AI Suite cheat kit for adventurers: gold, prestige, piety, renown,
  legitimacy, dread, Golden Age (its development pulse skips without land),
  skills, stress, tyranny, and Expand Men-at-Arms now work landless too.
  Landed-only tools (walls, domain development, instant building,
  government switches, Raise a Host) keep their gates and simply stay
  hidden.

## 1.5.0 - the Hollow Tide in the Situations window

### Added
* A full 1.20 Situation, `tfast_sc_hollow_tide`: "The Hollow Tide" now
  appears in the Situations window (Major group) for every landed ruler,
  with six chapters - Predatory Peace, Escalation, The Great Reckoning,
  Aftermath, The Long Dark, The Uprising - and two participant groups
  (The Roofed World / The Hollow Dominion).
* Seven named catalysts drive the chapters, fired from the crisis scripts
  at the exact moments the crisis state changes: escalation, reckoning,
  aftermath, dark, uprising, dawnbreak, peace. No divergence: the window
  always mirrors `tfast_sc_crisis_phase`.
* Nine new DDS icons (sub-region, groups, six phases) from the usual
  Pillow + quicktex pipeline (`tools/build_situation_icons.py`); no custom
  GUI is needed - the generic `window_situation` is used.
* Started once per world by the director with a flag guard, so the
  situation also appears in saves that predate it (no new campaign needed).

### Validation
* `validate_mod.py`: 62 script files, 2 localization files, 709 keys, exit 1
  with only the two documented false-positive classes. `check_modset.py`:
  no clashes. Status: STATICALLY_VALIDATED - confirm the window entry on the
  next live session.

## 1.4.0 - the world stops feeling scripted

### Added
* DeepSeek-generated flavor pools: 24 lines in
  `tfast_sc_flavor_generated_l_english.yml` (eight raid omens, eight dark
  omens, eight court whispers), regenerable with
  `python C:\Games\ck3-ai-automation\tools\tfast_flavor_deepseek.py`
  (reads DEEPSEEK_API_KEY from the environment or the tooling `.env`; falls
  back to a built-in pool when offline, so the mod always has content).
* Drawn omens in game: the raid warning (tfast_sc.0100) shows one of eight
  rolled lines; tfast_sc.0920 shows one of eight dark omens during the Long
  Dark; tfast_sc.0921 shows one of eight whispers in peacetime.
* An unpredictable Host: each raid season the Overlord rolls a temper -
  bold (+8 raid strength), measured, or cautious (-8) - and one year in
  five its goal is caprice: any of the five, for no reason. The AI stops
  repeating itself.

### Validation
* `validate_mod.py`: 60 script files, 2 localization files, 677 keys, exit 1
  with only the two documented false-positive classes.
* Status: STATICALLY_VALIDATED.

### Fixed (found in the first live session)
* The generated flavor file needed the engine-required `_l_english.yml`
  suffix — renamed to `tfast_sc_flavor_generated_l_english.yml`; the pools
  now load instead of logging "Unrecognized loc key" at startup.
* Removed the scripted AI frequency from the six player-only interactions
  (the five AI Suite grants and the chest-keeper naming): the engine logged
  "'ai_frequency' … but no 'ai_targets', won't be used" for each. They are
  gated on player actors in `is_shown`, so the blocks were noise.
  Both fixes are save-compatible; restart to apply.

## 1.3.0 - the in-game handbook

### Added
* "TFAST Handbook: Open/Close" with eight chapters (Getting Started, The
  Hollow Dominion, Raids and Defense, The Great Wall, The Great Reckoning,
  The Long Dark and the Uprising, The Host's Goals and Hiding, Your Toolbox),
  a chapter list, per-chapter pages and a Back decision - the same
  open/close flag-menu pattern as the cheat and automation menus.
* Every chapter's text states the prices and rules the scripts actually
  enforce, including the mercenary tiers, automation switches, resistance
  numbers (8 / 14), hiding's 5 years and 150 prestige, and pointers to the
  AI Suite (cheat menu, right-click grants for any ruler including AI
  rulers) and TFAST History.
* New plumbing: `tfast_sc_help_any_page_open_trigger`,
  `tfast_sc_help_clear_pages_effect`.

### Validation
* `validate_mod.py`: 59 script files, 647 localization keys, exit 1 with only
  the two documented false-positive classes. Status: STATICALLY_VALIDATED.

## 1.2.0 - the Host wants things; the realm runs itself

### Added - Hollow goals (the Host is an actor now)
* A yearly goal director for the Overlord: vendetta (whoever beat him is
  marked for 50 years and raided hard), hunt (find whoever is hiding), blood
  (feed on neighbours: development, lives, readiness), terror (dread
  campaigns), treasure (the default).
* The Ten each carry a yearly obsession that colours their court drift.
* A lost war (CB on_defeat) or a thrown-back raid now sets a real vendetta,
  so the Host pursues those who made it lose.

### Added - hiding from the Host
* "Go Into Hiding" / "Come Out of Hiding": five years of concealment (raid
  targeting weight -200) at the price of 150 prestige and court standing.
  The hunt finds you anyway - hiding buys time, never safety.

### Added - the automation menu
* Seven toggles in one open/close menu (maintain wall, reinforce wall,
  rebuild counties, tell the tale, rise against the Hollow, break blockades,
  hire mercenaries). The yearly pass does only what the matching decision
  could do, at the same prices, keeping a gold reserve. Player-only flags;
  the AI never sees the menu.

### Changed
* Reckoning defeat and white-peace outcomes and raid-defense results now feed
  the vendetta system instead of being recorded and forgotten.
* The rebuild and tell-the-tale decisions share scripted effects with the
  automation (same behaviour, one source).

### Validation
* `validate_mod.py`: 57 script files, 603 localization keys, exit 1 with only
  the two documented false-positive classes. `check_modset.py`: no clashes.
* Status: STATICALLY_VALIDATED - the third-pass systems have not been clicked
  through in a running game yet.

## 1.1.0 - the Long Dark, the uprising, the walls, and the mercenaries

### Added - the Long Dark (Hollow victory)
* The Great Reckoning can now be LOST: if any front falls to the Host, the
  aftermath hands off to crisis phase 6 - the Long Dark - unless the new
  "Shattered Crowns: The Long Dark" game rule is Off.
* Bounded yearly world decay: plague, famine and poverty county modifiers,
  development and control loss, and occasional plague deaths. AI rulers get
  one small roll per year; the human player's realm gets events instead of
  silent rolls.
* The Hollow tithe event (pay gold, or refuse and burn), the fever year
  (tend / seal / let it burn), and the blockade of wall counties ("The Roads
  Are Cut") with the "Break the Blockade" decision.
* Defeat consequences wired both ways: the Reckoning outcome variables now
  feed the dark-age logic, and the dark logic consumes them.

### Added - the uprising and the comeback
* A dedicated resistance meter (`tfast_sc_dark_resistance`), fed by deeds
  only: rising +2, a seat torn from the Hollow +3, a thrown-back raid +1, a
  wall that holds +1, refusing the tithe +1. At 8 (or 20 dark years) the
  world rises; at 14 the Long Dark breaks.
* The uprising grants pledged rulers a real host, bleeds the Host yearly,
  and ends with the Host's retreat, a reopened prophecy window, and the
  Spirit of the Uprising for those who endured.
* "Storm a Hollow Stronghold": a real claim war for one of the three seats,
  with volunteers, available to any landed ruler during the dark.

### Added - wall projects
* "Reinforce the Wall": two refits for a standing wall (fort level and
  defender advantage refaced on every wall county).
* "Dismantle the Wall": the sponsor may tear down their own project
  (-100 prestige, everything removed, nothing refunded).
* The Hollow demolish walls in the dark: staged assaults reduce integrity,
  downgrade the wall stage by stage, and can unmake it entirely (county
  modifiers and the project record removed, world notified).

### Added - mercenaries for hire
* Three gold-scaled tiers - Free Company (250 gold / 2,000 levies + 250
  bowmen), Great Company (800 / 8,000 + 500 bowmen + 500 light horse), Host
  of Fortune (2,000 / 20,000 + 1,000 + 1,000) - available to any landed
  ruler anywhere, sharing one two-year cooldown. Hosts use supply and
  attrition like ordinary armies; nothing is upkeep-free.

### Changed
* The aftermath recovery in the watch effect now clears crisis phase 5 only;
  the Long Dark is not auto-cleared and must be broken by the uprising.
* The Reckoning outcome variables (`attacker_won`, `attacker_lost`,
  `stalemate`) and `rebellion_result` are now read by the dark-age logic
  instead of being recorded and forgotten.

### Validation
* `validate_mod.py`: exit 1 with only the two documented false-positive
  classes (mod-local trait icons, `holy_sites_min`); 52 script files,
  518 localization keys. `check_modset.py`: no path/name/loc clashes.
* Status: STATICALLY_VALIDATED - the new systems have not been clicked
  through in a running game yet.

## 1.0.0 - first complete TFAST build (CK3 1.20.x / release-1.20.0)

### Added - the Hollow Dominion
* Bootstrap of the Supreme Immortal Overlord (Vaelos) and the ten original
  children with full family ties, closed-bloodline faith, island strongholds
  usurped from AI rulers only, and full repair/idempotency passes.
* The Hollow Communion religion with its own rite and faith
  (`doctrine_consanguinity_unrestricted` + `tenet_divine_marriage` for the
  closed bloodline), no holy sites, no head, no fervor interaction with any
  real faith.
* 13 traits: Hollow Immortal, Awakened, Watchman of the Great Wall, and one
  bloodline trait per original child.
* 6 supernatural men-at-arms, all Hollow-flag gated with hard caps and reused
  vanilla illustrations.
* `tfast_sc_hollow_immortal` uses the engine's own `immortal = yes`; newborn
  Hollow receive the trait at adulthood so visual age and fertility behave.

### Added - raiding
* Scripted raid director with dynamic target scoring (wealth, distraction,
  weakness, exhaustion, walls, readiness), yearly budget, per-target cooldown
  and exhaustion, real warning event with defense stance, and three-tier
  resolution: thrown back / contested / overrun.
* Raid outcomes: gold transfer, county control loss, Stripped by the Hollow
  county modifier, prisoner raids (35%), Kaedryn's frost (50%).
* Wall-first routing: scripted entry against an intact walled gate is blocked
  and resolved as a wall assault instead.

### Added - the Great Reckoning
* Crisis phase machine with foretelling (2 years of warnings), a real war via
  the script-only `tfast_sc_reckoning_war` CB, one primary (human player) plus
  at most one secondary front, and three bounded waves including Morvath's
  reinforcement.
* Resolution on any war outcome into the aftermath: retreat, banishment
  window, 40-year cooldown, prophecy window opening, refugee relief event.
* Overlord sealing (never death), Eternal Regency, and the later "the Hollow
  stir again" resurgence.

### Added - the Great Wall
* Five-stage project (planning, towers, rampart, gates, wards) over the
  sponsor's capital plus up to three own counties in the duchy - existing
  counties only.
* Integrity and upkeep economy, breach handling with world notification,
  repair decision, rehanging the gate, and the Last Watch watch commander.
* Documented engine limits: blocks this mod's scripted raids and slows sieges;
  cannot change vanilla pathfinding (stated in-game and in the docs).

### Added - the prophecy and True Death
* Hidden chosen marked at a qualifying post-Reckoning birth (30-360 day
  randomized delay), never public before awakening.
* Awakening at 16, or at 12+ under war/imprisonment; three-tier power via
  decision; True Death odds driven by tier and prowess.
* Succession strictly along the direct bloodline (children, grandchildren,
  great-grandchildren; eldest first); cousins never selected; extinction is
  explicit and final.
* True Death is the single kill site for Hollow immortals; the Overlord is
  excluded there and can only be sealed.

### Added - living world
* Eternal Court variables with yearly drift, personality tempering and
  sibling-destruction grief; five blocs; rare rebellion with hard
  prerequisites (loyalty <= 20, grievance >= 60, readiness >= 50, landed,
  30-year cooldown) fought as a real claim war.
* Dynasty memory (raid defeat, wall defense, wall breach, true death, raided)
  with bounded retention; "Tell the Tale" decision and follow-up event driven
  by the actually-saved memories.
* Captured-immortal crisis diplomacy (release/execute-seal/hold), refugee
  court arrivals with claims on the counties the Hollow stripped, and the
  World Council pledge.
* Banished children may return years later (new instance, same name and role;
  logged explicitly).

### Added - infrastructure
* Three game rules (Reckoning timing, Hollow strength, prophecy on/off).
* One-time fallback decision "Raise the Hollow Dominion" as a safety net that
  does not depend on any on_action hook.
* Full English localization, UTF-8 with BOM; descriptor registered in the
  TFAST playset `dlc_load.json` (backup retained in `docs/`).
* Documentation: design + feature matrix, compatibility report, story guide,
  and the validation/test report with an honest untested list.

### Fixed during the build (caught by validation)
* `small_county_control_loss` -> `miniscule_county_control_loss` (the former
  does not exist in 1.20).
* `legitimacy = 5` modifier -> `monthly_legitimacy_add = 0.2` (verified key).
* Repair-path saved-scope references -> global variable references.
* Bootstrap scope ordering for dynasty creation.
* Prophecy cousin-exclusion via the persistent last-chosen registry.
* Spawn-army stronghold assignment fallback for missing stronghold slots.
* All event themes present (a sibling TFAST module logged "Theme missing"
  without one).

### Known limitations (carried by design)
* In-game load/play verification pending one normal launcher start - see
  `docs/SHATTERED_CROWNS_TEST_REPORT.md` section 3.
* Native CK3 pathfinding cannot be walled; documented.
* Inbreeding uses vanilla rules for the closed bloodline.
* Artifact raids and eight of the ten signature abilities are scaffolded for
  a future version (Morvath and Kaedryn are live).
