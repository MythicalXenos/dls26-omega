#!/usr/bin/env python3
"""Turn 35 Wave 32: Dream Team Value + legacy signing/spend achievements + Fan Approval; goalkeeping (GKH/GKR semantics, GKR>=GKH rule, height, manual keeper control, shootout tactics, no positional penalty)."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w32')

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

# ---------- EV-424: dream team value + legacy signing/spend achievements ----------
e_dtv=new_ev("Nerdburglars DLS achievement list, thekittygamer DLS2017/18 coin guide, Exophase DLS2018 (Android + iOS) and DLS Classic achievement lists",
    "DREAM TEAM VALUE + LEGACY SIGNING/SPENDING ACHIEVEMENTS. Dream Team Value is a percentage-based squad-quality measure with achievement milestones at 50% ('Getting Stronger') and 80% ('Ultimate Dream Team'), which in legacy builds paid 25 and 100 coins (DLS Classic) or 1,000 and 2,000 XP (DLS2018). The 80% tier is one of the rarest achievements in the game - only 0.00% of tracked players on the iOS list and 5.05% on DLS Classic - and reaching 100% is associated with roughly 23 fully developed players. LEGACY SIGNING ACHIEVEMENTS: 'Sign On The Dotted Line' (5 players signed), 'Catalogue Of Players' (10), 'Transfers!' (20) and 'Revolving Door' (100). LEGACY SPENDING ACHIEVEMENTS: spend a total of 1,250 / 2,500 / 5,000 / 10,000 coins on players. A 'Fan Approval Rating' also exists, with a 'Fan Favourite' achievement for reaching 100% Fan Approval (2,000 XP) - the mechanics of Fan Approval are undocumented in any source found. Rarity benchmarks from the legacy lists: 'Revolving Door' 3.14% (Android) / 0.00% (iOS), 'Getting Stronger' 20.38% (Android) / 6.67% (iOS), 'Ultimate Dream Team' 13.08% (Android) / 0.00% (iOS), 'Invincible!' (finish a league season undefeated) 41.28%.",
    "evidence/raw/turn35_w32/EV-424_dream_team_value.html",
    "Dream Team Value = percentage squad-quality metric with 50% and 80% achievement tiers (legacy payouts 25/100 coins or 1000/2000 XP); 80% is among the rarest achievements; 100% ~= 23 developed players; legacy signing achievements 5/10/20/100 players; legacy spend achievements 1250/2500/5000/10000 coins; a Fan Approval Rating exists with a 100% 'Fan Favourite' achievement (mechanics undocumented); legacy rarity benchmarks recorded",
    quality="community")

add_claim("Dream Team Value is a percentage-based squad-quality measure with achievement milestones at 50% ('Getting Stronger') and 80% ('Ultimate Dream Team'); legacy builds paid 25 and 100 coins for these, or 1,000 and 2,000 XP.", 2, "squad/dream-team-value", [e_dtv])
add_claim("Reaching 100% Dream Team Value is associated with roughly 23 fully developed players in the squad.", 2, "squad/dream-team-value-100", [e_dtv])
add_claim("The 80% Dream Team Value achievement is among the rarest in the game - 0.00% of tracked players on the legacy iOS list and 5.05% on DLS Classic.", 3, "squad/dtv-80-rarity", [e_dtv])
add_claim("Legacy signing achievements: 'Sign On The Dotted Line' (5 players signed), 'Catalogue Of Players' (10), 'Transfers!' (20) and 'Revolving Door' (100) - the last at 3.14% Android / 0.00% iOS rarity.", 3, "career/legacy-signing-achievements", [e_dtv])
add_claim("Legacy spending achievements require cumulative player spend of 1,250 / 2,500 / 5,000 / 10,000 coins.", 3, "career/legacy-spend-achievements", [e_dtv])
add_claim("A Fan Approval Rating exists with a 'Fan Favourite' achievement for reaching 100%; its mechanics are undocumented in every source found - OPEN GAP.", 4, "squad/fan-approval", [e_dtv], notes="OPEN GAP - existence confirmed via achievement, mechanics unknown")

# ---------- EV-425: goalkeeping ----------
e_gk=new_ev("r/DreamLeagueSoccer (1bxd927 DLS24 position guide, 199x7me, hmya2v, 1co8wi2, 19bxl2g), LevelWinner DLS20/DLS22/DLS24 guides, dream-league-soccer.fandom Player Development, gamingonphone DLS26 beginner guide, YouTube DLS26 manual keeper tutorial, retbit",
    "GOALKEEPING. GKH (Goalkeeper Handling) covers catching with the hands, throw accuracy, POSITIONING, clearing crosses and corners from the air, and knocking the ball away. GKR (Goalkeeper Reflexes) covers preempting and reacting to shots and diving to save, and in newer versions slightly governs the keeper's tendency to rush out of the box to sweep - higher GKR means better one-on-one performance. CONSENSUS RULE: GKR should be greater than or equal to GKH; if GKH exceeds GKR it should be by no more than 3 points, with 6 points cited as the outer limit, and the best builds push both above 95. HEIGHT matters - a 190cm+ keeper is preferred and Courtois is valued partly for his height, while low-height defenders such as Ruben Dias are less preferred. Best keepers named: Alisson and Courtois, with Donnarumma a good option that rushes out quickly. MANUAL KEEPER CONTROL: holding the C button while out of possession makes the goalkeeper run toward the ball - this is the only way to control the keeper directly - and double-tapping the keeper drops the ball from his hands; the keeper also charges out automatically in one-on-ones. SHOOTOUT TACTIC: a full-powered B-kick aimed dead-centre while appearing to take time aiming sideways makes the AI keeper dive sideways, leaving the centre shot uncontested. DEFENSIVE CARD DISCIPLINE: the B button is the reliable way to dispossess and avoid conceding penalties and free kicks, whereas frequent A-button slide tackles raise yellow/red card risk. NO POSITIONAL PENALTY: assigning a natural defender as an attacker causes no form or performance penalty, unlike management-heavy games. COMMUNITY COMPLAINTS: keepers concede identical goal types from outside the box while saving point-blank headers, positioning sometimes leaves the net empty, and 'all goalkeepers like to play dodge ball' - the standing advice is never to depend on the keeper and to keep only one. VERSION DRIFT: the legacy player-development model listed a THIRD goalkeeper attribute, GK Positioning, alongside Handling and Reflexes; the current model has only GKH and GKR.",
    "evidence/raw/turn35_w32/EV-425_goalkeeping.html",
    "GKH = catching, throw accuracy, POSITIONING, clearing crosses/corners, knocking away; GKR = preempting/reacting/diving to save plus tendency to rush out and sweep, higher GKR = better 1v1; consensus GKR >= GKH (GKH may exceed GKR by at most 3, outer limit 6, best builds both 95+); 190cm+ height preferred (Courtois); best keepers Alisson/Courtois/Donnarumma; manual keeper = hold C out of possession, double-tap to drop the ball, auto-charge in 1v1; shootout tactic = full-power B dead-centre while appearing to aim sideways; B-button dispossess beats A-slide for avoiding cards; NO positional penalty for out-of-position players; legacy third GK attribute 'GK Positioning' removed; community complaints on keeper inconsistency",
    quality="community")

add_claim("GKH (Goalkeeper Handling) covers catching with the hands, throw accuracy, POSITIONING, clearing crosses and corners from the air, and knocking the ball away.", 2, "goalkeeping/gkh-semantics", [e_gk])
add_claim("GKR (Goalkeeper Reflexes) covers preempting and reacting to shots and diving to save, and in newer versions slightly governs the keeper's tendency to rush out of the box to sweep - higher GKR means better one-on-one performance.", 2, "goalkeeping/gkr-semantics", [e_gk])
add_claim("Consensus keeper build rule: GKR should be greater than or equal to GKH; if GKH exceeds GKR it should be by no more than 3 points with 6 as the outer limit, and the best builds push both attributes above 95.", 3, "goalkeeping/gkr-gkh-ratio", [e_gk])
add_claim("Keeper height matters: 190cm+ is preferred and Courtois is valued partly for his height, while low-height defenders such as Ruben Dias are less preferred.", 3, "goalkeeping/height", [e_gk])
add_claim("Best keepers named by the community: Alisson and Courtois, with Donnarumma a good option that rushes out of goal quickly.", 3, "goalkeeping/best-keepers", [e_gk])
add_claim("Manual keeper control: holding the C button while out of possession makes the goalkeeper run toward the ball - the only direct keeper control in the game - and double-tapping the keeper drops the ball from his hands; the keeper also charges out automatically in one-on-ones.", 2, "goalkeeping/manual-control", [e_gk])
add_claim("Penalty shootout tactic: a full-powered B-kick aimed dead-centre while appearing to take time aiming sideways makes the AI keeper dive sideways, leaving the central shot uncontested.", 3, "goalkeeping/shootout-tactic", [e_gk])
add_claim("Defensive card discipline: the B button is the reliable way to dispossess opponents and avoid conceding penalties and free kicks, whereas frequent A-button slide tackles raise yellow and red card risk.", 2, "goalkeeping/b-vs-a-cards", [e_gk])
add_claim("There is NO positional penalty: assigning a natural defender as an attacker causes no form or performance penalty, unlike management-heavy football games.", 2, "attributes/no-positional-penalty", [e_gk])
add_claim("Community keeper complaints: keepers concede identical goal types from outside the box while saving point-blank headers, positioning sometimes leaves the net empty, and the standing advice is never to depend on the keeper and to carry only one.", 3, "goalkeeping/community-complaints", [e_gk])
add_claim("VERSION DRIFT: the legacy player-development model listed a THIRD goalkeeper attribute, GK Positioning, alongside Handling and Reflexes; the current model has only GKH and GKR.", 3, "goalkeeping/legacy-third-attribute", [e_gk])

p=os.path.join(RAW_DIR,'EV-424_dream_team_value.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-425_goalkeeping.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
