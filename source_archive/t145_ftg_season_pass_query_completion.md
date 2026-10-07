# T145 — complete FTG Season Pass phrase query

Date: 2026-10-06 Asia/Dhaka. One retrieval call; per-call timestamp not exposed.

## Complete the existing partial query

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes%20Season%20Pass`. Retrieved `functions.fetch_page` chunkIndex 4 (the fifth and final chunk); chunks 0–3 were read in T144. The FTG Help Center API reports 16 results, page 1/1, five chunks total. Chunk 4 includes article 360004717278, “Can I use my Dream League Soccer (formally DLS19) profile in DLS25?”, updated 2026-10-05; it concerns profile transfer, not Cult Heroes. The full mixed response contains generic DLS Season Pass/help articles plus Score! Hero, Ultimate Clash Soccer, and unrelated support content. The DLS Season Pass FAQ describes generic pass structure, but no Cult Heroes-specific Agent/card acquisition route or reward guidance appears in this exact query. This does not establish global absence. Do not transfer other-game results to DLS26.

## Recovery

T145 began on reset checkout `fb9a2c0`; clock was recorded first. Archived and byte-verified 375 working files at `/tmp/dls26-t145-recovery-20261006122337.tar.gz`, SHA-256 `86b464fb3da680e37a01749e510a6ee882c5e7f5fc0fc0d3f6889854ab6ec045`; fetched/restored pushed tip `ef378e8`, restored upstream and repo-local identity, and retained safety stash `efd5468`. ISSUE-0014 occurrence #107.

The T144 duplicate retry of screenshot #18 remains documented on its original T143 record; T145 made no media requests. Both research dimensions remain open.
