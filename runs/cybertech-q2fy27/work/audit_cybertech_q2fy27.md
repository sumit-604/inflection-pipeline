# A5 AUDIT: CYBERTECH Q2 FY27 (results, Reg 33 board outcome 22-Oct-2026)

Stage: A5 adversary / completeness auditor. Model: claude-opus-5-5.
Inputs read: A4 review (runs/cybertech-q2fy27/work/review_cybertech_q2fy27.md, 672 lines); A1 fulltext (extracted/cybertech-results-q2fy27-fulltext.md, L1-L443); A1 structured (extracted/cybertech-results-q2fy27-structured.md, R001-R739); A2 ledger (work/ledger_results_cybertech_q2fy27.md). No source PDF and nothing under inputs/ was opened. A3 reasoning was not read.

Anchor convention: (Lnnn) = A1 fulltext line; (Rnnn) = A1 structured row; (A4 Lnnn) = line in the A4 review file; "c:" = A5 arithmetic on anchored filed figures. All arithmetic is in Rs lakh as filed unless a cell says Cr (x0.01). "Perimeter" = consolidated less standalone (the three WOS net of intercompany eliminations).

VERDICT: INCOMPLETE. Loop back to A4. Six looping findings: F1, F2, F3 (FACTUAL), C1 (CONTRADICTION), M1, M2 (MISSING). No A2 or A3 loop. Twelve STYLE notes logged.

---

## AUDIT 0. DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASS.

| Part | A4 location | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | A4 L541-L555 | 13 lines (inside the 10-20 line band; Role 4 results, not Document Review Protocol). Numbers, tiers, verdict, next test. | PRESENT |
| 2. Sector intelligence | A4 L557-L564 | 6 bullets; FILED vs SECONDARY labelled. Content defect in bullet 2 (F2), not an empty part. | PRESENT |
| 3. Business-model intelligence | A4 L566-L573 | 6 bullets: cost structure, asset intensity, treasury, model drift, gaps. | PRESENT |
| 4. Competition intelligence | A4 L575-L581 | 5 bullets; peers labelled SECONDARY, PENDING LIVE VERIFICATION. | PRESENT |
| 5. Forward map | A4 L583-L597 | Make-or-break line plus 9 dated or event-driven catalysts, each with a bull and a bear fork. Fork defect in the Q1 FY28 row (C1), not an empty part. | PRESENT |

---

## AUDIT 1. COVERAGE

Fresh pass: A5 enumerated A1's FULLTEXT (L1-L443) by category, then diffed against the A2 ledger and the structured file. "In-scope" means a unit of the same kind A1 already captures elsewhere (A1 captures the page-1 telephone R559 and the page-3 pin R572, so the page-3 and page-7 telephone and pin repeats are in scope).

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| notes | 7 | 7 (Notes 1-6 L430-L436; Note 5 para 2 L435; header L429 = R732) | none | PASS |
| line_items | 191 | 191 (consol P&L 23 lines L100-L128, BS 37 L142-L189, CF 38 L201-L242; standalone P&L 21 L286-L311, BS 36 L324-L370, CF 36 L382-L421) | none | PASS |
| table NUMBER cells R001-R551 | 551 | 551 (22x6+3, 37x2, 38x2 = 285; 20x6+3, 36x2, 35x2+1 = 266) | none | PASS |
| zero_standing | 45 cells / 27 items | 45 / 27 (consol P&L 14, BS 4, CF 7; standalone P&L 11, BS 2, CF 7) | none | PASS |
| embedded_numbers | 42 | 60 line-level units (42 + 18 uncaptured boilerplate, list below) | none | PASS; STYLE S1 |
| agenda_items | 1 | 1 (L37) | none | PASS |
| auditor_paras | 7 | 7 by paragraph number (consol 1-4 L68-L78; standalone 1-3 L258-L264) | none | PASS; mapping note in S1 |
| entities | 46 | 55 (46 + 9 uncaptured boilerplate) | none | PASS; STYLE S1 |
| forward | 3 | 3 (L434 x2, L435) | none | PASS |
| dates | 51 | 52 (51 + L33 subject-line repeat of the meeting date) | none | PASS; STYLE S1 |
| qualifiers | 46 | 51 (46 + 5 formula captions) | none | PASS; STYLE S1 |
| signature_blocks | 10 | 10 digital stamps (L50-L51, L83, L133, L194, L247, L269, L316, L375, L426, L443); 7 ED printed blocks sit in ledger section 9 | none | PASS |
| turns / questions / slides | 0 | 0 (no transcript, no deck) | n/a | PASS |

Uncaptured units from the fresh pass. None is a financial value, a period value, an event date, an entity of substance, a forward statement, or a qualifier that limits a figure:
- Embedded numbers (18): L28 BSE address numbers (Plot No. C1, Mumbai-400 001); L30 NSE pin 400 051; L62 auditor telephones (p2); L68 "2015" (consol para 1); L78 "Regulation 33 ... 2015" (consol para 4); L90 footer registration numbers (p2); L95 plot B-63/64/65 (p3); L96 telephone +91 22-4283-9200 and fax (p3); L126 "(of Rs.10 each)" EPS caption (consol); L252 auditor telephones (p6); L258 "2015" (standalone para 1); L260 "2013" as a number (ENTITY R622 covers it); L264 "Regulation 33 ... 2015" (standalone para 3); L268 firm registration number (p6; R568 holds p2 only); L276 footer registration numbers (p6); L281 plot and pin 400 604 (p7); L282 telephone and fax (p7); L309 "(of Rs.10 each)" EPS caption (standalone).
- Entities (9): L19 registered office as an entity; L20 corporate website; L43 exchange websites; L63 and L253 auditor email; L88 and L274 "Place: Mumbai"; L96 and L282 company website repeats.
- Dates (1): L33 subject-line "October 22, 2026" (repeat of R672/R673).
- Qualifiers (5): formula captions L115 "(5-6)", L123 "(7+8)", L296 "(3-4)", L301 "(5-6)", L306 "(7+8)" (A1 captured the consolidated "(1+2)" R706 and "(3-4)" R707 only).
- Auditor paragraph mapping: A2 maps R698 and R699 both to consolidated para 2 (L71) and R716 and R717 both to standalone para 2 (L262). Para 1 of each report (L68-L69, L258-L260) has no qualifier row; its content sits in R565, R575, R613, R614, R622, R623, R676, R680. The count of 7 holds by paragraph number.
Only one uncaptured unit has analytic use: the page-3 and page-7 telephone (L96, L282) is one side of the A3-20 telephone mismatch with page 1 (L20 "+91 226983-9200"). A4 carries that fact (A4 L483, L662) and the verdict does not turn on it. Typed STYLE (S1): no number, fact or conclusion changes, so missing_from_ledger stays empty.

