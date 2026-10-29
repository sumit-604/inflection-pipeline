# A5 ADVERSARY / COMPLETENESS AUDIT: Dynamic Cables Limited (DYCL), Q2 FY27

| Field | Value |
|---|---|
| Review under audit | runs/dycl-q2fy27/work/review_dycl_q2fy27.md (1,032 lines) |
| Inputs read | 4 A1 fulltexts, 4 A1 structured files, 3 A2 ledgers, the A4 review. No source PDF. Nothing under inputs/. No A3 notes. |
| Anchor convention | RES / PR / GOV Lnnn = fulltext file line. CC Lnnn = concall line prefix (file line = Lnnn + 20). REV Lnnn = review file line. R### = A1 structured row of the named document. |
| Units | Results Rs Lakhs x0.01 = Rs Cr, recomputed at full precision, then rounded. |
| Rounding rule applied | A value passes if it matches the full-precision result OR the result of A4's own displayed rounded parts, within one unit of the last shown digit. Anything else is a mismatch. |
| Model | claude-opus-5-5 |

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Part | Heading | Content check | Status |
|---|---|---|---|
| 1 Summary narrative | REV L869 | 17 lines (REV L871-L887), inside the 10-20 line band; every number carries a provenance tag | present |
| 2 Sector intelligence | REV L889 | 12 lines (REV L891-L902) | present |
| 3 Business-model intelligence | REV L904 | 11 lines (REV L906-L916) | present |
| 4 Competition intelligence | REV L918 | 11 lines (REV L920-L930) | present |
| 5 Forward map | REV L932 | make-or-break line plus 10 catalyst rows, each with a bull and a bear column (REV L934-L947) | present (STYLE S-07: one row has no real fork, two rows undated) |

Gate result: PASS. All five parts exist and carry real content.

---

## 1. COVERAGE AUDIT

Method. I ran a fresh pass over each fulltext: results statement rows (RES L201-L238, L329-L357, L458-L514), note headers (RES L359-L367, L516-L518), auditor paragraphs (RES L90-L122), "-" cells, every numeral, every speaker turn prefix and every analyst question in the concall, every sentence of the press-release MD quote and highlights, and every unit in the governance filing. I diffed each count against the A2 COUNT TEST blocks.

| Document / category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: notes | 12 | 12 (Notes 1-9 RES L359-L367; CF notes 1-3 RES L516-L518) | none | PASS |
| Results: line items | 124 | 124 (BS 38 RES L201-L238; P&L 29 RES L329-L357; CF 57 RES L458-L514) | none | PASS |
| Results: zero-standing cells | 62 | 62 (BS 10; P&L 30; CF 22; 23 lines affected) | none | PASS |
| Results: agenda items | 1 | 1 (RES L35-L38) | none | PASS |
| Results: auditor paragraphs | 4 | 4 (RES L90, L96, L103, L112) | none | PASS |
| Results: entities | 36 | 36 (R395-R430) | none | PASS |
| Results: structured IDs | 482 | 482 (NUMBER 394, ENTITY 36, FORWARD 2, DATE 23, QUALIFIER 27) | none | PASS |
| Press release: numbers | 107 | 107 (tiles 12, table 60, highlights 3, borrowing 24, about 2, identifiers 6) | none | PASS |
| Press release: entities / forward / dates / qualifiers | 17 / 5 / 11 / 11 | 17 / 5 / 11 / 11 | none | PASS |
| Press release: table lines / borrowing lines | 10 / 8 | 10 / 8 (PR L114-L123; PR L140-L155) | none | PASS |
| Press release: qualitative MD and highlight claims (A2 sweep class, M1-M2) | 2 | 3 (M1 PR L127; M2 PR L108; plus PR L109-L110) | none | FAIL: 1 missing (F-05) |
| Concall: numbers | 58 + M03 | 59 (R001-R058 plus CC L344 "20-30 years, 40 years") | none | PASS |
| Concall: entities / forward / dates / qualifiers | 54 / 30 / 17 / 15 | 54 / 30 / 17 / 15 | none | PASS |
| Concall: questions | 33 | 33 (14 callers; Ankit Shah twice, T38 and T88) | none | PASS |
| Concall: turns | 115 | 115 (T00-T114) | none | PASS |
| Concall: qualitative management claims (A2 sweep class, M01-M05) | 5 | 10 (M01-M05 plus CC L030-L032, L033-L034, L044-L047, L050-L051, L052-L054) | none | FAIL: 5 missing (F-05) |
| Governance (no A2 ledger, coordinator note, REV L28) | n/a | 116 structured (NUMBER 34, ENTITY 36, FORWARD 12, DATE 18, QUALIFIER 16); every material unit (fine, delay, deadline, freeze, Z-group, board, blank annexure) found in REV L93-L102 | n/a | PASS with qualifier gap F-06 |

