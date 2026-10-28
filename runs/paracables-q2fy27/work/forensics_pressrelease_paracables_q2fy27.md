# A3 FORENSIC NOTES: PARACABLES Q2 FY27, doctype presentation (Reg 30 press release, 3 pages)

Inputs read: A1 structured (R001-R157), A1 fulltext (127 lines), A2 ledger (157 IDs, gate_a2 pass), Notion snapshot sections only (line 11 properties; lines 210-215; 489-506; 612-622; 644-651; 735-737). No source PDF, nothing under inputs/. Prior-quarter fulltext: none. Notion content is memory to weigh, not anchored evidence; every place it is used is marked [MEMORY].

## 0. LEDGER RECONCILIATION

- Ledger IDs: 157. Structured IDs read: 157. Each read at its cited fulltext line. ledger_reconciled_pct = 100.
- Line drift (cited line vs actual quote line, no value impact): R124 cited 75, quote sits at 76-77; R119 cited 113, text spans 111-114; R122 cited 118, emails sit at 122; R123 cited 125, heading at 124; R115 Khushkhera sits at 115. All values match.
- CORRECTED_FROM_IMAGE rows (R041-R048, R057-R064, R089, R090, R092-R097): image not available to A3 (no source access). Arithmetic cross-check performed instead:
  - Operating margin R041-R048 ties to Operating Profit / Revenue from Operations: 40.9/560.4 = 7.30%; 34.7/529.4 = 6.55%; 5.7/427.6 = 1.33%; 75.6/1089.8 = 6.94%; 20.9/878.5 = 2.38%. Consistent.
  - EBITDA margin R057-R064 ties to EBITDA / Total Income (not revenue): 44.7/564.2 = 7.92%; 37.8/532.5 = 7.10%; 25.6/447.5 = 5.72%; 82.5/1096.7 = 7.52%; 58.8/916.4 = 6.42%. Consistent on that basis (see A3-07).
  - Export R090: 158.1/560.4 = 28.21%, ties to R091/R093/R099. Mix R092-R097 sums to 100.0. Domestic R098 = 100 - 28.2.
  - Order book R089 (Rs 731 Cr): no arithmetic tie available. Stays as A1 corrected it.
