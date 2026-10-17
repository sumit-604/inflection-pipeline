import re, sys, os
B = r"C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/q2fy27/runs/indorama-q2fy27/"
IMG = B + "work/a1-results/img/"
PL = ["Q2 FY27", "Q1 FY27", "Q2 FY26", "H1 FY27", "H1 FY26", "FY26"]
D = "-"
def six(s): return s.split("|")
PL_S = [
 ("Revenue from operations", "1,248.33|817.91|1,166.29|2,066.24|2,351.23|4,518.73"),
 ("Other income", "5.82|6.85|3.64|12.67|8.37|27.52"),
 ("Total income (1+2)", "1,254.15|824.76|1,169.93|2,078.91|2,359.60|4,546.25"),
 ("(a) Cost of materials consumed", "942.04|588.21|938.30|1,530.25|1,816.98|3,523.97"),
 ("(b) Purchase of stock-in-trade", "42.11|17.45|4.05|59.56|12.11|17.33"),
 ("(c) Changes in inventories of finished goods, WIP and stock-in-trade", "17.98|31.92|(23.30)|49.90|39.50|29.14"),
 ("(d) Employee benefits expense", "30.12|29.59|30.93|59.71|62.83|119.42"),
 ("(e) Other expenses", "128.76|85.37|148.75|214.13|285.16|556.10"),
 ("Total expenses before D&A, finance costs and FX loss/(gain)", "1,161.01|752.54|1,098.73|1,913.55|2,216.58|4,247.96"),
 ("Profit from operations before D&A, finance costs and FX loss/(gain) (3-4)", "93.14|72.22|71.20|165.36|143.02|298.29"),
 ("Depreciation and amortisation expense", "9.87|9.63|9.59|19.50|19.15|38.24"),
 ("Finance costs", "25.65|25.79|28.74|51.44|52.16|111.19"),
 ("Foreign exchange fluctuation loss", "2.57|3.05|9.83|5.62|16.36|36.14"),
 ("Total expenses before tax (4+6+7+8)", "1,199.10|791.01|1,146.89|1,990.11|2,304.25|4,433.53"),
 ("Profit before exceptional items and tax (3-9)", "55.05|33.75|23.04|88.80|55.35|112.72"),
 ("Exceptional items - Employee benefit expenses", "-|-|-|-|-|2.69"),
 ("Profit/(loss) before tax (10-11)", "55.05|33.75|23.04|88.80|55.35|110.03"),
 ("Tax expense/(credit)", "-|-|-|-|-|-"),
 ("Deferred tax (credit)/expense", "-|-|-|-|-|-"),
 ("Net profit/(loss) for the period (12-13)", "55.05|33.75|23.04|88.80|55.35|110.03"),
 ("OCI (i) Items not reclassified to profit or loss", "-|-|-|-|-|0.77"),
 ("OCI (ii) Income tax on items not reclassified", "-|-|-|-|-|-"),
 ("Total comprehensive income for the period (14+15)", "55.05|33.75|23.04|88.80|55.35|110.80"),
 ("Paid-up equity share capital (FV Rs 10)", "261.11|261.11|261.11|261.11|261.11|261.11"),
 ("Other equity", "||||302.65"),
 ("EPS (a) Basic (Rs, not annualised for quarters)", "2.11|1.29|0.88|3.40|2.12|4.21"),
 ("EPS (b) Diluted (Rs, not annualised for quarters)", "2.11|1.29|0.88|3.40|2.12|4.21"),
]
PL_C = [
 ("Revenue from operations", "1,340.64|936.64|1,220.64|2,277.28|2,526.35|4,910.06"),
 ("Other income", "3.40|3.56|1.71|6.96|4.56|18.95"),
 ("Total income (1+2)", "1,344.04|940.20|1,222.35|2,284.24|2,530.91|4,929.01"),
 ("(a) Cost of materials consumed", "944.32|584.61|931.31|1,528.93|1,754.02|3,533.96"),
 ("(b) Purchase of stock-in-trade", "116.22|48.30|78.76|164.52|161.16|196.60"),
 ("(c) Changes in inventories of finished goods, WIP and stock-in-trade", "(22.94)|62.14|(69.94)|39.20|(4.53)|36.21"),
 ("(d) Employee benefits expense", "31.53|30.97|32.38|62.50|65.79|125.31"),
 ("(e) Other expenses", "157.25|106.14|169.46|263.39|333.82|668.68"),
 ("Total expenses before D&A, finance costs and FX loss/(gain)", "1,226.38|832.16|1,141.97|2,058.54|2,350.26|4,560.76"),
 ("Profit from operations before D&A, finance costs and FX loss/(gain) (3-4)", "117.66|108.04|80.38|225.70|180.65|368.25"),
 ("Depreciation and amortisation expense", "12.30|12.01|11.98|24.31|23.91|47.76"),
 ("Finance costs", "28.99|29.38|33.57|58.37|62.60|130.31"),
 ("Foreign exchange fluctuation loss", "2.51|2.91|10.28|5.42|16.84|37.27"),
 ("Total expenses before tax (4+6+7+8)", "1,270.18|876.46|1,197.80|2,146.64|2,453.61|4,776.10"),
 ("Profit before exceptional items and tax (3-9)", "73.86|63.74|24.55|137.60|77.30|152.91"),
 ("Exceptional item - Employee benefit expenses", "-|-|-|-|-|2.70"),
 ("Profit/(loss) before tax (10-11)", "73.86|63.74|24.55|137.60|77.30|150.21"),
 ("Tax expense", "-|-|-|-|-|-"),
 ("Deferred tax (credit)", "(0.22)|-|-|(0.22)|-|-"),
 ("Net profit/(loss) for the period (12-13)", "74.08|63.74|24.55|137.82|77.30|150.21"),
 ("OCI (i) Items not reclassified to profit or loss", "-|-|-|-|-|0.75"),
 ("OCI (ii) Income tax on items not reclassified", "-|-|-|-|-|-"),
 ("Total comprehensive income for the period (14+15)", "74.08|63.74|24.55|137.82|77.30|150.96"),
 ("Profit attributable to Owners of the parent", "74.08|63.74|24.55|137.82|77.30|150.21"),
 ("Profit attributable to Non Controlling interest", "-|-|-|-|-|-"),
 ("OCI attributable to Owners of the parent", "-|-|-|-|-|0.75"),
 ("OCI attributable to Non Controlling interest", "-|-|-|-|-|-"),
 ("Total comprehensive income attributable to Owners of the parent", "74.08|63.74|24.55|137.82|77.30|150.96"),
 ("Total comprehensive income attributable to Non Controlling interest", "-|-|-|-|-|-"),
 ("Paid-up equity share capital (FV Rs 10)", "261.11|261.11|261.11|261.11|261.11|261.11"),
 ("Other equity", "||||258.06"),
 ("EPS (a) Basic (Rs, not annualised for quarters)", "2.84|2.44|0.94|5.28|2.96|5.75"),
 ("EPS (b) Diluted (Rs, not annualised for quarters)", "2.84|2.44|0.94|5.28|2.96|5.75"),
]
BS_S = [
 ("Property, plant and equipment","858.86","867.19"),("Right of use assets","6.01","7.07"),("Capital work-in-progress","35.42","36.91"),
 ("Intangible assets","0.04","-"),("Investments (non-current)","16.10","16.10"),("Loans (non-current)","76.10","127.85"),
 ("Other financial assets (non-current)","2.04","2.08"),("Deferred tax assets (net)","258.61","258.61"),("Non-current tax assets (net)","4.66","8.42"),
 ("Other non-current assets","26.88","26.47"),("Total non-current assets","1284.72","1350.70"),("Inventories","609.01","596.88"),
 ("Trade receivables","285.60","379.70"),("Cash and cash equivalents","1.65","10.49"),("Bank balances other than cash and cash equivalents","1.46","1.44"),
 ("Loans (current)","1.51","1.24"),("Other financial assets (current)","604.16","607.59"),("Other current assets","77.87","63.04"),
 ("Total current assets","1581.26","1660.38"),("TOTAL ASSETS","2,865.98","3011.08"),("Equity share capital","261.11","261.11"),
 ("Other equity","391.45","302.65"),("Total equity","652.56","563.76"),("Borrowings (non-current)","285.28","350.77"),
 ("Lease liabilities (non-current)","6.44","6.92"),("Provisions (non-current)","52.89","50.02"),("Total non-current liabilities","344.61","407.71"),
 ("Borrowings (current)","434.14","593.21"),("Lease liabilities (current)","0.49","1.35"),("Trade payables MSME","11.09","13.28"),
 ("Trade payables other than MSME","1347.56","1367.48"),("Other financial liabilities (current)","30.23","20.05"),("Other current liabilities","9.81","8.75"),
 ("Provisions (current)","35.49","35.49"),("Total current liabilities","1868.81","2039.61"),("TOTAL EQUITY AND LIABILITIES","2865.98","3011.08"),
]
BS_C = [
 ("Property, plant and equipment","1,214.65","1,225.06"),("Right of use assets","6.01","7.07"),("Capital work-in-progress","38.45","42.03"),
 ("Intangible assets","0.04","-"),("Other financial assets (non-current)","2.49","2.51"),("Deferred tax assets (net)","268.20","258.61"),
 ("Non-current tax assets (net)","7.31","10.02"),("Other non-current assets","27.75","26.53"),("Total non-current assets","1,564.90","1,571.83"),
 ("Inventories","690.81","666.86"),("Trade receivables","103.06","243.32"),("Cash and cash equivalents","6.82","16.82"),
 ("Bank balances other than cash and cash equivalents","1.44","1.44"),("Loans (current)","1.51","1.24"),("Other financial assets (current)","667.63","658.25"),
 ("Other current assets","95.51","84.33"),("Total current assets","1,566.78","1,672.26"),("TOTAL ASSETS","3,131.68","3,244.09"),
 ("Equity share capital","261.11","261.11"),("Other equity","395.88","258.06"),("Total equity","656.99","519.17"),
 ("Borrowings (non-current)","332.18","444.58"),("Lease liabilities (non-current)","6.44","6.92"),("Provisions (non-current)","53.45","50.58"),
 ("Deferred tax liabilities (net)","9.37","-"),("Total non-current liabilities","401.44","502.08"),("Borrowings (current)","527.95","687.02"),
 ("Lease liabilities (current)","0.49","1.35"),("Trade payables MSME","17.60","17.33"),("Trade payables other than MSME","1,444.43","1,433.26"),
 ("Other financial liabilities (current)","35.43","25.29"),("Other current liabilities","11.85","23.09"),("Provisions (current)","35.50","35.50"),
 ("Total current liabilities","2,073.25","2,222.84"),("TOTAL EQUITY AND LIABILITIES","3,131.68","3,244.09"),
]
CF_S = [
 ("Profit/(loss) before tax","88.80","55.35"),("Depreciation and amortisation expense","19.50","19.15"),("(Gain)/Loss on disposal of PPE","0.03","(0.42)"),
 ("Finance costs","51.44","52.16"),("Interest income","(5.95)","(3.71)"),("Debts/advances written off","0.01","0.12"),
 ("Operating profit before working capital changes","153.83","122.65"),("Changes in trade receivables","94.09","(90.33)"),
 ("Changes in other financial assets and loans","3.20","(65.48)"),("Changes in other assets","(14.83)","21.84"),("Changes in inventories","(12.13)","65.45"),
 ("Changes in trade payables","(22.11)","(9.92)"),("Changes in provisions","2.87","2.87"),("Changes in other financial liabilities","10.57","1.73"),
 ("Changes in other liabilities","1.05","(2.02)"),("Cash generated from operations before tax","216.54","46.79"),("Income taxes refund/(paid) net","3.76","1.62"),
 ("Net cash from operating activities [A]","220.30","48.41"),("Purchase of PPE incl CWIP, capital advances and creditors","(8.44)","(8.57)"),
 ("Proceeds from sale of PPE","-","0.82"),("Loans to subsidiaries (net)","51.75","(7.50)"),("Bank balances other than cash and cash equivalents [net]","(0.02)","1.69"),
 ("Interest received","5.94","3.73"),("Net cash from investing activities [B]","49.23","(9.83)"),("Repayment of non-current borrowings","(17.58)","(54.54)"),
 ("Proceeds from non-current borrowings","0.00","44.00"),("Movement in current borrowings [net]","(206.98)","8.27"),("Payment of lease liabilities (principal)","(1.34)","(1.24)"),
 ("Payment of lease liabilities (interest)","(0.39)","(0.48)"),("Finance costs paid","(52.08)","(52.64)"),("Net cash from financing activities [C]","(278.37)","(56.63)"),
 ("Net increase/(decrease) in cash [A+B+C]","(8.84)","(18.05)"),("Opening balance of cash","10.49","19.56"),("Closing balance of cash","1.65","1.51"),
]
CF_C = [
 ("Profit before tax","137.60","77.30"),("Depreciation and amortisation expense","24.31","23.91"),("(Gain)/Loss on disposal of PPE","0.03","(0.42)"),
 ("Finance costs","58.37","62.60"),("Interest income","(3.60)","(2.12)"),("Debts/advances written off","0.02","0.12"),
 ("Operating profit before working capital changes","216.73","161.39"),("Changes in trade receivables","140.26","3.50"),
 ("Changes in other financial assets and loans","(9.62)","(103.53)"),("Changes in other assets","(11.18)","8.09"),("Changes in inventories","(23.95)","20.80"),
 ("Changes in trade payables","11.45","(2.84)"),("Changes in provisions","2.87","2.87"),("Changes in other financial liabilities","10.53","1.84"),
 ("Changes in other liabilities","(11.34)","(1.41)"),("Cash generated from operations before tax","325.75","90.71"),("Income taxes (paid)/refund net","2.71","0.75"),
 ("Net cash from operating activities [A]","328.46","91.46"),("Purchase of PPE incl CWIP, capital advances and creditors","(9.83)","(9.99)"),
 ("Proceeds from sale of PPE","-","0.82"),("Bank balances other than cash and cash equivalents [net]","-","1.70"),
 ("Interest received","3.59","2.14"),("Net cash from investing activities [B]","(6.24)","(5.33)"),("Repayment of non-current borrowings","(64.49)","(93.63)"),
 ("Proceeds from non-current borrowings","-","44.00"),("Movement in current borrowings [net]","(206.98)","8.27"),("Payment of lease liabilities (principal)","(1.34)","(1.24)"),
 ("Payment of lease liabilities (interest)","(0.39)","(0.48)"),("Finance costs paid","(59.02)","(63.10)"),("Net cash from financing activities [C]","(332.22)","(106.18)"),
 ("Net increase/(decrease) in cash [A+B+C]","(10.00)","(20.05)"),("Opening balance of cash","16.82","24.21"),("Closing balance of cash","6.82","4.16"),
]
TABLES = [  # page, kind, entity, rows
 (3,"PL","standalone",PL_S),(4,"BS","standalone",BS_S),(5,"CF","standalone",CF_S),
 (9,"PL","consolidated",PL_C),(10,"BS","consolidated",BS_C),(11,"CF","consolidated",CF_C)]
