# T120 — FTG query, Play asset delivery, and Wayback index check

Date: 2026-10-06 Asia/Dhaka. Three distinct retrieval executions; no game-mechanics evidence obtained.

## FTG Help Center API

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?per_page=5&query=Cult%20Heroes%20collection`. `functions.fetch_page` status `success` (HTTP status not exposed). Query `Cult Heroes collection` returned JSON `count: 0`, `next_page: null`, `page_count: 0`, and `results: []`; the response reports `per_page: 25` despite the request parameter `per_page=5`. This is only the outcome of this exact query, not evidence of global absence.

## Google Play screenshot URL 8

Exact URL: `https://play-lh.googleusercontent.com/8djmQFQ5-YRLHpUDyUmR3NyNPdTvd6cNFIfTxAKnRri0ZvstRwNZyGkjZs2LoRO5c3PyVNzFJi_5sCugZv_3yus=w526-h296-rw`. A single curl GET (`--http1.1`) failed before HTTP: exit 35, `OpenSSL SSL_connect: SSL_ERROR_SYSCALL`, HTTP status 000, zero bytes. No image was saved or visually assessed. Do not retry this exact URL. The remaining untried screenshot URLs are 9–24 (16 URLs).

## Internet Archive CDX

Exact URL: `https://web.archive.org/cdx/search/cdx?url=www.ftgames.com%2Fgames%2Fdls&output=json&filter=statuscode%3A200&fl=timestamp%2Coriginal%2Cstatuscode%2Cdigest&collapse=digest`. `functions.fetch_page` status `success` (HTTP status not exposed); payload was the empty JSON array `[]` for this exact archived-URL query. This does not establish that no other snapshots or FTG/DLS captures exist. No snapshot page was fetched.

Cult Heroes route/rewards and DLS26 position-lock remain unresolved. Position-lock remains `user-stated` and unverified. No absence inference, spending advice, or dimension closure.
