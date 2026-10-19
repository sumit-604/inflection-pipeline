# A5 ADVERSARY / COMPLETENESS AUDIT - Gallantt Ispat Limited (GALLANTT) - Q2 FY27

Auditor: A5 (claude-opus-5-5), fresh context. Date: 2026-10-20.
Inputs read: A4 review `runs/gallantt-q2fy27/work/review_gallantt_q2fy27.md` (645 lines); A1 fulltext `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-fulltext.md` (1,157 lines; statement transcription L1056-L1157; garbled duplicate layers p2-p5 and p7-p10 checked against it); A1 structured `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-structured.md` (R001-R449); A2 ledger `runs/gallantt-q2fy27/work/ledger_results_gallantt_q2fy27.md`.
Not read: the source PDF, anything under `inputs/`, and A3 forensics (re-derived independently).
Line references: "L" = fulltext line; "A4 L" = review line; "R" = structured row ID. Units are Rs lakhs unless marked Rs Cr (lakhs x 0.01).

---

## AUDIT 0 - DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business-model PRESENT | competition PRESENT | forward map PRESENT. Gate PASS.

| Brief part | Location | Content check | Status |
|---|---|---|---|
| (1) Summary narrative | A4 L505-L521 | 16 lines (within 10-20); numbers, cause, decision line | present |
| (2) Sector intelligence | A4 L523-L530 | demand, price-taker spread, bull/bear readings, separating observation | present (one FACTUAL claim at L526, see F1) |
| (3) Business-model intelligence | A4 L532-L542 | value chain, two plants (L85, L90), trading and treasury drift, bull/bear | present (attribution at L539 needs fixing, see M2) |
| (4) Competition intelligence | A4 L544-L552 | peers marked INFERENCE with no figures, win/weak points, bull/bear | present |
| (5) Forward map | A4 L554-L565 | make-or-break line plus 10 dated catalysts; every one carries a Bull and a Bear fork | present |

---

## AUDIT 1 - COVERAGE

Method: my own grep pass over the A1 fulltext (notes markers, numbered paragraphs, entity terms, statement rows L1057-L1155), then a check of the garbled text layers on p3 (L188-L281) and p4 (L296-L363) against the transcription for dropped lines. I found no line in the garbled layers that is missing from the transcription. I diffed the result against the A2 ledger. Then I checked that A4 cites or explicitly reviews each ledger row.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes, rows incl. restated | 15 | 15: CF notes L398, L400, L793, L794, L1156; P&L notes p6 L428, L435, L438, L448, L457; p11 L819, L828, L831, L840, L848 | none (A4 L16 cites all 15 IDs) | PASS |
| Notes, distinct | 7 | 7 (P&L Notes 1-5, CF Notes 1-2) | none | PASS |
| Statement lines | 96 | 96: P&L L1057-L1082 (26); BS L1084-L1118 (35); CF L1120-L1147 plus L1149-L1155 (35) | none | PASS |
| Statement cells | 296 | 296 (156 + 70 + 70) | none | PASS |
| Zero-standing cells | 27 | 27: L1069 x6, L1075 x4, L1078 x6, L1112 prior, L1116 prior, L1123 FY26, L1125 FY26, L1126 H1, L1142 H1, L1151 H1, subsidiary nil x4 (L1015-L1016) | none | PASS |
| Agenda items | 1 | 1 (L41) | none | PASS |
| Superseded garbled blocks | 8 | 8 (p2, p3, p4, p5, p7, p8, p9, p10 statement layers) | none | PASS |
| Auditor rows R399-R449 | 51 | 51 (standalone report L871-L946; consolidated report L949-L1054, incl. Reg 33(8) para L987, other-auditor para L1011, management assertion L1024, other matter L924 and L1028) | none | PASS |
| Consolidated entities | 1 | 1 (Suryalaxmi Technologies Pvt Ltd, L993); the associate line L1075 names no entity | none | PASS |
| Structured IDs vs ledger | 449 | 449 (ledger sections 14+10+13+8+40+15+296+28+9+16 = 449) | none | PASS |
| Turns / questions / slides | 0 | 0 (results-only filing) | none | PASS |

Missing from ledger: none. Missing from structured file: none.

Row-level coverage in A4: A4 L15-L17 states that it read all 449 rows and that no row is unreviewed. I accept this blanket as the explicit "reviewed" mark, so the formal orphan list is empty. A4 cites every A2-flagged row of substance except UDIN_DIFFERS (R418/R449) and MEETING_TIMES (R011). Both are benign: each review report carries its own UDIN in the valid 18-character format, and the 23:11 signature time fits an 11:00 PM close.

