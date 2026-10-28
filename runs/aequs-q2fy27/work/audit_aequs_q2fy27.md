# A5 ADVERSARY AUDIT: Aequs Limited (AEQUS), Q2 FY27 (quarter and half year ended 30-Sep-2026)
agent: A5 adversary (claude-opus-5-5) | audit date 28-Oct-2026 | prompt: prompts/quarterly-a5-adversary.md
inputs read: A4 review runs/aequs-q2fy27/work/review_aequs_q2fy27.md (1,035 lines); A1 fulltexts (results 870 lines, presentation 1,216, press release 245, concall 780); A1 structured (results R001-R1438, presentation R001-R566, press release R001-R171, concall R001-R302 + T01-T84); A2 ledgers (4).
not read: source PDFs, ASR transcript, anything under runs/aequs-q2fy27/inputs/, A3 notes, Notion snapshot, monitoring checklist. N-L and MC-L anchors in A4 are outside this audit's evidence and are checked only for internal arithmetic.
anchor key: R-L / P-L / PR-L / C-FT = A1 fulltext line numbers (same convention as A4). A4-L = line in the A4 review. R### = A1 structured row ID of the named document.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate, run first)

| Brief part | A4 heading and lines | Status | What is there |
|---|---|---|---|
| 1. Summary narrative | "## 1. SUMMARY NARRATIVE", A4-L868-870 | present | 17 sentences, about 200 words, anchored and tiered; within the 10-20 line band |
| 2. Sector intelligence | "## 2. SECTOR INTELLIGENCE", A4-L872-874 | present | Aerospace demand (order book, utilisation, programme length, Safran), CE qualification cycles, toy customer cycle, peer gap |
| 3. Business-model intelligence | "## 3. BUSINESS-MODEL INTELLIGENCE", A4-L876-878 | present | How aerospace earns, consumer fixed cost base, capital split, capex shift, parent vs subsidiary profit, named undisclosed items |
| 4. Competition intelligence | "## 4. COMPETITION INTELLIGENCE", A4-L880-882 | present | Belagavi ecosystem edge, peer margins, CE process shift risk, toy anchor loss, JV margins |
| 5. Forward map | "## 5. FORWARD MAP", A4-L884-897 | present | Make-or-break reading (A4-L886) plus 8 dated catalysts, each with a bull fork and a bear fork |

Gate result: PASS. All five parts exist and carry real content. Content defects inside the brief are logged below (F1, C1, S7). They do not void presence.

---

## 1. COVERAGE AUDIT

Method. I recounted each A2 category from the A1 fulltext (table lines, cells, note numbers, page markers, turn and question boundaries). I recounted the structured files by row type with my own grep. I then spot-tested high-materiality fulltext numbers against the structured rows to test whether A1 dropped anything. For the orphan test, A4 anchors by fulltext line and A3 finding ID, not by ledger row ID. Its preamble asserts every row reviewed (A4-L20). I accepted that blanket for boilerplate rows (addresses, phone numbers, IDs, certifications, divider slides, safe harbour). I tested every row that carries a financial, forward or customer fact against A4's line citations.

### 1A. Results (ledger_results)

| Category | A2 count | Fresh count (method) | Orphan rows | Status |
|---|---|---|---|---|
| notes | 21 | 21: standalone 1-10 (R-L234-282), consolidated 1-8 and 10-12 (R-L612-672), no 9 (R-L680) | none | PASS |
| line_items | 311 | 311 table lines with values: S-P&L 27 (R-L86-112), S-BS 38 (R-L125-162), S-CF 51 (R-L174-224), C-P&L 45 (R-L375-419), C-BS 48 (R-L432-479), C-CF 61 (R-L491-551), C-SEG 41 (R-L563-603) | none | PASS |
| line-item cells (R001-R1180) | 1,180 IDs | 1,176 printed values + 4 blank "Other equity" cells kept as rows (R145-R146, R635-R636) = 1,180 | none | PASS |
| zero_standing | 90 | 90 = 72 dashes + 18 zero decimals, recounted line by line | none | PASS |
| agenda_items | 1 | 1 (R-L40) | none | PASS |
| auditor_paras | 12 | 14 printed units (standalone para 1-4 + "Attention" para; consolidated para 1-6 + "Attention" + Reg 33(8) + "not modified"); all sit inside A2's 12 groupings | none | PASS (unit definition differs; no content outside the ledger) |
| entities (consolidation) | 22 | 22 in note 5 (R-L625-651) = 22 in Annexure I (R-L791-868) | none | PASS |
| signatures | 5 | 5 (letter R-L53-62, two LRRs R-L354-362 and R-L768-777, two note blocks R-L284-288 and R-L673-678) | none | PASS |
| footnotes | 3 | 3 (R-L113, R-L420, segment subtotal definition R-L570) | none | PASS |
| total IDs | 1,438 | 1,438 = NUMBER 1,236 + ENTITY 81 + FORWARD 9 + DATE 49 + QUALIFIER 63 | none | PASS |

Flagged rows traced into A4: TIE_FAIL (A4-L13, L137, L291); ENTITY_CHANGE (A4-L90, QfM 34-35); NOTE_NUMBERING_GAP (A4-L95); COMPARATIVES_UNREVIEWED (A4-L85, L101); OTHER_AUDITOR_UNNAMED / MGMT_FURNISHED_REPORT (A4-L101, QfM 32); STANDALONE_ONLY (A4-L87); RESTATED notes (A4-L91-92). SPELLING_VARIANT has no A4 mention. That is cosmetic, so I accept it under the blanket.

### 1B. Presentation (ledger_presentation)

| Category | A2 count | Fresh count (method) | Orphan rows | Status |
|---|---|---|---|---|
| slides | 33 | 33 ([page 1]-[page 33]) | none | PASS |
| slide_numbers | 451 | 451 ("\| NUMBER \|" rows) | R379, R418 | FAIL |
| line_items p16-19 | 210 | 210: p16 104 cells over 18 lines (P-L1114-1131), p17 52 (P-L1146-1182), p18 40 (P-L496-517), p19 14 (P-L1186-1213) | none | PASS |
| zero_standing | 2 | 2 (P-L509, P-L511) | none | PASS |
| forward | 25 | 25 | R473 | FAIL |
| dates | 20 | 20 | none | PASS |
| footnotes / qualifiers | 33 | 33 | none | PASS |
| entities | 37 | 37 | none | PASS |
| total IDs | 566 | 566 = 451 + 25 + 20 + 33 + 37 | 3 | FAIL |

