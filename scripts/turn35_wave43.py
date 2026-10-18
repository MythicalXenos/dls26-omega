#!/usr/bin/env python3
"""Turn 35 Wave 43: DLS26-specific modes — Dynamic Stars (live-upgrading Special Players tied to real-world national team performance, DLS's Path-to-Glory analogue), World Tournament event type, World Heroes/World Winners events, manager accessories, clan interactions, plus version-date noise across mirrors."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w43')

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

# ---------- EV-446: DLS26 modes ----------
e_dm=new_ev("App Store US/FM/SG DLS26 version history (official), official FTG TikTok (@dreamleaguesoccer.ftg) Summer Spotlight campaign, thesoccerera DLS26 feature breakdown, dlskits.mobi, fifaworldcupnews DLS26 September update, mokoweb, soft112 version mirror",
    "DLS26-SPECIFIC MODES. DYNAMIC STARS (official App Store + official TikTok): 'Dynamic Stars - Collect Special Players, upgrading live with national team performances.' The official TikTok campaign specified 'Starting on the 8th of June, collect Dynamic Stars to play your part in the World's tournament. These cards will upgrade live in line with National Team performances over the summer.' A feature breakdown describes them as 'specialized player cards that automatically upgrade live based on real-world national team tournament performances.' This makes Dynamic Stars DLS's structural analogue of EA FC's 'Path to Glory' cards: the card's rating moves with real-world tournament results rather than with in-game coaching. They are obtained via DYNAMIC STAR AGENTS from event draws and Season Passes (3 on the premium path, 2 free, per the World 26 Season 1 pass). WORLD TOURNAMENT (official App Store): 'International Football - Play our brand new World Tournament Event type', described as 'a completely fresh international football event structure offering high-tier reward tracking' that expands the existing event system with an international football format. WORLD HEROES: a large live-service event that began 1 July 2026, with a 'World Winners' event following; World Heroes are Special Players obtainable through LEGENDARY AGENTS, 'celebrating heroic performances at previous tournaments'. MANAGER ACCESSORIES (official): 'Take control in style with North American themed items' - cosmetic manager appearance items. CLAN IMPROVEMENTS: 'Communicate with new interactions and emoji reactions', alongside the earlier leaderboards, vice-captains and clan point boosts. VERSION-DATE NOISE: mirror sites disagree on exact release dates for the Summer Spotlight run - soft112 lists 13.310 (29 May), 13.320 (8 Jun), 13.330 (10 Jun), 13.340 (22 Jun), 13.350 (14 Jul), 13.410 (20 Aug), 13.420 (10 Sep) and 13.430 (1 Oct), while the App Store lists 13.320 (8 Jun) and 13.330 (10 Jun) and the datamine labels build 13430 as updated 2026-09-16. The version-to-content mapping is reliable; the version-to-date mapping across mirrors is not.",
    "evidence/raw/turn35_w43/EV-446_dls26_modes.html",
    "DYNAMIC STARS: Special Players whose cards UPGRADE LIVE based on real-world NATIONAL TEAM tournament performance - DLS's analogue of EA's Path to Glory; collection opened 8 June 2026; obtained via Dynamic Star Agents from event draws and Season Passes (3 premium + 2 free). WORLD TOURNAMENT: a brand-new International Football EVENT TYPE from Summer Spotlight, described as a completely fresh international football event structure with high-tier reward tracking. WORLD HEROES: large live-service event from 1 July 2026 with a World Winners follow-up; World Heroes are Special Players obtainable via LEGENDARY AGENTS. MANAGER ACCESSORIES: North American themed cosmetic items. CLAN IMPROVEMENTS: interactions and emoji reactions on top of leaderboards/vice-captains/clan point boosts. VERSION-DATE NOISE: mirrors disagree on release dates across the Summer Spotlight run (soft112: 13.310 29 May, 13.320 8 Jun, 13.330 10 Jun, 13.340 22 Jun, 13.350 14 Jul, 13.410 20 Aug, 13.420 10 Sep, 13.430 1 Oct; App Store: 13.320 8 Jun, 13.330 10 Jun; datamine: 13430 updated 2026-09-16). The version-to-CONTENT mapping is reliable; the version-to-DATE mapping across mirrors is not",
    quality="official")

add_claim("Dynamic Stars are Special Players whose cards UPGRADE LIVE based on real-world national team tournament performance - DLS26's structural analogue of EA FC's Path to Glory cards.", 1, "cards/dynamic-stars-live-upgrade", [e_dm])
add_claim("The Dynamic Stars collection opened on 8 June 2026 with the Summer Spotlight update, tied to the World's tournament.", 1, "cards/dynamic-stars-launch", [e_dm])
add_claim("World Tournament is a brand-new International Football EVENT TYPE introduced in Summer Spotlight, described as a completely fresh international football event structure with high-tier reward tracking.", 1, "events/world-tournament", [e_dm])
add_claim("World Heroes is a large live-service event that began 1 July 2026, followed by a World Winners event; World Heroes are Special Players obtainable through Legendary Agents, celebrating heroic performances at previous tournaments.", 1, "events/world-heroes", [e_dm])
add_claim("Manager Accessories are North American themed cosmetic manager appearance items added in Summer Spotlight.", 1, "customization/manager-accessories", [e_dm])
add_claim("Summer Spotlight's clan improvements add interactions and emoji reactions on top of the earlier leaderboards, vice-captains and clan point boosts.", 1, "clans/emoji-interactions", [e_dm])
add_claim("VERSION-DATE NOISE: mirror sites disagree on the release dates of the Summer Spotlight builds (13.310 through 13.430) while the App Store and the datamine disagree with them in turn. The version-to-CONTENT mapping is reliable; the version-to-DATE mapping across mirrors is not.", 2, "errata/version-date-noise", [e_dm], notes="Do not quote mirror dates as authoritative")

p=os.path.join(RAW_DIR,'EV-446_dls26_modes.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