- R147 (email, OCR_UNVERIFIED): immaterial; no finding rests on it.
- Internal tie-outs: H1 = Q1 + Q2 for Revenue (1089.8), Total Income (1096.7), Operating Profit (75.6), EBITDA (82.5), PAT (43.9), EPS (1.38). EBITDA minus Operating Profit equals Total Income minus Revenue in every column (3.8 / 3.1 / 19.9 / 6.9 / 37.9), so the release's Other Income is internally consistent. Growth rates match within rounding of one-decimal inputs (Operating Profit YoY 616.5% vs 617.5% on rounded figures; PAT YoY 82.8% vs 82.0%; both inside the rounding band).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
| --- | --- | --- | --- | --- | --- | --- |
| A3-01 | F6 | R127, R041 | 82, 92 | "Our priorities remain clear: strengthening our core business, restoring operating profitability" | FORWARD-SIGNAL | The CEO concedes operating profitability is not yet restored at a 7.3% operating margin (line 92), while the headline reads "STRONG Q2 FY27 PERFORMANCE" (line 64). Management's own benchmark sits above 7.3%. No target level, no date. A4: ask the margin that counts as "restored" and by when. |
| A3-02 | F6 | R128, R101, R114, R115 | 83-84, 114 | "Investments in specialized manufacturing capabilities will enable us to address more technically demanding applications" | FORWARD-SIGNAL | Undated, unquantified capex commitment. The profile still lists "two state-of-the-art manufacturing facilities" (line 114), Dharuhera and Khushkhera. The new plant (Narmadapuram [MEMORY]) is not named, dated or sized. The thesis capacity gate gets no milestone from this release. |
| A3-03 | F6 | R089, R130, R143, R155 | 101 | "Order book stood at approximately Rs 731 crore as of September 30, 2026, providing visibility into near-term" | AMBIGUOUS | Rs 731 Cr = 1.30x Q2 revenue (560.4), about four months of sales. Basis not stated (unexecuted vs total, GST, product vs EPC, domestic vs export). [MEMORY] Q1 FY27 order book Rs 615 Cr: if same basis, +18.9% QoQ and implied Q2 inflow about Rs 676 Cr, book-to-bill about 1.2. Basis must be confirmed before the trend counts. |
| A3-04 | F7 | R127, R090, R091, R124 | 82-83, 75, 103 | "expanding our international presence prudently" / "respond decisively to changing market conditions" | AMBIGUOUS | A qualifier on export growth while exports are Rs 158.1 Cr, 28.2% of revenue (line 103). The "changing market conditions" are not named. [MEMORY] FY26 margins were hit by tariffs. Lean bear: the word "prudently" may pre-announce slower export growth or export margin pressure. A4: ask which conditions and what "prudently" limits. |
| A3-05 | F10 | R065-R072, R081-R088 | 95, 97 | "EPS (Rs) 0.74 0.64 15.6% 0.44 68.2%" | FORWARD-SIGNAL | EPS growth lags PAT growth: QoQ 15.6% vs 23.0%, YoY 68.2% vs 82.8%. Implied weighted shares (PAT/EPS): Q2 FY27 about 32.7 Cr (band 32.5-32.9), Q1 FY27 about 30.8 Cr (30.5-31.0), Q2 FY26 about 30.2 Cr (29.9-30.6). That is about +6% QoQ and +8% YoY. Line 97 does not say basic or diluted. A weighted average understates the period-end count, and [MEMORY] promoter warrants (72 lakh, 25% upfront) are still to convert. Q3 EPS dilutes further at flat PAT. A4 runs the warrant cross-check. |
| A3-06 | F14 | R146, R148 | 38, 87 | "Unaudited (Standalone and Consolidated) Financial Results" vs "SNAPSHOT (STANDALONE)" | NEUTRAL-FACT | The cover letter announces consolidated results; the release carries standalone only. S-vs-C decomposition (F2/F3) cannot run from this document. [MEMORY] three foreign subsidiaries are dormant, so the gap is expected to be immaterial. A4 confirms from the results filing. |
| A3-07 | F14 | R041-R048, R057-R064, R073-R080, R025-R032 | 92, 94, 96 | "EBITDA Margin (incl. OI) 7.9% 7.1% 80 bps 5.7% 220 bps" | NEUTRAL-FACT | Margin denominators differ and are not disclosed. Operating margin uses revenue; EBITDA and PAT margins use Total Income. On revenue, Q2 EBITDA margin is 7.98% (prints as 8.0%) and Q2 FY26 is 5.99%, so YoY expansion is about 200 bps, not 220. H1 PAT margin expansion is about 35 bps on revenue vs 50 bps printed. Prior-year Total Income was inflated by other income, so the Total Income base flatters YoY margin deltas by about 15-20 bps. H1 PAT margin prints "4%" (line 96) at lower precision than the rest of the row. Small, but a drafting data point. |
| A3-08 | F16 | R025-R040, R049-R056 | 89-91, 93 | "Total Income 564.2 532.5 6.0% 447.5 26.1%" | FORWARD-SIGNAL | Derived Other Income (Total Income less Revenue; ties exactly to EBITDA less Operating Profit): Q2 FY27 3.8, Q1 FY27 3.1, Q2 FY26 19.9; H1 FY27 6.9 vs H1 FY26 37.9. In Q2 FY26, other income was 78% of EBITDA; in Q2 FY27 it is 8.5%. Earnings quality has flipped to operations. Other income no longer supports PAT, so PAT now tracks the operating margin one for one. [MEMORY] about Rs 98-123 Cr equity was raised in mid-2026, but no treasury income appears (OI 3.8 Cr). The cash is likely in working capital or debt paydown. A4 tests this against the filing's cash flow. |
| A3-09 | F16 | R007, R011, R036, R037 | 64, 69, 91 | "616.5% YoY" (tile) on "5.7" Q2 FY26 base | NEUTRAL-FACT | The headline tile features the growth rate with the lowest base (Rs 5.7 Cr). The same release's PAT YoY is 82.8% because other income fell by Rs 16.1 Cr. A reader should anchor on the PAT and margin lines, not the tile. No prior deck to diff, so dropped-metric and baseline-change tests cannot run. |
| A3-10 | F16 | R092-R097, R121, R157 | 105, 110 | "Power Cables 55.9% \| Export Sales 28.2% \| House Wires 6.0% \| Railway Cables 3.2% \| Telecom Cables 4.2% \| Others 2.5%" | AMBIGUOUS | The mix chart mixes a geography slice (Export Sales) with product slices. The product content of Rs 158.1 Cr exports is hidden. Telecom (about Rs 23.5 Cr) and Railway (about Rs 17.9 Cr) are small against the "diverse portfolio" claim (line 110). The "higher-value segments" claim (line 84) cannot be tracked on this chart. A4: ask for a product split of exports and a value-added share. |
| A3-11 | F14 | R020, R021, R036, R044 | 89, 92 | "427.6 31.1%" / "1.3% 600 bps" | AMBIGUOUS | [MEMORY] Notion Key Notes (26-Oct, from the results filing) record revenue YoY +30.9% and Q2 FY26 operating margin 1.45%. The release prints 31.1% and 1.3%. Implied comparators differ: Q2 FY26 revenue about 428.1 vs 427.6, operating profit about 6.2 vs 5.7. On a 6.2 base, operating profit YoY is about 560%, not 616.5%. Either the analyst's definition differs or the release comparative differs from the filing. A4 reconciles against the filed results before any number is reused. |
| A3-12 | F17 | R124, R129 | 76-77, 85 | "financial discipline and operational resilience" / "disciplined capital allocation" | AMBIGUOUS | The release claims financial discipline but is silent on every cash item on the Notion checklist: receivables, operating CFO, net debt, use of proceeds, warrant exercise, other-expense reversal, Narmadapuram date. [MEMORY] the same-day filing shows H1 CFO of minus Rs 31.89 Cr. Conservative bias: the discipline claim is unsupported in this document. See silence table. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
| --- | --- | --- |
| F1 Zero-value standing lines | N.A. | Press release, no statutory template; ledger zero_standing = 0. |
| F2 Standalone vs consolidated | N.A. | Only the standalone snapshot is shown (line 87). Consolidated figures are absent, so no gap can be computed. The omission is logged under F14 (A3-06). |
| F3 Shell-entity detection | N.A. | No consolidated cost lines on the document. |
| F4 Unaudited contribution ratio | N.A. | No auditor paragraph; results unaudited (line 38); ledger auditor_paras = 0. |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph; no prior extract to diff. |
| F6 Forward-commitment mining | FINDING | Lexicon hit only "will be" (line 80, industry statement). Wider forward sweep (R124-R130): 7 undated commitments. A3-01, A3-02, A3-03. |
| F7 Hedge phrase mining | FINDING | Lexicon hit "subject to" at line 125 is boilerplate safe harbour, so no finding on it. Non-lexicon qualifiers "prudently" (line 83) and "changing market conditions" (line 75) form A3-04. |
| F8 Tax forensics | N.A. | No PBT, tax or deferred tax line on the release. Context only: PAT/EBITDA conversion is stable at 52-55% (24.2/44.7 = 54.1%; 13.3/25.6 = 52.0%), so no tax anomaly is visible. ETR goes to the results filing. |
| F9 OCI forensics | N.A. | No OCI line. |
| F10 Share count and dilution | FINDING | Implied weighted share count is up about 6% QoQ; basic or diluted is not labelled. A3-05. |
| F11 Reserves / net worth tie-out | N.A. | No net worth, paid-up capital or reserves figure on the release. |
| F12 Segment forensics | N.A. | No statutory segment assets or liabilities. The revenue-mix chart is reviewed under F16 (A3-10). |
| F13 Board outcome | N.A. | Not a board outcome letter (ledger agenda_items = 0). The board meeting time is not on the document; signature 20:42:52 IST on 26-Oct (line 49). |
| F14 Drafting inconsistencies | FINDING | Cover letter vs content scope (A3-06), undisclosed margin denominators and "4%" precision (A3-07), comparator mismatch vs memory (A3-11). Cumulatively a minor governance data point. |
| F15 Entity list diffs | N.A. | No consolidation list on the release; no prior ledger. |
| F16 Dropped / reframed disclosures | FINDING | No prior deck, so the dropped-metric diff cannot run (stated, not assumed clean). In-document reframing: other-income collapse behind the tiles (A3-08), low-base headline tile (A3-09), mixed-axis mix chart (A3-10), order-book basis unstated (A3-03). |
| F17 Silence audit | FINDING | Run against the orchestrator-supplied Notion checklist, adapted to a press release (silence weighs less than on a call). 9 of 13 checklist items are not addressed. A3-12 and the table below. |

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref | status word |
| --- | --- | --- | --- | --- |
| C1 | Restore operating profitability | none stated | line 82, R127 | underway (implied by "restoring"; not completed) |
| C2 | Strengthen the core business | none stated | line 82, R127 | not stated |
| C3 | Expand international presence "prudently" | none stated | lines 82-83, R127 | underway (implied by "expanding") |
| C4 | Enhance product mix | none stated | line 83, R127 | not stated |
| C5 | Investments in specialized manufacturing capabilities to reach higher-value segments | none stated | lines 83-85, R128 | not stated (no initiated / underway / completed word) |
| C6 | Disciplined capital allocation and prudent risk management | none stated | line 85, R129 | ongoing |
| C7 | Order book Rs 731 Cr gives near-term execution visibility | about 4 months (1.30x Q2 revenue) | line 101, R089/R130 | n/a (status claim) |
| C8 | Sustainable growth, financial discipline, operational resilience | none stated | lines 76-77, R124 | ongoing |

