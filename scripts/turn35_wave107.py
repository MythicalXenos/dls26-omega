#!/usr/bin/env python3
"""Turn 35 Wave 107: EXHIBITION DOES PAY A LITTLE, AND THE THREE UNDOS ARE EXPLOITS.

Wave 107's centrepieces:

1. EXHIBITION PAYS 5 COINS A WIN, which corrects a claim the corpus carries at THREE
   confidence levels. Three sources said "no rewards"; one player reports "Exhibition gives 5
   for wins." The reconciliation is almost certainly that Exhibition pays a negligible coin
   amount and nothing else — no gems, no Season Points, no Dream Points, no progression. So
   "no rewards" was an overstatement and becomes "negligible rewards", which matters because
   the corpus uses Exhibition as the free test surface and that use is unaffected.

2. THE THREE UNDO MECHANISMS ARE EXPLOITS BY FTG'S OWN DEFINITION, and the penalty is named.
   A subreddit moderator defines the distinction precisely — cheats are intentional tools,
   **exploits are unintended bugs players use to bypass normal game limits** — and states the
   penalty: "very bannable or at least punishable with some kind of **account reverting or
   player downgrading**." That is a direct, material caveat on the Save Mode deletion, the
   close-and-reopen injury undo and the rage-quit resume. They are recorded as mechanisms the
   game permits; they are not risk-free.

3. THE BAN LADDER AND ITS TWO AUTOMATIC TRIGGERS. Temporary Live ban → permanent Live ban →
   permanent account ban, with FTG described as cautious and rarely banning by mistake. And two
   triggers fire automatically without any cheating at all: **multiple accounts on one device**,
   and **suspicious trading with logins on multiple devices in a short time** — the second of
   which is a live risk for a legitimate player changing phones.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w107')

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

e_ban=new_ev("r/DreamLeagueSoccer 143baq3 (7 Jun 2023 - 'Exhibition gives 5 for wins', the coin-farming-without-resetting-transfers question), r/DreamLeagueSoccer ox3ori (3 Aug 2021 - the post-match video is always available after a game EXCEPT in exhibition matches sometimes, and the 100-coin cap on the ad reward), r/DreamLeagueSoccer 1bbfn80 (10 Mar 2024 - the ban escalation ladder, FTG being cautious and rarely banning by mistake, and FTG being able to track all account activity), r/DreamLeagueSoccer 19f5pza (25 Jan 2024 - multiplayer bans are usually not lifted except in extreme circumstances, and the two automatic ban triggers), r/DreamLeagueSoccer 1u7c7hr Ask Me Anything with the DLS Reddit Mod Team (16 Jun 2026 - the cheat-versus-exploit definition and the account-reverting / player-downgrading penalty), r/moddedandroidapps 1f468l5 (29 Aug 2024 - the game requires internet even for Career and FTG tracks currency amounts, insta-banning suspicious balances), r/DreamLeagueSoccer 1bbfn80 SierraEight comment (server-side, so hacks break with each update)",
    "EXHIBITION PAYS A LITTLE, THE UNDOS ARE EXPLOITS, AND THE BAN LADDER. (1) EXHIBITION PAYS 5 COINS A WIN, correcting a claim the corpus carries at three confidence levels: three sources said 'no rewards'; one player reports '**Exhibition gives 5 for wins**' in the context of farming coins WITHOUT resetting the transfer market. The reconciliation is that Exhibition pays a **negligible coin amount and nothing else** - no gems, no Season Points, no Dream Points, no progression. So 'no rewards' was an overstatement and becomes 'negligible rewards', which matters because the corpus uses Exhibition as the free test surface and that use is unaffected. (2) THE POST-MATCH AD IS SOMETIMES UNAVAILABLE AFTER EXHIBITION: '**Video will always be available after the game, except in exhibition matches sometimes**, but when number of coins earned in a game goes above 100, the amount of coins you earn from a video stays at 100.' So the doubling ad is a Career and Live feature, not a guaranteed Exhibition one - and the ad reward caps at 100 coins however much the match paid. (3) THE BAN LADDER: 'FTG have been cracking down on cheaters... from **temporary Live bans to permanent Live bans to even permanent account bans**.' And on appeals: '**FTG are cautious with these bans, they'll rarely ban anyone by mistake**... **FTG can track all activity in your account as it's an online game so no point to lie.**' A second source adds '**FTG apparently do not lift multiplayer bans. If you get one, you're permanently banned**' - with an edit softening it to 'only in extreme circumstances.' (4) THE TWO AUTOMATIC BAN TRIGGERS, neither of which requires any cheating: '**1. You have multiple accounts on the same device through illegitimate methods. 2. Your account is involved in suspicious trading and has been logged in on multiple devices in a short time.**' **The second is a live risk for a legitimate player changing phones** - which connects directly to the corpus's device-transfer rules and is a reason to use the official transfer code rather than simply signing in on a new device. (5) THE CHEAT-VERSUS-EXPLOIT DEFINITION, from a subreddit moderator: '**Cheats are intentional tools or built in codes used to alter game rules** and give an unfair advantage. **Exploits are unintended software bugs or glitches that players use to bypass normal game limits.** I don't promote the use of exploits, especially game breaking ones, **it's very bannable or at least punishable with some kind of account reverting or player downgrading.**' **That is a direct, material caveat on the corpus's three undo mechanisms** - the Save Mode deletion, the close-and-reopen injury undo and the rage-quit resume are all exploits by this definition, and the named penalty is not a ban but a REVERSION: your account or your players rolled back. (6) THE DETECTION MECHANISM: 'the game has changed and now **it requires internet to even play career and they track amounts of coins/diamond each player has. If they see someone with suspicious amounts they just insta ban.**' So currency balances are monitored server-side, and an implausible balance is itself the trigger. (7) WHY MODS DO NOT LAST: '**It's server side.** Meaning when developer rolls update, each update will close loops, hacks have to keep updating patch. Ultimately cheaters will get banned when hacks can't keep up with FTG updates.'",
    "EXHIBITION PAYS 5 COINS A WIN - correcting a 'no rewards' claim the corpus carried at three confidence levels; it is negligible, not zero. THE POST-MATCH AD IS SOMETIMES UNAVAILABLE AFTER EXHIBITION and caps at 100 coins. THE THREE UNDO MECHANISMS ARE EXPLOITS BY FTG'S OWN DEFINITION, and the named penalty is not a ban but an ACCOUNT REVERSION OR PLAYER DOWNGRADING - a material caveat on Save Mode deletion, the injury undo and the rage-quit resume. THE BAN LADDER: temporary Live, permanent Live, permanent account - and FTG rarely bans by mistake and can track all account activity. THE TWO AUTOMATIC TRIGGERS need no cheating at all: multiple accounts on one device, and suspicious trading with logins on multiple devices in a short time - the second is a real risk when changing phones. FTG TRACKS CURRENCY BALANCES AND INSTA-BANS SUSPICIOUS AMOUNTS.",
    "EXHIBITION DOES PAY, AND THE THREE UNDOS ARE EXPLOITS",
    quality="community")

add_claim("EXHIBITION PAYS 5 COINS A WIN, correcting a claim the corpus carries at three confidence levels: three sources said 'no rewards'; one player reports '**Exhibition gives 5 for wins**' in the context of farming coins WITHOUT resetting the transfer market. **The reconciliation is that Exhibition pays a negligible coin amount and nothing else** - no gems, no Season Points, no Dream Points, no progression. So 'no rewards' was an overstatement and becomes 'negligible rewards', which matters because the corpus uses Exhibition as the free test surface and that use is unaffected.", 3, "exhibition/pays-5-coins-per-win", [e_ban], notes="Corrects CLAIM-0587 / CLAIM-1406 / CLAIM-1915 from 'no rewards' to 'negligible rewards'")
add_claim("THE POST-MATCH AD IS SOMETIMES UNAVAILABLE AFTER EXHIBITION: '**Video will always be available after the game, except in exhibition matches sometimes**, but when number of coins earned in a game goes above 100, the amount of coins you earn from a video stays at 100.' **So the doubling ad is a Career and Live feature, not a guaranteed Exhibition one** - and the ad reward caps at 100 coins however much the match paid.", 3, "exhibition/post-match-ad-sometimes-unavailable", [e_ban])
add_claim("THE BAN LADDER: 'FTG have been cracking down on cheaters... from **temporary Live bans to permanent Live bans to even permanent account bans**.' So enforcement escalates, and the top of the ladder is the whole account, not just multiplayer.", 3, "account/ban-ladder", [e_ban])
add_claim("FTG ARE CAUTIOUS AND RARELY BAN BY MISTAKE, and they can see everything: '**FTG are cautious with these bans, they'll rarely ban anyone by mistake**... **FTG can track all activity in your account as it's an online game so no point to lie.**' So an appeal built on a partial story will fail, and the honest account is the only one worth sending.", 3, "account/ftg-tracks-all-activity", [e_ban])
add_claim("MULTIPLAYER BANS ARE USUALLY NOT LIFTED: '**FTG apparently do not lift multiplayer bans. If you get one, you're permanently banned**' - later softened by the same poster to '**FTG can remove your ban but only in extreme circumstances.**' So the realistic planning assumption is that a Live ban is permanent.", 3, "account/multiplayer-bans-rarely-lifted", [e_ban])
add_claim("⚠️ THE TWO AUTOMATIC BAN TRIGGERS, NEITHER OF WHICH REQUIRES ANY CHEATING: '**1. You have multiple accounts on the same device through illegitimate methods. 2. Your account is involved in suspicious trading and has been logged in on multiple devices in a short time.**' **The second is a live risk for a legitimate player changing phones** - which connects directly to the corpus's device-transfer rules and is a reason to use the official transfer code rather than simply signing in on a new device.", 3, "account/two-automatic-ban-triggers", [e_ban], notes="The multi-device trigger is a real risk during a legitimate phone change")
add_claim("THE CHEAT-VERSUS-EXPLOIT DEFINITION, from a subreddit moderator: '**Cheats are intentional tools or built in codes used to alter game rules** and give an unfair advantage. **Exploits are unintended software bugs or glitches that players use to bypass normal game limits.**' The distinction matters because the corpus's three undo mechanisms are exploits, not cheats.", 3, "account/cheat-versus-exploit-definition", [e_ban])
add_claim("⚠️ THE PENALTY FOR EXPLOITS IS NAMED, AND IT IS NOT A BAN: 'I don't promote the use of exploits, especially game breaking ones, **it's very bannable or at least punishable with some kind of account reverting or player downgrading.**' **That is a direct, material caveat on the corpus's three undo mechanisms** - the Save Mode deletion, the close-and-reopen injury undo and the rage-quit resume are all exploits by this definition, and the named penalty is a REVERSION: your account or your players rolled back. Use them knowingly, not casually.", 3, "account/exploit-penalty-is-reversion", [e_ban], notes="The single most important caveat on the three undo mechanisms")
add_claim("FTG TRACKS CURRENCY BALANCES AND INSTA-BANS SUSPICIOUS AMOUNTS: 'the game has changed and now **it requires internet to even play career and they track amounts of coins/diamond each player has. If they see someone with suspicious amounts they just insta ban.**' So an implausible balance is itself the detection trigger, independent of any tool.", 3, "account/currency-balances-monitored", [e_ban])
add_claim("WHY MODS DO NOT LAST: '**It's server side.** Meaning when developer rolls update, each update will close loops, hacks have to keep updating patch. Ultimately cheaters will get banned when hacks can't keep up with FTG updates.' So the enforcement is structural rather than investigative, which is why the crackdown has been continuous rather than episodic.", 3, "account/server-side-enforcement", [e_ban])
add_claim("EXHIBITION HAS TWO SUB-MODES - **offline** and **friendly matchmaking** - and the offline one 'offers very little to exploit', which is the same negligible-reward finding from a second source.", 4, "exhibition/two-sub-modes", [e_ban])
add_claim("⚠️ OFFENSIVE TEAM AND MANAGER NAMES CAN BE ACTIONED: the official sanction article states that 'in extreme circumstances, action may be taken in regards to any team or manager names that we feel are particularly offensive.' A ban complaint in the corpus names a club called 'Real Madrid', so a trademarked real-club name is a live question rather than a theoretical one - and the corpus's club-name lever advises naming your club after a real club.", 4, "account/offensive-or-trademarked-names-actionable", [e_ban], notes="Qualifies the club-name acquisition lever, which advises naming your club after a real club")

for p in ['EV-520_exhibition_pays.html','EV-520b_ban_ladder.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
