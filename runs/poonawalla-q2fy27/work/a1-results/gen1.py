import json,re,datetime
body=open('body.txt',encoding='utf-8').read().rstrip('\n').split('\n')
HDR=[
"=== A1 EXTRACTION HEADER ===",
"source_filename: Poonawalla_Q2FY27_Results.pdf",
"doctype: results",
"page_count_pdfinfo: 30",
"formfeed_count: 30",
"line_count: @@LC@@",
"unit_convention: Crores (Rs in crores) for the financial statements, Reg 52(4) and Annexures I/II; exceptions: pages 20-21 QIP deviation statement in Rs million; pages 24-25 Annexure A in absolute rupees",
"conversion_factor_to_cr: Crores -> x1; Rs million -> x0.1; absolute rupees -> x0.0000001. Extracted text is NOT converted.",
"text_layer_present: yes",
"extraction_mode: text-only",
"render_candidates: [none; every page yields characters (min 287 chars on page 4). Pages 7-9, 13-15, 24-25 and 30 carry degraded OCR-style text (e.g. '2,4 l 5.54', garbled page 30 column headers); logged only, not rendered, per text-only rule]",
"rendered_pages: [none]",
"page_coverage: 100%",
"detected_quarter: Q2 FY27 (quarter and half year ended 30 September 2026)",
"extraction_date: 2026-10-17",
"layout_note: body below is pdftotext -layout output per page, preceded by [page N] markers on their own lines; the text layer of the source is an OCR layer for most financial pages, so digit glyphs are sometimes misread (I/l for 1, O/J for 0). Values are kept verbatim.",
"=== END HEADER ===",
""]
OFF=len(HDR)
full=HDR+body
LC=len(full)
full[5]=full[5].replace('@@LC@@',str(LC))
open('../../extracted/poonawalla-results-q2fy27-fulltext.md','w',encoding='utf-8').write('\n'.join(full)+'\n')
def FL(b): return b+OFF

rows={'NUMBER':[],'ENTITY':[],'FORWARD':[],'DATE':[],'QUALIFIER':[]}
def add(t,pg,bl,val,ctx,flag=''):
    rows[t].append((pg,bl,val,ctx,flag))
N=lambda *a:add('NUMBER',*a)
E=lambda *a:add('ENTITY',*a)
F=lambda *a:add('FORWARD',*a)
D=lambda *a:add('DATE',*a)
Q=lambda *a:add('QUALIFIER',*a)

T=json.load(open('tbl.json'))
PER={'PL':["Q2 FY27 (qtr ended 30 Sep 2026)","Q1 FY27 (qtr ended 30 Jun 2026)","Q2 FY26 (qtr ended 30 Sep 2025)","H1 FY27 (half year ended 30 Sep 2026)","H1 FY26 (half year ended 30 Sep 2025)","FY26 (year ended 31 Mar 2026)"],
 'BS':["as at 30 Sep 2026","as at 31 Mar 2026"],'CF':["H1 FY27 (half year ended 30 Sep 2026)","H1 FY26 (half year ended 30 Sep 2025)"]}
