# PROMPT CHANGELOG

Per PROMPT.md §8 PROMPT VERSIONING and WHO MAY CHANGE THIS FILE.

- Only the user may change PROMPT.md. The agent proposes; it never edits.
- Proposals are written here marked **PROPOSED**, with evidence, **no version number and no "supersedes" field**, and the rule keeps being followed as written until adopted.
- On adoption the entry gets a version number and is rewritten as an adopted change; the outgoing version is archived to `prompt_versions/archive/PROMPT_v{X}_{date}.md` **before** the live file is replaced. The live file keeps one permanent filename (`PROMPT.md`) for the life of the repo.
- Read this changelog before proposing any change: a rule that looks redundant or over-cautious is usually a correction of something that already failed once.

| Version | Date | Change | Reason / prompting finding | Supersedes |
|---|---|---|---|---|
| v1.0 | 2026-09-27 | Baseline. Full prompt as supplied by the user in session 1, written verbatim to `PROMPT.md` (228,491 bytes, 842 lines) and archived as `archive/PROMPT_v1.0_2026-09-27.md`. | First session bootstrap; PROMPT.md must be the first data file on disk | — |

## PROPOSED amendments (not adopted — rules continue as written)

*none yet*

## Verification note on v1.0 transcription

The prompt was transcribed from the conversation into `PROMPT.md` in four committed chunks (write_file + three quoted-heredoc appends), then checked: all 13 numbered sections present and in order (`grep -n` over section headings), plus the INITIALIZATION DIRECTIVE preamble. One transcription slip was found and corrected during that check — §10 CANDIDATE POOL "PER-SLOT BOUND **proved**" → "**proves**" — logged as ISS-001. No other divergence was detected by that check; the check is heading-level plus targeted spot-reading, not a byte-for-byte diff against the original message, which is not mechanically possible from inside the session. Recorded as a limitation, not as a clean result.
