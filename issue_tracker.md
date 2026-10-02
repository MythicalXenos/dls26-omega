# Issue tracker

## ISSUE-0001 — Prompt capture is incomplete and the original text is unavailable in the current compressed context
- **First recorded:** 2026-10-02T11:31:16Z (from the prior setup handoff).
- **State:** Open and blocked on user-provided source; prompt-identity/setup obligation remains unmet.
- **Observation:** `DLS26_OMEGA_PROMPT.md` is a capture-status placeholder, not the full unmodified user prompt required by Knowledge Management.
- **Initial investigation (preserved historical note):** The earlier assistant record said the current conversation contained the full prompt and that manual verbatim reproduction remained possible. It was not copied then; this was recorded as an execution omission.
- **Context update — 2026-10-02T11:47:19Z:** This model turn received only a condensed session summary, not the complete raw original prompt. Exact wording is not visible in the current context and no source file exists in the repository. The prior “available in the conversation” assessment is stale for this context. Do not reconstruct a purported verbatim prompt from the summary.
- **Impact:** The placeholder cannot serve as an authority or rebuild source; exact identity comparison and a trustworthy state-4 reset remain impossible until the full text is supplied.
- **Root cause:** The assistant substituted a status note instead of copying the full prompt during initial setup, then proceeded despite the unmet capture gate; the original text was subsequently omitted from the condensed context.
- **Next:** Ask the user to attach the original `.md`/`.txt` or paste the full prompt. Then store it exactly at the stable path and verify. Until supplied, keep the visible user summary as context only; do not invent missing instructions or continue research.

## ISSUE-0002 — Direct shell HTTPS requests failed
- **First recorded:** 2026-10-02T11:39:15Z.
- **State:** Open capability limitation; alternative retrieval works for the pages tested.
- **Observation:** `curl` with a browser User-Agent failed with `OpenSSL SSL_connect: SSL_ERROR_SYSCALL` and HTTP status 000 for the FTG help center, Apple App Store, Google Play, SakibPro and APKMirror URLs. The matching pages were retrievable with `functions.fetch_page`.
- **Investigation:** Five distinct hosts failed in the same way; the failure is at the sandbox's direct-shell TLS connection layer, not a source-specific page barrier. Search and fetch tools work, so this is not a global network-access gap and none of those pages is a wall on this evidence.
- **Impact:** Raw APK downloads, direct API/JavaScript inspection and shell-based full-page archival may be blocked. Page/search tools remain available; do not re-probe every turn unless the capability/network state changes.
- **Disposition:** Use available page/search retrieval, try alternate technical routes when required, and report direct-shell HTTPS limitation once per cause.

## ISSUE-0003 — Retrieved page payloads not fully archived
- **First recorded:** 2026-10-02T11:39:15Z.
- **State:** Open; source processing remains explicitly partial.
- **Observation:** Long Apple/Google store pages and FTG comments were fetched in chunks and summarized in `source_archive/bootstrap_research_2026-10-02.md`, but their full raw payloads are not stored in the repository. The source ledger records chunk counts and incomplete analysis.
- **Investigation:** `functions.fetch_page` returns payload text in tool output but has no file-save argument. Direct shell `curl` failed on five hosts (ISSUE-0002). Manual archival is still possible, so this is not a source wall; the full payload obligation is staged rather than closed.
- **Impact:** Historical verification and later-session source review are weaker until the raw contents are preserved. No source is described as exhausted; no confidence is promoted on this basis.
- **Next:** Archive full payloads or a complete information-equivalent extraction in source-specific files, sanitize them, and update ledger state. Process unique UGC comments and translations rather than duplicating reaction/spam bytes.

## ISSUE-0004 — STATE_1 research began with STATE_0 prompt capture incomplete
- **First recorded:** 2026-10-02T11:39:15Z.
- **State:** Open procedural deviation; do not hide or retroactively declare STATE_0 fully complete.
- **Observation:** Research-search and page-retrieval actions were run after initial setup records were written while the required full prompt file remained an incomplete placeholder. This did not satisfy the user's strict STATE_0_SETUP → STATE_1_RESEARCH_SWEEP gate.
- **Investigation:** Compared with ISSUE-0001: both share the same root cause (assistant substituted a status note for the prompt capture and proceeded under time/length pressure). The first research results are physically recorded and must be preserved; deleting them would lose work and would not repair the state-boundary failure. No other state-boundary deviation is recorded yet.
- **Impact:** Bootstrap state labels and prompt-based recovery are less reliable; this bears on future advice and must be disclosed at first contact. The handoff records the actual research resumption point and keeps the prompt issue open.
- **Correction:** Keep the prompt defect and unauthorized transition visible; do not claim an exhaustion declaration or a completed bootstrap step. Further research is paused. The current condensed context does not contain the verbatim prompt, so request the original file/text from the user rather than reconstructing it; after it is captured, re-read the operational rules and only then resume from the saved frontier under strict state boundaries.
