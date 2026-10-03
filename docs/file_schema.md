# Repository file schema — v1 bootstrap

**Created:** 2026-10-02 (UTC clock observed this turn). **Status:** initial structure; revise only with a migration plan and preserve the prior schema.

## Record ownership and paths

- `DLS26_OMEGA_PROMPT.md` — intended immutable, stable-path copy of the user prompt. Current file is a capture-status placeholder, explicitly not authoritative; resolve at first contact. Archived prompt versions belong in `docs/prompt_archive/`; `docs/prompt_changelog.md` records proposed and adopted changes.
- `bootstrap/capability_inventory.md` — point-in-time observed tools, absences, and limits; re-check at bootstrap/session start.
- `OPERATIONAL_RULES.md` — behavioral reset derived from the prompt, not a substitute for it. Pending State 4 construction; until complete, not a valid reset document.
- `SESSION_HANDOFF.md` — compact, atomically updated resumption point and current obligations. Branch records file state; handoff records intent.
- `knowledge/knowledge_base.md` — current claims; source trace, verification date and method, first-publication dates when relevant, checkable origin or explicit absence, confidence tier, volatility tier, applicable deception/datamining labels, version/date scope, and links to logs. Replaced claims remain marked, not deleted.
- `knowledge/gaps.md` — open questions vs. evidence-backed negative findings; a negative finding names sources and game version and is reopened by a relevant patch.
- `knowledge/user_profile.md` — user-stated preferences, game state, decisions, skill/understanding, and unknowns. Game state is always last-known with timestamp and user-stated vs extracted provenance.
- `knowledge/irreversible_action_list.md`, `watchlist.md`, `deception_register.md`, `revision_register.md`, `volatility_model.md`, and `milestone_tracker.md` — the dedicated records described by their filenames and the governing instructions.
- `logs/sources_visited.json` — machine-readable retrieval ledger and exhaustion frontier. It is the evidence source for coverage counters and exhaustion declarations.
- `logs/main_operational_log.md` — timestamped event log, organized by named categories; recommendations carry stable topic names.
- `logs/exhaustion_declarations.md` — declarations with structured evidence for both exhaustion conditions, source/language/type checklist, no-new-information run, and blocked routes.
- `issue_tracker.md` — defects, failures, anomalies, repeated patterns and investigations.
- `research_queue/active.md` and `research_queue/archive.md` — active queue and resolved/deprioritized history.
- `audits/` — one self-contained Mechanism 9 package per triggering period; update an unsent package in place.
- `source_archive/` — complete raw source payloads when necessary; main log points to the file. Sanitize credentials before committing; do not export credential-bearing payloads.
- `raw_game_data/` — read-only external extractions; never alter source files. Keep extraction metadata adjacent and check staleness before use.
- `scripts/` and `tools/` — versioned, documented scripts/utilities with changelogs. Mac-side scripts are delivered for the user to run, not run from this sandbox.
- `snapshots/` — immutable, dated KB snapshots; never overwrite earlier snapshots.

## Source ledger structure

Each `logs/sources_visited.json` entry records: `source_id`, exact `url`, normalized `domain`, fetched timestamp, retrieval role (`page-render`, `discovery-search`, or `shell/script` as actually used), tool name, HTTP status or an explicit non-HTTP/unknown marker, source type and language, payload path and/or complete extracted text, payload summary, `complete`/`partial` processing state, source-screen outcome (including clean outcomes), conflicts, affected KB claims, and `discovered_not_yet_visited` (reachable URLs/routes/files/endpoints only; questions belong in `knowledge/gaps.md`). Store raw content when large; do not put secrets in the ledger. Search queries and results without fetched pages are also recorded as discovery events, but a question is never represented as a lead. A visit is not exhausted until its layers and discovered leads are handled or recorded as blocked.

Coverage grids, counters, and exhaustion status are derived from this ledger at each turn boundary, not manually maintained. A URL without a result/status or a clear failure note is not a completed visit. Search-result snippets are partial evidence.

## Labels and timestamps

- Use only the confidence-tier names defined in the prompt, and name the system whenever a tier word could be ambiguous. User reports are labeled `user-stated` and are never silently promoted to verified game data.
- Every KB claim has a volatility tier from entry. Where there is no observed basis, use Critical until observations justify a change.
- Timestamp records with a clock reading made in the same turn, preferably ISO 8601 UTC plus Asia/Dhaka display when useful. If no clock is available, say so.
- English for repo records; retain original non-English text beside an English translation.

## Integrity, history, and turn-boundary checks

- Never edit archived KB snapshots or archived prompt versions. New evidence revises the live claim and appends a log entry.
- At each turn boundary reconcile workspace and branch contents, derive frontier movement from the source ledger, update handoff atomically, check file/repo sizes, and preserve any divergence before resolving it.
- Keep generated/cache files out of Git; raw external inputs are read-only and credential-scanned before commit.
- This schema is not evidence of game mechanics. Preliminary DLS26 storefront/help/search research is recorded in the ledger and source archive; it was run before the STATE_0 prompt-capture gate was satisfied. See `ISSUE-0004`; do not mark STATE_0 complete or treat the first research block as a completed/exhausted sweep.

---
## Update 2026-10-03 (session arena/01a1022d)
- New path: `prior_sessions/<date>_<session-id>/` — frozen, read-only archives of earlier sessions' artifacts (never interpreted as active state; read on demand).
- `DLS26_OMEGA_PROMPT.md` intentionally **absent** under capture status DIGEST-ONLY; a placeholder is forbidden. `OPERATIONAL_RULES.md` (RULES DIGEST) holds behavioral authority until a verified prompt file exists.
- Ledger merge pending (queue-High): active ledger `logs/sources_visited.json`; archived ledger in `prior_sessions/2026-09-27_01a0e3cd/logs/sources_visited.json`.
