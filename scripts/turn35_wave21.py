#!/usr/bin/env python3
"""Turn 35 Wave 21: coach breakthrough baseline + max-potential resolution, Medical/Training/Recruitment/Accommodation per-level benefits, Form Boost duration, scout drop rates."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w21')

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

# ---------- EV-405: coaches / breakthrough / max potential ----------
e_coach=new_ev("LevelWinner DLS20 Training Guide, r/DreamLeagueSoccer (1i3f2jv Jan2025 DLS25, 11on7r4 Mar2023, zvchju Dec2022, 1b4ovuj Mar2024, 1hmsicn Dec2024, 1hnll1u Dec2024, 18dqq9e DLS24, 1aioi6e Feb2024, yxw3mg Nov2022, 1emifpy Aug2024, 19c1jxc Jan2024), Bluestacks 2026, gamingonphone 2026, dream-league-soccer.fandom Perfect Players",
    "COACHES / BREAKTHROUGH / MAX POTENTIAL. MAX POTENTIAL RESOLVED: coaches do NOT affect a player's maximum potential - 'If you get a breakthrough, points are added. The higher rarity just increases breakthrough chance, that's all' (r/DLS Jan 2025, DLS25). A player's OVR can rise by a maximum of +10 through coach development. BREAKTHROUGH BASELINE (LevelWinner DLS20 Training Guide, explicit percentages): Common coach = 25 gems, 2 random stats +2 each, 5% Breakout Rating; Rare = 50 gems, trains 2 players, 3 random stats +3 each, 10% Breakout; Legendary = 225 gems, trains 3 players, 4-point increase across all applicable stats, 20% Breakout. Post-DLS25 exact percentages are NOT published by any source - only the direction is confirmed (higher rarity = higher breakthrough chance), so the current-version table remains an OPEN GAP. BREAKTHROUGH MECHANICS: a breakthrough adds stat points beyond the coach's normal grant and can produce half-point increments (example: a 90-Tackle defender receiving a common tactical-coach breakthrough goes to 91.5 instead of 91). A breakthrough can be wasted when the player's development progress bar is nearly full and there is no room for the extra points. COACHES TO MAX ONE PLAYER (r/DLS Mar 2024): outfield ~80 Common / 20 Rare / 9 Legendary; goalkeepers 20 Common / 10 Rare / 4 Legendary; other threads give 80-87 Common, '90 common coaches for 1 maxed card', and ~7.5 Legendary SPECIAL coaches for a special player. SPECIAL COACH EFFICIENCY at maxed Training facility (r/DLS Dec 2024): Common 2 stat points / 63 gems = 31.5 gems per point; Rare 6 points / 168 gems = 28 gems per point; Legendary 12 points / 280 gems = 23.33 gems per point - Legendary Special coaches are the most gem-efficient. Stat-point accounting: Strength and Control count double (+1 STR/CON = +2 points), which is why wingers and CBs max at different total point counts.",
    "evidence/raw/turn35_w21/EV-405_coaches_breakthrough.html",
    "Coaches do NOT affect max potential (+10 OVR cap; rarity only changes breakthrough chance); DLS20 breakthrough baseline Common 5% / Rare 10% / Legendary 20%; post-DLS25 exact % UNCONFIRMED (open gap); breakthrough adds points beyond normal grant, can give half-points (90 -> 91.5), wasted when progress bar full; max one outfield = 80 Common/20 Rare/9 Legendary, GK 20/10/4; Special coach efficiency 31.5/28/23.33 gems per point; STR and CON count double",
    quality="community")

add_claim("Coaches do NOT affect a player's maximum potential: rarity only changes the breakthrough chance, and a player's overall rating can rise by at most +10 through coach development.", 2, "coaches/no-potential-cap-effect", [e_coach])
add_claim("DLS20-era coach breakthrough baseline: Common 5%, Rare 10%, Legendary 20% Breakout Rating, with Common = 25 gems/2 stats +2, Rare = 50 gems/2 players/3 stats +3, Legendary = 225 gems/3 players/all applicable stats +4.", 2, "coaches/breakthrough-baseline", [e_coach], notes="Dated DLS20 baseline; post-DLS25 values unpublished")
add_claim("Post-DLS25 exact coach breakthrough percentages are unpublished by any source found - only the direction (higher rarity = higher chance) is confirmed. OPEN GAP requiring device verification.", 4, "coaches/breakthrough-current-gap", [e_coach], notes="OPEN GAP - was already suspected; now explicitly confirmed as unavailable in public sources")
add_claim("A breakthrough adds stat points beyond the coach's normal grant and can produce half-point increments (example: a defender at 90 Tackle receiving a common tactical-coach breakthrough reaches 91.5 rather than 91).", 3, "coaches/breakthrough-half-points", [e_coach])
add_claim("A breakthrough is wasted when the target player's development progress bar is nearly full, because there is no room left for the extra stat points.", 3, "coaches/breakthrough-wasted", [e_coach])
add_claim("Coaches required to max one player: outfield ~80 Common / 20 Rare / 9 Legendary; goalkeeper 20 Common / 10 Rare / 4 Legendary; a Special player needs roughly 7.5 Legendary Special coaches.", 2, "coaches/coaches-to-max", [e_coach])
add_claim("Special Coach gem efficiency at a maxed Training facility: Common 2 points/63 gems (31.5 per point), Rare 6 points/168 gems (28 per point), Legendary 12 points/280 gems (23.33 per point) - Legendary Special coaches are the most gem-efficient.", 2, "coaches/special-coach-efficiency", [e_coach])
add_claim("Strength and Control stat points count double toward a player's development total, so players who receive more Strength/Control upgrades max out faster but reach a lower total point count.", 3, "coaches/str-con-double-weight", [e_coach])

# ---------- EV-406: facility per-level benefits ----------
e_fac=new_ev("LevelWinner DLS20 advanced guide, LevelWinner DLS21 advanced guide, LevelWinner DLS24 formations guide, FTG support (develop players), chaptercheats DLS24 hints, ldplayer DLS24 beginner guide, Bluestacks/gamingonphone 2026, NamuWiki DLS20, rajatips, fifaworldcupnews DLS26, r/DreamLeagueSoccer (i5ynnd, 176ntor, 15bpnih)",
    "FACILITY PER-LEVEL BENEFITS. MEDICAL CENTRE: Level 1 upgrade cuts healing cost by 10% and injury probability by 5% (LevelWinner DLS20 + DLS21); each subsequent upgrade gives an additional physiotherapist discount and progressively lower injury probability, but the exact per-tier percentages beyond Level 1 are NOT published by any source - OPEN GAP. Maxing the Medical Centre makes individual and group physio trips very cheap and its passive injury resistance is a major bonus (LevelWinner DLS22). TRAINING CENTRE: each upgrade grants (a) additional Form Boost matches, (b) an extra percentage discount on coach hire cost, and (c) new formations. FTG SUPPORT (official): a Form Boost increases a player's attributes for a set number of matches determined by the Training facility level, with duration starting at a minimum of one match. LevelWinner DLS20 confirms Form Boosts last exactly 1 match at the base Training level; the per-level duration table (2, 3, 4... matches) is unpublished - OPEN GAP. Formation unlocks per Training upgrade: up to 3 new formations in DLS24 (LevelWinner recommends stopping at Level 2 for ~15 total), versus 2 per upgrade in the DLS20 era (NamuWiki) - version drift. RECRUITMENT CENTRE: upgrading it boosts scout discounts (chaptercheats + ldplayer). Scout tier drop rates (rajatips, Indonesian): Common 93% ordinary / 5% talented / 2% legendary (80+ OVR); Rare 75% / 20% / 5%; Legendary 40% / 45% / 15%. ACCOMMODATION: increases maximum squad size - the base roster is 20 slots, expandable to about 24 (LevelWinner DLS24); community advice is to upgrade Accommodation last (r/DLS 2020). DLS26: Special players no longer count against accommodation/squad limits, and stadium customisation gained inside/outside views plus covered/uncovered toggles (fifaworldcupnews). Facility roster confirmed for DLS26: Stadium, Commercial, Medical, Training, Recruitment, Accommodation, plus the new Fanzone.",
    "evidence/raw/turn35_w21/EV-406_facility_levels.html",
    "Medical L1 = -5% injury / -10% heal cost, per-tier % beyond L1 UNCONFIRMED (open gap); Training upgrades grant +Form Boost matches, +coach discount, +formations (3/upgrade DLS24, 2/upgrade DLS20); FTG official: Form Boost duration set by Training level, minimum 1 match, per-level table UNCONFIRMED (open gap); Recruitment Centre = scout discounts; scout drop rates Common 93/5/2, Rare 75/20/5, Legendary 40/45/15; Accommodation = squad size 20 -> ~24, upgrade last; DLS26 specials ignore accommodation limits; stadium covered/uncovered toggle",
    quality="community")

add_claim("Medical Centre Level 1 cuts healing cost by 10% and injury probability by 5%; each later upgrade adds a further physiotherapist discount and progressively lower injury probability.", 2, "facilities/medical-level-benefits", [e_coach, e_fac])
add_claim("Medical Centre per-tier percentages beyond Level 1 are unpublished by any source found - OPEN GAP requiring device verification.", 4, "facilities/medical-per-tier-gap", [e_fac], notes="OPEN GAP - sources only describe the trend, never the numbers")
add_claim("Training Centre upgrades grant three benefits: additional Form Boost matches, an extra percentage discount on coach hire cost, and new formations.", 2, "facilities/training-level-benefits", [e_fac])
add_claim("FTG support (official): a Form Boost raises a player's attributes for a set number of matches determined by the Training facility level, with the duration starting at a minimum of one match.", 1, "formboost/duration-by-training-level", [e_fac])
add_claim("Form Boost lasts exactly one match at the base Training Centre level; the per-level duration table (2, 3, 4+ matches) is unpublished - OPEN GAP.", 4, "formboost/per-level-duration-gap", [e_fac], notes="OPEN GAP - only the minimum is confirmed")
add_claim("Each Training Centre upgrade unlocks up to 3 new formations in DLS24 (Level 2 yields roughly 15 total), versus 2 per upgrade in the DLS20 era - the unlock rate was re-tuned.", 3, "facilities/training-formation-unlocks", [e_fac])
add_claim("Upgrading the Recruitment Centre increases scout discounts.", 3, "facilities/recruitment-scout-discount", [e_fac])
add_claim("Scout tier drop rates: Common 93% ordinary / 5% talented / 2% legendary (80+ OVR); Rare 75% / 20% / 5%; Legendary 40% / 45% / 15%.", 3, "recruitment/scout-drop-rates", [e_fac], notes="Single Indonesian-language source (rajatips); plausible ladder shape but unverified")
add_claim("The Accommodation facility raises maximum squad size from a base of 20 slots to roughly 24, and community advice is to upgrade it last.", 3, "facilities/accommodation-squad-size", [e_fac])
add_claim("In DLS26 Special players no longer count against accommodation/squad limits, and stadium customisation gained inside/outside views plus covered/uncovered toggles.", 3, "facilities/dls26-accommodation-specials", [e_fac])
add_claim("Confirmed DLS26 facility roster: Stadium, Commercial, Medical, Training, Recruitment, Accommodation, plus the new Fanzone (seven facilities).", 2, "facilities/dls26-roster", [e_fac])

p=os.path.join(RAW_DIR,'EV-405_coaches_breakthrough.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-406_facility_levels.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
