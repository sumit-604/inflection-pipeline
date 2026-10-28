import re
W = "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-paracables-q2fy27-a220cd/runs/paracables-q2fy27/"
FT = W + "extracted/paracables-results-q2fy27-fulltext.md"
lines = open(FT, encoding="utf-8").read().split("\n")
page_of = {}
cur = 0
for i, ln in enumerate(lines, 1):
    m = re.match(r"^\[page (\d+)\]", ln)
    if m:
        cur = int(m.group(1))
    page_of[i] = cur

def find(sub, page, nth=1):
    c = 0
    for i, ln in enumerate(lines, 1):
        if page_of[i] == page and sub in ln:
            c += 1
            if c == nth:
                return i
    raise SystemExit("NOT FOUND p%d: %s" % (page, sub))

rows = {"NUMBER": [], "ENTITY": [], "FORWARD": [], "DATE": [], "QUALIFIER": []}
def add(t, page, line, val, ctx):
    rows[t].append((page, line, val, ctx))

PER6 = ["quarter 30.09.2026", "quarter 30.06.2026", "quarter 30.09.2025", "half year 30.09.2026", "half year 30.09.2025", "year ended 31.03.2026"]
PER2 = ["as at 30.09.2026", "as at 31.03.2026"]
PERC = ["half year ended 30.09.2026", "half year ended 30.09.2025"]
cfg = {3: (6, PER6, "standalone P&L"), 9: (6, PER6, "consolidated P&L"), 13: (6, PER6, "consolidated segment"),
       4: (2, PER2, "standalone balance sheet"), 10: (2, PER2, "consolidated balance sheet"),
       5: (2, PERC, "standalone cash flow"), 11: (2, PERC, "consolidated cash flow")}
tok = re.compile(r"^\(?[\d,]+\.\d{2}\)?$|^-$")
unmatched = []
for i, ln in enumerate(lines, 1):
    p = page_of[i]
    if p not in cfg:
        continue
    n, per, ctxn = cfg[p]
    s = ln.replace("|", " ").strip()
    if not s:
        continue
    parts = s.split()
    vals = []
    while parts and tok.match(parts[-1]):
        vals.append(parts.pop())
    vals.reverse()
    label = " ".join(parts)
    if not vals:
        continue
    if p == 13 and len(vals) == 0:
        continue
    if len(vals) < n:
        unmatched.append((i, p, s))
        continue
    vals = vals[-n:]
    label = re.sub(r"\s+", " ", label).strip(" -")
    if not label:
        label = "(continuation line)"
    for v, pr in zip(vals, per):
        flag = " ZERO_STANDING" if (v == "-" or v in ("0.00", "(0.00)")) else ""
        add("NUMBER", p, i, v + flag, "%s: %s, %s" % (ctxn, label[:60], pr))

# ---------- manual rows for text pages ----------
def M(t, p, sub, val, ctx, nth=1):
    add(t, p, find(sub, p, nth), val, ctx)

