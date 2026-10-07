# T135 — FTG query completion and first-party probes

Date: 2026-10-06 Asia/Dhaka. Six retrieval calls total. Per-call timestamps not exposed.

## FTG `Agent rewards` completion

Exact URL: `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Agent%20rewards`. T135 fetched chunkIndex 7 (retry after T134 HTTP 502) and chunkIndex 9. Both returned `status=success`; chunk 7 reports `totalChunks=10`, chunk 9 reports `hasMore=false`. Combined with chunks 0–6 and 8 already fetched in T133–T134, the exact 18-result, one-page search is now complete across chunks 0–9. The final chunks return general/older DLS Help Center and other-product material (player statistics, player appearance, friend-match/reward FAQs); the completed fuzzy query does not establish a Cult Heroes route, guarantee, cost, or reward. This is not a global absence finding.

## Distinct FTG queries

1. Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=Cult%20Heroes%20Agent%20rewards` (`Cult Heroes Agent rewards`): `functions.fetch_page`, chunk 0, `status=success`; response `count=0`, `page_count=0`, `results=[]`. This exact phrase only; no global absence inference.
2. Exact URL `https://support.ftgames.com/api/v2/help_center/articles/search.json?query=change%20formation` (`change formation`): `functions.fetch_page`, chunk 0, `status=success`; API reports count=48, page_count=2, and page 1 is rendered in 7 chunks. Only chunk 0/7 was read. Visible material includes article 7917587319313 (“How do I change my formation?”), already visited and mapped to non-DLS section 7900693036561, and a formation-unlock result in Score! Match section 115001619089. Neither is evidence about DLS26 moving/locking individual players. Page 1 chunks 1–6 and page 2 remain unread; the API advertises `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=change+formation`. Do not infer absence from this partial mixed query.

## Official Play screenshot attempts

Distinct T114 inventory URLs #11 and #12 were tried once each with `curl -L --max-time 30 --silent --show-error`. Both failed TLS before HTTP: curl exit 35, HTTP `000`, zero bytes, no image saved or inspected. Exact URLs:
- `https://play-lh.googleusercontent.com/tEgeHK-qliU3iD1mI1Hm_mCOHRTLTGwqzdNOx0fFt8XraGUVAiTwcuCQTnWLUAwEgcMB7jPI25cqKP9SzusKHw=w526-h296-rw`
- `https://play-lh.googleusercontent.com/_XzQcNoEgW7X1Fb8Jx0yjwMH90YYO3LNTkzdbZPnPyhaLLPHUrBty5-8WJimr9Y9eeLTMT_FbnHObPs3vJHOFnM=w526-h296-rw`
Do not retry either URL or infer its contents. URLs #13–24 remain untried (12).

## Recovery

T135 began on reset checkout `fb9a2c0`; clock was recorded first. Archived 355 files at `/tmp/dls26-t135-recovery-20261006083441.tar.gz`, SHA-256 `685c5c37c5828397b533ca4633711626e2512746fe6dc15ccb51b904bd061e69`; fetched/restored pushed tip `9654c12`, restored upstream and repo-local identity, and byte-verified all files. ISSUE-0014 occurrence #97.
