import re, sys, json
base = r"C:\Users\SUMIT SHARMA\repos\inflection-pipeline\.claude\worktrees\quarterly-cybertech-q2fy27-920b89\runs\cybertech-q2fy27"
raw_b = open(base + r"\work\raw.txt", "rb").read()
ff = raw_b.count(b"\f")
raw = raw_b.decode("utf-8", "replace").replace("\f", "").rstrip("\n").split("\n")
body = open(base + r"\work\body_p2_10.txt", encoding="utf-8").read().rstrip("\n").split("\n")
src = "Cybertech_Q2FY27_Results_Reg33_BoardOutcome_22Oct2026.pdf"
fh = base + r"\extracted\cybertech-results-q2fy27-fulltext.md"
sp = base + r"\extracted\cybertech-results-q2fy27-structured.md"

def header(total):
    return [
        "=== A1 EXTRACTION HEADER ===",
        "source_filename: " + src,
        "doctype: results",
        "page_count_pdfinfo: 10",
        "formfeed_count: %d   # form-feed characters in pdftotext output (grep -c counts 1 line because pages 2-10 are empty)" % ff,
        "line_count: %d   # lines in this file including header" % total,
        "unit_convention: Lakhs   # financial statements pages 3-5, 7-9 print (Rs. In Lakhs); page 1 and pages 2, 6, 10 carry no unit",
        "conversion_factor_to_cr: Lakhs -> x0.01 (100 Lakhs = 1 Crore); extracted text NOT converted",
        "text_layer_present: yes   # pdffonts lists embedded CIDFont/MyriadPro fonts, but only page 1 carries text",
        "extraction_mode: text-only for page 1; pages 2-10 rendered (zero-character data-bearing pages, see rendered_pages)",
        "render_candidates: [p2 (zero chars; consolidated limited review report image), p3 (zero chars; consolidated P&L table image), p4 (zero chars; consolidated balance sheet image), p5 (zero chars; consolidated cash flow image), p6 (zero chars; standalone limited review report image), p7 (zero chars; standalone P&L table image), p8 (zero chars; standalone balance sheet image), p9 (zero chars; standalone cash flow image), p10 (zero chars; notes to results image)]",
        "rendered_pages: [p2, p3, p4, p5, p6, p7, p8, p9, p10 - each data-bearing (financial statements, auditor report or notes) with no text layer; Print-To-PDF producer rasterised them; pdftoppm -png -r 200 then tesseract --psm 6; tesseract output on ruled tables (p3, p4) was garbled/incomplete so every rendered page was read visually from the 200 dpi image and transcribed as 'label | value | value' rows; values on pages 3-5 and 7-9 come from the image read, not raw tesseract output]",
        "transcription_note: pages 2-10 text is a transcription of the rendered images, labelled [OCR page N]; unlabelled subtotal rows in cash flows are marked [unlabelled]; bracketed tags like [current] / [non-current] disambiguate repeated captions and are not in the source",
        "page_coverage: 100%",
        "detected_quarter: Q2 FY27 (quarter and half year ended 30-Sep-2026)",
        "extraction_date: 2026-10-23",
        "=== END HEADER ===",
    ]

hl = len(header(0))
lines = header(0) + ["[page 1]"] + raw + body
total = len(lines)
lines = header(total) + ["[page 1]"] + raw + body
assert len(lines) == total
open(fh, "w", encoding="utf-8").write("\n".join(lines) + "\n")

# page tracking
page_of = {}
cur = 0
for i, l in enumerate(lines, 1):
    m = re.match(r"^\[page (\d+)\]$", l)
    if m:
        cur = int(m.group(1))
    page_of[i] = cur

def find(pg, sub, nth=1):
    c = 0
    for i, l in enumerate(lines, 1):
        if page_of[i] == pg and sub in l:
            c += 1
            if c == nth:
                return i
    raise SystemExit("NOT FOUND p%d: %s" % (pg, sub))

scope = {3: "consolidated", 4: "consolidated", 5: "consolidated", 7: "standalone", 8: "standalone", 9: "standalone"}
rows = {"NUMBER": [], "ENTITY": [], "FORWARD": [], "DATE": [], "QUALIFIER": []}

