# MECHANISM 3 — SOURCE-TYPE COVERAGE WALK (category by category)
Walked 2026-10-17T20:56Z (session sess-20261017-001, turn 9) against `step1_epochs/EPOCH_CONTRACT_DRAFT.md`. Each category states what was searched, what was found, and what the last attempt returned. This is the walk the Exhaustion Declaration Protocol requires; it is **not** an exhaustion declaration, because Condition 1 and Condition 2 remain unmet.

## 1. Official sources
- **Searched:** FTG support portal (30-article inventory + 13 additionally discovered), Google Play listing, App Store US and ID-locale listings, FTG core-principles and ToU pages, official social channels (URLs known).
- **Found:** 26/30 section-listed articles captured (22 with EV records, 4 summary-only), 13 additional articles, store metadata, IAP catalogue, version histories, policy pages.
- **Last attempts:** support.ftgames.com and firsttouchgames.zendesk.com → TLS failure, null HTTP status (S-055/S-056). No official host is reachable from this sandbox.
- **Unanswered within category:** three article bodies (#19, #26, #27), one moved update slug, official social feeds, comment threads.
- **Verdict:** category worked to the limit of access; not exhausted.

## 2. Third-party databases and tools
- **Searched:** sakibpro (DB, price calculator, comparison, simulator), dlsinside (version table, roster, card taxonomy), dreamkitsapp, dlskits, APKMirror/APKCombo/AppBrain/AppMagic/AppGlint mirrors, z2u (RMT marketplace — flagged).
- **Found:** version-code table, roster counts and card-collection counts, pricing model claims, upgrade simulator claims, store-metric mirrors.
- **Last attempts:** dlsinside.com → TLS failure (S-057). No live database is reachable.
- **Unanswered:** any current live roster/card list; the JS-rendered projections were never fully extracted even when reachable.
- **Verdict:** historically covered, currently blocked.

## 3. English-language community
- **Searched:** Reddit r/DreamLeagueSoccer (3 threads referenced), gamingonphone, thesoccerera, sportsdunia, dlskits, z2u, bluestacks, mwm.ai, fifaworldcupnews, App Store/Play review text.
- **Found:** snippets only — formation opinions, launch sentiment, rating lists, economy complaints.
- **Last attempts:** all hosts TLS-blocked; Reddit also carries a recorded 403 bot-wall from the earlier environment.
- **Unanswered:** every full-thread and full-article projection (8 refs IN_PROGRESS).
- **Verdict:** **weakest covered category** — snippet-level. This is the single biggest coverage deficit in the epoch.

## 4. Non-English community
- **Searched:** ES (kotaku ES, tuapppara, mundodls), VI (download.com.vn ×4 + the main guide chunks), TR (dlshile — untrusted, risk-only), ID (industry.co.id guide, store locale), PT (gameoverdrive, dreamkitsapp).
- **Found:** substantive VI and ID/PT material (economy, prize ladder, division structure, card taxonomy); ES only snippets.
- **Last attempts:** all hosts blocked; VI main guide captured through chunk 2/4 previously.
- **Unanswered:** ES full articles (role demands, camera/controls advice), VI tail chunk, TR untrusted family.
- **Verdict:** partial — genuinely multilingual coverage exists, but ES and TR remain thin.

## 5. Technical sources
- **Searched:** GitHub repository search (4 queries), GitHub code search, npm registry search, pypi reachability.
- **Found:** **negative** — fan sites, kit generators, a Unity prototype, hack-spam packages; no APK, save format, stat table or decompilation corpus (NEG-004).
- **Last attempts this turn:** none repeated; the identical queries are recorded and will not be re-run without a new lead.
- **Unanswered:** any permitted static-analysis layer (store metadata is already covered under official; binary analysis is prohibited — OBS-013).
- **Verdict:** covered to the permitted limit, with a negative result. The category cannot reach "exhaustive" while the only remaining method is the one the EULA forbids; that is an access/capability boundary, recorded as such, not as effort withheld.

## 6. User-generated content
- **Searched:** YouTube (pack-opening and guide videos referenced), TikTok discover pages, creator-demostration indexes.
- **Found:** partial — a few referenced videos, no transcribed content.
- **Last attempts:** blocked hosts.
- **Unanswered:** creator-demonstration sampling, any transcribed guide.
- **Verdict:** partial, blocked.

## 7. Any further type the work turned up
- **Repository family (this session):** GitHub as a *source* was swept and as a *transport* carried the continuity import (S-063). Kept distinct from official sources.
- **Environment/capability observations:** not a knowledge source; recorded separately so they are never counted as coverage.
- **User-supplied captures:** a source type that does not exist yet in this epoch but will (device screenshots). Declared here so its absence is not mistaken for a category that was tried.

## Result
| Category | State |
| --- | --- |
| Official | worked; access-limited |
| Third-party databases | historically covered; blocked |
| English community | **snippet-only — largest deficit** |
| Non-English community | partial |
| Technical | negative to permitted limit; further depth prohibited |
| UGC | partial |
| Further types | repository family covered; user captures not yet available |

Exhaustion cannot be declared: two categories are blocked rather than worked, and the "no new information" run has never been reached for the community family.
