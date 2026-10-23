import re, sys
FT = '../extracted/supremepwr-results-h1fy27-fulltext.md'
L = open(FT, encoding='utf-8').read().split('\n')   # L[i-1] is line i
pagestart = {}
for i, l in enumerate(L, 1):
    m = re.match(r'^\[page (\d+)\]$', l)
    if m:
        pagestart[int(m.group(1))] = i
pagestart[16] = len(L) + 1
def prange(p):
    return pagestart[p], pagestart[p + 1] - 1
def find(p, pat, last=True, after=None):
    a, b = prange(p)
    hits = [i for i in range(a, b + 1) if re.search(pat, L[i - 1])]
    if after:
        hits = [h for h in hits if h > after]
    if not hits:
        raise SystemExit('NOT FOUND p%d %s' % (p, pat))
    return hits[-1] if last else hits[0]

num = []; ent = []; fwd = []; dat = []; qual = []

TOK = re.compile(r'(\(?-?[\d,]+\.\d+\)?|\(?-?\d[\d,]*\)?(?=\s|$)|(?<=\s)-(?=\s|$))')
def tabrows(page, cols, ctxprefix):
    a, b = prange(page)
    # block starts after the OCR marker
    st = [i for i in range(a, b + 1) if L[i - 1].startswith('[OCR page')][0] + 1
    i = st
    section = ''
    pending = None
    while i <= b:
        line = L[i - 1]
        if line.startswith('Columns:') or not line.strip() or line.startswith('Particulars') or line.startswith('STANDALONE STATEMENT') or line.startswith('CONSOLIDATED STATEMENT') or line.startswith('(Paid up') or line.startswith('Figures of') or line.startswith('Place:') or line.startswith('Notes:') or line.startswith('(ii)'):
            i += 1; continue
        # strip trailing values
        toks = []
        rest = line.rstrip()
        while True:
            m = re.search(r'\s+(\(?-?[\d,]+\.\d+\)?|\(?-?\d[\d,]*\)?|-)$', rest)
            if m and len(toks) < len(cols):
                toks.insert(0, m.group(1)); rest = rest[:m.start()]
            else:
                break
        label = rest.strip()
        if label.startswith('(no value'):
            label = label
        if len(toks) == len(cols):
            lab = pending if (label == '' and pending) else label
            pending = None
            for c, t in zip(cols, toks):
                num.append((page, i, t, '%s, %s %s' % (lab.strip(), c, ctxprefix), t == '-'))
        elif len(toks) == 0:
            pending = label
        else:
            # partial values: label with fewer tokens, pad skip
            for c, t in zip(cols[-len(toks):], toks):
                num.append((page, i, t, '%s, %s %s' % (label, c, ctxprefix), t == '-'))
        i += 1

SA = ['H1 FY27 (HY ended 30-Sep-2026)', 'H2 FY26 (HY ended 31-Mar-2026)', 'H1 FY26 (HY ended 30-Sep-2025)', 'FY26 (year ended 31-Mar-2026)']
BS = ['as at 30-Sep-2026', 'as at 31-Mar-2026']
CF = ['H1 FY27 (HY ended 30-Sep-2026)', 'FY26 (year ended 31-Mar-2026)']
tabrows(4, SA, 'standalone P&L')
tabrows(5, BS, 'standalone balance sheet')
tabrows(7, CF, 'standalone cash flow')
tabrows(10, SA, 'consolidated P&L')
tabrows(11, BS, 'consolidated balance sheet')
tabrows(13, CF, 'consolidated cash flow')

# ---------------- manual rows ----------------
def N(p, pat, val, ctx, zero=False):
    num.append((p, find(p, pat), val, ctx, zero))
def E(p, pat, val, ctx):
    ent.append((p, find(p, pat), val, ctx))
def F(p, pat, val, ctx):
    fwd.append((p, find(p, pat), val, ctx))
def D(p, pat, val, ctx):
    dat.append((p, find(p, pat), val, ctx))
def Q(p, pat, val, ctx, flag=''):
    qual.append((p, find(p, pat), val, ctx, flag))

