# Capability Inventory (Setup, STATE_0_SETUP)

Observed: 2026-10-18T15:32:51Z (UTC), by direct command execution in the session sandbox. Re-verify at every session start (capability may appear or vanish).

## Host
- OS: Debian GNU/Linux 12 (bookworm), kernel 6.1.158 (x86_64). Hostname e2b.local.
- CPU: 2 vCPU. RAM: ~3.9 GiB total, ~3.7 GiB available at observation. Disk: /dev/root 21G, 20G free.
- Hardware virtualization: /dev/kvm ABSENT. An Android emulator or any KVM-accelerated VM is not available here. Missing acceleration is not a game-compatibility finding.

## Present (version observed)
- bash 5.2.15; python3 3.11.2; pip 23.0.1 (python3 -m pip); node v22.22.3; npm 10.9.8; npx 10.9.8
- git 2.39.5; gh 2.23.0 (authenticated as MythicalXenos via GH_TOKEN; token not recorded here)
- curl 7.88.1 (OpenSSL 3.0.20); wget 1.21.3; jq 1.6; unzip 6.00; zip (Info-ZIP; version string not captured); tar 1.34; openssl (present)
- git identity configured: user.name MythicalXenos, user.email (noreply address) — first commit will not fail.

## Absent (observed by command -v / --version)
- adb, java, javac, keytool, apktool, jadx, aapt, aapt2, 7z, sqlite3, file, xxd, ffmpeg, git-lfs (not a git command).
- No Android SDK, no device connection, no ADB device. Device-dependent work (STATE_3) is blocked on user-side or on an available device path; it must use ATTENTION_REQUIRED when needed, never fabricated results.

## Network (egress policy observed)
- Allowlisted by host policy (per system configuration): github.com, codeload.github.com, api.github.com, registry.npmjs.org, pypi.org, files.pythonhosted.org.
- Probed this session: github.com 200; api.github.com 200; registry.npmjs.org 200; pypi.org 200.
- Not allowlisted, not reachable from bash: example.com (000), play.google.com (000). Not attempted further; no proxy, mirror or tunnel is used to get around the boundary (OMEGA-RETRIEVAL-001).
- Platform-provided tools (not sandbox networking, a separate capability per OMEGA-RETRIEVAL-001): web_search, fetch_page, image_search, read/write/edit tools, generate_image, generate_speech, add_voice. Declared available; NOT exercised in Setup. Recorded as declared-only.

## Resources and limits
- Host call-count limit: unknown (not exposed to the agent). Recorded as unknown per OMEGA-BUDGET-002.
- Turn wall-clock deadline: the prompt's 420 s (Setup) and 360 s (later turns). Host-enforced limit: unknown.
- Repository: /home/user/dls26-omega; branch arena/357aaddf-dls26-omega; remote origin https://github.com/MythicalXenos/dls26-omega.git. Git LFS absent: large artifacts stay out of Git unless required (see docs/SCHEMA.md storage section).

## Constraints re-verified against Datamining hard constraints
- No device, no emulator, no APK tooling installed. Static APK decompilation (STATE_2) would need an install step (java + jadx or apktool). Installing from pypi/npm only is possible if an equivalent exists on those registries; that is a later step, not Setup work.
- Any datamining must respect the game's ToS and the account-safety rules in the prompt's Irreversible Action Protection; the capability to run it does not authorize it.

## Absences recorded explicitly
- No device access (no ADB device, no emulator).
- No Java runtime (blocks standard Android decompilers).
- No SQLite CLI (python sqlite3 module is available via the python stdlib — not separately verified here).
