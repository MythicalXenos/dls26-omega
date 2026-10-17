# FIRST CONTACT BASIS — Step-5 briefing skeleton

**Status: written at turn 10, deliverable only at Step 5. This file is not delivered, quoted, or summarised to the user during bootstrap.** It exists so that first contact is assembled from vetted material rather than improvised. Every statement below is traceable to `kb/claims.jsonl`; where the KB is weak, the weakness is written into the briefing rather than hidden.

## 0. How the briefing will be tiered
The user will always see which tier a statement comes from. The four tiers map to the KB's confidence field and never get silently upgraded in prose:

| Briefing tier | KB basis | Permitted use |
| --- | --- | --- |
| **T1 — Official** | Confirmed, official-stated evidence (FTG support, store listing, EULA/policy) | State as fact; cite article/claim |
| **T2 — Corroborated** | High Confidence, ≥2 independent origins or a physical record | State with the qualifier "documented", verify in-client before acting on numbers |
| **T3 — Community** | Community Consensus, single-family guides/threads | Label every time ("community guide reports…"); never plan around alone |
| **T4 — Hypothesis** | Speculative / Disputed | Name it as a hypothesis and a test; never coach from it |

Discipline rule: a T4 claim quoted in coaching must carry its challenge (SCHEMA §4a). A claim past `next_due` is quoted with its date.

## 1. What the mission actually is (and the first thing the user must decide)

- **The prompt's success condition is "make the user the #1 DLS26 player". The KB cannot yet define "#1" operationally.** CLAIM-003 (Speculative, overdue) records that the highest verifiable global ranking surface is **not established**. The candidate surfaces found are: the store-advertised global leaderboard, Dream League Live **LIVE Tier**, Clan leaderboards, Game Centre friend leaderboards, and career's 8-division ladder (CLAIM-045, CLAIM-071, CLAIM-098).
- The only *official* ranked surfaces held are: **Season Leaderboard** = Season Points totals, earned by winning matches (CLAIM-071, T1); **career promotion/relegation** = XP ladder, wins gain XP, losses lose XP (CLAIM-067, T1); **DLL matchmaking** = LIVE Tier + location + availability (CLAIM-081, T1).
- There is **no verified public surface that ranks all DLS26 players on one global list** (NEG-007 records this as an explicit failure-to-find, not as proof of absence).
- Therefore the briefing opens with a definitional question, not a training plan: **which ladder is "#1" on, over what window, and with what constraints?** Everything downstream (squad build, match volume, season timing) depends on that answer. This is a user-only decision.

## 2. Tier 1 — official facts the coaching can stand on

**Account safety (must be delivered before any competitive advice):**
- One DLS account per player; official transfer paths are same-provider sign-in or a single-use cross-platform code (CLAIM-083).
- Signing out of the provider at any time **unlinks** the profile — uninstall/device-change loss risk (CLAIM-083).
- Career Reset is irreversible, one per 30 days; Delete Profile wipes **all** device profiles (CLAIM-082).
- Only App Store / Google Play builds are authorised; modded APKs, external hacks and bug exploitation are bannable, and bans are not lifted on request unless incorrectly flagged (CLAIM-075, CLAIM-043).

**Mechanics that change how the game feels:**
- Auto-switch is ON by default and is changed at gear icon → Controls → Auto Switch (CLAIM-106) — directly relevant to the "broken switching" sentiment in CLAIM-091.
- Skill moves: swipe down = Marseille turn, up = rainbow flick, left/right = stepover (CLAIM-107).
- Dream League Live is always human-vs-human, no bots, no difficulty control, no AI manipulation (CLAIM-080, CLAIM-009); matchmaking uses LIVE Tier + location + pool at match time (CLAIM-081).
- Single-player difficulty scales with division progress, up and down (CLAIM-011, CLAIM-080).
- Formations are **season-limited**: only a limited set (the official article says two) is available per season (CLAIM-077) — any formation recommendation must be re-mapped each season.
- Graphics: Main Menu → Profile → Graphics (Android only); 30/60 FPS cap, quality presets, GL troubleshooting (CLAIM-109, CLAIM-037, CLAIM-078).
- Connection ladder: disable VPN, better signal, near router, reset router, other Wi-Fi; known DNS fix 8.8.8.8 (CLAIM-073, CLAIM-108); FTG's netcode claims opponent connection does not affect your experience (CLAIM-113).
- Selling a non-starting-XI player grants a coach and puts the player in a "Recover" section (CLAIM-114, CLAIM-076); the transfer market refreshes each in-game week after a single-player match (CLAIM-020).
- Season Pass is free + premium, pays a Progress Bank at season end, and seasons are global (CLAIM-040, CLAIM-014).
- Reward channels: coins (matches, objectives, cups, clips), gems (objectives, tournaments, pass, Prize Ladder, DLL), Dream Points/event currency (Prize Ladder) (CLAIM-019, CLAIM-015, CLAIM-016, CLAIM-050).

