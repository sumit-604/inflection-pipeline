# A3 FORENSIC NOTES: DYCL q2fy27 (doctype: results)

Company: Dynamic Cables Limited (DYCL; BSE 540795, NSE DYCL)
Filing: Q2 / H1 FY27 unaudited standalone results, board meeting 27 Oct 2026 (fulltext line 35), limited review by A Bafna & Co (line 84)
Units: Rs Lakhs throughout (x0.01 = Rs Crore). Statement values are cited at the [RENDER-CORRECTED] lines (BS lines 201-238, P&L lines 329-357, CF lines 458-514), which govern.
Inputs read: A1 structured (R001-R482, all rows), A1 fulltext (lines 1-519, all), A2 ledger (all sections). Prior-quarter fulltext: none (first quarterly review of this name). Notion checklist: none; operator batch watch list (7 items) used instead. No source PDF and nothing under inputs/ was opened.
Model: claude-opus-5-5

## 0. LEDGER RECONCILIATION

| Ledger section | Structured IDs | Read at fulltext line | Result |
|---|---|---|---|
| Notes (12) | R466-R474, R480-R482 | 359-367, 516-518 | all read; ledger cross-refs (R380, R381-R384, R385-R387, R432, R478) verified |
| Line items (124 items) | R001-R359 | BS 201-238, P&L 329-357, CF 458-514 | all read; values match render-corrected rows |
| Zero-standing (62 cells, 23 items) | as tagged | 204, 215, 224, 225, 227, 333, 341, 349-351, 462, 463, 467-469, 471, 472, 474-476, 488, 491, 505 | all read; covered in F1 |
| Agenda / meeting / trading window | R456, R457, R366, R367, R431, R438, R361 | 35-48 | read |
| Admin / letter header | R360, R362-R365, R395-R403, R433-R439 | 21-76 | read |
| Auditor paragraphs | R458-R462, R404-R410, R369-R377, R413, R415, R417, R440, R441 | 78-132 | read; no EoM / Other Matter / Going Concern text |
| Entities | R395-R430 | 22-519 | read; no subsidiary, JV or associate |
| Dates / forward / qualifiers | R431-R482 | as cited | read |

ids_in_structured 482; ids_referenced_in_ledger 482; ids read by A3 482. ledger_reconciled_pct = 100.
Ledger disagreements: none. Minor anchor note: R431 cites line 41; the sentence runs lines 40-44. No effect on any finding.

Independent tie-outs run by A3 (all Rs Lakhs):
- Other equity roll-forward: 40,878.40 (line 220) + TCI H1 4,693.10 (line 353) - dividend 242.29 (line 506) + ESOP charge 32.86 (line 476) = 45,362.07 vs 45,362.09 printed (line 220). Diff 0.02. PASS.
- DTA roll-forward: 129.52 + P&L credit 30.89 + OCI tax 5.85 = 166.26 vs 166.27 (line 206). PASS.
- Current tax liability: 303.76 + 1,634.40 - 1,605.10 = 333.06 vs 333.04 (line 236). PASS.
- Capex: change in (PPE + CWIP + intangibles) 1,275.34 + D&A 633.84 + disposals at WDV 42.92 (50.13 proceeds less 7.21 profit) = 1,952.10 vs cash capex 1,952.11 (line 496). PASS.
- Finance cost: P&L H1 710.51 (line 336) = CF finance cost 696.97 paid (line 510) + lease interest 13.54 (line 466). The CF adjustment line prints 696.90 (line 477), 0.07 short.

## 1. FINDINGS TABLE