# NUMBER (narrative, non-table)
N(1, r'Date: 16\.10\.2026', '16.10.2026', 'date of outcome letter as number')
N(1, r'400051', '400051', 'NSE address pin code')
N(3, r'Registration No: 0136235', '0136235', 'auditor firm registration no. as read, standalone LRR')
N(3, r'Membership No\.238452', '238452', 'partner membership no., standalone LRR')
N(3, r'UDIN : 26238452HYPQTBY855', '26238452HYPQTBY855', 'UDIN standalone LRR')
N(3, r'020690', '020690', 'peer review certificate no., standalone LRR')
N(2, r'SRE\) 2410', '2410', 'SRE standard number, standalone LRR')
N(2, r'AS 25', '25', 'AS 25 Interim Financial Reporting, standalone LRR')
N(3, r'CIR/CFD/CMD1/44/2019', '44/2019', 'SEBI circular number, standalone LRR')
N(9, r'CIR/CFD/CMD1/44/2019', '44/2019', 'SEBI circular number, consolidated LRR')
N(9, r'Registration No: 013623S', '013623S', 'firm registration no. as read, consolidated LRR')
N(9, r'UDIN: 262384520LVCDF9963', '262384520LVCDF9963', 'UDIN consolidated LRR')
N(9, r'Membership No\.238452', '238452', 'partner membership no., consolidated LRR')
N(9, r'020690', '020690', 'peer review certificate no., consolidated LRR')
N(12, r'holds a 90% share', '90%', 'Holding Company share in profits/losses of Danya Electric Company')
N(12, r'Rajmohan 7\.5%', '7.5%', 'Mr. Vee Rajmohan partner share in Danya Electric Company')
N(12, r'2\.5%', '2.5%', 'Mr. K.V. Pradeep Kumar partner share in Danya Electric Company')
N(6, r'12,47,000', '12,47,000', 'convertible equity share warrants allotted 27-Aug-2025 (standalone note 3)')
N(6, r'Rs 169', 'Rs 169', 'issue price per warrant (standalone note 3)')
N(6, r'42\.25', 'Rs 42.25 (25% of issue price)', 'warrant subscription price per warrant (standalone note 3)')
N(6, r'126 75', 'Rs 126.75 (75% of issue price)', 'warrant exercise price per warrant (standalone note 3)')
N(6, r'5,26,85,750', 'Rs 5,26,85,750', 'subscription amount received on warrants (standalone note 3)')
N(6, r'Rs\. 10 upon', 'Rs 10', 'face value of equity share on warrant conversion (standalone note 3)')
N(6, r'Rs\.126\.75 per warrant', 'Rs 126.75 per warrant', 'balance payable on exercise per warrant (standalone note 3)')
N(6, r'18 months', '18 months', 'warrant conversion window from allotment date (standalone note 3)')
N(14, r'2,107\.43 Lakhs', 'Rs 2,107.43 Lakhs', 'original allocation amount, Utilization of Funds Certificate')
N(14, r'526\.86 Lakhs', 'Rs 526.86 Lakhs', '25% subscription received on original allocation, certificate')
N(14, r'25% from the original', '25%', 'subscription received share of original allocation, certificate')
N(14, r'520\.31', '520.31', 'actual utilised amount till 30-09-26, Rs Lakhs, certificate (column read from OCR)')
N(14, r'6\.55', '6.55', 'unutilised amount as on 30-09-26, Rs Lakhs, certificate (column read from OCR)')
N(14, r'NSE/CML/2024/23', 'NSE/CML/2024/23', 'NSE circular number cited in certificate')
N(15, r'5,26,85,750\s*$|Rs\. 5,26,85,750', 'Rs. 5,26,85,750', 'proceeds received 27.08.2025 upfront 25%, certificate list')
N(15, r'12,47,000', '12,47,000', 'convertible warrants allotted, certificate note 1')
N(15, r'Rs\.169', 'Rs.169', 'issue price per warrant, certificate note 1')
N(15, r'Rs\.42\.25', 'Rs.42.25 (25% of issue price)', 'subscription price per warrant, certificate note 1')
N(15, r'Rs\.126\.75 \(75%', 'Rs.126.75 (75% of issue price)', 'warrant exercise price per warrant, certificate note 1')
N(15, r'5,26,85,750/-', 'Rs.5,26,85,750/-', 'subscription amount received at reporting date, certificate note 1')
N(15, r'126\.75 per warrant', '126.75 per warrant', 'balance payable on conversion, certificate note 1')
N(15, r'^months from', '18 months', 'conversion window from allotment, certificate note 1')
N(15, r'0136238', '0136238', 'firm registration no. as read, certificate')
N(15, r'020690', '020690', 'peer review certificate no., certificate')
N(15, r'Membership Number: 238452', '238452', 'partner membership no., certificate')
N(15, r'UDIN', '26238452QAPRXM5385', 'UDIN of certificate')

