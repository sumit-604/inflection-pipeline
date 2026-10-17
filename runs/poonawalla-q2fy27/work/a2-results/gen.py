import re,collections,pickle
B='C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/q2fy27/runs/poonawalla-q2fy27/'
S=open(B+'extracted/poonawalla-results-q2fy27-structured.md',encoding='utf8').read().split('\n')
rows=[]
for l in S:
    m=re.match(r'R(\d+) \| page (\d+) \| line (\d+) \| (\w+) \| (.*)',l)
    if m:
        rest=m.group(5)
        fl=set(re.findall(r'(ZERO_STANDING|OCR_SUSPECT|OCR_SPACE|COLUMN_UNRESOLVED|NOT_APPLICABLE|MISSING_VALUE|TEXT_TRUNCATED|OCR_QUALITY)',rest.split('FLAG:')[-1] if 'FLAG:' in rest else ''))
        rows.append(dict(id=int(m.group(1)),p=int(m.group(2)),ln=int(m.group(3)),t=m.group(4),fl=fl))
LI_PAGES={7,8,9,13,14,15}
SEG=[
(1,35,'AG0','letter','Cover letter header, addressees, subject, regulation reference'),
(36,42,'AG1','agenda','Board approval item 1: unaudited standalone and consolidated results Q2/H1 FY27'),
(43,46,'ENC1','agenda','Enclosure 1: results (newspaper publication follows)'),
(47,50,'ENC2','agenda','Enclosure 2: Limited Review Reports (joint auditors MSKA, B K Khare)'),
(51,52,'ENC3','agenda','Enclosure 3: Reg 52(4) line-item statement'),
(53,55,'ENC4','agenda','Enclosure 4: QIP deviation statement Reg 32(1)'),
(56,59,'ENC5','agenda','Enclosure 5: Reg 52(7)/52(7A) statement'),
(60,70,'ENC6','agenda','Enclosure 6: Reg 54 security cover disclosure'),
(71,77,'AG4','agenda','Investor Presentation sent separately (Reg 30); NRC recommendation lead-in'),
(78,89,'AG2','agenda','Board approval: re-appointment of independent director Kemisha Soni, 2nd term, special resolution'),
(90,93,'AG3','agenda','Board approval: Postal Ballot Notice for the re-appointment'),
(94,95,'AGT','agenda','Board meeting start 1:45 PM and end 3:32 PM (107 minutes)'),
(96,116,'SIG1','signature','Cover letter signatory (Company Secretary), digital signature 2026.10.09 16:23:14'),
(117,126,'ANXA1','annexa','Annexure A item 1: reason for change'),
(127,130,'ANXA2','annexa','Annexure A item 2: date and term of re-appointment'),
(131,158,'ANXA3','annexa','Annexure A item 3: brief profile'),
(159,167,'ANXA4','annexa','Annexure A item 4: relationship between directors'),
(168,182,'ANXA5','annexa','Annexure A item 5: debarment confirmation, BSE/NSE circular references'),
(183,196,'AUDC0','auditor','Consolidated LRR header, addressee and title'),
(197,202,'AUDC1','auditor','Consolidated LRR para 1: scope of review'),
(203,208,'AUDC2','auditor','Consolidated LRR para 2: management responsibility, Ind AS 34'),
(209,218,'AUDC3','auditor','Consolidated LRR para 3: SRE 2410 basis, no audit opinion'),
(219,227,'AUDC4','auditor','Consolidated LRR para 4: entity list (JASPL JV, held for sale)'),
(228,238,'AUDC5','auditor','Consolidated LRR para 5: conclusion (nothing came to attention)'),
(239,248,'AUDC6','auditor','Consolidated LRR para 6: JV figures unreviewed, management furnished (other matter)'),
(249,258,'AUDC7','auditor','Consolidated LRR para 7: prior period reviewed/audited by Kirtane and Pandit LLP'),
(259,277,'AUDC8','signature','Consolidated LRR signature block: firm regs, UDINs, place, date'),
(472,472,'NC0','note','Consolidated notes header'),
(473,479,'NC1','note','Consolidated note 1: basis of preparation'),
(480,482,'NC2','note','Consolidated note 2: Audit Committee review and Board approval'),
(483,486,'NC3','note','Consolidated note 3: limited review, unmodified conclusion'),
(487,489,'NC4','note','Consolidated note 4: filing with exchanges'),
(490,492,'NC5','note','Consolidated note 5: single segment'),
(493,496,'NC6','note','Consolidated note 6: ESOP allotment'),
(497,502,'NC7','note','Consolidated note 7: QIP completed 13 April 2026'),
(503,508,'NC8','note','Consolidated note 8: CP and NCD issuance, listing'),
(509,515,'NC9','note','Consolidated note 9: JASPL sale, assets held for sale (Ind AS 105)'),
(516,519,'NC10','note','Consolidated note 10 (marker OCR "I OJ"): regrouping of prior figures'),
(520,534,'SIG2','signature','Consolidated results signature block, DIN, CIN, addresses'),
(535,548,'AUDS0','auditor','Standalone LRR header, addressee and title'),
(549,555,'AUDS1','auditor','Standalone LRR para 1: scope'),
(556,562,'AUDS2','auditor','Standalone LRR para 2: management responsibility'),
(563,571,'AUDS3','auditor','Standalone LRR para 3: SRE 2410 basis'),
(572,579,'AUDS4','auditor','Standalone LRR para 4: conclusion (nothing came to attention)'),
(580,597,'AUDS5','auditor','Standalone LRR para 5: PFL Employee Welfare Trust unreviewed, management furnished (other matter)'),
(598,608,'AUDS6','auditor','Standalone LRR para 6: prior period reviewed/audited by Kirtane and Pandit LLP'),
(609,631,'AUDS7','signature','Standalone LRR signature block: firm regs, UDINs, place, date'),
(830,838,'NS1','note','Standalone note 1 (marker OCR "I]"): basis of preparation'),
(839,841,'NS2','note','Standalone note 2: Audit Committee review and Board approval'),
(842,843,'NS3','note','Standalone note 3: limited review'),
(844,845,'NS4','note','Standalone note 4: filing with exchanges'),
(846,846,'NS5','note','Standalone note 5: single segment'),
(847,849,'NS6','note','Standalone note 6: ESOP allotment'),
(850,853,'NS7','note','Standalone note 7: QIP'),
(854,857,'NS8','note','Standalone note 8: CP and NCD issuance'),
(858,861,'NS9','note','Standalone note 9: JASPL sale, held for sale'),
(862,867,'NS10','note','Standalone note 10 (marker OCR "I OJ"): Reg 54 security cover maintained'),
(868,869,'NS11','note','Standalone note 11 (marker OCR "I !]"): RBI transfer-of-loans disclosures, lead-in'),
(870,881,'NS11a','notesub','Standalone note 11(a): loans not in default transferred through assignment'),
(882,897,'NS11b','notesub','Standalone note 11(b): loans not in default acquired through assignment (NIL)'),
(898,916,'NS11c','notesub','Standalone note 11(c): stressed loans transferred to ARCs'),
(917,940,'NS11d','notesub','Standalone note 11(d): ratings of security receipts'),
(941,965,'NS12','note','Standalone note 12: COVID resolution framework table'),
(966,966,'NS13','note','Standalone note 13: regrouping of prior figures'),
(967,983,'SIG3','signature','Standalone results signature block, place, date, addresses'),
(1357,1375,'AUDK0','auditor','Security cover certificate header, addressee, title'),
(1376,1378,'AUDK1','auditor','Certificate para 1: engagement letter'),
(1379,1391,'AUDK2','auditor','Certificate para 2: statement and basis'),
(1392,1399,'AUDK3','auditor','Certificate para 3: management responsibility'),
(1400,1404,'AUDK4','auditor','Certificate para 4: compliance responsibility'),
(1405,1424,'AUDK5','auditor','Certificate para 5: auditor responsibility, limited assurance'),
(1425,1437,'AUDK6','auditor','Certificate para 6: standalone results reviewed, unmodified conclusion 09 Oct 2026'),
(1438,1442,'AUDK7','auditor','Certificate para 7: Guidance Note basis'),
(1443,1446,'AUDK8','auditor','Certificate para 8: SQC 1 compliance'),
(1447,1485,'AUDK9','auditor','Certificate para 9: limited assurance procedures (a) to (f)'),
(1486,1498,'AUDK10','auditor','Certificate para 10: conclusion'),
(1499,1508,'AUDK11','auditor','Certificate para 11: restriction on distribution'),
(1509,1517,'AUDK12','auditor','Certificate para 12: addressee and use restriction'),
(1518,1531,'AUDK13','signature','Certificate signature block: firm reg, UDIN, place, date'),
]
def key_of(r):
    p,ln,t=r['p'],r['ln'],r['t']
    for a,b,key,cat,d in SEG:
        if a<=ln<=b: return (key,cat,d)
    if p in LI_PAGES:
        if t=='NUMBER': return ('LI%d_%d'%(p,ln),'line_item','')
        return ('TQ%d'%p,'tblq','Non-numeric rows on statement page %d (entity/date/qualifier cross-references)'%p)
    if p==18:
        if t=='NUMBER': return ('R52_%d'%ln,'line_item','')
        return ('R52Q','tblq','Reg 52(4) page non-numeric rows (entity/date/qualifier)')
    if p==19: return ('FN19_%d'%ln,'footnote','Reg 52(4) page footnote / unnumbered paragraph / signature line')
    return ('ANX%d_%d'%(p,ln),'annex','')
groups=collections.OrderedDict()
for r in rows:
    k=key_of(r)
    g=groups.setdefault(k[0],dict(cat=k[1],desc=k[2],ids=[],fl=set(),pg=set(),ln=set(),types=collections.Counter()))
    g['ids'].append(r['id']);g['fl']|=r['fl'];g['pg'].add(r['p']);g['ln'].add(r['ln']);g['types'][r['t']]+=1
pickle.dump((rows,groups),open(B+'work/a2-results/groups.pkl','wb'))
print(collections.Counter(g['cat'] for g in groups.values()))
print(len(rows),sum(len(g['ids']) for g in groups.values()))
# unmapped check: statement-page rows landing in SEG
for k,g in groups.items():
    if g['cat'] in ('line_item',) : pass
print([k for k,g in groups.items() if g['cat']=='annex' and min(g['pg'])<=17])
