# A3 FORENSIC NOTES: NEOCHEM H1 FY27 (q2fy27), doctype: results

Company: Neochem Bio Solutions Limited (NSE SME, symbol NEOCHEM). Half year ended 30-Sep-2026. Standalone only.
Comparators: H1 FY26 (30.09.2025, audited), H2 FY26 (31.03.2026, balancing figure per Note 4), FY26 (audited).
Units: Rs Lakhs as filed (x0.01 = Rs Cr). Line numbers refer to the A1 fulltext.

SOURCE STATUS: connector-rebuilt copy of the NSE filing (fulltext lines 19-24; R330-R333). Every number below is PENDING VERIFICATION against the exchange original. No Decision Status write may rest on it.

Inputs read: A1 structured (R001-R363), A1 fulltext (292 lines), A2 ledger. Prior-quarter fulltext: none (first run on this name). Notion checklist: none; a batch-brief watch list is used instead (labelled "batch brief, not Notion").

## 0. LEDGER RECONCILIATION

- Structured IDs in ledger: 363 of 363. Each read at its cited fulltext line. A2 missing items M1, M2, M3 read at lines 88-90, 83-84, 216 and 291. Reconciled: 100%.
- Arithmetic ties, all hold within 0.01 rounding:
  - Balance sheet: equity 1,712.08 + 6,957.08 = 8,669.16; total current liabilities 5,503.62; total current assets 10,508.72; both sides 14,886.73 (Mar-26 11,711.52).
  - Results: expense columns sum to Total Expenses in all four periods. H1 FY26 + H2 FY26 = FY26 on every line (revenue 4,583.16 + 6,486.78 = 11,069.94; PAT 548.38 + 654.28 = 1,202.66).
  - Reserves roll: 6,172.40 + PAT 784.69 = 6,957.09 vs 6,957.08 filed. No dividend, no other movement.
  - Cash flow: every working-capital line ties to the balance-sheet change (payables 616.30, inventory 1,115.58, receivables 58.85, ST loans and advances 802.18, other current assets 57.62, borrowings 471.78 and 1,057.00, investments 115.93). Capex tie: net block plus CWIP plus intangibles up 1,371.23, plus depreciation 68.40, plus disposal 5.84 = 1,445.47 vs capex 1,445.46.
- A1 line drift (values verbatim, cite off by 1-2 lines, not material): R247/R315 "(1982)" sits on line 85 (cited 84); R295 "ICAI" on line 113 (cited 112); R312 CCO date on line 47 (cited 46); R263-R270 span lines 288-290 (all cited 288).
- A2 carry-ins checked at source lines: Note 9 cyber fraud (238-239, no rupee amount confirmed); asset-side "Deferred Tax Liabilities (net)" (163); negative FY26 proceeds (270, 277, 279); CFO/CCO changes (42-56, 67-90). All confirmed.

## 1. CONTEXT COMPUTATIONS (from filed numbers; feed F8, F10, F12)

| Metric | H1 FY27 | H2 FY26 | H1 FY26 | FY26 |
|---|---|---|---|---|
| Revenue from operations (line 184) | 6,892.43 | 6,486.78 | 4,583.16 | 11,069.94 |
| Revenue growth YoY / HoH | +50.4% / +6.3% | | | |
| Material cost incl. inventory change (188-189) | 4,776.31 | 4,532.88 | 2,941.69 | 7,474.58 |
| Gross margin | 30.70% | 30.12% | 35.82% | 32.48% |
| EBITDA (PBT pre-exceptional + finance + D&A - other income) | 1,203.66 | 1,125.94 | 859.20 | 1,985.14 |
| EBITDA margin | 17.46% | 17.36% | 18.75% | 17.93% |
| Other income (185) / % of PBT | 37.12 / 3.6% | 134.88 / 13.7% | 135.03 / 18.4% | 269.91 / 15.7% |
| PBT less other income | 1,008.47 | 850.55 | 597.80 | 1,448.34 |
| PAT (212) | 784.69 | 654.28 | 548.38 | 1,202.66 |
| Total tax / PBT (ETR) | 24.95% | 33.60% | 25.17% | 30.01% |
| ETR excl. prior-year short provision | 24.95% | 30.40% | 25.17% | 28.17% |
| Basic EPS (214) / implied weighted shares (lakh) | 4.58 / 171.33 | 4.74 / 138.03 | 4.52 / 121.32 | 8.71 / 138.08 |

