# EV-247 — Chinese-community Coach DP model (LeoH321/dls26-tool-CB, DLS26China)
**Date:** 2026-10-17T23:25Z
**Tool:** GitHub API raw fetch of `index.html` from `LeoH321/dls26-tool-CB` (single-file HTML+JS coach-optimisation tool).
**Origin:** DLS26China WeChat community tool (per page branding: "微信公众号：DLS26China"). Title: "DLS26 后卫练卡推演 (极限胜率版)" — DLS26 defender training-card deduction (max-win-rate version).
**Authenticity limits:** single-community tool, reverse-engineered/observed mechanic, not official. The DP model encodes a specific hypothesis about how coach upgrades resolve; we record it as a high-value community model, not confirmed truth. It specifically targets CB (defender) training, using four technical stats: 控制 (CON/Control), 传球 (PAS/Passing), 射门 (SHO/Shooting), 抢断 (TKL/Tackling).

## Mechanic model encoded in the tool (verbatim from JS)

1. **Three coach rarities = three actions**, each choosing k = rarity stats to upgrade out of the eligible pool and granting +rarity points to each chosen stat:
   - White (Common, id=1): k=1, gain +1, cost = sum(weight of chosen stats) × 1
   - Blue (Rare, id=2): k=2, gain +2, cost = sum(weight) × 2
   - Gold (Legendary, id=3): k=3, gain +3, cost = sum(weight) × 3

2. **Stat weights (technical coach for defenders)**:
   - 控制 CON: weight 2
   - 传球 PAS: weight 1
   - 射门 SHO: weight 1
   - 抢断 TKL (tackling, target stat): weight 1
   (Note: CON weight 2 — this corroborates sakibpro's "weighted progression energy" hypothesis CLAIM-104, but is a different weight set. Fitness/Goalkeeping/Special coaches are not modeled in this tool.)

3. **Stat cap at 100**: any stat at 100 is removed from the selection pool, regardless of whether the target is met (hard cap).

4. **"Safe capacity" pool** (`exactCap`) is computed as `sum((target - current) * weight)` over the four trained stats. The tool's UI warns:
   - ≥12 points remaining → green (accent-target, "safe")
   - 6–11 → gold ("careful")
   - ≤5 → red (accent-warn, "near bust")
   - ≤0 → capacity exhausted (潜能已满).

5. **Combination resolution**: for each action the DP enumerates all k-combinations of the eligible pool, then either:
   - If `cost > remaining cap`, a fractional allocation (`gainedStat = cap / sumWeight`) is applied — i.e., over-capacity coaches "spill" and only partial stat gain happens. TKL gain is capped at min(rarity, gainedStat) if TKL is in the combo.
   - Otherwise each chosen stat gains +rarity points, capped at 100.

6. **Target is a SINGLE stat** (in this tool, TKL tackling). The DP chooses the action (white/blue/gold) that maximises the probability of reaching the user-set target TKL value, tie-broken by expected final TKL. This confirms community theory CLAIM-105 is directionally right ("coaches pick stats randomly and you're gambling on weighted hits") but far more specific: the selection is uniform over k-combinations of eligible stats, weighted by stat weight for cost, with known +1/+2/+3 gains.

7. **Colour thresholds in UI** mirror in-game card colours: <70 red, 70–79 yellow, 80–89 green, ≥90 blue. This is just display logic but corroborates EV-143 (card-colour taxonomy: bronze=common, blue=rare, gold=legendary, plus an extra "blue/90+" tier for stats that's just the tool's styling, not in-game).

8. **Luck score** (persona text): 10/10 if prob ≥0.8, down to 1/10 if prob=0. This is cosmetic UI, not a mechanic.

## Analytical consequences
- **CLAIM-008 / CLAIM-104 (weighted progression, sakibpro) PARTIALLY CORROBORATED but with different weights.** Sakibpro's simulator claimed CON/SPE cost more capacity; this Chinese DP assigns CON weight 2, PAS/SHO/TKL weight 1 for TECHNICAL coaches (SPE/ACC/STA/STR are fitness-coach stats and not modelled here). The sakibpro "100% cumulative weight = +10 ceiling" claim is NOT directly tested because this tool works in absolute "point" capacity rather than percentage.
- **CLAIM-006 (release yields "fitness coaches" for injury recovery) is NOT addressed** — this is a technical-coach DP, not fitness.
- **CLAIM-105 ("trained = base + 1" theory) is WRONG/incomplete in its "+1" form** — coaches grant +1/+2/+3 per applied stat depending on rarity, not a flat +1. The "+1" rumor likely describes common-coach single-stat outcomes only.
- **A new practical claim**: coaching a target stat to a desired threshold is a COMBINATORIAL GAMBLE with known action space, NOT a deterministic "feed coaches to the player". This explains why players report "stats never go where I want" (CLAIM-091 complaints) — it is a weighted-random allocation with capacity cost, not directed training.

## Caveats
- The tool encodes the COMMUNITY MODEL, not a datamined constant table. We treat it as Community Consensus with unusually strong specificity. Step-2 datamining must verify the +1/+2/+3 gains and weight table.
- Only the TECHNICAL-coach defender case is modeled; fitness/goalkeeping/special weights are NOT evidenced by this tool.
- The fractional "over-cap" allocation (cost > cap, gainedStat = cap/sumWeight) is the most speculative line — confirm in Step 2.

## Covers
CLAIM-134 (new — coach DP model: +1/+2/+3 gains, weights, capacity pool), CLAIM-104 (corroborates + partially revises sakibpro weights), CLAIM-105 (revised — "trained=base+1" is a mis-description of common-coach behaviour), CLAIM-091 (explains training-randomness complaints).
