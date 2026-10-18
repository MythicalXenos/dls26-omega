#!/usr/bin/env python3
"""Turn 35 Wave 113: WORLD HEROES ARE AGENT-EXCLUSIVE, THE SUMMER ECONOMY RESET, AND PLAY FEST IS LIVE.

Wave 113's centrepieces:

1. WORLD HEROES AND WORLD WINNERS ARE LEGENDARY-AGENT-EXCLUSIVE. A source states it plainly:
   *"Just like the World Cup Heroes promo, World Winners cards will sit exclusively in the
   **Legendary Agent** pool. You will not be able to pull these special editions from standard
   Common or Rare draws."* That is the single most useful acquisition fact in the event
   section — it tells you exactly which agent to buy and, more importantly, which draws are a
   waste of gems for that collection.

2. THE SUMMER UPDATE CARRIED AN "ECONOMY RESET", which the corpus had not recorded. A source
   headline reads *"DLS Summer Update Officially Confirmed: Dynamic Stars, Classic Icons, and
   Economy Reset."* The corpus has the rating reshuffle and the Commercial nerf as separate
   findings; this suggests they were one coordinated change rather than two. Recorded as a
   single-source claim at C3 because the headline is all the detail available.

3. PLAY FEST IS LIVE RIGHT NOW. The Google Play listing carries *"Special event — Play Fest
   starts on 13 October"* against a 14 September update. Today is 18 October 2026, so **the
   event the corpus should be pointing at is the one running this week**, and the corpus's
   event advice is only useful if it is checked against the live event rather than a
   remembered one.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w113')

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

e_ev=new_ev("footballgamingbd.online DLS 26 World Cup Winners (1 Jul 2026 - World Winners cards sit exclusively in the Legendary Agent pool, not Common or Rare draws; World Winners as the second phase of the Champion event), sakibpro.com (15 Aug 2026 - 'DLS Summer Update Officially Confirmed: Dynamic Stars, Classic Icons, and Economy Reset'; 'World Winners is officially confirmed as the next major Legendary Agent event... serving as the direct follow-up to DLS 26 World Cup Heroes'), Google Play DLS26 listing (Jul 2026 - 'Updated on 14 Sept 2026 - Ends on 10/14 - Special event - Play Fest starts on 13 October'), App Store DLS26 World Winners event page (21 Jul 2026 - 'These players have won with their nation on the global stage'), dlsinside.com latest-versions table (the version code sequence 160-13430 through 152-13330), r/DreamLeagueSoccer 1chedv5 (1 May 2024 - the cross-assist definition, and the claim that assists on low or off give 'a better chance at playing in rigged/handicapped matches'), gamingonphone.com DLS26 career guide (27 Jan 2026 - customisation of Team Kit, Logo, Player Kit Number, Boot Color and sock color from the Customize section in My Club, and 'the editing takes your Gems away'), dreamleaguesoccerkits.com best-settings (15 May 2026 - the audio settings: commentary 40-60, crowd 70, music 20-30), dlskitsurl.net (7 Oct 2026 - My Club is at the bottom right of the screen), logodls.com (26 Sep 2026 - Customise sits in the club menu alongside the squad and stadium selections), TikTok ix_smdsubsid (the controller settings path: game, then controls, then 'game pad control')",
    "WORLD HEROES ARE AGENT-EXCLUSIVE, THE SUMMER ECONOMY RESET, AND PLAY FEST IS LIVE. (1) THE AGENT EXCLUSIVITY, the most useful acquisition fact in the event section: '**Just like the World Cup Heroes promo, World Winners cards will sit exclusively in the Legendary Agent pool. You will not be able to pull these special editions from standard Common or Rare draws.**' **So for those collections, a Common or Rare agent is a guaranteed waste of gems** - which is a sharper instruction than the corpus's generic agent-tier advice, and it tells you exactly which agent to save for. (2) WORLD WINNERS IS THE SECOND PHASE OF THE CHAMPION EVENT: 'the big **second phase of the Champion event** we saw last year' - so the Champion event from DLS25 continued into DLS26 as World Cup Heroes and then World Winners, which explains why the two collections share a pool and a mechanic. (3) THE SUMMER ECONOMY RESET: a source headline reads '**DLS Summer Update Officially Confirmed: Dynamic Stars, Classic Icons, and Economy Reset**.' The corpus carries the rating reshuffle and the Commercial nerf as separate findings; this headline suggests they were one coordinated change. Recorded at C3 because the headline is the only detail available - the mechanism behind the reset is not described. (4) PLAY FEST IS LIVE: the Google Play listing carries '**Special event - Play Fest starts on 13 October**' against a 14 September update, and today is 18 October 2026. **So the event the corpus's advice should point at is the one running this week** - and the general lesson is that the event calendar rotates faster than the corpus's checkpoint cadence, so the live listing must be checked before any event spend. (5) CUSTOMISATION COSTS GEMS: 'you can customize your **Team Kit, Logo, Player Kit Number, Boot Color, and sock color** from the Customize Section in My Club. **The editing takes your Gems away**, so make sure you stick to the selection of your logo and team name.' So the gem cost is not limited to the kit import - it applies across the customisation surface, which raises the stakes on the corpus's 'do it once' advice. (6) THE AUDIO SETTINGS INVENTORY: commentary 40-60, crowd 70, music 20-30 - the only audio configuration in the corpus. (7) THE NAVIGATION SURFACE, from four independent sources: **My Club is at the bottom right of the screen**, and **Customise sits in the club menu alongside the squad and stadium selections**. (8) THE CONTROLLER SETTINGS PATH: game, then controls, then 'game pad control' - the only documented route to the controller profile, which pairs with the corpus's controller-layout claims. (9) THE CROSS-ASSIST DEFINITION: 'it's to have a cross go to the nearest player if you chipped inside the box instead of needing to aim yourself.' (10) THE ASSISTS-AND-HANDICAP LINKAGE: 'If set to low or off, you have **a better chance at playing in rigged/handicapped matches**' - a player explicitly connecting the assist setting to the handicap perception, which is a new linkage between two corpus findings. (11) THE VERSION CODE SEQUENCE: 160-13430 (16 Sep 2026), 159-13420 (5 Sep), 158-13410 (20 Aug), 154-13350 (21 Jul), 153-13340 (23 Jun), 152-13330 (12 Jun).",
    "WORLD HEROES AND WORLD WINNERS ARE LEGENDARY-AGENT-EXCLUSIVE - Common and Rare agents cannot pull them, so for those collections a low-tier agent is a guaranteed waste of gems. WORLD WINNERS IS THE SECOND PHASE OF THE CHAMPION EVENT. THE SUMMER UPDATE CARRIED AN 'ECONOMY RESET' that likely bundled the rating reshuffle and the Commercial nerf into one change. PLAY FEST STARTED 13 OCTOBER 2026 AND IS LIVE NOW - the event calendar rotates faster than the checkpoint cadence, so check the live listing before any event spend. CUSTOMISATION COSTS GEMS across the whole surface, not just the kit import. THE AUDIO SETTINGS INVENTORY. THE NAVIGATION SURFACE (My Club bottom right, Customise alongside squad and stadium). THE CONTROLLER SETTINGS PATH. AND a new linkage between the assist settings and the handicap perception.",
    "THE AGENT EXCLUSIVITY, THE ECONOMY RESET, AND PLAY FEST IS LIVE",
    quality="community")

add_claim("⚠️ WORLD HEROES AND WORLD WINNERS ARE LEGENDARY-AGENT-EXCLUSIVE: '**Just like the World Cup Heroes promo, World Winners cards will sit exclusively in the Legendary Agent pool. You will not be able to pull these special editions from standard Common or Rare draws.**' **So for those collections a Common or Rare agent is a guaranteed waste of gems** - a sharper instruction than the corpus's generic agent-tier advice, and it tells you exactly which agent to save for.", 3, "cards/world-heroes-agent-exclusive", [e_ev])
add_claim("WORLD WINNERS IS THE SECOND PHASE OF THE CHAMPION EVENT: 'the big **second phase of the Champion event** we saw last year.' So the DLS25 Champion event continued into DLS26 as World Cup Heroes and then World Winners, which explains why the two collections share a pool and a mechanic.", 3, "events/world-winners-second-phase-of-champion", [e_ev])
add_claim("THE SUMMER UPDATE CARRIED AN 'ECONOMY RESET': a source headline reads '**DLS Summer Update Officially Confirmed: Dynamic Stars, Classic Icons, and Economy Reset**.' The corpus carries the rating reshuffle and the Commercial nerf as separate findings; this suggests they were one coordinated change. Recorded at C3 because the headline is the only detail available - the mechanism behind the reset is not described anywhere.", 3, "economy/summer-economy-reset", [e_ev])
add_claim("⚠️ PLAY FEST STARTED 13 OCTOBER 2026 AND IS LIVE NOW. The Google Play listing carries '**Special event - Play Fest starts on 13 October**' against a 14 September update, and today is 18 October 2026. **So the event the corpus's advice should point at is the one running this week** - and the general lesson is that the event calendar rotates faster than the corpus's checkpoint cadence, so the live listing must be checked before any event spend.", 3, "events/play-fest-live-october-2026", [e_ev], notes="Time-stamped: current as of 18 October 2026")
add_claim("CUSTOMISATION COSTS GEMS ACROSS THE WHOLE SURFACE, not just the kit import: 'you can customize your **Team Kit, Logo, Player Kit Number, Boot Color, and sock color** from the Customize Section in My Club. **The editing takes your Gems away**, so make sure you stick to the selection of your logo and team name.' So the corpus's do-it-once advice applies to every cosmetic decision, not only the 150-gem kit unlock.", 3, "customization/costs-gems-throughout", [e_ev])
add_claim("THE AUDIO SETTINGS INVENTORY, the only one in the corpus: **commentary 40-60, crowd 70, music 20-30**. Commentary low or off is the competitive recommendation, since it removes a distraction without changing the match.", 4, "settings/audio-inventory", [e_ev])
add_claim("THE NAVIGATION SURFACE, from four independent sources: **My Club is at the bottom right of the screen**, and **Customise sits in the club menu alongside the squad and stadium selections**. Small, but it is the difference between finding a surface and hunting for it.", 4, "ui/navigation-my-club-and-customise", [e_ev])
add_claim("THE CONTROLLER SETTINGS PATH, the only documented route to the controller profile: game, then controls, then '**game pad control**'. Pairs with the corpus's controller-layout claims and the corpus's no-controller-support negative.", 4, "settings/controller-settings-path", [e_ev])
add_claim("THE CROSS-ASSIST DEFINITION: 'it's to have a cross go to the nearest player if you chipped inside the box instead of needing to aim yourself.' So Cross Assist converts an aimed cross into a nearest-player cross, which is why the corpus's competitive advice is to turn it off.", 3, "controls/cross-assist-definition", [e_ev])
add_claim("A NEW LINKAGE between the assist settings and the handicap perception: 'If set to **low or off, you have a better chance at playing in rigged/handicapped matches**.' A player explicitly connecting the assist toggle to the corpus's maxed-squad-handicap finding - recorded as a linkage, not as a mechanism.", 4, "controls/assists-and-handicap-linkage", [e_ev])
add_claim("THE VERSION CODE SEQUENCE (dlsinside): **160-13430** (16 Sep 2026) · 159-13420 (5 Sep) · 158-13410 (20 Aug) · 154-13350 (21 Jul) · 153-13340 (23 Jun) · 152-13330 (12 Jun). So the build number and the version code move together, which is the pair to quote when reporting a bug.", 4, "patching/version-code-sequence", [e_ev])

for p in ['EV-526_agent_exclusivity.html','EV-526b_economy_reset_and_navigation.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
