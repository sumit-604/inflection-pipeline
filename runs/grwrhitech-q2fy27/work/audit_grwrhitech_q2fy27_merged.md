# A5 ADVERSARY AUDIT (MERGED REVIEW): GRWRHITECH | q2fy27

Agent: A5 adversary / completeness auditor | Model: claude-opus-5-5 | Date: 2026-10-23
Review under audit: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md (1,271 lines, A4 loop_iteration 3 plus the concall merge)
Inputs read: the A4 review (in full); A1 fulltexts (results l.1-1492; concall L0001-L0842, in full); A1 structured extractions (concall R001-R419 in full; results rows by targeted grep); A2 ledgers (results, concall, in full). No source PDF, no audio, nothing under inputs/ opened. No A3 file and no prior A5 audit opened.
Anchors: "rev l.N" = line N of the review. "l.N" = line N of grwrhitech-results-q2fy27-fulltext.md. "L0nnn" = the 4-digit source prefix in grwrhitech-concall-q2fy27-fulltext.md. "R###" = A1 structured row. [DERIVED] = my arithmetic on the cited lines.

---

## AUDIT 0. DELIVERABLE-COMPLETENESS (hard gate)

| Brief part | Location | Status |
|---|---|---|
| (1) Summary narrative | rev l.1095-1112 (17 lines; inside the 10-20 band) | PRESENT |
| (2) Sector intelligence | rev l.1114-1121 (7 bullets) | PRESENT |
| (3) Business-model intelligence | rev l.1123-1132 (9 bullets) | PRESENT |
| (4) Competition intelligence | rev l.1134-1138 (4 bullets) | PRESENT (content issue F2 below; the part itself is real content, not a placeholder) |
| (5) Forward map | rev l.1140-1151 (make-or-break line plus 10 dated catalysts, each with a Bull and a Bear fork) | PRESENT (threshold issue F1 below) |

Gate: PASS. All five parts exist and carry real content.

---

## AUDIT 1. COVERAGE (fresh enumeration vs A2 ledgers)

Method. Results: I re-counted each category from the results fulltext (notes l.357-367 and l.735-749; auditor paragraphs l.100-135 and l.390-480; entities l.424-427 and l.744-746; agenda l.40-49; statement labels l.170-224, l.236-288, l.298-355, l.509-585, l.597-651, l.665-733, l.770-788; deck asterisk and footnote text l.1114-1470) and diffed against the ledger. I spot-checked load-bearing deck numbers for rows (764, 141, 774, 650, 182, 4,200, 600, 4,800, 42,000, 66,000, 168, 38, 37, 35%, 70%: all present, R1066-R1288). Concall: I swept every number-bearing source line L0001-L0842 against the line anchors of R001-R419, allowing the 1-3 line drift that A2 documents (ledger_concall l.21).

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: numbered notes | 7 | 7 (SA 1-3, l.358-367; C 1-4, l.736-749) | none | PASS |
| Results: unnumbered footnotes | 14 | 14 (p29 4, p31 2, p32 1, p35 4, p42 3). Every footnote text in l.1114-1470 maps to R1766-R1779, including "**Debt repayment of Rs 141 cr in FY24" (l.1470, R1778) | none | PASS |
| Results: line items | 205 | 205 (SA P&L 24, SA BS 30, SA CF 38, C P&L 32, C BS 31, C CF 41, release table 9) | none | PASS |
| Results: zero-standing | 11 | 11. Three of them carry values by position (l.547 OCI tax 0.14; l.687 MF gain 23.22; l.728 FX effect 1.54); the review handles all three (rev l.22) | none | PASS |
| Results: agenda items | 3 | 3 (1 numbered item, 2 enclosures, l.40-49) | none | PASS |
| Results: auditor paragraphs | 13 | 13 (SA 4; C 7 numbered + SEBI-circular paragraph l.419-422 + "not modified" l.480) | none | PASS |
| Results: entities | 4 distinct / 6 rows | 4 / 6 (l.425-427, l.744-746) | none | PASS |
| Results: forward statements | 37 | 37 (R1391-R1427, contiguous) | none | PASS |
| Results: slides | 24 | 24 (pp20-43; dividers pp23, 30, 36, 39) | none (category-level "all reviewed", rev l.18, l.23; see S9) | PASS |
| Results: MISSING_FROM_STRUCTURED | 4 | 4 (l.77, l.495, l.1478 CIN; l.751 signature) | none | PASS |
| Concall: participants | 11 | 11 (host L0019-L0021, Deepak Joshi L0026, 9 analysts from the 9 moderator hand-offs L0103-L0804) | none | PASS |
| Concall: turns | 97 | 97 (T01-T97; no diarization, boundaries are best effort) | none | PASS |
| Concall: analyst-side turns | 39 | 39 (Bendre 5, Parikh 5, Pal 6, Jain 6, Singhvi 4, Desai 2, Sarada 3, Chain 3, Jain 5). A4 Step 4A maps them to 36 exchanges and merges T67, T73 and T81 into adjacent exchanges; all 39 are accounted for | none | PASS |
| Concall: NUMBER rows | 222 | No new distinct unit. These digit lines have no same-line row: L0022, L0087, L0228, L0560-L0563, L0607, L0633, L0660, L0774, L0826-L0827, L0834. Each one restates a value that has a row within the documented drift (e.g. L0774 "25% ... 75% ... 10% 15%" vs R370, R371, R353; L0228 "3500" vs RESTATED R146, R162, R322) | none | PASS |
| Concall: forward / hedge / entity / date rows | 67 / 47 / 53 / 30 | 67 / 47 / 53 / 30 (tally of R001-R419; 222 + 67 + 47 + 53 + 30 = 419). I enumerated the 67 FORWARD rows one by one for the specificity check (audit 2) | none | PASS |
| Concall: MISSING_FROM_STRUCTURED | 1 (MFS01, L0520) | 1 | none (review rev l.22 item 6) | PASS |

