# A5 ADVERSARY / COMPLETENESS AUDIT: SUPREMEPWR H1 FY27

Company: Supreme Power Equipment Limited (NSE SME: SUPREMEPWR). Period: half year ended 30-Sep-2026.
Agent: A5 adversary | Model: claude-opus-5-5 | Audit date: 24-Oct-2026
Under audit: runs/supremepwr-h1fy27/work/review_supremepwr_h1fy27.md (A4, 1,051 lines)

Inputs read (and nothing else):
- A1 fulltexts: extracted/supremepwr-{results,presentation,pressrelease,concall}-h1fy27-fulltext.md
- A1 structured: extracted/supremepwr-{results,presentation,pressrelease,concall}-h1fy27-structured.md
- A2 ledgers: work/ledger_{results,presentation,pressrelease,concall}_supremepwr_h1fy27.md
- A4 review (above)

Not read: the source PDFs, anything under inputs/, A3 forensic notes, any other work/ file. No source access was needed. No pipeline error.

Anchor key: "review l.N" = line in the A4 review. "RES l.N", "PPT l.N", "PRS l.N", "CC l.N" = line in the matching A1 fulltext. "RES-R###" etc. = A1 structured row. Lakhs converted x0.01 to Rs Cr. "derived" = A5 arithmetic on anchored filed numbers.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS: narrative PRESENT | sector PRESENT | business model PRESENT | competition PRESENT | forward map PRESENT. Gate: PASS.

| Brief part | Location | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | review l.913-918 | Five paragraphs, about 215 words; results, cash, Danya, call, verdict. Inside 200-400 words; renders inside 10-20 lines | PRESENT |
| 2. Sector intelligence | review l.920-928 | Grid capacity, industry growth, GEC-II, access rule, inputs, bushings, one [INFERENCE], not-disclosed list | PRESENT |
| 3. Business-model intelligence | review l.930-937 | Order route, unit economics per MVA, mix, margin, working capital, model drift | PRESENT |
| 4. Competition intelligence | review l.939-944 | Where it wins, where it is weaker, comparators (PENDING LIVE VERIFICATION marked), concentration | PRESENT |
| 5. Forward map | review l.946-956 | Make-or-break metric plus nine catalysts, each with a bull and a bear fork; eight dated, two honestly "undated" (STYLE note S6) | PRESENT |

The gate passes. The content defects inside the brief are logged under audits 2 and 3 (findings C1, C2, M3, M4, M5).

---

## 1. COVERAGE AUDIT

Method. I re-enumerated each A1 fulltext by line, independent of the A2 counts: every numbered note, every financial-table line (verified OCR blocks for results pages 4, 5, 7, 10, 11, 13), every slide and printed number (RAW-ORDER supplements for table pages), every press-release page, every speaker turn and every management number in the ASR transcript. I then matched each unit to a structured row ID and each row ID to a ledger row. Last, I checked each ledger category against A4's citations and its explicit "reviewed" statement (review l.23).

| Doc | Category | A2 count | A5 fresh count | Orphan rows (ledger, not in A4) | Status |
|---|---|---|---|---|---|
| Results | Notes (SA 8, CON 9, CF 4, BS footnotes 2, certificate 1) | 24 | 24 | 0 (all 24 in A4 Step 0D table, review l.62-74) | PASS |
| Results | Financial line items (SA P&L 25, SA BS 23, SA CF 40, CON P&L 27, CON BS 23, CON CF 30) | 168 | 168, plus 2 blank "Paid up Equity Share Capital" template rows (SA annotated R562, RES l.234; CON unannotated, raw RES l.756) | 0 | PASS (STYLE S1) |
| Results | ZERO_STANDING dash rows | 44 | 44 (SA P&L 12, SA CF 18, CON P&L 9, CON CF 5) | 0 | PASS |
| Results | Agenda items | 2 | 2 (RES l.39, l.46) | 0 | PASS |
| Results | Auditor paragraphs | 9 (qualifier rows) | 12 paragraphs (SA LRR 5, CON LRR 7); the 3 without a row (RES l.85, l.608, l.616) are boilerplate whose content sits in R003, R004, R556, R566 | 0 | PASS (STYLE S2) |
| Results | Entities / dates / forward / signatures | 28 / 33 / 9 / 3 | 28 / 33 / 9 / 3 | 0 | PASS |
| Results | ID accountability | 609 / 609 | 609 | 0 | PASS |
| Presentation | Slides (pages) | 41 | 41 | 0 | PASS |
| Presentation | Printed numbers | 457 | 457 (chart axis ticks excluded per R651) | 0 | PASS |
| Presentation | Entities / forward / dates / qualifiers | 94 / 58 / 35 / 103 | 94 / 58 / 35 / 103 | 0 | PASS |
| Presentation | ZERO_STANDING | 10 | 9 data zeros (PPT l.904-905, l.912) plus R101 "nil rejection" target, which is not a zero value | 0 | PASS (STYLE S3) |
| Presentation | ID accountability | 747 / 747 | 747 | 0 | PASS |
| Press release | Pages / numbers / entities / forward / dates / qualifiers | 4 / 78 / 34 / 28 / 13 / 13 | 4 / 78 / 34 / 28 / 13 / 13 | 0 | PASS |
| Press release | ID accountability | 166 / 166 | 166 | 0 | PASS |
| Concall | Turns (T01-T99) | 99 | 99 (boundaries re-checked at each moderator hand-off) | 0 | PASS |
| Concall | Participants / analysts | 16 / 10 (9 substantive) | 16 / 10 (9 substantive; Q5 audio loss CC l.327-341) | 0 | PASS |
| Concall | Analyst questions (turns) | 41 | 41 | 0 | PASS |
| Concall | Management numbers | 93 | 94: one management number has no row (see M1) | 0 | **FAIL, loop A2** |
| Concall | Forward / entities / dates / qualifiers / zero | 61 / 43 / 25 / 73 / 1 | 61 / 43 / 25 / 73 / 1 | 0 | PASS |
| Concall | ID accountability | 323 / 323 | 323 | 0 | PASS |

Orphan-row check against A4. A4 states that all 24 notes, 99 turns, 45 slides, 168 line items, 44 ZERO_STANDING rows, 9 auditor paragraphs and 2 agenda items were reviewed, and that ID accountability is 609/747/166/323 (review l.23). That is an explicit "reviewed" mark at category level. Every note, every P&L line and every analyst exchange is also cited by row. Orphan rows: 0.

Coverage findings:

