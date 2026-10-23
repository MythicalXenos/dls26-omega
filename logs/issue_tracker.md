# Issue Tracker

Each entry: ID, opened (UTC), status, severity, description, action, owner.

## ISSUE-001 — unresolved prompt cross-references — opened 2026-10-18T15:32:51Z — OPEN (partially addressed by v80) — severity High
- The v78 audit identified many missing named rules. v80 now supplies a five-pass import audit, `MECHANISM 5` confidence gates, mechanisms 6–9, evidence contracts, and the new liveness/recovery/dispatch rules; those portions are no longer missing.
- Remaining reproducible examples include `OMEGA-SQUAD-001` pointing to `MY SQUAD — MY GROUND TRUTH` with no matching canonical section; references to `Knowledge Management`, `PROMPT VERSIONING`, `Notification Threshold`, `Special Card Tracking`, `Datamining hard constraints`, `NO OUTPUT DURING BOOTSTRAP`, and related named sections that do not resolve to a unique canonical definition. Full list and test limits are in `docs/prompt_integrity/v80.json`.
- Action: no prompt edits by agent. Preserve conservative defaults; user-only repair is proposed as PROPOSED-D in `docs/PROMPT_CHANGELOG.md`. The v80 FAIL blocks a production-ready declaration.
- Owner: user (prompt text), agent (tracking).

## ISSUE-002 — legacy v78 version label/archive path mismatch — opened 2026-10-18T15:32:51Z — CLOSED-WITH-NOTICE — severity Low
- The original v78 text mandated a v76 archive filename. The legacy `OMEGA_PROMPT_v76.md` remains unchanged; a correctly versioned `docs/prompt_archive/OMEGA_PROMPT_v78.md` was copied from the pinned PR #6 prompt and byte-verified before the v80 live write. v80 now has its own v80 archive path. Historical mismatch is preserved, not rewritten.
- Owner: agent (archive); user (future prompt wording).

## ISSUE-003 — two manifest vocabularies — opened 2026-10-18T15:32:51Z — CLOSED-WITH-NOTICE — severity Medium
- v80 retains an older short manifest block with legacy `HARD_STOP_*` values, then explicitly supersedes obsolete manifest specifications, legacy terminal classes and duplicate watchdog instructions with `OMEGA-LIVENESS-001` / `OMEGA-DISPATCH-001`.
- Operational authority remains the six-class v80 contract. This closes the textual conflict with notice; controller execution is separately unverified under ISSUE-005.

## ISSUE-004 — digest append-size deviation — opened 2026-10-18T15:32:51Z — CLOSED-WITH-NOTICE — severity Low
- The original digest's second block exceeded the 12,000-character append rule in one write. Historical deviation retained. Future digest additions are split into chunks at or below 12,000 characters.

## ISSUE-005 — controller identity/consumption not exposed — opened 2026-10-18T15:32:51Z — OPEN — severity High
- The agent cannot observe the configured browser controller's conversation identity, durable consumption receipt, single-writer lock, exact-once acknowledgement or runtime tests. Repository evidence does not show PR #6 controller consumption. The current turn is not a watchdog send.
- Action: do not authorize unattended continuation. User/controller owner must expose a validated test path or keep the run manually controlled. No automatic retry or continuation is asserted.

## ISSUE-006 — device and APK tooling absent — opened 2026-10-18T15:32:51Z — OPEN — severity Medium
- Reverified 2026-10-18T20:56:38Z: `adb`, Java/Javac, apktool, jadx, aapt/aapt2 and KVM/device path are unavailable in this sandbox. STATE_2/STATE_3 work cannot be fabricated. At the relevant transition, place the exact dependency request in `handoff/attention_required.md`.

## ISSUE-007 — irreversible-action list not complete — opened 2026-10-18T15:32:51Z — OPEN — severity Medium
- `kb/irreversible_actions.md` contains candidates only. Its referenced claims are quarantined by the v80 five-pass audit; no action type is admitted as verified. Step 1 research and first-contact disclosure remain owed.

## ISSUE-008 — NO OUTPUT DURING BOOTSTRAP Yes-list reference unresolved — opened 2026-10-18T15:32:51Z — OPEN (behavior conservatively covered) — severity Medium
- v80's `OMEGA-OUTPUT-001` now imposes a strict one-line output contract and prohibits question-tool use during bootstrap, so the operational default is no questions. The named Yes-list rule still has no canonical section/definition and remains a cross-reference defect under ISSUE-001.

## ISSUE-009 — confidence gates previously undefined — opened 2026-10-18T15:32:51Z — CLOSED-WITH-NOTICE — severity High
- v80 supplies `MECHANISM 5 — CONFIDENCE PROMOTION GATES`. No legacy claim was promoted during migration. Its `Community Consensus tier` reference is inconsistent with the listed gates and is tracked as ISSUE-013.

## ISSUE-010 — tier words named by system — opened 2026-10-18T15:32:51Z — CLOSED historically; v80 regression tracked separately — severity Low
- The v78 operational application was logged. v80 contains a new confidence-label inconsistency; see ISSUE-013. No v80 claim tier is assigned by this entry.

