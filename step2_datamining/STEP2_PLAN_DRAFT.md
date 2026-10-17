# STEP 2 PLAN (DRAFT) — static datamining of APK/assets — execution BLOCKED on OBS-013
Prepared 2026-10-17T22:22Z (turn 19). This is a plan only; nothing here executes Step 2. Execution is blocked by OBS-013 (first-contact EULA/sanctions decision: the user must be the one who obtained the APK legitimately and consents to analysis; the sandbox itself does not download APKs and does not attempt circumvention).

## Goal
Extract authoritative, in-client data that research cannot supply:
1. Exact stat/attribute names, ranges, weight tables, and hidden coefficients.
2. Formations metadata (slot positions, name strings, unlock conditions).
3. Special-card collection IDs, OVR ceilings, acquisition routes.
4. Economy constants (coin/XP/SP/DP rewards per match per mode, coach rarities/stat weights, Form-Boost duration scaling with Training level).
5. Control mapping (input event names, gesture recognisers, assist thresholds).
6. Reset-cycle semantics (Season/Prize-Ladder/Leaderboard period lengths, DLL tier counts and XP).
7. Version/build metadata and any config flags (anti-cheat, debug, chat filters).

## Preconditions (MUST be met before any tool runs)
- [ ] **User consent captured in Step 5 first contact** — explicit acknowledgement that analysing their installed copy is permitted. Recorded with timestamp in `raw_game_data/consent/SCREENSHOT_CONSENT.txt` (git-ignored).
- [ ] **Legitimate APK provenance**: APK pulled from the user's own device (`adb pull` of a Play-installed copy, only with separate `ADB_CONSENT.txt`) or supplied by the user into `raw_game_data/`. **No third-party APK-mirror downloads** for Step 2 — EV-175 (APKMirror) is used only for build/version cross-reference, not as a code source.
- [ ] **Sandbox tooling present**: current probe (turn 21) shows **java, aapt/aapt2, apktool, jadx, adb, d8/dex2jar, baksmali/smali, sqlite3 ALL MISSING**; only python3 3.11 and node 22 / npm 10 are available. Before Step 2 execution we must (a) install default-jre + aapt/apktool/jadx via apt if the sandbox permits, OR (b) perform the analysis on the player's machine with a walkthrough script, OR (c) restrict Step 2 to asset-only inspection via `unzip` + manual XML/JSON reading (possible for strings/assets, not sufficient for dex constants). Installing analysis tools itself does not require consent; running them against an actual APK does.
- [ ] **Size budget respected**: extracted tree kept under 250 MB; `target/`, `build/`, `dist/`, `jadx_out/` are in `.gitignore`.
- [ ] **Hash anchor recorded**: sha256 of the APK file and of any extracted `classes*.dex` and `assets/` tree captured BEFORE any tool runs, so later sessions can detect a different build.

## Forbidden actions (even with consent)
These are recorded so they are not "discovered" to be useful and quietly executed:
- **No running the APK** in an emulator for automated gameplay. Emulation for static inspection of resource loading is acceptable; automation (macros, scripted matches, farming) is not — it is ToU-relevant and contravenes the fair-play position (CLAIM-002, CLAIM-123).
- **No network-interception / packet capture** against live FTG servers. Even if technically educational, it is a ToU red line and is not required for any coaching question.
- **No save-file editing, no memory inspection, no debugger attachment during live play.** Inspecting save files statically (from a consented pull) to understand schema is acceptable; modifying them is not.
- **No patched/modded APKs** as the analysis base.
- **No bypass of licence / IAP / anti-cheat checks.** Reading them is fine; disabling them is not.
- **No redistribution** of the APK, extracted assets, or card images beyond this private repo.
- **No use of the analysis to produce cheats, hacks, or automation tools.** The output of Step 2 is coaching knowledge, not exploits.
- **No tool is installed from untrusted sources** — use distro packages (apt) for `default-jre-headless`, `aapt`, `apktool`, `jadx`; verify package hashes before install.

