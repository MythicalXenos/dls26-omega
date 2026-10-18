#!/usr/bin/env python3
"""Turn 35 Wave 34: OFFICIAL FTG Form Boost documentation (Training-level-gated duration, min 1 match), coach random-selection rule, Form Boost cost/variance, Clan point economy (~3.5k/online win, 350k cap, top-contributor gems), clan creation cost, clan season totals, Prize Ladder Cult-Heroes lead."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w34')

last_ev=max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl=max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id=last_ev+1; cl_id=last_cl+1

def new_ev(origin, summary, artifact_path, vol, quality="official"):
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

# ---------- EV-428: official Form Boost + coaches ----------
e_fb=new_ev("FTG support article 360003914778 'How do I develop my players?' (official, updated Dec 2024), LevelWinner DLS20 Training Guide + DLS21 Advanced Guide, r/DreamLeagueSoccer 1ew85gh (Aug 2024), r/DLS 1gbkyq0 (Oct 2024), gamingonphone DLS26 Career Guide, ldplayer, chaptercheats",
    "OFFICIAL FORM BOOST DOCUMENTATION (FTG support 360003914778, updated 2024-12-06): 'Coaches will then randomly select a player to permanently upgrade. For more powerful but temporary player upgrades, give them a Form Boost. This will increase your player's attributes for a set number of matches as detailed by your Training facilities level (duration starts at a minimum of one match).' This closes the FORM BOOST MECHANIC gap officially - duration is gated by the Training facility level with a floor of one match - but the exact per-level match counts remain unpublished, so the numeric ladder is still OPEN. Two further official-adjacent facts from the same article: COACHES SELECT A PLAYER AT RANDOM (not player-chosen), and coach upgrades are PERMANENT while Form Boosts are temporary. DLS20/21 BASELINE: Form Boosts lasted exactly one match and cost 5 gems for +1 OVR, 8 gems for +2 and 10 gems for +3, with the price identical for all players regardless of rating. FORM BOOST VARIANCE (r/DLS 1ew85gh): boosts are RANDOM in which attributes they raise - a player can receive only +2 strength or +4/+5, and a +4 OVR jump is possible when the boosted stats land favourably (28 boosted card points versus 26, counting strength and control as 2 each), which can push a card over a rating threshold. Community criticism: the Training facility also GATES FORMATIONS ('formations should not be gatekept by training facility'), and commercial upgrades at ~1,250 gems were judged poor value.",
    "evidence/raw/turn35_w34/EV-428_form_boost_official.html",
    "OFFICIAL: Form Boost duration = 'a set number of matches as detailed by your Training facilities level', minimum one match - mechanic now documented but the per-level match counts remain UNPUBLISHED (gap still open on the numbers only); OFFICIAL: coaches select a player at RANDOM and coach upgrades are permanent; DLS20/21 baseline: one match duration, 5g=+1 OVR, 8g=+2, 10g=+3, price flat across ratings; form boosts are random in which attributes they raise and a +4 OVR jump is possible (28 vs 26 boosted card points); Training facility also gates formations (criticised); commercial ~1,250 gems judged poor value",
    quality="official")

add_claim("OFFICIAL (FTG support): a Form Boost increases a player's attributes for a set number of matches as detailed by the Training facility level, with a duration floor of one match.", 1, "formboost/duration-gated-by-training", [e_fb], notes="Mechanic documented; the exact per-level match counts are still unpublished")
add_claim("OFFICIAL (FTG support): coaches randomly select which player to permanently upgrade - the manager does not choose the recipient of a coach card.", 1, "training/coach-random-selection", [e_fb])
add_claim("DLS20/DLS21 baseline: a Form Boost lasted exactly one match and cost 5 gems for +1 OVR, 8 gems for +2 and 10 gems for +3, with the price identical for all players regardless of rating.", 2, "formboost/cost-oot-baseline", [e_fb])
add_claim("Form Boosts are random in which attributes they raise - a player can receive only +2 strength or +4/+5, and a +4 OVR jump occurs when the boosted card points total 28 versus 26 (counting strength and control as 2 each), pushing the card over a rating threshold.", 3, "formboost/attribute-variance", [e_fb])
add_claim("The Training facility gates access to FORMATIONS as well as Form Boost duration and coach discounts, which the community criticises as arbitrary gating.", 2, "training/gates-formations", [e_fb])
add_claim("OPEN GAP: the exact Form Boost duration in matches for each Training facility level (2 through 5) has never been published by FTG or any community source.", 4, "formboost/per-level-duration-open", [e_fb], notes="Official wording confirmed; numeric ladder still missing")

# ---------- EV-429: clan point economy ----------
e_cp=new_ev("r/DreamLeagueSoccer 1pk9dae (Dec 2025, clan leader thread, Spanish), 1tp8zg7 (May 2026 monthly clan thread), 1peo0q2 (Dec 2025 promote/join thread), dlsmod.com DLS Clans + DLS 26 Review, FTG support 30839289076626 'What are Clans', sportsdunia Clans guide, TikTok Evans DLS (Prize Ladder classics)",
    "CLAN POINT ECONOMY. Roughly 3,500 Clan Points are earned per ONLINE MATCH WIN, so the 350,000 individual contribution cap corresponds to about 100 online wins per season. CONTRIBUTION CAP: a single member can contribute at most 350,000 points to the clan total; anything earned beyond that only serves to rank that member first inside the clan and win the top-contributor gem reward at the end of the season. TOP-CONTRIBUTOR REWARD CONFLICT: a Spanish-language clan leader thread states the clan's number-one contributor receives 50 gems at season end, whereas sportsdunia states the highest clan points earn 100 gems - the figure is unresolved. CLAN CREATION costs 150 gems and dlsmod notes you barely break even in the first season unless the clan is highly active. SEASON TOTALS: active clans report roughly 13-15 million Clan Points per season with a 350,000+ member requirement, while others target an 8 million season prize; a second-tier clan reaches 10-11 million with 200-350k contributors. REWARD LADDER (sportsdunia): the first reward unlocks at 25,000 Clan Points, then 25 gems at 1,000,000, a Legendary XP boost at 2,000,000, a Legendary Scout at 3,000,000, 500 coins at 5,000,000, a Rare Special Coach at 7,500,000 and 150 gems at 10,000,000. JOIN CONDITIONS (official FTG support): some clans set entry requirements and are then hidden from search, but an invite code still bypasses them. CLAN CREATION OPTIONS: badge (style, background, icon, frame colour, dressing), name, country, entry requirements (minimum team rank) and type (open, closed, invite-only). PRIZE LADDER LEAD: a TikTok datamine claims upcoming Prize Ladder players include Roy Keane (rating and year not revealed), Irvin at 85 (year not revealed), Conor Gallagher and Peter Robinson - consistent with the Cult Heroes collection but unconfirmed.",
    "evidence/raw/turn35_w34/EV-429_clan_point_economy.html",
    "~3,500 Clan Points per online win (so the 350k individual cap = ~100 online wins per season); anything above 350k only ranks you first in-clan for the top-contributor gem reward; CONFLICT on top-contributor reward (50 gems per a Spanish clan-leader thread vs 100 gems per sportsdunia); clan creation costs 150 gems and barely breaks even in season one; active clans earn 13-15M CP/season, others target 8M, second-tier 10-11M; reward ladder 25k first, then 25g@1M, Leg XP@2M, Leg Scout@3M, 500c@5M, Rare Special Coach@7.5M, 150g@10M; entry requirements hide clans from search but invite codes bypass; creation options include badge/name/country/min rank/type; Prize Ladder Cult Heroes lead: Roy Keane, Irvin 85, Conor Gallagher, Peter Robinson",
    quality="community")

add_claim("Roughly 3,500 Clan Points are earned per online match win, so the 350,000 individual contribution cap corresponds to about 100 online wins in a season.", 3, "clans/points-per-online-win", [e_cp])
add_claim("A single clan member can contribute at most 350,000 points to the clan total; points earned beyond that only rank that member first inside the clan for the top-contributor gem reward.", 2, "clans/contribution-cap-meaning", [e_cp])
add_claim("CONFLICT on the clan top-contributor reward: a Spanish-language clan leader thread states 50 gems at season end for the clan's number-one contributor, while sportsdunia states 100 gems - unresolved.", 3, "clans/top-contributor-reward-conflict", [e_cp], notes="C-017 candidate")
add_claim("Creating a clan costs 150 gems and barely breaks even in the first season unless the clan is highly active.", 3, "clans/creation-cost", [e_cp])
add_claim("Active clans report roughly 13-15 million Clan Points per season with a 350,000+ member contribution requirement, while some target an 8 million season prize and a second-tier clan reaches 10-11 million with 200-350k contributors.", 3, "clans/season-totals", [e_cp])
add_claim("Clan reward ladder: first reward at 25,000 Clan Points, then 25 gems at 1M, a Legendary XP boost at 2M, a Legendary Scout at 3M, 500 coins at 5M, a Rare Special Coach at 7.5M and 150 gems at 10M Clan Points.", 3, "clans/reward-ladder", [e_cp])
add_claim("Clan join conditions set by a leader hide that clan from search results, but an invite code still allows entry regardless of requirements.", 1, "clans/invite-code-bypass", [e_cp])
add_claim("Clan creation customisation covers badge (style, background, icon, frame colour, dressing), clan name, clan country, entry requirements by minimum team rank, and clan type (open, closed, invite-only).", 3, "clans/creation-options", [e_cp])
add_claim("LEAD: upcoming Prize Ladder players reportedly include Roy Keane (rating and year unrevealed), Irvin at 85 (year unrevealed), Conor Gallagher and Peter Robinson - consistent with the Cult Heroes collection but unconfirmed.", 4, "prizeladder/cult-heroes-lead", [e_cp], notes="Cult Heroes official card list still open")

p=os.path.join(RAW_DIR,'EV-428_form_boost_official.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-429_clan_point_economy.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