Ledger-row accounting in A4: the preamble states that every note, turn and slide was reviewed and that no ledger row is unreviewed (rev l.18-23). A4 also takes up each specific A2 flag: UNIDENTIFIED_ENTITY_ASSIGNMENT (Q12), STEP_DOWN_ONLY_IN_NOTE3 (1-G), FOOTNOTE_UNRESOLVED R1712 and R1740 (rev l.97, l.1087), MGMT_ABSENCE (FN14), REPEAT_QUESTION and MARGIN_THEME (Step 4B), the studio-count conflict (Q23), "beta margin" (Q25) and MFS01 (rev l.22).
orphan_rows: none. missing_from_ledger: none. Coverage: PASS.

---

## AUDIT 2. ARITHMETIC (recomputed from raw extracted numbers)

Every derived figure in the A4 tables that I recomputed ties within rounding. The table lists the load-bearing set. I also re-tied every statement subtotal: SA and C Total Expenses in all six columns; PBT and PAT; both balance sheets by position (C l.597-651; SA l.236-288); both cash flows (C l.665-733; SA l.298-355).

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| C Op EBITDA Q2 FY27 (PBT + D + Fin - OI) | 169.47 | 173.06 + 13.05 + 2.89 - 19.53 = 169.47 | l.510, l.523, l.525, l.532 | PASS |
| C Op EBITDA margin Q2 FY27 / Q1 FY27 / Q2 FY26 / H1 FY27 | 24.37% / 27.17% / 20.97% / 25.70% | 24.366% / 27.169% / 20.966% / 25.701% | l.509 | PASS |
| C Reported EBITDA Q2 FY27 / H1 FY27 / FY26 | 189.00 / 380.72 / 499.55 | 189.00 / 380.72 / 499.55 | l.523-532 | PASS |
| C ETR Q2 FY27 / H1 FY27 | 25.21% / 25.01% | 43.62/173.06 = 25.205%; 87.43/349.52 = 25.014% | l.532, l.539 | PASS |
| C gross margin by nature Q2 / Q1 | 54.69% / 59.87% | 380.39/695.53 = 54.691%; 379.02/633.08 = 59.869% | l.509, l.516, l.518 | PASS |
| C H1 FY26 change in inventories (garbled "(1?.60)") | (12.60) | 861.20 - 873.80 = (12.60) | l.518, l.530 | PASS |
| SA Op EBITDA Q2 FY27 / margin | 144.16 / 22.73% | 176.51 + 12.72 + 1.57 - 46.64 = 144.16; 22.735% | l.170-193 | PASS |
| SA H1 FY26 displaced cells | (10.27), 64.84, 78.43 | sum 133.00 = 790.39 - 448.04 - 2.56 - 20.81 - 185.98 | l.179-191 | PASS |
| PAT gap (C - SA)/SA, six periods | -14.35 / +4.80 / -7.46 / -3.79 / -1.64 / +1.05% | same | l.202, l.541 | PASS |
| Intra-group revenue eliminated Q2 / Q1 / H1 | 225.19 / 218.53 / 443.72 | 634.09 + 286.63 - 695.53; 584.14 + 267.47 - 633.08; 1,218.23 + 554.10 - 1,328.61 | l.170, l.443, l.509 | PASS |
| PAT-level consolidation deduction Q2 / Q1 / H1 | 50.88 / 3.71 / 54.59 | 139.87 + 40.55 - 0.10 - 129.44; 126.58 + 10.06 - 0.28 - 132.65; 266.45 + 50.61 - 0.38 - 262.09 | l.202, l.444, l.457, l.541 | PASS |
| Beyond-dividend deduction H1 | 26.55 to 26.68 | 54.59 - 28.04; 54.59 - 27.91 | l.307, l.681 | PASS |
| YoY C revenue / Op EBITDA / PAT / EPS | +22.09% / +41.89% / +41.88% / +41.86% | 125.84/569.69; 50.03/119.44; 38.21/91.23; 16.44/39.27 | l.509, l.541, l.571-577 | PASS |
| Margin YoY / QoQ (ex-OI) | +340 bps / -280 bps | 24.366 - 20.966 = 3.40; 27.169 - 24.366 = 2.80 | as above | PASS |
| Q2 ex-OI margin before an 11 refund | 22.78%, +182 bps | 158.47/695.53 = 22.784%; +1.818 pp | L0388; l.509 | PASS |
| PAT bridge YoY sum | +38.21 | 26.38 + 23.65 - 2.24 - 0.79 + 5.67 - 12.76 - 1.70 = 38.21 | rev l.286 | PASS |
| Tax bridge split | 12.76 + 1.70 | 52.67 x 24.221% = 12.757; 173.06 x 0.984 pp = 1.703 | l.532, l.539 | PASS |
| Two-year Q2 revenue / H1 revenue | +12.0% (5.8% a year) / +21.2% (10.1% a year) | 695.53/621; 1,328.61/1,096; square roots | l.1010 chart re-pairing (verified: 87/459, 157/597, 94/466, 121/548, 90/447 all match the l.1021 margin labels; FY25 sum 2,110 vs 2,109; FY25 EBITDA 130+150+94+121 = 495 = l.1120; FY26 123+133+87+157 = 500 = l.1120) | PASS |
| Guide-implied H2 margin incl OI | 25.12% | (675 - 380.72)/1,171.39 = 25.122% | l.1118; rev 1-C | PASS |
| 8C refund share / bear line | 2.79% / 19.5% | 16/573 = 2.792%; 22.31 - 2.79 = 19.52 | L0390; rev l.266 | PASS (arithmetic; interpretation fails, F1) |
| C CFO/PAT H1 FY27 / FY26 | 0.75x / 0.94x | 195.34/262.09 = 0.745; 163.03/174.25 = 0.936 | l.709, l.541 | PASS |
| SA CFO/PAT H1 FY27 | 0.36x | 94.70/266.45 = 0.355 | l.330-333, l.202 | PASS |
| Reading A CFO/PAT C / SA | 0.83x / 0.44x | 218.04/262.09; 117.40/266.45 | l.606, l.697, l.321 | PASS |
| Other assets tie C / SA | 35.80 / 27.47 | 13.10 + 22.70; 4.77 + 22.70 | l.606, l.619-620, l.697; l.244, l.258, l.321 | PASS |
| C receivable / inventory / payable days; CCC | 9.83 / 63.32 / 25.44; 47.71 | 71.56, 460.99, 185.21 on 2,657.22 x 365 | l.609-619, l.642-645 | PASS |
| SA CCC | 68.45 | 39.34 + 56.77 - 27.66 | l.247-250, l.279-280 | PASS |
| Net cash C 31-Mar / 30-Sep | (757.93) / (920.21) | 126.53 + 28.87 + 618.19 - 15.66; 191.62 + 29.45 + 711.75 - 12.61 | l.611-616, l.634-640 | PASS |
| Net cash ex MF gain | 898.93 | 920.21 - (711.75 - 618.19 - 72.28) | l.716 | PASS |
| "933" liquidity | 932.82 | 191.62 + 29.45 + 711.75 | l.813; L0053 | PASS |
| Finance-cost implied rate C | 75.6% | 10.68/14.135 = 75.56% (75.5% on the shown 14.14; S6) | l.523, l.634-642 | PASS (rounding) |
| ROCE FY26 / H1 ann. / avg CE / Q2 ann. / TTM | 17.01% / 24.31% / 25.39% / 24.11% / 19.68% (20.55%) | 454.42/2,671.82; 709.72/2,919.46; /2,795.64; 703.80/2,919.46; 574.41/2,919.46 (/2,795.64) | l.523, l.532, l.629-642 | PASS |
| Reval-adjusted ROCE FY26 / H1 | 23.82% / 32.93% | 454.42/1,907.82; 709.72/2,155.46 | l.1137, l.1470 | PASS |
| EPS bases: Q2 ann. / H1 ann. / TTM / Q1 x4 | 222.84 / 225.62 / 183.40 / 228.40 | 55.71 x 4; 112.81 x 2; 70.59 + 112.81; 57.10 x 4 | l.571-577 | PASS |
| PE at CMP 7,037.90 (H1 ann. / TTM) | 31.2x / 38.4x | 31.19x / 38.37x | rev l.453 | PASS |
| Cash profit H1 | 293.22, +46.2% | 262.09 + 25.86 + 5.27; / 200.63 | l.537-541 | PASS |
| 3,500 ceiling check | 3,482-3,532; SCF headroom about 473 | 2,782.12 + 450-500 + 250; 0.51 x 2,782 / 0.75 x 0.25 = 472.9 | L0693-L0695, L0117-L0121, L0369 | PASS |
| Opening-claims quantified share | 24 of 36 (66.7%) | 24 YES rows counted in rev l.580-615 | rev Step 1 | PASS |
| Specificity ratio | 0.52 (0.46 de-duplicated) | 35/67; 27/59 (my strict count of quantified FORWARD rows is 33, 35 with R140/R204; within judgment) | R016-R419 | PASS |
| Q&A grade count | A 3, B 19, C 12, D 1, E 1; C-E 38.9% | same; 14/36 | rev l.716-751 | PASS |
| Hedge-phrase count | 21 | 3 + 1 + 3 + 1 + 13 (each "expect" line verified) | L0045-L0829 | PASS |

