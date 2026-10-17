# STEP 2/3 PREPARATION — REVIEW AGAINST THE CURRENT CAPABILITY INVENTORY
Reviewed 2026-10-17T20:24Z (session sess-20261017-001, turn 8). Subject: the inherited `docs/continuity/a7e23a6b/docs/step2_3_preparation/` set, which was written in a previous session and pre-dates this sandbox. This is Step-1 work: it tests whether Steps 2 and 3 are executable at all before the state machine reaches them.

## Verdict in one line
The inherited perimeter document is **substantively correct about what is prohibited**, and that correctness creates a direct conflict with the prompt's own Step 2 definition. The conflict is recorded, not resolved by me.

## 1. The conflict that matters
- **The prompt's Step 2** (HARD STATE BOUNDARY RULE) is described as "Decompilation and static extraction of APK assets, stat tables, and formation data".
- **The verified EULA and sanction policy** (CLAIM-043, Confirmed; CLAIM-017 / CLAIM-075, Confirmed) prohibit reverse engineering, decompilation and derivative use, and FTG bans accounts for using unauthorised builds or exploiting the game. Decompiling the APK is therefore a ban-risk action taken against the user's own account.
- **This is a precedence collision**, and the ladder resolves it without me choosing: rung 2 (a rule protecting against irreversible or consequential loss) beats a rule that would produce better work. Compiling a richer dataset from a decompiled APK is "better work"; a ban is a consequential loss to the user's account. The loss-protecting rule wins.
- **What I have done:** not decompiled anything, not downloaded an APK, not searched for one. Step 2 remains **unentered**. The conflict is logged as OBS-013, and a PROPOSED prompt amendment is written in the changelog (marked PROPOSED, no version, not adopted) so the user can decide whether Step 2 should be redefined as *legal static analysis* (store metadata, published assets, permitted APIs) rather than decompilation.
- **What I have not done:** silently redefined Step 2. The state machine still treats Step 2 as the prompt defines it; I simply cannot execute the banned part, and will not, until the user directs otherwise.

## 2. Corrections needed in the inherited prep docs for this environment
| Item in the prep docs | Inherited assumption | This environment | Correction |
| --- | --- | --- | --- |
| "fetch-capable when tools return" | that page fetching returns | every non-allowlisted host is TLS-blocked (S-055…058) | All fetch-dependent checklist items are ACCESS_BOUNDARY here, not scheduled work |
| Step 2 allowed surfaces | store listings, screenshots, comments | none reachable | unchanged in principle, unreachable in practice |
| Step 3 device work | user-driven captures (correct) | no device, no ADB | still correct: captures are user-supplied; the agent never drives the device |
| Decompilation ban | stated | stated | **correct and now load-bearing** — it is the reason Step 2 is not executed |
| Comment-thread backlog | "cursor backlog" | blocked | stays owed |

## 3. What remains genuinely executable without a device or a permitted route
- Maintaining this repo's structure, the claim authority, the coverage accounting and the audit trail (what this session has been doing).
- Drafting the epoch contract skeleton (done this turn, not sealed).
- Reviewing imported material for internal consistency and provenance (this review, and the spot-check).
- Preparing the *user-facing* observation checklist — the in-client questions that only the user can answer — so that when the bootstrap reaches first contact, the ask is batched and specific rather than vague.

## 4. What remains blocked, with the exact blocker named
| Work | Blocker | Reopening predicate |
| --- | --- | --- |
| Any external research fetch | sandbox allowlist (TLS-blocked hosts) | allowlist change, permitted route, or user-supplied captures in `raw_game_data/` |
| Step 2 static analysis | EULA/ban policy (and, separately, no java/APK tooling) | **user direction** on the prompt conflict, plus permitted, non-banned analysis surfaces |
| Step 3 device pipeline | no device, no ADB | user-supplied captures on their own device |
| Controls/settings inventory | in-game observation only | user screenshots or in-client answers |
| Exact economy values, XP thresholds | in-game observation only | user transcriptions or screenshots |

## 5. Recommendation
Do not attempt to satisfy Step 2 by the route the prompt names. Record it as user-decision-blocked (OBS-013) and proceed on the assumption that Step 2 will be redefined as legal static analysis. This is a proposal, not an action: the user's word settles it.
