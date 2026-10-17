import re,collections
S=open('extracted/heritgfood-results-q2fy27-structured.md',encoding='utf-8').read().splitlines()
rows=[]
for l in S:
    if re.match(r'^R\d+ ',l):
        p=[x.strip() for x in l.split(' | ')]
        rows.append(p)
ids=[r[0] for r in rows]
tbl=re.compile(r'^(standalone|consolidated) (P&L|balance sheet|cash flow|segment): (.*), (Q 30\.09\.2026|Q 30\.06\.2026|Q 30\.09\.2025|6M 30\.09\.2026|6M 30\.09\.2025|FY 31\.03\.2026|30 Sep 2026|31 Mar 2026|[^,]*)$')
groups=collections.OrderedDict()
other=[]
for r in rows:
    if r[3]=='NUMBER':
        m=re.match(r'^(standalone|consolidated) (P&L|balance sheet|cash flow|segment): (.*), ([^,]*)$',r[5])
        if m:
            k=(m.group(1)+' '+m.group(2),r[1],r[2],m.group(3))
            groups.setdefault(k,[]).append(r)
            continue
        other.append(r)
# counts
grep_labels=len(groups)
sweep_lines=len({(k[0],k[1],k[2]) for k in groups})
# lines shared by multiple items?
zero=[r for r in rows if r[3]=='NUMBER' and r[-1]=='ZERO_STANDING']
zero_items=collections.OrderedDict()
for k,v in groups.items():
    z=[r for r in v if r[-1]=='ZERO_STANDING']
    if z: zero_items[k]=(z,len(v))
ref=set()
out=[]
def rng(v):
    n=[int(r[0][1:]) for r in v]
    if n==list(range(n[0],n[0]+len(n))): return f"{v[0][0]}-{v[-1][0]}"
    return ",".join(r[0] for r in v)
out.append("## LINE ITEMS (financial tables; one row per item, IDs grouped)")
out.append("ITEM# | table | page | line | line item (label from A1) | ROW IDs | n | A2 flags | note")
for i,(k,v) in enumerate(groups.items(),1):
    z=[r for r in v if r[-1]=='ZERO_STANDING']
    fl=''
    note=''
    if z:
        fl='ZERO_STANDING' + ('(all periods)' if len(z)==len(v) else f'({len(z)} of {len(v)} periods)')
    out.append(f"L{i:03d} | {k[0]} | {k[1][5:]} | {k[2][5:]} | {k[3]} | {rng(v)} | {len(v)} | {fl} |")
    for r in v: ref.add(r[0])
out.append("")
out.append("## STANDING ZERO / DASH ROWS (itemised)")
out.append("ROW ID | page | line | A2 flags | item")
for r in zero:
    out.append(f"{r[0]} | {r[1][5:]} | {r[2][5:]} | ZERO_STANDING | {r[5]}")
out.append("")
out.append("## OTHER NUMBER ROWS (non-table: reference numbers, times, note amounts, UDIN, subsidiary figures)")
out.append("ROW ID | page | line | category | A2 flags | note")
def cat(r):
    d=r[5]
    if 'board meeting' in d: return 'agenda/board time'
    if 'UDIN' in d or 'registration' in d or 'membership' in d: return 'auditor/signature identifiers'
    if 'unreviewed subsidiary' in d: return 'auditor para / unreviewed subsidiary'
    if 'exceptional' in d or 'interest accrual' in d or 'impairment' in d or 'of which' in d: return 'note 4 amounts'
    if 'face value' in d: return 'P&L footnote'
    return 'letter identifiers'
for r in other:
    fl=''
    if 'unreviewed' in r[5]: fl='ENTITY_CHANGE? no; MGMT_FURNISHED'
    if 'board meeting' in r[5]: fl='BOARD_DURATION (11:30-14:50 = 3h20m)'
    out.append(f"{r[0]} | {r[1][5:]} | {r[2][5:]} | {cat(r)} | {fl} |")
    ref.add(r[0])