Orphans (material, no citation and no treatment anywhere in A4; A4 cites no line in P-L540-880 and never uses "MoU"):
- R379 (NUMBER, P-L562) and R473 (FORWARD, P-L560-563). Text: "Entered into MoU with GoK for investment of ₹28,560 Mn". It sits in the latest timeline column of slide 21, beside the TN aero-engine MoU dated Feb 2026 (P-L220). A4 argues that the funding stack (warrants Rs 650 Cr, term loans "over Rs 800 Cr", a possible FY28 raise) "far exceeds FY27 capex of about Rs 320 Cr" (A4-L520). It also says the post-FY27 capex envelope is "Not said" (A4-L601), and QfM 19-22 (A4-L771-774) ask for uses. A Rs 2,856 Cr Karnataka investment MoU bears on both points. It may explain the funding stack, and it also signals a much larger capex and dilution exposure. MISSING, route A3, then A4.
- R418 (NUMBER, P-L775). Text: top 5 customer groups = 63% of H1 FY27 revenue. The competition brief (A4-L882) names consumer customer concentration as "the competitive risk to watch". It never states the group-level figure. MISSING, route A3, then A4.

Consequence: the A4 preamble claim "Orphans: none in any ledger. Unreviewed rows: none" (A4-L20) does not hold for the presentation.

### 1C. Press release (ledger_pressrelease)

| Category | A2 count | Fresh count (method) | Orphan rows | Status |
|---|---|---|---|---|
| pages | 5 | 5 | none | PASS |
| numbers | 112 | 112; key table PR-L81-92 = 3 header + 5 + 8 + 8 + 8 + 8 cells | none | PASS |
| dates | 8 | 8 | none | PASS |
| entities + entity-summary | 19 + 5 | 24 | none | PASS |
| qualifiers | 17 | 17 | none | PASS |
| forward | 10 | 10 | none | PASS |
| total IDs | 171 | 171 = 112 + 59 | none | PASS |

### 1D. Concall (ledger_concall)

| Category | A2 count | Fresh count (method) | Orphan rows | Status |
|---|---|---|---|---|
| turns | 84 | 84 (T01-T84) | none | PASS |
| questions | 29 | 29: Renu 2, Deepak 4, Akash 3, Gaurav 3, Nomura 1, Priyanka 4, Sanitya 4, Ashika 2, Suraj 2, Amitajit 4 | none | PASS. A4 4A has 28 rows. T15 ("please repeat", C-FT345) sits inside row 3's span C-FT344-346, and T70 sits inside row 25's span C-FT714-724 |
| participants | 16 | 16 (host side 6, analysts 10) | none | PASS |
| mgmt_numbers | 134 | 155 NUMBER rows = 134 mgmt + 17 analyst + 4 operator | none | PASS |
| forward | 51 | 51 | none | PASS |
| dates | 25 | 25 | none | PASS |
| entities | 42 | 42 | none | PASS |
| qualifiers | 29 | 29 | none | PASS |
| total IDs | 386 | 386 = 302 R + 84 T | none | PASS |

Flagged rows traced: FOOTNOTE_UNRESOLVED R292-R296 (A4-L14, L483); WITHDRAWN_DATE R198/R252/R256/R257 (A4-L461, L503); ENTITY_CHANGE R174/R176 (A4-L321, L486).

### 1E. Fulltext-to-structured spine test (did A1 drop anything)

Each of these was found as a structured row: presentation R379 (₹28,560 Mn), R418 (63%), R018 (3,589 workforce), R365-R378 (all 14 key-metric values), R405-R407 (consumer capacity); concall R091-R093 (50% upfront, 25% minimum, 18 months), R100 (12 to 18 months), R103/R105 (four to six times), R119-R120 (50%, FY30), R152/R155 (289 Cr, 800 Cr), R169 (250 acre); results R1321/R1324 ("proposed to be converted"). Results table cells tie at 1,176 printed values. Nothing the fulltext holds is missing from the structured files or the ledgers.

missing_from_ledger: none. missing_from_structured: none.

---

## 2. ARITHMETIC AUDIT

All values in Rs Cr unless marked Mn. Recomputed from the raw Rs Mn lines.

