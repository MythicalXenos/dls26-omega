# EV-249 — Static APK security analysis of `com.firsttouchgames.dls7` (beerphilipp/taptrap research corpus)
**Date:** 2026-10-17T23:50Z
**Tool:** api.github.com raw fetch (allowlisted) of `beerphilipp/taptrap/vulnerable_app_detection/results/2025-05-20/output/com.firsttouchgames.dls7.json` and `beerphilipp/tabbed-out/analysis/results/com.firsttouchgames.dls7.res.json`.
**Origin:** Academic security-research datasets (TapTrap tapjacking study, Tabbed-Out custom-tabs study). The APK they analysed is at path `/home/experiments/apks/android/tapjacking/free_18_12_24_merged/com.firsttouchgames.dls7_merged.apk` with `target_sdk=35` (Android 15, late-2024/2025 build — this confirms DLS26 targets a recent SDK).
**Authenticity limits:** These are security-research JSONs, not game data; they only reveal package structure and third-party SDKs present. No game logic. Build hash is unknown. Target SDK 35 suggests a recent build consistent with B-008.

## Verified technical facts
- Package name confirmed as `com.firsttouchgames.dls7` (corroborates CLAIM-072/B-002).
- **Target SDK 35** (Android 15) — DLS26 ships as a modern-targeted app, not a legacy target.
- **MainActivity: `com.firsttouchgames.dls7.MainActivity`** (confirms entry point).
- **52 activities** total.
- **Ad networks present** (visible from activity class names in the static manifest):
  - AdColony (`com.adcolony.sdk.*` — interstitial, ad view)
  - Unity Ads (`com.unity3d.ads.android.view.UnityAdsFullscreenActivity`)
  - MoPub (`com.mopub.mobileads.*` — interstitial, MRAID, browser, rewarded video)
  - Google Play Ads / AdMob (`com.google.android.gms.ads.AdActivity`)
- Custom Tabs session intent filter is enabled (`uses_ct: true`, `ct_session_intent_filter: true`) per the tabbed-out result, i.e. the app uses Chrome Custom Tabs for in-app web views (likely support-center links).
- Tapjacking protection: `is_enabled: true`, `protected_confirmation: false` — the app enables touch filtering but does not use the Android Protected Confirmation UI for irreversible actions.

## Relevance
- Confirms the game is a **Unity build** (Unity Ads activity + `com.unity3d.ads` namespace) — useful for Step 2 (Unity asset bundles likely present, asset layout follows Unity conventions).
- Four ad networks in the same build is consistent with the multi-ad-network rewarded-video policy in CLAIM-115/GS-015 ("multiple ad networks manage their own content; FTG controls only ad types"). Claim direction corroborated; the set is larger than we previously stated (AdColony, Unity Ads, MoPub, AdMob all visible, not just "multiple" generically).
- Tapjacking surface exists but with filtering; never a player-facing mechanic, noted only for completeness.

## Covers
CLAIM-136 (new), CLAIM-115 (corroborates multi-ad-network), CLAIM-072/B-002 (pkg name), CLAIM-094/B-008 (technical envelope).