Ledger rows vs A4 citations. A4 cites the P&L and cash-flow tables as ranges (L99-L128, L199-L242, L285-L311, L380-L421) and the balance sheets line by line. Not cited by R-ID or L-line:
- Consolidated balance sheet L143, L148, L150, L151, L155, L158-L162, L173, L175, L186-L189 (R138-R139, R146-R147, R150-R153, R156-R157, R162-R171, R182-R183, R186-R187, R202-R209). L155 values are used in A4's receivable days without the anchor.
- Standalone balance sheet L324-L327, L330-L333, L337-L344, L347, L349, L353-L356, L359-L370 (R409-R416, R419-R426, R429-R446, R449-R480). L337, L338, L339, L349 and L359 values are used in A4 Step 5B without anchors.
- Identifier rows inside R552-R593, R594-R639, R643-R693 that A4 does not name (DIN repeats, statute numbers, auditor stamps on pages 3-5 and 7-9, CS stamp R675).
A4 marks all of these in one explicit statement (A4 L15: "A4 read every structured row against the fulltext line it cites. No row is unreviewed."). A5 re-reviewed every uncited row:
- Both balance sheets foot on both dates. Consolidated: NCA 5,531.15 / 4,582.32; CA 23,584.43 / 23,301.71; TA 29,115.58 / 27,884.03; equity 20,572.73 / 21,230.00; NCL 805.07 / 872.96; CL 7,737.78 / 5,781.07; TL 8,542.85 / 6,654.03; TEL = TA. Standalone: NCA 11,831.89 / 6,752.20; CA 6,371.84 / 11,855.79; TA 18,203.73 / 18,607.99; equity 13,375.59 / 14,906.47; NCL 528.58 / 647.35; CL 4,299.56 / 3,054.17; TL 4,828.14 / 3,701.52; TEL = TA.
- No uncited row carries an unaddressed material item. Two supportive details, no defect: (a) at 31-Mar-2026 the parent's other financial assets (current) exceeded the consolidated figure by 470.08 (c: L341 1,769.30 less L159 1,299.22), an intercompany balance eliminated on consolidation, which supports A4's intercompany-timing reading (A4 L339); (b) 22.04 Cr of the 25.94 Cr consolidated other current liabilities sits in the perimeter at 30-Sep-2026 (c: L184 2,594.32 less L365 390.09); the parent's balance fell 1.62 Cr while the perimeter's rose 4.99 Cr, which narrows A4 Q6 to the subsidiaries (S9).
Orphan rows: none. The blanket mark in place of row-range "reviewed, no finding" markers is logged as STYLE (S2).
A2 flags vs A4: ZERO_STANDING (A4 L18, L292, Step 5), SIGNATURE_BEFORE_MEETING_CLOSE (A4 L79), AGENDA_NOT_LISTED (A4 L521), ENTITY_WORDING_DIFF (A4 L61), ENTITY_UNNAMED (A4 L70), RESTATED (A4 L62, L64), FOOTNOTE_UNRESOLVED (A4 L662). All addressed.

Coverage verdict: PASS. orphan_rows [], missing_from_ledger [].

---

## AUDIT 2. ARITHMETIC

Extract self-consistency first. Every P&L column foots in both statements (TI = revenue + OI; PBT = TI less total expenses; PAT = PBT less the three tax lines; H1 = Q1 + Q2; TCI = PAT + OCI). Both balance sheets foot (Audit 1). Both cash flows foot (A, B and C subtotals, net change, closing cash; consolidated closing 1,854.94 includes the 7.24 FX effect, L241). Rounding breaks inside the filing: L110 2,415.96 vs L201 2,415.95; L293 128.56 vs L384 128.55; L292 56.13 vs L388 56.12. A4 carries them as A3-20. The standalone financing total for H1 FY26 (L418, -458.03) ties without a buyback cell, so that cell is nil (S11).

