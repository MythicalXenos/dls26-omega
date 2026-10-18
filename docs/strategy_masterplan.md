# DLS26 OMEGA — Strategy Masterplan: Path to #1

**Compiled:** 2026-10-18 · **KB basis:** ckpt-180 — 2,224 claims / 419 evidence records
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

> **THE ACHIEVEMENT SYSTEM NOW PROVES TACTIC 1** [EV-454, C3]. DLL promotion achievements pay an **escalating XP ladder**:
>
> | Tier | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | **1** |
> |---|---|---|---|---|---|---|---|---|---|---|
> | XP | 500 | 1,000 | 1,500 | 2,000 | 2,500 | 3,000 | 3,500 | 4,000 | 4,500 | **5,000** |
>
> Promoting from tier 10 to Tier 1 Champion therefore pays **27,500 XP in achievements alone** — and **Bragging Rights** adds **2,000 XP for champion of any tier**, so every tier title is worth banking. Each tier cleared pays more than the last, while a season spent in a tier you have already cleared pays nothing extra. That is the arithmetic behind *"not once did I not get promoted to the next tier (crucial to saving XP)."*
>
> **Full achievement set: 40 achievements / 20,000 XP on Android, 63 achievements / 13,483 EXP on iOS** [EV-466, C2 — C-026 RESOLVED: the earlier "63 / 98,000 XP" figure stitched the iOS count to a Classic-era Google Play XP total; the classic-era number must not be quoted as a DLS26 figure]. Every achievement in the DLS26 Android set is worth **500 XP**, and the set is front-loaded — completion runs 62.8% for reaching the Amateur division down to **8.45% for 150 DLL wins**. Biggest non-tier targets: **Goal Machine 3,000** (10,000 goals) · **Unstoppable 3,000** (1,000 wins) · **Elite Champions 3,000** · **Scoring For Fun 2,500** (+100 GD in a season) · **Revolving Door 2,500** (100 signings) · **Ultimate Dream Team 2,000** (80% club value) · **Fan Favourite 2,000** (100% approval) · **Golden Boot 2,000** (40 goals, one player) · **A Place Called Home 2,000** (80,000 capacity) · **Rise To The Top 1,500** (develop a player to 100).
>
> **A realistic three-month benchmark** [EV-454, C3]: maxed XI + 9 maxed subs, **1,472,836 online XP**, 57% win rate, **13 Tier 1 championships**, 149 gold medals, 987 Career + 1,086 Live games, 19 Legendary premierships.

> ### THE GEM ENGINE — tier camping [EV-448, C2/C3]
>
> The record run optimised for **speed to Tier 1**. If your priority is **gems per hour**, the optimal tactic is the opposite:
>
> **Camp between Tier 5 and Tier 2** (Tier 1 cannot be camped — it is the ceiling) and **aim for SURVIVAL, NOT PROMOTION.** Win only **4–5 matches** (12–15 points), then **quit the rest** — and *losing en route is even better*, because it keeps you in the camping tier instead of promoting you into a harder one.

> **⚠️ CHECK THE SEASON FORMAT BEFORE YOU CAMP** [EV-483, C2]. DLL seasons run 10 days and the format **alternates between draw-allowed and extra-time-mandatory** — *"DLS switches between Extra Time and Draw after every season, so this season is Extra Time and next season… the match format will again be draws and it will repeat like this"* — and the game tells you which at kick-off. **In a draw-allowed season the arithmetic above holds. In an extra-time season a draw is not a result, it is a coin-flip you must play out** — so bank the 4–5 wins first and treat any remaining match as a genuine extra-time match, not a free point.
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

### 4.1 The complete coaching economy [EV-489, C2/C3]

**THE EFFICIENCY LADDER AT A MAXED TRAINING FACILITY** — the arithmetic behind every gem you spend on a coach:

| Tier | Development points | Gem cost | **Gems per point** |
|---|---|---|---|
| **Common** | 2 | 63 | **31.5** |
| **Rare** | 6 | 168 | **28** |
| **Legendary** | 12 | 280 | **23.33** |

**Legendary is the most gem-efficient coach per point** — which is why the Training facility's 75 × N ladder pays for itself, and why the corpus's Training-first rule is not just convenience.

**THE COST TO MAX ONE PLAYER** (~90 development points):

| Route | Coaches | Total gems |
|---|---|---|
| Common | 45 | **2,835** |
| Rare | 15 | **2,520** |
| Legendary (special players) | 7.5 | **2,100** |
| **Legendary (normal players)** | **9** | **~2,520** |

> **Normal players need 9 Legendaries, not 7.5** — the 7.5 figure applies to special players. Plan on 9.

**COACH COUNTS TO MAX:** outfield **80 Common / 20 Rare / 9 Legendary**; goalkeepers **20 / 10 / 4**. A full 16-player squad needs roughly **142 Legendary / 320 Rare / 1,280 Common**.

**EFFECT SIZES:** Legendary boosts **3 random stats by +3** · Rare **2 by +2** · Common **1 by +1**. This reconciles the 12-point and 9-point figures once the Strength/Control double-weighting is applied.

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
> **So the most expensive item in DLS doubles as a free information tool.** Open a Legendary Special coach, read the next four stats, cancel, and spend a Common coach if the preview is bad. The saving is quantified at **~70 gems × 6–7 = ~420 gems per maxed special player**. **Keep at least one Legendary Special coach in reserve at all times for this purpose.**

> **🎯 THE GOALKEEPER RULE:** *"Legendary coaches increase GKR and GKH by +3, but only use if GKR > GKH."* A Legendary raises **both**, so using it when GKH is already the higher stat wastes half the value. For GKs, run **1 Rare + 4 Commons and repeat**.

**THE CLUB MINIMUM IS 16 PLAYERS** — *"Make sure you have 16 players before using coaches, that's the club minimum size and it helps speed up the process."*

**THE COACH GEM PRICE LADDER** [EV-491, C2]: Common **17 gems** · Rare **52 (maxed) / 67 (unmaxed)** · Legendary **157 (maxed) / 202 (unmaxed)**. So the Training facility saves **15 gems per Rare and 45 per Legendary** — and a **third** source confirms it *"will pay itself after 20 or so legendary coaches."*

**THE COMMERCIAL-vs-COACHES BREAKEVEN** [EV-491, C3]: a Common coach bought efficiently costs ~200 gems for 54 upgrade points = 10,800, which at a 10% Commercial bonus needs **~108,000 coins** to match. **So max Commercial only if you will grind past ~108,000 coins; otherwise keep the gems for facilities.** That is the cleanest decision rule the corpus has for the Commercial question.

**RARE GOALKEEPERS YIELD ONLY ONE COMMON COACH** [EV-491, C3] — *"Don't buy rare goalies as they also only get 1 common coach after release, same as any common goalie."* An explicit exception to the release mapping and a direct instruction for coach farming.

**THE COACH-FARMING THRESHOLD IS 192 COINS** — two independent derivations of the same number. Releasing a legendary player yields 2 Rare coaches, so *"1535:8=192… only buy common players that are 192 coins or less."* That brackets the *"buy under 180-210 coins"* band from §3.6 exactly.

**And the sharper, DLS26-dated filter** [EV-511, C3]: *"**Buy a common scout for 75 coins** (~63 if you max out the recruitment facilities), and **target only players who cost 130 coins or less.** After buying them, **immediately sell them and repeat.**"* The reporter saw players as low as **42 coins** appear. So the farm has a ceiling (130, tighter than 192) and a floor, and the Recruitment facility discounts the scout as well as the coach — which is a second reason the facility outranks its gem cost.

> **🎯 NEVER COACH THE INTERIM SQUAD** [EV-511, C3]: *"**coaches shouldn't be applied to your common team. Save and store ALL your coaches until you have the starting 11 you are satisfied with.** This is even more important for those who are aiming for a full gold team."* So the coaching economy is banked, not spent, until the XI is final — and **form boosts and physios are a waste of currency unless you earned them free from an event.** Gems go to facilities and coaching; never to temporary OVR.

**THE RELEASE-TO-COACH MAPPING, three sources agreeing:** Common release = **1 Common coach** · Rare release = **2 Common coaches** · Legendary (80+) release = **1 Rare coach**. This is the product of the DLS21 nerf, which also cut Legendary coaches from +5 to +3 per stat.

**THE SCOUT LADDERS:** discounts of **2–4% (Common) / 3–5% (Rare) / 4–8% (Legendary)** per recruit, and — because each scout yields **two candidates** — P(at least one legendary) is **3.96% for a Common scout and 27.75% for a Legendary**, a 7.01× ratio against a 6.67× price ratio. **Legendary scouts are good value; the 2% Common figure is the correct one.**

**THE DP BOOST MAXIMA:** Rare Boost **+75%** (245 DP max in Career, 324 in DLL/Dream Draft) · Legendary Boost **+150%** (350 Career, 463 DLL/Dream Draft).

### 1.2 Career Mode (the economy and the rating engine)

Eight divisions: **Academy → Amateur → Division 4 → Division 3 → Division 2 → Division 1 → Elite → Legendary** [EV-423, C2].

- **Promotion:** top 2 direct; 3rd–6th enter a playoff; a **stadium class gate** also applies [EV-423, C2].
- **Cups follow your current division** — Bronze (Academy/Amateur), Silver (Div 4/3), Gold (Div 2/1), Diamond (Elite/Legendary) [EV-431, C3]. **Consequence:** to win the Gold Cup you must *drop* to Division 1; once promoted, Gold becomes Diamond.
- **Relegation is not a disaster:** dropping divisions reduces coin/gem awards but **does not affect the transfer market** [EV-431, C3].
- A **70-rated team can win the Legendary Division**, though it is very hard [EV-432, C3].

---

## 2. Phase plan

### PHASE 0 — Setup (Day 0, one sitting)

> **💾 SAVE MODE MAKES A CAREER LOSS UNDOABLE** [EV-514, C3] — and this is the game's own feature, not an exploit. *"We can use **Save Mode** in Dream League Soccer to **delete saved matches**. So, if you have conceded a goal, you can delete the saved match and start it from the beginning... choose **Delete Save Match → Yes**, then **Exit Save Mode → Yes**."* One source claims **2,000 matches without a loss** built this way. **So in Career a defeat is a choice, not an outcome** — which reframes the corpus's play-through-your-mistakes advice: play through mistakes in DLL, where the record is permanent, and use Save Mode in Career, where it is not. (The source adds that turning the internet off makes it faster, so treat the online behaviour as unverified.)

1. **Captain selection.** Current build offers ~80 captain choices plus *Create Your Own Captain* [EV-427, C2]. The DLS21-era build showed 9 random Legendary Cards [EV-427, C2] — do not follow old guides that assume 9. **Pick a fast forward with *minimum* shooting who can at least shoot, and never a goalkeeper or a defender** [EV-501, C3] — *"you always want to get a fast forward with minimum shooting that can at least shoot... YOU SHOULD NEVER PICK OUT A GOALKEEPER OR A DEFENDER!"* **Filter on stamina, not pace**: the community benchmark is **80+ stamina**, because a fast captain with no legs gets replaced. Above 180cm with shooting and speed above 80 and a decent passing attribute, and he can take set pieces too. **Foden and Nunez are the named long-term picks** — they still fit a gold team later. The reason to spend the slot on attack: *"offensive players cost a lot more than defensive players."*
2. **Controls.** Preset **A = Hard Kick/Shoot, B = Low Kick/Pass, C = Lofted/Chip/Curl/Cross** [prior waves, C2]. Set pieces require the joystick; the B auto-press needs stick input [C2].
3. **Camera:** Tele, H75 / Z35 [C3]. **Graphics:** Medium / 60 FPS / Semi-auto [C3].
4. **Commentary:** English (Gary Bloom) is the default; DLS26 added Turkish and Arabic [EV-427, C1].
5. **Create the account on one platform only — and understand that this is a ONE-WAY DOOR** [EV-462, **C1 — OFFICIAL**]:
   - **Do not buy an account.** Marketplaces sell DLS26 accounts **from $37–$40** with the contents itemised, and FTG **prohibits profile sale and purchase and bans for it** [EV-516, C3]. The official 30-day reset cooldown may not be policed — one player reports a third reset without waiting — **but that is a reason to ignore the loophole, not to use it**: enforcement can land mid-plan, and the official rule stands.
   - **"We have limited each player to one DLS account."** The profile is permanently bound to a **Sign in with Google (Android only)** or **Sign in with Apple (iOS only)** login.
   - **NEVER sign out** of that login. *"If you sign out … at any point whilst playing, your account will no longer be linked with your game profile and is susceptible to loss if you uninstall or change devices."* A lost profile **cannot be recovered**.
   - **⚠️ THE OVERWRITE HAZARD — the mechanism that actually destroys accounts** [EV-497, C2]. A player who lost years of progress: *"I made the mistake of uninstalling the 2024 version without rechecking the account link. But when I reinstalled the game, my original account was gone. I was met with a fresh profile, and **worse, it seems that this new empty account overwrote my old one.**"* It runs the other way too: *"**Current progress will be deleted if the Google account you connect has the old data saved**"* — and *"make sure no previous profile is connected to your Apple ID before you connect it, as it will override the data if there's an existing profile already."* **So the link is not a one-time setup step: check the sign-in state every session, and always immediately before an uninstall or a device change**, because the link itself can drop silently — the same player reports the Google sign-in being *"disabled in the settings (which happened randomly)."*
   - **Before any transfer**, run the check: on iOS, Apple ID settings → Sign-in & Security → sign in with Apple, and confirm no previous profile is attached. On Android, open the signed-in-with-Google setting and if it shows a stale game entry, remove it first, then sign in inside the game.
   - **If a profile is lost anyway**, the account ID persists on FTG's servers and support can recover it — send them the player's rating, your account name, rank, phone name, and a screenshot of the **Manage Device ID**. And **ignore any guide that tells you to back up via "Settings → Cloud → Save Progress"** — that path does not exist; the seventh and most dangerous playdreamleaguesoccer.com fabrication.
   - Cross-platform transfer (Android to iOS or back) is possible but needs a **code from Manage Devices → Generate Code** typed into **Link Profile** on the new device — both under Options (gear) → **Advanced** — and a code cannot be used on the device that generated it.
   - **Reset Profile** (Settings → Advanced, skull icon) is irreversible, **destroys all coins, gems, consumables and in-app purchases**, and is limited to **ONE RESET EVERY 30 DAYS**.
   - **Consequence for this mission:** the account — and with it the **region seed that decides your matchmaker pool and leaderboard surface** — is permanent. **There is no cheap re-roll.** Set it up deliberately, on the platform you will keep, linked and never signed out, and treat every early mistake as something to play through rather than reset.
