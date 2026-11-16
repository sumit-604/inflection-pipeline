#!/usr/bin/env python3
"""Group run folders by company and write companies.json.

Usage: python build_companies.py <export_out_dir> <companies.json>
<export_out_dir> is the folder export_repo_text.py wrote (holds run_folders.tsv, export/).
"""
import collections
import glob
import json
import os
import re
import sys

# run-folder prefix -> company key, where one company has two spellings
SAME = {'ayefin': 'aye', 'divgi': 'divgiitts', 'gocl': 'goclcorp', 'raymondrel': 'raymondrealty',
        'sona': 'sonacoms', 'd-dev': 'deedev', '544555': 'ameenji'}
ALIASES = {
    'lt': ['Larsen & Toubro', 'Larsen and Toubro', 'L&T'], 'route': ['Route Mobile'],
    'satin': ['Satin Creditcare'], 'sonacoms': ['Sona BLW', 'Sona Comstar'],
    'raymondrealty': ['Raymond Realty'], 'goclcorp': ['GOCL'], 'ddevplstik': ['DDev Plastiks', 'DDev Plastik'], 'deedev': ['DEE Development', 'D-Dev'],
    'divgiitts': ['Divgi'], 'aye': ['Aye Finance', 'AYEFIN'],
    '526717': ['HCP Plastene', 'Gopala Polyplast'], '530077': ['Pure Tropic', 'PURETROP', 'Freshtrop'],
    'supremepwr': ['Supreme Power'], 'grwrhitech': ['Garware Hi-Tech', 'Garware Hi Tech'],
    'tinnarubr': ['Tinna Rubber'], 'tejasnet': ['Tejas Networks'], 'fairchemor': ['Fairchem'],
    'dycl': ['Dynamic Cables'], 'paracables': ['Paramount Cables', 'Paramount Communications'],
    'wework': ['WeWork India'], 'ghvinfra': ['GHV Infra'], 'mapmyindia': ['MapmyIndia'],
    'tatacomm': ['Tata Communications'], 'poonawalla': ['Poonawalla Fincorp'],
    'heritgfood': ['Heritage Foods'], 'gmbrew': ['GM Breweries', 'G M Breweries'],
    'eimcoeleco': ['Eimco Elecon'], 'premierpol': ['Premier Polyfilm'],
    'stltech': ['Sterlite Technologies'], 'e2e': ['E2E Networks'], 'ebgng': ['GNG Electronics'],
    '544516': ['Airfloa'], '544332': ['Fabtech Technologies Cleanrooms', 'Fabtech Cleanrooms'],
    'iks': ['Inventurus'], 'sfl': ['Sheela Foam'], 'unimech': ['Unimech Aerospace'],
    'iolcp': ['IOL Chemicals'], 'kissht': ['OnEMI'], 'totem': ['Forbes Precision'],
}


def prefix(r):
    m = re.match(r'^(.*?)-(\d{4}-\d\d-\d\d.*|[qh]\d[fc]y\d\d|agm-.*|corppres-.*)$', r)
    return m.group(1) if m else r


def main():
    root, out = sys.argv[1], sys.argv[2]
    runs = [l.split('\t')[0] for l in open(os.path.join(root, 'run_folders.tsv'), encoding='utf-8')]
    groups = collections.defaultdict(list)
    for r in runs:
        if r.startswith('_'):
            continue
        p = prefix(r)
        groups[SAME.get(p, p)].append(r)
    res = {}
    for p, rs in sorted(groups.items()):
        nm = None
        for r in rs:
            f = os.path.join(root, 'export', 'runs', r, 'manifest.yaml')
            if os.path.exists(f):
                t = open(f, encoding='utf-8', errors='replace').read()
                m = re.search(r'^company:\s*(.+)$', t, re.M)
                if m:
                    nm = m.group(1).split('#')[0].strip().strip('"\'')
                    m = re.search(r'^ticker:\s*(\S+)', t, re.M)
                    if m:
                        nm += ' | ' + m.group(1).strip('"\'')
                    break
        if not nm:
            c = os.path.join(root, 'export', 'companies', p.upper() + '.md')
            if os.path.exists(c):
                nm = open(c, encoding='utf-8', errors='replace').readline().strip('# \n')
        res[p] = {'runs': rs, 'name': nm}
        if p in ALIASES:
            res[p]['aliases'] = ALIASES[p]
    json.dump(res, open(out, 'w', encoding='utf-8'), indent=1)
    print(len(res), 'companies')


if __name__ == '__main__':
    main()
