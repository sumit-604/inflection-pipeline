import json, os, re, sys
root = sys.argv[1]  # repo dir containing export/ and export_manifest.tsv
c = json.load(open(sys.argv[2]))
files = {}
for l in open(os.path.join(root, 'export_manifest.tsv'), encoding='utf-8').read().splitlines()[1:]:
    p = l.split('\t')
    if p[0].startswith('runs/'):
        files.setdefault(p[0].split('/')[1], []).append((p[0], int(p[5]), p[2], p[3], p[6]))
rows = []
for k, v in sorted(c.items()):
    val = th = dv = 0
    qs = []
    for r in v['runs']:
        fs = [f[0] for f in files.get(r, [])]
        if any(re.search(r'11-valuation|B11-valuation', f) for f in fs): val = 1
        if any(re.search(r'14-thesis', f) for f in fs): th = 1
        if any(re.search(r'15-devil', f) for f in fs): dv = 1
        if re.search(r'[qh]\d[fc]y\d\d$', r): qs.append(r.split('-')[-1])
    cf = os.path.exists(os.path.join(root, 'export', 'companies', k.upper() + '.md'))
    rows.append((k, val, th, dv, cf, ','.join(qs), len(v['runs'])))
print('total', len(rows), 'val', sum(r[1] for r in rows), 'thesis', sum(r[2] for r in rows),
      'devil', sum(r[3] for r in rows), 'companyfile', sum(r[4] for r in rows))
print('VAL+Q:', [r[0] + ':' + r[5] for r in rows if r[1] and r[5]])
print('VAL only:', [r[0] for r in rows if r[1] and not r[5]])
print('PIPE(noval)+Q:', [r[0] + ':' + r[5] for r in rows if not r[1] and r[5] and r[6] > len(r[5].split(','))])
print('Q only:', len([r for r in rows if r[5] and r[6] == len(r[5].split(','))]))
print('PIPE only no val:', [r[0] for r in rows if not r[1] and not r[5]])
json.dump([dict(key=r[0], val=r[1], thesis=r[2], devil=r[3], cfile=r[4], q=r[5]) for r in rows],
          open(os.path.join(root, 'tiers.json'), 'w'), indent=0)
