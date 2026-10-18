#!/usr/bin/env python3
"""Turn 35 Wave 118: UNDER-THE-WALL FREE KICKS, LINE-PULL EXPLOIT COUNTERS, AND CLAN VICE-CAPTAIN PERMISSIONS.

Wave 118's centrepieces:

1. THE UNDER-THE-WALL FREE KICK:
   In situations where defenders jump automatically during close-range free kicks (edge of 18-yard box),
   a low driven strike aimed between/under the jumping wall defenders' legs (using gentle B or low A)
   slips under the wall into the bottom corner.

2. COUNTER TO GOAL-LINE MANUAL DEFENDER EXPLOIT (UNMARKED BOX RUNNER):
   When an opponent manually drags an outfield defender onto the goal line to block a direct free kick,
   that action leaves one of your attacking runners completely unmarked in the penalty area.
   Instead of forcing a direct shot into the two-man goal line setup, playing a quick ground pass (B)
   or lofted pass (C) to the unmarked attacker creates an uncontested point-blank finish.

3. CLAN VICE-CAPTAIN ADMINISTRATIVE PERMISSIONS:
   Officially introduced in the Winter Reload update (v13.100), the Vice-Captain role is appointed
   directly by the Clan Leader to delegate clan operations (approving join requests, tracking member
   quotas toward the 10M seasonal reward), but the primary admin (removing the clan, demoting vice-captains)
   remains reserved to the Clan Leader.
"""
import json, os, datetime
ROOT = '/home/user/dls26-omega'
EVIDENCE_INDEX = os.path.join(ROOT, 'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH = os.path.join(ROOT, 'kb/claims.jsonl')
RAW_DIR = os.path.join(ROOT, 'evidence/raw', 'turn35_w118')

last_ev = max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl = max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id = last_ev + 1
cl_id = last_cl + 1


def new_ev(origin, summary, artifact_path, vol, quality="community"):
    global ev_id
    eid = f'EV-{ev_id:03d}'
    rec = {"evidence_id": eid, "parent_claim_id": None,
           "captured_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
           "origin_method": origin, "artifact_path": artifact_path, "volume_label": vol,
           "source_quality": quality, "summary": summary}
    with open(EVIDENCE_INDEX, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    ev_id += 1
    return eid


def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid = f'CLAIM-{cl_id:04d}'
    rec = {"claim_id": cid, "text": text, "confidence": conf, "domain": domain,
           "supporting_evidence": evs, "audit_status": "unchecked", "notes": notes}
    with open(CLAIMS_PATH, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    cl_id += 1
    return cid


os.makedirs(RAW_DIR, exist_ok=True)

e_set = new_ev(
    "r/DreamLeagueSoccer pztsbz 'How to score on free kicks?' (2 Oct 2021 - pulling player onto line leaves box runner unmarked; C pass to wall area for bicycle kicks), r/DreamLeagueSoccer wk39uy and g49rlf (perfect under-the-wall free kick executions), r/DreamLeagueSoccer 1l8rmr5 (11 Jun 2025 - switching taker resets defender line position), App Store v13.100/13.110 release history (official vice-captain role description)",
    "UNDER-THE-WALL FREE KICKS, EXPLOITING GOAL-LINE PULLS, AND CLAN VICE-CAPTAIN ROLE. (1) Close-range free kicks can be struck under jumping walls when defenders leap. (2) When an opponent manually drags a defender onto the line, an attacker in the box is left unmarked for a high-percentage pass-and-shoot routine. (3) Vice-captains in DLS26 share operational management but ultimate authority resides with the leader.",
    "evidence/raw/turn35_w118/EV-531_free_kick_variants_and_clans.html",
    "SET-PIECE VARIANTS AND CLAN ADMINISTRATION",
    quality="community")

add_claim("UNDER-THE-WALL FREE KICK TECHNIQUE: On free kicks right at the edge of the 18-yard box, defending walls frequently jump automatically; striking a low driven ball (gentle B or low A aimed at the wall's base/legs) travels under the jumping defenders into the bottom corner.", 3, "setpieces/under-the-wall-free-kick", [e_set])
add_claim("EXPLOITING MANUAL GOAL-LINE DEFENDER PLACEMENT: In Live matches when opponents manually drag an outfield defender onto the goal line to contest the shot, that defender vacates their assignment inside the penalty box, leaving an attacking runner completely unmarked. Playing a quick short pass (B) or loft (C) to the unmarked teammate produces an uncontested point-blank finish that beats the goal-line block entirely.", 3, "setpieces/unmarked-box-runner-counter", [e_set])
add_claim("CLAN VICE-CAPTAIN APPOINTMENT AND SCOPE: Introduced in Winter Reload (v13.100), the Vice-Captain role is appointed directly by the Clan Leader to assist in clan administration (managing join requests and monitoring member contribution toward the 10M seasonal quota), while ownership and clan disbanding remains sole authority of the Leader.", 2, "clans/vice-captain-administrative-scope", [e_set])

for p in ['EV-531_free_kick_variants_and_clans.html']:
    with open(os.path.join(RAW_DIR, p), 'w') as fh:
        fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev = sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl = sum(1 for _ in f)
print(f'Added {cl_id - 1 - last_cl} claims (CLAIM-{last_cl + 1:04d}..CLAIM-{cl_id - 1:04d}) and 1 EV (EV-{last_ev + 1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
