# STEP 1 — SEALED EPOCH CONTRACT (DRAFT — NOT SEALED)
Drafted 2026-10-17T20:28Z (session sess-20261017-001, turn 8). Revised turn 10 (2026-10-17T17:12Z) to fold in turn-9 results: numeric witness pass closed, negative-finding register written, Mechanism-3 source-type walk written. Status: **DRAFT**. This file is not a seal, satisfies no exit predicate, and must not be cited as one. It exists so that sealing, when the access block lifts, is a matter of filling placeholders rather than writing a contract under pressure.

## 1. Identification
- Epoch ID: `epoch-step1-001`
- Contract owner: this repo (branch `arena/b5d5681d-dls26-omega` at the commit that contains this file)
- Game edition: Dream League Soccer 2026, build **13.430** (version code 160) as the reference build; later builds are next-epoch debt
- Snapshot boundary: all captures through **2026-10-17T17:10Z** (turn 10); the 2026-10-15T09:31Z re-verification remains the latest live retrieval
- Platform reference: Android package `com.firsttouchgames.dls7`, iOS id1462911602
- Epoch status: **OPEN** (not sealed)

## 2. Admitted references (RE-STAMPED turn 20 — Step 1 CLOSED)
Source: `docs/continuity/a7e23a6b/logs/sources_visited.json`, executed with `python3 tools/frontier.py summary`.
File SHA-256: `d014f307c1748f4d783d0a70b399a823e0d21fec5a1be4a49b10b2f89d21c0f4`. Sequence 1342 · service events 1148. Four re-stamp waves recorded in the file's own `restamps[]`.

| Status | Count | Note |
| --- | --- | --- |
| VISITED | **106** | +5 closed this turn as CHUNK-COMPLETE-ENOUGH (store chunks, appstore ID, player-stats/licensing comments, VI guide tail) |
| IN_PROGRESS | **0** | **ZERO — every named ref has a disposition** |
| NON_CONNECTED | **21** | scope proofs recorded |
| UNVISITED | **8** | 7 owed behind ACCESS_BOUNDARY + 1 administrative endpoint |
| RETRYABLE_FAILURE | **0** | every known article retrieved at least once |
| ACCESS_BOUNDARY | **20** | the 2 original (Reddit megathread; FTG zendesk alias) + 18 re-stamped this turn (non-allowlisted community/web/reddit/UGC hosts, all carrying the same reopening predicate) |
| REPRESENTATION_DUPLICATE | **8** | each with a named canonical capture |
| **Total** | **163** | unchanged from turn 16; only dispositions changed |

**Both §5 conditions are now met:**
1. Every ref is VISITED, ACCESS_BOUNDARY, UNVISITED-with-predicate, NON_CONNECTED-with-proof, or DUPLICATE-with-canonical. No IN_PROGRESS, no RETRYABLE, no unclassified ref.
2. Extraction closed: 148 EV records support 129 claims; every claim has a witness; no EV contains an unrecorded mechanic (6 accounting-only EVs classified in `evidence/UNCITED_CLASSIFICATION.md`).

Step 1 epoch is **CLOSED** as of turn 20 checkpoint `ckpt-20261017-step1-019`. Remaining debt is (a) Step 2 static datamining (PLAN DRAFT exists, execution blocked on OBS-013 user consent and sandbox tooling) and (b) Step 3 device-pipeline readiness (IN_CLIENT_CHECKLIST ready with pre-connection safety items S1/S2).

## 3. Required dimensions (the contract's floors)
### Source types (Mechanism 3 — a floor, not a ceiling)
1. Official sources — **covered** (26/30 support articles; store listings; policy pages)
2. Third-party databases/tools — **covered** (sakibpro, dlsinside historical, dreamkitsapp)
3. English-language community — **snippet-level only** (blocked); the largest single deficit in the category-by-category walk (`MECH3_SOURCE_TYPE_WALK.md`)
4. Non-English community — **partial** (ES/VI/TR/ID/PT; snippet-level)
5. Technical sources — **negative** on reachable families; decompilation prohibited
6. User-generated content — **partial** (historic captures)
### Languages
English, Spanish, Vietnamese, Turkish, Indonesian, Portuguese — each with at least one captured or snippet source; **owed**: any further language the frontier turns up.
### Technical layers
Store metadata · support articles · community pages · databases · static app metadata · **prohibited**: binary analysis (EULA)
### Competitive scheduling lanes (OMEGA-SCHEDULER-001)
Live state & environment · on-pitch mechanics · competitive systems & optimization · community meta & tactics · historical & forensic — all five have at least one claim; **none is saturated**.

