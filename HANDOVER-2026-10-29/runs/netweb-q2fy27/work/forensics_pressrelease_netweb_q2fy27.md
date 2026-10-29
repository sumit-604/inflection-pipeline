# A3 FORENSIC NOTES: NETWEB q2fy27, doctype presentation (press release, label "pressrelease")

Agent: A3 forensic notes | model: claude-opus-5-5 | run date 2026-10-28
Inputs read: A1 structured (R001-R170), A1 fulltext (175 lines), A2 ledger (170 R rows + 4 M rows), Notion checklist excerpt (memory, not evidence).
Not read: source PDF, inputs/. Prior-quarter fulltext: not available (no prior NETWEB run folder). Every cross-quarter diff (F5, F15, F16 cross-deck) is therefore untestable in this run and is stated as such.
Unit: INR Millions as printed. All derived figures use only printed numbers and are marked [DERIVED].

## 0. LEDGER RECONCILIATION

Rows in ledger: 174 (R001-R170 plus M001-M004). Rows read at cited fulltext line: 174. Reconciled: 100%.

Line-cite notes (not findings; the values are present, the cited line drifts):
| Row(s) | cited line | value actually at | note |
|---|---|---|---|
| R030, R039, R048, R057, R066, R075 | 94, 96, 98, 100, 102, 104 | 93, 94, 95, 96, 97, 98 | LAYOUT_SHIFT. A1 paired via raw mode. A3 confirms each pairing arithmetically: 13,233/3,037 = +335.7%; 1,973/455 = +333.6% (334.0% printed, rounding); 1,367/314 = +335.4% (334.8% printed, rounding); 23.54/5.55 = +324.1%; EBITDA margin 14.91% vs 14.98% = -7 bps ((6 bps) printed); PAT margin 10.23% vs 10.31% = -8 bps ((9 bps) printed). Pairing holds. |
| R104, R105 | 28 | 25 | exchange names on line 25; line 28 holds scrip codes |
| R109 | 65 | 66 | "High-end Computing Solutions (HCS)" |
| R137 | 66 | 67 | "meeting held on 24th October 2026" |
| R102, R150 | 169 | 167 | "Founded in 1999" |

MISSING_FROM_STRUCTURED rows, read at fulltext:
- M001 line 160: "a strengthened balance sheet following the recent capital raise and a robust order book". Used in FN07.
- M002 line 159: "sustained investment in innovation and a chip-agnostic design philosophy". Used in FN11.
- M003 line 63: "Netweb's H1 FY27 profits exceeds full-year FY26". Tested: 2,220 (line 100) > 2,058 (line 100). True on printed figures.
- M004 line 116: "another record quarter ... highest-ever quarterly Revenue from Operations and Profit After Tax". Tested by elimination: H2 FY26 revenue = 21,836 - 6,049 = 15,787 and H2 FY26 PAT = 2,058 - 619 = 1,439 [DERIVED]. A single FY26 quarter above Q2 FY27 (13,233 / 1,367) would force the other H2 FY26 quarter below 2,554 revenue / 72 PAT, under the Q2 FY26 print (3,037 / 314). The record claim is consistent with printed figures. No finding.

