#!/usr/bin/env python3
"""Turn 16: merge the sibling branch's service records into the workspace log and
repair a 12-ID namespace collision.

Background: both sessions wrote into logs/sources_visited.json using the
S-20261017-NNN namespace. IDs 001-050 (and 057) are identical. IDs 051-063
(excluding 057) contain DIFFERENT records in the two logs, and the sibling
continued to 069. Any citation of S-20261017-05x from this workspace has been
ambiguous.

Repair, in order:
  1. take the sibling's 051-069 as canonical for that range (they are the
     earlier, higher-content records);
  2. renumber this workspace's colliding entries to 070-081;
  3. record the mapping in the log itself so the change is auditable;
  4. verify no ID appears twice and no URL is lost.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OURS = os.path.join(ROOT, "logs", "sources_visited.json")
SIB = "/tmp/sv_22655.json"

ours = json.load(open(OURS, encoding="utf-8"))
sib = json.load(open(SIB, encoding="utf-8"))

o_entries = {e["id"]: e for e in ours["entries"]}
s_entries = {e["id"]: e for e in sib["entries"]}

colliding = []
for i in sorted(o_entries):
    if i in s_entries and o_entries[i].get("url_or_query") != s_entries[i].get("url_or_query"):
        colliding.append(i)

print("colliding ids:", len(colliding), colliding)

# new ids continue after the highest id in either log
all_ids = sorted(set(o_entries) | set(s_entries))
highest = max(int(i.rsplit("-", 1)[1]) for i in all_ids)
mapping = {}
nxt = highest + 1
for i in colliding:
    mapping[i] = "S-20261017-%03d" % nxt
    nxt += 1

# 1 + 2: build the merged entry list
merged = []
taken = set()
for i in sorted(set(o_entries) | set(s_entries)):
    if i in mapping:
        e = dict(o_entries[i])
        e["id"] = mapping[i]
        e["renumbered_from"] = i
        e["renumber_reason"] = (
            "ID namespace collision with branch arena/22655f48-dls26-omega: that session "
            "already used " + i + " for a different retrieval. Renumbered turn 16 (OBS-017)."
        )
        merged.append(e)
        taken.add(mapping[i])
    elif i in s_entries and (i not in o_entries or i in colliding):
        e = dict(s_entries[i])
        e["imported_from"] = "arena/22655f48-dls26-omega"
        merged.append(e)
        taken.add(i)
    else:
        merged.append(dict(o_entries[i]))
        taken.add(i)

# siblings that exist only on that branch (064-069)
for i in sorted(s_entries):
    if i not in taken:
        e = dict(s_entries[i])
        e["imported_from"] = "arena/22655f48-dls26-omega"
        merged.append(e)
        taken.add(i)

merged.sort(key=lambda e: e["id"])

ours["entries"] = merged
ours.setdefault("id_repairs", []).append({
    "at": "2026-10-17T20:55:00Z",
    "session": "sess-20261017-001",
    "turn": 16,
    "issue": "OBS-017 - S-20261017-051..063 (except 057) were assigned to different retrievals by this session and by branch arena/22655f48-dls26-omega.",
    "action": "This session's colliding records renumbered; the sibling's 051-069 imported as canonical for that range; sibling-only 064-069 imported.",
    "mapping": mapping,
    "entries_before": len(o_entries),
    "sibling_entries": len(s_entries),
    "entries_after": len(merged),
    "rule_for_future": "Continue numbering from max(existing)+1 after fetching all sibling refs. Never assume a date-based namespace is single-writer.",
})

with open(OURS, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(ours, fh, indent=2, ensure_ascii=False)
    fh.write("\n")

# verify
check = json.load(open(OURS, encoding="utf-8"))["entries"]
ids = [e["id"] for e in check]
urls = [e.get("url_or_query") for e in check]
print("entries after:", len(check))
print("unique ids:", len(set(ids)) == len(ids), "dupes:", len(ids) - len(set(ids)))
print("unique urls:", len(set(urls)), "of", len(urls))
print("mapping:", json.dumps(mapping, indent=1))
