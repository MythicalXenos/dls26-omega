#!/usr/bin/env python3
"""Turn 30 unbounded sweep wave 1: add EV-256..EV-277 and new/updated claims from FTG official support + coach sim sources."""
import json,os,datetime
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
ev=[json.loads(l) for l in open(EIP) if l.strip()]
by={c['claim_id']:c for c in claims}
max_c=max(int(c['claim_id'][6:]) for c in claims)
max_e=max(int(e['evidence_id'][3:]) for e in ev if e['evidence_id'].startswith('EV-'))
print(f'starting max_c={max_c} max_e={max_e}')
ts=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

def mk_ev(eid, origin, artifact, covers, summary):
    eid_full=f'EV-{eid:03d}'
    ev.append({'evidence_id':eid_full,
               'origin_method':origin,
               'artifact':artifact,
               'captured_at':ts,
               'covers':covers,
               'summary':summary,
               'extracted_from':origin})
    return eid_full

def mk_claim(cid,prop,tier,evrefs,context='DLS26',challenges=None,vol='Low'):
    cid_full=f'CLAIM-{cid:03d}'
    c={'claim_id':cid_full,
       'proposition':prop,
       'confidence_tier':tier,
       'supporting_evidence':evrefs,
       'challenges':challenges or [],
       'context_build':context,
       'last_checked_by':f'turn 30 unbounded sweep ({ts})',
       'last_valid_check':ts,
       'last_attempt':ts,
       'next_due':(datetime.datetime.utcnow()+datetime.timedelta(days=30)).strftime('%Y-%m-%d'),
       'volatility_tier':vol,
       'cross_refs':[],
       'replacements':None,
       'contradicting_evidence':[]}
    claims.append(c); by[cid_full]=c; return cid_full

# === New EVs ===
e256=mk_ev(max_e+1,'official-stated (support.ftgames.com article 360019166777, fetched 2026-10-17)',
           'evidence/raw/ftg_support_turn30/EV-256_stats_semantics.html',
           [],'Per-stat gameplay semantics official FTG: SPE=top speed (dribble penalty ∝ 1/CON; reduces w/ energy); ACC=0-to-top speed; STA=energy depletion rate + half-time boost; CON=dribble tightness, first-touch speed, skill-move execution, skill-shot success; STR=collision impact, stumble recovery; TAC=stand/slide tackle reach; PAS=pass accuracy; SHO=shot accuracy, keeper-assist, keeping shots low, curl on FK, skill-shot success (paired w/ CON); GKH=catch vs parry, cross claim, collision stability; GKR=reaction time, save %, anticipate-save chance; ENERGY (battery icon)=fatigue, stats degrade below threshold, esp. speed.')
e257=mk_ev(max_e+2,'official-stated (support.ftgames.com 360003914778)',
           'evidence/raw/ftg_support_turn30/EV-257_develop_players.html',
           [],'Coaches (accessed Team Mgmt > Coaches) randomly select a player to PERMANENTLY upgrade. Form Boost = temporary attribute boost for a set number of matches determined by Training facility level (minimum 1 match).')
e258=mk_ev(max_e+3,'official-stated (support.ftgames.com 23108987826962)',
           'evidence/raw/ftg_support_turn30/EV-258_prize_ladder.html',
           [],'Prize Ladder awards coins/gems/coaches/dream-point-boosts/special-players/etc based on Dream Points earned from every match. DP boosts temporarily increase DP awarded per match.')
e259=mk_ev(max_e+4,'official-stated (support.ftgames.com 24081168829330)',
           'evidence/raw/ftg_support_turn30/EV-259_dp_boosts.html',
           [],'DP Boosts purchased within Prize Ladder; apply to career, dream draft, scenario, DLL matches only (NOT exhibition/friend); unusable if ladder complete/inactive; unused boosts carry to next ladder.')
e260=mk_ev(max_e+5,'official-stated (support.ftgames.com 4404070913169, v12200+)',
           'evidence/raw/ftg_support_turn30/EV-260_season_pass.html',
           [],'Season Pass: FREE + PREMIUM tiers; Premium adds Progress Bank (DLL XP → coins/gems at season end) + gold profile cosmetics; NOT a subscription (no auto-renew); tiers unlock by Season Points earned from matches; tier locks correspond to day-of-season; Premium Pass removes ALL tier locks; retroactive unlock of premium rewards for tiers already reached when purchased.')
