import re,json
L=open('extracted/eimcoeleco-results-q2fy27-fulltext.md',encoding='utf-8').read().split('\n')
def pg(ln):
    p=1
    for i in range(ln):
        m=re.match(r'\[page (\d+)\]',L[i])
        if m:p=int(m.group(1))
    return p if ln>17 else 0
def F(s,after=17):
    for i in range(after,len(L)):
        if re.sub(r'\s+',' ',s) in re.sub(r'\s+',' ',L[i]): return i+1
    print('NOTFOUND',s); return 0
rows={'NUMBER':[],'ENTITY':[],'FORWARD':[],'DATE':[],'QUALIFIER':[]}
def add(t,ln,val,ctx,flag=''):
    rows[t].append((pg(ln),ln,val,ctx,flag))
auto=json.load(open('work/a1-results/auto.json'))
ov={171:['FY 31.03.26'],177:['FY 31.03.26'],178:['FY 31.03.26'],179:['FY 31.03.26'],182:['FY 31.03.26'],
 211:['30.09.26'],236:['30.09.26'],237:['30.09.26'],315:['H1 30.09.26','FY 31.03.26'],
 291:['H1 30.09.26','FY 31.03.26','H1 30.09.25'],304:['H1 30.09.26','FY 31.03.26','H1 30.09.25']}
for ln,p,label,vals,cols in auto:
    if ln==291: vals=['{308.64)','(361.59)','(801.71)']
    if ln==304: vals=['5.40','121."~\\','(41.89)']
    cs=ov.get(ln,cols)
    label=re.sub(r'\s+',' ',label)
    for v,c in zip(vals,cs):
        fl=[]
        if re.search(r'[S{~"\\]',v): fl.append('TEXT_LAYER_GLITCH')
        if ln==211: fl.append('COLUMN_UNRESOLVED (value sits at 30.09.26 position in layout; 31.03.26 cell otherwise blank)')
        add('NUMBER',ln,v,f'{label}, {c}',';'.join(fl))
tp=[('791.17','Trade payables MSME dues, 30.09.26'),('1,803.87','Trade payables other than MSME, 30.09.26'),('770.37','Trade payables MSME dues, 31.03.26'),('992.58','Trade payables other than MSME, 31.03.26')]
for v,c in tp: add('NUMBER',F(v),v,c,'ASSIGNMENT_BY_LAYOUT (label and value rows separated in text layer)')
for a,b,panel in [(355,367,'Revenue/EBITDA charts'),(376,385,'PAT/Order Book charts')]:
    for ln in range(a,b+1):
        for t in re.findall(r'[+]?\d[\d.,]*%?',L[ln-1]):
            add('NUMBER',ln,t,f'slide chart label ({panel})','CHART_UNMAPPED (series/period not resolvable from text layer)')
