#!/usr/bin/env python3
"""Re-OCR the corrupt pages of a scanned PDF and rebuild a page-marked text file.

Some filings ship a PDF whose embedded text layer is bad OCR: digits dropped or
merged, letters swapped ("sllare data", "0,aJ595"). No number from such a page can
be trusted. This re-renders those pages and OCRs them again with tesseract.

RESUMABLE. Each page's OCR text is cached under <outdir>/ocrcache/<pdf stem>/, and
the run stops when its time budget is spent. Re-running continues from the cache,
so a long document is repaired across several bounded invocations and a killed run
never loses completed pages. The page analysis is cached too, since extracting the
embedded text of every page is the largest fixed cost of a resumable run.

A page whose OCR fails keeps its embedded text and is tagged [OCR:embedded-CORRUPT],
so a failed repair never leaves the corpus worse than it started, and a downstream
reader can see the page is unreliable.

Usage: ocr_repair.py <pdf> <out.txt> [workers] [dpi] [budget_seconds]
Exit 0 = nothing left to do. Exit 10 = budget spent, pages remain, run again.
"""
import sys, re, os, json, glob, time, shutil, tempfile, subprocess
from concurrent.futures import ThreadPoolExecutor

pdf, out = sys.argv[1], sys.argv[2]
workers = int(sys.argv[3]) if len(sys.argv) > 3 else 3
dpi     = sys.argv[4] if len(sys.argv) > 4 else '200'
budget  = float(sys.argv[5]) if len(sys.argv) > 5 else 400.0
# Optional 6th arg: page spec like "174-224,232-239". Those pages are repaired
# first, so a run that never finishes still repairs the pages that matter most.
priority = sys.argv[6] if len(sys.argv) > 6 else ''

import pypdf
reader = pypdf.PdfReader(pdf)
N = len(reader.pages)
stem  = os.path.splitext(os.path.basename(pdf))[0]
cache = os.path.join(os.path.dirname(out) or '.', 'ocrcache', stem)
os.makedirs(cache, exist_ok=True)

def cpath(i):
    return os.path.join(cache, f'p{i+1:04d}.txt')

def garble_rate(t):
    """Corrupt-OCR signature: punctuation wedged inside words, non-printable bytes."""
    if len(t) < 200:
        return 99.0
    weird = len(re.findall(r"[A-Za-z][~!\\|\[\]{}<>@#\$%^&*_](?=[A-Za-z])", t))
    odd   = len(re.findall(r"[^\x20-\x7e\n\r‘’“”–—₹ ]", t))
    return (weird + odd) / max(len(t), 1) * 1000

anpath = os.path.join(cache, '_analysis.json')
if os.path.exists(anpath):
    embedded = json.load(open(anpath, encoding='utf-8'))
else:
    embedded = []
    for i in range(N):
        try:
            embedded.append(reader.pages[i].extract_text() or '')
        except Exception:
            embedded.append('')
    json.dump(embedded, open(anpath, 'w', encoding='utf-8'))

need = [i for i in range(N) if garble_rate(embedded[i]) > 1.5]
todo = [i for i in need if not os.path.exists(cpath(i))]

def parse_spec(spec):
    want = set()
    for part in filter(None, (x.strip() for x in spec.split(','))):
        if '-' in part:
            a, b = part.split('-', 1)
            want.update(range(int(a) - 1, int(b)))
        else:
            want.add(int(part) - 1)
    return want

if priority:
    pri = parse_spec(priority)
    todo = [i for i in todo if i in pri] + [i for i in todo if i not in pri]
sys.stderr.write(f'{os.path.basename(pdf)}: {N}pp | corrupt {len(need)} | '
                 f'cached {len(need)-len(todo)} | todo {len(todo)} | '
                 f'{dpi}dpi | budget {int(budget)}s\n')
sys.stderr.flush()

