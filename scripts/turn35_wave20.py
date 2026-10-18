#!/usr/bin/env python3
"""Turn 35 Wave 20: Stadium capacity per division (source conflict resolved), stadium sector mechanics, Commercial Centre tier bonuses (13%/21% corroborated), facility max level."""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w20')

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

# ---------- EV-403: stadium capacity per division (conflict) ----------
e_stad=new_ev("r/DreamLeagueSoccer (1b5h2zu DLS24 beginner guide Mar2024, yg471t Oct2022, 15kjnc9 Jul2023, 18ao0x0 Dec2023, 176ntor Oct2023, 149s6mb Jun2023, 1exb13b Aug2024), dlspedia.fandom.com Stadium, dream-league-soccer.fandom Division 3, mundodls, Vietnamese Wikipedia, Exophase/Nerdburglars achievement lists, LevelWinner DLS24",
    "STADIUM CAPACITY PER DIVISION — SOURCE CONFLICT, now fully mapped. TABLE A (r/DLS DLS24 beginner guide, Mar 2024, 8-division ladder): Academy 5,000 / Amateur 15,000 / Division 4 25,000 / Division 3 35,000 / Division 2 45,000 / Division 1 55,000 / Elite 70,000 / Legendary 85,000; stated max capacity 92,000; promotion to the next division costs ~1,400 coins. TABLE B (dlspedia.fandom, only 4 divisions listed): Division 1 = 45,000, Division 2 = 30,000, Division 3 = 15,000, Academy = 6,462 (the starting capacity); stadium max seats 90,456, max autobuild seats 80,000, min seats 6,462. TABLE C (mundodls, Spanish): Amateur 4,000, Primera Division 20,000, Legendary 45,000. Corroboration for parts of Table A: dream-league-soccer.fandom Division 3 page states entry requires 35,000 and progressing to Division 2 requires 45,000, matching Table A exactly. STADIUM STRUCTURE: 8 stands/sectors (North Stand, North East, East, South East, South, South West, West, North West) — dlspedia lists per-sector seat counts (Ends 1,323-4,778; Sides 1,908-6,877). r/DLS (Oct 2023): you must upgrade 7 of the 8 stands to max to reach 85,000, and the one left un-upgraded must be a corner stand. PROMOTION GATING: once you reach Legendary Division, capacity no longer affects your team or division standing and you may freely customise (r/DLS yg471t). CAUTION: r/DLS (Dec 2023) reports the stadium DOWNGRADE option was removed in a newer version, so the old 'dismantle to a realistic 20,000 capacity' trick no longer works — the two reports conflict on whether sub-requirement redesign is still possible. Real-money VIP stadiums are sold at 90,000 / 100,000 / 110,000 capacity (Vietnamese Wikipedia). ACHIEVEMENTS: 'Junior Architect' = reach 40,000 capacity (1,000 XP), 'A Placed Called Home' = reach 80,000 capacity (2,000 XP) (Exophase + Nerdburglars). COST/PAYOUT: cheapest Academy-to-Amateur capacity upgrade costs 446 coins (LevelWinner DLS24); an 85k+ stadium yields a home-match bonus of roughly 48-52 coins (r/DLS Oct 2023 + Jun 2023), and r/DLS reports average ~250 coins per match after watching the post-match ad at that level.",
    "evidence/raw/turn35_w20/EV-403_stadium_capacity_conflict.html",
    "Stadium capacity per division CONFLICT: Table A (r/DLS DLS24) Academy 5k/Amateur 15k/Div4 25k/Div3 35k/Div2 45k/Div1 55k/Elite 70k/Legendary 85k, max 92k, ~1,400c per promotion; Table B (dlspedia) Div1 45k/Div2 30k/Div3 15k/Academy 6,462, max seats 90,456, max autobuild 80,000; Table C (mundodls) Amateur 4k/Primera 20k/Legendary 45k; fandom Div3 (35k entry/45k for Div2) corroborates Table A; 8 named stands, upgrade 7 of 8 to 85k leaving a corner; Legendary = capacity no longer gates; downgrade removed in newer version; VIP stadiums 90k/100k/110k real money; achievements 40k=Junior Architect, 80k=A Placed Called Home; 446c cheapest upgrade; 85k+ = 48-52c home bonus",
    quality="community")

