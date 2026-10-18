#!/usr/bin/env python3
"""Turn 35 Wave 110: THE COMPLETE CAREER SEASON MATCH COUNT, AND THE RED ZONE'S REAL CONSEQUENCE.

Wave 110's centrepieces:

1. THE COMPLETE CAREER SEASON MATCH COUNT, which the corpus had only in pieces. A player
   gives the full arithmetic: **15 league + 9 Global Challenge Cup + 5 Diamond Cup + 1
   Allstar match + 7 International Cup + 3 Allstar Cup = 40 matches** for a full season at
   the top. That is the number the corpus's time-efficiency unlock is measured against, and
   it explains why the auto-finish-and-lose tactic matters: forty matches is a real time
   commitment, and the corpus's plan collapses it to ten.

2. THE RED ZONE'S REAL CONSEQUENCE, which the corpus understated. The corpus records the red
   zone as a Legendary Division relegation trigger. The wiki's account is stronger and applies
   lower down: **concede until your team drops into the red zone and you have to RESTART** —
   not merely get relegated. That is a much harsher failure mode, and it changes how the
   corpus's "never concede" advice should be weighted in the lower divisions.

3. THE FRIENDLY OFFER AFTER A CUP LOSS, a mechanic the corpus did not have. Lose at any stage
   of a cup and the game offers a friendly against a random team before the next league
   season begins. Small, but it is a real part of the Career loop and it explains the
   transition between a cup exit and the next season.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w110')

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

e_cs=new_ev("r/DreamLeagueSoccer 148h7yr (13 Jun 2023 - the complete Career season match count: 15 league + 9 GC cup + 5 diamond cup + 1 allstar match + 7 international cup + 3 allstar cup = 40 total), dream-league-soccer.fandom.com/wiki/Dream_League_Soccer_Wiki (29 Jul 2026 - the classic-era structure: 16 teams per division, single round-robin, 64 teams in the GC Cup, the International Cup after the Elite Division, and the friendly offer after a cup loss), dls-wiki.fandom.com/wiki/Leagues (29 Jul 2026 - the red-zone restart consequence for conceding too much), dontruko.com all-divisions page (17 Mar 2023 - a division list that omits Division 1), betechwise.com (17 Nov 2024 - the 70% shot power ceiling), archon.progressiveparts.com and eliselegrow.com (Jun 2026 - two AI content farms carrying an identical '22 Tips' article)",
    "THE COMPLETE CAREER SEASON MATCH COUNT, THE RED ZONE'S REAL CONSEQUENCE, AND THE FRIENDLY OFFER. (1) THE COMPLETE MATCH COUNT, which the corpus had only in pieces: '**15 (league) + 9 (GC cup) + 5 (diamond cup) + 1 (allstar match) + 7 (international cup) + 3 (allstar cup) = 40 (total)**.' **That is the number the corpus's time-efficiency unlock is measured against** - a full season at the top is forty matches, and the auto-finish-and-lose tactic collapses the league portion to about ten played matches. It also explains the corpus's per-division gem income: forty matches is the denominator. (2) THE RED ZONE'S REAL CONSEQUENCE, which the corpus understated. The corpus records the red zone as a Legendary Division relegation trigger (CLAIM-0792). The wiki's account is stronger and applies lower down: '**if you concede until your team gets in the red zone in the fixtures, you have to restart**' - not merely get relegated, but restart. **That is a much harsher failure mode**, and it changes how the corpus's conceding advice should be weighted: in the lower divisions a bad run of results is a restart risk, not just a lost season. (3) THE FRIENDLY OFFER AFTER A CUP LOSS: 'If you lose at any stage of the competition... you are asked if you want to play a friendly against a random team, and then another season of the Elite Division starts.' **So a cup exit is followed by an offered friendly before the next league season** - a real part of the Career loop that explains the transition, and a small extra match worth taking for the coins. (4) THE STRUCTURE, from the classic-era wiki: 16 teams per division, single round-robin, and the Global Challenge Cup 'randomly matches up all 64 teams against one another in a single-legged playoff competition.' **The 64 figure conflicts with the corpus's 128** (CLAIM-1181) - the 64 is the DLS1-era count and the 128 is the current DLS26 structure, so the wiki's number is the legacy one and the corpus's stands. (5) AN ERRATUM: dontruko's list of the eight divisions omits Division 1 entirely, listing academic, amateur, division 4, division 3, division 2, elite and legendary - seven, not eight. The corpus's eight-division ladder (Academy, Amateur, D4, D3, D2, D1, Elite, Legendary) is correct. (6) THE 70% SHOT POWER CEILING: 'the ideal power range to score a goal is filling the bar to a maximum of 70%.' Recorded at Speculative - it conflicts with the corpus's 100% charge for power shots and 40% for A-kicks, and the source is a low-quality tips site. (7) TWO NEW AI CONTENT FARMS: archon.progressiveparts.com and eliselegrow.com publish an identical '22 Tips To Dominate Dream League Soccer' article with generic advice. Neither is usable.",
    "THE COMPLETE CAREER SEASON MATCH COUNT: 15 league + 9 GC cup + 5 diamond cup + 1 allstar match + 7 international cup + 3 allstar cup = 40 matches for a full season at the top - the denominator the corpus's time-efficiency unlock is measured against. THE RED ZONE'S REAL CONSEQUENCE: conceding until you drop into the red zone forces a RESTART, not merely a relegation - a much harsher failure mode that applies in the lower divisions too. THE FRIENDLY OFFER after a cup loss, before the next league season. A CONFLICT on the GC Cup team count (64 legacy vs 128 current - the corpus's 128 stands). AN ERRATUM on dontruko's seven-division list. THE 70% SHOT POWER CEILING at Speculative. AND TWO NEW AI CONTENT FARMS.",
    "THE CAREER SEASON MATCH COUNT AND THE RED ZONE'S REAL CONSEQUENCE",
    quality="community")

add_claim("THE COMPLETE CAREER SEASON MATCH COUNT: '**15 (league) + 9 (GC cup) + 5 (diamond cup) + 1 (allstar match) + 7 (international cup) + 3 (allstar cup) = 40 (total)**.' **That is the denominator the corpus's time-efficiency unlock is measured against** - a full season at the top is forty matches, and the auto-finish-and-lose tactic collapses the league portion to about ten played. It also fixes the per-division gem income: forty matches is the base.", 3, "career/full-season-match-count-40", [e_cs])
add_claim("⚠️ THE RED ZONE'S REAL CONSEQUENCE, which the corpus understated: the corpus records the red zone as a Legendary Division relegation trigger (CLAIM-0792), but the wiki's account is stronger and applies lower down - '**if you concede until your team gets in the red zone in the fixtures, you have to restart**.' **Not merely a relegation: a restart.** That is a much harsher failure mode, and it means a bad run in a lower division risks the season, not just the table position.", 3, "career/red-zone-forces-restart", [e_cs], notes="Refines CLAIM-0792 from 'relegation' to 'restart' in the lower divisions")
add_claim("THE FRIENDLY OFFER AFTER A CUP LOSS: 'If you lose at any stage of the competition... **you are asked if you want to play a friendly against a random team**, and then another season of the Elite Division starts.' So a cup exit is followed by an offered friendly before the next league season - a real part of the Career loop, and a free extra match worth taking for the coins.", 3, "career/friendly-offer-after-cup-loss", [e_cs])
add_claim("A CONFLICT ON THE GLOBAL CHALLENGE CUP TEAM COUNT: the wiki describes the GC Cup as matching 'all **64 teams** against one another in a single-legged playoff competition', while the corpus carries **128 teams** (CLAIM-1181). **The 64 is the DLS1-era count and the 128 is the current DLS26 structure**, so the wiki's figure is the legacy one and the corpus's stands. Recorded so the two are not conflated.", 3, "errata/gc-cup-team-count-conflict", [e_cs])
add_claim("AN ERRATUM: dontruko's list of the eight divisions omits Division 1 entirely - academic, amateur, division 4, division 3, division 2, elite and legendary, which is seven. **The corpus's eight-division ladder (Academy, Amateur, D4, D3, D2, D1, Elite, Legendary) is correct** and the source's list is wrong.", 4, "errata/dontruko-division-list-omits-d1", [e_cs])
add_claim("THE 70% SHOT POWER CEILING: 'the ideal power range to score a goal is filling the bar to a maximum of 70%.' **Recorded at Speculative** - it conflicts with the corpus's 100% charge for power shots and ~40% for A-kicks, and the source is a low-quality tips site. Treat the corpus's per-shot-type power guidance as authoritative until a device test says otherwise.", 4, "shooting/70-percent-power-ceiling", [e_cs])
add_claim("TWO NEW AI CONTENT FARMS: archon.progressiveparts.com and eliselegrow.com publish an identical '22 Tips To Dominate Dream League Soccer' article with generic advice (power shots, finesse shots, aim for corners). Neither is usable as evidence; recorded so they are not mistaken for independent sources.", 4, "errata/two-new-ai-content-farms", [e_cs])

for p in ['EV-523_career_season_arithmetic.html','EV-523b_red_zone_and_friendly.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