- **M1 (MISSING, loop A2).** CC l.287 (turn T38, management reply): "Actually customer they are placed out of one year before or eight months nine months before the project may the timeline of the project may extend for the customer." This is a management number (orders placed 8 to 12 months before the customer's project). It is management's only stated reason why the 353 Cr customer requirement (CC l.270) runs above the 200-250 Cr H2 guide (CC l.275). No structured row carries it: T38 maps to R064, R065, R066, R192, R193, R286, R287, R309 (concall ledger l.80), and none holds the 8-12 month figure. The ledger reports MISSING_FROM_STRUCTURED "none" (concall ledger l.510-511). A2 must raise it so A1 adds the row.
- **M2 (MISSING, loop A3).** Deck slide 34 (PPT page 35, l.739-807) carries two concentration series that no A4 line cites. (a) Top-10 vs other customers, FY24-FY26: 79.68/20.32, 65.55/34.45, 67.86/32.14 % of SA revenue (PPT-R271-R276). (b) Government vs non-government, FY24-FY26: 34.93/65.07, 26.35/73.65, 31.73/68.27 % (PPT-R277-R282). A1 flags the series-to-legend mapping as unresolved (PPT-R723). On the high reading, the top 10 customers made 67.86% of FY26 SA revenue. Series (b) gives the FY24-FY26 baseline (about 26-35% government) against which H1 FY27's 40.14% government share (PPT-R133, l.347) is a rise, against the deck's own "Increase Private Sector Mix" pillar (PPT-R596, l.563). A4's flag 10 (review l.872) rests only on H1 order geography. The deck's own risk slide lists "Customer Concentration (EPC & Utilities)" (PPT-R699, l.573). A3 must note both series with the mapping caveat, and A4 must carry both readings and add a question.

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4's tables was recomputed from the filed Lakh values (four decimals in Cr), then rounded as A4 rounds. Section A arithmetic ties throughout. The two mismatches sit in Section B (Role 5 counts). One basis contradiction sits in Step 5 (C1).

| # | Metric | A4 value | A5 recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | CON Op EBITDA H1 FY26 / H2 FY26 / H1 FY27 / FY26 (PBT + D + Fin - OI) | 14.11 / 18.71 / 23.35 / 32.82 | 14.113 / 18.711 / 23.355 / 32.824 | RES l.767, 774, 775, 784 | PASS |
| 2 | CON Op EBITDA margin | 18.77 / 17.58 / 17.26 / 18.07% | 18.769 / 17.578 / 17.260 / 18.071% | RES l.766 | PASS |
| 3 | CON reported EBITDA, margin on total income | 14.27 / 19.01 / 23.62 / 33.29; 18.94 / 17.81 / 17.42 / 18.28% | 14.275 / 19.011 / 23.619 / 33.285; 18.943 / 17.809 / 17.422 / 18.278% | RES l.768; ties PPT l.164, l.844 | PASS |
| 4 | CON gross margin (Rev - net material - other direct) | 24.83 / 23.43 / 22.83 / 24.01% | 24.825 / 23.430 / 22.830 / 24.008% | RES l.766, 770-772 | PASS |
| 5 | CON core PBT; OI / PBT | 12.71 / 15.35 / 18.40 / 28.06; 1.26 / 1.91 / 1.42 / 1.62% | 12.709 / 15.346 / 18.396 / 28.055; 1.256 / 1.915 / 1.417 / 1.617% | RES l.767, 784 | PASS |
| 6 | CON ETR | 26.17 / 28.59 / 26.19 / 27.50% | 26.169 / 28.588 / 26.191 / 27.496% | RES l.786-788 | PASS |
| 7 | CON PAT margin (attributable / revenue) | 12.51 / 10.36 / 10.09 / 11.25% | 12.512 / 10.364 / 10.089 / 11.253% | RES l.792 | PASS |
| 8 | SA Op EBITDA; margin | 12.53 / 16.12 / 21.37 / 28.65; 15.53 / 14.74 / 16.81 / 15.07% | 12.528 / 16.124 / 21.369 / 28.652; 15.532 / 14.736 / 16.808 / 15.074% | RES l.204, 205, 212, 213, 222 | PASS |
| 9 | SA reported EBITDA FY26 | 30.99 | 30.987 | RES l.222; ties PPT l.731 | PASS |
| 10 | SA core PBT; OI / PBT; ETR; PAT margin | 11.31 / 13.28 / 16.57 / 24.58; 7.87 / 9.35 / 7.28 / 8.67%; 23.33 / 24.68 / 23.64 / 24.07%; 11.66 / 10.08 / 10.74 / 10.75% | 11.307 / 13.277 / 16.575 / 24.584; 7.868 / 9.350 / 7.283 / 8.675%; 23.334 / 24.679 / 23.638 / 24.065%; 11.664 / 10.082 / 10.737 / 10.754% | RES l.204-227 | PASS |
| 11 | S-v-C attributable PAT gap | 0.00 / 0.00 / 0.0001 / 0.00 | 0.0000 / 0.0000 / 0.0001 / 0.0000 | RES l.792 vs l.227 | PASS |
| 12 | S-v-C pre-minority PAT gap, % of SA PAT | +0.09 / +0.14 / +0.12 / +0.24; 1.00 / 1.28 / 0.89 / 1.15% | +0.094 / +0.141 / +0.122 / +0.235; 0.998 / 1.279 / 0.894 / 1.150% | RES l.789 vs l.227 | PASS |
| 13 | S-v-C revenue gap; % of SA revenue | (5.47) / (2.97) / +8.17 / (8.44); -6.78 / -2.71 / +6.43 / -4.44% | -5.467 / -2.970 / +8.171 / -8.437; -6.777 / -2.715 / +6.427 / -4.439% | RES l.766 vs l.204 | PASS |
| 14 | Op EBITDA margin gap CON - SA | +324 / +284 / +45 / +300 bps | +324 / +284 / +45 / +300 bps | derived rows 2, 8 | PASS |
| 15 | FY24-FY26 revenue gap (deck) | +6.28 / +3.92 / -8.44 | +6.28 / +3.92 / -8.44 | PPT l.724, l.837 | PASS |
| 16 | CON YoY: revenue, op EBITDA, D&A, finance | +79.9 / +65.5 / +415.4 / +189.5% | +79.95 / +65.48 / +415.4 / +189.5% | RES l.766, 774, 775 | PASS |
| 17 | CON EBIT (op EBITDA - D&A) and YoY | 13.72 to 21.31, +55.4% | 13.717 to 21.314, +55.38% | derived | PASS |
| 18 | CON YoY: OI, core PBT, PBT, PAT, EPS | +63.7 / +44.7 / +45.0 / +45.1 / +45.2% | +63.68 / +44.74 / +44.98 / +45.09 / +45.21% | RES l.767, 784, 792, 794 | PASS |
| 19 | SA YoY: revenue, op EBITDA, D&A, finance, EBIT, OI, core PBT, PBT, PAT | +57.6 / +70.6 / +468.1 / +221.7 / +59.1 / +34.8 / +46.6 / +45.7 / +45.1% | +57.62 / +70.56 / +468.1 / +221.7 / +59.11 / +34.83 / +46.59 / +45.67 / +45.09% | RES l.204-227 | PASS |
| 20 | Danya share of SA OI | 84% | 84.3% (109.73 / 130.19 L) | RES l.549, l.205 | PASS |
| 21 | H1 share of FY27 guide; FY26 H1 seasonality; seasonal FY27 | 38.7-45.1%; 41.40%; 326.8 | 38.66-45.10%; 41.40%; 326.85 | RES l.766; CC l.150 | PASS |
| 22 | PAT bridge items (Step 4) | +14.92 / (2.70) / (2.02) / (0.96) / (1.65) / (1.91) / +0.10 / (1.52) / (0.03) = +4.24 | +14.924 / -2.699 / -2.021 / -0.961 / -1.645 / -1.910 / +0.103 / -1.519 / -0.028 = +4.243 vs filed delta +4.242 | RES l.766-792 | PASS |
| 23 | Bridge items as % of PAT change | +351.8 / -63.7 / -47.6 / -22.6 / -38.8 / -45.0 / +2.4 / -35.8 / -0.7 | +351.8 / -63.6 / -47.6 / -22.6 / -38.8 / -45.0 / +2.4 / -35.8 / -0.7 | derived | PASS (rounding) |
| 24 | Tax change split volume / rate | 1.515 / 0.004 | 1.515 / 0.004 | derived | PASS |
| 25 | OI share of PBT change; run-rate PAT if OI reverts | 1.8%; 13.57 | 1.78%; 13.575 | derived | PASS |
| 26 | HoH revenue; H2 need for guide; H2 need vs H2 FY26; implied Q2 | +41.6%, +27.1%; 164.69-214.69; +54.7% to +101.7%; 87.08 | +41.56%, +27.12%; 164.69-214.69; +54.72% to +101.69%; 87.08 | RES l.766; CC l.150 | PASS |
| 27 | FY24 / FY25 op margin and core PBT (deck) | 20.45 / 19.00%; 19.61 / 25.23 | 20.448 / 18.995%; 19.61 / 25.23 | PPT l.837-847 | PASS |
| 28 | CON CFO; CFO / pre-minority PAT; FCF | 25.90 / (5.74); 1.25 / -0.42; (31.58) / (14.42) | 25.905 / -5.738; 1.253 / -0.417; -31.576 / -14.416 | RES l.1153, 1155, 789 | PASS |
| 29 | CON working-capital change from CF | +2.82 / (26.75) | +2.824 / -26.751 | RES l.1145-1150 | PASS |
| 30 | CON receivable / inventory / payable days, CCC (A4 basis: 31-Mar balance on FY26 flows, 30-Sep balance on H1 flows) | 94.1 to 84.8; 164.2 to 153.3; 164.5 to 148.3; 93.9 to 89.8 (-4.1) | 94.13 to 84.77; 164.20 to 153.27; 164.47 to 148.26; 93.86 to 89.78 | RES l.911, 910, 896-897 | PASS on arithmetic; basis contradicts the ruling (C1) |
| 31 | Same days, matched-half basis (31-Mar balance on H2 FY26 flows, 182 days) | not shown | 80.1 to 84.8 (+4.7); 138.7 to 153.3 (+14.6); 138.9 to 148.3 (+9.4); CCC 79.9 to 89.8 (+9.9) | RES l.766 and l.770-772 column B | see C1 |
| 32 | Same days, TTM basis (H2 FY26 + H1 FY27 flows) | not shown | 94.1 to 94.6 (+0.5); 164.2 to 171.7 (+7.5); 164.5 to 166.1 (+1.6); CCC 93.9 to 100.3 (+6.4) | as above | see C1 |
| 33 | CON PPE / CWIP change; net debt; gross D/E ex-MI | +2.34 / +3.93; 40.23 to 57.20 (+42.2%); 0.42 / 0.44 | +2.342 / +3.927; 40.228 to 57.198 (+42.19%); 0.423 / 0.436 | RES l.884-912 | PASS |
| 34 | SA CFO / PAT; FCF; WC change | 1.36 / -0.38; (29.73) / (13.79); +4.71 / (24.16) | 1.357 / -0.383; -29.731 / -13.788; +4.712 / -24.157 | RES l.551-571 | PASS |
| 35 | SA receivable / inventory / payable days, CCC; net debt | 86.8 to 75.4; 109.7 to 130.3; 143.4 to 139.9; 53.1 to 65.8; 35.99 to 54.80 (+52.3%) | 86.82 to 75.38; 109.75 to 130.34; 143.42 to 139.90; 53.15 to 65.82; 35.989 to 54.802 (+52.27%) | RES l.334-359 | PASS |
| 36 | Danya slice: receivables, inventory, LT debt repaid, SA LT borrowing, SA injection, partner withdrawal | 1.63 to 10.31 (6.3x); 17.02; 2.96; 5.11; 2.75; 0.20 | 1.634 to 10.312 (6.31x); 17.015; 2.965; 5.109; 2.746; 0.200 | RES l.911 vs 358, 910 vs 357, l.1161 vs 576, l.572, l.1164 | PASS |
| 37 | Danya ETR; Danya PAT share of CON PAT | about 35.2%; 8.85% | 35.17% (tax 0.6615 / PBT 1.8807); 8.85% (1.2192 / 13.7729) | derived from RES l.784/222, 786-787/224-225, 549 | PASS |
| 38 | Capex rebuild H1 (PPE + D&A + CWIP + IAUD + intangibles) | ties 8.56 SA | 8.558 SA; 8.678 CON | RES l.350-353, 213; l.904-907, 775 | PASS |
| 39 | Warrant balance; dilution; due date | 15.81; 4.99%; 27-Feb-2027 | 15.806; 4.990%; 27-Aug-2025 + 18 months | RES l.435-441 | PASS |
| 40 | TTM PAT; TTM PE; diluted mcap and PE | 24.68; 23.9x; 619.9 / 25.1x | 24.684; 23.92x; 619.88 / 25.11x | RES l.792; PPT l.1044-1046 | PASS |
| 41 | FY26 incremental ROCE; fixed-asset turnover; 500-550 Cr need | 5.2%; 4.60 / 2.32 / 1.52; 4.2-4.6x | 5.20%; 4.599 / 2.325 / 1.517; 4.18-4.59x | PPT l.844-903 | PASS |
| 42 | Step 8C thresholds | 31.64 / 5.74 | 31.64 / 5.74 | RES l.1153; PPT l.852 | PASS |
| 43 | Q6 gap; Q8 implied H2 inflow | 103-153; 234-484 | 103-153; 234.2-484.2 | CC l.144-145, 270-275 | PASS |
| 44 | Order concentration: Hyderabad share; Hyderabad "company" share; 20 MVA share; 112.5 MVA value; 13+ month value | 67.7%; 48.6%; 75.9%; 27.10; 114.50 | 67.67%; 48.60%; 75.91%; 27.10; 114.50 | PPT l.207-217; PRS l.106-153 | PASS |
| 45 | 6A PAT margin vs 9% floor; 7C implied growth | 10.09%, 109 bps; 65%-93% | 10.089%, 109 bps; 65.2%-92.7% | derived | PASS |
| 46 | Call duration; Q&A length and share | 49.3 min; 40.3 min, 82% | 49.33; 40.33, 81.8% | CC l.26, l.115, l.557 | PASS |
| 47 | Q&A grade count | A 5, B 18, C 10, D 3, ND 2 of 38 | same | review l.619-658 | PASS |
| 48 | Hedge counts; "I think" | 7 / 11 / 3 / 1 / 1 = 23; 14 | 7 / 11 (12 instances, l.179-180 merged) / 3 / 1 / 1; 14 management lines | CC l.100-519 | PASS |
| 49 | Role 5 Step 1 quantified share of opening claims | 8 of 23 = 34.8% | 9 of 23 = 39.1% (the claims table marks claims 1, 5, 6, 7, 8, 9, 11, 12, 14 as YES) | review l.533-555 vs l.558 | **FAIL (F1)** |
| 50 | Role 5 Step 6B specificity ratio | 22 / 60 = 0.37 | 27 / 60 = 0.45 with A4's rule applied evenly; 31 / 60 = 0.52 on a literal reading | CC-R165-R225; review l.749 | **FAIL (F2)** |

Arithmetic findings:

- **F1 (FACTUAL, loop A4).** Review l.558 says "Quantified share: 8 of 23 = 34.8%". The table above it (review l.533-555) marks nine claims YES: 1, 5, 6, 7, 8, 9, 11 (binary), 12, 14. The ratio is 9 / 23 = 39.1%. The same line says "All eight quantified claims are backward-looking or order data". Claim 11 (Maharashtra entry) is operational and claim 14 (PVC share) is operational. Fix the count, or drop claim 11 from YES and say why.
- **F2 (FACTUAL, loop A4).** Review l.749 counts 22 of 60 forward rows as quantified "(number, date or binary)". The rule is applied unevenly. R183 ("final unit expected next year") is counted, but R199, R207 and R208 (each "next year") are not. R190 ("600 crores in next two years") is counted, but R210 ("next 2 years") is not. R197 ("next 8 to 10 years") is not counted. With the rule applied evenly: 27 / 60 = 0.45. On a literal reading that also counts R166, R167 (period references), R220 (50 MVA) and R223 (2-3 orders): 31 / 60 = 0.52. At 0.52 the provisional EVASIVE quadrant at review l.763 flips, because it keys on "at or below 0.5". Fix: state the classification per row, recompute, and label the quadrant INDETERMINATE when the ratio sits within 0.05 of 0.5.
- **C1 (CONTRADICTION, loop A4).** The Step 5-CON days rows (review l.289-292) show improvement: receivable -9.3, inventory -10.9, payable -16.2 and CCC -4.1 days. This is a basis artefact. The 31-Mar-2026 column divides a year-end balance by full-year FY26 flows, while the 30-Sep-2026 column divides by H1 flows. The year-end balance reflects the heavier second half: FY26 had only 41.4% of revenue in H1. The ruling at review l.324 says "direction: deteriorating", and the brief at review l.915 says "Stock and receivables grew faster than sales". On a matched-half basis (rows 31-32), receivable days rose 80.1 to 84.8, inventory days 138.7 to 153.3, payable days 138.9 to 148.3, and CCC 79.9 to 89.8 (+9.9 days). On TTM the CCC rose 93.9 to 100.3 (+6.4). The matched bases support A4's ruling. A4's own table contradicts it. Restate the table on a matched-half or TTM basis, or footnote that the sign comes from the basis.

---

## 3. ADVERSARIAL READ

Three most positive claims in the A4 review, each attacked from the same extracted text.

### Claim 1: "Demand is proven" (review l.918); "The quarter proves demand and order intake" (review l.857)
Strongest bear counter:
- 13.64 Cr of the 60.11 Cr YoY increase in CON revenue (22.7%) is the swing in the CON-minus-SA revenue gap, from (5.47) to +8.17 Cr (RES l.766 vs l.204; derived). The parent's own revenue grew +57.6%, not +79.9%.
- That swing is carried by Danya Electric. Danya is an unaudited partnership whose other partners are the MD and the WTD (RES l.1009-1010). Note 4 leaves its assurance level as an unfilled placeholder (RES l.1019). Intra-group sales are not disclosed. CON attributable PAT equals SA PAT to within Rs 1,000 (RES l.792 vs l.227), so no unrealised-profit elimination is visible on Danya's 17.02 Cr of stock.
- Order intake is concentrated. 67.7% of H1 order value came from Hyderabad buyers. Four unnamed Hyderabad "company" orders made 48.6%. No counterparty is named (PPT l.207-217; PRS-R162).
- Management's own H2 guide (200-250 Cr, CC l.271-275) sits below the 353 Cr customer requirement (CC l.270) because "the timeline of the project may extend for the customer" (CC l.287).

Survives: YES. A4 holds each piece separately (review l.175-179, flags 4 and 10), but it never states that 22.7% of the headline growth rides on the Danya swing. It also lets "Demand is proven" stand unqualified in the brief and in Section C.
Graft into A4 (finding M5, MISSING): Section C l.857 and brief l.918 should read that order intake is proven, that 22.7% of the YoY CON revenue increase is the Danya swing, and that the parent's revenue grew 57.6%.

### Claim 2: "The headline is real, not treasury-driven" (review l.222); "Revenue +79.9% and core PBT +44.7% are real" (analyst_note, review l.1048)
Strongest bear counter: "Not treasury-driven" does not mean cash-backed or confirmed. CFO was (5.74) Cr against pre-minority PAT of 13.77 Cr (RES l.1153, l.789). The 26.75 Cr working-capital build absorbed all the profit. Trade payables, loans and other liabilities are "subjected to confirmation and reconciliation", with adjustments "in the year of confirmation" (RES l.445, l.1022). The Danya input (8.85% of CON PAT) rests on the note 4 placeholder and on the auditor's reliance on "the statement provided by the management" (RES l.665).
Survives: YES in substance, but A4 already carries every element (Step 5 RED rows, the cash ruling, flags 2, 4 and 5, Q2 and Q10, monitorable 9). No graft is needed. STYLE note S10: in the analyst note, change "are real" to "are non-treasury".

### Claim 3: "Run-rate lifted: PASS on revenue" (capex commissioning test, review l.245); Kannur fill "Confirming evidence: Revenue run-rate lifted HoH +27.1%" (review l.399); "PARTIALLY CONFIRMED" (review l.773)
Strongest bear counter:
- The Kannur build sits in the parent [INFERENCE from filed lines]. CWIP is identical in SA and CON (3,190.70 L, RES l.352 and l.906). FY26 capex was 57.46 Cr in SA against 57.48 Cr in CON (RES l.571, l.1155). SA carries 88.92 of the 92.64 Cr CON PPE (RES l.350, l.904).
- The parent's revenue rose only +16.2% HoH (109.42 to 127.14 Cr, RES l.204).
- 11.14 Cr of the 28.86 Cr HoH increase in CON revenue (38.6%) is the Danya gap swing, from (2.97) to +8.17 Cr (derived).
- Kannur runs at 20-30% (CC l.462). 75.9% of H1 order value is 20 MVA units, and the old plant is rated up to 25 MVA (PPT l.444). Plant-wise revenue and MVA output are not disclosed (CC l.357).
- SA inventory rose 24.88 Cr (RES l.209), so production ran ahead of dispatch.
- So the HoH lift in CON revenue is not evidence of Kannur fill.

Survives: YES. A4 notes "Attribution by plant: ND", but it still scores the revenue test as PASS and still uses the HoH lift as confirming evidence.
Graft into A4 (finding M6, MISSING): in Step 3, Step 6D and Step 7A, state the parent HoH of +16.2% and the 38.6% swing share. Set the Kannur-fill confirming evidence to "none attributable".

### Mandatory acquisition-economics probe
Not triggered. A grep of all four fulltexts for "acqui|stake|takeover|merger|amalgamat" returns two hits. One is "type test certificates all to be to be acquired" (CC l.525). The other is Danya's existing 90% "subsidiary stake" (PPT l.547). No document describes an acquisition, a purchase or a stake buy, so there is no consideration to set against target earnings.

The nearest analogue is the H1 capital injection of 2.75 Cr into Danya (RES l.572). It is a contribution to an existing 90% partnership while the MD and WTD partners withdrew 0.20 Cr (RES l.1164). SPEL's capital account in Danya is 16.52 Cr (RES l.354) against minority capital of 3.99 Cr (RES l.887). That is 80.5% of partners' capital for a 90% profit share. A4 Q3 already covers this (review l.456). No new graft.

---

## FINDINGS REGISTER (every finding tagged)

| ID | Type | Loop | Finding | Anchors |
|---|---|---|---|---|
| M1 | MISSING | A2 | A management number (orders placed one year or 8-9 months before the customer's project) has no structured row and no ledger row | CC l.287 (T38); concall ledger l.80, l.510-511 |
| M2 | MISSING | A3 | The deck slide 34 top-10 customer and government-share series (FY24-FY26) are uncited. Mapping unresolved; high reading: top 10 = 67.86% of FY26 SA revenue; government 26-35% FY24-FY26 vs 40.14% in H1 FY27 | PPT l.739-807; PPT-R271-R282, R723, R133, R596, R699; review l.872 |
| M3 | MISSING | A4 | The filed PVC figure "around 70-75%" (deck and release) is omitted. The brief gives "about 70-80% ... four different figures" and Q15 lists 70/80/70-80/90. The only written figure must anchor; the call figures are ASR | PPT l.182 (R057, R553); PRS l.80 (R025); review l.925, l.468 |
| M4 | MISSING | A4 | The brief states "The last two targets were missed." without a tag. No extract supports the FY26 guide path or the Q1 miss (a grep for 48.23, 190, 225 and 50-60 finds nothing relevant). The source is Spear memory (review l.239, l.386, l.598-599), but the brief header says "Every figure below is from this half's documents" | review l.911, l.917 |
| M5 | MISSING | A4 | Surviving bear counter to claim 1: the Danya swing is 22.7% of the YoY CON revenue increase; parent revenue +57.6% | RES l.204, l.766, l.1019; review l.857, l.918 |
| M6 | MISSING | A4 | Surviving bear counter to claim 3: the parent (which holds Kannur) grew +16.2% HoH; the Danya swing is 38.6% of the HoH CON increase; the HoH lift is not Kannur-fill evidence | RES l.204, l.352, l.571, l.766, l.906, l.1155; CC l.357, l.462; review l.245, l.399, l.773 |
| C1 | CONTRADICTION | A4 | The Step 5-CON days Change column shows improvement (CCC -4.1) from a basis mismatch, against the "deteriorating" ruling and the brief. Matched-half CCC +9.9 days; TTM CCC +6.4 days | RES l.766, 770-772, 896-897, 910-911; review l.289-292, l.324, l.915 |
| C2 | CONTRADICTION | A4 | The capability threshold "above 25 MVA" is tagged "(MGMT, call)", but the call states no 25 MVA figure. Its type-test remark covers "100 MA 50 MA" for the new plant. The 25 MVA figure is the deck's (PPT-R153, R121, R126), and the deck's own Kannur slide says earlier rating "Up to 50 MVA" (PPT-R162). Name the conflict and re-tag as deck plus [INFERENCE] | CC l.524-527; PPT l.279, l.312, l.444, l.457; review l.439, l.469, l.941 |
| F1 | FACTUAL | A4 | Opening-claims quantified share is 9 of 23 = 39.1%, not 8 of 23 = 34.8% | review l.533-558 |
| F2 | FACTUAL | A4 | Specificity ratio 0.37 rests on an uneven rule. Applied evenly: 0.45. Literal: 0.52, which crosses the 0.5 EVASIVE line | CC-R165-R225; review l.749, l.763 |

Not challenged: the protocol verdict (PROCEED WITH FLAGS), the cash ruling (INDETERMINATE-WITH-DIRECTION), the governance flags, and all Section A arithmetic. The A3 correction A4 carried on Kannur's state (review l.27) is right: PPT l.441-442 and CC l.226 both place the plant in Tamil Nadu.

---

## VERDICT

**INCOMPLETE.** Loop back to **A2**, the earliest failing agent. A re-run from A2 also re-runs A3 and A4 on the corrected ledger. The failures by agent and type:
- **A2:** M1 (MISSING). Ledger the CC l.287 management number. Raise MISSING_FROM_STRUCTURED so A1 adds the row.
- **A3:** M2 (MISSING). Forensic note on the deck slide 34 concentration and government-share series, with the mapping caveat (PPT-R723).
- **A4:** C1 and C2 (CONTRADICTION), M3, M4, M5 and M6 (MISSING), F1 and F2 (FACTUAL), as set out in the register above.

---

## STYLE NOTES (logged; no re-run on their own)

- S1. The CON P&L "Paid up Equity Share Capital" template row (raw RES l.756) is blank, like the SA row, but has no A1 note equivalent to R562. Three value rows for four labels confirm that the row is blank. No number is affected.
- S2. The A1 structured file and the A2 ledger do not carry boilerplate auditor paragraphs (RES l.85, l.608, l.616), statutory references (s.133, s.143(10), Rule 7, Chapter XB) or the auditor's phone numbers (RES l.72, l.1178). Their substantive content is captured in R003, R004, R556 and R566.
- S3. PPT-R101 ("nil rejection at customer end", a vision target) is flagged ZERO_STANDING. It is not a zero value.
- S4. A4's "reviewed, no finding" mark is category-level (review l.23), not row-level. It is acceptable here; a row-level mark would make the next audit cheaper.
- S5. Results ledger R487 carries the generic note "holding / sole subsidiary Danya". The row is SPEL itself (RES l.57).
- S6. Two forward-map items are "Undated" or "Next filing" (review l.954-955). They are honest, but the brief part calls for dated catalysts. Add "date not given by management".
- S7. "Depreciation rose five times" (review l.914) reads as +500%. The filed change is 5.2x (+415%).
- S8. "Fourth fall in a row" (review l.243, l.914) mixes annual (FY24, FY25) and half-year readings. Every like-for-like basis also falls, so the conclusion stands.
- S9. "Three decades of supply to Tamil Nadu utilities" (review l.940): the deck dates the TNEB relationship to 2001 (PPT l.309). Three decades is the company's age (PPT l.283). "The CMD answered every working-capital, cash and margin question with ranges only" (review l.516): the CFO answer was a sign and a period, not a range.
- S10. Analyst note "are real" should read "are non-treasury" (claim 2 counter, already covered in the body).
- S11. Step 2 forward guidance cites CC-R078 for management's drift to "350" (review l.567). R078 is analyst-stated. Management's own drift is CC-R068 (CC l.305).

---

Loop 0 YAML block, SUPERSEDED by the Loop 2 block at the end of this file:

```yaml
stage: A5-adversary
company: "SUPREMEPWR"
quarter: "h1fy27"
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
  missing_from_ledger:
    - {doc: "concall", fulltext_line: 287, turn: "T38", unit: "management: customers place orders one year or 8-9 months before the project; project timeline may extend", type: "MISSING", loop: "A2"}
arithmetic_mismatches:
  - {metric: "Role 5 Step 1 quantified share of opening claims", a4_value: "8 of 23 = 34.8%", recomputed: "9 of 23 = 39.1% (claims 1,5,6,7,8,9,11,12,14 marked YES)", source_line: "review l.533-558"}
  - {metric: "Role 5 Step 6B specificity ratio", a4_value: "22/60 = 0.37", recomputed: "27/60 = 0.45 with A4's rule applied evenly (+R197,R199,R207,R208,R210); 31/60 = 0.52 literal (+R166,R167,R220,R223)", source_line: "concall structured R165-R225; review l.749, l.763"}
surviving_bear_counters:
  - {claim: "Demand is proven; quarter proves demand and order intake (review l.918, l.857)", counter: "13.64 Cr of the 60.11 Cr YoY CON revenue increase (22.7%) is the CON-minus-SA gap swing (-5.47 to +8.17) carried by Danya, an unaudited promoter-partnered firm with the note 4 assurance placeholder and no visible elimination; parent revenue +57.6%; 67.7% of H1 inflow from unnamed Hyderabad buyers", source_line: "RES l.204, l.766, l.792 vs l.227, l.1019; PPT l.207-217", type: "MISSING"}
  - {claim: "Headline is real, not treasury-driven (review l.222; analyst_note)", counter: "non-treasury is not cash-backed or confirmed: CFO (5.74) vs PAT 13.77; payables and liabilities unconfirmed (notes 4/5); Danya input on management statement; already incorporated in Step 5 and flags 2/4/5, wording fix only", source_line: "RES l.1153, l.789, l.445, l.1022, l.665", type: "STYLE"}
  - {claim: "Capex commissioning test PASS on revenue; Kannur fill confirmed by HoH +27.1% (review l.245, l.399, l.773)", counter: "Kannur sits in the parent (CWIP SA = CON 3,190.70 L; FY26 capex SA 57.46 of CON 57.48 Cr) [INFERENCE]; parent revenue +16.2% HoH (109.42 to 127.14); 11.14 Cr (38.6%) of the 28.86 Cr CON HoH increase is the Danya swing; Kannur 20-30%; 75.9% of H1 inflow is 20 MVA; plant-wise revenue and MVA not disclosed", source_line: "RES l.204, l.352, l.571, l.766, l.906, l.1155; CC l.357, l.462", type: "MISSING"}
findings_by_type:
  factual:
    - "F1 [A4] Opening-claims quantified share is 9 of 23 = 39.1%, not 8 of 23 = 34.8% (review l.533-558)"
    - "F2 [A4] Specificity ratio 0.37 applies the number/date/binary rule unevenly (R183 vs R199/R207/R208; R190 vs R210; R197); even 0.45, literal 0.52 crosses the 0.5 EVASIVE line (review l.749, l.763)"
  missing:
    - "M1 [A2] Concall l.287 (T38) management number, orders placed one year or 8-9 months before project, has no structured or ledger row"
    - "M2 [A3] Deck slide 34 top-10 customer and government-share series FY24-FY26 (PPT-R271-R282, mapping unresolved R723) uncited; high reading top-10 = 67.86% of FY26 SA revenue; government 26-35% vs 40.14% H1 FY27 (PPT-R133)"
    - "M3 [A4] Filed PVC figure 'around 70-75%' (PPT l.182, PRS l.80) omitted; brief l.925 gives 70-80%"
    - "M4 [A4] Brief l.917 'The last two targets were missed' is untagged Spear memory inside a brief declared to use only this half's documents (l.911); no extract support"
    - "M5 [A4] Graft counter to claim 1: Danya swing = 22.7% of YoY CON revenue increase; qualify 'Demand is proven' (l.857, l.918)"
    - "M6 [A4] Graft counter to claim 3: parent HoH revenue +16.2%; Danya swing = 38.6% of HoH CON increase; Kannur-fill confirming evidence = none attributable (l.245, l.399, l.773)"
  contradiction:
    - "C1 [A4] Step 5-CON days Change column shows improvement (CCC -4.1) from a full-year vs half-year basis mismatch, against the 'deteriorating' ruling (l.324) and brief l.915; matched-half CCC 79.9 to 89.8 (+9.9), TTM 93.9 to 100.3 (+6.4)"
    - "C2 [A4] 'Above 25 MVA' capability threshold tagged (MGMT, call) at l.941 but the call states no 25 MVA figure; deck gives 25 MVA (PPT-R153 l.444) and 'Earlier: Up to 50 MVA' (PPT-R162 l.457); conflict unaddressed (also l.439, l.469)"
  style:
    - "S1 CON paid-up share capital template row (raw RES l.756) blank but unannotated; SA equivalent R562"
    - "S2 Boilerplate auditor paragraphs, statutory references and auditor phone numbers carry no rows; content captured elsewhere"
    - "S3 PPT-R101 'nil rejection' flagged ZERO_STANDING; not a zero value"
    - "S4 A4 'reviewed' mark is category-level (l.23), not row-level"
    - "S5 Results ledger R487 note is generic; row is SPEL itself"
    - "S6 Two forward-map items undated (l.954-955); add 'date not given by management'"
    - "S7 'Depreciation rose five times' reads +500%; filed change 5.2x"
    - "S8 'Fourth fall in a row' mixes annual and half readings; like-for-like also falls"
    - "S9 'Three decades of supply to TN utilities' vs TNEB from 2001; 'ranges only' overstates (CFO answer was a sign and period)"
    - "S10 Analyst note 'are real' should read 'are non-treasury'"
    - "S11 Step 2 cites analyst-stated CC-R078 as management drift to 350; management row is CC-R068"
loop_back_to: "A2"
gap: "A2: ledger the CC l.287 (T38) management number and raise MISSING_FROM_STRUCTURED so A1 adds the row. A3: forensic note on deck slide 34 top-10 customer and government-share series (PPT-R271-R282, mapping caveat R723). A4 on re-run: restate Step 5-CON days on a matched-half or TTM basis (C1); name the deck 25 vs 50 MVA conflict and re-tag brief l.941 (C2); anchor PVC to filed 70-75% (M3); tag 'last two targets were missed' as Spear memory (M4); graft Danya-swing counters (22.7% YoY, 38.6% HoH, parent HoH +16.2%) into Section C, brief, Step 3, Step 6D, Step 7A (M5, M6); fix Role 5 Step 1 count to 9 of 23 (F1) and the Step 6B specificity rule and quadrant (F2)."
style_notes:
  - "S1-S11 as listed under findings_by_type.style; logged only, no re-run"
analyst_note: "Section A arithmetic ties: more than 60 derived metrics recomputed from filed Lakh values, none off beyond rounding. The failures are coverage, provenance and framing, not numbers. The loop starts at A2 only because one ASR management number (CC l.287) has no row; that fix is narrow, and A3 and A4 then re-run on the corrected ledger. The strongest adversarial result: the Danya consolidation swing explains 22.7% of the YoY and 38.6% of the HoH increase in CON revenue, and the parent that holds Kannur grew 16.2% HoH. Neither 'demand is proven' nor the Kannur revenue PASS can stand unqualified. The days table shows improvement only because it divides a year-end balance by full-year flows; on matched halves the CCC rose about 10 days, which supports A4's own 'deteriorating' ruling. The acquisition probe was not triggered: no document has a purchase or stake buy, and the 2.75 Cr Danya injection is already covered by A4 Q3. None of the findings moves the protocol verdict (PROCEED WITH FLAGS) or the cash cap."
```

---

# LOOP 1 RE-AUDIT (24-Oct-2026)

Scope. Correction loop 1 changed three inputs. The A4 review now runs to 1,107 lines, with its change list at review l.8-24. The concall structured file now runs R001-R326 (header counts NUMBER 123, FORWARD 62). The concall ledger now accounts for 326 of 326 IDs, and its count test shows management numbers 95 and forward rows 62. The other three structured files and ledgers are unchanged (results 609/609, presentation 747/747, press release 166/166; headers re-checked). Input discipline is the same as loop 0: A1 fulltexts and structured files, A2 ledgers and the A4 review only. I did not read the A3 notes. Where a fix depends on A3 (M2), I verified its content as A4 carries it.

Line anchors in this section ("review l.N") refer to the loop-1 revision of the review. Before this section, I made one change to the loop-0 text: the label above the loop-0 YAML block marks it SUPERSEDED.

## L1-1. Per-finding clearance

| ID | Type | A5 check against the extracts | Where in the revised review | Status |
|---|---|---|---|---|
| F1 | FACTUAL | The claims table (review l.570-592) marks 9 YES: claims 1, 5, 6, 7, 8, 9, 11, 12, 14. 9 / 23 = 39.13%. The line no longer says "all eight" | review l.595 | CLEARED |
| F2 | FACTUAL | The rule is stated (l.788). Every forward row R165-R225 except analyst-voice R206, plus R326, is classified exactly once: 31 QUANTIFIED, 30 UNQUANTIFIED, total 61. The rule is applied evenly (spot checks: R183, R199, R207, R208 all "next year" and all QUANTIFIED; R190, R210 both QUANTIFIED; R222, R224, R225 UNQUANTIFIED). 31 / 61 = 0.508; 28 / 57 = 0.491. The archetype moves from EVASIVE to INDETERMINATE, within 0.05 of the line (l.808, l.890, YAML flag l.1101). M7 below adds one or two unquantified rows to the population, giving 31 / 62 = 0.500 or 31 / 63 = 0.492. The label holds | review l.787-794, l.808 | CLEARED (denominator moves with M7) |
| C1 | CONTRADICTION | The matched-half basis is stated (l.309). CON: A5 recompute 80.10 to 84.77, 138.66 to 153.27, 138.89 to 148.26, CCC 79.87 to 89.78; matches l.320-323. TTM row matches l.324. SA: A5 recompute 75.20 to 75.38, 94.53 to 130.34, 123.53 to 139.90, CCC 46.20 to 65.82; matches l.343-346. The ruling (l.356, l.360), flags 5 (l.915), the YAML and brief l.964 and l.984 now all point the same way | review l.309-360, l.915, l.964, l.984 | CLEARED |
| C2 | CONTRADICTION | The cited rows exist and say what A4 says: PPT-R121 (l.279), R126 (l.312) and R153 (l.444) give 25 MVA; PPT-R162 (l.457) gives "Up to 50 MVA"; CC-R115 (l.526) gives "100 MA 50 MA". The call is no longer cited for 25 MVA. The capability inference is tagged [INFERENCE] | review l.474, l.504 (Q16), l.918 (flag 8), l.990 | CLEARED |
| M1 | MISSING | CC-R324 and R325 exist at CC l.287 (structured l.459-460). The ledger carries them as T38 management numbers (ledger l.514-515). The review cites them | review l.612, l.672, l.714-715, l.742, l.822, l.515 (Q27), l.935, l.980, l.1000 | CLEARED |
| M2 | MISSING | FP-20 and FP-21 are in A4's incorporation list (l.45). Both chart readings are stated with PPT-R271-R282 and the R723 caveat (l.208). A5 recompute: government share +8.41 pp (40.14 - 31.73) under reading A and -28.13 pp (40.14 - 68.27) under reading B; A4 notes that the bases differ | review l.208, l.423, l.457, l.510 (Q22), l.516 (Q28), l.920, l.992, l.953 | CLEARED |
| M3 | MISSING | "Around 70-75%" (PPT-R057, l.182; PRS-R025, l.80) is anchored as the written figure. The call figures are listed as ASR | review l.503 (Q15), l.583, l.721, l.817, l.974 | CLEARED |
| M4 | MISSING | A MEMORY tier is added to the brief header (l.960). The sentence is tagged "(MEMORY)" (l.966). The forward map is tagged (l.999). Flag 6 is tagged Spear memory (l.916) | review l.960, l.966, l.999, l.916 | CLEARED |
| M5 | MISSING | Attribution table (l.199-204): A5 recompute 60.115, 13.638, 22.69%, +57.62%. A grep for "Demand is proven" finds only the change list; the claim now reads "Order intake is proven" | review l.199-206, l.220, l.249, l.905, l.914, l.963, l.967, l.985, l.1104 | CLEARED |
| M6 | MISSING | The capex test now reads INDETERMINATE on revenue (l.274); a grep for "PASS on revenue" finds 0 hits. Kannur-fill confirming evidence reads "None attributable" (l.433), and 7A and Role 5 8A read "no attributable filed revenue evidence" (l.818, l.842). A5 recompute: 28.863, 11.142, 38.60%, +16.20% | review l.204, l.269, l.274, l.433, l.507, l.730, l.818, l.842 | CLEARED |

STYLE S1-S11 status. A4 applied S6-S11 (S6 l.942-945 and l.1004-1005; S7 l.963; S8 l.272; S9 l.989; S10 l.251 and l.1104; S11 l.604). S1-S5 belong to A1/A2 or are about category-level marking. They stay open and are logged only.

## L1-2. Coverage re-run (changed sections)

Method change, stated plainly. In loop 0, my concall pass checked management numbers line by line but checked forward statements only by sample. That pass missed two forward units. One was CC l.383 ("So we believe this margin will sustain"), which A1 found on its own sweep and added as R326. The other is M7 below. This loop swept every management turn (T03 to T95) for future-tense, expectation and commitment wording, and matched each unit to a row.

| Doc | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Concall | Management numbers | 95 | 95 (M1 rows R324, R325 present) | 0 | PASS |
| Concall | Forward rows | 62 | 63 or 64: T17 CC l.206-207 has no row (M7) | 0 | **FAIL, loop A2** |
| Concall | Turns / questions / entities / dates / qualifiers / zero | 99 / 41 / 43 / 25 / 73 / 1 | unchanged, re-confirmed | 0 | PASS |
| Concall | ID accountability | 326 / 326 | 326 | 0 (R324-R326 cited at review l.502, l.515, l.612, l.672, l.682, l.722, l.742) | PASS |
| Results / presentation / press release | ID accountability | 609 / 747 / 166 | unchanged files | 0 | PASS |

New finding:

- **M7 (MISSING, loop A2).** Turn T17, CC l.206-207, management reply: "So whatever the price escalates it will be covered. The margin will not affect much". This is a forward claim on margin protection, and no FORWARD row carries it:
  - A grep of the structured file for "affect" and "will be covered" returns 0 hits.
  - T17 maps only to R032, R120, R135, R182 and R314 (ledger l.59). R120 rows the "more than three decades" number on the same line l.207 but not the forward clause. R314 rows the PVC-coverage statement at l.203, not the margin forecast.
  - A1's own convention rows every instance of a forward statement: R180, R212 and R221, and in this loop R326, the second instance of the margin-sustain claim. The l.206-207 claim is the same class.
  - A4 already tests this exact claim against the filing (review l.817: CONTRADICTED), so the review's content is complete. Only the spine and the Step 6B population change: 31 / 62 = 0.50 with one row, or 31 / 63 = 0.49 with two. The INDETERMINATE label holds.
  - Fix: A2 raises MISSING_FROM_STRUCTURED, and A1 adds one or two FORWARD rows. A4 then updates the Step 6B population and ratio and cites the new row(s) in 7A l.817. No new forensic content is expected from A3.

Borderline units, logged as STYLE (no loop): CC l.90-91 "We continue to manage this through disciplined procurement ... protecting profitability" (substance restated in R171-R172 at l.103-104); CC l.497 "we do not find any problem in getting bushings" (present tense; bushing supply is rowed in R222-R223).

Brief gate re-check. All five parts are present (review l.962-1006). The summary is about 235 words, inside 200-400. The forward map has ten catalysts, each with a bull and a bear fork; two say "date not given by management" (l.1004, l.1005). Gate: PASS.

## L1-3. Arithmetic re-run (changed sections)

| Metric | A4 value | A5 recomputed | Source line | Status |
|---|---|---|---|---|
| Swing attribution YoY: CON increase, swing, share, parent growth | 60.11; 13.64; 22.7%; +57.6% | 60.115; 13.638; 22.69%; +57.62% | RES l.204, l.766 | PASS |
| Swing attribution HoH | 28.86; 11.14; 38.6%; +16.2% | 28.863; 11.142; 38.60%; +16.20% | RES l.204, l.766 | PASS |
| CON matched-half days, CCC | 80.1 to 84.8; 138.7 to 153.3; 138.9 to 148.3; 79.9 to 89.8 (+9.9) | 80.10 to 84.77; 138.66 to 153.27; 138.89 to 148.26; 79.87 to 89.78 (+9.91) | RES l.766, 770-772 col B; l.896-897, 910-911 | PASS |
| CON TTM CCC | 93.9 to 100.3 (+6.4) | 93.86 to 100.26 (+6.40) | as above | PASS |
| SA matched-half days, CCC | 75.2 to 75.4; 94.5 to 130.3; 123.5 to 139.9; 46.2 to 65.8 (+19.6) | 75.20 to 75.38; 94.53 to 130.34; 123.53 to 139.90; 46.20 to 65.82 (+19.62) | RES l.204, 208-210 col B; l.341-343, 357-358 | PASS |
| Brief: inventory days "up from about 139"; cash cycle "about 10 days" longer | 139; 10 | 138.66; 9.91 | derived | PASS |
| Government share change, reading A / B | +8.4 / -28.1 pp | +8.41 / -28.13 pp | PPT l.797-802; l.347 | PASS (bases differ, stated) |
| Q15 fixed-price value on the written PVC figure | 141-170 Cr | 141.45-169.74 | PPT l.189, l.182 | PASS |
| Q28 four Hyderabad "company" orders | 101.70; 18.0% of book | 101.70; 17.97% | PPT l.208-217; l.189 | PASS |
| F1 opening-claims share | 9 / 23 = 39.1% | 39.13% | review l.570-592 | PASS |
| F2 specificity | 31 / 61 = 0.51; 28 / 57 = 0.49 | 0.508; 0.491 on A4's population; 0.500 or 0.492 after M7 | review l.791-794 | PASS on the stated population; denominator moves with M7 |
| Section A tables outside the changed sections | unchanged | unchanged | loop-0 rows 1-48 | PASS |

## L1-4. New STYLE notes (logged; no re-run)

- S12. The R326 structured context reads "turn near T55", but CC l.383 sits in T61 (lines 380-384). The ledger has T61, which is correct.
- S13. The ledger note on R326 cites R186 at "l.224/252 area". R186 is at CC l.251.
- S14. The ledger's section 2 turn map was not updated for T38 (R324, R325) and T61 (R326). The additions table carries the turns.
- S15. The brief at review l.963 says "About a fifth of the group rise came from Danya Electric". The swing is the CON-minus-SA gap, which is Danya's external sales net of intra-group eliminations. "Came through Danya's consolidation" is more exact.
- S16. The watchlist at review l.418 tags only the Q1 figures as Spear memory. The FY26 "190 last guide" figure is memory too.
- S17. CC l.90-91 is a borderline forward unit; its substance is restated in R171-R172.
- S18. CC l.497 is a borderline forward unit (present tense); bushing supply is rowed in R222-R223.

## L1-5. Loop 1 verdict

**INCOMPLETE.** Loop back to **A2**, for M7 (MISSING) only. All ten loop-0 findings are CLEARED: F1, F2, C1, C2 and M1-M6. Nothing in A4's Section A arithmetic, cash ruling, flags or protocol verdict (PROCEED WITH FLAGS) changes.

The expected downstream work is small:
- A2 raises MISSING_FROM_STRUCTURED for T17 CC l.206-207.
- A1 adds one or two FORWARD rows.
- A3 should find nothing new.
- A4 changes two places: the Step 6B population and ratio (0.50 or 0.49, INDETERMINATE label unchanged), and the 7A row citation at l.817.

---

Loop 1 YAML block, SUPERSEDED by the Loop 2 block at the end of this file:

```yaml
stage: A5-adversary
company: "SUPREMEPWR"
quarter: "h1fy27"
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
  missing_from_ledger:
    - {doc: "concall", fulltext_line: "206-207", turn: "T17", unit: "management forward claim: 'So whatever the price escalates it will be covered. The margin will not affect much'; no FORWARD row (R120 rows only the three-decades number on l.207; R314 rows the PVC coverage at l.203)", type: "MISSING", loop: "A2"}
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing:
    - "M7 [A2] Concall T17 l.206-207 management forward margin claim has no structured or ledger FORWARD row; A1 convention rows every instance (R180, R212, R221, R326); A4 already tests it (review l.817), so only the spine and the Step 6B population move (31/62 = 0.50 or 31/63 = 0.49; INDETERMINATE label holds)"
  contradiction: []
  style:
    - "S1-S5 open from loop 0 (A1/A2 cosmetic, category-level marking); S6-S11 applied by A4"
    - "S12 R326 structured context says 'turn near T55'; l.383 is in T61 (ledger correct)"
    - "S13 Ledger R326 note cites R186 at 'l.224/252'; R186 is at l.251"
    - "S14 Ledger turn map for T38 and T61 not updated with R324-R326; additions table carries the turns"
    - "S15 Brief l.963 'came from Danya': the swing is CON-minus-SA, i.e. through Danya's consolidation net of intra-group eliminations"
    - "S16 Watchlist l.418 tags only the Q1 figures as Spear memory; FY26 '190 last guide' is memory too"
    - "S17 CC l.90-91 borderline forward unit; substance restated in R171-R172"
    - "S18 CC l.497 borderline forward unit (present tense); bushing supply rowed in R222-R223"
loop_back_to: "A2"
gap: "A2: raise MISSING_FROM_STRUCTURED for concall T17 l.206-207 so A1 adds one or two FORWARD rows ('So whatever the price escalates it will be covered'; 'The margin will not affect much'). A4: add the row(s) to the Step 6B population (62 or 63; ratio 31/62 = 0.50 or 31/63 = 0.49; INDETERMINATE label unchanged) and cite them in Step 7A l.817. No other change expected; A3 should find no new forensic content."
style_notes:
  - "S12-S18 new in loop 1; S1-S5 still open; S6-S11 applied. Logged only, no re-run"
analyst_note: "Loop 1 re-audit. All ten loop-0 findings are cleared: F1, F2, C1, C2 and M1-M6 each verified against the fulltexts, structured rows and ledgers, and every changed number recomputed (swing shares 22.7% and 38.6%, CON and SA matched-half days, specificity 31/61, Q15 and Q28 values, government-share shifts). One new gap remains. Management's T17 margin claim at concall l.206-207 has no FORWARD row. My loop-0 pass checked concall numbers line by line but only sampled forward statements, so it missed this line and l.383, which A1 has since added as R326. This loop swept every management turn. The gap is narrow: A4 already tests the claim against the filing (review l.817), so only the spine and the Step 6B denominator change (0.50 or 0.49), and the INDETERMINATE archetype holds. The verdict, the cash cap and every flag stand. The loop to A2 is rule-mandated; no new forensic content is expected downstream."
```

---

# LOOP 2 RE-AUDIT (24-Oct-2026, final; no further loop is permitted)

Scope. Correction loop 2 changed three inputs:
- The A4 review has a loop 2 change list at review l.8-21.
- The concall structured file now runs R001-R344. R327-R344 are 18 FORWARD rows appended in loop 2 (structured l.463-483). The header now reads FORWARD 80, total 344.
- The concall ledger accounts for 344 of 344 IDs, with forward rows 80 and management numbers 95 (ledger l.3-11, l.518-537).

The other three structured files and ledgers are unchanged. Input discipline is the same as before. Line anchors in this section ("review l.N") refer to the loop-2 revision of the review. Before this section, I changed only the two labels above the earlier YAML blocks, which now point to the Loop 2 block as the one that governs.

## L2-1. Per-finding clearance

| ID | What was checked | Evidence | Status |
|---|---|---|---|
| M7 | The T17 claim at CC l.206-207 has a structured row, a ledger row and review citations | CC-R327 (structured l.466: "So whatever the price escalates it will be covered. The margin will not affect much", T17). Ledger l.520 (T17, l.206-207). Cited at review l.676 (Q&A row 5), l.732 and l.735 (Exchange 2), l.841 (7A), l.893, l.927-928 (Section C), l.941 (flag 7), l.1073 (Q15) | CLEARED |
| F2 follow-on: quantified classification | Each of the 79 rows checked against A4's stated counting rule (review l.801) | Population 61 + 1 + 18 = 80, less R206 = 79 (l.805). 35 QUANTIFIED + 44 UNQUANTIFIED = 79, each row once (l.808-809). New rows checked one by one: R331 (80% PVC), R337 ("1% to 100%", garbled but with a referent), R339 (160-200 MVA) and R340 (230 kV / 110 kV) are QUANTIFIED. The other 14 carry no number, named period or binary event in their own text: R333's "January" sits only in the context column, and R344's "one month" sits in NUMBER row R118. All consistent | CLEARED |
| F2 follow-on: all-rows ratio | Arithmetic | 35 / 79 = 0.4430. Sensitivity: 34 / 79 = 0.4304; 36 / 79 = 0.4557 (l.814-816) | CLEARED |
| F2 follow-on: ex-restated ratio and the EVASIVE label | A4's restatement rule (l.803) applied row by row to the 23-row restated list (l.811) | Four rows fail the rule's ordering test (finding F3). With those four corrected, the ex-restated ratio is 28 / 60 = 0.467, inside the 0.05 band. The 6E statement that "Both sit more than 0.05 below the 0.5 line" (l.832, also l.914, l.948, l.1126) does not hold | **NOT CLEARED (F3)** |
| S15, S16 | Applied by A4 | l.262, l.988, l.1010 ("through Danya's consolidation"); l.431 ("190 last guide, Spear memory") | CLEARED (STYLE) |
| S17, S18 | Applied | l.817: CC l.90-91 is not counted; CC l.497 is now R341 | CLEARED (STYLE) |
| S12-S14 | A1/A2 artefacts | R326 context still reads "turn near T55" (structured l.461); ledger maps unchanged | OPEN (STYLE, logged) |

## L2-2. New finding

- **F3 (FACTUAL, loop A4).** The ex-restated specificity cross-check misapplies the restatement rule A4 states. A4's rule (review l.803): "a row is a restatement if management states the same claim again on the call, with the same figure where one is given, after an earlier forward row already carries it." Four rows on A4's restated list (l.811) fail the "earlier forward row" test.
  - **R331** (CC l.165-167, "expected margin ... almost 80% is covered with PVC") is listed as a repeat of R178 and R179. Those rows sit at CC l.168 and l.172, later on the call. No earlier forward row (R165-R177, R329, R330) carries a PVC or margin claim.
  - **R334** (CC l.248-250, power-transformer uplift absorbed by overheads) is listed as a repeat of R186 and R076. R186 sits at CC l.251, later. R076 is a NUMBER row.
  - **R339** (CC l.466-467, data-centre units above 160-200 MVA) is listed as a repeat of R213 with R104. R213 sits at CC l.469, later. R104 is a NUMBER row.
  - **R340** (CC l.493-494, bushing supply constrained only above 230 kV) is listed as a repeat of R222 with R110-R112. R222 sits at CC l.502, later. R110-R112 are NUMBER rows.
  - Three of these four are QUANTIFIED (R331, R339, R340). Taking them out of the restated list gives 19 restated rows, 7 of them quantified. The ex-restated ratio becomes (35 - 7) / (79 - 19) = 28 / 60 = 0.467. That sits inside the 0.45-0.55 INDETERMINATE band, against A4's 25 / 56 = 0.446. A4's own figure was only 0.004 outside the band.
  - The other calls on the list are judgement, and across them the cross-check spans 0.44 to 0.48. R333, R336 and R343 are tagged as repeats of rows that make different claims. R179 ("expected margin can be achieved", CC l.172) arguably repeats R178 (CC l.168) and is not marked. R341 is valid as a repeat of R340 once R340 is treated as the first statement.
  - The all-rows ratio (0.443) and the per-row classification are right. The error sits in the ex-restated cross-check and in the label argument built on it. Review l.832 says "Both sit more than 0.05 below the 0.5 line, so the INDETERMINATE band no longer applies". The same claim appears at l.914, l.948 and l.1126. On A4's own rule, the cross-check sits inside the band. So the EVASIVE label holds only if the all-rows ratio governs the label, which A4 did in loop 1 but does not state now.
  - Fix (text only; no new evidence and no A1/A2/A3 work):
    - In Step 6B (l.811), take R331, R334, R339 and R340 off the restated list, and show the ex-restated ratio as 28 / 60 = 0.467.
    - Update the sensitivity line (l.816): the corrected cross-check also lands inside the band.
    - In 6E (l.832), Step 9 (l.914), flag 14 (l.948) and the YAML flag (l.1126), replace "both sit more than 0.05 below the 0.5 line" with: "the all-rows ratio (0.443) governs the label, as in loop 1; the ex-restated cross-check (0.467) sits inside the band, so the provisional EVASIVE label is fragile".
    - Alternatively, label INDETERMINATE because the two variants straddle the band edge.

Effect: none on the protocol verdict (PROCEED WITH FLAGS), the cash cap, or any flag other than the provisional archetype (flag 14), which A4 itself marks "not of record".

## L2-3. Coverage re-run (changed sections)

| Doc | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Concall | Forward rows | 80 | 80 rowed. Every unit that meets the forward definition (future tense, expectation, commitment) now has a row; T17 CC l.206-207 is R327 | 0 (R327-R344 cited at review l.392-397, l.447-449, l.509, l.515, l.518-519, l.622-630, l.639, l.672-709, l.732-765, l.841-850, l.867-868, l.893, l.927-941, l.962-973) | PASS |
| Concall | Management numbers | 95 | 95 | 0 | PASS |
| Concall | ID accountability | 344 / 344 | 344 | 0 | PASS |
| Concall | Turns / questions / entities / dates / qualifiers / zero | 99 / 41 / 43 / 25 / 73 / 1 | unchanged | 0 | PASS |
| Results / presentation / press release | ID accountability | 609 / 747 / 166 | unchanged files | 0 | PASS |

No unit that meets the forward definition lacks a row. M7 is closed.

Brief gate re-check. All five parts are present (review l.987-1031). The summary is about 240 words, inside 200-400. The forward map is unchanged from loop 1. Gate: PASS.

## L2-4. Arithmetic re-run (changed sections)

| Metric | A4 value | A5 recomputed | Source line | Status |
|---|---|---|---|---|
| Forward population | 80; less R206 = 79 | 61 (R165-R225) + 1 (R326) + 18 (R327-R344) = 80; 79 | structured l.5, l.463-483; ledger l.11 | PASS |
| Quantified / unquantified | 35 / 44 | 35 / 44; total 79 | review l.808-809 | PASS |
| All-rows specificity | 35 / 79 = 0.443 | 0.4430 | review l.814 | PASS |
| Sensitivity variants | 34 / 79 = 0.430; 36 / 79 = 0.456 | 0.4304; 0.4557 | review l.816 | PASS |
| Ex-restated specificity | (35 - 10) / (79 - 23) = 25 / 56 = 0.446 | 28 / 60 = 0.467 on A4's stated rule (four ordering corrections); 0.44-0.48 across the judgement calls | review l.811, l.815 | **FAIL (F3)** |
| Loop history | 0.37 / 0.51 / 0.44 | 22/60 = 0.367; 31/61 = 0.508; 35/79 = 0.443 | review l.818 | PASS |

## L2-5. New STYLE notes (logged; no re-run)

- S19. The A2 ledger's RESTATED tags for R327-R344 (ledger l.520-537) differ from A4's restated list in places. For example, R330 is tagged to R165 in the ledger but to R169 in A4. R327 is tagged RESTATED in the ledger, while A4 treats it as new substance. The ledger flag is an enumeration flag, not A4's ordered rule, so this is cosmetic.
- S20. A1's loop-2 sweep rowed some present-tense outlook statements as FORWARD (R328, R329, R340, R341, R343). It did not row the parallel opening-remark statements at CC l.92-98. Under the forward definition this is not a coverage miss. If those statements were rowed (all unquantified), the all-rows ratio would be 35 / 82 = 0.427, and the label would not change.
- S21. Step 7A (review l.841) cites R327 at "l.203-207". R327 sits at CC l.206-207; l.203 is R032 and R314.

## L2-6. Final verdict

**INCOMPLETE.** The failing agent is **A4**, for F3 (FACTUAL) only.
- M7 is CLEARED, and all ten loop-0 findings stay cleared.
- The remaining gap is text-only, and its exact replacement wording is given above.
- It touches only the provisional, not-of-record archetype label and its cross-check. The protocol verdict (PROCEED WITH FLAGS), the cash cap and every other flag stand.
- No loop is permitted after this one, so F3 stays an open item for the operator, with the fix stated in full.

---

```yaml
stage: A5-adversary
company: "SUPREMEPWR"
quarter: "h1fy27"
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
  - {metric: "Role 5 Step 6B ex-restated specificity ratio", a4_value: "25/56 = 0.446 (23 restated rows, 10 quantified)", recomputed: "28/60 = 0.467 on A4's stated restatement rule: R331, R334, R339, R340 are first statements (cited originals R178/R179, R186, R213, R222 come later on the call; R076, R104, R110-R112 are NUMBER rows), so 19 restated rows, 7 quantified; 0.44-0.48 across the judgement calls (R333, R336, R343, R179)", source_line: "review l.803, l.811, l.815; CC l.165-172, l.248-251, l.466-469, l.493-502"}
surviving_bear_counters: []
findings_by_type:
  factual:
    - "F3 [A4] Ex-restated specificity cross-check misapplies A4's own restatement rule (four rows tagged as repeats of later or NUMBER rows); corrected 28/60 = 0.467 sits inside the 0.05 band, so the 6E claim 'both sit more than 0.05 below the 0.5 line' (review l.832, l.914, l.948, l.1126) fails; all-rows 35/79 = 0.443 is correct; EVASIVE holds only if the all-rows ratio governs, which A4 must state, else INDETERMINATE"
  missing: []
  contradiction: []
  style:
    - "S12-S14 open (A1/A2 artefacts: R326 turn label, R186 line cite, ledger turn map)"
    - "S19 Ledger RESTATED tags for R327-R344 differ from A4's restated list (e.g. R330, R327); enumeration flag, cosmetic"
    - "S20 A1 rowed some present-tense outlook statements as FORWARD (R328, R329, R340, R341, R343) but not the parallel CC l.92-98; not a miss under the forward definition; adding them gives 35/82 = 0.427, label unchanged"
    - "S21 Step 7A l.841 cites R327 at l.203-207; R327 is l.206-207"
loop_back_to: "A4"
gap: "A4 (text-only; no loop remains, so this is an open item for the operator): in Role 5 Step 6B (review l.811, l.815-816) take R331, R334, R339 and R340 off the restated list, show the ex-restated ratio as (35-7)/(79-19) = 28/60 = 0.467, and note it sits inside the 0.05 band. In 6E (l.832), Step 9 (l.914), flag 14 (l.948) and the YAML flag (l.1126), replace 'both sit more than 0.05 below the 0.5 line' with 'the all-rows ratio (0.443) governs the label, as in loop 1; the ex-restated cross-check (0.467) sits inside the band, so the provisional EVASIVE label is fragile', or label INDETERMINATE. No other change; protocol verdict, cash cap and other flags unaffected."
style_notes:
  - "S19-S21 new in loop 2; S12-S14 still open; S15-S18 applied. Logged only, no re-run"
analyst_note: "Loop 2 final re-audit. M7 is cleared: CC-R327 carries the T17 margin claim at l.206-207, the ledger holds 344/344 with forward 80, and the review cites R327 wherever it tests margin protection. Coverage of the changed sections is clean; no forward unit lacks a row. The per-row quantified classification follows A4's stated rule, and the all-rows ratio is right: 35/79 = 0.443. The ex-restated cross-check is not. A4's own restatement rule needs an earlier forward row carrying the claim. Four rows break that test: R331, R334, R339 and R340 are each tagged as repeats of rows that come later on the call or of NUMBER rows. Correcting only those four gives 28/60 = 0.467, inside the 0.05 band, so the 6E claim that both ratios sit more than 0.05 below 0.5 fails. The EVASIVE label then rests on the all-rows ratio alone. The fix is text-only: correct the list, show 0.467, and state that the all-rows ratio governs, or label INDETERMINATE. The archetype is provisional and not of record; the protocol verdict, the cash cap and every other flag stand. No loop remains, so this is an open item for the operator."
```
