# Third-party notices and asset provenance

The MIT license in `LICENSE` covers the **scripts, localization files and
documentation written for these mods**. It does not automatically cover every
image file. This page records what came from where so that a contributor — or a
downstream redistributor — can make an informed decision.

---

## Assets that may derive from third-party mod artwork

The following files were produced during development using artwork from
community mods as a **visual placeholder**. They have been renamed into the
`tfast_*` namespace, but the underlying picture may not be original work:

| File | Placeholder derived from |
|---|---|
| `mods/tfast_shattered_crowns/gfx/interface/icons/modifiers/tfast_sct_dragon_egg.dds` | Dragon-egg iconography from the **AGOT** mod |
| `mods/tfast_shattered_crowns/gfx/interface/illustrations/decisions/tfast_sct_dragon_throne_decision.dds` | Dragon decision artwork from the **AGOT** mod |

**If you intend to redistribute these files outside GitHub, or publish this
work on a mod platform, treat them as placeholders to be replaced.** Replacing
them with original or permissively licensed art requires no script changes —
only the `.dds` file at the same path, at the same dimensions.

If you are the author of the source artwork and want these files removed,
open an issue and they will be replaced or deleted promptly.

---

## Reference material (not shipped)

The **AGOT** and **LotR Realms in Exile — Wraiths** mods were read as reference
for Paradox scripting conventions, GUI patterns, and DDS encoding. **No files
from those mods are included in this repository other than the two placeholder
icons listed above.** Neither mod is redistributed here, and neither is
required to use these mods.

---

## Game data

Every mod in this repository reads and overrides data files belonging to
**Crusader Kings III**, © Paradox Interactive. Where a file under
`common/defines/` is overridden, it is a *partial* override of specific keys —
see each mod's README for exactly which keys and why.

Crusader Kings III is a trademark of Paradox Interactive AB. These mods are
unofficial, are not endorsed by Paradox Interactive, and are not affiliated with
Paradox Interactive in any way.

---

## Fonts

`tfast_ui_readable` does not ship any font files. It changes the *sizes* of the
font templates that reference the fonts already installed with the game.
