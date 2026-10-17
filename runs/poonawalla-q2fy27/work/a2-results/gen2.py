import re,collections,pickle
exec(open('C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/q2fy27/runs/poonawalla-q2fy27/work/a2-results/gen.py',encoding='utf8').read().split("pickle.dump")[0])
F=open(B+'extracted/poonawalla-results-q2fy27-fulltext.md',encoding='utf8').read().split('\n')
byline=collections.defaultdict(list)
for r in rows: byline[r['ln']].append(r)
def ids_on(lo,hi):
    return sorted(r['id'] for ln in range(lo,hi+1) for r in byline.get(ln,[]))
def R(lst): return rng(lst) if lst else 'none'
def fl(g): return ' '.join(sorted(g['fl'])) if g['fl'] else '-'
def rng(lst):
    lst=sorted(lst);out=[];s=p=None
    for x in lst:
        if s is None: s=p=x
        elif x==p+1: p=x
        else: out.append((s,p));s=p=x
    if s is not None: out.append((s,p))
    return ','.join('R%03d'%a if a==b else 'R%03d-R%03d'%(a,b) for a,b in out)
STMT={7:'CONS P&L',8:'CONS BS',9:'CONS CF',13:'STAND P&L',14:'STAND BS',15:'STAND CF',18:'REG52(4)'}
out=[]
W=out.append
referenced=set()
def ref(ids): referenced.update(ids)
# ---- tables
# Notes
notes=[]
for a,b,key,cat,d in SEG:
    if cat=='note' and key not in ('NC0',):
        notes.append((key,a,b,d))
W('## T1 NOTES (numbered). Format: LEDGER_ID | structured ROW IDs (line range) | A2 flags | note')
W('| LEDGER_ID | ROW IDs | fulltext lines | A2 flags / materiality note |')
W('|---|---|---|---|')
nn=0
ref(groups['NC0']['ids']); W('| NC0 (header, not counted) | %s | 472 | consolidated notes header |'%R(groups['NC0']['ids']))
for key,a,b,d in notes:
    g=groups.get(key); ids=g['ids'] if g else []
    ref(ids); nn+=1
    extra=''
    fls=[]
    if key in ('NC9','NS9'): fls.append('FOOTNOTE_UNRESOLVED(JASPL sale pending since 2021)')
    if key in ('NC7','NS7'): fls.append('RESTATED(QIP also on Reg 32(1) pp20-22)')
    if key in ('NS11',): fls.append('subnotes 11a-11d below')
    if key=='NS11a' : pass
    if g and g['fl']: fls.append('A1:'+fl(g))
    W('| %s | %s | %d-%d | %s; %s |'%(key,R(ids),a,b,' '.join(fls) if fls else '-',d))
    if key=='NS11':
        for k2 in ('NS11a','NS11b','NS11c','NS11d'):
            g2=groups.get(k2); i2=g2['ids'] if g2 else []; ref(i2)
            s2=[x for x in SEG if x[2]==k2][0]
            f2=[]
            if g2 and g2['fl']: f2.append('A1:'+fl(g2))
            if k2=='NS11b': f2.append('ZERO_STANDING')
            W('| %s (sub of NS11, not counted) | %s | %d-%d | %s; %s |'%(k2,R(i2),s2[0],s2[1],' '.join(f2) if f2 else '-',s2[4]))
# Annexure II notes
an2=[]
for ln in (1750,1751,1752,1753,1754):
    ids=ids_on(ln,ln)
    if ln==1750: continue
    an2.append((ln,ids))
for i,(ln,ids) in enumerate(an2,1):
    ref(ids); nn+=1
    W('| ANXII_N%d | %s | %d | Annexure II note %d (p30); column mapping on p30 unresolved |'%(i,R(ids),ln,i))
