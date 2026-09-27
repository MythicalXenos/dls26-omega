# TOPIC: Prize Ladder, live events, and the current limited-time window

**Sweep:** STATE_1_RESEARCH_SWEEP. **Opened:** 2026-09-27T17:55Z. **Exhaustion declaration:** NONE — open.
**⏱ TIME-SENSITIVE.** This file holds a live, expiring acquisition window that overlaps the user's stated current activity ("grinding prize ladder for a special player", user-stated). It is the first item staged for the earliest permitted advisory output (first contact at Step 5, or an interim contact if the bootstrap reaches three sessions first). Under NO OUTPUT DURING BOOTSTRAP nothing here may be said to the user yet — see ISS-006 for that collision and how it was resolved.

---

## Why this topic exists

"Prize ladder" is used in PROMPT.md §7 as undefined shorthand. As of this fetch it is **resolved: "Prize Ladder" is FTG's own term**, appearing in FTG's App Store in-app-event copy for a live event. That makes it an official game/event structure rather than a conversation artifact, and the user is currently grinding one.

## The two live events (both first-party, retrieved 2026-09-27)

- CLAIM: Two in-app events are marked "HAPPENING NOW" on FTG's official App Store listing: **"Cult Heroes"** ("Sign these top stars who are remembered by passionate football fans. Now available with boosted attributes.", eventid=6802988564) and **"English League Classics"** ("Relive the glory days – Unlock top players and claim big rewards in our this new Prize Ladder.", eventid=6759716099).
  - source: S-0015 (page-render, apps.apple.com official listing, Events section)
  - first_published: listing retrieved 2026-09-27; events marked live at that moment
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single origin = FTG; origin DIRECT and checkable at the recorded URL/eventids)
  - volatility: volatility-Critical
  - volatility_dimensions: patch-triggered: a client update can add/remove events | event-triggered: the events' own start and end dates — the Cult Heroes window is stated to end **10/14** (year not stated on the page; inferred 2026 from the retrieval date and the 2026-09-14 store update, recorded as an INFERENCE)
  - origin: DIRECT (FTG's own store event surfaces)
  - independence: ONE origin (FTG) across two platforms. The Play event page and the App Store event card are separate surfaces but the same author, so they corroborate the *identity* of the event strongly while counting as one source for tier purposes.
  - deception_screen: clean (first-party marketing; incentive is general — drive engagement/spend — not claim-specific)
  - datamining: pending-confirmation (flagged 2026-09-27; event configs, reward tables and card data should be in client assets — blocked, gaps G-0004)
  - evidence_class: verified tool output for the copy; inference for the year of 10/14
  - game_version: the client published 2026-09-14 (number unresolved, DLS26-C1) and its content state as of 2026-09-27
  - notes: "our this new Prize Ladder" (FTG's own grammar) marks English League Classics as a NEW Prize Ladder, implying Prize Ladders are a recurring event format rather than a one-off. "Boosted attributes" on Cult Heroes implies special cards whose stats exceed some baseline — the mechanic is NOT established.

- CLAIM: The Google Play in-app-event page for the event ending 10/14 is the Cult Heroes collection. Verbatim: "Event • Ends on 10/14 — The names the fans remember, from their peak years. Sign these top names who have made their impact on passionate football fans. Frozen in time from their peak years, and available to play for your team on the path to glory. Obtain them now for a limited time - don't miss out!"
  - source: S-0016 (page-render, play.google.com/store/apps/eventdetails/4830045897422713648)
  - first_published: retrieved 2026-09-27
  - last_verified: 2026-09-27 by page-render
  - confidence: Speculative (gate-capped: single origin; origin DIRECT)
  - volatility: volatility-Critical
  - volatility_dimensions: patch-triggered: none expected mid-event | event-triggered: the 10/14 end; the collection's expiry is the whole point of the copy
  - origin: DIRECT (FTG's own event page)
  - independence: one origin; the App Store Cult Heroes card (S-0015) is the same author on another platform
  - deception_screen: clean
  - datamining: pending-confirmation (flagged 2026-09-27; blocked, gaps G-0004)
  - evidence_class: verified
  - game_version: as above
  - notes: Closes gap G-0008 affirmatively. Establishes a limited-time acquisition window and the framing "frozen in time from their peak years" (i.e. cards representing players at their peak, not current form). Establishes NO cost, NO odds, NO player names, NO reward structure, NO card ratings. The event artwork (a tall image on that page) may name the players — retrievable via image tooling; owed.

- CLAIM: Cult Heroes moved from "coming soon" to live between 2026-09-14 and 2026-09-27.
  - source: S-0012 (Play changelog of the 2026-09-14 update: "New Special Players – 'Cult Heroes' collection, coming soon!") vs S-0015/S-0016 (live event surfaces retrieved 2026-09-27)
  - first_published: 2026-09-14 and 2026-09-27
  - last_verified: 2026-09-27
  - confidence: Speculative (gate-capped: single origin; origin DIRECT — two FTG surfaces at two dates)
  - volatility: volatility-Critical
  - volatility_dimensions: patch-triggered: the client update that shipped it | event-triggered: the launch itself
  - origin: DIRECT
  - independence: one origin, two dates — this is a temporal comparison of first-party records, which is exactly what makes it checkable
  - deception_screen: clean
  - datamining: pending-confirmation (flagged 2026-09-27)
  - evidence_class: verified
  - game_version: unknown number; the content state changed without a store-listing update, which means **the store changelog lags the client** — a durable lesson for the volatility model
  - notes: CONSEQUENCE FOR MONITORING: Mid-Session Monitoring cannot rely on store changelogs alone to detect a live event; the App Store Events section and the Play eventdetails page are the surfaces that show live state. Both belong in the Named Set consideration for event monitoring (adding a fourth Named Set slot is the user's to do, per PROMPT.md §5 — recorded as a proposal candidate, not adopted).

## What is NOT established (all owed)

Prize Ladder mechanics: how progress accumulates, what the milestones are, what the rewards are, whether progress resets, whether it is per-event or account-wide, whether it can be accelerated, what it costs, and what is permanently lost if the window closes. Cult Heroes: which players, what "boosted attributes" means numerically, card type, acquisition route (draw/purchase/ladder), odds, price, whether the collection returns later. English League Classics: same list. Whether either event is available in the user's region/store or on their client version. Whether the user's stated ladder is one of these two or something else entirely.

**Never record "no records found" as "does not exist"** — every item above is an OPEN gap, re-checked on later passes.

## Research order for this topic (by source)

1. Official: the two App Store event cards (eventid 6802988564, 6759716099); the Play event artwork image; FTG's Facebook / Instagram (@playdls) / TikTok (@dreamleaguesoccer.ftg) / X (@firsttouchgames) / YouTube for the Cult Heroes and Prize Ladder announcements and player lists; ftgames.com and firsttouchgames.com support/news routes.
2. Databases and tools: SakibPro's event articles ("DLS 26 New Update: All New Events, Special Cards & Upcoming Player Details", 2026-08-21; "World Winners"; "World Cup Heroes"; "Dream Star Event 2026") and its Player Database for any Cult Heroes / English League Classics cards; every other database discovered.
3. English community: Reddit, YouTube (including subtitle/transcript text), X, TikTok, Facebook groups, forums, wikis — specifically for Prize Ladder reward tables and Cult Heroes player lists, which the community usually enumerates fast.
4. Non-English community: tr, ar, pt, es, fr, id and any other language found — event guides are often published first in Turkish/Portuguese/Indonesian communities for this franchise (a HYPOTHESIS to test, not knowledge).
5. Technical: client assets for event configs (Step 2); Wayback captures of the listings and event pages to date the launch precisely.
6. User-generated: comments on all of the above.

## Cross-references

- Terminology: `kb/topics/terminology_and_abbreviations.md` (prize ladder → RESOLVED as an official term).
- Live-ops timeline and card families: `kb/topics/live_ops_events_and_cards.md`.
- Special Card Tracking (PROMPT.md §8): Cult Heroes and English League Classics cards must be evaluated on the card Tier 1–4 framework once their usefulness and rarity/return-likelihood are researched. Rarity and return likelihood are determined through exhaustive research into event history and FTG release patterns, **never assumed** — so no card tier may be assigned from this file's current evidence.
- User state: `kb/user_profile.md` §2 (prize-ladder position unknown; which ladder the user is on is a first-contact question).

---

## ADDENDUM 2026-09-27T18:52Z — a candidate Cult Heroes roster and an acquisition route (both third-party, both unverified)

Gap G-0010 advances on two fronts, and neither front is confirmed by FTG.

**(1) A 12-name candidate roster for the live Cult Heroes collection** (S-0019, sakibpro.com/players/trending.php): de Gea (GK 85), Aubameyang (CF 85), Dybala (SS 85), David Luiz (CB 84), Alarcón (AM 84), Insigne (LW 84), Ziyech (RW 84), Otamendi (CB 84), Blind (CB 83), Herrera (CM 83), Shaqiri (AM 83), Évora Dias (GK 83). Full table with heights, ages, nationalities and numeric ids in `kb/topics/player_pool_card_types_and_stats.md`. The same page lists 4 CLASSIC cards (Essien, Cole, Petit, Berbatov) and 1 SEASON PASS card (João Pedro, CF 82) as part of the same "latest update" — 17 players in total. **Every rating on that page is a third-party estimate from a domain whose authority over numbers was withdrawn (DR-001); the card page for de Gea flags its own OVR as "⚠️ ESTIMATED".** The roster is a hypothesis with two named first-party confirmation routes: FTG's own Cult Heroes event artwork (the Play event page carries a tall image, S-0016) and FTG's social channels.

**(2) An acquisition route: the "Cult Heroes Agent".** A per-player card page states "💎 Acquired Via | **Cult Heroes Agent** ✔️ SPECIAL EDITION" and, in prose, "As a special edition, this card is **exclusively available via the Cult Heroes Agent**" and "obtained exclusively through the Cult Heroes Agent" (S-0021). It gives **no cost, no odds and no mechanism**. Why this matters more than the roster:
- FTG officially names "**Agents** and Scouts to help identify top talent in the transfer market" (S-0011/S-0015), so an agent-mediated acquisition is *consistent with official vocabulary* — this is the first concrete lead on HOW the user would actually obtain a Cult Heroes card, which is the question that decides whether the expiring window is actionable at all.
- It sharpens the **loot-box question**: Apple's metadata declares the app "Contains: Loot Boxes" (S-0017) and Google's declares "Includes Random Items" (S-0011). An "Agent" that yields a specific-but-unpredictable special card is exactly the shape of a randomised acquisition. **Which purchase path is the loot box is gap G-0014, and the Cult Heroes Agent is now its leading candidate.** If the route is randomised, no expected-value calculation is possible without odds, and no spend recommendation may be made — which is precisely the discipline PROMPT.md requires for anything touching real money or an irreversible action.
- It also means the collection may NOT be a Prize Ladder reward at all. FTG's live events are two separate things: Cult Heroes (special players, "boosted attributes") and English League Classics (the "Prize Ladder"). A third-party "Acquired Via: Cult Heroes Agent" is consistent with Cult Heroes being agent-gated rather than ladder-gated — so **the user's stated "grinding prize ladder for a special player" may be the English League Classics ladder, a different ladder, or an agent grind they are calling a ladder.** Which one is a first-contact question, not an assumption.

**What is still completely unknown:** the Prize Ladder's mechanics (accumulation, milestones, rewards, reset, cost, what is lost if the window closes), whether the ladder and the agent are alternative routes to the same cards, whether Cult Heroes cards return after 10/14, what "boosted attributes" means numerically relative to a base card's +10 ceiling, and whether either event is live in the user's region and client version.

## ADDENDUM 2026-09-27T19:03Z — collection size confirmed as 12 by a second page of the same source; the acquisition question is now the bottleneck

The card-type index for Cult Heroes states "**Showing 12 of 12 Players Found**" and gives the same 12 names, ids and OVRs as the trending page (S-0022 vs S-0019), with common display names for two of them (**Isco** for Francisco Alarcón, **Vozinha** for Josimar José Évora Dias). The roster hypothesis is therefore internally consistent across two pages — still ONE source, so the tier does not rise and the list remains unconfirmed by anything first-party.

**The bottleneck has moved.** Knowing the 12 names is now the cheap part; the expensive part is *how a card is obtained and what it costs*. The only acquisition statement anywhere in the KB is a third-party card page's "💎 Acquired Via | **Cult Heroes Agent** ✔️ SPECIAL EDITION" and "exclusively available via the Cult Heroes Agent" (S-0021) — no cost, no odds, no mechanism, no confirmation. Until that is resolved:
- it is unknown whether the expiring window is actionable by a career-mode grinder who watches ads for rewards and has no stated gem balance;
- it is unknown whether the Agent is the app's declared "Loot Box" (Apple: "Contains: Loot Boxes", S-0017; Google: "Includes Random Items", S-0011) — and if it is randomised, no expected-value calculation and therefore no spend advice is possible;
- it is unknown whether the **English League Classics Prize Ladder** offers an alternative, non-random route to special players — FTG's own copy says "Unlock top players and claim big rewards" (S-0015), which is the one first-party sentence suggesting the ladder itself yields players, and it is the sentence most relevant to what the user says they are doing.

Priority order for this topic, restated after this turn's findings: (1) FTG's own Cult Heroes event artwork and channels — the only first-party route to both the roster and the acquisition mechanic; (2) the user's own in-game agent/ladder screens at first contact — one look settles cost, randomness and whether the ladder yields players; (3) community guides across the 15 client languages, which typically publish agent costs and ladder reward tables within days of an event; (4) client data in Step 2.

---

## ADDENDUM 2026-09-27T19:47Z — the acquisition mechanic now has a shape, and in-game evidence behind part of it

Four independent-of-each-other statements now describe how a Cult Heroes card is obtained, and one of them is visible in the game itself:
1. **Agents are items you collect, and opening one signs a RANDOM player.** dlskiturl.com (guide, human-authored prose with typos): "you will be able to sign player based on the **agents collected by you form the normal in-game events, Season Pass, Online Events, etc.** The Cult Heroes players can be **signed randomly by opening the agents** collected by you. The players will be **signed randomly to your team**." It adds the event "**will not be a Pay to Win Event**" — an opinion about design, recorded as one, and "This event will **commence on 16th September 2026**", which matches the 13.430 release date exactly.
2. **A per-player database states the route as a field:** "💎 Acquired Via | **Cult Hero Agent**" for all 12 (dlsinside.com), and "exclusively available via the Cult Heroes Agent" (SakibPro, S-0021).
3. **Three of the twelve are winnable rather than drawn:** "A total of **3 Cult Heroes** will be exclusively available as top-tier rewards by winning matches in upcoming Online Events" (SakibPro's update article).
4. **The game itself shows an AGENTS panel and a LIVE TRANSFERS screen with a CULT HEROES subsection** (S-0025), and the community's own vocabulary for opening one is gacha vocabulary — a Reddit post titled "Lucky Cult heroes **pull**".

What this changes, stated carefully: the expiring window is **probably actionable without real money** (agents earned through events, the Season Pass and Online Events), which matters enormously for a career-mode grinder who watches ads for rewards — but "probably", because the randomness claim rests on one guide site and the agent-earning routes on the same site plus one database. The FTG-official anchor remains only the store declarations that the app "Contains: Loot Boxes" / "Includes Random Items", which are consistent with a random agent draw but name no mechanic. **The Season Pass is confirmed as a card source in a second way**: dlskiturl describes a locked João Pedro card in the pass, "unlocked by buying the season pass", matching SakibPro's SEASON PASS card type and the $3.99 IAP.
Unchanged and still the bottleneck: no source states what an agent COSTS in earned currency, the odds of each of the 12, whether the three Online-Event rewards are fixed or random, or what the English League Classics Prize Ladder itself yields — and **the ladder has had no dedicated search yet**, which is now the single most obvious hole in this topic given that the user states they are grinding one.

---

## ADDENDUM 2026-09-27T20:10Z — THE PRIZE LADDER'S MECHANICS, AT LAST (G-0035 core closed in shape; every number still gated)

The dedicated search (S-0026) found one guide page — dlskiturl.com/dls-26-english-league-classics/ — and it answers the question the user's own activity makes urgent:

- **The ladder's currency is Dream Points (DP)**, earned "by playing matches across various game modes"; cumulative DP climbs tiers; at milestones you "claim milestone rewards" and the four ladder players become "free to be signed... without any limitation".
- **The four ladder players are Dimitar Berbatov, Michael Essien, Andy Cole and Emmanuel Petit** — exactly the four cards SakibPro listed as newly added CLASSIC cards in the same update (S-0019). The two "live events" and the roster update are therefore one release seen from three angles. Essien carries a year stamp too: "Version 2006".
- **Milestone thresholds: 62,500 / 115,000 / 175,000 / 250,000 DP** for the four signings.
- **Milestone rewards besides players: "coins, gems, coaches, and special agents."** This is the link that ties the two events into one economy: the Prize Ladder pays out the very agents that open Cult Heroes pulls, so ladder progress is convertible into Cult Heroes acquisition without money.
- **THE MODE DIFFERENTIAL — the single most decision-relevant sentence found in the entire bootstrap for this user:** "**DLS Live PvP:** Online multiplayer matches award **significantly higher DP per match** compared to standard offline Career Mode games", and "**Event Tournaments**... offer large DP completion bonuses upon winning the event."
- **Recycling:** the community criticism quoted on the page says Petit and Cole "were already made available in the previous Ladders" with "the Stats slightly [changed] and the card image [changed]", i.e. ladder content recurs across events with stat and art revisions — so any stat for these four is version-specific and undated tables for them are unplaceable.

Tier and honesty notes, unchanged in discipline: ONE third-party origin, so every threshold, rate and reward stays **Speculative**; the mechanics' SHAPE is recorded because it is specific, falsifiable in-game, and internally coherent with everything else found (agents exist in-game — S-0025; coaches and gems are official currencies — S-0017; the four Classic cards exist in three databases). The user's own ladder screen at first contact settles DP totals, tier position and per-mode rates in one look and outranks this page entirely.

**Why this is the lead item of the staged notification, ahead of everything else:** the user states they are grinding a prize ladder for a special player. If the mode differential is real, a Career-Mode grind is the designed slow path, and the ladder window shares the 10/14 expiry with Cult Heroes. Both facts change what this week's effort should look like, and neither is sayable under NO OUTPUT DURING BOOTSTRAP — which is the cost ISS-006 states openly rather than hides.

## ADDENDUM 2026-09-27T20:40Z — the ladder's four cards carry year stamps; card images and a mod route appear (S-0028)

The full page-render confirms the snippet was complete on mechanics (no milestone table was elided) and adds: **year stamps for all four ladder players — Berbatov 2011, Essien 2006, Cole 1994, Petit 1999** — i.e. the ladder's own instance of the year-stamp mechanic already at High Confidence (R-0003); partial stat claims (Berbatov CON 91 / SHO 92 at 189 cm with low speed and stamina; Essien STA 91; Cole high acceleration; Petit STA 90 with high passing and control); a key-attribute table; and **four card images** at dlskiturl.com/wp-content/uploads/2026/09/dls-26-{berbatov,essien,cole,petit}-new-card.png — a confirmation route for the ladder cards' design, years and possibly stats, unread and queued.
Two structural finds with governance consequences:
1. **The page links its own "DLS 26 Mod APK" page**, and an external dlsmod.com guide. Under the All Methods principle the mod route must be RESEARCHED WITH A RISK ASSESSMENT (detection, account safety, ToS exposure, and the server-authoritative-state inference from S-0017) rather than ignored — and the link is also an INCENTIVE SIGNAL for this domain (mod pages monetise traffic), recorded in its screening note. Research owed; no use ever recommended without the risk assessment and the user's informed choice.
2. **The comments thread contains French** ("J'ai envie de créer un joueur sur DLS M6") on an English guide page — non-English community presence inside English sources, and an uninterpreted fragment ("DLS M6") recorded verbatim rather than guessed at.
Nothing here changes any tier: one third-party origin for all ladder numbers, every value Speculative, the user's ladder screen still the fastest and strongest verification route.

## ADDENDUM 2026-09-27T21:12Z — the ladder as a system: 90-day cycles, claim-or-lose, gem-buyable speed, and a documented history of earlier cycles

Four additions change the ladder from an event into a system with a history and a clock (S-0031, S-0030):
1. **Cycles and loss:** 90-day cycles that reset with new rewards and new Classic players; tier rewards must be CLAIMED or can be lost at reset. Unresolved against the FTG-stated 10/14 end of the live ladder (G-0040).
2. **Speed is purchasable:** DP boosts (Common +50%/25 gems/3 matches; Rare +75%/35 gems/5; Legendary exists) and a paid Season Pass tier with bonus DP. The ladder is free to complete but not free to complete *quickly* — and "quickly" is exactly what a 10/14 deadline makes valuable.
3. **Earlier cycles are documented:** a May 2026 Reddit thread farms "20,000 DP... until the ladder is over just to get a 2nd special player", a Jan 2026 thread computes expected DP per match for a then-live ladder, and the ladder article itself says Petit and Cole recur from "previous Ladders" with changed stats and art (G-0039 substantially advanced: the ladder series exists, recycles players, and revises stats per cycle — so missing a cycle may cost the *current stat revision* of a card rather than the card forever, which materially changes the cost of the 10/14 window).
4. **The ladder's cards corroborated by a third party:** the site-rendered card images show Essien 85/2006/DM and Petit 84/1999/DM, matching SakibPro's OVRs and the article's years (S-0030). As watermarked renders they are agreement between third parties, not contact with the game; and their gold-star/no-gradient design differs from the in-game Cult Heroes captures' red-star/gradient design — family-specific art or template divergence, open (G-0046).
The staged notification's shape is now complete: window dates (16 Sep to 10/14), the mode differential (Community Consensus), the claim-or-lose rule, the gem-speed option with its prices, and the recycling caveat that softens the cost of missing it. Everything numeric remains Speculative and version-stamped; the user's own ladder screen remains the fastest verification and outranks all of it.

## ADDENDUM 2026-09-27T21:39Z — the ladder's documented history reaches Dec 2024, with a claim bug and a first-party rate image in its past (S-0033)

Four historical datapoints, each from community memory and each gated: **Dec 2024** — the Prize Ladder and Dream Points INTRODUCE with DLS25's season update, its first cycle themed on "**4 other Classic Players who featured in the 98 World Cup**", on a 90-day cycle (gamingonphone, which also credits a **First Touch Games image** for the DLL DP reward breakdown — a first-party origin for rates exists and is now a named lead); **Jan 2025** — a ladder with **Batistuta** as a special player and a **claim-order bug** ("when I claimed [the 70,000 milestone], it also claimed the special player"), plus community threads tracking ladder age ("More than 20 days have passed"); **Jan 2026** and **May 2026** — the farming threads already recorded. The series therefore spans at least seven cycles, recycles players with stat and art revisions, and has shipped at least one claiming bug — which is why "claim rewards as you hit each tier" advice (bluestacks) carries a second, bug-related reason, and why the current live ladder's claim behaviour is worth verifying before any claiming strategy is discussed (gap opened).
Nothing here changes the live ladder's tier status; it changes the COST OF MISSING A WINDOW: with a seven-cycle history of recycling, the 10/14 expiry most plausibly costs the current stat revision and the cycle's gem/agent rewards rather than the players forever — a hypothesis from pattern, labelled as one, and exactly the kind of thing the 90-day-vs-10/14 clock question (G-0040) will settle or break.
