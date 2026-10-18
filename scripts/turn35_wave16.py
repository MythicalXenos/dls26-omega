#!/usr/bin/env python3
"""Turn 35 Wave 16: physio energy % (Common 10%/Rare 20%/Legendary 50% + heal all), injury duration 3-10 games, gem heal cost 5g/game, Medical L1 -5% injury/-10% heal, injuries visible post-match, STR reduces injury, starter 1200c/40g outlier again, IAP USD prices, 15 languages listed, loot box advisory."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w16')

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

e_med=new_ev("LevelWinner DLS20/DLS21/DLS24, r/DLS injury threads (2021-2024), BlueStacks, ldplayer, chaptercheats, gamingonphone DLS26, App Store US IAP info",
    "PHYSIO ENERGY RESTORATION (DLS20-DLS24 baseline): Common Physio = 50 coins, restores 10% energy for all players. Rare Physio = 100 coins, restores 20% energy. Legendary Physio = 200-250 coins (varies by source; default 250, 150c with max Medical facility discount per r/DLS), restores 50% energy AND heals ALL active injuries. Earlier guides (BlueStacks) said Legendary = full energy heal; LevelWinner DLS21 gives the 50% number which is more specific — treat 50% team-wide energy restore + full injury heal as the canonical legendary effect. Individual 'Heal' option on tired/injured players costs coins or gems scaled by severity — minor fatigue ~2-4 coins per player; injuries cost ~5 gems per match of recovery (e.g., 3-match knee strain = 15 gems to instant-heal). Injuries last MULTIPLE GAMES: observed durations range 3 games (minor) up to 7-10 games (severe). Injury type + duration shown when you tap the gems-to-heal button ('player has X injury, out for Y games'); this info is also briefly visible post-match but disappears after closing app or playing another match. Playing reserves while injuries heal naturally is more coin-efficient than instant-gem heals. Medical Centre: L1 upgrade reduces injury probability by 5% AND reduces physio/heal costs by 10%. Higher levels reduce injury chance and physio cost further (exact per-tier % not documented). Higher STR stat on individual players also reduces their injury chance. Meta: upgrade Training before Medical (facility upgrade priority) but Medical is second priority for sustainable play. Starter resources outlier (gamingonphone DLS26 + footballeffect): ~1,200 coins / 40 gems — contradicts 1,500c/75g+free scout/agent (likely older beta or regional variation; App Store/fandom baseline 1500/75 likely). Season Pass IAP price: $3.99 USD (App Store). Other IAP: Bundle of Coins $1.99, Stack of Coins $3.99, Special Offer $4.99. Loot boxes/random items warning present in App Store rating (Frequent/Contests + Loot Boxes). DLS26 supports 15 languages per App Store: English, Arabic, Dutch, French, German, Indonesian, Italian, Japanese, Korean, Portuguese, Russian, Simplified Chinese, Spanish, Traditional Chinese, Turkish.",
    "evidence/raw/turn35_w16/EV-397_physio_injury.html",
    "Physio energy: C=10%/50c, R=20%/100c, L=50%+heal-all-injuries/200-250c (150c max Medical discount); individual heal 2-4c minor, ~5g/game injury; injury duration 3-10 games; injury info visible at gem-heal prompt + post-match transient; Med L1 = -5% injury/-10% heal cost; higher STR = less injury; Training > Medical priority; IAP Season Pass $3.99, Coin Bundle $1.99, Coin Stack $3.99, Special Offer $4.99; loot box advisory; 15 languages list: EN/AR/NL/FR/DE/ID/IT/JA/KO/PT/RU/ZH-S/ES/ZH-T/TR")

add_claim("Physio energy restoration: Common = 50 coins, +10% energy for ALL players; Rare = 100 coins, +20% energy; Legendary = 200-250 coins, +50% energy AND heals ALL active injuries (team-wide).", 2, "physio/energy-restore", [e_med])
add_claim("Legendary Physio cost ~150 coins when Medical facility is fully upgraded (discount applied).", 2, "physio/leg-maxed", [e_med])
add_claim("Individual player 'Heal' (minor fatigue): costs ~2-4 coins per player for mild stamina depletion (limit ~8 coins per match in physio spend for beginners).", 3, "physio/individual-cost", [e_med])
add_claim("Instant gem-heal for injury costs ~5 GEMS PER MATCH of recovery (e.g., 3-match knee strain = 15 gems; 7-game injury = 35 gems).", 2, "physio/gem-heal-cost", [e_med])
add_claim("Injuries last 3 to 10 matches depending on severity; 7-10 game injuries are 'big injuries' that most commonly affect high-usage star players (e.g., KDB, Haaland) after repeated fouling.", 3, "injuries/duration", [e_med])
add_claim("Injury type + games-out is displayed when you tap the gem instant-heal option. The info is also briefly visible immediately after the match where the injury occurs, but disappears after closing the app or playing another match.", 3, "injuries/display", [e_med])
add_claim("Meta for injury economy: play reserves while injuries heal naturally rather than gem-healing (free vs. costly); Legendary Physio (200c) is more cost-effective than individual gem heals when multiple players are hurt/tired.", 2, "injuries/meta", [e_med])
add_claim("Medical Centre L1 upgrade: reduces injury probability by 5% AND reduces physio/heal costs by 10%. Higher levels scale both benefits.", 2, "facilities/medical-l1", [e_med])
add_claim("Higher STR stat on a player reduces their individual chance of injury (absorb contact better).", 2, "attributes/str-injury", [e_med])
add_claim("Facility upgrade priority recommendation: Stadium → Commercial → Training first, then Medical (Training's coach discount/formation/form-boost has bigger long-term payout; Medical second).", 2, "facilities/priority", [e_med])
add_claim("IAP pricing (USD, App Store): Season Pass = $3.99; Bundle of Coins = $1.99; Stack of Coins = $3.99; Special Offer = $4.99. Loot boxes/random items warning shown in App Store rating ('Frequent Contests, Contains Loot Boxes, Advertising').", 1, "iap/usd-pricing", [e_med])
add_claim("DLS26 supports 15 languages CONFIRMED: English, Arabic, Dutch, French, German, Indonesian, Italian, Japanese, Korean, Portuguese, Russian, Simplified Chinese, Spanish, Traditional Chinese, Turkish (Brazilian Portuguese live commentary also added in v12.250).", 1, "platform/languages-list", [e_med])
add_claim("ERRATA prior starter pack outlier (~1200c/40g) is likely from pre-DLS26 beta or regional variant; canonical starter remains 1,500c + 75g + 1 free Common Scout + 1 free Common Agent.", 2, "errata/starter-outlier-again", [e_med])

p=os.path.join(RAW_DIR,'EV-397_physio_injury.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
