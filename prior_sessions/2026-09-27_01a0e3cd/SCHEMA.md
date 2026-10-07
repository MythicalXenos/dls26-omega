# FILE SCHEMA — DLS26 Omega repository

**Authority:** PROMPT.md §8 (Knowledge Management) defines *which* artifacts must exist; this file defines *where they live, what shape they have, and how to read them*. Sessions read this file before interpreting or modifying any persisted artifact.
**Version:** schema v1.0 — 2026-09-27 (STATE_0_SETUP, session 1).
**Change rule:** schema changes require a proposal with explanation, migration plan, and rollback path. The superseded schema version is kept below under *Schema history* — never deleted.

---

## 1. TREE

```
dls26-omega/
├── PROMPT.md                     # LIVE full prompt. Stable permanent filename. Authority for behaviour.
├── OPERATIONAL_RULES.md          # Behavioural reset doc (built in STATE_4). Read at session start + after each major work phase.
├── CAPABILITY_INVENTORY.md       # What this environment can do. Read at session start.
├── SCHEMA.md                     # This file.
├── HANDOFF.md                    # Session handoff. Updated atomically before EVERY turn ends.
├── README.md                     # Repo front page (pre-existing).
├── .gitignore                    # Pre-existing.
│
├── prompt_versions/
│   ├── CHANGELOG.md              # Prompt version history + PROPOSED amendments (proposals carry no version number).
│   └── archive/                  # Archived outgoing prompt versions: PROMPT_v{X}_{YYYY-MM-DD}.md
│
├── kb/                           # KNOWLEDGE BASE — current state of knowledge by topic.
│   ├── README.md                 # KB index + claim-record format + tier legends.
│   ├── user_profile.md           # Everything about the user (state, preferences, playstyle, skill/understanding trackers, spending).
│   ├── disputed_claims.md        # Authoritative list of open Disputed claims. Handoff points here, never enumerates.
│   ├── deception_register.md     # Domains/sources flagged by the deception screen. Never cleared.
│   ├── irreversible_action_list.md # Game knowledge: every irreversible/consequential action type found by research.
│   ├── watchlist.md              # Players monitored per the Watchlist rule.
│   ├── volatility_model.md       # Volatility tiers, per-claim dimensions, impact weighting, observed FTG change patterns.
│   ├── gaps.md                   # Open gaps and closed gaps (negative findings), two states kept distinct.
│   ├── milestone_tracker.md      # Targets, distances, resource requirements.
│   └── topics/                   # One file per research topic. Filename = topic slug, lowercase-hyphenated.
│       ├── terminology_and_abbreviations.md   # Resolution of prompt shorthand → exact in-game terms.
│       ├── game_identity_and_version.md       # Package, version history, patch cadence, rebrand continuity.
│       └── ...                                # Grows with the research; no predetermined shape.
│
├── logs/
│   ├── sources_visited.json      # MACHINE-READABLE registry of every fetch. Physical basis of every exhaustion declaration.
│   ├── sweep_tracker.md          # Human-readable frontier state for the running sweep (source types × languages × layers, leads).
│   ├── main_operational_log.md   # Timestamped ground truth, by category. Rotated to main_operational_log_NNN.md.
│   ├── issue_tracker.md          # Problems, failures, deviations, degradation events, saturation entries, word-sense separations.
│   ├── revision_register.md      # Fast index of changes to advice/knowledge. Not a copy of recommendations.
│   ├── research_queue_active.md  # Active queue only (lean).
│   └── research_queue_archive.md # Deprioritised/resolved items + wall sources with what was tried.
│
├── source_archive/               # Complete raw content of large sources, one file per source.
│   └── {domain}__{slug}__{YYYY-MM-DD}.{ext}
│
├── raw_game_data/                # READ-ONLY inputs pushed by user-side scripts (ADB pulls, saves, API captures).
│   └── {YYYY-MM-DD_HHMM}__{device}__{account}/   # extraction dir; contains METADATA.json + raw files.
│
├── tools/                        # Self-contained, documented, versioned scripts + per-tool CHANGELOG.
│   ├── state_extraction/         # Step 3 ADB snapshot script for the user's MacBook.
│   └── capture_pipeline/         # Step 3 API-capture design (if researched viable).
│
├── audit_packages/               # Mechanism 9 packages: audit_package_{YYYY-MM-DD}_{scope}.md
│
└── snapshots/                    # KB snapshots: kb_snapshot_{YYYY-MM-DD}_{seq}/ (kept indefinitely).
```

