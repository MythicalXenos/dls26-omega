# STATE_1 RESEARCH SWEEP — FRONTIER TRACKER

Human-readable companion to `logs/sources_visited.json`. The JSON log is the mechanical basis of any exhaustion declaration (PROMPT.md §2 MECHANICAL EXHAUSTION INVARIANT); this file tracks the frontier's shape so that "what is left" is a recorded fact rather than a feeling.

**Sweep:** bootstrap Step 1, opened 2026-09-27T17:22Z. **Sources visited: 6 distinct origins across 9 content fetches (S-0001, S-0002, S-0011..S-0017) plus capability probes S-0003..S-0010.** **Scope:** everything about DLS26 and everything around it (PROMPT.md §13 Step 1) — the widest scope a trigger can set. **Organization:** by SOURCE, not by question; each source is exhausted before moving on, and organizing by source never narrows scope.
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
| 1. Training & Coaching architecture | FRAGMENT | Official: "Use Coaches to develop your players technical and physical abilities" (S-0011/S-0015) — confirms a technical/physical split in FTG's own words; **"Special Coach Packs"** named in the 12.200 changelog ("Develop your favourite players more easily", S-0017). Categories, rarity, yields, breakthrough probabilities, caps, pacing: nothing. Unverified lead: a review alleges buying a coach then paying again to apply training (S-0012) |
| 2. Economic & Currency matrix | PARTIAL — currencies and prices official, spending rules unknown | Official (S-0017): two currencies named **Coins** and **Gems**; a full US IAP ladder ($1.99–$16.99) incl. a **Season Pass** at $3.99; Apple declares **"Contains: Loot Boxes"** and Google "Includes Random Items"; four facilities named (Stadium, Medical, Commercial, Training); Agents and Scouts; Coaches for technical/physical development; third-party advertising. Which currency buys what, all income rates, facility cost/return curves, ad-reward caps: nothing verified. Unverified user-generated leads: two-stage coach fee allegation, no coin refund on sale (S-0012). See `kb/topics/economy_currencies_and_iap.md` |
| 3. Live Operations & Progression tracks | PARTIAL — official event structures now named, mechanics still unanswered | OFFICIAL (S-0015/S-0016/S-0017): **Prize Ladder** is FTG's own term and one is LIVE ("English League Classics"); **Cult Heroes** Special Players collection LIVE with "boosted attributes", window ends 10/14; paid **Season Pass** exists; "regular seasons and events"; daily scenarios; Dream Draft; Global Leaderboards and Events. Accumulation/reset mechanics, reward tables, free-vs-paid tracks: nothing verified. Earlier: Official: "regular seasons and events", "daily scenarios", "Dream Draft", "Global Leaderboards and Events", changelog "Special Players – 'Cult Heroes'", store event ending 10/14 (S-0011/S-0012). Non-official, Speculative: Dream Star Event (Mar 26), Summer Update "Dynamic Stars / Classic Icons / Economy Reset" (May 26-27), World Cup Heroes (Jul 1), World Winners (Jul 13) — all one incentivised source (S-0013/S-0014). Accumulation and reset mechanics: still nothing. See `kb/topics/live_ops_events_and_cards.md` |
| 4. Match Physics & Energy dynamics | UNANSWERED | Official copy claims "full 3D motion-captured kicks, tackles, celebrations and goalkeeper saves" and "new animations and improved AI" (S-0011) — marketing, no stamina/fatigue/recovery mechanics. Medical facility is named (S-0011) but its effect is not established |
| 5. Tactical & Control mechanics | FRAGMENT | Official: formations/tactics not described in the listing at all; manager and kit customisation confirmed. Unverified user-generated leads: no control remapping in settings, pass-target selection picking distant players, player-switch input delay 0.5–2 s, "c spamming" as an exploited attack pattern (S-0012). Includes the user-stated no-position-locking claim (G-0001), Skeptic verification owed |
| 6. Other discovered subsystems | none discovered yet | — |

A dimension is satisfied by a positive sourced finding OR by an exhaustively-searched-and-documented open gap; a genuinely unanswered dimension after exhaustive search across every source type does not block the gate, provided the negative result and the sources exhausted against it are written to the KB.

## Consecutive-no-new-information run (exhaustion condition 2)

| Checkpoint | Sources reached since last checkpoint | New information found? | Run length |
|---|---|---|---|
| 2026-09-27T17:28Z | 2 | YES (identity, package id, store listings, version conflict, live-ops fragment, FTG portfolio) | 0 |
| 2026-09-27T17:36Z | 2 (Play Store listing ×2 chunks = S-0011/S-0012; sakibpro.com ×2 chunks = S-0013/S-0014) | YES — 18 officially named systems, official changelog, developer entity, second official domain, data-safety disclosure, active store event ending 10/14, 3 user reviews, SakibPro's 3 tools + ~15 article leads, a non-official 2026 event timeline, and 9 new terminology leads | 0 |
| 2026-09-27T18:12Z | 3 fetches (App Store chunk 0 = S-0015; Play eventdetails = S-0016; App Store chunk 5 = S-0017) | YES — **version resolved (13.430)**; prior version 12.200 dated 06/04/2025 recovered with two official mechanic names (Player Recovery, Special Coach Packs); **"Prize Ladder" confirmed as an official term with one LIVE**; Cult Heroes confirmed LIVE and ending 10/14; **Coins and Gems** named; full US IAP price ladder incl. Season Pass; **Loot Boxes** declared; the client's **15 languages** enumerated (bounding the language frontier); developer data-collection declarations (server-side User ID, Purchase History, Gameplay Content); iOS 13+ / controller / Game Center; slug redirect proving one retitled product | 0 |

## Resumption point (mirrored in HANDOFF.md)

Last action: fetched the official Play Store listing (S-0011/S-0012) and SakibPro home (S-0013/S-0014); wrote `kb/topics/gameplay_systems_inventory.md` and `kb/topics/live_ops_events_and_cards.md`; resolved DLL → Dream League Live plus the facility, division and Special Players terminology; advanced DLS26-C1 (update date confirmed, number still open); added gaps G-0006..G-0009.
Next specific action: page-render `https://apps.apple.com/us/app/dream-league-soccer-2020/id1462911602?ls=1` — Apple's version history carries numbers and dates, the strongest remaining web route for DLS26-C1. Then in order: `sakibpro.com/players` (candidate-pool enumeration source); `sakibpro.com/players/simulator.html` (upgrade/ceiling model); the Play Store eventdetails page (10/14 event); `ftgames.com` + `/privacy-policy`; `firsttouchgames.com` root and support; SakibPro's event articles; then Reddit/YouTube/X/TikTok/Facebook/wikis; then non-English languages; then GitHub technical repos via the proven codeload route; then FTG-as-a-company.