| Metric | A4 value | Recomputed (c:) | Source line | Status |
|---|---|---|---|---|
| 1A Tax expense, consol (Q2FY27 / Q1FY27 / Q2FY26 / FY26 / H1FY26 / H1FY27, Cr) | 2.87 / 3.14 / 2.75 / 9.79 / 5.40 / 6.01 | 286.70 / 313.81 / 274.80 / 979.20 / 540.46 / 600.51; PBT less tax = L115 in all six | L112-L115 | MATCH |
| 1A Op EBITDA, consol (Cr) | 8.09 / 5.72 / 4.62 / 18.74 / 9.55 / 13.81 | 808.87 / 571.89 / 461.92 / 1,874.37 / 955.25 / 1,380.76 | L110+L107+L106-L101 | MATCH |
| 1A Op EBITDA margin, consol | 11.04 / 8.36 / 7.86 / 7.90 / 8.17 / 9.74% | 11.036 / 8.355 / 7.858 / 7.904 / 8.166 / 9.741% | / L100 | MATCH |
| 1A Reported EBITDA, consol (Cr) | 12.82 / 13.90 / 12.57 / 44.62 / 24.55 / 26.73 | 1,282.10 / 1,390.44 / 1,256.60 / 4,462.38 / 2,454.52 / 2,672.54 | L110+L107+L106 | MATCH |
| 1A Core PBT ex-OI, consol (Cr) | 6.81 / 4.43 / 3.46 / 14.34 / 7.24 / 11.24 | 681.20 / 442.98 / 345.66 / 1,434.16 / 724.07 / 1,124.18 | L110-L101 | MATCH |
| 1A OI / PBT, consol | 40.99 / 64.89 / 69.69 / 64.34 / 67.43 / 53.47% | 40.99 / 64.89 / 69.69 / 64.34 / 67.43 / 53.47% | L101/L110 | MATCH |
| 1A ETR, consol | 24.83 / 24.88 / 24.10 / 24.35 / 24.31 / 24.86% | 24.835 / 24.875 / 24.098 / 24.345 / 24.308 / 24.856% | tax / L110 | MATCH |
| 1A PAT margin, consol | 11.84 / 13.85 / 14.72 / 12.83 / 14.39 / 12.81% | same to two decimals | L115/L100 | MATCH |
| 1B Tax, standalone (Cr) | 1.76 / 1.94 / 2.04 / 7.48 / 3.54 / 3.70 | 176.19 / 193.64 / 203.91 / 748.22 / 354.25 / 369.83; PBT less tax = L301 in all six | L298-L301 | MATCH |
| 1B Op EBITDA, standalone (Cr) / margin | 4.82 / 5.12 / 4.17 / 15.90 / 7.58 / 9.94; 10.94 / 11.63 / 10.46 / 9.91 / 9.54 / 11.28% | 482.26 / 511.87 / 416.87 / 1,589.93 / 758.32 / 994.13; 10.937 / 11.627 / 10.458 / 9.913 / 9.540 / 11.282% | L296+L293+L292-L287; / L286 | MATCH |
| 1B Reported EBITDA, core PBT, OI/PBT, ETR, PAT margin, standalone | as A4 L160-L164 | 822.37 / 895.35 / 935.44 / 3,444.04 / 1,674.45 / 1,717.72; core 376.52 / 404.46 / 333.15 / 1,231.04 / 567.33 / 780.98; ratios agree to two decimals | L286-L301 | MATCH |
| 1C Perimeter revenue (Cr) / share | 18.92 (32.2%) / 24.42 (35.7%) / 29.20 (39.8%) / 37.49 (32.1%) / 53.63 (37.8%) / 76.77 (32.4%) | 1,892.26 / 2,442.45 / 2,920.29 / 3,749.43 / 5,362.74 / 7,676.50 | L100 less L286 | MATCH |
| 1C Perimeter Op EBITDA (Cr) / margin | 0.45 (2.4) / 0.60 (2.5) / 3.27 (11.2) / 1.97 (5.3) / 3.87 (7.2) / 2.84 (3.7) | 45.05 / 60.02 / 326.61 / 196.93 / 386.63 / 284.44 | 1A less 1B | MATCH |
| 1C Perimeter OI / PAT (Cr); S-C PAT gap | OI 2.76 / 4.35 / 1.33 / 5.83 / 5.68 / 7.34; PAT 2.18 / 3.53 / 3.27 / 5.54 / 6.81 / 7.06; gap 33.6 / 59.5 / 60.6 / 49.0 / 60.0 / 30.2% | 276.11 / 435.07 / 133.12 / 583.14 / 568.19 / 733.90; 217.73 / 353.42 / 327.29 / 553.67 / 680.71 / 706.04; 33.61 / 59.47 / 60.56 / 49.03 / 59.99 / 30.21% | L101-L287, L115-L301 | MATCH |
| 1C Gap +27.0 pp YoY, +1.1 pp QoQ; perimeter revenue +54.3% YoY; 70.8% of group growth | as stated | 26.95 pp; 1.09 pp; 54.33%; 1,028.03 / 1,451.07 = 70.85% | L100, L286 | MATCH |
| 2A Consol YoY: revenue, Op EBITDA, margin, D&A, FC, EBIT, OI, core PBT, PBT, PAT, EPS | +24.7%, +75.1%, +318 bps, -13.2%, +104.3%, +97.5%, -40.5%, +97.1%, +1.2%, +0.3%, +2.9% | +24.685%, +75.11%, +317.8 bps, -13.18%, +104.31%, +97.52% (368.41 to 727.68), -40.45%, +97.07%, +1.236%, +0.253%, +2.88% | L100-L127 | MATCH |
| 2B Standalone YoY: revenue, Op EBITDA, margin, D&A, FC, EBIT, OI, core PBT, PBT, PAT, EPS | +10.6%, +15.7%, +48 bps, -6.2%, +137.7%, +19.7%, -34.4%, +13.0%, -15.9%, -16.6%, -14.4% | +10.61%, +15.69%, +47.9 bps, -6.23%, +137.74%, +19.72%, -34.41%, +13.02%, -15.86%, -16.57%, -14.42% | L286-L310 | MATCH |
| 2C Cost ratios YoY (EBE, outsourced, other) | -209, -73, -36 bps | 56.013 to 53.923; 24.823 to 24.092; 11.306 to 10.949 | L104, L105, L108 / L100 | MATCH |
| 2C Sequential margin, consol / standalone | +268 bps / -69 bps | +268.1 / -69.0 bps | as 1A, 1B | MATCH |
| 2C OI components H1 (interest and dividend, FV gain, MF profit, residual) | 7.06 vs 6.93; 0.19 vs 2.65; 0.03 vs 0.08; 5.64 vs 5.34 Cr | 705.77 / 692.82; 18.69 / 264.50; 2.89 / 8.11; 564.43 / 533.84 | L101, L206, L211, L212 | MATCH |
| 3 Q1FY26 derived (revenue, margin, core PBT) | 58.19 Cr, 8.48%, 3.78 Cr | 5,819.41; 493.33 / 5,819.41 = 8.477%; 1,083.00 less 704.59 = 378.41 | H1FY26 less Q2FY26 | MATCH |
| 3 H2FY26 block (revenue, margin, core PBT) | 120.17 (avg 60.09), 7.65%, 7.10 (avg 3.55) | 12,017.32; 919.12 / 12,017.32 = 7.648%; 710.09 | FY26 less H1FY26 | MATCH |
| 3 QoQ run-rate steps | +1.0%, +2.2%, +13.9%, +7.1%; standalone +0.2%; perimeter +19.6% | 1.015, 1.0221, 1.1391, 1.0708; 1.0016; 1.1956 | L100, L286 | MATCH |
| 4A Consol PAT bridge (revenue, margin, D&A, FC, OI, tax on PBT change, ETR change; total) | +114.02, +232.93, +12.32, -23.73, -321.45, -3.40, -8.50; +2.19 | 1,451.07 x 7.858% = 114.02; 7,329.57 x 3.178 pp = 232.93; 14.09 x 24.098% = 3.40; 1,154.43 x 0.737 pp = 8.50; sum 2.19 = L115 change | L100-L115 | MATCH |
| 4B Standalone PAT bridge | +44.24, +21.15, +4.04, -26.06, -178.46, +32.34, -4.62; -107.37 | same; sum -107.37 = L301 change | L286-L301 | MATCH |
| 4C OI-normalised PBT and PAT; core engine | 14.76 / 11.09 / 5.12 / 2.62 Cr; core +38.76%, OI -37.14% of prior PAT | 1,475.88; 1,109.35; 512.03; 262.36; 38.76; -37.14 | L101, L110, tax lines | MATCH |
| 0C Share count: buyback, ESOP, closing, average buyback cost | 8,50,000; 2.73%; 1,00,000; 0.33%; 3,03,80,600; Rs 176.24 | 85.00 / Rs 10; 8,50,000 / 3,11,30,600; 10.00 / Rs 10; 1,00,000 / 3,02,80,600; 3,038.06 / Rs 10; 1,498.00 lakh / 8,50,000 | L124, L166, L234, L235, L432 | MATCH |
| 5A CFO, CFO/PAT, capex, FCF, WC release | 16.44 to 28.26 (+72.0%); 0.98x to 1.56x; 2.56 to 0.44 (-83.0%); 13.87 to 27.83 (+100.6%); 5.64 to 13.06; 94.6% of H1 Op EBITDA | 1,643.55 / 2,826.32; 0.977 / 1.557; 256.23 / 43.55; 1,387.32 / 2,782.77; 563.66 / 1,305.74; 1,305.74 / 1,380.76 | L115, L219, L222, L224 | MATCH |
| 5A CFO pre-WC after tax / PAT (ratio arithmetic) | 0.64x / 0.84x | 1,079.89 / 1,682.88 = 0.642; 1,520.58 / 1,815.45 = 0.838 | L214, L221, L115 | MATCH (arithmetic); interpretation FAIL, see F3 |
| 5A Receivable, payable days, CCC | 53.4 to 44.5; 105.1 to 102.6; -51.6 to -58.0 | 53.45 / 44.51; 105.09 / 102.56; -51.64 / -58.04 | L155, L181, L182, L100, L104, L108 | MATCH |
| 5A Net cash Mar-26 / Sep-26; with NC OFA; lease; shares of TA and equity | 169.59 / 167.92; 174.50 / 190.30; 4.02; 57.7% / 81.6% | 16,959.49 / 16,792.44; 17,450.07 / 19,030.48; 402.05; 0.5768 / 0.8162 | L147, L149, L154, L156, L157, L163, L168, L172, L178, L179 | MATCH |
| 5A Other financial liabilities (current) rise | +13.60 Cr | 1,484.90 less 124.47 = 1,360.43 | L183 | MATCH |
| 5B Standalone CFO, CFO/PAT, capex, FCF, WC | 32.65 to 41.47 (+27.0%); 2.89x to 3.65x; 2.45 to 0.22; 30.20 to 41.25 (+36.6%); 22.55 to 29.36 (+6.81) | 3,264.63 / 4,146.63; 2.891 / 3.654; 244.67 / 21.55; 3,019.96 / 4,125.08; 2,254.77 / 2,936.27 (diff 681.50 = 6.815, rounding) | L301, L398, L401, L403 | MATCH |
| 5B Standalone receivable days, net cash; NC investment tie; perimeter investments | 69.1 to 21.0; 53.14 to 25.76; 6,448.66; 32.64; 104.29 to 136.92; 95.1% | 69.08 / 20.99; 5,314.01 / 2,575.81; 3,036.69 - 701.16 + 4,113.13 = 6,448.66; 3,293.77 - 30.00; 10,428.51 / 13,692.28; 0.9509 | L329, L336-L339, L359, L405, L406, L226, L154 | MATCH |
| A3-11 Other equity gap (standalone / consol) | 12.15 Cr; 10,337.53 filed vs 11,552.75 expected; 9.1% of SA net worth | 11,793.41 + 1,134.74 - (1,498.00 - 85.00) + (47.60 - 10.00) = 11,552.75; gap 1,215.22; consol 1,215.24; 1,215.22 / 13,375.59 = 9.09% | L167, L168, L235, L234, L301, L348, L349 | MATCH (and = Rs 4.00 x 3,03,80,600 exactly, S10) |
| Verdict and QfM figures | 27.6% of opening SA net worth; 20.25 Cr / 66.7%; 25.94; 32.33; 17.47; 0.17 Cr a quarter | 4,113.13 / 14,906.47 = 27.59%; 2,024.85 / 3,035.28 = 66.71%; 2,594.32; 3,233.32; 1,747.46; 16.81 | L118, L149, L157, L184, L337, L349, L405 | MATCH |

