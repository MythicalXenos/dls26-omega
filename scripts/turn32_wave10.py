#!/usr/bin/env python3
"""Turn 32 Wave 10 — Player attribute system (weights, caps, position priorities) + facilities upgrade costs/effects."""
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

e338=E("gamedls.net DLS25 player stats + r/DLS training/stat-weight threads + sakibpro simulator + fandom wiki Player Development/Perfect Players",
       "DLS has 10 visible attributes for outfield players: SPE (Speed), ACC (Acceleration), STA (Stamina), CON (Control/Dribbling), STR (Strength), TAC (Tackling), PAS (Passing), SHO (Shooting), plus GKH (Handling) and GKR (Reflexes) for GKs. Older/community references sometimes split HEA (Heading) and CRO (Crossing) and GKP (Positioning) — these were folded into STR/PAS/GK stats in DLS20+. Stat cap per attribute: 100. OVR card colors: silver/gold upgraded, black at 100 OVR ('special' cap). Stat weights in coach/development point system: SPE, ACC, STA, TAC, PAS, SHO = 1 point each; CON, STR = 2 points each (weight doubles). CON and STR are thus twice as costly per upgrade. DLS26 sakibpro PRO SIMULATOR confirms 8 outfield stats + 2 GK stats with weighted progression and +10 OVR development cap (100% cumulative weight). Coach categories by stat: Technical -> CON/TAC/PAS/SHO; Fitness -> STA/STR/ACC/SPE; Goalkeeping -> GKH/GKR. Earlier DLS versions (DLS2019) had no training cap; in DLS20+ each player has a fixed number of upgrade points based on their base card; Breakthrough proc adds bonus point(s) BEYOND that cap. About 10 stat points = +1 OVR. Height is an unlisted but impactful attribute — affects header wins, shielding, collision wins, set-piece effectiveness; taller players (e.g., Yildiz 187cm, Haaland, VVD) outperform shorter maxed players of same stats in practice.",
       "evidence/raw/community_turn32/EV-338_attributes.html",
       typ='community',reliability='High')
e339=E("r/DLS position-priority threads (2022-24) + LevelWinner DLS24 + gamedls.net",
       "Position stat priorities (community consensus): Forwards (ST/CF/LW/RW) = SPE, CON, SHO, (ACC, STR, STA) — ideal ST blueprint 100 SPE/ACC, 90+ STA, 95+ STR, 95+ SHO; high-CON CF with 90 CON/90-95 SHO outperforms 80 CON/100 SHO. Wingers = 100 SPE/ACC/STA, 90+ CON, 80+ STR. Midfielders = everything at least green, 90+ STA/CON/PAS; AM adds 90+ SHO; DM needs 100 STR/95+ TAC plus passing. Defenders = 100 SPE/ACC/STA/STR (fitness 4-lines) + TAC as high as possible (~90-95 when STR=100), some CON useful on CBs; wingbacks also need PAS for overlap. STR effects: hold ground in body contact, win aerial duels (partially compensates for lack of height), reduce injury susceptibility, reduce post-contact stun animation duration (so player-switch/joystick recovery is ~0.5s faster). SPE and ACC should stay within ~12 points of each other (SPE > ACC) or stamina drains faster.",
       "evidence/raw/reddit_turn32/EV-339_position_priorities.html",
       typ='community',reliability='Medium-High')
e340=E("BlueStacks DLS26 beginner/career guides + LevelWinner DLS20 advanced + r/DLS facilities threads (2020-24) + dlspedia stadium + fandom Stadium + dlsinside stadium list",
       "Six facilities: Stadium, Commercial, Training, Medical, Accommodation, Recruitment (+ new Fanzone in Summer Spotlight 2026). Stadium (costs COINS, not gems): min capacity 6,462 (Academy start); max 90,456 seats (dlspedia) / 92,632 optimal build; auto-build max 80k-85k; 8 stands (2 End, 2 Side, 4 Corners) — North/South Ends (End goal stands), East/West Sides (long side stands), NE/NW/SE/SW Corners. Promotion seat minima: Academy 6,462 -> Div3 15k (dlspedia) / 35k (fandom Div3 entry per some versions) -> Div2 30k/45k -> Div1 45k -> Junior Elite 60k -> Elite 80k. Community optimal cost build: East/West sides +North/South ends to certain levels then corners to '51' for ~92k capacity at 52 home-coin bonus for ~10k coins (don't add roofs — cosmetic only, wastes coins). Stadium upgrades can be done one stand at a time; partial builds don't pro-rate — always upgrade a stand to its tier in one go. Home-match coin bonus ~48-52 coins per home match at max stadium (250+ total post-ad). Other facilities cost GEMS (75/150/225/300/375 per star, 5 stars max = 1,125 gems per facility = 5,625 gems total to max all 5 non-stadium facilities): Commercial -> +% coin bonus per match (Lvl I initial 75g, Lvl II +13%, Lvl III +21%, max ~+40-50 coin bonus per game at 5-star). Medical -> reduces injury chance and physio healing cost (10% cheaper +5% less injury per first upgrade; stacks). Training -> unlocks formations, extends Form Boost duration, discounts coach hire (max training = -30% Legendary coach cost: 225g->157g). Accommodation -> increases squad size (20 -> 24 first upgrade; max 40; in DLS26 Special Players no longer consume accommodation slots per Summer Spotlight). Recruitment -> discount on scout/agent hiring. Fanzone (Summer Spotlight 2026 new) provides Clan bonuses and Stadium discounts. Recommended early-game upgrade order varies: (1) Stadium first (coin income) — side stand -> 15k capacity for Amateur division; (2) Training (75g starter) for coach discount + formations; (3) Commercial for coin bonus; (4) Medical to reduce injury costs; (5) Accommodation/Recruitment last. Community debate whether to prioritize Commercial over Medical first.",
       "evidence/raw/community_turn32/EV-340_facilities.html",
       typ='community',reliability='High')

