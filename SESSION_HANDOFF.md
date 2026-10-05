# SESSION HANDOFF — session `arena/01a1022d-dls26-omega`

**Updated:** 2026-10-05T10:55Z (UTC), Turn 35. Branch authoritative for file state; this file for intent.
**Last session ended:** 2026-10-02T11:48Z (prior session `arena/01a0f962`).

## Active state and exact resumption point

- **`STATE_1_RESEARCH_SWEEP` ACTIVE — Turn 35 produced a netcode answer AND a correction to existing claims.**
- **Git clean at open** (no drop). Tip at close: `559cfd7`.
- **Ledger (machine figures): 493 entries · 403 visited · 416 leads.** Retrieval **6 of 6**; tool calls **9 of 10**.
- **CORRECTION — the single most important open item in the corpus.** The **Ultimate Clash Soccer** section listing (43 articles) contains five ids we have previously cited as DLS sources: `7916959134737` (change kit), `7917587319313` (change formation), `7917423348497` (get promoted), `7917583876625` (player roles), `17146555181585` (sell players / "bux"). A check of the KB shows those ids entered our corpus as **related-article links inside DLS articles**, not as DLS section listings — so the DLS attribution was never established by a listing. Status is **ATTRIBUTION UNCERTAIN** (not "definitely UCS", not "DLS"). **Suspended as DLS facts until settled:** formation season-gating, the promotion/relegation XP meter, the Player Roles sub-system, the home+GK kit route, the "bux" sale reward. **Conflicts (n) and the kit divergence are re-opened, not resolved.**
- **Netcode gap CLOSED, first-party:** DLL runs both players on FTG cloud servers; the netcode is designed so the **opponent's** connection quality cannot degrade your experience (**lag-switch cheats ineffective**); your **address is never revealed** to the opponent (DoS hard). If *you* lag it is between your device and their server — usually the last mile. **≈2MB per match**; low bandwidth need but **sensitive to latency and packet loss**; **IPv6 and 5G supported**; tip: **disable Bluetooth on Wi-Fi**; **no Facebook invites** but **local same-platform multiplayer over the same router**; multiplayer needs Wi-Fi or high-quality 5G/4G/3G.
- **Two distinct destructive controls** (both in Settings → Advanced): **Reset Profile** (loses progress incl. purchases, **one per 30 days**, no undo) vs **Delete Profile** (Main Menu → Settings → Advanced → **Delete (trash can)** → Delete Profile; **wipes all profiles on the device**, cancellable via **"Cancel Request" before the countdown ends**).
- **Census:** "Ultimate Draft Soccer" is a **stale slug** — the section is **Ultimate Clash Soccer** (slugs are not evidence). A **sixth title section exists: 8 Ball Hero FAQs (360000489137)** — the family census needs one more row.
- **Help-centre structure fully mapped** (section ids unlock the remaining sections): Core Principles `360002602258` (1) · Parents' Guide `360000030369` (8) · **General FAQs `203171905` (21)** · DLS `203117809` (52, all read) · Score! Hero `203117609` (24) · Ultimate Clash Soccer `7900693036561` (43) · Score! Match `115001619089` (43) · 8 Ball Hero `360000489137`.
- **Save-data transfer confirmed cross-game (214387685):** Google / Apple (iOS 13+) link for DLS, UCS, Score! Hero, Score! Match; **not automatic**; **not Google Play Games or iCloud**; retired games (DLS19) are iCloud / Google Play Saved Games only with **no cross-platform transfer**; 8 Ball Hero uses Facebook.
- **Next exact action (Turn 36, in order):**
  1. **Check `git log -1 HEAD`**; repair if dropped (ISSUE-0014 hit turns 21, 23, 24).
  2. **Mid-Session Monitoring** — one fetch (dlskiturl).
  3. **SETTLE THE ATTRIBUTION FIRST** — open `7917423348497` (get promoted), `7917587319313` (formation) and `17146555181585` (sell players) and read which game/section each belongs to. This decides whether three of our progression claims are DLS facts at all.
  4. Then enumerate the **General FAQs section `203171905`** (21 articles) — it is now unlocked and may paginate.
  5. Then, as budget allows: `360018359998` (DLL matchmaking) or `214388065` / `214388105` (device incompatibility and download errors).
  6. Log, bluff-check, snapshot, commit research **first**, then handoff **second**.
