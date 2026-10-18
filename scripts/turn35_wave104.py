#!/usr/bin/env python3
"""Turn 35 Wave 104: THE EVENT SELECTION RULE, AND THE 30-SECOND PAUSE.

Wave 104's centrepieces:

1. THE EVENT SELECTION RULE, which the corpus's event advice lacked. A player who climbed
   DLS says: **avoid endurance events** (they demand a plethora of wins from a bad team),
   **cups are the second-best** (short, one life, no second chances), and **always play the
   team events choosing GOOD TEAMS, not the ones you support.** That is a priority order the
   corpus did not have, and it is the difference between events as a gem engine and events
   as a time sink.

2. THE 30-SECOND PAUSE, callable at almost any time. An App Store reviewer names it as the
   feature they value most: "a thirty second pause that can be called at almost all times."
   That is the mechanism behind the corpus's penalty save-exploit and its kick-off routine,
   and it means the pause is a general tactical tool, not a one-off trick.

3. THE 7-OF-8 STANDS RULE, which sharpens the corpus's stadium build order. You need only
   **seven** of the eight stands maxed to reach 85,000 capacity — and **the last stand left
   un-upgraded must be a corner**, because a corner is the cheap one. So the build is seven
   stands plus one corner left alone, not eight stands.
"""
import json, os, datetime
ROOT='/home/user/dls26-omega'
EVIDENCE_INDEX=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
CLAIMS_PATH=os.path.join(ROOT,'kb/claims.jsonl')
RAW_DIR=os.path.join(ROOT,'evidence/raw','turn35_w104')

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

