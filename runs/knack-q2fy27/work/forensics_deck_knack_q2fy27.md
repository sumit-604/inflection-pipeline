# A3 FORENSIC NOTES: KNACK Q2 FY27 (doctype: presentation / deck)

Company: Knack Packaging Limited (KNACK, BSE 544814). Quarter: Q2 FY27 (quarter and half year ended 30-Sep-2026).
Inputs read: A1 structured `extracted/knack-deck-q2fy27-structured.md` (R001-R798), A1 fulltext `extracted/knack-deck-q2fy27-fulltext.md` (L1-847, OCR L641-847), A2 ledger `work/ledger_deck_knack_q2fy27.md` (798 R rows + M01-M06).
Not read: source PDF, anything under `inputs/`. No prior-quarter extract (first review). No Notion page or companies/KNACK.md (PRE-THESIS READ); F17 uses the coordinator watch list.
Units: Rs Million unless marked (Cr = x0.1). Every derived number below is arithmetic on cited rows. No missing number is estimated.

## 0. LEDGER RECONCILIATION
- Structured rows read at their fulltext line: 798 of 798 (R001-R798). M01-M06 read at their own lines (L22, L24, L25, L26, L45, L704). 804 of 804 = 100%.
- ZERO_STANDING 15 rows: all read (Section F1 table).
- FORWARD_COMMIT 23 rows (R628-R650): all in the commitment register or findings.
- FOOTNOTE_UNRESOLVED 6 rows: R711 -> D-A3-11; R717 -> D-A3-13; R726 -> left with A1 (name mapping on p23; only R692, the CS bio, is used here); R729 and R737 RESOLVED by arithmetic: EBITDA = profit before exceptional items and tax + finance cost + D&A, and it INCLUDES Other Income. Q2 FY27: 356.74 + 38.70 + 102.20 = 497.64 (R361, R337, R343) vs 497.65 printed (R110). Q1 FY27: 452.87 + 40.26 + 98.60 = 591.73 (R111). Q2 FY26: 280.63 + 30.52 + 71.89 = 383.04 (R112). Headline margins divide by Total Income: 497.65 / 3,044.61 = 16.35%. R740 (RoCE/RoE definition) stays unresolved. Q2 FY27 RoE 19.42% reproduces as (Q2 PAT x 4) / average of Mar-26 and Sep-26 equity: 1,000.80 / 5,152.55 = 19.42%. H1 21.29% does not reproduce on the same basis (21.56%).
- RESTATED groups: duplicates only (same value printed twice). No restatement of a prior-period value is visible inside the deck. The word "Restated" in the statement titles is handled in D-A3-13.
- M01-M05: address and signature tokens, no forensic content.
- M06 ("14%", OCR p13 L704, between "nine" L703 and "UNIT-5" L705): UNRESOLVED. No label is recoverable from A1's OCR text, and A3 cannot open the render. NOT used in any finding. It could be a utilisation or share figure. It goes back to A1 for a render check before A4 cites it.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| D-A3-01 | F16 | R110-R112, R301-R303, R295-R297, R116, R729, R737 | L352, L364, L474 (p26, p27, p31) | "EBITDA margin of 16.35% reflects global input cost headwinds" | FORWARD-SIGNAL | Headline EBITDA includes Other Income and is divided by Total Income. Operating EBITDA (EBITDA minus Other Income) was 400.61 in Q2 FY27, 13.59% of revenue from operations 2,947.57. That compares with 21.66% in Q1 FY27 (568.61 / 2,624.59) and 16.57% in Q2 FY26 (320.13 / 1,932.57). Operating EBITDA fell 29.5% QoQ while revenue from operations rose 12.3%. Other Income is 19.5% of Q2 EBITDA (97.04 / 497.65), against 3.9% in Q1. The true operating drop is 807 bps QoQ, not the 600 bps headline. Use 13.59% as the Q3 pass-through baseline. |
| D-A3-02 | F7 | R643, R695, R313-R327 | L353-354 (p26); L479-481 (p31) | "adjustments expected to reflect in realizations from Q3 FY27 onwards subject market stabilization" | FORWARD-SIGNAL | The pass-through is "currently underway" and hedged with "subject [to] market stabilization". Gross margin (revenue from operations minus materials, purchases and inventory change) was 34.64% in Q2 FY27 (COGS 1,926.60), against 42.07% in Q1 FY27 and 41.15% in Q2 FY26. Q1 FY27 was helped by a 316.12 FG/WIP build (R326). Q2 had almost none (2.69, R325). Q3 test: gross margin back above 40% with no fresh FG build. If it fails, the hedge was the signal. |
| D-A3-03 | F16 | R102, R379, R381, R644, R645 | L355-356 (p26); L490 (p31) | "this drag reverses and PAT margin recovers fully" | FORWARD-SIGNAL | Excluding the JV, Q2 FY27 PAT margin was 9.08% ((250.20 + 26.15) / 3,044.61), against 10.43% in Q2 FY26 ((206.36 + 1.78) / 1,995.48). The JV explains about 77 bps of the 212 bps decline. JV breakeven therefore does NOT restore the PAT margin in full. The JV share is also 10.9% of H1 PAT (60.60 / 555.48), not "slightly" (L355). This is Knack's 50% share (R044), so the JV-level loss is about 121.20 in H1. |
| D-A3-04 | F1 | R440, R441, R103, R382, R540, R544, R458, R459, R680 | L515, L356, L598, L600, L205 | "consolidated PAT with zero revenue offset today" | AMBIGUOUS | The equity-method JV investment went from 34.55 (Mar-26) to nil (Sep-26). The H1 JV loss of 60.60 exceeds the opening carrying value by 26.05. Q1's loss of 34.45 almost exactly used up the 34.55. There was no equity infusion in H1 (R540 nil, against 42.18 in H1 FY26), but net loans of 138.29 were given (R544). Current loans fell from 50.55 to 16.94, and the deck has no non-current loans line. Questions: (a) Which balance absorbed the excess 26.05 loss (long-term interest/loan, or a provision)? (b) Who received the 138.29 loan? (c) Why does the JV report "zero revenue" six months after "Plant commissioned in April 2026" (L205)? |
| D-A3-05 | F2 | R104-R187 | L363-366 (p27) | "250.20 305.28 206.36 555.48 412.97 927.24 258.44 315.06 203.96 573.49 402.16 894.21" | AMBIGUOUS | The consolidated-minus-standalone PAT gap as % of standalone PAT: FY26 +3.69%, H1 FY26 +2.69%, Q2 FY26 +1.18%, Q1 FY27 -3.10%, Q2 FY27 -3.19%, H1 FY27 -3.14%. H1-on-H1 swing -5.83 pp. FY26 to H1 FY27 swing -6.83 pp. Both exceed the 5 pp threshold. Split: JV share -60.60 in H1 FY27. Subsidiary plus eliminations +42.59 in H1 FY27, against +12.59 in H1 FY26 and +42.44 in all of FY26. The revenue gap (Total Income basis) is 108.19 in H1 FY27 and the EBITDA gap 57.71, which is 53% "margin" on the gap. The South Africa subsidiary (R583, R780) earns outsized margin on small revenue. Ask what it does (sales arm, trading, transfer pricing) and its standalone revenue and PAT. |
| D-A3-06 | F8 | R385-R408, R444, R445, R479, R480, R556 | L493-494, L517, L553, L613 | "(f) Deferred Tax Assets (Net)" | AMBIGUOUS | Tax / profit before JV and tax: Q2 FY27 22.54% (80.40 / 356.74), Q1 FY27 24.98%, Q2 FY26 25.83%, H1 FY27 23.90%, FY26 25.67%. The statutory rate is 25.17%. Q2 FY27 has the first deferred-tax CREDIT (6.09) in the six periods shown, a 171 bps shield. On the balance sheet, net DTL 42.22 (Mar-26) became net DTA 7.83 (Sep-26), a swing of 50.05 against a P&L credit of 3.89. About 46.16 sits outside P&L. The equity roll-forward leaves an independent residual of 45.96 (see F11). Candidate: the tax effect of IPO issue expenses (Sec 35D) credited to equity. Confirm with the results filing. Q3 ETR should revert towards 25%, and the Q2 shield should not recur. No "earlier years" tax line appears in the deck. |
| D-A3-07 | F10 | R469, R470, R123, R134, R135, R136, R427 | L544, L498, L350-351 | "EPS holding firm at 2.07, very strong" | FORWARD-SIGNAL | Paid-up capital rose from 1,000.00 to 1,223.65 (+22.4%). Implied weighted shares: Q1 FY27 100.09 Mn (305.28 / 3.05), Q2 FY27 120.87 Mn (250.20 / 2.07). Period-end shares are 122.37 Mn (at the Rs 10 face value implied by Q1). Q2 PAT on period-end shares gives EPS Rs 2.04, below Q2 FY26's Rs 2.06. Q3 carries full dilution, so EPS growth will trail PAT growth by about 22 pp for four quarters. Basic equals diluted (one line, L498), so the deck shows no dilutive instruments. |
| D-A3-08 | F6 | R279, R282, R454-R457, R536, R537, R542, R554, R556, R558, R648-R650 | L453-458, L462-463 (p30); L527-528 (p32); L596-614 (p34-35) | "deployment of IPO proceeds into productive assets is still underway" | FORWARD-SIGNAL | The fresh issue raised 3,800.00, with 253.03 of issue expense. Cash 680.49 plus other bank balances 2,647.34 = 3,327.83, which is 93.8% of the 3,546.97 net proceeds. H1 FY27 capex was 274.99, against 454.68 in H1 FY26, so capex FELL after the IPO. Borrowings of 1,910.55 (≈191 Cr) were kept, and short-term borrowings rose 81.00 (R558). Yet the deck says "zero leverage dependency on growth" (L463). RoCE "will recover and improve in the coming quarters" (L457-458), but the stated new facility is only due by October 2027 (L250-251). Ask for the IPO objects-versus-utilisation table, and why debt was not retired. |
| D-A3-09 | F6 | R023, R646, R633, R634, R686, R774-R777, R434, R435, M06 | L101, L388-389, L248-251, OCR L744, L710 | "are firing at full capacity, with the FY26 capex-driven" | FORWARD-SIGNAL | Installed capacity is "50,000+ MTPA" (H1 FY27) and the India plants run "at full capacity". Units 4 and 5 were established in April and July 2026 (OCR). The next capacity step is "by October 2027". Net PPE grew only 176.87 in H1 (2,332.79 to 2,509.66). Q3 FY27 to Q2 FY28 volume growth is capped, so growth must come from price and mix. Unit 4 and 5 capacity, utilisation %, and how the Oct-2027 facility relates to Units 4 and 5 are all NOT FOUND. M06 "14%" on the same slide is unresolved and not used. |
| D-A3-10 | F16 | R197-R200, R237-R244, R289-R294, R732, R734, R736, R741 | L461 (p30), L370 (p27), L400 (p28), L376-391, L403-430 | "Q1 FY26 Q1 FY27" | AMBIGUOUS | The charts on pp28-30 hold Q1 FY26 and Q1 FY27 series in the text layer, but the render does not show them. Examples: Q1 FY27 consolidated EBITDA margin 22.35% (R240) and revenue 2,647.71 (R198). The p30 legend still names Q1 periods, and the p27/p28 footers read "Q1 FY2026-27". The deck was built on the Q1 template, and the Q1 columns are hidden. As rendered, the charts show only YoY and H1, which hides the 600 bps sequential EBITDA-margin fall. p30 holds six hidden ratio values (RoCE 54.73%, 46.05%, and others) with periods unmapped. Ask management for the Q1 FY27 RoCE/RoE. |
| D-A3-11 | F16 | R711, R101, R204, R581 | L102 (p6); L84, L379-380 | "Export CEoBnItTrDibAut/ioPnAT(F(YH216)- FY27)" | AMBIGUOUS | The interleaved text layer carries an "Export Contribution (FY26)" tile label, but the render shows no tile or value. The deck calls the company "export led" (L84) and credits growth to "significantly higher export volumes across 75 countries" (L379-380), yet export share is NOT FOUND anywhere in the deck. A metric whose label was drafted and whose value was withheld is a dropped-disclosure signal. Ask for export share for FY26, H1 FY26 and H1 FY27. |
| D-A3-12 | F16 | R046-R050, R595, R598, R629-R632, R640, R019, R020 | L219, L240-241, L251, L99-100 (p16, p17, p19, p6) | "with no material dependency on any segment" | FORWARD-SIGNAL | One customer contract of "~1,500 Mn" a year (L219) equals 18.2% of FY26 revenue from operations (8,234.34) and 13.5% of H1 FY27 annualised revenue (11,144.32). Implied price is about Rs 25 per bag (1,500 / 60 Mn bags). Top-10 customers were 40.87% of FY26 revenue. The counterparty is unnamed on p16 (L216), but p19 names "partnership with Cargill" (L251). The contract runs to December 2028, which is a renewal cliff inside a 3-5 year hold. Ask how much of the 1,500 Mn is incremental versus renewal, and for the H1 FY27 top-1 and top-10 share. |
| D-A3-13 | F14 | R743, R748, R750, R744, R186, R184, R201, R090, R271, R735, R738, R751, R594, R584, R782, R717, R582, R556 | L470, L508, L539, L369, L377-378, L345, L462, L613, L147, L109/L208/OCR L764 | "Restated Consolidated Statement of Profit and Loss" | AMBIGUOUS | Twelve drafting defects, each small. (1) "Restated" titles (IPO RHP wording) sit on Unaudited interim statements. The cash-flow slides drop the word. (2) Standalone H1 FY26 net worth is printed as 3361.21, but Q2 FY26 (same date) is 2552.23. 3361.21 is the Q1 FY27 value copied over. (3) The p28 text pairs "52.52%" with Total Income values 3,044.61 / 1,995.48, whose true growth is 52.58%. 52.52% is revenue-from-operations growth. (4) p26 ROE change is 1538 bps, but p30 says -1,539 bps. (5) Rounding drifts: 5,692.32 vs 5,692.31, and 1,089.38 vs 1,089.37. (6) Total assets 10,269.96 vs total equity and liabilities 10,269.95. (7) The JV is named three ways (L109, L208, OCR L764). (8) "revenue nearly doubling" (L462) against +52.5%. (9) The cash flow says "Share issue expense (net of tax)", but a cash outflow cannot be net of a deferred tax (see D-A3-06). (10) The p9 customer count is blank. (11) The rating agency is not named. (12) p27 "Revenue" is Total Income. Together they are a governance data point. Ask whether any prior-period figure was restated against the original filings. |
| D-A3-14 | F13 | R692, R614, R579, R703 | L328, L333, L46-47 | "Associated with the Company since 9th August, 2026" | AMBIGUOUS | The Company Secretary and Compliance Officer who signs the cover letter joined on 9-Aug-2026, weeks after the listing quarter. The IPO-era CS must have left around listing. Ask for the prior CS's name, exit date and reason. The three independent directors all joined on 18-Jul-2025 (pre-IPO board build; L304-307). No renewal falls in the window. |
| D-A3-15 | F14 | R038-R043, R045, R593, R681 | L184-186 (p11); L206-207 (p15) | "Total installed: 5 machines" | AMBIGUOUS | The p11 count of 5 pinch-bottom machines (4th and 5th arrived 2026) does not say whether the Mexico JV's machine, "Commissioned 1 Pinch Bottom Machine from April 2026", is one of the 5. If it is, India has 4 machines and the "5x growth" claim includes JV capacity that is not consolidated. Pinch-bottom bags drive the premium export mix, so the India machine count bears on the price/mix lever in D-A3-09. |
| D-A3-16 | F17 | R534, R535, R522-R533, R085, R086, R450-R453, R462, R463 | L593, L588-590 (p34), L347 (p26), L523-532 (p32) | "Net cash generated from operating activities" | FORWARD-SIGNAL | H1 FY27 CFO was 220.59, against 389.44 in H1 FY26 (-43%), while PAT rose 34.5%. CFO/PAT fell from 0.94 to 0.40, and CFO/EBITDA from 50.6% to 20.2%. Receivables rose 404.78 (+29.3%) in six months against +25.5% half-on-half revenue. Other current assets rose 150.26 (+53.5%). The "75 Days" working-capital tile does not reproduce from the deck's own rows: (1,462.54 + 1,787.77 - 566.94) / (Q2 revenue from operations x 4) x 365 = 83 days. No definition is given. Receivable days and inventory days are not disclosed. Ask for the definition and the components. |

