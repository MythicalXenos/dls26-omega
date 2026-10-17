#!/usr/bin/env python3
"""Pull thienntdev/bot-dls key source files to learn HUD layout, game states, ad detection, resource targets."""
import os,time,urllib.request,urllib.parse,urllib.error
ROOT='/home/user/dls26-omega'
DEST=os.path.join(ROOT,'logs','research','thienntdev_botdls'); os.makedirs(DEST,exist_ok=True)
H={'User-Agent':'dls26-omega-research','Accept':'application/vnd.github.v3.raw'}
KEY=[
 'README.md','config/settings.py','config/ai_ml_config.py','config/resource_targets.json',
 'core/bot_manager.py','core/central_data_collector.py','core/input_scheduler.py',
 'emulator/emulator_controller.py',
 'game_logic/action_executor.py','game_logic/ad_handler.py','game_logic/computer_vision.py',
 'game_logic/decision_maker.py','game_logic/game_bot.py','game_logic/game_controller.py',
 'game_logic/game_state_detector.py','game_logic/machine_learning.py','game_logic/resource_manager.py',
 'game_logic/special_situations.py','game_logic/deep_learning.py','game_logic/natural_language.py',
 'docs/USAGE.md','AI_ML_FEATURES.md','main.py','requirements.txt',
 'logs/dls_bot_20250814_154001.log'  # sample log
]
def pull(path,maxb=200_000):
    out=os.path.join(DEST,path.replace('/','__'))
    if os.path.exists(out) and os.path.getsize(out)>50: return ('exists',os.path.getsize(out))
    req=urllib.request.Request(f'https://api.github.com/repos/thienntdev/bot-dls/contents/{urllib.parse.quote(path)}',headers=H)
    for i in range(3):
        try:
            with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
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
