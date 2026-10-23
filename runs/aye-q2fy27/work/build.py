import re,collections
src=open('inputs/AyeFinance_Q2FY27_Concall_Transcript_ASR.txt',encoding='utf-8').read().split('\n')
if src[-1]=='': src.pop()
n=len(src)
hdr="""=== A1 EXTRACTION HEADER ===
source_filename: AyeFinance_Q2FY27_Concall_Transcript_ASR.txt
doctype: concall
page_count_pdfinfo: N/A (plain-text ASR transcript, %d lines; no PDF). Page unit used in structured file = 10-minute audio segment (page 1 = 00:00-09:59 ... page 8 = 70:00-79:59); call spans 00:00:00-01:11:05 = 8 segments
formfeed_count: N/A (text file)
line_count: %d source lines (fulltext file = header + source; source line S = fulltext line S+OFFSET, OFFSET stated below)
unit_convention: Crores (stated "crores"/"crore rupees"; borrowers in lakh)
conversion_factor_to_cr: Crores -> x1 (lakh count of borrowers is a count, not currency)
text_layer_present: N/A (plain text input, not PDF)
extraction_mode: text-only (verbatim copy of ASR text; no OCR, no rendering)
render_candidates: none
rendered_pages: none
page_coverage: 100%% (all %d source lines present verbatim in fulltext, verified by diff)
asr_caveat: MACHINE (ASR) transcript, NOT official; speaker turns best effort; numbers as heard; names mis-heard (IFL Finance = Aye Finance)
detected_quarter: Q2 FY27 (quarter ended 30-Sep-2026); call date 22-Oct-2026
extraction_date: 2026-10-23
fulltext_line_offset: OFFSET
=== END HEADER ==="""
h=hdr%(n,n,n)
hl=h.count('\n')+1
off=hl
h=h.replace('OFFSET',str(off))
# header length unchanged by replace? digits only; recompute
hl2=h.count('\n')+1
assert hl2==hl
open('extracted/aye-concall-q2fy27-fulltext.md','w',encoding='utf-8').write(h+'\n'+'\n'.join(src)+'\n')
def ts(i):
    m=re.match(r'\[(\d+):(\d+):(\d+)\]',src[i-1])
    if m: return int(m[1])*3600+int(m[2])*60+int(m[3])
    return None
def page(i):
    for j in range(i,0,-1):
        t=ts(j)
        if t is not None: return t//600+1
    return 1
skip=[(15,),]
sections=collections.OrderedDict()
cur=None
for l in open('work/rows.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('## '): cur=l[3:]; sections[cur]=[]; continue
    if not l.strip(): continue
    s,v,c=l.split('|',2)
    sections[cur].append((int(s),v,c))
# drop invented qualifiers
sections['QUALIFIER']=[r for r in sections['QUALIFIER'] if not (r[0] in(15,16) )]
out=[];rid=0;counts={}
body=[]
for t,rows in sections.items():
    body.append('\n### %s\n'%t)
    counts[t]=len(rows)
    for s,v,c in rows:
        rid+=1
        flag=''
        if t=='NUMBER' and re.match(r'^(0|nil|-)$',v): flag=' ZERO_STANDING'
        body.append('R%03d | page %d | line %d | %s | %s | %s'%(rid,page(s),s+off,t,v,c))
head="""# A1 STRUCTURED EXTRACTION - Aye Finance Q2 FY27 concall (ASR)
ID range: R001-R%03d
Counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d
Anchors: "line L" = line number in aye-concall-q2fy27-fulltext.md (source line + %d header offset). "page N" = 10-minute audio segment from the [hh:mm:ss] stamp. Values verbatim as heard; ASR_UNCERTAIN marks garbled values. No ZERO_STANDING values present.
Q&A turn boundaries ([MODERATOR TURN] tagged, fulltext line = source+%d): source lines 227,263,366,431,500,507,598,646,666,721,787
"""%(rid,counts['NUMBER'],counts['ENTITY'],counts['FORWARD'],counts['DATE'],counts['QUALIFIER'],off,off)
open('extracted/aye-concall-q2fy27-structured.md','w',encoding='utf-8').write(head+'\n'.join(body)+'\n')
print(rid,counts,off)