OV={('PL-C',290):'Profit before tax (1-2)',('PL-C',296):'Profit after tax (3-4)',('PL-C',301):'Income tax relating to items not reclassified to P&L (OCI)',
('PL-C',308):'Effective portion of gain/(loss) on hedging instruments in cash flow hedge (OCI)',('PL-C',311):'Income tax relating to items reclassified to P&L (OCI)',
('PL-C',314):'Total comprehensive income (5+6)',('PL-C',316):'Total comprehensive income attributable to Owners of the Company',
('PL-C',318):'Profit attributable to Owners of the Company',('PL-C',320):'OCI attributable to Owners of the Company',('PL-C',321):'Paid-up equity share capital (FV Rs 2 each)',
('PL-S',653):'Income tax relating to items not reclassified to P&L (OCI)',('PL-S',658):'Effective portion of gain/(loss) on hedging instruments in cash flow hedge (OCI)',
('PL-S',661):'Income tax relating to items reclassified to P&L (OCI)',('PL-S',665):'Paid-up equity share capital (FV Rs 2 each)',
('PL-C',325):'Basic EPS (Rs, not annualised)',('PL-C',326):'Diluted EPS (Rs, not annualised)',('PL-S',667):'Basic EPS (Rs, not annualised)',('PL-S',668):'Diluted EPS (Rs, not annualised)',
('BS-C',350):'[unlabelled subtotal] Total Financial Assets',('BS-C',360):'[unlabelled subtotal] Total Non-Financial Assets',('BS-C',376):'[unlabelled subtotal] Total Financial Liabilities',
('BS-C',381):'[unlabelled subtotal] Total Non-Financial Liabilities',('BS-C',385):'[unlabelled subtotal] Total Equity',
('BS-S',703):'[unlabelled subtotal] Total Financial Assets',('BS-S',714):'[unlabelled subtotal] Total Non-Financial Assets',('BS-S',732):'[unlabelled subtotal] Total Financial Liabilities',
('BS-S',738):'[unlabelled subtotal] Total Non-Financial Liabilities',('BS-S',743):'[unlabelled subtotal] Total Equity',
('PL-C',305):'Financial instruments through OCI (OCI, to be reclassified)',('PL-S',656):'Financial instruments through OCI (OCI, to be reclassified)'}
strict=re.compile(r'^\(?\d{1,3}(,\d{3})*\.\d\d\)?$|^\(?\d+\.\d\d\)?$')
for x in T:
    if x['ln']==323: continue
    k=x['t'][:2]; ent='consolidated' if x['t'].endswith('C') else 'standalone'
    lab=OV.get((x['t'],x['ln']),re.sub(r'\s+',' ',x['label']).strip())
    for c,v in sorted(x['cols'].items(), key=lambda kv:int(kv[0])):
        c=int(c); fl=[]
        if v.strip()=='-': fl.append('ZERO_STANDING')
        elif not strict.match(v.strip()): fl.append('OCR_SUSPECT')
        N(x['pg'],x['ln'],v,f"{ent} {lab}, {PER[k][c]}",' '.join(fl))

exec(open('manual.py',encoding='utf-8').read())

order=['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']
rid=0; out=[]; counts={}
for t in order:
    rs=sorted(rows[t],key=lambda r:(r[0],r[1]))
    counts[t]=len(rs)
    out.append(f"\n## {t} TABLE\n")
    for pg,bl,val,ctx,fl in rs:
        rid+=1
        out.append(f"R{rid:03d} | page {pg} | line {FL(bl)} | {t} | {val} | {ctx}"+(f" | FLAG: {fl}" if fl else ""))
total=rid
pg_of={}
cur=0
for i,l in enumerate(full,1):
    m=re.match(r'\[page (\d+)\]$',l)
    if m: cur=int(m.group(1))
    pg_of[i]=cur
bad=[]
for t in order:
    for pg,bl,val,ctx,fl in rows[t]:
        if pg_of[FL(bl)]!=pg: bad.append((t,pg,bl,pg_of[FL(bl)],val[:30]))
print('anchor mismatches',len(bad))
for b in bad[:60]: print(b)
head=[f"# A1 STRUCTURED EXTRACTION: Poonawalla Fincorp Limited (POONAWALLA), Q2 FY27 results filing (quarter and half year ended 30 September 2026)",
f"source_fulltext: runs/poonawalla-q2fy27/extracted/poonawalla-results-q2fy27-fulltext.md (line numbers below are lines of that file, header included, line_count {LC})",
f"ROW ID RANGE: R001-R{total:03d}",
f"COUNTS: NUMBER {counts['NUMBER']} | ENTITY {counts['ENTITY']} | FORWARD {counts['FORWARD']} | DATE {counts['DATE']} | QUALIFIER {counts['QUALIFIER']} | TOTAL {total}",
"UNITS: Rs crores for pages 7-19, 23, 26-30 unless stated; Rs million on pages 20-21 QIP table; absolute rupees on pages 24-25 Annexure A. Not converted.",
"ROW FORMAT: R### | page N | line L | TYPE | verbatim value | context | FLAG (optional)",
"FLAGS: ZERO_STANDING (dash/nil/zero), OCR_SUSPECT (token not a clean number or text-layer glyph error; value kept verbatim), OCR_SPACE (stray space inside digits), COLUMN_UNRESOLVED (column mapping not determinable from text layer), NOT_APPLICABLE, MISSING_VALUE, TEXT_TRUNCATED.",
"NOTE: standalone and consolidated statements (pages 13 and 7) are separate sets of rows; financial statement table rows are atomic by (line item x period) and anchored to the line holding the row's values.",
"NOTE: Pages 7-9, 13-15, 24-25, 30 carry OCR-quality text; page 30 (Annexure II) column headers are not recoverable from the text layer.",
""]
open('../../extracted/poonawalla-results-q2fy27-structured.md','w',encoding='utf-8').write('\n'.join(head+out)+'\n')
print(LC,total,counts)
json.dump(dict(lc=LC,total=total,counts=counts),open('summary.json','w'))
