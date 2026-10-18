#!/usr/bin/env python3
"""Turn 32 Wave 9 — Soundtrack list + TOS/bans/anti-cheat."""
import json, os, datetime, re
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb/claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
evs=[json.loads(l) for l in open(EIP) if l.strip()]
next_c=max(int(c['claim_id'].split('-')[1]) for c in claims)+1
next_e=max(int(e['evidence_id'].split('-')[1]) for e in evs)+1
ac,ae=0,0
def cid():
    global next_c,ac; r=f"CLAIM-{next_c:03d}"; next_c+=1; ac+=1; return r
def eid():
    global next_e,ae; r=f"EV-{next_e:03d}"; next_e+=1; ae+=1; return r
def C(text, conf, evids, chal=None, vol='Low', notes=None):
    cv=cid()
    rec={"claim_id":cv,"text":text,"confidence":conf,"supporting_evidence":evids,
         "challenges":chal or [],"volatility":vol,"notes":notes or [],
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
    with open(CP,'a') as f: f.write(json.dumps(rec)+"\n"); claims.append(rec)
def E(origin, summary, artifact, typ='web_article', method='web_search_community', reliability='Medium'):
    ev=eid()
    rec={"evidence_id":ev,"origin_method":origin,"summary":summary,"artifact_path":artifact,
         "evidence_type":typ,"capture_method":method,"reliability":reliability,
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),"raw_data_ref":""}
    with open(EIP,'a') as f: f.write(json.dumps(rec)+"\n"); evs.append(rec)
    return ev

e336=E("vgost.fandom.com DLS26 soundtrack page + YouTube DLS26 OST playlists + DLS-FTS YouTube channel",
       "DLS26 official soundtrack (9 confirmed tracks per vgost.fandom): AR/CO x Punctual x NewEra - Generation Love (also in EA FC26); Benson Boone - Sorry I'm Here for Someone Else; Katy Perry - LIFETIMES; Marshmello, Trueno - Fale Entao; NoMBe - Space for Two; Rachel Chinouriri - Can We Talk About Isaac?; Rudimental x Khalid - All I Know; South Arcade - Supermodels; TEEYZ - Coming in Hot. DLS-classic soundtracks (DLS14-19 era) include Secret Rivals (Ghosting, Tonight Matthew), We Outspoken (Crisis, I Can Be), Charly Coombes & The New Breed (Broken Glass, Hell Below, Jungle & Tides), Dance a la Plage (Need To Know, She's Gone by Morning). DLS25 soundtrack included Bakermat ft Rhys Lewis (Good Feeling), Two Door Cinema Club (Sure Enough), Barns Courtney (Supernatural), among others. The in-game Music volume slider controls soundtrack; prior r/DLS guidance recommended Music off for competitive focus.",
       "evidence/raw/community_turn32/EV-336_soundtrack.html",
       typ='wiki',reliability='Medium-High')
e337=E("FTG support 'Why have I been blocked from playing DLS?' (Aug2021 OFFICIAL) + ftgames.com Terms of Use + r/DLS ban threads (2024-26) + hackerbot + happymod/modcombo + mundodls",
       "OFFICIAL FTG policy: Only authorised DLS versions are from Apple App Store or Google Play. Modded APKs and external software hacks aimed at gaining unfair advantage (inappropriate virtual currency gain, AI interference, circumvention of normal progression, exploiting obvious game bugs) result in bans. Sanctions may also be applied in extreme circumstances for offensive team/manager names. Ban appeals only considered if incorrectly flagged; support will not reverse bans based on user requests otherwise. Multiplayer bans are often permanent (per r/DLS mod-team info, FTG rarely lifts DLL bans except in extreme cases). Common ban triggers: multiple accounts on one device via illegitimate methods; suspicious trading/logging in from many devices rapidly; use of modified APKs (unlimited coins/gems menu options — stupid rivals, freeze players, unlimited energy/subs, no injuries, opponent no goals); Vietnamese/Turkish communities historically associated with speed hacks/cheats. Server-side currency tracking since DLS20+ means unlimited coin/gem mods are detected quickly (hours) -> permanent ban. Account hacking/linking to unknown devices has been reported. Subreddit policy prohibits posts/comments promoting hacks/cheats/exploits.",
       "evidence/raw/official_turn32/EV-337_bans_tos.html",
       typ='official+community',reliability='High')

# CLAIMS
C("DLS26 official soundtrack (9 tracks confirmed): AR/CO x Punctual x NewEra - Generation Love; Benson Boone - Sorry I'm Here for Someone Else; Katy Perry - LIFETIMES; Marshmello & Trueno - Fale Entao; NoMBe - Space for Two; Rachel Chinouriri - Can We Talk About Isaac?; Rudimental x Khalid - All I Know; South Arcade - Supermodels; TEEYZ - Coming in Hot.",
  'Medium-High Confidence',[e336],['Compiled from vgost.fandom; YouTube full-soundtrack videos verify the same list.'],vol='Low')
C("DLS-classic (2014-2019 era) nostalgia tracks: Secret Rivals (Ghosting, Tonight Matthew), We Outspoken (Crisis, I Can Be), Charly Coombes & The New Breed (Broken Glass, Hell Below, Jungle & Tides), Dance a la Plage (Need To Know, She's Gone by Morning).",
  'Medium-High Confidence',[e336],vol='Low')
# Anti-cheat
C("OFFICIAL FTG policy: Only App Store and Google Play versions of DLS are authorised. Modded APKs, external hack software, and exploitation of unknown bugs (currency dupes, AI manipulation, progression circumvention) result in account bans. Offensive team/manager names may also trigger action.",
  'Very High Confidence',[e337])
C("Ban appeals are only accepted by FTG support if the player believes they were incorrectly flagged; otherwise bans are not lifted on request.",
  'Very High Confidence',[e337])
C("Dream League Live multiplayer bans are typically permanent; FTG rarely reverses them except in extreme circumstances.",
  'Medium-High Confidence',[e337],vol='Medium')
C("Common ban triggers: multiple accounts on same device via illegitimate methods; suspicious trading or rapid multi-device logins; use of modified APKs (which advertise unlimited coins/gems, freeze players/stupid rivals, unlimited energy/subs, no-injuries, opponent-cannot-score toggles). Since DLS20, server-side currency tracking detects abnormal coin/gem amounts quickly (hours) leading to permanent ban.",
  'High Confidence',[e337])
C("Well-documented hacking communities (notably Vietnamese and Turkish scenes per r/DLS) sell or distribute speed-boost and other cheats; FTG bans accounts detected using these. Account hijacking (unknown-device linking) has also been reported.",
  'Medium-High Confidence',[e337],vol='Medium')
C("r/DreamLeagueSoccer subreddit rules prohibit posts or comments promoting hacks/cheats/exploits (removed on sight).",
  'High Confidence',[e337])

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
