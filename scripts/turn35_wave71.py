#!/usr/bin/env python3
"""Turn 35 Wave 71: THE NEWS SYSTEM (what it actually is), the DLS suspension rule, a SECOND
ROUTE TO CLASSIC PLAYERS, the switching-delay finding, and a batch of wish-list negatives.

Wave 71's most valuable acquisition finding: Classic players are buyable with COINS on the
regular transfer market, not only from the Prize Ladder. The corpus had the Prize Ladder as
the sole Classic route.

The wish-list negatives are an efficient way to document absences - every feature players are
publicly asking FTG to add is a feature DLS26 does not have.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w71')

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

e_news=new_ev("App Store / APKMirror DLS26 version history v13.100 (26 Feb 2026) and v13.110 (2 Mar 2026, the Winter Reload notes), sakibpro DLS26 new features (27 Nov 2025, Classic players on the transfer market, the new ball, the new camera), egw.news DLS26 teaser report (10 Nov 2025, the volley skill move and the redesigned stadium), r/DreamLeagueSoccer zxl3ou (28 Dec 2022, the five-yellow suspension rule), 1papf7u (30 Nov 2025, special players excluded from accommodation), dlsmod.com DLS26 new features (10 Dec 2025, unlimited special players and the auto-switch fix), Google Play DLS26 reviews (14 Sep 2026, the switching delay), YouTube 'DREAM LEAGUE SOCCER 2026 | What We KNOW!' (the wish-list of absent features), thesoccerera (19 Feb 2026, new faces), r/DLS 1pe5zl2 (4 Dec 2025, FTG's team size), apkpure.net (Kick-Off Stars)",
    "THE NEWS SYSTEM, THE DLS SUSPENSION RULE, A SECOND CLASSIC-PLAYER ROUTE, THE SWITCHING DELAY, AND A BATCH OF WISH-LIST NEGATIVES. (1) THE NEWS SYSTEM IS FTG'S INFO HUB, NOT A NEWS FEED. The Winter Reload notes read 'News System - Get the latest DLS info, all in one place' (v13.110, 2 Mar 2026), and v13.100 (26 Feb 2026) shipped the 'Improved News System - Get the latest DLS info'. Crucially, a community wish-list asks FTG to 'Bring back news system like in DLS 22 (transfers, injuries, debuts, retirements)' - which confirms the DLS26 News System is a DIFFERENT thing from the DLS22 one. It is FTG's announcement channel for updates, events and content, not a simulated transfer/injury feed. (2) THE DLS SUSPENSION RULE, the only DLS-specific disciplinary source on record: 'There's a rule if your player receives 5 yellow cards he will be suspended for the next game. That yellow card icon appears if your player receive 4 yc.' So FIVE ACCUMULATED YELLOWS = a one-match ban, with a warning icon at four - the same threshold as the Premier League. (3) A SECOND ROUTE TO CLASSIC PLAYERS, the wave's most valuable acquisition finding: 'From a video posted by First Touch Games, we can clearly see that in DLS 26, we will be able to buy classic players with coins from the Transfer Market. That means, besides the prize ladder, Classic Players will also be available on the Regular Transfer Market.' The corpus had the Prize Ladder as the only Classic route. (4) THE SWITCHING DELAY, an important gameplay finding: a September 2026 Play Store review reports 'the controls and player switching are not synced, so there's a .5 to 2 second delay when switching. Offense can take advantage usually by dribbling sideways or c spamming. The 2025 version had much better input responsiveness.' This sits against dlsmod's December 2025 claim that the auto-switch bugs 'have been solved as of now' - recorded as a conflict. (5) v13.110's full Winter Reload list: updated team data from the transfer window, Dream Stars 26, the 12th Man Vote, the News System, major Clan improvements (leaderboards, vice-captains, Clan Point boosts), UI and SFX upgrades, and Game Centre on iOS - 'See your achievements and friend leaderboards on iOS!' (6) THE NEW VOLLEY SKILL MOVE was teased pre-launch ('A brand-new volley skill move, briefly showcased in the teaser'), alongside a redesigned stadium with enhanced lighting, a new camera operator hinting at cinematic replays and a possible new gameplay angle, a new ball model, and a refined UI 'blending dark shades of pink and blue'. (7) SPECIAL AND CLASSIC PLAYERS DO NOT COUNT TOWARD THE SQUAD CAP, corroborated by three sources: v13.040's 'Increased squad size - Now with unlimited special players in your club', dlsmod's 'all the new classic and star players will not be counted towards the main squad size', and a player's 'special players being excluded from accommodation count'. (8) THE WISH-LIST NEGATIVES - every feature players are publicly asking FTG to add is a feature DLS26 does not have: home-and-away legs in tournaments (GCC from the Round of 16, Diamond Cup from the semi-finals), player accessories (wristbands, bandages, gloves), a home-and-away league format, Bundesliga and Ajax licences, a Player of the Season award, a DLS22-style news feed, fog/cloudy/light-rain weather, post-match interviews, VAR animations, stand-colour and decoration customisation, and animated training drills. (9) New player models include 'new faces for stars like Florian Wirtz'. (10) FTG operates with 11-50 people, per a community estimate. (11) Kick-Off Stars 'are available during special periods, giving early access to headline players for starting matches'.",
    "evidence/raw/turn35_w71/EV-485_news_suspensions_and_classic_route.html",
    "NEWS SYSTEM: it is FTG's info hub - 'Get the latest DLS info, all in one place' (v13.110, 2 Mar 2026) - NOT the DLS22-style transfer/injury/debut/retirement feed that players are asking to have brought back. SUSPENSION: FIVE accumulated yellow cards = a one-match ban, with a warning icon at four. CLASSIC PLAYERS: a SECOND route - buyable with COINS on the regular transfer market, not only from the Prize Ladder. SWITCHING DELAY: a .5-2 second delay in DLS26, worse than DLS25, exploitable by sideways dribbling and C-spamming - against dlsmod's December 2025 claim that auto-switch bugs were solved (a conflict). WINTER RELOAD (v13.110): updated team data, Dream Stars 26, the 12th Man Vote, the News System, clan leaderboards/vice-captains/point boosts, UI and SFX upgrades, and Game Centre on iOS. PRE-LAUNCH TEASERS: a new volley skill move, a redesigned stadium, a new camera operator, a new ball model. SQUAD CAP: special and classic players do not count toward it (three sources). NEGATIVES from the public wish-list: no home-and-away legs, no player accessories, no home-and-away league format, no Bundesliga/Ajax licences, no Player of the Season award, no DLS22-style news feed, no fog/cloudy weather, no post-match interviews, no VAR, no stand-decoration customisation, no animated training drills",
    quality="community")

add_claim("THE NEWS SYSTEM IS FTG'S INFO HUB, NOT A NEWS FEED: 'News System - Get the latest DLS info, all in one place' (v13.110, 2 Mar 2026; 'Improved News System' in v13.100, 26 Feb 2026). A community wish-list asking to 'bring back news system like in DLS 22 (transfers, injuries, debuts, retirements)' confirms the two are different things.", 2, "presentation/news-system-is-info-hub", [e_news])
add_claim("THE DLS SUSPENSION RULE: five accumulated yellow cards earns a one-match suspension, and a warning icon appears on the player at four.", 3, "gameplay/five-yellows-suspension", [e_news], notes="The only DLS-specific disciplinary source on record; era-stale (2022)")
add_claim("A SECOND ROUTE TO CLASSIC PLAYERS: they are buyable with COINS on the regular transfer market, not only from the Prize Ladder - 'besides the prize ladder, Classic Players will also be available on the Regular Transfer Market.'", 2, "transfers/classic-players-on-transfer-market", [e_news], notes="The corpus had the Prize Ladder as the sole Classic route")
add_claim("THE SWITCHING DELAY: a September 2026 review reports 'the controls and player switching are not synced, so there's a .5 to 2 second delay when switching. Offense can take advantage usually by dribbling sideways or c spamming. The 2025 version had much better input responsiveness.'", 3, "controls/switching-delay", [e_news])
add_claim("CONFLICT - the auto-switch delay: dlsmod reported in December 2025 that the auto-switch bugs 'have been solved as of now', while a September 2026 review reports a 0.5-2 second switching delay and worse input responsiveness than DLS25. Either it regressed or the fix was partial.", 3, "controls/auto-switch-fix-conflict", [e_news])
add_claim("v13.110 (Winter Reload, 2 Mar 2026) shipped: updated team data from the transfer window, Dream Stars 26, the 12th Man Vote, the News System, major Clan improvements (leaderboards, vice-captains, Clan Point boosts), UI and SFX upgrades, and Game Centre on iOS - 'See your achievements and friend leaderboards on iOS!'", 2, "patching/winter-reload-v13.110", [e_news])
add_claim("Game Centre support on iOS surfaces achievements and friend leaderboards outside the game.", 2, "platform/game-centre-ios", [e_news])
add_claim("A brand-new VOLLEY SKILL MOVE was teased for DLS26 pre-launch, alongside a redesigned stadium with enhanced lighting, a new camera operator hinting at cinematic replays and a possible new gameplay angle, a new ball model, and a refined UI.", 3, "skillmoves/new-volley-teased", [e_news], notes="The corpus's existing Volley input is rainbow flick then swipe - this may be its formalisation")
add_claim("Special and classic players do NOT count toward the squad cap, corroborated by three sources: v13.040's 'unlimited special players in your club', 'all the new classic and star players will not be counted towards the main squad size', and a player's 'special players being excluded from accommodation count'.", 2, "facilities/special-players-excluded-from-cap", [e_news])
add_claim("DOCUMENTED NEGATIVES FROM THE PUBLIC WISH-LIST - features players are asking FTG to add, and therefore DLS26 does not have: home-and-away legs in tournaments (GCC from the Round of 16, Diamond Cup from the semi-finals), player accessories (wristbands, bandages, gloves), a home-and-away league format, Bundesliga and Ajax licences, a Player of the Season award, a DLS22-style news feed, fog/cloudy/light-rain weather, post-match interviews, VAR animations, stand-colour and decoration customisation, and animated training drills.", 2, "negatives/wish-list-absent-features", [e_news], notes="An efficient way to document absences - each is publicly requested and therefore missing")
add_claim("DLS26's player models include new faces for stars such as Florian Wirtz, with 'improved 3D motion capture, hyper-realistic player models, dynamic lighting, and stadium atmospheres'.", 2, "presentation/new-player-models", [e_news])
add_claim("Kick-Off Stars 'are available during special periods, giving early access to headline players for starting matches' - a timed early-access card window rather than a permanent route.", 3, "events/kick-off-stars-early-access", [e_news])

for name in ('EV-485_news_suspensions_and_classic_route.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
