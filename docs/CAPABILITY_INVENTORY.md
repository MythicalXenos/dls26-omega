# Capability inventory (Setup, Turn 1)

Observed 2026-10-09 UTC, session a8a92133, workspace /home/user/dls26-omega.
Method: shell probes (uname, /etc/os-release, `command -v` and `--version`, curl HTTP status codes, gh auth status, git config) plus the agent's own tool list. Absences are recorded as explicitly as presences. Re-probe at every session start and record any change in the handoff.

## Sandbox (bash)
- OS: Debian GNU/Linux 12 (bookworm); Linux 6.1.158+ x86_64.
- CPU: 2 cores. Memory: 3939 MiB total, about 3.7 GiB available at probe. Disk: 21 GB root, about 20 GB free.
- Repository: git working tree at /home/user/dls26-omega. Branch arena/a8a92133-dls26-omega (fixed for this session). HEAD at start: fb9a2c0 "Initial commit", branched from main at fb9a2c0. Remote origin: github.com/MythicalXenos/dls26-omega.
- Git identity: user.name and user.email are already configured (MythicalXenos, GitHub noreply address). No change was needed. The configuration scope was not checked.
- GitHub CLI: gh 2.23.0, authenticated as MythicalXenos (token supplied by the environment; never recorded here). No open PR on this branch at probe time.

## Runtimes and tools present
- python3 3.11.2 with pip 23.0.1.
- node v22.22.3 with npm 10.9.8.
- git 2.39.5; gh 2.23.0.
- unzip (Info-ZIP) and zip; tar 1.34 (GNU); xz 5.4.1; jq 1.6.
- curl 7.88.1 (OpenSSL 3.0.20, brotli, zstd, libssh2, nghttp2); wget 1.21.3.

## Absent (recorded explicitly)
- Java runtime (java and javac absent).
- sqlite3, file, xxd.
- Android Debug Bridge (adb absent).
- Android APK tooling: aapt, aapt2, apktool, jadx all absent.
- lsusb absent; no USB device visible.
- /dev/kvm absent: no hardware acceleration, so no Android emulator can run here.
- No Android device or emulator is reachable from the sandbox.

## Network egress from bash (HTTP status at probe)
- Reachable: github.com 200; api.github.com 200; codeload.github.com 301; registry.npmjs.org 200; pypi.org 200; files.pythonhosted.org 404 at the root path (reachable; only the root was probed).
- Blocked: example.com (HTTP 000). This confirms an allowlist. The sandbox policy lists only github.com, codeload.github.com, api.github.com, registry.npmjs.org, pypi.org and files.pythonhosted.org.
- Consequence: APK tooling or a JDK could only come through npm or PyPI packages, and only if such packages exist. Game files, wiki pages and community sources are not reachable from bash. Web research goes through the platform tools below.

## Platform tools (agent-side, outside the sandbox)
- web_search (depth 1–3): discovery; each claim cites its result id and URL.
- fetch_page: retrieves page text in chunks; PDFs are parsed up to 30 pages.
- image_search (saves to the workspace); generate_image (saves .jpg or .png); generate_speech with add_voice (a voice must be registered first). Presence recorded; not needed for Setup.
- start_process, get_process_output, stop_process: background processes with live preview on 0.0.0.0 ports. Not used.
- list_connector_tools: the user has enabled the connectors linear and notion for this conversation. Their tools are not loaded in this turn. The bootstrap does not depend on them, because GitHub is the source of truth.

## Constraints that bound the datamining and device plan
- No Android device, ADB, or emulator is reachable. STATE_3 (device pipeline) therefore needs either the user's device or user-supplied extraction files. Missing device access never authorizes fabricated results.
- No APK decompiler or JDK is installed. Step 2 must first check whether an installable route exists through the allowed registries. Record the result either way.
- Hardware: 2 vCPU and about 3.9 GB RAM. Large decompilation or asset processing will be slow, so work is batched.
- Storage: about 20 GB free. Large datasets stay out of Git unless required (STORAGE MANAGEMENT).
- Web research is limited to what web_search and fetch_page return. No raw store pages or game servers are reachable from bash.

## Agent-declared conduct boundary (not in the prompt text; to be surfaced at STATE_3 for the user's confirmation)
The agent will not build or run tools that modify game files, save data or server data; bypass anti-cheat or licensing protections; intercept live game traffic; or automate gameplay. Read-only analysis of user-owned or user-supplied data is in scope, subject to a ToS and ban-risk assessment at STATE_3.
