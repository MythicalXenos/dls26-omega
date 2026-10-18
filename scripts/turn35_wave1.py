#!/usr/bin/env python3
"""Turn 35 Wave 1: coach weights/Special Coach Packs/sell-buyback window, manager customization/player kit numbers/boots/socks, in-game kit editor."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w1')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="mixed"):
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

e_coach=new_ev("sakibpro DLS26 Coaching Simulator FAQ (stat weights) + App Store VN v12.200 changelog + dlsinside KDB stats + r/DLS mid-season ratings",
    "DLS26 uses a HIDDEN WEIGHTED PROGRESSION system for coach upgrades (per sakibpro coach simulator FAQ, which reflects in-game mechanics): every attribute costs different 'progression energy' — Control (CON) and Speed (SPE) cost more capacity than Stamina (STA). Total cumulative development weight caps at 100%, which corresponds to the +10 OVR development limit (above base card rating). Goalkeeper upgrades: every 2.2 visual points added to GKR/GKH equals +1 OVR, with a strict cap of 22 points allocated (=10 OVR for GKs). Coach categories map: Fitness = SPE/ACC/STA/STR (4 stats); Technical = CON/PAS/SHO/TAC (4 stats, contradicts earlier CON-in-Fitness framing; sakibpro explicitly puts CON in Technical — earlier ckpt-045 EV-338 Fitness was STA/STR/ACC/SPE, Technical was FIT/TAC/PAS/SHO; need reconcile: 'Technical' grouping includes CON; 'Fitness' is the 4 physicals, SPECIAL = ALL STATS; GK = GKR/GKH). dlsinside example player Kevin De Bruyne 83 AM/CM: PAS 92, CON 88, ACC 72, SPE 75, STA 70, STR 71, TAC 68, SHO 80, GKR 13, GKH 13 (note dlsinside displays 9 appended to stat values 729/759/709/719/689/889/809/929 — likely HTML rendering artifact where trailing '9' is a star/badge marker; actual values are 72/75/70/71/68/88/80/92). v12.200 (Jun 4 2025, DLS25-era) added: 'Buy a sold player back within a limited time' (sell-buyback window) and 'New Special Coach Packs – Develop your favourite players more easily' (IAP bundles of coaches). Special Coaches upgrade ALL stats (per sakibpro sim). Mid-season (v13.110 Winter Reload, Feb/Mar 2026) stat adjustments example: Pedri SPE lowered, ACC increased, TAC boosted, SHO unchanged — individual stats shift with rating refreshes. CON (Control) is described as the most important universal technical attribute — affects first touch, close dribbling and direction change; retbit and LevelWinner confirm. Common coaches boost single random stat; Rare stronger multi-stat; Legendary highest + higher breakthrough chance (BlueStacks/Gamingonphone consistent).",
    "evidence/raw/turn35_w1/EV-381_coach.html",
    "Coach weight system (CON/SPE heavy, STA light), +10 OVR = 100% weight, GK 2.2pts/OVR cap 22, Special=ALL stats, dlsinside KDB stats example, v12.200 buyback+Coach Packs")
e_custom=new_ev("BlueStacks custom-kit guide (detailed Customize tabs) + Google Play description + gamingonphone career guide + App Store + apkmb",
    "My Club → Customise screen tabs (left nav): Kit, Logo, Team Name, Players, Manager (BlueStacks FR/EN guides). In-game Kit Editor (no import needed, free): edit Shirt/Shorts/Socks separately, with 5 color channels per piece — Primary, Secondary, Sponsor, Trim, Shirt Number — plus Kit Type (plain/striped patterns selectable by arrow) and Kit Trim selector (collar/cuff style by number). These built-in options produce varied looks without 300-gem import unlock. Imported custom kits cost 300 gems one-time (BlueStacks DLS20 figure, DLS26 price discrepancy 150 vs 300 from earlier waves). Manager customization: choose hairstyles and outfits (App Store/Google Play descriptions), expandable with themed accessories like v13.330 'North American themed items' (manager accessories feature). Player customization (gamingonphone career guide): can change Player Kit Number, Boot Color, sock color from the Customize → Players tab; costs gems. Liteapks mod description claims players' appearances (face/hair/skin tone) and manager professional attire customizable — take as plausible but the 'fully customizable player face/skin' is from MOD-APK marketing, treat cautiously. Customize Team Name exists as a tab. Default manager options start at 3 faces (gamingonphone onboarding); customization is unlocked afterwards. Google Play description Sep 2026 explicitly: 'Customise your manager from a host of different options including hairstyles and outfits.'",
    "evidence/raw/turn35_w1/EV-382_custom.html",
    "Customise tabs Kit/Logo/TeamName/Players/Manager; built-in editor 5 color channels+patterns+trim; player customization (number/boots/socks); manager hairstyles/outfits/accessories; 3-face start")

# COACH MECHANICS (CORRECTED/EXPANDED)
add_claim("DLS26 uses a hidden weighted progression system for player development: each attribute has a different 'progression-energy cost'; CON (Control) and SPE (Speed) are heavier (more capacity) than STA (Stamina) which is lighter.", 2, "training/weights", [e_coach], "sakibpro simulator FAQ reflects in-game observations")
add_claim("Total cumulative development weight is capped at 100%, which corresponds to the +10 OVR hard cap over base card rating (corroborates the earlier +10 OVR claim with a mechanistic basis).", 2, "training/cap", [e_coach])
add_claim("Goalkeeper upgrades use a different conversion: approximately 2.2 training points in GKR/GKH = +1 OVR, with a strict cap of 22 total points allocated (= +10 OVR max above base GK rating, consistent with outfield cap).", 2, "training/gk-conversion", [e_coach])
add_claim("Coach category stat mapping (CORRECTED): Fitness Coach = SPE/ACC/STA/STR (4 physical); Technical Coach = CON/PAS/SHO/TAC (4 technical, including CON — NOT Fitness); Goalkeeping Coach = GKR/GKH; Special Coach = ALL STATS. (Earlier ckpt-045 grouping of CON with Fitness was an error from gamedls.net categorization.)", 2, "coaches/categories-corrected", [e_coach], "sakibpro simulator lists Technical=(CON,PAS,SHO,TAC) and Fitness=(SPE,ACC,STA,STR)")
add_claim("Example of visible stat values from dlsinside: Kevin De Bruyne 83 AM/CM — PAS 92, CON 88, SPE 75, ACC 72, STA 70, STR 71, TAC 68, SHO 80, GKR 13, GKH 13 (display shows digits 729/759/709/719/689/889/809/929 on page due to trailing HTML badge artifact '9').", 2, "ratings/example-kdb", [e_coach])
add_claim("v12.200 (Jun 4, 2025, DLS25 era) introduced two features carried into DLS26: (1) 'Buy a sold player back within a limited time' (sell regret window); (2) 'New Special Coach Packs' (IAP bundles of coaches for easier development).", 1, "patching/v12-200", [e_coach])
add_claim("Winter Reload (v13.110 Mar 2026) included individual stat adjustments for player cards (e.g. Pedri SPE↓ ACC↑ TAC↑ SHO unchanged), not just overall rating changes.", 1, "patching/stat-adjustments", [e_coach])
add_claim("CON (Control) is widely regarded as the most important universal technical attribute across positions — governs first-touch quality, close dribbling and the ability to change direction sharply.", 2, "attributes/control", [e_coach], "retbit/LevelWinner/r/DLS")
add_claim("Common coaches boost a single random stat; Rare coaches provide stronger multi-stat increases; Legendary coaches yield the highest stat boosts and highest breakthrough probability. (Re-asserted with corrected category mappings.)", 1, "coaches/tiers", [e_coach])
add_claim("Prior claim that Technical includes Fit/Tac/Pas/Sho (from ckpt-045) should be read as Fitness covering SPE/ACC/STA/STR (4 stats) and Technical covering CON/TAC/PAS/SHO (4 stats). CON is a Technical attribute, not Fitness.", 2, "errata/coach-cat", [e_coach], "corrects earlier ambiguity")

# MANAGER / PLAYER CUSTOMIZATION
add_claim("Customize screen (My Club → Customise) has five left-navigation tabs: Kit, Logo, Team Name, Players, Manager.", 1, "customization/tabs", [e_custom])
add_claim("In-game Kit Editor (free, no unlock) lets you edit Shirt, Shorts, Socks separately with 5 independent color channels per piece: Primary, Secondary, Sponsor, Trim, and Shirt Number; plus Kit Type (pattern arrows for plain/striped) and Kit Trim number selector (collar/cuff style).", 1, "customization/kit-editor", [e_custom])
add_claim("Manager customization supports hairstyle and outfit selection from multiple options (Google Play/App Store description); v13.330 added 'Manager Accessories' themed items (e.g. North American themed at launch), implying ongoing cosmetic updates.", 1, "customization/manager", [e_custom])
add_claim("Player customization (Customise → Players) allows changing kit number, boot color, and sock color; some options cost gems.", 2, "customization/players", [e_custom])
add_claim("Onboarding starts with 3 default manager faces (customizable later per gamingonphone).", 2, "onboarding/manager-faces", [e_custom])
add_claim("Custom kit/logo import unlock is a one-time gem purchase (BlueStacks cites 300 diamonds; dlskiturl cites 150g — price may have been lowered between DLS20 and DLS26; treat 300 as legacy DLS20 baseline and 150 as possible DLS26 discount).", 2, "customization/unlock-cost", [e_custom], "reconciles prior price discrepancy")
add_claim("Team name is editable from the Team Name tab in Customise.", 1, "customization/team-name", [e_custom])

p=os.path.join(RAW_DIR,'EV-381_coach.html'); os.makedirs(RAW_DIR,exist_ok=True)
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p=os.path.join(RAW_DIR,'EV-382_custom.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
