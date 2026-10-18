# DLS26 OMEGA — Strategy Masterplan: Path to #1

**Compiled:** 2026-10-18 · **KB basis:** ckpt-118 (`94bb636`) — 1,479 claims / 355 evidence records
**Branch:** `arena/b5d5681d-dls26-omega` · **Confidence ladder:** 1 = Confirmed (official/FTG or multi-source) · 2 = High · 3 = Community Consensus · 4 = Speculative · 5 = Disputed
**Scope:** Dream League Soccer 2026 (FTG), v13.430 (16 Sep 2026), FIFPRO 4,000+ licensed players.

---

## 0. What "#1" actually means — and the one decision that defines the whole plan

The mission target is **#1 in Dream League Live**. Two facts fix the definition:

| Fact | Evidence | Confidence |
|---|---|---|
| The DLL leaderboard is **by region** and is based on **performances, not team rating**. Worldwide ranking was only directly visible via the iOS Game Center leaderboard in DLS19. | EV-427 / r/DLS 1e42njg | 2 |
| The DLL tier ladder is **numeric 20 (bottom) → 1 (top)**, with "Tier 1 Champion" the ceiling. | EV-431/432 / r/DLS 1qz14ir | 3 |

> **DECISION:** The operational target is **Tier 1 Champion in the player's own region** (Asia/Dhaka → the SEA/Asia pool), sustained across multiple seasons. A true global #1 surface is not exposed in DLS26; treating "global #1" as the goal would be chasing a metric the game does not publish.

**A third fact, discovered later in the sweep, confirms this from the matchmaking side** [EV-451, C2]: your Live **seed** is set by your **region and the time you started your account**. Seeds divide the player base into small packets so the matchmaker never scans the world — which is why accounts created years apart still meet in Live, and why your realistic competition is always your own regional pool.

This matters because it changes the optimisation target: **the leaderboard rewards performance (XP and results), not squad value.** A world-record run reached Tier 1 Champion with a *mostly common/rare team* — 16 days, 12 games, 110 wins, 10 losses, 1 draw, 145,296 XP, starting deliberately from tier 20 [EV-432, C3].

---

## 1. The ladder and the clock

### 1.1 Dream League Live tiers (the ranked surface)

| Tier band | What happens there | Evidence |
|---|---|---|
| **20 → 11** | Bottom half. Below tier 10, **Live pays no gems** — the grind must happen at tier 10 or above. | r/DLS 176ntor, C3 |
| **10** | The **gem-farming floor** and the deliberate relegation target: players drop to tier 10 to farm gems and win events as a break, then re-climb. | r/DLS 1ghbsed, C3 |
| **7 → 5** | First wall. Players who go undefeated in tier 6 get relegated in tier 5. Tier 3+ was *easier* in DLS23 because lower points were required. | r/DLS 108xox7, C3 |
| **3** | **The wall of fully maxed teams.** The record-holder "scraped through Tier 3 against countless fully maxed teams, clutching a win on the final game to just get promotion." | EV-432, C3 |
| **2** | Opponents commonly hold **10M+ online XP**. The record-holder went undefeated here. | EV-432, C3 |
| **1** | **Tier 1 Champion.** Reachable in ~16 days of full-time play with a common squad. | EV-431/432, C3 |

**Two tactics from the record run that cost nothing:**
1. **Promote at every tier.** "Not once did I not get promoted to the next tier (crucial to saving XP)." Every season spent in a tier you have already cleared is wasted XP.
2. **Restart from the bottom deliberately.** The run began at tier 20 with a fully common team — low tiers are cheap XP, not a punishment.

> ### THE GEM ENGINE — tier camping [EV-448, C2/C3]
>
> The record run optimised for **speed to Tier 1**. If your priority is **gems per hour**, the optimal tactic is the opposite:
>
> **Camp between Tier 5 and Tier 2** (Tier 1 cannot be camped — it is the ceiling) and **aim for SURVIVAL, NOT PROMOTION.** Win only **4–5 matches** (12–15 points), then **quit the rest** — and *losing en route is even better*, because it keeps you in the camping tier instead of promoting you into a harder one.
>
> | Metric | Value |
> |---|---|
> | Matches | ~48 |
> | Time | 4 – 4.8 hours |
> | Gems from DLL | ~150 |
> | 4-hour minimum | 160 – 208 gems |
> | **Rate** | **~35–43 gems/hour** |
>
> The full daily challenge set pays **5–11 gems per day**. Camping is roughly **30× more efficient per hour.** Do **not** forfeit while camping — forfeiting may cost you the maximum gems.
>
> **These two tactics are not in conflict — they answer different questions.** *Promote at every tier* is the fastest route to Tier 1. *Tier camping* is the cheapest route to gems. Decide which you are optimising before each block of matches; never mix them in one session, because camping punishes promotion and climbing punishes deliberate loss. Band-by-band detail: **`docs/dll_tier_playbook.md`**.

> ### THE COUNTER-INTUITIVE SQUAD RULE (C-024) [EV-447, C1 / EV-448, C2]
>
> **Maxing your squad can make you worse in Live.** A Tier 1 player: *"maxxed squads perform TERRIBLY in high tiers due to handicap… just try not to coach your players anymore."* The **official** FTG matchmaking article names **team strength** as an explicit matching input, and players with maxxed squads report being stuck at tiers 4 and 10.
>
> **Run two separate optimisation targets:** *competitive but NOT maxed* for DLL Tier 1; *maxed* for club value and the Prize Ladder. The record Tier 1 run used a **mostly common/rare squad** [EV-432] — maxing is not a prerequisite for the top tier.

### 1.2 Career Mode (the economy and the rating engine)

Eight divisions: **Academy → Amateur → Division 4 → Division 3 → Division 2 → Division 1 → Elite → Legendary** [EV-423, C2].

- **Promotion:** top 2 direct; 3rd–6th enter a playoff; a **stadium class gate** also applies [EV-423, C2].
- **Cups follow your current division** — Bronze (Academy/Amateur), Silver (Div 4/3), Gold (Div 2/1), Diamond (Elite/Legendary) [EV-431, C3]. **Consequence:** to win the Gold Cup you must *drop* to Division 1; once promoted, Gold becomes Diamond.
- **Relegation is not a disaster:** dropping divisions reduces coin/gem awards but **does not affect the transfer market** [EV-431, C3].
- A **70-rated team can win the Legendary Division**, though it is very hard [EV-432, C3].