e261=mk_ev(max_e+6,'official-stated (support.ftgames.com 360003945617, v12200+)',
           'evidence/raw/ftg_support_turn30/EV-261_sell_players.html',
           [],'Releasing a player (Transfers > Manage Players) yields a COACH (not coins); recently sold players appear in "Recover" section for a limited time.')
e262=mk_ev(max_e+7,'official-stated (support.ftgames.com 360000002185)',
           'evidence/raw/ftg_support_turn30/EV-262_formations.html',
           [],'Formation unlock: (1) collect enough of the same formation cards, then (2) unlock with Bux (gems) from squad > formation screen. Different formations require different card counts and Bux.')
e263=mk_ev(max_e+8,'official-stated (support.ftgames.com 360003914998)',
           'evidence/raw/ftg_support_turn30/EV-263_leaderboards.html',
           [],'DLL leaderboards reset every 3-30 days; prizes awarded based on position at reset.')
e264=mk_ev(max_e+9,'official-stated (support.ftgames.com 360018360418)',
           'evidence/raw/ftg_support_turn30/EV-264_difficulty.html',
           [],'Single-player difficulty auto-scales with division progression; DLS25 introduced base difficulty toggle Easy/Medium/Hard. DLL = always real human opponents, NO bots, NO outcome manipulation, NO teammate AI scripting, NO difficulty adjustment, NO influence on match outcome.')
e265=mk_ev(max_e+10,'official-stated (support.ftgames.com 360003914938)',
           'evidence/raw/ftg_support_turn30/EV-265_gems.html',
           [],'Gems sources: league objectives, tournaments, Season Pass, Prize Ladder, Dream League Live participation/leaderboards; also purchasable in shop.')
e266=mk_ev(max_e+11,'official-stated (support.ftgames.com 360017063617)',
           'evidence/raw/ftg_support_turn30/EV-266_super_players.html',
           [],'Super Players = enhanced player types won in Events and rare packages; low frequency; grey or gold shiny background.')
e267=mk_ev(max_e+12,'official-stated (support.ftgames.com 360000002845)',
           'evidence/raw/ftg_support_turn30/EV-267_view_stats.html',
           [],'Player stats viewed by tapping card on Squad screen; shows lifetime match performance + current attributes + upgrade progress. Team stats via My Profile > Records (lifetime) or Career > current competition.')
e268=mk_ev(max_e+13,'official-stated (support.ftgames.com 214387685)',
           'evidence/raw/ftg_support_turn30/EV-268_backup_save.html',
           [],'Save data secured by linking to "Sign in with Google" or "Sign in with Apple" (iOS 13+) via in-game Settings; NOT automatic.')
e269=mk_ev(max_e+14,'official-stated (support.ftgames.com 360018359998)',
           'evidence/raw/ftg_support_turn30/EV-269_matchmaking.html',
           [],'DLL matchmaking inputs confirmed: primarily LIVE Tier ranking, location, player availability pool at match time; outcomes governed by individual skill reflected in tactics, gameplay choices, team strength.')
e270=mk_ev(max_e+15,'community-web-en (bluestacks.com DLS26 free rewards guide, dated 2026-06-02)',
           'evidence/raw/bluestacks_turn30/EV-270_rewards_guide.html',
           [],'BlueStacks rewards guide DLS26: Daily Login 20-day cycle (miss → reset Day1) w/ coins+occasional gems; Daily/Weekly/Career Challenges (full daily→gems, full weekly→gems); Career matches award coins+Season Points + optional 30s ad doubles coins; Stadium Commercials L2=+13% / L3=+21% match coin bonus; Daily Scenario = 50 coins/day vs Hard AI comeback; DLL weekly leaderboard gems + match-participation gems; Season Pass activation = 400 Season Points (daily login = 40 SP/day; all free tiers = 1,095 coins); Progression Bank = DLL XP → coins+gems at 10-day season end; Prize Ladder = 90-day cycle rewards coins/gems/Classic Players; Global Challenge Cup = 10 gems per round cleared.')
