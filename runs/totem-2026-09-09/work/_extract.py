import glob, os, pathlib
import pypdfium2 as pdfium
from pypdf import PdfReader

scanned = []
for p in sorted(glob.glob('inputs/**/*.pdf', recursive=True)):
    rel = str(pathlib.Path(p).relative_to('inputs'))
    flat = rel.replace(os.sep, '__').replace('/', '__')[:-4] + '.txt'
    out = pathlib.Path('work/text') / flat
    r = PdfReader(p)
    chunks = []
    total = 0
    n = len(r.pages)
    for i, pg in enumerate(r.pages):
        t = pg.extract_text() or ''
        total += len(t.strip())
        chunks.append("\n===== [PAGE %d of %d] %s =====\n%s" % (i + 1, n, rel, t))
    out.write_text("".join(chunks), encoding='utf-8')
    if total < 300:
        scanned.append((p, n))
    print("%9d chars %4dp -> %s" % (total, n, out))

print("\nSCANNED/LOW-TEXT:", scanned)
for p, n in scanned:
    stem = pathlib.Path(p).stem
    d = pathlib.Path('work/pages') / stem
    d.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(p)
    for i in range(len(doc)):
        img = doc[i].render(scale=200 / 72).to_pil()
        f = d / ("page-%02d.png" % (i + 1))
        img.save(f)
        print("rendered", f, img.size)
