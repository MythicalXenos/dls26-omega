#!/usr/bin/env python3
"""Turn 27 final wave - Chinese community repos, discord/reddit archival, web_search if available, LeoH321/dls26-tool-CB re-examine, remaining FBGD tree."""
import json,os,time,urllib.request,urllib.parse,urllib.error
ROOT='/home/user/dls26-omega'
DEST=os.path.join(ROOT,'logs','research','deep_fetch_turn27'); os.makedirs(DEST,exist_ok=True)
OUT=os.path.join(ROOT,'logs','research','github_sweep_turn27.jsonl')
H={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3+json'}
def api(path,retries=2,raw=False):
    hh=dict(H)
    if raw: hh['Accept']='application/vnd.github.v3.raw'
    for i in range(retries):
        req=urllib.request.Request('https://api.github.com'+path,headers=hh)
        try:
            with urllib.request.urlopen(req,timeout=30) as r: return r.read() if raw else json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            if e.code in (403,429):
                reset=e.headers.get('X-RateLimit-Reset'); wait=max(3,min(65,float(reset)-time.time()+2)) if reset else 30
                print(' rate',e.code,'wait',int(wait)); time.sleep(wait); continue
            print(' HTTP',e.code,path[:80]); return None
        except Exception as e: print(' err',e); time.sleep(4)
    return None

def code(q,pages=2):
    items=[]
    for p in range(1,pages+1):
        d=api(f'/search/code?q={urllib.parse.quote(q)}&per_page=100&page={p}')
        if not d or d.get('total_count',-1)<0: break
        items+=d.get('items',[])
        if len(d.get('items',[]))<100: break
        time.sleep(3)
    print(f'  Q="{q[:60]}" got={len(items)}')
    return {'query':q,'kind':'code','items':items,'total_count':len(items)}

def repos(q,pages=2):
    items=[]
    for p in range(1,pages+1):
        d=api(f'/search/repositories?q={urllib.parse.quote(q)}&per_page=100&page={p}')
        if not d: break
        items+=d.get('items',[])
        if len(d.get('items',[]))<100: break
        time.sleep(3)
    print(f'  R="{q[:60]}" got={len(items)}')
    return {'query':q,'kind':'repos','items':items,'total_count':len(items)}

results=[]
# Final precise queries
qs=[
    '"梦幻足球联盟" 26',
    '"梦幻足球联盟" 教练',
    '"DLS26" 教练',
    '"dream league soccer 2026" formation',
    '"DLS 26" "player development"',
    '"DLS26" "Season Pass"',
    '"first touch games" dls save',
    '"dream league soccer" sql',
    '"com.firsttouchgames.dls7" database',
    'DLS26 filename:player',
    '"DLS26" discord',
    '"dream league" subreddit',
]
for q in qs:
    results.append(code(q,pages=2)); time.sleep(1)
# Search repos (fan sites/tools)
for q in ['dls26','dream league soccer 2026','梦幻足球联盟26','dls 26 kit','dls 26 coach']:
    results.append(repos(q,pages=2)); time.sleep(1)
with open(OUT,'w',encoding='utf-8') as fh:
    for r in results: fh.write(json.dumps(r,ensure_ascii=False)+'\n')

# Pull LeoH321/dls26-tool-CB (CB = coach builder?) tree
print('\n=== LeoH321/dls26-tool-CB tree ===')
t=api('/repos/LeoH321/dls26-tool-CB/git/trees/HEAD?recursive=1')
if t and 'tree' in t:
    files=[x for x in t['tree'] if x.get('type')=='blob']
    print(f' {len(files)} files')
    for f in files[:40]: print(f'   {f.get("size",0):>8} {f["path"]}')
    # Pull HTML/JS/JSON
    for f in files:
        if any(f['path'].lower().endswith(e) for e in ['.html','.js','.json','.md','.css']) and f.get('size',0)<500_000:
            out=os.path.join(DEST,'LeoH321__CB__'+f['path'].replace('/','__'))
            if not os.path.exists(out):
                d=api(f'/repos/LeoH321/dls26-tool-CB/contents/{urllib.parse.quote(f["path"])}',raw=True)
                if d: open(out,'wb').write(d[:2_000_000]); print(f' pulled {f["path"]} {len(d)}b')
                time.sleep(1)
print('wrote',OUT)
