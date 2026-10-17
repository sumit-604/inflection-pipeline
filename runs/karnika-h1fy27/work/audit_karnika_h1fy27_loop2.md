# A5 ADVERSARY / COMPLETENESS AUDIT, LOOP 2 | KARNIKA | h1fy27

Agent: A5, claude-opus-5-5. Run date 2026-10-17. Fresh context.
Inputs read: A4 review (runs/karnika-h1fy27/work/review_karnika_h1fy27.md, 1,377 lines, loop-2 amended), the three A1 fulltexts and three structured files (extracted/), and the three A2 ledgers. I did not read the source PDFs, anything under inputs/, A3 notes, or the earlier A5 audit files.

Anchor key: `res Lnnn` = results fulltext line. `cc Lnnn` = concall fulltext line. `ppt lnnn` / `ppt Rnnn` = presentation fulltext line / structured row. `rev Lnnn` = line in the A4 review. All arithmetic is in Rs lakhs from the filed line, converted at x0.01.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading in review | Status |
|---|---|---|
| 1. Summary narrative | "## 1. SUMMARY NARRATIVE" (rev L1211-1228) | PRESENT. 16 numbered lines, inside the 10-20 line band. Each line carries a provenance tag |
| 2. Sector intelligence | "## 2. SECTOR INTELLIGENCE" (rev L1230-1237) | PRESENT. Market size, structure, input cost, seasonality, trade credit, a not-disclosed list |
| 3. Business-model intelligence | "## 3. BUSINESS-MODEL INTELLIGENCE" (rev L1239-1248) | PRESENT. Standalone model, Kidcity model, deal economics, model drift |
| 4. Competition intelligence | "## 4. COMPETITION INTELLIGENCE" (rev L1250-1256) | PRESENT. Claimed edge, named peers, structural weakness, switch risk |
| 5. Forward map | "## 5. FORWARD MAP" (rev L1258-1271) | PRESENT. Make-or-break line plus 8 dated rows, each with a bull fork and a bear fork |

Gate result: PASS. All five parts are present and carry real content.

---

## 1. COVERAGE AUDIT

Method. I re-ran the enumeration on the A1 fulltexts, not on the ledgers: speaker-label regex for turns; analyst-turn walk for questions; a forward-phrase lexicon sweep (will, would, target, expect, plan, going to, hope, aim, intend, want to, soon, objective, priority, focus, supposed to, projection, predict) over management turns; a digit sweep plus a words-number read for management numbers; numbered-note and table-line walks for the results; page markers and a slide-by-slide number tally for the deck. I then diffed against the A2 ledgers and checked each ledger row against the A4 review.

