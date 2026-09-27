# USER PROFILE

Per PROMPT.md §8. Everything about the user. All club/game state is labelled **"last known as of [timestamp]"** and is NEVER assumed current. All club and game state carries volatility-Critical.

Individual match results and mid-session resource deltas do **not** belong here — they go to the MATCH LOG category of `logs/main_operational_log.md`.

> **Reference note (verbatim from PROMPT.md §8):** "Before any recommendation: consult the User Profile in the KB for preferences, game state, coaching state, spending stance, and anything else the profile has come to hold. Verify game state currency against confirmed-current values — confirmed by me in this session, or by a raw-data extraction taken since I last played — before any irreversible or resource-dependent action."

---

## 1. Identity & hardware

| Field | Value | Evidence class | As of |
|---|---|---|---|
| Device (play) | Samsung Galaxy S9+, USB debugging enabled, unrooted | prompt-stated → to be confirmed with the user | 2026-09-27 |
| Second machine | MacBook Air M4 | prompt-stated | 2026-09-27 |
| Test device/account | Dedicated secondary device/account available; technical data only, never personal game state | prompt-stated | 2026-09-27 |
| Platform/store region | UNKNOWN — asked at first contact | — | — |

## 2. Club and game state (last known as of prompt creation — date UNKNOWN, treat as stale until confirmed)

| Field | Last known | Label | As of | Volatility |
|---|---|---|---|---|
| Game version installed | UNKNOWN | gap G-0002 | — | volatility-Critical |
| Squad composition (primary XI) | UNKNOWN — user has one special card and is building around standard cards | user-stated, partial | prompt creation | volatility-Critical |
| Squad composition (secondary XI) | UNKNOWN — rotation not yet set up | user-stated | prompt creation | volatility-Critical |
| Player stats & coaching state | UNKNOWN — no extraction yet | gap | — | volatility-Critical |
| Coins / premium currency balances | UNKNOWN — exact currency names pending terminology resolution (G-0005) | gap | — | volatility-Critical |
| Coaches by type and rarity | UNKNOWN | gap | — | volatility-Critical |
| Facility levels | UNKNOWN | gap | — | volatility-Critical |
| Division & season points | UNKNOWN | gap | — | volatility-Critical |
| Prize-ladder position | "grinding the prize ladder for a special player" — position unknown | user-stated | prompt creation | volatility-Critical |
| Active events & progress | UNKNOWN | gap | — | volatility-Critical |
| Special cards owned | one (identity unknown) | user-stated | prompt creation | volatility-Critical |
| Formations unlocked | 3-2-3-2 (preferred, in use); 3-1-4-2 (unlocked, not priority); 4-4-2 no longer played | user-stated | prompt creation | volatility-High |
| Control toggles | Kick Assist OFF, Cross Assist OFF (these two specifically); all other toggles unknown | user-stated | prompt creation | volatility-Low |
| DLL status | not started yet | user-stated | prompt creation | volatility-Critical |

## 3. Playstyle model

Built from conversation *and* reported results. Where stated and demonstrated playstyle diverge: flag explicitly, ask whether the stated preference is **aspirational** (what the user wants to do) or **descriptive** (what they actually do), calibrate to demonstrated while working toward aspirational, never silently reconcile.

| Dimension | Stated | Demonstrated | Divergence? | Notes |
|---|---|---|---|---|
| Formation preference | 3-2-3-2 | unknown | unknown | 3-1-4-2 unlocked but not a priority |
| Build-up / attacking approach | unknown | unknown | — | first-contact question |
| Defensive approach | unknown | unknown | — | first-contact question |
| Mechanical experience | "inexperienced mechanically, want to learn everything" | unknown | — | self-assessed |
| Mode focus | career mode grinding; watches ads for rewards | — | — | user-stated |
| Competitive pressure response | unknown | unknown | — | matters for DLL prep |

## 4. Preferences and decisions

Newest versions override old conflicting ones; unsuperseded preferences stay active regardless of age. When uncertain whether a decision is significant, treat it as significant and record it.

| Date | Type | Content | Status |
|---|---|---|---|
| prompt creation | preference | Primary formation 3-2-3-2 | ACTIVE |
| prompt creation | preference | 3-1-4-2 unlocked, not a priority | ACTIVE |
| prompt creation | preference | No longer playing 4-4-2 | ACTIVE |
| prompt creation | preference | Kick Assist OFF, Cross Assist OFF | ACTIVE |
| prompt creation | preference | Rotation: primary = best XI, secondary = second-best XI, no overlap except GK, no bench subs, cross-formation overlap allowed, switching per a researched conditional decision tree maximising win rate | ACTIVE — setup deferred until squad depth exists |
| prompt creation | preference | Building around standard cards | ACTIVE |
| prompt creation | factual claim (user-stated) | DLS26 has no position locking; players can be deployed in any position | PENDING VERIFICATION — gap G-0001, Skeptic runs on it during the sweep |

## 5. Spending profile

Two inputs: community research on what is worth buying at each stage, **and** the user's directly stated stance, categories, limits, triggers. Neither exists yet.

| Field | Value |
|---|---|
| Stated stance | UNKNOWN — first-contact question |
| Categories | UNKNOWN |
| Limits | UNKNOWN |
| Triggers | UNKNOWN |
| Ad-watching behaviour | Watches ads for rewards (user-stated) — implies zero-spend or low-spend leaning, **not confirmed** |
| Community research | NOT STARTED |

## 6. Understanding tracker (depth view) and 7. Skill tracker (progression view)

Two views of one data set, never collapsed. Understanding = how well a concept is grasped. Skill = whether the in-game action can be executed. Demonstrated execution is evidence of understanding, not proof of it; gaps in understanding determine which skill to teach next.

| Concept / skill | Understanding (none → deep) | Executed in play? | Evidence | Next step |
|---|---|---|---|---|
| *nothing assessed yet — no match reports, no questions asked* | | | | |

Self-assessed baseline: "inexperienced mechanically, want to learn everything" (user-stated).

## 8. User-reported facts (labelled `user-stated`)

Every item in §2 and §4 above marked user-stated is a fact of this class. Extractable facts get cross-referenced against datamined data and weighted per the Evidence Hierarchy; non-extractable facts get verified by exhaustive research with contradiction tracking.

## 9. Gaps about the user (work around them, flag reduced confidence where they bite)

Store/region; exact currency balances; squad list; facility levels; division; prize-ladder position and target card; which special card is owned; coaching state; all control toggles other than the two named; spending stance; playstyle dimensions; match results; whether the stated no-position-locking belief is descriptive or aspirational.
