#!/usr/bin/env python3
"""tools/frontier.py — executable frontier module (OMEGA-FRONTIER-001).

Operates on logs/sources_visited.json:
  * admission assigns a monotone shared sequence (admission/service ticket)
  * NON_CONNECTED classification is folded into the status field while its
    scope proof is preserved in the record
  * successful service moves the family/reference ticket to the tail
  * rotation helpers implement fair service within a group

CLI:
  python3 tools/frontier.py admit  --family F --ref REF --projection P [--non-connected PROOF]
  python3 tools/frontier.py start  --ref REF
  python3 tools/frontier.py complete --ref REF [--partial CURSOR]
  python3 tools/frontier.py next
  python3 tools/frontier.py summary
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_PATH = os.path.join(REPO_ROOT, "logs", "sources_visited.json")

VALID = {"UNVISITED", "IN_PROGRESS", "RETRYABLE_FAILURE", "VISITED",
         "ACCESS_BOUNDARY", "REPRESENTATION_DUPLICATE", "NON_CONNECTED"}


def utc():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load():
    with open(SOURCES_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save(doc):
    tmp = SOURCES_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, SOURCES_PATH)


def next_seq(doc):
    doc["sequence_counter"] = int(doc.get("sequence_counter", 0)) + 1
    return doc["sequence_counter"]


def find(doc, ref_id):
    for r in doc.get("references", []):
        if r["ref_id"] == ref_id:
            return r
    raise SystemExit("reference not found: %s" % ref_id)


def cmd_adend(doc, args):
    seq = next_seq(doc)
    rec = {
        "ref_id": args.ref,
        "family": args.family,
        "status": "NON_CONNECTED" if args.non_connected else "UNVISITED",
        "admission_seq": seq,
        "ticket_seq": seq,
        "projections": [args.projection] if args.projection else [],
        "extraction_cursor": None,
        "service_events": [],
        "discovered_at": utc(),
    }
    if args.non_connected:
        rec["scope_proof"] = args.non_connected
    doc.setdefault("references", []).append(rec)
    fam = doc.setdefault("source_families", {})
    fam.setdefault(args.family, {"ticket_seq": seq, "served_count": 0})
    save(doc)
    print(json.dumps({"admitted": args.ref, "seq": seq, "status": rec["status"]}))


def cmd_start(doc, args):
    rec = find(doc, args.ref)
    if rec["status"] in {"VISITED", "NON_CONNECTED"}:
        raise SystemExit("cannot start service on %s (%s)" % (args.ref, rec["status"]))
    rec["status"] = "IN_PROGRESS"
    rec.setdefault("service_events", []).append(
        {"event": "start", "at": utc(), "seq": next_seq(doc)})
    save(doc)
    print(json.dumps({"started": args.ref}))


def cmd_complete(doc, args):
    rec = find(doc, args.ref)
    if rec["status"] != "IN_PROGRESS":
        raise SystemExit("complete requires IN_PROGRESS (got %s)" % rec["status"])
    seq = next_seq(doc)
    if args.partial:
        rec["extraction_cursor"] = args.partial
        rec["service_events"].append({"event": "slice", "at": utc(), "seq": seq})
        # partial source stays IN_PROGRESS with its cursor
    else:
        rec["status"] = "VISITED"
        rec["extraction_cursor"] = None
        rec["service_events"].append({"event": "complete", "at": utc(), "seq": seq})
    rec["ticket_seq"] = seq  # completed service moves ticket to the tail
    fam = doc.setdefault("source_families", {}).setdefault(
        rec["family"], {"ticket_seq": seq, "served_count": 0})
    fam["ticket_seq"] = seq
    fam["served_count"] = int(fam.get("served_count", 0)) + 1
    save(doc)
    print(json.dumps({"updated": args.ref, "status": rec["status"], "seq": seq}))


def cmd_next(doc):
    """Fair next candidate: oldest ticket among owed (CONNECTED/UNCERTAIN) refs."""
    owed = [r for r in doc.get("references", [])
            if r["status"] in {"UNVISITED", "IN_PROGRESS", "RETRYABLE_FAILURE"}]
    owed.sort(key=lambda r: r.get("ticket_seq", r.get("admission_seq", 0)))
    print(json.dumps({"owed": len(owed),
                      "next": owed[0]["ref_id"] if owed else None,
                      "order": [r["ref_id"] for r in owed]}, indent=2))


def cmd_summary(doc):
    counts = {}
    for r in doc.get("references", []):
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(json.dumps({"epoch": doc.get("epochs", [{}])[0].get("epoch_id"),
                      "status_counts": counts,
                      "sequence_counter": doc.get("sequence_counter", 0),
                      "service_events": len(doc.get("service_events", []))},
                     indent=2))


def main(argv):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    pa = sub.add_parser("admit")
    pa.add_argument("--family", required=True)
    pa.add_argument("--ref", required=True)
    pa.add_argument("--projection", default="")
    pa.add_argument("--non-connected", default="")
    ps = sub.add_parser("start"); ps.add_argument("--ref", required=True)
    pc = sub.add_parser("complete"); pc.add_argument("--ref", required=True)
    pc.add_argument("--partial", default="")
    sub.add_parser("next")
    sub.add_parser("summary")
    args = ap.parse_args(argv[1:])
    doc = load()
    if args.cmd == "admit":
        cmd_adend(doc, args)
    elif args.cmd == "start":
        cmd_start(doc, args)
    elif args.cmd == "complete":
        cmd_complete(doc, args)
    elif args.cmd == "next":
        cmd_next(doc)
    else:
        cmd_summary(doc)


if __name__ == "__main__":
    main(sys.argv)
