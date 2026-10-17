rows=[]
N=[(1,18,"October 09, 2026","cover letter date"),(1,24,"524000","BSE scrip code"),(1,23,"400 001","BSE address pincode"),(1,23,"400 051","NSE address pincode"),(1,29,"2015","SEBI LODR Regulations year"),(1,28,"Regulation 30","SEBI LODR regulation cited"),(1,34,"September 30, 2026","quarter end, cover"),(1,50,"ACS-13918","company secretary membership no."),
(2,60,"Rs 74,008 crore","AUM, Q2FY27"),(2,61,"21.8% QoQ","PAT growth, Q2FY27"),(2,61,"Rs 375 crore","PAT, Q2FY27"),(2,67,"Rs 74,008 crore","AUM, Q2FY27"),(2,67,"2.18%","RoA, Q2FY27"),(2,67,"2.19%","credit cost, Q2FY27"),(2,68,"21 bps","credit cost reduction QoQ"),(2,68,"12.3% QoQ","NII growth, Q2FY27"),(2,68,"Rs 1,589 crore","NII, Q2FY27"),(2,73,"Rs 74,008 crore","AUM, Q2FY27"),(2,75,"Rs 375 crore","PAT, Q2FY27"),(2,75,"Rs 308 Crore","PAT, Q1FY27"),(2,77,"9.26%","NIM incl fees and other income, Q2FY27"),(2,77,"9.10%","NIM incl fees and other income, Q1FY27"),(2,78,"16 bps","NIM improvement QoQ"),(2,80,"2.18%","RoA, Q2FY27"),(2,80,"1.98%","RoA, Q1FY27"),(2,80,"1.81%","RoA, Q4FY26"),(2,83,"2.19%","credit cost % avg AUM, Q2FY27"),(2,83,"2.40%","credit cost % avg AUM, Q1FY27"),(2,86,"1.20%","GNPA, Q2FY27"),(2,86,"1.37%","GNPA, Q1FY27"),(2,88,"0.61%","NNPA, Q2FY27"),(2,88,"0.70%","NNPA, Q1FY27"),(2,90,"Rs 1,589 Crore","NII incl fees and other income, Q2FY27"),(2,90,"12.3% QoQ","NII growth, Q2FY27"),(2,92,"Rs 877 crore","PPoP, Q2FY27"),(2,92,"11.8% QoQ","PPoP growth, Q2FY27"),(2,94,"52:48","secured to unsecured on-book mix, Q2FY27"),(2,96,"97.9%","Stage 1 assets % on-book, Q2FY27"),(2,96,"97.6%","Stage 1 assets % on-book, Q1FY27"),(2,98,"18.68%","capital adequacy ratio, 30-Sep-2026"),(2,98,"17.15%","Tier-1 capital ratio, 30-Sep-2026"),(2,99,"15%","regulatory CAR requirement"),(2,101,"Rs 6,526 crore","liquidity buffer, 30-Sep-2026"),(2,103,"7.76%","cost of borrowing, Q2FY27"),(2,103,"4 bps","cost of borrowing increase vs Q1FY27"),(2,105,"42","new AI projects added, Q2FY27"),(2,105,"143","total AI projects"),(2,106,"84","AI projects implemented"),(3,125,"nearly three decades","operating history"),(3,128,"Rs 74,008 crore","AUM, 30-Sep-2026"),(3,128,"7,313","employees, 30-Sep-2026")]
E_=[(1,24,"Poonawalla Fincorp Limited","reporting company; NSE symbol POONAWALLA"),(1,19,"BSE Limited","exchange addressee"),(1,19,"National Stock Exchange of India Limited","exchange addressee"),(1,28,"Securities and Exchange Board of India","regulator, LODR"),(1,48,"Shabnum Zaman","Company Secretary, signatory"),(2,64,"Board of Directors of Poonawalla Fincorp Limited","announced results"),(3,108,"Mr. Arvind Kapil","MD and CEO, quoted"),(3,123,"Cyrus Poonawalla group","promoter group"),(3,124,"Reserve Bank of India (RBI)","regulator of the NBFC"),(3,126,"BSE Limited (BSE) / NSE","listing venues"),
(3,129,"Product lines: Loan Against Property, Gold Loans, Prime Personal Loans, Education Loans, Consumer Durable Loans, Business Loans, Instant Consumer Loans, Commercial Vehicle Loans, Mid-Market, Pre-Owned Car Finance, Loans for Professionals, Machinery Loans, Shopkeeper Loans","offering list, 13 products"),(3,135,"www.poonawallafincorp.com","website"),(3,136,"corporatecommunications@poonawallafincorp.com","media contact")]
F=[(2,64,"focusing on consumer and MSME finance","stated business focus"),(2,99,"CAR well above 15% requirement providing enough headroom for growth","growth headroom claim"),(3,111,"This quarter marks a decisive inflection point in establishing a highly resilient, self-sustaining earnings engine","CEO claim"),(3,112,"structural improvements across our four core performance vectors","CEO claim"),(3,114,"demonstrating strong pricing power across core and newly incubated verticals","CEO claim"),(3,116,"credit costs lower ... translating directly into a structural lift in RoA","CEO claim"),(3,117,"Accelerated by our rapidly maturing proprietary AI layer","CEO claim, AI"),(3,118,"gains reinforce the compounding power and long-term sustainability of our franchise","CEO claim")]
D=[(1,18,"October 09, 2026","cover letter date"),(1,34,"quarter ended September 30, 2026","results period"),(1,44,"Date: 2026.10.09 16:28:49 +05:30","digital signature timestamp"),(2,63,"Mumbai, October 09, 2026","press release dateline"),(2,65,"quarter ended September 30, 2026","results period"),(2,75,"Q2FY27 vs Q1FY27","PAT comparison periods"),(2,80,"Q4FY26","RoA comparison period"),(2,92,"quarter ended September 30, 2026","PPoP period"),(2,98,"as on September 30, 2026","CAR date"),(2,101,"as of September 30, 2026","liquidity buffer date"),(2,105,"this quarter (Q2FY27)","AI projects period"),(3,125,"nearly three decades back","operations start"),(3,128,"as on September 30, 2026","AUM and headcount date")]
Q=[(1,55,"Classification | INTERNAL","document classification marking"),(1,33,"Unaudited Financial Results","cover: results unaudited"),(2,65,"unaudited financial results","press release: results unaudited"),(2,77,"NIM (inc. fees and other income)","NIM includes fees and other income"),(2,83,"Credit cost as a percentage to average AUM","credit cost defined on average AUM"),(2,90,"Net Interest Income (inc. fees and other income)","NII includes fees and other income"),(2,96,"Stage 1 Assets ... of on-book assets","Stage 1 denominator is on-book assets"),(2,94,"Secured to Unsecured on-book mix","mix is on-book basis"),(2,98,"Tier-1 at 17.15%","Tier-1 stated within CAR 18.68%"),(2,68,"NII grew by 12.3% QoQ to Rs 1,589 crore","lead para omits the inc. fees qualifier"),(3,123,"non-deposit taking systemically important NBFC (ND-SI-NBFC)","entity classification")]
for T,L in (("NUMBER",N),("ENTITY",E_),("FORWARD",F),("DATE",D),("QUALIFIER",Q)):
    for p,l,v,c in L: rows.append((T,p,l,v,c))