Material rows that A4 marks as reviewed but never cites. Each carries a fact that A4's text needs (see Audit 3):
- R260/R261 (L1098): other current financial assets, Rs 326.09 Cr at 30-Sep-2026 and Rs 306.95 Cr at 31-Mar-2026.
- R354 (L1144, FY26): loan outflow of (29,649.96), equal to the whole 31-Mar-2026 loan balance at L1097.
- R350 (L1142, FY26): PPE sale proceeds of Rs 110.30 Cr.
- R330 (L1132, FY26): a Rs 118.59 Cr inflow from current financial assets inside FY26 CFO.
- R356 (L1145, FY26): Rs 148.68 Cr placed in bank deposits of more than 3 months.
- R311 (L1123): fair value gain of Rs 0.65 Cr, the fourth line that went live in H1 (style note S4).

Cross-check note: on p2 the garbled OCI layer (L158-L164) sits on item 10, with dashes on A and B. The transcription puts the figures on line A (L1077) and a dash on B (L1078). The totals are the same, so no A4 figure changes.

---

## AUDIT 2 - ARITHMETIC (recomputed from L1057-L1155)

Statement re-foot: every P&L column foots: Total income, Total expenses, PBT, tax and PAT. The largest gap is 0.01 lakhs (Q2 FY26 and Q1 FY27 total expenses, Q1 FY27 PAT, FY26 PAT). Q1 plus Q2 equals H1 on every line, within 0.03 lakhs (PAT). Both balance-sheet dates foot (4,49,297.18; 4,26,961.76). Both cash flows foot through to closing cash (111.58; 10,165.48, 0.01 rounding on FY26).

