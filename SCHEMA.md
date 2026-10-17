# FILE SCHEMA — DLS26 OMEGA (schema_version 1)
Authoritative artifact map, required fields, migration and rollback. Read this before interpreting or modifying persisted artifacts. Changes require a described migration and a retained old schema (FILE SCHEMA rule).

## 1. Identity and ownership
| Artifact | Path | Owner/authority | Required core fields |
| --- | --- | --- | --- |
| Live prompt | DLS26_OMEGA_PROMPT.md | User (system proposes only) | Version header; full text; SHA-256 recorded in changelog |
| Prompt archive | docs/prompt_archive/OMEGA_PROMPT_v<version>_<date>.md (+ mandated v76 path) | Versioning | Immutable copy; version/date in filename |
| Changelog | docs/prompt_archive/CHANGELOG.md | Versioning | version, date, change, reason, trigger, superseded, regression checks |
| Operational rules | OPERATIONAL_RULES.md | System (Step 4 rebuild) | Digest header, exact strings/limits, named-rule entries, recovery order, file map |
| Capability inventory | CAPABILITY_INVENTORY.md | System | Observation time, presences, absences, network limits, repo verification |
| Handoff | handoff/HANDOFF.md | System, atomic each turn | active state, checkpoint, resumption point, debt, asks |
| Turn manifest | logs/turn_manifest.json | OMEGA-LIVENESS-001 | see §3 |
| Sources log | logs/sources_visited.json | OMEGA-FRONTIER-001 | entries[], source_families[], coverage, digests |
| Main log | logs/main_operational_log.md | MAIN OPERATIONAL LOG | timestamped category entries |
| KB | kb/*.md, kb/index.md | KNOWLEDGE BASE | claim ID, statement, confidence, volatility, origin, sources, verification date |
| Revision register | revision_register.md | REVISION REGISTER | timestamp, change, before, why, trigger, affected advice, topic |
| Issue tracker | issue_tracker.md | Problems/deviations/degradations | ID, date, class, status, description, evidence, resolution |
| Research queue | logs/research_queue.json, logs/research_queue_archive.json | MECHANISM 4 | items with id, topic, tier, status, added, sources |
| User profile | user_profile.md | User facts only | identity/context, preferences, game state, gaps |
| Irreversible actions | knowledge_management/irreversible_actions.md | IRREVERSIBLE ACTION PROTECTION | action, reversibility, cost, evidence |
| Raw data | raw_game_data/ (imported name; also raw_data/ scaffold) | External scripts, read-only | extraction metadata, staleness |
| Audit packages | audit/<package>.md | Mechanism 9 | scope, evidence, claims, challenges, result |
| Continuity | docs/continuity/<branch-or-session>/ | Migration records | source commit, copied artifacts, reconciliation notes |

## 2. Sources log entry schema
\`{ "id": "S-YYYYMMDD-NNN", "url_or_query": str, "tool": "page-render|discovery-search|shell/script", "status": int|"success"|"failed", "source_family": str, "payload_summary": str, "retrieved_at": ISO8601 }\`
Frontier fields (when applicable): canonical_source_id, source_type, language, technical_layer, first_seen_turn, last_served_turn, connection_state, traversal_state, duplicate_of, classification_evidence.

## 3. Turn manifest schema (schema_version 1)
Required: run_id, operation_id, conversation_id, session_id, turn_seq (positive, monotonic across the lineage), checkpoint_id, previous_checkpoint_id, environment_generation, active_state, active_bootstrap_step, next_state, contract_id, contract_digest, progress_event_refs[], consecutive_no_progress, continuation_allowed, needs_user, expected_terminal_class (six-class vocabulary; see OPERATIONAL_RULES.md), exact_resumption_point, created_at, not_before, expires_at, status, diagnostic_refs[]. Never store the containing commit hash in the manifest. \`status: READY_TO_YIELD\` is required for continuation.

## 4. KB claim schema
Claim ID, proposition, build/platform/mode context, confidence tier, volatility tier (named with its system), evidence-origin tags, source URLs/IDs, last verified (date + method), first-publication dates where independence matters, datamining flag, deception-screen outcome, checkable origin or explicit none-found, challenge/replacement history.

## 5. Migration and rollback
- Version is explicit and integer; unknown versions are rejected, not guessed.
- Any schema change: write the reason and migration steps here, keep the old shape readable, migrate losslessly, verify counts/digests, commit a KB snapshot before and after.
- Rollback path: last KB snapshot + git history; restore the snapshot's claims, diff forward to identify affected entries, log scope and trigger (KB SNAPSHOTS rule).
- Derived indexes (coverage, digests) are regenerated from the sources log, never independently edited.
