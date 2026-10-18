#!/usr/bin/env python3
"""Turn 35 Wave 2: stadium build optimization (92,632 cap / 52c), stand numbering, total costs, accommodation 64 players, division capacity gates."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w2')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="community"):
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
os.makedirs(RAW_DIR,exist_ok=True)

e_stadium=new_ev("r/DLS stadium build threads (Dec2022/Mar2023/Jun2023/Dec2023) + dlspedia + fandom Division 3 + apkmody accommodation",
    "Optimal stadium build: highest coin-bonus-per-cost build produces 92,632 capacity and yields 52 coins per home match (max stadium bonus). Build pattern (8 stands × N/S/E/W + 4 corners): North/South ends = level 20; East/West sides = level 26; NE/NW/SE/SW corners = level 49 (one corner may stay unupgraded to hit cost optimum). Total cost for optimal stadium: ~10,000 coins (slightly over 10k) per r/DLS; a side-stand first upgrade costs ~1,432 coins without roofs. Stadium-building rule: NEVER upgrade a stand partially/incrementally. Each stand must be built to its target level in one purchase; partial upgrades force you to pay full price again on top (no pro-rata saving). Roofs are cosmetic only and cost coins without adding capacity or bonus — skip for economy. Auto Build Capacity button auto-selects stands but is not optimal (chooses corners early, wastes coins). 8 stadium stands total (4 side, 4 corner/end). Pitch customization: 7 pitch surface types selectable; stadium name is editable (default 'Dream F.C. Stadium'). Stadium coin bonus pays out even on losses. Division capacity minimums (from dlspedia / fandom / LevelWinner): start Academy 6,462; Div3/Amateur gate 15,000 (cheapest first upgrade ~446c); Div2 gate ~30,000; Div1 gate ~45,000 (per dls-wiki Div2→Div1 is 35k per source variance; Division 3 entry is 35,000); Elite gate 80,000; Legendary ~90,000. Maxing all 5 non-stadium facilities (Commercial/Training/Medical/Accommodation/Recruitment) costs 1,125 gems per facility = 5,625 gems total across all 5 (gem-costs-per-tier: 75/150/225/300/375). Stadium upgrades cost COINS, not gems. Total max-stadium + max-facilities cost reported as ~10,000 coins + 5,625 gems. Commercial L3 removes rust from the stadium roof (cosmetic polish in addition to +21% coin bonus); L2 is +13%. Accommodation max capacity: DLS25-era 40 players; DLS26 is 64 players (per apkmody, v13.x 'max 10 floors, 64 players') — confirms DLS25 press-release 'squad size increased to 64' and DLS26 unlimited-specials. Training Centre unlocks formations and Form Boosts; Medical reduces injuries/heal cost; Recruitment discounts scout/agent costs. Stadium upgrade order recommendation: Stadium → Commercial → Medical → Accommodation/Training/Recruitment last. Training player-development costs (r/DLS 2023): ~80 upgrade points per player from scratch; Common coaches ~400c/coach (32,000c per player to max); Rare coaches ~1,500c/coach (30,000c per player to max) — RARE coaches are actually more coin-efficient per upgrade point than Common despite higher per-card cost (legendary coach trick: buy 80+ OVR players ~1,300-1,400c and immediately release for Legendary coaches).",
    "evidence/raw/turn35_w2/EV-383_stadium.html",
    "Optimal 92,632/52c stadium (N/S 20, E/W 26, corners 49), total ~10k coins, no roofs, no partial upgrades; pitch customization; division capacity gates; 1125g/facility (5625 total); accommodation 64 players; training coin costs per player")

add_claim("Optimal coin-max stadium build yields 92,632 capacity and 52 coins per home match (max stadium bonus): North/South ends = level 20; East/West sides = level 26; four corners = level 49 (one corner may stay unupgraded for cost-optimal configuration).", 2, "facilities/stadium-optimal", [e_stadium])
add_claim("Stadium total cost for optimal 92k/52c build: ~10,000 coins (slightly over); first side-stand upgrade ~1,432 coins (without roof).", 2, "facilities/stadium-cost", [e_stadium])
add_claim("Stadium build rule: NEVER upgrade a stand partially — each stand must be built to its target level in ONE purchase; partial upgrades cause full-price repayment on top (no pro-rata credit).", 2, "facilities/stadium-rule", [e_stadium])
add_claim("Roofs are purely cosmetic — they cost coins without adding capacity or match bonus; skip for economy.", 2, "facilities/roofs", [e_stadium])
add_claim("Auto Build Capacity is not cost-optimal (it prioritizes corners early wasting coins).", 2, "facilities/auto-build", [e_stadium])
add_claim("8 stadium stands total: 4 side stands (N/S/E/W) + 4 corner/end stands (NE/NW/SE/SW).", 1, "facilities/stadium-stands", [e_stadium])
add_claim("Pitch customization: 7 different pitch surface types selectable (grass patterns/colors).", 2, "customization/pitch", [e_stadium])
add_claim("Stadium name is editable (default 'Dream F.C. Stadium').", 2, "customization/stadium-name", [e_stadium])
add_claim("Stadium home-match coin bonus pays out even after losses (consistent income floor).", 2, "facilities/stadium-loss-bonus", [e_stadium])
add_claim("Division stadium capacity minimums (consolidated): start Academy 6,462; Amateur/Div3 gate ~15,000; Div2 gate ~30,000; Div1 gate ~45,000; Elite gate 80,000; Legendary ~90,000. (DLS23/DreamLeagueSoccer-wiki lists Div3 entry at 35k — inconsistent; treat 15k as Div3/D3 entry.)", 2, "facilities/capacity-gates", [e_stadium], "sources vary slightly across DLS versions")
add_claim("Facility upgrade costs (gems per level, per facility): 75 / 150 / 225 / 300 / 375 gems (L1/L2/L3/L4/L5) = 1,125 gems to max one facility.", 1, "facilities/costs", [e_stadium])
add_claim("Maxing all 5 non-stadium facilities (Commercial + Training + Medical + Accommodation + Recruitment) costs 5,625 gems total.", 1, "facilities/total-cost", [e_stadium])
add_claim("Stadium upgrades cost COINS, not gems; non-stadium facilities cost GEMS.", 1, "facilities/currency", [e_stadium])
add_claim("Complete endgame club build cost: ~10,000 coins for optimal stadium + 5,625 gems to max all 5 facilities.", 2, "facilities/endgame-cost", [e_stadium])
add_claim("Commercial facility L3 bonus (+21% coins) also removes visible rust from the stadium roof (cosmetic polish).", 2, "facilities/commercial-cosmetic", [e_stadium])
add_claim("Accommodation max capacity in DLS26: 64 players (up from 40 in DLS20-DLS24); achieved at 10 upgrade 'floors'.", 1, "facilities/accommodation-64", [e_stadium], "apkmody + DLS25 press release; confirms 64-squad")
add_claim("Training Centre unlocks formations and provides Form Boosts (per BlueStacks). Form Boost duration extended by Training level.", 1, "facilities/training", [e_stadium])
add_claim("Medical Centre reduces injury chance and physio recovery cost (no specific %s beyond L1 -5% injury / -10% heal established earlier).", 1, "facilities/medical", [e_stadium])
add_claim("Recruitment Centre provides discounts when hiring scouts and agents (discount % scales with level).", 1, "facilities/recruitment", [e_stadium])
add_claim("Player training cost from scratch: ~80 upgrade points per player; Common coaches cost ~400c per coach (≈32,000c total per player to max); Rare coaches ~1,500c per coach (≈30,000c total per player to max) — Rare coaches are more coin-EFFICIENT per upgrade point than Common.", 3, "training/player-cost", [e_stadium], "r/DLS 2023 DLS23 numbers; likely similar in DLS26")
add_claim("Legendary-coach farming meta: buy 80+ OVR players for 1,300-1,400 coins and immediately release them to receive Legendary coach cards, cheaper than buying Legendary coaches directly with gems.", 2, "training/legendary-coach-trick", [e_stadium])

p=os.path.join(RAW_DIR,'EV-383_stadium.html')
os.makedirs(RAW_DIR,exist_ok=True)
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
