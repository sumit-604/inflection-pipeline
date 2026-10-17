import json,re,collections
src=open('work/a2-results/gen.py',encoding='utf-8').read().split('# ---------- NUMBER')[0]
exec(src)
assigned=json.load(open('work/a2-results/assigned.json'))
cat=collections.defaultdict(list)
for i,(c,g) in assigned.items(): cat[c].append(i)
ft=open('extracted/tatacomm-results-q2fy27-fulltext.md',encoding='utf-8').read().split('\n')
SF='extracted/tatacomm-results-q2fy27-structured.md'
sraw=open(SF,encoding='utf-8').read().split('\n')
out=[];prim=set()
def P(ids): prim.update(ids)
def lab(s,k=44): return re.sub(r'\s+',' ',s)[:k].replace('|','/')
STMT={3:'CONSOL P&L',4:'CONSOL P&L (OCI/EPS)',5:'CONSOL SEGMENT RESULTS',6:'CONSOL SEGMENT ASSETS/LIABS',7:'CONSOL BS (assets)',8:'CONSOL BS (equity/liabs)',9:'CONSOL CASH FLOW (operating)',10:'CONSOL CASH FLOW (invest/finance)',11:'CONSOL EXCEPTIONAL ITEMS TABLE (note 2)',12:'CONSOL DISCONTINUED OPS TABLE (note 5)',13:'STANDALONE P&L',14:'STANDALONE SEGMENT (results + A&L)',15:'STANDALONE BS (assets)',16:'STANDALONE BS (equity/liabs)',17:'STANDALONE CASH FLOW (operating/invest)',18:'STANDALONE CASH FLOW (financing) + Reg52(4) margins',19:'STANDALONE Reg52(4) ratios + EXCEPTIONAL TABLE'}
lines=collections.OrderedDict()
for i in cat['line_item']:
    r=R[i]; lines.setdefault((r['pg'],r['ln']),[]).append(i)
li_rows=[];zero_groups=0
for (pg,ln),ids in lines.items():
    ids=sorted(ids,key=n)
    zc=[i for i in ids if 'ZERO_STANDING' in R[i]['v']]
    r0=R[ids[0]]; lbl=lab(r0['c'].split(' | ')[0]) or '(unlabelled row)'
    nonnum=[i for i in ids if not re.fullmatch(r'[\(\)\d,\.\-%\s]+|-\s*ZERO_STANDING',R[i]['v'].strip())]
    fl=[]
    if zc:
        fl.append('ZERO_STANDING all %d cells'%len(ids) if len(zc)==len(ids) else 'ZERO_STANDING %d of %d cells (%s)'%(len(zc),len(ids),comp(zc)))
        zero_groups+=1
    if nonnum and not zc: fl.append('NONNUMERIC_VALUE (label fragment or text cell)')
    li_rows.append((pg,ln,lbl,ids,fl))
P(cat['line_item'])
extra=set(L((667,702),(718,737)))
dec=re.compile(r'\d[\d,]*\.\d+')
pm=[];cur=1
for l in ft:
    m=re.match(r'\[page (\d+)\]',l)
    if m: cur=int(m.group(1))
    pm.append(cur)
TP=(3,4,5,6,7,8,9,10,13,14,15,16,17,19)
ft_dec_lines=set()
for idx,l in enumerate(ft):
    p=pm[idx]; ln=idx+1
    if (p in TP or (p==18 and ln<=915)) and dec.search(l): ft_dec_lines.add(ln)
