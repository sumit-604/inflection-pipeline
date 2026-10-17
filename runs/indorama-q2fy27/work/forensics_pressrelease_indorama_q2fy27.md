# A3 FORENSIC NOTES: INDORAMA Q2 FY27, doctype presentation (pressrelease: Reg 30 cover + media release, 3 pages)

Inputs read: A1 structured (R001-R132), A1 fulltext (lines 1-181), A2 ledger. Source PDF and inputs/ not opened.
Prior-quarter fulltext: ND (not available). Notion checklist: NONE (no page, no spear).
Unit: Rs crore. Table basis consolidated (line 92). Results unaudited (line 39-40).

## LEDGER RECONCILIATION
- Rows in ledger: 132 (R001-R132, orphan_ids none). Rows read at cited fulltext line: 132. Reconciled: 100%.
- Line cites verified. Minor span notes only: R020 block spans lines 64-67; R130 block spans 160-169; R131 heading at 173, text 174-180; R003 exchange name at line 23 (line 22 is the department). None changes a value.
- Arithmetic tie-out of the page 2 table (line 96-106): H1 = Q1 + Q2 holds for Total Income (940.2 + 1,344.0 = 2,284.2), EBITDA (108.0 + 117.7 = 225.7), EBIT (93.1 + 102.9 = 196.0), PAT (63.7 + 74.1 = 137.8). All margins recompute to the stated 1 dp. Four growth cells sit 0.1 pp below recompute from rounded inputs (EBITDA QoQ 8.9% vs 9.0%; EBIT YoY 77.0% vs 77.1%; EBIT QoQ 10.4% vs 10.5%; PAT QoQ 16.2% vs 16.3%). Each is reachable from unrounded inputs; not a finding.
- Derived prior-year quarter (H1FY26 minus Q2FY26): Q1FY26 Total Income 1,308.5; EBITDA 100.3; EBIT 81.8; PAT 52.7; implied D&A 18.5.

## FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F6 | R114, R115, R116, R117 | 139-140 | "we plan to invest approximately X200 crore over the next 12—18 months to diversify in specialty fibre and filament products" | FORWARD-SIGNAL | First quantified diversification spend. Rs 200 cr = 0.89x H1FY27 EBITDA (225.7, line 98). Window from 16 Oct 2026 ends Oct 2027 to Apr 2028. No funding source, board approval, tonnage, product list, start date or return target stated. Feeds Role 5 promise tracker and FTTCP catalyst timeline. |
| FN-02 | F16 | R049, R051, R070, R072, R104 | 73-74; 100; 130-131 | "Marks a Strong Quarter of Profit Growth and Margin Expansion"; "EBITDA Margin % 8.8% 6.6% 11.5%"; "higher raw material costs and continued volatility across the polyester value chain" | FORWARD-SIGNAL | Headline margin expansion is YoY only. QoQ EBITDA margin fell 270 bp (11.5% to 8.8%) and PAT margin 130 bp (6.8% to 5.5%). CMD calls the crude-led cost pressure "continued". Lean bear: Q3 spread at risk if crude stays high. |
| FN-03 | F16 | R036, R038, R039, R040, R079, R080 | 96; 111-113 | "degrowth of 9.7% due to supply chain issues in view of geopolitical issues in the middle east" | AMBIGUOUS | Derived Q1FY27 total income 940.2 vs Q1FY26 1,308.5 = -28.1% YoY; release states only the H1 -9.7%. Q2FY27 1,344.0 is just 2.7% above Q1FY26. The +43.0% QoQ is a rebound from a disrupted Q1. The release gives no volume or realisation split; crude-led price pass-through could carry the +10% YoY. Question: Q2 volumes and realisations YoY and QoQ; is supply chain normal now. |
| FN-04 | F16 | R014, R021, R033, R035, R102 | 75; 96; 129 | "For Q2FY27 Revenue Growth of 10% y-o-y"; "Total Income 1,344.0 \| 1,222.4 \| 10.0%"; "revenue from operations improving" | AMBIGUOUS | Headline "revenue" growth is Total Income growth. Revenue from operations and other income are not disclosed. EBITDA margin recomputes on Total Income (117.7 / 1,344.0 = 8.76%), so other income may sit inside EBITDA. Question: revenue from operations and other income for Q2FY27, Q2FY26, Q1FY27; is other income in EBITDA. |
| FN-05 | F16 | R041, R042, R044, R054, R055, R057 | 98; 102 | "EBITDA 117.7 80.4 46.4% 108.0"; "EBIT 102.9 58.1 77.0% 93.1" | AMBIGUOUS | Implied D&A (EBITDA minus EBIT): 14.8 Q2FY27, 22.3 Q2FY26, 14.9 Q1FY27, 18.5 Q1FY26 (derived). D&A down 7.5 cr YoY (-34%), which supplies 16.7% of the 44.8 cr EBIT increase. Readings: asset sale or impairment lowering the base, useful-life change, or a Q2FY26 one-off. Question: depreciation and amortisation by quarter and the cause of the fall. |
| FN-06 | F8 | R054, R055, R057, R060, R062, R065, R068 | 102; 104 | "EBIT 102.9 58.1 ... 93.1 ... 139.9"; "PAT 74.1 246 ... 63.7 ... 77.3" | AMBIGUOUS | EBIT minus PAT (finance cost + tax + any exceptional, not split in the release): 28.8 Q2FY27, 33.5 Q2FY26, 29.4 Q1FY27, 29.1 Q1FY26 (derived). The wedge is flat at 28.8-29.4 cr in 3 of 4 quarters while EBIT moves 81.8-102.9 cr. A flat wedge fits finance cost with little profit-linked tax. Reading A: near-nil tax (loss carry-forward or DTA); at 25.17% on implied PBT 74.1, PAT would be about 55.4 cr (-25%), an ETR step-up risk. Reading B: full tax already charged, which needs finance cost near 3.9 cr in Q2FY27 vs about 25.2 cr in Q2FY26. Separating observation: finance cost and tax lines in the results filing. Lean bear on Reading A. |
| FN-07 | F14 | R063, R092, R071 | 104; 120 | "PAT 74.1 246 201.8%"; "compared with X24.6 crore in Q2 FY26" | NEUTRAL-FACT | Table value 246 is a decimal glyph loss. 24.6 is confirmed three ways: PAT margin 2.0% (24.6 / 1,222.4 = 2.01%), H1FY26 77.3 minus 24.6 = 52.7 (246 would exceed H1), YoY 201.8% fits an unrounded base near 24.55. Use 24.6. |
| FN-08 | F14 | R030, R027, R028, R029 | 85; 89 | "Yoy Yoy Yoy" | NEUTRAL-FACT | Card YoY percentages are absent from the text layer (likely graphic). Card values are rounded (118 Cr, 74 Cr) versions of table values 117.7 and 74.1. No conflict; FOOTNOTE_UNRESOLVED stands. |

## CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Press release, no statutory template; A2 ledger zero_standing 0 (ledger line 34). |
| F2 Standalone vs consolidated | N.A. | Consolidated only (line 80, 92); no standalone figures in doc. |
| F3 Shell-entity detection | N.A. | No standalone cost lines, no entity list. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters para; results "Un-audited" (line 39-40). |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph; prior-quarter fulltext ND. |
| F6 Forward-commitment mining | FINDING | FN-01: Rs 200 cr capex, 12-18 months (line 139). Lexicon note: no exact-phrase hit ("will be", "commenc", "board has approved" absent); "is expected to broaden" (line 140) is the nearest. Commitment captured as dateable. |
| F7 Hedge phrase mining | PASS | Only lexicon hit is safe-harbor boilerplate "subject to risks and uncertainties" (line 175). No prior deck to diff for newly added hedges. |
| F8 Tax forensics | FINDING | No tax, PBT or finance-cost line; ETR not computable. FN-06: flat EBIT-to-PAT wedge implies either sub-statutory tax or a finance-cost collapse. |
| F9 OCI forensics | N.A. | No OCI data. |
| F10 Share count and dilution | N.A. | Release carries no paid-up capital, share count or EPS. |
| F11 Reserves and net worth | N.A. | Release carries no equity or net worth figure. |
| F12 Segment forensics | N.A. | No segment data. |
| F13 Board outcome | N.A. | No board outcome in this document; board meeting times absent. Cover signed 2026.10.16 21:47:58 (line 52). A4 to read the results filing for board items. |
| F14 Drafting inconsistencies | FINDING | FN-07 (246 vs 24.6), FN-08 (card YoY blanks). Both text-layer artefacts, resolved or neutral. Cover title "INDORAMA Marks..." (line 41) vs page 2 "Indo Rama Synthetics Marks..." (line 73): cosmetic. |
| F15 Entity list diffs | N.A. | No consolidation entity list; prior ND. |
| F16 Dropped / reframed disclosures | FINDING | Cross-deck diff not possible (prior ND). Within-document reframing: FN-02 (margin headline YoY only), FN-03 (H1 cause stated, Q1 -28.1% YoY not stated), FN-04 (Total Income labelled revenue), FN-05 (undisclosed D&A fall lifts EBIT growth). |
| F17 Silence audit | N.A. | Concall-specific; no transcript in this doctype; no Notion checklist exists. Disclosure gaps for A4 listed below. |

## COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| Invest approx. Rs 200 cr to diversify into specialty fibre and filament products | Oct 2027 to Apr 2028 (12-18 months from 16 Oct 2026) | line 139 (R114-R116) | planned (pre-initiation; not initiated/underway/completed) |
| Investment to broaden portfolio, raise value-added participation, support growth | medium term, undated | line 140-142 (R117) | expected |
| Further strengthen operating and financial performance | undated | line 138 (R113) | aspirational, no milestone |

