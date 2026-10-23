# A5 ADVERSARY / COMPLETENESS AUDIT, TINNARUBR Q2 FY27

Stage: A5-adversary | Model: claude-opus-5-5 | Date: 2026-10-23
Under audit: runs/tinnarubr-q2fy27/work/review_tinnarubr_q2fy27.md (744 lines)
Inputs read: A1 fulltexts (results 1,430 lines; release 145 lines), A1 structured files (results R001-R927; release R001-R138), A2 ledgers (both), the A4 review. Not opened: source PDFs, anything under inputs/, A3 forensics, orchestrator commentary.

Line convention. RV L = review line. RF L = results fulltext line. PF L = release fulltext line. R### = A1 results row. PR R### = A1 release row. Rs crore = Rs lakhs x 0.01. [derived] = my arithmetic on cited filed cells.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Part | Heading | Content found | Status |
|---|---|---|---|
| 1. Summary narrative | RV L597 | 15 lines (RV L599-L613), about 260 words: YoY, QoQ, cash, debt, Panipat, overseas, next test | present |
| 2. Sector intelligence | RV L615 | 5 bullets: demand driver, seasonality, regulation (bull and bear reading), input cycle, feedstock | present |
| 3. Business-model intelligence | RV L623 | 6 bullets: revenue engine, unit economics, three drift lines, overseas book | present |
| 4. Competition intelligence | RV L632 | 6 bullets: peers NOT FOUND stated, candidate peer marked INFERENCE and PENDING LIVE VERIFICATION, scale claims, credit, weak points, EPR risk with both readings and a separating observation | present |
| 5. Forward map | RV L641 | make-or-break reading plus 9 catalyst rows, each with a bull fork and a bear fork; 6 rows dated, 3 labelled "undated" honestly | present |

Gate: PASS. All five parts are present and carry real content.

---

## 1. COVERAGE AUDIT

Method. A fresh grep over each A1 fulltext (embedded layer and [OCR page N] block of the same page counted once, never twice) and a row-type count over each structured file, diffed against the A2 ledgers. Then a trace of ledger rows into the review.

### 1A. Results (Reg 33 filing)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 10 | 10 (SA: RF L624, L627, L632, L635, L641; CO: RF L1243, L1246, L1251, L1254, L1260) | none | PASS |
| Line items (groups) | 226 | 226 (SA P&L 26, BS 39, CF 43; CO P&L 34, BS 39, CF 45) | none | PASS |
| Statement cells | 692 | 692 (SA 156 + 78 + 86; CO 204 + 78 + 90) | none | PASS |
| ZERO_STANDING cells | 81 | 81 (grep "\| ZERO_STANDING" on the structured file = 81) | none | PASS |
| Agenda items | 1 | 1 (results approval, RF L41-L44) | none | PASS |
| Auditor paragraphs | 12 | 12 (SA: RF L692, L699, L707, L718, L733; CO: RF L1308, L1316, L1323, L1335, L1343, L1356, L1364; OCR duplicates RF L1394, L1401 excluded) | none | PASS |
| Entities | 57 | 57 (ICAI at RF L709 / L1325 sits inside R890 / R922; the Land Acquisition Act at RF L650 sits inside R834; State Government at RF L650 sits inside R886) | none | PASS |
| FORWARD | 10 | 10 (Chile objective, scope, infusion; relocation; compensation; x2 statements) | none | PASS |
| DATE | 45 | 45 | none | PASS |
| QUALIFIER | 70 | 70 | none | PASS |
| Non-statement NUMBER | 53 | 53 | none | PASS |
| All row IDs | 927 | 927 (grep "^R\d{3} \|" = 927) | none | PASS |

Footing check of A1 cells (spot): SA CF operating items sum to 6,191.90 (R274), WC items to 1,864.09, cash generated 8,055.99 (R250), CFO 6,822.38 (R294); investing sums to (4,723.99) (R310); financing to (2,094.38) (R328); net change 4.01 (R330). CO CF foots the same way to 6,442.52 / 7,893.43 / 6,660.01 / (4,518.28) / 21.73 (R663, R633, R681, R697, R717). CO P&L Q2 FY27 expenses foot to 13,405.73 (R365). The A1 values of record are internally consistent.