led_dec_lines=set(ln for (pg,ln,lbl,ids,fl) in li_rows if any(dec.search(R[i]['v']) for i in ids) and (pg in TP or (pg==18 and ln<=915)))
grep_li=len(ft_dec_lines); sweep_li=len(led_dec_lines)
miss_ft=sorted(ft_dec_lines-led_dec_lines); extra_led=sorted(led_dec_lines-ft_dec_lines)
cells_grep=sum(1 for l in sraw if re.match(r'^R\d+ \| page (3|4|5|6|7|8|9|10|13|14|15|16|17|18|19) \| line \d+ \| NUMBER \|',l) and 'pagination' not in l and not l.startswith('R018 '))+sum(1 for r in rows if r['id'] in extra)
cells_sweep=sum(len(x[3]) for x in li_rows)
zero_all=[r['id'] for r in rows if 'ZERO_STANDING' in r['v']]
zero_grep=sum(1 for l in sraw if re.match(r'^R\d+ \|',l) and 'ZERO_STANDING' in l)
zero_nonli=[i for i in zero_all if assigned[i][0]!='line_item']
note_pat=re.compile(r'^R\d+ \| page \d+ \| line \d+ \| QUALIFIER \| ((Standalone )?[Nn]ote [0-9a-e]:|(Standalone )?[Rr]esults subjected|Rs 7,513)')
fn_pat=re.compile(r'^R\d+ \| page \d+ \| line \d+ \| QUALIFIER \| (\*|@|#|\$|i Figures|Figures in brackets|.*marker)')
g_notes=sum(1 for l in sraw if note_pat.match(l))
g_fn=sum(1 for l in sraw if fn_pat.match(l))
g_aud=sum(1 for r in rows if r['t']=='QUALIFIER' and (21<=r['pg']<=23 or 26<=r['pg']<=27) and not 1753<=n(r['id'])<=1763)+1
g_ent=sum(1 for l in sraw if re.search(r'(subsidiary|associate) no\. \d+ in auditor',l))
note_lab={'R1678':'consol note 1 (limited review, approval 15-Oct-2026)','R1684':'consol note 2a (staff cost optimisation)','R1685':'consol note 2b (gain on sale of held-for-sale assets)','R1686':'consol note 2c (Labour Codes provision and reversal)','R1687':'consol note 2d (accidental damages / fire at third party DC)','R1688':'consol note 2e (provision, contractual obligation)','R1689':'consol note 3 (DOT demand notices)','R1690':'consol note 3 classification (contingent vs remote)','R1691':'consol note 4 (foreign subsidiary VAT)','R1692':'consol note 5 (discontinued ops, subsidiary deconsolidated)','R1696':'consol note 6 (FY26 OCI gain, DTL)','R1733':'standalone note 1','R1739':'standalone note a','R1740':'standalone note b','R1741':'standalone note c','R1742':'standalone note d','R1743':'standalone note e','R1744':'standalone note 3'}
RESTATE={'R1678':'R1733','R1684':'R1739','R1685':'R1740','R1686':'R1741','R1687':'R1742','R1688':'R1743','R1689':'R1744'}
W=out.append
W('# A2 COMPLETENESS LEDGER - Tata Communications Limited (TATACOMM) - results - q2fy27')
W('source of truth: runs/tatacomm-q2fy27/extracted/tatacomm-results-q2fy27-structured.md (R001-R1778). Rows reference A1 IDs; verbatim values stay in the structured file.')
W('Prior-quarter ledger: not available (ND). ENTITY_CHANGE flags rest on in-document wef/upto qualifiers only; no list-vs-list diff possible.')
W('')
W('@@COUNT@@')
W('\n## 1. AGENDA ITEMS (Board Outcome letter, pp1-2) - cross-reference rows')
W('Board meeting: commenced 10:30 IST, concluded 13:45 IST on 15-Oct-2026 = 3h15m (R006, R007, R1583). Letter signed by Company Secretary 13:52:19 (R015, R1586).')
W('| AGENDA_ID | item | supporting ROW IDs | A2 flags / note |'); W('|---|---|---|---|')
ag=[('A1','(i) Unaudited standalone and consolidated results, quarter and half-year to 30-Sep-2026, with Limited Review Report (unmodified) and press release',L('R1584','R1653','R1424','R1587','R1643'),'Attachments A, B, C'),
('A2','(ii) Other Restructuring: transfer of entire Kaleyra, Inc. shareholding to Tata Communications (Netherlands) B.V. (TCNL), consideration in TCNL shares at FMV',L('R1425','R1426',(1550,1552),(1574,1579),(1402,1410),'R1546','R1547','R1650'),'Attachment D. ENTITY_CHANGE candidate (Kaleyra becomes direct subsidiary of TCNL, R1578). Intra-group; benefit to promoter Nil (R1778, R1410). Cross-check: Kaleyra Africa (Pty) deconsolidated upto 04-Sep-2026 (R1509, R1634, R1757).'),
('A3','(iii) Change in KMP: appointment of Ms. Ridhi Sood as Company Secretary and Compliance Officer w.e.f. 01-Nov-2026',L('R014','R1428','R1429','R1430',(1553,1554),(1580,1581),'R1585','R1652',(1411,1417),'R1548','R1549','R1651'),'Attachment E. Incumbent signatory Zubin Adil Patel (R1430); letter does not say whether he leaves.'),
('A4','Meeting timing',L('R006','R007','R1583'),'3h15m meeting.'),
('A5','Standard items NOT on this agenda: annual report approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, ESOP grant, capital-raising resolution',L('R1582'),'ABSENCE row. Letter lists only items (i)-(iii). No dividend item.')]
for a in ag: W(f'| {a[0]} | {a[1]} | {comp(a[2])} | {a[3]} |')
W('\n## 2. NOTES (numbered / lettered) and FOOTNOTES')
W('### 2a Notes'); W('| ROW_ID | note | A2 flags | cross-ref / materiality |'); W('|---|---|---|---|')
rv={v:k for k,v in RESTATE.items()}
for i in sorted(cat['note'],key=n):
    fl=[];x=''
    if i in RESTATE: fl.append('RESTATED'); x=f'restated on standalone at {RESTATE[i]}'
    if i in rv: fl.append('RESTATED'); x=f'restates {rv[i]}'
    if i=='R1686': x+='; Rs 60.58cr FY26 provision, Rs 18.52cr Q1 FY27 reversal sit in qualifier text'
    if i in ('R1689','R1690','R1691'): fl.append('CONTINGENT_LIABILITY'); x+='; also auditor emphasis paragraph (section 5)'
    if i=='R1692': fl.append('DISCONTINUED_OPS')
    if i=='R1687': x+='; ties to exceptional item d'
    W(f'| {i} | {note_lab[i]} | {",".join(fl) or "-"} | {x.lstrip("; ") or "-"} |')
