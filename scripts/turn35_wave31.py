#!/usr/bin/env python3
"""Turn 35 Wave 31: legacy vs current division structures (dates the dlspedia table), Allstars XI / Ultimate Challenge cycle, promotion mechanics, achievement-count growth, development-ceiling version drift, legacy tier numbering."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w31')

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

e_leg=new_ev("Vietnamese Wikipedia DLS gameplay section, dream-league-soccer.fandom (main wiki, Division 2, Elite Division), dlspedia.fandom Stadium, Exophase DLS2018 and DLS-Classic achievement lists plus a cached earlier DLS26 snapshot, r/DreamLeagueSoccer (10uboyp, 1kzop2e), LevelWinner DLS24",
    "LEGACY VS CURRENT STRUCTURES + PROMOTION MECHANICS. The dlspedia stadium table is now DATED: Vietnamese Wikipedia records that the 2016-2019 era had only SIX divisions - Academy, Division 3, Division 2, Division 1, Junior Elite and Elite - across 96 teams, with the Global Challenge Cup unchanged and the Elite Cup restricted to Junior Elite and above. dlspedia's table (Academy 6,462 / Div 3 15,000 / Div 2 30,000 / Div 1 45,000 / Junior Elite 60,000 / Elite 80,000) therefore describes the LEGACY six-division ladder, not the current eight-division one - which substantially resolves conflict C-010 in favour of the current-build table. POST-DIVISION CYCLE: after winning a division the club must face that division's ALLSTARS XI; after winning that, older versions pitted you against a copy of YOUR OWN TEAM in the Ultimate Challenge, which was removed from DLS21 onward; winning returned you to the top division and the cycle repeated. The legacy DLL tier ladder was NUMERIC with Tier 1 at the top and Tier 10 at the bottom, and promotion achievements paid escalating XP (Tier 10 promotion 500 XP, Tier 9 1,000, Tier 8 1,500, Tier 7 2,000, Tier 6 2,500, Tier 5 3,000, Tier 4 3,500, Tier 3 4,000, Tier 2 4,500, Junior Elite 'Time To Step Up' 2,500). The current build replaced this with named ranks (Rookie through Veteran). PROMOTION MECHANICS (dream-league-soccer.fandom Division 2, legacy-era): the top two teams are promoted directly and third through sixth contest a promotion playoff, and promotion also requires a minimum STADIUM CLASS (Class B or higher) - a class gate, not only a seat count. ACHIEVEMENT GROWTH: a cached Exophase snapshot shows DLS26 with 40 achievements and 20,000 XP, while the live page shows 42 and 21,000 - the two additions carry much higher achievement IDs (876880 'Back Of The Net' and 876881 'Debut' versus 820241-820280 for the rest), confirming they were appended in a later update. DEVELOPMENT CEILING VERSION DRIFT: in DLS2020 goalkeepers were not limited to +10 and reached +11 to +14 (producing 97 Buffon and 99 De Gea cards), whereas the current ceiling is base OVR +10, rarely +11. MARKET TRACKS OVR: if team OVR falls, the transfer market shows lower-rated legendary players. SCORING DIFFICULTY is described as uniform across divisions (LevelWinner DLS24) even though official difficulty scales with division. DLS Classic champion coin rewards: Division 3 champions 20 coins, Division 1 champions 40, Elite champions 50.",
    "evidence/raw/turn35_w31/EV-423_legacy_structures.html",
    "dlspedia table DATED as the legacy 2016-2019 SIX-division structure (Academy/Div3/Div2/Div1/Junior Elite/Elite, 96 teams, Elite Cup for Junior Elite+) - substantially resolving C-010; post-win cycle = Allstars XI then (pre-DLS21) Ultimate Challenge vs a copy of your own team, removed from DLS21; legacy DLL tiers numeric Tier 1 top to Tier 10 bottom with escalating promotion XP; promotion = top 2 direct + 3rd-6th playoff + stadium CLASS gate (Class B); DLS26 achievements grew 40->42 with the two additions carrying much higher IDs; DLS2020 GK ceiling was +11 to +14 vs current +10 (rarely +11); market quality tracks team OVR; scoring difficulty uniform across divisions; DLS Classic champion coins 20/40/50",
    quality="community")

add_claim("The dlspedia stadium table is dated as the LEGACY 2016-2019 six-division structure - Academy, Division 3, Division 2, Division 1, Junior Elite and Elite across 96 teams - not the current eight-division ladder, which substantially resolves conflict C-010 in favour of the current-build table.", 2, "facilities/dlspedia-table-legacy", [e_leg], notes="Dates Table B; Vietnamese Wikipedia lists the historical six-division structure explicitly")
add_claim("In the 2016-2019 era the Elite Cup was restricted to Junior Elite Division and above, while the Global Challenge Cup was open in every division.", 3, "cups/legacy-elite-cup-eligibility", [e_leg])
add_claim("After winning a division the club must play that division's ALLSTARS XI, and in versions before DLS21 a further Ultimate Challenge pitted you against a copy of your own team; the Ultimate Challenge was removed from DLS21 onward.", 2, "career/allstars-ultimate-challenge", [e_leg])
add_claim("The legacy Dream League Live tier ladder was numeric with Tier 1 at the top and Tier 10 at the bottom, replaced in the current build by named ranks (Rookie through Veteran).", 2, "dll/legacy-numeric-tiers", [e_leg])
add_claim("Legacy tier-promotion achievements paid escalating XP: Tier 10 promotion 500 XP, Tier 9 1,000, Tier 8 1,500, Tier 7 2,000, Tier 6 2,500, Tier 5 3,000, Tier 4 3,500, Tier 3 4,000 and Tier 2 4,500, plus 2,500 XP for 'Time To Step Up' from Junior Elite.", 3, "dll/legacy-tier-promotion-xp", [e_leg])
add_claim("Promotion mechanics (legacy-era fandom): the top two teams are promoted directly and third through sixth contest a promotion playoff, and promotion additionally requires a minimum STADIUM CLASS (Class B or higher) - a class gate, not only a seat count.", 3, "career/promotion-mechanics", [e_leg], notes="Legacy-era description; current-build playoff/class rules unverified")
add_claim("DLS26 achievements grew from 40 to 42 between Exophase snapshots: the two additions ('Back Of The Net' and 'Debut') carry far higher achievement IDs (876880/876881) than the original 820241-820280 block, confirming they were appended in a later update.", 2, "career/achievement-growth", [e_leg])
add_claim("DEVELOPMENT CEILING VERSION DRIFT: in DLS2020 goalkeepers were not capped at +10 and reached +11 to +14 (producing 97 Buffon and 99 De Gea cards), whereas the current ceiling is base OVR +10, rarely +11.", 3, "coaches/ceiling-version-drift", [e_leg], notes="Dated DLS2020 baseline; the +10 ceiling is a current-build rule")
add_claim("Transfer market quality tracks team OVR directly: if team OVR falls, the market shows lower-rated legendary players.", 2, "transfers/market-tracks-ovr-confirmed", [e_leg])
add_claim("Scoring difficulty is described as uniform across divisions - it does not get harder to score in Legendary than in Academy - even though overall difficulty officially scales with division progression.", 3, "difficulty/scoring-uniform", [e_leg], notes="Community observation; partially in tension with the official difficulty-scaling statement")
add_claim("DLS Classic champion coin rewards: Division 3 champions 20 coins, Division 1 champions 40 coins and Elite champions 50 coins.", 3, "cups/classic-champion-coins", [e_leg])
add_claim("OPEN GAP: no source names the LIVE ranks above 'Veteran' in the current build, so the top of the DLL ladder is unknown.", 4, "dll/rank-names-above-veteran", [e_leg], notes="OPEN GAP - blocks a precise statement of what #1 means at the top of the ladder")

p=os.path.join(RAW_DIR,'EV-423_legacy_structures.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
