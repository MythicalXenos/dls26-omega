# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:18Z (UTC), Turn 29. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — first-party support block, eighth pass complete.**
- **Git clean at open** (no drop). Tip at close: `97bfd99`.
- **Ledger (machine figures): 457 entries · 378 visited · 392 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **This turn's haul (all FIRST-PARTY unless noted):**
  - **9804887423121 Facebook Login removed** — dead route; **Facebook-stored profiles can no longer be recovered**; use Sign in with Apple / Google.
  - **360004080497 customise kit/logo** — full map: Players / Manager / Kit tabs; logo templates auto-render the team name; **Custom Logo section must be unlocked**; **512×512 max** URL import; kit png needs a specific layout; **shading/creases applied at run-time**; Reset/Delete paths.
  - **360020938198 emojis** — 6 default, 6 equippable, extras earned or purchased; **Settings → Game → Multiplayer Chat OFF** disables them entirely.
  - **360021064298 opponent visibility** — **imported kits/logos are not transferred in multiplayer** (local-only).
  - **360015150438** — **NOT READ: HTTP 200 with a Zendesk sign-in wall.** New failure class; do not retry via the fetch tool.
  - Monitoring: dlskiturl unchanged (**thirteenth** check).
- **Step-5 package updated:** item 4b now states the Facebook-unrecoverable rule and gives the exact menu route (Options → Advanced → Link Profile).
- **Next exact action (Turn 30, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl; do not re-fetch the Apple listing).
  3. **Continue the first-party block** (highest value first):
     - `https://support.ftgames.com/hc/en-us/articles/7916959134737-How-do-I-change-my-kit` (new lead; kit vs kit-import distinction)
     - `https://support.ftgames.com/hc/en-us/articles/214385685-Is-my-device-compatible-with-the-app`
     - `https://support.ftgames.com/hc/en-us/articles/14369944135058-How-do-I-hide-the-text-on-the-control-buttons` (controls/UI)
     - `https://support.ftgames.com/hc/en-us/articles/360005680437-How-can-I-reduce-my-mobile-data-usage`
     - `https://support.ftgames.com/hc/en-us/articles/37082887837202-How-do-I-find-my-User-ID`
  4. Keep harvesting related-article URLs — **the single most productive lead source in the sweep**.
  5. **Reconcile the frontier every turn; write log figures only from script output.**
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; first-party official spine now **51+ support articles** plus Core Principles; full family census; first-party coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching; **stat bible**; **card-colour ladder**; promotion/relegation XP rule; **Dream Point Boost rules**; **Season Pass economics (two diverging articles)**; **Prize Ladder reward pool**; **clan rules**; **scoped difficulty denial**; **account-recovery routes**; **customisation map**; update-disclosure policy; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates · DK+dlsinside = ONE family · cross-source OVR drift ≤ ±1 · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · **support.ftgames.com can return HTTP 200 behind a Zendesk sign-in wall — a 200 is not proof of a read** · reconcile the frontier before judging yield · **first-party articles carry no version stamp** · **FTG does not pre-announce updates** · **black cards = the special tier** · **Season Points ≠ Dream Points** · **ad income is variable** · **two device-only timers** · **FTG's own text contradicts itself in at least five places — record both, never harmonise** · **no backslash escapes in bash commands** · **log figures come from script output**.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered, updated at Turns 27 and 29):** both in-game timers + DP/tier; balances; spending stance; squad/division and which formations the grid offers; **4b save-link check with exact menu path and the Facebook-unrecoverable rule**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts; (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward; (p) Season Points completing vs winning; (q) Progress Bank basis.
- **Known-unknowns:** Roles system mechanics; OVR thresholds for card tiers; all currency rates/amounts; per-season formation count; both in-game end dates; the device limit for code transfers; contents of the auth-walled articles.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 29):** clean, and its central act was a negative — the auth-walled page is recorded as blocked rather than read, with status and payload kept together.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `97bfd99`; handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