Arithmetic result: no mismatch above rounding in any A4 cell. One metric is mis-specified (F3).

### F3. Pre-WC conversion: correct arithmetic, unsupported reading (FACTUAL, loop A4)

A4 L306 calls 0.84x (H1 FY27) and 0.64x (H1 FY26) "Underlying conversion below 1.0x". A4 L595 makes "pre-WC 0.84x becomes the true reading" the bear fork. A4 L343, L445, L658 and the analyst note pass 0.84x to /fttcp as the Pillar 2 (Cash Multiplier) fact.
The ratio mixes bases. "Operating profit before working capital changes" (L214) has 729.95 of income items taken out: unrealised FX gain 2.55 (L204), interest and dividend income 705.77 (L206), ECL reversal 0.05 (L210), MF sale profit 2.89 (L211), FV gain 18.69 (L212). Interest received goes to investing (L230, 845.60). PAT (L115) still holds all of that income.

| Like-for-like basis | H1 FY27 | H1 FY26 | Source |
|---|---|---|---|
| A4 mixed basis: (pre-WC op profit - taxes paid) / PAT | 1,520.58 / 1,815.45 = 0.84x | 1,079.89 / 1,682.88 = 0.64x | L214, L221, L115 |
| (a) add interest and dividend income back to the numerator | (1,520.58 + 705.77) / 1,815.45 = 1.23x | (1,079.89 + 692.82) / 1,682.88 = 1.05x | + L206 |
| (b) strip after-tax removed income from PAT | 1,520.58 / (1,815.45 - 729.95 x 0.7514) = 1,520.58 / 1,266.94 = 1.20x | 1,079.89 / (1,682.88 - 977.74 x 0.7569) = 1,079.89 / 942.81 = 1.15x | L204-L212, ETR 24.86% / 24.31% |

On either like-for-like basis, underlying conversion is above 1.0x in both halves, and it improves YoY. The headline 1.56x is still inflated by the 13.06 Cr liability-led release, so INDETERMINATE-WITH-DIRECTION stands on H2 reversal risk. The "below 1.0x" conclusion and the 0.84x "true reading" do not stand.
Fix (A4): replace the A4 L306 verdict cell with "Mixed basis: numerator excludes 7.30 Cr of treasury and non-cash income that PAT includes. Like-for-like 1.20x to 1.23x H1 FY27 vs 1.05x to 1.15x H1 FY26." Then align A4 L343, L445, L658 and the analyst note. Change the L595 bear fork to "WC release reverses; H2 FY27 CFO/PAT below 1.0x".

