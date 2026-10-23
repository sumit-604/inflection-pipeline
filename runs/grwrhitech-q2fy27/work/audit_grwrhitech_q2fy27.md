# A5 ADVERSARY AUDIT: GRWRHITECH (Garware Hi-Tech Films Limited) | Q2 FY27

Audited artifact: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md (A4, 673 lines).
Inputs read: A1 fulltext (FT, 1,492 lines), A1 structured (ST, R001-R1782), A2 ledger (LG), A4 review (RV). No source PDF opened. Nothing under inputs/ opened. A3 reasoning not read.
Anchors: "FT l.N", "ST l.N", "LG l.N", "RV l.N" are line numbers in those files. [DERIVED] = my arithmetic on filed numbers, formula shown.
Scope: Notion baseline values (RV l.25-55) and the orchestrator-supplied MPCB Reg 30 facts (RV l.81) are outside A5 inputs. I check only their internal arithmetic and the filing's silence. A grep of FT for "MPCB|pollution|consent|bank guarantee" returns zero hits. The only related text is the ESG slide, FT l.1369-1370.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading (RV) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | l.547 | 13 lines (l.548-560), inside 10-20. Results filing, so the 200-400 word rule does not govern | present |
| 2. Sector intelligence | l.562 | 6 bullets (l.563-568) | present |
| 3. Business-model intelligence | l.570 | 6 bullets (l.571-576) | present |
| 4. Competition intelligence | l.578 | 3 bullets (l.579-581) | present |
| 5. Forward map | l.583 | Make-or-break line plus 8 catalysts (l.585-592). Each has a bull fork and a bear fork. 7 are dated; the MPCB item (l.586) is undated (STYLE S6) | present |

DELIVERABLE-COMPLETENESS: narrative present | sector present | business model present | competition present | forward map present. Gate PASS.

---

## 1. COVERAGE AUDIT

Fresh pass method: Grep over FT for note headers and numbered notes, forward-looking language ("on track", "expected to", "guidance", "target", "plans", "FY27E", "Medium-term", "underway", "raises", "reaffirm"), asterisk footnotes, auditor paragraphs, entity lists, and slide pages 20-43. I also re-mapped every P&L, balance sheet and cash flow table by hand against its filed subtotals.

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 7 | 7: SA Notes 1-3 (FT l.357-367), C Notes 1-4 (FT l.735-749) | none | PASS |
| Footnotes (unnumbered) | 14 rows (R1766-R1779) | 12 footnote definitions on 5 text lines (FT l.1137, l.1173, l.1201, l.1280, l.1470), plus marker lines and the "(Including Other Income)" label (FT l.1121). All map into R1766-R1779 | none | PASS |
| Disclaimers | 4 | 4 on p22 (FT l.928, l.947, l.952, l.953) | none | PASS |
| Line items | 205 | 205: SA P&L 24, SA BS 30, SA CF 38, C P&L 32, C BS 31, C CF 41, media table 9. The 10 BS section subtotals are header rows under A2's label method; their values sit in ST (for example R232-R233, R253-R254) and A4 ties them (RV l.16) | none | PASS |
| Zero-standing flags | 11 | 6 genuine. 5 flagged rows carry values: SA held-for-sale (FT l.257), C held-for-sale (FT l.618), C OCI reclassifiable (FT l.547), C CF net gain on financial assets (FT l.687), C CF FX on cash (FT l.728) | n/a | DIFF RESOLVED. A4 carries the correction (RV l.16); I re-verified each value by subtotal tie. Logged STYLE S9 |
| Agenda items | 3 | 3: item 1 (FT l.40-43), press release enclosure (FT l.45-46), presentation enclosure (FT l.48-49); times FT l.51 | none | PASS. Ledger ID pointers wrong (STYLE S5) |
| Auditor paragraphs | 13 | 13: SA 4 (FT l.100, l.106, l.114, l.125); C 7 numbered (FT l.390, l.398, l.407, l.424, l.429, l.441, l.454) plus 2 unnumbered (FT l.419, l.480) | none | PASS |
| Entities | 6 rows / 4 distinct | 6 / 4 (FT l.425-427; FT l.744-746) | none | PASS |
| Forward statements | 37 | 37 FORWARD rows confirmed. Grep also finds 3 verbatim restatements on p24 (FT l.970, l.973, l.974) with no FORWARD row. They duplicate R1399-R1401 (p18), and the lines carry NUMBER/DATE rows (R912-R914, R1525-R1528) | none | PASS (STYLE S8) |
| Slides | 24 | 24 (FT pages 20-43) | none | PASS |
| Slide numbers | 580 | 385 NUMBER (R908-R1292) + 195 DATE ties to LG l.14. Spot-check p25 (FT l.979-1004): 28 numeric and 20 period tokens = R915-R942, R1529-R1548 | none | PASS (spot-checked) |
| MISSING_FROM_STRUCTURED | 4 | 4 (FT l.77, l.495, l.751, l.1478). Spot-checks of digit lines on pp1-2, 4, 11, 18, 19, 34, 37, 40, 43 found rows for each | n/a | PASS |
| Turns / questions | 0 | 0 (results filing) | n/a | N/A |
| Structured IDs | 1,782 | 1,782 referenced; orphan_ids [] (LG l.18) | none | PASS |

