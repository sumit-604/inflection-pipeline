import re, subprocess, sys, os
D = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(D, '..', '..', 'inputs', 'Aequs_Q2FY27_Results.pdf')
OUTF = os.path.join(D, '..', '..', 'extracted', 'aequs-results-q2fy27-fulltext.md')
OUTS = os.path.join(D, '..', '..', 'extracted', 'aequs-results-q2fy27-structured.md')
raw = open(os.path.join(D, 'raw.txt'), encoding='utf-8', errors='replace').read().split('\f')
raw = [p for p in raw if p.strip() != '' or False]
# raw pages (text) in order = pdf pages 1,6,7,13,14,15,16
textmap = {1: raw[0], 6: raw[1], 7: raw[2], 13: raw[3], 14: raw[4], 15: raw[5], 16: raw[6]}
imgpages = [2, 3, 4, 5, 8, 9, 10, 11, 12]
body = []
for p in range(1, 17):
    body.append('[page %d]' % p)
    if p in textmap:
        t = textmap[p].strip('\n')
        body.extend([l.rstrip() for l in t.split('\n')])
    else:
        t = open(os.path.join(D, 't%d.txt' % p), encoding='utf-8').read().strip('\n')
        body.extend(t.split('\n'))
HDRN = 20  # header lines count placeholder, fixed below
header_tpl = """=== A1 EXTRACTION HEADER ===
source_filename: Aequs_Q2FY27_Results.pdf
doctype: results
page_count_pdfinfo: 16
formfeed_count: 7 (pdftotext text layer; 9 further pages are image-only, see rendered_pages)
line_count: {lc}
unit_convention: Millions (all financial statements: "Rs in Millions, except per share data"; LRR text also quotes INR million)
conversion_factor_to_cr: Millions -> x0.1 (Rs Mn x 0.1 = Rs Crores)
text_layer_present: yes (pdffonts lists embedded SegoeUI fonts; pages 1, 6, 7, 13, 14, 15, 16 carry text; pages 2, 3, 4, 5, 8, 9, 10, 11, 12 yield zero characters)
extraction_mode: text-only for pages 1, 6, 7, 13-16; OCR + visual transcription for the nine image-only pages (narrow exception: they hold the financial statements)
render_candidates: [2 standalone P&L: zero chars, data-bearing; 3 standalone balance sheet: zero chars, data-bearing; 4 standalone cash flow: zero chars, data-bearing; 5 standalone notes: zero chars, text only; 8 consolidated P&L: zero chars, data-bearing; 9 consolidated balance sheet: zero chars, data-bearing; 10 consolidated cash flow: zero chars, data-bearing; 11 consolidated segment: zero chars, data-bearing; 12 consolidated notes: zero chars, text only]
rendered_pages: [2, 3, 4, 5, 8, 9, 10, 11, 12 (pdftoppm -r 200 + tesseract --psm 6; none of the nine pages has any text layer, they are scanned image pages holding the financial statements, so rendering was necessary). Tesseract output was garbled on every table page (2, 3, 4, 8, 9, 10, 11), so those seven pages were transcribed from the rendered image by visual reading; pages 5 and 12 are text-only notes (page 5 from OCR with glyph fixes, page 12 from visual reading). The text-layer spot check found no garbled text on pages 1, 6, 7, 13-16.]
page_coverage: 100%
detected_quarter: Q2 FY27 (quarter and six months ended 30-Sep-2026)
extraction_date: 2026-10-28
=== END HEADER ===
"""
def build_full(lc):
    h = header_tpl.format(lc=lc).rstrip('\n').split('\n')
    return h
h0 = build_full(0)
lc = len(h0) + len(body)
h = build_full(lc)
assert len(h) == len(h0)
full = h + body
# line_count should be total file lines
total = len(full)
h = build_full(total)
full = h + body
open(OUTF, 'w', encoding='utf-8').write('\n'.join(full) + '\n')
lines = full
pg_start = {}
cur = None
for i, l in enumerate(lines, 1):
    m = re.match(r'^\[page (\d+)\]$', l)
    if m:
        pg_start[int(m.group(1))] = i
pg_end = {}
for p in range(1, 17):
    pg_end[p] = (pg_start[p + 1] - 1) if p < 16 else len(lines)

def find(page, key):
    for i in range(pg_start[page], pg_end[page] + 1):
        if key in lines[i - 1]:
            return i
    sys.stderr.write('NOT FOUND p%d: %s\n' % (page, key))
    return pg_start[page]

rows = {'NUMBER': [], 'ENTITY': [], 'FORWARD': [], 'DATE': [], 'QUALIFIER': []}
def add(t, page, line, val, ctx, flag=''):
    rows[t].append((page, line, val, ctx, flag))
def M(t, page, key, val, ctx, flag=''):
    add(t, page, find(page, key), val, ctx, flag)

# ---- table-driven NUMBER rows
cur_cols = None; ctx = ''
for p in range(1, 17):
    for i in range(pg_start[p], pg_end[p] + 1):
        l = lines[i - 1]
        if l.startswith('#COLS:'):
            cur_cols = [c.strip() for c in l[6:].split('|')]
        elif l.startswith('#CTX:'):
            ctx = l[5:].strip()
        elif ' | ' in l and cur_cols and p in (2, 3, 4, 8, 9, 10, 11):
            parts = [x.strip() for x in l.split(' | ')]
            label = parts[0]
            vals = parts[1:]
            for c, v in zip(cur_cols, vals):
                if v == '':
                    continue
                flag = 'ZERO_STANDING' if v in ('-', '0.00', '(0.00)') else ''
                add('NUMBER', p, i, v, '%s %s, %s' % (ctx, label[:70], c.split(' (')[0]), flag)
