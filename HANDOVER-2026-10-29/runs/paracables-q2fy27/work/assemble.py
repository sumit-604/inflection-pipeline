import pickle, re
W = "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-paracables-q2fy27-a220cd/runs/paracables-q2fy27/"
out = pickle.load(open(W + "work/pages.pkl", "rb"))
PATCH = [
 ("| (ll) Deferred Tax (1.20) (0.07) 0.35 (1.27) 0.36 | 0.55", "(II) Deferred Tax (1.20) (0.07) 0.35 (1.27) 0.38 0.55"),
 (" PQOe", ""), (" PACT V3", ""), (" AoNMOSS", ""), (" NGS", ""),
 ("Equity share 97.67 7", "Equity share 97.67 -"),
 ("Convertibles Equity share 97.67 7", "Convertibles Equity share 97.67 -"),
 ("Net Proceeds from Issue of Equity Shares and Convertibles Equity share 97.67 7", "Net Proceeds from Issue of Equity Shares and Convertibles Equity share 97.67 -"),
 ("XIll | Profit for the period (IX + XII) 24.24 19.70 13.26 43.94 32.26 60.24", "XIII | Profit for the period (IX + XII) 24.24 19.70 13.26 43.94 32.26 60.24"),
]
body = []
for p, lines in out:
    body.append("[page %d]" % p)
    for ln in lines:
        for a, b in PATCH:
            if a in ln:
                ln = ln.replace(a, b)
        ln = ln.replace(" | ", " ").replace("| ", "") if p in (3, 4, 5, 9, 10, 11, 13) and False else ln
        body.append(ln)
    body.append("\f")
