#!/usr/bin/env python3
"""Turn 32 Wave 4 — Difficulty, Dream Draft, Dream Points, referee/carding issues, daily challenge gem rewards.

Adds claims 335-347 and EV-323..EV-326.
"""
import json, os, datetime
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

e323=E("r/DLS difficulty threads (2023-2025) + App Store reviews + NamuWiki DLS23",
       "Difficulty: DLS25 introduced a settings toggle for difficulty (Medium/Hard only; Easy and Very Hard were removed per DLS25 threads; DLS23 NamuWiki listed Easy/Medium/Hard/Very Hard rewarding 25/50/75/100 gold). Many users report Hard vs Medium difference is subtle: faster AI passing, more aggressive tackling, shooting from outside box nerfed; AI adapts to player formation over time (common theory). AI difficulty scales with division tier (Academy easy -> Legendary hardest); post-red-card AI becomes drastically harder (widely-reported '10v11 bug'). Career mode widely considered too easy once team is maxed (common complaint since DLS23). Dream League Live vs humans is the real endgame difficulty; scenario mode uses fixed Hard AI.",
       "evidence/raw/reddit_turn32/EV-323_difficulty.html",
       typ='community',reliability='Medium')
e324=E("BlueStacks Dream Draft update (Oct2021) + r/DLS Dream Draft threads + YouTube DLS25 Global Stars",
       "Dream Draft: limited-time tournament mode where you draft a 75+ rated squad (at least 1 Star Player required); up to 7 rounds against different opponents (DLS25 Global Stars event uses 3 lives); leaderboard rewards medals/coins/gems for winners/runner-up/3rd. Entry costs 40 gems; typical profit ~10 gems after rewards (considered poor value for many players). Some offline variants vs AI; can earn gems by beating CPU 8 times in a row. Part of Prize Ladder/Dream Points grind.",
       "evidence/raw/bluestacks_turn32/EV-324_dream_draft.html",
       typ='community',reliability='Medium-High')
e325=E("gamingonphone Dream Points guide (Dec2024)",
       "Dream Points (DP): earned from Career, Dream League Live, Dream Draft, and Weekly Challenges. DP boosts: Common +50% (210 DP max Career, 278 DLL/Draft), Rare +75% (245 / 324), Legendary +150% (350 / 463). DP drives the Prize Ladder (90-day cycle with coins/gems/Classic Players).",
       "evidence/raw/gamingonphone_turn32/EV-325_dream_points.html",
       typ='guide',reliability='High')
e326=E("r/DLS referee/carding threads (2024-25) + LevelWinner DLS24 guide + r/DLS daily-challenge gem math",
       "Referee behaviour is a common complaint: red cards given AFTER advantage played to a goal (incorrect per real laws where advantage + goal should yield yellow max); last-man DOGSO detection sometimes fails (only yellow for clear last-defender fouls); red-card AI becomes drastically harder ('10x'). Daily Challenge gem rewards (reddit DLS24 numbers): Regular daily main reward 5-11 gems streak (+1/day, miss resets to 5, max 11); Season Pass daily 10-22 streak (+2/day). Regular weekly fixed 10 gems; Season Pass weekly 20 gems. Additional gem task rewards: Regular daily 2x10=20, Season Pass daily 2x20=40, Regular weekly 2x20=40, Season Pass weekly 2x50=100. AI behaviour: faster passing at higher divisions, through-ball space denied, better GK saves, increased tackle effectiveness.",
       "evidence/raw/reddit_turn32/EV-326_referee_dailies.html",
       typ='community',reliability='Medium')

# CLAIMS
C("DLS25 added an in-setting difficulty toggle; DLS26 offers Medium and Hard (Easy/Very Hard were removed by DLS25 per community consensus). Hard increases AI passing speed, defensive aggression, and reduces long-shot success; many players report the difference is subtle with maxed squads.",
  'Medium-High Confidence',[e323],vol='Medium')
C("AI difficulty scales with division progression: opponents shoot more accurately, tackle harder, deny through-ball space, and GKs make more saves as you climb from Academy to Legendary. AI appears to adapt to your formation (common community theory), prompting many players to switch formations each season.",
  'Medium-High Confidence',[e323,e326],vol='Medium')
C("Commonly reported AI bug: after the AI receives a red card (10v11 disadvantage FOR the PLAYER), the AI becomes drastically harder rather than easier.",
  'Medium Confidence',[e323,e326],vol='Medium')
C("Scenario mode uses fixed Hard AI (come-from-behind) and resets daily for 50 Coins.",
  'High Confidence',[e323])
# Dream Draft
C("Dream Draft is a limited-time tournament mode: draft a 75+ rated squad (at least 1 Star Player required); up to 7 rounds/opponents; 3-life variant in Global Stars events; pays medals/coins/gems to top placers via leaderboard.",
  'Medium-High Confidence',[e324],vol='Medium')
C("Dream Draft entry costs ~40 gems; net profit often only ~10 gems, leading many F2P players to consider it poor value. Some sources cite 8-win CPU runs as a fast gem source.",
  'Medium Confidence',[e324],vol='Medium')
# Dream Points
C("Dream Points (DP) are earned from Career matches, Dream League Live, Dream Draft, and Weekly Challenges. DP fuels the 90-day Prize Ladder which grants Coins, Gems, and Classic Players.",
  'High Confidence',[e325,e324])
C("DP Boosts (Consumables): Common +50% (max 210 DP Career / 278 DLL+Draft), Rare +75% (245 / 324), Legendary +150% (350 / 463).",
  'Medium-High Confidence',[e325],vol='Low')
# Referee
C("Referee decisions are a recurring complaint: post-advantage red cards after goals (incorrect application of real-football advantage law where a goal scored on advantage should limit punishment to yellow at most); last-man DOGSO detection sometimes fails (only yellow for clear goal-denying fouls).",
  'Medium Confidence',[e326],vol='Medium')
# Dailies reward structure
C("Daily Challenge gem rewards use a streak system: Regular daily 5-11 gems (+1/day, miss resets to 5, cap 11); Season Pass daily 10-22 gems (+2/day). Regular weekly fixed 10 gems; Season Pass weekly 20 gems. Additional task rewards: Regular daily tasks 2x10=20 gems; Season Pass daily 2x20=40; Regular weekly tasks 2x20=40; Season Pass weekly tasks 2x50=100.",
  'Medium Confidence',[e326],['Numbers from r/DLS DLS24 beginner guide; DLS26 numbers may differ slightly.'],vol='Medium')
C("Career mode is widely considered too easy once the squad is fully upgraded (5+ goals/game common in Legendary division); Dream League Live (human opponents) is the primary endgame challenge.",
  'Medium-High Confidence',[e323])

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
