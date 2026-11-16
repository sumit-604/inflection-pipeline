#!/usr/bin/env python3
"""Compute operating-profit growth and labels from the extracted filing figures.

Usage: python compute_growth.py <work> <out_dir>
  <work>/filing_map.json, <work>/universe.csv   from build_universe.py
  <work>/out/G*.json                            reader output (EXTRACT_BRIEF.md)
Writes <out_dir>/universe.csv, growth.csv, names.md, missing.md.

Method (same for both years):
  operating profit before tax = profit before tax and exceptional items
                                - other income
                                - share of associates/JVs (only if that share is inside the PBT line)
  operating profit after tax  = operating profit before tax x (1 - 25.17%)
  growth = this year / last year - 1   (identical before and after the flat tax rate)
Lenders: profit before tax and exceptional items minus treasury/trading gains
  where the filing states them; otherwise reported profit before tax, marked LENDER-REPORTED.
"""
import collections
import csv
import glob
import json
import os
import re
import shutil
import sys

work, out = sys.argv[1], sys.argv[2]
TAX = 0.2517
PERIODS = ['Q4 FY26', 'Q1 FY27', 'Q2/H1 FY27']
LABELS = ['ABOVE 25%', '0 TO 25%', 'FELL', 'LOSS', 'TURNAROUND', 'LOW BASE', 'NO FILING', 'NOT COMPARABLE']


def factor(unit):
    u = (unit or '').lower()
    if 'lakh' in u or 'lac' in u:
        return 0.01
    if 'crore' in u or re.search(r'\bcr\b', u):
        return 1.0
    if 'million' in u or re.search(r'\bmn\b', u):
        return 0.1
    if 'billion' in u:
        return 100.0
    if 'thousand' in u or "'000" in u or '000s' in u:
        return 0.0001
    if 'hundred' in u:
        return 0.00001
    if re.search(r'rupees|\binr\b|\brs\.?$|^rs\.?$|^₹$', u):
        return 0.0000001
    return None


def num(x):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else None


fmap = json.load(open(os.path.join(work, 'filing_map.json'), encoding='utf-8'))
ext = {}
for f in sorted(glob.glob(os.path.join(work, 'out', 'G*.json'))):
    try:
        data = json.load(open(f, encoding='utf-8'))
    except ValueError as e:
        print('BAD JSON', f, e)
        continue
    for r in data:
        ext[f"{r.get('key')}|{r.get('period')}"] = r


def fmt(x, nd=2):
    return '' if x is None else f'{x:.{nd}f}'


