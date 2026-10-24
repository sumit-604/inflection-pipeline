import re
F="extracted/cybertech-presentation-q2fy27-fulltext.md"
L=open(F,encoding="utf-8").read().split("\n")
rows=[]
def A(t,p,l,v,c,f=""): rows.append((t,p,l,v,c,f))
A("DATE",1,23,"22nd October 2026","presentation date")
A("DATE",1,21,"Q2FY27","quarter of presentation")
A("ENTITY",1,25,"CyberTech Systems and Software Limited","issuer, footer")
A("QUALIFIER",1,25,"CyberTech Systems and Software Limited , All Rights Reserved","copyright footer on every slide")
A("ENTITY-SUMMARY",2,29,"Safe Harbor legal text: no representation or warranty, no liability, information current only as of date, content may be altered without notice, general information only, risk of loss of principal, not an offer or invitation","safe harbor boilerplate (grouped)")
A("QUALIFIER",2,38,"This presentation is based on the publicly available information on CyberTech including but not limited to Company's website and Annual Reports.","source basis of the presentation")
A("QUALIFIER",2,36,"Actual results may differ materially from these forward-looking statements","forward-looking caveat")
A("QUALIFIER",2,35,"The information contained in this presentation is only current as of its date","currency limit of information")
A("FORWARD",2,35,"Certain statements may be forward-looking statements, including general business plans and strategy, future financial condition and growth prospects, future developments in industry","generic safe harbor; no numeric guidance in deck")
A("ENTITY-SUMMARY",3,55,"Agenda: 1 Company Overview; 2 Financial Performance","agenda slide")
A("ENTITY-SUMMARY",4,63,"Section divider: Company Overview","divider slide")
A("ENTITY-SUMMARY",10,171,"Section divider: Financial Performance","divider slide")
A("ENTITY",5,70,"Esri ArcGIS Enterprise Cloud platforms","specialization")
A("ENTITY",5,73,"Cloud-based SAP digitalized solutions","specialization")
A("ENTITY",5,74,"Spatialitics Cloud native SaaS","specialization/product")
A("NUMBER",5,76,"over 500","professionals, global team")
A("NUMBER",5,78,"300+","Geospatial SMEs, Geospatial CoE")
A("NUMBER",5,79,"100+","SMEs, SAP CoE")
A("ENTITY",5,78,"World's largest Geospatial CoE","claim: Geospatial Centre of Excellence")
A("ENTITY",5,79,"SAP CoE","Centre of Excellence")
for e in ["SAP","Esri","Cisco","Salesforce","Microsoft"]:
    A("ENTITY",5,81,e,"technology partner")
for e,l in [("Chicago",84),("Philadelphia",84),("Aurora",84),("Redlands",84),("Mumbai",85),("Pune",85),("Kolkata",85)]:
    A("ENTITY",5,l,e,"office location "+("USA" if l==84 else "India"))
A("ENTITY",5,87,"development center at Thane (owned)","owned state-of-the-art development center")
A("DATE",6,96,"2009","Vish took over control of the company")
A("DATE",6,94,"2010-13","GeoSpatial became main focus area")
A("DATE",6,95,"2015-16","Incubate Geo 2.0 Products")
A("DATE",6,94,"2016-17","Advisory Board formed with industry leaders")
A("DATE",6,94,"2017-18","Spatialitics formed")
A("ENTITY",6,98,"Vish","took over control of the company 2009")
A("ENTITY",6,94,"Geo Focus","timeline milestone")
A("ENTITY",6,94,"Exceptional Talent","timeline milestone")
A("ENTITY",6,95,"Incubate Geo 2.0 Products","timeline milestone")
A("ENTITY",6,96,"Advisory Board formed with industry leaders","timeline milestone")
A("ENTITY",6,96,"Spatialitics","formed 2017-18")
A("ENTITY",7,106,"Enterprise Multi-Cloud Transformation services","slide title")
for e in ["SAP S/4HANA","SAP Supply Chain","SAP BTP","SAP Spatial Enablement","ArcGIS Enterprise","ArcGIS Utility Networks","Sales Cloud","Service Cloud","Salesforce CPQ","Community Cloud","Tableau"]:
    A("ENTITY",7,108,e,"product suite / technology")
