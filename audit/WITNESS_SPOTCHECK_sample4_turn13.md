# WITNESS SPOT-CHECK — SAMPLE 4: HIGH-CONFIDENCE SINGLE-WITNESS CLAIMS (turn 13)

Date: 2026-10-17T18:5xZ. Sample rule: eight claims from the **42 High Confidence claims never previously witness-tested**, biased toward those resting on a **single** evidence record — the configuration where a misreading has nowhere to hide and the tier offers no protection. Question: does the proposition say exactly what its one record says, no more and no less?

## Results

| Claim | Witness | Verdict |
| --- | --- | --- |
| CLAIM-009 | EV-107 (full article text) | **PASS, verbatim** — "No bots are used. There is no control of difficulty and there is no manipulation of any in-game situation, including team mate AI. There is no influencing of any outcome" |
| CLAIM-013 | EV-115 (chunk 0/4) | **PASS, verbatim** — every stat mapping matches, including the CON-linked skill list (Rabona/overhead, heel-chops, double-tap-or-swipe skill shots, step-over/Marseille/heel-flick) and ENERGY degrading all stats with speed most affected |
| CLAIM-014 | EV-116 (full article, version-marked "12200 onwards") | **PASS to source, superseded in fact** — see S-1 |
| CLAIM-016 | EV-118 (full text) | **PASS, verbatim** — coins, gems, coaches, dream point boosts, special players; DP from matches; purchasable boosts that temporarily raise DP per match |
| CLAIM-028 | EV-136 (full text) | **PASS, verbatim** — random player selection, permanent upgrade, Form Boost duration "as detailed by your Training facilities level (duration starts at a minimum of one match)" |
| CLAIM-039 | EV-157 (full text) | **PASS, verbatim** — Apple password + Screen Time, FTG advises against TouchID/FaceID, Android all / 30 min / never |
| CLAIM-094 | B-008 (derived summary of APKMirror) | **PASS at derived level, disclosure added** — see S-2 |
| CLAIM-116 | GS-029 (derived summary of a dlsinside database) | **PASS at derived level** — every count matches the summary, and the claim's own challenge already warns that "Exclusives 7,388" and "Hidden 270" are row counts of unverified meaning, not collection sizes. That challenge is the reason this claim is usable at all |

## Findings

### S-1 — CLAIM-014 states a rule that an official revision has since replaced
EV-116 (the 12200-era article) says the Progress Bank "rewards currency based on your DLL (multiplayer) XP". The **current** official article (EV-162, rev1) says it "rewards CURRENCY based on your SEASON POINTS", and EV-197 reinforces Season Points. CLAIM-014 reproduces its source faithfully — but a reader who consults CLAIM-014 alone receives a superseded rule with no marker.
**Action:** supersession note added to CLAIM-014 pointing to CLAIM-068/040 and to EV-162/197. No tier change: the claim remains an accurate record of the older article, and the newer text has its own claim. **Structural lesson:** tension ownership is asymmetric across the KB — when two claims describe the same mechanism from different eras, only one tends to carry the conflict. Any future sampling should test *pairs*, not just singletons.

### S-2 — CLAIM-094 quotes one side of an open conflict without saying so
The claim lists "24 languages" from APK metadata. That is C-001's Side B; the App Store lists 15. The claim is accurate about its source but reads as a global fact.
**Action:** challenge added naming C-001. No change to content or tier.

### S-3 — Two of the eight rest on derived Markdown summaries, not EV records
CLAIM-094 (B-008) and CLAIM-116 (GS-029) are witnessed only by `kb/*.md` entries produced in an earlier session. This is the same independence limitation recorded as D-03 in the degradation audit: the summary is a re-statement, and a re-statement cannot detect an error made during the original extraction. Both claims disclose their origin in `origin_history`; the limitation is real but bounded, and neither is currently load-bearing for a coaching decision.

## Cumulative position after four samples

| Sample | Focus | Claims | Findings |
| --- | --- | --- | --- |
| 1 (turn 8) | transcription, numbers | 10 | 2 corrections |
| 2 (turn 9) | all numeric claims | 62 | 4 corrections |
| 3 (turn 11) | mixed | 10 | 1 discrepancy (C-007) |
| 4 (turn 12) | interpretive / low tier | 10 | 1 conflict (C-008), 2 drifts |
| 5 (turn 13) | High Confidence, single witness | 8 | 1 supersession, 1 undisclosed conflict side |

**Union of witness-tested claims: 38 of 117 (32%).** Error *rate* is falling as tiers rise (High Confidence claims are cleaner than community ones), which is the direction the tier model predicts. It is still not zero, so the practice continues.

## Fixes applied this turn
- CLAIM-100: corrected from the live capture (see `FRONTIER_DELTA_turn13.md` §4); Speculative → High Confidence; proposition rewritten around the documented content.
- CLAIM-014: supersession note; CLAIM-094: C-001 disclosure.
- `kb/claims_index.md`: three rows regenerated (CLAIM-014 unchanged in tier, 094 unchanged, 100 updated).
- No tier lowered, no evidence deleted, no date bumped.