# keep column-label rows: periods listed in header rows below

# ---- remaining NUMBER rows (text pages and notes)
N = lambda p, k, v, c, f='': M('NUMBER', p, k, v, c, f)
N(1, 'BSE Scrip Code', '544634', 'BSE scrip code')
N(1, 'Membership Number', 'A20823', 'CS membership number')
N(1, 'T: + 91 080', '+ 91 080 61348000', 'registered office telephone')
N(1, 'T: +91 0831', '+91 0831 4222500', 'corporate office telephone')
N(1, 'Corporate Identity Number', 'L30305KA2000PLC026760', 'CIN')
N(1, '14:50 HRS', '14:50 HRS IST', 'board meeting commenced')
N(1, '14:50 HRS', '15:35 HRS IST', 'board meeting concluded')
N(1, 'Regulation 33 and Regulation 30', 'Regulation 33; Regulation 30', 'SEBI LODR regulations cited')
for key, v, c in [('4. Based', '', '')]:
    pass
N(6, 'Registration No. BA61223', 'BA61223', 'BSR & Co partnership registration')
N(6, 'AAB-8181', 'AAB-8181', 'BSR & Co LLP registration')
N(6, 'Telephone: +91 80', '+91 80 4682 3000', 'BSR telephone')
N(6, 'Fax:', '+91 80 4682 3999', 'BSR fax')
N(7, "Firm's Registration", '101248W/W-100022', 'BSR firm registration, standalone LRR')
N(7, 'Membership No.', '060573', 'auditor partner membership, standalone LRR')
N(7, 'UDIN', '26060573JYKDQR9325', 'UDIN standalone LRR')
N(13, 'Registration No. BA61223', 'BA61223', 'BSR & Co partnership registration, consolidated LRR')
N(13, 'AAB-8181', 'AAB-8181', 'BSR & Co LLP registration, consolidated LRR')
N(13, 'Telephone: +91 80', '+91 80 4682 3000', 'BSR telephone')
N(13, 'Fax:', '+91 80 4682 3999', 'BSR fax')
N(13, 'SRE) 2410', 'SRE 2410', 'review standard cited')
N(6, 'SRE) 2410', 'SRE 2410', 'review standard cited, standalone LRR')
N(6, '34 "Interim', 'Ind AS 34', 'accounting standard cited, standalone LRR')
N(13, '34 "Interim', 'Ind AS 34', 'accounting standard cited, consolidated LRR')
N(14, 'INR 1,293.62', 'INR 1,293.62 million', 'unreviewed subsidiary total assets at 30-Sep-2026 (before consolidation adjustments)')
N(14, 'INR 324.99', 'INR 324.99 million', 'unreviewed subsidiary revenue, quarter ended 30-Sep-2026 (before consolidation adjustments)')
N(14, 'INR 324.99', 'INR 712.44 million', 'unreviewed subsidiary revenue, 1-Apr to 30-Sep-2026 (before consolidation adjustments)')
N(14, 'million and INR 73.86', 'INR 30.81 million', 'unreviewed subsidiary net loss after tax, quarter (before consolidation adjustments)')
N(14, 'million and INR 73.86', 'INR 73.86 million', 'unreviewed subsidiary net loss after tax, 1-Apr to 30-Sep-2026')
N(14, 'million and INR 73.86', 'INR 30.81 million', 'unreviewed subsidiary total comprehensive loss, quarter')
N(14, 'million and INR 73.86', 'INR 73.86 million', 'unreviewed subsidiary total comprehensive loss, 1-Apr to 30-Sep-2026')
N(14, 'Rs. 5.98 million', 'Rs. 5.98 million', 'unreviewed subsidiary net cash outflow, 1-Apr to 30-Sep-2026')
N(14, "Firm's Registration", '101248W/W-100022', 'BSR firm registration, consolidated LRR')
N(14, 'Membership No.', '060573', 'auditor partner membership, consolidated LRR')
N(14, 'UDIN', '26060573PSWXHT1975', 'UDIN consolidated LRR')
N(14, 'Page 2 of 4', '4', 'consolidated LRR page count')
N(15, 'Annexure I', '22', 'entities in Annexure I (rows 1-22)')
# notes page 5
N(5, 'reversed the past impairment', 'Rs 234.39', 'FY26 impairment reversal on SQuAD investment (standalone, Mn)')
N(5, 'Rs 476.22', 'Rs 476.22 Mn', 'FY26 IPO expenses incl Pre-IPO (standalone)')
N(5, 'Rs 476.22', 'Rs 39.02 Mn', 'IPO expenses expensed as exceptional loss')
N(5, 'Rs 476.22', 'Rs 437.20 Mn', 'IPO expenses reduced from securities premium (stated "balance")') if False else None
N(5, 'Mn has been expensed', 'Rs 437.20 Mn', 'IPO expenses reduced from Securities Premium (standalone)')
N(5, 'consolidating 29', '29', 'existing labour laws consolidated into four Labour Codes')
N(5, 'consolidating 29', '4', 'number of Labour Codes notified')
N(5, 'gratuity of', 'Rs 7.92 Mn', 'incremental gratuity impact, FY26 (standalone)')
N(5, 'up to 28,071,690', '28,071,690', 'warrants proposed to Melligeri Private Family Foundation')
N(5, 'up to 28,071,690', 'Rs 6,500 million', 'aggregate consideration of warrants')
N(5, 'Place: Belagavi', '01468590', 'DIN of Rajeev Kaul') if False else None
N(5, 'DIN-01468590', 'DIN-01468590', 'DIN Rajeev Kaul')
N(5, 'Notes to unaudited standalone', '10', 'note count (notes 1 to 10)') if False else None
# notes page 12
N(12, 'Rs 476.22', 'Rs 476.22 Mn', 'FY26 IPO expenses incl Pre-IPO (consolidated note 6)')
N(12, 'Rs 476.22', 'Rs 39.02 Mn', 'IPO expenses expensed as exceptional loss (consolidated)')
N(12, 'Securities Premium', 'Rs 437.20 Mn', 'IPO expenses reduced from Securities Premium (consolidated)')
N(12, 'consolidating 29', '29', 'existing labour laws consolidated')
N(12, 'consolidating 29', '4', 'Labour Codes notified')
N(12, 'gratuity of', 'Rs 37.93 Mn', 'incremental gratuity impact, FY26 (consolidated)')
N(12, 'up to 28,071,690', '28,071,690', 'warrants proposed to Melligeri Private Family Foundation')
N(12, 'up to 28,071,690', 'Rs 6,500 million', 'aggregate consideration of warrants')
N(12, 'DIN-01468590', 'DIN-01468590', 'DIN Rajeev Kaul')
N(12, 'two reportable segments', '2', 'reportable segments (Aerospace, Consumer)')
N(12, 'Indian Subsidiaries', '9', 'Indian subsidiaries listed in note 5') if False else None