---

## 2. Phase plan

### PHASE 0 — Setup (Day 0, one sitting)

1. **Captain selection.** Current build offers ~80 captain choices plus *Create Your Own Captain* [EV-427, C2]. The DLS21-era build showed 9 random Legendary Cards [EV-427, C2] — do not follow old guides that assume 9.
2. **Controls.** Preset **A = Hard Kick/Shoot, B = Low Kick/Pass, C = Lofted/Chip/Curl/Cross** [prior waves, C2]. Set pieces require the joystick; the B auto-press needs stick input [C2].
3. **Camera:** Tele, H75 / Z35 [C3]. **Graphics:** Medium / 60 FPS / Semi-auto [C3].
4. **Commentary:** English (Gary Bloom) is the default; DLS26 added Turkish and Arabic [EV-427, C1].
5. **Create the account on one platform only.** Google/Apple cloud is same-platform; cross-platform transfer uses a code; DLS25 data does **not** carry over; Facebook Login was removed [prior waves, C1].
6. **Join a clan immediately** (rank 20 unlocks full clan features; minimum 50 members; 150 gems to create) [EV-429, C2/C3]. Clan points are earned from regular matches, Live events, Dream Draft, real-life scenarios and Season Pass tiers [EV-429, C2].

### PHASE 1 — First 48 hours (economy bootstrap)

**Priority order for facilities** (the community consensus and the income logic agree):

| Order | Facility | Why | Numbers |
|---|---|---|---|
| 1 | **Stadium** | Home-match coin bonus is the only compounding income source | 1,125 gems per facility; **5,625 gems total** for all five; optimal build **92,632 capacity → 52 coins per home match** for ~10,000 coins [C2/C3] |
| 2 | **Commercial** | +13% coins at L2, **+21% at L3**; L3 also removes stadium rust | First tier 75 gems [C2/C3] |
| 3 | **Training** | Coach discounts **and** Form Boost duration **and** formations | See full ladder below |
| 4 | **Medical** | Injury reduction and cheaper recovery | L1 gives −5% injury / −10% heal cost; L2–L5 **never published** [C2] |
| 5 | **Fanzone** (new in Summer Spotlight) | **Clan bonuses + stadium discounts** | Per-level costs **never published** [EV-428/App Store, C1 on function, C5 on cost] |

**Full Training ladder with prices** [EV-437, C2]:

| Level | Cost | Discount | Bonus |
|---|---|---|---|
| L1 | 75 gems | 5% off coaches | — |
| L2 | 150 gems | 10% | + a group of formations |
| L3 | 225 gems | 15% | + a group of formations |
| **L4** | **300 gems** | — | **LEGENDARY COACHES DROP BELOW 200 GEMS EACH — the coach-farming unlock** |
| L5 | 375 gems | — | Full discount ladder |

Each Training upgrade unlocks **up to three new formations** (~15 by Level 2). Community advice: **stop at Level 2** unless you intend to spend 3,000+ gems on legendary coaches [EV-437, C2].

> **DLS26 CHANGE:** the first facility tier now costs **375 COINS**, not 75 gems as in every prior version [EV-411, C2]. This is the single biggest early-game change — spend coins, save gems.

**Gem rule (hard):** gems go to **agents and facilities**, never to Form Boosts on low-rated players. The Form Boost baseline is 5g/+1, 8g/+2, 10g/+3 for **one match** [EV-428, C2] — that is a terrible rate at any stage.

**Free-to-play income stack (do all of these daily):**
- Daily challenges: **5–11 gems/day** [EV-433, C3]
- Scenarios: **50 coins daily**; 75–100 coins per 8-hour cycle [C2/C3]
- Ads: 30 coins per ad, up to ~600 coins in 15 minutes [EV-426, C3]
- Season Pass: **400 SP**, **40 SP/day login**, 10-day season; the **free track alone gives 1,095 coins + an Epic agent** [EV-399, C2]
- Progression Bank: accumulates coins and gems from DLL XP over a **10-day season**, paid out in full at season end [EV-431, C2]
- Weekly DLL leaderboard: gems for **placement** *and* gems for playing a set number of DLL matches that week [EV-431, C2]

### PHASE 2 — Weeks 1–3: the ranked climb

1. **Play Career first to build the coin engine**, then switch to Live.
2. **In Live, always play at tier 10 or above** — below that you earn no gems [EV-432, C3].
3. **Climb without lingering.** Promote every tier; never voluntarily sit in a tier you can win.
4. **If you hit the tier 5–6 wall or tilt, drop to tier 10 and farm gems/events**, then re-climb — tier 7→1 took a documented player **4 days** [EV-432, C3].
5. **Target Tier 1 within ~16 days** of concentrated play [EV-431, C3]. After that, the goal becomes *holding* Tier 1, which is where the 10M+ XP opponents live.

### PHASE 3 — Squad building (the long game, runs in parallel)

**The transfer market is gated by your own rating — this is the counter-intuitive core:**
- Legendary players **will not appear** until you buy lower-rated players, even with a maxed stadium and top division [EV-431, C3].
- Gold-carded (80+) players become regular above **80 team rating**; even a **94.4-rated team** may not see 85–86 players for a long time [EV-433, C3].
- **Therefore: buy and sell constantly.** Regular buying/selling refreshes the market and signals activity, increasing the chance of higher-rated players appearing [C2/C3].
- Dropping divisions means you see *more lower-rated* legendary players — useful when filling the bench cheaply [C3].

**Best players per position** [EV-426, C3]: GK Alisson/Courtois · LB Robertson/Theo Hernández (Grimaldo is marked LWB) · CB Rudiger/Saliba (83) and Van Dijk/Dias (84) · RB Hakimi/Trent · DM Rodri · AM De Bruyne · CM Valverde · LW Vinícius Jr.

**Base rating ceiling is 86** (Dembélé/Mbappé/Kane/Haaland cluster) — special cards sit above it [EV-426, C3, conflict noted].

**The counter-intuitive early rule** [EV-441, C2]: **do NOT buy legendary players early.** Buying them raises your team rating, and a higher rating makes the *cheap* players disappear from the market — which kills the coach-farming loop that actually builds your squad. Buy one or two fast common or rare players to win games, and only start buy-sell cycling once the stadium is maxed. Also pick the **best attacker as captain**: it boosts team rating, which improves who appears in the market.

