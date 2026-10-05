# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:22Z (UTC), Turn 30. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — and the first-party block is demonstrably NOT exhausted.**
- **Git clean at open** (no drop). Tip at close: `7566d12`.
- **Ledger (machine figures): 463 entries · 383 visited · 398 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **The turn's main result is a self-correction:** the **FAQ category index** gives the site's own counts — **Core Principles 1 · Parents' Guide 8 · General FAQs 21 · Dream League Soccer FAQs 52** · Score! Hero 24 · UCS 43 · Score! Match 43. Our ~30-URL enumeration was therefore **not** "the complete official spine"; that claim is **retracted** in the KB, the gate, the saturation assessment and this handoff. Roughly **22 DLS FAQ articles remain unread**.
- **Other captures:** kit route = My Club → kit section, editing **home and GK** kit (diverges from the home/away description — logged as a gap) · in-match buttons read **Low Kick / Hard Kick / Lofted Kick**, hide via **Game Settings → Display → Descriptive Button Text OFF** · Android **3,000+ compatible devices** · Wi-Fi strongly recommended.
- **New high-value leads from the index:** `360001369698 Some game values and content have changed. Is this a bug?` (may be the first-party explanation for rating/stat drift — the mechanism behind our ±1 conflicts) · `360009168377 Our Commitment to Fair Gaming` (Zendesk copy; check against ftgames.com/core-principles) · `360000191445 Other Sites Offering In-App products` · `213853309 What languages` · `213689249 When is the next app update being released`.
- **Next exact action (Turn 31, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl).
  3. **Enumerate the remaining first-party corpus** — `https://support.ftgames.com/hc/en-us/sections/203117809-Dream-League-Soccer-FAQs` (**all 52 DLS articles; this is the only way to know what is unread**).
  4. Then read by value: `360001369698` (values changed — drift), `360009168377` (fair gaming), `213689249` (update cadence), `213853309` (languages), `360000191445` (other IAP sites).
  5. **Reconcile the frontier every turn; write log figures only from script output.**
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; **~30 of 52 DLS first-party FAQ articles read** plus Core Principles, the storefront version chain and the full family census; first-party coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching; **stat bible**; **card-colour ladder**; promotion/relegation XP rule; **Dream Point Boost rules**; **Season Pass economics (two diverging articles)**; **Prize Ladder reward pool**; **clan rules**; **scoped difficulty denial**; **account-recovery routes**; **customisation map**; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates · DK+dlsinside = ONE family · cross-source OVR drift ≤ ±1 · open the card before trusting an index row · match by id sets, never list length · shell curl unusable · Reddit/TikTok fetch-blocked (403) · **support.ftgames.com can return HTTP 200 behind a Zendesk sign-in wall — a 200 is not proof of a read** · reconcile the frontier before judging yield · **never infer completeness from an unreconciled list (this has now bitten twice: Turn 20 saturation, Turn 30 spine)** · first-party articles carry no version stamp · FTG does not pre-announce updates · black cards = the special tier · Season Points ≠ Dream Points · ad income is variable · two device-only timers · FTG's own text contradicts itself in at least five places — record both, never harmonise · no backslash escapes in bash commands · log figures come from script output.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered; updated at Turns 27 and 29):** both in-game timers + DP/tier; balances; spending stance; squad/division and which formations the grid offers; **4b save-link check with menu path and Facebook-unrecoverable rule**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots.
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts; (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; (n) "bux" vs "coins"; (o) sale reward; (p) Season Points completing vs winning; (q) Progress Bank basis. **New minor gap:** home/GK kit vs home/away kit descriptions.
- **Known-unknowns:** Roles mechanics; OVR thresholds for card tiers; currency rates; per-season formation count; both in-game end dates; device limit for code transfers; contents of auth-walled articles; **the ~22 unread DLS FAQ articles**.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 30):** the turn's substance is a retraction made in-turn, in all three places the claim lived (KB, gate, saturation assessment), with the corrected count recorded.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `7566d12`; handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