# ---- DATE rows
Dt = lambda p, k, v, c: M('DATE', p, k, v, c)
Dt(1, 'October 26, 2026', 'October 26, 2026', 'letter date')
Dt(1, 'Monday, October 26', 'Monday, October 26, 2026', 'board meeting date')
Dt(1, '14:50 HRS', '14:50 HRS IST to 15:35 HRS IST', 'meeting start and end time')
Dt(1, 'quarter and half year ended', 'quarter and half year ended September 30, 2026', 'results period approved')
Dt(1, '2026.10.26', '2026.10.26 16:09:14 +05\'30\'', 'digital signature timestamp')
Dt(6, 'quarter ended 30 September 2026', 'quarter ended 30 September 2026; 1 April 2026 to 30 September 2026', 'standalone LRR period')
Dt(6, 'September 2025', 'quarter ended 30 September 2025; 1 April 2025 to 30 September 2025', 'comparative period not reviewed, standalone')
Dt(6, 'with effect from October 14, 2013', 'October 14, 2013', 'BSR & Co conversion to LLP')
Dt(7, '26 October 2026', '26 October 2026', 'standalone LRR signing date')
Dt(13, 'quarter ended 30 September 2026', 'quarter ended 30 September 2026; 1 April 2026 to 30 September 2026', 'consolidated LRR period')
Dt(13, 'September 2025', 'quarter ended 30 September 2025', 'comparative quarter not reviewed, consolidated')
Dt(13, 'with effect from October 14, 2013', 'October 14, 2013', 'BSR & Co conversion to LLP')
Dt(14, 'as at 30 September 2026', '30 September 2026', 'unreviewed subsidiary balance date')
Dt(14, 'INR 324.99', 'quarter ended 30 September 2026 and 1 April 2026 to 30 September 2026', 'unreviewed subsidiary periods')
Dt(14, '26 October 2026', '26 October 2026', 'consolidated LRR signing date')
Dt(15, '17 September', 'Liquidated with effect from 17 September 2026', 'Aequs Toys Hong Kong liquidation')
Dt(2, 'Statement of unaudited standalone', 'quarter and six months ended September 30, 2026', 'standalone P&L period')
Dt(2, 'Revenue from operations', 'Q 30-Sep-2026; Q 30-Jun-2026; Q 30-Sep-2025; 6M 30-Sep-2026; 6M 30-Sep-2025; FY 31-Mar-2026', 'standalone P&L column periods')
Dt(3, 'Statement of unaudited standalone', 'as at September 30, 2026; as at March 31, 2026', 'standalone balance sheet dates')
Dt(4, 'Unaudited standalone statement', 'six months ended September 30, 2026; September 30, 2025; year ended March 31, 2026', 'standalone cash flow periods')
Dt(8, 'Statement of unaudited consolidated', 'quarter and six months ended September 30, 2026', 'consolidated P&L period')
Dt(8, 'Continuing operations', 'Q 30-Sep-2026; Q 30-Jun-2026; Q 30-Sep-2025; 6M 30-Sep-2026; 6M 30-Sep-2025; FY 31-Mar-2026', 'consolidated P&L column periods')
Dt(9, 'Statement of unaudited consolidated', 'as at September 30, 2026; as at March 31, 2026', 'consolidated balance sheet dates')
Dt(10, 'Unaudited consolidated statement', 'six months ended September 30, 2026; September 30, 2025; year ended March 31, 2026', 'consolidated cash flow periods')
Dt(11, 'Unaudited consolidated segment', 'quarter and six months ended September 30, 2026', 'segment information period')
Dt(5, '1 The above standalone', 'quarter and six months ended September 30, 2026', 'standalone notes period')
Dt(5, 'October 26, 2026', 'October 26, 2026', 'Audit Committee and Board meetings, standalone note 2')
Dt(5, 'corresponding quarter and six', 'quarter and six months ended September 30, 2025', 'comparative period not audited or reviewed, standalone note 3')
Dt(5, 'reversed the past impairment', 'year ended March 31, 2026', 'impairment reversal year, note 4')
Dt(5, 'Initial Public Offer', 'year ended March 31, 2026', 'IPO expenses year, note 5')
Dt(5, 'On November 21, 2025', 'November 21, 2025', 'Labour Codes notified')
Dt(5, 'April 23, 2026', 'April 23, 2026', 'board resolution on Scheme of Amalgamation')
Dt(5, 'vide its order dated', 'October 12, 2026', 'Regional Director order rejecting Scheme of Amalgamation')
Dt(5, 'On September 25, 2026', 'September 25, 2026', 'board approval of preferential warrant issue')
Dt(5, 'Extraordinary General Meeting', 'October 22, 2026', 'EGM approving warrants')
Dt(5, 'before December 31, 2027', 'on or before December 31, 2027', 'proposed warrant conversion deadline')
Dt(5, 'Date : October 26, 2026', 'October 26, 2026', 'notes signing date')
Dt(5, 'Place: Belagavi', 'Belagavi', 'place of signing') if False else None
Dt(12, 'October 26, 2026. The Statutory', 'October 26, 2026', 'Audit Committee and Board meetings, consolidated note 2')
Dt(12, 'corresponding quarter ended September 30, 2025', 'quarter ended September 30, 2025', 'comparative quarter not audited or reviewed, consolidated note 3')
Dt(12, 'six months ended September 30, 2025 are extracted', 'six months ended September 30, 2025', 'audited special purpose interim statements, note 4')
Dt(12, 'Dissolved w.e.f.', 'September 17, 2026', 'Aequs Toys Hong Kong dissolved')
Dt(12, 'Initial Public Offer', 'year ended March 31, 2026', 'IPO expenses year, note 6')
Dt(12, 'On November 21, 2025', 'November 21, 2025', 'Labour Codes notified')
Dt(12, 'April 23, 2026', 'April 23, 2026', 'board resolution on Scheme of Amalgamation')
Dt(12, 'October 12, 2026', 'October 12, 2026', 'Regional Director order rejecting Scheme')
Dt(12, 'On September 25, 2026', 'September 25, 2026', 'board approval of preferential warrant issue')
Dt(12, 'on October 22, 2026', 'October 22, 2026', 'EGM approving warrants')
Dt(12, 'December 31, 2027', 'on or before December 31, 2027', 'proposed warrant conversion deadline')
Dt(12, 'Date: October 26, 2026', 'October 26, 2026', 'notes signing date')

