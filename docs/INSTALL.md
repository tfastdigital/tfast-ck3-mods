# Installation

These instructions assume Windows, because that is where CK3 puts user files by
default. On Linux and macOS the same path exists under the Proton/Wine prefix or
`~/Documents/Paradox Interactive/Crusader Kings III/`.

---

## 1. Find your mod folder

```
C:\Users\<you>\Documents\Paradox Interactive\Crusader Kings III\mod\
```

If that folder does not exist, launch Crusader Kings III once and close it —
the game creates the whole `Paradox Interactive\Crusader Kings III\` tree on
first run.

A quick way to open it: press `Win+R`, paste
`%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod`, press Enter.

> If you use OneDrive, "Documents" may be redirected to
> `C:\Users\<you>\OneDrive\Documents\...`. The launcher reads whichever one the
> game actually uses, so check for a `mod` folder inside the path CK3 created.

---

## 2. Copy the mods

Download this repository (**Code → Download ZIP**, then extract), or clone it:

```bash
git clone https://github.com/<owner>/tfast-ck3-mods.git
```

Then copy **the entire contents of the `mods/` folder** into your CK3 `mod`
folder. That means both:

- the folders — `tfast_shattered_crowns\`, `tfast_africa\`, …
- the launcher files — `tfast_shattered_crowns.mod`, `tfast_africa.mod`, …

The result should look like this:

```
Documents/Paradox Interactive/Crusader Kings III/mod/
├── tfast_shattered_crowns/
│   └── descriptor.mod
├── tfast_shattered_crowns.mod
├── tfast_africa/
├── tfast_africa.mod
└── ...
```

> **Do not** create an extra folder level such as `mod/tfast-ck3-mods/mods/...`.
> The launcher scans the `mod` folder directly.

---

## 3. Why the `.mod` files work on your machine

Each launcher file contains a _relative_ path:

```txt
path="mod/tfast_shattered_crowns"
```

That path is resolved against your own
`Documents\Paradox Interactive\Crusader Kings III\` directory, so it is correct
on every machine, every drive, and every Windows user. Games that were shared
between friends often ship an absolute path like
`path="C:/Users/SomeoneElse/Documents/..."` — those only work on the machine that
wrote them. This repository does not do that.

If you moved the folders somewhere else, edit the `path=` line to match.

---

## 4. Enable them in the launcher

1. Start Crusader Kings III.
2. In the launcher, open **Playsets**.
3. Create a new playset (or use an existing one).
4. Click **Add mods**, tick the ones you want, and confirm.
5. Click **Play**.

Load order: everything here is designed to sit **after** the base game in any
order. See [COMPATIBILITY.md](COMPATIBILITY.md) for the one real conflict
(`tfast_performance` vs `tfast_smarter_ai`).

---

## 5. Check it loaded

In game, open the **Decisions** tab.

| Mod                                  | What you should see                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Shattered Crowns                     | Hollow Host, Great Wall, Last Watch and prophecy decisions; the **Hollow Tide** situation in the Situations window after the first yearly tick |
| AI Suite                             | **TFAST Cheat Menu: Open** under Major Decisions                                                                                               |
| Africa                               | Twelve African-history decisions                                                                                                               |
| History                              | Thirty-five historic-act decisions                                                                                                             |
| Fun Pack                             | Six court decisions                                                                                                                            |
| Late Game / Performance / Smarter AI | No decisions — they change defines only                                                                                                        |
| UI Readable                          | Immediately larger interface text                                                                                                              |

If a mod's decisions are missing, the most common cause is that the `.mod` file
did not get copied, or the `path=` inside it points at the wrong folder.

---

## Troubleshooting

### The mod does not appear in the launcher at all

- Confirm the `.mod` file is in the **same** directory as the mod folder, not
  inside it.
- Open the `.mod` file and check `path=` — it must point at the folder that
  actually exists.
- Confirm the file ends in `.mod`, not `.mod.txt` (Windows hides extensions by
  default: turn on _File name extensions_ in Explorer's View menu).

### The mod appears, but its content does not

- Check `Documents/Paradox Interactive/Crusader Kings III/logs/error.log`.
- If you see **hundreds of lines of raw `tfast_...` keys** in game, a
  localization file was saved without a UTF-8 BOM. Re-download the file — do not
  re-save it in an editor that strips the BOM.
- If you see "no such character" for Hollow titles, a title history entry did not
  resolve. Report it with the log lines.

### The game crashes on load

- Disable every mod, then enable them one at a time to find the culprit.
- Check whether you are also running a total conversion. Shattered Crowns
  rewrites characters and titles in the British Isles and will collide with mods
  that do the same. See [COMPATIBILITY.md](COMPATIBILITY.md).

### Text is too large / too small after enabling UI Readable

That mod only changes font sizes. Disable it, or edit
`gui/preload/fonts.gui` in the mod to taste. The four templates are
`Font_Size_Tiny`, `Font_Size_Small`, `Font_Size_Medium`, `Font_Size_Big`.

### Achievements

Modding disables achievements, as with any mod. There is no workaround and this
repository does not pretend otherwise.

---

## Uninstalling

Delete the mod's folder **and** its `.mod` file. Removing only one of the two
leaves an entry the launcher still tries to load.

Deleting a mod does not affect your save files, but a save created with a mod
enabled may complain about missing content. Keep the folders if you intend to
return to that campaign.
