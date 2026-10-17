rows=[]
def add(t,p,l,v,c,f=""): rows.append((t,p,l,v,c,f))
P=["Q2FY27","Q1FY27","Q2FY26","H1FY27","H1FY26","FY26"]
def pl(p,l,name,vals,flags=None,P=P):
    for i,v in enumerate(vals):
        if v is None: continue
        f=""
        if v in("-",): f="ZERO_STANDING"
        if flags and i in flags: f=(f+" "+flags[i]).strip()
        add("NUMBER",p,l,v,f"{name}, {P[i]}",f)
pl(2,75,"Revenue from Operations (Inclusive of GST)",["11,506","10,006.00","8,317.00","21,512","15,761","33,890.00"])
pl(2,76,"Other Operating Income",["112","59.00","96,00","171","149","236.00"],{2:"OCR_AS_READ"})
pl(2,77,"TOTAL INCOME",["11,618","10,065","8,413","21,683","15,910","34,126"])
pl(2,80,"Cost of materials consumed",["6,843","4,961","4,167","11,804","8,291","17,351"])
pl(2,81,"Purchases of stock-in-trade",["217","704","215","921","394","1,575"])
pl(2,82,"Change in inventories of FG, WIP, stock-in-trade",["(78)","143","173","65","(78)","(304)"])
pl(2,83,"Employee benefits expense",["888","820","775","1,708","1,499","3,044"])
pl(2,84,"Finance Costs",["24","20","13","At","37","81"],{3:"OCR_UNREADABLE"})
pl(2,85,"Depreciation and amortisation expense",["118","118","116","236","233","469"])
pl(2,87,"Other expenses: GST",["1,363","1,273","1053","2,636","2,041","4,232"],{2:"OCR_AS_READ"})
pl(2,88,"Other Expenses (other items)",["932","812","801","1,744","1,569","3,398"])
pl(2,91,"TOTAL OTHER EXPENSES",["2,295","2,085","1,854","4,380","3,610","7,630"])
pl(2,92,"TOTAL EXPENSES",["10,307","8,851","7,313","19,158","13,986","29,846"])
pl(2,93,"Total Profit before Exceptional Items & Tax",["1311","1,214","1,100","2,525","1,924","4,280"])
pl(2,95,"Total Profit before Tax",["1311","1214","1,100","2,525","1,924","4,280"])
pl(2,97,"Current Tax",["330","306","299","636","523","1,079"])
pl(2,98,"Deferred Tax",["0",None,None,None,None,"13"],{0:"ZERO_STANDING"})
pl(2,99,"Total tax expenses",["330","306","299","636","523","1,092"])
pl(2,102,"Net Profit from continuing Operations",["981","908","801","1,889","1,401","3,188"])
pl(2,103,"Profit/(loss) from discontinued Operations before tax",["-","-","-","-","-","-"])
pl(2,108,"Total Profit for the period",["981","908","801","1,889","1,401","3,188"])
pl(2,109,"Other comprehensive Income net of taxes",["(218)","384","-145","166","12","(97)"])
pl(2,110,"Total Comprehensive Income for the period",["763","1,292","656","2,055","1,413","3,091"])
pl(3,126,"Paid-up Equity Share capital (Rs Lakhs)",["1,059","1,059","1,059","1059","1,059","1,059"])
pl(3,130,"Reserve excluding revaluation Reserves",["13,661","13,661","10,728","13,661","10,728","10,728"])
pl(3,127,"Face Value (Rs)",["1","1"],P=["col1","col2"])
for l,n,v in[(139,"Basic EPS continuing ops (Rs)",["0,94","0.87","0.76","1.80","1.34","3.04"]),(140,"Diluted EPS continuing ops (Rs)",["0.94","0.87","0.76","1.80","134","3,04"]),(145,"Basic EPS continuing and discontinued (Rs)",["0,94","0.87","0.76","1.80","1.34","3.04"]),(146,"Diluted EPS continuing and discontinued (Rs)",["0,94","0.87","0.76","1,80","1.34","3.04"]),(147,"Debt Equity Ratio (x)",["0.11","0.1","0.09","0.11","0.09","0.13"]),(148,"DSCR (x)",["17.12","15.99","4.81","16.56","12.20","13.84"]),(149,"ISCR (x)",["56.05","61.65","87.14","58.61","53.01","53.99"])]:
    fl={}
    if l==140: fl={4:"OCR_AS_READ",5:"OCR_AS_READ"}
    if l in(139,145,146): fl={0:"OCR_AS_READ"}
    if l==146: fl[3]="OCR_AS_READ"
    pl(3,l,n,v,fl)