6. **Join a clan immediately** (rank 20 unlocks full clan features; minimum 50 members; 150 gems to create) [EV-429, C2/C3]. Clan points are earned from regular matches, Live events, Dream Draft, real-life scenarios and Season Pass tiers [EV-429, C2].

### PHASE 1 — First 48 hours (economy bootstrap)

**Priority order for facilities** (the community consensus and the income logic agree):

| Order | Facility | Why | Numbers |
|---|---|---|---|
> **💰 THE CAREER GEM-PER-MATCH RULE — the most useful number in the Career economy** [EV-502, C2, two independent sources]: *"do your own calculations and if you are getting **4+ gems on each match** then it's worth it otherwise it's not."* **Play everything and you average 3.5 gems a match (145 gems across 41 games); play the selective set and you average 4.3 (100 across 23).** Same total, nearly half the matches. The selective set is: **Legendary Division home matches only · skip the Global Challenge Cup entirely ("the matches are way too many") · play every International and Allstar cup match · the Diamond Cup only when a Division Objective demands reaching its final.** The Legendary Division needs only **10–12 wins** to win, and playing the cups is what buys you the skip — with the cups, the league objective drops to 11–13 wins and you can miss two away games; without them the third objective becomes *"win all legendary games"* and you must play all 15. **And once the division is won, concede the rest:** *"I just matches finish without playing and lose as even after losing we get around 150 75+75 coins from home games and this is without investing any time."* You lose only the win-all objective, not the income.

> **The per-competition gem table behind that rule** [EV-502, C3]: **30** Legendary Division · **25** Diamond Cup · **20** International Cup · **15** Global Challenge Cup · **15** International Allstars · **5** allstar match. And promotion itself requires the **Division Objectives** (My Club) completed inside **15 Division Games** — a finishing position *and* a **goal count**, with 10 wins enough to top the table but the goals the harder half.

| 1 | **Stadium** | Home-match coin bonus is the only compounding income source — **and capacity is a hard promotion gate** | A **coin** project, not a gem one: sector levels cost 0–650 coins each, optimal build **92,632 capacity → 52 coins per home match** for ~10,000 coins [EV-460, C2] — and **only seven of the eight stands need maxing**: *"you'll need to upgrade 7 to the max to get 85,000 capacity. The last stand un-upgraded must be a corner stand"* [EV-517, C3], so the corner is the one to leave. **Division gates:** Academy 6,462 → Div 3 **15,000** → Div 2 **30,000** → Div 1 **45,000** → Junior Elite **60,000** → Elite **80,000**; max capacity 90,456 [EV-460, C2] |
| 2 | **Commercial** | +13% coins at L2, **+21% at L3** (one source curve, contested — C-019) | First tier 75 gems. **Real magnitude at max: only ~6–20 extra coins per game** [EV-465, C3] — the payback runs to hundreds of matches, so **spend here last** |
| 3 | **Training** | Coach discounts **and** Form Boost duration **and** formations — **the highest-value gem facility** | **10 levels at 75×N gems** (see the uniform-cost rule below); L4 is the coach-farming unlock |
| 4 | **Medical** | Injury reduction and cheaper recovery | L1 gives −5% injury / −10% heal cost; L2–L5 **never published** [C2] |
| 5 | **Fanzone** (new in Summer Spotlight) | **Clan bonuses + stadium discounts** | Per-level costs **never published** [EV-428/App Store, C1 on function, C5 on cost] |

**The stadium ladder — the numbers behind row 1** [EV-460, C2]:

| Division | Minimum seats | |
|---|---|---|
| Academy (start) | **6,462** | already built when the game begins |
| Division 3 | **15,000** | |
| Division 2 | **30,000** | |
| Division 1 | **45,000** | |
| Junior Elite | **60,000** | |
| **Elite (top)** | **80,000** | Auto Build ceiling is also 80,000; absolute max 90,456 |

> **Capacity is a hard promotion gate, not a bonus:** *"if you finish your championship and automatically you are promoted to next division. But if you haven't a precise number (per each league) of seats you will not be promoted to next division."* Win the league without the seats and you stay where you are.

**The build order is arithmetic, not folklore** [EV-460, C2/C3]. The stadium is **8 sectors** — 2 Ends, 2 Sides, 4 Corners — each upgraded independently, and each has its own seat ladder: **Ends** 22 levels (1,323 → 9,722 seats) · **Sides** 29 levels (1,908 → 14,128) · **Corners** 43 levels (0 → 10,692). All costs are in **coins**, not gems — which is why the stadium is a *coin* project while the facilities are a *gem* project.

- **Corners are the cheap seats.** Corner 7 costs about **100 coins for 722 seats**; Corner 11 adds 1,264 for about 130. Corner stands deliver the most seats per coin by a wide margin.
- **⚠️ BUILD EACH STAND TO ITS OPTIMAL LEVEL IN ONE PURCHASE** [EV-499, C2]: *"If you cannot afford to build it at once, build each time one (or more) of the 8 side directly to its optimal level (eg North directly to 20)... **If you build a side only partially, the next time you will have to pay the full price to complete it.**"* A half-built stand is a trap — it must be finished in one go or you pay twice. And **skip the roofs**: *"No need to have roofs, it's only costly optics."*
- **The named optimal build** [EV-499, C2] — a concrete order for the whole project: **North 20 · North East 49 · East 26 · South East 45 · South 20 · South West 49 · West 26 · North West 49**, which reaches the 52-coin maximum *"at minimum cost (slightly more than 10000 coins)."* Each stand costs 900–1,300 coins when built straight to its target.
- **Never upgrade the same stand twice** — *"if you build a side only partially, the next time you would have to pay the full price to complete it."*
- **Max one stand at a time**, from the **lowest capacity stand to the highest**, and **leave one corner stand un-upgraded** — 7 maxed stands reach the top-division requirement; 8 overshoot it.
- **Never buy a roof on the highest level** — *"on the highest number you're paying for the roof and no extra seats."*
- **Downgrading was removed around DLS24.** Capacity, once built, is permanent — so build to the *division gate*, not to a design you like, because you cannot undo it.
- A fully completed stadium cost one player **5,625 gems and 10,000 coins**.

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

**The uniform facility-cost rule — and the correction it forces** [EV-468, C2]. The Accommodation facility's full ladder is published, and its first five levels are **identical to the Training ladder's**: 75, 150, 225, 300, 375, 450, 525, 600, 675, 750. So the facility gem cost follows **level N = 75 × N gems**, and the figures above are the cost of the **first five levels only** — **1,125 gems**, not a maxed facility.

- **Accommodation (the only other fully-published ladder):** 10 levels, **+4 squad space per level**, **4,125 gems** from zero. A legacy account that already maxed the old 40-player facility starts at 44 and pays **3,000 gems** for the last five levels — which lands on the current cap of **64 players** (44 + 5 levels × 4). **The corpus's earlier 40-player figure is a DLS24-era value and is now corrected.**
- **Where the old "5,625 gems for all five facilities" figure came from — and why it is stale:** a **DLS23-era** post (Dec 2022) reading *"each facility takes 1125 gems to reach max level, so to max all facilities you need 5625 gems"*. That was true when facilities had **five** levels. The ckpt-131 correction is a version correction, not a reinterpretation.
- **Correction to the corpus's old budget line:** "5,625 gems total for all five facilities" is a **five-level figure**. If the pattern holds, fully maxing one facility costs **4,125 gems** — and the real question is how many levels each facility actually has, which is published for Training and Accommodation and **unpublished for Medical, Commercial and Fanzone**.
- **Practical read:** the first five levels of any facility are cheap (1,125 gems) and the next five are expensive (another 3,000). **Spend the first five widely; be deliberate about the second five.** The community's "only Accommodation and Training are worth gems" advice now has a price attached: Training to L5 is 1,125 gems and Accommodation to L5 is 1,125 more, so both are affordable inside the first few seasons — while maxing either is a 4,125-gem commitment.

**Gem rule (hard):** gems go to **agents and facilities**, never to Form Boosts on low-rated players. The Form Boost baseline is 5g/+1, 8g/+2, 10g/+3 for **one match** [EV-428, C2] — that is a terrible rate at any stage.

**The official coin list** [EV-462, **C1**] — eleven sources, and **DLL wins are not among them**: winning matches, drawing matches, clean sheets, scoring goals, **stadium bonuses**, season objectives, Season Pass rewards, Prize Ladder rewards, final league positions, cup wins, and watching video clips. **Coins are a Career-and-cups economy; gems are the DLL economy.** That is the official mirror of the split the whole plan is built on, and it is why the stadium (a coin sink that pays coins) and the DLL climb (a gem source) are separate loops. Free coins officially come from **watching short video clips, subject to availability**.

**Free-to-play income stack (do all of these daily):**
- Daily challenges: **5–11 gems/day** [EV-433, C3]
- Scenarios: **50 coins daily**; 75–100 coins per 8-hour cycle [C2/C3]
- Ads: 30 coins per ad, up to ~600 coins in 15 minutes [EV-426, C3]
- Season Pass: **400 SP**, **40 SP/day login**, 10-day season; the **free track alone gives 1,095 coins + an Epic agent** [EV-399, C2]. **The cycle has changed across versions** — a 2021 thread reports *"the season pass restarts every week. So every week you have to invest money"* — so the buy-late advice below is calibrated to the **10-day** cycle and would be wrong against a weekly one [EV-516, C3]

**The structure is official, twice** [EV-492, **C1**]: a second FTG article (4404070913169), stamped *"applicable from our latest DLS release (version 12200 onwards)"* — i.e. DLS26 — confirms the split in FTG's own words, *"The FREE section is accessible to all users and the SEASON PASS section contains premium rewards which can only be accessed when purchasing the Season Pass,"* and confirms that purchasing *"unlocks the Progress Bank, which rewards currency based on your DLL (multiplayer) XP"* with the reward *"given at the end of the season."* It also states the purpose of the gold trim: *"to show off to other players."* **The per-tier reward list itself is not published by FTG and rotates every season**, so the only reliable read of the current track is the device at season start.

**The Season Pass purchase decision, priced** [EV-472, C2]. Two paid tiers exist: a **basic pass at about $4** (INR 399) and a **Premium pass at about $13–15** (INR 1,199 / $14.60). The original pass's full reward list was **4,000 coins, 150 crystals, 5 legendary form boosts, 3 legendary coaches (technical, fitness and GK), 1 legendary physio, 1 legendary scout and 1 legendary agent** — shop-equivalent about **£21.95**. The Premium tier adds: tiers unlocked to **Tier 8** immediately, **double Season Points and double Live XP**, a gold profile trim, a head start on the tier ladder, and better packs (a legendary agent plus 3 legendary scouts). Reviewers' verdict: *"almost the exact same"* as basic apart from the XP, and *"most suitable for a new player but not so much for a veteran."*

> **The mechanic that makes timing free:** *"you get to advance a SP level every 10 hours. If you don't play every 10 hours, the game will **store** the level so that you can advance multiple levels at once on a later time."* The free track's drip-feed is a **storage system, not a penalty** — and because a late purchase backfills every premium tier you already unlocked for free, **waiting costs nothing and buying early buys nothing extra.** **Buy the pass LATE in the season, or not at all.**
- Progression Bank: accumulates coins and gems from DLL XP over a **10-day season**, paid out in full at season end [EV-431, C2]
- Weekly DLL leaderboard: gems for **placement** *and* gems for playing a set number of DLL matches that week [EV-431, C2]. **Official cadence:** leaderboards *"reset at regular intervals (from 3-30 days)"* and pay by final position [EV-462, **C1**] — the 10-day Progression Bank season sits inside that range

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

### PHASE 3.0 — The facility ladder, confirmed and ranked [EV-490, C2/C3]

**The uniform cost ladder, now confirmed by a second independent source:** **75 / 150 / 225 / 300 / 375 gems** for levels 1–5, so **1,125 gems per facility**. Two sources quote the identical numbers.

**Accommodation is the only facility with more than five levels — it has ten** (75, 150, 225, 300, 375, 450, 525, 600, 675, 750 = **4,125 gems**), because squad size is the one benefit that keeps scaling.

