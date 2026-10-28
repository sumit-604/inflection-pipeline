# A2 COMPLETENESS LEDGER: WeWork India Management Ltd (WEWORK) Q2 FY27 results filing
source: A1 structured extraction runs/wework-q2fy27/extracted/wework-results-q2fy27-structured.md (R001-R1112). Prior ledger: none (first review), so no DROPPED_SLIDE / ENTITY_CHANGE diff is possible. Row format: ROW_ID | category | A2 flags | cross-ref / materiality note. Claim text lives in the structured file at the ID.

=== A2 COUNT TEST ===
category: notes        grep_count: 21   sweep_count: 21   match: yes   (structured grep "Note N:" = 17, plus statement notes 1) and 2) in SA and CA = 4, total 21; fulltext numbered-line grep = 20 because CA note 5 has no number printed in the text layer, recovered by sweep at R1092)
category: line_items   grep_count: 232   sweep_count: 232   match: yes   (grep = period-NUMBER rows / columns per statement page; sweep = distinct page/line/label groups; 716 period rows = 169x2 + 63x6)
category: zero_standing grep_count: 52 cells   sweep_count: 52 cells in 25 line items   match: yes   (grep flag ZERO_STANDING)
category: agenda_items grep_count: 2   sweep_count: 2   match: yes   (fulltext lines 52, 60 numbered 1., 2.)
category: auditor_paras grep_count: 10   sweep_count: 10   match: yes   (fulltext lines 101,107,115,126 SA; 387,394,402,415,433,442 CA)
category: entities     grep_count: 67   sweep_count: 67   match: yes   (consolidation list 4)
category: forward      grep_count: 9   sweep_count: 9   match: yes
category: tieouts      grep_count: 66   sweep_count: 66   match: yes   (header: 66 checks, 0 FAIL)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 1112 | ids_referenced_in_ledger: 1112 | orphan_ids: [] | match: yes

## A. NOTES (numbered notes, standalone SA and consolidated CA)
Note | page | anchor ROW | category | A2 flags | related structured IDs (numbers/dates/entities/forward on the same note lines) | cross-ref
SA-1 | p4 | R975 | note: Standalone Statement of Assets and Liabilities (statement; line items in section B page 4) | - | - | 
SA-2 | p5 | R988 | note: Standalone Statement of cash flows (statement; line items in section B page 5) | - | - | 
SA-3 | p6 | R1005 | note: basis of results, Reg 33, Audit Committee/Board approval, limited review | - | R816-R817,R895,R1005 | RESTATED in CA-3
SA-4 | p6 | R1006 | note: Ind AS 34 basis | - | R1006 | RESTATED in CA-4
SA-5 | p6 | R1007 | note: Labour Codes exceptional item | - | R322-R324,R818-R819,R864,R896-R897,R1007-R1008 | RESTATED in CA-5; exceptional-item provision 42.94 Mn (SA R324) vs 43.26 Mn (CA R755), difference 0.32 Mn from subsidiaries; also drives the exceptional item P&L row
SA-6 | p6 | R1009 | note: IPO offer for sale | - | R325-R332,R820,R898-R899,R1009-R1010 | RESTATED in CA-6; IPO was a pure offer for sale, no primary proceeds to the company stated
SA-7 | p6 | R1011 | note: ESOP grants | - | R333-R334,R821-R822,R900,R1011 | RESTATED in CA-7
SA-8 | p6 | R1012 | note: paid-up capital change on ESOP exercise | - | R335-R340,R1012 | RESTATED in CA-8
SA-9 | p6 | R1013 | note: segment (single segment) | - | R341,R823,R1013-R1014 | RESTATED in CA-9
SA-10 | p6 | R1015 | note: NCLT capital reduction scheme | - | R342-R343,R824-R825,R865-R866,R901,R1015 | RESTATED in CA-10; pending NCLT scheme, accumulated loss 20,501.60 Mn against Securities Premium
CA-1 | p10 | R1059 | note: Consolidated Statement of Assets and Liabilities (statement; line items in section B page 10) | - | - | 
CA-2 | p11 | R1073 | note: Consolidated Statement of cash flows (statement; line items in section B page 11) | - | - | 
CA-3 | p12 | R1090 | note: basis of results, Reg 33, Audit Committee/Board approval, limited review | - | R848-R849,R924,R1090 | RESTATED of SA-3
CA-4 | p12 | R1091 | note: Ind AS 34 basis | - | R1091 | RESTATED of SA-4
CA-5 | p12 | R1092 | note: Labour Codes exceptional item | NOTE_NUMBER_NOT_IN_TEXT_LAYER | R753-R755,R850-R851,R867,R925-R926,R1092-R1093 | RESTATED of SA-5; exceptional-item provision 42.94 Mn (SA R324) vs 43.26 Mn (CA R755), difference 0.32 Mn from subsidiaries; also drives the exceptional item P&L row
CA-6 | p12 | R1094 | note: IPO offer for sale | - | R756-R763,R852,R927-R928,R1094-R1095 | RESTATED of SA-6; IPO was a pure offer for sale, no primary proceeds to the company stated
CA-7 | p12 | R1096 | note: ESOP grants | - | R764-R765,R853-R854,R929,R1096 | RESTATED of SA-7
CA-8 | p12 | R1097 | note: paid-up capital change on ESOP exercise | - | R766-R771,R1097 | RESTATED of SA-8
CA-9 | p12 | R1098 | note: segment (single segment) | - | R772,R855,R1098-R1099 | RESTATED of SA-9
CA-10 | p12 | R1100 | note: NCLT capital reduction scheme | - | R773-R774,R856-R857,R868-R869,R930,R1100 | RESTATED of SA-10; pending NCLT scheme, accumulated loss 20,501.60 Mn against Securities Premium
CA-11 | p12 | R1101 | note: standalone figures table (revenue, PBT, PAT) | - | R775-R792,R931-R937,R1101-R1112 | ties to SA P&L page 3 (extractor tie-outs R1110-R1112); only on consolidated page

Unnumbered notes, footnotes and fine print:
ROW_ID | category | A2 flags | note
R955 | footnote | - | unit footnote Rs Million (SA P&L)
R973 | footnote | - | EPS not annualised (SA)
R970 | footnote | - | OCI not reclassified header (SA)
R1051 | footnote | - | OCI not reclassified header (CA)
R966 | footnote | - | exceptional item refer Note 5 (SA)
R1047 | footnote | - | exceptional item refer Note 5 (CA)
R1057 | footnote | - | EPS not annualised (CA)
R1008 | footnote | - | estimate qualifier on Note 5 provision (SA)
R1093 | footnote | - | estimate qualifier on Note 5 provision (CA)
R1014 | footnote | - | CODM qualifier (SA Note 9)
R1099 | footnote | - | CODM qualifier (CA Note 9)
R148 | footnote | - | face value per share (SA EPS)
R149 | footnote | - | nominal value for EPS (SA)
R561 | footnote | - | face value per share (CA EPS)
R562 | footnote | - | nominal value for EPS (CA)
R943 | footnote | - | Encl. reference to Annexure A
R1003 | footnote | - | break-up of cash table header (SA)
R1088 | footnote | - | break-up of cash table header (CA)

