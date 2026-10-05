# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:45Z (UTC), Turn 32. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — the DLS first-party corpus is now fully enumerated.**
- **Git clean at open** (no drop). Tip at close: `5f09d73`.
- **Ledger (machine figures): 475 entries · 391 visited · 407 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **Coverage discrepancy CLOSED:** the DLS FAQ section **paginates** — page 1 rendered 30 titles, page 2 rendered 22, **total 52**, matching the category index. **All 52 titles are now known. Nine remain unread:**
  `360003945917 What are facilities` · `360003945677 How can I expand my squad` · `214229005 Can I make an in-app purchase` · `360003945557 I can't connect to the game` · `19336294718098 What is Haptic Feedback` · `214385385 Home/Away kits before a match` · `214385405 Watch saved replays` · `213851469 View my team's stats` · `213851429 Change my nationality`.
- **Safety rule established (irreversible-action territory):** **Reset Profile** (skull-and-crossbones, Settings → Advanced) **destroys all progress including in-app purchases**, is **unrecoverable**, and is **limited to one per 30 days**. Menu hazard: it sits in the same Advanced menu as Link Profile and Manage Devices.
- **Other captures:** User ID path = Options → Advanced → System Info (i) → Copy Info; DLS19 → DLS25 is **No** (standalone, purchases don't transfer); update-troubleshooting steps for iOS/Android (also the publisher's own fix for a store listing that appears not to show the current version). Monitoring: dlskiturl unchanged (**sixteenth** check).
- **Next exact action (Turn 33, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl).
  3. **Read the two substantive unread systems first:** `360003945917 What are facilities` and `360003945677 How can I expand my squad` — both are core progression systems we have only seen in storefront marketing copy.
  4. Then, as budget allows: `214229005 Can I make an in-app purchase` (relevant to the user's spending-stance ask), `213851469 View my team's stats`, `214385385 Home/Away kits`, `19336294718098 Haptic Feedback`.
  5. **Check whether the *General FAQs* section (21 articles) also paginates** — we have read only a handful of its titles; enumerate it with the same `?page=N` approach before assuming coverage.
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; **43 of 52 DLS first-party FAQ articles read** (all 52 titles known), plus Core Principles, the storefront version chain and the full family census; first-party coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching; **stat bible**; **card-colour ladder**; promotion/relegation XP rule; **Dream Point Boost rules**; **Season Pass economics (two diverging articles)**; **Prize Ladder reward pool**; **clan rules**; **scoped difficulty denial**; **account-recovery routes**; **customisation map**; **live-service value-change policy**; **Reset Profile irreversible rule**; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates **and point-in-time readings — published values move, sometimes temporarily** · DK+dlsinside = ONE family · ±1 drift, cause open · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · **support.ftgames.com can return HTTP 200 behind a sign-in wall** · reconcile the frontier before judging yield · **never infer completeness from an unreconciled list (bitten twice) — check whether a listing paginates before concluding** · first-party articles carry no version stamp · FTG does not pre-announce updates · black cards = the special tier · Season Points ≠ Dream Points · ad income is variable · two device-only timers · FTG's own text contradicts itself in several places — record both · **Reset Profile destroys purchases; never suggest it without a warning** · no backslash escapes in bash commands · log figures from script output.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered; updated Turns 27 and 29):** both timers + DP/tier; balances; spending stance; squad/division and which formations the grid offers; **4b save-link check**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts (cause open); (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward; (p) Season Points completing vs winning; (q) Progress Bank basis. Minor divergences: home/GK vs home/away kit; official channel lists.
- **Known-unknowns:** Roles mechanics; OVR thresholds for card tiers; currency rates; per-season formation count; both in-game end dates; device limit for code transfers; auth-walled contents; **the 9 unread DLS titles**; **whether General FAQs paginates**.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 32):** clean; the pagination finding closes a previously-flagged discrepancy instead of papering over it, and the Reset Profile consequences are quoted from FTG's own IMPORTANT warning.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `5f09d73`; handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