def add(t, pg, ln, val, ctx):
    rows[t].append((pg, ln, val, ctx))

# NUMBER: table rows
cols = []
colpage = {}
for i, l in enumerate(lines, 1):
    pg = page_of[i]
    if l.startswith("COLUMNS:"):
        cols = [c.strip() for c in l[len("COLUMNS:"):].split(" | ")]
        colpage[pg] = (i, cols)
        continue
    if pg in scope and " | " in l and not l.startswith("["):
        parts = [p.strip() for p in l.split(" | ")]
        label = parts[0]
        vals = parts[1:]
        # pad (blank cells)
        for j, v in enumerate(vals):
            if v == "":
                continue
            colname = cols[j] if j < len(cols) else "col%d" % j
            colname_short = re.sub(r" \((Un)?[Aa]udited\)", "", colname)
            colname_short = re.sub(r" \[date printed.*", "", colname_short)
            ctx = "%s %s, %s" % (scope[pg], label[:70], colname_short)
            val = v
            if v == "-":
                ctx += " [ZERO_STANDING]"
            add("NUMBER", pg, i, val, ctx)
        continue
    # DATE: column headers and signatures
for pg, (ln, cl) in colpage.items():
    for c in cl:
        add("DATE", pg, ln, c, "column period header, %s" % scope[pg])
for i, l in enumerate(lines, 1):
    if l.startswith("Digital signature:"):
        add("DATE", page_of[i], i, l.split("Baradiya ")[1], "digital signature timestamp, Rajendra Parasmal Baradiya")

# NUMBER: manual
man = [
    (1, "Scrip Code: 532173", "532173", "BSE scrip code"),
    (1, "07:20 P.M.", "07:20 P.M.", "board meeting commencement time"),
    (1, "08:30 P.M.", "08:30 P.M.", "board meeting conclusion time"),
    (1, "BM 03/2026-27", "BM 03/2026-27", "board meeting serial number"),
    (1, "Regulation 33", "Regulation 33", "SEBI LODR regulation cited"),
    (1, "Regulations, 2015", "2015", "year of SEBI LODR Regulations"),
    (1, "Membership No.: A35587", "A35587", "company secretary membership number"),
    (1, "+91 226983-9200", "+91 226983-9200", "company telephone, page 1"),
    (1, "Thane 400604", "400604", "registered office pin code, page 1"),
    (1, "Plot No. B-63/64/65", "B-63/64/65", "registered office plot, page 1"),
    (1, "Road # 21/34", "21/34", "registered office road number"),
    (2, "SRE) 2410", "2410", "SRE standard cited by auditor, consolidated review"),
    (2, "Section 133", "133", "Companies Act section cited, consolidated review"),
    (2, "Regulation 33", "Regulation 33", "SEBI LODR regulation, consolidated review"),
    (2, "Act, 2013", "2013", "Companies Act year, consolidated review"),
    (2, "Membership No. 044101", "044101", "auditor partner membership number"),
    (2, "301051E / E300284", "301051E / E300284", "auditor firm registration numbers"),
    (2, "UDIN: 26044101KYIDLJ7365", "26044101KYIDLJ7365", "UDIN, consolidated review report"),
    (2, "December 27, 2023", "December 27, 2023", "Lodha LLP conversion effective date"),
    (3, "Face value: Rs.10", "Rs.10", "face value per share, consolidated P&L"),
    (3, "400 604", "400 604", "registered office pin code, page 3"),
    (6, "SRE) 2410", "2410", "SRE standard cited by auditor, standalone review"),
    (6, "Section 133", "133", "Companies Act section cited, standalone review"),
    (6, "Regulation 33", "Regulation 33", "SEBI LODR regulation, standalone review"),
    (6, "Membership No. 044101", "044101", "auditor partner membership number, standalone review"),
    (6, "UDIN: 26044101XLYUZC6704", "26044101XLYUZC6704", "UDIN, standalone review report"),
    (7, "Face value: Rs.10", "Rs.10", "face value per share, standalone P&L"),
    (10, "1,00,000 equity shares of Rs. 10 each, pursuant", "1,00,000", "equity shares allotted on ESOP exercise, quarter ended 30-Sep-2026"),
    (10, "1,00,000 equity shares of Rs. 10 each, pursuant", "Rs. 10", "face value per share, Note 3 allotment"),
    (10, "Rs. 10,00,000", "Rs. 10,00,000", "equity share capital as stated in Note 3"),
    (10, "comprising of 1,00,000 equity shares", "1,00,000", "number of shares comprising capital as stated in Note 3"),
    (10, "consolidating 29 existing labour laws", "29", "labour laws consolidated by the four Labour Codes"),
    (10, "four Labour Codes", "four", "Labour Codes notified"),
    (10, "IND AS110", "IND AS110", "accounting standard for consolidation, Note 2"),
    (10, "IND AS 108", "IND AS 108", "accounting standard for segments, Note 4"),
    (10, "DIN : 05350841", "05350841", "executive director DIN, page 10"),
]
for pg, sub, val, ctx in man:
    add("NUMBER", pg, find(pg, sub), val, ctx)
