#!/usr/bin/env python3
"""Epistemic Crucible Audit: Part 1 — integrity + raw-data spot-checks against JSON/CSV captures."""
import json,os,re,statistics,collections,math
ROOT='/home/user/dls26-omega'
CP=os.path.join(ROOT,'kb','claims.jsonl')
EIP=os.path.join(ROOT,'docs/continuity/a7e23a6b/evidence/index.jsonl')
claims=[json.loads(l) for l in open(CP) if l.strip()]
ev=[json.loads(l) for l in open(EIP) if l.strip()]
by={c['claim_id']:c for c in claims}
eby={e['evidence_id']:e for e in ev}
report=[]
def log(msg): report.append(msg); print(msg)

log(f'=== CRUCIBLE AUDIT START ===')
log(f'claims={len(claims)}  evidence={len(ev)}')

# 1. Integrity: covers bidirectional
ids={c['claim_id'] for c in claims}
evids={e['evidence_id'] for e in ev}
badcov=[]; missed=[]
for e in ev:
    for c in e.get('covers',[]):
        if c.startswith('CLAIM-') and c not in ids: badcov.append((e['evidence_id'],c))
for c in claims:
    for s in c.get('supporting_evidence',[]):
        for tok in re.findall(r'(?:EV|EVD)-(\d{3,4})',s):
            full=('EVD-'+tok if 'EVD-'+tok in s else 'EV-'+tok)
            if full not in evids: missed.append((c['claim_id'],full))
log(f'\n[INTEGRITY] dangling covers: {len(badcov)}; missing EV refs: {len(missed)}')
for x in badcov[:5]: log('  '+str(x))
for x in missed[:5]: log('  '+str(x))

# 2. Load data files and run numerical spot-checks
def load_json(path):
    try: return json.load(open(os.path.join(ROOT,path)))
    except FileNotFoundError:
        # try deep_fetch
        for sub in ['logs/research/trungtahust','logs/research/deep_fetch_turn24/Larrycr7aaaa__DLS26-API','logs/research/larrycr7aaaa_ftgapi','logs/research/footballgamingbd']:
            p=os.path.join(ROOT,sub,os.path.basename(path))
            if os.path.exists(p):
                return json.load(open(p))
        return None
import glob
def lpath(name):
    # search recursively
    for pat in [f'logs/**/{name}',f'logs/**/{name.replace("__","/")}']:
        for p in glob.glob(os.path.join(ROOT,pat),recursive=True): return p
    return None

# 2a. EV-251 20261 roster assertions
s2026=load_json('resources__data__20261.json') or load_json('logs/research/trungtahust/resources__data__20261.json')
if not s2026:
    p=lpath('resources__data__20261.json'); s2026=json.load(open(p)) if p else None
if s2026:
    rates=[p['rate'] for p in s2026]
    non=[p for p in s2026 if p['pos']!='GK']
    gks=[p for p in s2026 if p['pos']=='GK']
    log(f'\n[SPOT-CHECK 20261] n={len(s2026)} rate range {min(rates)}-{max(rates)} non-GK={len(non)} GK={len(gks)}')
    # CLAIM-141 says base cap 86
    c141=by.get('CLAIM-141')
    log(f'CLAIM-141 says OVR 52-86; actual {min(rates)}-{max(rates)} -> {"OK" if min(rates)==52 and max(rates)==86 else "FAIL"}')
    # 8-attr check
    bad_attr=[p for p in s2026 if not all(k in p for k in ['spe','acc','sta','str','con','pas','sho','tac'])]
    log(f'8-attr schema violations: {len(bad_attr)}')
    # Top 86 players
    tops=[p for p in s2026 if p['rate']==86]
    top_names=sorted({p['fname']+' '+p['lname'] for p in tops})
    log(f'OVR 86 players ({len(tops)}): {top_names}')
    # Price of 86s
    top_prices={p['prc'] for p in tops}
    log(f'86-player prices: {top_prices} (CLAIM-139 says tier-4=2800)')
    # Haaland/Kane/Mbappe/Dembele presence
    expected={'Erling Haaland','Harry Kane','Kylian Mbappe','Ousmane Dembele'}
    got={p['fname']+' '+p['lname'] for p in tops}
    log(f'Missing expected 86-cap names: {expected-got}')

