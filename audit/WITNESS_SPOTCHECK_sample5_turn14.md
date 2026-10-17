# WITNESS SPOT-CHECK — SAMPLE 5: CLAIM PAIRS (turn 14)

Date: 2026-10-17T19:5xZ. Sample rule: instead of singletons, **four pairs** of claims that describe the same mechanism from different angles. Sample 4 showed that tension ownership is asymmetric — when two claims cover one mechanism, usually only one carries the note. A pair test is the only way to see that.

## Pair A — ranking surfaces: CLAIM-002 vs CLAIM-021 / CLAIM-071 / CLAIM-003
**Sources:** EV-101 (`What are Leaderboards?`), EV-126 / EV-197 (`What are Season Points?`).
- EV-101, verbatim: *"Leaderboards are a way to compare your performance against other players in **Multiplayer (Dream League Live)**. Leaderboards reset at regular intervals (from 3-30 days) and users will receive prizes based on their position at the end time."*
- EV-197, verbatim: *"Season Points are earned from winning matches and your current total is shown on the **season leaderboard accessed from the Main Menu**. They are also used to unlock prize tiers in the Season Pass ladder."*
- **Both claims reproduce their sources.** But the pair exposes a scope fact that neither carries alone: the article that defines "Leaderboards" scopes them to **Multiplayer (DLL)**, while the Season Leaderboard is a **Main Menu** board whose *metric* is Season Points. Nothing in the corpus says whether these are one board or two, or whether Season Points are visible to other players at all.
- **Consequence for the mission:** CLAIM-003 lists the Season Leaderboard as a candidate "#1" surface. If it ranks only within a division, or only friends, or is not public, it cannot host a global "#1". That question is now explicit rather than assumed — see the amendment to CLAIM-003 and conflict **C-009**.
- Verdict: **PASS on transcription, gap on scope.** Recorded, not fixed by inference.

## Pair B — Dream Point Boosts: CLAIM-016 vs CLAIM-019
**Source:** EV-118 (Prize Ladder), EV-121 (Dream Point Boosts).
- EV-121 verbatim: boosts apply to "career matches, dream draft matches, scenario matches and DLL (multiplayer) matches. They will not apply to exhibition and friend matches… cannot be used if the Prize Ladder is complete or no longer active. Any unused Dream Point Boosts will remain in your inventory for the next Prize Ladder… subject to change as we run live services."
- CLAIM-016 states the reward list and that boosts temporarily raise DP per match. CLAIM-019 states the four-mode restriction, the carry-over and the inactivity rule.
- Verdict: **PASS both.** The pair is cleanly partitioned — no duplication, no contradiction, and the "subject to change" caveat is carried on the claim that needs it.

## Pair C — career ladder: CLAIM-010 vs CLAIM-045
**Source:** EV-103 (Google Play listing), EV-171/172 (store chunks).
- Both state 8 divisions and "Legendary Division". CLAIM-010 adds "this is separate from Dream League Live's online leaderboards/tiers" — an inference, but a safe one: the store copy names Global Leaderboards under Dream League Live and the career ladder under divisions.
- Verdict: **PASS**, with the inference labelled as such.

## Pair D — matchmaking: CLAIM-002 vs CLAIM-081
**Source:** EV-102 (matchmaking article, verbatim in full).
- CLAIM-002 summarises; CLAIM-081 reproduces the full input list and the "no overlaid difficulty controls" sentence. EV-102 contains both. CLAIM-081's added operational reading ("queue timing + Tier banding + location are the levers") is clearly marked as an implication, and it also correctly records that "recent results" is **not** in the official list while CLAIM-044's fairness charter mentions it — a real cross-document tension already preserved.
- Verdict: **PASS**, and the one tension is owned.

## Findings
1. **The only new problem is Pair A's scope gap (C-009).** The other three pairs are clean, which is the first sample with no transcription error at all.
2. **Pairs are cheaper per useful finding than singletons** — one conflict surfaced from four readings instead of eight.
3. **Asymmetry is real but not universal:** in Pair B and Pair D the tension is owned by one claim *and* cross-referenced by the other; in Pair A neither claim knew the other existed.

## Fixes applied this turn
- `logs/conflicts.md` **C-009** — are the DLL leaderboards and the Main Menu Season Leaderboard the same surface, and is Season Points rank public?
- CLAIM-003 amended with that open scope question (it is the claim that defines the mission's target).
- No tier changed. Cumulative witness coverage: **46 of 118 claims (39%)**.
