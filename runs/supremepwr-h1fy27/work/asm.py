import re
raw = open('raw.txt', 'rb').read().decode('utf-8', 'replace')
pages = raw.split('\f')[:15]
V = {4: 'v/p4.txt', 5: 'v/p5.txt', 7: 'v/p7.txt', 10: 'v/p10.txt', 11: 'v/p11.txt', 13: 'v/p13.txt'}
N = {6: 'nocr6.txt', 12: 'nocr12.txt', 14: 'ocr14.txt', 15: 'ocr15.txt'}
out = []
for i, p in enumerate(pages, 1):
    out.append('[page %d]' % i)
    if i in (14, 15):
        out.append('(pdftotext yielded zero characters; page is a scanned image)')
    else:
        out += [l.rstrip() for l in p.split('\n')]
    if i in V:
        out.append('[OCR page %d: table transcribed and verified against rendered image at 300 dpi; raw text layer above is OCR-derived and garbled]' % i)
        out += open(V[i], encoding='utf-8').read().split('\n')
    if i in N:
        why = 'rendered because zero-character image page' if i > 13 else 'clean re-read of OCR-derived text layer'
        out.append('[OCR page %d: tesseract psm 6, 300 dpi (250 dpi for p14-15), %s]' % (i, why))
        out += open(N[i], encoding='utf-8', errors='replace').read().split('\n')
body = re.sub('\n{3,}', '\n\n', '\n'.join(out)).split('\n')
hdr = open('hdr.txt', encoding='utf-8').read()
n = len(hdr.split('\n')) - 1 + len(body)
open('../extracted/supremepwr-results-h1fy27-fulltext.md', 'w', encoding='utf-8').write(hdr.replace('LINECOUNT', str(n)) + '\n'.join(body) + '\n')