arithmetic_mismatches: none above rounding.

---

## AUDIT 3. ADVERSARIAL READ (three most positive claims)

### AR1. "The margin climb survives the base test": +297 bps Q2 and +311 bps H1 over two years (rev l.230, Step 2 answer 1); Flag 13 "about +300 bps" (rev l.1052)
Bear counter (same extract). Management says 11 Cr of US tariff refund is "in our book" "till date" (L0386-L0388). The review itself places it inside H1 (rev l.89). The two-year test never strips it. On H1 the strip is unconditional: (380.72 - 11) / 1,328.61 = 27.83% against H1 FY25 280 / 1,096 = 25.55%, so the climb is +228 bps, not +311 [DERIVED; l.523-532, l.1010, l.1022]. On Q2, if all 11 fell there: 178.00 / 695.53 = 25.59% against 24.2%, so the climb is about +139 bps, and rupee EBITDA rose 18.7% over two years, not 26.0% [DERIVED; 178.00/150]. Both readings still include other income (2.81% of Q2 and 2.95% of H1 FY27 revenue; FY25 other income ND), so the ex-OI two-year gain could be smaller still.
Survives: YES. The direction holds; the size falls by a quarter (H1) to a half (Q2). Graft into Step 2 answer 1 and Flag 13, and into brief l.1097 if the two-year frame stays there. Type: MISSING (finding M2).