**The Training facility's real ladder** [EV-499, C2] — and it converts the "Training is the priority" claim into a priced decision. **Each level unlocks a GROUP of formations** (level 1 gives one group, level 5 gives *"every group of formations in the game"*), and the gem discount is **5% at level 1, 10% at level 2, 15% at level 3**, flattening after that. The guidance that follows from it: *"this is also a great level to stay at if you're deciding to **use coins and coaches** to max players instead of gems"*, while level 5 *"is only ideal if you plan on maxing your team with **only gems**."* **So on the F2P route — where a max costs ~32,000 coins — Training level 1 is enough, and level 5 is a gem-spender's purchase.** There is also a **conflict to note**: the corpus carries a six-level 0/5/10/15/20/30% discount ladder, which cannot coexist with the twice-confirmed five-level 75 × N price ladder; the level attribution above matches the price ladder and is the one to plan on.

**The ranked priority order** [C3], and the arithmetic that justifies it:

| # | Facility | Why |
|---|---|---|
| 1 | **Stadium** | Capacity is a **hard promotion gate**; maxed it pays **48–52 coins a home match** |
| 2 | **Training** | Cheapens every coach — **23.33 gems/point at max vs 31.5 at L1** |
| 3 | **Accommodation** | Rotation, depth, and the 64-player cap |
| 4 | **Commercial** | +6% at L1, **kit/logo/scout discounts**, **rust removal at L3** — but only **10–20 coins a match at max** |
| 5 | **Medical** | −10% healing / −5% injuries at L1; maxed makes physio trips "super cheap" |
| 6 | **Recruitment** | Discounts agents **and** scouts (gem **or** coin cost) |

> **The comparison that settles it:** *"1125 Diamonds being used on the commercial facility for a bonus of 10 to 20 coins/match is not worth it knowing you can max 2.5 players with the same amount of diamonds."* **So 1,125 gems ≈ 2.5 maxed players ≈ 450 gems per maxed player.** Every facility decision is comparable to a coaching decision.

**The Fanzone has five levels** (two mod-site sources agree) — its **per-level cost remains unpublished**, which is one of the corpus's eight surviving gaps. **But its benefit is now precise** [EV-513, C3]: it grants **structural discounts on Stadium expansions** — not a general gem discount, a discount on the **sector builds that make up the capacity ladder**. So the Fanzone is priced directly against the ~10,000-coin stadium project, which is the comparison the corpus needed: **if it discounts sectors, it is a coin facility that happens to cost gems, and it belongs in the stadium conversation rather than the gem one.**

> **💰 THE F2P COIN COST OF A MAXED PLAYER:** **~32,000 coins via Common coaches** (80 releases at ~400 coins each) or **~30,000 via Rare** (20 at ~1,500), with an 80-rated defender available at about **1,460 coins**. This is the number that decides whether a free-to-play account maxes one star or keeps farming facilities — and it is why the **coin** engine matters more than the gem engine for squad building.

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

> **⚠️ THERE IS NO CHEMISTRY SYSTEM IN DLS26** [EV-479, C2 — documented negative]. A targeted search for a DLS26 chemistry system returned **only EA FC / FIFA chemistry models** (the 33-point club-league-nation link system) plus two AI-written DLS descriptions that use *"squad chemistry"* as filler. No DLS source documents a chemistry threshold, a chemistry UI, a link rule, or any attribute effect — in DLS the word appears **only** as an input to market quality (*"as your team rating and chemistry improve, higher-quality players will appear"*). **A player arriving from FIFA will hunt for a chemistry system that does not exist. Do not spend a single gem or squad slot chasing one.**

**Fastest refresh:** quit a **LIVE** match at half-time (or play the first half and forfeit).

**Lock Player — the paid answer to waiting:** spend **20 or 40 gems** to lock any player on the live transfer market for **24 hours**. They survive the next match refresh, a small lock sign appears on their card, and they vanish as normal when the period ends.

**Churning the market works too** [EV-479, C2]: a January 2026 guide advises *"regularly buying and selling players helps refresh the market, increasing the chances of higher-rated players appearing"* — the same idea as the match-refresh rule above, from an independent source, and the reason its tip 7 is *"Stay Attentive in the Live Transfer Market."* Note this is a **community** claim while the match-refresh table above is the corpus's better-evidenced rule: **play matches to refresh, and churn when you are actively hunting.**

**The filters include contract length** [EV-479, C2]: the market's search axes are **position, rating and contract length**. Contract length is therefore a *searchable* axis, not merely a display field — the corpus had nothing on wages or contracts before this wave, and this is the whole of what is documented.

**Starting out** [EV-479, C2]: new players begin with a **50–60 OVR** lineup, and returning players carry over **their squad and Academy Division status** from DLS25. Free transfers are *"usually players with low stats or players that you've released"*, while paid general transfers are *"normally better"*.

> **⚠️ THE PRICE BAND CORRECTED (ckpt-150, EV-488, C2).** The *"10 to about 900 coins"* figure came from an old fandom page and is **stale**. A December 2025 DLS26 thread shows a **secret player at 2,355 coins** after a discount from 2,555, and concludes *"we need at least 10,000 coins if we want to buy a player and still save money."* **DLS26 transfers run into the thousands. Budget accordingly, and do not plan a signing around a three-figure price.**

**PLAYER RECOVERY** [EV-488, C1 — official]: *"buy a sold player back within a limited time"*, via the **Recover** section of **Manage Players** — FTG's own wording is *"Players who were recently sold, appear in the 'Recover' section of 'Manage Players' for a limited time."* **It costs 5 gems.** A player sitting in Recovery does **not** re-enter the market rotation, which is why the community asks for a *"sell definitely"* option — and which is the mechanism behind the corpus's *"collection pieces never come back"* rule.

> **✅ THE RECRUITMENT CENTRE IS REAL — a SIXTH FACILITY (ckpt-150, EV-488, C2).** The v9.00 release notes read *"New facility - Upgrade your recruitment centre for Scout and Agent discounts"*, and DLS26 content still lists it. **The corpus's five-facility list was incomplete.** It discounts both recruitment tools, which makes it a genuine candidate in the facility ladder rather than a cosmetic extra.

**LOCKING WAS EXPANDED IN SUMMER SPOTLIGHT** [EV-488, C2]: *"Transfer upgrades - manage lock players in more ways than before"*, on top of the existing **20-or-40-gem 24-hour lock** that leaves *"a small lock sign on their card."*

**THE MAXED-STADIUM BONUS** [EV-488, C3]: *"stadium bonus rises to 48-52 coins per home match for 85k+ stadiums"*, averaging **~250 coins per match** after the post-match ad. That is the number the whole coin economy is built on.

**A SECOND SOURCE FOR THE TRAINING-FIRST GEM RULE, with its exception** [EV-488, C3]: *"all gems you earn should go to upgrading training center ONLY, unless you NEED to lock a player."* The same thread confirms the DLL gate — *"if you wanna... need gems (tier 10 and above only)... play live."*

**THE SUSPENSION WORKAROUND** [EV-488, C3 — era-stale]: *"If a player has a red card suspension, release him and buy him back from the Free Transfers Page."* It clears the ban but *"will erase your players records (goals, games played, etc) for the season"* — upgraded stats survive. **A last resort, not a habit.**

**New player-specific celebrations are arriving** [EV-488, C3] — a Mbappe corner-LED celebration after a hat-trick — but **celebrations are not player-controllable**, as a wish-list asking for exactly that confirms.

**Other rules that catch people out:**
- **Released players do reappear** — after a grace period during which you can buy them back from the release area. But **collection pieces never come back**, and rare/common cards may take a long wait.
- **No duplicates:** you cannot buy a player you already own. To get a new version of a card you must first sell the one you have.
- **Buy the highest-rated player at each refresh** — it raises team strength and attracts better players.
- **Legendary players** appear individually or as **Top Picks**, and land in the **~1,500–2,800 coin** band once your rating attracts interest.
- **CLASSIC PLAYERS ARE ON THE TRANSFER MARKET TOO** [EV-485, C2]: *"besides the prize ladder, Classic Players will also be available on the Regular Transfer Market"*, bought with **coins**. The corpus previously treated the Prize Ladder as the only Classic route — **it is not.** If a Classic you want is not on the current ladder, check the market before spending gems on agents.
- **The squad cap does not count special or classic players** [EV-485, C2] — three independent sources confirm *"all the new classic and star players will not be counted towards the main squad size."* Collect them freely.
- **Scouts:** Common 75 coins, Legendary 500 coins. The Common's legendary chance is **2% per one source and 5% per another** — unresolved, and the difference decides whether Common scouts are worth 75 coins.

**THE PROBABILITY LADDERS** [EV-486, C3] — the only complete figures on record:

| Tier | Ordinary | Talented | Legendary (80+) |
|---|---|---|---|
| **Common scout** | 93% | 5% | **2%** |
| **Rare scout** | 75% | 20% | **5%** |
| **Legendary scout** | 40% | 45% | **15%** |

**Agents guarantee their band instead of rolling for it:** Common = one ordinary player (below 70) · Rare = one talented player (71–79) · Legendary = one legendary player (above 80). **And agents skip the second purchase** — *"agents allow you to get players directly without having to buy them again"*, whereas a scout costs twice (once to scout, once to buy).

> **The efficiency case, as arithmetic:** *"12 Common scouts would involve an investment of 900 coins while on the other hand, 6 legendary scouts would eat up 3000 coins"* for the same legendary player.

**The grey-goalkeeper route** [EV-509, C3] — the coin alternative to the corpus's no-gems-on-GK-coaches rule: *"**Don't use gems for goalkeeper coaches... You'll find that it is much cheaper to spend coins on gray goalkeepers and then immediately selling them for goalkeeper coaches**"*, because goalkeepers are the cheapest players in the game. And a second rung for Rares: *"buy the cheapest legendary player in the transfer market (usually around **1400**) and then immediately release them for a rare coach."* **So the coin-only coaching ladder runs grey goalkeeper → 80-rated defender → 1,400-coin legendary**, with gems reserved for the facility ladder.

**THE COACH-FARMING LOOP, with its price band** [EV-486, C2]: *"Buy players under 180-210 coins and release for common coaches."* For unmazed squads, use **a 7:3 fitness-to-technical ratio**, then redo the players that end up badly after maxing. **What you get back is set by what you release:** an 80+ player yields a **Rare** coach, a sub-80 yields a **Common**, and a special player yields a **Special** coach. Goalkeeping coaches touch **only GKR and GKH**; Special coaches work **only on special players**.

**THE GEM RULE** [EV-486, C3]: *"Avoid spending gems on anything other than upgrading facilities or training special players."* As a starter, *"aim to buy players rated 68 or above."*

**THE PER-TIER POSITION BUILDS** [EV-503, C3] — the corpus had *ideal blueprints* for a **maxed** player; these are the recruitment targets you actually use when buying a Common, a Rare or a Legendary:

| Position | Common | Rare | Legendary |
|---|---|---|---|
| **Centre back** | 70+ SPE/ACC · 65+ STR/TAC | 75+ SPE/ACC · 70+ STR · 80+ TAC | 80+ SPE/ACC · 80+ STR · 90+ TAC |
| **Fullback** | 70+ SPE/ACC · 65+ TAC/CON | 75+ SPE/ACC · 80+ TAC/CON | 80+ SPE/ACC · 85+ TAC/CON |
| **Centre mid** | 75+ CON/PAS/SHO · 70+ TAC/STR · 65+ SPE/ACC | 80+ · 75+ · 75+ | 90+ · 80+ · 75+ |
| **Defensive mid** | 60+ SPE/ACC · 65+ STR/TAC · 60+ CON/PAS | 60+ SPE/ACC · 80+ STR/TAC · 70+ CON/PAS | — |
| **Second striker** | 65+ SPE/ACC/CON/PAS/SHO | 70+ · 75+ · 75+ · 75+ | 80+ · 85+ · 85+ · 85+ |

> **🎯 CB PACE IS THE TOP CENTRE-BACK STAT — and the reason is mechanical, not aesthetic:** *"Good pace is the most important stat for a CB, you can't chase forwards with a slow CB. And it is the most recurring occasion in DLS where a CB chases a forward."* So the centre-back is a **recovery position**, and a slow CB is a liability no matter how good his tackling or strength is. That single line should decide most CB purchases.
>
> **And against long-ball spammers, play a LOW fullback at CB** to chase the forwards down — a personnel answer to the long-ball problem, sitting alongside the C-spam and wing-spam counters. **Strength also slows forwards** on pressure, which is why it outranks shooting on any defender's build.

**THE CARD COLOUR TAXONOMY** [EV-486, C3] — worth knowing before you read any guide: **gold** = standard (better odds as you sign better players) · **black** = legends (Prize Ladder, a set window, usually ~80 days) · **purple** = Dream Stars (summer event) · **blue** = Champions (*"the most luck/p2w ones"*) · **orange** = maxed gold players.

> **⚠️ THE BLUE-CARD TRAP** [EV-509, C3] — colour is a **price** signal, not a quality one: *"Often the rare players that'll appear will be expensive and <75 OVR. **The blue cards may look appealing but they'll be at double the expense of 65-70 OVR common (silver) players and the attribute differences aren't that significant performance wise in matches so treat them as a trap.**"* The exception: *"**secret player offers will be of great benefit if they're >1.2k in cost.**"* So the market has a two-line rule — **take a discounted secret offer above ~1,200 coins, refuse an expensive blue card below 75 OVR.**

**THE 84+ PURCHASE RULE** [EV-509, C3], from two independent voices: *"**save money and wait for those 84-86 players**"* and *"**I advise you to buy only 84 and above players rating as they give the best chance of winning.**"* With the fan-buy caution: even a die-hard Messi or Ronaldo card is not worth buying now if *"their performance is not good as compared to other better players"* — buy it for the collection, not the win. **The market threshold behind it: good players appear around team rating 75, and the best ones once you hit 80** — so each purchase is a bid for a better market (*"buy the highest rated players every time the market refreshes, this will increase your team strength and accordingly you'll attract more better players"*). The cost of waiting is real: one player reports *"36 matches and still haven't gotten the player I wanted."*

