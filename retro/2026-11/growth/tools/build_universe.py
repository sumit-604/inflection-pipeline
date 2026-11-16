#!/usr/bin/env python3
"""Build the universe of analysed results and find a results filing for each row.

Usage: python build_universe.py <repo> <work> <census.csv> <companies.json> <local_root> [...]
  <work>/results_inv.tsv   branch \t blob \t size \t path   (git ls-tree -r -l over all branches,
                           lines whose path mentions result/financial)
Writes <work>/universe.csv, <work>/filing_map.json and copies each chosen filing
to <work>/filings/<key>/<period>/ (PDF converted with `pdftotext -layout`, one
"=== PAGE n ===" marker per page).

A row is in the universe when
  A. a repo quarterly folder exists for the company and period, or
  B. the local "Q2 FY27 Results" folder has a folder for the company, or
  C. the earlier census has actuals for that company and period.
"""
import collections
import csv
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
from extract_session_excerpts import build_patterns  # noqa: E402

repo, work, census_csv, comp_json = sys.argv[1:5]
local_roots = sys.argv[5:]
PERIODS = ['Q4 FY26', 'Q1 FY27', 'Q2/H1 FY27']
SUFFIX = {'q4fy26': 'Q4 FY26', 'q1fy27': 'Q1 FY27', 'q2cy26': 'Q1 FY27', 'q2fy27': 'Q2/H1 FY27',
          'h1fy27': 'Q2/H1 FY27'}
TOK = {
    'Q4 FY26': re.compile(r'q4.?fy.?(20)?(25.)?26|fy.?(20)?(25.)?26.?audit|audit\w*.{0,12}fy.?26|mar(ch)?.?(31)?.{0,2}2026|'
                          r'31.?0?3.?2026|2026-?05-?\d\d|fy26.?(annual|full)', re.I),
    'Q1 FY27': re.compile(r'q1.?fy.?(20)?(26.)?27|fy.?27.?q1|jun(e)?.?(30)?.{0,2}2026|30.?0?6.?2026|2026-?0[78]-?\d\d', re.I),
    'Q2/H1 FY27': re.compile(r'q2.?fy.?(20)?(26.)?27|h1.?fy.?(20)?(26.)?27|fy.?27.?q2|sep(t|tember)?.?(30)?.{0,2}2026|'
                             r'30.?0?9.?2026|2026-?1[01]-?\d\d', re.I),
}
TEXTKIND = re.compile(r'fulltext|extract_results|extracted/results|a1-results/[^/]*\.(txt|md)$|_textcache|'
                      r'ocr|inputs/results/[^/]*\.txt$', re.I)
NOTFILING = re.compile(r'/blocks/|\.py$|\.ya?ml$|\.json$|\.png$|\.jpe?g$|\.pkl$|\.sh$|ledger|forensic|audit_|'
                       r'/review_|structured|press.?release|presentation|transcript|concall|-pages/|/pages/|/img/|'
                       r'/images/|auditors?_report|rating', re.I)

MANUAL = {'Paushak': 'paushak', 'Urban Company': 'urbanco', 'Aurum Proptech': 'aurum', 'Cyient DLM': 'cyientdlm',
          'Fedbank Financial': 'fedfina', 'Indo Rama': 'indorama', 'Karnika Industries': 'karnika',
          'Kross': 'kross', 'HFCL': 'hfcl', 'Tatva Chintan': 'tatva', 'GOCL Corporation': 'goclcorp',
          'Netweb Technologies': 'netweb', 'Aequs': 'aequs', 'Gallantt Ispat': 'gallantt',
          'Quality Power': 'qpower', 'Pitti Engineering': 'pittieng', 'Indiamart': 'indiamart',
          'Paisalo Digital': 'paisalo', 'Syngene': 'syngene', 'Cybertech Systems': 'cybertech',
          'Aye Finance': 'aye', 'Indosolar': 'indosolar', 'Ador Welding': 'ador', 'Route Mobile': 'route',
          'Knack Packaging': 'knack', 'Dynamic Cables': 'dycl', 'Sky Gold': 'skygold',
          'Neochem': 'neochem', 'Pure Tropic': '530077', 'Yash Highvoltage': 'yashhv'}