Derived ratios used below (A3 arithmetic on cited rows):
- Materials net of inventory change, % of revenue: Q2 FY27 83.29% | Q1 FY27 80.60% | Q2 FY26 79.25% | FY26 80.48%
- Other expenses, % of revenue: Q2 FY27 3.09% | Q1 FY27 4.56% | Q2 FY26 5.43% | FY26 4.84%
- Materials + other expenses combined: Q2 FY27 86.37% | Q1 FY27 85.17% | Q2 FY26 84.68%
- EBITDA (PBT + finance cost + D&A - other income): Q2 FY27 3,635.17 (10.01%) | Q1 FY27 3,799.92 (10.88%) | Q2 FY26 3,082.13 (10.95%) | H1 FY27 7,435.09 (10.44%) | H1 FY26 5,776.86 (10.63%) | FY26 12,955.62 (10.82%)
- Revenue: Q2 +29.0% YoY, +4.0% QoQ; H1 +31.0% YoY. PAT: Q2 +12.8% YoY, -11.2% QoQ.

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R197-R214; R272 | 349-351; 471 | "PL\|X(b)(i) Items that will be reclassified to Profit or Loss \| - \| - \| - \| - \| - \| -" ; "CF\|Unrealized foreign exchange (gain)/loss \| (56.70) \| \| - \|" | AMBIGUOUS | The reclassifiable OCI line is nil in all six periods. So no cash-flow hedge is designated, although the business converts copper and aluminium and a forex line appears for the first time in H1 FY27 (56.70 gain vs nil in H1 FY26). Metal and currency moves then hit P&L in the quarter they happen. This fits the Q2 spread compression (A3-13). Ask: is metal price hedged (LME or back-to-back), and is the hedge designated? What creates the new forex exposure: metal imports, export receivables, or buyer's credit? |
| A3-02 | F1 | R101-R106, R149-R154, R254-R257, R264-R269, R278-R279, R340-R341, R007-R008, R029-R030, R047-R050, R053-R054 | 333; 341; 462; 463; 469; 505 | "PL\|VI Exceptional items \| - \| - \| - \| - \| - \| -" ; "CF\|Commission income against Financial Liability \| - \| \| - \|" ; "CF\|Proceeds from Preferential allotment \| - \| \| - \|" | NEUTRAL-FACT | The template lines expect four transaction classes. (a) Exceptional items: none in 6 periods. (b) Stock-in-trade purchases: nil, so the company is a pure manufacturer with no traded revenue. (c) Commission income against a financial liability, and other income / interest cost on security deposits received: these are Ind AS 109 lines for a financial guarantee and for discounted deposits. Both H1 periods are nil. (d) Proceeds from preferential allotment: the line stays from the June 2024 issue (Note 6). Check at the AR: any corporate guarantee given or received, with the counterparty named. |
| A3-03 | F6 | R471, R380, R448, R449; R013-R014, R031-R032 | 364; 207; 216 | "The proceeds of the issue have been fully utilized in accordance with the stated objects of the issue, including advances, as at September 30, 2026." | AMBIGUOUS | Status word "completed". The Rs 9,658.79 Lakhs (19.2% of current equity, line 221) is reported as fully used, 27 months after the June 2024 raise. But "including advances" means part of the use is cash paid out ahead of asset delivery. Other non-current assets rose 58.5% (373.46 to 591.88, line 207), other current assets rose 43.8% (2,356.25 to 3,388.20, line 216), and CWIP stands at 3,420.54 (line 202). [INFERENCE] The issue is just under Rs 100 Cr, so a monitoring-agency report may not be required; A4 to verify the ICDR threshold before relying on it. Ask: how much of the 9,658.79 still sits as advances, and to whom? |
| A3-04 | F6 | R473, R432, R478, R451; R051-R052 | 366; 226 | "The Company continues to monitor the finalisation of Central/State Rules ... and would provide appropriate accounting effect (if any) on the basis of such developments as needed." | FORWARD-SIGNAL | Status word "underway". The commitment is open, with the trigger set as the date Central and State Rules are finalised. No charge is booked to date, even though the Codes were notified 21 Nov 2025 (line 366). Non-current provisions rose 14.7% in H1 (308.40 to 353.68, line 226). [INFERENCE] If the final wage definition widens the gratuity and leave base, a one-time past-service charge would land in a future quarter, possibly through the nil exceptional line (A3-02). Feeds the promise-vs-delivery tracker. |
| A3-05 | F7 | R473, R478 | 366 | "there is no material impact of these changes and to the best information available" | AMBIGUOUS | No strict lexicon hit anywhere in the notes; the "subject" hit, "subjected to limited review" (line 362), is boilerplate. Note 8 uses hedge-equivalent qualifiers ("to the best information available", "(if any)", "as needed"). These cover the nil-impact conclusion itself, not only the future accounting. No prior-quarter text exists, so A3 cannot tell whether the qualifier is new. Ask: what gratuity and leave base, and what wage-definition reading, did the nil-impact assessment use? |
| A3-06 | F9 | R179-R184, R270 | 346; 470 | "PL\|X(a)(i) Items that will not be reclassified to Profit or Loss \| 18.33 \| (41.58) \| 10.38 \| (23.25) \| (22.02) \| (12.12)" | NEUTRAL-FACT | Each FY27 quarter's actuarial swing is larger than the whole FY26 figure: Q1 (41.58) is 3.4x and Q2 +18.33 is 1.5x FY26's (12.12). The QoQ reversal is 59.91. The amounts are immaterial (Q2 is 0.83% of PAT). This pattern points to quarterly re-measurement on a moving discount rate. Verify discount-rate and salary-escalation assumptions at the FY27 AR, together with the Labour Code base (A3-04). |
| A3-07 | F10 | R227-R232, R234-R245, R472, R381-R383, R282 | 354; 356-357; 365; 476 | "PL\|XIV(2) Diluted EPS (in INR) \| 4.56 \| 5.15 \| 4.05 \| 9.71 \| 7.81 \| 17.42" ; "the granted options have reduced to 183405" | NEUTRAL-FACT | Paid-up capital is 4,845.86 (48,458,600 shares) in all six periods, with no corporate action. A basic-diluted spread shows for the first time in Q2 FY27 (4.57 vs 4.56; H1 9.72 vs 9.71); it was nil in Q1 FY27 and earlier. [INFERENCE] The DCL-ESOP 2024 options at Rs 324 became dilutive in Q2 under the treasury method. The maximum is 183,405 options, which is 0.38% dilution and Rs 594.23 Lakhs on exercise. 16,595 grants (8.3%) lapsed "due to the change in number of employees". A4 to cross-check against the thesis. |
| A3-08 | F14 | R469, R475, R453 | 362; 328 | "the unpublished year to date figures upto 30th June 2026" | NEUTRAL-FACT | Note 4 calls the Q1 FY27 figures "unpublished". The same statement prints the 30-06-2026 column (line 328), and that column was reported last quarter. The wording reads as carried-over boilerplate. The point that matters is that Q2 is a balancing figure (H1 less Q1). So any H1 regrouping under Note 5 (line 363) lands entirely in the Q2 column (see A3-13). Note 5 also has a typo ("in order to confirm to the presentation"). Immaterial alone; one governance data point. |
| A3-09 | F14 | R282-R287, R314-R315, R350, R352 | 477; 478; 492; 510; 511 | "CF\|Finance Cost \| 696.90 \| \| 543.25 \|" ; "CF\|Finance Cost \| (696.97) \| \| (543.25) \|" | NEUTRAL-FACT | The cash flow has four small casting gaps in the printed figures. Adjustment-line finance cost 696.90 vs 696.97 paid (P&L 710.51 less lease interest 13.54 = 696.97). Adjustments subtotal 1,339.44 vs line sum 1,339.38. H1 FY26 working-capital lines sum (2,855.89) vs printed (2,855.94). Financing lines sum (1,246.81) vs printed (1,246.82). All are under 0.1 Lakh and immaterial. Together they suggest the statement is compiled by hand. |
| A3-10 | OBS (watch item 4) | R017-R018, R107-R112, R290, R292, R320-R321, R021-R022 | 209; 334; 480; 481; 495 | "BS\|Inventories \| 24,343.32 \| 17,278.62" ; "CF\|Net Cash Inflow/(outflow) from Operating Activities (A) \| \| 666.37 \| \| 2,018.63" | FORWARD-SIGNAL | Inventory rose 40.9% in six months (+7,064.70). Q2 revenue grew only 4.0% QoQ. FG/WIP alone built 4,974.34 in H1, which is 148% of all FY26's 3,366.75 (line 334). Inventory days 76.1 vs 65.4 at Mar-26 (H1-annualised COGS basis). Receivable days 70.3 vs 87.7, payable days 52.6 vs 60.3, so the net cycle is about flat (93.8 vs 92.8 days); the mix moved from receivables to inventory. OCF/EBITDA 9.0% vs 34.9% in H1 FY26; OCF/PAT 14.1% vs 53.3%. Two readings: (a) order-backed pre-build for H2 dispatch, or (b) slower offtake or deferred dispatch. Separating observation: H2 revenue and an inventory unwind by the Q4 balance sheet. Lean bear until then. |
| A3-11 | OBS (watch item 5) | R019-R020, R336, R258-R259, R322, R083-R088 | 210; 503; 464; 496; 330 | "BS\|Current financial assets - Investments \| 92.85 \| 3,062.04" ; "CF\|Unrealized Gain (Loss) on Fair Value Of MF (Indirect Income) \| 134.80 \| \| (27.91) \|" | FORWARD-SIGNAL | Mutual-fund holdings fell from 3,062.04 to 92.85: CF realisation 2,834.58 plus a 134.80 non-cash add-back (the sum, 2,969.38, ties to the 2,969.19 fall). That cash funded H1 capex of 1,952.11 and the inventory build. FCF is (1,235.61), against (516.13) in H1 FY26. Net cash of about 1,844 at Mar-26 became net debt of about 409 at Sep-26 (gross debt less cash, other bank balances and MF; the bank balances may be lien-marked). H1 other income fell 43% (392.32 to 223.27). The treasury buffer is used up, so the next build of working capital or capex needs borrowing. The 134.80 add-back carries the "Gain (Loss)" label but a loss sign (it was a gain in H1 FY26). Ask whether it is a fair-value loss or a reversal of earlier gains on redemption, and where it sits in P&L. |
| A3-12 | OBS (watch item 5) | R119-R124, R043-R044, R057-R058, R025-R026, R063-R064 | 336; 222; 229; 213 | "PL\|IV(e) Financial Costs \| 424.64 \| 285.87 \| 286.11 \| 710.51 \| 552.44 \| 1,148.42" | AMBIGUOUS | Finance cost rose 48.5% QoQ and 48.4% YoY. Period-end borrowings fell over the same span, from 4,038.99 to 3,731.43 (lines 222 + 229). Q2 annualised finance cost (1,698.56) is 45.5% of closing gross debt, and FY26 was 28.4%. [INFERENCE] That rate is far above any plausible bank rate. So either average debt within the quarter runs well above period-end levels, or finance cost includes LC/BG commission, bill-discounting or acceptance interest that never shows as borrowings. Other bank balances (likely margin money) rose 408.50 to 3,214.44 (line 213), and trade payables rose to 16,819.51. Lean bear: the real funding used is larger than balance-sheet debt. Ask for a split of finance cost, average utilisation of working-capital limits, and LC acceptances held in trade payables. |
| A3-13 | OBS (watch items 1, 3) | R095-R100, R107-R112, R131-R136, R469, R470 | 332; 334; 338; 362; 363 | "PL\|IV(g) Other Expenses \| 1,120.51 \| 1,593.18 \| 1,529.01 \| 2,713.69 \| 2,911.59 \| 5,802.72" | AMBIGUOUS | Materials net of inventory change took 83.29% of revenue, up 269 bps QoQ and 404 bps YoY. Other expenses fell to 3.09% of revenue: down 29.7% QoQ and 26.7% YoY in Rs terms, while revenue grew 29%. Combined, the two lines still worsened 120 bps QoQ and 169 bps YoY. So the EBITDA margin fell to 10.01% from 10.88% QoQ and 10.95% YoY, and absolute EBITDA grew only 17.9% YoY against revenue +29.0%. Two readings: (a) H1 regrouping of freight or packing from other expenses into materials (Note 5), all landing in the Q2 balancing figure (Note 4), or (b) metal-price pass-through inflating revenue at a thinner spread. No volume or tonnage figure is disclosed. Ask for Q2 volume (km or tonnes), realisation per unit, and any H1 reclassification. |
| A3-14 | OBS (watch item 5) | R125-R130, R001-R004, R013-R014, R322 | 337; 201; 202; 207; 496 | "PL\|IV(f) Depreciation and amortisation expense \| 347.67 \| 286.17 \| 281.42" | FORWARD-SIGNAL | D&A rose 21.5% QoQ, a step change, so assets were capitalised in or just before Q2. Net PPE rose 1,111.45 (line 201). CWIP still grew to 3,420.54 (line 202), and capital advances (other non-current assets) rose 58.5%. Capex 1,952.11 ties exactly to the gross-block movement and had no new net borrowing behind it. [INFERENCE] New capacity is coming on stream and about Rs 34 Cr more is still in CWIP. Watch utilisation of the new block against the H2 revenue run-rate. Ask which line or plant was commissioned, its date and capacity, and the timeline for the remaining CWIP. |
| A3-15 | OBS (watch items 1, 2, 6, 7) | R468, R456-R457 | 361; 36-38 | "The Company's business activity fall within a single primary business segment." | NEUTRAL-FACT | The filing does not disclose volume, order book, customer mix (utilities / EPC / exports), capacity, or promoter holding and pledge. It shows a single segment and a board agenda limited to results. Each of these is NOT FOUND in this document. A4 to source them from the concall, the presentation or the shareholding filing; not estimated here. |

