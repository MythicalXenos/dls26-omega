# DLS26 OMEGA — Operational Rules & Audit

> **DERIVED VIEW — the authority is `kb/claims.jsonl` + `docs/strategy_masterplan.md`.** Where this file and a claim record disagree, the claim record wins and this file is corrected.
> Every rule below carries its evidence. Rules marked **[UNVERIFIED]** rest on Community Consensus or below and must be treated as hypotheses, not instructions.
> Basis: ckpt-143 — 1,727 claims / 383 evidence records. Companion to `docs/strategy_masterplan.md`.

---

## 0. How to read this

The masterplan says *what* to aim for. This file says *what to do in each game state*, in order, with the guards that move you between states. It is written so a decision can be made in under five seconds at the phone.

**Three rules govern everything below:**

> **R-0.1 — The coin rule.** Coins are the scarcest real constraint early; gems are the scarcest throughout. Never spend gems on anything that coins can buy. **[EV-441, C2]**
> **R-0.2 — The rating trap.** Do NOT buy legendary players before the stadium is maxed — they raise team rating and the cheap players vanish from the market, killing the coach-farming loop that actually builds the squad. **[EV-441, C2]**
> **R-0.3 — The honesty rule.** Infinite coins and gems do not exist; mods get your account blocked and generators are scams. There is no shortcut. **[OFFICIAL FTG, GS-020]**

---

## 1. The state machine

Nine states. You are always in exactly one. The guard column is the *only* thing that changes your state.

```
S0 BOOTSTRAP ──guard: 1,500c + 75g claimed, name/kit/logo set──▶ S1
S1 ECONOMY BOOTSTRAP ──guard: daily+weekly challenges running, ads cycling──▶ S2
S2 PROMOTION PUSH ──guard: top-2 finish OR 3rd-6th playoff won AND stadium class met──▶ S3
S3 SECURE DIVISION ──guard: division no longer winnable this season──▶ S4
S4 COIN FARMING ──guard: stadium maxed (92,632) ──▶ S5
S5 COACH FARMING ──guard: ~80 upgrade points/player achieved across XI──▶ S6
S6 SQUAD ASSEMBLY ──guard: team rating 80+ ──▶ S7
S7 DLL CLIMB ──guard: Tier 3 reached (first fully-maxed wall)──▶ S8
S8 CULTIVATION ──guard: Tier 1 Champion held across consecutive seasons──▶ S9
S9 MAINTENANCE (goal state)
```

Any state → **any** state on a Patch Response trigger (see §6).

---

## 2. State definitions and rules

### S0 — Bootstrap (Day 0, one sitting)

| # | Action | Value | Evidence |
|---|---|---|---|
| 0.1 | Claim the starter grant | **1,500 coins + 75 gems** | EV-441 |
| 0.2 | Set the manager name, club name, kit and logo (kit import is **150 gems** and **512×512 px** max — do it only if you have a real kit) | cosmetic | EV-437 |
| 0.3 | **Pick your best attacker as captain** — it boosts team rating, which improves who appears in the market | rating | EV-441 |
| 0.4 | Confirm you are NOT connected to Facebook (save-tampering does not work when cloud-linked) | — | EV-439 |

**Do not:** import a kit on Day 0. Do not buy players yet. Do not enter DLL yet.

---

### S1 — Economy bootstrap (first 48 hours)

| # | Action | Value | Evidence |
|---|---|---|---|
| 1.1 | Log in every day — the login cycle is **20 days** and **restarts from Day 1 if you miss one** | coins + occasional gems | EV-445 |
| 1.2 | Complete the **full** Daily challenge set | **5–11 gems/day**, ~70–100 coins | EV-445 |
| 1.3 | Complete the **full** Weekly challenge set | gems for the set | EV-445 |
| 1.4 | Reroll a bad daily objective — you get **2 rerolls per day**, 2 per week for weekly | free | EV-445 |
| 1.5 | Run **one 8-hour ad cycle** | up to **600 coins** | EV-437 |
| 1.6 | Play the **Daily Scenario** — 50 coins, you are already losing and must beat Hard AI | 50 coins | EV-445 |
| 1.7 | Buy **1–2 fast common or rare players** to win games. Nothing more. | — | EV-441 |

**Guard to S2:** challenges and ads are cycling daily, and you have a squad that can win.

---

### S2 — Promotion push

**The promotion rule** [EV-437, C2]: finish **top 2**, or finish 3rd–6th and win the playoff. There is also a **stadium class gate** — you cannot promote without it, whatever your league position.

| # | Action | Value | Evidence |
|---|---|---|---|
| 2.1 | Play every Career match with intent to win. Goal coins are **capped at 30 per match** (6 goals × 5) — do not chase a 7th | ≤30 coins | EV-441 |
| 2.2 | Win Career matches by **4+ goals** to maximise Season Points (40 SP/day target) | SP | EV-437 |
| 2.3 | Rotate for stamina: **30% regen** per match played, **full regen** on the bench, sub at **60–70 min**, **3-sub limit** | stamina | EV-437 |
| 2.4 | The **cup follows your current division** — you get one shot per division per season | cup | EV-437 |
| 2.5 | Check the stadium class requirement **before** the final rounds, not after | promotion | EV-437 |

---

### S3 — Secure division (the time-efficiency unlock)

**This is the single highest-value state transition in the game** [EV-441, C3].

> A Legendary **home** match pays **~150 coins even in a LOSS** (75 base + 75 stadium). Once the division is secured, **auto-finish and lose** every remaining home match. You sacrifice only a 10-gem win-all objective and gain the time for everything else.

| # | Action | Value | Evidence |
|---|---|---|---|
| 3.1 | Detect "division is secure" = mathematically promoted, or unwinnable this season | — | — |
| 3.2 | **Auto-finish and lose** remaining home matches | ~150c each | EV-441 |
| 3.3 | Never auto-finish a match you still need to win | — | — |
| 3.4 | If the division is unwinnable, spend the season farming instead | coins | EV-441 |

