#!/usr/bin/env python3
"""Pull per-company excerpts from local markdown folders (Concall pipeline etc).

Usage:
  python extract_local_excerpts.py <companies.json> <out_dir> <root> [<root> ...]

Walks every .md file under each root (skips files over 3 MB and raw transcript
files), splits into paragraphs, keeps a paragraph for a company when it names
the company and mentions results, guidance, margin, delay, order book or a miss.
Writes <out_dir>/<TICKER>.md, <out_dir>/_files.tsv (every file read) and
<out_dir>/_summary.tsv. Same company matching as extract_session_excerpts.py.
"""
import collections
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_session_excerpts import TOPIC, build_patterns  # noqa: E402

MAX_PER_FILE = 8
MAX_PARA = 1500
SKIP = re.compile(r'transcript|fulltext|node_modules|__pycache__', re.I)


def main():
    companies = json.load(open(sys.argv[1], encoding='utf-8'))
    out_dir = sys.argv[2]
    roots = sys.argv[3:]
    os.makedirs(out_dir, exist_ok=True)
    pats = build_patterns(companies)
    big = re.compile('|'.join('(?:' + p.pattern + ')' for p in pats.values()))
    per = collections.defaultdict(list)
    seen = collections.defaultdict(set)
    flog = open(os.path.join(out_dir, '_files.tsv'), 'w', encoding='utf-8')
    n = 0
    for root in roots:
        for d, _, names in os.walk(root):
            for nm in names:
                if not nm.lower().endswith('.md') or SKIP.search(nm):
                    continue
                p = os.path.join(d, nm)
                try:
                    if os.path.getsize(p) > 3_000_000:
                        continue
                    t = open(p, encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                n += 1
                k = 0
                if big.search(t):
                    cnt = collections.Counter()
                    for para in re.split(r'\n\s*\n', t):
                        para = para.strip()
                        if len(para) < 40 or not TOPIC.search(para):
                            continue
                        for key, pat in pats.items():
                            if cnt[key] < MAX_PER_FILE and pat.search(para):
                                h = hashlib.md5(para.encode('utf-8', 'replace')).hexdigest()
                                if h in seen[key]:
                                    continue
                                seen[key].add(h)
                                cnt[key] += 1
                                per[key].append((p, para[:MAX_PARA]))
                                k += 1
                flog.write(f'{p}\t{k}\n')
    flog.close()
    with open(os.path.join(out_dir, '_summary.tsv'), 'w', encoding='utf-8') as s:
        for key in sorted(companies):
            items = sorted(per.get(key, []))
            s.write(f'{key}\t{len(items)}\t{len(set(i[0] for i in items))}\n')
            if items:
                with open(os.path.join(out_dir, key.upper() + '.md'), 'w', encoding='utf-8') as f:
                    f.write(f'# {key.upper()} - local-file excerpts ({len(items)})\n\n')
                    for p, para in items:
                        f.write(f'## {p}\n\n{para}\n\n')
    print(f'md_files_read={n} companies_with_excerpts={len(per)}')


if __name__ == '__main__':
    main()
