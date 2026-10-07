# T146 — FTG YouTube and DLS shortlink checks

Date: 2026-10-06 Asia/Dhaka. Three retrieval calls; exact per-call timestamps not exposed.

## First Touch Games official-channel pages

- `https://www.youtube.com/watch?v=gpvjf6qVl5c`: official uploader `firsttouchgames`; title “Dream League Soccer 2026 | OFFICIAL TEASER TRAILER”, uploaded 2025-11-07. Description says DLS26 is available December 2025 and links to `https://ftgames.com/dls`. Only page chunk 0/154 was read; the render is script-heavy. No Cult Heroes route/reward/position detail appears in the visible metadata. Remaining chunks 1–153 are low-priority/unread; do not treat them as absent.
- `https://www.youtube.com/watch?v=03VNg9djVZ8`: official uploader `firsttouchgames`; title “CHAMPIONS Are Here In DLS25!”, uploaded 2025-07-17. Its description says Champions are available in DLS25 and directs players to Legendary Agents. This is older-version context only; do not transfer it to DLS26 Cult Heroes.

## Follow the FTG shortlink

Request `https://ftgames.com/dls` resolves to `https://www.ftgames.com/games`, a generic FTG games catalogue already visited in the same first-party page family. The page repeats general DLS marketing text, store links, and screenshots only; it offers no Cult Heroes route/reward/position evidence.

## Recovery

T146 began on reset checkout `fb9a2c0`; clock was recorded first. Archived and byte-verified 377 working files at `/tmp/dls26-t146-recovery-20261006122727.tar.gz`, SHA-256 `41f47f5cbd5434b09fd74987d96fd5e848c7f3b5ba56ad0981d24dec5270429a`; fetched/restored pushed tip `4e72b23`, restored upstream and repo-local identity, and retained safety stash `46365a0`. ISSUE-0014 occurrence #108.

No new Cult Heroes acquisition route/reward or DLS26 position-lock evidence.
