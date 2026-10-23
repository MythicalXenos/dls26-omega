# Attention Required — v80 prompt fidelity and integrity

Written: 2026-10-23T15:41:55Z (UTC). Session `dls26-s001-20261018T153458Z`, logical turn 5. Current checkpoint is recorded in `logs/turn_manifest.json`.

## Short answer — “What's wrong?”

The pause is for process and evidence integrity, not a newly discovered game problem:

1. **The v80 text is not proven to match your original prompt.** The live file and archive match each other at SHA-256 `495bd2dc946c4ec999914e839952ef17aeef9777ba0cf0f7d87e465451ba014a`, but the original prompt bytes/hash are unavailable in this resumed context. That is mirror verification, not source verification.
2. **The v80 draft fails its own integrity checks.** It points to an undefined `MY SQUAD — MY GROUND TRUTH` rule, uses `Community Consensus` as a confidence tier outside the five listed gates, and lacks state-specific exit predicates for Steps 2 and 3.
3. **The 12 imported game claims are not trustworthy enough to use as facts yet.** Their cited sources are summaries/snippets without complete immutable primary payloads, hashes, and extraction spans. They remain quarantined; none was newly verified.
4. **The external continuation controller is unverified.** Its exact-once acknowledgement/runtime tests were not available, so unattended continuation is disabled.
5. **The previous turn also exceeded its 360-second budget.** This is recorded as ISSUE-018; it is a process violation, not a game finding.

The supporting checks and exact evidence are in `docs/prompt_integrity/v80.json` and `docs/audits/2026-10-18-v80-import-audit.md`. The user authorized manual Step-1 work; the Q-008 store-page slice is recorded at `kb/research_observations/2026-10-23-Q-008-official-store-slice.md`.

## User direction — manual Step-1 research authorized

At 2026-10-23T15:36:29Z, the user instructed: “Approved. Proceed with Step 1 background research.” Interpreted narrowly as authorization to resume Step 1 manually from the validated Q-008 cursor under the existing draft. This does **not** verify the original v80 bytes, repair the prompt, promote any legacy claim, or validate/enable the external controller. The integrity ledger remains FAIL / NOT PRODUCTION-READY, and unattended continuation remains disabled.

## Why production readiness and automation remain paused

The v80 draft and its archive match byte-for-byte, but that proves only that the two repository files are mirrors. The original user-supplied v80 text/hash is not available as a byte-addressable source in this resumed context. Three known transcription defects were repaired, but further differences cannot be excluded. The prompt's own integrity ledger therefore records `FAIL_NOT_PRODUCTION_READY`; the agent may not edit the prompt to repair policy text.

The semantic audit also finds unresolved named-rule pointers, a `Community Consensus` confidence-tier reference outside the five Mechanism 5 gates, and missing state-specific entry/exit/successor predicates for Steps 2 and 3. Full evidence is in `docs/prompt_integrity/v80.json`; proposed user-only repair is in `docs/PROMPT_CHANGELOG.md`.

## User action needed (batched)

1. Provide the complete authoritative v80 prompt as an attachment or paste it again, preferably with a SHA-256, so the live draft and archive can be compared against the actual source; alternatively, explicitly confirm the current live file's hash in the changelog as the text you intend to govern despite the unresolved audit findings.
2. If v80 is to be production-ready, supply/adopt a repaired prompt that resolves the remaining named pointers, confidence-tier mismatch and state exit predicates. The agent will not edit the user-owned prompt.
3. The external controller's consumption acknowledgement and runtime are unverified. Manual Step-1 research has now been explicitly authorized and performed for this turn. Do not enable unattended continuation until the controller owner exposes the required validation; no controller send was attempted.

## Preserved state

- Step 1 / epoch-0001 remains OPEN; no state transition or epoch exit is claimed.
- Q-008 received a bounded retrieval slice; the next cursor is Q-009 through Q-013, then classification of all CONNECTED/UNCERTAIN references. Q-002 and Q-003–Q-007 remain open or blocked as recorded; CONF-002 remains unresolved. No queue item was silently discarded.
- Legacy claims CLM-0001–CLM-0012 remain unchanged and quarantined after the five-pass import audit. The Q-008 store-page observation is not a newly admitted/verified claim; all CLM-0001–CLM-0012 remain quarantined and unchanged.
- PR #6 remains the sole open PR and was not changed or merged. This session works only on `arena/1e90cb90-dls26-omega`.

## Additional material warning

The resumed turn exceeded the later-turn 360-second wall-clock ceiling: the first observed same-turn clock was 20:56:38Z and checkpoint preparation continued through 21:12:50Z, a span of 16m12s; the turn itself began earlier, so the ceiling was exceeded by at least 10m12s. The exact turn-start time was not instrumented. This is logged as a DEGRADATION EVENT / ISSUE-018. No further game research was performed after detecting the overrun. Future turns must instrument the actual end-to-end deadline and reserve checkpoint time; this record does not certify budget compliance.

## Release condition

The user has authorized manual Step-1 research under the existing draft; that authorization does not clear the source-fidelity/integrity FAIL. Manual research may resume only on a direct user turn; do not use `>` because unattended continuation remains disabled pending validated controller evidence. Production-ready status still requires the user-owned source/fidelity action and an auditable integrity attempt. Continue from Q-009; do not restart or skip a bootstrap state.
