#!/usr/bin/env python3
"""Re-OCR the OCR-garbled pages of a scanned PDF and rebuild a page-marked text file.

Clean pages keep their embedded text layer; garbled pages are rendered at 300 dpi
and re-OCR'd with tesseract. Each page header records which source was used, so a
downstream anchor can be traced.

Usage: ocr_repair.py <pdf> <out.txt> [workers]
"""
import sys, re, os, subprocess, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor

pdf, out = sys.argv[1], sys.argv[2]
workers = int(sys.argv[3]) if len(sys.argv) > 3 else 4

import pypdf
reader = pypdf.PdfReader(pdf)
N = len(reader.pages)

def garble_rate(t):
    if len(t) < 200:
        return 99.0  # too little text: treat as needing OCR
    weird = len(re.findall(r"[A-Za-z][~!\\|\[\]{}<>@#\$%^&*_](?=[A-Za-z])", t))
    odd = len(re.findall(r"[^\x20-\x7e\n\r‘’“”–—₹ ]", t))
    return (weird + odd) / max(len(t), 1) * 1000

embedded = []
for i in range(N):
    try:
        t = reader.pages[i].extract_text() or ''
    except Exception:
        t = ''
    embedded.append(t)

need = [i for i in range(N) if garble_rate(embedded[i]) > 1.5]
sys.stderr.write(f'{os.path.basename(pdf)}: {N} pages, {len(need)} need OCR\n')

tmp = tempfile.mkdtemp(prefix='ocr_')
results = {}

def do_page(i):
    pno = i + 1
    stem = os.path.join(tmp, f'p{pno}')
    try:
        subprocess.run(['pdftoppm', '-r', '300', '-f', str(pno), '-l', str(pno),
                        '-png', '-singlefile', pdf, stem],
                       check=True, capture_output=True, timeout=300)
        r = subprocess.run(['tesseract', stem + '.png', 'stdout', '--psm', '6'],
                           check=True, capture_output=True, timeout=300)
        txt = r.stdout.decode('utf-8', 'replace')
    except Exception as e:
        txt = f'[OCR FAILED on page {pno}: {type(e).__name__}]'
    finally:
        for ext in ('.png',):
            try: os.remove(stem + ext)
            except OSError: pass
    results[i] = txt
    if len(results) % 25 == 0:
        sys.stderr.write(f'  ...{len(results)}/{len(need)}\n'); sys.stderr.flush()

with ThreadPoolExecutor(max_workers=workers) as ex:
    list(ex.map(do_page, need))

shutil.rmtree(tmp, ignore_errors=True)

parts = [f'SOURCE: {pdf}\nPAGES: {N}\n'
         f'TEXT LAYER: mixed. Pages marked [OCR:tesseract] were re-OCR\'d at 300dpi '
         f'because the embedded text layer was corrupt. Pages marked [OCR:embedded] '
         f'use the PDF\'s own text layer.\n'
         f'RE-OCR\'d PAGES: {len(need)} of {N}\n']
for i in range(N):
    src = 'tesseract' if i in results else 'embedded'
    body = results.get(i, embedded[i])
    parts.append(f'\n===== PAGE {i+1} =====\n[OCR:{src}]\n{body}')
open(out, 'w').write(''.join(parts))
sys.stderr.write(f'wrote {out}\n')
