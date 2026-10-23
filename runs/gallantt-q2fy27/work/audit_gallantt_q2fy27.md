# A5 ADVERSARY AUDIT - Gallantt Ispat Limited (GALLANTT) - Q2 FY27 merged review (results + resultsrev + presentation + concall)

Auditor: A5, claude-opus-5-5, fresh context. Run date 23-Oct-2026.
Under audit: work/review_gallantt_q2fy27.md (A4, 1,260 lines).
Read: the four A1 fulltexts, the four A1 structured files, the four A2 ledgers, the A4 review.
Not opened: source PDFs, audio, anything under inputs/, the A3 forensics, prior audits, the results-only review.

Anchor key:
- rev Lnnn = A4 review line.
- R:Lnnnn = original results fulltext. RR:Lnnnn = revised results fulltext. P:pN lL = presentation fulltext page and line. P:Rnnnn = presentation structured row. C:lN = concall fulltext line (ASR text).
- led-res / led-rr / led-pres / led-cc Lnnn = A2 ledger lines (results, resultsrev, presentation, concall).
- st-rr / st-pres / st-cc Lnnn = A1 structured file lines.
- Rs Cr unless stated. Filed lakhs x 0.01.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PLAIN-LANGUAGE BRIEF at rev L1072-L1140. All five parts present and non-empty:
- (1) Summary narrative: PRESENT. rev L1076-L1092, 16 lines (inside the 10-20 band). Real content: revenue, own volume, trading, core PBT, PAT, cash, net-cash claim, capacity, promoter stake, late filing, decision.
- (2) Sector intelligence: PRESENT. rev L1094-L1103. Demand, price, cost, bull, bear, separating observation.
- (3) Business-model intelligence: PRESENT. rev L1105-L1116. Chain, spread, three drifts, bull, bear, separating observation.
- (4) Competition intelligence: PRESENT. rev L1118-L1127. Peers tagged INFERENCE, win and weak points, bull, bear, separating observation.
- (5) Forward map: PRESENT. rev L1129-L1140. One make-or-break line and ten dated catalysts. Each carries a bull fork and a bear fork.

Gate result: PASS.

---

## 1. COVERAGE AUDIT

Method. (a) ID count by grep on every structured file and ledger. (b) A fresh unit pass over each FULLTEXT: notes, statement lines and cells, auditor paragraphs, perimeter entities; slides and per-slide numbers; turns, questions, analysts, spoken numbers. (c) Diff against the A2 counts. (d) Test that every ledger row is cited in A4 or marked reviewed.

| Category | A2 count | Fresh count (A5) | Orphan / missing rows | Status |
|---|---|---|---|---|
| results: structured IDs vs ledger IDs | 449 / 449 | 449 (structured header 320+40+1+35+53) | none | PASS |
| results: note rows (distinct notes) | 15 (7) | 15 (7): CF notes R:L398-400; notes 1-5 R:L428-460; restated at R:L1156 and on p11 | none | PASS |
| results: statement lines / cells | 96 / 296 | 96 / 296: P&L R:L1057-1082 = 26 x 6; BS R:L1084-1118 = 35 x 2; CF R:L1120-1147 + L1149-1155 = 35 x 2 | none | PASS |
| results: auditor rows (R399-R449) | 51 | 51 (pp12-15, R:L872-1054) | none | PASS |
| results: perimeter entities | 1 | 1 (R:L993, Suryalaxmi Technologies, wholly-owned) | none | PASS |
| results: A2-noted rows absent from A4 | n.a. | R349/R350 at R:L1142 (FY26 PPE sale proceeds) | 1 row pair | FAIL, A3 (finding M3) |
| resultsrev: structured IDs vs ledger IDs | 743 / 743 (led-rr L3, L14) | 744. st-rr L4 "ROW ID range: R001-R744"; st-rr L5 QUALIFIER 55 (ledger says 54); R744 at st-rr L757 | R744 not in ledger | FAIL, A2 (finding M1) |
| resultsrev: new standalone lines / cells | 94 / 284 | 94 / 284: P&L RR:L191-214 = 24 x 6; BS RR:L316-350 = 35 x 2; CF RR:L444-471 + L521-527 = 35 x 2 | none | PASS |
| resultsrev: note rows | 15 | 15: CF notes RR:L528; notes 1-5 RR:L533-561; 8 carried | none | PASS |
| resultsrev: carried rows | 385 (R359-R743) | 385. Carried cells match the original at line + 101 (spot check RR:L1176-1177, L1198, L1206, L1241) | none | PASS |
| resultsrev: A2-noted rows absent from A4 | n.a. | R307/R308 at RR:L466 (same FY26 PPE sale, led-rr L347-348) | same item as above | FAIL, A3 (finding M3) |
| presentation: slides | 38 | 38 page markers (P fulltext L18-L768) | none | PASS |
| presentation: slides with no rows | 9 | 9, all dividers or the contents list: p4 L98, p5 L110, p7 L143, p14 L294, p20 L440, p25 L541, p28 L596, p33 L682, p36 L748 | none | PASS |
| presentation: per-slide numbers, 18 slides fresh-counted (1, 6, 8, 9, 10, 11, 12, 13, 15, 17, 21, 24, 29, 30, 31, 32, 34, 35, 37) | A2 per-slide counts (led-pres L61-85) | All match except p17. p37 lists scrip code 532726 once for two columns (acceptable) | see next row | see next row |
| presentation: p17 capacity table cells | 7 (R152-R158, st-pres L160-166) | 8. P:p17 l368-372: existing Mines "Nil", Steel 9,93,300 MT, Thermal 129 MW, Solar 7 MW; post Mines 70,00,000 MT, Steel 12,29,000 MT, Thermal 160 MW, Solar 85 MW | "Nil" (P:p17 l369) has no structured row; led-pres L215-216 says MISSING_FROM_STRUCTURED none | FAIL, A2 (finding M2) |
| presentation: rendered CELL rows | 366 | 366 by table geometry: p12 3; p16 34 (2 plants x 5 rows x 3 cols + 4 pie labels); p18 135 (9 products x 15 cols); p19 81 (9 x 9); p22 70 (14 x 5); p23 43 | none | PASS |
| presentation: MAPS-TO / CORRECTION rows | 358 / 5 | 358 / 5 | none | PASS |
| presentation: structured IDs vs ledger | 1,489 / 1,489 | 1,489 (597+66+26+37+34+366+358+5) | none | PASS |
| presentation: A2-flagged rows absent from A4 | n.a. | R018: CONFLICT p6 "30% QoQ" vs p21 "(23)%", "stays open" (led-pres L62, L210, L255). A4 never cites R018 or the 30% figure | 1 row | FAIL, A3 (finding M4) |
| concall: turns | 60 | 60 on A2's segmentation (C:l26-444). T39 and T40 each hold a question and its answer; no content falls outside a turn | none | PASS |
| concall: questions / analysts | 17 / 7 | 17 / 7: Q1a l215-217, Q1b l224-226, Q2a l250-252, Q2b l260-262, Q2c l274-276, Q3a l285-286, Q3b l291-293, Q3c l298-301, Q4a l321-322, Q4b not transcribed (answer l338-342), Q5a l346-348, Q5b l356, Q5c l360-362, Q6a l374-375, Q6b l380-382, Q6c l388 + l395, Q7 l419-422 | none | PASS |
| concall: management numbers | 115 | 115 figure-bearing rows confirmed line by line (C:l63-l399). Two rhetorical counts lack rows: "two decades" (C:l113), "four pillars" (C:l123). They carry no figure | none of data | PASS (STYLE note S8) |
| concall: structured IDs vs ledger | 263 / 263 | 263 (127+44+45+28+19). Ledger's 281 "R### \|" lines = 263 + 15 participant duplicates + 3 zero-standing duplicates | none | PASS |

