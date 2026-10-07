# T118 — App Store developer page and third-path screenshot attempt

Date: 2026-10-06 Asia/Dhaka. Two retrievals.

## Apple developer directory
Exact URL: `https://apps.apple.com/us/developer/first-touch-games-ltd/id471316020`. `fetch_page` returned a complete page titled “First Touch Games Ltd. for iPhone - App Store” (HTTP status not exposed). It lists Dream League Soccer 2026 among FTG's apps, alongside Ultimate Clash Soccer, Score! Match, and Score! Hero. It provides no Cult Heroes route/rewards/cost or DLS26 position-lock rule. This is storefront listing context only.

## Google Play screenshot URL 7
Exact URL: `https://play-lh.googleusercontent.com/xnrPfNzmQ4sOl1YwIGBbKJScDSj9Hqx57Xg4m63GC6Swu-5Z8E7D-k0v_C5Qj9DfmcVJZOKRkFmFGp4VVb0HXQ=w526-h296-rw`. A single `curl` GET using a third delivery client failed with exit 35 (`OpenSSL SSL_connect: SSL_ERROR_SYSCALL`) and HTTP status 000; no response bytes. Do not retry the exact URL or infer its contents. The six earlier screenshot failures were not retried; 17 exact image URLs (8–24) remain unvisited in the ledger. No screenshot has been visually assessed.

Recovery: T118 opened on reset `fb9a2c0`; 316 non-ignored project files were archived to `/tmp/dls26-t118-recovery-20261006065432.tar.gz` (SHA-256 `81e28c8b959d1bc586f12a5c73d01ada8661337f6272e20a7c6b69671af14d4c`, 316 members), then `12a774a`, upstream, and repo-local identity were restored. No files discarded.

Ledger: **733 entries / 551 visited URLs / 411 unvisited leads**. Cult Heroes route/rewards and DLS26 position-lock remain unresolved; position-lock remains `user-stated` and unverified. No absence inference or exhaustion declaration.
