#!/usr/bin/env python3
"""Regenerate kb/claims_index.md rows from kb/claims.jsonl (mechanical, turn 15)."""
import json
import os
import re
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAIMS = os.path.join(ROOT, "kb", "claims.jsonl")
INDEX = os.path.join(ROOT, "kb", "claims_index.md")
NL = chr(10)

records = []
with open(CLAIMS, "r", encoding="utf-8") as fh:
    for line in fh:
        if line.strip():
            records.append(json.loads(line))

def row(c):
    prop = " ".join(c["proposition"].split()).replace("|", "/")
    if len(prop) > 160:
        prop = prop[:157] + "..."
    return "| %s | %s | %s | volatility-%s | %s |" % (
        c["claim_id"], prop, c["confidence_tier"], c["volatility_tier"], c["next_due"])

lines = [l for l in open(INDEX, encoding="utf-8").read().splitlines() if l.strip()]
by_id = {c["claim_id"]: c for c in records}
out = []
seen = set()
for l in lines:
    m = re.match(r"^\|\s*(CLAIM-\d{3})\s*\|", l)
    if m:
        cid = m.group(1)
        if cid in by_id:
            out.append(row(by_id[cid]))
            seen.add(cid)
        # drop rows for claim IDs that no longer exist
    else:
        out.append(l)

missing = [c["claim_id"] for c in records if c["claim_id"] not in seen]
for cid in missing:
    out.append(row(by_id[cid]))

now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
for i, l in enumerate(out):
    if l.startswith("# KB — CLAIM INDEX"):
        out[i] = l
    elif l.startswith("Generated mechanically"):
        out[i] = "Generated mechanically from `kb/claims.jsonl` at %s. Do not edit by hand. `kb/claims.jsonl` is the claim authority." % now
    elif l.startswith("Total claims:"):
        out[i] = "Total claims: **%d**" % len(records)

with open(INDEX, "w", encoding="utf-8", newline=NL) as fh:
    fh.write(NL.join(out) + NL)

rows = re.findall(r"^\|\s*(CLAIM-\d{3})", open(INDEX, encoding="utf-8").read(), re.M)
print("records", len(records), "rows", len(rows), "unique", len(set(rows)), "appended", missing)
