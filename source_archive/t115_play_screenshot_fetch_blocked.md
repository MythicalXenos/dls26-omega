# T115 — Play screenshot image fetch attempts

Date: 2026-10-06 Asia/Dhaka. Three retrievals.

The T114 Google Play event page exposed 24 screenshot links; its first three were already attempted via Python urllib in T114 and failed TLS before HTTP. T115 attempted the next three distinct exact URLs with `functions.fetch_page`; each returned HTTP 500 with no payload. No image bytes were received and no visual contents were assessed. Do not retry these exact three, and do not infer anything about the screenshots or global access.

4. `https://play-lh.googleusercontent.com/d0Pfspg2Bqdqp0RHUGGru-ilO-Pyq-4pmCB2_DRIqukkxoDt_vdIHdpAAtf7PWbY53rbLGZfuOLWQDXgJFUTVw=w526-h296-rw` — functions.fetch_page returned HTTP 500/no payload; do not retry exact URL.
5. `https://play-lh.googleusercontent.com/1guviZqNIulGQp-FTbh0BEEYw6lsgdPYFAKPqLXg1nUn3vxji_VERojgeE2UaX42Zt_swIFdlrA1Y8UJVDr4_g=w526-h296-rw` — functions.fetch_page returned HTTP 500/no payload; do not retry exact URL.
6. `https://play-lh.googleusercontent.com/YK5LCoglhj8ZXB5yaM7zM8pRmzYWpetlhsVj3Zgsx0ah2pO5BqI10R8sl3Eyh0Tu6KWngVuGkvT3R9O4RtXM=w526-h296-rw` — functions.fetch_page returned HTTP 500/no payload; do not retry exact URL.

Eighteen exact screenshot links (URLs 7–24 in `source_archive/t114_play_bd_event_screenshots.md`) remain unvisited. The official store page's copy is not evidence of in-game availability or route/rewards. Cult Heroes route/rewards and DLS26 position-lock remain unresolved; position-lock stays user-stated/unverified.

Recovery: T115 opened at reset `fb9a2c0`; 310 non-ignored files were archived to `/tmp/dls26-t115-recovery-20261006064207.tar.gz` (SHA-256 `600a4b8b0a3f0f75382891967e590a739eb3e0c6e88a5140847f106da8b94d28`, 310 members), then `1f1c1ce`, upstream, and repo-local identity were restored. No files discarded.

Ledger: **729 entries / 547 visited URLs / 415 unvisited leads**.