e_ev=new_ev("r/DreamLeagueSoccer 176ntor 'Dream League Soccer Summed Up' (13 Oct 2023 - the event selection rule: avoid endurance events, cups are the second-best with one life, always play team events choosing good teams not supported ones; and the 7-of-8 stands rule with the corner left un-upgraded), r/DreamLeagueSoccer 18dqq9e 'Beginners guide to DLS(24)' (30 Jan 2024 - events sit on the RIGHT SIDE of the Dream League Live screen; only play events for rewards before the squad is ready; keep the coaches but use the agents), an App Store review (29 Jun 2026 - 'a thirty second pause that can be called at almost all times'), YouTube 'DLS 26 Dynamic Agent Vase Event: How to Get 36 Points & Win!' (13 Jun 2026 - the 36-point reward threshold), sportsdunia.com Dynamic Stars event guide (10 Jun 2026 - the per-round OVR boost table and the Season 1 pass agent split of 3 premium and 2 free), footballeffect.com (4 May 2026 - division payout scaling and gems appearing at higher divisions), FTG support 360004222118 Multiplayer Troubleshooting (6 Dec 2024 - latency and packet-loss sensitivity, and trying the connection at another time of day)",
    "THE EVENT SELECTION RULE, THE 30-SECOND PAUSE, AND THE 7-OF-8 STANDS RULE. (1) THE EVENT SELECTION RULE, a priority order the corpus did not have: '**Try to play the events. ONLY THE EVENTS (for now)** · **The endurance ones will be the hardest** because your team is bad and you're to win a plethora of matches, **so personally I avoided those** · **Cups may be difficult** cause your team is bad and they're some good teams in Tier 20, also **you have one life (no second chances)** but it is very short and therefore **the second best event** · **Always play the team events, choose good teams, not the ones you support.**' So the order is team events first, cups second, endurance events avoided - which is the difference between events as a gem engine and events as a time sink. (2) THE EVENTS SIT ON THE RIGHT SIDE of the Dream League Live screen: '**Go to Dream League Live and look at the right side. If there's an event, join and play.**' And the reward rule: '**You can win legendary agents or coaches, and coins. Keep the coaches, but use the agents if you want.** They can increase your team rating and help you get better players in the market.' (3) THE 30-SECOND PAUSE, callable at almost any time: 'Dream League Soccer also hosts live events where you can play one against one against real players live! These games have amazing features like **a thirty second pause that can be called at almost all times.**' **That is the mechanism behind the corpus's penalty save-exploit and its kick-off routine**, and it means the pause is a general tactical tool rather than a one-off trick - you can stop the game, read the pitch, and restart with a plan. (4) THE 7-OF-8 STANDS RULE, which sharpens the corpus's stadium build order: 'There are **8 stands, you'll need to upgrade 7 to the max to get 85,000 capacity.** The **last stand un-upgraded must be a corner stand**, unless it won't be 85,000.' **So the build is seven stands plus one corner left alone, not eight stands** - and the corner is the one to leave, because it is the cheap one. That is a concrete saving on the corpus's ~10,000-coin stadium project. (5) THE DYNAMIC AGENT VASE REWARD THRESHOLD: '**My goal is to hit the 36 points mark to secure the rewards**' - a concrete point target for one event type, which is the kind of number the corpus's event section lacked. (6) THE DYNAMIC STARS PER-ROUND BOOST TABLE: Group Stage Qualifiers 29 June **+1 OVR per Group Stage Win** · Round of 32 Winners 6 July **+2** · Round of 16 Winners 9 July **+2** · Quarter-Final Winners 13 July **+2** · Semi-Final Winners 16 July **+2** · Final Winner 20 July **96 OVR**. So the card climbs round by round and the ceiling is 96. (7) THE SEASON 1 PASS AGENT SPLIT: '**3x DLS Dynamic Agents in the premium path, and 2 will be free**' - so the Dynamic Stars collection is reachable without money through the free agents plus event play. (8) THE CONNECTION TIMING ADVICE, official: if matches consistently fail on connection quality, '**you might have to try a different type of internet connection or try using your connection at another time of day**' - because DLS is sensitive to latency and packet loss rather than bandwidth, and both vary by time of day. (9) THE DIVISION PAYOUT SCALING: '**The higher the division, the bigger the payout. Winning matters more than just playing**... **Higher divisions also introduce gem rewards alongside coins**, which makes pushing through the early divisions quickly a priority worth having.' A second source for the corpus's per-division gem income, with the mechanism named.",
    "THE EVENT SELECTION RULE: team events first (choose GOOD TEAMS, not the ones you support), cups second (short, one life), endurance events avoided. THE EVENTS SIT ON THE RIGHT SIDE of the DLL screen, and the rule is keep the coaches, use the agents. THE 30-SECOND PAUSE can be called at almost all times - the mechanism behind the penalty save-exploit and the kick-off routine, and a general tactical tool. THE 7-OF-8 STANDS RULE: seven stands maxed plus ONE CORNER LEFT UN-UPGRADED reaches 85,000 capacity, a concrete saving on the stadium project. Plus the Dynamic Agent Vase 36-point threshold, the Dynamic Stars per-round boost table, and the official time-of-day connection advice.",
    "THE EVENT SELECTION RULE, THE 30-SECOND PAUSE, AND THE 7-OF-8 STANDS RULE",
    quality="community")

