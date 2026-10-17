# WITNESS SPOT-CHECK — SAMPLE 2 (turn 11)

Date: 2026-10-17T17:4xZ · Corrects degradation D-05 (`audit/DEGRADATION_SELF_AUDIT_turn10.md`): the first sample (turn 8) and the numeric pass (turn 9) left most claims structurally verified only.
**Sample rule:** 10 claims, drawn from those **not** in the turn-8 sample, weighted to tiers that could actually change advice — Confirmed (6), Community Consensus (2), plus two cross-branch imports. Five of the ten rest on a single EV record, which is where a mis-transcription has nowhere to hide.
**Method:** read each cited artifact in full or in the cited section, compare every propositional clause against the text with claim IDs, dates and years stripped, then classify: PASS / NARROWED / MISMATCH.

## Results

| Claim | Tier | Witness read | Verdict |
| --- | --- | --- | --- |
| CLAIM-043 | Confirmed | EV-170 (full ToU page) | **PASS with correction** — see M-1 |
| CLAIM-075 | Confirmed | EV-201 (verbatim sanctions) | **PASS** — every clause present: modded APKs, external hacks on authorised versions, bug exploitation incl. currency gain / AI interference / progression circumvention, offensive names, bans not removed; "only authorised versions… Apple's App Store or Google's Play Store" is verbatim |
| CLAIM-083 | Confirmed | EV-213, EV-214 | **PASS** — one account; Google Android-only / Apple iOS-only sign-in; Generate Code under device limit, not usable on the generating device; Manage Devices X-removal + device limit; sign-out unlinks; codes unrecoverable; Facebook login permanently removed |
| CLAIM-106 | Confirmed | EV-145 (full text) | **PASS** — verbatim: closest player to the ball, gear icon top-left → Controls → Auto Switch |
| CLAIM-107 | Confirmed | EV-151 (full text) | **PASS** — verbatim swipe map (down Marseille, up rainbow, left/right stepover) |
| CLAIM-113 | Confirmed | GS-024 summary (imported) | **PASS** — cloud servers, opponent connection has no impact, lag switches ineffective, address hidden, last-mile diagnosis, ~2 MB/match, IPv6/5G, Bluetooth, no FB-invite, same-router local play. **Limitation: witness is an inherited Markdown summary, not an EV record** |
| CLAIM-114 | Confirmed | GS-026 summary (imported) | **PASS** — v12.200+, Manage Players bottom-right, release grants a coach, Recover section limited time |
| CLAIM-115 | Confirmed | GS-027 summary (imported) | **PASS** — ad networks own inventory, no frequency/doubler promise, LAT reduces availability (iOS 14+), troubleshooting ladder matches |
| CLAIM-091 | Community Consensus | M-001 summary (imported) | **PASS** — all six sentiment items present, and the claim correctly refuses to treat them as current state. **Limitation: summary witness, not an EV record** |
| CLAIM-118 | Community Consensus | EV-173 (536-byte chunk) | **PASS, narrowed** — see N-1 |

## Findings

### M-1 — CLAIM-043: the EULA lists **four** authorised stores, not two (real discrepancy)
- EV-170 says: *"AUTHORISED STORES: Apple App Store, Google Play, Amazon App Store, Windows Phone Store — 'First Touch does not publish to any other store.'"*
- EV-201 says, verbatim: *"The only authorised versions of DLS are available from Apple's App Store or Google's Play Store."*
- CLAIM-043's proposition said only "authorised stores only", which is true but conceals the difference; CLAIM-075 says "Play / App Store", which is correct **for its own source** but reads like a global fact.
- **Action taken:** a challenge was added to CLAIM-043 quoting the discrepancy and pointing at `logs/conflicts.md` **C-007**; `last_checked_by` populated for this claim (the first non-null in the KB); no tier change — both texts are official and the red line is identical under either.
- **Why it matters:** precision. Quoting the EULA as "Play and App Store only" is a misquotation of an official document, and this system has already committed to never doing that.

### N-1 — CLAIM-118 omits "leagues" from a list it paraphrases
EV-173 says reviewers describe "difficulty progression through Bronze/Silver/Gold/Diamond Cups **+ leagues**"; the claim says "Cup progression" only. Not a contradiction — the claim is about cups — but the summary is narrower than its source. Left as-is, recorded here so a future editor does not mistake the narrowing for the source's scope.

## What this sample does and does not establish
- **Establishes:** 9 of 10 claims reproduce their sources faithfully; 1 contains a genuine cross-document discrepancy that was previously invisible to the KB.
- **Does not establish:** that the sources themselves are right, that extraction was complete, or anything about claims outside the sample. Combined with turns 8–9, **20 of 117 claims (17%)** have now had a textual witness test. The other 97 remain structurally verified only.
- **Error rate trend:** turn 8 — 2/10 corrected; turn 9 — 4/62 numeric; turn 11 — 1/10. The rate is falling but is not zero, and every sample has found something. That is the argument for continuing sampling rather than declaring the KB clean.

## Follow-ups
- C-007 added to `logs/conflicts.md` (open, both sides quoted, reopening test named).
- C-006 added for the CLAIM-106 / sibling GS-030 dead-link report (no content conflict; liveness only).
- Next sample should target the 13 Speculative claims and the 23 Community Consensus claims, where interpretive overreach is likelier than transcription error.
