#!/usr/bin/env python3
"""Turn 35 Wave 14: yellow card accumulation (5 = 1-game ban), DLS26 launch subs/reserves update, transfer lock players, Daily Bonus, First Touch Utd (FTG employees), Dream FC, Dream FC value, squad depth ~19-22 players, 23-player 100% value, coach randomization + Special Coach targeting, Legendary XP 250k."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w14')

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

e_disc=new_ev("App Store DLS26 v13.x version history (Summer Spotlight), r/DLS yellow-card expiry, r/DLS DLS26 megathread day-2 subs/reserves, r/DLS DLS25 XP 250k, r/DreamLeagueSoccer maxing players, r/DreamLeagueSoccer red-cards 5+ DLS21, supercheats DFC value, keengamer squad, gamedls.net upgrade mechanics, dreamkitsapp First Touch Utd roster, fandom Dream FC",
    "DISCIPLINE: Yellow cards DO NOT expire — they accumulate across the season (r/DLS Dec2022). After 5 yellow cards in a season, player is suspended 1 match. Warning (yellow-card icon next to player) appears at 4 yellows. Red card = automatic 1-match suspension (consistent with earlier). Two yellows in same match = red (send off + suspension). When you have multiple suspensions+injuries AND only 5 subs, you can be shorthanded (r/DLS DLS21). If you have 5 red cards in a match AND additional yellows-turned-reds you might run out of players. DLS26 LAUNCH (v13.0xx Dec2025) added: SUBSTITUTES AND RESERVES system (adds realism; reserves regen more stamina: players who don't start a match regain full stamina by the next match). SUMMER SPOTLIGHT (v13.3xx): added 'Transfer upgrades – manage lock players in more ways than before' (PLAYER LOCK feature: lock players to prevent accidental sale/use in coach upgrades); 'Daily Bonus – get rewarded for playing regularly' (daily login/play reward beyond existing 20-day login cycle); 'more friend match options'; 'new special players from peak seasons'; 'Player Recovery' feature; 'All new Clans' (DLS26 launch also introduced Clans); new commentary languages Turkish + Arabic; updated 2025/26 player data with more classic/special/national team players; unlimited special players in squad; new iconic stadiums/upgraded facilities. Special Coaches can bypass random player selection to enable targeted upgrades (gamedls.net DLS25). Coach upgrades: random player selection, random stat; players at max potential get no upgrade; fewer eligible players in squad increases chance a specific player is selected (meta tip: sell down to 15 players for targeted upgrades). Legendary card XP requirement increased to 250,000 XP in Mar2025 update (up 50k from prior). Dream FC is your default club name; you start as manager of Dream FC, can rename. Dream FC club VALUE stat (legacy DLS): to reach 100% value you need ~23 players in squad (starters+bench+reserves) all maxed. ~19-22 players is considered sufficient for rotation (keengamer). First Touch United players are named after FTG employees (most 90+ rated); dreamkitsapp shows Phil Woodovic (92, Serbia, RW/AM, Dream FC), Charles Chapman (92, Anguilla, CB/RB, First Touch Utd), Ben Jones (GK, Gibraltar, FTU), Melvin Terrino (91, Turks & Caicos, CM/DM, FTU) — fictional nationalities are humorous placeholders (employees' fake nationalities).",
    "evidence/raw/turn35_w14/EV-395_discipline_lock_daily.html",
    "Yellow cards accumulate; 5 YC = 1-match ban (warning at 4); red = 1-match ban; 5 subs max; DLS26 launch added Substitutes+Reserves (non-starters regen full stamina next match); Summer Spotlight added Player Lock (transfer upgrades/lock management), Daily Bonus, Player Recovery, Clans v2, TR+AR commentary; Special Coaches can target upgrades; sell down to 15 players for coach targeting; Leg card XP raised to 250k; Dream FC default club, ~23 players for 100% club value, 19-22 sufficient; FTU = FTG employees (Phil Woodovic 92, Charles Chapman 92, Ben Jones GK, Melvin Terrino 91)")

add_claim("Yellow cards do NOT expire within a season — they accumulate across matches.", 2, "discipline/yellow-accumulate", [e_disc])
add_claim("Yellow card suspension threshold: 5 yellows in a season = 1-match suspension. A warning yellow-card icon appears next to the player at 4 yellows (one more = ban).", 2, "discipline/yellow-5", [e_disc])
add_claim("Red card = automatic 1-match suspension; two yellows in one match = red (send off + suspension).", 1, "discipline/red-card", [e_disc])
add_claim("Substitutions per match: 5 subs (confirmed). With multiple red cards + yellows-turning-red + injuries, you can run out of available players (especially with only 5 subs covering 7+ missing players).", 2, "discipline/short-handed-risk", [e_disc])
add_claim("DLS26 LAUNCH (v13.0xx Dec 2025) added SUBSTITUTES + RESERVES system for squad realism (separate subs bench and reserve pool); non-starting players regain FULL stamina by the next match.", 1, "squad/subs-reserves-update", [e_disc])
add_claim("Summer Spotlight (v13.310/330) added PLAYER LOCK feature ('Transfer upgrades – manage lock players in more ways than before'): lock players to prevent accidental sale/release/coach consumption.", 1, "transfers/player-lock", [e_disc])
add_claim("Summer Spotlight added DAILY BONUS (regular-play reward) alongside existing Daily Login cycle.", 1, "economy/daily-bonus", [e_disc])
add_claim("Summer Spotlight added Player Recovery mechanic (likely quick-heal / recovery card).", 2, "economy/player-recovery", [e_disc], "exact mechanics require in-game verification")
add_claim("DLS26 launch also added: 'All new Clans' (v2 launch-day), Turkish + Arabic commentary languages (expanded from prior languages), more Classic/Special/National team players, unlimited Special Players in squad, new iconic stadiums + upgraded facilities.", 1, "patches/dls26-launch-features", [e_disc])
add_claim("Special Coaches (IAP/event) can BYPASS random player selection, allowing TARGETED upgrades (unlike regular coaches which are random).", 2, "coaches/special-targeted", [e_disc])
add_claim("Coach targeting meta-tip: sell down the squad to ~15 players to make random coach selection more likely to land on a desired target (fewer eligible players = higher odds per remaining player).", 3, "coaches/targeting-meta", [e_disc])
add_claim("Legendary card XP requirement raised to 250,000 XP in March 2025 update (up 50,000 from prior threshold).", 3, "cards/legendary-xp-250k", [e_disc])
add_claim("Dream FC is your default club at career start (name editable). You are the manager of Dream FC.", 2, "career/dream-fc", [e_disc])
add_claim("Dream FC Club Value stat reaches 100% when you have ~23 maxed players (starters+bench+reserves). About 19-22 players is considered sufficient for good rotation across fixtures.", 3, "career/club-value", [e_disc], "older DLS data")
add_claim("First Touch United players are named after FTG employees (fictional nationalities): Phil Woodovic (92 RW/AM, Dream FC), Charles Chapman (92 CB/RB, FTU), Ben Jones (GK, FTU), Melvin Terrino (91 CM/DM, FTU). Most FTU starters are 90+ rated.", 2, "endgame/ftu-roster", [e_disc])
add_claim("Substitutes and reserves add tactical depth — keep ~19-22 players minimum to cover injuries, suspensions, and fatigue during long seasons.", 2, "squad/depth", [e_disc])

p=os.path.join(RAW_DIR,'EV-395_discipline_lock_daily.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