**Version reality:** current public build observed at **13.430** (Google Play, 2026-09-14), prior 13.420 "Summer Spotlight" (CLAIM-087, CLAIM-048, CLAIM-057); launch build 13.040 dated 17/12/2025 (CLAIM-054). Anything the user sees that differs from 13.4x invalidates the numerical parts of the briefing.

## 3. Tier 2 — corroborated, verify in-client before acting

- Standard-card ceiling ≈ **86 OVR** and named profiles (Haaland, Mbappé, Yamal, Dembélé, Kane) — community guide, two families, not store-verified (CLAIM-058, CLAIM-061).
- Special cards exceed the standard ceiling; taxonomy is multi-scheme with ~10 types (CLAIM-059, CLAIM-116). One DB's numbers are self-declared approximations (CLAIM-060).
- Community data/tooling lags the live season; fan datasets stop at DLS23-era assets (CLAIM-085). Treat all community DBs as planning aids (CLAIM-046, CLAIM-047, CLAIM-049).
- Roster licensing gaps exist — some players/leagues are absent for licensing reasons (CLAIM-079). Never plan a squad around a named player without checking the account's market.
- Squad depth: reserves plus a fixed eight substitutes (CLAIM-101) — community consensus.
- Release/coach economy and market quality scaling with club progress (CLAIM-110, CLAIM-114).
- Five facilities: Stadium, Medical, Commercial, Training, Fanzone (CLAIM-093).
- Live-service cadence: roughly monthly version bumps plus calendar-tied events (CLAIM-103).

## 4. Tier 3 — community consensus, always labelled

- Division season = **15 matches**; promotion via Division Objectives (wins + goals), not requiring a perfect record (CLAIM-062, single VI family).
- Season Pass activation ≈ 400 Season Points; full pass ≈ 1,095 coins (CLAIM-068).
- Prize Ladder Dream-Point milestones 62.5K / 115K / 175K / 250K (CLAIM-063, CLAIM-064).
- Currency-flow map and multi-track progression — no single global rank (CLAIM-065, CLAIM-066, CLAIM-088).
- Facility economics: Stadium Commercials L2 +13% / L3 +21% coins per match (CLAIM-111, single family).
- Formation rankings: 4-2-3-1 "most balanced", 4-3-3 wing/counter, 3-5-2 midfield control, 5-2-1-2 low block (CLAIM-070) — must be filtered through the season-limited pool (CLAIM-077).
- Launch-era sentiment: goalkeeper positioning and defender auto-switching criticised (CLAIM-091); "scripts" is slang, not a documented system (CLAIM-090).
- Store-sentiment wish list: manage other teams, choose a league at season start; Bronze/Silver/Gold/Diamond Cup progression (CLAIM-118).
- DLS27 cycle being prepared by fan sites (CLAIM-117) — planning relevance only.

## 5. Tier 4 — hypotheses with named tests