W('')
notes_total=nn
# unnumbered footnotes
W('## T1b UNNUMBERED NOTES AND FOOTNOTES')
W('| LEDGER_ID | ROW IDs | fulltext line | flags / note |')
W('|---|---|---|---|')
fnlines=[(226,'JV (*) footnote: held for sale, equity method discontinued 13 Dec 2021 (auditor para 4)'),(469,'"Note:" under consolidated cash flow (p9)'),(828,'"Note:" indirect method statement under standalone cash flow (p15)'),(912,'Bullet under note 11(c): further 10,558 accounts transferred'),(963,'Footnote * IBC definition under note 12 table'),(964,'Footnote # interest accrued under note 12 table'),(1033,'Footnote ** DRR not required for privately placed debentures (p19)'),(1038,'Unmarked paragraph: CP and NCD issued/listed in H1 (p19)'),(1144,'Footnote * on QIP table: net proceeds and issue expenses (p21)'),(1568,'Footnote * on Annexure I outstanding column (p29)')]
fn_n=0
for ln,d in fnlines:
    ids=ids_on(ln,ln); ref(ids); fn_n+=1
    W('| FN%02d | %s | %d | %s |'%(fn_n,R(ids),ln,d))
W('')
# Line items
W('## T2 LINE ITEMS (financial statements pp7-9, 13-15 and Reg 52(4) p18). One row per source line; ROW IDs span the period columns.')
W('| LEDGER_ID | statement | page | line | ROW IDs | A2 flags / note |')
W('|---|---|---|---|---|---|')
li_by={7:0,8:0,9:0,13:0,14:0,15:0,18:0}
zs_ids=[]
for k,g in groups.items():
    if g['cat']!='line_item': continue
    p=min(g['pg']); ln=min(g['ln']); ref(g['ids']); li_by[p]+=1
    f=[]
    if 'ZERO_STANDING' in g['fl']:
        f.append('ZERO_STANDING'); zs_ids+= [r['id'] for r in rows if r['id'] in g['ids'] and 'ZERO_STANDING' in r['fl']]
    for x in ('OCR_SUSPECT','OCR_SPACE','COLUMN_UNRESOLVED','NOT_APPLICABLE'):
        if x in g['fl']: f.append('A1:'+x)
    W('| %s | %s | %d | %d | %s | %s |'%(k,STMT[p],p,ln,R(g['ids']),' '.join(f) if f else '-'))
W('')
W('## T2b STATEMENT-PAGE NON-NUMERIC ROWS (entity/date/qualifier cross-references on table pages)')
W('| LEDGER_ID | ROW IDs | note |')
W('|---|---|---|')
for k,g in groups.items():
    if g['cat']=='tblq':
        ref(g['ids']); W('| %s | %s | %s |'%(k,R(g['ids']),g['desc']))
W('')
# zero standing
W('## T3 ZERO_STANDING ROWS (A1 flagged, A2 confirmed by independent dash/nil sweep of fulltext)')
W('| ROW ID | page | line | A2 flag |')
W('|---|---|---|---|')
for r in rows:
    if 'ZERO_STANDING' in r['fl']:
        W('| R%03d | %d | %d | ZERO_STANDING%s |'%(r['id'],r['p'],r['ln'],' COLUMN_UNRESOLVED' if 'COLUMN_UNRESOLVED' in r['fl'] else ''))