Finding count: 15 total. FORWARD-SIGNAL 4 (A3-04, A3-10, A3-11, A3-14); AMBIGUOUS 5 (A3-01, A3-03, A3-05, A3-12, A3-13); CONFIRMATORY-NEGATIVE 0; NEUTRAL-FACT 6 (A3-02, A3-06, A3-07, A3-08, A3-09, A3-15).
A3-10 to A3-15 are supplementary observations outside the F1-F17 taxonomy. They are tied to the operator watch list and do not change any checklist status.
Flagged for A4 management questions: A3-01, A3-03, A3-04, A3-05, A3-10, A3-11, A3-12, A3-13, A3-14.

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 23 zero-standing items (62 cells) read. OCI(b) nil despite metal/forex exposure (A3-01). Exceptional, stock-in-trade, guarantee, security-deposit and preferential-allotment template lines (A3-02). |
| F2 Standalone vs consolidated | N.A. | Standalone-only filing: "Standalone Financial Results" (line 84); no consolidated statement, no subsidiary/JV/associate disclosed (R395-R430). |
| F3 Shell-entity detection | N.A. | No consolidated cost lines to compare; no group entities disclosed. |
| F4 Unaudited contribution ratio | PASS | Review report (lines 90-122) has no Other Matters paragraph and no component auditors or management-certified entities. 0% of PAT rests on numbers the auditor did not review. |
| F5 Going concern / EoM tracking | PASS | Conclusion unmodified (line 112, Note 1 line 359); no EoM or Going Concern text. Prior-quarter verbatim diff not possible (no prior extract); the current-quarter absence is verified directly. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits are template labels "will be reclassified" (349-350), meeting "commenced" (48) and "shall remain closed" (40). Live commitments: Note 6 completion "including advances" (A3-03), Note 8 open accounting effect (A3-04), trading window (register only). |
| F7 Hedge phrases | FINDING | No strict lexicon hit. Note 8 hedge-equivalent qualifiers on the nil-impact conclusion (A3-05). |
| F8 Tax forensics | PASS | ETR (current + deferred) Q2 25.36%, Q1 25.43%, Q2 FY26 25.44%, H1 25.40%, FY26 25.32%, all above statutory 25.17%. Deferred tax is a credit in all six periods, but small: shield 15 bps of PBT in Q2, 49 bps in H1, 52 bps in FY26. These are timing items (DTA 129.52 to 166.27 ties), not carry-forward losses. No earlier-years tax line; interest on income tax nil (line 468). |
| F9 OCI forensics | FINDING | Single-quarter actuarial swings larger than the full prior year (A3-06); immaterial; AR assumption check. |
| F10 Share count and dilution | FINDING | Paid-up unchanged in all six periods. Basic-diluted spread first appears in Q2 FY27 (A3-07). |
| F11 Reserves and net worth tie-out | PASS | 45,362.09 + 4,845.86 = 50,207.95 (lines 219-221); Mar-26 40,878.40 + 4,845.86 = 45,724.26. Roll-forward diff 0.02. No third-party net worth figure in context; no revaluation or warrant reserve shown. |
| F12 Segment forensics | PASS | Single primary segment (Note 3, line 361); no segment assets or liabilities table exists. Nothing to trend. The missing product/customer mix is logged in A3-15. |
| F13 Board outcome beyond results | PASS | Only agenda item: approve results and take the LRR on record (lines 35-38). No AR, AGM, dividend, director, auditor, ESOP or fund-raise item. Meeting ran 35 minutes (line 48). Trading window to 48h after dissemination (line 43). |
| F14 Note drafting inconsistencies | FINDING | Note 4 "unpublished" Q1 figures (A3-08); cash-flow casting gaps (A3-09). Note 1 "limited review" matches the auditor letter (line 84). Entity name consistent across pages. |
| F15 Entity list diffs | N.A. | No consolidation list in a standalone filing; no prior extract; ledger records ENTITY_CHANGE not assessable. |
| F16 Presentation: dropped / reframed disclosures | N.A. | Results doctype. |
| F17 Concall: silence audit | N.A. | Results doctype. Watch-list coverage logged for A4 in section 4. |

