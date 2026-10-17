# A2 LEDGER: SUPREMEPWR results h1fy27 (Rs Lakhs; claim text stays in structured file at the row ID)

=== A2 COUNT TEST ===
category: notes            grep_count: 21   sweep_count: 21   match: yes   (SA notes 8 + CON notes 9 + CF notes 4; certificate notes R553/R554 and CON header R535 listed separately)
category: line_items       grep_count: 153   sweep_count: 153   match: yes   (SA P&L 22, SA BS 23, SA CF 30, CON P&L 25, CON BS 23, CON CF 30; plus MISSING rows in section 9: M12-M15 added in correction loop 1)
category: zero_standing    grep_count: 13   sweep_count: 13   match: yes   (structured line items with a dash value; plus 8 from MISSING rows)
category: agenda_items     grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras    grep_count: 9    sweep_count: 9    match: yes   (structured; plus M10, M11, M16, M17 MISSING)
category: entities         grep_count: 20   sweep_count: 20   match: yes   (structured; plus M18 Audit Committee MISSING)
category: forward          grep_count: 10   sweep_count: 10   match: yes
category: dates            grep_count: 35   sweep_count: 35   match: yes   (A1 structured rows. Loop 2 independent FULLTEXT sweep: 58 date-bearing lines excl. L15 metadata; structured anchors 26 of them; 26 genuine unanchored lines, 6 share-count false positives L15/201/575/910/911/1085; all 26 now in M19-M32 incl. signing dates L283,L339,L412,L649,L708,L1192; fulltext total = 35 + 14 M rows)
category: qualifiers       grep_count: 48   sweep_count: 48   match: yes   (A1 structured rows. Loop 2 FULLTEXT sweep of Unaudited/Audited/Notes/asterisk: 21 Unaudited/Audited lines, 6 Note lines, 1 asterisk (L863 stamp, non-qualifier); header lines L214,L349,L588,L725,L974 plus L516,L401 and prose L42,77,90,421,432,472,474,684,1034 not anchored, now M19-M22,M33-M35)
category: header_total     grep_count: 554  sweep_count: 554  match: yes   (441+20+10+35+48)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 554 | ids_referenced_in_ledger: 554 | orphan_ids: [] | match: yes | missing_from_structured: 35 (M01-M35; M19-M35 added in correction loop 2)

Prior ledger: none (ND). ENTITY_CHANGE cannot be tested.

