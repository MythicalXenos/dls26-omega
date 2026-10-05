# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:47Z (UTC), Turn 33. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — the DLS FAQ corpus is nearly closed (48 of 52 read).**
- **Git clean at open** (no drop). Tip at close: `2f9b428`.
- **Ledger (machine figures): 481 entries · 396 visited · 407 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **The substantive find:** **squad size is a facility upgrade, not a constant.** Squad slots come from upgrading the **accommodation** facility on the **Stadiums & Facilities** screen — "for each level this is increased, you can add more players". **Consequence:** the user's rotation plan (secondary XI) has a **cost dimension**; a second XI is bought with facility levels. Per-level slots **and** upgrade costs remain unknown.
- **Facilities defined but not enumerated:** "different buildings belonging to your club that grant unique bonuses" helping career progression — that is the whole article. Individual bonuses stay a known-unknown; **do not fill them from marketing copy**.
- **Kit divergence clarified, not resolved:** *editing* kits is My Club (home + GK); *selecting* on match day is tapping the player models on the pre-match screen to cycle home/away. Whether an away kit is separately editable is still open.
- **IAP:** Shop opens by tapping the coin or gem tally on any screen; no prices in first-party text — **all pricing in this corpus remains third-party**.
- **Team stats:** My Profile (top-right team/manager name) → **Records** for lifetime; **Career** → competition for current.
- **DLS FAQ: 4 titles unread** — `360003945557` (can't connect), `19336294718098` (haptic feedback), `214385405` (saved replays), `213851429` (nationality).
- **Next exact action (Turn 34, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl).
  3. **Close out the last four DLS FAQ titles** (above).
  4. Then **enumerate the *General FAQs* section (21 articles)** using the `?page=N` approach that worked on the DLS section — its section id is **not yet known**, so find it from a related-articles block or a search rather than re-fetching the category index `201738105`.
  5. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; **48 of 52 DLS first-party FAQ articles read (all titles known)**; Core Principles; storefront version chain; family census; coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching; **stat bible**; **card-colour ladder**; promotion/relegation XP rule; **Dream Point Boost rules**; **Season Pass economics (two diverging articles)**; **Prize Ladder reward pool**; **clan rules**; **scoped difficulty denial**; **account-recovery routes**; **customisation map**; **live-service value-change policy**; **Reset Profile irreversible rule**; **facilities/squad-cap mechanism**; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates **and point-in-time readings — published values move, sometimes temporarily** · DK+dlsinside = ONE family · ±1 drift, cause open · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · **support.ftgames.com can return HTTP 200 behind a sign-in wall** · reconcile the frontier before judging yield · **never infer completeness from an unreconciled list — check whether a listing paginates** · first-party articles carry no version stamp · FTG does not pre-announce updates · black cards = the special tier · Season Points ≠ Dream Points · ad income is variable · two device-only timers · **squad size is a spendable progression target** · FTG's own text contradicts itself in several places — record both · **Reset Profile destroys purchases; never suggest it without a warning** · no backslash escapes in bash commands · log figures from script output.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered; updated Turns 27 and 29):** both timers + DP/tier; balances; spending stance; squad/division and which formations the grid offers; **4b save-link check**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots. **Turn 33 adds a natural item: the user's current accommodation level and squad size**, since rotation advice depends on it.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts (cause open); (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward; (p) Season Points completing vs winning; (q) Progress Bank basis. Minor divergences: channel lists; **kit editing vs selection (clarified, still open on away-kit editing)**.
- **Known-unknowns:** Roles mechanics; OVR thresholds for card tiers; **all prices**; per-season formation count; both in-game end dates; device limit for code transfers; **per-level squad slots and facility upgrade costs**; **individual facility bonuses**; auth-walled contents; the 4 unread DLS titles; **General FAQs enumeration**.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 33):** clean; squad expansion reported with its missing numbers stated as missing, the kit finding labelled a clarification rather than a resolution, and the facility-bonus gap refused rather than filled from marketing.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `2f9b428`; handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