# ENTITY
E(1, r'National Stock Exchange', 'National Stock Exchange of India Limited (NSE)', 'recipient of disclosure; listing venue')
E(1, r'SUPREMEPWR', 'SUPREMEPWR', 'NSE trading symbol')
E(1, r'For Supreme Power Equipment Limited', 'Supreme Power Equipment Limited', 'company filing the disclosure')
E(1, r'Priyanka Bansal$', 'Priyanka Bansal, Company Secretary and Compliance Officer', 'signatory of outcome letter')
E(1, r'Statutory Auditors', 'Statutory Auditors of the Company', 'issued Limited Review Report')
E(1, r'Regulation 30', 'SEBI (LODR) Regulations 2015, Regulations 30, 32, 33', 'regulatory basis of disclosure')
E(2, r'PP NAND COMPANY', 'P P N and Company, Chartered Accountants, Chennai', 'statutory auditor (letterhead)')
E(3, r'R\. RAJARAM', 'R. Rajaram, Partner, Membership No. 238452', 'signing partner of auditor')
E(2, r'Securities and Exchange Board of', 'Securities and Exchange Board of India', 'regulator cited in LRR')
E(4, r'SIDCO Industrial', 'No.55, SIDCO Industrial Estates, Thirumazhisai, Tiruvallur 600124', 'registered office address')
E(4, r'supremepower', 'cs@supremepower.in; www.supremepower.in; +91 44 26811221', 'company contact details')
E(5, r'VEE RAJMOHAN', 'Vee Rajmohan, Managing Director, DIN 00844400', 'signatory for the Board')
E(8, r'PP NAND COMPANY', 'P P N and Company (consolidated LRR)', 'statutory auditor on consolidated LRR')
E(9, r'Danya Electric Company', 'Danya Electric Company', 'subsidiary included in consolidation (AS 21), partnership firm')
E(12, r'Danya Electric Company, a partnership', 'Danya Electric Company, partnership firm; only subsidiary', 'subsidiary of Holding Company')
E(12, r'Rajmohan 7\.5%', 'Mr. Vee Rajmohan (other partner, 7.5%)', 'partner in Danya Electric Company')
E(12, r'Pradeep', 'Mr. K.V. Pradeep Kumar (other partner, 2.5%)', 'partner in Danya Electric Company')
E(6, r'Promoter & Promoter Group', '"Promoter & Promoter Group" and "Non-Promoter" allottees', 'warrant allottees')
E(6, r'Extra-Ordinary General Meeting', 'Extra-Ordinary General Meeting 14-Jul-2025', 'approved warrant issue')
E(6, r'Ministry of Corporate Affairs', 'Ministry of Corporate Affairs', 'regulator cited for AS and SME Ind AS exemption')
E(6, r'regulauions|regulations, and holders|ICDR', 'SEBI ICDR Regulations 2018', 'governs warrant conversion period')
E(14, r'CHARTERED ACCOUNTANTS', 'P P N and Company, Chartered Accountants, Nungambakkam, Chennai 600034', 'auditor issuing utilisation certificate')
E(14, r'The Board of Directors', 'Board of Directors, Supreme Power Equipment Limited', 'addressee of certificate')
E(14, r'Sub: Certificate', 'Preferential Issue of Convertible Warrants', 'instrument whose proceeds are certified')
E(14, r'NSE/CML/2024/23', 'NSE Circular NSE/CML/2024/23', 'basis of certificate')
E(14, r'Thirumazhisai, Thiruvallur', 'No.55, SIDCO Industrial Estate, Thirumazhisai, Thiruvallur 600124', 'company address in certificate')
E(15, r'Peer Review', 'Peer Review Certificate No. 020690', 'auditor credential')
E(15, r'Partner', 'R. Rajaram, Partner, Membership No. 238452', 'signatory of certificate')