H=["H1FY27","FY26"]
def cf(p,l,n,v,fl=None): pl(p,l,n,v,fl,P=H)
cf(4,189,"CF Profit before tax",["2,525.00","4,280.00"])
cf(4,191,"CF Adjustments for finance costs",["32.00","57.00"])
cf(4,194,"CF Adj decrease(increase) trade receivables current",["(3.00)","(1,829.00)"])
cf(4,196,"CF Adj decrease(increase) trade receivables non-current",["162.00","(422.00"],{1:"OCR_AS_READ"})
cf(4,197,"CF Adj decrease(increase) other current assets",["(1,084.00)","(64.00)"])
cf(4,224,"CF Total adjustments for reconcile profit(loss)",["(726.00)"],{0:"PERIOD_COLUMN_UNRESOLVED"})
cf(4,225,"CF Net cash flows from operations",["1,799.00"],{0:"PERIOD_COLUMN_UNRESOLVED"})
cf(4,229,"CF Income taxes paid (refund), operating",["477.00"],{0:"PERIOD_COLUMN_UNRESOLVED"})
cf(4,231,"CF Net cash flows from operating activities",["1,322.00"],{0:"PERIOD_COLUMN_UNRESOLVED"})
cf(4,244,"CF Proceeds from sales of PPE",["1.00","4.00"])
cf(4,245,"CF Purchase of PPE",["581.00","895.00"])
cf(5,268,"CF Dividends received (investing)",["2.00","4.00"])
cf(5,269,"CF Interest received (investing)",["76.00","48.00"])
cf(5,271,"CF Other inflows (outflows) investing",["(455.00)","(1,920.00)"])
cf(5,272,"CF Net cash flows from investing activities",["(957.00)","(2,759.00)"])
cf(5,283,"CF Repayments of borrowings",["147.00"],{0:"PERIOD_COLUMN_UNRESOLVED"})
cf(5,287,"CF Interest paid (financing)",["32.00"],{0:"PERIOD_COLUMN_UNRESOLVED"})
cf(5,290,"CF Net cash flows from financing activities",["(179.00)","(492.00)"])
cf(5,292,"CF Net increase(decrease) in cash before FX",["186.00","(581.00)"])
cf(5,296,"CF Cash and equivalents at beginning of period",["504.00","1,085.00"])
cf(5,298,"CF Cash and equivalents at end of period",["690.00","504.00"])
B=["30/09/2026","31/03/2026"]
def bs(p,l,n,v,fl=None): pl(p,l,"BS "+n,v,fl,P=B)
bs(6,320,"Property, Plant and equipment",["6,009","6,011"])
bs(6,321,"Capital work-in-progress",["397","50"])
bs(6,324,"Other intangible assets",["1","1"])
bs(6,329,"Non current financial assets (subtotal)",["6,407","6,062"],{0:"LABEL_MISALIGNED_OCR",1:"LABEL_MISALIGNED_OCR"})
bs(6,330,"Non-current Investments",["1,077","985"])
bs(6,331,"Trade receivables non current",["=","-"],{0:"ZERO_STANDING OCR_AS_READ",1:"ZERO_STANDING"})
bs(6,333,"Other non-current financial assets",["932","132"])
bs(6,334,"Total non current financial assets",["1,309","1,117"])
bs(6,335,"Deferred tax assets (net)",["442","142"])
bs(6,336,"Other non-current assets",["579","99"])
bs(6,337,"TOTAL NON CURRENT ASSETS",["8,437","7,420"])
bs(6,339,"Inventories",["5,029","5,027"])
bs(6,341,"Current investments",["1,246","1,164"])
bs(6,342,"Trade receivables current",["3,964","4,126"])
bs(6,343,"Cash and cash equivalents",["690","504"])
bs(6,346,"Other current financial assets",["1,586","1,186"])
bs(6,347,"Total current financial assets",["7,486","6,980"])
bs(6,348,"Current tax assets (net)",["-","="],{0:"ZERO_STANDING",1:"ZERO_STANDING OCR_AS_READ"})
bs(6,349,"Other current assets",["1,325","735"])
bs(6,350,"TOTAL CURRENT ASSETS",["13,840","12,742"])
bs(6,351,"Non current assets held for sale",["-","-"],{0:"ZERO_STANDING",1:"ZERO_STANDING"})
bs(6,355,"TOTAL ASSETS",["22,277","20,162"])
bs(6,360,"Equity Share Capital",["1,059","1,059"])
bs(6,361,"Other Equity",["15,716","13,661"])
bs(6,364,"TOTAL EQUITY",["16,775","14,720"])
for l,n in[(370,"Borrowings non current"),(371,"Trade payable non current"),(372,"Other non current financial liabilities")]:
    bs(7,l,n,["-","-"],{0:"ZERO_STANDING",1:"ZERO_STANDING"})
