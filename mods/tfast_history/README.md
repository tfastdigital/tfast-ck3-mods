# TFAST History — Historic Acts & Institutions

Historical content for **Crusader Kings III 1.20.x**.

Companion to `tfast_ai_suite` (cheats & automation). Kept separate so you can
enable serious historical content without also enabling cheats.

## How to enable

1. This folder and `tfast_history.mod` are already in your CK3 mod directory.
2. Open the CK3 launcher → **Playsets** → add **TFAST History**.
3. Launch. The decisions appear in the **Decisions** tab under *Major Decisions*.

## What it adds

Thirty-five decisions, each modelling something that really happened in the
medieval world. They carry real costs, cooldowns and dates, so they read as
history rather than as cheat buttons.

| Decision | Real-world parallel | Cost | Cooldown |
|---|---|---|---|
| Proclaim a Merchant League | The Hanseatic League | 500 gold | 5 years |
| Found a Studium Generale | Bologna (1088), Paris, Oxford | 400 gold | 10 years |
| Convene a Church Council | Nicaea, Clermont (1095), Lateran | 500 piety | 5 years |
| Issue a Golden Bull | Golden Bull of 1356; Hungary 1222 | 500 prestige | 10 years |
| Forge a Dynastic Union | Kalmar Union (1397); Krewo (1385) | 1000 prestige | 10 years |
| Commission a Translation Movement | Toledo; Baghdad's House of Wisdom | 300 gold | 10 years |
| Seal a Great Charter | Magna Carta (1215) | 400 prestige | 10 years |
| Raise a Foreign Guard | Varangian Guard; Mamluks; Janissaries | 300 gold | 5 years |
| Commission a Great Cathedral | The Gothic cathedral boom | 600 gold | 10 years |
| Embrace Iconoclasm | Byzantine iconoclasm, 726–843 | free | 5 years |
| Hire a Condottiere | Italian condottieri; Catalan Company | 400 gold | 5 years |

Each grants a **25-year** standing modifier, and most also confer a permanent
reputation **trait**:

`Caesaropapist` · `Iconoclast` · `Condottiere` · `Patron of Letters` · `League Founder`

Two decisions fire a short narrative event as a payoff — *Charter of the League*
and *The Consecration*.

## Korea: Goryeo and Joseon institutions

Six further decisions recreate how the Korean courts actually ran, for rulers
of Korean (or Buyeo) heritage, each founded **once in the world** and gated
behind its real date:

| Decision | Real-world parallel | From | Cost |
|---|---|---|---|
| Institute the Civil Service Examinations | The Gwageo, 958 (Gwangjong of Goryeo) | 958 | 300 gold |
| Carry Out the Land Survey | The Gwajeonbeop land reform, 1391 | 1391 | 300 gold + 200 prestige |
| Establish the Three Censors | The Samsa — Saheonbu, Saganwon, Hongmungwan | 1392 | 300 prestige |
| Found the Hall of Worthies | The Jiphyeonjeon of Sejong, 1420 | 1420 | 400 gold |
| Promulgate the People's Script | Hunminjeongeum (Hangul), 1443 | 1443 | 500 prestige + 200 gold |
| Commission the History of Goryeo | The Goryeosa, 1446–1451 | 1446 | 400 gold |

Each grants a 25-year standing modifier; the examinations, the Hall and the
history also grant the **Patron of Letters** trait. The vanilla game already
gives Korea the meritocratic government — this pack is how they ran it. No
DLC is required: without the Korea content the culture and date gates simply
never come true, and nothing errors either way.

## China: inventions and institutions

The vanilla game already gives China the **celestial government**, the
examination system, the dynastic cycle, and the **Great Wall** and **Grand
Canal** as great projects. What it does not model is the empire's record of
invention and office — six more dated, once-per-world decisions for rulers of
Chinese heritage:

| Decision | Real-world parallel | From | Cost |
|---|---|---|---|
| Issue the First Paper Money | The Jiaozi, Chengdu — first state paper currency | 1023 | 400 gold |
| Commission Movable Type | Bi Sheng's ceramic type | 1040s | 300 gold |
| Enshrine the Commentaries | Zhu Xi entered the Confucian temples | 1241 | 400 prestige |
| Compile the Yongle Encyclopedia | 11,000 volumes, ordered 1403, finished 1408 | 1403 | 500 gold |
| Launch the Treasure Voyages | Zheng He's fleets | 1405 | 600 gold + 200 prestige |
| Found the Bureau of Translators | The Siyi Guan, after the first voyage | 1407 | 300 gold |

