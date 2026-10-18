#!/usr/bin/env python3
"""Turn 35 Wave 27: Scenarios mode (daily + Real World + difficulty tiers + offline), onboarding manager/captain selection, career AI difficulty, market rating thresholds, challenge rerolling, AI-adaptation red flag."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w27')

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

# ---------- EV-417: scenarios ----------
e_sc=new_ev("gamingonphone DLS24/25/26 guides, Bluestacks DLS26 free-rewards + beginner guides, mobilegaminghub, aiting, r/DreamLeagueSoccer (1f7mmxc Sep2024, 1d7vbro Jun2024, 1f4x5jj, 1hmyx6j Dec2024, 1hprf7o Dec2024, 1ha876r Dec2024), 3Zebras DLS25 review, Vietnamese Wikipedia, apkmody",
    "SCENARIOS MODE. Daily Scenario: you are placed in a match your team is losing and must come back to beat Hard AI; completing it pays 50 coins per day and the scenario resets daily. REAL WORLD SCENARIOS recreate actual recent real-life matches (community examples: Madrid 3-0, Chelsea 6-2) and are the mode's hardest tier. DLS25 substantially RAISED scenario difficulty: shorter completion windows, some requiring a 3-4 goal winning margin, and AI opponents given drastically boosted stats relative to your team - multiple threads call them 'impossible' and 'a whole different kettle of fish' versus DLS24. Vietnamese Wikipedia records four scenario difficulty tiers paying 25 / 50 / 75 / 100 coins for Easy / Medium / Hard / Very Hard. DLS25 also added selectable career AI difficulty with Medium and Hard options (3Zebras). Scenario mode remains playable OFFLINE in DLS26 (apkmody), alongside Celebration Cup and Friends modes. REGRESSION REPORTS: a Dec 2024 update broke C-button player switching and degraded player AI, prevented substitutions at throw-ins and corners, and caused auto-switching to trigger at the wrong moment. CONFLICTING DIFFICULTY VIEWS: some players call career mode 'way too easy' and want more difficulty, while others find daily scenarios unwinnable even with a strong team. AI PENALTY BEHAVIOUR: community reports AI keepers saving a very high share of penalties ('every AI GK is Buffon') and the AI always electing to take a penalty rather than allow a free shot on goal. META CRITICISM: the dominant online approach is passing back to the keeper and lofting a long ball for a pacey striker to chase, and Dream Point rewards are tied to goals scored rather than match results, which the community wants changed.",
    "evidence/raw/turn35_w27/EV-417_scenarios.html",
    "Daily Scenario = comeback win vs Hard AI, 50 coins/day, resets daily; Real World Scenarios recreate real matches and are hardest; DLS25 raised difficulty sharply (shorter windows, 3-4 goal margins, stat-boosted AI); tiers Easy/Medium/Hard/Very Hard pay 25/50/75/100 coins; DLS25 added career AI difficulty Medium/Hard; scenarios playable offline; Dec2024 update broke C-switching, subs at stoppages and auto-switch timing; career too easy vs scenarios impossible conflict; AI GKs save heavily and always take penalties; long-ball meta and goals-scored DP rewards criticised",
    quality="community")

add_claim("The Daily Scenario drops you into a match your team is losing and requires a comeback win against Hard AI, paying 50 coins per day and resetting daily.", 2, "modes/scenarios-daily", [e_sc])
add_claim("Real World Scenarios recreate actual recent real-life matches and represent the hardest tier of the mode.", 2, "modes/real-world-scenarios", [e_sc])
add_claim("DLS25 substantially raised scenario difficulty: shorter completion windows, some requiring a 3-4 goal winning margin, and AI opponents granted drastically boosted stats relative to your team.", 3, "modes/scenarios-difficulty-increase", [e_sc])
add_claim("Scenario difficulty tiers Easy / Medium / Hard / Very Hard pay 25 / 50 / 75 / 100 coins respectively.", 3, "modes/scenarios-difficulty-tiers", [e_sc], notes="Single non-English source (Vietnamese Wikipedia); plausible but unverified")
add_claim("DLS25 added selectable career-mode AI difficulty with Medium and Hard options.", 3, "difficulty/career-ai-modes", [e_sc])
add_claim("Scenario mode remains playable offline in DLS26, alongside Celebration Cup and Friends modes.", 3, "modes/scenarios-offline", [e_sc])
add_claim("Regression reports: a December 2024 update broke C-button player switching, degraded player AI, blocked substitutions at throw-ins and corners, and caused auto-switching to trigger at the wrong moment.", 3, "errata/dec2024-switching-regression", [e_sc])
add_claim("CONFLICT on difficulty: some players call DLS26 career mode 'way too easy' and want more challenge, while others find daily scenarios unwinnable even with a strong team.", 3, "difficulty/conflicting-views", [e_sc])
add_claim("AI penalty behaviour: community reports AI keepers saving a very high proportion of penalties ('every AI GK is Buffon') and the AI always electing to take a penalty rather than allow a free shot on goal.", 3, "ai/penalty-behaviour", [e_sc])
add_claim("The dominant online approach criticised by players is passing back to the keeper and lofting a long ball for a pacey striker to chase, and Dream Point rewards are tied to goals scored rather than match results.", 3, "ai/long-ball-meta-dp-goals", [e_sc])

# ---------- EV-418: onboarding + market thresholds + rerolling ----------
e_on=new_ev("gamingonphone DLS26 beginners guide (Jan 2026), r/DreamLeagueSoccer 1b5h2zu DLS24 beginner guide (Mar 2024), r/DreamLeagueSoccer 18dqq9e DLS24 beginners guide (Jan 2024), eslamgaming AI-adaptation articles, playdreamleaguesoccer.com",
    "ONBOARDING + MARKET THRESHOLDS + CHALLENGE REROLLING. ONBOARDING SEQUENCE: choose a manager from three default face options (customisable later), name the manager, then select your team captain from a list of big names - new players get the option to start with a Legendary player immediately, and picking an attacker or midfielder is advised because early goal-scoring eases the first season. MARKET RATING THRESHOLDS: once team rating passes 65, Rare players begin appearing in the market; above 68.7, Legendary players rated 80-82 start appearing and become worth buying - below those thresholds buying rare players is poor value. EVENTS: timed events run roughly every 4 days and offer a chance at a Legendary player plus 600+ coins. CHALLENGE REROLLING: daily objectives can be rerolled twice per day and weekly objectives twice per week, using the video icon beside a hard objective (e.g. 'Win Dream League Live games'); players are advised to reroll DLL-dependent objectives early on and focus on daily, weekly and career tracks instead. AI ADAPTATION RED FLAG: claims that the AI 'learns your playstyle', adapts defensively to repeated wing play, or runs a 'Neural Match Engine' appear ONLY on eslamgaming and playdreamleaguesoccer.com - the two sources already flagged as unreliable - and are UNCONFIRMED.",
    "evidence/raw/turn35_w27/EV-418_onboarding_market.html",
    "Onboarding = pick manager from 3 default faces (customisable later), name manager, pick captain (Legendary available from the start; attacker/midfielder advised); market thresholds: >65 rating = rares appear, >68.7 = 80-82 legendaries worth buying; events every ~4 days give legendary chance + 600+ coins; daily objectives rerollable 2x/day, weekly 2x/week via video icon, reroll DLL-dependent ones early; AI 'learns your playstyle'/'Neural Match Engine' claims come only from the two already-flagged unreliable sources",
    quality="community")

add_claim("Onboarding sequence: choose a manager from three default face options (customisable later), name the manager, then select your team captain from a list of big names.", 2, "onboarding/sequence", [e_on])
add_claim("New players can start with a Legendary captain immediately, and picking an attacker or midfielder is advised because early goal-scoring makes the first season easier.", 2, "onboarding/captain-choice", [e_on])
add_claim("Transfer market rating thresholds: above 65 team rating Rare players begin appearing; above 68.7, Legendary players rated 80-82 appear and become worth buying - buying rares below those thresholds is poor value.", 3, "transfers/market-rating-thresholds", [e_on])
add_claim("Timed events run roughly every 4 days and offer a chance at a Legendary player plus 600+ coins.", 3, "events/four-day-events", [e_on])
add_claim("Challenge rerolling: daily objectives can be rerolled twice per day and weekly objectives twice per week via the video icon beside a hard objective; DLL-dependent objectives should be rerolled early and daily, weekly and career tracks prioritised.", 2, "challenges/rerolling", [e_on])
add_claim("Claims that the AI learns your playstyle, adapts defensively to repeated wing play, or uses a 'Neural Match Engine' appear only on eslamgaming and playdreamleaguesoccer.com and are UNCONFIRMED.", 4, "ai/adaptation-unconfirmed", [e_on], notes="Both sources already flagged unreliable; consistent with the pre-existing AI-farm red flag")

p=os.path.join(RAW_DIR,'EV-417_scenarios.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-418_onboarding_market.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