# ---- FORWARD rows
F = lambda p, k, v, c: M('FORWARD', p, k, v, c)
F(1, 'This intimation will also be made available', 'This intimation will also be made available on the website of the Company', 'intimation to be posted on company website')
F(5, 'The Company is evaluating', 'The Company is evaluating the available course of actions in this regard', 'standalone note 7 course of action after rejection')
F(5, 'subject to receipt of requisite', 'preferential issue of up to 28,071,690 warrants ... for an aggregate consideration of Rs 6,500 million, subject to receipt of requisite regulatory approvals', 'standalone note 8 warrant issue')
F(5, 'proposed to be converted', 'warrants ... are proposed to be converted on or before December 31, 2027', 'warrant conversion into equity shares')
F(12, 'The Group is evaluating', 'The Group is evaluating the available course of actions in this regard', 'consolidated note 8 course of action after rejection')
F(12, 'subject to receipt of requisite', 'preferential issue of up to 28,071,690 warrants ... for an aggregate consideration of Rs 6,500 million, subject to receipt of requisite regulatory approvals', 'consolidated note 10 warrant issue')
F(12, 'proposed to be converted', 'warrants ... are proposed to be converted on or before December 31, 2027', 'warrant conversion into equity shares')
F(5, 'rejection of the scheme does not have', 'the rejection of the scheme does not have any material impact on the business operations of the Company', 'management statement on impact of rejection')
F(12, 'rejection of the scheme does not have', 'the rejection of the scheme does not have any material impact on the business operations of the Group', 'management statement on impact of rejection')

