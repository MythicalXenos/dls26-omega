#!/usr/bin/env python3
"""ckpt-154: masterplan + operational rules + BRIEFING - the breakthrough ladder and the
look-ahead trick."""
import io
def patch(P, subs):
    t=io.open(P,encoding='utf-8').read()
    for a,b in subs:
        assert a in t and t.count(a)==1, 'ANCHOR PROBLEM in '+P+': '+a[:70]
        t=t.replace(a,b,1)
    io.open(P,'w',encoding='utf-8').write(t)
    print('patched', P)

patch('/home/user/dls26-omega/docs/strategy_masterplan.md', [
 ('**KB basis:** ckpt-153 — 1,856 claims / 392 evidence records',
  '**KB basis:** ckpt-154 — 1,872 claims / 393 evidence records'),
 ('''**EFFECT SIZES:** Legendary boosts **3 random stats by +3** · Rare **2 by +2** · Common **1 by +1**. This reconciles the 12-point and 9-point figures once the Strength/Control double-weighting is applied.''',
  '''**EFFECT SIZES:** Legendary boosts **3 random stats by +3** · Rare **2 by +2** · Common **1 by +1**. This reconciles the 12-point and 9-point figures once the Strength/Control double-weighting is applied.

**THE BREAKTHROUGH LADDER — now known** [EV-491, C2]: **Common 5% · Rare 10% · Legendary 20%**, corroborated by three sources spanning DLS20 to DLS24 (*"with a 5 percent Breakout Rating… 10 percent… 20 percent"*; *"6x9 = 54 single point upgrades, with 20% breakthrough chance"*; *"Legendary coaches… 10% more chance of breakthrough"*). **The Legendary 20% is the new figure** — the corpus previously had only the 5% and 10% baseline. So the tier that costs the most is also the tier most likely to hand you a free development point.

**THE COACH CATEGORY POOLS** [EV-491, C2] — the coaching system mapped onto the official stat model:

| Coach category | Draws from |
|---|---|
| **Fitness** | SPE · ACC · STA · STR |
| **Technical** | CON · PAS · SHO · TAC |
| **Goalkeeping** | GKR · GKH |

This is why chaining by category works: the category is the only control you have over *which* stat moves.

> **🎯 THE LOOK-AHEAD TRICK — the most valuable mechanic in the game** [EV-491, C2]. *"You want to always keep at least 1 Legendary Special coach because it will allow you to look at the next 4 upgradable stats (you can cancel it and use any other coach without losing the legendary special coach). Always use a common coach if at least 1 of the stats isn't what you want."* Confirmed independently: *"You never lose the coach no matter what, whether you close the app or simply click on the 'x' to cancel the coaching."*
>
> **So the most expensive item in DLS doubles as a free information tool.** Open a Legendary Special coach, read the next four stats, cancel, and spend a Common coach if the preview is bad. The saving is quantified at **~70 gems × 6–7 = ~420 gems per maxed special player**. **Keep at least one Legendary Special coach in reserve at all times for this purpose.**'''),
 ('''**THE COACH-FARMING THRESHOLD IS 192 COINS** — two independent derivations of the same number.''',
  '''**THE COACH GEM PRICE LADDER** [EV-491, C2]: Common **17 gems** · Rare **52 (maxed) / 67 (unmaxed)** · Legendary **157 (maxed) / 202 (unmaxed)**. So the Training facility saves **15 gems per Rare and 45 per Legendary** — and a **third** source confirms it *"will pay itself after 20 or so legendary coaches."*

**THE COMMERCIAL-vs-COACHES BREAKEVEN** [EV-491, C3]: a Common coach bought efficiently costs ~200 gems for 54 upgrade points = 10,800, which at a 10% Commercial bonus needs **~108,000 coins** to match. **So max Commercial only if you will grind past ~108,000 coins; otherwise keep the gems for facilities.** That is the cleanest decision rule the corpus has for the Commercial question.

**RARE GOALKEEPERS YIELD ONLY ONE COMMON COACH** [EV-491, C3] — *"Don't buy rare goalies as they also only get 1 common coach after release, same as any common goalie."* An explicit exception to the release mapping and a direct instruction for coach farming.

**THE COACH-FARMING THRESHOLD IS 192 COINS** — two independent derivations of the same number.'''),
])