**THE DREAM POINTS ECONOMY** [EV-486, C2]: **75–250 DP per match** depending on performance, with boost items at **+50%, +70% and +150%** and post-match ads for more. The **first Prize Ladder special player costs ~50,000 DP**.

> **⚠️ NO DERBIES AND NO FREE AGENTS** [EV-486, C2 — documented negatives]. Fixtures carry no rivalry weighting, and *"free transfers"* are only your own released players reappearing — there is no unattached-player pool. **A possible sixth facility (a Recruitment Centre that discounts scouts and agents) is flagged for device verification, not adopted.**
- **Release yields coaches, not coins** — this *is* the coach-farming loop.
- **The name lever [EV-492, C3].** The corpus carries a full method (CLAIM-1799): reach a team rating of **75+** (preferably 82+), set the manager **name and nationality** to the target player's, play 20–40 matches; if that fails, change the **club name** to the target's club. Wave 79 adds the ordering correction — **try the club name first, because it is free to change and costs nothing to test** — with a positive data point ("changed name to PSV and Manager to Xavi Simons, got him in 5 matches"), a nation variant, and two named community recipes ("exclusives", Lyon + the current Lyon manager or Dejan Lovren). Evidence is genuinely mixed and the corpus holds it at **Community Consensus**, so the posture is unchanged: **try it, do not plan around it.** It is a free option, not a dependency.

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
- **✅ C-027 — RESOLVED ON AN OFFICIAL BASIS (ckpt-126).** FTG's own support article *"How do the various player stats in DLS affect gameplay?"* publishes the full per-stat model, and it makes both community positions true at once: SPE's effect is **conditional** (it falls with energy, and falls when dribbling *inversely to CON*, so a lower-SPE player can outrun a higher-SPE one), while **CON, PAS and TAC each govern a possession action** (dribbling speed and touch quality, pass accuracy, tackle *distance*) and **STR** decides who keeps the ball in a collision. See **§4.2**. The community split — *"control, passing and tackling stats have more value than ever before"* [EV-455, C3] versus *"knock-ahead can outrun even maxed defenders"* — is the same model seen from two ends, so **recruit for both — a fast spine with a technical core** — and do not let the ×2 weighting talk you out of a genuinely fast defender. **Verify in Exhibition before committing a coaching plan** remains in force, because the community reports describe the current build's *tuning*, which the official article does not quantify.
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

### 4.2 The official stat model — what every attribute actually does [EV-456, C1 — OFFICIAL]

FTG opens the article by stating that DLS *"is a 'game' and is not intended to be a full and accurate simulation"* and that part of the game is discovering how stats affect it yourself — **but** that *"it is intended that the stats have a meaningful bearing on gameplay in line with real life strengths and attributes."* This is the closest thing to a design document in the entire corpus, and it is the reason §4.1's heuristics can now be replaced with mechanics.

| Stat | What it officially does | Coaching consequence |
|---|---|---|
| **SPE** (Speed) | Top-speed running. **Falls as energy reduces**, and **falls when dribbling, inversely proportional to CON** — *"it is entirely possible for a player with a lower SPE stat to run faster than a player with higher SPE stat, whether they are dribbling or not"* | Speed alone does not win chases. **SPE without CON is wasted pace** — this is the mechanism behind "100-paced players get locked up by 87 legendaries" |
| **ACC** (Acceleration) | How quickly a player **reaches** top speed | The catch-up stat. The "tackling is worthless if you can catch up" complaint is an **ACC** question, not a TAC question |
| **STA** (Stamina) | How quickly energy depletes when running, **and how much energy is restored at half time**. *"Impacts more on some positions than others"* — *"a centre-back will typically cover far less distance than a midfielder"* | **Weight STA by position**: high on midfielders and wingers, lower on centre-backs. Refines the flat STR/CON ×2 heuristic |
| **CON** (Ball Control) | Less speed lost when dribbling; **quicker kick after a first touch**; more touches closer together to change direction quicker; touches keep the ball closer; greater chance of **Rabonas, Overhead Kicks, heel-chops, skill shots and skill moves** (Step-over, Marseilles turn, Heel-Flick) | The technical multiplier **and** a speed stat in disguise. Gates every skill move — the "skill moves are swipes dependent on Ball Control" rule is now official |
| **STR** (Strength) | Collision impact: a higher stat means **less impact from a collision**, so better ability to gain/maintain control of the ball or complete a kick; also **shortens the stumble after being tackled** | Decides who keeps the ball in contact. The ×2 weighting is justified: STR is scored twice — once on the tackle and once on the recovery |
| **TAC** (Tackling) | Sets **the distance from which** a standing tackle and a sliding tackle can be performed | A **reach** stat, not a binary success stat. High TAC = you can tackle from further out; low TAC = you must be on top of the man |
| **PAS** (Passing) | Accuracy of passes — *"more accurate with all types of pass"* **AND charge time**: *"players with orange or red PAS will need to stop for a bit to perform a clean B-pass"* | Directly governs the possession game, and therefore the Tier-1 space model in §3.1. **A low-PAS player must stop to pass; a high-PAS player passes on the run** — and about **90% of defenders are poor passers**, which is why build-up from the back is slow by design and the long ball from a centre-back is the intended alternative |
| **SHO** (Shooting) | Accuracy for all shot types; controls how much **'assist'** moves a shot away from the keeper; **keeps shots down/low** (low SHO kicks shots higher and potentially over the bar); raises skill-shot chance (with CON); raises special kick/header chance (Overhead kick, Diving header); **increases the spin/curl on a free kick** | Low SHO skies shots — pair a finisher with a set-piece taker. **SHO also sets free-kick curl**, which refines §3.3's free-kick rules |
| **GKH** (Keeper Handling) | Handling and 'presence': more likely to **catch** a shot than deflect it; more likely to **claim a cross**; more **stable** when saving while players collide with the keeper | GKH is the claiming/crosses stat |
| **GKR** (Keeper Reactions) | Faster reaction time; better save chance relative to shot speed and save distance; chance of an **'anticipate' save** made without time to react | GKR is the shot-stopping stat — confirms the **GKR ≥ GKH** rule |
| **ENERGY** | Below a certain level the other stats **reduce gradually** as energy drops — *"most noticeable for player speed, but a tired player will perform worse in all areas"* | **Rotation and physios are stat protection.** A tired player is a nerfed player in every attribute, not just speed |

**Why this settles the coaching argument:** the model says speed is *conditional* (energy-gated, and CON-gated while dribbling) while the technical stats are *unconditional* possession actions. That is exactly the both/and build — **a fast spine with a technical core** — and it means the ×2 STR/CON weighting survives, the "speed is everything" rule does not survive as stated, and **STA should now be weighted by position** rather than flatly.

### PHASE 5 — Club value and Fan Approval

- **100% Dream Team/club value requires EVERY player maxed, including bench and reserves — about 23 players** [EV-433, C3; corroborated by EV-424/425]. A starting eleven of 99s with 100% fan approval was still stuck at 58.52%.
- **Fan Approval milestones:** *Mr Popular* at **75%** (500 XP) and *Fan Favourite* at **100%** (2,000 XP in DLS2018 / 1,000 XP in DLS Classic) [EV-433, C2].
- **✅ DOCUMENTED NEGATIVE (ckpt-126, EV-457):** a dedicated two-search sweep for any fan-approval mechanic returned **nothing**. Every "fan" result was one of four unrelated things — crowd **graphics/movement settings** (TikTok "secret settings to make your fans move", graphics-quality tweaks), **bugs** where fans do not celebrate goals (the sound plays, the visuals do not), the **Fan Favourite achievement**, and the **Fanzone facility**. **No source documents how to raise Fan Approval, and no plan may depend on one.** The only evidenced lever remains the one in the bullet above: 100% club value requires *every* player maxed including bench and reserves, so **Fan Approval almost certainly tracks total squad development** — treat maxing the full ~23-man squad as the strategy and the percentage as the readout, not the target.

### PHASE 6 — Special and Classic players (the 90-day engine)

- **Special Players cannot be bought with coins** — events, challenges and the Prize Ladder only [EV-426, C2].
- **Two routes:** (a) the **Prize Ladder** — first special at **~50,000 DP**, draw is **random**, first icon ~**300–324 games** with boosters, all four WC'98 icons ~**1,370–1,428 games** against a ~200,000 DP ladder; (b) **Legendary Agents** — every use has a chance of a **World Hero** Special Player [EV-426, C1 for the agent route].
- **WC'98 four:** Petit, Šuker, Bergkamp, Batistuta [C2].
- **Dynamic Stars** need Dynamic Star Agents from event draws and Season Passes (3 premium + 2 free) [C3].
- **Cult Heroes** (v13.430, live 16 Sep 2026) — the complete 12-player collection from **Cult Hero Agents**, available in **Events, Drafts and the Season Pass**: **de Gea 85, Aubameyang 85, Dybala 85** · **Insigne 84, Ziyech 84, Alarcón 84, Otamendi 84, David Luiz 84** · **Blind 83, Shaqiri 83, Herrera 83, Vozinha 83** [EV-459, C2]. **The complete route map** [EV-515, C3]: **6 from the three Season Passes** (2 each, one free + one premium) · **3 exclusively from Online Events** as top-tier PvP rewards · **up to 3 per Dream Draft** across 1 free and 2 paid drafts. **So the collection is obtainable without money through three separate systems** — and the official wording confirms all three.
- **Season Pass Players** — a new card type carrying *"special agents and players distributed across both the Free and Premium tiers"* [EV-515, C3]. **So the Season Pass now carries cards, not just consumables** — a new reason the pass decision matters.
- **TOTY (Team of the Year) cards are GREEN**, and named: *"TOTY Yamal & Pedri: the brilliant green cards"* [EV-515, C3]. **A sixth card colour outside the corpus's five-colour taxonomy.**
- **✅ C-018 RESOLVED (ckpt-127):** the 92-vs-95 conflict was **three states of the same card**. **85 = base** · **92 = the LIVE-EVENT BOOSTED rating** (App Store: *"now available with boosted attributes"*; the 92 reports are dated the day after launch) · **95 = fully maxed** (85 + the +10 coach cap). *Correction to the earlier roster:* **Isco was never in the collection** — it was a fan wish-list mention; **Francisco Alarcón** is the missing 12th player. **Planning read: Cult Heroes are the weakest special set in the game by ceiling (max 85 base)** — a community member predicted exactly that a month before launch: *"the highest stat is only 85, which is not strong enough to attract people paying."* Spend on them only if you want the card, not the rating. Sample stats: Luiz TAC 89 / STR 85 · de Gea GKR 85 / GKH 80 · Herrera STA 91 / PAS 86 / CON 86.
- **Classic Players:** unlock to sign with **500 coins**, or by completing the game (beating your own team after First Touch United); ratings 85–97 [C2]. **Confirmed above the roster ceiling:** Rivaldo 1999 and Matthäus 1991 are listed at 86, and Classic Marcel Desailly at 85 [EV-476, C2].
- **THE ROSTER RATING CEILING IS 86** [EV-476, C2] — held by a cluster of about six players: **Dembélé, Mbappé, Haaland, Kane, Yamal**, plus Bellingham or Valverde depending on build. Four independent sources across Dec 2025 – Mar 2026 agree. **This retires the rejected AI-farm figures** (Haaland 94, Vinícius Jr 91) with real data — and note a player's roster card and their special card can differ sharply: Aubameyang's roster card is 78 while his Cult Hero card is 85.
- **Dynamic Stars roster** (8 players, all from Dynamic Agents, all base 82): Laimer, Eze, **Nico Williams**, Barcola, Cunha, de Paul, João Félix, Woltemade — plus Kang-in Lee at 82 [EV-476, C2].
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

**🎯 A CLASSIC IS A MAXING PLAY, NOT A RATING PLAY** [EV-512, C3]: *"**none of them are 86 so none of them are gonna knock your socks off** or revolutionise the game, but they're nice enough."* The value is in what a Classic can be coached **to**: *"**You could probably make Desailly a 5x 100 defender**"* — five stats at 100 — and the named best first pick is a **defender, not a striker**: *"If you already are stacked with great strikers, I'd say your main man will be **Desailly**... potentially **5x 1000 with full fitness and full tackling**."* **So the Prize Ladder is the cheapest route to a genuinely maxed defender**, which is a different proposition from collecting cards. Each Classic also carries a **year** (Matthäus 1991, Rivaldo 1999, Pires 2002), so a card is a specific season's player. The current ladder is the **English League Classics** — Berbatov, Essien, Andy Cole, Petit — and the previous one was the **Midfield Classics** (Matthäus 86, Valderrama 83, Rivaldo 86, Pires 84), with one player reporting *"my Matthäus is kinda useless now"* after the rotation. **Most ladder players are recycled from older events.**