for e in ["Advisory","Cloud Move","Implementation & Integration","AMS","Managed ArcGIS Cloud Services","GIS Professional Services","Data & Integration","Ongoing Support"]:
    A("ENTITY",7,110,e,"service offering")
A("ENTITY",7,114,"CyberTech Services","grouping label")
A("ENTITY",7,116,"Cloud/SaaS","grouping label")
A("ENTITY",8,129,"Spatialitics Platform","Cloud Native SaaS offering")
for e in ["Public Safety","Healthcare","Utilities"]:
    A("ENTITY",8,133,e,"Spatialitics industry")
A("ENTITY",9,144,"Vish Tadimety","Chairman and CEO")
A("ENTITY",9,144,"Steven Jeske","Group CFO and Director")
A("ENTITY",9,144,"Ramasubramanian S.","Executive Director")
A("DATE",9,147,"1990","Vish co-founded the company")
A("DATE",9,157,"2007","Vish co-founded Corliant with Cisco partnership")
A("DATE",9,152,"since 1999","Steven Jeske Group CFO tenure start")
A("NUMBER",9,153,"30 years","Raman experience, heads global operations")
A("ENTITY",9,157,"Corliant","co-founded 2007, later acquired by Accenture")
A("ENTITY",9,157,"Cisco","Corliant partnership")
A("ENTITY",9,159,"Accenture","acquirer of Corliant")
A("ENTITY",9,161,"PWC","Steven Jeske former manager")
A("ENTITY",9,162,"University of Illinois","Steven Jeske undergraduate degree in accounting")
A("ENTITY",9,164,"University of Chicago","Steven Jeske MBA")
A("ENTITY",9,161,"CPA","Steven Jeske qualification")
A("ENTITY",9,147,"Vish bio: led growth in networking, enterprise solutions and GIS; set up offices in Europe, APAC, Latin America and Japan; turnaround specialist; raised capital from public markets, strategic partners and venture funds","executive bio claims")
A("ENTITY",9,153,"Raman bio: strategic planning, budgeting, forecasting, taxation; financial controls; relationships with auditors, bankers, lawyers, consultants","executive bio claims")
A("ENTITY",9,155,"Steven bio: serial entrepreneur; key partner of strategy and financial decisions; co-founder of Corliant along with Vish","executive bio claims")
A("NUMBER",11,179,"780.3 million","Total Revenue Q2FY27")
A("NUMBER",11,179,"1.8% Q-o-Q","Total Revenue growth Q2FY27")
A("NUMBER",11,179,"16.9% Y-o-Y","Total Revenue growth Q2FY27")
A("NUMBER",11,180,"733.0 million","Operating Revenue Q2FY27")
A("NUMBER",11,180,"7.1% Q-o-Q","Operating Revenue growth Q2FY27")
A("NUMBER",11,180,"24.7% Y-o-Y","Operating Revenue growth Q2FY27")
A("NUMBER",11,181,"128.2 million","Reported EBITDA Q2FY27")
A("NUMBER",11,181,"16.4% of total revenue","Reported EBITDA margin Q2FY27")
A("NUMBER",11,182,"115.4 million","PBT Q2FY27")
A("NUMBER",11,182,"14.8% of total revenue","PBT margin Q2FY27")
A("NUMBER",11,183,"86.8 million","PAT Q2FY27")
A("NUMBER",11,183,"11.1% of total revenue","PAT margin Q2FY27")
A("QUALIFIER",11,181,"Reported EBITDA; margins stated as % of total revenue","denominator is total revenue (780.3 million)")
A("QUALIFIER",11,179,"Currency symbol not rendered in text layer; unit shown as million","unit of slide 11 figures")
A("DATE",11,177,"Q2FY27","financial summary period")
for p,v in [("Q2FY26","587.9"),("Q1FY27","684.5"),("Q2FY27","733.0")]:
    A("NUMBER",12,222,v,f"Operating Revenue INR Million, {p}")