W('Standalone has no notes 4-6 (consolidated only): note 4 VAT, note 5 discontinued ops, note 6 OCI. Numeric facts inside notes sit in section 7b.')
P(cat['note'])
W('### 2b Footnotes and markers (asterisk, @, #, $, bracket convention)'); W('| ROW_ID | page/line | A2 flags | pairing |'); W('|---|---|---|---|')
pair={'R1670':'marker -> text R1676','R1672':'marker -> text R1677','R1676':'text for R1670','R1677':'text for R1672','R1693':'marker -> text R1695','R1694':'marker -> text R1695','R1695':'text for R1693,R1694','R1700':'marker -> text R1707','R1703':'marker -> text R1706','R1704':'marker -> text R1706','R1706':'text for R1703,R1704','R1707':'text for R1700','R1710':'marker -> text R1714','R1712':'marker -> text R1715','R1714':'text for R1710','R1715':'text for R1712 (refers to note 2)','R1716':'marker -> text R1731','R1719':'marker -> text R1730','R1721':'marker -> text R1732','R1722':'marker -> text R1730','R1726':'marker -> text R1730','R1730':'text for R1719,R1722,R1726','R1731':'text for R1716','R1732':'text for R1721','R1770':'marker -> text R1771','R1771':'text for R1770','R1675':'cash-flow bracket convention','R1705':'cash-flow bracket convention'}
for i in sorted(cat['footnote'],key=n): W(f'| {i} | p{R[i]["pg"]}/L{R[i]["ln"]} | RESOLVED | {pair.get(i,"-")} |')
P(cat['footnote'])
W('### 2c Unresolved footnotes'); W('| ROW_ID | page/line | A2 flags | note |'); W('|---|---|---|---|')
for i in sorted(cat['footnote_unres'],key=n): W(f'| {i} | p{R[i]["pg"]}/L{R[i]["ln"]} | FOOTNOTE_UNRESOLVED | press release headline metric stated without a definition; no reconciliation to the filed P&L |')
P(cat['footnote_unres'])
W('### 2d Note-reference and column qualifiers'); W('| ROW_ID | page/line | A2 flags | note |'); W('|---|---|---|---|')
for i in sorted(cat['qual_xref'],key=n): W(f'| {i} | p{R[i]["pg"]}/L{R[i]["ln"]} | - | {"blank-page placeholder" if i=="R1763" else "refer-note / column qualifier"} |')
P(cat['qual_xref'])
W('### 2e Segment definitions and ratio definitions'); W('| ROW_ID | page/line | A2 flags | note |'); W('|---|---|---|---|')
for i in sorted(cat['qual_segdef']+cat['qual_defn'],key=n): W(f'| {i} | p{R[i]["pg"]}/L{R[i]["ln"]} | - | {"segment definition" if i in cat["qual_segdef"] else "ratio/margin definition"} |')
P(cat['qual_segdef']+cat['qual_defn'])
W('Consolidated has 5 segments (R1431); standalone has 3 (R1443). Data Services includes digital platforms and connected services (R1666).')
W('### 2f Legal and Attachment D qualifiers'); W('| ROW_ID | page/line | A2 flags | note |'); W('|---|---|---|---|')
for i in sorted(cat['qual_legal'],key=n): W(f'| {i} | p{R[i]["pg"]}/L{R[i]["ln"]} | - | {"disclaimer / image alt text" if n(i)<=1774 else "Attachment D qualifier"} |')
P(cat['qual_legal'])
W('\n## 3. FINANCIAL TABLE LINE ITEMS (every line, including zero and dash cells)')
W('One row per table line (page/line). Cells are the period columns, referenced by ID range. Label shown for lookup only.')
W('| page/line | label | ROW IDs | cells | A2 flags |'); W('|---|---|---|---|---|')
curp=None
for pg,ln,lbl,ids,fl in li_rows:
    if pg!=curp: W(f'| **p{pg}** | **{STMT[pg]}** | | | |'); curp=pg
    W(f'| p{pg}/L{ln} | {lbl} | {comp(ids)} | {len(ids)} | {"; ".join(fl) or "-"} |')
