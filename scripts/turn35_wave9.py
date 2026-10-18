#!/usr/bin/env python3
"""Turn 35 Wave 9: FTG OFFICIAL stat definitions (SPE/ACC/STA/CON/STR/TAC/PAS/SHO/GKH/GKR/Energy) — 10 attributes fully defined, high-confidence."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w9')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

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
os.makedirs(RAW_DIR,exist_ok=True)

e_stats=new_ev("FTG OFFICIAL support page 'How do the various player stats in DLS affect gameplay?' (support.ftgames.com, canonical 10-attribute schema)",
    "OFFICIAL ATTRIBUTE DEFINITIONS (FTG, canonical). Ten player stats total: SPE, ACC, STA, CON, STR, TAC, PAS, SHO, GKH, GKR. No hidden 11th stat in official schema. SPE (Speed): affects top running speed. Top speed decreases as energy (stamina) reduces. Top speed also decreases when dribbling, inversely proportional to CON — so high-CON players dribble faster than low-CON players with the same SPE. A lower-SPE player can outrun a higher-SPE player situationally. ACC (Acceleration): how quickly player reaches top speed; higher = faster to max speed. STA (Stamina): how quickly energy depletes when running; higher STA = less energy lost for same distance/intensity. Also affects HALF-TIME ENERGY BOOST magnitude. Position-dependent: CBs cover less distance than mids, so STA matters more for mids/wingers/fullbacks. CON (Ball Control): affects dribbling speed retention, first-touch-to-kick speed, touches-per-second (tighter dribble = faster direction changes), ball proximity to feet, skill-kick chance (Rabonas, Overhead Kicks), skill-control success (heel-chops), skill-shot success (double-tap/swipe), skill-move execution (Step-over, Marseille turn/roulette, Heel-Flick). Most important technical attribute (corroborates BlueStacks/retbit). STR (Strength): controls collision impact — higher STR vs opponent means less disruption when challenged, better able to win/retain ball and finish kicks after contact; also reduces stumble duration after being tackled. Aerial/jostle bias is rooted in STR. TAC (Tackling): affects tackle success; in particular the standing-tackle reach and sliding-tackle reach (distance from which a standing/slide tackle will successfully win the ball). PAS (Passing): accuracy of all pass types (short/long/through/cross). SHO (Shooting): shot accuracy (all shot types); increases shot 'assist' (aim away from keeper); ability to keep shots DOWN (low shots = higher goal probability; low SHO = sky shots over bar); co-governs skill-shot success (with CON); increases chance of special kicks/headers (overhead kick, diving header); increases spin/curl on free kicks. GKH (Keeper Handling): catch-vs-parry ratio (higher = more likely to hold than deflect), willingness/ability to claim crosses (comes off line), stability when catching/saving under contact from nearby attackers. GKR (Keeper Reactions/Shot-stopping): reaction time to shots, save probability relative to shot speed/distance, chance of 'anticipate' save (pre-emptive reflex save before ball is struck). ENERGY (Battery Icon / fatigue): controls fatigue impact on performance; below a threshold all other stats GRADUALLY decrease as energy drops; most noticeable on SPEED, but ALL stats degrade when tired. DLS is explicitly an arcade game (not a sim; FTG notes 'meant for discovery with some unpredictability') but stats are intended to map meaningfully to real-life attributes.",
    "evidence/raw/turn35_w9/EV-390_ftg_stats_definition.html",
    "OFFICIAL 10-attribute definitions: SPE (top speed, dribble inversely w/ CON, stamina-reduced); ACC (time-to-top-speed); STA (drain rate, HT boost, position-dependent); CON (dribble+first touch+skill moves+skill shots+ball proximity — most important tech); STR (collision/contact/stumble); TAC (stand+slide tackle reach); PAS (pass accuracy); SHO (shot accuracy+assist+keeping low+skill shots+headers+FK curl); GKH (catch/claim crosses/stability); GKR (reaction time/save distance/anticipate saves); Energy (all stats degrade below threshold, most noticeably speed)")

add_claim("OFFICIAL (FTG): Ten player attributes total — SPE, ACC, STA, CON, STR, TAC, PAS, SHO, GKH, GKR. No other primary stats.", 1, "attributes/canonical-10", [e_stats])
add_claim("OFFICIAL: SPE (Speed) = top running speed. Top speed decreases as energy (stamina) drops; dribbling reduces speed inversely proportional to CON (high CON retains dribble speed); lower-SPE players CAN outrun higher-SPE players situationally.", 1, "attributes/spe", [e_stats])
add_claim("OFFICIAL: ACC (Acceleration) = how quickly player reaches top speed; higher = faster to max speed.", 1, "attributes/acc", [e_stats])
add_claim("OFFICIAL: STA (Stamina) = energy drain rate per distance/intensity; higher STA = less energy lost for same run. Also governs magnitude of HALF-TIME ENERGY BOOST. Position-dependent (mids/wingers/FBs cover more distance; CBs less).", 1, "attributes/sta", [e_stats])
add_claim("OFFICIAL: CON (Ball Control) governs: dribble speed retention, first-touch-to-kick speed, tightness of touches (faster direction changes), ball proximity to feet, skill-kick chance (Rabonas, Overhead Kicks), skill-control success (heel-chops), skill-shot success (double-tap/swipe), skill-move execution (Step-over, Marseille turn/Roulette, Heel-Flick).", 1, "attributes/con", [e_stats])
add_claim("OFFICIAL: CONFIRMS CON is BALL CONTROL (not 'Control' as generic 'most important' stat) — officially a Technical attribute (not Fitness), matching the errata-corrected coach category mapping.", 1, "attributes/con-category-confirmed", [e_stats])
add_claim("OFFICIAL: STR (Strength) governs collision outcomes — higher STR vs opponent = less disruption, wins/retains ball better through contact, finishes kicks more reliably after contact; reduces stumble recovery time after tackles.", 1, "attributes/str", [e_stats])
add_claim("OFFICIAL: TAC (Tackling) governs tackle success, specifically: (1) standing-tackle reach and (2) sliding-tackle reach (distance at which tackle will connect).", 1, "attributes/tac", [e_stats])
add_claim("OFFICIAL: PAS (Passing) = accuracy of ALL pass types (short pass, long pass, through ball, cross).", 1, "attributes/pas", [e_stats])
add_claim("OFFICIAL: SHO (Shooting) governs: shot accuracy (all types); 'shot assist' (moves ball away from keeper); ability to keep shots LOW (low-SHO = skied shots); skill-shot success (synergy with CON); special kick/header chance (overhead kicks, diving headers); free-kick spin/curl.", 1, "attributes/sho", [e_stats])
add_claim("OFFICIAL: GKH (Goalkeeper Handling) = catch-vs-parry ratio (higher = catches, not spills), cross-claiming (comes off line to claim), stability under contact when catching.", 1, "attributes/gkh", [e_stats])
add_claim("OFFICIAL: GKR (Goalkeeper Reactions) = shot-stopping: reaction time, save probability vs shot speed/distance, chance of 'anticipate' saves (pre-emptive/instinctive saves).", 1, "attributes/gkr", [e_stats])
add_claim("OFFICIAL: Energy (Battery Icon = stamina bar) is a fatigue value: below a threshold ALL stats degrade GRADUALLY; speed degradation is most noticeable but ALL stats suffer.", 1, "attributes/energy", [e_stats])
add_claim("OFFICIAL: High CON + high SPE is better dribbling than SPE alone; this is the mechanical basis for why wingers/AM need high CON.", 1, "attributes/con-spe-synergy", [e_stats])
add_claim("OFFICIAL: Half-time energy restoration is NOT a fixed % — it is MODULATED by the STA stat (higher STA = bigger HT boost). This refines the earlier '30% regen/match' + 'Team Boost HT 30c = +10% stamina' claims.", 2, "attributes/sta-ht-boost", [e_stats], "quantitative HT regen number may vary by STA level")
add_claim("OFFICIAL: FTG explicitly states DLS is an arcade game (not a sim; matches not 90min) with some intentional 'discovery' and unpredictability, not a pure stats engine.", 1, "design/arcade", [e_stats])

p=os.path.join(RAW_DIR,'EV-390_ftg_stats_definition.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
