# A3 FORENSIC NOTES: INDORAMA (Indo Rama Synthetics (India) Ltd), Q2 FY27, doctype: results

Inputs read: A1 structured `runs/indorama-q2fy27/extracted/indorama-results-q2fy27-structured.md` (R001-R721, all rows); A1 fulltext `runs/indorama-q2fy27/extracted/indorama-results-q2fy27-fulltext.md` (lines 1-837, all lines; VER- image-verified lines govern over the OCR text); A2 ledger `runs/indorama-q2fy27/work/ledger_results_indorama_q2fy27.md`. Prior-quarter fulltext: ND. Notion checklist: NONE (no Notion page, no spear on record). Source PDF and `inputs/` not opened.

Unit: Rs crore unless stated. S = standalone, C = consolidated. "Derived" = A3 arithmetic on filed numbers, not a filed figure.

## 0. LEDGER RECONCILIATION
- Ledger accounts for 721 of 721 structured IDs (ledger line 13, orphan_ids empty). A3 read all 721 rows in the structured file and the cited fulltext line for each. Reconciled: 721 / 721 = 100%.
- Arithmetic tie-outs (all PASS): S and C P&L subtotals for all six columns; Q1 + Q2 = H1 on revenue, D&A, finance cost and PAT; S and C balance sheets foot both dates; S and C cash flows foot to closing cash (S 1.65, C 6.82); other equity roll-forward equals H1 total comprehensive income exactly (S 302.65 + 88.80 = 391.45; C 258.06 + 137.82 = 395.88); EPS = PAT / 26.111 crore shares in every column.
- Borrowings tie: S total 943.98 to 719.42 = -224.56 = repayment 17.58 + current movement 206.98. C total 1,131.60 to 860.13 = -271.47 = 64.49 + 206.98. S non-current fall 65.49 less repayment 17.58 = 47.91 reclassified to current maturities.