tdict = {t[0]: t for t in TABLES}

# ---------- fulltext
hdr_tpl = open(B+"work/a1-results/hdr_new.txt").read()
body = []
for p in range(1,13):
    body.append(f"[page {p}]")
    txt = open(IMG+f"p-{p:02d}.txt", encoding="utf-8", errors="replace").read().rstrip("\n")
    body.append(txt)
    if p in tdict:
        _,kind,ent,rows = tdict[p]
        body.append(f"[IMAGE-VERIFIED TABLE page {p}, {ent}, read from 300 dpi render; supersedes OCR text above where they differ]")
        if kind=="PL": body.append("Particulars | " + " | ".join(PL))
        elif kind=="BS": body.append("Particulars | 30 Sep 2026 | 31 Mar 2026")
        else: body.append("Particulars | H1 FY27 (six months to 30 Sep 2026) | H1 FY26 (six months to 30 Sep 2025)")
        for r in rows:
            body.append(f"VER-{p} | {r[0]} | " + " | ".join(r[1].split("|") if kind=="PL" else r[1:]))
alltext = body
nlines = len(chr(10).join(body).split(chr(10))) + hdr_tpl.count(chr(10))
hdr = hdr_tpl.replace("@@LINES@@", str(nlines))
full = hdr + "\n".join(body) + "\n"
open(B+"extracted/indorama-results-q2fy27-fulltext.md","w",encoding="utf-8").write(full)
lines = full.split("\n")
# page map
pagestart = {}
cur = 0
pages = [0]*(len(lines)+2)
for i,l in enumerate(lines, start=1):
    m = re.match(r"\[page (\d+)\]$", l)
    if m: cur = int(m.group(1))
    pages[i] = cur