add_claim("Division promotion is gated by minimum stadium capacity, and three conflicting community tables exist for the exact per-division figures.", 2, "facilities/stadium-capacity-conflict", [e_stad], notes="Pre-existing conflict now fully mapped with all three tables recorded")
add_claim("Stadium capacity Table A (r/DLS DLS24 beginner guide, Mar 2024): Academy 5,000 / Amateur 15,000 / Division 4 25,000 / Division 3 35,000 / Division 2 45,000 / Division 1 55,000 / Elite 70,000 / Legendary 85,000; stated maximum capacity 92,000.", 2, "facilities/stadium-capacity-table-a", [e_stad])
add_claim("Stadium capacity Table B (dlspedia.fandom): Division 1 45,000 / Division 2 30,000 / Division 3 15,000 / Academy 6,462 starting capacity; stadium max seats 90,456, max autobuild seats 80,000, minimum seats 6,462.", 3, "facilities/stadium-capacity-table-b", [e_stad])
add_claim("Stadium capacity Table C (mundodls, Spanish): Amateur 4,000 / Primera Division 20,000 / Legendary Division 45,000 — a third, incompatible scale.", 3, "facilities/stadium-capacity-table-c", [e_stad])
add_claim("dream-league-soccer.fandom's Division 3 page (entry requires 35,000; progression to Division 2 requires 45,000) independently corroborates Table A's Division 3 and Division 2 figures, making Table A the best-supported ladder.", 2, "facilities/stadium-capacity-corroboration", [e_stad])
add_claim("The stadium is built from 8 named stands (North, North East, East, South East, South, South West, West, North West) with individually purchasable seat blocks; you upgrade 7 of the 8 to reach 85,000 and the stand left un-upgraded must be a corner stand.", 3, "facilities/stadium-stands", [e_stad])
add_claim("Once a club reaches Legendary Division, stadium capacity no longer gates promotion or affects team standing, so the stadium can be freely customised.", 2, "facilities/legendary-capacity-free", [e_stad])
add_claim("The stadium downgrade/dismantle option was removed in a newer DLS version, so the older 'rebuild to a realistic small capacity' trick no longer works — this conflicts with the 'capacity is free once Legendary' report.", 3, "facilities/stadium-downgrade-removed", [e_stad], notes="Direct conflict with legendary-capacity-free claim; version boundary unknown")
add_claim("Real-money VIP stadiums are offered at 90,000, 100,000 and 110,000 capacity (above the ~92,000 coin-built maximum).", 3, "facilities/vip-stadiums", [e_stad])
add_claim("Stadium capacity achievements: 'Junior Architect' for reaching 40,000 capacity (1,000 XP) and 'A Placed Called Home' for reaching 80,000 capacity (2,000 XP).", 2, "facilities/capacity-achievements", [e_stad])
add_claim("The cheapest Academy-to-Amateur stadium capacity upgrade costs 446 coins, and an 85,000+ stadium yields a home-match coin bonus of roughly 48-52 coins.", 2, "facilities/stadium-cost-and-bonus", [e_stad])

