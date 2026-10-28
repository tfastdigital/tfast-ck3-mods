# Shattered Crowns handoff

Written 12 October 2026. Cheat-menu pass added the same day. This is the state of the files, not a claim that a new campaign has been played.

Statuses mean what they say. STATICALLY_VALIDATED is not VERIFIED. Do not mark a click, a portrait, or a shield as seen until a new campaign after a full reload has shown it.

## Where things live

| Thing | Path |
|---|---|
| Game | `C:\Games\ckIII` — Crusader Kings III 1.20.0.3 Crozier |
| Live mod | `C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III\mod\tfast_shattered_crowns` |
| Cheat suite | `...\mod\tfast_ai_suite` |
| Art library | `C:\Games\SHATTERED_CROWNS_ARTWORK` |
| Logs | `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\logs\` |
| Validator | `python C:\Games\ck3-ai-automation\tools\validate_mod.py "<mod>" --game C:\Games\ckIII` |
| This status table | `docs\BUILD_STATUS.md` |

Script `.txt` and localization `.yml` must be UTF-8 with BOM. `has_game_rule` uses the setting key. An unset `var:` comparison must be guarded by `has_variable` first. Do not invent event IDs. Do not overwrite vanilla files or existing TFAST assets. Do not replace vanilla gold, the map, succession, cultures, or religions.

## Last static check

`validate_mod.py` on `tfast_shattered_crowns` after the third pass: 57 script files, 603 localization keys, exit code 1.

The only errors are the old false positives. Do not "fix" them:

- Trait icons `tfast_sc_icon_*.dds` "do not exist". The validator only looks in vanilla `game/gfx/interface/icons/traits`.
- `holy_sites_min` reported as an unknown trigger. It is a valid religion-type field.

`tfast_ai_suite` was re-validated after the cheat-menu pass: 10 script files, 139 localization keys, exit code 0. Before the menu it was 9 script files and 107 keys.

## What a running game will not show

A campaign that was already open when these files were written loaded the older scripts. Quit fully and start a new campaign before judging any of this:

- Hollow dynasty, personal houses, DNA, crowns, armor, shields.
- Gold rumor, survey, and opening a gold working.
- Iron, stone, timber, grain, the neighbor scout, and the family chest.
- The TFAST AI Suite cheat menu (Open → five pages → Back / Close).

The gold seed itself did write a debug-log line during an earlier campaign start. That is the only economy action with a runtime trace. Survey and opening a working were not clicked.

## Court, faces, crowns, shields

Written into the mod. Not looked at in a new campaign.

- Predefined dynasty `tfast_sc_hollow_dynasty` and house `tfast_sc_hollow_house`. The ten children each have `tfast_sc_house_<id>` under that dynasty. Personal shields need separate houses because clothing colors follow house and title colors.
- DNA donors are born 1 January 1 and dead 1 January 2. Templates copy inheritable appearance from `character:tfast_sc_dna_<id>`. Faces share Halfdan Whiteshirt's morph. There is no scar gene in vanilla DNA (`gene_scars_battle` is unused).
- Displayed age via `set_immortal_age`: Vaelos 58; Vaelor 42, Morvath 48, Kaedryn 36, Draven 40, Tharion 50, Seralyth 43, Nyxara 34, Velmora 46, Eryndra 38, Malethra 35. Template `age` fields are still the older numbers (41 for the Overlord, 24–34 for the children). A child brought back still freezes at visual age 30.
- Coat of arms: broken iron ring, gap at one o'clock. Eryndra is the only royal with a complete ring. Usurped seats call `set_coa` with a house or dynasty key. Do not write `limit = { $IDX$ = 1 }`. After substitution that becomes a bare number, which is not a trigger.
- Portrait group `tfast_sc_royal_outfit` (`usage = game`, `selection_behavior = max`, `priority = 8`) locks vanilla clothes, headgear, cloaks, and legwear when the character has `tfast_sc_outfit_<id>`. The flag is set on creation and again in repair for the original children only, so descendants do not wear the eleven crowns. Prison and the naked trigger still win. War and prison outfit tags can still replace the court look because `ignore_outfit_tags` is not set.
- The portrait window uses the game's own crown and armor meshes. The painted crown is a picture. It is not a `.mesh`, and it is not worn.

## Economy that is in the mod

Game rule `tfast_sc_economy`, settings `tfast_sc_economy_on` and `tfast_sc_economy_off`. Deposits are county variables, not a second currency. One county tax modifier each. Vanilla `generic_gold_mines_01` blocks a second gold-mine modifier, which is why these are tax modifiers.

Knowledge runs 0–4. A rumor is one step. A survey raises knowledge. Opening a working sets knowledge to 4 and adds the tax modifier. No daily world scan. No infinite resources. No duplicated gold.

| Kind | Type value | Counties (richness) | Tax when opened |
|---|---|---|---|
| Gold | 1 | Bambuk 3, Bure 3, Allaqi 2, Altay 2, Carmarthenshire 1, Astorga 2 | 5% / 10% / 15% by richness |
| Iron | 2 | Västmanland 3, Hereford 2, Toledo 2 | 8% |
| Stone | 3 | Dorset 2, Bayeux 3 | 6% |
| Timber | 4 | Dalarna 3, Värmland 2, Nottinghamshire 2 | 6% |
| Grain | 5 | Chartres 3, Fayyum 3, Agrigento 2 | 8% |

Gold decisions: Question the Locals, Survey the Capital, Survey the Rumored County, Open the Gold Working. Events `tfast_sc.1000`–`tfast_sc.1002`.

Resource decisions: Survey a Resource County (75 gold, 730-day cooldown), Open the Resource Working (150 gold), Scout a Neighboring County (50 gold, 365-day cooldown). Events `tfast_sc.1010`–`tfast_sc.1013`. The scout looks at one neighboring county of a random held county. If that neighbor already has a deposit at knowledge 0, it becomes a rumor. The scout does not create a deposit and does not take land.

Aetherstone is not built.

## Chest, inheritance, banking

Family chest, in the mod, statically checked, not clicked:

- Set Aside a Family Chest costs 200 gold. That gold leaves the treasury. Variable `tfast_sc_chest` records it.
- Open the Family Chest pays 200 gold back and subtracts it from the variable.
- Right-click Name Keeper of the Chest sets `tfast_sc_financial_heir`.
- On death, a loop pays 200 gold at a time (guarded at 40 passes) to the keeper if alive, otherwise to `primary_heir`.

Ordinary treasury gold still follows vanilla succession. A trust that leaves gold in the treasury and also spends a variable was not built. That would spend the same gold twice.

Banking and loans are Counting House, workshop folder `pdx_156899`, already a 1.20 mod. It was not copied into Shattered Crowns. Enable it beside this mod. Copying it would load the bank twice.

Population bookkeeping is Population Foundation, `pdx_162659`, already 1.20. Same rule: leave it as its own mod.

## Cheat menu, in TFAST AI Suite

All cheats and automation tools now sit behind one Daddy Pika-style flag menu. Player-only: `is_ai = no`, `ai_check_interval = 0`. Achievements are disabled the same way the debug console disables them. Nothing on a page is visible until the menu is open, and one page is open at a time.

The shell is `common/decisions/04_tfast_menu.txt` (10 decisions, `sort_order` 8990–8997). It is pure character flags — `tfast_menu_open` and `tfast_menu_page_*` — so the menu resets on succession. The trigger `tfast_menu_any_page_open_trigger` and effect `tfast_menu_clear_pages_effect` live in `tfast_triggers.txt` / `tfast_effects.txt`. Every cheat in the other decision files now carries the two flag checks in its `is_shown`.

```text
TFAST Cheat Menu: Open          (8990)
 ├─ Cheat Menu: Resources       (8992)  gold / prestige / piety / renown / legitimacy / dread / influence / Golden Age
 ├─ Cheat Menu: Domain          (8993)  development x3 / building slots / instant building
 ├─ Cheat Menu: Military        (8994)  raise a host / expand men-at-arms
 ├─ Cheat Menu: Character       (8995)  skills / stress / tyranny
 ├─ Cheat Menu: Realm           (8996)  grant excess titles / four government switches
 ├─ Cheat Menu: Back            (8997)
 └─ TFAST Cheat Menu: Close     (8991)
