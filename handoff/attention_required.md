STEP 2 APK ACQUISITION BLOCKED — ATTENTION_REQUIRED

Step 1 research sweep is closed (saturated). Step 2 requires the actual DLS26 APK (com.firsttouchgames.dls7) for Unity asset/IL2CPP datamine.

Sandbox outbound network is restricted to api.github.com, github.com, codeload.github.com, pypi.org, files.pythonhosted.org, registry.npmjs.org. All APK hosts (Google Play, APKPure, APKMirror, APKMono, Uptodown, Softonic, happymod, mediafire, cdn.jsdelivr.net) and FTG's own servers are TLS-blocked from this environment, as confirmed by repeated probing turns 22–28.

GitHub corpus searched exhaustively: no real DLS26 APK is hosted on any public GitHub repo (releases checked across 7 repos; code search only reveals scanners, false-positive template matches, scam/fan-HTML shells, and one TWA wrapper we already downloaded and discarded as a webview-only shell).

To unblock Step 2, please provide ONE of:
  1. A copy of the com.firsttouchgames.dls7 APK (any current version) uploaded into the workspace, e.g. at /home/user/dls26-omega/apk/dls26.apk;
  2. An expanded APK directory tree (already unzipped) with assets/bin/Data present;
  3. A URL from which the sandbox can download the APK (must be a host matching the allowlist above — Google Play does not work, but an S3/GitHub Releases URL would).

Once the APK (or Unity data directory) is available, Step 2 will proceed:
  - Unzip APK, extract unity builtin data + global-metadata.dat
  - Use strings/binwalk/assetstudio (pip UnityPy available offline? verify)
  - Dump asset bundles (sharedassets, resources.assets, data.unity3d)
  - Extract player-stats tables, OVR constants, coach tables, card definitions, formation data, event tables, matchmaking constants
  - Cross-validate/refute OVR formula from EV-253; confirm GK attribute labels; enumerate non-CB coach weights; validate Dream Points/Form Boost/Season Pass economy
  - Extract save/shared_prefs schema
  - Produce the Step 2 datamine EVs.

No further turns will make progress on Step 2 without an APK. Awaiting user action.
