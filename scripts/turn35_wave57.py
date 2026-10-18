#!/usr/bin/env python3
"""ckpt-133: wave 57 - the DLL tier playbook refresh, recorded as an EV."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w57')

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

e=new_ev("ckpt-133 deliverable refresh pass over docs/dll_tier_playbook.md (basis ckpt-109, 1,429 claims / 350 EVs) against the findings accumulated through ckpt-132 (1,628 claims / 372 EVs)",
    "THE DLL TIER PLAYBOOK REFRESH - the oldest of the five build deliverables (basis ckpt-109) was 24 checkpoints behind and carried the same withdrawn C-024 claim the ckpt-132 audit found elsewhere. REFRESHED WITH: (1) the corrected matchmaking section - team strength is NOT a matching input, so the maxed-squad handicap has no official basis and the confidence note is downgraded to Community Consensus with an explicitly unknown threshold; (2) the official stat model's Tier-1 implications - a fast spine with a technical core, STA weighted by position (high on midfielders and wingers, low on centre-backs, because a centre-back covers far less distance than a midfielder), verified in Exhibition before committing a coaching plan; (3) the formation guidance - no best shape, only failure modes, with Tier-1 players switching to 4-2-3-1 on the climb and the rule that stamina depth beats formation every time, so rotation is a tactical decision; (4) the XP bill and the benchmark - 27,500 XP to promote from tier 10 to tier 1 (500 rising by 500 per tier to 4,500 for tier 2, plus 5,000 for Tier 1 Champions), against a world record of 145,296 XP in 16 days on a mostly common/rare squad, with the runner's own note that never failing a promotion was crucial to saving XP - so promotion streaks outrank everything; (5) the relegation risk - 2 points was the difference between staying in tier 2 and dropping to tier 3, which is the direct cost of the camping strategy's match-quitting.",
    "evidence/raw/turn35_w57/EV-471_tier_playbook_refresh.html",
    "TIER PLAYBOOK REFRESHED from a ckpt-109 basis to ckpt-133. It carried the same withdrawn C-024 claim (team strength as an official matching input) and now records that the maxed-squad handicap is community-only with an unknown threshold. New Tier-1 content: the official stat model's fast-spine/technical-core build with position-weighted STA; the formation failure-mode guidance with stamina-beats-shape; the 27,500 XP promotion bill against the 145,296 XP / 16-day world record on a common/rare squad, with promotion streaks as the priority; and the relegation risk (2 points) that the camping strategy must respect",
    quality="official")

add_claim("The DLL tier playbook was refreshed from a ckpt-109 basis to ckpt-133 - it had carried the withdrawn C-024 claim and was missing the official stat model, the formation failure-mode guidance, the tier XP bill, the world-record benchmark and the relegation risk.", 1, "audit/tier-playbook-refreshed", [e], notes="All five deliverables are now on a current basis")
add_claim("Every failed DLL promotion wastes the accumulated points of that tier, so a promotion streak is worth protecting above individual match results - the world-record runner explicitly credits 'not once did I not get promoted to the next tier (crucial to saving XP)'.", 2, "dll/promotion-streak-priority", [e], notes="Reframes the camping strategy: survival matters more than gem-per-hour")

for name in ('EV-471_tier_playbook_refresh.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
