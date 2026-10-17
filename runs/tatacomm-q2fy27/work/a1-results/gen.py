import re,sys
F='runs/tatacomm-q2fy27/extracted/tatacomm-results-q2fy27-fulltext.md'
L=open(F,encoding='utf-8').read().split('\n')
page={};p=0
for i,l in enumerate(L,1):
    m=re.match(r'\[page (\d+)\]$',l)
    if m:p=int(m.group(1))
    page[i]=p
C6=['Q2 FY27 (qtr 30-Sep-2026)','Q1 FY27 (qtr 30-Jun-2026)','Q2 FY26 (qtr 30-Sep-2025)','H1 FY27 (half yr 30-Sep-2026)','H1 FY26 (half yr 30-Sep-2025)','FY26 (yr 31-Mar-2026)']
A4=['30-Sep-2026','30-Jun-2026','30-Sep-2025','31-Mar-2026']
A2=['30-Sep-2026','31-Mar-2026']
CF=['H1 FY27','H1 FY26','FY26']
YOY=['Q2 FY27','Q2 FY26','YoY growth']
# (start,end,cols,ref line or None, basis)
blocks=[(135,167,C6,135,'consol P&L'),(188,214,C6,207,'consol P&L'),(234,254,C6,234,'consol segments'),
(269,285,A4,269,'consol segment A&L'),(317,346,A2,317,'consol BS'),(361,390,A2,361,'consol BS'),
(407,441,CF,407,'consol CF'),(458,491,CF,458,'consol CF'),(515,526,C6,515,'consol exceptional'),
(589,595,C6,None,'discontinued ops'),(621,653,C6,621,'standalone P&L'),(670,685,C6,670,'standalone segments'),
(693,705,A4,693,'standalone segment A&L'),(730,757,A2,730,'standalone BS'),(774,800,A2,774,'standalone BS'),
(814,861,CF,814,'standalone CF'),(875,887,CF,875,'standalone CF'),(902,915,C6,904,'standalone Reg52(4)'),
(928,954,A2,932,'standalone Reg52(4) ratios'),(972,983,C6,972,'standalone exceptional'),(1382,1388,YOY,1382,'press release Table 1')]
TOK=re.compile(r'(?:(?<=\s)|^)(\(?-?[\d,]*\d(?:\.\d+)?\)?%?(?:\s?bps)?[@#$*]*|-[@#$*]*)(?=\s{2,}|\s*$)')
def toks(s):
    out=[]
    for m in TOK.finditer(s):
        t=m.group(1)
        if re.fullmatch(r'\d+\.',t):continue
        out.append((t,m.end()))
    return out
rows=[]
def lab(i):
    s=L[i-1]
    m=re.search(r'\s{2,}(\(?-?[\d,]*\d|-)',s)
    base=s[:TOK.search(s).start()] if TOK.search(s) else s
    base=re.sub(r'\s+',' ',base).strip()
    k=i
    if len(base)<4 or re.fullmatch(r'[\d.]+\s*\S*',base):
        # borrow neighbours
        prev=re.sub(r'\s+',' ',L[i-2]).strip() if not toks(L[i-2]) else ''
        nxt=re.sub(r'\s+',' ',L[i]).strip() if i<len(L) and not toks(L[i]) else ''
        base=(prev+' '+base+' '+nxt).strip()
    return base[:90]
for (a,b,cols,ref,basis) in blocks:
    anchors=None
    if ref:
        rt=toks(L[ref-1]); rt=rt[-len(cols):]
        if len(rt)==len(cols): anchors=[e for _,e in rt]
    for i in range(a,b+1):
        tk=toks(L[i-1])
        if not tk:continue
        tk=tk[-len(cols):]
        for j,(t,e) in enumerate(tk):
            if anchors and len(tk)<len(cols) or (anchors and True):
                k=min(range(len(cols)),key=lambda x:abs(anchors[x]-e))
            else:
                k=len(cols)-len(tk)+j
            if basis=='discontinued ops': k=([0,1,2,4,5] if len(tk)==5 else [0,1,2])[j]
            flag=''
            if re.fullmatch(r'-[@#$*]*',t): flag=' ZERO_STANDING'
            rows.append((i,'NUMBER',t+flag,f'{lab(i)} | {cols[k]} | {basis}'))
for i,l in enumerate(L,1):
    if re.search(r'Page \d+ of 18',l):
        rows.append((i,'NUMBER',re.search(r'Page \d+ of 18',l).group(0),'page footer pagination'))
for i in range(1181,1263):
    m=re.match(r'\s*(\d+)\.\s{2,}(.+)',L[i-1])
    if m:
        sec='subsidiary' if i<1258 else 'associate'
        rows.append((i,'ENTITY',m.group(2).strip(),f'{sec} no. {m.group(1)} in auditor annexure list'))
exec(open('runs/tatacomm-q2fy27/work/a1-results/manual.py',encoding='utf-8').read())
order=['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']
out=[];n=0;cnt={}
for t in order:
    rs=sorted([r for r in rows if r[1]==t],key=lambda r:r[0])
    cnt[t]=len(rs)
    out.append(f'\n## {t} TABLE ({len(rs)} rows)\n')
    for r in rs:
        n+=1
        out.append(f'R{n:03d} | page {page[r[0]]} | line {r[0]} | {t} | {r[2]} | {r[3]}')
hdr=f'''# A1 STRUCTURED EXTRACTION - Tata Communications Limited (TATACOMM) - results Q2 FY27
source: TataComm_Q2FY27_Results_with_Press_Release.pdf | fulltext: tatacomm-results-q2fy27-fulltext.md (line numbers = file lines, header included)
unit: Crores (x1). Values verbatim; column labels in context are copied from table headers. Row format: R### | page | line | TYPE | value | context
ROW ID RANGE: R001-R{n:03d}
counts: NUMBER {cnt['NUMBER']} | ENTITY {cnt['ENTITY']} | FORWARD {cnt['FORWARD']} | DATE {cnt['DATE']} | QUALIFIER {cnt['QUALIFIER']} | TOTAL {n}
note: table cells with blank column (no value printed) emit no row. A "-" cell is a ZERO_STANDING row. Parenthesised values are negatives as printed. Row numbering prefixes in the source (e.g. "15") are not emitted as values.
'''
open('runs/tatacomm-q2fy27/extracted/tatacomm-results-q2fy27-structured.md','w',encoding='utf-8').write(hdr+'\n'.join(out)+'\n')
print(cnt,n)
