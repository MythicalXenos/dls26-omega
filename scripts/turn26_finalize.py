#!/usr/bin/env python3
"""Turn 26 finalize: EV-254, CLAIM-150..153, sample 16."""
import json,os,re,random
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl'); NL='\n'
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]; by={c['claim_id']:c for c in claims}
ev=[json.loads(l) for l in open(EIP) if l.strip()]
ev.append({'evidence_id':'EV-254','artifact':'evidence/extract/EV-254_thienntdev_botdls_automation_repo.md','tool':'github-api (allowlisted)','origin_method':'thienntdev/bot-dls (Vietnamese DLS CV/ML auto-farming bot for BlueStacks/Nox/LDPlayer/GameLoop) — pulled README, USAGE, settings, ad_handler, game_controller, decision_maker, special_situations, game_state_detector, computer_vision, sample log, 23 source files total',
           'retrieved_at_utc':'2026-10-18T01:10:00Z','authenticity_limits':'Third-party bot; detects only what is visible in screenshots at 1920x1080; does not read game memory. Farming-target numbers (15k gold / 400 gems) are the author defaults, not game caps. Vietnamese-language comments; menu/button names are the bot\'s labels (A=pass/B=shoot/C=skill corroborated by widely-published DLS control guides and EV-085 UI description).','covers':['CLAIM-150','CLAIM-151','CLAIM-152','CLAIM-153','CLAIM-026','CLAIM-115','CLAIM-012','CLAIM-017']})

# refine CLAIM-026 to mention A/B/C naming
by['CLAIM-026']['proposition']='Controls layout (default): left virtual joystick (360° movement); right side has three virtual buttons A, B, C plus separate sprint/tackle/switch controls. Button mapping: A = pass, B = shoot, C = skill moves (thienntdev/bot-dls corroborates). Sprint is a hold modifier; tackle/switch are defensive buttons. Auto-switch can be toggled in Settings (default on).'
by['CLAIM-026']['supporting_evidence'].append('EV-254')

new=[
('CLAIM-150',
 'On-screen action button mapping in match controls: A = pass (ground pass / through ball context-dependent), B = shoot (finish / long shot / clearance), C = skill moves (flicks/feints). Three additional virtual actions: sprint (hold-to-run modifier), tackle (standing/sliding when defending), switch (change controlled player). Movement is a 360° virtual left joystick; the game supports ADB/touch input at 1920×1080 (BlueStacks/Nox/LDPlayer/GameLoop default).',
 'Community Consensus','Low',['EV-254','CLAIM-026'],'2026-11-18',
 ['Mapping derived from a third-party auto-bot; consistent with widely-published DLS control guides. Step 2 APK should verify exact button region coordinates; in-game tutorial text is gold-standard but not yet scraped'],['CLAIM-026']),
('CLAIM-151',
 'DLS26 in-match state machine (exhaustive enumeration visible to a CV bot): top-level UI = MAIN_MENU / CAREER_MODE / LIVE_MODE / MATCH_LOADING / MATCH_PLAYING / MATCH_PAUSED / MATCH_END. Match contexts = ATTACKING / DEFENDING / COUNTER_ATTACK. Set pieces = KICKOFF / FREE_KICK (direct) / INDIRECT_FREE_KICK / CORNER_KICK / THROW_IN / GOAL_KICK / PENALTY_KICK. Events = GOAL_SCORED / GOAL_CONCEDED. Bot does not report any additional states beyond these, suggesting this is the full externally-visible automata.',
 'Community Consensus','Low',['EV-254','CLAIM-012','CLAIM-017'],'2026-11-18',
 ['Set of states reflects what a CV bot can detect; dialogs/events the bot ignores (e.g. post-match rewards, transfer market, pack openings) are not captured here'],['CLAIM-012']),
('CLAIM-152',
 'Ad inventory confirmed by bot: (1) rewarded ads (center-screen, no skip, reward is coins OR diamonds/gems), (2) interstitial ads (full-screen, no skip, no reward), (3) skippable interstitials (skip button top-right ~1750,100 at 1920×1080, appears after ~5s wait, no reward). Corroborates the four-ad-SDK set found in CLAIM-136 and the multi-network policy CLAIM-115. Rewarded ads grant either coins OR gems (not one exclusively).',
 'Community Consensus','Low',['EV-254','CLAIM-115','CLAIM-136'],'2026-11-18',
 ['Rewards observed indirectly via farming-statistics increments; bot does not read reward amount directly'],['CLAIM-115','CLAIM-136']),
('CLAIM-153',
 'DLS26 exposes a player-controllable HUD with two stamina/boost indicator icons ("filled" and "hollow" circle templates used by the bot for HUD detection), a score region in the top-middle area, and two goal-post regions detectable via white HSV mask. Jersey colours are read from the kick-off circle area (~0.45–0.55, 0.48–0.55 relative coords) to auto-classify own vs opponent players.',
 'Community Consensus','Medium',['EV-254'],'2026-11-18',
 ['HUD icon semantics (filled/hollow) inferred from template names; the bot does not label them explicitly as stamina/boost. Could correspond to sprint stamina, form, or a boost meter — Step 2 required for precise semantics'],['CLAIM-052','CLAIM-151']),
]
for cid,prop,tier,vol,evl,due,chall,cross in new:
    claims.append({'claim_id':cid,'proposition':prop,'context_build':'thienntdev/bot-dls source code (23 Python files, CV+ML automation bot)','confidence_tier':tier,'volatility_tier':vol,'supporting_evidence':evl,
                   'contradicting_evidence':[],'last_valid_check':'2026-10-18T01:10:00Z','last_attempt':'2026-10-18T01:10:00Z','last_checked_by':'turn-26 bot-dls source analysis',
                   'next_due':due,'origin_history':[{'at':'2026-10-18','origins':['community-tool']}],'challenges':chall,'replacements':None,'cross_refs':cross or [],'context_evidence':[]})