A("NUMBER",12,222,"24.7%","Operating Revenue YoY growth Q2FY27")
A("NUMBER",12,222,"7.1%","Operating Revenue QoQ growth Q2FY27")
for p,v in [("Q2FY26","125.7"),("Q1FY27","139.0"),("Q2FY27","128.2")]:
    A("NUMBER",12,223,v,f"EBITDA INR Million, {p}")
for p,v in [("Q2FY26","18.8%"),("Q1FY27","18.1%"),("Q2FY27","16.4%")]:
    A("NUMBER",12,223,v,f"EBITDA margin, {p}")
A("NUMBER",12,223,"2.0%","EBITDA YoY growth Q2FY27")
A("NUMBER",12,223,"7.8%","EBITDA QoQ de-growth Q2FY27")
for p,v in [("Q2FY26","114.0"),("Q1FY27","126.2"),("Q2FY27","115.4")]:
    A("NUMBER",12,224,v,f"PBT INR Million, {p}")
for p,v in [("Q2FY26","17.1%"),("Q1FY27","16.5%"),("Q2FY27","14.8%")]:
    A("NUMBER",12,224,v,f"PBT margin, {p}")
A("NUMBER",12,224,"1.2%","PBT YoY growth Q2FY27")
A("NUMBER",12,224,"8.5%","PBT QoQ de-growth Q2FY27")
for p in ["Q2FY26","Q1FY27","Q2FY27"]:
    A("DATE",12,222,p,"chart period axis")
A("QUALIFIER",12,224,"Q1FY27 PBT margin label partly hidden behind bar in image; value 16.5% from text layer","chart label legibility note")
for p,v in [("Q2FY26","99.0%"),("Q1FY27","99.0%"),("Q2FY27","99.0%")]:
    A("NUMBER",13,246,v,f"Revenue share US, {p}")
for p,v in [("Q2FY26","1.0%"),("Q1FY27","1.0%"),("Q2FY27","1.0%")]:
    A("NUMBER",13,246,v,f"Revenue share India, {p}")
data={"Technology":[73,72,68],"State/Local Government":[9,11,15],"Utilities":[7,9,8],"Others":[11,9,10]}
for k,v in data.items():
    for p,x in zip(["Q2FY26","Q1FY27","Q2FY27"],v):
        A("NUMBER",13,247,f"{x}.0%",f"Revenue share {k}, {p}")
for e in ["US","India"]:
    A("ENTITY",13,239,e,"revenue region")
for e in ["Technology","State / Local Government","Utilities","Others"]:
    A("ENTITY",13,247,e,"revenue industry segment")
for p in ["Q2FY26","Q1FY27","Q2FY27"]:
    A("DATE",13,242,p,"chart period axis")
A("QUALIFIER",13,246,"Region legend: India light shade, US dark shade; series mapping read from image","text layer lacks series mapping")
A("NUMBER",14,252,"12","new clients added Q2FY27")
A("NUMBER",14,253,"96","total active clients (LTM)")
A("NUMBER",14,254,"55%","top client revenue share")
A("NUMBER",14,255,"68%","top 3 clients revenue share")
A("NUMBER",14,258,"529","total employees as on 30 September 2026")
A("NUMBER",14,261,"136","number of projects")
A("DATE",14,258,"30 September 2026","employee count date")
A("QUALIFIER",14,253,"(LTM)","active client count measured over last twelve months")
A("QUALIFIER",14,254,"Top Client / Top 3 Client revenue: period basis not stated on slide","concentration period unstated")
A("QUALIFIER",14,261,"Number of Projects - 136: period basis not stated on slide","project count period unstated")
hdr=["Q2FY27","Q1FY27","QoQ growth","Q2FY26","YoY growth","H1FY27","H1FY26","H1 YoY growth"]
for i in range(308,337):
    ln=L[i]
    if " | " not in ln: continue
    parts=[x.strip() for x in ln.split("|")]
    name=re.sub(r"^\d+\s+","",parts[0]); vals=parts[1:]
    if vals==["(blank)"]: continue
    for j,v in enumerate(vals):
        if v=="" or j>=8: continue
        A("NUMBER",15,i+1,v,f"{name}, {hdr[j]}","ZERO_STANDING" if v=="-" else "")