# FORWARD
F(6, r'balance amount will be payable', 'The balance amount will be payable upon the exercise of the warrants', 'standalone note 3: balance Rs 126.75 per warrant on exercise')
F(6, r'18 months', 'Conversion can occur in one or more tranches within 18 months from the date of allotment', 'standalone note 3: warrant conversion window')
F(6, r'may exercise their right', 'holders may exercise their right to convert the warrants into equity shares within this period', 'standalone note 3: warrant exercise')
F(6, r'consequent adjustments', 'consequent adjustments, if any, will be accounted for in the year of confirmation and / or reconciliation', 'standalone note 4')
F(12, r'consequent adjustments', 'consequent adjustments, if any, will be accounted for in the year of confirmation and / or reconciliation', 'consolidated note 5')
F(15, r'balance amount will be payable', 'The balance amount will be payable upon the exercise of the warrants', 'certificate note 1')
F(15, r'^months from', 'Conversion can occur in one or more tranches within 18 months from the date of allotment', 'certificate note 1')
F(15, r'may exercise their right', 'holders may exercise their right to convert the warrants into equity shares within this period', 'certificate note 1')

F(14, r"To augment the fund", "Object of issue: to augment fund requirement for establishment and development of Factory premises, Working Capital Requirements and General Corporate Purposes", "certificate objects table, use of warrant proceeds")

# DATE
D(1, r'Date: 16\.10\.2026', '16.10.2026', 'date of outcome letter')
D(1, r'Friday, October 16th 2026\.', 'Friday, October 16th 2026', 'board meeting date')
D(1, r'02:30', '02:30 p.m. to 04:30 p.m.', 'board meeting commenced and concluded times')
D(1, r'Half Year ended 30th September, 2026', 'Half Year ended 30th September, 2026', 'period of results approved')
D(1, r'half-year ended September 30, 2026', 'half-year ended September 30, 2026', 'period of deviation statement')
D(1, r'Date: 2026\.10\.16', '2026.10.16 (digital signature 16:37:54 +05:30)', 'CS digital signature date and time')
D(2, r'half year ended', 'half year ended September 30, 2026', 'LRR review period, standalone')
D(3, r'March 29, 2019', 'March 29, 2019', 'date of SEBI circular cited in LRR')
D(3, r'Date :16-10-2026', '16-10-2026', 'standalone LRR date')
D(9, r'Date :16-10-2026', '16-10-2026', 'consolidated LRR date')
D(9, r'March 29, 2019', 'March 29, 2019', 'date of SEBI circular cited, consolidated LRR')
D(4, r'30TH SEPTEMBER, 2026', 'half year ended 30th September 2026', 'standalone P&L period')
D(5, r'30TH SEPTEMBER, 2026', 'as at 30th September 2026', 'standalone balance sheet date')
D(5, r'Date: 16-10-2026', '16-10-2026', 'standalone balance sheet signing date')
D(6, r'16-10-2026', '16-10-2026', 'date results approved by Board (standalone note 1)')
D(6, r'February 16, 2015', 'February 16, 2015', 'MCA notification date (standalone note 2)')
D(6, r'August 27, 2025', 'August 27, 2025', 'warrant allotment date (standalone note 3)')
D(6, r'July 14, 2025', 'July 14, 2025', 'EGM date approving warrants (standalone note 3)')
D(7, r'SEPTEMBER 30, 2026', 'half year ended September 30, 2026', 'standalone cash flow period')
D(10, r'SEPTEMBER 30, 2026', 'half year ended September 30, 2026', 'consolidated P&L period')
D(11, r'30TH SEPTEMBER, 2026', 'as at 30th September 2026', 'consolidated balance sheet date')
D(12, r'16-10-2026', '16-10-2026', 'date results approved by Board (consolidated note 1)')
D(12, r'February 16, 2015', 'February 16, 2015', 'MCA notification date (consolidated note 2)')
D(12, r'half year ended September 30, 2026', 'half year ended September 30, 2026', 'subsidiary results period (consolidated note 4)')
D(13, r'SEPTEMBER 30, 2026', 'half year ended September 30, 2026', 'consolidated cash flow period')
D(14, r'up to September 30, 2026', 'up to September 30, 2026', 'period to which utilisation certified')
D(14, r'September 05, 2024', 'September 05, 2024', 'date of NSE circular NSE/CML/2024/23')
D(14, r'30-09-26', '30-09-26', 'date for unutilised amount')
D(15, r'27\.08\.2025', '27.08.2025', 'date of receipt of 25% warrant proceeds')
D(15, r'August 27, 2025', 'August 27, 2025', 'warrant allotment date')
D(15, r'July 14, 2025', 'July 14, 2025', 'EGM date')
D(15, r'Date: 16-10-2026', '16-10-2026', 'certificate date')
D(15, r'^ended September 30, 2026', 'half year ended September 30, 2026', 'no-deviation statement period')