## DISCLOSURE GAPS FOR A4 (not an F17 silence audit; one-quarter view, consecutive count ND)
| item absent from the release | relevance |
|---|---|
| Revenue from operations, other income | FN-04 |
| Volumes, realisations, product mix | FN-03 |
| Depreciation, finance cost, tax, exceptional items | FN-05, FN-06 |
| Funding plan, board approval, tonnage for Rs 200 cr capex | FN-01 |
| Debt, net worth, cash flow | F10/F11 not testable |
| Q1FY27 YoY decline (derived -28.1%) | FN-03 |

## A4 FLAGS
- FORWARD-SIGNAL: FN-01, FN-02.
- AMBIGUOUS (convert to management questions): FN-03, FN-04, FN-05, FN-06.

```yaml
stage: A3-forensics
company: "INDORAMA"
quarter: "Q2 FY27"
doctype: "presentation (pressrelease: Reg 30 cover + media release)"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indorama-q2fy27/work/forensics_pressrelease_indorama_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F6", line: "139-140", classification: "FORWARD-SIGNAL", implication: "Rs 200 cr specialty fibre/filament capex over 12-18 months (window Oct 2027-Apr 2028); 0.89x H1 EBITDA; no funding, approval, tonnage or returns stated"}
  - {id: "FN-02", check: "F16", line: "73-74; 100; 130-131", classification: "FORWARD-SIGNAL", implication: "Margin expansion headline is YoY only; QoQ EBITDA margin 11.5% to 8.8% (-270 bp); CMD says cost volatility continued; Q3 spread risk"}
  - {id: "FN-03", check: "F16", line: "96; 111-113", classification: "AMBIGUOUS", implication: "Derived Q1FY27 total income -28.1% YoY; Q2FY27 only 2.7% above Q1FY26; +43% QoQ is rebound; volume vs price split absent"}
  - {id: "FN-04", check: "F16", line: "75; 96; 129", classification: "AMBIGUOUS", implication: "Headline revenue growth is Total Income growth; revenue from operations and other income undisclosed; other income may sit in EBITDA"}
  - {id: "FN-05", check: "F16", line: "98; 102", classification: "AMBIGUOUS", implication: "Implied D&A 14.8 vs 22.3 YoY (-34%) supplies 7.5 of 44.8 cr EBIT growth; cause undisclosed"}
  - {id: "FN-06", check: "F8", line: "102; 104", classification: "AMBIGUOUS", implication: "EBIT-PAT wedge flat 28.8-29.4 cr in 3 of 4 quarters; either near-nil tax (statutory tax would cut PAT to about 55 cr) or finance cost fell to about 3.9 cr; results filing separates"}
  - {id: "FN-07", check: "F14", line: "104; 120", classification: "NEUTRAL-FACT", implication: "Q2FY26 PAT table 246 is glyph loss; 24.6 confirmed by margin, H1 and YoY tie-outs"}
  - {id: "FN-08", check: "F14", line: "85; 89", classification: "NEUTRAL-FACT", implication: "Card YoY percentages absent from text layer; card values are rounded table values"}
forward_signals: ["FN-01", "FN-02"]
ambiguous: ["FN-03", "FN-04", "FN-05", "FN-06"]
commitments:
  - {commitment: "Invest approx. Rs 200 cr to diversify into specialty fibre and filament products", implied_date: "Oct 2027 to Apr 2028", ref: "line 139 (R114-R116)", status_word: "planned"}
  - {commitment: "Broaden portfolio, raise value-added participation, support growth", implied_date: "medium term, undated", ref: "line 140-142 (R117)", status_word: "expected"}
  - {commitment: "Further strengthen operating and financial performance", implied_date: "undated", ref: "line 138 (R113)", status_word: "aspirational"}
gate_a3: pass
blank_checks: []
analyst_note: "This is a press release only. It carries no notes, auditor text, standalone, segment or balance sheet data, so F1-F5, F9-F13, F15 and F17 are N.A. No prior deck exists, so F16 is a within-document reading. FN-06 is the load-bearing item. EBIT minus PAT holds at 28.8-29.4 cr in three of four quarters while EBIT moves from 81.8 to 102.9 cr. A flat wedge fits finance cost with little profit-linked tax. In that case, 74.1 cr PAT carries a tax shield, and at 25.17% on implied PBT PAT would be about 55 cr. The other reading needs finance cost near 3.9 cr, against about 25 cr a year earlier. The finance cost and tax lines in the results filing separate the two readings. The 202% PAT headline rests on a weak base of 24.6 cr. Derived Q1FY27 income fell 28.1% YoY, and Q2FY27 is only 2.7% above Q1FY26. Margin fell 270 bp QoQ while the headline claims expansion. The Rs 200 cr capex states no funding, tonnage or approval."
```