# ---- QUALIFIER rows
Q = lambda p, k, v, c, f='': M('QUALIFIER', p, k, v, c, f)
Q(1, 'Un-audited Financial Results', 'Approval of Un-audited Financial Results', 'results are unaudited')
Q(1, 'approved the Unaudited financial results', 'Unaudited financial results (both standalone and consolidated) ... along with Limited Review Report issued by the Statutory Auditors', 'results unaudited, limited review')
Q(1, 'Encl.', 'Encl.: as above', 'enclosures')
Q(1, 'Digitally signed', 'Digitally signed by RAVI MALLIKARJUN HUGAR', 'signature qualifier')
Q(1, 'formerly known as Aequs Private Limited', 'Aequs Limited (formerly known as Aequs Private Limited)', 'name change qualifier')
Q(2, '*Earnings per equity share', '*Earnings per equity share is not annualised for the quarters and six months ended.', 'defines asterisk on Basic* and Diluted* EPS, standalone')
Q(2, 'Basic*', 'Basic*', 'asterisk marker, standalone EPS')
Q(2, 'Diluted*', 'Diluted*', 'asterisk marker, standalone EPS')
Q(2, 'Statement of unaudited standalone', 'Statement of unaudited standalone financial results', 'standalone P&L is unaudited')
Q(2, '(Rs in Millions', '(Rs in Millions, except per share data)', 'unit convention, standalone P&L')
Q(2, 'Total comprehensive income', 'Unaudited / Audited column labels', 'columns: 5 Unaudited; FY 31-Mar-2026 Audited')
Q(2, 'Exceptional items gain', 'Exceptional items gain', 'exceptional item line, FY26 only (see standalone note 4)')
Q(3, '(Rs in Millions', '(Rs in Millions, except per share data)', 'unit convention, standalone balance sheet')
Q(3, 'Statement of unaudited standalone', 'Statement of unaudited standalone assets and liabilities', 'balance sheet unaudited; 31-Mar-2026 audited')
Q(4, '(Rs in Millions', '(Rs in Millions, except per share data)', 'unit convention, standalone cash flow')
Q(4, 'Unaudited standalone statement', 'Unaudited standalone statement of cash flows', 'cash flow unaudited; 31-Mar-2026 audited')
Q(8, '*Earnings per equity share', '*Earnings per equity share is not annualised for the quarters and six months ended. Further, diluted earnings per equity share is anti-dilutive.', 'defines asterisk on consolidated EPS')
Q(8, 'EPS from continuing', 'asterisk (*) marker on the three consolidated EPS lines', 'asterisk marker, consolidated EPS')
Q(8, '(Rs in Millions', '(Rs in Millions, except per share data)', 'unit convention, consolidated P&L')
Q(8, 'Statement of unaudited consolidated', 'Statement of unaudited consolidated financial results', 'consolidated P&L unaudited')
Q(8, '6M 30-Sep-2025', '6M 30-Sep-2025 column labelled Audited (not Unaudited)', 'six months ended Sep-2025 consolidated figures are audited special purpose interim, see note 4') if False else None
Q(8, '#COLS', '', '') if False else None
Q(9, '(Rs in Millions', '(Rs in Millions, except per share data)', 'unit convention, consolidated balance sheet')
Q(10, '(Rs in Millions', '(Rs in Millions, except per share data)', 'unit convention, consolidated cash flow')
Q(10, 'Loss before income tax from continuing operations', '6M 30-Sep-2025 column labelled Audited', 'comparative six-month column labelled Audited (see consolidated note 4)') if False else None
Q(11, '(Rs in Millions', '(Rs in Millions, except per share data)', 'unit convention, consolidated segment')
Q(11, 'Total segment results before', 'Total segment results before finance cost, depreciation and amortisation, share of net profit/(loss) of associate and joint ventures accounted for using the equity method net of tax, exceptional items, unallocated corporate expenses net of unallocated income and income taxes', 'defines the segment results subtotal')
Q(11, 'Unaudited consolidated segment', 'Unaudited consolidated segment information', 'segment information unaudited')
Q(5, 'prepared in accordance with the Indian Accounting Standard', 'standalone financial results prepared in accordance with Ind AS', 'basis of preparation, standalone note 1')
Q(5, 'reviewed by the Audit Committee', 'Limited Review ... unmodified review report', 'standalone note 2')
Q(5, 'have not been audited or reviewed', 'corresponding quarter and six months ended September 30, 2025 ... approved by the Board but have not been audited or reviewed by the statutory auditors', 'standalone note 3 comparatives unaudited and unreviewed')
Q(5, 'reversed the past impairment', 'reversed the past impairment of Rs 234.39 on investment in joint venture SQuAD ... improved business performance', 'standalone note 4')
Q(5, 'Rs 476.22', 'IPO expenses Rs 476.22 Mn: Rs 39.02 Mn exceptional loss, Rs 437.20 Mn from Securities Premium', 'standalone note 5')
Q(5, 'On November 21, 2025', 'Labour Codes incremental impact presented under Exceptional items for FY26, gratuity Rs 7.92 Mn', 'standalone note 6')
Q(5, 'On September 25, 2026', 'Warrants to Melligeri Private Family Foundation, one of the Promoters; EGM approved October 22, 2026', 'standalone note 8')
Q(5, "Company's Chief Operating Decision Maker", 'no separate segment disclosure in standalone results; segments in consolidated results (Ind AS 108)', 'standalone note 9')
Q(5, 'available on the BSE Limited', 'standalone results available on BSE, NSE and company websites', 'standalone note 10')
Q(5, 'Scheme of Amalgamation', 'Scheme of Amalgamation of AeroStructures Manufacturing India, Aequs Engineered Plastics and Aequs Force Consumer Products rejected by Regional Director order dated October 12, 2026', 'standalone note 7')
Q(12, 'prepared in accordance with', 'consolidated results prepared in accordance with Ind AS', 'basis of preparation, consolidated note 1')
Q(12, 'These consolidated financial results have been reviewed', 'Limited Review ... unmodified review report', 'consolidated note 2')
Q(12, 'have not been', 'corresponding quarter ended September 30, 2025 ... not audited or reviewed by the statutory auditors', 'consolidated note 3 comparatives')
Q(12, 'extracted from the audited special purpose', 'six months ended September 30, 2025 extracted from audited special purpose interim financial statements prepared for IPO', 'consolidated note 4; explains Audited label on 6M Sep-2025 column')
Q(12, 'Rs 476.22', 'IPO expenses Rs 476.22 Mn: Rs 39.02 Mn exceptional loss, Rs 437.20 Mn from Securities Premium', 'consolidated note 6')
Q(12, 'On November 21, 2025', 'Labour Codes incremental impact under Exceptional items for FY26, gratuity Rs 37.93 Mn', 'consolidated note 7')
Q(12, 'Scheme of Amalgamation', 'Scheme of Amalgamation rejected by Regional Director order dated October 12, 2026', 'consolidated note 8')
Q(12, 'On September 25, 2026', 'Warrants to Melligeri Private Family Foundation, one of the Promoters', 'consolidated note 10')
Q(12, "Group's Chief Operating Decision Maker", 'CODM is Executive Chairman and CEO; two reportable segments Aerospace and Consumer; non-attributable or non-recurring expenses disclosed as unallocable', 'consolidated note 11')
Q(12, 'available on the BSE Limited', 'consolidated results available on BSE, NSE and company websites', 'consolidated note 12')
Q(12, '(Note numbering', 'Printed note numbering skips from 8 to 10 (no note 9)', 'A1 mechanical observation of document numbering')
Q(6, '(in which is included interim', '(in which is included interim financial information of Aequs Stock Option Plan Trust)', 'standalone LRR scope')
Q(6, 'have not been subjected to review', 'figures for the corresponding quarter ended 30 September 2025 and period 1 April 2025 to 30 September 2025 approved by Board but not subjected to review', 'standalone LRR comparatives')
Q(6, 'we do not express an audit opinion', 'we do not express an audit opinion', 'standalone LRR review is not an audit')
Q(6, 'substantially less in scope', 'A review ... is substantially less in scope than an audit', 'standalone LRR')
Q(13, 'have not', 'figures for the corresponding quarter ended 30 September 2025 approved by Board but not subjected to review', 'consolidated LRR comparatives')
Q(13, 'we do not express an audit opinion', 'we do not express an audit opinion', 'consolidated LRR review is not an audit')
Q(13, 'substantially less in scope', 'A review ... is substantially less in scope than an audit', 'consolidated LRR')
Q(13, 'Regulation 33(8)', 'procedures in accordance with circular issued by SEBI under Regulation 33(8), to the extent applicable', 'consolidated LRR')
Q(13, 'share of the', 'includes share of profit/(loss) after tax and total comprehensive income/(loss) of its associate and joint ventures', 'consolidated LRR scope')
Q(14, 'We did not review', 'We did not review the interim financial information of a subsidiary included in the Statement', 'consolidated LRR para 6 other auditor')
Q(14, 'before consolidation adjustments', '(before consolidation adjustments)', 'defines subsidiary figures in para 6')
Q(14, 'reviewed by other auditor', 'reviewed by other auditor whose report has been furnished by Parent management; conclusion based solely on that report', 'consolidated LRR para 6 reliance')
Q(14, 'Our conclusion is not modified', 'Our conclusion is not modified in respect of this matter', 'consolidated LRR emphasis, unmodified conclusion')
Q(15, 'Liquidated', '(Liquidated with effect from 17 September 2026)', 'Annexure I item 15 status')
Q(15, 'List of entities included', 'List of entities included in unaudited consolidated financial results', 'Annexure I')
Q(6, 'Limited Review Report on unaudited standalone', 'Limited Review Report on unaudited standalone financial results', 'standalone LRR')
Q(13, 'Limited Review Report on unaudited consolidated', 'Limited Review Report on unaudited consolidated financial results', 'consolidated LRR')