Other in-document ties checked and clean: all QoQ / YoY / H1 YoY percentages recompute within rounding; PAT margin on Total Income (R161) recomputes for all six columns; H1 revenue and H1 PAT equal Q1 + Q2 exactly. The exceptions are Total Income and Op EBITDA (FN04).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F6 | R124, R165, R126 | 127-128, 154-155 | "providing strong revenue visibility for the coming quarters" | AMBIGUOUS | Zero F6 lexicon hits in the document. Every forward statement is undated. The Role 5 tracker gets no dated promise to score. A4 asks for the quarter-wise execution schedule of the 26,290 Mn book and the expected conversion date of the 6,525 Mn L1. |
| FN02 | F10 | R055-R063, R073-R081 | 100, 104 | "PAT2 1,367 ... 853" / "Diluted EPS ()*,2 23.54 ... 14.98" | FORWARD-SIGNAL | [DERIVED] implied weighted diluted shares (PAT/EPS): Q2 FY26 56.58 Mn, Q1 FY27 56.94 Mn, Q2 FY27 58.07 Mn (+1.98% QoQ). EPS growth 324.2% trails PAT growth 334.8% by 10.6 pp. The 12,000 Mn raise (line 130) is in the count for part of Q2 only. Q3 carries the full post-raise count, so EPS grows slower than PAT again in Q3. Basic EPS not printed, so the basic vs diluted spread is not testable. |
| FN03 | F12 | R093-R097, R016, R120 | 125-126, 85, 166 | "contributing 7,731 Mn (58.4% of Revenue from Operations)" / "contributing 2,482 Mn and 2,448 Mn" | AMBIGUOUS | [DERIVED] Q1 AI Systems = 12,836 - 7,731 = 5,105 Mn, 62.3% of Q1 revenue 8,197. Q2 AI share 58.4%: down 3.9 pp QoQ. AI grew +51.4% QoQ; non-AI revenue grew +77.9% QoQ (3,092 to 5,502). Three named lines sum to 12,661; 572 Mn (4.3%) sits in HPS, Data Centre Servers, HCI and anything else, unsplit. No segment assets or liabilities printed. A4 asks what drove the non-AI surge (one large HPC / private cloud delivery or broad) and what the 572 Mn residual holds. |
| FN04 | F14 | R019-R027, R037-R054 | 92, 96, 98 | "Total Income 13,361 ... 8,282 ... 21,591" / "Op EBITDA1,2 1,973 ... 1,205 ... 3,230" / "Op EBITDA Mg (%)2 14.9% ... 14.7% ... 15.1%" | AMBIGUOUS | [DERIVED] H1 does not equal Q1 + Q2 on two lines. Total Income: 8,282 + 13,361 = 21,643 vs 21,591 printed (-52). Op EBITDA: 1,205 + 1,973 = 3,178 vs 3,230 printed (+52). Revenue and PAT tie exactly. So a 52 Mn item moves between other income and operating profit across columns. The printed H1 margin 15.1% sits above both quarters (14.7%, 14.9%), which additive figures cannot produce. On the additive basis H1 Op EBITDA margin is 14.83%, a 10 bps fall vs H1 FY26 14.93%, not the printed "14 bps" rise. A4 asks which column carries the reclassification, what the 52 Mn item is (forex, scrap, interest?), and which basis the Q3 print will use. |
| FN05 | F14 | R151, R152 | 35, 67 | "the unaudited financial results for the quarter and half year" / "took on record the unaudited Financial Results" | AMBIGUOUS | The press release never states standalone or consolidated. No limited-review mention. F2/F3/F4 cannot run on this document. A4 confirms the basis against the results filing, more so if a new overseas subsidiary enters consolidation in H2. |
| FN06 | F14 | R153-R157, R159-R161 | 96-104, 108-109 | "Op EBITDA Mg (%)2" / "2.Profit after Tax (PAT) margin is a percentage of `Profit for the period/year' divided by `Total Income'" | NEUTRAL-FACT | Marker 2 defines PAT margin only, yet it is attached to Op EBITDA, Op EBITDA Mg, PAT and Diluted EPS. The Op EBITDA margin definition actually sits in footnote 1. Immaterial alone. With FN04 and the unsigned Net Debt bracket (R170), it is a cumulative drafting-care data point. |
| FN07 | F16 | R014, R170, R100, M001 | 80, 130, 160 | "Net Debt was (136 Mn) as of 30th September'26" / "successfully raised 12,000 Mn" / "a strengthened balance sheet following the recent capital raise" | FORWARD-SIGNAL | [DERIVED] Net debt is within 136 Mn of zero after a 12,000 Mn raise in the same quarter: 1.1% of the raise. Under either sign of the undefined bracket, the raise is absorbed (working capital and/or debt repayment), not held as a cash cushion. The document prints no CFO, gross debt, inventory or receivables. The "strengthened balance sheet" claim rests on this one number. H2 working capital growth must come from operating cash or new borrowing. A4 asks for gross debt, cash, inventory and H1 CFO, and the bracket sign. |
| FN08 | F16 | R015, R098, R099, R165, R124 | 83, 127-128 | "Order Book: 26,290 Mn as of 30th September'26" / "an additional L1 position of 6,525 Mn" | FORWARD-SIGNAL | [DERIVED] Closing order book = 1.99 quarters of Q2 revenue. H2 at the flat Q2 run-rate needs 26,466 Mn: 100.7% of the closing book. H2 revenue above Q2 run-rate needs L1 conversion (6,525 Mn; book plus L1 = 2.48 quarters) and orders won and delivered inside the half. No book-to-bill, no inflow figure, no opening book, no definition (gross or net of GST; pending only or including executed). Q3 lumpiness risk is visible from this document alone. |
| FN09 | F16 | R101, R126, R127 | 154-155 | "Our active pipeline of 1,11,518 Mn provides significant visibility into potential business opportunities" | AMBIGUOUS | [DERIVED] Pipeline = 4.24x order book, 3.40x book plus L1, 5.1x FY26 revenue. Undefined: no stage, probability, horizon or customer type. "potential" carries the hedge. A4 asks for the definition and the historic pipeline-to-order conversion rate. |
| FN10 | F16 | R016-R018, R163, R094, R164 | 85-86, 125 | "its contribution to the company's operating revenue increased to 59.9% during the same period" / "7,731 Mn (58.4% of Revenue from Operations)" | AMBIGUOUS | Key Business Highlights use the H1 basis to say AI share "increased". On the Q2 basis the share fell QoQ (62.3% derived Q1 to 58.4%, FN03). The highlight picks the basis that shows a rise. A cross-deck diff to check whether Q1 used the quarter basis is not possible (no prior run). A4 asks why the headline moved to the H1 basis. |
| FN11 | F16 | M002, R118 | 159 | "sustained investment in innovation and a chip-agnostic design philosophy" | AMBIGUOUS | The CMD frames the design stance as chip-agnostic. No GPU vendor is named anywhere in the document. Notion memory ties thesis-broken #4 to one GPU OEM partnership and its next generation. Two readings: diversification away from one vendor (lower dependency), or pre-emptive cover for a weaker single-vendor allocation. A4 asks for vendor mix of AI Systems revenue and next-generation allocation status. |
| FN12 | F16 | R019-R063, R159 | 92-100, 108 | "1: Operating EBITDA is calculated as Profit before Tax (PBT) plus `Depreciation and amortization expenses' and `Finance cost' less `Other income'" | AMBIGUOUS | PBT, tax, D&A, finance cost and other income are not printed. [DERIVED] Op EBITDA + other income - PAT = D&A + finance cost + tax: Q2 FY26 150, Q1 FY27 437, Q2 FY27 734 Mn (+68% QoQ vs Op EBITDA +63.7%). As a share of (Op EBITDA + other income): 32.3%, 33.9%, 34.9%, rising each period. Other income rose 9 to 85 to 128 Mn [DERIVED, TI minus revenue], which offsets part of the leak. Finance cost on working-capital funding before the raise, a D&A step, or a higher ETR could each explain it. A4 asks for the split. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Press release carries a 7-line P&L summary, not a statutory template. Ledger ZERO_STANDING count 0; no nil or dash cells (lines 92-104). |
| F2 Standalone vs consolidated | N.A. | One unlabelled basis only (FN05). No S-vs-C pair to decompose. |
| F3 Shell-entity detection | N.A. | No cost lines, no entity split. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph in a press release. |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph; no prior-quarter fulltext to diff. |
| F6 Forward-commitment mining | FINDING | Zero lexicon hits; forward language undated (FN01). Register below. |
| F7 Hedge phrase mining | PASS | Lexicon run, zero hits. No safe-harbour paragraph in the document. The one soft word ("potential", line 155) is logged in FN09. |
| F8 Tax forensics | N.A. | No PBT or tax line printed. The derived below-EBITDA stack, which includes tax, is in FN12. |
| F9 OCI forensics | N.A. | No OCI line. |
| F10 Share count and dilution | FINDING | Implied diluted count +1.98% QoQ; EPS growth trails PAT growth (FN02). Basic EPS not printed. |
| F11 Reserves / net worth tie-out | N.A. | No paid-up capital, other equity or net worth printed. Net Debt only (handled in FN07). |
| F12 Segment forensics | FINDING | Product-line revenue only, no segment assets or liabilities. AI share fell QoQ; 572 Mn unsplit residual (FN03). |
| F13 Board outcome beyond results | PASS | Board "took on record the unaudited Financial Results" (lines 66-67). No AR, AGM, director, fund-raise or entity outcome in this document. |
| F14 Note drafting inconsistencies | FINDING | H1 non-additivity of 52 Mn (FN04); basis unlabelled (FN05); footnote marker mismatch (FN06). |
| F15 Entity list diffs | N.A. | No consolidation list in a press release; no prior ledger (ledger section 4 note on R107-R108). |
| F16 Dropped / reframed disclosures | FINDING | Cross-deck diff not possible (no prior run). In-document framing findings FN07-FN12. |
| F17 Concall silence audit | N.A. | Concall-specific check; this document is a press release. Informational checklist coverage map below for A4; no silence counts are claimed. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Execute order book of 26,290 Mn ("strong revenue visibility for the coming quarters") | undated; "coming quarters" (Q3-Q4 FY27 at the Q2 run-rate) | lines 127-128 (R098, R124) | underway |
| Convert additional L1 position of 6,525 Mn into orders | undated | line 127 (R099, R165) | initiated |
| Convert active pipeline of 1,11,518 Mn ("potential business opportunities") | undated | lines 154-155 (R101, R126) | initiated |
| Capital raise of 12,000 Mn, first since July 2023 listing | done in Q2 FY27; use of proceeds not stated in this document | line 130 (R100, R167) | completed |