bs(7,374,"Provisions non current",["498","473"])
bs(7,376,"Deferred tax liabilities (net)",["430","130"],{0:"LABEL_ON_PRIOR_LINE",1:"LABEL_ON_PRIOR_LINE"})
bs(7,378,"Other non current liabilities",["-","-"],{0:"ZERO_STANDING",1:"ZERO_STANDING"})
bs(7,379,"TOTAL NON CURRENT LIABILITIES",["6228","603"],{0:"OCR_AMBIGUOUS"})
bs(7,382,"Borrowings current",[":","-"],{0:"ZERO_STANDING OCR_AS_READ",1:"ZERO_STANDING"})
bs(7,383,"Trade payable current",["1,887","2,074"])
bs(7,384,"Other current financial liabilities",["2,363","2,457"])
bs(7,385,"Total current financial liabilities",["4,250","4,531"])
bs(7,386,"Other current liabilities",["315","188"])
bs(7,388,"Provisions current",["96","65"])
bs(7,389,"Current tax liabilities (net)",["213","55"])
bs(7,391,"TOTAL CURRENT LIABILITIES",["4,874","4,839"])
bs(7,397,"TOTAL LIABILITIES",["5,502","5,442"])
bs(7,398,"TOTAL EQUITY AND LIABILITIES",["22,277","20,162"])
for p,l,v,c in[(1,21,"BSE 514354","BSE scrip code"),(1,5,"L52109DL1992PLC049590","CIN"),(1,6,"011-45537559","telephone"),(2,67,"152109DL1992PLC049590","CIN as OCR read on p2"),(8,513,"522310","auditor membership no."),(8,515,"UDIN Ve <2 2:370 BEA EID 8623","UDIN garbled"),(3,174,"00061027","MD DIN"),(1,35,"13.30 Hrs","meeting commenced"),(1,35,"14.30 Hrs","meeting terminated")]:
    add("NUMBER",p,l,v,c,"IDENTIFIER")
