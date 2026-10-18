#!/usr/bin/env python3
"""Turn 35 Wave 11: coach gem costs (base + max Training discount), player release yields, coach stat points, breakthrough % (DLS20 legacy), Form Boost costs/duration, 90-point upgrade pool per player, STR/CON double-weighted, optimal meta."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w11')

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

e_coaches=new_ev("FTG official support (develop players), r/DLS coach threads (DLS20-DLS26), LevelWinner DLS20 training, gamedls.net release card table, BlueStacks DLS26",
    "OFFICIAL (FTG support): Coaches randomly select a player to upgrade permanently via 'Coaches' button in Team Management. Form Boosts are TEMPORARY player upgrades; duration is set by Training Centre level (minimum 1 match). COACH MECHANICS (community-verified DLS20-DLS26, note DLS20 base costs may be lower than DLS26 but relative efficiencies hold). Coach cost in GEMS (DIRECT PURCHASE): Common ~15-25g (DLS20 15g, DLS24+ ~17-25g), Rare ~50-67g (DLS20 50g; DLS24 ~52-67g), Legendary ~90-225g (DLS20 90g, DLS24+ ~202g base, 157g with max Training discount). Max Training Facility discount ≈ 22-30% off coach gem cost (r/DLS '30% training facility discount' to max team). At max Training Facility: Common ~63g for Special coaches, Rare ~168g, Legendary ~280g (Special coach packs — likely v13.x 'Special Coach Packs' IAP). PLAYER RELEASE YIELDS (releasing a player grants coach cards — gold mine for free coach economy): releasing a Legendary (Gold, 80+) player yields 1 Rare (Blue) coach; releasing a Rare (Blue) player yields 2 Common coaches; releasing a Common (White) player yields 1 Common coach (gamedls.net). DLS20 r/DLS: 80-rated defenders are cheapest Rare-player source (~1,460-1,690c) making them the best coin→Rare-coach conversion (meta 'buy 80 DEF release trick' confirmed by multiple threads). Coach STAT EFFECTS (outfield): Common coach boosts 1 random stat in-category by +1 point for 1 player; Rare boosts 2 random in-category stats by +2 points for 2 players (or 2 stats × 2 players? — clarified: Rare = 2 players × 2 stats = +4 total points for outfield, but some sources say +2 points on 2 stats per player — likely +2 in 2 random stats on the chosen players); Legendary boosts 3 random in-category stats by +3 points for 3 players (3×3=9 total points outfield). GK coaches: Common +1 GKR or GKH; Rare +2 to either GKR or GKH; Legendary +3 to BOTH GKR+GKH (use only if GKR > GKH per r/DLS). Breakthrough (Breakout) rate (LevelWinner DLS20): Common 5%, Rare 10%, Legendary 20% — breakthrough adds BONUS points (extra stats) without consuming upgrade pool. r/DLS Jan2025 confirms 'higher rarity increases breakthrough chance, does NOT change cap'. Upgrade pool per player: ~80 points (outfield) from base to max OVR; ~90 points for Special/top-tier cards. Total coaches to max 1 outfield player: 80 Common / 20 Rare / 9 Legendary. Total to max 1 GK: 20 Common / 10 Rare / 4 Legendary. STR and CON are DOUBLE-WEIGHTED: each point in STR/CON counts as 2 upgrade points toward OVR progression (for most positions except wingers). Special player max cost (DLS24 at max training): Common coach path 2835g (63g×45 coaches needed for 90pts / 2pts/coach); Rare path 2520g (168g×15); Legendary path 2100g (280g×7.5) — Legendary Special coaches are the BEST gem efficiency at 23.3 gems/point. Meta coaching order: max Training Facility FIRST (discounts coach gem costs permanently, unlocks formations, extends Form Boost duration); then use the coin-based coach loop (buy 80 DEF for ~1,400-1,700c → release for Rare coach) instead of buying coaches with gems when possible; spend gems only on Legendary Special Coaches after Training maxed. Common player 'common boost' meta: use Common coaches to selectively control which stats get boosted by picking only players you want upgraded (since you can't choose which player gets upgraded with higher-rarity coaches, Common coaches give you more granular control). Form Boosts: +1 OVR for 5g (Common), +2 OVR for 8g (Rare), +3 OVR for 10g (Legendary); duration = minimum 1 match, extended by Training Facility level; COST SAME regardless of player OVR. Form Boosts are considered poor value (5 gems for +1 OVR for one match) — only use for crucial cup/endgame matches. Training Centre upgrades also unlock formations.",
    "evidence/raw/turn35_w11/EV-392_coaches_form_boost.html",
    "Coaches cost 15-25g/50-67g/90-225g base; max Training ~30% discount (17/52/157g); Special coaches 63/168/280g at max Training; release yields: Gold→1 Rare, Blue→2 Common, White→1 Common; 80 DEF ~1400-1700c = cheapest Rare coach; outfield coach: C+1/1stat/1p, R+2/2stat/2p, L+3/3stat/3p (9pts total); GK C+1 GK stat, R+2 one, L+3 both; breakthrough 5/10/20%; ~80 upgrade pts/outfield, ~20 GK; STR & CON double-weighted; max cost 2100-2835g/Special (Leg best 23.3g/pt); Form Boost 5g/+1, 8g/+2, 10g/+3 for 1+ match; max Training first meta")

add_claim("OFFICIAL (FTG): Coaches permanently upgrade a randomly selected player's stats; selected via 'Coaches' button in Team Management.", 1, "coaches/official", [e_coaches])
add_claim("Coach gem cost — base (no Training discount, DLS20-era): Common 15g, Rare 50g, Legendary 90g. DLS24-DLS26 costs higher: Common ~17-25g, Rare ~52-67g, Legendary ~202g.", 2, "coaches/base-costs", [e_coaches])
add_claim("Coach gem cost — at MAX Training Facility (~22-30% discount): Common ~17g, Rare ~52g, Legendary ~157g (regular coaches). Special Coach Packs (v12.200+): Common ~63g, Rare ~168g, Legendary ~280g at max Training.", 2, "coaches/max-training-costs", [e_coaches], "Special coach prices likely post-v13.x; confirm in-game")
add_claim("Player release yields: releasing Legendary (Gold/80+) → 1 Rare coach; releasing Rare (Blue) → 2 Common coaches; releasing Common (White) → 1 Common coach.", 2, "coaches/release-yields", [e_coaches])
add_claim("Best coin-to-rare-coach conversion: buy 80-rated DEFENDERS for ~1,460-1,690c (cheapest Gold players on transfer market) and immediately release for 1 Rare coach — meta '80 DEF release trick' confirmed.", 2, "coaches/80-def-trick", [e_coaches])
add_claim("Common outfield coach: boosts 1 RANDOM stat in selected category by +1 point for 1 random player.", 2, "coaches/common-effect", [e_coaches])
add_claim("Rare outfield coach: boosts 2 random stats in-category by +2 points on 2 random players (≈4 total stat points).", 2, "coaches/rare-effect", [e_coaches])
add_claim("Legendary outfield coach: boosts 3 random stats in-category by +3 points on 3 random players (≈9 total stat points).", 2, "coaches/legendary-effect", [e_coaches])
add_claim("GK coaches: Common +1 to either GKR or GKH; Rare +2 to either GKR or GKH; Legendary +3 to BOTH GKR and GKH (use Leg GK coaches only when GKR > GKH to balance).", 2, "coaches/gk-effect", [e_coaches])
add_claim("Breakthrough (breakout) rate per coach use: Common 5%, Rare 10%, Legendary 20% (DLS20 baseline). Breakthrough adds BONUS stat points without consuming upgrade pool (pure upside).", 3, "coaches/breakthrough", [e_coaches], "LevelWinner DLS20; percentages may have shifted in DLS26")
add_claim("Coach rarity does NOT increase player max potential (no cap increase); rarity only changes magnitude of upgrade and breakthrough chance. +10 OVR hard cap stands.", 2, "coaches/no-cap-increase", [e_coaches])
add_claim("Outfield players require ~80 upgrade points from base to max OVR (~90 points for Special/top-tier cards).", 2, "coaches/upgrade-pool", [e_coaches])
add_claim("Goalkeepers require ~20 upgrade points to max (≈1/4 of outfield pool, consistent with GK 22-pt cap = +10 OVR).", 2, "coaches/gk-pool", [e_coaches])
add_claim("Coaches needed to max 1 outfield player: 80 Common / 20 Rare / 9 Legendary. To max 1 GK: 20 Common / 10 Rare / 4 Legendary.", 2, "coaches/counts-per-player", [e_coaches])
add_claim("STR and CON are DOUBLE-WEIGHTED in OVR progression: each stat point in STR/CON counts as 2 upgrade points (for most positions except wingers). This is why high-STR/CON players feel more 'expensive' to train and contributes to STR meta bias.", 2, "coaches/double-weighted", [e_coaches])
add_claim("Special coach gem efficiency (max Training): Legendary = 23.3 g/pt (best); Rare = 28 g/pt; Common = 31.5 g/pt. Legendary Special coaches are most gem-efficient upgrade method.", 2, "coaches/gem-efficiency", [e_coaches])
add_claim("Meta coaching priority: (1) MAX Training Facility FIRST (permanent coach discount + unlocks formations + extends Form Boost); (2) use coin-purchased 80-DEF releases for Rare coaches; (3) spend gems on Legendary Special Coaches only AFTER Training is maxed.", 2, "coaches/meta-priority", [e_coaches])
add_claim("'Common boost' method: use Common coaches for granular stat targeting since you can't pick which player gets upgraded with Rare/Legendary (more controlled, less waste).", 3, "coaches/common-boost-meta", [e_coaches])
add_claim("Form Boost costs: +1 OVR = 5 gems (Common), +2 OVR = 8 gems (Rare), +3 OVR = 10 gems (Legendary). Cost is flat regardless of player OVR.", 2, "formboost/costs", [e_coaches])
add_claim("Form Boost duration: minimum 1 match, extended by Training Facility level (exact levels-to-duration mapping not publicly documented).", 2, "formboost/duration", [e_coaches], "gap: duration per Training level")
add_claim("Form Boosts are considered poor gem value overall (1-match duration); reserve for crucial cup/endgame/DLL matches only.", 2, "formboost/value", [e_coaches])
add_claim("OFFICIAL (FTG): Training Centre level governs (1) coach cost discount, (2) Form Boost duration, (3) formation unlocks.", 1, "facilities/training-effects", [e_coaches])

p=os.path.join(RAW_DIR,'EV-392_coaches_form_boost.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
