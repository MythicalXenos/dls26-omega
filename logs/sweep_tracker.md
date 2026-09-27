# STATE_1 RESEARCH SWEEP — FRONTIER TRACKER

Human-readable companion to `logs/sources_visited.json`. The JSON log is the mechanical basis of any exhaustion declaration (PROMPT.md §2 MECHANICAL EXHAUSTION INVARIANT); this file tracks the frontier's shape so that "what is left" is a recorded fact rather than a feeling.

**Sweep:** bootstrap Step 1, opened 2026-09-27T17:22Z. **Sources visited: 11 distinct origins across 17 content fetches + 1 search + 2 images (S-0001, S-0002, S-0011..S-0017) plus capability probes S-0003..S-0010.** **Scope:** everything about DLS26 and everything around it (PROMPT.md §13 Step 1) — the widest scope a trigger can set. **Organization:** by SOURCE, not by question; each source is exhausted before moving on, and organizing by source never narrows scope.
**Exhaustion declaration:** NONE. Neither condition is met: unvisited leads exist (condition 1 fails) and new information is still arriving from every reached source (condition 2 fails).

## Coverage grid — Mechanism 3 gate categories × progress

| Source type (gate category) | Planned sources | Visited | Status | Next specific action |
|---|---|---|---|---|
| official | FTG root, /games, /support, **ftgames.com + /privacy-policy (second official domain, discovered)**, patch notes, Facebook, Instagram, TikTok, X/Twitter, YouTube, Play Store (all regions + eventdetails + datasafety + dev page), App Store (all storefronts) | 2 (FTG /games; Play Store US/en listing, both chunks) | PARTIAL | page-render App Store `id1462911602` — Apple publishes version numbers and dates, the strongest remaining route for DLS26-C1 |
| third-party databases & tools | SakibPro (home fetched; tools `/players`, `/players/simulator.html`, `/dls-26-card-creator` and ~15 article pages outstanding; its code/API/undocumented functionality outstanding), plus every other DLS database/tool found — the list is discovered, not prescribed | 1 (sakibpro.com home, both chunks) | STARTED | page-render `sakibpro.com/players` (the player database — the candidate-pool enumeration source) |
| English-language community | Reddit (r/DreamLeagueSoccer + any other), YouTube (titles, descriptions, comments, subtitles/transcripts), Discord (public servers), X, TikTok, Facebook groups, forums, wikis, guide sites, blogs, app-store reviews | 1 partial (3 top Play Store reviews retrieved inside the official listing; the full review set is outstanding) | STARTED | Play Store 'See all reviews' + locate the subreddit(s) |
| non-English community | Turkish, Arabic, Portuguese, Spanish, French, Indonesian, and every other language with a DLS26 community — discovered by search in those languages, not assumed | 0 | NOT STARTED | discovery-search in tr / ar / pt / es / fr / id for the game's own terms |
| technical | APK repositories (apkmirror, apkpure, uptodown), GitHub repos and community datamining dumps (codeload route WORKS), web archives (Wayback), cached pages, public APIs, API responses, code comments, DB schemas | 0 content sources (route proven available) | NOT STARTED | discovery-search GitHub for `com.firsttouchgames.dls7` / DLS datamining repos |
| user-generated content | comments and posts on all of the above; every unique informative item processed, duplicates/spam/pure reactions filtered as non-informative | 0 | NOT STARTED | follows from community fetching |
| FTG as a company (topic, not a gate category) | business model, monetization, update philosophy, historical behaviour across all DLS versions, what they changed and why | 0 | NOT STARTED | page-render FTG root + search for company/press history |

## Language coverage — BOUNDED by the client's own supported-language list

**Frontier-shaping finding (S-0017):** FTG's App Store Information block enumerates exactly 15 client languages — **English, Arabic, Dutch, French, German, Indonesian, Italian, Japanese, Korean, Portuguese, Russian, Simplified Chinese, Spanish, Traditional Chinese, Turkish**. This converts PROMPT.md §2's "every language with a DLS26 community" from an open-ended instruction into a checkable core set, and closes gap G-0011.

