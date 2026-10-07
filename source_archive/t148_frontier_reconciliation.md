# T148 — T147 frontier reconciliation correction

At T148 start, recovered pushed tip `098bd55` and byte-verified 381 files against `/tmp/dls26-t148-recovery-20261006124249.tar.gz` (SHA-256 `da6b1d67f3e3222877bdc0b0b9bad2a42ab2f52427c15e0ccde1d7cf3e276f65`). No external research retrieval was made for this correction.

The T147 finalizer had logged screenshot #19 as an HTTP 500 attempt and incremented `visited_total`, but its unvisited lead was a free-text string containing the URL followed by a description; a bare-URL equality check failed to remove it. The entry has now been removed from `frontier.unvisited_leads`, and `unvisited_total` corrected from 396 to 395. `visited_total` remains 611; `entries` remains 810. T147 source archive and handoff totals were corrected accordingly.

Exact URL: `https://play-lh.googleusercontent.com/F6iyUl_VUu2750o_S0azaxZF2B-er2p2cuF8rIdduT0mkQfXvQ5wNQsYGCRfalHSgdsu-3fduzCbg70WFIT3Xw=w526-h296-rw`. Its T147 fetch returned HTTP 500 with no image bytes; no visual inference.

## Second reset recovery during T148

A reset recurred before closeout. A second archive `/tmp/dls26-t148b-recovery-20261006125000.tar.gz` captured 382 files and was byte-verified after restoring pushed tip `098bd55`; SHA-256 `a3791188a063f77fb48d997882f1b05437510efcf0da5eb255aacbc9d73b2f36`. Upstream and repo-local identity were restored again.
