#!/usr/bin/env python3
"""Compare the blind 20-row re-extraction (chk/C*.json) with the first pass (out/G*.json).
Usage: python compare_check.py <work> <out_md>"""
import glob, json, os, sys
work, out_md = sys.argv[1], sys.argv[2]
def load(pat):
    d = {}
    for f in glob.glob(os.path.join(work, pat)):
        for r in json.load(open(f, encoding='utf-8')):
            d[f"{r['key']}|{r['period']}"] = r
    return d
def n(x): return x if isinstance(x, (int, float)) and not isinstance(x, bool) else None
def op(r, side):
    d = r.get(side) or {}
    p = n(d.get('pbt_before_exceptional'))
    if p is None: return None
    if r.get('lender'):
        tg_t, tg_l = n((r.get('this') or {}).get('treasury_gains')), n((r.get('last') or {}).get('treasury_gains'))
        return p - n(d.get('treasury_gains')) if (tg_t is not None and tg_l is not None) else p
    oi = n(d.get('other_income'))
    if oi is None: return None
    s = n(d.get('share_of_associates_jv')) if r.get('share_included_in_pbt_line') is True else 0
    return p - oi - (s or 0)
def growth(r):
    a, b = op(r, 'this'), op(r, 'last')
    return None if a is None or b is None or b <= 0 else (a / b - 1) * 100
A, B = load('out/G*.json'), load('chk/C*.json')
lines = ['# 20-row check', '', 'Twenty rows were drawn at random (seed 20261117) from the rows with a computed growth figure.',
         'A second reader re-read the PDF pages without seeing the first numbers. Growth was recomputed by the same formula.',
         'MATCH = recomputed growth within 0.1 percentage point of the first pass.', '',
         '| row | first pass growth % | recheck growth % | basis first / recheck | result | difference |', '|---|---|---|---|---|---|']
m = 0
for k in sorted(B):
    a, b = A.get(k), B[k]
    ga, gb = growth(a) if a else None, growth(b)
    ok = ga is not None and gb is not None and abs(ga - gb) <= 0.1
    m += ok
    diff = ''
    if not ok and a:
        ds = []
        for side in ('this', 'last'):
            for f in ('pbt_before_exceptional', 'other_income', 'share_of_associates_jv', 'treasury_gains'):
                x, y = (a.get(side) or {}).get(f), (b.get(side) or {}).get(f)
                if x != y: ds.append(f'{f} {side}: {x} vs {y}')
        for f in ('basis', 'unit', 'lender', 'share_included_in_pbt_line', 'period_type'):
            if a.get(f) != b.get(f): ds.append(f'{f}: {a.get(f)} vs {b.get(f)}')
        diff = '; '.join(ds)
    f1 = '' if ga is None else f'{ga:.1f}'; f2 = '' if gb is None else f'{gb:.1f}'
    lines.append(f"| {b.get('ticker')} {k.split('|')[1]} | {f1} | {f2} | {a.get('basis') if a else ''} / {b.get('basis')} | {'MATCH' if ok else 'DIFFERENT'} | {diff} |")
lines += ['', f'Result: {m} of {len(B)} matched.']
open(out_md, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('\n'.join(lines[7:]))