ent=[(1,2,"Premier Polyfilm Limited","reporting company"),(1,15,"BSE Limited","stock exchange addressee"),(1,15,"National Stock Exchange of India Ltd","stock exchange addressee"),(1,21,"NSE: PREMIERPOL","scrip"),(1,49,"Heena Soni","Company Secretary & Compliance Officer"),(1,32,"Statutory Auditor (Limited Review Report)","auditor referenced"),(1,61,"Head Office & Factory, 40/1A Sahibabad Industrial Area Site IV, Ghaziabad (U.P.)","factory"),(1,62,"Vinyl Flooring","product"),(1,62,"PVC Sheeting","product"),(1,62,"PVC Geomembranes","product"),(1,62,"PVC Artificial Leather cloth","product"),(1,3,"Registered Office 305 Elite House, Kailash Colony Extension, New Delhi 110048","registered office"),(3,155,"Flexible PVC Flooring, Film and Sheets","main business"),(3,172,"Amitaabh Goenka","Managing Director & CEO"),(3,153,"Companies (Indian Accounting Standards) Rules 2015 (Ind AS)","accounting framework"),(3,153,"Companies Act 2013 Section 133","statute"),(3,152,"Audit Committee","reviewed statement"),(3,152,"Board of Directors","approved statement"),(8,415,"ADV AND CO LLP, Chartered Accountants","statutory auditor"),(8,442,"SEBI (LODR) Regulations 2015, Regulation 33","regulation"),(8,466,"Indian Accounting Standard 34 Interim Financial Reporting","standard"),(8,480,"Standard on Review Engagements (SRE) 2410","review standard"),(8,483,"Institute of Chartered Accountants of India (ICAI)","professional body")]
dates=[(1,10,"10-10-2026","letter date"),(1,18,"quarter and half year ended 30-09-2026","results period"),(1,25,"03rd October, 2026","board meeting intimation letter"),(1,28,"10th October, 2026","board meeting date"),(1,35,"13.30 Hrs to 14.30 Hrs","meeting time"),(2,71,"30-09-2026","Q2FY27 column"),(2,71,"30-06-2026","Q1FY27 column"),(2,71,"30-09-2025","Q2FY26 column"),(2,71,"32-03-2026","year-ended column as OCR read (FY26)"),(3,152,"10th October, 2026","board approval date"),(3,172,"10-10-2026","signing date"),(4,179,"half year ended 30th September, 2026","cash flow period"),(4,182,"31st March, 2026","prior year end"),(5,307,"10-10-2026","cash flow signing date"),(6,312,"30th September, 2026","balance sheet date"),(6,315,"31/03/2026","prior balance sheet date"),(7,408,"10-10-2026","balance sheet signing date"),(8,435,"quarter and half year ended 30th September, 2026","review period"),(8,516,"October 10, 2026","auditor report date")]
quals=[
(1,18,"UNAUDITED FINANCIAL RESULTS FOR THE QUARTER AND HALF YEAR","results unaudited",""),
(1,32,"A copy of Limited Review Report ... issued by the Statutory Auditor is attached","limited review, not audit",""),
(1,37,"The link to the results is as follows: (no link in text layer)","link missing","FOOTNOTE_UNRESOLVED"),
(1,25,"Board Meeting to consider and approve Standalone Unaudited Financial Results","standalone basis",""),
(2,68,"STATEMENT OF STANDALONE UNAUDITED FINANCIAL RESULTS","standalone, unaudited",""),
(2,69,"Figures: Rs. In Lakhs","unit",""),
(2,73,"(Refer Notes Below) Unaudited x5 / Audited (FY26 column)","audit status per column",""),
(2,75,"Revenue from Operations (Inclusive of GST)","revenue defined inclusive of GST",""),
(2,87,"Other expenses sub-line 'GST' shown separately","GST in expenses",""),
(2,88,"Other Expenses (Any item exceeding 10% of the total expenses relating to continuing operations to be shown separately)","format instruction",""),
(2,95,"Total Profit before Tax' (stray apostrophe marker)","marker with no footnote","FOOTNOTE_UNRESOLVED"),
(2,100,"Net movement in regulatory deferral account balances ... (no value)","blank row",""),
(3,113,"Page 3 header: 'Year ended' over 30-09-2026 and 30-09-2025 half-year columns","header label as read",""),
(3,115,"Unaudited x5 / Audited","audit status",""),
(3,118,"Rows 19-20 attribution (owners of parent / non-controlling interest) carry no values","blank rows",""),
(3,131,"stray marker '3' beside Reserve excluding revaluation Reserves","marker with no footnote","FOOTNOTE_UNRESOLVED"),
(3,151,"Notes:","notes header",""),
(3,152,"Note 1: Statement reviewed by Audit Committee and approved by Board at Meeting held on 10th October, 2026","note",""),
(3,153,"Note 2: Prepared per Ind AS (Companies Indian Accounting Standards Rules 2015, Section 133 Companies Act 2013) and other recognised accounting practices and policies to the extent applicable","note",""),
(3,155,"Note 3: Company mainly engaged in manufacturing and sale of Flexible PVC Flooring, Film and Sheets; single business product; segment reporting not applicable","note",""),
(3,157,"Note 4: Other Figures, except Earning per share, for the previous period regrouped/rearranged wherever necessary to correspond with current period's figures","note",""),
(3,158,"Note 5: The Company has no subsidiary/associate/Joint Venture Company(ies)","note",""),
(3,165,"The above company results are also available on the website of the company","note",""),
(4,179,"UNAUDITED CASH FLOW STATEMENT FOR THE HALF YEAR ENDED 30th SEPTEMBER, 2026","unaudited",""),
(4,180,"Figures: Rupees in Lakhs","unit",""),
(4,185,"Unaudited / Audited column status","audit status",""),
(4,187,"Whether cash flow statement is applicable on company (no value)","blank",""),
(4,196,"(422.00 (unclosed parenthesis as read)","OCR_AS_READ",""),
(4,208,"Most cash-flow rows between lines 192 and 223 carry labels but no values in text layer","values absent",""),
(6,312,"STATEMENT OF UNAUDITED ASSETS AND LIABILITIES AS AT 30th SEPTEMBER, 2026","unaudited",""),
(6,313,"Figures Rupees in Lakhs","unit",""),
(6,316,"Unaudited / Audited","audit status",""),
(6,317,"(Refer Notes Below)","note pointer",""),
(7,399,"Disclosure of notes on assets and liabilities (no text)","blank",""),
(8,428,"Independent Auditor's Limited Review Report on Unaudited Standalone Financial Results","limited review",""),
(8,461,"Statement is responsibility of Company's Management, approved by Board","responsibility",""),
(8,477,"Review per Standard on Review Engagements (SRE) 2410","review standard",""),
(8,490,"Fragment: nothing came to attention causing belief Statement not in accordance with Ind AS 34 / not disclosed required information / contains material misstatement (text as read, fragmentary)","conclusion fragment",""),
(8,477,"Auditor paragraphs 3-4 garbled in OCR; text partially missing","OCR_GARBLED",""),
(8,521,"stray '*' marker","marker with no footnote","FOOTNOTE_UNRESOLVED"),
]
out=[];rid=0
def emit(t,p,l,v,c,f=""):
    global rid
    rid+=1
    out.append((t,f"R{rid:03d} | page {p} | line {l} | {t} | {v} | {c}"+(f" | {f}" if f else "")))