## 1. LINE ITEMS (ID range = period columns of one line item)
range | table | A1 label | A2 flags | note
R003-R006 | SA P&L | Revenue from operations | - | 4 columns
R007-R010 | SA P&L | Other income | OCR_UNCERTAIN carried | 4 columns
R011-R014 | SA P&L | Total income | OCR_UNCERTAIN carried | 4 columns
R015-R018 | SA P&L | Purchases of stock in trade | - | 4 columns
R019-R022 | SA P&L | Changes in inventories | - | 4 columns
R023-R026 | SA P&L | Other direct expenses | - | 4 columns
R027-R030 | SA P&L | Employee benefits expenses | - | 4 columns
R031-R034 | SA P&L | Finance costs | - | 4 columns
R035-R038 | SA P&L | Depreciation and amortisation | - | 4 columns
R039-R042 | SA P&L | Other expenses | - | 4 columns
R043-R046 | SA P&L | Total expenses | OCR_UNCERTAIN carried | 4 columns
R047-R050 | SA P&L | Profit before exceptional and extraordinary items and tax | - | 4 columns
R051-R054 | SA P&L | Exceptional items | ZERO_STANDING(all periods) | 4 columns
R055-R058 | SA P&L | Profit before tax | - | 4 columns
R059-R062 | SA P&L | Current tax | - | 4 columns
R063-R066 | SA P&L | Deferred tax | OCR_UNCERTAIN carried | 4 columns
R067-R070 | SA P&L | Profit for the period (PAT) | - | 4 columns
R071-R074 | SA P&L | EPS basic Rs | - | 4 columns
R075-R078 | SA P&L | EPS diluted Rs | - | 4 columns
R079-R082 | SA P&L | Weighted average shares (basic) | - | 4 columns
R083-R086 | SA P&L | Weighted average shares (diluted) | - | 4 columns
R087-R090 | SA P&L | Face value per share Rs | - | 4 columns
R091-R092 | SA BS | Share capital | - | 2 columns
R093-R094 | SA BS | Reserves and surplus | - | 2 columns
R095-R096 | SA BS | Money received against share warrants | OCR_UNCERTAIN carried | 2 columns
R097-R098 | SA BS | Long-term borrowings | OCR_UNCERTAIN carried | 2 columns
R099-R100 | SA BS | Deferred tax liabilities (net) | - | 2 columns
R101-R102 | SA BS | Long-term provisions | - | 2 columns
R103-R104 | SA BS | Short-term borrowings | - | 2 columns
R105-R106 | SA BS | Trade payables, micro and small enterprises | OCR_UNCERTAIN carried | 2 columns
R107-R108 | SA BS | Trade payables, other creditors | OCR_UNCERTAIN carried | 2 columns
R109-R110 | SA BS | Other current liabilities | OCR_UNCERTAIN carried | 2 columns
R111-R112 | SA BS | Short-term provisions | - | 2 columns
R113-R114 | SA BS | Total equity and liabilities | OCR_UNCERTAIN carried | 2 columns
R115-R116 | SA BS | Property plant and equipment | - | 2 columns
R117-R118 | SA BS | Intangible assets | - | 2 columns
R119-R120 | SA BS | Capital work in progress | - | 2 columns
R121-R122 | SA BS | Intangible assets under development | - | 2 columns
R123-R124 | SA BS | Non-current investments | - | 2 columns
R125-R126 | SA BS | Other non-current assets | - | 2 columns
R127-R128 | SA BS | Inventories | - | 2 columns
R129-R130 | SA BS | Trade receivables | - | 2 columns
R131-R132 | SA BS | Cash and cash equivalents | - | 2 columns
R133-R134 | SA BS | Other current assets | - | 2 columns
R135-R136 | SA BS | Total assets | OCR_UNCERTAIN carried | 2 columns
R137-R138 | SA CF | CF profit before extraordinary items and tax | - | 2 columns
R139-R140 | SA CF | CF depreciation adjustment | - | 2 columns
R141-R142 | SA CF | CF gratuity provision adjustment | ZERO_STANDING(some periods); OCR_UNCERTAIN carried | 2 columns
R143-R144 | SA CF | CF interest expense adjustment | - | 2 columns
R145-R146 | SA CF | CF interest income adjustment | - | 2 columns
R147-R148 | SA CF | CF share of profit from partnership firm | OCR_UNCERTAIN carried | 2 columns
R149-R150 | SA CF | CF operating profit before working capital changes | - | 2 columns
R151-R152 | SA CF | CF change in inventories | - | 2 columns
R153-R154 | SA CF | CF change in trade receivables | - | 2 columns
R155-R156 | SA CF | CF change in other non-current assets | - | 2 columns
R157-R158 | SA CF | CF change in other current assets | - | 2 columns
R159-R160 | SA CF | CF change in trade payables | - | 2 columns
R161-R162 | SA CF | CF change in other current liabilities | - | 2 columns
R163-R164 | SA CF | CF change in provisions | ZERO_STANDING(some periods) | 2 columns
R165-R166 | SA CF | CF cash generated from operations | - | 2 columns
R167-R168 | SA CF | CF income taxes paid | - | 2 columns
R169-R170 | SA CF | CF net cash from operating activities before extraordinary i | OCR_UNCERTAIN carried | 2 columns
R171-R172 | SA CF | CF purchase of tangible and intangible assets | ZERO_STANDING(some periods) | 2 columns
R173-R174 | SA CF | CF interest received (investing) | - | 2 columns
R175-R176 | SA CF | CF proceeds from sale of fixed assets | ZERO_STANDING(some periods) | 2 columns
R177-R178 | SA CF | CF fixed assets purchased including CWIP | ZERO_STANDING(some periods) | 2 columns
R179-R180 | SA CF | CF (increase)/decrease in non-current investments | - | 2 columns
R181-R182 | SA CF | CF interest paid (financing) | - | 2 columns
R183-R184 | SA CF | CF increase in long-term borrowings | - | 2 columns
R185-R186 | SA CF | CF increase in short-term borrowings | - | 2 columns
R187-R188 | SA CF | CF proceeds from share warrants | ZERO_STANDING(some periods) | 2 columns
R189-R190 | SA CF | CF net cash from financing | - | 2 columns
R191-R192 | SA CF | CF opening cash and cash equivalents | - | 2 columns
R193-R194 | SA CF | CF cash and cash equivalents per balance sheet | OCR_UNCERTAIN carried | 2 columns
R195-R196 | SA CF | CF cash and cash equivalents at end of period | OCR_UNCERTAIN carried | 2 columns
R197-R200 | CON P&L | Revenue from operations | - | 4 columns
R201-R204 | CON P&L | Other income | - | 4 columns
R205-R208 | CON P&L | Total income | - | 4 columns
R209-R212 | CON P&L | Purchases of stock in trade | - | 4 columns
R213-R216 | CON P&L | Changes in inventories | - | 4 columns
R217-R220 | CON P&L | Other direct expenses | - | 4 columns
R221-R224 | CON P&L | Employee benefits expenses | - | 4 columns
R225-R228 | CON P&L | Finance costs | - | 4 columns
R229-R232 | CON P&L | Depreciation and amortisation | - | 4 columns
R233-R236 | CON P&L | Other expenses | - | 4 columns
R237-R240 | CON P&L | Total expenses | - | 4 columns
R241-R244 | CON P&L | Profit before exceptional and extraordinary items and tax | - | 4 columns
R245-R248 | CON P&L | Exceptional items | ZERO_STANDING(all periods) | 4 columns
R249-R252 | CON P&L | Profit before tax | OCR_UNCERTAIN carried | 4 columns
R253-R256 | CON P&L | Current tax | - | 4 columns
R257-R260 | CON P&L | Deferred tax | - | 4 columns
R261-R264 | CON P&L | Tax adjustments for earlier years | ZERO_STANDING(some periods); OCR_UNCERTAIN carried | 4 columns
R265-R268 | CON P&L | Profit for the period | - | 4 columns
R269-R272 | CON P&L | Share of minority interest | - | 4 columns
R273-R276 | CON P&L | Net profit transferred to reserves and surplus | - | 4 columns
R277-R280 | CON P&L | EPS basic Rs | - | 4 columns
R281-R284 | CON P&L | EPS diluted Rs | - | 4 columns
R285-R288 | CON P&L | Weighted average shares (basic) | - | 4 columns
R289-R292 | CON P&L | Weighted average shares (diluted) | - | 4 columns
R293-R296 | CON P&L | Face value per share Rs | - | 4 columns
R297-R298 | CON BS | Share capital | - | 2 columns
R299-R300 | CON BS | Reserves and surplus | - | 2 columns
R301-R302 | CON BS | Money received against share warrants | - | 2 columns
R303-R304 | CON BS | Minority interest | - | 2 columns
R305-R306 | CON BS | Long-term borrowings | - | 2 columns
R307-R308 | CON BS | Deferred tax liabilities (net) | OCR_UNCERTAIN carried | 2 columns
R309-R310 | CON BS | Long-term provisions | - | 2 columns
R311-R312 | CON BS | Short-term borrowings | - | 2 columns
R313-R314 | CON BS | Trade payables, micro and small enterprises | - | 2 columns
R315-R316 | CON BS | Trade payables, other creditors | - | 2 columns
R317-R318 | CON BS | Other current liabilities | - | 2 columns
R319-R320 | CON BS | Short-term provisions | - | 2 columns
R321-R322 | CON BS | Total equity and liabilities | OCR_UNCERTAIN carried | 2 columns
R323-R324 | CON BS | Property plant and equipment | - | 2 columns
R325-R326 | CON BS | Intangible assets | - | 2 columns
R327-R328 | CON BS | Capital work in progress | - | 2 columns
R329-R330 | CON BS | Intangible assets under development | - | 2 columns
R331-R332 | CON BS | Other non-current assets | - | 2 columns
R333-R334 | CON BS | Inventories | - | 2 columns
R335-R336 | CON BS | Trade receivables | - | 2 columns
R337-R338 | CON BS | Cash and cash equivalents | - | 2 columns
R339-R340 | CON BS | Other current assets | - | 2 columns
R341-R342 | CON BS | Total assets | OCR_UNCERTAIN carried | 2 columns
R343-R344 | CON CF | CF profit before extraordinary items and tax | - | 2 columns
R345-R346 | CON CF | CF depreciation adjustment | - | 2 columns
R347-R348 | CON CF | CF gratuity provision adjustment | - | 2 columns
R349-R350 | CON CF | CF interest expenses adjustment | - | 2 columns
R351-R352 | CON CF | CF interest income adjustment | - | 2 columns
R353-R354 | CON CF | CF exchange difference on forex | ZERO_STANDING(all periods) | 2 columns
R355-R356 | CON CF | CF profit on sale of fixed assets | ZERO_STANDING(some periods) | 2 columns
R357-R358 | CON CF | CF operating profit before working capital changes | - | 2 columns
R359-R360 | CON CF | CF change in trade receivables | - | 2 columns
R361-R362 | CON CF | CF change in inventories | - | 2 columns
R363-R364 | CON CF | CF change in other current assets | - | 2 columns
R365-R366 | CON CF | CF change in other non-current assets | - | 2 columns
R367-R368 | CON CF | CF change in trade payables | - | 2 columns
R369-R370 | CON CF | CF change in other current liabilities | OCR_UNCERTAIN carried | 2 columns
R371-R372 | CON CF | CF income taxes paid | - | 2 columns
R373-R374 | CON CF | CF cash generated from operations | - | 2 columns
R375-R376 | CON CF | CF net cash from operating activities | - | 2 columns
R377-R378 | CON CF | CF purchase of tangible and intangible assets | - | 2 columns
R379-R380 | CON CF | CF proceeds from sale of fixed assets | ZERO_STANDING(some periods) | 2 columns
R381-R382 | CON CF | CF interest received (investing) | OCR_UNCERTAIN carried | 2 columns
R383-R384 | CON CF | CF net cash from investing | - | 2 columns
R385-R386 | CON CF | CF interest paid (financing) | - | 2 columns
R387-R388 | CON CF | CF increase in long-term borrowings | - | 2 columns
R389-R390 | CON CF | CF increase in short-term borrowings | - | 2 columns
R391-R392 | CON CF | CF moneys raised through share warrants | ZERO_STANDING(some periods) | 2 columns
R393-R394 | CON CF | CF net additional/(withdrawn) by other partners in subsidiar | - | 2 columns
R395-R396 | CON CF | CF net cash from financing | - | 2 columns
R397-R398 | CON CF | CF net increase/(decrease) in cash | - | 2 columns
R399-R400 | CON CF | CF opening cash and cash equivalents | OCR_UNCERTAIN carried | 2 columns
R401-R402 | CON CF | CF closing cash and cash equivalents | OCR_UNCERTAIN carried | 2 columns

