# CHUNK-CONTINUATION TRIAGE — 23 IN_PROGRESS refs (turn 19)

Date: 2026-10-17T22:25Z. The 23 IN_PROGRESS refs fall into two buckets per the closure review. This file records which are CHUNK-COMPLETE-ENOUGH (chunk 0+ already supports the claims that cite them; further chunks are commentary/review pagination unlikely to change a mechanic) and which remain IN_PROGRESS as legitimate research debt.

## Bucket A — chunk-pagination mid-capture (8 refs)

| Ref | Family | Current capture | Triage | Rationale |
| --- | --- | --- | --- | --- |
| ref-store-gplay-chunk1 | official-store | chunk 1/6 + chunk 0/6 description | **CHUNK-COMPLETE-ENOUGH** | Chunk 0 (description, EV-103/172) contains the official copy that supports CLAIM-001/003/004/045; further chunks are user reviews which are already sampled in chunk 1 (EV-111) and carry only anecdotal weight — no new mechanic will come from them. |
| ref-store-gplay-reviews-chunk1 | official-store | chunk 1/6 user reviews | **CHUNK-COMPLETE-ENOUGH** | Same as above; reviews are community sentiment, not mechanics. |
| ref-player-stats-comments | official-support | comment chunk 0/4 (staff replies) | **CHUNK-COMPLETE-ENOUGH** | Article body (EV-115) is the stat semantics; comments are community questions with occasional staff replies. If a future sample surfaces a staff reply that contradicts GS-001, we re-open; until then the body is the witness. |
| ref-friend-match-comments | official-support | chunk 0/1 comments | **CHUNK-COMPLETE-ENOUGH** | Article body (EV-223) supports CLAIM-099; comments are anecdotal. |
| ref-cant-update | official-support | full text | **PORMOTION TO VISITED owed** | EV-225 (cant-update) was written turn 14; the ref was never restamped. Do in a future maintenance turn; no new mechanic. |
| ref-dreamkitsapp-deep | database-community | captured index only | **CHUNK-COMPLETE-ENOUGH** | We have the roster data we need (CLAIM-129/130 via EV-239); deeper pages are per-player stats already captured for the 12 Cult Heroes and a sample of others. Deeper crawl is Step-2 (APK) territory for definitive stats. |
| ref-store-appstore-chunk1 | official-store | chunk 1/? | **CHUNK-COMPLETE-ENOUGH** | Version-history chunk 1 (EV-177/183) supports CLAIM-048/054/055/057/087; further locale chunks would only add translations, not new mechanics. |
| ref-support-section-inventory | official-support | full inventory | **PROMOTION TO VISITED owed** | EV-114 (support-section inventory) was captured; the ref was never restamped. Maintenance only. |

## Bucket B — community-family pages (15 refs)

These are Reddit thread families, non-English community pages, and technical-web database facets that we know exist but have not enumerated specific URLs for. All are behind the web ACCESS_BOUNDARY (non-allowlisted hosts). Each carries the standard predicate (host allowlist change; permitted proxy; user-supplied captures in `raw_game_data/`).

Triage: **remain IN_PROGRESS-ACCESS-BOUNDED**. They are not retrieval failures; they are families that cannot be enumerated without reaching the host. Their state satisfies epoch §5 condition 1 (every named ref has a disposition; there are no "we forgot" refs in this bucket).

## Effect on epoch closure

After the two promotions (ref-cant-update, ref-support-section-inventory) in a maintenance turn, the IN_PROGRESS count drops from 23 to 6 reviews/chunks we have declared CHUNK-COMPLETE-ENOUGH (which is a disposition, not a status change) plus 15 access-bounded community families. The 6 chunk-complete refs will be re-stamped to VISITED-with-note at that point; the 15 remain IN_PROGRESS-ACCESS-BOUNDED.

**No new claims depend on any of these 23 refs as they stand.** The claim set (129) is supported by EVs that already exist; chunking more pages would either re-capture known mechanics (reviews) or be blocked by the network boundary (community families).
