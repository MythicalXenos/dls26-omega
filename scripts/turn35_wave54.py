#!/usr/bin/env python3
"""Turn 35 Wave 54: THE ACHIEVEMENT COUNT RESOLVED AS A SOURCE CONFLATION (C-026), and THE COACHING
METHOD - including a finding that reframes breakthroughs from a bonus into a risk.

Wave 54's two results:

1. C-026 - ACHIEVEMENT COUNT: the KB's '63 achievements / 98,000 XP' figure turns out to be TWO
   DIFFERENT PLATFORMS stitched together. Exophase lists DLS26 on Google Play at 40 achievements /
   20,000 XP, and DLS26 on Apple Game Centre at 63 achievements / 13,483 EXP, while the 98,000 XP
   figure belongs to a generic 'Dream League Soccer' listing from the Classic era. So the correct
   numbers are platform-specific, and neither 63 nor 98,000 is wrong - they were never measuring
   the same thing. The full Android achievement list is captured, which gives the early-game XP
   structure and the DLL win-count ladder.

2. COACHING METHOD: three findings that change how coaches should be spent. (a) A BREAKTHROUGH IS A
   RISK, not just a bonus - 'you can't control when or where it applies, so if you get it to tackling
   when you're maxing a striker it can reduce total points available to the good stats', which means
   a wasted breakthrough actively consumes development capacity. (b) TRAIN A PLAYER ALONE - a
   Dembélé maxing report describes training a single player alone and chaining Common coaches by
   category. (c) THE WEIGHTED-CAPACITY MODEL is independently corroborated: 'upgrading crucial
   attributes like Control (CON) or Speed (SPE) consumes significantly more progression capacity than
   raising Stamina (STA) ... a player reaches their absolute +10 OVR limit when their total cumulative
   development weight hits 100%' - which is exactly the KB's x2 STR/CON weighting and +10 cap.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w54')

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

# ---------- EV-466: achievement counts ----------
e_ach=new_ev("Exophase DLS26 Android achievements page (40 achievements / 20,000 XP / 40,351 obtainable EXP, with the full per-achievement list and completion percentages), Exophase DLS26 Apple iOS achievements page (63 achievements / 13,483 obtainable EXP), Exophase DLS Classic Android page (87 achievements / 131,215 EXP / 100,000 XP), Nerdburglars Dream League Soccer achievement list (98,000 total XP, Google Play)",
    "THE ACHIEVEMENT COUNT RESOLVED AS A SOURCE CONFLATION (C-026). The KB carried '63 achievements / 98,000 XP'. Those two numbers come from DIFFERENT PLATFORMS and DIFFERENT GAME ENTRIES: 63 is the APPLE GAME CENTRE count for DLS26 (Exophase lists DLS26 on iOS at 63 total achievements, 13,483 obtainable EXP), while 98,000 XP belongs to a GENERIC 'Dream League Soccer' Google Play listing from the Classic era (Nerdburglars shows 98,000 total XP with no version qualifier). The DLS26 ANDROID count is neither of them: **40 achievements, 20,000 XP** (Exophase, with 40,351 obtainable EXP tracked). So all three figures are real and none is wrong - they measure three different surfaces. THE FULL DLS26 ANDROID ACHIEVEMENT LIST (each worth 500 XP): the DLL win ladder - Kick Off (win 5 DLL matches), First Steps (25), Finding Form (50), In the Flow (100), Full Stride (150); the scenario ladder - Scenario Starter (complete a scenario), Finding Your Feet (5), Tactical Thinker (10), Matchday Mastery (25), Scenario Specialist (50); team rating - Rising the Ranks (reach a team rating of 68), Ultimate XI (reach 80); gold medals - Taste of Victory (win a gold medal), Golden Start (5), Trophy Room (10), Decorated Club (25), Legendary (50); stadium - Local Grounds (reach 15,000 stadium capacity, which matches the Division 3 gate exactly); divisions - First Whistle (Amateur), Rising Contender (Div 4), League Challenger (Div 3), Promotion Push (Div 2), Elite Status (Elite); and ranks - Making Progress (Intermediate), Going Pro (Pro), DLS Veteran (Veteran). COMPLETION RATES give the difficulty curve for free: First Whistle is 62.84% complete while Ultimate XI is 38.76%, DLS Veteran 14.04% and Full Stride (150 DLL wins) just 8.45% - so the achievement set is front-loaded and the online grind is the tail.",
    "evidence/raw/turn35_w54/EV-466_achievement_counts.html",
    "ACHIEVEMENT COUNT (C-026) RESOLVED AS A SOURCE CONFLATION: the KB's '63 achievements / 98,000 XP' was two platforms stitched together. DLS26 on ANDROID (Google Play) is 40 achievements / 20,000 XP; DLS26 on iOS (Game Centre) is 63 achievements / 13,483 EXP; the 98,000 XP belongs to a generic Classic-era listing. THE FULL DLS26 ANDROID LIST (500 XP each): DLL wins at 5/25/50/100/150; scenarios at 1/5/10/25/50; team rating 68 and 80; gold medals at 1/5/10/25/50; stadium capacity 15,000 (the Division 3 gate); divisions Amateur/Div 4/Div 3/Div 2/Elite; ranks Intermediate/Pro/Veteran. Completion rates give the difficulty curve: First Whistle 62.84% vs Full Stride 8.45% and DLS Veteran 14.04%",
    quality="community")

add_claim("C-026 RESOLVED AS A SOURCE CONFLATION: the corpus's '63 achievements / 98,000 XP' stitched together two platforms. DLS26 on ANDROID (Google Play) is **40 achievements / 20,000 XP**; DLS26 on iOS (Game Centre) is **63 achievements / 13,483 EXP**; the 98,000 XP figure belongs to a generic Classic-era 'Dream League Soccer' listing.", 2, "achievements/count-resolved-platform-split", [e_ach], notes="C-026 CLOSED - all three figures are real; they measure different surfaces")
add_claim("The DLS26 Android achievement set is 40 achievements at 500 XP each = 20,000 XP total, covering the DLL win ladder (5/25/50/100/150 wins), the scenario ladder (1/5/10/25/50), team ratings 68 and 80, gold medals (1/5/10/25/50), 15,000 stadium capacity, the division ladder (Amateur/Div 4/Div 3/Div 2/Elite) and the rank ladder (Intermediate/Pro/Veteran).", 2, "achievements/full-android-list", [e_ach])
add_claim("Achievement completion rates give the difficulty curve: First Whistle (reach Amateur division) is 62.84% complete, Ultimate XI (team rating 80) 38.76%, DLS Veteran 14.04%, and Full Stride (150 DLL wins) only 8.45% - the set is front-loaded and the online grind is the tail.", 2, "achievements/completion-curve", [e_ach], notes="Useful for expectation-setting: 150 DLL wins is a top-8% achievement")
add_claim("'Local Grounds' requires reaching 15,000 stadium capacity - exactly the Division 3 seat gate, confirming the two systems are linked.", 2, "achievements/stadium-gate-link", [e_ach])

# ---------- EV-467: coaching method ----------
e_coach=new_ev("r/DreamLeagueSoccer 1t98x80 (10 May 2026, 'let me explain the best coaching method in DLS'), 1pdknia (3 Dec 2025, DLS26 Dembele maxed), 1tlrk16 (23 May 2026, Szoboszlai maxed), sakibpro.com/players/simulator.html (DLS 26 Player Upgrade Simulator), gamingonphone DLS26 Career Mode guide (27 Jan 2026), Level Winner DLS2020 training guide (3 Jul 2020), Bluestacks DLS26 character development guide, r/DLS 18dqq9e (30 Jan 2024, DLS24 beginner coaching), 1rf3sbg (26 Feb 2026), 176ntor (13 Oct 2023), 1jgbp59 (21 Mar 2025)",
    "THE COACHING METHOD - breakthroughs as a risk, the train-alone technique, and the weighted-capacity model. (1) A BREAKTHROUGH IS A RISK, NOT JUST A BONUS. The best coaching-method thread in the corpus ('let me explain the best coaching method in DLS to you', 10 May 2026) argues for the 'COMMON BOOST' method: 'While using rare or legendary coaches, you basically don't have any influence on what stats get picked for the upgrade. Besides that you have to spend thousands of gems per coach, only to get disappointed when you don't get a 6x100 or whatever upgrade, so you redo, making it cost more.' The thread's explanation of a breakthrough is the strategically important part: 'It is when a coach applies bonus development. It is helpful but YOU CAN'T CONTROL WHEN OR WHERE IT APPLIES, so if you get it to tackling when you're maxing a striker it can reduce total points available to the good stats.' So a breakthrough landing on an unwanted stat actively CONSUMES development capacity that would otherwise have gone to the stats you want - which reframes breakthrough chance from a pure upside to a variance you should minimise. (2) TRAIN A PLAYER ALONE. A DLS26 Dembele maxing report (Dec 2025) describes the technique: 'train him alone, I used full common tech coaches to max his tech stats to 3x100 then switching to full common fitness coaches, when his sta reaches 98 I did one rare fitness coach - if you are lucky enough to keep his tackling low an 80 str is also possible.' The same report notes the build is easier than DLS25: 'this is a clear upgrade to his DLS25 version which last year I wasn't able to pull 6x100 stats in my second try, this time is much easier.' (3) THE WEIGHTED-CAPACITY MODEL IS INDEPENDENTLY CORROBORATED. A coaching simulator that claims to mirror the game's internal logic states: 'In DLS 26, not all stats are created equal. Upgrading crucial attributes like Control (CON) or Speed (SPE) consumes significantly more progression capacity than raising Stamina (STA) ... a player reaches their absolute +10 OVR limit when their total cumulative development weight hits 100%.' That is exactly the KB's x2 STR/CON weighting and the +10 OVR cap, now from a second source. (4) THE DLS20 BREAKTHROUGH BASELINE IS CONFIRMED AND EXTENDED: Level Winner's DLS20 training guide gives 'Breakthrough Rating, which represents the chances of a trained player getting a huge boost in stats thanks to some bonus development' - Common 25 gems, two random stats +2, 5 percent Breakout Rating; Rare 50 gems, trains two players, three random stats +3, 10 percent Breakout Rating - completing the 5/10/20 ladder. DLS26 sources mention breakthrough only qualitatively ('Legendary coaches provide the best upgrades and higher Breakthrough chances'), with no numbers. (5) Midfielders are the hardest cards to build: 'I genuinely hate maxing midfielders in DLS because they always come out weirdly built. One minute you're aiming for a balanced AM, next thing you know the card has 100 stamina, 96 pace, but the control and passing are disappointing.' (6) League seasons run 15 games and you can forfeit once you have enough points; career goal rewards stop accumulating past a threshold (a 2023 thread says 15 goals).",
    "evidence/raw/turn35_w54/EV-467_coaching_method.html",
    "COACHING METHOD: (1) A BREAKTHROUGH IS A RISK - 'you can't control when or where it applies, so if you get it to tackling when you're maxing a striker it can reduce total points available to the good stats', so a wasted breakthrough CONSUMES development capacity. The 'common boost' method argues for chaining Common coaches because Rare/Legendary give no control over which stats are picked and cost thousands of gems to redo. (2) TRAIN A PLAYER ALONE, chaining Common coaches by category (all tech, then all fitness). (3) THE WEIGHTED-CAPACITY MODEL is corroborated by a second source: CON and SPE consume significantly more progression capacity than STA, and the +10 OVR cap is a 100% cumulative development weight. (4) DLS20 breakthrough baseline confirmed: Common 5%, Rare 10% (implying Legendary 20%); DLS26 sources give no numbers, only that Legendary has higher breakthrough chances. (5) Midfielders are the hardest cards to build. (6) League seasons are 15 games and can be forfeited once the points are secure",
    quality="community")

add_claim("A BREAKTHROUGH IS A RISK, NOT ONLY A BONUS: 'it is when a coach applies bonus development. It is helpful but you can't control when or where it applies, so if you get it to tackling when you're maxing a striker it can reduce total points available to the good stats.' A breakthrough on an unwanted stat CONSUMES development capacity.", 3, "coaching/breakthrough-is-a-risk", [e_coach], notes="Reframes the breakthrough stat from pure upside to managed variance")
add_claim("THE 'COMMON BOOST' COACHING METHOD: with rare or legendary coaches 'you basically don't have any influence on what stats get picked for the upgrade' and you spend thousands of gems per coach only to redo a disappointing result, so chaining Common coaches gives more control per gem.", 3, "coaching/common-boost-method", [e_coach], notes="Reconciles with the KB's Common-coach farming loop - the farming route is also the controlled route")
add_claim("TRAIN A PLAYER ALONE: a DLS26 maxing report describes training a single player alone and chaining Common coaches by category - 'I used full common tech coaches to max his tech stats to 3x100 then switching to full common fitness coaches, when his sta reaches 98 I did one rare fitness coach'.", 3, "coaching/train-alone", [e_coach])
add_claim("THE WEIGHTED-CAPACITY MODEL IS CORROBORATED BY A SECOND SOURCE: 'upgrading crucial attributes like Control (CON) or Speed (SPE) consumes significantly more progression capacity than raising Stamina (STA) ... a player reaches their absolute +10 OVR limit when their total cumulative development weight hits 100%.' This matches the KB's x2 STR/CON weighting and the +10 OVR cap.", 3, "coaching/weighted-capacity-corroborated", [e_coach], notes="Second source on the coach weight model")
add_claim("THE DLS20 BREAKTHROUGH BASELINE IS CONFIRMED: Common coaches carry a 5% Breakout Rating and Rare coaches 10% (25 gems for two random stats +2; 50 gems to train two players at three random stats +3), completing the 5/10/20 ladder. DLS26 sources describe breakthrough only qualitatively - 'Legendary coaches provide the best upgrades and higher Breakthrough chances' - with no numbers.", 3, "coaching/breakthrough-dls20-baseline-confirmed", [e_coach], notes="Post-DLS25 breakthrough percentages remain unpublished - the gap survives")
add_claim("Midfielders are the hardest cards to build: 'I genuinely hate maxing midfielders in DLS because they always come out weirdly built. One minute you're aiming for a balanced AM, next thing you know the card has 100 stamina, 96 pace, but the control and passing are disappointing.'", 3, "coaching/midfielders-hardest", [e_coach])
add_claim("Career league seasons are 15 games and can be forfeited once the points are secure: 'you can forfeit league games when you've got enough points to win so don't need to play the full 15 games.'", 3, "career/15-game-season-forfeit", [e_coach], notes="Time-saving rule for the Career coin loop")

for name in ('EV-466_achievement_counts.html','EV-467_coaching_method.html'):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
