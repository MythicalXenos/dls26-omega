# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:15Z (UTC), Turn 28. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — first-party support block, seventh pass complete.**
- **Git clean at open** (no drop). Tip at close: `fdf590d`.
- **Ledger (machine figures): 451 entries · 373 visited · 391 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **This turn's haul (all FIRST-PARTY):**
  - **4404070913169 Season Pass (second, older, v12200+)** — **conflict (q)**: Progress Bank pays on **DLL XP** here vs **Season Points** in 17143633310225; only this article says purchase **removes all tier locks**; tier named "SEASON PASS" not "PREMIUM"; **Season Points from completing matches, amount varying by game mode** (leans conflict (p) two-surfaces-to-one, without closing it).
  - **4413273241873 save data in DLS** — one account per player; **Options (gear, top-left) → Advanced → Manage Devices / Link Profile**; Google = Android only, Apple = iOS only; **code transfer for cross-platform**, unusable on the generating device; **signing out silently unlinks the profile**.
  - **23108987826962 Prize Ladder** — rewards are **coins, gems, coaches, dream point boosts, special players and more**; Dream Points given in matches. **The ladder grants coaches — loop closed with the coaching and selling rules.**
  - **30839289076626 Clans** — one clan at a time; one leader; **entry requirements hide clans from search but invite codes bypass them**; **clan points from matches, challenges and season passes**.
  - **360018360418 difficulty** — single-player difficulty **scales with division movement**; DLS25 added a Medium/Hard base setting; **DLL: no bots, no difficulty control, no AI manipulation, no outcome influence** — an explicit denial **scoped to multiplayer only**.
  - Monitoring: dlskiturl unchanged (**twelfth** check).
- **Correction this turn:** the Turn-28 log line was written before the reconciliation script reported; corrected in place to the machine figures (373/391, not 379/393).
- **Next exact action (Turn 29, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl; do not re-fetch the Apple listing).
  3. **Continue the first-party block** (highest value first):
     - `https://support.ftgames.com/hc/en-us/articles/9804887423121-Removal-of-Facebook-Login-from-DLS` (account/link history)
     - `https://support.ftgames.com/hc/en-us/articles/360004080497-How-do-I-customise-my-kit-logo`
     - `https://support.ftgames.com/hc/en-us/articles/360020938198-How-do-I-change-my-emojis-in-Dream-League-Live`
     - `https://support.ftgames.com/hc/en-us/articles/360021064298-Can-my-opponent-see-my-custom-kit-and-logo-in-Dream-League-Live`
     - `https://support.ftgames.com/hc/en-us/articles/360015150438-Can-I-use-my-existing-DLS24-profile-in-DLS25` (carry-over rules)
  4. Keep harvesting related-article URLs — **the single most productive lead source in the sweep**.
  5. **Reconcile the frontier against the visited set every turn, and write log figures only from the script output, never before it.**
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; first-party official spine now **47+ support articles** plus Core Principles; full family census; first-party coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching; **first-party stat bible**; **card-colour ladder**; promotion/relegation XP rule; **Dream Point Boost rules**; **Season Pass economics (two articles, diverging)**; **Prize Ladder reward pool**; **clan rules**; **scoped difficulty denial**; update-disclosure policy; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates · DK+dlsinside = ONE family · cross-source OVR drift ≤ ±1 · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · reconcile the frontier before judging yield · **first-party support articles carry no version stamp** · **FTG does not pre-announce updates** · **black cards = the special tier** · **Season Points ≠ Dream Points** · **ad income is variable** · **two device-only timers** · **FTG's own text now contradicts itself in at least five places — record both, never harmonise** · **no backslash escapes in bash commands** · **log figures come from script output, not from memory**.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered, updated at Turn 27):** both in-game timers + DP/tier; balances; spending stance; squad/division and which formations the grid offers; **4b save-link check (Options → Advanced)**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts; (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward; (p) Season Points: completing (2 surfaces) vs winning (1 surface); **(q) Progress Bank basis: DLL XP vs Season Points**.
- **Known-unknowns:** Roles system mechanics; OVR thresholds for card tiers; all currency rates/amounts; per-season formation count; both in-game end dates; the device limit for code transfers.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 28):** clean — conflict (q) recorded, conflict (p) recorded as a lean rather than a resolution, the scripting denial scoped to multiplayer with the allegation left open for career play, and the log figure error corrected in-turn.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `fdf590d`; handoff commit follows (with the log correction). PR #3 remains the single active PR. Next input expected: `>`.
