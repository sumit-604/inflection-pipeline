#!/usr/bin/env python3
"""Write one reading packet per company and group companies into batches.

Usage: python make_packets.py <scratch_root>
Expects <scratch_root>/repo (export), /tools/companies.json, /sessions, /local.
Writes <scratch_root>/packets/<KEY>.txt and <scratch_root>/batches.json.
"""
import json
import os
import re
import sys

root = sys.argv[1]
repo = os.path.join(root, 'repo')
exp = os.path.join(repo, 'export')
companies = json.load(open(os.path.join(root, 'tools', 'companies.json'), encoding='utf-8'))
tiers = {t['key']: t for t in json.load(open(os.path.join(repo, 'tiers.json')))}
runinfo = {}
for l in open(os.path.join(repo, 'run_folders.tsv'), encoding='utf-8'):
    p = l.rstrip('\n').split('\t')
    runinfo[p[0]] = p
man = {}
for l in open(os.path.join(repo, 'export_manifest.tsv'), encoding='utf-8').read().splitlines()[1:]:
    p = l.split('\t')
    man[p[0]] = p

P1 = re.compile(
    r'outputs/final/|/reports/(01-gate0|05-concall|10-|11-valuation|13-|14-thesis|15-devil|12b-)|'
    r'B13-synthesis|notion-payload|operator-brief|notion[-_]thesis|notion[-_]brief|/review_|'
    r'/narrative_|RUNLOG|run-log|step1-business-brief|manifest\.yaml|/audit_[^/]*\.md$', re.I)

os.makedirs(os.path.join(root, 'packets'), exist_ok=True)
for key, info in companies.items():
    lines = [f'COMPANY KEY: {key}', f'NAME (from manifest, may be null): {info.get("name")}',
             f'EXPORT ROOT (repo-relative paths below live under it): {exp}', '']
    cf = f'companies/{key.upper()}.md'
    if cf in man:
        lines.append(f'COMPANY MEMORY FILE: {cf}  ({man[cf][5]} bytes; branch {man[cf][2]}; on_main={man[cf][6]})')
    else:
        lines.append('COMPANY MEMORY FILE: NOT FOUND on any branch')
    for r in info['runs']:
        ri = runinfo.get(r, [r, '?', '?', '?'])
        lines.append('')
        lines.append(f'RUN FOLDER runs/{r}/  on {ri[1]} branch(es); on_main={ri[2]}; branches: {ri[3]}')
        fs = sorted(p for p in man if p.startswith(f'runs/{r}/'))
        p1 = [p for p in fs if P1.search(p)]
        p2 = [p for p in fs if not P1.search(p)]
        lines.append('  PRIORITY FILES (read; for files over 60 KB read the top 150 lines then grep):')
        for p in p1:
            lines.append(f'    {p}  ({man[p][5]} bytes)')
        lines.append(f'  OTHER FILES ({len(p2)}; grep only when a field is still missing):')
        for p in p2[:60]:
            lines.append(f'    {p}  ({man[p][5]} bytes)')
    s = os.path.join(root, 'sessions', key.upper() + '.md')
    lines.append('')
    lines.append(f'SESSION-HISTORY EXCERPTS: {s if os.path.exists(s) else "NONE"}')
    s = os.path.join(root, 'local', key.upper() + '.md')
    s2 = os.path.join(root, 'local_old', key.upper() + '.md')
    lines.append(f'LOCAL-FOLDER EXCERPTS (Concall pipeline): {s} (if that file does not exist yet, use {s2}; if neither exists: NONE)')
    lines.append(f'LESSONS FILES (grep for the ticker/name): {os.path.join(exp, "LESSONS_ARCHIVE.md")} ; {os.path.join(exp, "LESSONS.md")}')
    open(os.path.join(root, 'packets', key + '.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')


def tier(k):
    t = tiers[k]
    nq = len(t['q'].split(',')) if t['q'] else 0
    if t['val'] and nq:
        return 1
    if t['val']:
        return 2
    if nq and len(companies[k]['runs']) > nq:
        return 3
    if nq:
        return 4
    return 5


size = {1: 3, 2: 4, 3: 4, 4: 8, 5: 8}
batches = []
for t in (1, 2, 3, 4, 5):
    ks = sorted(k for k in companies if tier(k) == t)
    for i in range(0, len(ks), size[t]):
        batches.append({'id': f'T{t}-{i // size[t] + 1:02d}', 'tier': t, 'keys': ks[i:i + size[t]]})
json.dump(batches, open(os.path.join(root, 'batches.json'), 'w'), indent=1)
print(len(batches), 'batches;', {t: sum(1 for b in batches if b['tier'] == t) for t in size})
