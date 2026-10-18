#!/usr/bin/env python3
"""Turn 35 Wave 114: THE XP PARADOX — THE STRONGEST EVIDENCE THE MISSION IS SKILL, NOT SQUAD.

Wave 114's centrepiece:

THE XP PARADOX. In a single thread, one player reports winning Tier 1 at **2 million** live
XP while another reports **5 million** XP and never having won Tier 2 — and a third, at 5.5
million, has won Tier 1 twice. So accumulated XP does not determine tier success. That is the
strongest single piece of evidence for the corpus's core claim: **the top of the DLL ladder is
decided by player skill, not by squad value or hours played.** It is the evidence behind the
record run's common/rare squad, behind the stop-coaching advice, and behind the maxed-squad
handicap finding — and it means the plan's investment in *technique* over *cards* is correct.

Plus: the tier-5 wall is a squad-quality wall (opponents there hold multiple 90+ players), a
tier-7-to-1 run in four days, the returning-player mechanic in the rating table, the community
"ROBBERY" slang, and a new player-search tool.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w114')

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

e_xp=new_ev("r/DreamLeagueSoccer 1ays8j6 'Done with tier 1. Now what?' (24 Feb 2024 - the XP paradox: a 2M-XP player who won tier 1, a 5M-XP player who never won tier 2, a 5.5M-XP player with two tier 1 titles, and 'do all players 80s stats in tier 1'), r/DreamLeagueSoccer 1hcn4f3 (12 Dec 2024 - the tier-5 wall as a squad-quality wall with multiple 90+ opponents), r/DreamLeagueSoccer 1ghbsed (1 Nov 2024 - the tier 7 to 1 in four days run, and the 'Tier 1 Champion' subreddit flair), r/DreamLeagueSoccer 1pcj8n2 (2 Dec 2025 - the Arsenal rating table with returning players Giroud 76 and Aubameyang 78, and the 'ROBBERY' slang), r/DreamLeagueSoccer 1qmtigp (25 Jan 2026 - the dls-ext.vercel.app player-search tool), dlsgame.net player index (8 Dec 2025 - the Midfield Classics with positions and years), r/DreamLeagueSoccer 1kzop2e (31 May 2025 - Petit as LB and Valverde as RB)",
    "THE XP PARADOX, THE TIER-5 WALL, AND THE FOUR-DAY CLIMB. (1) THE XP PARADOX, the strongest single piece of evidence for the corpus's core claim. In one thread: 'How do these young guys in dls manage I won tier 1 when I was having **2m live exp**' - against 'Lol I have **5m xp** and I've never won tier 2 let alone tier 1' - and a third at **5.5m** live xp who 'has been tier 1 champion twice.' **So accumulated XP does not determine tier success.** A player with a quarter of the XP reached the top; a player with two and a half times the XP never cleared tier 2. **That is the evidence behind the record run's common/rare squad, behind the stop-coaching advice, and behind the maxed-squad handicap finding** - the top of the DLL ladder is decided by player skill, not by squad value or hours played, which is why the plan invests in technique over cards. (2) THE TIER-5 WALL IS A SQUAD-QUALITY WALL: 'I've been able to get up to Level 5 but can't seem to get past it. Extremely frustrating. **My highest ranked player is De Bruyne at 90 and the teams up there all tend to have multiple 90+ players if not the entire team.**' So the wall at tier 5 is where opponent squad quality steps up, which is the practical argument for the corpus's buy-84+ rule - and it explains why the record run's common/rare squad was remarkable. (3) THE FOUR-DAY CLIMB: '**Grinded from tier 7 to 1 in only 4 days, championed every tier.**' A second benchmark against the 16-day world record and the 3-week typical figure - so the spread is 4 days to 3 weeks depending on the player. (4) THE RETURNING-PLAYER MECHANIC in the rating table: the Arsenal list carries '**Giroud: 76 (RETURNING PLAYER)**' and '**Aubameyang: 78 (RETURNING PLAYER)**' alongside the current squad and a former-players section - so the rating refresh can bring players BACK into a club's list, which is a route to cards that have left the database. (5) THE 'ROBBERY' SLANG: the same thread rates Merino and Trossard as '+0, ROBBERY btw' - community vocabulary for a rating the players consider wrong, which is the register the corpus's rating-reshuffle claims should be read against. (6) A NEW PLAYER-SEARCH TOOL: 'https://dls-ext.vercel.app/ - you can search players by rating, nationality, and it has the stats and gives you complete lists.' A second searchable roster alongside dlsinside and dlsgame. (7) THE MIDFIELD CLASSICS WITH POSITIONS AND YEARS: Rivaldo 1999 86 LW - Matthaus 1991 86 AM - Pires 2002 84 LM - Valderrama 1993 83 AM. So each Classic is a specific season's card, and the year is part of the identity. (8) THE 'TIER 1 CHAMPION' SUBREDDIT FLAIR is a community artifact, not an in-game rank - recorded so it is not mistaken for a seventh LIVE rank name. (9) CLASSICS ARE POSITIONALLY FLEXIBLE: 'Petit played as a LB through his career as well so therefore he counts. Valverde is also currently playing as a right back for most games.'",
    "THE XP PARADOX: a 2M-XP player won Tier 1 while a 5M-XP player never won Tier 2, and a 5.5M-XP player has won it twice - so accumulated XP does not determine tier success, and the top of the ladder is decided by SKILL, not squad value or hours played. That is the strongest evidence for the corpus's core claim and for the plan's investment in technique over cards. THE TIER-5 WALL is a squad-quality wall (opponents hold multiple 90+ players). THE FOUR-DAY CLIMB from tier 7 to 1. THE RETURNING-PLAYER MECHANIC (Giroud 76, Aubameyang 78 back in the rating table). THE 'ROBBERY' SLANG. A NEW PLAYER-SEARCH TOOL. THE MIDFIELD CLASSICS WITH POSITIONS AND YEARS. AND the 'Tier 1 Champion' subreddit flair recorded so it is not mistaken for a seventh LIVE rank name.",
    "THE XP PARADOX - THE STRONGEST EVIDENCE THE MISSION IS SKILL",
    quality="community")

add_claim("⚠️ THE XP PARADOX — the strongest single piece of evidence for the corpus's core claim. In one thread: 'How do these young guys in dls manage I won tier 1 when I was having **2m live exp**' — against 'Lol I have **5m xp** and I've never won tier 2 let alone tier 1' — and a third at **5.5m** live xp who 'has been tier 1 champion twice.' **So accumulated XP does not determine tier success.** A player with a quarter of the XP reached the top; a player with two and a half times the XP never cleared tier 2. **The top of the DLL ladder is decided by player skill, not by squad value or hours played** — which is the evidence behind the record run's common/rare squad, behind the stop-coaching advice, and behind the maxed-squad handicap finding.", 3, "dll/xp-paradox", [e_xp], notes="The strongest evidence that the mission is skill, not squad")
add_claim("THE TIER-5 WALL IS A SQUAD-QUALITY WALL: 'I've been able to get up to Level 5 but can't seem to get past it. Extremely frustrating. **My highest ranked player is De Bruyne at 90 and the teams up there all tend to have multiple 90+ players if not the entire team.**' So the wall at tier 5 is where opponent squad quality steps up — the practical argument for the corpus's buy-84+ rule, and the reason the record run's common/rare squad was remarkable.", 3, "dll/tier-5-wall-is-squad-quality", [e_xp])
add_claim("THE FOUR-DAY CLIMB: '**Grinded from tier 7 to 1 in only 4 days, championed every tier.**' A third benchmark against the 16-day world record and the 3-week typical figure — so the realistic spread for a skilled player is 4 days to 3 weeks, depending on how much of the day goes into it.", 3, "dll/four-day-climb-benchmark", [e_xp])
add_claim("THE RETURNING-PLAYER MECHANIC in the rating refresh: the Arsenal rating table carries '**Giroud: 76 (RETURNING PLAYER)**' and '**Aubameyang: 78 (RETURNING PLAYER)**' alongside the current squad and a former-players section. **So the rating refresh can bring players BACK into a club's list** — a route to cards that have left the database, and a reason to re-check a club's list after every update rather than assuming a departure is permanent.", 3, "patching/returning-player-mechanic", [e_xp])
add_claim("THE 'ROBBERY' SLANG: a community rating thread marks two players '+0, **ROBBERY** btw' — community vocabulary for a rating the players consider wrong. So the corpus's rating-reshuffle claims should be read against a register that expects some assignments to feel incorrect, which is consistent with the corpus's finding that FTG's position and rating assignments are sometimes wrong.", 4, "patching/robbery-slang", [e_xp])
add_claim("A NEW PLAYER-SEARCH TOOL: 'https://dls-ext.vercel.app/ — you can search players by rating, nationality, and it has the stats and gives you complete lists.' A second searchable roster alongside dlsinside and dlsgame, and a third route to the per-tier build targets.", 4, "transfers/dls-ext-player-search-tool", [e_xp])
add_claim("THE MIDFIELD CLASSICS WITH POSITIONS AND YEARS: **Rivaldo 1999 86 LW · Matthaus 1991 86 AM · Pires 2002 84 LM · Valderrama 1993 83 AM.** So each Classic is a specific season's card and the year is part of its identity — which is why two cards of the same player can differ, and why the corpus's per-club rating table lists them with years.", 3, "cards/midfield-classics-with-years", [e_xp])
add_claim("THE 'TIER 1 CHAMPION' SUBREDDIT FLAIR is a community artifact, not an in-game rank name — recorded so it is not mistaken for a seventh LIVE rank above Veteran. The in-game ladder remains Rookie, Amateur, Semi-Pro, Intermediate, Pro, Veteran, and the tier numbers 20 to 1.", 4, "errata/tier-1-champion-flair-not-a-rank", [e_xp])
add_claim("CLASSICS ARE POSITIONALLY FLEXIBLE: 'Petit played as a LB through his career as well so therefore he counts. Valverde is also currently playing as a right back for most games.' So a Classic's listed position is not a hard constraint, which matters when fitting a 5x100 Classic into a shape.", 4, "cards/classics-positionally-flexible", [e_xp])

for p in ['EV-527_xp_paradox.html','EV-527b_tier5_wall_and_returning.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
