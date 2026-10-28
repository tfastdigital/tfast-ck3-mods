# Shattered Crowns - The Story, and How to Live It

## The lore, briefly

Long before the first crown was forged, there was a Dominion that ruled by
pact: a single Overlord who could not die, ten children who could not be
killed, and a promise - the world, in time. The world took too long to notice.
The Dominion was shattered, its children scattered, its Overlord sealed in a
stronghold that became a reef, then an island, then a rumor.

But the Hollow keep their promises. Silence is not death. The Hollow
Immortals have spent a thousand years in the hollow places doing the one thing
mortals cannot: waiting.

Now the Overlord walks again. The Ten hold island refuges. The Host is moving
in the space between wars, and it has begun to count the world's walls.

## The loop, in plain words

1. **False peace.** The Host raids. You get a real warning event, you choose
   how to defend, and real things are lost or saved: gold, county control,
   prisoners, the fields themselves. The raids are the Hollow's only peacetime
   diplomacy, and it is not diplomacy.
2. **The warning.** After enough raids (or a stronghold lost), the world is
   foretold: two years of open warnings before the Reckoning.
3. **The Great Reckoning.** Real war. Three waves at most, keyed to the
   Host's readiness. You can win, hold, or lose ground - and the tide always
   ends, with ground or without it.
4. **The aftermath.** The Host retreats; refugees flood the roads; the
   prophecy window opens for ten years.
5. **The mythologizing.** If a child of your dynasty is born in that window,
   something hidden starts watching them. You will not be told what.

## How to build a Great Wall

Decisions from your capital:

1. **Plan the Great Wall** (free) - designates your capital plus up to three
   of your own counties in the same duchy; the capital is the gate.
2. **Raise Watchtowers** (gold) - the frontier gets eyes.
3. **Raise the Rampart** (gold) - fort level and holding advantage.
4. **Close the Gates** (gold) - while the gate stands unbreached, the Hollow's
   scripted raids cannot take your stores; they break against the stone and
   damage the wall instead.
5. **Set the Wards** (piety) - the Hollow's hands cannot cross unbroken.

Then: **Fund the Great Wall** keeps it maintained; **Repair the Great Wall**
restores integrity and rehangs a breached gate; **Recruit a Watch Commander**
puts a named defender in the towers.

Integrity falls with every assault and every unfunded year. At zero, the gate
is breached, the world is notified, and the raids come through until you mend
it. A wall is a promise too.

## The Awakening

You will never see it coming. There is no trait, no title, no omen your
council can read. In the decade after the first Reckoning, one child of your
dynasty may carry a private something that the chronicles do not record.

If they live to grow up - or if danger comes for them first - the Awakening
happens (`THE AWAKENING`). Then, and only then:

* **Deepen the Power** (decision, three thresholds) - the only power in the
  world that can permanently end a Hollow immortal, made deeper.
* **Invoke True Death** (decision, war-time only) - a strike at an immortal.
  It can fail, and failing costs. Succeed, and one of the Ten is struck out
  of a ledger where names are supposed to be permanent.
* If the bloodline dies out, the prophecy ends, explicitly and finally. No
  cousins are ever chosen after the line is gone.

## What the Hollow are - and are not

* The Overlord cannot be killed. Ever. He can be sealed (fifteen years of
  silence, an Eternal Regency among the Ten) and he will come back counting.
* The Ten can be destroyed by the Awakened. Anyone else who kills one only
  *banishes* them - and banished things walk again, years later, wearing the
  years like a coat.
* The Hollow do not negotiate. The only door ever opened is the one where you
  are holding one of them in your dungeons (`tfast_sc.0600`), and even then
  every answer has teeth.
* The Ten are not loyal to each other. Watch: an open rebellion (`The Hollow
  Court Is Torn`) is rare but real, and it means one of them has decided the
  Overlord's throne has been empty long enough.

## The events, in order (event -> event)

| Event | Fires when | Leads to |
|---|---|---|
| `tfast_sc.0100` | The raid director picks you | `tfast_sc.0101` (resolution: toasts, gold, control, prisoners) |
| `tfast_sc.0200` | Escalation threshold crossed | `tfast_sc.0201` after two years |
| `tfast_sc.0201` | The Reckoning begins | wave spawns; `tfast_sc.0202` or `tfast_sc.0203` later |
| `tfast_sc.0202` | Every Reckoning end | refugee/rebuild chain (`tfast_sc_rebuild_county`) |
| `tfast_sc.0203` | Aftermath cooldown expires | the raid director resumes |
| `tfast_sc.0301/0302/0303` | Wall assaults, breaches, unpaid watch | wall upkeep decisions |
| `tfast_sc.0402` | A hidden Chosen is marked | `tfast_sc.0403` at awakening, `tfast_sc.0404` if the line dies |
| `tfast_sc.0403` | Awakening | `tfast_sc_chosen_deepen_power` |
| `tfast_sc.0500/0501/0502/0503` | True Death attempts and seals | the world is told; memory is recorded |
| `tfast_sc.0600` | You hold a Hollow immortal | release / execution (banishment) / sealing |
| `tfast_sc.0700` | You tell the tale | your saved memories become renown |
| `tfast_sc.0810/0811` | Hollow civil war / a banished one returns | the world watches |
