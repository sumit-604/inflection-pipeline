#!/usr/bin/env python3
"""Assemble census.csv, gaps.md and sources.md from the per-company row files.

Usage: python assemble_census.py <scratch_root> <retro_dir> <laptop_name>
  <scratch_root>/out/rows/<key>.json      3 rows per company (see READER_BRIEF.md)
  <scratch_root>/out/companies/<T>.md     excerpts per company
  <scratch_root>/repo/...                 output of export_repo_text.py
  <scratch_root>/sessions, /local         output of the two extractors
Writes into <retro_dir>: census.csv, companies/*.md, gaps.md, sources.md.
No value is computed here except the framework-date flag (first analysis date
before / after 08-Sep-2026) and counts.
"""
import collections
import csv
import datetime
import glob
import json
import os
import re
import shutil
import sys

root, retro, laptop = sys.argv[1], sys.argv[2], sys.argv[3]
NF = 'NOT FOUND'
PERIODS = ['Q4 FY26', 'Q1 FY27', 'Q2/H1 FY27']
COLS = [
    ('ticker', 'ticker'), ('name', 'name'), ('period', 'period'), ('board', 'board (SME or main)'),
    ('reporting', 'reports quarterly or half-yearly'), ('archetype', 'archetype'),
    ('first_analysis_date', 'first analysis date'),
    ('verdict_at_first_analysis', 'verdict at that date'),
    ('framework_date', 'framework date (before or after 08-Sep-2026)'),
    ('projection_basis', 'projection basis'),
    ('base_revenue', 'our base-case revenue'), ('base_margin', 'our base-case margin'),
    ('base_profit', 'our base-case profit'),
    ('mgmt_guidance', 'management guidance at the time (short quote)'),
    ('promised_catalysts', 'promised catalysts with dates'),
    ('actual_revenue', 'actual revenue'), ('actual_margin', 'actual margin'),
    ('actual_profit', 'actual profit'),
    ('result_vs_base', 'result against our base case'),
    ('result_basis', 'basis for result classification'),
    ('classification_caveat', 'classification caveat'),
    ('mgmt_reason', "management's stated reason"),
    ('risk_flagged_before', 'risk flagged before the result (file and line)'),
    ('flagged_by', 'who flagged it'), ('overruled', 'whether it was overruled'),
    ('sources', 'source file for every number'), ('branches', 'run folders and branches'),
    ('notes', 'notes'),
]
VALID = {'BEAT', 'IN LINE', 'MISS', 'NO BASELINE', 'BASELINE NOT COMPARABLE'}


def clean(v):
    if v is None:
        return NF
    if isinstance(v, (list, dict)):
        v = json.dumps(v, ensure_ascii=False)
    v = re.sub(r'\s+', ' ', str(v)).strip()
    return v or NF


def norm_period(p, i):
    p = (p or '').upper()
    if 'Q4' in p and '26' in p:
        return PERIODS[0]
    if 'Q1' in p and '27' in p:
        return PERIODS[1]
    if 'Q2' in p or 'H1' in p:
        return PERIODS[2]
    return PERIODS[i]


companies = json.load(open(os.path.join(root, 'tools', 'companies.json'), encoding='utf-8'))
runinfo = {}
for l in open(os.path.join(root, 'repo', 'run_folders.tsv'), encoding='utf-8'):
    p = l.rstrip('\n').split('\t')
    runinfo[p[0]] = p
man = [l.split('\t') for l in open(os.path.join(root, 'repo', 'export_manifest.tsv'),
                                   encoding='utf-8').read().splitlines()[1:]]
cfile = {m[0]: m for m in man if m[0].startswith('companies/')}

