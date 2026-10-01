# RESEARCH QUEUE — ACTIVE

Per PROMPT.md §3 Mechanism 4. **During sweeps and all bootstrap steps this queue is INACTIVE for everything except inaccessible wall sources** — all other discoveries are followed immediately, regardless of depth. During operational work it captures only discoveries genuinely unrelated to the current task that would derail it if pursued now. When uncertain: follow immediately.

Queue-priority tiers (NOT volatility tiers — TIER RULE): queue-Critical = directly affects a recommendation about to be acted on or blocks a pending task; queue-High = affects pending recommendations or active decisions; queue-Medium = improves knowledge quality, no immediate impact; queue-Low = useful context, no current application. Within a tier, more recent = higher priority. Nothing is discarded — irrelevant items move to `research_queue_archive.md` with a reason. Both files are committed after every update to either.

Format: SCHEMA.md §2.5.

---

## Wall sources (the only entries permitted during the bootstrap sweep)

*None yet. No source may be entered here until every applicable retrieval capability has been attempted and failed — and a shell HTTP 000 is not an attempt by the capable role (ISS-002).*

## Items queued during operational work (post-bootstrap)

*None — the system is in STATE_1_RESEARCH_SWEEP.*

## Added 2026-09-27T18:28Z (session 1 turn 2) — TECHNICAL: reaching the sakibpro.com player-database rows (gap G-0019)

The database page is client-side rendered: a page-render returned the shell, filters, prose and tool links but NO rows ("Loading Players Database..."). So PROMPT.md §10 WORKFLOW step 3 (enumerate the candidate pool) cannot be satisfied from it as-is. This is an OPEN gap, not a "does not exist" finding and not a declaration that the host is walled off.

Probe order, cheapest first, each attempted by page-render (bash cannot reach non-GitHub/non-PyPI hosts, and a shell failure is NEVER sufficient to declare a source unreachable):
1. `https://sakibpro.com/players/trending.php` — server-rendered "Upcoming Players" page; may expose real player names, including Cult Heroes cards. **HIGHEST VALUE AND TIME-SENSITIVE: the Cult Heroes window is stated to end 10/14.**
2. `https://sakibpro.com/players/simulator.html` — a static `.html` tool is the likeliest place to embed or reference a data file path directly.
3. `https://sakibpro.com/players/price-calculator.php` and `/players/compare.php` — both must read player data from somewhere.
4. The site's own JS bundles, read for the endpoint the database calls (an XHR/fetch URL, a `.json` path, or a `.php` handler).
5. Common data paths under `/players/` (`data.json`, `players.json`, `db.json`, `api/…`) and the sitemap.
6. A SECOND player database, in any of the 15 client languages — now MANDATORY rather than optional, because DR-001 withdrew authority from SakibPro's numbers and with one source there is no cross-check for any third-party value in this project.

If none is reachable from this environment, record the negative result as an OPEN gap with the attempts listed, and treat Step 2 client extraction as the only remaining route to the candidate pool — which raises the stakes on gap G-0004 (whether an APK or extracted asset archive is reachable at all).
