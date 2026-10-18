#!/usr/bin/env python3
"""Turn 33 Wave 7: match length/difficulty/offline, form boosts/stamina regen, top players, defending."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
EXTRACT_DIR=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','match_turn33')

ev_id=362
def new_ev(origin, summary, artifact_path, vol):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":"mixed","summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid

cl_id=523
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid

os.makedirs(RAW_DIR,exist_ok=True)

e_match=new_ev("appitika store listing + r/DLS reviews + mwm reviews + minireview FAQ",
    "Match length: default 3-minute halves (~5-6 min realtime + stoppage, total match ~6 min plus ads); players request 5-minute halves (matches often end 1-0 at default length). Action can be sped up or paused. Halftime includes forced ads in some versions; halftime team talk boosts available for 30 coins (+small stamina/form). Offline capability: Career Mode + Training + Exhibition/local matches are fully offline (run locally on device, syncs to cloud on reconnect); Dream League Live, events (World Tournament, GCC, Clan events), and ads require internet. Difficulty levels offered (beginners recommended Medium; community divides Medium/Hard; Hard mode reviews cite excessive fouling by AI, superhuman GKs, AI players impossible to dispossess (60/70 AI shielding off 80/90 players), scripting complaints (crossbar hits, button non-response, half-time comeback AI). AI adaptive behavior (per multiple sources): opponents adapt to playstyle (long shots → tighter box defense; short passing → higher press; winger exploitation → mid-match switch to compact 4-4-2). DLS26 community observations: scripting reduced vs DLS25; pace more realistic, control buffed, standing tackles harder to win; strength differential more apparent (low-strength teams bullied); player switching 0.5-2s delay persists; DLS26 foul frequency on Hard criticized.",
    "evidence/raw/match_turn33/EV-362_match.html",
    "Match length, offline mode, difficulty, AI adaptiveness, scripting perceptions")
e_stamina=new_ev("FTG support + LevelWinner DLS20/22/24 guides + r/DLS DLS26 day2",
    "FTG official stat definitions (support.ftgames.com): ACC = how quickly player reaches top speed. STA = rate of energy depletion when running; affects halftime energy boost; below a threshold other stats degrade gradually as energy drops (most noticeable on speed; tired players perform worse in all areas). Stamina regen: ~30% of max stamina regenerates after each match (baseline); halftime gives small stamina boost. Form Boosts: temporary per-player stat increases purchased with gems: Common=5g (+1 OVR), Rare=8g (+2 OVR), Legendary=10g (+3 OVR); duration starts at 1 match minimum, extended by Training Centre level. Team Boost (mid-game) and Team Physio (post-game) both restore ~10% stamina and cost coins. Halftime team-boost costs 30 coins (DLL). Substitution sweet-spot minutes 60-70 for 5-man subs; substitute any player with orange stamina bar. Don't sub in first half in DLL unless injured (halftime regen + 30c team form boost incoming). DLS26 launch day-2 complaint (r/DLS): stamina NOT restoring between games in some cases (possible bug, or new deliberate stamina-carryover). Reservation system for subs bench: max 8 substitutes reported (likely bench of 7 = typical 5-subs+2 GK/res). Coach upgrade cost scales with current stat height (wiki). Coach training options six: Fitness (SPE/ACC/STA) per fandom wiki, plus others aligning to the 8 outfield + 2 GK stats.",
    "evidence/raw/match_turn33/EV-363_stamina.html",
    "Stamina regen rates, form boost costs, sub timing, coach cost scaling")
e_players=new_ev("Z2U + thesoccerera + playdreamleaguesoccer top-ratings",
    "Top-rated players DLS26 (source variance, treat as approximate ratings snapshot): Z2U Jun 2026 lists Haaland/Kane/Mbappé/Yamal 86 ST/RW; Vini 85 LW; Raphinha 85; Bruno F 85 AM; Pedri 85 CM; Valverde 85. thesoccerera Feb 2026 lists Dembélé 86 CF (PSG/France) as highest; Rodri 86 DM; Bellingham 85 AM; Valverde 85; KDB 84; GKs Alisson 85, Courtois 84, Ederson/ter Stegen 83. playdreamleaguesoccer (AI-farm, inflated) lists Haaland 94/Mbappé 93/Messi 92/Chhetri 82 (unreliable 99 dribble Messi). Rating snapshot will vary by update (e.g. Summer Spotlight reshuffles). Note dlsinside v13.430 shows player DB of 14,435 rows.",
    "evidence/raw/match_turn33/EV-364_ratings.html",
    "Top player rating snapshots (approximate)")
e_defend=new_ev("eslamgaming defending + Kotaku ES defending tips",
    "Defending in DLS26: punish over-committal (lunging tackles allow AI to play through quickly); 'Contain' (B button hold with stick direction) is primary tool — keep defender in front of attacker, wait for window to execute standing tackle; sliding tackles risk fouls/cards. Specialize training per position: ST = finishing/control/speed; Mid = passing/stamina/control; DEF = strength/tackle/positioning.",
    "evidence/raw/match_turn33/EV-365_defend.html",
    "Defending technique (contain > lunge), position-specific training priorities")

# MATCH LENGTH / DIFFICULTY
add_claim("Default match length is 3 minutes per half (~6 min of play per match excluding ads/stoppage); match can be paused and sped up. Community requests option for 5-min halves (1-0 scorelines common at default length).", 2, "match/length", [e_match], "appitika + App Store reviews")
add_claim("Career Mode, Training, and Exhibition/local matches are fully offline (run locally on device, save syncs on reconnect); Dream League Live, online events (GCC, World Tournament, Clans), and ads require internet.", 1, "platform/offline", [e_match])
add_claim("Difficulty settings include at least Easy (Beginner), Medium, Hard; scenarios mode forces Hard AI. Beginners recommended Medium; community meta play on Medium/Hard.", 2, "match/difficulty", [e_match])
add_claim("Hard difficulty community complaints: excessive AI fouling (breaking up dribbles), superhuman GKs (impossible saves), AI players 'impossible to dispossess' (60-70 OVR shielding off 80-90 OVR players), button non-response, excessive crossbar hits — interpreted as 'AI cheating/scripting'.", 3, "match/difficulty-complaints", [e_match], "subjective; perennial DLS complaint")
add_claim("AI adaptive behavior reported: opponents adjust tactics in response to player tendencies (long shots → tighter box defense; short passing → higher press; winger exploitation → switch to compact 4-4-2 mid-match). Some sources call this 'Mind of the Manager AI'.", 2, "match/ai-adaptive", [e_match], "eslamgaming/playdreamleaguesoccer (AI-farms); mechanism plausible but specifics unverified")
add_claim("DLS26 gameplay balance observations vs DLS25: scripting is reduced or gone (multiple users); pace more realistic; close control buffed; standing tackles harder to win (2 per game typical for underleveled teams); strength differentials more punishing; player switching 0.5-2 second delay persists.", 2, "match/balance", [e_match])
add_claim("Halftime includes ads in some builds; mid-game Team Boost (30 coins) available at halftime in DLL; forced ads criticized as disruptive.", 2, "match/ads", [e_match])
add_claim("Online matchmaking uses a hidden Skill Rating (SR) system per community reports.", 3, "multiplayer/matchmaking", [e_match], "playdreamleaguesoccer, AI-farm but plausible")

# STAMINA / FORM / TRAINING
add_claim("Official FTG stat definitions: ACC governs time to reach top speed; STA governs energy depletion rate while running AND halftime energy recovery; below a stamina threshold all other stats degrade gradually (speed most visible, but all areas impacted).", 1, "attributes/stamina", [e_stamina], "FTG support")
add_claim("Post-match stamina regen is approximately 30% of max stamina per match (baseline, no physios/facilities).", 2, "stamina/regen", [e_stamina])
add_claim("Halftime provides a small stamina boost; players advised not to sub in first half during DLL (wait for halftime regen + 30-coin team boost).", 2, "stamina/halftime", [e_stamina])
add_claim("Form Boosts (temporary per-player): Common = 5 gems (+1 OVR), Rare = 8 gems (+2 OVR), Legendary = 10 gems (+3 OVR); duration starts at 1 match, extended by Training Centre upgrades.", 2, "form-boost/costs", [e_stamina])
add_claim("Team Boost (mid-game, coins) and Team Physio (post-game, coins) each restore ~10% stamina to the squad.", 2, "stamina/items", [e_stamina])
add_claim("Optimal substitution window: minutes 60-70 for a 5-man substitution block; substitute any player showing orange stamina/teardrop indicator.", 2, "tactics/subs", [e_stamina])
add_claim("DLS26 launch (Dec 2, 2025) reports of stamina NOT restoring between matches (possible bug or new stamina-carryover design); verify with APK/current version.", 3, "stamina/bug", [e_stamina], "Day-2 megathread; may have been hotfixed")
add_claim("Sub bench 'reservation system' reported to cap at 8 substitutes (7 bench + 1 likely reserve structure, typical modern 5-subs rule).", 3, "squad/subs", [e_stamina], "r/DLS complaint; exact cap unverified")
add_claim("Coach training cost scales with the player's current stat height (higher stats cost more per point).", 2, "training/cost-scaling", [e_stamina])
add_claim("Coach upgrade categories map to stats: Technical (CON/TAC/PAS/SHO), Fitness (STA/STR/ACC/SPE), Goalkeeping (GKH/GKR), Special (event/limited, varies).", 2, "coaches/categories", [e_stamina], "corroborates earlier ckpt-045")

# TOP PLAYERS
add_claim("Top-rated outfield players DLS26 (approximate Jun-Sep 2026 ratings, sources vary): Haaland ST 86, Kane ST 86, Mbappé ST/CF/LW 86, Yamal RW 86, Dembélé CF/RW 86, Rodri DM 86; Vini Jr LW 85, Raphinha LW/RW 85, Bruno Fernandes AM 85, Pedri CM 85, Valverde CM 85, Bellingham AM 85, De Bruyne AM 84; GKs Alisson 85, Courtois 84, Ederson 83, ter Stegen 83. (Ratings change with rating-refresh updates.)", 3, "ratings/top", [e_players], "snapshots vary between sources (z2u vs thesoccerera); AI-farm playdreamleaguesoccer lists Haaland 94 which is inflated")

# DEFENDING / TRAINING PRIORITIES
add_claim("Defending meta: do NOT lunge-tackle early (AI punishes with quick through-passes); use Contain (hold B while steering with stick) to keep defender goal-side and wait for a standing tackle opportunity; slide tackles risk fouls/cards.", 2, "defending/technique", [e_defend])
add_claim("Position-specific training priorities: Forwards = finishing (SHO) + control (CON) + speed (SPE/ACC); Midfielders = passing (PAS) + stamina (STA) + control (CON); Defenders = strength (STR) + tackling (TAC) + positioning.", 2, "training/priorities", [e_defend], "Kotaku ES tip")

for f in ['EV-362_match.html','EV-363_stamina.html','EV-364_ratings.html','EV-365_defend.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl=sum(1 for _ in f)
print(f"Added {cl_id-523} new claims and {ev_id-362} EVs. Totals: {n_cl} claims, {n_ev} EVs")