Movable type and the Encyclopedia also grant the **Patron of Letters** trait.

## England: the institutions of the crown

Gated on holding the crown of England (`k_england`) or the empire of
Britannia — the institutions belong to the realm, not the blood (the Norman
kings of England were French). Each founded once in the world:

| Decision | Real-world parallel | From | Cost |
|---|---|---|---|
| Commission the Great Survey | The Domesday Book | 1086 | 400 gold |
| Establish the Exchequer | The Pipe Rolls, the counting house | 1130 | 300 gold |
| Grant Trial by Jury | The Assize of Clarendon | 1166 | 300 prestige |
| Summon the Model Parliament | Knights and burgesses summoned | 1295 | 400 prestige |
| Found the Order of the Garter | Windsor, twenty-six knights | 1348 | 300 gold + 200 prestige |
| Build the Navy Royal | Henry V's standing fleet | 1413 | 500 gold |

The Garter also grants the new **Founder of the Order** trait. Two events
follow: *The Great Survey* and *The Order Is Founded*.

## Europe: movements and institutions

For rulers of European heritage. The Cluniac and Cistercian congregations
already exist in the game as holy orders; these acts patronize the movements
and build the institutions, generalized to your realm the way the base pack
does with the Hanseatic League:

| Decision | Real-world parallel | From | Cost |
|---|---|---|---|
| Back the Monastic Reform | Cluny and the reform congregations | 910 | 300 prestige |
| Proclaim the Truce of God | The Peace and Truce of God | 989 | 300 piety |
| Charter the Communes | The communal movement of the cities | 1100 | 400 gold |
| Charter the Great Fairs | The fairs of Champagne | 1150 | 300 gold |
| Proclaim the Siete Partidas | Alfonso the Wise's legal code | 1265 | 400 prestige |
| Swear an Everlasting League | The Swiss oath of 1291 | 1291 | 300 prestige |

## Why it is safe

* **`is_ai = no`** — only you can ever see or take these. The AI's economy,
  wars and balance are completely untouched.
* **`ai_check_interval = 0`** — the AI never even evaluates them.
* **Purely additive** — no vanilla file is overwritten or replaced. Disabling
  the mod restores the game exactly.
* **No new art.** Trait icons and decision illustrations are reused from
  vanilla, so there is nothing to go missing and no texture conflicts.
* Every effect, trigger, modifier key and illustration was verified against the
  installed 1.20.0.3 data before being used.

> **Achievements.** As with any gameplay mod, using these decisions disables
> achievements for that save.

## Files

```
tfast_history.mod                                          launcher descriptor
tfast_history/descriptor.mod                               mod descriptor
tfast_history/common/decisions/00_tfast_historic_decisions.txt
tfast_history/common/decisions/01_tfast_korea_decisions.txt
tfast_history/common/decisions/02_tfast_china_decisions.txt
tfast_history/common/decisions/03_tfast_england_decisions.txt
tfast_history/common/decisions/04_tfast_europe_decisions.txt
tfast_history/common/scripted_triggers/tfast_history_triggers.txt
tfast_history/common/traits/tfast_historic_traits.txt
tfast_history/common/modifiers/tfast_history_modifiers.txt
tfast_history/events/tfast_history_events.txt
tfast_history/localization/english/tfast_history_l_english.yml
```

Note that events live in the top-level `events/` folder — that is where CK3
loads them from, *not* `common/events/`.

## Validate after editing

```powershell
python c:\Games\ck3-ai-automation\tools\validate_mod.py "C:\Users\Engineer Brian\Documents\Paradox Interactive\Crusader Kings III\mod\tfast_history"
```

Checks the descriptor pairing, the UTF-8 BOM, decision groups, illustration
paths, every effect/trigger/modifier key, trait fields, trait references, event
localization and decision localization — all against the installed game.

## Uninstalling

Remove it from the playset, load the save, then save under a new name. Only
delete the folder once no save you care about was made with it active.
