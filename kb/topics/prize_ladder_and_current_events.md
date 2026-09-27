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