Ledger-to-review check:
- A4 cites the notes by ID (RV l.66-79).
- A4 cites the flagged rows by ID or line: R1737-R1740, R1767-R1769, R1778, the R1394/R1425 variance (RV l.399) and R1426 (RV l.400).
- A4 marks the remaining rows reviewed at category level. Its counts equal the ledger (RV l.14-17: "Unreviewed ledger rows: none").
- I accept the category mark. Every uncited row without a flag is decorative or is a line item inside a table that ties: cover p20, contents p21, dividers p23/30/36/39, partnerships p34, CSR p41.
- Orphan rows: none. Rows found that the ledger lacks: none. STYLE S7 asks for an explicit row list.

---

## 2. ARITHMETIC AUDIT

Independent tie-outs:
- Every P&L column, standalone and consolidated, sums to its filed Total Expenses.
- The balance sheet subtotals tie. SA: non-current 1,757.90, current 1,469.87, total 3,227.77, liabilities 79.77 / 306.43. C: 1,760.62, 1,558.93, 3,319.55, 69.37 / 343.33.
- Cash flow A, B, C, net change and closing cash tie in both statements. C: 126.53 + 63.55 + 1.54 = 191.62. SA: 45.14 - 9.16 = 35.98.
- A4's tie-out claim (RV l.16) holds.

