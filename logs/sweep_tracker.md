# STATE_1 RESEARCH SWEEP — FRONTIER TRACKER

Human-readable companion to `logs/sources_visited.json`. The JSON log is the mechanical basis of any exhaustion declaration (PROMPT.md §2 MECHANICAL EXHAUSTION INVARIANT); this file tracks the frontier's shape so that "what is left" is a recorded fact rather than a feeling.

**Sweep:** bootstrap Step 1, opened 2026-09-27T17:22Z. **Scope:** everything about DLS26 and everything around it (PROMPT.md §13 Step 1) — the widest scope a trigger can set. **Organization:** by SOURCE, not by question; each source is exhausted before moving on, and organizing by source never narrows scope.
**Exhaustion declaration:** NONE. Neither condition is met: unvisited leads exist (condition 1 fails) and new information is still arriving from every reached source (condition 2 fails).

## Coverage grid — Mechanism 3 gate categories × progress

| Source type (gate category) | Planned sources | Visited | Status | Next specific action |
|---|---|---|---|---|
| official | FTG root, /games, /support, patch notes, Facebook, Instagram, TikTok, X/Twitter, YouTube, Play Store (all regions), App Store (all storefronts) | 1 (FTG /games) | PARTIAL | page-render Play Store listing for `com.firsttouchgames.dls7` |
| third-party databases & tools | SakibPro (every tool, its code, API calls, undocumented functionality), plus every other DLS database/tool found — the list is discovered, not prescribed | 0 | NOT STARTED | page-render sakibpro.com (never attempted by a capable role; shell 000 is not an attempt) |
| English-language community | Reddit (r/DreamLeagueSoccer + any other), YouTube (titles, descriptions, comments, subtitles/transcripts), Discord (public servers), X, TikTok, Facebook groups, forums, wikis, guide sites, blogs, app-store reviews | 0 | NOT STARTED | page-render the Play Store reviews + locate the subreddit(s) |
| non-English community | Turkish, Arabic, Portuguese, Spanish, French, Indonesian, and every other language with a DLS26 community — discovered by search in those languages, not assumed | 0 | NOT STARTED | discovery-search in tr / ar / pt / es / fr / id for the game's own terms |
| technical | APK repositories (apkmirror, apkpure, uptodown), GitHub repos and community datamining dumps (codeload route WORKS), web archives (Wayback), cached pages, public APIs, API responses, code comments, DB schemas | 0 content sources (route proven available) | NOT STARTED | discovery-search GitHub for `com.firsttouchgames.dls7` / DLS datamining repos |
| user-generated content | comments and posts on all of the above; every unique informative item processed, duplicates/spam/pure reactions filtered as non-informative | 0 | NOT STARTED | follows from community fetching |
| FTG as a company (topic, not a gate category) | business model, monetization, update philosophy, historical behaviour across all DLS versions, what they changed and why | 0 | NOT STARTED | page-render FTG root + search for company/press history |

## Language coverage

| Language | Searches run | Sources found | Extracted | Notes |
|---|---|---|---|---|
| en | 1 | 3 (2 distinct origins) | partial | version conflict found immediately |
| tr, ar, pt, es, fr, id, others | 0 | 0 | 0 | owed; each requires searching in that language for the game's own terms |

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
| 1. Training & Coaching architecture | UNANSWERED | none |
| 2. Economic & Currency matrix | UNANSWERED | none |
| 3. Live Operations & Progression tracks | FRAGMENT | store changelog: "New Special Players – 'Cult Heroes' collection, coming soon!" (S-0001) — evidences a live-ops content track, nothing about accumulation/reset |
| 4. Match Physics & Energy dynamics | UNANSWERED | none |
| 5. Tactical & Control mechanics | UNANSWERED | includes the user-stated no-position-locking claim (G-0001), Skeptic verification owed |
| 6. Other discovered subsystems | none discovered yet | — |

A dimension is satisfied by a positive sourced finding OR by an exhaustively-searched-and-documented open gap; a genuinely unanswered dimension after exhaustive search across every source type does not block the gate, provided the negative result and the sources exhausted against it are written to the KB.

## Consecutive-no-new-information run (exhaustion condition 2)

| Checkpoint | Sources reached since last checkpoint | New information found? | Run length |
|---|---|---|---|
| 2026-09-27T17:28Z | 2 | YES (identity, package id, store listings, version conflict, live-ops fragment, FTG portfolio) | 0 |

## Resumption point (mirrored in HANDOFF.md)

Last action: wrote STATE_0 artifacts + opened STATE_1 with S-0001/S-0002 and the version conflict DLS26-C1.
Next specific action: page-render `https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7&hl=en` to resolve DLS26-C1 from a checkable origin, then the App Store listing, then FTG root + /support, then SakibPro, then community sources by language.