## B. LINE ITEMS (every row of every financial table, one ledger row per line item; IDs span all period columns)
Cols: P&L pages = 6 columns (Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26, FY26); BS = 2 (30-Sep-2026, 31-Mar-2026); CF = 2 (H1FY27, H1FY26); Note 11 table = 6.
Grp | statement | page | line | line item label (A1 context label) | ROW IDs | cols | A2 flags
G001 | SA P&L | p3 | L158 | Revenue from operations | R010-R015 | 6 | -
G002 | SA P&L | p3 | L159 | Other income | R016-R021 | 6 | -
G003 | SA P&L | p3 | L160 | Finance income | R022-R027 | 6 | -
G004 | SA P&L | p3 | L161 | Total income | R028-R033 | 6 | -
G005 | SA P&L | p3 | L163 | Sub-contracting cost | R034-R039 | 6 | ZERO_STANDING(2 of 6 cols nil)
G006 | SA P&L | p3 | L164 | Employee benefits expense | R040-R045 | 6 | -
G007 | SA P&L | p3 | L165 | Finance costs | R046-R051 | 6 | -
G008 | SA P&L | p3 | L166 | Depreciation and amortisation expense | R052-R057 | 6 | -
G009 | SA P&L | p3 | L167 | Operating expenses | R058-R063 | 6 | -
G010 | SA P&L | p3 | L168 | Other expenses | R064-R069 | 6 | -
G011 | SA P&L | p3 | L169 | Total expenses | R070-R075 | 6 | -
G012 | SA P&L | p3 | L170 | SI No. 3 Profit/(Loss) before exceptional item and tax for the period/year (1-2) | R076-R081 | 6 | -
G013 | SA P&L | p3 | L171 | SI No. 4 Exceptional item (Refer Note 5) | R082-R087 | 6 | ZERO_STANDING(5 of 6 cols nil)
G014 | SA P&L | p3 | L172 | SI No. 5 Profit/(Loss) before tax for the period/year (3+4) | R088-R093 | 6 | -
G015 | SA P&L | p3 | L174 | Current tax charge | R094-R099 | 6 | ZERO_STANDING(all columns nil)
G016 | SA P&L | p3 | L175 | Deferred tax (credit)/charge | R100-R105 | 6 | ZERO_STANDING(5 of 6 cols nil)
G017 | SA P&L | p3 | L176 | Total tax expense | R106-R111 | 6 | ZERO_STANDING(5 of 6 cols nil)
G018 | SA P&L | p3 | L177 | SI No. 7 Profit/(Loss) for the period/year (5-6) | R112-R117 | 6 | -
G019 | SA P&L | p3 | L180 | Re-measurement (loss)/gain on defined benefit plans | R118-R123 | 6 | -
G020 | SA P&L | p3 | L181 | Income tax effect on above credit/(charge) | R124-R129 | 6 | ZERO_STANDING(5 of 6 cols nil)
G021 | SA P&L | p3 | L182 | SI No. 8 OCI for the period/year (net of tax) | R130-R135 | 6 | -
G022 | SA P&L | p3 | L183 | SI No. 9 Total comprehensive income/(Loss) for the period/year (7+8) | R136-R141 | 6 | -
G023 | SA P&L | p3 | L184 | SI No. 10 Paid-up equity share capital (Face Value of Rs.10/- per share) | R142-R147 | 6 | -
G024 | SA P&L | p3 | L186 | Basic (Rs. per share) | R150-R155 | 6 | -
G025 | SA P&L | p3 | L187 | Diluted (Rs. per share) | R156-R161 | 6 | -
G026 | SA BS | p4 | L199 | (a) Property, plant and equipment | R162-R163 | 2 | -
G027 | SA BS | p4 | L200 | (b) Capital work-in-progress | R164-R165 | 2 | -
G028 | SA BS | p4 | L201 | (c) Right-of-use assets | R166-R167 | 2 | -
G029 | SA BS | p4 | L202 | (d) Intangible assets | R168-R169 | 2 | -
G030 | SA BS | p4 | L203 | (e) Intangible assets under development | R170-R171 | 2 | ZERO_STANDING(1 of 2 cols nil)
G031 | SA BS | p4 | L205 | (i) Investments (non-current) | R172-R173 | 2 | -
G032 | SA BS | p4 | L206 | (ii) Other financial assets (non-current) | R174-R175 | 2 | -
G033 | SA BS | p4 | L207 | (g) Deferred tax assets (net) | R176-R177 | 2 | -
G034 | SA BS | p4 | L208 | (h) Income tax assets (net) | R178-R179 | 2 | -
G035 | SA BS | p4 | L209 | (i) Other non-current assets | R180-R181 | 2 | -
G036 | SA BS | p4 | L210 | Total non-current assets | R182-R183 | 2 | -
G037 | SA BS | p4 | L213 | (i) Investments (current) | R184-R185 | 2 | -
G038 | SA BS | p4 | L214 | (ii) Trade receivables | R186-R187 | 2 | -
G039 | SA BS | p4 | L215 | (iii) Cash and cash equivalents | R188-R189 | 2 | -
G040 | SA BS | p4 | L216 | (iv) Other financial assets (current) | R190-R191 | 2 | -
G041 | SA BS | p4 | L217 | (b) Other current assets | R192-R193 | 2 | -
G042 | SA BS | p4 | L218 | Total current assets | R194-R195 | 2 | -
G043 | SA BS | p4 | L219 | Total assets | R196-R197 | 2 | -
G044 | SA BS | p4 | L222 | (a) Equity share capital | R198-R199 | 2 | -
G045 | SA BS | p4 | L223 | (b) Other equity | R200-R201 | 2 | -
G046 | SA BS | p4 | L224 | Total equity | R202-R203 | 2 | -
G047 | SA BS | p4 | L227 | (i) Borrowings (non-current) | R204-R205 | 2 | -
G048 | SA BS | p4 | L228 | (ii) Lease liabilities (non-current) | R206-R207 | 2 | -
G049 | SA BS | p4 | L229 | (iii) Other financial liabilities (non-current) | R208-R209 | 2 | -
G050 | SA BS | p4 | L230 | (b) Provisions (non-current) | R210-R211 | 2 | -
G051 | SA BS | p4 | L231 | (c) Other non-current liabilities | R212-R213 | 2 | -
G052 | SA BS | p4 | L232 | Total non-current liabilities | R214-R215 | 2 | -
G053 | SA BS | p4 | L235 | (i) Borrowings (current) | R216-R217 | 2 | -
G054 | SA BS | p4 | L236 | (ii) Lease liabilities (current) | R218-R219 | 2 | -
G055 | SA BS | p4 | L238 | -Total outstanding dues of micro enterprises and small enterprises | R220-R221 | 2 | -
G056 | SA BS | p4 | L239 | -Total outstanding dues of creditors other than micro enterprises and small enterprises | R222-R223 | 2 | -
G057 | SA BS | p4 | L240 | (iv) Other financial liabilities (current) | R224-R225 | 2 | -
G058 | SA BS | p4 | L241 | (b) Other current liabilities | R226-R227 | 2 | -
G059 | SA BS | p4 | L242 | (c) Provisions (current) | R228-R229 | 2 | -
G060 | SA BS | p4 | L243 | Total current liabilities | R230-R231 | 2 | -
G061 | SA BS | p4 | L244 | Total equity and liabilities | R232-R233 | 2 | -
G062 | SA CF | p5 | L254 | Profit/(loss) before tax and after exceptional item | R234-R235 | 2 | -
G063 | SA CF | p5 | L256 | Depreciation and amortisation expense | R236-R237 | 2 | -
G064 | SA CF | p5 | L257 | Share based payment expense | R238-R239 | 2 | -
G065 | SA CF | p5 | L258 | Provision for doubtful debts (net of reversals) | R240-R241 | 2 | -
G066 | SA CF | p5 | L259 | Liability written back | R242-R243 | 2 | ZERO_STANDING(1 of 2 cols nil)
G067 | SA CF | p5 | L260 | Profit on sale of investments in mutual funds (net) | R244-R245 | 2 | ZERO_STANDING(1 of 2 cols nil)
G068 | SA CF | p5 | L261 | Gain on financial instruments at fair value through profit and loss | R246-R247 | 2 | -
G069 | SA CF | p5 | L262 | (Profit)/Loss on sale of property plant and equipment (net) | R248-R249 | 2 | -
G070 | SA CF | p5 | L263 | Finance income | R250-R251 | 2 | -
G071 | SA CF | p5 | L264 | Gain on termination of security deposits | R252-R253 | 2 | ZERO_STANDING(1 of 2 cols nil)
G072 | SA CF | p5 | L265 | Gain on termination/modification of lease (net) | R254-R255 | 2 | ZERO_STANDING(1 of 2 cols nil)
G073 | SA CF | p5 | L266 | Finance costs | R256-R257 | 2 | -
G074 | SA CF | p5 | L267 | Operating profit before working capital changes | R258-R259 | 2 | -
G075 | SA CF | p5 | L269 | Decrease/(Increase) in trade receivables | R260-R261 | 2 | -
G076 | SA CF | p5 | L270 | Decrease/(Increase) in other assets | R262-R263 | 2 | -
G077 | SA CF | p5 | L271 | Decrease/(Increase) in other financial assets | R264-R265 | 2 | -
G078 | SA CF | p5 | L272 | Increase/(Decrease) in trade payables | R266-R267 | 2 | -
G079 | SA CF | p5 | L273 | Increase/(Decrease) in provisions | R268-R269 | 2 | -
G080 | SA CF | p5 | L274 | Increase/(Decrease) in other liabilities | R270-R271 | 2 | -
G081 | SA CF | p5 | L275 | Increase/(Decrease) in other financial liabilities | R272-R273 | 2 | -
G082 | SA CF | p5 | L276 | Cash generated from operations | R274-R275 | 2 | -
G083 | SA CF | p5 | L277 | Income taxes refunded/(paid) (net) | R276-R277 | 2 | -
G084 | SA CF | p5 | L278 | Net cash generated from operating activities (A) | R278-R279 | 2 | -
G085 | SA CF | p5 | L280 | Acquisition of property, plant and equipment and intangible assets | R280-R281 | 2 | -
G086 | SA CF | p5 | L281 | Proceeds from sale of property, plant and equipment | R282-R283 | 2 | -
G087 | SA CF | p5 | L282 | Payment towards additions to right-of-use asset | R284-R285 | 2 | -
G088 | SA CF | p5 | L283 | (Investment)/Redemption made in bank deposits | R286-R287 | 2 | -
G089 | SA CF | p5 | L284 | Proceeds from sale of current investment/(Purchase of current investments) (net) | R288-R289 | 2 | ZERO_STANDING(1 of 2 cols nil)
G090 | SA CF | p5 | L285 | Interest received | R290-R291 | 2 | -
G091 | SA CF | p5 | L286 | Net cash used in investing activities (B) | R292-R293 | 2 | -
G092 | SA CF | p5 | L288 | Proceeds from borrowings | R294-R295 | 2 | -
G093 | SA CF | p5 | L289 | Repayment of borrowings | R296-R297 | 2 | -
G094 | SA CF | p5 | L290 | Proceeds from exercise of employee stock options | R298-R299 | 2 | ZERO_STANDING(1 of 2 cols nil)
G095 | SA CF | p5 | L291 | Interest, bank charges and processing charges paid | R300-R301 | 2 | -
G096 | SA CF | p5 | L292 | Interest paid on vehicle loan | R302-R303 | 2 | -
G097 | SA CF | p5 | L293 | Payment of principal portion of lease liabilities | R304-R305 | 2 | -
G098 | SA CF | p5 | L294 | Interest paid on lease liabilities | R306-R307 | 2 | -
G099 | SA CF | p5 | L295 | Net cash used in financing activities (C) | R308-R309 | 2 | -
G100 | SA CF | p5 | L296 | Net increase/(decrease) in cash and cash equivalents (A+B+C) | R310-R311 | 2 | -
G101 | SA CF | p5 | L297 | Cash and cash equivalents at the beginning of the period | R312-R313 | 2 | -
G102 | SA CF | p5 | L298 | Cash and cash equivalents at the end of the period | R314-R315 | 2 | -
G103 | SA CF | p5 | L301 | - in current accounts | R316-R317 | 2 | ZERO_STANDING(1 of 2 cols nil)
G104 | SA CF | p5 | L302 | - in escrow accounts | R318-R319 | 2 | -
G105 | SA CF | p5 | L303 | Cash and cash equivalents at the end of the period (break-up total) | R320-R321 | 2 | -
G106 | CA P&L | p9 | L486 | Revenue from operations | R363-R368 | 6 | -
G107 | CA P&L | p9 | L487 | Other income | R369-R374 | 6 | -
G108 | CA P&L | p9 | L488 | Finance income | R375-R380 | 6 | -
G109 | CA P&L | p9 | L489 | Total income | R381-R386 | 6 | -
G110 | CA P&L | p9 | L491 | Sub-contracting cost | R387-R392 | 6 | ZERO_STANDING(2 of 6 cols nil)
G111 | CA P&L | p9 | L492 | Cost of materials consumed | R393-R398 | 6 | -
G112 | CA P&L | p9 | L493 | Employee benefits expense | R399-R404 | 6 | -
G113 | CA P&L | p9 | L494 | Finance costs | R405-R410 | 6 | -
G114 | CA P&L | p9 | L495 | Depreciation and amortisation expense | R411-R416 | 6 | -
G115 | CA P&L | p9 | L496 | Operating expenses | R417-R422 | 6 | -
G116 | CA P&L | p9 | L497 | Other expenses | R423-R428 | 6 | -
G117 | CA P&L | p9 | L498 | Total expenses | R429-R434 | 6 | -
G118 | CA P&L | p9 | L499 | SI No. 3 Profit/(Loss) before share of profit/(loss) in associate, exceptional item and tax for the period/year (1-2) | R435-R440 | 6 | -
G119 | CA P&L | p9 | L500 | SI No. 4 Share of profit/(loss) in associate | R441-R446 | 6 | -
G120 | CA P&L | p9 | L501 | SI No. 5 Profit/(Loss) before exceptional item and tax for the period/year (3+4) | R447-R452 | 6 | -
G121 | CA P&L | p9 | L502 | SI No. 6 Exceptional item (Refer Note 5) | R453-R458 | 6 | ZERO_STANDING(5 of 6 cols nil)
G122 | CA P&L | p9 | L503 | SI No. 7 Profit/(Loss) before tax for the period/year (5+6) | R459-R464 | 6 | -
G123 | CA P&L | p9 | L505 | Current tax charge | R465-R470 | 6 | -
G124 | CA P&L | p9 | L506 | Deferred tax (credit)/charge | R471-R476 | 6 | -
G125 | CA P&L | p9 | L507 | Total tax expense/(credit) | R477-R482 | 6 | -
G126 | CA P&L | p9 | L508 | SI No. 9 Profit/(Loss) for the period/year (7-8) | R483-R488 | 6 | -
G127 | CA P&L | p9 | L511 | Re-measurement (loss)/gain on defined benefit plans | R489-R494 | 6 | -
G128 | CA P&L | p9 | L512 | Income tax effect on above credit/(charge) | R495-R500 | 6 | ZERO_STANDING(1 of 6 cols nil)
G129 | CA P&L | p9 | L513 | Share of other comprehensive income/loss of an associate | R501-R506 | 6 | -
G130 | CA P&L | p9 | L514 | OCI for the period/year (net of tax) | R507-R512 | 6 | -
G131 | CA P&L | p9 | L515 | SI No. 11 Total comprehensive Income/(Loss) for the period/year (9+10) | R513-R518 | 6 | -
G132 | CA P&L | p9 | L517 | Owners of the Parent | R519-R524 | 6 | -
G133 | CA P&L | p9 | L518 | Non-controlling interests | R525-R530 | 6 | -
G134 | CA P&L | p9 | L520 | Owners of the Parent (OCI) | R531-R536 | 6 | -
G135 | CA P&L | p9 | L521 | Non-controlling interests (OCI) | R537-R542 | 6 | -
G136 | CA P&L | p9 | L523 | Owners of the Parent (TCI) | R543-R548 | 6 | -
G137 | CA P&L | p9 | L524 | Non-controlling interests (TCI) | R549-R554 | 6 | -
G138 | CA P&L | p9 | L525 | SI No. 15 Paid up Equity Share Capital (Face Value Rs.10/- per share) | R555-R560 | 6 | -
G139 | CA P&L | p9 | L527 | Basic (Rs. per share) | R563-R568 | 6 | -
G140 | CA P&L | p9 | L528 | Diluted (Rs. per share) | R569-R574 | 6 | -
G141 | CA BS | p10 | L540 | (a) Property, plant and equipment | R575-R576 | 2 | -
G142 | CA BS | p10 | L541 | (b) Capital work-in-progress | R577-R578 | 2 | -
G143 | CA BS | p10 | L542 | (c) Right-of-use assets | R579-R580 | 2 | -
G144 | CA BS | p10 | L543 | (d) Goodwill | R581-R582 | 2 | -
G145 | CA BS | p10 | L544 | (e) Other intangible assets | R583-R584 | 2 | -
G146 | CA BS | p10 | L545 | (f) Intangible assets under development | R585-R586 | 2 | ZERO_STANDING(1 of 2 cols nil)
G147 | CA BS | p10 | L546 | (g) Investments accounted for using equity method | R587-R588 | 2 | -
G148 | CA BS | p10 | L548 | (i) Investments (non-current) | R589-R590 | 2 | -
G149 | CA BS | p10 | L549 | (ii) Other financial assets (non-current) | R591-R592 | 2 | -
G150 | CA BS | p10 | L550 | (i) Deferred tax assets (net) | R593-R594 | 2 | -
G151 | CA BS | p10 | L551 | (j) Income tax assets (net) | R595-R596 | 2 | -
G152 | CA BS | p10 | L552 | (k) Other non-current assets | R597-R598 | 2 | -
G153 | CA BS | p10 | L553 | Total non-current assets | R599-R600 | 2 | -
G154 | CA BS | p10 | L555 | (a) Inventories | R601-R602 | 2 | -
G155 | CA BS | p10 | L557 | (i) Investments (current) | R603-R604 | 2 | -
G156 | CA BS | p10 | L558 | (ii) Trade receivables | R605-R606 | 2 | -
G157 | CA BS | p10 | L559 | (iii) Cash and cash equivalents | R607-R608 | 2 | -
G158 | CA BS | p10 | L560 | (iv) Bank balances other than cash and cash equivalents | R609-R610 | 2 | -
G159 | CA BS | p10 | L561 | (v) Other financial assets (current) | R611-R612 | 2 | -
G160 | CA BS | p10 | L562 | (c) Other current assets | R613-R614 | 2 | -
G161 | CA BS | p10 | L563 | Total current assets | R615-R616 | 2 | -
G162 | CA BS | p10 | L564 | Total assets | R617-R618 | 2 | -
G163 | CA BS | p10 | L567 | (a) Equity share capital | R619-R620 | 2 | -
G164 | CA BS | p10 | L568 | (b) Other equity | R621-R622 | 2 | -
G165 | CA BS | p10 | L569 | Equity attributable to owners of the parent | R623-R624 | 2 | -
G166 | CA BS | p10 | L570 | Non-controlling interest | R625-R626 | 2 | -
G167 | CA BS | p10 | L571 | Total equity | R627-R628 | 2 | -
G168 | CA BS | p10 | L574 | (i) Borrowings (non-current) | R629-R630 | 2 | -
G169 | CA BS | p10 | L575 | (ii) Lease liabilities (non-current) | R631-R632 | 2 | -
G170 | CA BS | p10 | L576 | (iii) Other financial liabilities (non-current) | R633-R634 | 2 | -
G171 | CA BS | p10 | L577 | (b) Provisions (non-current) | R635-R636 | 2 | -
G172 | CA BS | p10 | L578 | (c) Other non-current liabilities | R637-R638 | 2 | -
G173 | CA BS | p10 | L579 | Total non-current liabilities | R639-R640 | 2 | -
G174 | CA BS | p10 | L582 | (i) Borrowings (current) | R641-R642 | 2 | -
G175 | CA BS | p10 | L583 | (ii) Lease liabilities (current) | R643-R644 | 2 | -
G176 | CA BS | p10 | L585 | Total outstanding dues of micro enterprises and small enterprises | R645-R646 | 2 | -
G177 | CA BS | p10 | L586 | Total outstanding dues of creditors other than micro enterprises and small enterprises | R647-R648 | 2 | -
G178 | CA BS | p10 | L587 | (iv) Other current financial liabilities | R649-R650 | 2 | -
G179 | CA BS | p10 | L588 | (b) Other current liabilities | R651-R652 | 2 | -
G180 | CA BS | p10 | L589 | (c) Provisions (current) | R653-R654 | 2 | -
G181 | CA BS | p10 | L590 | (d) Current tax liabilities (net) | R655-R656 | 2 | -
G182 | CA BS | p10 | L591 | Total current liabilities | R657-R658 | 2 | -
G183 | CA BS | p10 | L592 | Total equity and liabilities | R659-R660 | 2 | -
G184 | CA CF | p11 | L602 | Profit/(Loss) before tax and share of Profit/(Loss) in associate and after exceptional item | R661-R662 | 2 | -
G185 | CA CF | p11 | L604 | Depreciation and amortisation expense | R663-R664 | 2 | -
G186 | CA CF | p11 | L605 | Share based payment expense | R665-R666 | 2 | -
G187 | CA CF | p11 | L606 | Provision for doubtful debts (net of reversals) | R667-R668 | 2 | -
G188 | CA CF | p11 | L607 | Liability written back | R669-R670 | 2 | ZERO_STANDING(1 of 2 cols nil)
G189 | CA CF | p11 | L608 | Profit on sale of investments in mutual funds (net) | R671-R672 | 2 | ZERO_STANDING(1 of 2 cols nil)
G190 | CA CF | p11 | L609 | Gain on financial instruments at fair value through profit and loss | R673-R674 | 2 | -
G191 | CA CF | p11 | L610 | (Profit)/Loss on sale of property, plant and equipment (net) | R675-R676 | 2 | -
G192 | CA CF | p11 | L611 | Finance income | R677-R678 | 2 | -
G193 | CA CF | p11 | L612 | Gain on termination of Security deposits | R679-R680 | 2 | ZERO_STANDING(1 of 2 cols nil)
G194 | CA CF | p11 | L613 | Gain on termination of lease (net) | R681-R682 | 2 | ZERO_STANDING(1 of 2 cols nil)
G195 | CA CF | p11 | L614 | Finance costs | R683-R684 | 2 | -
G196 | CA CF | p11 | L615 | Operating profit before working capital changes | R685-R686 | 2 | -
G197 | CA CF | p11 | L617 | Decrease/(Increase) in inventories | R687-R688 | 2 | -
G198 | CA CF | p11 | L618 | Decrease/(Increase) in trade receivables | R689-R690 | 2 | -
G199 | CA CF | p11 | L619 | Decrease/(Increase) in other assets | R691-R692 | 2 | -
G200 | CA CF | p11 | L620 | Decrease/(Increase) in other financial assets | R693-R694 | 2 | -
G201 | CA CF | p11 | L621 | (Decrease)/Increase in trade payables | R695-R696 | 2 | -
G202 | CA CF | p11 | L622 | (Decrease)/Increase in provisions | R697-R698 | 2 | -
G203 | CA CF | p11 | L623 | (Decrease)/Increase in other liabilities | R699-R700 | 2 | -
G204 | CA CF | p11 | L624 | (Decrease)/Increase in other financial liabilities | R701-R702 | 2 | -
G205 | CA CF | p11 | L625 | Cash generated from operations | R703-R704 | 2 | -
G206 | CA CF | p11 | L626 | Income taxes refunded/(paid) (net) | R705-R706 | 2 | -
G207 | CA CF | p11 | L627 | Net cash generated from operating activities (A) | R707-R708 | 2 | -
G208 | CA CF | p11 | L629 | Acquisition of property, plant and equipment and intangible assets | R709-R710 | 2 | -
G209 | CA CF | p11 | L630 | Proceeds from sale of property, plant and equipment | R711-R712 | 2 | -
G210 | CA CF | p11 | L631 | Payment towards additions to right-of-use assets | R713-R714 | 2 | -
G211 | CA CF | p11 | L632 | (Investment)/Redemption made in bank deposits | R715-R716 | 2 | -
G212 | CA CF | p11 | L633 | Proceeds from sale of current investment/(Purchase of current investments) (net) | R717-R718 | 2 | ZERO_STANDING(1 of 2 cols nil)
G213 | CA CF | p11 | L634 | Purchase of non-current investments | R719-R720 | 2 | ZERO_STANDING(1 of 2 cols nil)
G214 | CA CF | p11 | L635 | Interest received | R721-R722 | 2 | -
G215 | CA CF | p11 | L636 | Net cash used in investing activities (B) | R723-R724 | 2 | -
G216 | CA CF | p11 | L638 | Proceeds from long-term borrowings | R725-R726 | 2 | -
G217 | CA CF | p11 | L639 | Repayment of long-term borrowings | R727-R728 | 2 | -
G218 | CA CF | p11 | L640 | Proceeds from exercise of employee stock options | R729-R730 | 2 | ZERO_STANDING(1 of 2 cols nil)
G219 | CA CF | p11 | L641 | Interest, bank charges and processing charges paid on borrowings | R731-R732 | 2 | -
G220 | CA CF | p11 | L642 | Interest paid on vehicle loan | R733-R734 | 2 | -
G221 | CA CF | p11 | L643 | Payment of principal portion of lease liabilities | R735-R736 | 2 | -
G222 | CA CF | p11 | L644 | Interest paid on lease liabilities | R737-R738 | 2 | -
G223 | CA CF | p11 | L645 | Net cash used in financing activities (C) | R739-R740 | 2 | -
G224 | CA CF | p11 | L646 | Net decrease in cash and cash equivalents (A+B+C) | R741-R742 | 2 | -
G225 | CA CF | p11 | L647 | Cash and cash equivalents at the beginning of the period | R743-R744 | 2 | -
G226 | CA CF | p11 | L648 | Cash and cash equivalents at the end of the period | R745-R746 | 2 | -
G227 | CA CF | p11 | L651 | - in current accounts | R747-R748 | 2 | -
G228 | CA CF | p11 | L652 | - in escrow accounts | R749-R750 | 2 | -
G229 | CA CF | p11 | L653 | Cash and cash equivalents at the end of the period (break-up total) | R751-R752 | 2 | -
G230 | SA P&L extract (Note 11) | p12 | L709 | Note 11 standalone Revenue from operations | R775-R780 | 6 | RESTATED of page 3 line items
G231 | SA P&L extract (Note 11) | p12 | L710 | Note 11 standalone Profit/(Loss) before tax for the period/year | R781-R786 | 6 | RESTATED of page 3 line items
G232 | SA P&L extract (Note 11) | p12 | L711 | Note 11 standalone Profit/(Loss) for the period/year | R787-R792 | 6 | RESTATED of page 3 line items

