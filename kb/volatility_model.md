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