rows, problems, by_key = [], [], {}
for key in sorted(companies):
    f = os.path.join(root, 'out', 'rows', key + '.json')
    if not os.path.exists(f):
        problems.append(f'{key}: no row file')
        continue
    try:
        data = json.load(open(f, encoding='utf-8'))
    except ValueError as e:
        problems.append(f'{key}: bad JSON ({e})')
        continue
    if isinstance(data, dict):
        data = data.get('rows') or list(data.values())
    if len(data) != 3:
        problems.append(f'{key}: {len(data)} rows')
    out = []
    for i, r in enumerate(data[:3]):
        r = {k: clean(v) for k, v in r.items()}
        r['period'] = norm_period(r.get('period'), i)
        d = r.get('first_analysis_date', NF)
        m = re.match(r'(\d{4})-(\d\d)-(\d\d)', d)
        if m:
            dt = datetime.date(int(m[1]), int(m[2]), int(m[3]))
            r['framework_date'] = 'before 08-Sep-2026' if dt < datetime.date(2026, 9, 8) else \
                ('on 08-Sep-2026' if dt == datetime.date(2026, 9, 8) else 'after 08-Sep-2026')
        else:
            r['framework_date'] = NF
        v = r.get('result_vs_base', NF).upper()
        v = 'IN LINE' if v in ('IN-LINE', 'INLINE') else v
        if v not in VALID:
            problems.append(f'{key} {r["period"]}: result_vs_base={v!r}')
        r['result_vs_base'] = v
        cav = []
        if v in ('BEAT', 'IN LINE', 'MISS'):
            if re.search(r'mixed', r.get('result_basis', ''), re.I):
                cav.append('FILE SAYS MIXED; label chosen by reader')
            if r.get('base_revenue', NF).startswith(NF):
                cav.append('NO NUMERIC REVENUE BASE; label rests on a threshold, tripwire or file wording')
            if re.search(r'COMPUTED', r.get('result_basis', '')):
                cav.append('COMPUTED same-period at +/-5%')
        r['classification_caveat'] = '; '.join(cav) if cav else 'none'
        for k, _ in COLS:
            r.setdefault(k, NF)
        out.append(r)
    by_key[key] = out
    rows.extend(out)