companies = json.load(open(comp_json, encoding='utf-8'))
pats = build_patterns(companies)
run2key = {r: k for k, v in companies.items() for r in v['runs']}

census = list(csv.DictReader(open(census_csv, encoding='utf-8-sig')))
# census rows are in companies.json key order, 3 per key
keys = sorted(companies)
tick = {}
uni = collections.OrderedDict()   # (key, period) -> dict
maybe = {}
for i, key in enumerate(keys):
    rows = census[i * 3:i * 3 + 3]
    tick[key] = (rows[0]['ticker'], rows[0]['name'])
    for r in rows:
        if not r['actual revenue'].startswith('NOT FOUND'):
            segs = [s for s in r['source file for every number'].split(' | ') if s.strip().startswith('actual')]
            src = ' '.join(segs)
            if re.search(r'ConcallPipeline|excerpts/(local|sessions)|session \d{4}', src):
                uni[(key, r['period'])] = {'where': ['local or session review note (see census.csv sources)']}
            else:
                maybe[(key, r['period'])] = True

for key, v in companies.items():
    for run in v['runs']:
        m = re.search(r'-([qh]\d[fc]y\d\d)$', run)
        if m and m.group(1) in SUFFIX:
            d = uni.setdefault((key, SUFFIX[m.group(1)]), {'where': []})
            d['where'].insert(0, f'repo quarterly folder runs/{run}')
            d.setdefault('qfolders', []).append(run)

# local Q2 folder
local_pdfs = []
for root in local_roots:
    for d, _, names in os.walk(root):
        for n in names:
            if n.lower().endswith('.pdf') and re.search(r'result|financial', n, re.I) \
                    and not re.search(r'presentation|press|transcript|newspaper|publication', n, re.I):
                local_pdfs.append(os.path.join(d, n))
        if os.path.basename(os.path.dirname(d)) == 'Q2 FY27 Results' or os.path.basename(d) == 'Q2 FY27 Results':
            pass
q2root = None
for root in local_roots:
    p = os.path.join(root, 'Q2 FY27 Results')
    if os.path.isdir(p):
        q2root = p
        for name in sorted(os.listdir(p)):
            if not os.path.isdir(os.path.join(p, name)):
                continue
            label = re.sub(r'^\d+\s+', '', name)
            label = re.sub(r'\(.*?\)', '', label).strip()
            hit = [MANUAL[label]] if label in MANUAL else [k for k, pt in pats.items() if pt.search(label)]
            print('Q2 folder', repr(label), '->', hit)
            if len(hit) != 1:
                hit = []
            if len(hit) >= 1:
                k = hit[0]
                d = uni.setdefault((k, 'Q2/H1 FY27'), {'where': []})
                d['where'].append(f'local folder Q2 FY27 Results/{name}')
                d['q2dir'] = os.path.join(p, name)
            else:
                print('UNMATCHED local Q2 folder:', name)

# repo candidates
inv = collections.defaultdict(dict)   # path -> blob (newest irrelevant; first wins), keep size
for l in open(os.path.join(work, 'results_inv.tsv'), encoding='utf-8', errors='replace'):
    b, blob, size, path = l.rstrip('\n').split('\t', 3)
    parts = path.split('/')
    if len(parts) < 3 or parts[1] not in run2key:
        continue
    if NOTFILING.search(path):
        continue
    if not (path.lower().endswith('.pdf') or TEXTKIND.search(path)):
        continue
    inv[path] = (blob, int(size) if size.isdigit() else 0, b)

by_key = collections.defaultdict(list)
for path, (blob, size, b) in inv.items():
    by_key[run2key[path.split('/')[1]]].append((path, blob, size, b))


def pick(key, period, info):
    cands = []
    for path, blob, size, b in by_key.get(key, []):
        run = path.split('/')[1]
        rest = '/'.join(path.split('/')[2:])
        in_q = run in info.get('qfolders', [])
        tokhit = bool(TOK[period].search(rest))
        other = any(TOK[p].search(rest) for p in PERIODS if p != period)
        if in_q and not (other and not tokhit):
            score = 3
        elif tokhit and not re.search(r'-[qh]\d[fc]y\d\d$', run):
            score = 2
        elif tokhit:
            score = 1
        else:
            continue
        cands.append((score, path, blob, size, b))
    pdf = sorted([c for c in cands if c[1].lower().endswith('.pdf')], key=lambda c: (-c[0], -c[3]))
    txt = sorted([c for c in cands if not c[1].lower().endswith('.pdf')], key=lambda c: (-c[0], -c[3]))
    return pdf[:2], txt[:2]