**The ladder's real time cost** [EV-512, C3]: a match plus its ads is **9–10 minutes**, and the extra-DP ads **stop appearing after a while** — so the ~145,000-DP final reward is roughly **250 matches, about 40 hours**. Set against the camping route's 35–43 gems an hour, that is the honest price, and it is why the corpus's tier-camping route outranks the ladder for gems. A genuine dissent sits beside it: *"**The real tip is: just don't care about classic players.** Play some matches for fun, just like you all used to do before prize ladder was a thing."*
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
| Reward ladder | **25,000 points** to unlock anything · **25 gems at 1M** · Legendary XP boost 2M · Legendary Scout 3M · 500 coins 5M · Rare Special Coach 7.5M · **150 gems at 10M** [EV-502, C3 — endpoints two-source, middle tiers single-source from a source rejected for tables] |
| The in-clan prize | **50 gems** for finishing first among your own clanmates — which is all the cap leaves you competing for |
| Clan value, weighed | About **275 gems a season** out of a total budget where DLL is **6,000** — so the clan is a rounding error against a 1,125-gem facility decision, and it is **competitive, not social**: members advertise "200k minimum each season" and clans target 7.5–8M, with leaders expelling anyone under 20,000 points in their first hour |
| Creation cost | **150 gems**; barely breaks even in season one |
| Active clan season total | **13–15M CP** (350k+ members); others target 8M; second-tier 10–11M |
| Reward ladder | 25k first reward → 25g @1M → Leg XP @2M → Leg Scout @3M → 500c @5M → Rare Special Coach @7.5M → **150g @10M** |
| Entry requirements | Hide a clan from search, **but an invite code still bypasses them** |
| Fanzone | Gives **clan bonuses + stadium discounts** — the official store copy reads *"Upgrade your Fanzone for Clan bonuses and Stadium discounts"* [EV-458, C1]; no per-level values published |
| Membership | **One clan at a time**; leadership passes on if the leader leaves, and the clan disappears if nobody is left [EV-456, C1] |
| Unlock | Clans open **once you have progressed far enough through the Ranks** [EV-458, C2] |
| Points sources | Matches, challenges **and Season Pass tiers** [EV-456, C1] — **plus clan-internal matches** [EV-478, C2] |
| Creation options | Badge (style, background, icon, frame colour, dressing), name, **country**, **minimum team rank**, and type (**open / closed / invite-only**) [EV-478, C2] |
| Leadership | One leader who is the **sole admin** and can remove members; a **vice-captain is appointed** by the leader [EV-478, C2] |
| Size | Minimum **50 members** [EV-478, C2] |
| Where to find it | The Clans tab on the **main home screen title** or the **top-right profile menu** [EV-478, C2] |

**Strategic read:** the 350k cap means the *clan* is the multiplier and *you* are the input. Joining a clan already running 13–15M is strictly better than building one, because the reward ladder is a clan-total goal.

**The cap's precise semantics (ckpt-140, EV-478):** the 350,000 limit governs your **contribution to the clan's total**. Everything you earn beyond it counts only toward your **personal ranking inside the clan** — and therefore the top-contributor reward — and *"won't help your clan's total points."* Once you have banked 350k, further clan points are purely a race for the top spot, so **stop treating clan points as a goal and start treating them as a by-product of the DLL climb**.

**Choosing a clan is a competitive decision, not a social one.** An active clan *"gives you not only extra rewards but also opponents at your level to measure yourself against"*, and competitive clans screen hard for it — real recruitment threads demand *"minimum 50 wins within the remaining time limit (5 days)"*, activity, Discord membership and *"no inactivity"*, and one leader's method is to prune *"anyone who doesn't contribute at least 20k Clan Points in the first hour of joining."* **Join a clan that is already at or near the member cap and already running 13–15M; do not build one.**

**Also new:** **clan-internal matches pay clan points** — playing members of your own clan is a legitimate point source alongside matches, challenges and Season Pass tiers.

**Corroboration (ckpt-126, EV-458):** the ~3,500-points-per-online-win figure and the 350,000 cap each now have a **second independent source** — a clan leader reports *"approximately 3.5k Puntos de Clan per online win"*, and a second thread confirms the 350k ceiling, adding that anything beyond it *"is not going to help your clan's total points"* but still ranks you first in-clan. At 3,500 points a win, **~100 online wins maxes a personal season** — so a player who grinds DLL for the tier climb banks the clan cap as a by-product, at no extra cost.

**⚠️ C-017 RE-OPENED (ckpt-126):** that same leader states the end-of-season top-contributor reward is **50 gems** — a **second community source on the 50 side**, against the earlier lean toward 100. The conflict is now **one source each side, neither official**. **Do not plan on either figure**; treat the 275-gem Clans line in the ledger as a mid-point estimate, not a commitment. It is resolved only by an in-client screenshot or an FTG support reply.

---

**The Career cup ladder** [EV-478, C2] — the sequence that sits above the divisions:

| Stage | Qualification | Opponents |
|---|---|---|
| **International Cup** (aka World Cup) | Win the **Legendary Division** | National teams — England, Sweden, Portugal, Argentina |
| **Allstar Cup** | Win the International Cup | Continental all-star teams |
| **Diamond Cup** | Elite or Legendary Division | Teams across continents — *"the final cup of the game"* |

Losing in the International Cup **returns you to the Legendary Division**, and every cup eliminates you on a concession — so a cup run is a separate discipline from the league, and the *league* is what pays.

**The World Tournament** [EV-478, C2] is the **new international-football event type** shipped in Summer Spotlight (v13.330, 10 Jun 2026; 13.350 on 14 Jul) — distinct from the Career International Cup, and the surface for the summer's **World Cup Heroes** (from 1 Jul), **World Cup Challenge** (30 Jun) and **World Cup Winners** (21 Jul) events. Treat it as a limited-time reward surface: enter when it is live, and do not restructure the plan around it.

**The Prize Ladder's current Classic roster is named** [EV-478, C2 — official TikTok]: the **Italian League Classics — Trezeguet, Batistuta, Crespo and Desailly** — obtained by earning Dream Points and completing the ladder. This is the first named current-cycle ladder in the corpus, and it confirms the ladder's Classic players are **themed by league and season**, so the roster rotates.

> **Special cards have unlimited accommodation** [EV-478, C1] — they never count against the 64-player squad cap, which is why collecting them is free in squad terms.

---

## 3. Matchcraft — the mechanical edge

These are the cheap, permanent wins that separate tier 2 from tier 1.

**Stamina management** [EV-422, C2]:
- **30% stamina regenerates post-match**; a **benched player fully regenerates**.
- The **60–70 minute substitution sweet spot** — bring subs on there.
- **⚠️ CANCEL THE AUTOMATIC CHASE-DOWNS** [EV-505, C3]: the game auto-chases *"when a goalie sweeps the ball in desperation or similar defensive efforts when players dish out under pressure"* — and each one burns stamina you did not choose to spend. **Cancelling it is a repeatable, free in-match stamina lever.**
- **⚡ THE STAMINA-CONSERVATION TRICK** [EV-505, C3] — it links the DP cap to the stamina economy: *"After scoring 5 goals, use a player with highest control stats to get ball. Keep the ball under your possession by dribbling the ball in a small area."* **Once you are five up there is no DP left to win**, so the correct play is possession with your best-CON player in a small area near the touchline. The match is already won; burn nothing.
- **Turning back is the easiest way to avoid AI tackles** [EV-505, C3] — the same principle as the planted-foot read, arriving from the defensive side.
- **A pace sub is for their defenders, not just yours** [EV-505, C3]: *"sub in high stamina + speed players in the second half to maintain the threat of a long ball all second half when the opponents defenders are tired."*
- **Physios are a scam — repair stamina individually** [EV-505, C3]: *"It's so much cheaper to just repair your players' stamina one by one"*, capped at **two players and 6–8 coins per match**. And **Team Boosts and Team Physios are the same 10%** — one is mid-game, one post-game, so the choice is timing, not value.
- **A tired start compounds** [EV-505, C3]: a player who starts below 100% *"will naturally become fatigued quicker."* So the sweet spot matters more than it looks — it is not just energy, it is the rate you lose it at.
- **3-sub limit** per match.
- Hidden daily fatigue was reported in an April 2026 review — if the squad feels heavy, that is why.

**Goalkeeping** [EV-424/425, C2/C3]:
- **GKH = positioning and catching; GKR = reflexes and rushing out.** Keep **GKR ≥ GKH** — an unbalanced keeper is wasted.
- Target **~190cm** height.
- Manual control: **hold C** to hold the ball; **double-tap** to drop it.
- In shootouts, the **dead-centre** tactic is the reliable save.

**The goalkeeper's actual model** [EV-496, C2/C3] — the corpus had the two-stat rule and not the model behind it:
- **GKR is the dive stat** — *"the higher the stat, the lower the rigidity of the keeper."* **GKH is the positioning, aerial and cross-clearing stat**, not just handling: *"GK catching the ball in the air, goalkeeper positioning all falls under GKH... GK with higher Handling also clears those Crosses and Corners from air better."* So GKR ≥ GKH is a *weighting* preference, and starving GKH costs you positioning and aerials — *"too low GKH is not appreciable."*
- **60+ Strength is a keeper constraint**: below it he *"fall[s] randomly whenever the opponent has the ball."* Above it he wins aerial balls. Treat it as a recruitment filter alongside the ~190cm height target.
- **The keeper auto-clears.** *"GK automatically kicks the ball away when it is between kicking range and opponent is in cue to win possession ahead of your defender."* So he can give the ball away on his own, and the manual sweeper-keeper role exists because of it.
- **Rushing is partly a per-player AI trait** — *"Some GKs have better rush system in built in game than others. Like Donnarumma rushes forward very quickly."* So the sweeper-keeper has to be driven by hand (hold C), and **rush late**: *"wait until they're almost to the box before holding it."* The yield is about **one goal saved every two matches**.

> **🎯 THE GK DOCTRINE: *"All Goalkeepers like to play dodge ball"* and *"never depend on GKs, keep them as a luck factor."*** So the keeper is **not a system you can invest your way out of** — which is the whole argument for spending on the defence and the facility ladder rather than on an elite keeper. Coach the back line; accept the dives.

**The outer-foot shooting technique** [EV-496, C3] — new to the corpus and the direct counter to the keeper's positioning: charge **B to 100%** for power, then **aim at the outer foot of the imaginary goalkeeper on the side you are shooting at**. He will dive sideways and your dead-centre shot goes in uncontested. This is the technique that exploits exactly the positioning stat GKH governs.

**Discipline** [prior waves, C2]:
- Yellow cards **accumulate**; **5 = ban**, with a warning at 4. A red card is an automatic ban.
- Injuries cost **3–10 games** at roughly **5 gems per game** to heal.
- Physios: Common +10% / 50 coins · Rare +20% / 100 coins · Legendary +50% and heals all / 200–250 coins (150 coins max in Medium).

**Set pieces** [C2]: require joystick direction held. Free kicks — aim above the wall and add curl. Penalties — a gentle tap with stick direction. Corners — outswinger, call a second player, max B.

**Form Boost usage** [EV-428, C1/C2]: duration is a **set number of matches gated by your Training facility level, minimum one match**. Because the exact per-level table has never been published, treat Form Boosts as a **one-match** tool and spend them only on a player who needs a specific rating threshold crossed *now* — never as a routine.

### 3.1 The tier-1 control model (the single highest-value section)

Every item below is community-consensus [EV-436, C2] and costs nothing to adopt.

**Attack — the two reading tricks a Tier 1 player actually uses** [EV-500, C3]:
- **Pass into the GAP, not to the man.** *"I visualize the defenders as moving cones, and see the correct passing lane, as the gap present between two defenders. Passes of this manner are difficult for my opponents to intercept, **because they don't know which of the two defenders to switch to.**"* So the pass is placed to defeat the switch — the attacking twin of the corpus's switching-delay findings.
- **Dribble at the PLANTED FOOT.** *"If a player has planted his right foot, his left foot is rendered near-useless, making his left side the weak side. So, if a defender is running towards me, I pass or dribble to the opposite side of his planted foot. He now has to turn around first... **As a result, I have gained maybe 0.5 to 1 seconds of extra time, and a yard of space.**"*
- **Build composure deliberately.** *"Actively seek guys who react faster than you, and play them"* — it forces care with every touch. The self-test: in the seconds before a free kick in the opponent's half, can you plan dead ball to a good shot in under five passes?

**Defence — the non-negotiable rules**