Zero/nil/dash standing cells (rule 3), every nil cell:
ROW_ID | category | A2 flags | note
R035 | line_item nil cell | ZERO_STANDING | SA P&L p3 L163 Sub-contracting cost
R036 | line_item nil cell | ZERO_STANDING | SA P&L p3 L163 Sub-contracting cost
R082 | line_item nil cell | ZERO_STANDING | SA P&L p3 L171 SI No. 4 Exceptional item (Refer Note 5)
R083 | line_item nil cell | ZERO_STANDING | SA P&L p3 L171 SI No. 4 Exceptional item (Refer Note 5)
R084 | line_item nil cell | ZERO_STANDING | SA P&L p3 L171 SI No. 4 Exceptional item (Refer Note 5)
R085 | line_item nil cell | ZERO_STANDING | SA P&L p3 L171 SI No. 4 Exceptional item (Refer Note 5)
R086 | line_item nil cell | ZERO_STANDING | SA P&L p3 L171 SI No. 4 Exceptional item (Refer Note 5)
R094 | line_item nil cell | ZERO_STANDING | SA P&L p3 L174 Current tax charge
R095 | line_item nil cell | ZERO_STANDING | SA P&L p3 L174 Current tax charge
R096 | line_item nil cell | ZERO_STANDING | SA P&L p3 L174 Current tax charge
R097 | line_item nil cell | ZERO_STANDING | SA P&L p3 L174 Current tax charge
R098 | line_item nil cell | ZERO_STANDING | SA P&L p3 L174 Current tax charge
R099 | line_item nil cell | ZERO_STANDING | SA P&L p3 L174 Current tax charge
R100 | line_item nil cell | ZERO_STANDING | SA P&L p3 L175 Deferred tax (credit)/charge
R101 | line_item nil cell | ZERO_STANDING | SA P&L p3 L175 Deferred tax (credit)/charge
R102 | line_item nil cell | ZERO_STANDING | SA P&L p3 L175 Deferred tax (credit)/charge
R103 | line_item nil cell | ZERO_STANDING | SA P&L p3 L175 Deferred tax (credit)/charge
R104 | line_item nil cell | ZERO_STANDING | SA P&L p3 L175 Deferred tax (credit)/charge
R106 | line_item nil cell | ZERO_STANDING | SA P&L p3 L176 Total tax expense
R107 | line_item nil cell | ZERO_STANDING | SA P&L p3 L176 Total tax expense
R108 | line_item nil cell | ZERO_STANDING | SA P&L p3 L176 Total tax expense
R109 | line_item nil cell | ZERO_STANDING | SA P&L p3 L176 Total tax expense
R110 | line_item nil cell | ZERO_STANDING | SA P&L p3 L176 Total tax expense
R124 | line_item nil cell | ZERO_STANDING | SA P&L p3 L181 Income tax effect on above credit/(charge)
R125 | line_item nil cell | ZERO_STANDING | SA P&L p3 L181 Income tax effect on above credit/(charge)
R127 | line_item nil cell | ZERO_STANDING | SA P&L p3 L181 Income tax effect on above credit/(charge)
R128 | line_item nil cell | ZERO_STANDING | SA P&L p3 L181 Income tax effect on above credit/(charge)
R129 | line_item nil cell | ZERO_STANDING | SA P&L p3 L181 Income tax effect on above credit/(charge)
R171 | line_item nil cell | ZERO_STANDING | SA BS p4 L203 (e) Intangible assets under development
R243 | line_item nil cell | ZERO_STANDING | SA CF p5 L259 Liability written back
R245 | line_item nil cell | ZERO_STANDING | SA CF p5 L260 Profit on sale of investments in mutual funds (net)
R253 | line_item nil cell | ZERO_STANDING | SA CF p5 L264 Gain on termination of security deposits
R255 | line_item nil cell | ZERO_STANDING | SA CF p5 L265 Gain on termination/modification of lease (net)
R289 | line_item nil cell | ZERO_STANDING | SA CF p5 L284 Proceeds from sale of current investment/(Purchase of current investments) (net)
R299 | line_item nil cell | ZERO_STANDING | SA CF p5 L290 Proceeds from exercise of employee stock options
R316 | line_item nil cell | ZERO_STANDING | SA CF p5 L301 - in current accounts
R388 | line_item nil cell | ZERO_STANDING | CA P&L p9 L491 Sub-contracting cost
R389 | line_item nil cell | ZERO_STANDING | CA P&L p9 L491 Sub-contracting cost
R453 | line_item nil cell | ZERO_STANDING | CA P&L p9 L502 SI No. 6 Exceptional item (Refer Note 5)
R454 | line_item nil cell | ZERO_STANDING | CA P&L p9 L502 SI No. 6 Exceptional item (Refer Note 5)
R455 | line_item nil cell | ZERO_STANDING | CA P&L p9 L502 SI No. 6 Exceptional item (Refer Note 5)
R456 | line_item nil cell | ZERO_STANDING | CA P&L p9 L502 SI No. 6 Exceptional item (Refer Note 5)
R457 | line_item nil cell | ZERO_STANDING | CA P&L p9 L502 SI No. 6 Exceptional item (Refer Note 5)
R499 | line_item nil cell | ZERO_STANDING | CA P&L p9 L512 Income tax effect on above credit/(charge)
R586 | line_item nil cell | ZERO_STANDING | CA BS p10 L545 (f) Intangible assets under development
R670 | line_item nil cell | ZERO_STANDING | CA CF p11 L607 Liability written back
R672 | line_item nil cell | ZERO_STANDING | CA CF p11 L608 Profit on sale of investments in mutual funds (net)
R680 | line_item nil cell | ZERO_STANDING | CA CF p11 L612 Gain on termination of Security deposits
R682 | line_item nil cell | ZERO_STANDING | CA CF p11 L613 Gain on termination of lease (net)
R718 | line_item nil cell | ZERO_STANDING | CA CF p11 L633 Proceeds from sale of current investment/(Purchase of current investments) (net)
R719 | line_item nil cell | ZERO_STANDING | CA CF p11 L634 Purchase of non-current investments
R730 | line_item nil cell | ZERO_STANDING | CA CF p11 L640 Proceeds from exercise of employee stock options