No commitment in this release carries a date. None can enter the Role 5 promise-vs-delivery tracker as dated. C1 and C5 are the candidates to convert into dated questions.

## 4. WHAT WAS NOT DISCUSSED (F17)

Quarters of silence counts only pipeline-read documents for this ticker. This is the first quarterly-pipeline document, so the floor is 1. Memory context is noted, never counted.

| # | checklist item (Notion source line) | addressed in release? | quarters of silence | note |
| --- | --- | --- | --- | --- |
| 1 | Receivables / receivable days (213; 493; 648; 737 Q1, Q3) | NO | 1 | [MEMORY] filing gives Rs 394.79 Cr. The release omits the thesis's cleanest metric. |
| 2 | Operating CFO, Trigger B (622; 649; 737 Q3) | NO | 1 | [MEMORY] H1 CFO minus Rs 31.89 Cr. A deteriorating metric left out of a "financial discipline" release. |
| 3 | Op EBITDA margin trajectory (212; 496; 650) | YES | 0 | Line 92: 7.3% vs 6.6% Q1 vs 1.3% Q2 FY26. No guidance number (8E Q4 still unanswered). |
| 4 | Other Expenses +331 bps reversal (494; 737 Q2) | NO | 1 | No cost lines on the release. |
| 5 | Preferential issue terms / use of proceeds (214; 495; 617; 647) | NO | 1 | Dilution shows only through EPS (A3-05). |
| 6 | Warrant exercise pace (615; 651) | NO | 1 | Not on the release. |
| 7 | Allottee identity, Trigger A (614; 621; 646) | NO | 1 | [MEMORY] already resolved benign. Low weight. |
| 8 | Narmadapuram hard date, CWIP, long-lead equipment (737) | NO | 1 | Only generic line 83; facility list (line 114) shows two plants. [MEMORY] the filing is also silent on the date. |
| 9 | Keyman insurance / OI repeatability (498) | PARTIAL | 0 | Derived OI 3.8 vs 19.9 YoY (lines 89-90). The support is gone, which answers the question in practice. |
| 10 | Promoter pledge, FII+DII holding (497) | NO | 1 | Outside release scope. Low weight. |
| 11 | Order book trend ([MEMORY] Q1 Rs 615 Cr) | YES | 0 | Line 101, Rs 731 Cr; basis unstated (A3-03). |
| 12 | Q1 FY27 results gate (616) | SUPERSEDED | n/a | Q2 numbers present. |
| 13 | Promoter background check / Role 2 thesis (215) | N.A. | n/a | Internal pipeline item, not a disclosure. |