| Rule | Why |
|---|---|
| **Hold B and do NOT touch the joystick** | While holding B the player auto-moves to the ball; joystick input fights it |
| **Run players BACKWARDS** | The core fix for both wing-spam and C-spam. Do **not** tackle the outermost player as the ball is switched — that strands your players upfield. Switch to defensive mode and run backwards at every opportunity to concentrate the team in your own third |
| **Anti-C-spam: backwards-running central midfielders** | You will intercept the lofted passes; on intercept switch to attacking mode and counter |
| **Anti-C-spam, the LINE count as well as the defender count** [EV-500, C3] | After escalating 3 → 4 → 5 defenders, *"if your 4- or 5-defender formation had three vertical lines (e.g. 4-4-2 or 5-3-2), switch to one with four or five vertical lines, such as 4-1-2-1-2 or 5-2-1-2. This will utterly negate 95% of C spamming."* So the escalation is not only a number of defenders but a number of LINES |
| **Anti-cross-spam** [EV-500, C3] | *"Switch to 4-1-2-1-2 defensive. Once they get to the crossing stage, the only thing stopping them from scoring is poor composure or finishing - so cut them off before they get there."* |
| **Anti-central-play** [EV-500, C3] | *"Avoid vertically shallow formations like 3-5-2 or 4-4-2, as they will utterly slice up your midfield."* Central players *"excel at through balls"* — use 4-1-2-1-2, 3-4-1-2 or 3-2-3-2, which cover the middle vertically |
| **AUTO-SWITCH OFF is a top-of-the-ladder setting** [EV-500, C3] | *"You're gonna lose a little bit if you go straight away to Live Mode, especially Tiers <14."* So manual switching is right at Tier 1 and costly below it |
| **Secondary press > main press** | Use the secondary press so a *teammate* applies pressure while you position your player to block the pass or shot. The same applies in aerial duels — against C-spammers never hold the main press. **But it was nerfed in DLS26** — it won the ball ~80% of the time in DLS25 and is reported degraded or broken as late as January 2026. The specific failure: **the second presser freezes for a second on winning the ball and gives it back**, and the press commits only two players while the rest disengage. **Treat it as a bonus, not a system** [EV-506, C3] |
| **⚠️ DOUBLE-TAP TO CLEAR — the third defensive control** | Distinct from B (pressure) and A (slide): if your defender is in range of the ball, he **snaps to it and kicks it away instantly, with no possibility of a foul**. It beats B in traffic because B requires physical contact before the ball is won. **Strongest in box scrambles.** And keep it straight: double-tap *clearing* works, double-tap *shooting* does not [EV-506, C2/C3] |
| **Turn AUTO-SWITCH OFF** | The standard anti-C-spam setting. Practise in Career Mode first; it feels wrong for a while. **Official location:** Settings (gear icon, top-left) > Controls > *Auto Switch* — with default settings the game auto-switches control when defending to bring your closest player to the ball [EV-456, C1]. Given the DLS26 switching nerf, setting this deliberately is now a first-order decision, not a preference |
| **Never push defenders forward** | Use a DM to press in midfield; play zonal defending out of possession |
| **Block shots, and press C to bring the keeper out** | When the ball is in the air (lob or C-spam), press B and aim at the nearest midfielder/winger/fullback |
| **Slide-tackle sparingly** | Yellow-card risk; a ban costs you matches |
| **Switch tactics constantly** | DEFENSIVE when you cannot reach the ball in your own half (forwards track back, creating 2v1s), then ATTACKING the instant you win it |
| **⚠️ THEIR KICK-OFF IS THE MOST DANGEROUS MOMENT** | *"play defensive when they have kick-off. Kick-off is the most dangerous time."* The routine: **run at the player they are targeting and man-mark him with your forward**, while a second finger holds the secondary press on the receiver. Two fingers, two jobs, from the first second [EV-510, C3] |

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

**Skill moves are swipe gestures, not buttons** — and whether the move executes depends on the player's **Ball Control** stat plus the engine's decision [EV-441, C2]. A high-CON player is worth more for this alone. The three named skill mechanics in DLS26 are **Close Control, Knock Ahead and Secondary Press** [EV-455, C3].

> ### ⚠️ DLS26 CORRECTIONS TO THIS SECTION [EV-455, C3]
>
> Several rules above were built on DLS24/DLS25 behaviour and are **partly obsolete in DLS26**. Read them with these qualifiers:
>
> | Rule above | DLS26 status |
> |---|---|
> | **C-spam escalation ladder** | **Nerfed.** The "float to Haaland, head to Mbappe and repeat" loop has been *vastly reduced* in efficacy. Keep the ladder as a fallback, but do not expect ~95% negation. |
> | **Long B pass (the meta)** | **Qualified.** The diagonal "A" pass is **60–80% less effective**. Grounded diagonal B passes still work but are less dominant. |
> | **Secondary press > main press** | **Nerfed.** Secondary press was *"even too op"* in DLS25 and has been tuned down in DLS26. |
> | **Long shots >75% accuracy** | **Qualified.** Long-range effectiveness was reduced, though one review still finds long shots "very easy". |
> | **Through balls** | **Effectively do not exist** — *"line splitting passes are rare."* Do not build a tactic on them. |
> | **Player switching** | **Nerfed.** Expect 3–4 switches to find the right defender where DLS25 needed two. Switching also gets confused on loose balls. |
>
> **Two more DLS26 realities to internalise:**
> - **The game plays "loose."** Players no longer *snap* onto the ball; passes that used to be "close enough" are no longer collected; defenders watch the ball go past them; and **charging the keeper to cut the angle "does nothing now."**
> - **Responsiveness is the top mechanical complaint** — a direction change registers a touch late roughly 6–7 times in 10. Budget for it rather than fighting it.
>
> **Source-dating warning:** at DLS26 **launch**, passing was *"utter crap"* with a 100-rated passer feeling like a 42-rated bronze; two mini-updates later it reverted to the DLS25 feel. **Any DLS26 review dated December 2025 describes the launch build, not the current one.**

### 3.2 Injury and healing economics [EV-437, C2/C3]

- **Gem-to-games conversion:** 35 gems = 7 games out · 25 gems = 5 · 10 gems = 2 · 5 gems = 1.
- **Physio tiers:** Common +10% energy / ~50 coins · Rare +20% / ~100 coins · **Legendary +50% and heals ALL injuries / 150 coins with maxed facilities, 250 otherwise**.
- A **mid-game Team Boost** and a **post-match Team Physio** both restore 10% stamina; individual healing costs ~2–4 coins per player.
- **Maxed Medical Centre** makes physio trips "super cheap" — effectively endless playtime.
- Injuries last **3–10 games**; a **Fitness coach** can also help heal an injured player [C3].
- **THE INJURY-PROOF SUBSTITUTION EXPLOIT** [EV-457, C3]: *"players can't get injured if you don't have players to sub them off for."* Put 5 bench players in the first team, enter the match, then use all 5 subs before kick-off to bring the real XI on — no injuries can occur. **Cost: every substitution for that match.** Use it in Career when a fixture cannot afford an injury; never in DLL, where the subs are worth more than the injury risk.

**And the injury is undoable** [EV-515, C3]: *"I will just **close my game if my player got injured, then open it again. The game will resume at the last time stop before the injury** (goal kick, free kick, corner kick, throw in, or half time). **Can also work for yellow cards and red cards, but not for penalties.**"* So an injury, a booking and a sending-off can all be undone by closing the app — the second save-based undo alongside the Save Mode trick. **The exception matters: a penalty cannot be undone, so the shootout is the one moment where the record is truly permanent.** And if you keep the injury, the **games-out figure is readable on demand** — click the player, click heal, and a dialogue states the matches needed; a **Legendary physio heals all injuries at once and is cheaper than gems**.

> **⚠️ THE INJURY REPORT IS EPHEMERAL — READ IT FIRST** [EV-484, C2]. DLS *does* tell you the injury and the games out, but only in the moment: *"it's only visible after you exit the match where the injury happened. It's gone if you close the app or play another match."* The same text sits behind the gem-recovery button. **The instant a match ends with an injury, read the report before you touch anything else** — by your next match it is gone and you are guessing.

**Rest is a genuine recovery channel** [EV-484, C3]: resting a tired player for one match fully restores them — *"play one division match and sit out the most tired players. And they'll be fully fit the next match"* — and the half-time team boost accelerates it. Idle recovery scales with the squad: **3–4 hours for a weak team, about 20 minutes for a maxed one**. So a thin squad recovers slowly in real time, which is another argument for the Accommodation ladder.

**⚠️ FOUR CAREER-LIFECYCLE NEGATIVES** [EV-484, C2 — documented negatives]. A targeted search for player growth, aging, morale and retirement returned **only real-football research and other games' systems**:
- **No morale or dressing-room system** — nothing to manage, nothing to keep happy.
- **No player growth or potential curve, and no aging** — players do not develop with minutes and do not decline with age. **A DLS player is a static card that moves only when you spend coaches on it.** There is no career-mode development arc.
- **No retirement** — the only lifecycle event in the database is real-world.
- **No surgery or rehabilitation timeline** — injuries are healed by physios, rest or gems, full stop.

> A player arriving from FIFA will look for all four. **None of them exists here**, which is precisely why the coaching method in §4.2 is the only development lever in the game.

**Mid-season refreshes re-rate players** [EV-484, C2]: the January 2026 update applied *"January transfer movements and updated player ratings"*, moving for example *"Raya 83 > 84, Gabriel 84 > 85, Merino 79 > 80, Zubimendi 81 > 82, Trossard 79 > 80."* **A card you hold can be re-rated mid-season** — relevant if you are holding players as assets rather than playing them.

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

**Two caveats:** DLS25 **nerfed corner headers**, so the fallback is to aim middle and press **B to pass** to someone better placed rather than heading immediately. And the **short corner** is a real option when crossing into the crowd fails — hold **B** to the nearest player outside the box and set up a long shot.

**The near-post post-to-post routine** [EV-507, C3] — for the corner hit too deep to head directly: *"C pass it lightly to the other side of the post to another player who can head it in with an A shot. **This makes the keeper have to run post-to-post twice** and you can easily score near-post."*

**Defending them** [EV-507, C3]:
- **Set the header up BEFORE the ball arrives, not after.** Switch to your tallest defender, drag him outside the box, and hold **B** while he moves — do not wait for the ball to be in the air.
- **Point the aim marker AWAY from the ball's trajectory** — toward the sideline of the *opposite* corner — then hold B. One source reports it *"works 4/5 especially if you have tall center backs."*
- **Free kicks:** put a player on the goal line before the kick; he is auto-switched to quickly, and the **double-tap "trick shot"** produces an immediate goal-line header (CLAIM-1295).

> **⚠️ THE FOOTEDNESS QUESTION IS CONFUSED EVEN INSIDE SINGLE SOURCES** [EV-507, C2]. One commenter writes *"your right footed players should always take right corners... **the mistake yall do with corners is making your left footed players take right corners**"* — and then, a few lines later in the same comment, *"**use a right footed player when taking the left corner and vice-versa.**"* Both arrangements, one source, no acknowledgement. **That is the clearest evidence yet for C-022's resolution: the two camps were never describing two opinions, they were describing two deliveries** — and even individual players hold both without noticing. Do not let a single confident source settle it for you.

**Free kicks — the three mechanics the corpus was missing** [EV-500, C3]:
- **THE AIM-OFFSET PRINCIPLE, which explains every other instruction:** *"The effects will start after you don't aim on the line from your player to the center of the goal. Whatever direction."* **A straight-on free kick is a straight shot; all curl comes from aiming off that line.** A right-footer aiming right gets an out-swinger, a left-footer gets a transverse — and the mapping flips when the angle changes.
- **THE 70% POWER FLOOR:** *"Use at least 70% of power... now anything below 70% isn't guaranteed to go over the wall."* (One dissenting voice prefers 50–60% and calls them luck-based; the 70% figure is the more recent and specific.)
- **POWER BY DISTANCE:** *"3/4s at 30 yards or 2/3s at 20, 25 yards."*
- **TWO DEDICATED TAKERS**, one left-foot and one right-foot, kept permanently — and **learn each one's curl**, because it is a per-player property: Ødegaard and Trent Alexander-Arnold curve heavily, Vinícius and Modric shoot straighter. **A left-footer is worth a slot on his own** because he can take from both sides without trouble.

**✅ C-022 RESOLVED (ckpt-137, EV-475) — the footedness conflict was two camps describing two different deliveries:**

| Delivery | Foot | What it does | Use it for |
|---|---|---|---|
| **Out-swinger** | **SAME foot** — right-footed on the right corner, left-footed on the left | Curves **away** from goal, so the header is played back toward goal with pace and the keeper **cannot claim it** | **The DLS26 near-post routine** — *"aim it near the goal post and it's money from there"* |
| **In-swinger** | **OPPOSITE foot** — left-footed on the right corner | Curves **toward** goal, suiting near- and far-post headers, but the spin brings the ball **to the keeper** | Real-football default; the professional game runs 2,643 inswingers to 541 outswingers |

**One r/DLS thread contains both positions side by side**, which is the conflict in miniature — and neither is wrong. **Adopt the out-swinger (same foot) for the near-post routine the table above describes**, and keep an in-swinger taker as the alternative when the near post is blocked. **The out-swinger technique:** call a second player first (it drags a defender out and opens space for your striker), set the taker to out-swinger, then **max B** and shoot.

**Free-kick footedness inverts the corner logic:** a **left-footed taker is the more versatile free-kick option** — *"on the field's right side, the right footed player will have a little turbulence to shoot. The left footed player can do both sides with no trouble at all."* A **both-footed striker** is structurally better because foot affects curve, power and accuracy from every angle.

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

**The two newest techniques** [EV-508, C3]:
- **Aim is set by where you FINISH, not where you start.** A player who went from missing every penalty to scoring 8/10: *"I would aim to the left and hold for a second then I switch to the right and tap A."* So the stick movement during the tap is the aim — which is the mechanism behind the corpus's hold-the-joystick rule.
- **Break the keeper's pattern, not just his dive.** *"Go middle for 4-5 straight games and then change side once in the sequence — then the penalty is less likely to get saved."* One player reports not missing a penalty for four months after adopting it. **This is the only penalty advice in the corpus that is about the opponent's memory rather than your own input.**
- **The taker's SHO changes the target:** a low-SHO kicker should aim at the keeper's **body**, a natural shooter at his **outer leg**, with a **40% A-kick power load** for maximum trajectory.
- **And down the middle is a scoring shot, not a safe one:** *"In DLS live always hit right down the middle. Works 10/10 times"* — because the keeper dives.

> **🎯 HEADERS ARE THE REPORTED WAY THROUGH A P2W SQUAD** [EV-508, C3]: *"Place the arrow on your corners slightly inside the default direction and hold C to 2/3-3/4 power and **50% of the time it's a free goal. Headers are one of the easiest ways to score against p2w players on dream league live.**"* **That is a direct answer to the corpus's maxed-squad-handicap concern: if the handicap is real, the corner header is the reported way through it** — which makes the corner routine a competitive tool, not just a scoring one.

### 3.4 Scenarios and Exhibition [EV-445, C2/C3]