Statement apparatus (period headers, audit-status tags, units, tie-outs, extractor notes) by statement page:
ROW_ID range | category | A2 flags | note
R793 | NUMBER (1) | - | SA P&L extract (Note 11) p12
R858-R860 | CIN / identity (3) | - | SA P&L extract (Note 11) p12
R938 | period/column date header (1) | - | SA P&L extract (Note 11) p12
R815 | CIN / identity (1) | - | SA P&L p3
R881-R887 | period/column date header (7) | - | SA P&L p3
R953 | extractor note (transcribed from image) (1) | - | SA P&L p3
R954,R956-R961 | audit-status tag / unit / title qualifier (7) | - | SA P&L p3
R962-R965,R967-R969,R971-R972 | tie-out PASS (extractor) (9) | - | SA P&L p3
R847 | CIN / identity (1) | - | CA P&L p9
R910-R916 | period/column date header (7) | - | CA P&L p9
R1032 | extractor note (transcribed from image) (1) | - | CA P&L p9
R1033-R1040,R1045 | audit-status tag / unit / title qualifier (9) | - | CA P&L p9
R1041-R1044,R1046,R1048-R1050,R1052-R1056 | tie-out PASS (extractor) (13) | - | CA P&L p9
R888-R890 | period/column date header (3) | - | SA BS p4
R974 | extractor note (transcribed from image) (1) | - | SA BS p4
R976-R978 | audit-status tag / unit / title qualifier (3) | - | SA BS p4
R979-R986 | tie-out PASS (extractor) (8) | - | SA BS p4
R891-R894 | period/column date header (4) | - | SA CF p5
R987 | extractor note (transcribed from image) (1) | - | SA CF p5
R989-R991 | audit-status tag / unit / title qualifier (3) | - | SA CF p5
R992-R1002,R1004 | tie-out PASS (extractor) (12) | - | SA CF p5
R917-R919 | period/column date header (3) | - | CA BS p10
R1058 | extractor note (transcribed from image) (1) | - | CA BS p10
R1060-R1062 | audit-status tag / unit / title qualifier (3) | - | CA BS p10
R1063-R1071 | tie-out PASS (extractor) (9) | - | CA BS p10
R920-R923 | period/column date header (4) | - | CA CF p11
R1072 | extractor note (transcribed from image) (1) | - | CA CF p11
R1074-R1076 | audit-status tag / unit / title qualifier (3) | - | CA CF p11
R1077-R1087,R1089 | tie-out PASS (extractor) (12) | - | CA CF p11