# DIN on each page
for pg in (3, 4, 5, 7, 8, 9):
    add("NUMBER", pg, find(pg, "DIN: 05350841"), "05350841", "executive director DIN, page %d" % pg)
# unit numbers (note: Tel etc. kept as above)

# ENTITY
ent = [
    (1, "CYBERTECH SYSTEMS AND SOFTWARE LIMITED", "CyberTech Systems and Software Limited", "reporting company / signatory"),
    (1, "BSE Limited", "BSE Limited", "stock exchange addressee"),
    (1, "National Stock Exchange of India Ltd.", "National Stock Exchange of India Ltd.", "stock exchange addressee"),
    (1, "Symbol: CYBERTECH", "CYBERTECH", "NSE symbol"),
    (1, "CIN L72100MH1995PLC084788", "L72100MH1995PLC084788", "company CIN"),
    (1, "GSTIN 27AAACC1905B1ZE", "27AAACC1905B1ZE", "company GSTIN"),
    (1, "SEBI (Listing Obligations", "SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015", "regulation cited"),
    (1, "Audit Committee", "Audit Committee", "reviewed and recommended results"),
    (1, "Board of Directors", "Board of Directors", "approved results"),
    (1, "Sarita Leelaramani", "Sarita Leelaramani", "Company Secretary and Compliance Officer"),
    (1, "LEELA RAMANI", "Leela Ramani Ramani Sarita Kumar (digital signature text)", "digital signatory text"),
    (1, "https://investors.cybertech.com/", "https://investors.cybertech.com/", "company investor website"),
    (1, "cssl.investors@cybertech.com", "cssl.investors@cybertech.com", "company investor email"),
    (2, "LODHA & CO LLP", "Lodha & Co LLP", "statutory auditor / reviewer"),
    (2, "R P Baradiya", "R P Baradiya (Rajendra Parasmal Baradiya)", "audit partner signing review report"),
    (2, "i. CyberTech Systems and Software Inc. USA", "CyberTech Systems and Software Inc. USA", "wholly owned subsidiary reviewed"),
    (2, "ii. Spatialitics LLC, USA", "Spatialitics LLC, USA", "wholly owned subsidiary reviewed"),
    (2, "iii. CyberTech Systems and Software Canada Inc.", "CyberTech Systems and Software Canada Inc.", "wholly owned subsidiary reviewed"),
    (2, "Institute of Chartered Accountants of India", "Institute of Chartered Accountants of India", "issuer of SRE 2410"),
    (2, "Companies Act, 2013", "Companies Act, 2013", "statute cited"),
    (2, "Indian Accounting Standard 34", "Indian Accounting Standard 34 (Ind AS 34)", "interim reporting standard"),
    (2, "Fort, Mumbai- 400 001", "6, Karim Chambers, 40, Ambalal Doshi Marg, Fort, Mumbai 400 001", "Lodha & Co Mumbai office address"),
    (2, "Regd. Office : 19, Esplanade", "Lodha & Co regd office Kolkata 700069", "auditor regd office"),
    (2, "Offices: Kolkata", "Kolkata, Mumbai, New Delhi, Chennai, Hyderabad, Jaipur", "auditor office cities"),
    (3, "Ramasubramanian Sankaran", "Ramasubramanian Sankaran, Executive Director, DIN 05350841", "signatory of results"),
    (3, "Company seal", "CyberTech Systems and Software Ltd, Thane (seal)", "company seal on results"),
    (6, "LODHA & CO LLP", "Lodha & Co LLP", "statutory auditor, standalone review"),
    (6, "R P Baradiya", "R P Baradiya (Rajendra Parasmal Baradiya)", "audit partner, standalone review"),
    (6, "Companies Act, 2013", "Companies Act, 2013", "statute cited, standalone review"),
    (6, "Indian Accounting Standard 34", "Indian Accounting Standard 34 (Ind AS 34)", "interim reporting standard, standalone review"),
    (9, "Investment in a wholly owned subsidiary", "wholly owned subsidiary (unnamed in this line)", "standalone investing outflow counterparty"),
    (10, "CyberTech Systems and Software Inc. USA, along", "CyberTech Systems and Software Inc. USA", "subsidiary consolidated, Note 2"),
    (10, "CyberTech Systems and Software, Canada Inc.", "CyberTech Systems and Software, Canada Inc.", "step-down subsidiary of the USA entity, Note 2 wording"),
    (10, "Spatialitics LLC, wholly owned", "Spatialitics LLC", "subsidiary consolidated, Note 2"),
    (10, "Employee Stock Option Scheme (ESOP)", "Employee Stock Option Scheme (ESOP)", "scheme under which shares allotted"),
    (10, "'Information Technology Services'", "Information Technology Services", "single reportable business segment"),
    (10, "Government of India", "Government of India", "notified four Labour Codes"),
    (10, "Code on Wages, 2019", "Code on Wages, 2019", "Labour Code"),
    (10, "Industrial Relations Code, 2020", "Industrial Relations Code, 2020", "Labour Code"),
    (10, "Code on Social Security, 2020", "Code on Social Security, 2020", "Labour Code"),
    (10, "Occupational Safety, Health and Working Conditions Code, 2020", "Occupational Safety, Health and Working Conditions Code, 2020", "Labour Code"),
    (10, "Ministry of Labour & Employment", "Ministry of Labour & Employment", "published draft Central Rules and FAQs"),
    (10, "S. Ramasubramanian", "S. Ramasubramanian, Executive Director, DIN 05350841", "signatory for the Board, page 10"),
    (10, "Place : Thane", "Thane", "place of signing"),
    (5, "Treasury bills", "Treasury bills", "instrument in fair valuation gain line"),
    (5, "mutual funds", "mutual funds", "investment instrument in cash flow lines"),
]
for pg, sub, val, ctx in ent:
    add("ENTITY", pg, find(pg, sub), val, ctx)

