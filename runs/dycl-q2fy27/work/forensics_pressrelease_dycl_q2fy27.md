# A3 FORENSIC NOTES: DYCL q2fy27 (doctype: pressrelease)

Company: Dynamic Cables Limited (DYCL; BSE 540795)
Document: Reg 30 press release, Q2 and H1 FY27 (quarter ended 30 Sep 2026), 3 pages, dated 27.10.2026
Inputs read: runs/dycl-q2fy27/extracted/dycl-pressrelease-q2fy27-structured.md; runs/dycl-q2fy27/extracted/dycl-pressrelease-q2fy27-fulltext.md; runs/dycl-q2fy27/work/ledger_pressrelease_dycl_q2fy27.md
Prior-quarter extract: none (first quarterly review of this name). No Notion page and no companies/DYCL.md; the operator batch-brief watch list stands in as the monitoring checklist.
Units: Rs Crore. Page 2 table read from the render-corrected block (fulltext lines 112-124), per A1 and the ledger.
Model: claude-opus-5-5

## 1. LEDGER RECONCILIATION

Rows in ledger: 151 structured IDs (R001-R151) plus 2 MISSING_FROM_STRUCTURED rows (M1, M2) = 153. Rows read at cited line: 153. Reconciled: 100%.

Reconciliation notes (none change a value):
- R076, R077 (Term Loans 30 Sep 2.3, 30 Jun 2.5) are cited at line 140. In the fulltext they print at line 141 ("2.3      2.5"); line 140 carries only the 31 Mar value 2.6. Layout offset, values agree.
- R143 (tile rounding) and R145 (render correction) are A1 annotations, not source text. They are not used as evidence.
- M1 read at line 127: "Strong growth momentum from both government and private sector players". M2 read at line 108: "The business environment has improved despite crude price volatility and geo political disruptions."