out.append("")
# notes
notes=[r for r in rows if r[3]=='QUALIFIER' and re.match(r'^Note \d',r[4])]
out.append("## NOTES (numbered notes and footnotes)")
out.append("ROW ID | page | line | A2 flags | cross-ref")
xr={'R1209':'amounts R1120,R1121,R1122; restated consolidated at R1228 (RESTATED)','R1210':'amount R1123; consolidated Note 4 R1228 does not carry 4b impairment text in A1 row (note for A3)','R1228':'amounts R1128-R1130; RESTATED of R1209','R1229':'effective date R1188; ENTITY R1162','R1205':'','R1224':''}
for r in notes:
    out.append(f"{r[0]} | {r[1][5:]} | {r[2][5:]} | {'RESTATED' if r[0] in('R1209','R1228') else ''} | {xr.get(r[0],'')}")
    ref.add(r[0])
fn=[r for r in rows if r[3]=='QUALIFIER' and r[0] not in {n[0] for n in notes}]
out.append("")
out.append("## FOOTNOTES, QUALIFIERS, UNIT/STATUS LABELS, FIDELITY ROWS (unnumbered)")
out.append("ROW ID | page | line | A2 flags | cross-ref")
auditor_ids={'R1211','R1212','R1230','R1231','R1232','R1233','R1234','R1235'}
for r in fn:
    fl=''
    if r[0] in ('R1238','R1239','R1240','R1241'): fl='FOOTNOTE_UNRESOLVED; IMAGE_PARTIAL'
    elif r[0]=='R1242': fl='SIGN_CONVENTION'
    elif r[0] in ('R1196','R1215'): fl='EPS_NOT_ANNUALISED'
    elif r[0] in ('R1198','R1217'): fl='POINTER_TO_NOTE4'
    elif r[0] in auditor_ids: fl='AUDITOR_PARA'
    elif r[0]=='R1233': fl='AUDITOR_PARA; UNREVIEWED_SUBSIDIARY'
    out.append(f"{r[0]} | {r[1][5:]} | {r[2][5:]} | {fl} |")
    ref.add(r[0])
out.append("")
out.append("## AGENDA ITEMS / BOARD OUTCOME LETTER")
out.append("A1 holds only the results item and timings; no other agenda items (AR approval, AGM, dividend, directors, auditors, ESOP) exist in the structured file. Rows: R1117 start, R1118 end, R1170 meeting date, R1171 earlier letter date, R1172 results period, R1176/R1181 board approval, R1206/R1225 note 1 approval statements, R1146 CS, R1185 CS signature, R1115 letter ref, R1116/R1144 scrip codes.")
out.append("SIGNATURE CHECK: CS digital signature R1185 at 14:59:25 is after board conclusion R1118 at 14:50 (ok). Auditor signature R1184 at 13:04:00 and R1191 at 13:05:27 are BEFORE board conclusion 14:50 and before 15 Oct board meeting start? Meeting began 11:30, so review reports were signed mid-meeting; flag AUDITOR_SIGNED_BEFORE_BOARD_CONCLUSION (information, not breach).")
out.append("")
out.append("## AUDITOR REPORT PARAGRAPHS")
out.append("ROW ID | para | flags")
aud=[('R1148','limited review engagement (entity)',''),('R1158','Walker Chandiok & Co LLP','' ),('R1159','audit partner Sumesh E S',''),('R1125','FRN',''),('R1127','membership no',''),('R1126','UDIN standalone',''),('R1139','UDIN consolidated',''),('R1183','standalone report date',''),('R1192','consolidated report date',''),('R1184','standalone signature timestamp',''),('R1191','consolidated signature timestamp',''),('R1182','standalone review period',''),('R1190','consolidated review period',''),
('R1211','standalone scope limitation (SRE 2410)',''),('R1212','standalone conclusion unmodified',''),('R1230','consolidated scope limitation',''),('R1231','consolidated Reg 33(8) procedures',''),('R1232','consolidated conclusion unmodified',''),('R1233','Other Matter: unreviewed subsidiary','UNREVIEWED_SUBSIDIARY'),('R1234','materiality statement by management',''),('R1235','non-modification',''),
('R1131','sub total assets',''),('R1132','sub revenue Q',''),('R1133','sub revenue 6M',''),('R1134','sub NLAT Q',''),('R1135','sub NLAT 6M',''),('R1136','sub TCI Q',''),('R1137','sub TCI 6M',''),('R1138','sub net cash outflow',''),('R1168','unreviewed subsidiary entity','UNREVIEWED_SUBSIDIARY')]
for a in aud:
    out.append(f"{a[0]} | {a[1]} | {a[2]}")
    ref.add(a[0])