### Extraction notes for A4 / verifiers (A1 issues, not filer findings)
- R145 and R478 carry the label "Other equity, H1 FY26". Their values (302.65 S, 258.06 C) equal the 31 Mar 2026 balance-sheet other equity (R201 line 309; R530 line 699). The VER lines (220, 620) give only five cells for six columns. Treat both as the FY26 (31 Mar 2026) figure, not H1 FY26.
- R640 records the consolidated firm registration as "000756N". Fulltext line 520 reads "000756N/N500441", the same as the standalone report. A1 truncation, no source inconsistency.
- Derived subsidiary borrowings at 31 Mar 2026 equal 93.81 in both non-current (444.58 - 350.77) and current (687.02 - 593.21). The current gap is again 93.81 at 30 Sep 2026 (527.95 - 434.14). The arithmetic is possible, but a verifier should confirm lines 701 and 706 against the page 10 image.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R091-R096, R388-R393 | 211, 605 | "Exceptional items - Employee benefit expenses \| - \| - \| - \| - \| - \| 2.69" | AMBIGUOUS | A named employee-benefit exceptional of 2.69 (S) / 2.70 (C) hit FY26. H1 FY26 shows nil, so the charge fell in H2 FY26. The template keeps a line for this transaction class (typically a separation/VRS scheme; the filing does not name it). Ask what the FY26 charge was and whether a further scheme is planned for H2 FY27. |
| A3-02 | F1 | R442-R447, R454-R459, R466-R471 | 614 | "Profit attributable to Non Controlling interest \| - \| - \| - \| - \| - \| -" | NEUTRAL-FACT | NCI is nil in every period, so the four subsidiaries are wholly owned (implied, not stated). All subsidiary profit flows to parent shareholders. |
| A3-03 | F1 | R280-R281, R609-R610, R268, R599 | 399, 791 | "Proceeds from non-current borrowings \| 0.00 \| 44.00" | NEUTRAL-FACT | H1 FY27 raised no new term debt (H1 FY26: 44.00) and sold no PPE. The 271.47 debt fall is all repayment, with no refinancing behind it. |
| A3-04 | F2 | R115-R120, R412-R417, R055-R060, R352-R357 | 609, 215 | "Net profit/(loss) for the period (12-13) \| 74.08 \| 63.74 \| 24.55 \| 137.82 \| 77.30 \| 150.21" | AMBIGUOUS | The C-minus-S PAT gap as a % of S PAT is 34.6% (Q2 FY27), 88.9% (Q1 FY27), 6.6% (Q2 FY26). That is -54.3 pp QoQ and +28.0 pp YoY. H1 gap: 39.7% to 55.2%, +15.5 pp. All moves exceed the 5 pp trigger. Subsidiaries made 47.1% of C PAT in Q1 and 25.7% in Q2, with no entity split. Ask which subsidiary earns this and why it swings. |
| A3-05 | F2 | R025-R030, R322-R327, R031-R036, R328-R333 | 594, 200 | "(b) Purchase of stock-in-trade \| 116.22 \| 48.30 \| 78.76" | AMBIGUOUS | Subsidiary traded-goods purchases (derived C - S) were 74.11 in Q2 FY27, 30.85 in Q1 FY27, 74.71 in Q2 FY26 and 179.27 in FY26. The subsidiary revenue gap (92.31 in Q2) is mostly trading, not conversion. Subsidiary earnings ride trading margins and inventory timing: the Q2 inventory change gap is -40.92. Ask what the subsidiaries trade and from whom. |
| A3-06 | F2 | R182-R183, R511-R512 | 690, 300 | "Trade receivables \| 103.06 \| 243.32" vs S "Trade receivables \| 285.60 \| 379.70" | AMBIGUOUS | C receivables sit below S by 182.54 (31 Mar 2026: 136.38). At least 182.54, or 63.9%, of the parent's receivables are therefore owed by subsidiaries and are eliminated. Intercompany credit grew by 46.16 or more while the parent's reported receivables fell 94.10. The parent's external receivables are 103.06 or less. Ask about intercompany sale terms and settlement. |
| A3-07 | F2 | R200-R201, R529-R530, R145, R478 | 699, 309 | "Other equity \| 395.88 \| 258.06" vs S "Other equity \| 391.45 \| 302.65" | NEUTRAL-FACT | At 31 Mar 2026, C other equity was 44.59 below S, so the subsidiaries carried a net cumulative deficit or consolidation adjustments. H1 subsidiary profit of 49.02 turned the gap to +4.43. The subsidiaries' turnaround is recent. |
| A3-08 | F3 | R037-R042, R334-R339, R019-R024, R316-R321, R158-R159, R491-R492, R061-R066, R358-R363 | 596, 593, 680 | "(d) Employee benefits expense \| 31.53 \| 30.97"; "(a) Cost of materials consumed \| 944.32 \| 584.61" | AMBIGUOUS | The subsidiaries are not shells in aggregate: derived PPE of 355.79, D&A 2.43 a quarter, other expenses 28.49 a quarter. But payroll is thin at 1.41 a quarter against 355.79 of PPE. C materials cost sits below S in 4 of 6 periods (Q1 FY27: 584.61 vs 588.21), so the parent buys materials from the subsidiaries as well as sells to them. The partial-shell signature fits asset-holding or trading vehicles. Ask which of the four entities run plant and who staffs it. |
| A3-09 | F8 | R103-R114, R097-R102, R172-R173, R400-R405 | 213, 214, 295 | "Tax expense/(credit) \| - \| - \| - \| - \| - \| -"; "Deferred tax assets (net) \| 258.61 \| 258.61" | FORWARD-SIGNAL | S effective tax rate (ETR) is 0% in all six periods on positive PBT (FY26 110.03; H1 FY27 88.80). The 258.61 S deferred tax asset (DTA) did not move in H1. Derived shield against the 25.17% statutory rate: 22.35 S / 34.85 C in H1 FY27, about 2,517-2,533 bps of PBT. At 25.17%, C H1 EPS would be 3.94, not the reported 5.28. ETR step-up risk arises when the unrecognised loss pool is used up, or when DTA utilisation starts to run through P&L. No earlier-years tax adjustment line exists. |
| A3-10 | F8 | R406-R411, R501-R502, R539-R540 | 608, 685, 704 | "Deferred tax (credit) \| (0.22) \| - \| - \| (0.22)"; "Deferred tax liabilities (net) \| 9.37 \| -" | AMBIGUOUS | C DTA rose 9.59 and a new C DTL of 9.37 appeared (nil at 31 Mar 2026). Net movement +0.22 ties to the P&L credit. The gross-up means one subsidiary now carries a DTL and another holds the added DTA. This is the first tax line at subsidiary level. Ask which entity and why. |
| A3-11 | F12 | R204-R205, R212-R213, R533-R534, R543-R544, R575-R576, R607-R608, R611-R612 | 701, 706, 774 | "Borrowings (current) \| 527.95 \| 687.02"; "Changes in trade receivables \| 140.26 \| 3.50" | AMBIGUOUS | There is one reportable segment (lines 425, 819), so the segment test runs on the entity balance sheet. C borrowings fell 271.47 (-24.0%) in H1. C receivables fell 57.6% (243.32 to 103.06) while Q2 C revenue rose 9.8% YoY. That implies about 7 days of Q2 sales in receivables (derived). Of the H1 C operating cash flow of 328.46, 109.02 is a working-capital release. This could be a working-capital unwind or a durable fall in debt. Ask about receivable discounting/factoring, quarter-end timing, and whether it repeats in H2. |
| A3-12 | F12 | R190-R191, R218-R219, R519-R520, R549-R550 | 694, 709 | "Other financial assets (current) \| 667.63 \| 658.25"; "Trade payables other than MSME \| 1,444.43 \| 1,433.26" | AMBIGUOUS | Two undisclosed blocks dominate the balance sheet. Other financial assets are 21.3% of C total assets (3,131.68). Total trade payables (1,462.03) are 46.7%, about 126 days of Q2 materials plus traded purchases (derived). Payables of this size usually include acceptances or LC-backed supplier credit, which is debt-like. The filing does not name the counterparty or say whether it is a related party. Ask what makes up both lines and what the payables cost. |
| A3-13 | F14 | R688 | 57, 59 | "b) Publication of Extract of Audited Financial Results" vs "publishing Extract of Un-audited Financial Results" | NEUTRAL-FACT | The heading was carried over from a year-end template. Immaterial alone; counts toward the governance data point. |
| A3-14 | F14 | R657, R708, R717 | 460-461, 505, 811 | "its subsidiary (Holding Company and its subsidiary together referred to as “the Group”)" | AMBIGUOUS | Para 1 of the consolidated review report uses the singular. Para 4 lists four subsidiaries (lines 506-509) and Note 2 says "its subsidiaries" (line 811). A singular left in the template can mean the perimeter was one subsidiary when the template was set. Links to A3-16. |
| A3-15 | F14 | R696, R697, R712, R713, R700, R716, R630 | 225, 415, 63 | "Notes:1 Unaudited Standalone Statement of Assets and Liabilities"; "concluded at 14:35 PM IST" | NEUTRAL-FACT | "Note 1" and "Note 2" each appear twice per filing: the balance sheet and cash flow labels, then the numbered notes. The time format mixes 24-hour and PM. Cosmetic; counts toward the cumulative data point. |
| A3-16 | F15 | R659-R662, R708 | 506-509 | "Indorama Ventures Yarns Private Limited ... Indorama Sustainable Polyester Yarns Private Limited" | AMBIGUOUS | The perimeter is four subsidiaries, no JV or associate. The prior-quarter list is ND, so additions, deletions or renames cannot be diffed. Lean bear on A3-14. Ask when each of the four entered the group and whether any were renamed or reclassified in the last four quarters. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 85 ZERO_STANDING cells on 22 line items, all read. Employee-benefit exceptional line (A3-01). Nil NCI means wholly owned (A3-02). No new term debt or asset sales (A3-03). Nil tax: see F8. Nil interim OCI: see F9. New intangible of 0.04 at 30 Sep 2026 is immaterial. |
| F2 S vs C decomposition | FINDING | No JV or associate, so the gap is subsidiaries net of eliminations. PAT-gap moves exceed 5 pp in every comparison (A3-04). Trading-led subsidiary activity (A3-05). Intercompany receivables of 182.54 or more (A3-06). Subsidiary deficit at FY26 (A3-07). Table in section 4. |
| F3 Shell-entity detection | FINDING | Not shells in aggregate. Thin payroll, and C materials below S, give a partial-shell signature. Per-entity split ND (A3-08). No Going Concern EoM to reconcile. |
| F4 Unaudited contribution ratio | PASS | The consolidated review report lists four subsidiaries (lines 505-509) and has no Other Matter paragraph on component auditors or unreviewed component financials. Conclusion unmodified (line 510). Unreviewed share of C PAT stated as 0. Every period is limited review, not audit. |
| F5 Going Concern / EoM scope | PASS | Neither review report has an Emphasis of Matter or Going Concern paragraph (S lines 124-130; C lines 510-517; grep returned none). No current-quarter scope to expand. The prior-quarter verbatim diff did not run (prior extract ND), so a dropped prior EoM cannot be excluded. |
| F6 Forward-commitment phrases | PASS | Lexicon hits: line 63 "commenced" (meeting start, past tense, no commitment); lines 58-60 "would be publishing" and "being published" (procedural Reg 47 extract). The notes (lines 415-429, 805-823) hold no business commitment: no capex, project, approval or timeline. See register. |
| F7 Hedge phrases | PASS | Zero hits for the lexicon in notes or reports (grep). |
| F8 Tax forensics | FINDING | S ETR 0% in all periods; C ETR -0.3% in Q2 FY27 and 0% elsewhere; frozen DTA and shield quantified (A3-09). Subsidiary DTA/DTL gross-up (A3-10). No earlier-years tax line. Income-tax refund of 3.76 ties to the S non-current tax asset fall (8.42 to 4.66). |
| F9 OCI forensics | PASS | Interim OCI is nil in every quarter and half-year. FY26 OCI is 0.77 S / 0.75 C, so remeasurement runs at year-end only. No single-quarter swing. Verify FY27 actuarial assumptions at the Annual Report. |
| F10 Share count / dilution | PASS | Paid-up 261.11 in every period (26.111 crore shares). Basic = diluted in all 12 EPS cells: no dilutive instruments in the EPS. A4 runs the warrant/ESOP cross-check. |
| F11 Reserves / net worth tie-out | PASS | S 261.11 + 391.45 = 652.56; C 261.11 + 395.88 = 656.99. Both dates tie. The H1 roll-forward equals total comprehensive income exactly, so no dividend or other reserve movement. No third-party figure in the document to reconcile. |
| F12 Segment forensics | FINDING | One reportable segment, no segment assets or liabilities table. Test applied to the entity balance sheet: sharp debt and receivable fall (A3-11); undisclosed other financial assets and payables blocks (A3-12). |
| F13 Board outcome beyond results | PASS | Agenda items a and b only (lines 49-61): results and Reg 47 extract. No AR, AGM, record date, dividend, fund-raising enabling resolution or director appointment. No Role 6 trigger from this filing. |
| F14 Note drafting inconsistencies | FINDING | Audited vs Un-audited heading (A3-13). Singular "its subsidiary" vs four listed (A3-14). Duplicate note numbering and time format (A3-15). Note 2 "limited review" (lines 421, 815) matches both auditor reports. |
| F15 Entity list diffs | FINDING | Four subsidiaries (lines 506-509). Prior list ND, A2 flags ENTITY_CHANGE_UNKNOWN. The singular "its subsidiary" hints at a perimeter change (A3-16). |
| F16 Presentation: dropped/reframed disclosures | N.A. | Results doctype; no presentation. |
| F17 Concall silence audit | N.A. | Results doctype; no transcript. No Notion checklist exists (pre-thesis read). The filing's notes carry no business commentary, so no commitment exists to track for silence. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Publish extract of unaudited Q2/H1 FY27 results in newspapers under Reg 47(1)(b) | Not stated in filing (statutory Reg 47 window after the 16 Oct 2026 meeting) | Board outcome item b, lines 57-60 (R667) | initiated ("would be publishing") |
| Publish extract on company website www.indoramaindia.com | Not stated in filing | Board outcome item b, line 60 (R668) | underway ("is also being published") |