for r in rows: emit(*r)
for p,l,v,c in ent: emit("ENTITY",p,l,v,c)
for p,l,v,c in dates: emit("DATE",p,l,v,c)
for p,l,v,c,f in quals: emit("QUALIFIER",p,l,v,c,f)
cnt={k:sum(1 for o in out if o[0]==k) for k in["NUMBER","ENTITY","FORWARD","DATE","QUALIFIER"]}
hdr="""=== A1 STRUCTURED EXTRACTION ===
source: PremierPolyfilm_Q2FY27_Results.pdf | fulltext: premierpol-results-q2fy27-fulltext.md (line anchors = number prefix of body lines)
units: Rs Lakhs (x0.01 to Crores); EPS in Rs; ratios in x
column key P&L (p2-3): Q2FY27=quarter 30-09-2026; Q1FY27=quarter 30-06-2026; Q2FY26=quarter 30-09-2025; H1FY27=half year 30-09-2026; H1FY26=half year 30-09-2025; FY26=year ended 31-03-2026 (audited)
ID range: R001-R%03d
counts: NUMBER %d | ENTITY %d | FORWARD %d (none: filing contains no forward-looking statement) | DATE %d | QUALIFIER %d
flags: values verbatim as OCR read; no estimation or fill. OCR_AS_READ / OCR_UNREADABLE mark garbled cells.
""" % (rid,cnt['NUMBER'],cnt['ENTITY'],cnt['FORWARD'],cnt['DATE'],cnt['QUALIFIER'])
body=""
for k in["NUMBER","ENTITY","FORWARD","DATE","QUALIFIER"]:
    body+="\n## "+k+"\n"+"\n".join(o[1] for o in out if o[0]==k)+("\n(none)" if cnt[k]==0 else "")+"\n"
open("../../extracted/premierpol-results-q2fy27-structured.md","w",encoding="utf-8").write(hdr+body)
print(rid,cnt)