# FORWARD
fw = [
    (10, "with effect from April 1, 2026", "The Company has considered to restructure the compensation of its employees with effect from April 1, 2026", "Note 5 compensation restructuring from 1-Apr-2026"),
    (10, "The Company continues to monitor the finalization", "The Company continues to monitor the finalization of Central / State Rules ... and would provide appropriate accounting effect on the basis of such developments as needed", "Note 5 future accounting effect of Labour Codes"),
    (10, "published draft Central Rules and FAQs", "The Ministry of Labour & Employment published draft Central Rules and FAQs to enable the assessment of the financial impact", "Note 5 Labour Code rules still in draft"),
]
for pg, sub, val, ctx in fw:
    add("FORWARD", pg, find(pg, sub), val, ctx)

# DATE manual
dt = [
    (1, "Date: October 22, 2026", "October 22, 2026", "date of cover letter"),
    (1, "Thursday, October 22, 2026", "Thursday, October 22, 2026", "board meeting held"),
    (1, "quarter and half year ended September 30, 2026", "September 30, 2026", "quarter and half year end"),
    (1, "Date: 2026.10.22 20:45:14", "2026.10.22 20:45:14 +05'30'", "digital signature, company secretary"),
    (2, "quarter and half year ended September 30, 2026", "September 30, 2026", "period reviewed, consolidated"),
    (2, "Date: October 22, 2026", "October 22, 2026", "consolidated review report date"),
    (2, "December 27, 2023", "December 27, 2023", "Lodha LLP conversion date"),
    (3, "Unaudited Consolidated Financial Results for the Quarter", "Quarter and Half year ended September 30, 2026", "consolidated results period"),
    (6, "quarter and half year ended September 30, 2026", "September 30, 2026", "period reviewed, standalone"),
    (6, "Date: October 22, 2026", "October 22, 2026", "standalone review report date"),
    (7, "Unaudited Standalone Financial Results for the Quarter", "Quarter and Half Year ended September 30, 2026", "standalone results period"),
    (10, "held on October 22, 2026", "October 22, 2026", "Note 1 board and audit committee meetings"),
    (10, "During the quarter ended September 30, 2026", "quarter ended September 30, 2026", "Note 3 ESOP allotment period"),
    (10, "On November 21, 2025", "November 21, 2025", "Note 5 Labour Codes notified"),
    (10, "with effect from April 1, 2026", "April 1, 2026", "Note 5 compensation restructure effective date"),
    (10, "year ended March 31, 2026", "March 31, 2026", "Note 5 year of incremental impact presented"),
    (10, "Date  : October 22, 2026", "October 22, 2026", "signing date of results"),
    (3, "Code on Wages", "x", "x"),
] if False else [
    (1, "Date: October 22, 2026", "October 22, 2026", "date of cover letter"),
    (1, "Thursday, October 22, 2026", "Thursday, October 22, 2026", "board meeting held"),
    (1, "quarter and half year ended September 30, 2026", "September 30, 2026", "quarter and half year end"),
    (1, "Date: 2026.10.22 20:45:14", "2026.10.22 20:45:14 +05'30'", "digital signature, company secretary"),
    (2, "quarter and half year ended September 30, 2026", "September 30, 2026", "period reviewed, consolidated"),
    (2, "Date: October 22, 2026", "October 22, 2026", "consolidated review report date"),
    (2, "December 27, 2023", "December 27, 2023", "Lodha LLP conversion date"),
    (3, "Unaudited Consolidated Financial Results for the Quarter", "Quarter and Half year ended September 30, 2026", "consolidated results period"),
    (6, "quarter and half year ended September 30, 2026", "September 30, 2026", "period reviewed, standalone"),
    (6, "Date: October 22, 2026", "October 22, 2026", "standalone review report date"),
    (6, "December 27, 2023", "December 27, 2023", "Lodha LLP conversion date, page 6"),
    (7, "Unaudited Standalone Financial Results for the Quarter", "Quarter and Half Year ended September 30, 2026", "standalone results period"),
    (10, "held on October 22, 2026", "October 22, 2026", "Note 1 board and audit committee meetings"),
    (10, "During the quarter ended September 30, 2026", "quarter ended September 30, 2026", "Note 3 ESOP allotment period"),
    (10, "On November 21, 2025", "November 21, 2025", "Note 5 Labour Codes notified"),
    (10, "with effect from April 1, 2026", "April 1, 2026", "Note 5 compensation restructure effective date"),
    (10, "year ended March 31, 2026", "March 31, 2026", "Note 5 year of incremental impact presented"),
    (10, "Date  : October 22, 2026", "October 22, 2026", "signing date of results"),
    (10, "Code on Wages, 2019", "2019", "year of Code on Wages"),
    (10, "Industrial Relations Code, 2020", "2020", "year of Industrial Relations Code"),
    (10, "Code on Social Security, 2020", "2020", "year of Code on Social Security"),
    (10, "Working Conditions Code, 2020", "2020", "year of OSH Code"),
]
for pg, sub, val, ctx in dt:
    add("DATE", pg, find(pg, sub), val, ctx)

