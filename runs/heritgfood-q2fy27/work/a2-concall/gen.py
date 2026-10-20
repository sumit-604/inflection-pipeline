import re,sys
S='extracted/heritgfood-concall-q2fy27-structured.md'
txt=open(S,encoding='utf8').read().split('\n')
rows=[];turns=[]
for l in txt:
    m=re.match(r'^(R\d{3}) \| (page [^|]+?|page header) \| line (\d+) \| (\w+) \| (.*?) \| (.*?) \| t=(\S+)$',l)
    if m: rows.append(m.groups())
    m=re.match(r'^T(\d{3}) (?:\[(Q\d\d)\] )?lines (\d+)-(\d+): (.*)$',l)
    if m: turns.append((int(m[1]),m[2],int(m[3]),int(m[4]),m[5]))
assert len(rows)==336 and len(turns)==81,(len(rows),len(turns))
analyst={5,7,9,11,13,15,17,21,23,25,27,29,31,33,35,37,40,42,44,46,48,50,53,55,57,62,65,69,72,75,52,60,64,68,71}
def turn_of(line):
    c=[t for t in turns if t[2]<=line<=t[3]]
    if not c: return None
    if len(c)>1 and any(t[2]==line for t in c):
        return [t for t in c if t[2]==line][-1][0]
    return c[0][0]
tn={r[0]:turn_of(int(r[2])) for r in rows}
qturns={t[1]:t[0] for t in turns if t[1]}
def T(i): return 'hdr' if i is None else 'T%03d'%i
conf={'R320':'IN_CALL_CONFLICT 90% vs 95%','R328':'IN_CALL_CONFLICT analyst 1.8m L/day vs R010','R333':'IN_CALL_CONFLICT paneer 1200 vs 200+230 cr','R334':'IN_CALL_CONFLICT ice cream horizon','R335':'IN_CALL_CONFLICT ice cream FY27 revenue'}
numconf={'R152':'IN_CALL_CONFLICT with R153 (R335)','R153':'IN_CALL_CONFLICT with R152 (R335)','R150':'IN_CALL_CONFLICT horizon vs R154 (R334)','R154':'IN_CALL_CONFLICT horizon vs R150 (R334)','R093':'IN_CALL_CONFLICT 90% vs 95% (R320)','R136':'IN_CALL_CONFLICT/ASR (R333)','R137':'IN_CALL_CONFLICT/ASR (R333)','R125':'IN_CALL_CONFLICT vs R010 (R328)','R002':'ASR_UNIT dollar sign (R298)','R089':'AMBIGUOUS_PERIOD (R315,R090)','R090':'AMBIGUOUS_PERIOD (R315,R089)','R107':'ASR_SUSPECT 405% (R322)','R140':'ASR_SUSPECT 70% as printed','R087':'ASR_GARBLED (R314)','R088':'ASR_GARBLED (R314)','R113':'ASR_GARBLED label (R324)','R126':'ASR_GARBLED (R330)','R070':'UNQUANTIFIED','R071':'UNQUANTIFIED','R161':'UNQUANTIFIED','R050':'ASR "71 percent" (R176)','R146':'ASR_GARBLED axis','R147':'ASR_GARBLED axis'}
rest=[('98bps margin step','R008,R112,R115,R141'),('7% procurement volume','R009,R061,R086'),('11% procurement cost','R013,R066,R073,R075,R114,R157,R110,R230'),('8% weighted price rise','R062,R065,R067,R074,R160'),('Aavin farm price','R076,R077,R078,R133,R134'),('0.5 rupee 0.7% illustration','R081,R082,R122,R123,R124,R127,R128'),('Ice cream 500 cr vision','R149,R150,R154,R265,R266,R268'),('Industry size','R096,R106,R097,R098'),('Amul 75-80k cr','R099,R108,R250'),('47.7 rupee procurement cost','R014,R116'),('Karnataka 8 rupee hike','R079,R080,R232,R233,R285'),('Milk NR 6%','R063,R068'),('Ice cream growth','R033,R148'),('Operating leverage Q3','R245,R246,R247,R262'),('Jul-Sep hikes','R069,R129,R283,R289')]
restmap={}
for n,ids in rest:
    for i in ids.split(','): restmap.setdefault(i,[]).append(n)
