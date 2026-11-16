#!/usr/bin/env python3
"""Remove holdings, cost and position-size wording before the folder goes to a public repo.

Usage: python scrub_public.py <retro_dir> [--report removed.txt]
Works clause by clause on census.csv cells and companies/*.md lines. A clause that
mentions an actual holding, its cost or its size is replaced by
"[holding detail removed]". Person names are replaced by "operator".
Valuation outputs (fair value, entry zone) and verdict words are left alone.
"""
import csv
import glob
import io
import re
import sys

R = sys.argv[1]
report = sys.argv[sys.argv.index('--report') + 1] if '--report' in sys.argv else None
MARK = '[holding detail removed]'

HOLD = re.compile(
    r'\(held\)|\bnot held\b|\bposition held\b|\balready held\b|\bheld[,.:;)\'" -]|\bheld$|\bheld (as|at|since|from|with a|\d)|'
    r'\d+(\.\d+)?\s*%\s*(position|starter|momentum|allocation|weight|cap\b|max\b|of (the )?portfolio)|'
    r'\bposition\s+(size|sizing|cap|zero|held|at rs|fully|exited|small|is not|was already|then|status|date)|'
    r'\b(small|starter|full|half|core|tracking)\s+position\b|\bposition\b.{0,30}\d+(\.\d+)?\s*%|\d+(\.\d+)?\s*%.{0,30}\bposition\b|'
    r'\btrim(s|med|ming)?\b|\bavg\.? cost\b|\baverage cost\b|\bcost basis\b|\bat rs\.?\s*[\d,.]+ cost\b|\bbought\b|'
    r'\bbuy price\b|\bpurchase price\b|\bour cost\b|\bfully exited\b|\bposition exited\b|\bexited (on )?\d|\btranche\b|\bstarter\b|'
    r'\bmomentum bucket\b|\bholding sleeve\b|\bour holding|\bwe hold\b|\bwe own\b|\bholdings? table\b|holdings\.md|'
    r'\b(add|added|adding) to (the )?position\b|\bhold at \d|\bhold \d+(\.\d+)?\s*%|\bportfolio weight\b|\bportfolio, set by hand',
    re.I)
SAFE = re.compile(
    r'meeting|agm\b|egm\b|\bcall\b|concall|conference|promoter|pledge|for sale|subsidiar|investments? held|treasury|'
    r'shareholding|cash held|inventor|land held|held by|held on|held in|held to maturity|held-for', re.I)
STRONG = re.compile(
    r'\bHELD\b|\bEXITED\b|momentum bucket|momentum trade|\bno position\b|pre-position|non-held|\bnot held\b|\(held\)|'
    r'avg\.? cost|cost basis|position size|\d+(\.\d+)?\s*%\s*position|\bstarter\b|\btranche\b|upsize to \d|'
    r'\bdo not add\b|\bno add\b|\bHOLD \d|\bstop Rs')
STRONG_I = re.compile(r'momentum bucket|momentum trade|\bno position\b|pre-position|non-held|\bnot held\b|avg\.? cost|'
                      r'cost basis|position size|\bstarter\b|\btranche\b|upsize to \d|\bdo not add\b|\bno add\b', re.I)
NAMES = re.compile(r'\b(Keerti Kaushik|Keerti|Kaushik|Sumit Sharma|Sumit)\b')
removed = []


def scrub(text, where):
    parts = re.split(r'(\s\|\s|;\s|(?<=[a-z0-9\)\]\'"])\.\s)', text)
    out = []
    for p in parts:
        if p and (STRONG.search(p) or STRONG_I.search(p)):
            removed.append(f'{where}	{p.strip()[:240]}')
            lead = re.match(r'^\s*(- )?([a-z_ /]+:\s)?', p, re.I).group(0)
            out.append(lead + MARK)
        elif p and HOLD.search(p) and not (SAFE.search(p) and not re.search(
                r'position|trim|avg\.? cost|cost basis|starter|tranche|\(held\)|not held', p, re.I)):
            removed.append(f'{where}\t{p.strip()[:240]}')
            lead = re.match(r'^\s*(- )?([a-z_ /]+:\s)?', p, re.I).group(0)
            out.append(lead + MARK)
        else:
            out.append(p)
    return NAMES.sub('operator', ''.join(out))


f = R + '/census.csv'
rows = list(csv.reader(open(f, encoding='utf-8-sig', newline='')))
for i, row in enumerate(rows[1:], 1):
    rows[i] = [scrub(c, f'census:{row[0]}:{row[2]}') for c in row]
buf = io.StringIO()
csv.writer(buf, lineterminator='\r\n').writerows(rows)
open(f, 'w', encoding='utf-8-sig', newline='').write(buf.getvalue())

for f in glob.glob(R + '/companies/*.md'):
    lines = open(f, encoding='utf-8').read().split('\n')
    name = f.replace('\\', '/').rsplit('/', 1)[1]
    open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(scrub(l, name) for l in lines))

if report:
    open(report, 'w', encoding='utf-8').write('\n'.join(removed))
print('clauses removed', len(removed))