Orphan test (ledger row present, A4 silent). No orphan rows.
- Results: REV L25 marks all 482 IDs reviewed by category. Step 1 cites every P&L line (RES L329-L357). Step 5 cites every CF line it uses (RES L458-L514). BS lines with no line-level cite (RES L205, L206, L214, L223, L226, L230, L233-L236) fall under the category mark and carry no finding.
- Press release: REV L26 marks 153 rows. M1 cited REV L272, L723. M2 cited REV L448.
- Concall: each of R175-R207 has its own row (REV L554-L586). M01 REV L466. M02 REV L893. M03 under the category mark only (REV L27; immaterial). M04 REV L571, L601. M05 REV L271, L898. All 115 turns REV L27.

Missing-from-ledger detail (F-05). A4's own opening-claims inventory (REV L455-L467) lists 11 claims from T03. The A1 structured file and the A2 ledger hold 6 of them (R066, R113, R067-R068, R114, M01, R115). Five are in neither (grep for "prudent" and "disciplined" over all structured files and ledgers returns no match):

| Unit | Text | A4 use |
|---|---|---|
| CC L030-L032 | "We have continued to build our industry demand, discipline and execution, and our focus on operational efficiency" | REV L457 |
| CC L033-L034 | "Our performance reflects the resilience of our business and our ability to navigate a dynamic operating environment" | REV L458 |
| CC L044-L047 | "We continue to focus on expanding our market reach, strengthening customer relationships ..." | REV L462 |
| CC L050-L051 | "Commodity, price, volatility, and geopolitical developments continue to influence the business environment" | REV L464, L448 |
| CC L052-L054 | "Our emphasis remains on disciplined execution, prudent working capital management, and operational excellence" | MATERIAL. It carries A4's CONTRADICTED finding (REV L473, L644, L715) and one of the two "narrative contradicts filing" items behind the verdict (REV L831, L1029). |
| PR L109-L110 | "We have always followed disciplined approach towards execution, expanding our market reach and strengthening our position as a trusted partner of evolving Indian power landscape." | Not cited. It is the filed (MGMT tier) twin of CC L052-L054 and sits one line after M2 (PR L108), which A2 did add. |

By A2's own sweep standard (M01 and M2 are claims of the same class), these are enumerable units. FAIL, return to A2.

---

## 2. ARITHMETIC AUDIT

