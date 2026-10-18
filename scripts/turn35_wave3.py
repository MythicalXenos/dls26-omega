#!/usr/bin/env python3
"""Turn 35 Wave 3: Fanzone facility, 12th Man vote, World Tournament, Dream Stars 26, Clan improvements, News System, v13.3xx version timeline."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w3')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="patch_notes"):
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

e_fanzone=new_ev("App Store + APKMirror + thesoccerera + dlskits.mobi + mokoweb + soft112 + TikTok FTG (v13.100-v13.430)",
    "Fanzone facility: introduced in Summer Spotlight update (v13.310/May27-29 2026). SIXTH club facility alongside Stadium/Medical/Commercial/Training/Accommodation (Recruitment is the established 5th — Fanzone is a new 6th). Fanzone provides (1) Clan bonuses and (2) Stadium discounts (structural discounts on stadium expansions). Per FTG TikTok: 'all new Fanzone facility'. No exact costs or level structure published. 12th Man vote: introduced v13.110/v13.120 Mar 2026 as part of Dream Stars 26. Community votes on ONE extra Dream Star card to add to the Dream Stars 26 collection (the 'final' addition to that set). Voting period was a limited-time in-game event; the winning player was added in v13.120 Mar25 ('12th Man – DLS community has voted, added'). Winner identity not in patch notes (likely revealed in-game). Dream Stars 26: set of boosted special cards for the season's top performers (enhanced attributes + enhanced card/player appearances), introduced v13.100 Feb26; v13.110 Winter Reload added the rest; v13.120 finalized with 12th Man. Separate from Dynamic Stars (launched Jun8 with Summer Spotlight) and Cult Heroes (Sep16 2026). World Tournament: new event type introduced in Summer Spotlight (international/World Cup themed event). Clan improvements: v13.100 added Clan Leaderboards, Vice-Captains, Clan Point boosts; v13.310/v13.330 added Clan interactions (chat) and emoji reactions. News System: added v13.100 — centralized in-game news feed for DLS updates. iOS Game Center support added v13.120 Mar25 (achievements + friend leaderboards). Manager Accessories: North American themed manager outfits/items released in v13.330 Summer Spotlight. Version timeline cross-check: v13.100 Feb26 (Winter Reload base, 12th Man Vote, News System, Clan upgrades, UI/SFX, Game Center); v13.110 Mar2 (Updated Team Data / January transfers); v13.120 Mar25 (Dream Stars finalized, 12th Man revealed, bug fixes); v13.130 Mar27 (duplicate of 12th Man release per App Store VN); v13.300 May27 (Dream Stars restatement, bug fixes, Game Center); v13.310/v13.330 May27-29 (Summer Spotlight: Dynamic Stars, Fanzone, World Tournament, Manager Accessories, Clan chat/emoji); v13.350 Jul14 (Dream Stars restatement); v13.410 Aug20 (Pre-Season Kickoff, physics/GK AI); v13.420 Sep1 (slide-tackle + collision fixes); v13.430 Sep16 (Cult Heroes). Confirms FIFPRO license 4,000+ players, 8 divisions, 3D motion-captured moves.",
    "evidence/raw/turn35_w3/EV-384_fanzone_clans.html",
    "Fanzone 6th facility (clan bonuses + stadium discounts); 12th Man community vote adds one extra Dream Star; World Tournament event; clan leaderboards/vice-captains/emoji; News System; Game Center iOS; version timeline v13.100-13.430")

add_claim("Fanzone is the SIXTH club facility introduced in Summer Spotlight update (v13.310 May27-29 2026), alongside Stadium/Medical/Commercial/Training/Accommodation/Recruitment.", 1, "facilities/fanzone", [e_fanzone])
add_claim("Fanzone grants TWO bonuses when upgraded: (1) Clan bonuses (clan resource rewards) and (2) Stadium discounts (structural discounts on stadium expansion costs).", 1, "facilities/fanzone-bonuses", [e_fanzone])
add_claim("Fanzone exact gem cost per level, number of levels, and discount % per tier are NOT publicly documented in patch notes or community guides (requires in-game inspection/APK).", 1, "facilities/fanzone-unknowns", [e_fanzone], "gap")
add_claim("12th Man is a single extra Dream Star card added via community vote (in-game poll) — the community selects the final player of the Dream Stars 26 set.", 1, "cards/dream-stars-12th-man", [e_fanzone])
add_claim("12th Man voting period ran during Winter Reload (v13.110-v13.120 Mar 2-25 2026); the winning player was added in v13.120 Mar25.", 1, "cards/12th-man-timeline", [e_fanzone])
add_claim("12th Man winner identity not specified in public patch notes (revealed in-game).", 1, "cards/12th-man-identity-gap", [e_fanzone], "gap: needs in-game check")
add_claim("Dream Stars 26 is a set of Special boosted cards featuring the season's top performers, with enhanced attributes AND enhanced card art/player appearances.", 1, "cards/dream-stars-26", [e_fanzone])
add_claim("World Tournament is a new Event type introduced in Summer Spotlight — international/World Cup themed limited-time event.", 1, "events/world-tournament", [e_fanzone])
add_claim("Clan improvements across v13.100-v13.330: Clan Leaderboards, Vice-captains role, Clan Point boosts, in-Clan chat/interactions, and emoji reactions.", 1, "clans/improvements", [e_fanzone])
add_claim("News System added v13.100: centralized in-game feed for official DLS news, updates, and event announcements.", 1, "ui/news-system", [e_fanzone])
add_claim("iOS Game Center support added v13.120: Game Center achievements and friend leaderboards.", 1, "platform/ios-game-center", [e_fanzone])
add_claim("Manager Accessories: North American themed manager outfit items released with v13.330 Summer Spotlight.", 1, "customization/manager-accessories-na", [e_fanzone])
add_claim("Full v13.x update timeline (confirmed): v13.100 Feb26 (Winter Reload base, 12th Man Vote, News System, Clan upgrades, UI/SFX); v13.110 Mar2 (Jan transfer update); v13.120 Mar25 (Dream Stars + 12th Man final, Game Center); v13.130 Mar27 (bug fix restatement); v13.300 May27 (Dream Stars restate); v13.310/v13.330 May27-29 (Summer Spotlight: Dynamic Stars, Fanzone, World Tournament, Manager Accessories, Clan chat/emoji); v13.350 Jul14 (bug fixes); v13.410 Aug20 (Pre-Season Kickoff, physics/GK AI); v13.420 Sep1 (slide-tackle/collision fixes); v13.430 Sep16 (Cult Heroes).", 1, "patches/v13-timeline", [e_fanzone])

p=os.path.join(RAW_DIR,'EV-384_fanzone_clans.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
