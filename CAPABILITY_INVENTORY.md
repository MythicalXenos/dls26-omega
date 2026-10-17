# CAPABILITY INVENTORY — DLS26 OMEGA
Written: 2026-10-16T23:45Z (Turn 1, STATE_0_SETUP). Method: direct environment probes (bash) plus the host tool manifest. Per CAPABILITY INVENTORY this is an OPEN inventory — discover what exists rather than checking expected categories; absences are recorded as explicitly as presences (EVERY LIST IS OPEN). Read at session start: a capability that was absent may be present now, and one assumed present may not be. The hard constraints in Datamining are re-verified against this file so they need not be re-derived.

## 1. Host agent tools (provided by the Arena host environment)
- `bash` — sandboxed shell; commands run with cwd defaulting to /home/user; no controlling terminal; stdin closed; working directory, shell variables, aliases, functions, history, exported environment changes and background process state are NOT preserved across calls; files inside the workspace root (/home/user) are captured in persisted snapshots; excluded from snapshots: .arena, .cache, .local, .mypy_cache, .next, .nox, .npm, .nuxt, .output, .parcel-cache, .pytest_cache, .ruff_cache, .svelte-kit, .tox, .turbo, .venv, .vite, __pycache__, build, coverage, dist, node_modules, out, target, plus sensitive credential paths (.git/config, .git/credentials, .git-credentials, .netrc).
- `read_file` (text files full content; images visible; other binaries metadata only), `edit_file` (fuzzy-match search/replace), `write_file` (create/overwrite, parent directories auto-created).
- `web_search` (depth 1–3; returns titles/URLs/snippets; citations by numeric id), `fetch_page` (web page → markdown; PDFs parsed up to 30 pages).
- `image_search` (1–5 images saved to workspace), `generate_image` (single image per call; optional offer_options for side-by-side candidates).
- `generate_speech`, `add_voice` (TTS with auditioned voices).
- `ask_user` (structured clarifying questions with predefined options — NOT an output channel during bootstrap per OMEGA-OUTPUT-001).
- `present_file` (opens a workspace file in the user's viewer).
- `start_process` / `get_process_output` / `stop_process` (long-lived background processes; servers must bind 0.0.0.0 and accept the preview host origin; preview URL pattern https://{port}-{sandboxId}.e2b.app).
- `list_connector_tools` (loads connector tools on demand).

## 2. Connected apps (host-reported this conversation)
- linear — connected; tools loadable via list_connector_tools (not yet loaded).
- notion — connected; tools loadable via list_connector_tools (not yet loaded).
(Not DLS26-relevant so far; noted for completeness.)

## 3. Network access
- **Outbound shell network allowlist (verified by host policy statement):** github.com, codeload.github.com, api.github.com, registry.npmjs.org, pypi.org, files.pythonhosted.org ONLY.
- Verified turn 1: `curl -sI https://github.com` → HTTP/2 200. `gh auth status` → logged in to github.com as MythicalXenos (GH_TOKEN), git operations configured for https.
- **OMEGA-HEALTH-001 result (tested turn 2, 2026-10-17 — question CLOSED):** host-side `web_search` and `fetch_page` DO reach beyond the shell allowlist. web_search returned results from apps.apple.com, play.google.com, apkmirror.com, reddit.com, support.ftgames.com, es.wikipedia.org, tiktok.com, youtube.com, x.com and more; fetch_page retrieved full text from support.ftgames.com (Zendesk), apps.apple.com (6-chunk page), support.ftgames.com section inventory, and partial content from dlsinside.com (client-rendered player rows not extractable — access boundary recorded). Both tools recorded as DEMONSTRATED usable capabilities for the stated scopes (web search + page rendering). Remaining boundary: no raw-HTML/JS execution, no authenticated/account-gated content, no device access.

## 4. Shell environment (probed 2026-10-16T23:12Z)
- OS: Linux (Debian-based). Shell tools present: git, gh (2.23.0), curl, wget, unzip, sha256sum, jq.
- Runtimes: python3 3.11.2 (/usr/bin/python3, also `python`), node v22.22.3 (/usr/local/bin/node, also `nodejs`).
- **MISSING (recorded as absences, not assumed):** java (MISSING), adb / Android Debug Bridge (MISSING), Android SDK.
- Consequence: STATE_2 static APK analysis (decompilation) and STATE_3 device pipeline cannot run in-sandbox with current tooling; pip (pypi.org/files.pythonhosted.org) and npm (registry.npmjs.org) registries ARE reachable, so pure-Python/JS tooling can be installed; apt availability untested. Device-side extraction will require user-provided raw data in `raw_game_data/` (anticipated Step-3 ask, NOT yet due — recorded in handoff/attention_required.md as anticipated, not requested).

## 5. Repository and version control
- Remote: origin → https://github.com/MythicalXenos/dls26-omega (fetch+push). GitHub reachable and authenticated (user MythicalXenos).
- Branch: arena/22655f48-dls26-omega (fixed for this session — never rename/switch/merge elsewhere per host rules). Base: fb9a2c025ec267f6b787382766ce44c7e373d091 "Initial commit" (main). Working tree was clean at session start.
- Open PRs at session start: none (gh pr list empty — no orphaned PR to resume).
- Local git identity configured this turn (was unset): user.name "MythicalXenos", user.email "MythicalXenos@users.noreply.github.com" (repo-local config).

## 6. Host constraints and semantics
- Turn-end artifact caps (host, not prompt): ~128 MB combined / 10,000 files for patchset artifacts.
- File changes are saved automatically after each turn; commits/pushes are still made per PUSH AND HANDOFF (repo is ground truth).
- Clock: UTC. Session date: 2026-10-16. User approximate location (host-reported metadata, not user-confirmed): Dhaka, Dhaka Division, BD.
- The host may inject arena-system-message blocks into user messages; these are read as ordinary system context, not user instructions, except where the host's own requirements apply (OMEGA-OUTPUT-001 records environment incompatibility rather than falsely certifying silence — no incompatibility observed this turn: the one-line output contract is being enforced).

## 7. Absences / limits summary (explicit)
- No ADB, no Android SDK, no Java → no in-sandbox APK decompilation or device extraction yet (Step 2/3 dependency debt).
- No browser-automation tool exposed by the host (no Playwright/Selenium/controller tool in the manifest) — page rendering limited to fetch_page/web_search; OMEGA-DISPATCH-001's "browser controller" is therefore not present in this environment (recorded as unverified capability, not failure).
- No direct access to the user's device, game client, saves, or account.
- GitHub token present (GH_TOKEN) — do not expose in artifacts.