Raw inputs: RES L201-L238 (BS), RES L329-L357 (P&L), RES L458-L514 (CF), PR L113-L155, CC L001, GOV L36-L37, L155-L170. Column order where six values appear: Q2 FY26 / Q1 FY27 / Q2 FY27 / FY26 / H1 FY26 / H1 FY27.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 1 extraction table, all 96 filled cells (Lakhs x0.01) | REV L114-L130 | identical | RES L329-L357 | PASS |
| Tax split, current and deferred, 12 cells | REV L132 | identical | RES L343-L344 | PASS |
| Operating EBITDA (PBT + D + FC - OI) | 30.82 / 38.00 / 36.35 / 129.56 / 57.77 / 74.35 | 30.82 / 38.00 / 36.35 / 129.56 / 57.77 / 74.35 | RES L330, L336, L337, L342 | PASS |
| Op EBITDA margin | 10.95 / 10.88 / 10.01 / 10.82 / 10.63 / 10.44 % | 10.95 / 10.88 / 10.01 / 10.82 / 10.63 / 10.44 % | RES L329 | PASS |
| Reported EBITDA | 32.01 / 39.18 / 37.40 / 136.31 / 61.69 / 76.58 | identical | RES L336-L342 | PASS |
| Reported EBITDA margin | 11.37 / 11.22 / 10.30 / 11.38 / 11.35 / 10.75 % | identical | RES L329 | PASS |
| Core PBT ex-OI | 25.15 / 32.28 / 28.63 / 106.31 / 46.78 / 60.91 | identical | RES L330, L342 | PASS |
| OI / PBT | 4.51 / 3.54 / 3.54 / 5.97 / 7.74 / 3.54 % | identical | RES L330, L342 | PASS |
| Effective tax rate | 25.44 / 25.43 / 25.36 / 25.32 / 25.36 / 25.40 % | identical | RES L342-L344 | PASS |
| PAT margin | 6.97 / 7.15 / 6.10 / 7.05 / 6.96 / 6.61 % | identical | RES L345 | PASS |
| Gross margin ((Rev - materials - change in inv) / Rev) | 20.75 / 19.40 / 16.71 / 19.52 / 20.09 / 18.03 % | identical | RES L332, L334 | PASS |
| Other expenses / revenue | 5.43 / 4.56 / 3.09 / 4.84 / 5.36 / 3.81 % | identical | RES L338 | PASS |
| Employee cost / revenue | 4.37 / 3.95 / 3.62 / 3.85 / 4.11 / 3.78 % | identical | RES L335 | PASS |
| PR "Operating Profits" vs Op EBITDA | within 0.1 | 36.35 vs 36.3; 74.35 vs 74.3; others exact to 0.1 | PR L115 | PASS |
| PR snapshot tiles | +31 / +29 / +24 % H1; +29 / +18 / +13 % Q2 | +31.0 / +28.7 / +24.5; +29.0 / +17.9 / +12.8 | PR L78-L86 | PASS |
| Step 2 YoY: revenue, Op EBITDA, margin | +29.0%, +17.9%, -94 bps | +28.99%, +17.94%, -93.8 bps | RES L329 | PASS |
| Step 2 YoY: D&A, D&A QoQ, finance cost | +23.5%, +21.5%, +48.4% | +23.54%, +21.49%, +48.42% | RES L336-L337 | PASS |
| Step 2 YoY: EBIT, OI, core PBT, PBT, PAT, EPS | 28.01 to 32.88 +17.4%; -11.7%; +13.8%; +12.7%; +12.8%; +12.6% | +17.38%; -11.68%; +13.85%; +12.70%; +12.82%; +12.59% | RES L330-L357 | PASS |
| H1 revenue YoY; QoQ margin; incremental margin; H1 OI | +31.0%; -88 bps; 6.8%; -43.1% | +31.03%; -87.6 bps; 6.77%; -43.09% | RES L329-L330 | PASS |
| Step 3: Q1 FY26 derived revenue, margin, core PBT | 262.04; 10.28%; 21.63 | 262.04; 10.28%; 21.63 | RES L329-L342 | PASS |
| Step 3: H2 FY26 revenue, quarterly avg, margin, core PBT | 654.23; 327.11; 10.97%; 59.53 | 654.23; 327.11; 10.97%; 59.53 | RES L329-L342 | PASS |
| Step 3: QoQ steps +7.4%, +6.7%, +4.0%; core PBT QoQ -11.3% | as stated | +7.45%, +6.72%, +4.04%; -11.31% | RES L329, L342 | PASS |
| Step 3: H1 avg 356.15, Q2 +2.0%; Q3 base 392.5 | as stated | 356.15, +1.98%; 327.11 x 1.20 = 392.54 | RES L329 | PASS (label: see F-01) |
| Step 4 bridge: revenue at prior margin; margin change | +8.94; -3.41 | +8.936; -3.406 | RES L329-L342 | PASS |
| Step 4 bridge: D&A, FC, OI, tax at prior ETR, ETR change | -0.66, -1.39, -0.14, -0.85, +0.02 | -0.663, -1.385, -0.139, -0.851, +0.023 | RES L330-L344 | PASS |
| Step 4 bridge closes to PAT change; % of prior PAT column | +2.52; 45.5 / -17.3 / -3.4 / -7.1 / -0.7 / -4.3 / +0.1 / +12.8 % | +2.517; 45.5 / -17.3 / -3.4 / -7.1 / -0.7 / -4.3 / +0.1 / +12.8 % | RES L345 | PASS |
| OI reversion effect after tax | +0.10 | +0.104 | RES L330 | PASS |
| CFO; change; CFO/PAT; CFO/Op EBITDA | 20.19 / 6.66; -13.53; 0.53x / 0.14x; 34.9% / 9.0% (-25.9 pp) | 20.19 / 6.66; -13.52; 0.533x / 0.141x; 34.94% / 8.96% (-26.0 pp) | RES L495, L345 | PASS (displayed-parts rule) |
| Capex; FCF; FCF net of disposals | 25.48 / 19.52; (5.30) / (12.86); (12.36) | 25.48 / 19.52; (5.30) / (12.86); (12.36) | RES L495-L497 | PASS |
| WC change; inventories; receivables; payables (CF) | (28.56)/(53.82); (4.79)/(70.65), 14.7x; (0.52)/+13.92; (35.82)/+8.81 | identical; 14.75x | RES L480-L492 | PASS |
| Receivable / inventory / payable days, CCC, on A4's stated basis | 87.7 to 70.3; 65.4 to 76.1; 60.3 to 52.6; 92.8 to 93.8 (+1.0 day, "Flat net") | identical on that basis | RES L209, L211, L231-L232, L329, L332, L334 | FAIL (basis): windows mixed, see F-02 |
| Receivable days gross-up | 70.3 / 1.18 = 59.6 vs company ~59 | 59.6 | PR L129 | PASS |
| PPE, CWIP, other NC assets, MF balance changes | +11.11; +1.66; +2.19; -29.69 | +11.11; +1.66; +2.18; -29.69 | RES L201, L202, L207, L210 | PASS |
| On-BS net debt | (18.44) to 4.09; +22.53 | (18.44) to 4.09; +22.54 | RES L210-L213, L222, L229 | PASS |
| Company net debt incl. LC creditors; LC change | 58.2 to 81.8; +1.1 | 117.0 - 58.8 = 58.2; 115.0 - 33.2 = 81.8; +1.1 | PR L147-L155 | PASS |
| H1 FY27 sources and uses | 38.26 = 38.26 | 38.25 sources, 38.26 uses; gap 0.007 = cash change (0.72 L) | RES L495-L514 | PASS |
| Derived PPE additions | 17.86 | 11.11 + 6.32 + 0.43 = 17.86; plus CWIP +1.66 = 19.52 = cash capex RES L496 (cross-tie holds) | RES L201, L337, L460, L497 | PASS |
| TTM PAT; TTM EPS; TTM revenue | 93.71; 19.33; 1,366.52 | 93.70 (93.71 on displayed parts); 19.33; 1,366.52 | RES L329, L345, L356 | PASS |
| Order-book cover; exports share; plant potential share | 0.61x; 7.9%; 18% | 0.607x; 7.86%; 17.9% | PR L131, L133; CC L089 | PASS |
| Share count; max dilution; ESOP charge | 48,458,600; 0.38%; 0.33 Cr | 48,458,600; 0.378%; 0.329 Cr | RES L354, L365, L476 | PASS |
| Finance cost QoQ; other expenses QoQ; other NCA; other CA | +48.5%; -29.7%; +58.5%; +43.8% | +48.54%; -29.67%; +58.49%; +43.80% | RES L336, L338, L207, L216 | PASS |
| Gross margin change YoY | -404 bps | -403.6 bps | RES L332-L334 | PASS |
| Other expenses / revenue change YoY | -233 bps (REV L722) | -234.5 bps (5.4306% to 3.0852%); A4's displayed parts give -234 | RES L338 | FAIL (F-04) |
| Brief: "sold Rs 29.69 Cr of mutual funds" | 29.69 sold (REV L879) | balance fell 29.69 (RES L210); sale proceeds 28.35 (RES L503); FV item 1.35 (RES L464); A4's own sources table uses 28.35 (REV L244) | RES L210, L464, L503 | FAIL (F-03) |
| FY27 20% guide test (M4, forward map, YAML monitorable) | "FY27 value growth vs 20% guide: H2 revenue at least 20% above H2 FY26 Rs 654.23 Cr" (REV L846, L945, L1002) | H2 at +20% = 785.07 Cr, which makes FY27 = 1,497.36 Cr = +25.0%. FY27 at +20% = 1,437.38 Cr needs H2 = 725.09 Cr = +10.8%, i.e. 362.54 Cr a quarter | RES L329 | FAIL (F-01) |
| Governance: fine; Cr equivalent; payment due | 2,000 + 360 = 2,360; 0.000236 Cr; 29-Aug-2026 | identical | GOV L36-L37, L155, L161, L168 | PASS |
| Concall: duration; Q&A time share; Q&A turn share | 52.3 min; 47.4 min, ~91%; 110 of 114, 96% | 52.27; 47.43, 90.7%; 96.5% | CC L001, L062, L410 | PASS |
| Concall: grade count; C/D/E share; specificity; opening quantified; defensive count | 3/5/11/8/5/1; 24 of 32 = 75%; 9/30 = 0.30, 5/26 = 0.19; 2/11 = 18%; 16 | identical | REV L554-L586, L671-L696 | PASS |

