# ISSUE TRACKER

All problems, errors, bad recommendations, failures, rule deviations, degradation events, saturation entries, word-sense separations, and anything else of that kind (EVERY LIST IS OPEN). Investigated on first occurrence — and what investigation means depends on what the entry reports (PROMPT.md §8 ISSUE TRACKER): entries about the game, a method, a recommendation or a failure are investigated for root cause; entries reporting this system's own state are investigated by comparison against entries sharing the category/pattern and against patterns flagged in recent digests, then judged for whether the pattern bears on advice. Saturation entries are exempt from investigate-on-first-occurrence to prevent administrative death-spirals.

Format: SCHEMA.md §2.4.

---

### ISS-001 — Transcription slip in PROMPT.md §10 CANDIDATE POOL  [RESOLVED]
opened: 2026-09-27T17:18Z | kind: failure (own output)
report: While writing PROMPT.md verbatim, "only when the PER-SLOT BOUND **proves** that the excluded candidate…" was transcribed as "**proved**".
investigation: Root cause = manual chunked transcription of a ~228 KB document with no mechanical diff available against the original message. Caught by the post-write verification pass (heading grep + targeted spot-reading of rule-critical sentences). Fixed in place with an asserted string replacement (assert-on-miss, so a silent no-op was impossible).
resolution: Corrected; verified by grep (1 match for the correct wording). Preventive measure adopted: every chunk write is followed by a targeted read-back of rule-critical sentences, and the limitation is recorded in prompt_versions/CHANGELOG.md rather than presented as a clean byte-for-byte result.
saturation_exempt: false

### ISS-002 — Shell-role network egress is an allowlist, not open internet  [OPEN — environmental, not fixable from inside]
opened: 2026-09-27T17:04Z | kind: environment/capability
report: `curl` from the shell returns HTTP 000 for every DLS-relevant host (FTG, SakibPro, Play, App Store, Reddit, YouTube, APKPure, APKMirror, Wikipedia, DuckDuckGo, Wayback, jsDelivr, Maven) and for objects.githubusercontent.com / raw.githubusercontent.com, while github.com, api.github.com, codeload.github.com and pypi.org return 200.
investigation: Root cause = sandbox egress filtering, a property of the environment rather than of any source (apt is also blocked, so no tooling can be added at OS level). Directly probed with a desktop User-Agent and a 10 s timeout; the same host (firsttouchgames.com) that returned 000 from the shell was fetched successfully by the page-render role in the same turn, which proves the barrier is the shell's egress path and not the source. Bypass attempts made and their results: page-render = WORKS (the primary bypass); discovery-search = WORKS; custom UA = no effect on the blocked hosts; jina reader proxy = blocked; GitHub API contents route = WORKS (base64 file contents, bypassing raw.githubusercontent); codeload tarballs = WORKS (bypasses repo-clone needs); GitHub release assets = FAIL (objects.githubusercontent unreachable); pip/PyPI = WORKS (bypasses apt for pure-Python tooling).
resolution: Recorded once as a network-access gap in CAPABILITY_INVENTORY.md §4 with the classes of source affected, per PROMPT.md §5 WALL-BREAKING (report once per cause, not once per source). Standing consequence enforced repo-wide: no source may be declared a wall source on the strength of a shell 000 — page-render and discovery-search must be attempted and failed first. Remaining genuine gap: binary acquisition (APK/ZIP/image bytes) is limited to codeload, GitHub API contents, PyPI, and image_search. Bears on advice: yes — it constrains Step 2's datamining depth, so it is carried in the handoff and will be surfaced at first contact rather than discovered later.
saturation_exempt: false

### ISS-003 — Prompt-file fidelity cannot be mechanically verified from inside the session  [OPEN — limitation, disclosed not fixed]
opened: 2026-09-27T17:28Z | kind: system-state / verification-limit
report: PROMPT.md is the behavioural authority, and it was produced by manual transcription from the conversation. No byte-for-byte diff against the original is possible from inside the session, because the original exists only in context.
investigation: Comparison against existing entries of the same kind: this is the first entry of its kind; no prior pattern exists. What was done instead: section-heading grep confirming all 13 numbered sections plus the INITIALIZATION DIRECTIVE are present and in order; byte/line count recorded (228,491 B / 842 lines); targeted spot-reading of rule-critical sentences (which caught ISS-001); v1.0 archived as an immutable baseline so any later corruption is diffable against a known copy. Does the pattern bear on advice? Not yet — no advice has been delivered. It bears on behaviour, which is why it is disclosed in prompt_versions/CHANGELOG.md rather than reported as a clean result.
resolution: Held open as a standing limitation. If the user can supply a checksum or a canonical copy, PROMPT.md should be diffed against it and this entry closed; that ask is batched into the first-contact ask rather than raised separately (carry-the-load).
saturation_exempt: false

### ISS-004 — `.git/config` is excluded from turn snapshots, so local git identity may not persist  [OPEN — mitigated]
opened: 2026-09-27T17:29Z | kind: environment
report: The platform excludes `.git/config` (and other credential paths) from persisted snapshots. Local `user.name`/`user.email` were already set by the clone environment (MythicalXenos / 333574927+MythicalXenos@users.noreply.github.com), but may not survive between turns.
investigation: Root cause = snapshot exclusion list, not a git or auth fault. A failed identity would surface as a rejected commit mid-session, which would put the "push before every turn ends" rule at risk — the highest-cost failure mode available here, because PROMPT.md §8 THE CONVERSATION IS MORTAL makes the last successful commit the only guaranteed terminal state.
resolution: Mitigation adopted — every commit command re-asserts `git config user.name`/`user.email` inline before committing, and push success is verified (not assumed) by reading back the remote ref. Re-verify at each session start.
saturation_exempt: false
