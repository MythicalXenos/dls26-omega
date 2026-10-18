# DLS26 OMEGA — Strategy Masterplan: Path to #1

**Compiled:** 2026-10-18 · **KB basis:** ckpt-094 (`ab32028`) — 1,333 claims / 341 evidence records
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

**Cost to max one special player:** ~7.5 Legendary Special Coaches ≈ **2,100 gems** (15 Rares = 2,520). Conflict C-020 records a 6–7 coach and a 2,100–2,835 gem alternative.

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
- **DP economics:** career max **140 DP/match**, DLL+Draft **185 DP**; **5-goal cap**; ~**2,800 DP/day**; ~**200,000 DP** total; boosts **+50% / +70% / +150%** plus ad boosts [prior waves, C2/C3].

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

**Formation meta is genuinely unsettled** (C-014 stays open by design): 4-4-2 for balance (LM/RM as wingers, full-backs supporting both phases); 4-1-2-1-2 and 4-1-3-2 favoured by the tier-1 guides; 4-3-3 and 3-4-1-2 pushed by sportsdunia. **Pick one and learn it deeply rather than chasing the meta** — the record run used a mostly common/rare squad.

### 3.2 Injury and healing economics [EV-437, C2/C3]

- **Gem-to-games conversion:** 35 gems = 7 games out · 25 gems = 5 · 10 gems = 2 · 5 gems = 1.
- **Physio tiers:** Common +10% energy / ~50 coins · Rare +20% / ~100 coins · **Legendary +50% and heals ALL injuries / 150 coins with maxed facilities, 250 otherwise**.
- A **mid-game Team Boost** and a **post-match Team Physio** both restore 10% stamina; individual healing costs ~2–4 coins per player.
- **Maxed Medical Centre** makes physio trips "super cheap" — effectively endless playtime.
- Injuries last **3–10 games**; a **Fitness coach** can also help heal an injured player [C3].

---

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
| Half-upgrading a stadium stand | "If you build a side only partially, the next time you would have to pay the full price to complete it" [C3] |
| Upgrading a stand **with a roof** | "On the highest number you're paying for the roof and no extra seats" [C3] |

---

## 5. Open gaps that still bound the plan

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
| 13 | **Special player max cost** (C-020) | 2,100 gems / 7.5 coaches vs 6-7 coaches vs 2,100-2,835 | OPEN — plan on 2,100 gems |

**Step 2 (static APK datamining)** remains postponed pending user direction. It is the only route that would close gaps 1, 2, 3, 4 and 5 definitively, because all five are numeric tables inside the game data.

---

## 6. The one-page routine

**Daily (≈45–60 min):**
1. Season Pass login (+40 SP) and daily challenges (5–11 gems)
2. Scenarios (50 coins; 75–100 per 8h cycle)
3. 3–5 DLL matches **at tier 10 or above**
4. Buy 3–5 players under 210 coins → release → coaches
5. One 8-hour ad cycle (up to 600 coins)

**Weekly:**
1. Push the DLL weekly leaderboard before the reset (placement gems + participation gems)
2. Clan contribution toward the 350k cap
3. Dream Draft (18 players, 75+ OVR, 7 rounds, free since DLS24)
4. Facility upgrade — **stadium first, always**
5. Reassess: are you lingering in a tier you can win? Promote.

**Every 90 days:**
1. Prize Ladder cycle closes — first special at ~50,000 DP, all four at ~200,000
2. Progression Bank pays out (10-day seasons inside it)

---

## 7. Success criteria

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

*End of masterplan. All figures traceable to `kb/claims.jsonl` and `docs/continuity/a7e23a6b/evidence/index.jsonl` at ckpt-089.*