GATE A3: pass. No blank checks.

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | note / line ref | status word |
|---|---|---|---|
| Preferential issue proceeds Rs 9,658.79 Lakhs (June 2024) fully used per stated objects, "including advances"; no unused proceeds | as at 30 Sep 2026 | Note 6, line 364 (R471) | completed (with advances; conversion to assets open) |
| Labour Codes: continue to monitor Central/State Rules and "provide appropriate accounting effect (if any)" | on finalisation of Central/State Rules (undated) | Note 8, line 366 (R432, R473) | underway |
| DCL-ESOP 2024: 183,405 options outstanding at Rs 324; expensed under Ind AS 102 (H1 charge 32.86, line 476) | vesting schedule NOT DISCLOSED | Note 7, line 365 (R472) | underway |
| Trading window closed for designated persons | until 48 hours after dissemination (about 29 Oct 2026) | lines 40-44 (R431, R438) | initiated |

## 4. WATCH-LIST COVERAGE (operator batch brief; no Notion page; F17 N.A. on results)

| watch item | what the filing shows | ref |
|---|---|---|
| 1 Volume vs metal pass-through | No volume disclosed. Revenue +29.0% YoY with materials share up 404 bps reads as price-led; NOT FOUND on volume | A3-13 |
| 2 Order book | NOT FOUND | A3-15 |
| 3 EBITDA per unit / margin | EBITDA margin 10.01% Q2 vs 10.88% Q1 vs 10.95% Q2 FY26; per-unit NOT FOUND | A3-13 |
| 4 WC days and OCF | Inventory 76.1 days (from 65.4), receivables 70.3 (from 87.7), payables 52.6 (from 60.3); OCF 666.37 vs 2,018.63 | A3-10 |
| 5 Capacity and funding | Capex 1,952.11; CWIP 3,420.54; D&A +21.5% QoQ; funded by MF redemption; finance cost +48.5% QoQ | A3-11, A3-12, A3-14 |
| 6 Customer mix | NOT FOUND; first-time forex line (56.70) hints at an import or export exposure | A3-01, A3-15 |
| 7 Promoter holding / pledge | NOT FOUND in this filing | A3-15 |