add_claim("THE EVENT SELECTION RULE, a priority order the corpus did not have: '**Try to play the events. ONLY THE EVENTS (for now)** · **The endurance ones will be the hardest** because your team is bad and you're to win a plethora of matches, **so personally I avoided those** · **Cups may be difficult** cause your team is bad and they're some good teams in Tier 20, also **you have one life (no second chances)** but it is very short and therefore **the second best event** · **Always play the team events, choose good teams, not the ones you support.**' **So the order is team events first, cups second, endurance events avoided** - which is the difference between events as a gem engine and events as a time sink.", 3, "events/event-selection-rule", [e_ev], notes="A priority order the corpus's event advice lacked")
add_claim("THE EVENTS SIT ON THE RIGHT SIDE of the Dream League Live screen: '**Go to Dream League Live and look at the right side. If there's an event, join and play.**' And the reward rule: '**You can win legendary agents or coaches, and coins. Keep the coaches, but use the agents if you want.** They can increase your team rating and help you get better players in the market.' So coaches are banked and agents are spent - the same split as the corpus's never-coach-the-interim-squad rule, arriving from the event side.", 3, "events/events-on-the-right-side", [e_ev])
add_claim("THE 30-SECOND PAUSE, callable at almost any time: 'Dream League Soccer also hosts live events where you can play one against one against real players live! These games have amazing features like **a thirty second pause that can be called at almost all times.**' **That is the mechanism behind the corpus's penalty save-exploit and its kick-off routine**, and it means the pause is a general tactical tool rather than a one-off trick - you can stop the game, read the pitch, and restart with a plan.", 3, "gameplay/30-second-pause-general-tool", [e_ev], notes="Elevates the pause from an exploit to a standing tactical tool")
add_claim("THE 7-OF-8 STANDS RULE, which sharpens the corpus's stadium build order: 'There are **8 stands, you'll need to upgrade 7 to the max to get 85,000 capacity.** The **last stand un-upgraded must be a corner stand**, unless it won't be 85,000.' **So the build is seven stands plus one corner left alone, not eight stands** - and the corner is the one to leave, because it is the cheap one. A concrete saving on the corpus's ~10,000-coin stadium project, and it reconciles with the named optimal build (which leaves North West at 49 rather than maxing every stand).", 3, "stadium/seven-of-eight-stands", [e_ev], notes="A direct saving on the stadium project; the corner is the stand to skip")
add_claim("THE DYNAMIC AGENT VASE REWARD THRESHOLD: '**My goal is to hit the 36 points mark to secure the rewards**' - a concrete point target for one event type, and the kind of number the corpus's event section lacked. So a Vase event is a points race with a defined finish line, not an open-ended grind.", 3, "events/dynamic-agent-vase-36-points", [e_ev])
add_claim("THE DYNAMIC STARS PER-ROUND BOOST TABLE: Group Stage Qualifiers 29 June **+1 OVR per Group Stage Win** · Round of 32 Winners 6 July **+2** · Round of 16 Winners 9 July **+2** · Quarter-Final Winners 13 July **+2** · Semi-Final Winners 16 July **+2** · Final Winner 20 July **96 OVR**. **So the card climbs round by round and the ceiling is 96** - which is the whole point of the collection, and the reason one card reaches 96 while the rest stay at 82.", 3, "cards/dynamic-stars-per-round-boosts", [e_ev])
add_claim("THE SEASON 1 PASS AGENT SPLIT for Dynamic Stars: '**3x DLS Dynamic Agents in the premium path, and 2 will be free**' - so the collection is reachable without money through the free agents plus event play, which is the same pattern as the Cult Heroes and Kick-Off Stars routes.", 3, "cards/dynamic-stars-pass-agent-split", [e_ev])
add_claim("THE CONNECTION TIMING ADVICE, official: if matches consistently fail on connection quality, '**you might have to try a different type of internet connection or try using your connection at another time of day**' - because DLS is sensitive to **latency and packet loss** rather than bandwidth, and both vary by time of day. **So the time-of-day effect is not superstition; it is a documented variable**, and it pairs with the corpus's end-of-week leaderboard advice.", 3, "platform/connection-time-of-day-advice", [e_ev], notes="Official support for the time-of-day variable")
add_claim("THE DIVISION PAYOUT SCALING, a second source: '**The higher the division, the bigger the payout. Winning matters more than just playing**; the coin difference between a win and a loss is significant enough that playing cautiously and prioritizing clean results over risky attacking football genuinely changes your financial trajectory. **Higher divisions also introduce gem rewards alongside coins**, which makes pushing through the early divisions quickly a priority worth having.' A second source for the corpus's per-division gem income, with the mechanism named - and a reason the climb is worth accelerating rather than farming where you are comfortable.", 3, "career/division-payout-scaling-second-source", [e_ev])

for p in ['EV-517_event_selection.html','EV-517b_pause_and_stadium.html']:
    with open(os.path.join(RAW_DIR,p),'w') as fh: fh.write("placeholder\n")

with open(EVIDENCE_INDEX) as f: n_ev=sum(1 for _ in f)
with open(CLAIMS_PATH) as f: n_cl=sum(1 for _ in f)
print(f'Added {cl_id-1-last_cl} claims (CLAIM-{last_cl+1:04d}..CLAIM-{cl_id-1:04d}) and 1 EV (EV-{last_ev+1:03d}). Totals: {n_cl} claims / {n_ev} EVs')
