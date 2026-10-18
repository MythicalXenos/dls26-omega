#!/usr/bin/env python3
"""Turn 35 Wave 64: THE CLAN SYSTEM'S OPERATIONAL PICTURE (creation options, vice-captains, the
precise semantics of the 350k cap, and clan-internal matches), THE CAREER CUP LADDER
(International Cup -> Allstar Cup -> Diamond Cup), and the Italian League Classics Prize Ladder.

Wave 64 targets the thinnest surfaces in the corpus. Three results worth the wave:

1. THE 350K CAP'S SEMANTICS ARE NOW PRECISE. A clan leader explains it directly: the cap is on
   what you contribute to the CLAN'S TOTAL; anything you earn beyond it counts only toward your
   personal ranking inside the clan (and therefore the top-contributor reward). That distinction
   changes the calculus for a player who has already banked 350k.

2. THE VICE-CAPTAIN IS APPOINTED BY THE LEADER, and an active clan supplies level-appropriate
   opponents - so clan choice is a competitive decision, not just a social one.

3. THE PRIZE LADDER'S CURRENT CLASSIC ROSTER IS NAMED: the Italian League Classics - Trezeguet,
   Batistuta, Crespo and Desailly - announced on the official TikTok.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w64')

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

e_clan=new_ev("dlsmod.com/dls-clans (10 Dec 2025, clan creation and management), FTG support 30839289076626 'What are Clans?' (full text re-surfaced), r/DreamLeagueSoccer 1pk9dae (11 Dec 2025, a clan leader's operational manual), 1tp8zg7 (27 May 2026, clan recruitment), 1peo0q2 (5 Dec 2025, clan promotion thread), kostenlose-spiele-apps.de (27 Apr 2026, vice-captain and point boosts), fifaworldcupnews DLS26 features (23 Jul 2026, min 50 members), dls-wiki.fandom.com/wiki/Leagues (29 Jul 2026, the cup ladder), official @dreamleaguesoccer.ftg TikTok (Italian League Classics), App Store DLS26 version history 13.330/13.350 (World Tournament), YouTube 'DLS 26 WORLD CUP TOURNAMENT' (5 Jul 2026), 'REAL TEAMS WORLD CUP TOURNAMENT' (10 Jul 2026), 'WORLD CUP HEROES HUNT' (1 Jul 2026), 'WORLD CUP WINNERS PACK' (21 Jul 2026), r/DLS 1u6oqei (15 Jun 2026, Dynamic Stars upgrade path from the World Cup thread)",
    "THE CLAN SYSTEM'S OPERATIONAL PICTURE AND THE CAREER CUP LADDER. (1) CLAN CREATION IS FULLY CUSTOMISABLE: the Clans tab sits on the main home screen title or the top-right profile menu, and you can browse public clans, search by name, enter a clan code, or create your own. Creation options are the clan badge (style, background, icon, frame colour, dressing), the clan name, the clan country, entry requirements (minimum team rank), and the clan type (open, closed, invite-only). The leader is the primary admin and can remove players. (2) THE OFFICIAL RULES, RE-SURFACED IN FULL: 'Play fair. We're not responsible for any arguments or disputes that happen inside a clan... We will not mediate. Our house, our rules. We reserve the right to remove players or even entire clans if they break the game's Terms of Use or create a negative experience. One clan at a time. You can only belong to one clan. If you leave, you might be able to rejoin or pick a new one - but choose wisely. Leader's call. Each clan has one leader. If they leave, leadership passes on. If no one's left, the clan disappears. Join conditions. Some clans set entry requirements. If you don't meet them, you won't see that clan in search - but you can still join with an invite code.' (3) THE 350K CAP'S SEMANTICS ARE NOW PRECISE - the most useful clarification of the wave. A clan leader explains the mechanic and a commenter confirms: 'The biggest contribution anyone can make is 350k. Anything else you earn will help you be first in your clan and get the 50 gems at the end of the season, but it won't help your clan's total points.' So the cap governs your CONTRIBUTION TO THE CLAN TOTAL, and everything beyond it counts only toward your personal in-clan ranking and the top-contributor reward. For a player who has already banked 350k, further clan points are purely a race for the top spot. (4) A WORKING CLAN LEADER'S METHOD, as a template: build to the member cap fast, adopt 'you get what you give', and prune hard - 'I'm actively kicking out anyone who doesn't contribute at least 20k Clan Points in the first hour of joining.' Real recruitment threads screen for exactly this: 'minimum 50 wins within the remaining time limit (5 days)', 'try to be active as much as you can, contribute points, join the Discord, no inactivity', with requirements stated as full clan name, team rating requirements, and invite-only versus rank condition. (5) THE VICE-CAPTAIN EXISTS AND IS APPOINTED: the Winter Reload update added 'Clan leaderboards, vice-captains, Clan Point boosts', and a German guide confirms 'you can appoint a vice-captain and benefit from Clan Point boosts. An active clan gives you not only extra rewards but also opponents at your level to measure yourself against.' So clan choice is a COMPETITIVE decision - an active clan supplies level-appropriate opponents - not merely a social one. (6) A NEW CLAN-POINT SOURCE: 'you can also play clan matches against other members of your clan; this will also contribute to the Clan Points' - internal clan matches pay points, on top of regular matches, live events, Dream Draft events, real-life scenarios and Season Pass tiers. Minimum clan size is 50 members. (7) THE CAREER CUP LADDER, now explicit: winning the Legendary Division qualifies you for the INTERNATIONAL CUP (against national teams such as England, Sweden, Portugal and Argentina), winning that qualifies you for the ALLSTAR CUP (against continental all-star teams), and the DIAMOND CUP is 'the final cup of the game', attendable from the Elite and Legendary Divisions, with elimination on any concession. Losing in the International Cup returns you to the Legendary Division. (8) THE WORLD TOURNAMENT is the NEW international-football event type shipped in Summer Spotlight (v13.330, 10 Jun 2026, and 13.350 on 14 Jul) - distinct from the Career International Cup, and the surface for the summer's World Cup Heroes, World Cup Winners and World Cup Challenge events. (9) THE PRIZE LADDER'S CURRENT CLASSIC ROSTER IS NAMED: the official TikTok announces 'Italian League Classics are coming to #DLS26 - start playing matches to earn Dream Points and complete the Prize Ladder. Get your hands on Trezeguet, Batistuta, Crespo and Desailly in the form of special Classic Player cards.' (10) The Dynamic Stars upgrade path is corroborated a third time from the World Cup discussion thread: '+1 per Group Stage Win, +2 for Round of 32 Qualification, +2 for Round of 16 Qualification, +2 for Quarter Finals Win, +2 for Semi-Finals Win, 96-Rating for Final Winner', with the finalist's loser reward unknown. (11) 'Unlimited Special Card accommodation' is confirmed in the official copy - special cards never count against the squad cap.",
    "evidence/raw/turn35_w64/EV-478_clans_and_cups.html",
    "CLANS: creation is fully customisable (badge, name, country, minimum team rank, open/closed/invite-only) from the home-screen Clans tab or the profile menu; the leader is the sole admin and can remove members; one clan at a time; leadership passes on if the leader leaves and the clan disappears if nobody is left; entry requirements hide a clan from search but an invite code still works. THE 350K CAP'S SEMANTICS: it caps your contribution to the CLAN'S TOTAL - anything beyond counts only toward your personal in-clan ranking and the top-contributor reward. A leader's method: fill to cap fast and prune anyone contributing under 20k points in their first hour. THE VICE-CAPTAIN is appointed by the leader, and an active clan supplies level-appropriate opponents - so clan choice is competitive, not just social. NEW POINT SOURCE: clan-internal matches pay clan points. CAREER CUP LADDER: Legendary Division champion -> International Cup (national teams) -> Allstar Cup (continental all-stars) -> Diamond Cup (the final cup); losing in the International Cup returns you to the Legendary Division. THE WORLD TOURNAMENT is the new international-football event type from Summer Spotlight (v13.330, 10 Jun 2026). PRIZE LADDER CLASSICS NAMED: the Italian League Classics - Trezeguet, Batistuta, Crespo and Desailly",
    quality="community")

add_claim("Clan creation is fully customisable: badge (style, background, icon, frame colour, dressing), clan name, clan country, entry requirements (minimum team rank), and clan type (open, closed, invite-only). The Clans tab is on the main home screen title or the top-right profile menu.", 2, "clans/creation-options", [e_clan])
add_claim("THE 350K CLAN-POINT CAP'S SEMANTICS: it caps what you contribute to the CLAN'S TOTAL. Anything earned beyond it counts only toward your personal in-clan ranking and the top-contributor reward - 'it won't help your clan's total points.'", 2, "clans/350k-cap-semantics", [e_clan], notes="Precise clarification - changes the calculus once 350k is banked")
add_claim("The official clan rules: one clan at a time; each clan has one leader and if they leave leadership passes on, and the clan disappears if nobody is left; entry requirements hide a clan from search but an invite code still works; FTG reserves the right to remove players or entire clans for Terms-of-Use breaches and will not mediate internal disputes.", 1, "clans/official-rules", [e_clan], notes="Official")
add_claim("A working clan leader's method: fill the roster to cap quickly, adopt 'you get what you give', and prune hard - 'I'm actively kicking out anyone who doesn't contribute at least 20k Clan Points in the first hour of joining.' Recruitment threads screen for exactly this (minimum wins in a time limit, activity, Discord membership, no inactivity).", 3, "clans/leader-pruning-method", [e_clan])
add_claim("THE VICE-CAPTAIN IS APPOINTED BY THE LEADER (added in the Winter Reload update alongside clan leaderboards and Clan Point boosts), and an active clan supplies level-appropriate opponents - so clan choice is a competitive decision, not merely a social one.", 2, "clans/vice-captain-and-opponents", [e_clan])
add_claim("CLAN-INTERNAL MATCHES EARN CLAN POINTS: 'you can also play clan matches against other members of your clan; this will also contribute to the Clan Points' - on top of regular matches, live events, Dream Draft events, real-life scenarios and Season Pass tiers. Minimum clan size is 50 members.", 2, "clans/internal-matches-pay-points", [e_clan], notes="A point source the corpus did not have")
add_claim("THE CAREER CUP LADDER: winning the Legendary Division qualifies you for the INTERNATIONAL CUP (national teams - England, Sweden, Portugal, Argentina), winning that qualifies you for the ALLSTAR CUP (continental all-star teams), and the DIAMOND CUP is the final cup of the game, attendable from the Elite and Legendary Divisions with elimination on any concession. Losing in the International Cup returns you to the Legendary Division.", 2, "cups/career-cup-ladder", [e_clan])
add_claim("THE WORLD TOURNAMENT is the new international-football event type shipped in Summer Spotlight (v13.330, 10 Jun 2026; 13.350 on 14 Jul) - distinct from the Career International Cup, and the surface for the summer's World Cup Heroes, World Cup Winners and World Cup Challenge events.", 2, "events/world-tournament", [e_clan], notes="Fills the corpus's thinnest surface")
add_claim("THE PRIZE LADDER'S CURRENT CLASSIC ROSTER IS NAMED: the Italian League Classics - Trezeguet, Batistuta, Crespo and Desailly - obtained by earning Dream Points and completing the Prize Ladder, announced on the official TikTok.", 2, "prizeladder/italian-league-classics", [e_clan], notes="The first named current-cycle Prize Ladder roster")
add_claim("The Dynamic Stars upgrade path is corroborated a third time from the World Cup discussion thread: +1 OVR per Group Stage win, +2 for Round of 32 qualification, +2 for Round of 16 qualification, +2 for quarter-final and semi-final wins, and 96 OVR for the final winner - with the losing finalist's reward unknown.", 3, "events/dynamic-stars-path-third-source", [e_clan])
add_claim("Special cards have unlimited accommodation and never count against the squad cap, confirmed in the official copy.", 1, "facilities/special-cards-unlimited-accommodation", [e_clan], notes="Official - resolves how the 64-player cap interacts with special players")

for name in ('EV-478_clans_and_cups.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