| Metric | A4 value (RV line) | Recomputed | Source line (FT) | Status |
|---|---|---|---|---|
| C Op EBITDA Q2 FY27 / margin | 169.47 / 24.37% (l.126-127) | 173.06 + 13.05 + 2.89 - 19.53 = 169.47; / 695.53 = 24.366% | l.509-510, l.523, l.525, l.532 | PASS |
| C Op EBITDA Q2 FY26 / Q1 FY27 | 119.44 / 20.97%; 172.00 / 27.17% | 119.44 / 20.966%; 172.00 / 27.169% | l.509-532 | PASS |
| C Op EBITDA H1 FY27 / H1 FY26 / FY26 | 341.47 / 25.70%; 229.01 / 21.51%; 434.71 / 20.50% | 341.47 / 25.701%; 229.01 / 21.510%; 434.71 / 20.504% | l.509-532 | PASS |
| C Reported EBITDA Q2 FY27 / Q2 FY26 / H1 FY27 | 188.99 / 27.17%; 133.30 / 23.40%; 380.72 / 28.66% | same; 27.172%, 23.399%, 28.656% | l.523-532 | PASS |
| C ETR Q2 FY27 / Q2 FY26 / H1 FY27 / FY26 | 25.21% / 24.22% / 25.01% / 24.20% | 25.205% / 24.221% / 25.014% / 24.201% | l.532, l.539 | PASS |
| C OI/PBT, PAT margin, by-nature gross margin (all 6 periods) | l.131-134 | All within 0.01 pp (e.g. GM Q2 FY27 380.39 / 695.53 = 54.691%) | l.509-541 | PASS |
| C H1 FY26 change in inventories | (12.60) (l.109) | 861.20 - 873.80 = (12.60) | l.518, l.530 | PASS |
| SA Op EBITDA Q2 FY27 / Q1 / Q2 FY26 / H1 FY27 | 144.16 / 22.73%; 166.16 / 28.45%; 100.84 / 19.70%; 310.32 / 25.47% | same; 22.735%, 28.445%, 19.702%, 25.473% | l.170-202 | PASS |
| SA ETR Q2 FY27 | 20.76% (l.167) | 36.64 / 176.51 = 20.758% | l.193, l.200 | PASS |
| SA H1 FY26 displaced column | 133.00 (l.138) | 790.39 - 448.04 - 2.56 - 20.81 - 185.98 = 133.00 = -10.27 + 64.84 + 78.43 | l.179-191 | PASS |
| PAT gap (C - SA)/SA | -14.35 / +4.80 / -7.46 / -3.79 / -1.64 / +1.05% (l.173) | -14.354 / +4.795 / -7.457 / -3.788 / -1.636 / +1.046% | l.202, l.541 | PASS |
| Op EBITDA C - SA | 18.60 / 5.84 / 25.31 / 31.57 / 31.15 / 47.59 (l.174) | same | derived | PASS |
| Intra-group revenue eliminated | 225.19 (35.5%); 218.53 (37.4%); 443.72 (36.4%) (l.176-177) | same | l.170, l.443, l.509 | PASS arithmetic; upper-bound qualifier MISSING (M3) |
| Subsidiary PAT Q1 FY27; share of C PAT | 10.06; 31.3% Q2, 19.3% H1 (l.73, l.178) | 50.61 - 40.55 = 10.06; 31.33%; 19.31% | l.444, l.541 | PASS |
| C YoY: revenue / Op EBITDA / margin / core PBT / PBT / PAT / EPS | +22.09% / +41.89% / +340 bps / +44.12% / +43.75% / +41.88% / +41.86% (l.191-201) | +22.089% / +41.887% / +340.0 bps / +44.12% / +43.75% / +41.88% / +41.86% | l.509-577 | PASS |
| C QoQ: op margin / reported margin / core PBT / revenue | -280 bps / -311 bps / -2.05% / +9.86% (l.220-221, l.246) | -280.3 / -311.2 bps / -2.048% / +9.865% | l.509-532 | PASS |
| SA YoY set | l.206-216 | All tie (e.g. EBIT 131.44 vs 90.33 = +45.51%) | l.170-220 | PASS |
| PAT bridge Q2 YoY | 26.38 + 23.65 - 2.24 - 0.79 + 5.67 - 12.76 - 1.70 = 38.21 (l.264-273) | 26.384, 23.647, 12.757, 1.703; sum 38.21 | derived | PASS |
| QoQ bridge | Op EBITDA -2.53 ... PAT -3.21 (l.275) | same | derived | PASS |
| OI-revert / OI-stripped PAT and EPS | 125.20 / Rs 215.56; 114.83 / Rs 197.71 (l.279) | 167.39 x 0.74795 = 125.20; 500.80 / 2.3232 = 215.56; 114.83; 197.71 | derived | PASS |
| Guidance arithmetic | H2 need 1,171.39 (+10.99% on 1,055.43); >20% -> 2,544.13; midpoint H2 EBITDA 294.28 / 25.12% (l.219, l.253) | same | l.1108, l.1114, l.1118 | PASS |
| 8C bull threshold | 22.3% (l.454) | 25.12% - 19.53 / 695.53 (2.81%) = 22.31% | l.510 | PASS |
| Q1 FY26 derived; H2 FY26 ex-OI; Q4 FY26 lower bound | 494.99 / 22.14%; 19.49%; 20.0% (l.240-244) | 494.99 / 22.136%; 205.70 / 1,055.43 = 19.490%; (157 - 37.60) / 597 = 20.0% | l.510-532, l.1021-1022 | PASS |
| CFO/PAT C / SA | 0.75x vs 0.94x; 0.36x vs 0.79x (l.295, l.313) | 0.745 / 0.936; 0.355 / 0.793 | l.709, l.328-333 | PASS arithmetic; classification CONTRADICTION (C1) |
| WC change C / SA | (95.87) vs (39.84); (170.58) vs (29.82) (l.298, l.316) | same, from the CF line items | l.692-704, l.316-328 | PASS |
| FCF C / SA | 168.27 vs 76.21; 67.64 vs 57.21 | same | l.709-711, l.328-336 | PASS |
| Days C (rec / inv / pay / CCC) | 9.83 / 63.32 / 25.44 / 47.71 vs 9.14 / 67.01 / 31.13 / 45.02 | 9.830 / 63.322 / 25.440 / 47.71; 9.138 / 67.014 / 31.132 / 45.02 | l.609-622, l.642-645 | PASS |
| Days SA | 39.34 / 56.77 / 27.66 / 68.45 vs 36.41 / 54.16 / 33.90 / 56.67 | same | l.247-252, l.279-280 | PASS |
| Net cash C / SA | 920.21 vs 757.93; 767.58 vs 680.05 | 191.62 + 29.45 + 711.75 - 12.61; 126.53 + 28.87 + 618.19 - 15.66; SA same method | l.611-622, l.634-642 | PASS |
| "933 liquidity" | 191.62 + 29.45 + 711.75 (l.325) | 932.82 | l.813, l.1155 | PASS |
| ROCE unadjusted / adjusted | FY26 17.01%; H1 ann 24.31% (avg CE 25.39%); Q2 ann 24.11%; adj 23.82% / 32.93% (l.370) | 454.42 / 2,671.82 = 17.008%; 709.72 / 2,919.46 = 24.310%; / 2,795.64 = 25.387%; 703.80 / 2,919.46 = 24.107%; 23.819%; 32.927% | l.523, l.532, l.629, l.634-640 | PASS ("matching" deck: STYLE S2) |
| EPS bases | 222.84 / 225.62 / 183.40 (TTM PAT 426.07) / 228.40; +24.5% (l.419) | same | l.541, l.576-577 | PASS |
| PE and CMP gaps | 29.5x / 36.3x; +93.8%; +16.8% (l.431, l.442) | 6,660 / 225.62 = 29.52; / 183.40 = 36.31; 6,660 / 3,437 = 1.938; 6,660 / 5,700 = 1.168 | Notion CMP taken as given | PASS |
| 6A pro-rata and seasonality | 1,166 / 1,229.5 / 1,251; 50.2% / 51.5% (l.359-362) | same; 1,064.68 / 2,120.11 = 50.22%; 174.25 / 338.23 = 51.52% | l.509-541 | PASS |
| H1 C other income composition | MF 23.22 = 59%; interest 3.05; "remainder 12.97 ND by type" (l.224) | 39.25 - 23.22 - 3.05 = **12.98**. Dividend income 0.13 (C CF) is a known type, so the true ND remainder is **12.85** | l.510, l.675, l.681, l.687 | FAIL (F2, at rounding scale) |
| SA ex-OI margin QoQ | -572 bps (l.505, l.658) | 22.735% - 28.445% = -571 bps (unrounded) | l.170-193 | Rounding only (STYLE S1) |
| Subsidiary inventory at group cost | 100.26 -> 82.01, -18.25 (l.180, l.468) | 389.25 - 288.99; 460.99 - 378.98 | l.247, l.609 | PASS |
| Subsidiary cash; intra-group receivables floor | 155.64; at least 191.03 (l.317, l.329) | 191.62 - 35.98; 262.59 - 71.56 | l.250-252, l.612-614 | PASS |
| Gross margin swing; EBITDA bridge mapping | -518 / +211 bps; 189.0 and H1 380.7 (l.226) | -517.8 / +211.2 bps; bridge sums tie; S&M +16.5 is inside the 17.57 other-expense rise | l.516-526, l.1010-1029 | PASS |
| SA ex-dividend tax (F8) | 37.37 vs 36.64 (l.281) | (176.51 - 28.04) x 25.168% = 37.37 | l.193, l.307 | PASS |

