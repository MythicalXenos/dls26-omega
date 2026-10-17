# CONFLICTS LEDGER — DLS26 OMEGA
Consolidated 2026-10-17T19:15Z (session sess-20261017-001, turn 6). Authority: CONFLICT PROTOCOL (Core Identity) and the EVIDENCE CONFLICT log category.
Each entry: the two sides with origin and date, the status, what would settle it, and what the system may say meanwhile. An unresolved conflict is never resolved by picking the more convenient side; where advice depends on one, both are presented with the cost of being wrong.

## OPEN

### C-001 — Language count: 15 vs 24
- **Side A:** 15 languages — App Store listing snapshot, captured 2026-10-11 (CLAIM-053, store-published).
- **Side B:** 24 languages — static APK listing metadata, captured through 2026-10 (CLAIM-094, APKMirror-derived).
- **Status:** UNRESOLVED. Hypothesis to test first: the store field counts *localised store listings* while the APK field counts *packaged language resources*; they would then both be true of different objects.
- **Settles it:** a datamined resource count (`res/values-*` directories) or an official statement of supported languages.
- **May say meanwhile:** "the store lists 15 localised listings, the APK metadata lists 24 languages — these may count different things." Never quote either as "the" language count.
- **Reopening/verification:** RQ-20261017-012.

### C-002 — Leaderboard reward cadence: "weekly gems" vs 3–30 day resets
- **Side A:** official FTG text says multiplayer leaderboards reset at regular intervals of 3–30 days (CLAIM-002, Confirmed).
- **Side B:** an Indonesian community guide says Dream League Live pays gems weekly by leaderboard position (CLAIM-051, Community Consensus), and CLAIM-066 repeats "weekly-leaderboard gems".
- **Status:** UNRESOLVED but narrowed — the official 3–30 day window does not forbid a weekly *reward* cycle; the conflict is about whether the words describe the same clock.
- **Settles it:** an in-game leaderboard screen capture showing both the reset timer and the reward statement.
- **May say meanwhile:** "resets are officially 3–30 days; weekly gem payouts are a community report and are not confirmed."

### C-003 — Release payout: "coach" vs "bux/coins"
- **Side A:** v12.200+ release grants a *coach* (official article 360003945617, CLAIM-032 / CLAIM-114, Confirmed).
- **Side B:** earlier captures describe a specified payout of "bux"/coins (CLAIM-029, inherited summary).
- **Status:** UNRESOLVED, most likely a version change (payout model changed at 12.200) rather than a contradiction.
- **Settles it:** a current-build release observation, or an article revision captured after 12.200 that mentions both.
- **May say meanwhile:** "in v12.200+ you receive a coach; older text describes a coin payout, so the payout may depend on build."

### C-004 — iCloud save toggle
- **Side A:** an older official article documents an in-game iCloud toggle for DLS (preserved in the inherited corpus).
- **Side B:** the current save/account model is Google/Apple sign-in plus a one-time transfer code (CLAIM-022/083, Confirmed).
- **Status:** DISPUTED (CLAIM-042) — the older article is not obviously wrong, it is older.
- **Settles it:** a current-build Settings capture on iOS.

### C-005 — "Weekly" DLL structure vs multi-ladder reality
- **Side A:** community descriptions treat DLL as a weekly ladder (CLAIM-066).
- **Side B:** progression is multi-track with no single global rank (CLAIM-088, High Confidence), and the mission's "#1 global" target has no verified surface at all (CLAIM-003, Speculative).
- **Status:** UNRESOLVED in wording; the underlying facts are compatible if "weekly" refers to one of several ladders.
- **Settles it:** a capture of the live leaderboard surface with its timer.

## RESOLVED (kept for history, with the evidence that resolved them)

### C-R01 — Launch date: Dec 4 2026 vs Dec 17 2025
- Community text (thesoccerera, EV-001/002) claimed "full global availability December 4, 2026"; the store version history shows build 13.040 dated 17/12/2025 and continuous updates since.
- **Resolved** in favour of the store timeline (CLAIM-008). The community claim is retained in-record as a historical anomaly, not deleted.

### C-R02 — Summer Spotlight attribution
- Two candidate update windows; resolved by the version-history mapping to the 13.310–13.350 band (CLAIM-048). Retained as resolved.

### C-R03 — XP transcription 145,299 vs 145,296
- A Tier-1 world-record total was transcribed as 145,299; the source states 145,296. **Resolved** by re-reading the source; corrected in the KB with the transcription lesson recorded (numeric transcriptions get a second check).

## Standing rule for this ledger
A conflict is closed only with evidence that settles the proposition, never because a later claim simply repeated one side. Where a conflict depends on the current build and cannot be checked in this environment, it stays open and its advice states the dependency.
