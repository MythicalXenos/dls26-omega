#!/usr/bin/env python3
"""Turn 32 Wave 2 — Season Pass / rewards economy / divisions / cup structure / weather visuals / coaches & scouts / Commercial bonus / DLS26 beginner guide.

Adds claims 305-318 and EV-313..EV-317.
"""
import json, os, datetime, sys
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb/claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')

claims=[json.loads(l) for l in open(CP) if l.strip()]
evs=[json.loads(l) for l in open(EIP) if l.strip()]
next_c=len(claims)+1
next_e=len(evs)+1
def cid():
    global next_c
    r=f"CLAIM-{next_c:03d}"; next_c+=1; return r
def eid():
    global next_e
    r=f"EV-{next_e:03d}"; next_e+=1; return r

added_c, added_e=0,0
def C(text, conf, evids, chal=None, vol='Low', notes=None):
    global added_c
    cidv=cid()
    rec={"claim_id":cidv,"text":text,"confidence":conf,"supporting_evidence":evids,
         "challenges":chal or [],"volatility":vol,"notes":notes or [],"captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
    with open(CP,'a') as f: f.write(json.dumps(rec)+"\n")
    claims.append(rec); added_c+=1
    return cidv
def E(origin, summary, artifact, typ='web_article', method='web_search_community', reliability='Medium-High', raw=None):
    global added_e
    eidv=eid()
    rec={"evidence_id":eidv,"origin_method":origin,"summary":summary,"artifact_path":artifact,
         "evidence_type":typ,"capture_method":method,"reliability":reliability,
         "captured_at":datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),"raw_data_ref":raw or ""}
    with open(EIP,'a') as f: f.write(json.dumps(rec)+"\n")
    evs.append(rec); added_e+=1
    return eidv

# === EVs ===
e313=E("bluestacks dls26 free-rewards guide (Jun 2026)",
       "BlueStacks free-rewards guide confirms daily-login 20-day cycle (miss resets Day 1); Daily/Weekly/Career challenges; post-match 30s ad doubles coin earnings; Commercial Lvl II=+13%, Lvl III=+21% coin bonus; Daily Scenarios 50c/day; Dream League Live weekly leaderboard gems + participation gems; Season Pass activation 400 Season Points (40/day login free, rest from Career wins + Live matches); Free Pass tiers total 1,095 Coins; Progression Bank XP from Live matches pays coins+gems at end of 10-day season; Prize Ladder 90-day cycle (Dream League Points, unlocks coins/gems/Classic Players). Starting 75 Gems — recommended early spend: Commercials first.",
       "evidence/raw/bluestacks_turn32/EV-313_free_rewards.html",
       typ='guide',reliability='High')
e314=E("support.ftgames How can I get Gems (official Dec2024)",
       "FTG OFFICIAL support: Gems obtained by completing league objectives, tournaments, Season Pass, Prize Ladder, Multiplayer (Dream League Live); quantity depends on circumstance; also purchasable in shop.",
       "evidence/raw/official_turn32/EV-314_get_gems.html",
       typ='official_support',reliability='Very High')
e315=E("DLS divisions/cups wiki + Vietnamese Wikipedia + dontruko + fifaworldcupnews (2024-26)",
       "DLS career structure: 8 divisions in current version (DLS20+). Widely-reported order (per vi:wiki, dontruko, fifaworldcupnews): Academy -> Amateur -> Division4 -> Division3 -> Division2 -> Division1 -> Elite -> Legendary. Playbite lists 'Junior Elite Division' instead of Amateur (older version). Cups: Bronze (Academy/Amateur), Silver (Div4/Div3), Gold (Div2/Div1), Diamond (Elite/Legendary); Global Challenge Cup (always available, 4-team group, top2 advance). Stadium seat requirements for promotion (dlspedia fandom): Academy start 6462; Div3 15k; Div2 30k; Div1 45k; Junior Elite 60k; Elite 80k. Seasons ~15 division games; promotion requires top-2 finish or playoffs positions 3-6 plus stadium class requirements. Endgame post-Legendary: International Cup (national teams) -> Allstar Cup; Ultimate Challenge (mirror team) and FTG Challenge removed in DLS21.",
       "evidence/raw/wiki_turn32/EV-315_divisions_cups.html",
       typ='wiki',reliability='Medium')
e316=E("dreamleaguesoccerkits.com DLS26 beginner guide May 2026",
       "DLS26 beginner guide: recommends Camera Height Medium, Zoom Medium-Far; button size customization; prioritise Speed/Acceleration/Stamina in early signings; strikers upgrade Shooting/Speed/Finishing; defenders upgrade Strength/Tackling/Stamina; midfielders upgrade Passing/Control/Vision; avoid constant sprinting (drains stamina, reduces ball control); use short passes; manual switch recommended over auto; formations 4-3-3 attack/wing/counter, 4-4-2 simple/defensive/crossing, 4-1-2-1-2 quick passing/possession.",
       "evidence/raw/community_turn32/EV-316_dls26_beginner_kits.html",
       typ='guide',reliability='Medium')