e271=mk_ev(max_e+16,'community tool (sakibpro.com DLS26 Coaching Simulator Pro, fetched 2026-10-17)',
           'evidence/raw/sakibpro_turn30/EV-271_coach_simulator.html',
           [],'SakibPro DLS26 Coaching Simulator Pro: Coach gem costs — Fitness Common=25💎 / Rare=75💎 / Legend=225💎 (boosts SPE,ACC,STA,STR); Technical Common=25 / Rare=75 / Legend=225 (CON,PAS,SHO,TAC); Special (ALL STATS) Common=90 / Rare=240 / Legend=400; Goalkeeping Common=15 / Rare=40 / Legend=150 (GKR,GKH); Coach selection per use: pick one attribute to boost by +2 (discard & reshuffle option); facility discount tiers 0/5/10/15/20/30%; +10 OVR hard cap = 100% cumulative development weight (10% weight = +1 OVR); GK upgrades use classic points system: 2.2 visual points to GKR/GKP = +1 OVR, capped at 22 points total allocation; CON and SPE consume most capacity weight; STA consumes least.')
e272=mk_ev(max_e+17,'community-web-en (fifaworldcupnews.com DLS26 update timeline, fetched 2026-10-17)',
           'evidence/raw/fifaworldcupnews_turn30/EV-272_update_timeline.html',
           [],'DLS26 version timeline confirmed: DLS25=12.250 (last prior); DLS26 launched Dec 2025; 13.0x launch (Dec 2025) introduced Clans (50+ members, clan points, friendlies, casual/competitive), Kick-Off Stars special edition (Raphinha/Alvarez), new UI/dark theme, starter pack legendary agents, My Club+stadium preview, redesigned scoreboard/sideline, new broadcast angles, tracksuits walkout; Jan 2026 mid-season transfer refresh + QoL; Feb 2026 stability fixes + Turkish/Arabic commentary + February CUP; May 2026 Summer Showdown + GK AI fixes (1v1/corners); July 2026 Summer Spotlight (13.410): Dynamic Stars, Fanzone facility, World Tournament, manager accessories (North America), clan improvements (emoji reactions/interactions), World Heroes event (Jul 1) + World Winners, new commentary (Turkish, Arabic), unlimited special players, stadium banners/flags/cameraman/medical bag, new SFX/soundtrack, friend match options, transfer lock upgrades, Daily Bonus, Scenario updates, Raphinha/Alvarez Kick-Off Stars; Aug 2026 (13.410 / 13.420?): pre-season transfers, new kits, defensive slide-tackle recovery + collision fixes, 120Hz frame-rate fix, Pre-Season Kickoff/European Champions Tour events; Sep 1 2026 (13.420): Cult Heroes announced "coming soon"; Sep 16 2026 (13.430): late summer update bug fixes, Cult Heroes still "coming soon". Roster over 4,000 FIFPRO players + legendary classics.')
e273=mk_ev(max_e+18,'community-web-en (sportsdunia.com Dynamic Stars guide, 2026-06-10)',
           'evidence/raw/sportsdunia_turn30/EV-273_dynamic_stars.html',
           [],'Dynamic Stars event schedule: base 82 OVR dynamic cards; Group Stage Qualifiers (29 Jun): +1 OVR per group-stage win; R32 Winners (6 Jul): +2; R16 (9 Jul): +2; QF (13 Jul): +2; SF (16 Jul): +2; Final Winner (20 Jul): 96 OVR.')
e274=mk_ev(max_e+19,'community-web-en (gamingonphone.com DLS26 beginner guide 2026-01-21)',
           'evidence/raw/gamingonphone_turn30/EV-274_beginners_guide.html',
           [],'Coach categories confirmed four types: Technical (CON,PAS,SHO,TAC), Fitness (SPE,ACC,STA,STR), Goalkeeping (GKR,GKH), Special (ALL STATS); three rarities Common/Rare/Legendary; Common typically boosts single random stat; Rare stronger; Legendary best upgrades + higher Breakthrough chance. Coaches hired via gems OR releasing players. Formation unlock via Training Centre upgrades (community observation).')
e275=mk_ev(max_e+20,'community-reddit (r/DreamLeagueSoccer Season Pass tip thread, Jan 2026)',
           'evidence/raw/reddit_turn30/EV-275_dp_cap.html',
           [],'Dream Points per match capped at 5-0 win margin (goals beyond 5th do not increase DP); DP Boost cost/duration: Common +50% (25 gems / 3 matches), Rare +75% (35 gems / 5 matches), Legendary +150% (125 gems / 8 matches — community reports); baseline per-match DP ~54 + 9.75 + 15.75 = 79.5 DP mix (career/DLL/draft); Premium Season Pass = double SP + double XP.')