### AR2. Pricing power as Strategic Premium evidence: "pricing at 85-120% of global players" (rev l.450, l.810, l.977); brief: "Management now claims parity or better on many products" (rev l.1137)
Bear counter (same extract). The answer is about architectural film (L0478). The current level management states is "80-85% of the global player" (L0498-L0501). "85-90%" applies "in some cases" (L0505). A premium of 10-20% applies only to "certain products" (L0506-L0508). The comparison set excludes "the imports from China and Korea" (L0502-L0504). The deck says Chinese and Korean makers dominate the economy segment (l.1347-1353). Cheap Chinese PPF is still competing with no duty imposed (L0410-L0412, L0424-L0425). PPF is the lowest-margin consumer line at 20-25% (L0744). The stated typical position is therefore a 15-20% discount to the US/EU leader. That fits the prior 10-15% discount record. It is not a reversal, and the extract supports no "parity or better on many products". A4's own Step 4A row #15 (rev l.730) reads the answer correctly, so the brief also contradicts the review body.
Survives: YES. Fix the brief sentence (finding F2). Add the qualifier to the Strategic Premium rows (Step 7 rev l.450; Step 8D rev l.977) and to the 5A row (rev l.810). Type: FACTUAL (brief) plus MISSING qualifier (Step 7/8D).

### AR3. "At or above Base on H1 pro-rata for revenue, margin, PAT, EPS, net cash and ROCE, also after an 11 refund strip"; revenue "Above Bull" (rev l.381-386, l.463)
Bear counter tested. H1 is the strong half: Q1 is peak season and Q3 is the weakest quarter (L0043, L0655; l.1021). So a 50% pro-rata flatters H1. I tested the heaviest seasonal shares in the extract. FY25 H1 was 52.0% of revenue (1,096 / 2,109) and 56.6% of EBITDA (280 / 495). FY26 H1 was 50.2% of revenue, 51.3% of EBITDA and 51.5% of PAT [DERIVED; l.1010, l.1022, l.1116, l.1120, l.509-541]. On those shares, implied FY27 revenue is 2,556-2,646 (above Bull 2,502). Implied EBITDA incl OI is 673-742, a 26.3-28.0% margin (above the 24% base). Implied PAT is about 509, or about 493 after a post-tax 11 refund strip (base 397). ROCE on the trailing four quarters is 19.68% (20.55% on average CE) against the 19% base: above, by less. The review already shows that figure (rev l.389).
Survives: NO. The claim holds on every seasonal basis in the extract. Side observation, not a finding: the FY25 seasonal share implies FY27 EBITDA of about 673, almost exactly the 675 guide midpoint.

