# T111 — FTG Help Center “out of position” query, chunks 2–7

Date: 2026-10-06 Asia/Dhaka. Six retrievals: chunks 2–7 of page 1.

Exact query URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=out%20of%20position`. The API reports 34 results across 2 pages; page 1 has 13 rendered chunks. T110 already read chunks 0–1; T111 read chunks 2–7. Chunks 8–12 and all of page 2 remain unread. `fetch_page` returned success; no HTTP status or per-call timestamp was exposed.

The returned Help Center material is mixed across FTG games. In chunk 7, the API result includes the DLS-labeled article [`How do the various player stats in DLS affect gameplay`](https://support.ftgames.com/hc/en-us/articles/360019166777-How-do-the-various-player-stats-in-DLS-affect-gameplay), with `updated_at` `2026-10-03T10:47:54Z`. Its body says: “Players with this behaviour attribute will actively make runs into attacking positions or to find space. Players without this behaviour will stay more closely to their formation position.” This is a statement about the Running behavior and in-match movement/AI, not evidence of a locked squad slot, and the title/body do not explicitly identify a DLS26 position-lock rule. A direct-page visit is queued only if the exact URL is not already in the machine ledger. Do not convert this into confirmation or refutation of the user-stated no-lock claim.

Other chunks include Score! Match/Score! Hero/UCS material and leaderboard-position wording. Do not transfer those games' mechanics to DLS26. No absence inference.

Recovery: opening reset `fb9a2c0`; archived 302 non-ignored project files to `/tmp/dls26-t111-recovery-20261006062044.tar.gz`, SHA-256 `f256ffffe3ff4cfe853bdd040dda5a0e4ecf4ea1636c7ab44ee883818f151324`. The archive was fully listed/verified before fetching/restoring `506987a`, upstream, and repo-local identity. The T111 start marker was restored to the committed clock; no files were discarded.

Ledger: **719 entries / 537 visited URLs / 401 unvisited leads**. Cult Heroes route/rewards remain unresolved; position locking remains `user-stated` and unverified. No dimension closed and no exhaustion declaration.
