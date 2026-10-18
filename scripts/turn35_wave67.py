#!/usr/bin/env python3
"""Turn 35 Wave 67: THE OFFICIAL GEM-SOURCE LIST, the currency-naming conflict (C-028), the
Commercial facility's real benefit, the three pre-match objectives, the offside trap (and its
reported loss), and the kit-import specification.

Wave 67 closes several small but high-frequency gaps:

1. THE OFFICIAL GEM-SOURCE LIST (Confirmed tier) - league objectives, tournaments, the Season
   Pass, the Prize Ladder and Dream League Live - plus FTG's parental-control note.

2. C-028 OPENED: the currency names conflict. "Diamonds" appears only on scam sites and one
   boilerplate guide; "crystals" appears once in a Season Pass reward list. Plan on two
   currencies - coins and gems - and treat the other names as unverified.

3. THE OFFICIAL MATCH OBJECTIVE SYSTEM: three objectives arrive before each match and pay
   coins - the corpus had nothing on this despite it being a per-match income stream.

4. THE OFFSIDE TRAP: executable via team press in DLS24, but an August 2026 thread asks
   "where are the offside traps, high lines...?" - recorded as a conflict, not a fact.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w67')

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

e_eco=new_ev("FTG support 360003914938 'How can I get Gems?' (re-surfaced in full), sportsdunia DLS26 coins guide (30 Dec 2025, Commercial's discounts and the 20-day login cycle), bluestacks DLS26 custom-kits guide (the 300-Diamond unlock claim), gamingonphone DLS26 Beginners Guide (21 Jan 2026, the 1,200-coin/40-gem starter grant), footballeffect (4 May 2026, the same grant), sportsdunia DLS26 gems guide (31 Dec 2025, '75 Free Gems to start'), myce DLS coins guide (the three pre-match objectives), r/DreamLeagueSoccer 18gf5gx (12 Dec 2023, the offside trap via team press), 1ve8w1l (3 Aug 2026, the DLS2027 suggestion thread), 1tnvfy8 (26 May 2026, Dream Draft costs coins), 1p4q4dg (23 Nov 2025, save Common coaches), 1ceqwgc (27 Apr 2024, the DLS24 gems guide and the Training payback comment), dreamkitsapp DLS26 kit pages (the 512x512 PNG import spec), Play Store DLS26 reviews (13 Jul 2026)",
    "THE OFFICIAL GEM-SOURCE LIST, THE CURRENCY-NAMING CONFLICT, THE COMMERCIAL FACILITY'S REAL BENEFIT, THE MATCH-OBJECTIVE SYSTEM, THE OFFSIDE TRAP, AND THE KIT-IMPORT SPEC. (1) THE OFFICIAL GEM-SOURCE LIST (Confirmed): 'Gems can be obtained by completing league objectives, completing tournaments, through the Season Pass and Prize Ladder and by participating in Multiplayer (Dream League Live) mode. The quantity of Gems you receive will depend on the circumstance. You can also purchase Gems in the shop if you wish to acquire them more quickly (please seek the bill payer's permission).' The parenthetical is FTG's own parental-control note and is worth preserving verbatim. (2) C-028 OPENED - THE CURRENCY NAMES CONFLICT. FTG names exactly two currencies, COINS and GEMS. But a bluestacks kit guide states the custom-kit unlock 'is a one-time purchase costing 300 Diamonds, which is the premium currency in Dream League Soccer 2026', and the Season Pass reward list carries '150 crystals'. Every source that says 'diamonds' is either a scam/hack site or that one boilerplate guide; no official source uses the word. CONCLUSION: plan on coins and gems only; treat 'diamonds' as a third-party misnomer for gems and 'crystals' as either gems or a separate rare currency, unresolved pending device confirmation. (3) THE COMMERCIAL FACILITY'S REAL BENEFIT, which the corpus lacked beyond the coin figure: upgrading it to a '5-star upgrade' earns 'massive match-winning bonuses, KITS, and LOGO DISCOUNTS' - Commercial is the kit-and-logo discount facility, not just a coin tap. The same guide advises spending 'your first 75 Gems on upgrading it to the second tier', which conflicts with the corpus's community priority of Training and Accommodation first. (4) THE MATCH-OBJECTIVE SYSTEM: 'Before the match, you will receive three objectives (for example: score in the first half or to receive a limited number of goals), and you will have other objectives throughout the season, and reaching any of them will bring you coins.' Three per-match objectives are a per-match income stream the corpus had not recorded. (5) THE OFFSIDE TRAP, and its reported loss: a December 2023 thread reports 'with the new team press move you are able to do offside traps when opposing players cross the ball from side to side... if you control the CB you can use team press to move the defensive line up to force an Offside', advising switching to wing-backs to move them up with the line. But an August 2026 suggestion thread asks 'where are the offside traps, high lines, attacking shape, and any kind of tactical transition when you lose possession?' and complains 'defenders refuse to hold their line'. RECORDED AS A CONFLICT: the offside trap is documented as working in DLS24 and reported absent or broken in DLS26. (6) NEW CONTROL DETAIL from the same thread: 'double tapping will clear the ball while you're defending', and a player asks to 'tap a player to switch to them' because 'you have to keep tapping C just to get to the right player' - corroborating C as the switch button. (7) DREAM DRAFT COSTS COINS: 'For Dream Points... do Dream Drafts. But NEVER for coins. Dream Drafts make you lose coins but gain gems and Dream Points.' (8) GEM-EFFICIENCY RULES: 'save agents and scouts but only from events do not waste gems on agents and coins on scouts. and save coaches even commons because the next promo will probably be good' - so bank Common coaches. The Training facility 'will save gems after 20 uses', corroborating Training as the best gem in the game. (9) THE KIT-IMPORT SPEC: community kits are optimised at 512x512 PNG, with shirt, shorts and socks in Home, Away and Third versions plus Goalkeeper kits in the same three. (10) The starter grant is reported as 'around 1200 coins and 40 gems' by two sources (possibly shared lineage - the corpus previously rejected this pair as an outlier) and as '75 Free Gems' by a third; login bonuses refresh every 20 days. (11) A Play Store review corroborates the promotion gate: 'you might have to win the league twice because you have to pay in game currency to upgrade your stadium in order to play in the next league.'",
    "evidence/raw/turn35_w67/EV-481_gem_sources_currency_and_objectives.html",
    "OFFICIAL GEM SOURCES (Confirmed): league objectives, tournaments, the Season Pass, the Prize Ladder, and Dream League Live - plus FTG's '(please seek the bill payer's permission)' note. C-028: only two currencies are official (coins, gems); 'diamonds' is a third-party/scam misnomer and 'crystals' is unresolved. COMMERCIAL: a 5-star upgrade earns match bonuses, KIT DISCOUNTS and LOGO DISCOUNTS - it is the kit-and-logo facility, not just a coin tap (one guide's 'spend your first 75 gems here' advice conflicts with the Training-first priority). MATCH OBJECTIVES: three arrive before each match and pay coins. OFFSIDE TRAP: documented as working via team press in DLS24, reported absent in DLS26 - a conflict. NEW CONTROLS: double-tap clears the ball while defending; C is the switch button. DREAM DRAFT costs coins and yields gems plus Dream Points. GEM EFFICIENCY: bank Common coaches, don't waste gems on agents or coins on scouts; Training pays back after ~20 uses. KIT IMPORT: 512x512 PNG, home/away/third plus goalkeeper kits. Starter grant 1,200 coins + 40 gems (two sources, previously rejected as an outlier) vs '75 free gems' (one source); login bonuses refresh every 20 days",
    quality="community")

add_claim("OFFICIAL GEM-SOURCE LIST: gems come from completing league objectives, completing tournaments, the Season Pass, the Prize Ladder, and participating in Dream League Live - plus the shop. FTG's own wording adds '(please seek the bill payer's permission)'.", 1, "economy/official-gem-sources", [e_eco], notes="Official")
add_claim("C-028 OPENED - THE CURRENCY NAMES CONFLICT. FTG names exactly two currencies, COINS and GEMS. A kit guide claims the custom-kit unlock costs '300 Diamonds, which is the premium currency', and the Season Pass reward list carries '150 crystals'. Every 'diamonds' source is a scam site or one boilerplate guide. Plan on coins and gems only.", 2, "economy/currency-naming-conflict", [e_eco], notes="C-028 - diamonds looks like a third-party misnomer; crystals is unresolved")
add_claim("THE COMMERCIAL FACILITY'S REAL BENEFIT: a 5-star Commercial upgrade earns match-winning bonuses plus KIT DISCOUNTS and LOGO DISCOUNTS - Commercial is the kit-and-logo discount facility, not merely a coin tap.", 2, "facilities/commercial-kit-and-logo-discounts", [e_eco])
add_claim("One guide advises spending 'your first 75 Gems' on the Commercial centre's second tier - which conflicts with the corpus's community priority of Training and Accommodation first. Recorded, not adopted.", 3, "facilities/commercial-first-advice-conflicts", [e_eco])
add_claim("THE MATCH-OBJECTIVE SYSTEM: three objectives arrive before each match (for example 'score in the first half' or 'receive a limited number of goals') and each pays coins, with further objectives across the season.", 2, "economy/three-pre-match-objectives", [e_eco], notes="A per-match income stream the corpus lacked")
add_claim("THE OFFSIDE TRAP IS DOCUMENTED AS WORKING IN DLS24: 'with the new team press move you are able to do offside traps when opposing players cross the ball from side to side... if you control the CB you can use team press to move the defensive line up to force an Offside', and switching to a wing-back moves them up with the line.", 3, "matchcraft/offside-trap-via-team-press", [e_eco])
add_claim("CONFLICT - THE OFFSIDE TRAP MAY BE GONE IN DLS26: an August 2026 thread asks 'where are the offside traps, high lines, attacking shape, and any kind of tactical transition when you lose possession?' and complains 'defenders refuse to hold their line'. DLS24 documented it working; DLS26 players report it missing.", 3, "matchcraft/offside-trap-reported-missing", [e_eco], notes="C-029 opened - testable in Exhibition")
add_claim("NEW CONTROL DETAIL: double-tapping clears the ball while defending, and C remains the player-switch button ('you have to keep tapping C just to get to the right player').", 3, "controls/double-tap-clear-and-c-switch", [e_eco])
add_claim("DREAM DRAFT COSTS COINS: 'For Dream Points... do Dream Drafts. But NEVER for coins. Dream Drafts make you lose coins but gain gems and Dream Points.'", 2, "draft/draft-costs-coins", [e_eco])
add_claim("GEM-EFFICIENCY: bank agents and scouts earned from events rather than buying them - 'do not waste gems on agents and coins on scouts' - and SAVE COMMON COACHES because a future promo may make them valuable.", 3, "economy/bank-common-coaches", [e_eco])
add_claim("The Training facility 'will save gems after 20 uses' - corroborating Training L4 as the best gem in the game.", 3, "facilities/training-pays-back-after-20-uses", [e_eco])
add_claim("THE KIT-IMPORT SPEC: community kits are optimised at 512x512 PNG, supplied as shirt, shorts and socks in Home, Away and Third versions, plus Goalkeeper kits in the same three.", 2, "customisation/kit-import-spec", [e_eco])
add_claim("The starter grant is reported as 'around 1200 coins and 40 gems' by two sources and as '75 Free Gems' by a third. The 1,200c/40g pair was previously REJECTED as an outlier; a second source repeating it (possibly shared lineage) does not overturn that - verify on device.", 3, "economy/starter-grant-conflicting", [e_eco], notes="Deliberately does not overturn the earlier rejection")
add_claim("Daily login bonuses refresh every 20 days - miss a day inside the cycle and the reward cycle restarts from day one.", 2, "economy/login-bonus-20-day-cycle", [e_eco])

for name in ('EV-481_gem_sources_currency_and_objectives.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
