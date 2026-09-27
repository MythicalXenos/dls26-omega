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
