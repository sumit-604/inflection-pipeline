#!/usr/bin/env python3
"""Pull per-company excerpts out of Claude Code session history.

Usage:
  python extract_session_excerpts.py <companies.json> <out_dir> [projects_dir]

projects_dir defaults to %USERPROFILE%/.claude/projects (or ~/.claude/projects).

What it does
- Walks every .jsonl under projects_dir (sub-agent transcripts included).
- Reads line by line; keeps only user and assistant TEXT. Tool calls, tool
  results, thinking blocks and system/meta lines are skipped.
- Tags each session with its first timestamp (date) and its folder (cwd).
- Splits text into paragraphs. A paragraph is kept for a company when it names
  the company AND mentions results, guidance, margin, delay, order book or a miss.
- Writes <out_dir>/<TICKER>.md (excerpts with date | folder | session | role)
  and <out_dir>/_sessions.tsv (one row per session file read) and
  <out_dir>/_summary.tsv (excerpt count per company).

companies.json: {"<key>": {"name": "Company Ltd | TICKER" or null,
                           "runs": [...], "aliases": ["optional", ...]}}
Nothing here calls the network.
"""
import collections
import hashlib
import json
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor

TOPIC = re.compile(
    r'\bresults?\b|guidance|guided|margin|\bdelay|deferr|slipp|order[- ]?book|order inflow|'
    r'\bmiss(?:ed|es)?\b|shortfall|\bbeat\b|in[- ]line|base[- ]case|\bEBITDA\b|\bPAT\b|'
    r'\bQ[1-4] ?FY ?\d\d|\bH[12] ?FY ?\d\d', re.I)
MAX_PARA = 1200
MAX_PER_SESSION = 40
STOP_NAME_WORDS = {'ltd', 'limited', 'india', 'industries', 'the', 'and', '&', '&amp;',
                   'technologies', 'company', 'corporation', 'solutions', 'services'}
# short or dictionary-word keys: match only as an upper-case token
COMMON = {'route', 'satin', 'susan', 'totem', 'credo', 'aris', 'ador', 'anup', 'amagi',
          'accord', 'aurum', 'azad', 'entero', 'kross', 'knack', 'sona', 'gargi', 'oswal',
          'kwick', 'vilas', 'tatva', 'avana', 'prizor', 'stallion', 'wework', 'mideast'}


def build_patterns(companies):
    pats = {}
    for key, info in companies.items():
        alts = []
        k = key.replace('-', '')
        tick = k.upper()
        name = (info.get('name') or '')
        if '|' in name:
            name, t2 = [x.strip() for x in name.split('|', 1)]
            t2 = t2.split()[0] if t2 else ''
            if t2 and t2.upper() != tick:
                alts.append(r'\b' + re.escape(t2.upper()) + r'\b')
        if len(k) <= 4 or k in COMMON or k.isdigit():
            alts.append(r'\b' + re.escape(tick) + r'\b')            # case-sensitive
        else:
            alts.append(r'(?i:\b' + re.escape(k) + r'\b)')
        name = re.sub(r'COMPANY MEMORY\s*[—-]\s*', '', name)
        name = re.sub(r'\(.*?\)', '', name).replace('&amp;', '&').strip()
        words = [w for w in re.split(r'\s+', name) if w]
        core = []
        for w in words:
            if w.lower().strip('.,') in STOP_NAME_WORDS and core:
                break
            core.append(w)
            if len(core) == 2:
                break
        if core and len(' '.join(core)) >= 6:
            alts.append(r'(?i:\b' + r'\s+'.join(re.escape(w) for w in core) + r'\b)')
        for a in info.get('aliases', []):
            alts.append(r'(?i:\b' + re.escape(a) + r'\b)')
        pats[key] = re.compile('|'.join(alts))
    return pats


def texts_of(obj):
    msg = obj.get('message') or {}
    c = msg.get('content')
    if isinstance(c, str):
        yield c
    elif isinstance(c, list):
        for part in c:
            if isinstance(part, dict) and part.get('type') == 'text' and part.get('text'):
                yield part['text']


