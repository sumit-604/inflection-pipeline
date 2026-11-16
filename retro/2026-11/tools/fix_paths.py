#!/usr/bin/env python3
"""Rewrite working-folder paths in census.csv and companies/*.md to repo paths.

Usage: python fix_paths.py <retro_dir> <reader_brief_source.md>
Readers cite excerpt files by their working-folder path; this turns those into
retro/2026-11/excerpts/... and repo-relative runs/... paths.
"""
import glob
import re
import sys

R = sys.argv[1]
brief = open(sys.argv[2], encoding='utf-8').read()
brief = re.sub(r'C:\\Users\\[^\\]+\\AppData\\Local\\Temp\\claude\\[0-9a-f]+\\[0-9a-f-]+\\scratchpad',
               '<SCRATCH: any empty working folder>', brief)
open(R + '/tools/READER_BRIEF.md', 'w', encoding='utf-8').write(brief)

pat = re.compile(r'(?:C:[\\/]+Users[\\/]+[^\\/]+[\\/]+AppData[\\/]+Local[\\/]+Temp[\\/]+claude[\\/]+'
                 r'[0-9a-f]+[\\/]+[0-9a-f-]+[\\/]+scratchpad|\bSCRATCH|\.\.\.[\\/]scratchpad|\bscratchpad)[\\/]+')
n = 0
files = [R + '/census.csv'] + glob.glob(R + '/companies/*.md')
for f in files:
    enc = 'utf-8-sig' if f.endswith('.csv') else 'utf-8'
    t = open(f, encoding=enc, newline='').read()
    u = pat.sub('retro/2026-11/excerpts/', t)
    u = re.sub(r'retro/2026-11/excerpts/repo[\\/]+export[\\/]+', '', u)
    u = re.sub(r'retro/2026-11/excerpts/out[\\/]+', 'retro/2026-11/', u)
    u = re.sub(r'excerpts/(?:local_old|local)[\\/]+', 'excerpts/local/', u)
    u = re.sub(r'excerpts/sessions[\\/]+', 'excerpts/sessions/', u)
    u = re.sub(r'(?<![/\w])local_old[\\/]+', 'retro/2026-11/excerpts/local/', u)
    if u != t:
        n += 1
        open(f, 'w', encoding=enc, newline='').write(u)
print('files rewritten', n)
left = 0
for f in files:
    t = open(f, encoding='utf-8', errors='replace').read()
    left += len(re.findall(r'scratchpad|AppData|local_old', t))
print('leftover working-folder refs', left)