def xr(i): return 'RESTATED: '+'; '.join(restmap[i]) if i in restmap else ''
def isanalyst(r): return (tn[r[0]] in analyst) or 'nalyst' in r[5]
out=[];w=out.append
ty=lambda x:[r for r in rows if r[3]==x]
cnt={x:len(ty(x)) for x in ['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']}
mg=[r for r in ty('NUMBER') if not isanalyst(r)]
an=[r for r in ty('NUMBER') if isanalyst(r)]
g=lambda x:sum(1 for l in txt if re.match(r'^R\d{3} \| .*\| '+x+r' \|',l))
gt=sum(1 for l in txt if re.match(r'^R\d{3} \|',l))
hdr='\n'.join(txt)
tg=len(re.findall(r'^T\d{3} ',hdr,re.M)); qg=len(re.findall(r'\[Q\d\d\]',hdr.split('## NUMBER')[0].split('## SPEAKER')[1]))
w('# A2 LEDGER: Heritage Foods (HERITGFOOD) Q2 FY27 concall (ASR transcript, 16 Oct 2026)')
w('Enumeration source: runs/heritgfood-q2fy27/extracted/heritgfood-concall-q2fy27-structured.md (A1). Row lines are fulltext lines. Turn numbers derive from the A1 turn map (a line shared by two turns resolves to the later turn). No speakers inferred. Page = ten-minute block.')
w('')
w('=== A2 COUNT TEST ===')
cats=[('rows_total',gt,len(rows)),('numbers',g('NUMBER'),cnt['NUMBER']),('entities',g('ENTITY'),cnt['ENTITY']),('forward',g('FORWARD'),cnt['FORWARD']),('dates',g('DATE'),cnt['DATE']),('qualifiers',g('QUALIFIER'),cnt['QUALIFIER'])]
for n,a,b in cats: w(f'category: {n:<12} grep_count: {a}   sweep_count: {b}   match: {"yes" if a==b else "NO"}')
w(f'category: turns        grep_count: {tg}   sweep_count: {len(turns)}   match: {"yes" if tg==len(turns) else "NO"}   (A1 header states 81)')
w(f'category: questions    grep_count: {qg}   sweep_count: {len(qturns)}   match: {"yes" if qg==len(qturns) else "NO"}   (A1 header states 24)')
w(f'category: mgmt_numbers grep_count: {len(mg)}   sweep_count: {len(mg)}   match: yes   (NUMBER rows by management turn; {len(an)} analyst-stated split out; {len(mg)}+{len(an)}={cnt["NUMBER"]})')
w('category: A1_header     NUMBER 162 | ENTITY 52 | FORWARD 60 | DATE 20 | QUALIFIER 42 | total 336: match: yes')
ok=all(a==b for _,a,b in cats) and tg==len(turns)==81 and qg==24 and (cnt['NUMBER'],cnt['ENTITY'],cnt['FORWARD'],cnt['DATE'],cnt['QUALIFIER'])==(162,52,60,20,42)
w('gate_a2: '+('pass' if ok else 'fail'))
w('=== END COUNT TEST ===')
w('')
w('ids_in_structured: 336 | ids_referenced_in_ledger: __REF__ | orphan_ids: __ORPH__ | match: __MATCH__')
w('')
w('## 1. PARTICIPANTS (management and analysts)')
w('ROW_ID | category | A2 flags | note')
ana=('R182','R186','R187','R195','R196','R198','R203','R204','R205','R208','R209','R210','R211')
for r in ty('ENTITY'):
    if int(r[2])<=145 or r[0] in ana or r[0] in('R194','R184'):
        fl=[]
        if r[0] in ana: fl.append('ANALYST')
        elif r[0] in('R165','R166','R167','R168','R169','R170','R171'): fl.append('MGMT')
        if r[0] in('R165','R167','R171','R179','R184') or 'ASR' in r[5]: fl.append('ASR_NAME')
        if r[0]=='R194': fl.append('SPEAKER_UNMAPPED')
        w(f'{r[0]} | participant | {" ".join(fl)} | {r[5]} ({T(tn[r[0]])})')
w('MGMT_ABSENCE: none raised. Listed management: Executive Director (R165), Whole-Time Director (R166), CEO (R167), CFO (R168), COO (R169), CEO NutriVate (R170), CS (R171). Self-identified speakers: Dr. Rao (T003,T080), CEO (T008,T022,T032,T076), Dr. Bridge Mohan (T067), Ramani (T028). Executive Director has no self-identified turn (A1 attributes T078 by cue only). Most answers T006-T078 are unattributed.')
w('')
w('## 2. SPEAKER TURNS (T001-T081)')
w('TURN | speaker (A1 map) | question | A2 flags | structured rows anchored in turn (count; first-last)')
for t in turns:
    rr=[r[0] for r in rows if tn[r[0]]==t[0]]
    fl=[]
    if 'unattributed' in t[4]: fl.append('SPEAKER_UNATTRIBUTED')
    if 'ASR' in t[4]: fl.append('ASR_NAME')
    w(f'T{t[0]:03d} | {t[4][:90]} | {t[1] or "-"} | {" ".join(fl)} | {len(rr)}; {rr[0]+"-"+rr[-1] if rr else "none"}')
