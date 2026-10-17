# WITNESS SPOT-CHECK — SAMPLE 6: ECONOMY AND CADENCE PAIRS (turn 15)

Date: 2026-10-17T20:2xZ. Sample rule: four pairs chosen because they bear on **spending currency or match volume** — the two levers the eventual coaching plan will pull. Same pair method as sample 5.

## Pair A — gem sources vs coin sources: CLAIM-015 / CLAIM-019
- **EV-117, verbatim:** *"Gems can be obtained by completing league objectives, completing tournaments, through the Season Pass and Prize Ladder and by participating in Multiplayer (Dream League Live) mode. The quantity of Gems you receive will depend on the circumstance. You can also purchase Gems in the shop…"*
- **EV-122, the full coin list:** Winning Matches; Drawing Matches; Clean Sheets; Scoring Goals; Stadium Bonuses; Season Objectives; Season Pass rewards; Prize Ladder rewards; Final League Positions; Cup Wins; Watching Video Clips (where available).
- **Verdict: PASS, both verbatim.** One useful observation the pair makes visible: **the coin list has eleven entries and the gem list five, but no article gives a rate for any of them.** The economy is documented as *sources only*; every "what should I grind" question is therefore unanswered by official text and must be answered by measurement in-client. That is item 8 of the checklist, and this pair is the reason it exists.
- Secondary: EV-117 adds that gems come from DLL play "depending on circumstance" but never mentions leaderboard position — the community "weekly leaderboard gems" claim (C-002) describes a mechanism no official page states. C-002 updated.

## Pair B — acquisition vs churn: CLAIM-020 / CLAIM-029
- **EV-124, verbatim:** Transfers ("New players appear each in-game week i.e. after playing a single player match"), Scouts ("discounted rate"), Agents ("immediately add a player"), Prize Ladder ("special rare players when the criteria is met").
- **EV-137, verbatim:** *"Provided that you have the necessary number of players, you can discard (sell) players on your squad who are not in your Starting 11. You will be provided with a specified amount of bux for the removal of the player."*
- **CLAIM-020 FAILED on one clause — corrected.** It said *"Free coins only via short video clips."* EV-123 says *"Yes, you can watch short video clips to earn free coins (subject to availability)"* — no exclusivity, and the official coin list credits match wins, draws, clean sheets and goals, none of which require payment. The absolute was an over-reading. The proposition was rewritten to state the clip route as *one* advertised route and to stop conflating it with the acquisition channels (which are stable) — the two halves also carry different volatility.
- **CLAIM-029 minor drift.** The source says "bux"; the claim rendered it "bux/coins". The record itself had preserved the drift, so the claim normalised what the evidence deliberately did not. Challenge added, cross-refs to CLAIM-076/114, and the point is that the payout *type* is exactly what C-003 is unresolved about — a gloss here makes an open conflict look settled.
- **Verdict: one real correction, one wording drift.**

## Pair C — release schedule vs observed cadence: CLAIM-025 / CLAIM-103
- **EV-131, verbatim:** FTG does not provide future release/update schedules or planned activities on request; occasional news on TikTok/Instagram/Facebook.
- **CLAIM-103** cites no evidence records at all — only four other claims. Its "roughly monthly" is an inference from build dates, and its World Cup example rests on CLAIM-095/096, both Speculative single-source UGC.
- **Verdict: CLAIM-025 PASS (but it is a compound claim — see F-2). CLAIM-103 PASS only as a derived inference**, and it now says so in its own challenge. It should never be quoted as "FTG updates monthly".
- This pair is internally consistent: the studio publishes no schedule (official) *and* the community observes a cadence (derived). Those are not in conflict; they are different kinds of statement.

## Pair D — card rarity vs tier terminology: CLAIM-033 / CLAIM-012
- **EV-143, verbatim:** *"Depending on the overall rating of your player or if they are a special player, they will have a different player card colour, for example - common (bronze), rare (blue), legendary (gold), max (red) and special (black)."*
- **EV-110** records the "tier" search: Season Pass articles say "work towards tier five (the first tier is free)" and "unlock prize tiers in the Season Pass ladder", which are a different concept from LIVE Tier ranking.
- **Verdict: both PASS.** CLAIM-033's second half (re-signing/Recover/licensing) is accurate to EV-142/144 but belongs to a different mechanism — compound-claim defect (F-2).

## Findings

### F-1 — One substantive error: the "free coins only" absolute (fixed)
This is the kind of error the tier model is supposed to prevent: the claim was High Confidence, its sources were correct, and the sentence still said something no source says. It survived four earlier samples because none of them read EV-122 and EV-123 together.

### F-2 — Compound claims are a structural pattern, not three isolated slips
Three claims in this sample carry two unrelated mechanisms under one ID: CLAIM-020 (acquisition + ad availability), CLAIM-025 (schedule policy + profile transfer), CLAIM-033 (card colours + re-signing rules). In each case the first half is stable official text and the second half is build- or roster-dependent. A single tier cannot be honest for both halves, and a reader cannot tell which half a citation is supporting.
**Action:** recorded as a schema convention (`SCHEMA.md` §4c): *one mechanism per claim for all new claims*; existing compound claims are flagged in place rather than split, because splitting would renumber evidence links and invalidate the turn-8/9 witness record. CLAIM-020 was rewritten because it was also factually wrong; CLAIM-025/033 carry a flag only.

### F-3 — Derived claims are legitimate but must announce themselves
CLAIM-103 is the first claim found that rests entirely on other claims. That is allowed (a synthesis still needs a home), but it must not read like an observed fact. It now says "DERIVED" in its own challenge.

### F-4 — No rate data exists anywhere in the corpus
Across both currency pairs, the KB holds *sources* but zero *rates*. That is not a research failure — FTG publishes no numbers — but it means every "best way to earn X" answer must be measured, not cited. The in-client checklist item 8 is the only route.

## Cumulative position

| Sample | Focus | Claims | Findings |
| --- | --- | --- | --- |
| 1 | transcription, numbers | 10 | 2 corrections |
| 2 | all numeric | 62 | 4 corrections |
| 3 | mixed | 10 | 1 discrepancy (C-007) |
| 4 | interpretive / low tier | 10 | 1 conflict (C-008), 2 drifts |
| 5 | High Confidence singletons | 8 | 1 supersession |
| 6 | mechanism pairs, economy | 8 | 1 conflict (C-009), 1 real error, 3 compound-claim flags |

**Witness coverage: 54 of 118 claims (46%).** Six samples, six findings; none has been empty. The rate of *substantive* error is roughly one per fourteen claims read closely, which is the number that should govern how much of the remaining 64 claims can be trusted without reading.

## Fixes applied this turn
- CLAIM-020 proposition corrected (real error) and re-scoped; CLAIM-029 challenge + cross-refs; CLAIM-103, 033, 025 flagged.
- `logs/conflicts.md` C-002: EV-117 added, showing the official gem article never says leaderboard position.
- `SCHEMA.md` §4c: one mechanism per claim (new claims only).
- `step1_epochs/IN_CLIENT_CHECKLIST.md`: C-009 question promoted to **Priority 0**.
- No tier raised or lowered; no evidence deleted.