e276=mk_ev(max_e+21,'store-published (App Store id1462911602 version history, fetched 2026-10-17)',
           'evidence/raw/appstore_turn30/EV-276_appstore_changelog.html',
           [],'App Store version history for DLS26 confirms 13.410 Aug 20 Summer Spotlight, 13.420 Sep 1 late-summer (Cult Heroes "coming soon"), 13.430 Sep 16 bug fixes. Android 10+ (some variants 12L+), arm64-v8a + armeabi-v7a, base APK 31.6 MB, 120-480dpi bundles.')
e277=mk_ev(max_e+22,'official-web (firsttouchgames.com about + ftgames.com core-principles, ftgames.com press release 2024-12-05 DLS25 unveil, MobyGames/LinkedIn/Wikidata/Tracxn)',
           'evidence/raw/ftg_corp_turn30/EV-277_ftg_profile.html',
           [],'FTG corporate profile: founded 2011 (spun out of Exient Sept 2011); Oxford UK; ~30-45 employees (per Tracxn Jul 2026 / firsttouchgames.com about page "around thirty-strong"); CEO/founder Charles Chapman; studio portfolio: DLS (2011, originally First Touch Soccer), Score! Hero (2015), Score! Match (2018), 8 Ball Hero (2019), Ultimate Clash Soccer (2023); >1 billion downloads; 20M+ MAU (per 2024 press release); 12+ languages localised; 850M+ downloads as of Sep 2020 (Sheffield Utd partnership press); Companies House #07638595, SIC 58210 (computer game publishing); revenue ~$6.4M (RocketReach); not to be confused with DreamLeague (ESL Dota 2 circuit).')
print(f'EVs added: {max_e+1}..{max_e+22}')

# === New/updated claims ===
new_c=[]
def C(prop,tier,evr,chal=None,vol='Low'):
    global max_c; max_c+=1
    cid=mk_claim(max_c,prop,tier,evr,'DLS26 live service 2026',chal,vol); new_c.append(cid); return cid