## 4. NOTION CHECKLIST COVERAGE (informational for A4; F17 is N.A. on this doctype)

Notion text is memory, not evidence. Silence counts are not computed because no prior run exists.
| # | checklist item | addressed in this press release? | line |
|---|---|---|---|
| 1 | CFO/PAT | no | none |
| 2 | CCC / WC days | no; Net Debt only | 80 |
| 3 | Blackwell order execution | no; order book total only, no programme split | 83, 127 |
| 4 | EBITDA margin (red: below 12% two quarters) | yes; Q2 14.9%, Q1 14.7%. Not near the red line. See FN04 for the H1 basis | 98 |
| 5 | Software + services share | no; inside the 572 Mn unsplit residual at most | 125-126 |
| 6 | Customer concentration | no | none |
| 7 | Promoter stake sales | no | none |
| 8 | Inventory audit remediation | no | none |
| 9 | New strategic AI order of 5,000 Mn or more | no named order; aggregate L1 6,525 Mn only | 127 |
| 10 | Chandelier Exit | out of document scope | none |
| TB-4 | GPU OEM partnership / next generation | no vendor named; "chip-agnostic" framing | 159 |

## 5. CLASSIFICATION ROLL-UP
FORWARD-SIGNAL: FN02, FN07, FN08. AMBIGUOUS (A4 questions): FN01, FN03, FN04, FN05, FN09, FN10, FN11, FN12. NEUTRAL-FACT: FN06. CONFIRMATORY-NEGATIVE: none.

