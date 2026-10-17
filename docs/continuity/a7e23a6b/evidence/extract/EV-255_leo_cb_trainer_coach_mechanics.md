# EV-255 — LeoH321/dls26-tool-CB "DLS26 后卫练卡推演 (唯抢断胜率版)" (DLS26China WeChat CB-train simulator): coach-training probability engine
**Date:** 2026-10-18T01:30Z
**Tool:** api.github.com raw pull of LeoH321/dls26-tool-CB (README.md is a Chinese-language single-page trainer; index.html is the actual simulator). Title bar attributes the simulator to WeChat public account "DLS26China" (same Chinese community as EV-247).
**Origin:** Chinese community CB ("后卫" = defender) card-training simulator. The JS is a fully-specified exhaustive combinatorial solver for which coach rarity to pick next during player development to maximize the probability of reaching a target attribute value (e.g. TKL 100). Because the bot/dp_core model embeds the author's model of DLS26 coach/training mechanics in executable form, it is a much higher-fidelity signal than a prose guide — the parameters are the game's rules as observed by the community.

**Authenticity limits:** Community-constructed simulator, not FTG-dumped code. Mechanics here are asserted by the Chinese competitive community and implemented in a solver; they should agree with EV-247's +1/+2/+3 coach boosts and EV-052's triad dev system. We treat this as High-Confidence corroboration with quantified math.

## Coach tiers (three rarities; action IDs in code)
- **1 = 普通教练 (白 / White / Common):** +1 to selected attributes, cost = sumWeight × 1.
- **2 = 稀有教练 (蓝 / Blue / Rare):** +2 to selected attributes, cost = sumWeight × 2.
- **3 = 传奇教练 (金 / Gold / Legendary):** +3 to selected attributes, cost = sumWeight × 3.
This corroborates EV-247's +1/+2/+3 coaching system exactly. Color coding in the UI matches in-game: white < blue < yellow < gold border (wait — simulator uses white/blue/gold; the yellow/epic tier presumably exists but this specific solver only implements 3 tiers, matching the EV-247 COMMUNITY/RARE/EPIC? — need to resolve).

## Attribute weighting (POSITION-SPECIFIC)
For the CB (defender) training target shown, attributes have these weights toward capacity cost:
- 控制 (CON/Control): weight 2
- 传球 (PAS/Passing): weight 1
- 射门 (SHO/Shooting): weight 1
- 抢断 (TKL/Tackling): weight 1 (and is the isTarget attribute)

**CRITICAL:** Control (CON) costs TWICE as much capacity per point added as other attributes. This is the weighted-capacity system EV-247/CLAIM-049 described qualitatively; now quantified: CON weight=2, PAS/SHO/TAC/PRE/ACC/etc. weight=1 for CB. This explains why EV-247 described coach-development as a weighted capacity system — you do NOT get uniform points per coach use; capacity cost is Σ(weight_of_attribute_hit × boost_level).

## Training mechanic rules (from dp_core)
1. **Capacity budget (cap)** is consumed at a rate of `sum_of_weights_of_selected_stats × coach_boost_level`. Example: a gold coach (+3) hitting only CON costs 2×3 = 6 capacity. A gold coach hitting CON+PAS costs (2+1)×3 = 9 capacity.
2. **Coach picks = `action` (1/2/3) attributes at random** from the pool of attributes not yet at 100, with each combination weighted equally (uniform random over C(n,k) where k = boost level, n = number of non-maxed attributes). The bot enumerates ALL combinations of size k (k-th row of Pascal) and averages probabilities.
3. **Each picked attribute gets +`action` points**, hard-capped at 100 (`Math.min(100, val + action)`).
4. **Attributes at 100 are removed from the draw pool** (`if (ctrl<100) pool.push(...)`) — this prevents "wasting" capacity on stats that are already maxed; the game engine automatically skips maxed attributes.
5. If `cost > cap` (over-capacity "爆仓" / busting), the remaining capacity is distributed fractionally: `gainedStat = cap / sumWeight`, and only attributes in the combo receive proportional gains (no integer rounding — fractional gains accumulate to next integer). The simulator treats busting as risky because gains get diluted.
6. **Success condition** for the solver: target attribute (e.g. TKL) reaches target_tkl (the user-supplied goal value, commonly 100 for a "polarized" build).
7. The DP maximizes the probability of reaching the target; on ties, maximizes expected final target attribute. Recommended coach is the argmax over {1,2,3}.

## Stat cap and training cap
- Per-attribute hard cap is **100** (`Math.min(100, …)`) — confirmed by the border-highlight rule (`if curr>=100 → blue border`). EV-252 promo stats show individual attributes can already hit 100 on maxed cards (Arda Güler ACC/STA/CON/PAS=100, Eze ACC/CON/PAS=100, De Paul STA/PAS/CON=100). 100 is the hard stat cap, period.
- Training capacity ("容量" / "安全点数") is a shared budget. The simulator's "remain" panel uses `≥12` green (SAFE), `≥6` gold (CAUTIOUS), `<6` red (DANGER), `≤0` red "潜能已满" (potential full / capacity exhausted).

## Coach recommendation logic / decision persona
The solver returns a probability for each coach tier and selects the highest-probability one, with text personas:
- Gold coach (+3): "用金教练强开覆盖，利用+3的爆发力，哪怕爆仓也能强行灌分" (force open coverage with gold, use +3 burst, even busting can force-inject points — highest variance)
- Blue coach (+2): "金教练爆仓平分后容易被高权重属性拖累，白教练单点效率又太低。蓝教练+2的爆发刚好" (gold bust gets dragged down by high-weight attrs; white is too slow; blue +2 is the sweet spot)
- White coach (+1): "容量已经极度危险…切白教练，用最小代价死抠" (when capacity is critical, switch to white for minimal cost)
This matches EV-247's qualitative recommendation to pick coaches based on current weighted capacity remaining.

## Color thresholds (stat number coloring in DLS UI)
- ≥90 → blue
- ≥80 → green
- ≥70 → yellow
- <70 → red
These are the per-stat color bands shown on the in-game card (same coloring is documented in EV-246 card-creator UI).

## Position-specific weighting
This page is explicitly the **CB (defender) 唯抢断胜率版 (tackle-only winrate)** build. Only 4 attributes appear (CON/PAS/SHO/TKL) because a defender card's trainable attributes for a tackle-polarized build are those four — SHO is typically ignored for defenders but is still in the cost pool. The framework generalizes; the author suggests they have similar simulators for other positions/builds (title says "这回合" implying a series). We do not have other-position weights yet, but CB weight pattern (CON=2, others=1) is explicit.

## Covers
CLAIM-154 (coach tiers 1/2/3 = +1/+2/+3, colors white/blue/gold, cost = Σw·b), CLAIM-155 (weighted training capacity: CON weight=2 for CB, others=1), CLAIM-156 (trainer mechanic: k attributes drawn from non-maxed pool uniform; hard cap 100; fractional overflow distribution), CLAIM-157 (stat color bands: ≥90 blue, ≥80 green, ≥70 yellow, <70 red), CLAIM-158 (CB-tackle-polarized optimal strategy: gold/blue/white picked by capacity thresholds ~12/~6), CLAIM-049 (weighted-capacity corroborated, upgraded), CLAIM-052 (triad Players-Coaches-Physio context, coach leg now concrete), CLAIM-247 (EV-247 +1/+2/+3 corroborated and quantified).
