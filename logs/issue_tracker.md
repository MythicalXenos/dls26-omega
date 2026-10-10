# Issue tracker (logs/issue_tracker.md)

Entries: ISSUE-NNN, date (UTC), category, description, status, log reference. Problems and rule deviations are recorded here and in the main operational log.

## ISSUE-001 — DEGRADATION EVENT (self-detected), 2026-10-09
- Category: DEGRADATION EVENT. Description: two RULES DIGEST writes exceeded the 12,000-character append limit (15,653 and 14,155 characters). The content is complete and committed in 9448398. No content was lost.
- Status: logged. Later appends stayed under the limit. Remaining work continues in chunks under 12,000 characters.
- Log reference: main log, category DEGRADATION EVENT, topic "rules digest write size".

## ISSUE-002 — prompt capture incomplete
- Category: capture gap. Description: the pasted prompt references many sections that are absent from the text, including PROMPT CAPTURE, NO OUTPUT DURING BOOTSTRAP (and its Yes list), Mechanisms 5, 6 and 8, the bodies of Mechanisms 7 and 9, Confidence Promotion Gates, Session Handoff, First Session Bootstrap, Knowledge Management, Datamining, Analysis & Reasoning Standards, and others. The full list is OPERATIONAL_RULES.md section 6.
- Status: open. PROMPT CAPTURE settles this without a question, so the bootstrap proceeds on the captured text. Gaps are carried into the Step 5 consolidated ask if they still matter then.

## ISSUE-003 — duplicated broken header in the capture
- Category: capture anomaly. Description: OMEGA-SQUAD-001 appears twice. The first copy has a malformed refs list and a heading that runs into the "MY SQUAD" section. The second copy is complete.
- Status: open. The complete copy is used.

## ISSUE-004 — stale terminal enum in the manifest rule
- Category: prompt inconsistency. Description: the manifest rule lists expected_terminal_class as BOOTSTRAP_START | CONTINUE | HARD_STOP_STEP3 | HARD_STOP_COMPLETE. These predate the closed MACHINE-READ LINES vocabulary (ATTENTION_REQUIRED, PUBLICATION_PENDING, PROTOCOL_ERROR, COMPLETE).
- Status: open. The current vocabulary is used. A PROPOSED change is in PROMPT_CHANGELOG.md.

## ISSUE-005 — CAPABILITY INVENTORY ordering conflict
- Category: CONFLICT (rule collision). Description: the CAPABILITY INVENTORY paragraph calls the inventory the second file, immediately after the prompt file. The STATE_0 order and the RULES DIGEST paragraph place the digest before the inventory document.
- Resolution: STATE_0 order followed. The HARD STATE BOUNDARY RULE is the more specific rule (precedence rung 4). Status: resolved on the record; the user may confirm or correct.

## ISSUE-006 — empty rule bodies
- Category: capture anomaly. Description: OMEGA-BATCH-001, OMEGA-FRONTIER-001 and OMEGA-LAB-001 have IDs and refs but no body.
- Status: open. Behaviour follows the rules that reference them.

## ISSUE-007 — Mechanisms 5 to 9 incomplete
- Category: capture gap. Description: only Mechanisms 1 to 4 are present in full. Mechanism 7 (Devil's Advocate) and Mechanism 9 (Independent Verification, Occasions) are referenced without bodies. BOOTSTRAP_READY requires the combined audit package, so Step 4 can only produce the package under the rules that are present, with the limits recorded.
- Status: open. Blocks a complete audit package until the bodies exist.

## ISSUE-008 — tier definitions absent
- Category: capture gap. Description: the five confidence tier names (Confirmed, High Confidence, Community Consensus, Speculative, Disputed) appear only in references. Their definitions, quotas and promotion records are absent. Risk-tier and special-card-tier definitions and the two gap states are absent too.
- Status: open. Until defined, no claim may be promoted to a tier that needs those definitions. Claims stay at the lowest tier their evidence supports, with the gap recorded.

## ISSUE-009 — abbreviations and undefined game terms
- Category: pending resolution. Description: DLL, OVR, GK and XI, plus the undefined game terms listed in OPERATIONAL_RULES.md, must be resolved to DLS26's exact terms in Step 1 and recorded in kb/GLOSSARY.md.
- Status: open (Step 1 task).

## ISSUE-010 — session identifier assumption
- Category: assumption. Description: session_id a8a92133 is taken from the branch suffix because the host supplied no separate session identifier.
- Status: recorded. Confirm if the host later supplies a different identifier.

## ISSUE-011 — device access is required for STATE_3
- Category: blocked dependency. Description: no Android device, adb, or emulator is reachable (no /dev/kvm). STATE_2 and STATE_3 need user-supplied material or device access. Fabricated results are not permitted.
- Status: open. Batched into the consolidated ask at the process's end, not raised during Setup.

## ISSUE-012 — agent-declared conduct boundary
- Category: policy proposal. Description: the agent will not modify game files, saves or server data, bypass protections, intercept live traffic, or automate gameplay. This boundary is not in the prompt text. It is recorded in handoff/handoff.md and will be surfaced at STATE_3 for the user's confirmation.
- Status: open (awaiting user confirmation at STATE_3).

## ISSUE-013 — stray heading in Mechanism 7 area
- Category: capture anomaly. Description: a "COMPULSORY DEVIL'S ADVOCATE" heading appears with a body that is only the Mechanism 7 category note.
- Status: open; recorded with ISSUE-007.

## ISSUE-014 — no transcription check against the original
- Category: verification limit. Description: DLS26_OMEGA_PROMPT.md is an agent transcription. It cannot be checked byte-for-byte against the original message from inside the sandbox.
- Status: open. Capture status recorded as transcription, not MECHANICAL.

## ISSUE-015 — original prompt source unavailable at resumed turn
- Category: blocking dependency. Description: the current resumed context contains only a condensed summary, not the full Turn 1 prompt. No `DLS26_OMEGA_PROMPT.md` exists in the published checkpoint. Reconstructing a verbatim user-authored prompt from the digest would fabricate or omit content.
- Status: ATTENTION_REQUIRED. Setup remains incomplete; STATE_1 is blocked. Required input and resumption condition are in handoff/attention_required.md.
- Log reference: main log, category SETUP, topic "prompt capture blocked".

## ISSUE-016 — local branch reference diverged from published checkpoint
- Category: environment divergence. Description: at turn start, local branch `arena/a8a92133-dls26-omega` pointed to `fb9a2c0` while origin's branch pointed to `4bcee78`. Content comparison showed every local file matched the remote tree and there were no workspace-only files. The remote branch was fetched and the local branch pointer reconciled to it with a mixed reset; no worktree content was discarded.
- Status: resolved and recorded once for this cause. Local branch and remote now both point to the published checkpoint; working tree clean before this turn's blocker files.
- Log reference: main log, category SELF-AUDIT, topic "turn-start repository reconciliation".