---

## AUDIT 3. ADVERSARIAL READ

The three most positive claims in A4, each attacked from the same extract, then the mandatory purchase-economics probe.

### Claim 1. "The flat profit hides a better business." Core PBT ex-OI nearly doubled, 3.46 to 6.81 Cr; "the cleanest test passed"; "core growth is real and the headline understates it" (A4 L197, L222, L289, L545).

Strongest bear counter from the extract:
- It is one quarter, and all of the QoQ gain sits outside the parent. Consolidated Op EBITDA rose 236.98 QoQ (571.89 to 808.87; c: L101, L106, L107, L110). The perimeter rose 266.59 (60.02 to 326.61). The parent fell 29.61 (511.87 to 482.26; c: L287, L292, L293, L296). Parent core PBT fell 6.9% QoQ (404.46 to 376.52) and rose 13.0% YoY.
- The perimeter's EBITDA margin was 2.4% (Q2 FY26) and 2.5% (Q1 FY27) before the 11.2% print. The filing gives no segment, entity, customer or USD split (L433).
- Q2 carries a currency swing. FCTR was -24.96 in Q1 and +217.88 in Q2 (L121) [INFERENCE: the rupee weakened in Q2]. A weaker rupee lifts the INR margin of USD revenue delivered at INR cost, with no operating leverage. Constant-currency margin is ND.
- On the H1 basis, Other Income is still 53.47% of PBT (c: 1,291.78 / 2,415.96). On H1 the group is still mostly a treasury earner.
Survives: YES, in part. A4 states the perimeter concentration (A4 L221) and names the Q3 test (A4 L474-L478). But A4's stated rival reading is a transfer-pricing shift (F1), and that cannot produce a consolidated margin gain. The valid rival readings for the group step (one quarter; currency) appear nowhere in the review. Graft required (M1).
Graft text (A4 Step 2C item 3, Step 3 diagnostics, brief L550): "Bear reading: the core-PBT doubling is one quarter, and all of the QoQ gain sits outside the parent. Consolidated Op EBITDA rose Rs 2.37 Cr QoQ: the subsidiaries added Rs 2.67 Cr and the parent lost Rs 0.30 Cr. In the two prior reported quarters (Q2 FY26, Q1 FY27) the subsidiaries' margin was 2.4% and 2.5%. Q2 also carried a currency swing (FCTR -Rs 0.25 Cr in Q1, +Rs 2.18 Cr in Q2, L121) [INFERENCE]. Constant-currency margin is ND. The Q3 FY27 consolidated Op EBITDA margin separates a lasting step (at or above 11.04%) from a one-quarter step (at or below 8.36%)."

### Claim 2. "Trajectory: STEPPING UP." Revenue ran flat at 58-60 Cr a quarter through FY26, then stepped to 68.45 Cr and 73.30 Cr (A4 L244).

Strongest bear counter: the step was bought (inorganic), or it is currency, or the flat FY26 base is unproven.
Test against the extract:
- Inorganic: not supported. Neither half-year consolidated investing section has an acquisition line (L223-L231 hold only PPE, investments, FDs and interest). The consolidated balance sheet has no goodwill line, and intangibles fell to nil (L145). The perimeter is the same three WOS (L73-L76, L431).
- Currency: weak for Q1. Q1 FY27 revenue was 13.9% above the H2 FY26 average while FCTR was negative (-24.96, L121) [INFERENCE: rupee stronger in Q1]. Only part of Q2's +7.1% QoQ can be currency.
- Flat base: true as a wording point only. Q3 and Q4 FY26 are ND (A4 L241). FY26 H2 averaged 60.09 Cr (S7).
Survives: NO. The consolidated step is real on the extract. The residual is wording (S7).

### Claim 3. "Parent receivables built at March and cleared in H1 in both years; that favours intercompany timing over a one-off round-trip" (A4 L339; analyst note), the benign reading of A3-06.

Strongest bear counter: the 41.13 Cr injection (L405) funded the perimeter's payment of about 20.27 Cr of parent receivables (L395). The parent's own cash came back as "collections", which inflates standalone CFO (3.65x PAT).
Test against the extract:
- The perimeter did not need parent cash. At 31-Mar-2026 it held 104.29 Cr of current investments (c: L154 10,762.47 less L336 333.96) and 5.16 Cr of cash (c: L156 2,101.47 less L338 1,585.66).
- The same pattern ran in H1 FY26 with no injection: parent receivables -18.67 Cr (L395); consolidated -2.02 Cr (L216); injection cell nil (R522).
- After the injection the perimeter bought 32.64 Cr of investments (c: L226 3,293.77 less L406 30.00). That matches the injection's size and use better than a round-trip does.
- A second intercompany balance existed at March: the parent's other financial assets (current) exceeded the consolidated figure by 470.08 (c: L341 less L159).
Survives: NO. A4's reading holds on the extract. A4 already says standalone CFO is not clean cash (A4 L327).

### Mandatory purchase-economics probe

The filing describes two purchases: an investment in a wholly owned subsidiary (L405) and a buyback of the company's own shares (L235, L415). "Purchase of investments" (L226, L406) is treasury. Consolidated non-current investments are nil at 30-Sep-2026 (L147), so no strategic stake was bought.

(a) Investment in a wholly owned subsidiary, 4,113.13 (L405).
- At group level this is not an acquisition. The consolidated cash flow has no acquisition line (L223-L231), there is no goodwill line, and the perimeter is unchanged (L73-L76, L431). The holding stays 100%.
- Price / target PAT measures nothing here: no stake changed hands and no earnings were bought. For the record: 41.13 Cr / FY26 perimeter PAT 7.06 Cr (c: L115 3,042.97 less L301 2,336.93) = 5.8x.
- Perimeter quality markers: cash-rich (136.92 Cr current investments at 30-Sep-2026, c); no borrowings (L178 nil); EBITDA margin 2.4% to 2.5% until Q2.
- Bear reading: idle offshore treasury, or a pre-funded deal not yet disclosed. A4 already carries both (A4 Q4, Q5; forward map row 2). No graft.