| Metric | A4 value | Recomputed (lakhs basis) | Source line | Status |
|---|---|---|---|---|
| Step 1 Rs Cr conversions, all 26 P&L lines x 6 cols | as tabled A4 L85-L108 | each cell = lakh value x 0.01, rounded | L1057-L1082 | PASS |
| EPS on PAT after associate, Q2 FY26 / H1 FY26 | 3.69 / 10.89 | 8,892.62/2,412.809 = 3.686; 26,272.05/2,412.809 = 10.889 | L1076, L1081 | PASS |
| Filed EPS ties to PAT before associate (Q2 FY26 / H1 FY26) | 3.62 / 10.82 | 8,723.25/2,412.809 = 3.615; 26,102.68/2,412.809 = 10.818 | L1074, L1082 | PASS |
| Operating EBITDA Q2 FY26 / Q1 FY27 / Q2 FY27 | 13,154.15 / 18,509.28 / 10,969.41 | 10,300.75+3,266.63+908.42-1,321.65 = 13,154.15; 16,481.45+3,011.47+847.35-1,830.99 = 18,509.28; 8,317.37+3,550.62+916.66-1,815.24 = 10,969.41 | L1058, L1064, L1065, L1070 | PASS |
| Operating EBITDA H1 FY26 / H1 FY27 / FY26 | 37,838.91 / 29,478.68 / 71,644.38 | 37,838.91; 29,478.68; 71,644.38 | same | PASS |
| Op EBITDA margin (6 cols) | 12.99 / 16.16 / 9.57 / 17.68 / 12.86 / 16.21% | 12.989 / 16.156 / 9.573 / 17.677 / 12.864 / 16.213% | + L1057 | PASS |
| Reported EBITDA and margin (6 cols) | 144.76/203.40/127.85/398.43/331.25/776.04 Cr; 14.29/17.75/11.16/18.61/14.46/17.56% | 14,475.80/20,340.27/12,784.65/39,843.02/33,124.91/77,603.79; 14.294/17.754/11.157/18.614/14.455/17.562% | L1064, L1065, L1070, L1057 | PASS |
| Core PBT ex-OI (6 cols) | 89.79/146.50/65.02/299.34/211.53/544.44 Cr | 8,979.10/14,650.46/6,502.13/29,933.93/21,152.58/54,444.07 | L1058, L1070 | PASS |
| OI / PBT (6 cols) | 12.83/11.11/21.82/6.27/14.70/9.87% | 12.831/11.109/21.825/6.275/14.703/9.866% | L1058, L1070 | PASS |
| ETR (6 cols) | 15.31/24.97/27.25/18.27/25.73/19.83% | 15.314/24.966/27.248/18.271/25.731/19.828% | L1070, L1073 | PASS |
| PAT margin (6 cols) | 8.78/10.79/5.28/12.27/8.04/10.96% | 8.781/10.794/5.281/12.274/8.037/10.959% | L1057, L1076 | PASS |
| Material cost ratio (6 cols) | 74.55/72.65/79.00/71.34/75.82/72.21% | 75,498.96/83,229.90/90,526.63/152,700.98/173,756.53/319,099.84 over revenue = 74.548/72.648/79.001/71.338/75.825/72.212% | L1057, L1060-L1062 | PASS |
| Traded purchases / revenue (6 cols) | 0.50/0.77/8.63/1.05/4.70/0.90% | 0.504/0.767/8.628/1.052/4.698/0.900% | L1057, L1061 | PASS |
| Revenue YoY Q2 | +13.15% (+133.14 Cr) | 13,314.13/101,275.02 = +13.147% | L1057 | PASS |
| Op EBITDA YoY Q2 | -16.61% | -2,184.74/13,154.15 = -16.609% | derived | PASS |
| Op EBITDA margin YoY / QoQ | -342 bps / -659 bps | -341.6 bps / -658.3 bps (unrounded 16.1559% - 9.5728%) | derived | PASS (rounding; S1) |
| D&A YoY / QoQ; FC YoY | +8.69% / +17.90%; +0.91% | +8.694% / +17.903%; +0.907% | L1064, L1065 | PASS |
| EBIT operating YoY | 98.88 -> 74.19, -24.97% | 9,887.52 -> 7,418.79, -24.968% | derived | PASS |
| OI YoY | +37.35% | 493.59/1,321.65 = +37.346% | L1058 | PASS |
| Core PBT / PBT / PAT after / PAT before YoY | -27.59 / -19.25 / -31.95 / -30.63% | -27.586 / -19.255 / -31.954 / -30.633% | L1058, L1070, L1074, L1076 | PASS |
| EPS YoY filed / consistent | -30.66% / -31.98% | 2.51/3.62 = -30.663%; 2.51/3.69 = -31.978% | L1082 | PASS |
| Q1 FY26 derived revenue / Op EBITDA / margin / core PBT | 1,127.78 Cr / 24,684.76 / 21.89% / 209.55 Cr | 1,12,777.84 / 24,684.76 / 21.888% / 20,954.83 | H1 FY26 minus Q2 FY26 | PASS |
| Q1 FY26 gross margin | 31.54% | 1 - 77,202.02/1,12,777.84 = 31.5450% | derived | PASS (rounding; S3) |
| H2 FY26 per-quarter revenue / margin / core PBT / GM | 1,139.20 Cr / 14.84% / 122.55 Cr / 26.97% | 2,27,839.33/2; 33,805.47/2,27,839.33 = 14.837%; 24,510.14/2; 26.967% | FY26 minus H1 FY26 | PASS |
| H2 FY26 deferred tax | (2,360.19) | -3,830.43 - (-1,470.24) = -2,360.19 | L1072 | PASS |
| Traded purchases multiples | 11.25x QoQ; 19.38x YoY | 9,886.58/878.47 = 11.254; /510.26 = 19.376 | L1061 | PASS |
| Core PBT vs H1 average | 38.5% short | 6,502.13/10,576.29 = 0.6148 | derived | PASS |
| PAT bridge: revenue effect / GM effect | +3,388.65 / -5,102.19 | 13,314.13 x 25.4515% = 3,388.65; GP change -1,713.54 less 3,388.65 = -5,102.19 | L1057, L1060-L1062 | PASS |
| Bridge: staff / other exp / D&A / FC / OI / tax / associate | -805.84 / +334.63 / -283.99 / -8.24 / +493.59 / -688.80 / -169.37 | same | L1063-L1066, L1058, L1073, L1075 | PASS |
| Bridge tax split | +303.75 / -992.55 | 1,983.38 x 15.314% = 303.74; (27.248% - 15.314%) x 8,317.37 = 992.55 | L1070, L1073 | PASS |
| Bridge sum | -2,841.56 vs -2,841.55 | -2,841.56 (0.01 rounding) | L1076 | PASS |
| Current gross margin in bridge text | 20.9988% | 24,062.52/1,14,589.15 = 20.99895% | derived | PASS (rounding; S2) |
| Core vs non-core share of PAT fall | 87.2% / 12.8% | 2,476.97/2,841.55 = 87.17%; 364.58 = 12.83% | derived | PASS |
| OI-reverted PAT | 5,691.97; 227.68 Cr annualised | 7,823.78 x 72.752% = 5,691.98 | derived | PASS |
| FY26 deferred credit / PBT | 634 bps | 3,830.43/60,403.48 = 6.341% | L1070, L1072 | PASS |
| CFO / PAT FY26 / H1 FY27 | 1.24x / 0.49x | 60,226.48/48,426.70 = 1.244; 9,082.36/18,417.78 = 0.493 | L1140, L1076 | PASS (see M3 for basis) |
| CFO / Op EBITDA | 84.1% / 30.8% | 84.063% / 30.810% | L1140 | PASS |
| Capex; H1 share of FY26 | 348.15 / 278.47 Cr; 80.0% | 34,815.06 / 27,846.60; 79.98% | L1141 | PASS |
| FCF | 254.11 / (187.64) Cr | 25,411.42 / (18,764.24) | L1140, L1141 | PASS |
| WC change in CFO | +3.58 / (125.01) Cr | 72,878.03-72,519.72 = 358.31; 17,012.03-29,512.93 = (12,500.90); WC items re-summed both periods | L1127-L1138 | PASS |
| Receivable / inventory / payable days; CCC | 14.67/14.80; 63.00/70.42; 19.62/18.40; 58.05/66.82 | 14.668/14.796; 62.997/70.421; 19.617/18.398; 58.05/66.82 | L1092, L1094, L1112, L1113 | PASS |
| PPE / CWIP / intangibles change | -42.18 / +249.32 (+71.4%) / -13.70 Cr | -4,218.09 / +24,931.62 (+71.43%) / -1,369.83 | L1084-L1086 | PASS |
| Gross borrowings | 547.69 -> 591.97 Cr | 54,768.70 -> 59,197.39 | L1106, L1111 | PASS |
| Net debt (excl. loans) | 21.82 -> 165.86 Cr | 2,181.75 -> 16,586.13 | L1093, L1095, L1096, L1106, L1111 | PASS |
| Net debt with loans as liquid | (274.68) -> (99.92) Cr | 2,181.75-29,649.96; 16,586.13-26,578.46 | + L1097 | PASS |
| Gross D/E | 0.17x / 0.17x | 0.165 / 0.170 | L1105 | PASS |
| Other-equity roll-forward gap | 14.06 Cr | 3,07,495.39 + 18,436.30 - 3,24,526.04 = 1,405.65 | L1104, L1080 | PASS |
| Inventory build; RM/stores remainder | +21.41%; 71.24 Cr | 11,788.93/55,074.62 = 21.405%; 11,788.93-4,665.41 = 7,123.52 | L1092, L1062 | PASS |
| Tax paid vs charge | 79.30 vs 59.01; +20.29 Cr | 7,929.67-5,901.03 = 2,028.64 = 2,676.05-647.41 | L1139, L1071, L1099 | PASS |
| Capex tie | 24,931.62 + 1,895.56 + 974.17 + 45.25 = 27,846.60 | 974.17 = 6,562.09 - (4,218.09+1,369.83); residual 45.25 | L1084-L1086, L1090, L1141 | PASS |
| H1 funding | sources vs uses | sources 29,558.62 vs uses 29,557.95; gap 0.67 = investments +15.63 and deposits -16.30, which A4 leaves out (immaterial) | L1140-L1155 | PASS |
| ROCE H1 annualised / FY26 | 13.38% / 16.71% | 53,125.64/3,97,121.85 = 13.378%; 64,572.07/3,86,392.18 = 16.712% | L1070, L1064, L1105, L1106, L1111 | PASS |
| TTM revenue / Op EBITDA / margin / PAT / EPS | 4,569.95 / 632.84 Cr / 13.85% / 405.72 Cr / 16.82 | 4,56,995.19 / 63,284.15 / 13.848% / 40,572.43 / 16.815 | derived | PASS |
| Q2 annualised PAT / EPS | 242.04 Cr / 10.03 | 24,204.28; 10.032 | L1076 | PASS |
| S-vs-C proxy gap | 1.90% (1.94%) / 0.0002% / 0.0001% | 169.37/8,892.62 = 1.905%; /8,723.25 = 1.942%; 0.01/6,051.07; 0.01/18,417.78 | L1075, L1076, L1015 | PASS |
| Dividend outflow | 48.26 Cr | 2 x 2,412.809 = 4,825.62 | L457-L460, L1081 | PASS |
| Interest income / H1 PBT | 14.2% | 3,530.19/24,798.81 = 14.235% | L1122, L1070 | PASS |
| Statutory dates | 14-Feb-2027; 30-May-2027; 14-Aug-2027; ~21-Oct-2026; ~30-Oct-2026 | 45/60/45-day Reg 33; Reg 31 21 days; s.127 30 days | calendar | PASS |