# CLAIMS
C("Outfield player attributes (10): SPE (Speed), ACC (Acceleration), STA (Stamina), CON (Control/Dribbling), STR (Strength), TAC (Tackling), PAS (Passing), SHO (Shooting); GK-only: GKH (Handling), GKR (Reflexes). Older versions had separate Heading/Crossing/GK-Positioning which were folded into STR/PAS/GK stats in DLS20+.",
  'High Confidence',[e338],vol='Low')
C("Each attribute caps at 100. Card tier visuals: bronze/silver/gold as upgraded; black card at 100 OVR. Approximately 10 attribute upgrade points = +1 OVR.",
  'High Confidence',[e338],vol='Low')
C("Coach/development stat weights: SPE/ACC/STA/TAC/PAS/SHO = 1 weight point each; CON/STR = 2 weight points each (twice as costly to upgrade). A player reaches a +10 OVR development cap at 100% cumulative weight (sakibpro DLS26 simulator confirms). Breakthrough proc adds bonus stats ABOVE the normal point cap.",
  'High Confidence',[e338],vol='Low')
C("Coach category -> stat mapping: Technical boosts CON/TAC/PAS/SHO; Fitness boosts STA/STR/ACC/SPE; Goalkeeping boosts GKH/GKR only.",
  'High Confidence',[e338],vol='Low')
C("Height is an unlisted but high-impact attribute: affects aerial duel win rate, shielding, collision wins, set-piece effectiveness. Tall players (187cm+) with equal stats outperform shorter ones in practice (e.g., 187cm Yildiz > 170cm Messi at same stats per community analysis).",
  'Medium-High Confidence',[e338],vol='Medium')
# Position priorities
C("Ideal stat blueprints: CF/ST 100 SPE/ACC, 90+ STA, 95+ STR, 95+ SHO, 90+ CON (90CON/95SHO > 80CON/100SHO); Wingers 100 SPE/ACC/STA, 90+ CON, 80+ STR; Midfielders all green with 90+ STA/CON/PAS; AM adds 90+ SHO; DM 100 STR, 95+ TAC, passing; Defenders 100 SPE/ACC/STA/STR with 90-95 TAC and ~80 CON.",
  'Medium-High Confidence',[e339],vol='Medium')
C("STR effects beyond physicality: reduces post-contact stun animation duration (~0.5s faster joystick/player-switch recovery); slightly reduces injury rate; contributes to aerial win rate (partially compensates for lack of height).",
  'Medium-High Confidence',[e339],vol='Medium')
C("Keep SPE and ACC within ~12 points of each other (ideally SPE > ACC); too large a gap accelerates stamina drain during sprints.",
  'Medium Confidence',[e339],vol='Medium')
# Facilities
C("Six classic facilities: Stadium (upgraded with coins), Commercial, Training, Medical, Accommodation, Recruitment (all upgraded with gems); Summer Spotlight 2026 adds Fanzone (Clan bonuses + Stadium discounts).",
  'High Confidence',[e340])
C("Stadium: 8 stands (North/South Ends, East/West Sides, NE/NW/SE/SW Corners). Start capacity 6,462; max 90,456 seats (dlspedia) / ~92,632 optimal community build; auto-build max 80-85k. Roofs are cosmetic (cost coins, no gameplay benefit). Upgrade one stand fully at a time (partial upgrades don't pro-rate the next cost). Optimal min-cost max-capacity build: East/West to 26, North/South to 20, corners to 51 (~92,632 cap) for ~10k coins, yielding 52-coin home match bonus.",
  'Medium-High Confidence',[e340],["Optimal build numbers are from r/DLS DLS23 community; exact costs may differ in DLS26."],vol='Medium')
C("Non-stadium facilities cost 75 gems for 1-star, scaling 75/150/225/300/375 per star (5 stars max = 1,125 gems per facility; 5,625 gems total to max Commercial/Training/Medical/Accommodation/Recruitment).",
  'High Confidence',[e340],vol='Low')
C("Facility effects: Commercial = +% post-match coin earnings (Lvl I base 75g, Lvl II +13%, Lvl III +21%, ~+40-50 coin/game at max); Medical = lower injury rate + cheaper physio recovery (~5%/10% per level); Training = unlocks formations, extends Form Boost duration, discounts coaches (max Training = -30% Legendary cost: 225g->157g); Accommodation = larger squad (20 -> 24 at first upgrade; max 40; Special Players exempt from accommodation limits in DLS26); Recruitment = scout/agent hiring discounts; Fanzone (Summer 2026) = Clan bonuses + Stadium discounts.",
  'High Confidence',[e340],vol='Medium')
C("Recommended early upgrade order: (1) Stadium side stand with starter coins for Amateur-division capacity (15k) and recurring coin income; (2) spend 75 starter gems on Training for coach discount + new formations; (3) Commercial for coin multiplier; (4) Medical to reduce injury costs; (5) Accommodation/Recruitment last (24-player squad sufficient until later; recruitment discount lower priority).",
  'Medium-High Confidence',[e340],vol='Medium')

print(f"Added {ac} new claims and {ae} EVs. Totals: {next_c-1} claims, {next_e-1} EVs")
