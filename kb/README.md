# KNOWLEDGE BASE — index and rules

**Authority:** PROMPT.md §8 KNOWLEDGE BASE. The KB is the *current state* of knowledge by topic. The main operational log is the history of how it got there. Where they disagree, the later valid evidence wins and the change is a revision (logged in `logs/revision_register.md`).

## Files

| File | Holds |
|---|---|
| `user_profile.md` | Everything about the user: club/game state (last-known, timestamped), playstyle model, preferences & decisions, spending profile, understanding tracker, skill tracker, user-stated facts |
| `topics/*.md` | One file per research topic. No predetermined shape — the KB grows wherever research leads |
| `disputed_claims.md` | Authoritative list of open Disputed claims (confidence-tier sense). The handoff points here rather than enumerating |
| `deception_register.md` | Sources/domains entered by the deception screen. Never cleared |
| `irreversible_action_list.md` | Game knowledge: every irreversible or consequential action type research has identified |
| `watchlist.md` | Monitored players, per the Watchlist rule |
| `volatility_model.md` | Volatility tiers, per-claim dimensions, impact weighting, observed FTG change patterns |
| `gaps.md` | Open gaps ("no evidence either way") and closed gaps ("evidence confirms non-existence") — two distinct states |
| `milestone_tracker.md` | Targets, distances, resource requirements |

## Claim record format

Defined in `SCHEMA.md` §2.2 and mandatory. Minimum fields: source attribution, first-publication dates where they bore on independence, last-verified date and by what, confidence tier, volatility tier (named with its system), datamining flag where applicable, deception-screen outcome where an incentive was found, and the **checkable origin** the claim rests on — or an explicit "NONE FOUND" with the tier capped accordingly.

## Tier legends (always named with their system — TIER RULE, PROMPT.md §3)

- **Confidence:** Confirmed / High Confidence / Community Consensus / Speculative / Disputed — gates in PROMPT.md §3 Mechanism 5.
- **Volatility:** volatility-Critical / volatility-High / volatility-Low / volatility-Frozen — PROMPT.md §9.
- **Queue priority:** queue-Critical / queue-High / queue-Medium / queue-Low — PROMPT.md §3 Mechanism 4.
- **Risk:** risk Tier 1–4 — PROMPT.md §6.
- **Special card:** card Tier 1–4 — PROMPT.md §8 SPECIAL CARD TRACKING.

## Standing rules

- Every claim carries a volatility tier from the moment it enters. Unassignable → volatility-Critical until observation says otherwise.
- Nothing is deleted. Superseded knowledge moves to `logs/revision_register.md` and stays in snapshots.
- Prompt shorthand (DLL, OVR, GK, XI, prize ladder, special card, base OVR, rotation, coaching state, reset cycles, breakpoints, matchup matrix, gameplans, touch patterns, facilities, ceiling, bonus development, division, season points) is **not** game terminology until resolved in `topics/terminology_and_abbreviations.md`.
- Zero ungrounded claims: no game fact enters the KB without a traceable tool-output origin (`S-NNNN` in `logs/sources_visited.json`) or an explicit `user-stated` / `inference` evidence class.