## C. AGENDA ITEMS AND BOARD OUTCOME LETTER (page 1)
Board meeting 26-Oct-2026: start 19:15 IST (R874), end 20:50 IST (R875), 95 minutes; signature 20:57:42 IST (R877) is 7 minutes after conclusion (no flag).
Item | ROW IDs | category | A2 flags | note
Agenda 1: Unaudited Standalone and Consolidated Results, quarter/half year ended 30-Sep-2026 | R939,R940,R871,R872,R870,R802 | agenda_item | - | Annexure A enclosure R943; limited review not audit
Agenda 2: Final approval, 10 MWp captive solar plant, Karnataka, est. cost 34.25 crore (earlier in-principle 3-Sep-2026) | R003,R004,R803,R861,R862,R863,R873,R941,R942 | agenda_item | UNIT_CRORE_AS_PRINTED_NOT_MILLION | Only non-results item; forward capex; no completion date stated; 34.25 crore = 342.5 Mn; mixed-unit hazard vs Rs Million statements. Only 2 agenda items: no dividend, AGM, record date, director, auditor, ESOP or enabling-resolution item (absence recorded)
Meeting timing | R874,R875 | board_time | - | 95-minute meeting
Letter header, addressees, identifiers | R001,R002,R794,R795,R796,R797,R798,R799,R800,R801,R005,R804,R876,R877 | letter_admin | - | registrant, exchanges, scrip code, CS signature (see F)

