# Prompt Changelog — DLS26_OMEGA_PROMPT.md

## Entry 1 — ADOPTED-AS-CAPTURED — 2026-10-18T15:32:51Z
- Version in force at the time: 78 (from the prompt header). Reason: initial repository capture. Prompted by: the user's initialization message in the original workspace.
- Capture status: MECHANICAL at the time of capture. SHA-256 `35eb78178fac8f03e970e4a81c720d59d7709470667d50529865aaf408492cac`, 175,594 bytes.
- Original archive path mandated by that prompt: `docs/prompt_archive/OMEGA_PROMPT_v76.md`. Its contents carried version 78. The legacy filename is retained unchanged. A correctly named v78 archive was later made from the pinned PR #6 prompt before the v80 live-file write; see `docs/prompt_archive/OMEGA_PROMPT_v78.md` and `continuity/imports/2026-10-18-session-resume/reconciliation.md`.
- Supersedes: nothing at the time of entry.

## Entry 2 — USER-SUPPLIED VERSION 80 ADOPTED FOR MIGRATION; INTEGRITY FAIL — 2026-10-18T21:03:32Z
- Version in force as user-directed text: 80. The user's supplied v80 revision supersedes v78; only the user may change the live prompt. The outgoing v78 bytes remain preserved at `docs/prompt_archive/OMEGA_PROMPT_v78.md`.
- Current live prompt: `DLS26_OMEGA_PROMPT.md`, 184,126 bytes, SHA-256 `495bd2dc946c4ec999914e839952ef17aeef9777ba0cf0f7d87e465451ba014a`.
- Archive: `docs/prompt_archive/OMEGA_PROMPT_v80.md`; `cmp` verifies it is byte-identical to the live file at the same size/hash. This proves mirror identity only. The full original user message is not available as a byte-addressable source in this resumed context, so full source-text fidelity is NOT verified. Capture is recorded as `RECONSTRUCTED_UNVERIFIED`; do not describe the current bytes as proven verbatim user text.
- Diff: `docs/prompt_archive/diffs/OMEGA_PROMPT_v78_to_v80.diff` (191 lines, 35,786 bytes; zero-context unified diff from v78 archive to current v80 draft, to keep the patch artifact free of whitespace-marker warnings). It is a repository-version diff, not a raw-user-message comparison.
- Reason and trigger: the user supplied a full v80 prompt and directed that it be authoritative. During recovery, comparison against the available v78 prompt and the remembered/supplied fragments found and repaired three transcription defects: (1) duplicated/mangled text in the Condition 1 sentence; (2) incorrect word order in the Scope paragraph; (3) omitted `REPRESENTATION_DUPLICATE` paragraph. These are capture corrections, not agent-authored policy amendments. The full prompt still cannot be proven identical to the original source without that source or its hash.
- Main v80 additions/changes relative to the repository's v78: five-pass import audit and corpus custody rules; `OMEGA-INTEGRITY-001`; explicit confidence-promotion gates and mechanisms 5–9; expanded evidence/claim requirements; frontier fairness, closure, health, retrieval, progress and recovery contracts; a single liveness/dispatch/migration control plane; stricter exact-line bootstrap output. The regenerated diff is the detailed change record.
- Explicitly superseded v78 machinery: the old `HARD_STOP_STEP3` / `HARD_STOP_COMPLETE` vocabulary, legacy four-part/HEAD-bound consumption descriptions, and duplicate watchdog instructions defer to `OMEGA-LIVENESS-001` and `OMEGA-DISPATCH-001`. No other removed or materially weakened instruction is claimed exhaustive while raw-source fidelity is unresolved.
- Regression result: see `docs/prompt_integrity/v80.json`. The v80 integrity audit is FAIL / NOT PRODUCTION-READY because source fidelity is unverified, named cross-references remain unresolved, the confidence taxonomy contains a `Community Consensus` tier reference absent from the five listed gates, and Step 2/3 exit predicates are incomplete. The current imported claim records also fail the five-pass evidence audit and remain quarantined. No game claims were newly researched or verified in this turn.
- Controller validation: actual external/browser controller behavior and consumption acknowledgement were not observable or tested. No automatic continuation is authorized by this checkpoint.
- In-flight work: Step 1 / epoch 0001 remains OPEN; the saved research cursor remains Q-008 through Q-013, then classify all CONNECTED/UNCERTAIN references. This migration turn performed no game research. See the current handoff and manifest.
- Supersedes: v78 as the user-directed prompt revision, subject to source-fidelity and integrity review. This entry does not declare v80 production-ready.

## Historical proposals from the v78 changelog (preserved)

### PROPOSED-A — Complete the missing sections of the prompt — 2026-10-18T15:32:51Z
- Historical evidence: v78 contained unresolved named sections and mechanisms. Version 80 defines several of them, but not all; the proposal is therefore partially addressed, not silently closed. The unresolved items are tracked in `ISSUE-001` and `ISSUE-012`.
- Until the user adopts a complete repair, follow the specific extant rules and conservative defaults; do not invent missing sections.

### PROPOSED-B — Resolve the two manifest vocabularies — 2026-10-18T15:32:51Z
- Status: resolved with notice by v80. The older list remains in the prompt, but v80 explicitly says its legacy terminal classes, obsolete manifest specifications and duplicate watchdog instructions are superseded by `OMEGA-LIVENESS-001` / `OMEGA-DISPATCH-001`. See `ISSUE-003`.

### PROPOSED-C — Name the confidence tiers in the text — 2026-10-18T15:32:51Z
- Status: partially resolved by v80's `MECHANISM 5 — CONFIDENCE PROMOTION GATES`. No legacy claim was promoted during migration. `Community Consensus tier` remains an inconsistent reference; see `ISSUE-013`.

## PROPOSED entries (no version number; not in force until the user adopts them)

### PROPOSED-D — Repair remaining v80 integrity defects and verify source fidelity — 2026-10-18T21:03:32Z
- Current rule gets wrong: the v80 draft has a metadata reference from `OMEGA-SQUAD-001` to `MY SQUAD — MY GROUND TRUTH` with no matching canonical section; other named rule pointers remain unresolved; `Community Consensus tier` is referenced outside the five categories in Mechanism 5; and the bootstrap state list does not provide explicit entry/completion/successor predicates for every state (notably Steps 2 and 3). Full comparison to the original user message is unavailable, so additional transcription defects cannot be excluded.
- Evidence: `docs/prompt_integrity/v80.json`, `docs/audits/2026-10-18-v80-import-audit.md`, the generated v78→v80 diff, and `ISSUE-012`, `ISSUE-013`, `ISSUE-017`.
- Proposed change: user supplies or confirms an exact v80 source/hash and adopts a complete text-only repair resolving the named pointers, confidence-tier conflict and missing state predicates. Agent does not edit the prompt to make these repairs.
- Dependencies: operational rules digest, prompt assertion ledger, schema, controller validation and any future continuation authorization.
- Until adopted: preserve the user's supplied text as the active draft, flag it as not production-ready, do not claim exact source identity, and do not authorize automatic continuation.
