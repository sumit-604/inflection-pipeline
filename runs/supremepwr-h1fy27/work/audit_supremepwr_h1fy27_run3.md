# A5 ADVERSARY / COMPLETENESS AUDIT: SUPREMEPWR (Supreme Power Equipment Limited), H1 FY27 results

Auditor: A5 (claude-opus-5-5), fresh context. Audit date: 2026-10-17.
Inputs read: A4 review (runs/supremepwr-h1fy27/work/review_supremepwr_h1fy27.md, 771 lines, header says CORRECTION LOOP 2); A1 fulltext (extracted/supremepwr-results-h1fy27-fulltext.md, 1,193 lines); A1 structured (extracted/supremepwr-results-h1fy27-structured.md, R001-R554); A2 ledger (work/ledger_results_supremepwr_h1fy27.md). Source PDF, inputs/, A3 forensics and orchestrator notes NOT opened.
Anchor convention: "A4 L###" = review line; "FT L###" = A1 fulltext line; "R###" = A1 structured row; "LG L###" = ledger line. All money in Rs lakh unless stated as Rs Cr.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PLAIN-LANGUAGE BRIEF heading at A4 L654. Narrative: PRESENT (A4 L658-L667, 9 paragraph lines, about 400 words, real content). Sector: PRESENT (A4 L669-L674). Business model: PRESENT (A4 L676-L681). Competition: PRESENT (A4 L683-L687). Forward map: PRESENT (A4 L689-L695; six dated catalysts, each with a bull and a bear fork). **Gate: PASS.** Length note logged as STYLE S-4.

---

## 1. COVERAGE AUDIT

Fresh pass method: line-by-line read of FT L1-L1193 plus greps for date tokens (years 2009-2126, month names), qualifiers (audit / unaudited / note / subject to / if any / wherever / certif / limited review / asterisk), auditor-paragraph terms (emphasis / other matter / going concern / qualified / adverse), acquisition terms, and units lines. Each hit diffed against structured line anchors (grep "line N") and ledger M-row anchors (grep "LN").