# ---- ENTITY rows
E = lambda p, k, v, c: M('ENTITY', p, k, v, c)
E(1, 'National Stock Exchange', 'National Stock Exchange of India Limited', 'stock exchange addressee')
E(1, 'BSE Limited,', 'BSE Limited', 'stock exchange addressee')
E(1, 'NSE Scrip Symbol', 'NSE Scrip Symbol: AEQUS', 'ticker')
E(1, 'Subject:', 'Aequs Limited', 'issuer')
E(1, 'SEBI', 'SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015', 'regulator and regulation')
E(1, 'Ravi Mallikarjun Hugar', 'Ravi Mallikarjun Hugar', 'Company Secretary & Compliance Officer')
E(1, 'Statutory Auditors', 'Statutory Auditors of Company', 'reviewers')
E(1, 'Aequs Tower', 'Aequs Tower, No. 55, Whitefield Main Road, Mahadevapura Post, Bengaluru - 560048', 'registered office')
E(1, 'Aequs SEZ', 'Aequs SEZ, No. 437/A, Hattargi Village, Hukkeri Taluk, Belagavi - 591243', 'corporate office')
E(1, 'Exchange Plaza', 'Exchange Plaza, C-1, Block G, Bandra Kurla Complex, Mumbai - 400 051', 'NSE address')
E(1, '20th Floor', '20th Floor, P.J. Towers, Dalal Street, Mumbai - 400 001', 'BSE address')
E(6, 'B S R & Co. LLP', 'B S R & Co. LLP', 'statutory auditor')
E(6, 'Option Plan Trust', 'Aequs Stock Option Plan Trust', 'trust included in standalone results')
E(6, 'Embassy Golf Links', 'Embassy Golf Links Business Park, Pebble Beach, B Block, 3rd Floor, Bengaluru - 560 071', 'auditor address')
E(6, 'Institute of Chartered', 'Institute of Chartered Accountants of India', 'professional body')
E(7, 'Sampad Guha Thakurta', 'Sampad Guha Thakurta', 'audit partner')
E(13, 'subsidiaries', 'Aequs Limited and its subsidiaries; associate and joint ventures (the Group)', 'consolidation perimeter')
E(14, 'We did not review', 'a subsidiary reviewed by other auditor (unnamed)', 'unnamed subsidiary and other auditor')
E(14, 'Sampad Guha Thakurta', 'Sampad Guha Thakurta', 'audit partner')
E(5, 'to Melligeri Private', 'Melligeri Private Family Foundation', 'promoter, warrant allottee')
E(5, 'SQuAD', 'SQuAD Forging India Private Limited', 'joint venture, FY26 impairment reversal')
E(5, 'Scheme of Amalgamation', 'AeroStructures Manufacturing India Private Limited; Aequs Engineered Plastics Private Limited; Aequs Force Consumer Products Private Limited', 'wholly owned subsidiaries in rejected amalgamation')
E(5, 'Regional Director', 'Office of the Regional Director, South Western Region, Ministry of Corporate Affairs', 'regulator rejecting scheme')
E(5, 'Executive Chairman', 'Executive Chairman and Chief Executive Officer (CODM)', 'chief operating decision maker')
E(5, 'Rajeev Kaul', 'Rajeev Kaul, Co-Founder and Managing Director, DIN-01468590', 'signatory')
E(5, 'Ministry of', 'Ministry of Labour and Employment', 'regulator, Labour Codes')
E(5, 'Institute of Chartered', 'Institute of Chartered Accountants of India', 'professional body')
E(5, 'Government of India', 'Government of India', 'notified Labour Codes')
E(5, 'bseindia', 'BSE Limited; National Stock Exchange of India Limited', 'exchanges where results are posted')
E(12, 'Melligeri Private Family Foundation', 'Melligeri Private Family Foundation', 'promoter, warrant allottee')
E(12, 'Regional Director', 'Office of the Regional Director, South Western Region, Ministry of Corporate Affairs', 'regulator rejecting scheme')
E(12, 'Executive Chairman', 'Executive Chairman and Chief Executive Officer (CODM)', 'chief operating decision maker')
E(12, 'Rajeev Kaul', 'Rajeev Kaul, Co-Founder and Managing Director, DIN-01468590', 'signatory')
E(12, 'Ministry of', 'Ministry of Labour and Employment', 'regulator')
E(12, 'Institute of Chartered', 'Institute of Chartered Accountants of India', 'professional body')
E(12, 'Aerospace', "'Aerospace' and 'Consumer' reportable segments", 'segments')
E(12, 'Aequs Stock Option Plan Trust', 'Aequs Stock Option Plan Trust', 'trust consolidated')
for name, key in [
 ('Aequs Limited (Holding Company)', 'Holding Company'),
 ('Aerostructures Manufacturing India Private Limited (ASMIPL), Indian subsidiary', 'ASMIPL'),
 ('Aerospace Manufactuiring Holdings Private Limited (AMHPL), Indian subsidiary [spelling as printed]', 'AMHPL'),
 ('Aequs Force Consumer Products Private Limited (AFCPPL), Indian subsidiary', 'AFCPPL'),
 ('Aequs Engineered Plastics Private Limited (AEPPL), Indian subsidiary', 'AEPPL'),
 ('Aequs Consumer Products Private Limited (ACPPL), Indian subsidiary', 'ACPPL'),
 ('Aequs Manufacturing Private Limited (AMPL) formerly Aequs Toys Private Limited, Indian subsidiary', 'AMPL'),
 ('Koppal Toys Moulding COE Private Limited (KTMCPL), Indian subsidiary', 'KTMCPL'),
 ('Aerostructures Assemblies India Private Limited (AAIPL), Indian subsidiary', 'AAIPL'),
 ('Aequs Rajas Extrusion Private Limited (AREPL), Indian subsidiary', 'AREPL'),
 ('Aequs Aerospace France SAS (AAF SAS), foreign subsidiary', 'AAF SAS'),
 ('Aequs Aerospace BV (AABV), foreign subsidiary', 'AABV'),
 ('Aequs Aerospace LLC (AALLC), foreign subsidiary', 'AALLC'),
 ('Aequs Holdings France, SAS (AHF), foreign subsidiary', 'AHF'),
 ('Aequs Aero Machine Inc. (AAM), foreign subsidiary', 'AAM'),
 ('Aequs Oil and Gas LLC (AOGLLC), foreign subsidiary', 'AOGLLC'),
 ('Aequs Toys Hong Kong Private Limited (ATHPL), foreign subsidiary, dissolved w.e.f. September 17, 2026', 'ATHPL'),
 ('SQuAD Forging India Private Limited (SQuAD), Indian joint venture', '(SQuAD)'),
 ('Aerospace Processing India Private Limited (API), Indian joint venture', '(API)'),
 ('Aequs Cookware Private Limited (ACPL), Indian joint venture', '(ACPL)'),
 ('Ajna Aerospace & Defence Private Limited (Ajna), Indian joint venture', '(Ajna)'),
 ('Aequs Foundation, Indian associate', 'Aequs Foundation')]:
    ln = None
    for i in range(pg_start[12], pg_end[12] + 1):
        if key in lines[i - 1] and i > find(12, 'The consolidated financial results include'):
            ln = i; break
    if ln is None:
        sys.stderr.write('ENT NF ' + key + '\n'); ln = pg_start[12]
    add('ENTITY', 12, ln, name, 'consolidation list, note 5')
