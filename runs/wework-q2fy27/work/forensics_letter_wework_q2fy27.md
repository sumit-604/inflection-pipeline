# A3 FORENSIC NOTES: WeWork India Management Ltd (WEWORK) Q2 FY27, doctype: presentation (Shareholders' Letter, file tag letter)

Inputs read: A1 structured extraction runs/wework-q2fy27/extracted/wework-letter-q2fy27-structured.md (R001-R1570, all rows read); A1 fulltext runs/wework-q2fy27/extracted/wework-letter-q2fy27-fulltext.md (every ledger anchor line read: body lines 20-906, 1120-1299, 1548-1618; IMAGE-VERIFIED appendix lines 1620-1872); A2 ledger runs/wework-q2fy27/work/ledger_letter_wework_q2fy27.md; results A3 runs/wework-q2fy27/work/forensics_results_wework_q2fy27.md (cross-check of the duplicated statements only). Source PDF and inputs/ not opened.
Not used as a value source: misaligned body text of pages 22-24 and 28-30 (lines 907-1119, 1300-1547), per A1 and A2. No ledger row anchors there.
Prior-quarter fulltext: none (first quarterly review of this name). Every prior-quarter diff (F5 language, F6 status transitions, F15 entity list, F16 dropped metrics, F17 consecutive-quarter count) is recorded as BASELINE, not as a pass on change.
Monitoring checklist: no Notion page and no companies/WEWORK.md. PRE-THESIS READ. Operator batch watch list plus the results-filing points used in its place (F17 table, section 5).
Units: pages 3-20 Rs Cr as printed; filed statements Rs Million (x0.1 = Rs Cr). Figures marked [derived] are A3 arithmetic on printed figures, not company-reported numbers.

