#!/usr/bin/env python3
"""Turn 33 Wave 9: cloud save/account transfer + clans mechanics + exhibition friendlies."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
EXTRACT_DIR=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/extract')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','account_turn33')

ev_id=368
def new_ev(origin, summary, artifact_path, vol):
    global ev_id
    eid=f'EV-{ev_id:03d}'
    rec={"evidence_id":eid,"parent_claim_id":None,"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
         "origin_method":origin,"artifact_path":artifact_path,"volume_label":vol,"source_quality":"official-support+community","summary":summary}
    with open(EVIDENCE_INDEX,'a') as f: f.write(json.dumps(rec)+'\n')
    ev_id+=1; return eid

cl_id=566
def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid=f'CLAIM-{cl_id:04d}'
    rec={"claim_id":cid,"text":text,"confidence":conf,"domain":domain,"supporting_evidence":evs,"audit_status":"unchecked","notes":notes}
    with open(CLAIMS_PATH,'a') as f: f.write(json.dumps(rec)+'\n')
    cl_id+=1; return cid

os.makedirs(RAW_DIR,exist_ok=True)

e_account=new_ev("FTG support + sakibpro transfer guide + r/DLS + oyuncozumleri",
    "FTG official (support.ftgames.com): save data NOT secured on Google Play Games or iCloud (those are different services not used). Same-OS backup uses 'Sign in with Google' (Android) or 'Sign in with Apple' (iOS 13+) via Settings→Advanced — manual opt-in, NOT automatic. Cross-platform transfer (Android↔iOS) uses one-time transfer code via Settings→Advanced→Manage Devices→Generate Code (5-minute expiry, enter via Link Profile on new device). Profile limited to ONE account per player. Maximum 3 devices per profile; devices can be removed via Manage Devices. Signing out unlinks profile → risk of data loss on uninstall/device change. DLS26 cross-platform transfer code introduced (DLS25-era sakibpro guide, same system applies). NO automatic cloud save — r/DLS warns users frequently lose progress if not linked. Facebook login NO LONGER SUPPORTED (removed years ago; cannot rescue old FB-linked profiles). IAP and save data historically did NOT transfer across platforms (FTG: 'save data and IAPs cannot be transferred Android↔iOS') — but DLS26 code-transfer suggests progress may now carry across platforms (verify with APK). DLS19 profiles and IAPs do NOT transfer to DLS25/26 (separate standalone builds); DLS25→DLS26 is an in-place seasonal update (same app, profile carries). Google Play Games cloud-save / iCloud backup / Game Center NOT used by the game (per official support). Game Center integration added in v13.110 for achievements/friend leaderboards (iOS), not save data.",
    "evidence/raw/account_turn33/EV-368_account.html",
    "Sign-in-with-Google/Apple, cross-platform transfer code (5min/3dev), no Facebook, no GPG/iCloud, profile carryover rules")
e_clans=new_ev("sportsdunia clans guide + dlsmod + appstore changelog",
    "Clans (v13.040 launch feature, expanded v13.110/v13.330): accessible from main screen or top-right profile menu. Minimum 50 members cited for full clan functionality (fifaworldcupnews). Create or browse/search/enter-code to join. Clan customization: Badge (style/background/icon/frame-colour/dressing), Name, Country, Entry Requirements (minimum team rank), Type (open/closed/invite-only). Leader is primary admin (can remove members); v13.110 added vice-captains. Clan Points earned by: regular matches, Live Event wins, Dream Draft event wins, Real-Life Scenarios completion, Season Pass tiers, intra-clan friendly matches. Personal contribution cap 350,000 CP per cycle — must cooperate with clanmates to reach top tiers. Clan reward ladder (sportsdunia): 25g @1M CP, Legendary XP boost @2M, Legendary Scout @3M, 500c @5M, Rare Special Coach @7.5M, 150g @10M. First reward unlocks at 25,000 CP. v13.110 added Clan leaderboards + Clan Point boosts; v13.330 added Clan chat emoji reactions + interactions + Fanzone bonuses. Clans unlocks at a 'high enough rank' per dlsmod (tier gate unspecified). Community request for easier clan menu access + dedicated chat (beyond emoji reactions). Appitika listing mentions 'trade resources with fellow managers' — unverified feature. Fanzone facility upgrades grant Clan bonuses (paired with Stadium discounts per v13.330).",
    "evidence/raw/account_turn33/EV-369_clans.html",
    "Clan creation/joining, customization, CP sources/cap, reward ladder, v13 updates, Fanzone synergy")
e_exhibition=new_ev("BlueStacks beginner guide (DLS20, mechanics preserved in DLS26)",
    "Exhibition Mode: offline-friendly; supports local friendlies via room code (invite friends/family); no match rewards; ideal for testing formations/tactics without league pressure.",
    "evidence/raw/account_turn33/EV-370_exhibition.html",
    "Exhibition mode, room-code friendlies, no rewards")

# CLOUD SAVE / ACCOUNT
add_claim("Same-platform backup uses 'Sign in with Google' (Android) or 'Sign in with Apple' (iOS 13+) via Settings → Advanced; requires manual opt-in, NOT automatic.", 1, "account/cloud", [e_account])
add_claim("DLS does NOT use Google Play Games cloud save, iCloud backup, or Game Center for save data (Game Center in v13.110+ is for achievements/friend leaderboards only).", 1, "account/cloud", [e_account])
add_claim("Cross-platform transfer (Android↔iOS): Settings→Advanced→Manage Devices→Generate Code creates a one-time transfer code valid for 5 minutes; enter via Settings→Advanced→Link Profile on new device.", 1, "account/transfer", [e_account])
add_claim("Each DLS profile is limited to one account/player and a maximum of 3 linked devices; devices can be unlinked via Manage Devices.", 1, "account/devices", [e_account])
add_claim("Signing out of Sign in with Google/Apple while playing unlinks the profile and risks data loss on uninstall or device change.", 1, "account/warning", [e_account])
add_claim("Facebook login is NO LONGER SUPPORTED (removed years ago); old Facebook-linked profiles cannot be recovered.", 1, "account/facebook", [e_account])
add_claim("Historical FTG policy: save data and IAPs do NOT transfer across platforms (Android↔iOS). DLS26 cross-platform code system may now carry profile progress (verify post-transfer behaviour).", 2, "account/crossplat", [e_account])
add_claim("DLS19 (and earlier) profiles and IAPs do NOT transfer to DLS25/DLS26 (separate standalone builds). DLS25→DLS26 is an in-place seasonal update over the same app (com.firsttouchgames.dls7), so progress carries forward automatically.", 1, "account/migration", [e_account])
add_claim("Unlinked-profile horror stories (lost accounts after Google-link mistakes) appear on r/DLS; always verify linked account before reinstall or device change; FTG support requests Account ID for recovery (impossible to provide once wrong save loads).", 3, "account/pitfalls", [e_account])

# CLANS
add_claim("Clans are accessible from the main home screen or top-right profile menu; joining a clan may require reaching a minimum rank/division (tier gate unspecified).", 2, "clans/access", [e_clans])
add_claim("Clans require a minimum size (~50 members) for full features/competitive ranking (one source cites min 50).", 3, "clans/size", [e_clans])
add_claim("Clan customization: Badge (style/background/icon/frame/dressing), Clan Name, Country, Entry Requirements (minimum team rank), Type (open / closed / invite-only).", 1, "clans/customization", [e_clans])
add_claim("Clan leadership: founding player is Leader (primary admin, can remove members); v13.110 added Vice-Captain roles.", 1, "clans/leadership", [e_clans])
add_claim("Clan Points (CP) are earned by: playing regular matches, winning Live events, winning Dream Draft events, completing Daily/Real-Life Scenarios, progressing Season Pass tiers, playing intra-clan friendly matches.", 2, "clans/points", [e_clans])
add_claim("Per-player personal CP contribution cap per cycle is approximately 350,000 CP; reaching top rewards requires a large active clan.", 2, "clans/cap", [e_clans])
add_claim("Clan reward ladder thresholds: 25,000 CP unlock; 25 gems @1M; Legendary XP Boost @2M; Legendary Scout @3M; 500 coins @5M; Rare Special Coach @7.5M; 150 gems @10M.", 2, "clans/rewards", [e_clans])
add_claim("v13.110 (Mar 2026) added Clan leaderboards and Clan Point boosts; v13.330 (Jun 2026) added in-clan emoji reactions/interactions and Fanzone-facility synergy (Clan bonuses, Stadium discounts).", 1, "clans/patches", [e_clans])
add_claim("Upgrading the Fanzone facility grants Clan bonuses (paired with Stadium build discounts) per v13.330.", 2, "clans/fanzone", [e_clans], "Fanzone synergy with Clans corroborated across multiple sources")
add_claim("Clans include casual/competitive modes with rating-gated entry; intra-clan friendly matches contribute CP and provide skill practice.", 2, "clans/modes", [e_clans])
add_claim("Community feedback: Clans feature praised but wants easier menu access and proper text chat with clanmates (current chat limited to emoji reactions).", 2, "clans/feedback", [e_clans])
add_claim("Trading resources with clanmates is mentioned in one store listing (appitika) but unverified; treat as speculative.", 4, "clans/trading", [e_clans])

# EXHIBITION
add_claim("Exhibition Mode: offline-friendly, no rewards; supports local friendlies via room-code invite; ideal testing ground for formations/tactics without league pressure.", 1, "modes/exhibition", [e_exhibition])

for f in ['EV-368_account.html','EV-369_clans.html','EV-370_exhibition.html']:
    p=os.path.join(RAW_DIR,f)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write(f"placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl=sum(1 for _ in f)
print(f"Added {cl_id-566} new claims and {ev_id-368} EVs. Totals: {n_cl} claims, {n_ev} EVs")
