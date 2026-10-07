# T150 — FTG change-formation query continuation

Date: 2026-10-06, Asia/Dhaka. Five retrieval calls: four page-2 chunks and one direct article. Exact per-call timestamps and numeric HTTP statuses were not exposed; every fetch_page result reported status `success`.

## Retrieval record

- Existing FTG Help Center endpoint: `https://support.ftgames.com/api/v2/help_center/articles/search.json?page=2&per_page=25&query=change+formation`. Chunks 1–4/15 were retrieved; chunk 0 was previously read in T137. The 48-result, two-page query remains partial; chunks 5–14 unread. The returned mixed-product response includes an unbound chunk-boundary snippet stating that default player positions follow formation and ball position, with overrides; the owning article identity/version is not established by the fragment. Do not treat it as a DLS26 rule.
- Direct FTG Zendesk API article: `https://firsttouch.zendesk.com/api/v2/help_center/en-us/articles/360019166777.json`. Title “How do the various player stats in DLS affect gameplay?” Metadata reports created 2021-04-13 and updated 2026-10-03. Its body is generic DLS material and includes a stamina note that some positions run more than others. It does not mention DLS26 or a squad-position lock, and has no Cult Heroes route/reward information. Keep it version-unstamped; do not promote to DLS26-specific evidence.

## Result and boundaries

No confirmed DLS26 position-lock behavior and no Cult Heroes route/reward evidence. The user-stated “DLS26 has no position locking” remains unverified. Other-product rules and generic DLS wording are not transferred to DLS26. No global-absence inference, spending advice, exhaustion declaration, or research-dimension closure.

Ledger after T150: **821 records / 618 visited URL attempts / 394 unvisited leads**.