**Throughput:** ~10 matches ≈ **2,000 coins/hour**; ~**110 gems per season** from DLL.

---

### S4 — Coin farming (until the stadium is maxed)

**Order of operations — this matters:**

| # | Action | Why |
|---|---|---|
| 4.1 | **Forfeit Career matches** — earns coins, **does NOT refresh the transfer market** | EV-442 |
| 4.2 | **Play scenarios** (50/day) — earns coins, **does NOT refresh** | EV-442 |
| 4.3 | **Exhibition matches** — earns coins, **does NOT refresh** | EV-442 |
| 4.4 | **Watch free ads** (30 each, up to 600/cycle) — **does NOT refresh** | EV-442 |
| 4.5 | **Dream Draft** — **does NOT refresh** | EV-442 |

> **Why 4.1–4.5 are the whole point:** the market refreshes **after every match you play**. So farming coins via forfeits/scenarios/ads lets you **save for a specific target player without burning the slot they are sitting in.** This is the correct answer to "I can't afford the player I want." **[EV-442, C2/C3]**

**Fastest legitimate refresh, when you DO want one:** quit a **LIVE** match at half-time, or play the first half and forfeit. **[EV-442, C3]**

**The stadium build** [EV-437, C2]: follow the optimal stand order (N20 / NE49 / E26 / SE45 / S20 / SW49 / W26 / NW49) to **92,632 capacity / 52 coins per home game**. It maxes in **~3 months** just by playing home games — do not shortcut it with gems.

**Guard to S5:** stadium at 92,632.

---

### S5 — Coach farming (the actual rating engine)

**The loop, in order:**

| # | Action | Value | Evidence |
|---|---|---|---|
| 5.1 | Buy **common players at ≤180–210 coins** | cheap input | EV-437 |
| 5.2 | Buy **80-rated defenders** for rares — defenders are the cheapest 80s | cheap input | EV-437 |
| 5.3 | **Release** them — release yields **coaches, not coins** | the point | EV-442 |
| 5.4 | **Train** with the coaches: **7:3 or 90:10 fitness:technical** | ratio | EV-437 |
| 5.5 | Coach prices: **Common +1 stat / 17g · Rare +2 / 52g · Legendary +3 / 157g** — all land at **~5.8 gems per point** | price | EV-439 |
| 5.6 | One full max costs **~32,000 coins (Commons)** or **~30,000 coins (Rares)** | budget | EV-439 |
| 5.7 | **~80–81 upgrade points per player**, ~8 stat points per OVR point | budget | EV-439 |
| 5.8 | **STR and CON count ×2** toward the total — **except wingers** | weighting | EV-439 |
| 5.8b | **✅ C-027 RESOLVED ON AN OFFICIAL BASIS (ckpt-126).** FTG's own stat model makes both community positions true at once: SPE's effect is **conditional** (falls with energy, and falls when dribbling *inversely to CON*, so a lower-SPE player can outrun a higher-SPE one), while **CON/PAS/TAC each govern a possession action** and **STR** decides who keeps the ball in a collision. **Recruit for both — a fast spine with a technical core** — and weight **STA by position** (high on midfielders/wingers, low on centre-backs). **Verify in Exhibition before committing a coaching plan** remains in force: the community reports describe the current build's *tuning*, which the official article does not quantify. | weighting | EV-455, EV-456 |
| 5.9 | **GK coaches touch only GKR + GKH.** A Legendary GK coach is usable **only if GKR > GKH** | constraint | EV-439 |
| 5.10 | **THE OFFICIAL STAT MODEL is the coaching bible** [EV-456, C1]: **SPE** top speed, energy-gated and CON-gated while dribbling · **ACC** time to top speed · **STA** energy drain + half-time restore, position-weighted · **CON** dribbling speed loss, touch quality, and the gate on every skill move · **STR** collisions and stumble time · **TAC** the *distance* a tackle can be made from · **PAS** accuracy of all passes · **SHO** accuracy, 'assist', keeping shots low, and free-kick curl · **GKH** catching/claiming/stability · **GKR** reactions and anticipate saves · **ENERGY** below a threshold every stat decays | weighting | EV-456 |
| 5.11 | **Plan on a ONE-match Form Boost.** The official article gives only the rule (a set number of matches, minimum one) and **no source publishes the per-Training-level numbers** — a documented negative after a dedicated sweep | budget | EV-457 |
| 5.12 | **Do not build any plan on a "Fan Approval" mechanic** — a dedicated sweep found **no such system in any documented DLS26 source**. Fan Approval is a *readout* of total squad development (100% club value needs every player maxed, ~23 men), not a lever | guard | EV-457 |
| 5.13 | **Injury-proof substitution:** start with 5 bench players in the XI, enter the match, then use **all 5 subs before kick-off** to bring the real XI on — *"players can't get injured if you don't have players to sub them off for."* Career only; never in DLL, where the subs are worth more than the injury risk | guard | EV-457 |

**THE SET-PIECE RULES** [EV-475, C3]:

| Rule | Detail |
|---|---|
| **Corners are the most reliable goal source** | *"Corners are way too easy to score now. If your opponent in DLL gets one, its almost guaranteed that you concede"* |
| **C-022 RESOLVED — two deliveries, not two opinions** | **SAME foot = out-swinger** (curves away from goal; header back toward goal with pace; keeper cannot claim) · **OPPOSITE foot = in-swinger** (curves toward goal; suits near/far-post headers but brings the ball to the keeper) |
| **Adopt the out-swinger for the near-post routine** | Right-footed on the right corner, left-footed on the left; aim near the goal post |
| **The out-swinger technique** | Call a second player first (drags a defender out, opens space for your striker), set out-swinger, then **max B** and shoot |
| **Shortest players take the corners** | So the players in the box are on average taller |
| **Take from behind the goal line** | Not from beside the sideline; arrow ~90% inside the pitch, or ~30° to the goal line |
| **Press A right before arrival** | And if the header is not on, press **B to pass** to someone better placed (DLS25 nerfed headers) |
| **Free-kick footedness inverts** | A **left-footed** taker is the more versatile option — it works from both sides |
| **Short corner is a real option** | Hold B to the nearest player outside the box and set up a long shot |