cnt={};out=[]
for i,(t,p,l,v,c) in enumerate(rows,1):
    out.append("R%03d | page %d | line %d | %s | %s | %s"%(i,p,l,t,v,c)); cnt[t]=cnt.get(t,0)+1
hdr="""# A1 STRUCTURED EXTRACTION, Poonawalla Fincorp press release Q2FY27
ID range: R001-R%03d
Counts: NUMBER %d, ENTITY %d, FORWARD %d, DATE %d, QUALIFIER %d
Line numbers refer to the fulltext file (header included). Units: Rs crore. Rupee symbol rendered as Rs.
No ZERO_STANDING values. No asterisk or footnote markers in the document. No disclaimer text present.
Page 1 = Reg 30 cover letter; pages 2-3 = press release.

"""%(len(rows),cnt['NUMBER'],cnt['ENTITY'],cnt['FORWARD'],cnt['DATE'],cnt['QUALIFIER'])
open("extracted/poonawalla-pressrelease-q2fy27-structured.md","w",encoding="utf-8").write(hdr+"\n".join(out)+"\n")
y="""stage: A1-extractor
company: "POONAWALLA"
quarter: "q2fy27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
page_count: 3
formfeed_count: 3
line_count: 136
unit_convention: "Crores"
conversion_factor_to_cr: "x1"
text_layer_present: true
extraction_mode: text-only
render_candidates: []
rendered_pages: []
page_coverage_pct: 100
detected_quarter: "Q2 FY27"
fulltext_path: "runs/poonawalla-q2fy27/extracted/poonawalla-pressrelease-q2fy27-fulltext.md"
structured_path: "runs/poonawalla-q2fy27/extracted/poonawalla-pressrelease-q2fy27-structured.md"
structured_counts:
  number: %d
  entity: %d
  forward: %d
  date: %d
  qualifier: %d
structured_id_range: "R001-R%03d"
gate_a1: pass
gap_note: ""
"""%(cnt['NUMBER'],cnt['ENTITY'],cnt['FORWARD'],cnt['DATE'],cnt['QUALIFIER'],len(rows))
open("work/blocks/a1-pressrelease.yaml","w").write(y)
print(y)
