# docs/CAPABILITY_INVENTORY.md — observed environment capabilities and limits

Session: sess-bb22126f679b | Branch: arena/a7e23a6b-dls26-omega | Observed: 2026-10-10T17:33:23Z (UTC, real clock via `date -u`)

This inventory records ACTUAL observed capabilities and limits for OMEGA-DEVICE-001 /
OMEGA-BUDGET-001 planning. Software feasibility ≠ authorization. Nothing here is a claim
about the user's Mac or phone. No claim in this file is a game fact.

## 1. Host platform

- Arena.ai Agent Mode coding agent in a cloud sandbox (hostname `e2b.local`), NOT the user's
  Mac or phone. Sandbox loopback cannot reach user machines; no verified-bridge service is
  present, so publication is verified by ordinary git push + `ls-remote` only, and any
  browser-side cue is treated as agent attestation (standalone mode).
- OS: Debian GNU/Linux 12 (bookworm), Linux 6.1.158+, x86_64.
- Resources (observed): 2 vCPU, ~3.8 GiB RAM, ~20 GiB free disk at /
- Tool interface (host calls): `bash` (sandboxed shell), `read_file`, `write_file`,
  `edit_file`, `web_search`, `fetch_page`, `image_search`, `generate_image`,
  `generate_speech`, `add_voice`, `ask_user`, `list_connector_tools`, `start_process`,
  `get_process_output`, `stop_process`, `present_file`.
- Telemetry note (OMEGA-BUDGET-001): the inherited dossier figure of a "six-call
  environment" is treated as a conservative launch configuration. Observed in turn 1:
  parallel batching of independent host calls works and no six-call hard cap was enforced
  before call 7; per-turn host-call, bash-subprocess and underlying-retrieval counts are
  recorded in `logs/turn_manifest.json`. Do not relabel hidden work as free.

## 2. Version control / publication

- `git` 2.39.5, `gh` 2.23.0; GitHub authentication preconfigured (never request or store
  credentials; never log tokens).
- Repository: https://github.com/MythicalXenos/dls26-omega.git
- Working branch (fixed for this session): `arena/a7e23a6b-dls26-omega`, based on `main`
  @ fb9a2c025ec267f6b787382766ce44c7e373d091 ("Initial commit"). Only this branch may be
  pushed. Ordinary push + remote verification available; force-push forbidden by policy.
- Workspace root (persists across turns): /home/user/dls26-omega

## 3. Network

- Direct sandbox egress (bash `curl`, `git fetch`, package installs) is allowlisted to:
  github.com, api.github.com, codeload.github.com, registry.npmjs.org, pypi.org,
  files.pythonhosted.org.
- Web research is performed through the host `web_search` and `fetch_page` tools, which are
  not limited to the sandbox egress list. Search snippets are evidence of visible content
  only (OMEGA-EVIDENCE-001).
- Downloads from outside the allowlist are possible only via `fetch_page` (text/PDF ≤30
  pages); arbitrary binary/APK download is NOT currently demonstrated. Reassess in Step 2.

## 4. Runtime / analysis tools

- Python 3.11.2 (`python3`, `pip3`; PyPI reachable) — schemas, validators, solvers feasible.
- Node.js + npm available (registry reachable) if JS tooling is needed.
- `unzip`, `tar`, `jq`, `sha256sum`, `curl` present.
- NOT present (as of inventory): java, apktool, jadx, aapt/aapt2, 7z. Static APK analysis
  would require installing tooling (pypi/npm/githost sources) and obtaining authentic
  artifacts — deferred to Step 2 with explicit feasibility recording.
- `/dev/kvm` absent. Per OMEGA-DEVICE-001 this does NOT prove emulation is impossible;
  it also does not imply any specific game runs. No emulator attempt has been made.

## 5. Device / private state access (Step 3 domain, pre-assessment)

- No USB/ADB bridge, no mounted phone storage, no user-Mac filesystem access.
- No spare device or spare account is assumed to exist.
- Device disposition for `logs/control.json`: `UNASSESSED` (Step 3 not reached). Expected
  realistic outcomes: DECLINED or UNAVAILABLE unless the user later provides on-demand
  user-run extraction. Reopening condition: user provides a device route or artifacts.

## 6. Conversational channel (OMEGA-OUTPUT-001 compatibility record)

- The bootstrap/Steps 1–4 single-terminal-line output contract IS implementable in this
  channel: the final assistant message can be exactly the required plain-text line, and all
  findings can live in repository files.
- Host tool-call envelopes and UI metadata are visible to the user as host channel behavior;
  that is outside assistant-authored conversational text. If a future host requirement forces
  assistant commentary (e.g. a required clarification), obey the host, log the incompatibility
  in `logs/issues.jsonl`, and do not certify exact silence (per OMEGA-OUTPUT-001).
- Host tools `ask_user` / `present_file` exist. During silent bootstrap turns they are not
  used as narration channels; indispensable asks go to `handoff/attention_required.md` with
  the matching pause line.

## 7. Identity / binding honesty

- No host-provided conversation ID or message/request ID is observable via tools. Local
  logical IDs (session/turn/nonce) are generated locally and marked
  `observed_from_host: false` in `logs/control.json` and `logs/turn_manifest.json`
  (OMEGA-CHECKPOINT-001: do not pretend generated IDs were observed from Arena).
- Git identity configured: MythicalXenos <333574927+MythicalXenos@users.noreply.github.com>.

## 8. Known limits carried as debt

- Binary artifact acquisition path (Step 2) not yet demonstrated in this sandbox.
- "Six-call" harness figure not yet reconciled with observed batching (telemetry debt).
- No external reviewer exists yet; all audit/verification packages remain unreviewed debt
  (OMEGA-GATES-001 gate 9).
- Public build/version of DLS26 unknown at Setup time; establish in Step 1 research.
