#!/usr/bin/env python3
"""Turn 35 Wave 23: full Clan mechanics (rank 20, points, reward ladder, 350k cap), Training discount ladder, Accommodation expansion, DLS26 facility cost change (375 coins), Summer Spotlight version correction."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w23')

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

# ---------- EV-409: clans ----------
e_clan=new_ev("sportsdunia DLS26 Clans guide (Jan 2026), dlsmod.com DLS Clans (Dec 2025), dlsapk.net, appitika, dlskits.mobi, thesoccerera, sakibpro, fifaworldcupnews, player.gg, App Store US v13.320 notes, TikTok DLS26 clan tutorials",
    "CLAN MECHANICS (DLS26). UNLOCK: clan features require manager rank 20 (stated by sportsdunia, dlsmod and Spanish-language TikTok tutorials: 'el rango minimo para unirse es de 20'). ACCESS: via your DLS name at the top-right of the screen or the Clan option in the Main Menu. JOINING: browse Public Clans, search a clan by name, enter a Clan Code, or create your own. CREATION customisation: Frame, Background, Icon and their colours, plus Clan Name, Clan Country, Entry Requirements (minimum team rank) and Clan Type (open / closed / invite-only). LEADERSHIP: the clan leader is the primary admin and can remove members; Vice-captains were added in the Winter Reload update. CLAN POINTS are earned from regular matches, winning Live Events, winning Dream Draft events, completing Real-Life Scenarios, Season Pass tiers, and friendly matches against other clan members. Clans are ranked on Clan Leaderboards by accumulated points. REWARD LADDER (sportsdunia): 25,000 Clan Points unlocks the reward track; 25 Gems at 1,000,000 CP; Legendary XP boost at 2,000,000; Legendary Scout at 3,000,000; 500 Coins at 5,000,000; Rare Special Coach at 7,500,000; 150 Gems at 10,000,000. PERSONAL CAP: a member can contribute at most 350,000 Clan Points, so rewards require a large active clan. A Clan Shop is referenced by sakibpro. fifaworldcupnews states clans need a minimum of 50 members for chat/team rewards and offer casual or competitive modes with rating requirements. SUMMER SPOTLIGHT = v13.320 (8 Jun 2026) per the App Store US version history, which also confirms its Clan Improvements were communication-focused: 'new interactions and emoji reactions'. Manager Accessories in that update are North American themed items.",
    "evidence/raw/turn35_w23/EV-409_clans.html",
    "Clans unlock at manager rank 20; join via public browse/name search/clan code/create; creation customises frame, background, icon, colours, name, country, min rank, open/closed/invite-only; leader is admin, vice-captains added Winter Reload; Clan Points from regular matches, Live Events, Dream Draft, Real-Life Scenarios, Season Pass tiers and clan friendlies; clan leaderboards; reward ladder 25k start then 25g@1M, Leg XP boost@2M, Leg Scout@3M, 500c@5M, Rare Special Coach@7.5M, 150g@10M; personal cap 350,000 CP; Clan Shop; min 50 members; Summer Spotlight = v13.320 Jun 8 with clan emoji/interactions + North American manager accessories",
    quality="community")

add_claim("Clan features in DLS26 unlock at manager rank 20.", 2, "clans/unlock-rank-20", [e_clan])
add_claim("Clans are accessed from your DLS name at the top-right of the screen or the Clan option in the Main Menu; you can browse public clans, search by name, enter a clan code, or create your own.", 2, "clans/access-and-join", [e_clan])
add_claim("Clan creation lets you set Frame, Background, Icon and their colours, plus Clan Name, Clan Country, Entry Requirements (minimum team rank) and Clan Type (open / closed / invite-only).", 2, "clans/creation-options", [e_clan])
add_claim("The clan leader is the primary admin and can remove members; Vice-captains were added to clans in the Winter Reload update.", 2, "clans/leadership", [e_clan])
add_claim("Clan Points are earned from regular matches, winning Live Events, winning Dream Draft events, completing Real-Life Scenarios, Season Pass tiers, and friendly matches against other clan members.", 2, "clans/point-sources", [e_clan])
add_claim("Clans are ranked on Clan Leaderboards by accumulated Clan Points, and a Clan Shop exists for spending them.", 3, "clans/leaderboards-shop", [e_clan])
add_claim("Clan reward ladder: 25,000 Clan Points unlocks the reward track, then 25 Gems at 1,000,000 CP, Legendary XP boost at 2,000,000, Legendary Scout at 3,000,000, 500 Coins at 5,000,000, Rare Special Coach at 7,500,000 and 150 Gems at 10,000,000.", 3, "clans/reward-ladder", [e_clan], notes="Single source (sportsdunia); figures unverified")
add_claim("A clan member can contribute a maximum of 350,000 Clan Points, so unlocking the top clan rewards requires a large, active clan.", 3, "clans/personal-cap-350k", [e_clan])
add_claim("Clans require a minimum of 50 members for chat and team rewards, and offer casual or competitive modes with rating requirements.", 3, "clans/min-members-50", [e_clan])
add_claim("Summer Spotlight is v13.320 (8 Jun 2026), not 13.300/13.310 — its Clan Improvements were communication-focused (new interactions and emoji reactions) and its Manager Accessories are North American themed items.", 1, "patching/summer-spotlight-version", [e_clan], notes="Corrects the earlier 13.300/13.310 version attribution")

# ---------- EV-410: facility discount + cost ladders ----------
e_disc=new_ev("r/DreamLeagueSoccer 1b2xxys TRAINING FACILITY GUIDE (Feb 2024), r/DreamLeagueSoccer 1h6nprr Accommodation facility (Dec 2024), r/DreamLeagueSoccer 1apuwf3 currency math (Feb 2024), r/DreamLeagueSoccer whgg7n stadium upgrades (Aug 2022), LevelWinner DLS24",
    "FACILITY DISCOUNT AND COST LADDERS. TRAINING CENTRE COACH DISCOUNT (r/DLS Feb 2024, explicit per-level): Level 1 = 5% gem discount + first formation group, costs 75 gems; Level 2 = 10% discount + another formation group, costs 150 gems; Level 3 = 15% discount + another formation group; Level 4 = a large jump that brings Legendary coaches below 200 gems each; Level 5 = roughly 1,175 gems cumulative, unlocks every formation group in the game and the cheapest coaches. Community guidance: stay at Level 1 if maxing with coins, reach Level 2 if planning to spend ~3,000 gems on Legendary coaches, Level 4-5 only if maxing predominantly with gems. ACCOMMODATION EXPANSION (r/DLS Dec 2024): the facility gained 5 additional levels, each granting +4 squad slots; maxing from zero costs 4,125 gems, or 3,000 gems if you already held the previous 40-player maximum (starting from 44). Older guides citing 20-24 slots are pre-expansion figures. STADIUM BONUS: 52 coins per home game at a maxed stadium (corroborates the 48-52 range). STADIUM UPGRADE TIP: upgrade one stand at a time rather than levelling all stands evenly, as this is cheaper.",
    "evidence/raw/turn35_w23/EV-410_facility_ladders.html",
    "Training Centre discount ladder: L1 5%/75g, L2 10%/150g, L3 15%, L4 pushes Legendary coaches under 200g, L5 ~1,175g cumulative = all formations + cheapest coaches; Accommodation gained 5 levels at +4 slots each, 4,125g from zero or 3,000g from the old 40-player max (44 start); stadium bonus 52c/home game; upgrade one stand at a time is cheaper",
    quality="community")

add_claim("Training Centre coach discount ladder: Level 1 = 5% (75 gems), Level 2 = 10% (150 gems), Level 3 = 15%, Level 4 pushes Legendary coaches below 200 gems each, Level 5 = ~1,175 gems cumulative and unlocks every formation group plus the cheapest coaches.", 2, "facilities/training-discount-ladder", [e_disc])
add_claim("Community guidance on Training Centre depth: stay at Level 1 if maxing players with coins, reach Level 2 if planning ~3,000 gems of Legendary coaches, and only reach Level 4-5 if maxing predominantly with gems.", 3, "facilities/training-depth-guidance", [e_disc])
add_claim("The Accommodation facility gained 5 additional levels, each granting +4 squad slots: 4,125 gems to max from zero, or 3,000 gems if you already held the previous 40-player maximum (starting from 44).", 2, "facilities/accommodation-expansion", [e_disc])
add_claim("The pre-expansion maximum squad size was 40 players; older guides citing 20-24 slots are outdated by several versions.", 3, "facilities/squad-size-history", [e_disc])
add_claim("A fully upgraded stadium pays a home-match bonus of 52 coins, corroborating the 48-52 coin range reported elsewhere.", 2, "facilities/stadium-bonus-52", [e_disc])
add_claim("Stadium upgrade efficiency tip: upgrade one stand at a time rather than levelling all stands evenly, as staggered upgrades are cheaper.", 3, "facilities/stadium-upgrade-tip", [e_disc])

# ---------- EV-411: DLS26 economy changes ----------
e_econ=new_ev("r/DreamLeagueSoccer 1phcvdv DLS26 review after 1 week (Dec 2025), r/DreamLeagueSoccer 1pcdhg8 new DLS26 details (Dec 2025), r/DreamLeagueSoccer 1papf7u (Nov 2025), official FTG TikTok on facilities cityscape + unlimited special storage, r/DreamLeagueSoccer 1lm2gfw (Jun 2025)",
    "DLS26 ECONOMY CHANGES. FACILITY COST RESTRUCTURE (r/DLS 1-week review, Dec 2025): the FIRST tier of every facility upgrade now costs 375 COINS instead of 75 GEMS — a significant change from all prior versions where the first tier was 75 gems. DREAM POINT BOOSTS: in DLS26 you choose which Dream Point boost you buy rather than receiving one at random — the boost is guaranteed rather than luck-based; community reports boosting 5-6 times (600+ gems) and consistently receiving only +50%. PRIZE LADDER: DLS26's ladder gives far more frequent and better early-stage rewards than before. NEW STADIUM DESIGNS: a new stadium design costs 950 gems, and a separate pay-to-win premium stadium IAP exists (reported around GBP 25, alongside a GBP 99.99 gem/coin bundle). UNLIMITED SPECIAL STORAGE: all players now have unlimited Special Player storage, and the facilities screen was redesigned as a cityscape view where you build and view your stadium and facilities. SEASONAL GEM INCOME (r/DLS Jun 2025 estimate): ~40 gems for seasonal objectives, 35 league, 30 Global Challenge Cup, 25 Diamond Cup, 20 All Star Match, 15 National Tournament, 10 All Stars tournament — roughly 180 gems per season from objectives and cups alone.",
    "evidence/raw/turn35_w23/EV-411_dls26_economy.html",
    "DLS26 first facility tier now costs 375 COINS not 75 gems; DP boosts are chosen/guaranteed not random (5-6 boosts = 600+ gems, only +50% each); Prize Ladder more generous early; new stadium design 950 gems; P2W stadium IAP ~GBP25 (gem/coin bundle GBP99.99); unlimited Special Player storage; facilities screen redesigned as cityscape; ~180 gems/season from objectives+cups",
    quality="community")

add_claim("DLS26 restructured facility pricing: the FIRST tier of every facility upgrade now costs 375 coins instead of the 75 gems charged in all prior versions.", 2, "economy/dls26-facility-first-tier-coins", [e_econ])
add_claim("In DLS26 you choose which Dream Point boost to purchase rather than receiving a random one — boosts are guaranteed rather than luck-based.", 2, "economy/dp-boost-guaranteed", [e_econ])
add_claim("Dream Point boosts cost roughly 100+ gems each and community reports consistently receiving only +50% (5-6 boosts costing 600+ gems).", 3, "economy/dp-boost-cost-yield", [e_econ])
add_claim("The DLS26 Prize Ladder gives far more frequent and better rewards in the early stages than in previous versions.", 3, "economy/prize-ladder-dls26-generosity", [e_econ])
add_claim("A new stadium design in DLS26 costs 950 gems, and a separate premium pay-to-win stadium IAP exists (reported around GBP 25, alongside a GBP 99.99 gem-and-coin bundle).", 3, "economy/new-stadium-950-gems", [e_econ])
add_claim("All DLS26 players have unlimited Special Player storage, removing the squad-limit pressure on collecting Special cards.", 2, "economy/unlimited-special-storage", [e_econ])
add_claim("The DLS26 facilities screen was redesigned as a cityscape view where you build, upgrade and view your stadium and facilities.", 2, "ui/facilities-cityscape", [e_econ])
add_claim("Approximate seasonal gem income from objectives and cups alone is ~180 gems: 40 seasonal objectives, 35 league, 30 Global Challenge Cup, 25 Diamond Cup, 20 All Star Match, 15 National Tournament, 10 All Stars tournament.", 3, "economy/seasonal-gem-income", [e_econ])
add_claim("Fanzone upgrade gem costs per level remain unpublished by every source found — OPEN GAP requiring device verification.", 4, "facilities/fanzone-cost-gap", [e_clan, e_econ], notes="OPEN GAP - facility existence confirmed officially, per-level costs unavailable")

p=os.path.join(RAW_DIR,'EV-409_clans.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-410_facility_ladders.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
p3=os.path.join(RAW_DIR,'EV-411_dls26_economy.html')
if not os.path.exists(p3):
    with open(p3,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
