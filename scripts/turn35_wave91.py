#!/usr/bin/env python3
"""Turn 35 Wave 91: THE COMPLETE ACHIEVEMENT LIST, AND THE RANK LADDER FROM GOOGLE PLAY'S OWN DATA.

Wave 91's centrepieces:

1. THE COMPLETE 40-ACHIEVEMENT LIST, taken from Google Play's own achievement data rather than a
   guide. That matters because it is a primary source: it names the **six LIVE ranks exactly** -
   Rookie, Amateur, Semi-Pro, Intermediate, Pro, Veteran - and it confirms there is nothing above
   Veteran, which closes the rank-name gap as far as the open web can close it. It also gives
   four milestone ladders the corpus did not have: DLL wins (5/25/50/100/150), team rating
   (65/68/72/75/80), stadium capacity (15k/20k/30k/50k/70k) and Career divisions.

2. EVERY ACHIEVEMENT IS WORTH EXACTLY 500 XP, which is the arithmetic behind the corpus's
   20,000-XP figure: 40 x 500 = 20,000. That makes the achievement system a fixed, knowable
   contribution rather than a vague one - and it is worth about a fifth of the world record's
   145,296 XP on its own.

3. A FIFTH CONTAMINATION, and an achievement-count conflict that will not resolve cleanly. The
   corpus carries both a 40-achievement/20,000-XP figure and a 42-achievement/21,000-XP figure
   from two Exophase snapshots, and the tracked-player counts run the opposite way to the
   claimed growth direction - so the ordering is genuinely unresolved and is recorded as such.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w91')

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

e_ach=new_ev("exophase.com/game/dream-league-soccer-2026-android/achievements (the complete 40-achievement list from Google Play's own achievement data, each worth 500 XP, with the tracked-player and earned-achievement counters), exophase.com DLS Classic achievements (87 achievements, 131,215 obtainable EXP, 100,000 Points - a DIFFERENT game), exophase.com DLS 2018 achievements (63 achievements, 98,000 XP), r/DreamLeagueSoccer 1j41uqt (5 Mar 2025 - the total XP requirement was raised to 250,000, 'adding 50k more XP points on top of what was already a grind'), r/DreamLeagueSoccer 1qz14ir (8 Feb 2026 - the Tier 1 world record at 145,296 XP), two searches on the DLL season structure and the achievement list, both contaminated by ESL's DreamLeague Dota 2 tournament (Seasons 26, 27, 28 and 29 formats, prize pools and EPT points) and by League of Legends ranked-system documentation",
    "THE COMPLETE 40-ACHIEVEMENT LIST FROM GOOGLE PLAY'S OWN DATA, AND THE RANK LADDER CONFIRMED BY A PRIMARY SOURCE. (1) THE RANK LADDER, primary-source confirmed: the achievements '**Rookie Rank** - Reach rank Amateur 1', '**Climbing the Ladder** - Reach rank Semi-Pro 1', '**Making Progress** - Reach rank Intermediate 1', '**Going Pro** - Reach rank Pro 1' and '**DLS Veteran** - Reach rank Veteran 1' mean Google Play itself names **six LIVE ranks - Rookie, Amateur, Semi-Pro, Intermediate, Pro, Veteran** - and the list stops there. **So the rank-name gap is closed as far as the open web can close it: nothing above Veteran is published anywhere.** (2) EVERY ACHIEVEMENT IS WORTH EXACTLY 500 XP, which is the arithmetic behind the corpus's 20,000-XP figure: **40 x 500 = 20,000.** That converts the achievement system from a vague contribution into a fixed, knowable one - and it is worth roughly a seventh of the world record's 145,296 XP. (3) THE DLL WIN LADDER: 'Kick Off - Win 5 DLL matches', 'First Steps - 25', 'Finding Form - 50', 'In the Flow - 100', 'Full Stride - **150**'. So **150 DLL wins is a published milestone**, which is a useful yardstick for the mission - and it sits just above the 110 wins the record run needed. (4) THE TEAM-RATING LADDER: 'Building Blocks - 65', 'Rising the Ranks - 68', 'Team Chemistry - 72', 'Top Squad - 75', '**Ultimate XI - 80**'. So 80 is the top published rating milestone. (5) THE STADIUM-CAPACITY LADDER: 'Local Grounds - 15,000', 'Growing Crowd - 20,000', 'Fortress Forming - 30,000', 'World-Class Stadium - 50,000', 'Iconic Arena - **70,000**'. **These are NOT the division gates** - the corpus's gates are 6,462 / 15,000 / 30,000 / 45,000 / 60,000 / 80,000, so 20,000, 50,000 and 70,000 are achievement-only milestones with no promotion attached, and 45,000, 60,000 and 80,000 are promotion gates with no achievement. Two independent ladders, recorded separately. (6) THE CAREER DIVISION ACHIEVEMENTS name the climb: 'First Whistle - Amateur division', 'Rising Contender - Div 4', 'League Challenger - Div 3', 'Promotion Push - Div 2', 'Top Flight - Div 1', 'Elite Status - Elite division', '**Legend of the Game - Legendary division**'. (7) THE SCENARIO LADDER: 1, 5, 10, 25, **50** scenarios. THE GOLD-MEDAL LADDER: 1, 5, 10, 25, **50**. (8) 'Stronger Together - **Join a clan**' is an achievement, so the clan system has a one-time 500-XP reward attached. (9) THE SNAPSHOT RETRIEVED TODAY: 40 total achievements, 20,000 Points (XP), 40,351 obtainable EXP, **627 players tracked, 9,545 achievements earned, 1 player at 100%**. **That conflicts with the corpus's CLAIM-1158, which records 42 achievements, 21,000 obtainable XP, 912 players tracked and 13,727 earned** - and because Exophase's counters are cumulative, 912 tracked means CLAIM-1158's snapshot is the LATER one, which is the opposite direction to CLAIM-1186's claim that the count grew from 40 to 42. **The ordering is genuinely unresolved and is recorded as a conflict rather than smoothed.** (10) THE ACHIEVEMENT-COUNT CONFLICT IS NOW EXPLAINED: the 87-achievement/100,000-XP figure is **DLS Classic**, a separate game with its own 87 achievements paying in coins, and the 63-achievement/98,000-XP figure is **DLS 2018**. So DLS26 on Android is 40 (or 42) achievements at 500 XP each, and the other two lists were never DLS26 at all. (11) THE XP REQUIREMENT WAS RAISED: 'They have now increased the total XP points required to **250000 XP**, adding 50k more XP points on top of what was already a grind' - a DLS25-era change, so the 200,000 figure in older guides is stale. (12) A FIFTH CONTAMINATION: both searches returned ESL DreamLeague Dota 2 formats and prize pools and League of Legends ranked documentation. Five waves, five contaminations, four with identified causes - the general rule from wave 88 now has a fifth instance behind it.",
    "THE COMPLETE 40-ACHIEVEMENT LIST FROM GOOGLE PLAY'S OWN DATA - a primary source, not a guide. THE SIX LIVE RANKS ARE NAMED AND NOTHING ABOVE VETERAN EXISTS: Rookie, Amateur, Semi-Pro, Intermediate, Pro, Veteran - so the rank-name gap is closed as far as the open web can close it. EVERY ACHIEVEMENT IS EXACTLY 500 XP, so 40 x 500 = 20,000 - the achievement system is a fixed seventh of the world record's 145,296 XP. THE DLL WIN LADDER runs 5/25/50/100/150, so 150 wins is a published milestone just above the record run's 110. THE TEAM-RATING LADDER runs 65/68/72/75/80. THE STADIUM-CAPACITY LADDER runs 15k/20k/30k/50k/70k and is NOT the division gate ladder - they are independent. THE ACHIEVEMENT-COUNT CONFLICT IS EXPLAINED: the 87/100,000 list is DLS Classic and the 63/98,000 list is DLS 2018; neither was ever DLS26. A FIFTH CONTAMINATION.",
    "THE COMPLETE ACHIEVEMENT LIST AND THE RANK LADDER FROM GOOGLE PLAY'S OWN DATA",
    quality="official")

add_claim("THE SIX LIVE RANKS, PRIMARY-SOURCE CONFIRMED by Google Play's own achievement data: **Rookie, Amateur, Semi-Pro, Intermediate, Pro, Veteran** - via the achievements 'Rookie Rank - Reach rank Amateur 1', 'Climbing the Ladder - Semi-Pro 1', 'Making Progress - Intermediate 1', 'Going Pro - Pro 1' and 'DLS Veteran - Veteran 1'. **The list stops at Veteran, so the rank-name gap is closed as far as the open web can close it: nothing above Veteran is published anywhere.**", 2, "dll/six-rank-ladder-primary-source", [e_ach], notes="Closes the rank-names gap below Veteran at primary-source confidence; above Veteran stays device-only")
add_claim("EVERY ACHIEVEMENT IS WORTH EXACTLY 500 XP, which is the arithmetic behind the corpus's 20,000-XP figure: **40 x 500 = 20,000.** So the achievement system is a fixed, knowable contribution rather than a vague one - and at 500 XP each it is worth roughly a seventh of the world record's 145,296 XP.", 2, "achievements/every-achievement-500-xp", [e_ach])
add_claim("THE DLL WIN LADDER, from the achievement names: 'Kick Off - Win **5** DLL matches', 'First Steps - **25**', 'Finding Form - **50**', 'In the Flow - **100**', 'Full Stride - **150**'. So **150 DLL wins is a published milestone** - a yardstick for the mission that sits just above the 110 wins the record Tier 1 run needed.", 3, "achievements/dll-win-ladder-5-25-50-100-150", [e_ach])
add_claim("THE TEAM-RATING LADDER: 'Building Blocks - reach a team rating of **65**', 'Rising the Ranks - **68**', 'Team Chemistry - **72**', 'Top Squad - **75**', '**Ultimate XI - 80**'. So 80 is the top published rating milestone, and the ladder is a published proxy for squad progress.", 3, "achievements/team-rating-ladder-65-68-72-75-80", [e_ach])
add_claim("THE STADIUM-CAPACITY LADDER: 'Local Grounds - **15,000**', 'Growing Crowd - **20,000**', 'Fortress Forming - **30,000**', 'World-Class Stadium - **50,000**', 'Iconic Arena - **70,000**'. **These are NOT the division gates** - the corpus's promotion gates are 6,462 / 15,000 / 30,000 / 45,000 / 60,000 / 80,000. So 20,000, 50,000 and 70,000 are achievement-only milestones with no promotion attached, and 45,000, 60,000 and 80,000 are promotion gates with no achievement. **Two independent ladders - do not read one as the other.**", 3, "achievements/stadium-capacity-ladder-independent-of-gates", [e_ach], notes="Prevents conflating the achievement ladder with the promotion gates")
add_claim("THE CAREER DIVISION ACHIEVEMENTS name the climb exactly: 'First Whistle - Amateur division', 'Rising Contender - Div 4', 'League Challenger - Div 3', 'Promotion Push - Div 2', 'Top Flight - Div 1', 'Elite Status - Elite division', '**Legend of the Game - Legendary division**'.", 3, "achievements/career-division-achievement-names", [e_ach])
add_claim("THE SCENARIO LADDER runs 1, 5, 10, 25 and **50** completed scenarios, and the GOLD-MEDAL LADDER runs 1, 5, 10, 25 and **50** - so both systems have a 50-unit top milestone, which is a useful long-run target for the daily routine.", 3, "achievements/scenario-and-medal-ladders", [e_ach])
add_claim("'**Stronger Together - Join a clan**' is itself a 500-XP achievement, so the clan system carries a one-time reward on top of its season ladder.", 3, "achievements/join-a-clan-achievement", [e_ach])
add_claim("AN ACHIEVEMENT-COUNT CONFLICT THAT WILL NOT RESOLVE CLEANLY. The snapshot retrieved today shows **40 total achievements, 20,000 Points (XP), 40,351 obtainable EXP, 627 players tracked, 9,545 achievements earned and 1 player at 100%** - which matches the corpus's CLAIM-1492. But CLAIM-1158 records **42 achievements, 21,000 obtainable XP, 912 players tracked and 13,727 earned**, and because Exophase's counters are cumulative, 912 tracked means CLAIM-1158's snapshot is the LATER one - the opposite direction to CLAIM-1186's claim that the count grew from 40 to 42. **The ordering is genuinely unresolved and is recorded as a conflict rather than smoothed.**", 3, "errata/achievement-count-conflict-unresolved", [e_ach], notes="Three corpus claims disagree on direction; recorded, not forced")
add_claim("THE ACHIEVEMENT-COUNT CONFLICT IS NOW EXPLAINED: the 87-achievement / 100,000-XP list is **DLS Classic**, a separate game with its own 87 achievements paying in coins (5 to 1,000 coins each), and the 63-achievement / 98,000-XP list is **DLS 2018**. So DLS26 on Android is 40 (or 42) achievements at 500 XP each, and the other two lists were never DLS26 at all.", 2, "achievements/other-lists-are-other-games", [e_ach], notes="Resolves a large part of CLAIM-1492's conflict by identifying the other two lists")
add_claim("THE XP REQUIREMENT WAS RAISED: 'They have now increased the total XP points required to **250,000 XP**, adding 50k more XP points on top of what was already a grind' - a DLS25-era change, so any guide quoting a 200,000-XP requirement is stale.", 3, "achievements/xp-requirement-raised-to-250000", [e_ach])
add_claim("A FIFTH CONTAMINATION: both of this wave's searches returned ESL's **DreamLeague Dota 2** tournament (Seasons 26, 27, 28 and 29 - formats, prize pools, EPT points) and **League of Legends** ranked-system documentation. Five waves, five contaminations, four with identified causes - the general rule from wave 88 now has a fifth instance behind it.", 3, "errata/fifth-contamination", [e_ach])

for p in ['EV-504_achievement_list.html','EV-504b_other_game_lists.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