Mismatch detail.

F-01 (FACTUAL). REV L846 (M4), REV L945 (forward map) and REV L1002 (YAML monitorable) label the test "FY27 value growth vs 20% guide" but set the bar at H2 FY27 at least 20% above H2 FY26. Recomputed: FY26 1,197.82 x 1.20 = 1,437.38 Cr; less H1 FY27 712.29 Cr = 725.09 Cr needed in H2, +10.8% on 654.23 Cr, 362.54 Cr a quarter (RES L329). A4's bar (785.07 Cr) is FY27 +25.0%. Two dependent statements carry the same error. REV L496 says 20% value growth with dipping metal "requires volume growth above 20%"; for FY27 the H2 value need is +10.8%. REV L362 and REV L1029 call the Rs 392.5 Cr bull line "management's own 20% guide"; on FY27 the guide pace is the bear line (363.19 Cr).

F-02 (FACTUAL). REV L242 sets 31-Mar-2026 day counts on 12-month FY26 flows and 30-Sep-2026 day counts on H1 FY27 flows x2. With revenue +31.0% YoY, the windows do not match, and the 12-month March denominator flatters the trend. Matched windows, same raw inputs (RES L209, L211, L231-L232, L329, L332, L334; H2 FY26 = FY26 less H1 FY26; TTM = H2 FY26 + H1 FY27):

| Day count | A4 (mixed windows) | TTM at both dates (seasonality-neutral) | Trailing 6 months at both dates (company KPI basis, PR L129) |
|---|---|---|---|
| Receivable days | 87.7 to 70.3 (-17.4) | 87.7 to 73.3 (-14.4) | 80.3 to 70.3 (-10.0) |
| Inventory days (COGS) | 65.4 to 76.1 (+10.7) | 65.4 to 79.8 (+14.4) | 59.5 to 76.1 (+16.6) |
| Payable days (COGS) | 60.3 to 52.6 (-7.7) | 60.3 to 55.1 (-5.2) | 54.9 to 52.6 (-2.3) |
| Cash conversion cycle | 92.8 to 93.8 (+1.0, "Flat net") | 92.8 to 98.0 (+5.2) | 84.9 to 93.8 (+8.9) |

Denominators: TTM revenue 1,366.52 Cr; TTM COGS 1,113.56 Cr (H2 FY26 529.67 + H1 FY27 583.89); H2 FY26 revenue 654.23 Cr. "Flat net" does not hold on either matched basis.

