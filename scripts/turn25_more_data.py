#!/usr/bin/env python3
"""Turn 25 - pull more TrungTaHust data files (20262, 20263, 2025x) and Larrycr7aaaa FTG API repo."""
import os,time,urllib.request,urllib.error,json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADERS={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3.raw'}
def pull(repo,path,out,max_bytes=20_000_000):
    os.makedirs(os.path.dirname(out),exist_ok=True)
    if os.path.exists(out) and os.path.getsize(out)>100: return ('exists',os.path.getsize(out))
    req=urllib.request.Request(f'https://api.github.com/repos/{repo}/contents/{path}',headers=HEADERS)
    for i in range(3):
        try:
            with urllib.request.urlopen(req,timeout=90) as r: data=r.read()
            if max_bytes: data=data[:max_bytes]
            open(out,'wb').write(data); return ('pulled',len(data))
        except urllib.error.HTTPError as e:
            if e.code in (403,429): time.sleep(35); continue
            if e.code==404: return ('404',0)
            return (f'HTTP {e.code}',0)
        except Exception as e: time.sleep(5)
    return ('fail',0)

DEST=os.path.join(ROOT,'logs','research','trungtahust')
results={}
for f in ['resources/data/20262.json','resources/data/20263.json','resources/data/20253.json','resources/data/20252.json','resources/data/data.json']:
    out=os.path.join(DEST,f.replace('/','__'))
    st,n=pull('TrungTaHust/dls-ext',f,out)
    print(f'  {f}: {st} {n}'); results[f]=(st,n)
    time.sleep(2)

# Larrycr7aaaa DLS-FIFA-FC-PES-UCS--FTG-API tree scan -> pull interesting small files
LDEST=os.path.join(ROOT,'logs','research','larrycr7aaaa_ftgapi')
os.makedirs(LDEST,exist_ok=True)
req=urllib.request.Request('https://api.github.com/repos/Larrycr7aaaa/DLS-FIFA-FC-PES-UCS--FTG-API/git/trees/HEAD?recursive=1',headers={'User-Agent':'dls26-omega-research'})
with urllib.request.urlopen(req,timeout=30) as r: t=json.loads(r.read())
files=[x for x in t['tree'] if x.get('type')=='blob']
print(f'\nLarrycr7aaaa/FTG-API: {len(files)} files')
data_files=[f for f in files if any(f['path'].lower().endswith(ext) for ext in ['.json','.js','.html','.md','.css','.txt','.csv']) and f.get('size',0)<500_000]
print('  small data-like:',len(data_files))
for f in data_files:
    out=os.path.join(LDEST,f['path'].replace('/','__'))
    st,n=pull('Larrycr7aaaa/DLS-FIFA-FC-PES-UCS--FTG-API',f['path'],out)
    print(f'  {f["path"]}: {st} {n}')
    time.sleep(1)
json.dump(results,open(os.path.join(DEST,'turn25_pull_log.json'),'w'),indent=2)
print('done')