H2 FY26 PBT less other income uses PBT after the 61.89 exceptional (985.43 - 134.88); pre-exceptional it is 912.43.

Working capital (days on half-year basis: H1 = 183 days, H2 = 182 days; receivables on revenue, inventory and payables on material cost):

| | 30.09.2026 | 31.03.2026 |
|---|---|---|
| Receivable days | 127.8 | 136.7 |
| Inventory days | 154.8 | 117.5 |
| Payable days | 67.8 | 46.4 |
| Cash conversion cycle | 214.8 | 207.8 |
| Total borrowings (143 + 149) | 3,308.13 | 1,779.35 |
| of which short term | 83.6% | 96.1% |
| Debt / equity | 0.38 | 0.23 |
| MSME share of trade payables (151) | 65.7% | 67.0% |

Cash conversion: CFO -105.25 (H1 FY27) and -1,693.78 (FY26). Over 18 months, PAT 1,987.35 against CFO -1,799.03.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R115, R116, R117 | 198 | "Exceptional Items \| - \| 61.89 \|" | AMBIGUOUS | The exceptional line is nil in the half that holds the disclosed July 2026 cyber fraud (Note 9). Any loss is in Other Expenses (418.73, +35.7% YoY), carried as an asset, or nil. The H2 FY26 charge of 61.89 has no note in this filing. The line points to a possible H2 FY27 write-off. Ask: nature of the 61.89; where the fraud loss sits. |
| A3-02 | F1 | R043, R044, R055, R056, R190 | 164, 171, 262 | "Short Term Loans and Advances \| 1,019.20 \| 217.02" | AMBIGUOUS | All loans and advances are short term; the long-term line is nil (164). The balance rose 4.7x (+802.18). That is 60.8% of the H1 working-capital outflow (1,318.69), and no note explains it. Possible contents: capital advances for the 1,445.46 capex, supplier advances, an unrecovered fraud receivable, advance tax, loans to related parties. Ask for the split. |
| A3-03 | F1 | R168, R169, R051, R052 | 251, 169 | "Add: Bad Debt \| 0.00 \| 0.00" | AMBIGUOUS | No write-off and no provision line in either period. Receivables are 4,813.49, about 128 days of H1 revenue (161 days on FY26 revenue at Mar-26). FY26 receivables rose 2,344.66 (259). Ask for ageing above 180 days and the provisioning policy. |
| A3-04 | F1 | R267, R268, R174, R202, R263, R265 | 254, 289-290 | "Fixed deposits having maturity less than 12 months 0.00 / 0.00" | AMBIGUOUS | H1 interest income of 27.34 already exceeds full-year FY26 (13.04), with no FDs and a bank balance of 0.46. Cash on hand is 18.03 (97.5% of cash). Some other asset earns interest: non-current investments 509.07, ST loans and advances 1,019.20, or other non-current assets 499.22. Ask which asset earns it and whether any counterparty is related. |
| A3-05 | F1 | R172, R173, R070, R175, R177 | 253, 185, 254-255 | "Less: Subsidy Income \| 0.00 \| 0.00" | AMBIGUOUS | FY26 other income is 269.91. Interest (13.04) and investment profit (0.13) explain only 13.17. Subsidy is nil, so 256.74 (15% of FY26 PBT) has no source shown. H1 FY27 other income fell to 37.12. Reported PBT grew +42.7% YoY; operating PBT less other income grew +68.7%. Ask what the FY26 other income was and whether it recurs. |
| A3-06 | F6 | R352, R303, R298, R299, R327 | 238-239 | "the balance is in the process of recovery with the assistance of the legal authorities" | FORWARD-SIGNAL | An undated commitment, status underway. The note gives no fraud amount, no amount recovered, no balance and no balance-sheet location. "Substantial amount" is not a number. If recovery fails, a charge lands in a later period (see A3-01, A3-02). Ask: gross loss, amount recovered to date, balance, where carried, provision, FIR or insurance claim, control fix. |
| A3-07 | F6 | R210, R211, R033, R034, R037, R038, R216, R220 | 273, 159, 161, 277, 279 | "Purchase of fixed assets \| -1,445.46 \| -295.44" | FORWARD-SIGNAL | H1 capex is 4.9x full-year FY26. PPE rose 55.3% and CWIP went from 5.84 to 275.58. No note names the project, capacity, cost or commissioning date, so the largest use of cash has no commitment to track. Funding: LT borrowings +471.78 (32.6% of capex) and ST borrowings +1,057.00, with CFO -105.25. Higher depreciation and interest follow. ST funding of fixed assets means a refinancing or a raise. Ask about the project and the funding plan. |
| A3-08 | F8 | R131, R133, R127 | 204, 203 | "Short Provision for Previous year \| - \| 31.61 \| - \| 31.61" | AMBIGUOUS | A non-zero prior-year tax true-up (rule FINDING). H2 FY26 ETR was 33.60%, or 30.40% excluding the true-up, against 25.17% statutory. H1 periods sit at 25.17% current tax. H2 shows a step-up pattern; H2 FY27 may repeat it. Ask the cause: disallowances, the exceptional item, s.43B(h) (see A3-10). |
| A3-09 | F8 | R198, R199, R126, R027, R028, R361 | 266, 203, 154 | "Less: Direct taxes paid \| 0.00 \| 296.22" | FORWARD-SIGNAL | The H1 tax provision is 263.15; tax paid is nil. ST provisions rose 263.16, equal to the H1 provision. The Mar-26 balance (494.08) did not fall either. FY26 tax expense was 520.69 against 296.22 paid. [INFERENCE] Either the advance tax instalments due in June and September were not paid (interest exposure; a cash outflow of about 263 ahead), or payments were booked elsewhere (for example inside the ST loans and advances change). Ask for the advance tax paid in H1 and where it is booked. |
| A3-10 | F8 | R021, R022, R019, R020 | 151, 150 | "Total Outstanding dues of MSME \| 1,162.79 \| 773.06" | FORWARD-SIGNAL | MSME dues are 65.7% of trade payables. Payable days rose from 46.4 to 67.8. [INFERENCE] If MSME dues stay unpaid past 45 days at 31-Mar, s.43B(h) disallows the deduction and ETR rises. This may explain the 30.40% H2 FY26 ETR (A3-08). Ask for MSME ageing past 45 days. |
| A3-11 | F8 | R138-R141, R011, R012, R033, R034 | 206, 144, 159 | "Deferred tax \| -2.25 \| -2.89 \| -2.22 \| -5.10" | NEUTRAL-FACT | Deferred tax is a credit in every period; the shield is 21.5 bps of H1 PBT. DTL fell from 55.06 to 52.81 although net PPE rose 1,101.36 and was put to use. New plant usually raises DTL. The year-end deferred charge may turn to a debit. Low materiality. |
| A3-12 | F10 | R154-R161, R151, R001, R002 | 214-215, 137 | "(1) Basic \| 4.58 \| 4.74 \| 4.52 \| 8.71" | AMBIGUOUS | Basic equals diluted in all periods, so no dilutive instruments. Paid-up capital is unchanged at 1,712.08. H2 FY26 EPS of 4.74 implies 138.03 lakh weighted shares, which is the FY26 full-year weighting. H1 + H2 = 9.26 against FY 8.71; a balancing EPS would be 4.19. Per-share growth YoY is +1.3% against PAT +43.1%, because the FY26 issue diluted shares from 121.3 to 171.3 lakh implied. Face value is NOT FOUND in this filing. Ask how H2 FY26 EPS was computed. |
| A3-13 | F12 | R200, R201, R178, R179, R150, R153 | 267, 256, 212 | "Cash Generated/(used in) from operating activities (A) \| -105.25 \| -1,693.78" | CONFIRMATORY-NEGATIVE | Single segment (Note 5), so the entity balance sheet is the segment balance sheet. CFO is negative for two periods running. Over 18 months, cumulative PAT is 1,987.35 and CFO is -1,799.03. Assets grew 3,175.21 in H1; liabilities funded most of it (borrowings +1,528.78, payables +616.30, unpaid tax +263.16). Growth uses cash. External funding continues until working capital turns. |
| A3-14 | F12 | R049, R050, R182, R079 | 168, 258, 189 | "Inventories \| 4,040.97 \| 2,925.39" | AMBIGUOUS | Inventory rose 38.1% in six months while HoH revenue rose 6.3%. The P&L inventory change is -75.23, so roughly 1,040 of the build is raw material or other stock outside finished goods and WIP. Inventory days went from 117.5 to 154.8. Two readings: stock bought ahead for the new capacity, or slow-moving stock. The H2 FY27 inventory line will separate them. Ask. |
| A3-15 | F12 | R075-R082, R063-R066 | 188-189, 184 | "Cost of Material Consumed \| 4,851.54 \| 4,342.08 \| 3,015.20" | AMBIGUOUS | Gross margin fell 511 bps YoY (35.82% to 30.70%) and held at the H2 FY26 level (30.12%). Revenue rose 50.4% YoY. Employee cost rose only 3.5%, which held EBITDA margin near 17.5% (-129 bps YoY). Possible causes: price, mix or input cost. Ask which, and whether the H1 FY26 level of 35.8% can return. |
| A3-16 | F13 | R280, R282, R283, R311, R313, R304, R246, R248, R244 | 42-44, 53-56, 75-76, 79 | "Mr. Pradip Ramniklal Solanki has ceased to be the Chief Financial Officer" | FORWARD-SIGNAL | The CFO in post since 2018, who "has overseen the financial management" (lines 84-86), was replaced at the results meeting. This is the same half as the cyber fraud and the second negative-CFO period. The new CFO's profile stresses "internal controls, treasury and working capital management" (76) and "banking relationships" (79). Annexure A states no term for any of the three people (73-74), so terms cannot be mapped to catalyst dates. Ask why the change came now, whether it links to the fraud, and what Solanki's new role covers. Outcome filed at 18:53:20 (R273), 23 minutes after the 18:30 close. |
| A3-17 | F13 | R281, R289, R245, R297 | 45-47, 80-81, 231 | "Most recently Vertical Head - Textile Chemicals at Indofil Industries" | FORWARD-SIGNAL | The new CCO has 30+ years across textiles, coatings, plastics, construction chemicals and petrochemicals. This points to a commercial push into new applications or customers inside the single "Specialty chemicals" segment. It may also be what the new capacity serves. Ask about the target markets and the revenue plan for the capex. |
| A3-18 | F13 | R225, R224, R185, R217, R221, R205 | 281, 259, 277, 279, 270 | "Proceeds from issue of equity shares \| 0.00 \| 4,706.54" | FORWARD-SIGNAL | The board outcome has no statement of use or deviation of the FY26 issue proceeds. On the FY26 cash flow, the 4,706.54 went to the receivables build (2,344.66), net debt reduction (1,783.08 shown as negative proceeds), investments (625.00) and the CFO deficit. In H1 FY27 the company borrowed again (+1,528.78) for capex. Equity raised in FY26 is already spent and debt is rising again. Ask for the proceeds utilisation against the offer objects, and any deviation. |
| A3-19 | F14 | R204-R207, R039, R040, R176, R177, R359 | 270-271, 162, 255 | "Proceeds from sale of investments \| 115.93 \| -625.00" | AMBIGUOUS | The FY26 purchase of 625.00 sits as negative "proceeds", and "Purchase of investments" is 0.00 in both periods. The H1 sale of 115.93 left a profit of 0.00, so it was sold at book value. The investee is not disclosed. The company files standalone only. If the investee is a subsidiary or associate, the consolidation basis is open. Ask what the investment is and who the counterparty is. |
| A3-20 | F14 | R358, R360, R362, R285, R286, R342, R347, R208, R038 | 106-107, 224-226, 163, 277-280, 175 vs 216, 48 vs 61-62, 182 vs 229, 272 vs 161 | "applicable Indian Accounting Standards prescribed under Section 133" | AMBIGUOUS | Cumulative drafting points: (a) the review report cites Ind AS, but Note 2 cites GAAP under Rule 7 and the cash flow note cites AS 3 (287); (b) a "Deferred Tax Liabilities (net)" line appears on the assets side; (c) FY26 repayments appear as negative proceeds while repayment lines read 0.00; (d) the MD is "Swapnil B. Makati" on the balance sheet but "Swapnil R Makati" elsewhere; (e) the footer reads "Formerly Know as" and omits one former name; (f) the H2 FY26 column is labelled "(Audited)" although Note 4 calls it a balancing figure; (g) fixed-asset sale proceeds of 5.84 equal the Mar-26 CWIP of 5.84 exactly. Each point is minor. Together they are a finance-function quality signal, and they coincide with the CFO change (A3-16). Ask one governance question. |

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing lines | FINDING | All 42 ZERO_STANDING rows read. Most are template lines: warrants (139), WIP/stock-in-trade (190), MAT (205), discontinued (209-211), repayment lines, intangibles, FDs. Five carry signal: A3-01 to A3-05. |
| F2 Standalone vs consolidated | N.A. | Standalone-only filer (lines 39, 180); no consolidated statement and no subsidiary named. Investee question routed to A3-19. |
| F3 Shell-entity detection | N.A. | No consolidated cost lines to compare; no going concern paragraph. |
| F4 Unaudited contribution ratio | PASS | The review report covers the whole standalone statement (101-104). No Other Matter paragraph and no component auditor (121-126). Unreviewed share of PAT: 0%. |
| F5 Going concern / EoM tracking | PASS | No EoM, Other Matter or going concern paragraph (121-126); unmodified (Note 1, 223). First run: no prior text to diff. This filing is the baseline. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits: "in the process of" (239); "commenc" (38, meeting time only); near-hit "will also be made available" (59). A3-06 (fraud recovery, undated); A3-07 (capex with no commitment note). |
| F7 Hedge phrases | PASS | Zero lexicon hits in the notes (220-241), the letter or Annexure A. The "obtain assurance" text (116) is standard review scope. The vague quantifier "substantial amount" (238) is handled under A3-06. |
| F8 Tax forensics | FINDING | ETR 24.95% / 33.60% / 25.17% / 30.01%. Prior-year short provision 31.61 (A3-08). Nil tax paid in H1 (A3-09). MSME s.43B(h) exposure (A3-10). Deferred tax shield 21.5 bps (A3-11). |
| F9 OCI forensics | N.A. | AS (Indian GAAP) reporter (Note 2, 224-226; AS 3, 287). No OCI line in the results (184-215). The reserves movement equals PAT (784.68 vs 784.69). |
| F10 Share count and dilution | FINDING | Paid-up unchanged at 1,712.08 (137). Basic equals diluted, so the spread is nil. H2 FY26 EPS is inconsistent with the H1 and FY figures (A3-12). |
| F11 Net worth tie-out | PASS | 1,712.08 + 6,957.08 = 8,669.16 (137-140). The reserves roll-forward ties to PAT. No third-party number in context. |
| F12 Segment forensics | FINDING | Single segment (Note 5, 231), so the entity balance sheet is the segment balance sheet. The asset build is debt-funded and CFO is negative (A3-13). Inventory build (A3-14). Gross margin reset (A3-15). |
| F13 Board outcome beyond results | FINDING | No AR, AGM or fund-raise item. CFO replaced (A3-16) and CCO hired (A3-17), with no terms stated. No issue-proceeds utilisation statement (A3-18). Outcome filed 23 minutes after close (R273 stamp 18:53:20 vs 18:30). |
| F14 Note drafting inconsistencies | FINDING | Investment line mislabelled and investee undisclosed (A3-19). Cumulative drafting points (a)-(g) (A3-20). |
| F15 Entity list diffs | N.A. | No consolidation list in the filing and no prior quarter held. Former names recorded as a baseline (48, 61-62). |
| F16 Presentation: dropped disclosures | N.A. | Results doctype. |
| F17 Concall: silence audit | N.A. | Results doctype. Watch-list mapping below, for A4 only. |

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Recover the balance of the July 2026 cyber fraud loss with legal authorities' help; "substantial amount" already recovered | Not stated (undateable) | Note 9, lines 238-239 (R303, R352) | underway |
| CFO (Harshit Shah) and CCO (Vikram Nair) appointments | w.e.f. 27-Oct-2026; term not stated | Items 2-3, lines 42-47; Annexure A 73-74 | completed |
| Solanki re-designated to senior management and "continues in the employment of the Company" | w.e.f. 27-Oct-2026; ongoing | Item 4, lines 53-56 (R304) | completed |
| Intimation to be made available on www.neochem.in | On filing, 27-Oct-2026 | Line 59 (R305) | initiated |