F-03 (CONTRADICTION). REV L879 says the company "sold Rs 29.69 Cr of mutual funds". REV L244 (A4's own sources table) uses MF redemption 28.35 Cr (RES L503). The 29.69 Cr is the balance fall (RES L210). The difference is the 1.35 Cr fair-value item (RES L464).

F-04 (FACTUAL). REV L722: other expenses "-233 bps of revenue YoY". Recomputed -234.5 bps (RES L338, L329). A4's own displayed 5.43% and 3.09% give -234.

---

## 3. ADVERSARIAL READ

### ADV-1. Claim: "Growth is real at the top line" (REV L833 Section C Net impact; REV L886 summary read)
- Bear counter from the extract. The only volume figure on the record is the analyst's 6% (CC L123), restated with "of the growth revenue growth is coming from a price increase" (CC L198-L200). Management did not dispute it. It refused a volume split three times (R179, R186, R194) and said "The budget is not volume based" (CC L139). At 6% volume, about 22 points of the 29.0% YoY revenue growth is price and mix [INFERENCE: 1.290 / 1.06 - 1 = 21.7%]. Gross margin fell 404 bps YoY (RES L332-L334). 80-90% of contracts pass metal through (CC L255), and metal is now "dipping" (CC L317; aluminium "3800 to 3000", CC L274, analyst tier, ASR_DOUBT). The price part reverses on pass-through.
- Survives: YES. A4 holds the pieces in Step 6B item 1 (REV L297) and Exchange 2 (REV L607-L613). The claim sites carry no volume qualifier, and the 10-20 line summary the operator reads first never states the 6% figure.
- Graft (F-07, MISSING, A4): add to the summary after REV L883 and to the Section C Net impact row (REV L833): "The only volume figure on the record is an analyst's 6% (CC L123, L198), not disputed. At 6% volume, about 22 points of the 29.0% growth is price and mix [INFERENCE]. That part reverses on pass-through as metal falls (CC L255, L317)."

### ADV-2. Claim: receivable days improved 17.4 days (GREEN); cash conversion cycle "Flat net" (REV L229, L232); "the company KPI looks fair" (REV L1029)
- Bear counter from the extract. The day counts mix a 12-month March window with a 6-month September window (REV L242). On matched windows the receivable gain is 10.0 to 14.4 days, inventory days rise 14.4 to 16.6 days, and the cash cycle worsens 5.2 to 8.9 days (F-02 table). The H1 cash-flow comparatives A4 already uses (RES L480-L481) agree with the direction: receivables released 13.92 Cr against a 0.52 Cr build in H1 FY26, and inventory built 70.65 Cr against 4.79 Cr.
- Survives: YES, on magnitude. The receivable improvement is real but smaller. The cycle is not flat. The KPI reconciliation (70.3 / 1.18 = 59.6 vs ~59, PR L129) stands.
- Graft (F-02, FACTUAL, A4): restate the Step 5 day-count rows on matched windows. Replace "Flat net" with "+5.2 days (TTM) / +8.9 days (trailing 6 months)". Keep the CF comparatives as the basis-free test. The cash classification INDETERMINATE-WITH-DIRECTION (adverse) is unchanged; the direction is reinforced.

### ADV-3. Claim: 20% value-growth guide "CONFIRMED (ahead) for H1" (REV L721); the Rs 392.5 Cr bull line is "management's own 20% guide" (REV L362, L1029)
- Bear counter from the extract. H1 +31.0% (RES L329) front-loads FY27. A 20% FY27 needs only +10.8% in H2, 362.54 Cr a quarter. That pace is A4's bear line (363.19 Cr). A Q3 print A4 calls "bear" therefore keeps FY27 on the guide. The guide is not a demanding bar and does not test H2. With that cushion, management still refused to say FY27 would beat 20% (CC L372) [INFERENCE: a weak signal on H2]. The "confirmed" label is true for H1 and says nothing about H2.
- Survives: YES.
- Graft (F-01, FACTUAL, A4): state the FY27 arithmetic beside the Step 8C thresholds and in the watchpoint row. Relabel M4, the forward-map row and the YAML monitorable to one of two consistent tests: "FY27 at least +20%: H2 FY27 at least Rs 725.09 Cr", or "H2 at the 20% long-run rate: at least Rs 785.07 Cr (FY27 +25.0%)". Correct REV L496 to the +10.8% H2 value need.

### Also tested (counter does not survive)
Claim: headline PAT growth is "real ... not treasury-driven" (REV L173, L212). OI is 3.54% of Q2 PBT (RES L330, L342); reversion adds about 0.10 Cr. The treasury drawdown moves cost to finance cost, which A4 bridges (-1.39 Cr, REV L203) and flags (REV L1021). The Q2 fall in other expenses (RES L338) sits inside the 10.01% margin, which A4 reads together with gross margin (REV L79, L911). No graft.

### Mandatory acquisition-economics probe
Not triggered. No extract describes an acquisition, a business purchase or a stake buy. "Purchase / Acquisition of Property, Plant and Equipment" (RES L496) is capex. Nearest analogue, the new plant: capex amount ND, revenue potential "240, 250 crore" is ASR_DOUBT with the answer opening lost (CC L089-L090). No price-to-earnings multiple can be computed. A4 Questions 6-8 (REV L377-L379) already ask for the inputs.

---

## 4. INDEPENDENT-READ FINDING (outside the three adversarial reads)

F-06 (MISSING, A4). Governance Z-group qualifier.
- Extract: "Further in the event of this being the second consecutive year of non-compliance for the Regulation 31 would result in the company being transferred to Z group and liable for suspension of trading" (GOV L173-L174).
- A4: "a repeat in the June-2027 quarter would trigger the Z-group rule" and "LOW weight, one governance data point, not a pattern" (REV L104). M18 (REV L860), the forward-map row (REV L947) and REV L1016, L1024 test only the June-2027 quarter.
- Gap: (a) The clause reads on "this" instance. No document states the prior-year Reg 31 record, so "not a pattern" is unverified and the Z-group status of the June-2026 lapse is ND, not nil. The 14-Aug letter lists status "Late Submission" with no Z-group action (GOV L155-L161). That leans against a live Z-group status but does not settle the prior-year record. (b) The clause names no quarter. Any Reg 31 lapse in the following year can count. The first test is the Sep-2026 pattern due 21-Oct-2026, which A4 already lists as M17 (REV L859).
- Fix: replace "not a pattern" with "prior-year Reg 31 record ND". Widen M18 and the forward-map row to every quarterly Reg 31 filing through Jul-2027. Add a question: was there any Reg 31 non-compliance in FY26? Add "prior-year record ND" to the Section C Governance row (REV L832).

---

## 5. FINDINGS REGISTER

| ID | Type | Loop to | Gap | Moves a verdict-card number? |
|---|---|---|---|---|
| F-01 | FACTUAL | A4 | "FY27 vs 20% guide" tested at H2 +20% (= FY27 +25.0%); the FY27 20% pace is 725.09 Cr H2, 362.54 Cr a quarter, equal to A4's bear line; REV L362, L496, L846, L945, L1002, L1029 | No number moves. The watchpoint row (REV L837) needs the FY27 qualifier. |
| F-02 | FACTUAL | A4 | Day counts mix 12-month and 6-month windows; matched windows give CCC +5.2 to +8.9 days, not +1.0 "Flat"; REV L229-L232, L242 | No. Cash classification unchanged (direction reinforced). |
| F-03 | CONTRADICTION | A4 | Brief "sold Rs 29.69 Cr" vs sources table 28.35 Cr redemption (RES L503); REV L879 vs REV L244 | No (verdict card states balances 30.62 to 0.93, correct). |
| F-04 | FACTUAL | A4 | Other expenses -233 bps vs -234.5 bps recomputed; REV L722 | No. |
| F-05 | MISSING | A2 | Six enumerable units absent from structured file and ledger: CC L030-L032, L033-L034, L044-L047, L050-L051, L052-L054 (material, carries A4's WC contradiction), PR L109-L110 | No. After A2 adds them, A4 must cite PR L109-L110 (the five CC units are already cited, REV L457-L465). |
| F-06 | MISSING | A4 | Z-group clause reads on the current instance; prior-year Reg 31 record ND; trigger not limited to June-2027; REV L104, L860, L947, L1016, L1024 | No number. Governance row (REV L832) gains a qualifier. |
| F-07 | MISSING | A4 | Surviving ADV-1 counter: volume qualifier (analyst 6%, undisputed) absent where "growth is real at the top line" is claimed; REV L833, L871-L887 | No number. Net impact row (REV L833) gains a qualifier. |

---

## VERDICT

INCOMPLETE.

- Failing agents: A2 first (F-05, MISSING), then A4 (F-01 FACTUAL, F-02 FACTUAL, F-03 CONTRADICTION, F-04 FACTUAL, F-06 MISSING, F-07 MISSING). A3 needs to review only the six new ledger rows.
- Exact gap: A2 adds six sweep rows (CC L030-L032, L033-L034, L044-L047, L050-L051, L052-L054; PR L109-L110). A4 then (1) states the FY27 20% arithmetic (725.09 Cr H2, +10.8%, 362.54 Cr a quarter) and relabels M4, the forward map and the YAML monitorable; (2) restates day counts on matched windows (CCC +5.2 / +8.9 days); (3) corrects "sold Rs 29.69 Cr" to proceeds 28.35 Cr; (4) corrects -233 bps to -235 bps; (5) adds the prior-year Reg 31 ND qualifier and widens the Z-group monitor; (6) grafts the 6% volume qualifier into the summary and Section C; (7) cites PR L109-L110.
- No finding changes the protocol verdict (PROCEED WITH FLAGS) or any verdict-card number.

---

## STYLE NOTES (logged, no loop)

- S-01. Peer-work quotes (REV L900, L921) come from a Notion page outside A5's inputs. A5 did not verify them. Their provenance tag is present.
- S-02. REV L922 tags CC L186 as MGMT-ASR. CC L186 is an analyst turn (T35). Retag to analyst tier.
- S-03. REV L235 labels "Other non-current assets" (RES L207) as "Capital advances". The filing gives no split. Tag [INFERENCE].
- S-04. REV L176 attributes the H1 OI fall to MF redemption without an [INFERENCE] tag. The largest filed driver is interest income, 2.08 to 0.96 Cr (RES L461).
- S-05. Note 5 (RES L363) says prior figures are regrouped "to conform to the classification of current period". Within this filing the line ratios are on one basis; the "reclassification caveat" (REV L69) applies against earlier published figures. Question 13 (REV L384) could say so. No number changes.
- S-06. REV L595 counts "So you expect 20% price growth?" (CC L202) as pushback. It is an analyst misreading that management corrected (CC L203).
- S-07. Forward map: the "Trading window reopens" row (REV L938) has the same text in both forks; drop it or give it a real fork. Two catalysts are undated (REV L939, L943); the labels are honest.
- S-08. A1 anchor drift: concall R037 and R038 cite line 267; the "10 to 11%" text sits on CC L268. A1 only.

---

```yaml
stage: A5-adversary
company: "DYCL"
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
    - "CC L030-L032 (T03 opening claim 1, 'continued to build our industry demand, discipline and execution'); A4 cites REV L457; absent from structured and ledger"
    - "CC L033-L034 (T03 claim 2, 'performance reflects the resilience of our business'); A4 cites REV L458"
    - "CC L044-L047 (T03 claim 6, expanding market reach and customer relationships); A4 cites REV L462"
    - "CC L050-L051 (T03 claim 8, commodity price volatility and geopolitics); A4 cites REV L464"
    - "CC L052-L054 (T03 claim 9, 'prudent working capital management'); MATERIAL, carries A4 CONTRADICTED finding REV L473, L644, L715, L831"
    - "PR L109-L110 (MD quote, 'We have always followed disciplined approach towards execution'); absent from structured, ledger and review"
arithmetic_mismatches:
  - metric: "FY27 value growth vs 20% guide (M4, forward map, YAML monitorable)"
    a4_value: "H2 FY27 at least 20% above H2 FY26 654.23 Cr (= 785.07 Cr, implies FY27 +25.0%)"
    recomputed: "FY27 +20% = 1,437.38 Cr; H2 need 725.09 Cr = +10.8%; 362.54 Cr a quarter (equals A4 bear line 363.19)"
    source_line: "RES L329; REV L846, L945, L1002, L362, L496, L1029"
  - metric: "Cash conversion cycle 31-Mar-2026 to 30-Sep-2026"
    a4_value: "92.8 to 93.8 days, +1.0, Flat net (12-month Mar window vs 6-month Sep window)"
    recomputed: "TTM both dates 92.8 to 98.0 (+5.2); trailing 6 months both dates 84.9 to 93.8 (+8.9); inventory days +14.4 / +16.6; receivable days -14.4 / -10.0"
    source_line: "RES L209, L211, L231-L232, L329, L332, L334; REV L229-L232, L242"
  - metric: "Mutual funds sold in H1 FY27 (brief)"
    a4_value: "29.69 Cr sold (REV L879)"
    recomputed: "proceeds 28.35 Cr (RES L503); balance fall 29.69 Cr (RES L210) includes 1.35 Cr FV item (RES L464)"
    source_line: "RES L210, L464, L503; REV L244"
  - metric: "Other expenses / revenue change YoY"
    a4_value: "-233 bps (REV L722)"
    recomputed: "-234.5 bps (5.4306% to 3.0852%); displayed parts give -234"
    source_line: "RES L329, L338"
surviving_bear_counters:
  - claim: "Growth is real at the top line (REV L833, L886)"
    counter: "Only volume figure is the analyst's undisputed 6%; at 6% volume about 22 of the 29.0 points is price and mix [INFERENCE], reversing on pass-through as metal dips; summary and Section C carry no volume qualifier"
    source_line: "CC L123, L139, L198-L200, L255, L274, L317; RES L332-L334"
    type: MISSING
  - claim: "Receivable days -17.4 GREEN; cash conversion cycle Flat net (REV L229, L232, L1029)"
    counter: "Mixed day-count windows; matched windows give receivables -10.0 to -14.4 days, inventory +14.4 to +16.6 days, CCC +5.2 to +8.9 days"
    source_line: "RES L209, L211, L231-L232, L329, L332, L334; PR L129"
    type: FACTUAL
  - claim: "20% guide CONFIRMED (ahead) for H1; Rs 392.5 Cr bull line is management's own 20% guide (REV L362, L721, L1029)"
    counter: "H1 +31.0% front-loads FY27; FY27 at 20% needs only +10.8% H2 (362.54 Cr a quarter), which is A4's bear line; management still refused an FY27 number (CC L372)"
    source_line: "RES L329; CC L201, L203, L372"
    type: FACTUAL
findings_by_type:
  factual:
    - "F-01 A4: FY27 20% test set at H2 +20% (= FY27 +25.0%); correct FY27 pace is H2 725.09 Cr (+10.8%), 362.54 Cr a quarter; REV L362, L496, L846, L945, L1002, L1029"
    - "F-02 A4: day counts mix 12-month and 6-month windows; matched windows CCC +5.2 (TTM) to +8.9 (6M) days, not +1.0 Flat; REV L229-L232, L242"
    - "F-04 A4: other expenses -233 bps vs recomputed -234.5 bps; REV L722"
  missing:
    - "F-05 A2: six enumerable units absent from structured and ledger: CC L030-L032, L033-L034, L044-L047, L050-L051, L052-L054 (material), PR L109-L110"
    - "F-06 A4: GOV L173-L174 Z-group clause reads on the current instance; prior-year Reg 31 record ND, so 'not a pattern' unverified; trigger not limited to June-2027; REV L104, L832, L860, L947, L1016, L1024"
    - "F-07 A4: surviving ADV-1 counter, analyst 6% volume qualifier absent from summary (REV L871-L887) and Section C Net impact (REV L833)"
  contradiction:
    - "F-03 A4: brief 'sold Rs 29.69 Cr of mutual funds' (REV L879) vs own sources table 28.35 Cr redemption (REV L244; RES L503)"
  style:
    - "S-01 peer-work quotes REV L900, L921 outside A5 inputs, unverified, provenance tag present"
    - "S-02 REV L922 tags analyst turn CC L186 as MGMT-ASR"
    - "S-03 REV L235 labels other non-current assets as capital advances without [INFERENCE]"
    - "S-04 REV L176 attributes OI fall to MF redemption without [INFERENCE]; interest income RES L461 is the larger filed driver"
    - "S-05 Note 5 RES L363 conforms comparatives to current classification; caveat at REV L69 and Q13 premise could say so"
    - "S-06 REV L595 counts CC L202 analyst misreading as pushback"
    - "S-07 forward map trading-window row REV L938 has no real fork; two catalysts undated"
    - "S-08 A1 anchor drift: concall R037-R038 cite line 267, text on CC L268"
loop_back_to: "A2"
gap: "A2: add six sweep rows (CC L030-L032, L033-L034, L044-L047, L050-L051, L052-L054; PR L109-L110). A3: review the six new rows only. A4: (1) F-01 state FY27 20% arithmetic (H2 725.09 Cr, +10.8%, 362.54 Cr a quarter) beside Step 8C and the watchpoint, relabel M4, forward map and YAML monitorable, fix REV L496; (2) F-02 restate Step 5 day counts on matched windows, CCC +5.2 (TTM) / +8.9 (6M) days; (3) F-03 brief MF proceeds 28.35 Cr, balance fall 29.69 Cr; (4) F-04 -233 to -235 bps; (5) F-06 prior-year Reg 31 record ND, widen Z-group monitor to every Reg 31 filing to Jul-2027; (6) F-07 graft 6% volume qualifier into summary and Section C Net impact; (7) cite PR L109-L110. No verdict-card number and no protocol verdict changes."
style_notes:
  - "S-01 peer-work quotes REV L900, L921 outside A5 inputs, unverified, provenance tag present"
  - "S-02 REV L922 tags analyst turn CC L186 as MGMT-ASR; retag analyst tier"
  - "S-03 REV L235 'Capital advances' label for RES L207 other non-current assets; tag [INFERENCE]"
  - "S-04 REV L176 OI fall attributed to MF redemption; tag [INFERENCE]; interest income RES L461 fell 2.08 to 0.96 Cr"
  - "S-05 Note 5 RES L363 conforms comparatives; REV L69 caveat and Q13 premise could say so"
  - "S-06 REV L595 CC L202 is an analyst misreading corrected at CC L203, not pushback"
  - "S-07 forward map REV L938 trading-window row has identical forks; drop or fork it"
  - "S-08 A1 concall R037-R038 anchor line 267; text on CC L268"
analyst_note: "INCOMPLETE on seven non-STYLE findings. None moves a verdict-card number or the PROCEED WITH FLAGS verdict. On A4's stated bases the arithmetic is clean: every P&L, bridge, cash-flow and day-count figure recomputes from RES L201-L514 within rounding, except one bps figure. The material issues are basis and framing. First, day counts mix a 12-month March window with a 6-month September window; matched windows show the cash cycle 5 to 9 days worse, not flat. Second, H1 +31% front-loads FY27: a 20% year needs only +10.8% in H2, about Rs 362.5 Cr a quarter, which is A4's bear line, so the 'FY27 vs 20%' monitor really tests +25%. Third, 'growth is real' carries no volume qualifier where it is claimed; the only volume figure is the analyst's undisputed 6%. A2 must add five MD opening claims and one press-release claim that A4's own Step 1 inventory found; CC L053 among them carries A4's working-capital contradiction. The Z-group clause reads on the current lapse; prior-year record ND. Loop A2, then A3 on new rows only, then A4."
```