Row-to-A4 test. A4 marks every row reviewed (rev L22, L31-L32). I accept that blanket mark for rows that carry no A2 flag. I do not accept it for the A2-flagged rows that A4 neither cites nor closes: results R349/R350 = resultsrev R307/R308 (FY26 PPE sale), and presentation R018 (open conflict). A4 also accepts gate_a2 = pass for resultsrev while noting that R744 sits outside the ledger (rev L27, L31). The protocol requires the ledger to account for every structured ID, so that acceptance does not hold.

---

## 2. ARITHMETIC AUDIT

I recomputed every derived metric in A4's tables from raw filed lakhs, or from rendered deck cells and ASR text where A4 uses them. Raw cells: R:L1057-1082 (consolidated P&L), R:L1084-1118 (BS), R:L1120-1155 (CF), RR:L191-214, RR:L316-350, RR:L444-471, RR:L521-527 (standalone).

| Metric (rev line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q2 FY27 (rev L194) | 109.69 | 8,317.37 + 3,550.62 + 916.66 - 1,815.24 = 10,969.41 lakhs = 109.69 | R:L1058, L1064, L1065, L1070 | PASS |
| Op EBITDA Q2 FY26 / Q1 FY27 / H1 FY27 / H1 FY26 / FY26 (rev L194) | 131.54 / 185.09 / 294.79 / 378.39 / 716.44 (S 716.45) | 13,154.15 / 18,509.28 / 29,478.68 / 37,838.91 / 71,644.38 (S 71,644.98) | same lines | PASS |
| Op EBITDA margin, six columns (rev L195) | 12.99 / 16.16 / 9.57 / 17.68 / 12.86 / 16.21% | 12.988 / 16.156 / 9.573 / 17.677 / 12.864 / 16.213% | R:L1057 | PASS |
| Margin change YoY / QoQ (rev L238, L257) | -342 / -658 bps | -341.6 / -658.3 bps | computed | PASS |
| Reported EBITDA and margin (rev L196-197) | 144.76, 203.40, 127.85, 398.43, 331.25, 776.04; 14.29, 17.75, 11.16, 18.61, 14.46, 17.56% | identical to 2 dp | R:L1064-1070 | PASS |
| Core PBT ex-OI and YoY (rev L198, L244) | 89.79, 146.50, 65.02, 299.34, 211.53, 544.44; -27.59% | 8,979.10 ... 54,444.07; 6,502.13 / 8,979.10 - 1 = -27.586% | R:L1058, L1070 | PASS |
| OI / PBT (rev L199) | 12.83, 11.11, 21.82, 6.27, 14.70, 9.87% | 12.831, 11.109, 21.825, 6.27498, 14.703, 9.866% | R:L1058, L1070 | PASS |
| ETR (rev L200) | 15.31, 24.97, 27.25, 18.27, 25.73, 19.83% | 15.314, 24.966, 27.248, 18.271, 25.731, 19.828% | R:L1073 | PASS |
| PAT margin C / S (rev L201-202) | Q2 FY26 8.78 / 8.61; Q2 FY27 5.28%; H1 FY26 12.27 / 12.19% | 8.781 / 8.613; 5.281; 12.274 / 12.194% | R:L1074, L1076 | PASS |
| Material ratio and gross margin (rev L203-204) | GM 25.45, 27.35, 21.00, 28.66, 24.18, 27.79% | 25.452, 27.353, 20.999, 28.662, 24.176, 27.788% | R:L1060-1062 | PASS |
| Traded purchases / revenue (rev L205) | 0.50, 0.77, 8.63, 1.05, 4.70, 0.90% | 0.504, 0.767, 8.628, 1.052, 4.698, 0.900% | R:L1061 | PASS |
| EPS on reported PAT (rev L131) | 3.69 / 10.89 | 8,892.62 / 2,412.809 = 3.686; 26,272.05 / 2,412.809 = 10.889 | R:L1076, L1081 | PASS |
| Revenue YoY; trading share of rise (rev L233) | +13.15%, +133.14; 93.76 = 70.4% | +13.146%, 13,314.13 lakhs; 9,376.32 lakhs = 70.42% | R:L1057, L1061 | PASS |
| PBT / PAT C / PAT S YoY (rev L245-247) | -19.25 / -31.95 / -30.63% | -19.255 / -31.954 / -30.632% | R:L1070, L1076; RR:L208 | PASS |
| EPS YoY (rev L248) | -30.66% filed; -31.98% vs 3.69 | 2.51 / 3.62 - 1 = -30.66%; 2.51 / 3.69 - 1 = -31.98% | R:L1082 | PASS |
| D&A YoY / QoQ; finance cost YoY (rev L240-241, L260) | +8.69 / +17.90 / +0.91% | +8.694 / +17.903 / +0.907% | R:L1064-1065 | PASS |
| EBIT operating (rev L242) | 98.88 to 74.19, -24.97% | 9,887.52 to 7,418.79 lakhs, -24.968% | computed | PASS |
| Deck volumes YoY / QoQ (rev L234-236, L252, L278) | TMT -6.82 / -14.58%; billets -11.76 / -22.1%; DRI sales +35.3% | -6.818 / -14.583%; -11.765 / -22.078%; +35.29% | P:R928-R931, R853-R856, R898-R901 | PASS |
| Op EBITDA per billet tonne (rev L220, L239) | 6,448 / 8,013 / 6,094 / 8,110; -5.5%; deck -7.1% | 6,448.1 / 8,012.7 / 6,094.1 / 8,110.1; -5.49%; 6,148.56 / 6,617.75 - 1 = -7.09% | P:R853-R856, R966, R1096-R1098 | PASS |
| PAT bridge (rev L295-309) | +3,388.65; -5,102.19; -805.84; +334.63; -283.99; -8.24; +493.59; -688.80 (= +303.75 - 992.55); -169.37; sum -2,841.56 | identical; GP change -1,713.54 = 24,062.52 - 25,776.06; actual PAT change -2,841.55 | R:L1057-1076 | PASS |
| Bridge shares of Q2 FY26 PAT (rev L295-307) | 38.1, 57.4, 9.1, 3.8, 3.2, 0.1, 5.6, 7.7, 3.4, 11.2, 1.9, 31.95% | identical to 1 dp | on 8,892.62 | PASS |
| Core vs other share of PAT fall (rev L316) | 87.2% / 12.8% | 2,476.97 / 2,841.55 = 87.17%; 364.58 / 2,841.55 = 12.83% | computed | PASS |
| OI-revert PAT (rev L317) | PBT 7,823.78; PAT 56.92 | 7,823.78 x 0.7275 = 5,691.80 lakhs | computed | PASS |
| Coal effect on Q2 revenue (rev L311) | 51.6-57.3; 68-76% of 75.40 | 51.57-57.29; 68.4-76.0% of 185.09 - 109.69 = 75.40 | C:l268-269 | PASS |
| FY26 deferred credit share of PBT (rev L319) | 634 bps | 3,830.43 / 60,403.48 = 6.341% | R:L1072 | PASS |
| Current tax assets change (rev L319) | +20.29 = 79.30 - 59.01 | 2,676.05 - 647.41 = 2,028.64 lakhs; 7,929.67 - 5,901.03 = 2,028.64 | R:L1099, L1139, L1071 | PASS |
| Q1 FY26 derived (rev L271) | 1,127.78; 21.89%; 209.55; GM 31.55% | 112,777.84; 21.888%; 20,954.83; 31.545% | H1 FY26 minus Q2 FY26 | PASS |
| H2 FY26 average (rev L273) | 1,139.20; 14.84%; 122.55; GM 26.97%; deferred credit 23.60 | 113,919.67; 14.837%; 12,255.07; 26.967%; 2,360.19 | FY26 minus H1 FY26 | PASS |
| Trading multiple; pellet vs nameplate (rev L280) | 11.25x; 115% | 9,886.58 / 878.47 = 11.254x; 228 / (792 / 4) = 115.2% | R:L1061; P:R823; P:p13 l285 | PASS |
| H1 average comparisons (rev L281) | 1,145.78; 105.76; 38.5% short | 2,291.56 / 2; 211.53 / 2; 65.02 / 105.76 = 0.615 | computed | PASS |
| CFO / PAT reported, C and S (rev L333-334) | 1.24x / 0.49x both | C 60,226.48 / 48,426.70 = 1.244; 9,082.36 / 18,417.78 = 0.493. S 1.244; 0.493 | R:L1140; RR:L464 | PASS |
| CFO / PAT ex current-financial-asset line (rev L335-336) | 1.00x / 0.56x both | C 48,367.88 / 48,426.70 = 0.999; 10,388.74 / 18,417.78 = 0.564. S 48,367.96 and 10,387.70 as A4 states | R:L1132; RR:L456 | PASS |
| CFO / PAT net-interest view (rev L337-338) | 1.25x / 0.56x both | C 60,561.10 = 1.251; 10,293.19 = 0.559. S 60,561.18 = 1.251; 10,270.15 = 0.558 | R:L1146, L1150; RR:L470, L522 | PASS |
| CFO / Op EBITDA (rev L339) | 84.1% / 30.8% | 84.06% / 30.81% | computed | PASS |
| Capex share of FY26; parent share (rev L340-341) | 80.0%; 98.1% | 278.47 / 348.15 = 79.98%; 273.12 / 278.47 = 98.08% | R:L1141; RR:L465 | PASS |
| FCF C / S (rev L342-343) | 254.11 / (187.64); 255.01 / (182.30) | 25,411.42 / -18,764.24; 25,500.65 / -18,230.19 lakhs | computed | PASS |
| WC change in CFO (rev L344) | +3.58 / (125.01) | 72,878.03 - 72,519.72 = 358.31; 17,012.03 - 29,512.93 = -12,500.90 | R:L1127, L1138 | PASS |
| Inventory rise (rev L345) | +21.41% | 66,863.55 / 55,074.62 - 1 = 21.405% | R:L1092 | PASS |
| Receivable / inventory / payable days; CCC (rev L346-349) | 14.67, 63.00, 19.62, 58.05 to 14.80, 70.42, 18.40, 66.82 | 14.668, 62.996, 19.617, 58.05 to 14.795, 70.421, 18.398, 66.82 (365 and 183 days) | R:L1092, L1094, L1112-1113 | PASS |
| Borrowings and current share (rev L352-354, L871) | 547.69 to 591.97 (+44.29); current 85.4% | 54,768.70 to 59,197.39; 50,568.66 / 59,197.39 = 85.42% | R:L1106, L1111 | PASS |
| Net debt C / S (rev L362-363) | 21.82 to 165.86; 21.86 to 165.89 | 2,181.75 to 16,586.13; 2,185.86 to 16,589.15 lakhs | R:L1093-1096, L1106, L1111; RR:L325-328 | PASS |
| Loans + other current financial assets (rev L361) | 603.45 to 591.88; 17.0% of equity | 60,344.95 to 59,187.83; 59,187.83 / 348,654.13 = 16.98% | R:L1097-1098, L1105 | PASS |
| Net cash as the CFO frames it; H2 need share (rev L365, L375) | +99.92; pool 691.90; 79.2% | 42,611.26 + 26,578.46 - 59,197.39 = 9,992.33 lakhs; 548.26 / 691.90 = 79.24%. A4's "426.12" sums rounded crores; the lakh sum is 426.11 | R:L1093-1097 | PASS (rounding) |
| Gross D/E; deck D/E basis (rev L366) | 0.17x; deck 0.289 = total liabilities / equity | 0.165 / 0.170; 100,643.05 / 348,654.13 = 0.2887 | R:L1105, L1110, L1117; P:p10 l216 | PASS |
| Deck ROCE and WC bases (rev L377) | 7.09% six months; Rs 1,274 Cr | (24,798.81 + 1,764.01) / (449,297.18 - 74,386.29) = 7.085%; 201,802.58 - 74,386.29 = 127,416.29 lakhs | R:L1101-1117; P:p10 l215; P:R1112 | PASS |
| Equity roll-forward gap (rev L367) | 14.06 | C: 18,436.30 - 17,030.65 = 1,405.65; S: 18,436.31 - 17,030.66 = 1,405.65 lakhs | R:L1080, L1104; RR:L212, L336 | PASS |
| S-vs-C PAT gap (rev L165-170) | +1.94 / +1.90%; 0.65 / 0.64%; FY26 -0.0013% | 169.37 / 8,723.25 = 1.942%; / 8,892.62 = 1.905%; 0.649 / 0.645%; -0.61 / 48,427.31 = -0.00126% | RR:L208 vs L1177 | PASS |
| S-vs-C balance sheet lines (rev L175-184) | PPE +1.80; CWIP +0.24; ONCA +4.19; cash +0.03; loans -6.03; OCFA -0.22; equity -0.005; capex +5.35 | 180.46; 24.38; 419.37; 3.02; -603.32; -22.01; -0.50; 535.08 lakhs | RR:L316-337, L465 vs L1185-1206, R:L1141 | PASS |
| Parent funding share of subsidiary assets (rev L187, L529) | Rs 6.26 Cr covers 99.7% | Loan + receivable 625.33 lakhs = 6.25 = 99.68% of 627.35; with the Rs 1.00 lakh equity (RR:L320 vs L1189) 626.33 = 6.26 = 99.84% | RR:L329-330 vs L1198-1199; R:L1013 | PASS (rounding-level basis mix; STYLE S2) |
| Dividend amount (rev L80) | 48.26 | 2 x 2,412.809 lakh shares = 4,825.62 lakhs | R:L1081; RR:L557-559 | PASS |
| TTM and annualised figures (rev L448) | Rev 4,569.95; Op EBITDA 632.84 (13.85%); PAT 405.72; EPS 16.82; Q2 annualised 242.04, EPS 10.03 | 456,995.19; 63,284.15 (13.848%); 40,572.43; 16.815; 24,204.28; 10.032 | FY26 + H1 FY27 - H1 FY26 | PASS |
| Market data (rev L465) | -22.1%; Rs 12,978 Cr; 32.0x | 537.90 / 690.65 - 1 = -22.12%; 537.90 x 24.128 crore shares = 12,978.5; 537.90 / 16.82 = 31.98 | P:p37 l760-762 | PASS |
| Promoter change; 30-Sep sum (rev L70, L368) | +0.95 pp as printed, 0.86 pp alt; 100.09% | 70.98 - 70.03; 70.98 + 0.09 + 29.02 = 100.09 | P:R582-R587 | PASS |
| Capacity step (rev L373, L450) | +23.7% | 12,29,000 / 9,93,300 = 1.2373 | P:R153, R157 | PASS |
| Capex tracker sums (rev L374, L523, L792) | 1,191 itemised; 652.54 spent; thermal 155.35 vs 151.00 | 860.00 + 331.00; 438.60 + 213.94; 107.99 + 47.36 vs 106.00 + 45.00 | P:R764-R793 | PASS |
| Deck vs filed EBITDA gap (rev L866) | 0.83 | 110.52 - 109.69 | P:p6 l121 | PASS |
| "+1000 bps" base (rev L534) | about -0.4% | 9.64 - 10.00 = -0.36% | P:p9 l197 | PASS |
| Q&A share of call (rev L591) | 25:14 = 57.6% | 1,514 / 2,629 s = 57.59% | C:l208, l437, l21 | PASS |
| Quantified claims; specificity (rev L649, L836) | 30 / 43 = 69.8%; 20 / 32 = 0.625 | recounted from the A4 rows: 30 YES, 13 NO; 20 and 12 items listed | rev L604-646, L835 | PASS |
| Defensive-language count (rev L841-846) | 10; 15 with supplementary | management "expect / feel" at C:l74, l131, l166, l205, l257, l273, l276, l349; "difficult" at l324, l333; passive at l144, l154, l399, l428; conditional at l352 | concall fulltext | PASS |

Arithmetic mismatches above rounding: none.

---

## 3. ADVERSARIAL READ

The three most positive claims in A4, each attacked from the same extracted text.

### Claim 1. The capacity step is "the main new positive" (rev L946, L1088, L435, L552, L1140)
A4: capacity rises 23.7%, from 9,93,300 MT to 12,29,000 MT, with a start near 10-Nov-2026 and 85-90% by December end. The 6D row reads ON TRACK. The forward map bull says the first full quarter "lifts volume".

Strongest bear counter:
- The step lands at one plant. The call says the 1.0 to 1.23 MT expansion "is now being integrated at Gorakhpur" (C:l87-88), with capacity added "at every stage of the chain at Gorakhpur except" sponge iron (C:l133-135). The deck sizes Gorakhpur at 6 lakh MTPA (P:p17 l356; P:R142). The 2,35,700 MT step (P:R153, R157) therefore lifts Gorakhpur by about 39% [INFERENCE: the deck does not split post-enhancement capacity by plant].
- Management's own ramp target implies a large jump in tonnes. 85-90% of about 8.36 lakh MTPA (C:l349-352) is about 178-188 KT of billets a quarter [computed]. Gorakhpur made 142 KT in Q1 FY27 (P:R844) and 107 KT in Q2 (P:R843).
- The market does not grow that fast. Management puts construction-steel demand growth at about 7% (C:l288). It already claims more than 25% of the served UP market (C:l146-147; P:p15 l316-318). Own TMT sales grew 1.5% at Gorakhpur in FY26, from 465.4 KT to 472.5 KT (P:R1005-R1006), and 1.6% overall, from 753.5 KT to 765.8 KT (P:R1011-R1013).
- About 59 KT a quarter of extra steel [computed] must therefore come from share gain, new geographies or lower prices. The call offers only "a ready channel to place the additional volumes" (C:l147).
- Management's Kutch record cuts against that channel claim. The Kutch rolling mill was a named focus area, yet utilisation moved only from 66% to 68% (C:l142-143). The distribution work gave "not much result" (C:l363-364).
- The deck figure carries an asterisk with no footnote and the label "(debottlenecking)" (P:p17 l371-372; P:R750, led-pres L198 FOOTNOTE_UNRESOLVED).

Strongest rebuttal from the extract: the old Gorakhpur plant was full. It ran at about 95% of nameplate in Q1 FY27 (142 / 150 KT) and 86% in FY26 (514.3 / 600 KT, P:R960) [computed]. Some of the Q2 trading (Rs 98.87 Cr, R:L1061) may also have served unmet demand, but the call is silent on trading.

Survives? YES. The rebuttal proves the old plant was capacity-bound. It does not prove that a 39% larger Gorakhpur can sell its output at today's spread. A4's bear forks on this claim cover a late start and commissioning trouble (rev L1133, L1135, L1140). They do not cover absorption or price.
Graft into A4: add the absorption counter to the 6D Gorakhpur row (killing evidence), the business-model or competition bear reading, and the Q1 FY28 forward-map bear fork.
Separating observation: Q4 FY27 Gorakhpur TMT sales tonnes (deck p18) against 125 KT in Q1 FY27 (P:R919), read with Q4 gross margin against 27.35% [INFERENCE threshold].

### Claim 2. Promoter buying is "the one clear bull datum" (rev L1066, L1089, L1012, L368, L476, L794)
A4: "Promoters bought about 0.9 pp in a falling quarter."

Strongest bear counter:
- The extract shows a percentage change, not a purchase. The only source is the deck's unaudited table (P:p37 l755-758). Its 30-Sep column sums to 100.09% (P:R582, R584, R586), and the deck disclaimer calls its figures "indicative and provisional" (P:p3 l93).
- The share count did not change (24,12,80,945, P:R588-R589). The rise therefore came from shares moving out of non-promoter hands. The extract does not say whether that was an open-market purchase, an off-market transfer or a reclassification of a holder into the promoter group. Only an open-market purchase is a confidence signal at a price.
- If it was a purchase, it was large. 0.86-0.95 pp is 20.75-22.92 lakh shares. At Rs 537.90-690.65 (P:R593-R594) that is about Rs 112-158 Cr [computed].
- The same half drew the company's cash down to Rs 1.12 Cr (R:L1095), while Rs 265.78 Cr of loans sat with unnamed borrowers (R:L1097).

Strongest rebuttal from the extract: A4 already carries the 100.09% error (rev L70), the funding and pledge question (Q33, rev L538), and a bear answer of "Funded by company-linked loans; pledge".

Survives? YES, in part. A4 states the purchase as fact in five places. It never states the transaction size.
Graft into A4: change "bought" / "buying" to "holding rose; mechanism undisclosed" at rev L368, L476, L794, L1012 and L1066. Add the Rs 112-158 Cr scale to Q33. Add to monitorable 2 (rev L960) that the filed shareholding pattern, together with any SAST or PIT disclosure, separates a purchase from a transfer.

### Claim 3. Prices rose late in Q2, so the spread recovers in Q3 (rev L1097, L1100, L252)
A4: September TMT prices were about 21% above a year earlier; "the better spread lands in Q3".

Strongest bear counter:
- The 21% is a year-on-year figure for one month (C:l128, l291). It is not a Q3-versus-Q2 spread.
- In the same answer management says coal took "about 4.5 to 5%" of sales (C:l268-269) and iron ore rose too (C:l270). It also says metallics prices "rose sharply in the second half of the quarter" (C:l129-130), and that "some bit of it is obviously being passed on to the energy prices" (C:l257-258). The realisation gain made no impact on Q2 (C:l265-266).

Survives? YES, but A4 already carries it: the sector bear "coal stays dear" (rev L1101), the input leg "not one-time on its own words" (rev L313), and the realisation contradiction (rev L253, L864). No graft required.
Note: I did not use the deck's per-tonne bridge here (NSR +13,964 against raw material -13,339, P:p24 l539). Both bars include traded goods (rev L312), so their ratio does not measure the own-steel spread.

### MANDATORY ACQUISITION-ECONOMICS PROBE
The documents describe four purchases or awards. I tested each.
- Iron ore blocks (preferred-bidder wins, P:p8 l150-152, l174-176; P:p9 l192): this is the testable one.
  - Price: the tracker plans Rs 249.00 Cr for raw-material deepening at Gorakhpur (P:R767). The call books Rs 240 Cr of H2 FY27 capex to mines (C:l311), which matches the Rs 240.75 Cr balance (P:R769).
  - Claimed earnings: about Rs 2,000 per tonne of EBITDA (P:p13 l290; C:l166, l276-277, l390).
  - Multiple: on FY26 own TMT sales of 765.8 KT (P:R1011) the gain is about Rs 153 Cr a year. On 12.29 lakh MT of capacity (P:R157) it is about Rs 246 Cr [computed]. The ratio is about Rs 249 Cr / Rs 153-246 Cr = 1.0-1.6x one year's claimed EBITDA, a payback of about 1-1.6 years [computed].
  - Why so cheap? (i) The Rs 2,000/t is a "management estimate" (P:p13 l290-291). Its scope moves between three levers (C:l165-167) and iron ore alone (C:l276-277). (ii) The benefit year is not representative. The call says FY28 (C:l157, l277) and the deck says FY30 (P:p9 l194). The mines will not feed 100% for "a year or two post FY28" (C:l278-281). (iii) The cost base may be incomplete. Rs 1,809 Cr of the Rs 3,000 Cr programme is not itemised (P:R776, R791; P:p11 l231-233). (iv) The gain runs "on the beta of the steel prices" (C:l277). (v) Rs 240 Cr leaves in H2 FY27 while clearances are still "underway" (C:l157), so cash goes out 1.5-3.5 years before the benefit.
  - Bear survives. A4 asks about scope and year (Q15, rev L520) and marks the trigger DELAYED (rev L437). It never states the multiple. Graft the multiple and these qualifiers into 6D, Q15 and 8D (rev L437, L520, L920).
- Coal block (award C:l78-79; due diligence C:l218; go or no-go in about a month, 2-3 years to operate, C:l376-379): consideration NOT FOUND, reserves NOT FOUND, target earnings not applicable (undeveloped block). No multiple can be stated, and the extract makes no "cheap, accretive" claim. A4's Q14 (rev L519) asks for reserves, grade, capex and the decision date. That is adequate.
- Suryalaxmi Technologies (wholly-owned subsidiary): cost of investment about Rs 0.01 Cr (non-current investments S 247.13 vs C 246.13 lakhs, RR:L320 vs L1189). Nil revenue and a Rs 0.01 lakh loss (R:L1013-1015). No meaningful multiple. A4's Q24 (rev L529) covers purpose and joining date.
- Promoter stake (a stake buy, if it was one): about Rs 112-158 Cr, as computed under Claim 2. At the 30-Sep price the stock traded at 32.0x TTM EPS (rev L465). Any purchase was therefore at a full multiple, not a cheap one. The economics belong in the Claim 2 graft.

---

## FINDINGS (every finding tagged)

| ID | Type | Loop to | Severity | Exact gap | Evidence lines |
|---|---|---|---|---|---|
| M1 | MISSING | A2 | LOW (mechanical) | The resultsrev ledger is stale. The structured file now runs R001-R744 with QUALIFIER 55. The ledger header and count test still say 743 and QUALIFIER 54, and "match: yes". R744, an A1 CORRECTION to R697, is not enumerated. | st-rr L4, L5, L710, L757; led-rr L3, L14, L452; rev L27, L31 |
| M2 | MISSING | A2 | LOW | The p17 capacity table has 8 cells; the structured file holds 7. The existing-mines cell "Nil" (P:p17 l369) has no row, and A2 recorded MISSING_FROM_STRUCTURED: none. A1's own convention extracts nil and dash cells (p16 dashes R782-R784 carry ZERO_STANDING). | P fulltext L368-372; st-pres L160-166; led-pres L215-216, L243 |
| M3 | MISSING | A3, then A4 | HIGH | The FY26 disposal of PPE for Rs 110.30 Cr (11,030.49 lakhs C, 11,030.50 S; loss Rs 0.24 Cr) appears nowhere in A4: no note, question, flag or monitorable. A2 noted it at resultsrev R307/R308. It equals 18.3% of FY26 CFO and 6.2% of 31-Mar-2026 PPE. It falls in the same year as the Rs 296.50 Cr loan book built from nil, a Rs 13.13 Cr investment exit and the vanished associate. Needed: what asset, which buyer, whether related, and whether the proceeds funded the loans. | R:L1084, L1126, L1140, L1142-1144; RR:L450, L466; led-res L412-413; led-rr L347-348 |
| M4 | MISSING | A3, then A4 | LOW | An open A2 CONFLICT on deck row R018 is unresolved. p6 prints "EBITDA per tonne 7% YoY. 30% QoQ"; p21 prints "(23)%"; the cells give 6,148.56 / 8,010.40 - 1 = -23.2%. A2 says it "stays open". A4's deck-error lists omit it. | P:p6 l123; P:p21 l457; P:R1097-R1098; led-pres L62, L210, L255; rev L1007, L981 |
| M5 | MISSING | A4 | MEDIUM | Surviving bear counter on Claim 1 (capacity absorption at Gorakhpur) is not in A4. | Section 3, Claim 1 |
| M6 | MISSING | A4 | MEDIUM | Surviving bear counter on Claim 2 is not in A4. The promoter rise is not evidenced as a purchase; the mechanism is undisclosed; the scale is Rs 112-158 Cr. | Section 3, Claim 2 |
| M7 | MISSING | A4 | MEDIUM | The mandatory acquisition probe finds no stated multiple in A4. The Rs 249 Cr mine plan is set against a claimed Rs 153-246 Cr a year of EBITDA (1.0-1.6x). The surviving bear qualifiers are not grafted. | Section 3, probe |
| M8 | MISSING | A4 | LOW | The deck's "Net debt / EBITDA 0.64x" divides Rs 190.58 Cr by half-year EBITDA (190.58 / 0.64 = Rs 297.8 Cr implied; call H1 EBITDA Rs 296 Cr). On TTM operating EBITDA of Rs 632.84 Cr it is 0.30x [computed]. The ratio is absent from A4's deck-basis flag and monitorable. It errs in the conservative direction. | P:p6 l132-137; C:l192; rev L448, L1008, L982 |
| M9 | MISSING | A4 | LOW | The deck's own p17 table lists existing solar at 7 MW and post-enhancement at 85 MW, which equals 7 + 18 + 60. So the deck counts Sidhpur's 18 MW as not yet existing [INFERENCE]. That sides with the call (C:l152) against "Commissioned Jul 2026" (P:p6 l137; P:p9 l193). A4 records the conflict as UNCLEAR without this evidence. | P:p17 l367-370; P:R152, R155; rev L686, L522, L1047 |

Factual findings: none. Contradiction findings: none.

---

## VERDICT

VERDICT: INCOMPLETE.

- Failing agents, in pipeline order: A2 (M1, M2), then A3 (M3, M4), then A4 (M5-M9 grafts).
- loop_back_to = A2, the earliest failing agent.
- Every looping finding is MISSING. There is no FACTUAL or CONTRADICTION finding, and the arithmetic is clean.
- Suggested narrow re-run scope:
  - A2: resultsrev ledger (add R744; refresh header and count test) and presentation ledger (record the p17 l369 "Nil" as MISSING_FROM_STRUCTURED for A1).
  - A3: results/resultsrev forensic on R:L1142 / RR:L466, and presentation forensic on R018.
  - A4: graft M3-M9 and the three adversarial results.
  - A5: re-audit.

---

## STYLE NOTES (logged; no loop)

- S1. rev L584 says "16 of 24 management Q&A turns". The A2 turn table (led-cc L42-L101) has 21 management-speaking Q&A turns: T10, T12, T16, T18, T20, T24, T26, T28, T30, T31, T32, T36, T37, T39, T40, T42, T45, T47, T49, T51, T55. The 24 adds the three prepared-remark turns T05-T07. Say "16 of 24 management turns" or "16 of 21 Q&A turns". The conclusion holds. The label is inherited from led-cc L458.
- S2. rev L187 and L529: "Rs 6.26 Cr covers 99.7%". The loan plus the receivable is Rs 6.25 Cr (99.7%). Adding the Rs 0.01 Cr equity gives Rs 6.26 Cr (99.8%). Use one basis. Rounding level.
- S3. rev L752 counts two analysts who congratulated on "a good set of numbers" (C:l248, l284). A third congratulated on "this good results" (C:l373). Add it if the point stays.
- S4. rev L662 and L736: "Rs 400 Cr Gorakhpur (Rs 240 Cr mines, Rs 170 Cr Prayagraj solar)". On the ASR text 240 + 170 = 410, not 400 (C:l310-311). The tracker balances support A4's reading (P:R769 240.75; P:R772 171.26; P:R778 421.40). Note the Rs 10 Cr ASR gap.
- S5. rev L438 and L611 date the coal block award to August 2026 (C:l78-79). The same call says it "was just allotted last month" (C:l376), which is September on a 21-Oct call. Note both.
- S6. rev L375: "funded by cash, debt and loan recoveries, not by CFO of Rs 90.82 Cr". CFO funded Rs 90.82 Cr of the Rs 278.47 Cr (32.6%). Say "beyond CFO".
- S7. Ledger and A1 anchors are off in note columns. Q4b "answer at lines 321-326" should be C:l338-342 (led-cc L116; the T37 row at L78 is right). T40 "management reply lines 340-341" should be C:l357-358 (led-cc L81). R019 context "lines 70 and 375" should be C:l87 and l392 (st-cc L30). R117 is anchored at l357, but the analyst speaks at C:l356 (st-cc L128). A4 cites the right lines in each case.
- S8. The concall rhetorical counts "two decades" (C:l113) and "four pillars" (C:l123) have no NUMBER row, while "three anchors" has one (R011, st-cc L22). They carry no figure, and no downstream agent uses them. Align the A1 convention at the next extraction.

---

```yaml
stage: A5-adversary
company: "GALLANTT"
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
  orphan_rows:
    - "results R349/R350 = resultsrev R307/R308 (R:L1142, RR:L466): FY26 PPE sale proceeds Rs 110.30 Cr, A2-noted at led-rr L347-348, absent from A4"
    - "presentation R018 (P:p6 l123 'EBITDA per tonne 7% YoY. 30% QoQ'): A2 CONFLICT vs p21 '(23)%' left open (led-pres L62, L210, L255), absent from A4"
  missing_from_ledger:
    - "resultsrev R744 (st-rr L757, A1 CORRECTION to R697): structured now R001-R744 and QUALIFIER 55 (st-rr L4-5); ledger still 743 and QUALIFIER 54 (led-rr L3, L14)"
    - "presentation P:p17 l369 'Nil' (Mines, existing capacity): 8-cell table, structured holds 7 (R152-R158); no MISSING_FROM_STRUCTURED entry (led-pres L215-216)"
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Capacity +23.7% from ~10-Nov-2026 is the main new positive (rev L946, L1088, L435, L552, L1140)"
    counter: "The step lands at Gorakhpur (C:l87-88), a 6 lakh MTPA plant (P:p17 l356), so +39% there [INFERENCE]. 85-90% (C:l349-352) implies ~178-188 KT billets a quarter vs a 142 KT Q1 peak (P:R844). Home demand ~+7% (C:l288); share already >25% (C:l146-147); own TMT sales +1.5% Gorakhpur and +1.6% total in FY26 (P:R1005-R1006, R1011-R1013); Kutch mill 66% to 68% after a focus quarter (C:l142-143, l363-364); post-enhancement cell has an unresolved asterisk (P:p17 l371, R750). A4 bear forks cover timing only, not absorption or price."
    source_line: "C:l87-88, l146-147, l288, l349-352; P:p17 l356, l371; P:R844, R1005-R1006, R1011-R1013"
    type: MISSING
  - claim: "Promoters bought about 0.9 pp in a falling quarter; the one clear bull datum (rev L1066, L1089, L1012, L368, L476, L794)"
    counter: "The extract shows a percentage change in an unaudited deck table that sums to 100.09% (P:p37 l755-758) under an 'indicative and provisional' disclaimer (P:p3 l93), not a purchase. Share count unchanged (P:R588-R589); mechanism (open market, off-market transfer, reclassification) undisclosed. If a purchase, 0.86-0.95 pp = 20.75-22.92 lakh shares = ~Rs 112-158 Cr at Rs 537.90-690.65 [computed], in a half when company cash fell to Rs 1.12 Cr (R:L1095) and Rs 265.78 Cr sat in loans to unnamed borrowers (R:L1097)."
    source_line: "P:p37 l755-762; P:p3 l93; P:R582-R594; R:L1095, L1097"
    type: MISSING
  - claim: "Iron ore mines add ~Rs 2,000/t EBITDA (deck P:p13 l290; A4 rev L437, L520, L920 records it without a multiple)"
    counter: "Acquisition probe: Rs 249 Cr mine plan (P:R767; H2 Rs 240 Cr, C:l311) vs claimed ~Rs 153-246 Cr a year (Rs 2,000/t on 765.8 KT sales or 12.29 lakh MT capacity, P:R1011, R157) = 1.0-1.6x, a ~1-1.6 year payback [computed]. Benefit is a management estimate with shifting scope (C:l165-167 vs l276-277), dated FY28 (C:l157) vs FY30 (P:p9 l194), full only a year or two post FY28 (C:l278-281); Rs 1,809 Cr of the programme is unitemised (P:R776, R791); cash leaves in H2 FY27 while clearances are underway (C:l157, l311)."
    source_line: "P:p13 l290-291; P:R767-R769, R776, R791, R1011, R157; P:p9 l194; C:l157, l165-167, l276-281, l311"
    type: MISSING
findings_by_type:
  factual: []
  missing:
    - "M1 (A2, LOW): resultsrev ledger stale; R744 not enumerated; header/count test 743 and QUALIFIER 54 vs structured R001-R744 and QUALIFIER 55 (st-rr L4-5, L757; led-rr L3, L14)"
    - "M2 (A2, LOW): P:p17 l369 'Nil' existing-mines cell missing from structured; A2 recorded no MISSING_FROM_STRUCTURED (st-pres L160-166; led-pres L215-216)"
    - "M3 (A3 then A4, HIGH): FY26 PPE disposal Rs 110.30 Cr, loss Rs 0.24 Cr (R:L1126, L1142; RR:L450, L466) absent from A4; same year as Rs 296.50 Cr loan book from nil (R:L1144) and Rs 13.13 Cr investment exit (R:L1143); need asset, buyer, related-party status, use of proceeds"
    - "M4 (A3 then A4, LOW): open A2 CONFLICT R018, p6 EBITDA/t '30% QoQ' vs p21 '(23)%', computed -23.2% (P:p6 l123, P:p21 l457, P:R1097-R1098; led-pres L255); not in A4 deck-error lists (rev L1007, L981)"
    - "M5 (A4, MEDIUM): graft the Claim 1 capacity-absorption counter"
    - "M6 (A4, MEDIUM): graft the Claim 2 promoter counter; replace 'bought'/'buying' with 'holding rose, mechanism undisclosed'; add the Rs 112-158 Cr scale to Q33"
    - "M7 (A4, MEDIUM): graft the mines acquisition multiple 1.0-1.6x and its bear qualifiers into 6D, Q15, 8D"
    - "M8 (A4, LOW): deck Net debt/EBITDA 0.64x uses half-year EBITDA (190.58 / ~296-298); 0.30x on TTM operating EBITDA 632.84; add to flag 17 and monitorable 24 (P:p6 l132-137; C:l192)"
    - "M9 (A4, LOW): deck p17 solar existing 7 MW and post 85 MW (= 7 + 18 + 60) imply Sidhpur 18 MW is not yet existing [INFERENCE]; add to the Sidhpur conflict (P:p17 l367-370; rev L686, L522)"
  contradiction: []
  style:
    - "S1: rev L584 '16 of 24 management Q&A turns'; Q&A management turns are 21 on A2's table; 24 includes T05-T07"
    - "S2: rev L187, L529 'Rs 6.26 Cr covers 99.7%' mixes bases (6.25 = 99.7%; 6.26 incl. equity = 99.8%); rounding level"
    - "S3: rev L752 two congratulating analysts; a third at C:l373"
    - "S4: rev L662, L736 H2 split 240 + 170 = 410 vs 400 on the ASR text (C:l310-311); tracker supports A4's reading"
    - "S5: rev L438, L611 coal block Aug-2026 vs 'just allotted last month' (C:l376)"
    - "S6: rev L375 'not by CFO of Rs 90.82 Cr'; CFO funded 32.6%; say 'beyond CFO'"
    - "S7: ledger/A1 note-column anchors off (led-cc L81, L116; st-cc L30, L128); A4 cites correct lines"
    - "S8: concall rhetorical counts 'two decades' (C:l113), 'four pillars' (C:l123) not extracted while 'three anchors' (R011) was; no figure carried"
loop_back_to: "A2"
gap: "A2: (M1) resultsrev ledger lacks R744 and carries a stale 743/QUALIFIER 54 count test; (M2) P:p17 l369 'Nil' existing-mines cell missing from structured, not recorded as MISSING_FROM_STRUCTURED. A3: (M3) no forensic on the FY26 PPE disposal Rs 110.30 Cr (R:L1142, RR:L466); (M4) open CONFLICT R018 p6 '30% QoQ' vs p21 '(23)%' unresolved. A4: graft surviving bear counters M5 (Gorakhpur absorption), M6 (promoter rise not evidenced as a purchase, Rs 112-158 Cr), M7 (mines 1.0-1.6x capex-to-claimed-EBITDA), plus M8 (deck net debt/EBITDA on half-year EBITDA) and M9 (p17 solar 7/85 MW on Sidhpur). All MISSING; arithmetic clean."
style_notes:
  - "S1: relabel '16 of 24' as management turns, or say 16 of 21 Q&A turns"
  - "S2: pick one basis for the subsidiary funding share (99.7% or 99.8%)"
  - "S3: third congratulating analyst at C:l373"
  - "S4: note the Rs 10 Cr ASR gap in the H2 capex split"
  - "S5: note the coal block award-date conflict inside the call"
  - "S6: 'beyond CFO' in place of 'not by CFO'"
  - "S7: fix ledger and A1 note-column line anchors"
  - "S8: align the A1 convention for rhetorical counts"
analyst_note: "Arithmetic is clean: every derived metric in A4's tables re-foots from filed lakhs and deck cells within rounding, and the five-part brief passes the gate. The verdict rests on coverage and on surviving bear counters, all MISSING. Two coverage gaps are mechanical: the resultsrev ledger predates A1's R744 correction row, and A1 dropped the p17 'Nil' existing-mines cell. The one material miss is the FY26 sale of PPE for Rs 110.30 Cr (R:L1142). It is unexplained and absent from A4, in the year the Rs 296.50 Cr loan book appeared and the associate vanished. Adversarially, the capacity bull ignores absorption: Gorakhpur grows about 39% on the call's own plant split, in a market growing about 7%, after own TMT sales grew 1.6% in FY26. The promoter 'buying' is a percentage change in a deck table, not an evidenced purchase, and would be worth Rs 112-158 Cr if it was one. The mines claim implies a 1-1.6 year payback that nothing in the extract costs. The price-recovery bull holds up only because A4 already carries the coal counter. Re-runs can stay narrow: A2 on two ledgers, A3 on two rows, A4 on grafts."
```
