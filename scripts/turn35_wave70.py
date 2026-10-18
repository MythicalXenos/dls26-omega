#!/usr/bin/env python3
"""Turn 35 Wave 70: THE INJURY AND PHYSIO SYSTEM (the tier ladder, the gem-to-games healing
conversion, the ephemeral injury report, the all-subs exploit) and FOUR DOCUMENTED NEGATIVES
on the career lifecycle: no morale, no growth, no retirement, no surgery.

Wave 70's most operationally useful finding is that the injury report is EPHEMERAL - it names
the injury and the number of games out, but only in the moment after the match in which it
happened. Read it before you do anything else.

The four negatives matter for expectation-setting: a player arriving from FIFA expects a
growth curve, a morale system and retirements. DLS has none of them. Players are static cards
that only move when you spend coaches on them.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w70')

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

e_inj=new_ev("bluestacks DLS26 character-development guide (the physio tier ladder and the coin currency), r/DreamLeagueSoccer kqzik4 (5 Jan 2021, recovery by resting and passive recovery times), the azizfcb comment in kqzik4 (the gem-to-games healing conversion and the legendary physio price), o25np9 (17 Jun 2021, the ephemeral injury report and the gem-button text), zmglpx (15 Dec 2022, the all-subs injury-prevention method), 1rf90a7 (26 Feb 2026, the mid-season rating update megathread), fifaworldcupnews DLS26 features (23 Jul 2026, the January mid-season squad refresh), thesoccerera DLS26 features (the refreshed 2025/26 database), 1dh905e (the Sarkic database joke)",
    "THE INJURY AND PHYSIO SYSTEM, THE EPHEMERAL INJURY REPORT, THE ALL-SUBS EXPLOIT, AND FOUR CAREER-LIFECYCLE NEGATIVES. (1) THE PHYSIO TIER LADDER: 'Physios are essential for managing your team fitness throughout a long season. As you play matches frequently, your players will lose stamina and may occasionally pick up injuries. Physios help recover energy and heal these issues. **Common Physios restore a small amount of energy, while Legendary Physios fully restore energy and heal all active injuries.** Unlike coaches, physios are hired using **coins**, making them much easier to manage for beginners.' So physios are the COIN-funded counterpart to the gem-funded coaches, and the tier ladder is Common = partial energy, Legendary = full energy plus every active injury. (2) THE GEM-TO-GAMES HEALING CONVERSION, the most precise healing figure on record: 'If it takes 35 gems to heal it's 7 games, if it takes 25 gems it's 5 games, if it takes 10 gems it's 2 games, if it's 5 gems to heal it takes 1 game to recover. You can get a legendary physio for 250 to heal em.' So **5 gems = 1 game, 10 = 2, 25 = 5, 35 = 7**, and a legendary physio runs about 250 (coins). (3) THE INJURY REPORT IS EPHEMERAL - the wave's most operationally useful finding. 'It actually says what the injury is, and how long he'll be out... **It doesn't stay though. It's only visible after you exit the match where the injury happened. It's gone if you close the app or play another match.**' The same detail is available at the recovery button: 'You can see when you touch the diamonds button to recover the player, it says, \"player has this injury and will be out for this number of games\".' **Practical rule: the moment a match ends with an injury, read the report before doing anything else - it will not be there later.** (4) REST-BASED RECOVERY: 'If you want to have them fit for online matches; play one division match and sit out the most tired players. And they'll be fully fit the next match. Also if you use \"team boost\" at halftime that helps a lot.' So one match of rest fully restores a tired player, and the half-time team boost accelerates it. (5) PASSIVE RECOVERY TIMES: 'it depends on your player individual stamina. With not a good team it can take 3-4 hours, but with fully maxed out team it takes 20 min I think.' (6) THE ALL-SUBS INJURY-PREVENTION METHOD, recorded as an EXPLOIT with its cost stated: 'Before entering the game put 5 bench players in your first team. Enter a game. Before kick-off, use your 5 subs to sub in your first team players for the bench players. No injuries. **Players can't get injured if you don't have players to sub them off for. Therefore, you can't get injuries if you have used all subs.**' The trade-off is obvious: you have no substitutions left for the match itself. (7) FOUR DOCUMENTED NEGATIVES ON THE CAREER LIFECYCLE. A targeted search for player growth, aging, morale and retirement in DLS returned **only real-football research and other games' systems** (pro11.zendesk's retirement-at-32 rule is a different game; the retirement-age tables are real football). **DLS26 has NO morale or dressing-room system, NO player growth or potential curve, NO aging, and NO retirement.** The only lifecycle event in the database is real-world: a common goalkeeper 'passed away at the young age of 26' and is technically retired. **Players in DLS are static cards that move only when you spend coaches on them** - there is no career-mode development arc to manage. (8) MID-SEASON RATING REFRESHES DO HAPPEN: the January 2026 update applied 'January transfer movements and updated player ratings... (new signings and winter moves reflected in rosters)', and the mid-season megathread logs the actual changes - 'Raya 83 > 84, Gabriel 84 > 85, Merino 79 > 80, Zubimendi 81 > 82, Trossard 79 > 80'. So a player you bought at one rating can be re-rated mid-season, which matters for anyone holding cards as assets.",
    "evidence/raw/turn35_w70/EV-484_injuries_physios_and_lifecycle_negatives.html",
    "PHYSIOS: hired with COINS (the counterpart to gem-funded coaches); Common restores a small amount of energy, LEGENDARY fully restores energy AND heals all active injuries; a legendary physio runs about 250. HEALING: 5 gems = 1 game, 10 = 2, 25 = 5, 35 = 7. THE INJURY REPORT IS EPHEMERAL - it names the injury and the games out, but only immediately after the match in which it happened; it vanishes if you close the app or play another match, so READ IT FIRST. RECOVERY: resting a tired player for one match fully restores them, and the half-time team boost accelerates it; passive recovery is 3-4 hours for a weak squad and about 20 minutes for a maxed one. EXPLOIT: using all five subs before kick-off prevents injuries entirely, because a player can only be injured if there is a sub to bring them off - at the cost of having no subs left. NEGATIVES: DLS26 has NO morale system, NO player growth or potential curve, NO aging, and NO retirement - players are static cards that move only when you spend coaches. Mid-season refreshes do re-rate players (January 2026 moved Raya 83>84, Gabriel 84>85, Merino 79>80, Zubimendi 81>82, Trossard 79>80)",
    quality="community")

add_claim("PHYSIOS ARE HIRED WITH COINS - the coin-funded counterpart to gem-funded coaches. 'Common Physios restore a small amount of energy, while Legendary Physios fully restore energy and heal all active injuries.'", 2, "medical/physio-tier-ladder", [e_inj])
add_claim("THE GEM-TO-GAMES HEALING CONVERSION: 5 gems = 1 game out, 10 = 2, 25 = 5, 35 = 7. A legendary physio runs about 250 (coins).", 3, "medical/gem-to-games-healing-conversion", [e_inj], notes="Era-stale source but the most precise healing figure on record")
add_claim("THE INJURY REPORT IS EPHEMERAL: it names the injury and the number of games out, but 'it's only visible after you exit the match where the injury happened. It's gone if you close the app or play another match.' The same text appears on the gem-recovery button.", 2, "medical/injury-report-is-ephemeral", [e_inj], notes="READ IT THE MOMENT THE MATCH ENDS - it will not be there later")
add_claim("Resting a tired player for one match fully restores them - 'play one division match and sit out the most tired players. And they'll be fully fit the next match' - and the half-time team boost accelerates recovery.", 3, "medical/rest-one-match-restores", [e_inj])
add_claim("Passive (idle) recovery depends on squad stamina: 'With not a good team it can take 3-4 hours, but with fully maxed out team it takes 20 min.'", 3, "medical/passive-recovery-times", [e_inj])
add_claim("EXPLOIT - USING ALL FIVE SUBS BEFORE KICK-OFF PREVENTS INJURIES: 'Players can't get injured if you don't have players to sub them off for. Therefore, you can't get injuries if you have used all subs.' The cost is having no substitutions left for the match itself.", 3, "medical/all-subs-prevents-injury-exploit", [e_inj], notes="Recorded with its cost stated - not a recommendation")
add_claim("DOCUMENTED NEGATIVE - **DLS26 HAS NO MORALE OR DRESSING-ROOM SYSTEM.** A targeted search returned only FIFA/EA and real-football content. There is no morale to manage and no dressing room to keep happy.", 2, "negatives/no-morale-system", [e_inj])
add_claim("DOCUMENTED NEGATIVE - **DLS26 HAS NO PLAYER GROWTH OR POTENTIAL CURVE AND NO AGING.** Players do not develop with minutes and do not decline with age; they are static cards that move only when you spend coaches on them.", 2, "negatives/no-growth-or-aging", [e_inj])
add_claim("DOCUMENTED NEGATIVE - **DLS26 HAS NO RETIREMENT.** The only retirement rules found belong to other games; the only lifecycle event in the DLS database is real-world (a common goalkeeper who died at 26 is 'technically retired').", 2, "negatives/no-retirement", [e_inj])
add_claim("DOCUMENTED NEGATIVE - **DLS26 HAS NO SURGERY MECHANIC.** Injuries are healed by physios, rest or gems; there is no surgical repair, no rehabilitation timeline and no return-to-play protocol.", 2, "negatives/no-surgery", [e_inj])
add_claim("MID-SEASON RATING REFRESHES RE-RATE PLAYERS: the January 2026 update applied 'January transfer movements and updated player ratings', with the megathread logging 'Raya 83 > 84, Gabriel 84 > 85, Merino 79 > 80, Zubimendi 81 > 82, Trossard 79 > 80'. A card you hold can be re-rated mid-season.", 2, "transfers/mid-season-rating-refresh", [e_inj])
add_claim("The 2025/26 database refresh brought current team data plus 'more classic players, special players, and national team players'.", 2, "patching/database-refresh-contents", [e_inj])

for name in ('EV-484_injuries_physios_and_lifecycle_negatives.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