## 2. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | 15 ZERO_STANDING rows read (table below). The material one is R440: JV equity-method investment nil at Sep-26 (D-A3-04). |
| F2 | FINDING | The deck carries S-vs-C Revenue, EBITDA and PAT for 6 periods (p27). The PAT-gap swing exceeds 5 pp (D-A3-05). The results A3 owns the filed version. |
| F3 | N.A. | The deck carries no standalone cost lines (only S Revenue, EBITDA, PAT, NW). The shell test belongs to the results filing. The 1.7% revenue gap shows the subsidiary operates. |
| F4 | N.A. | No auditor report or Other Matters paragraph in a presentation. |
| F5 | N.A. | No auditor report or EoM in a presentation. No prior quarter to diff. |
| F6 | FINDING | 13 commitments registered. IPO deployment "still underway" with 93.8% of net proceeds in cash and bank balances (D-A3-08). Capacity commitments conflict (D-A3-09). |
| F7 | FINDING | One lexicon hit outside the safe harbour: "subject market stabilization" on the pass-through (D-A3-02). The p3 safe harbour is boilerplate. |
| F8 | FINDING | Q2 ETR on pre-JV PBT is 22.54% against 25.17%. First deferred-tax credit. 46.16 of DT movement sits outside P&L (D-A3-06). |
| F9 | PASS | OCI Q2 FY27 (4.43), Q1 (2.60), H1 (7.03), against FY26 +7.52. No single quarter swing exceeds the prior full year (4.43 < 7.52). The sign turned negative; watch at the AR. |
| F10 | FINDING | Paid-up capital +22.4% from the IPO. Q2 EPS on period-end shares is 2.04 < 2.06 YoY. Basic equals diluted (D-A3-07). |
| F11 | PASS | 1,223.65 + 5,999.59 = 7,223.24 = p27 net worth. Debt 1,910.55 = "~191 Cr". D/E 0.26x reproduces. The equity roll-forward residual of 45.96 (0.64%) is under the 5% bar. Candidate reconciling item: tax on issue expenses credited to equity (D-A3-06). |
| F12 | N.A. | The deck carries no segment assets, liabilities or results. |
| F13 | FINDING | The cover letter records only results approval. KMP change: CS since 9-Aug-2026 (D-A3-14). |
| F14 | FINDING | 12 drafting defects, including "Restated" titles on unaudited interims and a copied standalone NW (D-A3-13), plus the machine-count ambiguity (D-A3-15). |
| F15 | N.A. | No prior-quarter entity list (first review). Baseline recorded: 1 subsidiary (Knack Packaging SA (RF) (Pty) Ltd, South Africa) and 1 JV (Sayem Knack SA de CV / "Knack-BESSHER HOLDING S.A.P.I. DE C.V", 50:50, Mexico). |
| F16 | FINDING | No prior deck, so the within-deck evidence is used. Margins are computed on Total Income including Other Income (D-A3-01). Q1 series are hidden (D-A3-10). The export tile has no value (D-A3-11). The JV and concentration claims are reframed (D-A3-03, D-A3-12). |
| F17 | FINDING | Coordinator watch list run against the deck. 5 of 9 items are silent or have no number (table below). Cash conversion deteriorated without comment (D-A3-16). |

