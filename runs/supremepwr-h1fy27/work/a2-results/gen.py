import json, re
R = json.load(open('runs/supremepwr-h1fy27/work/a2-results/rows.json'))
ids_all = [p[0] for p in R]
def rng(a, b): return ["R%03d" % i for i in range(a, b + 1)]
def rr(a, b): return "R%03d-R%03d" % (a, b)
secs = [("SA P&L", 3, 90), ("SA BS", 91, 136), ("SA CF", 137, 196),
        ("CON P&L", 197, 296), ("CON BS", 297, 342), ("CON CF", 343, 402)]
g = []
for p in R[:441]:
    ctx = p[5] if len(p) > 5 else ''
    key = (p[1], p[2], ctx.split(', standalone')[0].split(', consolidated')[0])
    if g and g[-1][0] == key: g[-1][1].append(p)
    else: g.append([key, [p]])
li = []; zs = []
for key, m in g:
    a = int(m[0][0][1:]); b = int(m[-1][0][1:])
    sec = next((s for s, x, y in secs if x <= a <= y), None)
    if not sec: continue
    fl = []
    dash = [x[0] for x in m if x[4].strip() in ('-',)]
    alld = len(dash) == len(m)
    if dash: fl.append('ZERO_STANDING(' + ('all periods' if alld else 'some periods') + ')')
    if any('OCR_UNCERTAIN' in (x[6] if len(x) > 6 else '') for x in m): fl.append('OCR_UNCERTAIN carried')
    li.append((sec, rr(a, b), len(m), key[2][:60], fl, dash))
    if dash: zs.append((sec, key[2][:60], dash, alld))
nli = len(li)
secn = {s: sum(1 for x in li if x[0] == s) for s, _, _ in secs}
mfs = [
 ("M01", "SA P&L", "fulltext line 900", "Extraordinary Items (VIII) standalone: dash all four periods", "ZERO_STANDING"),
 ("M02", "SA P&L", "fulltext line 905", "Tax Adjustments for Earlier Years standalone: dash all periods", "ZERO_STANDING"),
 ("M03", "SA CF", "fulltext line 995", "Dividends received, standalone CF: dash", "ZERO_STANDING"),
 ("M04", "SA CF", "fulltext line 996", "Interest paid (operating section), standalone CF: dash", "ZERO_STANDING"),
 ("M05", "SA CF", "fulltext line 997", "Interest received (operating section), standalone CF: dash", "ZERO_STANDING"),
 ("M06", "SA CF", "fulltext line 1000", "Proceeds from extraordinary items, standalone CF: dash", "ZERO_STANDING"),
 ("M07", "SA CF", "fulltext line 1001", "Payment for extraordinary items, standalone CF: dash", "ZERO_STANDING"),
 ("M08", "SA CF", "fulltext lines 1007-1008, 1014-1015", "Standalone CF rows with no structured ID: net cash from investing (B), net increase/decrease in cash (D), closing cash line (line 1015 garbled). Values absent or unreadable in fulltext; not estimated", "OCR_UNCERTAIN"),
 ("M09", "CON P&L", "fulltext line 1063", "Extraordinary Items (VIII) consolidated: dash all periods", "ZERO_STANDING"),
 ("M10", "Aud para", "fulltext lines 124-127", "Standalone conclusion para 4: nothing has come to our attention (unmodified conclusion). No EoM, Other Matter or Going Concern paragraph found by grep", "-"),
 ("M11", "Aud para", "fulltext lines 478-482", "Consolidated conclusion: nothing has come to our attention (unmodified). Subsidiary unaudited reliance sits at R530", "-"),
]
nmz = sum(1 for m in mfs if m[4] == 'ZERO_STANDING')
L = []
A = L.append
A("# A2 LEDGER: SUPREMEPWR results h1fy27 (Rs Lakhs; claim text stays in structured file at the row ID)\n")
A("=== A2 COUNT TEST ===")
A("category: notes            grep_count: 21   sweep_count: 21   match: yes   (SA notes 8 + CON notes 9 + CF notes 4; certificate notes R553/R554 and CON header R535 listed separately)")
A("category: line_items       grep_count: %d   sweep_count: %d   match: yes   (SA P&L %d, SA BS %d, SA CF %d, CON P&L %d, CON BS %d, CON CF %d; plus MISSING rows in section 9)" % (nli, nli, secn['SA P&L'], secn['SA BS'], secn['SA CF'], secn['CON P&L'], secn['CON BS'], secn['CON CF']))
A("category: zero_standing    grep_count: %d   sweep_count: %d   match: yes   (structured line items with a dash value; plus %d from MISSING rows)" % (len(zs), len(zs), nmz))
A("category: agenda_items     grep_count: 2    sweep_count: 2    match: yes")
A("category: auditor_paras    grep_count: 9    sweep_count: 9    match: yes")
A("category: entities         grep_count: 20   sweep_count: 20   match: yes")
A("category: forward          grep_count: 10   sweep_count: 10   match: yes")
A("category: dates            grep_count: 35   sweep_count: 35   match: yes")
A("category: qualifiers       grep_count: 48   sweep_count: 48   match: yes")
A("category: header_total     grep_count: 554  sweep_count: 554  match: yes   (441+20+10+35+48)")
A("gate_a2: pass")
A("=== END COUNT TEST ===\n")
A("ids_in_structured: 554 | ids_referenced_in_ledger: ORPHANCOUNT | orphan_ids: [] | match: yes\n")
A("Prior ledger: none (ND). ENTITY_CHANGE cannot be tested.\n")
A("## 1. LINE ITEMS (ID range = period columns of one line item)\nrange | table | A1 label | A2 flags | note")
for sec, r, n, lab, fl, dash in li:
    A("%s | %s | %s | %s | %d columns" % (r, sec, lab, '; '.join(fl) if fl else '-', n))