## D. AUDITOR REPORT PARAGRAPHS (pages 2, 7, 8)
Opinion type: limited review, unmodified conclusion, no Emphasis of Matter, no Going Concern language in the structured rows. Both reports S.R. Batliboi & Associates LLP.
Para | page | ROW IDs | category | A2 flags | note
SA title | p2 | R944 | auditor_para | - | 
SA Para 1 scope | p2 | R945,R878,R879 | auditor_para | - | 
SA Para 2 responsibilities | p2 | R946,R808,R809 | auditor_para | - | 
SA Para 3 SRE 2410 moderate assurance, review limitation, no audit opinion | p2 | R947,R948,R949,R950,R810 | auditor_para | - | 
SA Para 4 unmodified conclusion | p2 | R951,R952 | auditor_para | FOOTNOTE_UNRESOLVED | UDIN illegible (R952)
CA title | p7 | R1016 | auditor_para | - | 
CA Para 1 scope | p7 | R1017,R903,R904 | auditor_para | - | 
CA Para 2 responsibilities | p7 | R1018 | auditor_para | - | 
CA Para 3 SRE 2410, SEBI Master Circular 33(8) procedures | p7 | R1019,R1020,R1021,R1022,R1023,R831,R832 | auditor_para | - | 
CA Para 4 entity list lead-in | p7 | R1024,R833,R834,R835,R836,R837,R838,R839 | auditor_para | - | consolidation list: 1 holding, 2 subsidiaries, 1 associate
CA Para 5 unmodified conclusion based on other auditors | p8 | R1025 | auditor_para | - | 
CA Para 6 Other Matters (2 subsidiaries + 1 associate reviewed by other auditors) | p8 | R1026,R1027,R1028,R1029,R1030,R842,R843,R905,R906,R907,R908,R347,R348,R349,R350,R351,R352,R353,R354,R355,R356,R357,R358,R359,R360 | auditor_para | RELIANCE_ON_OTHER_AUDITORS | subsidiary and associate figures not reviewed by SRBC; review reports furnished by management; not-modified language R1030
Auditor paragraphs: SA paras 1-4 (4), CA paras 1-6 (6) = 10; plus titles. UDINs: SA R952, CA R1031, both FOOTNOTE_UNRESOLVED_OCR_ILLEGIBLE. Signing partners: SA Nikunj Jay (R812, membership R008); CA partner name partial R845 (OCR_PARTIAL), membership R362. R008 and R362 carry the same membership number against two different printed partner names: VERIFY (flag MEMBERSHIP_NO_NAME_MISMATCH; may be the OCR-partial name).