```

Every player-visible entry, by page:

| Page | Cheat | Effect |
|---|---|---|
| Resources | Windfall of Gold | +10000 gold |
| Resources | Legendary Renown | +10000 prestige |
| Resources | Divine Favour | +10000 piety |
| Resources | Dynasty Renown | +10000 renown (prestige if no dynasty) |
| Resources | Unquestioned Right | +1000 legitimacy |
| Resources | A Terrifying Reputation | +100 dread |
| Resources | Political Influence | +1000 influence (administrative governments only) |
| Resources | Golden Age | +10000 gold/prestige/piety/renown, +1000 legitimacy, +150 dread, clears stress and tyranny, +2 development realm-wide, 20-year realm boon |
| Domain | Enrich the Capital | +1 development in the capital county |
| Domain | Develop the Realm | +1 development in every county you rule |
| Domain | Auto: Develop Your Domain | +1 development in your personally held counties only, no vassals enriched |
| Domain | Add Building Slots | +1 permanent slot per held province, repeatable, caps at 10 |
| Domain | Instant Building | one finished new building per held barony with a free slot |
| Military | Raise a Host | 2500 levies, footmen, bowmen, a permanent armored horsemen regiment, levies refilled |
| Military | Expand Men-at-Arms | +1 size to every regiment |
| Character | Sharpen Every Skill | +2 to all five skills and prowess |
| Character | Peace of Mind | clears all stress |
| Character | Absolved of Tyranny | clears all tyranny |
| Realm | Auto: Grant Excess Titles | surplus counties to newly generated local nobles until back inside the domain limit, capital kept |
| Realm | Become Feudal / Tribal / Clan / Administrative | switches government |

Outside the menu: the right-click grants — Grant Gold (1000), Grant an Army, Grant a Building, Grant Standing, Grant Skill — stay character interactions (auto-accept, AI frequency 0, grateful opinion 10–20).

The host is `spawn_army` (2500 levies, 5 armored foot stacks, 5 bow stacks, at the capital, uses supply, not inheritable) plus an armored horsemen regiment of size 2 with `check_can_recruit = no`, then `refill_levy`. Instant buildings call `generate_building` on free barony slots. There is no effect that finishes a building already in the construction queue. Add Building Slots is the separate cheat for a full holding. Skills add 2 to diplomacy, martial, stewardship, intrigue, learning, and prowess.

Menu tab art: `gfx/interface/illustrations/decisions/tfast_menu_tab_open/close/page.dds` (1100x440 DXT1), generated by `python C:\Games\ck3-ai-automation\tools\build_menu_tabs.py` — the same Pillow + quicktex pipeline as the Shattered Crowns decision art. New, not viewed in game.

## Workshop mods that were not copied

Folder: `...\Crusader Kings III\mod`, names starting `pdx_`. They are workshop zips.

| Mod | Why it stayed out |
|---|---|
| Daddy Pika's Cheat Menu (`pdx_62824`) | Old cheat menu (v1.9.0.2, 2023). Replaced by the AI Suite cheat menu built this pass. Its `open_tab`/`close_tab` flag pattern is what `04_tfast_menu.txt` follows. |
| Divine Intervention (`pdx_112029`) | Supported 1.16.2.2. A culture-tradition cooldown hook, not a new system. |
| Terra (`pdx_156256`) | 1.19 map, culture, religion, and title replacement. |
| Blood & Shadows (`pdx_159000`) | 1.19 vampire court. Overlaps the Hollow immortals. |
| Counting House (`pdx_156899`) | Keep enabled. Do not merge. |
| Population Foundation (`pdx_162659`) | Keep enabled. Do not merge. |

## Art

Library: `C:\Games\SHATTERED_CROWNS_ARTWORK`. Filenames begin with `tfast_sc_`. No embedded text or watermarks. Original heraldry only. The Chosen has no fixed face or gender. The Overlord can be sealed and is never painted as permanently killed. Mortals do not join the Hollow Host by choice. Art does not use the changelog name Vaelos as a personal name on the plate.

In the library and accepted earlier: art bible, consistency guide, heraldry guide, Winter Wall specification, eleven portraits, dynasty sheet, thirteen heraldic shields, Winter Wall plate, omen and gold-raid drafts, reckoning, awakening, wall breach.

Filed this pass as PNG, not quality-reviewed against the bible, not converted to DDS, not wired as event pictures:

- `01_CHARACTER_REFERENCES\OVERLORD\tfast_sc_overlord_fullbody.png`
- `01_CHARACTER_REFERENCES\OVERLORD\tfast_sc_overlord_crown_closeup.png`
- `08_IMMORTAL_POLITICS\tfast_sc_eternal_court.png`

`14_INTEGRATION_MANIFEST\PRODUCTION_QUEUE.md` still says those three are next. That queue is behind the files. Check the faces, the broken ring, Eryndra's complete ring, and that the court painting has exactly eleven royals before treating them as accepted.

Still unpainted:

- Ten separate full-body plates, one person at a time.
- Batch 2 war pictures that are not already drafted: undead host assembling, Hollow legion reference, mortal defensive victory, Hollow retreat, immortal banishment, Winter Wall gate with two portcullises, Last Watch oath, stronghold awakening. Partial breach, reckoning, omen, and gold raid already have plates.
- Batch 3 Chosen pictures. No fixed face.
- Batch 4 court and living-world pictures.
- Batch 5 icons.
- Economy artwork. None was made for deposits, the chest, or the scout.

Do not invent event IDs to attach a new painting.

## Still postponed or rejected

- Workforce, famine, roads, a second currency, espionage.
- Aetherstone.
- A second bank inside Shattered Crowns.
- A copied population ledger.
- A family trust that spends gold the founder still holds.
- Custom walls that claim to block vanilla pathfinding.
- New 3D crown meshes. The portrait lock is the implementation.

## The Long Dark, the uprising, the walls, the mercenaries (second pass)

**The Hollow can now win for a while.** If any front of the Great Reckoning is lost (the CB sets `tfast_sc_reckoning_attacker_won`), the aftermath hands off to crisis phase 6 — the Long Dark — unless the "Shattered Crowns: The Long Dark" game rule is Off. While it runs:

- the world decays: one small yearly roll per AI ruler (`every_ruler`, chance 4) and a pass over the player's realm — plague, famine, and poverty county modifiers, `change_development_level = -1` rolls, control loss, occasional `death_bubonic_plague` court deaths;
- `tfast_sc.0900` The Hollow Tithe: pay 150 gold, or refuse and burn (capital raided modifier, +1 resistance);
- `tfast_sc.0901` The Fever Year: tend the sick (malady risk), seal the gates (dev loss), or let it burn (two courtiers die);
- `tfast_sc.0902` The Roads Are Cut + "Break the Blockade" decision: wall counties lose their routes until escorts are paid;
- the wall is assaulted (`tfast_sc.0903`): integrity −25 per strike, and when it hits zero a stage comes down — towers, rampart, gates, wards, then the wall is unmade (`tfast_sc.0908`) and the project record is wiped.

**The comeback loop.** Resistance is a dedicated global (`tfast_sc_dark_resistance`), fed by deeds only: Rise Against the Hollow (+2, 2-year cooldown), storming a seat (+3 when a stronghold changes hands), a thrown-back raid (+1), a wall that holds (+1), refusing the tithe (+1). At 8 (or 20 dark years) `tfast_sc.0905` fires — the world rises, pledged rulers get a real host, the Host bleeds yearly. At 14, `tfast_sc.0906`: the Host retreats, the prophecy window reopens for 10 years, and every player keeps the Spirit of the Uprising.

**The walls as projects.** New decisions: Reinforce the Wall (two refits: fort level + defender advantage refaced on every wall county) and Dismantle the Wall (the sponsor takes their own stones down; −100 prestige; everything removed). The Hollow's dark assaults do the demolition from the other side.

**Mercenaries, anywhere.** Free Company (250 gold: 2,000 levies + 250 bowmen), Great Company (800: 8,000 + 500 + 500 horse), Host of Fortune (2,000: 20,000 + 1,000 + 1,000). Any landed ruler, any corner of the world; one shared two-year cooldown; ordinary supply and attrition.

New files: `common/scripted_effects/tfast_sc_dark_age_effects.txt` and `tfast_sc_merc_effects.txt`; `events/tfast_sc_dark_events.txt` (0900–0908); `common/decisions/tfast_sc_dark_decisions.txt` and `tfast_sc_merc_decisions.txt`; 9 modifiers, 3 scripted triggers, 1 game rule, ~100 loc keys. Integration edits: Reckoning end → dark begin + defeat reads; the aftermath recovery now clears phase 5 only (the dark is not auto-cleared); director yearly dark tick; player yearly dark pass; stronghold-loss news; raid/wall resistance hooks.

Status: STATICALLY_VALIDATED. To look at it quickly: start a campaign in debug mode and run in the console
`effect set_global_variable = { name = tfast_sc_crisis_phase value = 6 }`, `effect set_global_variable = { name = tfast_sc_dark_years value = 0 }`, `effect set_global_variable = { name = tfast_sc_dark_resistance value = 0 }` — the dark pass begins on your next yearly tick. The real path is letting a Reckoning front be lost.

## The Host's goals, hiding, the automation menu (third pass, same day)

**The Overlord and the Ten now want things.** Every year the Host picks a goal (`global_var:tfast_sc_hollow_goal`): vendetta (someone made it lose — that ruler is marked `tfast_sc_raid_marked` and the raid director hammers them), hunt (someone is hiding), blood (readiness under 60), terror (dread under 50), or treasure (the default). It then acts: blood feeds drain a neighbouring realm (development, lives, +10 readiness), terror campaigns burn a county's control and raise the Overlord's dread, the hunt finds whoever hid. Each of the Ten carries a personal obsession that colours their court drift (blood → readiness, treasure → influence, terror → grievance, hunt → ambition).

**Vendettas.** Whoever beats the Host is remembered: a lost war (the CB `on_defeat`) and a thrown-back raid both set `tfast_sc_grievance_vendetta` on the Overlord, pointing at that ruler, for 50 years. While it lives, the Host's goal is vendetta and the raid director targets them.

**Hiding.** Two new decisions: Go Into Hiding (5 years, 150 prestige, `tfast_sc_hiding_modifier`) — the raid director passes you over (targeting weight −200) — and Come Out of Hiding. Hiding is not safety: if the Host makes the hunt its goal, the hidden are marked (+60) and event tfast_sc.0912 finds them.

**The automation menu.** Seven switches in one open/close menu: Auto: Maintain the Wall, Auto: Reinforce the Wall, Auto: Rebuild Counties, Auto: Tell the Tale, Auto: Rise Against the Hollow, Auto: Break Blockades, Auto: Hire Mercenaries. The yearly pass (`tfast_sc_automation_yearly_effect`) only ever does what the matching decision could do, at the same prices, and always keeps a gold reserve behind. All switches are character flags; the AI never sees the menu.

New files: `tfast_sc_goal_effects.txt`, `tfast_sc_automation_effects.txt`, `tfast_sc_goal_decisions.txt`, `tfast_sc_auto_decisions.txt`, `events/tfast_sc_goal_events.txt` (0910–0912), plus the hiding modifier and two raid-score terms. The rebuild and tell-the-tale decisions now share scripted effects with the automation.

Status: STATICALLY_VALIDATED; nothing clicked yet. The goals run on their own once the campaign starts — watch the debug log for "the Host has fed" / "the Host has made an example".

**The in-game handbook.** "TFAST Handbook: Open" (sort 9280) leads to eight chapters — Getting Started, The Hollow Dominion, Raids and Defense, The Great Wall, The Great Reckoning, The Long Dark and the Uprising, The Host's Goals and Hiding, Your Toolbox — with a chapter list, pages, and Back/Close, using the same flag-menu pattern as the cheat and automation menus. Each chapter's text states the prices and rules the scripts actually enforce; the Toolbox chapter also points at the AI Suite (cheat menu, right-click grants for any ruler including AI rulers) and TFAST History. Files: `tfast_sc_help_decisions.txt`, `tfast_sc_help_effects.txt`, one trigger. Status: STATICALLY_VALIDATED.

**Randomized flavor and an unpredictable Host (DeepSeek pipeline).** The raid warning, the dark omens (tfast_sc.0920) and the peacetime whispers (tfast_sc.0921) each draw one of eight lines from `tfast_sc_flavor_generated_l_english.yml` — generated by `python C:\Games\ck3-ai-automation\tools\tfast_flavor_deepseek.py` (DEEPSEEK_API_KEY from the environment or the tooling `.env`; built-in fallback pool offline). The Host also rolls a raid temper each season (bold +8 / measured / cautious −8 on `tfast_sc_raid_strength_value`) and, one year in five, its goal is pure caprice — no deterministic pattern survives. Status: STATICALLY_VALIDATED.

**First live session fixes (from the 1066 campaign of 12 Oct, 06:18–06:40).** The generated loc file originally shipped without the engine-required `_l_english.yml` suffix, so the pools were not loading (the raid warning fell back to its plain line; the log showed "Unrecognized loc key tfast_sc_flavor_*" for all 24). Renamed — flavor now loads. Also removed the scripted AI frequency from the six grant/naming interactions (AI Suite grants ×5, the chest-keeper naming): the engine logged "'ai_frequency' … but no 'ai_targets', won't be used" for each; they are player-only by `is_shown`, so the blocks were redundant noise. Both fixes are save-compatible; restart the game to apply.

**Korea (tfast_history).** Shipped the same day in the history module: six dated, once-per-world decisions recreating how Goryeo and Joseon actually ran — Gwageo (958), Land Survey (1391), Samsa (1392), Hall of Worthies (1420), Hunminjeongeum (1443), Goryeosa (1446). The vanilla game already gives Korea the meritocratic government; the pack is the institutions on top. See `tfast_history/README.md`.

**China (tfast_history).** Also the same day: the vanilla game already has the celestial government, the examination activities, the dynastic cycle, and the Great Wall and Grand Canal as great projects. The pack adds the missing record — Jiaozi paper money (1023), movable type (the 1040s), Zhu Xi's orthodoxy (1241), the Yongle Encyclopedia (1403), Zheng He's treasure voyages (1405), and the Bureau of Translators (1407). Validator: 7 script files, 195 loc keys, exit 0.

**England and Europe (tfast_history).** Also the same day: England gets six crown-gated institutions — the Great Survey (Domesday, 1086), the Exchequer (1130), trial by jury (Assize of Clarendon, 1166), the Model Parliament (1295), the Order of the Garter (1348, with the new Founder of the Order trait), and the Navy Royal (1413) — plus two events. Europe gets six heritage-gated acts: the monastic reform (Cluny, 910), the Truce of God (989), the communes (1100), the great fairs (1150), the Siete Partidas (1265), and the Everlasting League (1291). Cluniacs/Cistercians already exist as vanilla holy orders — patronized, not duplicated. Validator: 9 script files, 288 loc keys, exit 0.

**The Hollow Tide, in the Situations window.** The crisis is now a first-class 1.20 Situation (`common/situation/situations/tfast_sc_hollow_tide.txt` + `catalysts/tfast_sc_catalysts.txt`), Major group, generic `window_situation`, six chapters mirroring `tfast_sc_crisis_phase` exactly (peace → escalation → Reckoning → aftermath / dark → uprising → aftermath). Seven catalysts fired at the crisis state changes; icons generated by `tools/build_situation_icons.py`. The director starts it once, guarded by `tfast_sc_tide_started`, so existing saves get it on their next yearly tick — no new campaign needed. Status: STATICALLY_VALIDATED; the one thing to confirm next session is that "The Hollow Tide" shows up in the Situations window (if not, look for `start_situation` scope errors in the log).

**Adventurers can see the menus now (live-session fix).** The player was on a landless adventurer start, and every menu shell hid behind `is_landed = yes`, so the cheat menu, the automation menu and the handbook never appeared. The shells (and the six safe resource cheats in the AI Suite: gold/prestige/piety/renown/legitimacy/dread) are now player-gated only; landed-only tools keep their gates. Import: `is_landed` removed from `04_tfast_menu.txt` and the resource cheats in AI Suite, and from `tfast_sc_auto_decisions.txt` / `tfast_sc_help_decisions.txt`.

**TFAST Performance - Lean AI (new companion mod).** `mod/tfast_performance`: a partial `NAI` defines override (18 keys merged per key - the validator's own define-aware check confirms "additive defines file") that makes the AI recalculate less often, weigh fewer options and search fewer candidates. It deliberately conflicts with `tfast_smarter_ai` (opposite direction on the same keys; both can be loaded, last merge wins, but use one). Enabled in the playset; README documents the trade. Pair with `tfast_lategame` for the character-population side.

## Audit pass (same day)

A full cross-reference audit ran over both mods. Clean, no action needed: every event ID reference resolves; every scripted effect/trigger call resolves; every gfx and event-background path exists; character/house/dynasty/faith references resolve; game-rule settings and their loc keys exist; decisions carry all four loc keys; MAA/CB/religion/opinion/modifier loc is complete; every script and loc file has the UTF-8 BOM; the playset lists all nine mods with matching `.mod` files; `check_modset.py` reports no path/name/loc clashes; `test_art_refs.py` passes (trait icons, decisions, event overrides).

Fixed in this pass:

- `[building_slot|E]` in the AI Suite "Add Building Slots" description is not a 1.20 game concept; the engine logged `Data error in loc string 'tfast_cheat_building_slots_desc'` on every render. Now `[building|E] slot`.
- Raids, the wall branch, and gate breaches took gold with `add_gold = ... multiply = -1`; the engine logs `Trying to add add_gold with negative value` for every one. All four sites now use `remove_short_term_gold = var:tfast_sc_loot`, the vanilla effect for this (`common/activities/pulse_actions/pilgrimage_actions.txt`).
- `tfast_sc_released_opinion` and `tfast_sc_wall_slighted_opinion` had no loc keys. Added.
- `tfast_sc_wall_slighted_opinion` was defined but never used; now wired where the wall holds — the Overlord takes the slight (one `add_opinion` toward the wall sponsor in `tfast_sc_wall_defense_effect`).
- Three writes of never-read variables were removed: `tfast_sc_wave_spawn_guard` (crisis), `tfast_sc_raid_attacker` (raid director), `tfast_sc_reckoning_count` (aftermath).
- `validate_mod.py` ground truth missed `remove_short_term_gold` (a real effect with no `effect_localization` entry). Added to the tool, cache version bumped. Re-run: AI Suite exit 0; Shattered Crowns exit 1 with only the two false-positive classes above.

Expected engine warnings still to come — designed state with no consumer yet. Do NOT "fix" them by deleting; wire the consumer when the matching system grows:

| Variable | Set where | Consumer planned |
|---|---|---|
| `tfast_sc_assigned_stronghold`, `tfast_sc_bloc`, `tfast_sc_stronghold`, `tfast_sc_stronghold_index` | bootstrap (per child) | court events / return from banishment (spec 3.2) |
| `tfast_sc_first_reckoning_completed` | crisis end | later-campaign checks (spec 3.1 keeps it) |
| `tfast_sc_hostage_held` | crisis diplomacy | follow-ups to keeping a captive immortal |
| `tfast_sc_grievance_humiliation` | raid resolution | targeted-retaliation scoring (spec 3.7 chain) |

Resolved in the Long Dark pass: `tfast_sc_reckoning_attacker_won/lost`, `tfast_sc_reckoning_stalemate`, and `tfast_sc_rebellion_result` are now read at the Reckoning's end and the dark's beginning; `tfast_sc_wall_gate_county` is removed by the dismantle/destroy cleanup. The audit tool also flags `tfast_sc_influence`, `tfast_sc_rumor_county`, `tfast_sc_role_*`, `tfast_sc_stronghold_*`; all four are false positives — read via the parameterised `tfast_sc_clamp_variable_effect`, loc data functions, or wildcard names.

## What to do next

1. Quit the game fully (mod scripts load at startup). Start a new campaign with Shattered Crowns, TFAST AI Suite, Counting House, and Population Foundation enabled.
2. Decisions tab: click **TFAST Cheat Menu: Open**, walk all five pages, click one cheap cheat per page, then **Back** and **Close**. When closed, no cheat cards may remain; when open, only one page may be listed at a time.
3. Open Vaelos and each of the ten. Confirm house shields, vanilla crowns, and armor. Descendants should not wear those eleven crowns.
4. Hold a seeded county. Click the rumor, the survey, and opening a working for gold and for one other resource. Click the scout and the chest, including naming a keeper.
5. Review the three new paintings before painting the ten full-body plates.
6. Hire a mercenary company (all three tiers if the purse allows) and confirm the hosts muster at your capital. For the Long Dark, either lose a Reckoning front or use the console quick-look from the second-pass section.
7. After the session, run `python C:\Games\ck3-ai-automation\tools\check_runtime.py`. Expected clean: no `building_slot` loc errors, no negative-`add_gold` errors, no bootstrap scope errors. The backlog warnings listed in the audit section above may appear; they are documented.
8. Update `BUILD_STATUS.md` only after a click actually happens. A clean validator run stays STATICALLY_VALIDATED.