(b) Buyback, 1,498.00 including transaction costs (L235, L415).
- Shares: 8,50,000 (c: L124 3,113.06 less 3,028.06 = 85.00 / Rs 10). Average cost: about Rs 176.24 a share (A4 c). Price, route and dates: ND (A4 L54).
- Multiple on reported earnings: Rs 176.24 / FY26 basic EPS Rs 9.77 (L127) = 18.0x trailing.
- Quality markers: net cash at 31-Mar-2026 was 16,959.49 (A4 c: L154, L156, L157, L147, L178), or Rs 54.48 a share on 3,11,30,600 shares. That is 30.9% of the price. Debt nil after H1 repayment (L178, L233).
- Multiple on core earnings, ex-cash: (Rs 176.24 - Rs 54.48) = Rs 121.76 / FY26 core EPS ex-OI Rs 3.49 (c: 1,434.16 x (1 - 24.35%) / 3,11,30,600) = about 35x trailing. On the Q2 FY27 core run-rate (c: 681.20 x 4 x (1 - 24.83%) / 3,03,80,600 = Rs 6.74) it is about 18x.
- Bear reading: on trailing core earnings the buyback was not cheap. It looks fair only if the Q2 core run-rate holds. A4's "+2.6 pp EPS over PAT" (A4 L200) is a share-count effect, not a value effect. The extract cannot show the price was fair (CMP and peer multiples ND).
Survives: YES. Graft required (M2).
Graft text (A4 Step 0C, after L54): "Buyback economics: about Rs 176.24 a share = 18.0x FY26 basic EPS (Rs 9.77, L127). Net cash was Rs 54.48 a share at 31-Mar-2026, 30.9% of the price. Ex-cash, the price was about 35x FY26 core EPS ex-OI (Rs 3.49) and about 18x the Q2 FY27 core run-rate (Rs 6.74). The +2.6 pp EPS effect is share count only."

---

## FINDINGS (tagged)

| ID | Type | A4 location | Finding | Evidence | Fix | Loop |
|---|---|---|---|---|---|---|
| F1 | FACTUAL | A4 L493, L511, L550, L596, L669 | A4 names a transfer-pricing shift as the rival to real leverage for the group margin step. It names Q3 core PBT as the observation that separates them. QfM 1: "Decides whether the +318 bps group margin gain is real leverage or a move of margin between entities." Intercompany revenue and cost eliminate on consolidation (Note 2, L431). A transfer-price change moves EBITDA between the parent and the perimeter one for one and leaves the group figure unchanged. So the group gain cannot be "a move of margin between entities". Consolidated core PBT also cannot separate the two readings. | Consolidated Op EBITDA +236.98 QoQ and +346.95 YoY (c: L101, L106, L107, L110). Parent -29.61 QoQ, perimeter +266.59 (c: L287, L292, L293, L296). | Scope transfer pricing to WHERE profit sits: S-C gap, tax, cash location, the parent's standalone base. Rival reading for the group step: one quarter or currency-assisted (M1). Separator: Q3 FY27 consolidated Op EBITDA margin (at or above 11.04% vs at or below 8.36%). QfM 1 "Why it matters": "Decides where profit sits between the parent and the subsidiaries, which drives the S-C gap, tax and cash location. It cannot explain the group gain, which is the same under any transfer price." L596 bear fork: "Intercompany pricing moved profit to the subsidiaries; the parent's own base is weaker than reported." | A4 |
| F2 | FACTUAL | A4 L560 (and L65) | The sector bullet, labelled FILED, says the Codes "changed the wage base" and that Cybertech "expects a further charge when final rules arrive (Note 5)". Note 5 says neither. | L434: the company "has considered to restructure the compensation of its employees with effect from April 1, 2026" and booked the incremental impact in FY26 EBE, amount not given. L435: it "would provide appropriate accounting effect on the basis of such developments as needed". No amount, no direction, no wage-base statement. | L560: "FILED: four Labour Codes notified 21-Nov-2025 consolidate 29 labour laws (L434). FILED: Cybertech restructured compensation from 1-Apr-2026 and booked the incremental impact in FY26 EBE, amount ND (L434). FILED: it will book any further effect when final rules arrive; amount and direction ND (L435). INFERENCE: a cost item for every Indian IT employer." L65: "possible further EBE effect; amount and direction ND". | A4 |
| F3 | FACTUAL | A4 L306, L343, L445, L595, L658, L669 | Pre-WC 0.84x is called "underlying conversion below 1.0x" and "the true reading", and it is passed to /fttcp as the Pillar 2 fact. The numerator excludes 729.95 of income that PAT includes. | Like-for-like 1.20x to 1.23x H1 FY27 vs 1.05x to 1.15x H1 FY26 (Audit 2, F3 table). | Restate as in Audit 2 F3. | A4 |
| C1 | CONTRADICTION | A4 L597 (and L247, L534, L652) | The Q1 FY28 forks overlap. Bull: "above the FY26 run-rate of 58-60 Cr". Bear: "stalls near Q1 FY27's 68.45 Cr". A 60-70 Cr print satisfies both. The bull fork also sits below the Step 3 trajectory bar of revenue at or above 73.30 Cr (A4 L247), so a fall of up to 18% from Q2 FY27 would read as bull. A4 L534, L597 and L652 call Q1 FY28 the "fourth" reading; it is the fifth quarter after the step (Q1-Q4 FY27, Q1 FY28). | A4 L247, L597; L100 | Bull: "Q1 FY28 revenue at or above Rs 73.30 Cr (Q2 FY27 level)". Bear: "Q1 FY28 revenue back toward the FY26 average of Rs 58-60 Cr". Between the two: unresolved. Relabel "fifth quarter". | A4 |
| M1 | MISSING | Step 2C item 3, Step 3, brief L545-L550, analyst note | The surviving bear counter to Claim 1 (one quarter, all QoQ gain outside the parent, currency swing) is absent. | Audit 3, Claim 1 | Graft the Claim 1 text. | A4 |
| M2 | MISSING | Step 0C (A4 L54), Step 2A (A4 L200) | The buyback purchase-economics multiple is absent, yet the review states the buyback's EPS accretion. | Audit 3, probe (b) | Graft the probe (b) text. | A4 |

---

## VERDICT

INCOMPLETE. Failing agent: A4. Types: FACTUAL (F1, F2, F3), CONTRADICTION (C1), MISSING (M1, M2).
Exact gap: re-scope the transfer-pricing reading so it cannot explain the consolidated margin step, and name the one-quarter or currency reading with the Q3 consolidated margin as separator (F1, M1). Correct the Labour Code bullet to Note 5's wording (F2). Restate pre-WC conversion like-for-like and fix the Pillar 2 fact and the L595 fork (F3). Rebuild the Q1 FY28 forks and fix "fourth" to "fifth" (C1). Graft the buyback multiple (M2).
No A2 loop: coverage passes; the 33 uncaptured units are STYLE. No A3 loop: no orphan row, no missed forensic that changes a finding.
A4's protocol verdict (PROCEED WITH FLAGS) and cash classification (INDETERMINATE-WITH-DIRECTION) are not contradicted by these findings. F3 improves the underlying cash reading; the H2 reversal risk still binds. The 12.15 Cr item ties to a Rs 4.00 dividend to the paisa (S10), which softens one leg of the FLAGS basis but does not remove it: 41.13 Cr into an unnamed subsidiary, the undisclosed buyback terms and the document-control errors still stand.