# QUALIFIER
Q(1, r'Un-Audited Financial Results', 'Un-Audited Financial Results (Standalone and Consolidated) ... along with the Limited Review Report', 'results are unaudited, limited-reviewed')
Q(1, r'Statement of Deviations', 'Statement of Deviations / Variations for proceeds of Preferential Issue of Convertible Warrants for half-year ended 30-Sep-2026, with Statutory Auditor certificate', 'Reg 32 statement scope')
Q(1, r'Digitally signed', 'Digitally signed by Priyanka Bansal', 'signature qualifier on outcome letter')
Q(2, r'recognition and measurement principles', 'prepared under AS 25 Interim Financial Reporting (Section 133 Companies Act 2013)', 'standalone LRR basis of preparation')
Q(2, r'moderate', 'review gives moderate assurance; substantially less in scope than an audit', 'standalone LRR scope')
Q(3, r'do not express an audit opinion', 'we have not performed an audit and accordingly, we do not express an audit opinion', 'standalone LRR')
Q(3, r'nothing has come to our attention', 'nothing has come to our attention that causes us to believe ... material misstatement', 'standalone LRR conclusion (no modification)')
Q(9, r'based solely', 'unaudited interim financial results of this subsidiary ... is based solely on such unaudited interim financial results', 'consolidated LRR: subsidiary results unaudited, relied upon')
Q(9, r'statement provided by the management', 'based on the statement provided by the management related to Parent & Subsidiary', 'consolidated LRR basis')
Q(8, r'moderate', 'review gives moderate assurance; substantially less in scope than an audit', 'consolidated LRR scope')
Q(8, r'do not express an audit opinion', 'Accordingly, we do not express an audit opinion', 'consolidated LRR')
Q(9, r'nothing has come to our attention', 'nothing has come to our attention ... material misstatement', 'consolidated LRR conclusion (no modification)')
Q(4, r'All Amounts are in Rs\. Lakhs', '(All Amounts are in Rs. Lakhs except for No. of Shares & EPS)', 'unit qualifier, standalone P&L')
Q(4, r'Columns:', 'Columns: H1 FY27, H2 FY26, H1 FY26 Unaudited; FY26 Audited', 'audit status of standalone P&L columns')
Q(4, r'Paid up Equity Share Capital row', 'Paid up Equity Share Capital row carries no value in the standalone P&L image', 'A1 extraction note', 'A1_NOTE')
Q(5, r'All Amounts are in Rs\. Lakhs', '(All Amounts are in Rs. Lakhs)', 'unit qualifier, standalone balance sheet')
Q(5, r'rearranged / reclassified', 'Figures of the previous period / year have been rearranged / reclassified wherever necessary', 'standalone balance sheet footnote')
Q(6, r'Notes on Standalone', 'Notes on Standalone Financial Results (notes 1-8)', 'heading of standalone notes')
Q(6, r'reviewed by the Audit Committee', 'Note 1: results reviewed by Audit Committee, approved by Board 16-10-2026; Limited Review by Statutory Auditors; prepared under Accounting Standards (AS)', 'standalone note 1')
Q(6, r'exempted from', 'Note 2: SME-listed companies exempt from compulsory adoption of Ind AS (MCA notification 16-Feb-2015)', 'standalone note 2')
Q(6, r'On August 27, 2025', 'Note 3: 12,47,000 convertible warrants allotted at Rs 169; 25% (Rs 42.25) received; balance 75% (Rs 126.75) on exercise; conversion within 18 months', 'standalone note 3')
Q(6, r'subjected to confirmation', 'Note 4: Trade Payables, Loans and Advances, Other Current Liabilities are subject to confirmation and reconciliation', 'standalone note 4')
Q(6, r'one business segment', 'Note 5: single business segment; segment disclosure not applicable', 'standalone note 5')
Q(6, r'EPS for the respective', 'Note 6: EPS computed on weighted average shares by days; sum of half-year EPS may not reconcile with annual EPS', 'standalone note 6')
Q(6, r'figures for the corresponding', 'Note 7: previous period figures regrouped / reclassified wherever necessary', 'standalone note 7')
Q(6, r'no exceptional', 'Note 8: no exceptional and extra-ordinary items for the reporting period', 'standalone note 8')
Q(7, r'^Columns:', 'Standalone cash flow columns: 30-Sep-2026 Unaudited, 31-Mar-2026 Audited (headers say "As at")', 'audit status of standalone cash flow')
Q(7, r'All Amounts are in Rs\.', '(All Amounts are in Rs. Lakhs)', 'unit qualifier, standalone cash flow')
Q(7, r'skewed', 'values assigned to labels by row order (image rows slightly skewed)', 'A1 extraction note on standalone cash flow table', 'A1_NOTE')
Q(7, r'^Notes: \(i\)', 'Notes (i): figures in brackets are outflows / deductions', 'standalone cash flow note')
Q(7, r'^\(ii\) The above', 'Notes (ii): cash flow statement prepared under the Indirect Method per AS-3', 'standalone cash flow note')
Q(10, r'Rs\. in Lakhs except', '(Rs. in Lakhs except for No. of Shares & EPS)', 'unit qualifier, consolidated P&L')
Q(10, r'^Columns:', 'Columns: H1 FY27, H2 FY26, H1 FY26 Unaudited; FY26 Audited', 'audit status of consolidated P&L columns')
Q(10, r'^VIII Extraordinary', 'Extraordinary Items row: first column blank in image, other three columns "-"', 'A1 extraction note on consolidated P&L', 'A1_NOTE')
Q(11, r'Rs\. in Lakhs', 'Rs. in Lakhs', 'unit qualifier, consolidated balance sheet')
Q(11, r'^Figures of', 'Figures of the previous period / year have been rearranged / reclassified wherever necessary', 'consolidated balance sheet footnote')
Q(12, r'Notes on Consolidated', 'Notes on Consolidated Financial Results (notes 1-9)', 'heading of consolidated notes')
Q(12, r'reviewed by the Audit Committee', 'Note 1: results reviewed by Audit Committee, approved by Board 16-10-2026; limited review carried out; prepared under Accounting Standards (AS)', 'consolidated note 1')
Q(12, r'exempted from', 'Note 2: SME-listed companies exempt from compulsory adoption of Ind AS', 'consolidated note 2')
Q(12, r'consolidated financial results include', 'Note 3: AS 21 consolidation of Holding Company and only subsidiary Danya Electric Company (partnership, 90% profit share; Mr. Vee Rajmohan 7.5%, Mr. K.V. Pradeep Kumar 2.5%); line-by-line; inter-company items eliminated; minority interest = other partners share', 'consolidated note 3')
Q(12, r'reviewed by the Statutory Auditors / certified', 'Note 4: subsidiary results unaudited and "[reviewed by the Statutory Auditors / certified by the management]" (bracketed alternatives left unresolved in filed text)', 'consolidated note 4', 'UNRESOLVED_PLACEHOLDER')
Q(12, r'confirmation and reconciliation|subjected to confirmation|are subjected', 'Note 5: Trade Payables, Loans and Advances, Other Current Liabilities are subject to confirmation and reconciliation', 'consolidated note 5')
Q(12, r'EPS for the respective', 'Note 6: EPS by weighted average shares by days; sum of half-year EPS may not reconcile with annual EPS', 'consolidated note 6')
Q(12, r'one business Segment', 'Note 7: single business segment; segment disclosure not applicable', 'consolidated note 7')
Q(12, r'figures for the corresponding', 'Note 8: previous period figures regrouped / reclassified wherever necessary', 'consolidated note 8')
Q(12, r'no exceptional', 'Note 9: no exceptional and extra-ordinary items for the reporting period', 'consolidated note 9')
Q(13, r'Rs\. in Lakhs', 'Rs. in Lakhs', 'unit qualifier, consolidated cash flow')
Q(13, r'^Columns:', 'Consolidated cash flow columns: HY ended 30-Sep-2026 Unaudited, year ended 31-Mar-2026 Audited', 'audit status of consolidated cash flow')
Q(13, r'^Notes: \(i\)', 'Notes (i): figures in brackets are outflows / deductions', 'consolidated cash flow note')
Q(13, r'^\(ii\) The above', 'Notes (ii): cash flow statement prepared under the Indirect Method per AS-3', 'consolidated cash flow note')
Q(15, r'no deviation', 'there has been no deviation(s) or variation(s) in the use of Preferential Issue of Convertible Warrants proceeds for the half year ended September 30, 2026', 'certificate conclusion')
Q(14, r'we hereby certify', 'certification based on review of documents, statements, papers, books of accounts of the Company; expenditure incurred up to September 30, 2026', 'certificate basis')
Q(14, r'Original allocation', 'a. Original allocation amount Rs 2,107.43 Lakhs; b. Subscription received 25% of original allocation = Rs 526.86 Lakhs', 'certificate allocation qualifier')
Q(14, r'Nil', 'Remarks: Nil (token read from OCR on the same row as 520.31 and 6.55)', 'certificate remarks column')
Q(15, r'^Notes:-', 'Notes:- (certificate note heading; note 1 on warrant allotment terms)', 'certificate note heading')
Q(15, r'As of the reporting date', 'As of the reporting date the Company has received Rs.5,26,85,750/- representing the subscription amount (25% of issue price)', 'certificate note 1')
Q(15, r'Each warrant entitles', 'Each warrant entitles holder to apply for one fully paid-up equity share of face value Rs 10 upon payment of balance Rs.126.75; conversion within 18 months per SEBI ICDR 2018', 'certificate note 1')

