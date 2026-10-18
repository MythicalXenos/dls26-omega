#!/usr/bin/env python3
"""Turn 36 Wave 36 (turn35 continuation): DLL tier ladder detail from the world-record run, Live-gem tier gating (tier 10+), coach mechanics (Fitness/Tech pools, base+10, re-train gems, pool narrowing), coach-farming economics, 23-player max rule for 100% club value, Fan Approval 75%/100% milestones, daily challenge gem income."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w36')

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

# ---------- EV-432: DLL tier ladder detail ----------
e_dll=new_ev("r/DreamLeagueSoccer 1qz14ir (Feb 2026 full world-record post), 1ghbsed (Nov 2024 tier 7->1 in 4 days), 108xox7 (Jan 2023 tier survey), rsrzfa (Dec 2021 'Levels' 12-10), 176ntor (Oct 2023 summary)",
    "DREAM LEAGUE LIVE TIER LADDER - DETAILED EVIDENCE. The February 2026 world-record post gives the fullest picture: the player set out to minimise online XP to Tier 1 Champion, 'not once did I not get promoted to the next tier (crucial to saving XP)', set records for the least XP to tier 10, the least XP to tier 5 and the least XP to tier 1, 'scraped through Tier 3 against countless fully maxed teams, clutching a win on the final game to just get promotion', and 'went undefeated in Tier 2 against players with 10M+ XP'. Tier 3 is therefore the first wall of fully maxed opposition and Tier 2 opponents commonly hold 10M+ XP. NOVEMBER 2024: a player reports deliberately RELEGATING to tier 10 'for farming gems and winning events as a break for my mental health', then grinding from tier 7 to 1 in only 4 days, championing every tier. JANUARY 2023 SURVEY: one player goes undefeated in tier 6 but is relegated in tier 5; another was stuck in tier 6 in DLS22 but reached tier 3 in DLS23 because 'lower points required', promoting every single time; a third sits in tier 10 with a full gold team but 'still need a few more top players to even start grinding on Live'. DECEMBER 2021 (DLS21-era, when tiers were called 'Levels'): a player fluctuated between Levels 12-10, winning comfortably at 12 and 11 but suffering four straight defeats on hitting Level 10, and was in the SEA region - confirming both the terminology drift (Level -> Tier) and that regional pools differ. GEM GATING RULE (Oct 2023): Live is for players who want to recycle their transfer list or need gems, and gems from Live are available at TIER 10 AND ABOVE ONLY - a decisive operational rule that puts a floor on where the grind must happen. Also recorded: a 70-rated team can win the Legendary Division, though it is very hard.",
    "evidence/raw/turn35_w36/EV-432_dll_tier_detail.html",
    "Tier ladder detail: promotion every tier saves XP (world-record tactic); records set for least XP to tier 10, tier 5 and tier 1; Tier 3 is the first wall of fully maxed teams (promotion clinched on the final game); Tier 2 opponents commonly have 10M+ XP and the record-holder went undefeated there; a player deliberately relegated to tier 10 to farm gems and win events, then ground tier 7 to 1 in 4 days; tier 5-6 is a common sticking point while tier 3+ was easier in DLS23 due to lower point requirements; DLS21-era tiers were called 'Levels' (12-10) and a SEA player confirms regional pools differ; CRITICAL RULE - Live gems are available at TIER 10 AND ABOVE ONLY; a 70-rated team can win the Legendary Division but it is very hard",
    quality="community")

add_claim("Dream League Live tiers run 20 to 1; the world-record Tier 1 run promoted at every tier deliberately, because promotion is the cheapest way to save online XP.", 3, "dll/tier-ladder-detail", [e_dll])
add_claim("Tier 3 is the first wall of fully maxed opposition (the record-holder clinched promotion only on the final game), and Tier 2 opponents commonly hold 10M+ online XP.", 3, "dll/tier-3-wall", [e_dll])
add_claim("A documented strategy is to deliberately RELEGATE to tier 10 to farm gems and win events, then grind from tier 7 to 1 in as little as 4 days, championing every tier.", 3, "dll/tier-10-farming-strategy", [e_dll])
add_claim("Live gems are available at TIER 10 AND ABOVE ONLY - below tier 10 Live does not pay gems, which sets a hard floor on where the ranked grind must happen.", 3, "dll/gem-gating-tier-10", [e_dll], notes="Decisive operational rule")
add_claim("Tier 5-6 is a common sticking point for players, while a DLS23 player found tier 3+ easier because lower points were required for promotion.", 3, "dll/tier-5-6-wall", [e_dll])
add_claim("In the DLS21 era Dream League Live tiers were called 'Levels' (players reported fluctuating between Levels 12-10), and a SEA-region player confirms regional match pools differ.", 3, "dll/level-to-tier-terminology-drift", [e_dll])
add_claim("A 70-rated team can win the Legendary Division in Career Mode, though it is very hard.", 3, "career/low-rated-legendary-win", [e_dll])

# ---------- EV-433: coach mechanics + max economics + fan approval ----------
e_cm=new_ev("r/DreamLeagueSoccer 1pudgh8 (Dec 2025), 1k1fwgl (Apr 2025), 1bxmcwf (Apr 2024), 1ib3awb (Jan 2025), 1qbkdkl (Jan 2026), 11on7r4 (Mar 2023), 1nn7uez (Sep 2025), gamedls.net Player Stat Upgrades, dream-league-soccer.fandom Player Development, Exophase DLS2018/DLS Classic achievements, Nerdburglars achievement list, thekittygamer 2018 guide, supercheats Q&A",
    "COACH MECHANICS AND MAX ECONOMICS. Coaches are obtained from the Season Pass, the Prize Ladder, Live events, gems and real money; the recipient player AND the upgraded attribute are both chosen at random. A card's MAX RATING is base overall +10, with very rare +11 cases. There are exactly TWO coach types for outfield players: FITNESS covers SPE, ACC, STA and STR, while TECH covers CON, PAS, SHO and TAC - this is the pool the RNG draws from. POOL NARROWING: releasing players you do not want to train is the way to make coaches target the players you do want, and fewer eligible players in the squad increases the chance a specific player is upgraded. RE-TRAIN: if a coach lands on the player you want, tapping re-train spends GEMS to gain more points on that player. SPECIAL COACHES temporarily bypass the randomisation and allow targeted upgrades. COACH-FARMING ECONOMICS: buy players under 180-210 coins and release them for Common coaches; buy 80-rated DEFENDERS (the cheapest legendary class, since Attacker > Midfield > Defender in gold cost) and release them for Rare coaches. One analysis prices a full max at roughly 32,000 coins using Common coaches (about 400 coins per player across ~80 coaches, each player having ~80 upgrade points) or ~30,000 coins using Rare coaches (about 1,500 coins per player across ~20 coaches), with Rare 80-rated defenders available from ~1,460 coins. RECOMMENDED RATIOS: 7:3 fitness-to-tech for non-maxed teams, or 90:10 while targeting speed first; for isolating a single player you need a full maxed team or a squad of goalkeepers plus that one outfield player. DAILY INCOME: daily challenges pay 5-11 gems per day, and the advice is to stack coaches and not use them too early. CARD COLOUR PROGRESSION: a player's card becomes silver then gold once overall rises by a rating-dependent amount, and turns black at 100 overall; upgraded players also appear in the market as silver or gold cards, which is an efficient way to buy an already-developed player. MARKET GATING: legendary players do not appear until your team rating rises, gold-carded players become regular above 80 team rating, and even a 94.4-rated team may not see 85-86 players for a long time. FAN APPROVAL is a percentage with two published milestones: 'Mr Popular' at 75% (500 XP) and 'Fan Favourite' at 100% (2,000 XP in DLS2018 / 1,000 XP in DLS Classic). CLUB VALUE: a player with nearly all 99-rated players, 300+ consecutive wins and 100% fan approval was still stuck at 58.52% club value, and the community answer is that 100% requires EVERY player including bench and reserves to be maxed - 'you need 23 players to max'.",
    "evidence/raw/turn35_w36/EV-433_coach_mechanics.html",
    "Coaches come from Season Pass/Prize Ladder/Live events/gems/real money; both recipient and attribute are RANDOM; max rating = base +10 (rarely +11); only TWO outfield coach types - Fitness (SPE/ACC/STA/STR) and Tech (CON/PAS/SHO/TAC); release unwanted players to narrow the pool and raise the odds; RE-TRAIN costs gems to add points after a lucky hit; Special Coaches bypass randomisation; coach farming: buy players under 180-210c for Common coaches and 80-rated DEFENDERS (cheapest legendary, Attacker>Midfielder>Defender) for Rare coaches; full max costs ~32,000c with Commons (~400c x 80 coaches, ~80 upgrade points per player) or ~30,000c with Rares (~1,500c x 20); ratios 7:3 fitness:tech (or 90:10 for speed-first); daily challenges 5-11 gems/day; card goes silver then gold by a rating-dependent amount and black at 100 OVR, and upgraded players appear in the market as silver/gold cards; legendaries only appear as team rating rises (80+ for gold cards, and even 94.4 teams may not see 85-86s); Fan Approval milestones Mr Popular 75% (500 XP) and Fan Favourite 100% (2,000 XP); 100% club value requires ALL players maxed including bench and reserves - about 23 players",
    quality="community")

add_claim("OFFICIAL-ADJACENT COACH MODEL: coaches are obtained from the Season Pass, Prize Ladder, Live events, gems and real money, and BOTH the recipient player and the upgraded attribute are chosen at random.", 2, "training/coach-sources-random", [e_cm])
add_claim("A card's maximum rating is its base overall +10, with very rare +11 cases.", 2, "training/max-plus-10", [e_cm])
add_claim("There are exactly two outfield coach types: FITNESS upgrades SPE, ACC, STA and STR, while TECH upgrades CON, PAS, SHO and TAC.", 2, "training/coach-stat-pools", [e_cm])
add_claim("Releasing players you do not want to train narrows the coach pool and increases the chance that coaches upgrade the players you do want.", 2, "training/pool-narrowing", [e_cm])
add_claim("RE-TRAIN: after a coach lands on the player you want, tapping re-train spends gems to gain additional points on that player.", 3, "training/re-train-gems", [e_cm])
add_claim("Coach-farming economics: buy players under 180-210 coins and release them for Common coaches, and buy 80-rated DEFENDERS (the cheapest legendary class, since Attacker > Midfielder > Defender in gold cost) and release them for Rare coaches.", 2, "economy/coach-farming-prices", [e_cm])
add_claim("A full player max costs roughly 32,000 coins with Common coaches (about 400 coins per player across ~80 coaches, each player having ~80 upgrade points) or ~30,000 coins with Rare coaches (about 1,500 coins per player across ~20 coaches), with Rare 80-rated defenders available from about 1,460 coins.", 3, "economy/max-cost-estimate", [e_cm])
add_claim("Recommended fitness-to-tech coach ratios are 7:3 for non-maxed teams and 90:10 when targeting speed first; isolating a single player requires a full maxed team or a squad of goalkeepers plus that one outfield player.", 3, "training/coach-ratios", [e_cm])
add_claim("Daily challenges pay 5-11 gems per day, and the community advice is to stack coaches and not use them too early.", 3, "economy/daily-challenge-gems", [e_cm])
add_claim("A player's card becomes silver then gold once overall rises by a rating-dependent amount and turns black at 100 overall; upgraded players also appear in the transfer market as silver or gold cards, an efficient way to buy an already-developed player.", 2, "cards/colour-progression-market", [e_cm])
add_claim("Legendary players do not appear in the transfer market until team rating rises, gold-carded players become regular above 80 team rating, and even a 94.4-rated team may not see 85-86 players for a long time.", 3, "transfers/rating-gating-86s", [e_cm])
add_claim("Fan Approval has two published milestones: 'Mr Popular' at 75% (500 XP) and 'Fan Favourite' at 100% (2,000 XP in DLS2018, 1,000 XP in DLS Classic).", 2, "economy/fan-approval-milestones", [e_cm])
add_claim("100% club (Dream Team) value requires EVERY player including bench and reserves to be maxed - about 23 players - not merely a high-rated starting eleven.", 3, "economy/club-value-23-players", [e_cm], notes="Corroborates the ~23-player Dream FC figure")

p=os.path.join(RAW_DIR,'EV-432_dll_tier_detail.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-433_coach_mechanics.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