Arithmetic mismatches above rounding: 1. The OI remainder (F2) is off by 0.01, plus an unbucketed known type of 0.13. No other derived metric differs.

---

## 3. ADVERSARIAL READ

### Claim 1 (most positive): "Revenue +22.09% YoY and op EBITDA +41.89%: Strong. H1 +24.79% lands above Bull on H1 pro-rata. Watchlist item 3 GREEN." (RV l.191-201, l.219, l.362, l.377, l.548)
Strongest bear counter, from the same extract: the YoY base is a tariff-hit quarter, and the review never sizes that effect.
- The deck chart (FT l.1010 revenue labels, l.1015-1017 axis, l.1021-1022 margin and EBITDA labels) re-pairs FY25 as Q1 475, Q2 621, Q3 466, Q4 548.
- Pairing checks [DERIVED]: the sum is 2,110 vs filed FY25 2,109 (FT l.1116, l.1412). 621 x 24.2% = 150.3 vs the EBITDA label 150. 475 x 27.4% = 130.2 vs the label 130. A4 itself uses Q2 FY25 = 621 (RV l.238).
- Q2 FY26 (569.69) was 8.3% below Q2 FY25 (621).
- Q2 FY27 695.53 vs Q2 FY25 621 = +12.0% over two years, which is 5.8% a year [sqrt(1.1200)].
- H1 FY27 1,328.61 vs H1 FY25 1,096 (475 + 621) = +21.2% over two years, which is 10.1% a year.
- Both two-year rates sit below the Notion base of 16% CAGR (RV l.219).
- The deck computes growth on reported INR (FT l.953) for a business that exported 75% of FY26 sales (FT l.1199). Constant-currency growth: ND.
- Margins survive the counter. Reported Q2 EBITDA went from 150 (24.2%) to 188.99 (27.17%), +26.0% and about +300 bps over two years.

