import re
F='extracted/gmbrew-results-q2fy27-fulltext.md'
L=open(F,encoding='utf8').read().split('\n')
pg={}; cur=0
for i,l in enumerate(L,1):
    m=re.fullmatch(r'\[page (\d+)\]',l)
    if m: cur=int(m.group(1))
    pg[i]=cur
def find(p,sub,nth=1):
    n=0
    for i,l in enumerate(L,1):
        if pg[i]==p and sub in l:
            n+=1
            if n==nth: return i
    raise Exception((p,sub))
tok=re.compile(r'(\(?-?[\d,]+(?:\.\d+)?\)?|-)$')
def parse(p,cols):
    rows=[];prev=''
    for i,l in enumerate(L,1):
        if pg[i]!=p: continue
        s=l.strip()
        s=re.sub(r'(\s):(?=\s|$)',r'\1-',s)
        s=re.sub(r'(\d),$',r'\1',s)
        parts=s.split()
        n=len(cols);vals=[]
        while parts and len(vals)<n and tok.match(parts[-1]):
            vals.insert(0,parts.pop())
        if len(vals)==n and parts:
            label=' '.join(parts)
            if label in('Advances','three months)'): label=prev+' '+label
            rows.append((p,i,label,vals))
        prev=s
    return rows
out=[]
def addtab(rows,cols,ctx):
    for p,i,label,vals in rows:
        for c,v in zip(cols,vals):
            flag=' ZERO_STANDING' if v=='-' else ''
            out.append(('NUMBER',p,i,v+flag,(ctx+' '+label+', '+c)[:140]))
PL=['Q2 FY27 (qtr 30.09.2026)','Q1 FY27 (qtr 30.06.2026)','Q2 FY26 (qtr 30.09.2025)','H1 FY27 (30.09.2026)','H1 FY26 (30.09.2025)','FY26 (31.03.2026)']
BS=['as at 30.09.2026','as at 31.03.2026']
CF=['half year 30.09.2026','half year 30.09.2025']
for p,cols,ctx in[(3,PL,'standalone P&L Rs Lakhs:'),(10,PL,'consolidated P&L Rs Lakhs:'),(4,BS,'standalone BS Rs Lakhs:'),(11,BS,'consolidated BS Rs Lakhs:'),(5,CF,'standalone CF Rs Lakhs:'),(12,CF,'consolidated CF Rs Lakhs:')]:
    addtab(parse(p,cols),cols,ctx)
rp=[(1,'Remuneration','Jimmy Almeida Kashap CMD','180.00','90.00'),(2,'Remuneration','Jyoti Almeida Kashyap ED','132.00','66.00'),(3,'Remuneration','Kiran Parashare ED','36.00','18.00'),(4,'Remuneration','S Swaminathan CFO','30.25','15.13'),(5,'Remuneration','Sandeep Kutchhi VP Finance & CS','25.54','12.77'),(6,'Lease Rentals','Jimmy Almeida Kashap CMD','297.74','148.87'),(7,'Dividend','Jimmy Almeida Kashyap CMD','1269.92','1269.92'),(8,'Dividend','Jyoti Almeida Kashyap ED','40.92','40.92'),(9,'Dividend','Almeida Holdings Pvt Ltd promoter','219.63','219.63'),(10,'Loans and Advances','Buildfort Infradev Pvt Ltd subsidiary','101.05','101.05')]
for n,t,who,a,b in rp:
    ln=find(6,str(n)+' | GM BREWERIES')
    out.append(('NUMBER',6,ln,a,'RPT#%d %s %s, value approved by audit committee Rs Lakhs'%(n,t,who)))
    out.append(('NUMBER',6,ln,b,'RPT#%d %s %s, value during reporting period Rs Lakhs'%(n,t,who)))
    out.append(('NUMBER',6,ln,'0.00','RPT#%d %s, opening balance Rs Lakhs'%(n,who)))
    out.append(('NUMBER',6,ln,'0.00','RPT#%d %s, closing balance Rs Lakhs'%(n,who)))
    out.append(('NUMBER',6,ln,str(n),'RPT annexure serial number, '+who))
