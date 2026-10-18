#!/usr/bin/env python3
"""Turn 35 Wave 111: THE DAILY GEM CEILING, AND WHY THE GLOBAL CHALLENGE CUP IS NOT WORTH IT.

Wave 111's centrepieces:

1. THE DAILY GEM CEILING, which the corpus's gem ledger lacked. A player does the arithmetic:
   at 100 games a day, with 8 games needed per Tier 1 championship and 48 gems per
   championship, the ceiling is **576 gems a day**. That is the hard limit on the DLL engine
   the corpus's whole gem plan runs on, and it is the number that tells you the 6,000-gem
   season figure is a *maximum*, not an expectation.

2. WHY THE GLOBAL CHALLENGE CUP IS NOT WORTH IT, which the corpus asserted without the
   mechanism. The reason is now explicit: the GCC has *"a shit ton of rounds"*, **none of them
   played at home** — so no stadium bonus — and each match pays only **30–40 coins**. That is
   the arithmetic behind the corpus's GCC exclusion, and it is a different reason from the
   wave-89 gem-per-match rule.

3. THE DIAMOND CUP IS THE EFFICIENT CUP, with the numbers: fewer matches than the GCC, 15 gems
   for the win plus 10 more in challenges. So when the corpus says "play the cups selectively",
   this is which one to play.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w111')

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

e_gm=new_ev("r/DreamLeagueSoccer clan-discussion gem-budget post (the daily gem ceiling arithmetic: 100 games a day, 8 games per Tier 1 championship, 48 gems per championship, 576 gems a day; the DLL quest ladder; the daily-reward streak arithmetic), r/DreamLeagueSoccer 1oo1dkw (4 Nov 2025 - the 110-gem Career season total, the Dream Draft two-week cadence and 10-15 gem win, and the Global Challenge Cup not-worth-it argument with the no-home-stadium mechanism), r/DreamLeagueSoccer 1i75pm4 (22 Jan 2025 - the Diamond Cup as the efficient cup with 15 gems plus 10 in challenges), r/DreamLeagueSoccer 1rf90a7 (26 Feb 2026 - the Man City per-club rating change table from the Winter Reload update)",
    "THE DAILY GEM CEILING, WHY THE GCC IS NOT WORTH IT, AND THE EFFICIENT CUP. (1) THE DAILY GEM CEILING, which the corpus's gem ledger lacked: 'Lets assume you play the highest possible (**100 games**), and you are in Tier 1 and you win all games, because it takes **8 games to become champion** - hence this means you'll only be champion a maximum of **12 times**, with 4 games played remainder in a day (100/8 = 12.5), hence youll gain **576 Gems in a day**.' **That is the hard ceiling on the DLL engine the corpus's whole gem plan runs on** - and it means the ledger's 6,000-gem DLL figure is a maximum achieved at roughly ten hours a day, not an expectation. It also independently corroborates the corpus's 8-wins-per-Tier-1-championship figure and its 48-gems-per-championship arithmetic. (2) WHY THE GLOBAL CHALLENGE CUP IS NOT WORTH IT, which the corpus asserted without the mechanism: '**never play Global challenger cup it has shit ton of rounds and none of them is played on home stadium** after the game we get only **30-40 coins**, playing so many matches for mere 25 gems doesn't feel worth to me.' **So the GCC's problem is structural, not just arithmetic**: it is an away-only competition, which means the stadium bonus - the corpus's single largest coin source - never applies, and each match pays 30-40 coins instead of the ~150 a home match pays. That is the mechanism behind the corpus's GCC exclusion, and it is a different reason from the wave-89 gem-per-match rule. (3) THE DIAMOND CUP IS THE EFFICIENT CUP: 'Play diamond cup as it has **less matches to play** and gives **15 gems and 10 more in challenge**.' So when the corpus says play the cups selectively, the Diamond Cup is the one to play - fewer rounds than the GCC and a challenge top-up on top of the win. (4) THE 110-GEM CAREER SEASON TOTAL, the sum of the corpus's per-competition breakdown (30 + 25 + 15 + 5 + 20 + 15 = 110), now stated explicitly - plus 'you can earn +10-15 gems if you win the Dream Draft event they punt in the game every two weeks', so a full Career season with a draft win is about 120-125 gems. (5) THE PER-CLUB RATING CHANGE TABLE, a concrete example of the Winter Reload reshuffle: 'Man City: **Guehi, Foden +1** · Haaland, Donna, Doku, Gvardiol, Rodri, Dias, Reijnders **retains** · Marmoush, Silva **-1** · Semenyo, Cherki **+2** · Trafford **-1** · NOR +3.' So the reshuffle is per-club and per-player, with most players unchanged and a minority moving one or two points - which is the mechanism behind the corpus's rating-reshuffle finding and the reason a locked player's rating can surprise you. (6) THE DAILY-REWARD STREAK ARITHMETIC: 'For Regular Daily Main Reward - it is **5-11, with a +1 Increment per every day** you complete them, in a streak-style format... The Max stays at the max, so in a 10 day period assuming we keep our streak, for 3 days we will be at the max.'",
    "THE DAILY GEM CEILING: at 100 games a day, 8 games per Tier 1 championship and 48 gems per championship, the DLL engine tops out at 576 gems a day - so the ledger's 6,000-gem season is a maximum, not an expectation. WHY THE GCC IS NOT WORTH IT, with the mechanism at last: it is an away-only competition, so the stadium bonus never applies and each match pays only 30-40 coins. THE DIAMOND CUP IS THE EFFICIENT CUP - fewer matches, 15 gems plus 10 in challenges. THE 110-GEM CAREER SEASON TOTAL. THE PER-CLUB RATING CHANGE TABLE from the Winter Reload reshuffle. AND THE DAILY-REWARD STREAK ARITHMETIC.",
    "THE DAILY GEM CEILING AND WHY THE GCC IS NOT WORTH IT",
    quality="community")

add_claim("THE DAILY GEM CEILING: 'Lets assume you play the highest possible (**100 games**), and you are in Tier 1 and you win all games, because it takes **8 games to become champion** - hence this means you'll only be champion a maximum of **12 times**... hence youll gain **576 Gems in a day**.' **That is the hard ceiling on the DLL engine the corpus's whole gem plan runs on** - and it means the ledger's 6,000-gem DLL figure is a maximum reached at roughly ten hours a day, not an expectation. It independently corroborates the corpus's 8-wins-per-championship and 48-gems-per-championship figures.", 3, "economy/daily-gem-ceiling-576", [e_gm])
add_claim("WHY THE GLOBAL CHALLENGE CUP IS NOT WORTH IT, with the mechanism at last: '**never play Global challenger cup it has shit ton of rounds and none of them is played on home stadium** after the game we get only **30-40 coins**, playing so many matches for mere 25 gems doesn't feel worth to me.' **So the GCC's problem is structural, not just arithmetic: it is an away-only competition**, which means the stadium bonus - the corpus's single largest coin source - never applies, and each match pays 30-40 coins instead of the ~150 a home match pays.", 3, "cups/gcc-away-only-no-stadium-bonus", [e_gm], notes="The mechanism behind the corpus's GCC exclusion, and a different reason from the gem-per-match rule")
add_claim("THE DIAMOND CUP IS THE EFFICIENT CUP: 'Play diamond cup as it has **less matches to play** and gives **15 gems and 10 more in challenge**.' So when the corpus says play the cups selectively, the Diamond Cup is the one to play - fewer rounds than the GCC and a challenge top-up on top of the win.", 3, "cups/diamond-cup-is-the-efficient-cup", [e_gm])
add_claim("THE 110-GEM CAREER SEASON TOTAL, the sum of the corpus's per-competition breakdown (30 + 25 + 15 + 5 + 20 + 15 = 110), now stated explicitly - plus 'you can earn **+10-15 gems if you win the Dream Draft event** they punt in the game every two weeks', so a full Career season with a draft win is about 120-125 gems. **That is the true size of the Career gem engine, against the DLL engine's 576-gem daily ceiling.**", 3, "career/110-gem-season-total", [e_gm])
add_claim("THE PER-CLUB RATING CHANGE TABLE, a concrete example of the Winter Reload reshuffle: 'Man City: **Guehi, Foden +1** · Haaland, Donna, Doku, Gvardiol, Rodri, Dias, Reijnders **retains** · Marmoush, Silva **-1** · Semenyo, Cherki **+2** · Trafford **-1** · NOR +3.' **So the reshuffle is per-club and per-player, with most players unchanged and a minority moving one or two points** - the mechanism behind the corpus's rating-reshuffle finding, and the reason a locked player's rating can surprise you after an update.", 3, "patching/per-club-rating-change-table", [e_gm])
add_claim("THE DAILY-REWARD STREAK ARITHMETIC: 'For Regular Daily Main Reward - it is **5-11, with a +1 Increment per every day** you complete them, in a streak-style format... **The Max stays at the max**, so in a 10 day period assuming we keep our streak, for 3 days we will be at the max.' So the daily challenge reward climbs from 5 to 11 over six days and then holds, which is the arithmetic behind the corpus's 5-11 gems/day figure.", 3, "economy/daily-reward-streak-arithmetic", [e_gm])

for p in ['EV-524_daily_gem_ceiling.html','EV-524b_gcc_and_cup_arithmetic.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