RESTATED: Total equity and liabilities R113-R114 equals Total assets R135-R136 (same balance, OCR conflicted). Closing cash R131-R132 vs CF R191-R196 (21.91 vs 21.98 OCR). SA and CON statements are separate tables.

## 2. ZERO_STANDING
table | line item | dash IDs | scope
SA P&L | Exceptional items | R051,R052,R053,R054 | all periods
SA CF | CF gratuity provision adjustment | R142 | some periods
SA CF | CF change in provisions | R163 | some periods
SA CF | CF purchase of tangible and intangible assets | R172 | some periods
SA CF | CF proceeds from sale of fixed assets | R175 | some periods
SA CF | CF fixed assets purchased including CWIP | R177 | some periods
SA CF | CF proceeds from share warrants | R187 | some periods
CON P&L | Exceptional items | R245,R246,R247,R248 | all periods
CON P&L | Tax adjustments for earlier years | R261,R263 | some periods
CON CF | CF exchange difference on forex | R353,R354 | all periods
CON CF | CF profit on sale of fixed assets | R355 | some periods
CON CF | CF proceeds from sale of fixed assets | R379 | some periods
CON CF | CF moneys raised through share warrants | R391 | some periods
Plus M01-M07, M09 in section 9 (M12-M18 carry no dash value; none added).