## ISSUE-011 — imported source conflicts from turn 2 — opened 2026-10-18T15:41:35Z — OPEN — severity Medium
- The inherited records describe CONF-001 (launch-date leads) and CONF-002 (Summer Spotlight/version leads). Their cited sources are not all immutable primary payloads; the five-pass audit leaves CLM-0010–CLM-0012 quarantined. These are reported conflicts/leads, not verified game facts.
- Turn 5 Q-008 slice fetched App Store chunks 1–4 and Google Play chunk 1. Returned App Store text associates Summer Spotlight with 13.320–13.350 (dates without years), and labels 13.120 Mar 25 “Winter Reload,” conflicting with the quarantined CLM-0011 summary. No unique Summer Spotlight date or Android build is established; source payload/hash is unavailable. Q-002/CONF-002 remain open; CLM-0010/0011 remain quarantined and unchanged. See `kb/research_observations/2026-10-23-Q-008-official-store-slice.md`.

## ISSUE-012 — v80 source fidelity and prompt integrity gate fail — opened 2026-10-18T21:03:32Z — OPEN — severity High
- Live v80 and archive are byte-identical (184,126 bytes, SHA-256 `495bd2dc946c4ec999914e839952ef17aeef9777ba0cf0f7d87e465451ba014a`), but the original user-supplied v80 bytes/hash are not available in this resumed context. Three known transcription defects were repaired; further defects cannot be excluded. The assertion ledger fails source fidelity and cross-reference checks.
- Action: preserve this draft and its diff; ask the user through `handoff/attention_required.md` to provide/confirm an exact source or hash. Do not call the text verbatim or production-ready. User alone repairs prompt rules.

## ISSUE-013 — Community Consensus conflicts with five-tier gates — opened 2026-10-18T21:03:32Z — OPEN — severity High
- `MECHANISM 2` calls “Community Consensus” a confidence tier. `MECHANISM 5` lists five gate labels without it, and `OMEGA-EVIDENCE-001` says community-controlled testing is an origin/method tag, not a confidence tier. This is an internal taxonomy conflict.
- Action: leave all imported claims quarantined and unpromoted; user-only prompt repair via PROPOSED-D.

## ISSUE-014 — capability inventory path migration — opened 2026-10-18T21:03:32Z — CLOSED-WITH-NOTICE — severity Low
- v80 names `docs/capabilities.md`; the existing inventory is `docs/CAPABILITY_INVENTORY.md`. A symlink alias now points the v80 path to the existing inventory, avoiding duplicate content. The schema documents the alias and single source of truth.

## ISSUE-015 — audit tooling deviations — opened 2026-10-18T20:56:38Z — CLOSED-WITH-NOTICE — severity Low
- The first read-only Python audit command had a quoting SyntaxError before executing any checks or changing files; it was rerun successfully with a corrected script. The import-audit report was also written twice identically because of a duplicated parallel tool request. No files diverged and no evidence was lost.

## ISSUE-016 — legacy evidence payloads missing — opened 2026-10-18T21:03:32Z — OPEN — severity High
- Five-pass audit of CLM-0001–CLM-0012 found source summaries/snippets but not complete immutable primary payloads, payload hashes, and extraction spans for every citation. Passes 1–3 therefore fail or are blocked; the records remain read-only and quarantined. Full per-claim dispositions: `docs/audits/2026-10-18-v80-import-audit.md`.
- Action: restore or re-fetch permissible primary evidence, then rerun all five passes before admitting any claim.

## ISSUE-017 — state-specific exit predicates incomplete — opened 2026-10-18T21:03:32Z — OPEN — severity High
- `OMEGA-INTEGRITY-001` requires every state to have entry, completion and successor conditions. The canonical state list names STATE_2_STATIC_ANALYSIS and STATE_3_DEVICE_PIPELINE but does not define their state-specific entry/exit evidence or successor predicate. General transition prose is insufficient. See the assertion ledger.
- Action: user-only prompt repair; no state transition is inferred.

## ISSUE-018 — later-turn wall-clock budget exceeded — opened 2026-10-18T21:03:32Z — OPEN — severity High
- OMEGA-BUDGET-002 sets a 360-second end-to-end ceiling for later bootstrap turns. The first same-turn clock observation was 20:56:38Z and checkpoint preparation continued through 21:12:50Z, a span of 16m12s; the turn itself began earlier, so the ceiling was exceeded by at least 10m12s. Exact turn-start time was uninstrumented. This was not certified as compliant.
- Action: no further game research in this turn; record as DEGRADATION EVENT, keep continuation paused, and require reliable turn-deadline instrumentation/reserve enforcement before future automatic work.
- Turn 5 recurrence: earliest same-turn clock observed at 2026-10-23T15:36:29Z; cursor-correction/publication workflow had reached 2026-10-23T15:42:35Z (at least 6m06s elapsed, so at least 6 seconds over the 360-second ceiling; final push completed later). Exact turn start/final-action times were not instrumented. Same budget-control cause; no further research after detection.

## ISSUE-019 — local branch/worktree reset after checkpoint — opened 2026-10-19T18:35:53Z — CLOSED-WITH-NOTICE — severity Low
- At turn start, the fixed local branch name pointed to base `fb9a2c025ec267f6b787382766ce44c7e373d091`; remote `arena/1e90cb90-dls26-omega` pointed to `408ba78fd03fbc8ecc96cd9281fb935a67d6a6cd`, and the workspace files appeared untracked. Compared every one of 67 remote tree entries by Git blob ID and checked for extras: all bytes matched and there were no workspace-only files. Aligned the same local branch to the remote tip; no branch switch or data loss.
- Recurrence: at turn 5 start, the same environment/ref-pointer reset recurred: local ref at base `fb9a2c0`, remote at `8fae263`; all 67 blobs again matched, no extras, and the fixed branch was aligned without loss. This is the same cause, not a new issue. Action: reconciliation recorded in `docs/REPO_ACCESS_VERIFICATION.md`; closed with notice.
