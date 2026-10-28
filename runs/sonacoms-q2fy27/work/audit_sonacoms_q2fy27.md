# A5 ADVERSARY AUDIT: SONACOMS Q2 FY27

Agent: A5 adversary | model claude-opus-5-5 | run date 2026-10-28
Under audit: work/review_sonacoms_q2fy27.md (A4, 1,128 lines)
Inputs read: four A1 fulltexts, four A1 structured files (targeted reads and greps), four A2 ledgers. No source PDF and nothing under inputs/ was opened.
Anchor key: "review L###" = A4 review line; "res / deck / PR / call L###" = A1 fulltext line; "ledger_<doc> L###" = A2 ledger line.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading (review line) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | review L983 | 10 prose lines, L984-L993 (Document Review Protocol not loaded, review L6, so the 10-20 line rule applies) | PRESENT |
| 2. Sector intelligence | review L995 | 8 bullets: demand, US EV, input costs, rare earths, Europe, railway, credit, non-disclosures | PRESENT |
| 3. Business-model intelligence | review L1005 | 7 bullets: product set, unit economics, three model drifts, order book, concentration | PRESENT |
| 4. Competition intelligence | review L1014 | 6 bullets: share wins, weak points, DENSO, peers ND, risk | PRESENT |
| 5. Forward map | review L1022 | Make-or-break line plus 12 dated rows, each with a bull and a bear fork (L1025-L1038) | PRESENT |

Gate result: PASS. All five parts are present and carry real content.

---

## 1. COVERAGE AUDIT

Method: an independent grep pass over each A1 FULLTEXT, then a diff against the A2 ledger counts, then a check that every ledger row is cited in A4 or marked reviewed.

| Doc | Category | A2 count | A5 fresh count (fulltext) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Numbered notes (SA 7 + C 6) | 13 | 13 (res L302, 305, 307, 312, 315, 320, 321; L635, 638, 640, 645, 648, 653) | none | PASS |
| Results | Notes incl. 4a/4b | 15 | 15 (res L313-314, L646-647) | none | PASS |
| Results | Unnumbered footnotes | 3 | 3 (res L292, L625, L460) | none | PASS |
| Results | Line items | 249 | 249 (SA P&L L146-174 = 29; SA BS L185-223 = 39; SA CF L234-268 + L278-291 = 49; SA Note 3 L309-311 = 3; C P&L L470-505 = 36; C BS L516-556 = 41; C CF L567-599 + L609-624 = 49; C Note 3 L642-644 = 3) | none | PASS |
| Results | Line-item cells | 771 | 771 (169 + 78 + 98 + 17 + 211 + 82 + 98 + 18; SA Note 3 H1 FY26 total blank, res L311) | none | PASS |
| Results | Zero-standing | 47 cells / 19 lines | 47 / 19 (SA P&L 9, SA CF 4, SA N3 11, C P&L 9 incl. "0.00" at res L490, C CF 3, C N3 11) | none | PASS |
| Results | Agenda items | 1 | 1 (res L36-38) | none | PASS |
| Results | Auditor paragraphs | 9 | 9 (res L83, 90, 98, 113; L344, 353, 362, 379, 388) | none | PASS |
| Results | Annexure 1 entities | 17 | 17 (res L437-458) | none | PASS |
| Results | Signature blocks | 5 | 5 (res L58-61, L125-128, L323-327, L415-418, L655-659) | none | PASS |
| Results | Structured IDs | 1,098 | 1,098 referenced; spot check of R176, R250, R407, R618, R619, R675, R692, R696, R698, R732, R738, R750, R972 against res L171, 215, 390, 502, 503, 537, 546, 548, 549, 576, 579, 585, 418: all present and correct | none | PASS |
| Deck | Slides | 36 | 36 ([page 1]-[page 36]) | none | PASS |
| Deck | NUMBER units | 201 | 213 (12 fulltext units with no structured row, listed below) | none | FAIL |
| Deck | ENTITY units | 40 | 41 (slide 26 Phase 4 event row missing; Phase 3 has R225) | none | FAIL |
| Deck | Footnotes / qualifiers | 42 | 42 | none | PASS |
| Deck | Forward | 12 | 12 | none | PASS |
| Deck | Dates | 22 | 22 | none | PASS |
| PR | Pages | 4 | 4 | none | PASS |
| PR | NUMBER units | 52 | 52 (PR L22-182) | none | PASS |
| PR | ENTITY / FORWARD / DATE / QUALIFIER | 33 / 8 / 20 / 14 | 33 / 8 / 20 / 14 | none | PASS |
| Concall | Turns | 53 | 53 (T01-T53 contiguous over L1-L921, ledger_concall L47-L99; boundaries inferred) | none | PASS |
| Concall | Questions | 18 | 18 (call L393-395, L396, L433-434, L459-469, L470-477, L514-530, L531-539, L557, L599-609, L640-643, L645-659, L711-722, L723-726, L768-771, L801-805, L841-844, L856-857, L883-885) | none | PASS |
| Concall | Participants | 15 | 15 (call L015-025, L385, L456, L513, L598, L705) | none | PASS |
| Concall | Management numbers | 110 + M01-M09 | 110 + 9; my sweep found no further unit | none | PASS |
| All | Ledger rows cited in A4 or marked reviewed | 1,098 / 317 / 127 / 345 | A4 reconciliation table marks all rows reviewed, no orphans (review L28-L33) | none | PASS (see STYLE S9) |

### Fresh-pass units the deck structured file and the A2 ledger lack (FAIL, MISSING, loop to A2)

| # | Fulltext line | Unit | Note |
|---|---|---|---|
| 1 | deck L291 | "22%" | Slide 16 pie value. Absent from R109 and R110. Sum test: geography FY26 5+17+51+27 = 100; H1 FY27 10+14+25 = 49, so the L291 "51%" that R110 assigns to the product pie fits the H1 FY27 geography pie (49 + 51 = 100); R110's 20 values sum to 229, and 229 - 51 + 22 = 200. A1 mapping needs a re-check |
| 2 | deck L504-505 | "Became publicly listed"; "Acquisition of NOVELIC and Railway Business" | Slide 26 Phase 4 events (Phase 3 event has R225) |
| 3 | deck L506 | "12 plants" | Slide 26 Phase 4 |
| 4 | deck L507 | "34 products" | Slide 26 Phase 4 |
| 5 | deck L510 | "57,136 H1FY27 (Ann.)" | Revenue series end point |
| 6 | deck L512-513 | "FY22-H1FY27 Ann. Avg. EBITDA margin 25.1%" | R227 captured only the left-hand 25.3% on the same line |
| 7 | deck L515 | "FY22-H1FY27 Ann. Revenue CAGR 24.1%" | R228 captured only the left-hand 33.9% on the same line. A4 cites it (review L253) |
| 8 | deck L516 | "44,752" (FY26 by position) | A4 uses it as the FY28E-B CAGR end point (review L971) |
| 9 | deck L518 | "35,545" (FY25) | |
| 10 | deck L519 | "31,866" (FY24) | |
| 11 | deck L520 | "26,756" (FY23) | |
| 12 | deck L522 | "21,306" (FY22) | |
| 13 | deck L523 | "28,568 H1FY27" | |

Cause: the A2 deck count test compared structured NUMBER rows with themselves ("grep NUMBER rows = per-page sweep sum = A1 header", ledger_presentation L8). It never swept the fulltext. The concall ledger shows the right method (ledger_concall L13, L658-L671). A3 had already found these units, and A4 cites them from the fulltext (review L35). So the completeness spine broke at A2, not in A4's reading. A forward-estimate input (FY21-FY26 CAGR 23.4%, review L971) rests on a deck number that has no row ID.

---

## 2. ARITHMETIC AUDIT