# Page 1
M("DATE", 1, "Date:26.10.2026", "26.10.2026", "cover letter date")
M("NUMBER", 1, "Symbol/Scrip Code", "530555", "BSE scrip code")
M("ENTITY", 1, "Symbol/Scrip Code", "PARACABLES (NSE symbol)", "NSE symbol")
M("ENTITY", 1, "BSE Limited", "BSE Limited", "stock exchange addressee")
M("ENTITY", 1, "BSE Limited", "National Stock Exchange of India Ltd.", "stock exchange addressee")
M("ENTITY", 1, "Regulation 30 _and_33", "SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015", "regulator and regulation")
M("NUMBER", 1, "Regulation 30 _and_33", "Regulation 30 and 33", "SEBI LODR regulations invoked")
M("DATE", 1, "Directors of the Company", "Monday, 26 October 2026", "board meeting date")
M("DATE", 1, "a) Standalone", "quarter and half year ended 30th September, 2026", "period of results approved")
M("DATE", 1, "b) Limited Review", "quarter and half year ended 30th September, 2026", "period of limited review report")
M("NUMBER", 1, "commenced at", "02.00 p.m.", "board meeting start time")
M("NUMBER", 1, "commenced at", "3.40 p.m.", "board meeting end time")
M("ENTITY", 1, "For Paramount Communications Limited", "Paramount Communications Limited", "issuer")
M("ENTITY", 1, "Rashi Goel", "Rashi Goel, Company Secretary & Compliance Officer", "signatory")
M("DATE", 1, "Date: 2026.10.26", "2026.10.26 15:52:13 +05'30'", "digital signature timestamp")
M("NUMBER", 1, "CIN", "CIN L74899DL1994PLC061295", "company CIN")
M("DATE", 1, "CIN", "1994 (CIN incorporation year)", "year embedded in CIN")
M("ENTITY", 1, "www.paramountcables.com", "www.paramountcables.com", "company website")
M("QUALIFIER", 1, "a) Standalone", "Un-Audited Financial Results", "results are unaudited")
M("QUALIFIER", 1, "b) Limited Review", "Limited Review Report of Statutory Auditors", "review not audit")
M("FORWARD", 1, "uploaded on website", "information being uploaded on website of the Company", "filing disclosure commitment")
# Page 2 auditor report
M("ENTITY", 2, "BHOLUSARIA", "P. Bholusaria & Co., Chartered Accountants", "statutory auditor")
M("ENTITY", 2, "Firm", "Firm Registration No: 000468N", "auditor firm registration") if False else None
M("ENTITY", 2, "Registration No", "Firm Registration No: 000468N", "auditor firm registration")
M("ENTITY", 2, "Pawan Bholusaria", "Pawan Bholusaria, Partner, M.No.080691", "signing partner")
M("NUMBER", 2, "Registration No", "000468N", "ICAI firm registration number")
M("NUMBER", 2, "M.No", "080691", "partner membership number")
M("NUMBER", 2, "UDIN", "UDIN 26080691IIABTTN583 (OCR: 2 6O806GIIABTTN5 (83)", "UDIN standalone report; OCR unclear")
M("QUALIFIER", 2, "UDIN", "UDIN text OCR-illegible; FOOTNOTE_UNRESOLVED", "UDIN needs image check")
M("DATE", 2, "Date: 26.10.2026", "26.10.2026", "standalone review report date")
M("DATE", 2, "half", "quarter and half year ended 30th September 2026", "review period standalone")
M("NUMBER", 2, "Standard on Review Engagement", "SRE 2410", "review standard")
M("NUMBER", 2, "Indian Accounting Standard 34", "Ind AS 34", "interim reporting standard")
M("NUMBER", 2, "section", "Section 133, Companies Act 2013; Rule 3", "legal basis")
M("QUALIFIER", 2, "moderate assurance", "review gives moderate assurance, not an audit; no audit opinion expressed", "limited review scope")
M("QUALIFIER", 2, "Based on our review", "nothing has come to our attention indicating material misstatement (unmodified conclusion)", "review conclusion standalone")
M("ENTITY", 2, "Institute of Chartered Accountants", "Institute of Chartered Accountants of India", "standard setter")
# Page 6 notes standalone
M("QUALIFIER", 6, "aforesaid Standalone", "Results reviewed by Audit Committee 26 Oct 2026 and approved by Board same date", "note 1 standalone")
M("DATE", 6, "aforesaid Standalone", "26th October, 2026", "audit committee and board date")
M("QUALIFIER", 6, "Limited Review of the standalone", "Statutory Auditors limited review; unmodified opinion", "note 2 standalone")
M("QUALIFIER", 6, "These standalone financial results", "Prepared under Ind AS, Section 133 Companies Act 2013", "note 3 standalone")
M("DATE", 6, "Extra Ordinary General Meeting", "EGM 06.06.2026", "EGM approving preferential issue")
M("NUMBER", 6, "issue 2,19,97,664", "2,19,97,664 equity shares", "preferential issue to non-promoters")
M("NUMBER", 6, "issue 2,19,97,664", "Face Value Rs. 2/- per share", "preferential shares face value")
M("NUMBER", 6, "42/- per equity", "Rs. 42/- per equity share (including premium)", "preferential issue price")
M("DATE", 6, "allotted the equity shares", "01.07.2026", "allotment date equity shares")
M("NUMBER", 6, "30,52,09,814", "30,52,09,814 equity shares", "share count before allotment")
M("NUMBER", 6, "32,72,07,478", "32,72,07,478 equity shares", "share count after preferential allotment")
M("NUMBER", 6, "issue 72,00,000", "72,00,000 convertible equity share warrants", "warrants to promoters")
M("NUMBER", 6, "price of Rs. 42/-", "Rs. 42/- per warrant (including premium)", "warrant issue price") if False else None
M("NUMBER", 6, "10.50/- per equity warrant", "25% application money (Rs. 10.50/- per warrant)", "warrant application money")
M("DATE", 6, "allotees on 01.07.2026", "01.07.2026", "allotment date warrants")
M("ENTITY", 6, "to non-promoter persons", "non-promoter persons and entities", "allottees preferential equity")
M("ENTITY", 6, "to\npromoters", "promoters", "warrant allottees") if False else None
M("FORWARD", 6, "convertible equity share warrants each", "72,00,000 warrants each convertible into one equity share of Rs. 2/- (75% balance payable on conversion)", "warrant conversion pending")
M("QUALIFIER", 6, "Description Amount", "Amount (Rs. in Crores)", "use-of-proceeds table unit")
M("NUMBER", 6, "Funds raised for issue of 2,19,97,664", "92.39", "funds raised, equity shares non-promoters, Rs Cr")
M("NUMBER", 6, "Funds raised for issue of 72,00,000", "7.56", "funds raised, warrants promoters, Rs Cr")
M("NUMBER", 6, "Add: Income earned", "0.10", "income on unutilised amount, Rs Cr")
M("NUMBER", 6, "Less: Utlization", "73.39", "utilisation during quarter ended 30.09.2026, Rs Cr")
M("NUMBER", 6, "Un-utilized Amount", "26.66", "unutilised issue proceeds 30.09.2026, Rs Cr")
M("QUALIFIER", 6, "parked in mutual fund", "* The amount has been parked in mutual fund and utilization account with schedule bank", "footnote on Un-utilzed Amount*")
M("QUALIFIER", 6, "no deviation", "funds utilised for purpose raised; no deviation in utilisation of issue proceeds", "use-of-proceeds statement")
M("DATE", 6, "14.07.2026", "14.07.2026", "ESOP allotment date")
M("NUMBER", 6, "31,995", "31,995 equity shares", "ESOP exercise allotment")
M("NUMBER", 6, "premium of Rs. 3/-", "premium Rs. 3/- per share (face value Rs. 2/-)", "ESOP exercise price component")
M("ENTITY", 6, "Stock Incentive Plan", "Paramount Communications - Stock Incentive Plan", "ESOP scheme")
M("NUMBER", 6, "32,72,39,473", "32,72,39,473 equity shares", "share count after ESOP allotment")
M("QUALIFIER", 6, "no separate reportable segments", "No separate reportable segments under Ind AS-108 (standalone)", "note 6 standalone segments")
M("QUALIFIER", 6, "regrouped", "Previous period figures regrouped/rearranged for comparison", "note 7 standalone")
M("ENTITY", 6, "Sanjay", "Sanjay Aggarwal, Chairman & CEO (DIN 00001788)", "signatory standalone results")
M("DATE", 6, "Date: 26.10.2026", "26.10.2026", "signing date standalone results")
# Page 3 + 9 notes/qualifiers
M("QUALIFIER", 3, "(Rs. In Crores except per share data", "Rs. In Crores except per share data", "unit statement standalone P&L")
M("QUALIFIER", 3, "not annualised", "EPS (not annualised for the quarters)", "EPS qualifier standalone", 1)
M("QUALIFIER", 3, "Unaudited Unaudited", "Quarter/half year columns Unaudited; year ended 31.03.2026 Audited", "audit status of columns standalone")
M("QUALIFIER", 9, "(Rs. in Crores except per share data", "Rs. in Crores except per share data", "unit statement consolidated P&L")
M("QUALIFIER", 9, "not annualised", "EPS (not annualised for the quarters)", "EPS qualifier consolidated", 1)
M("QUALIFIER", 9, "Unaudited Unaudited", "Quarter/half year columns Unaudited; year ended 31.03.2026 Audited", "audit status of columns consolidated")
M("QUALIFIER", 3, "XVI]", "Paid-up Equity Share Capital (Face Value Rs. 2 per share)", "face value qualifier standalone")
M("QUALIFIER", 9, "XVI |", "Paid-up Equity Share Capital (Face Value Rs. 2 per share)", "face value qualifier consolidated")
M("QUALIFIER", 4, "(Rs. in crores)", "Standalone Statement of Assets and Liabilities, Rs. in crores", "unit statement standalone BS")
M("QUALIFIER", 4, "(Unaudited)", "30.09.2026 Unaudited; 31.03.2026 Audited", "audit status standalone BS")
M("QUALIFIER", 10, "(Rs. in Crores)", "Consolidated Statement of Assets and Liabilities, Rs. in Crores", "unit statement consolidated BS")
M("QUALIFIER", 10, "(Unaudited)", "30.09.2026 Unaudited; 31.03.2026 Audited", "audit status consolidated BS")
M("QUALIFIER", 5, "Note:", "Note: Cash Flow Statement prepared under indirect method per IND AS-7", "note 1 standalone cash flow")
M("QUALIFIER", 5, "2. Figures", "Figures in brackets represent outflow of cash", "note 2 standalone cash flow")
M("QUALIFIER", 5, "(Rs. in Crores )", "Rs. in Crores", "unit statement standalone CF")
M("QUALIFIER", 11, "1. Consolidated Cash", "Consolidated Cash Flow Statement prepared under indirect method per IND AS-7", "note 1 consolidated cash flow")
M("QUALIFIER", 11, "2. Figures", "Figures in brackets represent outflow of cash", "note 2 consolidated cash flow")
M("QUALIFIER", 11, "(Rs. in Crores )", "Rs. in Crores", "unit statement consolidated CF")
M("QUALIFIER", 13, "Rs. in Crores", "Rs. in Crores (segment)", "unit statement segment") if False else None
M("QUALIFIER", 13, "(Rs. in Crores)", "Rs. in Crores", "unit statement segment annexure")
M("QUALIFIER", 13, "Annexure-", "Annexure-A Consolidated unaudited Segment Information", "annexure label")
M("QUALIFIER", 13, "Particulars 30.09.2026", "Quarter ended/Half Year Ended Unaudited; Year Ended 31.03.2026 Audited", "audit status segment columns")
# Dates headers periods
M("DATE", 3, "STATEMENT OF UNAUDITED STANDALONE", "quarter and half year ended 30th September, 2026", "standalone results period")
M("DATE", 9, "STATEMENT OF UNAUDITED CONSOLIDATED", "quarter and half year ended 30th September, 2026", "consolidated results period")
M("DATE", 4, "Balance", "30.09.2026 and 31.03.2026", "standalone BS dates") if False else None
M("DATE", 4, "30.09.2026 31.03.2026", "30.09.2026 and 31.03.2026", "standalone balance sheet dates")
M("DATE", 10, "30.09.2026 31.03.2026", "30.09.2026 and 31.03.2026", "consolidated balance sheet dates")
M("DATE", 5, "HALF YEAR ENDED", "half year ended 30th September, 2026 (comparative 2025)", "standalone cash flow period")
M("DATE", 11, "HALF YEAR ENDED", "half year ended 30th September, 2026 (comparative 2025)", "consolidated cash flow period")
M("DATE", 13, "Segment Information for the Quarter", "Quarter and Half Year ended 30th September, 2026", "segment period")
M("ENTITY", 3, "PARAMOUNT COMMUNICATIONS", "Paramount Communications Limited", "issuer standalone results")
M("ENTITY", 9, "PARAMOUNT COMMUNICATIONS", "Paramount Communications Limited", "issuer consolidated results")
M("NUMBER", 3, "CIN", "CIN L74899DL1994PLC061295", "CIN on standalone P&L")
M("ENTITY", 3, "KH-433", "KH-433, Maulsari Avenue, Westend Greens, Rangpuri, New Delhi-110037", "registered address")
M("NUMBER", 3, "Ph.:", "+91-11-45618600-900 (OCR; as on page 3 OCR)", "company phone")
# Page 7 consolidated review
M("ENTITY", 7, "BHOLUSARIA", "P. Bholusaria & Co., Chartered Accountants", "statutory auditor consolidated")
M("ENTITY", 7, "Pawan Bholusaria", "Pawan Bholusaria, Partner", "signing partner consolidated") if False else None
M("ENTITY", 7, "Paramount Holdings Limited", "Paramount Holdings Limited", "subsidiary")
M("ENTITY", 7, "AEI Power Cables Limited", "AEI Power Cables Limited", "subsidiary")
M("ENTITY", 7, "Securities and Exchange", "Securities and Exchange Board of India", "regulator")
M("NUMBER", 7, "2 subsidiaries", "2 subsidiaries", "count of subsidiaries not reviewed by their auditors")
M("NUMBER", 7, "total assets of Rs. NIL", "Rs. NIL ZERO_STANDING", "total assets of unreviewed subsidiaries 30.09.2026")
M("NUMBER", 7, "total revenue of Rs. NIL", "Rs. NIL ZERO_STANDING", "total revenue unreviewed subsidiaries")
M("NUMBER", 7, "profit after tax of Rs. NIL", "Rs. NIL ZERO_STANDING", "net profit after tax unreviewed subsidiaries")
M("NUMBER", 7, "total comprehensive income of Rs. NIL", "Rs. NIL ZERO_STANDING", "total comprehensive income unreviewed subsidiaries")
M("NUMBER", 7, "net cash flows of Rs. NIL", "Rs. NIL ZERO_STANDING", "net cash flows unreviewed subsidiaries half year")
M("QUALIFIER", 7, "2 subsidiaries which have not been reviewed", "2 subsidiaries' interim results not reviewed by their auditors; management-furnished, unaudited", "emphasis on unreviewed subsidiaries")
M("QUALIFIER", 7, "moderate", "limited review gives moderate assurance, not an audit", "review scope consolidated")
M("NUMBER", 7, "Standard on Review Engagement", "SRE 2410", "review standard consolidated")
M("NUMBER", 7, "Regulation 33(8)", "Regulation 33(8)", "SEBI circular procedures")
M("DATE", 7, "30th September, 2026 (", "quarter and half year ended 30th September, 2026", "consolidated review period") if False else None
# Page 8
M("QUALIFIER", 8, "not material to the group", "results of 2 subsidiaries not material to the group", "auditor view on subsidiaries")
M("QUALIFIER", 8, "not modified", "Conclusion on the Statement is not modified in respect of above matter", "unmodified conclusion consolidated")
M("QUALIFIER", 8, "nothing has come to our attention", "nothing has come to attention indicating material misstatement", "review conclusion consolidated")
M("NUMBER", 8, "Firm Registration No", "000468N", "ICAI firm registration number consolidated")
M("NUMBER", 8, "M.No", "080691", "partner membership number consolidated")
M("NUMBER", 8, "DIN", "DIN 26080691VFYDBU8230 (UDIN)", "UDIN consolidated report")
M("DATE", 8, "Date: 26.10.2026", "26.10.2026", "consolidated review report date")
M("ENTITY", 8, "Pawan Bholusaria", "Pawan Bholusaria, Partner", "signing partner consolidated")
# Page 12 notes consolidated
M("QUALIFIER", 12, "aforesaid Consolidated", "Results reviewed by Audit Committee 26 Oct 2026 and approved by Board same date", "note 1 consolidated")
M("DATE", 12, "aforesaid Consolidated", "26th October, 2026", "audit committee and board date consolidated")
M("QUALIFIER", 12, "Limited Review of the consolidated", "Statutory Auditors limited review; unmodified opinion", "note 2 consolidated")
M("QUALIFIER", 12, "These consolidated financial results", "Prepared under Ind AS, Section 133 Companies Act 2013", "note 3 consolidated")
M("QUALIFIER", 12, "Ind AS 110", "Consolidated results prepared per Ind AS 110 Consolidated Financial Statements", "note 4 consolidated")
M("NUMBER", 12, "Ind AS 110", "Ind AS 110", "consolidation standard")
M("DATE", 12, "Extra Ordinary General Meeting", "EGM 06.06.2026", "EGM approving preferential issue")
M("NUMBER", 12, "issue 2,19,97,664", "2,19,97,664 equity shares", "preferential issue to non-promoters")
M("NUMBER", 12, "42/- per equity", "Rs. 42/- per equity share (including premium)", "preferential issue price")
M("DATE", 12, "01.07.2026", "01.07.2026", "allotment date equity shares")
M("NUMBER", 12, "30,52,09,814", "30,52,09,814 equity shares", "share count before allotment")
M("NUMBER", 12, "32,72,07,478", "32,72,07,478 equity shares", "share count after preferential allotment")
M("NUMBER", 12, "issue 72,00,000", "72,00,000 convertible equity share warrants", "warrants to promoters")
M("NUMBER", 12, "10.50/- per equity warrant", "25% application money (Rs. 10.50/- per warrant)", "warrant application money")
M("FORWARD", 12, "convertible equity share warrants each", "72,00,000 warrants each convertible into one equity share of Rs. 2/- (75% balance payable on conversion)", "warrant conversion pending")
M("NUMBER", 12, "Funds raised for issue of 2,19,97,664", "92.39", "funds raised, equity shares non-promoters, Rs Cr")
M("NUMBER", 12, "Funds raised for issue of 72,00,000", "7.56", "funds raised, warrants promoters, Rs Cr")
M("NUMBER", 12, "Add: Income", "0.10", "income on unutilised amount, Rs Cr")
M("NUMBER", 12, "Less: Utlization", "73.39", "utilisation during quarter ended 30.09.2026, Rs Cr")
M("NUMBER", 12, "Un-utilized Amount", "26.66", "unutilised issue proceeds 30.09.2026, Rs Cr")
M("QUALIFIER", 12, "parked in mutual fund", "* The amount has been parked in mutual fund and utilization account with schedule bank", "footnote on Un-utilized Amount*")
M("QUALIFIER", 12, "no deviation", "funds utilised for purpose raised; no deviation in utilisation of issue proceeds", "use-of-proceeds statement")
M("DATE", 12, "14.07.2026", "14.07.2026", "ESOP allotment date")
M("NUMBER", 12, "31,995", "31,995 equity shares", "ESOP exercise allotment")
M("NUMBER", 12, "premium of Rs. 3/-", "premium Rs. 3/- per share (face value Rs. 2/-)", "ESOP exercise price component")
M("NUMBER", 12, "32,72,39,473", "32,72,39,473 equity shares", "share count after ESOP allotment")
M("ENTITY", 12, "Stock Incentive Plan", "Paramount Communications - Stock Incentive Plan", "ESOP scheme")
M("ENTITY", 12, "Valens Technologies", "Valens Technologies Private Limited", "former wholly owned subsidiary divested")
M("DATE", 12, "6th November, 2025", "6th November, 2025", "Valens Technologies divestment and cessation date")
M("QUALIFIER", 12, "does not include any figure", "Q2 FY27, Q1 FY27 and H1 FY27 exclude Valens Technologies; Q2 FY26, H1 FY26 and FY26 include it; figures not directly comparable", "comparability note 7 consolidated")
M("QUALIFIER", 12, "two reportable segments", "Two reportable segments: Wires & Cables and Pipes (Annexure A)", "note 8 consolidated segments")
M("ENTITY", 12, "two reportable segments", "Wires & Cables segment", "reportable segment")
M("ENTITY", 12, "two reportable segments", "Pipes segment", "reportable segment")
M("QUALIFIER", 12, "regrouped", "Previous period figures regrouped/rearranged for comparison", "note 9 consolidated")
M("ENTITY", 12, "Sanjay", "Sanjay Aggarwal, Chairman & CEO (DIN 00001788)", "signatory consolidated results")
M("DATE", 12, "Date: 26.10.2026", "26.10.2026", "signing date consolidated results")
M("NUMBER", 12, "Sanjay", "DIN 00001788", "director identification number") if False else None
M("NUMBER", 6, "DIN:00001788", "DIN 00001788", "director identification number standalone") if False else None
# Page 13
M("ENTITY", 13, "Wire and Cables 560.40", "Wire and Cables segment", "segment")
M("ENTITY", 13, "Pipes - - 3.69", "Pipes segment", "segment")
M("QUALIFIER", 13, "Less Inter-segment", "Inter-segment revenue eliminated in total revenue from operations", "segment revenue elimination")
M("QUALIFIER", 13, "Unallocated (income)", "Segment results before finance cost, exceptional items, unallocated expenses/income and tax", "segment result definition")
M("QUALIFIER", 13, "Profit (Loss) before Finance", "Segment results stated before finance cost, exceptional items, unallocated items and tax", "segment profit definition")

