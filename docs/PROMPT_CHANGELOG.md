# Prompt Changelog — DLS26_OMEGA_PROMPT.md

## Entry 1 — ADOPTED-AS-CAPTURED — 2026-10-18T15:32:51Z
- Version in force: 78 (from the prompt's header line). Reason: first capture of the live prompt in this repository. Prompted by: user's first message (initialization in a new workspace).
- Capture status: MECHANICAL. SHA-256 35eb78178fac8f03e970e4a81c720d59d7709470667d50529865aaf408492cac, 175594 bytes.
- Archive: docs/prompt_archive/OMEGA_PROMPT_v76.md (byte-identical). The bootstrap text names this archive filename; its version label conflicts with the header (78). Filename kept as instructed; version identity is the content header. See ISSUE-002.
- Supersedes: nothing (first capture).

## PROPOSED entries (no version number; not in force until the user adopts them)

### PROPOSED-A — Complete the missing sections of the prompt — 2026-10-18T15:32:51Z
- Current rule gets wrong: many rules reference sections or mechanisms that the pasted text never defines (Session Start, Session Handoff, First Session Bootstrap, Knowledge Management, Analysis & Reasoning Standards, Patch Response, Notification Threshold, Communication Style, Confidence Promotion Gates, Scope Division, Mechanisms 5–9, Special Card Tracking, Planted And Decoy Data, Deterministic Versus Variable, Gaps, Named Set, Irreversible Action List, NO OUTPUT DURING BOOTSTRAP Yes list, PROMPT VERSIONING, PROMPT CAPTURE, MY SQUAD — MY GROUND TRUTH, Mid-Session Monitoring, Independent Verification, Recommendation Consistency, Intelligence Pipeline, Datamining hard constraints, Origin-tracing in the Promotion Gates). Evidence: grep of DLS26_OMEGA_PROMPT.md during Setup (ISSUE-001).
- Proposed change: the user supplies the full text of those sections, or confirms that they are intentionally absent.
- Until adopted: the conservative default in the referring rule applies; blockers are logged to the issue tracker and the single consolidated ask is made at the end of the bootstrap process.

### PROPOSED-B — Resolve the two manifest vocabularies — 2026-10-18T15:32:51Z
- Current text has two versions of the manifest rule: the older four-step list with expected_terminal_class values HARD_STOP_STEP3 / HARD_STOP_COMPLETE, and OMEGA-LIVENESS-001 with six classes. The prompt names OMEGA-LIVENESS-001 as the sole checkpoint contract.
- Proposed: delete the older list and the HARD_STOP_* values, or mark them superseded by OMEGA-LIVENESS-001.
- Until adopted: the six-class table in OMEGA-LIVENESS-001 is followed (ISSUE-003).

### PROPOSED-C — Name the confidence tiers in the text — 2026-10-18T15:32:51Z
- The text uses Confirmed, High Confidence, Community Consensus, Speculative and Disputed, and says there are five tiers. The five-tier definition and its promotion quotas are not in the pasted text (ISSUE-009).
- Proposed: the user supplies the Confidence Promotion Gates section or confirms the five tier names and order.