Neither entry is a business commitment. The notes contain no capex, commissioning, approval or restructuring commitment that could feed the Role 5 promise-vs-delivery tracker or the FTTCP catalyst timeline.

## 4. F2 WORKING: S vs C GAP BY PERIOD (derived, C minus S)

| period | revenue gap | % of S revenue | EBITDA* gap | % of S EBITDA | PAT gap | % of S PAT | subs share of C PAT |
|---|---|---|---|---|---|---|---|
| Q2 FY27 | 92.31 | 7.4% | 24.52 | 26.3% | 19.03 | 34.6% | 25.7% |
| Q1 FY27 | 118.73 | 14.5% | 35.82 | 49.6% | 29.99 | 88.9% | 47.1% |
| Q2 FY26 | 54.35 | 4.7% | 9.18 | 12.9% | 1.51 | 6.6% | 6.2% |
| H1 FY27 | 211.04 | 10.2% | 60.34 | 36.5% | 49.02 | 55.2% | 35.6% |
| H1 FY26 | 175.12 | 7.4% | 37.63 | 26.3% | 21.95 | 39.7% | 28.4% |
| FY26 | 391.33 | 8.7% | 69.96 | 23.5% | 40.18 | 36.5% | 26.7% |

*EBITDA = "Profit from operations before D&A, finance costs and FX loss/(gain)" (lines 205, 599).