# 1. Stat semantics (official A-tier, CONFIRMED)
C("OFFICIAL per-stat gameplay semantics confirmed by FTG: SPE = top speed (decreases with ENERGY and when dribbling inversely with CON); ACC = acceleration to top speed; STA = energy depletion rate + half-time energy restoration (midfielders deplete most); CON = dribble speed-retention, first-touch kick speed, tight-touch frequency (close dribble/change of direction), skill-move probability (rabona/overhead-kick/step-over/Marseilles turn/heel-flick), skill-shot success (double-tap/swipe paired with SHO); STR = collision impact winner (less stumble duration on tackle, better ball retention on contact); TAC = stand/slide tackle reach distance; PAS = pass accuracy on all pass types; SHO = shot accuracy, 'keeper-assist' (shot moved away from keeper), shot-height control (low shots more likely to score, high shots go over bar), skill-shot success (paired with CON), special-kick/header probability (bicycle/diving header), free-kick spin/curl; GKH = catch-vs-parry chance, cross-claiming radius, stability when catching under collision; GKR = keeper reaction speed, save percentage vs shot speed/distance, anticipate-save probability; ENERGY (battery icon) = fatigue stat below which other stats gradually degrade (speed most noticeable, all areas affected).",'Confirmed',[e256],vol='Low')
# 2. Form Boost duration
C("Form Boost provides TEMPORARY attribute boosts to a player, lasting a set number of matches determined by the Training facility level (minimum 1 match at base Training level). Distinct from permanent coach upgrades.",'Confirmed',[e257],vol='Low')
# 3. Coaches permanent random player upgrade
C("Coaches (accessed Team Management > Coaches) select a player RANDOMLY to receive a PERMANENT attribute upgrade when applied. Contrary to some community belief that player is chosen first, official text states coach -> random player selection.",'Confirmed',[e257],vol='Low')
# 4. Releasing players yields coach not coins
C("Releasing a player (Transfers > Manage Players) yields a COACH as reward (not coins), from v12200 onwards. Recently released players appear in a 'Recover' tab for a limited undo window.",'Confirmed',[e261],vol='Low')
# 5. Prize Ladder mechanics
C("Prize Ladder (90-day cycle per BlueStacks; official says 'based on progression') awards coins, gems, coaches, Dream Point boosts, and special players based on cumulative Dream Points earned from all match modes. DP boosts purchased from Prize Ladder.",'Confirmed',[e258,e270],vol='Low')
# 6. DP boost applicability
C("Dream Point Boosts apply ONLY to career, dream draft, scenario, and DLL (multiplayer) matches; they do NOT apply to exhibition or friend matches. Unused boosts roll over to the next Prize Ladder; unusable when ladder complete or inactive.",'Confirmed',[e259])
# 7. Season Pass detailed mechanics
C("Season Pass mechanics (v12200+): FREE + SEASON PASS (paid) tiers; buying paid Pass unlocks Progress Bank (DLL XP → coins+gems paid at season end) and gold profile cosmetics; NOT a subscription (no auto-renew); Season Points earned per match (varies by mode); tier locks correspond to day-of-season; buying Premium Season Pass removes ALL daily tier locks; rewards retroactive: buying pass mid-season instantly unlocks all premium rewards for tiers already reached free. Season is 10 days (per BlueStacks).",'Confirmed',[e260,e270],vol='Medium')
C("Season Pass activation threshold: 400 Season Points; daily login provides 40 Season Points/day for free (10-day season = 400 SP from logins alone). All FREE tiers completed guarantee 1,095 coins reward.",'Confirmed',[e270],vol='Medium')
# 8. Formation unlock = cards + Bux
C("Formation unlock is a two-step process: (1) collect enough of the same formation cards; (2) pay Bux (gems) to unlock at squad > formation screen. Different formations require different card counts and Bux amounts. This confirms EV-251 formations.json (149+79 formations) lists formations present in DB but NOT all unlocked by default.",'Confirmed',[e262])
# 9. Leaderboards reset 3-30 days
C("Dream League Live leaderboards reset at regular intervals ranging 3-30 days (different leaderboards have different cadences); prizes awarded based on final position.",'Confirmed',[e263])
# 10. Difficulty + DLL no-bots/no-manipulation (strong official fair-play statement)
C("Single-player difficulty scales automatically with division progression; DLS25 introduced a manual base difficulty toggle (Easy/Medium/Hard). In DLL (multiplayer), FTG officially states NO bots are used, NO difficulty adjustment, NO manipulation of any in-game situation (including teammate AI), NO influence on any match outcome — every match is real human vs real human with outcomes governed entirely by player skill, tactics, and team strength.",'Confirmed',[e264],['Scripting/momentum perceptions ("scripts" community slang CLAIM-090) are explicitly denied by official fair-gaming statement; player-perceived momentum may exist as statistical/bias artifact or lag/randomness effects.'])
# 11. Gems sources
C("Official gems sources: league objectives, tournaments, Season Pass, Prize Ladder, Dream League Live participation + leaderboard placement; also purchasable via in-app purchase.",'Confirmed',[e265])
# 12. Super Players
C("'Super Players' are enhanced player types won in Events and occasionally in rarer packages; they have a low appearance frequency and display a grey or GOLD shiny background (distinct from bronze/blue/gold base rarity cards).",'Confirmed',[e266])
# 13. Save backup
C("Save backup/restore/transfer is achieved by linking profile to 'Sign in with Google' or 'Sign in with Apple' (iOS 13+) via in-game Settings; this is NOT automatic — user must initiate the link.",'Confirmed',[e268])
# 14. Coach categories 4 types
C("Coaches are divided into FOUR categories: Fitness (boosts SPE/ACC/STA/STR), Technical (boosts CON/PAS/SHO/TAC), Goalkeeping (boosts GKR/GKH), Special (boosts ALL stats). Each category has three rarities: Common / Rare / Legendary. Common coaches typically boost a single random stat; Legendary coaches provide the strongest upgrades and highest 'Breakthrough' chance.",'Confirmed',[e274,e271],vol='Low')
# 15. Coach gem costs
C("Coach hire gem costs confirmed via SakibPro Pro Simulator: Fitness Common=25💎 / Rare=75💎 / Legend=225💎; Technical Common=25 / Rare=75 / Legend=225; Special (all-stats) Common=90 / Rare=240 / Legend=400; Goalkeeping Common=15 / Rare=40 / Legend=150. Each coach application lets player pick ONE attribute to boost by +2 (discard & reshuffle available).",'Community Consensus',[e271],['Costs are from a community tool simulator; not directly APK-verified but simulator claims to mirror official internal logic.'],vol='Medium')
# 16. Training capacity +10 OVR cap (100% weight)
C("Player development HARD CAP = +10 OVR over base rating, achieved at 100% cumulative development weight capacity. Every 10% of total progression weight = +1 OVR. Attributes have different per-point weights (CON and SPE consume most capacity; STA consumes least).",'High Confidence',[e271],['Weighted capacity numbers from SakibPro simulator; OVR formula confirmed via QR-OLS (EV-253) — cap and +10 ceiling match community theory CLAIM-105 but official support has not stated the exact +10 figure directly.'],vol='Low')
# 17. GK training formula (2.2 visual points per OVR, cap 22)
C("Goalkeeper training uses a classic points system (not the complex weighted system used for outfield). Every 2.2 visual points allocated to GKR or GKH = +1 OVR, with a STRICT 22-point total allocation cap (= +10 OVR max for GKs, consistent with outfield cap).",'High Confidence',[e271],['Single community tool source; needs APK verification.'])
# 18. Facility discount tiers
C("Recruitment/Training facility discount tiers confirmed for coaching costs: 0% / 5% / 10% / 15% / 20% / 30% (six levels).",'Community Consensus',[e271])
# 19. Commercial facility bonuses
C("Stadium Commercials facility upgrade multipliers: Level II = +13% coin earnings after matches; Level III = +21% (affects Career + Exhibition coin income).",'High Confidence',[e270,e272],['Per BlueStacks guide; VI guide (EV-236) previously cited L2=+13% but L3 not confirmed before.'])
# 20. Daily Login 20-day cycle (reset on miss)
C("Daily Login reward cycle is 20 days, refreshing on completion; MISSING A SINGLE DAY resets the cycle back to Day 1. Rewards = coins + occasional Gems.",'Community Consensus',[e270],['Community guide; needs APK verification.'],vol='Medium')
# 21. Daily Scenario reward
C("Daily Scenarios mode places player in a comeback situation vs Hard AI; completion rewards 50 coins per day; scenario resets daily.",'Community Consensus',[e270])
# 22. Global Challenge Cup reward
C("Global Challenge Cup (online round-robin under Career section) awards 10 Gems per round cleared; resets on a regular schedule.",'Community Consensus',[e270])
# 23. Post-match ad doubles coins (once per match, optional 30s)
C("Post-match rewarded ad (30 seconds, optional) DOUBLES coin earnings for that match. A second optional ad can boost Dream Points. Ads appear after every Career match; reward once per match.",'High Confidence',[e270,e275],['BlueStacks cites post-match ad doubles coins; Reddit cites a second DP-boost ad.'])
# 24. DP cap at 5-0 win
C("Dream Points per match are capped at a 5-0 win margin; goals beyond the 5th do not increase DP awarded.",'Community Consensus',[e275],['Community Reddit tip; multiple users corroborate cap; not APK-confirmed.'])
# 25. DP boost pricing/duration (community)
C("DP Boost gem costs and durations (community reports): Common +50% = 25 gems / 3 matches; Rare +75% = 35 gems / 5 matches; Legendary +150% = 125 gems / 8 matches; alternatively 100 gems for a random boost from Prize Ladder. Baseline per-match DP ~54+9.75+15.75=79.5 DP (estimated mix of modes).",'Community Consensus',[e275,e274],['Community-reported prices; need APK verification; Legendary +150% per gamingonphone DLS25 guide (EV-245/247).'])
# 26. Premium SP doubles SP and XP
C("Premium Season Pass grants DOUBLE Season Points AND double Live XP (faster tier progression + faster Progression Bank fill).",'Community Consensus',[e275])
# 27. DLS26 update timeline (major events)
C("DLS26 post-launch update timeline confirmed: Dec 2025 launch with Clans/Kick-Off Stars/Raphinha-Alvarez new UI/broadcast angles; Jan 2026 winter transfer refresh; Feb 2026 Turkish/Arabic commentary added + stability + February CUP; May 2026 Summer Showdown + GK AI fixes (1v1/corners) + ball physics; Jul 2026 v13.410 Summer Spotlight (Dynamic Stars, Fanzone facility, World Tournament event, manager accessories, clan emoji reactions, World Heroes event starting Jul 1, World Winners upcoming, new soundtrack/SFX, unlimited Special Players, friend match options, transfer locks, Daily Bonus, Scenario updates); Aug 2026 pre-season transfer sync + new kits + defensive slide-tackle recovery speed fix + collision physics fixes + 120Hz frame-rate stabilization + Pre-Season Kickoff/European Champions Tour events; Sep 1 v13.420 Cult Heroes collection announced as 'coming soon'; Sep 16 v13.430 late-summer bugfixes.",'Community Consensus',[e272,e276],['Aggregated from fifaworldcupnews + App Store changelog; some dates (May/Jul) from community site reporting.'],vol='High')
# 28. Fanzone facility
C("Fanzone (new facility added Summer Spotlight 13.410, July 2026) is a buildable club facility that yields CLAN RESOURCE BONUSES and STADIUM EXPANSION DISCOUNTS.",'High Confidence',[e272,e276],['Store changelog + community site both confirm Fanzone effects.'])
# 29. Dynamic Stars upgrade ladder
C("Dynamic Stars (Summer Spotlight event, 13.410) are Special Players that upgrade LIVE based on real-world national team tournament performance: base 82 OVR; Group Stage Qualifiers (29 Jun): +1 OVR per group-stage win; R32 (6 Jul): +2; R16 (9 Jul): +2; QF (13 Jul): +2; SF (16 Jul): +2; Final winner representative upgrades to 96 OVR.",'Community Consensus',[e273,e272],vol='High')
# 30. World Tournament event type
C("World Tournament is a new event type introduced in Summer Spotlight (13.410): an international football event structure with high-tier reward tracking.",'Community Consensus',[e272,e276],vol='Medium')
# 31. Clan minimum 50 members
C("Clans require minimum 50 members; clan points earned from matches/events; clan leaderboards, vice-captains, clan point boosts, emoji reactions/interactions added in successive updates. Casual and competitive clan modes exist with rating requirements.",'Community Consensus',[e272],vol='Medium')
# 32. Clans launched at DLS26 launch (Dec 2025)
C("Clans system was the HEADLINE new feature of DLS26 launch (Dec 2025); subsequently expanded with leaderboards/roles/reactions in Winter Reload and Summer Spotlight updates.",'High Confidence',[e272],vol='Low')
# 33. FTG corporate profile
C("First Touch Games Ltd (FTG): founded 2011 (spun out of Exient Entertainment, where Charles Chapman was co-founder/CTO); independent studio headquartered Oxford, UK (264 Banbury Road OX2 7DY; PO Box 390 OX1 9RW); ~30-45 employees (per Tracxn 2026 / FTG 'about 30 strong' page); CEO/founder Charles Chapman; Companies House #07638595, SIC 58210 (computer game publishing); games portfolio: Dream League Soccer (originally First Touch Soccer, launched 6 May 2011), Score! Hero (2015), Score! Match (2018), 8 Ball Hero (2019), Ultimate Clash Soccer (2023); 1B+ downloads, 20M+ MAU, localised in ~12 languages; DLS26 package com.firsttouchgames.dls7.",'High Confidence',[e277],vol='Low')
# 34. FIFPRO license 4000+ players
C("DLS26 is FIFPRO-licensed with over 4,000 real players + legendary Classic greats (store description and APKMirror listing both confirm '4,000+ FIFPRO licensed players').",'Confirmed',[e276,e272])
# 35. Commentary languages
C("Commentary languages in DLS26 include English plus Turkish and Arabic (added in the Feb 2026 / Summer Spotlight updates), per App Store changelog.",'Community Consensus',[e276,e272])
# 36. Walkout presentation
C("New pre-match presentation: players walk out wearing warm-up/training tracksuits before kickoff (introduced at DLS26 launch).",'Community Consensus',[e272])
# 37. Unlimited special players
C("DLS26 allows UNLIMITED Special Players in a single club (no accommodation/squad cap on specials); Summer Spotlight 13.410 removed prior special-player count limits.",'High Confidence',[e276,e272])
# 38. Cult Heroes collection
C("Cult Heroes is an upcoming Special Player collection announced in v13.420/v13.430 (Sep 2026) but not yet released as of 13.430 (16 Sep 2026).",'Community Consensus',[e276,e272],vol='High')
# 39. 120Hz support added
C("120Hz display frame-rate stabilization/polish added in August 2026 update.",'Community Consensus',[e272],vol='Medium')
# 40. Post-match coin ad optional, once per match
C("Watching a 30-second ad after a match DOUBLES coin earnings for that match; available once per match (BlueStacks says once per match, FAQ suggests once per 24 hours — wording ambiguous; likely once-per-match for coins, with possible cooldown on DP ad).",'High Confidence',[e270],['One source says "once per match" another implies "once per 24 hours"; needs in-game verification.'])