Arithmetic mismatches above rounding: none.

---

## AUDIT 3 - ADVERSARIAL READ (three most positive claims)

A4 reads bearish. Its positive claims are few. The three that do the most to lift the reading are below. Each counter is built only from the extract.

### Claim 1 - Revenue grew 13.15% YoY to Rs 1,145.89 Cr (A4 L152, L166; brief L506-L507)
Bear counter:
- Traded purchases rose by 9,886.58 - 510.26 = 9,376.32 lakhs (Rs 93.76 Cr) YoY (L1061). That equals 70.4% of the Rs 133.14 Cr revenue rise (L1057).
- Proxy for own-made sales, revenue less traded purchases [INFERENCE: assumes traded goods resold in the quarter near cost; the stock-in-trade part of L1062 is not split out]: Q2 FY27 Rs 1,047.03 Cr vs Q2 FY26 Rs 1,007.65 Cr = +3.9% YoY. Against Q1 FY27 (Rs 1,136.88 Cr) it is -7.9% QoQ.
- The base was weak. Q2 FY26 revenue (Rs 1,012.75 Cr) sat 10.2% below derived Q1 FY26 (Rs 1,127.78 Cr). H1 FY27 grew 7.06% YoY (L1057). TTM revenue is up 3.42% on FY26.
- Survives? YES. A4 says traded purchases equal 8.63% of revenue (L152) and asks for own volume (Q3, L416). It never states that most of the YoY rise is matched by traded purchases, and it never gives the ex-traded trend. The summary calls the print "13.15% more than a year ago" with no qualifier. Tag: MISSING. Graft into Step 2 (revenue row and diagnostic 1) and summary narrative line 2.
- Suggested graft text: "Traded purchases rose Rs 93.76 Cr YoY (L1061). That equals 70.4% of the Rs 133.14 Cr revenue rise. Revenue less traded purchases was Rs 1,047.03 Cr: +3.9% YoY and -7.9% QoQ [INFERENCE: traded goods resold in the quarter near cost]. The base was weak: Q2 FY26 sat 10.2% below derived Q1 FY26. H1 FY27 revenue grew 7.06% YoY."