def find(page, rx):
    for i,l in enumerate(lines, start=1):
        if pages[i]==page and re.search(rx, l): return i
    print("UNRESOLVED", page, rx, file=sys.stderr); return 0

# ---------- rows
rows_out = []
def add(t, page, line, val, ctx): rows_out.append((t, page, line, val, ctx))
numrows = []
for page,kind,ent,rows in TABLES:
    for r in rows:
        ln = find(page, r"^VER-%d \| %s \|" % (page, re.escape(r[0])))
        if kind=="PL":
            vals = r[1].split("|")
            for per, v in zip(PL, vals):
                if v=="" : continue
                numrows.append((page, ln, v, f"{ent} {r[0]}, {per} (image-verified)" + (" ZERO_STANDING" if v=="-" else "")))
        elif kind=="BS":
            for per, v in zip(["30 Sep 2026","31 Mar 2026"], r[1:]):
                numrows.append((page, ln, v, f"{ent} {r[0]}, {per} (image-verified)" + (" ZERO_STANDING" if v=="-" else "")))
        else:
            for per, v in zip(["H1 FY27","H1 FY26"], r[1:]):
                numrows.append((page, ln, v, f"{ent} cash flow {r[0]}, {per} (image-verified)" + (" ZERO_STANDING" if v in("-","0.00") else "")))