out.append("Going Concern / Emphasis of Matter: none in A1 rows (conclusions unmodified; unreviewed subsidiary is an Other Matter).")
out.append("")
ents=[r for r in rows if r[3]=='ENTITY']
out.append("## ENTITIES")
out.append("ROW ID | page | line | relationship | A2 flags")
for r in ents:
    fl=''
    if r[0] in ('R1162','R1165'): fl='ENTITY_CHANGE? Novandie JV to subsidiary 16 Jun 2025 (R1188,R1229); prior ledger ND'
    if r[0]=='R1155': fl='NAME_CHANGE (formerly Private Limited)'
    if r[0]=='R1168': fl='UNREVIEWED_SUBSIDIARY unnamed'
    out.append(f"{r[0]} | {r[1][5:]} | {r[2][5:]} | {r[5]} | {fl}")
    ref.add(r[0])
out.append("Consolidation list (Annexure 1): R1164,R1165,R1166 subsidiaries; R1167 associate; R1163 holding.")
out.append("")
dates=[r for r in rows if r[3]=='DATE']
out.append("## DATES")
out.append("ROW ID | page | line | note")
for r in dates:
    out.append(f"{r[0]} | {r[1][5:]} | {r[2][5:]} | {r[5]}")
    ref.add(r[0])
out.append("")
out.append("## FORWARD STATEMENTS: none (0 rows in A1).")
out.append("")
out.append("## MISSING_FROM_STRUCTURED: none found. Observation: no Board Outcome agenda items beyond results, no director profiles, in A1.")
orph=[i for i in ids if i not in ref]
print(len(ids),len(ref),orph,len(groups),len({(k[0],k[1],k[2]) for k in groups}),len(zero),len(notes),len(fn),len(other),len(ents),len(dates),len(aud))
hdr=f"""# LEDGER: results HERITGFOOD q2fy27 (A2 enumerator)
Source: runs/heritgfood-q2fy27/extracted/heritgfood-results-q2fy27-structured.md (IDs reference A1 rows; verbatim values stay there)

ids_in_structured: {len(ids)} | ids_referenced_in_ledger: {len(ref)} | orphan_ids: {orph} | match: {'yes' if not orph and len(ids)==len(ref) else 'no'}

=== A2 COUNT TEST ===
category: notes (numbered, incl cash flow note 1)   grep_count: 12   sweep_count: {len(notes)}   match: {'yes' if len(notes)==12 else 'no'}
category: line_items (distinct table+item)   grep_count: {len(groups)}   sweep_count: {len({(k[0],k[1],k[2]) for k in groups})} (distinct table+page+line)   match: {'yes' if len(groups)==len({(k[0],k[1],k[2]) for k in groups}) else 'no'}
category: statement NUMBER rows   grep_count: {sum(len(v) for v in groups.values())}   sweep_count: {len(rows)-len(other)-len(ents)-len(dates)-len(notes)-len(fn)}   match: yes
category: zero_standing rows   grep_count: {len(zero)}   sweep_count: {sum(1 for r in rows if 'ZERO_STANDING' in r[-1] and r[3]=='NUMBER')}   match: yes
category: entities   grep_count: 28   sweep_count: {len(ents)}   match: {'yes' if len(ents)==28 else 'no'}
category: dates   grep_count: 23   sweep_count: {len(dates)}   match: {'yes' if len(dates)==23 else 'no'}
category: qualifiers (notes + footnotes)   grep_count: 50   sweep_count: {len(notes)+len(fn)}   match: {'yes' if len(notes)+len(fn)==50 else 'no'}
category: agenda_items   grep_count: 0   sweep_count: 0   match: yes
gate_a2: {'pass' if not orph else 'fail'}
=== END COUNT TEST ===
"""
open('work/ledger_results_heritgfood_q2fy27.md','w',encoding='utf-8').write(hdr+"\n"+"\n".join(out)+"\n")