### Claim 2 - Low leverage: gross D/E 0.17x; net cash of Rs 99.92 Cr if the loans are recoverable; finance cost small (A4 L263-L264, L281)
Bear counter:
- The loan book is new. FY26 "Movement in loans and advances" is (29,649.96) (L1144, R354). That equals the whole 31-Mar-2026 Loans balance of 29,649.96 (L1097, R259), which fits a nil opening balance [computed; the 31-Mar-2025 balance sheet is not in the filing].
- In that same year the group drew Rs 170.02 Cr of borrowings (L1149), sold PPE for Rs 110.30 Cr (L1142, R350) and placed Rs 148.68 Cr in deposits of more than 3 months (L1145, R356). Only Rs 30.71 Cr of the loans came back in H1 FY27 (L1144). The tie holds: 29,649.96 - 3,071.49 = 26,578.47 against 26,578.46 at L1097.
- A second undisclosed pool is missing from A4. Other current financial assets are Rs 326.09 Cr (L1098, R260), up Rs 19.14 Cr in H1, and larger than the loan book. A4's liquidity table (L239-L266) leaves it out.
  - It holds accrued interest by tie: interest income 3,530.19 (L1122) less interest received 2,922.18 (L1146) = 608.01; add the CF increase of 1,306.38 (L1132) to get 1,914.39, which matches the balance-sheet rise of 1,914.38.
  - So A4's attribution of the treasury income to "Rs 401.66 Cr of bank balances and Rs 265.78 Cr of loans [FILED]" (A4 L171, L539) is not filed. It is inference, and it leaves out L1098.
