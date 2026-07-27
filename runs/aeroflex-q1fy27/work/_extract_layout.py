import sys, fitz
inp, outp = sys.argv[1], sys.argv[2]
d = fitz.open(inp)
lines_out = []
for i, pg in enumerate(d, start=1):
    lines_out.append(f"[page {i}]")
    # layout-preserving: sort blocks top-to-bottom, left-to-right; keep intra-block text
    txt = pg.get_text("text", sort=True)
    for ln in txt.split("\n"):
        lines_out.append(ln.rstrip())
    lines_out.append("\f")  # formfeed page break marker like pdftotext
open(outp, "w").write("\n".join(lines_out))
print("pages", d.page_count, "outlines", len(lines_out))
