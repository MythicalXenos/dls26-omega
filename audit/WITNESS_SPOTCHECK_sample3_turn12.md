# WITNESS SPOT-CHECK — SAMPLE 3: INTERPRETIVE TIER (turn 12)

Date: 2026-10-17T18:2xZ · Sample rule: 10 claims drawn from the **Speculative (13) and Community Consensus (23)** tiers, plus the two overdue claims. Question is different from samples 1–2: not "is the number right" but **"does the proposition assert more than its source does?"** A transcription error is visible; an over-reading is not, because the sentence is fluent and the source is plausible.

## Results

| Claim | Tier | Source read | Verdict |
| --- | --- | --- | --- |
| CLAIM-042 | Disputed | EV-167, EV-130, EV-213 | **PASS** — the iCloud toggle, the "not used by our games" wording and the sign-in path are all verbatim. Note: EV-130 itself already documents the split (older titles used iCloud/Play Games), so "leading resolution: legacy vs current" is slightly *more* cautious than the evidence warrants; it may be stated as a documented version split, not a hypothesis |
| CLAIM-049 | Comm. Consensus | EV-179 | **PASS** — weighted development, 10% weight = +1 OVR, +10 cap, GK 2.2-point/22-cap, gem tiers 25/75/225 · 90/240/400 · 15/40/150, +2 single-attribute application with discard/reshuffle, 0–30% facility discount: all present verbatim |
| CLAIM-052 | Comm. Consensus | EV-182 | **PASS** — triad (Players/Coaches/Physio), four coach categories, Physio "mechanics unspecified", stadium-capacity home bonus, per-match market refresh, market-check frequency claim, legendary rarity, gem agents, room-code friendlies: all present |
| CLAIM-062 | Comm. Consensus | EV-192, EV-196 | **PASS on transcription, FAIL on conflict status** — see F-1 |
| CLAIM-065 | Comm. Consensus | EV-193, EV-192, EV-162, EV-185 | **PASS** — Career → Season Points + Coins; Prize Ladder → DP; DLL → gems by weekly position; holiday Special Cup knockout; daily Scenario 50 coins: all present, and "partial separation" is honestly labelled |
| CLAIM-068 | Comm. Consensus | EV-196, EV-162, EV-195, EV-126, EV-197 | **PASS** — 400 SP activation (Career **or** DLL), ~1,095 coins + gems, payout at season end, Progress Bank = Season Points (officially confirmed by EV-162/197). The "(10-day season window)" phrasing is an interpretation (see N-2) |
| CLAIM-070 | Comm. Consensus | EV-196, EV-182, EV-203 | **PASS with drift** — see N-3 |
| CLAIM-101 | Comm. Consensus | GS-022 (derived summary) | **PASS at summary level** — eight substitutes stated; no raw megathread in the corpus, so the witness is one derived file (same limitation as D-03) |
| CLAIM-102 | Speculative | M-006 (derived summary) | **PASS at summary level** — 50–60 OVR, progress carry-over, "Academy Division" all present and correctly labelled single-source |
| CLAIM-110 | Comm. Consensus | EV-191, EV-188, EV-190 | **PASS** — club-progress scaling of market quality, specials outside rotation, drift of ratings/attributes/position/availability: verbatim; independence limit is already recorded in the claim's own challenge |

## Findings

### F-1 — CLAIM-062 is accurate but presented without the conflict that matters most (C-008)
The claim reproduces its source faithfully. What it did **not** carry is that the only official statement of promotion says something structurally different: an **XP ladder** (wins gain XP, losses lose XP, maximum XP promotes — EV-195, Confirmed). The community source says promotion runs on **Division Objectives** (wins + goals). Both could be true (objectives may award XP; or the two may govern different ladders), but nothing in the corpus says so.
**Action:** `logs/conflicts.md` **C-008** created with both texts quoted and a reopening test; challenge added to CLAIM-062 forbidding objective-efficiency coaching until the division screen is captured. Tier unchanged — the claim is honest about being community-sourced; the missing element was the conflict, not the confidence.
**Why this sample was worth running:** this is the first conflict found that changes a *strategy*, not a datum.

### N-2 — "(10-day season window)" over-reads a parenthesis
EV-196 reads "Progression Bank pays out AT SEASON END (10 days)". The claim renders this as a 10-day season window. A 10-day payout delay, a 10-day season, and "10 days" as a guide's shorthand are all compatible with the text. CLAIM-088 independently says "accumulates over 10-day season", so the reading has support elsewhere — but it is not in *this* record. Flagged, not fixed: the phrase stays because it is corroborated by a second claim, and the existing challenge already marks the season-length relationship as unclear.

### N-3 — CLAIM-070 adds two adjectives the source does not have
EV-196: 5-2-1-2 = "low block counter"; 4-1-2-3 = "all-out attack". The claim says "solid block + counter **vs strong opponents**" and "all-out **pressure**". Neither addition is in any cited record. Separately, EV-182/CLAIM-051 call 4-4-2 the "best basic" formation while this ranking puts 4-2-3-1 first — a genuine disagreement between two community publishers.
**Action:** challenge added recording both; content left intact because the additions are harmless *if* read as commentary, which is exactly why they must be labelled as such.

### N-4 — CLAIM-042 is more cautious than its own evidence
Not a defect, but an asymmetry worth recording: the claim calls the iCloud reconciliation "leading resolution", while EV-130 already states the version split as fact ("Older titles (DLS19): iCloud… only"). Understating confidence is a lesser error than overstating it, and the claim's caution protects against advising iCloud for a current build. No change.

## What the three samples together establish

| Sample | Focus | Claims | Corrections | Rate |
| --- | --- | --- | --- | --- |
| Turn 8 | transcription (numbers) | 10 | 2 | 20% |
| Turn 9 | all numeric claims | 62 | 4 | 6.5% |
| Turn 11 | mixed, first sample 2 | 10 | 1 | 10% |
| Turn 12 | interpretive / low-tier | 10 | 1 conflict + 2 wordings | 10–30% |

**Union of textually witnessed claims: 30 of 117 (26%).** Every sample has found something; the interpretive sample found the most consequential item so far. The remaining 87 claims are structurally verified only, and the next sample should keep targeting the low tiers, where an over-reading survives longest.

## Fixes applied this turn
- `logs/conflicts.md`: **C-008** (promotion mechanics).
- `kb/claims.jsonl`: challenges on CLAIM-062 and CLAIM-070; `next_due` repaired on CLAIM-003 (2026-10-21) and rolled forward on CLAIM-006 (2026-11-01); `last_checked_by` set on all four.
- No tier changed. No proposition deleted. No date bumped without a check — both date changes are derived from checks that had already happened, and both are documented in the claims themselves.
