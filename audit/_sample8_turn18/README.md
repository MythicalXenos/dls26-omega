# SAMPLE 8 (turn 18) — witness-physical verification of 7 claims

Date: 2026-10-17T21:55Z. Same stratified draw (2/2/2/1) and same procedure as samples 3–7, with the fix that integrity now also walks `evidence/raw/` and recognises `#anchor` references.

## Draw

| Claim | Tier | First-pass result | Post-repair |
| --- | --- | --- | --- |
| CLAIM-073 | Confirmed | WARN | OK |
| CLAIM-057 | Confirmed | WARN | OK |
| CLAIM-088 | High Confidence | WARN | OK |
| CLAIM-034 | High Confidence | WARN | OK |
| CLAIM-064 | Community Consensus | WARN | OK |
| CLAIM-061 | Community Consensus | WARN | OK |
| CLAIM-007 | Speculative | BAD (script) | OK |

**After repair: 7 OK / 0 WARN / 0 BAD.**

## Findings

1. **All seven initial WARNs were covers-array lag**, not broken witnesses. EV-171/183/184/218/219/140/192/186/187/189/190/001/002 all physically exist on disk and were correctly cited; their `covers[]` simply did not list every claim that later grew to cite them. All 13 were back-stamped (`scripts/turn18b_covers_backstamp2.py`).
2. **CLAIM-007 BAD was a script false positive**, not a content defect. EV-001 and EV-002 are legitimate `#ds-1` / `#ds-2` anchors inside `evidence/raw/search_digest_turn1.md` (they reference turn-1 search-result snippets), as listed in `evidence/index.jsonl`'s `artifact` field. My first-pass anchor-matching looked for a literal `#ev-001` inside the file, while the anchor label uses the `DS-` numbering. The EV record was correct; the check was wrong. CLAIM-007 carries a clarifying challenge for future auditors; no claim content changed.
3. **No substantive errors found this sample.** This is the first clean sample since sample 4 (turn 13). The two-sample run of error-rich findings (sample 5: C-009, sample 6: CLAIM-020) has not repeated; samples 7 and 8 produce only bookkeeping defects.

## Pre-connection safety items added to IN_CLIENT_CHECKLIST (S1, S2)

The checklist now leads with two items derived from turn-17 claims, to be confirmed on the player's device BEFORE any execution advice is followed:
- **S1:** verify Sign-in-with-Google / Sign-in-with-Apple is linked (CLAIM-128 no-recovery guarantee for unlinked profiles).
- **S2:** copy the System-Info text so we have the actual build string and a User ID recovery handle (CLAIM-125).
These are not research asks; they are safety gates.

## Cumulative error-rate tracking

| Sample | Turn | OK (post-repair) | WARN | BAD | Substantive errors |
| --- | --- | --- | --- | --- | --- |
| 3 | 12 | 7 | 0 | 0 | 0 |
| 4 | 13 | 7 | 0 | 0 | 0 (1 supersession) |
| 5 | 14 | 3 | 3 | 1 | 1 (C-009 scope gap) |
| 6 | 15 | 5 | 2 | 1 | 1 (CLAIM-020 "only" over-read) |
| 7 | 17 | 2 | 5 | 0 | 0 |
| 8 | 18 | 7 | 0 | 0 | 0 |

Cumulative over 56 sampled claims: **2 substantive errors**, ~3.6%. The rate is dropping as the corpus stabilises — the samples are now surfacing bookkeeping lag (which is easy and scriptable to fix) rather than factual errors.
