# TOPIC: Economy — currencies, in-app purchases, season pass, loot boxes, monetization

**Sweep:** STATE_1_RESEARCH_SWEEP. **Opened:** 2026-09-27T18:08Z. **Exhaustion declaration:** NONE — open.
Taxonomy-gate dimension 2 (Economic & Currency matrix) is answered here: which currency is consumed for facilities vs stadium vs transfers vs physios vs scouts/agents, and facility compounding return curves.

Everything below comes from ONE first-party origin (FTG's own App Store listing, S-0017, chunk 5) — the strongest evidence class available for *what FTG publishes*, and tier-capped at Speculative by the Mechanism 5 count gate until an independent extraction exists. Origin is DIRECT for every item; see the tier policy note in `kb/README.md`.

---

## Officially named currencies

- CLAIM: DLS26 has (at least) two purchasable currencies, officially named **Coins** and **Gems**, evidenced by IAP product names: "Bundle of Coins", "Stack of Coins", "Cup of Coins", "Bundle of Gems", "Stack of Gems", "Locker of Gems".
  - source: S-0017 (Apple Information block, IAP list)
  - first_published: listing retrieved 2026-09-27
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single origin; origin DIRECT)
  - volatility: volatility-Low for the currency NAMES; volatility-High for prices and for which currency buys what
  - volatility_dimensions: patch-triggered: a currency rename, a new currency, or a price change ships with a client update | event-triggered: promotions, season boundaries, regional pricing changes
  - origin: DIRECT (FTG's own published IAP product names)
  - independence: one origin (FTG) displayed by Apple
  - deception_screen: clean; note that store price lists are platform-normalised and may lag or round
  - datamining: pending-confirmation (flagged 2026-09-27; the client's economy config would be direct evidence — blocked, gaps G-0004)
  - evidence_class: verified
  - game_version: 13.430 (iOS, Sep 16) / Play update Sep 14 2026
  - notes: The naming pattern implies tiers of purchase size (Bundle / Stack / Cup / Locker) rather than distinct currencies. Whether other currencies or resources exist in-game (e.g. event points, ladder tokens, coach-related consumables) is NOT established — the prompt's shorthand "coaches by type and rarity" and "season points" are unresolved terminology, and a store IAP list is not an inventory of in-game resources.

## Official US price list (App Store, retrieved 2026-09-27)

| IAP product | US price | What it is | Established? |
|---|---|---|---|
| Bundle of Coins | $1.99 | coins | name only — amount unknown |
| Bundle of Gems | $1.99 | gems | name only |
| Season Pass Special Offer | $1.99 | season pass, discounted entry | existence only |
| Stack of Coins | $3.99 | coins | name only |
| Season Pass | $3.99 | paid seasonal track | existence only |
| Special Offer | $4.99 | unspecified bundle | contents unknown |
| Cup of Coins | $6.99 | coins | name only |
| Stack of Gems | $7.99 | gems | name only |
| Promo Pack | $9.99 | unspecified bundle | contents unknown |
| Locker of Gems | $16.99 | gems | name only |

- CLAIM: A paid **Season Pass** exists at $3.99 (US), with a $1.99 "Season Pass Special Offer" variant.
  - source: S-0017 (Apple IAP list)
  - first_published: retrieved 2026-09-27; last_verified: 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single origin; origin DIRECT)
  - volatility: volatility-High
  - volatility_dimensions: patch-triggered: price or contents change with updates | event-triggered: season boundaries — a season pass is by definition season-scoped, so its window is the trigger
  - origin: DIRECT (FTG's own product list)
  - independence: one origin
  - deception_screen: clean
  - datamining: pending-confirmation (flagged 2026-09-27)
  - evidence_class: verified
  - game_version: 13.430
  - notes: Directly relevant to the user's spending profile (currently UNKNOWN — a first-contact question) and to taxonomy-gate dimension 3 (progression tracks: how a season pass accumulates and resets). Whether a free track runs alongside the paid one is NOT established. Highest-price item is the Locker of Gems at $16.99; the price ladder spans $1.99–$16.99, which bounds what "expensive" means for the high-stakes determination once the user's balances are known.

- CLAIM: Apple's content metadata for DLS26 states the app **"Contains: Loot Boxes"** and **"Advertising"**, with **"Frequent: Contests"** under the 13+ age rating.
  - source: S-0017 (Apple Information block, age-rating detail); corroborating taxonomy on Android: "In-Game Purchases (Includes Random Items)" (S-0011)
  - first_published: retrieved 2026-09-27; last_verified: 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single origin FTG self-declared, displayed by two platform operators; origin DIRECT for what was declared, NONE FOUND for which in-game purchase path is randomised)
  - volatility: volatility-Low
  - volatility_dimensions: patch-triggered: a change to what is sold | event-triggered: a change in store policy or rating taxonomy
  - origin: DIRECT for the declaration itself; NONE FOUND for the mapping to a specific in-game mechanic
  - independence: one origin (FTG's declaration) surfaced through two unrelated platforms (Apple's and Google's taxonomies), which is corroboration of the *declaration*, not of the mechanic
  - deception_screen: clean; note FTG has an incentive to declare narrowly, and Apple states privacy/rating answers are developer-provided
  - datamining: pending-confirmation (flagged 2026-09-27; which purchase yields random items is exactly the kind of thing client data would show)
  - evidence_class: verified
  - game_version: 13.430
  - notes: **Consequential for advice.** If any acquisition route the user is considering is randomised, its expected value must be computed rather than assumed, and it belongs in the irreversible/consequential analysis. The prompt's "special card" tracking and the Special Card Tracking card Tier 1–4 framework both require cost/reward to be calculated explicitly — impossible for a randomised route without odds, and odds are not published here. Which mechanic is the loot box (a pack, a draw, an agent/scout outcome, an event reward) is an OPEN gap.

## Developer-declared data practices (S-0017, App Privacy — Apple states these are NOT verified)

Tracking: Purchases, Identifiers, Usage Data. Linked to the user: Purchase History, Coarse Location, Device ID, Advertising Data (third-party advertising); User ID, Device ID, Product Interaction (analytics); **Gameplay Content**, Device ID, Product Interaction (product personalization); Purchase History, Coarse Location, User ID, Device ID (app functionality). Not linked: Crash Data, Performance Data (diagnostics).

- CLAIM: DLS26 maintains server-side user identity and collects gameplay content and purchase history.
  - source: S-0017 (developer-declared App Privacy answers)
  - first_published: retrieved 2026-09-27; last_verified: 2026-09-27
  - confidence: Speculative (gate-capped: single self-reported origin; Apple explicitly has not verified it; origin = FTG's own declaration, which is DIRECT for what FTG says it does and NONE for what the client actually transmits)
  - volatility: volatility-Low
  - volatility_dimensions: patch-triggered: a privacy-practice change would be declared with an update | event-triggered: a policy or SDK change
  - origin: DIRECT for the declaration; the client's actual traffic is the checkable route and is owed (risk Tier 3 research, Step 3)
  - independence: single self-reported origin
  - deception_screen: incentive OBSERVED but general — a developer has an incentive to declare narrowly; not claim-specific, so no cap beyond the ordinary single-source cap, and no register entry
  - datamining: pending-confirmation (flagged 2026-09-27; the whole risk Tier 3 question rests on it)
  - evidence_class: verified (the declaration exists), inference (what it implies about architecture)
  - game_version: 13.430
  - notes: INFERENCE, labelled as such and resting on the declaration plus the game's known online modes: the presence of User ID, server-side Purchase History and Gameplay Content collection implies server-authoritative account state rather than a purely local save. If correct, this raises the detection surface for any client-state tampering and lowers the value of local-only extraction for online play — a risk Tier 3/Tier 4 consideration to be researched properly in Step 3, never assumed here. It also means the State Access Pipeline's local extraction may be a partial view of true state (PROMPT.md §6 asks exactly this: "what is and is not reachable via ADB on an unrooted device").

## Unanswered (all OPEN gaps, none closed as "does not exist")

Which currency buys what: facilities (Stadium, Medical, Commercial, Training), transfers, coaches, physios/recovery, agents and scouts, kit/logo imports, event entries. Facility upgrade cost curves and any compounding return. Coin and gem income rates from every source (matches, ads, events, ladders, clans, daily scenarios, Dream Draft). Whether "watch ads for rewards" (user-stated) pays coins, gems, or items, and its daily cap. Gem-to-coin conversion, if any. Regional pricing. What the Special Offer and Promo Pack contain. Whether the Season Pass has a free track. Which purchase path is the loot box. Anything at all about an in-game transfer market economy (price formation, listing fees, the review allegation that selling returns no coins — S-0012).

## Research order for this topic (by source)

1. Official: FTG support pages on both official domains (`ftgames.com`, `firsttouchgames.com`); the privacy policy (SDK and data-partner disclosure); in-game help text via community screenshots.
2. Databases and tools: SakibPro (its Player Database and Upgrade Simulator imply cost/growth models worth inspecting as *models*, not as evidence); any other database found.
3. English community: spending guides, "is the season pass worth it" threads, coin/gem rate tables, ad-reward caps.
4. Non-English community: the client's own 14 non-English languages (ar, nl, fr, de, id, it, ja, ko, pt, ru, zh-Hans, es, zh-Hant, tr) — economy guides are frequently published in tr/pt/id first for this franchise (HYPOTHESIS to test, not knowledge).
5. Technical: client economy configs (Step 2), Wayback price history, IAP product-id enumeration from store APIs.
6. User-generated: review mining for prices and rates, processed for unique information.

---

## ADDENDUM 2026-09-27T20:12Z — a third currency-like resource and the ladder's payout table (all third-party, all gated)

The Prize Ladder introduces **Dream Points (DP)** as an earn-only progression resource (no purchase route reported), and its milestone rewards are reported as **coins, gems, coaches and special agents** (S-0026). Two consequences for the economic matrix:
1. **The earn side of the economy now has a named event pipeline**: matches → DP → tiers → {players, coins, gems, coaches, agents}, with per-mode rates that differ sharply ("DLS Live PvP... significantly higher DP per match... compared to standard offline Career Mode"; tournaments pay completion bonuses). If real, mode choice is an economic decision, not merely a gameplay preference — and for a user who watches ads for rewards and grinds in Career Mode, it is the highest-leverage single fact found so far.
2. **Agents as a ladder reward link the two live events into one economy** (ladder DP → agents → Cult Heroes pulls), which means the 10/14 expiry applies to both the direct Cult Heroes route and the ladder route that feeds it.
Everything here is one third-party origin and stays Speculative; the DP-per-mode rates are the specific numbers to verify first, because they are exactly what would change the user's grinding plan, and the user's own ladder and match screens can verify them in minutes.

---

## ADDENDUM 2026-09-27T21:10Z — the Dream Point economy: rates, boosts, cycles and three new named systems (S-0031; every number version-stamped and Speculative)

**Rates are VERSION-SENSITIVE — the central discipline of this section.** Four dated sources give three different rate sets (Dec 2024 / DLS25: Career win 75, +10/goal to 5, +15 CS, DLL win 120; Jan 2026: Career win 65, DLL win 115, DLL draw 45, DLL loss 15, +10/goal capped at 50, +10 CS, ads +35 Career win / +50 DLL win / +25 DLL draw-loss; May 2026: Career 5-0 win 120, +ad 160, +rare boost 250, +legendary 300-320). No undated DP number may be used anywhere in this KB; any advice touching DP must carry a version stamp and a re-check (Volatility Model, Critical).

**What is constant across all four — and promoted at Community Consensus (R-0006):** DLS Live (PvP) pays materially more DP per match than Career Mode; goal bonuses cap at 5 goals; ads add a flat DP bonus per match; boosts multiply DP for a limited number of matches.

**The boost economy — gems convertible into ladder speed:** Common DP Boost +50% for 25 gems over 3 matches; Rare +75% for 35 gems over 5 matches; a Legendary tier exists (May 2026 users quote ~300-320 DP/match under it). A paid Season Pass tier "grants bonus DP". Consequences, recorded not advised: the ladder is free in principle but **time is purchasable with gems**, so the user's ad-earned currency has a ladder-speed exchange rate; and gem spend on boosts is a CONSEQUENTIAL action (IA-05's family) whose expected value depends on the current rate set, which is unknown for 13.430.

**Three new named systems (each single-sourced, each an open gap):** **Progression Bank** — accumulates Coins and Gems from Dream League Live XP over a **10-day season**, paid out at season end (G-0045); **Season Points** — earned from Career Mode matches alongside Coins, amounts rising with division (G-0047; this is the prompt's unresolved shorthand "season points" finding a candidate official referent); **Global Challenge Cup** — a named competition (G-0037's family). Plus daily logins and challenges as reward sources.

**The ladder clock:** "Each Prize Ladder cycle lasts **90 days** before resetting with a fresh set of rewards and new Classic Players", and unclaimed tier rewards can be lost at reset ("Checking it regularly and claiming rewards as you hit each tier ensures nothing goes uncollected during the 90-day window"). This sits in unresolved tension with the live ladder's FTG-stated **10/14** end (G-0040): two clocks over one system, or one source wrong — recorded, not reconciled by preference.

---

## ADDENDUM 2026-09-27T21:38Z — a user's full gem-income model for a 10-day season, the complete boost ladder, and ads that double coins (S-0033)

**The model (one user's computation, assumptions stated, arithmetic checked — a hypothesis, not a fact):** over a 10-day DLL season at Tier 1 with max Stadium upgrades, a full-reward clan and a premium Season Pass, gem income enumerates as **DLL 6,000; Progression Bank 1,640; DLL Leaderboard 100; DLL Challenges/Quests 180; Season Pass 300; Daily+Weekly Challenges 897; Clans 275; DP Ladder 215; shop "Daily Mini" free rewards 180 (at 1,000 wins)**. Ladder gem milestones are **25+30+40+50+75 = 215**, and the ladder's final gem reward sits at **145,000 DP** (~300 DP per Legendary-boosted Tier-1 3-0 win ⇒ ~484 matches). A **daily match cap of 100** is asserted.
**The complete boost ladder:** Common +50% / 25 gems / 3 matches; Rare +75% / 35 gems / 5 matches; **Legendary +150% / 125 gems / 8 matches** (price at High Confidence per R-0007 on two independent threads; multiplier and duration Speculative, with the clan thread's ~300-DP figure arithmetically consistent with +150%).
**Ads double post-match COINS** (bluestacks: "a 30-second ad at the end of each match doubles your post-match coin earnings"), which reframes the user's stated ad-watching: it is a coin multiplier per match, on top of the DP ad bonuses recorded earlier.
**Two structural observations for the economic matrix, both labelled inference:** (a) the ladder pays gems (215/cycle) that can fund the boosts (25-125 gems) that speed the ladder — a small internal loop whose net value depends on the DP rates and is exactly the kind of compounding question PROMPT.md's dimension 2 asks about; (b) the Progression Bank sits **inside the Season Pass system** (bluestacks), so the paid pass may gate or enlarge a gem-income stream of 1,640/season — consequential for any pass-purchase decision and still single-sourced.
Everything above is version-sensitive and Speculative except where R-0007 says otherwise; the user's own screens (shop, boost purchase, post-match rewards, bank) can verify the whole model in one sitting and outrank all of it.

## Addendum 2026-09-28T00:20Z (session 1 turn 9) — first-party reward matrix and boost UI read directly from FTG captures (S-0035, S-0036)

Origin: five in-game captures retrieved via image_search and read directly; three are Dec-2024 FTG promotional captures (kb/evidence/ftg_career_reward_matrix_dec2024.jpg, ftg_dp_boost_popup_dec2024.jpg, ftg_weekly_challenges_dec2024.jpg), one a Jan-2026 DLS26 home screen (dls26_home_screen_jan2026.jpg), one a ~Jun-2024 DLS24 post-match screen (dls24_postmatch_stats_jun2024.jpg). All figures below are version-stamped to those captures; per tier policy a single FTG origin caps them at Speculative, but every column of the reward matrix sums exactly, which is an internal consistency check no second-hand report has.

**Career-mode reward matrix, Dec-2024 (4-0 away win, clean sheet, Academy Division game 1 of 15).** Three currency columns per line: coins / Season-Pass points (SP) / Dream Points (DP). WIN MATCH 15c / 100 SP / 75 DP. GOALS SCORED (4) 8c / 40 SP / 40 DP, i.e. 2c / 10 SP / 10 DP per goal. CLEAN SHEET 3c / 5 SP / 15 DP. REWARDS panel totals: 26 coins / 145 SP / 130 DP. Arithmetic: 15+8+3=26, 100+40+5=145, 75+40+15=130 — all exact. This is the checkable origin behind the Dec-2024 rate set (Career win 75, +10/goal capped at 5, +15 clean sheet) and it adds two economies never before on record: **coins per career match (15 win / 2 per goal / 3 clean sheet)** and **Season-Pass points per career match (100 / 10 / 5)**. The DLS24 capture shows no DP column at all, bracketing the DP introduction to Dec 2024 as the guides say.

**Dream Point Boosts popup, Dec-2024.** COMMON +50% for 3 matches; RARE +75% for 5 matches; LEGENDARY +150% for 8 matches; owned counts shown as badges (3 / 1 / 0, Legendary button greyed at zero owned); bottom purchase button **100 gems = 1 Random Boost** (category unspecified). Left panel shows active-boost state ('NO ACTIVE BOOST') and the DP balance (4,445). Multipliers and durations here match the Jan-2026 community thread independently => promoted to High Confidence in R-0008. The 100-gem random price is single-origin => Speculative, and note it coexists with the Jan-2026 per-tier prices (25/35/125): if both persisted, the random draw is a gamble priced between Common and Legendary.

**Challenges screen, weekly tab, Dec-2024.** Tabs: DAILY / WEEKLY / CAREER / DREAM LEAGUE LIVE. FREE column: four objectives each paying 80 DP plus a side reward (Use 1 Physio +25c; Complete 40 Career matches +x1 blue item; Win 20 Career matches +150c; Score 30 goals with a Forward +x1 gold item), plus Complete-all = 10 gems. SEASON PASS column: four objectives each paying **150 DP** plus side rewards (Sign 3 players +x1 silver item; Complete 20 Career matches +120c; Win 15 DLL matches +50 gems; a fourth hidden behind ACTIVATE PASS! showing 150c+150DP), plus Complete-all = 20 gems. Footer: weekly challenges can be **refreshed by tapping the video buttons** (ads), with a countdown to the next set (3d 22h 23m shown). So the Dec-2024 weekly DP income is 320 free + 600 pass-gated; the gem model's 'Daily+Weekly Challenges 897 gems per 10-day season' line and this 10+20 gems weekly complete-all are different lines of the same economy and must not be conflated.

**DLS26 challenge counts, Jan-2026 home tile:** DAILY 1/5, WEEKLY 0/5, CAREER 0/4, DLL 0/8 — the per-tab objective counts in DLS26 (weekly shows 5 here vs 4 free rows in the Dec-2024 capture; whether the fifth is the complete-all row or a added objective is unresolved, G-0056).

**Season-Pass points (SP)** emerge as a third match currency (100/10/5 per career win/goal/clean sheet; 195 SP shown on the Jan-2026 pass banner; pass objectives also pay DP). The pass economy is now a named gap (G-0051).

## Addendum (turn 19): facility architecture + stadium economy + division gates (S-0083) — gate dim 2
**FACILITIES:** Stadium (capacity → home-match coin bonus), Medical Centre (injury chance + recovery cost), Training Centre (unlocks formations + player form boost), Commercial Centre (coin % per match), Accommodations (squad size) [+ **Fanzone** — mod-sourced (gtrmod, Jun 2026): clan performance bonuses + stadium-expansion discounts; mod-screened ⇒ capped Speculative pending non-mod verification]. Facilities have ~5 levels (mod page; DLS23-era reddit cost data).
**STADIUM MATH (DLS23-era community, version risk HIGH):** 8 stands; upgrade 7 to max (leave a corner stand) → 85,000 capacity; never upgrade the same stand twice; roofs are cosmetic-cost traps; stadium bonus ≈ 48-52 coins/home match at 85k+ (≈250 coins/match with the after-match ad). Side stands ≈1,432 coins w/out roofs (DLS23 prices).
**COMMERCIAL % — DISPUTED numbers:** bluestacks (old page) L2 = +13% / L3 = +21% per match; reddit (2023) "10% for level 5 which costs 1000+ gems... biggest FTG scam". Treat percentages as version-unstable; datamining the facility table is the clean fix (flag: facility tables).
**DIVISION GATES:** App Store review (Sep 2026): "won't let me upgrade my stadium and division... division 4" + gtrmod: "strict seating requirements of higher divisions" ⇒ division promotion is gated on stadium capacity (two independent surfaces; mechanism specifics open).
**CURRENCIES & FEEDS:** Coins (matches/ads/daily), Gems (hard currency — coaches/agents/facility upgrades), DP (ladder, event-scoped), season points (Season Pass + "Progression Bank" — "accumulate during the 10-day season period, paid at season's end" [bluestacks, old page — the 10-day figure is version-risky]). Starter gems = 75 (old figure). Post-match ad multiplier exists (user + reddit).
**TRANSFER-LOCK MECHANIC (new, G-0019 refinement):** players can be "locked in transfer" (r/ mid-season megathread Feb-2026 + launch megathread: "if I've locked a player in transfer and they get updated do I get the chance to buy the upgraded player?" — OPEN question); a 2023 guide mentions gems to "lock a player". The home-screen "Locked. Sign." badges = this feature's status display. Rating-update interaction OPEN (G-0073).

## Addendum (turn 27): commercial table 3-way + daily-login reset rule + ad multiplier (S-0104)
**COMMERCIAL CENTRE — THREE CONTESTED TABLES (G-0074):** sportsdunia (30 Dec 2025): L1 2% match-win bonus + 5% kit/logo discount; L2 4%+10%; L3 6%+1%(?); L4 8%+20%; L5 10%+25% — adds a **Kit & Logo discount perk** per level. reddit (2023): "10% for level 5, costs 1000+ gems". bluestacks/gamingonphone (older figures): L2 +13% / L3 +21% per match. The sportsdunia+reddit pair agrees at L5=10%; the 13/21 pair is likely stale or flat-wrong. Datamine the facility table remains the fix (G-0074). 
**DAILY LOGIN (bluestacks + sportsdunia, DLS26-era):** 20-day reward cycle; **missing a single day RESETS to Day 1** (the streak rule); coins + occasional gems. **AD ECONOMY (gamingonphone DLS26, Jan 2026):** 30-second post-game ad can DOUBLE match rewards; separate daily ad-watch ≈30 coins (DLS25-era figure). **STARTER KIT (DLS26): ~1,200 coins + 40 gems** (was 75 gems in older versions). Scenarios = comeback-vs-Hard-AI, 50 coins/day. Season points: 40/day from login alone; challenges grant season points too.

## Addendum (turn 30): facility set = SEVEN + discipline costs + upgrade-order consensus (S-0110)
**FACILITY SET (updated):** Stadium · Medical Centre (injury chance + recovery cost) · Training Centre (formations + form boost) · Commercial Centre (match coins + kit/logo discounts; rust removal on high levels) · Accommodation Centre (squad size) · **Recruitment Centre (scout/agent hire discounts — NEW)** · Fanzone (Clan bonuses + stadium discounts, first-party 13.310). = 7 facilities.
**DISCIPLINE COSTS (fandom wiki "Coins", 31 Aug 2026):** yellow/red cards cost coins in matches (the wiki page is vandalized with garbage numerics — values unusable, structure indicative only: match coins vary by competition; goals/clean sheets pay; stadium bonus scales with stadium). Deception screen: community wiki, vandalism observed — content flagged corrupted.
**UPGRADE-ORDER CONSENSUS (3 surfaces):** stadium first → commercial → medical; accommodation/training last (bluestacks + r/ 2020 + r/ 2023). Feed-loop price point re-corroborated: 80+ players at 1,300-1,400 coins → release → legendary coach (r/ 2020). Healing costs scale with team level ("60-70 OVR team might use 50+ coins after every match to heal") — DLS20-era figure. Ad-grinding removes coin pressure entirely ("if you can watch ads with no daily limit, coins shouldn't be a problem").
**G-0074 status:** exact per-level cost tables still NOT in any indexed source — the datamine (facility config) or in-game screen captures remain the only clean routes.

## Addendum (turn 31): ECONOMY RESET — DP purchasable with Coins AND Diamonds (S-0115)
**SUMMER UPDATE (27 May 2026) reset the classic-progression economy:** **DP (Development Points)** — the currency for unlocking/upgrading classic players (Prize Ladder progression) — can now be bought directly with **Coins and Diamonds**. Previously the classic unlock/upgrade path was a grind bottleneck; now hoarded coins/gems convert straight to DP. Consequences: (a) coin-stacking endgame problem (G-0068) gets a new sink; (b) gem value shifts toward DP + Season Pass + transfer-lock; (c) the "feed-loop" release→coach loop competes with direct DP purchase. First-party confirmation via sakibpro FAQ ("Yes. The Summer Update officially allows players to purchase DP directly using in-game Coins and Diamonds"). Exact conversion rates OPEN (user can quote the DP shop screen).

## Addendum (turn 44): gem IAP tiers, Season Pass mechanics, facility-cost currency conflict (S-0193/0194)
- **Gem IAP tiers (sportsdunia, INR):** Bundle 90 gems = ₹199 · Stack 400 = ₹799 · Locker 910 = ₹1,799 · Sack 2,700 = ₹4,999 · Vault 6,000 = ₹9,900. (US App Store ladder: $1.99 Bundle … $16.99 Locker; the listing now also shows Special Offer $4.99, Cup of Coins $6.99, Promo Pack $9.99.) Implied gem-per-currency band ~0.45-0.6 gems/₹, Vault best.
- **Season Pass (bluestacks free-rewards guide — recycled evergreen prose, numbers unverified):** activation = **400 Season Points**; daily login alone = **40 SP/day**; free tiers guarantee **1,095 Coins**; **Progression Bank** = DLL-XP converted to coins+gems, paid at season end over a **10-day season period**. Daily Scenarios = 50 coins/day. Daily login refresh every 20 days. (G-0084 material.)
- **Prize Ladder cycle = 90 days** claimed again (third echo; vs FTG's 10/14 hard end — G-0040 clock question stays OPEN, both readings monitored).
- **Starting-kit conflict:** 1,200 coins + 40 gems (gamingonphone Jan-2026, footballeffect May-2026) vs "75 free gems to start" (sportsdunia Dec-2025) — possibly era drift or mode difference; unresolved.
- **Facility cost CURRENCY is contested (G-0074):** bluestacks beginner guide says GEMS pay stadium/facility upgrades; the fandom wiki says stadiums cost COINS (capacity gates division entry; home-match coin bonus scales with capacity). Both surfaces are recycled evergreen prose. Possible reconciliation: coins for early levels / gems for later (matches the "significant amount of gems as you move up the divisions" line) — OR pure source drift. Per-level cost TABLE still absent from the web; the user's facility screens are the decisive route.
- **DP-shop conversion rates (G-0085): NOT on any web surface** (turn-44 search was clean — no scam lures touched). User screen remains the only route. Dream Points remain known only as the ladder currency earned per match (mode-dependent rates unquantified).

## Addendum (turn 47): Season Pass dual-track + bank-claim gate (S-0204, dual-sourced)
- **Dual track: Free + Premium/Elite** (premium bought with gems or real money; rewards = large gems/coins, rare/legendary coaches, **exclusive player cards**, boosters) — gamedls.net (DLS25-era explainer, mechanism carried into DLS26 per bluestacks).
- **Activation gate:** accumulate **400 Season Points** (login 40/day + Career matches + DLL + Daily Challenges) to ACTIVATE the pass and claim the **Progression Bank** (DLL-XP → coins+gems, accumulated over a **10-day season**) at season end — miss the activation/claim and the payout is lost.
- **Two-cycle structure confirmed across sources:** 10-day Season Pass/Progression Bank vs 90-day Prize Ladder (bluestacks). Both surfaces recycled-evergreen; numbers remain "unverified but dual-sourced".
- SP sources per gamingonphone: Career matches grant SP + coins; Daily Challenges grant SP; DLL gems = weekly leaderboard.

## Addendum (turn 49): price-grid anchors + secret-market discount mechanic (S-0210)
- **Price anchors (community, unverified single-claims):** Rodri 86 = **2,725 coins** (DLS25 post-increase) vs Dickison 85 = **2,375 coins** (DLS26, verified anchor) — implies a mid-80s step band of roughly 350-400 coins per OVR point (NOT a fitted curve; two points only).
- **Secret-market mechanic (NEW):** secret-class players can appear IN THE LIVE TRANSFER MARKET at a discount — crossed-out base price ~2,555 -> 2,355 paid (~200 reduction) for an 82 OVR forward. The crossed-out prices are effectively the base-price table made visible; "can be off by 2 or 3 coins" (community precision note).
- **Special cards have NO market price** (sakibpro squad-builder): Champion / World-Cup-Heroes / Dreamstars obtainable only via special agents, events, season passes — coin value nullified in budget tools. Confirms: specials are agent/event/DP-side, not coin-side.
- Community budget heuristic: "at least 10,000 coins to buy a player and still save money" (top-end market prices).

## Addendum (turn 50): THE PRICE FORMULA + verified anchor 86 CF = 2,970 (S-0213)
- **Formula (sakibpro price calculator):** price = f(**Base OVR**, **exact position**) — "attackers generally cost more than defenders with the exact same rating." Positions: CF LW RW SS AM CM DM LM RM LB RWB CB RB GK (14).
- **VERIFIED anchor: 86 OVR CF = 2,970 coins** ("Verified Data" badge = manually confirmed in the live transfer market): Kane 86 CF, Mbappe 86 CF, Dembele 86 CF, Haaland 86 CF all = 2,970. Alongside Dickison 85 CB = 2,375 (our verified anchor) this implies a STRONG position premium (CF >> CB at equal OVR).
- **Verified vs Extrapolated discipline:** verified = live-market-confirmed; extrapolated = their claimed "exact mathematical pricing formula" (formula itself not exposed on the page).
- **Secret-player discount mechanic CONFIRMED (second surface):** secret market offers at a slight discount to standard price; knowing the standard grid lets you identify the hidden player from the discounted price ("you can easily guess who the secret player might be"). Matches the Reddit crossed-out-price observation.
- Tension to resolve: Rodri 86 = 2,725 (DLS25, CM) vs Kane 86 = 2,970 (DLS26, CF) — era + position effects are confounded; needs an 86 CM datapoint on DLS26.

## Addendum (turn 51): price grid sampling + deconfound + anchor validation (S-0215..0217)
**Grid (sakibpro URL params WORK: ?ovr=&pos=):**
| OVR | CF (Forward) | CM (Midfield) | CB (Defense) | GK |
|---|---|---|---|---|
| 86 | **2,970** (VERIFIED: Kane/Mbappe/Dembele/Haaland) | **2,730** (Extrapolated; 0 DB matches) | ? | ? |
| 85 | ? | ? | **2,375** (VERIFIED: Gabriel 16347 / VVD 27130) | ? |
- **DECONFOUND:** Rodri 86 CM = 2,725 (community DLS25) vs 86 CM = 2,730 (formula DLS26) = 5 coins apart -> **era effect ~0-5 coins**; the CF-over-CM premium at 86 = **+240**. The "DLS25 price increase" maps to essentially the same grid.
- **VALIDATION:** their 85 CB = 2,375 **exactly matches our Dickison 85 CB = 2,375 anchor** (independent). Grid trustworthy at Verified cells; formula consistent so far at Extrapolated ones.
- **Positional groupings:** Forward / Midfield / Defense / GK ("attackers cost more than defenders at equal OVR").
- VVD market id = 27130 (adjacent to 27133 PEDRI — champion-block era ids noted).

## Addendum (turn 52): grid growth + C.Ronaldo pair + FACILITY ECONOMICS (S-0218..0221)
**Grid (all sakibpro; v = Verified, e = Extrapolated):**
| OVR | CF (F) | CM (M) | CB (D) | GK |
|---|---|---|---|---|
| 86 | 2,970 v | 2,730 e | 2,520 e | ? |
| 85 | 2,785 e | ? | 2,375 v | ? |
| 82 | 2,275 v | ? | ? | ? |
Curve notes: CF 82->85 = +510 (~170/OVR), 85->86 = +185 (steepening); CB 85->86 = +145. Position premium at 86: CF+450 over CB, +240 over CM; at 85: CF +410 over CB.
**TENSION (open):** Reddit secret-market datapoint (crossed ~2,555 for "an 82 overall forward") does NOT match 82CF = 2,275 — either the market showed an approximate display OVR (grid keys on BASE OVR) or the position was SS/LW/RW. The market-displayed-OVR-vs-base question matters for identifying secret players from discounted prices.
**FACILITY ECONOMICS (DLS23-era community + DLS26-labeled evergreen) — currency conflict RESOLVED as a split:**
- **Stadium STANDS = COINS:** 8 stands (4 sides + 4 corners); side stand maxed w/out roofs ~1,432 coins (DLS23); roofs extra; **7 maxed + 1 corner un-upgraded = 85,000 capacity**; home-match stadium bonus **48-52 coins** at 85k+.
- **Facility LINES = GEMS:** five lines at **1,125 gems each = 5,625 gems** full completion (+ ~10,000 coins for stands); "around 5K gems to upgrade everything".
- **Stadium Commercials bonus ladder (DLS26-labeled):** Level II = **+13%** match-coin bonus; Level III = **+21%**; "starting 75 gems on Commercials" (bluestacks) — 75-gem starting kit corroborated (vs 40-gem conflict still open).
- Numbers era-tainted (2023-era anecdotes); DLS26 confirmation via user facility screens still owed (G-0074).

## Addendum (turn 53): CF curve complete; SS = CF tier; GK cheapest (S-0222..0225)
**Grid (sakibpro; v = Verified, e = Extrapolated):**
| OVR | CF | SS | CM | CB | GK |
|---|---|---|---|---|---|
| 86 | 2,970 v | — | 2,730 e | 2,520 e | 2,220 e |
| 85 | 2,785 e | — | ? | 2,375 v | ? |
| 84 | 2,610 v | — | ? | ? | ? |
| 83 | 2,440 v | — | ? | ? | ? |
| 82 | 2,275 v | 2,275 v | ? | ? | ? |
- **CF curve COMPLETE and smooth:** steps 82->83 +165, 83->84 +170, 84->85 +175, 85->86 +185 (concave-up; extrapolate with care beyond 86 — the calculator caps at 86 base).
- **82 SS = 82 CF = 2,275** — SS/CF share the Forward tier (at 82; assume tier-wide).
- **GK = cheapest tier:** 86 GK 2,220 < 82 CF 2,275. Position ladder at 86: CF 2,970 > CM 2,730 > CB 2,520 > GK 2,220. (GK upgrade model is also separate: 2.2 pts/OVR.)
- **2,555 tension UNRESOLVED and narrowed:** crossed-out 2,555 matches NO CF/SS cell (sits between 83 CF 2,440 and 84 CF 2,610; the discounted 2,355 also exceeds the 82 CF standard 2,275). Candidates left: LW/RW tier difference (82 LW/RW untested), display-OVR-vs-base, special-card pricing, or a wrong/rounded community claim.
- **Base-record ids from verified cells:** Lautaro 16329, **Alvarez 19159 (84 CF — the Kick-Off Star cover star's NORMAL card)**, Osimhen 17319, Benzema 2602, Lewandowski 2862, Thuram 15672, Gyokeres 18877, C.Ronaldo 382 + 25851, Gabriel 16347, VVD 27130.

## Addendum (turn 54): TIER-FLAT pricing + the 2,555 tension RESOLVED (S-0226..0229)
**Grid (14 cells; v = Verified, e = Extrapolated):**
| OVR | CF | SS | LW | AM | CM | CB | GK |
|---|---|---|---|---|---|---|---|
| 86 | 2,970 v | — | — | 2,730 e | 2,730 e | 2,520 e | 2,220 e |
| 85 | 2,785 e | — | — | — | **2,555 v** | 2,375 v | ? |
| 84 | 2,610 v | — | — | — | — | 2,230 v | ? |
| 83 | 2,440 v | — | — | — | — | — | ? |
| 82 | 2,275 v | 2,275 v | 2,275 v | — | — | — | ? |
- **PRICING IS TIER-FLAT:** Forward (CF = SS = LW, 2,275 at 82), Midfield (AM = CM, 2,730 at 86). The "exact position" factor operates at TIER level: Forward / Midfield / Defense / Goalkeeper. Tier ladder at 86: F 2,970 > M 2,730 > D 2,520 > GK 2,220; at 85: F 2,785 > M 2,555 > D 2,375.
- **Curves:** CF +165/+170/+175/+185 (82->86); CB = FLAT +145 steps (2,230/2,375/2,520 at 84/85/86); CM 85->86 = +175.
- **2,555 TENSION RESOLVED:** 85 CM = 2,555 VERIFIED (Valverde 16636 / Pedri 17763 / Vitinha 18183) = the exact crossed-out datapoint. The community's "82 overall forward" label was a display-OVR artifact or mis-ID; **market pricing follows the BASE grid (display can lie; price cannot)**. Secret-market recipe CONFIRMED: crossed-out = standard grid price; discount ~200 coins; identify the hidden player by mapping the crossed price to (base OVR, tier).
- **New base-era ids:** Neymar 1892 (82 LW), Sane 12413, Valverde 16636, **Pedri 17763 (85 CM — distinct from champion-era 27133)**, Vitinha 18183, Bastoni 16390, Saliba 17387, **VVD 7307 (84 CB — second VVD record vs 27130 85 CB)**.

## Addendum (turn 55): TIER MODEL COMPLETE — F/M/D/GK all confirmed flat (S-0230..0233)
**Final grid shape (18 cells; v = Verified, e = Extrapolated):**
| OVR | F (CF=SS=LW=RW*) | M (AM=CM=DM=LM*=RM*) | D (CB=LB=RB*=RWB*) | GK |
|---|---|---|---|---|
| 86 | 2,970 v | 2,730 e | 2,520 e | 2,220 e |
| 85 | 2,785 e | 2,555 v | 2,375 v | 2,080 v |
| 84 | 2,610 v | ~2,395? | 2,230 v | ? |
| 83 | 2,440 v | 2,235 v | ? | ? |
| 82 | 2,275 v | ? | ? | ? |
(* = assumed flat on the confirmed pattern; not yet sampled.)
- **TIER-FLAT CONFIRMED on every sampled member:** F: CF = SS = LW · M: AM = CM = DM · D: CB = LB · GK separate. Price = f(base OVR, tier) with 4 tiers.
- **Tier ladders:** at 86: F-M 240 / M-D 210 / D-GK 300. At 85: F-M 230 / M-D 180 / D-GK 295.
- **Curves:** F concave-up (+165/170/175/185); D linear +145 (84-86); M 83->85 +320 then +175 (steepening like F); GK +140 (85->86).
- **New base ids:** Donnarumma 14078 (85 GK), Barella 14738, de Jong 15307, McTominay 15929, Bruno Guimaraes 17566, Joao Neves 21494.
- **MODEL STATUS: complete for practical use** (secret identification, budgeting, agent valuation). Remaining micro-cells are interpolation/assumption territory, confirmable on user market screens.

## Addendum (turn 65): five new verified grid cells + the 2,085 COLLISION (S-0255)
**Route note (integrity):** this price-calculator route was opened at S-0213 and mined through S-0233 — the `?ovr=&pos=` scheme and the Verified(v)/Extrapolated(e) labelling were ALREADY established there. This batch extends the grid; it is the SAME single source and therefore does NOT raise the confidence tier of the model.
**New VERIFIED cells (previously absent from the KB):**
| Cell | Price | Badge | Named matches (id) |
|---|---|---|---|
| 84 CM | 2,390 | v | Declan Rice (16332) |
| 84 AM | 2,390 | v | Szoboszlai (17272), Bellingham (17799) |
| 83 CB | 2,085 | v | Bremer (16359), Upamecano (18191), Pacho (21336) |
| 82 CM | 2,085 | v | Milinkovic-Savic (13747), Fabian Ruiz (14961), Modric (1498), Enzo Fernandez (19972) |
| 84 GK | 1,950 | v | Alisson (14939), David Raya (16412), Courtois (7458) |
**THE 2,085 COLLISION (new and practically important):** **83 CB = 82 CM = 2,085** — two different ratings in two different positional groups resolve to the identical price. A crossed price of 2,085 is therefore AMBIGUOUS between an 83-rated defender and an 82-rated midfielder, and the crossed-price recipe (Q-007) cannot disambiguate on price alone; it needs the position group from the card. This is the first identified collision in the grid and it should be checked for others (the four ladders are close enough that more may exist).
**Grouping confirmed as four ladders** with explicit labels Forward / Midfield / Defense / Goalkeeper; CM = AM at 84 extends the previously recorded midfield flatness (AM = CM = DM at 86) down to 84.
**Tool quirk:** the query param must be `pos` — `position` is silently ignored and the request falls through to the Forward-group default (85 & position=CM returned 2,785, the Forward figure, mislabelled as the CM answer). Anyone re-running this route must use `pos`.

## Addendum (turn 66): THE PRICE MATRIX IS COMPLETE (81-86 x 4 groups) + the full collision set (S-0258)
**The complete matrix** (v = Verified badge, e = Extrapolated badge — same single source throughout, so the tier does not rise):
| OVR | Forward | Midfield | Defense | Goalkeeper |
|---|---|---|---|---|
| 86 | **2,970** v | 2,730 e | 2,520 e | 2,220 e |
| 85 | 2,785 e | **2,555** v | **2,375** v | **2,080** v |
| 84 | **2,610** v | **2,390** v | **2,230** v | **1,950** v |
| 83 | **2,440** v | **2,235** v | **2,085** v | 1,825 e |
| 82 | **2,275** v | **2,085** v | **1,950** v | **1,705** v |
| 81 | **2,115** v | **1,935** v | **1,815** v | **1,590** v |
**THE COMPLETE COLLISION SET for 81-86 — exactly two, both cross-group and cross-OVR:**
- **2,085 = 82 CM = 83 CB** (the cheaper group, one rating higher)
- **1,950 = 84 GK = 82 CB** (the cheapest group, two ratings higher)
No other value is duplicated anywhere in the 24 cells. For the crossed-price recipe (Q-007) these two prices are genuinely ambiguous and cannot be resolved without the position group printed on the card; every other price in the range maps to a single cell.
**Structure:** the group ordering is strict at every rating — Forward > Midfield > Defense > Goalkeeper — and the inter-group gap WIDENS as the rating rises (Midfield-to-Defense gap: 135 at 82, 150 at 83, 160 at 84, 180 at 85, 210 at 86). Within a group the per-rating step also grows with rating (Forward: +160, +165, +170, +175, +185).
**METHODOLOGICAL CATCH — Extrapolated cells still list named players.** The 83 GK cell is badged **Extrapolated** while displaying Emiliano Martinez and Maignan. So the "TOP N MATCHES" list is NOT corroboration of the price: on an Extrapolated cell those players are simply being shown at a formula-derived figure. **Any candidate-name reasoning built on an Extrapolated cell is circular** and must not be used as evidence for the secret-player recipe.
**Interpolation check (self-validation, not independent truth):** turn 65 predicted 84 CB = 2,230 by interpolating between 83 CB (2,085) and 85 CB (2,375); the fetched value is exactly 2,230. The arithmetic tracks their formula — but since it is the same source, this validates internal consistency only.
**New named IDs captured (normal base tier):** Marquinhos 11519 · Koulibaly 12375 · Gvardiol 19396 · Bastoni 16390 · Saliba 17387 · van Dijk 7307 · Sommer 12197 · Oblak 12336 · Ederson 15227 · Joan Garcia 19544 · Kobel 19920 · E.Martinez 14124 · Maignan 15467 · Son 10074 · Schick 14955 · Leao 16348 · Isak 17237 · Firmino 7413 · Rabiot 11114 · Aleix Garcia 13739 · Mac Allister 18243 · Reijnders 18693 · Marchisio 2463 · Rudiger 12480 · Ruben Dias 16288 · Militao 16518 · Guehi 18301 · Cubarsi 24065 · Diogo Costa 17212 · Unai Simon 17474 · Carnesecchi 9713.

## Addendum (turn 67): A SECOND INDEPENDENT SOURCE — three cells corroborated (S-0259/0260/0261/0262)
**This closes the binding weakness flagged at turn 66.** The matrix rested entirely on one operator (sakibpro). A community price list for DLS 26 (Reddit, u/ahmthn0, Dec-2025) reports prices observed by players in their own transfer markets — a different source TYPE and an unrelated author — and it corroborates three cells exactly:
| Cell | sakibpro matrix | Reddit price list | Agreement |
|---|---|---|---|
| 86 CF | 2,970 (Verified) | "86 = 2,970 (Kane / Haaland)" | **exact** |
| 85 CM | 2,555 (Verified) | "2,555 = 85 midfielder (Vitinha, Bruno etc.)" | **exact** |
| 82 CF | 2,275 (Verified) | "An 82 overall forward" = 2,275 | **exact** |
These three cells now rest on two independent sources and may be treated as the reliable spine of the grid. **The other 21 cells remain single-source** and should be used with that caveat.
**Three operational facts from the same thread (these matter more than the cell matches for the market recipe):**
1. **The secret-player discount is about 200 coins** (observed: 2,555 -> 2,355).
2. **"The crossed-out price can be off by 2 or 3 coins"** — the observed price carries a tolerance of roughly +/-3. Any recipe that treats a crossed price as exact will misidentify at the margins, and this tolerance is wider than the gap between some adjacent cells.
3. **"There isn't one [86 MID], the best midfielder is Pedri, with 85"** — an independent, structural explanation for why our 86 CM cell is badged Extrapolated: no such base card exists to verify. The same reasoning plausibly covers 86 CB, 86 GK and 85 CF. **Practical consequence: Extrapolated cells are prices for cards that do not exist in the base market, so the recipe is unlikely ever to need them.** The 83 GK cell remains the exception that breaks the clean reading (it is Extrapolated yet named 83-rated goalkeepers exist), so the badge should be read as "not manually confirmed" rather than as a strict existence claim.
**Weak corroboration (recorded, not load-bearing):** TikTok auto-generated search-suggestion strings echo 2,230 (84 CB), 2,610 (84 CF) and 2,970 (86 CF) as DLS26 secret-player prices. Low reliability — no author, no method — so it raises nothing on its own, but the 2,230 value was only obtained yesterday and seeing it echoed is worth noting.
**Route note:** Reddit returns 403 to direct fetch, including the .json endpoint (S-0261). Reddit evidence is therefore permanently snippet-limited here.

## Addendum (turn 68): A SECOND INDEPENDENT OPERATOR CONFIRMS THE GRID — and both collisions (S-0263..0266)
**The independence problem is materially solved.** dlsinside — a different operator with its own database — states a coin price as a data field on every per-player page ("In this edition, the card has a value of N coins"). Seven cells are now independently corroborated:
| Cell | sakibpro | dlsinside (player, id) | Independent? |
|---|---|---|---|
| 86 CF | 2,970 | Harry Kane (10159) | **yes** (also Reddit) |
| 85 CM | 2,555 | Federico Valverde (16636) | **yes** (also Reddit) |
| 84 GK | 1,950 | Alisson (14939) | **yes** |
| 82 CB | 1,950 | Marquinhos (11519) | **yes** |
| 83 CB | 2,085 | Bremer (16359) | **yes** |
| 82 CM | 2,085 | Luka Modric (1498) | **yes** |
| 81 CF | 2,115 | Heung-min Son (10074) | **yes** |
**BOTH COLLISIONS ARE NOW TWO-SOURCE CONFIRMED — they are real properties of the pricing system, not artifacts of one tool's formula:**
- **2,085 = 83 CB (Bremer) = 82 CM (Modric)**
- **1,950 = 84 GK (Alisson) = 82 CB (Marquinhos)**
This is the practically decisive result for the crossed-price recipe (Q-007). At 2,085 an 83-rated defender and an 82-rated midfielder are genuinely indistinguishable by price; at 1,950 an 84-rated goalkeeper and an 82-rated defender likewise. Only the position group printed on the card separates them. **Eight of the 24 cells are now two- or three-source (up from three at turn 67); the remaining sixteen are still sakibpro-only.**
**Entity data captured (dlsinside):** Kane 86 CF 188cm/33/Right, Shooting 96/Speed 75/Acc 70, England + North European Allstars · Valverde 85 CM-RM-RB 182cm/28/Right, Passing 83/Control 82/Stamina 90, R Madrid + Uruguay + South American Allstars · Alisson 84 GK 193cm/33/Right, GK Reactions 82/GK Handling 80/Passing 68, Liverpool · Marquinhos 82 CB-RB 183cm/32/Right, Tackling 91/Strength 85/Speed 79, Paris SG · Son 81 CF-LW 183cm/34/**Both-Right**, Shooting 83/Speed 85/Acc 85, Korea Republic + Asian Allstars · Bremer 83 CB 188cm/29/Right, Tackling 91/Strength 86/Speed 83, J Turin · Modric 82 CM-DM 172cm/**41**/Both-Right, Passing 92/Control 90/Stamina 75, A Milan + Croatia + South European Allstars.
**Route results:** `dls-ext.vercel.app` (a community DLS26 database shared on Reddit) exposes a **Price** field in its player-detail panel but is a client-side SPA — fetch_page gets only an empty shell, so it needs a JS-capable approach or a user screenshot (lead, not yet a source). `dlsplayers.com` is a NEGATIVE: its player profiles are empty "Coming Soon" stubs behind an APK-promotion funnel — no rating, no stats, no price despite claiming a "Player Value" feature. `dls-database.lovable.app` is **DLS25-era** and its prices conflict with the DLS25 figures quoted on Reddit (Rodri 86: 2,600 vs 2,725), so the entire DLS25 price picture is contested and unusable for DLS26.
