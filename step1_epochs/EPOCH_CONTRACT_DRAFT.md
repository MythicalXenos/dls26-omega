# STEP 1 — SEALED EPOCH CONTRACT (DRAFT — NOT SEALED)
Drafted 2026-10-17T20:28Z (session sess-20261017-001, turn 8). Status: **DRAFT**. This file is not a seal, satisfies no exit predicate, and must not be cited as one. It exists so that sealing, when the access block lifts, is a matter of filling placeholders rather than writing a contract under pressure.

## 1. Identification
- Epoch ID: `epoch-step1-001`
- Contract owner: this repo (branch `arena/b5d5681d-dls26-omega` at the commit that contains this file)
- Game edition: Dream League Soccer 2026, build **13.430** (version code 160) as the reference build; later builds are next-epoch debt
- Snapshot boundary: all captures through **2026-10-17T20:00Z**
- Platform reference: Android package `com.firsttouchgames.dls7`, iOS id1462911602
- Epoch status: **OPEN** (not sealed)

## 2. Admitted references
| Group | Count | Source |
| --- | --- | --- |
| Frontier refs (t69) | 161 | `logs/sources_visited.json` @ 5ab3ec6 |
| VISITED | 91 | same |
| IN_PROGRESS | 23 | accounted in `INPROGRESS_ACCOUNTING.md` |
| NON_CONNECTED | 20 | scope proofs recorded |
| UNVISITED | 15 → 8 after disposition | `UNVISITED_DISPOSITIONS.md` |
| RETRYABLE_FAILURE | 9 | retry owed |
| ACCESS_BOUNDARY | 2 | reopening predicates recorded |
| REPRESENTATION_DUPLICATE | 1 | canonical pointer recorded |
| This session's probes | 13 (S-051…063) | capability + continuity, not game content |
| **Admitted total pending seal** | **to be frozen at seal** | — |

## 3. Required dimensions (the contract's floors)
### Source types (Mechanism 3 — a floor, not a ceiling)
1. Official sources — **covered** (26/30 support articles; store listings; policy pages)
2. Third-party databases/tools — **covered** (sakibpro, dlsinside historical, dreamkitsapp)
3. English-language community — **snippet-level only** (blocked)
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
- [ ] 23 IN_PROGRESS refs — completed or carried as access-limited with predicate
- [ ] 9 RETRYABLE refs — retried or carried
- [ ] 7 owed UNVISITED refs — captured or carried
- [ ] 3 uncaptured support article bodies (#19, #26, #27)
- [ ] 4 summary-only articles lacking EV records (RQ-006)
- [ ] 5 open conflicts (C-001…C-005) — settled or carried with both sides
- [ ] 53 remaining numeric claims — spot-checked (RQ-015)

## 6. Required final checks before seal
1. Both exhaustion conditions computed independently and written, per the two-condition test.
2. Mechanism 3 checklist walked category by category with specific answers.
3. Skeptic pass on every claim promoted during the epoch; Devil's Advocate pass on the epoch's conclusions.
4. A negative-finding register complete, with the version each closure was established against.
5. The audit package for the epoch assembled from the promotion log.
6. This contract's placeholders resolved; the frontier regenerated from the physical log and diffed against it.

## 7. Successor
On seal: `STATE_1_RESEARCH_SWEEP` closes; the next state entry is **blocked on the Step-2 conflict** (OBS-013) until the user rules on it. A sealed Step 1 does not authorise entering Step 2 under the prompt's current wording, because the named activity is banned.