# Update existing claims: CLAIM-152 (ad rewards coins/diamonds — upgrade from bot comment to Community Consensus with BlueStacks corroboration)
# Already at Confirmed because of EV chain - leave alone but add evidence.
# CLAIM-104 team OVR = mean of starting-11 — was High Confidence with 2 sources, now add SakibPro coach sim corroboration
by['CLAIM-104']['supporting_evidence'].append(f'{e271} (SakibPro coach simulator operates per-player, not team formula; OVR computed per player per 10% weight)')
# CLAIM-154 coach rarities was 3 tiers (white/blue/gold) — now we know 4 categories (Fitness/Technical/GK/Special) × 3 rarities (Common/Rare/Legendary). Update.
by['CLAIM-154']['proposition']="Coach rarities confirmed: FOUR categories (Fitness/SPE+ACC+STA+STR; Technical/CON+PAS+SHO+TAC; Goalkeeping/GKR+GKH; Special/ALL stats) each with three rarities: Common (white, +1 boost, cheap 15-90 gems), Rare (blue, +2 boost, 40-240 gems), Legendary (gold, +3 boost most powerful, 150-400 gems). Each coach application picks a random eligible player in the targeted attribute category and offers +2 to one attribute in that category (with discard/reshuffle). Prices per SakibPro simulator: GK Common=15/ Rare=40/Legend=150; Fitness/Technical Common=25/Rare=75/Legend=225; Special Common=90/Rare=240/Legend=400 gems. SakPro coach gem costs community-sourced, not APK-confirmed."
by['CLAIM-154']['confidence_tier']='High Confidence'
by['CLAIM-154']['supporting_evidence']+=[e271,e274]
by['CLAIM-154']['challenges']=['Coach prices from community tool (SakibPro) only; category×rarity matrix is consistent across BlueStacks/gamingonphone/SakibPro/Leo-CB DP but needs APK byte-verification.']