add("NUMBER",3,198,"717.03","standalone P&L: Other Equity excluding revaluation Reserve, year ended 31.03.2026")
add("NUMBER",9,494,"717.03","consolidated P&L: Other Equity excluding revaluation Reserve, year ended 31.03.2026")
# ---------- emit ----------
order = ["NUMBER", "ENTITY", "FORWARD", "DATE", "QUALIFIER"]
out = []
rid = 0
counts = {}
for t in order:
    counts[t] = len(rows[t])
    out.append("\n## %s\nROW | page | line | TYPE | value | context" % t)
    for (p, l, v, c) in rows[t]:
        rid += 1
        out.append("R%03d | page %d | line %d | %s | %s | %s" % (rid, p, l, t, v, c))
hdr = """# A1 STRUCTURED EXTRACTION
source: Paramount_Q2FY27_Results.pdf (PARACABLES, Q2 FY27, results)
fulltext: extracted/paracables-results-q2fy27-fulltext.md (line numbers refer to that file as written, header included)
unit: Rs Crores (x1); per-share data in Rs; share counts in numbers
extraction_mode: scan-ocr, image-verified statement pages (see fulltext header correction log)
ROW ID RANGE: R001-R%03d
counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d | TOTAL %d
""" % (rid, counts["NUMBER"], counts["ENTITY"], counts["FORWARD"], counts["DATE"], counts["QUALIFIER"], rid)
open(W + "extracted/paracables-results-q2fy27-structured.md", "w", encoding="utf-8").write(hdr + "\n".join(out) + "\n")
print(rid, counts)
print("UNMATCHED (fewer values than columns):")
for u in unmatched:
    print(u)
