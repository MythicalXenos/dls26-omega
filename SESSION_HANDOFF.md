# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:10Z (UTC), Turn 26. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — first-party support block, fifth pass complete.**
- **Git clean at open** (no drop). Tip at close: `4d13b53`.
- **Ledger: 439 entries · 368 visited · 386 leads** (reconciled this turn; stale strings removed). Retrieval **6 of 6**; tool calls **9 of 10**.
- **This turn's haul (all FIRST-PARTY):**
  - **24081168829330 Dream Point Boosts** — bought inside the ladder; apply to **career / dream draft / scenario / DLL only, not exhibition or friend**; **unusable once the ladder is complete or inactive**; **unused boosts carry over to the next ladder**; explicit live-service caveat. **The most actionable finding of the session for the user.**
  - **7916583518353 Season Points** — from wins; shown on the Main-Menu season leaderboard; unlock Season Pass tiers. **A separate economy from Dream Points** (recorded as a standing rule).
  - **360017166918 no video clips** — ad supply is provider-controlled; **no frequency guaranteed**; **LAT-enabled devices may get no ads**; troubleshooting list. Bounds the user's ad-income route as variable.
  - **360004034498 connection required** — online for most features (anti-exploit); **Exhibition playable offline**; server-side backup/restore.
  - **360003945937 manager** — My Club → Customise → Manager.
  - Monitoring: dlskiturl unchanged (**tenth** check).
- **Correction made this turn:** the Turn-26 log line initially recorded ledger figures written before the frontier dedupe ran (370/411); corrected in place to the machine values (368/386).
- **Next exact action (Turn 27, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl; do not re-fetch the Apple listing).
  3. **Continue the first-party block** (highest value first):
     - `https://support.ftgames.com/hc/en-us/articles/17143633310225-What-is-the-Season-Pass` (**second Season Pass article id — check for divergence from 4404070913169**)
     - `https://support.ftgames.com/hc/en-us/articles/360019064438-How-do-I-play-a-Friend-Match` (offline/friend distinction)
     - `https://support.ftgames.com/hc/en-us/articles/360004222118-Multiplayer-Troubleshooting` (dim 6)
     - `https://support.ftgames.com/hc/en-us/articles/214387685-How-do-I-backup-restore-transfer-my-save-data` (risk to the user's career save)
     - `https://support.ftgames.com/hc/en-us/articles/360008904718-Why-have-I-been-blocked-from-playing-DLS` (account risk)
  4. Keep harvesting related-article URLs — **the single most productive lead source in the sweep**.
  5. **Reconcile the frontier against the visited set every turn.**
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package (`research_queue/step5_ask_package.md`) prepared, **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; first-party official spine now **37+ support articles** plus Core Principles; full family census; first-party coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching text (conflict m); **first-party stat bible**; **first-party card-colour ladder**; first-party promotion/relegation XP rule; **first-party Dream Point Boost rules**; first-party update-disclosure policy; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates · DK+dlsinside = ONE family · cross-source OVR drift ≤ ±1 · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · reconcile the frontier before judging yield · **first-party support articles carry no version stamp — never promote their text to a DLS-26 claim without one** · **FTG does not pre-announce updates** · **black cards = the special tier** · **Season Points ≠ Dream Points** · **ad income is variable, never guaranteed** · **no backslash escapes in bash commands**.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered):** 7 items — ladder timer/DP; balances; spending stance; squad/division; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots. **Note: the DP-boost finding raises the value of item 1 (the ladder timer) — the carry-over rule means the user's decision depends entirely on the ladder end date.**
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts; (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward bux vs coach.
- **Known-unknowns:** Roles system mechanics; OVR thresholds for card tiers; all currency rates/amounts; the actual per-season formation count; **the ladder end date (device-only)**.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 26):** clean; the in-turn figure error was caught and corrected in the same turn rather than left standing.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `4d13b53`; handoff commit follows (with the log correction). PR #3 remains the single active PR. Next input expected: `>`.