Arithmetic tie-outs run on the render-corrected table (lines 114-123) and the borrowing table (lines 139-155):
- OP - Finance Cost - Depreciation + Other Income = PBT holds in all six periods within 0.1 (Q2FY27 36.3-4.2-3.5+1.0 = 29.6 vs 29.7; FY26 129.6-11.5-11.8+6.8 = 113.1 exact).
- Q1FY27 + Q2FY27 = H1FY27 on revenue (712.3), OP (74.3), finance cost (7.1), other income (2.2), PAT (47.1); depreciation 6.4 vs 6.3 and EPS 9.8 vs 9.7 are rounding.
- Margins recompute: Q2FY27 9.99%, Q1FY27 10.89%, Q2FY26 10.94%, H1FY27 10.43%, H1FY26 10.63%, FY26 10.82%.
- Tile growth rates recompute: Q2 revenue +29.0%, OP +17.9%, PAT +12.8%; H1 revenue +31.0%, OP +28.5%, PAT +24.3%.
- Borrowing table adds: 2.3+2.7+32.3 = 37.3; 37.3+77.7 = 115.0; 115.0-33.2 = 81.8. Same for 30 Jun (135.8-47.0 = 88.8 vs 88.7 printed, rounding) and 31 Mar (117.0-58.8 = 58.2).

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F6 | R117, R126, R127, R136 | 106-107, 135 | "new manufacturing plant going on stream and will start contributing from second half"; "Plant and Machinery have been installed at the newly established manufacturing facility" | FORWARD-SIGNAL | Dated commitment: revenue from the new plant in H2FY27 (Oct 2026 to Mar 2027). Status: installed, not commissioned. No capacity, capex amount, commissioning date or product line is given. Depreciation already rose 2.9 to 3.5 QoQ (+21%, line 118), so part of the asset may be capitalised. H2 brings depreciation, finance cost and start-up cost before full output. Tracker: first revenue from the plant by the Q3/Q4 FY27 filing. |
| A3-02 | F6 | R125 | 105 | "The growth momentum has continued this year and is expected to continue" | FORWARD-SIGNAL | Undated, unquantified growth commitment for the rest of FY27. Baseline: H1FY27 revenue +31% YoY (line 114, 712.3 vs 543.6). Test at Q3/Q4: H2FY27 YoY revenue growth vs H2FY26 654.2 (FY26 1197.8 minus H1FY26 543.6). |
| A3-03 | F7 | R128, M2 | 110, 108 | "The export market is also expected to gain momentum as global macros normalise"; "despite crude price volatility and geo political disruptions" | AMBIGUOUS | The export outlook is conditional on an external event outside management control, with no date. Export sales were ~Rs 56 Cr in H1 (line 131), 7.9% of H1 revenue. The crude-price mention points to insulation-compound (polymer) cost pressure, a possible cause of the Q2 margin dip (A3-05). Conservative read: exports stay soft until the condition is met. Question: export order book and the Q2 export run rate vs Q1. |
| A3-04 | F14 | R105, R132, R141, R144 | 24, 33, 88 | "Bandra(East) Mumbai-4000501"; "Un-Audited Financial Results"; "Financial Performance:  Q2FY27 ... (₹ in Crs)" | NEUTRAL-FACT | Drafting: the table never states standalone or consolidated. The cover letter says unaudited but does not state limited review status. The NSE postal code prints as 7 digits. Each item is immaterial. Together they are a minor governance data point. A4 must confirm the basis from the results filing before a number from this release enters the tracker. |
| A3-05 | F16 | R025-R027, R019-R021, R061-R062, R142, M2 | 67, 74, 81, 116, 122, 108 | "Scaling with Strength"; "Operating Margins %  10.0% / 10.9% / 11.0%"; "The business environment has improved" | AMBIGUOUS | Framing: the headline and the H1 tiles (+31/+29/+24, line 80) come before the Q2 tiles (+29/+18/+13, line 86). Q2 OPM of 10.0% is the lowest of the six periods shown: -90 bps QoQ, -100 bps YoY. Q2 PAT fell 11.6% QoQ (25.0 to 22.1). Q2 OP fell 4.5% QoQ on revenue +4.0%. The YoY incremental margin was 6.7% (5.5 / 81.6). The release does not explain the compression. Two readings: (a) copper/aluminium pass-through raises revenue and lowers margin %, with per-unit EBITDA held; (b) price or input-cost pressure (crude-linked compounds, line 108) or new-plant start-up cost. Volume or per-km EBITDA would show which. Neither is disclosed. |
| A3-06 | F16 | R019-R024, R031-R054 | 115-120 | "Operating Profits  36.3 / 38.0 / 30.8 / 74.3 / 57.8 / 129.6" | NEUTRAL-FACT | KPI definition: "Operating Profit" is not defined in the release. Arithmetic shows it equals EBITDA excluding Other Income (PBT + Finance Cost + Depreciation - Other Income) in all six periods within 0.1. Tracker label: EBITDA ex other income. Other income fell from 3.9 (H1FY26) to 2.2 (H1FY27), in line with lower cash. |
| A3-07 | F16 | R075, R148 | 133 | "Order book stands at ~ ₹ 829 Crores" | AMBIGUOUS | The order book has no definition and no date. The release does not say gross or net of GST, whether L1 / unsigned orders are included, or whether orders carry metal price-variation clauses. No inflow and no prior figure, so book-to-bill cannot be computed. Cover: 829 / TTM revenue 1366.5 (H2FY26 654.2 + H1FY27 712.3) = 0.61x, about 7.3 months. Question: definition, inflow in Q2, and the share of variable-price orders. |
| A3-08 | F16 | R085-R099, R150 | 147-155 | "LC Creditors (Off- balance sheet)  77.7  64.6  76.6"; "Net Debt  81.8  88.7  58.2" | NEUTRAL-FACT | KPI definition: company Net Debt includes off-balance-sheet LC creditors (115.0 - 33.2 = 81.8). This is the conservative view. On-balance-sheet net debt: 31 Mar net cash 18.4 (40.4 - 58.8); 30 Jun net debt 24.2; 30 Sep net debt 4.1. The H1 swing from net cash to net debt is 22.5 on-balance-sheet and 23.6 on the company's definition. Track both lines each quarter. |
| A3-09 | F16 | R031-R033, R082-R093 | 117, 145, 147, 149 | "Finance Cost  4.2  2.9  2.9"; "Total On-balance sheet Debt  37.3  71.2  40.4" | AMBIGUOUS | Q2 finance cost rose 45% QoQ and YoY (2.9 to 4.2). Over the same quarter, period-end on-balance-sheet debt fell from 71.2 to 37.3. Average period-end on-balance-sheet debt is about flat (Q1 55.8, Q2 54.3). Annualised Q2 finance cost of 16.8 is 31% of that average, too high for bank interest alone. The likely contents are LC / bill-discounting / acceptance charges, peaks within the quarter that the period-end snapshot misses, or interest that is no longer capitalised on the new plant. Question: split of finance cost into interest on fund-based debt, LC/discounting charges and other items, plus average utilisation within the quarter. |
| A3-10 | F16 | R082-R084, R088-R090, R094-R096 | 145, 149, 153 | "Working Capital Loans  32.3  64.4  35.6"; "Cash & equivalents  33.2  47.0  58.8" | AMBIGUOUS | In Q2, working capital loans fell 32.1 (64.4 to 32.3). Over the same quarter, LC creditors rose 13.1 (64.6 to 77.7) and cash fell 13.8 (47.0 to 33.2). About 27 of the 32 fell from cash drawdown and a move to non-fund (LC) credit. Little came from released working capital. Two readings: real working-capital release vs end-of-quarter repayment that raises again within the quarter. Separating observation: average WC utilisation and Q3 period-end WC loans. |
| A3-11 | F17 | R064, R040, R094-R099 | 122, 118, 153-155 | "Net Debt  81.8  88.7  58.2" | AMBIGUOUS | H1 cash earnings (PAT 47.1 + depreciation 6.3 = 53.4) plus the rise in net debt (23.6) mean about Rs 77 Cr of H1 uses. The release does not itemise them as capex, working capital or dividend. Cash fell from 58.8 to 33.2. Term loans are only 2.3 (line 141), so the new plant appears funded from accruals and cash, not project debt. No OCF and no capex figure. Watch items 4 and 5. Question: H1 capex, H1 OCF, inventory and payable days, and the plant's remaining capex and its funding. |
| A3-12 | F17 | M1, R073, R074, R118-R122, R146 | 127, 129, 131, 160-161 | "Strong growth momentum from both government and private sector players" | AMBIGUOUS | Silence audit vs the operator watch list (table in section 5). Not disclosed: volume or metal-price split of growth, per-unit EBITDA, inventory/payable days, OCF, capex and capacity of the new plant, and the revenue split between utilities, EPC and industrial customers. Promoter holding and pledge are not covered (normal for a press release; check the shareholding filing). Silence count 1 for each, a floor because earlier quarters are not in the pipeline. Repeated silence on the margin cause while margin falls would become CONFIRMATORY-NEGATIVE. |
| A3-13 | F16 | R073, R139, R146 | 129 | "Receivable days (calculated on trailing six-month gross sales) was ~ 59 days in Q2FY27" | NEUTRAL-FACT | The KPI is defined. Gross sales (GST-inclusive) is the like-for-like denominator for GST-inclusive receivables, so this is fair. A six-month base during 31% growth gives about 2 days fewer than a TTM base. No prior value. This is the only working-capital day count in the release. Track it on the same definition each quarter. |

