#!/usr/bin/env python3
"""Step 2 entry: locate a DLS26 APK via GitHub release/repo/LFS references (the only reachable host)."""
import json,os,time,urllib.request,urllib.parse,urllib.error
ROOT='/home/user/dls26-omega'
DEST=os.path.join(ROOT,'logs','research','apk_hunt'); os.makedirs(DEST,exist_ok=True)
H={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3+json'}
def api(path,retries=2):
    for i in range(retries):
        req=urllib.request.Request('https://api.github.com'+path,headers=H)
        try:
            with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            if e.code in (403,429):
                reset=e.headers.get('X-RateLimit-Reset'); wait=max(3,min(65,float(reset)-time.time()+2)) if reset else 30
                print(' rate',e.code,'wait',int(wait)); time.sleep(wait); continue
            print(' HTTP',e.code,path[:80]); return None
        except Exception as e: print(' err',e); time.sleep(3)
    return None
# Search repos with apk/releases mentioning com.firsttouchgames.dls7 OR dls26 apk
queries=[
    'com.firsttouchgames.dls7 apk',
    'dls26 apk',
    'dream league soccer 2026 apk',
    'firsttouchgames dls apk',
    '"DLS 26" filename:apk',
]
found=[]
for q in queries:
    d=api(f'/search/code?q={urllib.parse.quote(q)}&per_page=50')
    if d:
        for it in d.get('items',[]):
            r=it['repository']['full_name']; p=it['path']
            print(' ',r,p,it.get('html_url',''))
            found.append((r,p))
        time.sleep(3)
# Check releases on a few repos
print('\n=== Release checks ===')
for repo in ['wasswacosmas/DLS2026-game','wasswacosmas/dls26','thienntdev/bot-dls','imsaifbalti/dls-kit-generator','Larrycr7aaaa/DLS26-API','LeoH321/dls26-tool-CB','fathidevs/DreamLeagueKit']:
    rels=api(f'/repos/{repo}/releases?per_page=5')
    if rels:
        for r in rels:
            for a in r.get('assets',[]):
                if a.get('content_type','').endswith('apk') or '.apk' in a.get('name','').lower():
                    print(f'  {repo} release {r["tag_name"]}: asset {a["name"]} size={a["size"]} url={a["browser_download_url"]}')
                    found.append((repo,a['browser_download_url']))
        time.sleep(1)
json.dump(found,open(os.path.join(DEST,'candidates.json'),'w'),indent=2)
print('\nTotal candidates:',len(found))
