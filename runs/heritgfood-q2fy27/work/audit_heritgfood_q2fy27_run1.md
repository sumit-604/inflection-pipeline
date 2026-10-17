# A5 ADVERSARY / COMPLETENESS AUDIT: Heritage Foods Limited (HERITGFOOD) | Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-17
Under audit: runs/heritgfood-q2fy27/work/review_heritgfood_q2fy27.md (890 lines)
Inputs read: A1 fulltexts (results 782 lines, presentation 1,328, press release 230), A1 structured files (results R001-R1242, presentation R001-R651, press release R001-R180), A2 ledgers (all three), A4 review.
Not read: source PDFs, anything under inputs/, A3 forensics. Disclosure: one Grep over work/*.md for slide 9 values returned two lines of work/forensics_presentation_heritgfood_q2fy27.md as incidental matches (lines 29 and 120). They were not opened and not relied on; the slide 9 reading below is derived from the fulltext alone.

Anchor key: L### = results fulltext; P-l### = presentation fulltext; PR-L### = press release fulltext; R-L### = A4 review line; R### = A1 structured row. Rs Cr unless marked Rs m.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PLAIN-LANGUAGE BRIEF at R-L746-804.

| Part | Location | Status | Note |
|---|---|---|---|
| (1) Summary narrative | R-L750-766 | PRESENT | 15 lines, within 10-20; real content |
| (2) Sector intelligence | R-L768-775 | PRESENT | Cost cycle, season, structure, policy, payer mix. Contains factual error F3 (CY25 vs CY30P) |
| (3) Business-model intelligence | R-L777-783 | PRESENT | Earnings model, margin engine, model drift, undisclosed items |
| (4) Competition intelligence | R-L785-791 | PRESENT | States that the corpus names no peers; peer set labelled [INFERENCE]. Contains F4 |
| (5) Forward map | R-L793-804 | PRESENT | 6 catalysts, each with a bull and a bear fork; 4 dated, 2 honestly "date ND" |

Gate result: PASS. All five parts are present and non-empty.

---

## 1. COVERAGE AUDIT

Fresh pass over the three A1 FULLTEXTS (grep and positional count), diffed against the A2 ledgers.

### 1A. Counts

| Doc | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Numbered notes (incl. CF note 1) | 12 | 12 (L275, 287, 289, 293, 296, 299; L620, 633, 635, 639, 642, 645) | none | PASS |
| Results | Statement line items | 299 | 299 (S P&L 25, S seg 21, S BS 44, S CF 53, C P&L 33, C seg 26, C BS 44, C CF 53) | none | PASS |
| Results | Statement NUMBER cells | 1,114 | 1,114 (line items x period columns; two single-cell "other equity" lines) | none | PASS |
| Results | Dash / zero cells | 60 | 60 (S P&L 14, S CF 6, C P&L 24, C seg 4, C BS 1, C CF 11) | none | PASS |
| Results | Entities | 28 | 28 named; SEBI and ICAI appear only inside auditor boilerplate (L326, L347, L695, L702), carried in R1211/R1230/R1231 | none | PASS |
| Results | Dates | 23 | 23 | none | PASS |
| Results | Agenda items | 0 | 2 (L38 results, L41 limited review report) | none: carried as R1193/R1172 (L38) and R1148 (L41) | PASS (S3: category label only) |
| Results | Auditor paragraphs | section | 9 (standalone 4: L331, 337, 345, 364; consolidated 5: L677, 685, 693, 713, 721) | none | PASS |
| Results | Forward statements | 0 | 0 | none | PASS |
| Presentation | Slides | 45 | 45 ([page 1] to [page 45]) | none | PASS |
| Presentation | Table cells, slides 8 / 42 / 43 | 242 | 245 printed cells (slide 8: 107; slide 42: 48; slide 43: 90) | none | PASS with STYLE S4: 3 dash cells on slide 8 not carried (P-l242 H1FY27; P-l245 Q1FY27 and H1FY27); filing confirms nil (L421, L423) |
| Presentation | Zero-standing | 11 | 14 (the same 3 dash cells) | none | STYLE S4 |
| Presentation | Forward statements | 15 | 15 | none | PASS |
| Presentation | Footnotes / fine print | 23 | 23 | none | PASS |
| Presentation | Chart / slide numbers | 535 | Spot-checked slides 5, 6, 8, 9, 16, 17, 18, 21, 23, 29, 36, 42, 43, 44: complete, except number-word claims "Zero Milk Holiday" (P-l600-601) and "No Milk holiday since inception" (P-l665-667) | none | STYLE S5 (A4 cites both from fulltext; nothing lost) |
| Press release | Pages | 5 | 5 | none | PASS |
| Press release | Numbers | 117 | 117 (line-by-line recount PR-L23 to PR-L224) | none | PASS |
| Press release | Entities / forward / dates / qualifiers | 27 / 8 / 12 / 13 | 27 / 8 / 12 / 13 | none | PASS |

### 1B. Ledger-to-review orphan check

A4 marks every ledger row reviewed, with ranges (R-L18): results R001-R1242, presentation 45 slide rows plus R001-R651, release R001-R180. I spot-checked material rows for real treatment, not only the blanket line: note 4a/4b (R1209/R1210 -> R-L117-118), note 5 (R1229 -> R-L124), unreviewed subsidiary (R1131-R1138, R1168, R1233 -> R-L142, R-L145), Annexure entities (R1164-R1167 -> R-L160), board and signature timing (R1117/R1118, R1184/R1191 -> R-L143), name change (R1155 -> Q13), deck 0.33 (R244 -> Q20), CY30P projection (R598 -> R-L772, misread, see F3), release Top 5 / 71% (R101/R102 -> R-L160), procurement LLPD (R063-R066 -> R-L342).

Result: orphan rows: none. Missing from ledger (material): none. Non-material uncaptured units are logged as STYLE S3-S6, no loop.

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4's tables was recomputed from the Rs m source lines. The table shows the load-bearing set plus every mismatch. Rows marked PASS recompute to within 0.01 Cr / 1 bp.

| Metric | A4 value (R-L) | Recomputed | Source line | Status |
|---|---|---|---|---|
| C Op EBITDA Q2 FY27 / Q2 FY26 / Q1 FY27 | 73.97 / 77.19 / 61.86 (R-L207) | 739.67 / 771.88 / 618.63 m | L420+L416+L415-L408 | PASS |
| C Op EBITDA FY26 / H1 FY26 / H1 FY27 | 266.27 / 151.08 / 135.83 | 2,662.70 / 1,510.75 / 1,358.29 m | same | PASS |
| C Op EBITDA margin, 6 periods | 6.94 / 4.62 / 5.61 / 5.88 / 6.72 / 5.11% | 6.938 / 4.623 / 5.605 / 5.883 / 6.717 / 5.111% | / L407 | PASS |
| C core PBT Q2 FY27 / Q2 FY26 | 39.23 / 53.24 | 392.33 / 532.38 m | L420-L408 | PASS |
| C ETR Q2 FY27 / Q2 FY26 / H1 FY27 | 27.56 / 24.74 / 26.69% | 117.42/425.99; 167.65/677.60; 203.20/761.46 | L426-427 / L424 | PASS |
| C gross margin Q2 FY27 / Q2 FY26 / Q1 FY27 / FY26 | 21.84 / 24.54 / 21.20 / 23.44% | 2,881.38/13,195.80; 2,730.61/11,125.17; 2,837.38/13,380.94; 10,607.13/45,259.91 | L407, L411-413 | PASS |
| S Op EBITDA Q2 FY27 / Q2 FY26 / Q1 FY27 | 71.12 / 71.88 / 59.40 | 711.17 / 718.78 / 594.02 m | L88+L84+L83-L76 | PASS |
| S ETR Q2 FY27 / Q1 FY27 | 26.39 / 24.59% | 109.38/414.53; 80.75/328.45 | L92-93 / L90 | PASS |
| YoY revenue C / S | +18.61 / +16.78% | 13,195.80/11,125.17; 12,733.76/10,904.14 | L407, L75 | PASS |
| YoY Op EBITDA C / S | -4.17 / -1.06% | 739.67/771.88; 711.17/718.78 | derived | PASS |
| YoY core PBT C / S | -26.31 / -22.76% | 392.33/532.38; 380.39/492.47 | derived | PASS |
| YoY PAT C / owners / S | -39.49 / -38.60 / -36.96% | 308.57/509.95; 313.63/510.81; 305.15/484.04 | L428, L436, L94 | PASS |
| D&A / finance cost YoY (C) | +36.61 / +89.12% | 274.70/201.09; 72.64/38.41 | L416, L415 | PASS |
| QoQ C Op margin / core PBT / Op EBITDA | +98 bps / +44.56% / +19.57% | +98.2 bps; 392.33/271.40; 739.67/618.63 | derived | PASS |
| PAT bridge 4A, every component and total | +508.22, -357.45, -182.98, -73.61, -34.23, -18.00, -93.56, +62.25, -12.02 = -201.38 | identical; dGP 150.77 ties; dPBT -251.61 ties; tax -50.23 ties | L407-428 | PASS |
| PAT bridge 4B (standalone) | -178.89 m | -223.21 PBT, +53.79, -9.47 | L75-94 | PASS |
| Recurring share of PBT fall | 55.7% / 44.3% | 140.05/251.61; 111.56/251.61 | derived | PASS |
| Segment walk (all 27 cells) | e.g. Dairy result -29.47%, Feed margin 3.91% | 438.07/621.13; 33.29/852.50 | L461-470 | PASS (Feed YoY bps see S1) |
| Product split and derived Q1 | Milk +8.48%, VAP +31.95%, Q1 VAP +39.75% | 6,857/6,321; 4,510/3,418; 563.6/403.3 | P-l187-219 | PASS (sums tie to L407 within 1 m) |
| Spread and pass-through | 13.93 -> 12.61 (-9.5%); 72% | 60.34/1.06 = 56.92; 3.42/4.74 | PR-L76-84 | PASS |
| VAP share on standalone denominator | 35.42 / 42.47 / 31.35% | 4,510/12,733.76; 5,408/12,733.76; 3,418/10,904.14 | L75, PR-L130-138 | PASS |
| CFO, CFO/PAT (C) H1 FY27 / H1 FY26 / FY26 | 3.12x / 2.71x / 1.58x | 1,741.44/558.26; 2,481.16/915.41; 2,371.78/1,501.38 | L596, L428 | PASS |
| CFO/PAT ex inventory (C) | 2.08x / 1.03x / 1.35x | (1,741.44-581.74)/558.26 etc. | L586 | PASS |
| FCF (C) | -0.97 / 59.12 / -145.21 | 1,741.44-1,751.18; 2,481.16-1,889.93; 2,371.78-3,823.88 | L596, L598 | PASS |
| Inventory / receivable / payable days (C) | 22.82 / 5.41 / 17.71 (H1 FY27) | 2,600.79/20,857.98x183; 785.79/26,576.74x183; 2,018.93/20,857.98x183 | L516, L519, L547-548 | PASS |
| Net debt (C) incl. current investments | 68.41 -> 105.39 | 3,241.33-647.06-55.62-1,854.56; 3,452.25-584.51-74.64-1,739.25 | L517-521, L536, L544 | PASS |
| Gross D/E (C) FY26 / 30 Sep | 0.29 / 0.30 | 3,241.33/11,081.14 = 0.293; 3,452.25/11,408.26 = 0.303 | L533, L536, L544 | PASS |
| Deck "Net Debt/Equity 0.33" = gross D/E | "equals gross D/E" (R-L164, R-L457, Q20 R-L677) | Gross D/E = 0.29, not 0.33. 0.33 = (borrowings + lease liabilities) / total equity = (2,230.33+312.67+1,011.00+60.81) / 11,081.14 = 3,614.81 / 11,081.14 = 0.326 | L533, L536-537, L544-545; deck borrowings 2,543 + 1,072 (P-l1253, P-l1258) | FAIL (F1) |
| S-vs-C gap, 6 periods (all 54 cells) | e.g. Q2 FY27 PAT gap 1.12%, owners 2.78% | 3.42/305.15; 8.48/305.15 | L94, L428, L436 | PASS |
| Subsidiaries' net effect (brief) | "Subsidiaries now subtract more than they add" (R-L761) | Consolidated minus standalone: PBT +11.46 m, PAT +3.42 m, owners' PAT +8.48 m, Op EBITDA +28.50 m, all positive | L90/L424, L94/L428, L436 | FAIL (C1) |
| HNFL months consolidated in H1 FY26 | "about 2.5 months only" (R-L124) | 16 Jun to 30 Sep 2025 = about 3.5 months consolidated; about 2.5 months not consolidated | L645 | FAIL (F2) |
| Organised share of milk sales | "36% (CY20) to 41% (CY25)" (R-L772) | 36% CY20, 38% CY25, 41% CY30P (projection); column positions P-l1024/P-l1034 (36% col 128 = CY20 col 128; 38% col 144 = CY25 col 143; 41% col 161 = CY30P col 159); A1 R598 records CY30P as forward | P-l1018-1036 | FAIL (F3) |
| Trailing 4Q owners' PAT / EPS | 115.45 / 12.44 | (1,505.21-916.53)+565.80 = 1,154.48 m; /92.796 m | L436, L443 | PASS |
| ROCE proxy H1 FY27 annualised | 12.3% | (761.46+154.99)x2 / (11,408.26+3,452.25) = 12.33% | L424, L415, L533, L536, L544 | PASS |
| Unreviewed subsidiary Q1 loss / share of PAT | 0.09 Cr / 3.5% | 11.76-10.82 = 0.94 m; 10.82/308.57 | L723-724 | PASS |
| Bps and pp computed from rounded intermediates | GM YoY -270 bps (R-L216); S QoQ +98 bps (R-L299); Feed margin -512 bps (R-L318); VAP share +3.46 pp (R-L167, Q19); FCF change -60.09 (R-L446); WC change -52.83 (R-L447); S FCF change -55.74 (R-L469); H1 gap narrowing 5.26 pp (R-L507) | -271 bps; +99 bps; -513 bps; +3.45 pp; -60.10; -52.84; -55.75; 5.27 pp | various | ROUNDING (S1) |

Arithmetic result: core financial arithmetic is clean. Four mismatches change a stated number or fact (F1, F2, F3, C1).

---

## 3. ADVERSARIAL READ

The three most positive claims in A4's review are the Step 8 bull reading (R-L632) and its brief versions. Each counter is built only from the extract.

### P1. "Value-added products grew 32% YoY to Rs 451.0 Cr and are now the growth engine" (R-L760; R-L632; R-L780)

Strongest bear counter:
- About 40% of the revenue growth in the large VAP lines is price or mix, not volume. Implied realisation from revenue vs volume growth (PR-L86-90): curd 1.26/1.15 = +9.6%; paneer 1.38/1.21 = +14.0%; ice cream 1.81/1.44 = +25.7%; buttermilk 1.66/1.56 = +6.4%; lassi 1.91/1.89 = +1.1%. On a log split, price is 40% of curd growth, 41% of paneer and 39% of ice cream. These are price rises taken in a milk-inflation year, so elasticity is untested.
- The deck's product split is consolidated (it sums to L407). It therefore holds the yogurt (Heritage Novandie) and ice-cream (Get-A-Way) subsidiaries. Their dairy segment result was negative: consolidated Dairy minus standalone Dairy = -20.51 m in Q2 FY27 vs -13.29 m in Q2 FY26 (L468 minus L125) [derived; includes consolidation adjustments]. Part of the VAP growth therefore carries a negative margin [INFERENCE].
- A4 already carries the Q1-to-Q2 deceleration (+39.75% to +31.95%, R-L336) and the gross-margin fall against the mix shift (R-L781).

Survives: YES, for the price share and the subsidiary content. Graft into brief part 3 and the Step 8 bull reading (text in Section 5).

### P2. "Cash conversion positive at CFO level: CFO exceeds PAT in all three in-run readings, with and without the inventory release" (R-L492; R-L443-444; R-L763; R-L632)

Strongest bear counter:
- CFO/PAT above 1.0x is mostly mechanical in a capex-heavy year. D&A was 53.9% of FY26 PAT (809.83/1,501.38) and 96.7% of H1 FY27 PAT (539.57/558.26; L570, L428).
- Against operating EBITDA, pre-tax cash generated excluding the stock release (L594 minus L586) covered 0.91x in FY26 (2,422.92/2,662.70), 0.78x in H1 FY26 (1,181.26/1,510.75) and 1.01x in H1 FY27 (1,373.94/1,358.29). Excluding the Rs 10.98 Cr inflow from other financial liabilities (L592), H1 FY27 is 0.93x. That line's standalone counterpart does not tie to the balance sheet (RES-F12-3, R-L488).
- Non-inventory working capital absorbed cash: Rs 38.82 Cr in FY26 (receivables -37.86, other assets -27.39, other financial liabilities -8.95, offset by payables +36.40; L587-593) and about Rs 43.3 Cr in H1 FY26. A4's "there is no WC drag" (R-L485) holds only for inventory.

Survives: YES. The "positive direction" is not established on an EBITDA basis. The classification should read INDETERMINATE (direction not established) or carry this counter next to the direction. The verdict cap is unchanged.

### P3. "Q2 margin recovered 98 bps from the Q1 trough; core PBT +44.6% QoQ; opex fell 138 bps as a share of revenue" (R-L759; R-L367; R-L381; R-L430; R-L632)

Strongest bear counter:
- The same Q1-to-Q2 step happened last year. In FY26, Op EBITDA margin went from 6.50% (Q1) to 6.94% (Q2), +44 bps. Gross margin went from 23.81% to 24.54%, +74 bps. The H2 FY26 average then fell to an Op margin of 5.06% and a gross margin of 22.71%, which is 183 bps below Q2 FY26 (derived from L407-418, H1, FY and Q2 columns). Q2 is the seasonal gross-margin high, so a Q2 rise is weak evidence of a turn.
- The +98 bps QoQ splits as gross margin +63 bps, other expenses +58 bps (1,300.80 to 1,206.51 m, -7.2% QoQ, L418) and employee cost -23 bps (L414). The other-expense fall is likely seasonal summer spend [INFERENCE].
- The gross-margin gain came with a Rs 48.32 Cr drawdown of finished goods and WIP (L413; Q1 FY27 only Rs 0.29 Cr). Fat-product sales also jumped 31.9% QoQ (69.6 to 91.8 Cr, derived from P-l187-219). Slide 9 shows both cost series rising every month in level (P-l276-288). The drawn-down stock was therefore made at lower milk cost than the September replacement cost [INFERENCE: inventory carried at cost].
- The YoY opex leverage (-138 bps) rides on price-led revenue: milk volume +2.5% vs realisation +6% (PR-L126-128). Pass-through revenue carries little margin.
- Consequence for Step 8C (finding M3): repeat FY26's Q2-to-H2 step (-183 bps) on Q2 FY27's 21.84% and the result is about 20.0%. That is below A4's bear threshold of 21.20% (R-L647), so the bear threshold can fire on season alone with no change in the spread.

Survives: YES. Graft into 3C, the brief summary line and Step 8C.

### MANDATORY ACQUISITION-ECONOMICS PROBE

The documents describe acquisitions. Control of Heritage Novandie Foods Limited was taken on 16 Jun 2025 (L645). The release headline is "Strategic Acquisitions Scaling Up", with Novandie "wholly owned" and Get-A-Way "71%-owned" (PR-L146-148). Non-controlling interest first appears in FY26 (deck 0 / 0 / 48, P-l1250).

- Consideration: NOT FOUND in the corpus. Cash proxy: the FY26 consolidated investing line "Investment in a Subsidiaries" was a net outflow of Rs 16.22 Cr (L600) [INFERENCE: acquisition cash net of cash acquired]. Standalone cash put into subsidiaries over FY26 and H1 FY27 was investments 175.00 + 72.00 m and loans 67.34 + 4.86 m, a total of Rs 31.92 Cr (L254-255; covers all three subsidiaries).
- Target earnings: negative in every disclosed period. The derived dairy-subsidiary segment result (consolidated Dairy minus standalone Dairy) was -35.36 m in FY26, -17.57 m in H1 FY26 and -31.48 m in H1 FY27 (L468, L125). The NCI loss was 7.54 m in H1 FY27 (L440). If Get-A-Way is the only NCI entity at 29%, its H1 FY27 loss is about 26.0 m.
- Multiple: about Rs 16.2 Cr net cash (consideration NOT FOUND) against target PAT below zero. No positive earnings multiple exists, and price/PAT is not meaningful.
- Quality markers: target ROCE, debt, cash and customer tenure are NOT FOUND. The unreviewed subsidiary shows total assets Rs 15.65 Cr and an H1 net cash outflow of Rs 0.40 Cr (L722-725).
- Balance-sheet exposure: goodwill is 71.85 m (L507). Other intangibles held in subsidiaries are 134.46 m (consolidated 145.07 m, L508, minus standalone 10.61 m, L160). Together that is about Rs 20.63 Cr. Consolidated "intangible assets and investment property" rose from 65 m to 246 m in FY26, the acquisition year (P-l1250). A4 names only the Rs 7.19 Cr goodwill (Q14 R-L671, M8 R-L709).
- Bear reading: the acquisitions are presented as scaling, but the release gives no revenue or profit for either (A4 Q3 notes this). The acquired dairy businesses lose money at a widening rate (-1.33 Cr Q2 FY26 to -2.05 Cr Q2 FY27). They carry about Rs 20.6 Cr of goodwill and intangibles, which is 17.9% of trailing owners' PAT of Rs 115.45 Cr (R-L596). The FY27 year-end impairment exposure is therefore about 2.9x the goodwill figure A4 states.
- Side inference for Q8 [INFERENCE]: if Get-A-Way's implied H1 loss is about 26.0 m, it is not the unreviewed subsidiary (H1 loss 11.76 m, L724). Nutrivet earned PBT Rs 5.6 Cr in H1 (PR-L144). By elimination, the unreviewed subsidiary is most likely Heritage Novandie. Its scale (Q2 revenue Rs 14.26 Cr) fits the dairy subsidiaries' Q2 segment revenue of about Rs 15.65 Cr (L461 minus L119).

Survives: YES. Graft into Q14, M8 and F5.

---

## 4. FINDINGS (tagged)

### FACTUAL (loop A4)
- F1. Deck "Net Debt/Equity 0.33" is described as equal to gross D/E (R-L164, R-L457, Q20 R-L677). A4's own FY26 gross D/E is 0.29. The 0.33 is borrowings plus lease liabilities over total equity (3,614.81 / 11,081.14 = 0.326; L536-537, L544-545; deck borrowings 2,543 + 1,072 include leases, P-l1253, P-l1258). The point that the "net" label is wrong still stands, because no cash is deducted. The stated equality is false.
- F2. R-L124 says H1 FY26 consolidates HNFL "for about 2.5 months only". Control from 16 Jun 2025 (L645) means about 3.5 months consolidated and about 2.5 months missing. The acquisition-effect conclusion stands; the figure is wrong.
- F3. R-L772 says organised share rose "from 36% (CY20) to 41% (CY25) and 59% unorganised". The extract gives 36% CY20, 38% CY25 and 41% CY30P, a projection (P-l1024, P-l1029, P-l1034; R598). Actual shift: 2 pp in five years.
- F4. R-L789 calls the "zero milk holiday" a farmer-payment record. The deck lists "No Milk holiday since inception" (P-l665-667) separately from "Thrice a month payment" (P-l661-662). It is a procurement-continuity claim: the company buys all milk offered. That is relevant to Q10, where procurement grew +7% vs sales +2.5%.

### CONTRADICTION (loop A4)
- C1. The brief says "Subsidiaries now subtract more than they add" (R-L761). F5 says "Subsidiaries turned into a drag" (R-L734), and Step 9 and the YAML flags say "subsidiaries now a drag" (R-L722, R-L879). A4's own 5E table (R-L500) shows consolidated above standalone in Q2 FY27: PAT +Rs 0.34 Cr, owners' PAT +Rs 0.84 Cr, Op EBITDA +Rs 2.85 Cr. Its 6E red threshold "< 0% (subsidiaries net loss-making)" is not hit at 1.12% (R-L584). Correct reading: subsidiaries still add, but far less. Feed adds (+3.33 Cr segment result); dairy subsidiaries lose (-2.05 Cr).
- C2. R-L742 says the cash-conversion state means "the verdict cannot be PROCEED or PROCEED WITH CAVEATS". R-L492 and the house rule say INDETERMINATE caps at PROCEED WITH CAVEATS with the missing evidence named. PROCEED WITH FLAGS stands on F2-F8 anyway; only the rationale sentence is wrong.

### MISSING (loop A4)
- M1. Slide 9 cost-series reading. A4 labels the +4.8% to +8.3% series "Main procurement series" (R-L350). F3, the sector brief, Q1 and 8C say procurement-cost YoY inflation "rose every month to September" (R-L732, R-L770, R-L658, R-L646). The species mapping is unresolved in the extract: R178/R181 carry CHART_LABEL_UNMAPPED, and the legend at P-l295 does not fix position. The extract's own arithmetic leans the other way. Weight cow at 80% (P-l265) and use the Q2 months (P-l270-288):
  - Reading A (cow = Rs 51-55 series): blended standard cost Rs 51.08/L is above landed cost Rs 47.73/L (PR-L76), and the YoY change is +Rs 3.98.
  - Reading B (cow = Rs 39-41 series): blended standard cost Rs 42.85/L sits Rs 4.88 below landed, a stable add-on (Rs 5.06 a year earlier), and the YoY change is +Rs 4.92 vs landed +Rs 4.74 (PR-L77).
  - Under B, cow cost inflation, 80% of procurement, ran +15.5% / +15.0% / +14.5% in Jul / Aug / Sep. It peaked in July and stayed at about twice reading A's level.
  - Fix: state both readings and this check. Name the separating observation: the species split of Q2 procurement cost (Q2 concall or a labelled Q3 slide 9). Re-word F3, the sector brief, Q1 and 8C so that the September exit claim is "cost level rising every month", which holds in both readings.
- M2. Deck-internal contradiction not recorded. Slide 17 claims a 6% 3-year CAGR (FY23-FY26) for milk procurement and 3% for milk sales (P-l540-554; the 6% sits over "Milk Procurement"; A1 R250 mislabels it as an "Others" pie label). The deck's own slide 21 chart, validated by its H1 FY27 tie (17.7 / 12.0 vs release 17.69 / 11.99 LLPD, PR-L122, PR-L127), gives procurement of 15.9 LLPD in FY23 and 16.7 in FY26: 1.6% CAGR. Sales go 10.9 to 11.8: 2.7%, consistent with the claim. Procurement fell 2.9% in FY26 (17.2 to 16.7). Fix: add to F8 (disclosure quality). Note that Q2's +7% procurement growth is off an FY26 base that fell.
- M3. The Step 8C make-or-break metric ignores seasonality visible in the extract. FY26 gross margin went from 24.54% in Q2 to a 22.71% H2 average (-183 bps). The bear threshold (< 21.20%) can fire on season alone. Fix: test Q3 FY27 gross margin YoY against Q3 FY26, which is printed as a comparative in the Q3 FY27 filing. Bull: the YoY gap narrows from -271 bps. Bear: it widens. Or state seasonally adjusted thresholds. Align R-L795 and the forward-map row R-L800.
- M4. Surviving bear counter P1 (VAP price share; subsidiary content) is not in the review.
- M5. Surviving bear counter P2 (D&A-driven CFO/PAT; EBITDA-basis conversion 0.78x to 1.01x; non-inventory WC absorbed Rs 38.8 Cr in FY26) is not in the review.
- M6. Surviving bear counter P3 (seasonal Q1-to-Q2 step; stock drawdown at older cost; other-expense swing) is not in the review.
- M7. Acquisition-economics probe result is not in the review: no multiple computable, target earnings negative, and about Rs 20.6 Cr of goodwill plus intangibles at risk vs the Rs 7.19 Cr A4 names.

Note on routing. M1 and M2 are forensic misses on the presentation. This audit fully derives both with line anchors, so A4 can graft them without an A3 re-run. The orchestrator may route them through A3 if it prefers strict routing.

### STYLE (logged, no loop)
- S1. Bps and pp deltas computed from rounded intermediates: -270 vs -271 bps (R-L216); standalone QoQ +98 vs +99 bps (R-L299); Feed -512 vs -513 bps (R-L318); +3.46 vs +3.45 pp (R-L167, Q19); -60.09 vs -60.10 (R-L446); -52.83 vs -52.84 (R-L447); -55.74 vs -55.75 (R-L469); 5.26 vs 5.27 pp (R-L507). Compute deltas from unrounded ratios.
- S2. The preamble heading "Findings incorporated (47)" lists 48 items including A4-OBS-1 (R-L20-24).
- S3. The A2 results ledger counts agenda_items 0. The board outcome letter has 2 numbered items (L38, L41), carried under other categories (R1193, R1172, R1148). No row is missing.
- S4. A1/A2 presentation: 3 dash cells on slide 8 are not carried as rows (P-l242 H1FY27; P-l245 Q1FY27 and H1FY27). The filing confirms nil (L421, L423).
- S5. The A1 presentation structured file lacks the number-word claims "Zero Milk Holiday" (P-l600-601) and "No Milk holiday since inception" (P-l665-667). "Thrice a month" is carried (R289). A4 cites both from the fulltext.
- S6. A1 R250 labels slide 17's "6%" as "Others 6%". Positionally it is the procurement CAGR bar; the FY23 pie closes at 100% with Others 3% (P-l542-554). See M2.
- S7. A1 R178/R181 assign species (51.59 cow, 38.80 buffalo) inside rows flagged only "month unmapped". The species assignment needs its own flag. See M1.
- S8. Two forward-map catalysts carry "date ND" (R-L801, R-L803). Anchor the check to the Q3 FY27 results date (by 14 Feb 2027) and the FY27 audited results date (by 30 May 2027) as review points.

---

## 5. GRAFT TEXT FOR A4 (ready to paste; numbers anchored)

1. F1 (R-L164, R-L457, Q20): "The deck's FY26 'Net Debt/Equity 0.33' is borrowings plus lease liabilities over total equity (Rs 361.48 Cr / Rs 1,108.11 Cr = 0.33; L536-537, L544-545). Borrowings alone give 0.29. No cash or investments are deducted, so the 'net' label is wrong."
2. F2 (R-L124): "H1 FY26 consolidates HNFL for about 3.5 months (16 Jun to 30 Sep 2025); about 2.5 months of HNFL are missing from the base."
3. F3 (R-L772): "the deck cites organised share of milk sales at 36% (CY20) and 38% (CY25), projected 41% by CY30 (P-l1018-1036, 'Ilattice Analysis') [SECONDARY]."
4. F4 (R-L789): "a 'no milk holiday since inception' procurement commitment (P-l600-601, P-l665-667): the company buys all milk offered, which also explains why procurement (+7%) ran ahead of milk sales (+2.5%) [INFERENCE]."
5. C1 (R-L761, R-L734, R-L722, flags): "Subsidiaries now add little. Consolidated PAT beat standalone PAT by Rs 0.34 Cr (1.12%), against Rs 2.59 Cr (5.35%) a year ago. Feed still earns (segment result Rs 3.33 Cr); the dairy subsidiaries lose money (-Rs 2.05 Cr)."
6. C2 (R-L742): replace with "Cash conversion is INDETERMINATE, which caps the verdict at PROCEED WITH CAVEATS; the flags below take it to PROCEED WITH FLAGS."
7. M1 (R-L350-351, F3, R-L770, Q1): relabel the two rows "Series 1 (Rs 51-55/L)" and "Series 2 (Rs 39-41/L)", species unresolved. Add: "If cow milk (80%) is the lower-priced series, its blended standard cost (Rs 42.85/L) sits Rs 4.9 below landed cost and its YoY rise (+Rs 4.92) matches landed (+Rs 4.74). On that reading, cow cost inflation ran +15.5% / +15.0% / +14.5% in Jul to Sep: it peaked in July at about twice the other reading. Both readings show the cost level rising every month. Separating observation: the species split of Q2 cost (concall or Q3 slide 9)."
8. M2 (F8): "Slide 17 claims a 6% FY23-FY26 procurement CAGR; the deck's own slide 21 gives 15.9 to 16.7 LLPD, 1.6%, with FY26 down 2.9% (17.2 to 16.7). Q2's +7% procurement growth is off that lower base."
9. M3 (8C, R-L795, R-L800): "Seasonal note: in FY26 gross margin fell from 24.54% (Q2) to a 22.71% H2 average. Test Q3 FY27 gross margin YoY against Q3 FY26 (comparative in the Q3 filing): bull if the YoY gap narrows from -271 bps, bear if it widens."
10. M4 (brief part 3, Step 8 bull): "About 40% of revenue growth in curd (+26% revenue, +15% volume), paneer (+38%, +21%) and ice cream (+81%, +44%) is price or mix (PR-L86-90). The consolidated VAP figure includes loss-making yogurt and ice-cream subsidiaries."
11. M5 (5D, R-L763): "CFO/PAT above 1x is mostly D&A (54% of FY26 PAT, 97% of H1 FY27 PAT). Against operating EBITDA, pre-tax cash generated excluding the stock release was 0.91x (FY26), 0.78x (H1 FY26) and 1.01x (H1 FY27), or 0.93x without the untraced Rs 10.98 Cr other-financial-liabilities inflow (L592). Non-inventory working capital absorbed Rs 38.8 Cr in FY26. Direction not established."
12. M6 (3C, R-L759): "The same Q1-to-Q2 step happened in FY26 (+44 bps Op margin, +74 bps gross margin), followed by an H2 gross margin 183 bps lower. Q2 FY27's +63 bps gross-margin gain came with a Rs 48.32 Cr stock drawdown (L413) made at earlier, lower milk cost [INFERENCE]; other expenses fell 7.2% QoQ (L418)."
13. M7 (Q14, M8, F5): "Acquisition economics: consideration NOT FOUND; acquired dairy businesses loss-making in every period (FY26 -Rs 3.54 Cr, H1 FY27 -Rs 3.15 Cr segment result, derived); no positive earnings multiple. Goodwill Rs 7.19 Cr plus Rs 13.45 Cr of other intangibles held in subsidiaries (L507-508 vs L160) = about Rs 20.6 Cr exposed to the FY27 impairment test. Q8 hypothesis: the unreviewed subsidiary is most likely Heritage Novandie [INFERENCE]."

---

## VERDICT

INCOMPLETE. Loop back to: A4.
- FACTUAL: F1 (0.33 is not gross D/E), F2 (HNFL months), F3 (CY25 organised share), F4 (milk-holiday gloss).
- CONTRADICTION: C1 (subsidiaries "subtract more than they add" vs a positive gap), C2 (verdict rationale vs cap rule).
- MISSING: M1 (slide 9 alternate reading), M2 (slide 17 vs slide 21), M3 (8C seasonality), M4-M6 (surviving bear counters P1-P3), M7 (acquisition probe).
- Mechanics are clean: the deliverable gate passes, ledgers reconcile, no orphan rows, and core arithmetic recomputes. The protocol verdict PROCEED WITH FLAGS is not challenged.

## STYLE NOTES

S1-S8 above, recorded for the record. No re-run is triggered by any of them.

---

```yaml
stage: A5-adversary
company: "HERITGFOOD"
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
  - {metric: "Deck Net Debt/Equity 0.33 = gross D/E (FY26)", a4_value: "equals gross D/E (A4 gross D/E 0.29)", recomputed: "0.29 borrowings-only; 0.326 = (borrowings + lease liabilities 3,614.81 m) / total equity 11,081.14 m", source_line: "L533, L536-537, L544-545; P-l521, P-l1253, P-l1258"}
  - {metric: "HNFL months consolidated in H1 FY26", a4_value: "about 2.5 months", recomputed: "about 3.5 months (16 Jun-30 Sep 2025); 2.5 months missing", source_line: "L645"}
  - {metric: "Organised share of milk sales CY25", a4_value: "41% (CY25), 59% unorganised", recomputed: "38% CY25 (62% unorganised); 41%/59% is CY30P projection", source_line: "P-l1024, P-l1029, P-l1034; R598"}
  - {metric: "Subsidiaries net effect Q2 FY27", a4_value: "subtract more than they add", recomputed: "consolidated minus standalone PAT +3.42 m, owners +8.48 m, PBT +11.46 m, Op EBITDA +28.50 m", source_line: "L94, L428, L436, L90, L424"}
surviving_bear_counters:
  - {claim: "VAP +32% YoY to Rs 451.0 Cr is the growth engine (R-L760, R-L632)", counter: "About 40% of growth in curd, paneer and ice cream is price or mix (curd +26% revenue on +15% volume; paneer +38% on +21%; ice cream +81% on +44%); consolidated VAP includes loss-making yogurt and ice-cream subsidiaries (dairy subsidiary segment result -20.51 m Q2 FY27)", source_line: "PR-L86-90; L468, L125; P-l187-219", type: "MISSING"}
  - {claim: "Cash conversion positive: CFO exceeds PAT in all readings (R-L492, R-L763)", counter: "D&A = 54% of FY26 PAT and 97% of H1 FY27 PAT; pre-tax cash generated ex stock release / Op EBITDA = 0.91x FY26, 0.78x H1 FY26, 1.01x H1 FY27 (0.93x ex untraced 109.76 m other-financial-liabilities inflow); non-inventory WC absorbed Rs 38.8 Cr in FY26; direction not established", source_line: "L570, L585-596, L592; L428", type: "MISSING"}
  - {claim: "Q2 margin recovered 98 bps QoQ; core PBT +44.6%; opex -138 bps (R-L759, R-L632)", counter: "Same seasonal Q1-to-Q2 step in FY26 (+44 bps Op margin, +74 bps GM) followed by H2 GM 183 bps lower; Q2 GM gain came with a Rs 48.32 Cr stock drawdown at earlier, lower cost; other expenses -7.2% QoQ; opex leverage rides on price-led revenue", source_line: "L407-418, L413, L418; P-l276-288; PR-L126-128", type: "MISSING"}
  - {claim: "Strategic Acquisitions Scaling Up (PR-L146-148); acquisition probe", counter: "Consideration NOT FOUND; acquired dairy businesses loss-making every period (FY26 -35.36 m, H1 FY27 -31.48 m derived); no positive multiple (about Rs 16.2 Cr net cash / PAT < 0); goodwill 71.85 m + subsidiary intangibles 134.46 m = about Rs 20.6 Cr at impairment risk vs Rs 7.19 Cr named by A4", source_line: "L600, L507-508, L160, L468, L125, L440; P-l1250", type: "MISSING"}
findings_by_type:
  factual:
    - "F1: deck Net Debt/Equity 0.33 is (borrowings + lease liabilities)/equity = 0.326, not A4's gross D/E 0.29 (R-L164, R-L457, Q20; L536-537, L544-545)"
    - "F2: H1 FY26 consolidated HNFL about 3.5 months, not 2.5 (R-L124; L645)"
    - "F3: organised share 36% CY20, 38% CY25, 41% is CY30P projection; A4 says 41% CY25 (R-L772; P-l1024-1034)"
    - "F4: 'zero milk holiday' is a procurement-continuity claim listed apart from 'Thrice a month payment', not a farmer-payment record (R-L789; P-l661-667)"
  missing:
    - "M1: slide 9 species mapping unresolved; extract arithmetic (blended standard vs landed cost) leans to cow = Rs 39-41 series with Q2 YoY +15.5/+15.0/+14.5% peaking July; A4 states only the 'rising every month' reading (R-L350, R-L732, R-L770, Q1, 8C)"
    - "M2: deck slide 17 claims 6% FY23-FY26 procurement CAGR; deck slide 21 gives 15.9 to 16.7 LLPD = 1.6%, FY26 -2.9%; not in F8 (P-l540-554, P-l647-671)"
    - "M3: Step 8C GM thresholds ignore FY26 seasonal Q2-to-H2 step of -183 bps; bear threshold can fire on season alone; re-base to YoY vs Q3 FY26 (R-L643-648, R-L795, R-L800)"
    - "M4: surviving bear counter P1 (VAP price share, subsidiary content) not grafted"
    - "M5: surviving bear counter P2 (D&A-driven CFO/PAT; EBITDA-basis conversion 0.78-1.01x) not grafted"
    - "M6: surviving bear counter P3 (seasonal QoQ step; stock drawdown at older cost) not grafted"
    - "M7: acquisition-economics probe (no computable multiple; about Rs 20.6 Cr goodwill + intangibles at risk) not in review"
  contradiction:
    - "C1: brief 'subsidiaries now subtract more than they add' and F5/Step 9 'now a drag' vs A4's own 5E table (+Rs 0.34 Cr PAT, +Rs 0.84 Cr owners, +Rs 2.85 Cr Op EBITDA) and 6E red threshold not hit (R-L761, R-L734, R-L722, R-L500, R-L584)"
    - "C2: R-L742 says CAVEATS is barred; R-L492 and house rule cap at PROCEED WITH CAVEATS; verdict unaffected"
  style:
    - "S1: bps/pp deltas from rounded intermediates (-270 vs -271; +98 vs +99; -512 vs -513; +3.46 vs +3.45 pp; -60.09 vs -60.10; -52.83 vs -52.84; -55.74 vs -55.75; 5.26 vs 5.27)"
    - "S2: preamble 'Findings incorporated (47)' lists 48 items"
    - "S3: A2 results agenda_items 0 vs 2 numbered items (L38, L41) carried under R1193/R1172/R1148"
    - "S4: 3 slide-8 dash cells not carried as rows (P-l242, P-l245); filing confirms nil (L421, L423)"
    - "S5: A1 lacks number-word rows 'Zero Milk Holiday' (P-l600-601), 'No Milk holiday since inception' (P-l665-667)"
    - "S6: A1 R250 labels slide 17 '6%' as Others pie label; it is the procurement CAGR bar"
    - "S7: A1 R178/R181 assign cow/buffalo species under a month-only unmapped flag"
    - "S8: two forward-map rows 'date ND'; anchor review points to 14 Feb 2027 and 30 May 2027"
loop_back_to: "A4"
gap: "A4 to correct F1 (0.33 = borrowings + leases / equity), F2 (HNFL 3.5 months), F3 (CY25 organised share 38%; 41% is CY30P), F4 (milk holiday gloss); resolve C1 (subsidiaries still net positive: +Rs 0.34 Cr PAT) and C2 (cap wording); add M1 (slide 9 alternate species reading and separating observation), M2 (slide 17 vs 21 procurement CAGR), M3 (seasonally neutral 8C test), and graft the four surviving bear counters M4-M7 using audit Section 5 text."
style_notes:
  - "S1: compute bps/pp deltas from unrounded ratios"
  - "S2: preamble count says 47, lists 48"
  - "S3: A2 agenda_items category should read 2"
  - "S4: carry slide-8 dash cells as ZERO_STANDING rows"
  - "S5: carry number-word claims as NUMBER rows"
  - "S6: A1 R250 label fix"
  - "S7: A1 species assignment needs its own unmapped flag"
  - "S8: anchor date-ND catalysts to filing deadlines"
analyst_note: "Mechanics are clean. All five brief parts are present, ledgers reconcile with no material orphan or missing row, and core P&L, segment, bridge, cash and S-vs-C arithmetic recompute to rounding. The audit is INCOMPLETE on content. Three numbers are misread: the deck 0.33 includes lease liabilities; HNFL was consolidated about 3.5 months of H1 FY26; the CY25 organised share is 38%, and 41% is a CY30 projection. The brief says subsidiaries subtract more than they add, but A4's own table shows they still add Rs 0.34 Cr. The weightiest open point is slide 9. Landed vs blended standard cost leans to cow milk being the cheaper series, whose YoY inflation ran 14.5-15.5% and peaked in July, not 'rising every month'. The 8C thresholds also ignore a 183 bps Q2-to-H2 seasonal step. Four bear counters survive. M1 and M2 are forensic misses but fully derived here, so A4 can graft them without an A3 re-run. A grep returned two A3 lines incidentally; they were not used."
```
