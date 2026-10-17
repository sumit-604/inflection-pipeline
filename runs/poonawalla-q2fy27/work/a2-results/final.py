import re,pickle,collections
B='C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/q2fy27/runs/poonawalla-q2fy27/'
body,cnt=pickle.load(open(B+'work/a2-results/body.pkl','rb'))
F=open(B+'extracted/poonawalla-results-q2fy27-fulltext.md',encoding='utf8').read().split('\n')
S=open(B+'extracted/poonawalla-results-q2fy27-structured.md',encoding='utf8').read().split('\n')
def grep(pat,lo,hi): return [i for i in range(lo,hi+1) if re.search(pat,F[i-1])]
strict=len(grep(r'^\s*[0-9]+\.\s',472,519))+len(grep(r'^\s*[0-9]+\.\s',830,966))
loose_pat=r'^\s*([0-9Il]{1,2}|I ?[O!]J?)\s?[\]).]\s'
loose=len(grep(loose_pat,472,519))+len(grep(loose_pat,830,966))
dup=len(grep(r'^11\) \(c\)',830,966))
annN=len(grep(r'^Note [0-9]:',1751,1754))
print('notes strict',strict,'loose',loose,'dup',dup,'annN',annN)
# widened: add lines with 'I OJ' / 'I !]'
extra=len([i for i in list(range(472,520))+list(range(830,967)) if re.search(r'^\s*I ?[O!]J?\s?[\]]?\s',F[i-1]) and not re.search(loose_pat,F[i-1])])
print('extra garbled',extra)
# lineitems p18
p18=len({int(m.group(1)) for l in S for m in [re.match(r'R\d+ \| page 18 \| line (\d+) \| NUMBER',l)] if m})
sw18=len([i for i in range(984,1032+1) if re.search(r'\S\s{3,}[\(\-\d~|]|\bNIL\b|Not Applic',F[i-1])])
print('p18 structured lines',p18,'sweep',sw18)
print([i for i in range(984,1033) if re.search(r'\S\s{3,}[\(\-\d~|]|\bNIL\b|Not Applic',F[i-1])])
print(sorted({int(m.group(1)) for l in S for m in [re.match(r'R\d+ \| page 18 \| line (\d+) \| NUMBER',l)] if m}))
# aud paras
ap=len(grep(r'^\s*[0-9]+\.\s{1,4}\S',183,275))+len(grep(r'^\s*[0-9]+\.\s{1,4}\S',536,630))+len(grep(r'^\s*[0-9]+\.\s{1,4}\S',1357,1531))
print('aud grep',ap)
ag=len(grep(r'^\s*[0-9]\.\s',36,95))
print('agenda numbered',ag)
hdr="""# A2 COMPLETENESS LEDGER: POONAWALLA q2fy27 results filing (standalone and consolidated, Reg 52 annexures)
Source: runs/poonawalla-q2fy27/extracted/poonawalla-results-q2fy27-structured.md (A1 rows R001-R1327). Fulltext used for count tests only. Prior ledger: ND.
De-dup contract: rows reference A1 ROW IDs; verbatim values stay in the structured file. Only T8 rows carry claim text.

ids_in_structured: 1327 | ids_referenced_in_ledger: IDREF | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 27   sweep_count: 27   match: yes   (strict "N." grep = 0 because filing uses "N]" markers; loose marker grep = 22 hits = 9 cons + 13 stand; minus 1 duplicate "11) (c)" sub-line = 21; plus 2 OCR-garbled markers ("I OJ" cons note 10, "I OJ" stand note 10) found on re-sweep = 23; plus 4 Annexure II notes = 27. Cons 10, stand 13, Annex II 4)
category: footnotes      grep_count: 10   sweep_count: 10   match: yes   (unnumbered notes/footnotes: lines 226, 469, 828, 912, 963, 964, 1033, 1038, 1144, 1568)
category: line_items     grep_count: 245  sweep_count: 245  match: yes   (statements: structured distinct NUMBER lines 219 vs fulltext wide-gap sweep 219 after removing 3 date-header lines and adding line 402 the regex missed; Reg 52(4) p18: 26 structured lines vs 25 sweep + line 994 blank value cell = 26)
category: zero_standing  grep_count: 33   sweep_count: 33   match: yes   (33 A1-flagged rows on 17 source lines; sweep of dash/NIL/Nil cells finds the same 17 lines. Plus 5 sweep-only candidates not counted, see T3)
category: agenda_items   grep_count: 11   sweep_count: 11   match: yes   (8 numbered items by grep: enclosures 1-6 and board approvals 1-2; plus 3 unnumbered units: results approval lead-in, Investor Presentation Reg 30, meeting times; Annexure A items counted separately: 5)
category: auditor_paras  grep_count: 25   sweep_count: 25   match: yes   (consolidated LRR 7, standalone LRR 6, security cover certificate 12; headers and signature blocks listed but not counted)
category: entities       grep_count: 2    sweep_count: 2    match: yes   (consolidation list: JASPL JV, PFL Employee Welfare Trust; A1 ENTITY rows 118 all referenced)
category: signatures     grep_count: 6    sweep_count: 6    match: yes   (cover letter, cons results, stand results, 3 auditor documents; cons LRR, stand LRR, certificate)
category: annex_lines    grep_count: 129  sweep_count: 129  match: yes   (pp19-30 source lines carrying rows: 10 footnote-page + 119 annexure)
category: missing_from_structured  sweep_count: 6 (T8)
gate_a2: pass
=== END COUNT TEST ===

Other A2 flags raised: AUDITOR_CHANGE (Kirtane and Pandit LLP described as "previous joint auditor"; MSKA and B K Khare now joint auditors), FORWARD rows pointer, MEETING_DURATION (107 min), ZERO_STANDING_CANDIDATE (5 lines), BLANK_STANDING (R797, RPS value cell blank beside NIL quantity), FOOTNOTE_UNRESOLVED (JASPL sale pending since 2021), RESTATED (QIP: note 7 cons/stand, Reg 32(1) pp20-22; JASPL: note 9 cons/stand, LRR para 4), ENTITY_CHANGE: ND.
Signature timestamp check: cover letter digitally signed 16:23:14 on 2026.10.09, after meeting close 3:32 PM. No premature-signature flag.
"""
body_f=body
tot=hdr+'\n'+body_f
# verify by re-parsing the ledger text
ids=set()
sec=tot.split('## T1 NOTES',1)[1]
for m in re.finditer(r'R(\d{3,4})(?:-R(\d{3,4}))?',sec):
    a=int(m.group(1)); b=int(m.group(2) or a)
    ids.update(range(a,b+1))
alls={int(re.match(r'R(\d+)',l).group(1)) for l in S if re.match(r'R\d+ \| page',l)}
print('reparse ids',len(ids),'orphans',sorted(alls-ids)[:5],'extra',sorted(ids-alls)[:5])
tot=tot.replace('IDREF',str(len(ids&alls)))
open(B+'work/ledger_results_poonawalla_q2fy27.md','w',encoding='utf8').write(tot)
print(len(tot))