## 0. LEDGER RECONCILIATION
- Structured IDs: 1,570. Ledger IDs referenced: 1,570 (orphans: none). Rows read at their cited fulltext line: 1,570 of 1,570 = 100%.
- ZERO_STANDING: 121 rows (p17 37, p18 32, p22 28, p23 1, p24 7, p28 8, p29 1, p30 7) read at lines 674-705, 735-766, 1638-1653, 1666, 1704-1741, 1749-1767, 1788, 1832-1857.
- MFS-1 (A2): lines 1584-1585 read. Values 1,385.90 / 1,388.70 / 1,353.78 Mn equal R965-R966, R1177-R1182. Confirmed low materiality.
- FOOTNOTE_UNRESOLVED rows confirmed at line: R1514 (line 206, order book basis), R1516 (line 221, FCFO/FCFF formula), R1522 (line 388, chart basis), R1526 (line 503, brand licence terms). Notes 1-2 of the filed statements are absent from text layer and appendix (A2 section 7); not testable.
- Letter copy vs results filing (statements duplicated on pages 22-31): every results-filing value cited in the results A3 was checked against the letter's IMAGE-VERIFIED blocks. About 40 values matched exactly, including SA H1 OCF 10,247.80, lease liabilities 52,331.24, DTA 3,077.49, SA other income 184.53, sub-contracting 27.57, PPE capex 3,639.79, ROU additions 783.68, tax paid 389.97, CA PAT 204.35, associate 8.69, subsidiary PAT 3.35, SA total equity 3,465.28, ESOP proceeds 171.75, other NC financial liabilities 2,626.08 / 1,623.12, other NC liabilities 750.89 / 270.69, membership 222345, and the 4-entity consolidation list. Differences found: none. Limit: this is not a cell-by-cell diff. The results structured file is outside this run's allowed inputs.
- Internal arithmetic re-run on pages 5-7 and 17-18: every growth rate and margin recomputes from the reconciliation tables. Examples: PAT 65.8/39.3 = +67.4%; EBITDA 162.9/118.4 = +37.6%; revenue 768.7/584.0 = +31.6%; margin 19.8% to 21.2% = +138 bps; H1 PAT 119.0/47.7 = +149.5%. Reconciliation columns add across (Q2 EBITDA adj (17.7) - 328.1 = (345.8); PBT adj (116.2) + 8.8 + 152.7 = 45.3).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| L-F1-a | F1 | R542-R550, R353-R361, R587-R595 | 753, 763, 692 | "Exceptional item ... – (34.1) (34.1)" | AMBIGUOUS | The exceptional line is nil in 17 of 18 reconciliation cells. It is live only in the H1 FY25 IGAAP column: a 34.1 Cr charge with NO Ind AS counterpart (IndAS cell "–"). IGAAP PAT before exceptional H1 FY25 = 35.3 vs PAT 1.2 (line 763). The headline basis carries its own exceptional items, of undisclosed nature, that the filed Ind AS statements do not. Future "PAT before exceptional" headlines can strip charges with no audit trail. Ask what the 34.1 Cr was. |
| L-F6-a | F6 | R058-R059, R1452 | 195-196 | "A further ~47k desks are secured through signed leases and LOIs, 32% beyond today's capacity." | FORWARD-SIGNAL | Pipeline of ~47k desks with no opening dates, no split between signed leases and LOIs, and no capex or rent figure. Signed leases not yet commenced are not in the 5,233.1 Cr Ind AS 116 lease liability (lines 1811, 1817) [derived sum]. Each handover adds lease liability and ROU assets, and fit-out capex follows. Feeds the Role 5 tracker: desks opened vs the 47k, quarter by quarter. |
| L-F6-b | F6 | R1448-R1449 | 148-153 | "the business is on track to unlock operating leverage and deliver superior, more profitable growth" | AMBIGUOUS | Undated and unmeasured. No margin target, no date, no metric. Not trackable as stated. A4: ask for the margin or rent-to-revenue level management means by "operating leverage", and by when. |
| L-F7-a | F7 | R1452, R1453, R1508-R1511 | 195, 206-207, 92-115 | "secured through signed leases and LOIs"; "is already locked in" | AMBIGUOUS | Hedge lexicon hits sit only in the page-3 disclaimer ("could", lines 92/95; "subject to change", line 114). The narrative carries none. It uses certainty words ("secured", "locked in", "on track") for items that include non-binding LOIs and an undefined order book. Inverse signal: the hedging moved into the boilerplate, not the claims. A4: what share of the 47k is LOI only? |
| L-F8-a | F8 | R371-R379, R560-R568, R015, R098 | 696, 757, 145 | "Current Tax / Deferred tax – – –"; "(235.0) 235.4 0.4" | FORWARD-SIGNAL | The headline PAT carries zero tax in every reconciliation column (Q2 FY27 "–"; H1 FY27 0.1 Cr). At the statutory 25.17%, Q2 IGAAP-equivalent PAT of 65.8 Cr would carry about 16.6 Cr of tax [derived]. Page 18 also dates the DTA: an Ind AS tax credit of 235.0 Cr in H1 FY25, reversed in the IGAAP column. That one half-year built most of the 307.7 Cr standalone DTA (line 1669). The letter never says when book or cash tax normalises. "PAT +67%" is a pre-tax growth rate in substance. Same tax facts as results F8-a. |
| L-F11-a | F11 | R038, R047-R048, R111-R114, R132, R135, R1239-R1250, R1261 | 181, 227-231, 676, 1805-1816 | "ROCE reached 34.5%, up 1,235 bps YoY and" | AMBIGUOUS | Net worth ties (SA 1,388.70 + 2,076.58 = 3,465.28; CA 1,388.70 + 2,015.60 + NCI 16.37 = 3,420.67). The letter's only capital-based ratio, ROCE, does not tie to the filed balance sheet. Q2 IGAAP EBIT 78.2 Cr annualised = 312.8 Cr; at 34.5% this implies capital employed of 906.7 Cr [derived]. Filed CA equity plus borrowings = 732.3 Cr (gives 42.7%) [derived]. The IGAAP-equivalent net worth is never shown. The +590 bps in one quarter cannot be tested. A4: ask for the formula and the capital employed figure. |
| L-F12-a | F12 | R101, R106-R108, R1319-R1322, R1251-R1258, R1271 | 220-225, 1847-1848 | "Our model generates cash at scale, enough to fully fund our capex and leave a surplus." | FORWARD-SIGNAL | Single segment (Note 9, line 1587). H1 FCFO of 379.8 Cr exceeds EBITDA of 301.2 Cr only because of working-capital inflows. "Other liabilities" brought in +70.4 Cr and "other financial liabilities" +76.2 Cr (CA, lines 1847-1848). Excluding those, FCFO would be about 233.2 Cr, below EBITDA [derived]. The nature of these liabilities is not disclosed in the narrative or the notes (same as results F12-a). If they are member deposits and advance billing, they reverse when growth or renewals slow. "1.5x EBITDA" (line 224) is a growth-phase number, not a steady-state number. |
| L-F14-a | F14 | R098, R100, R326-R334, R344-R352, R380-R388, R515-R577; R1057-R1109 | 218, 684, 690, 698, 745, 751, 759 vs 1757-1765 | "PAT was ₹20.5 Cr, from a ₹4.2 Cr loss in Q1" | NEUTRAL-FACT | The "Reported IndAS" column does not round to the filed consolidated statements. Q2 PAT 20.5 vs filed 204.35 Mn = 20.4 (20.5 is PBT; owners' share 20.3). Q1 PAT (4.2) vs (40.61) Mn = (4.1). Q1 PBSA (4.2) vs (40.37) Mn = (4.0). Q1 PBT (4.1) vs (39.43) Mn = (3.9). H1 PBSA/PBT/PAT 15.4/16.4/16.3 vs 15.5/16.5/16.4. H1 FY26 PAT (7.8) vs (7.7). Differences are 0.1-0.2 Cr, so the IGAAP-equivalent figures built on this column (53.2, 119.0) carry the same error. Immaterial alone. It is still a drafting data point in the table the letter offers as its bridge to audited numbers. |
| L-F14-b | F14 | R964, R1377, R1434, R1444, R1428, R648, R984 | 1152, 1581, 1582, 881, 883, 1279, 1281 | "468,896" vs "4,68,896"; "Equity Incentive Plan 2018" vs "the Equity Plan 2018"; "per Nikunj Jay" vs "ra Shah" | NEUTRAL-FACT | The letter's copy reproduces the results filing's drafting slips. Option count is formatted two ways between SA and CA Note 7. The plan name is given two ways. One membership number (222345) appears under two partner-name OCR strings (results F14-a; likely OCR). CA Note 5 is unnumbered in the text layer (line 1568). These are not new issues. They confirm the letter annexes the same filing unchanged. |
| L-F16-a | F16 | R055-R057, R1451, R1473-R1474 | 194-195 | "First-half additions of 18.4k, with ~4.5k more desks opened in the first week of October, take us past the 22k we set out in Q1." | AMBIGUOUS | Within the reported period, additions were 18.4k = 83.6% of the 22k [derived]. The letter reaches "past the 22k" only by adding ~4.5k post-period desks (October, outside the half, unaudited). The target's window is not stated. A4: was 22k an H1 target? What is the FY27 target, and what are Q3 additions excluding the October 4.5k already claimed? |
| L-F16-b | F16 | R017, R027, R032, R069, R181, R221, R1513, R180, R179 | 172, 175, 202, 599, 1631 | "The 114 bps QoQ dip is new capacity still filling." | FORWARD-SIGNAL | Portfolio occupancy was a record 86.9% in March 2026 (line 599). It was about 84.8% in June [derived from -114 bps] and 83.7% in September. That is a 320 bps fall over two consecutive quarters [derived]. The letter explains only the last 114 bps. The page-11 chart also shows 84% (Mar 2023) falling to 77% (Mar 2025) under the heading "Resilient through every cycle", and the narrative does not mention that 7-point fall. Mature occupancy for March is not given, so the mix effect cannot be separated. Watch item deteriorating; next data point is Q3. |
| L-F16-c | F16 | R077-R080, R1453, R1514, R614-R616, R1251, R1263 | 206-207, 783, 1811, 1817 | "₹3,843 Cr of core revenue is already locked in, up 66% YoY and 2.7 times the ₹1,421 Cr of rent committed against it." | FORWARD-SIGNAL | Basis undefined (R1514 FOOTNOTE_UNRESOLVED): period, gross or net of GST, lock-in or full term, IGAAP or Ind AS. 1,421 Cr is about 1.19 years of Q2 cash rent (298.2 x 4 = 1,192.8) [derived]. 3,843 Cr is about 1.25 years of Q2 revenue run-rate [derived]. Ind AS 116 lease liabilities are 5,233.1 Cr (present value), about 4.4 years of cash rent [derived], and exceed the locked-in revenue. The 2.7x cover measures only the near window that matches member lock-ins. It does not measure total landlord obligations. The duration mismatch (members about 1.25 years, landlords longer) is the core flex-operator risk, and this ratio hides it. Also: +66% YoY vs revenue +31.6% means longer lock-ins or a changed definition. Ask which. |
| L-F16-d | F16 | R109-R110, R1227-R1230, R1223, R1249-R1250, R1261-R1262, R1345-R1347 | 224-225, 220, 1797-1800, 1810, 1816, 1860-1861 | "we closed September with net cash of ₹23.1 Cr, from net debt of ₹310.5 Cr a year ago" | AMBIGUOUS | Not reproducible from the filed CA balance sheet. Borrowings 3,902.05 Mn less cash 59.54, other bank balances 57.72 and current investments 3,786.83 gives net cash 2.04 Mn = 0.2 Cr [derived; results A3 got the same]. Unexplained gap: about 22.9 Cr. The YoY frame starts from Sep 2025. On the same basis, March 2026 net debt was 14.3 Cr [derived], so H1 FY27 moved it by about 14 Cr, not 333 Cr. Gross borrowings rose 57.4 Cr (+17.3%) in H1 (proceeds 189.5 Cr, repayments 133.2 Cr) while the letter says cash was "enough to fully fund our capex". Lease liabilities of 5,233.1 Cr are excluded and not mentioned. A4: ask for the definition and what bridges 0.2 Cr to 23.1 Cr. |
| L-F16-e | F16 | R101, R103-R105, R133-R134, R137-R138, R1516, R1327, R1329, R1333, R1355-R1357 | 220-223, 1851-1854, 1865-1866 | "and still left ₹16.0 Cr of free cash flow to the firm (FCFF)" | AMBIGUOUS | FCFO and FCFF formulas are not given (R1516). Capex of 363.8 Cr equals filed PPE acquisitions (3,637.70 Mn). Filed CA OCF 1,026.2 Cr less lease cash 588.0 Cr less "payment towards additions to right-of-use assets" 78.4 Cr = 359.8 Cr, less capex 363.8 Cr = FCFF (4.0) Cr [derived]. The letter reports FCFF +16.0 Cr, a gap of 20.0 Cr. The 78.4 Cr ROU-addition payment is not visible in either the FCFO or the capex figure. If FCFO excludes it, then the "fully funded with a surplus" claim fails by about 62 Cr [derived: 16.0 - 78.4]. Results A3 got the SA equivalent as (55.78) Mn. Resolve the definition before Role 1 uses FCFF. |
| L-F16-f | F16 | R166, R172-R177, R1522, R1003-R1008, R990 | 405-416, 1631, 1745, 1748 | "REVENUE ₹ CR ... 2,490 ... 3.9× in 5 years" | AMBIGUOUS | The chart basis is not stated (R1522). The FY26 bar of 2,490 equals filed CA Ind AS TOTAL INCOME 24,904.28 Mn (line 1748). That figure includes finance income 364.87 Mn and other income 137.61 Mn. CA revenue from operations was 24,401.80 Mn = 2,440.2 Cr (line 1745). The match could be a coincidence with an IGAAP-equivalent total, but the FY26 IGAAP figure is not in the letter, so it cannot be tested. The "3.9x" growth claim rests on an undefined series. A4: ask for the basis of each bar. |
| L-F16-g | F16 | R073-R076, R163-R164, R1456 | 204-206, 395, 432 | "VAS + Digital generating 14.6% of revenue" | AMBIGUOUS | The 2022-24 era share is printed as 14.6%. Q2 FY27 VAS + Digital is 108.8 of 768.7 Cr = 14.2% [derived]. The narrative says the platform is "compounding on top of the core" and calls it "margin-accretive" (line 432), with no margin figure. On the letter's own numbers, the share is no higher than the earlier era. It is rising YoY (VAS + Digital +38% vs core +31.7%). A4: ask for the share trend FY24-FY27 on one basis, and the VAS + Digital margin. |
| L-F16-h | F16 | R254-R262, R228-R244, R614-R616, R641-R646, R443-R451, R632-R634 | 662-668, 729, 783, 810-811 | "Operating and Other expenses 277.7 328.1 605.8" | AMBIGUOUS | The headline basis is management-defined, and the composition of its largest adjustment is not given. The opex adjustment, less cash rent paid to landlords and the brokerage accrual, leaves residuals of 0.8 Cr (Q2), 9.9 Cr (Q1), 7.6 Cr (Q2 FY26) and 10.7 Cr (H1) [derived]. Possible contents (straight-lining, CAM) are not stated. The revenue adjustment flips sign: (1.3) in Q2 vs +3.5 in Q1, +3.7 in Q2 FY26 and +16.4 in H1 FY25. Brokerage accrual is +63.5% YoY in Q2 (17.8 to 29.1 Cr) vs revenue +31.6%. That is a leasing-intensity cost of the 47k pipeline. On the positive side, the finance and other income adjustment strips 16.4 of 18.6 Cr in Q2 (line 664), so the headline does not lean on the treasury and lease gains in results F1-a. |
| L-F16-i | F16 | R088-R091, R068, R040, R115-R117, R1412 | 213-214, 201, 183, 231-232 | "Centre-level EBITDA grew 38.4% YoY to ₹214.0 Cr, with margin up 109 bps to 28.4%." | AMBIGUOUS | Several KPIs have no definition. The centre-level margin of 28.4% on 214.0 Cr implies a revenue base of 753.5 Cr [derived]. That is neither total revenue (768.7) nor revenue from operations (766.5). Breakeven occupancy of 55.7% has no basis. The cost of borrowing (8.5%) has no formula. The credit rating moved "A− to A+" (two notches) with no agency named (R1412) and no date. Prior-deck definitions cannot be compared (no prior letter), so definition drift is a baseline for Q3. |
| L-F17-a | F17 | see section 5 table | 172-262 (narrative), 1136-1168, 1669, 1811-1817, 1847-1848 | narrative pages 3-20 (silence; no quote possible); anchors: "(g) Deferred tax assets" row line 1669; "Non-current Lease liabilities" line 1811 | AMBIGUOUS | 11 of 16 watch and results-raised items are not addressed in narrative pages 3-20. The items: Ind AS 116 lease liability balance, rent-to-revenue ratio, DTA and tax, ESOP dilution, NCLT reduction, lease-termination gains, Labour Code, nature of the other-liabilities build, solar capex, associate jump, escrow-only standalone cash. Occupancy is addressed only partly (L-F16-b). Quarters of silence: 1 (first letter in repo; consecutive count is a baseline). If the silence on lease liabilities, tax and the liability build continues in Q3, it becomes CONFIRMATORY-NEGATIVE per Role 5. |

## 2. CHECKLIST SCORECARD

| check | status | basis (one line) |
|---|---|---|
| F1 | FINDING | 121 ZERO_STANDING rows read. Filed-statement nil lines match the results copy (results F1-a to F1-d stand). Reconciliation nil cells are structural (ROU lines nil under IGAAP by design), except the IGAAP-only H1 FY25 exceptional charge (L-F1-a). |
| F2 | PASS | Letter copy of SA and CA P&L matches every results-cited value. The headline reconciliation is on a consolidated basis (Reported IndAS ties to CA within 0.1-0.2 Cr, see L-F14-a). The narrative carries no S-vs-C content. Results F2-a stands. |
| F3 | PASS | Copy matches. Cost of materials appears in CA only (line 1750). Employee cost SA 543.16 vs CA 557.90. Subsidiaries carry revenue 31.51 Mn (line 1256). No shells. No going concern. |
| F4 | PASS | Other Matters paragraph matches (subsidiaries 293.78 / 31.51 / 3.35 / 9.02 Mn; associate 8.69 / 9.63 Mn, lines 1255-1262). Results F4-a and F4-b stand. The narrative is silent on the associate (F17). |
| F5 | PASS | No EoM, no going concern, unmodified conclusions (lines 869-875, 1243-1250, 1272-1273). Prior-quarter verbatim diff untestable (no prior fulltext). BASELINE. |
| F6 | FINDING | Lexicon hits at lines 151 ("on track"), 195 (secured pipeline), 636 ("will keep"), 1141-1143 and 1572-1573 ("in the process of", "will be evaluated"), 1166 and 1593 ("shall adjust"). Register in section 3. L-F6-a, L-F6-b. Transitions untestable (no prior). |
| F7 | FINDING | Hedges appear only in the disclaimer (lines 92, 95, 114) and the Labour Code note ("evaluated", lines 1142, 1573; results F7-a). The narrative has none and uses certainty words for LOIs and an undefined order book (L-F7-a). "Newly added" test untestable. |
| F8 | FINDING | ETR on headline PAT 0% in all periods (lines 696, 757). DTA origin dated to H1 FY25 (235.0 Cr). Tax silence in narrative (L-F8-a). Copy matches results F8-a and F8-b. |
| F9 | PASS | OCI copy matches (SA 2.96 / (6.69) / 0.89; CA 3.02 / (6.93), lines 1652, 1766). Results F9-a (Q1 swing exceeds FY26) stands. Nothing new in the letter. |
| F10 | PASS | Paid-up 1,388.70 Mn ties to Notes 7-8 (279,961 and 3,492,205 shares, lines 1155-1157, 1584-1585). EPS spread CA 1.46/1.45, SA 1.40/1.39, narrow. ESOP cost 5.7 / 9.7 Cr stated as deducted in EBITDA (lines 188, 262) and ties to the filed SBP 97.04 Mn H1. The narrative does not mention dilution (F17). Results F10-a stands. |
| F11 | FINDING | SA and CA net worth tie. The letter's capital-based ratio (ROCE 34.5%) does not reconcile to filed capital (L-F11-a). Results F11-a (DTA 88.8% of SA net worth) stands. |
| F12 | FINDING | Single segment (lines 1159-1163, 1587-1590). The letter adds a VAS + Digital split (108.8 Cr) with no assets or liabilities. The FCFO claim rests on an undisclosed liability build (L-F12-a). |
| F13 | PASS | The letter carries no board outcome beyond results (Notes 3, lines 1126-1129, 1558-1561). No AR, AGM, record date, director term or enabling resolution. The results-filing solar approval is not mentioned (F17). |
| F14 | FINDING | Reconciliation "Reported IndAS" column vs filed statements (L-F14-a). Reproduced drafting slips (L-F14-b). Note 3 "limited review" (line 1129) is consistent with the review reports (lines 836, 1189). |
| F15 | PASS | Four entities (lines 1229-1234): holding, WW Tech Solutions India Pvt Ltd, Zoapi Innovations Pvt Ltd, MyHQ Anarock Pvt Ltd. Same as results F15. Prior list unavailable. BASELINE. |
| F16 | FINDING | Dropped-metric and baseline-shift tests need a prior letter (none). BASELINE. In-document reframing and definition gaps: L-F16-a to L-F16-i (target window, occupancy framing, order-book cover, net cash, FCFF, chart basis, VAS share, reconciliation composition, KPI definitions). |
| F17 | FINDING | Applied to the letter narrative by caller instruction, using the watch list and results-raised points. 11 of 16 items silent, 1 partial. Table in section 5 (L-F17-a). |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note / line ref | status word |
|---|---|---|---|
| ~47k desks secured through signed leases and LOIs (32% beyond current 145.3k capacity) | NOT FOUND (no opening schedule) | p5, lines 195-196 | "secured" (signing stage; LOI share NOT FOUND) |
| ~4.5k desks opened in the first week of October 2026 | Oct 2026 (post-period) | p5, line 194 | completed (claimed; outside the reviewed period; verify in Q3) |
| Desk-addition target of 22k "set out in Q1" | window NOT FOUND (letter implies H1) | p5, line 195 | claimed met, only with post-period openings (L-F16-a) |
| Unlock operating leverage; "superior, more profitable growth" | NOT FOUND | p4, lines 151-153 | "on track" (no metric) |
| Labour Code rules: impact to be evaluated and accounted for when notified | on notification; NOT FOUND | SA Note 5 lines 1141-1143; CA Note 5 lines 1572-1573 | pending ("in the process of") |
| NCLT capital reduction: set off accumulated losses Rs 20,501.60 Mn against Securities Premium | on NCLT sanction; NOT FOUND | SA Note 10 lines 1165-1168; CA Note 10 lines 1592-1594 | initiated (scheme filed; "shall adjust") |
| IPO offer for sale, 46,296,296 shares, Rs 29,996.43 Mn; listed NSE/BSE | 2025-10-10 | SA Note 6 lines 1145-1150; CA Note 6 lines 1575-1579 | completed (pure OFS, no primary proceeds) |
| "We will keep leading from the front." | not dateable | p15, line 636 | intent (no metric) |

## 4. WORKINGS FOR A4 ([derived] by A3 from printed letter figures; not company-reported)
- Rent paid to landlords (A) / IGAAP total revenue: Q2 FY27 38.8% (298.2/768.7), Q1 FY27 39.9%, Q2 FY26 42.1%. H1 FY27 39.3%, H1 FY26 42.8%, H1 FY25 39.7% (lines 666, 727, 783, 796). The company does not print the ratio.
- Occupancy path: Sep-25 80.1% (83.7 - 3.57), Mar-26 86.9% record, Jun-26 84.8%, Sep-26 83.7%.
- Capacity: Mar-26 126.9k (145.3 - 18.4), Jun-26 133.5k, Sep-26 145.3k. Members Sep-25 91.8k, Sep-26 121.7k.
- Lease liabilities (Ind AS 116, CA = SA): 5,233.1 Cr at Sep-26 vs 5,217.5 Cr at Mar-26 (+0.3%), while capacity rose 14.5% in H1. ROU assets 4,503.1 Cr vs 4,593.9 Cr. The H1 openings mostly sit on leases recognised before April 2026. The 47k pipeline is not yet in the balance.
- Order-book cover: 1,421 Cr = 1.19 years of Q2 cash rent; 3,843 Cr = 1.25 years of Q2 revenue; lease liabilities 5,233.1 Cr = 4.4 years of Q2 cash rent and 1.36x locked-in revenue.
- FCFO bridge attempt: CA OCF 1,026.2 - lease cash 588.0 = 438.1; less ROU-addition payments 78.4 = 359.8 vs letter FCFO 379.8 (gap 20.0). FCFF (4.0) vs letter 16.0.
- FCFO ex liability inflows: 379.8 - 146.6 = 233.2 Cr vs EBITDA 301.2 Cr (H1).
- Net cash (CA, incl. other bank balances): Sep-26 +0.2 Cr; Mar-26 (14.3) Cr. Gross borrowings 332.8 to 390.2 Cr.
- ROCE: implied capital employed 906.7 Cr vs CA equity plus borrowings 732.3 Cr.
- Tax at statutory 25.17% on Q2 headline PAT: about 16.6 Cr (headline carries nil).
- IGAAP opex adjustment residual after cash rent and brokerage: Q2 0.8, Q1 9.9, Q2 FY26 7.6, H1 FY27 10.7, H1 FY26 15.2, H1 FY25 13.9 Cr.

## 5. F17 SILENCE AUDIT: WHAT WAS NOT DISCUSSED (narrative pages 3-20)

| watch / results-raised item | addressed in narrative? | where / note | consecutive quarters of silence |
|---|---|---|---|
| Occupancy | PARTIAL | 83.7% and the 114 bps QoQ explained (lines 172, 202). The fall from the March record 86.9% (line 599) is not reconciled. Chart dip 84% to 77% (line 1631) not discussed. | 1 (partial) |
| Desks | YES | Lines 192-196. Pipeline undated (L-F6-a). | 0 |
| Rent-to-revenue | NO | Inputs only on p19 (line 783); ratio not stated; 38.8% derived. | 1 |
| Net debt | YES, unreconciled | Net cash 23.1 Cr (line 224) does not tie (L-F16-d). | 0 |
| Lease liabilities (Ind AS 116) balance | NO | Never stated on pp3-20. Only cash payments on p19. Balance 5,233.1 Cr appears only in filed BS (lines 1811, 1817). | 1 |
| IGAAP-equivalent vs Ind AS | YES | Lines 188, 217-218, 262; pp17-18 bridge. Drafting gaps L-F14-a, L-F16-h. | 0 |
| Other income share of profit (results F1-a) | ANNEXURE ONLY | IGAAP basis strips 16.4 of 18.6 Cr (line 664). Narrative silent. | 1 |
| DTA 88.8% of SA net worth / zero tax (results F8-a, F11-a) | NO | DTA row line 1669 only. | 1 |
| ESOP dilution (results F10-a) | NO | ESOP cost only (lines 188, 262); 2.58% H1 dilution not mentioned. | 1 |
| NCLT capital reduction (results F6-b) | NO (filed note only) | Lines 1165-1168. | 1 |
| Lease termination gains (results F1-b) | NO | Filed CF line 1838 only; centres or desks exited NOT FOUND. | 1 |
| Labour Code provision (results F6-a, F7-a) | NO (filed note only) | Lines 1136-1143. | 1 |
| Nature of the rise in other liabilities (results F12-a) | NO | The FCFO narrative (lines 220-225) depends on it (L-F12-a). | 1 |
| 10 MWp captive solar, Rs 34.25 Cr (results F13-a) | NO | Not in letter. | 1 |
| Associate MyHQ Anarock jump (results F4-b) | NO | Other Matters only (line 1261). | 1 |
| Standalone cash all in escrow (results F1-c) | NO | Filed CF line 1742 only. | 1 |

Count basis: first shareholders' letter of this name in the repo. "1" means silent this quarter. The consecutive-quarter count starts here.

## 6. RUN NOTES
- Stuck rule not triggered. No source access needed or attempted.
- Untestable for lack of a prior letter: F5 language diff, F6 status transitions, F15 list diff, F16 dropped metrics, changed chart baselines and definition drift, F17 consecutive count. All recorded as BASELINE for Q3 FY27.
- Classification lean: where direction was unclear (net cash, FCFF, ROCE, chart basis), the finding is AMBIGUOUS with a question, not resolved in the company's favour.

```yaml
stage: A3-forensics
company: "WEWORK"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/wework-q2fy27/work/forensics_letter_wework_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: FINDING
  F17: FINDING
findings:
  - {id: "L-F1-a", check: "F1", line: "753, 763, 692", classification: "AMBIGUOUS", implication: "IGAAP-only exceptional charge 34.1 Cr in H1 FY25 with no Ind AS counterpart; nature undisclosed; headline basis can strip items outside the audit trail."}
  - {id: "L-F6-a", check: "F6", line: "195-196", classification: "FORWARD-SIGNAL", implication: "~47k desk pipeline (signed leases + LOIs) undated, unsplit, unpriced; not yet in 5,233.1 Cr lease liability; track openings vs 47k each quarter."}
  - {id: "L-F6-b", check: "F6", line: "148-153", classification: "AMBIGUOUS", implication: "'On track to unlock operating leverage' has no date or metric; not trackable as stated."}
  - {id: "L-F7-a", check: "F7", line: "195, 206-207, 92-115", classification: "AMBIGUOUS", implication: "Hedges only in disclaimer; narrative uses 'secured' and 'locked in' for non-binding LOIs and an undefined order book; LOI share NOT FOUND."}
  - {id: "L-F8-a", check: "F8", line: "696, 757, 145", classification: "FORWARD-SIGNAL", implication: "Headline PAT untaxed in all periods; ~16.6 Cr Q2 tax at 25.17% [derived]; 235.0 Cr Ind AS DTA credit booked H1 FY25; tax normalisation date never stated."}
  - {id: "L-F11-a", check: "F11", line: "181, 227-231, 676, 1805-1816", classification: "AMBIGUOUS", implication: "ROCE 34.5% implies capital employed 906.7 Cr vs filed equity+borrowings 732.3 Cr [derived]; formula undisclosed; +590 bps QoQ untestable."}
  - {id: "L-F12-a", check: "F12", line: "220-225, 1847-1848", classification: "FORWARD-SIGNAL", implication: "FCFO > EBITDA only via 146.6 Cr H1 inflow from other and other financial liabilities (nature undisclosed); ex these FCFO ~233.2 Cr < EBITDA 301.2 [derived]; reverses if growth slows."}
  - {id: "L-F14-a", check: "F14", line: "218, 684-698, 745-759 vs 1757-1765", classification: "NEUTRAL-FACT", implication: "Reconciliation 'Reported IndAS' column off filed CA by 0.1-0.2 Cr (Q2 PAT 20.5 vs 20.4; Q1 (4.2) vs (4.1); H1 16.3 vs 16.4); IGAAP figures inherit it."}
  - {id: "L-F14-b", check: "F14", line: "1152, 1581-1582, 881, 883, 1279, 1281", classification: "NEUTRAL-FACT", implication: "Letter annex reproduces results drafting slips unchanged (468,896 vs 4,68,896; plan name two ways; one membership no. under two partner OCR names)."}
  - {id: "L-F16-a", check: "F16", line: "194-195", classification: "AMBIGUOUS", implication: "In-period H1 additions 18.4k = 83.6% of 22k target [derived]; 'past the 22k' only with ~4.5k post-period October desks; target window unstated."}
  - {id: "L-F16-b", check: "F16", line: "172, 175, 202, 599, 1631", classification: "FORWARD-SIGNAL", implication: "Occupancy down 320 bps from March record 86.9% over two quarters [derived]; letter explains only last 114 bps; chart 84%->77% (Mar23-Mar25) unaddressed."}
  - {id: "L-F16-c", check: "F16", line: "206-207, 783, 1811, 1817", classification: "FORWARD-SIGNAL", implication: "3,843/1,421 Cr basis undefined; 1,421 Cr ~1.19 yrs of cash rent; lease liabilities 5,233.1 Cr exceed locked-in revenue [derived]; 2.7x cover is near-window only, hides duration mismatch."}
  - {id: "L-F16-d", check: "F16", line: "224-225, 220, 1797-1800, 1810, 1816, 1860-1861", classification: "AMBIGUOUS", implication: "Net cash 23.1 Cr vs derived 0.2 Cr (gap ~22.9); H1 change ~14 Cr not 333; gross borrowings +17.3% in H1; leases excluded and unmentioned."}
  - {id: "L-F16-e", check: "F16", line: "220-223, 1851-1854, 1865-1866", classification: "AMBIGUOUS", implication: "FCFO/FCFF formula absent; derived FCFF (4.0) Cr vs letter +16.0; 78.4 Cr ROU-addition payments visible in neither FCFO nor capex; resolve before Role 1."}
  - {id: "L-F16-f", check: "F16", line: "405-416, 1631, 1745, 1748", classification: "AMBIGUOUS", implication: "Revenue chart basis unstated; FY26 bar 2,490 equals CA Ind AS total income (incl. 50.2 Cr finance+other income), not revenue from ops 2,440.2; '3.9x' rests on undefined series."}
  - {id: "L-F16-g", check: "F16", line: "204-206, 395, 432", classification: "AMBIGUOUS", implication: "VAS + Digital 14.2% of Q2 revenue [derived] vs 14.6% printed for 2022-24; 'margin-accretive' with no margin given."}
  - {id: "L-F16-h", check: "F16", line: "662-668, 729, 783, 810-811", classification: "AMBIGUOUS", implication: "IGAAP opex adjustment composition undisclosed (residual 0.8-15.2 Cr after cash rent and brokerage); revenue adj flips sign; brokerage +63.5% YoY; positive: basis strips 16.4 of 18.6 Cr other income."}
  - {id: "L-F16-i", check: "F16", line: "213-214, 201, 183, 231-232", classification: "AMBIGUOUS", implication: "Centre-level margin implies 753.5 Cr base (neither 768.7 nor 766.5); breakeven, CoB undefined; rating agency for A- to A+ unnamed."}
  - {id: "L-F17-a", check: "F17", line: "172-262; 1136-1168, 1669, 1811-1817, 1847-1848", classification: "AMBIGUOUS", implication: "11 of 16 watch/results items silent in narrative (lease liability balance, rent-to-revenue, DTA/tax, ESOP dilution, NCLT, lease gains, Labour Code, other-liability build, solar, associate, escrow cash); occupancy partial; 1 quarter, baseline."}
forward_signals: ["L-F6-a", "L-F8-a", "L-F12-a", "L-F16-b", "L-F16-c"]
ambiguous: ["L-F1-a", "L-F6-b", "L-F7-a", "L-F11-a", "L-F16-a", "L-F16-d", "L-F16-e", "L-F16-f", "L-F16-g", "L-F16-h", "L-F16-i", "L-F17-a"]
commitments:
  - {commitment: "~47k desks secured via signed leases and LOIs (32% beyond 145.3k capacity)", implied_date: "NOT FOUND", ref: "p5 L195-196", status_word: "secured (LOI share NOT FOUND)"}
  - {commitment: "~4.5k desks opened first week of October 2026", implied_date: "2026-10 (post-period)", ref: "p5 L194", status_word: "completed (claimed; verify Q3)"}
  - {commitment: "22k desk-addition target set in Q1", implied_date: "window NOT FOUND", ref: "p5 L195", status_word: "claimed met only with post-period openings"}
  - {commitment: "Unlock operating leverage and more profitable growth", implied_date: "NOT FOUND", ref: "p4 L151-153", status_word: "on track (no metric)"}
  - {commitment: "Evaluate and account for Labour Code rules when notified", implied_date: "on notification; NOT FOUND", ref: "SA Note 5 L1141-1143; CA Note 5 L1572-1573", status_word: "pending"}
  - {commitment: "NCLT capital reduction: set off Rs 20,501.60 Mn accumulated losses against Securities Premium", implied_date: "on NCLT sanction; NOT FOUND", ref: "SA Note 10 L1165-1168; CA Note 10 L1592-1594", status_word: "initiated"}
  - {commitment: "IPO OFS 46,296,296 shares, Rs 29,996.43 Mn; listed NSE/BSE", implied_date: "2025-10-10", ref: "SA Note 6 L1145-1150; CA Note 6 L1575-1579", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The pages 17-18 bridge reconciles the headline basis, but four KPIs that carry the narrative do not reproduce from the statements in the same letter: net cash 23.1 Cr (derived 0.2 Cr), FCFF 16.0 Cr (derived (4.0) Cr; 78.4 Cr ROU-addition payments sit in neither FCFO nor capex), ROCE 34.5% (capital employed undefined), and the 3,843/1,421 Cr order-book cover (basis undefined). The 2.7x cover is a near-window ratio: 1,421 Cr is about 1.2 years of current cash rent, while Ind AS lease liabilities are 5,233 Cr. FCFO above EBITDA rests on 146.6 Cr of H1 liability inflows of undisclosed nature. Occupancy fell 320 bps from the March record over two quarters, and the letter explains only the last 114 bps. The 22k desk target was reached only by counting October openings. Headline PAT carries zero tax. In the company's favour, the IGAAP basis strips 16.4 of 18.6 Cr finance and other income, so the headline does not lean on the treasury and lease gains the results A3 flagged. Every prior-quarter diff is a baseline."
```