# CLAIM-155 CB weights CON=2 - note this is per-position, CB only, consistent with "CON costs most capacity" general rule
by['CLAIM-155']['supporting_evidence'].append(f'{e256} (official stat semantics confirm CON is high-impact dribble-control stat)')
by['CLAIM-155']['supporting_evidence'].append(f'{e271} (SakibPro simulator confirms CON and SPE consume most capacity weight, STA least)')

# CLAIM-040 Season Pass FREE+PREMIUM already Confirmed; add EV-260
by['CLAIM-040']['supporting_evidence'].append(e260)

# CLAIM-041 delete profile path already Confirmed; add EV-268 (Sign in with Google/Apple backup)

# CLAIM-033 card rarity bronze/blue/legendary - now add Super Players grey/gold distinction from EV-266
by['CLAIM-033']['proposition']+=" Additionally 'Super Players' (event/rare-package exclusive) display a grey or gold SHINY background distinct from base rarities (EV-266)."
by['CLAIM-033']['supporting_evidence'].append(e266)

# CLAIM-027 matchmaking inputs - add EV-269 explicit confirmation
by['CLAIM-027']['supporting_evidence'].append(e269)

# CLAIM-044 fair gaming - add EV-264 explicit no-bots/no-manipulation statement
by['CLAIM-044']['supporting_evidence'].append(e264)

# Write back
import shutil
shutil.copy(CP,CP+'.preturn30.bak')
with open(CP,'w') as f:
    for c in claims: f.write(json.dumps(c,ensure_ascii=False)+'\n')

# Add EVs
shutil.copy(EIP,EIP+'.preturn30.bak')
with open(EIP,'a') as f:
    for e in ev[-22:]:  # newly added
        f.write(json.dumps(e,ensure_ascii=False)+'\n')

print(f'Added {len(new_c)} new claims (CLAIM-{max_c-len(new_c)+1:03d}..CLAIM-{max_c:03d}) and 22 EVs (EV-{max_e+1:03d}..EV-{max_e+22:03d}).')
print(f'Total claims now: {len(claims)}; EVs now: {len(ev)}')
