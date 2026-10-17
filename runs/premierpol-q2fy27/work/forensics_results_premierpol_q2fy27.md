# A3 FORENSIC NOTES: PREMIERPOL Q2 FY27 (doctype: results)

Company: Premier Polyfilm Limited (NSE PREMIERPOL, BSE 514354). Standalone only (Note 5, line 158).
Inputs read: A1 structured (R001-R401), A1 fulltext (body lines 1-522), A2 ledger (corrected loop 1, section 10A rows X001-X012). Source PDF and inputs/ not opened.
Prior-quarter fulltext: not available (ND). Notion checklist: not available (PRE-THESIS READ, no companies/PREMIERPOL.md, no spear).
Units: Rs Lakhs unless stated. "Derived" = arithmetic on filed cells only. No cell is filled by estimate.
Line numbers are the A1 body-line prefixes in the fulltext file.

CORRECTION LOOP 1 (A5-M2). Named fixes only: (1) R312 / R314 CIN_OCR_MISMATCH disposed in section 0A; (2) R316 UDIN_UNRESOLVED disposed into F-03 (F5); (3) ledger rows X001-X012 read at their fulltext lines and carried into the F1 register (section 3), F-01 and F-13. No other finding, number or classification changed.

## 0. LEDGER RECONCILIATION (413 of 413 rows read at cited line: R001-R401 plus X001-X012)

| ledger block | IDs | fulltext lines read | result |
|---|---|---|---|
| P&L line items | R001-R134 | 75-110 | All casts tie. TOTAL INCOME, TOTAL EXPENSES, PBT, tax, PAT, TCI tie in all six columns. |
| Page 3 items | R135-R190 | 126-149 | Paid-up 1,059 constant. EPS below PAT/paid-up (F-06). |
| Cash flow | R191-R226 | 189-298 | OCF 2,525 - 726 = 1,799; 1,799 - 477 = 1,322; investing 1 - 581 + 2 + 76 - 455 = (957); financing (147) - 32 = (179); 1,322 - 957 - 179 = 186; 504 + 186 = 690. All tie. |
| Balance sheet | R227-R310 | 320-398 | Totals tie. Four 30/09 line items do not cast to their subtotals (F-10). |
| Identifiers | R311-R319 | 5, 6, 21, 35, 67, 174, 513, 514, 515 | R312 / R314 disposed in 0A (no finding). R316 UDIN unreadable, carried into F-03. |
| Entities | R320-R342 | 2-62, 152-172, 415-483 | Four product lines (line 62) vs single-product Note 3 (line 155). |
| Dates | R343-R361 | 10-516 | All signing dates 10-10-2026 = board date. "32-03-2026" (line 71) is OCR; line 114 reads 31-03-2026. |
| Qualifiers / notes | R362-R401 | 18-521 | Notes 1-5 lines 152-158. Auditor text lines 428-502 garbled. |
| Section 10A additions | X001-X012 | 86, 94, 96, 98, 104, 105, 106, 128, 373, 377, 390, 393 | All read. 26 zero-standing cells plus 2 blank rows (L94, L128). X003 "2" (L96) feeds no total. Carried into section 3, F-01, F-13. |

