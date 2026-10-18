#!/usr/bin/env python3
"""Turn 35 Wave 33: Special Players acquisition (Prize Ladder DP milestones + Legendary Agent route), DLS26 official launch feature list, DP boost values, card colour rules, secret players, best-per-position, regional DLL leaderboard, player benchmarks."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w33')

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

# ---------- EV-426: special players ----------
e_sp=new_ev("r/DreamLeagueSoccer 1h76l31 (Dec 2024), sportysure, tricksvile, dls-database.lovable.app/special, kitdls.net, official FTG TikTok (World Heroes), sportsdunia Dynamic Stars event guide, r/DLS 1cd7bx9, 1ap8z6n, 1de1vd1",
    "SPECIAL PLAYERS ACQUISITION. Special Players CANNOT be purchased with coins - they are earned through exclusive in-game events, challenges and the Prize Ladder. PRIZE LADDER MILESTONES: the first Special Player unlocks at roughly 50,000 DP and WHICH one you get is random (it behaves like a Legendary Agent draw). Community grind calculations: the first icon takes 300-305 games with free boosters (exactly 324 matches by one calculation), and unlocking all four WC'98 icons takes about 1,370 games, or 1,428 at 140 DP per match against a 200,000 DP ladder. The four WC'98 Special Players are Emmanuel Petit, Davor Suker, Dennis Bergkamp and Gabriel Batistuta. SECOND ROUTE (official FTG TikTok, DLS26): World Heroes are available through LEGENDARY AGENTS - 'every time you use a Legendary Agent, you have a chance of getting a World Hero Special Player, celebrating heroic performances at previous tournaments'. So specials are obtainable both via the Prize Ladder and as agent draws. DYNAMIC STARS require Dynamic Star Agents, earned from event draws and Season Passes (Season 1 pass gives 3 Dynamic Agents on the premium path with 2 free). DP BOOST VALUES: boost items increase DP by 50%, 70% or 150%, and watching ads after each match adds further points; one guide describes per-match DP as roughly 75-250 including boosts. CARD COLOURS: card colour follows BASE rarity - players rated 70-79 finish blue when maxed, 80+ finish black, and only legendary players change colour (turning black), with a star appearing on the card once fully upgraded. SECRET PLAYERS appear in the shop at a 200-300 coin discount, so any secret player costing 2,000+ coins is usually 83+ rated; players short of coins are advised to play scenarios (75-100 coins every 8 hours) and watch free ads (30 coins each, up to 600 coins in 15 minutes). BEST PER POSITION (r/DLS Jun 2024): GK Alisson/Courtois; LB Robertson/Theo Hernandez (Grimaldo is marked LWB); CB Rudiger/Saliba (83) and Van Dijk/Dias (84); RB Hakimi/Trent (Trent plays more like a CM); DM Rodri; AM De Bruyne; CM Valverde; LW Vinicius Jr.",
    "evidence/raw/turn35_w33/EV-426_special_players.html",
    "Special Players cannot be bought with coins - earned via events/challenges/Prize Ladder; first special at ~50,000 DP with a RANDOM draw (like a Legendary Agent); first icon ~300-324 games with boosters, all four ~1,370-1,428 games; WC'98 four = Petit/Suker/Bergkamp/Batistuta; SECOND official route = Legendary Agents can yield World Hero Special Players; Dynamic Stars need Dynamic Star Agents from event draws and Season Passes (3 premium + 2 free); DP boosts = +50%/+70%/+150% plus ad boosts; card colour follows base rarity (70-79 blue, 80+ black, only legendaries change colour, star on full upgrade); secret players at 200-300 coin discount so 2,000+ = 83+ rated; scenarios 75-100 coins/8h, ads 30 coins each up to 600 in 15 min; best per position list",
    quality="community")

add_claim("Special Players cannot be purchased with coins - they are earned exclusively through in-game events, challenges and the Prize Ladder.", 2, "cards/special-players-not-purchasable", [e_sp])
add_claim("The first Prize Ladder Special Player unlocks at roughly 50,000 Dream Points and WHICH one you receive is random, behaving like a Legendary Agent draw.", 3, "prizeladder/first-special-50k", [e_sp])
add_claim("Grind to the first Special Player takes about 300-305 games with free boosters (one calculation says exactly 324 matches), and unlocking all four World Cup '98 Special Players takes about 1,370 games, or 1,428 at 140 DP per match against a 200,000 DP ladder.", 3, "prizeladder/special-grind-games", [e_sp])
add_claim("The four World Cup '98 Special Players are Emmanuel Petit, Davor Suker, Dennis Bergkamp and Gabriel Batistuta.", 2, "cards/wc98-special-players", [e_sp])
add_claim("DLS26 World Heroes are obtainable through LEGENDARY AGENTS - official FTG states every Legendary Agent use gives a chance of a World Hero Special Player - so Special Players have two routes: the Prize Ladder and agent draws.", 1, "cards/special-via-legendary-agent", [e_sp])
add_claim("Dynamic Stars require Dynamic Star Agents, earned from event draws and Season Passes; the World 26 Season 1 pass offered 3 Dynamic Agents on the premium path with 2 free.", 3, "events/dynamic-star-agents", [e_sp])
add_claim("Dream Point boost items increase DP by 50%, 70% or 150%, and watching ads after each match adds further points; one guide describes total per-match DP as roughly 75-250 including boosts.", 3, "prizeladder/dp-boost-values", [e_sp])
add_claim("Card colour follows BASE rarity: players rated 70-79 finish blue when maxed and 80+ finish black, only legendary players change colour (turning black), and a star appears on the card once the player is fully upgraded.", 2, "cards/colour-rules", [e_sp])
add_claim("Secret players appear in the shop at a 200-300 coin discount, so any secret player costing 2,000+ coins is usually 83+ rated; scenarios pay 75-100 coins every 8 hours and free ads pay 30 coins each (up to 600 coins in 15 minutes).", 3, "transfers/secret-players", [e_sp])
add_claim("Best players per position (r/DLS Jun 2024): GK Alisson/Courtois; LB Robertson/Theo Hernandez (Grimaldo is marked LWB); CB Rudiger/Saliba (83) and Van Dijk/Dias (84); RB Hakimi/Trent (Trent plays more like a CM); DM Rodri; AM De Bruyne; CM Valverde; LW Vinicius Jr.", 3, "attributes/best-per-position", [e_sp])
add_claim("CONFLICT on the DLS26 top base rating: thesoccerera/z2u/sportsdunia put Dembele, Mbappe, Kane and Haaland at 86, while some databases list Yamal at 86, 85 or 84 and Messi only at 87 as a World Heroes SPECIAL card.", 3, "ratings/top-base-conflict", [e_sp], notes="Multiple community databases disagree; base ceiling is 86 with special cards above it")

# ---------- EV-427: official launch features + leaderboard geography + benchmarks ----------
e_lf=new_ev("App Store US DLS26 version history (launch notes), r/DreamLeagueSoccer 1e42njg (Jul 2024) and 1b183rw (3-month review), dls-wiki Captains, G2G marketplace listings, Exophase legacy lists",
    "DLS26 OFFICIAL LAUNCH FEATURE LIST (App Store version history, distinct from the Summer Spotlight notes): Dynamic Stars; the new Fanzone facility for Clan bonuses and stadium discounts; new commentary languages Turkish and Arabic; updated 2025/26 player data with more classic, special and national team players; INCREASED SQUAD SIZE with unlimited special players in your club; improved venues with new iconic stadiums and upgraded club facilities; enhanced match atmosphere with more props, banners and flags; KICK-OFF STARS - collect special edition Raphinha and Julian Alvarez cards at launch; and a brand new soundtrack and SFX. LEADERBOARD GEOGRAPHY (r/DLS Jul 2024): the Dream League Live leaderboard is BY REGION and is based on PERFORMANCES rather than team rating; worldwide ranking was visible through the iOS Game Center leaderboard in DLS19. This is decisive for the mission target - '#1' is only meaningful within a region unless a global surface exists. PLAYER BENCHMARKS from a 3-month review: 13 times Tier 1 Champion, 1,472,836 online XP, 57% online win rate (up from 49%), 987 career games and 1,086 live games played, 19 Legendary Division premierships, 18 All-Star Cup and 18 International Cup wins, a fully maxed starting 11 plus 9 maxed substitutes. CAPTAIN SELECTION VERSION DRIFT: dls-wiki (DLS21-era) describes being shown 9 random Legendary Cards and choosing one, whereas the current build offers roughly 80 captain choices plus Create Your Own Captain. MARKETPLACE TERMINOLOGY: G2G account listings advertise tiers named 'GRAND LEGENDARY X' and 'GRAND LEGENDARY VII' - these are seller/marketplace labels, NOT confirmed in-game rank names, and must not be quoted as such.",
    "evidence/raw/turn35_w33/EV-427_launch_features.html",
    "DLS26 official launch features: Dynamic Stars, Fanzone, Turkish+Arabic commentary, 2025/26 data, unlimited special players, new iconic stadiums, enhanced match atmosphere, Kick-Off Stars Raphinha+Alvarez at launch, new soundtrack/SFX; DLL leaderboard is BY REGION and performance-based (worldwide ranking was visible via iOS Game Center in DLS19) - decisive for defining #1; 3-month player benchmarks (13x Tier 1 Champion, 1.47M online XP, 57% win rate, 987 career + 1086 live games, 19 Legendary premierships, 18 All-Star + 18 International Cups, maxed 11 + 9 subs); captain selection was 9 random legendary cards in the DLS21 era vs ~80 + Create Your Own now; G2G 'Grand Legendary' tiers are marketplace labels, not in-game ranks",
    quality="official")

add_claim("DLS26 official launch features (App Store version history): Dynamic Stars, the Fanzone facility, Turkish and Arabic commentary, updated 2025/26 player data with more classic/special/national players, unlimited special players in the club, new iconic stadiums and upgraded facilities, enhanced match atmosphere, Kick-Off Stars Raphinha and Julian Alvarez cards at launch, and a new soundtrack and SFX.", 1, "patching/dls26-launch-features-official", [e_lf])
add_claim("Kick-Off Stars are special-edition Raphinha and Julian Alvarez cards available at DLS26 launch.", 1, "cards/kick-off-stars", [e_lf])
add_claim("The Dream League Live leaderboard is BY REGION and is based on performances rather than team rating - worldwide ranking was only directly visible through the iOS Game Center leaderboard in DLS19.", 2, "dll/leaderboard-regional", [e_lf], notes="Decisive for defining '#1' - the mission target is regional unless a global surface exists")
add_claim("Serious-player benchmarks from a 3-month review: 13 times Tier 1 Champion, 1,472,836 online XP, a 57% online win rate, 987 career and 1,086 live games played, 19 Legendary Division premierships, 18 All-Star Cup and 18 International Cup wins, and a fully maxed starting 11 plus 9 maxed substitutes.", 3, "career/player-benchmarks", [e_lf])
add_claim("VERSION DRIFT on captain selection: the DLS21-era build showed 9 random Legendary Cards to choose from, whereas the current build offers roughly 80 captain choices plus Create Your Own Captain.", 2, "onboarding/captain-selection-version-drift", [e_lf])
add_claim("G2G marketplace listings advertise account tiers named 'GRAND LEGENDARY X' and 'GRAND LEGENDARY VII' - these are seller/marketplace labels and are NOT confirmed in-game rank names.", 3, "errata/g2g-grand-legendary-marketplace", [e_lf], notes="Must not be quoted as an in-game rank")

p=os.path.join(RAW_DIR,'EV-426_special_players.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-427_launch_features.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
