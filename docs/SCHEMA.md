# File Schema (schema_version 1) — created 2026-10-18T15:32:51Z

Read this file before interpreting or modifying any persisted artifact. Old schemas are kept; migrations preserve every record and every unresolved discovery.

## Artifacts and owners
| Path | Owner | Format | Notes |
| --- | --- | --- | --- |
| DLS26_OMEGA_PROMPT.md | user | Markdown (verbatim prompt) | Live authority. Only the user edits it. |
| docs/prompt_archive/OMEGA_PROMPT_v76.md | archive | byte-identical copy | Outgoing versions go to versioned archive paths. |
| docs/PROMPT_CHANGELOG.md | agent (proposals only) | Markdown | PROPOSED entries carry no version number. |
| OPERATIONAL_RULES.md | agent (derived) | Markdown | Digest now; compaction-minimal form in Step 4. |
| docs/CAPABILITY_INVENTORY.md | agent | Markdown | Re-verified each session. |
| docs/REPO_ACCESS_VERIFICATION.md | agent | Markdown | |
| docs/contracts/*.json | agent | JSON (sealed contracts) | Each contract has an id and sha256 digest. |
| logs/turn_manifest.json | agent | JSON (schema_version 1) | One per checkpoint; fields per OMEGA-LIVENESS-001. |
| handoff/handoff.md | agent | Markdown | Written atomically (tmp file, then rename). |
| handoff/attention_required.md | agent | Markdown | Only when ATTENTION_REQUIRED applies. |
| logs/sources_visited.json | agent | JSON (schema_version 1) | Physical source of truth for exhaustion (OMEGA-FRONTIER-001). |
| logs/main_operational_log.md | agent | Markdown, timestamped entries by category | Categories as in prompt; new categories noted in handoff. |
| logs/issue_tracker.md | agent | Markdown entries ISSUE-NNN | |
| logs/revision_register.md | agent | Markdown entries REV-NNN | Knowledge changes only. |
| logs/research_queue_active.md / logs/research_queue_archive.md | agent | Markdown tables | Both committed on every update. |
| kb/knowledge_base.md | agent | Markdown index | Authoritative current state by topic. |
| kb/claims/CLM-NNNN.json | agent | JSON (claim contract, OMEGA-EVIDENCE-002) | One claim ID per proposition. |
| kb/user_profile.md | agent (facts from user) | Markdown | Preferences, state, decisions. |
| kb/irreversible_actions.md | agent | Markdown list | The Irreversible Action List artifact. |
| kb/snapshots/YYYY-MM-DDTHHMMSSZ/ | agent | copy of kb/ | Kept indefinitely. |
| raw_game_data/ | external scripts | game format | READ-ONLY for the agent. |

## Claim record minimum (KB and kb/claims)
claim_id; proposition; applicable build/platform/mode/context; confidence tier (named: the five Confidence Promotion Gates tiers — names not defined in the pasted prompt, see issue tracker); volatility tier (named with its system); patch-triggered and event-triggered dimensions; evidence_refs; origin tags (not tiers); last_valid_verification (time, method); expiry/trigger rules; unresolved challenges; replacement history; datamining flag; deception-screen outcome; checkable origin or explicit "none found".

## Source log record (logs/sources_visited.json)
retrievals[] (id, url, domain, tool, http_status, timestamp, payload digest, projection, cursor), discovered_references[] (canonical_source_id, source_family, source_type, language, technical_layer, first_seen_turn, last_served_turn, connection_state, traversal_state, duplicate_of, evidence), service_events[] (unique id, record ref, family, cursor advance), coverage[] (required dimension id, status), digest (sha256 of the body).

## Manifest (logs/turn_manifest.json, schema_version 1)
Required fields exactly as OMEGA-LIVENESS-001 defines. The commit hash is never stored inside the manifest. The six expected_terminal_class values are BOOTSTRAP_START, CONTINUE, ATTENTION_REQUIRED, PUBLICATION_PENDING, PROTOCOL_ERROR, COMPLETE.

## Storage management (practical limits to be measured in Step 1)
- Repo size: currently tiny. Individual JSON logs rotate by sequential numbering (sources_visited.json.1 …) once they exceed a size set in Step 1 measurements; rotated files stay readable.
- Git LFS is absent; if a large raw dataset is needed, prefer a separate archive location and record its digest in the schema rather than committing bulk binaries.
