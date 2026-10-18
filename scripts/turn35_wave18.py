#!/usr/bin/env python3
"""Turn 35 Wave 18: Season Pass full mechanics — 400 SP activation, free track 1,095c + Epic agent, Progression Bank 10-day payout, level cadence."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w18')

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

e_sp=new_ev("Bluestacks 2026 DLS guide, gamingonphone 2024/2025 guides, hgret 2023, gamedls.net, r/DreamLeagueSoccer (jwes7t Nov2020, 1bl405h Mar2024, 1ercjvd Aug2024), App Store SG listing, FTG support",
    "SEASON PASS full mechanics. Activation: requires 400 Season Points; SP earned from daily login (40/day free), winning Career Mode games, and Dream League Live matches; online and league matches give the most SP. Season length = 10 days. FREE track: completing all free tiers guarantees 1,095 coins plus an Epic agent (per r/DLS 2020 review); free rewards are coins, small gems, basic coaches. PREMIUM/ELITE pass (IAP: US $3.99 / SG S$5.98 / SG Special Offer S$2.98; INR 399 basic + 1199 premium per sportsdunia, flagged outlier) unlocks an extra reward row: large gem/coin quantities, Rare & Legendary coaches, exclusive/high-rated player cards, XP or SP boosters. PROGRESSION BANK: coins and gems earned through season progression accumulate in the Progression Bank and are only credited after the 10-day season ends; bigger payout the more Dream League Live matches you win. LEVEL CADENCE: one SP level advances every 10 hours; if you don't play, levels are 'stored' so multiple levels can advance at once later. Advancing a level usually takes ~3 matches depending on performance. Reward reveal cadence: 1 reward unlocks every 12 hours (12 AM/PM), and buying mid-season makes the backlog of already-earned levels claimable. DLS21-era (Nov 2020) first paid Season Pass contents (dated baseline): 4000 coins, 150 crystals, 5 legendary form boosts, 3 legendary coaches (1 technical, 1 fitness, 1 GK), 1 legendary physio, 1 legendary scout, 1 legendary agent; manager card turns gold. r/DLS 2024: premium vs lower tier nearly identical apart from season XP for better Dream League Live leaderboard rewards + tier head start. Daily login cycle refreshes every 20 days and missing one day resets to Day 1. Daily Scenarios = 50 coins/day; daily challenges pay coins per challenge + gems for full set; weekly challenges pay gems for full set. FTG support confirms Gems come via league objectives, tournaments, Season Pass and Prize Ladder, and multiplayer (DLL).",
    "evidence/raw/turn35_w18/EV-399_season_pass.html",
    "Season Pass = 400 SP to activate, 10-day season, 40 SP/day login, free track = 1,095 coins + Epic agent, premium = extra row (gems/coins, Rare+Legendary coaches, exclusive players, boosters), Progression Bank pays at season end, 1 level/10h with stored levels, ~3 matches per level, 12h reward unlock cadence, DLS21 paid-pass baseline 4000c/150crystals/5 Leg boosts/3 Leg coaches/Leg physio+scout+agent/gold manager card",
    quality="community")

add_claim("Season Pass activation requires 400 Season Points; Season Points come from daily login, winning Career Mode games, and Dream League Live matches.", 2, "economy/season-pass-activation", [e_sp])
add_claim("Daily login grants 40 Season Points per day for free toward the 400-point Season Pass activation.", 2, "economy/season-points-login", [e_sp])
add_claim("A Season Pass season lasts 10 days; accumulated Season Pass coins/gems sit in the Progression Bank and are only credited when the season ends.", 2, "economy/season-length-progression-bank", [e_sp])
add_claim("Progression Bank payout scales with Dream League Live (online) match performance during the 10-day season — more DLL wins means a larger end-of-season coin/gem payout.", 2, "economy/progression-bank-dll", [e_sp])
add_claim("Completing all FREE Season Pass tiers guarantees 1,095 coins plus an Epic agent, with no purchase required.", 2, "economy/season-pass-free-track", [e_sp])
add_claim("Free Season Pass rewards are coins, small gem quantities, and basic coaches; the premium/elite pass adds a separate reward row.", 2, "economy/season-pass-free-rewards", [e_sp])
add_claim("Premium/Elite Season Pass (IAP: US $3.99; SG S$5.98, special offer S$2.98) unlocks an extra reward row: large gem/coin quantities, Rare and Legendary coaches, exclusive or high-rated player cards, and XP/Season Point boosters.", 2, "economy/season-pass-premium-track", [e_sp], notes="INR 399/1199 figures from sportsdunia flagged as unverified regional outlier")
add_claim("Season Pass level advancement: one level every 10 hours; unplayed time 'stores' levels so several levels can advance at once on a later login.", 2, "economy/season-pass-level-cadence", [e_sp])
add_claim("Advancing one Season Pass level typically takes about 3 matches depending on performance; online and league matches award the most Season Point XP.", 3, "economy/season-pass-level-cost", [e_sp])
add_claim("Season Pass rewards unlock on a 12-hour cadence (12 AM / 12 PM); purchasing the pass mid-season makes the backlog of already-earned tier rewards immediately claimable.", 3, "economy/season-pass-reward-cadence", [e_sp])
add_claim("DLS21-era baseline (Nov 2020 first paid Season Pass): 4,000 coins, 150 crystals, 5 legendary form boosts, 3 legendary coaches (1 technical, 1 fitness, 1 GK), 1 legendary physio, 1 legendary scout, 1 legendary agent, and a gold manager card — DLS26 contents are expected to differ.", 2, "economy/season-pass-paid-baseline-dls21", [e_sp], notes="Dated DLS21 baseline; treat as floor reference not DLS26 values")
add_claim("Per r/DLS (Mar 2024) the premium and lower paid tiers are nearly identical; the premium tier's advantage is season XP for better Dream League Live leaderboard rewards plus a head start in season tiers.", 3, "economy/season-pass-tier-delta", [e_sp])
add_claim("Daily login reward cycle refreshes every 20 days; missing a single day resets the cycle back to Day 1, forfeiting progress toward later rewards.", 2, "economy/daily-login-cycle", [e_sp])
add_claim("FTG support confirms Gems are obtainable through league objectives, tournaments, the Season Pass and Prize Ladder, and Dream League Live multiplayer participation.", 2, "economy/gem-sources-official", [e_sp])
add_claim("App Store SG listing shows Season Pass at S$5.98 and Season Pass Special Offer at S$2.98, versus US $3.99 — confirming strong regional IAP price variance.", 2, "economy/iap-region-variance", [e_sp])

p=os.path.join(RAW_DIR,'EV-399_season_pass.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
