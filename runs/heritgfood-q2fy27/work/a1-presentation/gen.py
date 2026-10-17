import sys
d='work/a1-presentation/'
num=[]
for l in open(d+'rows_a.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if l: p=l.split('|'); num.append(('NUMBER',p[0],p[1],p[2],p[3],p[4] if len(p)>4 else ''))
BS=[(1247,"Equity share capital",464,464,464),(1248,"Reserve and surplus",7618,9256,10569),(1249,"Shareholders fund",8082,9720,11033),(1250,"Minority interest",0,0,48),(1251,"Total equity",8082,9720,11081),(1253,"Long-term borrowings",1095,1461,2543),(1254,"Deferred tax liabilities (net)",261,287,417),(1255,"Other long-term liabilities and provisions",302,350,519),(1256,"Total non-current liabilities",1658,2098,3479),(1258,"Short-term borrowings",226,283,1072),(1259,"Trade payables",1450,1715,2043),(1260,"Short term provisions",108,136,103),(1261,"Other current liabilities",1287,1631,1720),(1262,"Total current liabilities",3071,3766,4938),(1263,"Total equity and liability",12811,15583,19498),
(1248,"PPE",6968,7411,11395),(1249,"Capital WIP",201,680,466),(1250,"Intangible assets and investment property",76,65,246),(1251,"Investment in associate and JV",177,96,0),(1252,"Financial assets (non-current)",115,160,200),(1253,"Other non-current assets",25,320,221),(1254,"Total non-current assets",7561,8732,12562),(1256,"Inventories",2619,3552,3183),(1257,"Investments (current)",1222,1862,1855),(1258,"Trade receivables",287,380,712),(1259,"Cash and bank balances",838,697,703),(1260,"Loans",0,0,0),(1261,"Other current assets",283,360,484),(1262,"Total current assets",5250,6851,6936),(1263,"Total assets",12811,15583,19498)]
for ln,n,a,b,c in BS:
    for y,v in zip(("FY24","FY25","FY26"),(a,b,c)):
        num.append(('NUMBER','43',str(ln),f"{v:,}",f"{n} {y} (Rs Mn)","ZERO_STANDING" if v==0 else ""))
for ln,v in [(1274,"0.3"),(1275,"1.8"),(1276,"5.7"),(1277,"23.6"),(1278,"1.4"),(1280,"0.2"),(1281,"14.0"),(1282,"4.8"),(1295,"11.2"),(1295,"30.4"),(1296,"155.2"),(1296,"24.0"),(1299,"10.3"),(1299,"18.7"),(1300,"14.4"),(1301,"82.9")]:
    num.append(('NUMBER','44',str(ln),v,"ratio chart value (ratio/year mapping unresolved)","CHART_LABEL_UNMAPPED"))
rows={'NUMBER':num,'ENTITY':[],'FORWARD':[],'DATE':[],'QUALIFIER':[]}
for l in open(d+'rows_b.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if not l: continue
    p=l.split('|'); t=p[0]; k='ENTITY' if t=='ENTITY-SUMMARY' else t
    rows[k].append((t,p[1],p[2],p[3],p[4] if len(p)>4 else '',p[5] if len(p)>5 else ''))
# lines must map to correct page: verify
ft=open('extracted/heritgfood-presentation-q2fy27-fulltext.md',encoding='utf-8').read().split('\n')
pg=[0]*(len(ft)+2); cur=0
for i,x in enumerate(ft,1):
    if x.startswith('[page '): cur=int(x[6:-1])
    pg[i]=cur
bad=0
out=[];i=0
cnt={}
for k in ['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']:
    cnt[k]=len(rows[k])
tot=sum(cnt.values())
hdr=f"""=== A1 STRUCTURED EXTRACTION ===
source: Heritage_Q2FY27_Investor_Presentation.pdf (doctype presentation, Q2 FY27)
row_id_range: R001-R{tot:03d}
counts: NUMBER {cnt['NUMBER']} | ENTITY {cnt['ENTITY']} (incl. ENTITY-SUMMARY rows) | FORWARD {cnt['FORWARD']} | DATE {cnt['DATE']} | QUALIFIER {cnt['QUALIFIER']}
unit: Rs Mn (INR Mn) in financial slides; conversion to Rs Cr x0.1 (values NOT converted here)
line refs: line numbers are lines in the fulltext file (header block included)
row format: R### | page N | line L | TYPE | verbatim value | context | flag
flags: CHART_LABEL_UNMAPPED = value printed in a chart whose series/period cannot be resolved from the text layer; CHART_PERIOD_ORDER_INFERRED = period assigned by chart order and cross-check; COLUMN_UNRESOLVED; ZERO_STANDING; FOOTNOTE_UNRESOLVED
"""
out.append(hdr)
for k in ['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']:
    out.append(f"\n## {k} TABLE\n")
    for r in rows[k]:
        i+=1
        t,p,ln,v,c,f=r
        if pg[int(ln)]!=int(p):
            bad+=1; sys.stderr.write(f"MISMATCH {t} page {p} line {ln} -> actual page {pg[int(ln)]}: {v[:40]}\n")
        out.append(f"R{i:03d} | page {p} | line {ln} | {t} | {v} | {c}" + (f" | {f}" if f else ""))
open('extracted/heritgfood-presentation-q2fy27-structured.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(cnt,tot,bad)