def N(s,v,c,fl=''): add('NUMBER',F(s),v,c,fl)
N('Revenue for the quarter','Rs 57 crore','Q2 FY27 revenue per ED remarks (text: "increased to")')
N('increased to ₹57 crore from','Rs 33 crore','corresponding period last year revenue per ED remarks')
N('year-on-year growth of 70.9%','70.9%','revenue YoY growth, Q2 FY27')
N('108.8% year-on-year','108.8%','EBITDA YoY growth, Q2 FY27')
N('108.8% year-on-year','Rs 11 crore','EBITDA Q2 FY27')
N('margin improving to 18.8%','18.8%','EBITDA margin Q2 FY27')
N('PAT stood at','Rs 8 crore','PAT Q2 FY27')
N('46.5% year-on-year increase','46.5%','PAT YoY growth Q2 FY27')
N('targeted range of 18-20%','18-20%','targeted margin range')
N('open order pipeline of','Rs 133 crore','open order pipeline')
N('Company Code 523708','523708','BSE company code')
N('SEBI/','SEBI/HO/49/14/14(7)2025-CFD-POD2/I/3762/2026','SEBI circular number')
N('11:30 a.m.','11:30 a.m. to 1:00 p.m.','board meeting time window')
N('Face Value~ 10/','Rs 10/-','face value per share (Paid-up Equity row)')
N('( Face Value of~ 10/- each)','Rs 10/-','face value per share (EPS row)')
N('Membership No.','045027','auditor partner membership no.')
N('UDIN','26045027DECSCP3663','UDIN')
N("Firm's Registration",'10623_7W/W100829','auditor firm registration no.')
N('LLPIN','ABB-3171','KC Mehta LLPIN')
N('CIN: L28249GJ1974PLC002574','L28249GJ1974PLC002574','company CIN')
N('DIN: 08629181','08629181','Kamlesh N. Shah DIN')
N('(SRE)','2410','Standard on Review Engagements number')
N('section 133','133','Companies Act section')
N('section 143(10)','143(10)','Companies Act section')
N('Ind AS 7','7','Ind AS 7 reference')
N('+91 265 2440400','+91 265 2440400','auditor phone')
N('Anand Sojitra Road, Vallabh','388 120','registered office PIN')
N('Meghdhanush','390 007','auditor registered office PIN')
E=[('Eimco Elecon (India) Limited','Company (filer)','Eim/Sec/SE'),('BSE Ltd.','Exchange','BSE Ltd.'),('National Stock Exchange of India Limited','Exchange','National Stock'),
('Securities and Exchange Board of India','Regulator','Pursuant to Regulation 30'),('Symbol EIMCOELECO - Series EQ','NSE symbol','Symbol EIMCOELECO'),
('SEBI LODR Regulation 30 and Regulation 33, 2015','Regulatory provisions cited','Pursuant to Regulation 30'),
('Mr. Vishal C. Begwani','CFO and KMP, resigning','has noted the resignation'),('Risk Committee','Committee Begwani leaves','Risk Committee of the'),
('Rikenkumar Dalwadi','Company Secretary & Compliance Officer','Rikenkumar Dalwadi'),('Audit Committee','Committee that reviewed results','reviewed and recommended by the Audit'),
('K C Mehta & Co LLP','Statutory auditor','For K C Mehta'),('Institute of Chartered Accountants of India (ICAI)','Standards body','ICAI'),
('Standard on Review Engagements (SRE) 2410','Review standard','(SRE)'),('Ind AS 34 Interim Financial Reporting','Accounting standard','Interim'),
('Partner (name not legible in text layer; Membership No. 045027)','Auditor signatory','Partner'),
('Kamlesh N. Shah','Executive Director, signatory and press release quote','Kamlesh N. Shah'),
('Ms. Vrushali Thakkar','Investor contact','Vrushali Thakkar'),
('Machinery and Spares','Sole reportable business segment','only one reportable business segment'),
('Subsidiary/Associate/JV: none (ZERO_STANDING)','Note 3: no subsidiary, associate or JV','no Subsidiary, Associate'),
('Product; Spares','Revenue split legend on slide','Product Spares'),
('underground mining equipment and engineered solutions','Company product description','leading'),
('battery-operated vehicles','Product line','battery-operated vehicles'),
('construction equipment','Product line','high-performance construction'),
('service and spares network','After-sales business','service and spares network'),
('Vallabh Vidyanagar, Gujarat','Registered office / HQ location','Registered Office'),
('Vadodara','Auditor office and signing place','Place : Vadodara'),
('Ahmedabad, Bengaluru, Mumbai, Dubai','Auditor branches','Branch'),
('Executive Director (addressee of resignation)','Resignation addressee','The Executive Director'),
('Board of Directors','Approving body','The Board of Directors')]
for v,c,s in E: add('ENTITY',F(s),v,c)
FW=[('has noted the resignation','Begwani resignation effective close of business 30th October 2026 (Item 2)'),
('He shall cease to be the Key','Ceases to be KMP for materiality determination from 30th October 2026'),
('He shall also cease','Ceases to be Risk Committee member from 30th October 2026'),
('pursuant to which he will relinquish','Will relinquish CFO and KMP position (Annexure B)'),
('Closure of business hours on 30th October','Cessation date: close of business 30th October 2026 (Annexure B)'),
('relieve me from my duties','Request to be relieved at close of business 30th October 2026 (letter)'),
('structured handover','Commitment to seamless structured handover of financial operations (letter)'),
('I will work closely','Will work with team to complete transition formalities (letter)'),
('Margins are in line with our targeted range','Targeted margin range of 18-20%'),
('Looking ahead, we remain optimistic','Optimistic on demand, supported by infrastructure development and mining activity'),
('we are well positioned to sustain','Well positioned to sustain growth momentum and capitalize on opportunities'),
('healthy open order pipeline','Healthy open order pipeline of Rs 133 crore'),
('We remain','Focus on operational excellence; continuing to invest in capabilities'),
('continues to strengthen its portfolio','Continues to strengthen portfolio and broaden capabilities'),
('remains committed to enabling','Committed to enabling safer, more efficient and sustainable projects')]
for s,v in FW: add('FORWARD',F(s),v,'forward-looking / dateable commitment')
D=[('Date: 13th October, 2026','13th October, 2026','letter date'),
('11:30 a.m.','11:30 a.m. to 1:00 p.m., 13th October 2026','board meeting time'),
('quarter and half-year ended on 30th','30th September, 2026','quarter and half-year end'),
('dated 30th January, 2026','30th January, 2026','SEBI circular date'),
('with effect from the close of business hours','30th October, 2026','Begwani resignation effective date'),
('Date: 2026.10.13 13:05:56','2026.10.13 13:05:56 +05:30','digital signature timestamp'),
('Date : October 13, 2026','October 13, 2026','auditor report date'),
('quarter and half year ended on September 30, 2026','quarter and half year ended September 30, 2026','review period'),
('STATEMENT OF UNAUDITED FINANCIAL RESULTS','Quarter 30.09.26, 30.06.26, 30.09.25; Half Year 30.09.26, 30.09.25; Year 31.03.26','P&L column periods'),
('Particulars as at','as at 30.09.26 and 31.03.26','balance sheet column dates'),
('Particulars 30.09.26','30.09.26, 31.03.26, 30.09.25','cash flow column dates'),
('meeting held on October 13, 2026','October 13, 2026','Board meeting date (Note 1)'),
('Place : Vallabh Vidyanagar','October 13, 2026','cash flow statement signing date'),
('13th October 2026','13th October 2026','press release date'),
('Q2 & H1 FY27 Highlights','Q2 & H1 FY27','press release period'),
('Q2 FY26 Q2 FY27 H1 FY26 H1 FY27','Q2 FY26, Q2 FY27, H1 FY26, H1 FY27','chart x-axis periods'),
('Order Book as on September 30th, 2026','September 30th, 2026','order book date'),
('Sep-25 Sep-26','Sep-25, Sep-26','order book chart axis'),
('second quarter of FY27','second quarter of FY27','ED remarks period'),
('corresponding period last year','corresponding period last year','ED remarks comparison'),
('first half of the year','first half of the year','ED remarks period'),
('Date of appointment/ cessation','Closure of business hours on 30th October, 2026','Annexure B cessation date'),
('Date: September 5, 2026','September 5, 2026','resignation letter date'),
('of business hours on 30th October 2026.','30th October 2026','letter requested relieving date')]
for s,v,c in D: add('DATE',F(s),v,c)
Q=[('in Lakhs)','Unit statement: figures in Rs Lakhs (statement of results)',''),
('Unaudited Unaudited Unaudited','Column status labels: Unaudited (five columns) / Audited (31.03.26)',''),
('annualised)','EPS: for the period not annualised',''),
('Notes:','Header: Notes (Notes 1-5 follow)',''),
('1 The above Unaudited','Note 1: reviewed by Audit Committee, approved by Board 13 Oct 2026; reviewed by Statutory Auditors; Unmodified conclusion',''),
('2 The Company has only one','Note 2: only one reportable business segment, Machinery and Spares',''),
('3 The Company has no Subsidiary','Note 3: no Subsidiary, Associate or JV as on September 30, 2026',''),
('4 Figures of corresponding','Note 4: previous-period figures regrouped/rearranged to be comparable',''),
('5 Statement of Asset','Note 5: Statement of Assets and Liabilities at September 30, 2026 attached',''),
('6 Statement of cash flows','Note 6: Statement of cash flows for half year ended Sept 30, 2026 attached',''),
('Note:','Cash flow note: prepared under Indirect Method per Ind AS 7',''),
('Particulars as at','Balance sheet columns: 30.09.26 Unaudited; 31.03.26 Audited',''),
('Particulars 30.09.26','Cash flow columns: 30.09.26 Unaudited; 31.03.26 Audited; 30.09.25 Unaudited',''),
('moderate assurance','Auditor: review under SRE 2410 gives moderate assurance; substantially less in scope than an audit',''),
('we do not express an audit opinion','Auditor: no audit opinion expressed',''),
('nothing has come to our attention','Auditor para 4: nothing has come to attention indicating non-disclosure or material misstatement',''),
('Independent Auditor','Report is a limited review report on interim unaudited results',''),
('Unaudited Financial Results along with the Limited','Results unaudited; accompanied by Limited Review Report',''),
('Revenue (₹ crore)','Press release charts in Rs crore (unit differs from Lakhs statements)',''),
('Product Spares','Revenue chart legend: Product / Spares split (series mapping unresolved)','FOOTNOTE_UNRESOLVED'),
('Order Book as on September 30th','Order book as on September 30th, 2026 (inclusion/exclusion basis not given)','FOOTNOTE_UNRESOLVED'),
('EBITDA (₹ crore) & Margin','EBITDA definition not stated in press release (Other Income treatment not given)','FOOTNOTE_UNRESOLVED'),
('requisite disclosures','Annexure B disclosures per Regulation 30 read with SEBI circular',''),
('no material reasons','Begwani confirmed no material reasons other than those in resignation letter',''),
('Digitally signed','Company Secretary signature is digital',''),
('Brief profile (in case of appointment)','Brief profile: Not applicable',''),
('Disclosure of relationships between directors','Relationships between directors: Not applicable',''),
('KC Mehta & Co LLP (LLPIN','Auditor footer: registered as Partnership with limited liability','')]
for s,v,fl in Q: add('QUALIFIER',F(s),v,'defining/restricting text',fl)
order=['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']
out=[];i=0
for t in order:
    out.append(f'\n## {t} TABLE\n')
    for p,ln,v,c,fl in rows[t]:
        i+=1
        out.append(f'R{i:03d} | page {p} | line {ln} | {t} | {v} | {c}'+(f' | {fl}' if fl else ''))
cnt={t:len(rows[t]) for t in order}
hdr=f'''=== A1 STRUCTURED EXTRACTION ===
source: Eimco_Q2FY27_Results.pdf | fulltext: runs/eimcoeleco-q2fy27/extracted/eimcoeleco-results-q2fy27-fulltext.md (line numbers refer to that file, header included)
ROW ID RANGE: R001-R{i:03d}
counts: NUMBER {cnt['NUMBER']} | ENTITY {cnt['ENTITY']} | FORWARD {cnt['FORWARD']} | DATE {cnt['DATE']} | QUALIFIER {cnt['QUALIFIER']}
units: financial statements pp4-6 in Rs Lakhs (x0.01 to Cr); press release pp7-8 in Rs crore. Values verbatim; whitespace inside numbers (e.g. "3,323 .64") closed; text-layer glitches (S for 5, braces) kept and flagged. Column assignment of blank-cell rows follows layout position; see flags.
format: R### | page | line | TYPE | verbatim value | context | flags
=== END ===
'''
open('extracted/eimcoeleco-results-q2fy27-structured.md','w',encoding='utf-8').write(hdr+'\n'.join(out)+'\n')
print(cnt,i)
