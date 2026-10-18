# Lineage staging and reconciliation — 2026-10-18

## Custody
- Repository: MythicalXenos/dls26-omega; configured remote: origin.
- All four discovered DLS26 Omega remote branch snapshots are staged read-only in this transaction. `manifest.json` pins each ref, commit, tree, path, Git blob OID and SHA-256; all 2,524 current-tree payloads in the four tar archives were re-hashed and matched (PASS).
- Open PR #6: https://github.com/MythicalXenos/dls26-omega/pull/6, head `arena/357aaddf-dls26-omega` at `7f198081f90f429de561edeb066fcf72af0815a2`. The PR head, staged archive, fetched remote ref and GitHub metadata agree.

## Primary checkpoint candidate — PR #6
- Validated published checkpoint `ckpt-0002-step1-epoch-open`, turn sequence 2, `READY_TO_YIELD`, `CONTINUE`, `STATE_1_RESEARCH_SWEEP`, Step 1; `continuation_allowed=true`, `needs_user=false`.
- Predecessor `ckpt-0001-setup-complete` is present in the Setup commit and is bound by `docs/contracts/setup_0001.json`; all ten declared obligations are present, and the successor is Step 1 at the next turn boundary. Setup exit evidence and the open epoch contract agree with the current handoff and manifest.
- Exact resumption cursor is preserved in the imported handoff/manifest: Q-008 through Q-013, then classify all CONNECTED/UNCERTAIN references; epoch-0001 remains OPEN. No Step-1 exit is inferred.
- Prompt capture on the PR head was 175,594 bytes, SHA-256 `35eb78178fac8f03e970e4a81c720d59d7709470667d50529865aaf408492cac`; live prompt and the legacy-named v76 archive were byte-identical.
- External controller consumption/acknowledgement is not exposed in repository evidence. This import does not claim exactly-once controller execution. The current turn is a user-directed recovery, not a watchdog send.
- Imported Step-1 claims are unpromoted and remain quarantined pending evidence reconciliation; the source log carries partial summaries, not complete immutable primary payloads for every claim.

## Other discovered branches — preserved, not admitted to the active KB
- `arena/b5d5681d-dls26-omega` at `66d4289f81d564674dfbe60c3ea0c2c0821652a8`: large historical corpus. Its `handoff/HANDOFF.md` describes checkpoint 028 / 156 claims, while the head is checkpoint 196 / turn 35 wave 120; `logs/turn_manifest.json` remains at turn 22. The latest handoff/manifest do not bind the current head, so it is not a validated resumption checkpoint. Claims/evidence remain quarantined; any future baseline import requires the full five-pass audit.
- `arena/22655f48-dls26-omega` at `a3109c7bbec7d6b5a148004683e2ad3866de9e91`: older Step-1 turn-7 lineage, preserved but not selected over the open PR checkpoint.
- `arena/a7e23a6b-dls26-omega` at `5ab3ec688b2c8bd33e00778dd9a8af775b3cb7a6`: older v77 lineage with a different control/manifest schema and no matching active PR; preserved but not selected.
- No claims, prompt rules, counters or control-plane state were imported from those three historical branches. Their immutable snapshots remain available under this transaction for later five-pass custody, witness, skeptic, devil's-advocate and reconciliation work.

## Branch-constrained recovery
- The session-bound writable branch is `arena/1e90cb90-dls26-omega`; all new commits/pushes remain on it. PR #6 is left open and untouched, and no second PR is opened. The validated PR checkpoint is staged and will be recovered on the bound branch without rewriting its source ref.

## Outgoing prompt archive
- `docs/prompt_archive/OMEGA_PROMPT_v78.md` was copied from the pinned PR head before any v80 live-prompt write; bytes: 175,594; SHA-256: `35eb78178fac8f03e970e4a81c720d59d7709470667d50529865aaf408492cac`.
- Existing `OMEGA_PROMPT_v76.md` is retained unchanged. The prior changelog records that it was byte-identical to v78 but mislabeled; the new correctly versioned archive repairs discoverability without rewriting history.

## Recovery-tool deviation
- A first unquoted shell here-document expanded inline backticks as commands while drafting this report. The resulting draft was detected immediately from shell diagnostics and replaced from pinned repository data; the v78 archive is byte-identical and unaffected, and no imported claim or checkpoint was changed. Record this as a self-detected DEGRADATION EVENT / issue when the active operational log is restored.
