# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:05Z (UTC), Turn 25. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — first-party support block, fourth pass complete.**
- **Git clean at open** (no drop this turn). Tip at close: `c6ee2fb`.
- **Ledger: 433 entries · 364 visited · 405 leads.** Retrieval **6 of 6**; tool calls **11 of 10** (one lost to a shell-quoting failure, now documented).
- **This turn's haul (all FIRST-PARTY):**
  - **7917587319313 formations** — Squad → formation grid; **formations are limited by season** (example given: 2 available). **User-relevant:** 3-2-3-2 / 3-1-4-2 may not be selectable in a given season.
  - **7917423348497 promotion** — rank is an **XP meter that falls on defeats**; max XP promotes, XP loss relegates.
  - **360000842697 "not realistic"** — FTG's fairness position: luck is deliberate, rules identical for all players, game is "fair"; **recorded as a publisher position, not evidence on the rubber-banding allegation**.
  - **214385345 team name** — Customise button → Team Name.
  - **360004718318 likeness** — one-sentence body; **staff comment reply repeats the licensing cause** (second first-party surface). Comments are 5–6 years old, flagged non-current.
  - Monitoring: dlskiturl unchanged (**ninth** check).
- **Operational note (new, important):** a ledger script failed because **backslash escapes in bash commands are consumed before the shell sees them**. Rule added to the log: **never use backslash escapes in bash commands.**
- **Next exact action (Turn 26, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 has hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl; do not re-fetch the Apple listing).
  3. **Continue the first-party block** (highest value first):
     - `https://support.ftgames.com/hc/en-us/articles/7916583518353-What-are-Season-Points` (**likely a core progression currency/score - may illuminate the DP/ladder question**)
     - `https://support.ftgames.com/hc/en-us/articles/360018360418-How-does-game-difficulty-work` (if still unread; check the ledger first)
     - `https://support.ftgames.com/hc/en-us/articles/23108987826962-What-is-the-Prize-Ladder` (recheck status in the ledger first)
     - `https://support.ftgames.com/hc/en-us/articles/4404070913169-What-is-the-Season-Pass`
     - `https://support.ftgames.com/hc/en-us/articles/360004080497-How-do-I-customise-my-kit-logo`
  4. Keep harvesting related-article URLs — **the single most productive lead source in the sweep**.
  5. **Reconcile the frontier against the visited set every turn.**
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package (`research_queue/step5_ask_package.md`) prepared, **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; first-party official spine now **32+ support articles** plus Core Principles; full family census; first-party coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching text (conflict m); **first-party stat bible**; **first-party card-colour ladder**; first-party promotion/relegation rule; first-party update-disclosure policy; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates · DK+dlsinside = ONE family · cross-source OVR drift ≤ ±1 · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · reconcile the frontier before judging yield · **first-party support articles carry no version stamp — never promote their text to a DLS-26 claim without one** · **FTG does not pre-announce updates** · **black cards = the special tier** · **no backslash escapes in bash commands**.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered):** 7 items — ladder timer/DP; balances; spending stance; squad/division; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts; (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward bux vs coach.
- **Known-unknowns:** Roles system mechanics; OVR thresholds for card tiers; all currency rates/amounts; Season Points definition; the actual per-season formation count.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6 on 2026-10-04/05)** open; 0009, 0012 resolved.
- **Bluff check (Turn 25):** clean after the rerun — the fairness statement is framed as a publisher position, the formation "2" is flagged as an example, the likeness comments are flagged as historic, and the failed script was rerun rather than worked around so no ledger entry is missing.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commits+pushes `abd6abc` (KB/gate/log) and `c6ee2fb` (ledger entries); handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
