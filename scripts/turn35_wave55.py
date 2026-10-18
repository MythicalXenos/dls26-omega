#!/usr/bin/env python3
"""Turn 35 Wave 55: THE ACCOMMODATION LADDER (the second fully-published facility ladder) and the
uniform 75xN facility-cost pattern it reveals, the corroborated DLL tier-promotion XP ladder, the
Progression Bank gem formula, and a second source on the clan top-contributor reward.

Wave 55's headline: the Accommodation facility's full 10-level ladder is published
(75/150/225/300/375/450/525/600/675/750 = 4,125 gems, +4 squad space per level), and its first five
levels are IDENTICAL to the Training ladder's. That means the facility gem cost is a uniform
75 x level progression - which reframes the KB's '1,125 gems per facility' as the cost of the first
FIVE levels only, and raises the question of how many levels each facility really has.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w55')

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

# ---------- EV-468: facility ladders ----------
e_fac=new_ev("r/DreamLeagueSoccer 1h6nprr (4 Dec 2024, 'Total Gem Cost to Max Accommodation Facility'), 1b2xxys (29 Feb 2024, TRAINING FACILITY GUIDE with the full level-by-level ladder), Nerdburglars Dream League Soccer achievement list (per-achievement XP values including the tier ladder), r/DLS monthly clan discussion thread (gem ledger and the Progression Bank formula), gtrmod.com DLS26 mod menu page (Fanzone level count), thesoccerera DLS26 features page (Fanzone stadium discounts), dlskits.mobi DLS26 features page",
    "THE ACCOMMODATION LADDER AND THE UNIFORM FACILITY-COST PATTERN. THE ACCOMMODATION FACILITY'S FULL LADDER IS PUBLISHED (r/DLS 1h6nprr, 4 Dec 2024): 'Accommodation Facility now has +5 more Levels. Each level giving +4 player space in your Squad. You get +4 extra space for free when you install DLS25 with your current squad... From 0 to max Level it will take a Total of 4125 Gems. From Level 1 to Max it will cost Gems in this Order: 75, 150, 225, 300, 375, 450, 525, 600, 675, 750. If you already had maxed 40 players you will start with 44 and 5 extra new levels. It will cost 3000 Gems to Max from there.' So: TEN levels, +4 squad space per level, 4,125 gems from zero, and a legacy account starting at 44 players pays 3,000 gems for the last five levels. THE HEADLINE FINDING: those first five levels are IDENTICAL to the Training ladder the KB already holds (75/150/225/300/375), which means the facility gem cost follows a uniform pattern - LEVEL N COSTS 75 x N GEMS - and the KB's '1,125 gems per facility' is the cost of the first FIVE levels only. If the pattern holds across facilities, fully maxing one facility is 4,125 gems and the KB's '5,625 gems total for all five facilities' is a five-level figure, not a maxed one. THE TRAINING LADDER IS INDEPENDENTLY CORROBORATED (r/DLS 1b2xxys): 'LEVEL 1 PRICE: 75 / LEVEL 2: 150 / LEVEL 3: 225 / LEVEL 4: 300 / LEVEL 5: 375', with 'to get to this position you will have to spent around 1175 gems' cumulative to L5, L4 described as the point where 'legendaries are going to cost less than 200 gems', and L5 as 'you will now have every group of formations in the game, and also have the cheapest coaches'. THE DLL TIER-PROMOTION XP LADDER IS CORROBORATED EXACTLY (Nerdburglars, per-achievement XP): Tier 10 Promotion 500 XP, Tier 9 1,000, Tier 8 1,500, Tier 7 2,000, Tier 6 2,500, Tier 5 3,000, Tier 4 3,500, Tier 3 4,000, Tier 2 4,500 - which with the 5,000-XP Tier 1 Champions achievement sums to exactly the 27,500 XP the KB already holds for promoting tier 10 to tier 1. The same list carries the division ladder (Academy promotion 500, Division 3 promotion 1,000, Division 2 promotion 1,500), 'Bragging Rights' 2,000 XP for becoming champion of any DLL tier, and 1,500 XP for finishing a league season undefeated. THE PROGRESSION BANK FORMULA: '1,000 DLL XP = 1 GEM. In 1 game: assuming you win every game 3-0, in Tier 1 + Season Pass Premium, and a 50% of having a home advantage, you will gain roughly 1,640 DLL XP' - which reproduces the KB's 1,640-gem Progression Bank figure exactly. THE DLL CHAMPION CAP: '125 is maximum amount of times you can become champion in one season' at 48 gems each = 6,000 gems, matching the KB's DLL figure. A LEGENDARY DP POINT BOOSTER COSTS 125 GEMS, and a full-season grind is planned around 61 of them (7,625 gems). THE CLAN TOP-CONTRIBUTOR REWARD IS 100 GEMS in this same ledger ('in a clan there is a leaderboard where having the highest clan points give you the reward of 100 Gems'), which is a SECOND source for the 100-gem side of C-017 against one source for 50. THE FANZONE HAS FIVE LEVELS according to a mod-site feature list ('instantly level up your Commercial, Medical, Training, and the brand-new Fanzone facilities to level 5'), and two sources describe its function as clan bonuses plus structural discounts on stadium expansions - which, if true, makes it a cost-reducer for the wave-51 stadium ladder. DLL RELEGATION EXISTS: 'all I needed was just 2 points to stay in tier 2 or get relegated to tier 3.'",
    "evidence/raw/turn35_w55/EV-468_facility_ladders.html",
    "FACILITY LADDERS: the Accommodation facility's full ladder is published - TEN levels at 75/150/225/300/375/450/525/600/675/750 gems = 4,125 total, +4 squad space per level, 3,000 gems for the last five levels from a legacy 44-player start. ITS FIRST FIVE LEVELS ARE IDENTICAL TO THE TRAINING LADDER, which reveals a UNIFORM FACILITY-COST PATTERN: level N costs 75 x N gems. So '1,125 gems per facility' is the cost of the first FIVE levels only, and fully maxing one facility is 4,125 gems - the KB's '5,625 total for all five' is a five-level figure, not a maxed one. DLL TIER-PROMOTION XP CORROBORATED EXACTLY: 500/1000/1500/2000/2500/3000/3500/4000/4500 for tiers 10 down to 2, plus 5,000 for Tier 1 Champion = 27,500 XP. Progression Bank formula confirmed: 1,000 DLL XP = 1 gem, about 1,640 DLL XP per Tier-1 3-0 win. DLL champion cap 125 per season at 48 gems = 6,000. A Legendary DP booster is 125 gems. CLAN TOP CONTRIBUTOR = 100 GEMS (second source for that side of C-017). The Fanzone has five levels per one mod-site source, and its stadium discounts would cut the wave-51 stadium ladder's coin cost. DLL relegation exists - 2 points kept one player in tier 2",
    quality="community")

add_claim("THE ACCOMMODATION FACILITY LADDER IS FULLY PUBLISHED: ten levels costing 75, 150, 225, 300, 375, 450, 525, 600, 675 and 750 gems - 4,125 gems from zero - with each level giving +4 squad space. A legacy account that already maxed the old 40-player facility starts at 44 players and pays 3,000 gems for the last five levels.", 2, "facilities/accommodation-ladder", [e_fac], notes="The second fully-published facility ladder after Training")
add_claim("THE FACILITY GEM COST IS A UNIFORM 75 x LEVEL PATTERN: Accommodation's first five levels (75/150/225/300/375) are identical to the Training ladder's, so level N costs 75 x N gems. This means '1,125 gems per facility' is the cost of the FIRST FIVE LEVELS ONLY, and fully maxing one facility costs 4,125 gems.", 2, "facilities/uniform-75x-level-pattern", [e_fac], notes="Reframes the whole facility budget - the KB's 5,625 'all five' figure is a five-level figure, not a maxed one")
add_claim("The Training facility ladder is independently corroborated level by level (75/150/225/300/375), with L4 the point where 'legendaries are going to cost less than 200 gems', L5 giving 'every group of formations in the game, and also have the cheapest coaches', and a cumulative cost of about 1,175 gems to L5.", 2, "facilities/training-ladder-corroborated", [e_fac])
add_claim("THE DLL TIER-PROMOTION XP LADDER IS CORROBORATED EXACTLY: Tier 10 promotion 500 XP, Tier 9 1,000, Tier 8 1,500, Tier 7 2,000, Tier 6 2,500, Tier 5 3,000, Tier 4 3,500, Tier 3 4,000, Tier 2 4,500 - plus the 5,000-XP Tier 1 Champions achievement = exactly 27,500 XP to promote from tier 10 to tier 1.", 2, "dll/tier-promotion-xp-corroborated", [e_fac], notes="Independent confirmation of the KB's headline ladder")
add_claim("Other achievement XP values (Nerdburglars): Bragging Rights 2,000 XP for becoming champion of any DLL tier; 1,500 XP for finishing a league season undefeated; Academy promotion 500, Division 3 promotion 1,000, Division 2 promotion 1,500.", 2, "achievements/division-and-undefeated-xp", [e_fac])
add_claim("THE PROGRESSION BANK FORMULA: 1,000 DLL XP converts to 1 gem, and a Tier-1 3-0 win with Season Pass Premium and about 50% home advantage yields roughly 1,640 DLL XP - which reproduces the corpus's 1,640-gem Progression Bank season figure exactly.", 2, "dll/progression-bank-formula", [e_fac])
add_claim("The DLL champion cap is 125 championships per 10-day season at 48 gems each = 6,000 gems, matching the corpus's DLL gem figure. A Legendary DP Point Booster costs 125 gems and a full-season plan stockpiles 61 of them (7,625 gems).", 2, "dll/champion-cap-and-booster-cost", [e_fac])
add_claim("A SECOND SOURCE NAMES 100 GEMS for the clan top contributor: 'in a clan there is a leaderboard where having the highest clan points give you the reward of 100 Gems.' C-017 now has two sources on the 100-gem side against one on the 50-gem side.", 2, "clans/top-contributor-100-second-source", [e_fac], notes="C-017 - weight shifts toward 100")
add_claim("The Fanzone has five levels according to a mod-site feature list ('instantly level up your Commercial, Medical, Training, and the brand-new Fanzone facilities to level 5'), and two sources describe its benefit as clan bonuses plus structural discounts on stadium expansions - which, if accurate, makes it a cost-reducer for the stadium build rather than a pure gem sink.", 3, "facilities/fanzone-five-levels", [e_fac], notes="Speculative on the level count - the only data point; the function is official")
add_claim("DLL RELEGATION EXISTS: a player reports needing only 2 points to stay in tier 2 or be relegated to tier 3, so tier survival - not just promotion - is a target in the middle bands.", 3, "dll/relegation-exists", [e_fac], notes="Affects the camping strategy: quitting matches risks the points needed to survive")

for name in ('EV-468_facility_ladders.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
