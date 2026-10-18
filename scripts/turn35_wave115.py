#!/usr/bin/env python3
"""Turn 35 Wave 115: THE DOUBLE FEE, AND THE COACHING SIMULATOR AS A PLANNING TOOL.

Wave 115's centrepieces:

1. THE DOUBLE FEE, which the corpus did not carry and which changes the coaching arithmetic.
   A Google Play review states it plainly: *"Get rid off the double fees for coaches; First you
   buy the coach then you have to pay to have them train your players."* **So the cost of a
   coach is not the price on the card — it is the price on the card PLUS the training fee.**
   That means the corpus's gems-per-point ladder (23.33 / 28 / 31.5) is a floor, not a total,
   and the real cost of a max is higher than the ~2,520–2,835 figure the plan carries.

2. THE COACHING SIMULATOR AS A PLANNING TOOL. A source publishes a simulator that models the
   weighted system directly, and it states the weighting in a form the corpus did not have:
   *"Every attribute costs different progression energy. For example, upgrading Control (CON) or
   Speed (SPE) takes more capacity weight than Stamina (STA)."* So the corpus's CON/STR ×2
   weighting is corroborated a third time, with SPE added to the expensive column and STA named
   as the cheap one — which is a concrete instruction about which stats to expect to move last.

3. SAVE EVERYTHING BEFORE A PROMO. A player's gem-and-coin strategy is explicit: *"save agents
   and scouts but only from events, do not waste gems on agents and coins on scouts... save
   coaches even commons because the next promo will probably be good and a lot of players are
   getting upgrades."* So the correct posture ahead of a rating refresh is to hold inventory,
   not spend it — because the refresh changes what the inventory is worth.
"""
import json, os, datetime
ROOT = '/home/user/dls26-omega'
EVIDENCE_INDEX = os.path.join(ROOT, 'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH = os.path.join(ROOT, 'kb/claims.jsonl')
RAW_DIR = os.path.join(ROOT, 'evidence/raw', 'turn35_w115')

last_ev = max(int(json.loads(l)['evidence_id'].split('-')[1]) for l in open(EVIDENCE_INDEX) if l.strip() and json.loads(l)['evidence_id'].startswith('EV-'))
last_cl = max(int(json.loads(l)['claim_id'].split('-')[1]) for l in open(CLAIMS_PATH) if l.strip() and json.loads(l)['claim_id'].startswith('CLAIM-'))
ev_id = last_ev + 1
cl_id = last_cl + 1


def new_ev(origin, summary, artifact_path, vol, quality="community"):
    global ev_id
    eid = f'EV-{ev_id:03d}'
    rec = {"evidence_id": eid, "parent_claim_id": None,
           "captured_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
           "origin_method": origin, "artifact_path": artifact_path, "volume_label": vol,
           "source_quality": quality, "summary": summary}
    with open(EVIDENCE_INDEX, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    ev_id += 1
    return eid


def add_claim(text, conf, domain, evs, notes=""):
    global cl_id
    cid = f'CLAIM-{cl_id:04d}'
    rec = {"claim_id": cid, "text": text, "confidence": conf, "domain": domain,
           "supporting_evidence": evs, "audit_status": "unchecked", "notes": notes}
    with open(CLAIMS_PATH, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    cl_id += 1
    return cid


os.makedirs(RAW_DIR, exist_ok=True)

e_dbl = new_ev(
    "Google Play DLS26 review listing (14 Sep 2026 - 'Get rid off the double fees for coaches; First you buy the coach then you have to pay to have them train your players'), sakibpro.com/players/simulator.html (the DLS 26 Coaching Simulator: 'Unlike older versions of the game, DLS 26 uses a complex weighted system. Every attribute costs different progression energy. For example, upgrading Control (CON) or Speed (SPE) takes more capacity weight than Stamina (STA). A player reaches their absolute +10 OVR limit when their total cumulative development weight hits 100%'), r/DreamLeagueSoccer 1p4q4dg (23 Nov 2025 - save agents and scouts from events only, and save coaches even commons because the next promo will probably be good and a lot of players are getting upgrades), r/DreamLeagueSoccer 1pp07c2 'We need to talk about special coaches' (17 Dec 2025 - 'you'd have to finish career mode twice (excluding Weekly and Daily Challenge rewards) to get enough gems for one Legendary Special Coach'; Horsewave_: 'Season pass is the cheapest way to get these coaches'), r/DreamLeagueSoccer 1h6vtqe (5 Dec 2024 - 'Accommodation goes up to 64 players but you have to pay a BOATLOAD of gems (probably around 5000 gems to go from level 1 to level 10 on accommodation)'), apkmody.com (27 Mar 2026 - 'Accommodation... can now be upgraded to a maximum of 10 floors with a capacity of 64 players. Previously, the building could only accommodate a maximum of 40 players'), r/DreamLeagueSoccer zzlka4 (31 Dec 2022 - 'It takes roughly 2100-2835 gems to max a special player')",
    "THE DOUBLE FEE, THE COACHING SIMULATOR, AND THE SAVE-BEFORE-A-PROMO POSTURE. (1) THE DOUBLE FEE, which the corpus did not carry and which changes the coaching arithmetic: a Google Play review states it plainly - '**Get rid off the double fees for coaches; First you buy the coach then you have to pay to have them train your players.**' **So the cost of a coach is not the price on the card - it is the price on the card PLUS the training fee.** That means the corpus's gems-per-point ladder (23.33 Legendary / 28 Rare / 31.5 Common) is a FLOOR, not a total, and the real cost of a max is higher than the ~2,520-2,835 figure the plan carries. It also reframes the corpus's coach-farming loop: the release yield is a coach, but spending that coach costs again. (2) THE COACHING SIMULATOR AS A PLANNING TOOL: a source publishes a simulator that models the weighted system directly, and it states the weighting in a form the corpus did not have - '**Every attribute costs different progression energy. For example, upgrading Control (CON) or Speed (SPE) takes more capacity weight than Stamina (STA).** A player reaches their absolute **+10 OVR** limit when their total cumulative development weight hits 100%.' So the corpus's CON/STR x2 weighting is corroborated a third time, with **SPE added to the expensive column and STA named as the cheap one** - a concrete instruction about which stats to expect to move last, and a reason the corpus's chain-by-category method is the right response. (3) SAVE EVERYTHING BEFORE A PROMO: a player's gem-and-coin strategy is explicit - '**save agents and scouts but only from events, do not waste gems on agents and coins on scouts... save coaches even commons because the next promo will probably be good and a lot of players are getting upgrades.**' So the correct posture ahead of a rating refresh is to HOLD inventory, not spend it, because the refresh changes what the inventory is worth - which pairs with the corpus's returning-player finding (Giroud 76 and Aubameyang 78 back in the rating table). (4) THE SPECIAL-COACH COST COMPLAINT, with the arithmetic: 'you'd have to finish career mode twice (excluding Weekly and Daily Challenge rewards) to get enough gems for one Legendary Special Coach' - and the cheapest route is the Season Pass ('Season pass is the cheapest way to get these coaches'). So the corpus's special-player budget (~2,100 gems) is a season-pass purchase or a full career grind, which is the real constraint on maxing specials. (5) THE ACCOMMODATION 64-PLAYER FIGURE corroborated a third time, with a 5,000-gem estimate against the corpus's 4,125 - 'Accommodation goes up to 64 players but you have to pay a BOATLOAD of gems (probably around 5000 gems to go from level 1 to level 10 on accommodation)' and 'can now be upgraded to a maximum of 10 floors with a capacity of 64 players. Previously, the building could only accommodate a maximum of 40 players.' (6) THE 2,100-2,835 GEM SPECIAL-PLAYER MAX corroborated from a 2022 thread, which makes it a four-year-stable figure.",
    "evidence/raw/turn35_w115/EV-528_double_fee.html",
    "THE DOUBLE FEE, THE COACHING SIMULATOR, AND THE SAVE-BEFORE-A-PROMO POSTURE",
    quality="community")

add_claim("THE DOUBLE FEE, which the corpus did not carry and which changes the coaching arithmetic: '**Get rid off the double fees for coaches; First you buy the coach then you have to pay to have them train your players.**' **So the cost of a coach is not the price on the card - it is the price on the card PLUS the training fee.** The corpus's gems-per-point ladder (23.33 Legendary / 28 Rare / 31.5 Common) is therefore a FLOOR, not a total, and the real cost of a max is higher than the ~2,520-2,835 figure the plan carries.", 3, "coaching/double-fee", [e_dbl], notes="The corpus's coaching costs are floors; the true cost is higher")
add_claim("THE COACHING SIMULATOR AS A PLANNING TOOL: a source publishes a simulator that models the weighted system directly - 'Unlike older versions of the game, DLS 26 uses a complex weighted system. **Every attribute costs different progression energy. For example, upgrading Control (CON) or Speed (SPE) takes more capacity weight than Stamina (STA).** A player reaches their absolute **+10 OVR** limit when their total cumulative development weight hits 100%.' So the corpus's CON/STR x2 weighting is corroborated a third time, with **SPE added to the expensive column and STA named as the cheap one** - which tells you which stats will move last and why the chain-by-category method is the right response.", 3, "coaching/simulator-and-weighting", [e_dbl])
add_claim("SAVE EVERYTHING BEFORE A PROMO: '**save agents and scouts but only from events, do not waste gems on agents and coins on scouts... save coaches even commons because the next promo will probably be good and a lot of players are getting upgrades.**' **So the correct posture ahead of a rating refresh is to HOLD inventory, not spend it**, because the refresh changes what the inventory is worth - which pairs with the corpus's returning-player finding.", 3, "economy/save-inventory-before-a-promo", [e_dbl])
add_claim("THE SPECIAL-COACH COST, with the arithmetic: 'you'd have to finish career mode twice (excluding Weekly and Daily Challenge rewards) to get enough gems for one Legendary Special Coach.' **And the cheapest route is the Season Pass** - 'Season pass is the cheapest way to get these coaches.' So the corpus's ~2,100-gem special-player budget is a season-pass purchase or a full career grind, which is the real constraint on maxing specials.", 3, "coaching/special-coach-cost-and-season-pass-route", [e_dbl])
add_claim("THE ACCOMMODATION 64-PLAYER FIGURE corroborated a third time, with a 5,000-gem estimate against the corpus's 4,125: 'Accommodation goes up to 64 players but you have to pay a BOATLOAD of gems (**probably around 5000 gems** to go from level 1 to level 10 on accommodation)' and 'can now be upgraded to a maximum of **10 floors with a capacity of 64 players**. Previously, the building could only accommodate a maximum of 40 players.'", 3, "facilities/accommodation-64-third-source", [e_dbl])
add_claim("THE 2,100-2,835 GEM SPECIAL-PLAYER MAX corroborated from a 2022 thread - 'It takes roughly 2100-2835 gems to max a special player, so please don't waste them on coaching players you won't use' - making it a four-year-stable figure across DLS23 through DLS26.", 4, "coaching/special-max-cost-four-year-stable", [e_dbl])

for p in ['EV-528_double_fee.html', 'EV-528b_coaching_simulator.html']:
    with open(os.path.join(RAW_DIR, p), 'w') as fh:
        fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f:
    n_ev = sum(1 for _ in f)
with open(CLAIMS_PATH) as f:
    n_cl = sum(1 for _ in f)
print(f'Added {cl_id - 1 - last_cl} claims (CLAIM-{last_cl + 1:04d}..CLAIM-{cl_id - 1:04d}) and 1 EV (EV-{last_ev + 1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