CORR = """\
ocr_corrections_log (page | line item | OCR value -> image value; image-verified via Read on pages 3,4,5,9,10,11,13 and notes tables on 6,12):
  C01 p3 | Depreciation and amortization, half year 30.09.2026 | 8.66 -> 8.86
  C02 p3 | Deferred Tax, half year 30.09.2025 | 0.36 -> 0.38
  C03 p3 | OCI income tax item (II), quarter 30.09.2025 | 0.04 -> 0.01
  C04 p3 | EPS XX diluted, half year 30.09.2025 | 1.08 -> 1.06
  C05 p3 | Profit IX/year ended 31.03.2026 | 60,24 -> 60.24 (comma for decimal)
  C06 p3 | Depreciation, quarter 30.09.2026 | 4,43 -> 4.43 (comma for decimal)
  C07 p3 | EPS XX rows (stamp-obscured, OCR garbled) | restored from image: 0.74 0.64 0.44 1.38 1.06 1.97 (basic and diluted)
  C08 p3 | Exceptional items row | OCR symbols -> dashes (nil) x6
  C09 p4 | Current Tax Liability (Net), 30.09.2026 | 44.59 -> 11.59
  C10 p4 | Trade payables MSME, 31.03.2026 | 10.674 -> 10.67
  C11 p4 | Totals rows blank in OCR | restored: Total Non-Current Assets 346.02/317.05; Total Current Assets 902.57/811.60; Total Assets 1,248.59/1,128.65; Total Equity 920.01/778.07; Total NCL 32.31/14.81; Total Equity and Liabilities 1,248.59/1,128.65
  C12 p5 | Net cash from investing (B), HY 30.09.2026 | (64.99) -> (61.99)
  C13 p5 | Purchase of Investments (Mutual Fund), HY 30.09.2026 | 35.00 -> (35.00) (sign lost)
  C14 p5 | Operating profit before WC changes, Cash gen., tax paid, net cash from ops, financing total, net increase, row values blank/garbled in OCR | restored from image: 77.23/53.52; (4.67)/(1.62); (31.89)/(60.02); 99.45/63.02; 5.57/(19.51)
  C15 p5 | Equity proceeds HY 30.09.2025 | 7 -> - (nil)
  C16 p9 | Revenue from operations and Other income, year ended 31.03.2026 | blank in OCR -> 1,913.35 and 51.10
  C17 p9 | Profit for the period XIII, half year 30.09.2025 | 31.76 -> 31.75
  C18 p9 | EPS (2) Diluted, half year 30.09.2025 | 1.044 -> 1.04
  C19 p9 | EPS XX (2) Diluted row (stamp-obscured, garbled) | restored 0.74 0.64 0.43 1.38 1.04 1.96
  C20 p9 | Total Income, quarter 30.06.2026 | §32.49 -> 532.49
  C21 p9 | Exceptional items, year ended 31.03.2026 | OCR 0.03 kept; dashes restored for other columns
  C22 p10 | Other Equity, 31.03.2026 | 717,03 -> 717.03 (comma for decimal)
  C23 p10 | Provisions (current), 31.03.2026 | 055 -> 0.55
  C24 p10 | Current Tax Liability (Net), 30.09.2026 | 11,59 -> 11.59 (comma for decimal)
  C25 p10 | Trade payables MSME, 31.03.2026 | blank -> 10.67
  C26 p10 | Total Current Assets, Total Assets, Total Equity and Liabilities rows | blank in OCR -> 902.57/811.60; 1,248.59/1,128.65; 1,248.59/1,128.65
  C27 p11 | Net cash from operating (A), HY 30.09.2025 | (57.98) -> (57.96)
  C28 p11 | Purchase of Investments (Mutual Fund), HY 30.09.2026 | 35.00 -> (35.00) (sign lost)
  C29 p11 | Operating profit before WC changes, tax paid, financing total, opening cash HY25 blank in OCR | restored 77.23/53.71; (4.67)/(2.40); 99.45/61.41; 4.76/23.37
  C30 p13 | Profit After tax, half year 30.09.2025 | 341.75 -> 31.75
  C31 p13 | Total Segment Assets, half year 30.09.2025 | 1,007.66 -> 1,007.86
  C32 p13 | Less Inter-segment Revenue HY30.09.2025 | 3,53 -> 3.53 (comma for decimal)
  C33 p13 | Tax expenses, year ended 31.03.2026 | 21,07 -> 21.07 (comma for decimal)
  C34 p13 | Wire and Cables segment liabilities, 30.09.2025 columns | 243,93 -> 243.93 (comma for decimal)
  C35 p13 | Column header row missing in OCR | restored six period headers
  C36 p6 | Un-utilized Amount (use of proceeds table) | blank in OCR -> 26.66
  C37 p12 | Un-utilized Amount (use of proceeds table) | blank in OCR -> 26.66
  C38 p5 | Interest/Operating table label alignment (OCR placed "Cash generated from operation" separators) | row values re-bound to line items per image
ocr_corrections_count: 38 (each C-entry = one logged correction; C07/C08/C11/C14/C26/C29 each restore a group of values)
"""
def header(n):
    return """=== A1 EXTRACTION HEADER ===
source_filename: Paramount_Q2FY27_Results.pdf
doctype: results
page_count_pdfinfo: 13
formfeed_count: 13
line_count: %d
unit_convention: Crores (statement pages state "Rs. in Crores"; per-share data in Rs)
conversion_factor_to_cr: x1 (Crores -> Crores; no conversion)
text_layer_present: no (pdffonts shows only a third-party hidden OCR layer, DTBDOV+GlyphLessFont by Online2PDF.com, over 13 scanned pages; orchestrator compared page 3 to image and found row-label offsets and digit errors, so the layer is treated as untrusted; hidden-layer pdftotext output is NOT in this file)
extraction_mode: scan-ocr
render_candidates: none (every page rendered; scan)
rendered_pages: [1,2,3,4,5,6,7,8,9,10,11,12,13] (300 dpi pdftoppm, tesseract --psm 6; all pages OCR'd because the text layer is unreliable; statement pages 3,4,5,9,10,11,13 and notes-number blocks on 6,12 checked against page image)
page_coverage: 100%% (13 of 13 pages present; each marked [page N])
detected_quarter: Q2 FY27 (quarter and half year ended 30-Sep-2026)
extraction_date: 2026-10-28
note: OCR text on non-statement pages (1,2,6,7,8,12 narrative) is raw tesseract output; stamp/signature noise is residual and unaltered except where stated. [OCR page N] label applies to every page body.
%s=== END HEADER ===
""" % (n, CORR)
b = "\n".join(body)
n = len(header(0).split("\n")) + len(b.split("\n")) - 1
for _ in range(3):
    h = header(n)
    full = h + b
    n = len(full.split("\n"))
open(W + "extracted/paracables-results-q2fy27-fulltext.md", "w", encoding="utf-8").write(full)
print(n, full.count("\f"))