Survives? YES, for revenue pace. A4 names the base effect in one clause (RV l.219) but never sizes it. The Step 3 table starts at Q3 FY25 (RV l.238). Graft the two-year figures into Step 2 answer 1, the 6B item 3 reading and the brief narrative. Type MISSING. Loop A4.

### Claim 2: "FCF 168.27 strong. Net cash 920.21 above the 820 base. The working-capital build leans growth-induced. Capital advances +22.70 build ahead of TPU/SCF and carry the TPU spend gap." (RV l.297-306, l.329-331, l.398, l.466, l.556, l.576)
Strongest bear counter, from the same extract: the 22.70 that A4 calls capital advances sits inside operating cash flow.
- Consolidated: the rise in other current assets of 13.10 (91.67 - 78.57, FT l.619-620) plus the rise in other non-current assets of 22.70 (50.67 - 27.97, FT l.606) = 35.80. That equals the CF "Other assets" outflow (FT l.697).
- Standalone: 4.77 (49.40 - 44.63, FT l.258) + 22.70 (FT l.244) = 27.47. That equals the SA CF "Other assets" outflow (FT l.321).
- These are two exact ties. A4 counts the 35.80 and the 27.47 as operating working capital (RV l.298, l.316). The same table calls the 22.70 capital advances (RV l.305). Both cannot hold.
- Reading A (they are capital advances): CFO carries capex. H1 capex is then 49.77 C / 49.76 SA, not 27.07 / 27.06. CFO/PAT without the advances is 0.83x C (218.04 / 262.09) and 0.44x SA (117.40 / 266.45). FCF does not change. On this reading the 0.75x Pillar 2 reading (RV l.295, l.328) understates conversion. It also sits above the 0.65-0.80 band A4 cites. The "TPU spend behind" bear reading (RV l.330) weakens.
- Reading B (they are not capital advances): no filed line supports "Advances building ahead of TPU/SCF" (RV l.305, l.398) or the bull answer "advances 50.67 explain the gap" (RV l.466). The TPU gap stands at CWIP 37.24 plus H1 capex 27.07 against 118. A further 22.70 of unexplained non-current asset build sits in operating WC, which weakens the growth-induced lean (RV l.329).
- Secondary point: 21.28 of the 162.28 rise in net cash is mutual-fund fair-value gain, not cash generated [DERIVED: current investments +93.56 (711.75 - 618.19, FT l.611-612) less net MF purchase 72.28 (FT l.716)]. "Net cash above base" (RV l.331, l.366) carries a market-linked part.

Survives? YES. Type CONTRADICTION: the same 22.70 sits in two incompatible cells. Loop A4. A4 must pick one reading, state the other, and name the separating observation: the FY27 AR note on other non-current assets, or a management answer added to Q3.

### Claim 3: "Profit did not simply move from parent to subsidiaries. Over H1 the subsidiaries-plus-eliminations contribution was flat YoY (31.15 vs 31.57). The neutral reading is intra-group timing: subsidiary-held inventory at group cost fell from 100.26 to 82.01, which releases eliminated profit into consolidated Q2." (RV l.180, l.468, l.575, analyst note l.670)
Strongest bear counter, from the same extract: at PAT level, consolidation took profit out. Entity PATs less consolidated PAT [DERIVED]:
- Q2: SA 139.87 (FT l.202) + two subsidiaries 40.55 (FT l.444) - third subsidiary 0.10 (FT l.457) - C 129.44 (FT l.541) = 50.88 deducted.
- Q1: 126.58 + 10.06 - 0.28 - 132.65 = 3.71 deducted.
- H1: 266.45 + 50.61 - 0.38 - 262.09 = 54.59 deducted.
- The parent's intra-group dividend explains 27.91 to 28.04 of the H1 total (SA dividend 28.04 at FT l.307 vs C 0.13 at FT l.681). The other 26.55 to 26.68 is a net deduction.
- A4 infers that the dividend fell in Q2 (RV l.84). Other income supports that: C OI minus SA OI is -27.11 in Q2 and +3.72 in Q1 (FT l.171, l.510). On that basis Q2 carried about 22.84 to 22.97 of non-dividend deductions, against 3.71 in Q1.
- A release of eliminated profit would push the other way.
- The inventory figures A4 uses are 31-Mar and 30-Sep balances (FT l.247, l.609). They cannot place a release in Q2.
- The numbers fit A4's reading (a). Unrealised profit in subsidiary stock rose by about 26.6 while that stock at group cost fell 18.25, which implies a higher transfer markup.
- Reading (b) holds only if the subsidiaries' 50.61 PAT carries an undisclosed intra-subsidiary dividend of about that size, for example from the step-down Global Hi-Tech Films Inc. (FT l.744-746).