## 3. NOTES
ID | note | flags
R516 | SA note 1 | -
R517 | SA note 2 | -
R518 | SA note 3 warrants | RESTATED with R422-R426, R409-R417, R553
R519 | SA note 4 | RESTATED SA/CON and R466/R467
R520 | SA note 5 | -
R521 | SA note 6 | -
R522 | SA note 7 | -
R523 | SA note 8 | -
R536 | CON note 1 | -
R537 | CON note 2 | -
R538 | CON note 3 | -
R539 | CON note 4 | FOOTNOTE_UNRESOLVED (alternative "reviewed by Statutory Auditors / certified by management" left unresolved)
R540 | CON note 5 | RESTATED SA/CON and R466/R467
R541 | CON note 6 | -
R542 | CON note 7 | -
R543 | CON note 8 | -
R544 | CON note 9 | -
R525 | SA CF note (i) | -
R526 | SA CF note (ii) | -
R546 | CON CF note (i) | -
R547 | CON CF note (ii) | -
R535 | CON notes header | -
R553 | certificate note 1 (warrant terms) | RESTATED with SA note 3
R554 | certificate note 2 (only 25% received) | RESTATED with R552
SA has 8 notes, CON has 9 (CON note 4 on subsidiary status has no SA twin).

## 4. AGENDA ITEMS / BOARD OUTCOME
ID | item | flags
R472,R473,R474 | item 1: approve unaudited SA and CON results H1 FY27, audit committee reviewed, LRR enclosed | -
R551,R549,R548,R459,R460,R461 | item 2: statement of deviations, warrant proceeds (Reg 32), auditor certificate | -
R002 | meeting 02:30 p.m. to 04:30 p.m. (2 hours) | -
R475,R508,R444 | signature Priyanka Bansal 16:37:54 +05:30 on 2026.10.16, after the 16:30 conclusion | no pre-meeting flag
Absent from outcome letter: AR/AGM, dividend, record date, director changes, auditor change, ESOP, enabling resolutions. Only 2 items.

