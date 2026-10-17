# PROMPT CHANGELOG — DLS26 OMEGA

## Version 78 — captured 2026-10-17T16:45Z (this session)
- Change: full mechanical capture of the v78 prompt as delivered in this session.
- Size/SHA-256: 175,596 bytes / b7fd30da008740723e62241002a447adf2ccda57fc23a68da4bb1f6b8db6dd7b.
- Archive: docs/prompt_archive/OMEGA_PROMPT_v76.md (literal mandated path) and docs/prompt_archive/OMEGA_PROMPT_v78_2026-10-17.md.
- Reason/trigger: new workspace, no completed handoff on this branch; PROMPT PERSISTENCE MANDATE.
- Supersedes: no prompt text was edited. This capture supersedes the prior session's 173,446-byte capture labelled v78 (OBS-007), which is retained at docs/continuity/22655f48/DLS26_OMEGA_PROMPT_173446B.md.
- Regression checks: 25/25 OMEGA-RULE blocks balanced; 25 unique rule IDs; six terminal strings present; byte count and hash re-computed from disk.
- Continuity: prior v78 work on arena/22655f48-dls26-omega imported (see docs/continuity/22655f48/ and handoff).

## Prior history
- v76/v77/v78 history from earlier sessions is retained at docs/prompt_changelog.md (imported 2026-10-17) and in the archived copies referenced there.

## PROPOSED (not adopted) — Step 2 redefinition — 2026-10-17
- **Rule affected:** HARD STATE BOUNDARY RULE, `STATE_2_STATIC_ANALYSIS` ("Decompilation and static extraction of APK assets, stat tables, and formation data").
- **Defect evidence:** CLAIM-043 (Confirmed, EULA 25 Jul 2025) prohibits reverse engineering, decompilation and derivative use; CLAIM-017/CLAIM-075 (Confirmed, official sanction policy) state that only App Store / Google Play builds are authorised and that exploitation/unauthorised builds are bannable. Executing Step 2 as written would require an act that the game's own terms make bannable against the user's account — a consequential loss, not a data-quality trade-off.
- **Proposed replacement:** `STATE_2_STATIC_ANALYSIS` becomes *permitted static analysis*: published store metadata and version notes, officially published assets and documents, permitted public APIs, and the user's own screenshots/transcriptions. Explicitly excluded: APK/IPA decompilation, string mining, asset ripping, traffic interception, save editing, memory editing, automation.
- **Affected cross-references:** HARD STATE BOUNDARY RULE, `STEP_2`/Step-3 prep docs, OMEGA-RETRIEVAL-001 (retrieval legality), IRREVERSIBLE ACTION PROTECTION, Mechanism 3 technical-source coverage.
- **Disposition if adopted:** SUPERSEDES the current STATE_2 definition; Step-3 device pipeline unchanged (already user-driven).
- **Regression checks required before adoption:** confirm no other rule depends on decompilation as an evidence source; confirm the technical-source coverage gate can still be satisfied by permitted layers (it can — the gate requires coverage of a source type, not of a prohibited method).
- **Status:** PROPOSED. No version number, no supersedes field, per WHO MAY CHANGE THIS FILE. The rule remains in force as written until the user adopts or rejects.
