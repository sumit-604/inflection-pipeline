import json,re
exec(open('parse.py').read().split("for t in ['TARIL'")[0])
out=[]
for t in ['TARIL','VOLTAMP','SHILCTECH','DANISH','INDOTECH','SUPREMEPWR']:
    s=open(t+'.html',encoding='utf-8',errors='ignore').read()
    mc=float(re.search(r'Market Cap.*?<span class="number">([\d,\.]+)',s,re.S).group(1).replace(',',''))
    pe=re.search(r'Stock P/E.*?<span class="number">([\d,\.]+)',s,re.S).group(1)
    oa=json.load(open(t+'.oa.json'))
    cash=float(oa['Cash Equivalents']['Mar 2026'].replace(',',''))
    hdr,bs=table(s,'balance-sheet')
    bor=[v for k,v in bs.items() if 'Borrowings' in k][0][-1]; bor=float(bor.replace(',',''))
    inv=float(bs['Investments'][-1].replace(',',''))
    hdr,pl=table(s,'profit-loss')
    g=lambda k: float([v for kk,v in pl.items() if k in kk][0][-1].replace(',',''))
    op,oi,it,dp,pbt=g('Operating Profit'),g('Other Income'),g('Interest'),g('Depreciation'),g('Profit before tax')
    sales=g('Sales') if any('Sales' in k for k in pl) else None
    ebit_op=op-dp; ebit_all=pbt+it
    ev=mc+bor-cash; ev2=ev-inv
    out.append((t,mc,pe,bor,cash,inv,sales,op,oi,dp,it,pbt,ebit_op,ebit_all,ev,ev2))
    print(f"{t}: mcap {mc} PE {pe} debt {bor} cash {cash} inv {inv} | sales {sales} OP {op} OI {oi} Dep {dp} Int {it} PBT {pbt} | EBIT(op-dep) {ebit_op} EBIT(PBT+int) {ebit_all} | EV {ev} EV/EBITop {ev/ebit_op:.1f} EV-inv {ev2} -> {ev2/ebit_op:.1f} | Mcap/EBITop {mc/ebit_op:.1f}")
