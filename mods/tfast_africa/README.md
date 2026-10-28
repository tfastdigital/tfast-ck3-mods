# TFAST Africa — Historical Depth

Twelve decisions, six traits and twelve modifiers drawn from documented African
history. For **Crusader Kings III 1.20.x**.

---

## Why this mod exists

I surveyed what CK3 1.20 ships for Africa:

| | Count |
|---|---|
| African faiths | **16+** (`akom_pagan`, `bimoism`, `dab_qhuas`, `hantuism`, `kushitism_pagan`, `ngaiism_pagan`, `satsana_phi`, `waaqism_pagan`, `west_african_*` ×5, `zun_pagan`, …) |
| African cultures | **16** (akan, daju, ewe, hausa, igbo, kanuri, malinke, nubian, sao, serer, somali, songhai, soninke, swahili, wolof, yoruba) |
| African holy sites | **7** (aksum, kukiya, wadan, bono, ife, nikki, mogadishu) |
| **African content files** | **~1 — and it is about the Maghreb** |

The only Africa-named decision file in the game is
`00_major_decisions_iberia_north_africa.txt`, which covers Muslim Iberia and
North Africa — the Mediterranean world, not Africa south of the Sahara.

Compare the investment elsewhere: the East Asia update shipped **789 noble-family
titles** in `04_china_noble_families.txt` alone, plus dedicated title files for
China, Japan, Korea, SE Asia and the Philippines. Africa has **no dedicated
script file of any kind**.

So the religions, cultures and holy sites are all there, waiting — and almost
nothing in the game uses them. This mod adds depth in the form that is safest to
add: player-only decisions, traits and modifiers.

## What it adds

Every decision is a real institution, practice or event.

| Decision | Historical basis | Region |
|---|---|---|
| Open the Gold Road | Trans-Saharan gold-for-salt trade; the Wangara gold fields | West |
| Conduct the Silent Trade | Documented trade without shared language | Any African |
| Undertake the Great Pilgrimage | Mansa Musa's hajj of 1324, which depressed Cairo's gold price | Muslim African |
| Endow a House of Learning | Timbuktu's Sankore mosque and its manuscript libraries | West |
| Proclaim the Oral Charter | The Kurukan Fuga (c. 1236), the spoken Manden constitution | West, kingdom+ |
| Raise the Dry-Stone Walls | Great Zimbabwe's mortarless granite walls | Any African |
| Carve the Rock Churches | Lalibela's eleven monolithic churches (c. 1200) | East |
| Assert the Solomonic Line | The Kebra Nagast claim of descent from Solomon and Sheba | East, kingdom+ |
| Mint Cowrie Currency | Cowrie shells as small coin across West Africa | West |
| Institute the Age-Grade System | The Gadaa generational cycle of the Oromo | East |
| Cast the Bronze Heads | Ife and Benin lost-wax brass and bronze casting | West |
| Open the Ocean Trade | Kilwa and the Swahili city-states' monsoon trade | East, coastal |

**Traits** (permanent): `Gold Merchant` · `Patron of Scholars` · `Charter Keeper` ·
`Stone Builder` · `Elder of the Grades` · `Ocean Merchant`

Each decision also grants a **25–30 year** modifier.

## How it is gated

Four scripted triggers do the work, using the region-test pattern vanilla itself
uses (`capital_province = { geographical_region = ... }`, as in
`00_artifact_triggers.txt`):

| Trigger | Regions |
|---|---|
| `tfast_africa_is_african_trigger` | `world_africa` |
| `tfast_africa_is_west_african_trigger` | `world_africa_west`, `custom_sahel_proper`, `custom_sub_saharan_africa_immediate` |
| `tfast_africa_is_east_african_trigger` | `world_africa_east`, `ghw_region_horn_of_africa`, `ghw_region_ethiopia`, `dlc_tgp_swahili_coast_region` |
| `tfast_africa_is_saharan_trigger` | `world_africa_sahara`, `world_africa_north`, `ghw_region_north_africa` |

All 11 region names were verified against the 703 regions in
`map_data/geographical_regions`, and the validator now checks this automatically
— a typo here fails **silently**, so it is worth catching.

## Why it is safe

* **`is_ai = no`** — only you can see or take these. The AI's economy, wars and
  balance are untouched.
* **`ai_check_interval = 0`** — the AI never evaluates them.
* **Purely additive** — no vanilla file is overwritten. Disabling the mod
  restores the game exactly. Notably it does **not** touch the map, titles or
  history, so there is no save-format risk.
* **No new art.** All six trait icons and all twelve illustrations are reused
  from vanilla.
* Every effect, trigger, modifier key, trait icon, modifier icon, illustration
  and geographical region was verified against the installed 1.20.0.3 data.

## What this mod deliberately does not do

* **It does not add de jure titles, cultures or map changes.** Those are the
  changes that break saves and conflict with other map mods. Adding content
  *through* the existing religions and cultures is far safer and still gives
  Africa the depth it was missing.
* **It does not invent history.** Every entry names a documented practice or
  event, described generically enough to fit any ruler of the relevant region
  rather than asserting one dynasty's claim over another's.

> **Achievements.** As with any gameplay mod, using these decisions disables
> achievements for that save.

## Files

```
tfast_africa.mod                                          launcher descriptor
tfast_africa/descriptor.mod                               mod descriptor
tfast_africa/common/scripted_triggers/tfast_africa_triggers.txt
tfast_africa/common/decisions/00_tfast_africa_decisions.txt
tfast_africa/common/traits/tfast_africa_traits.txt
tfast_africa/common/modifiers/tfast_africa_modifiers.txt
tfast_africa/localization/english/tfast_africa_l_english.yml
```

## Validate after editing

```powershell
python c:\Games\ck3-ai-automation\tools\validate_mod.py "C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III\mod\tfast_africa"
```

## Uninstalling

Remove it from the playset, load the save, then save under a new name. Traits
will persist on characters in that save.