The list is a FLOOR, not the boundary (EVERY LIST IS OPEN): a community can exist in a language the client does not ship (e.g. Hindi, Bengali, Vietnamese, Thai, Polish — plausible for this franchise's audience, none of it established), and any such community found is covered and recorded as an addition to this grid, not excluded because the client does not list it.

| Language | Client-supported | Searches run | Sources found | Extracted | Notes |
|---|---|---|---|---|---|
| en | yes | 1 | 5 (FTG site, Play listing, App Store listing, Play event page, sakibpro home; + 1 SEO farm, 1 aggregator echo) | partial | version resolved; two live events found |
| ar | yes | 0 | 0 | 0 | owed |
| nl | yes | 0 | 0 | 0 | owed |
| fr | yes | 0 | 0 | 0 | owed |
| de | yes | 0 | 0 | 0 | owed |
| id | yes | 0 | 0 | 0 | owed |
| it | yes | 0 | 0 | 0 | owed |
| ja | yes | 0 | 0 | 0 | owed |
| ko | yes | 0 | 0 | 0 | owed |
| pt | yes | 0 | 0 | 0 | owed |
| ru | yes | 0 | 0 | 0 | owed |
| zh-Hans | yes | 0 | 0 | 0 | owed |
| es | yes | 0 | 0 | 0 | owed |
| zh-Hant | yes | 0 | 0 | 0 | owed |
| tr | yes | 0 | 0 | 0 | owed |
| any non-client language with a community | n/a | 0 | 0 | 0 | discovered opportunistically; recorded here when found |

## Technical-layer coverage (every layer of every source — surface is never enough)

| Layer | Attempted | Result |
|---|---|---|
| Surface page content | yes (FTG /games) | retrieved |
| Frontend JavaScript of database sites (e.g. SakibPro) | no | owed — page-render returns rendered text; JS/API inspection needs the shell, which cannot reach those hosts (ISS-002). Attempt-and-record owed before any wall entry |
| API calls / network requests of tools | no | owed; likely capability gap → must be recorded as such, with the missing capability and the resulting gap, per PROMPT.md §2 |
| Underlying data structures / DB schemas | no | owed (Step 2 for the client; database APIs for tools) |
| APK client code and assets | no | STATE_2; binary route constrained (S-0008) |
| Hidden/undocumented functionality | no | owed |
| Video subtitle/transcript text | no | capability question open (no yt-dlp/ffmpeg; YouTube shell-blocked) — must be tested, not assumed |
| Comment threads | no | owed |

## Mandatory Core Gameplay Taxonomy Gate (Step 1 completion precondition)

| Dimension | Status | Evidence so far |
|---|---|---|
| 1. Training & Coaching architecture | SUBSTANTIAL AS A HYPOTHESIS, ZERO AS VERIFIED FACT | A complete third-party model recovered (S-0020): 4 coach types (Fitness SPE/ACC/STA/STR, Technical CON/PAS/SHO/TAC, Special ALL STATS, Goalkeeping GKR/GKH) × 3 rarities (Common/Rare/Legend) priced in GEMS (25/75/225, 25/75/225, 90/240/400, 15/40/150); 100% development weight → +10 OVR at 10% per +1; per-attribute weighting (CON/SPE costlier than STA); GK exception at 22 points / 2.2 per +1 OVR (closes on the same +10); a claimed 1-of-3 attribute pick worth +2 with DISCARD & RESHUFFLE; a "COACHES WASTED" readout; a FACILITY DISCOUNT ladder 0/5/10/15/20/30%. ALL from one domain whose authority over numbers was withdrawn (DR-001) — every value is a falsifiable hypothesis with a named verification plan (user's own coaching screen first). See `kb/topics/coaching_and_upgrade_system.md`. Earlier: | Official: "Use Coaches to develop your players technical and physical abilities" (S-0011/S-0015) — confirms a technical/physical split in FTG's own words; **"Special Coach Packs"** named in the 12.200 changelog ("Develop your favourite players more easily", S-0017). Categories, rarity, yields, breakthrough probabilities, caps, pacing: nothing. Unverified lead: a review alleges buying a coach then paying again to apply training (S-0012) |
| 2. Economic & Currency matrix | PARTIAL — official currencies/IAP plus a third-party facility-discount lead | THIRD-PARTY LEAD (S-0020, authority withdrawn): a facility grants a coaching-cost discount in six steps to 30% — the first quantitative lead on the facility compounding return curve; coaches priced in gems. Earlier: | Official (S-0017): two currencies named **Coins** and **Gems**; a full US IAP ladder ($1.99–$16.99) incl. a **Season Pass** at $3.99; Apple declares **"Contains: Loot Boxes"** and Google "Includes Random Items"; four facilities named (Stadium, Medical, Commercial, Training); Agents and Scouts; Coaches for technical/physical development; third-party advertising. Which currency buys what, all income rates, facility cost/return curves, ad-reward caps: nothing verified. Unverified user-generated leads: two-stage coach fee allegation, no coin refund on sale (S-0012). See `kb/topics/economy_currencies_and_iap.md` |
| 3. Live Operations & Progression tracks | SUBSTANTIAL IN SHAPE, ZERO FIRST-PARTY MECHANICS | THE PRIZE LADDER'S MECHANICS FOUND from one guide (S-0026): Dream Points per match with mode-dependent rates (DLS Live PvP >> Career; tournaments pay completion bonuses), cumulative tiers, four free milestone signings at 62.5k/115k/175k/250k DP (Berbatov, Essien [Version 2006], Cole, Petit = the four Classic cards), milestone rewards of coins/gems/coaches/**special agents** (tying the ladder into the Cult Heroes draw economy). FTG's only official word on the ladder remains one sentence. Earlier: OFFICIAL (S-0015/S-0016/S-0017): **Prize Ladder** is FTG's own term and one is LIVE ("English League Classics"); **Cult Heroes** Special Players collection LIVE with "boosted attributes", window ends 10/14; paid **Season Pass** exists; "regular seasons and events"; daily scenarios; Dream Draft; Global Leaderboards and Events. Accumulation/reset mechanics, reward tables, free-vs-paid tracks: nothing verified. Earlier: Official: "regular seasons and events", "daily scenarios", "Dream Draft", "Global Leaderboards and Events", changelog "Special Players – 'Cult Heroes'", store event ending 10/14 (S-0011/S-0012). Non-official, Speculative: Dream Star Event (Mar 26), Summer Update "Dynamic Stars / Classic Icons / Economy Reset" (May 26-27), World Cup Heroes (Jul 1), World Winners (Jul 13) — all one incentivised source (S-0013/S-0014). Accumulation and reset mechanics: still nothing. See `kb/topics/live_ops_events_and_cards.md` |
| 4. Match Physics & Energy dynamics | UNANSWERED | Official copy claims "full 3D motion-captured kicks, tackles, celebrations and goalkeeper saves" and "new animations and improved AI" (S-0011) — marketing, no stamina/fatigue/recovery mechanics. Medical facility is named (S-0011) but its effect is not established |
| 5. Tactical & Control mechanics | FRAGMENT | Official: formations/tactics not described in the listing at all; manager and kit customisation confirmed. Unverified user-generated leads: no control remapping in settings, pass-target selection picking distant players, player-switch input delay 0.5–2 s, "c spamming" as an exploited attack pattern (S-0012). Includes the user-stated no-position-locking claim (G-0001), Skeptic verification owed |
| 6. Other discovered subsystems | none discovered yet | — |

A dimension is satisfied by a positive sourced finding OR by an exhaustively-searched-and-documented open gap; a genuinely unanswered dimension after exhaustive search across every source type does not block the gate, provided the negative result and the sources exhausted against it are written to the KB.

## Consecutive-no-new-information run (exhaustion condition 2)

| Checkpoint | Sources reached since last checkpoint | New information found? | Run length |
|---|---|---|---|
| 2026-09-27T17:28Z | 2 | YES (identity, package id, store listings, version conflict, live-ops fragment, FTG portfolio) | 0 |
| 2026-09-27T17:36Z | 2 (Play Store listing ×2 chunks = S-0011/S-0012; sakibpro.com ×2 chunks = S-0013/S-0014) | YES — 18 officially named systems, official changelog, developer entity, second official domain, data-safety disclosure, active store event ending 10/14, 3 user reviews, SakibPro's 3 tools + ~15 article leads, a non-official 2026 event timeline, and 9 new terminology leads | 0 |
| 2026-09-27T21:20Z | 2 image searches + 2 image reads + 1 discovery search (S-0030 ladder renders read; S-0031 DP rates; S-0032 artwork attempt) | YES — dated DP rate sets from four independent parties with the mode differential constant across them (placed at Community Consensus, R-0006, magnitudes declared version-sensitive); gems-buy-ladder-speed boost economy; 90-day ladder cycle with claim-or-lose vs FTG's 10/14 (two clocks, unresolved); Progression Bank / Season Points / Global Challenge Cup named; earlier ladder cycles documented; ladder renders corroborate Essien/Petit fields but open a design question (G-0046); official artwork still unfound by image search (route limitation logged) | 0 |
| 2026-09-27T20:50Z | 2 page-renders (S-0028 full ladder page; S-0029 Isco fidelity check) | PARTIAL — year stamps for all four ladder cards (2011/2006/1994/1999), four ladder card images found (unread), a mod-APK route entered with risk assessment owed (G-0043), a French comment seam; and the second fidelity card matching nine of ten with one field quarantined in open conflict (G-0041, R-0005) | 0 |
| 2026-09-27T20:24Z | 1 search + 1 page-render (S-0026 ladder mechanics; S-0027 the DR-001 decisive check) | YES — the Prize Ladder's mechanics found in shape (DP, tiers, four free signings, agent rewards, the PvP-vs-Career DP differential); and the decisive fidelity check: SakibPro's Dybala row matches an in-game capture on ten of ten fields, splitting DR-001's authority (rows partially restored case-by-case, prose still withdrawn) and promoting one card to High Confidence (R-0004) | 0 |
| 2026-09-27T19:50Z | 1 re-fetch + 1 discovery search + 1 image search + 2 image reads (S-0023, S-0024, S-0025) | YES — DLS26-C1 resolved as a FALSE CONFLICT (13.410 → 13.420 → 13.430 across Aug 20/Sep 1/Sep 16, all first-party); the Cult Heroes acquisition mechanic shaped (collectible agents opened randomly; 3 winnable via Online Events; Season Pass card source); a THIRD database breaking open the card taxonomy (Secret players, Star players, World Winners, World Heroes, Kick-off Stars, Team of 2025, Champion); the first DIRECT in-game evidence — two captures yielding stat octets, year stamps, localized codes, and the LIVE TRANSFERS / SCOUTS / AGENTS screens; r/DreamLeagueSoccer found; TWO TIER PROMOTIONS (R-0002, R-0003) | 0 |
| 2026-09-27T18:42Z | 3 fetches (2 successes + 1 tool-error: sakibpro trending.php = S-0019, simulator.html = S-0020; one fetch_page call failed on a stale signed proxy URL and was retried with the real URL) | YES — a 17-player "latest update" enumeration resolving into 12 Cult Heroes + 4 Classic + 1 Season Pass card with positions, OVRs, heights, ages, nationalities and numeric ids; a complete third-party coaching model (4 types × 3 rarities, gem prices, 100%-weight → +10 OVR ceiling, GK 22-point exception, 1-of-3 +2 pick with reshuffle, coaches-wasted, facility discount to 30%); the card-type URL/asset structure; two structural hypotheses (contiguous id blocks per release batch; third-party trackers moving faster than official changelogs); DR-001 escalated with two further instances | 0 |
| 2026-09-27T18:12Z | 3 fetches (App Store chunk 0 = S-0015; Play eventdetails = S-0016; App Store chunk 5 = S-0017) | YES — **version resolved (13.430)**; prior version 12.200 dated 06/04/2025 recovered with two official mechanic names (Player Recovery, Special Coach Packs); **"Prize Ladder" confirmed as an official term with one LIVE**; Cult Heroes confirmed LIVE and ending 10/14; **Coins and Gems** named; full US IAP price ladder incl. Season Pass; **Loot Boxes** declared; the client's **15 languages** enumerated (bounding the language frontier); developer data-collection declarations (server-side User ID, Purchase History, Gameplay Content); iOS 13+ / controller / Game Center; slug redirect proving one retitled product | 0 |

## Resumption point (mirrored in HANDOFF.md)

Last action: fetched the official Play Store listing (S-0011/S-0012) and SakibPro home (S-0013/S-0014); wrote `kb/topics/gameplay_systems_inventory.md` and `kb/topics/live_ops_events_and_cards.md`; resolved DLL → Dream League Live plus the facility, division and Special Players terminology; advanced DLS26-C1 (update date confirmed, number still open); added gaps G-0006..G-0009.
Next specific action: page-render `https://apps.apple.com/us/app/dream-league-soccer-2020/id1462911602?ls=1` — Apple's version history carries numbers and dates, the strongest remaining web route for DLS26-C1. Then in order: `sakibpro.com/players` (candidate-pool enumeration source); `sakibpro.com/players/simulator.html` (upgrade/ceiling model); the Play Store eventdetails page (10/14 event); `ftgames.com` + `/privacy-policy`; `firsttouchgames.com` root and support; SakibPro's event articles; then Reddit/YouTube/X/TikTok/Facebook/wikis; then non-English languages; then GitHub technical repos via the proven codeload route; then FTG-as-a-company.