**THE MATCHCRAFT RULES** [EV-474, C3] — the execution layer:

| Rule | Detail |
|---|---|
| **DLL unlocks after SIX Career matches** | Which also unlocks Friend Match. Play six regardless — they pay coins and Season Points (C-025 substantially resolved) |
| **Defending: no joystick while holding B** | Your player moves toward the ball automatically; steering fights it |
| **Never push defenders forward** | A DM presses in midfield; zonal out of possession |
| **Slide tackles sparingly, never on the counter** | Block shots; press C for the keeper; aerial ball = press B at the nearest midfielder |
| **Tactic switching is a rhythm** | Defensive the moment they have it, attacking the moment you win it, balanced to reset |
| **Anti-C-spam escalation** | Head diagonally backwards toward the second striker, then escalate the back line 3 → 4 → 5 |
| **Footedness placement** | Left-footed at LB/LCB, right-footed at RB/RCB; strikers inverted |
| **One-on-one: hold C, then release** | Lowers their scoring chance and prevents chip shots |
| **Verify the secondary press** | The DLS26 update nerfed it — the secondary-press model above is the pre-nerf version, so re-check in Exhibition |

**THE SEASON PASS RULES** [EV-472, C2]:

| Rule | Detail |
|---|---|
| **Two paid tiers** | Basic ~**$4** (INR 399) · Premium ~**$13–15** (INR 1,199 / $14.60). Not a subscription — **repurchase every 10-day season** |
| **The free track is worth claiming regardless** | **1,095 coins + an Epic agent**, with no purchase |
| **Levels are STORED, not lost** | *"If you don't play every 10 hours, the game will store the level so that you can advance multiple levels at once"* — inactivity costs nothing |
| **Buy LATE or not at all** | A late purchase **backfills every premium tier already unlocked for free**, so early buying gains nothing |
| **Premium's real value is double XP** | Double Season Points *and* double Live XP (faster Progress Bank and leaderboard), tiers to Tier 8 up front, gold trim, better packs |
| **Verdict** | *"Most suitable for a new player but not so much for a veteran"* — if the squad and facilities are maxed, the rewards stop mattering |

**THE FACILITY COST LADDER** [EV-468, C2] — the budget rule that replaces "1,125 per facility":

| Rule | Detail |
|---|---|
| **Level N costs 75 × N gems** | Confirmed on Training and Accommodation: 75, 150, 225, 300, 375, 450, 525, 600, 675, 750 |
| **Five levels = 1,125 gems** | That is the cheap half, not a maxed facility |
| **Ten levels = 4,125 gems** | Full max per facility; Accommodation is published at 10 levels for **+4 squad space each** |
| **Spend the first five widely** | Training to L5 (1,125) and Accommodation to L5 (1,125) are affordable early and are the two facilities the community rates |
| **Be deliberate about the second five** | Another 3,000 gems each — only for a facility you will actually use |
| **Level counts for Medical, Commercial and Fanzone are unpublished** | The 75 × N pattern is inferred, not confirmed, for those three |
| **The stadium is a COIN project** | Sector levels cost 0–650 coins, so it never competes with facilities for gems |

**THE COACHING METHOD** [EV-467, C3] — how to spend coaches without wasting capacity:

| Rule | Detail |
|---|---|
| **A breakthrough is a RISK** | *"You can't control when or where it applies, so if you get it to tackling when you're maxing a striker it can reduce total points available to the good stats."* A breakthrough on an unwanted stat **consumes development capacity** |
| **Train ONE player at a time** | Chain Common coaches by category — all Technical to max the tech stats, then all Fitness — and save the single Rare for the stat that stalls |
| **Prefer Common coaches for control** | With Rare/Legendary coaches *"you basically don't have any influence on what stats get picked"*, and a disappointing result costs thousands of gems to redo |
| **Budget by weight, not by points** | **CON and SPE consume more development capacity than STA**, and the **+10 OVR cap is a 100% cumulative weight** — so a CON-heavy player eats the budget faster |
| **Midfielders are the hardest build** | They *"always come out weirdly built"* — expect to compromise on one of CON / PAS / STA |
| **Breakthrough percentages are unpublished** | The DLS20 baseline is Common 5% / Rare 10%; no DLS26 figures exist, only that Legendary has *"higher Breakthrough chances"* |

**THE FORMATION RULE** [EV-464, C3] — there is no best shape, only failure modes:

| Rule | Detail |
|---|---|
| **Learn 4-4-2 first** | *"Two banks of four, two up top, no clever ideas. Nothing brilliant happens. Nothing catastrophic happens either"* — put it on and don't touch it for twenty matches |
| **Switch to 4-2-3-1 at Tier 1** | Tier-1 players report the change: *"when I get to tier 1 I tend to meet a lot of people who attack better than I do so I change to a 4-2-3-1. 1 extra defensive mid helps me a lot"* |
| **4-2-2-2 for online** | Two strikers, two CAMs wide, two CDMs, back four — rising because DLS25 **nerfed 4-1-2-1-2's wide mids** so they no longer defend |
| **Avoid 4-3-3 in close games** | Scores the most but concedes the most — wide forwards don't track back |
| **Never five at the back online** | *"Usually not a good idea"* |
| **STAMINA BEATS SHAPE** | *"A 4-3-3 with fresh legs at minute 70 beats a 'perfect' 4-2-3-1 with three players at low stamina."* **Rotation is a tactical decision** |

**ACCOUNT GUARDS — the rules that protect the whole mission** [EV-462, **C1 — OFFICIAL**]:

| Rule | Detail |
|---|---|
| **One account per player** | *"We have limited each player to one DLS account."* The profile is bound to **Sign in with Google (Android)** or **Sign in with Apple (iOS)** — pick the platform you will keep |
| **NEVER sign out** | Signing out of Google/Apple *"at any point whilst playing"* unlinks the account from the profile and exposes it to **total loss** on uninstall or device change. A lost profile **cannot be recovered** |
| **Cross-platform transfer** | Only via a code: **Manage Devices → Generate Code** on the old device, typed into **Link Profile** on the new one (both under Options → gear → **Advanced**). A code cannot be used on the device that generated it |
| **No cheap re-roll** | **Reset Profile** (Settings → Advanced, skull icon) is irreversible, destroys all coins, gems, consumables **and in-app purchases**, and is limited to **ONE RESET EVERY 30 DAYS** |
| **The region seed is permanent** | The account decides the matchmaker pool and the leaderboard surface. Set it up deliberately and **play through early mistakes — do not reset** |

**The stadium capacity gate** [EV-460, C2] — the rule that can silently stall a Career season:

| Rule | Detail |
|---|---|
| **Capacity gates promotion** | Win the league without the seats and you **stay in the division**: Academy 6,462 → Div 3 15,000 → Div 2 30,000 → Div 1 45,000 → Junior Elite 60,000 → Elite 80,000 (max 90,456) |
| **Build corners first** | Corners are the cheap seats — Corner 7 is about **100 coins for 722 seats**. Corner stands give the most seats per coin |
| **Never half-upgrade a stand** | A partial side must later be paid for **at full price** to complete |
| **One stand at a time, lowest to highest** | Max one stand before starting the next; **leave one corner stand un-upgraded** — 7 maxed stands hit the top gate, 8 overshoot it |
| **Never roof the top level** | *"on the highest number you're paying for the roof and no extra seats"* |
| **Capacity is permanent** | **Downgrading was removed around DLS24** — build to the gate, not to a design, because it cannot be undone |
| **It is a COIN project** | Every sector level costs coins (roughly 0–650), not gems — the facilities are the gem project, the stadium is the coin project |

**The Season Pass retroactivity rule** [EV-456, C1 — OFFICIAL]: rewards unlock one per 12 hours on the free track, **but a pass purchased late in the season unlocks all content regardless of those time locks** provided the Season Points are earned — and buying **instantly backfills the Premium rewards for every free tier already unlocked**. The pass is **not a subscription**. **If the pass is going to be bought at all, buy it LATE in the season:** same rewards, none of the waiting.

**Cult Heroes** [EV-459, C2] — 12 players, base ratings **85/85/85/84/84/84/84/84/83/83/83/83**, from **Cult Hero Agents in Events, Drafts and the Season Pass** (3 passes × 2 heroes, one free + one premium = 6 of 12). **The 92-vs-95 conflict is resolved: 85 = base, 92 = live-event boosted, 95 = fully maxed.** They are the **weakest special set by ceiling** — collect for the card, not the rating.

**The training-facility ladder** [EV-437, C2] — the unlock that makes 5.1–5.4 cheap:

| Level | Cost | Effect |
|---|---|---|
| L1 | **75 gems** | +5% |
| L2 | 150 gems | +10% |
| L3 | 225 gems | +15% |
| L4 | 300 gems | **Legendary coaches drop below 200 coins — THE FARMING UNLOCK** |
| L5 | 375 gems | +25% |

> **Buy L4 before anything else in the facility list.** It converts the entire coach economy from expensive to cheap. **Corrected at ckpt-132:** the old line here read "per-facility total is 1,125 gems; all five facilities is 5,625 gems" as though those were maxed costs. Under the **75 × level** pattern [EV-468, C2], **1,125 gems is the first FIVE levels** and a fully maxed facility is **4,125 gems**; level counts are published for Training and Accommodation and unpublished for Medical, Commercial and Fanzone. The first tier of every facility costs **375 coins** in DLS26. **[EV-437, EV-468, C2]**

**Facility priority order:** Training (L4 first) → Stadium → Medical → Commercial → Fanzone. **[EV-437, C2]**

**Medical** is numeric only at L1: **−5% injury chance, −10% healing cost** [EV-437, C2]. Do not assume a curve above L1 — that is an open gap.

**Guard to S6:** the XI each carry ~80 upgrade points.

> **R-5.1 — THE LADDER FEASIBILITY RULE.** Reaching 200,000 DP inside the 90-day Prize Ladder needs **at least 15 games a day** — roughly **54 career seasons in 90 days**, ~137 hours for all four icons. **A DLL win pays ~115 DP against a Career win's ~65 DP, so run the ladder on DLL.** Buy DP boosts **early** in a ladder: unused boosts carry over, and they do nothing on a dead ladder. **[EV-453, C3 / EV-452, C1]**

> **R-5.2 — BOOST EXCLUSIONS.** DP boosts apply to Career, Dream Draft, Scenario and DLL matches only. **Exhibition and Friend Matches earn no boosted DP** — practice there, farm DP elsewhere. **[EV-452, C1]**

---

### S6 — Squad assembly (the market layer)