- **Do NOT enter STATE_2.** No dimension closed. Step-5 package prepared but **not delivered**.

## Progress signal (bootstrap)

- **Corpus:** 15 imported topics; **all 52 DLS FAQ articles read**; Core Principles; storefront version chain; family census (**needs a 6th row**); coin income (11 sources) + gem income (5 sources); third-party price model; coaching model + first-party coaching; **stat bible**; **card-colour ladder**; **Dream Point Boost rules**; **Season Pass economics (two diverging articles)**; **Prize Ladder reward pool**; **clan rules**; **scoped difficulty denial**; **account-recovery routes**; **customisation map**; **live-service value-change policy**; **Reset Profile vs Delete Profile**; **facilities/squad-cap mechanism**; **My Profile menu map**; **netcode**; version chain 13.050→13.430.
- **Rules of record:** DB OVR labels = estimates **and point-in-time readings — published values move, sometimes temporarily** · DK+dlsinside = ONE family · ±1 drift, cause open · open the card before trusting an index row · match by id sets, never list length · **a URL slug is not evidence — read the page** · shell curl unusable · Reddit/TikTok fetch-blocked (403) · **support.ftgames.com can return HTTP 200 behind a sign-in wall** · reconcile the frontier before judging yield · **never infer completeness from an unreconciled list — check whether a listing paginates** · first-party articles carry no version stamp · FTG does not pre-announce updates · black cards = the special tier · Season Points ≠ Dream Points · ad income is variable · two device-only timers · **squad size is a spendable progression target** · FTG's own text contradicts itself in several places — record both · **Reset Profile and Delete Profile are both destructive; never suggest either without a warning** · no backslash escapes in bash commands · log figures from script output.
- **Cycle dates:** last completed self-audit: never; last completed full sweep: none. **Verification debt:** none owed yet; Mechanism 9 package due at the end of STATE_4.

## Pending decisions / disputed / asks

- **Step-5 package (prepared, undelivered; updated Turns 27 and 29):** both timers + DP/tier; balances; spending stance; squad/division and which formations the grid offers; **4b save-link check**; prompt-capture upgrade; PRs #1/#2 + PROPOSED amendment #2; optional screenshots. **Natural additions now:** accommodation level + squad size, and connection type (multiplayer is latency-sensitive).
- **Disputed claims: 0.** Open conflicts: (c) Cult Heroes route; (d) Aubameyang year; (e) Season Pass 1 vs 6; (f) Vozinha 83/84; (g)+(k) Pedri 87/86/85; (h) ±1 drifts (cause open); (i) Classic 32/34; (l) Kane 86 vs 85 in one article; (m) coach targeting; **(n) "bux" vs "coins" — re-opened, may be two games**; (o) sale reward (**attribution uncertain**); (p) Season Points completing vs winning; (q) Progress Bank basis. Minor divergences: channel lists; **kit route — re-opened**.
- **Known-unknowns:** Roles mechanics (**attribution uncertain**); OVR thresholds for card tiers; **all prices**; per-season formation count (**attribution uncertain**); both in-game end dates; device limit for code transfers; **per-level squad slots and facility costs**; **individual facility bonuses**; auth-walled contents; **General FAQs (21) enumeration**; **the 8 Ball Hero section**; **which game each of the five re-attributed articles belongs to**.

## Working context

- Issue tracker: ISSUE-0001, 0003–0008, 0010, 0011, 0013, **0014 (occurrences #4 #5 #6)** open; 0009, 0012 resolved.
- **Bluff check (Turn 35):** clean and deliberately conservative — the re-attribution is filed as ATTRIBUTION UNCERTAIN rather than flipped to a confident "these are UCS", because Zendesk can surface one article under more than one section; conflicts (n) and the kit divergence were **re-opened** rather than silently resolved.
- **Continuity note:** consult the User Profile before any recommendation; verify game-state currency before any irreversible or resource-dependent action.

## Turn-end fields

- Turn end: research commit+push `559cfd7`; handoff commit follows. PR #3 remains the single active PR. Next input expected: `>`.
