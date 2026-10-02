# Issue tracker

## ISSUE-0001 — Prompt capture is incomplete
- **First recorded:** 2026-10-02T11:31:16Z (clock read in this turn).
- **State:** Open / bootstrap-blocking for prompt identity, but does not block unrelated setup or research.
- **Observation:** `DLS26_OMEGA_PROMPT.md` is a capture-status placeholder, not the full unmodified user prompt required by Knowledge Management. No raw-message export tool is exposed in the current tool schema; manual verbatim reproduction was not completed. This is not evidence that manual reproduction or a user-provided text attachment is impossible.
- **Investigation:** The workspace was checked for pre-existing prompt files and no source copy was found. The current conversation contains the text. The failure is therefore a capture/transfer omission, not evidence that the prompt does not exist. No other prompt-capture issues are present in the initial repository state.
- **Impact:** Prompt file cannot serve as a restore source or be mechanically compared to active instructions. Do not rebuild operational rules from it. At first contact, ask the user to supply/confirm a verbatim text file or permit a complete manual capture; preserve current conversation instructions meanwhile.
- **Root cause:** Prompt was not copied into the first file; the assistant substituted a status note. This is an execution defect, not an environment-imposed block.
- **Next:** Resolve before relying on the file for a context reset; update the handoff and changelog only if an adopted prompt amendment actually occurs.
