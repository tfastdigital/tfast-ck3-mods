# The Story

Shattered Crowns is the only TFAST mod with a narrative spine. Everything else —
Africa, History, the Fun Pack — is content that can be enabled alongside it
without breaking the fiction. This page is the lore, and the note on how each
piece of lore is expressed in script.

**Reading order:** lore first, then "how it plays" at the end of each chapter.

---

## Chapter I — The Hollow

There was a people under the world before there were kingdoms on it.

They are called the **Hollow**. They are not undead, not demons, not a metaphor.
They are a civilisation that grew old in the dark, learned to stop dying, and
then found that immortality is mostly a very long wait.

Their realm is the **Hollow Dominion**: a court that has outlasted the
languages spoken above it. It is ruled from a seat that has never fallen, by a
ruler who has never been replaced, and its most important law is that the seat
cannot be taken — only endured.

> **In script:** every Hollow ruler is immortal, holds a permanent castle
> barony, and is **independent**. Their land can be conquered; their seat cannot
> be destroyed. If a seat is somehow lost, a quarterly effect reclaims it.

---

## Chapter II — Vaelos and Vaelith

**Vaelos**, the Overlord, and **Vaelith**, his twin sister and wife, are the two
fixed points of the Hollow.

They are not villainous in the sense of wanting to burn the world. They are
patient in a way only immortals can be: they measure loss in centuries and
grievances in bloodlines. Their ten children — **Vaelor, Morvath, Kaedryn,
Draven, Tharion, Seralyth, Nyxara, Velmora, Eryndra, Malethra** — each hold a
crown of their own, and each inherited a single facet of their parents'
obsession.

| Name     | Facet                              |
| -------- | ---------------------------------- |
| Vaelor   | Command                            |
| Morvath  | Endurance — bounded reinforcements |
| Kaedryn  | Frost                              |
| Draven   | Terror                             |
| Tharion  | The hunt                           |
| Seralyth | Blood                              |
| Nyxara   | Secrets                            |
| Velmora  | Treasure                           |
| Eryndra  | Omen                               |
| Malethra | Law                                |

> **In script:** Vaelos holds `h_hollow_dominion`, Vaelith holds
> `e_hollow_vaelith`, and the Ten hold kingdoms and counties of their own. All
> twelve are independent at every start date, so any of them can be fought,
> beaten, and stripped of land — but never destroyed.

---

## Chapter III — The Darkness

There is a thing older than the Hollow that is not one of them.

It is called **the Darkness** — the first of the Hollow, or the thing the Hollow
were made from, depending on which courtier you ask. It does not want to rule.
It wants to be _owed_.

In the early years of the common era it rose out of the Dominion, walked into
the world, and went looking for a throne to sit on. It found a dragonlord
instead.

> **In script:** `tfast_sc_darkness`, born in the early years, present in the
> Hollow family file, and tied to the Overlord's grief.

---

## Chapter IV — Aelfhere

**Aelfhere** was born in year 1, killed the Darkness in year 21, and died in
year 60. He is the reason the word _Targaryen_ is not spoken aloud in the Hollow
Dominion.

He was not a king. He had no army worth the name. He simply met the Darkness
with something it had never encountered — a bloodline that burned — and it did
not survive the meeting.

The Hollow never forgave this. They do not hate humanity, which they consider
beneath notice. They hate **one family**, and they hate it across generations,
which for them is the same thing as hating one person who keeps changing shape.

> **In script:** every Hollow character carries `−100` opinion of every
> Targaryen, permanently. The Hollow will pursue Targaryens specifically; a
> Hollow war declared on a Targaryen is not a war of conquest but of collection.

---

## Chapter V — The Scattered Blood

Aelfhere's line did not stay together. Over the centuries it dispersed into the
petty nobility of the British Isles, marrying into Welsh houses —
**Mathrafal**, **Caerloyw**, **Ternyllwg**, **Gwerthrynion** — and fragmenting
further with every generation.

By the eleventh century the Targaryens exist as dozens of households under a
dozen surnames. **Alfred** (760–840), **Edward** (800–880), **Edith** (808–882)
and **Edmund** (835–930) are the best-recorded of the medieval ancestors. Every
one of them carried the same two things without knowing why: **platinum-white
hair**, and a recurring dream of something enormous sleeping under the earth.

