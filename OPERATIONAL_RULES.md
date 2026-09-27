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