def spans(pages, max_gap=2, max_span=40):
    """Group page indices into contiguous render spans.

    Corrupt pages are usually sparse (13, 17, 24, ... then a 174-189 run). Rendering
    from the first to the last page of a fixed-size batch would render every page in
    between and discard most of them: a 30-page batch spanning pages 13 to 189
    renders 177 pages to use 30. A new span starts whenever the gap to the next
    needed page exceeds max_gap, so wasted rendering is bounded.
    """
    out, cur = [], []
    for i in pages:
        if cur and (i - cur[-1] > max_gap or i - cur[0] >= max_span):
            out.append(cur); cur = []
        cur.append(i)
    if cur:
        out.append(cur)
    return out

t0  = time.time()
tmp = tempfile.mkdtemp(prefix='ocr_')

def ocr_png(png):
    pno = int(re.search(r'pg-0*(\d+)\.png$', png).group(1))
    try:
        r = subprocess.run(['tesseract', png, 'stdout', '--psm', '6'],
                           check=True, capture_output=True, timeout=300)
        open(cpath(pno - 1), 'w').write(r.stdout.decode('utf-8', 'replace'))
    except Exception as e:
        sys.stderr.write(f'  page {pno} ocr failed: {type(e).__name__}\n')
    finally:
        try: os.remove(png)
        except OSError: pass

try:
    for span in spans(todo):
        if time.time() - t0 > budget:
            sys.stderr.write('  budget spent, stopping\n')
            break
        lo, hi = span[0] + 1, span[-1] + 1
        try:
            subprocess.run(['pdftoppm', '-r', dpi, '-f', str(lo), '-l', str(hi),
                            '-png', pdf, os.path.join(tmp, 'pg')],
                           check=True, capture_output=True, timeout=600)
        except Exception as e:
            sys.stderr.write(f'  render {lo}-{hi} failed: {type(e).__name__}\n')
            continue
        wanted = {p + 1 for p in span}
        keep, drop = [], []
        for f in glob.glob(os.path.join(tmp, 'pg-*.png')):
            (keep if int(re.search(r'pg-0*(\d+)\.png$', f).group(1)) in wanted
                  else drop).append(f)
        for f in drop:
            try: os.remove(f)
            except OSError: pass
        with ThreadPoolExecutor(max_workers=workers) as ex:
            list(ex.map(ocr_png, sorted(keep)))
        done = sum(1 for i in need if os.path.exists(cpath(i)))
        sys.stderr.write(f'  span {lo}-{hi} ({len(span)}pp) | cached {done}/{len(need)}'
                         f' | {int(time.time()-t0)}s\n')
        sys.stderr.flush()
finally:
    shutil.rmtree(tmp, ignore_errors=True)

ok      = {i for i in need if os.path.exists(cpath(i))}
corrupt = [i for i in need if i not in ok]
hdr = (f'SOURCE: {pdf}\nPAGES: {N}\n'
       f"TEXT LAYER: mixed. [OCR:tesseract] pages were re-OCR'd at {dpi}dpi because the "
       f"PDF's own text layer was corrupt. [OCR:embedded] pages use the PDF's own text "
       f"layer, which is sound. [OCR:embedded-CORRUPT] pages needed re-OCR and it has not "
       f"succeeded: their text is the corrupt original and NO NUMBER may be taken from "
       f"them.\n"
       f'RE-OCR OK: {len(ok)} | STILL CORRUPT: {len(corrupt)} | '
       f'CLEAN EMBEDDED: {N-len(need)}\n')
parts = [hdr]
for i in range(N):
    if i in ok:
        tag, body = 'tesseract', open(cpath(i), encoding='utf-8', errors='replace').read()
    elif i in corrupt:
        tag, body = 'embedded-CORRUPT', embedded[i]
    else:
        tag, body = 'embedded', embedded[i]
    parts.append(f'\n===== PAGE {i+1} =====\n[OCR:{tag}]\n{body}')
open(out, 'w').write(''.join(parts))
sys.stderr.write(f'wrote {out}: ok={len(ok)} still_corrupt={len(corrupt)} '
                 f'clean={N-len(need)}\n')
sys.exit(10 if corrupt else 0)