for p,d in [("Q2FY27","30-Sep-26"),("Q1FY27","30-Jun-26"),("Q2FY26","30-Sep-25"),("H1FY27","30-Sep-26"),("H1FY26","30-Sep-25")]:
    A("DATE",15,268,d,f"P&L column date, {p}")
A("NUMBER",15,333,"Rs.10 per share","face value of equity share")
A("QUALIFIER",15,268,"Consolidated Unaudited Financial Statements","P&L is unaudited")
A("QUALIFIER",15,269,"(All figures in INR Million except EPS)","unit statement")
A("QUALIFIER",15,336,"Basic (Not annualised); Diluted (Not annualised)","EPS not annualised")
A("QUALIFIER",15,313,"Cost of Hardware / Software package/ for service delivery Outsourced project cost","line item label as printed")
A("QUALIFIER",15,266,"Raw text layer rows misaligned vs image; image-verified block (lines 308-337) governs","extractor alignment note, not a source claim")
A("ENTITY",15,266,"Consolidated Quarterly P&L - Q2FY27","slide title")
A("ENTITY",16,339,"Saumitra Banerjee","contact person")
A("ENTITY",16,341,"saumitra.banerjee@cybertech.com","contact email")
A("ENTITY-SUMMARY",16,343,"Copyright and trademark text: 2020 CyberTech copyright; CyberTech Logo trademark; no reproduction without prior written consent; product and company names are trademarks of their owners","legal boilerplate (grouped)")
A("QUALIFIER",16,344,"In addition to Company data, data from market research agencies, Stock Exchanges and industry publications has been used for this presentation.","data sourcing qualifier")
A("QUALIFIER",16,344,"This material was used during an oral presentation; it is not a complete record of the discussion.","completeness qualifier")
A("DATE",16,343,"2020","copyright year")
cnt={}
out=[]
for k,(t,p,l,v,c,f) in enumerate(rows,1):
    cnt[t]=cnt.get(t,0)+1
    out.append(f"R{k:03d} | page {p} | line {l} | {t} | {v} | {c}"+(f" | {f}" if f else ""))
n=len(rows)
hd=f"""=== A1 STRUCTURED EXTRACTION ===
source: Cybertech_Q2FY27_Earnings_Presentation_22Oct2026.pdf (doctype presentation, Q2 FY27)
fulltext: runs/cybertech-q2fy27/extracted/cybertech-presentation-q2fy27-fulltext.md (line numbers refer to that file, header included)
units: INR Million (x0.1 to Rs Crore); values verbatim, not converted
ID range: R001-R{n:03d}
counts: NUMBER {cnt.get('NUMBER',0)} | ENTITY {cnt.get('ENTITY',0)} (plus ENTITY-SUMMARY {cnt.get('ENTITY-SUMMARY',0)}) | FORWARD {cnt.get('FORWARD',0)} | DATE {cnt.get('DATE',0)} | QUALIFIER {cnt.get('QUALIFIER',0)}
page 15 note: raw text layer is row-shifted; rows anchored to the image-verified block (lines 308-337). Slides 12 and 13 chart rows anchored to the image-verified CHART lines (222-224, 246-247).
FORWARD note: the deck holds no guidance, targets or plans beyond the generic safe-harbor statement.
Row format: ID | page | line | TYPE | verbatim value | context | flag
=== END HEADER ===
"""
open("extracted/cybertech-presentation-q2fy27-structured.md","w",encoding="utf-8").write(hd+"\n".join(out)+"\n")
print(n,cnt)
