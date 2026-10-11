# RANKING & PROGRESSION RESIDUE — synthesis memo (living)
Session sess-bb22126f679b | Updated 2026-10-11T17:35:13Z | Status: Step 1 research epoch OPEN
Purpose: consolidate mission-residue items (CLAIM-003/071 ranking surfaces, CLAIM-067 XP ladder, CLAIM-006 Legendary Fitness) into one precise "known / open / where-to-close" memo, plus the volatility revalidation calendar. Nothing here is coaching advice; all tiers quoted from kb/claims.jsonl.

## 1. Ranking surfaces — what is KNOWN (evidence-tiered)
- **CLAIM-071 (Confirmed, official 7916583518353)**: SEASON LEADERBOARD exists as a Main Menu surface showing **Season Points totals**; Season Points are earned from **WINNING matches**; Season Points also unlock Season Pass ladder prize tiers.
- **CLAIM-067 (Confirmed, official 7917423348497)**: ranked progression is an **XP LADDER** — wins earn XP, losses lose XP; max XP at current rank = PROMOTION; XP loss = RELEGATION. Article does NOT state which surface (Career divisions vs Dream League Live).
- **CLAIM-002 (High Confidence)**: DLL Multiplayer leaderboards compare players (official).
- **CLAIM-021 (High Confidence, Critical volatility)**: SEASON LEADERBOARD displays players' Season Points (cf CLAIM-071 official upgrade).
- **CLAIM-081 (Confirmed)**: DLL matchmaking = LIVE Tier + location + availability pool; no difficulty overlays; outcomes = skill.
- **CLAIM-003 (Speculative, Critical volatility, DUE 2026-10-11)**: the mission-target ranking ("highest verifiable global competitive ranking") is **NOT yet pinned to a specific surface**. Named surfaces: (a) DLL Global Leaderboards (store text), (b) LIVE Tier ranking (matchmaking), (c) Clan points/leaderboards, (d) career 8-division ladder topping at Legendary Division (store text), (e) SEASON LEADERBOARD (Season Points).

## 2. Ranking residue — OPEN items (must close before ranking strategy locks)
1. **Target-surface selection** for "#1 verifiable global ranking" (user decision at Step 5 — staged ask #6 in attention_required.md).
2. **Tie-break rules** on every surface (Season Points ties, XP ties, DLL leaderboard ties).
3. **Reset intervals** (season length/end date visibility — CLAIM-014 seasons are global bounded periods; leaderboard reset cadence unstated).
4. **Eligibility + verification** (what makes a ranking position "verifiable"; account standing, region scope, minimum games).
5. **XP measurement** (how XP is earned/measured per match; relation between XP ladder and LIVE Tier; whether the XP ladder IS the DLL rank or the Career division ladder).
6. **Division scope of the Season Leaderboard** (global vs league/division-scoped).
Closure candidates (when fetch_page returns): support 360019166777 comment chunks 1-3 (player-stats article comments — community Q&A often carries tie-break answers), develop-players 360003914778 (coaches snippet), player-diamonds, VI guides 186558/197994/199177/161114, reddit (ISS-0006 reopen), plus **in-client observation in Steps 3-5** (leaderboard screens are readable UI — CLAIM-043-safe).

## 3. Legendary Fitness / coaches — KNOWN vs OPEN
- **CLAIM-006 (Speculative, High volatility, DUE 2026-10-11)**: VI community source (download.com.vn, 2025-12-03) claims releasing unused players yields **'fitness coaches'** that boost speed/acceleration. Single origin, translation-interpretation risk. MUST verify terminology before ANY Legendary Fitness coaching.
- **CLAIM-028 (High Confidence)**: coaches are player-development consumables; a selected coach randomly picks a player and boosts one stat (official).
- **CLAIM-032 (High Confidence)**: release economy (v12200+): releasing a player via Transfers > Manage Players can return coach items (cf EV-137 bux-wording conflict, preserved).
- **CLAIM-016 (High Confidence)**: Prize Ladder grants progression rewards incl. coaches, dream point boosts.
- Terminology conflict preserved: "Legendary Fitness" (user plan name) vs "fitness coach" (VI source) vs generic "coach" items (official) — these may or may not be the same object.
- OPEN: (a) does a distinct "Legendary Fitness" item exist in DLS26? (b) does release-yield include fitness coaches specifically? (c) which stats can coaches boost (speed/accel vs all)? (d) is coach-targeting random only?
- Closure candidates: develop-players 360003914778 (coaches snippet — top priority), can-i-sell follow-up comments (EV-137 conflict), VI guides (186558 etc. on the exact wording 'cần thủ'/'fitness'), in-client item catalogue inspection (Steps 3-5).

## 4. Volatility revalidation calendar (OMEGA-VOLATILITY-001 review, t65)
- Volatility mix: Critical 3, High 29, Medium 26, Low 27 (85 claims).
- **DUE 2026-10-11 (today)**: CLAIM-003, CLAIM-006 — first-valid-check still null; t65 local synthesis logged as attempt; **real validation requires sources (fetch_page) or in-client checks**.
- **DUE 2026-10-17**: CLAIM-005 (competitive-integrity reviews, Critical), CLAIM-021 (Season Leaderboard, Critical).
- **DUE 2026-10-24**: CLAIM-004, 007, 008, 011, 014.
- **DUE 2026-10-11→11-01 window (High volatility, 15 claims)**: CLAIM-002/009/013/015/016/017/018/019/020/028/032/040/045/046/047 — mostly official mechanics; revalidate via support re-fetch or store version-notes drift check.
- Priority order when tools return: (1) CLAIM-003/067/071 ranking mechanics sources, (2) CLAIM-006 fitness sources, (3) CLAIM-005/021 critical-drift, (4) version-marker discrepancy (12200 vs 13.4x), (5) remaining dated claims.

## 5. Standing constraints (do-not-cross reminders)
- CLAIM-075: stores-only play; mods/hacks/bug-exploits bannable (ecosystem evidence EV-215/217 = environment only, never tooling).
- CLAIM-043: UI-only access for all Steps 2/3 work (no RE/decompilation/automation).
- CLAIM-082: Reset/Delete-Profile = automation hard-blocks. CLAIM-083: sign-in pinned (sign-out = profile loss).
