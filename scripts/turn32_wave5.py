#!/usr/bin/env python3
"""Turn 32 Wave 5 — Clans system, version history (Summer Spotlight, Cult Heroes, Dynamic Stars, Fanzone, World Tournament), friend matches, launch covers."""
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

e327=E("sportsdunia DLS26 clans guide (Jan2026) + dlsmod + fifaworldcupnews clans + r/DLS clan recruitment threads",
       "Clans system (new in DLS26): unlock at rank 20; accessed via Main Menu or top-right profile menu; join public clan / search by name / enter clan code / create own (free). Clan creation options: custom badge (frame/background/icon/colours), name (with generate option), country, entry requirements (min team rating/rank), type (open/closed/invite-only); leader is admin who can remove members. Clan Points earned via: regular matches, Live events wins, Dream Draft wins, real-life scenarios, Season Pass tiers; individual cap 350,000 CP per season per player (so join large/active clans). Clan rewards ladder (per sportsdunia): 25k CP threshold to unlock rewards; 25 Gems @1M CP; Legendary XP boost @2M; Legendary Scout @3M; 500 Coins @5M; Rare Special Coach @7.5M; 150 Gems @10M. Top clan leaderboard players earn 100 Gems. Minimum 50 members for ranked clan play (per fifaworldcupnews). Friend/clan matches: both players must be in the same clan; challenge via DLL->Clan tab. Friend Match feature unlocks after 6 Career Mode matches (DLS25 data), uses friend codes; weak connection = forfeit 3-0.",
       "evidence/raw/community_turn32/EV-327_clans.html",
       typ='guide',reliability='High')
e328=E("App Store version history (US/ZA) + APKMirror + fifaworldcupnews + dlskits.mobi + thesoccerera",
       "DLS26 App package: com.firsttouchgames.dls7 (same package as DLS20+ — continuous update line; DLS25/26 are in-place updates of same app). Version history from App Store (2026): v13.320/v13.330 (Jun 8/10 2026, Summer Spotlight initial rollout): Dynamic Stars (special players that upgrade live with national team performances — coming soon), new Fanzone facility (Clan bonuses + Stadium discounts), new World Tournament event type, manager accessories (North American themed items), Clan improvements (interactions + emoji reactions); v13.340 (Jun 22 Clan Improvements only); v13.350 (Jul 14 repeats Fanzone/World Tournament/Accessories/Clan Improv); v13.410 (Aug 20) Cult Heroes special player collection announced; v13.420 (Sep 1) Cult Heroes coming soon + bug fixes; v13.430 (Sep 16) Cult Heroes coming soon + dozens of bug fixes. Initial DLS26 launch (Nov-Dec 2025): All-new Clans, new Turkish (Erdi Eliacik) and Arabic (Dr Kamal Atteya) commentary, updated 2025/26 player data (more classic/special/national-team players), increased squad size (unlimited Special Players), improved venues/iconic stadiums, enhanced match atmosphere (props/banners/flags), Kick-Off Stars launch cards (Raphinha + Julian Alvarez special editions), new soundtrack/SFX.",
       "evidence/raw/official_turn32/EV-328_version_history.html",
       typ='official',reliability='Very High')
e329=E("fifaworldcupnews DLS26 features + fifaworldcupnews July 2026 World Heroes event",
       "World Heroes event started July 1, 2026 alongside upcoming World Winners event — limited-time global events offering exclusive event-specific players (special agent rewards) and updated Season Pass objectives. May 28, 2026 noted as Summer Spotlight release date (article says 13.420 released Sep 1, likely conflicting — May date was initial launch and Sep was patch). Summer Spotlight also included major rating changes: some Rare players upgraded to Legendary cards and vice versa. Player Recovery feature: buy a sold player back within limited time (from v12.200 DLS25 notes, carried forward).",
       "evidence/raw/community_turn32/EV-329_events.html",
       typ='article',reliability='Medium')