## E. ENTITIES (all ENTITY rows)
ROW_ID | category | A2 flags | note
R794 | entity (p1) | - | 
R795 | entity (p1) | - | 
R796 | entity (p1) | - | 
R797 | entity (p1) | - | 
R798 | entity (p1) | - | 
R799 | entity (p1) | - | 
R800 | entity (p1) | - | 
R801 | entity (p1) | - | 
R802 | entity (p1) | - | 
R803 | entity (p1) | - | 
R804 | entity (p1) | - | 
R805 | entity (p2) | - | 
R806 | entity (p2) | - | 
R807 | entity (p2) | - | 
R808 | entity (p2) | - | 
R809 | entity (p2) | - | 
R810 | entity (p2) | - | 
R811 | entity (p2) | - | 
R812 | entity (p2) | - | 
R813 | entity (p2) | - | 
R814 | entity (p2) | - | 
R815 | entity (p3) | - | 
R816 | entity (p6) | - | 
R817 | entity (p6) | - | 
R818 | entity (p6) | - | 
R819 | entity (p6) | - | 
R820 | entity (p6) | - | 
R821 | entity (p6) | - | 
R822 | entity (p6) | - | 
R823 | entity (p6) | - | 
R824 | entity (p6) | - | 
R825 | entity (p6) | - | 
R826 | entity (p6) | - | 
R827 | entity (p6) | - | 
R828 | entity (p6) | - | 
R829 | entity (p7) | - | 
R830 | entity (p7) | - | 
R831 | entity (p7) | - | 
R832 | entity (p7) | - | 
R833 | entity (p7) | - | consolidation: holding company category A
R834 | entity (p7) | - | consolidation: holding (WeWork India Management Ltd)
R835 | entity (p7) | - | consolidation: subsidiaries category B header
R836 | entity (p7) | NO_PRIOR_LIST (ENTITY_CHANGE not testable) | consolidation: subsidiary 1
R837 | entity (p7) | NO_PRIOR_LIST (ENTITY_CHANGE not testable) | consolidation: subsidiary 2
R838 | entity (p7) | - | consolidation: associate category C header
R839 | entity (p7) | NO_PRIOR_LIST (ENTITY_CHANGE not testable) | consolidation: associate
R840 | entity (p7) | - | 
R841 | entity (p8) | - | 
R842 | entity (p8) | - | 
R843 | entity (p8) | - | 
R844 | entity (p8) | - | 
R845 | entity (p8) | OCR_PARTIAL | 
R846 | entity (p8) | - | 
R847 | entity (p9) | - | 
R848 | entity (p12) | - | 
R849 | entity (p12) | - | 
R850 | entity (p12) | - | 
R851 | entity (p12) | - | 
R852 | entity (p12) | - | 
R853 | entity (p12) | - | 
R854 | entity (p12) | - | 
R855 | entity (p12) | - | 
R856 | entity (p12) | - | 
R857 | entity (p12) | - | 
R858 | entity (p12) | - | 
R859 | entity (p12) | - | 
R860 | entity (p12) | - | 
Consolidation list: 4 entities (1 holding; subsidiaries WW Tech Solutions India Pvt Ltd and Zoapi Innovations Pvt Ltd; associate MyHQ Anarock Pvt Ltd). Prior list not supplied.