def process(args):
    path, companies = args
    pats = build_patterns(companies)
    big = re.compile('|'.join('(?:' + p.pattern + ')' for p in pats.values()))
    out = collections.defaultdict(list)
    first_ts, cwd, n_msgs = None, None, 0
    try:
        f = open(path, encoding='utf-8', errors='replace')
    except OSError:
        return path, None, None, 0, {}
    with f:
        for line in f:
            if '"type":"user"' not in line and '"type":"assistant"' not in line \
                    and '"type": "user"' not in line and '"type": "assistant"' not in line:
                continue
            try:
                o = json.loads(line)
            except ValueError:
                continue
            typ = o.get('type')
            if typ not in ('user', 'assistant') or o.get('isMeta'):
                continue
            ts = o.get('timestamp')
            if ts and not first_ts:
                first_ts = ts
            if o.get('cwd') and not cwd:
                cwd = o['cwd']
            for t in texts_of(o):
                n_msgs += 1
                if not big.search(t):
                    continue
                for para in re.split(r'\n\s*\n', t):
                    para = para.strip()
                    if len(para) < 40 or not TOPIC.search(para):
                        continue
                    for key, p in pats.items():
                        if p.search(para) and len(out[key]) < MAX_PER_SESSION:
                            out[key].append((ts or '', typ, para[:MAX_PARA]))
    return path, first_ts, cwd, n_msgs, dict(out)


def main():
    companies = json.load(open(sys.argv[1], encoding='utf-8'))
    out_dir = sys.argv[2]
    proj = sys.argv[3] if len(sys.argv) > 3 else os.path.join(
        os.environ.get('USERPROFILE') or os.path.expanduser('~'), '.claude', 'projects')
    os.makedirs(out_dir, exist_ok=True)
    files = []
    for root, _, names in os.walk(proj):
        for n in names:
            if n.endswith('.jsonl'):
                files.append(os.path.join(root, n))
    files.sort()
    per_co = collections.defaultdict(list)
    seen = collections.defaultdict(set)
    sess = open(os.path.join(out_dir, '_sessions.tsv'), 'w', encoding='utf-8')
    sess.write('date\tfolder\tproject_dir\tsession_file\ttext_messages\texcerpts\n')
    with ProcessPoolExecutor(max_workers=max(2, (os.cpu_count() or 4) - 1)) as ex:
        for path, ts, cwd, n, out in ex.map(process, [(p, companies) for p in files], chunksize=8):
            rel = os.path.relpath(path, proj)
            pdir = rel.split(os.sep)[0]
            date = (ts or '')[:10]
            folder = cwd or pdir
            k = 0
            for key, items in out.items():
                for its, role, para in items:
                    h = hashlib.md5(para.encode('utf-8', 'replace')).hexdigest()
                    if h in seen[key]:
                        continue
                    seen[key].add(h)
                    per_co[key].append((its or ts or '', folder, os.path.basename(path), role, para))
                    k += 1
            sess.write(f'{date}\t{folder}\t{pdir}\t{rel}\t{n}\t{k}\n')
    sess.close()
    with open(os.path.join(out_dir, '_summary.tsv'), 'w', encoding='utf-8') as s:
        for key in sorted(companies):
            items = sorted(per_co.get(key, []))
            s.write(f'{key}\t{len(items)}\t{len(set(i[2] for i in items))}\n')
            if not items:
                continue
            with open(os.path.join(out_dir, key.upper() + '.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {key.upper()} - session-history excerpts ({len(items)})\n\n')
                for ts, folder, fn, role, para in items:
                    f.write(f'## {ts[:16]} | {folder} | {fn} | {role}\n\n{para}\n\n')
    print(f'session_files={len(files)} companies_with_excerpts={len(per_co)}')


if __name__ == '__main__':
    main()
