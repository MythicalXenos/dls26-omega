# Attention Required — v80 prompt fidelity and integrity

Written: 2026-10-18T21:12:50Z (UTC). Session `dls26-s001-20261018T153458Z`, logical turn 3. Current checkpoint is recorded in `logs/turn_manifest.json`.

## Why the run is paused

The v80 draft and its archive match byte-for-byte, but that proves only that the two repository files are mirrors. The original user-supplied v80 text/hash is not available as a byte-addressable source in this resumed context. Three known transcription defects were repaired, but further differences cannot be excluded. The prompt's own integrity ledger therefore records `FAIL_NOT_PRODUCTION_READY`; the agent may not edit the prompt to repair policy text.

The semantic audit also finds unresolved named-rule pointers, a `Community Consensus` confidence-tier reference outside the five Mechanism 5 gates, and missing state-specific entry/exit/successor predicates for Steps 2 and 3. Full evidence is in `docs/prompt_integrity/v80.json`; proposed user-only repair is in `docs/PROMPT_CHANGELOG.md`.

## User action needed (batched)

1. Provide the complete authoritative v80 prompt as an attachment or paste it again, preferably with a SHA-256, so the live draft and archive can be compared against the actual source; alternatively, explicitly confirm the current live file's hash in the changelog as the text you intend to govern despite the unresolved audit findings.
2. If v80 is to be production-ready, supply/adopt a repaired prompt that resolves the remaining named pointers, confidence-tier mismatch and state exit predicates. The agent will not edit the user-owned prompt.
3. The external controller's consumption acknowledgement and runtime are unverified. Do not enable unattended continuation until the controller owner exposes the required validation; if continuing manually is preferred, state that explicitly. No controller send was attempted in this turn.

## Preserved state

- Step 1 / epoch-0001 remains OPEN; no state transition or epoch exit is claimed.
- Saved research cursor remains Q-008 through Q-013, then classification of all CONNECTED/UNCERTAIN references. Queue items Q-002 through Q-007 remain open or blocked as recorded; none was silently discarded.
- Legacy claims CLM-0001–CLM-0012 remain unchanged and quarantined after the five-pass import audit. No game research was performed and no game claim was newly verified.
- PR #6 remains the sole open PR and was not changed or merged. This session works only on `arena/1e90cb90-dls26-omega`.

## Additional material warning

The resumed turn exceeded the later-turn 360-second wall-clock ceiling: the first observed same-turn clock was 20:56:38Z and checkpoint preparation continued through 21:12:50Z, a span of 16m12s; the turn itself began earlier, so the ceiling was exceeded by at least 10m12s. The exact turn-start time was not instrumented. This is logged as a DEGRADATION EVENT / ISSUE-018. No further game research was performed after detecting the overrun. Future turns must instrument the actual end-to-end deadline and reserve checkpoint time; this record does not certify budget compliance.

## Release condition

Resume only after the user's prompt-source/fidelity action is recorded and the prompt integrity ledger has a new auditable attempt. Any unattended continuation additionally requires a validated controller path. On release, reconcile the workspace/repository and resume from the unchanged Step-1 cursor; do not restart or skip a bootstrap state.