patch('/home/user/dls26-omega/docs/operational_rules.md', [
 ('> Basis: ckpt-153 — 1,856 claims / 392 evidence records. Companion to `docs/strategy_masterplan.md`.',
  '> Basis: ckpt-154 — 1,872 claims / 393 evidence records. Companion to `docs/strategy_masterplan.md`.'),
 ('''- **Effects:** Legendary 3 stats ×+3 · Rare 2 ×+2 · Common 1 ×+1.''',
  '''- **Effects:** Legendary 3 stats ×+3 · Rare 2 ×+2 · Common 1 ×+1.
- **BREAKTHROUGH LADDER:** Common **5%** · Rare **10%** · Legendary **20%** — three sources, DLS20–DLS24.
- **CATEGORY POOLS:** Fitness = SPE/ACC/STA/STR · Technical = CON/PAS/SHO/TAC · Goalkeeping = GKR/GKH.
- **🎯 LOOK-AHEAD TRICK:** a Legendary Special coach previews the **next four stats** and can be **cancelled without being consumed**. Keep one in reserve at all times; worth **~420 gems per special player**.'''),
 ('''- **Scouts:** discounts 2–4% / 3–5% / 4–8%; two candidates each, so P(≥1 legendary) is 3.96% Common vs 27.75% Legendary — **Legendary scouts are good value.**''',
  '''- **Scouts:** discounts 2–4% / 3–5% / 4–8%; two candidates each, so P(≥1 legendary) is 3.96% Common vs 27.75% Legendary — **Legendary scouts are good value.**
- **Coach prices:** Common 17g · Rare 52g (maxed) / 67g · Legendary 157g (maxed) / 202g — so Training saves 15g per Rare and 45g per Legendary.
- **Commercial breakeven:** max it only if you will grind past **~108,000 coins**.
- **Rare goalkeepers yield only ONE Common coach** on release — do not buy them for farming.'''),
])

patch('/home/user/dls26-omega/docs/BRIEFING.md', [
 ('> **Basis:** ckpt-153 — **1,856 claims / 392 evidence records**',
  '> **Basis:** ckpt-154 — **1,872 claims / 393 evidence records**'),
 ('| Post-DLS25 coach breakthrough percentages | The DLS20 baseline (Common 5% / Rare 10%) is confirmed; DLS26 figures are unpublished. The **efficiency ladder is now known** (23.33 gems/point at max), only the breakthrough rate is not |',
  '| ~~Post-DLS25 coach breakthrough percentages~~ | **CLOSED at ckpt-154: Common 5% · Rare 10% · Legendary 20%**, corroborated by three sources spanning DLS20–DLS24. The Legendary 20% is the figure that was missing |'),
 ('| 7 | **Coach deliberately, and treat breakthroughs as a risk.** A breakthrough on an unwanted stat **consumes development capacity**, and Legendary coaches **do not raise the upgrade cap**. At a maxed Training facility the efficiency ladder is **23.33 gems/point (Legendary) vs 31.5 (Common)** — which is why Training L4 is the best gem in the game. A full max costs ~**32,000 coins** via Common coaches or ~**30,000** via Rare. | Saves the most gems |',
  '| 7 | **Coach deliberately, and treat breakthroughs as a risk.** A breakthrough on an unwanted stat **consumes development capacity**, and Legendary coaches **do not raise the upgrade cap**. Breakthrough odds are **5% / 10% / 20%** by tier. **Keep one Legendary Special coach in reserve: it previews the next four stats and can be cancelled without being spent** — worth ~420 gems per special player. At a maxed Training facility the efficiency ladder is **23.33 gems/point (Legendary) vs 31.5 (Common)**. A full max costs ~**32,000 coins** via Common coaches or ~**30,000** via Rare. | Saves the most gems |'),
])