- Loans plus other current financial assets = Rs 591.87 Cr = 17.0% of equity (L1105). The counterparties of both are undisclosed.
- Low gross D/E does not show liquidity. Cash is Rs 1.12 Cr and current borrowings are Rs 505.69 Cr. The Rs 48.26 Cr dividend falls due about 30-Oct-2026. FY26 dividend paid was Rs 9.40 Cr (L1151).
- Survives? YES. Tag: MISSING. Graft into the Step 5 table (new row for L1098; FY26 origination fact), the Q1 "why it matters" cell, brief L539 (re-tag as INFERENCE and name L1098), and flags 8 and 9.
- Suggested graft text: "The loan book was built in FY26. The FY26 loan outflow of Rs 296.50 Cr (L1144) equals the whole 31-Mar-2026 balance (L1097). In that year the group borrowed Rs 170.02 Cr (L1149) and sold PPE for Rs 110.30 Cr (L1142). H1 FY27 recovered Rs 30.71 Cr. Other current financial assets add Rs 326.09 Cr (L1098), nature not disclosed. The two pools total Rs 591.87 Cr, 17.0% of equity."

### Claim 3 - FY26 cash conversion of 1.24x is the healthy baseline (A4 L242, L278; seed checklist green bar L392; forward-map bull fork L563)
Bear counter:
- FY26 CFO of Rs 602.26 Cr (L1140) includes a Rs 118.59 Cr inflow from a decrease in current financial assets (L1132, R330). This is a non-trade line, not inventory, receivables or payables.
- Without it, FY26 CFO = Rs 483.68 Cr, CFO/PAT = 1.00x (48,367.88 / 48,426.70) and CFO/Op EBITDA = 67.5%.
- The 1.24x green bar in 8B and the bull fork "CFO/PAT returns near 1.24x" are set by a year whose conversion rested on that release.
- Survives? YES. Tag: MISSING. Graft into the Step 5 CFO/PAT row, 8B row 3 and the forward-map FY27 bullet: show 1.24x reported and 1.00x without the L1132 release.

### Mandatory acquisition-economics probe
N/A. The filing describes no acquisition, business purchase or stake buy. The year-ago associate share (L1075) is a perimeter exit with no consideration disclosed, so there is no purchase multiple to state. The subsidiary (L993, L1013) carries no purchase disclosure. "Purchase of stock in trade" (L1061) and "Purchase of fixed assets" (L1141) are operating and capex lines, not acquisitions.

### Additional FACTUAL finding from the read
F1 - The seasonality claim is not supported by the filing.
- What A4 says:
  - A4 L193: "both Q2 prints are the weakest of their year (12.99% in FY26, 9.57% in FY27)".
  - Brief L526: the same claim, tagged [FILED, computed].
  - Step 6.5 L354: "Q2 is the seasonal low in both years on record", used to point to a seasonal-name base.
- What the filing shows:
  - Q3 and Q4 FY26 are not filed apart. A4 says so itself at L179 and L197. The H2 FY26 average of 14.84% leaves room for one H2 quarter below 12.99%, if the other runs above about 16.7%.
  - FY27 has only two quarters.
  - Q2 FY26 (12.99%) is below Q1 FY26 (21.89%) and below the H2 FY26 average (14.84%). Q2 FY27 (9.57%) is below Q1 FY27 (16.16%). Nothing more.
- Why it matters: the claim reads as filed fact and props up the bull reading "Q2 was a seasonal trough" (L528). Tag: FACTUAL. Loop A4.
- Suggested fix text: "Q2 FY26 (12.99%) sits below Q1 FY26 (21.89%) and below the H2 FY26 quarterly average (14.84%). Q3 and Q4 FY26 are not split, and FY27 has two quarters. The filing does not show that Q2 is the seasonal low [INFERENCE only: monsoon dip]."

---

## FINDINGS BY TYPE

| ID | Type | Finding | Lines | Loop |
|---|---|---|---|---|
| F1 | FACTUAL | Seasonality "weakest of their year" claim is unsupported (Q3/Q4 FY26 not split; FY27 incomplete) and tagged as filed | A4 L193, L526, L354; L1057-L1076 | A4 |
| M1 | MISSING | Revenue-growth qualifier: traded purchases = 70.4% of YoY revenue rise; ex-traded proxy +3.9% YoY, -7.9% QoQ; weak base; H1 +7.06% | L1057, L1061 | A4 |
| M2 | MISSING | FY26 loan origination from nil alongside borrowing and a Rs 110.30 Cr asset sale; Rs 326.09 Cr other current financial assets missing from liquidity and from the interest attribution; Rs 591.87 Cr undisclosed = 17.0% of equity | L1097, L1098, L1105, L1122, L1132, L1142, L1144, L1145, L1146, L1149 | A4 |
| M3 | MISSING | FY26 CFO/PAT 1.24x includes a Rs 118.59 Cr current-financial-asset release; 1.00x without it; green bar and bull fork rest on it | L1132, L1140, L1076 | A4 |
| S1 | STYLE | QoQ margin -659 bps comes from rounded inputs; unrounded is -658 bps | A4 L154, L167 | none |
| S2 | STYLE | Bridge text gives current GM 20.9988%; unrounded 20.99895%. Bridge rows are correct | A4 L205 | none |
| S3 | STYLE | Q1 FY26 GM 31.54%; unrounded 31.5450% (31.55% on round-half-up) | A4 L183 | none |
| S4 | STYLE | A4 L60 says four lines went live in H1; Q12 (L425) names three. The fourth is the fair value gain on investment, Rs 0.65 Cr (L1123, R311) | A4 L60, L425 | none |
| S5 | STYLE | Symmetry (Rule J). CFO strips interest income (L1122) and books interest received in investing (L1146). With interest received added back, H1 FY27 CFO/PAT = 0.65x and FY26 = 1.33x. Show this as a second view; the classification stands | L1122, L1140, L1146 | none |
| S6 | STYLE | A2 analyst note says zero-standing 27 "incl 6 nil-subsidiary figures", but the ledger tags 4 (R434, R435, R438, R439). The total of 27 is correct | ledger L534 | none |