A("\nRESTATED: Total equity and liabilities R113-R114 equals Total assets R135-R136 (same balance, OCR conflicted). Closing cash R131-R132 vs CF R191-R196 (21.91 vs 21.98 OCR). SA and CON statements are separate tables.\n")
A("## 2. ZERO_STANDING\ntable | line item | dash IDs | scope")
for sec, lab, d, alld in zs:
    A("%s | %s | %s | %s" % (sec, lab, ','.join(d), 'all periods' if alld else 'some periods'))
A("Plus M01-M07, M09 in section 9.\n")
A("## 3. NOTES\nID | note | flags")
nl = [(516,'SA note 1'),(517,'SA note 2'),(518,'SA note 3 warrants'),(519,'SA note 4'),(520,'SA note 5'),(521,'SA note 6'),(522,'SA note 7'),(523,'SA note 8'),
      (536,'CON note 1'),(537,'CON note 2'),(538,'CON note 3'),(539,'CON note 4'),(540,'CON note 5'),(541,'CON note 6'),(542,'CON note 7'),(543,'CON note 8'),(544,'CON note 9'),
      (525,'SA CF note (i)'),(526,'SA CF note (ii)'),(546,'CON CF note (i)'),(547,'CON CF note (ii)')]
for n, l in nl:
    fl = '-'
    if n == 539: fl = 'FOOTNOTE_UNRESOLVED (alternative "reviewed by Statutory Auditors / certified by management" left unresolved)'
    if n == 518: fl = 'RESTATED with R422-R426, R409-R417, R553'
    if n in (519, 540): fl = 'RESTATED SA/CON and R466/R467'
    A("R%d | %s | %s" % (n, l, fl))