- Weighted-capacity player development: CON/SPE cost more than STA; 10% weight ≈ +1 OVR; +10 OVR cap (CLAIM-049, one simulator). **Test:** upgrade a cheap player one attribute step in-client and record the OVR delta.
- Team OVR = mean of the 11 base-or-max ratings (CLAIM-104). **Test:** compare the in-game team OVR with the computed mean for the user's actual XI.
- "Trained" player ≈ base + 1 OVR (CLAIM-105) — quarantined; do not use.
- Starting state 50–60 OVR / "Academy Division" (CLAIM-102) — single guide.
- World Cup Winners/World Heroes event dating (CLAIM-095, CLAIM-096) — single UGC sources.
- 60,000-point challenge cost (CLAIM-112) — single thread.
- Device minimums: the official article 404s; no verified minimum-spec list (CLAIM-100). Only the store requirement is solid.
- Save-path conflict: older article describes an iCloud toggle, current backup article says iCloud/Play Games are not used (CLAIM-042, **Disputed**) — never advise on save migration from the KB; check the user's build in-client.

## 6. What the briefing must admit it does not have

1. **No primary retrieval this session.** Every game fact is inherited from the repository's imported corpora; all six external research families are at ACCESS_BOUNDARY (allowlist block). NEG-004 records the negative GitHub/npm search; NEG-007 the missing global ranking surface.
2. **No APK/datamining layer.** Step 2 as written collides with the EULA (CLAIM-043) and the sanction policy (CLAIM-017/075); nothing was downloaded or decompiled (OBS-013). Numbers that only datamining could settle remain unverified.
3. **English-language community coverage is snippet-level** — the largest deficit in the Mechanism-3 walk.
4. **No in-client data yet.** 14 observations are queued in `IN_CLIENT_CHECKLIST.md` (P1: controls list, FPS/quality, camera, stat labels, build number; P2: division/points, Season Leaderboard label and scope, match rewards, release preview, Prize Ladder state; P3: formation + OVRs, subs count, market refresh + price, coach rarity).
5. **Freshness debt.** CLAIM-003 and CLAIM-006 are past their review dates and are quoted with dates; no date was bumped without a check.
6. **No independence claim.** Both imported corpora were produced in earlier sessions of the same system; agreement between them is not independent corroboration. This is stated in the degradation audit and will be stated once, plainly, in the briefing's limitations section.

## 7. User-only asks — batched, to be asked at first contact (not before)

Ordered by what unblocks the most work. The prompt's rule is that questions travel through `handoff/attention_required.md`, so these will be presented as one block, not drip-fed.

1. **Step-2 ruling (required decision, OBS-013).** Options: (a) skip APK decompilation entirely and continue lawful research only; (b) user supplies APK/assets into `raw_game_data/` and accepts the decision as theirs; (c) pursue only static store metadata (APKMirror-style), which is what CLAIM-094 already used. Default if unanswered: (a) + (c).
2. **Ranking definition.** Which ladder is "#1": DLL LIVE Tier, Season Leaderboard, career Legendary Division, Clan, or an external public table? Over what window? Any spend/time constraints?
3. **Account snapshot.** Platform (Android/iOS), current build number, division/Season Points, squad OVR and formation, coin/gem balance, Season Pass state (free/premium/inactive), Prize Ladder event state.
4. **Device.** Model, Android/iOS version, RAM, current Graphics/FPS settings — needed before any FPS advice (CLAIM-109/078 are Android-specific).
5. **In-client capture batch.** Screenshots for the 14 P1–P3 items into `raw_game_data/`; P1 first (it changes what the KB may assert).
6. **Constraints.** Hours per week, tolerance for ad-watching (CLAIM-115: FTG promises no clip frequency), and whether the account is new or carried over (CLAIM-072 — FB-saved profiles are unrecoverable).

## 8. What the first briefing will *not* do
- It will not recommend mods, hacks, save editors, bots or automation — prohibited by CLAIM-075/043 and unsafe (CLAIM-084).
- It will not state a global rank for the user that the KB cannot verify.
- It will not present community guide numbers as official.
- It will not promise a "#1" outcome; it will propose a measurable ladder, a baseline, and a review cadence.

## 9. Delivery gate
Per the prompt's sequence this material is delivered at **Step 5 (First Contact)**, after the Step-2 ruling and the Step-3 device pipeline are resolved. Until then this file stays internal. If the sequence is renegotiated by the user, the tiers and limitations above travel with the content unchanged.