zs_n=sum(1 for r in rows if 'ZERO_STANDING' in r['fl'])
W('')
W('Sweep-only candidates, NOT counted (dash glyphs in OCR-garbled form/column areas, A1 did not emit a value row): fulltext lines 1111 (p20 form), 1656, 1662, 1664, 1686 (p30 Annexure II). Flag ZERO_STANDING_CANDIDATE, column mapping unresolved; A3 to confirm against the page image via A1 if material.')
W('')
# agenda
W('## T4 AGENDA ITEMS / BOARD OUTCOME LETTER')
W('| LEDGER_ID | ROW IDs | fulltext lines | A2 flags / note |')
W('|---|---|---|---|')
ag=[x for x in SEG if x[3]=='agenda']
for a,b,key,cat,d in ag:
    ids=groups[key]['ids'] if key in groups else []; ref(ids)
    f='-'
    if key=='AGT': f='MEETING_DURATION 107 min (1:45 PM to 3:32 PM); signature 16:23:14 is after close, no flag'
    if key=='AG2': f='FORWARD (R1096,R1097,R1098); director re-appointment, term 30 Jan 2027 to 29 Jan 2030'
    if key=='AG3': f='FORWARD (postal ballot pending)'
    if key=='ENC2': f='AUDITOR_CHANGE context: Kirtane and Pandit LLP now "previous joint auditor" (see T5 AUDC7/AUDS6)'
    W('| %s | %s | %d-%d | %s; %s |'%(key,R(ids),a,b,f,d))
W('')
W('Agenda coverage note: the letter carries NO items for dividend, AR approval, AGM notice, record date, auditor appointment, ESOP grants or capital-raising enabling resolutions. Absence recorded, not inferred.')
W('')
W('### T4b ANNEXURE A (director disclosure) items')
W('| LEDGER_ID | ROW IDs | fulltext lines | note |')
W('|---|---|---|---|')
for a,b,key,cat,d in [x for x in SEG if x[3]=='annexa']:
    ids=groups[key]['ids'] if key in groups else []; ref(ids)
    W('| %s | %s | %d-%d | %s |'%(key,R(ids),a,b,d))
W('')
W('### T4c LETTER HEADER AND SIGNATURES')
W('| LEDGER_ID | ROW IDs | fulltext lines | note |')
W('|---|---|---|---|')
for a,b,key,cat,d in [x for x in SEG if x[3] in ('letter','signature') and not x[2].startswith('AUD')]+[x for x in SEG if x[3]=='signature' and x[2].startswith('AUD')]:
    ids=groups[key]['ids'] if key in groups else []; ref(ids)
    W('| %s | %s | %d-%d | %s |'%(key,R(ids),a,b,d))
W('')
# auditor
W('## T5 AUDITOR REPORT PARAGRAPHS')
W('Opinion type in all three documents: unmodified conclusion on limited review (consolidated and standalone) and limited assurance conclusion (certificate). No Emphasis of Matter. No Going Concern language. Other-matter style paragraphs: AUDC6, AUDS5. Prior-auditor paragraphs: AUDC7, AUDS6.')
W('| LEDGER_ID | ROW IDs | fulltext lines | A2 flags / note |')
W('|---|---|---|---|')
aud_n=0
for a,b,key,cat,d in [x for x in SEG if x[3]=='auditor']:
    g=groups.get(key); ids=g['ids'] if g else []; ref(ids)
    is_para=bool(re.search(r'para \d+',d))
    if is_para: aud_n+=1
    f=[]
    if not ids: f.append('NO_STRUCTURED_ROW(boilerplate; unit located by line range)')
    if key in ('AUDC7','AUDS6'): f.append('AUDITOR_CHANGE(previous joint auditor Kirtane and Pandit LLP)')
    if key in ('AUDC6','AUDS5'): f.append('OTHER_MATTER; unreviewed management-furnished data')
    if key=='AUDC4': f.append('ENTITY list; ENTITY_CHANGE ND (no prior)')
    W('| %s | %s | %d-%d | %s; %s%s |'%(key,R(ids),a,b,' '.join(f) if f else '-',d,'' if is_para else ' (header, not counted as a paragraph)'))
W('')
# entities
W('## T6 CONSOLIDATION ENTITIES (auditor entity lists)')
W('| LEDGER_ID | ROW IDs | relationship | A2 flags |')
W('|---|---|---|---|')
ent=[(224,'Jaguar Advisory Services Private Limited (JASPL)','Joint venture; held for sale per Ind AS 105; equity method discontinued 13 Dec 2021; share of profit ~Nil'),(580,'PFL Employee Welfare Trust','Included in standalone statement; interim info unreviewed by other auditor; total assets Rs 0.41 cr, revenue and NPAT Nil')]
for i,(ln,nm,rel) in enumerate(ent,1):
    ids=ids_on(ln,ln); ref(ids)
    W('| ENT%02d | %s (line %d) | %s: %s | ENTITY_CHANGE: ND (no prior ledger) |'%(i,R(ids),ln,nm,rel))
