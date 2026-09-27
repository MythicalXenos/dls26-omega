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

### PROPOSED — Mechanism 5: a direct-origin tier for first-party/self-evident claims
**No version number, no "supersedes" field** — per WHO MAY CHANGE THIS FILE. The rule continues to be followed exactly as written until adopted.

**What the current rule gets wrong, with evidence:** Mechanism 5 sets High Confidence at "minimum 2 independent sources" while the same section states "the count is never what makes a claim true. What makes it true is that the origin rests on something checkable". Applied literally, a claim read directly out of a first-party document — FTG's own store listing, changelog, or support page — is capped at **Speculative** unless some *second party* happens to have extracted the same fact independently, because two surfaces of one origin count as one source and an aggregator echo counts as none. Evidence from this session: the package id `com.firsttouchgames.dls7` appears in FTG's own outbound store link and in FTG's own listing URL, is directly checkable by anyone at that URL, and cannot be tiered above Speculative under the count gate (ISS-005, revision R-0001). The cap then understates the most checkable class of evidence in the whole system, and the KB ends up ranking a first-party document below three unrelated forum posts agreeing with each other (Community Consensus, 5+ members).

**Proposed change (for the user to accept, reject, or rewrite):** add to Mechanism 5 a distinct tier or an explicit exemption — e.g. "**Direct-Origin (first-party/self-evident): a claim whose origin is a document or datum read directly from the party that authored it, or from the thing itself, with no interpretive step, is recorded at High Confidence regardless of source count, provided the origin is checkable by a third party at a recorded location and no contradicting source exists. It never reaches Confirmed on that basis alone; Confirmed still requires 3 independent sources.**" Keep the deception re-screen (PLANTED AND DECOY DATA applies to FTG too) and keep requiring that marketing claims *about game behaviour* remain Speculative — the exemption would cover what a document says, not what the game does.

**Cost of not adopting it:** none to safety; the conservative cap stays. Cost is informational — the KB's tiers stop discriminating between "one unreliable blog" and "the publisher's own document", which is a distinction every downstream decision would benefit from.

**Status:** PROPOSED 2026-09-27, session 1. To be surfaced to the user at first contact (Step 5) or earlier if it begins to affect an active decision. Until then the count gate is followed as written.

## Verification note on v1.0 transcription

The prompt was transcribed from the conversation into `PROMPT.md` in four committed chunks (write_file + three quoted-heredoc appends), then checked: all 13 numbered sections present and in order (`grep -n` over section headings), plus the INITIALIZATION DIRECTIVE preamble. One transcription slip was found and corrected during that check — §10 CANDIDATE POOL "PER-SLOT BOUND **proved**" → "**proves**" — logged as ISS-001. No other divergence was detected by that check; the check is heading-level plus targeted spot-reading, not a byte-for-byte diff against the original message, which is not mechanically possible from inside the session. Recorded as a limitation, not as a clean result.
