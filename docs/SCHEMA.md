# File Schema (schema_version 1) — created 2026-10-18T15:32:51Z; v80 migration update 2026-10-18T21:03:32Z

Read this file before interpreting or modifying any persisted artifact. Old schemas are retained; migrations preserve every record, source payload reference, conflict, and unresolved discovery. Imported claim files are read-only until a lossless migration is explicitly recorded.

## Artifacts and owners
| Path | Owner | Format | Notes |
| --- | --- | --- | --- |
| `DLS26_OMEGA_PROMPT.md` | user | Markdown | Live authority. Only the user edits it. Current v80 source fidelity is unverified; see the integrity ledger. |
| `docs/prompt_archive/OMEGA_PROMPT_v78.md` | archive | Markdown | Preserved outgoing v78 prompt; 175,594 bytes, SHA-256 `35eb78178fac8f03e970e4a81c720d59d7709470667d50529865aaf408492cac`. |
| `docs/prompt_archive/OMEGA_PROMPT_v80.md` | archive | Markdown | Current draft mirror; must `cmp` against live prompt. Mirror equality does not prove identity to the original user message. |
| `docs/prompt_archive/OMEGA_PROMPT_v76.md` | legacy archive | Markdown | Retained unchanged; its contents were version 78 under the earlier filename mismatch. |
| `docs/prompt_archive/diffs/OMEGA_PROMPT_v78_to_v80.diff` | agent | unified diff | Repository v78→v80 draft diff; not a raw-user-source diff. |
| `docs/PROMPT_CHANGELOG.md` | agent (proposals only) | Markdown | Adopted history plus versionless `PROPOSED` entries. User alone adopts prompt changes. |
| `docs/prompt_integrity/v80.json` | agent | JSON (schema_version 1) | Machine-readable PASS/FAIL ledger for the v80 amendment-integrity assertions. Each attempt preserves tests and evidence; later attempts append rather than erase an earlier failure. |
| `docs/audits/2026-10-18-v80-import-audit.md` | agent | Markdown audit report | Five-pass audit/disposition for imported `CLM-0001`–`CLM-0012`; failed/missing passes mean quarantine, not knowledge. |
| `OPERATIONAL_RULES.md` | agent (derived) | Markdown | Rules digest remains active during Steps 1–3; Step 4 replaces it with the compaction-minimal form. Prompt outranks this digest. |
| `docs/capabilities.md` | agent | symlink | Canonical v80 path; points to `CAPABILITY_INVENTORY.md` so there is one capability inventory source of truth. |
| `docs/CAPABILITY_INVENTORY.md` | agent | Markdown | Inventory target for the alias above; re-verified each session. |
| `docs/REPO_ACCESS_VERIFICATION.md` | agent | Markdown | Current bound branch, configured remote/refspecs, PR state and publication verification. |
| `docs/contracts/*.json` | agent | JSON (sealed contracts) | Each sealed contract has an ID and SHA-256 digest; do not edit it in place. Successor obligations are recorded separately. |
| `logs/turn_manifest.json` | agent | JSON (schema_version 1) | One per checkpoint; fields and six terminal classes per `OMEGA-LIVENESS-001`. Commit hash is not stored in the manifest it commits. |
| `handoff/handoff.md` | agent | Markdown | Written atomically; exact state, next obligation, outstanding warnings and user-dependent gates. |
| `handoff/attention_required.md` | agent | Markdown | Written only when ATTENTION_REQUIRED applies; records indispensable user action/input and evidence. |
| `logs/sources_visited.json` | agent | JSON (schema_version 1) | Physical source-of-truth registry per `OMEGA-FRONTIER-001`; incomplete legacy records are not upgraded to verified payloads by summary alone. |
| `logs/main_operational_log.md` | agent | Markdown | Timestamped ground truth by category; categories and new categories noted in handoff. |
| `logs/issue_tracker.md` | agent | Markdown | `ISSUE-NNN` records with status, severity, evidence, action and owner. |
| `logs/revision_register.md` | agent | Markdown | `REV-NNN` entries for knowledge/advice changes; not prompt-version history. |
| `logs/research_queue_active.md` / `logs/research_queue_archive.md` | agent | Markdown tables | Both committed on every queue update; staging does not close an obligation. |
| `kb/knowledge_base.md` | agent | Markdown index | Current admitted knowledge by topic; quarantined legacy candidates are listed separately and are not usable as verified facts. |
| `kb/claims/CLM-NNNN.json` | agent / imported read-only inputs | JSON claim records | One stable ID per proposition. PR #6 files remain unchanged pending a lossless schema migration and evidence restoration. |
| `kb/user_profile.md` | agent (facts from user) | Markdown | User-stated preferences, state and decisions; system context is separately labelled. |
| `kb/irreversible_actions.md` | agent | Markdown list | Candidate-only until each action type is supported by admitted evidence. |
| `kb/snapshots/YYYY-MM-DDTHHMMSSZ/` | agent | copied KB tree plus manifest | Full snapshot, including claims, profile and action list; retained indefinitely. |
| `raw_game_data/` | external scripts | game format | Read-only to the agent. |

