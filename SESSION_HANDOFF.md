# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:50Z (UTC), Turn 34. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — the DLS FAQ section is now closed out (52 of 52).**
- **Git clean at open** (no drop). Tip at close: `da4b423`.
- **Ledger (machine figures): 487 entries · 400 visited · 409 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **Milestone, stated with its limits:** every one of the **52 DLS FAQ articles has been enumerated and read**. **This is NOT an exhaustion declaration** — General FAQs (21), Parents' Guide (8), the auth-walled articles and the blocked routes are all still open, and this is only one section of the help centre.
- **Captures:** offline **exhibition** play is now corroborated by a **second** first-party article (mobile data or Wi-Fi both acceptable; a *stable* connection is required for multiplayer). **Haptic Feedback** toggles at Options → **Audio** → Haptic Feedback (not Controls/Display). **Saved replays**: My Profile → **Highlights**. **Nationality**: My Profile → the flag near your manager (no stated limit — absence of a limit is not evidence of none).
- **The My Profile menu is now fully mapped:** Records (lifetime stats), Highlights (replays), nationality flag.
- **Two open items raised:** (1) the help-centre root renders **no General FAQs section id**, so that section's enumeration stays blocked; (2) a fifth title section appeared — **Ultimate Draft Soccer (7900693036561)** — which is either a rename of **UCS** or a distinct title. **Unresolved; do not assume either.**
- **Highest-value remaining lead:** `360004222118 Multiplayer Troubleshooting` — the best remaining first-party route into netcode, an open gap.
- **Next exact action (Turn 35, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl).
  3. **`360004222118 Multiplayer Troubleshooting`** — read it; it is the strongest netcode lead we have.
  4. **Resolve the Ultimate Draft Soccer question** by fetching its section page `7900693036561` (that is a different game's section, but it settles a census claim in our own corpus).
  5. **Attempt General FAQs enumeration again** — try `https://support.ftgames.com/hc/en-us/categories/201738105?page=2` or a related-articles block; if it stays blocked, record it as blocked rather than guessing.
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; **all 52 DLS first-party FAQ articles read**; Core Principles; storefront version chain; family census (**one open question**); coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching; **stat bible**; **card-colour ladder**; promotion/relegation XP rule; **Dream Point Boost rules**; **Season Pass economics (two diverging articles)**; **Prize Ladder reward pool**; **clan rules**; **scoped difficulty denial**; **account-recovery routes**; **customisation map**; **live-service value-change policy**; **Reset Profile irreversible rule**; **facilities/squad-cap mechanism**; **My Profile menu map**; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates **and point-in-time readings — published values move, sometimes temporarily** · DK+dlsinside = ONE family · ±1 drift, cause open · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · **support.ftgames.com can return HTTP 200 behind a sign-in wall** · reconcile the frontier before judging yield · **never infer completeness from an unreconciled list — check whether a listing paginates** · first-party articles carry no version stamp · FTG does not pre-announce updates · black cards = the special tier · Season Points ≠ Dream Points · ad income is variable · two device-only timers · **squad size is a spendable progression target** · FTG's own text contradicts itself in several places — record both · **Reset Profile destroys purchases; never suggest it without a warning** · no backslash escapes in bash commands · log figures from script output.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered; updated Turns 27 and 29):** both timers + DP/tier; balances; spending stance; squad/division and which formations the grid offers; **4b save-link check**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots. **Two natural additions:** the user's **accommodation level and current squad size** (rotation advice depends on it) and, now, their **connection type**, since multiplayer needs a stable one.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts (cause open); (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward; (p) Season Points completing vs winning; (q) Progress Bank basis. Minor divergences: channel lists; kit editing vs selection.
- **Known-unknowns:** Roles mechanics; OVR thresholds for card tiers; **all prices**; per-season formation count; both in-game end dates; device limit for code transfers; **per-level squad slots and facility costs**; **individual facility bonuses**; **netcode behaviour**; auth-walled contents; **General FAQs enumeration**; **UCS vs Ultimate Draft Soccer**.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 34):** clean; the 52/52 milestone carries its limits in the same breath, the help-centre root is treated as a partial render, and the Ultimate Draft Soccer question is left open rather than mapped onto UCS.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `da4b423`; handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