| Category | A2 count | My fresh count | Orphan rows (ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results: numbered notes | 18 | 18 (notes 1-6, 11-13, printed twice: res L290-L350, L584-L649) | none | PASS |
| Results: unnumbered notes | 2 | 2 (res L334, L632) | none | PASS |
| Results: line items | 210 | 210 (29 + 26 + 44 + 32 + 35 + 44 by table walk) | none | PASS |
| Results: zero-standing | 45 | 45 (grep ZERO_STANDING in structured) | none | PASS |
| Results: agenda items | 1 | 1 (res L44-50) | none | PASS |
| Results: auditor paragraphs | 8 | 8 (res L90-115, L369-394) | none | PASS |
| Results: entities | 4 | 4 | none | PASS |
| Results: structured IDs | 780 | 780 | none | PASS |
| Concall: turns | 167 | 167 (speaker-label regex) | none | PASS |
| Concall: participants | 8 | 8 | none | PASS |
| Concall: questions | 67 | 67 (77 analyst turns less 8 acknowledgements T37/64/89/113/117/134/140/163 and 2 audibility checks T13/T67) | none | PASS |
| Concall: management numbers | 106 | 106 (every management digit line maps to R002-R104; words-numbers map to R009, R040, R042, R044, R071, R094 and M001-M006) | none | PASS |
| Concall: forward statements | 61 | 61. Every management lexicon hit maps to an A1 FORWARD/QUALIFIER row or M007-M020, or is non-forward (thanks, hand-over, descriptive billing flow, "would be" estimates). L562-564 ("It will be break-even only ... This is our initial target") sits under QUALIFIER R236, so it is in the ledger | none | PASS |
| Concall: hedge counts (6C) | 6 protocol / 11 other | 6 / 11 (we believe L137, L196; expect L437, L471; hope L411, L1095; I think x5; maybe x4; assuming L403; presuming L698) | none | PASS |
| Concall: structured IDs | 246 | 246 | none | PASS |
| Presentation: slides | 32 | 32 page markers | none | PASS |
| Presentation: numbers | 445 | 445 (slide tally: cover 1, S5 12, S6 1, S7 3, S8 19, S9 8, S10 20, S13 28, S14 112, S16 8, S17 6, S18 3, S20 1, S23 1, S24 8, S26 4, S27 22, S28 4, S29 68, S30 116) | none at ID level; see finding M1 for six S30 rows marked reviewed whose content A4 did not use | PASS (A2) / see M1 (A4) |
| Presentation: structured IDs | 553 | 553 | none | PASS |

Missing from ledger (fresh-pass units the ledger lacks): none. A2 is clean.

Orphan rows: none at ID level. A4 marks all 780 + 246 + 553 IDs reviewed (rev L58) and disposes every A2-flagged row individually (rev L64-108), with one small gap in the flagged-row list (style note S2). The blanket "reviewed" mark is contradicted for six presentation rows that carry an unused finding (M1 below).

---

## 2. ARITHMETIC AUDIT

Every derived figure in A4's tables was recomputed from raw lakhs. Selected rows below; every other derived cell I checked also ties.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Standalone op EBITDA Q2 FY27 / margin | 15.16 / 18.53% | 1,516.12 / 18.528% | res L189-201 | PASS |
| Standalone op EBITDA Q2 FY26 / margin | 14.45 / 20.72% | 1,444.62 / 20.718% | res L189-201 | PASS |
| Standalone op EBITDA H1 FY27, H1 FY26, FY26 | 25.49 / 19.43 / 34.93 | 2,548.99 / 1,943.23 / 3,492.68 | res L189-201 | PASS |
| Consolidated op EBITDA Q1, Q2, H1, FY26 / margins | 12.71, 19.96, 32.67, 37.25 / 17.23, 18.79, 18.15, 14.99% | 1,271.13, 1,995.59, 3,266.72, 3,725.35 / 17.231, 18.791, 18.152, 14.993% | res L469-481 | PASS |
| ETR standalone Q2 FY27 / H1 FY27 / FY26 | 26.35 / 27.56 / 27.09% | 386.92/1,468.60; 691.15/2,508.02; 991.42/3,659.15 | res L201-205 | PASS |
| ETR consolidated Q1 / Q2 / H1 | 28.50 / 26.04 / 27.02% | 364.15/1,277.90; 504.84/1,938.38; 868.99/3,216.28 | res L481-485 | PASS |
| Gross margin standalone Q2 FY27 / Q2 FY26 / Q1 FY26 | 38.64 / 38.54 / 49.23% | 1-5,020.98/8,182.82; 1-4,285.72/6,972.71; 1-1,689.93/3,328.59 | res L189, L193-195 | PASS |
| Q2 material-plus-conversion spread | 21.89% vs 23.56% (-167 bps) | 1-6,391.89/8,182.82; 1-5,330.24/6,972.71 | res L189, L193-195, L199 | PASS |
| Standalone Q2 YoY: revenue / core PBT / PAT | +17.4 / +7.4 / +15.2% | 1.17355 / 1.07415 / 1.15210 | res L189-206 | PASS |
| Standalone H1 YoY: revenue / core PBT / PAT | +37.5 / +40.8 / +45.8% | 1.37464 / 1.40849 / 1.45765 | res L189-206 | PASS |
| Mgmt headline Q2 rev / H1 rev / H1 PAT (before, after associate) | +52.3 / +74.7 / +88.3, +87.1% | 10,619.84/6,972.71; 17,997.04/10,301.30; 2,347.29 and 2,331.76 / 1,246.44 | res L469, L486, L488, L189, L206 | PASS |
| OI share of Q2 PBT gain | 51% | 98.98 / 192.76 = 51.3% | res L190, L201 | PASS |
| OI from interest + MF + PPE gain, standalone / consolidated | 92.0% / 89.1% | 250.63/272.53; 250.63/281.44 | res L237, L238, L243, L190, L470 | PASS |
| Q2 PAT bridge | +2.51, -1.79, +0.24, -0.02, +0.99, -0.51, +0.01 = +1.43 | 250.71, -179.21, 23.82, -1.54, 98.98, -50.91, 0.95 = 142.80 lakh | res L189-206 | PASS |
| H1 PAT bridge | +7.28, -1.22, +0.41, +0.02, +1.69, -2.15, -0.32 = +5.70 | 728.03, -122.28, 40.86, 1.71, 169.28, -214.73, -32.45 = 570.43 lakh | res L189-206 | PASS |
| Consolidated vs standalone PAT gap FY26 / Q1 / Q2 / H1 | 6.4 / 24.3 / 32.5 / 29.2% | 2,838.66/2,667.73; 913.75/735.19; 1,433.54/1,081.68; 2,347.29/1,816.87 | res L486, L206 | PASS |
| Kidcity C-S H1 revenue / op EBITDA / PAT / PAT margin | 38.36 / 7.18 / 5.30 / 13.8% | 3,836.44 / 717.73 / 530.42 / 13.83% | res L469-486, L189-206 | PASS |
| NCI tie-out H1 / FY26 | 530.40 vs 530.42; 170.92 vs 170.93 | 132.60/0.25; 42.73/0.25 | res L499 | PASS |
| Kidcity consideration route A / route B | 367.42 / 367.43 lakh | 2,552.91-2,169.96-15.53; (160.53-42.73)/0.25 x 0.75 + 14.03 | res L140, L420, L487, L439, L499, L418 | PASS |
| Price / TTM PAT; price / book; price / first half annualised | 0.70x / 1.04x / 1.43x | 489.89/701.35; 367.42/353.40; 489.89/341.86 | res L486, L206 | PASS |
| Kidcity H1 CFO / CFO-to-PAT | 0.47 Cr / 0.09x | -440.63 - (-487.90) = 47.27; 47.27/530.42 | res L553, L259 | PASS (see M2 for the qualifier) |
| Kidcity receivables / days; inventory; borrowings | 35.40 / ~168; 3.96; 4.61 | 3,540.14 / 168.4; 395.72; 460.66 | res L427, L147, L425, L145, L444, L449, L163, L168 | PASS |
| Kidcity purchases Q2 / H1; ex-intra-group YoY Q2 / H1 | 13.37 / 26.68; +5.8 / +21.9% | 1,337.35 / 2,668.10; 7,380.41/6,972.71; 12,559.74/10,301.30 | res L474, L194, L189 | PASS |
| CFO/PAT standalone H1 FY27 / H1 FY26; consolidated H1 FY27 | -0.27x / 1.48x; -0.19x | -487.90/1,816.87; 1,846.18/1,246.44; -440.63/2,331.76 | res L259, L206, L553, L488 | PASS |
| Standalone receivable / inventory / payable days; CCC | 109.7 to 141.7; 129.5 to 121.0; 41.9 to 64.0; 197.3 to 198.7 | 109.70, 141.66; 129.54, 121.00; 41.90, 63.99; 197.34, 198.67 | res L145, L147, L170-171, L189, L193-195 | PASS |
| Consolidated CCC, as computed / scope-matched | 182.2 to 159.5; 151.9 to 159.5 (+7.6) | 182.24, 159.47; 110.00 + 100.67 - 58.77 = 151.90 | res L425, L427, L451-452, L469, L473-475 | PASS |
| Net debt standalone / consolidated; ND/E | 70.40 to 78.61; 75.23 to 83.17; 0.74x to 0.63x; 0.75x to 0.62x; 0.77x corrected | 7,039.64, 7,860.78; 7,523.47, 8,317.33; 0.740, 0.626; 0.753, 0.623; 7,523.47/9,802.30 = 0.768 | res L148, L159, L163, L168, L428, L440, L444, L449 | PASS |
| FY26 consolidated ROCE / ex-OI / corrected; H1 annualised | 25.2 / 20.3 / 25.5%; 35.7 / 32.8% | 4,428.20/17,548.42; 3,559.25/17,548.42; 4,428.20/17,354.83; 7,009.54/19,628.5 | res L481, L477, L470, L440, L444, L449 | PASS |
| FVOCI tie-out (investments, DTA, Other Equity) | 2,243.04; 28.42; 193.59 lakh | 2,359.43 + 251.03 - 367.42; 85.16 - 57.43 + 0.69; 3,635.61 - 3,442.02 | res L140, L142, L208-209, L420, L422, L437, L507, L494 | PASS |
| Elementa loss annualised / share of cost / 100% | 0.82 Cr / 41% / 2.05 Cr | 15.53 x 365/69 = 82.15 lakh; /200; /0.40 | res L487, L346-348 | PASS |
| Implied H2 FY27 standalone / group | 127.53-138.74 (+5.2 to +14.4%); 143.05-155.48 (-1.7 to +6.9%) | 269.14-280.35 less 141.61; 323.02-335.45 less 179.97 | res L189, L469; cc L189, L821 | PASS |
| Component-guide FY28 CAGR | 42.3 to 48.8% | sqrt(502.97/248.48), sqrt(550.44/248.48) | cc L403-412, L821 | PASS |
| Specificity | 25/61 = 0.41 | 0.410; 24/59 = 0.407; 24/49 = 0.490 | ledger 5, 5b | PASS |
| Q&A grade tally | A22 B28 C14 D2 E0 n/a1 = 67 | recounted row by row: same | rev L848-914 | PASS |
| EPS-implied weighted shares; diluted shares; max dilution | 285.4 / 205.3 / 416.2 lakh; ~647; 6.40% | 938.88/3.29; 1,246.44/6.07; 2,667.73/6.41; 1,300.39/2.01; 39.6686/619.975 | res L206, L217, L498, L510, L308 | PASS |
| Q1 FY27 NCI mis-statement | 0.30 Cr; equals 25% of Kidcity Q1 tax | 0.25 x 178.56 - 14.98 = 29.66; 0.25 x 59.92 = 14.98 | res L483-486, L499, L203-206 | PASS |
| Market CAGR 2025-2034 | ~5.1% | (17.4/11.1)^(1/9) = 1.0512 | ppt R037-R038 | PASS |

DTA term check: A4's "Kidcity 0.69" is in lakhs. The Sep-26 C-S DTA is 63.75 - 62.90 = 0.85 lakh (res L422, L142). Kidcity's H1 deferred tax is a 0.16 lakh credit (res L484 15.99 vs L204 16.15). So Kidcity's Mar-26 DTA = 0.85 - 0.16 = 0.69 lakh. It ties.

Arithmetic mismatches above rounding: none.

---

## 3. ADVERSARIAL READ

A4's review is bear-leaning overall. The three most positive claims it makes are these.

### Claim 1. Kidcity delivered its margin, and Karnika bought it cheaply (1-K2, 6A-M, 7A, Brief part 3)
A4 says Kidcity's H1 PAT margin of 13.8% is "CONFIRMED on the reported accrual split" (rev L1062), and that Karnika's 75% share of Kidcity's TTM PAT (Rs 5.26 Cr) is "more than the price paid" (rev L281).

Mandatory acquisition-economics probe (Kidcity):
- Price: about Rs 3.67 Cr for 75% (derived two ways; ties to 0.01 lakh). Implied 100% value Rs 4.90 Cr.
- Multiple: ~Rs 4.90 Cr / Kidcity TTM PAT Rs 7.01 Cr = ~0.70x earnings. On the first post-deal half annualised (Rs 3.42 Cr) it is ~1.43x. On deal-date book it is ~1.04x.
- Quality markers from the extract: TTM PAT over deal-date net assets (Rs 4.71 Cr) is about 149%. Debt Rs 4.61 Cr at Sep-26, about equal to deal-date book. Cash Rs 0.04 Cr. One concentrated customer link (Hopscotch, sole aggregator, cc L308-311).
- Why is a 149%-ROE asset priced under 1x earnings? The earnings that make it cheap appeared after the deal, on goods Karnika makes (cc L425). A4 already carries this bear reading (transfer prices, 25% NCI leakage, 0.09x cash conversion).

Strongest bear counter from the same extract, not yet in A4:
- Kidcity's +Rs 0.47 Cr H1 CFO is itself propped up. It includes a +Rs 5.74 Cr rise in trade payables [res L546 2,007.01 less L252 1,432.71] and a +Rs 3.43 Cr inventory release [res L541 (399.76) less L247 (742.32)]. Without these two items, Kidcity's H1 CFO is about -Rs 8.70 Cr. Without the payables rise alone, it is about -Rs 5.27 Cr.
- Kidcity's trade payables are at least Rs 23.51 Cr at 30-Sep-2026 [(347.55 + 5,074.77) less (347.55 + 2,723.35) lakh; res L451-452, L170-171]. They were Rs 17.49 Cr at Mar-26. That is about 161 days of annualised H1 purchases [2,351.42 / (2,668.10 x 2) x 365]. A4's 5-K table lists Kidcity receivables, inventory, borrowings and cash, but not payables.
- Kidcity buys finished goods only (C-S materials consumed = 0, res L473 vs L193) and gets 60% of them from Karnika (cc L425). So part of these payables is likely owed to Karnika [INFERENCE; size ND]. Any such amount sits inside Karnika's standalone receivables of Rs 109.91 Cr (res L147), whether or not the group eliminates on consolidation.
- Survives: yes. It is supported by filed lines. It must be grafted (finding M2).

Observation, no change needed: the FY26 C-S "other expenses" line is negative (consolidated 3,853.31 at res L479 vs standalone 3,927.42 at res L199, so -74.11 lakh). The FY26 Kidcity column therefore carries an elimination. A4 already labels 1-K "includes any eliminations". This supports A4's assumption-3 caveat (style note S6).

Other stake buys in the document (probe applied):
- Elementa Lifespaces: Rs 2.00 Cr for 40%, subscribed at face value (res L343-348). The target is loss-making, so price/PAT is not meaningful. The group's share of loss annualises to about Rs 0.82 Cr a year, 41% of the cost (res L487). Business and related-party status are ND. A4 carries this in Q6. No new counter.
- RDB Elementa: Rs 5.20 lakh for 26%, unpaid, not allotted (res L337-342). Immaterial. A4 carries it in Q7.

### Claim 2. H1 standalone growth ex intra-group (~+21.9%) sits inside the 20-25% guide (2-X, diagnostic 1, 6A-M, T4)
- Strongest bear counter: the latest quarter ex intra-group is about +5.8% (2-X), and H1 rides a weak Q1 FY26 base (Q1 FY26 Rs 33.29 Cr; Q1 FY27 +79.6%).
- Survives: yes, but A4 already states both points (rev L312, L329, L361, L375). No graft needed.
- While testing this claim, I found a factual error in A4's Step 3 base reading for H2 (finding F1).

### Claim 3. Leverage fell, and management's 0.6x D/E is confirmed (5-S, 5-C, 7A)
- Strongest bear counter: the ratio fell because of warrant money (Rs 12.00 Cr) and profit, not lower debt. Standalone net debt rose Rs 8.21 Cr in H1.
- Survives: yes, but A4 already states it (rev L485, L530, L837). No graft needed.

---

## 4. FINDINGS (tagged)

### F1. FACTUAL. Loop to A4.
Where: Step 3 diagnostics, "Implied next-half base" (rev L419).
A4 text: "The H2 FY26 base already holds about one quarter of Kidcity supply (from 04-Oct-2025)".
Extract:
- Kidcity joined on 04-Oct-2025 (res L318), the first week of H2 FY26. H2 FY26 is therefore a full post-deal half. A4's own 1-K2 calls H2 FY26 Kidcity's "first post-deal half" (rev L279, L288), so the review contradicts itself.
- Kidcity's H2 FY26 purchases of stock-in-trade were Rs 27.25 Cr [consolidated FY26 5,440.27 (res L474) less standalone FY26 2,715.64 (res L194) lakh]. That is above its H1 FY27 purchases of Rs 26.68 Cr (2-X).
- At the CFO's 60% (cc L425), the method A4 uses in 2-X, H2 FY26 standalone revenue holds about Rs 16.35 Cr of sales to Kidcity [INFERENCE]. That is a full half, about the same size as H1 FY27 (Rs 16.01 Cr).
Effect: H2 FY27 vs H2 FY26 standalone growth is roughly like-for-like on intra-group sales. FY26 standalone revenue (Rs 224.28 Cr), the base for the 20-25% guide test (T4, M8), already carries about one half-year of intra-group sales. A4's sentence implies the opposite.
Fix (A4): replace the sentence with: "Kidcity joined on 04-Oct-2025, so H2 FY26 is a full post-deal half. Kidcity's H2 FY26 purchases were Rs 27.25 Cr [res L474 less L194, FY26 column], about the same as H1 FY27 (Rs 26.68 Cr). At the CFO's 60% that is about Rs 16.35 Cr of sales to Kidcity in the H2 FY26 base [INFERENCE]. So H2 FY27 vs H2 FY26 is roughly like-for-like on intra-group sales. FY26 standalone revenue, the base of the 20-25% guide, already carries about one half-year of them." Carry one clause into M8 / T4 ("FY26 base holds about one half-year of intra-group sales").

### M1. MISSING. Loop to A4.
Where: Q8 (rev L682), Top-3 rationale (rev L716), Brief line 11 (rev L1223), CONSOLIDATION ERRORS flag (rev L1362), M16 (rev L1197); also the Mar-26 equity basis in 5-C (rev L508) and Step 7 (rev L635).
Gap: the company's own deck FY26 consolidated balance sheet carries the FVOCI-adjusted figures on every affected line. It does not match the filing's Mar-26 comparative column. A4 never uses these deck rows, though it marks them reviewed.

| Line | Filing Mar-26 comparative | A4 corrected (Q8 method) | Deck FY26 |
|---|---|---|---|
| Other Equity / Reserves | 36.36 (res L437) | 34.42 | 34 (ppt R337, l582) |
| Total equity | 99.96 (res L440) | 98.02 | 98 (ppt R345, l584) |
| Non-current investments | 22.43 (res L420) | 19.92 | 20 (ppt R401, l584) |
| Deferred tax asset | 0.28 (res L422) | 0.86 | 1 (ppt R405, l585) |
| Total non-current assets | 31.38 (res L423) | 29.44 | 29 (ppt R413, l587) |
| Total assets | 216.87 (res L433) | 214.94 | 215 (ppt R445, l596) |

The deck's FY26 ROCE of 25.5% (ppt R063, l219; series by position) also matches A4's corrected 25.5%, not the 25.2% filing basis.
Effect: this MGMT-tier evidence favours Q8's bull fork. The omission most likely sits only in the comparative column of this H1 filing, which the limited review passed. It makes Q8's bear fork ("the FY26 FVOCI loss is missing from the audited consolidated accounts") unlikely. A bear claim carries the same evidence bar as a bull claim, so this must be stated.
Fix (A4): (a) In Q8, add: "The deck's FY26 balance sheet (ppt R337, R345, R401, R405, R413, R445) already carries the corrected figures: Reserves 34, total equity 98, investments 20, DTA 1, total assets 215. The error therefore most likely sits in the comparative column of this filing only." Then narrow the bear fork to "the AR differs from the deck". (b) Reword the Top-3 rationale to "tests the H1 filing's consolidation close and the limited review that passed it". (c) Brief line 11 and the flag: say "the Mar-26 comparative column in this filing", and add "the deck carries the corrected figures". (d) In 5-C and Step 7, make 98.02 the primary Mar-26 equity (ND/E 0.77x, ROCE 25.5%) and show 99.96 as the filing-column figure. Q8 can stay in the Top 3 or drop from it. That is A4's call; state the reason.

### M2. MISSING. Loop to A4. This is the surviving bear counter from Claim 1.
Where: 1-K2 cash bullet (rev L291), 1-K2 table rows (rev L283-284), 5-K (rev L511-522), 6A-M Kidcity row (rev L586), 7A Kidcity rows (rev L1062), Step 8C and the Forward Map make-or-break line (rev L662-665, L1260), Brief part 3 (rev L1245), KIDCITY CASH flag (rev L1361), Q15 or Q2.
Gap: A4 reports Kidcity's H1 CFO as +Rs 0.47 Cr (0.09x PAT) but does not show what supports it. It also omits Kidcity's payables and the intra-group receivable inside Karnika's standalone debtors.
Extract:
- Kidcity C-S operating cash flow components for H1: receivables -14.85; payables +5.74 (res L546 less L252); inventories +3.43 (res L541 less L247); other +0.67. Total working capital -5.01 (ties to res L549 less L255).
- CFO without the payables rise and the inventory release: about -Rs 8.70 Cr [47.27 - 574.30 - 342.56 lakh].
- Kidcity trade payables at least Rs 23.51 Cr at Sep-26, up from Rs 17.49 Cr at Mar-26 (res L451-452 less L170-171). That is about 161 days of annualised H1 purchases. This is a floor, because intra-group payables eliminate if the group eliminates.
- 60% of Kidcity's goods come from Karnika (cc L425). Part of Kidcity's payables is likely owed to Karnika [INFERENCE; size ND]. Standalone statements never eliminate, so any such amount is inside Karnika's Rs 109.91 Cr standalone receivables (res L147). That is the base of A4's single cleanest metric.
Fix (A4):
- (a) Add a 5-K row: "Trade payables, at least 23.51 (Mar-26: 17.49); about 161 days of annualised H1 purchases; floor, because intra-group balances eliminate."
- (b) Restate the 1-K2 cash bullet, 5-K CFO row, 6A-M, 7A and Brief part 3 as: "Kidcity H1 CFO +Rs 0.47 Cr came after a Rs 5.74 Cr payables rise and a Rs 3.43 Cr inventory release. Without them it was about -Rs 8.70 Cr."
- (c) In 8C and the Forward Map make-or-break line, add: "Standalone receivables include any amount Kidcity owes Karnika (ND). Group credit terms can move this metric. Read it with consolidated scope-matched receivable days."
- (d) Extend Q15 (or Q2) to ask: "What did Kidcity owe Karnika at 30-Sep-2026, in Rs Cr?"
- (e) Update the KIDCITY CASH flag to match.

No other FACTUAL, MISSING or CONTRADICTION findings.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**. No A2 or A3 rework is needed. The ledgers are complete, and every fix uses filed lines A4 already cites or can cite directly.
- F1 (FACTUAL): Step 3 (rev L419) says H2 FY26 holds "about one quarter" of Kidcity supply. The filing shows a full post-deal half: Kidcity H2 FY26 purchases were Rs 27.25 Cr, res L474 less L194.
- M1 (MISSING): Q8, the Top-3 rationale, Brief line 11 and the flag omit that the deck's FY26 balance sheet carries the FVOCI-corrected figures (ppt R337, R345, R401, R405, R413, R445).
- M2 (MISSING): the Kidcity cash test omits that the +Rs 0.47 Cr H1 CFO rests on a Rs 5.74 Cr payables rise and a Rs 3.43 Cr inventory release (about -Rs 8.70 Cr without them). It also omits Kidcity payables of at least Rs 23.51 Cr and the intra-group receivable inside the 8C metric.

None of the three changes the protocol verdict (PROCEED WITH FLAGS) or the cash class (INDETERMINATE-WITH-DIRECTION). Each changes a stated fact or a material qualifier, so none is STYLE. All three are local text edits with exact replacement text given above.

---

## STYLE NOTES (logged; no re-run)

- S1. Q34 (rev L708) calls Rs 146 Cr "working capital". It is receivables 88 plus inventory 58 (ppt R421, R417). Net of payables 34 (ppt R369) it is Rs 112 Cr (filed 111.83, 5-C). Change the label.
- S2. The Loop 2 list of A2-flagged presentation rows (rev L101-108) leaves out R224-R231 (SERIES_BY_POSITION, 2028 slide), R516/R518/R543/R544 (HEADER_LABEL_MISMATCH) and R549 (NO_2028_VALUE_IN_TEXT). They are covered in substance by Q19 (P-A3-06) and the Step 3 diagnostic (P-A3-12). Add one disposition line each.
- S3. Distribution-partner counts are not reconciled across documents: 500-plus (cc L132), 540+ distributors (ppt R015, l133), and 150+ distribution partners on the export slide (ppt R220, l356). No conclusion depends on them.
- S4. 6B does not count relative-date forward rows R167 ("next half"), R168 ("quarter third or quarter four") and R169 ("following quarter") as quantified. Counting them gives 27/61 = 0.44, the same band. State the choice.
- S5. Q4 (rev L678) gives Kidcity staff cost as "about 1%"; 1-K2 gives 1.27%. Use one figure.
- S6. 1-K FY26 column: C-S other expenses are negative (-0.74 Cr; res L479 vs L199), so C-S operating EBITDA (2.33) exceeds C-S gross profit (1.95) in H2 FY26. A one-line footnote would show that the FY26 column carries an elimination. A4's "includes any eliminations" label already covers it.

---

```yaml
stage: A5-adversary
company: "KARNIKA"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Kidcity delivered a 13.8% H1 PAT margin and was bought at ~0.70x TTM PAT; its H1 profit converted 0.09x to cash (+Rs 0.47 Cr CFO)", counter: "The +Rs 0.47 Cr CFO rests on a Rs 5.74 Cr payables rise and a Rs 3.43 Cr inventory release; without them Kidcity H1 CFO is about -Rs 8.70 Cr. Kidcity payables are at least Rs 23.51 Cr (~161 days of purchases); with 60% of goods from Karnika, part is likely owed to Karnika and sits in Karnika's Rs 109.91 Cr standalone receivables (size ND)", source_line: "res L546, L252, L541, L247, L451-452, L170-171, L147; cc L425", type: MISSING}
findings_by_type:
  factual:
    - "F1: Step 3 (rev L419) says the H2 FY26 base holds 'about one quarter' of Kidcity supply. Kidcity joined 04-Oct-2025 (res L318), so H2 FY26 is a full post-deal half, and its H2 FY26 purchases were Rs 27.25 Cr (res L474 5,440.27 less L194 2,715.64, FY26) vs Rs 26.68 Cr in H1 FY27. At 60%, about Rs 16.35 Cr of sales to Kidcity sit in the H2 FY26 base [INFERENCE]. The sentence also contradicts 1-K2's 'first post-deal half'"
  missing:
    - "M1: Q8, Top-3 rationale, Brief line 11, CONSOLIDATION ERRORS flag, M16: the deck FY26 balance sheet (ppt R337 34, R345 98, R401 20, R405 1, R413 29, R445 215) carries the FVOCI-corrected figures (34.42, 98.02, 19.92, 0.86, 29.44, 214.94), not the filing's Mar-26 comparative column (36.36, 99.96, 22.43, 0.28, 31.38, 216.87). This favours Q8's bull fork: the error is most likely confined to this H1 filing's comparative column"
    - "M2: Kidcity cash test (1-K2, 5-K, 6A-M, 7A, 8C, Forward Map, Brief part 3, flag) omits that the +Rs 0.47 Cr H1 CFO includes a +Rs 5.74 Cr payables rise and a +Rs 3.43 Cr inventory release (about -Rs 8.70 Cr without them), omits Kidcity payables of at least Rs 23.51 Cr (~161 days), and omits that any Kidcity debt to Karnika sits in the standalone receivables behind the 8C metric"
  contradiction: []
  style:
    - "S1: Q34 labels Rs 146 Cr (receivables 88 + inventory 58) as working capital; net is ~Rs 112 Cr"
    - "S2: A2-flagged presentation disposition list omits R224-R231, R516/R518/R543/R544, R549 (covered in substance by Q19 and Step 3)"
    - "S3: distribution-partner counts unreconciled: 500-plus (cc L132), 540+ (ppt R015), 150+ (ppt R220)"
    - "S4: 6B excludes relative-date rows R167-R169 from quantified; including them gives 27/61 = 0.44, same band"
    - "S5: Kidcity staff cost 'about 1%' in Q4 vs 1.27% in 1-K2"
    - "S6: 1-K FY26 column carries an elimination (C-S other expenses -0.74 Cr, res L479 vs L199); add a footnote"
loop_back_to: "A4"
gap: "A4 only, no A2/A3 rework. (F1, FACTUAL) Step 3 rev L419: replace 'about one quarter of Kidcity supply' with a full post-deal half; Kidcity H2 FY26 purchases Rs 27.25 Cr (res L474 less L194) vs H1 FY27 Rs 26.68 Cr; carry into M8/T4. (M1, MISSING) Q8, Top-3 rationale, Brief line 11, flag, M16: add that the deck FY26 balance sheet (ppt R337, R345, R401, R405, R413, R445) carries the FVOCI-corrected figures, narrow the bear fork, use 98.02 as the primary Mar-26 equity. (M2, MISSING) Kidcity cash: add the payables row (at least Rs 23.51 Cr, ~161 days) to 5-K; restate the CFO as +0.47 after a 5.74 payables rise and a 3.43 inventory release (about -8.70 without them); add the intra-group receivable qualifier to 8C and the Forward Map; extend Q15 or Q2. Exact replacement text is in the audit file, section 4."
style_notes:
  - "S1: Q34 'working capital' Rs 146 Cr is gross (receivables + inventory)"
  - "S2: complete the A2-flagged presentation disposition list (R224-R231, R516/R518/R543/R544, R549)"
  - "S3: distribution-partner counts differ across documents"
  - "S4: state the 6B choice on relative-date rows"
  - "S5: one figure for Kidcity staff-cost share"
  - "S6: footnote the FY26 C-S elimination in 1-K"
analyst_note: "Fresh enumeration matches all three ledgers (167 turns, 67 questions, 106 management numbers, 61 forward rows, 32 slides, 445 deck numbers, 210 result lines); A2 is clean. Every derived metric ties to the lakh. The three gaps are content, not arithmetic. F1: H2 FY26 already holds a full half of sales to Kidcity, so the FY26 base of the 20-25% guide is not intra-group-free. M1: the deck's FY26 balance sheet carries the FVOCI-corrected figures on all six affected lines. That weakens Q8's bear fork (audited accounts omit the loss) and points to a comparative-column error in this filing. M2: Kidcity's positive CFO rests on payables and inventory release. Its payables of at least Rs 23.51 Cr, with 60% of goods from Karnika, make the standalone receivable-days metric partly a group credit-terms number. None of the three changes PROCEED WITH FLAGS or the cash class. All three are local A4 edits with exact text in the audit file."
```