ent_all=sum(1 for r in rows if r['t']=='ENTITY')
W('A1 ENTITY table rows (118) are all accounted in groups on this ledger (cover letter, annexure, auditors, notes, annexures). Entity_count_in_consolidation_list: 2.')
W('')
# annexures
W('## T7 ANNEXURES AND TABLES, pp19-30 (one row per source line that carries structured rows)')
W('| LEDGER_ID | page | line | ROW IDs | table | A2 flags |')
W('|---|---|---|---|---|---|')
TBL={19:'Reg 52(4) footnote page',20:'QIP deviation statement (Rs million) table A',21:'QIP deviation statement (Rs million) table A/B',22:'NCD proceeds deviation statement (Rs crore)',23:'Reg 32 NCD issue list, ISIN/series/value date/amount',24:'Annexure A: utilisation of issue proceeds (absolute rupees)',25:'Annexure A: utilisation of issue proceeds (absolute rupees)',29:'Annexure I: ISIN-wise secured NCDs outstanding',30:'Annexure II: book value of assets (columns A to O unresolved)'}
annex_n=0
for k,g in groups.items():
    if g['cat'] in ('annex','footnote'):
        p=min(g['pg']); ln=min(g['ln']); ref(g['ids']); annex_n+=1
        f=[]
        for x in ('ZERO_STANDING','OCR_SUSPECT','OCR_SPACE','COLUMN_UNRESOLVED','NOT_APPLICABLE','OCR_QUALITY'):
            if x in g['fl']: f.append(x if x=='ZERO_STANDING' else 'A1:'+x)
        W('| %s | %d | %d | %s | %s | %s |'%(k,p,ln,R(g['ids']),TBL.get(p,'?'),' '.join(f) if f else '-'))
W('')
# missing
W('## T8 MISSING_FROM_STRUCTURED (A1 lacks a row; loop back to A1)')
W('| ID | line | flag | claim text |')
W('|---|---|---|---|')
miss=[('M001',81,'Independence confirmation: director meets Companies Act and SEBI LODR independence criteria; not debarred by SEBI or other authority; not related to any director (cover letter p2 lines 80-86)'),
('M002',159,'Annexure A item 4: Ms. Soni is not related inter-se to any Director of the Company (p3)'),
('M003',168,'Annexure A item 5: Ms. Soni is not debarred from holding office of Director by any SEBI order or other authority (p4)'),
('M004',228,'Consolidated LRR para 5 conclusion: nothing has come to attention that the Statement is not in accordance with Ind AS 34 (unmodified conclusion)'),
('M005',572,'Standalone LRR para 4 conclusion: nothing has come to attention (unmodified conclusion)'),
('M006',1488,'Certificate para 10 conclusion: nothing has come to attention that Statement details are not in agreement with unaudited standalone results, books and records (unmodified)')]
for m,ln,t in miss:
    W('| %s | %d | MISSING_FROM_STRUCTURED | %s |'%(m,ln,t))
W('')
body='\n'.join(out)
# counts
ids_ref=len(referenced);
orph=sorted(set(r['id'] for r in rows)-referenced)
cnt=dict(notes=notes_total,footnotes=fn_n,line_items=sum(li_by.values()),li_by=li_by,zs=zs_n,agenda=len(ag),annexa=len([x for x in SEG if x[3]=='annexa']),aud=aud_n,annex_lines=annex_n,orph=orph,ids_ref=ids_ref,missing=len(miss))
pickle.dump((body,cnt),open(B+'work/a2-results/body.pkl','wb'))
print(cnt)