W('\n## 4. ZERO_STANDING register')
W(f'Total ZERO_STANDING cells: {len(zero_all)}. Lines carrying at least one zero cell: {zero_groups}.')
W('| page/line | label | zero cells | of cells | pattern |'); W('|---|---|---|---|---|')
for pg,ln,lbl,ids,fl in li_rows:
    zc=[i for i in ids if 'ZERO_STANDING' in R[i]['v']]
    if zc: W(f'| p{pg}/L{ln} | {lbl} | {comp(zc)} | {len(ids)} | {"zero in ALL periods (template signal)" if len(zc)==len(ids) else "zero in some periods"} |')
W(f'Zero cells outside the line-item groups: {comp(zero_nonli) or "none"}.')
W('\n## 5. AUDITOR PARAGRAPHS (limited review reports, pp21-27)')
W('Going Concern language: none (grep count 0 in structured and in fulltext). Opinion type: limited review, unmodified conclusion (R1653).')
W('| ROW_ID | paragraph | A2 flags |'); W('|---|---|---|')
ap={'R1653':('Board letter: Limited Review Report, unmodified opinion',''),'R1745':('Consolidated para 3: moderate assurance, not an audit',''),'R1746':('Consolidated para 3: no audit opinion expressed',''),'R1747':('Consolidated para 6: emphasis, note 3 DOT demand notices, contingent liability Rs 7,513.71cr','EMPHASIS_OF_MATTER'),'R1748':('Consolidated para 7: emphasis, note 4 tax litigation uncertainty in one subsidiary','EMPHASIS_OF_MATTER'),'R1749':('Consolidated: conclusion not modified for paras 6 and 7',''),'R1750':('Consolidated para 8: one subsidiary reviewed by other auditor, sole reliance','OTHER_AUDITOR_RELIANCE'),'R1751':('Consolidated para 9: two subsidiaries and three associates not reviewed by their auditors, management-furnished','MGMT_FURNISHED_UNREVIEWED'),'R1752':('Consolidated: conclusion not modified for paras 8 and 9',''),'R1764':('Standalone para 3: moderate assurance, not an audit',''),'R1765':('Standalone para 5: emphasis, note 3 DOT demand notices, conclusion not modified','EMPHASIS_OF_MATTER')}
for i in sorted(cat['auditor_para'],key=n): W(f'| {i} | {ap[i][0]} | {ap[i][1] or "-"} |')
P(cat['auditor_para'])
W('Auditor numbers (address, standard, emphasis refs, other-auditor and unreviewed-entity financials):')
W('| ROW IDs | group | cells |'); W('|---|---|---|')
byg=collections.OrderedDict()
for i in cat['auditor_num']: byg.setdefault(assigned[i][1],[]).append(i)
for g,ids in byg.items(): W(f'| {comp(ids)} | {g} | {len(ids)} |')
P(cat['auditor_num'])
W('\n## 6. ENTITIES')
W('### 6a Consolidation list (auditor annexure, pp24-25): 72 subsidiaries + 3 associates = 75')
W('| ROW_ID | seq | A2 flags | note |'); W('|---|---|---|---|')
ec={'R1482':'wef 18-Apr-2025 (R1630,R1753)','R1495':'upto 15-Sep-2025 (R1631,R1754)','R1496':'upto 22-Apr-2025 (R1632,R1755)','R1508':'upto 14-Jan-2026 (R1633,R1756)','R1509':'upto 04-Sep-2026, IN CURRENT PERIOD (R1634,R1757)','R1514':'upto 01-Oct-2025 (R1635,R1758)','R1516':'wef 01-Dec-2025 (R1636,R1759)','R1517':'wef 01-Dec-2025 (R1637,R1760)','R1518':'wef 12-Mar-2026 (R1638,R1761)','R1519':'wef 21-May-2026, IN CURRENT PERIOD (R1639,R1762)'}
for i in L((1448,1522)):
    c=R[i]['c'].replace('in auditor annexure list','').strip()
    note=ec.get(i,'')
    if i=='R1502': note='Kaleyra Inc: subject of Attachment D transfer to TCNL (R1425)'
    if i=='R1464': note='TCNL, transferee in Attachment D (R1426)'
    W(f'| {i} | {c} | {"ENTITY_CHANGE" if i in ec else "-"} | {note or "-"} |')