Finding count: 13 total. FORWARD-SIGNAL 2 (A3-01, A3-02). AMBIGUOUS 7 (A3-03, A3-05, A3-07, A3-09, A3-10, A3-11, A3-12). CONFIRMATORY-NEGATIVE 0. NEUTRAL-FACT 4 (A3-04, A3-06, A3-08, A3-13).

## 3. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | No statutory results template in a press release. The ledger carries no ZERO_STANDING rows. The summary table has no exceptional or discontinued line, so their absence cannot be tested here. |
| F2 Standalone vs consolidated | N.A. | One unlabelled basis is shown (lines 113-123). No S-vs-C pair to decompose. The unstated basis is logged under F14 (A3-04). |
| F3 Shell-entity detection | N.A. | No standalone and consolidated cost lines to compare. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph in the document. |
| F5 Going concern / EoM scope | N.A. | No auditor report and no prior-quarter extract. |
| F6 Forward-commitment mining | FINDING | A3-01 (new plant contributes from H2, P&M installed), A3-02 (growth to continue). Register below. |
| F7 Hedge mining | FINDING | A3-03 (export momentum conditional on global macros; crude volatility). Disclaimer lines 167-173 are standard boilerplate and not a finding. |
| F8 Tax forensics | PASS | ETR Q2FY27 25.3%, Q1FY27 25.4%, Q2FY26 25.5%, H1FY27 25.4%, H1FY26 25.4%, FY26 25.3%. All within 35 bps of the 25.17% statutory rate. No deferred-tax split and no earlier-years line in the release. |
| F9 OCI forensics | N.A. | No OCI line in the release. |
| F10 Share count and dilution | PASS | Implied shares from PAT/EPS are about 4.84-4.86 Cr in every period, within EPS rounding (Q2FY27 22.1/4.6, FY26 84.4/17.4). No change detectable. EPS basis (basic/diluted) is not labelled. No diluted figure, so no spread to flag. |
| F11 Reserves and net worth tie-out | N.A. | No paid-up capital, other equity or net worth in the release. The borrowing table ties internally (section 1). |
| F12 Segment forensics | N.A. | No segment assets, liabilities or results. Customer segments are named only (lines 160-161). |
| F13 Board outcome beyond results | N.A. | The release reports no board meeting outcome, AGM, director or fund-raising item. |
| F14 Drafting inconsistencies | FINDING | A3-04 (basis unstated, review status unstated, postal-code typo). Grammar slip at line 161-162 ("Company has 4 manufacturing plants are situated") is noted, not a separate finding. |
| F15 Entity list diffs | N.A. | No consolidation list and no prior extract. |
| F16 Dropped and reframed disclosures / KPI definitions | FINDING | No prior release to diff for dropped metrics (first review). Findings on framing and KPI definitions: A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-13. |
| F17 Silence audit | FINDING | Applied to the release as management's chosen narrative, against the F6 register and the operator watch list. A3-11, A3-12. Silence count 1 (floor). |

