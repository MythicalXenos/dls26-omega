# FILE SCHEMA — DLS26 OMEGA ARTIFACTS
Version: 1 (designed Turn 1, first session, per FILE SCHEMA). Subsequent sessions read this file before interpreting or modifying persisted artifacts. Changes only if the user asks, or the agent proposes a better structure with explanation, migration plan and rollback; the old schema is kept.

## DLS26_OMEGA_PROMPT.md / docs/prompt_archive/OMEGA_PROMPT_v76.md
Plain-text verbatim prompt captures. Live file keeps one permanent filename for the life of the repo; archived versions carry version and date in their filenames. Capture status (MECHANICAL or DIGEST-ONLY), byte size and SHA-256 are recorded in OPERATIONAL_RULES.md §HEADER and handoff/handoff.md.

## OPERATIONAL_RULES.md
The rules digest (Turn 1 form) / rebuilt operational rules file (Step 4 form). Sections: HEADER (first line verbatim, version, capture status with size+SHA-256, time, authority sentence); §A verbatim strings/paths/schema names/numeric limits/ordering conditions; §B named-rule index (open list); §C recovery order and user-ask policy; §D file map.

## CAPABILITY_INVENTORY.md
Open inventory of environment capabilities: host agent tools; connected apps; network access and its limits; shell environment (runtimes, tools, absences); repository and version control; host constraints; absences/limits summary. Re-verified against Datamining's hard constraints.

## logs/turn_manifest.json
JSON object, one file, rewritten each turn (write-or-replace). Fields: schema_version (integer; unknown versions rejected), run_id, operation_id, conversation_id (strings; stable, controller-bound, never inferred from display text — recorded honestly when the host exposes none), session_id, turn_seq (positive integer, monotonic within session; a new session does not reset it), checkpoint_id (unique within session), previous_checkpoint_id (string|null; genesis binds null during setup), environment_generation, active_state, active_bootstrap_step (integer 0–5), next_state, contract_id, contract_digest, progress_event_refs (array of repo-relative artifact paths), consecutive_no_progress (derived integer), continuation_allowed (bool), needs_user (bool), expected_terminal_class (enum; six-class terminal vocabulary is the authority — see Issue Tracker OBS-003), exact_resumption_point (string), created_at, not_before (ISO-8601 UTC), expires_at (ISO-8601 UTC|null), status ("READY_TO_YIELD" for a valid continuation checkpoint), diagnostic_refs (array of repo-relative paths with integrity binding). The containing commit's hash is NEVER stored inside the manifest.

## logs/sources_visited.json
JSON, append-only. Top level: schema_version, authority note, created_utc, entries[], source_families{}, coverage{}, digests{}. Entry fields: retrieval_id, timestamp_utc, domain, exact_url, retrieval_tool (page-render | discovery-search | shell/script), http_status (integer|null), payload_summary (structured), source_family, source_type, language, technical_layer, connection_state (CONNECTED|NON_CONNECTED|UNCERTAIN), traversal_state (UNVISITED|IN_PROGRESS|RETRYABLE_FAILURE|VISITED|ACCESS_BOUNDARY|REPRESENTATION_DUPLICATE), canonical_source_id, duplicate_of, classification_evidence, extraction_cursor, service_event_id. Derived views carry this file's digest and are regenerated from it.

## logs/main_operational_log.md
Markdown, timestamped entries: `[UTC ISO timestamp] CATEGORY — content`. Categories per OPERATIONAL_RULES.md §A.3 (RESEARCH, RECOMMENDATION, OUTCOME, QUESTION, REVISION, CONFLICT, DISAGREEMENT, EXHAUSTION DECLARATION, SKEPTIC CHALLENGE, DEVILS ADVOCATE, BLUFF CHECK, SELF-AUDIT, INDEPENDENT VERIFICATION, DEGRADATION EVENT, DECEPTION FINDING, EVIDENCE CONFLICT, CONFIDENCE PROMOTION, SOURCE TYPE COVERAGE, NEGATIVE FINDING, MATCH LOG, SETUP, SESSION, ANOMALY, others as useful — new categories announced in the handoff). Every RECOMMENDATION entry carries a Topic field written identically each time. Filterable by category and date; rotated (sequential numbering, all files accessible) when approaching performance-affecting sizes.

## logs/research_queue.json / logs/research_queue_archive.json
JSON. Item fields: ticket_id, discovered_turn, reference (URL/endpoint/account/file/route/citation), source_family, source_type, language, technical_layer, connection_state, traversal_state, priority_tier (queue-Critical/High/Medium/Low), discovered_utc, reason, status, cursor, attempt_history[], next_eligible_utc (RETRYABLE_FAILURE), archived_reason (archive file only). Both files committed after every update to either.

## handoff/handoff.md
Markdown, rewritten atomically before every turn end. Sections: Session (IDs, branch, base commit, prompt version/capture status/hashes); State (active state, step, checkpoint ID, manifest summary, consecutive_no_progress); Exact resumption point; User information received; Awaited outcomes; Consolidated ask to the user; Anomalies/new categories; Progress signal (bootstrap sessions); Storage.

## handoff/attention_required.md
Markdown, append-only standing requests: timestamp, state/operation, specific request/warning/authorization needed, evidence in hand, why user input is indispensable, blocked action (+deadline/expiry), resolution. Device-access requests live here.

## kb/index.md + kb/<topic>.md
Markdown. Claim entry fields: claim_id; precise proposition; applicable build/platform/mode/context; confidence_tier (five-tier system); volatility_tier (named with its system per TIER RULE); evidence_records[] (origin/method tags, author/origin identity, publication/observation time, tool/user-report provenance, exact immutable payload or observation artifact reference, extraction span, build/context, authenticity limits, incentive assessment, material shared failure modes); datamining_confirmation_flag; deception_screen_outcome; checkable_origin (direct evidence) or explicit none-found record; last_valid_verification; expiry/trigger_rules; unresolved_challenges[]; replacement_history[]. Evidence-origin/method tags (official-stated, static-analysis, dynamically-observed, community-controlled-test, community-anecdote, user-stated, creator-demonstration, database-derived, inferred, …) are carried alongside, never as a second confidence taxonomy.

## kb_snapshots/
Full KB snapshots named kb_snapshot_<UTC-date>_<seq>.md, committed at every session end and every significant push; kept indefinitely; the rollback path per KB SNAPSHOTS.

## user_profile.md
Markdown: identity/context, stated preferences (each with the pros/cons record of alternatives shown), decisions log, club & game state (persistent fields only — individual match results and mid-session resource deltas go to the main log's MATCH LOG category), awaited outcomes, contradictions/flags, knowledge gaps.

## issue_tracker.md / revision_register.md
Markdown registers per their prompt rules (issue classes and statuses; revision-change index fields).

## knowledge_management/irreversible_actions.md
Markdown standing list of verified irreversible/consequential DLS26 action types (empty until Step 1 verifies entries).

## raw_game_data/
Read-only external drops (ADB extractions, save pulls, API captures), organized per extraction batch; the agent never modifies these files.

## docs/prompt_changelog.md
Markdown: version, date, every change, reason, conversation round/finding, what it superseded; PROPOSED entries carry no version number and no supersedes field; reversals recorded with reasoning.