annex = [
 (15, 'Aequs Parent', 'Aequs Limited (includes Aequs Stock Option Plan Trust), Parent, Annexure I item 1'),
 (14, 'AeroStructures Manufacturing India Private', 'AeroStructures Manufacturing India Private Limited, Subsidiary, item 2'),
 (14, 'Aerospace Manufacturing Holdings', 'Aerospace Manufacturing Holdings Private Limited, Subsidiary, item 3'),
 (14, 'Aequs Engineered Plastics Private', 'Aequs Engineered Plastics Private Limited, Subsidiary, item 4'),
 (14, 'Aequs Consumer Products Private', 'Aequs Consumer Products Private Limited, Subsidiary, item 5'),
 (14, 'Aequs Manufacturing Private Limited', 'Aequs Manufacturing Private Limited (formerly Aequs Toys Private Limited), Subsidiary, item 6'),
 (14, 'Aerostructures Assemblies India', 'Aerostructures Assemblies India Private Limited, Subsidiary, item 7'),
 (14, 'Aequs Force Consumer Products', 'Aequs Force Consumer Products Private Limited, Subsidiary, item 8'),
 (14, 'Aequs Aerospace BV', 'Aequs Aerospace BV, Subsidiary, item 9'),
 (14, 'Aequs Oil and Gas LLC', 'Aequs Oil and Gas LLC, Subsidiary, item 10'),
 (14, 'Aequs Aerospace LLC', 'Aequs Aerospace LLC, Subsidiary of AeroStructures Manufacturing India Private Limited, item 11'),
 (14, 'Aequs Aero Machine Inc', 'Aequs Aero Machine Inc, Subsidiary of Aequs Aerospace LLC, item 12'),
 (14, 'Aequs Holdings France SAS', 'Aequs Holdings France SAS, Subsidiary of Aequs Aerospace BV, item 13'),
 (14, 'Aequs Aerospace France SAS', 'Aequs Aerospace France SAS, Subsidiary of Aequs Aerospace BV, item 14'),
 (14, 'Aequs Toys Hong Kong', 'Aequs Toys Hong Kong Private Limited (Liquidated w.e.f. 17 September 2026), Subsidiary of Aequs Engineered Plastics Private Limited, item 15'),
 (15, 'Koppal Toys Molding', 'Koppal Toys Molding COE Private Limited, Subsidiary of Aequs Manufacturing Private Limited, item 16'),
 (15, 'Aequs Rajas Extrusion', 'Aequs Rajas Extrusion Private Limited, Subsidiary of Aequs Manufacturing Private Limited, item 17'),
 (15, 'Aerospace Processing India', 'Aerospace Processing India Private Limited, Joint venture, item 18'),
 (15, 'SQuAD Forging', 'SQuAD Forging India Private Limited, Joint venture, item 19'),
 (15, 'Aequs Cookware', 'Aequs Cookware Private Limited, Joint venture, item 20'),
 (15, 'Ajna Aerospace', 'Ajna Aerospace & Defence Private Limited, Joint venture, item 21'),
 (15, 'Aequs Foundation', 'Aequs Foundation, Associate, item 22')]