| Category | A2 count | A5 fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Notes | 21 (LG L4) | 21: SA notes 1-8 (FT L294-L330), CON notes 1-9 (FT L658-L696), CF notes 2+2 (FT L1019-L1020, L1184-L1185) | none | PASS |
| Line items | 153 structured (LG L5) + line-item M rows (M01-M09 except M10/M11 are paras; M12-M15) | 155 structured-class: 153 + 2 blank "Paid up Equity Share Capital" rows (SA FT L909, text layer L199; CON FT L1083, text layer L572). All M-row line items re-found. Total line labels in six statements 170 vs ledger 168 | 2 rows absent from structured AND ledger | **FAIL, A2 (M-2)** |
| Zero-standing | 13 (+8 M) (LG L6) | 13 (+8 M): SA exceptional, SA CF gratuity FY26, provisions H1, purchase FY26, proceeds H1, FA incl CWIP H1, warrants H1; CON exceptional, tax adj H1FY27/H1FY26, forex, profit on sale H1, proceeds H1, warrants H1 | none (the 2 paid-up rows are blank, not dash; carried under line items) | PASS |
| Agenda items | 2 (LG L7) | 2 (FT L38-L43, L45-L48) | none | PASS |
| Auditor paragraphs | 9 (+M10, M11, M16, M17) (LG L8) | SA LRR 6 units (FT L90-L95, L97-L102, L104-L117, L119-L122, L124-L131, L136-L148); CON LRR 8 units (FT L432-L438, L440-L447, L449-L460, L462-L465, L467-L470, L472-L474, L476-L485, L489-L500). All anchored by R-rows, M10/M11/M16/M17, M32/M34. No EoM / Other Matter / Going Concern (grep nil) | none | PASS |
| Entities | 20 (+M18) (LG L9) | 21 | none | PASS |
| Forward | 10 (LG L10) | 10 (FT L312, L313, L314, L318, L321, L686, L819-L825, L849, L853, L856) | none | PASS |
| Dates | 35 (+M19-M32, 14 rows covering 26 lines) (LG L11) | 35 + the same 26 lines + 5 unanchored date-bearing line groups: FT L35 (meeting date repeat, twin R473 L30); FT L345-L346 (SA CF title, text layer, twin R486 L972); FT L511-L515 and L1036-L1040 (CON P&L column date headers, both copies; the SA P&L analog is M29); FT L815-L816 (certificate column "Utilized Amount till September 30, 2026") | 5 line groups absent from structured and ledger; LG L11 claims "all 26 now in M19-M32" | **FAIL, A2 (M-2)** |
| Qualifiers | 48 (+M19-M22, M33-M35) (LG L12) | 48 + same M rows + 9 unanchored text-layer copies of anchored qualifiers, the class A2 itself rowed as M33 (L516) and M35 (L401-L403): FT L154 (twin R511 L879), L209 (R514 L922), L272 (R515 L957), L344 (R524 L971), L506 (R531 L1033), L584 (R533 L1099), L636-L637 (R534 L1136), L715 (R545 L1149), L773-L777 (R546/R547 L1184-L1185; L773 "Notes;" sits inside A2's own declared sweep scope) | 9 line groups absent under A2's own loop-2 standard | **FAIL, A2 (M-2)** |
| ID integrity | 554 in structured, 554 referenced, orphans [] (LG L17) | R001-R554 all referenced by ledger ranges/lists (LG L23-L175, L181-L276); type counts 441/20/10/35/48 re-tallied | none | PASS |
| Ledger rows to A4 | 589 = 554 R + 35 M | A4 L16-L29: 156 cited + 138 routed + 295 reviewed-no-finding = 589; 416 (6b) + 154 (6c) + 19 (6d) = 589; notes (A4 L25) and M12-M35 (A4 L26-L27) dispositioned by ID; M01-M11 cited at A4 L28, L56, L101, L111, L126 | 0 on A4's attestation | PASS (method note S-7) |

**Ledger-to-A4 method note.** 280 R rows carry "reviewed, no finding" only by category reference to the A3 section 6b register (A4 L21). Spot check: R002, R087, R173, R293, R381, R408, R419, R432, R435, R440, R441, R447, R451, R459-R461, R497, R505, R508, R513, R548-R550, R552 are absent from A4 text and rest on that register. Input discipline bars A5 from A3, so per-ID verification is not possible here; the category totals tie exactly. Not raised as a FAIL because A4 marks the set explicitly and the totals reconcile; logged as S-7.

**M-2 content materiality.** Every orphan in the dates and qualifiers rows duplicates the content of an anchored row (twins listed above). The paid-up rows are blank in every column; A4 already read them and routed them to A1 (A4 L56, L82). No A4 number, fact or conclusion depends on any orphan. The FAIL stands because the coverage rule is absolute and the ledger count test (LG L5, L11, L12) asserts a completeness the fresh pass does not reproduce. The fix is mechanical (see Findings).

---

## 2. ARITHMETIC AUDIT

All recomputed from A1 lakh values. Status PASS = within rounding of the last shown digit.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| SA Op EBITDA H1FY26 / H2FY26 / H1FY27 / FY26 | 12.53 / 16.12 / 21.37 / 28.65 Cr (A4 L168) | 1,252.84 / 1,612.36 / 2,136.89 / 2,865.20 | FT L901, L892, L891, L884 | PASS |
| SA Op EBITDA margin | 15.53 / 14.74 / 16.81 / 15.07% | 15.532 / 14.736 / 16.808 / 15.074% | FT L883 | PASS |
| SA reported EBITDA, core PBT | 13.49/17.49/22.67/30.99; 11.31/13.28/16.57/24.58 | 1,349.40/1,749.31/2,267.08/3,098.71; 1,130.68/1,327.68/1,657.48/2,458.36 | FT L884-L901 | PASS |
| SA OI / PBT | 7.87 / 9.35 / 7.28 / 8.67% | 7.868 / 9.350 / 7.283 / 8.675% | FT L884, L901 | PASS |
| SA ETR | 23.33 / 24.68 / 23.64 / 24.07% | 286.36/1,227.24 = 23.334; 361.45/1,464.63 = 24.679; 422.57/1,787.67 = 23.638; 647.81/2,691.87 = 24.065% | FT L903-L904 | PASS (H1FY26 DT read as 0.30 credit: 1,227.24 - 286.36 = 940.88 vs PAT 940.87; H1 + H2 DT 117.36 - 0.30 = 117.06 = FY26) |
| SA PAT margin, gross margin | 11.66/10.08/10.74/10.75; 22.36/20.99/24.67/21.57% | 11.665/10.082/10.737/10.754; 22.360/20.986/24.671/21.569% | FT L883, L887-L888, L194 | PASS |
| SA total expenses H1FY27 | ND (A4 L153) | Line sum 11,056.61 vs TI - PBT 11,056.31 (0.30 residual); R043 11,086.31 fails | FT L885-L894 | PASS (ND correct) |
| CON Op EBITDA | 14.11 / 18.71 / 23.35 / 32.82 Cr (A4 L209) | 1,411.31 / 1,871.11 / 2,335.45 / 3,282.42 | FT L1064, L1051, L1050, L1043 | PASS |
| CON Op EBITDA margin | 18.77 / 17.58 / 17.26 / 18.07% | 18.769 / 17.578 / 17.260 / 18.071% | FT L1042 | PASS |
| CON ETR | 26.17 / 28.59 / 26.19 / 27.50% | 336.81/1,287.07 = 26.169; 447.29/1,564.59 = 28.588; 488.72/1,866.01 = 26.191; 784.10/2,851.66 = 27.496% | FT L1067-L1071 | PASS |
| CON PAT margin, gross margin | 12.64/10.50/10.18/11.38; 26.51/24.72/25.22/25.46% | 12.637/10.496/10.179/11.383; 26.508/24.718/25.223/25.459% | FT L1042-L1072 | PASS |
| CON PAT ties | 1,377.29 / 1,117.29 / 950.26 / 2,067.56 | 1,866.01-411.44-77.28; 1,564.59-329.27-117.65-0.37 = 1,117.30; 1,287.07-337.01+0.20; 2,851.66-666.28-117.45-0.37 | FT L1064-L1072 | PASS (prior-year tax as A4 reads it) |
| S-v-C revenue gap | (5.47)/(2.97)/(8.44)/+8.17 Cr (A4 L225) | -546.66 / -297.03 / -843.69 / +817.12 | FT L883 vs L1042 | PASS |
| S-v-C purchases gap | -263.45/-352.19/-615.62/+588.77 | same | FT L887 vs L1046 | PASS |
| Inventory build gap; implied Danya stock | 472.94/279.81/752.75/48.03; 1,653.47 / 1,701.50 | same; 6,209.72-4,556.25; 8,745.50-7,044.00 | FT L888 vs L1047; L953 vs L1131 | PASS |
| Other creditors gap | (4.48) / (0.81) Cr | 2,627.00-3,074.78 = -447.78; 4,376.18-4,457.00 = -80.82 | FT L939 vs L1118 | PASS |
| Op EBITDA gap and % of SA PAT | 1.58/2.59/4.17/1.99 Cr; 16.8/23.5/20.4/14.5% | 158.47/258.75/417.22/198.56; 16.84/23.46/20.41/14.55% | derived | PASS |
| Danya PAT (MI x 10) and % CON PAT | 0.94/1.41/2.35/1.22 Cr; 9.9/12.6/11.4/8.85% | 93.9/141.1/235.0/121.9; 9.88/12.63/11.37/8.85% | FT L1073, L1072 | PASS |
| Implied Danya employee cost | 0.66/(0.44)/0.22/0.11 Cr | 66.04/-43.59/22.45/10.92 | FT L890 vs L1049 | PASS |
| Receivables build CON minus SA | at least 8.65 Cr (8.65 / 8.68 / 11.68) | 1,583.64-718.82 = 864.82; -715.82 = 867.82; -415.82 = 1,167.82 | FT L1164, L988, L954 | PASS |
| CON YoY (rev, Op EBITDA, margin, D&A, FC, EBIT, core PBT, PBT, PAT, owners, EPS) | 79.95%, 65.48%, -151 bps, 415.4%, 189.5%, 55.38%, 44.74%, 44.98%, 44.94%, 45.09%, 45.21% (A4 L262-L273) | 79.946, 65.481, -150.9 bps, 415.40, 189.47, 55.379, 44.744, 44.981, 44.938, 45.089, 45.213 | FT L1042-L1080 | PASS |
| SA YoY (same set) | 57.62%, 70.56%, +128 bps, 468.1%, 221.7%, 59.11%, 46.59%, 45.67%, 45.09% (A4 L278-L287) | 57.620, 70.564, +127.5 bps, 468.13, 221.67, 59.111, 46.592, 45.666, 45.088 | FT L883-L907 | PASS |
| Gross margin YoY | CON -129 bps; SA +231 bps (A4 L294) | -128.5; +231.1 | derived | PASS |
| HoH (A4 L324) | CON rev 41.56 / 27.12%; SA 35.65 / 16.20%; core PBT 19.87 / 24.84% | 41.561 / 27.115; 35.650 / 16.197; 19.870 / 24.840 | FT L883, L1042 | PASS |
| CON PAT bridge (A4 L343-L356) | +15.94, -1.74, -4.96, -1.65, -1.91, +0.10, -1.52, -0.00; PAT +4.27 | 1,593.55 - 173.88 - 495.53 - 164.50 - 190.99 + 10.29 = 578.94 PBT; tax 151.50 + 0.41; PAT 427.03 | FT L1042-L1072 | PASS |
| SA PAT bridge (A4 L361-L372) | +10.39, +2.94, -4.49, -1.64, -1.93, +0.34, -1.31, -0.05; PAT +4.24 | 1,039.21 + 293.81 - 448.97 - 164.22 - 193.03 + 33.63 = 560.43; tax 130.77 + 5.44; PAT 424.22 | FT L883-L907 | PASS |
| D&A + FC as % of CON revenue (A4 L308, L679) | 1.87% to 3.67% | 140.40/7,519.44 = 1.867%; 495.89/13,530.91 = 3.6649% = 3.66% | FT L1050-L1051, L1042 | STYLE S-1 (rounding of rounded Cr inputs) |
| CON CFO, CFO/PAT, FCF | 25.90 / (5.74); 1.25x / -0.42x; (31.58) / (14.42) | 2,590.47 / -573.76; 1.253 / -0.417; -3,157.57 / -1,441.61 | FT L750, L752 | PASS |
| CON WC change | +2.82 / (26.75) Cr | +282.35 / -2,675.10 (3,155.53 + 282.35 = 3,437.88 vs 3,437.89) | FT L1164-L1169 | PASS |
| CON receivable / inventory / payable days, CCC | 80.10/84.77; 141.04/158.18; 116.77/122.34; 104.36/120.61 | 80.095/84.774; 141.035/158.177; 116.766/122.339; 104.364/120.612 | FT L1132, L1131, L1116-L1118 | PASS |
| CON gross debt, net debt | 49.97/57.45; 40.23/57.20 (+42.2%) | 4,997.30/5,744.56; 4,022.75/5,719.75 (+42.19%) | FT L1110, L1114, L1133 | PASS |
| CON balance sheet foots | (implied) | 30,574.82 vs 30,574.83; 26,139.11 vs 26,139.10 | FT L1105-L1135 | PASS |
| SA CFO/PAT, FCF | 1.36x / -0.38x; (29.73) / (13.79) | 1.357 / -0.383; -2,973.10 / -1,378.81 | FT L999, L1003, L1006 | PASS |
| SA WC change | +4.71; (24.16) A3-13 / (24.19) as extracted | +471.18; -2,415.67 / -2,418.67 (2,110.46 - 2,415.67 = -305.21 vs -305.20) | FT L987-L994 | PASS |
| SA days, CCC | inv 95.92/134.60; pay 107.86/114.68; rec 75.38; CCC 95.30 | 95.917/134.596; 107.855/114.680; 75.379; 95.295 | FT L953-L954, L937-L939 | PASS |
| SA payables tie, net debt, ND/NW | 5,954.07 to 7,560.72 = +1,606.65; 35.99/54.80 (+52.3%); 0.32x/0.43x | ties CF FT L991; 3,598.91/5,480.18 (+52.27%); 0.319/0.433 | FT L930-L955 | PASS |
| SA BS foots | Mar-26 24,873.69 vs 24,873.68 at 4,521.09; Sep-26 28,802.45 | both sides re-added: same | FT L926-L956 | PASS |
| SA OCA BS change vs CF | 739.73 vs 521.97, gap 217.76 = taxes paid | same | FT L956, L990, L998 | PASS |
| ROCE (indicative) | SA 23.6%; CON 23.6% (24.1% ex MI); with payables 17.0% / 16.8% | 4,135.56/17,540.62 = 23.58%; 4,315.60/18,277.01 = 23.61%; /17,874.15 = 24.14%; 4,135.56/24,298.01 = 17.02%; 4,315.60/25,616.66 = 16.85% | FT L926-L941, L1105-L1120 | PASS |
| MSE days bound | 42.0 / 52.7; GST 35.6 / 44.7 | 3,103.72/13,511.53 x 183 = 42.04; 4,083.10/14,178.90 x 183 = 52.70; /1.18 = 35.62 / 44.66 | FT L937, L1116, L887-L893, L1003, L1046-L1052, L752 | PASS |
| 5-D capital roll, multiple, yield | 12.68 to 16.52 Cr (+30.3%); 7.5x; 13.3% | 1,267.73 + 274.59 + 109.73 = 1,652.05 (+30.32%); 1,652.05/219.46 = 7.53x; 13.28% | FT L950, L1007, L983 | PASS |
| 5-D Danya PBT, returns, tax | 188.07; 18.3% / 18.2%; 35.2% | 1,866.01 - 1,787.67 + 109.73 = 188.07; 376.14/2,051.00 = 18.34%; 399.50/2,196.28 = 18.19%; 66.15/188.07 = 35.17% | FT L1055, L896, L1050, L891 | PASS |
| 5-D funding cost; debt shift | 11.1% / 8.3%; -296.45 / +114.32 / -182.13 | 560.22/5,037.40 = 11.12%; 3,526.02-3,504.67 vs 3,311.60-2,993.80; 2,218.54-1,997.42 vs 1,685.70-1,578.90 | FT L891, L930, L934, L1110, L1114 | PASS |
| MI capital roll (A5 extra tie) | n.a. | 406.76 + 12.19 - 20.00 = 398.95 | FT L1108, L1073, L1180 | PASS |
| **Unrealised profit, FY26 "upper bound"** (A4 L304) | at most 162.4 lakh (Rs 1.62 Cr), 5.7% of FY26 CON PBT | Maximum on A4's own 21.57% proxy is 1,653.47 x 21.57% = 356.65 lakh (Rs 3.57 Cr), 12.5% of 2,851.66, reached if Danya's Mar-25 stock carried no parent margin. 162.4 is a constant-mix estimate, not a bound | FT L953 vs L1131; L883, L887, L888; L1055 | **FAIL (FACTUAL, F-1)** |
| **Unrealised profit, H1FY27 "at most"** (A4 L305, L375) | at most 11.85 lakh (Rs 0.12 Cr) | Range -356.65 to +419.76 lakh (1,701.50 x 24.67%); +419.76 = 22.5% of H1FY27 CON PBT 1,866.01. Even at 100% parent-sourced stock on both dates, A4's own proxies give 1,701.50 x 24.67% - 1,653.47 x 21.57% = +63.14 lakh (Rs 0.63 Cr), 5.3 times A4's figure | FT L953, L1131, L883, L887-L888, L1064 | **FAIL (FACTUAL, F-1)** |
| **Unrealised profit, H1FY26 base** (A4 L305) | up to 105.75 lakh | Not boundable from the filing: Danya stock at 30-Sep-25 is not filed (A4 L228 itself marks it ND) | A4 L228 | **FAIL (FACTUAL, F-1)** |

Supporting fact for F-1: CON reserves equal SA reserves at both dates (10,159.80 and 8,794.70; FT L927 vs L1106, R093/R094 vs R299/R300). No unrealised profit has been eliminated cumulatively, so the whole margin, whatever it is, on parent-sourced goods in Danya's stock sits in group equity at each date. The P&L effect of a half equals the change in that stock-level figure. It depends on the parent-sourced share and the transfer margin at both dates, not only on the change in stock.

---

## 3. ADVERSARIAL READ

### Claim 1. "Growth is real at PBT": CON core PBT +44.74%, PAT +45% "is real at the PBT level; it is not driven by other income" (A4 L295, L768).
Strongest bear counter from the extract: (a) the growth is accrual only. CFO was -573.76 against group PAT 1,377.29 (FT L750, L1072), and working capital absorbed 2,675.10 (FT L1164-L1169). (b) Group PBT includes Danya's PBT of 188.07 (10.1% of CON PBT), and Danya's figures are unaudited with an unresolved review bracket (FT L472-L474, L684). (c) Group PBT carries an unsigned unrealised intercompany margin term. No elimination was made in any period (FT L194 vs L1074; L927 vs L1106). On A4's proxy margins the H1FY27 term lies between -3.57 and +4.20 Cr, the top end being 22.5% of CON PBT. The H1FY26 term is unknown. So the core PBT growth rate cannot be signed clean of this item.
Survives? (a) and (b) are already in A4 (Step 5 A4 L391-L399, 0D A4 L106, verdict A4 L648). **(c) survives and is not in A4**; it is grafted through F-1.

### Claim 2. "H1FY27 growth is not inflated by this item ... at most Rs 0.12 Cr ... If anything, the YoY comparison is understated" (A4 L305; repeated A4 L375, L525, L648, L666, L757, L768).
Strongest bear counter: the bound multiplies the change in Danya stock (48.03, FT L1047 vs L888) by a margin. That is valid only if the parent-sourced share and the transfer margin were the same on 31-Mar-26 and 30-Sep-26. The filing constrains neither. A4 itself says two-way flow in H1FY27 "can be neither shown nor excluded" (A4 L248). By A4's own proxies the margin rose from 21.57% (FY26) to 24.67% (H1FY27), so a fully parent-sourced stock gives +63.14 lakh, not +11.85. The extract-supported range is -356.65 to +419.76 lakh. **Survives. Must be grafted (F-1, FACTUAL, A4).** The defensible statement: the filing cannot sign or size the H1FY27 effect beyond plus or minus (Danya stock x transfer margin); Q21 (A4 L609) is the separating observation.

### Claim 3. "The parent earns 13.3% post-tax on its Danya capital, above its after-tax cost of debt" by about 5 pp (A4 L451, L455, L461, L680).
Strongest bear counter: the 13.3% is an accrual credited to the capital account, not cash. In the half the parent paid in 274.59 and received no distribution (1,267.73 + 274.59 + 109.73 = 1,652.05; FT L950, L1007, L983). The partners drew 20.00 (FT L1180). The yield is set by related-party transfer prices with goods moving both ways (FY26 floors 843.69 and 615.62; FT L883 vs L1042, L887 vs L1046), and rests on unaudited figures (FT L684).
Survives? Yes, but it is **already incorporated** in A4 Step 5-D (A4 L450 "profit share left in", L458 two-way trade, L459 assurance, L461 bear reading). No graft. The brief line A4 L680 omits the accrual and related-party caveat: STYLE S-6.

### Mandatory acquisition-economics probe
The extract describes no acquisition, business purchase or stake buy (grep "acqui|stake|takeover|merger|amalgamat" nil; the only subsidiary references are FT L434-L477, L673-L683, L766, L1180). A4 ran the probe on the parent's capital in Danya (A4 L446-L461). Re-derived: Rs 16.52 Cr capital / Rs 2.19 Cr annualised H1FY27 profit share (109.73 x 2) = about 7.5x. On the audited FY26 share (90% x 235.0 = 211.5): Rs 12.68 Cr Mar-26 capital = 6.0x, Rs 16.52 Cr Sep-26 capital = 7.8x. Representative or peak: Danya PAT 0.94 / 1.41 (unassured) / 1.22 Cr by half; H1FY27 annualised 2.44 vs FY26 2.35, so the base is not a peak. Quality markers are weak: cash 2.90 lakh (FT L1133 vs L955), debt 242.47 at Sep-26, stock Rs 17.02 Cr, pre-tax return 18.2-18.3% vs group 23.6%, tax 35.2%, unaudited. This is not a cheap high-quality asset. The multiple is fair for a stock-heavy, cash-poor related-party firm, and A4's bear reading (A4 L461) already carries this. No further graft.

---

## FINDINGS (tagged)

**F-1. FACTUAL. Route A4.** Unrealised-profit bounds mis-derived. A4 calls 752.75 x 21.57% = 162.4 lakh an "upper bound" on the FY26 effect (A4 L304). It calls 48.03 x 24.67% = 11.85 lakh the most H1FY27 can carry (A4 L305). It then concludes "H1FY27 growth is not inflated" and "the YoY comparison is understated" (A4 L305). The change in stock times a margin is a constant-mix estimate. Correct figures on A4's own proxy margins:
- FY26 maximum: 356.65 lakh (Rs 3.57 Cr, 12.5% of FY26 CON PBT).
- H1FY27 range: -356.65 to +419.76 lakh (up to Rs 4.20 Cr, 22.5% of H1FY27 CON PBT).
- H1FY27 at 100% parent sourcing on both dates: +63.14 lakh (Rs 0.63 Cr).
- H1FY26 base: not boundable (Danya stock at 30-Sep-25 not filed, A4 L228).
Fix: replace "upper bound / at most" with the constant-mix estimate plus the true range. Withdraw "not inflated" and "understated". Carry the change to every restatement: A4 L375, L438, L525, L609 (Q21 why-it-matters), L648, L666 (brief), L757, L768.

**C-1. CONTRADICTION. Route A4.** A4 L243 defines CON revenue as SA revenue plus Danya's external revenue less the parent's sales to Danya. A4 L248 says two-way flow in H1FY27 "can be neither shown nor excluded". Yet A4 L662 states "Sales booked outside the parent were Rs 8.17 Cr ... That money had not come in". A4 L648 flags "revenue booked outside the parent not collected (... against Rs 8.17 Cr revenue)", and A4 L296 concludes "that revenue was not collected". By A4's own identity, Danya's external sales were 8.17 Cr plus the parent's H1FY27 sales into Danya, at least 8.17 Cr and undisclosed. The receivables build of at least 8.65 Cr means "not collected" only if the parent sold nothing into Danya in the half. Fix: restate 8.17 Cr as the CON-minus-SA revenue gap. Add reading 3 to bear counter 1 (Danya's external sales exceed 8.17 Cr by the parent's sales into Danya, so the build is a smaller share of them). Make A4 L648 and L662 conditional. Rule J symmetric bar: a bear claim needs the same qualifier a bull claim would.

**M-2. MISSING. Route A2 (then A3 disposition).** Fresh-pass units absent from both structured file and ledger:
- (a) blank "Paid up Equity Share Capital" line items in the SA P&L (FT L909; text layer L199) and the CON P&L (FT L1083; text layer L572).
- (b) date-bearing lines FT L35, L345-L346, L511-L515, L1036-L1040, L815-L816.
- (c) text-layer qualifier copies FT L154, L209, L272, L344, L506, L584, L636-L637, L715, L773-L777.
Groups (b) and (c) are the same classes A2 rowed in loop 2 (M29 column date header, M32 repeat date mentions, M33 and M35 text-layer copies). The ledger count test (LG L5, L11, L12) therefore overstates completeness. Fix: add M rows for (a). For (b) and (c), either add M rows, or state a one-anchor-per-unit rule (text-layer duplicates are not separate units) and correct the LG L11-L12 claims to match. A3 disposes of the new IDs. A4 has already read (a) at A4 L56, so no A4 content change is needed beyond the register count. Content materiality: nil; every orphan duplicates an anchored row or is blank.

---

## VERDICT

**INCOMPLETE.** Earliest looping agent: A2 (M-2, MISSING: ledger lacks fresh-pass units listed above). Then A3 (dispose of the new IDs), then A4 (F-1, FACTUAL: unrealised-profit "upper bound" and "H1FY27 not inflated" are mis-derived and unsupported by the extract; C-1, CONTRADICTION: Rs 8.17 Cr treated as Danya's external sales and called uncollected against A4's own L243/L248). Arithmetic is otherwise clean: every other A4 table cell, bridge, ratio and day count ties within rounding. The protocol verdict (PROCEED WITH FLAGS) is not affected by any finding; the flag wording is.

---

## STYLE NOTES (logged, no loop)

- **S-1.** D&A + finance cost share of CON revenue reads 3.67% (A4 L308, L679); on lakh inputs it is 3.6649% = 3.66%. Use 3.66% or say "about 3.7%".
- **S-2.** A4 L308 "FY26 capex Rs 57.48 Cr (R378) plus CWIP Rs 31.91 Cr still not earning" reads as additive; part of the CWIP is inside FY26 capex. Write "of which Rs 31.91 Cr sits in CWIP at 30-Sep-26 and is not yet earning" (A4 L660 already phrases it correctly).
- **S-3.** The A1 routing list (A4 L56) omits R114 (28,736.9?) and R136 (34,873.69?). The Mar-26 SA balance sheet foots at 24,873.69 on the A3-13 reading, so both A1 totals are misreads. A4 uses neither; add them for A1.
- **S-4.** Summary narrative is 9 paragraph lines (A4 L659-L667, about 400 words) against the 10-20 line spec for a Quarterly Results review. Content is complete; splitting one paragraph meets the letter.
- **S-5.** Brief house style. Hyphenated compound modifiers: "single-segment" (A4 L670), "cash-rich" (A4 L686), "Make-or-break" (A4 L690). Sentences over 20 words: A4 L660 sentence 2 (25 words), A4 L686 sentence 2 (23 words).
- **S-6.** Brief line A4 L680 ("Capital sent to Danya earns 13.3% after tax ...") should say the return is accrued at related-party prices and not received in cash. The parent paid in Rs 2.75 Cr and received nothing in the half (A4 L450 carries it).
- **S-7.** Coverage method: 280 R rows are dispositioned "reviewed, no finding" only by category reference to the A3 6b register (A4 L21). Append them as ID ranges so A5 can verify per ID without opening A3.

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
  missing_from_ledger:
    - "Paid up Equity Share Capital, SA P&L, blank all columns (FT L909; text layer L199)"
    - "Paid up Equity Share Capital, CON P&L, blank all columns (FT L1083; text layer L572)"
    - "Date lines unanchored: FT L35 (meeting date repeat), L345-L346 (SA CF title, text layer), L511-L515 and L1036-L1040 (CON P&L column date headers), L815-L816 (certificate utilised-column date)"
    - "Text-layer qualifier copies unanchored (class of M33/M35): FT L154, L209, L272, L344, L506, L584, L636-L637, L715, L773-L777"
arithmetic_mismatches:
  - {metric: "Unrealised profit in Danya stock, FY26 effect 'upper bound'", a4_value: "at most 162.4 lakh (Rs 1.62 Cr), 5.7% of FY26 CON PBT (A4 L304)", recomputed: "max 1,653.47 x 21.57% = 356.65 lakh (Rs 3.57 Cr), 12.5% of FY26 CON PBT; 162.4 is a constant-mix estimate", source_line: "FT L953 vs L1131; L883, L887, L888; L1055"}
  - {metric: "Unrealised profit, H1FY27 effect 'at most'", a4_value: "at most 11.85 lakh (Rs 0.12 Cr) (A4 L305, L375)", recomputed: "range -356.65 to +419.76 lakh (up to 22.5% of H1FY27 CON PBT); +63.14 lakh even at 100% parent-sourced stock on A4's own proxy margins (1,701.50 x 24.67% - 1,653.47 x 21.57%)", source_line: "FT L953, L1131, L883, L887-L888, L1064"}
  - {metric: "Unrealised profit, H1FY26 base", a4_value: "up to 105.75 lakh (A4 L305)", recomputed: "not boundable; Danya stock at 30-Sep-25 not filed (A4 L228 marks it ND)", source_line: "A4 L228"}
surviving_bear_counters:
  - {claim: "H1FY27 growth is not inflated by unrealised profit; at most Rs 0.12 Cr; YoY if anything understated (A4 L305, L375, L666, L757)", counter: "Bound valid only at constant parent-sourced share and transfer margin; filing constrains neither (A4 L248); range -3.57 to +4.20 Cr; +0.63 Cr even at full parent sourcing on A4's proxies; CON reserves equal SA reserves at both dates so the full stock-level margin sits in group equity", source_line: "FT L953, L1131, L194 vs L1074, L927 vs L1106", type: FACTUAL}
  - {claim: "Growth is real at PBT: CON core PBT +44.74%, PAT +45% (A4 L295, L768)", counter: "Cash and unaudited-Danya counters already in A4; surviving part: group PBT carries an unsigned unrealised-margin term of up to Rs 4.20 Cr (22.5% of H1FY27 CON PBT), H1FY26 term unknown, so clean core PBT growth cannot be signed until Q21 is answered", source_line: "FT L194 vs L1074, L927 vs L1106, L1131, L953", type: FACTUAL}
findings_by_type:
  factual:
    - {id: F-1, route: A4, gap: "Unrealised-profit 'upper bound' (FY26 Rs 1.62 Cr) and 'at most Rs 0.12 Cr' (H1FY27) are constant-mix estimates, not bounds; 'H1FY27 not inflated' and 'YoY understated' unsupported. Correct: FY26 max Rs 3.57 Cr; H1FY27 -3.57 to +4.20 Cr; +0.63 Cr at full parent sourcing; H1FY26 unboundable", lines: "A4 L304-L305, L375, L438, L525, L609, L648, L666, L757, L768"}
  missing:
    - {id: M-2, route: A2, gap: "Fresh-pass units absent from structured and ledger: blank Paid up Equity Share Capital rows (FT L909/L199, L1083/L572); date lines FT L35, L345-L346, L511-L515, L1036-L1040, L815-L816; text-layer qualifier copies FT L154, L209, L272, L344, L506, L584, L636-L637, L715, L773-L777. Ledger count test overstates completeness (LG L5, L11, L12). Content materiality nil", lines: "LG L5, L11, L12"}
  contradiction:
    - {id: C-1, route: A4, gap: "Rs 8.17 Cr CON-minus-SA revenue gap stated as 'sales booked outside the parent' and called uncollected, against A4's own identity (L243) and caveat that H1FY27 parent-to-Danya sales cannot be excluded (L248); Danya external sales are 8.17 Cr plus undisclosed parent sales into Danya; add reading 3, make L648/L662 conditional", lines: "A4 L243, L248, L296, L648, L662"}
  style:
    - "S-1 D&A + FC share of CON revenue 3.67% should be 3.66% on lakh inputs (A4 L308, L679)"
    - "S-2 'FY26 capex plus CWIP' reads additive (A4 L308)"
    - "S-3 A1 routing list omits R114 and R136 misread Mar-26 SA totals; foots at 24,873.69 (A4 L56)"
    - "S-4 Summary narrative 9 paragraph lines vs 10-20 line spec (A4 L659-L667)"
    - "S-5 Brief hyphenated compound modifiers (A4 L670, L686, L690) and sentences over 20 words (A4 L660, L686)"
    - "S-6 Brief 13.3% Danya return line omits accrual and related-party caveat (A4 L680)"
    - "S-7 280 R rows dispositioned only by category reference to A3 6b; append ID ranges (A4 L21)"
loop_back_to: "A2"
gap: "A2 (M-2, MISSING): add ledger rows for blank Paid up Equity Share Capital lines (FT L909/L199, L1083/L572) and either row or rule out (one-anchor-per-unit) the unanchored date/qualifier duplicates, correcting LG L11-L12. A3: dispose of new IDs. A4 (F-1, FACTUAL): replace unrealised-profit 'upper bound/at most' with FY26 max Rs 3.57 Cr and H1FY27 range -3.57 to +4.20 Cr, withdraw 'H1FY27 not inflated' across A4 L304-L305, L375, L438, L525, L609, L648, L666, L757, L768. A4 (C-1, CONTRADICTION): restate Rs 8.17 Cr as the CON-minus-SA gap and add reading 3 to bear counter 1 (A4 L296, L648, L662)."
style_notes:
  - "S-1 3.67% to 3.66% (A4 L308, L679)"
  - "S-2 capex plus CWIP wording (A4 L308)"
  - "S-3 add R114/R136 to A1 routing list (A4 L56)"
  - "S-4 narrative line count (A4 L659-L667)"
  - "S-5 brief hyphens and long sentences (A4 L660, L670, L686, L690)"
  - "S-6 brief Danya return caveat (A4 L680)"
  - "S-7 list A3 6b IDs as ranges in A4 (A4 L21)"
analyst_note: "Numbers are clean: every other A4 cell, bridge, ratio and day count recomputed from A1 lakh values ties within rounding, and the CON and SA balance sheets and CON cash flow foot. The loop is driven by one logic error and one dropped qualifier. A4's unrealised-profit bound multiplies the change in Danya stock by a margin; that holds only if the parent-sourced share and transfer margin were the same at both dates, and the filing constrains neither. CON reserves equal SA reserves at both dates (FT L927 vs L1106), so the whole margin on parent-sourced goods in Danya's stock, whatever it is, sits in group equity. On A4's own proxy margins the H1FY27 effect spans about -Rs 3.57 Cr to +Rs 4.20 Cr and is +Rs 0.63 Cr even at full parent sourcing. The claim 'H1FY27 not inflated' must go; Q21 already names the separating observation. The A2 gaps are bookkeeping: each duplicates an anchored row or is blank and already read by A4 (L56). Ledger-to-A4 coverage rests on A4's attestation of the A3 6b register, which input discipline keeps from A5; totals tie at 589. Protocol verdict unaffected."
```
