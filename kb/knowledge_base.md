# Knowledge Base — index (current admitted state)

Last reconciled: 2026-10-23T15:41:55Z. Epoch-0001 remains OPEN. No claim from the imported PR #6 corpus is admitted as verified knowledge, and no confidence tier has been assigned. Do not use the quarantined records below as factual support for a recommendation. Five-pass audit: `docs/audits/2026-10-18-v80-import-audit.md`.

## Quarantined legacy candidates (read-only claim records)

| ID | Topic | Disposition |
| --- | --- | --- |
| CLM-0001 | Publisher and store identity | Quarantined; store summaries lack immutable primary payload/hash. |
| CLM-0002 | Free-to-download, IAP, advertising and store tags | Quarantined; source payload/hash missing. |
| CLM-0003 | App Store rating and listing metadata | Quarantined; time-of-fetch summary only. |
| CLM-0004 | App Store US IAP price list | Quarantined; time-of-fetch summary only. |
| CLM-0005 | Google Play update date and Cult Heroes note | Quarantined; partial page summary only. |
| CLM-0006 | Prize Ladder description | Quarantined; article payload/hash missing. |
| CLM-0007 | Player-stat descriptions and DLS26 applicability | Quarantined; chunk 0/4 only; applicability unresolved. |
| CLM-0008 | FTG company claims | Quarantined; page payload/hash missing. |
| CLM-0009 | DLS FAQ article inventory | Quarantined; pagination unchecked and payload/hash missing. |
| CLM-0010 | App Store version history | Quarantined; search snippet/third-party lead only. |
| CLM-0011 | Earlier version/date claims | Quarantined; search snippet only; CONF-002 unresolved. |
| CLM-0012 | DLS26 launch-date conflict | Quarantined; primary pages/language version unverified; CONF-001 unresolved. |

The original JSON records in `kb/claims/` are preserved unchanged. Their legacy `unassigned-pending-gates` labels are historical metadata, not a current confidence tier. Re-admission requires restored or freshly fetched immutable witnesses and a completed five-pass audit.

## Step-1 research observations (not admitted claims)

- Q-008 official-store slice: `kb/research_observations/2026-10-23-Q-008-official-store-slice.md`. The returned store-page projection associates Summer Spotlight with versions 13.320–13.350 (dates shown without years), while the 13.120 row says “Winter Reload.” This is a conflict/access note only: the full source payload/hash is not preserved, no exact launch date or Android build is established, and CLM-0010/CLM-0011 remain unchanged and quarantined.

## Owed work

- Step 1 epoch-0001 is OPEN; the validated saved cursor advances to Q-009 through Q-013; Q-008 was serviced with unresolved Q-002/CONF-002 debt, then classify all CONNECTED/UNCERTAIN references. No exit is inferred.
- Queue items Q-002 through Q-007 remain owed or blocked as recorded in `logs/research_queue_active.md`; prompt-policy text in an unverified v80 draft does not establish a game claim.
- Irreversible/consequential action types remain candidate-only in `kb/irreversible_actions.md`.
