#!/usr/bin/env python3
"""Turn-15 claim edits (pair sample 6). Writes kb/claims.jsonl with real newlines only."""
import json
import os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "kb", "claims.jsonl")
P = os.path.normpath(P)
NL = chr(10)


records = []
with open(P, "r", encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        if not line:
            continue
        records.append(json.loads(line))

for c in records:
    cid = c["claim_id"]
    if cid == "CLAIM-020":
        c["proposition"] = (
            "Player acquisition channels (official, article 360004066417): Transfers (new players appear each "
            "in-game week, i.e. after playing a single-player match), Scouts (a selection of players at a "
            "discounted rate), Agents (immediately add a player), Prize Ladder (awards special rare players when "
            "criteria are met). Separately (article 213851369), watching short video clips earns free coins "
            "subject to availability. That is an ADVERTISED FREE-COIN ROUTE, not the only one: the official coin "
            "list also credits match wins, draws, clean sheets, goals and objectives (CLAIM-019)."
        )
        c["challenges"] = [x for x in c.get("challenges", []) if "only" not in x.lower()]
        c["challenges"].append(
            "CORRECTED turn 15 (pair sample 6): the earlier wording said 'Free coins only via short video clips', "
            "which the source does not say and which contradicts the official coin list. Video-clip availability "
            "is also Critical-volatility (ad networks, CLAIM-026/115) while acquisition channels are stable; the "
            "claim now separates the two."
        )
        c["last_checked_by"] = "turn-15 pair sample (B)"
    elif cid == "CLAIM-029":
        c.setdefault("challenges", []).append(
            "Source says 'bux' (legacy wording); this claim glosses it as coins and therefore hides the same "
            "terminology drift that keeps C-003 (coach vs bux payout) unresolved. Read the payout type as "
            "build-dependent until C-003 is settled."
        )
        c["cross_refs"] = ["CLAIM-076", "CLAIM-114"]
        c["last_checked_by"] = "turn-15 pair sample (B)"
    elif cid == "CLAIM-103":
        c.setdefault("challenges", []).append(
            "Basis is DERIVED: this claim cites other claims (008/048/054/087), not evidence records directly. "
            "'Roughly monthly' is an inference from observed build dates, not a stated cadence. The 'summer 2026 "
            "World Cup window' example rests on CLAIM-095/096, which are Speculative single-source UGC - the "
            "example is illustrative, not established."
        )
        c["last_checked_by"] = "turn-15 pair sample (C)"
    elif cid == "CLAIM-033":
        c.setdefault("challenges", []).append(
            "COMPOUND CLAIM (noted turn 15): the card-colour taxonomy (stable, official, verbatim) and the "
            "re-signing/Recover/licensing rules (change with build and roster) are two mechanisms with different "
            "volatility under one tier. Card colours are the reliable half; read the re-signing half through "
            "CLAIM-114 and C-003."
        )
        c["last_checked_by"] = "turn-15 pair sample (D)"
    elif cid == "CLAIM-025":
        c.setdefault("challenges", []).append(
            "COMPOUND CLAIM (noted turn 15): release-schedule policy and DLS19-profile transfer are unrelated "
            "propositions under one ID. Both are accurate to their sources; the pairing is a hygiene defect, not "
            "an error. New claims must carry one mechanism each."
        )
        c["last_checked_by"] = "turn-15 pair sample (C)"

out = []
for c in records:
    out.append(json.dumps(c, sort_keys=True))

with open(P, "w", encoding="utf-8", newline=chr(10)) as fh:
    fh.write(NL.join(out) + NL)

data = open(P, "rb").read()
print("records", len(records))
print("bytes", len(data))
print("real_newlines", data.count(b"\n"))
print("literal_backslash_n", data.count(b"\\n"))
print("blank_pairs", data.count(b"\n\n"))