- **Scenarios:** you are already **losing** and must beat **Hard AI**. 50 coins daily, resets each day. DLS26 Summer Spotlight officially added *more bonus objectives and rewards*. The community calls scenarios **the hardest content in the game** — "way harder than Live Games", and even "easy" scenarios reportedly play at medium difficulty. Budget time accordingly. **DLS26 raised the difficulty further** — "have you also noticed how ridiculously hard scenarios has become?" [EV-495, C3] — so price the 50 coins against several attempts, not one.
- **⚠️ A LIMITED-TIME SCENARIO REPLACES THE DAILY ONE** [EV-510, C3]: *"you don't get normal scenario until limited time scenario is over or you use your all 3 chances."* So the 50-coin routine is **not guaranteed** — an event can take it away, and the event can demand *"4 goals in 45 minutes with half tired team with rare players."* Some scenarios also require **winning by a 3- or 4-goal margin** — one player was asked to turn 2-2 at the 57th minute into a four-goal win.
- **The scenario levers** [EV-510, C3]: **keep passes under 40% power** (*"any pass above 40% power no matter how accurate, will get stolen"*), expect the AI to collect loose balls from metres away, and use the shape that works — *"pass around the halfway line to your wingers, it opens up so much space."*

> **⚠️ DLS DOES NOT DOCUMENT ITS REFEREE MODEL** [EV-495, C2 — a methodology finding]. A search for DLS referee, card and penalty rules returns **only** real-world football law — IFAB Laws 5 and 12, the 2026/27 VAR protocol, Premier League VAR guidance, MLS and ASL disciplinary codes. Not one DLS-specific source. So the corpus's two referee rules (**five reds ends the match · five accumulated yellows = a one-match ban**) are the best available, and **any DLS "rule" that reads like the Laws of the Game has been imported from real football and is not evidence.** Recorded so no future research wave repeats the search and mistakes football law for game documentation.

**What Hard mode actually is** [EV-495, C3] — the corpus had the official selector and the handicap perception but not the characterisation: *"Hard mode is basically DLS without all the random and stupid gameplay. In hard mode teams play like actual teams to an extent."* Only **Medium and Hard** exist since DLS25 cut Easy and Very Hard (DLS23 had four, paying 25/50/75/100 coins). The reported handicap **intensifies in larger stadiums** as well as on Hard — which couples the difficulty question to the capacity gate, so test it before maxing the stadium.
- **Exhibition:** offline friendlies via a **room code**, no rewards. This is your **free training ground** — the right place to drill corners, free kicks and new formations before taking them into Live.

**The defending model — four independent sources agree** [EV-474, C3]:

| Rule | Detail |
|---|---|
| **Do not use the joystick while holding B** | Your player moves toward the ball automatically; steering fights the mechanic |
| **Never push defenders forward** | Hold the line; a DM does the pressing in midfield |
| **Zonal out of possession** | Cover lanes, do not chase the ball |
| **Slide tackles sparingly** | *"A slide tackle can do wonders but don't do it too much especially when an attacker is pushing your defence in a counter"* |
| **Press C for the keeper** | And block shots rather than diving in |
| **Switch to defensive tactics the moment they have the ball** | Then attacking the moment you win it, balanced to reset — **a rhythm, not a setting** |
| **Aerial ball: press B at the nearest midfielder** | Not at the striker |

**The anti-C-spam escalation ladder** [EV-474, C3] — the one situation where a big back line is correct. Two strikers running at you: **head diagonally, backwards and slightly toward the second striker** — you either win it back to a defender or neither of you gets it (switch fast and collect). Still losing? **Escalate the back line: 3 → 4 → 5 defenders.** Against a dedicated C-spammer, five at the back is the answer; as a default it is not.

**Footedness placement** [EV-474, C3]: **left-footed at LB/LCB, right-footed at RB/RCB** to get balls down the wing; **strikers inverted** (left foot on the right, right foot on the left). Place your squad by foot before you spend a single coach.

**The one-on-one** [EV-474, C3]: **hold C for a few seconds before releasing** — it lowers the chance of them scoring and helps prevent chip shots. Always take the half-time boost, and never drag a defender out of position.

**Formation meta is genuinely unsettled — and the best analysis says it cannot be settled** [EV-464, C3]. The strongest piece of formation writing in the corpus argues the game *"doesn't have a strongest shape"* and that what differs is each shape's **failure mode**: 4-2-3-1 **"fails gracefully"** (you get overrun slowly and can see it happening), while 3-4-3 concedes two in ninety seconds and forces a full rebuild.

| Shape | Use it for | Its failure mode |
|---|---|---|
| **4-4-2** | **Learning, balance, and the default.** *"Two banks of four, two up top, no clever ideas. Nothing brilliant happens. Nothing catastrophic happens either"* — the recommendation for anyone losing right now: put it on and don't touch it for twenty matches | Least upside; relies on LM/RM tracking back |
| **4-2-3-1** | **Tier 1**, where opponents attack better — one extra defensive mid. Tier-1 players report switching to it on the climb | Lone striker gets no support; punished by long balls |
| **4-2-2-2** | **Live/online** — two strikers, two CAMs wide, two CDMs and a back four. Rising because DLS25 **nerfed 4-1-2-1-2's two wide mids** so they no longer defend and now play centrally | Thin in midfield if both CAMs push on |
| **4-1-3-2** | A dedicated Tier-1 guide: four defenders, a midfield diamond with one DM, two strikers — *"doesn't even require all the best players"* | Diamond is narrow; wide areas exposed |
| **3-2-3-2 / 3-2-3-3** | Closing the middle (two CDMs) and tiki-taka; the C-spam counters | Concedes fast when broken; no full-backs |
| **4-3-3** | **Most goals scored** per the shape-testing evidence | **Concedes the most** — wide forwards don't track back |
| **Five at the back** | — | *"Usually not a good idea"* online |

**THE VARIABLE THAT OUTRANKS THE SHAPE** [EV-464, C3 — and it is the official STA model from §4.2 arriving here]: *"Stamina depth beats formation, every time — a 4-3-3 with fresh legs at minute 70 beats a 'perfect' 4-2-3-1 with three players at low stamina."* **Rotation and fitness are tactical decisions, not chores.**

### 3.5 The in-match tactics surface [EV-487, C2/C3]

**⚠️ A FORMATION CHANGE TAKES EFFECT ONLY AT KICK-OFF.** *"Each change will only take effect on resets during kickoffs. Goal kicks, free kick pauses, or sending the ball out of bounds will welcome substitutions but not formation changes."* So you can sub at any stoppage but you **cannot** change shape mid-flow — set it, then wait for the restart. Confusing the two wastes the change.

**You start with two shapes:** **4-4-2** by default and **4-1-2-1-2**; everything else is gated behind progression (the Training Centre's formation unlocks). So the "4-4-2 for twenty matches" advice is also the only thing available to you early.

**Six Live strategies** [C3], from a player who climbed DLS22–26: **no blind C passes · dribble while stopped · long B passes (the meta) · backwards running for defensive play · call out the GK when necessary · no blind shots.**

**THE FORMATION DECISION RULES** [EV-493, C3] — the corpus had a catalogue and not rules, and these are the missing half:

| Rule | Detail |
|---|---|
| **Run it for thirty matches** | "Pick one shape... Run it for **thirty matches**. Not five. You cannot evaluate a formation across five games because the variance in this game is enormous and you'll conclude whatever the last result told you to conclude." |
| **Change width before you change shape** | The cheapest diagnostic. Narrow and wide are different games with the same eleven players. |
| **Change personnel before you change width** | So the diagnosis order is personnel → width → shape, and the shape is the last thing to move. |
| **Stamina depth beats shape, every time** | The high press (4-1-2-3) is "excellent if your squad has the stamina for it and miserable if it doesn't, which is the part the videos skip." |

**Why 4-4-2 for a new player, with the reason rather than the ranking** [EV-493, C3]: *"Two banks of four, two up top, no clever ideas. Nothing brilliant happens. Nothing catastrophic happens either, and when you're learning, the second one matters far more than the first. You get a defensive shape that holds itself together without you thinking about it, which frees you up to learn passing weight and when to press — the two things that actually decide games at every level of this game."*

**The anti-wing tactic, refined** [C3]: *"the trick is to NOT try and tackle their outermost players as they switch the ball. This will leave your players stuck up the field. Instead, switch to defensive mode, and run your players backwards at every opportunity."* **Retreat; do not chase** — which is the same conclusion the escalation ladder reaches from the other direction.

> **⚠️ THERE IS NO IN-MATCH TEAM-INSTRUCTION SYSTEM IN DLS** [EV-487, C2 — documented negative, **narrowed at ckpt-156**]. No source documents in-match team instructions, a mentality slider, tempo, pressing intensity or marking styles. Every guide describing those is Football Manager or EA FC. **DLS gives you a formation and an attacking/balanced/defensive switch, and in-match that is the entire tactical surface.** A player arriving from FIFA or FM will look for sliders that do not exist.

> **⚠️ BUT THE FORMATION EDITOR DOES HAVE A WIDTH SETTING** [EV-493, C2 — **C-030 opened at ckpt-156**]. Two corpus claims already said so (CLAIM-0454, C2), and wave 80 supplies a **third independent source**: *"Width settings quietly change everything. Narrow your shape and the same eleven players play a completely different game... If a shape isn't working for you, change the width before you change the shape."* So the negative above was **over-broad** — it listed "width or depth controls" among the things that do not exist. **The reconciliation is a surface distinction: width is a pre-match property of the shape, not an in-match instruction.** Device-verifiable in one minute: open the formation editor and look for the option. Until verified, **change width before you change shape** — it is the cheapest diagnostic available.

> **⚠️ NO IN-MATCH FORMATION FLUIDITY** [EV-487, C2]. The claims of "Tactical Presets" switching between shapes *"on the fly"*, custom tactics you can save and share, and a "3-5-2 Fluid" formation are uncorroborated — and *"on the fly"* switching directly contradicts the kick-off rule above. The related claim that *"the A.I. learns from your playstyle"* and *"the opposing manager switches to a compact 4-4-2 mid-game"* is **refuted by FTG's own article**: *"there are no additional overlaid controls to manage the difficulty experience."*

**Pick one and learn it deeply rather than chasing the meta** — the record run to Tier 1 used a mostly common/rare squad. **And carry the dissent:** one experienced player says *"**Never use 4-2-3-1, if you can. Striker has zero support all the time, and still punished by long balls**"* — a genuine disagreement with a Tier 1 player's own preferred shape, recorded as a dissent rather than smoothed into consensus. The corpus's own C-014 explains it: shapes differ by failure mode, and 4-2-3-1's failure mode is an isolated striker. **The shape that works with a weak squad is 4-5-1** — *"It can work even if your lineup still has a lot of white/common players"* — best used reactively to preserve a score. The conflict in miniature: two YouTube videos in the same spring assert opposite conclusions (4-3-3 in March, 4-4-2 in May).

### 3.5 The control model and the complete skill catalogue [EV-480, C2]

**The three action buttons are context-dependent** — in possession they **pass, shoot and cross**; out of possession the same three become **press, tackle and change-player**. The layout is customisable from the options menu (button size, movement-stick position), and **the shooting assistant can be disabled**.

**The three kicks** (two independent sources agree):

| Kick | Use |
|---|---|
| **Low Kick** | Low, short, precise passes |
| **Hard Kick** | Shots and long-range through balls |
| **Lofted Kick** | Long-ball passes and chipped goals |

**The complete skill catalogue** — the corpus's first full input list:

| Skill | Input | Use |
|---|---|---|
| **Rainbow Flick** | Swipe **UP** while running | Lift over a defender — needs **Control above 80** |
| **Feint** | Swipe **LEFT/RIGHT** while running | Change direction |
| **Roulette** | Swipe **DOWN** while running | Shield and turn — needs **Control above 70** |
| **Bicycle Kick** | Double-tap **in the air** | Finish crosses |
| **Scorpion Kick** | Double-tap in the air | Rare finish |
| **Heading** | Double-tap **under the ball** | Headers and clears |
| **Rabona** | Rainbow Flick → **B/C** | Fancy cross |
| **Close Control** *(DLS25/26)* | **Tap and hold** in empty space while in possession | Tight dribbling — *"for more controlled dribbling"* (official) |
| **Knock Ahead** *(DLS25/26)* | **Tap** while in possession | Fast breaks |
| **Secondary Press** *(DLS25/26)* | **Tap and hold** while defending | Double press — corroborates §3.1's defending model |

**Skill moves are gated by the Control stat** — below the threshold the player *"will just lose the ball."*

**Where to learn them:** **My Club → Training → Free Practice**, and the **Advanced Tutorial** that teaches every skill sits inside the training mode from the club screen. The training mode offers six modules: **Free Training, Free Kick, Left Corner, Right Corner, Penalty, Penalty Save** (an era-stale source, but corroborated by the corner drill in §3.3).

**Technique:** *"Combine your swipe with your joystick… time it so that you flick your joystick and change the direction of the run WITH the skill move"* — it raises the chance of losing the ball, but beats the defender outright when it lands. Skill moves pay most **in a one-on-one with the keeper**, where they give *"a bit of a speed boost"* and distance from recovering defenders.

> **⚠️ DLS's skill set is deliberately SMALLER than FIFA's.** A player arriving from FIFA will look for elastico, trivela and the rest; they are not in this game. **Learn these ten and stop looking.**

### 3.6 Economy mechanics the corpus had missed [EV-481, C1/C2/C3]

**The official gem sources** — the only Confirmed-tier list in the corpus:

| Source | Note |
|---|---|
| **League objectives** | Per-league goals |
| **Tournaments** | Cup runs |
| **Season Pass** | Free track included |
| **Prize Ladder** | The 90-day cycle |
| **Dream League Live** | Participation, not just placement |

FTG's own wording adds *"(please seek the bill payer's permission)"* before the shop — a parental-control note worth repeating: **if someone else pays for the account, ask before buying.**

