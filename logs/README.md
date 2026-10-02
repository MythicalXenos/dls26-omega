# Logs

- `sources_visited.json` is the machine-readable retrieval frontier and exhaustion record.
- `main_operational_log.md` is timestamped, categorized, and append-only in substance.
- `exhaustion_declarations.md` contains evidence-backed closures only.

Before turn-end, derive coverage/frontier movement from the JSON ledger, reconcile file content against the branch, and update the handoff atomically.