### F1 ZERO_STANDING table (15 rows)
| row | line | line item | reading |
|---|---|---|---|
| R103 | L356 | JV "zero revenue offset today" | Not a template line. It is a management phrase. JV revenue never consolidates under the equity method. If the JV itself has no revenue six months after commissioning, that is the signal (D-A3-04). |
| R367-R371 | L488 | Exceptional Item, Labour Codes (5 interim columns nil) | FY26 carried 10.77 (R372). The line stays in the template for further Labour Code true-ups (gratuity and leave on the new wage definition). Non-current provisions appeared at 2.29 from nil (R481/R482), a candidate first trace. No finding. Watch Q3/Q4. |
| R440 | L515 | Investments accounted for equity method, Sep-26 nil | Opening 34.55 has been absorbed by JV losses. Losses now exceed the carrying value (D-A3-04). |
| R445 | L517 | DTA Mar-26 nil | Flipped to 7.83 DTA at Sep-26 (D-A3-06). |
| R479 | L553 | DTL Sep-26 nil | DTL of 42.22 eliminated (D-A3-06). |
| R482 | L554 | Non-current provisions Mar-26 nil | New 2.29 at Sep-26. Minor. |
| R540 | L598 | Purchase of equity investment H1 FY27 nil | No fresh JV equity in H1. Funding route switched to loans? (D-A3-04) |
| R543 | L599 | Investment in FD H1 FY26 nil | H1 FY27 2,643.41 = IPO cash parked (D-A3-08). |
| R550 | L610 | Proceeds from long-term borrowings H1 FY27 nil | No new term debt. Short-term borrowing still +81.00 (D-A3-08). |
| R555, R557 | L612-613 | Share capital proceeds and issue expense, H1 FY26 nil | Prior-year comparatives before the IPO. No finding. |