---

## STYLE NOTES (logged, no loop)

- S1. Coverage scope: 33 boilerplate units are absent from A1's structured file and A2's ledger: 18 embedded numbers, 9 entities, 1 date, 5 formula-caption qualifiers (list in Audit 1). A2's auditor-paragraph mapping is by qualifier, not by paragraph. For future runs, A1 should capture the page-3 and page-7 telephone and fax (L96, L282), because they evidence A3-20.
- S2. A4 L15 marks every row reviewed in one blanket statement. Row-range "reviewed, no finding" markers for the uncited balance-sheet lines and identifier rows would make the orphan check mechanical. A5 re-reviewed those rows; no item is unaddressed.
- S3. Brief L551, "Most of it came from higher payables and liabilities": the antecedent is unclear. The liability line (L218, 1,112.60) is 39% of CFO (L222, 2,826.32). The WC release explains the excess over PAT (1,010.87), not most of CFO. Suggested: "The working-capital release explains the cash above profit, and it can reverse." Step 5C L344, "The release came from liabilities, not assets": liabilities were 85.2% of the release and assets 14.8% (c: L216 27.40 + L217 165.74 of L219 1,305.74).
- S4. Brief L548, "The growth and the margin gain both sit in the US subsidiaries": YoY the perimeter supplied 70.8% of revenue growth and 81.2% of Op EBITDA growth (c: 281.56 / 346.95), and all of the QoQ gain. Say "most of". The perimeter includes Canada and intercompany eliminations, so "US subsidiaries" is shorthand.
- S5. Brief L546, "Treasury income fell Rs 3.21 Cr": the line is Other Income. A4's own L225 shows 5.64 Cr a half of it is not itemised, and 561.47 of the H1 FY27 residual sits in the parent (c: L287 723.59 less L387 140.54, L390 2.89, L391 18.69). Say "Other income".
- S6. A4 L337, L571, L655, "95.1% of group current investments now sit in the subsidiaries", is cited as evidence that treasury is moving offshore. At 31-Mar-2026 the share was 96.9% (c: 10,428.51 / 10,762.47), so the share fell. The absolute rise (104.29 to 136.92 Cr) and the parent's net cash fall (53.14 to 25.76 Cr) carry the point. Cite those instead.
- S7. A4 L244, "ran flat at 58-60 Cr a quarter through FY26" and "3.46-3.78 Cr a quarter": Q3 and Q4 FY26 are ND (A4 L241). The H2 averages are 60.09 Cr and 3.55 Cr. Say "averaged".
- S8. A4 L561 labels "the rupee weakened in Q2" FILED; A4 L180 tags the same reading [INFERENCE]. Use one tier: the FCTR is filed, the rupee reading is inference.
- S9. Optional sharpening. Q9 / A3-05 (A4 L501): consolidated FV gain H1 FY27 (L212, 18.69) equals standalone (L391, 18.69). So the perimeter booked zero fair-value gain in H1 FY27, against 155.23 in H1 FY26 (c: 264.50 less 109.27). Perimeter interest and dividend income was 565.23 (c: L206 705.77 less L387 140.54), close to perimeter OI of 568.19. The Q1 4.35 Cr vs Q2 1.33 Cr swing therefore cannot be even interest accrual. Q6 (A4 L498): 22.04 Cr of the 25.94 Cr sits in the subsidiaries (Audit 1).
- S10. The 12.15 Cr item (A4 L321, L495, L552): the standalone gap of 1,215.22 equals Rs 4.00 x 3,03,80,600 closing shares exactly. Stating the tie firms the dividend reading. The filing still does not confirm it.
- S11. A4 L18 treats the standalone H1 FY26 buyback cell (L415) as ND. The H1 FY26 financing total (L418, -458.03) ties without it (-402.20 - 42.72 - 13.11), so the cell is nil.
- S12. A1 artifact: R121, R122, R394 and R395 are rows for blank Other-equity cells, against A1's own header rule (structured file L9). No value is lost. Logged for A1, which is outside the loop set.

---