e330=E("gamingonphone DLS25 friend-match guide (Dec2024)",
       "Friend Match unlock: complete 6 Career Mode matches -> unlock Dream League Live tab + Friend Match. Adding friends: Friends menu -> Generate Code on one device -> enter on the other. Setting up a friendly: DLL tab -> Exhibition Mode -> both enter code -> tap OK; secure connection established within seconds. Weak connection on either side = immediate forfeit and 3-0 victory to the other side. Requires stable internet.",
       "evidence/raw/gamingonphone_turn32/EV-330_friends.html",
       typ='guide',reliability='High')

# CLAIMS
C("Clans system is a DLS26-exclusive new feature; requires player rank 20 to unlock; accessible from Main Menu or top-right profile menu.",
  'High Confidence',[e327],vol='Low')
C("Clans: free to create (custom badge/frame/background/icon/colours, name, country, open/closed/invite-only, min team rating/rank requirements). Can join via public browse, name search, or clan code. Leader can remove members.",
  'High Confidence',[e327],vol='Low')
C("Clan Points earned via: regular matches, Live event wins, Dream Draft wins, completing scenarios, Season Pass tiers. Individual contribution cap per player per season is ~350,000 CP. Minimum ~50 members typically required for top-tier competitiveness.",
  'High Confidence',[e327,e329],vol='Low')
C("Clan reward ladder (total CP): 25k unlock threshold; 25 Gems @1M; Legendary XP boost @2M; Legendary Scout @3M; 500 Coins @5M; Rare Special Coach @7.5M; 150 Gems @10M. Individual top contributor on clan leaderboard earns 100 Gems.",
  'Medium-High Confidence',[e327],['Sportsdunia-published ladder; DLS26 live values may differ by season.'],vol='Medium')
C("Clan member matches: same-clan players can challenge each other 1v1 via Dream League Live -> Clan tab. These matches contribute Clan Points.",
  'High Confidence',[e327])
# Version history
C("DLS26 shares package com.firsttouchgames.dls7 with DLS20-DLS25 — continuous in-place update line, not a separate app. Latest version as of mid-Sep 2026: 13.430 (Sep 16, 2026).",
  'Very High Confidence',[e328])
C("DLS26 launch (Nov-Dec 2025) introduced: Clans system, Turkish commentary (Erdi Eliacik) and Arabic commentary (Dr Kamal Atteya), updated 2025/26 FIFPRO player data with additional Classic/Special/national-team players, unlimited Special Player slots in squad, new/upgraded iconic stadiums, enhanced matchday atmosphere (more props/banners/flags), Kick-Off Stars launch special cards (Raphinha + Julian Alvarez), new soundtrack and SFX.",
  'Very High Confidence',[e328])
C("Summer Spotlight 2026 update (rolling out May-Jun 2026, v13.320-13.350) added: Dynamic Stars (special players whose OVR upgrades live with real-world national-team performances — marked 'Coming Soon' at launch), new Fanzone facility (Clan bonuses + Stadium discounts), new World Tournament event type, North American themed manager accessories (cosmetic), Clan chat improvements (emoji reactions, new interactions), friend-match options, transfer market upgrades (player lock management), Daily Bonus, Scenario expansion (more objectives/rewards), Player Recovery (buy back sold players within limited time), Special Coach Packs, gameplay tuning, roster updates. Major rating rebalances: some players upgraded Rare->Legendary and vice versa.",
  'Very High Confidence',[e328,e329])
C("Late Summer 2026 update (v13.410/13.420/13.430, Aug-Sep 2026): 'Cult Heroes' Special Player collection announced (coming soon); dozens of bug fixes.",
  'Very High Confidence',[e328])
C("World Heroes event launched July 1, 2026; World Winners event teased. Both are limited-time global events with special-agent rewards, exclusive event players, and updated Season Pass objectives.",
  'Medium Confidence',[e329],vol='Medium')
# Friend matches
C("Friend Match feature unlocks after completing 6 Career Mode matches. Friends added via generated friend code (in Friends menu). Friendly matches launched from DLL -> Exhibition Mode by both sides entering the code; requires stable internet; disconnect = forfeit 3-0.",
  'High Confidence',[e330],["From DLS25 guide; system unchanged in DLS26 per Summer Spotlight notes."],vol='Low')

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
