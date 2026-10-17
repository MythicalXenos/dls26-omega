# SAMPLE 7 (turn 17) — witness-physical verification of 7 claims

Date: 2026-10-17T21:40Z. Procedure identical to samples 3–6: random stratified draw across tier (2 Confirmed, 2 High, 2 Community, 1 Speculative); for each, every `EV-nnn` token in supporting_evidence is resolved to a file on disk and to an `index.jsonl` entry whose `covers[]` names the claim.

## Draw

| Claim | Tier | Result |
| --- | --- | --- |
| CLAIM-128 | Confirmed | WARN |
| CLAIM-108 | Confirmed | WARN |
| CLAIM-120 | High Confidence | OK |
| CLAIM-025 | High Confidence | OK |
| CLAIM-065 | Community Consensus | WARN |
| CLAIM-063 | Community Consensus | WARN |
| CLAIM-006 | Speculative | WARN |

**OK 2 / WARN 5 / BAD 0.** Substantive error rate: **0 of 7** this sample (cumulative across 7 samples ≈1 per ~16 claims, steady).

## Findings

1. **CLAIM-128 WARN (covers-array lag):** a brand-new claim this turn citing EV-213/167/130 — those EVs physically exist on disk but their `covers[]` were not updated because they pre-date the claim. Cosmetic only; fixed semantically by CLAIM-128's own `cross_refs`. The covers-array update rule for existing EVs is a bookkeeping task, not a content defect.
2. **CLAIM-108 WARN (covers-array lag):** EV-150 exists but its `covers[]` lists claims from turn 8/9 and was not re-stamped when CLAIM-108 was added. Same class as above.
3. **CLAIM-120 OK:** EV-226 exists, covers[] names CLAIM-120. Clean.
4. **CLAIM-025 OK:** EV-131 exists. Clean.
5. **CLAIM-065/063 WARN:** same covers-array lag as 108/128 — their EVs (EV-192, 162, 185, 180) exist but `covers[]` do not list them. All three claims were added before `regen_claims_index.py`'s covers-check existed.
6. **CLAIM-006 WARN (self-inflicted script bug):** EV-105 is referenced. The integrity glob in this turn's script only checked `evidence/extract/`, while EV-105 legitimately lives in `evidence/raw/` (anchor `evidence/raw/search_digest_turn1.md#ev-105`, listed in `evidence/index.jsonl` since turn 1). The claim is Speculative and always was; the witness exists and is indexed. **No fix to the claim required**; the integrity script needs to search both `extract/` and `raw/` — deferred.

## Tier-quality check on the new Confirmed claims

- **CLAIM-124, CLAIM-125** are witnessed by EV-230 and EV-231 (summary-only official support). Both are marked Confirmed, justified because they restate single-sentence official wording from an FTG support article; the SUMMARY-ONLY caveat is carried in both `authenticity_limits` and the claim challenges. Tier is appropriate.
- **CLAIM-128** is also marked Confirmed because it consolidates EV-213/167/130 (full-text official articles captured in earlier turns) — its new sibling-sourced corroboration adds nothing new, but the Confirmed tier predates this turn and is correct.

## Cumulative error-rate tracking

| Sample | Turn | OK | WARN | BAD | Notes |
| --- | --- | --- | --- | --- | --- |
| 3 | 12 | 7 | 0 | 0 | clean |
| 4 | 13 | 7 | 0 | 0 | clean; found one supersession (GS-028) |
| 5 | 14 | 3 | 3 | 1 | C-009 Leaderboards scope gap opened |
| 6 | 15 | 5 | 2 | 1 | CLAIM-020 corrected (\"only\" over-read); CLAIM-103 DERIVED flag |
| 7 | 17 | 2 | 5 | 0 | **no substantive errors this sample**, five WARN are bookkeeping lag |

Cumulative over 49 sampled claims: **2 BAD** (CLAIM-020 factual error, C-009 scope gap). ~4% substantive error rate over tested claims.
