import re,html
def table(s,sid):
    m=re.search(r'<section id="%s".*?</section>'%sid,s,re.S)
    if not m: return None
    sec=m.group(0)
    hdr=[re.sub('<.*?>','',h).strip() for h in re.findall(r'<th.*?>(.*?)</th>',sec,re.S)]
    rows={}
    for r in re.findall(r'<tr.*?>(.*?)</tr>',sec,re.S):
        cells=[re.sub(r'\s+',' ',html.unescape(re.sub('<.*?>','',c))).strip() for c in re.findall(r'<td.*?>(.*?)</td>',r,re.S)]
        if cells: rows[cells[0].replace('\xa0',' ').rstrip('+ ').strip()]=cells[1:]
    return hdr,rows
for t in ['TARIL','VOLTAMP','SHILCTECH','DANISH','INDOTECH','SUPREMEPWR']:
    s=open(t+'.html',encoding='utf-8',errors='ignore').read()
    print('=====',t, 'cash' in s.lower())
    for sid in ['quarters','profit-loss','balance-sheet']:
        r=table(s,sid)
        if not r: print(sid,'none'); continue
        hdr,rows=r
        print(sid,hdr[-5:])
        for k in ['Sales','Revenue','Operating Profit','Financing Profit','Other Income','Interest','Depreciation','Profit before tax','Net Profit','Borrowings','Investments','Other Assets','Total Assets']:
            if k in rows: print('  ',k,rows[k][-5:])
print('-----')
for t in ['TARIL','VOLTAMP','SHILCTECH','DANISH','INDOTECH','SUPREMEPWR']:
    s=open(t+'.html',encoding='utf-8',errors='ignore').read()
    hdr,rows=table(s,'balance-sheet')
    print(t,{k:v[-1] for k,v in rows.items()})
    hdr,rows=table(s,'profit-loss')
    print('  PL', {k:v[-2:] for k,v in rows.items() if k in ('Sales','Revenue','Other Income','Net Profit','EPS in Rs')})
    for m in re.finditer(r'[Cc]ash[^<]{0,60}',s): print('  ',m.group(0)[:80]); 