## 5. AUDITOR PARAGRAPHS
ID | para | flags
R509,R510 | SA: moderate assurance, no audit opinion | -
R446,R447,R439,R438,R449 | SA: firm, SRE 2410, SEBI circular 29-Mar-2019 | -
R527,R528 | CON: moderate assurance, no audit opinion | -
R529 | CON: includes subsidiary Danya Electric Company (AS 21) | -
R530 | CON: subsidiary unaudited, reliance on unaudited interim information | unaudited / management-furnished subsidiary
R430-R433,R434-R437,R418-R421 | signature blocks: firm reg, peer review 020690, partner 238452, UDINs | OCR variants of firm reg: 0136235 (R434), 013623S (R431), 0136238 (R418); UDINs R437, R433, R421
R448,R476,R478,R488,R490 | signatory R. Rajaram; review period 30-Sep-2026; report dates 16-10-2026 | -
M10,M11 | conclusion paras SA and CON (unmodified) | MISSING_FROM_STRUCTURED
M16,M17 | management-responsibility paras SA (AS 25 qualifier) and CON | MISSING_FROM_STRUCTURED
EoM, Other Matter, Going Concern: none found in fulltext grep.

## 6. ENTITIES
ID | entity | flags
R442 | NSE listing exchange | -
R443 | trading symbol | -
R444 | CS signatory | -
R445 | statutory auditors | -
R446 | auditor firm | -
R447 | ICAI | -
R448 | auditor signatory | -
R449 | SEBI | -
R450 | reporting company | -
R451 | MCA | -
R452 | MD signatory Vee Rajmohan | -
R453 | Promoter and Promoter Group warrant allottees | -
R454 | non-promoter allottees | -
R455 | Danya Electric Company subsidiary (AS 21) | ENTITY_CHANGE untestable (no prior list)
R456 | Danya 90% held, only subsidiary | ENTITY_CHANGE untestable (no prior list)
R457 | partner 7.5% (also MD, R452) | -
R458 | partner 2.5% | -
R459 | NSE circular | -
R460 | certificate issuer | -
R461 | Board addressee | -
M18 | Audit Committee | MISSING_FROM_STRUCTURED

