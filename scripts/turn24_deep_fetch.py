#!/usr/bin/env python3
"""Turn 24 deep fetch of new promising repos discovered in wave 3."""
import json,os,time,urllib.request,base64
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADERS={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3+json'}
OUT=os.path.join(ROOT,'logs','research','deep_fetch_turn24')
os.makedirs(OUT,exist_ok=True)

def api(path,retries=3,raw=False):
    for i in range(retries):
        h=dict(HEADERS)
        if raw: h['Accept']='application/vnd.github.v3.raw'
        req=urllib.request.Request('https://api.github.com'+path,headers=h)
        try:
            with urllib.request.urlopen(req,timeout=30) as r:
                if raw: return r.read()
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            if e.code in (403,429):
                reset=e.headers.get('X-RateLimit-Reset');
                wait=max(3,min(90,float(reset)-time.time()+2)) if reset else 35
                print(' rate',e.code,'wait',int(wait)); time.sleep(wait); continue
            print(' HTTP',e.code,path[:80]); return None
        except Exception as e:
            print(' err',e); time.sleep(5)
    return None

def tree(full_name):
    d=api(f'/repos/{full_name}/git/trees/HEAD?recursive=1')
    if not d or 'tree' not in d: return None
    return d

def list_files(t):
    return [x for x in t['tree'] if x.get('type')=='blob']

def fetch_raw(full_name,path,save_to=None,max_bytes=2_000_000):
    data=api(f'/repos/{full_name}/contents/{path}',raw=True)
    if data is None: return None
    if save_to:
        os.makedirs(os.path.dirname(save_to),exist_ok=True)
        open(save_to,'wb').write(data[:max_bytes])
    return data

def safe_dir(name):
    return name.replace('/','__')

# Promising target repos (ordered by likely data density)
targets=[
    'Larrycr7aaaa/DLS-FIFA-FC-PES-UCS--FTG-API',  # 88MB - contains "FTG API" -> could be actual game API reverse-engineering
    'Larrycr7aaaa/specialcardsdls-api-and-database-css-html-js-json',
    'Larrycr7aaaa/DLS26-API',
    'Larrycr7aaaa/ultra-updated-dls26-and-api',
    'Larrycr7aaaa/26dls-41-cards-data',
    'Larrycr7aaaa/dls26-UPDTD',
    'Larrycr7aaaa/DLS-DATA-BASE',
    'fathidevs/DreamLeagueKit',  # real Android app com.gmail.dreamleaguekit
    'FootballGamingBD/dls-player-db',
    'FootballGamingBD/DLS26_PlayerData',
    'FootballGamingBD/Player-Database',
    'FootballGamingBD/players',
    'FootballGamingBD/PlayerDls',
    'FootballGamingBD/Dls',
    'TrungTaHust/dls',
    'TrungTaHust/dls-ext',
    'LeoH321/DLS26-quiz',
    'LeoH321/dls26-reaction-test',
    'LeoH321/DLSsuperleague',
    'wasswacosmas/DLS2026-game',
    'wasswacosmas/dls26',
    'wasswacosmas/dls_hub',
]

summary={}
for repo in targets:
    print(f'\n=== {repo} ===')
    safe=safe_dir(repo)
    repo_dir=os.path.join(OUT,safe); os.makedirs(repo_dir,exist_ok=True)
    t=tree(repo)
    if not t:
        print('  TREE FAILED'); summary[repo]={'err':'tree-failed'}; continue
    files=list_files(t)
    print(f'  {len(files)} files')
    # Identify small data-like files (json,js,html,txt,md,csv) - filter out PNG/JPG/mp3 assets
    data_files=[f for f in files if any(f['path'].lower().endswith(ext) for ext in ['.json','.js','.html','.md','.txt','.csv','.css','.xml','.java','.kt']) and f.get('size',0)<500_000]
    # identify any data-carrying files with large jsons
    big_data=[f for f in files if f['path'].lower().endswith('.json') and f.get('size',0)>500_000]
    print(f'  small data-like: {len(data_files)}  big json: {len(big_data)}')
    # Print tree of directories (non-asset names)
    dirs=sorted({os.path.dirname(f['path']) for f in files if os.path.dirname(f['path'])})
    if len(dirs)<40:
        for d in dirs[:40]: print(f'    dir: {d}')
    # Pull index.html/README first and any likely data file
    pulled=[]
    for cand in ['README.md','readme.md','index.html','Index.html','data.json','players.json','player.json','dls26.json','config.json','package.json','app.json','manifest.json']:
        match=[f for f in files if f['path'].lower()==cand.lower()]
        if match:
            f=match[0]
            ext=os.path.splitext(f['path'])[1]
            out_path=os.path.join(repo_dir,f['path'].replace('/','__'))
            try:
                data=fetch_raw(repo,f['path'],out_path)
                preview=(data[:800].decode('utf-8','ignore') if isinstance(data,bytes) else str(data)) if data else ''
                print(f'  pulled {f["path"]} ({f.get("size",0)} bytes)')
                print('    preview:',preview[:300].replace('\n',' '))
                pulled.append(f['path'])
            except Exception as e:
                print(f'  pull fail {f["path"]}: {e}')
            time.sleep(1)
    # Pull up to 8 additional interesting small data files (json/js that mention dls/player/stat/coach/form/ovr/rarity)
    keywords=['player','coach','stat','form','ovr','rarity','dream','dls26','card','pack','event','season','boost','point','tactic','formation']
    interesting=[]
    for f in data_files:
        low=f['path'].lower()
        if any(k in low for k in keywords) and f['path'] not in pulled:
            interesting.append(f)
    interesting.sort(key=lambda f:f.get('size',0))  # smallest first to save bandwidth
    for f in interesting[:8]:
        out_path=os.path.join(repo_dir,f['path'].replace('/','__'))
        try:
            data=fetch_raw(repo,f['path'],out_path)
            preview=(data[:500].decode('utf-8','ignore') if isinstance(data,bytes) else '') if data else ''
            print(f'  + {f["path"]} ({f.get("size",0)}b): {preview[:200].replace(chr(10)," ")}')
            pulled.append(f['path'])
        except Exception as e:
            print(f'  + fail {f["path"]}: {e}')
        time.sleep(1)
    summary[repo]={'total_files':len(files),'data_files':len(data_files),'big_json':len(big_data),'pulled':pulled,'top_dirs':dirs[:20]}
    # Save manifest
    with open(os.path.join(repo_dir,'_manifest.json'),'w') as fh:
        json.dump({'files':[{'path':f['path'],'size':f.get('size',0)} for f in files],'pulled':pulled},fh,indent=2)
    time.sleep(2)

with open(os.path.join(OUT,'_summary.json'),'w') as fh:
    json.dump(summary,fh,indent=2)
print('\nWROTE',os.path.join(OUT,'_summary.json'))