| Metric | A4 value (A4 line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| 1-C table, all 22 lines x 6 periods (Mn to Cr) | A4-L114-135 | every cell ties | R-L375-419 | PASS |
| 1-S standalone table, all lines | A4-L161-177 | every cell ties; op EBITDA Q2 FY27 (43.58 Mn) = (4.36) | R-L86-112 | PASS |
| Operating EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 | 13.86 / 14.76 / 28.51 (L146) | 138.55 / 147.64 / 285.07 Mn | R-L384 less R-L376 | PASS |
| Operating EBITDA H1 FY27 / H1 FY26 / FY26 | 28.62 / 55.72 / 89.07 | 286.19 / 557.20 / 890.71 Mn | same | PASS |
| Operating EBITDA margin Q2 FY27 / Q1 / Q2 FY26 | 3.39% / 3.73% / 10.12% (L147) | 3.387% / 3.733% / 10.124% | R-L375, R-L384, R-L376 | PASS |
| Reported EBITDA margin Q2 FY27 / Q2 FY26 / FY26 | 5.98% / 15.72% / 12.55% (L149) | 5.981% / 15.715% / 12.553% | R-L384 / R-L375 | PASS |
| Margin change, operating / reported | -673 bps / -974 bps (L202-203) | -673.7 / -973.4 bps | same | PASS (rounding; S2) |
| Core PBT (PBT less OI) Q2 FY27 / Q2 FY26 / FY26 | (51.46) / (27.70) / (136.92) (L150) | (514.64) / (276.98) / (1,369.15) Mn | R-L390, R-L376 | PASS |
| Effective tax rate Q2 FY27 / H1 FY27 / FY26 / H1 FY26 | -27.8% / -30.7% / -58.4% / -208.0% (L152) | -27.77% / -30.71% / -58.37% / -207.99% | R-L393 / R-L390 | PASS |
| PAT margin Q2 FY27 / H1 FY27 | -12.81% / -13.13% (L153) | -12.807% / -13.127% | R-L398 / R-L375 | PASS |
| S-vs-C gap Q2 FY27, % of standalone | (54.18), -3,025% (L187) | (541.83) Mn; -3,025.3% | R-L104, R-L398 | PASS |
| S-vs-C gap Q2 FY26 / Q1 FY27 / H1 FY27 / H1 FY26 / FY26 | (20.76) / (57.29) / (111.48) / (20.99) / (163.05) | (207.61) / (572.94) / (1,114.77) / (209.94) / (1,630.47) Mn | same | PASS |
| Subsidiaries + eliminations Q2 FY27 vs Q2 FY26 | (55.99) vs (22.86), 2.4x (L187-192) | (559.94) vs (228.57) Mn = gap less JV share; 2.45x | R-L388 | PASS |
| Revenue YoY / op EBITDA YoY / D&A YoY / finance YoY | +45.3% / -51.4% / +42.7% / -19.8% (L200-205) | +45.27% / -51.40% / +42.72% / -19.85% | R-L375, R-L384, R-L386, R-L385 | PASS |
| EBIT (op EBITDA less D&A) Q2 FY26 / Q2 FY27 | (4.09) / (32.67) (L206) | (40.96) / (326.77) Mn = (4.10) / (32.68) | R-L384, R-L376, R-L386 | PASS (rounding; S2) |
| Core-to-PAT bridge gap | -8.04 (L217) | -5.13 - 2.70 - 0.20 = -8.03 | R-L376, R-L393, R-L397 | PASS |
| Op EBITDA QoQ | -6.2% (L219) | -6.16% | R-L384, R-L376 | PASS |
| Consumer D&A / revenue | 47.6% (L218) | 274.25 / 576.68 = 47.56% | R-L576, R-L564 | PASS |
| Q1 FY26 derived (revenue, op margin, core PBT) | 255.57 / 10.65% / (6.11) (L227) | 2,555.69 Mn / 10.648% / (61.05) Mn | R-L375-390 H1 less Q2 | PASS |
| H2 FY26 derived | 693.28; 4.81%; (103.11) / (95.42) (L229) | 6,932.77 Mn; 4.811%; (1,031.12) / (954.17) Mn | FY26 less H1 FY26 | PASS |
| QoQ run-rates | +10.2% / +23.1% / +14.1% / +3.4% (L228-231) | +10.18% / +23.10% / +14.11% / +3.42% | same | PASS |
| H1 non-cash gains, share of H1 EBITDA | 12.41; 27.0% (L235) | 83.74 + 20.66 + 13.09 + 6.63 = 124.12 Mn; 27.01% | R-L500, R-L498, R-L510, R-L496, R-L384 | PASS |
| PAT bridge Q2 FY27 vs Q2 FY26 (Mn) | sum -317.99 (L256) | -146.52 - 139.29 + 51.00 - 51.32 - 2.85 - 26.97 - 2.04 = -317.99 = (523.92) less (205.93) | R-L384-398 | PASS (ties exactly) |
| Bridge split: revenue / margin effect (Mn) | +129.06 / -275.58 (L256) | +129.07 / -275.58 | R-L375, R-L384, R-L376 | PASS (rounding) |
| Bridge shares | -41 / +87 / +44 / -16 / +16 / +1 / +8 / +1 % (L245-253) | -40.6 / +86.7 / +43.8 / -16.0 / +16.1 / +0.9 / +8.5 / +0.6 % | derived | PASS |
| Recurring core share | -23.48, 74% (L259) | -14.65 - 13.93 + 5.10 = -23.48; 73.8% | derived | PASS |
| D&A QoQ, finance QoQ, aero finance QoQ | +2.6% / +9.3% / +53% (L261) | +2.62% / +9.27% / +53.2% | R-L386, R-L385, R-L571 | PASS |
| H1 tax drag vs 25.17% credit | about 45.1 (L262) | 247.68 + 806.56 x 0.2517 = 450.7 Mn | R-L393, R-L390 | PASS |
| CFO H1 FY27 / H1 FY26 | (80.83) / 47.90 (L270) | (808.31) / 479.02 Mn | R-L523 | PASS |
| FCF H1 FY27 / H1 FY26 | (245.66) / (152.04) (L273) | (2,456.64) / (1,520.35) Mn | R-L523, R-L524 | PASS |
| Working-capital change H1 FY27 / H1 FY26 | (102.76) / (18.99) (L274) | (1,027.64) / (189.89) Mn | R-L511-520 | PASS |
| Receivable / inventory / payable days, Sep-26 vs Mar-26 | 67.8 / 155.0 / 86.8 vs 78.5 / 168.3 / 95.6 (L275-277) | 67.76 / 154.95 / 86.79 vs 78.49 / 168.33 / 95.62 | R-L445-446, R-L469-470, R-L375 | PASS |
| CCC | 136.0 vs 151.2 (L278) | 135.92 vs 151.20 | derived | PASS |
| Absolute NWC | 599.28 vs 509.71, +17.6% (L279) | 5,992.82 vs 5,097.09 Mn; +17.57% | same lines | PASS |
| Gross borrowings | 561.19 vs 403.58 (L282) | 5,611.90 vs 4,035.78 Mn | R-L460 + R-L467 | PASS |
| Cash and bank | 199.85 vs 356.65 (L283) | 1,998.54 vs 3,566.52 Mn | R-L447 + R-L448 | PASS |
| Net debt ex leases / incl. leases | 361.34 / 636.57 vs 46.93 / 344.28 (L284-286) | 3,613.36 / 6,365.68 vs 469.26 / 3,442.79 Mn | R-L460-468, R-L447-448 | PASS |
| Net debt / equity ex / incl. leases | 0.26 / 0.46 vs 0.03 / 0.23 (L287-288) | 0.2596 / 0.4573 vs 0.0316 / 0.2318 | R-L459 | PASS |
| Operating cash before WC | +34.68 (L295) | (680.87) less (1,027.64) = 346.77 Mn | R-L521, R-L511-520 | PASS |
| Parent PBT ex intra-group; parent net cash | (12.54); 47.28 vs 117.42 (L179, L297) | (125.41) Mn; 472.83 vs 1,174.21 Mn | R-L174, R-L181, R-L185, R-L137-138, R-L147, R-L152 | PASS |
| FY27 run-rate revenue / EBITDA / PAT | 1,622.8 / 94.9 / (210.4) (L333-336) | 1,622.78 / 94.89 / (210.40) | R-L375, R-L384, R-L398 | PASS |
| Run-rate vs Notion base | -4.0% / -38% / 78% toward bear (L333-336) | -3.98% / -38.4% / 78.2% | Notion values as stated by A4 | PASS |
| Aero segment margin, harsh floor Q2 and Q1 | 22.29% / 19.27% / 20.59% (L348) | 22.289% / 19.268% / 20.592% | R-L563, R-L566, R-L376 | PASS |
| Aero growth Q2 / H1; seg margin H1 | +44.2% / +42.1%; 22.47% (L384) | +44.22% / +42.12%; 22.475% | R-L563, R-L566 | PASS |
| Consumer segment EBITDA | (40.14) (L359) | (401.41) Mn | R-L567 | PASS |
| Pledge cover, CMP vs warrant price | 10.7x / 6.6x / 3.3x; 8.4% below (L378) | 10.65x / 6.56x / 3.28x; 8.44% | share count N-L162 (not re-derivable here) | PASS (arithmetic only) |
| Warrant price | Rs 231.55 (A4 cites N-L16) | 6,500 Mn / 28,071,690 = Rs 231.55 | R-L272-273 | PASS (also derivable from the filing) |
| Dilution on conversion | 4.19% (L92) | 28.07 / 670.67 = 4.19% (pre-issue base); 4.02% of post-issue | R-L109, R-L272 | PASS |
| Step 6.5 annualised base | 1,636.3 / (209.6) (L405) | 1,636.32 / (209.56) | R-L375, R-L398 | PASS |
| Concall reconciliations (Mn) | +341.42 / +1,157.45 / +1,576.12 / +135.01 / +347.19 / +36.98 (L690-694) | same | R-L445-446, R-L460/467, R-L393, R-L386, R-L385 | PASS |
| JV share QoQ; consumer share of segment assets | -37.6%; 45% (L695, L698) | -37.59%; 45.4% | R-L388; R-L590-592 | PASS |
| QfM figures | 157 Mn fall; 104.2 / 46.7; 12.3% parent ETR; +190 Mn; -61% contract liabilities; Rs 161 Cr; about 767 Mn (A4-L755-791) | 157.18; 104.21 / 46.65; 12.32%; 190.27; -60.82%; 650 - 289 - 100 - 100 = 161; 766.64 | R-L564, R-L569, R-L103/100, R-L149, R-L475, C-FT761-765, R-L385/386/393/388 | PASS |
| Notion-check rows | -49.3% / -69.6%; 53.06 vs 53.37; -12.4% (L848-859) | -49.25% / -69.61%; 530.60 vs 533.72 Mn; -12.40% | R-L564, R-L567, R-L581 | PASS |
| FY27E segment revenue | aero 1,376.4; consumer 246.4 (L905-906) | 673.57 + 702.82 = 1,376.39; 131.05 + 115.34 = 246.39 | R-L563-564 | PASS |
| FY28E EBITDA build | 373.3 - 160.6 - 54.8 = 157.9 (L908) | 373.34 - 160.56 - 54.86 = 157.92 | R-L563/566, R-L567, R-L569, R-L586 | PASS (component should read (54.9); S1) |
| FY28E PAT / at Q2 D&A run-rate | (177.7) / (148.8) (L913) | (177.7) / (148.8) | derived | PASS |
| EPS FY27E / FY28E, basic and diluted | (3.14) / (3.01); (2.65) / (2.54) (L925-926) | 3.137 / 3.011; 2.649 / 2.543 | derived | PASS |
| Weighted shares implied; market cap | about 656 Mn; Rs 14,218 Cr, 0.3% above 14,169 (L920, L924) | 656.0 Mn; 14,218.2 Cr; +0.35% | R-L398, R-L419, R-L109 | PASS |
| Exceptional reconciliations | (76.95) = 39.02 + 37.93; S4 234.39 read as Mn (L87-97) | 76.95; standalone FY26 gain 187.45 = 234.39 - 39.02 - 7.92 confirms Mn | R-L389, R-L99, R-L248-261 | PASS |
| Concall counts | 22/31 = 71%; grades A2 B11 C11 D4 E1, 16/29 = 55%; specificity 16/32, 13/29; defensive 9 (L490, L578, L668-673) | same | A4 tables vs C-FT | PASS |

Result: zero mismatches above rounding across more than 100 recomputed figures. arithmetic_mismatches: none.

---

## 3. ADVERSARIAL READ (three most positive claims, plus the mandatory acquisition-economics probe)

### Claim 1. "Aerospace delivered" / growth trigger ON TRACK / spear fact 1 NOT FIRED (A4-L384, L393, L1032)
Strongest bear counter from the extract:
- Aerospace revenue rose 292.52 Mn QoQ, +9.1% (3,221.59 to 3,514.11; R-L563). Segment profit after its own finance cost and D&A, plus JV share, fell from 533.72 to 530.60 Mn (R-L581). Excluding JV share it was flat at 471.76 to 472.80 Mn.
- Incremental segment EBITDA margin was 18.0% (52.64 / 292.52; R-L566), against a 22.3% average. The harsh ex-OI margin fell from 20.59% to 19.27%.
- Aerospace finance cost rose 41.45 Mn QoQ, +53% (R-L571). Aerospace segment liabilities rose 840.26 Mn in H1 (4,741.99 to 5,582.25; R-L597).
- Management says the H1 receivables (+341.42 Mn) and inventory (+1,157.45 Mn) build is "driven by aerospace growth" (C-FT254-255; R-L445-446). This quarter, aerospace growth adds revenue and capital, not profit after financing, and not cash.
Survives: YES.
In A4 already: YES. Flat after D&A and finance (A4-L851), finance +53% (A4-L261, L393), harsh margin fall (A4-L348), WC attribution and INDETERMINATE cash (A4-L301, L305). ON TRACK on revenue and the order book is a fair status with these counters shown. No graft required.

### Claim 2. Order book USD 1,096 Mn, +9% QoQ, "HIGH on level"; growth visibility up (A4-L387, L417, L506)
Strongest bear counter from the extract:
- The order book is a management number with no filed definition or reconciliation.
- The filed proxy for customer commitment, contract liabilities (advances), fell. Current fell from 338.34 to 132.56 Mn, -60.8% (R-L475). Non-current fell from 73.51 to 69.08 Mn (R-L465). The cash flow shows a (210.43) Mn outflow (R-L520).
- Management refused a FY27-29 revenue figure (C-FT755-757). It puts execution at 5-7 years "based on the customer demands" (C-FT752-755). The new Safran scope commercialises in FY29 (C-FT458). The analyst framed it as outside the book, and the reply began "Yeah" (C-FT451-453).
- So the +9% adds little FY27-28 revenue visibility.
Survives: YES.
In A4 already: YES (QfM 29 A4-L781; "LOW on timing" A4-L506; "earnings timing FY29+" A4-L417; QfM 27 A4-L779). No graft required.

### Claim 3. "The promoter puts Rs 650 Cr in at Rs 231.55" (Reading A, A4-L931); "committed to pay the balance irrespective of market price" (6C-bis, A4-L378, NOTION-PRIOR)
Strongest bear counter from the extract:
- The filed notes say the warrants were approved "subject to receipt of requisite regulatory approvals". They "are proposed to be converted on or before December 31, 2027" (R-L272-275, R-L665-667).
- Only Rs 3,250 Mn (50%) is payable on allotment (C-FT269-270). The balance comes only on conversion.
- At CMP Rs 212 (operator-supplied, A4-L924), the Rs 231.55 issue price (R-L272-273) is 9.2% above market. So the second Rs 325 Cr is a promoter option running to 31-Dec-2027, not committed cash.
- The "irrespective of market price" commitment is not in this corpus. The filed word "proposed" is weaker, and filed evidence wins on conflict (A4 caveat 2, A4-L14).
- The warrant-use split (289 + 100 + 100 + balance; C-FT760-765) and A4's "funding exceeds stated capex" (A4-L520, L932) both assume the full Rs 650 Cr.
Survives: YES.
In A4 already: PARTLY. Out-of-the-money status is noted (A4-L859, L1026). Missing: the filed "proposed" qualifier, the contingent Rs 325 Cr balance, and a non-conversion bear fork.
Graft required into Reading A (A4-L931), 6C-bis (A4-L378) and the conversion catalyst (A4-L809). Finding M3, route A4.

### Mandatory acquisition-economics probe
(a) Promoter warrant subscription (a stake buy into Aequs). Multiple stated:
- Price Rs 231.55 per share. EPS H1 FY27 (1.61) and FY26 (1.87) (R-L419), so P/E = NM.
- Book value per share = 13,930.70 Mn / 670.67 Mn = Rs 20.77 (R-L457, R-L109), so about 11.1x book.
- Implied post-money value = 231.55 x 698.74 Mn = Rs 16,179 Cr. The promoter's added stake is 4.0% post-issue.
- Quality markers: group ROCE -5% H1 annualised (P-L1202). CFO (808.31) Mn (R-L523). Net debt ex leases +3,144 Mn in H1 (R-L460-468, R-L447-448).
- Reading: this is not a cheap high-quality asset. The price is rich for a business that is losing money and burning cash. If paid in full, the economics favour minority holders. The surviving bear reading is optionality, not price. See Claim 3.

(b) JV and associate stake investment.
- The group invested Rs 93.00 Mn in H1 FY27 (R-L531). The parent invested 285.48 Mn in subsidiaries, associates and JVs (R-L208). A further Rs 100 Cr of warrant money is earmarked for "JV investments and new strategic initiatives" (C-FT764-765).
- No target is named, and no target PAT is disclosed. Price / target PAT: NOT COMPUTABLE from the extract. Missing evidence: the JV name and its PAT.
- Context: the equity-method carrying value of 1,173.93 Mn (R-L437) earned 47.13 Mn in H1 (R-L388), 8.0% annualised. Aerospace JVs earned +119.76 Mn and consumer JVs lost (72.63) Mn (R-L578-579). The consumer JV share was (39.69) Mn in Q2, against (20.42) Mn a year earlier.
- The corpus makes no "cheap, accretive" claim for these investments. The bear reading (cash into unnamed JVs while consumer JV losses rise) survives and is already in A4 at QfM 25-26 (A4-L777-778). No new graft.

Observation, no finding: consumer segment liabilities rose 798.16 Mn in H1 (7,202.93 to 8,001.09; R-L598). That is close to the H1 consumer segment EBITDA loss of 762.85 Mn (R-L567). The consumer loss is being funded on the balance sheet. This is consistent with A4-L620 and L301.

---

## FINDINGS (every finding tagged)

### FACTUAL
- F1 [route A4]. The brief summary (A4-L870) says: "The group pays tax on a loss because the merger of loss-making units was rejected [FILED, R-L265, R-L393]". The cited filing does not support the cause, and the dates disprove it.
  - (i) The rejection order is dated 12-Oct-2026 (R-L265-266). That is after the quarter closed on 30-Sep-2026.
  - (ii) The group paid tax on a loss before the scheme existed. Q2 FY26 tax was 86.48 Mn on PBT of (119.53) Mn, and FY26 tax was 417.55 Mn on PBT of (715.36) Mn (R-L390, R-L393). The board approved the scheme only on 23-Apr-2026 (R-L263).
  - (iii) Management attributes the tax to current tax at profitable aerospace operations in India (C-FT245-247).
  - Fix: "The group pays tax on a loss. Profitable aerospace units pay current tax, and subsidiary losses earn no tax credit [FILED R-L391-393; ASR C-FT245-247]. The 12-Oct-2026 merger rejection blocks one route to offset them [FILED R-L265-268]."

### MISSING
- M1 [route A3, then A4]. Orphan presentation rows R379 and R473: "MoU with GoK for investment of ₹28,560 Mn" (P-L560-562). A4 does not mention them. They bear on A4-L520 (funding exceeds capex), A4-L600-603 (post-FY27 envelope "Not said") and QfM 19-22 (A4-L771-774).
- M2 [route A3, then A4]. Orphan presentation row R418: top 5 customer groups = 63% of H1 FY27 revenue (P-L775-777). A4 does not mention it. The competition brief (A4-L882) names concentration as the watch risk but cites only consumer.
- M3 [route A4]. Unincorporated surviving bear counter (Claim 3). The filed "proposed to be converted" (R-L274-275, R-L666-667) and the contingent Rs 325 Cr balance are absent. At CMP Rs 212 against Rs 231.55, that balance is an option. Graft into A4-L931, A4-L378 and A4-L809.

### CONTRADICTION
- C1 [route A4]. The brief (A4-L870) says "Consumer plant use fell from 22% to 17% [MGMT-FILED, P-L184]". P-L184 prints 17% only. A4's own 6C (A4-L360, L363) tiers the 22% as the analyst's ASR statement (C-FT415-416). It also says comparability with 22% "cannot be proven without the prior deck". Fix: "fell to 17% [MGMT-FILED, P-L184] from 22% in Q1 [ASR C-FT416, analyst, undisputed; basis comparability unconfirmed]".

### STYLE (logged; no re-run)
- S1. FY28E bridge component "(54.8)" (A4-L908). (104.21 + 32.94) x 4 = 548.60 Mn, so it should read (54.9). The 157.9 total is unaffected.
- S2. Rounded displays: -673 bps (exact -673.7) and -974 bps (exact -973.4) at A4-L202-203; EBIT (4.09) / (32.67) against (4.10) / (32.68) at A4-L206; +129.06 against +129.07 Mn at A4-L256. All within rounding.
- S3. Management's ATP answer is qualified "From the scale of investment perspective" (C-FT529-530). A4-L625 ("The CE plant, not toys, drives the loss") and A4-L932 drop that basis. The call gave no measured loss split. Restore the qualifier.
- S4. Mattel is named as a key consumer customer in the deck (P-L659). A4-L321 and L395 anchor Mattel to Notion only.
- S5. A4-L878 tags "segment margin near 22% with other income inside" as [FILED, R-L563, R-L566]. The "other income inside" basis comes from the deck note P-L396 (MGMT-FILED).
- S6. Step 6.5 mixes two run-rates. The annualised PAT is (209.6) (Q2 x 4; A4-L405), and the divergence test uses (210.4) (H1 + 2 x Q2; A4-L407). Label each.
- S7. House style in the brief: hyphenated compound modifiers "loss-making" (A4-L870, L932), "single-site" (A4-L882) and "Make-or-break" (A4-L886).
- S8. JV "stable margins" CONTRADICTED (A4-L695) rests on JV profit share, which carries consumer JV losses. The deck margin basis also supports it. JV EBITDA margin (JV-inclusive figures less reported; P-L301, R-L375, R-L384) was 22.2% in Q2, against 26.7% in Q1 and 23.9% in Q2 FY26. Cite it.
- S9. A1 structured column label: results R147 (11,970.32) and R637 (8,158.19) carry "Q 30-Sep-2025" but sit in the FY 31-Mar-2026 column (R-L110, R-L416; cf. R-L145, R-L456). No A4 number uses them. This is A1 hygiene only.
- S10. Optional sharpening for QfM 9 and 13. Exports are 87% of H1 FY27 revenue (P-L355, layout-assigned R428-R429). The H1 cash flow shows a net unrealised exchange loss of 49.98 Mn (R-L506), plus 40.38 Mn of write-back, lease and disposal gains (R-L496, R-L498, R-L510) that often sit in other income. Both sit beside management's "forex" label for the Q2 other income rise (C-FT223-224).

---

## VERDICT

INCOMPLETE.
- Failing agent (first in chain): A3. A4 follows in the same loop.
- Finding types driving the loop: FACTUAL 1 (F1), MISSING 3 (M1, M2, M3), CONTRADICTION 1 (C1). STYLE 10, logged only.
- Exact gap:
  - (1) A3 reviews presentation R379 and R473 (GoK MoU Rs 28,560 Mn, P-L560-562) and R418 (top 5 customer groups 63%, P-L775-777).
  - (2) A4 then works those findings into the funding and capex analysis (A4-L520, L600-603, QfM 19-22) and the competition brief (A4-L882).
  - (3) A4 rewrites the brief's tax-causation sentence (F1, A4-L870).
  - (4) A4 grafts the warrant bear counter (M3, A4-L931, L378, L809).
  - (5) A4 re-tiers the 22% utilisation figure (C1, A4-L870).
  - (6) A5 rechecks.
- What passed: the deliverable gate, every enumeration count on all four documents, and the arithmetic (no mismatch above rounding).

## STYLE NOTES
S1-S10 above. Recorded for the A4 pass. They trigger no re-run on their own.

```yaml
# SUPERSEDED by the RE-AUDIT, LOOP 1 block below (kept for the record)
stage: A5-adversary
company: "AEQUS"
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
  orphan_rows: ["presentation R379 (P-L562, MoU with GoK for Rs 28,560 Mn investment)", "presentation R473 (P-L560-563, same MoU, FORWARD row)", "presentation R418 (P-L775, top 5 customer groups = 63% of H1 FY27 revenue)"]
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Promoter puts Rs 650 Cr in at Rs 231.55 (A4-L931); balance committed irrespective of price (A4-L378, Notion only)", counter: "Filed notes say warrants are 'proposed to be converted on or before 31-Dec-2027' and subject to regulatory approvals; only Rs 325 Cr (50%) is due on allotment; at CMP Rs 212 the Rs 231.55 price is 9.2% above market, so the Rs 325 Cr balance is a contingent promoter option, not committed cash; warrant-use split and A4 funding-exceeds-capex view assume the full Rs 650 Cr", source_line: "R-L272-275, R-L665-667, C-FT269-272, C-FT760-765", type: MISSING}
findings_by_type:
  factual:
    - "F1 [A4] Brief A4-L870: 'pays tax on a loss because the merger ... was rejected' [FILED R-L265, R-L393] is unsupported. Rejection dated 12-Oct-2026 is post-period (R-L265). Tax on a loss predates the scheme: Q2 FY26 tax 86.48 Mn on PBT (119.53) Mn, FY26 417.55 on (715.36) (R-L390, R-L393), scheme approved 23-Apr-2026 (R-L263). Mgmt attributes it to aerospace current tax (C-FT245-247)."
  missing:
    - "M1 [A3 then A4] Orphan presentation R379/R473: MoU with GoK for Rs 28,560 Mn investment (P-L560-562) absent from A4, though A4 argues funding outruns FY27 capex and the post-FY27 envelope is unsaid (A4-L520, L600-603, QfM 19-22)."
    - "M2 [A3 then A4] Orphan presentation R418: top 5 customer groups = 63% of H1 FY27 revenue (P-L775-777) absent; competition brief A4-L882 names concentration as the watch risk but cites consumer only."
    - "M3 [A4] Unincorporated surviving bear counter on promoter warrants: filed 'proposed to be converted' (R-L274-275, R-L666-667) and the contingent Rs 325 Cr balance at CMP 212 < 231.55 are missing from Reading A (A4-L931), 6C-bis (A4-L378) and the conversion catalyst (A4-L809)."
  contradiction:
    - "C1 [A4] Brief A4-L870 tiers 'consumer plant use fell from 22% to 17%' as [MGMT-FILED, P-L184]; P-L184 prints 17% only; A4 6C (A4-L360, L363) tiers 22% as ASR analyst speech (C-FT416) with basis comparability unproven."
  style: ["S1 FY28E (54.8) should read (54.9)", "S2 rounding displays bps/EBIT/bridge", "S3 ATP 'scale of investment' qualifier dropped", "S4 Mattel named in deck P-L659", "S5 OI-inside basis is P-L396 not R-L563/566", "S6 two run-rate PAT definitions in Step 6.5", "S7 hyphenated compound modifiers in brief", "S8 cite deck JV EBITDA margin 22.2% vs 26.7%", "S9 A1 R147/R637 column label", "S10 exports 87% and H1 unrealised FX loss 49.98 Mn for QfM 9/13"]
loop_back_to: "A3"
gap: "A3: review presentation R379/R473 (MoU with GoK for Rs 28,560 Mn, P-L560-562) and R418 (top 5 customer groups 63% of H1 FY27 revenue, P-L775-777). A4 then: work them into the funding and capex analysis (A4-L520, L600-603, QfM 19-22) and the competition brief (A4-L882); rewrite the brief tax-causation sentence (F1, A4-L870); graft the warrant bear counter with the filed 'proposed to be converted' and the contingent Rs 325 Cr balance (M3, A4-L931, L378, L809); re-tier the 22% utilisation as ASR (C1, A4-L870). Then A5 rechecks."
style_notes:
  - "S1 FY28E bridge component (54.8) at A4-L908 recomputes to (54.86) = (54.9); total 157.9 unaffected."
  - "S2 Rounded displays: -673 bps (exact -673.7), -974 bps (exact -973.4) A4-L202-203; EBIT (4.09)/(32.67) vs (4.10)/(32.68) A4-L206; +129.06 vs +129.07 Mn A4-L256."
  - "S3 ATP loss attribution was qualified 'From the scale of investment perspective' (C-FT529-530); A4-L625 and L932 drop it; no measured split was given."
  - "S4 Mattel is a named key consumer customer in the deck (P-L659); A4-L321 and L395 anchor it to Notion only."
  - "S5 A4-L878 'other income inside' basis is the deck note P-L396 (MGMT-FILED), not R-L563/566."
  - "S6 Step 6.5 uses (209.6) (Q2 x 4) and (210.4) (H1 + 2 x Q2) in one step (A4-L405, L407); label each."
  - "S7 Hyphenated compound modifiers in the brief: loss-making (A4-L870, L932), single-site (A4-L882), Make-or-break (A4-L886)."
  - "S8 JV 'stable margins' CONTRADICTED (A4-L695): add the deck basis, JV EBITDA margin 22.2% Q2 vs 26.7% Q1 vs 23.9% Q2 FY26 (P-L301, R-L375, R-L384)."
  - "S9 A1 structured R147 (11,970.32) and R637 (8,158.19) labelled Q 30-Sep-2025 but sit in the FY 31-Mar-2026 column (R-L110, R-L416); no A4 number affected."
  - "S10 For QfM 9/13: exports 87% of H1 revenue (P-L355, R428-R429 layout-assigned); H1 net unrealised FX loss 49.98 Mn (R-L506); 40.38 Mn write-back, lease and disposal gains (R-L496, R-L498, R-L510) often booked in other income."
analyst_note: "Arithmetic is clean. Over 100 derived figures were recomputed from raw Rs Mn lines, none off beyond rounding, and the PAT bridge ties exactly. Enumeration ties on all four documents, and A1 dropped nothing from the fulltext. The failures are completeness and judgement. Dates alone disprove the tax sentence: the rejection is post-period, and tax on a loss predates the scheme. The GoK MoU cuts both ways. It may explain why funding outruns FY27 capex. It also signals a capex programme far above any guided figure, which raises the dilution and leverage risk. A4 should show both readings. The warrant probe found a rich price, 11.1x book for a business losing money. Minority economics hold if paid; the live risk is the optional second Rs 325 Cr. Consumer segment liabilities rose 798 Mn in H1 (R-L598), close to the 763 Mn consumer EBITDA loss, so the loss is balance-sheet funded. Loop A3 only for three presentation rows; the A4 fixes are text edits."
```

---

# RE-AUDIT, LOOP 1 (28-Oct-2026; the one permitted iteration)

Scope. I re-checked F1, M1, M2, M3 and C1 against the revised A4 review (runs/aequs-q2fy27/work/review_aequs_q2fy27.md, now 1,085 lines with a LOOP 1 CHANGE LOG at A4-L1069-1084). I then swept every revised passage for new FACTUAL, MISSING or CONTRADICTION items. Line numbers below are revised-review lines.
Input discipline: I did not open runs/aequs-q2fy27/work/forensics_presentation_aequs_q2fy27.md. It is A3 reasoning, which A5 must not read. A4's P-A3-23 and P-A3-24 citations are taken as labels only; every fact below is re-derived from A1 lines.

## Item status

| Item | Type | Revised location | Re-derived check | Status |
|---|---|---|---|---|
| F1 tax causation | FACTUAL | Brief A4-L889; sweep A4-L91, L262, L354, L400, L706, L911, L933, L1051 | The causal clause is gone. The brief now says aerospace units pay current tax and subsidiary losses earn no credit (R-L391-393; C-FT245-247). It adds that the same happened in Q2 FY26 and FY26 (R-L390, R-L393), and that the 12-Oct-2026 rejection came after the quarter and blocks one offset route (R-L265-268). Step 4 (A4-L262) restates Q2 FY26 tax 8.65 on PBT (11.95) and FY26 41.76 on (71.54), both before the 23-Apr-2026 scheme (R-L263): matches 86.48 / (119.53) and 417.55 / (715.36) Mn. No causal wording remains (grep of "merger" and "amalgamation" lines). | CLOSED |
| M1 GoK MoU (R379/R473) | MISSING | A4-L324, L424, L514, L528, L609-611, L651, L739, L804-805, L829, L847, L897, L915, L954, L1035, L1056 | Stated as P-L560-562: "MoU with GoK for investment of Rs 28,560 Mn", undated, entity and funding NOT FOUND. That matches the deck. New figures check: 28,560 / 13,921.31 total equity = 2.05x (R-L459); 28,560 / 1,597 deck H1 capex = 17.9x (P-L501). Both readings are shown (A4-L528): an unfunded Aequs capital call, or a partner and state ecosystem headline. A separating observation is named. QfM 41-42 and a forward map row with bull and bear forks were added. | CLOSED |
| M2 top-5 concentration (R418) | MISSING | A4-L325, L397, L423, L652, L741, L806, L830, L901, L1036, L1057 | Stated as "Five customer groups gave 63% of H1 FY27 revenue [MGMT-FILED, P-L775-777]". That matches P-L775. The new inference "about 75% of aerospace revenue if all five are aerospace [INFERENCE, 63/84]" checks out: 63 / 84 = 75.0%, with aerospace 84% of H1 per P-L584 and C-FT198, and it is labelled conditional. "15 OEM customer groups" matches P-L775. The competition brief now names concentration in both segments. | CLOSED |
| M3 warrant bear counter | MISSING | A4-L73, L92, L380-382, L528, L707, L824, L918, L942-943, L952-953, L1030, L1055 | The filed "proposed to be converted on or before December 31, 2027" is quoted (R-L274-275, R-L666-667). Only Rs 325 Cr (50%) is due on allotment (C-FT269-270). The second Rs 325 Cr is an option while CMP Rs 212 is below Rs 231.55. "Irrespective of market price" is re-tagged NOTION-PRIOR only. Reading A now says "commits Rs 325 Cr on allotment" with a bear counter inside it. A non-conversion fork is in the forward map (A4-L918). "9.2% above market" checks: 231.55 / 212 = 1.092. | CLOSED |
| C1 22% tier | CONTRADICTION | Brief A4-L889; A4-L349, L365, L369, L822, L865, L1028, L1045 | Brief now reads 17% [MGMT-FILED, P-L184] and 22% in Q1 [ASR C-FT416, analyst, undisputed; NOTION N-L107; basis comparability unconfirmed]. 6B, 6C and the monitorables carry the same tier. The falsification leg rests on 17% against the 23% threshold, so the verdict is unaffected. | CLOSED |

## New-item sweep (revision introduced no FACTUAL, MISSING or CONTRADICTION)

- Every new number recomputes: 2.05x, 17.9x, 75% (63/84), 9.2%, the Q2 FY26 and FY26 tax-on-loss pairs. The FY28E component now reads (54.9) (A4-L929), and the 157.9 total is unchanged. No headline figure moved (change log A4-L1081-1084, verified against A4-L889, L929, L934).
- No two cells disagree. The verdict card (PROCEED WITH FLAGS), cash conversion (INDETERMINATE-WITH-DIRECTION), position branch (8A-W) and falsification status (FIRED on both legs) are consistent across Section A, Section B, Section C and the YAML.
- The deliverable gate still passes. All five brief parts are present (A4-L887-918). The forward map now has 10 dated catalysts, each with a bull and a bear fork.
- One new STYLE item:
  - S11. A4-L382 and L824 say non-conversion "forfeits the upfront". Neither cited line (R-L274-275, R-L666-667, C-FT269-272) states forfeiture. The corpus gives only the 50% upfront, the "required minimum 25%" and the 18-month window (C-FT269-271). Forfeiture is the standard term for preferential warrants under SEBI ICDR, so the fact is right and the Rs 325 Cr received conclusion holds. Only its anchor is missing. Fix: tag it "[regulatory term, SEBI ICDR; not stated in corpus]". It changes no number, fact or verdict, so it is STYLE.
- Carried STYLE notes:
  - S1 is closed.
  - S3 is still open. Reading B (A4-L954) says "Management says the majority of the loss sits in the electronics plant" without the "scale of investment" basis (C-FT529-530). The new "Management says" framing narrows the gap.
  - S5 and S7 are still open (A4-L897, L901, L905, L954).
  - S2, S4, S6, S8, S9 and S10 are carried as logged.

## Final verdict, loop 1

COMPLETE. All FACTUAL, MISSING and CONTRADICTION items (F1, M1, M2, M3, C1) are CLOSED. No new looping item exists. The remaining findings are STYLE only (S2-S11), recorded with no re-run. The review may proceed to the Notion save gate.

```yaml
stage: A5-adversary
company: "AEQUS"
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
  orphan_rows: []               # loop 1: R379, R473, R418 now incorporated (A4-L528, L897, L901, QfM 41-43)
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []     # loop 1: warrant counter grafted (A4-L382, L918, L953); claims 1-2 counters already present
findings_by_type:
  factual: []                   # F1 CLOSED loop 1 (A4-L889, L262)
  missing: []                   # M1, M2, M3 CLOSED loop 1
  contradiction: []             # C1 CLOSED loop 1 (A4-L889, L349, L365)
  style: ["S2 rounding displays bps/EBIT/bridge", "S3 ATP 'scale of investment' qualifier still dropped (A4-L954)", "S4 Mattel named in deck P-L659", "S5 OI-inside basis is P-L396 not R-L563/566 (A4-L897)", "S6 two run-rate PAT definitions in Step 6.5", "S7 hyphenated compound modifiers in brief (A4-L901, L905, L954)", "S8 cite deck JV EBITDA margin 22.2% vs 26.7%", "S9 A1 R147/R637 column label", "S10 exports 87% and H1 unrealised FX loss 49.98 Mn for QfM 9/13", "S11 'forfeits the upfront' unanchored (A4-L382, L824)"]
loop_back_to: ""
gap: ""
style_notes:
  - "S1 CLOSED loop 1: FY28E component now (54.9) at A4-L929."
  - "S2 Rounded displays: -673 bps (exact -673.7), -974 bps (exact -973.4); EBIT (4.09)/(32.67) vs (4.10)/(32.68); +129.06 vs +129.07 Mn."
  - "S3 ATP loss attribution was qualified 'From the scale of investment perspective' (C-FT529-530); Reading B A4-L954 still omits it, now framed as 'Management says'."
  - "S4 Mattel is a named key consumer customer in the deck (P-L659); A4 anchors it to Notion only."
  - "S5 Brief A4-L897 'other income inside' basis is the deck note P-L396 (MGMT-FILED), not R-L563/566."
  - "S6 Step 6.5 uses (209.6) (Q2 x 4) and (210.4) (H1 + 2 x Q2) in one step; label each."
  - "S7 Hyphenated compound modifiers in the brief: single-site (A4-L901), Make-or-break (A4-L905), loss-making (A4-L954)."
  - "S8 JV 'stable margins' CONTRADICTED: add the deck basis, JV EBITDA margin 22.2% Q2 vs 26.7% Q1 vs 23.9% Q2 FY26 (P-L301, R-L375, R-L384)."
  - "S9 A1 structured R147 (11,970.32) and R637 (8,158.19) labelled Q 30-Sep-2025 but sit in the FY 31-Mar-2026 column (R-L110, R-L416); no A4 number affected."
  - "S10 For QfM 9/13: exports 87% of H1 revenue (P-L355); H1 net unrealised FX loss 49.98 Mn (R-L506); 40.38 Mn write-back, lease and disposal gains (R-L496, R-L498, R-L510) often booked in other income."
  - "S11 A4-L382 and L824 say non-conversion 'forfeits the upfront'; no cited line states forfeiture (corpus gives 50% upfront, 25% minimum, 18-month window, C-FT269-271). Correct under SEBI ICDR; tag as a regulatory term not in the corpus."
analyst_note: "Loop 1 closed all five looping findings, and I re-derived each closure from A1 lines, not from the change log. The tax sentence now rests on dated filed facts. The GoK MoU enters as an undated intent with both readings and a separating observation. That is the honest treatment: the deck gives no entity, period or funding source. The new ratios recompute (2.05x equity, 17.9x H1 capex). The 75% aerospace concentration figure is properly conditional. The warrant counter is grafted in five places, and Reading A now claims only the Rs 325 Cr due on allotment. The one new defect is an unanchored but correct legal term ('forfeits'), logged as STYLE. I did not read the A3 forensics file; A5 must not see A3 reasoning. Verdict COMPLETE; save may proceed."
```