Survives? YES. Graft into the 1-G read (RV l.180), Q5 (RV l.468), the brief (RV l.575) and the A4 analyst note. Transfer pricing stays a question, but the evidence now leans to reading (a). Type MISSING. Loop A4.

### Mandatory acquisition-economics probe
Scan result: the extract has no acquisition of a business, no third-party stake buy and no purchase consideration. Items tested:
- Investment in subsidiary 0.52 in H1 (SA CF, FT l.335; nil in H1 FY26). This is intra-group capital into a wholly owned entity. Suppose it went to the nil-revenue subsidiary (H1 loss 0.38, total assets 0.18, FT l.455-458). Then price / target PAT is undefined (negative earnings) and price / assets is about 2.9x [0.52 / 0.18]. This is not a cheap-asset case. A4 already asks about it (Q12, RV l.475). No new counter.
- Lubrizol: an MoU with no consideration (FT l.830-833). There is no multiple to compute.
- TPU line: organic capex of Rs 118 Cr (FT l.1057) with a claimed 150-200 bps consolidated margin uplift (FT l.1065). On the FY27 revenue target of Rs 2,500 Cr (FT l.1108), that is Rs 37.5-50 Cr of EBITDA a year, a 2.4-3.1 year pre-tax payback [DERIVED]. The line supplies 360 LSF p.a. (FT l.1213) into a 600 LSF PPF base (FT l.1166), and the deck gives no cost bridge. A4 already classes the uplift as a bull input, not base (RV l.420). No new counter.

---

## FINDINGS (tagged)

| ID | Type | Agent | Exact gap | Fix |
|---|---|---|---|---|
| C1 | CONTRADICTION | A4 | 22.70 rise in other non-current assets is labelled capital advances (RV l.305, l.330, l.398, l.466) and also counted in operating "Other assets" (C 13.10 + 22.70 = 35.80, FT l.697; SA 4.77 + 22.70 = 27.47, FT l.321) | Pick a reading. If advances: restate H1 capex to 49.77 and add CFO/PAT without advances (0.83x C, 0.44x SA) beside the filed 0.75x / 0.36x in Step 5, the Step 7 Pillar 2 row, and brief l.555 and l.576. If not: drop the advances label and the TPU bull reading built on it. Name the separating observation either way |
| M1 | MISSING | A4 | Tariff-base effect named but not sized. Two-year Q2 revenue +12.0% (5.8% a year) and H1 +21.2% (10.1% a year) vs the 16% base CAGR are absent (RV l.219, l.238, l.377, l.548) | Add the two-year figures and the FY25 quarter re-pairing (FT l.1010, l.1021-1022, l.1116) to Step 2 answer 1, Step 3, the 6B item 3 reading and the brief narrative. Note that the margin climb survives (+300 bps over two years) |
| M2 | MISSING | A4 | PAT-level consolidation deductions are absent: Q2 50.88, Q1 3.71, H1 54.59, of which about 26.6 lies beyond the 28.04 intra-group dividend. Reading (b) asserts a Q2 release that the PAT arithmetic and the H1-only inventory dates do not support (RV l.180, l.468, l.575, l.670) | Add the bridge (FT l.202, l.307, l.444, l.457, l.541, l.681) to the 1-G read. State that reading (b) needs an undisclosed intra-subsidiary dividend of about 26.6. Add that sub-question to Q5 |
| M3 | MISSING | A4 | "Intra-group sales were 35.5% of the parent's Q2 sales" (RV l.376, l.464, l.572) drops the upper-bound qualifier. 225.19 = SA + two subsidiaries' "total revenues" (FT l.443) - C. It includes any sale between the two subsidiaries and any subsidiary other income | Restate as "intra-group revenue eliminated 225.19 (35.5% of parent revenue); parent-to-subsidiary sales are at most this" in 6B item 2, Q1 and the brief |
| F1 | FACTUAL | A4 | "ESG slide claims ZLD" (RV l.81, l.471, l.503, l.656). The slide says "Zero Liquid Discharge initiatives" and "100% water recycling through advanced treatment processes" (FT l.1369-1372) | Quote the slide text exactly. The transparency point survives on the 100% water-recycling claim |
| F2 | FACTUAL | A4 | H1 C other income remainder stated as 12.97, "ND by type" (RV l.224). The correct figure is 39.25 - 23.22 - 3.05 = 12.98, and dividend income 0.13 (FT l.681) is a known type | Write: remainder 12.98, of which dividend 0.13, ND 12.85. The 59% MF share is unchanged |

---