# non-table numbers
misc = [
 (1,r"BSE: 500207|Stock Code BSE","500207","BSE stock code"),
 (1,r"INE156A01020","INE156A01020","ISIN"),
 (1,r"12:00 Noon","12:00 Noon IST","board meeting start time"),
 (1,r"14:35","14:35 PM IST","board meeting end time"),
 (1,r"ACS","ACS: 14223","company secretary membership number"),
 (1,r"Regulation 30 and Regulation 33","Regulation 30 and Regulation 33","LODR regs for outcome"),
 (1,r"Regulation 47","Regulation 47(1)(b)","LODR reg for results extract publication"),
 (2,r"UDIN","UDIN: 26092671NZAYBJ4662","standalone review report UDIN"),
 (2,r"Firm Registration","000756N/N500441","auditor firm registration"),
 (2,r"Membership Number","092671","auditor partner membership number"),
 (2,r"SRE\)? ?2410|\(SRE\)","2410","Standard on Review Engagements number"),
 (6,r"DIN","00206807","DIN of CMD, standalone signature"),
 (8,r"UDIN","UDIN: 26092671GASHHZ5629","consolidated review report UDIN"),
 (8,r"Firm Registration","000756N","auditor firm registration, consolidated"),
 (8,r"Membership Number","092671","auditor partner membership number, consolidated"),
 (12,r"DIN","00206807","DIN of CMD, consolidated signature"),
]
for p,rx,v,c in misc:
    numrows.append((p, find(p,rx), v, c))