GATE A3: pass. No blank checks.

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| New manufacturing plant goes on stream and contributes revenue | H2FY27 (1 Oct 2026 to 31 Mar 2027) | line 106-107 (R126, R127, R136) | underway (P&M installed, line 135; not commissioned) |
| Plant and Machinery installed at the new facility | by 27 Oct 2026 (release date) | line 135 (R117) | completed (installation step only) |
| Growth momentum continues, domestic and export | FY27 (undated) | line 105 (R125) | initiated (statement of expectation, unquantified) |
| Export market gains momentum as global macros normalise | undated, conditional on an external event | line 110 (R128) | initiated (conditional expectation) |

## 5. WHAT WAS NOT DISCUSSED (F17, vs operator watch list)

| watch item | in the release? | ref | consecutive quarters of silence |
|---|---|---|---|
| 1. Volume growth vs metal-price pass-through | No. No volume, no copper/aluminium price comment. Only "crude price volatility" | line 108 | 1 (floor) |
| 2. Order book | Yes, ~Rs 829 Cr, undefined, no inflow | line 133 | 0 (definition open, A3-07) |
| 3. EBITDA per unit / margin | Margin yes (10.0%, falling); per unit no; cause of the fall not explained | line 116 | 1 (floor) on the cause and per unit |
| 4. Working capital days and OCF | Receivable days only (~59); inventory days, payable days and OCF absent | line 129 | 1 (floor) |
| 5. Capacity expansion and funding | P&M installed; capacity, capex Rs, commissioning date, funding absent; borrowing table given | lines 135, 139-155 | 1 (floor) on capex and capacity |
| 6. Customer mix (utilities, EPC, exports) | Segments named; exports ~Rs 56 Cr H1; no utilities/EPC split | lines 127, 131, 160-161 | 1 (floor) on the split |
| 7. Promoter holding and pledge | No (outside press-release scope) | none | 1 (floor); check the shareholding filing |
| F6: new plant from H2 | Yes | lines 106-107, 135 | 0 |
| F6: export momentum | Yes, conditional | line 110 | 0 |

## 6. NOTES FOR A4

Questions follow from A3-01, A3-02 (tracker items) and A3-03, A3-05, A3-07, A3-09, A3-10, A3-11, A3-12 (management questions). The highest priority is the cause of the Q2 margin fall (A3-05). The observation that separates the two readings is volume or per-km EBITDA. Next is the finance-cost rise against lower period-end debt (A3-09). Then the unitemised H1 cash uses of about Rs 77 Cr (A3-11).