## VERDICT
INCOMPLETE. Failing agent: A4. All six non-STYLE findings belong to A4 (1 CONTRADICTION, 3 MISSING, 2 FACTUAL). No A2 or A3 loop: coverage holds with no orphan rows and nothing missing from the ledger. Exact gaps: C1, M1, M2, M3, F1, F2 in the table above. The Plain-Language Brief gate passes. After A4 grafts the three surviving counters and fixes F1-F2, the review can go to save.

## STYLE NOTES (logged, no re-run)
- S1. SA ex-OI QoQ change shown as -572 bps (RV l.505, l.658). Unrounded it is -571 bps (22.735% - 28.445%). The gap is rounding only.
- S2. "matching the deck's 23% and 32%" (RV l.370). The recomputed figures are 23.82% and 32.93%. Say "close to", and note that the deck basis is ND.
- S3. "Q2 FY27 (25.31) sits near Q2 FY26 (18.60)" (RV l.180). It is 36% higher. Say so.
- S4. The brief (RV l.575) says "subsidiaries' share". The metric is subsidiaries plus eliminations, as labelled at RV l.174.
- S5. A2 ledger agenda rows point to the wrong IDs. R1297 is the SEBI entity (ST l.1309) and R1347 is the exchange codes (ST l.1359), not the enclosures (FT l.45-49). The row content is correct.
- S6. The forward-map MPCB catalyst (RV l.586) is undated. The protocol asks for dated catalysts. Use "next Reg 30 update or Q3 call" with a date bound.
- S7. A4 coverage relies on a category-level "reviewed" mark (RV l.14-17). Next time, list the uncited rows by ID as "reviewed, no finding".
- S8. The p24 restatements of R1399-R1401 (FT l.970, l.973-974) have no FORWARD rows in ST. They are verbatim duplicates of p18, so no information is lost.
- S9. The A2 zero-standing count of 11 is stale. Five of the rows carry values (see the coverage table). A4 already carries the correction (RV l.16), so no number in the audited review changes. The true zero-standing count is 6.

---