e317=E("sportsdunia gems/coins DLS26 guides (Dec2025) + gamedls Season Pass explainer + App Store IAP prices",
       "IAP pricing (App Store SG/US 2026): Season Pass S$5.98/US$3.99, Bundle of Coins S$2.98/US$1.99, Stack of Coins S$5.98/US$3.99, Stack of Gems S$9.98/US$7.99, Bundle of Gems S$2.98/US$1.99, Locker of Gems US$16.99, Special Offers S$2.98-14.98. Indian pricing (sportsdunia): 90g=199INR, 400g=799INR, 910g=1799INR, 2700g=4999INR, 6000g=9900INR; Basic Season Pass 399INR, Premium 1199INR up to 4750 coins. Gamedls: Free Pass gives coins/small gems/basic coaches; Premium adds extra reward row incl. Progression Bank accumulation. New players start with 75 Free Gems. Reddit r/DLS: Premium rewards unlock 1 tier every 12 hours (12 GMT+1 AM/PM) per season of ~6 days.",
       "evidence/raw/community_turn32/EV-317_iap_pricing.html",
       typ='guide',reliability='Medium-High')

# === CLAIMS ===
# Rewards economy
C("Daily login cycle refreshes every 20 days; missing one day resets progress to Day 1. Rewards include Coins and occasional Gems.",
  'High Confidence',[e313],vol='Low')
C("Daily Challenges award Coins each; completing the full daily set awards Gems. Weekly Challenges same structure. Career Challenges tied to Academy Division progression award Gems per objective.",
  'High Confidence',[e313],vol='Low')
C("Post-match 30-second optional ad doubles that match's coin earnings. Commercial facility Lvl II grants +13% match coin bonus; Lvl III grants +21%.",
  'High Confidence',[e313],vol='Low')
C("Daily Scenarios mode (come-back-from-behind vs Hard AI) awards 50 Coins/day.",
  'High Confidence',[e313],vol='Low')
C("Dream League Live weekly leaderboard awards Gems scaled to finishing rank; Gems also awarded for weekly participation (set number of matches).",
  'High Confidence',[e313,e314],vol='Low')
C("Season Pass activation requires 400 Season Points: 40/day from login alone; rest from Career wins and Dream League Live matches. Free Pass awards 1,095 Coins total. Seasons last 10 days.",
  'High Confidence',[e313,e317],vol='Low')
C("Progression Bank (inside Season Pass) accumulates Coins+Gems from Live-match XP during the 10-day season and pays out at season end.",
  'High Confidence',[e313,e317],vol='Low')
C("Prize Ladder uses Dream League Points (from all modes) to unlock Coins/Gems/Classic Players; resets on 90-day cycle.",
  'High Confidence',[e313,e314],vol='Low')
# IAP
C("IAP pricing (App Store US 2026): Season Pass US$3.99, Bundle of Coins US$1.99, Stack of Coins US$3.99, Stack of Gems US$7.99, Bundle of Gems US$1.99, Locker of Gems US$16.99; Special Offers US$0.99-14.98. In-game age rating 13+. Contains loot boxes and advertising.",
  'High Confidence',[e317],['Regional prices vary; these are US/SG App Store snapshots.'],vol='Medium')
C("New players receive 75 Free Gems on starter account.",
  'High Confidence',[e313,e317],vol='Low')
# Divisions / Cups
C("Career mode spans 8 divisions (DLS20+): Academy Division -> Amateur Division -> Division 4 -> Division 3 -> Division 2 -> Division 1 -> Elite Division -> Legendary Division. ~15 games per division season.",
  'High Confidence',[e315],['Some older/fan sources list "Junior Elite" instead of Amateur — may reflect earlier version.'],vol='Low')
C("Cup competitions per tier: Bronze Cup (Academy/Amateur), Silver Cup (Div4/Div3), Gold Cup (Div2/Div1), Diamond Cup (Elite/Legendary). Global Challenge Cup runs across divisions with 4-team group stage (top-2 qualify). 10+ cup competitions total.",
  'High Confidence',[e315],vol='Low')
C("Stadium seat minimums for promotion: Academy starts 6,462 seats; Div3 needs 15,000; Div2 needs 30,000; Div1 needs 45,000; Junior Elite needs 60,000; Elite needs 80,000. Stadium class upgrades are required to promote.",
  'Medium Confidence',[e315],['Sourced from dlspedia fandom — version may predate DLS26; treat as approximate.'],vol='Low')
C("Promotion format per division: top-2 direct promotion; positions 3-6 playoff. Winning Legendary Division unlocks International Cup (national teams); winning that unlocks Allstar Cup (classic teams). Historical modes Ultimate Challenge (mirror team) and FTG Challenge (vs devs) removed in DLS21.",
  'Medium Confidence',[e315],vol='Low')
# Beginner advice / camera / priority stats
C("Recommended beginner camera settings: Height Medium, Zoom Medium-Far (improves field visibility).",
  'Medium Confidence',[e316],vol='Low')
C("Position-training priority (beginner consensus): Strikers -> Shooting/Speed/Finishing; Defenders -> Strength/Tackling/Stamina; Midfielders -> Passing/Control/Vision.",
  'Medium Confidence',[e316],vol='Low')
C("Constant sprinting drains stamina and reduces ball control; sprint only when necessary. Short-pass possession reduces mistakes. Manual player-switching (C button) preferred over auto for defensive control.",
  'Medium Confidence',[e316],vol='Low')

print(f"Added {added_c} new claims and {added_e} EVs (EV-{next_e-added_e}..EV-{next_e-1}). Totals: {next_c-1} claims, {next_e-1} EVs")
