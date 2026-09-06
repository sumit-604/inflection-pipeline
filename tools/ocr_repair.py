#!/usr/bin/env python3
"""Re-OCR the OCR-garbled pages of a scanned PDF and rebuild a page-marked text file.

Clean pages keep their embedded text layer. Garbled pages are rendered at 300 dpi
in ONE pdftoppm pass (rendering page-by-page re-parses the whole PDF each time and
is what made the first attempt time out), then OCR'd in parallel with tesseract.

A page whose OCR fails KEEPS its embedded text and is marked, so a failed repair
never leaves the corpus worse than it started.

Usage: ocr_repair.py <pdf> <out.txt> [workers] [dpi]
"""
import sys, re, os, subprocess, tempfile, shutil, glob, time
from concurrent.futures import ThreadPoolExecutor

pdf, out = sys.argv[1], sys.argv[2]
workers = int(sys.argv[3]) if len(sys.argv) > 3 else 3
dpi = sys.argv[4] if len(sys.argv) > 4 else '300'

import pypdf
reader = pypdf.PdfReader(pdf)
N = len(reader.pages)

def garble_rate(t):
    if len(t) < 200:
        return 99.0
    weird = len(re.findall(r"[A-Za-z][~!\\|\[\]{}<>@#\$%^&*_](?=[A-Za-z])", t))
    odd = len(re.findall(r"[^\x20-\x7e\n\r‘’“”–—₹ ]", t))
    return (weird + odd) / max(len(t), 1) * 1000

embedded = []
for i in range(N):
    try:
        embedded.append(reader.pages[i].extract_text() or '')
    except Exception:
        embedded.append('')

need = sorted(i for i in range(N) if garble_rate(embedded[i]) > 1.5)
name = os.path.basename(pdf)
sys.stderr.write(f'{name}: {N} pages, {len(need)} need OCR, {workers} workers, {dpi}dpi\n')
sys.stderr.flush()

tmp = tempfile.mkdtemp(prefix='ocr_')
ocr, failed = {}, {}

def render_span(lo, hi):
    """Render pages lo..hi (1-indexed, inclusive) in one pdftoppm pass."""
    subprocess.run(['pdftoppm', '-r', dpi, '-f', str(lo), '-l', str(hi), '-png',
                    pdf, os.path.join(tmp, 'pg')],
                   check=True, capture_output=True, timeout=3600)

def ocr_png(png):
    m = re.search(r'pg-0*(\d+)\.png$', png)
    if not m:
        return
    pno = int(m.group(1)); i = pno - 1
    try:
        r = subprocess.run(['tesseract', png, 'stdout', '--psm', '6'],
                           check=True, capture_output=True, timeout=600)
        ocr[i] = r.stdout.decode('utf-8', 'replace')
    except Exception as e:
        failed[i] = type(e).__name__
    finally:
        try: os.remove(png)
        except OSError: pass
    done = len(ocr) + len(failed)
    if done % 20 == 0:
        sys.stderr.write(f'  ...{done}/{len(need)} ocr\n'); sys.stderr.flush()

# Render in contiguous chunks so pdftoppm parses the document a handful of times,
# not once per page. Chunk size bounds peak disk use.
CHUNK = 40
t0 = time.time()
for c in range(0, len(need), CHUNK):
    span = need[c:c + CHUNK]
    lo, hi = span[0] + 1, span[-1] + 1
    try:
        render_span(lo, hi)
    except Exception as e:
        sys.stderr.write(f'  render {lo}-{hi} failed: {type(e).__name__}\n')
        continue
    wanted = {p + 1 for p in span}
    pngs = [p for p in sorted(glob.glob(os.path.join(tmp, 'pg-*.png')))
            if int(re.search(r'pg-0*(\d+)\.png$', p).group(1)) in wanted]
    # drop rendered pages we did not ask for
    for p in glob.glob(os.path.join(tmp, 'pg-*.png')):
        if p not in pngs:
            try: os.remove(p)
            except OSError: pass
    with ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(ocr_png, pngs))
    sys.stderr.write(f'  chunk {lo}-{hi} done, {len(ocr)} ok {len(failed)} failed, '
                     f'{int(time.time()-t0)}s elapsed\n')
    sys.stderr.flush()

shutil.rmtree(tmp, ignore_errors=True)

hdr = (f'SOURCE: {pdf}\nPAGES: {N}\n'
       f'TEXT LAYER: mixed. [OCR:tesseract] pages were re-OCR\'d at {dpi}dpi because the '
       f'PDF\'s own text layer was corrupt. [OCR:embedded] pages use the PDF\'s own text '
       f'layer, which is sound. [OCR:embedded-CORRUPT] pages needed re-OCR and it failed: '
       f'their text is the corrupt original and NO NUMBER may be taken from them.\n'
       f'RE-OCR OK: {len(ocr)} | RE-OCR FAILED: {len(failed)} | CLEAN EMBEDDED: {N-len(need)}\n')
parts = [hdr]
for i in range(N):
    if i in ocr:
        tag, body = 'tesseract', ocr[i]
    elif i in failed:
        tag, body = 'embedded-CORRUPT', embedded[i]
    else:
        tag, body = 'embedded', embedded[i]
    parts.append(f'\n===== PAGE {i+1} =====\n[OCR:{tag}]\n{body}')
open(out, 'w').write(''.join(parts))
sys.stderr.write(f'wrote {out}: ok={len(ocr)} failed={len(failed)} clean={N-len(need)}\n')
