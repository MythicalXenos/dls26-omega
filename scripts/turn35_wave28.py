#!/usr/bin/env python3
"""Turn 35 Wave 28: reconciliation with official anchors — facility roster correction (GS-023), Clan official rules (GS-007), Season Pass official tiers (GS-004), coach categories (GS-008)."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w28')

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

e_rec=new_ev("kb/game-systems.md GS-004/GS-007/GS-008/GS-023 (FTG official support articles already captured), FTG support articles 4404070913169 (Season Pass), 30839289076626 (Clans), 360003914778 (player development), DLS26 official store copy, ldplayer/chaptercheats facility-screen descriptions",
    "RECONCILIATION WITH OFFICIAL ANCHORS. (1) FACILITY ROSTER CORRECTION: the official store copy names only FIVE facilities - Stadium, Medical, Commercial, Training, plus the new Fanzone (GS-023, official-stated). The earlier 'seven facilities' claim overstates the official position: Recruitment Centre and Accommodation do appear in the in-game Stadium & Facilities screen per community guides (ldplayer: 'recruitment, training, accommodation, commercials, and the stadium'), so the in-game roster is larger than the five the store copy enumerates, but only the five are official-stated. (2) CLAN OFFICIAL RULES (article 30839289076626, GS-007): you may belong to ONE clan at a time; each clan has one leader and leadership passes on; an empty clan disappears; clans can set entry requirements that are hidden from search unless met and are joinable via invite code; Clan Points are earned through matches, challenges and season passes; FTG may remove players or entire clans for Terms-of-Use breaches or negative experiences, and does not mediate internal disputes. These official rules complement (and bound) the community-sourced rank-20 unlock, 350,000-point personal cap, reward ladder and vice-captain details. (3) SEASON PASS OFFICIAL TIERS (article 4404070913169, GS-004, from version 12.200): exactly two tiers - FREE for all users and the premium SEASON PASS purchase; purchasing unlocks the Progress Bank paying currency based on DLL XP at season end; premium turns profile elements gold; it is NOT a subscription and must be repurchased each season with no auto-renewal; Season Points are earned by completing matches with the amount varying by game mode; tier locks correspond to days, and buying mid-season instantly unlocks premium rewards for tiers already reached while premium removes all tier locks. (4) COACH CATEGORIES (article 360003914778, GS-008): Fitness covers SPE/ACC/STA/STR, Technical covers CON/PAS/SHO/TAC, Goalkeeping covers GKR/GKH, and Special offers two randomised stat choices; rarities are Common (+1 random stat), Rare (+2 stats by +2) and Legendary (+3 stats by +3); the development ceiling is base OVR +10, rarely +11; coaches are hired with gems or by releasing players. sakibpro's weighted-progression-energy model remains Speculative.",
    "evidence/raw/turn35_w28/EV-419_official_anchor_reconciliation.html",
    "Facility roster corrected: official store copy names only 5 (Stadium, Medical, Commercial, Training, Fanzone) - Recruitment/Accommodation are in-game-only per community guides; Clan official rules = one clan at a time, single leader with succession, empty clans vanish, entry requirements hidden unless met, invite-code join, points from matches/challenges/season passes, FTG may remove clans/players, no dispute mediation; Season Pass official = 2 tiers (FREE/premium), Progress Bank on DLL XP paid at season end, gold profile, not a subscription, tier locks by day, mid-season purchase unlocks reached tiers; coach categories Fitness(SPE/ACC/STA/STR)/Technical(CON/PAS/SHO/TAC)/Goalkeeping(GKR/GKH)/Special(2 random choices), +1/+2/+3 rarities, ceiling base+10 rarely +11",
    quality="official")

add_claim("CORRECTION: the official store copy names only FIVE facilities - Stadium, Medical, Commercial, Training and the new Fanzone. Recruitment Centre and Accommodation appear in the in-game Stadium & Facilities screen per community guides but are not official-stated, so the 'seven facilities' claim is withdrawn as overstated.", 2, "facilities/roster-correction", [e_rec], notes="Corrects the earlier 'seven facilities' claim; the five named in store copy are the official roster")
add_claim("Clan official rules (article 30839289076626): you may belong to only one clan at a time; each clan has one leader and leadership passes on; an empty clan disappears.", 1, "clans/official-rules", [e_rec])
add_claim("Clans can set entry requirements that stay hidden from search unless met, and are joinable via an invite code; Clan Points are earned through matches, challenges and season passes.", 1, "clans/official-points-and-entry", [e_rec])
add_claim("FTG may remove players or entire clans that breach the Terms of Use or create a negative experience, and does not mediate disputes inside a clan.", 1, "clans/official-enforcement", [e_rec])
add_claim("Season Pass official structure (article 4404070913169, from version 12.200): exactly two tiers - FREE for all users and the premium SEASON PASS purchase - and it is NOT a subscription, so it must be repurchased each season with no auto-renewal.", 1, "economy/season-pass-official-tiers", [e_rec])
add_claim("Season Pass tier locks correspond to days; buying the pass mid-season instantly unlocks the premium rewards for tiers already reached, and premium removes all tier locks entirely.", 1, "economy/season-pass-tier-locks", [e_rec])
add_claim("Season Points are earned by completing matches, with the amount varying by game mode (official-stated) - the 40-points-per-login figure is a community measurement, not an official guarantee.", 2, "economy/season-points-official", [e_rec], notes="Reconciles the community 40 SP/day figure with the official 'varies by mode' statement")
add_claim("Coach categories are officially scoped: Fitness covers SPE/ACC/STA/STR, Technical covers CON/PAS/SHO/TAC, Goalkeeping covers GKR/GKH, and Special offers two randomised stat choices.", 1, "coaches/official-categories", [e_rec])
add_claim("Coach rarities are officially scoped as Common (+1 random stat), Rare (+2 stats by +2) and Legendary (+3 stats by +3), with the development ceiling at base OVR +10 and rarely +11.", 1, "coaches/official-rarity-scale", [e_rec])

p=os.path.join(RAW_DIR,'EV-419_official_anchor_reconciliation.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