```yaml
stage: A3-forensics
company: "DYCL"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/dycl-q2fy27/work/forensics_results_dycl_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: PASS
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "349-351; 471", classification: "AMBIGUOUS", implication: "OCI(b) nil in all 6 periods: no designated cash-flow hedge despite Cu/Al exposure; first-time forex gain 56.70 in H1. Metal and FX moves hit P&L directly. Ask hedge policy and source of FX exposure."}
  - {id: "A3-02", check: "F1", line: "333; 341; 462; 463; 469; 505", classification: "NEUTRAL-FACT", implication: "Exceptional, stock-in-trade, guarantee-commission, security-deposit and preferential-allotment template lines nil; pure manufacturer; check any guarantee given at AR."}
  - {id: "A3-03", check: "F6", line: "364; 207; 216", classification: "AMBIGUOUS", implication: "Rs 9,658.79 L preferential proceeds 'fully utilized ... including advances'; part may sit as advances (other NC assets +58.5%, other CA +43.8%). Ask advance balance and counterparties."}
  - {id: "A3-04", check: "F6", line: "366; 226", classification: "FORWARD-SIGNAL", implication: "Labour Code accounting effect left open pending final Rules; NC provisions +14.7% in H1; a possible past-service charge lands in a future quarter."}
  - {id: "A3-05", check: "F7", line: "366", classification: "AMBIGUOUS", implication: "Nil-impact conclusion hedged 'to the best information available' and '(if any)'. Ask the wage-definition basis of the assessment."}
  - {id: "A3-06", check: "F9", line: "346; 470", classification: "NEUTRAL-FACT", implication: "Q1 (41.58) and Q2 +18.33 actuarial swings each exceed FY26 total (12.12); immaterial (0.83% of PAT); verify discount-rate assumptions at the FY27 AR."}
  - {id: "A3-07", check: "F10", line: "356-357; 365", classification: "NEUTRAL-FACT", implication: "Basic/diluted spread first appears in Q2 (4.57/4.56); ESOP 183,405 options at Rs 324 now dilutive; max 0.38% dilution; 8.3% of grants lapsed."}
  - {id: "A3-08", check: "F14", line: "362; 328", classification: "NEUTRAL-FACT", implication: "Note 4 calls the published Q1 figures 'unpublished'; boilerplate. Q2 is a balancing figure, so any H1 regrouping lands wholly in Q2."}
  - {id: "A3-09", check: "F14", line: "477; 478; 492; 510; 511", classification: "NEUTRAL-FACT", implication: "Four CF casting gaps under 0.1 L (finance cost 696.90 vs 696.97 paid); immaterial; suggests a hand-compiled statement."}
  - {id: "A3-10", check: "OBS-watch4", line: "209; 334; 480; 495", classification: "FORWARD-SIGNAL", implication: "Inventory +40.9% in H1 (FG/WIP build 4,974.34 = 148% of FY26) vs Q2 rev +4.0% QoQ; inventory days 76.1 vs 65.4; OCF/EBITDA 9.0% vs 34.9%. Pre-build vs slow offtake; H2 revenue and Q4 unwind separate the two."}
  - {id: "A3-11", check: "OBS-watch5", line: "210; 503; 464; 496; 330", classification: "FORWARD-SIGNAL", implication: "MF 3,062.04 to 92.85 funded capex 1,952.11 and WC; FCF (1,235.61); net cash ~1,844 L to net debt ~409 L; other income -43%. Next build needs debt. Ask about the 134.80 MF add-back."}
  - {id: "A3-12", check: "OBS-watch5", line: "336; 222; 229; 213", classification: "AMBIGUOUS", implication: "Finance cost +48.5% QoQ while period-end debt fell 4,038.99 to 3,731.43; annualised cost 45.5% of closing debt. Intra-quarter debt or LC/discount charges exceed what the BS shows. Ask for the split."}
  - {id: "A3-13", check: "OBS-watch1-3", line: "332; 334; 338; 362; 363", classification: "AMBIGUOUS", implication: "Materials 83.29% of rev (+269 bps QoQ); other exp fell to 3.09%; combined +120 bps QoQ; EBITDA margin 10.01% vs 10.88%/10.95%. Regrouping into Q2 balancing figure vs thinner pass-through spread. Ask volume and reclassification."}
  - {id: "A3-14", check: "OBS-watch5", line: "337; 201; 202; 207; 496", classification: "FORWARD-SIGNAL", implication: "D&A +21.5% QoQ = capitalisation; CWIP still 3,420.54; capital advances +58.5%. New capacity is on stream; ask asset, date, capacity, and CWIP timeline."}
  - {id: "A3-15", check: "OBS-watch1-2-6-7", line: "361; 36-38", classification: "NEUTRAL-FACT", implication: "Volume, order book, customer mix, capacity, promoter holding/pledge NOT FOUND in filing; A4 sources from concall/deck/shareholding."}
forward_signals: ["A3-04", "A3-10", "A3-11", "A3-14"]
ambiguous: ["A3-01", "A3-03", "A3-05", "A3-12", "A3-13"]
commitments:
  - {commitment: "Preferential issue proceeds Rs 9,658.79 L fully utilised per objects, including advances", implied_date: "as at 2026-09-30", ref: "Note 6, line 364 (R471)", status_word: "completed"}
  - {commitment: "Provide Labour Code accounting effect (if any) on finalisation of Central/State Rules", implied_date: "on Rules finalisation (undated)", ref: "Note 8, line 366 (R432)", status_word: "underway"}
  - {commitment: "DCL-ESOP 2024: 183,405 options at Rs 324 expensed under Ind AS 102", implied_date: "vesting NOT DISCLOSED", ref: "Note 7, line 365 (R472)", status_word: "underway"}
  - {commitment: "Trading window closed for designated persons", implied_date: "48h after dissemination (~2026-10-29)", ref: "lines 40-44 (R431)", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "The quarter's forward signal is in working capital, not the notes. Inventory rose 40.9% in six months (line 209) while Q2 revenue grew 4.0% QoQ; the H1 FG/WIP build of 4,974.34 (line 334) already exceeds all of FY26. Two readings: order-backed pre-build for H2 dispatch, or slower offtake. H2 revenue against an inventory unwind by Q4 separates them. Liquidating about Rs 29.7 Cr of mutual funds (lines 210, 503) paid for the build and the capex, so the balance sheet moved from about Rs 18 Cr net cash to about Rs 4 Cr net debt; the next build needs borrowing. Finance cost rose 48.5% QoQ while period-end debt fell (line 336 vs 222/229). The implied rate is too high for bank debt alone, so intra-quarter borrowing or LC/discounting charges exceed what the balance sheet shows. Materials plus other expenses rose 120 bps QoQ; the 147 bps fall in other expenses (line 338) may be a regrouping landing wholly in the Q2 balancing figure (Notes 4, 5). The notes themselves are clean: no EoM, ETR about 25.4%, equity ties to 0.02."
```
