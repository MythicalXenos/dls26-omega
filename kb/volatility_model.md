# VOLATILITY MODEL

Per PROMPT.md §9. Governs ongoing maintenance **between** full sweeps; it does not govern initial truth establishment. Built *after* the sweep and datamining from **observed FTG patterns** — no pre-sweep priors about how FTG changes things.

**Model status: NOT YET BUILT.** Building it is STATE_4 work. Until then, claims entering the KB are tiered by the definitional assignment plus the default rule below, and the observation log underneath this file accumulates the evidence the model will be built from.

## Definitional assignment (does not wait on observation)

- The user's club and game state changes with every match played → **volatility-Critical** from the first session.

## Default where the model has no basis yet

Treat as **volatility-Critical** until observation says otherwise (PROMPT.md §9). Rationale: an unnecessary re-check costs less than a missed change; a tier guessed high corrects itself on the next observation, a tier guessed low silently stops being checked.

## Tier definitions (four — closed count, PROMPT.md §9)

| Tier | Meaning | Check cadence |
|---|---|---|
| volatility-Critical | frequent changes AND high impact | every session start, fresh searches, checked first |
| volatility-High | changes with patches or real-world events | when a TRIGGER fires |
| volatility-Low | rarely changes | at least monthly, and whenever a conflict touches the area |
| volatility-Frozen | cannot change without a major version or an FTG-stated system replacement | at major versions only; re-tiered immediately if direct observation shows change |

**TRIGGER** (capitalized = the defined sense): an observable event of the kind the item's own two recorded dimensions name — a patch/update whose notes, changed data or community reports mention any system, value or mechanic the item concerns; or a real-world event bearing on it (transfer window, competition, licensing change, season boundary). TRIGGERED = one has occurred since the item was last checked.

## Per-claim dimensions (recorded with every tier assignment)

`patch-triggered: <what would fire it>` and `event-triggered: <what would fire it>` — so trigger status is a comparison against a recorded fact, never a judgement made fresh.

## Impact weighting

A ranking, **not** an arithmetic product: volatility tier + bearing on active/pending recommendations, ranked together. Where the two disagree, the claim behind a live recommendation ranks first.

## Self-updating rule

Low/Frozen item found to have changed → re-tier from observed behaviour, log the change and its prompt, treat the discrepancy as a research trigger (ordinary sense). Critical item showing no change across successive logged checks → re-tier down, citing the checks.

## FTG change-pattern observation log (raw evidence for the model — append-only)

| Date observed | What changed | Game version before → after | How it was learned | Source (S-id) | Pattern note |
|---|---|---|---|---|---|
| 2026-09-27 | Client version moved 13.410 → 13.420 (reported 2026-09-01) and → 13.430 (reported 2026-09-14); the two reports conflict and are under Conflict Protocol | unknown → 13.420/13.430 (disputed value) | discovery-search snippets + page-render | S-0001, S-0002 | Cadence appears to be roughly monthly minor versions with a named seasonal content drop ("late summer update", "Cult Heroes" special players) — UNVERIFIED, single-thread evidence, do not treat as a pattern yet |
| 2026-09-27 | Version history: **12.200 dated 06/04/2025** and **13.430 dated Sep 16 (2026)** are the two entries Apple exposes; the Play listing shows "Updated on Sep 14, 2026" | 12.200 → 13.430 | page-render of the official App Store listing (version history) + Play listing | S-0017, S-0011, S-0012 | Major-number → product-year mapping hypothesis (12.x = 2025 product, 13.x = 2026 product) with a persistent package id `com.firsttouchgames.dls7`. Platform stagger of ~2 days (Play then iOS). UNVERIFIED as a cadence — the intermediate history is missing (gap G-0013), so no pattern may be asserted yet |
| 2026-09-27 | Content state moved AHEAD of the store changelog: 13.430's changelog says Cult Heroes is "coming soon", while both stores' event surfaces showed it LIVE on 2026-09-27 | 13.430 | page-render of Apple Events section + Play eventdetails page | S-0015, S-0016, S-0017 | DURABLE OBSERVATION for monitoring design: changelogs lag live content. The surfaces that show live state are the App Store Events cards and the Play in-app-event pages, not "What's New". This is an observation about how FTG publishes, and belongs in the model's evidence base |
| 2026-09-27 | Mechanics named in a historical changelog still absent from the current one: **Player Recovery** and **Special Coach Packs** (12.200, 06/04/2025) | 12.200 | page-render | S-0017 | A mechanic advertised in an old changelog does not reappear in later ones — so absence from a recent changelog is NOT evidence of removal. Bearing on the two gap states: this is why "no records found" must never be recorded as "does not exist" |
| 2026-09-27 | A third-party database dated its own list "September 27, 2026" — the same day it was retrieved — and separately lists a card type ("Cult Heroes") whose collection FTG's own changelog called "coming soon" only 13 days earlier | unstated by the source; FTG client 13.430 | page-render of /players/trending.php and /players/simulator.html | S-0019, S-0020, S-0015, S-0016, S-0017 | Two observations. (1) A freshness marker equal to the retrieval date cannot be distinguished from a generated one, so it carries no information until a Wayback capture tests it (gap G-0022) — a durable rule for this project: **treat an undated or self-dated third-party number as unplaceable against a version, and prefer any source that stamps a version**. (2) Third-party databases can move FASTER than official changelogs (a card family listed as live here while FTG's own 13-day-old changelog still said "coming soon"), so the volatility model's monitoring set must include third-party trackers as early-warning sensors while never accepting their values as evidence |
| 2026-09-27 | Numeric ids for a card family appear to occupy a contiguous block (Cult Heroes 28324-28334, 11 of 12 with no gaps; Season Pass card at 28356) | unstated | page-render of per-player URLs on /players/trending.php | S-0019 | If ids are allocated sequentially per release batch, then a new collection is detectable by probing neighbouring ids BEFORE any official announcement — an early-warning sensor with real lead time. HYPOTHESIS ONLY, inferred from one third party's id space; must be confirmed against client data before it is relied on (gap G-0025) |