### Mandatory acquisition-economics probe
No acquisition, business purchase or third-party stake buy appears in either document. The only investment in an entity is 0.52 into a wholly owned subsidiary (SA CF l.335/l.339). That subsidiary has nil revenue and an H1 loss of 0.38 (l.457), so consideration / target PAT = 0.52 / (-0.38), which is not meaningful. There is no seller and no earnings multiple to test. The review already asks its purpose (Q12). The Lubrizol "understanding ... we buy this much of resin" (L0820-L0821) is a supply commitment, not a purchase of a business. The review tests it as a possible take-or-pay (Q20). Probe: NOT APPLICABLE, with the reason stated.

---

## FINDINGS (tagged)

### FACTUAL
F1. Step 8C Q3 test thresholds (rev l.476-478) misstate their own meaning and are not like-for-like. Agent: A4.
- The bear sentence "at or below 19.5% ... That means no YoY margin gain in the weak quarter" (rev l.478) is wrong on the extract. Q3 FY26 was 18.9% INCLUDING other income: EBITDA 87 on revenue 459 (l.1010, l.1021, l.1024). Q3 FY26 ex-OI is therefore at most 18.95% [DERIVED]. A Q3 FY27 reading of 19.5% ex-OI and ex-refund is a YoY gain of at least 55 bps, and more on any positive Q3 FY26 other income (about 460 bps on the even H2 split in M1, illustration only [INFERENCE]).
- Both lines are half-year averages applied to Q3 alone: 19.49% is H2 FY26 ex-OI; 22.31% is the guide-implied H2 incl OI less Q2's other-income share. Q3 runs below its own half: by about 103 bps in FY25 (94/466 = 20.17% vs 215/1,014 = 21.20%) and about 410-416 bps in FY26 (18.95% vs 23.05-23.11%) [DERIVED; l.1010, l.1021-1024; rev l.257].
- On that seasonality, the guide-implied H2 of 25.12% incl OI is consistent with a Q3 of about 21.0-24.1% incl OI [DERIVED 25.12 - 4.16; 25.12 - 1.03]. That is about 18.2-21.3% ex-OI at the 2.81% other-income share, or about 15.4-18.5% if the 16 refund is inside the guide and is also stripped [DERIVED].
- So a Q3 on management's guide path can print at or below the 19.5% "bear" line. The 22.3% "bull" line sits above every guide-consistent Q3 on FY25-FY26 seasonality, so it marks a beat, not "the guidance midpoint" (rev l.477).
- Fix: rebuild the Q3 test like-for-like (Q3 FY27 vs Q3 FY26 with the M1 bound, or move the H2-based lines to the FY27 results as an H2 test). Fix both meaning sentences. Align every dependent cell in the same pass: 5.5C (rev l.365), 8E (rev l.988), Section C watchpoints (rev l.1033), M6 (rev l.1070), Step 9 Key Notes payloads (rev l.524), brief l.1112 and l.1141/l.1147, YAML monitorables (rev l.1229) and the analyst_note.

F2. Brief, Competition (rev l.1137): "Management now claims parity or better on many products [ASR]" is not supported. Agent: A4.
- The call states 80-85% of the global leader as the current level (L0498-L0501), 85-90% "in some cases" (L0505), and a 10-20% premium only for "certain products" (L0506-L0508). The answer is about architectural film (L0478) and excludes Chinese and Korean imports (L0502).
- This contradicts the review's own Step 4A #15 (rev l.730).
- Fix: state the levels as said. Note that a typical 80-85% level is consistent with, not a reversal of, the prior 10-15% discount record.

### MISSING
M1. Tripwire 3 (op EBITDA margin below 18% for 2 quarters) has no Q3 FY26 ex-OI bound. Agent: A4.
- The review uses the chart method to give Q4 FY26 a floor (at least 20.0%, rev l.256) but leaves Q3 FY26 at "18.9% headline (ex-OI ND)" (rev l.411, l.967). The same method bounds Q3 FY26 ex-OI = (87 - Q3 OI)/459: at most 18.95%. It is below 18% whenever Q3 FY26 other income exceeded about 4.4 (87 - 0.18 x 459) [DERIVED; l.1010, l.1024].
- Filed quarterly other income ran 13.38 to 19.72 (Q1 FY26 = 27.24 - 13.86; l.510-511). H2 FY26 other income was 37.60. For Q3 FY26 other income to be 4.4 or less, Q4 FY26 would need 33.2 or more, above every filed quarter.
- So the seasonal low quarter most likely already printed below the 18% line once [INFERENCE]. An even H2 split gives about 14.9%, as an illustration only [INFERENCE]. Tripwire 3 did not fire, because Q4 FY26 was at least 20.0%. But Q3 FY27 after the 16 refund strip is a live test of the line, not a remote one.
- Fix: add the bound to 6C row 3, 8C row 3 and Step 3. Symmetric with the Q4 floor (Rule J).