```yaml
stage: A3-forensics
company: "DYCL"
quarter: "q2fy27"
doctype: "pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/dycl-q2fy27/work/forensics_pressrelease_dycl_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: PASS
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "106-107, 135", classification: "FORWARD-SIGNAL", implication: "New plant to contribute from H2FY27; P&M installed, not commissioned; no capacity, capex or date given; Q2 depreciation +21% QoQ suggests partial capitalisation; H2 depreciation, finance cost and start-up cost step up"}
  - {id: "A3-02", check: "F6", line: "105", classification: "FORWARD-SIGNAL", implication: "Unquantified growth commitment; test H2FY27 revenue YoY vs H2FY26 654.2 (derived FY26 minus H1FY26)"}
  - {id: "A3-03", check: "F7", line: "110, 108", classification: "AMBIGUOUS", implication: "Export momentum conditional on global macros, undated; exports ~56 Cr = 7.9% of H1 revenue; crude mention points to polymer cost pressure"}
  - {id: "A3-04", check: "F14", line: "24, 33, 88", classification: "NEUTRAL-FACT", implication: "Standalone/consolidated basis and review status unstated; postal-code typo; confirm basis from results filing before tracker use"}
  - {id: "A3-05", check: "F16", line: "67, 74, 81, 116, 122, 108", classification: "AMBIGUOUS", implication: "Headline and H1-first tiles lead while Q2 OPM 10.0% is the lowest shown (-90 bps QoQ, -100 bps YoY), PAT -11.6% QoQ; cause unexplained: metal pass-through vs price/input pressure vs start-up cost; volume or per-km EBITDA separates"}
  - {id: "A3-06", check: "F16", line: "115-120", classification: "NEUTRAL-FACT", implication: "Operating Profit undefined; arithmetic shows EBITDA excluding other income in all six periods"}
  - {id: "A3-07", check: "F16", line: "133", classification: "AMBIGUOUS", implication: "Order book ~829 Cr undefined (GST, L1, price-variation), no inflow or prior; cover 0.61x TTM revenue (~7.3 months)"}
  - {id: "A3-08", check: "F16", line: "147-155", classification: "NEUTRAL-FACT", implication: "Net Debt includes off-BS LC creditors; on-BS moved from net cash 18.4 (Mar) to net debt 4.1 (Sep); track both"}
  - {id: "A3-09", check: "F16", line: "117, 145, 147, 149", classification: "AMBIGUOUS", implication: "Finance cost +45% QoQ while period-end on-BS debt halved and average period-end debt flat; annualised 31% of average on-BS debt; likely LC/discounting charges, intra-quarter peaks or interest no longer capitalised"}
  - {id: "A3-10", check: "F16", line: "145, 149, 153", classification: "AMBIGUOUS", implication: "WC loans -32.1 QoQ funded mostly by cash drawdown 13.8 and LC creditors +13.1; real WC release vs quarter-end repayment; check average utilisation and Q3 period-end"}
  - {id: "A3-11", check: "F17", line: "122, 118, 153-155", classification: "AMBIGUOUS", implication: "H1 uses ~77 Cr (cash earnings 53.4 + net debt rise 23.6) not itemised; term loans 2.3 so plant funded from accruals and cash; no OCF or capex disclosed"}
  - {id: "A3-12", check: "F17", line: "127, 129, 131, 160-161", classification: "AMBIGUOUS", implication: "Silent on volume vs metal price, per-unit EBITDA, inventory/payable days, OCF, plant capex and capacity, utilities/EPC split, promoter pledge; silence count 1 (floor)"}
  - {id: "A3-13", check: "F16", line: "129", classification: "NEUTRAL-FACT", implication: "Receivable days ~59 defined on trailing six-month gross sales; fair like-for-like basis; only WC day count given; no prior"}
forward_signals: ["A3-01", "A3-02"]
ambiguous: ["A3-03", "A3-05", "A3-07", "A3-09", "A3-10", "A3-11", "A3-12"]
commitments:
  - {commitment: "New manufacturing plant goes on stream and contributes revenue", implied_date: "H2FY27 (Oct 2026 - Mar 2027)", ref: "line 106-107", status_word: "underway"}
  - {commitment: "Plant and Machinery installed at new facility", implied_date: "by 2026-10-27", ref: "line 135", status_word: "completed"}
  - {commitment: "Growth momentum continues, domestic and export", implied_date: "FY27, undated", ref: "line 105", status_word: "initiated"}
  - {commitment: "Export market gains momentum as global macros normalise", implied_date: "undated, conditional", ref: "line 110", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Press release, one unlabelled basis, so statement checks F1-F5, F9, F11-F13, F15 are N.A. The forensic content sits in KPI framing and the borrowing table. Three facts belong together: Q2 margin is the lowest of six periods shown, Q2 finance cost jumped 45% while period-end on-balance-sheet debt halved, and H1 absorbed about Rs 77 Cr of unitemised cash with term debt near zero. Read together, the period-end debt table likely flatters the funding position: working capital loans were repaid from cash and moved into LC credit at quarter end, while the finance-cost line shows intra-quarter usage or rising LC charges. The new plant is self-funded so far, and its H2 ramp adds working capital need on a thinner cash buffer (33.2). Margin cause is open: metal pass-through would leave per-unit EBITDA intact; polymer cost or start-up cost would not. Volume disclosure separates the readings. F17 applied to the release as management's chosen narrative; silence counts are floors because no prior quarter is in the pipeline. R076/R077 line cite is 140; values print at 141."
```
