# PROMPT_CHANGELOG.md

The changelog is the single authority for prompt-level changes, deprecations and supersessions. Entries: version (adopted entries only), date, changes, reason, triggering finding, supersedes, and status (adopted or PROPOSED). Proposals are written here and never applied by the agent.

## v76 — adopted as the live prompt (Turn 1, session a8a92133, 2026-10-09)
- Source: the Turn 1 user message, header "DLS26 OMEGA PROMPT — VERSION 76 (CANONICAL LIVE MASTER AUTHORITY)".
- Change: first adoption in this repository. The repository held only the initial commit, so there is no earlier version to archive.
- Capture status: agent transcription to DLS26_OMEGA_PROMPT.md, incomplete (OPERATIONAL_RULES.md section 6; logs/issue_tracker.md ISSUE-002 and ISSUE-007).
- Supersedes: none (first adoption).
- Reason: user-directed bootstrap of the DLS26 Omega engine.

## PROPOSED items (not adopted; no version number; no supersedes field; the user decides)
- P-001 — replace the expected_terminal_class enum in the turn-manifest rule (HARD_STOP_STEP3, HARD_STOP_COMPLETE) with the current MACHINE-READ LINES classes (BOOTSTRAP_START, CONTINUE, ATTENTION_REQUIRED, PUBLICATION_PENDING, PROTOCOL_ERROR, COMPLETE). Evidence: the two sections name different vocabularies in the same version (ISSUE-004). Current behaviour: the manifest uses the current classes.
- P-002 — remove the duplicate, malformed OMEGA-SQUAD-001 header in the capture (ISSUE-003). Likely a paste artifact.
- P-003 — make the CAPABILITY INVENTORY ordering agree with STATE_0 (ISSUE-005). Current behaviour: STATE_0 order.
- P-004 — restore the absent bodies listed in OPERATIONAL_RULES.md section 6, and the empty bodies of OMEGA-BATCH-001, OMEGA-FRONTIER-001 and OMEGA-LAB-001. This is a capture completion request, not a rule change. Status: pending; if still absent at Step 5, it goes into the consolidated ask.
