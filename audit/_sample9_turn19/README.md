# SAMPLE 9 (turn 19) — witness-physical verification after extraction wave 1

Date: 2026-10-17T22:20Z. Same stratified draw and procedure as samples 3–8.

## Draw

| Claim | Tier | First-pass | Post-repair |
| --- | --- | --- | --- |
| CLAIM-048 | Confirmed | WARN (covers) | OK |
| CLAIM-128 | Confirmed | OK | OK |
| CLAIM-013 | High Confidence | OK | OK |
| CLAIM-039 | High Confidence | OK | OK |
| CLAIM-059 | Community Consensus | WARN (covers) | OK |
| CLAIM-066 | Community Consensus | WARN (covers) | OK |
| CLAIM-090 | Speculative | WARN (covers) | OK |

**Post-repair: 7 OK / 0 WARN / 0 BAD.** All four WARNs were covers-array lag again. Back-stamped via `scripts/turn19_covers_batch3.py`.

## Post-extraction state

After wave 1 (`scripts/turn19_extraction_wave1.py` + `turn19_fixups.py`):
- 129 claims.
- 148 EV records (EV-001…EV-245 + EVD-0005…EVD-0010, EVD-0012).
- **Every claim now has at least one EV/EVD token in `supporting_evidence` except CLAIM-103**, which is a synthesis of four EV-backed claims (CLAIM-008/048/054/087) and carries an explanatory challenge noting the inheritance.
- 14 new EV records (EV-232…EV-245) created this turn: 10 service-record EVs (S-* backed), 3 derived-view EVs for topic-summary witnesses, 1 UGC EV for the World-Cup-Winners YouTube record. EVD-0005 added to the index (it was a file without an index entry, an old bookkeeping gap).
- 0 missing EV references, 0 bad covers.

## Cumulative error-rate tracking

| Sample | Turn | OK | WARN→OK | BAD | Substantive errors |
| --- | --- | --- | --- | --- | --- |
| 3 | 12 | 7 | 0 | 0 | 0 |
| 4 | 13 | 7 | 0 | 0 | 0 (1 supersession) |
| 5 | 14 | 3 | 3 | 1 | 1 (C-009) |
| 6 | 15 | 5 | 2 | 1 | 1 (CLAIM-020) |
| 7 | 17 | 2 | 5 | 0 | 0 |
| 8 | 18 | 7 | 0 | 0 | 0 |
| 9 | 19 | 7 | 0 | 0 | 0 |

Cumulative over 63 sampled claims: **2 substantive errors** (~3.2%). Three consecutive clean samples (7/8/9) — the corpus appears to have stabilised at bookkeeping-only defects.
