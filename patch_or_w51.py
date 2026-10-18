#!/usr/bin/env python3
"""ckpt-127: operational rules - stadium gate rule, Cult Heroes rule, rank ladder."""
import io
P='/home/user/dls26-omega/docs/operational_rules.md'
t=io.open(P,encoding='utf-8').read()
def sub(a,b):
    global t
    assert a in t, 'MISSING ANCHOR: '+a[:80]
    assert t.count(a)==1, 'ANCHOR NOT UNIQUE: '+a[:80]
    t=t.replace(a,b,1)

sub("> Basis: ckpt-126 — 1,546 claims / 360 evidence records. Companion to `docs/strategy_masterplan.md`.",
    "> Basis: ckpt-127 — 1,565 claims / 363 evidence records. Companion to `docs/strategy_masterplan.md`.")
sub("*End of operational rules. Authority: `kb/claims.jsonl` (1,546 claims) + `docs/continuity/a7e23a6b/evidence/index.jsonl` (360 records) at ckpt-126.*",
    "*End of operational rules. Authority: `kb/claims.jsonl` (1,565 claims) + `docs/continuity/a7e23a6b/evidence/index.jsonl` (363 records) at ckpt-127.*")

# Stadium rules - insert before the season-pass retroactivity block added at ckpt-126
anchor = "**The Season Pass retroactivity rule**"
assert anchor in t, 'season pass anchor missing'
stadium = """**The stadium capacity gate** [EV-460, C2] — the rule that can silently stall a Career season:

| Rule | Detail |
|---|---|
| **Capacity gates promotion** | Win the league without the seats and you **stay in the division**: Academy 6,462 → Div 3 15,000 → Div 2 30,000 → Div 1 45,000 → Junior Elite 60,000 → Elite 80,000 (max 90,456) |
| **Build corners first** | Corners are the cheap seats — Corner 7 is about **100 coins for 722 seats**. Corner stands give the most seats per coin |
| **Never half-upgrade a stand** | A partial side must later be paid for **at full price** to complete |
| **One stand at a time, lowest to highest** | Max one stand before starting the next; **leave one corner stand un-upgraded** — 7 maxed stands hit the top gate, 8 overshoot it |
| **Never roof the top level** | *"on the highest number you're paying for the roof and no extra seats"* |
| **Capacity is permanent** | **Downgrading was removed around DLS24** — build to the gate, not to a design, because it cannot be undone |
| **It is a COIN project** | Every sector level costs coins (roughly 0–650), not gems — the facilities are the gem project, the stadium is the coin project |

"""
t = t.replace(anchor, stadium + anchor, 1)

# Cult Heroes rule - append after the stadium block via the training ladder anchor
anchor2 = "**The training-facility ladder**"
assert anchor2 in t, 'training ladder anchor missing'
ch = """**Cult Heroes** [EV-459, C2] — 12 players, base ratings **85/85/85/84/84/84/84/84/83/83/83/83**, from **Cult Hero Agents in Events, Drafts and the Season Pass** (3 passes × 2 heroes, one free + one premium = 6 of 12). **The 92-vs-95 conflict is resolved: 85 = base, 92 = live-event boosted, 95 = fully maxed.** They are the **weakest special set by ceiling** — collect for the card, not the rating.

"""
t = t.replace(anchor2, ch + anchor2, 1)

io.open(P,'w',encoding='utf-8').write(t)
print('operational rules patched OK')