---

## VERDICT

VERDICT: INCOMPLETE. Loop back to A4. Finding types: 1 FACTUAL, 3 MISSING, 0 CONTRADICTION, 6 STYLE.
Gap: A4 must make four changes:
1. Graft the three surviving bear counters:
   - M1: the revenue-growth qualifier in Step 2 and summary line 2.
   - M2: FY26 loan origination, the L1098 Rs 326.09 Cr row and the corrected interest attribution, in the Step 5 table, Q1, brief L539 and flags 8 and 9.
   - M3: FY26 CFO/PAT without the release (1.00x), in the Step 5 CFO/PAT row, 8B row 3 and forward-map L563.
2. Correct F1, the seasonality claim at L193, L526 and L354.

No arithmetic mismatch, no coverage orphan and no missing ledger row. The A4 protocol verdict (PROCEED WITH FLAGS) is not challenged. The grafts make flags 8 and 9 sharper and change the 8B green bar.

## STYLE NOTES (logged, no re-run)
S1-S6 as tabled above.

```yaml
stage: A5-adversary
company: "GALLANTT"
quarter: "Q2 FY27"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Revenue Rs 1,145.89 Cr, +13.15% YoY (A4 L152, L166, brief L506-L507)", counter: "Traded purchases rose Rs 93.76 Cr YoY, 70.4% of the Rs 133.14 Cr revenue rise. Revenue less traded purchases Rs 1,047.03 Cr: +3.9% YoY vs Rs 1,007.65 Cr, -7.9% QoQ vs Rs 1,136.88 Cr [INFERENCE: traded goods resold in-quarter near cost]. Q2 FY26 base 10.2% below derived Q1 FY26; H1 FY27 YoY +7.06%; TTM vs FY26 +3.42%.", source_line: "L1057, L1061 (R072-R077, R096-R098)", type: MISSING}
  - {claim: "Low leverage: gross D/E 0.17x; net cash Rs 99.92 Cr if loans recoverable (A4 L263-L264, L281)", counter: "FY26 loan outflow (29,649.96) equals the whole 31-Mar-2026 loan balance, so the book was built in FY26, the year the group borrowed Rs 170.02 Cr and sold PPE for Rs 110.30 Cr; H1 FY27 recovered only Rs 30.71 Cr. Other current financial assets of Rs 326.09 Cr (+Rs 19.14 Cr in H1; holds accrued interest by tie) are absent from A4's liquidity table and interest attribution. Undisclosed loans plus other current financial assets = Rs 591.87 Cr = 17.0% of equity; cash Rs 1.12 Cr vs current borrowings Rs 505.69 Cr.", source_line: "L1097, L1098, L1105, L1111, L1122, L1132, L1142, L1144, L1146, L1149 (R258-R261, R330, R350, R353, R354)", type: MISSING}
  - {claim: "FY26 CFO/PAT 1.24x as healthy baseline and green bar (A4 L242, L392, L563)", counter: "FY26 CFO Rs 602.26 Cr includes a Rs 118.59 Cr inflow from a decrease in current financial assets; without it FY26 CFO = Rs 483.68 Cr, CFO/PAT 1.00x, CFO/Op EBITDA 67.5%.", source_line: "L1132, L1140, L1076 (R330, R346, R191)", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): A4 L193, brief L526 [FILED, computed] and Step 6.5 L354 claim Q2 is the weakest quarter / seasonal low in both years. Unsupported: Q3 and Q4 FY26 are not split (H2 average 14.84% allows one H2 quarter below 12.99%) and FY27 has two quarters. Filed evidence shows only Q2 FY26 12.99% < Q1 FY26 21.89% and < H2 FY26 avg 14.84%; Q2 FY27 9.57% < Q1 FY27 16.16%."
  missing:
    - "M1 (A4): Step 2 revenue row, diagnostic 1 and summary line 2 lack the qualifier that traded purchases (+Rs 93.76 Cr YoY, L1061) equal 70.4% of the Rs 133.14 Cr revenue rise (L1057); ex-traded proxy +3.9% YoY, -7.9% QoQ; weak Q2 FY26 base; H1 YoY +7.06%."
    - "M2 (A4): Step 5, Q1, brief L539 and flags 8-9 omit that the Rs 296.50 Cr loan book was originated in FY26 (L1144 FY26 = L1097 31-Mar balance) alongside Rs 170.02 Cr borrowing (L1149) and a Rs 110.30 Cr PPE sale (L1142), and omit Rs 326.09 Cr other current financial assets (L1098); brief L539 tags the interest-income attribution FILED when it is inference."
    - "M3 (A4): Step 5 CFO/PAT row, 8B row 3 and forward-map L563 use FY26 1.24x without noting the Rs 118.59 Cr current-financial-asset release in FY26 CFO (L1132); ex-release 1.00x."
  contradiction: []
  style:
    - "S1: QoQ op margin -659 bps from rounded inputs; unrounded -658 bps (A4 L154, L167)."
    - "S2: Bridge text current GM 20.9988%; unrounded 20.99895%; bridge rows correct (A4 L205)."
    - "S3: Q1 FY26 GM 31.54%; unrounded 31.5450% (A4 L183)."
    - "S4: A4 L60 says four lines went live; Q12 (L425) names three; add fair value gain on investment Rs 0.65 Cr (L1123, R311)."
    - "S5: Symmetry: CFO/PAT with interest received (L1146) added back is 0.65x H1 FY27 and 1.33x FY26; show as a second view, classification unchanged."
    - "S6: A2 analyst note says 6 nil-subsidiary zero-standing cells; ledger tags 4 (R434, R435, R438, R439); total 27 is correct."
loop_back_to: "A4"
gap: "A4 to graft three surviving bear counters and fix one factual claim: M1 revenue-growth traded-goods qualifier (Step 2, summary line 2); M2 FY26 loan origination from nil plus Rs 326.09 Cr other current financial assets (L1098) and the re-tagged interest attribution (Step 5, Q1, brief L539, flags 8-9); M3 FY26 CFO/PAT 1.00x ex Rs 118.59 Cr L1132 release (Step 5, 8B row 3, forward map L563); F1 replace the 'Q2 weakest of its year / seasonal low' claim at L193, L526, L354 with what the filing shows."
style_notes:
  - "S1: QoQ op margin -659 bps vs unrounded -658 bps."
  - "S2: current GM 20.9988% vs unrounded 20.99895%."
  - "S3: Q1 FY26 GM 31.54% vs unrounded 31.5450%."
  - "S4: name the fourth newly live line (fair value gain Rs 0.65 Cr, L1123) in Q12."
  - "S5: show interest-adjusted CFO/PAT (0.65x H1 FY27; 1.33x FY26) as a second view."
  - "S6: A2 analyst note miscounts nil-subsidiary cells (6 vs 4); total 27 correct."
analyst_note: "All 449 rows reconcile and my fresh counts match A2 in every category. Every A4 derived figure recomputes within rounding from L1057-L1155, so the loop is for content, not arithmetic. A4's blanket 'read all 449' meets formal coverage, but six uncited rows hold facts that change the reading. R354 shows the FY26 loan outflow equals the whole 31-Mar-2026 book. R350 shows a Rs 110.30 Cr FY26 asset sale. R330 shows a Rs 118.59 Cr release inside FY26 CFO. R260/R261 show a Rs 326.09 Cr undisclosed pool, larger than the loans. A4 can graft all of this without an A3 re-run, because the cells are already in its inputs. I did not read A3, so whether A3 saw these rows is unchecked. F1 is the only FACTUAL finding. The seasonality line reads as filed fact but rests on Q3/Q4 FY26, which the filing does not split. The filing has no acquisition, so the acquisition probe is N/A. The PROCEED WITH FLAGS verdict stands. The grafts sharpen flags 8-9 and lower the 8B green bar."
```
