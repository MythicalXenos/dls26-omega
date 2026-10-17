#!/usr/bin/env python3
"""Pull Randyblazedev/dls-hub key source files - community hub reveals economy/points/tournament/features."""
import os,time,urllib.request,urllib.parse,urllib.error
ROOT='/home/user/dls26-omega'
DEST=os.path.join(ROOT,'logs','research','randy_dls_hub'); os.makedirs(DEST,exist_ok=True)
H={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3.raw'}
KEY=['README.md','manifest.json','setup.sql','features.sql','tournaments_schema.sql','all_fixes.sql','points-from-posting.sql','dls-hub-points-migration.sql','rls_policies.sql','security_fixes.sql','fix-rls.sql','server.js','public/js/app.js','public/js/features.js','index.html']
def pull(path,maxb=300_000):
    out=os.path.join(DEST,path.replace('/','__'))
    if os.path.exists(out) and os.path.getsize(out)>50: return ('exists',os.path.getsize(out))
    req=urllib.request.Request(f'https://api.github.com/repos/Randyblazedev/dls-hub/contents/{urllib.parse.quote(path)}',headers=H)
    for i in range(3):
        try:
            with urllib.request.urlopen(req,timeout=30) as r: data=r.read()
            if maxb: data=data[:maxb]
            open(out,'wb').write(data); return ('pulled',len(data))
        except urllib.error.HTTPError as e:
            if e.code==404: return ('404',0)
            if e.code in (403,429): time.sleep(30); continue
            return (f'HTTP {e.code}',0)
        except Exception as e: time.sleep(4)
    return ('fail',0)
for f in KEY:
    s,n=pull(f); print(f'  {f}: {s} {n}'); time.sleep(1)
print('done')