```yaml
stage: A3-forensics
company: "NETWEB"
quarter: "q2fy27"
doctype: "presentation (press release), label pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-netweb-q2fy27-a60c5c/runs/netweb-q2fy27/work/forensics_pressrelease_netweb_q2fy27.md"
ledger_reconciled_pct: 100        # 174 of 174 (R001-R170 + M001-M004)
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN01", check: "F6", line: "127-128, 154-155", classification: "AMBIGUOUS", implication: "Zero lexicon hits; all forward language undated ('for the coming quarters'). Ask the execution schedule of the 26,290 Mn book and the L1 6,525 Mn conversion date."}
  - {id: "FN02", check: "F10", line: "100, 104", classification: "FORWARD-SIGNAL", implication: "Implied diluted shares 56.94 to 58.07 Mn QoQ (+1.98%); EPS +324.2% vs PAT +334.8% YoY. Raise only part-quarter in Q2, so Q3 EPS again grows slower than PAT."}
  - {id: "FN03", check: "F12", line: "125-126, 85", classification: "AMBIGUOUS", implication: "Derived Q1 AI 5,105 Mn (62.3%) to Q2 7,731 Mn (58.4%); non-AI +77.9% QoQ; 572 Mn (4.3%) unsplit residual; no segment assets/liabilities."}
  - {id: "FN04", check: "F14", line: "92, 96, 98", classification: "AMBIGUOUS", implication: "H1 not equal to Q1+Q2: Total Income -52, Op EBITDA +52; revenue and PAT tie. Printed H1 margin 15.1% exceeds both quarters; additive basis 14.83% = -10 bps YoY, not +14 bps."}
  - {id: "FN05", check: "F14", line: "35, 67", classification: "AMBIGUOUS", implication: "Standalone vs consolidated basis never stated; no limited-review mention. Confirm basis against the results filing."}
  - {id: "FN06", check: "F14", line: "96-104, 108-109", classification: "NEUTRAL-FACT", implication: "Footnote marker 2 (PAT margin definition) attached to Op EBITDA, Op EBITDA Mg, PAT and EPS. Cumulative drafting-care point with FN04 and the unsigned Net Debt bracket."}
  - {id: "FN07", check: "F16", line: "80, 130, 160", classification: "FORWARD-SIGNAL", implication: "Net debt within 136 Mn of zero after a 12,000 Mn raise (1.1%), under either bracket sign. Raise absorbed; 'strengthened balance sheet' rests on this one number; no CFO, gross debt or WC printed. H2 WC needs operating cash or new debt."}
  - {id: "FN08", check: "F16", line: "83, 127-128", classification: "FORWARD-SIGNAL", implication: "Order book = 1.99 quarters of Q2 revenue; flat Q2 run-rate in H2 needs 100.7% of the closing book. Growth above it needs L1 conversion and in-half inflow. No inflow, book-to-bill or definition printed."}
  - {id: "FN09", check: "F16", line: "154-155", classification: "AMBIGUOUS", implication: "Pipeline 1,11,518 Mn = 4.24x order book, 5.1x FY26 revenue; undefined stage, horizon, probability; 'potential' hedge. Ask definition and historic conversion rate."}
  - {id: "FN10", check: "F16", line: "85-86, 125", classification: "AMBIGUOUS", implication: "Highlight uses the H1 basis to say AI share 'increased to 59.9%'; on the Q2 basis it fell QoQ to 58.4%. Basis choice shows a rise."}
  - {id: "FN11", check: "F16", line: "159", classification: "AMBIGUOUS", implication: "'chip-agnostic design philosophy'; no GPU vendor named. Diversification or cover for single-vendor allocation. Links to Notion thesis-broken #4 (memory). Ask vendor mix and next-generation allocation."}
  - {id: "FN12", check: "F16", line: "92-100, 108", classification: "AMBIGUOUS", implication: "PBT, tax, D&A, finance cost not printed. Derived D&A+finance+tax 150 / 437 / 734 Mn (Q2 FY26 / Q1 / Q2), 32.3% / 33.9% / 34.9% of EBITDA+OI; +68% QoQ vs EBITDA +63.7%. Ask the split."}
forward_signals: ["FN02", "FN07", "FN08"]
ambiguous: ["FN01", "FN03", "FN04", "FN05", "FN09", "FN10", "FN11", "FN12"]
commitments:
  - {commitment: "Execute order book 26,290 Mn ('strong revenue visibility for the coming quarters')", implied_date: "undated; coming quarters (Q3-Q4 FY27)", ref: "lines 127-128 (R098, R124)", status_word: "underway"}
  - {commitment: "Convert additional L1 position 6,525 Mn", implied_date: "undated", ref: "line 127 (R099, R165)", status_word: "initiated"}
  - {commitment: "Convert active pipeline 1,11,518 Mn", implied_date: "undated", ref: "lines 154-155 (R101, R126)", status_word: "initiated"}
  - {commitment: "Capital raise 12,000 Mn, first since July 2023 listing; use of proceeds not stated", implied_date: "Q2 FY27 (done)", ref: "line 130 (R100, R167)", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Two derived numbers matter most. First, H1 is not the sum of Q1 and Q2 on Total Income (21,591 vs 21,643) or Op EBITDA (3,230 vs 3,178), while revenue and PAT tie. A 52 Mn item sits in other income on one basis and in operating profit on the other. On the additive basis the H1 margin is 14.83%, a 10 bps YoY fall, not the printed 14 bps rise. The printed H1 margin of 15.1% sits above both quarters. Second, net debt sits within 136 Mn of zero after a 12,000 Mn raise. The raise funded working capital or repaid debt and left no cash cushion, yet line 160 calls this a strengthened balance sheet. The closing order book covers about two quarters at the Q2 run-rate, so H2 growth above Q2 needs L1 conversion and inflow inside the half. Diluted shares rose about 2% QoQ on a part-quarter raise, and Q3 carries the full count. All derivations use printed figures only. Cross-quarter diffs (F5, F15, F16 cross-deck) were not possible because no prior NETWEB run exists."
```
