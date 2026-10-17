#!/usr/bin/env python3
"""Pull critical data files from TrungTaHust/dls-ext (the real DLSStats app)."""
import os,time,urllib.request,json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST=os.path.join(ROOT,'logs','research','trungtahust')
os.makedirs(DEST,exist_ok=True)
HEADERS={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3.raw'}
REPO='TrungTaHust/dls-ext'
KEY=['resources/data/special.json','resources/data/price_map.json','resources/data/checklist.json','resources/data/player_id.json','resources/data/20261.json']
import urllib.error
for f in KEY:
    out=os.path.join(DEST,f.replace('/','__'))
    if os.path.exists(out) and os.path.getsize(out)>100:
        print('skip exists',f,os.path.getsize(out)); continue
    url=f'https://api.github.com/repos/{REPO}/contents/{f}'
    req=urllib.request.Request(url,headers=HEADERS)
    for i in range(3):
        try:
            with urllib.request.urlopen(req,timeout=60) as r:
                data=r.read()
            open(out,'wb').write(data)
            print(f'pulled {f} -> {len(data)} bytes')
            break
        except urllib.error.HTTPError as e:
            if e.code in (403,429):
                print('rate-limit wait',f); time.sleep(35); continue
            print('HTTP',e.code,f); break
        except Exception as e:
            print('err',e,f); time.sleep(5)
    time.sleep(2)
print('done')
