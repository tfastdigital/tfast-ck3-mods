# TFAST UI Readable Fonts

Larger, easier-to-read text on the **Crusader Kings III** interface. For
**1.20.x**.

## What it does

The whole CK3 interface inherits its text size from just four templates in
`gui/preload/fonts.gui`. This mod raises all four:

| Template | Vanilla | Now | Used in |
|---|---|---|---|
| `Font_Size_Tiny` | 13px | **15px** | 18 places |
| `Font_Size_Small` | 15px | **17px** | 155 places |
| `Font_Size_Medium` | 18px | **20px** | 542 places |
| `Font_Size_Big` | 23px | **26px** | 151 places |

That is roughly **+11%**, which is enough to help on a high-resolution or
high-DPI display without restructuring the layout.

## How it is done

Each template pairs a point size with a text-box height:

```
template Font_Size_Medium
{
    fontsize = 20
    size = { 0 29 }
}
```

Both move together, and the height-to-point ratio is kept inside the **1.38–1.53
band vanilla already uses**. Raising the point size while leaving the height
alone would clip text, so the two are always changed as a pair.

The file is otherwise byte-identical to vanilla — the only difference is eight
numbers.

## Read this: the honest trade-off

**Text can overflow in tightly-sized UI elements.** Buttons, list rows and some
tooltips are laid out to fit vanilla's 13–23px. At +11% most fit fine, but a few
long strings in a narrow control may wrap or clip.

If you hit that, the scale is not baked in — edit the `TARGETS` table at the top
of `tools/tune_ui_fonts.py` and re-run it:

```powershell
python c:\Games\ck3-ai-automation\tools\tune_ui_fonts.py --dry-run   # preview
python c:\Games\ck3-ai-automation\tools\tune_ui_fonts.py            # apply
```

Something around `fontsize` +1 and `size` +1 or +2 is the conservative option.

## Maintenance after a game patch

`fonts.gui` is shipped whole, so if a patch adds a **fifth** size template, this
copy would not have it and the game would fall back for that one. Check with:

```powershell
python c:\Games\ck3-ai-automation\tools\tune_ui_fonts.py --check
```

It reports any template vanilla has but this copy lacks, and any change that was
not one of the four intended ones.

To refresh after a patch:

```powershell
copy "C:\Games\ckIII\game\gui\preload\fonts.gui" `
     "C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III\mod\tfast_ui_readable\gui\preload\fonts.gui"
python c:\Games\ck3-ai-automation\tools\tune_ui_fonts.py
```

## Relationship to the game's own UI Scale setting

CK3 has a built-in UI scale option in the graphics settings. If that alone is
enough for you, use it and skip this mod — they stack, so using both can make
things comically large.

## Files

```
tfast_ui_readable.mod                                  launcher descriptor
tfast_ui_readable/descriptor.mod                       mod descriptor
tfast_ui_readable/gui/preload/fonts.gui                full vanilla copy, 4 sizes raised
```

## Uninstalling

Remove it from the playset. Because it only changes text metrics, disabling it
restores vanilla immediately — no save-format risk.