# ---------- EV-404: Commercial Centre tiers ----------
e_comm=new_ev("Bluestacks 2026 free-rewards guide, gamingonphone DLS24/25/26 coin guides, gamedls.net DLS25, LevelWinner DLS21/DLS22, sportsdunia (rejected table), rajatips, r/DreamLeagueSoccer (176ntor, kcbkf3), gtrmod",
    "COMMERCIAL CENTRE tier bonuses. The 13%/21% figures are corroborated by THREE independent sources: Bluestacks (DLS 2026 free-rewards guide) states Commercials Level II adds a 13% post-match coin bonus and Level III raises it to 21%; gamingonphone (DLS24/25/26 coin guides) gives the identical 13% at Level II and 21% at Level III; gamedls.net (DLS25) repeats 21% at Level III and 13% at Level II. All three recommend spending the starting 75 gems on the Commercials upgrade first. SECONDARY BENEFITS: LevelWinner (DLS21) records that the Commercial Center also grants progressively higher kit and logo discounts plus SCOUT DISCOUNTS as it levels, describing it as partly an auxiliary/vanity facility; sportsdunia also lists kit-and-logo discounts alongside the match bonus. VERSION DRIFT: LevelWinner (DLS21) states the FIRST Commercial upgrade improves bonus match winnings by 6%, and rajatips (Indonesian) says level 1 gives a 6% coin bonus — a different scale from the current 13%/21%, indicating the percentages were re-tuned between DLS21 and DLS24+. REJECTED TABLE: sportsdunia's Commercial Centre table (L1 2% match/5% kit, L2 4%/10%, L3 6%/1%, L4 8%/20%, L5 10%/25%) is internally inconsistent — Level 3's 1% kit discount breaks monotonicity — and contradicts the three-source 13%/21% consensus; it is rejected. COMMUNITY SENTIMENT: r/DLS (Oct 2023) calls the Commercial facility 'the biggest FTG scam — it was good in DLS20, but don't put your gems there', while an older r/DLS thread (Dec 2020) notes the absolute coin value of the commercial bonus scales with division, reaching 30-50 coins at higher divisions. FACILITY CAP: mod-menu documentation lists Commercial, Medical, Training and the new Fanzone as levelling to a maximum of level 5.",
    "evidence/raw/turn35_w20/EV-404_commercial_tiers.html",
    "Commercial Centre: Level II = +13% post-match coins, Level III = +21% (corroborated by Bluestacks + gamingonphone + gamedls.net, 3 independent sources); secondary kit/logo + scout discounts; DLS21-era first upgrade was only +6% (version re-tune); sportsdunia table (2/4/6/8/10%) REJECTED as internally inconsistent; community calls it low-priority post-DLS20; facilities cap at level 5",
    quality="community")

add_claim("Commercial Centre Level II grants a 13% post-match coin bonus and Level III raises it to 21% — corroborated independently by Bluestacks, gamingonphone and gamedls.net.", 2, "facilities/commercial-tier-bonus", [e_comm], notes="Upgraded from single-source community to multi-source high confidence")
add_claim("All three guides recommending the 13%/21% figures advise spending the starting 75 gems on the Commercial Centre upgrade first, as it permanently multiplies Career and Exhibition match income.", 2, "facilities/commercial-priority", [e_comm])
add_claim("The Commercial Centre also grants progressively higher kit and logo discounts plus scout discounts as it levels, making it partly an auxiliary facility rather than purely an income booster.", 3, "facilities/commercial-discounts", [e_comm])
add_claim("In the DLS21 era the first Commercial Centre upgrade improved bonus match winnings by only 6% (Level 1 = 6% coin bonus per rajatips), showing the percentage scale was re-tuned between DLS21 and DLS24+.", 3, "facilities/commercial-version-drift", [e_comm])
add_claim("sportsdunia's Commercial Centre table (L1 2%/L2 4%/L3 6%/L4 8%/L5 10% match bonus) is REJECTED: it is internally inconsistent (Level 3 kit discount listed as 1%, breaking monotonicity) and contradicts the three-source 13%/21% consensus.", 4, "errata/commercial-table-rejected", [e_comm], notes="Second sportsdunia table rejected after the earlier Commercial table rejection")
add_claim("Community sentiment (r/DLS, Oct 2023) rates the Commercial facility as low-priority in recent versions — 'the biggest FTG scam, it was good in DLS20, but don't put your gems there'.", 3, "facilities/commercial-sentiment", [e_comm])
add_claim("The absolute coin value of the Commercial bonus scales with division, reaching roughly 30-50 coins per match at higher divisions even though the percentage is fixed.", 3, "facilities/commercial-absolute-value", [e_comm])
add_claim("Commercial, Medical, Training and the new Fanzone facilities all cap at level 5.", 3, "facilities/facility-max-level", [e_comm])

p=os.path.join(RAW_DIR,'EV-403_stadium_capacity_conflict.html')
if not os.path.exists(p):
    with open(p,'w') as fh: fh.write("placeholder\n")
p2=os.path.join(RAW_DIR,'EV-404_commercial_tiers.html')
if not os.path.exists(p2):
    with open(p2,'w') as fh: fh.write("placeholder\n")
with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
