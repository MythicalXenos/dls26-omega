# CAPABILITY INVENTORY — DLS26 Omega

**File role:** second file written in the bootstrap (after `PROMPT.md`), per STATE_0_SETUP in PROMPT.md §13.
**Purpose:** what this environment can and cannot do. Read at every session start. It is the artifact the Hard Constraints On Your Own Capabilities (PROMPT.md §6) are re-verified against, and the source of the role-name bindings used everywhere else in the repo.
**Inventoried:** 2026-09-27 (session 1, turn 1) by direct tool execution — every row below is the output of a command or tool call run in this session, not recall.
**Method note:** inventory was performed by discovery (probing what exists), not by checking a list of expected categories. Absences are recorded as explicitly as presences.

---

## 1. ROLE BINDINGS (used everywhere else in this repo)

The prompt names roles, not tools. These are the bindings for this environment:

| Role name | Bound to in this environment | Status |
|---|---|---|
| **page-render** | `fetch_page` tool (fetches a URL, returns markdown-ized content; parses PDFs up to 30 pages; supports chunked reads) | CONFIRMED WORKING — retrieved `https://www.firsttouchgames.com/games` (HTTP success, full text) even though the shell role cannot reach that host |
| **discovery-search** | `web_search` tool (returns titles, URLs, content snippets; depth parameter 1–3) | CONFIRMED WORKING — returned 3 results for a DLS26 version query |
| **shell/script** | `bash` tool (sandboxed Linux shell, cwd default `/home/user`, max timeout 1800 s) | CONFIRMED WORKING, network-restricted (see §4) |
| **workspace file tools** | `write_file`, `edit_file`, `read_file`, `present_file` | CONFIRMED WORKING (`write_file` used for `PROMPT.md` chunk 1 and this file) |
| **background process** | `start_process` / `get_process_output` / `stop_process` (long-lived servers, preview proxying) | AVAILABLE, not yet exercised; usable for a local HTTP server or long parse jobs |
| **image generation / speech** | `generate_image`, `generate_speech`, `add_voice`, `image_search` | AVAILABLE. `image_search` saves images into the workspace and `read_file` can view them — this is a viable route for reading screenshots of game UI found on the web |

No subtitle/transcript extraction tool exists as a first-class capability. Feasible substitutes recorded in §6.

---

## 2. HOST, OS, RESOURCES

| Item | Value | Verified by |
|---|---|---|
| Kernel / OS | Linux 6.1.158+ x86_64, Debian GNU/Linux 12 (bookworm), host `e2b.local` | `uname -a`, `/etc/os-release` |
| Working user | `user` (HOME `/home/user`); passwordless `sudo` available → root reachable | `whoami`, `sudo -n id` → `uid=0(root)` |
| CPU | 2 cores | `nproc` |
| RAM | 3.8 GiB total, ~3.6 GiB available, no swap | `free -h` |
| Disk | `/dev/root` 21 GB total, 813 MB used, 20 GB free | `df -h` |
| Workspace root | `/home/user`; repo at `/home/user/dls26-omega` | `pwd`, `ls` |
| Snapshot exclusions | `.git/config`, `.git/credentials`, `.git-credentials`, `.netrc` are NOT persisted between turns; also excluded: `node_modules`, `build`, `dist`, `.venv`, `.cache`, `__pycache__`, etc. | platform documentation in system context |
| Consequence of the above | Local `git config` may not survive between turns → **set `user.name`/`user.email` inside the same command as each commit**, and re-verify before every push | derived from exclusion list; re-verify each turn |

---

## 3. LANGUAGES, RUNTIMES, TOOLS PRESENT

Present (version output captured this session):

- **Python 3.11.2** (`python3`, `python`), pip 23.0.1, setuptools 66.1.1, wheel 0.38.4
- **Node.js v22.22.3**, npm 10.9.8
- **git 2.39.5**, **gh 2.23.0** (authenticated as `arena-ai-coding-agent[bot]` via `GH_TOKEN`; `gh api` confirmed working)
- **curl 7.88.1** (TLS 1.3, brotli, zstd, HTTP/2), **wget 1.21.3**
- **unzip / zip**, **tar**, **gzip**, **xz**, **jq 1.6**, **ripgrep 13.0.0**, **openssl 3.x**
- Python stdlib confirmed importable: `json`, `sqlite3`, `zipfile`, `struct`, `xml.etree.ElementTree`