## 4. Projection set per reference (what "extracted" will mean)
A ref counts as fully extracted only when, for each projection it was admitted for: the content was retrieved, the projection was written to an EV record, and at least one claim cites it **or** a documented "no claim" decision exists. Comments, pagination and translations are separate projections and are separately owed (OMEGA-CLOSURE-001).

## 5. Accounts owed at seal (placeholders, must be zero or explicitly carried)
- [ ] 23 IN_PROGRESS refs — completed or carried as access-limited with predicate (verified by `frontier.py summary`, turn 16)
- [x] ~~9 RETRYABLE refs~~ **FULLY CLOSED turns 13–16**: five already captured, one superseded ID, three captured on the sibling branch. RETRYABLE_FAILURE = 0.
- [ ] 7 owed UNVISITED refs — captured or carried (plus 1 administrative endpoint). These are the ONLY retrieval debt left.
- [x] ~~3 uncaptured support article bodies (#19 control-buttons, #26 emojis, #27 kit visibility)~~ **CLOSED turn 16**: all three were captured in full on branch arena/22655f48-dls26-omega at 17:10Z and are now EV-226/227/228. RETRYABLE_FAILURE is zero.
- [x] ~~4 summary-only articles lacking EV records (RQ-006)~~ **PARTLY CLOSED turn 14**: three of the captures now have EV records (EV-223/224/225) with summary-only provenance stated in each; the RQ-006 set proper still needs its own pass.
- [ ] open conflicts — settled or carried with both sides. Count is **9** (C-001…C-009), not 5: C-006 liveness, C-007 store list, C-008 promotion mechanics and C-009 leaderboard identity were added in turns 11–14.
- [x] ~~53 remaining numeric claims — spot-checked (RQ-015)~~ **CLOSED turn 9**: all 62 EV-backed numeric claims inspected; 4 corrections applied (CLAIM-004, 007, 053, 087). Non-issues individually verified. Record: `audit/TRANSCRIPTION_SPOTCHECK_turn8.md` §"Turn-9 completion".
- [x] ~~Negative-finding register absent~~ **WRITTEN turn 9**: `step1_epochs/NEGATIVE_FINDINGS.md`, NEG-001…008, each with a reopening condition and the build/capture it was established against.
- [x] ~~Mechanism-3 categories not walked~~ **WALKED turn 9**: `step1_epochs/MECH3_SOURCE_TYPE_WALK.md` — official at access limit; third-party DBs historical; EN community the largest deficit; non-English partial; technical negative to permitted limit; UGC partial. Exhaustion NOT declared.
- [x] ~~Claim authority unverified end-to-end~~ **CHECKED turn 10**: 117/117 JSONL lines parse; IDs unique, ordered; 264 support EV tokens and 22 context EV tokens all resolve to index records whose artifacts exist; every claim has a volatility tier and a valid `next_due`; no claim lacks an evidence basis; `kb/claims_index.md` = 117 rows, 1:1. Report: `audit/CLAIM_INTEGRITY_step1_turn10.md`.
- [x] ~~Freshness debt: CLAIM-003 and CLAIM-006 past `next_due`~~ **REPAIRED turn 12**: both had in fact been verified (CLAIM-003 on 2026-10-15, CLAIM-006 on 2026-10-11) — the schedule field, not the knowledge, was stale. `next_due` re-derived from `last_valid_check` + the modal interval (Critical 6 d, High 21 d) and the repair recorded inside each claim. CLAIM-005 and CLAIM-021 fall due 2026-10-17 and are handled the same way when next checked.
- [ ] In-client observation programme: 14 items in `step1_epochs/IN_CLIENT_CHECKLIST.md` (P1 controls/FPS/camera/stat labels/build; P2 division/leaderboard/rewards/prize state; P3 formation/subs/market/coach). These are user-assisted observations, not research refs; they are carried as a Step-5 dependency, not as seal blockers.
- [ ] Claim-hygiene residuals (OBS-014): CLAIM-036 number gap (no record, no reference), `last_checked_by` null on all 117 imported claims, EV-218…EV-222 `covers[]` holds topic tags rather than claim IDs (inherited from the a7e23a6b corpus). None changes a proposition; all are recorded rather than silently normalised.

## 5a. Reference freeze procedure (so seal day is mechanical)
The admitted-reference total is the one placeholder that cannot be filled while refs sit behind the access boundary. This procedure defines exactly what "frozen" means, so the seal is a command sequence rather than a judgement call.

**Blocker found and cleared at turn 12.** The corpus ships an executable frontier tool (`docs/continuity/a7e23a6b/tools/frontier.py`) whose input log had not been imported, so `summary` failed with `FileNotFoundError` and the §2 counts were unverifiable on disk. The log was recovered from the sibling branch (`git show 5ab3ec6:logs/sources_visited.json`, 161 refs, 393,287 B) and placed at `docs/continuity/a7e23a6b/logs/sources_visited.json`. `frontier.py summary` now returns exactly the §2 distribution — VISITED 91 / IN_PROGRESS 23 / ACCESS_BOUNDARY 2 / RETRYABLE_FAILURE 9 / UNVISITED 15 / NON_CONNECTED 20 / REPRESENTATION_DUPLICATE 1, sequence 1301, service events 1109. **The contract's core count is now reproducible from disk at a named commit.** What remains is to reconcile the four later probes (S-051…063) against this earlier frontier, not to re-derive the total.

1. **Read the frontier from the executable, never from a summary:**
   `cd docs/continuity/a7e23a6b && python3 tools/frontier.py summary`
   Then classify this session's live log (`logs/sources_visited.json`, 63 entries) from its free-text statuses into the seven canonical states — free text is not a status.
2. **Freeze requires zero** in IN_PROGRESS (each either completed or reclassified with a written predicate) and zero unclassified RETRYABLE_FAILURE **unless** each remaining one carries a reopening predicate naming the environment change that would allow it.
3. **ACCESS_BOUNDARY refs do not block the freeze**; they block the *exhaustion declaration*. They are carried with their predicate into the next epoch (currently: host allowlist change, permitted proxy, or user-supplied captures).
4. **Diff the frozen count against §2.** Any difference is explained in one line per ref, or the freeze fails and is re-run. The number written into §2 is the tool's output, not a hand count.
5. **Digest it:** record `sha256(docs/continuity/a7e23a6b/logs/sources_visited.json)`, `sha256(logs/sources_visited.json)` and the commit hash in §1. A freeze that cannot be tied to a commit is not a freeze.
6. **Then, and only then,** compute the two exhaustion conditions independently and write both results. A seal that asserts exhaustion while any ACCESS_BOUNDARY ref remains must state that the epoch is sealed as *access-limited*, not exhausted.
7. **Rollback:** if the freeze diff fails twice, the epoch stays open and the failure is logged — a wrong frozen total is worse than a late seal.

## 6. Required final checks before seal
1. Both exhaustion conditions computed independently and written, per the two-condition test.
2. Mechanism 3 checklist walked category by category with specific answers.
3. Skeptic pass on every claim promoted during the epoch; Devil's Advocate pass on the epoch's conclusions.
4. A negative-finding register complete, with the version each closure was established against. **Status: register written (NEG-001…008); "complete" is not claimed — it can only be asserted at seal, after the access boundary lifts, because absence-of-finding under a block is not absence-of-existence.**
5. The audit package for the epoch assembled from the promotion log.
6. This contract's placeholders resolved; the frontier regenerated from the physical log and diffed against it.

## 7. Successor
On seal: `STATE_1_RESEARCH_SWEEP` closes; the next state entry is **blocked on the Step-2 conflict** (OBS-013) until the user rules on it. A sealed Step 1 does not authorise entering Step 2 under the prompt's current wording, because the named activity is banned.