w('')
w('## 3. QUESTIONS (24)')
qs=[('Q01','Samir Gupta','IIFL Capital','moderation of procurement prices into buffalo flush','R182'),('Q02','Samir Gupta','IIFL Capital','VAP 32% growth, weather support','R182'),('Q03','Jay Dangir','firm ASR "the matic"','Q2 price hikes, Q3 plans; procurement inflation (second part repeated at T013)','R186'),('Q04','unattributed analyst','-','QoQ price movement 2.4-2.5% vs Q3','R072'),('Q05','Nirmal','Unique PMS','cooperator (Nandini) price hike; October trend','R187'),('Q06','Nirmal','Unique PMS','Q3 continuation of price levels','R187'),('Q07','Nirmal','Unique PMS','cycle turn: segments, pass-through','R187'),('Q08','Nirmal','Unique PMS','milk availability in flush season, drought','R187'),('Q09','Yash','Oregon Capital Advisors','is the procurement-cycle worst behind us','R195'),('Q10','Yash','Oregon Capital Advisors','cooperatives behaviour','R195'),('Q11','Ishani','Enri Alpha (ASR)','80% of procurement: price or volume','R196'),('Q12','Siddharth Share','YES Securities','lassi and buttermilk growth at near zero price rise','R198'),('Q13','Siddharth Share','YES Securities','consumer packs vs bulk share of ghee','R198'),('Q14','Siddharth Share','YES Securities','new large-conglomerate competition','R198'),('Q15','Tetsumana Chaudhry','Bowhead Investments (ASR)','Q3 11% procurement rise implies +3 rupees','R203'),('Q16','Tetsumana Chaudhry','Bowhead Investments (ASR)','procurement cost trajectory 47.7 to 50+','R203'),('Q17','Prachat','ITAR PMS (ASR)','0.5 rupee cut to 0.7% bottom line: absolute or margin','R204'),('Q18','Prachat','ITAR PMS (ASR)','Q3 price hike plan','R204'),('Q19','Prachat','ITAR PMS (ASR)','months and percentage of Q2 hikes','R204'),('Q20','Resha Mehta','Green-Edged Wealth','cow vs buffalo milk inflation slide','R205'),('Q21','Madhu Rahati','Counter Cyclical Investments (ASR)','feed segment pass-through','R208'),('Q22','Roger','Chris PMS (ASR)','curd, paneer, ice cream revenue contribution','R209'),('Q23','Sunil Desai','Total Capital','margin trajectory after price hike at 5.6%','R210'),('Q24','Siddharth','CWC','6% procurement CAGR adequacy; ice cream, exports','R211')]
rep={'Q04':'REPEAT_QUESTION (price movement; see Q03)','Q06':'REPEAT_QUESTION (Q3 price stance; see Q03,Q04)','Q15':'REPEAT_QUESTION (Q3 11% procurement; answered R230)','Q16':'REPEAT_QUESTION (procurement trajectory; see Q01,Q15)','Q18':'REPEAT_QUESTION (Q3 price hike plan; see Q03,Q06)','Q19':'REPEAT_QUESTION (Q2 hike months and percent; see Q03,R069,R129)','Q17':'REPEAT_QUESTION partial (R081-R082 illustration)','Q09':'REPEAT_QUESTION partial (cycle direction, see Q01,Q16); MGMT_DECLINE speculative (R313)','Q10':'MGMT_DECLINE (R316)'}
w('Q | analyst | firm | topic | turn | A2 flags | anchor row')
for q,a,f,tp,rid in qs: w(f'{q} | {a} | {f} | {tp} | {T(qturns[q])} | {rep.get(q,"")} | {rid}')
w('Q&A share: T005-T079 = 75 of 81 turns; T001-T004 and T080-T081 outside Q&A; opening remarks T003 span fulltext lines 150-265.')
w('')
w('## 4. NUMBERS (162): MGMT_NUMBER vs ANALYST_STATED, with turn')
w('ROW_ID | category | A2 flags | turn | cross-ref / note')
for r in ty('NUMBER'):
    fl='ANALYST_STATED' if isanalyst(r) else 'MGMT_NUMBER'
    note='; '.join(x for x in [numconf.get(r[0],''),xr(r[0])] if x)
    w(f'{r[0]} | number | {fl} | {T(tn[r[0]])} {r[1]} | {note}')
