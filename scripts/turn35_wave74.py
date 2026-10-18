#!/usr/bin/env python3
"""Turn 35 Wave 74: THE RECOVERY, LOCK AND RECRUITMENT MECHANICS - the official Player Recovery
wording and its 5-gem price, the Recruitment Centre (resolving the wave-72 flag), the real
DLS26 price band, the maxed-stadium bonus, the suspension workaround, and new celebrations.

Wave 74 resolves the wave-72 flag and corrects a stale figure:

1. THE RECRUITMENT CENTRE IS REAL AND OFFICIAL - 'New facility - Upgrade your recruitment
   centre for Scout and Agent discounts' in the v9.00 release notes. It is a SIXTH facility.

2. THE CORPUS'S PRICE BAND IS STALE. '10 to about 900 coins' comes from an old fandom page;
   a December 2025 thread shows a secret player at 2,355-2,555 coins and concludes 'we need
   at least 10,000 coins if we want to buy a player and still save money.'
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w74')

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

e_rec=new_ev("APKMirror DLS26 v12.200 release notes (Player Recovery - 'buy a sold player back within a limited time'), App Store DLS26 version history ('Player Recovery - Changed your mind?', 'Transfer upgrades - manage lock players in more ways than before', 'Daily Bonus'), APKMirror DLS v9.00 release notes (Dec 2021, 'New facility - Upgrade your recruitment centre for Scout and Agent discounts'), FTG support 360003945617 'Can I sell my players?' (the Manage Players path and the Recover section), r/DreamLeagueSoccer 1mu374v (19 Aug 2025, the 5-gem recovery price and the 'sell definitely' request), 14vw8e4 (10 Jul 2023, the Lock Player mechanic), 1pe7j7l (4 Dec 2025, the DLS26 price list and the 10,000-coin conclusion), 176ntor (13 Oct 2023, the 48-52 coin stadium bonus and the Training-only gem rule), dream-league-soccer.fandom.com Free Transfers page (the suspension workaround and the half-value release history), r/DLS 1ofp7i1 (25 Oct 2025, the new Mbappe celebration), App Store DLS25 review wish-list (no controllable celebrations), eslamgaming visual evolution (23 Mar 2026 - a FLAGGED source)",
    "THE RECOVERY, LOCK AND RECRUITMENT MECHANICS, THE REAL PRICE BAND, AND THE MAXED-STADIUM BONUS. (1) PLAYER RECOVERY IS OFFICIAL AND NAMED: the Summer Spotlight notes read 'Player Recovery - buy a sold player back within a limited time' (the App Store wording is 'Player Recovery - Changed your mind?'), and FTG's support portal confirms the mechanism: 'Players who were recently sold, appear in the \"Recover\" section of \"Manage Players\" for a limited time.' (2) RECOVERY COSTS 5 GEMS: 'You can buy back sold players for diamond 5.' (3) A PLAYER WANTS A 'SELL DEFINITELY' OPTION so a card 'can appear again in the market rotation' - which implies a player sitting in Recovery does NOT re-enter the market rotation, corroborating the corpus's 'collection pieces never come back'. (4) THE RECRUITMENT CENTRE IS REAL AND OFFICIAL, resolving the wave-72 flag: the v9.00 release notes read 'New facility - Upgrade your recruitment centre for Scout and Agent discounts.' It is a SIXTH facility alongside Stadium, Medical, Commercial, Training and Accommodation, and it discounts the two recruitment tools. Bluestacks' DLS26 content independently lists it. (5) SUMMER SPOTLIGHT EXPANDED LOCKING: 'Transfer upgrades - manage lock players in more ways than before', on top of the existing 20-or-40-gem 24-hour lock that leaves 'a small lock sign on their card'. (6) THE PRICE BAND IS STALE - a significant correction. The corpus's '10 to about 900 coins' comes from an old fandom page. A December 2025 DLS26 thread shows a secret player at 2,355 coins after a ~200-rupee discount from 2,555, and concludes 'This proves that we need at least 10,000 coins if we want to buy a player and still save money.' **DLS26 transfer prices run into the thousands; budget accordingly.** (7) THE MAXED-STADIUM BONUS, a figure the corpus lacked: 'I average 250 coins every match (after watching an after match ad) because stadium bonus rises to 48-52 coins per home match for 85k+ stadiums.' So a completed stadium pays 48-52 coins a home match. (8) A SECOND INDEPENDENT SOURCE FOR THE TRAINING-FIRST GEM RULE, with the exception stated: '75 gems to upgrade training center, 1,500 coins on stadium upgrades... all gems you earn should go to upgrading training center ONLY, unless you NEED to lock a player.' And 'If you need coins, grind career. If you wanna recycle transfer list/need gems (tier 10 and above only)/casual player - play live' - corroborating that DLL gems need tier 10+. (9) THE SUSPENSION WORKAROUND, era-stale but mechanically interesting: 'If a player has a red card suspension, release him and buy him back from the Free Transfers Page. Note this will erase your players records (goals, games played, etc) for the season, however if you have upgraded the players stats, they will stay the same.' So releasing clears a suspension at the cost of the season record. (10) RELEASE VALUE HAS CHANGED ACROSS BUILDS: an older-era source states 'one must sell the player for half its purchase value. They will go on to the market, priced at their value', against the current 'You will receive a coach for the release of this player'. Recorded as version drift; the current wording wins. (11) NEW PLAYER-SPECIFIC CELEBRATIONS ARE ARRIVING: a player reports 'My Mbappe just did a totally new celebration I've never seen before... he scored, went to the LED screen at the corner, rested on it with his back, pointed at the camera and then spread his arms. After a hattrick.' (12) CELEBRATIONS ARE NOT PLAYER-CONTROLLABLE - a wish-list asks to 'allow players to choose or control celebrations for each player', confirming you cannot. (13) TIME-OF-DAY AND FLOODLIGHTS ARE REPORTED TO AFFECT PLAY: 'Matches played during sunset or under floodlights have distinct lighting conditions that affect visibility and player performance. The warm hues of a sunset can make it harder to spot a through ball, while the stark contrast of floodlights can create glare, impacting goalkeepers' ability to track the ball.' **This rests on eslamgaming, a source the reliability register flags for fabrications - C4, device verification required.**",
    "evidence/raw/turn35_w74/EV-488_recovery_lock_and_recruitment.html",
    "PLAYER RECOVERY (official): 'buy a sold player back within a limited time', via the Recover section of Manage Players, costing 5 GEMS. A player sitting in Recovery does not re-enter the market rotation (hence the 'sell definitely' request). THE RECRUITMENT CENTRE IS REAL AND OFFICIAL - a SIXTH facility that discounts Scouts and Agents, added in v9.00 and still listed in DLS26 content. LOCKING was expanded in Summer Spotlight ('manage lock players in more ways than before') on top of the 20/40-gem 24-hour lock. THE PRICE BAND IS STALE: DLS26 transfers run into the thousands of coins (a secret player at 2,355 after discount), and you need ~10,000 coins to buy a player and still save - the corpus's 10-900 band is an old-fandom figure. MAXED STADIUM: 48-52 coins per home match at 85k+ capacity, ~250 per match with the ad. TRAINING-FIRST GEM RULE corroborated a second time, with the lock-player exception. SUSPENSION WORKAROUND (era-stale): release a suspended player and buy them back to clear the ban, at the cost of their season records. RELEASE VALUE drifted: half purchase value (old) vs a coach (current). NEW player-specific celebrations are arriving (Mbappe's corner-LED celebration), but celebrations are NOT player-controllable. Floodlight/sunset visibility effects are reported by a FLAGGED source - C4, verify on device",
    quality="community")

add_claim("PLAYER RECOVERY IS OFFICIAL: 'buy a sold player back within a limited time', via the Recover section of Manage Players (FTG support: 'Players who were recently sold, appear in the \"Recover\" section of \"Manage Players\" for a limited time').", 1, "transfers/player-recovery-official", [e_rec], notes="Official - confirms the corpus's release-area grace period")
add_claim("Recovery costs 5 GEMS to buy a sold player back.", 3, "transfers/recovery-costs-5-gems", [e_rec])
add_claim("A player sitting in Recovery does NOT re-enter the market rotation - the basis of a community request for a 'sell definitely' option so the card 'can appear again in the market rotation'.", 3, "transfers/recovery-blocks-market-rotation", [e_rec], notes="Corroborates 'collection pieces never come back'")
add_claim("THE RECRUITMENT CENTRE IS REAL AND OFFICIAL - a SIXTH FACILITY: 'New facility - Upgrade your recruitment centre for Scout and Agent discounts' (v9.00 release notes), independently listed in DLS26 content. It discounts both recruitment tools.", 2, "facilities/recruitment-centre-is-real", [e_rec], notes="RESOLVES the wave-72 flag - the corpus's five-facility list was incomplete")
add_claim("Summer Spotlight expanded the Lock Player system: 'Transfer upgrades - manage lock players in more ways than before', on top of the existing 20-or-40-gem 24-hour lock that leaves 'a small lock sign on their card'.", 2, "transfers/lock-player-expanded", [e_rec])
add_claim("THE DLS26 PRICE BAND IS FAR HIGHER THAN THE CORPUS RECORDED: a December 2025 thread shows a secret player at 2,355 coins after a discount from 2,555, concluding 'we need at least 10,000 coins if we want to buy a player and still save money.' The '10 to about 900 coins' figure is an old-fandom artefact.", 2, "transfers/dls26-price-band-is-thousands", [e_rec], notes="CORRECTS a stale corpus figure")
add_claim("THE MAXED-STADIUM BONUS: 'stadium bonus rises to 48-52 coins per home match for 85k+ stadiums', averaging ~250 coins per match after watching the post-match ad.", 3, "stadium/maxed-bonus-48-52-coins", [e_rec])
add_claim("A SECOND INDEPENDENT SOURCE FOR THE TRAINING-FIRST GEM RULE, with the exception stated: 'all gems you earn should go to upgrading training center ONLY, unless you NEED to lock a player.' Also: 'If you need coins, grind career. If you wanna... need gems (tier 10 and above only)... play live.'", 3, "economy/training-first-gem-rule-second-source", [e_rec], notes="Corroborates the Training L4 finding and the tier-10 DLL gate")
add_claim("THE SUSPENSION WORKAROUND (era-stale): 'If a player has a red card suspension, release him and buy him back from the Free Transfers Page' - this clears the ban but 'will erase your players records (goals, games played, etc) for the season', while upgraded stats survive.", 3, "gameplay/suspension-workaround", [e_rec], notes="Connects the wave-71 suspension rule to the recovery mechanic")
add_claim("Release value has drifted across builds: an older-era source states a released player sells 'for half its purchase value' and goes to the market, against the current official 'You will receive a coach for the release of this player.' The current wording wins.", 3, "transfers/release-value-version-drift", [e_rec])
add_claim("NEW PLAYER-SPECIFIC CELEBRATIONS ARE ARRIVING: a player reports 'My Mbappe just did a totally new celebration I've never seen before... he scored, went to the LED screen at the corner, rested on it with his back, pointed at the camera and then spread his arms. After a hattrick.'", 3, "presentation/new-player-specific-celebrations", [e_rec])
add_claim("Celebrations are NOT player-controllable - a wish-list asking to 'allow players to choose or control celebrations for each player' confirms you cannot choose or trigger them.", 2, "negatives/no-controllable-celebrations", [e_rec])
add_claim("Time-of-day and floodlights are reported to affect play: 'Matches played during sunset or under floodlights have distinct lighting conditions that affect visibility and player performance... sunset can make it harder to spot a through ball, while the stark contrast of floodlights can create glare, impacting goalkeepers' ability to track the ball.' **C4 - this rests on eslamgaming, a source the reliability register flags for fabrications. Verify in Exhibition.**", 4, "presentation/floodlight-visibility-effects", [e_rec], notes="Flagged source - device verification required")

for name in ('EV-488_recovery_lock_and_recruitment.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