## 5. FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: A3-01, A3-02, A3-05, A3-08. AMBIGUOUS: A3-03, A3-04, A3-10, A3-11, A3-12.

```yaml
stage: A3-forensics
company: "PARACABLES"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-paracables-q2fy27-a220cd/runs/paracables-q2fy27/work/forensics_pressrelease_paracables_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "82 'restoring operating profitability'; 92", classification: "FORWARD-SIGNAL", implication: "CEO concedes 7.3% op margin is not 'restored'; target level and date unstated"}
  - {id: "A3-02", check: "F6", line: "83-84 'Investments in specialized manufacturing capabilities will enable'; 114", classification: "FORWARD-SIGNAL", implication: "Undated unquantified capex; profile lists two plants; Narmadapuram not named or dated"}
  - {id: "A3-03", check: "F6", line: "101 'Order book stood at approximately Rs 731 crore'", classification: "AMBIGUOUS", implication: "1.30x Q2 revenue, about 4 months; basis unstated; +18.9% QoQ vs memory Rs 615 Cr only if same basis"}
  - {id: "A3-04", check: "F7", line: "82-83 'expanding our international presence prudently'; 75", classification: "AMBIGUOUS", implication: "Qualifier on exports (28.2%, Rs 158.1 Cr) plus unnamed 'changing market conditions'; possible export slowdown"}
  - {id: "A3-05", check: "F10", line: "97 'EPS (Rs) 0.74 0.64 15.6%'; 95", classification: "FORWARD-SIGNAL", implication: "Implied weighted shares about +6% QoQ, +8% YoY; basic/diluted unlabelled; period-end count and warrants dilute Q3 further"}
  - {id: "A3-06", check: "F14", line: "38 'Standalone and Consolidated'; 87 '(STANDALONE)'", classification: "NEUTRAL-FACT", implication: "Consolidated not carried; S-vs-C not computable from release"}
  - {id: "A3-07", check: "F14", line: "94 'EBITDA Margin (incl. OI) 7.9%'; 92; 96 '4%'", classification: "NEUTRAL-FACT", implication: "EBITDA/PAT margins on Total Income, op margin on revenue, undisclosed; YoY EBITDA delta about 200 bps on revenue vs 220 printed"}
  - {id: "A3-08", check: "F16", line: "90 'Total Income 564.2 532.5 6.0% 447.5'; 89, 91, 93", classification: "FORWARD-SIGNAL", implication: "Derived OI 3.8 vs 19.9 YoY (78% to 8.5% of EBITDA); PAT now operating; no treasury income from equity raise, cash likely in WC"}
  - {id: "A3-09", check: "F16", line: "69 '616.5% YoY'; 91 '5.7'", classification: "NEUTRAL-FACT", implication: "Headline tile rides a Rs 5.7 Cr base; PAT +82.8% is the cleaner growth figure"}
  - {id: "A3-10", check: "F16", line: "105 'Export Sales 28.2%'", classification: "AMBIGUOUS", implication: "Mix chart mixes geography with product; export product content and value-added share untrackable"}
  - {id: "A3-11", check: "F14", line: "89 '427.6 31.1%'; 92 '1.3%'", classification: "AMBIGUOUS", implication: "Memory from filing shows +30.9% and 1.45%; comparator op profit about 6.2 vs 5.7; reconcile to filed results"}
  - {id: "A3-12", check: "F17", line: "76-77 'financial discipline'; 85 'disciplined capital allocation'", classification: "AMBIGUOUS", implication: "Silent on receivables, CFO, proceeds, warrants, other expenses, Narmadapuram; 9 of 13 checklist items unaddressed"}
forward_signals: ["A3-01", "A3-02", "A3-05", "A3-08"]
ambiguous: ["A3-03", "A3-04", "A3-10", "A3-11", "A3-12"]
commitments:
  - {commitment: "Restore operating profitability", implied_date: "none stated", ref: "line 82 R127", status_word: "underway (implied)"}
  - {commitment: "Strengthen the core business", implied_date: "none stated", ref: "line 82 R127", status_word: "not stated"}
  - {commitment: "Expand international presence prudently", implied_date: "none stated", ref: "lines 82-83 R127", status_word: "underway (implied)"}
  - {commitment: "Enhance product mix", implied_date: "none stated", ref: "line 83 R127", status_word: "not stated"}
  - {commitment: "Investments in specialized manufacturing capabilities for higher-value segments", implied_date: "none stated", ref: "lines 83-85 R128", status_word: "not stated"}
  - {commitment: "Disciplined capital allocation and prudent risk management", implied_date: "none stated", ref: "line 85 R129", status_word: "ongoing"}
  - {commitment: "Order book Rs 731 Cr gives near-term visibility", implied_date: "about 4 months (1.30x Q2 revenue)", ref: "line 101 R089 R130", status_word: "n/a"}
  - {commitment: "Sustainable growth, financial discipline, operational resilience", implied_date: "none stated", ref: "lines 76-77 R124", status_word: "ongoing"}
gate_a3: pass
blank_checks: []
analyst_note: "Press release, standalone only. Two signals matter. First, earnings quality flipped. Other income, derived as Total Income less Revenue (ties exactly to EBITDA less Operating Profit), fell from 19.9 to 3.8 Cr YoY. In Q2 FY26 it was 78% of EBITDA; now 8.5%. The 616.5% tile is base effect; the 82.8% PAT growth is the cleaner number. No treasury income shows despite the mid-2026 equity raise, so the cash likely went into working capital or debt; A4 tests this against the filing's cash flow. Second, dilution: EPS lags PAT by about 7 points QoQ. Implied weighted shares rose about 6% QoQ, and the period-end count plus unconverted warrants mean Q3 EPS dilutes further at flat PAT. The CEO's phrase 'restoring operating profitability' concedes 7.3% is not the target; ask the number and date. The release is silent on every cash item on the Notion checklist while claiming financial discipline. Memory shows Q2 FY26 op margin 1.45% vs 1.3% printed; reconcile to the filing. CORRECTED_FROM_IMAGE margin and mix rows are arithmetically consistent; A3 did not see the image."
```