def local_pick(key, period, info):
    out = []
    if period == 'Q2/H1 FY27' and info.get('q2dir'):
        for n in os.listdir(info['q2dir']):
            if n.lower().endswith('.pdf') and re.search(r'result', n, re.I) and not re.search(r'press|presentation', n, re.I):
                out.append(os.path.join(info['q2dir'], n))
    if not out:
        for p in local_pdfs:
            n = os.path.basename(p).replace('_', ' ')
            if pats[key].search(n):
                ctx = p.replace('_', ' ')
                if TOK[period].search(os.path.basename(p)) or TOK[period].search(os.path.basename(os.path.dirname(p))):
                    out.append(p)
    return out[:2]


def to_text(pdf_path, out_txt):
    try:
        raw = subprocess.run(['pdftotext', '-layout', pdf_path, '-'], capture_output=True, timeout=180).stdout
    except Exception:
        return 0, 0
    pages = raw.decode('utf-8', 'replace').split('\f')
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    with open(out_txt, 'w', encoding='utf-8') as f:
        for i, pg in enumerate(pages, 1):
            f.write(f'\n=== PAGE {i} ===\n{pg}')
    return len(pages), sum(len(p.strip()) for p in pages)


for (key, period) in maybe:
    if (key, period) in uni:
        continue
    pdfs, txts = pick(key, period, {})
    if pdfs or txts:
        run = (pdfs + txts)[0][1].split('/')[1]
        uni[(key, period)] = {'where': [f'repo pipeline run runs/{run} (this result was an input; actuals in census.csv)']}
fmap = {}
os.makedirs(os.path.join(work, 'filings'), exist_ok=True)
for (key, period), info in uni.items():
    pdfs, txts = pick(key, period, info)
    loc = local_pick(key, period, info)
    pslug = period.replace('/', '-').replace(' ', '')
    d = os.path.join(work, 'filings', key, pslug)
    entry = {'ticker': tick[key][0], 'name': tick[key][1], 'period': period, 'where': info['where'], 'files': []}
    if pdfs or txts or loc:
        os.makedirs(d, exist_ok=True)
    for sc, path, blob, size, b in pdfs + txts:
        dest = os.path.join(d, os.path.basename(path))
        if not os.path.exists(dest):
            with open(dest, 'wb') as f:
                f.write(subprocess.run(['git', '-C', repo, 'cat-file', 'blob', blob], capture_output=True).stdout)
        rec = {'origin': f'{path} ({b})', 'local_copy': dest, 'kind': 'pdf' if path.lower().endswith('.pdf') else 'text'}
        if rec['kind'] == 'pdf':
            n, chars = to_text(dest, dest + '.txt')
            rec.update(pages=n, text_chars=chars, text_copy=dest + '.txt')
        entry['files'].append(rec)
    for p in loc:
        dest = os.path.join(d, os.path.basename(p))
        n, chars = to_text(p, dest + '.txt')
        entry['files'].append({'origin': p, 'local_copy': p, 'kind': 'pdf', 'pages': n, 'text_chars': chars,
                               'text_copy': dest + '.txt'})
    fmap[f'{key}|{period}'] = entry

json.dump(fmap, open(os.path.join(work, 'filing_map.json'), 'w', encoding='utf-8'), indent=1)
with open(os.path.join(work, 'universe.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['ticker', 'name', 'period', 'where the review lives'])
    for (key, period), info in sorted(uni.items(), key=lambda x: (PERIODS.index(x[0][1]), tick[x[0][0]][0])):
        w.writerow([tick[key][0], tick[key][1], period, ' ; '.join(info['where'])])
c = collections.Counter(p for _, p in uni)
nf = collections.Counter(e['period'] for e in fmap.values() if not e['files'])
print('universe rows', len(uni), dict(c), 'companies', len(set(k for k, _ in uni)))
print('rows without any filing', dict(nf))
