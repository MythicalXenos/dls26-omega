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

### C-006 — Auto-switch article: live text vs reported dead link
- **Side A:** the article "Why are my players auto-switching all the time?" (360008315158) is **live and fully captured** — EV-145 holds its complete text, fetched 2026-10-10T22:58Z, and CLAIM-106 is built on it verbatim.
- **Side B:** the sibling session on `arena/22655f48-dls26-omega` records the same article as a dead link (GS-030), captured on its own timeline.
- **Status:** UNRESOLVED. Both captures are physical; the most probable explanation is a transient Zendesk outage or a removal-and-restore between the two fetches, not a contradiction about content.
- **Settles it:** one fresh fetch of the slug in a permitted environment, recording HTTP status and timestamp.
- **May say meanwhile:** quote CLAIM-106 from EV-145 (full text exists) and note that the URL's liveness is not guaranteed; the *behaviour* claim does not depend on the URL staying up.
- **Note:** this is the residual "cross-branch contradiction" item carried since turn 6.

### C-007 — Which stores are authorised: four vs two
- **Side A:** the Terms of Use / EULA (last updated 25 Jul 2025, EV-170, full page) names **four** authorised stores — Apple App Store, Google Play, Amazon App Store, Windows Phone Store — and says FTG "does not publish to any other store".
- **Side B:** the sanction-policy article (EV-201, verbatim) says **"The only authorised versions of DLS are available from Apple's App Store or Google's Play Store."**
- **Status:** UNRESOLVED. The two official texts are not reconcilable as written. Likely explanations: the EULA is the older, broader legal list (Windows Phone Store is defunct), while the sanction article reflects current distribution. Neither side is a community claim.
- **Impact on the mission:** **none for the red line** — mods, hacks and third-party builds are prohibited under both texts, and only Play/App Store builds are what the user can install today. It matters for precision: CLAIM-043 must not be quoted as "the EULA says Play and App Store only".
- **Settles it:** a current FTG store-availability statement, or an EULA revision listing two stores.
- **May say meanwhile:** "FTG's EULA lists four storefronts; its sanctions article recognises Play and App Store. Only those two are current for DLS26."

### C-008 — Promotion: Division Objectives vs XP ladder
- **Side A (community, VI):** each Division season = 15 matches, and promotion runs through **Division Objectives** — required wins + goals totals, no need to win every match (EV-192 snippet, EV-196 full page; CLAIM-062, Community Consensus).
- **Side B (official, verbatim):** *"The more matches you win, the more XP you will earn. When you reach the maximum XP for your current rank, you will be promoted. Similarly, losing matches will cause you to lose XP and get relegated."* (EV-195, article 7917423348497; CLAIM-067, Confirmed). The article does **not** name the surface (Career division vs Dream League Live rank).
- **Status:** UNRESOLVED, and it is the sharpest conflict found in the interpretive sample, because the two accounts imply different strategies: objective-completion efficiency (Side A) vs win-rate/XP accumulation (Side B).
- **Plausible reconciliation:** objectives grant the XP, or the two mechanics govern different ladders (Career vs DLL). Neither is documented.
- **Settles it:** a Career screen capture showing the promotion requirement (objectives list vs XP bar), or an official article that names the surface.
- **May say meanwhile:** "the only official promotion text describes an XP ladder; a community guide describes division objectives. Which governs Career is unverified — check your division screen before optimising for objectives."
- **Impact on coaching:** blocks any advice that trades wins for goal-farming until resolved.

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