Installable on demand (verified, not assumed): `python3 -m venv /tmp/venvtest` succeeded and `pip install requests beautifulsoup4 lxml` succeeded inside it → **requests 2.34.2, bs4, lxml available in a venv**. System-wide pip needs `--break-system-packages` (PEP 668); venv is the cleaner route. PyPI is reachable (§4).

---

## 4. NETWORK ACCESS — THE SINGLE MOST CONSEQUENTIAL CONSTRAINT

The **shell role** has a restricted egress path. Direct `curl` results (HTTP code, 2026-09-27):

| Host | Result | Meaning |
|---|---|---|
| `github.com` | 200 | reachable |
| `api.github.com` | 200 | reachable (`gh api` works) |
| `codeload.github.com` | 200 | reachable → **GitHub repo tarballs/zips ARE downloadable** |
| `pypi.org` | 200 | reachable → pip installs work |
| `objects.githubusercontent.com` | 000 / 302 with `size=0` | **GitHub release assets and LFS objects are NOT downloadable** |
| `raw.githubusercontent.com` | 000 | blocked → use `api.github.com/repos/.../contents/...` (base64) instead, confirmed 200 |
| `www.google.com` | 000 | blocked |
| `deb.debian.org` | 000 | blocked → **`apt-get update`/`install` does not work**; no OS packages can be added |
| `www.firsttouchgames.com` | 000 | blocked from shell (reachable via page-render) |
| `sakibpro.com` | 000 | blocked from shell (page-render untested on this host — owed) |
| `play.google.com`, `apps.apple.com` | 000 | blocked from shell (page-render owed) |
| `reddit.com`, `youtube.com`, `tiktok.com` (not probed), `facebook.com` (not probed) | 000 for the two probed | blocked from shell (page-render owed) |
| `apkpure.com`, `apkmirror.com` | 000 | blocked from shell — relevant to APK acquisition (§7) |
| `duckduckgo.com`, `html.duckduckgo.com` | 000 | blocked |
| `web.archive.org` | 000 | blocked from shell (page-render owed) |
| `r.jina.ai`, `cdn.jsdelivr.net`, `repo1.maven.org` | 000 | blocked |
| `/dev/kvm` | does not exist | no nested virtualization |

**Conclusion (recorded once, as a network-access gap, per PROMPT.md §5 WALL-BREAKING):** the shell role's egress is limited to the GitHub family (github.com, api.github.com, codeload.github.com — excluding release-asset and raw-content CDNs) and pypi.org. Every other class of host is unreachable *from the shell*. This is a property of the sandbox, not of any source.

**This is NOT a wall-source declaration.** The page-render and discovery-search roles are not subject to this restriction — `fetch_page` successfully retrieved `firsttouchgames.com` in the same turn that `curl` returned `000` for it. Therefore:

- Sources must never be declared inaccessible on the strength of a shell `000`. Each must be attempted through page-render (and discovery-search for cache/snippet extraction) before any wall-source entry is written.
- The gap that genuinely bites is **binary download**: page-render returns text/markdown, not bytes, so it cannot fetch an APK, a ZIP, or an image file into the workspace. `image_search` is the one exception (it saves images to disk). Binary acquisition is therefore limited to what is retrievable from `codeload.github.com`, `api.github.com` contents, or `pypi.org`. See §7.

---

## 5. REPOSITORY ACCESS — verified separately per operation

| Operation | Result |
|---|---|
| Local clone | `/home/user/dls26-omega`, branch `arena/01a0e3cd-dls26-omega` (branched from `main` @ `fb9a2c0` "Initial commit"), clean tree |
| Prior state | Repo contained only `.gitignore` (4628 B) and `README.md` (135 B). **No handoff, no KB, no logs, no prior PR** → this is genuinely a first session; FIRST SESSION BOOTSTRAP is correctly triggered per PROMPT.md §8 POST-COMPACTION |
| Read remote | works (`git remote -v`, `git branch -a` show `origin/main`) |
| Write/commit | to be exercised this turn (first commit = `PROMPT.md` + this file) |
| Push | to be exercised this turn |
| PR | `gh` authenticated as `arena-ai-coding-agent[bot]`; PR creation to be exercised this turn |
| Session branch rule | All work commits to `arena/01a0e3cd-dls26-omega` only; PRs opened from it; no other branch is created, pushed to, or switched to |

---

## 6. CAPABILITIES ABSENT (recorded as explicitly as presences)