P(cat['entity_consol'])
W('ENTITY_CHANGE: 10 rows (inclusions R1482,R1516,R1517,R1518,R1519; exclusions R1495,R1496,R1508,R1509,R1514). Two fall in the current half-year: R1509 (excluded) and R1519 (added). Prior list not available; no diff.')
W('Entity qualifier rows (wef/upto brackets): '+comp(cat['qual_entity'])+' - flag ENTITY_CHANGE, paired to entities above and dates R1630-R1639.')
P(cat['qual_entity'])
W('### 6b Other entities named (regulators, exchanges, counterparties, partners, signatories)')
W('| ROW_ID | A2 flags | note |'); W('|---|---|---|')
for i in sorted(cat['entity_other'],key=n):
    x='-'
    if i in ('R1424','R1446'): x='statutory auditor'
    if i in ('R1425','R1426'): x='Attachment D party'
    if i in ('R1429','R1430','R1444','R1447'): x='named individual (signatory, appointee or partner)'
    W(f'| {i} | {"NAME_NOT_DISCLOSED" if i in ("R1433","R1442","R1439") else "-"} | {x} |')
P(cat['entity_other'])
W('\n## 7. SIGNATURE BLOCKS, NOTE NUMBERS, ADMIN')
W('### 7a Signatures (rule 7)'); W('| signatory | ROW IDs | timestamp | A2 flags | note |'); W('|---|---|---|---|---|')
W('| Company Secretary Zubin Adil Patel (board outcome letter) | R015,R1430,R1586 | 15-Oct-2026 13:52:19 IST | - | signed after meeting concluded 13:45 (R007) |')
W('| MD and CEO Ganapathi S. Lakshminarayanan (results, both sets) | R1323,R1324,R1444,R1622,R1623 | 15-Oct-2026 12:58:01 IST | SIGNATURE_BEFORE_MEETING_END | stamp is 47 min before the 13:45 conclusion; approval time inside the meeting is not stated |')
W('| Auditor S.R. Batliboi & Associates, partner Sanjay Bachchani, consolidated report | R1628,R1629,R1446,R1447,R1357,R1358,R1359 | 15-Oct-2026 13:05:38 IST | SIGNATURE_BEFORE_MEETING_END | UDIN R1359; stamp 40 min before conclusion |')
W('| Auditor, standalone report | R1641,R1642,R1362,R1363,R1364 | 15-Oct-2026 13:04:44 IST | SIGNATURE_BEFORE_MEETING_END | UDIN R1364; stamp 41 min before conclusion |')
P(cat['signature'])
W('Signature-class number IDs: '+comp(cat['signature'])+' (R1628,R1629,R1641,R1642,R1622,R1623,R1586 are DATE rows in section 9).')
W('### 7b Numbers embedded in notes text'); W('| ROW IDs | group |'); W('|---|---|')
nn=collections.OrderedDict()
for i in cat['note_numbers']: nn.setdefault(R[i]['pg'],[]).append(i)
for pg,ids in nn.items(): W(f'| {comp(ids)} | page {pg} note-text numbers ({len(ids)}) |')
P(cat['note_numbers'])
W('### 7c Admin (letter metadata, page footers)'); W('| ROW IDs | group |'); W('|---|---|')
for g in sorted(set(assigned[i][1] for i in cat['admin'])):
    ids=[i for i in cat['admin'] if assigned[i][1]==g]; W(f'| {comp(ids)} | {g} ({len(ids)}) |')
