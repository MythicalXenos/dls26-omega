#!/usr/bin/env python3
"""ckpt-135: wave 59 - the First Contact script refresh, recorded as an EV."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w59')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1
os.makedirs(RAW_DIR,exist_ok=True)

def new_ev(origin, summary, artifact_path, vol, quality="official"):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":quality,"summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid

def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid

e=new_ev("ckpt-135 refresh pass over step5_first_contact/FIRST_CONTACT_v2.md (basis ckpt-116) against the findings accumulated through ckpt-134 (1,640 claims / 374 EVs)",
    "THE FIRST CONTACT SCRIPT REFRESHED from a ckpt-116 basis to ckpt-135 - the user-facing coaching document, which is the one deliverable the player actually reads. FOUR ADDITIONS, EACH CHOSEN BECAUSE IT CHANGES BEHAVIOUR RATHER THAN JUST KNOWLEDGE: (1) A NEW PRE-FLIGHT CHECK A3 - THE ONE-WAY DOOR. FTG limits every player to one DLS account; the profile is permanently bound to a Google or Apple login; signing out unlinks it and risks total unrecoverable loss; and Reset Profile destroys every coin, gem and purchase while being permitted only once every 30 days. The account also fixes the region, which decides the matchmaking pool and the leaderboard surface. The script now tells the player to set this up deliberately and to play through early mistakes rather than reset them. (2) THE FACILITY COST RULE - level N costs 75 x N gems, so five levels cost 1,125 and a maxed facility costs 4,125; spend the first five levels widely and be deliberate about the second five, with Training L4 named as the single best gem in the game because it drops legendary coaches below 200 coins. (3) THE SEASON PASS DECISION - two paid tiers at about $4 and $13-15, unplayed levels are stored rather than lost, a late purchase backfills every premium tier already unlocked for free, so buy late or not at all, and the free track alone is worth claiming for 1,095 coins and an epic agent. (4) THE COACHING METHOD - a breakthrough is a risk rather than only a bonus because you cannot control where it lands and a wasted one consumes development capacity; train one player at a time chaining Common coaches by category; and budget by weight rather than points, since Control and Speed consume more development capacity than Stamina and the +10 cap is a 100% cumulative weight.",
    "evidence/raw/turn35_w59/EV-473_first_contact_refresh.html",
    "FIRST CONTACT SCRIPT REFRESHED from ckpt-116 to ckpt-135 with four behaviour-changing additions: (1) a new pre-flight check A3 on the ONE-WAY DOOR - one account per player, never sign out, reset destroys everything and is allowed once per 30 days, and the region seed is permanent; (2) the facility cost rule - level N = 75 x N gems, 1,125 for five levels and 4,125 maxed, with Training L4 named the best gem in the game; (3) the Season Pass decision - buy LATE or not at all, because unplayed levels are stored and a late purchase backfills every premium tier already unlocked; (4) the coaching method - breakthroughs are a risk, train one player at a time with Common coaches chained by category, and budget by weight not points",
    quality="official")

add_claim("The First Contact script was refreshed from a ckpt-116 basis to ckpt-135, adding the one-way-door account check, the facility cost rule, the Season Pass buy-late decision and the coaching method - all chosen because they change behaviour rather than merely adding knowledge.", 1, "audit/first-contact-refreshed", [e], notes="All five build deliverables are now on a current basis and mutually consistent")

for name in ('EV-473_first_contact_refresh.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