All values are recomputed from raw Rs million cells (res) and converted x0.1 to Rs Cr. "OK" means equal within rounding (0.01 Cr or 0.01 pp on a Cr-rounded input).

| # | Metric | A4 value (review line) | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | C op EBITDA Q2 FY27 | 356.24 (L146) | 2,959.64 + 789.10 + 123.17 - 309.51 = 3,562.40 mn | res L481, L478, L477, L472 | OK |
| 2 | C op EBITDA Q2 FY26 / Q1 FY27 | 289.06 / 302.60 | 2,890.57 / 3,026.04 mn | same lines | OK |
| 3 | C op EBITDA H1 FY27 / H1 FY26 / FY26 | 658.84 / 491.60 / 1,106.85 | 6,588.44 / 4,916.05 / 11,068.54 mn | same lines | OK |
| 4 | Op margin, rev ops, Q2 FY27 / Q2 FY26 | 23.20% / 25.39% (L147) | 23.195% / 25.394% | res L470 | OK |
| 5 | Op margin ex-forex Q2 FY27 / Q2 FY26 | 22.51% / 24.93% (L149) | 3,456.61 / 15,358.40 = 22.506%; 2,838.31 / 11,382.93 = 24.935% | res L471 | OK |
| 6 | Op margin, deck basis Q2 FY27 / Q2 FY26 | 23.04% / 25.28% (L150) | 3,562.40 / 15,464.19 = 23.037%; 2,890.57 / 11,435.19 = 25.278% | res L470-471; deck L119, L390 | OK |
| 7 | Margin change YoY: rev ops / ex-forex / deck | -219 / -243 / -224 bps (L222-223, L254) | -219.9 / -242.9 / -224.1 bps | as above | OK |
| 8 | Reported EBITDA Q2 FY27 / FY26 | 387.19 / 1,152.84 (L151) | 3,871.91 / 11,528.38 mn | res L483 | OK |
| 9 | Core PBT (PBET - OI) Q2 FY27 / Q2 FY26 / Q1 FY27 | 265.01 / 212.28 / 215.24 (L152) | 2,650.13 / 2,122.75 / 2,152.46 mn | res L481, L472 | OK (Q1 215.25 on raw; rounding) |
| 10 | OI / PBT Q2 FY27 / H1 FY26 | 10.46% / 15.57% (L154) | 10.458% / 15.565% | res L472, L483 | OK |
| 11 | ETR Q2 FY27 / Q2 FY26 / H1 FY27 / FY26 | 24.66 / 25.09 / 25.22 / 25.24% (L155) | 24.657 / 25.089 / 25.219 / 25.240% | res L487, L483 | OK |
| 12 | PAT margin Q2 FY27 / Q2 FY26 | 14.52 / 14.98% (L156) | 14.519 / 14.976% | res L488 | OK |
| 13 | Materials incl. inventory change / rev ops Q2 FY27 / Q2 FY26 | 50.97 / 48.01% (L157) | 7,828.63 / 15,358.40 = 50.973%; 5,465.32 / 11,382.93 = 48.013% | res L474-475 | OK |
| 14 | Employee / other expenses to rev ops, Q2 FY27 vs Q2 FY26 | 8.50 vs 9.05%; 18.02 vs 18.00% (L158-159) | 8.504 vs 9.052%; 18.017 vs 17.9997% | res L476, L479 | OK |
| 15 | Cost bridge ties to ex-forex margin | +296 - 55 + 2 = 243 bps (L254) | 15,358.40 - 7,828.63 - 1,306.03 - 2,767.13 = 3,456.61 = ex-forex op EBITDA | res L470-479 | OK |
| 16 | SA op EBITDA Q2 FY27 / Q2 FY26 / Q1 FY27 | 314.40 / 277.52 / 270.28 (L189) | 3,143.97 / 2,775.13 / 2,702.81 mn | res L157, L154, L153, L148 | OK (277.51 on raw; rounding) |
| 17 | SA op margin Q2 FY27 / Q2 FY26 | 22.83 / 26.26% (L190) | 22.831 / 26.255% | res L146 | OK |
| 18 | SA vs C PAT gap Q2 FY27 / Q1 FY27 / H1 FY27 / FY26 | -12.97 / +18.90 / +3.83 / +2.66% (L203-207) | -25.61 / 197.38; 41.60 / 220.11; 15.98 / 417.48; 17.23 / 646.42 | res L164, L488 | OK |
| 19 | Ex-dividend gap Q1 / H1 | about -11.1 / -12.1% | (160.65 - 178.51) / 160.65 = -11.12%; (358.02 - 401.50) / 358.02 = -12.14% | res L320 | OK |
| 20 | Subsidiary-layer op EBITDA Q2 FY27 / Q2 FY26 and share | 41.84 / 11.54; 11.7% / 4.0% (L202-204) | 356.24 - 314.40; 289.06 - 277.52; 11.74% / 3.99% | rows 1, 16 | OK |
| 21 | YoY: rev / op EBITDA / ex-forex / reported PBT / PAT / owners PAT / EPS | +34.92 / 23.24 / 21.78 / 30.06 / 30.81 / 29.30 / 28.78% (L219-233) | +34.92 / 23.24 / 21.78 / 30.06 / 30.81 / 29.31 / 28.78% | res L470, L483, L488, L496, L505 | OK |
| 22 | Finance cost YoY, C / SA | +138.76 / +116.27% (L225, L243) | +138.56 / +116.36% on raw mn (123.17 / 51.63; 90.44 / 41.80) | res L477, L153 | ROUNDING ARTEFACT (S1) |
| 23 | Core PBT ex-forex YoY | +22.88% (L229) | 254.43 / 207.05 | rows 9, 5 | OK |
| 24 | QoQ revenue Q2 FY27 | +18.03% (L271) | 15,358.40 / 13,012.01 | res L470 | OK |
| 25 | Q1 FY26 (tagged NOTION MEMORY) | 853.91 / 23.72% / 130.23 (L266) | H1 FY26 - Q2 FY26: 853.91 / 23.72% / 130.22 | res L470, L481 | OK (derivable from the filing, S6) |
| 26 | Q3 FY26 derived revenue | 1,199.76 (L268) | 4,449.46 - 1,992.20 - 1,257.50 | res L470; Q4 FY26 input is NOTION MEMORY | Derivation OK; Q4 input outside extract, not audited |
| 27 | H1 average run-rate and Q2 excess | 1,418.52; +8.27%; core 240.13; +10.4% (L276) | 2,837.04 / 2; 1,535.84 / 1,418.52; 480.26 / 2; 265.01 / 240.13 | res L470, L481 | OK |
| 28 | PAT bridge PBT change and components | +68.40 = 99.13 - 37.29 + 5.35 - 7.29 - 7.16 + 14.00 + 1.67 (L285-292) | Sum 68.41; 2,959.64 - 2,275.59 = 684.05 mn; revenue effect 397.55 x 24.935% = 99.13; margin effect 1,535.84 x -2.428 pp = -37.29 | res L470-483 | OK |
| 29 | Bridge tax lines and PAT | -17.16; +1.27; +52.52 (L293-295) | 68.40 x 25.089% = 17.16; 0.432 pp x 295.96 = 1.28; 2,229.87 - 1,704.66 = 525.21 mn | res L487-488 | OK |
| 30 | Recurring share; OI-revert run-rate | 47.39 = 69.3%; 212.44, +24.6% (L298-299) | 47.39 / 68.40 = 69.28%; 222.99 - 14.00 x 0.7534 = 212.44; / 170.47 = +24.62% | rows 28-29 | OK |
| 31 | CFO / PAT H1 FY27 / H1 FY26 | 1.48x / 1.16x (L310) | 5,935.27 / 4,015.01 = 1.478; 3,397.54 / 2,921.73 = 1.163 | res L591, L488 | OK |
| 32 | CFO / PAT ex-payables | 0.78x / 1.00x (L311) | (5,935.27 - 2,787.85) / 4,015.01 = 0.784; (3,397.54 - 464.50) / 2,921.73 = 1.004 | res L585 | OK |
| 33 | SA CFO / PAT; ex-payables; ex-dividend | 1.31x; 0.72x; 1.53x (L328) | 5,481.81 / 4,174.84 = 1.313; 3,025.22 / 4,174.84 = 0.725; 5,481.81 / 3,580.21 = 1.531 | res L259, L253, L164, L320 | OK (A4 0.72x is right; 0.7246) |
| 34 | Capex, FCF, CFO growth | 148.50; 445.03; +74.70% (L309-313) | 1,485.04; 5,935.27 - 1,485.04 = 4,450.23; 5,935.27 / 3,397.54 = 1.747 | res L591-592 | OK |
| 35 | Net WC movement H1 FY27 / H1 FY26 | (11.08) / (94.09) (L314) | 6,881.46 - 6,992.28 = -110.82; 4,030.24 - 4,971.11 = -940.87 | res L580, L589 | OK |
| 36 | Receivable / inventory / payable days; CCC | 94.4 to 76.2; 107.2 to 100.1; 80.5 to 93.3; 121.1 to 83.0 (L315-318) | 94.40 to 76.25; 107.16 to 100.07; 80.46 to 93.30; 121.1 to 83.0 | res L529, L527, L548-549, L474-475 | OK |
| 37 | Gross borrowings; narrow net cash; deck net cash; ND/EBITDA | 242.68 to 469.40; (605.58) to (854.52); (1,026.3) to (1,496.1); 1.17x (L322-325) | 2,426.85 to 4,694.05 mn; 8,482.57 - 2,426.85; 13,239.11 - 4,694.05; 19,655 - 4,694.05 = 14,960.95 mn; / LTM 1,274.09 = 1.174 | res L540, L546, L528, L530-531; deck L446, L448, L479 | OK |
| 38 | Subsidiary CWIP; subsidiary IAUD | 77.63; 299.66 (L320-321) | 2,082.80 - 1,306.54; 3,058.11 - 61.51 | res L518, L187, L521, L190 | OK |
| 39 | Warranty and slow-moving provision multiples | 5.7x; 6.7x (L947) | 124.91 / 21.81 = 5.73; 80.18 / 12.03 = 6.67 | res L576, L573 | OK |
| 40 | Shares; H1 dilution; MD PSP | 62.41 Cr; +0.37%; about 0.03% (L82-83, L99) | 6,241.28 / 10 = 624.128 mn; 22.81 / 6,218.47 = 0.367%; 0.170747 / 624.128 = 0.027% | res L502, L171, L314 | OK |
| 41 | TTM rev ops / owners PAT / EPS / PE | 5,294.30 / 746.56 / 11.96 / 73.5x (L967) | 4,449.46 - 1,992.20 + 2,837.04; 640.17 - 297.48 + 403.87; / 62.41; 879 / 11.96 | res L470, L496 | OK |
| 42 | FY27E-A / FY27E-B | 5,908.72, 850.67, 13.63, 64.5x; 5,674.08, 807.74, 12.94, 67.9x (L968-969) | identical | res L470, L496 | OK |
| 43 | FY28E-A / FY28E-B | 7,385.90, 1,074.34, 17.21, 51.1x; 7,001.81, 996.75, 15.97, 55.0x (L970-971) | 7,385.90 x 14.546% = 1,074.36; 7,001.81 x 14.236% = 996.75 | res L496, L470 | OK |
| 44 | FY21-FY26 revenue CAGR | 23.4% (L971) | (44,752 / 15,663)^(1/5) = 23.36%; deck 5-year CAGR 23% (deck L583, L605) cross-checks | deck L516, L528 | OK; L516 input has no structured row (coverage FAIL) |
| 45 | Order-book arithmetic | 16.3 bn = 45%; 60% start FY28-FY29; 4.8 bn unitemised; 6.6 vs 6.9 bn; 1.6x consumption (L445, L493) | 16.3 / 36 = 45.3%; 18.7 / 31.2 = 59.9%; 36 - 31.2; 3.3 + 1.6 + 2.0; 25 / 15.464 = 1.62 | deck L201-203, L221, L234, L248 | OK |
| 46 | BEV share of total Q2 revenue | about 39.2% (L819) | 6,061 / 15,464 = 39.19% | deck L125, L119 | OK |
| 47 | Auditor signing lead | about 33 min (L941) | 14:00 - 13:27:12 = 32.8 min (SA 33.5 min) | res L49, L128, L418 | OK |
| 48 | Q&A time share | 36.1 min = 57% (L549) | 01:02:26 - 00:26:23 = 36.05 min / 63.63 = 56.7% | call L001 | OK |
| 49 | Credibility ratio; specificity | 8.3%; 0.42 (L645, L794) | 0.25 / 3; 8 / 19 | review tables | OK |
| 50 | Price ratios | 2.29x; 4.75x (L462) | 879 / 384; 879 / 185 | NOTION MEMORY inputs | OK |