ent = [
 (1,r"Corporate Listing|National Stock Exchange","National Stock Exchange of India Limited (NSE, INDORAMA)","exchange addressee"),
 (1,r"BSE Limited","BSE Limited","exchange addressee"),
 (1,r"for Indo Rama Synthetics","Indo Rama Synthetics (India) Limited","filer"),
 (1,r"Ashok Yadav$|^Ashok Yadav|Ashok","Ashok Yadav","Company Secretary and Compliance Officer"),
 (1,r"Corporate Office","Corporate Office, Plot 53 & 54, Udyog Vihar, Gurugram","company address"),
 (1,r"Regd","Regd. Office and Manufacturing Complex, A-31 MIDC Butibori, Nagpur","plant and registered office"),
 (1,r"CIN","L17124MH1986PLC166615","CIN"),
 (2,r"(?i)kothari|CHARTERED","S S Kothari Mehta & Co. LLP","statutory auditor"),
 (2,r"Vijay Kumar","Vijay Kumar","auditor partner"),
 (2,r"Institute of Chartered","Institute of Chartered Accountants of India","issuer of SRE 2410"),
 (6,r"Audit Committee","Audit Committee","reviewed standalone results"),
 (6,r"polyester","polyester goods (manufacturing and trading)","sole reportable segment, standalone"),
 (6,r"nseindia","www.nseindia.com / www.bseindia.com","disclosure sites"),
 (6,r"Chairman","Chairman and Managing Director","standalone signatory"),
 (7,r"Holding Company","Holding Company: Indo Rama Synthetics (India) Limited","consolidated review"),
 (7,r"Regulation\s*$|33 \(8\)|33\(8\)","SEBI circular under Regulation 33(8)","regulator procedure"),
 (8,r"Indorama Ventures Yarns","Indorama Ventures Yarns Private Limited","subsidiary"),
 (8,r"Indorama Yarns Private","Indorama Yarns Private Limited","subsidiary"),
 (8,r"Indorama Sustainable Polymers","Indorama Sustainable Polymers (India) Private Limited","subsidiary"),
 (8,r"Indorama Sustainable Polyester","Indorama Sustainable Polyester Yarns Private Limited","subsidiary"),
 (8,r"Vijay Kumar","Vijay Kumar","auditor partner, consolidated"),
 (12,r"Lohia","Om Prakash Lohia","Chairman and Managing Director, signatory"),
 (12,r"Audit Committee","Audit Committee","reviewed consolidated results"),
 (12,r"polyester","polyester goods (manufacturing and trading)","sole reportable segment, Group"),
]
fwd = [
 (1,r"would be","the Company would be publishing Extract of Un-audited Financial Results for Q2 and half-year ended 30 September 2026 (Reg 47(1)(b))","board agenda item b, newspaper publication"),
 (1,r"website of the|Company at www","It is also being published on the website of the Company at www.indoramaindia.com","extract on website"),
]
dates = [
 (1,r"STEXCH|October 2026$","16 October 2026","letter date"),
 (1,r"Meeting held today","16 October 2026","board meeting date"),
 (1,r"second","second quarter and half-year ended 30 September 2026","results period (Q2 FY27, H1 FY27)"),
 (2,r"Date:","October 16, 2026","standalone review report date"),
 (2,r"year to date from","April 1, 2026 to September 30, 2026","review period"),
 (3,r"^VER-3|Particulars \|","Q2 FY27, Q1 FY27 (30 June 2026), Q2 FY26, H1 FY27, H1 FY26, FY26 (31 March 2026)","standalone result column periods"),
 (4,r"As at|30 September","30 September 2026 and 31 March 2026","standalone balance sheet dates"),
 (5,r"Particulars","six months ended 30 September 2026 and 2025","standalone cash flow periods"),
 (6,r"held on 16|October 2026","16 October 2026","board and audit committee approval, standalone"),
 (6,r"Date:","16 October 2026","standalone signature date"),
 (7,r"year to date from","April 1, 2026 to September 30, 2026","consolidated review period"),
 (8,r"Date:","October 16, 2026","consolidated review report date"),
 (9,r"^VER-9|Particulars \|","Q2 FY27, Q1 FY27 (30 June 2026), Q2 FY26, H1 FY27, H1 FY26, FY26 (31 March 2026)","consolidated result column periods"),
 (10,r"As at|30 September","30 September 2026 and 31 March 2026","consolidated balance sheet dates"),
 (11,r"Particulars","30 September 2026 and 30 September 2025","consolidated cash flow periods"),
 (12,r"16 October","16 October 2026","board and audit committee approval, consolidated"),
 (12,r"Date:","16 October 2026","consolidated signature date"),
]
qual = [
 (1,r"Un-audited Standalone","Un-audited Standalone and Consolidated Financial Results","results are unaudited"),
 (1,r"Limited Review","Limited Review Reports ... submitted by the Auditors of the Company","limited review, not audit"),
 (1,r"Publication of Extract","Board item b heading reads \"Extract of Audited Financial Results\" while body says Un-audited","wording inconsistency in source"),
 (1,r"inter-alia","Board \"has inter-alia considered and approved the following\" (items a and b only)","agenda scope"),
 (2,r"moderate assurance","review obtains moderate assurance; substantially less in scope than an audit","review scope limit, standalone"),
 (2,r"do not express","Accordingly, we do not express an audit opinion","standalone review report"),
 (2,r"nothing has come","nothing has come to our attention ... material misstatement (unmodified conclusion)","standalone review conclusion"),
 (3,r"crores, unless","(Rs in crores, unless otherwise stated)","standalone P&L unit convention"),
 (3,r"^VER-3 \| EPS \(a\)","Earnings per share (not annualised for the quarters)","EPS qualifier, standalone"),
 (3,r"Audited|Unaudited|STATEMENT OF UNAUDITED","Unaudited for five columns; Audited for year ended 31 March 2026","audit status per column, standalone P&L"),
 (4,r"Notes:1","Notes:1 Unaudited Standalone Statement of Assets and Liabilities (Rs in crores, unless otherwise stated)","balance sheet heading and unit"),
 (5,r"Note:2","Note:2 Unaudited Standalone Statement of Cash Flows (Rs in crores, unless otherwise stated)","cash flow heading and unit"),
 (5,r"Purchase of property","Purchase of property, plant and equipment [including capital work-in-progress, capital advances and creditors]","capex definition, standalone"),
 (5,r"\[net\]","Income taxes refund/(paid) [net]; Movement in current borrowings [net]; Bank balances [net]","net presentation qualifiers, standalone cash flow"),
 (6,r"prepared in accordance","Note 1: results prepared under Ind AS, Section 133 Companies Act 2013, Reg 33 LODR","basis of preparation, standalone"),
 (6,r"reviewed by the Audit","Note 2: reviewed by Audit Committee, approved by Board 16 Oct 2026; statutory auditors carried out limited review","approval and review, standalone"),
 (6,r"one reportable","Note 3: one reportable segment, manufacturing and trading of polyester goods (Ind AS 108)","segment note, standalone"),
 (6,r"more detalls|more details","Note 4: more details at Investor Relations section of website and NSE/BSE sites","reference note, standalone"),
 (7,r"moderate assurance","review obtains moderate assurance; substantially less in scope than an audit","review scope limit, consolidated"),
 (7,r"do not express","Accordingly, we do not express an audit opinion","consolidated review report"),
 (7,r"33 \(8\)|33\(8\)|performed procedures","procedures also performed per SEBI circular under Regulation 33(8), to the extent applicable","consolidated review extra procedure"),
 (8,r"nothing$|nothing ","nothing has come to our attention ... material misstatement (unmodified conclusion)","consolidated review conclusion"),
 (8,r"Subsidiaries","Consolidation covers Holding Company and four subsidiaries","consolidation perimeter"),
 (9,r"crores, unless","(Rs in crores, unless otherwise stated)","consolidated P&L unit convention"),
 (9,r"^VER-9 \| EPS \(a\)","Earnings per share (not annualised for the quarters)","EPS qualifier, consolidated"),
 (9,r"Audited|Unaudited|STATEMENT OF UNAUDITED","Unaudited for five columns; Audited for year ended 31 March 2026","audit status per column, consolidated P&L"),
 (10,r"Note No. 1","Note No. 1: Unaudited Consolidated Statement of Assets and Liabilities (Rs in crores, unless otherwise stated)","balance sheet heading and unit"),
 (11,r"Note No. 2","Note No. 2 : Unaudited Consolidated Statement of Cash Flows (Rs in crores, unless otherwise stated)","cash flow heading and unit"),
 (11,r"Purchase of property","Purchase of property, plant and equipment [including capital work-in-progress, capital advances and creditors]","capex definition, consolidated"),
 (11,r"\[net\]","Income taxes (paid)/refund (net); Movement in current borrowings [net]; Bank balances [net]","net presentation qualifiers, consolidated cash flow"),
 (12,r"prepared in accordance","Note 1: consolidated results prepared under Ind AS, Section 133, Reg 33 LODR","basis of preparation, consolidated"),
 (12,r"Ind AS.{0,3}\) ?110|110","Note 2: prepared per Ind AS 110; reviewed by Audit Committee, approved by Board 16 Oct 2026; limited review by auditors","consolidation and approval note"),
 (12,r"one reportable","Note 3: Group operates in one reportable segment, manufacturing and trading of polyester goods","segment note, consolidated"),
 (12,r"more details","Note 4: more details at Investor Relations section of website and NSE/BSE sites","reference note, consolidated"),
 (3,r"^\[IMAGE-VERIFIED","extractor note: document is a scan; OCR text above the IMAGE-VERIFIED block can differ from the printed values; use the VER- lines","EXTRACTOR_FLAG not source text"),
 (9,r"^\[IMAGE-VERIFIED","extractor note: document is a scan; OCR text above the IMAGE-VERIFIED block can differ from the printed values; use the VER- lines","EXTRACTOR_FLAG not source text"),
]
out = []
def emit(label, items, typ):
    out.append(("## " + label, None));
    for it in items: out.append((typ, it))