No capex, capacity, commissioning or fund-raise commitment appears anywhere in the filing (see A3-07, A3-18).

## 5. WATCH-LIST MAPPING (batch brief, not Notion; F17 itself N.A.)

| Batch brief item | Filing coverage | Where |
|---|---|---|
| 1. Revenue and margin trend across half-years | Covered by numbers, not explained | Section 1; A3-15 |
| 2. Working capital days | Covered by numbers, no note | Section 1; A3-13, A3-14, A3-02 |
| 3. Related-party dealings | SILENT. No RPT disclosure. Counterparties of investments, interest-earning assets and ST advances unknown | A3-02, A3-04, A3-19 |
| 4. Promoter pledge or holding changes | SILENT (not part of a results filing) | none |
| 5. Capex or fund-raise; use of issue proceeds | Capex visible in the cash flow only; no project note; no proceeds utilisation statement | A3-07, A3-18 |

Silence count: first quarter observed (no prior held), so the count is 1 for items 3 and 4 and for the proceeds part of item 5.

## Loop 1 dispositions (A5 F1)

- R005-R006 | line 139 | "Money Received against Share warrants | - | -" | reviewed, no finding. Template line, nil on both dates. Consistent with basic EPS = diluted EPS in all periods (lines 214-215) and unchanged share capital 1,712.08 (line 137).
- R041-R044 | lines 163-164 | "Deferred Tax Liabilities (net) | - | -" / "Long Term loans and advances | - | -" | finding. R041-R042: F14, AMBIGUOUS, line 163, carried as A3-20 item (b) (asset-side DTL label; the real net DTL is on the liability side, 52.81 / 55.06, line 144). R043-R044: F1, AMBIGUOUS, line 164, carried as A3-02 (LT line nil while ST loans and advances rose 217.02 to 1,019.20, line 171).
- R236-R237 | line 38 | "commenced at 05:20 P.M. and concluded at 06:30 P.M." | reviewed, no finding. A 70-minute meeting covered the results and three KMP/SMP changes. The NSE file stamp NEOCHEM_27102026185320 (R273, line 20) shows filing at 18:53:20, 23 minutes after the close. The governance context is carried in A3-16 (F13); the timing raises no separate finding.