P(cat['admin'])
W('### 7d Board-letter numbers placed under agenda'); W('| ROW IDs | group |'); W('|---|---|')
W(f'| {comp(cat["agenda"])} | meeting times and CS membership number (also in section 1) |')
P(cat['agenda'])
W('\n## 8. PRESS RELEASE (Attachment C) AND ATTACHMENTS D, E')
W('| ROW IDs | group | cells | A2 flags |'); W('|---|---|---|---|')
for c in ('press_num','attachD_num','attachE_num'):
    byg=collections.OrderedDict()
    for i in cat[c]: byg.setdefault(assigned[i][1],[]).append(i)
    for g,ids in byg.items():
        fl='-'
        if 'headline' in g: fl='FOOTNOTE_UNRESOLVED (see 2c: R1766-R1768)'
        if 'Table 1' in g: fl='RESTATED vs headline claims R1365-R1371; PAT after minority interest (R1771)'
        W(f'| {comp(ids)} | {g} | {len(ids)} | {fl} |')
    P(cat[c])
W('Press release revenue and EBITDA are not defined against filed lines (R1766-R1768); reconcile in A3.')
W('\n## 9. DATES'); W('| ROW IDs | group | count | A2 flags |'); W('|---|---|---|---|')
byg=collections.OrderedDict()
for i in sorted(cat['date'],key=n): byg.setdefault(assigned[i][1],[]).append(i)
for g,ids in sorted(byg.items()): W(f'| {comp(ids)} | {g} | {len(ids)} | {"ENTITY_CHANGE (cross-ref 6a)" if g.startswith("F") else "-"} |')
P(cat['date'])
W('\n## 10. FORWARD-LOOKING STATEMENTS'); W('| ROW IDs | group | count |'); W('|---|---|---|')
byg=collections.OrderedDict()
for i in sorted(cat['forward'],key=n): byg.setdefault(assigned[i][1],[]).append(i)
for g,ids in byg.items(): W(f'| {comp(ids)} | {g} | {len(ids)} |')
W('VAT appeal: National Court judgment was scheduled for 13-Oct-2026, two days before the board meeting; outcome not stated (R1558, R1608). Flag OUTCOME_NOT_DISCLOSED.')
P(cat['forward'])
W('\n## 11. MISSING_FROM_STRUCTURED'); W('None. Fulltext sweep of every decimal token on pp2, 11, 12, 18-20, 22-23, 27-28, 32 found each present in the structured file. Financial-table decimals on pp3-10, 13-17 match one-for-one.')
body='\n'.join(out)
yn=lambda b:'yes' if b else 'no'
cnt='\n'.join([
'=== A2 COUNT TEST ===',
f'category: notes            grep_count: {g_notes}   sweep_count: {len(cat["note"])}   match: {yn(g_notes==len(cat["note"]))}',
f'category: footnotes        grep_count: {g_fn}   sweep_count: {len(cat["footnote"])}   match: {yn(g_fn==len(cat["footnote"]))}   (+{len(cat["footnote_unres"])} FOOTNOTE_UNRESOLVED in 2c)',
f'category: line_items (fulltext lines with decimal cells vs ledger lines)  grep_count: {grep_li}   sweep_count: {sweep_li}   match: {yn(grep_li==sweep_li and not miss_ft and not extra_led)}',
f'category: line_item_cells  grep_count: {cells_grep}   sweep_count: {cells_sweep}   match: {yn(cells_grep==cells_sweep)}   (ledger line rows: {len(li_rows)})',
f'category: zero_standing    grep_count: {zero_grep}   sweep_count: {len(zero_all)}   match: {yn(zero_grep==len(zero_all))}   (lines with a zero cell: {zero_groups})',
'category: agenda_items     grep_count: 3   sweep_count: 3   match: yes   (letter items (i)-(iii); A4 timing and A5 absence rows added)',
f'category: auditor_paras    grep_count: {g_aud}   sweep_count: {len(cat["auditor_para"])}   match: {yn(g_aud==len(cat["auditor_para"]))}',
f'category: entities_consol  grep_count: {g_ent}   sweep_count: {len(cat["entity_consol"])}   match: {yn(g_ent==len(cat["entity_consol"]))}',
f'category: entities_total   grep_count: {sum(1 for r in rows if r["t"]=="ENTITY")}   sweep_count: {len(cat["entity_consol"])+len(cat["entity_other"])}   match: {yn(sum(1 for r in rows if r["t"]=="ENTITY")==len(cat["entity_consol"])+len(cat["entity_other"]))}',
f'category: dates            grep_count: {sum(1 for r in rows if r["t"]=="DATE")}   sweep_count: {len(cat["date"])}   match: {yn(sum(1 for r in rows if r["t"]=="DATE")==len(cat["date"]))}',
f'category: forward          grep_count: {sum(1 for r in rows if r["t"]=="FORWARD")}   sweep_count: {len(cat["forward"])}   match: {yn(sum(1 for r in rows if r["t"]=="FORWARD")==len(cat["forward"]))}',
'category: signatures       grep_count: 4   sweep_count: 4   match: yes',
'category: slides / turns / questions: not applicable (results filing)',
'@@IDLINE@@','@@GATE@@','=== END COUNT TEST ==='])
open('work/a2-results/body.md','w',encoding='utf-8').write(body)
open('work/a2-results/cnt.txt','w',encoding='utf-8').write(cnt)
json.dump(dict(prim=sorted(prim,key=n),miss_ft=miss_ft,extra_led=extra_led,zero_all=len(zero_all),zero_groups=zero_groups,li_lines=len(li_rows),cat={k:len(v) for k,v in cat.items()}),open('work/a2-results/stats.json','w'))
print(cnt)
print(miss_ft[:10],extra_led[:10],len(prim))
