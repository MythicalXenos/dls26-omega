#!/usr/bin/env python3
"""ckpt-153: tier playbook + First Contact - the season-format rule, the coaching economy,
and refreshed bases."""
import io
def patch(P, subs):
    t=io.open(P,encoding='utf-8').read()
    for a,b in subs:
        assert a in t and t.count(a)==1, 'ANCHOR PROBLEM in '+P+': '+a[:70]
        t=t.replace(a,b,1)
    io.open(P,'w',encoding='utf-8').write(t)
    print('patched', P)

patch('/home/user/dls26-omega/docs/dll_tier_playbook.md', [
 ('> **Basis:** ckpt-133 — 1,628 claims / 372 evidence records.',
  '> **Basis:** ckpt-153 — 1,856 claims / 392 evidence records.'),
 ('''**The rule: aim for SURVIVAL, NOT PROMOTION.**

- Survival = win **4–5 matches** (12–15 points).
- Then **quit the rest** — and *losing en route is even better*, because it keeps you in the camping tier instead of promoting you into a harder one.
- **Do not forfeit.** Forfeiting may prevent you receiving the maximum gems. [EV-448, C3]''',
  '''**The rule: aim for SURVIVAL, NOT PROMOTION.**

- Survival = win **4–5 matches** (12–15 points).
- Then **quit the rest** — and *losing en route is even better*, because it keeps you in the camping tier instead of promoting you into a harder one.
- **Do not forfeit.** Forfeiting may prevent you receiving the maximum gems. [EV-448, C3]

> **⚠️ CHECK THE SEASON FORMAT FIRST** [EV-483, C2]. DLL seasons run **10 days** and the format **alternates between draw-allowed and extra-time-mandatory** — *"DLS switches between Extra Time and Draw after every season… the match format will again be draws and it will repeat like this"* — and the game tells you which at kick-off. **In a draw-allowed season the arithmetic above holds. In an extra-time season a draw is not a result**, it is a coin-flip you must play out: bank the 4–5 wins first, then treat any remaining match as a genuine extra-time match rather than a free point.'''),
 ('''**The one caveat:** this depends on being good enough to survive at tiers 2–5. If you cannot survive there, camp higher (tier 6–8) where survival is easier but the gem return is lower. The camping tier is a dial, not a fixed setting.''',
  '''**The one caveat:** this depends on being good enough to survive at tiers 2–5. If you cannot survive there, camp higher (tier 6–8) where survival is easier but the gem return is lower. The camping tier is a dial, not a fixed setting.

### 4.1 What a maxed player actually costs [EV-489, EV-490, C2/C3]

The tier ladder tells you where to play; this tells you what your squad is worth in the currencies you are earning.

| Route | Development points | Gems | **Gems per point** |
|---|---|---|---|
| Common coach | 2 | 63 | **31.5** |
| Rare coach | 6 | 168 | **28** |
| **Legendary coach** | 12 | 280 | **23.33** |

**One full max ≈ 90 points** — 45 Commons (2,835 gems) · 15 Rares (2,520 gems) · **7.5 Legendaries for special players, 9 for normal players**.

**Or pay in coins instead:** ~**32,000 coins** via Common coaches (80 releases at ~400 each) or ~**30,000** via Rare (20 at ~1,500), buying at or below the **192-coin** coach-farming threshold. **That is the real F2P price of one maxed player** — roughly 130 camping-hours of gems, or about 130 Career-match coin cycles.

> **The comparison that decides everything:** **1,125 gems ≈ 2.5 maxed players (~450 gems each).** So a facility level and a coaching decision are the same currency, and the facility priority order (Stadium → Training → Accommodation → Commercial → Medical → Recruitment) is a genuine optimisation, not a preference.

**Goalkeepers:** only use a Legendary coach when **GKR > GKH** — it raises both, so using it when GKH is already higher wastes half the value. Otherwise run **1 Rare + 4 Commons**.'''),
])

patch('/home/user/dls26-omega/step5_first_contact/FIRST_CONTACT_v2.md', [
 ('> **Basis:** ckpt-135', '> **Basis:** ckpt-153'),
])