Q2 FY27 subsidiary bridge (C - S): revenue +92.31; other income -2.42 (intercompany interest eliminated: S H1 interest income 5.95 vs C 3.60); materials +2.28; stock-in-trade +74.11; inventory change -40.92; employee +1.41; other expenses +28.49; EBITDA +24.52; D&A +2.43; finance cost +3.34; FX -0.06; PBT +18.81; deferred tax credit +0.22; PAT +19.03.

Implied subsidiary PAT by quarter (derived): Q1 FY26 20.44, Q2 FY26 1.51, H2 FY26 18.23 (two quarters), Q1 FY27 29.99, Q2 FY27 19.03.

Subsidiary cash and funding (derived, H1 FY27): operating cash flow 108.16 (C 328.46 - S 220.30); repaid the parent 51.75 (S cash flow line 394, matching the S non-current loans fall 127.85 to 76.10); repaid external term debt 46.91 (C 64.49 - S 17.58). The parent's investment in subsidiaries is 16.10 (line 292); consolidation eliminates both the 16.10 and the 76.10 of loans.

## 5. FORWARD-SIGNAL AND AMBIGUOUS FLAGS FOR A4
- FORWARD-SIGNAL: A3-09 (zero-tax earnings; ETR step-up risk; reported EPS overstates statutory-rate EPS by about 25%).
- AMBIGUOUS (convert to management questions): A3-01, A3-04, A3-05, A3-06, A3-08, A3-10, A3-11, A3-12, A3-14, A3-16.