for p, k, v in annex:
    pp = p
    # annexure page placement: items 1-15 on pdf page 14, 16-22 on pdf page 16? resolve by search
    ln = None; pgf = None
    for cand in (15, 16):
        for i in range(pg_start[cand], pg_end[cand] + 1):
            if k in lines[i - 1] and (cand >= 15 or True):
                # annexure rows only after 'Annexure I' marker
                if cand == 14 and i < find(14, 'Annexure I') if False else False:
                    continue
                ln = i; pgf = cand; break
        if ln: break
    add('ENTITY', pgf, ln, v, 'Annexure I consolidation list')

# fix: annexure items located wrongly if matched earlier on p14 text; handled by search order (p14 body precedes)
# ---- write structured
ids = 0
out = []
order = ['NUMBER', 'ENTITY', 'FORWARD', 'DATE', 'QUALIFIER']
body_out = []
for t in order:
    body_out.append('')
    body_out.append('## %s TABLE' % t)
    body_out.append('ID | page | line | TYPE | verbatim value | context | flag')
    for (page, line, val, ctx, flag) in rows[t]:
        ids += 1
        body_out.append('R%03d | page %d | line %d | %s | %s | %s%s' % (ids, page, line, t, val, ctx, (' | ' + flag) if flag else ''))
hdr = ['# STRUCTURED EXTRACTION: Aequs Limited (AEQUS) results Q2 FY27 (quarter ended 30-Sep-2026)',
       'source: Aequs_Q2FY27_Results.pdf; fulltext: aequs-results-q2fy27-fulltext.md (line numbers refer to that file, header block included)',
       'unit: Rs Millions (x0.1 = Rs Crores); values verbatim, not converted; ( ) = negative as printed; "-" = nil printed in source',
       'ID range: R001-R%03d' % ids,
       'counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d' % tuple(len(rows[t]) for t in order),
       'note: page 1 is a covering letter; pages 2-5 standalone statements and notes; pages 6-7 standalone LRR; pages 8-12 consolidated statements and notes; pages 13-16 consolidated LRR and Annexure I.',
       'note: pages 2-5 and 8-12 are image pages; financial tables were transcribed from the rendered image after OCR failed on tables. Totals tie where checkable.']
open(OUTS, 'w', encoding='utf-8').write('\n'.join(hdr + body_out) + '\n')
print(total, ids, [len(rows[t]) for t in order])