rows = []
for k, e in fmap.items():
    key, period = k.split('|')
    r = ext.get(k)
    row = collections.OrderedDict(
        ticker=e['ticker'], name=e['name'], period=period, basis='', period_type='', unit_as_filed='',
        this_label='', last_label='')
    for side in ('this', 'last'):
        for fld in ('pbt_before_exceptional', 'other_income', 'exceptional_items', 'share_of_associates_jv',
                    'treasury_gains', 'pat'):
            row[f'{fld}_{side}_as_filed'] = ''
    row.update(pbt_before_exceptional_this_cr='', other_income_this_cr='', exceptional_items_this_cr='',
               op_profit_before_tax_this_cr='', op_profit_before_tax_last_cr='',
               op_profit_after_tax_this_cr='', op_profit_after_tax_last_cr='',
               growth_pct='', reported_profit_growth_pct='', label='', lender_note='',
               results_file='', page='', page_source='', notes='')
    if not e['files']:
        row['label'] = 'NO FILING'
        row['notes'] = 'No results filing for this period found on this machine.'
        rows.append(row)
        continue
    if r is None:
        row['label'] = 'NO FILING'
        row['notes'] = 'Filing candidate found but no figures were extracted.'
        row['results_file'] = ' ; '.join(f['origin'] for f in e['files'])
        rows.append(row)
        continue
    status = (r.get('status') or '').upper()
    row['basis'] = r.get('basis') or ''
    row['period_type'] = r.get('period_type') or ''
    row['unit_as_filed'] = r.get('unit') or ''
    row['this_label'] = r.get('this_label') or ''
    row['last_label'] = r.get('last_label') or ''
    origin = ''
    fn = (r.get('file') or '')
    for f in e['files']:
        if fn and os.path.basename(fn).lower().replace('.txt', '') in f['origin'].lower():
            origin = f['origin']
            break
    row['results_file'] = origin or (fn + ' [from: ' + ' ; '.join(f['origin'] for f in e['files']) + ']')
    row['page'] = str(r.get('page') or '')
    row['page_source'] = r.get('page_source') or ''
    notes = [re.sub(r'\s+', ' ', str(r.get('notes') or '')).strip()]
    if status == 'NO FILING':
        row['label'] = 'NO FILING'
        row['notes'] = 'File on this machine is not the statement of results for this period: ' + notes[0]
        rows.append(row)
        continue
    t, l = r.get('this') or {}, r.get('last') or {}
    for side, d in (('this', t), ('last', l)):
        for fld in ('pbt_before_exceptional', 'other_income', 'exceptional_items', 'share_of_associates_jv',
                    'treasury_gains', 'pat'):
            v = num(d.get(fld))
            row[f'{fld}_{side}_as_filed'] = '' if v is None else repr(v)
    fx = factor(r.get('unit'))
    lender = bool(r.get('lender'))
    inc = r.get('share_included_in_pbt_line') is True

    def op(d):
        p = num(d.get('pbt_before_exceptional'))
        if p is None:
            return None
        if lender:
            tg = num(d.get('treasury_gains'))
            return p - tg if tg is not None else p
        oi = num(d.get('other_income'))
        if oi is None:
            return None
        s = num(d.get('share_of_associates_jv')) if inc else 0
        return p - oi - (s or 0)

    if status == 'NOT COMPARABLE':
        row['label'] = 'NOT COMPARABLE'
        notes.insert(0, 'Reason: ' + re.sub(r'\s+', ' ', str(r.get('not_comparable_reason') or 'not stated')))
    o_t, o_l = op(t), op(l)
    if fx is None and (o_t is not None):
        notes.append(f'Unit "{r.get("unit")}" not converted to crore.')
    if lender:
        both_tg = num(t.get('treasury_gains')) is not None and num(l.get('treasury_gains')) is not None
        if not both_tg:
            # use reported PBT on both sides for a like-for-like method
            o_t, o_l = num(t.get('pbt_before_exceptional')), num(l.get('pbt_before_exceptional'))
            row['lender_note'] = 'LENDER-REPORTED (profit before tax as reported; treasury gains not stated for both years)'
        else:
            row['lender_note'] = 'LENDER (profit before tax minus stated treasury/trading gains)'
    if fx is not None:
        for fld in ('pbt_before_exceptional', 'other_income', 'exceptional_items'):
            v = num(t.get(fld))
            row[f'{fld}_this_cr'] = fmt(v * fx) if v is not None else ''
    c_t = o_t * fx if (o_t is not None and fx is not None) else None
    c_l = o_l * fx if (o_l is not None and fx is not None) else None
    row['op_profit_before_tax_this_cr'] = fmt(c_t)
    row['op_profit_before_tax_last_cr'] = fmt(c_l)
    row['op_profit_after_tax_this_cr'] = fmt(c_t * (1 - TAX)) if c_t is not None else ''
    row['op_profit_after_tax_last_cr'] = fmt(c_l * (1 - TAX)) if c_l is not None else ''
    g = None
    if o_t is not None and o_l is not None and o_l > 0:
        g = (o_t / o_l - 1) * 100
        row['growth_pct'] = fmt(g, 1)
    pt, pl = num(t.get('pat')), num(l.get('pat'))
    if pt is not None and pl is not None and pl > 0:
        row['reported_profit_growth_pct'] = fmt((pt / pl - 1) * 100, 1)
    if not row['label']:
        if o_t is None or o_l is None:
            row['label'] = 'NOT COMPARABLE'
            d = t if o_t is None else l
            miss = 'this year' if o_t is None else 'last year'
            what = 'profit before tax and exceptional items' if num(d.get('pbt_before_exceptional')) is None \
                else 'other income as a separate line'
            notes.insert(0, f'Reason: the statement of results does not show {what} for {miss}, '
                            f'so operating profit cannot be computed by the stated method.')
        elif o_t < 0:
            row['label'] = 'LOSS'
        elif o_l <= 0:
            row['label'] = 'TURNAROUND'
        elif c_l is not None and c_l < 1:
            row['label'] = 'LOW BASE'
        elif g > 25:
            row['label'] = 'ABOVE 25%'
        elif g >= 0:
            row['label'] = '0 TO 25%'
        else:
            row['label'] = 'FELL'
    row['notes'] = ' | '.join(n for n in notes if n)
    rows.append(row)