| Absent capability | Evidence | Consequence | Workaround available? |
|---|---|---|---|
| Java runtime (`java`, `javac`) | `command -v` → not found; `apt-get` blocked so it cannot be installed | `apktool`, `jadx`, `aapt`/`aapt2` cannot run even if obtained | Yes — pure-Python APK/DEX/AXML analysis (e.g. `androguard` via pip; PyPI is reachable). Feasibility must be *tested*, not assumed, when Step 2 begins |
| `adb` | not installed, not installable | no device interaction from the sandbox at all (consistent with PROMPT.md §6 hard constraint: no path to the user's devices) | None — device work is user-side by design (Step 3) |
| Android emulator / KVM | `/dev/kvm` absent; unprivileged container | cannot install or run DLS26; cannot link a profile; cannot observe play | None. Hard constraint confirmed by inventory |
| `ffmpeg`, `yt-dlp` | not installed | no local video/audio processing, no direct subtitle download via yt-dlp | `yt-dlp` is pip-installable (PyPI reachable) but its network targets (youtube.com) are shell-blocked → transcript retrieval must go via page-render of transcript-bearing pages, or `yt-dlp` remains untested-until-proven. **Record as an open capability question, to be tested in Step 1** |
| `sqlite3` CLI | not installed | — | Python `sqlite3` module works |
| `7z` | not installed | some archives may not open | Python `zipfile`/`tarfile` cover APK (ZIP) and tarballs; 7z-only archives would be a gap |
| Browser automation (Playwright/Selenium/Chromium) | not installed; npm registry reachability untested | no headless rendering, no JS execution, no network-panel capture from the shell | page-render covers JS-heavy page *reading*; it does not cover interaction or request capture |
| Any path to the user's LAN, phone, or MacBook | no route exists; shell egress is a filtered allowlist | device-side extraction must be run by the user and pushed to the repo | By design — Step 3 pipeline |
| Outbound mail / notification | none | cannot contact an external verifier directly | Mechanism 9 packages are prepared and surfaced; sending is the user's decision |

---

## 7. IMPLICATIONS FOR THE BOOTSTRAP STEPS

**Step 1 (research sweep):** fully supported. discovery-search for query expansion and frontier discovery; page-render for every URL including JS-heavy databases; `image_search` + `read_file` for screenshots of game UI; shell for parsing/normalising whatever the tools return and for GitHub-hosted data (community datamining repos, data dumps committed to git) via `codeload`/`api.github.com`.

**Step 2 (static analysis / APK):** constrained. Direct APK retrieval from apkmirror/apkpure/uptodown/Google Play is shell-blocked and page-render cannot return binaries. Viable routes to attempt, in order: (a) GitHub-hosted APKs or extracted asset archives committed inside repos → `codeload.github.com` tarball or `api.github.com` contents (base64 → decode); (b) community datamining repos with already-extracted stat tables/CSV/JSON; (c) PyPI-installed pure-Python APK parsers if a binary is obtained; (d) databases and community dumps as the fallback explicitly authorized by PROMPT.md §13 Step 2 ("record this explicitly as an environment retrieval boundary"). Whether a real APK is reachable is an open question to be tested, not assumed in either direction.

**Step 3 (device pipeline):** the deliverables are scripts and documentation the user runs on their own hardware — fully supported by the file and shell roles (write, test what can be tested locally, e.g. shell syntax checking; cannot test against a real device).

**Step 4 (volatility model, operational rules, audit package):** fully supported — pure file work over the KB and logs.

---

## 8. TURN / SESSION MECHANICS OBSERVED

- `bash` calls: default timeout 30 s, max 1800 s; each call is independent (no preserved shell state, no background survival) → long jobs must use `start_process` or be split.
- Parallel tool calls are supported and were used this turn (independent probes issued in the same block).
- Files under `/home/user` are snapshot-persisted between turns except the excluded names in §2; the repo is additionally pushed to GitHub, which is the source of truth.
- The environment injects no autonomous scheduler: **nothing runs between turns and nothing claims to.**

---

## 9. RE-VERIFICATION TRIGGERS

This inventory is re-checked at every session start and whenever: a command fails in a way that suggests a capability changed; a new tool appears; GitHub auth fails; a host that was blocked becomes reachable; or Step 2 needs a binary-acquisition route that §4 says is closed. A capability found present that §6 lists as absent is a reason to re-read PROMPT.md §6 Hard Constraints, since a stale "cannot" stops work that is now possible.

*Last verified: 2026-09-27, session 1 turn 1.*
