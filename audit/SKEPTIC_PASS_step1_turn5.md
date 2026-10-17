# MECHANISM 2 — INTERNAL SKEPTIC PASS (Step 1, turn 5)
Run: 2026-10-17T18:18Z–18:26Z (session sess-20261017-001). Scope: the 22 claims promoted in turn 4 (CLAIM-089…110), the regenerated claim index, and the claim-authority handover.
Purpose: check whether the EVIDENCE is complete and whether each promotion rests on a checkable origin at the tier it claims — not whether the conclusions are agreeable (that is the Devil's Advocate, Mechanism 7).

## Checks run
1. **Origin tracing per claim.** Every promoted claim cites an EV record or an inherited summary that names its capture. No claim cites a number that appears only in this session's prose.
2. **Independence assessment.** Where two sources exist, are they independent origins or one owner/one family? Six claims were affected (below).
3. **Tier fit against the promotion convention observed in the inherited corpus** (Confirmed ≈ official full text or ≥3 independent origins; High Confidence ≈ 2 origins or single official surface with interpretation; Community Consensus ≈ multi-source community agreement; Speculative ≈ single weak source).
4. **Mixed-provenance scan.** A claim that combines an official fact with a community inference cannot inherit the official tier for the whole proposition.
5. **Duplicate scan** across all 111 claims (proposition overlap, not ID collision).
6. **Conflict scan** for pairs that assert incompatible numbers.

## Findings and dispositions

| # | Finding | Disposition |
| --- | --- | --- |
| S-1 | CLAIM-093 mixed provenance: the five-facility LIST is official, but the per-level percentages (+13%/+21%) are a single VI guide. Promoting the whole claim as High Confidence let a community number ride an official tier. | **Corrected.** CLAIM-093 narrowed to the official list at Confirmed; effect values split into CLAIM-111 at Community Consensus with an explicit single-family challenge. |
| S-2 | CLAIM-092 mixed provenance: part (a) was one Reddit thread, part (b) multiple threads. A single claim took the stronger tier for the weaker part. | **Corrected.** CLAIM-092 keeps the multi-thread copy-existence finding at Community Consensus; the 60,000-point single-thread report is now CLAIM-112 at Speculative. |
| S-3 | CLAIM-066 says DLL pays "weekly-leaderboard gems", while CLAIM-002 (official) says leaderboard resets are 3–30 days and CLAIM-051 (ID guide) says weekly gems. Cadence is unresolved and "weekly" is a community assumption. | **Challenge recorded** on CLAIM-066; cadence stays unresolved, not repeated as weekly. |
| S-4 | Language-count conflict: CLAIM-053 (store listing) says 15 languages; CLAIM-094 (static APK listing data) says 24. These may measure different things (store-localised listing vs packaged resources), but as written they are incompatible numbers. | **Challenge recorded** on both; neither may be quoted as "the" language count until a datamined resource count or official statement settles it. Logged as an EVIDENCE disagreement, not a rule conflict. |
| S-5 | CLAIM-103 (live-service cadence) is an inference from one official surface (store version history). It is not a stated FTG policy, and CLAIM-025 says FTG does not publish schedules. | **Challenge recorded**; tier held at High Confidence provisionally (the underlying version list is official and the cadence is directly countable), with the more conservative treatment named. If the next version-history capture contradicts the observed cadence, it drops to Speculative. |
| S-6 | CLAIM-110 is supported by EV-188/190/191, all from one Portuguese content family (dreamkitsapp + gameoverdrive). Counting them as three origins would be independence inflation. | **Challenge recorded**; the claim is capped at Community Consensus and may not be promoted without an unrelated origin. |
| S-7 | Duplicate scan: CLAIM-008 (launch resolution) and CLAIM-054 (version timeline) overlap on the 13.040 / 17-12-2025 launch date. This is complementary, not contradictory — one resolves the launch, the other carries the timeline. | **Not merged.** Cross-references added (`cross_refs`), with CLAIM-008 named as the launch-date authority. |
| S-8 | Official-claim exemption check: CLAIM-098 (Clans), 106 (Auto Switch), 107 (skill moves), 108 (connection ladder) are quoted official text with zero conflicting source and zero interpretation. | **Exemption holds**, but the deception re-screen still ran: all four are FTG's own support text about its own product, which is the interest-bearing origin; none of the four asserts a competitive advantage, so no incentive distortion is plausible beyond ordinary obsolescence. Volatility tiers carry the obsolescence risk. |
| S-9 | CLAIM-089 (My Club surface) contains one interpretive sentence ("the two surface names may coexist across versions"). | **Accepted with note** — the interpretation is flagged in the proposition itself; the verifiable part is the documented menu path. |
| S-10 | CLAIM-097 (OVR = Overall) has no official origin; two secondary sources (a tool FAQ and a guide) define it. | **Accepted at High Confidence** with the official-text gap recorded; it must not be used as if official terminology until Step 2 datamining or official wording lands. |

## Result
- 2 claims corrected by splitting (093, 092), 2 new claims created from the split (111, 112), 4 challenges added (066, 053, 094, 103, 110 — five challenge fields, one of them shared across 053/094), 2 cross-references added.
- No claim was promoted by this pass; one could have been (093) and was not.
- Claim count 111: Confirmed 28 / High Confidence 48 / Community Consensus 21 / Speculative 13 / Disputed 1.
- The pass found no fabricated value, no uncited number, and no tier that survived only because its source looked credible. It found two provenance-mixing errors, which is the failure mode this mechanism exists to catch.
- Ledger entries written to `logs/main_operational_log.md` under SKEPTIC CHALLENGE and EVIDENCE CONFLICT.
