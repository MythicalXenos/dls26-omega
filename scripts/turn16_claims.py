#!/usr/bin/env python3
"""Turn 16: append four claims from cross-branch captures and upgrade summary-only witnesses.

Writes kb/claims.jsonl with real newlines only, and verifies byte structure.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "kb", "claims.jsonl")
NL = chr(10)

records = []
with open(P, "r", encoding="utf-8") as fh:
    for line in fh:
        if line.strip():
            records.append(json.loads(line))

by_id = {c["claim_id"]: c for c in records}
now = "2026-10-17T21:00:00Z"

# --- witness upgrades: replace derived-summary witnesses with service records ---
upgrades = {
    "CLAIM-113": ["S-20261017-051 (sibling branch service record, article 360004222118, full text 2026-10-17)"],
    "CLAIM-114": ["S-20261017-053 (sibling branch service record, article 360003945617, full text 2026-10-17)", "CLAIM-032", "CLAIM-076"],
    "CLAIM-115": ["S-20261017-055 (sibling branch service record, articles 360017166918 + 360005680437 + 360004718318)", "CLAIM-026"],
    "CLAIM-116": ["S-20261017-057 (sibling branch service record, dlsinside.com, build 13430, 2026-10-17)"],
    "CLAIM-117": ["S-20261017-057 (sibling branch service record, dlsinside blog 'DLS 27' dated 25 Aug 2026)"],
    "CLAIM-101": ["S-20261017-050 (sibling branch service record: megathread day 3 reports reserves + fixed eight subs)"],
    "CLAIM-102": ["S-20261017-008 (sibling branch service record: gamingonphone 50-60 OVR start)"],
    "CLAIM-104": ["S-20261017-008 (sibling branch service record: sakibpro squad builder team-OVR formula)"],
    "CLAIM-105": ["S-20261017-008 (sibling branch service record: reddit ratings theory 'trained = base+1')"],
    "CLAIM-097": ["S-20261017-008 (sibling branch service record: sakibpro squad builder)"],
}
for cid, ev in upgrades.items():
    c = by_id[cid]
    c["supporting_evidence"] = ev
    c["last_checked_by"] = "turn-16 witness upgrade (summary -> service record)"
    c.setdefault("challenges", []).append(
        "Witness upgraded turn 16 from a kb/*.md derived summary to the originating service record "
        "on branch arena/22655f48-dls26-omega. Both are summaries of a fetch; neither is the page body. "
        "The upgrade improves traceability, not evidential strength - the independence limit (D-03) is unchanged."
    )

# CLAIM-090 and CLAIM-099 keep their existing evidence; note the merge
for cid in ("CLAIM-090",):
    by_id[cid].setdefault("challenges", []).append(
        "Witness is still a derived megathread summary (M-003) plus EV-102; the service record for the "
        "megathread (S-20261017-050) was located in turn 16 and corroborates the 'scripts' phrasing but is a search summary."
    )

# --- new claims ---
def add(cid, prop, tier, vol, ev, due, chall, cross=None):
    records.append({
        "claim_id": cid,
        "proposition": prop,
        "context_build": "official-support article; capture 2026-10-17T17:10Z on branch arena/22655f48-dls26-omega; summary-only provenance",
        "confidence_tier": tier,
        "volatility_tier": vol,
        "supporting_evidence": ev,
        "contradicting_evidence": [],
        "last_valid_check": "2026-10-17T17:10:00Z",
        "last_attempt": "2026-10-17T17:10:00Z",
        "last_checked_by": "turn-16 cross-branch merge",
        "next_due": due,
        "origin_history": [{"at": "2026-10-17", "note": "fetched on the sibling branch and recorded only as a service summary; merged into this workspace in turn 16", "origins": ["official-stated"]}],
        "challenges": chall,
        "replacements": None,
        "cross_refs": cross or [],
        "context_evidence": [],
    })

add(
    "CLAIM-120",
    "Control-button captions ('Low Kick', 'Hard Kick', 'Lofted Kick') can be removed: Game Settings > Display > Descriptive Button Text OFF, from in-game or the Main Menu; re-enable with ON. This is the setting behind much of the launch-era 'clear input is wrong' complaint (CLAIM-091): the captions describe the button, not the action the game will take in that situation.",
    "High Confidence", "Low",
    ["EV-226 (cross-branch capture record, summary-only provenance)"],
    "2026-11-17",
    ["Summary-only witness", "The article does not say whether the setting affects only captions or also any assist behaviour - do not claim it changes gameplay"],
    ["CLAIM-091", "CLAIM-106"],
)

add(
    "CLAIM-121",
    "Dream League Live emoji system (official 360020938198): six emojis available by default; further emojis are earned or purchased and chosen in Emoji Selection; only six can be active at once, so swapping is required. Access is My Profile (top-right of the Main Menu, beside team and manager name) > Emojis. Chat can be disabled entirely: gear icon > Game > Multiplayer Chat OFF.",
    "High Confidence", "Low",
    ["EV-227 (cross-branch capture record, summary-only provenance)"],
    "2026-11-17",
    ["Summary-only witness", "The claim is about the UI; it says nothing about whether emoji use is penalised or rewarded"],
    ["CLAIM-075"],
)

add(
    "CLAIM-122",
    "Custom imported kits and logos are NOT visible to opponents in Dream League Live (official 360021064298): the opponent does not see yours and you do not see theirs. FTG acknowledges the demand and states it is not possible for several reasons, without listing them. Practical consequence: kit customisation is a personal/career and offline surface, not a multiplayer status signal.",
    "High Confidence", "Low",
    ["EV-228 (cross-branch capture record, summary-only provenance)", "CLAIM-074 (kit customisation surface)"],
    "2026-11-17",
    ["Summary-only witness", "Community guides and showcase videos imply visible kits; those show career or capture footage, not DLL opponent view"],
    ["CLAIM-074", "CLAIM-099"],
)

add(
    "CLAIM-123",
    "OFFICIAL FAIRNESS STANCE (article 360000842697): DLS is a game, not an accurate simulation of football or physics; FTG balances fun against realism; unpredictable situations occur 'just like in real life', including unrealistic ball/player behaviour and referee decisions the player disagrees with; 'luck forms a part of the experience'; 'Ultimately it's the same for all players and above all else we consider our games fair'. FTG reviews feedback and fixes what harms enjoyment, but states not everything will be addressed, and asks that genuine bugs be reported.",
    "High Confidence", "Low",
    ["EV-229 (cross-branch capture record, summary-only provenance)", "CLAIM-024", "CLAIM-044"],
    "2027-01-17",
    ["This is a POLICY statement, not a measurement: it does not show the implementation is unbiased", "Establishes only that variance is acknowledged; a one-match 'scripted' complaint is neither proven nor refuted by it", "Bears on mission design: a '#1' target must span enough matches for luck to average out"],
    ["CLAIM-044", "CLAIM-024", "CLAIM-090"],
)

# keep file ordered by claim number
records.sort(key=lambda c: int(c["claim_id"].split("-")[1]))

with open(P, "w", encoding="utf-8", newline=NL) as fh:
    fh.write(NL.join(json.dumps(c, sort_keys=True) for c in records) + NL)

data = open(P, "rb").read()
print("records", len(records))
print("real_newlines", data.count(b"\n"))
print("literal_backslash_n", data.count(b"\\n"))
print("blank_pairs", data.count(b"\n\n"))
print("ids", records[-1]["claim_id"], "unique", len({c["claim_id"] for c in records}))
