# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:12Z (UTC), Turn 27. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — first-party support block, sixth pass complete.**
- **Git clean at open** (no drop). Tip at close: `ebab726`.
- **Ledger: 445 entries · 373 visited · 391 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **This turn's haul (all FIRST-PARTY):**
  - **17143633310225 Season Pass** — FREE/PREMIUM tracks; **not a subscription** (repurchase each season, no auto-renew); **Progress Bank pays currency at season end based on Season Points**; **retroactive** (unlocked free tiers convert instantly); **late purchase removes time locks**; **a countdown on the Season Pass message box gives the season end for all users**; buying does **not** unlock Season VIP. **Conflict (p)**: Season Points from *completing* vs *winning* matches (two first-party articles).
  - **360004222118 Multiplayer Troubleshooting** — Wi-Fi or 3G/4G/5G only; **~2 MB per match**; latency-sensitive; **cloud-server netcode, lag-switch ineffective**; local same-platform Wi-Fi play; no Facebook invites.
  - **360019064438 Friend Match** — code-based private matches from the DLL button; A–Z/0–9/hyphen; collision risk; stats tracked in DLL.
  - **214387685 save data** — **Google Play Games and iCloud do NOT secure DLS saves**; only a manual in-game Sign in with Google / Apple link does; unlinked profiles are not guaranteed recoverable.
  - **360008904718 enforcement** — bans for modded APKs, hacks, bug exploitation; only store builds authorised; offensive names actionable; bans not lifted on request.
  - Monitoring: dlskiturl unchanged (**eleventh** check).
- **Step-5 ask package UPDATED this turn** (`research_queue/step5_ask_package.md`): item 1 now requests **both** in-game timers (Prize Ladder **and** Season Pass season countdown), and a new item **4b** asks whether the user's save is linked to Sign in with Google/Apple, plus which formations the grid actually offers.
- **Next exact action (Turn 28, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl; do not re-fetch the Apple listing).
  3. **Continue the first-party block** (highest value first):
     - `https://support.ftgames.com/hc/en-us/articles/4404070913169-What-is-the-Season-Pass` (**direct comparison against 17143633310225 — resolution of conflict (p) may sit here**)
     - `https://support.ftgames.com/hc/en-us/articles/4413273241873-How-is-save-data-stored-and-transferred-in-DLS` (DLS-specific save detail)
     - `https://support.ftgames.com/hc/en-us/articles/23108987826962-What-is-the-Prize-Ladder` (verify against the boost article)
     - `https://support.ftgames.com/hc/en-us/articles/30839289076626-What-are-Clans`
     - `https://support.ftgames.com/hc/en-us/articles/360018360418-How-does-game-difficulty-work`
  4. Keep harvesting related-article URLs — **the single most productive lead source in the sweep**.
  5. **Reconcile the frontier against the visited set every turn.**
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; first-party official spine now **42+ support articles** plus Core Principles; full family census; first-party coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching text; **first-party stat bible**; **first-party card-colour ladder**; promotion/relegation XP rule; **Dream Point Boost rules**; **Season Pass economics**; update-disclosure policy; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates · DK+dlsinside = ONE family · cross-source OVR drift ≤ ±1 · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · reconcile the frontier before judging yield · **first-party support articles carry no version stamp** · **FTG does not pre-announce updates** · **black cards = the special tier** · **Season Points ≠ Dream Points** · **ad income is variable, never guaranteed** · **two separate in-game timers, both device-only** · **no backslash escapes in bash commands**.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered, updated this turn):** items — both timers + DP/tier; balances; spending stance; squad/division (incl. which formations are actually offered); **4b save-link check**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts; (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward bux vs coach; **(p) Season Points: completing vs winning matches**.
- **Known-unknowns:** Roles system mechanics; OVR thresholds for card tiers; all currency rates/amounts; per-season formation count; **both in-game end dates (device-only)**.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 27):** clean — conflict (p) recorded not averaged; historic comments dated and excluded; netcode claims attributed to FTG's own description; the two timers recorded as device-only rather than as dates.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `ebab726`; handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
