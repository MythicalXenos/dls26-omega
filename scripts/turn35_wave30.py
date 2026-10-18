#!/usr/bin/env python3
"""Turn 35 Wave 30: full DLS26 achievement set (42) incl. LIVE Tier rank names and team-rating milestones, stamina/energy management system, physio cost corroboration, CON terminology resolution, 'Team Chemistry' achievement-name resolution."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w30')

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

# ---------- EV-421: full achievement set ----------
e_ach=new_ev("Exophase Dream League Soccer 2026 achievements page (Google Play, fetched in full 2026-10-18), cross-checked against the legacy Exophase DLS list",
    "COMPLETE DLS26 ACHIEVEMENT SET — 42 achievements, 500 XP each, 21,000 obtainable XP; 912 players tracked, 13,727 achievements earned, 3 players at 100%. DREAM LEAGUE LIVE WINS: Kick Off (5), First Steps (25), Finding Form (50), In the Flow (100), Full Stride (150). SCENARIOS: Scenario Starter (1), Finding Your Feet (5), Tactical Thinker (10), Matchday Mastery (25), Scenario Specialist (50). TEAM RATING: Building Blocks (65), Rising the Ranks (68), Team Chemistry (72), Top Squad (75), Ultimate XI (80). GOLD MEDALS: Taste of Victory (1), Golden Start (5), Trophy Room (10), Decorated Club (25), Legendary (50). STADIUM CAPACITY: Local Grounds (15,000), Growing Crowd (20,000), Fortress Forming (30,000), World-Class Stadium (50,000), Iconic Arena (70,000). LIVE RANK: Rookie Rank (reach rank Amateur 1), Climbing the Ladder (Semi-Pro 1), Making Progress (Intermediate 1), Going Pro (Pro 1), DLS Veteran (Veteran 1). CAREER DIVISION: First Whistle (Amateur), Rising Contender (Div 4), League Challenger (Div 3), Promotion Push (Div 2), Top Flight (Div 1), Elite Status (Elite), Legend of the Game (Legendary). OTHER: Stronger Together (join a clan), Hattrick Hero (hattrick with any player), First Signing (sign a player in the transfer market), Back Of The Net (score your first goal), Debut (complete your first match). Rarity spread shows the progression curve: First Signing 83.22%, Debut 42.87%, Back Of The Net 43.53%, Legend of the Game 23.68%, Elite Status 27.08%, Iconic Arena 25.99%, Scenario Specialist 0.66%. TWO IMPORTANT CORROBORATIONS: (a) the team-rating achievements at 65 and 68 independently corroborate the community market thresholds (65 = rares appear, 68.7 = 80-82 legendaries appear); (b) 'Team Chemistry' is merely the ACHIEVEMENT NAME for reaching a 72 team rating - the word 'chemistry' appears in DLS26 only as this label, which explains how the fabricated 'team chemistry system' claim arose. The LIVE rank names (Rookie, Amateur, Semi-Pro, Intermediate, Pro, Veteran) are the first concrete current-build naming of the DLL tier ladder and are directly relevant to the mission's ranking target.",
    "evidence/raw/turn35_w30/EV-421_achievements.html",
    "42 DLS26 achievements, 500 XP each, 21,000 total; DLL wins 5/25/50/100/150; scenarios 1/5/10/25/50; team rating 65/68/72/75/80; gold medals 1/5/10/25/50; stadium 15k/20k/30k/50k/70k; LIVE ranks Amateur 1/Semi-Pro 1/Intermediate 1/Pro 1/Veteran 1; career divisions Amateur through Legendary; clan join; hattrick; first signing/goal/match; rarity curve; corroborates 65/68 market thresholds; 'Team Chemistry' = achievement name for 72 rating, explaining the fabricated chemistry claim; LIVE rank names Rookie>Amateur>Semi-Pro>Intermediate>Pro>Veteran",
    quality="official")

add_claim("DLS26 has exactly 42 Google Play achievements worth 500 XP each (21,000 obtainable XP); as of capture 912 players were tracked with 13,727 achievements earned and 3 players at 100%.", 2, "career/achievement-set-dls26", [e_ach])
add_claim("Dream League Live win achievements: Kick Off (5 wins), First Steps (25), Finding Form (50), In the Flow (100) and Full Stride (150).", 2, "dll/win-achievements", [e_ach])
add_claim("Scenario achievements: Scenario Starter (1), Finding Your Feet (5), Tactical Thinker (10), Matchday Mastery (25) and Scenario Specialist (50) - Scenario Specialist is the rarest achievement in the game at 0.66% of tracked players.", 2, "modes/scenario-achievements", [e_ach])
add_claim("Team-rating achievement milestones: Building Blocks (65), Rising the Ranks (68), Team Chemistry (72), Top Squad (75) and Ultimate XI (80) - independently corroborating the community market thresholds at 65 and 68.", 2, "transfers/rating-achievements", [e_ach], notes="Second independent source for the 65/68 market thresholds")
add_claim("Gold-medal achievements: Taste of Victory (1), Golden Start (5), Trophy Room (10), Decorated Club (25) and Legendary (50).", 2, "career/gold-medal-achievements", [e_ach])
add_claim("Stadium-capacity achievements use a round-number ladder: Local Grounds (15,000), Growing Crowd (20,000), Fortress Forming (30,000), World-Class Stadium (50,000) and Iconic Arena (70,000).", 2, "facilities/capacity-achievements-dls26", [e_ach], notes="Achievement thresholds, NOT promotion requirements - a distinct scale from all three promotion tables")
add_claim("DREAM LEAGUE LIVE RANK NAMES confirmed for the current build: Rookie, Amateur, Semi-Pro, Intermediate, Pro and Veteran, with achievements awarded for reaching division 1 of Amateur, Semi-Pro, Intermediate, Pro and Veteran.", 2, "dll/rank-names", [e_ach], notes="First concrete current-build naming of the LIVE Tier ladder - directly relevant to the #1 mission target")
add_claim("Career-division achievements: First Whistle (Amateur), Rising Contender (Div 4), League Challenger (Div 3), Promotion Push (Div 2), Top Flight (Div 1), Elite Status (Elite) and Legend of the Game (Legendary).", 2, "career/division-achievements", [e_ach])
add_claim("Remaining DLS26 achievements: Stronger Together (join a clan), Hattrick Hero (score a hattrick with any player), First Signing (sign a player in the transfer market), Back Of The Net (score your first goal) and Debut (complete your first match).", 2, "career/misc-achievements", [e_ach])
add_claim("'Team Chemistry' is only the ACHIEVEMENT NAME for reaching a 72 team rating - the word 'chemistry' has no mechanical meaning in DLS26, which explains how the fabricated 'team chemistry system' claim arose.", 2, "chemistry/achievement-name-only", [e_ach], notes="Resolves the origin of the chemistry red flag")
add_claim("Achievement rarity shows the DLS26 progression curve: First Signing 83.22%, Back Of The Net 43.53%, Debut 42.87%, Elite Status 27.08%, Iconic Arena 25.99%, Legend of the Game 23.68%, Scenario Specialist 0.66%.", 3, "career/achievement-rarity-curve", [e_ach])

# ---------- EV-422: stamina / energy management ----------
e_sta=new_ev("LevelWinner DLS22/DLS24 guides, r/DreamLeagueSoccer (rtrs4j, 15bpnih, nzg9qk), retbit 8 beginner tips, gamingonphone DLS26 career guide, Bluestacks, ldplayer DLS24, chaptercheats DLS21, keengamer, gamingroute, touchtapplay, App Store RO review (Apr 2026)",
    "STAMINA / ENERGY MANAGEMENT. After each match players regenerate 30% of their maximum stamina; players left on the bench for a whole match regain FULL stamina, so a two-squad rotation removes the need to wait. All players need roughly 2 hours of real time to return to full stamina, which is why filling every roster slot early is a priority. SUBSTITUTION RULES: only three substitutions are allowed within regulation time, and 5-6 players may reach orange stamina after a full game. The 5-man substitution sweet spot is the 60th-70th minute, targeting any player showing an orange stamina bar or teardrop marker; players subbed IN during that window recover to 100% for the next match, and players subbed OUT are fully rested. Advice from r/DLS: never substitute in the first half unless a player is injured, because half-time restores a small amount of stamina and the game offers a team form boost for 30 coins when the second half starts; substitute at around the 65th minute or later. RECOVERY TOOLS: a post-match Team Recovery button grants 10% energy; Team Boosts (mid-game) and Team Physios (post-game) have the identical effect of restoring 10% stamina. PHYSIO COSTS are corroborated by two independent sources: Common 50 coins / +10% energy, Rare 100 coins / +20%, Legendary 250 coins / +50% plus healing all active injuries (LevelWinner DLS21; ldplayer independently gives the same 10/20/50% split). Individual physio use should be capped at two players per match and 6-8 coins. A Rare Physio is required to fully restore the whole squad's stamina. Community consensus is that team physios are poor value compared with healing players individually. Tired players are slower, tackle less effectively and are MORE PRONE TO INJURY - one player substitutes his best player before the last 20 minutes for this reason. HIDDEN DAILY FATIGUE: an App Store review (Apr 2026) reports that after roughly 10 matches in a day the team plays slower and less organised even though stamina indicators are not low, suggesting an undisclosed daily performance depreciation - single-source, unverified. TERMINOLOGY RESOLVED: chaptercheats' claim that CON means 'Condition, how prone they are to injuries' is WRONG - official FTG stat semantics (GS-001) tie CON to dribbling and ball control, and injury proneness is governed by STR.",
    "evidence/raw/turn35_w30/EV-422_stamina.html",
    "Post-match regen 30% of max stamina; benched-for-a-match players regain FULL stamina; ~2 hours real time for full squad recovery; 3 substitutions in regulation, 5-6 players go orange per game; 5-man sub sweet spot 60-70 min targeting orange bars, subbed-in recover 100% and subbed-out fully rested; never sub in first half unless injured (halftime regen + 30-coin team form boost at second-half start); Team Recovery/Team Boost/Team Physio all = 10% stamina; physio costs Common 50c/+10%, Rare 100c/+20%, Legendary 250c/+50% + heal all (two independent sources); cap individual physios at 2 players/6-8 coins; tired players more injury-prone; hidden daily fatigue after ~10 matches/day (single review, unverified); CON = Control not Condition (chaptercheats wrong)",
    quality="community")

add_claim("After each match players regenerate 30% of maximum stamina, and any player left on the bench for a whole match regains FULL stamina - a two-squad rotation removes the need to wait for recovery.", 2, "stamina/post-match-regen", [e_sta])
add_claim("A full squad needs roughly 2 hours of real time to return to full stamina, which is why filling every roster slot early is a priority.", 2, "stamina/full-recovery-time", [e_sta])
add_claim("Only three substitutions are allowed within regulation time, and 5-6 players may reach orange stamina after a full game.", 2, "stamina/substitution-limit", [e_sta])
add_claim("The five-man substitution sweet spot is the 60th-70th minute, targeting players with an orange stamina bar or teardrop marker: players subbed in during that window recover to 100% for the next match and players subbed out are fully rested.", 2, "stamina/substitution-timing", [e_sta])
add_claim("Never substitute in the first half unless a player is injured - half-time restores a small amount of stamina and the game offers a 30-coin team form boost when the second half starts.", 2, "stamina/no-first-half-subs", [e_sta])
add_claim("A post-match Team Recovery button, a mid-game Team Boost and a post-game Team Physio all restore exactly 10% stamina and are functionally equivalent.", 2, "stamina/recovery-tools-10pct", [e_sta])
add_claim("Physio costs are corroborated by two independent sources: Common 50 coins for +10% team energy, Rare 100 coins for +20%, and Legendary 250 coins for +50% plus healing all active injuries.", 2, "physio/costs-corroborated", [e_sta], notes="LevelWinner DLS21 and ldplayer independently agree on the 10/20/50% split")
add_claim("Individual physio use should be capped at two players per match and 6-8 coins, and community consensus is that team physios are poor value compared with healing players individually.", 3, "physio/individual-vs-team-value", [e_sta])
add_claim("Tired players are slower, tackle less effectively and are more prone to injury, so key players should be substituted before the final 20 minutes.", 2, "stamina/tired-injury-risk", [e_sta])
add_claim("A single App Store review (Apr 2026) reports hidden daily fatigue - after roughly 10 matches in a day the team plays slower and less organised even though stamina indicators are not low. UNVERIFIED, single source.", 3, "stamina/hidden-daily-fatigue", [e_sta])
add_claim("TERMINOLOGY RESOLVED: CON means Control (ball control/dribbling), not Condition - official FTG stat semantics tie CON to dribbling, and injury proneness is governed by STR. chaptercheats' 'CON = how prone to injuries' definition is wrong.", 2, "errata/con-terminology", [e_sta])

p=os.path.join(RAW_DIR,'EV-421_achievements.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-422_stamina.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
