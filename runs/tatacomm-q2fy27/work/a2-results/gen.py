import json,re,collections,subprocess
rows=json.load(open('work/a2-results/rows.json'))
R={r['id']:r for r in rows}
def n(i): return int(i[1:])
def rng(a,b): return [f'R{k:04d}' if k>=1000 else f'R{k:03d}' for k in range(a,b+1)]
def idf(k): return f'R{k:04d}' if k>=1000 else f'R{k:03d}'
def comp(ids):
    ids=sorted(set(ids),key=n); out=[];i=0
    while i<len(ids):
        j=i
        while j+1<len(ids) and n(ids[j+1])==n(ids[j])+1: j+=1
        out.append(ids[i] if i==j else f'{ids[i]}-{ids[j]}'); i=j+1
    return ','.join(out)
assigned={}
def put(ids,cat,grp):
    for i in ids:
        assert i not in assigned,(i,assigned.get(i),cat)
        assert i in R,i
        assigned[i]=(cat,grp)
def L(*spans):
    o=[]
    for s in spans:
        if isinstance(s,tuple): o+=rng(*s)
        else: o.append(s)
    return o
# ---------- NUMBER
foot=[r['id'] for r in rows if r['t']=='NUMBER' and 'pagination' in r['c']]
put(foot,'admin','page footer pagination')
put(L((1,5),(8,13),(16,18)),'admin','letter metadata (reference, addresses, pincodes, scrip code, regs, circular, CIN, phone)')
put(L('R006','R007'),'agenda','board meeting start and end times')
put(L('R014'),'agenda','A-3 appointment: membership number')
put(L('R015'),'signature','CS digital signature time (letter)')
put(L('R1323','R1324'),'signature','MD and CEO signature time and DIN (p20)')
put([i for i in L((703,717),(738,740),(1313,1322)) if i not in assigned],'note_numbers','numbers embedded in notes text')
put(L((1326,1331)),'auditor_num','auditor address, LODR reg, SRE standard')
put(L((1332,1334)),'auditor_num','emphasis paragraph references (DoT years, contingent liability, subsidiary tax)')
put(L((1335,1342)),'auditor_num','one subsidiary reviewed by other auditor (financials)')
put(L((1343,1351)),'auditor_num','two subsidiaries not reviewed by their auditors (count and financials)')
put(L((1352,1356)),'auditor_num','three associates not reviewed (count and group share)')
put(L((1357,1359)),'signature','consolidated report: ICAI firm reg, partner membership, UDIN')
put(L((1360,1361)),'auditor_num','standalone emphasis paragraph references')
put(L((1362,1364)),'signature','standalone report: ICAI firm reg, partner membership, UDIN')
put(L((1365,1371)),'press_num','press release headline claims (growth, margins, digital losses)')
put(L((1372,1392)),'press_num','press release Table 1 (7 lines x 3 cells)')
put(L((1393,1393)),'press_num','press release DC-to-DC opportunity figure')
put(L((1394,1401)),'press_num','press release awards, contacts, company profile counts')
put(L((1402,1410)),'attachD_num','Attachment D Kaleyra transfer figures')
put(L((1411,1417)),'attachE_num','Attachment E CS appointment details')
FIN_PAGES={3,4,5,6,7,8,9,10,13,14,15,16,17,18,19}
extra=set(L((667,702),(718,737)))
li=[r['id'] for r in rows if r['t']=='NUMBER' and r['id'] not in assigned and (r['pg'] in FIN_PAGES or r['id'] in extra)]
put(li,'line_item','')
left=[r['id'] for r in rows if r['t']=='NUMBER' and r['id'] not in assigned]
assert not left,left[:10]
# ---------- ENTITY
put(rng(1448,1522) and L((1448,1522)),'entity_consol','')
put([r['id'] for r in rows if r['t']=='ENTITY' and r['id'] not in assigned],'entity_other','')
# ---------- DATE groups
put(L((1582,1584),(1585,1585),(1643,1645),(1650,1652)),'date','A letter, press release and circular dates')
put(L((1587,1593),(1612,1614),(1624,1624),(1640,1640),(1646,1646),(1648,1649)),'date','B reporting-period and column dates')
put(L((1586,1586),(1622,1623),(1628,1629),(1641,1642)),'date','C signature, board approval and report dates')
put(L((1594,1594),(1615,1615)),'date','C2 board approval dates (notes 1)')
put(L((1595,1603),(1616,1621),(1625,1625),(1626,1627)),'date','D notes: exceptional items, Labour Codes, DoT/AGR timeline, subsidiary cash-flow periods')
put(L((1604,1611)),'date','E notes: VAT litigation timeline and discontinued ops dates')
put(L((1630,1639)),'date','F consolidation-list effective and cut-off dates (ENTITY_CHANGE)')
put(L((1647,1647)),'date','G award year labels')
assert all(r['id'] in assigned for r in rows if r['t']=='DATE'),[r['id'] for r in rows if r['t']=='DATE' and r['id'] not in assigned]
# ---------- FORWARD
put(L((1550,1552),(1574,1579)),'forward','Kaleyra transfer to TCNL (letter and Attachment D)')
put(L((1553,1554),(1580,1581)),'forward','CS appointment (letter and Attachment E)')
put(L((1555,1561)),'forward','notes: reorganisation, DoT defence, VAT appeal outcome')
put(L((1562,1566)),'forward','CEO quotes (H2 FY27 momentum, DC-to-DC, AI stack)')
put(L((1567,1570)),'forward','press release news items and Mint interview')
put(L((1571,1573)),'forward','data pack and disclaimer forward-looking language')
# ---------- QUALIFIER
note_re=re.compile(r'^R\d+ \| page \d+ \| line \d+ \| QUALIFIER \| ((Standalone )?[Nn]ote [0-9a-e]:|(Standalone )?[Rr]esults subjected|Rs 7,513)')
raw=open('extracted/tatacomm-results-q2fy27-structured.md',encoding='utf-8').read().split('\n')
note_ids=[l.split(' ')[0] for l in raw if note_re.match(l)]
put(note_ids,'note','')
fn_re=re.compile(r'^R\d+ \| page \d+ \| line \d+ \| QUALIFIER \| (\*|@|#|\$|i Figures|Figures in brackets|.*marker)')
fn_ids=[l.split(' ')[0] for l in raw if fn_re.match(l) and l.split(' ')[0] not in assigned]
put(fn_ids,'footnote','')
put(L((1766,1768)),'footnote_unres','')
put(L('R1653',(1745,1752),(1764,1765)),'auditor_para','')
put(L((1753,1762)),'qual_entity','')
put(L((1664,1669)),'qual_segdef','')
put(L('R1709','R1711','R1713','R1717','R1718','R1720','R1723','R1724','R1725','R1727','R1728','R1729'),'qual_defn','')
put(L((1772,1778)),'qual_legal','')
rest=[r['id'] for r in rows if r['t']=='QUALIFIER' and r['id'] not in assigned]
put(rest,'qual_xref','')
assert len(assigned)==len(rows)==1778
json.dump(assigned,open('work/a2-results/assigned.json','w'))
cat=collections.defaultdict(list)
for i,(c,g) in assigned.items(): cat[c].append(i)
print({k:len(v) for k,v in cat.items()})
print('notes',comp(note_ids)); print('fn',len(fn_ids),comp(fn_ids)); print('rest',comp(rest))
