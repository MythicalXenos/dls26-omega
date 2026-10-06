# T132 — DLS26 lineup/position image-search results

Date: 2026-10-06 Asia/Dhaka. Exact query: `Dream League Soccer 2026 official team management formation lineup player positions in-game screenshot`. `functions.image_search` status success; three results were saved and inspected with `functions.read_file`. Numeric HTTP statuses for thumbnail retrieval are not exposed.

## Result 1: Dream League Soccer 2026 Best Teams

- Returned source page: `https://www.sportsdunia.com/gaming/dream-league-soccer-2026-best-formations`; exact thumbnail proxy URL: `https://imgs.search.brave.com/GWrwjR9wEEdQApO7k7-lMNB3VblXLQtpeHRSDv6uklY/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/c3BvcnRzZHVuaWEu/Y29tL2Nkbi1jZ2kv/aW1hZ2Uvd2lkdGg9/Mzg0MCxvbmVycm9y/PXJlZGlyZWN0L2h0/dHBzOi8vc2Rwcm9k/c3RvcmFnZS5ibG9i/LmNvcmUud2luZG93/cy5uZXQvc2QtY21z/LXByb2QvY21zLXBv/c3QvRHJlYW0lMjBM/ZWFndWUlMjBTb2Nj/ZXIlMjAyMDI2JTIw/QmVzdCUyMFRlYW1zLTE3Njg0OTk3NDY5MjUud2VicA`.
- Archived asset: `{item["archive_path"]}`; SHA-256 `{item["sha256"]}`.
- Visual classification: sports editorial/promo banner; image reads COLLECT CULT HEROES; no game UI. No player-position controls or lock behavior can be read from this image.
## Result 2: Dream League Soccer 2026 Game Screenshot

- Returned source page: `https://taptap.io/app/180521`; exact thumbnail proxy URL: `https://imgs.search.brave.com/5RnOeADxkjtWQuYx6wjElBrY6tN0VzpXMO8nwepiNWQ/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/dGFwaW1nLm5ldC9t/YXJrZXQvaW1hZ2Vz/LzEwYTY1OWU0NDRm/YjQ5Y2VlOWMyNmE1/Y2VhNjMxNGIzLnBuZz9pbWFnZVZpZXcyLzIvdy8zNjAvaC8zNjAvcS84MC9mb3JtYXQvanBnL2ludGVybGFjZS8xL2lnbm9yZS1lcnJvci8xJnQ9MQ`.
- Archived asset: `{item["archive_path"]}`; SHA-256 `{item["sha256"]}`.
- Visual classification: TapTap editorial thumbnail reading BEST TEAMS IN DLS 26; not an in-game lineup screen. No player-position controls or lock behavior can be read from this image.
## Result 3: Dream League Soccer 2026 Game Screenshot

- Returned source page: `https://taptap.io/app/180521`; exact thumbnail proxy URL: `https://imgs.search.brave.com/AQG68eav-OCLDDjskn0_KsVdY_-WRk9ols5eDS80Ld8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/dGFwaW1nLm5ldC9t/YXJrZXQvaW1hZ2Vz/L2QzZjU0ZjVjNDgz/YjBkZDM2MzExNmIw/N2YxMDg1YjdhLnBu/Zz9pbWFnZVZpZXcy/LzIvdy8zNjAvaC8z/NjAvcS84MC9mb3JtYXQvanBnL2ludGVybGFjZS8xL2lnbm9yZS1lcnJvci8xJnQ9MQ`.
- Archived asset: `{item["archive_path"]}`; SHA-256 `{item["sha256"]}`.
- Visual classification: TapTap promotional stadium collage with INVEST IN YOUR CLUB text; not lineup controls. No player-position controls or lock behavior can be read from this image.

T125 comparison: visually similar Cult Heroes promotional artwork; byte identity not asserted (prior T125 file SHA-256 `8597e44fec49ba1ab90acfe0cf6af2984ea24ba6c6c14188bac2cf485504fd00`).

None of the images is authenticated first-party or an in-game lineup screen. The query did not yield position-lock behavior, formation-edit controls, or Cult Heroes acquisition/reward evidence. Do not infer absence from image-search results. Fourteen other queued Play screenshots remain low priority.

Recovery: reset `fb9a2c0`; archived 347 files at `/tmp/dls26-t132-recovery-20261006021737.tar.gz`, SHA-256 `2e3a71cb356090d34963f3bdfaa4f37ede4b60d2afced62c5ce02384f89ea6e1`; restored and byte-verified pushed tip `a63f2cd`, upstream, and repo-local identity. ISSUE-0014 occurrence #94; no content loss.
