# SCHEMA — persisted artifacts (schema_version 1.0)

Read this file before interpreting or modifying any artifact below. Each row names the owner, the format, the required fields, and the recovery path. Changes need a migration plan and a rollback path; the old schema is kept under docs/schema_history/ (created at the first change).

| Path | Owner | Format | Required fields and notes | Recovery path |
|---|---|---|---|---|
| DLS26_OMEGA_PROMPT.md | user authored; agent persists it | Markdown, verbatim capture | First line verbatim. Capture status: MECHANICAL (with size and SHA-256) or DIGEST-ONLY/transcription. Not yet written (pending in Setup). | Re-persist from the user's paste, or from the last committed version. |
| OPERATIONAL_RULES.md | agent (derived from the prompt) | Markdown digest; Step 4 rebuilds it in compaction-minimal form | Header, exact strings, named-rule entries, recovery order, file map, capture gaps | Rebuild from the prompt file; else the last committed version; else DIGEST-ONLY from the handoff. Logged as DEGRADATION EVENT. |
| PROMPT_CHANGELOG.md | agent proposes; user adopts | Markdown entries | Version (adopted only), date, changes, reason, trigger, supersedes, status (PROPOSED or adopted) | Git history |
| README.md | agent | Markdown index | Pointers to the files above | Regenerate |
| docs/CAPABILITY_INVENTORY.md | agent | Markdown sections: sandbox, runtimes, absent, network, platform tools, constraints | Observation date and method | Re-probe |
| docs/SCHEMA.md | agent | This file | schema_version | Git history |
| handoff/handoff.md | agent | Markdown, fixed headings: Identity; Bootstrap state; Resumption point; Progress signal; Awaited outcomes; Recorded overrides; Obligations; Anomalies; Scope boundaries | Written atomically (temp file, then rename); committed with the manifest | Previous commit |
| handoff/attention_required.md | agent | Markdown: request, evidence, withheld consequential action, terminal class | Exists only while ATTENTION_REQUIRED is selected | Not applicable |
| logs/turn_manifest.json | agent | JSON object | schema_version, session_id, turn_seq, active_state, active_bootstrap_step, checkpoint_id, continuation_allowed, needs_user, expected_terminal_class, exact_resumption_point, timestamp, status (READY_TO_YIELD), next_state | Previous commit. Never stores its own commit hash. |
| logs/sources_visited.json | agent | JSON object: schema_version and records array | Each record: id, url, domain, retrieved_at (UTC), tool (page-render, discovery-search or shell/script), http_status, payload summary, notes. Append-only. | Git history. Frontier is generated from this file. |
| logs/main_operational_log.jsonl | agent | JSON Lines | Each line: ts (UTC ISO-8601), category (see OPERATIONAL_RULES.md), topic (required for RECOMMENDATION), entry, optional refs. Append-only. | Git history. Rotate to sequentially numbered files past about 5 MB. |
| logs/issue_tracker.md | agent | Markdown entries: ISSUE-NNN, date, category, description, status, log reference | Problems and rule deviations are recorded here as well as in the main log | Git history |
| research/queue/active_queue.md, archive_queue.md | agent | Markdown tables | id, queue priority tier (Critical, High, Medium, Low), item, origin, first_seen, status. Archived items keep their reason. | Both committed after every update to either. |
| kb/topics/*.md | agent | Claim records | claim_id, proposition, build/platform/mode/context, confidence tier, volatility tier (system named), patch and event trigger dimensions, evidence references with origin tags, verification dates, challenges, replacement history | KB snapshots |
| kb/snapshots/<date>_<label>/ | agent | Full copy of kb/ | Kept indefinitely | Not applicable |
| kb/REVISION_REGISTER.md | agent | Markdown entries | timestamp, what changed, before, why, trigger, affected prior advice, topic | Git history |
| kb/IRREVERSIBLE_ACTIONS.md | agent | Markdown list | Each action type: description, why it matters, source ids | Git history |
| kb/GLOSSARY.md | agent | Markdown table | Game term, resolved DLS26 term, source ids, status | Git history |
| kb/VOLATILITY_MODEL.md | agent (STATE_4) | Markdown tables | Each item: tier with system named, patch and event dimensions, last check | KB snapshots |
| kb/README.md | agent | Markdown index | Pointers into kb/ | Regenerate |
| user/USER_PROFILE.md | agent (facts from the user) | Markdown | user-stated facts, preferences, decisions, persistent club and game state fields, known gaps | Git history |
| raw_game_data/ | external scripts; read-only to the agent | Game-native formats | Never modified. Extraction metadata: time, device or build, method. | Re-pull from the device |
| audit/ | agent | One self-contained file per package | Created at Mechanism 9 Occasions | Not applicable |

Not an agent artifact: the browser Auto-Pilot's local record of consumed (session_id, turn_seq, checkpoint_id, HEAD) tuples. It is persisted by the watchdog and is not committed here.

Turn manifest validity, the terminal-line vocabulary and the watchdog contract are defined in OPERATIONAL_RULES.md (sections 1 and 3), not restated here.
