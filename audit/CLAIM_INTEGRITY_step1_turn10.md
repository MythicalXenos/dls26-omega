# CLAIM AUTHORITY — END-TO-END INTEGRITY CHECK (turn 10)

Date: 2026-10-17T17:12Z · Scope: `kb/claims.jsonl` (authority), `docs/continuity/a7e23a6b/evidence/index.jsonl` (EV registry), `docs/continuity/a7e23a6b/evidence/{extract,raw}/` (artifacts), `kb/claims_index.md` (derived view).
Method: mechanical, read-only pass over every line and every evidence token, then manual disposition of each anomaly. This check tests **structural integrity**, not truth. Witness-vs-proposition truth was tested in turn 9 (`audit/TRANSCRIPTION_SPOTCHECK_turn8.md`) and remains a sampled test, not a proof.

## 1. Results

| # | Check | Result |
| --- | --- | --- |
| A | Every JSONL line parses as JSON | **PASS** — 117/117, 0 errors |
| B | Claim IDs unique | **PASS** — 117 unique |
| C | Claim IDs contiguous | **PASS with note** — `CLAIM-001…CLAIM-118`; `CLAIM-036` absent and unreferenced (F-01) |
| D | File ordered by claim number | **PASS** — monotonic |
| E | Every EV token in `supporting_evidence` resolves | **PASS** — 264 tokens, 0 unresolved. Resolution = id present in `evidence/index.jsonl` **and** its recorded artifact exists. `EVD-0005`, cited by CLAIM-100, resolves to `evidence/extract/EVD-0005_page_missing_404.md` (failure records live as files but are not registered in `index.jsonl` — see F-05) |
| F | Every EV token in `context_evidence` resolves | **PASS** — 22 tokens, 0 unresolved |
| G | Every claim has a volatility tier from the allowed set | **PASS** — 117/117 (High 40 · Medium 31 · Low 32 · Critical 11 · Frozen 3) |
| H | Every claim has a valid ISO `next_due` | **PASS** — 117/117 parse as dates |
| I | No claim lacks an evidence/witness basis | **PASS** — minimum 1 entry; zero empties |
| J | `cross_refs` targets resolve | **PASS** — 11 claims carry cross-refs; all `CLAIM-###` tokens exist (formatting note F-04) |
| K | `replacements` targets resolve | **PASS** — all null; nothing to resolve |
| L | Derived index matches authority | **PASS** — `kb/claims_index.md` has 117 unique claim rows, 1:1 with JSONL, no extras, no omissions |
| M | Index `covers[]` entries are existing claim IDs | **FAIL (inherited, scoped)** — EV-218…EV-222 use topic tags, not claim IDs (F-03) |

Confidence distribution at check time: Confirmed 31 · High Confidence 49 · Community Consensus 23 · Speculative 13 · Disputed 1.

## 2. Findings and dispositions

### F-01 — `CLAIM-036` is a silent gap in the ID sequence
No claim numbered 036 exists, and a repository-wide grep finds **no reference to `CLAIM-036` anywhere** — not in the KB, the imported corpora, logs, or the cross-branch documents. So this is not a dangling pointer; it is an unexplained gap in the ID space.
**Disposition:** recorded here and in `issue_tracker.md` as OBS-014(a). No renumbering — IDs are stable identifiers and renumbering would invalidate the turn-8 spot-check record. The next claim is `CLAIM-119`.

### F-02 — `last_checked_by` is null on all 117 claims
The field exists in the schema and is populated nowhere; provenance is carried instead by `origin_history[]` and `last_valid_check`. This is a **field that promises more than the data delivers**.
**Disposition:** documented in `SCHEMA.md` as reserved/deprecated-in-practice, not back-filled. Back-filling from `origin_history` would manufacture a "checked by" attribution that no record actually makes. Future real re-checks populate it.

### F-03 — EV-218…EV-222 `covers[]` holds topic tags, not claim IDs
These five records (imported from the `a7e23a6b` corpus, retrieved 2026-10-15) list tags such as `community-web-en`, `progression`, `season-pass`, `access-boundary`. Every other record in `index.jsonl` lists claim IDs.
**Disposition:** recorded as inherited metadata, not mutated — the file is an imported corpus and the index is not the claim authority. No claim's tier or proposition depends on `covers[]`; it is an index-side navigation field only. OBS-014(b).

### F-04 — `cross_refs[]` entries are annotated strings, not bare IDs
Nine of the entries read like `"CLAIM-054 (full version timeline)"`. Parsing tolerates them only because a regex strips the parenthetical.
**Disposition:** recorded; new entries must be bare `CLAIM-###`. Not rewritten now, to avoid churn on 11 records for a cosmetic schema issue. OBS-014(c).

### F-05 — Evidence records are split across two registration regimes
`index.jsonl` registers 124 `EV-*` records; the seven `EVD-*` page-missing records exist only as files in `evidence/extract/`. This is why a naive "every EV resolves to an index record" check reports false failures.
**Disposition:** recorded as a schema fact in `SCHEMA.md`; a future `EVD` index stub would close it, but failure records must never be cited as support, so the risk is low. Not a defect in any claim.

### F-06 — Freshness debt is real and is not being hidden
- **Overdue:** `CLAIM-003` and `CLAIM-006` (both `next_due` 2026-10-11).
- **Due today:** `CLAIM-005`, `CLAIM-021` (2026-10-17).
- `next_due` was **not** bumped: with every retrieval family at ACCESS_BOUNDARY, a bump would assert a re-check that did not happen. The debt is carried visibly into `FIRST_CONTACT_BASIS.md` §6 and the epoch contract.
Both overdue claims are Speculative and both carry written challenges; neither is load-bearing for any coaching statement proposed so far.

## 3. Uncited evidence records (informational)
19 of 124 EV records are cited by no claim: 13 are inventory/revision tails (EV-109, 133, 158–161, 163–165, 168, 178, 205, 208) and 6 are page-missing failure records (EVD-0006…0010, 0012) that must never be cited as support. This matches the turn-4 classification; no new action.

## 4. Verdict
**Structural integrity: PASS**, with five documented, non-propositional residuals (F-01…F-05) and one carried debt (F-06). No claim's proposition, tier, evidence list or due date was changed by this check. Integrity is not truth: the KB is internally consistent, and only 10 claims have had a full transcription spot-check plus 62 numeric claims a numeric witness pass. The remaining risk is interpretive, not structural.