### PHASE 3.1 — Transfer market mechanics [EV-442, C2/C3]

This is the most operationally important layer in the game, and almost every guide gets it wrong.

**The refresh rule:** the Live Transfer Market refreshes **after every match you play**.

**What does NOT refresh it** — and this is the key insight:

| Action | Earns coins? | Refreshes the market? |
|---|---|---|
| Play a match | Yes | **Yes** |
| **Forfeit a Career match** | Yes | **No** |
| **Play scenarios** | Yes (50/day) | **No** |
| **Exhibition matches** | Yes | **No** |
| **Watch free ads** | Yes (30 each) | **No** |
| **Dream Draft** | — | **No** |

> **Why this matters:** you can farm coins for a specific target player **without burning the market slot they are sitting in.** This is the correct answer to "I can't afford the player I want."

**Fastest refresh:** quit a **LIVE** match at half-time (or play the first half and forfeit).

**Lock Player — the paid answer to waiting:** spend **20 or 40 gems** to lock any player on the live transfer market for **24 hours**. They survive the next match refresh, a small lock sign appears on their card, and they vanish as normal when the period ends.

**Other rules that catch people out:**
- **Released players do reappear** — after a grace period during which you can buy them back from the release area. But **collection pieces never come back**, and rare/common cards may take a long wait.
- **No duplicates:** you cannot buy a player you already own. To get a new version of a card you must first sell the one you have.
- **Buy the highest-rated player at each refresh** — it raises team strength and attracts better players.
- **Legendary players** appear individually or as **Top Picks**, and land in the **~1,500–2,800 coin** band once your rating attracts interest.
- **Scouts:** Common 75 coins, Legendary 500 coins. The Common's 5% legendary chance is good early value.
- **Release yields coaches, not coins** — this *is* the coach-farming loop.
- **Ignore the "rename your manager" trick.** One thread claims renaming your manager and nationality to a target player's makes them appear in 20–40 matches; the poster themselves states some say it works and others that it doesn't. **Speculative (C4) — do not plan around it.**

### PHASE 3.2 — Dream Draft (a gem engine, not a squad builder) [EV-440, C3]

| Mechanic | Detail |
|---|---|
| Draft size | **18 players**, every option **75+ rated** |
| Requirement | **At least one Star Player is mandatory** |
| Structure | Limited-time tournament, **up to 7 rounds max**, a different opponent each round |
| Formations | **Limited** selection |
| Opponents | **CPU** in the standard version (online variants exist) |
| DP | **185 max** for a clean sheet plus 5+ goals — easier than Live because of the CPU |
| Rewards | Gems for winning the **semi-finals and finals**, plus leaderboard medals/gems/coins for 1st, 2nd and 3rd |
| **The catch** | **The players are NOT kept.** Gems only — never treat this as squad building |
| Entry | Paid in DLS24, free in DLS25, may be paywalled again; ~40 gems or 500 coins, win pays 50 |
| Cadence | Roughly **every two weeks** |

**Verdict:** worth entering when free, because it is the cheapest 185 DP in the game and it feeds the Prize Ladder. Do not pay for it — the community calls the opposition scripted and notes that losing yields nothing.

### PHASE 4 — Player development (the actual rating engine)

**How coaches really work** [EV-433, C2, plus OFFICIAL FTG confirmation that the recipient is random — EV-428, C1]:

| Rule | Detail |
|---|---|
| Max rating | **Base overall + 10** (very rarely +11) |
| Two outfield pools | **Fitness = SPE, ACC, STA, STR** · **Tech = CON, PAS, SHO, TAC** |
| Double RNG | Both the *player* and the *stat* are random |
| Pool narrowing | **Release players you don't want to train** — fewer eligible players raises the odds on the ones you do |
| Re-train | After a lucky hit, **re-train costs gems** to add more points |
| Special Coaches | **Bypass the RNG** and allow targeted upgrades — the sell-to-15 meta |
| Categories | Technical, Fitness, Goalkeeping, Special × Common/Rare/Legendary |