# 2b. EV-253 multi-season stability
master=None
p=lpath('resources__data__data.json')
if p: master=json.load(open(p))
if master:
    # one bad cell Maehle STA '…'
    attrs=['spe','acc','sta','str','con','pas','sho','tac']
    clean=[p for p in master if all(isinstance(p.get(a),(int,float)) for a in attrs)]
    non=[p for p in clean if p['pos']!='GK']
    # Refit OLS via gradient descent with ridge penalty (numerically stable)
    def ols_gd(X,y,lr=5e-7,epochs=20000,ridge=1e-4):
        k=len(X[0])+1; w=[0.0]*k
        n=len(X)
        for ep in range(epochs):
            grad=[0.0]*k
            for i,row in enumerate(X):
                pred=w[0]+sum(w[j+1]*row[j] for j in range(len(row)))
                err=pred-y[i]
                grad[0]+=err
                for j in range(len(row)): grad[j+1]+=err*row[j]
            for j in range(k):
                w[j]-=lr*(2*grad[j]/n + ridge*w[j])
        return w
    X=[[p[a] for a in attrs] for p in non]; y=[p['rate'] for p in non]
    w=ols_gd(X,y)
    names=['const']+attrs
    c145=by['CLAIM-145']
    log(f'\n[DEVIL ADVOCATE OLS refit] n={len(non)}')
    # CLAIM-145 states const≈1.89, CON=0.211, STR=0.166, ACC=0.148, SPE=0.142, PAS=0.112, SHO=0.111, TAC=0.107, STA=0.037
    claim_w={'const':1.89,'spe':0.142,'acc':0.148,'sta':0.037,'str':0.166,'con':0.211,'pas':0.112,'sho':0.111,'tac':0.107}
    maxdiff=0
    for n,c in zip(names,w):
        cv=claim_w[n]
        d=abs(c-cv)
        if d>maxdiff: maxdiff=d
        log(f'  {n:6s}: refit={c:+.4f}  claim={cv:+.4f}  diff={d:+.4f}')
    # MAE from CLAIM-145 weights
    pred=[claim_w['const']+sum(claim_w[a]*p[a] for a in attrs) for p in non]
    mae=statistics.mean(abs(pr-p['rate']) for pr,p in zip(pred,non))
    rmse=math.sqrt(statistics.mean((pr-p['rate'])**2 for pr,p in zip(pred,non)))
    log(f'  CLAIM-145 weights MAE={mae:.3f} RMSE={rmse:.3f} (claimed 0.38 / 0.49)')
    within=sum(1 for pr,p in zip(pred,non) if abs(round(pr)-p['rate'])<=1)
    log(f'  within ±1 after round: {within}/{len(pred)} = {100*within/len(pred):.2f}% (claimed 99.8%)')
    log(f'  max coefficient drift vs CLAIM-145: {maxdiff:.4f}  -> {"OK" if maxdiff<0.02 else "DRIFT (claim weights slightly off)"}')

# 2c. EV-252 Larrycr7 cards
lar=None
p=lpath('dls26-cards.json')
if p:
    try: lar=json.load(open(p))
    except Exception: 
        for cp in glob.glob(os.path.join(ROOT,'logs/research/deep_fetch_turn24/Larrycr7aaaa__*/*.json')):
            try:
                d=json.load(open(cp))
                if isinstance(d,list) and d and isinstance(d[0],dict) and 'stats' in d[0]: lar=d; break
            except Exception: pass
if lar:
    rates=[c['rating'] for c in lar]
    log(f'\n[SPOT-CHECK Larry promo] n={len(lar)} rate range {min(rates)}-{max(rates)}')
    # CLAIM-144 says max 98 (Champions Messi/Ronaldo)
    n98=[c for c in lar if c['rating']==98]
    log(f'98-OVR cards: {[(c["name"],c["pos"],c["type"]) for c in n98]}')
    # GK column remap check
    gks=[c for c in lar if c.get('pos')=='GK']
    gk_keys=set()
    for g in gks: gk_keys|=set(g['stats'].keys())
    log(f'GK stat keys: {gk_keys} (CLAIM-138 says GKR/GKH)')
    # schema consistency
    outfields=[c for c in lar if c.get('pos')!='GK']
    ofk=set()
    for c in outfields: ofk|=set(c['stats'].keys())
    log(f'outfield stat keys: {ofk}')

# 2d. EV-255 CB trainer constants
p=lpath('LeoH321__CB__index.html')
if p:
    t=open(p,encoding='utf-8',errors='ignore').read()
    # extract weights
    w_weights=dict(re.findall(r"id:\s*'(\w+)',\s*name:\s*'[^']+',\s*weight:\s*(\d)",t))
    log(f'\n[SPOT-CHECK CB trainer] weights from JS: {w_weights}')
    # confirm +1/+2/+3 action ids
    action_ids=re.findall(r"for \(let action of \[(\d),\s*(\d),\s*(\d)\]\)",t)
    log(f'actions (boost levels): {action_ids[0] if action_ids else None}')
    # cap 100 check
    cap_refs=len(re.findall(r'Math\.min\(100',t))
    log(f'Math.min(100,…) cap references: {cap_refs}')
    # thresholds
    th=re.findall(r'remain\s*>=\s*(\d+)',t)
    log(f'capacity thresholds in JS: {sorted(set(th))}')

# 2e. EV-254 bot-dls button/state mapping
p_bd=os.path.join(ROOT,'logs/research/thienntdev_botdls')
if os.path.isdir(p_bd):
    gc=open(os.path.join(p_bd,'game_logic__game_controller.py'),errors='ignore').read()
    btns=re.findall(r'(\w+)\s*=\s*"(pass|shoot|sprint|tackle|switch|skill)"',gc)
    log(f'\n[SPOT-CHECK bot-dls buttons] {btns}')
    gsd=open(os.path.join(p_bd,'game_logic__game_state_detector.py'),errors='ignore').read()
    states=re.findall(r'^\s+(\w+)\s*=\s*"([^"]+)"',gsd,re.M)
    state_names=[v for _,v in states]
    log(f'states ({len(state_names)}): {state_names}')

# Persist intermediate
with open(os.path.join(ROOT,'logs','audit_spotcheck_report.txt'),'w') as f: f.write('\n'.join(report))
print('wrote logs/audit_spotcheck_report.txt')