A2 open items resolved here:
- R046 (H1FY27 finance cost "At", line 84). Derived 44: TOTAL EXPENSES 19,158 less the other six H1 lines (11,804 + 921 + 65 + 1,708 + 236 + 4,380 = 19,114) = 44; also Q2 24 + Q1 20 = 44. Source cell stays OCR_UNREADABLE.
- R289 (TOTAL NON CURRENT LIABILITIES "6228", line 379). Derived 628: TOTAL LIABILITIES 5,502 less TOTAL CURRENT LIABILITIES 4,874 = 628; also 498 + 130 = 628. The printed DTL "430" does not cast (F-10).
- R141-R146 (Reserves, line 130). Not a column misread. Current-year columns carry 13,661 (= BS Other Equity 31/03/2026, line 361). Prior-year columns and the FY26 column carry 10,728 (reserves at the prior year's audited balance sheet). Roll check: 10,728 + FY26 TCI 3,091 = 13,819 vs 13,661, so FY26 carried a 158 non-TCI reduction (F-07).
- R233 "NON CURRENT FINANCIAL ASSETS 6,407" (line 329). It is the PPE + CWIP + intangibles subtotal (6,009 + 397 + 1 = 6,407; prior 6,011 + 50 + 1 = 6,062). Label misaligned, value ties.

## 0A. FLAGGED IDENTIFIER ROWS (A5-M2, loop 1)

| row | A2 flag | line | verbatim | disposition |
|---|---|---|---|---|
| R312 / R314 | CIN_OCR_MISMATCH | 5 vs 67 | "CIN: L52109DL1992PLC049590" (5); "CIN NO. 152109DL1992PLC049590" (67) | REVIEWED, NO FINDING. The two strings are 21 characters each. Characters 2-21 ("52109DL1992PLC049590") are identical. Only the first character differs: "L" (5) vs "1" (67). A CIN begins with a letter (L = listed), and the page is an OCR text layer (A1 header line 9: GlyphLessFont only). The difference reads as OCR of "L" as "1". Same company, same registration. Not a drafting finding; F-13 no longer counts it. |
| R316 | UDIN_UNRESOLVED | 513-515 | "<uSinbership No. 522310" (513); "UDIN" (514); "Ve <2 2:370 BEA EID 8623" (515) | CARRIED INTO F-03 (F5). The UDIN is the code that authenticates the limited review report. Line 515 is unreadable. It does not even contain the membership number 522310 printed on line 513, so no part of it can be matched. With paragraphs 3-4 also garbled (lines 477-502, R400), this copy cannot authenticate the review report or confirm its conclusion in full. |

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F-01 | F1 | R277, R278, R291, R292, X008, X009 vs R173-R178, R217, R043-R048 | 370, 373, 382, 128, 147, 283, 84 | "Borrowings, non current ... -" (370); "TOTAL NON CURRENT FINANGIAL LIBILITIES . ‘i" (373); "Details of debt securities" (128, blank); "Debt Equity Ratio ... 0.11" (147); "Repayments of borrowings 147.00" (283) | AMBIGUOUS | Both borrowing lines are nil at 30/09/2026 and 31/03/2026. The total non-current financial liabilities subtotal is nil at both dates (373), so no term debt and no Ind AS 116 lease liability sits in non-current. The debt securities line is blank (128), so no listed debt is shown. The filing still prints D/E 0.11 (derived debt about 1,845 = 0.11 x 16,775), DSCR 17.12, finance cost 24 per quarter, and an H1 repayment of 147 with no proceeds line. A 147 repayment needs a borrowing that existed at 31/03/2026. Any debt is therefore unlisted and current, most likely inside Other current financial liabilities 2,363 (line 384). Ask which line carries the debt, its nature (working capital, buyer's credit, lease), and why the borrowing lines read nil. |
| F-03 | F5 | R396-R400, R316 (R315) | 490, 477-485, 513-515 | "attention that causes us to believe" (490); "UDIN" (514) "Ve <2 2:370 BEA EID 8623" (515) | AMBIGUOUS | The visible conclusion fragment reads as a standard unmodified negative-assurance review conclusion. Paragraph 3-4 text between lines 485 and 490 is missing in the text layer. No heading for Emphasis of Matter, Other Matter or Going Concern is visible, but absence cannot be confirmed. The UDIN (515) is unreadable and does not carry the membership number 522310 (513), so this copy cannot authenticate the review report. There is no prior-quarter text, so no verbatim diff is possible. This quarter becomes the baseline. Before Q3 FY27 diffing, obtain a clean copy that confirms no EoM and gives a legible UDIN to verify on the ICAI UDIN portal. |
| F-04 | F8 | R091-R104, R097-R098, X003, X004 | 96, 97, 98, 99 | "Current Tax 330 306 299 636 523 1,079" (97); "Total tax expenses 330 306 299 636 523 1,092" (99) | AMBIGUOUS | ETR Q2FY27 25.17% (330/1,311), Q1FY27 25.21%, Q2FY26 27.18% (299/1,100), H1FY26 27.18%, FY26 25.51%. Total tax equals current tax in all five interim columns, so interim deferred tax is nil. Deferred tax books only at year end (FY26: 13). The 2.01pp YoY ETR drop adds about 26 to Q2FY27 PAT (1,311 x 2.01%), about 3pp of the 22.5% PAT growth (PBT growth 19.2%). This is a base effect, not repeatable once Q3FY26 comparisons apply. No "earlier years" tax line exists. The "2" on the tax header row (96, X003) feeds no total and reads as OCR of a dash. Ask what lifted the FY26 interim ETR to 27.18% (earlier-year tax inside current tax?). Year-end deferred tax true-up risk applies to FY27. |
| F-05 | F9 | R123-R128 | 109 | "Other comprehensive Income net of taxes (218) 384 -145 166 12 (97)" | AMBIGUOUS | Q1FY27 OCI +384 (42% of Q1 PAT 908) and Q2FY27 OCI (218) are each larger than the full FY26 OCI of (97). Derived Q1FY26 OCI = 12 - (-145) = 157. Swings of this size in a company with non-current investments 1,077 and current investments 1,246 (lines 330, 341) point to fair-value moves on FVOCI investments more than to actuarial changes. Composition is not disclosed. TCI (1,292 in Q1, 763 in Q2) is volatile on this line. Verify OCI composition and actuarial assumptions at the FY27 Annual Report. |
| F-06 | F10 | R135-R140, R149-R172, R105-R110 | 126, 139, 145 | "Paid-up Equity Share capital (in Lakhs) 1,059" (126); "Basic earnings ... 0,94 0.87 0.76 1.80 1.34 3.04" (139) | AMBIGUOUS | Face value Rs 1 (line 127), so paid-up 1,059 lakhs = 1,059 lakh shares. Reported EPS is above PAT / 1,059 in five of six columns. Q2FY27: 981/1,059 = 0.926 vs 0.94. FY26: 3,188/1,059 = 3.010 vs 3.04. Implied weighted shares: Q2FY27 about 1,044 (rounding band 1,038-1,049); FY26 about 1,049 (band 1,047-1,050); H1FY27 about 1,049 (band 1,047-1,052). All sit below 1,059, a gap of 9-15 lakh shares (0.8-1.5%). Candidates are treasury shares (ESOP trust or buyback held), partly paid shares, or a forfeited-share amount inside paid-up capital. Basic equals diluted in every column, so no dilutive instruments are open. Ask the share basis. |
| F-07 | F11 | R273-R276, R129-R134, R141-R146 | 361, 110, 130 | "Other Equity 15,716 13,661" (361); "Total Comprehensive Income ... 2,055" (110, H1FY27) | AMBIGUOUS | Net worth ties: 1,059 + 15,716 = 16,775; 1,059 + 13,661 = 14,720. Other Equity moved 2,055, exactly H1FY27 TCI 2,055. No dividend, buyback or other appropriation passed through equity in H1FY27. The CF "Dividends paid" line (286) is blank and financing outflow 179 = 147 repayment + 32 interest. FY26 by contrast carried a 158 non-TCI reduction (10,728 + 3,091 - 13,661). If the FY26 AGM fell inside H1FY27 and approved a final dividend, the dividend would show as an equity reduction here. It does not. Ask whether a FY26 dividend was recommended, and the AGM date. No third-party net-worth number is in context for a 5% test. |
| F-08 | F12 | R229-R230, R245-R246, R207-R208, R213-R214, R227-R228, X010, X011 | 321, 336, 245, 271, 377, 390 | "Capital work - in -progress 397 50" (321); "Other non -current assets 579 99" (336); "Purchase of property, plant and equipment 581.00 895.00" (245) | FORWARD-SIGNAL | CWIP rose about 8x in H1 (50 to 397). Other non-current assets rose 480 (99 to 579), a line that usually carries capital advances. H1 PPE purchase 581 is 65% of all FY26 (895). Derived bridge: 6,011 + about 234 PPE additions - 236 D&A = 6,009, so the rest of the 581 went to CWIP (+347). "Other inflows (outflows)" in investing is (455) with no description. Deferred government grants are nil, non-current and current (377, 390), so no capital subsidy is booked against the build. A build is under way, and no note names the project, the capacity, the cost or a commissioning date (lines 151-158 are silent). Ask the project, total capex, funding, any subsidy claim, and commissioning date. This becomes a Role 5 promise-vs-delivery item once management states it. |
| F-09 | F12 | R381, R327-R330, R001-R006, R055-R060, R019-R036 | 155, 62, 87, 80 | "considered as a single business product. Segment reporting is not applicable." (155); "Manufacturer of Vinyl Flooring, PVC Sheeting, PVC Geomembranes, PVC Artificial Leather cloth" (62) | AMBIGUOUS | The letterhead names four product lines, and Note 3 reports one segment, so no mix data exists. Two proxies moved in Q2FY27. (1) GST / gross revenue fell to 11.85% (1,363/11,506) from 12.72% in Q1FY27 and 12.66% in Q2FY26 (FY26 12.49%). This means a shift toward zero-rated exports, a lower-rate product, or a rate change. (2) Material cost (6,843 + 217 - 78 = 6,982) rose to 68.8% of GST-net revenue (10,143), from 66.5% in Q1FY27 and 62.7% in Q2FY26. Net revenue grew 39.6% YoY, but PBT margin on GST-net total income fell to 12.8% from 14.9% YoY (Q1FY27 13.8%). EBITDA margin was 14.2% vs 16.7% YoY. Growth is coming with lower unit margin. Ask about export share, product mix, and PVC resin pass-through lag. |
| F-10 | F14 | R243, R285, R239, R289 (R241, R247, R290, R307) | 335, 376, 333, 379 | "Defrred tax assets (net) 442 142" (335); "430 130" (376); "Other non -current financial assets 932 132" (333); "TOTAL NON CURRENT LIABILITIES 6228 603" (379) | AMBIGUOUS | Four 30/09/2026 line items do not cast to the printed totals, which do tie. TOTAL NCA 8,437 needs DTA 142, not 442 (6,407 + 1,309 + 442 + 579 = 8,737). TOTAL NCL 628 (5,502 - 4,874) needs DTL 130, not 430. Total NC financial assets 1,309 needs Other NCFA 232, not 932 (1,077 + 932 = 2,009). NCL prints "6228" for 628. Each gap fits a one-digit OCR misread (1 to 4, 2 to 9). If the filing really prints these values, the statement does not cast, and that is a filing-quality fact. Either way, net deferred tax is 12 at both dates (142 - 130), which agrees with nil interim P&L deferred tax (F-04). Pipeline action: A1 re-reads page 6 lines 333 and 335 and page 7 lines 376 and 379 against the image. Do not carry 442 / 430 / 932 / 6228 into any model. |
| F-11 | F14 | R197-R198, R237-R238, R389 | 196, 331 | "Adjustments for decrease (increase) in trade receivables, non-current ... 162.00 (422.00" (195-196); "Trade receivables, non current = -" (331) | AMBIGUOUS | The cash flow shows a non-current receivables increase of 422 in FY26 and a release of 162 in H1FY27. The balance sheet shows nil non-current trade receivables at both dates. Either the CF line labels a balance held elsewhere (Other non-current financial assets 132 / 232, or Other non-current assets), or the statements disagree. Ask what the 422 non-current receivable is, where it sits on the balance sheet, and whether it is a long-dated or disputed customer dues balance. Conservative read: treat it as a stretched receivable until explained. |
| F-12 | F14 | R380, R369, R370, R055-R060 | 153, 75, 87 | "prepared in accordance with the Companies (Indian Accounting Standards) Rules,2015" (153); "Revenue from Operations (Inclusive of GST)" (75) | NEUTRAL-FACT | Note 2 cites Ind AS. The table still reports revenue gross of GST and books GST as an expense (line 87). Ind AS 115 revenue excludes amounts collected for third parties. Gross revenue overstates economic revenue by about 12% (Q2FY27 11,506 gross vs 10,143 net). Margins computed on reported revenue understate. Downstream stages must use GST-net revenue: Q2FY27 10,143, Q1FY27 8,733, Q2FY26 7,264, FY26 29,658 (33,890 - 4,232). |
| F-13 | F14 | R364, R374, R372, R377, R401, X002, X008 | 37, 113, 95, 131, 521, 94, 128 | "The link to the results is as follows:" (37, followed by no link); "Exceptional Items" (94, no value); "Details of debt securities" (128, no value) | NEUTRAL-FACT | Small drafting gaps: the results link is blank (37). The page 3 header has no "Half year ended" label over the half-year columns (113). Stray markers have no footnote (95, 131, 521). Two standing lines are left fully blank, not marked "-" or nil: Exceptional Items (94) and Details of debt securities (128). Nil template lines elsewhere carry dashes (103-106, 370-372), so the template is filled unevenly. The nil reading holds for Exceptional Items: PBT before exceptional items equals PBT in all six columns (93 vs 95). The CIN difference (5 vs 67) is OCR, disposed in 0A, and is not counted here. Note text and auditor letter agree on scope: both say limited review on unaudited standalone results (lines 32, 428). One governance data point on drafting care, not material alone. |
| F-14 | F17 | R378-R384 (notes), R229, R173, R381, R273 | 151-158 | "Notes:" (151) ... "The Company has no subsidiary/associate/Joint Venture Company(ies)." (158) | AMBIGUOUS | Silence audit run against the disclosures expected in a results filing of this kind (Notion checklist not available). See the "What Was NOT Disclosed" table. Five items with forward weight are silent: the capex project, debt location, product/export mix, FY26 dividend and share basis. Each is 1 quarter of silence (first observation; no prior quarter on file). |

No F-02 (F2/F3 not applicable, standalone only). IDs are kept contiguous to their checks. The gap at F-02 is deliberate, so the IDs cited in A4 handoffs stay stable.

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 49 nil cells on 20 lines plus 2 blank rows explained in section 3 (loop 1 adds X001-X012). One is live: nil borrowings, nil NC financial liabilities subtotal (373) and blank debt securities (128) contradicted by D/E 0.11, the 147 repayment and finance cost (F-01). |
| F2 Standalone vs consolidated | N.A. | Standalone only. "The Company has no subsidiary/associate/Joint Venture Company(ies)." (line 158). |
| F3 Shell-entity detection | N.A. | No subsidiaries (line 158). No consolidated cost lines to compare. |
| F4 Unaudited contribution ratio | PASS | No JV, associate or component auditor (line 158). Unaudited contribution 0% of PAT. The whole statement is limited-reviewed by ADV AND CO LLP (line 428), not audited. |
| F5 Going concern / EoM tracking | FINDING | Paragraphs 3-4 garbled (lines 477-502). EoM absence cannot be confirmed. UDIN unreadable (line 515), so the copy cannot be authenticated. No prior-quarter text to diff (F-03). |
| F6 Forward-commitment phrase mining | PASS | Lexicon run over lines 1-522. One hit: "commenced" (line 35) is meeting timing, not a commitment. No "will be", "expected", "proposes to", "board has approved", "in the process of" anywhere. Commitment register empty. The silent capex build is under F-08. |
| F7 Hedge phrase mining | PASS | No lexicon hit ("subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", "may sometimes", "could have an effect"). The nearest phrase, "to the extent applicable" (line 154), is boilerplate and outside the lexicon. |
| F8 Tax forensics | FINDING | ETR 25.17% Q2FY27 vs 27.18% Q2FY26. Interim deferred tax nil, booked at year end only. About 26 of PAT from the ETR base effect (F-04). |
| F9 OCI forensics | FINDING | Single-quarter OCI (+384 Q1, (218) Q2) exceeds the full FY26 OCI (97) (F-05). |
| F10 Share count and dilution | FINDING | Paid-up 1,059 constant in all periods. Basic = diluted (no spread). EPS implies about 1,044-1,049 lakh weighted shares, below 1,059 (F-06). |
| F11 Reserves and net worth tie-out | FINDING | 1,059 + 15,716 = 16,775 ties. The Other Equity move equals TCI exactly, so there is no FY26 dividend in H1 (F-07). No third-party number in context. |
| F12 Segment forensics | FINDING | Single segment (line 155). Asset accretion proxy shows a capex build with no grant booked (F-08). Mix proxies shifted with margin compression (F-09). |
| F13 Board outcome beyond results | PASS | Single agenda item: approve standalone unaudited results (lines 25-30). No AR, AGM notice, record date, dividend, fund raise, ESOP or director appointment. 60-minute meeting (line 35). No Role 6 event to schedule from this outcome. |
| F14 Note drafting inconsistencies | FINDING | BS line items do not cast (F-10). CF vs BS non-current receivables (F-11). GST-gross revenue vs Ind AS note (F-12). Blank link, stray markers, two fully blank standing lines (94, 128) (F-13). CIN difference is OCR, no finding (0A). |
| F15 Entity list diffs | N.A. | No consolidation list. Note 5 (line 158) says no subsidiary, associate or JV. No prior quarter on file. Baseline recorded: zero group entities. |
| F16 Presentation dropped/reframed | N.A. | Doctype results, not a presentation. |
| F17 Silence audit | FINDING | Run on caller instruction against expected results-filing disclosures. Notion checklist not available. Five silent items (F-14). |

## 3. F1 ZERO-STANDING REGISTER (49 cells on 20 lines: 23 structured + 26 X-rows; plus 2 blank rows X002, X008)

| line item | IDs | line | template purpose | read |
|---|---|---|---|---|
| Other Expenses header row | X001 | 86 | group header over GST and other expenses | Nil header cells. Sub-items carry the values (87-88). Template only |
| Exceptional items | X002 (blank row) | 94 | one-off gains/losses, impairments | Blank, no dash. Nil confirmed: PBT before exceptional = PBT in all six columns (93, 95). Drafting note in F-13 |
| Tax expenses header row | X003 | 96 | group header over current and deferred tax | "-" nil. The "2" token feeds no total (97 = 99 in every interim column). Reads as OCR of a dash |
| Deferred tax (interim) | R097, X004 | 98 | DTA/DTL movement | Year-end-only booking (F-04) |
| Discontinued ops PBT / tax / PAT | R111-R116, X005, X006 | 103-105 | divestment of a business line | Nil all six periods. Glyphs "f", "“", "=" (105) are OCR of dashes. No divestment staged |
| Share of associates/JV | X007 | 106 | equity-method income | Nil. Glyphs "S a z a" are OCR. Agrees with Note 5 (158) |
| Details of debt securities | X008 (blank row) | 128 | LODR disclosure of listed NCDs / CPs | Blank. No listed debt securities shown. Any debt is unlisted (F-01). Drafting note in F-13 |
| Trade receivables non current | R237, R238 | 331 | long-dated customer dues | Nil on BS but CF shows movement (F-11) |
| Current tax assets | R261, R262 | 348 | advance tax over provision | Nil. Current tax liability 213 vs 55 instead |
| Non current assets held for sale | R267, R268 | 351 | asset disposal staged | Nil both dates. No disposal staged |
| Borrowings non current | R277, R278 | 370 | term debt | Nil but D/E 0.11 (F-01) |
| Trade payable non current | R279, R280 | 371 | long-dated supplier credit | Nil |
| Other NC financial liabilities | R281, R282 | 372 | lease liabilities, deposits | Nil. No lease liability shown anywhere |
| Total NC financial liabilities | X009 | 373 | subtotal of 370-372 | Nil both dates (". ‘i" OCR). Confirms no NC debt or lease liability (F-01) |
| Deferred government grants non current | X010 | 377 | capital subsidy received, amortised | Nil. No grant booked against the CWIP build (F-08) |
| Other NC liabilities | R287, R288 | 378 | deferred income | Nil |
| Borrowings current | R291, R292 | 382 | working-capital debt | Nil but a 147 repayment in H1 (F-01) |
| Deferred government grants current | X011 | 390 | current portion of grants | Nil ("us", "=" OCR). Agrees with X010 |
| Liabilities in disposal group held for sale | X012 | 392-393 | liabilities going with a staged disposal | Nil. Agrees with nil held-for-sale assets (351) |
| Blank-in-source rows | R373, R376, R388 | 100, 115-123, 187 | regulatory deferral, NCI, CF applicability | Template only |

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| (none) | - | lines 151-165 searched | - |

The filing holds no forward-looking statement (A1 FORWARD = 0). The one forward-weight fact, the CWIP build (F-08), carries no management commitment to track yet.

## 5. WHAT WAS NOT DISCLOSED (F17; Notion checklist not available)

| expected disclosure | where it would sit | evidence it matters | consecutive quarters silent |
|---|---|---|---|
| Capex project, cost, commissioning date | Notes, lines 151-158 | CWIP 50 to 397 (321); other NCA 99 to 579 (336) | 1 (first observed) |
| Debt location and nature | Notes / BS borrowings, lines 370, 373, 382; debt securities line 128 | D/E 0.11 (147); repayment 147 (283) | 1 (first observed) |
| Product or export mix | Note 3, line 155 | Four product lines (62); GST ratio and material intensity shift (87, 80) | 1 (first observed) |
| FY26 dividend / AGM | Board outcome, lines 25-35 | Other Equity move = TCI (361, 110) | 1 (first observed) |
| Weighted share basis / treasury shares | EPS block, lines 136-146 | EPS above PAT/paid-up (139) | 1 (first observed) |
| OCI composition | P&L line 109 | +384 / (218) swings | 1 (first observed) |
| Results web link | Letter, line 37 | Blank after "as follows:" | 1 (first observed) |
| Legible review report (paras 3-4, UDIN) | Auditor report, lines 477-515 | UDIN unreadable (515); conclusion text partly missing (485-490) | 1 (first observed; copy quality, not management silence) |

## 6. HANDOFF TO A4

FORWARD-SIGNAL: F-08.
AMBIGUOUS (convert to management questions): F-01, F-03, F-04, F-05, F-06, F-07, F-09, F-10, F-11, F-14.
F-10 is mainly an A1 re-read action for the orchestrator. It becomes a management or data question only if the image confirms the printed values.
Loop 1: F-03 now carries the unreadable UDIN (R316, line 515). A4 ties it to its F-03 AMBER flag, Q14 and M2. R312 / R314 are reviewed, no finding (0A). F-01 now carries the nil NC financial liabilities subtotal (373) and the blank debt securities line (128). Neither changes its classification.

```yaml
stage: A3-forensics
company: "PREMIERPOL"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
loop: 1
forensics_path: "runs/premierpol-q2fy27/work/forensics_results_premierpol_q2fy27.md"
ledger_reconciled_pct: 100        # 413 of 413 (R001-R401 + X001-X012)
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: FINDING
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F-01", check: "F1", line: "370, 373, 382, 128, 147, 283, 84", classification: "AMBIGUOUS", implication: "Borrowings and NC financial liabilities subtotal nil both dates, debt securities blank, yet D/E 0.11 (derived debt ~1,845), H1 repayment 147, finance cost 24/qtr; any debt is unlisted and current, likely other current financial liabilities 2,363"}
  - {id: "F-03", check: "F5", line: "490, 477-485, 513-515", classification: "AMBIGUOUS", implication: "Review conclusion fragment unmodified; paras 3-4 garbled so EoM/Other Matter absence unconfirmed; UDIN unreadable (R316, L515), copy cannot be authenticated; no prior text to diff; baseline quarter"}
  - {id: "F-04", check: "F8", line: "96, 97, 98, 99", classification: "AMBIGUOUS", implication: "ETR 25.17% vs 27.18% YoY adds ~26 to PAT (~3pp of 22.5% growth), base effect; interim deferred tax nil, year-end true-up risk"}
  - {id: "F-05", check: "F9", line: "109", classification: "AMBIGUOUS", implication: "Q1 OCI +384 and Q2 (218) each exceed FY26 full-year (97); likely FVOCI investment marks; verify composition at AR"}
  - {id: "F-06", check: "F10", line: "126, 139, 145", classification: "AMBIGUOUS", implication: "EPS implies ~1,044-1,049 lakh weighted shares vs 1,059 lakh paid-up (FV Rs 1); treasury/partly-paid/forfeited shares; basic = diluted"}
  - {id: "F-07", check: "F11", line: "361, 110, 130", classification: "AMBIGUOUS", implication: "Other Equity +2,055 = H1 TCI exactly; no FY26 dividend or appropriation in H1 though FY26 roll had 158 non-TCI reduction"}
  - {id: "F-08", check: "F12", line: "321, 336, 245, 271, 377, 390", classification: "FORWARD-SIGNAL", implication: "CWIP 50 to 397, other NCA 99 to 579, H1 capex 581 = 65% of FY26; no deferred grant booked; undisclosed build, project/cost/commissioning date unknown"}
  - {id: "F-09", check: "F12", line: "155, 62, 87, 80", classification: "AMBIGUOUS", implication: "Single segment vs four product lines; GST/gross revenue 11.85% vs 12.72% QoQ, material cost 68.8% vs 62.7% YoY of net revenue; net revenue +39.6% YoY with PBT margin 12.8% vs 14.9%"}
  - {id: "F-10", check: "F14", line: "335, 376, 333, 379", classification: "AMBIGUOUS", implication: "DTA 442, DTL 430, other NCFA 932, NCL 6228 do not cast; totals tie with 142/130/232/628; A1 re-read; net DT 12 unchanged"}
  - {id: "F-11", check: "F14", line: "196, 331", classification: "AMBIGUOUS", implication: "CF shows non-current receivables (422) FY26 and +162 H1 while BS non-current receivables nil both dates; possible stretched receivable"}
  - {id: "F-12", check: "F14", line: "153, 75, 87", classification: "NEUTRAL-FACT", implication: "Revenue reported gross of GST despite Ind AS note; use net revenue Q2FY27 10,143, Q1FY27 8,733, Q2FY26 7,264, FY26 29,658"}
  - {id: "F-13", check: "F14", line: "37, 113, 95, 131, 521, 94, 128", classification: "NEUTRAL-FACT", implication: "Blank results link, unlabelled half-year header, stray markers, Exceptional Items and debt securities lines fully blank (not dashed); note and auditor scope agree (limited review); CIN difference is OCR, not counted"}
  - {id: "F-14", check: "F17", line: "151-158", classification: "AMBIGUOUS", implication: "Silent on capex project, debt location, product/export mix, FY26 dividend, share basis; 1 quarter each (first observation); Notion checklist not available"}
flagged_row_dispositions:
  - {rows: "R312, R314", flag: "CIN_OCR_MISMATCH", line: "5 vs 67", disposition: "reviewed, no finding: chars 2-21 identical, L read as 1 by OCR"}
  - {rows: "R316", flag: "UDIN_UNRESOLVED", line: "515", disposition: "carried into F-03 (F5): UDIN unreadable, review report not authenticable from this copy"}
forward_signals: ["F-08"]
ambiguous: ["F-01", "F-03", "F-04", "F-05", "F-06", "F-07", "F-09", "F-10", "F-11", "F-14"]
commitments: []
gate_a3: pass
blank_checks: []
analyst_note: "The quiet story is growth bought with margin plus an undisclosed build. GST-net revenue grew 39.6% YoY. Material intensity rose 6pp and PBT margin fell about 2pp, while the GST ratio dropped, so mix or exports likely shifted. CWIP rose 8x and other non-current assets 5x with no note and no grant booked, so a capacity project is under way. Its size and timing are the first concall question. Three items need resolution before any model uses this balance sheet. First, the debt location: D/E 0.11 against nil borrowing lines, a nil non-current financial liabilities subtotal and a blank debt securities line, so any debt is current and unlisted. Second, four BS cells that fail casting (likely OCR; A1 re-read). Third, CF non-current receivables with no BS home. The review report copy cannot be authenticated: UDIN unreadable, paragraphs 3-4 garbled. EPS runs about 1% above PAT/paid-up, so ask the share basis. PAT growth is flattered about 3pp by the ETR base effect. Revenue is gross of GST; use net revenue downstream."
```
