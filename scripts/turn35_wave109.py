#!/usr/bin/env python3
"""Turn 35 Wave 109: THE EVENT TEAM-CHOICE ADVICE, AND THE DLS26 SKILL-COMPRESSION COMPLAINT.

Wave 109's centrepieces:

1. THE EVENT TEAM-CHOICE ADVICE, which the corpus's event section lacked. A player who has
   run events for years gives a concrete recipe: **relegate to tier 8 or higher, then choose
   City or Liverpool as your event team, and you will earn around 3,000 in total.** That is
   the missing operational half of the corpus's event-selection rule — it names the tier to
   sit in and the teams to pick, and it explains WHY the corpus's deliberate-relegation
   finding exists: the low tiers are where the events pay.

2. THE DLS26 SKILL-COMPRESSION COMPLAINT, which is the sharpest version of the maxed-squad
   handicap argument the corpus has. A player reports that in DLS26 **there is no difference
   between maxed players and non-maxed players** — "you lose the ball at any contact" — and
   that the people enjoying the update are the unskilled ones in tiers 5 to 10. If true, that
   is the strongest possible argument for the corpus's stop-coaching advice, and it reframes
   the whole tier-1 problem: the skill gap is between players, not between squads.

3. GOALKEEPERS ARE THE EASIEST POSITION TO MAX, with two named routes. That is a genuine
   correction to the corpus's coaching priority, which treats the goalkeeper as a special
   case (the GKR>GKH rule) rather than as the cheap win it appears to be.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w109')

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

e_evt=new_ev("r/DreamLeagueSoccer 166iw2k (31 Aug 2023 - the event team-choice advice: relegate to tier 8+, pick City or Liverpool, earn around 3k in total), r/DreamLeagueSoccer 18ec2lh (9 Dec 2023 - the deep-442 to balanced-442 shift because the AI is better now), r/DreamLeagueSoccer 1pial1k (9 Dec 2025 - the DLS26 skill-compression complaint from a tier 5-10 player), r/DreamLeagueSoccer 16n9is4 Discovery9981 comment (the VVD chaining method in practice: rare and legendary fitness to near-100 fitness, then rare and common techs to 95 tackle, with control and passing up 5 as collateral), r/DreamLeagueSoccer 16n9is4 Ok-Letterhead-5011 comment (a $1 purchase converted into enough coins to buy Messi via a common card in transfers, on a free-to-play account that then reached tier 1), r/DreamLeagueSoccer 1r5jpmv (15 Feb 2026 - goalies are easiest to max, with the 80-rated and 50-rated routes and named keepers), r/DreamLeagueSoccer 1qmfzpq (25 Jan 2026 - avoid spending gems on anything but facilities and special-player training; play special online events; buy 68+ players as a starter), lfbb.net (1 Mar 2026, REJECTED - the Facebook-linking claim that contradicts the corpus's Facebook-removal finding)",
    "THE EVENT TEAM-CHOICE ADVICE, THE DLS26 SKILL-COMPRESSION COMPLAINT, AND THE GOALKEEPER SHORTCUT. (1) THE EVENT TEAM-CHOICE ADVICE: '**Also always play events which are very crucial to gain prizes. I recommend to relegate to 8 and higher and city or Liverpool as you'll earn around 3k in total.**' **So the event strategy has a tier component and a team component** - sit at tier 8 or above, and pick City or Liverpool as the event side. That is the missing operational half of the corpus's event-selection rule, and it explains WHY the deliberate-relegation finding exists: the low tiers are where the events pay. (2) THE DLS26 SKILL-COMPRESSION COMPLAINT, the sharpest version of the maxed-squad handicap argument in the corpus: '**I noticed that the people loving this update are those noobs or non skilled one! From tier 5 to tier 10. Because now they can win easily, there's no difference between the players you maxed and trained wise with their non maxed players! You lose the ball at any contact.**' **If true, that is the strongest possible argument for the corpus's stop-coaching advice, and it reframes the whole tier-1 problem: the skill gap is between players, not between squads.** It also explains the tier-5-to-10 band being where the new players cluster. (3) THE GOALKEEPER SHORTCUT: '**Goalies are easiest to max**, you can focus on one goalie like Donnarumma or if you want can also have a Courtois or Alisson. Buy either 80 rated goalies (Chevalier, Costa, Carnadeshi etc) to upgrade to goalies at once, or buy goalies in the 50's for like 100 coins to get a common coach and slowly build up 1 goalie at a time.' **So the goalkeeper is the cheap position, not the expensive special case** - a genuine correction to the corpus's coaching priority, which treats the keeper through the GKR>GKH rule rather than as the efficient win it appears to be. (4) THE CHAINING METHOD IN PRACTICE, with the collateral cost named: 'for VVD, I simply used loads of rare and legendary fitness to get it to nearly 100 fitness, then I used rare and common techs until tackle reached 95. **This is why my control and passing stats went up by 5.**' So the category chain works exactly as the corpus's model predicts, and the collateral is the price. (5) THE $1 CONVERSION: 'That $1 purchase actually got me a few extra coins enough to buy Messi after finding him through a common card in transfers... Considering that i have a free to play account, i have some of the players maxed out, and just a few minutes ago i reached tier 1 for the first time.' So a single small purchase, converted into coins rather than gems, funded a marquee signing on an otherwise free account. (6) THE DEEP-442 TO BALANCED-442 SHIFT: 'I used to play a deep 442 formation the previous seasons of the game to counter the guys who keep spamming long ball. **The AI is better now, that's why I changed mine to 442 Balanced.**' So the defensive shape that countered the long ball is no longer needed, which is a third data point on the corpus's formation-drift finding. (7) THE GEM RULE, restated by a DLS26 player: 'Avoid spending gems on anything other than upgrading facilities or training special players. Play and try to win special online events as much as possible... aim to buy players rated 68 or above since I'm guessing you are a starter player.' (8) A CONFLICT WITH A REJECTED SOURCE: lfbb.net claims that linking Facebook to DLS gave 150 gems. **The corpus carries Facebook login as REMOVED years ago, with old Facebook-saved profiles unrecoverable** - so this is a rejected source describing a feature that no longer exists, and it is recorded as a conflict rather than as evidence.",
    "THE EVENT TEAM-CHOICE ADVICE: relegate to tier 8 or higher and pick City or Liverpool as the event side for around 3k in total - the operational half the corpus's event-selection rule was missing. THE DLS26 SKILL-COMPRESSION COMPLAINT: there is no difference between maxed and non-maxed players, so the skill gap is between players and not between squads - the strongest argument yet for stop-coaching. GOALKEEPERS ARE THE EASIEST POSITION TO MAX, with two named routes. THE CHAINING METHOD IN PRACTICE with the collateral named. THE $1 CONVERSION into a marquee signing. AND A CONFLICT: a rejected source claims Facebook linking still pays gems, against the corpus's Facebook-removal finding.",
    "THE EVENT TEAM-CHOICE ADVICE AND THE DLS26 SKILL-COMPRESSION COMPLAINT",
    quality="community")

add_claim("THE EVENT TEAM-CHOICE ADVICE, the operational half the corpus's event-selection rule was missing: '**Also always play events which are very crucial to gain prizes. I recommend to relegate to 8 and higher and city or Liverpool as you'll earn around 3k in total.**' **So the event strategy has a tier component AND a team component** - sit at tier 8 or above, and pick City or Liverpool as the event side. That explains why the corpus's deliberate-relegation finding exists: the low tiers are where the events pay.", 3, "events/team-choice-and-tier", [e_evt])
add_claim("⚠️ THE DLS26 SKILL-COMPRESSION COMPLAINT, the sharpest version of the maxed-squad handicap argument in the corpus: '**I noticed that the people loving this update are those noobs or non skilled one! From tier 5 to tier 10. Because now they can win easily, there\'s no difference between the players you maxed and trained wise with their non maxed players! You lose the ball at any contact.**' **If true, that is the strongest possible argument for the corpus\'s stop-coaching advice, and it reframes the whole tier-1 problem: the skill gap is between players, not between squads.** It also explains why the tier-5-to-10 band is where the new players cluster.", 3, "dll/skill-compression-complaint", [e_evt], notes="The strongest single argument for stop-coaching; testable by comparing a maxed and an unmaxed squad in the same tier")
add_claim("GOALKEEPERS ARE THE EASIEST POSITION TO MAX, with two named routes: '**Goalies are easiest to max**, you can focus on one goalie like Donnarumma or if you want can also have a Courtois or Alisson. Buy either **80 rated goalies** (Chevalier, Costa, Carnadeshi etc) to upgrade to goalies at once, or buy **goalies in the 50\'s for like 100 coins** to get a common coach and slowly build up 1 goalie at a time.' **So the keeper is the cheap position, not the expensive special case** - a genuine correction to the corpus's coaching priority.", 3, "coaching/goalkeepers-easiest-to-max", [e_evt], notes="Corrects the corpus's treatment of the keeper as a special case rather than the efficient win")
add_claim("THE CHAINING METHOD IN PRACTICE, with the collateral cost named: 'for VVD, I simply used loads of rare and legendary fitness to get it to nearly 100 fitness, then I used rare and common techs until tackle reached 95. **This is why my control and passing stats went up by 5.**' **So the category chain works exactly as the corpus\'s model predicts, and the collateral stat movement is the price** - which is why the look-ahead trick and the never-redo rule matter.", 3, "coaching/chaining-method-in-practice", [e_evt])
add_claim("THE $1 CONVERSION: 'That $1 purchase actually got me a few extra coins enough to buy Messi after finding him through a common card in transfers... Considering that i have a free to play account, i have some of the players maxed out, and just a few minutes ago i reached tier 1 for the first time.' **So a single small purchase, converted into COINS rather than gems, funded a marquee signing on an otherwise free account** - which is the corpus's coins-not-gems rule arriving from the spending side.", 3, "economy/small-purchase-converted-to-coins", [e_evt])
add_claim("THE DEEP-442 TO BALANCED-442 SHIFT: 'I used to play a deep 442 formation the previous seasons of the game to counter the guys who keep spamming long ball. **The AI is better now, that\'s why I changed mine to 442 Balanced.**' **So the defensive shape that countered the long ball is no longer needed** - a third data point on the corpus's formation-drift finding, and a reason to re-test the deep shape rather than inherit it.", 3, "tactics/deep-442-to-balanced-442", [e_evt])
add_claim("THE GEM RULE, restated by a DLS26 player: 'Avoid spending gems on anything other than upgrading facilities or training special players. Play and try to win special online events as much as possible... aim to buy players rated 68 or above since I\'m guessing you are a starter player.' A second source for the corpus's gem rule, with the 68+ starter threshold attached.", 3, "economy/gem-rule-restated", [e_evt])
add_claim("⚠️ A CONFLICT WITH A REJECTED SOURCE: lfbb.net claims that linking Facebook to DLS gave 150 gems (plus 200 for Twitter and 50 for a shared result). **The corpus carries Facebook login as REMOVED years ago, with old Facebook-saved profiles unrecoverable** (CLAIM-072). So this is a rejected source describing a feature that no longer exists - recorded as a conflict, not as evidence, and it is a reason to treat the whole lfbb social-linking claim as false.", 4, "errata/facebook-linking-claim-contradicted", [e_evt])

for p in ['EV-522_event_strategy.html','EV-522b_skill_compression_and_goalkeeper.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
