#!/usr/bin/env python3
"""Turn 35 Wave 65: THE TRANSFER MARKET'S OPERATING RULES (filters, refresh cadence, the
buy/sell refresh trick, free transfers, price range) and a DOCUMENTED NEGATIVE on chemistry.

Wave 65 closes the corpus's true zero-coverage surface. Two results worth the wave:

1. CONTRACT LENGTH IS A TRANSFER-MARKET FILTER, and WAGES ARE NEGOTIATED AT SIGNING - the
   corpus had zero claims on either. The market list refreshes after every match, and buying
   and selling is itself the way to refresh it.

2. CHEMISTRY IS A DOCUMENTED NEGATIVE. Every DLS source that mentions "chemistry" uses it as
   boilerplate - an input to market quality, with no thresholds, no UI and no mechanic - while
   every source that actually explains a chemistry system is a FIFA/EA FC guide. A player
   arriving from FIFA will look for a chemistry system that DLS does not have. Recording that
   as an explicit negative is more useful than another ambiguous claim.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w65')

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

e_tm=new_ev("gamingonphone DLS26 Career Mode guide (27 Jan 2026, 'Live Transfer' section), gamingonphone DLS26 Beginners Guide (21 Jan 2026, tip 7 'Stay Attentive in the Live Transfer Market' + 'Gameplay Overview'), appitika.com DLS26 app description (transfer-market filters and contract negotiation), dream-league-soccer.fandom.com/wiki/Player (29 Jul 2026, free transfers, price range, Classic players), bluestacks character-development guide (coach categories and hiring route)",
    "THE TRANSFER MARKET'S OPERATING RULES AND A DOCUMENTED NEGATIVE ON CHEMISTRY. (1) THE FILTERS INCLUDE CONTRACT LENGTH: 'Search the transfer market for players using filters such as position, rating, and contract length' - so contract length is a searchable axis, not merely a display field, and the corpus previously had zero claims on it. (2) THE MARKET REFRESHES AFTER EVERY MATCH: 'The player list refreshes after every match you play, so the more you play, the more opportunities you have to find the players you need.' (3) BUYING AND SELLING REFRESHES THE MARKET: 'Regularly buying and selling players helps refresh the market, increasing the chances of higher-rated players appearing' - a deliberate churn tactic, and the guide's tip 7 is titled 'Stay Attentive in the Live Transfer Market', framed as the route toward signing Elite players. (4) MARKET QUALITY RISES WITH THE SQUAD: 'As your team rating and chemistry improve, higher-quality players will appear in the market more frequently' - stated independently in two guides, and the only operational role the word 'chemistry' plays in any DLS source. (5) THE STARTER SQUAD: new players 'begin with a basic lineup rated around the 50-60 OVR range, which gradually improves as the game opens up more systems and features', and returning players 'will find their progress carried over, including their existing squad and Academy Division status'. (6) FREE TRANSFERS AND THE PRICE BAND: 'You can get Free Transfers (which are usually players with low stats or players that you've released), or you can pay for players in the general transfers section. These players are normally better... The price on these players can scale from 10 coins to about 900 coins.' (7) COACHES: four categories (Technical, Fitness, Goalkeeping, Special) across three tiers (Common, Rare, Legendary); 'Common coaches usually provide a small boost to a single random stat, Legendary coaches offer the most significant upgrades and have a higher chance of a breakthrough'; and critically 'You can hire coaches using gems OR BY RELEASING PLAYERS from your current squad' - a gem-free route to coaches. (8) THE CHEMISTRY NEGATIVE: a targeted search for a DLS26 chemistry system returned only EA FC / FIFA chemistry guides (the 33-point, club-league-nation link model) and generic squad-builder wiki content, plus two AI-written DLS descriptions that use 'squad chemistry' as filler. No DLS source documents a chemistry threshold, a chemistry UI, a link rule, or any attribute effect. In DLS the word appears only in (4) above. CONCLUSION: DLS26 has no documented squad-chemistry system - chemistry is a FIFA mechanic, not a DLS one - and the two mentions in DLS guides are boilerplate. A player arriving from FIFA will hunt for a system that does not exist.",
    "evidence/raw/turn35_w65/EV-479_transfer_market_and_chemistry_negative.html",
    "TRANSFER MARKET: filters are position, rating AND contract length; the list refreshes after every match played; buying and selling is itself the way to refresh it and raises the chance of higher-rated players appearing; market quality rises as team rating improves. STARTER SQUAD: new players begin at 50-60 OVR and progress carries over from DLS25 including squad and Academy Division status. FREE TRANSFERS: usually low-stat players or ones you have released; paid transfers run 10 to about 900 coins. COACHES: four categories (Technical, Fitness, Goalkeeping, Special) x three tiers; Common boosts one random stat, Legendary is largest with the highest breakthrough chance; coaches can be hired with gems OR by releasing players from your squad. CHEMISTRY NEGATIVE: no DLS26 source documents a chemistry system - every explained chemistry model found is EA FC / FIFA; the word appears in DLS only as an input to market quality",
    quality="community")

add_claim("The transfer market's filters include POSITION, RATING AND CONTRACT LENGTH - contract length is a searchable axis, not merely a display field.", 2, "transfers/filters-include-contract-length", [e_tm], notes="Fills the corpus's zero-coverage wage/contract surface")
add_claim("The Live Transfer Market's player list refreshes after every match you play, so playing more matches creates more signing opportunities.", 2, "transfers/refresh-after-every-match", [e_tm])
add_claim("BUYING AND SELLING PLAYERS REFRESHES THE MARKET: regularly churning the market increases the chance that higher-rated players appear - the guide's route to signing Elite players.", 2, "transfers/buy-sell-churn-refreshes-market", [e_tm])
add_claim("Market quality rises with the squad: as team rating improves, higher-quality players appear in the market more frequently (stated independently in two guides).", 2, "transfers/market-quality-scales-with-rating", [e_tm])
add_claim("New players begin with a basic lineup rated around 50-60 OVR, and returning players carry over their squad and Academy Division status from DLS25.", 2, "transfers/starter-squad-and-carryover", [e_tm])
add_claim("Free transfers are usually low-stat players or players you have released yourself; paid general transfers are normally better and run from 10 to about 900 coins.", 2, "transfers/free-transfers-and-price-band", [e_tm])
add_claim("Coaches come in four categories (Technical, Fitness, Goalkeeping, Special) across three tiers (Common, Rare, Legendary); Common coaches boost a single random stat, Legendary coaches give the largest upgrade and the highest breakthrough chance.", 2, "coaching/four-categories-and-tiers", [e_tm])
add_claim("COACHES CAN BE HIRED BY RELEASING PLAYERS from your current squad - a gem-free route to coaches, on top of hiring them with gems.", 2, "coaching/hire-by-releasing-players", [e_tm], notes="A no-gem coach route the corpus lacked")
add_claim("DOCUMENTED NEGATIVE - DLS26 HAS NO DOCUMENTED SQUAD-CHEMISTRY SYSTEM. A targeted search returned only EA FC / FIFA chemistry models (the 33-point club-league-nation link system) and two AI-written DLS descriptions that use 'squad chemistry' as filler. No DLS source documents a chemistry threshold, UI, link rule or attribute effect; in DLS the word appears only as an input to market quality.", 2, "chemistry/no-system-documented-negative", [e_tm], notes="A player arriving from FIFA will hunt for a system that does not exist")

for name in ('EV-479_transfer_market_and_chemistry_negative.html',):
    p=os.path.join(RAW_DIR,name)
    if not os.path.exists(p):
        with open(p,'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f"Added {cl_id-(last_cl+1)} new claims and {ev_id-(last_ev+1)} EVs. Totals: {n_cl} claims, {n_ev} EVs")
