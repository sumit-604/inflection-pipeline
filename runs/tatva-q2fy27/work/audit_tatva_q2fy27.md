# A5 ADVERSARY / COMPLETENESS AUDIT: Tatva Chintan Pharma Chem Limited (TATVA), Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-20
Read: A4 review (merged file, 810 lines; part 2 starts at REV L358 and equals parts/review_tatva_q2fy27.part2.md, offset 357), the three A1 fulltexts, the three A1 structured files, the three A2 ledgers.
Not read: source PDFs, anything under inputs/, A3 forensics files, orchestrator commentary.

Anchors. REV L### = runs/tatva-q2fy27/work/review_tatva_q2fy27.md. RES / PPT / NTC L### = A1 fulltext line. LED-R / LED-P / LED-N L### = A2 results / presentation / notice ledger line. The filing is in Rs Mn; Rs Cr = Mn x 0.1. Every recomputation below starts from the Mn cell in the fulltext.

---

## AUDIT 0: DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (REV L660-L672, six paragraphs, about 290 words) | sector PRESENT (REV L674-L680) | business model PRESENT (REV L682-L688) | competition PRESENT (REV L690-L695) | forward map PRESENT (REV L697-L714: 12 catalysts, each with a bull fork and a bear fork; 10 dated; 2 undated because no date exists: the call reschedule, NTC L39-40, and operator rulings 50/51).

Gate result: PASS. All five parts carry real content.

---

## AUDIT 1: COVERAGE

Method. I re-ran the enumeration on the A1 fulltexts with my own grep pass. I did not use A2's counts as input. Then I diffed my counts against each ledger, checked that every structured row ID sits in a ledger, and checked that every ledger row is cited in A4 or covered by an explicit "reviewed" declaration. A2-flagged rows were checked one by one for an A4 disposition.

| Doc | Category | A2 count | A5 fresh count (method, lines) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | pages | 14 | 14 ("[page N]" markers) | 0 | PASS |
| Results | numbered notes | 13 | 13 (cons RES L345, L350, L353, L357, L359, L368, L371; std RES L633, L635, L637, L639, L641, L643) | 0 | PASS |
| Results | line items | 241 | 243 table data rows: 255 lines carry " \| " (grep), minus 9 COLUMNS lines (RES L142, L197, L261, L311, L361, L444, L488, L550, L600), minus the header comment (RES L16) and 2 auditor e-mail lines (RES L111, L433). The 2 extra rows are "Other equity excluding revaluation reserve" (RES L184, L475). A2 holds them as R241 and R654 in ledger section 3 (LED-R L383, L388) | 0 | PASS (reconciled; category placement only) |
| Results | ZERO_STANDING cells | 69 on 29 lines | 69 on 29 lines (dash cells counted line by line, RES L158 to L617) | 0 | PASS |
| Results | agenda items | 1 | 1 (RES L35-L41: results approval only) | 0 | PASS |
| Results | auditor report paragraphs | 10 | 10 (cons paras 1-6 RES L76, L83, L90, L100, L103, L115; std paras 1-4 RES L389, L395, L403, L413) | 0 | PASS |
| Results | consolidation entities | 3 | 3 (RES L105-L107) | 0 | PASS |
| Results | structured row IDs | 1,090 | 1,090 (grep "^R\d+ \|" on the structured file) | 0 | PASS |
| Presentation | slides | 42 | 42 ("[page N]" markers) | 0 | PASS |
| Presentation | structured row IDs | 738 | 738 (grep) | 0 | PASS |
| Presentation | superseded IDs | 24 | 24 (R165-R169 = 5, R622-R627 = 6, R642-R650 = 9, R692-R695 = 4) | 0 | PASS |
| Presentation | version-diff units | 5 | 5 (PPT L17-L20: p1 letter, p2 annexure, RoE, Debt/EBITDA, p14 note 2) | 0 | PASS |
| Presentation | numbers on text slides (fresh sweep of p1, p2, p18, p20-p24, p28, p29, p36, p38-p40, p42; image lines PPT L1106-L1110) | 591 (A2 grep side = A1 header totals, LED-P L17) | every data point found in the structured file, for example "100 bar" PPT L856 = R621; leadership experience years PPT L1051-L1059 = R688; address block PPT L1098-L1105 = R710; Dahej capacity PPT L813-L826 = R594-R613 | 0 | PASS |
| Notice | structured row IDs | 28 | 28 (7 numbers, 8 entities, 2 forward, 7 dates, 4 qualifiers; read in full) | 0 | PASS |
| All | ledger rows absent from A4 | n/a | 0. A4 cites all 13 notes (REV L56-L64), the agenda item and meeting time (REV L78), the auditor paragraphs and entity scope (REV L68), and declares all 1,856 IDs reviewed by range (REV L16: results 1,090 incl. R1049-R1090; presentation 738 incl. 24 superseded; notice 28). 1,090 + 738 + 28 = 1,856, matching my grep | 0 | PASS |

A2 flag disposition in A4:

| A2 flag (ledger line) | Rows | A4 disposition | Status |
|---|---|---|---|
| DIVIDEND_PAID_DIFF / CROSS_ENTITY_DIFF (LED-R L24, L167, L300) | R407-R409, R816-R818 | REV L335 (RES-A3-09) | PASS |
| RECLASS_UNQUANTIFIED (LED-R L37) | R1018, R1048 | REV L62, L337 | PASS |
| LONG_MEETING_NO_AGENDA, MEETING_TIME (LED-R L394) | R008-R009 | REV L78 | PASS |
| SIGNATURE_TS (LED-R L365) | R010 | REV L79 | PASS |
| ZERO_STANDING exceptional (LED-R L64, L210) | R095-R100, R574-R579 | REV L64, L109 | PASS |
| RESTATED Note 5 (LED-R L189-L193) | R466-R495 | REV L60 | PASS |
| MISSING_FROM_STRUCTURED, resolved (LED-R L435-L453) | R1049-R1090 | REV L16, L106, L149 | PASS |
| LABEL_ANOMALY "Net decrease" caption on positive values (LED-R L45, L174, L307) | R428-R430, R837-R839, R1005, R1040 | not disposed by name | STYLE S4 (cosmetic, no number) |
| VERSION_DIFF V1-V5 (LED-P L19-L24) | R002-R019, R171, R207, R217 | REV L83, L555 | PASS |
| SUPERSEDED (LED-P L28-L33) | 24 IDs | REV L16 | PASS |
| LABEL_MISMATCH (LED-P L826) | R543, R550 | REV L436, L555 | PASS |
| LAYOUT_SCRAMBLED, CHART_ORDER_UNRESOLVED (LED-P L33) | p11-p16, p26, p28 | REV L22 | PASS |
| NO_NEW_DATE, REASON_UNSPECIFIED (LED-N L34, L44) | R017, R025 | REV L80, L549 | PASS |
| ANCHOR_CORRECTED (LED-N L12) | R014 | A4 lists other anchor offsets (REV L23); no conflict with A2. I confirmed A2's correction: "Scrip Symbol: TATVA" is on NTC L26 | PASS |

Coverage result: PASS. Orphan rows: none. Rows my pass found that the ledgers lack: none.

---

## AUDIT 2: ARITHMETIC

Every derived metric in A4's tables recomputed from the Mn cells. Tolerance: plus or minus 1 in the last printed digit.