# QUALIFIER
ql = [
    (1, "Un-audited Financial Results", "Un-audited Financial Results (Standalone and Consolidated) along with the Limited Review Report", "results status unaudited, limited review"),
    (1, "Audit Committee pursuant", "duly reviewed and recommended by the Audit Committee pursuant to Regulation 33", "results reviewed by Audit Committee"),
    (1, "Encl.: a/a", "Encl.: a/a", "enclosures as annexed"),
    (1, "Digitally signed by LEELA", "Digitally signed by LEELA SARITA KUMAR", "digital signature on cover letter"),
    (2, "moderate assurance", "obtain moderate assurance as to whether the financial statements are free of material misstatement", "review scope, consolidated"),
    (2, "does not enable us to obtain assurance", "A review is substantially less in scope than an audit ... Accordingly, we do not express an audit opinion", "review is not an audit, consolidated"),
    (2, "wholly owned subsidiaries and the same are reviewed by us", "The Statement includes the results of the following wholly owned subsidiaries and the same are reviewed by us", "consolidation perimeter reviewed"),
    (2, "nothing has come to our attention", "nothing has come to our attention that causes us to believe ... contains any material misstatement", "unmodified conclusion, consolidated"),
    (3, "(Rs. In Lakhs)", "(Rs. In Lakhs)", "unit, consolidated results"),
    (3, "Basic (Not annualised)", "Basic (Not annualised)", "EPS not annualised, consolidated"),
    (3, "Diluted (Not annualised)", "Diluted (Not annualised)", "EPS not annualised, consolidated"),
    (3, "COLUMNS:", "Unaudited for all quarter and half-year columns; Audited for Year Ended 31-03-2026", "audit status of columns, consolidated P&L"),
    (3, "Total Income (1+2)", "Total Income (1+2) includes Other income", "Total Income defined as revenue plus other income"),
    (3, "Profit before Tax (3-4)", "Profit before Tax (3-4)", "PBT is after other income"),
    (4, "(Rs. in lakhs)", "(Rs. in lakhs)", "unit, consolidated balance sheet"),
    (4, "COLUMNS:", "30-09-2026 Unaudited; 31-03-2026 Audited", "audit status of columns, consolidated balance sheet"),
    (5, "(Rs. in lakhs)", "(Rs. in lakhs)", "unit, consolidated cash flow"),
    (5, "COLUMNS:", "Half year ended 30-09-2026 and 31-09-2025 both Unaudited; prior-year column header prints 31-09-2025", "audit status and header date typo, consolidated cash flow"),
    (5, "Purchase of property, plant & equipment", "Including capital work-in-progress and capital advances", "capex line definition, consolidated"),
    (5, "Proceeds from issue of equity shares under ESOP", "including securities premium", "ESOP proceeds definition, consolidated"),
    (5, "Buyback of equity shares", "including transaction costs", "buyback outflow definition, consolidated"),
    (5, "Increase in trade payables", "Increase in trade payables, other financial liabilities and other liabilities", "working capital line scope, consolidated"),
    (6, "moderate assurance", "obtain moderate assurance as to whether the financial statements are free of material misstatement", "review scope, standalone"),
    (6, "does not enable us to obtain assurance", "A review is substantially less in scope than an audit ... Accordingly, we do not express an audit opinion", "review is not an audit, standalone"),
    (6, "nothing has come to our attention", "nothing has come to our attention that causes us to believe ... contains any material misstatement", "unmodified conclusion, standalone"),
    (7, "(Rs. In Lakhs)", "(Rs. In Lakhs)", "unit, standalone results"),
    (7, "Basic (Not annualised)", "Basic (Not annualised)", "EPS not annualised, standalone"),
    (7, "Diluted (Not annualised)", "Diluted (Not annualised)", "EPS not annualised, standalone"),
    (7, "COLUMNS:", "Unaudited for all quarter and half-year columns; Audited for Year Ended 31-03-2026", "audit status of columns, standalone P&L"),
    (7, "Total Income (1+2)", "Total Income (1+2) includes Other income", "Total Income defined as revenue plus other income, standalone"),
    (8, "(Rs. in lakhs)", "(Rs. in lakhs)", "unit, standalone balance sheet"),
    (8, "COLUMNS:", "30-09-2026 Unaudited; 31-03-2026 Audited", "audit status of columns, standalone balance sheet"),
    (9, "(Rs. in lakhs)", "(Rs. in lakhs)", "unit, standalone cash flow"),
    (9, "COLUMNS:", "Half year ended 30-09-2026 and 30-09-2025 both Unaudited", "audit status of columns, standalone cash flow"),
    (9, "Purchase of property, plant & equipment", "Including capital work-in-progress and capital advances", "capex line definition, standalone"),
    (9, "Proceeds from issue of equity shares under ESOP", "including securities premium", "ESOP proceeds definition, standalone"),
    (9, "Buyback of equity shares", "including transaction costs", "buyback outflow definition, standalone"),
    (9, "Investment in a wholly owned subsidiary", "Investment in a wholly owned subsidiary (standalone only; absent from consolidated cash flow)", "standalone investing line, no subsidiary named"),
    (10, "Notes :", "Notes :", "notes header"),
    (10, "1 The above results", "Note 1: results reviewed by Audit Committee and approved by Board on October 22, 2026", "Note 1"),
    (10, "2 The accounts of", "Note 2: accounts of CyberTech Systems and Software Inc. USA, with its subsidiary Canada Inc. and Spatialitics LLC, wholly owned subsidiaries, consolidated under IND AS110", "Note 2 consolidation basis"),
    (10, "3 During the quarter", "Note 3: 1,00,000 equity shares of Rs. 10 each allotted on ESOP exercise; capital stated as Rs. 10,00,000 comprising 1,00,000 shares", "Note 3 ESOP allotment"),
    (10, "4 The Group has only single", "Note 4: Group has only single reportable business segment 'Information Technology Services' per IND AS 108", "Note 4 segment"),
    (10, "5 On November 21, 2025", "Note 5: Labour Codes notified 21-Nov-2025; compensation restructure from 1-Apr-2026; incremental impact presented under Employee Benefits Expense for year ended 31-Mar-2026", "Note 5 Labour Codes"),
    (10, "The Company continues to monitor", "Note 5 second paragraph: Company continues to monitor finalization of Central / State Rules and would provide accounting effect as needed", "Note 5 continuation"),
    (10, "6 The previous period", "Note 6: previous period's / year's figures regrouped/re-classified wherever required", "Note 6 regrouping"),
]
for pg, sub, val, ctx in ql:
    add("QUALIFIER", pg, find(pg, sub), val, ctx)

