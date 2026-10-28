# TFAST Mods for Crusader Kings III

**Ten open-source Crusader Kings III mods — a survival epic, a fleshed-out Africa, thirty-five historical institutions, and a set of honest performance tools.**

[![Game Version](https://img.shields.io/badge/CK3-1.20.x-502C97?style=flat-square)](docs/MOD_VERSIONS.md)
[![License](https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square)](LICENSE)
[![Validate](https://github.com/tfastdigital/tfast-ck3-mods/actions/workflows/validate.yml/badge.svg)](https://github.com/tfastdigital/tfast-ck3-mods/actions/workflows/validate.yml)
[![Status](https://img.shields.io/badge/status-in%20development-orange?style=flat-square)](docs/TESTING_STATUS.md)
[![Contributions](https://img.shields.io/badge/contributions-welcome-blue?style=flat-square)](CONTRIBUTING.md)

**[Download the latest release](https://github.com/tfastdigital/tfast-ck3-mods/releases/latest)** — each mod is packaged as its own zip.

---

## Supported game version

|                        |                                                                               |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Crusader Kings III** | `1.20.x`                                                                      |
| **Built against**      | `1.20.0.3` ("Crozier")                                                        |
| **Descriptor field**   | `supported_version="1.20.*"` in every mod                                     |
| **DLC required**       | None. All mods run on the base game.                                          |
| **Load order**         | Anywhere after the base game. See [load order](#load-order--known-conflicts). |

When Paradox ships a new major patch, `supported_version` is bumped **only after** the scripts have been re-checked against the new data files. A stale version number is better than a false promise.

---

## The mods

| Mod                                                                    | Version | What it is                                                                                                                                        |
| ---------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[TFAST Shattered Crowns](mods/tfast_shattered_crowns)**              | `1.0.0` | The flagship. An immortal Hollow Dominion beneath the world, the Great Wall, the Chosen Emperor, the Great Reckoning, and the Targaryen prophecy. |
| **[TFAST Africa — Historical Depth](mods/tfast_africa)**               | `1.0.0` | 12 decisions, 6 traits, 12 modifiers built from documented African history — the content vanilla never shipped.                                   |
| **[TFAST History — Historic Acts & Institutions](mods/tfast_history)** | `1.0.0` | 35 decisions modelled on real medieval institutions: the Hanseatic League, the Golden Bull, Magna Carta, the Kalmar Union.                        |
| **[TFAST Fun Pack — Court Life & Character](mods/tfast_funpack)**      | `1.0.0` | 6 court decisions with real costs and lasting marks. Nothing is pure upside.                                                                      |
| **[TFAST AI Suite — Cheats & Automation](mods/tfast_ai_suite)**        | `1.1.0` | A flag-gated cheat menu (5 pages, 23 cheats) plus realm automation. Single-player convenience.                                                    |
| **[TFAST Late Game — Stability](mods/tfast_lategame)**                 | `1.0.0` | Slows character-population growth so long campaigns stay playable. Honest about what it cannot fix.                                               |
| **[TFAST Performance — Lean AI](mods/tfast_performance)**              | `1.0.0` | Makes the AI recalculate less often. A deliberate trade: faster, dumber.                                                                          |
| **[TFAST Smarter AI](mods/tfast_smarter_ai)**                          | `1.0.0` | The opposite trade: 16 AI keys retuned for faster reactions and better choices. Harder game.                                                      |
| **[TFAST UI Readable Fonts](mods/tfast_ui_readable)**                  | `1.0.0` | Raises all four CK3 font templates by ~11% for high-DPI displays.                                                                                 |
| **[TFAST Template Mod](mods/tfast_template)**                          | `1.0.0` | A clean, empty starting point for your own TFAST-style mod.                                                                                       |

Full version table, tags, and per-mod file counts: **[docs/MOD_VERSIONS.md](docs/MOD_VERSIONS.md)**.

---

## The story

The mods are independent, but **Shattered Crowns** carries a story, and everything else is built to sit beside it without contradicting it.

> The Hollow Dominion has always been down there.
>
> It was old when the first kingdoms were young. Its Overlord, **Vaelos**, and his twin sister-wife **Vaelith**, ruled a court of ten immortal children and a thing older than all of them — **the Darkness**, the first of the Hollow. For ages it slept, and the world above forgot it was ever owed anything.
>
> Then the Darkness woke and went looking for a throne. It found a dragonlord instead. **Aelfhere of the Targaryens** — a bloodline scattered into a hundred minor Welsh houses, all of them carrying the same white hair and the same wrong memory — killed it.
>
> That is the whole of the grievance. The Hollow do not hate the world. They hate **one family**, with a hatred that outlives every individual member of it. And the Targaryens, who have never been one house in the eyes of the game, must become one, or be hunted down one branch at a time.

The full narrative, the cast, and the timeline: **[docs/STORY.md](docs/STORY.md)**.

---

## Installation

The `mods/` folder in this repository mirrors a CK3 mod directory exactly, so installation is a copy.

**Option A — download only what you want.** Grab a mod's zip from the [latest release](https://github.com/tfastdigital/tfast-ck3-mods/releases/latest), then unzip it into the `mod/` folder below. Each zip contains the mod folder **and** its `.mod` launcher file.

**Option B — clone everything.**

```
git clone https://github.com/tfastdigital/tfast-ck3-mods.git
```

1. Download a release, or clone this repository.
2. Copy **everything inside `mods/`** (the folders _and_ the `.mod` files) into:

   ```
   Documents/Paradox Interactive/Crusader Kings III/mod/
   ```

   On Windows that is usually `C:\Users\<you>\Documents\Paradox Interactive\Crusader Kings III\mod\`.

3. Launch CK3 → **Playsets** → add the mods you want → **Play**.

The `.mod` files in this repository use **relative paths** (`path="mod/tfast_shattered_crowns"`), so they work on any machine and any drive. If the launcher still cannot see a mod, open the `.mod` file and confirm the `path=` line points at the folder you actually copied.

Step-by-step with screenshots-free troubleshooting: **[docs/INSTALL.md](docs/INSTALL.md)**.

### Updating

Copy over the old folders. Your saves are unaffected; new scripted content is picked up on load. If a mod changes a save-visible key, the changelog says so. **Releases are tagged** (`v1.0.0`, `v1.0.1`, …) so you can see exactly which snapshot you are running.

---

## Load order & known conflicts

Most of these mods only **add** content and can be enabled in any combination.

| Pair                                                   | Verdict                                                                                                          |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Everything except the two AI mods                      | Compatible. No shared IDs.                                                                                       |
| `tfast_performance` + `tfast_smarter_ai`               | **Conflict by design.** They tune the same `common/defines/ai/` keys in opposite directions. Enable exactly one. |
| `tfast_shattered_crowns` + large total-conversion mods | Expect title-history and character-ID collisions. Test in a new save.                                            |

Details and the reasoning behind each call: **[docs/COMPATIBILITY.md](docs/COMPATIBILITY.md)**.

---

## Development status

Read this before you install, and read it again before you file a bug.

| Status                 | Meaning                                                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `STATICALLY_VALIDATED` | Every effect, trigger, scope, modifier key and database field was checked against the installed 1.20 data files. No validator or load errors. **Not played.** |
| `RUNTIME_TESTED`       | Observed working in a launched game.                                                                                                                          |
| `VERIFIED`             | Played through to the intended outcome, on a clean save, more than once.                                                                                      |

**Almost everything in this repository is `STATICALLY_VALIDATED`, not `VERIFIED`.** The mods load and parse cleanly; the recent features have not all been played through. That is the honest state, and the per-system table says so line by line:

- **[docs/TESTING_STATUS.md](docs/TESTING_STATUS.md)** — per-system validation state
- **[docs/ROADMAP.md](docs/ROADMAP.md)** — what is next, and what was deliberately rejected
- **[CHANGELOG.md](CHANGELOG.md)** — what changed and when

The single most useful thing a contributor can do right now is **play a campaign and report what breaks**. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Contributing

Contributions are why this is public. Bug reports, balance arguments, localization fixes, art, and whole new systems are all welcome.

- Read **[CONTRIBUTING.md](CONTRIBUTING.md)** — it covers the CK3-specific rules that will otherwise cost you an evening (UTF-8 BOM, scope discipline, `root` in `on_action`, negative years, file naming).
- Open an issue using the templates in `.github/ISSUE_TEMPLATE/`.
- Run `python tools/validate.py` before you open a pull request; CI runs the same check.

You do not need to be a CK3 scripting expert to help. Copy-editing the localization files, or playing a campaign and writing down what happened, is genuinely useful.

---

## License

- **Scripts, localization, and documentation:** [MIT](LICENSE) — use them, fork them, ship your own mod built on them.
- **Art assets:** a small number were copied from third-party mods for placeholder use. See **[NOTICE.md](NOTICE.md)**. Those specific files are **not** covered by the MIT license and should be replaced with original work before redistribution.

Crusader Kings III is a trademark of Paradox Interactive. These mods are unofficial and are not endorsed by or affiliated with Paradox Interactive.

---

## Credits

- **TFast Digital** — design, scripting, documentation.
- **Paradox Interactive** — Crusader Kings III, and the data files that make static validation possible.
- **AGOT** and **LotR Realms in Exile** mod teams — reference material and a handful of placeholder icons, credited in [NOTICE.md](NOTICE.md).