## F. SIGNATURE BLOCKS
Block | ROW IDs | note
Board outcome letter, CS Udayan Shukla, 26-Oct-2026 20:57:42 IST | R804,R005,R876,R877 | after meeting end 20:50, no flag
SA review report, S.R. Batliboi, partner Nikunj Jay, Bengaluru, 26-Oct-2026 | R811,R812,R813,R880,R007,R008,R009 | UDIN R952 illegible
SA results, MD and CEO Karan Virwani, Bengaluru, 26-Oct-2026 | R826,R827,R828,R902,R344 | 
CA review report, S.R. Batliboi, partner partial name, Bengaluru, 26-Oct-2026 | R844,R845,R846,R909,R361,R362 | UDIN R1031 illegible; OCR_PARTIAL name
CA results, MD and CEO Karan Virwani, Bengaluru, 26-Oct-2026 | R858,R859,R860,R924,R938,R793 | 

## G. FORWARD-LOOKING ROWS AND REMAINING IDS BY TYPE
ROW_ID | category | A2 flags | note
R861 | forward_looking (p1) | - | capex plan, solar
R862 | forward_looking (p1) | - | capex plan, solar
R863 | forward_looking (p1) | - | capex plan, solar
R864 | forward_looking (p6) | - | Labour Codes rules pending
R865 | forward_looking (p6) | - | NCLT capital reduction scheme pending
R866 | forward_looking (p6) | - | NCLT capital reduction scheme pending
R867 | forward_looking (p12) | - | Labour Codes rules pending
R868 | forward_looking (p12) | - | NCLT capital reduction scheme pending
R869 | forward_looking (p12) | - | NCLT capital reduction scheme pending
R006 | number p2 remaining (1) | - | dates / admin / identifiers not tied to a note or agenda line
R345-R346 | number p7 remaining (2) | - | dates / admin / identifiers not tied to a note or agenda line

## H. MISSING_FROM_STRUCTURED
none found. Gaps noted but not misses: consolidated Note 5 number absent in the fulltext text layer (A1 labelled it Note 5 from the image); two UDINs illegible; CA partner name partial.
