# T101 — targeted FTG/official-channel searches; no page-level evidence

Date: 2026-10-06 Asia/Dhaka. Four `functions.web_search` retrievals; each returned `status=success`. The search tool does not expose HTTP status. **No result page was fetched.** Search snippets are discovery only and are not promoted as game facts.

## Exact searches and outcomes
1. `site:ftgames.com "Cult Heroes" "Dream League Soccer" 2026 First Touch Games official` — generic FTG `/games`, `/terms-of-use`, `/about` and known Help Center results; no Cult Heroes route/reward or DLS26 position-lock detail.
2. `site:youtube.com/@dreamleaguesoccer "Cult Heroes" DLS 26 Agents First Touch Games` — returned `https://www.youtube.com/@dreamleaguesoccer7906`; its Arabic-language description labels itself a DLS channel and mentions hacks. FTG ownership is unverified. Retain only as an affiliation-check candidate, not as primary evidence or a source for gameplay claims.
3. `site:youtube.com/@FirstTouchGames "Cult Heroes" "DLS26" OR "Dream League Soccer 2026"` — returned the generic `https://www.youtube.com/@firsttouchgames` channel profile already listed in the ledger; no event-specific video/result.
4. `site:ftgames.com "Cult Hero Agents" DLS26` — only the generic FTG corporate landing page (search result dated 2018); no event-specific route or DLS26 position information.

The FTG/YouTube results were generic or already known. The unaffiliated/unverified channel is not evidence and must not be cited as FTG. No result snippets establish event availability, acquisition, cost, rewards, or position-lock behavior. No absence inference.

## Recovery and ledger
T101 opened on a reset `fb9a2c0` checkout. Clock was recorded first (`2026-10-06 05:37:53 +06`). Archived 282 files to `/tmp/dls26-t101-recovery-20261006053757.tar.gz`, SHA-256 `284feae2da370fabc8933b1700c6080970f6b82afaa9d9b3f7b7dfbfff3557cd`; fetched/restored `6350670`, upstream, and repo-local identity. After overlay, only the T101 clock-start append differed; no untracked paths. No loss/force-push. ISSUE-0014 recovery occurrence #63.

Four retrievals, within the six-retrieval limit; no page fetches. Four distinct search records added; one unverified channel URL retained as an affiliation-check lead. Ledger close: **704 entries / 522 unique visited URLs / 405 unvisited leads**. DLS26 no-position-lock remains `user-stated` and unverified pending Step-3 device setup. Cult Heroes availability, route, cost, and rewards remain unresolved; no spending advice, dimension closure, or exhaustion declaration.


## T102 provenance correction

T101’s four discovery records initially inherited a prior search entry’s `source_id`, `search_query`, `search_results`, and fetch timestamp. T102 replaced those copied values with four distinct source IDs, the exact T101 queries and returned results, the canonical `retrieval_tool` field, and transparent status/summary fields. Individual web-search call timestamps were not exposed; the timestamp in the corrected records is T101 closeout reconciliation time, not a claimed per-call time. No new retrieval occurred during this correction. Counts remain 704 entries / 522 visited / 405 unvisited.