## Tool chain (expected; verified against sandbox state turn 21 — ALL MISSING initially)
1. **Inspection**: `jadx` (CLI) over `classes*.dex` → Java sources in `step2_work/jadx_out/`. For code-only queries, `jadx -d` single-class decompilation is faster than full dump. **MISSING — install `jadx` after consent gate.**
2. **Resources**: `apktool d -s -f` to decode `res/`, `lib/`, `assets/`, `AndroidManifest.xml` without smali conversion (saves time; we need strings, not smali patches). If we later need smali, re-run without `-s`. **MISSING — install `apktool` + `aapt`.**
3. **Assets walk**: `assets/` typically contains JSON/SQLite/Unity asset bundles. Record the file listing first, then triage by extension:
   - `.json`, `.txt`, `.csv`: direct read with python3 (available).
   - `.db`, `.sqlite`: needs `sqlite3` (MISSING; install or use python's `sqlite3` module which IS in stdlib — python3 has built-in sqlite3 via `import sqlite3`, no CLI needed).
   - `.unity3d`, `.bundle`, `.assetbundle`: needs `AssetStudio`/`UAAE` (MISSING; out of scope unless encountered).
   - `.so`: `readelf`/`nm` for library inventory only (MISSING; defer).
4. **Strings sweep**: before any decompilation, run `strings classes.dex | grep -iE "season|tier|dream point|form boost|coach|ovr|stamina|script"` to get a quick map. `strings` is part of binutils (MISSING — use python fallback if binutils unavailable).
5. **Tooling that IS available without install**: python3 stdlib (zipfile, hashlib, json, sqlite3, struct, re — can parse APK zip, read AndroidManifest binary XML via 3rd-party `androguard` if needed; `pip install androguard` works because pypi.org is on the allowlist), node (for any JS tooling if needed).

## Workflow (batched)
1. **S0** — record APK hash, version code, signing certificate hash (to confirm build matches B-001 / CLAIM-048).
2. **S1** — manifest + permissions + activity inventory (confirm no hidden telemetry endpoints beyond what the ToU implies; identify the main activity for Step 3).
3. **S2** — resources/values/strings.xml pull for official in-game terminology (confirms or corrects T-001…T-033 from primary source instead of community).
4. **S3** — assets/ file listing + database schema walk; prioritize player/coach/event/formation tables.
5. **S4** — code search for known constants from the KB (Form Boost duration, coach rarity weights, season length, DLL tier XP thresholds, coin rates).
6. **S5** — targeted decompile of classes that hold the constants; record findings as new claims with Confirmed (datamined) tier and file:line anchors.
7. **S6** — write a `step2_work/FINDINGS.md` with before/after deltas vs the KB; flag every place the APK contradicts a community or web claim (these are conflict records, not silent overwrites).
8. **S7** — drop the working tree before committing large binaries; commit only findings, file listings, hashes, and small extracted tables (CSV/JSON under `step2_data/`). Use Git LFS if needed; stay under the 128 MB patchset cap.

## Datamining outputs vs. Step 5 coaching
Step 2 produces parameters, not plays. The deliverable is:
- Verified constants (rate tables, thresholds, hidden weights) that operational rules can cite.
- Corrected terminology and position/formation schema.
- Anti-tilt surfaces (CLAIM-121 Multiplayer Chat toggle, CLAIM-120 Descriptive Button Text, CLAIM-128 backup status) confirmed from UI layout XML.

Step 2 does NOT produce:
- A "best formation", "best players" list, or a mechanical "win every match" script. Those depend on the player's squad, tier, and opponent behaviour, which is Step 5 work.
- Any exploit or manipulation technique.

## Step 2 is NOT a prerequisite for Step 3 or first contact
The Step 3 device pipeline (screenshots, settings readout, manual observation per `IN_CLIENT_CHECKLIST.md`) can run entirely from installed-client observation and does not require the APK to be decompiled. First contact should NOT wait for Step 2 tooling; OBS-013 is resolved by user consent, not by sandbox capability.
