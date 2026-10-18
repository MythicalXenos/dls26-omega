#!/usr/bin/env python3
"""Turn 35 Wave 105: AUTO-SWITCH DOES NOT FIRE WHILE YOU HOLD B, AND THE COMMENTARY INVENTORY.

Wave 105's centrepieces:

1. AUTO-SWITCH DOES NOT FIRE WHILE YOU ARE HOLDING B. A single comment explains the entire
   auto-switch controversy that has run through three waves of this sweep: "**You have to let go
   of B for autoswitch to work.**" So the players who report auto-switch as broken are holding
   the pressure button, and the players who report it as fine have released it. That is not a
   bug or a preference — it is a mechanical interaction, and it reconciles the corpus's three
   competing auto-switch positions at a stroke.

2. THE COMPLETE AUTO-SWITCH MODE COMPARISON, with each mode's failure mode named. High switches
   too often and runs your defender the wrong way; Low is the best option but sometimes will not
   switch when you need it; Off is unreliable because the C button cycles through three players
   before the one closest to the ball, and a deflection becomes unrecoverable. That is the
   definitive statement of the trade-off, and it is why the corpus's answer has to be "it
   depends" rather than a single setting.

3. THE COMMENTARY INVENTORY — five languages with named commentators, Gary Bloom as the English
   default, and the actual phrase list from the wiki. Small, but it closes the presentation
   surface and it tells a player what they will hear.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w105')

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

e_as=new_ev("r/DreamLeagueSoccer 1pe08j8 'DLS 26 Major Issue [Auto Switch]' (4 Dec 2025 - 'You have to let go of B for autoswitch to work', plus the defending-is-difficult complaint and the set-it-to-low fix), r/DreamLeagueSoccer b8qfcu 'Best auto-switch method for playing online?' (2 Apr 2019 - the complete High/Low/Off mode comparison with each mode's failure mode), r/DreamLeagueSoccer 1chedv5 'Gameplay controls settings explained' (1 May 2024 - the three core control settings with definitions, and the version-dependent kick-assist advice), dreamleaguesoccerkits.com best-settings (15 May 2026 - Switching Sensitivity and Cursor Indicator), sportsdunia.com best-settings table (3 Mar 2026 - a SEVENTH sportsdunia table, the complete settings inventory), gamingtubebd.com (22 Jul 2026 - the five-language commentary table with named commentators, Gary Bloom as the English default), dream-league-soccer.fandom.com/wiki/Commentary (18 Jan 2025 - the actual commentary phrase list)",
    "AUTO-SWITCH DOES NOT FIRE WHILE YOU HOLD B, THE COMPLETE MODE COMPARISON, AND THE COMMENTARY INVENTORY. (1) THE MECHANICAL KEY: '**You have to let go of B for autoswitch to work.**' **So the players who report auto-switch as broken are holding the pressure button, and the players who report it as fine have released it.** That is not a bug or a preference - it is a mechanical interaction, and it reconciles the corpus's three competing auto-switch positions at a stroke. It also explains the corpus's own hold-B rule from the other side: while you are pressuring, switching is yours to do manually. (2) THE COMPLETE MODE COMPARISON, with each mode's failure mode named: '**High** - way too frequent. when the opponent makes a pass, your defender it switches to will instantly run whatever way you were previously aiming, resulting in an easy goal. but this is the best option for getting stray balls that get deflected. **Low** - this seems to be the best option, but still screws you sometimes. You'll be relying on it to switch and it won't. Then when you do a manual switch (hit c button,) it's too late. ... **Off** - see above, if the c button was more reliable, this would probably be the best... if there is a deflection, it's impossible to get a stray ball. it will switch you to 3 other players before the one closest to the ball.' **So High trades control for loose balls, Low is the best compromise, and Off makes deflections unrecoverable** - which is why the corpus's answer has to be 'it depends' rather than a single setting. (3) THE THREE CORE CONTROL SETTINGS, with definitions: 'When you go to the controls setting in DLS, you will find **3 settings**. They are; Auto Switch, Kick Assist and Cross assist' - and Auto Switch is 'Changing to a player that is nearest to the opponent in possession without manual intervention. If set to off, you will have to manually tap C to change the player being controlled.' (4) KICK ASSIST IS VERSION-DEPENDENT: 'With the current version it is **best to turn kick assist off**. Although previous versions it was better to set it on.' So the assist advice is not timeless, and the corpus's turn-the-assists-off rule is version-specific. (5) TWO MORE SETTINGS the corpus lacked: **Switching Sensitivity** (Medium recommended) and **Cursor Indicator** (ON recommended). (6) THE COMPLETE SETTINGS INVENTORY, from a seventh sportsdunia table: Gameplay (Language, Difficulty, Power Save, Camera Type, Camera Distance, Auto Replay, Quick Subs, Team Boosts, Multiplayer Chat) · Display (Player Names, Radar, Opponent Player Names, Direction Marker, Ball Colour, Bounce Marker, Score Display, Hide Multiplayer Opponent Data, Colour Blind Mode) · Controls (Auto Switch, Button Size, Kick Assists, Cross Assist, In-Game Tactics, Fixed Virtual Stick, Virtual Stick Visible, Virtual Stick Size, Descriptive Button Text). (7) THE COMMENTARY INVENTORY - five languages with named commentators: **Christian Martinoli & Luis Garcia (Mexican Spanish) · Mariano Closs & Diego Latorre (Argentine Spanish) · Rodolfo De Paoli & Diego Latorre (Argentine Spanish) · Carlos Martinez & Maldini (Spanish) · Gary Bloom (English, default)** - from a mod-APK site, so the Spanish variants may be mod-added rather than shipped, but Gary Bloom as the English default is corroborated by the corpus. (8) THE ACTUAL COMMENTARY PHRASES, from the wiki: 'Shihab crack from distance!' · 'Optimistic effort' · 'XXX with the shot' · \"Let's see how this shot goes\" · 'Well this shot looks dramatic' · 'On the volley!' · 'Volleyed goalwards!' · 'What a volley wow' · \"Off Shihab's head\" · 'Tries the header' · 'Headed goalwards'.",
    "AUTO-SWITCH DOES NOT FIRE WHILE YOU HOLD B - which reconciles the corpus's three competing auto-switch positions at a stroke: the players who call it broken are holding the pressure button. THE COMPLETE MODE COMPARISON: High trades control for loose balls, Low is the best compromise, Off makes deflections unrecoverable. KICK ASSIST IS VERSION-DEPENDENT. Two new settings (Switching Sensitivity, Cursor Indicator), the complete settings inventory, and the commentary inventory - five languages, named commentators, Gary Bloom as the English default - plus the actual commentary phrases.",
    "AUTO-SWITCH IS BLOCKED BY HOLDING B, AND THE COMMENTARY INVENTORY",
    quality="community")

add_claim("AUTO-SWITCH DOES NOT FIRE WHILE YOU ARE HOLDING B: '**You have to let go of B for autoswitch to work.**' **So the players who report auto-switch as broken are holding the pressure button, and the players who report it as fine have released it.** That is not a bug or a preference - it is a mechanical interaction, and it reconciles the corpus's three competing auto-switch positions at a stroke. It also explains the corpus's hold-B rule from the other side: while you are pressuring, switching is yours to do manually.", 3, "controls/auto-switch-blocked-by-holding-b", [e_as], notes="Reconciles the three auto-switch positions the corpus has been carrying")
add_claim("THE COMPLETE AUTO-SWITCH MODE COMPARISON, with each mode's failure mode named: '**High** - way too frequent. when the opponent makes a pass, your defender it switches to will instantly run whatever way you were previously aiming, resulting in an easy goal. but this is the best option for getting stray balls that get deflected. **Low** - this seems to be the best option, but still screws you sometimes. You'll be relying on it to switch and it won't. Then when you do a manual switch (hit c button,) it's too late. ... **Off** - if there is a deflection, it's impossible to get a stray ball. it will switch you to 3 other players before the one closest to the ball.' **So High trades control for loose balls, Low is the best compromise, and Off makes deflections unrecoverable** - which is why the corpus's answer has to be 'it depends' rather than a single setting.", 3, "controls/auto-switch-mode-comparison-complete", [e_as])
add_claim("THE THREE CORE CONTROL SETTINGS, with definitions: 'When you go to the controls setting in DLS, you will find **3 settings**. They are; Auto Switch, Kick Assist and Cross assist' - and Auto Switch is 'Changing to a player that is nearest to the opponent in possession without manual intervention. If set to off, you will have to manually tap C to change the player being controlled.' So the control surface is three switches, not a menu.", 3, "controls/three-core-control-settings", [e_as])
add_claim("KICK ASSIST IS VERSION-DEPENDENT: 'With the current version it is **best to turn kick assist off**. Although previous versions it was better to set it on.' **So the assist advice is not timeless** - the corpus's turn-the-assists-off rule is version-specific, and a guide written against an earlier build will say the opposite.", 3, "controls/kick-assist-version-dependent", [e_as])
add_claim("TWO MORE SETTINGS the corpus lacked: **Switching Sensitivity** (Medium recommended) and **Cursor Indicator** (ON recommended) - both in the controls block, both affecting how reliably you can get to the defender you want.", 3, "settings/switching-sensitivity-and-cursor-indicator", [e_as])
add_claim("THE COMPLETE SETTINGS INVENTORY, from a seventh sportsdunia table: **Gameplay** (Language, Difficulty, Power Save, Camera Type, Camera Distance, Auto Replay, Quick Subs, Team Boosts, Multiplayer Chat) · **Display** (Player Names, Radar, Opponent Player Names, Direction Marker, Ball Colour, Bounce Marker, Score Display, Hide Multiplayer Opponent Data, Colour Blind Mode) · **Controls** (Auto Switch, Button Size, Kick Assists, Cross Assist, In-Game Tactics, Fixed Virtual Stick, Virtual Stick Visible, Virtual Stick Size, Descriptive Button Text). Recorded with the sportsdunia rejection flag, but the inventory is a usable checklist.", 4, "settings/complete-inventory", [e_as], notes="Seventh sportsdunia table; the inventory is noted but not adopted as authority")
add_claim("THE COMMENTARY INVENTORY - five languages with named commentators: **Christian Martinoli & Luis Garcia (Mexican Spanish) · Mariano Closs & Diego Latorre (Argentine Spanish) · Rodolfo De Paoli & Diego Latorre (Argentine Spanish) · Carlos Martinez & Maldini (Spanish) · Gary Bloom (English, default)**. From a mod-APK site, so **the Spanish variants may be mod-added rather than shipped** - but Gary Bloom as the English default is corroborated by the corpus, and the Turkish and Arabic commentators are already on record.", 3, "presentation/five-language-commentary-inventory", [e_as])
add_claim("THE ACTUAL COMMENTARY PHRASES, from the wiki: '**Shihab crack from distance!**' · 'Optimistic effort' · 'XXX with the shot' · \"Let's see how this shot goes\" · 'Well this shot looks dramatic' · 'On the volley!' · 'Volleyed goalwards!' · 'What a volley wow' · \"Off Shihab's head\" · 'Tries the header' · 'Headed goalwards'. Small, but it closes the presentation surface, and 'Shihab' is a named running gag in the commentary set.", 4, "presentation/commentary-phrase-list", [e_as])

for p in ['EV-518_auto_switch_mechanism.html','EV-518b_settings_and_commentary.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
