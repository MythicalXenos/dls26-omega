# OPERATIONAL RULES — behavioural reset document

**STATUS: STUB. Not yet built.** Built in STATE_4_OPERATIONAL_RULES per PROMPT.md §13 Step 4, from PROMPT.md and from what Steps 1–3 actually found. Reading this file alone must restore correct behaviour after context degradation.

**Do not treat this stub as the operational rules.** Until it is built, PROMPT.md is the authority and must be read in full at session start.

## Construction rules that apply when it is built (from PROMPT.md §8 OPERATIONAL RULES FILE)

- Contains ONLY the behavioural constraints that must survive CONTEXT ROT — nothing already enforced by another mechanism, no redundancy, no elaboration.
- Maximise coverage per token: every rule necessary, nothing redundant. Small comes from removing what is unnecessary, never from shortening what is needed. Length is never the constraint; necessity is.
- A rule that already lives in the research queue, issue tracker, or handoff systems does not belong here too.
- Re-read at session start and after each MAJOR WORK PHASE.
- Intentional deviation from THIS file: log it, put it in the issue tracker, notify the user. That clause covers this file only — it never licenses deviation from PROMPT.md or from an explicit user instruction.
- Every adopted amendment to PROMPT.md is carried into this file before the turn that adopts it ends.
- If missing or corrupted: read PROMPT.md from the repo and rebuild; log the reconstruction in the issue tracker and under DEGRADATION EVENT.
- If PROMPT.md and this file conflict, PROMPT.md wins.

## Added 2026-09-27T21:57Z (session 1 turn 8) — turn-start history verification (ISS-007)

Before committing in any turn: confirm the local branch `arena/01a0e3cd-dls26-omega` is at the remote tip (fetch, then compare `HEAD` with `origin/arena/01a0e3cd-dls26-omega`; behind/ahead must be 0/N, never diverged). The workspace can be re-cloned or reset between turns by the environment: files are snapshotted, `.git` history and repository git identity are not, and a fresh clone reads `git status` clean exactly like a healthy repo — so local state alone can never certify itself.
On discovering a reset (history missing, identity reverted, branch at the base commit): set the git identity (DLS26 Omega / omega@dls26.local), fetch the remote branch into a remote-tracking ref, `git reset --soft` to the remote tip to preserve index and working tree, re-commit the pending content (reusing message and tree where a orphaned commit exists), push, and verify the remote tip and a clean status. Never push a diverged chain; never force-push. Log every occurrence in the main operational log and the issue tracker.