```yaml
stage: A3-forensics
company: "INDORAMA"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indorama-q2fy27/work/forensics_results_indorama_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "211, 605", classification: "AMBIGUOUS", implication: "Employee-benefit exceptional 2.69 S / 2.70 C in H2 FY26; line retained; ask nature and whether further scheme planned"}
  - {id: "A3-02", check: "F1", line: "614", classification: "NEUTRAL-FACT", implication: "NCI nil all periods; four subsidiaries wholly owned (implied)"}
  - {id: "A3-03", check: "F1", line: "399, 791", classification: "NEUTRAL-FACT", implication: "No new term debt (H1 FY26 44.00) and no PPE sales in H1 FY27; debt fall is pure repayment"}
  - {id: "A3-04", check: "F2", line: "609, 215", classification: "AMBIGUOUS", implication: "PAT gap % of S PAT 34.6% Q2 FY27 vs 88.9% Q1 FY27 vs 6.6% Q2 FY26; subs 25.7%-47.1% of C PAT with no entity split"}
  - {id: "A3-05", check: "F2", line: "594, 200", classification: "AMBIGUOUS", implication: "Subsidiary stock-in-trade purchases 74.11 in Q2 FY27; subsidiary revenue is trading-led, earnings ride trading margin and inventory timing"}
  - {id: "A3-06", check: "F2", line: "690, 300", classification: "AMBIGUOUS", implication: "C receivables 103.06 below S 285.60; at least 182.54 (63.9%) of parent receivables are intercompany, up at least 46.16 in H1"}
  - {id: "A3-07", check: "F2", line: "699, 309", classification: "NEUTRAL-FACT", implication: "C other equity 44.59 below S at 31 Mar 2026, +4.43 at 30 Sep 2026; subsidiary deficit erased by H1 profit"}
  - {id: "A3-08", check: "F3", line: "596, 593, 680", classification: "AMBIGUOUS", implication: "Subs hold 355.79 PPE but payroll 1.41/qtr and C materials below S in 4 of 6 periods; partial-shell or trading-vehicle signature; per-entity split ND"}
  - {id: "A3-09", check: "F8", line: "213, 214, 295", classification: "FORWARD-SIGNAL", implication: "S ETR 0% all periods, DTA frozen at 258.61; H1 FY27 shield 22.35 S / 34.85 C (~2,517-2,533 bps); C H1 EPS at statutory rate 3.94 vs reported 5.28; ETR step-up risk"}
  - {id: "A3-10", check: "F8", line: "608, 685, 704", classification: "AMBIGUOUS", implication: "C DTA +9.59 and new DTL 9.37 net to the 0.22 credit; first subsidiary-level tax line; ask entity and cause"}
  - {id: "A3-11", check: "F12", line: "701, 706, 774", classification: "AMBIGUOUS", implication: "C borrowings -271.47 (-24.0%) funded by receivables -57.6% (~7 days of sales); WC unwind vs durable deleveraging; ask factoring/discounting and H2 repeat"}
  - {id: "A3-12", check: "F12", line: "694, 709", classification: "AMBIGUOUS", implication: "Other financial assets 21.3% and trade payables 46.7% of C total assets (~126 days of purchases); composition, related-party share and cost undisclosed; payables may be debt-like"}
  - {id: "A3-13", check: "F14", line: "57, 59", classification: "NEUTRAL-FACT", implication: "Item b heading says Audited, body says Un-audited; template carryover"}
  - {id: "A3-14", check: "F14", line: "460-461, 505, 811", classification: "AMBIGUOUS", implication: "Review report para 1 says its subsidiary (singular) while para 4 lists four; possible perimeter change since template set"}
  - {id: "A3-15", check: "F14", line: "225, 415, 63", classification: "NEUTRAL-FACT", implication: "Duplicate Note 1/Note 2 numbering and 14:35 PM time format; cosmetic, cumulative governance data point"}
  - {id: "A3-16", check: "F15", line: "506-509", classification: "AMBIGUOUS", implication: "Four subsidiaries, prior list ND so no diff possible; ask entry date and any rename/reclassification in last four quarters"}
forward_signals: ["A3-09"]
ambiguous: ["A3-01", "A3-04", "A3-05", "A3-06", "A3-08", "A3-10", "A3-11", "A3-12", "A3-14", "A3-16"]
commitments:
  - {commitment: "Publish extract of unaudited Q2/H1 FY27 results in newspapers (Reg 47(1)(b))", implied_date: "not stated in filing; statutory Reg 47 window after 16 Oct 2026", ref: "Board outcome item b, lines 57-60 (R667)", status_word: "initiated"}
  - {commitment: "Publish extract on www.indoramaindia.com", implied_date: "not stated in filing", ref: "Board outcome item b, line 60 (R668)", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Three reads matter for A4. First, every rupee of reported profit is pre-tax: standalone tax is nil in all six periods while the 258.61 DTA did not move, so at 25.17% consolidated H1 EPS is 3.94, not 5.28. The tax-loss pool size is NOT FOUND here; the AR tax note decides how long the shield runs. Second, the subsidiaries supplied 25.7%-47.1% of consolidated PAT, run on trading purchases and 1.41 of payroll a quarter, and owe the parent at least 182.54 of receivables. The quarter's earnings mix and the parent's receivable quality both depend on four wholly owned entities with no per-entity disclosure. Third, the 271.47 debt fall came from a receivable release to about 7 days of sales, with payables at about 126 days. Until the factoring and acceptance terms are known, A3 treats it as working-capital timing, not proven deleveraging. Limits: prior quarter ND, so the F5 and F15 diffs did not run. R145/R478 are mislabelled H1 FY26; they are the 31 Mar 2026 balances."
```