os.makedirs(os.path.join(retro, 'companies'), exist_ok=True)
with open(os.path.join(retro, 'census.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow([h for _, h in COLS])
    for r in rows:
        w.writerow([r[k] for k, _ in COLS])
ncomp = 0
for p in glob.glob(os.path.join(root, 'out', 'companies', '*.md')):
    shutil.copy(p, os.path.join(retro, 'companies', os.path.basename(p)))
    ncomp += 1

# ---- gaps.md
g = ['# Gaps', '', f'Laptop: {laptop}. Built {datetime.date.today().isoformat()}. Facts only.', '']
count = collections.Counter(r['result_vs_base'] for r in rows)
no_base, no_act, one_branch, no_cfile = [], [], [], []
for key, rs in by_key.items():
    t = rs[0]['ticker']
    nb = [r['period'] for r in rs if r['result_vs_base'] == 'NO BASELINE' or r['base_revenue'].startswith(NF)]
    na = [r['period'] for r in rs if r['actual_revenue'].startswith(NF)]
    if len(nb) == 3:
        no_base.append(f'- {t} ({key}): no base case for any period')
    elif nb:
        no_base.append(f'- {t} ({key}): no base case for {", ".join(nb)}')
    if na:
        no_act.append(f'- {t} ({key}): no actuals for {", ".join(na)}')
    for run in companies[key]['runs']:
        ri = runinfo.get(run)
        if ri and ri[1] == '1':
            one_branch.append(f'- {t} ({key}): runs/{run} is on one branch only: {ri[3]}')
        elif ri and ri[2] == 'no':
            one_branch.append(f'- {t} ({key}): runs/{run} is on {ri[1]} branches, not on main: {ri[3]}')
    c = cfile.get(f'companies/{key.upper()}.md')
    if not c:
        no_cfile.append(f'- {t} ({key}): no companies/{key.upper()}.md on any branch')
    elif c[6] == 'no':
        one_branch.append(f'- {t} ({key}): companies/{key.upper()}.md not on main; newest copy on {c[2]} ({c[4]} branch(es), {c[3]} version(s))')
g += [f'## 1. No baseline ({len(no_base)} companies)', ''] + no_base + ['']
g += [f'## 2. No actuals in any file ({len(no_act)} companies)', ''] + no_act + ['']
g += [f'## 3. Files on one branch only, or not on main ({len(one_branch)} entries)', ''] + one_branch + ['']
g += [f'## 4. No company memory file ({len(no_cfile)} companies)', ''] + no_cfile + ['']
missing = [k for k in companies if k not in by_key]
g += [f'## 5. Companies with a run folder but no census rows ({len(missing)})', ''] + [f'- {k}' for k in missing] + ['']
if problems:
    g += ['## 6. Row-file problems', ''] + [f'- {p}' for p in problems] + ['']
open(os.path.join(retro, 'gaps.md'), 'w', encoding='utf-8').write('\n'.join(g))

# ---- sources.md
br = [l.split('\t')[0] for l in open(os.path.join(root, 'repo', 'branches.tsv'), encoding='utf-8')]
pref = collections.Counter(b.split('/')[1] for b in br)
sess = open(os.path.join(root, 'sessions', '_sessions.tsv'), encoding='utf-8').read().splitlines()[1:]
sfold = collections.Counter(s.split('\t')[2] for s in sess)
swith = sum(1 for s in sess if s.split('\t')[5] != '0')
dates = sorted(s.split('\t')[0] for s in sess if s.split('\t')[0])
lf = open(os.path.join(root, 'local', '_files.tsv'), encoding='utf-8').read().splitlines()
lwith = sum(1 for l in lf if l.rsplit('\t', 1)[1] != '0')
run_n = len([r for r in runinfo if not r.startswith('_')])
s = ['# Sources', '', f'Laptop: {laptop}. Built {datetime.date.today().isoformat()}.', '',
     '## A. Repo', '',
     f'- Remote branches read (after `git fetch --all`): {len(br)}',
     f'  - run/*: {pref["run"]}; claude/*: {pref["claude"]}; main: {pref["main"]}; other prefixes: '
     f'{len(br) - pref["run"] - pref["claude"] - pref["main"]}',
     f'- Run folders found across all branches: {run_n} '
     f'({sum(1 for r in runinfo.values() if r[2] == "yes" and not r[0].startswith("_"))} on main, '
     f'{sum(1 for r in runinfo.values() if r[2] == "no" and not r[0].startswith("_"))} not on main)',
     f'- Quarterly folders (name ends -q4fy26, -q1fy27, -q2fy27, -h1fy27, -q2cy26): '
     f'{sum(1 for r in runinfo if re.search(r"[qh][0-9][fc]y[0-9]{2}$", r))}',
     f'- Companies (run folders grouped by ticker): {len(companies)}',
     f'- Company memory files (companies/*.md, any branch): {len(cfile)}',
     f'- Text files exported and available to readers: {len(man)} (via `git cat-file`, nothing checked out)',
     '- LESSONS_ARCHIVE.md and LESSONS.md: read (grepped per company)',
     '', '## B. Claude Code session history', '',
     f'- .jsonl session files read: {len(sess)} in {len(sfold)} project folders',
     f'- Date range of sessions: {dates[0] if dates else NF} to {dates[-1] if dates else NF}',
     f'- Session files with at least one kept excerpt: {swith}',
     f'- Companies with session excerpts: {len(glob.glob(os.path.join(root, "sessions", "*.md")))}',
     '- Only user and assistant text was read; tool calls, tool results and thinking were skipped.',
     '', '## C. Local folders', '',
     '- C:\\ConcallPipeline\\Daily Concall Intelligence: found',
     f'  - .md files read: {len(lf)}; with at least one kept excerpt: {lwith}',
     f'  - Companies with local excerpts: {len(glob.glob(os.path.join(root, "local", "*.md")))}',
     '  - PDFs, audio and raw .txt extracts were not read.',
     '- Quarterly Reviewer output folder: NOT FOUND under that name (searched the user profile, '
     'Documents, Desktop, Downloads, OneDrive and C:\\ two levels deep). The folder '
     '"Q2 FY27 Results" inside the Concall folder was read as part of C.',
     '', '## Census', '',
     f'- Rows: {len(rows)} ({len(by_key)} companies x 3 periods)',
     f'- Company excerpt files: {ncomp}',
     '- result_vs_base counts (rows): ' + '; '.join(f'{k} {v}' for k, v in sorted(count.items())),
     '', '## Project folders in session history (files per folder)', '']
s += [f'- {k}: {v}' for k, v in sorted(sfold.items(), key=lambda x: -x[1])]
open(os.path.join(retro, 'sources.md'), 'w', encoding='utf-8').write('\n'.join(s) + '\n')

cc = collections.Counter()
for key, rs in by_key.items():
    for v in set(r['result_vs_base'] for r in rs):
        cc[v] += 1
print('rows', len(rows), 'companies', len(by_key), 'company_md', ncomp)
print('row counts', dict(count))
print('companies with at least one row of each', dict(cc))
print('problems', len(problems))
for p in problems[:40]:
    print(' ', p)