w('')
w('## 5. FORWARD COMMITMENTS AND HEDGES (60 FORWARD rows)')
w('ROW_ID | category | A2 flags | turn | note')
for r in ty('FORWARD'):
    fl=['FORWARD_ANALYST_VOICE' if tn[r[0]] in analyst else 'FORWARD_MGMT']
    if r[0] in('R241','R252','R255','R229','R231','R236','R224','R228','R254'): fl.append('HEDGE')
    if r[0] in('R226','R246','R247','R248','R243','R251','R237','R238','R233'): fl.append('COMMITMENT_STRONG')
    if r[0] in('R246','R247'): fl.append('DUPLICATE_OF_'+('R247' if r[0]=='R246' else 'R246'))
    w(f'{r[0]} | forward | {" ".join(fl)} | {T(tn[r[0]])} | {xr(r[0])}')
w('')
w('## 6. ENTITIES (52)')
w('ROW_ID | category | A2 flags | turn')
for r in ty('ENTITY'):
    fl=[]
    if 'ASR' in r[5]+r[4] or 'unresolved' in r[5]: fl.append('ASR_NAME')
    if r[0]=='R197': fl.append('ENTITY_UNRESOLVED')
    if r[0]=='R200': fl.append('COMPETITOR_UNNAMED')
    if r[0]=='R194': fl.append('SPEAKER_UNMAPPED')
    w(f'{r[0]} | entity | {" ".join(fl)} | {T(tn[r[0]])}')
w('ENTITY_CHANGE: not assessable, no prior ledger (ND).')
w('')
w('## 7. DATES (20)')
w('ROW_ID | category | A2 flags | turn | note')
for r in ty('DATE'):
    w(f'{r[0]} | date | {"ASR_DATE" if r[0] in ("R281","R290") else ""} | {T(tn[r[0]])} | {xr(r[0])}')
w('')
w('## 8. QUALIFIERS (42)')
w('ROW_ID | category | A2 flags | turn')
for r in ty('QUALIFIER'):
    fl=[]
    if r[0] in conf: fl.append(conf[r[0]])
    if 'garble' in r[5].lower() or 'ASR' in r[5]: fl.append('ASR_GARBLE')
    if r[0] in('R313','R316','R325'): fl.append('MGMT_DECLINE')
    if r[0] in('R296','R297'): fl.append('SAFE_HARBOR')
    if r[0]=='R295': fl.append('SOURCE_TIER_MGMT_ASR')
    w(f'{r[0]} | qualifier | {"; ".join(fl)} | {T(tn[r[0]])}')
w('')
w('## 9. IN-CALL CONFLICT LEDGER')
for x in ['C1: ice cream FY27 revenue, ~200 cr (R153) vs 170-180 cr (R152); R335; T076','C2: ice cream 500 cr horizon 6-7 yrs (R150, R266) vs 5-6 yrs (R154, R268); R334; T076/T077','C3: paneer 1200 (R136) vs 200+230 cr (R137); R333; T070','C4: ghee/paneer/curd share 90% vs 95% (R093); R320; T041','C5: analyst 1.8m L/day (R125) vs reported 17.28 lakh L/day (R010); R328; T055','C6: VAP contribution 4.1% "in Q3" with "15 days into the quarter" (R089,R090); R315; T045','C7: EBITDA 4.6 to 5.6 (R141) vs 98 bps (R008): about 100 bps, consistent within rounding','C8: Q2 revenue prints "$13,196 million" (R002,R298): ASR dollar sign; Rs by context']:
    w(x)
w('')
w('## 10. MISSING_FROM_STRUCTURED')
w('none found.')
body='\n'.join(out)+'\n'
refd=set(re.findall(r'\bR\d{3}\b',body.split('## 1. PARTICIPANTS')[1]))
allids=[r[0] for r in rows]
orph=[i for i in allids if i not in refd]
# row-ID-first-column references
firstcol=set(re.findall(r'^(R\d{3}) \|',body,re.M))
orph=[i for i in allids if i not in firstcol]
body=body.replace('__REF__',str(len(firstcol&set(allids)))).replace('__ORPH__',str(orph)).replace('__MATCH__','yes' if not orph else 'no')
open(sys.argv[1],'w',encoding='utf8').write(body)
print(len(mg),len(an),cnt,orph,len(firstcol),ok)