tl=find(6,'Total value of transaction')
out.append(('NUMBER',6,tl,'2,333.05','RPT total approved value, Rs Lakhs'))
out.append(('NUMBER',6,tl,'1,982.29','RPT total transaction value in reporting period, Rs Lakhs'))
def N(p,s,v,c,nth=1): out.append(('NUMBER',p,find(p,s,nth),v,c))
N(1,'Scrip Code','GMBREW','NSE scrip code'); N(1,'Scrip Code','507488','BSE scrip code')
N(1,'Mumbai- 400 051','400 051','NSE postal PIN'); N(1,'Mumbai - 400 001','400 001','BSE postal PIN')
N(1,'Regulation 33','33','SEBI LODR regulation number cited')
N(1,'Regulations, 2015','2015','SEBI LODR Regulations year')
N(1,'commenced','11.30 A.M.','board meeting start time'); N(1,'commenced','12.20 P.M.','board meeting end time')
N(1,'CIN','L15500MH1981PLC025809','CIN'); N(1,'GSTN','27AAACG1653N1ZG','GSTN')
N(7,'Nil','Nil ZERO_STANDING','loans/revolving facilities default amount (INR crore)',1)
N(7,'Nil','Nil ZERO_STANDING','unlisted debt securities default amount (INR crore)',2)
N(7,'Nil','Nil ZERO_STANDING','total financial indebtedness (INR crore)',3)
N(8,'SRE) 2410','2410','Standard on Review Engagement number'); N(8,'143(10)','143(10)','Companies Act section cited')
N(8,'133 of','133','Companies Act section cited'); N(8,'Indian Accounting','34','Ind AS 34')
N(9,'Firm Registration','0106326W','auditor firm registration no'); N(9,'Membership No','035722','auditor membership no')
N(9,'UDIN','26035722GQTJQY7770','standalone LRR UDIN')
N(14,'UDIN','26035722ZXAWAO6812','consolidated LRR UDIN'); N(14,'Membership No','035722','auditor membership no'); N(14,'Firm Registration','0106326W','auditor firm registration no')
N(3,'Earning Per share','Rs.10','EPS face value per share, standalone'); N(10,'Earning Per share','Rs.10','EPS face value per share, consolidated')
def Dt(p,s,v,c,nth=1): out.append(('DATE',p,find(p,s,nth),v,c))
Dt(1,'October 08, 2026','October 08, 2026','letter date',1)
Dt(1,'October 08, 2026','October 08, 2026','board meeting date',2)
Dt(1,'meeting held today','held today','board meeting "today"')
Dt(1,'quarter/half year ended','quarter/half year ended September 30, 2026','results period')
Dt(1,'half year ended September 30, 2026','September 30, 2026','results period (a.)')
Dt(1,'year ended September 30, 2026.','September 30, 2026','results period (b.)')
for p,tt in[(3,'standalone'),(10,'consolidated')]:
    ln=find(p,'Revenue from operations')-1
    for h in['30.09.2026|quarter','30.06.2026|quarter','30.09.2025|quarter','30.09.2026|half year','30.09.2025|half year','31.03.2026|year']:
        a,b=h.split('|')
        out.append(('DATE',p,ln,a,'%s P&L column: %s ended'%(tt,b)))
Dt(3,'Standalone Unaudited','September 30, 2026','standalone results title period')
Dt(10,'Consolidated Unaudited','September 30, 2025','consolidated results title period AS PRINTED')
Dt(3,'October 08, 2026','October 08, 2026','board meeting date in Note 1'); Dt(10,'October 08, 2026','October 08, 2026','board meeting date in Note 1')
for p,t in[(4,'standalone'),(11,'consolidated')]:
    Dt(p,'As at September','As at September 30, 2026',t+' BS date'); Dt(p,'30, 2026','As at March 31, 2026',t+' BS comparative date')
    Dt(p,'October 8, 2026','October 8, 2026',t+' BS signing date')
for p,t in[(5,'standalone'),(12,'consolidated')]:
    Dt(p,'HALF YEAR ENDED','HALF YEAR ENDED SEPTEMBER 30, 2026',t+' CF period'); Dt(p,'Particulars','September 30, 2025',t+' CF comparative period')
    Dt(p,'October 8, 2026','October 8, 2026',t+' CF signing date')
    Dt(p,'at beginning','beginning of period',t+' CF opening cash date'); Dt(p,'at End','end of period',t+' CF closing cash date')