## Prompt integrity ledger schema (`docs/prompt_integrity/v80.json`)
Required top-level fields: `schema_version` (integer 1), `ledger_id`, `prompt_version`, `overall_status`, `production_ready` (strict boolean), `prompt_capture` (classification, live/archive paths, byte lengths, SHA-256 values, mirror-equality result, and nullable source-text digest), `outgoing_prompt`, and `audit_attempts[]`. Each attempt carries an ID, UTC evaluation time, `assertions[]`, test/evidence references, unresolved limitations and deployment verdict. Every assertion has a stable `id`, `result` exactly `PASS` or `FAIL`, and evidence sufficient to reproduce or understand that result. Keep earlier attempts when adding later verification.

## Import-audit schema (`docs/audits/2026-10-18-v80-import-audit.md`)
Record the pinned corpus repository/ref/commit, claim-ID scope, five pass definitions, per-claim pass results, immutable witness paths/hashes or their explicit absence, conflicts/duplicates, and final admission disposition. A claim that fails or lacks any required pass stays quarantined. Recovery: restore or freshly retrieve admissible primary payloads under the active retrieval rules, rerun all five passes, append a new audit attempt, then make an explicit revision to the KB index. Never promote a claim by changing its text or confidence field in place.

## Claim record minimum (admitted KB claims)
`claim_id`; proposition; applicable build/platform/mode/context; exactly one confidence tier from the prompt's five-tier Confidence Promotion Gates; separately named volatility tier; patch-triggered and event-triggered dimensions; evidence references; origin/method tags (not tiers); last-valid-verification (time, method); expiry/trigger rules; unresolved challenges; replacement history; datamining flag; deception-screen outcome; and a checkable origin or explicit `none found`. v80 lists the gate labels as Confirmed, High Confidence, Corroborated / Plausible, Speculative and Disputed; its separate `Community Consensus tier` phrase is inconsistent and remains an issue. Quarantined legacy candidate records are not admitted claim records and are not used as game facts.

## Source log record (`logs/sources_visited.json`)
The active schema tracks retrieval ID/tool/URL/query, exact timestamp, HTTP status when available, payload digest, extraction projection/cursor, and status; discovered-reference IDs, family, language, first/last turn, connection/traversal state, duplicate pointer and evidence; unique service events with record/reference/family/cursor; required-dimension coverage; and a digest over the body. Existing PR #6 rows contain summaries without immutable payload hashes for many sources; preserve them as legacy observations and do not infer a payload digest.

## Manifest (`logs/turn_manifest.json`, schema_version 1)
Required fields exactly as `OMEGA-LIVENESS-001` defines: `schema_version`; `run_id`, `operation_id`, `conversation_id`; `session_id`, monotonic `turn_seq`; `checkpoint_id`, `previous_checkpoint_id`; `environment_generation`; `active_state`, `active_bootstrap_step`, `next_state`; `contract_id`, `contract_digest`, `progress_event_refs`; derived `consecutive_no_progress`; strict booleans `continuation_allowed`, `needs_user`; one of the six `expected_terminal_class` values; `exact_resumption_point`; `created_at`, `not_before`, nullable `expires_at` only when allowed; checkpoint `status`; and `diagnostic_refs`. In this checkpoint, `progress_event_refs` and `diagnostic_refs` use objects with an `id`, repository-relative `path`, and SHA-256 of the referenced file; imported earlier checkpoints may retain legacy string IDs. A detached publication envelope binds manifest and proof artifacts to the immutable repository/ref commit/tree. Automatic continuation requires published READY_TO_YIELD state, permission true, no user need, permitted terminal/state, valid predecessor/sequence, and a not-yet-consumed `(run_id, operation_id, checkpoint_id)`.

## Storage management
Practical storage limits are still unmeasured (Q-006 remains open). Repo size and per-file rotation limits must be measured in Step 1. Git LFS is absent; keep large raw datasets out of Git unless required, and record any separately stored payload digest and access path.