## 6. YAML BLOCK

```yaml
stage: A3-forensics
company: "NEOCHEM"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/neochem-q2fy27/work/forensics_neochem_q2fy27.md"
ledger_reconciled_pct: 100
source_status: "connector-rebuilt copy of NSE filing (fulltext lines 19-24); all numbers pending verification against exchange original"
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "198", classification: "AMBIGUOUS", implication: "Exceptional line nil in the half holding the July 2026 cyber fraud; H2FY26 61.89 exceptional has no note; possible later write-off"}
  - {id: "A3-02", check: "F1", line: "164, 171, 262", classification: "AMBIGUOUS", implication: "ST loans and advances 217.02 to 1,019.20 (+802.18, 60.8% of H1 WC outflow), no note; LT line nil; possible capital advances, fraud receivable, advance tax or related-party loans"}
  - {id: "A3-03", check: "F1", line: "251, 169", classification: "AMBIGUOUS", implication: "Bad debt 0.00 and no provision against receivables 4,813.49 (~128 days); ask ageing"}
  - {id: "A3-04", check: "F1", line: "254, 289-290", classification: "AMBIGUOUS", implication: "Interest income 27.34 in H1 vs 13.04 FY26 with nil FDs and bank 0.46; cash on hand 18.03; which asset earns interest, related counterparty?"}
  - {id: "A3-05", check: "F1", line: "253, 185", classification: "AMBIGUOUS", implication: "FY26 other income 269.91, of which 256.74 has no source shown (subsidy nil); H1FY27 falls to 37.12; operating PBT +68.7% YoY vs reported +42.7%"}
  - {id: "A3-06", check: "F6", line: "238-239", classification: "FORWARD-SIGNAL", implication: "Cyber fraud recovery underway, undated, no amounts or balance-sheet location; charge risk if recovery fails"}
  - {id: "A3-07", check: "F6", line: "273, 161, 279", classification: "FORWARD-SIGNAL", implication: "H1 capex 1,445.46 (4.9x FY26) with no project, capacity or date note; 67% funded outside term debt; depreciation, interest and refinancing step-up"}
  - {id: "A3-08", check: "F8", line: "204", classification: "AMBIGUOUS", implication: "Prior-year short provision 31.61; H2FY26 ETR 33.60% (30.40% ex true-up) vs 25.17%; H2 step-up pattern may repeat"}
  - {id: "A3-09", check: "F8", line: "266, 203, 154", classification: "FORWARD-SIGNAL", implication: "Direct taxes paid 0.00 vs H1 provision 263.15; ST provisions +263.16; advance tax unpaid (cash outflow and interest ahead) or misbooked"}
  - {id: "A3-10", check: "F8", line: "151", classification: "FORWARD-SIGNAL", implication: "MSME dues 1,162.79 (65.7% of payables), payable days 46.4 to 67.8; s.43B(h) disallowance risk raises ETR [INFERENCE]"}
  - {id: "A3-11", check: "F8", line: "206, 144", classification: "NEUTRAL-FACT", implication: "Deferred tax credit 2.25 (21.5 bps shield) and DTL falls despite +1,101.36 net PPE; year-end deferred charge may flip to debit"}
  - {id: "A3-12", check: "F10", line: "214-215", classification: "AMBIGUOUS", implication: "H2FY26 EPS 4.74 implies FY weighting (138.03 lakh); H1+H2 9.26 vs FY 8.71; per-share growth +1.3% YoY vs PAT +43.1% after FY26 dilution"}
  - {id: "A3-13", check: "F12", line: "267, 256", classification: "CONFIRMATORY-NEGATIVE", implication: "CFO negative two periods running; 18-month PAT 1,987.35 vs CFO -1,799.03; asset build funded by liabilities"}
  - {id: "A3-14", check: "F12", line: "168, 258, 189", classification: "AMBIGUOUS", implication: "Inventory +38.1% in six months vs revenue +6.3% HoH; ~1,040 raw material build; days 117.5 to 154.8; stock bought ahead vs slow-moving"}
  - {id: "A3-15", check: "F12", line: "188-189, 184", classification: "AMBIGUOUS", implication: "Gross margin 35.82% to 30.70% YoY (-511 bps) on +50.4% revenue; EBITDA margin held ~17.5% on employee-cost leverage"}
  - {id: "A3-16", check: "F13", line: "42-44, 53-56, 75-76", classification: "FORWARD-SIGNAL", implication: "CFO since 2018 replaced at the results meeting, same half as the fraud and negative CFO; new CFO profile stresses internal controls and working capital; no terms stated"}
  - {id: "A3-17", check: "F13", line: "45-47, 80-81", classification: "FORWARD-SIGNAL", implication: "CCO from Indofil textile chemicals; commercial push into new applications, possibly what the new capacity serves"}
  - {id: "A3-18", check: "F13", line: "281, 259, 277, 279", classification: "FORWARD-SIGNAL", implication: "No issue-proceeds utilisation statement; FY26 equity 4,706.54 absorbed by receivables, debt paydown, investments; H1 re-borrowing +1,528.78"}
  - {id: "A3-19", check: "F14", line: "270-271, 162, 255", classification: "AMBIGUOUS", implication: "FY26 investment purchase 625.00 shown as negative proceeds; 115.93 sold at book; investee undisclosed; consolidation basis open if related"}
  - {id: "A3-20", check: "F14", line: "106-107, 224-226, 163, 175, 182, 272", classification: "AMBIGUOUS", implication: "Seven drafting inconsistencies (Ind AS vs AS, asset-side DTL label, sign misposting, MD initial, footer name, balancing column labelled audited, 5.84 coincidence); finance-function quality signal alongside CFO change"}
forward_signals: ["A3-06", "A3-07", "A3-09", "A3-10", "A3-16", "A3-17", "A3-18"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-04", "A3-05", "A3-08", "A3-12", "A3-14", "A3-15", "A3-19", "A3-20"]
commitments:
  - {commitment: "Recover balance of July 2026 cyber fraud loss with legal authorities; substantial amount recovered", implied_date: "not stated", ref: "Note 9, lines 238-239", status_word: "underway"}
  - {commitment: "CFO Harshit Shah and CCO Vikram Nair appointed", implied_date: "w.e.f. 27-Oct-2026, term not stated", ref: "Items 2-3, lines 42-47; Annexure A 73-74", status_word: "completed"}
  - {commitment: "Solanki re-designated to senior management, continues in employment", implied_date: "w.e.f. 27-Oct-2026", ref: "Item 4, lines 53-56", status_word: "completed"}
  - {commitment: "Intimation to be posted on www.neochem.in", implied_date: "27-Oct-2026", ref: "line 59", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Source is a connector-rebuilt copy (lines 19-24); every number pends a check against the NSE original. The filing ties arithmetically, so the issues are disclosure, not addition. Three threads meet in one half. A July 2026 cyber fraud has no rupee amount and no exceptional charge (line 198 nil). ST loans and advances rose 802.18 with no note; that is the likeliest home for an unrecovered fraud balance or advance tax. The CFO was replaced at the results meeting, and the new CFO's profile stresses internal controls and working capital. A4 should ask these as one sequence, fraud amount first. Second thread: growth uses cash. CFO is negative two periods running, the FY26 issue money is spent, and H1 capex of 1,445.46 rode mostly on short-term debt with no project note. Nil tax paid against a 263.15 provision is either an unpaid liability or a misclassification. Gross margin fell 511 bps YoY; EBITDA margin held near 17.5% on operating leverage. First run: F5 and entity baselines set, no diffs possible."
```