secs = []
n = [0]
def rows_of(typ, items):
    return [(typ,)+it for it in items]
numfinal = [(p,l,v,c) for p,l,v,c in numrows]
ents = [(p, find(p,rx), v, c) for p,rx,v,c in ent]
fw = [(p, find(p,rx), v, c) for p,rx,v,c in fwd]
dt = [(p, find(p,rx), v, c) for p,rx,v,c in dates]
ql = [(p, find(p,rx), v, c) for p,rx,v,c in qual]
total = len(numfinal)+len(ents)+len(fw)+len(dt)+len(ql)
o = []
o.append("# A1 STRUCTURED EXTRACTION: Indo Rama Synthetics (India) Ltd (INDORAMA), Q2 FY27, results filing")
o.append("source fulltext: runs/indorama-q2fy27/extracted/indorama-results-q2fy27-fulltext.md (line numbers refer to that file, header included)")
o.append(f"ID range: R001-R{total:03d}")
o.append(f"counts: NUMBER {len(numfinal)} | ENTITY {len(ents)} | FORWARD {len(fw)} | DATE {len(dt)} | QUALIFIER {len(ql)}")
o.append("unit: Rs crores (x1); EPS in Rs; parentheses = negatives; '-' = nil (ZERO_STANDING). Source is a scan: all six financial tables (pages 3, 4, 5, 9, 10, 11) were confirmed against the 300 dpi page images and appear as VER- lines in the fulltext; rows cite those lines and are tagged image-verified. Board Outcome letter has agenda items a and b only, both captured individually.")
o.append("row format: R### | page | line | TYPE | verbatim value | context")
i = 0
for label, typ, items in [("NUMBER","NUMBER",numfinal),("ENTITY","ENTITY",ents),("FORWARD","FORWARD",fw),("DATE","DATE",dt),("QUALIFIER","QUALIFIER",ql)]:
    o.append(""); o.append("## "+label)
    for p,l,v,c in items:
        i += 1
        o.append(f"R{i:03d} | page {p} | line {l} | {typ} | {v} | {c}")
open(B+"extracted/indorama-results-q2fy27-structured.md","w",encoding="utf-8").write("\n".join(o)+"\n")
print(nlines, len(lines), len(numfinal), len(ents), len(fw), len(dt), len(ql), total)
