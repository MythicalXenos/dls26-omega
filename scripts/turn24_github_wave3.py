#!/usr/bin/env python3
"""Turn 24 GitHub wave 3 - finish remaining queries + sibling repo enumeration."""
import json,os,time,urllib.request,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'logs','research','github_sweep_turn24.jsonl')
HEADERS={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.text-match+json'}
def api(path,retries=3):
    for i in range(retries):
        req=urllib.request.Request('https://api.github.com'+path,headers=HEADERS)
        try:
            with urllib.request.urlopen(req,timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (403,429):
                reset=e.headers.get('X-RateLimit-Reset');
                wait=max(3,min(65,float(reset)-time.time()+2)) if reset else 30
                print(' rate-limit, waiting',int(wait),'s'); time.sleep(wait); continue
            print(' HTTP',e.code,path[:80]); return {'items':[],'total_count':-1,'_err':e.code}
        except Exception as e:
            print(' err',e); time.sleep(5); continue
    return {'items':[],'total_count':-1,'_err':'max-retries'}

def code(q,pages=5):
    all_items=[]; total=None
    for p in range(1,pages+1):
        enc=urllib.parse.quote(q)
        d=api(f'/search/code?q={enc}&per_page=100&page={p}')
        if d.get('_err'): break
        total=d.get('total_count',0) if total is None else total
        items=d.get('items',[])
        all_items+=items
        if len(items)<100: break
        time.sleep(3)
    print(f'  Q="{q[:50]}" total={total} got={len(all_items)}')
    return {'query':q,'kind':'code','total_count':total,'items':all_items,'ts':time.time()}

def repos(q,pages=3):
    all_items=[]; total=None
    for p in range(1,pages+1):
        enc=urllib.parse.quote(q)
        d=api(f'/search/repositories?q={enc}&per_page=100&page={p}')
        if d.get('_err'): break
        total=d.get('total_count',0) if total is None else total
        all_items+=d.get('items',[])
        if len(d.get('items',[]))<100: break
        time.sleep(3)
    print(f'  R="{q[:50]}" total={total} got={len(all_items)}')
    return {'query':q,'kind':'repos','total_count':total,'items':all_items,'ts':time.time()}

def repo_tree(full_name):
    d=api(f'/repos/{full_name}/git/trees/HEAD?recursive=1')
    if d.get('_err') or 'tree' not in d: return None
    files=[x for x in d['tree'] if x.get('type')=='blob']
    return {'name':full_name,'sha':d.get('sha'),'file_count':len(files),'files':files}

def repo_readme(full_name):
    """Fetch preferred readme if exists"""
    d=api(f'/repos/{full_name}/readme')
    if d.get('_err') or 'content' not in d: return None
    import base64
    try:
        return base64.b64decode(d['content']).decode('utf-8','ignore')
    except: return None

results=[]
# ---- remaining precise code queries ----
queries=[
    '"dls26 squad"',
    '"DLS 26" simulator',
    '"dream league soccer" discord',
    '"梦幻足球联盟"',
    '"梦幻足球联盟" 26',
    '"com.firsttouchgames" save',
    '"firsttouchgames" player stats',
    '"DLS 26" "Form Boost"',
    '"DLS 26" "Dream Points"',
    '"Dream League Soccer 2026" coach',
    'filename:playerdata "dream league"',
    'filename:coach "DLS"',
]
for q in queries:
    results.append(code(q,pages=4))
    time.sleep(2)

# ---- sibling repos: enumerate orgs/users that surfaced DBs ----
known_orgs=['FootballGamingBD','DLS26China','Larrycr7aaaa','lsproductionmarketing-oss','alexsuccess2013','imsaifbalti','TrungTaHust','LeoH321','wasswacosmas']
siblings={}
for org in known_orgs:
    d=api(f'/users/{org}/repos?per_page=100&type=all')
    if isinstance(d,list):
        rs=[]
        for r in d: rs.append({'name':r['full_name'],'desc':(r.get('description') or '')[:120],'stars':r.get('stargazers_count',0),'lang':r.get('language'),'size_kb':r.get('size',0)})
        siblings[org]=rs
        print(f'  {org}: {len(rs)} repos')
    else:
        print(f'  {org}: err {d.get("_err")}')
        siblings[org]=[]
    time.sleep(2)

# ---- readme + tree of promising siblings found from turn-22/23 lists ----
candidates=[
    'Larrycr7aaaa/UPDATED-DLS26-data-PF',
    'lsproductionmarketing-oss/dls26-kits',
    'imsaifbalti/dls-kit-generator',
    'imsaifbalti/dls-kits-generator',
    'alexsuccess2013/success---dls---zone',
    'TrungTaHust/dls_ext_sv',
    'dikbud/dikbud.github.io',
    'PRO100BYTE/ProjectArcade',
    'jeremyjia/Games',
    'doseeing/myrient_files',
    'ShuoAndy/ShuoAndy.github.io',
]
trees={}; readmes={}
for c in candidates:
    trees[c]=repo_tree(c)
    time.sleep(1)
    readmes[c]=repo_readme(c)
    time.sleep(1)

results.append({'query':'_siblings','kind':'aux','org_repos':siblings,'trees':{k:({'name':v['name'],'file_count':v['file_count'],'files':[{'p':f['path'],'s':f.get('size',0)} for f in v['files'] if any(ext in f['path'].lower() for ext in ['.json','.html','.js','.txt','.md','.csv'])]} if v else None) for k,v in trees.items()},'readmes':readmes,'ts':time.time()})

with open(OUT,'w',encoding='utf-8') as fh:
    for r in results: fh.write(json.dumps(r,ensure_ascii=False)+'\n')
print('wrote',OUT)