# add EV refs
for cid,toks in {'CLAIM-012':['EV-254'],'CLAIM-017':['EV-254'],'CLAIM-115':['EV-254']}.items():
    for t in toks:
        if t not in by[cid]['supporting_evidence']: by[cid]['supporting_evidence'].append(t)
claims.sort(key=lambda c:int(c['claim_id'].split('-')[1]))
with open(CP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(c,sort_keys=True) for c in claims)+NL)
for e in ev:
    cov=set(e.get('covers',[]))
    if e['evidence_id']=='EV-254': cov|={'CLAIM-150','CLAIM-151','CLAIM-152','CLAIM-153','CLAIM-026','CLAIM-115','CLAIM-012','CLAIM-017'}
    e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
ev.sort(key=lambda e:int(e['evidence_id'].split('-')[1]))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev)+NL)
# sample 16
random.seed(26)
ev_idx={e['evidence_id']:e for e in ev}
strata={'Confirmed':2,'High Confidence':2,'Community Consensus':2,'Speculative':1}; picked=[]
for tier,n in strata.items():
    pool=[c for c in claims if c['confidence_tier']==tier]; random.shuffle(pool); picked.extend(pool[:n])
ok=warn=bad=0; repairs={}
for c in picked:
    cid=c['claim_id']; t=c['confidence_tier']; notes=[]; status='OK'
    ev_tok=[]
    for s in c['supporting_evidence']: ev_tok+=re.findall(r'(?:EV|EVD)-(\d{3,4})',s)
    if not ev_tok and not any('cross-ref' in ch.lower() or 'synthesis' in ch.lower() for ch in c.get('challenges',[])): notes.append('no EV'); status='BAD'
    seen=set()
    for tok in ev_tok:
        full=('EVD-'+tok if any('EVD-'+tok in s for s in c['supporting_evidence']) else 'EV-'+tok)
        if full in seen: continue; seen.add(full)
        if full in ev_idx:
            if cid not in ev_idx[full].get('covers',[]): notes.append(f'{full} covers[] miss'); status='WARN'; repairs.setdefault(full,set()).add(cid)
        else: notes.append(f'not in index: {full}'); status='BAD'
    tag='OK' if status=='OK' else ('WARN' if status=='WARN' else 'BAD')
    print(f'  {cid} [{t}] {tag}: {c["proposition"][:80]}...')
    for n in notes: print('     -',n)
    if status=='OK': ok+=1
    elif status=='WARN': warn+=1
    else: bad+=1
print(f'SAMPLE 16: OK={ok} WARN={warn} BAD={bad}')
ev2=[json.loads(l) for l in open(EIP) if l.strip()]
for e in ev2:
    if e['evidence_id'] in repairs:
        cov=set(e.get('covers',[])); cov|=repairs[e['evidence_id']]
        e['covers']=sorted(cov,key=lambda s:(0,int(s.split('-')[1])) if s.startswith('CLAIM-') else (1,s))
with open(EIP,'w',encoding='utf-8',newline=NL) as fh:
    fh.write(NL.join(json.dumps(e,sort_keys=True) for e in ev2)+NL)
b=open(CP,'rb').read()
ids={c['claim_id'] for c in claims}; evids={e['evidence_id'] for e in ev2}
badcov=[(e['evidence_id'],c) for e in ev2 for c in e.get('covers',[]) if c.startswith('CLAIM-') and c not in ids]
miss=[(c['claim_id'],t) for c in claims for s in c.get('supporting_evidence',[]) for t in re.findall(r'(?:EV|EVD)-\d{3,4}',s) if t not in evids]
print('claims',len(claims),'LF',b.count(b'\n'),'ev',len(ev2),'badcovers',badcov,'miss',miss)