| # | Action | Rule | Evidence |
|---|---|---|---|
| 6.1 | Buy the **highest-rated player at each refresh** to raise team rating and attract better ones | market | EV-442 |
| 6.2 | You **cannot buy a player you already own** — sell first | market | EV-442 |
| 6.3 | **Released players reappear** after a grace period with a repurchase window; **collection pieces never return** | market | EV-442 |
| 6.4 | **Lock Player: 20 or 40 gems pins any player for 24 hours** — the paid answer to waiting for one specific card | market | EV-442 |
| 6.5 | Legendaries appear individually or as **Top Picks**, at **~1,500–2,800 coins** once your rating attracts interest | market | EV-442 |
| 6.6 | Scouts: **Common 75 coins / Legendary 500 coins**; the Common's 5% legendary chance is good early value | market | EV-442 |
| 6.7 | Now, and only now, start buying legendaries | rating | EV-441 |
| 6.8 | Cards go **silver → gold → black at 100 OVR** | cards | EV-437 |
| 6.9 | **THE GACHA LEVER** — buy and sell every 80+ player you see so they sit in the recovery tab for two days, removing them from the Legendary Agent pool. Reported to take Champion odds to **100%** for ~275,000 coins across ~145 players and 70+ refreshes | agent odds | EV-450, C2 |
| 6.10 | Stack gold players in the market (they cannot be pulled while there) and **Lock** targets (costs gems). Pity ceiling ~15 Legendary Agents per target | agent odds | EV-450, C2/C3 |
| 6.11 | **NEVER release a Classic Player** — future Prize Ladders randomise rewards, so you may get them next time and miss the new ones | collection | EV-450, C2 |
| 6.12 | **DLS26: special players do NOT count toward squad size** — the club holds **unlimited** specials, so there is no collection cap | cards | EV-449, C1 |

**[UNVERIFIED]** The manager-name/nationality "refresh trick" — one poster states some say it works and some that it doesn't. **Do not plan around it.** [EV-442, C4]

> **~300 matches** after maxing the stadium is the reported cost of building a dream squad. **[EV-442, C3]**

---

### S7 — DLL climb (the ranked surface)

**Tiers are numeric and count DOWN: 20 → 1.** [EV-437, C2]

| Milestone | Reality |
|---|---|
| **Tier 10** | the Live gem floor — play here or above |
| **Tier 3** | the **first fully-maxed wall** — expect to stall |
| **Tier 2** | opponents at **10M+ XP** |
| **Tier 7 → 1** | ~**4 days** |
| **Tier 1** | reachable in **~16 days** |

**Scoring: 3/1/0. Gem rewards: 100/100/100/40/30.** DLL pays gems for a season finish with a **minimum of 14 points**. [EV-437, C2]

> **R-7.1 — THE GEM ENGINE.** When gems are the priority, **tier camp between Tier 5 and Tier 2 and aim for SURVIVAL, NOT PROMOTION**: win only 4–5 matches (12–15 points), quit the rest, and accept that losing en route keeps you in the camping tier. ~48 matches over 4–4.8 hours = 150–208 gems (~35–43/hour) against 5–11 gems/day from challenges. **Do not forfeit while camping.** Tier 1 cannot be camped. **[EV-448, C2/C3]**

> **R-7.2 — THE SQUAD RULE (C-024).** Keep the DLL squad **competitive but NOT maxed**; pursue full maxing as a *separate* club-value objective. Team strength is an official matchmaking input, so a stronger squad faces stronger opponents. The record Tier 1 run used a mostly common/rare squad. **[EV-447, C1 / EV-448, C2]**

> **R-7.3 — TACKLING IS WORTHLESS IN LIVE.** Defend with **95+ speed and acceleration** players; put your fastest attackers at centre-back; keep real centre-backs for corner height; full-backs slide rather than chase. **[EV-448, C2/C3]**

**Matchcraft — the mechanical edge** (full detail in masterplan §3.1):

| Rule | Detail |
|---|---|
| **Hold B while defending** | and do not touch the joystick |
| **Anti-wing and anti-C spam** | both solved by running players **BACKWARDS** |
| **Secondary press > main press** | always |
| **Auto-switch OFF** | always |
| **Corners** | A-cross, tall targets (190+), take from behind the goal line, shortest players on corner duty, press A **right before** the ball arrives |
| **Free kicks** | two dedicated takers (one left, one right), **70% power floor**, **the wall is your curl reference** |
| **Live free-kick trick** | wait for the opponent onto the line → **switch the taker** (resets their player) → shoot immediately |
| **Penalties** | **85–90% in DLL, 70–80% in shootouts**; taps must be **gentle and quick**; always top or bottom corner |
| **C-spam escalation** | diagonal header → 3→4→5 at the back → 4–5 vertical lines, 4-1-2-1-2 / 5-2-1-2 negates ~95% |
| **Long shots** | >75% accuracy with correct power |
| **Never push defenders forward** | use a DM, zonal defending, block shots, press C for the keeper, switch tactics constantly |

---

### S8 — Cultivation

- **100% club value ≈ 23 players fully maxed.** [EV-437, C2]
- **Fan Approval: 75% = 500 XP, 100% = 2,000 XP.** **⚠️ The mechanics are a DOCUMENTED NEGATIVE (ckpt-126, EV-457):** a dedicated two-search sweep found **no fan-approval system in any documented DLS26 source** — only crowd-graphics settings, fans-not-celebrating bugs, the Fan Favourite achievement and the Fanzone. **No plan may depend on raising Fan Approval**; treat the percentage as a *readout* of total squad development (100% club value needs every player maxed, ~23 men) and max the squad as the strategy. [EV-437, C2 / EV-457, C2]
- **42 achievements × 500 XP.** [EV-437, C2]
- **Dream Points:** ~2,800/day, ~200,000 total; **career 140 / DLL + Draft 185**; 5-goal cap. [EV-437, C2]
- **Prize Ladder: 90 days**, first special player at **~50,000 DP** ≈ **300–324 matches**. [EV-437, C2]
- **Special coaches are the ONLY choose-your-stat coaches** — 2 randomised options, one fitness one technical: Common 63g/2pts · Rare 168g/6pts · Legendary 280g/12pts = **23.3 gems/point**. [EV-439, C2]
- **Maxing a special player ≈ 6–7 Legendary Special Coaches ≈ 2,000–2,100 gems.** **C-020 RESOLVED** [EV-453, C3]
- **The Legendary Scout trick:** one Legendary Special Coach reveals the next 4 upgradable stats and **can be cancelled without consumption**; clear unwanted stats legendary → rare → common. [EV-439, C2]

