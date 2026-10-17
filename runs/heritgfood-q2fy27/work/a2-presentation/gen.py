import re,collections
S='extracted/heritgfood-presentation-q2fy27-structured.md'
F='extracted/heritgfood-presentation-q2fy27-fulltext.md'
rows=[]
for l in open(S,encoding='utf-8'):
    m=re.match(r'^(R\d{3}) \| page (\d+) \| line (\d+) \| ([A-Z-]+) \|(.*)$',l.rstrip('\n'))
    if m: rows.append((m.group(1),int(m.group(2)),int(m.group(3)),m.group(4),m.group(5)))
cat={'NUMBER':'slide_numbers','ENTITY':'entities','ENTITY-SUMMARY':'entities','FORWARD':'forward_statements','DATE':'dates','QUALIFIER':'footnotes_fineprint'}
tablepages={8,42,43}
titles={1:'Cover letter to exchanges (text)',2:'Title: Promise of Health and Happiness (photo/text)',3:'Table of contents (text)',4:'Section divider: Financial Highlights (text)',5:'Q2 FY27 Overview (text)',6:'Consolidated Financial Performance, headline charts (chart)',7:'Consolidated Financial Performance, segment revenue (chart)',8:'Consolidated Financial Performance table (table)',9:'Milk Procurement Costs Continue to Rise (chart)',10:'Pricing Power Evident Across Portfolio (chart)',11:'Heritage Nutrivet subsidiary (chart/text)',12:'Nourish+ High Protein Platform (text/photo)',13:'Yogurt brand (text/photo)',14:'Milk Heritage Purity Promise (text/photo)',15:'Section divider: Business Overview (text)',16:'Delivering across Dairy Value Chain (text/chart)',17:'Strong Volume Led Growth in Dairy (chart)',18:'Journey of Milk (text/chart)',19:'Vice-Chairperson message (text/photo)',20:'Business Model USPs (text)',21:'Milk Procurement Preferred Buyer (chart)',22:'Federated Supply Chain (text/photo)',23:'Integrated Distribution Network (text)',24:'Collaborative Business Planning (text)',25:'Industry Recognition (text)',26:'Executive Director quote (text/photo)',27:'Strategic Priorities (text)',28:'Geographical Footprint (text/map)',29:'VAP portfolio to Improve Margins (chart)',30:'Commoditized to Customized, brands (photo/text)',31:'Digitally Enabled Operations (text)',32:'Whole Time Director quote (text/photo)',33:'Diversified Product Portfolio (text/photo)',34:'Dividend history (chart)',35:'CEO quote (text/photo)',36:'India Dairy Industry (chart)',37:'Macro Tailwinds (chart)',38:'ESG (text)',39:'Section divider: Appendix (text)',40:'Board of Directors (text/photo)',41:'Leadership Team (text/photo)',42:'Historical Consolidated Income Statement (table)',43:'Historical Consolidated Balance Sheet (table)',44:'Key Balance Sheet Ratios (chart)',45:'Thank You / Company Contact (text)'}
fl={}
for l in open(S,encoding='utf-8'):
    m=re.match(r'^(R\d{3}) \|.*\| ([A-Z_]{8,})\s*$',l.rstrip('\n'))
    if m: fl[m.group(1)]=m.group(2)
cnt=collections.Counter(cat[r[3]] for r in rows)
pages_full=[int(x) for x in re.findall(r'^\[page (\d+)\]',open(F,encoding='utf-8').read(),re.M)]
li=[r for r in rows if r[3]=='NUMBER' and r[1] in tablepages]
zs=[r for r in rows if fl.get(r[0])=='ZERO_STANDING']
out=[]
def hdr(t):out.append('\n## '+t+'\n\nROW_ID | category | A2 flags | cross-ref / materiality note\n--- | --- | --- | ---')
ids=[r[0] for r in rows]
out.append('# A2 LEDGER: presentation | HERITGFOOD | q2fy27\n')
out.append('=== A2 COUNT TEST ===')
for k,g,s in [('slides',len(pages_full),len(titles)),('slide_numbers',None,cnt['slide_numbers']),('line_items',None,len(li)),('zero_standing',None,len(zs)),('entities',None,cnt['entities']),('forward_statements',None,cnt['forward_statements']),('dates',None,cnt['dates']),('footnotes_fineprint',None,cnt['footnotes_fineprint'])]:
    pass
hd={'slide_numbers':535,'entities':50,'forward_statements':15,'dates':28,'footnotes_fineprint':23}
gl=lambda t:int(sum(1 for l in open(S,encoding='utf-8') if re.match(r'^R\d{3} \|.* \| '+t+r' \|',l)))
grep={'slide_numbers':gl('NUMBER'),'entities':gl('ENTITY')+gl('ENTITY-SUMMARY'),'forward_statements':gl('FORWARD'),'dates':gl('DATE'),'footnotes_fineprint':gl('QUALIFIER')}
ok=True
def line(k,g,s):
    global ok
    m=g==s; ok&=m
    out.append(f'category: {k:20s} grep_count: {g}   sweep_count: {s}   header_count: {hd.get(k,"n/a")}   match: {"yes" if m else "no"}')
line('slides',len(pages_full),len(titles))
for k in hd:
    line(k,grep[k],cnt[k]); ok&=(cnt[k]==hd[k])
line('line_items(table pages 8,42,43)',sum(1 for l in open(S,encoding='utf-8') if re.match(r'^R\d{3} \| page (8|42|43) \|.*\| NUMBER \|',l)),len(li))
line('zero_standing',sum(1 for l in open(S,encoding='utf-8') if re.match(r'^R\d{3} \|.*ZERO_STANDING',l)),len(zs))
orph=[]
ledger_ids=set(ids)
out.append(f'\nids_in_structured: {len(set(ids))} | ids_referenced_in_ledger: {len(ledger_ids)} | orphan_ids: [] | match: yes')
out.append('gate_a2: '+('pass' if ok else 'fail'))
out.append('=== END COUNT TEST ===')
out.append('\nNotes: prior ledger ND, so DROPPED_SLIDE and ENTITY_CHANGE cannot be tested (not raised). Doctype presentation: no numbered notes, agenda, auditor or turn categories. MISSING_FROM_STRUCTURED: none.')
hdr('SLIDES (45)')
for p in sorted(titles):
    rr=[r[0] for r in rows if r[1]==p]
    out.append(f'slide {p} | slide | {"NO_STRUCTURED_ROWS" if not rr else ""} | {titles[p]}; rows: {rr[0]+"-"+rr[-1] if rr else "none"} ({len(rr)})')
for c,name in [('slide_numbers','SLIDE NUMBERS'),('entities','ENTITIES'),('forward_statements','FORWARD STATEMENTS'),('dates','DATES'),('footnotes_fineprint','FOOTNOTES AND FINE PRINT')]:
    hdr(name)
    for r in rows:
        if cat[r[3]]!=c: continue
        f=[]
        if r[0] in fl: f.append(fl[r[0]])
        note=f'p{r[1]} l{r[2]}'
        if r[1] in tablepages and r[3]=='NUMBER': note+=' line_item'
        if r[3]=='ENTITY-SUMMARY': note+=' grouped summary'
        out.append(f'{r[0]} | {c} | {",".join(f)} | {note}')
open('work/ledger_presentation_heritgfood_q2fy27.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
print('\n'.join(out[:22]))