This is the central problem of the mod, and it is a problem of _administration_:
the Hollow hunt a family, and the family is not one house.

> **In script:** the scattered houses are consolidated. Members are moved into a
> single Targaryen house, renamed to English given names (or the old Targaryen
> names — Rhaenyra, Daenerys, Rhaenys, Visenya, Alysanne, Aemma, Helaena,
> Naerys, Rhaella, Alyssa), numbered II–X when a name repeats, and given the white
> hair gene directly. The dynasty head keeps the dynasty arms; every other
> member flies a separate house flag.

---

## Chapter VI — The Prophecy and the Chosen

The Hollow have a doctrine about the Targaryens, and it is not simply revenge.

They believe that when the last of Aelfhere's blood either submits or is
extinguished, the Dominion will be able to rise into the world permanently. So
the Hollow are looking for something: a Targaryen who is _enough_. Not the
strongest. The one the bloodline converges on.

That person is the **Chosen Emperor** — hidden, marked, and unaware, until the
day the mark wakes.

> **In script:** a hidden character flag marks the Chosen. Awakening grants three
> tiers of power, and succession is restricted to the dynasty alone. Only an
> awakened Chosen can inflict **True Death** on a Hollow. Everyone else can only
> seal one.

---

## Chapter VII — The Great Reckoning

Once a generation, the Hollow come up.

It is not a war of conquest and it is not a raid. It is an **audit**. The Host
counts what the world owes, takes payment in gold, land, and people, and then
goes back down — unless the world has grown weak enough that it does not have
to.

The world's answer is the **Great Wall**: five stages of construction, upkeep,
and repair, held by the **Last Watch**, a commander recruited for exactly this
purpose. The wall does not make the world safe. It makes the Reckoning
_survivable_.

> **In script:** the Reckoning is a real war with a custom casus belli, fought in
> three bounded waves against a Host that retreats on schedule. The wall gates
> the mod's scripted raids until it is breached, and its county modifiers slow
> real sieges. Native CK3 pathfinding cannot be walled off — the mod does not
> claim otherwise.

---

## Chapter VIII — The Long Dark

Sometimes the world loses.

If the Reckoning is lost on every front, the Hollow do not go home. The world
enters the **Long Dark**: yearly decay, a Hollow tithe, a fever year, blockaded
routes, and walls demolished stage by stage. The Hollow rule openly.

It is not an ending. `tfast_sc_dark_resistance` rises with every deed — a raid
held, a tithe refused, a seat taken, a wall standing one more year — and at the
thresholds the world rises, and at the higher threshold the dark breaks.

> **In script:** a game rule decides whether a lost Reckoning becomes the Long
> Dark. All of it is bounded and reversible on purpose: a hopeless state that
> cannot be escaped is a bug, not a challenge.

---

## How it plays, in one page

| You are                        | What the mod asks of you                                                                                    |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| A ruler near the British Isles | Survive the Reckoning. Build the wall. Do not lose on every front.                                          |
| A Targaryen                    | You are being hunted by something that does not die. Consolidate, or be picked off.                         |
| Anyone else, anywhere          | The Host reaches you too. The pale riders, the Hollow winter, and the world tick do not care where you are. |
| Playing the Hollow             | You cannot — they are AI rulers. Nothing in normal play lets you switch to them.                            |

### A note on that last line

The Hollow are AI-only. This is a design decision, not an oversight, and it is
stated plainly rather than papered over: Hollow rulers are created by script,
never placed in the player's dynasty, and there is no decision that hands you
control of one. Debug tools and external mods can do what debug tools do; the
[compatibility notes](COMPATIBILITY.md) say so openly.

---

## Deliberate anachronisms

The mod is not a history lesson and does not pretend to be:

- **Aelfhere is an Anglo-Saxon name** for a dragonlord. It is intended: the
  bloodline arrived long before the name "Targaryen" meant anything, and the
  name is a later imposition by the family itself.
- **The Hollow are older than the map.** Their titles are placed in the British
  Isles because that is where the story needs them, not because that is where
  they "should" be.
- **White hair is a gene, not a claim.** Every consolidated Targaryen gets the
  platinum hair through the DNA system, so it is heritable in game, the way the
  story says it should be.

If you want the history without the fiction, `tfast_history` is the mod for you.
If you want the fiction without the history, this one is.
