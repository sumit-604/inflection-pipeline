#!/usr/bin/env python3
"""Export analysis text from every remote branch without checking anything out.

Usage:  python export_repo_text.py <repo_path> <out_dir>

Reads `git ls-tree -r -l` for every origin/* branch, keeps text files under
runs/<folder>/ and companies/, plus LESSONS*.md, and writes each one with
`git cat-file blob`. Where the same path has different contents on different
branches, the copy from the branch with the newest commit is written and the
others are counted in the manifest (column n_variants).

Outputs in <out_dir>:
  export/...                 the files, same relative paths as the repo
  export_manifest.tsv        path, blob, chosen_branch, n_variants, n_branches, size, on_main
  branches.tsv               branch, last commit date
  run_folders.tsv            run folder, n_branches, on_main, branches (first 6)
"""
import collections
import os
import re
import subprocess
import sys

TEXT_EXT = ('.md', '.yaml', '.yml', '.txt', '.csv', '.json')
SKIP = re.compile(
    r'/inputs/|-tmp/|/_working/|page-images|/work/extracted/|/work/txt/|'
    r'fulltext|/extract_[^/]*\.txt$|/raw\.txt$|/_text/|\.gitkeep$')
MAX_BYTES = 400_000


def git(repo, *args, binary=False):
    out = subprocess.run(['git', '-C', repo, *args], capture_output=True, check=True).stdout
    return out if binary else out.decode('utf-8', 'replace')


def main():
    repo, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    refs = [l.split('\t') for l in git(
        repo, 'for-each-ref', '--format=%(refname:short)\t%(committerdate:iso-strict)',
        'refs/remotes/origin').splitlines()]
    refs = [(b, d) for b, d in refs if b not in ('origin/HEAD', 'origin')]
    bdate = dict(refs)
    with open(os.path.join(out, 'branches.tsv'), 'w', encoding='utf-8') as f:
        for b, d in sorted(refs):
            f.write(f'{b}\t{d}\n')

    variants = collections.defaultdict(lambda: collections.defaultdict(list))  # path -> blob -> [branch]
    size = {}
    runs = collections.defaultdict(set)
    for b, _ in refs:
        try:
            txt = git(repo, 'ls-tree', '-r', '-l', b, '--', 'runs', 'companies',
                      'LESSONS_ARCHIVE.md', 'LESSONS.md')
        except subprocess.CalledProcessError:
            continue
        for line in txt.splitlines():
            meta, path = line.split('\t', 1)
            _, typ, blob, sz = meta.split()
            if typ != 'blob':
                continue
            if path.startswith('runs/'):
                parts = path.split('/')
                if len(parts) > 2:
                    runs[parts[1]].add(b)
            if not path.lower().endswith(TEXT_EXT) or SKIP.search(path):
                continue
            if sz == '-' or int(sz) > MAX_BYTES:
                continue
            variants[path][blob].append(b)
            size[blob] = int(sz)

    with open(os.path.join(out, 'run_folders.tsv'), 'w', encoding='utf-8') as f:
        for r in sorted(runs):
            bs = sorted(runs[r])
            f.write(f"{r}\t{len(bs)}\t{'yes' if 'origin/main' in bs else 'no'}\t{';'.join(bs[:6])}\n")

    man = open(os.path.join(out, 'export_manifest.tsv'), 'w', encoding='utf-8')
    man.write('path\tblob\tchosen_branch\tn_variants\tn_branches\tsize\ton_main\n')
    n = 0
    for path in sorted(variants):
        blobs = variants[path]
        best_blob, best_branch = max(
            ((bl, max(brs, key=lambda x: bdate[x])) for bl, brs in blobs.items()),
            key=lambda t: bdate[t[1]])
        all_br = [b for brs in blobs.values() for b in brs]
        dest = os.path.join(out, 'export', *path.split('/'))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if not os.path.exists(dest):
            with open(dest, 'wb') as f:
                f.write(git(repo, 'cat-file', 'blob', best_blob, binary=True))
        man.write(f"{path}\t{best_blob[:10]}\t{best_branch}\t{len(blobs)}\t{len(all_br)}\t"
                  f"{size[best_blob]}\t{'yes' if 'origin/main' in all_br else 'no'}\n")
        n += 1
    man.close()
    print(f'branches={len(refs)} run_folders={len(runs)} files_exported={n}')


if __name__ == '__main__':
    main()