### 1B. Press release (presentation slot)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Pages (slides) | 3 | 3 | none | PASS |
| NUMBER | 66 | 66 | none | PASS |
| ENTITY | 29 | 29 | none | PASS |
| FORWARD | 14 | 14 | none | PASS |
| DATE | 18 | 18 | none | PASS |
| QUALIFIER | 11 | 11 | none | PASS |
| All row IDs | 138 | 138 | none | PASS |
| Claim units with no A1 type slot | n/a | 5: PF L65 / L82 "record H1 profitability"; PF L67 "among the largest end-of-life tyre recyclers globally"; PF L139 "among the world's largest end-of-life tyre recyclers"; PF L90 "driven by infrastructure demand"; PF L127 "a growing share of high-value products" | not orphans (A1's NUMBER / ENTITY / FORWARD / DATE / QUALIFIER scheme has no slot for a present-tense characterisation claim) | LOGGED as STYLE S6. A4 uses four of the five by line (RV L448, L617, L636, L493). The "record" headline is not tested. |

### 1C. Ledger-to-review trace

A4 marks every category reviewed with counts that equal A2's (RV L18-L27: results 927, release 138). Flagged ledger rows trace into the review: CONSOLIDATION_LIST_GAP R773 / R791 to RV L73 (R-A3-18); PAGE_MISSING R927 to RV L78; UNREVIEWED_ENTITIES R926 to RV L78, L365; R771 vs R789 segment wording to RV L72; PR R091 South Africa to RV L516 (S17); PR R075 prior rating to RV L512 (S13); PR R132 / R133 to RV L342; PR R135 to RV L492 (Q6). R822 DATE_CONFLICT is covered by the blanket mark with no finding; A1 R871 resolves it as an embedded-layer error.

Result: orphan rows = none. Rows missing from the ledger = none. Coverage PASS.

Note. Two rows that are in the ledger and marked reviewed carry filed facts the review's analysis leaves out: R339-R340 / R727-R728 (Panipat land split) and R302 with R185-R186 (Rs 2.71 Cr into subsidiaries). These are review omissions, not ledger gaps. They are findings F5 and F6, routed to A4.

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4's tables was recomputed from A1 lakh cells. Rounding tolerance: 0.01 pp on percentages, 0.01 Cr on rupees, 0.1 day on days.

| # | Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | SA op EBITDA Q2 FY27 | 28.06 Cr | 2,229.79 + 386.46 + 262.20 - 72.54 = 2,805.91 lakh | R078, R060, R054, R018 (RF L257, L253, L252, L244) | PASS |
| 2 | SA op EBITDA margin Q2 FY27 / Q1 FY27 / Q2 FY26 | 18.76% / 21.97% / 18.50% | 18.760% / 21.971% (3,314.36 / 15,085.10) / 18.500% (2,161.86 / 11,685.68) | R012-R014 (RF L243) | PASS |
| 3 | SA op EBITDA H1 FY27 / H1 FY26 / FY26 | 61.20 / 41.47 / 91.77 Cr; 20.37% / 16.98% / 17.21% | 6,120.27 / 4,146.63 / 9,176.56 lakh; 20.373% / 16.983% / 17.209% | R081-R083, R063-R065, R057-R059, R021-R023, R015-R017 | PASS |
| 4 | CO op EBITDA Q2 FY27 and margin | 29.45 Cr; 18.81% | 2,326.13 + 427.80 + 263.65 - 72.54 = 2,945.04 lakh; 18.807% | R413, R401, R395, R353, R347 (RF L861, L858, L857, L849, L848) | PASS |
| 5 | CO op EBITDA Q1 FY27 / Q2 FY26 / H1 FY27 / H1 FY26 / FY26 | 33.90 / 21.56 / 63.35 / 42.35 / 93.52; margins 21.71 / 18.04 / 20.26 / 16.95 / 17.13% | 3,390.37 / 2,156.09 / 6,335.41 / 4,234.86 / 9,352.06; 21.708 / 18.040 / 20.256 / 16.954 / 17.134% | R414-R418, R402-R406, R396-R400, R354-R358, R348-R352 | PASS |
| 6 | Reported EBITDA SA / CO Q2 FY27 | 28.78 / 30.18 | 2,878.45 / 3,017.58 | as rows 1, 4 | PASS (all 12 cells) |
| 7 | Core PBT ex-OI SA Q2 FY27 / Q2 FY26 | 21.57 / 16.70 | 2,157.25 / 1,670.09 | R078 - R018; R080 - R020 | PASS |
| 8 | Core PBT ex-OI CO Q2 FY27 / Q2 FY26 | 22.54 / 16.21 | 2,253.59 / 1,621.18 | R413 - R353; R415 - R355 | PASS |
| 9 | ETR SA Q2 FY27 / Q2 FY26 | 27.97% / 27.15% | 623.72 / 2,229.79 = 27.972%; 459.84 / 1,693.64 = 27.151% | R102, R078, R104, R080 (RF L262, L257) | PASS |
| 10 | ETR CO Q2 FY27 / Q2 FY26 | 27.24% / 27.94% | 637.84 / 2,341.77 = 27.238%; 456.21 / 1,632.89 = 27.939% | R449, R425, R451, R427 | PASS |
| 11 | PAT margin SA / CO Q2 FY27 | 10.74% / 10.88% | 10.738% / 10.881% | R108 / R012; R491 / R347 | PASS |
| 12 | OI / PBT SA / CO Q2 FY27 | 3.25% / 3.10% | 3.253% / 3.098% (CO on post-associate PBT) | R018, R078; R353, R425 | PASS |
| 13 | SA gross material cost Q2 FY27 / Q1 FY27 / Q2 FY26 | 47.44 / 47.78 / 47.99% | 7,095.62 / 14,956.64 = 47.441%; 7,207.56 / 15,085.10 = 47.779%; 5,607.48 / 11,685.68 = 47.986% | R030-R032, R036-R038, R042-R044 (RF L248-L250) | PASS |
| 14 | SA Q1 FY26 [derived]: revenue, GMC, op margin | 127.30; 55.22%; 15.59% | 12,730.44; 7,029.27 = 55.216%; 1,984.77 = 15.591% | R016 - R014 and peers | PASS |
| 15 | SA H2 FY26 [derived]: revenue, GMC, op margin, SIT | 289.07; 53.09%; 17.40%; 7.91% | 28,907.29; 15,347.98 = 53.094%; 5,029.93 = 17.400%; 2,285.65 = 7.907% | R017 - R016 and peers | PASS |
| 16 | SA employee / other expenses / SIT shares, all 1D columns | e.g. 11.82 / 21.98 / 8.64% (Q2 FY27) | 11.817 / 21.981 / 8.641%; every 1D cell within 0.01 pp | R048-R053, R066-R071, R036-R041 | PASS |
| 17 | CO 1D cells | e.g. 46.10 / 12.54 / 22.55% (Q2 FY27) | 46.098 / 12.545 / 22.550% | R371-R412 | PASS |
| 18 | YoY SA: revenue / op EBITDA / D&A / fin / EBIT / OI / core PBT / PBT / PAT / EPS | +27.99 / +29.79 / +50.83 / +11.32 / +26.96 / +208.0 / +29.17 / +31.66 / +30.17 / +27.10% | 27.991 / 29.792 / 50.825 / 11.319 / 26.963 / 208.03 / 29.170 / 31.657 / 30.172 / 27.104% | R012/R014 ... R157/R159 | PASS |
| 19 | YoY CO: revenue / op EBITDA / D&A / fin / EBIT / OI / core PBT / PBT / PAT / EPS | +31.02 / +36.59 / +44.01 / +10.85 / +35.41 / +200.0 / +39.01 / +43.41 / +44.81 / +37.70% | 31.020 / 36.592 / 44.011 / 10.847 / 35.406 / 200.00 / 39.009 / 43.413 / 44.808 / 37.700% | R347/R349 ... R540/R542 | PASS |
| 20 | Margin change YoY SA / CO | +26 / +77 bps | +26.0 / +76.7 bps | rows 2, 5 | PASS |
| 21 | QoQ SA: revenue / margin / core PBT / employee cost | -0.85% / -321 bps / -18.26% / +16.8% | -0.852% / -321.1 bps / -18.259% / +16.81% | R012/R013, R078/R079, R048/R049 | PASS |
| 22 | QoQ CO: revenue / op EBITDA / margin / PAT | +0.26% / -13.13% / -290 bps / -17.15% | +0.264% / -13.135% / -290.1 bps / -17.150% | R347/R348, R491/R492 | PASS (op EBITDA rounds to -13.14%; rounding only, S1) |
| 23 | CO Q2 FY26 revenue QoQ | -8.25% | -8.255% (rounds to -8.26%) | R349, R351 | PASS (rounding only, S1) |
| 24 | SA PAT QoQ (verdict card RV L583) | -20.15% | 1,606.07 / 2,011.22 - 1 = -20.144% | R108, R109 | PASS (rounding only, S1) |
| 25 | Q2 margin fall split, SA | +179 / +176 / -34 = 321 bps | +178.7 / +176.2 / -33.8 = 321.1 bps | 1D | PASS |
| 26 | SA PAT bridge (revenue / margin / D&A / finance / OI / tax at prior ETR / ETR change) | +6.05 / +0.39 / (1.30) / (0.27) / +0.49 / (1.46) / (0.18); total +3.72 | +605.13 / +38.92 / -130.23 / -26.66 / +48.99 / -145.57 / -18.30 = 372.28 lakh vs filed 372.27 | R012, R014, R060, R062, R054, R056, R018, R020, R078, R080, R102, R104, R108, R110 | PASS |
| 27 | CO PAT bridge (as above plus associate) | +6.69 / +1.20 / (1.31) / (0.26) / +0.48 / +0.28 / (1.98) / +0.16; total +5.27 | +668.82 / +120.14 / -130.74 / -25.80 / +48.36 / +28.11 / -198.05 / +16.42 = 527.26 lakh vs filed 527.25 | R347-R491 cells | PASS |
| 28 | OI reverts to Q2 FY26: PAT SA / CO | 15.71 (+27.3%) / 16.69 (+41.8%) | 1,570.78 (+27.31%) / 1,668.74 (+41.82%) | R018-R020, R102, R108, R110; CO peers | PASS |
| 29 | WC change SA H1 FY27 / H1 FY26 | +18.64 / (15.66) | 8,055.99 - 6,191.90 = 1,864.09; 2,640.16 - 4,206.53 = -1,566.37 | R250, R274, R251, R275 (RF L535-L545) | PASS |
| 30 | WC change CO H1 FY27 / H1 FY26 | +14.51 / (40.67) | 7,893.43 - 6,442.52 = 1,450.91; 326.60 - 4,394.05 = -4,067.45 | R633, R663, R634, R664 | PASS |
| 31 | CFO / PAT SA H1 FY27 / H1 FY26; CO H1 FY27 / H1 FY26 | 1.89x / 0.89x; 1.77x / (0.12)x | 1.886 / 0.887; 1.771 / -0.115 | R294, R111, R295, R112; R681, R494, R682, R495 | PASS |
| 32 | CFO ex-WC / PAT SA H1 FY27 / H1 FY26; CO H1 FY27 | 1.37x / 1.56x; 1.39x | 4,958.29 / 3,617.29 = 1.371; 3,634.67 / 2,332.06 = 1.559; 5,209.10 / 3,760.57 = 1.385 | as rows 29-31 | PASS |
| 33 | FCF SA / CO | 23.48, (32.52) / 21.31, (31.75) | 2,348.42, -3,252.03 / 2,131.31, -3,174.92 | R294-R297; R681-R684 | PASS |
| 34 | Receivable days SA / CO | 44.7 to 31.6 / 44.8 to 33.1 | 44.69 to 31.56 / 44.78 to 33.12 | R202, R017, R201, R015; R581, R352, R580, R350 | PASS |
| 35 | Inventory days on GMC SA / CO | 92.4 to 98.8 / 99.2 to 105.9 | 92.37 to 98.80 / 99.18 to 105.87 | R200, R199; R579, R578 | PASS |
| 36 | Payable days SA / CO | 77.8 to 74.7 / 79.8 to 78.4 | 77.75 to 74.75 / 79.83 to 78.38 | R237-R240; R620-R623 | PASS |
| 37 | CCC SA 30-Sep-2026 | 55.7 days | 55.61 days (A4 summed rounded parts) | rows 34-36 | PASS (rounding only, S1) |
| 38 | Gross borrowings CO and decline | 120.63 to 111.42; -7.63% | 12,062.69 to 11,142.36; -7.630% | R605 + R617, R604 + R616 (RF L1023, L1031) | PASS |
| 39 | Net debt CO; net D/E | 116.84 to 106.88; 0.39x to 0.32x | 11,684.38 to 10,688.39; 0.389x to 0.321x | R582-R585, R600, R601 | PASS |
| 40 | Debt with leases, decline | 129.12 to 121.91; -5.58% | 12,911.66 to 12,190.58; -5.585% | R606-R607, R618-R619 | PASS |
| 41 | ICR CO H1 FY27 / FY26; SA H1 FY27 | 9.91x / 7.49x; 9.73x | 5,476.32 / 552.70 = 9.908; 8,122.81 / 1,085.00 = 7.486; 5,345.97 / 549.58 = 9.727 | R398, R400, R404, R406; R057, R063 | PASS |
| 42 | SA-CO PAT gap % of SA PAT, 6 columns | -4.63 / +2.26 / +6.09 / +0.80 / +3.96 / -0.73% | -4.630 / +2.258 / +6.093 / +0.802 / +3.961 / -0.729% | R108-R113, R491-R496 | PASS |
| 43 | Q2 FY27 PAT gap split | subs +0.93; assoc + JV +0.16 (JV -0.25, assoc +0.41); eliminations -0.11 | 93.35; 15.64 (-24.98, +40.62); 97.86 - 93.35 - 15.64 = -11.13 | R733, R419, R738 (RF L1367, L862, L1370) | PASS |
| 44 | Intra-group share of Q2 subsidiary revenue | 37.5%; Rs 4.21 Cr | (1,123.67 - 702.68) / 1,123.67 = 37.47%; 420.99 lakh | R732, R347 - R012 | PASS |
| 45 | Unreviewed exposure Q2 / Q1 | 6.94% / 3.39% of CO PAT | (93.35 + 24.98) / 1,703.93 = 6.945%; (22.56 + 47.22) / 2,056.64 = 3.393% | R733-R734, R738-R739, R491-R492 | PASS |
| 46 | Oman H1 EBITDA ceiling | about 2.29 Cr | 11.5% x 1,995.11 lakh = 2.294 Cr | PR R055, R745 | PASS |
| 47 | HSIIDC demand / Q2 SA PAT | 23.2% | 373.27 / 1,606.07 = 23.24% | R341, R108 | PASS |
| 48 | Implied weighted shares Q2 FY26 SA / CO; H1 FY26 SA / CO | 176.0 / 171.3; 173.9 / 171.5 lakh | 176.01 / 171.28; 173.90 / 171.46 | R110 / R159, R493 / R542; R112 / R161, R495 / R544 | PASS |
| 49 | Dividend per share H1 FY27 | Rs 3.25 | 585.52 / 180.158 = 3.250 | R324, R145 | PASS |
| 50 | Release H1 tie-outs: revenue / PAT / EBITDA | +25.21 / +59.97 / +49.60% | 25.214 / 59.973 / 49.601% | R350 / R351, R494 / R495, row 5 | PASS |
| 51 | PCMB share of H1 CO revenue; Andhra / CO equity | 8.6%; 75% | 27 / 312.77 = 8.63%; 250 / 332.85 = 75.1% | PR R042, R350; PR R048, R600 | PASS |

Mismatches above rounding: none. Four residuals sit at the rounding edge (rows 22, 23, 24, 37); logged as STYLE S1.

---

## 3. ADVERSARIAL READ

The three most positive claims in A4, each attacked from the same extracted text.

### Claim 1. "So the year-on-year growth is real and does not lean on treasury income" (RV L602), with "That beats the release's own Vision 2029 pace of 'over 25%' CAGR" (RV L225).

Strongest bear counter. The quality half holds: other income is 3.25% of SA PBT (R018, R078). The pace half does not hold on the half year. SA H1 FY27 revenue grew 23.04% [derived: 30,041.74 / 24,416.12; R015, R016, RF L243], below the "over 25%" Vision pace (PR R058, PF L133-L134). CO H1 grew 25.21% (R350, R351), at the floor, not above it. The Q2 rate rides a soft base: Q2 FY26 SA revenue fell 8.21% QoQ (RV L243). Q2 FY27 SA revenue is only 3.48% above the H2 FY26 quarterly average [derived: 149.57 vs 144.54; (R017 - R016) / 2], and CO only 5.80% [156.59 vs 148.01; (R352 - R351) / 2]. The step-up happened in H2 FY26. FY27 adds little in sequence.

Survives: YES, on pace. A4 shows the plateau (RV L260) but leaves "beats the Vision pace" unqualified and never states the 23.04%. Graft required (finding F3).

### Claim 2. "Net debt fell about 10 Cr while 44.74 Cr of capex was spent, funded by CFO" (RV L349); "FCF ... Turned positive" (RV L322); narrative RV L606-L608.

Strongest bear counter. The working capital release paid for the whole debt fall. SA H1 FY27 cash before debt flows = CFO 6,822.38 (R294) less investing 4,723.99 (R310), interest paid 493.58 (R326), dividend 585.52 (R324), lease principal 38.23 (R320) and lease interest 48.58 (R322) = 932.48 lakh, Rs 9.32 Cr [derived]. Net borrowings fell 928.47 lakh (R314 + R316 + R318), and cash rose 4.01 (R330); this foots. The WC release was 1,864.09 lakh (R250 less R274). Without it, the half shows a deficit of 931.61 lakh, Rs 9.32 Cr: debt would have risen about Rs 9.3 Cr, not fallen Rs 9.9 Cr. CO: pre-debt cash 942.07 lakh [R681 less R697, R713, R711, R707, R709]; WC release 1,450.91 (R633 less R663); deficit without it 508.84 lakh, Rs 5.09 Cr. The release itself rests on a September versus March comparison (A4-04, RV L565). A receivables rebuild in the Q3 and Q4 road season reverses it.

Survives: YES. A4 states the WC split and the seasonal caveat but does not link them to the debt fall. "Funded by CFO" reads as funded by earnings. Graft required (finding F2).

### Claim 3. "Model drift toward manufacturing ... Lower trading share lines up with the gross margin gain" (A4-06, RV L567); brief RV L627; sector RV L620 "Raw material cost fell from 51.76% to 47.61%".

Strongest bear counter. A4's own Step 1D series (RV L172, L176) does not show the link. Pairs of (stock-in-trade share, gross material cost share), SA: Q1 FY26 15.76%, 55.22%; Q2 FY26 13.97%, 47.99%; H2 FY26 7.91%, 53.09%; Q1 FY27 6.21%, 47.78%; Q2 FY27 8.64%, 47.44%. H2 FY26 had the second-lowest trading share and the second-highest material cost. The H1 gain of 415 bps comes from one outlier quarter, Q1 FY26 at 55.22%. Like for like, Q2 FY27 against Q2 FY26, material cost fell only 55 bps while the trading share fell 533 bps. Own material consumed rose from 38.38% of revenue [R032 / R014] to 43.01% [R030 / R012]. The shift to own manufacturing is filed. A gross margin gain from that shift is not.

Survives: YES. A4 marks the link INFERENCE, but its own table contradicts the inference, and the brief carries the H1 gain as a structural drift. Graft required (finding F4).

Considered and not ranked in the top three: "The overseas book moved from a drag to a contributor" (RV L365). A4 already carries three binding caveats there. One sharpening is logged as STYLE S9.

### MANDATORY ACQUISITION-ECONOMICS PROBE

Neither document describes a purchase of an existing business with stated earnings. The price-to-target-PAT multiple therefore has no target. Three items come closest, and each is tested as far as the extract allows.

| Item | Economics from the extract | Multiple | Bear reading | Outcome |
|---|---|---|---|---|
| (a) Tinna Rubber Chile SpA, new wholly owned subsidiary (Note 4; RF L635-L639; R773, R883) | Greenfield incorporation. Authorised CLP 500,000,000 (R337). INR capital NOT FOUND. "Capital infusion is under process" (R805). No earnings. | not computable (no target PAT) | Scope includes battery and plastic waste (R804), with no capex or licence plan. A4 carries this (RV S6 L505). | no new graft |
| (b) Rs 2.71 Cr invested in subsidiaries in H1 FY27 (R302, RF L554; SA carrying value 13.32 to 16.03 Cr, R186, R185) | The two consolidated subsidiaries: H1 PAT Rs 1.16 Cr (R734), Q2 Rs 0.93 Cr (R733), total assets Rs 31.96 Cr (R731), no debt or cash figure filed, customer tenure NOT FOUND. | carrying value 16.03 Cr / annualised H1 PAT 2.32 Cr = about 6.9x; on the Q2 run-rate (3.73 Cr) about 4.3x [derived] | The low multiple rests on management-certified, unreviewed profit (R926), 37.5% intra-group Q2 revenue, and one quarter's step (Q1 0.23 Cr to Q2 0.93 Cr). The earnings year is not shown to be representative. The bear reading survives and A4 already carries it (R-A3-05, R-A3-07; RV L365). New element: A4 never states the Rs 2.71 Cr infusion or its recipient. | graft as F6 |
| (c) Panipat land, compulsory acquisition by HSIIDC (Note 5); the company is the seller | Compensation sanctioned and deposited, amount NOT FOUND (R886). Relocation cost NOT FOUND. HSIIDC demand Rs 3.73 Cr (R341) = 23.2% of Q2 SA PAT. | not computable | A4 carries the open amounts (S1-S3, RV L500-L502). Missing: the land split that bounds the dispute. | graft as F5 |

---

## 4. FINDINGS (tagged; only FACTUAL, MISSING, CONTRADICTION loop)

| ID | Type | Loop to | Exact gap | Evidence | Fix (graft text for A4) |
|---|---|---|---|---|---|
| F1 | FACTUAL | A4 | Step 6D PCMB row, killing-evidence cell (RV L432): "group margin fell in Q2 on higher PCMB share". No document gives a Q2 PCMB revenue split; the release gives H1 only (PR R042-R043, PF L105). The cell also contradicts A4's own attribution of the Q2 fall to employee cost (+179 bps) and other expenses (+176 bps), with material -34 bps (RV L261). | PR R042-R043; RV L261; 1D | Replace the cell with: "Q2 PCMB split ND (release gives H1 only, PR R042-R043); the Q2 margin fall traces to employee and other expenses, not material (Step 3C); PCMB margin ND". |
| F2 | MISSING | A4 | Surviving bear counter to Claim 2: the Rs 10 Cr debt fall is funded wholly by the WC release. | Claim 2 above; R294, R310, R326, R324, R320, R322, R314, R316, R318, R250, R274; CO R681, R697, R713, R711, R707, R709, R633, R663 | Append to RV L349: "The working capital release paid for the whole fall. SA H1 cash after capex, investments, interest, dividend and leases was Rs 9.32 Cr [derived], against a WC release of Rs 18.64 Cr. Without the release the half needed about Rs 9.32 Cr of new debt (CO Rs 5.09 Cr). The release compares September with March (A4-04), so an H2 receivables rebuild would reverse the fall." Add to RV L608: "The working-capital release paid for the whole debt fall; without it, debt would have risen about Rs 9 Cr (FILED, derived)." Add the same clause to flag 6 (RV L589) and the CASH flag (RV L730). |
| F3 | MISSING | A4 | Surviving bear counter to Claim 1: SA H1 revenue +23.04% sits below the 25% pace that RV L225 says Q2 beats; Q2 rides a soft base. | Claim 1 above; R015, R016, R350, R351, R017, R352; PR R058 | Replace the second sentence of RV L225 with: "The Q2 rate rides a soft base (Q2 FY26 fell 8.21% QoQ). On the half, SA revenue grew 23.04% (300.42 vs 244.16 Cr), below the Vision 2029 'over 25%' pace; CO grew 25.21%, at the floor. Q2 FY27 sits 3.48% (SA) and 5.80% (CO) above the H2 FY26 quarterly average." Add after RV L602: "The pace is lower than the Q2 rate suggests: standalone H1 revenue grew 23.04% (FILED, derived)." |
| F4 | MISSING | A4 | Surviving bear counter to Claim 3: the H1 material cost gain is a Q1 FY26 base effect; the quarter series shows no link from trading share to gross margin. | Claim 3 above; 1D RV L172, L176; R030, R032, R012, R014 | In A4-06 (RV L567) replace "Lower trading share lines up with the gross margin gain [INFERENCE on the link]" with: "The H1 material cost gain comes from one weak quarter (Q1 FY26 at 55.22%). Like for like, Q2 material cost fell 55 bps while the trading share fell 533 bps, and H2 FY26 paired a 7.91% trading share with 53.09% material cost. The filed series does not support a link from trading share to gross margin. Own material consumed rose from 38.38% to 43.01% of Q2 revenue." Apply the same qualifier to RV L620 and RV L627. |
| F5 | MISSING | A4 | Note 5 land split is absent from the review (0D Note 5 row RV L74, Q2 RV L488, S2 RV L501, narrative RV L609). Of 34 kanals 8 marlas, 20 kanals 12 marlas were released from acquisition and stay in possession; 13 kanals 16 marlas, about 40% by area [derived: 276 of 688 marlas], stayed under acquisition. The note does not say which part the plant occupies. That decides partial versus full relocation. | R339, R340 (RF L641-L644); R727, R728 (RF L1260-L1263) | Add to the 0D Note 5 row: "Land 34 kanals 8 marlas; 20 kanals 12 marlas released and in possession; 13 kanals 16 marlas (about 40% by area) under acquisition; plant footprint by parcel NOT FOUND." Add to Q2 or S2: "Does the relocation cover the whole Panipat plant or only the facilities on the 13 kanals 16 marlas still under acquisition?" Two readings: partial move (bull), full move (bear); separating observation: management's answer or a costed plan in a later Note 5. Reword RV L609 "so the company must plan a move" to "and the company is evaluating relocation (FILED)". |
| F6 | MISSING | A4 | Rs 2.71 Cr went into subsidiaries in H1 FY27 (R302), but the review never states it. M8 (RV L547) cites R302 as the line where Chile's infusion "will be visible", which reads as if no money has moved. Recipient NOT FOUND. Note 4 says Chile's infusion "is under process" (R805), and Chile is not in the consolidated entity list (R797-R801). | R302 (RF L554); R185, R186 (RF L391); R805; R797-R801 (RF L1338-L1341) | Add to Step 5A or M8: "H1 FY27 SA cash flow shows Rs 2.71 Cr invested in subsidiaries (R302; carrying value 13.32 to 16.03 Cr, R186, R185). Recipient NOT FOUND." Add question S19: "Which subsidiary received the Rs 2.71 Cr H1 FY27 investment, and did any of it go to Tinna Rubber Chile SpA? If yes, why is Chile outside the consolidated entity list?" Bull: all to Oman or Saudi. Bear: part to Chile, unconsolidated. |

No stand-alone CONTRADICTION finding. F1 also conflicts with RV L261 and is tagged FACTUAL as its primary type.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**. Finding types: 1 FACTUAL (F1), 5 MISSING (F2 to F6), 0 CONTRADICTION.

Exact gap: F1, the unsupported PCMB cause at RV L432. F2 to F4, the three surviving bear counters to graft (the debt fall is funded by the WC release; SA H1 revenue +23.04% sits below the 25% pace; the H1 material cost gain is a Q1 FY26 base effect). F5, the Panipat land split (R339-R340, R727-R728). F6, the Rs 2.71 Cr H1 FY27 investment in subsidiaries (R302) against Chile's "under process" infusion.

A2 and A3 need not re-run. Coverage and arithmetic pass. Every fix is a text edit inside the review, using A1 rows already in the ledger. The A4 protocol verdict (PROCEED WITH FLAGS) and cash classification (INDETERMINATE-WITH-DIRECTION) are not challenged. F2 strengthens the indeterminate reading; it does not change it.

---

## STYLE NOTES (logged; no loop)

- S1. Rounding-edge residuals: CO Q2 FY26 revenue QoQ -8.25% (-8.255%); CO Q2 op EBITDA QoQ -13.13% (-13.135%); SA PAT QoQ -20.15% (-20.144%, RV L583); SA CCC 55.7 days (55.61, sum of rounded parts). Prefer computing from lakh cells, then rounding once.
- S2. "Raw material cost" (RV L620, L626) is gross material cost: it includes traded-goods purchases and inventory change. Relabel it "material and traded-goods cost".
- S3. ND is used for figures the filing lets you derive. SA ICR H1 FY26 = 6.80x [(4,146.63 - 497.85) / 536.82] (RV L339). The CO Q1 FY26, H2 FY26 and H1 FY26 cost splits are marked ND in 1D (RV L181). ND means "not disclosed". Use "not computed" for these.
- S4. The release's "9%" debt fall has an arithmetic path: (121 - 111) / 111 = 9.0%, a decline divided by the closing base. Add it to A4-01 and S18 as the likely drafting basis. A4-01's conclusion stands: no correct filed basis gives 9%.
- S5. R-A3-14 sharpens. CO Q2 FY26 implied weighted shares (171.3 lakh) sit below CO H1 FY26 (171.5 lakh). A share issue during H1 cannot produce that, unless treasury shares rose in Q2. SA shows the expected order (176.0 above 173.9). The filed CO EPS stays the number of record.
- S6. Five release claim units have no A1 type slot (PF L65 / L82, L67, L90, L127, L139). Consider a CLAIM type in A1 and A2 for unsourced characterisations. The "record H1 profitability" headline is untested. A one-line tie-out: H1 FY27 is the highest of the three halves in the filing (SA PAT 36.17 vs H2 FY26 29.92 [53.24 - 23.32] vs H1 FY26 23.32 Cr). Earlier halves are NOT FOUND.
- S7. Step 5A (RV L346) says "Assumed band: ND", then cites "the top 1.30x band". Name the band's source.
- S8. Excess provisions written back: 46.83 lakh in H1 FY27 (R266) against 1.70 lakh in H1 FY26. This is a non-cash gain of Rs 0.47 Cr, about 1% of SA H1 PBT. Where it sits in the P&L is NOT FOUND. Optional mention in 4C.
- S9. The "drag" half of "drag to contributor" (RV L365) rests on the Q2 FY26 CO-SA PAT gap (-0.57 Cr). That gap mixes associate and JV (-0.12 Cr) with eliminations. The filing gives no Q2 FY26 subsidiary PAT (Other Matter covers the current periods only, RF L1365-L1368). Say so in one clause.
- S10. Three forward-map rows are undated (RV L650-L652). They are labelled honestly. Keep them, and keep the six dated rows first.

---

```yaml
stage: A5-adversary
company: "TINNARUBR"
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
  - {claim: "YoY growth is real and Q2 beats the Vision 2029 over-25% pace (RV L225, L602)", counter: "SA H1 FY27 revenue grew 23.04% (30,041.74 / 24,416.12), below the 25% pace; CO H1 25.21% sits at the floor; Q2 rides a soft Q2 FY26 base (-8.21% QoQ); Q2 FY27 is only 3.48% SA / 5.80% CO above the H2 FY26 quarterly average", source_line: "R015, R016 (RF L243); R350, R351 (RF L848); PR R058 (PF L134)", type: MISSING}
  - {claim: "Net debt fell about Rs 10 Cr while capex was spent, funded by CFO (RV L349, L608)", counter: "The WC release paid for the whole fall: SA pre-debt cash Rs 9.32 Cr vs WC release Rs 18.64 Cr, so without it the half needed about Rs 9.32 Cr of new debt (CO Rs 5.09 Cr); the release is a Sep vs Mar comparison", source_line: "R294, R310, R326, R324, R320, R322, R314, R316, R318, R250, R274 (RF L535-L567); CO R681, R697, R713, R711, R707, R709, R633, R663", type: MISSING}
  - {claim: "Model drift to manufacturing: lower trading share lines up with the gross margin gain (A4-06 RV L567; RV L620, L627)", counter: "The H1 gain of 415 bps comes from the Q1 FY26 outlier (55.22%); Q2 YoY material cost fell 55 bps while trading share fell 533 bps; H2 FY26 paired 7.91% trading with 53.09% material cost; own material consumed rose 38.38% to 43.01% of Q2 revenue; no filed link", source_line: "R030, R032, R036, R038, R042, R044, R012, R014 (RF L243-L250); 1D RV L172, L176", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): RV L432 Step 6D PCMB cell 'group margin fell in Q2 on higher PCMB share' has no support (no Q2 PCMB split; PR R042-R043 give H1 only) and conflicts with A4's own Step 3C attribution (RV L261)"
  missing:
    - "F2 (A4): graft Claim 2 counter, debt fall funded wholly by the Rs 18.64 Cr WC release; ex-WC SA deficit Rs 9.32 Cr, CO Rs 5.09 Cr (RV L349, L608, L589, L730)"
    - "F3 (A4): graft Claim 1 counter, SA H1 revenue +23.04% below the 25% pace, soft Q2 FY26 base (RV L225, L602)"
    - "F4 (A4): graft Claim 3 counter, H1 material cost gain is a Q1 FY26 base effect; no trading-to-margin link in the filed series (RV L567, L620, L627)"
    - "F5 (A4): Panipat land split absent: 34K8M total, 20K12M released and in possession, 13K16M (about 40%) under acquisition (R339-R340, R727-R728; RF L641-L644); add to 0D Note 5 row and Q2/S2; reword RV L609 'must plan a move'"
    - "F6 (A4): Rs 2.71 Cr H1 FY27 investment in subsidiaries (R302; carrying value 13.32 to 16.03 Cr, R185-R186) not stated; recipient NOT FOUND while Chile infusion is 'under process' (R805) and Chile is outside the consolidated list (R797-R801); add fact and question S19"
  contradiction: []
  style:
    - "S1 rounding-edge residuals (-8.25 vs -8.255, -13.13 vs -13.135, -20.15 vs -20.144, CCC 55.7 vs 55.61)"
    - "S2 relabel 'raw material cost' as material and traded-goods cost"
    - "S3 ND used for derivable figures (SA ICR H1 FY26 6.80x; CO 1D splits)"
    - "S4 release 9% debt fall matches (121-111)/111; add as likely drafting basis"
    - "S5 CO Q2 FY26 weighted shares 171.3 below H1 171.5 sharpens R-A3-14"
    - "S6 five release claim units lack an A1 type slot; 'record H1' headline untested"
    - "S7 name the source of the 1.30x Pillar 2 band (RV L346)"
    - "S8 excess provisions written back Rs 0.47 Cr non-cash gain (R266)"
    - "S9 the 'drag' side of drag-to-contributor rests on a mixed CO-SA gap"
    - "S10 three undated forward-map rows, honestly labelled"
loop_back_to: "A4"
gap: "F1 FACTUAL: RV L432 PCMB cause unsupported by any document and in conflict with RV L261. F2-F4 MISSING: graft three surviving bear counters (debt fall funded wholly by the Rs 18.64 Cr WC release; SA H1 revenue +23.04% below the 25% pace; H1 material cost gain is a Q1 FY26 base effect). F5 MISSING: Panipat land split 20K12M of 34K8M released (R339-R340, R727-R728). F6 MISSING: Rs 2.71 Cr H1 FY27 investment in subsidiaries (R302) vs Chile infusion 'under process'. Graft text for each is in the audit, section 4."
style_notes:
  - "S1 rounding-edge residuals (-8.25 vs -8.255, -13.13 vs -13.135, -20.15 vs -20.144, CCC 55.7 vs 55.61)"
  - "S2 relabel 'raw material cost' as material and traded-goods cost"
  - "S3 ND used for derivable figures (SA ICR H1 FY26 6.80x; CO 1D splits)"
  - "S4 release 9% debt fall matches (121-111)/111; add as likely drafting basis"
  - "S5 CO Q2 FY26 weighted shares 171.3 below H1 171.5 sharpens R-A3-14"
  - "S6 five release claim units lack an A1 type slot; 'record H1' headline untested"
  - "S7 name the source of the 1.30x Pillar 2 band (RV L346)"
  - "S8 excess provisions written back Rs 0.47 Cr non-cash gain (R266)"
  - "S9 the 'drag' side of drag-to-contributor rests on a mixed CO-SA gap"
  - "S10 three undated forward-map rows, honestly labelled"
analyst_note: "Coverage and arithmetic are clean. Fresh counts match A2 on every category (results 927 IDs, release 138), and every derived metric in A4 recomputes within rounding; four residuals of 0.01 pp or 0.1 day are logged as style. The review fails on substance, not numbers. Three positive claims lose force on A4's own filed rows. The Rs 10 Cr debt fall is entirely the Rs 18.64 Cr working capital release: excluding it, the half consumed Rs 9.32 Cr standalone. The H1 gross margin gain is a Q1 FY26 base effect, and the quarter series shows no link from trading share to margin. Standalone H1 revenue grew 23.04%, below the 25% pace A4 says Q2 beats. One cell (Step 6D PCMB) states a cause no document supports. Two filed facts are absent: about 60% of the Panipat land was released, which frames partial versus full relocation, and Rs 2.71 Cr already went into subsidiaries while the Chile infusion is 'under process'. No purchase of an earning business exists, so the price to PAT probe does not apply. All six fixes are A4 text edits from rows already in the ledger; A2 and A3 need not re-run."
audit_path: "runs/tinnarubr-q2fy27/work/audit_tinnarubr_q2fy27.md"
token_estimate: "about 290k total (about 250k input incl. the full review, both fulltexts, both structured files and both ledgers, with context re-reads; about 40k reasoning and output)"
```