# write structured
out = []
n = 0
body_rows = []
counts = {}
for t in ["NUMBER", "ENTITY", "FORWARD", "DATE", "QUALIFIER"]:
    counts[t] = len(rows[t])
    body_rows.append("")
    body_rows.append("## %s (%d rows)" % (t, len(rows[t])))
    for pg, ln, val, ctx in rows[t]:
        n += 1
        body_rows.append("R%03d | page %d | line %d | %s | %s | %s" % (n, pg, ln, t, val, ctx))
hdr = [
    "# A1 STRUCTURED EXTRACTION: CYBERTECH q2fy27 results (Reg 33 board outcome 22-Oct-2026)",
    "source fulltext: " + fh,
    "line numbers refer to the fulltext file as written (header block counted)",
    "ID range: R001-R%03d" % n,
    "counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d | total %d" % (counts["NUMBER"], counts["ENTITY"], counts["FORWARD"], counts["DATE"], counts["QUALIFIER"], n),
    "unit: Rs Lakhs on pages 3-5 and 7-9 (x0.01 to Rs Crores); values verbatim, not converted",
    "row format: R### | page N | line L | TYPE | verbatim value | short context",
    "NUMBER atomicity: one row per (metric x period); '-' cells carry [ZERO_STANDING]; blank cells (Other equity, quarter/half columns) are not values and carry no row",
    "page 1 had a text layer; pages 2-10 were rendered and transcribed from the image (see fulltext header)",
]
open(sp, "w", encoding="utf-8").write("\n".join(hdr + body_rows) + "\n")
print(json.dumps({"total_lines": total, "ff": ff, "counts": counts, "n": n}))