### S9 — Maintenance (the goal)

Hold **Tier 1 Champion in your own region** across consecutive seasons against 10M+ XP opponents. [EV-437, C2]

---

## 3. The parallel layer (runs in every state)

### 3.1 Gem income — the full season ledger [EV-443, C3]

| Source | Gems |
|---|---|
| Dream League Live (Progression Bank) | ~6,000 |
| Progression Bank | 1,640 |
| DLL leaderboard (most DLL XP) | 100 |
| DLL challenges | 180 |
| Season Pass ladder (20+25+10+30+40+125+50) | 300 |
| Daily + weekly challenges | 897 |
| **Clans** (25 + 150 at 10M CP + 100 in-clan #1) | **275** |
| DP Points Ladder | 215 |

Hard thresholds: **DLL pays gems only with ≥14 points**; the final DP ladder gem reward needs **~145,000 DP**.

### 3.2 Clans [EV-437, EV-443, C2/C3]

- Clan season = **10 days**. Minimum **50 members**.
- Personal cap **350,000 CP ≈ 100 wins**; realistic season total **13–15M CP**.
- Ladder pays up to **150 gems at 10M CP**.
- Elite clans demand **350K+ every season or removal**; leaders kick sub-20k first-hour contributors. **Read the clan's requirements before joining, not after.**
- **The 350k cap's semantics** [EV-478, C2]: it caps your contribution to the **clan's total**. Beyond it, points count only toward your **personal in-clan ranking** and the top-contributor reward — *"it won't help your clan's total points."* After 350k, clan points are a by-product, never a goal.
- **Clan-internal matches pay clan points** [EV-478, C2] — playing members of your own clan is a legitimate source alongside matches, challenges and Season Pass tiers.
- **The vice-captain is appointed by the leader** [EV-478, C2]; the leader is the **sole admin** and can remove members.
- **Choosing a clan is competitive, not social**: an active clan supplies *"opponents at your level"* [EV-478, C2]. Competitive clans screen for minimum wins in a time window, activity and no inactivity.
- Find it on the **home-screen Clans tab** or the **top-right profile menu**; creation lets you set badge, name, **country**, **minimum team rank** and **open / closed / invite-only** [EV-478, C2]. Entry requirements hide a clan from search, but **an invite code still bypasses them** [EV-456, C1].

### 3.3 Season Pass and Progression Bank [EV-437, C2]

- **400 SP total, 40 SP/day**, 10-day season. Free track pays **1,095 coins + an Epic agent**.
- **Progression Bank is 10 days** — it only pays if you keep playing daily. Missing days loses the accumulated reward.

### 3.4 Cups

**The Career cup ladder** [EV-478, C2] — win the **Legendary Division** → **International Cup** (national teams: England, Sweden, Portugal, Argentina) → **Allstar Cup** (continental all-stars) → **Diamond Cup** (*"the final cup of the game"*, Elite/Legendary). Losing in the International Cup **returns you to the Legendary Division**, and every cup eliminates on a concession.

**The World Tournament** [EV-478, C2] is the **new international-football event type** from Summer Spotlight (v13.330, 10 Jun 2026) — *not* the Career International Cup. It carries the summer's **World Cup Heroes** (1 Jul), **World Cup Challenge** (30 Jun) and **World Cup Winners** (21 Jul) events. **Enter it only while it is live; do not restructure the plan around it.**

**The Prize Ladder's Classic roster is themed and rotates** — the current cycle is the **Italian League Classics: Trezeguet, Batistuta, Crespo, Desailly** [EV-478, C2 — official]. **Special cards have unlimited accommodation** [EV-478, C1] and never count against the 64-player cap.

- **GCC:** online, **128 teams / 32 groups of 4** → R64, ~7 rounds, **10 gems/round + ~25 to win**. **Difficulty scales with DIVISION, not club stars** — you cannot out-star it. [EV-437, C2]
- **Diamond Cup:** ~32 teams. [EV-437, C2]
- **Scenarios:** 50 coins daily, 4 tiers, offline, and **the hardest content in the game**. [EV-445, C2]

### 3.5 Dream Draft [EV-440, C3]

Draft **18 players** from 75+ options per position; **≥1 Star Player mandatory**; up to **7 rounds**; limited formations; CPU opponents; **gems only — players are NOT kept**; 185 DP ceiling; entry ~40 gems or 500 coins, win pays 50 gems; runs **every ~2 weeks**.

**Verdict: worth entering only when the entry is free.** It is a gem engine, not a squad builder.

### 3.6 Transfer-market operating rules [EV-479, C2]

- **The market's filters include CONTRACT LENGTH** — the search axes are position, rating and contract length, so contract length is searchable, not just displayed.
- **Buying and selling churns the market** and raises the chance of higher-rated players appearing [C2]. The match-refresh rule in §3.1 remains the better-evidenced rule: **play matches to refresh, churn when actively hunting.**
- **Market quality scales with the squad** — as team rating improves, higher-quality players appear more often.
- **Starting out:** new accounts begin at **50–60 OVR**; DLS25 progress carries over, including the squad and Academy Division status.
- **Free transfers** are usually low-stat players or ones you released; paid general transfers run **10 to about 900 coins**.
- **Coaches can be hired by RELEASING PLAYERS from your squad** — a gem-free coach route. Four categories (Technical, Fitness, Goalkeeping, Special) × three tiers (Common, Rare, Legendary); Common boosts one random stat, Legendary is largest with the highest breakthrough chance.

**⚠️ DLS26 HAS NO DOCUMENTED SQUAD-CHEMISTRY SYSTEM** [EV-479, C2 — documented negative]. Every explained chemistry model on the open web is EA FC / FIFA; no DLS source documents a threshold, UI, link rule or attribute effect. **Do not spend gems or squad slots chasing one.**

### 3.7 The control model and the complete skill catalogue [EV-480, C2]

- **The three action buttons are context-dependent:** in possession they pass, shoot and cross; out of possession the same three become **press, tackle, change-player**. The layout is customisable and **the shooting assistant can be disabled**.
- **Kicks:** Low Kick = low/short precise passes · Hard Kick = shots and long through balls · Lofted Kick = long passes and chips.
- **Skills:** Rainbow Flick = swipe **UP** (Control > 80) · Feint = swipe **L/R** · Roulette = swipe **DOWN** (Control > 70) · Bicycle/Scorpion Kick = double-tap **in the air** · Heading = double-tap **under the ball** · Rabona = Rainbow Flick then **B/C** · **Close Control = tap and hold** in empty space while in possession (official: *"more controlled dribbling"*) · **Knock Ahead = tap** while in possession · **Secondary Press = tap and hold** while defending.
- **Skill moves are gated by Control** — below the threshold the player *"will just lose the ball."*
- **Learn them at My Club → Training → Free Practice**; the **Advanced Tutorial** teaching every skill is inside the training mode. Six modules: Free Training, Free Kick, Left Corner, Right Corner, Penalty, Penalty Save.
- **Technique:** combine the swipe with a joystick direction change; skill moves pay most **in a 1v1 with the keeper** (a speed boost plus distance from recovering defenders).
- **⚠️ DLS's skill set is deliberately smaller than FIFA's.** No elastico, no trivela. Learn these ten and stop looking.

### 3.8 The stadium's design surface [EV-480, C2]

- **Seven named pitch patterns:** Horizontal stripe, Vertical stripe, Check, Diagonal A, Diagonal B, Diamond, Circles — **all cosmetic**.
- **Eight named sectors:** North, North East, East, South East, South, South West, West, North West Stand. **Seat colour follows the home kit.**
- Advertising boards appear in every sector except the corners and the players' entrance; **some structures carry zero seats**.
- **Auto Build Capacity** sets an exact seat target (ceiling 80,000 of 90,456 max).
- **Build order:** *"Don't build the roofs, just until you reach max spectators"*; upgrade **one stand at a time** — levelling every stand together costs more.
- **Negatives:** no controller support on mobile; no gem-based injury healing (*"wait it out or use medical staff"*).

### 3.9 Economy mechanics [EV-481, C1/C2/C3]

- **OFFICIAL gem sources** [C1]: league objectives · tournaments · Season Pass · Prize Ladder · Dream League Live. FTG adds *"(please seek the bill payer's permission)"* — **if someone else pays for the account, ask before buying.**
- **⚠️ TWO CURRENCIES ONLY: coins and gems** [C1/C2]. "Diamonds" appears only on scam sites and one discredited guide (the same one rejected in C-012); "crystals" appears once and is unverified. **Do not plan on a third currency.** (C-028)
- **Three objectives arrive before every match** and each pays coins — read them before kick-off.
- **Commercial is the kit-and-logo facility**: a 5-star upgrade earns kit discounts and logo discounts, not just coins.
- **Bank Common coaches**; do not waste gems on agents or coins on scouts. Training pays back after ~20 uses.
- **Dream Draft costs coins** and returns gems plus Dream Points — never run it for coins.

### 3.10 The offside trap — unresolved, test in Exhibition [EV-481, C3]

- **Side A (DLS24, Dec 2023):** team press moves the defensive line up to force an offside; switch to a wing-back so it rises with the line.
- **Side B (DLS26, Aug 2026):** *"where are the offside traps, high lines, attacking shape...?"* and *"defenders refuse to hold their line."*
- **Status: OPEN (C-029), version-drift likely.** Until tested, **defend with a controlled line, not a high one** — the §3.1 rule "never push defenders forward" already assumes the trap is unreliable.
- **New control detail:** double-tap clears the ball while defending; **C** is the player-switch button.

---

## 4. Dead ends — do not retry

| Trap | Why |
|---|---|
| Chemistry / Fluid Formations systems | **Fabricated** — content farm, also publishes fake testimonials [EV-413] |
| Save-tampering for coins/gems | Ineffective when cloud-linked [EV-439] |
| Infinite coins/gems, mods, generators | **Do not exist / account blocking / scam** [OFFICIAL FTG] |
| Youth Academy | **Does not exist** in DLS26 [GS-023] |
| Free transfers | Ended at DLS2016h [EV-442] |
| Buying legendary players early | **R-0.2 — kills the coach-farming loop** |
| Manager-name refresh trick | **Speculative** [EV-442, C4] |
| Weather effects | **UNCONFIRMED** |
| "Five facilities" ≠ seven | Five official facilities [GS-023] |
| Out-gunning GCC with club stars | **Difficulty scales with division** [EV-437] |

---

## 5. The one-page routine

**Daily (≈45–60 min):**
1. Season Pass login (+40 SP) and the full daily challenge set (5–11 gems)
2. Daily Scenario (50 coins) — budget real time, it is the hardest content in the game
3. 3–5 DLL matches **at tier 10 or above**
4. Buy 3–5 players under 210 coins → release → coaches
5. One 8-hour ad cycle (up to 600 coins)
6. **Two free-kick or corner attempts in Exhibition** — the free training ground, and the highest-percentage scoring route in the game

**Weekly:** full weekly challenge set · 1 reroll budget check · clan contribution toward 350k · Progression Bank progress check.

**Every 90 days:** Prize Ladder reset — target the first special player at ~50,000 DP.

---

## 6. Patch Response triggers

The game is volatile; these are the only events that justify breaking the routine:

| Trigger | Response |
|---|---|
| New build ships | Re-verify: build number, version-to-content mapping, and any coach/breakthrough/facility figures |
| New event announced | Read the **official** notes first; ignore mirror dates (C-023) |
| New Special Player collection | Re-price against the 2,100-gem special-player budget |
| DLS27 announced | Expect the same package and seasonal-upgrade pattern (B-002) |
| Any "unlimited coins/gems" offer | **Scam. Ignore.** |

---

## 7. Audit

### 7.1 What this document is grounded in

| Check | Result |
|---|---|
| Every rule carries an EV or claim reference | **Yes** — 34 distinct evidence records cited |
| Every numeric figure traces to a claim | **Yes** |
| Unverified claims marked | **Yes — 1 ([UNVERIFIED] on the manager-name trick)** |
| Rejected sources used as authority | **No** |
| Terminology matches the official glossary | **Yes** (DLL, OVR, GK, XI, Special Players, Season Points, Dream Points, Form Boost, Progress Bank, My Club) |

### 7.2 Known weaknesses (stated, not hidden)

1. **The open-gaps list has moved substantially and the old note here was wrong on both the list and the method.** The old text claimed five numeric tables remained open and that they "can only be closed by APK datamining (Step 2, postponed)" — but **three of those five were closed by OFFICIAL SUPPORT ARTICLES**, not datamining. Current status: **Form Boost per-level match counts** — closed as a documented negative (official wording gives only "a set number of matches, minimum one"; assume ONE match) · **Medical percentages above L1** — L1 double-corroborated, L2–L5 unpublished · **Fan Approval mechanics** — closed as a documented negative (no such system exists) · **post-DLS25 coach breakthrough %** — still open, the DLS20 5/10/20 baseline confirmed · **Fanzone per-level gem costs** — still open (one mod-site source says five levels) · **plus** the Medical/Commercial level counts (the 75×N pattern is inferred), the exact Season Pass per-tier contents, the LIVE rank names above Veteran, the identity of the 12th Man winner, and the DLL-unlock Career-match count (C-025). **Web research is not exhausted — the FTG support portal is a live route and has produced the last several official findings.**
2. **Formation meta is genuinely unsettled** (C-014) — the rule is "pick one and learn it deeply", which is advice about process, not a claim about a best formation.
3. **Corner footedness is contested** (C-022) — the rule instructs testing both in training rather than asserting one.
4. **Market refresh cadence** (C-021) — "refreshes after every match" is the community consensus; a minority claims every 7 hours. The rule set uses the per-match model because it is the more conservative assumption for the farming loop.
5. **The special-player max cost** (C-020) — planned at 2,100 gems from the coach model, not from a datamine.
6. **~300 matches to a dream squad** and **~16 days to Tier 1** are single-source community figures, useful for planning but not guarantees.
7. **The gacha probability mechanic** (EV-450) is a well-corroborated community report with a plausible mechanism behind it, but the exact 100%-odds claim and the 275,000-coin cost are unverified. Treat the *direction* — fewer legendaries in the pool means better odds — as reliable and the numbers as planning figures.
7. **The tier-camping gem rate** (~35–43/hour) is a single well-detailed community report. The *method* is corroborated by several posters describing the same survival-not-promotion approach; the *exact numbers* are not.
8. **The maxed-squad handicap (C-024)** is Community Consensus with an official mechanism behind it, not a datamined fact. The direction is reliable; the threshold (how much coaching is too much) is unknown.

### 7.3 Audit verdict

**PASS with stated limits.** The rule set is internally consistent, fully referenced, and safe to execute. Rules R-7.1 to R-7.3 were added at ckpt-109, rules 6.9 to 6.12 at ckpt-112, and rules R-5.1 and R-5.2 at ckpt-119; the gacha lever (6.9) is the single highest-value collection rule and the ladder feasibility rule (R-5.1) the single most important planning rule. The open gaps are all *numeric refinements* that change an optimum at the margin, not the direction of the plan. None of them blocks starting.

---

---

## Economy and competition reference [EV-462/463]

**THE OFFICIAL COIN LIST** [EV-462, **C1**]: coins come from winning matches, drawing matches, clean sheets, scoring goals, stadium bonuses, season objectives, Season Pass rewards, Prize Ladder rewards, final league positions, cup wins and video clips — **DLL wins are not on the list**. **Coins = Career and cups. Gems = DLL.** Free coins come from watching short video clips, subject to availability.

**OFFICIAL LEADERBOARD CADENCE** [EV-462, **C1**]: leaderboards compare DLL performance, *"reset at regular intervals (from 3-30 days)"* and pay by final position — the 10-day Progression Bank season sits inside that range.

**GLOBAL CHALLENGE CUP** [EV-463, C2]: **128 teams, 4 per group home-and-away, top 2 qualify, then a straight knockout** (R32 → R16 → QF → SF → final) with extra time. Available in every division from Academy up; a loss after qualifying eliminates you. A coin-and-trophy surface only — never let it displace the DLL climb.

**THE 12TH MAN** [EV-463, C2]: the community vote concluded and the extra superstar **was added in v13.120 (25 Mar 2026)**. FTG never names the player, so treat the mechanic as closed and the identity as unknown.

**COMMERCIAL FACILITY — spend here LAST** [EV-465, C3]: a **maxed** Commercial facility gives only about **6–20 extra coins per game**, so at 1,125 gems to max the payback runs to hundreds of matches. Three mutually exclusive curves are on record (13%/21%, 10%-at-L5, and sportsdunia's rejected 2/4/6/8/10%), but the magnitude is what matters. **Community priority: Training and Accommodation first, Commercial last.** The one dissenting voice argues the bonus rises to 30–50 coins per game in higher divisions.

**ACHIEVEMENT COUNT (corrected, ckpt-130)** [EV-466, C2]: DLS26 is **40 achievements / 20,000 XP on Android** and **63 achievements / 13,483 EXP on iOS**. The 98,000 XP figure belongs to a Classic-era listing and must not be quoted as a DLS26 number. Every Android achievement is worth **500 XP**.

---

*End of operational rules. Authority: `kb/claims.jsonl` (1,663 claims) + `docs/continuity/a7e23a6b/evidence/index.jsonl` (377 records) at ckpt-137.*