rows.sort(key=lambda r: (PERIODS.index(r['period']), r['ticker']))
os.makedirs(out, exist_ok=True)
shutil.copy(os.path.join(work, 'universe.csv'), os.path.join(out, 'universe.csv'))
with open(os.path.join(out, 'growth.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(list(rows[0].keys()))
    for r in rows:
        w.writerow(list(r.values()))


def gkey(r):
    try:
        return -float(r['growth_pct'])
    except ValueError:
        return float('inf')


md = ['# Operating profit growth, by period and label', '',
      'Operating profit before tax = profit before tax and exceptional items minus other income. '
      'Growth is year on year. Sorted by growth, highest first. Source figures and pages: growth.csv.', '']
ms = ['# Results filings to fetch (NO FILING rows)', '',
      'A review exists for these, but the statement of results is not on this machine.', '']
summary = {}
for p in PERIODS:
    pr = [r for r in rows if r['period'] == p]
    cnt = collections.Counter(r['label'] for r in pr)
    summary[p] = cnt
    md += [f'## {p} ({len(pr)} results)', '']
    for lab in LABELS:
        lr = sorted([r for r in pr if r['label'] == lab], key=lambda r: (gkey(r), r['ticker']))
        md += [f'### {lab} ({len(lr)})', '']
        for r in lr:
            g = f"{r['growth_pct']}%" if r['growth_pct'] else 'n/a'
            extra = f" [{r['lender_note'].split(' (')[0]}]" if r['lender_note'] else ''
            if lab in ('NO FILING',):
                md.append(f"- {r['ticker']} ({r['name']})")
            elif lab in ('LOSS', 'TURNAROUND', 'NOT COMPARABLE'):
                md.append(f"- {r['ticker']} ({r['name']}): operating profit Rs {r['op_profit_before_tax_this_cr'] or 'n/a'} Cr "
                          f"vs Rs {r['op_profit_before_tax_last_cr'] or 'n/a'} Cr last year{extra}")
            else:
                md.append(f"- {r['ticker']} ({r['name']}): {g} (Rs {r['op_profit_before_tax_this_cr']} Cr vs "
                          f"Rs {r['op_profit_before_tax_last_cr']} Cr; {r['basis']}){extra}")
        md.append('')
    nf = sorted([r for r in pr if r['label'] == 'NO FILING'], key=lambda r: r['ticker'])
    ms += [f'## {p} ({len(nf)})', '']
    ms += [f"- {r['ticker']} | {r['name']} | {p} | {r['notes']}" for r in nf] + ['']
open(os.path.join(out, 'names.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
open(os.path.join(out, 'missing.md'), 'w', encoding='utf-8').write('\n'.join(ms) + '\n')
print('rows', len(rows), 'extracted', len(ext))
for p in PERIODS:
    print(p, sum(summary[p].values()), {lab: summary[p][lab] for lab in LABELS})
