import fitz

SRC = "runs/sugslloyd-q1fy27/inputs/sugslloyd_q1fy27_results.pdf"
OUT = "runs/sugslloyd-q1fy27/work/extract_results_sugslloyd_q1fy27.txt"

doc = fitz.open(SRC)

def layout_page(page, scale=0.12):
    """Reconstruct pdftotext -layout style output using word bboxes."""
    words = page.get_text("words")  # x0,y0,x1,y1,word,block,line,wordno
    if not words:
        return ""
    # group into rows by y0 (rounded); tolerance grouping
    words.sort(key=lambda w: (round(w[1]/3.0), w[0]))
    rows = {}
    for w in words:
        key = round(w[1]/3.0)
        rows.setdefault(key, []).append(w)
    out_lines = []
    for key in sorted(rows):
        rw = sorted(rows[key], key=lambda w: w[0])
        line = ""
        for w in rw:
            col = int(w[0]*scale)
            if col < len(line):
                col = len(line)+1
            if col > len(line):
                line += " "*(col-len(line))
            line += w[4]
        out_lines.append(line.rstrip())
    return "\n".join(out_lines)

parts = []
parts.append("=== A1 EXTRACTION HEADER ===")
parts.append("source_filename: sugslloyd_q1fy27_results.pdf")
parts.append("doctype: results")
parts.append(f"page_count_pdfinfo: {doc.page_count}")
# placeholders filled after
header_idx = len(parts)
body = []
low_pages = []
for i, page in enumerate(doc):
    txt = layout_page(page)
    if len(txt.strip()) < 100:
        low_pages.append(i+1)
    body.append(f"[page {i+1}]")
    body.append(txt)
    if i < doc.page_count-1:
        body.append("\f")

body_text = "\n".join(body)
formfeed = body_text.count("\f")

parts.append(f"formfeed_count: {formfeed}")
parts.append("line_count: TBD")
parts.append("unit_convention: Lakhs")
parts.append("conversion_factor_to_cr: Lakhs -> x0.01")
parts.append(f"ocr_pages: {'none' if not low_pages else low_pages}")
parts.append(f"page_coverage: {'100%' if not low_pages else 'GAP: pages '+str(low_pages)+' under 100 chars'}")
parts.append("detected_quarter: Q1 FY27 (quarter ended 30 June 2026)")
parts.append("extraction_date: 2026-07-29")
parts.append("extraction_tool: PyMuPDF 1.28 layout reconstruction (pdftotext unavailable in env; PDF fully text-based, no OCR needed)")
parts.append("=== END HEADER ===")

full = "\n".join(parts) + "\n" + body_text + "\n"
line_count = full.count("\n")
full = full.replace("line_count: TBD", f"line_count: {line_count}")

with open(OUT,"w") as f:
    f.write(full)

print("wrote", OUT)
print("pages:", doc.page_count, "formfeeds:", formfeed, "lines:", line_count, "low_pages:", low_pages)