---

## 2. RECORD FORMATS

### 2.1 `logs/sources_visited.json`
Top-level object; `entries` is an append-only array. One entry per fetch attempt (including failures — a failed attempt is evidence for a wall-source record).

```json
{
  "schema_version": 1,
  "entries": [
    {
      "id": "S-0001",
      "timestamp_utc": "2026-09-27T17:05:00Z",
      "session": 1,
      "turn": 1,
      "state": "STATE_1_RESEARCH_SWEEP",
      "role": "page-render | discovery-search | shell/script",
      "tool": "fetch_page | web_search | bash:curl | bash:gh-api | image_search",
      "url": "exact URL as requested",
      "resolved_url": "final URL after redirects, if different",
      "domain": "host only",
      "http_status": 200,
      "outcome": "success | blocked-network | 404 | paywall | bot-wall | partial | error",
      "query": "search query, where role = discovery-search",
      "source_type": "official | database-tool | community-english | community-non-english | technical | user-generated | ftg-as-company | <new kind>",
      "language": "en | tr | ar | pt | es | fr | id | ...",
      "payload_summary": "what was extracted, structured, specific",
      "raw_archive_path": "source_archive/... or null",
      "kb_paths_touched": ["kb/topics/..."],
      "deception_screen": {"incentive": "none|observed|inferred", "detail": "...", "outcome": "..."},
      "conflicts_found": [],
      "confidence_note": "...",
      "discovered_not_yet_visited": ["url or lead", "..."],
      "leads_consumed_from": "S-000X | initial-seed"
    }
  ],
  "frontier": {
    "discovered_total": 0,
    "visited_total": 0,
    "unvisited_leads": []
  }
}
```
`discovered_not_yet_visited` + `frontier.unvisited_leads` are what exhaustion condition (1) is checked against; "no new information from any reached source" (condition 2) is evidenced in `logs/sweep_tracker.md` per source type and language.

### 2.2 KB claim record (in `kb/topics/*.md` and in the KB-level files)
Every claim carries, at minimum:

```
- CLAIM: <statement, one fact, in the game's own terminology>
  - source: <S-000X log id(s)> + <origin URL/author>
  - first_published: <date(s) of the sources, where it bore on independence>
  - last_verified: <date> by <role/tool>
  - confidence: Confirmed | High Confidence | Community Consensus | Speculative | Disputed
  - volatility: volatility-Critical | volatility-High | volatility-Low | volatility-Frozen
  - volatility_dimensions: patch-triggered: <what would fire it> | event-triggered: <what would fire it>
  - origin: <direct evidence route — game code/data, FTG doc, reproducible test, observed behaviour> | NONE FOUND (tier capped accordingly)
  - independence: <per-source origin and why it is not an echo, or "single source">
  - deception_screen: <outcome, incl. clean>
  - datamining: pending-confirmation (flagged <date>, blocked because <reason>) | confirmed | unverifiable-through-datamining
  - evidence_class: verified | user-stated | inference (method: <...>)
  - game_version: <version the claim was observed against>
  - notes: <anything else — a field the work turns up that belongs on a claim is added here>
```
Tier words are always named with their system (TIER RULE, PROMPT.md §3). A claim with no volatility tier is a defect.

### 2.3 Main operational log entry
```
## [YYYY-MM-DDTHH:MMZ] CATEGORY — <short title>
session <n> turn <t> | state <STATE_x> | topic: <topic slug, mandatory for RECOMMENDATION>
<body: full content, not a summary. Evidence, decision, reasoning, outcome.>
refs: <S-xxxx log ids, kb paths, issue ids>
```
Categories (from PROMPT.md §8, extendable — a new category is announced in the handoff): RESEARCH, RECOMMENDATION, OUTCOME, QUESTION, REVISION, CONFLICT, DISAGREEMENT, EXHAUSTION DECLARATION, SKEPTIC CHALLENGE, DEVILS ADVOCATE, BLUFF CHECK, SELF-AUDIT, INDEPENDENT VERIFICATION, DEGRADATION EVENT, DECEPTION FINDING, EVIDENCE CONFLICT, CONFIDENCE PROMOTION, SOURCE TYPE COVERAGE, NEGATIVE FINDING, MATCH LOG.

