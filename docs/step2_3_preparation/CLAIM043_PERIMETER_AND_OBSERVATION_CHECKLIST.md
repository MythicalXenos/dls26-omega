# STEP 2/3 PREPARATION SCOPE — CLAIM-043-compliant perimeter (living)
Session sess-bb22126f679b | Updated 2026-10-11T17:43:20Z | Status: prep doc for the Step 1 -> 2 transition (NOT yet in Step 2)

## 1. Why this doc exists
Step 2 is nominally "static analysis". The EULA constraint (CLAIM-043, master v77) forbids reverse engineering, decompilation, and automation of the game. This document fixes the PERIMETER of permitted work so the Step 2/3 transition cannot drift into banned territory, and converts open research residue into a concrete in-client observation checklist (UI-only) that will run when Saad reaches Step 3/5.

## 2. Hard bans (never do; automation hard-blocks per CLAIM-082/083 too)
- No APK/IPA decompilation, unpacking, string mining, binary diffing, or asset ripping.
- No traffic interception, protocol RE, certificate pinning bypass, MITM, or API probing of game servers.
- No automation: no bots, no input injection, no scripted UI traversal, no memory editing, no save editing (save editors = the same cheat ecosystem as EV-215/217 — DO-NOT-USE).
- No third-party "tools"/"hack" packages (npm/GitHub ecosystem logged in EV-215/217 is evidence, never tooling).
- No touching Reset (CLAIM-082: 30-day cooldown, wipes IAP) or Delete Profile (wipes all device profiles). Never sign out of Google/Apple (CLAIM-083: profile-loss hazard).
- Anything requiring the above is not "research debt" — it is permanently out of scope; record it as ACCESS-boundary, not as owed work.

## 3. Allowed surfaces for Step 2 (now) and Step 3 (device)
- Public store listings, version notes, screenshots, review pages (fetch-capable when tools return).
- Official support articles + their public comment threads (cursor backlog).
- Public community pages/databases as PLANNING AIDS ONLY (CLAIM-085: validate in-client).
- In-client, human-driven, UI-only observation (screens are readable by the player): menus, leaderboards, squad/transfer screens, item catalogue, settings, version/build display. Screenshots belong to Saad's device; we describe procedure, never take control.
- Manual logs Saad transcribes (e.g., match results, Season Points per win) — user-generated measurements are admissible evidence with tier gates.

## 4. Residue -> in-client observation checklist (feeds Steps 3/5)
1. **Ranking target (CLAIM-003/071)**: open each named surface in-client (SEASON LEADERBOARD; DLL global leaderboard; LIVE Tier display; career division ladder; clan board). Capture: exact labels, metric shown, visible scope (global/friends/division), any tie-break/reset text on screen. Resolves staged ask #6.
2. **XP ladder surface (CLAIM-067)**: find the XP/rank display; record whether XP is attached to DLL rank or career divisions; record post-match XP delta screens if any.
3. **Legendary Fitness (CLAIM-006)**: item catalogue + release flow (Transfers > Manage Players) — record exact item names (coach/fitness coach/legendary fitness?), boost targets shown, and whether release-yield previews coach items. Terminology conflict resolution lives here.
4. **Roster validation (CLAIM-079/086)**: squad screen attribute labels (cf CLAIM-013/086 taxonomy: SPE/ACC/STA/... vs renamed), club names present/absent (Bundesliga check), ratings span.
5. **Version marker**: settings/about shows build/version — resolves the 12200-vs-13.4x discrepancy against store notes.
6. **Economy spot-checks (CLAIM-015/019/020/032/076)**: gem/coin source lists, market refresh timer, release yields (bux vs coaches), prize ladder rewards — all read from UI text.

## 5. Device-pipeline guardrails (Step 3 pre-commitment)
- Sign-in status must be pinned BEFORE any session work; verify the linked Google/Apple account at session start (CLAIM-083).
- Device disposition stays UNASSESSED until Step 3 opens; no assumptions about Saad's device in claims.
- All captures are Saad-driven; the agent only interprets provided screenshots/transcripts (UI-only compliance).
- Sensitive artifacts (roster, balances, account identifiers) stay in protected storage; sanitized copies only (master capture rules).

## 6. Transition gating
Step 2 may open only when the Step 1 epoch is sealed (coverage accounting + extraction sealed per OMEGA-EPOCH-001) OR the user directs the transition directly. This doc does not advance the state machine; it only pre-loads the compliant perimeter. The epoch cursor (official-support backlog) should keep priority when fetch tools return — Step 2 adds no fetchable content until then.