# ------------ write structured -------------
rid = 0
def nid():
    global rid
    rid += 1
    return 'R%03d' % rid
out = []
def emit(title, items, fmt):
    out.append('## %s' % title)
    for it in items:
        out.append(fmt(nid(), it))
    out.append('')
num.sort(key=lambda r: (r[0], r[1]))
emit('NUMBER', num, lambda i, r: '%s | page %d | line %d | NUMBER | %s | %s%s' % (i, r[0], r[1], r[2], r[3], ' | ZERO_STANDING' if r[4] else ''))
for t, items in (('ENTITY', ent), ('FORWARD', fwd), ('DATE', dat)):
    items.sort(key=lambda r: (r[0], r[1]))
    emit(t, items, lambda i, r, t=t: '%s | page %d | line %d | %s | %s | %s' % (i, r[0], r[1], t, r[2], r[3]))
qual.sort(key=lambda r: (r[0], r[1]))
emit('QUALIFIER', qual, lambda i, r: '%s | page %d | line %d | QUALIFIER | %s | %s%s' % (i, r[0], r[1], r[2], r[3], (' | ' + r[4]) if r[4] else ''))
hdr = ['# A1 STRUCTURED EXTRACTION: SUPREMEPWR results H1 FY27 (SupremePower_H1FY27_Results.pdf)',
       'Source fulltext: runs/supremepwr-h1fy27/extracted/supremepwr-results-h1fy27-fulltext.md (line numbers refer to that file; table rows anchor to the verified OCR block of each page)',
       'Units: Rs Lakhs (x0.01 to Rs Crores); values verbatim, not converted. Brackets = negatives as filed.',
       'ROW ID range: R001-R%03d' % rid,
       'Counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d' % (len(num), len(ent), len(fwd), len(dat), len(qual)),
       'Row format: R### | page N | line L | TYPE | verbatim value | context',
       '']
open('../extracted/supremepwr-results-h1fy27-structured.md', 'w', encoding='utf-8').write('\n'.join(hdr + out) + '\n')
print(rid, len(num), len(ent), len(fwd), len(dat), len(qual))
