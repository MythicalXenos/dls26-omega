#!/usr/bin/env python3
"""Turn 26: inspect remaining promising github repos (LeoH321 Chinese tools, girtab.github.io, FootballGamingBD siblings, com.firsttouchgames backup/launcher hits, Bistu crawler)."""
import json,os,time,urllib.request,urllib.parse,urllib.error,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST=os.path.join(ROOT,'logs','research','deep_fetch_turn26'); os.makedirs(DEST,exist_ok=True)
H={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3+json'}
def api(path,retries=2,raw=False):
    hh=dict(H)
    if raw: hh['Accept']='application/vnd.github.v3.raw'
    for i in range(retries):
        req=urllib.request.Request('https://api.github.com'+path,headers=hh)
        try:
            with urllib.request.urlopen(req,timeout=45) as r:
                return r.read() if raw else json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            if e.code in (403,429):
                reset=e.headers.get('X-RateLimit-Reset'); wait=max(3,min(65,float(reset)-time.time()+2)) if reset else 30
                print(' rate',e.code,'wait',int(wait)); time.sleep(wait); continue
            print(' HTTP',e.code,path[:80]); return None
        except Exception as e: print(' err',e); time.sleep(4)
    return None
def pull_raw(repo,path,save_to=None,max_bytes=5_000_000):
    data=api(f'/repos/{repo}/contents/{urllib.parse.quote(path)}',raw=True)
    if data is None: return None
    if max_bytes: data=data[:max_bytes]
    if save_to:
        os.makedirs(os.path.dirname(save_to),exist_ok=True)
        open(save_to,'wb').write(data)
    return data
def tree(repo):
    d=api(f'/repos/{repo}/git/trees/HEAD?recursive=1')
    return [x for x in d['tree']] if d and 'tree' in d else None
def safe(name): return name.replace('/','__')

# 1. LeoH321 DLSsuperleague index.html (already pulled) and quiz/reaction
targets=[
    ('LeoH321/DLSsuperleague','index.html'),
    ('LeoH321/DLS26-quiz','index.html'),
    ('LeoH321/dls26-reaction-test','index.html'),
    ('LeoH321/DLS26-quiz','style.css'),
    ('LeoH321/dls26-reaction-test','style.css'),
]
for repo,path in targets:
    out=os.path.join(DEST,safe(repo)+'__'+path.replace('/','__'))
    if os.path.exists(out) and os.path.getsize(out)>100: continue
    d=pull_raw(repo,path,out)
    print(f'{repo}/{path}: {len(d) if d else "FAIL"} bytes')
    time.sleep(1)

# 2. girtab/girtab.github.io tree (702 hits - inspect DLS/dream-league files only)
print('\n=== girtab/girtab.github.io tree scan ===')
gtree=tree('girtab/girtab.github.io')
if gtree:
    files=[x for x in gtree if x.get('type')=='blob']
    print(f' total {len(files)} files')
    dls_files=[f for f in files if re.search(r'(dls|dream.league|梦幻足球)',f['path'],re.I)]
    print(f' DLS-related: {len(dls_files)}')
    for f in dls_files[:30]: print(f'   {f.get("size",0):>8} {f["path"]}')
    # Pull up to 20 interesting small DLS files
    small=[f for f in dls_files if f.get('size',0)<200_000][:20]
    for f in small:
        out=os.path.join(DEST,'girtab__'+f['path'].replace('/','__'))
        try:
            d=pull_raw('girtab/girtab.github.io',f['path'],out)
            print(f'  pulled {f["path"][:80]} {len(d) if d else "FAIL"}b'); time.sleep(1)
        except Exception as e: print('fail',f['path'],e)
else:
    print(' tree fetch failed')

# 3. FootballGamingBD sibling repos - index/README + key data files
fg_siblings=['FootballGamingBD/Dls','FootballGamingBD/dls-player-db','FootballGamingBD/DLS26_PlayerData','FootballGamingBD/Player-Database','FootballGamingBD/players','FootballGamingBD/PlayerDls','FootballGamingBD/Mahi','FootballGamingBD/Main','FootballGamingBD/Main_repo']
print('\n=== FBGD siblings ===')
for repo in fg_siblings:
    t=tree(repo)
    if not t: print(f'  {repo}: TREE FAIL'); continue
    files=[x for x in t if x.get('type')=='blob']
    data=[f for f in files if f['path'].lower().endswith(('.json','.html','.md','.js','.txt','.csv'))]
    print(f'  {repo}: {len(files)} files, data-like {len(data)}')
    for f in data[:8]: print(f'    {f.get("size",0):>8} {f["path"]}')
    for cand in ['README.md','index.html','Data/Player.json','players.json','player.json']:
        m=[f for f in files if f['path'].lower()==cand.lower()]
        if m:
            f=m[0]; out=os.path.join(DEST,safe(repo)+'__'+f['path'].replace('/','__'))
            if not os.path.exists(out):
                d=pull_raw(repo,f['path'],out,max_bytes=500_000)
                print(f'    pulled {f["path"]} {len(d) if d else "FAIL"}b')
                time.sleep(1)
    time.sleep(1)

# 4. com.firsttouchgames.dls7 launcher/backup references - sample top repos from turn23b sweep
print('\n=== com.firsttouchgames.dls7 launcher/backup samples ===')
# Just look up a few known launcher/backup apps that reference the package
samples=[
    'beerphilipp/taptrap',  # already have
]
# Run a small precise search for "shared_prefs" or "com.firsttouchgames.dls7" in Java/Kotlin
def code_search(q,pages=2):
    all_items=[]
    for p in range(1,pages+1):
        d=api(f'/search/code?q={urllib.parse.quote(q)}&per_page=100&page={p}')
        if not d or d.get('total_count',-1)<0: break
        all_items+=d.get('items',[])
        if len(d.get('items',[]))<100: break
        time.sleep(3)
    return all_items
qs=[
    '"com.firsttouchgames.dls7" shared_prefs',
    '"com.firsttouchgames.dls7" save',
    '"com.firsttouchgames.dls7" file',
    'dream league soccer save data',
]
seen_repos=set(); hit_files=[]
for q in qs:
    items=code_search(q,pages=2)
    print(f'  Q="{q[:50]}" got={len(items)}')
    for it in items[:20]:
        repo=it.get('repository',{}).get('full_name','')
        if repo not in seen_repos:
            seen_repos.add(repo); hit_files.append((repo,it['path']))
    time.sleep(2)
print(f'  unique repos referencing save/shared_prefs/file: {len(seen_repos)}')
for r,p in hit_files[:20]: print(f'    {r} {p}')
# Pull README/one code file from up to 6
import os.path
for repo,path in hit_files[:6]:
    safe_r=safe(repo); out=os.path.join(DEST,'launcher__'+safe_r+'__'+path.replace('/','__'))
    if os.path.exists(out) and os.path.getsize(out)>50: continue
    d=pull_raw(repo,path,out,max_bytes=50_000)
    print(f'    pulled {repo}/{path} {len(d) if d else "FAIL"}b')
    time.sleep(1)

print('\nDone')