Dt(6,'Related party transactions for','September 30, 2026','RPT period (half year / quarter)')
Dt(7,'Limited Review Reports on','Quarter/ Half year ended September 30, 2026','LRR period')
Dt(8,'Quarter ended September 30, 2026.','September 30, 2026','LRR standalone scope period (quarter only)')
Dt(8,'Date: 2026.10.08','2026.10.08 10:28:02 +05:30','standalone LRR digital signature (cover page)')
Dt(9,'Date: 2026.10.08','2026.10.08 10:27:50 +05:30','standalone LRR digital signature')
Dt(9,'Date: 08-10-2026','08-10-2026','standalone LRR signing date')
Dt(13,'Quarter ended September 30, 2026.','September 30, 2026','LRR consolidated scope period (quarter only)')
Dt(13,'Date: 2026.10.08','2026.10.08 10:28:21 +05:30','consolidated LRR digital signature (cover)')
Dt(14,'Date: 2026.10.08','2026.10.08 10:28:32 +05:30','consolidated LRR digital signature')
Dt(14,'Date: 08-10-2026','08-10-2026','consolidated LRR signing date')
Dt(7,'Annual Filing','4th quarter','annual-only statement E periodicity'); Dt(7,'2ND AND 4TH','2nd and 4th quarter','RPT half-yearly filing periodicity')
def E(p,s,v,c,nth=1): out.append(('ENTITY',p,find(p,s,nth),v,c))
E(1,'Regd. Office','G M Breweries Limited (CIN L15500MH1981PLC025809), Regd. Office Ganesh Niwas, Prabhadevi, Mumbai-400 025; letterhead repeats on pages 2,3,4,5,7,10,11,12 (address/phone block)','registrant / letterhead summary')
E(1,'Exchange Plaza','National Stock Exchange of India Limited (NSE), Listing Department, Bandra-Kurla Complex','addressee exchange')
E(1,'Phiroze','Bombay Stock Exchange Limited (BSE), Phiroze Jeejeebhoy Towers, Dalal Street','addressee exchange')
E(1,'Regulation 33','SEBI (LODR) Regulations, 2015','regulation cited'); E(1,'Considered and approved','Board of Directors of the Company','approving body')
E(1,'statutory auditors','statutory auditors of the company (V. P. Mehta & Co per pages 8-9, 13-14)','LRR provider')
E(2,'Sandeep','Sandeep Kutchhi, Vice President Finance & Company Secretary','signatory of cover letter')
E(2,'Warm Regards','GM BREWERIES LTD','signing entity')
E(3,'Country Liquor','Country Liquor (sole operating segment)','segment named in Note 3'); E(10,'Country Liquor','Country Liquor (sole operating segment)','segment named in Note 3')
E(3,'reviewed by audit committee','Audit Committee','reviewer in Note 1')
E(4,'Jyoti','Jyoti Almeida Kashyap, Executive Director','BS signatory'); E(11,'Jyoti','Jyoti Almeida Kashyap, Executive Director','BS signatory')
E(5,'Jyoti','Jyoti Almeida Kashyap, Executive Director','CF signatory'); E(12,'Jyoti','Jyoti Almeida Kashyap, Executive Director','CF signatory')
E(5,'Factory','Factory: S. Veer Savarkar Marg, Virar (East), Dist. Palghar, PIN 401 305; phone (0250) 2528 728, 2528 793, 2529 127 (footer repeats pages 1,2,4,5,7,11,12)','factory address summary')
E(6,'1 | GM','Jimmy Almeida Kashap (PAN AADPA4837A), Chairman and Managing Director','RPT counterparty')
E(6,'2 | GM','Jyoti Almeida Kashyap (PAN ACGPA3738D), Executive Director','RPT counterparty')
E(6,'3 | GM','Kiran Parashare (PAN ALEPP3153G), Executive Director','RPT counterparty')
E(6,'4 | GM','S Swaminathan (PAN ABBPS3446G), CFO','RPT counterparty')
E(6,'5 | GM','Sandeep Kutchhi (PAN ASKPK6502D), Vice President Finance & Company Secretary','RPT counterparty')
E(6,'9 | GM','Almeida Holdings Pvt Ltd (PAN AAACA3918L), Promoter','RPT counterparty')
E(6,'10 | GM','Buildfort Infradev Private Limited (PAN AANCB4068R), Subsidiary Company','RPT counterparty; loans and advances')
E(6,'1 | GM','GM Breweries Limited (PAN AAACG1653N)','listed entity in RPT')
E(8,'V. P. MEHTA & CO','V. P. Mehta & Co, Chartered Accountants (Vipul P. Mehta, F.C.A), offices Vidyavihar (E) and Masjid (W), Mumbai','statutory auditor')
E(9,'Proprietor','Vipul P. Mehta, Proprietor, Membership No 035722, Firm Reg 0106326W','signing auditor')
E(8,'Chartered Accountants of India','Institute of Chartered Accountants of India (ICAI) SRE 2410','standard issuer')
E(8,'Companies Act','Companies Act, 2013','statute cited')
E(13,'Buildfort','Buildfort Infradev Private Limited, wholly owned subsidiary','consolidated entity')
E(14,'a. GM','GM Breweries Limited - Holding Company','LRR consolidation list'); E(14,'b. Build','Buildfort Infradev Private Limited - Wholly owned subsidiary','LRR consolidation list')
out.append(('FORWARD',1,find(1,'uploaded on'),'The above intimation and unaudited standalone financial results are also being uploaded on company\'s website www.gmbreweries.com','website upload intimation (no guidance in document)'))
def Q(p,s,v,c,nth=1): out.append(('QUALIFIER',p,find(p,s,nth),v,c))
Q(1,'unaudited','unaudited Consolidated & Standalone financial results','results are unaudited')
Q(1,'Limited Review Report','Limited Review Report by the statutory auditors','results reviewed, not audited')
Q(1,'Sub: Outcome of the Board meeting','Sub: Outcome of the Board meeting (OCR shows two Sub lines)','subject line')
for p,t in[(3,'standalone'),(10,'consolidated')]:
    Q(p,'Sales / Income','(inclusive of Excise Duty & VAT)',t+' revenue includes excise duty and VAT')
    Q(p,'Excise duty, VAT','Excise duty, VAT & TCS (expense line)',t+' excise expense line, gross of excise revenue')
    Q(p,'Unaudited','Unaudited (5 columns) / Audited (FY26 column)',t+' audit status of columns')
    Q(p,'1) The aforesaid','1) results reviewed by audit committee and taken on record by Board on October 08, 2026',t+' Note 1')
    Q(p,'2) Provision','2) Provision for taxation includes provision for current tax .',t+' Note 2')
    Q(p,'3) The company','3) The company\'s operation at present is confined to only one segment namely Country Liquor.',t+' Note 3')
    Q(p,'4) Figures','4) Figures of previous year/period have been regrouped, whereever necessary.',t+' Note 4')
    Q(p,'(Rs. Lakhs)','(Rs. Lakhs)',t+' P&L unit')
    Q(p,'Tax expenses','Tax expenses ( Current & Deffered Taxes)',t+' tax line covers current and deferred')
    Q(p,'Earning Per share','Basic & Diluted',t+' EPS basis')
    Q(p,'Gain/ Loss','Gain/ Loss on fair valuation of investment in equity shares (Net of Taxes)',t+' OCI line net of taxes')