## 3. COMMITMENT REGISTER (F6)
| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| 1 | Customer pricing revisions to pass on input-cost increases; realisations to reflect | from Q3 FY27, "subject [to] market stabilization" | p26 L353-354 (R643, R695) | underway |
| 2 | Deploy IPO proceeds (Rs 380 Cr) into capacity and growth initiatives | not dated | p30 L453-457 (R279, R649) | underway |
| 3 | RoCE and RoE "will recover and improve" | "coming quarters" (Q3-Q4 FY27 implied) | p30 L457-458 (R648) | initiated (claim) |
| 4 | Commission new facility increasing effective capacity | by October 2027 | p19 L250-251 (R634, R686) | initiated (planned) |
| 5 | Expand manufacturing capacity | by FY28 | p19 L248-249 (R633, R685) | initiated (planned) |
| 6 | Solar installations for the proposed facility | with item 4 | p19 L261-262 (R641) | initiated (planned) |
| 7 | Mexico JV plant commissioned, 1 pinch-bottom machine | April 2026 | p15 L203-207; p7 L133-137 (R033, R045, R680, R681) | completed |
| 8 | JV to reach breakeven, so PAT margin "recovers fully" | not dated ("peak scale-up investment phase") | p26 L355-356 (R644, R645) | initiated (claim) |
| 9 | Order and 3-year contract renewal: ~60 Mn bags, ~1,500 Mn per annum | to December 2028 | p16 L213-220 (R046-R050, R629-R631, R682) | completed (renewed) |
| 10 | India Units 4 and 5 established | April 2026 / July 2026 | p13 OCR L744, L710 (R775, R777) | completed (established); capacity NOT FOUND |
| 11 | 4th and 5th pinch-bottom machines arrived; total installed 5 | 2026 | p11 L184-186 (R041, R043, R679) | completed (perimeter ambiguous, D-A3-15) |
| 12 | New categories: modern-trend packaging, >50 kg bags, pulses/spices/rice/pet food; Europe, Australia, Gulf, Africa; leverage Cargill partnership | not dated | p19 L249-262 (R636-R640) | initiated (intent) |
| 13 | Listing on NSE and BSE mainboard | 2026 | p7 L139-141 (R586) | completed |