**Coach farming (the coin engine's output):**
- Buy players **under 180–210 coins** → release → **Common coaches**
- Buy **80-rated defenders** (cheapest legendary class: Attacker > Midfielder > Defender) → release → **Rare coaches**
- A full max costs roughly **32,000 coins with Commons** (~400 coins × ~80 coaches; each player has ~80 upgrade points) or **~30,000 coins with Rares** (~1,500 coins × ~20 coaches); 80-rated defenders are available from ~1,460 coins [EV-433, C3]

**Ratios:** **7:3 fitness-to-tech** for non-maxed teams; **90:10** when chasing speed first [EV-433, C3].

### 4.1 The complete coach model [EV-439, C2]

**Point delivery** — this is the table that decides everything:

| Coach | Effect | Gem cost (maxed Training) | Points | Gems/point |
|---|---|---|---|---|
| **Common** | 1 random stat **+1** | 17 | +1 | 17 |
| **Rare** | 2 random stats **+2 each** | 52 | +8 | 6.5 |
| **Legendary (fitness)** | 3 random stats **+3 each** | 157 | **+27** | **5.8** |
| **Legendary (Special)** | you **choose** the stat | 280 | +12 | 26.25 |

- **Goalkeeping coaches touch only GKR and GKH**: Legendary +3 to both, Rare +2 to one, Common +1 to one. **Use a Legendary GK coach only if GKR > GKH** — this independently confirms the GKR ≥ GKH rule.
- **Rare coaches in coins:** +8 points for **1,535 coins = 192 coins per point** — the exact maths behind "buy 80-rated defenders at 1,535 coins".
- **Legendary vs Rare trade-off:** for 225 gems, Legendary gives +27 points and Rares give +24. Legendary wins on raw points; **Rare wins on controllability**.
- **Capacity:** each player has ~**80–81 upgrade points** (~90 Common coaches to max), each OVR point ≈ **8 stat points**, and **STR and CON count ×2** for most positions except wingers.
- **Build time:** a 23-man squad took one player **about half a year**.
- **Breakthrough:** 5% / 10% / 20% (Common/Rare/Legendary, DLS20 baseline). Rarity affects **only** the breakthrough chance, never the cap.

**Special Coaches — the only coaches where you choose the stat:**

| | Price | Points | Gems/point |
|---|---|---|---|
| Common | 63 gems | 2 | 31.5 |
| Rare | 168 gems | 6 | 28 |
| Legendary | 280 gems | 12 | **23.33** |

The game offers **2 randomised options (one fitness, one technical)** and you pick one.

**Two techniques worth memorising:**

1. **The Legendary Scout trick** — keep at least one Legendary Special coach. It **reveals the next four upgradable stats**, and you can **cancel and use a different coach without consuming it**. This turns your most expensive coach into a free scouting tool.
2. **The clearing method** — open with a Legendary Special coach and inspect the first three stats. If all are desirable, follow with Rares. If unwanted stats appear (tackling for strikers, strength for wingers), use **Common** Special coaches to clear them, because commons add fewer points — then switch back to Rare/Legendary and repeat. Simpler variant: *always* use a Common if either offered stat is wrong.

**Cost to max one special player:** 6–7 Legendary Special Coaches ≈ **2,000–2,100 gems** (15 Rares = 2,520). **C-020 RESOLVED at ckpt-118** — a player states plainly *"each special player costs around 2000 gems to max out"*, corroborating the coach model. The cancel-without-consumption technique saves ~70 gems per coach, **~420 gems per maxed special** [EV-453, C3].

**Where the 12th Man fits:** it is the **community-voted final Dream Star** [EV-438, C1]. FTG publishes the Dream Stars squad from real-world season performances (vote in v13.100/13.110, winner added v13.120 on 25 Mar 2026, Dream Stars 2026 in v13.130), and Dream Stars come from **Dream Star Agents**. FTG has never named the winner, so treat it as an event to watch rather than a card to plan around. Vozinha's "(12th Man)" label in the Cult Heroes datamine is most likely a **card type**, not the vote winner — do not conflate the two.

**To isolate one player:** you need a fully maxed team, or a squad of goalkeepers plus that single outfield player [EV-433, C3].

**Cards go silver → gold → black at 100 OVR**, and **upgraded players appear in the market as silver/gold cards** — an efficient way to buy an already-developed player instead of grinding one [EV-433, C2].

### PHASE 5 — Club value and Fan Approval

- **100% Dream Team/club value requires EVERY player maxed, including bench and reserves — about 23 players** [EV-433, C3; corroborated by EV-424/425]. A starting eleven of 99s with 100% fan approval was still stuck at 58.52%.
- **Fan Approval milestones:** *Mr Popular* at **75%** (500 XP) and *Fan Favourite* at **100%** (2,000 XP in DLS2018 / 1,000 XP in DLS Classic) [EV-433, C2]. **The mechanics that drive the percentage are NOT documented** — this remains an open gap.

### PHASE 6 — Special and Classic players (the 90-day engine)

- **Special Players cannot be bought with coins** — events, challenges and the Prize Ladder only [EV-426, C2].
- **Two routes:** (a) the **Prize Ladder** — first special at **~50,000 DP**, draw is **random**, first icon ~**300–324 games** with boosters, all four WC'98 icons ~**1,370–1,428 games** against a ~200,000 DP ladder; (b) **Legendary Agents** — every use has a chance of a **World Hero** Special Player [EV-426, C1 for the agent route].
- **WC'98 four:** Petit, Šuker, Bergkamp, Batistuta [C2].
- **Dynamic Stars** need Dynamic Star Agents from event draws and Season Passes (3 premium + 2 free) [C3].
- **Cult Heroes** (v13.430, 16 Sep 2026) — 12 players, signed randomly from Cult Hero Agents: **de Gea 85, Aubameyang 85, Dybala 85** (max 95); **Isco, Insigne, Ziyech, Otamendi, David Luiz 84** (max 94); **Blind, Herrera, Shaqiri, Vozinha 83** (max 93) [EV-430, C2].
- **Classic Players:** unlock to sign with **500 coins**, or by completing the game (beating your own team after First Touch United); ratings 85–97 [C2].
- **Prize Ladder cycle = 90 days** and it unlocks coins, gems **and Classic Players** [EV-431, C2].
- **DP economics:** career max **140 DP/match**, DLL+Draft **185 DP**; **5-goal cap**; ~**2,800 DP/day**; ~**200,000 DP** total [prior waves, C2/C3]. Per-match DP is **75–250 depending on performance** [EV-450, C3].
- **THE EFFICIENCY RULE:** a DLL win pays **~115 DP** against a Career win's **~65 DP** — DLL is roughly **77% more DP-efficient per match**. Experienced players complete the Prize Ladder on **DLL alone**, with a few Career matches purely for daily challenges [EV-453, C3].
- **Per-match DP breakdown** [EV-453, C3]: win 115 (DLL) / 65 (Career) · 10 per goal up to 5 (50 max) · clean sheet 10–15 · post-match ad +50 (DLL) / +35 (Career). Non-wins still pay: 45 (DLL draw), 15 (DLL loss), 25 (ad on either).
- **OFFICIAL DP BOOST RULES** [EV-452, **C1**] — two of these change how you should buy:
  - Boosts apply **only** to Career, Dream Draft, Scenario and DLL matches. **They do NOT apply to Exhibition or Friend Matches** — so the free practice ground earns no boosted DP.
  - **Unused boosts carry over to the next Prize Ladder**, and boosts cannot be used on a completed or inactive ladder. **Buy early in a ladder, never late in a dying one.**
- **Boost pricing** [EV-453, C3]: Common 50% / 25 gems / 3 matches · Rare 75% / 35 gems / 5 matches · Legendary 150% / 125 gems / 8 matches.
- **THE FEASIBILITY NUMBER** [EV-453, C3]: reaching **200,000 DP** in the 90-day window needs **at least 15 games a day** — described as *"60% of a career season"* and equivalent to **54 career seasons in 90 days**. All four icons cost about **137 hours** total; the first icon is **300–324 games**. **Plan the ladder around this, not around hope.**
- **Milestones** [EV-453, C3]: first special at **~50,000 DP** and **random**; further milestones at **62,500** and **70,000 DP**; all four specials at **~200,000 DP**. A completed ladder drew Souness → Adams → Andy Cole → Gascoigne, confirming the order is random.
- **Honest caveat on filler** [EV-453, C3]: the ladder's coin and gem rewards are criticised as *"mediocre, unfulfilling, boring and quite frankly useless — FILLER rewards"*, with one player's ladder Legendary Scouts finding no Legendary at all. **The ladder is worth it for the Classic Players, not for the intermediate rewards.**
- **DLL Quests** pay gems for win counts — **5 gems for 5 wins, 175 gems for 175 wins**; DLL events pay **280 coins for 5 wins and +720 for 7** [EV-453, C3].
- **New Classic set** [EV-452, C1]: **Italian League Classics** — Trezeguet, Batistuta, Crespo, Desailly.
- **DP method ranking** [EV-450, C3]: 5-0 Career wins for casual play · **Scenarios if you are skilled** · Live matches if you win 90% online · gems and boosts if paying. Explicit community warning: **do not grind Classic Players at the cost of your enjoyment** — for most maxed teams they are useless, though basic-squad players call Batistuta and Petit uniquely strong.

#### 6.1 The complete card taxonomy [EV-450, C3 / EV-449, C1]

| Card | What it is | How you get it |
|---|---|---|
| **Gold** | Ordinary players. Odds improve as you sign better-rated players. | Market, Agents, Scouts |
| **Orange** | **A maxed gold player — NOT a separate card type** | Coach a gold player to max |
| **Black** | **Classic Players** — DLS's analogue of FIFA Icons. Rated **85–97**. Own tab at the top of the screen. | **Prize Ladder** milestones (62,500–250,000 DP), or 500 coins / completing the game |
| **Purple** | **Dream Stars** — the season's top performers with enhanced attributes; the 12th Man Vote picks the final one | Month-long event; **Dream Agents** from events and the Season Pass |
| **Blue** | **Champions** — players in their prime, high stats | Limited-time **Legendary Agent** events only |
| **Kick-Off Stars** | New DLS26 type; special edition Raphinha and Alvarez at launch | Agents, events, passes |
| **Cult Heroes** | 12-player collection, live in v13.430 | **Cult Hero Agents** |
| **Dynamic Stars** | Cards that **upgrade live** with real-world national team results | **Dynamic Star Agents** |
| **World Heroes** | Special Players from Legendary Agents | **Legendary Agents** (300+ gems each) |

> **THE DLS26 CORRECTION — OFFICIAL:** special players **no longer count toward the main squad size**. A club can hold **unlimited** special players [EV-449, C1]. There is no longer a collection cap.

#### 6.2 The gacha probability mechanic — the highest-value collection finding [EV-450, C2]

> The chance of pulling a special player from a Legendary Agent depends on **how many legendary players you currently own** plus **how many are sitting in the transfer market** — and **the probability increases the fewer legendary players are left to pull.**

**The method:** buy and sell **every 80+ player you see**, so they sit in the **recovery tab for two days** and are removed from the agent pool. Reported to take Champion odds to **100%**, at a cost of **~275,000 coins across ~145 players and 70+ market refreshes**.

**Supporting moves:**
- **Stack gold players in the market** — they cannot be pulled from agents while they are there.
- **Lock players** — helps, but costs gems.
- **Pity ceiling:** about **15 Legendary Agents per target**, TOTY-style guarantee after 15.
- **Super Agents** give 83+ players for ~550 gems — poor value, too large a pool.

> **This mechanic is the reason the transfer-market section matters.** The market is not just where you buy players; it is the **lever that controls your agent odds**. Farming the market *is* farming your gacha chances.

#### 6.3 The counter-intuitive rule: do NOT release Classic Players [EV-450, C2]

Future Prize Ladders **randomise** their rewards. If you fail to collect a full Classic set in one ladder, you may get those players in the next — and **miss the newly released ones**. So: **keep every Classic you pull, even unmaxed.**

Release yields coaches, not coins — but for Classics specifically, the opportunity cost of releasing is a possible permanent miss.

### PHASE 7 — Clans (the compounding social layer)

| Mechanic | Value |
|---|---|
| Points per online win | **~3,500 Clan Points** |
| Individual contribution cap | **350,000** (= ~100 online wins/season) |
| Above the cap | Only ranks you first in-clan for the top-contributor gem reward — **does not help the clan total** |
| Creation cost | **150 gems**; barely breaks even in season one |
| Active clan season total | **13–15M CP** (350k+ members); others target 8M; second-tier 10–11M |
| Reward ladder | 25k first reward → 25g @1M → Leg XP @2M → Leg Scout @3M → 500c @5M → Rare Special Coach @7.5M → **150g @10M** |
| Entry requirements | Hide a clan from search, **but an invite code still bypasses them** |
| Fanzone | Gives **clan bonuses + stadium discounts** |

**Strategic read:** the 350k cap means the *clan* is the multiplier and *you* are the input. Joining a clan already running 13–15M is strictly better than building one, because the reward ladder is a clan-total goal.

---

## 3. Matchcraft — the mechanical edge

These are the cheap, permanent wins that separate tier 2 from tier 1.

**Stamina management** [EV-422, C2]:
- **30% stamina regenerates post-match**; a **benched player fully regenerates**.
- The **60–70 minute substitution sweet spot** — bring subs on there.
- **3-sub limit** per match.
- Hidden daily fatigue was reported in an April 2026 review — if the squad feels heavy, that is why.

**Goalkeeping** [EV-424/425, C2/C3]:
- **GKH = positioning and catching; GKR = reflexes and rushing out.** Keep **GKR ≥ GKH** — an unbalanced keeper is wasted.
- Target **~190cm** height.
- Manual control: **hold C** to hold the ball; **double-tap** to drop it.
- In shootouts, the **dead-centre** tactic is the reliable save.

**Discipline** [prior waves, C2]:
- Yellow cards **accumulate**; **5 = ban**, with a warning at 4. A red card is an automatic ban.
- Injuries cost **3–10 games** at roughly **5 gems per game** to heal.
- Physios: Common +10% / 50 coins · Rare +20% / 100 coins · Legendary +50% and heals all / 200–250 coins (150 coins max in Medium).

**Set pieces** [C2]: require joystick direction held. Free kicks — aim above the wall and add curl. Penalties — a gentle tap with stick direction. Corners — outswinger, call a second player, max B.

**Form Boost usage** [EV-428, C1/C2]: duration is a **set number of matches gated by your Training facility level, minimum one match**. Because the exact per-level table has never been published, treat Form Boosts as a **one-match** tool and spend them only on a player who needs a specific rating threshold crossed *now* — never as a routine.

### 3.1 The tier-1 control model (the single highest-value section)

Every item below is community-consensus [EV-436, C2] and costs nothing to adopt.

**Defence — the non-negotiable rules**

| Rule | Why |
|---|---|
| **Hold B and do NOT touch the joystick** | While holding B the player auto-moves to the ball; joystick input fights it |
| **Run players BACKWARDS** | The core fix for both wing-spam and C-spam. Do **not** tackle the outermost player as the ball is switched — that strands your players upfield. Switch to defensive mode and run backwards at every opportunity to concentrate the team in your own third |
| **Anti-C-spam: backwards-running central midfielders** | You will intercept the lofted passes; on intercept switch to attacking mode and counter |
| **Secondary press > main press** | Use the secondary press so a *teammate* applies pressure while you position your player to block the pass or shot. The same applies in aerial duels — against C-spammers never hold the main press |
| **Turn AUTO-SWITCH OFF** | The standard anti-C-spam setting. Practise in Career Mode first; it feels wrong for a while |
| **Never push defenders forward** | Use a DM to press in midfield; play zonal defending out of possession |
| **Block shots, and press C to bring the keeper out** | When the ball is in the air (lob or C-spam), press B and aim at the nearest midfielder/winger/fullback |
| **Slide-tackle sparingly** | Yellow-card risk; a ban costs you matches |
| **Switch tactics constantly** | DEFENSIVE when you cannot reach the ball in your own half (forwards track back, creating 2v1s), then ATTACKING the instant you win it |

**The C-spam escalation ladder** — the highest-value single finding:

1. When two strikers run at you, **head the ball diagonally: backwards AND slightly toward the second striker**. You either win it back to a defender or neither of you gets it — then switch quickly to another defender and collect.
2. Still C-spammed? **3 at the back → 4.**
3. Still? **4 → 5.**
4. Still? If your formation had **three vertical lines** (4-4-2, 5-3-2), switch to one with **four or five vertical lines** — **4-1-2-1-2 or 5-2-1-2**.

Reported to negate **~95% of C-spamming** [EV-436, C2].

**A-spam defence** (crossing side to side, then cutting back to a striker in the box): switch to **4-1-2-1-2 DEFENSIVE**. Once they reach the crossing stage only poor composure stops them — the key is cutting them off *before* that.

**Free-kick defence:** there is no time to press A for a defensive header. Move a player onto the **goal line** before the kick; that player is auto-switched to quickly, and the **double-tap "trick shot"** control produces an immediate header and goal-line clearance.

**Dribbling — the close-control touch fix:** dribbling at pace then switching direction produces an extra unwanted touch in the original direction. **Just before** switching direction, **hold the screen** for close control — this kills the extra touch. Release immediately to resume normal dribbling.

**Attack**

| Tactic | Execution |
|---|---|
| **Counter-attack** | 3 attackers up front; fast wingers (Salah right, Vinícius/Dembélé left) and a clinical striker. Win the ball → pass to the free winger → sprint. If closed down, hold C or A and pass to the **opposite** winger, who is always free in a counterattack → shoot or lob over the CBs → press A in the 1v1 |
| **Long B pass (the meta)** | Diagonal grounded B passes to wingers, best when you dispossess the opponent in your own half. **Press the Heatmap button and switch to ATTACKING mode before pressing and holding B** |
| **C-spam offence** | Tall, fast forwards; C button at a power bar **slightly over half** beats the defensive line for a 1v1 |
| **Possession** | Hold the ball and build slowly — *when you have it, your opponent can't score*. Short accurate midfield passes, wait for the right moment. Practise in the **Corner** training mode |
| **Long shots** | >75% accuracy with correct power — a way to score without breaking the line |
| **After you score** | Drop back, pass to GK/CBs, and defend the lead |

**Avoid:** blind C passes, blind shots, and rushing passes. Do dribble while stopped, and call out the keeper when necessary.

**Skill moves are swipe gestures, not buttons** — and whether the move executes depends on the player's **Ball Control** stat plus the engine's decision [EV-441, C2]. A high-CON player is worth more for this alone.

### 3.2 Injury and healing economics [EV-437, C2/C3]

- **Gem-to-games conversion:** 35 gems = 7 games out · 25 gems = 5 · 10 gems = 2 · 5 gems = 1.
- **Physio tiers:** Common +10% energy / ~50 coins · Rare +20% / ~100 coins · **Legendary +50% and heals ALL injuries / 150 coins with maxed facilities, 250 otherwise**.
- A **mid-game Team Boost** and a **post-match Team Physio** both restore 10% stamina; individual healing costs ~2–4 coins per player.
- **Maxed Medical Centre** makes physio trips "super cheap" — effectively endless playtime.
- Injuries last **3–10 games**; a **Fitness coach** can also help heal an injured player [C3].

---

### 3.3 Set pieces — the highest-percentage scoring in the game [EV-444, C2/C3]

> **Corners are the most reliable goal source in DLS26.** A December 2025 post: *"Corners are way too easy to score now. If your opponent in DLL gets one, it's almost guaranteed that you concede."* Penalties, by contrast, are described as rigged.

**Corners — the agreed mechanics:**

| Rule | Detail |
|---|---|
| **Cross with A** | A passes are fast, produce faster headers, and make it easy to pinpoint players |
| **Tall targets** | Konaté, Haaland, Van Dijk named; one source says **190+ is required** for the header routine |
| **Take from behind the goal line** | Not from next to the sideline |
| **Shortest players on corner duty** | So the players in the box are on average taller |
| **Aim arrow ~90% inside the pitch** | Or set the aim line at ~30° to the goal line |
| **TIMING is critical** | Press A **right before** the ball reaches the target player |

Power recipes that work (pick one and drill it): A to 60% · A to 80–90% with in-then-out curve · C at 2/3–3/4 · C at 80% on a 50–60° angle · or leave the arrow alone and play a strong lob to a defender, then a short header to the nearest open man.

**Two caveats:** DLS25 **nerfed corner headers**, so the fallback is to aim middle and press **B to pass** to someone better placed rather than heading immediately. And **corner footedness is contested (C-022)** — the majority say same-foot corner, a minority say opposite-foot. Test both in the free training ground before committing.

**Defending corners:** switch to a tall player and **B-pass 90° away from the direction** the opponent wants to head it. Alternative: charge A and point up-field the moment the corner is taken.

**Free kicks — five rules that matter:**

1. **Two dedicated takers**, one left-footed and one right-footed. Technique becomes consistent.
2. **Every player has different free-kick settings.** Ronaldo and Messi take them differently; Alexander-Arnold "curves A LOT", Modrić far less. Do not assume one technique transfers.
3. **70% power floor.** Below that, the ball is not guaranteed to clear the wall.
4. **The wall is your reference.** Learn how much your taker curls by watching *which player in the wall* the arrow points at. Aim over the **shortest** player, at the **top corners**, with a **diagonal** swipe.
5. **Distance bands:** 18–22 yd = curl with the inside foot · 23–28 yd = power or curled top-corner · 30+ yd = long-shot technique or pass.

**The Live-mode timing trick:** an opponent can manually move a player onto the goal line and head your free kick away. So: **wait** for them to step onto the line → **switch the taker** (this resets where their player is) → **shoot immediately**.

If direct free kicks are unreliable, don't take them: C-pass to a player beside the wall and shoot the rebound, or cross into the box.

**Penalties** — reported conversion is **85–90% in DLL** and **70–80% in shootouts**, and players call shootouts rigged with predictable run-ups. Working techniques: slightly off-centre with moderate power · low C with a medium A · a light A tap or full-power B to the bottom corners · against the AI, the middle with a slightly powered A · or one-third off the keeper toward the post with the pass button at half to two-thirds power.

**The one universal rule:** make the taps **gentle and quick**. Holding a split-second too long produces a wild, overpowered shot. Always aim top or bottom corner — the top of the goal gives an illusion of width that a wasted penalty will not honour.

### 3.4 Scenarios and Exhibition [EV-445, C2/C3]

- **Scenarios:** you are already **losing** and must beat **Hard AI**. 50 coins daily, resets each day. DLS26 Summer Spotlight officially added *more bonus objectives and rewards*. The community calls scenarios **the hardest content in the game** — "way harder than Live Games", and even "easy" scenarios reportedly play at medium difficulty. Budget time accordingly.
- **Exhibition:** offline friendlies via a **room code**, no rewards. This is your **free training ground** — the right place to drill corners, free kicks and new formations before taking them into Live.

**Formation meta is genuinely unsettled** (C-014 stays open by design): 4-4-2 for balance (LM/RM as wingers, full-backs supporting both phases); 4-1-2-1-2 and 4-1-3-2 favoured by the tier-1 guides; 4-3-3 and 3-4-1-2 pushed by sportsdunia. **Pick one and learn it deeply rather than chasing the meta** — the record run used a mostly common/rare squad.

## 4. What NOT to do (dead ends, do not retry)

| Trap | Why |
|---|---|
| Chemistry / Fluid Formations systems | **Fabricated.** Source-attributed to `playdreamleaguesoccer.com`, which also publishes fake testimonials ("DLS_King_07 Mumbai", "GoalMachine_23 Bangalore") [EV-413] |
| Weather affecting gameplay | **Unconfirmed**, narrowed to one discreditable source [EV-407] |
| A Youth Academy | **Does not exist** — proven by a fan *feature request* thread [EV-408] |
| "Seven facilities" | **Wrong.** Five are official: Stadium, Medical, Commercial, Training, Fanzone. Recruitment and Accommodation are in-game but community-sourced only [EV-419, C1] |
| `sportsdunia` Commercial tables | **Rejected** — two rejected tables |
| `eslamgaming` | Fabrications **and** a wrong control map |
| `chaptercheats` | Wrong CON definition (CON = **Ball Control**, not something else) |
| `Baiduwiki` | Describes a non-existent auction-house market |
| Spending coaches early | Community consensus: **stack coaches, don't use them too early** [EV-433, C3] |
| Form Boosting low-rated players | 5g/+1 for one match is the worst gem rate in the game |
| Building your own clan from zero | 150 gems and you "barely break even in the first season" [EV-429, C3] |
| Mods, hacks or coin/gem generators | **OFFICIAL FTG:** infinite coins/gems do not exist, modified versions end in **account blocking**, and generators are a scam [EV-441, C1] |
| Half-upgrading a stadium stand | "If you build a side only partially, the next time you would have to pay the full price to complete it" [C3] |
| Upgrading a stand **with a roof** | "On the highest number you're paying for the roof and no extra seats" [C3] |

---

## 5. DLS26-specific modes worth watching [EV-446, C1]

| Mode | What it is | Why it matters |
|---|---|---|
| **Dynamic Stars** | Special Players whose cards **upgrade live** with real-world national team tournament performance — DLS's analogue of EA's "Path to Glory" | The only cards whose rating moves without you spending coaches. Collection opened 8 Jun 2026; obtained via **Dynamic Star Agents** |
| **World Tournament** | A brand-new **International Football event type** with high-tier reward tracking | Fresh reward surface; watch for its return |
| **World Heroes** | Live-service event from 1 Jul 2026; Special Players obtainable via **Legendary Agents** | The **second route to Special Players** outside the Prize Ladder — every Legendary Agent is a free roll |
| **Cult Heroes** | 12-player collection, live in v13.430 | Marquee targets: de Gea, Aubameyang, Dybala |
| **Dream Stars / 12th Man** | Dream Stars from real-world season performances; the 12th Man is the **community-voted extra slot** | FTG never names the winner — treat as an event to watch, not a card to plan around |

> **Practical takeaway:** because Legendary Agents can yield World Heroes, and Dynamic Star Agents come from event draws and Season Passes, **agents are a second acquisition lane parallel to the Prize Ladder.** Do not spend gems on agents you don't need, but do not ignore the free ones either.

---

### 5.1 The social and matchmaking layer [EV-451, C1/C2]

**Friend Match** (official): enter any code, share it, your opponent enters the same code, both tap OK. Two things to know:
- Codes may only contain **A-Z, 0-9 and the hyphen**, and FTG warns to pick a unique one — *a code already in use can see you joining the wrong match.*
- **If either side disconnects, the game awards a 3-0 win to the player with the more stable connection.** A weak connection hands your opponent a win rather than merely failing the match.

**Adding friends** uses a **closed internal system** — no username search, no social-media linking. You generate a code from your profile, and it **expires after 5 minutes**.

> **Practical warning:** a popular code like `12345` will match you against a **random** player, not your friend. The code is a shared lobby key, not a private invitation.

**Clan 1v1** requires both players in the **same clan**: DLL → Clan → select the member.

**The unlock:** Dream League Live and Friend Match open after **six Career matches** [C-025 — one guide self-contradicts with three; plan for six].

**Connection requirements** (official): DLS has low bandwidth needs but is **sensitive to high latency and packet loss**, so cellular and satellite connections can fail despite good bandwidth. **No co-op exists.** Summer Spotlight added a **Player Recovery** feature — officially confirming the recovery tab behind the gacha method in §6.2.

---

## 6. Open gaps that still bound the plan

These are unresolved and each one caps precision. They are ranked by impact on the mission.

| # | Gap | Impact | Status |
|---|---|---|---|
| 1 | **Fanzone per-level costs** | Unknown gem commitment for the newest facility | Never published. Function confirmed (clan bonuses + stadium discounts) [C1] |
| 2 | **Form Boost duration per Training level** | Cannot price the Training facility's real value | Mechanic officially confirmed; **numbers never published** [EV-428, C1] |
| 3 | **Medical per-tier % beyond L1** | Cannot optimise the injury economy | Only L1 (−5% injury / −10% heal cost) sourced; later tiers described qualitatively only [C2] |
| 4 | **Post-DLS25 coach breakthrough %** | Coach packs priced off a DLS20 baseline | 5/10/20 confirmed as the DLS20 baseline; post-DLS25 figures unconfirmed [C2] |
| 5 | **Fan Approval mechanics** | Blocks the last stretch to 100% club value | Only the 75%/100% milestones known |
| 6 | **GCC format** (C-013) | One cup's structure unclear | OPEN conflict |
| 7 | **LIVE rank names above "Veteran"** | Cannot name the top rank | Names known to Veteran only [C2] |
| 8 | **12th Man winner identity** | A mechanic to watch each season | MECHANIC CLOSED (community-voted final Dream Star, EV-438 C1); FTG never names the winner |
| 9 | **Cult Heroes OVR conflict** (C-018) | 92 vs 95 on the four 85-rated heroes | OPEN |
| 10 | **Clan top-contributor reward** (C-017) | 50 vs 100 gems | OPEN |
| 11 | **Formation meta** (C-014) | 4-2-3-1 vs sportsdunia top-5 vs 4-4-2 | OPEN — a genuine live disagreement, not an error |
| 12 | **Commercial bonus curve** (C-019) | 13%/21% vs "10% at L5, biggest FTG scam" | OPEN |
| ~~13~~ | ~~**Special player max cost** (C-020)~~ | ~~2,100 gems / 7.5 coaches vs 6-7 coaches vs 2,100-2,835~~ | **RESOLVED at ckpt-118** — ~2,000–2,100 gems, 6–7 Legendary Special Coaches, ~420 gems saved by cancelling |

**Step 2 (static APK datamining)** remains postponed pending user direction. It is the only route that would close gaps 1, 2, 3, 4 and 5 definitively, because all five are numeric tables inside the game data.

---

## 7. The one-page routine

**Daily (≈45–60 min):**
1. Season Pass login (+40 SP) and daily challenges (5–11 gems)
2. Daily Scenario (50 coins) — budget real time, it is the hardest content in the game
3. 3–5 DLL matches **at tier 10 or above**
4. Buy 3–5 players under 210 coins → release → coaches
5. One 8-hour ad cycle (up to 600 coins)
6. **Two free-kick or corner attempts in Exhibition** — the training ground, and the highest-percentage scoring route in the game

**Weekly:**
1. Push the DLL weekly leaderboard before the reset (placement gems + participation gems)
2. Clan contribution toward the 350k cap
3. Dream Draft when free (up to 7 rounds, 185 DP ceiling, gems only)
4. Facility upgrade — **stadium first, always**
5. Reassess: are you lingering in a tier you can win? Promote.

### The time-efficiency unlock [EV-441, C3]

Once a division is **mathematically secure** — typically after 9–10 wins in the Legendary Division — **stop playing the matches and let them auto-finish as losses.**

- A Legendary Division home match pays **~150 coins even in defeat** (about 75 base + 75 stadium bonus).
- Goal coins are **capped at 30 per match** (6 coins × 5 goals — the same limit as the DP cap), so scoring more than 5 buys nothing.
- The only cost is a **10-gem "win all games" objective**.
- A whole Career Season still yields **~110 gems** (35 + 75), and 10 matches produce **~2,000 coins in about an hour**.

This converts Career Mode from a time sink into a background coin farm and is the single biggest quality-of-life gain available.

**Gem ledger for a full season** [EV-443, C3] — where the free gems actually come from:

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

Two hard thresholds: **DLL pays gems for a season finish with a minimum of 14 points**, and the **final DP ladder gem reward needs ~145,000 DP**.

**Every 90 days:**
1. Prize Ladder cycle closes — first special at ~50,000 DP, all four at ~200,000
2. Progression Bank pays out (10-day seasons inside it)

---

## 8. Success criteria

| Milestone | Metric | Evidence-based expectation |
|---|---|---|
| M1 | Reach **tier 10** in Live | Unlocks Live gems |
| M2 | First **Tier 1 Champion** | ~16 days of full-time play; ~145,000 XP; achievable with a common squad |
| M3 | **Legendary Division** champion in Career | Requires the stadium class gate and top-2 finish |
| M4 | Team rating **80+** | Gold-carded players become regular in the market |
| M5 | **100% Fan Approval** | Fan Favourite achievement (2,000 XP) |
| M6 | **~23 players fully maxed** | The actual definition of 100% club value |
| M7 | First **Special Player** | ~50,000 DP ≈ 300–324 matches |
| M8 | **Cult Heroes marquee** (de Gea/Aubameyang/Dybala) | Random draw from Cult Hero Agents |
| M9 | **Hold Tier 1** across consecutive seasons | Against 10M+ XP opponents — the true #1 test |

---

*End of masterplan. All figures traceable to `kb/claims.jsonl` and `docs/continuity/a7e23a6b/evidence/index.jsonl` at ckpt-105.*

---

> **COMPANION FILE — `docs/operational_rules.md`.** The masterplan says *what* to aim for; the operational rules say *what to do in each game state*, as a nine-state machine (S0 Bootstrap -> S1 Economy -> S2 Promotion Push -> S3 Secure Division -> S4 Coin Farming -> S5 Coach Farming -> S6 Squad Assembly -> S7 DLL Climb -> S8 Cultivation -> S9 Maintenance) with the guards that move you between them. Every rule carries its evidence reference, every numeric figure traces to a claim, and the file ends with an explicit audit listing the six known weaknesses and a PASS-with-stated-limits verdict. A third companion, `docs/dll_tier_playbook.md`, gives band-by-band DLL tactics for tiers 20 to 1 including the tier-camping gem engine and the maxed-squad handicap.*