> **⚠️ THERE ARE EXACTLY TWO CURRENCIES: COINS AND GEMS.** A kit guide claims the custom-kit unlock costs *"300 Diamonds, which is the premium currency"*, and one Season Pass reward list mentions *"150 crystals"*. **Every source that says "diamonds" is a scam site or that one discredited guide** — the same source already rejected in C-012. **Crystals appear exactly once and are unverified. Do not plan on a third currency.** (C-028)

**Three objectives arrive before every match** and each pays coins — *"score in the first half"*, *"receive a limited number of goals"*, and similar, with more across the season. **Read them before kick-off; they are free money attached to matches you are playing anyway.**

**Commercial is the kit-and-logo facility.** Beyond the coin bonus, a 5-star Commercial upgrade earns **kit discounts and logo discounts**. That is the real argument for levelling it — one guide's advice to spend *"your first 75 Gems"* there conflicts with the Training-first priority below and is recorded, not adopted.

**Bank Common coaches.** Community advice is explicit: *"do not waste gems on agents and coins on scouts"*, and *"save coaches even commons because the next promo will probably be good."* The Training facility *"will save gems after 20 uses"* — the same conclusion the corpus reached from the cost ladder.

### 3.7 The customisation layer, and the wages negative [EV-482, C1/C2]

Everything cosmetic sits at **My Club → Customise**, across five tabs — **Kit, Logo, Team Name, Players, Manager** — with the buttons named **CUSTOM LOGO** and **CUSTOM KIT**.

**The official 11-layer kit template map** [EV-482, C1] — the fact that makes custom kits work:

| Layer | Region | Layer | Region |
|---|---|---|---|
| 1 | Shirt body | 7 | League badge |
| 2 | Sleeves (short) | 8 | Kit logo |
| 3 | Sleeves (long) | 9 | Shirt number colour |
| 4 | Socks | 10 | Short number colour |
| 5 | Shorts | 11 | Shirt collar |
| 6 | Club badge | | |

> **⚠️ "The logos are added to the shirt from the .png, and if none are specified then none will display."** A kit whose badge region is empty shows **no badge** — this is the single most common custom-kit failure, and it is why a downloaded kit can look wrong even when the colours are right.

**Layers 9 and 10 are not artwork** [EV-492, C3] — the shirt-number and shorts-number regions are **colour swatches the game reads** to render the squad numbers, so the colour chosen there decides whether your own players' numbers can be read on the pitch. Inside the Kit tab the editor exposes five independent colour slots — **Primary, Secondary, Sponsor, Trim, Shirt Number**. **Shirt creases are generated automatically at import**, and imported logos are deleted with **the reset button at the top left of the Edit Logo screen**.

**The import rules:** PNG only, **512×512**, **transparent background** (a JPEG loses the alpha channel and the badge edges and sleeve cutouts break), and **layers stay separate** — front, back, sleeves, shorts and socks are discrete assets, so a merged full-body PNG *"will misalign or crop unpredictably."* The image must follow the official template layout; smaller looks pixelated, larger may be auto-resized and blurred.

**The workflow** [C3]: take a kit, paste the logo on with any image app, host the PNG anywhere public, and paste the **direct URL** into the game. DLS fetches by URL and wants a direct PNG link, not a download page.

**Four kits** — home, away, third, goalkeeper — with a pattern vocabulary of **none, sides, halves, stripes, hoops** (3–30 stripes). **Manager customisation** is cosmetic: hairstyles, outfits and accessories, with the North American themed **Manager Accessories** arriving in Summer Spotlight. **Licensed club kits update with the real season** — August 2026 brought the official 2026/27 designs.

> **⚠️ DLS26 HAS NO WAGE SYSTEM** [EV-482, C2 — documented negative]. No source documents wages, salaries, a wage bill, or contract renewal costs; the only wage-adjacent hit on the open web is a rant about the game's own price. **A player arriving from FIFA will hunt for a wage bill that does not exist — there is nothing to balance.**

**Discipline** [EV-485, C3]: **five accumulated yellow cards earns a one-match suspension**, with a warning icon on the player at four. There is no cross-competition accumulation to track and no appeal.

**The News System is FTG's info hub, not a news feed** [EV-485, C2]: *"Get the latest DLS info, all in one place."* A community wish-list asking to *"bring back news system like in DLS 22 (transfers, injuries, debuts, retirements)"* confirms the two are different things — **do not expect simulated transfer or injury news.**

> **⚠️ THE SWITCHING DELAY** [EV-485, C3]: a September 2026 review reports *"a .5 to 2 second delay when switching… Offense can take advantage usually by dribbling sideways or c spamming,"* and that DLS25 had better input responsiveness. dlsmod claimed in December 2025 that the auto-switch bugs were solved — **either it regressed or the fix was partial.** This matters directly to the defending model in §3.1: switch early, not late.

**Absent by public request** [EV-485, C2 — documented negatives]: players are actively asking FTG for home-and-away legs in tournaments, player accessories, a home-and-away league format, Bundesliga and Ajax licences, a Player of the Season award, a DLS22-style news feed, fog and cloudy weather, post-match interviews, VAR animations, stand-decoration customisation, and animated training drills. **Each is a feature DLS26 does not have.**

### 3.8 The stadium's design surface [EV-480, C2]

Beyond the capacity ladder in §2, the stadium is a cosmetic sandbox:

- **Seven named pitch patterns:** Horizontal stripe, Vertical stripe, Check, Diagonal A, Diagonal B, Diamond, Circles. **All cosmetic** — *"only a cosmetic upgrade."*
- **Eight named sectors:** North, North East, East, South East, South, South West, West, North West Stand (2 Ends, 2 Sides, 4 Corners). **Seat colour follows the home kit.**
- **Advertising boards** run in every sector except the corners and the players' entrance, and **some structures carry zero seats** — they add appearance, not capacity.
- **Auto Build Capacity** sets an exact seat target and shapes the stadium automatically (ceiling 80,000 of a 90,456 maximum).
- **The stadium is modular** — FTG's asset folders classify sides, corners and ends as independent packages, which is why the sector ladder behaves as it does.

**Build order:** *"Don't build the roofs, just until you reach max spectators"*, and upgrade **one stand at a time** — levelling every stand together is more expensive.

> **Documented negatives:** DLS26 has **no controller support** on mobile and **no gem-based injury healing** — *"wait it out or use medical staff."*

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
| Building a stadium design you like before the division gate | **Downgrading was removed around DLS24** — capacity is permanent, so a 34,000-capacity ground built for looks will block promotion until you pay to raise it [EV-460, C3] |
| Upgrading a stand **with a roof** | "On the highest number you're paying for the roof and no extra seats" [C3] |

---

## 5. DLS26-specific modes worth watching [EV-446, C1]

| Mode | What it is | Why it matters |
|---|---|---|
| **Dynamic Stars** | Special Players whose cards **upgrade live** with real-world national team tournament performance — DLS's analogue of EA's "Path to Glory" | The only cards whose rating moves without you spending coaches. Collection opened 8 Jun 2026; obtained via **Dynamic Star Agents** |
| **World Tournament** | A brand-new **International Football event type** with high-tier reward tracking | Fresh reward surface; watch for its return |
| **World Heroes** | Live-service event from 1 Jul 2026; Special Players obtainable via **Legendary Agents** | The **second route to Special Players** outside the Prize Ladder — every Legendary Agent is a free roll |
| **Cult Heroes** | 12-player collection, live in v13.430 | Marquee targets: de Gea, Aubameyang, Dybala |
| **Dream Stars / 12th Man** | Dream Stars from real-world season performances; the 12th Man is the **community-voted extra slot** | The vote **concluded and the winner shipped in v13.120 (25 Mar 2026)** — *"the DLS community has voted, and we've added this extra superstar to the collection"* — but FTG never names them. **Mechanic closed; identity unknown** [EV-463, C2] |
| **Global Challenge Cup** | **128 teams, 4 per group home-and-away, top 2 qualify, then a straight knockout** (R32 to R16 to QF to SF to final) with extra time. Available in **every division**, Academy to Legendary; a loss after qualifying eliminates you | A pure coin-and-trophy surface. C-013 substantially resolved [EV-463, C2] |

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

**Three corrections and one confirmation from the achievement sweep** [EV-454, C3]:
- **The International Cup DOES exist** — confirmed by both an Exophase Apple achievement (*"International Cup Winners!"*) and a trophy count of **107 International Cup wins** against 122 GCC, 106 Allstar Cup and 110 Diamond Cup. This partially resolves **C-015**.
- **There is no clan-versus-clan mode.** A reviewer who expected inter-clan competition reports receiving *"a legendary scout and some coins"* instead.
- **Secret players exist** — the achievement SSSHHH pays 500 XP for purchasing one. Not previously in the KB.
- **Season Pass rewards unlock one per 12 hours** at 12:00 GMT+1 (AM and PM), so the track drip-feeds rather than opening all at once.
- **✅ THE 12-HOUR CLOCK CAN BE BYPASSED (ckpt-126, EV-456, OFFICIAL):** FTG states that *"even purchases made after day one will allow all content to be unlocked regardless of time locks between tiers, provided you earn the necessary Season Points to progress"* — a day-four buyer works towards tier five immediately. Buying the pass also **instantly unlocks the Premium content for every tier already unlocked on the free track** (reach tier 15, then buy, and 15 tiers of Premium rewards unlock at once). **So the 12-hour drip-feed is a free-track constraint, not a paid one: if the pass is going to be bought at all, buy it LATE in the season** — the same rewards, none of the waiting. The pass is **not a subscription** and must be repurchased each season.

---

## 6. Open gaps that still bound the plan

These are unresolved and each one caps precision. They are ranked by impact on the mission.

| # | Gap | Impact | Status |
|---|---|---|---|
| 1 | **Fanzone per-level costs** | Unknown gem commitment for the newest facility | Never published. Function confirmed (clan bonuses + stadium discounts) [C1] |
| 2 | **Form Boost duration per Training level** | Cannot price the Training facility's real value | ✅ **DOCUMENTED NEGATIVE (ckpt-126, EV-457)** — the official article gives only the rule (a set number of matches, **minimum one**); six guide families confirm the mechanic without numbers. **Plan on ONE match**; treat longer as a bonus |
| 3 | **Medical per-tier % beyond L1** | Cannot optimise the injury economy | ✅ **DOCUMENTED NEGATIVE (ckpt-126, EV-457)** — L1 is now **double-corroborated** (−10% heal / −5% injury, two independent Level Winner editions); L2–L5 are described only as *"progressively"* better. Higher player **STRENGTH** also lowers injury chance |
| 4 | **Post-DLS25 coach breakthrough %** | Coach packs priced off a DLS20 baseline | 5/10/20 confirmed as the DLS20 baseline; post-DLS25 figures unconfirmed [C2] |
| 5 | **Fan Approval mechanics** | Blocks the last stretch to 100% club value | ✅ **DOCUMENTED NEGATIVE (ckpt-126, EV-457)** — a dedicated two-search sweep found **no such mechanic in any documented source**; only crowd-graphics settings, fans-not-celebrating bugs, the Fan Favourite achievement and the Fanzone. **Strategy: max the full ~23-man squad and read the percentage as the output** |
| 6 | **GCC format** (C-013) | One cup's structure unclear | OPEN conflict |
| 7 | **LIVE rank names above "Veteran"** | Cannot name the top rank | **CLOSED BELOW VETERAN AT PRIMARY-SOURCE CONFIDENCE (ckpt-167, EV-504):** Google Play's own achievement data names all six ranks — **Rookie → Amateur → Semi-Pro → Intermediate → Pro → Veteran**, each a 500-XP achievement, and the list stops there. Above Veteran remains device-only |
| 8 | **12th Man winner identity** | A mechanic to watch each season | MECHANIC CLOSED (community-voted final Dream Star, EV-438 C1); FTG never names the winner |
| 9 | **Cult Heroes OVR conflict** (C-018) | 92 vs 95 on the four 85-rated heroes | OPEN |
| 10 | **Clan top-contributor reward** (C-017) | 50 vs 100 gems | **RE-OPENED (ckpt-126)** — now one community source each side; the "leans 100" note is withdrawn. Plan on neither |
| 11 | **Formation meta** (C-014) | 4-2-3-1 vs sportsdunia top-5 vs 4-4-2 | **EXPLAINED (ckpt-129)** — the disagreement is real and not an error: shapes differ by *failure mode*, stamina depth beats shape, and Tier-1 players switch shape as they climb. No single answer exists |
| 12 | **Commercial bonus curve** (C-019) | 13%/21% vs "10% at L5, biggest FTG scam" | OPEN |
| ~~13~~ | ~~**Special player max cost** (C-020)~~ | ~~2,100 gems / 7.5 coaches vs 6-7 coaches vs 2,100-2,835~~ | **RESOLVED at ckpt-118** — ~2,000–2,100 gems, 6–7 Legendary Special Coaches, ~420 gems saved by cancelling |

**Step 2 (static APK datamining)** remains postponed pending user direction. It is the only route that would close gaps 1, 2, 3, 4 and 5 definitively, because all five are numeric tables inside the game data.

---

## 7. The one-page routine

**Daily (≈45–60 min):**
1. Season Pass login (+40 SP) and the full daily challenge set (5–11 gems) — and **win Career matches by 4+ goals**, because goal count feeds Season Points as well as coins [EV-494, C3]
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