| # | Metric (REV line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | Cons op EBITDA Q2 FY27 (REV L122) | 40.69 | 289.40 + 107.94 + 27.09 - 17.54 = 406.89 Mn | RES L146, L153, L154, L157 | PASS |
| 2 | Cons op EBITDA Q1 FY27, post-exc (REV L122) | 32.30 (30.98) | 322.96 (309.78) Mn | RES L146-L158 | PASS |
| 3 | Cons op EBITDA Q2 FY26 / H1 FY27 / H1 FY26 / FY26 | 22.22 / 72.99 / 39.55 / 93.16 | 222.15 / 729.85 / 395.45 / 931.58 Mn | RES L146-L157 | PASS |
| 4 | Cons op EBITDA margin, 6 periods (REV L123) | 17.99 / 19.33 / 18.72 / 16.45 / 18.99 / 18.42 | 17.986 / 19.333 / 18.723 / 16.451 / 18.988 / 18.416 | RES L145 | PASS |
| 5 | Reported EBITDA, 6 periods (REV L124) | 23.22 / 35.08 / 42.44 / 41.71 / 77.52 / 96.71 | 232.23 / 350.76 / 424.43 / 417.08 / 775.19 / 967.07 Mn | RES L153-L157 | PASS |
| 6 | Core PBT ex-OI, 6 periods (REV L125) | 12.66 / 19.65 / 27.19 / 20.60 / 46.84 / 53.46 | 126.55 / 196.49 / 271.86 / 206.01 / 468.35 / 534.60 Mn | RES L146, L157 | PASS |
| 7 | OI / PBT pre-exc (REV L126) | 7.38 / 12.39 / 6.06 / 9.50 / 8.83 / 6.23 | 7.378 / 12.395 / 6.061 / 9.502 / 8.826 / 6.225 | RES L146, L157 | PASS |
| 8 | ETR (REV L127) | 27.42 / 24.30 / 25.88 / 27.22 / 25.21 / 26.23 | 27.417 / 24.300 / 25.878 / 27.219 / 25.212 / 26.233 | RES L159, L163 | PASS |
| 9 | PAT margin (REV L128) | 8.03 / 9.57 / 9.87 / 6.89 / 9.74 / 8.31 | 8.029 / 9.566 / 9.871 / 6.892 / 9.738 / 8.313 | RES L145, L164 | PASS |
| 10 | Gross margin (REV L129) | 55.58 / 54.93 / 51.11 / 52.90 / 52.77 / 55.61 | material 548.62 / 752.91 / 1,062.52 / 1,132.08 / 1,815.43 / 2,245.39 Mn; GM 55.583 / 54.930 / 51.108 / 52.904 / 52.769 / 55.612 | RES L149-L151 | PASS |
| 11 | Employee and other-expense ratios (REV L131-L132) | 12.10 / 10.02 / 8.39 / 12.08 / 9.10 / 12.44; 25.50 / 25.58 / 24.00 / 24.38 / 24.68 / 24.76 | 12.101 / 10.018 / 8.388 / 12.078 / 9.097 / 12.441; 25.496 / 25.580 / 23.997 / 24.376 / 24.685 / 24.756 | RES L152, L155 | PASS |
| 12 | Std op EBITDA, 6 periods (REV L163) | 21.11 / 24.03 / 31.23 / 36.18 / 55.26 / 89.33 | 211.09 / 240.25 / 312.33 / 361.76 / 552.58 / 893.30 Mn | RES L448, L455, L456, L459 | PASS |
| 13 | Std op EBITDA margin (REV L164) | 18.22 / 16.38 / 15.05 / 16.08 / 15.60 / 18.00 | 18.219 / 16.377 / 15.053 / 16.075 / 15.601 / 17.999 | RES L447 | PASS |
| 14 | Std reported EBITDA, core PBT, OI/PBT, ETR, PAT margin, GM (REV L165-L170, 36 cells) | e.g. Q2: 33.94 / 17.73 / 13.24 / 24.71 / 7.42 / 47.31 | 339.38 Mn / 177.32 Mn / 13.236 / 24.710 / 7.416 / 47.311 | RES L447-L466 | PASS (all 36) |
| 15 | PAT gap cons - std (REV L179) | 0.98 / 5.54 / 6.06 / 2.49 / 11.60 / 2.97 / 0.48 | 9.76 / 55.35 / 60.64 / 24.94 / 115.99 / 29.72 / 4.78 Mn | RES L164, L466 | PASS |
| 16 | Gap % of std PAT (REV L180) | 10.9 / 53.0 / 39.4 / 17.7 / 44.9 / 7.6 / 1.9 | 10.92 / 52.99 / 39.41 / 17.72 / 44.90 / 7.60 / 1.91 | RES L164, L466 | PASS |
| 17 | Gap % of cons PAT; parent share (REV L181-L182) | 9.8 / 34.6 / 28.3 / 15.1 / 31.0 / 7.1 / 1.9 | 9.84 / 34.63 / 28.27 / 15.05 / 30.99 / 7.07 / 1.88 | RES L164, L466 | PASS |
| 18 | Revenue, op EBITDA, OI gaps (REV L176-L178) | Q2: 9.84 / 9.46 / 0.95; H2 FY26: (5.78) / 0.46 / (0.02) | 98.36 / 94.56 / 9.51; -57.75 / 4.59 / -0.21 Mn | RES L145-L146, L447-L448 | PASS |
| 19 | Std op margin H2 FY26 (REV L183, L189) | 19.60% | 531.54 / 2,712.53 = 19.596% | RES L447, L459 | PASS |
| 20 | Shell read: inventory, receivable, OCL, cash gaps (REV L187) | 24.50 / 10.49 (24.69 at Mar) / 16.89 / 5.33 | 245.02 / 104.94 (246.88) / 168.94 / 53.31 Mn | RES L213/L504, L215/L506, L244/L533, L216/L507 | PASS |
| 21 | Std GM fall QoQ / YoY (REV L189) | 738 / 810 bps | 54.689 to 47.311 = 7.38 pp; 55.409 to 47.311 = 8.10 pp | RES L451, L453 | PASS |
| 22 | Cons YoY growth rates (REV L201-L211) | +75.9 / +83.2 / +19.2 / +434.3 / +127.1 / +74.0 / +114.8 / +111.8 / +116.3 / +116.3 | +75.94 / +83.16 / +19.23 / +434.32 / +127.13 / +74.01 / +114.82 / +111.81 / +116.31 / +116.27 | RES L145-L181 | PASS |
| 23 | Margin change YoY / QoQ (REV L203, L226) | +74 / -61 bps | +73.7 / -61.0 bps | RES L145 | PASS |
| 24 | Cost-ratio change YoY (REV L226) | material +447, employee -371, other -150 bps | +447.5 / -371.3 / -149.9 bps | RES L149-L155 | PASS |
| 25 | Std YoY (REV L217-L221) | +79.1 / +48.0 / -317 bps / +53.5 / +72.1; OI +1.91 | +79.08 / +47.96 / -316.6 bps / +53.54 / +72.09; 19.11 Mn | RES L447-L466 | PASS |
| 26 | H1 revenue YoY (REV L225) | +59.9% | +59.90% | RES L145 | PASS |
| 27 | Q1 FY26 derived (REV L242) | 116.86 / 14.83% / 7.95 | 1,168.64 Mn; 173.30 / 1,168.64 = 14.829%; 79.46 Mn | RES L145-L157 | PASS |
| 28 | H2 FY26 block (REV L246) | 265.48 / 20.19% / 32.86 | 2,654.78 Mn; 536.13 / 2,654.78 = 20.195%; 328.59 Mn | RES L145-L157 | PASS |
| 29 | QoQ run-rates (REV L243-L248) | +5.7 / +7.5 / +25.9 / +30.1 | +5.69 / +7.47 / +25.85 / +30.09 | RES L145 | PASS |
| 30 | H1 average, Q2 premium, Q2 annualised (REV L253-L254) | 192.19 / +13.1% / 869.28 | 1,921.875 Mn; +13.08%; 8,692.80 Mn | RES L145 | PASS |
| 31 | PAT bridge components (REV L267-L277) | +16.87 / +1.60 / -1.74 / -2.20 / +0.75 / -4.19 / +0.45; total 11.53 | 168.71 / 16.03 / -17.41 / -22.02 / +7.46 / -41.89 / +4.46 Mn; total 115.34 Mn = 214.51 - 99.17 | RES L145-L164 | PASS |
| 32 | Bridge shares of PAT change (REV L267-L273) | 146.3 / 13.9 / -15.1 / -19.1 / 6.5 / -36.3 / 3.9% | same to one decimal | RES L145-L164 | PASS |
| 33 | OI after tax; PAT if OI reverts (REV L280-L281) | 0.55, 4.8%; 20.90 | 7.46 x (1 - 0.25878) = 5.53 Mn, 4.79%; 214.51 - 5.53 = 208.98 Mn | RES L146, L163 | PASS |
| 34 | Deferred tax share H1, cons / std (REV L283) | 56.8% / 79.7% | 71.70 / 126.19 = 56.82%; 69.29 / 86.98 = 79.66% | RES L162-L163, L464-L465 | PASS |
| 35 | DTA cons / std (REV L283) | 9.57 to 1.92 / 8.17 to 0.77 | 95.67 to 19.21 / 81.68 to 7.65 Mn | RES L209, L500 | PASS |
| 36 | Cash-tax step-up (REV L283) | about Rs 3.5 Cr a quarter | 69.29 / 2 = 34.6 Mn | RES L464 | PASS |
| 37 | H1 summary (REV L285) | +84.6 / +254 bps / +127.3 / +125.9 | +84.56 / +253.7 bps / +127.34 / +125.93 | RES L145-L164 | PASS |
| 38 | Cons CFO and ratios (REV L299-L301) | (3.68); CFO/PAT -9.8 (80.8, 74.9); CFO/EBITDA -5.0 (33.8, 33.8) | -36.76 Mn; -9.82 / 80.76 / 74.88; -5.04 / 33.84 / 33.80 | RES L289 | PASS |
| 39 | Pre-WC profit absorbed (REV L302) | 72.73 of 73.47 = 99.0% | 727.30 / 734.67 = 98.997% | RES L273, L286 | PASS |
| 40 | Cash generated, change (REV L302) | -18.43 | 7.37 - 191.74 = -184.37 Mn = -18.44 | RES L287 | PASS (difference of rounded inputs) |
| 41 | Capex; FCF; FCF change (REV L303-L304) | 30.85; (34.52) / (42.62) / (82.29); +8.10 | 308.45; -345.21 / -426.18 / -822.85 Mn; +80.97 Mn | RES L289, L291 | PASS |
| 42 | FCF negative for a third half-year (REV L304) | yes | H2 FY26 = -822.85 + 426.18 = -396.67 Mn | RES L289, L291 | PASS |
| 43 | WC lines (REV L305) | (72.73); inventories (52.84); receivables (63.93); payables +33.19 | 727.30; 528.36; 639.29; 331.94 Mn | RES L275-L286 | PASS |
| 44 | Cons receivable days (REV L306) | 85.9 / 84.9 / 100.2 / 74.9 | 1,190.31 / 5,058.58 x 365 = 85.89; 1,783.77 / 3,843.75 x 183 = 84.92; / 6,498.53 x 365 = 100.19; / 8,692.80 x 365 = 74.90 | RES L145, L215 | PASS |
| 45 | Inventory days (REV L307) | 318.7 / 310.2; on revenue 139.8 / 141.5 | 1,960.74 / 2,245.39 x 365 = 318.73; 2,489.10 / 2,928.74 x 365 = 310.21; 139.80; 141.48 | RES L149-L151, L213 | PASS |
| 46 | Payable days; CCC; payables rise (REV L308-L309) | 94.7 / 106.6; 309.9 / 303.8; +27.28 | 582.46 / 2,245.39 x 365 = 94.68; 855.24 / 2,928.74 x 365 = 106.59; 309.9 / 303.8; 272.78 Mn | RES L241-L242 | PASS |
| 47 | Cons net debt; net debt / EBITDA (REV L312-L313) | 111.58 to 154.79; 1.20x / 1.22x / 1.06x | 1,115.82 to 1,547.90 Mn; 1.198 / 1.223 / 1.060 | RES L216-L217, L234, L240 | PASS |
| 48 | ST share of gross debt (REV L314) | 95.8% / 97.4% (165.53 of 169.99) | 95.84% / 97.37% (1,699.95 Mn = 170.00 Cr) | RES L234, L240 | PASS (169.99 vs 170.00 is rounding) |
| 49 | TTM revenue, op EBITDA, COGS (REV L317) | 649.85 / 126.60 / 292.87 | 6,498.53 / 1,265.98 / 2,928.74 Mn | RES L145-L157 | PASS |
| 50 | Sources and uses (REV L319) | 45.18; ST +50.13; cash +4.95 | 36.76 + 308.45 + 4.91 + 46.78 + 49.95 + 5.05 - 0.15 = 451.75 Mn; 501.27; 49.52 | RES L289-L321 | PASS |
| 51 | Std CFO, ratios, FCF (REV L325-L328) | (8.57); -33.2 / 85.3 / 74.6; -15.5 / 33.2 / 32.6; (39.42) / (43.99) / (84.60) | -85.70; -33.17 / 85.35 / 74.63; -15.51 / 33.20 / 32.65; -394.15 / -439.87 / -846.00 Mn | RES L578, L580 | PASS |
| 52 | Std receivable, inventory, payable days (REV L330-L332) | 105.7 / 97.6 / 110.2; 267.8 / 272.9; 90.6 / 103.1 | 105.70 / 97.58 / 110.22; 267.82 / 272.92; 90.55 / 103.10 | RES L447-L453, L504, L506, L530-L531 | PASS |
| 53 | Std net debt; ratio (REV L333) | 115.88 to 160.12; 1.48x / 1.30x | 1,158.75 to 1,601.20 Mn; 1.477 / 1.297 | RES L507-L508, L523, L529 | PASS |
| 54 | Dividend classification split (REV L335) | 4.68 / 0.86 / 3.82; (5.80) vs (1.97); std CFO (4.75); cons CFO (7.50) | 46.78 / 8.55 / 38.23; 57.95 vs 19.71; -85.70 + 38.23 = -47.47; -36.76 - 38.23 = -74.99 Mn | RES L282, L314, L571, L603 | PASS |
| 55 | Equity roll, Rs 2 a share (REV L335) | Rs 4.68 Cr both entities | cons 375.70 - 328.92 = 46.78; std 259.25 - 212.46 = 46.79; 46.78 / 23.392 = Rs 2.00 | RES L171, L227, L471, L518 | PASS |
| 56 | TTM PAT, TTM EPS (REV L397) | 62.92 / 26.90 | 629.18 Mn; 17.98 - 7.08 + 16.00 | RES L164, L181 | PASS |
| 57 | Net capital employed (REV L397) | 969.44 | 8,146.51 + 1,699.95 - 152.05 = 9,694.41 Mn | RES L216-L217, L230, L234, L240 | PASS |
| 58 | ROCE H1 annualised, incl OI / operating (REV L395) | 11.6% / 10.6% | 1,123.18 / 9,694.41 = 11.59%; 1,032.50 / 9,694.41 = 10.65% | RES L153, L154, L157 | PASS (10.65 at the rounding edge) |
| 59 | ROCE TTM, incl OI / operating (REV L461, L466) | 9.5% (Rs 92.34 Cr) / 8.9% | 923.35 / 9,694.41 = 9.52%; 864.15 / 9,694.41 = 8.91% | RES L146, L154, L157 | PASS |
| 60 | H2 margin needed for the 20-22% band (REV L435) | 20.9-24.7% | FY27 revenue 8,190.15 Mn; (1,638.03 - 729.85) / 4,346.40 = 20.89%; (1,801.83 - 729.85) / 4,346.40 = 24.66% | RES L145; band [memory] | PASS |
| 61 | ESS H2 need (REV L436) | Rs 26.8-36.8 Cr; 2.0-2.8x | 40 - 13.2; 50 - 13.2; 2.03-2.79x | PPT L674 | PASS |
| 62 | Asset turnover (REV L448) | 1.31x / 1.48x | 7,687.50 / 5,887.96 = 1.306; 8,692.80 / 5,887.96 = 1.476 | RES L145, L201-L202 | PASS |
| 63 | R&D intensity (REV L558) | Rs 4.59 Cr = 1.19%; FY26 Rs 7.83 Cr | 45.89 / 3,843.75 = 1.194% | PPT L1108 | PASS |
| 64 | 6D derived Q2 segments vs filed shares (REV L476-L481) | PTC 45.3 / SDA 96.8 / ESS 6.9 / PASC 66.3 | filed share x Rs 217.32 Cr, share +/-0.5 pp: PTC 44.6-46.7; SDA 96.7-98.9; ESS 5.4-7.6; PASC 64.1-66.3 | PPT L582, L614, L674, L705, L1106 | PASS (Q1 inputs are memory; consistent with filed shares) |
| 65 | SDA share of QoQ gain (REV L483) | Rs 39.0 of 50.26 Cr (78%) | QoQ gain 502.65 Mn = 50.27; 39.0 / 50.27 = 77.6% | RES L145 | PASS |
| 66 | Trailing P/E; CMP vs entry max (REV L500, L516) | 68.4x / 50.2x; 12.5x | 1,841 / 26.90 = 68.44; 1,841 / 36.68 = 50.19; 1,841 / 147 = 12.52 | RES L181; CMP [memory] | PASS |
| 67 | Filing-timeline gaps (REV L85, L549) | 56 min; 15 min; about 2 h | 17:00:00 - 16:03:53 = 56 min 7 s; 16:03:53 - 15:48:12 = 15 min 41 s; 18:05:26 - 16:03:53 = 2 h 1 min | NTC L58-L59; RES L60; PPT L17 | PASS |
| 68 | Restated-ratio basis checks (REV L555) | 2.64%; 4.30; FY26 RoE 5.4%; H1 4.6% (9.2% ann.) | 214.51 / 8,146.51 = 2.633%; 1,699.95 / 395.45 = 4.299; 420.54 / 7,817.59 = 5.38%; 374.32 / 8,146.51 = 4.59% (9.19%) | RES L164, L230, L234, L240; PPT L78-L79 | PASS (2.633 vs 2.64 is last digit) |
| 69 | Debt/EBITDA basis switch (REV L556) | FY23-FY25 incl OI; FY26 and H1 excl OI | FY23 1,702.57 / (605.81 + 57.44) = 2.57; FY24 143.01 / (681.96 + 75.09) = 0.19; FY25 363.88 / (342.13 + 23.15) = 1.00; FY26 1,203.73 / 931.58 = 1.29; H1 1,699.95 / 1,459.70 = 1.16 | PPT L407-L411, L425-L517; RES L234, L240 | PASS |
| 70 | CMD cost claim (REV L557) | -1.63 pp / -1.58 pp; +8.9% / +22.0% in rupees | -1.630 / -1.583 pp; +8.92% / +22.04% | RES L152, L155 | PASS |
| 71 | Receivables rise (REV L570) | +59.35 to 178.38 | 593.46 Mn; 1,783.77 Mn | RES L215 | PASS |
| 72 | EPS (REV L21, L115, L158) | cons per filing; std 6.57 and 6.01 flagged | cons EPS all round from PAT / 23.392 Mn shares; std Q2 6.578 and H1 FY26 6.017 vs filed 6.57 / 6.01 | RES L181, L472 | PASS (A4 already carries RES-A3-13) |
| 73 | Guidance-log tally (REV L452) | 4 consistent or on track; 6 not testable | row statuses REV L434-L450: 3 consistent or on track (#8, #10, #16); 5 not testable (#6, #9, #12, #13, #17); 1 FAR (#14); 1 NEAR (#15) | REV L434-L450 | CONTRADICTION (count; finding C1) |

Arithmetic result: no mismatch above rounding in any derived metric (rows 1-72). Row 73 is a count inconsistency, logged as finding C1.

---

## AUDIT 3: ADVERSARIAL READ

The three most positive claims in A4, each attacked from the same extract.

### Claim 1. "The profit growth is real at group level" (REV L662; also REV L208 "Real: core PBT grew in line with PAT", L227 "The headline growth is real at the consolidated level", L280 "About 95% of the YoY PAT change comes from core operations")

Strongest bear counter. The "core" metric removes other income only. The filing does not say where currency gains and losses sit. H1 FY27 carries an unrealised FX gain of 39.06 Mn (Rs 3.91 Cr; RES L268). H1 FY26 carried an unrealised FX loss of 4.26 Mn (Rs 0.43 Cr; RES L268). A4 tests only one location: "If the FX gain sits in OI" (REV L230). If FX sits in other expenses (RES L155), it is inside operating EBITDA and core PBT. Then up to Rs 3.91 Cr is 8.3% of H1 core PBT (Rs 46.84 Cr), and the Rs 4.33 Cr swing is 16.5% of the Rs 26.23 Cr H1 core-PBT increase. Realised FX is not visible at all. The Q2 split is ND.

Does it survive? YES. RES L268 supports the gain; no note or line discloses its location (RES L345-L371). The 95% "core" share (REV L280) is an upper bound that holds only if FX sits outside the operating lines. A4 does not say so. Tag MISSING. Graft to A4 (text in the correction list below).

### Claim 2. "Operating leverage offset the input-cost hit" (REV L226) and "Operating leverage is real" (REV L685)

Strongest bear counter. The offset exists only at group level. The parent carries all payroll (cons minus std employee cost is Rs 0.00 Cr, REV L187) and the plant. At the parent, Q2 FY27 vs Q2 FY26, as a share of revenue:
- materials (RM consumed plus FG/WIP change) rose from 44.59% to 52.69%, +810 bps (RES L447, L451, L453);
- employee cost fell from 12.90% to 8.79%, -411 bps (RES L454);
- other expenses fell from 24.29% to 23.47%, -82 bps (RES L457);
- operating EBITDA margin fell 317 bps, to 15.05%.

So 493 bps of cost leverage did not offset 810 bps of input cost at the factory. The group's +74 bps appears only after the subsidiary layer is added. That layer has no plant, payroll or debt, and its profit gap fell to Rs 0.48 Cr in H2 FY26 (REV L179). Two readings fit: a real cost squeeze at the factory, or margin moved to the subsidiaries through transfer prices. Both readings make the group offset depend on subsidiary profit holding at year end.

Does it survive? YES. Every number is a filed cell. A4 shows the parent margin falling (REV L219, L668), but it never qualifies the "offset" claim, and the brief states "Operating leverage is real" with no entity caveat. Tag MISSING. Graft to A4.

### Claim 3. SDA Euro 7 trigger "FIRED (revenue now visible)" (REV L487), SDA watch item "GREEN" (REV L407), "The quarter's numbers agree" (REV L676)

Strongest bear counter. Filed figures alone show the step-up sits in one quarter. H1 SDA is Rs 154.6 Cr (PPT L614), 40% of H1 revenue (PPT L623). The Q2 share is 45% (PPT L1106). On a rounded 44.5-45.5% share, Q2 SDA is Rs 96.7-98.9 Cr. Q1 SDA is then Rs 55.7-57.9 Cr, about 34% of Q1 revenue. That is only 9-13% above the FY26 quarterly average of Rs 51.1 Cr (Rs 204.5 Cr / 4, PPT L614). The Euro 7 link is a management claim (PPT L160-L161). No customer, volume or contract data is filed. The second leg of the GREEN threshold, new-customer invoicing, is ND (REV L407). Bull reading: Euro 7 run-rate demand. Bear reading: a one-quarter order spike or a customer pre-build. Separating observation: Q3 FY27 SDA revenue at or above about Rs 97 Cr (share at least 45% on revenue at or above Rs 217.32 Cr), with new customers named. A4 has no SDA row in the monitorables (REV L609-L632) or the forward map (REV L701-L714), although SDA supplied about 78% of the QoQ revenue gain (REV L483).

Does it survive? YES. The arithmetic uses filed shares and filed H1 values only. A4 shows the derived Q1 and Q2 values (REV L477) but grades FIRED and GREEN with no durability caveat, no separating observation and no monitorable. Tag MISSING. Graft to A4.

### Fourth candidate considered, not grafted: ROCE GREEN, "directionally at or above the FY28 bull figure" (REV L395, L406, L509)

Counter tested: TTM ROCE is 9.5% (8.9% operating) on closing capital employed, below the 12% reassess line. A4 already states this (REV L461, L466) and flags the period and basis mismatch (REV L395). The other counter, that the FY28 projection carries Dahej-III capital, rests on memory, not on the extract. Nothing new to graft.

### Mandatory acquisition-economics probe

The documents describe no business acquisition or stake buy in Q2 or H1 FY27 (RES L295 and L584: nil in the 30.09.2026 column). The only stake purchase in the filing is a FY26 non-current investment of 40.00 Mn (Rs 4.00 Cr; RES L295, L584), carried at 40.00 Mn at both balance-sheet dates (RES L207). The filing does not name the investee or give the stake or the investee's earnings. Price / target PAT is therefore not computable (target PAT ND). The amount is 0.49% of consolidated equity (40.00 / 8,146.51 Mn). The deck's 2021 Dahej-III land purchase (PPT L1017-L1019) is land with no earnings stream. Neither the documents nor A4 make a "cheap, accretive acquisition" claim, so no bear reading needs grafting. A4 does not name the Rs 4.00 Cr investment (style note S6).

---

## FINDINGS REGISTER

| ID | Type | Finding | Lines | Loop |
|---|---|---|---|---|
| M1 | MISSING | Surviving counter to claim 1: the P&L location of the Rs 3.91 Cr H1 unrealised FX gain is ND. If it sits in other expenses it is up to 8.3% of H1 core PBT and 16.5% of the H1 core-PBT increase. The 95% core share is an upper bound | REV L208, L227, L230, L280, L662; RES L155, L268 | A4 |
| M2 | MISSING | Surviving counter to claim 2: at the parent, materials +810 bps YoY against 493 bps of cost leverage; parent margin -317 bps. The group offset depends on the subsidiary layer | REV L226, L685; RES L447-L457 | A4 |
| M3 | MISSING | Surviving counter to claim 3: the SDA step-up is one quarter on filed shares (Q1 about 34%, Q2 45%) and the Euro 7 link is MGMT only; new-customer leg ND. No SDA monitorable, forward-map row or separating observation | REV L407, L483, L487, L609-L632, L676, L701-L714; PPT L160-L161, L614, L623, L1106 | A4 |
| F1 | FACTUAL | The CWIP rise of Rs 19.48 Cr is described as "since the 20-Jul groundbreaking" (REV L343) and as "Dahej-III build" (REV L311), and it is used as Dahej-III confirming evidence (REV L440, L488). RES L203 gives only the 31-Mar to 30-Sep change; the filing has no project split. The extract does not support the period or the attribution | REV L311, L343, L440, L488; RES L203 | A4 |
| C1 | CONTRADICTION | The guidance tally (REV L452) gives 4 consistent or on track and 6 not testable. The row statuses (REV L434-L450) give 3 consistent or on track, 5 not testable, 1 FAR (#14) and 1 NEAR (#15). The tally files a tested FAR reading as "not testable" | REV L434-L452 | A4 |
| S1-S7 | STYLE | See STYLE NOTES | below | none |

### Correction list for A4 (exact text; no table number changes)

1. M1. After REV L230 add: "The filing does not disclose the P&L line of the unrealised FX gain (RES L268). If it sits in other expenses, not other income, it is inside operating EBITDA and core PBT: up to Rs 3.91 Cr (8.3%) of H1 core PBT of Rs 46.84 Cr. With the H1 FY26 unrealised loss of Rs 0.43 Cr, the swing is up to Rs 4.33 Cr (16.5%) of the Rs 26.23 Cr H1 core-PBT increase. The Q2 split is ND." At the end of REV L280 add: "This share is an upper bound. It assumes non-cash FX sits outside the operating lines (location ND, RES L268)." In REV L662 add after the core-profit sentence: "The filing does not say where a Rs 3.91 Cr half-year currency gain sits, so part of that growth could be non-cash [FILED, Q2; INFERENCE]."
2. M2. After REV L226 add: "At the parent the offset fails. Standalone Q2 YoY: materials rose from 44.59% to 52.69% of revenue (+810 bps; RES L447, L451, L453). Employee cost fell 411 bps (L454) and other expenses 82 bps (L457), so parent operating EBITDA margin fell 317 bps. The group's +74 bps exists only after adding the subsidiary layer, which has no plant, payroll or debt; its profit gap fell to Rs 0.48 Cr in H2 FY26. Two readings: a real cost squeeze at the factory, or margin moved to the subsidiaries by transfer price. Both make the group offset depend on subsidiary profit holding at year end (Q5, Q7)." At the end of REV L685 add: "At the factory company the cost ratios also fell, but materials rose 8.1 points of revenue on last year, so its margin fell [FILED, Q2; INFERENCE ratio]."
3. M3. In REV L487 change the status to "FIRED on revenue (one quarter, MGMT attribution); durability unproven". In REV L407 change the status to "GREEN on revenue; new-customer leg ND; one quarter". After REV L483 add: "From filed figures alone, H1 SDA of Rs 154.6 Cr at 40% of H1 revenue (PPT L614, L623) and a 45% Q2 share (PPT L1106) imply Q2 SDA of about Rs 97-99 Cr and Q1 of about Rs 56-58 Cr (about 34% of Q1 revenue, close to the FY26 quarterly average of Rs 51.1 Cr). The step-up sits in one quarter. The Euro 7 link is MGMT (PPT L160-L161); no customer, volume or contract data is filed. Bull reading: Euro 7 run-rate demand. Bear reading: a one-quarter order spike or a customer pre-build. Separating observation: Q3 FY27 SDA at or above about Rs 97 Cr (share at least 45% on revenue at or above Rs 217.32 Cr), with new customers named." Add monitorable "M25 | Q3 FY27 SDA revenue vs Q2 (about Rs 97 Cr; share 45%) | Q3 FY27 results by 14-Feb-2027 | PPT L614, L623, L1106". Add forward-map row "by 14-Feb-2027 | Q3 SDA revenue (M25) | SDA holds at or above about Rs 97 Cr with new customers named | SDA falls back toward Rs 55-60 Cr; Q2 was a one-quarter spike". Add M25 to the closing YAML monitorables.
4. F1. REV L311 verdict: "CWIP build; project split ND; no major capitalisation". REV L343, replace the last two sentences with: "The Dahej-III budget is Rs 200 Cr [memory]. CWIP rose Rs 19.48 Cr between 31-Mar and 30-Sep (RES L203). The filing gives no project split, so the Dahej-III share is ND; H1 capex was Rs 30.85 Cr (RES L291)." In REV L440 and L488 write "CWIP +Rs 19.48 Cr in H1 (project split ND)".
5. C1. Replace the tally in REV L452 with: "Score: 1 delivered, 1 ahead, 2 behind, 1 far (#14 ROCE target), 1 near (#15 asset turn), 3 consistent or on track (claim only), 1 window open, 1 not updated, 1 unverifiable, 5 not testable (17 items)."

No change to any number in A4's Step 1 to Step 5 tables follows from these findings.

---

## VERDICT

**INCOMPLETE.** Failing agent: A4. Gap: three surviving bear counters are not grafted (MISSING M1, M2, M3); one claim is unsupported by the extract (FACTUAL F1, CWIP period and Dahej-III attribution); one internal count is inconsistent (CONTRADICTION C1, guidance tally). No A2 or A3 loop: coverage is clean, with no orphan rows and nothing missing from the ledgers. No arithmetic mismatch above rounding.

---

## STYLE NOTES (logged; no re-run)

- S1. REV L670 says the call was cancelled "with no reason". The notice gives "unforeseen circumstances" (NTC L39-40). Write "with no cause named", which matches REV L639.
- S2. REV L664 says "Stock and customer dues absorbed 99%". The 99% is the net working-capital change (RES L286 vs L273). Inventories and receivables alone took Rs 116.77 Cr (RES L275-L276), offset by payables of +Rs 33.19 Cr (RES L281). Write "Working capital, mainly stock and customer dues, absorbed 99%".
- S3. REV L85 says the CMD message "was written as the call script". This is an inference from "Good evening, ladies and gentlemen" (PPT L111, L199). Tag it [INFERENCE].
- S4. A2 flag LABEL_ANOMALY (LED-R L45, L174, L307; R1005, R1040: "Net decrease" caption on positive values, RES L321, L610) has no named disposition in A4. Add "reviewed, no finding" to the data-integrity list (REV L20-L24).
- S5. REV L6 and the YAML review_path (REV L808) describe the review as two files. The audited file holds both parts (part 2 from REV L358). Update the self-description.
- S6. The FY26 Rs 4.00 Cr non-current investment (RES L207, L295, L584) is not named in A4 Step 5. Investee, stake and earnings are ND, and the amount is 0.49% of equity. Add one ND line.
- S7. The A2 presentation count test takes its grep side from A1 header totals (LED-P L17), not from a grep of the fulltext. My fulltext sweep found no gap, so no loop. A2 should grep the fulltext in the next run.

---

```yaml
stage: A5-adversary
company: "TATVA"
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
  - claim: "Group profit growth is real; core PBT +114.8% YoY; about 95% of the PAT change is core (REV L208, L227, L280, L662)"
    counter: "The P&L line of the Rs 3.91 Cr H1 unrealised FX gain is not disclosed; A4 tests only the other-income case (REV L230). If FX sits in other expenses it is inside op EBITDA and core PBT: up to 8.3% of H1 core PBT (3.91 of 46.84) and up to 16.5% of the H1 core-PBT increase (4.33 of 26.23, incl. the H1 FY26 loss of Rs 0.43 Cr). The 95% core share is an upper bound; Q2 split ND."
    source_line: "RES L268, L155, L146, L157"
    type: MISSING
  - claim: "Operating leverage offset the input-cost hit; operating leverage is real (REV L226, L685)"
    counter: "At the parent the offset fails: Q2 YoY materials rose from 44.59% to 52.69% of revenue (+810 bps) against employee -411 bps and other expenses -82 bps, so parent op EBITDA margin fell 317 bps. The group +74 bps exists only after the subsidiary layer (no plant, payroll or debt; H2 FY26 gap Rs 0.48 Cr). Readings: real factory cost squeeze, or margin moved by transfer price; both make the group offset depend on subsidiary profit holding at year end."
    source_line: "RES L447, L451, L453, L454, L457"
    type: MISSING
  - claim: "SDA Euro 7 trigger FIRED; SDA watch item GREEN (REV L407, L487, L676)"
    counter: "Filed figures alone (H1 SDA Rs 154.6 Cr = 40% of H1 revenue; Q2 share 45%) imply Q1 SDA of about Rs 56-58 Cr (about 34% of Q1 revenue, near the FY26 quarterly average of Rs 51.1 Cr) and Q2 of about Rs 97-99 Cr: the step-up is one quarter. The Euro 7 link is MGMT only; no customer, volume or contract data; the new-customer leg of GREEN is ND. No SDA monitorable or forward-map row, although SDA gave about 78% of the QoQ gain. Separating observation: Q3 FY27 SDA at or above about Rs 97 Cr."
    source_line: "PPT L614, L623, L1106, L160-L161"
    type: MISSING
findings_by_type:
  factual:
    - "F1 (A4): CWIP +Rs 19.48 Cr is described as 'since the 20-Jul groundbreaking' and 'Dahej-III build' and used as Dahej-III confirming evidence (REV L311, L343, L440, L488). RES L203 gives only the 31-Mar to 30-Sep change with no project split. Restate: H1 CWIP change, project split ND."
  missing:
    - "M1 (A4): graft the FX-location qualifier to the 'core profit is real / 95% core' claims (REV L208, L227, L230, L280, L662); RES L268."
    - "M2 (A4): graft the parent-level bridge (materials +810 bps vs leverage -493 bps YoY) to 'operating leverage offset the input-cost hit' (REV L226, L685); RES L447-L457."
    - "M3 (A4): graft the one-quarter and MGMT-attribution qualifier to SDA FIRED and GREEN (REV L407, L487, L676); add Q3 SDA monitorable M25 and a forward-map row with the separating observation; PPT L614, L623, L1106."
  contradiction:
    - "C1 (A4): guidance tally (REV L452) says 4 consistent or on track and 6 not testable; the 17 row statuses (REV L434-L450) give 3 consistent or on track, 5 not testable, 1 FAR (#14), 1 NEAR (#15). Restate the tally."
  style:
    - "S1: REV L670 'with no reason'; the notice says 'unforeseen circumstances' (NTC L39-40). Write 'no cause named'."
    - "S2: REV L664 attributes the net 99% WC absorption to stock and customer dues; those two took Rs 116.77 Cr, offset by payables (RES L275-L281)."
    - "S3: REV L85 'written as the call script' is an inference (PPT L111, L199); tag [INFERENCE]."
    - "S4: A2 LABEL_ANOMALY (R1005, R1040; RES L321, L610) has no named disposition in A4; add 'reviewed, no finding'."
    - "S5: REV L6 and L808 describe two files; the audited file is merged (part 2 from REV L358)."
    - "S6: FY26 Rs 4.00 Cr non-current investment (RES L207, L295, L584) not named in A4; investee ND; 0.49% of equity."
    - "S7: A2 presentation count test uses A1 header totals as its grep side (LED-P L17); A5 fulltext sweep found no gap."
loop_back_to: "A4"
gap: "Graft three surviving bear counters (M1 FX location behind 'core profit is real'; M2 parent-level input cost vs leverage behind 'operating leverage offset'; M3 SDA one-quarter and MGMT-attribution qualifier plus Q3 SDA monitorable and forward-map row); restate the CWIP rise as an H1 change with project split ND (F1); fix the guidance tally to 3 consistent or on track, 5 not testable, 1 far, 1 near (C1). Exact text is in the audit correction list."
style_notes:
  - "S1: say 'no cause named', not 'no reason' (REV L670; NTC L39-40)."
  - "S2: '99%' is net working capital, not stock and dues alone (REV L664; RES L275-L286)."
  - "S3: tag the call-script reading [INFERENCE] (REV L85)."
  - "S4: dispose of A2 LABEL_ANOMALY by name (RES L321, L610)."
  - "S5: update the two-files self-description (REV L6, L808)."
  - "S6: name the FY26 Rs 4.00 Cr investment as ND (RES L207, L295)."
  - "S7: A2 should grep the presentation fulltext for its count test (LED-P L17)."
analyst_note: "Coverage and arithmetic are clean. Fresh fulltext counts match all three ledgers, every structured ID is in a ledger, and about 150 derived cells recompute within rounding. The loop comes from the adversarial read. Each of A4's three most positive claims has a counter that the extract supports and A4 does not state beside the claim. (1) 'Core profit is real' assumes the Rs 3.91 Cr H1 unrealised FX gain sits in other income, but its line is undisclosed. (2) 'Leverage offset input cost' holds only after adding the staffless subsidiaries; at the factory, materials rose 810 bps against 493 bps of leverage. (3) SDA 'FIRED' rests on one quarter and a management attribution, and no SDA monitorable exists. These are grafts, not rework: no table number changes. F1 and C1 are one-line edits. The acquisition probe found no business acquisition; the only stake buy is a FY26 Rs 4 Cr investment with an undisclosed investee, so no multiple can be computed."
```
