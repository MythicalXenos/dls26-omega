# T128 — two official Google Play event screenshot asset attempts

Date: 2026-10-06 Asia/Dhaka. Two distinct official Play-hosted screenshot URLs were attempted; neither returned image bytes.

1. URL: `https://play-lh.googleusercontent.com/QfnGqBQUfptOCmqKvFPByO9IrpJhdQOMbEqGcYURer53RF7z5xCGVnd9TT6J9cUSGUkzve1iGDo5yYEWcknROSw=w526-h296-rw`. Retrieval tool: `functions.fetch_page` (chunk 0). Tool reported HTTP 500 / failed fetch with no body. No image was saved or visually inspected. This exact URL is now an attempted/failed source; do not retry it.
2. URL: `https://play-lh.googleusercontent.com/LE_Ru9LmfZThTqc78Z3xvI_yabngdY-WohS9348FUnH-DawIc4R7U30s9VT86vYDiA0EKVlVQDXLDcRgr3eV3g=w526-h296-rw`. Retrieval tool: `bash curl -L --max-time 30`. Curl exit 35, `OpenSSL SSL_ERROR_SYSCALL`, HTTP code `000`, zero bytes. No image was saved or visually inspected. This exact URL is now an attempted/failed source; do not retry it.

These URLs were among the 16 queued official Google Play event screenshot leads. Both failed leads are retired from the unvisited frontier; 14 remain, still low priority. No event text, players, rewards, costs, route, availability, or gameplay UI were retrieved. No absence inference.

## Recovery

T128 began on reset `fb9a2c0`. Clock was recorded first. Archived 339 files to `/tmp/dls26-t128-recovery-20261006015919.tar.gz`, SHA-256 `37fdd306c297ed1a223f6566ff1a1fac182baa90c06c045b715938de98567f1b`; fetched/reset to `0f31a4b`, restored the fixed branch/upstream/repo-local identity, and byte-verified all 339 files. ISSUE-0014 occurrence #90; no content loss.