## 7. FORWARD, DATES, QUALIFIERS, OTHER NUMBERS
R462-R471 forward (10): warrant balance, conversion, validity, reconciliation. RESTATED: R462/R468; R463/R465/R470; R464/R469; R466/R467. R471 use of proceeds.
R472-R506 dates (35). RESTATED: R472/R001; R479/R503; R480/R502; R482/R494; R477/R489. R506 conversion window 18 months (R417/R426/R464).
R507-R554 qualifiers (48): units, column status (R512, R532: FY26 Audited per text layer), notes (section 3), certificate (R548-R554).
R001-R002 letter date and meeting time; R403-R421 certificate numbers; R422-R426 SA warrant note; R427-R429 Danya shares; R438-R441 identifiers.

## 8. WARRANT FIGURES (RESTATED)
Issue price 169: R412,R423. Subscription 42.25: R413,R424. Exercise 126.75: R414,R416,R424. Received Rs 5,26,85,750: R409,R415,R425; 526.86 Lakhs: R404, R095-R096. Warrants 12,47,000: R411,R422,R518,R553. Allocation 2,107.43: R403,R471. Utilised 520.31 / unutilised 6.55: R405,R406 (OCR column assignment).

## 9. MISSING_FROM_STRUCTURED (loop back to A1)
id | table | location | content | flag
M01 | SA P&L | fulltext line 900 | Extraordinary Items (VIII) standalone: dash all four periods | MISSING_FROM_STRUCTURED; ZERO_STANDING
M02 | SA P&L | fulltext line 905 | Tax Adjustments for Earlier Years standalone: dash all periods | MISSING_FROM_STRUCTURED; ZERO_STANDING
M03 | SA CF | fulltext line 995 | Dividends received, standalone CF: dash | MISSING_FROM_STRUCTURED; ZERO_STANDING
M04 | SA CF | fulltext line 996 | Interest paid (operating section), standalone CF: dash | MISSING_FROM_STRUCTURED; ZERO_STANDING
M05 | SA CF | fulltext line 997 | Interest received (operating section), standalone CF: dash | MISSING_FROM_STRUCTURED; ZERO_STANDING
M06 | SA CF | fulltext line 1000 | Proceeds from extraordinary items, standalone CF: dash | MISSING_FROM_STRUCTURED; ZERO_STANDING
M07 | SA CF | fulltext line 1001 | Payment for extraordinary items, standalone CF: dash | MISSING_FROM_STRUCTURED; ZERO_STANDING
M08 | SA CF | fulltext lines 1007-1008, 1014-1015 | Standalone CF rows with no structured ID: net cash from investing (B), net increase/decrease in cash (D), closing cash line (line 1015 garbled). Values absent or unreadable in fulltext; not estimated | MISSING_FROM_STRUCTURED; OCR_UNCERTAIN
M09 | CON P&L | fulltext line 1063 | Extraordinary Items (VIII) consolidated: dash all periods | MISSING_FROM_STRUCTURED; ZERO_STANDING
M10 | Aud para | fulltext lines 124-127 | Standalone conclusion para 4: nothing has come to our attention (unmodified conclusion). No EoM, Other Matter or Going Concern paragraph found by grep | MISSING_FROM_STRUCTURED
M11 | Aud para | fulltext lines 478-482 | Consolidated conclusion: nothing has come to our attention (unmodified). Subsidiary unaudited reliance sits at R530 | MISSING_FROM_STRUCTURED
M12 | SA P&L | fulltext line 899 | Item VII "Profit Before Extraordinary Items and Tax" standalone (label OCR-garbled as "vil ne Before Extraordinary Items and Tax"): H1 FY27 1,787.67; H2 FY26 1,464.63; H1 FY26 1,227.24; FY26 2,691.87 (period order per header; same figures as R047-R050) | MISSING_FROM_STRUCTURED; RESTATED with R047-R050
M13 | CON P&L | fulltext line 1060 | Item VII "Profit Before Extraordinary Items and Tax" consolidated: H1 FY27 1,866.01; H2 FY26 1,564.59; H1 FY26 1,287.07; FY26 2,851.66 (same figures as R241-R244) | MISSING_FROM_STRUCTURED; RESTATED with R241-R244
M14 | SA CF | fulltext line 982 | "Profit On Sale of Fixed Asset" (OCR "Protit On Sale of Fixed Asset"), standalone CF adjustments: one garbled value near "qas7)", period assignment unreadable; not estimated | MISSING_FROM_STRUCTURED; OCR_UNCERTAIN
M15 | SA CF | fulltext line 379 | Operating activities total row "NET CASH FLOWS FROM (USED IN) OPERATING ACTIVITIES (A)": no value on the row in the fulltext; not estimated | MISSING_FROM_STRUCTURED; OCR_UNCERTAIN
M16 | Aud para | fulltext lines 97-102 | Standalone auditor para 2: management responsible for the Statement per recognition and measurement principles in AS 25 Interim Financial Reporting (s.133 Companies Act 2013); auditor responsibility is to report based on review | MISSING_FROM_STRUCTURED
M17 | Aud para | fulltext lines 440-447 | Consolidated auditor para: Parent Company management responsible for the Statement per AS 25 and Regulation 33; Statement approved by Parent Board; auditor to report based on review | MISSING_FROM_STRUCTURED
M18 | Entity | fulltext line 40 (also lines 295, 660) | Audit Committee: reviewed and recommended the results to the Board (board outcome letter L40; reviewed again at L295, L660) | MISSING_FROM_STRUCTURED
M19 | Qualifier+Date hdr | fulltext L214 (date header L212) | SA balance sheet column header: "Unaudited    Audited" under "As at 30th Septembe r, 2026 | Asat 31st March, 2026" (H1 FY27 Unaudited; 31 Mar 2026 Audited) | MISSING_FROM_STRUCTURED
M20 | Qualifier+Date hdr | fulltext L349 and L974 (date header L347) | SA cash flow column header: L349 "(Unudited)  Audiced)" (OCR for Unaudited/Audited); L974 "(Unaudited) Audited)"; L347 "As t 30th September, 2026 | Asa1 315t March, 2026" | MISSING_FROM_STRUCTURED; OCR_UNCERTAIN
M21 | Qualifier+Date hdr | fulltext L588 (date header L587) | CON balance sheet column header: "Unaudited    Audited" under "Asat30th2026September, | 31 March, 2026" | MISSING_FROM_STRUCTURED
M22 | Qualifier+Date hdr | fulltext L725 (date header L722) | CON cash flow column header: "Unaudited    Audited" under "30th September, | 31st March," | MISSING_FROM_STRUCTURED
M23 | Signing date | fulltext L339 | SA notes page signing date: "+ 16-10-2026" (page 7 marker follows) | MISSING_FROM_STRUCTURED; OCR_UNCERTAIN
M24 | Signing date | fulltext L708 | CON notes signing date: "Date: 16-10-2026" (DIN: 00844400 on L707, Place Chennai) | MISSING_FROM_STRUCTURED
M25 | Signing date | fulltext L1192 | CON cash flow signing date: "Date; 16-10-2026" (Place: Chennai, Managing Director, DIN: 00844400) | MISSING_FROM_STRUCTURED
M26 | Signing date | fulltext L283 | Date line "Date: 16-10-2026" (text-layer page 6 block, before SA notes at L294) | MISSING_FROM_STRUCTURED
M27 | Signing date | fulltext L412 | Date line "Date: 16-10-2026" (follows SA CF notes header L401) | MISSING_FROM_STRUCTURED
M28 | Signing date | fulltext L649 | CON notes date, OCR-split: "Da | 6-10-2026" (read as 16-10-2026; not estimated beyond text) | MISSING_FROM_STRUCTURED; OCR_UNCERTAIN
M29 | Date hdr | fulltext L157, L159, L881, L882 (L210 wrapped title) | SA P&L column date headers: "31st March," ; "September, 2026 | 315t Mareh, 2026"; "Half Year Ended 30th} ... Year Ended 31st March,"; "September, 2126 3st March, 2026 ... 2026" (2126 is OCR) | MISSING_FROM_STRUCTURED; OCR_UNCERTAIN
M30 | Date hdr | fulltext L1101 (title L585) | CON balance sheet column date header: "As at 30th: September, As at 31st March, 2026" | MISSING_FROM_STRUCTURED
M31 | Date title | fulltext L155, L509, L717 | Statement period titles: L155 "STANDALONE STATEMENT OF UNAUDITED FINANCIAL RESULTS FOR THE HALF YEAR ENDED 30TH SEPTEMBER, 2026"; L509 "SEPTEMBER 30, 2026"; L717 "SEPTEMBER 39, 2026" (OCR). Restated with R483, R491, R496 | MISSING_FROM_STRUCTURED; RESTATED
M32 | Date text | fulltext L46, L92, L435, L662, L683, L810 | Period/circular date mentions: L46 warrants "half-year ended September 30, 2026"; L92 and L435 review period "September 30, 2026"; L662 CON note 1 "half year ended September 30, 2026"; L683 CON note 4 subsidiary period "September 30, 2026"; L810 "NSE/CML/2024/23 dated September 05, 2024". Restated with R474, R476, R488, R495, R498, R539 | MISSING_FROM_STRUCTURED; RESTATED
M33 | Qualifier hdr | fulltext L516 | CON P&L column status header text-layer copy: "Unaudited | Unaudited | Unaudited | Audited". Restated with R532 (anchored L1041) | MISSING_FROM_STRUCTURED; RESTATED
M34 | Qualifier prose | fulltext L42, L77, L90, L421, L432, L472, L474, L684, L1034 | Unaudited/unaudited mentions in letter, auditor report intro and notes prose (titles, review scope, subsidiary reliance). Meaning covered by R507, R509, R527, R530, R539; line anchors not in structured | MISSING_FROM_STRUCTURED; RESTATED
M35 | Qualifier note | fulltext L401-403 | SA CF notes text-layer copy: "Notes:", "(i) Figures in bracket are outflows / deductions", "(ii) ... Indirect Method ... (AS-3)". Restated with R525, R526 | MISSING_FROM_STRUCTURED; RESTATED
```yaml
stage: A2-enumerator
company: "SUPREMEPWR"
quarter: "h1fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/supremepwr-h1fy27/work/ledger_results_supremepwr_h1fy27.md"
counts:
  notes: 21
  line_items: 153
  zero_standing: 13
  agenda_items: 2
  auditor_paras: 9
  entities: 20
flags_raised: [ZERO_STANDING, OCR_UNCERTAIN, FOOTNOTE_UNRESOLVED, RESTATED, MISSING_FROM_STRUCTURED]
ids_in_structured: 554
ids_referenced: 554
orphan_ids: []
missing_from_structured: [M01-M35]
gate_a2: pass
mismatch_note: ""
analyst_note: "Prior ledger absent, so ENTITY_CHANGE is untestable (only subsidiary: Danya Electric Company, 90%). Eight dash rows were missing from A1 (standalone and consolidated Extraordinary Items, Tax Adjustments for Earlier Years, standalone CF dividends, interest and extraordinary lines); Correction loop 1 added M12-M18 (item VII PBT SA and CON, SA CF profit on sale of fixed asset and operating total (A) with unreadable values, SA and CON management-responsibility paras, Audit Committee). M08 is unreadable standalone CF rows (net investing, net increase, closing cash). M10/M11 are the unmodified auditor conclusions. No Emphasis of Matter or Going Concern found. CON note 4 leaves the subsidiary review alternative unresolved (FOOTNOTE_UNRESOLVED). Board outcome has only 2 agenda items; meeting ran 2 hours."
```
