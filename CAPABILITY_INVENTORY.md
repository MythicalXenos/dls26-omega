# CAPABILITY INVENTORY — DLS26 OMEGA
Observed: 2026-10-17T16:51:01Z (UTC), sandbox environment. Method: direct probes recorded below and in `logs/sources_visited.json` (now S-20261017-070..073 after the turn-16 namespace repair, OBS-017). Absences are recorded as explicitly as presences; nothing here is assumed on a later environment without re-checking (OMEGA-HEALTH-001).

## Present and verified this environment
- Linux x86_64 (kernel 6.1), 2 vCPU, 3,939 MB RAM, 20 GB free on /, no swap pressure observed.
- Python 3.11.2; pip 23.0.1; Node.js v22.22.3; npm 10.9.8.
- git 2.39.5; GitHub CLI 2.23.0 authenticated as MythicalXenos (HTTPS token); `git ls-remote origin` succeeded.
- curl 7.88.1, jq 1.6, unzip, ImageMagick `convert`, `gh`.
- File read/write/execute in /home/user/dls26-omega; git commit/push to origin.
- Network reachability observed: api.github.com 200, registry.npmjs.org 200, pypi.org 200. Host policy permits only github.com, codeload.github.com, api.github.com, registry.npmjs.org, pypi.org, files.pythonhosted.org.
- Long-lived background processes and TCP preview ports are supported by the host tooling; no web browser or GUI inside the sandbox.

## Absent or unverified
- java, adb, apktool, jadx, aapt: ABSENT. Android SDK env vars unset. No device or emulator access. Step 2/3 static APK work and save extraction therefore not executable in this sandbox until tooling/device access is supplied or an allowed package route is found.
- git-lfs, ffmpeg, sqlite3: ABSENT (installable only from the permitted registries).
- DISPLAY unset: no GUI browser; no direct app-store or in-game observation.
- No official DLS26 API access or credentials; no FTG backend access.
- Outbound web is restricted to the allowlist above; arbitrary game/community sites are not reachable from this sandbox. Any research relying on them requires an available permitted route or must be recorded as access-limited.
- Time: turn wall-clock ceilings apply (420 s Setup / 360 s later turns). Large parallel write batches previously caused a sandbox stream timeout in a prior session (OBS-005); keep write batches small.

## Repository access verification
- Remote: https://github.com/MythicalXenos/dls26-omega.git. Branch: arena/b5d5681d-dls26-omega (from main @ fb9a2c0).
- `gh auth status`: logged in; git HTTPS operations configured.
- Open PRs at setup: NONE. Closed prior bootstrap PRs #1–#5 exist.
- Prior unmerged branches discovered: origin/arena/22655f48-dls26-omega (v78 Setup complete + Step 1 turns 2–4, ckpt-20261017-step1-003) and origin/arena/a7e23a6b-dls26-omega (v77 long research run). Continuity from 22655f48 imported; see handoff and OBS-008.

## Hard constraints carried forward
- No fabricated device/datamining results. Step 2/3 outputs must be labeled as designed-but-unexecuted until tooling exists.
- No external endpoint outside the allowlist; no circumvention via proxies/mirrors.
- Keep generated artifacts and large datasets out of Git unless required; raw game data is read-only input under `raw_game_data/`.