## 4. F17 SILENCE AUDIT: "WHAT WAS NOT DISCUSSED" (coordinator watch list; deck)
| # | checklist item | deck treatment | ref | consecutive quarters silent |
|---|---|---|---|---|
| 1 | Volume (tonnes or bags) | SILENT. No production or sales volume. Only "significantly higher export volumes" without a number, plus one contract's ~60 Mn bags | L379; L218 | 1 (first review) |
| 2 | Realisation per kg | SILENT. NOT FOUND. Only "reflect in realizations from Q3 FY27" | L354 | 1 |
| 3 | Polymer (PP granule) pass-through | ADDRESSED qualitatively. No quantum, lag or contract-clause detail | L352-354 | 0 |
| 4 | Export share | SILENT. Tile label present, value absent (D-A3-11) | L102 | 1 |
| 5 | Capacity utilisation | NUMBER SILENT. Only "firing at full capacity". M06 "14%" unresolved | L388; OCR L704 | 1 |
| 6 | New capacity timeline (Units 4 and 5) | PARTIAL. Establishment dates given. Capacity, ramp, and link to the Oct-2027 facility NOT FOUND (D-A3-09) | OCR L744, L710; L250-251 | 0 (partial) |
| 7 | Receivable days and inventory days | SILENT on components. Composite "75 Days" only, not reproducible (D-A3-16) | L347 | 1 |
| 8 | Customer concentration | ADDRESSED for FY26 only (top-10 40.87%, continuity 93.75%). No H1 FY27 update. Claim of "no material dependency" (D-A3-12) | L99-100; L240-241 | 0 (stale) |
| 9 | IPO proceeds use | SILENT on use by object. "still underway" only. 93.8% in cash and bank balances (D-A3-08) | L455-456; L527-528 | 1 |
| F6-2 | IPO deployment schedule | no date | L455-456 | 1 |
| F6-8 | JV breakeven date | no date | L356 | 1 |