M2. The surviving bear counter AR1 is not in the review. Agent: A4.
- The refund strip cuts the two-year margin climb to +228 bps (H1, unconditional on the review's own H1 placement) and about +139 bps (Q2, if all 11 fell there). Q2 rupee EBITDA rises +18.7% over two years, not +26.0% [DERIVED above].
- Fix: graft into Step 2 answer 1 and Flag 13 (rev l.230, l.1052, YAML l.1259).

M3. Inventory composition is partly derivable, but the review calls it unverifiable (7A, rev l.898; Step 5 gap (a) and the missing-evidence list, rev l.345). Agent: A4.
- Consolidated H1 inventory build 71.74 (389.25 to 460.99, l.609) less the FG/WIP/stock-in-trade build of 26.45 (P&L l.518) leaves about 45.29 (63%) of raw material, stores and packing build [DERIVED].
- Standalone build 89.99 (l.247) less 44.37 (l.179) leaves 45.62, with parent FG/WIP up 44.37 [DERIVED].
- FG and stock-in-trade outside the parent, net of elimination, fell about 17.9 (26.45 - 44.37). That ties within FX to the review's 100.26 to 82.01 subsidiary stock at group cost [DERIVED].
- This partly verifies management's "deliberate raw-material build" (L0299-L0308) and narrows gap (a). Rule J symmetry: a pro-company fact left out.
- Fix: replace "composition unverifiable" with the derived split, with FX and elimination caveats. Update the missing-evidence list to "RM vs stores/spares vs pre-TPU split".

M4. Top-three concentration is shown only on the analyst's 30% [ASR] (rev l.487, l.777, l.1047, YAML l.1254). Agent: A4.
- The review's own rule says filed numbers win on conflict (rev l.7). The filed AR Note 31 figure is 34% (Notion record, rev l.487). On 34%, "a couple" at a half to a third of the top customer gives about 57-68% [DERIVED 34 + 2 x 11.33; 34 + 2 x 17].
- Fix: show both bases. The period of each figure is ND.

### CONTRADICTION
C1. 5.5C names the tracker signal "MPCB consent-to-operate status, Waluj plant" (rev l.366). Agent: A4.
- The review elsewhere holds the plant as ND: Q8 asks "At which plant?", with Waluj only as the bear answer (rev l.494). See also 6B row 9 (rev l.402), Flag 1 (rev l.1040) and M2 "plant named" (rev l.1066).
- The extract names Waluj only as the registered office (l.60, l.153). The company has two manufacturing locations (l.1150, l.1281).
- Fix: name the plant with its source, or drop "Waluj" from the signal name.

### STYLE (logged; no loop)
S1. Section B Step 1 (rev l.619): "(the deck carries the same, l.855)". l.855 is the media release (p17), not the deck. The deck p29 GHS row puts "50 Studios" in a cell that the text layer cannot assign to FY27E or medium-term (A1 R1409 tags medium-term; R1782 notes column displacement). Write "the release carries the same".
S2. The anchor l.1111 for the deck's "~20% CAGR" FY28-31 (rev l.620, l.630, l.1084) should be l.1115 (R1407).
S3. "she signed the results, l.369" (rev l.553): l.369 carries the title only. The name comes from the release, l.886 (A2 R1346). Cite both.
S4. "Booked at the US subsidiary" carries [ASR] (rev l.89, l.1099). The call says "our subsidiary ... as per the laws there" (L0539-L0540). "US" is a sound inference from the US-tariff context. Tag it [INFERENCE].
S5. 1-G reading (b) gives the subsidiaries' margin as 8.8% on the 286.63 total-revenue denominator (rev l.190). Reading (b)'s own premise puts their operating revenue at 262.86, which gives 9.6% [DERIVED 25.31/262.86]. No conclusion changes.
S6. Step 4 finance rate "75.6% [DERIVED 5.34 x 2 / 14.14]" (rev l.293). On the shown 14.14 it is 75.5%; 75.6% uses the unrounded 14.135. Show the unrounded denominator.
S7. Section B 0C (rev l.564) runs Q&A "to 1:08:10 (L0090-L0840)". L0840 is at 1:07:53, and 1:08:10 is the closing remark (L0841). Q&A to the hand-off is 57.95 min (84.5%). Cosmetic.
S8. Section B 0B (rev l.552): "Dr S.B. Garware per Notion". The release names him as Chairman and Managing Director (l.882, FILED). Use the filed source.
S9. The ledger preamble (rev l.18) covers slides at category level. For an auditable trail, list the content-light slides reviewed with no finding: pp20, 21, 23, 28, 30, 34, 36, 39, 41.

---

## VERDICT
INCOMPLETE. Loop back to A4.
- Gap: (F1, FACTUAL) Rebuild the Step 8C Q3 thresholds like-for-like for seasonality and fix both meaning sentences. 19.5% is a YoY gain, not "no YoY margin gain", because Q3 FY26 was 18.9% including other income (l.1021, l.1024). A guide-consistent Q3 can print at or below 19.5%. Align 5.5C, 8E, Section C, M6, the Step 9 payloads, brief l.1112/l.1141/l.1147, the YAML and the analyst_note.
- (F2, FACTUAL) Correct the brief's "parity or better on many products" to the stated 80-85% (L0498-L0508).
- (M1, MISSING) Add the Q3 FY26 ex-OI bound to tripwire 3: at most 18.95%, and below 18% unless Q3 other income was under 4.4.
- (M2, MISSING) Graft AR1: the two-year margin climb after the refund strip is +228 / about +139 bps.
- (M3, MISSING) Inventory split: about 45.3 of the 71.74 build is outside FG/WIP.
- (M4, MISSING) Show the top-three range on the filed 34% as well: about 57-68%.
- (C1, CONTRADICTION) Remove or source "Waluj plant" in 5.5C.
Coverage: PASS (no orphan rows, nothing missing from the ledgers). Arithmetic: PASS (no mismatch above rounding). No A2 or A3 loop is needed.

## STYLE NOTES
S1-S9 above, recorded for the record; no re-run on their account.

```yaml
stage: A5-adversary
company: "GRWRHITECH"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Two-year margin climb survives the base test: +297 bps Q2, +311 bps H1, Flag 13 ~+300 bps (rev l.230, l.1052)", counter: "11 Cr refund 'in our book' to date sits in H1 by the review's own reading; stripped, H1 two-year climb is +228 bps (369.72/1,328.61 = 27.83% vs 25.55%) and Q2 about +139 bps if all 11 fell in Q2 (178.00/695.53 = 25.59% vs 24.2%); Q2 rupee EBITDA +18.7% not +26.0%; still incl OI", source_line: "L0386-L0388; l.523-532; l.1010; l.1022", type: MISSING}
  - {claim: "Pricing power for the Strategic Premium: 85-120% of global players; brief 'parity or better on many products' (rev l.450, l.977, l.1137)", counter: "Stated current level is 80-85% of the leader for architectural film; 85-90% in some cases; premium only on certain products; excludes Chinese/Korean imports that dominate the economy tier; PPF lowest margin 20-25% with no duty imposed", source_line: "L0478; L0498-L0508; L0502; l.1347-1353; L0410-L0412; L0744", type: FACTUAL}
findings_by_type:
  factual:
    - "F1 (A4): Step 8C Q3 thresholds misread. 19.5% ex-OI ex-refund is a YoY gain of at least 55 bps vs Q3 FY26 18.9% incl OI (87/459, l.1010, l.1021, l.1024), not 'no YoY margin gain' (rev l.478). Both lines are H2 averages applied to Q3; Q3 ran about 103 bps (FY25) and 410-416 bps (FY26) below its half, so a guide-consistent Q3 is about 18.2-21.3% ex-OI (15.4-18.5% if the 16 refund is inside the guide) and can print in the 'bear' zone; 22.3% marks a beat, not the midpoint (rev l.477). Rebuild like-for-like and align 5.5C, 8E, Section C, M6, Step 9 payloads, brief l.1112/l.1141/l.1147, YAML, analyst_note"
    - "F2 (A4): Brief rev l.1137 'parity or better on many products' unsupported; call states 80-85% of the global leader (L0498-L0501), 85-90% in some cases (L0505), premium only for certain products (L0506-L0508), architectural context (L0478), excludes China/Korea imports (L0502); contradicts the review's own Step 4A #15 (rev l.730)"
  missing:
    - "M1 (A4): Tripwire 3 lacks the Q3 FY26 ex-OI bound: (87 - Q3 OI)/459 is at most 18.95% and below 18% whenever Q3 OI > 4.4, against filed quarterly OI 13.38-19.72 (l.510-511) and H2 FY26 OI 37.60; add to 6C row 3, 8C row 3, Step 3 (symmetric with the Q4 FY26 floor, rev l.256)"
    - "M2 (A4): Graft AR1: two-year margin climb after the refund strip is +228 bps H1 and about +139 bps Q2; Q2 rupee EBITDA +18.7% over two years; into Step 2 answer 1, Flag 13, YAML flags"
    - "M3 (A4): Inventory composition partly derivable, review says unverifiable (rev l.898, l.345): C build 71.74 (l.609) less FG/WIP/SIT build 26.45 (l.518) = about 45.29 non-FG; SA 89.99 (l.247) less 44.37 (l.179) = 45.62; partly verifies the raw-material build claim (L0299-L0308)"
    - "M4 (A4): Top-three concentration shown only on the ASR 30% (rev l.487, l.777, l.1047); on the filed AR Note 31 34% it is about 57-68%; the review's own rule says filed wins (rev l.7)"
  contradiction:
    - "C1 (A4): 5.5C signal 'MPCB consent-to-operate status, Waluj plant' (rev l.366) vs plant ND in Q8, 6B row 9, Flag 1, M2 (rev l.494, l.402, l.1040, l.1066); extract names Waluj only as the registered office (l.60, l.153)"
  style:
    - "S1: rev l.619 'the deck carries the same, l.855' -> l.855 is the release; deck p29 GHS cell column is ambiguous (R1409, R1782)"
    - "S2: anchor l.1111 for deck ~20% FY28-31 CAGR should be l.1115 (R1407)"
    - "S3: rev l.553 'she signed the results, l.369' -> l.369 has the title only; name from l.886"
    - "S4: 'US subsidiary' tagged [ASR] (rev l.89, l.1099); call says 'our subsidiary ... laws there' (L0539-L0540); tag [INFERENCE]"
    - "S5: 1-G reading (b) 8.8% uses 286.63; on reading (b)'s own 262.86 operating revenue it is 9.6%"
    - "S6: finance rate 75.6% shown as 5.34 x 2 / 14.14 (= 75.5%); show 14.135"
    - "S7: Q&A end 1:08:10 (L0841) vs L0840 at 1:07:53; 57.95 min, 84.5%"
    - "S8: CMD named from Notion; the release names him (l.882, FILED)"
    - "S9: list content-light slides reviewed with no finding (pp20, 21, 23, 28, 30, 34, 36, 39, 41)"
loop_back_to: "A4"
gap: "F1 rebuild Step 8C Q3 thresholds like-for-like for seasonality and fix both meaning sentences (19.5% is a YoY gain vs Q3 FY26 18.9% incl OI, l.1021/l.1024; a guide-consistent Q3 can print below it), aligning 5.5C, 8E, Section C, M6, Step 9 payloads, brief l.1112/l.1141/l.1147, YAML, analyst_note; F2 correct brief pricing to the stated 80-85% (L0498-L0508); M1 add Q3 FY26 ex-OI bound (at most 18.95%, below 18% unless Q3 OI < 4.4) to tripwire 3; M2 graft refund-stripped two-year margin climb (+228 bps H1, about +139 bps Q2); M3 add inventory split (about 45.3 of 71.74 build outside FG/WIP); M4 show top-three on filed 34% (about 57-68%); C1 drop or source 'Waluj plant' in 5.5C"
style_notes:
  - "S1 deck vs release anchor l.855 (rev l.619)"
  - "S2 anchor l.1111 -> l.1115"
  - "S3 name source l.886, not l.369"
  - "S4 'US subsidiary' is [INFERENCE], not [ASR]"
  - "S5 reading (b) margin denominator 262.86 gives 9.6%"
  - "S6 show unrounded 14.135 for the 75.6% rate"
  - "S7 Q&A end time L0840 1:07:53"
  - "S8 CMD name is FILED at l.882"
  - "S9 list no-finding slides explicitly"
analyst_note: "Coverage and arithmetic are clean: my fresh counts match both A2 ledgers and every derived metric I recomputed ties within rounding. The loop is about interpretation. The Q3 test in Step 8C, which the brief calls make-or-break, compares a Q3 print with half-year averages. Q3 is the seasonal low: on the deck chart it ran about 103 bps (FY25) and 416 bps (FY26) below its own half. A Q3 on management's guide path can therefore land at or under the 19.5% bear line. The stated meaning, no YoY gain, is wrong, because Q3 FY26 was 18.9% even with other income. The chart method A4 used for the Q4 FY26 floor also caps Q3 FY26 ex-OI at 18.95%. That is below the 18% tripwire unless Q3 other income was under 4.4, against at least 13.38 in every filed quarter. The refund strip cuts the two-year margin climb from about 300 bps to 139-228 bps. The brief overstates pricing: the call says 80-85% of the leader, with a premium only on certain products. The above-base call survives the seasonality test. The FY25 H1 share of EBITDA implies FY27 EBITDA near 673, close to the 675 guide midpoint."
```