### 2.4 Issue tracker entry
```
### ISS-NNN — <title>  [OPEN | INVESTIGATING | RESOLVED | WONTFIX]
opened: <ts> | kind: <game | method | recommendation | failure | deviation | degradation | saturation | word-sense | risk-tier-gap | card-tier-gap | other>
report: <what happened>
investigation: <root-cause investigation, OR for kind=system-state: comparison against entries sharing this category/pattern + whether the pattern bears on advice>
resolution: <...>
saturation_exempt: <true only for saturation entries — exempt from investigate-on-first-occurrence>
```

### 2.5 Research queue entry (active file)
```
### RQ-NNN — <discovery>   queue-priority: Critical|High|Medium|Low
added: <ts> session <n> | why_not_now: <only for operational-work items; during sweeps only wall sources queue>
natural_opportunity: <what would make it free to pursue>
sessions_passed_over: [<session ids>]
```
Archive file carries the same entry plus `archived_reason`. Wall sources carry: what it is, the barrier, every method tried (by role), what is believed to be behind it, what the user would need to do.

### 2.6 HANDOFF.md
Single file, rewritten atomically each turn. Sections in this order: `Session state`, `Return gap anchor`, `Awaited outcomes`, `Active/interrupted processes` (with last action / last source / last search / next specific action), `Current discussion`, `Pending decisions`, `Next action`, `Disputed count` (pointer to `kb/disputed_claims.md`), `Cycle dates` (last self-audit completion, last full sweep), `External verification debt`, `Milestone`, `Skill level assessment`, `Open PR status`, `Bootstrap status` (steps completed + last/next action for the current step), `Prompt version in force`, `Overrides in force`, `Progress signal` (full content, always), `Reference note` (the consolidated User Profile / state-currency note, verbatim from PROMPT.md §8).

### 2.7 Raw game data extraction metadata (`raw_game_data/<dir>/METADATA.json`)
```json
{"extraction_timestamp_utc":"","game_version_at_extraction":"","source_device":"","source_account":"personal|test",
 "script_version":"","files_pulled":[],"files_failed":[],"partial_or_retried_reads":[],
 "client_updated_since_files_written":"unknown|yes|no","redactions_applied":[],"notes":""}
```
Untagged-for-test extractions are treated as personal game state. Stale extractions are flagged, never used as current state.

---

## 3. SIZE, ROTATION, ARCHIVING

- Rotation thresholds (monitored, acted on before performance degrades): any single log/KB file > **1.5 MB** or > **20 000 lines** → rotate to `_NNN` continuation, all parts kept and indexed in the file's header.
- `source_archive/` is exempt from rotation (raw evidence) but tracked against total repo size.
- Repo-level budget: keep total repo well under **1 GB**; artifact cap for turn-end snapshots is ~128 MB / ~10 000 files, so large binaries are never committed unless required. Practical GitHub limits are researched during the bootstrap and recorded in `logs/main_operational_log.md` under RESEARCH.
- Snapshots and the deception register are never pruned. Nothing is discarded; archive instead of delete.

---

## 4. CONVENTIONS

- All repo documentation, schemas, and analysis in **English**. Non-English source material keeps the original text **plus** an English translation.
- Timestamps UTC, ISO-8601 (`YYYY-MM-DDTHH:MMZ`).
- IDs: sources `S-NNNN`, issues `ISS-NNN`, queue `RQ-NNN`, audit packages `AP-NNN`.
- Tier words never appear bare (TIER RULE).
- Cross-references name the rule, never its position in a file.
- Never modify anything under `raw_game_data/` (read-only inputs) or `snapshots/` (immutable).
- `PROMPT.md` is never edited by the agent — proposals go to `prompt_versions/CHANGELOG.md` marked PROPOSED.

---

## 5. SCHEMA HISTORY

- **v1.0 — 2026-09-27:** initial schema, created in STATE_0_SETUP. No prior version; nothing superseded.
