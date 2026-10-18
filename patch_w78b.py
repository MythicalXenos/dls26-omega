#!/usr/bin/env python3
"""ckpt-154b: fix the evidence references, the BRIEFING anchors, and resolve the 5.8-vs-23.33
gems-per-point conflict."""
import io
def patch(P, subs):
    t=io.open(P,encoding='utf-8').read()
    for a,b in subs:
        assert a in t and t.count(a)==1, 'ANCHOR PROBLEM in '+P+': '+a[:70]
        t=t.replace(a,b,1)
    io.open(P,'w',encoding='utf-8').write(t)
    print('patched', P)

patch('/home/user/dls26-omega/docs/operational_rules.md', [
 ('''- **BREAKTHROUGH LADDER:** Common **5%** · Rare **10%** · Legendary **20%** — three sources, DLS20–DLS24.
- **🎯 LOOK-AHEAD TRICK:** a Legendary Special coach previews the **next four stats** and can be **cancelled without being consumed**. Keep one in reserve at all times; worth **~420 gems per special player**.''',
  '''- **BREAKTHROUGH LADDER:** Common **5%** · Rare **10%** · Legendary **20%** — three sources, DLS20–DLS24 [EV-491, C2].
- **🎯 LOOK-AHEAD TRICK:** a Legendary Special coach previews the **next four stats** and can be **cancelled without being consumed**. Keep one in reserve at all times; worth **~420 gems per special player** [EV-491, C2].'''),
 ('''- **Coach prices:** Common 17g · Rare 52g (maxed) / 67g · Legendary 157g (maxed) / 202g — so Training saves 15g per Rare and 45g per Legendary.''',
  '''- **Coach prices:** Common 17g · Rare 52g (maxed) / 67g · Legendary 157g (maxed) / 202g — so Training saves 15g per Rare and 45g per Legendary [EV-491, C2].
- **Rare goalkeepers yield only ONE Common coach** on release — do not buy them for farming [EV-491, C3].
- **Agent odds:** ~1% per legendary agent, ~10–15% for a specific Champion; buying and releasing during an event keeps cards in Recovery and out of the transfer window [EV-491, C3].'''),
 ('| 5.5 | Coach prices: **Common +1 stat / 17g · Rare +2 / 52g · Legendary +3 / 157g** — all land at **~5.8 gems per point** | price | EV-439 |',
  '''| 5.5 | Coach prices: **Common +1 stat / 17g · Rare +2 / 52g · Legendary +3 / 157g** — all land at **~5.8 gems per point** | price | EV-439 |
| 5.5b | **Two efficiency figures coexist and they measure different things** [EV-439, EV-491]: **~5.8 gems per point** counts the points a coach delivers **across every player it can train**, while **23.33 gems per point** counts the points delivered **to one player** (280g / 12). Both are correct; the 5.8 figure is the one that applies when you are training several players at once. **This resolves the wave-76 conflict flag** | accounting | EV-439 / EV-491 |'''),
])

patch('/home/user/dls26-omega/docs/BRIEFING.md', [
 ('> **Basis:** ckpt-153 — **1,856 claims / 392 evidence records**',
  '> **Basis:** ckpt-154 — **1,872 claims / 393 evidence records**'),
 ('| Post-DLS25 coach breakthrough percentages | The DLS20 baseline (Common 5% / Rare 10%) is confirmed; DLS26 figures are unpublished. The **efficiency ladder is now known** (23.33 gems/point at max), only the breakthrough rate is not |',
  '| ~~Post-DLS25 coach breakthrough percentages~~ | **CLOSED at ckpt-154: Common 5% · Rare 10% · Legendary 20%**, corroborated by three sources spanning DLS20–DLS24. The Legendary 20% is the figure that was missing |'),
 ('| **7** | **Coach deliberately, and treat breakthroughs as a risk.** A breakthrough on an unwanted stat **consumes development capacity**, and Legendary coaches **do not raise the upgrade cap**. At a maxed Training facility the efficiency ladder is **23.33 gems/point (Legendary) vs 31.5 (Common)** — which is why Training L4 is the best gem in the game. A full max costs ~**32,000 coins** via Common coaches or ~**30,000** via Rare. | Saves the most gems |',
  '''| **7** | **Coach deliberately, and treat breakthroughs as a risk.** A breakthrough on an unwanted stat **consumes development capacity**, and Legendary coaches **do not raise the upgrade cap**. Breakthrough odds are **5% / 10% / 20%** by tier. **Keep one Legendary Special coach in reserve: it previews the next four stats and can be cancelled without being spent** — worth ~420 gems per special player. At a maxed Training facility the efficiency ladder is **23.33 gems/point (Legendary) vs 31.5 (Common)** — which is why Training L4 is the best gem in the game. A full max costs ~**32,000 coins** via Common coaches or ~**30,000** via Rare. | Saves the most gems |'''),
 ('Thirty-four of the corpus', 'Thirty-five of the corpus'),
])

patch('/home/user/dls26-omega/docs/strategy_masterplan.md', [
 ('**KB basis:** ckpt-153 — 1,856 claims / 392 evidence records',
  '**KB basis:** ckpt-154 — 1,872 claims / 393 evidence records'),
])
