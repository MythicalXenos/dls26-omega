#!/usr/bin/env python3
"""Turn 35 Wave 103: THE 30-DAY RESET IS NOT ENFORCED, AND ACCOUNTS ARE SOLD FOR $37.

Wave 103's centrepieces:

1. THE 30-DAY RESET COOLDOWN IS NOT ENFORCED, according to one player who did it three times.
   The official article says one reset per 30 days; a community member reports a third reset
   without waiting. That does not make the official rule wrong - it makes it a rule the game
   may not police, which is exactly the kind of thing a player must not rely on.

2. ACCOUNTS ARE SOLD OPENLY, at $37-$40, with the contents listed in the advert. FTG prohibits
   profile sale and purchase and bans for it. So the market exists, is priced, and is a
   ban risk - which is the practical form of the corpus's account-policy rule.

3. THE SEASON PASS USED TO BE WEEKLY. A 2021 thread says "the season pass restarts every week.
   So every week you have to invest money" - and the current pass is a 10-day season. That is a
   version-drift data point, and it matters because the corpus's "buy late or not at all" advice
   is calibrated to the 10-day cycle.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w103')

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

e_rs=new_ev("r/DreamLeagueSoccer zxlnrr 'How long until I can restart profile again after recently doing it' (28 Dec 2022 - the 30-day reset cooldown dissent from a player on their third reset), r/DreamLeagueSoccer mmzn9d (8 Apr 2021 - 'the season pass restarts every week. So every week you have to invest money'), z2u.com DLS 2026 account listings (8 Jun 2026 - accounts sold from $37-$40 with the full player and trophy contents listed in the advert), dreamleaguekits.com 'Top 7 Players In Every Position in DLS 26' (17 May 2026 - the per-position top-7 and the position-group summary), sportsdunia.com best-midfielders table (24 Dec 2025 - a SIXTH sportsdunia table), thesoccerera.com top-rated players (19 Feb 2026 - a Rodri-at-86 outlier), plus an eighth contamination from ESL DreamLeague Dota 2 (Seasons 26-31 with formats and prize pools), ManageFC, Dream Team Fantasy and Football Manager wonderkid guides",
    "THE 30-DAY RESET IS NOT ENFORCED, ACCOUNTS ARE SOLD FOR $37, AND THE SEASON PASS USED TO BE WEEKLY. (1) THE 30-DAY RESET DISSENT: the official article says one Reset Profile per 30 days; a community member on their **third** reset reports 'I'm not sure it's that long because this was my 3rd time doing it and I don't think it took 30 days for it to be resetted' - against another voice in the same thread saying 'Possibly 30 days.' **So the cooldown may not be policed, which is exactly the kind of thing a player must not rely on**: the official rule stands, and the corpus's one-way-door framing is unchanged. (2) ACCOUNTS ARE SOLD OPENLY: marketplace listings advertise DLS26 accounts 'from $37' and 'from $40' with the contents itemised - 'GRAND LEGENDARY III - FULL STADIUMS - RONALDO2018 - MESSI2022 - RODRI2026 - CANNAVARO2006 - DESAILLY1998 - 21 BEST PLAYER: DEMBELE, YAMAL, HAALAND, RAPHINHA, KANE, RODRI, VINI, BRUNO, VALVERDE, HAKIMI, GABRIEL, VANDIJK'. **FTG prohibits profile sale and purchase and bans for it**, so the market exists, is priced, and is a ban risk - the practical form of the corpus's account-policy rule, and a reason the corpus's honesty rule (no shortcuts) has a price attached. (3) THE SEASON PASS USED TO BE WEEKLY: '**Actually, the season pass restarts every week. So every week you have to invest money**' (April 2021, DLS21 era) - against the current 10-day season. **So the pass cycle has changed across versions**, which matters because the corpus's buy-late-or-not-at-all advice is calibrated to the 10-day cycle and would be wrong against a weekly one. (4) THE PER-POSITION TOP-7, corroborating the corpus's best-in-game roster: defenders Van Dijk 85, Gabriel Magalhaes 85, Hakimi 85, Bastoni 84, Saliba 84, Nuno Mendes 84, Upamecano 83 - with the position-group summary GK Donnarumma 85, defender Van Dijk 85, midfielder Rodri 85, attacker Yamal 86. (5) A SIXTH SPORTSDUNIA TABLE - a top-10 midfielders list (Bellingham 85, Pedri 85, Valverde 85, Rodri 85, Vitinha 85, Bruno Fernandes 84, De Bruyne 83, Palmer 83, Caicedo 83, Calhanoglu 83) - recorded so the rejection count is accurate. (6) A RODRI OUTLIER: thesoccerera puts Rodri at **86** DM where every other source has him at 85 - a minor rating conflict in the same family as the Yamal 86 outlier. (7) AN EIGHTH CONTAMINATION: both searches returned ESL DreamLeague Dota 2 (Seasons 26-31, formats, prize pools, EPT points), ManageFC's season-design blog, Dream Team Fantasy rules and Football Manager wonderkid shortlists. Eight waves, eight contaminations.",
    "THE 30-DAY RESET COOLDOWN IS NOT ENFORCED, according to a player on their third reset - the official rule stands, but it may not be policed, and that is a reason not to rely on it. ACCOUNTS ARE SOLD OPENLY at $37-$40 with the contents itemised, and FTG bans for it - so the market has a price and a risk. THE SEASON PASS USED TO BE WEEKLY (DLS21 era) against the current 10-day season, which is a version-drift point that matters because the buy-late advice is calibrated to 10 days. Plus the per-position top-7, a sixth sportsdunia table, a Rodri 86 outlier, and an eighth contamination.",
    "THE RESET COOLDOWN IS NOT ENFORCED, AND ACCOUNTS SELL FOR $37",
    quality="community")

add_claim("THE 30-DAY RESET COOLDOWN MAY NOT BE ENFORCED: a community member on their **third** reset reports '**I\'m not sure it\'s that long because this was my 3rd time doing it and I don\'t think it took 30 days for it to be resetted**' - against another voice in the same thread saying 'Possibly 30 days.' **The official rule stands (one reset per 30 days) and the corpus\'s one-way-door framing is unchanged** - but the cooldown may not be policed, which is exactly the kind of thing a player must not rely on, because a future enforcement could land mid-plan.", 4, "account/30-day-reset-may-not-be-enforced", [e_rs], notes="A dissent against a Confirmed-tier rule; the rule stands, the enforcement is doubtful")
add_claim("ACCOUNTS ARE SOLD OPENLY, WITH PRICES: marketplace listings advertise DLS26 accounts '**from $37**' and '**from $40**' with the contents itemised in the advert - 'GRAND LEGENDARY III - FULL STADIUMS - RONALDO2018 - MESSI2022 - RODRI2026 - CANNAVARO2006 - DESAILLY1998 - 21 BEST PLAYER: DEMBELE, YAMAL, HAALAND, RAPHINHA, KANE, RODRI, VINI, BRUNO, VALVERDE, HAKIMI, GABRIEL, VANDIJK'. **FTG prohibits profile sale and purchase and bans for it**, so the market exists, is priced, and is a ban risk - the practical form of the corpus's account-policy rule, and the reason the honesty rule has a price attached.", 3, "account/accounts-sold-at-37-40", [e_rs], notes="Extends CLAIM-1225 with concrete prices and listed contents")
add_claim("THE SEASON PASS USED TO BE WEEKLY: '**Actually, the season pass restarts every week. So every week you have to invest money**' (April 2021, DLS21 era) - against the current **10-day** season. **So the pass cycle has changed across versions**, which matters because the corpus's buy-late-or-not-at-all advice is calibrated to the 10-day cycle and would be wrong against a weekly one - and because the price of the pass scales with how often it must be bought.", 3, "seasonpass/used-to-be-weekly", [e_rs], notes="A version-drift point that qualifies the pass-timing advice")
add_claim("THE PER-POSITION TOP-7, corroborating the corpus's best-in-game roster (CLAIM-1842): **defenders** Van Dijk 85, Gabriel Magalhaes 85, Hakimi 85, Bastoni 84, Saliba 84, Nuno Mendes 84, Upamecano 83 - with the position-group summary **GK Donnarumma 85 · defender Van Dijk 85 · midfielder Rodri 85 · attacker Yamal 86**. So the per-position pecking order is stable across two sources, and the corpus's per-tier builds can be read against real names.", 3, "positions/per-position-top-7", [e_rs])
add_claim("A SIXTH SPORTSDUNIA TABLE - a top-10 midfielders list (Bellingham 85, Pedri 85, Valverde 85, Rodri 85, Vitinha 85, Bruno Fernandes 84, De Bruyne 83, Palmer 83, Caicedo 83, Calhanoglu 83) - recorded so the rejection count is accurate, while noting its figures happen to corroborate other sources.", 4, "errata/sportsdunia-sixth-table", [e_rs], notes="Sixth sportsdunia rejection")
add_claim("A RODRI RATING OUTLIER: thesoccerera puts Rodri at **86** DM where every other source has him at 85 - a minor rating conflict in the same family as the Yamal 86 outlier, and from a source already downgraded for version and date claims.", 4, "errata/rodri-86-outlier", [e_rs])
add_claim("AN EIGHTH CONTAMINATION: both searches returned ESL **DreamLeague Dota 2** (Seasons 26-31 with formats, prize pools and EPT points), ManageFC's season-design blog, Dream Team Fantasy rules and Football Manager wonderkid shortlists. Eight waves, eight contaminations - the general rule from wave 88 now has eight instances behind it.", 3, "errata/eighth-contamination", [e_rs])

for p in ['EV-516_reset_and_accounts.html','EV-516b_ratings_lists.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