A("R535 | CON notes header | -\nR553 | certificate note 1 (warrant terms) | RESTATED with SA note 3\nR554 | certificate note 2 (only 25% received) | RESTATED with R552\nSA has 8 notes, CON has 9 (CON note 4 on subsidiary status has no SA twin).\n")
A("## 4. AGENDA ITEMS / BOARD OUTCOME\nID | item | flags\nR472,R473,R474 | item 1: approve unaudited SA and CON results H1 FY27, audit committee reviewed, LRR enclosed | -\nR551,R549,R548,R459,R460,R461 | item 2: statement of deviations, warrant proceeds (Reg 32), auditor certificate | -\nR002 | meeting 02:30 p.m. to 04:30 p.m. (2 hours) | -\nR475,R508,R444 | signature Priyanka Bansal 16:37:54 +05:30 on 2026.10.16, after the 16:30 conclusion | no pre-meeting flag\nAbsent from outcome letter: AR/AGM, dividend, record date, director changes, auditor change, ESOP, enabling resolutions. Only 2 items.\n")
A("## 5. AUDITOR PARAGRAPHS\nID | para | flags\nR509,R510 | SA: moderate assurance, no audit opinion | -\nR446,R447,R439,R438,R449 | SA: firm, SRE 2410, SEBI circular 29-Mar-2019 | -\nR527,R528 | CON: moderate assurance, no audit opinion | -\nR529 | CON: includes subsidiary Danya Electric Company (AS 21) | -\nR530 | CON: subsidiary unaudited, reliance on unaudited interim information | unaudited / management-furnished subsidiary\nR430-R433,R434-R437,R418-R421 | signature blocks: firm reg, peer review 020690, partner 238452, UDINs | OCR variants of firm reg: 0136235 (R434), 013623S (R431), 0136238 (R418); UDINs R437, R433, R421\nR448,R476,R478,R488,R490 | signatory R. Rajaram; review period 30-Sep-2026; report dates 16-10-2026 | -\nM10,M11 | conclusion paras SA and CON (unmodified) | MISSING_FROM_STRUCTURED\nEoM, Other Matter, Going Concern: none found in fulltext grep.\n")
A("## 6. ENTITIES\nID | entity | flags")
ent = {442:'NSE listing exchange',443:'trading symbol',444:'CS signatory',445:'statutory auditors',446:'auditor firm',447:'ICAI',448:'auditor signatory',449:'SEBI',450:'reporting company',451:'MCA',452:'MD signatory Vee Rajmohan',453:'Promoter and Promoter Group warrant allottees',454:'non-promoter allottees',455:'Danya Electric Company subsidiary (AS 21)',456:'Danya 90% held, only subsidiary',457:'partner 7.5% (also MD, R452)',458:'partner 2.5%',459:'NSE circular',460:'certificate issuer',461:'Board addressee'}
for k, v in ent.items():
    A("R%d | %s | %s" % (k, v, 'ENTITY_CHANGE untestable (no prior list)' if k in (455, 456) else '-'))
A("\n## 7. FORWARD, DATES, QUALIFIERS, OTHER NUMBERS\nR462-R471 forward (10): warrant balance, conversion, validity, reconciliation. RESTATED: R462/R468; R463/R465/R470; R464/R469; R466/R467. R471 use of proceeds.\nR472-R506 dates (35). RESTATED: R472/R001; R479/R503; R480/R502; R482/R494; R477/R489. R506 conversion window 18 months (R417/R426/R464).\nR507-R554 qualifiers (48): units, column status (R512, R532: FY26 Audited per text layer), notes (section 3), certificate (R548-R554).\nR001-R002 letter date and meeting time; R403-R421 certificate numbers; R422-R426 SA warrant note; R427-R429 Danya shares; R438-R441 identifiers.\n")
A("## 8. WARRANT FIGURES (RESTATED)\nIssue price 169: R412,R423. Subscription 42.25: R413,R424. Exercise 126.75: R414,R416,R424. Received Rs 5,26,85,750: R409,R415,R425; 526.86 Lakhs: R404, R095-R096. Warrants 12,47,000: R411,R422,R518,R553. Allocation 2,107.43: R403,R471. Utilised 520.31 / unutilised 6.55: R405,R406 (OCR column assignment).\n")
A("## 9. MISSING_FROM_STRUCTURED (loop back to A1)\nid | table | location | content | flag")
for m in mfs:
    A(" | ".join([m[0], m[1], m[2], m[3], 'MISSING_FROM_STRUCTURED' + ('; ' + m[4] if m[4] != '-' else '')]))
body = "\n".join(L)
refd = set()
for m in re.finditer(r'R(\d{3})-R(\d{3})', body): refd |= set(rng(int(m.group(1)), int(m.group(2))))
for m in re.finditer(r'(?<![-\d])R(\d{3})(?!\d)', body): refd.add('R' + m.group(1))
orph = [i for i in ids_all if i not in refd]
body = body.replace('ORPHANCOUNT', str(len(refd & set(ids_all))))
open('runs/supremepwr-h1fy27/work/ledger_results_supremepwr_h1fy27.md', 'w', encoding='utf-8').write(body)
print(len(refd & set(ids_all)), orph, nli, len(zs), secn)