Q(10,'Consolidated Unaudited','Title reads "September 30, 2025" while columns read 30.09.2026','consolidated title period mismatch as printed')
for p,t in[(4,'standalone'),(11,'consolidated')]:
    Q(p,'5)','5) '+('Standalone' if p==4 else 'Consolidated')+' Balancesheet',t+' BS note number; no unit label printed in BS header')
    Q(p,'Trade payables','Trade payables ( Other than Micro & Small enterprises)',t+' BS line restricted to non-MSME')
    Q(p,'Tax Assets','Non Current Tax Assets (Net)',t+' BS net basis'); Q(p,'Tax Liabilities','Current Tax Liabilities (Net)',t+' BS net basis, blank both periods')
for p,t in[(5,'standalone'),(12,'consolidated')]:
    Q(p,'CASH FLOW STATEMENT','(Rs. Lakhs)',t+' CF unit')
    Q(p,'Indirect Taxes paid','Indirect Taxes paid added back and Indirect Taxes Paid deducted, both 1,25,042.01',t+' CF presentation of indirect taxes')
    Q(p,'Redemption','(with Maturity more than three months)',t+' CF fixed deposit scope')
Q(6,'in lakhs','in lakhs','RPT unit'); Q(6,'Annexure','Annexure: 1 (handwritten)','RPT annexure label')
Q(6,'Total value','Total 2,333.05 (approved value) vs 1,982.29 (transaction during reporting period)','RPT totals definition')
Q(6,'1 | GM','Loan/ICD columns (indebtedness, cost, tenure, interest, secured, purpose) blank for all rows','RPT additional disclosure blank')
Q(7,'Particulars in INR crore','Particulars in INR crore (default table header; Lakhs elsewhere)','default table unit differs from statements')
Q(7,'Not Applicable','B. Statement on deviation: Not Applicable','Section B')
Q(7,'Not Applicable.','E. Statement on impact of audit qualifications: Not Applicable. (annual only)','Section E')
Q(7,'ONLY','D. RPT format applicable only for half yearly filing (2nd and 4th quarter)','Section D applicability')
Q(7,'Statutory Auditors','Limited Review Reports issued under Companies Act 2013 and SEBI Listing Regulations 2015 for Quarter/ Half year ended September 30, 2026','LRR scope statement')
Q(8,'Re: Limited Review','LRR title scope "for the Quarter ended September 30, 2026" (half year not named)','LRR period scope')
Q(8,'1. We have','LRR para 1: review of standalone unaudited results, quarter ended September 30, 2026','scope')
Q(8,'2. This statement','LRR para 2: management responsibility; Ind AS 34','basis of preparation')
Q(8,'3. We conducted','LRR para 3: review under SRE 2410; substantially less in scope than an audit','review standard')
Q(8,'audit opinion','Accordingly we do not express an audit opinion.','no audit opinion expressed')
Q(9,'4. Based','LRR para 4: nothing has come to our attention ... material misstatement (no qualification)','conclusion')
Q(9,'Digitally signed','Digitally signed by VIPUL MEHTA','signature')
Q(13,'1. We have','LRR consolidated para 1: Holding Co and Buildfort Infradev Pvt Ltd (wholly owned subsidiary), quarter ended Sept 30, 2026','scope')
Q(13,'audit opinion','Accordingly we do not express an audit opinion.','no audit opinion expressed')
Q(14,'5. Based','LRR consolidated para 5 text says "accompanying statement of standalone unaudited Financial Results" (as printed)','wording as printed')
Q(14,'4. The statement','LRR para 4: statement includes results of Holding Co and Buildfort Infradev Pvt Ltd','consolidation list')
order=['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']
rows=[];c={}
for t in order:
    sel=[r for r in out if r[0]==t]
    c[t]=len(sel); rows+=sel
res=['# A1 STRUCTURED EXTRACTION, GMBREW q2fy27 results (14 pages)','ID range: R001-R%03d'%len(rows),
'Counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d | total %d'%(c['NUMBER'],c['ENTITY'],c['FORWARD'],c['DATE'],c['QUALIFIER'],len(rows)),
'Units: Rs Lakhs (x0.01 to Rs Cr); values verbatim, not converted. Line numbers refer to gmbrew-results-q2fy27-fulltext.md. Table rows are atomic (line item x period).',
'Format: R### | page N | line L | TYPE | verbatim value | context',
'Note: no forward-looking guidance, targets or commissioning dates appear in this filing; one intimation row logged under FORWARD.']
k=0;cur=None
for r in rows:
    if r[0]!=cur:
        cur=r[0];res.append('\n## '+cur)
    k+=1
    res.append('R%03d | page %d | line %d | %s | %s | %s'%(k,r[1],r[2],r[0],r[3],r[4]))
open('extracted/gmbrew-results-q2fy27-structured.md','w',encoding='utf8').write('\n'.join(res)+'\n')
print(c,len(rows))