Result: no mismatch above rounding. Row 22 and a few cells differ by 0.01-0.20 pp because A4 computed on Cr-rounded inputs. These are logged as STYLE S1. They change no conclusion.

---

## 3. ADVERSARIAL READ

### Read 1. DENSO stake sale: MANDATORY ACQUISITION-ECONOMICS PROBE

Positive claims in A4: "Undisclosed material positive: DENSO close dates" (review L896); "Catalyst status: DENSO ON TRACK" (review L923); Forward Map bull fork "Consolidated at 51%; gain booked in standalone; cash about Rs 800-900 Cr" (review L1029); Strategic Premium input "DENSO JVs" (review L446).

Purchase economics:
- Consideration: DENSO buys 49% at an Enterprise Value of Rs 17,500 mn = Rs 1,750 Cr (res L319). On an EV basis 49% = Rs 857.5 Cr. The equity bridge (the carve-out's own debt or cash) is ND.
- Target earnings: the carve-out's EBITDA and PAT are NOT FOUND. Note 5 (res L315-319) gives none. The call gave none for a second quarter (review L942). So the multiple "Rs 1,750 Cr / target PAT" = NOT FOUND.
- Sales multiple on the nearest filed proxy: E2W/E3W segment = 14% of H1 FY27 revenue (deck L297) x Rs 2,856.8 Cr (deck L138) = about Rs 400 Cr in H1, about Rs 800 Cr annualised. EV / annualised segment sales = about 2.2x. Q2 run-rate cross-check [ASR]: traction plus suspension motors Rs 1,400 Cr annualised (call L260), less suspension at about 7% of Q2 revenue (call L241; about Rs 433 Cr annualised) = about Rs 967 Cr. EV / run-rate sales = about 1.8x.
- Comparator: Sona itself at Rs 879 = (Rs 55,012 Cr market cap - Rs 1,496.1 Cr net cash) / TTM rev ops Rs 5,294.30 Cr = about 10.1x EV / sales (review L71, L325, L967).
- Quality markers: the unit grew almost 50% QoQ (call L060), beyond management's own internal expectations (call L058-059). It took Rs 16.3 bn of Q2 order additions (deck L201-203) from existing Indian 2W OEM customer(s) (deck L196-200; PR L128-135). Management calls one product line lower-margin (CFO, call L622-623, answering the analyst premise at call L607-608). Debt, cash and customer tenure of the carve-out: ND. Royalties run both ways, terms ND (res L319). The EV was fixed at the 22-Jul-2026 signing (res L315), three weeks into the quarter of the surge. The slump sale into the subsidiary is at fair market value per an independent valuer (res L318).

Strongest bear counter: Sona sells 49% of its fastest-growing engine at about one-fifth of its own sales multiple, on a price set before the Q2 surge and before Rs 16.3 bn of new 2W motor and controller orders. The counter-reading: the unit earns thin margins, so 1.8-2.2x sales is fair, the retained business's margin rises, and NCI leakage is small. The extract cannot separate the two readings because target earnings are not disclosed. Separating observation: the carve-out's EBITDA and PAT (the valuer's FMV report, or the first post-close NCI line).

Cash in the bull fork: 49% x EV = Rs 857.5 Cr before tax. Proceeds are taxable (call L660-661). The Rs 900 Cr upper end is the analyst's figure (call L649), which management did not confirm. So the bull fork's upper end exceeds the EV-implied gross unless the carve-out holds net cash (ND).

Railway acquisition (Note 2, res L305): consideration Rs 1,642.63 Cr. Target PAT is NOT FOUND (railway P&L silent two calls, review L384). The only sales proxy is NOTION MEMORY (Rs 973 Cr in 10 months, review L430), about 1.4x annualised sales. The ROCE definition excludes railway capital on deck p7 (deck L150) and includes it on p23 (deck L485), and railway EBIT is annualised (deck L492). A4 already carries this bear reading (review L403, L443, L492, L499). No new graft beyond stating the multiple as NOT FOUND.

Does the counter survive? YES for DENSO. The review never states the price as a multiple, never names the two readings, and does not cap the bull-fork cash. Finding M2, MISSING, loop to A4.

Graft text for A4 (Step 5A near review L741-742, Step 6.5/7 table at review L446, Brief section 3 drift 2 at review L1009, Forward Map row at review L1029):
"DENSO pays EV Rs 1,750 Cr for 49% of the EV-motor carve-out (res L319): Rs 857.5 Cr before tax, and proceeds are taxable [ASR, call L660-661]. Carve-out EBITDA and PAT: NOT FOUND, so EV/earnings cannot be stated. On the nearest filed proxy (E2W/E3W 14% of H1 FY27 revenue, deck L297, L138; about Rs 800 Cr annualised) the EV is about 2.2x sales, or about 1.8x on the Q2 run-rate [ASR, call L241, L260]. Sona trades near 10x EV/TTM sales at Rs 879. Reading A: a thin-margin unit (call L622-623), a fair price, a higher retained margin, small NCI leakage. Reading B: 49% of the fastest-growing engine (about +50% QoQ, call L060; Rs 16.3 bn of Q2 adds, deck L201-203) sold at about one-fifth of the group multiple, priced at the 22-Jul signing (res L315). Separating observation: carve-out EBITDA and PAT. Bull-fork cash caps at Rs 857.5 Cr before tax unless the carve-out holds net cash (ND)."

### Read 2. "Sona's BEV revenue still grew 129% because its customer base is broader [MGMT-FILED]" (review L997)

Strongest bear counter, from the same extracts:
- Tier: the 129% is filed (deck L125, L392; PR L70). The cause is not. The deck and PR state no cause. The "more diversified and less dependent on any single customer or single geography" claim is the CEO's spoken line (call L135-140). The tag should be [ASR].
- Substance: the CEO named India E2W/E3W demand as "the biggest reason" (call L077-080). The two 2W motor and controller additions (Rs 12.5 bn + Rs 3.8 bn = Rs 16.3 bn, 45% of Rs 36 bn) both come from existing Indian 2W OEM customer(s) (deck L196-203; PR L128-135). The Rs 12.5 bn alone is 35% of the quarter's additions, against the CEO's "not anchored ... on just one very, very large order" (call L216-218). Sona serves 3 of India's top 10 e-2W OEMs (deck L628-630). The fastest-growing product, suspension motors at about 7% of revenue, sits on one customer and one model (call L239-241, L403-408, L417).

Does the counter survive? YES. The extract supports "growth concentrated in India E2W and one China EV customer" at least as strongly as "a broader base". Finding F1, FACTUAL (a management claim from the call is presented as a filed fact), loop to A4.

Graft text for A4 (replace review L997):
"BEV revenue grew 129% YoY [MGMT-FILED, deck L125]. Management attributes it to a broader customer base [ASR, call L135-140], but it named India E2W/E3W demand as the biggest reason [ASR, call L077-080]. The two 2W motor and controller additions (Rs 16.3 bn, 45% of Q2 additions) come from existing Indian 2W OEM customer(s) [MGMT-FILED, deck L196-203; PR L128-135]. Suspension motors (about 7% of revenue) sit on one customer and one model [ASR, call L241, L417]."

### Read 3. FY27E-A / FY28E-A path and "Notion FY29 base EPS Rs 16.0 is already below FY28E-A EPS Rs 17.21" (review L968-L970, L977)

Strongest bear counter: management did not forecast Q2's traction-motor demand (call L058-059). The unit that delivered it moves into a 51:49 vehicle from end-Dec 2026 or Jan 2027 (res L318-319; call L439-440), so 49% of its PAT leaves owners' PAT from the close quarter. The Q2 owners' PAT margin carried into FY28E-A (14.546%) includes other income at 10.46% of PBT (res L472, L483) and the smallest NCI loss in the series, Rs 0.42 Cr (res L497).

Against the counter: H2 FY27E-A revenue (3,071.68) is +25.0% on H2 FY26 (4,449.46 - 1,992.20 = 2,457.26, res L470), below H1's +42.4%. So the revenue path is not stretched. A4 already states that both readings exclude NCI leakage and DENSO effects (review L960, L975) and shows the ex-other-income run-rate (review L299).

Does the counter survive? PARTLY, and A4 already carries it. No graft needed. STYLE S11: repeat the gross-of-NCI caveat beside the EPS comparison at review L977.

---

## 4. OTHER FINDINGS FROM THE AUDIT

- F2, FACTUAL, loop to A4. Review L1016 says "CY25 was the first dip in both share series". Starter-motor share also fell from CY21 4.6% to CY22 4.1% (deck L703), then recovered to 4.4% by CY24. Fix: "CY25 is the first year both series fell together; starter-motor share also fell in CY22 (4.6% to 4.1%)". The gear series statement is correct (deck L700).
- C1, CONTRADICTION, loop to A4. Railway diversification is rated AMBER / UNKNOWN as tripwire 8 (review L410) and UNKNOWN in the concall update (review L871). The same review rates growth trigger #1 ON TRACK (review L430, L858). Filed and spoken evidence: the non-auto share fell from 31% to 29% (deck L305). The Rs 9 bn railway book executes within 12 months (deck L257, L267), about 0.77 years of revenue on A4's own arithmetic (review L430). No railway order is itemised among Q2 wins (deck L190-L238; PR L120-L151), although the CEO lists railway products among wins without a value (call L097). The railway P&L is undisclosed for two calls (call L809-810). Growth depends on launching on time (call L824-825). Suspension motors already equal railway brake systems for H1 (call L242-243, ledger_concall M05). Fix: align 6D and 8A to AMBER / UNVERIFIED with this evidence, or state why a fired trigger is ON TRACK while its tripwire is UNKNOWN.

---

## VERDICT

INCOMPLETE.

| ID | Type | Failing agent | Exact gap |
|---|---|---|---|
| M1 | MISSING | A2 | The deck ledger lacks 12 numeric units and 1 Phase-4 event row present in the deck fulltext (deck L291, L504-507, L510, L512-513, L515, L516, L518, L519, L520, L522, L523). A2's deck count test was circular (ledger_presentation L8). Add MISSING_FROM_STRUCTURED rows by the concall method. A3 already reviewed these units (review L35), so its pass can be limited to confirming the new IDs |
| M2 | MISSING | A4 | No acquisition-economics multiple for the DENSO 49% stake sale. Graft Read 1 text (EV Rs 1,750 Cr; about 2.2x / 1.8x sales vs about 10.1x group; target earnings NOT FOUND; two readings; separating observation; bull-fork cash cap Rs 857.5 Cr before tax) |
| F1 | FACTUAL | A4 | Review L997 tags the spoken diversification claim as [MGMT-FILED] and omits the concentration counter. Graft Read 2 text |
| F2 | FACTUAL | A4 | Review L1016 "first dip in both share series" is wrong for starter motors (deck L703) |
| C1 | CONTRADICTION | A4 | Railway: ON TRACK (review L430, L858) vs AMBER / UNKNOWN (review L410, L871) |

Loop order: A2 first (row insertion), then A4 (cite the new row IDs and apply M2, F1, F2 and C1). Arithmetic is clean, and the deliverable gate passes.

---

## STYLE NOTES (logged, no loop)

- S1. Growth rates computed on Cr-rounded inputs drift 0.01-0.20 pp from the raw values: C finance cost +138.76% vs +138.56% (res L477); SA finance cost +116.27% vs +116.36% (res L153); C other income +82.60% vs +82.58% (res L472); SA other income +80.28% vs +80.25% (res L148). Cells: H1 FY26 ex-forex margin 24.56% vs 24.57%; H1 FY27 materials 50.50% vs 50.51%; H1 FY27 employee cost 9.15% vs 9.14%. Recompute on raw million values.
- S2. Review L987 "the subsidiaries tripled their profit": the measure is consolidated minus standalone op EBITDA, which includes eliminations. It rose 3.6x (11.54 to 41.84). Say so.
- S3. Review L984 "Both are records [FILED]": the record status comes from the press release (PR L68), so the tag is [MGMT-FILED].
- S4. Review L996 "E2W/E3W rose from 10% to 14% of revenue [MGMT-FILED, this quarter]": the comparison is FY26 vs H1 FY27 (deck L297), not this quarter.
- S5. Review L1001 "about one year of work" conflicts with A4's own 0.77 years (review L430). Use one figure.
- S6. Review L266 tags the Q1 FY26 revenue, margin and core PBT as [NOTION MEMORY]. They are derivable from the filing (H1 FY26 less Q2 FY26, res L470, L481). The Q3 and Q4 FY26 inputs stay outside the extract and were not audited.
- S7. Review L485 sets the H1 unrealised forex add-back (res L579 is an H1 cash-flow line) against "realised forex in Q2", which mixes periods.
- S8. Review L696 and ledger_concall L86 call Q15's asker ambiguous. Call L808 "Hi, Brahmoor" points to Ramod Kumar.
- S9. A2-flagged rows have no per-row disposition in A4: R882 NAME_VARIANT "Precisions" (res L437); R537 LOW_LEGIBILITY, C OCI remeasurement H1 FY27 7.05 (res L489; Q2 7.08 + Q1 (0.04) = 7.04, which ties within rounding); deck R044, R058, R317 FOOTNOTE_UNRESOLVED. All are immaterial. Record them as "reviewed, no finding".
- S10. The deck and PR ledgers end without the standard closing YAML block (ledger_presentation L444; ledger_pressrelease L146). The PR footer "Page | 1" (PR L101) has no row, while R125 and R127 capture the other two footers.
- S11. Review L977: repeat the gross-of-NCI-leakage caveat (review L960) beside the FY28E-A EPS 17.21 vs Notion FY29 EPS 16.0 comparison.
- S12. Review L313 "Ties deck FCFO 4,456 mn within rounding": the 5.8 mn gap is capex net of PPE sale proceeds (1,485.04 - 6.27 = 1,478.77 mn, deck L448 shows 1,479). Say "ties on a net-capex basis".

---

Loop 0 block, superseded by the RE-AUDIT, LOOP 1 block at the end of this file:

```yaml
stage: A5-adversary
company: "SONACOMS"
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
  missing_from_ledger:
    - "deck L291 '22%' slide 16 pie value, absent from R109/R110 (sum test suggests L291 '51%' belongs to the H1 FY27 geography pie)"
    - "deck L504-505 slide 26 Phase 4 events 'Became publicly listed' and 'Acquisition of NOVELIC and Railway Business'"
    - "deck L506 '12 plants' (slide 26 Phase 4)"
    - "deck L507 '34 products' (slide 26 Phase 4)"
    - "deck L510 '57,136 H1FY27 (Ann.)'"
    - "deck L512-513 'FY22-H1FY27 Ann. Avg. EBITDA margin 25.1%'"
    - "deck L515 'FY22-H1FY27 Ann. Revenue CAGR 24.1%'"
    - "deck L516 '44,752' (FY26 by position; used by A4 FY28E-B, review L971)"
    - "deck L518 '35,545' (FY25)"
    - "deck L519 '31,866' (FY24)"
    - "deck L520 '26,756' (FY23)"
    - "deck L522 '21,306' (FY22)"
    - "deck L523 '28,568 H1FY27'"
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "DENSO stake sale framed as positive: dated close, bull-fork cash Rs 800-900 Cr, strategic premium (review L896, L923, L1029, L446)"
    counter: "EV Rs 1,750 Cr for 49% = Rs 857.5 Cr before tax, proceeds taxable; target EBITDA/PAT NOT FOUND; about 2.2x annualised E2W/E3W H1 sales (about 1.8x Q2 run-rate, ASR) vs about 10.1x group EV/TTM sales; priced at 22-Jul signing before the Q2 traction surge and Rs 16.3 bn of 2W motor/controller adds; two readings (thin-margin fair price vs value transfer) unseparated; bull-fork upper end exceeds EV-implied gross"
    source_line: "res L315, L318-319; deck L138, L201-203, L297; call L058-060, L241, L260, L622-623, L649, L660-661; review L71, L325, L967"
    type: MISSING
  - claim: "Sona's BEV revenue still grew 129% because its customer base is broader [MGMT-FILED] (review L997)"
    counter: "Cause is the CEO's spoken claim (call L135-140), not filed; CEO named India E2W/E3W as the biggest reason (call L077-080); Rs 16.3 bn (45%) of Q2 adds from existing Indian 2W OEM customer(s), Rs 12.5 bn alone 35% (deck L196-203, PR L128-135); 3 of India's top 10 e-2W OEMs (deck L628-630); suspension motors about 7% of revenue on one customer and one model (call L241, L417)"
    source_line: "call L077-080, L135-140, L216-218, L239-241, L417; deck L125, L196-203, L628-630; PR L70, L128-135"
    type: FACTUAL
  - claim: "FY28E-A EPS Rs 17.21 already above Notion FY29 base EPS Rs 16.0 (review L977)"
    counter: "Q2 surge unforecast (call L058-059) in a unit moving into a 51:49 vehicle (res L318-319; call L439-440); Q2 owners PAT margin carries OI at 10.46% of PBT and the smallest NCI loss in the series (res L472, L483, L497). Already carried at review L960, L975, L299; H2 FY27E-A revenue only +25.0% on H2 FY26, so the revenue path is not stretched"
    source_line: "res L318-319, L470, L472, L483, L497; call L058-059, L439-440; review L960, L975, L977"
    type: STYLE
findings_by_type:
  factual:
    - "F1 (A4): review L997 tags the spoken diversification cause of BEV +129% as [MGMT-FILED] and omits the concentration counter; re-tag [ASR, call L135-140] and graft Read 2 text"
    - "F2 (A4): review L1016 'CY25 was the first dip in both share series' is wrong for starter motors, which fell CY21 4.6% to CY22 4.1% (deck L703)"
  missing:
    - "M1 (A2): deck ledger lacks 12 numeric units and 1 Phase-4 event row present in the deck fulltext (deck L291, L504-507, L510, L512-513, L515-523); A2 deck count test was circular (ledger_presentation L8)"
    - "M2 (A4): mandatory acquisition-economics multiple for the DENSO 49% stake sale absent; graft EV Rs 1,750 Cr, about 2.2x/1.8x sales vs about 10.1x group, target earnings NOT FOUND, two readings, separating observation, bull-fork cash cap Rs 857.5 Cr before tax"
  contradiction:
    - "C1 (A4): railway rated ON TRACK as growth trigger #1 (review L430, L858) but AMBER/UNKNOWN as tripwire 8 (review L410, L871); evidence: non-auto share 31% to 29% (deck L305), book about 0.77 yr, no itemised railway add, P&L silent two calls (call L809-810)"
  style:
    - "S1 growth rates on Cr-rounded inputs drift 0.01-0.20 pp (finance cost +138.76% vs +138.56% raw, res L477)"
    - "S2 review L987 'subsidiaries tripled their profit' is C-minus-SA op EBITDA incl. eliminations, 3.6x"
    - "S3 review L984 'records' tag should be [MGMT-FILED] (PR L68)"
    - "S4 review L996 E2W/E3W 10% to 14% is FY26 vs H1 FY27, not this quarter (deck L297)"
    - "S5 review L1001 'about one year of work' vs 0.77 yr at review L430"
    - "S6 review L266 Q1 FY26 values derivable from filing; Q3/Q4 FY26 inputs outside extract, not audited"
    - "S7 review L485 mixes H1 unrealised forex (res L579) with Q2 realised forex"
    - "S8 Q15 asker resolvable to Ramod Kumar (call L808)"
    - "S9 A2-flagged rows R882, R537, deck R044/R058/R317 lack per-row 'reviewed, no finding'"
    - "S10 deck and PR ledgers lack closing YAML block; PR footer L101 uncaptured"
    - "S11 repeat gross-of-NCI caveat beside review L977 EPS comparison"
    - "S12 review L313 FCF ties deck on net-capex basis (deck L448)"
loop_back_to: "A2"
gap: "A2: add MISSING_FROM_STRUCTURED rows for deck L291 22%, L504-505 Phase 4 events, L506 12 plants, L507 34 products, L510 57,136, L512-513 25.1%, L515 24.1%, L516 44,752, L518 35,545, L519 31,866, L520 26,756, L522 21,306, L523 28,568 (MISSING; A3 already reviewed these units per review L35, so A3 confirms IDs only). Then A4: cite the new IDs and fix M2 (MISSING, DENSO acquisition-economics multiple and two readings), F1 (FACTUAL, review L997 tier and concentration counter), F2 (FACTUAL, review L1016 starter-motor share history), C1 (CONTRADICTION, railway ON TRACK vs AMBER/UNKNOWN)."
style_notes:
  - "S1 recompute growth rates on raw Rs mn (finance cost +138.56%, SA +116.36%, OI +82.58%, SA OI +80.25%)"
  - "S2 say 'subsidiary-layer op EBITDA rose 3.6x (incl. eliminations)' at review L987"
  - "S3 tag 'records' [MGMT-FILED, PR L68] at review L984"
  - "S4 E2W/E3W share comparison is FY26 vs H1 FY27 (review L996)"
  - "S5 align railway book cover: 0.77 yr (review L430, L1001)"
  - "S6 tag Q1 FY26 as [FILED, derived] (review L266)"
  - "S7 align periods in Q5 forex question (review L485)"
  - "S8 Q15 asker is Ramod Kumar (call L808)"
  - "S9 record 'reviewed, no finding' for R882, R537, deck R044/R058/R317"
  - "S10 A2 deck and PR ledgers need closing YAML blocks"
  - "S11 restate NCI caveat at review L977"
  - "S12 FCF tie is on net-capex basis (review L313)"
analyst_note: "Arithmetic is clean: every derived metric recomputes from res L470-L624 within rounding, including the PAT bridge, cash ratios, working-capital days and the forward-estimate tables. INCOMPLETE rests on two gaps. First, the deck ledger is circular: A2 counted structured rows instead of sweeping the fulltext, so 12 slide 16 and slide 26 numbers have no row ID, and A4's FY28E-B CAGR rests on two of them. A3 already reviewed these units (review L35), so the fix is row insertion plus ID confirmation, not a full A3 re-run. Second, the review never prices the DENSO stake sale. EV Rs 1,750 Cr is about 2.2x the E2W/E3W segment's annualised H1 sales (about 1.8x on the ASR Q2 run-rate), against about 10x for Sona at Rs 879. Target earnings are NOT FOUND, so a thin-margin fair price and a value transfer cannot be told apart; the carve-out's EBITDA and PAT separate them. The Step 3 Q3/Q4 FY26 inputs come from Notion memory and were not audited. The other A4 fixes are small: BEV cause re-tag, starter-motor history, railway status alignment."
```

---

## RE-AUDIT, LOOP 1

Run date 2026-10-28. Correction loop 1 of 1.
Under audit: the patched review work/review_sonacoms_q2fy27.md (now 1,194 lines; change log at review L9-L21; loop1_changes at review L1185-L1192) and the patched deck ledger work/ledger_presentation_sonacoms_q2fy27.md (revision 2; count test at ledger_presentation L6-L20; MISSING_FROM_STRUCTURED rows M01-M15 at L453-L467). Every other input is unchanged. I opened no source PDF and nothing under inputs/.
Line numbers in this section refer to the PATCHED review. The loop-0 section above cites the pre-patch review.

### L1-A. Closure of loop-0 items

| Item | Type | Status | Evidence |
|---|---|---|---|
| M1 | MISSING (A2) | CLOSED | My 13 units map one-to-one by line to A2 rows M01-M14 (ledger_presentation L453-L466): L291 = M01; L504 = M02 and L505 = M03 (A2 split my one Phase 4 event row into two); L506 = M04; L507 = M05; L510 = M06; L512-513 = M07; L515 = M08; L516 = M09; L518 = M10; L519 = M11; L520 = M12; L522 = M13; L523 = M14. M15 adds the slide 8 and 19 photo captions (deck L156, L378). The count test now sweeps fulltext tokens, not structured rows (ledger_presentation L6-L13). A4 lists every M row by ID (review L45, L49) and cites them where they are used (review L270, L431, L454, L1016, L1066). A4 tied M09 to the filing (44,494.60 + 256.88 = 44,751.48 mn, res L470-471) and moved FY28E-B off the unlabelled FY21 bar (R239) onto the labelled deck "5-year Revenue CAGR 23%" (R242, deck L583-587); see review L1016 and L1025 |
| M2 | MISSING (A4) | CLOSED | New subsection "DENSO 49% stake-sale economics" (review L473-L499). It covers the EV basis, Rs 857.5 Cr before tax, taxability [ASR], the equity bridge as ND, carve-out earnings NOT FOUND, EV/proxy sales 2.19x and 1.81x against Sona at 10.1x, the price date, the valuer, both readings, the separating observation and the cash cap. A4 also adds a point I did not raise: Note 5 says DENSO "will buy" 49% (res L319) but does not say from whom, so the cash may stay in the vehicle. That reading is valid. The graft is carried into review L117, L452, L467, L515, L531 (Q2), L565, L671, L772-L773, L790-L791, L940, L946, L955, L970, L973, L993 (flag 6), L1045, L1063 and L1083 |
| F1 | FACTUAL (A4) | CLOSED | Review L1051 tags the 129% [MGMT-FILED, deck L125] and the cause [ASR, call L135-140], and adds the concentration counter (call L077-080; deck L196-203; PR L128-135; call L241, L417). A matching 7A row is added at review L869 |
| F2 | FACTUAL (A4) | CLOSED | Review L1070: "CY25 is the first year both share series fell together ... Starter-motor share also fell once before, from 4.6% in CY21 to 4.1% in CY22". This matches deck L700 and L703. The risk line at review L1074 now says "another joint dip" |
| C1 | CONTRADICTION (A4) | CLOSED | Railway is AMBER / UNVERIFIED in every place: tripwire 8 (review L429), growth trigger #1 (L451), concall 8A (L908), 8B (L921), Section C (L973), flag 14 (L1001), YAML flag (L1175) and brief part 2 (L1055). One evidence set R carries both sides (review L433). A grep for "ON TRACK (quantum" returns no hit |

The loop-0 style notes are applied: S1 (except the residue in R1 below), S2 (review L217, L226, L1041), S3 (L1038), S4 (L1050), S5 (L1055), S6 (L283, L290), S7 (L534), S8 (L745), S9 (L51), S11 (L1031) and S12 (L332). S10 remains open on the press-release ledger, which is A2 housekeeping (review L19).

### L1-B. Rewrite integrity check (full-file diff against the loop-0 review)

I compared the patched file with the loop-0 text section by section.
- **Headings:** every section heading is present in the same order. The only new headings are the change log (review L9) and the DENSO subsection (review L473).
- **Results tables:** every Step 0, 1, 2, 3, 4 and 5 table matches the loop-0 values, except the cells patched under S1, S2, S6 and S12. Other changed cells: the ex-forex H1 FY26 / H1 FY27 / FY26 row is 489.39 / 639.10 / 1,081.17 on raw values, and the H1 FY26 ex-forex margin is 24.57%.
- **Concall tables:** the Role 5 tables match loop 0. Exceptions: the patched railway and DENSO cells, the Q15 asker, two new pattern sentences (review L755-L756), the new 7A row (L869), and the extended 5A, 5B, 8D, 8E and 8F cells.
- **Questions for Management:** all 24 rows are present (review L530-L553). Only Q2 (M2), Q5 (S7) and Q19 (C1, "why it matters" cell) changed. The top-3 list and the channel line are unchanged.
- **Section C:** all 17 loop-0 flags are kept. Two are added: DENSO pricing (#6) and railway (#14), so the list now runs to 19.
- **YAML:** 24 questions, 15 monitorables and 20 flags (18 kept plus 2 added). The A3 findings list is unchanged.
- **Brief:** all five parts are present. The narrative is 10 lines (review L1038-L1047). The forward map keeps its 12 rows, and only the DENSO row changed.

Changes outside the patched points:
- D1. Narrative sentence dropped. Loop-0 review L991 read "How it will be accounted for is still unknown." The rewrite replaced it with the DENSO price sentences (review L1045). The fact survives in the brief's forward map bear fork (review L1083), in Q1 of Step 8.5 (L530), in Section C (L970) and in flag 5 (L992). STYLE R2.
- D2. Bullet relocated. The loop-0 brief part 3 bullet on suspension-motor concentration moved into part 2 (review L1051), and part 3 now ends with a "Scale" bullet (L1066). No content is lost. STYLE R3.
- No number, status or verdict changed outside the patched points. The protocol verdict stays PROCEED WITH FLAGS (review L977).

### L1-C. Audit 0 (deliverable gate), re-run

| Brief part | Heading (review line) | Status |
|---|---|---|
| 1. Summary narrative | L1037; 10 lines L1038-L1047 | PRESENT |
| 2. Sector intelligence | L1049; 8 bullets | PRESENT |
| 3. Business-model intelligence | L1059; 7 bullets | PRESENT |
| 4. Competition intelligence | L1068; 6 bullets | PRESENT |
| 5. Forward map | L1076; 12 dated rows with bull and bear forks (L1081-L1092) | PRESENT |

Gate: PASS.

### L1-D. Audit 1 (coverage), re-run

| Doc | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | All categories (notes, line items, cells, zero-standing, agenda, auditor paras, entities, signatures, 1,098 IDs) | unchanged | unchanged (loop-0 table above) | none | PASS |
| Deck | Slides | 36 | 36 | none | PASS |
| Deck | NUMBER units | 201 + 12 (M01, M04-M14) = 213 | 213 | none | PASS |
| Deck | ENTITY units | 40 + 3 (M02, M03, M15) = 43 | 41 on my convention (Phase 4 events as one row; photo captions not counted). A2 holds more rows than I count, not fewer | none | PASS |
| Deck | Footnotes / forward / dates | 42 / 12 / 22 | 42 / 12 / 22 | none | PASS |
| PR | All categories (127 IDs) | unchanged | unchanged | none | PASS |
| Concall | Turns / questions / participants / mgmt numbers + M01-M09 | 53 / 18 / 15 / 110 + 9 | 53 / 18 / 15 / 110 + 9 | none | PASS |
| All | Ledger rows cited in A4 or marked reviewed | 1,098 / 332 / 127 / 345 | Review L44-L47 marks all rows reviewed; every deck M row is listed by ID at L49; flagged rows are dispositioned at L51 | none | PASS |

missing_from_ledger: none. orphan_rows: none.

### L1-E. Audit 2 (arithmetic) on new and changed figures

| # | Metric | A4 value (review line) | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | FY28E-B revenue | 6,979.12 (L1025) | 5,674.08 x 1.23 = 6,979.12 | review L1023; deck L583-587 | OK |
| 2 | FY28E-B owners PAT | 993.52 (L1025) | 6,979.12 x 14.2356% (403.87 / 2,837.04) = 993.52 | res L496, L470 | OK |
| 3 | FY28E-B EPS / PE | 15.92 / 55.2x (L1025, L1031) | 993.52 / 62.41 = 15.92; 879 / 15.92 = 55.2 | res L502 | OK |
| 4 | M09 tie | 44,751.48 mn (L49, L1016) | 44,494.60 + 256.88 = 44,751.48; deck 44,752 within 1 mn | res L470-471; deck L516 | OK |
| 5 | M14 tie | 28,567.89 mn (L49) | 28,370.41 + 197.48 = 28,567.89; deck 28,568 | res L470-471; deck L523 | OK |
| 6 | Forex share of revenue | about 0.6-0.7% (L1016) | 256.88 / 44,494.60 = 0.58%; 197.48 / 28,370.41 = 0.70% | res L470-471 | OK |
| 7 | Positional FY21-FY26 CAGR | 23.36% (L1016) | (44,752 / 15,663)^(1/5) = 1.2336 | deck L516, L528 | OK |
| 8 | H2 FY27E-A vs H2 FY26 | +25.0% on 2,457.26 (L1022) | 3,071.68 / (4,449.46 - 1,992.20) = 1.250 | res L470 | OK |
| 9 | DENSO 49% at EV | Rs 857.5 Cr (L478) | 1,750 x 0.49 | res L319 | OK |
| 10 | Proxy segment sales | 399.95 H1; 799.9 annualised (L484) | 14% x 28,568 mn = 3,999.52 mn | deck L297, L138 | OK |
| 11 | EV / proxy sales; EV / run-rate | 2.19x; 1.81x (L485-L486) | 1,750 / 799.9 = 2.188; 7% x 1,546.42 x 4 = 433.0; 1,400 - 433 = 967; 1,750 / 967 = 1.810 | call L241, L260 | OK |
| 12 | Sona EV / TTM sales | 10.1x (L487) | (55,012 - 1,496.1) / 5,294.30 = 10.11 | review L88; deck L446; res L470 | OK |
| 13 | Raw-basis growth rates (S1) | +138.56 / +116.36 / +82.58 / +80.25% (L242, L260, L244, L262) | 123.17 / 51.63; 90.44 / 41.80; 309.51 / 169.52; 287.03 / 159.24 | res L477, L153, L472, L148 | OK |
| 14 | Ex-forex H1 FY26 / H1 FY27 / FY26 and H1 FY26 margin | 489.39 / 639.10 / 1,081.17; 24.57% (L165-L166) | 4,893.89 / 6,390.96 / 10,811.66 mn; 4,893.89 / 19,922.01 = 24.565% | res L470-481 | OK |
| 15 | Subsidiary layer multiple | 3.6x (L226, L1041) | 41.84 / 11.54 = 3.63 | rows 1, 16 of loop 0 | OK |
| 16 | Q1 FY26 derived | 853.91 / 23.72% / 130.22 (L283) | 11,382.93 subtracted from 19,922.01; (4,916.05 - 2,890.57) / 8,539.08; 3,424.99 - 2,122.75 | res L470, L481, L472 | OK |
| 17 | Residue on rounded inputs | owners PAT +29.30%; core PBT ex-forex +22.88%; CFO +74.70% (L249, L246, L328) | +29.31%; +22.89%; +74.69% on raw mn | res L496, L481, L472, L471, L591 | ROUNDING (0.01 pp, STYLE R1) |

All loop-0 arithmetic rows stand unchanged. There is no mismatch above rounding.

### L1-F. Audit 3 (adversarial read), re-run on the patched review

1. **"Revenue +34.92% YoY ... like-for-like on railway"; "Core grew, so the headline is real" (review L236, L272).** Bear counter: part of the growth could be passed-through input prices rather than volume (call L861-863). The extract gives no price and volume split.
   - The counter does not survive. Materials rose 296 bps as a share of revenue (res L474-475), so prices lagged costs; pass-through did not lift revenue ahead of cost.
   - Railway is a full quarter in both periods (res L305).
   - The "headline is real" claim rests on core PBT growth of +24.84% against reported +30.06%. A4 already decomposes that gap (review L272, L317-L318).
2. **"Notion FY29 base EPS Rs 16.0 is below FY28E-A EPS Rs 17.21" (review L1031).** The gross-of-NCI and other-income caveat now sits in the same sentence. FY28E-B is lower after the rebase. The counter is already carried, so no graft is needed.
3. **DENSO "positive for visibility only, not for value" (review L946); bull fork capped at Rs 857.5 Cr before tax (L1083). This is the mandatory acquisition-economics probe, re-tested.**
   - The multiple, the NOT FOUND target earnings, both readings, the separating observation and the cash cap are all in the review (L473-L497).
   - The primary-versus-secondary route point is supported by res L319, which does not say from whom DENSO buys.
   - The railway deal's multiple is stated as NOT FOUND (L499).
   - The probe passes, and no further graft is needed.

surviving_bear_counters: none open.

### L1-G. Verdict, loop 1

COMPLETE. All five loop-0 items (M1, M2, F1, F2, C1) are closed. The re-run finds no FACTUAL, MISSING or CONTRADICTION item. The deliverable gate passes, coverage has no orphan or missing row, and the arithmetic is clean. Only STYLE notes remain, and they never loop.

### L1-H. Style notes, loop 1 (logged, no re-run)

- R1. Three growth rates still use Cr-rounded inputs, although review L36 says growth is on raw values. Owners PAT is +29.30% (raw +29.31%, res L496). Core PBT ex-forex is +22.88% (raw +22.89%). CFO is +74.70% (raw +74.69%, res L591).
- R2. Restore "How it will be accounted for is still unknown." to the summary narrative at review L1045. The rewrite dropped it. The fact survives at review L1083, L530, L970 and L992.
- R3. The suspension-motor concentration bullet moved from brief part 3 to part 2 (review L1051). No content is lost.
- R4. Review L1045 says "DENSO pays about 2.2 times sales". The 2.2x is on a proxy segment (E2W/E3W, deck L297), and the 10x uses a screener market cap [SECONDARY] (review L88). Say "proxy" and tag [MGMT-FILED, SECONDARY, my arithmetic].
- R5. A2's note on M01 (ledger_presentation L453) says the 22% "belongs to the H1 FY27 geography pie (sum test)". The sum test says the opposite:
  - The H1 FY27 geography pie (10 + 14 + 25 = 49) needs the L291 "51%" to reach 100.
  - R110's product values sum to 229, and 229 - 51 + 22 = 200, so the 22% fits the product pie.
  - No review fact rests on this note. The review keeps the India share UNKNOWN (review L431, L454), and the pie labels are unrecoverable either way.
  - Fix the note. The operator may escalate this item; see the analyst note.
- R6. ledger_presentation L23 still lists slides 8 and 19 as having no rows; L469 corrects it. The slide 25 caption (deck L500) has no row, while the slide 8 and 19 captions do (M15). This is a convention note only.
- R7. Loop-0 S10 is carried forward. The press-release ledger still has no closing YAML block, and the PR L101 footer has no row. This is A2 housekeeping.

```yaml
stage: A5-adversary
company: "SONACOMS"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
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
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "R1 three growth rates still on Cr-rounded inputs: owners PAT +29.30% (raw +29.31%), core PBT ex-forex +22.88% (raw +22.89%), CFO +74.70% (raw +74.69%); review L36 claims raw basis"
    - "R2 narrative sentence 'How it will be accounted for is still unknown.' dropped in the rewrite (loop-0 L991, now review L1045); fact survives at review L1083, L530, L970, L992"
    - "R3 suspension-motor concentration bullet relocated from brief part 3 to part 2 (review L1051); no content lost"
    - "R4 review L1045 '2.2 times sales' is on a proxy segment (deck L297) and the 10x uses a SECONDARY market cap (review L88); say 'proxy' and fix the tag"
    - "R5 A2 M01 note (ledger_presentation L453) inverts the sum test: H1 FY27 geography 10+14+25 needs the L291 51%; the 22% fits the product pie (229 - 51 + 22 = 200); no review fact rests on it (review L431, L454)"
    - "R6 ledger_presentation L23 stale on slides 8 and 19 (L469 corrects it); slide 25 caption deck L500 unrowed while M15 rows slides 8 and 19"
    - "R7 loop-0 S10 still open: press-release ledger lacks closing YAML block; PR L101 footer unrowed (A2 housekeeping)"
loop_back_to: ""
gap: ""
style_notes:
  - "R1 recompute owners PAT, core PBT ex-forex and CFO growth on raw Rs mn"
  - "R2 restore the DENSO accounting-route sentence to the summary narrative (review L1045)"
  - "R3 suspension concentration now sits in brief part 2 (review L1051)"
  - "R4 label the DENSO 2.2x as proxy-segment sales and tag the market cap SECONDARY (review L1045)"
  - "R5 correct A2 M01 note: 22% fits the product pie, the L291 51% fits the H1 FY27 geography pie"
  - "R6 refresh ledger_presentation L23; decide the photo-caption convention for slide 25 (deck L500)"
  - "R7 add the press-release ledger closing YAML block and the PR L101 footer row"
analyst_note: "Loop 1 closes all five loop-0 items. M1: A2 revision 2 rows M01-M14 map by line to my 13 units (M02 and M03 split the Phase 4 events; M15 adds two photo captions), and the count test now sweeps the fulltext. A4 cites every M row and moved FY28E-B off the unlabelled FY21 bar to the labelled deck 23% CAGR; I recomputed 6,979.12 / 993.52 / EPS 15.92 / 55.2x. M2: the DENSO probe now sits in the review with the multiple, NOT FOUND carve-out earnings, both readings, the separating observation and the Rs 857.5 Cr pre-tax cap; A4 adds that res L319 does not say whether DENSO buys from Sona or subscribes, which is valid. F1, F2 and C1 are fixed throughout. The full-file rewrite changed nothing outside the patched points except one dropped narrative sentence and one relocated bullet; both facts survive elsewhere, so STYLE. A2's M01 note inverts my sum test; no review fact uses it and the pie labels are unrecoverable, so I logged it as STYLE; the operator may escalate it. Step 3's Q3 and Q4 FY26 inputs remain Notion memory and were not audited."
```