```yaml
stage: A5-adversary
company: "CYBERTECH"
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
  - {metric: "H1 CFO pre-WC after tax / PAT read as 'underlying conversion below 1.0x' and 'the true reading' (A4 L306, L343, L445, L595, L658, L669)", a4_value: "0.84x H1 FY27, 0.64x H1 FY26 (ratio arithmetic correct); conclusion 'below 1.0x'", recomputed: "like-for-like 1.20x vs 1.15x (PAT less after-tax removed income 729.95 / 977.74 lakh) or 1.23x vs 1.05x (interest and dividend income 705.77 / 692.82 lakh added back); above 1.0x on both bases", source_line: "L214, L221, L204, L206, L209, L210, L211, L212, L115"}
surviving_bear_counters:
  - {claim: "Core PBT ex-OI +97.1% YoY; the flat profit hides a better business (A4 L197, L222, L289, L545)", counter: "One quarter, with all of the QoQ gain outside the parent: consolidated Op EBITDA +236.98 lakh QoQ = perimeter +266.59 and parent -29.61; perimeter margin 2.4% and 2.5% in the two prior reported quarters; FCTR swung from -24.96 to +217.88 lakh in Q2; H1 OI still 53.47% of PBT. The valid rival reading is a one-quarter or currency-assisted step, not transfer pricing; separator is Q3 FY27 consolidated Op EBITDA margin (>=11.04% vs <=8.36%).", source_line: "L101, L106, L107, L110, L121, L287, L292, L293, L296", type: MISSING}
  - {claim: "Buyback adds 2.6 pp to EPS over PAT (A4 L200); terms ND (A4 L54)", counter: "Purchase-economics probe: about Rs 176.24 a share = 18.0x FY26 basic EPS Rs 9.77; net cash Rs 54.48 a share = 30.9% of the price; ex-cash about 35x FY26 core EPS ex-OI Rs 3.49 and about 18x the Q2 FY27 core run-rate Rs 6.74. The EPS gain is share count only; the price was full on trailing core earnings.", source_line: "L124, L127, L235, L415, L110, L101, L112-L114, L147, L154, L156, L157, L178", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4 L493, L511, L550, L596, L669): transfer pricing named as the rival reading of the group margin step, with Q3 core PBT as separator. Intercompany items eliminate on consolidation (L431), so the group gain (+236.98 lakh QoQ, +346.95 lakh YoY Op EBITDA) is the same under any transfer price, and consolidated core PBT cannot separate the two readings."
    - "F2 (A4 L560, L65): sector bullet labelled FILED says the company 'expects a further charge' and the Codes 'changed the wage base'. Note 5 (L434-L435) says only that it 'would provide appropriate accounting effect ... as needed'; no amount, no direction, no wage-base statement."
    - "F3 (A4 L306, L343, L445, L595, L658, L669): pre-WC 0.84x called 'underlying conversion below 1.0x' and 'the true reading', and passed to /fttcp as the Pillar 2 fact. The numerator excludes 729.95 lakh of income (L204, L206, L210-L212) that PAT includes; like-for-like 1.20x-1.23x H1 FY27 vs 1.05x-1.15x H1 FY26."
  missing:
    - "M1: the surviving bear counter to the core-PBT claim (one quarter, all QoQ gain outside the parent, currency swing) is absent; graft into Step 2C item 3, Step 3 diagnostics, the brief and the analyst note."
    - "M2: the buyback purchase-economics multiple (18.0x reported EPS; about 35x core EPS ex-cash) is absent while the review states the buyback's EPS accretion; graft into Step 0C."
  contradiction:
    - "C1 (A4 L597, L247, L534, L652): Q1 FY28 forks overlap (bull 'above 58-60 Cr', bear 'stalls near 68.45 Cr'; a 60-70 Cr print satisfies both), and the bull fork sits below the Step 3 bar of revenue >= 73.30 Cr. Q1 FY28 is called the 'fourth' reading; it is the fifth quarter after the step."
  style:
    - "S1 coverage: 33 boilerplate units uncaptured (18 embedded numbers, 9 entities, 1 date, 5 formula captions); A1 should capture L96/L282 telephone and fax (A3-20 evidence)"
    - "S2 A4 L15 blanket 'no row unreviewed' instead of row-range 'reviewed, no finding' markers"
    - "S3 brief L551 'Most of it came from higher payables' (liabilities = 39% of CFO; they explain the excess over PAT); L344 'not assets' (assets 14.8% of release)"
    - "S4 brief L548 'growth and margin gain both sit in the US subsidiaries' (70.8% of YoY revenue growth, 81.2% of YoY Op EBITDA growth)"
    - "S5 brief L546 'Treasury income' should read 'Other income' (5.64 Cr a half not itemised)"
    - "S6 '95.1% now sit in the subsidiaries' used as a trend; share was 96.9% at 31-Mar-2026"
    - "S7 A4 L244 'flat at 58-60 Cr ... through FY26': Q3/Q4 FY26 ND; say 'averaged'"
    - "S8 A4 L561 rupee reading labelled FILED, L180 labels it INFERENCE"
    - "S9 optional: perimeter FV gain H1 FY27 = 0 (L212 = L391); perimeter OI = interest and dividend income; 22.04 Cr of 25.94 Cr OCL in subsidiaries"
    - "S10 12.15 Cr gap = Rs 4.00 x 3,03,80,600 shares exactly; state the tie"
    - "S11 standalone H1 FY26 buyback cell is nil (L418 ties without it), not ND"
    - "S12 A1 rows R121, R122, R394, R395 for blank cells against A1's own rule; no value lost"
loop_back_to: "A4"
gap: "A4: (F1, M1) re-scope transfer pricing to where profit sits, since it cannot move the consolidated margin; name the one-quarter or currency reading for the group step with Q3 consolidated Op EBITDA margin as separator (A4 L493, L511, L550, L596, L669) and graft the Claim 1 counter. (F2) rewrite the Labour Code sector bullet L560 and L65 to Note 5's wording. (F3) restate pre-WC conversion like-for-like (1.20x-1.23x vs 1.05x-1.15x) at L306, L343, L445, L658, analyst note; L595 bear fork to 'H2 FY27 CFO/PAT below 1.0x'. (C1) rebuild Q1 FY28 forks (bull >= 73.30 Cr, bear back toward 58-60 Cr) and change 'fourth' to 'fifth' at L534, L597, L652. (M2) graft the buyback multiple into Step 0C."
style_notes:
  - "S1 coverage boilerplate (33 units; capture L96/L282 next run)"
  - "S2 blanket review mark vs row-range markers"
  - "S3 brief cash wording L551; L344 'not assets'"
  - "S4 'both sit in the US subsidiaries' should be 'most of'"
  - "S5 'Treasury income' should be 'Other income'"
  - "S6 95.1% share cited as a trend; was 96.9% at Mar-26"
  - "S7 FY26 'flat' is an average; Q3/Q4 ND"
  - "S8 rupee reading tier mismatch FILED vs INFERENCE"
  - "S9 optional sharpening of Q9 and Q6"
  - "S10 state the exact Rs 4.00 dividend tie"
  - "S11 standalone H1 FY26 buyback cell is nil"
  - "S12 A1 blank-cell rows"
analyst_note: "A4's arithmetic is clean: every cell, bridge and ratio recomputes to the filed lines, and all six statements foot. The failures are readings. (1) Transfer pricing is named as the rival to real leverage for the group margin step, with Q3 core PBT as the separator. Intercompany items eliminate on consolidation, so the group gain is the same under any transfer price and consolidated core PBT cannot separate the two. The live rival is a one-quarter or currency-assisted step. (2) The 0.84x 'underlying conversion' divides cash without 7.3 Cr of treasury income by PAT with it; like-for-like it is 1.20-1.23x, so the Pillar 2 fact passed to /fttcp is understated. Cash stays INDETERMINATE-WITH-DIRECTION on H2 reversal risk. (3) Note 5 does not say a further charge is expected. (4) The Q1 FY28 forks overlap. Buyback probe: 18.0x trailing EPS, about 35x trailing core EPS ex-cash. The 12.15 Cr equity gap equals Rs 4.00 x 3,03,80,600 shares to the paisa, which firms the dividend reading. Coverage holds; 33 uncaptured units are boilerplate (STYLE). All fixes sit in A4; no A2 or A3 loop."
```
