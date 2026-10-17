# SPOT-CHECK — TRANSCRIPTION FIDELITY ACROSS BRANCH BOUNDARIES (turn 8)
Run 2026-10-17T20:20Z (session sess-20261017-001). Method: automated witness pass over all 63 claims that both cite a preserved EV record and contain a number, then a manual read of the 10 highest-risk hits. The question was narrow: **does a claim's stated number actually appear in the record it cites?**

## Result table (automated pass, then manual disposition)
| Claim | Number(s) in proposition | Cited records | Found in cited text? | Disposition |
| --- | --- | --- | --- | --- |
| CLAIM-001 | years only | EV-001/002/103/104 | yes | no action |
| CLAIM-003 | surface enumeration | EV-101/102/110/222 etc. | yes (the "197" hit was a claim-ID fragment, not a fact) | no action |
| CLAIM-005 | 0.5–2s switching desync | EV-103, EV-002, EV-201 | **qualitative complaints yes, the 0.5–2s figure no** | **fixed**: the figure traces to the imported `research/turn1_discovery.md` (review text surfaced across searches) and EV-002; that record was added to the claim's supporting evidence. EV-103/EV-171 carry the desync complaint without a duration. |
| CLAIM-007 | 14,000+ players | EV-001, EV-002 | **no** | **fixed**: the figure is from EV-114 (sakibpro DB: "over 14,000 players"), which was missing from the evidence list. Added, with a challenge recording the correction. |
| CLAIM-008 | 13.040, 2025-12, 13.430 | EV-001, EV-183 | yes | no action |
| CLAIM-011 | article IDs | EV-107, EV-207 | yes | no action |
| CLAIM-021 | surface names | EV-116/126/197/162 | yes | no action |
| CLAIM-022 | account model | EV-125/213/214 | yes | no action |
| CLAIM-027 | matchmaking inputs | EV-135/209/222 | yes | no action |
| CLAIM-032 | 12.200+ release payout | EV-142/136/118 | yes | no action |

## Bonus finding
EV-114 states that player cards show "maximum potential (+10 OVR upgrades)". That is an **independent corroboration of the +10 development ceiling** in CLAIM-049, which previously rested on community consensus alone. Recorded as a cross-reference; no tier change, because a tool database is still one secondary origin and the ceiling remains unverified officially.

## What this check does and does not prove
- It proves that, for these ten claims, the number and the cited record agree — after two corrections — which is the specific failure the check was designed to catch (a figure drifting away from its source when a corpus is imported across branches).
- It does **not** prove that the cited record itself is correct, that the record was fully extracted, or that the claim's interpretation is sound. Those are the Skeptic's and the Devil's Advocate's questions, and both ran in earlier turns.
- Two corrections out of ten sampled claims (one evidence mis-attribution, one missing witness) is a high enough rate that the remaining 53 numeric claims should get the same pass rather than being assumed clean. Queued as RQ-20261017-015.

## Turn 9 — completion of the pass over all numeric claims
Method: automated witness test over every claim that cites a preserved EV record and contains a numeric token (62 claims after excluding claim-ID and evidence-ID fragments, years and dates), then manual reading of every unmatched hit.

| Claim | Unmatched number | Verdict |
| --- | --- | --- |
| CLAIM-004 | 10+ cups; 15 matches | **fixed** — "10+ cup competitions" is official store text in EV-103/EV-181 (added); "15 matches/season" is VI community text in EV-196 (added). A challenge now records that the two parts do not share a tier. |
| CLAIM-007 | 86 OVR | **fixed** — the 86 ceiling is in the PT guides EV-186/189/190 (added); the 14,000+ figure is EV-114 (added in turn 8). |
| CLAIM-053 | 15 languages | **fixed** — EV-185 states 15; EV-181 states 14; the APK metadata says 24. All three are now recorded, and the claim carries the three-way discrepancy as a challenge (conflicts C-001). |
| CLAIM-087 | 186 MB | **removed** — no preserved record witnesses that size. The figure is deleted from the proposition rather than re-attributed. |
| CLAIM-087 | 13.350 | no action — the number appears in a cross-claim reconciliation sentence referring to CLAIM-054/EV-177, not as this claim's own datum. |
| CLAIM-005 | 0.5 | no action — the witness is the imported research note `research/turn1_discovery.md` (line 84), added to that claim in turn 8; EV-103/EV-171 carry the qualitative complaint. |
| CLAIM-008, CLAIM-050, CLAIM-100 | fragments ("09", "002", "196", article IDs) | no action — ID/date fragments, or article IDs that legitimately cannot appear in a 404 record (CLAIM-100 cites the failure record EVD-0005). |

### Result
- 4 real corrections across 62 numeric claims (6.5%). Three were missing-witness errors and one was an unwitnessed figure.
- The pattern is consistent: numbers were right, but their witness lists were incomplete — which is exactly the failure mode that survives a merge undetected, and exactly why this pass was queued rather than assumed.
- The pass is now **complete** for claims citing preserved EV records. Claims resting on inherited summaries (no EV) cannot be tested this way; their witness is the summary itself and they carry that limitation in their origin history.