```yaml
stage: A5-adversary
company: "GRWRHITECH"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "H1 FY27 consolidated other income remainder after MF gain and interest", a4_value: "12.97, ND by type (RV l.224)", recomputed: "12.98 (39.25 - 23.22 - 3.05); ND 12.85 after dividend income 0.13", source_line: "FT l.510, l.675, l.681, l.687"}
surviving_bear_counters:
  - {claim: "Revenue +22.09% YoY, H1 +24.79%, above Bull on H1 pro-rata, item 3 GREEN (RV l.191, l.362, l.377)", counter: "Tariff-hit base: Q2 FY26 was 8.3% below Q2 FY25 621; two-year Q2 revenue +12.0% (5.8% a year), H1 +21.2% (10.1% a year), below the 16% base CAGR; margin climb (+300 bps over two years) survives", source_line: "FT l.1010, l.1015-1017, l.1021-1022, l.1116; RV l.219, l.238", type: MISSING}
  - {claim: "FCF strong, net cash above base, WC growth-induced, capital advances +22.70 carry the TPU gap (RV l.298-306, l.329-331, l.466)", counter: "The 22.70 sits inside operating Other assets (C 13.10 + 22.70 = 35.80; SA 4.77 + 22.70 = 27.47): either capex is 49.77 and CFO/PAT without advances is 0.83x C / 0.44x SA, or the advances label and TPU bull reading lack support; 21.28 of the net-cash rise is MF fair-value gain", source_line: "FT l.244, l.258, l.321, l.606, l.611-612, l.619-620, l.697, l.716; RV l.298, l.305, l.316", type: CONTRADICTION}
  - {claim: "Subsidiaries-plus-eliminations flat over H1; neutral reading releases eliminated profit into Q2 (RV l.180)", counter: "PAT-level consolidation deductions Q2 50.88, Q1 3.71, H1 54.59; about 26.6 beyond the 28.04 intra-group dividend; sign opposite to a release; fits a higher transfer markup unless an undisclosed intra-subsidiary dividend exists", source_line: "FT l.202, l.307, l.444, l.457, l.541, l.681; RV l.180", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): 'ESG slide claims ZLD' (RV l.81, l.471, l.503); slide says 'Zero Liquid Discharge initiatives' and '100% water recycling' (FT l.1369-1372)"
    - "F2 (A4): H1 C OI remainder 12.97 should be 12.98; dividend 0.13 (FT l.681) is a known type, ND 12.85 (RV l.224)"
  missing:
    - "M1 (A4): two-year base effect unsized: Q2 +12.0% (5.8% a year), H1 +21.2% (10.1% a year) vs 16% base (RV l.219, l.377, l.548)"
    - "M2 (A4): PAT-level consolidation deductions (Q2 50.88, Q1 3.71, H1 54.59; about 26.6 beyond dividend) absent; reading (b) release unsupported (RV l.180, l.468, l.575)"
    - "M3 (A4): 225.19 / 35.5% stated as parent's intra-group sales without upper-bound qualifier (RV l.376, l.464, l.572)"
  contradiction:
    - "C1 (A4): 22.70 other non-current asset rise labelled capital advances (RV l.305) and counted in operating Other assets 35.80 / 27.47 (RV l.298, l.316; FT l.697, l.321)"
  style:
    - "S1: SA ex-OI QoQ -572 bps vs -571 unrounded (RV l.505)"
    - "S2: 'matching' deck ROCE 23%/32% vs recomputed 23.82%/32.93% (RV l.370)"
    - "S3: 25.31 'near' 18.60 is 36% higher (RV l.180)"
    - "S4: brief 'subsidiaries' share' should read subsidiaries plus eliminations (RV l.575)"
    - "S5: A2 agenda rows cite R1297/R1347, which are SEBI and exchange-code entities (ST l.1309, l.1359)"
    - "S6: forward-map MPCB catalyst undated (RV l.586)"
    - "S7: A4 coverage uses category-level reviewed mark; list uncited rows by ID next time (RV l.14-17)"
    - "S8: p24 forward restatements (FT l.970, l.973-974) lack FORWARD rows; verbatim duplicates of R1399-R1401"
    - "S9: A2 zero_standing 11 is stale (6 genuine); correction already in A4 (RV l.16)"
loop_back_to: "A4"
gap: "C1: resolve the 22.70 other non-current assets: capital advances inside operating Other assets (C 35.80, SA 27.47) -> restate H1 capex 49.77 and CFO/PAT without advances 0.83x C / 0.44x SA, or drop the advances label and TPU bull reading. M1: size the tariff-base effect (Q2 two-year +12.0%, 5.8% a year; H1 +21.2%, 10.1% a year vs 16% base) in Step 2 ans 1, Step 3, 6B item 3, brief. M2: add PAT-level consolidation deductions (Q2 50.88, Q1 3.71, H1 54.59; about 26.6 beyond the 28.04 dividend) to 1-G reading (b), Q5, brief. M3: mark 225.19 / 35.5% as an upper bound for parent-to-subsidiary sales. F1: quote 'Zero Liquid Discharge initiatives' (FT l.1369). F2: OI remainder 12.98, ND 12.85 after 0.13 dividend."
style_notes:
  - "S1: SA ex-OI QoQ -572 bps vs -571 unrounded (RV l.505)"
  - "S2: 'matching' deck ROCE 23%/32% vs recomputed 23.82%/32.93% (RV l.370)"
  - "S3: 25.31 'near' 18.60 is 36% higher (RV l.180)"
  - "S4: brief 'subsidiaries' share' should read subsidiaries plus eliminations (RV l.575)"
  - "S5: A2 agenda rows cite R1297/R1347, which are SEBI and exchange-code entities (ST l.1309, l.1359)"
  - "S6: forward-map MPCB catalyst undated (RV l.586)"
  - "S7: A4 coverage uses category-level reviewed mark; list uncited rows by ID next time (RV l.14-17)"
  - "S8: p24 forward restatements (FT l.970, l.973-974) lack FORWARD rows; verbatim duplicates of R1399-R1401"
  - "S9: A2 zero_standing 11 is stale (6 genuine); correction already in A4 (RV l.16)"
analyst_note: "All non-STYLE findings route to A4; no A2 or A3 loop. Coverage holds: counts match, all 1,782 IDs are referenced, and every P&L, BS and CF subtotal ties. The A2 zero-standing flag is stale on 5 rows, but A4 already carries the A3 correction, so it is logged STYLE. C1 is the most material: the 22.70 rise in other non-current assets ties exactly into the operating Other assets line in both statements. That either lifts conversion (0.83x group without advances, above the 0.65-0.80 band A4 cites) or removes the evidence for the TPU-advance reading. It touches Pillar 2 and the TPU tripwire, so it must be resolved before save. M2 shows net deductions at PAT level where A4's neutral reading assumes a release. Transfer pricing stays a question, but the evidence leans to the bear reading. M1 qualifies revenue only: the two-year margin climb of about 300 bps survives. The FY25 chart re-pairing checks against filed FY25 revenue of 2,109 and the EBITDA labels. Notion values and the MPCB Reg 30 fact are outside A5 inputs and were not audited."
```