Role 5 note: silence count starts at 1 this quarter. Items 1, 2, 4 and 7 move to confirmatory-negative if the Q3 FY27 deck stays silent while D-A3-01/D-A3-16 metrics weaken.

## 5. HAND-OFF TO A4
FORWARD-SIGNAL (8): D-A3-01, 02, 03, 07, 08, 09, 12, 16.
AMBIGUOUS, convert to management questions (8): D-A3-04, 05, 06, 10, 11, 13, 14, 15.
Cross-document checks for the results/concall A3 runs (not done here, per instruction): the EBITDA definition, the JV carrying value and loans, the deferred tax on issue expenses, the standalone H1 FY26 net worth, and whether "Restated" means restated.

```yaml
stage: A3-forensics
company: "KNACK"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-knack-q2fy27-0febb1/runs/knack-q2fy27/work/forensics_deck_knack_q2fy27.md"
ledger_reconciled_pct: 100        # 798 R rows + 6 M rows read at cited lines; M06 logged UNRESOLVED
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "D-A3-01", check: "F16", line: "L352, L364, L474 (p26-p31)", classification: "FORWARD-SIGNAL", implication: "EBITDA includes Other Income and is divided by Total Income; operating EBITDA 400.61 = 13.59% of revenue from ops vs 21.66% Q1 and 16.57% Q2 FY26; operating EBITDA fell 29.5% QoQ"}
  - {id: "D-A3-02", check: "F7", line: "L353-354, L479-481", classification: "FORWARD-SIGNAL", implication: "pass-through hedged 'subject market stabilization'; gross margin 34.64% vs 42.07% Q1 (Q1 helped by 316.12 FG/WIP build); Q3 test is GM back above 40%"}
  - {id: "D-A3-03", check: "F16", line: "L355-356, L490", classification: "FORWARD-SIGNAL", implication: "ex-JV PAT margin 9.08% vs 10.43% YoY; JV explains ~77 of 212 bps, so breakeven does not restore margin; JV share 10.9% of H1 PAT, not 'slightly'"}
  - {id: "D-A3-04", check: "F1", line: "L515, L356, L598, L600, L205", classification: "AMBIGUOUS", implication: "JV equity-method investment 34.55 to nil; H1 loss 60.60 exceeds carrying value by 26.05; no equity infusion but net loans 138.29 given with no matching loan asset; JV 'zero revenue' despite April 2026 commissioning"}
  - {id: "D-A3-05", check: "F2", line: "L363-366", classification: "AMBIGUOUS", implication: "C-minus-S PAT gap swung from +2.69% (H1 FY26) to -3.14% (H1 FY27), -5.83 pp; JV -60.60, subsidiary plus eliminations +42.59 (3.4x YoY) at ~53% EBITDA on a 108.19 revenue gap; SA subsidiary role and transfer pricing open"}
  - {id: "D-A3-06", check: "F8", line: "L493-494, L517, L553, L613", classification: "AMBIGUOUS", implication: "Q2 ETR on pre-JV PBT 22.54% vs 25.17%; first deferred-tax credit (6.09, 171 bps); net DT swing 50.05 vs P&L 3.89, ~46 outside P&L, matches equity residual 45.96; candidate: issue-expense tax credited to equity"}
  - {id: "D-A3-07", check: "F10", line: "L544, L498, L350-351", classification: "FORWARD-SIGNAL", implication: "share capital +22.4%; Q2 weighted 120.87 Mn vs period-end 122.37 Mn shares; Q2 PAT on period-end shares = EPS 2.04 < 2.06 YoY; EPS trails PAT by ~22 pp for four quarters"}
  - {id: "D-A3-08", check: "F6", line: "L453-463, L527-528, L596-614", classification: "FORWARD-SIGNAL", implication: "3,327.83 cash and bank balances = 93.8% of 3,546.97 net IPO proceeds; capex fell to 274.99 from 454.68; debt 1,910.55 retained, short-term borrowing +81.00 vs 'zero leverage dependency'; RoCE recovery claim vs facility only by Oct 2027"}
  - {id: "D-A3-09", check: "F6", line: "L101, L388-389, L248-251, OCR L744, L710", classification: "FORWARD-SIGNAL", implication: "'full capacity' at 50,000+ MTPA; Units 4/5 established Apr/Jul 2026 but net PPE only +176.87; next step Oct 2027; volume capped ~4 quarters; utilisation % NOT FOUND; M06 14% unresolved"}
  - {id: "D-A3-10", check: "F16", line: "L461, L370, L400, L376-430", classification: "AMBIGUOUS", implication: "Q1 FY26/Q1 FY27 chart series hidden on pp28-30 (Q1 FY27 EBITDA margin 22.35%); Q1 template legend and footers left in; charts hide the 600 bps sequential fall; six hidden RoCE/RoE values"}
  - {id: "D-A3-11", check: "F16", line: "L102, L84, L379-380", classification: "AMBIGUOUS", implication: "'Export Contribution (FY26)' tile label present with no value in an 'export led' deck that credits growth to export volumes; export share NOT FOUND"}
  - {id: "D-A3-12", check: "F16", line: "L219, L240-241, L251, L99-100", classification: "FORWARD-SIGNAL", implication: "single contract ~1,500 Mn/yr = 18.2% of FY26 revenue from ops (~Rs 25/bag) vs 'no material dependency'; Cargill named on p19 only; renewal cliff Dec 2028"}
  - {id: "D-A3-13", check: "F14", line: "L470, L508, L539, L369, L377-378, L345, L462, L613, L147", classification: "AMBIGUOUS", implication: "12 drafting defects incl. 'Restated' titles on unaudited interims, standalone H1 FY26 NW 3361.21 copied from Q1 FY27, 52.52% paired with total-income values, JV named three ways; ask whether any prior period was restated"}
  - {id: "D-A3-14", check: "F13", line: "L328, L333, L46-47", classification: "AMBIGUOUS", implication: "Company Secretary and Compliance Officer joined 9-Aug-2026, weeks after the listing quarter; IPO-era CS exit unexplained"}
  - {id: "D-A3-15", check: "F14", line: "L184-186, L206-207", classification: "AMBIGUOUS", implication: "'Total installed: 5 machines' may include the Mexico JV pinch-bottom machine; India count may be 4; this bears on the price/mix lever"}
  - {id: "D-A3-16", check: "F17", line: "L593, L588-590, L347, L523-532", classification: "FORWARD-SIGNAL", implication: "H1 CFO 220.59 vs 389.44 (-43%) while PAT +34.5%; CFO/EBITDA 20.2% vs 50.6%; receivables +29.3% vs revenue +25.5% HoH; '75 Days' WC tile not reproducible (83 days on rows); components undisclosed"}
forward_signals: ["D-A3-01", "D-A3-02", "D-A3-03", "D-A3-07", "D-A3-08", "D-A3-09", "D-A3-12", "D-A3-16"]
ambiguous: ["D-A3-04", "D-A3-05", "D-A3-06", "D-A3-10", "D-A3-11", "D-A3-13", "D-A3-14", "D-A3-15"]
commitments:
  - {commitment: "Pass input-cost increases to customers; realisations reflect", implied_date: "from Q3 FY27, subject to market stabilisation", ref: "p26 L353-354", status_word: "underway"}
  - {commitment: "Deploy Rs 380 Cr IPO proceeds into capacity and growth", implied_date: "not dated", ref: "p30 L453-457", status_word: "underway"}
  - {commitment: "RoCE and RoE recover and improve", implied_date: "coming quarters", ref: "p30 L457-458", status_word: "initiated"}
  - {commitment: "New facility increasing effective capacity", implied_date: "by October 2027", ref: "p19 L250-251", status_word: "initiated"}
  - {commitment: "Expand manufacturing capacity", implied_date: "by FY28", ref: "p19 L248-249", status_word: "initiated"}
  - {commitment: "Solar installations at proposed facility", implied_date: "with new facility", ref: "p19 L261-262", status_word: "initiated"}
  - {commitment: "Mexico JV plant commissioned, 1 pinch-bottom machine", implied_date: "April 2026", ref: "p15 L203-207", status_word: "completed"}
  - {commitment: "JV breakeven restores PAT margin", implied_date: "not dated", ref: "p26 L355-356", status_word: "initiated"}
  - {commitment: "~60 Mn bags, ~1,500 Mn/yr order and 3-year contract renewal", implied_date: "to December 2028", ref: "p16 L213-220", status_word: "completed"}
  - {commitment: "India Units 4 and 5 established", implied_date: "April 2026 / July 2026", ref: "p13 OCR L744, L710", status_word: "completed"}
  - {commitment: "4th and 5th pinch-bottom machines arrived, 5 installed", implied_date: "2026", ref: "p11 L184-186", status_word: "completed"}
  - {commitment: "New categories and geographies; leverage Cargill partnership", implied_date: "not dated", ref: "p19 L249-262", status_word: "initiated"}
  - {commitment: "Listing on NSE and BSE mainboard", implied_date: "2026", ref: "p7 L139-141", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's headline numbers flatter the quarter in three stacked ways. First, EBITDA includes Other Income, which rose from 23 to 97 as IPO cash went into fixed deposits. Second, margins divide by Total Income. Third, the charts hide the Q1 FY27 columns that show the sequential fall. Strip all three and operating EBITDA fell 29.5% QoQ while revenue rose 12.3%. Gross margin fell 743 bps. Management blames polymer and freight, and the pass-through is hedged. Q3 gross margin is the separating observation: input-cost lag versus loss of pricing power. The JV story does not hold either. Breakeven explains only ~77 of 212 bps of PAT-margin loss. The equity-method investment is already at nil, and 138 of loans went out with no visible loan asset. That is the item most likely to grow. IPO cash sits idle, capacity is full until Oct 2027, and EPS carries 22% dilution, so FY27 per-share growth depends on price and mix alone. M06 '14%' was not used; A1 must label it from the render."
```
