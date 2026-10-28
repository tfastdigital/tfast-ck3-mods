# Changelog

All notable changes to the TFAST mods. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow
`MAJOR.MINOR.PATCH` per mod, independently.

**Status tags**: `STATICALLY_VALIDATED` means the scripts parse and every field
was checked against the 1.20 data files — it does **not** mean it was played.
See [docs/TESTING_STATUS.md](docs/TESTING_STATUS.md).

---

## 1.1.0 — cheats, situation scope fixes

### tfast_shattered_crowns — 1.1.0

#### Added

- **World-level yearly tick** (`tfast_sct_world_tick`) that reaches every
  playable ruler on the map, up to the eastern edge: resisting-the-Hollow
  modifier, dragon-at-court modifier, pale riders, Hollow winter.
- **Events `tfast_sct.0050` / `.0051`** — pale riders sighted; extra watches
  mustered.
- **Event `tfast_sct.0060`** — Hollow winter.
- **Decision `tfast_sct_raise_coalition`** — 300 gold, 100 prestige, duchy tier,
  10-year cooldown; grants +30 opinion from every independent non-Hollow ruler.
- **Hollow mutual war support** (`tfast_sc_hollow_war_effect`): when war is
  declared on one Hollow, every landed Hollow joins on the matching side, and
  those holding 150+ gold send 100 to the war leader.
- **Hollow vengeance wars** — the Overlord declares the Reckoning on a landed
  Targaryen on a 10-year cooldown once readiness reaches 50.
- **Dragon content** — egg gift (`tfast_sct.0001`), hatching (`tfast_sct.0002`),
  the `tfast_sct_claim_dragon_throne` decision, dragon modifiers.
- **The Hollow March** event (`tfast_sct.0040`) and the Hollow gathering warning
  (`tfast_sct.0010`).
- **Targaryen consolidation** — the scattered Welsh houses are folded into a
  single Targaryen house; members get numbered names (II–X), English and
  Targaryen given names, and a forced platinum-white hair gene. The dynasty head
  keeps the dynasty arms; other members carry a separate house flag.
- **Aelfhere**, the chosen Targaryen, who kills the Darkness in year 21 of his
  life; the Hollow therefore hold −100 opinion of every Targaryen forever.
- **Permanent Hollow seats** asserted at every start date, reclaimed quarterly if
  lost, with the county kept independent and the seat undeletable.
- **Fully built Hollow castles** — every castle barony held by a Hollow ruler is
  driven to the top building level in nine building chains.
- **Three generated art assets** — Hollow Tide situation icon, Elder culture
  heritage pillar, Hollow legacy track.

#### Changed

- All Hollow rulers are **independent** at start (previously vassals), so they
  can be fought and can lose land without losing their permanent seat.
- `tfast_sc_ensure_permanent_seats_effect` now runs at **every** start date, not
  only post-1066.
- The Darkness's birth and death dates were moved into the valid year range; the
  character previously did not exist, which is why no Hollow title resolved.

#### Fixed

- Unset `root` scope in `tfast_sc_give_crown_effect` that silently failed every
  title grant.
- `becomes_vassal_of` replaced with `change_liege`.
- Invalid negative years in Hollow character history.
- Invalid `liege` values in Hollow title history.
- Duplicate `dynn_Mathrafal` localization key moved to `replace/`.
- Portrait gene spam (unknown genes removed, required `complexion` gene added).
- `hostile_scheme_resistance_mult` → `enemy_hostile_scheme_success_chance_add`.
- ~1,500 trait-description log errors (`ROOT.GetHerHis` → `CHARACTER.GetHerHis`).
- Great Wall planning scope mismatch in `on_plan_build`.
- `(no character)` errors from vanilla building `on_complete` blocks, which read
  `scope:character` — unset whenever script places a building. The holder is now
  saved as `scope:character` before every `add_building` / `generate_building`.
- Every `trigger_situation_catalyst` call (12 sites) now runs inside
  `situation:tfast_sc_hollow_tide = { ... }` guarded by
  `exists = situation:tfast_sc_hollow_tide`. Called from character scope the
  engine only logged `Wrong scope for effect: character, expected situation`
  and the Hollow Tide never changed phase.
- `has_dynasty_perk` / `dynasty_prestige` wrapped in `dynasty ?= { ... }` — they
  are dynasty triggers and error out in character scope.
- 15 files missing the UTF-8 BOM.

---

### tfast_ai_suite — 1.2.0

#### Added

- Exportable flag-menu framework: open, page, back, close — 23 cheats across five
  pages (Resources, Domain, Military, Character, Realm).
- Landless-adventurer path for the full usable kit.
- **Cheat: Create an Army** — spawns a 4,000-levy host at your capital with six
  regiments of men-at-arms, tops up every existing regiment, and refills levies.
- **Cheat: Upgrade Everything You Rule** — walks every county you hold and
  drives each holding through its full building chain (`castle_01`→`04`,
  `city_01`→`04`, `temple_01`→`04`, `temple_citadel_01`→`04`), then fills any
  free building slots.
- Matching targeted interactions for **Create an Army** and **Upgrade
  Everything You Rule**, so both can be aimed at a vassal.

#### Changed

- All cheats gated behind a single menu flag so the Decisions tab stays clean
  while the menu is closed.
- **Max Men-at-Arms is now one step.** It fills every empty regiment slot from a
  fixed type list and then pushes each regiment to its maximum size, instead of
  requiring repeated clicks. It is also used by Golden Age.

#### Fixed

- `(no character)` errors from vanilla building `on_complete` blocks that read
  `scope:character`; the holder is now saved before every building is placed.
- `refill_maa_regiment` (not a real effect) replaced with
  `change_maa_troops_count` and the `maa_max_troops_count −
maa_current_troops_count` script value.

---

## 1.0.0 — initial public release

### tfast_shattered_crowns — 1.0.0

The Hollow Dominion, the Great Wall, the Chosen Emperor, the Great Reckoning, the
Long Dark, mercenaries, Hollow goals, hiding and hunting, the automation menu,
the in-game handbook, the Hollow Tide situation, six Hollow men-at-arms, and a
generated flavor pool.

### tfast_africa — 1.0.0

12 decisions, 6 traits, 12 modifiers drawn from documented African history.

### tfast_history — 1.0.0

35 decisions modelling real medieval institutions, with real costs and cooldowns.

### tfast_funpack — 1.0.0

6 court decisions — tournament, menagerie, artisan, blood feud, hoard, year of
pleasure — each with a genuine downside.

### tfast_lategame — 1.0.0

Partial override of four population-growth defines. Explicitly not a lag fix.

### tfast_performance — 1.0.0

16 AI keys retuned to reduce recalculation. Deliberately trades intelligence for
speed; conflicts with `tfast_smarter_ai` by design.

### tfast_smarter_ai — 1.0.0

16 AI keys retuned for faster reactions and wider search. Makes the game harder.

### tfast_ui_readable — 1.0.0

All four CK3 font templates raised ~11%.

### tfast_template — 1.0.0

Empty starting scaffold for a new TFAST-style mod.
