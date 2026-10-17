# A5 ADVERSARY / COMPLETENESS AUDIT: Heritage Foods Limited (HERITGFOOD) | Q2 FY27 | LOOP 2 RE-AUDIT

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-17 | loop: 2
Under audit: runs/heritgfood-q2fy27/work/review_heritgfood_q2fy27.md (986 lines, loop-2 revision)
Prior audits checked for resolution: work/audit_heritgfood_q2fy27_run1.md (run 1) and work/audit_heritgfood_q2fy27_loop1.md (loop 1)
Inputs read: A1 fulltexts in full (results 782 lines, presentation 1,328, press release 230); A1 structured files (press release rows R001-R144 in full; presentation and results by targeted row lookups and ID counts); A2 ledgers (count tests, flagged rows, notes, entities, dates, auditor sections); A4 review in full.
Not read: source PDFs, anything under inputs/, A3 forensics. No Grep in this run touched work/forensics_*.

Anchor key: L### = results fulltext; P-l### = presentation fulltext; PR-L### = press release fulltext; R-L### = line of the loop-2 A4 review; R### = A1 structured row. Rs Cr unless marked Rs m.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PLAIN-LANGUAGE BRIEF at R-L791-852.

| Part | Location | Status | Note |
|---|---|---|---|
| (1) Summary narrative | R-L795-812 | PRESENT | 16 lines, within 10-20; carries the seasonal, cash-conversion and price-share counters |
| (2) Sector intelligence | R-L814-821 | PRESENT | Cost cycle with both slide-9 readings; season; structure (36% / 38% / 41% CY30P); policy; payer mix |
| (3) Business-model intelligence | R-L823-830 | PRESENT | Two VAP-basis readings; Get-A-Way carries no product tag; undisclosed list includes the VAP-line basis |
| (4) Competition intelligence | R-L832-838 | PRESENT | No named peers in corpus, stated; peer set labelled [INFERENCE] |
| (5) Forward map | R-L840-852 | PRESENT | 7 catalysts, each dated or anchored to a review point, each with a bull and a bear fork |

Gate result: PASS. All five parts are present and carry real content.

---

## 1. COVERAGE AUDIT

### 1A. Fresh enumeration over the A1 fulltexts vs the A2 ledgers

Page markers counted by grep: results 16, presentation 45, press release 5. Structured row IDs counted by grep: results 1,242, presentation 651, press release 180. Each equals the ledger header (ids_in_structured = ids_referenced, orphan_ids [] in all three).

| Doc | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Pages | 16 | 16 | none | PASS |
| Results | Numbered notes (incl. 2 CF notes) | 12 | 12 (L275, 287, 289, 293, 296, 299; L620, 633, 635, 639, 642, 645) | none | PASS |
| Results | Statement line items | 299 | 299 (S P&L 25, S seg 21, S BS 44, S CF 53, C P&L 33, C seg 26, C BS 44, C CF 53; recounted line by line) | none | PASS |
| Results | Statement number cells | 1,114 | 1,114 (S P&L 24x6+1, S seg 21x6, S BS 44x2, S CF 53x3, C P&L 32x6+1, C seg 26x6, C BS 44x2, C CF 53x3) | none | PASS |
| Results | Dash cells | 60 | 60 (S P&L 14: L85 5, L89 3, L99 6; S CF 6; C P&L 24: L417 5, L421 4, L423 3, L433 6, L441 6; C seg 4; C BS 1; C CF 11) | none | PASS |
| Results | Entities / dates / qualifiers | 28 / 23 / 50 | 28 / 23 / 50 (ledger rows R1142-R1169, R1170-R1192 checked against L19-L772) | none | PASS |
| Results | Agenda items | 0 | 2 (L38, L41) | none: carried as R1193 / R1172 / R1148 | STYLE S3 (carried) |
| Results | Auditor paragraphs | section | 9 (L331, 337, 345, 364; L677, 685, 693, 713, 721) plus Other Matter figures R1131-R1138 | none | PASS |
| Results | Forward statements | 0 | 0 | none | PASS |
| Presentation | Slides | 45 | 45 (4 dividers carry no rows: slides 4, 15, 24, 39) | none | PASS |
| Presentation | Slide numbers | 535 | Spot-checked slides 5, 6, 7, 8, 9, 11, 16, 17, 18, 21, 22, 23, 29, 34, 36, 38, 42, 43, 44: every printed value carried | none | PASS (number-word claims: STYLE S5 carried) |
| Presentation | Table cells, slides 8 / 42 / 43 | 242 | 245 printed (3 slide-8 dash cells not carried: P-l242 H1FY27; P-l245 Q1FY27, H1FY27) | none | STYLE S4 (carried) |
| Presentation | Zero-standing | 11 | 14 (same 3 cells) | none | STYLE S4 (carried) |
| Presentation | Forward statements | 15 | 15 (R586-R600) | none | PASS; R599 year labels swapped, STYLE S21 |
| Presentation | Footnotes / entities / dates | 23 / 50 / 28 | 23 / 50 / 28 | none | PASS (carried, spot-checked) |
| Press release | Pages | 5 | 5 | none | PASS |
| Press release | Numbers | 117 | 117 (line-by-line recount, PR-L27 to PR-L224; letter ref "100-26" carried as DATE R156) | none | PASS |
| Press release | Entities / forward / dates / qualifiers | 27 / 8 / 12 / 13 | 27 / 8 / 12 / 13 | none | PASS |

### 1B. Ledger-to-review orphan check

The review keeps its blanket accounting line (R-L20: results R001-R1242, presentation 45 slide rows plus R001-R651, release R001-R180, all reviewed). I spot-checked that material and flagged rows carry real treatment in the loop-2 text:
- Slide 7 product split R052-R067 -> R-L335-344 (positional H1 reading; R064 / R066 label swap recorded R-L30).
- Slide 9 R172-R196 -> R-L358-366. Slide 10 R197-R202 -> Q17 R-L712. Slide 11 R209-R218 -> Q9 R-L704 (FY26 PBT 206 / revenue 2,454 = 8.4%, positional, P-l363-374).
- Slide 16 R244 (0.33) -> R-L168, Q20 R-L715. Slide 17 R250 -> R-L368. Slide 21 R275-R288 -> R-L368. Slide 29 R303-R306 -> Q16 R-L711. Slide 36 R598 -> R-L818. Slide 44 R520-R535 -> R-L306, R-L505, F8 R-L782.
- Release R079-R094 (VAP shares) -> R-L171, R-L826. R101 / R102 -> R-L533. R095-R100 (Nutrivet) -> R-L169.
- Results R1131-R1138, R1168, R1233 -> R-L146, Q8. R1162 / R1229 -> R-L128. R1155 -> Q13. R1164-R1167 -> R-L164. R1209 / R1210 -> R-L121-122. R1046 (L600) -> R-L535.

Result: orphan rows none. Missing from ledger (material) none. Non-material upstream items stay logged as STYLE (S3-S7 carried, S21 new).

### 1C. Resolution of prior findings

| Prior finding | Type | Resolved? | Where in the loop-2 review | Check |
|---|---|---|---|---|
| Run-1 F1 (0.33 is not gross D/E) | FACTUAL | YES | R-L168, R-L477, Q20 R-L715, F8 R-L782, YAML R-L903 | 3,614.81 / 11,081.14 = 0.326 (L533, L536-537, L544-545) |
| Run-1 F2 (HNFL months) | FACTUAL | YES | R-L128 | 16 Jun-30 Sep 2025 = about 3.5 months (L645) |
| Run-1 F3 (organised share) | FACTUAL | YES | R-L818 | 36% / 38% / 41% at CY20 / CY25 / CY30P (P-l1024, P-l1034) |
| Run-1 F4 (milk-holiday gloss) | FACTUAL | YES | R-L836, Q10 R-L705 | P-l600-601, P-l665-667 |
| Run-1 C1 (subsidiaries "subtract") | CONTRADICTION | YES | R-L527, R-L669, R-L767, F5 R-L779, R-L807, R-L829, R-L848, YAML R-L937 | Grep: no "subtract" or subsidiary "drag" claim remains |
| Run-1 C2 (cap wording) | CONTRADICTION | YES | R-L512, R-L787 | INDETERMINATE caps at PROCEED WITH CAVEATS |
| Run-1 M1 (slide 9 readings) | MISSING | YES | R-L358-366, F3 R-L777, R-L816, Q29, M14, forward map R-L847 | Recomputes (Section 2) |
| Run-1 M2 (slide 17 vs 21) | MISSING | YES | R-L368, F8, Q30 | 1.65%; FY26 -2.91% |
| Run-1 M3 (8C seasonality) | MISSING | YES | R-L681-686, 6E R-L616, M2 R-L747, R-L842 | YoY test vs -271 bps |
| Run-1 M4 (VAP counter) | MISSING | YES | R-L344, R-L806, R-L827, R-L668, Q31 | Subsidiary half now conditional on reading A |
| Run-1 M5 (cash conversion) | MISSING | YES | R-L461-467, R-L505, R-L512, F6, Q33, M9 | Recomputes |
| Run-1 M6 (seasonal QoQ) | MISSING | YES | R-L399, R-L448, R-L805, Q34 | Recomputes |
| Run-1 M7 (acquisition probe) | MISSING | YES | Step 5F R-L529-542, Q14, Q32, M8, F5 | Recomputes |
| Loop-1 F1 (VAP-share basis) | FACTUAL | YES | R-L171, R-L70, R-L75, R-L344, R-L668, Q19 R-L714, Q31 R-L726, F8 R-L782, R-L826-827, R-L830, YAML R-L902, R-L914, R-L940, R-L945 | Two readings, separating observation named, no reading picked. Grep: "RESOLVED ... Mixed basis" and "consistent base" absent. Weighting sentence: see S16 |
| Loop-1 F2 (Get-A-Way product) | FACTUAL | YES | R-L344, R-L827, R-L829, R-L838 | Grep: no line ties Get-A-Way to ice cream; Novandie keeps "yogurt" (PR-L146) |
| Loop-1 S9-S12 | STYLE | Applied | R-L364, R-L787, R-L806, R-L30 | Verified (S9 positions: 38.80 col 6, "Apr" col 14, 51.59 col 20; P-l278, P-l288, P-l293) |
| S3-S7 | STYLE | Logged (upstream A1/A2) | R-L30 hygiene line | Carried below |

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4's tables was recomputed from the Rs m source lines. PASS = within 0.01 Cr or 1 bp.

| Metric | A4 value (R-L) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Reading-B parent residual (S revenue less deck Milk + VAP + Fat) | 41.41 -> 44.88 (Q2), 81.85 -> 82.73 (H1) (R-L171) | 10,904.14 - 10,490 = 414.14; 12,733.76 - 12,285 = 448.76 (+8.36%); 22,093.54 - 21,275 = 818.54; 25,651.30 - 24,824 = 827.30 (+1.07%) | L75; P-l187-214 | PASS |
| Others vs C-S revenue gap | +27.6 / +53.5 vs +24.1 / +52.6 (R-L171) | 912 - 636 = 276; 1,753 - 1,218 = 535; (13,195.80 - 12,733.76) - (11,125.17 - 10,904.14) = 241.01; 925.44 - 399.18 = 526.26 | L75, L407; P-l187-214 | PASS |
| Reading-A parent residual growth | about 43-45% (R-L171) | Others less Feed external (L463 less C-S inter-segment L465 - L122): 424.42 -> 606.47 (+42.9%); 828.55 -> 1,199.73 (+44.8%) | L463, L465, L122 | PASS |
| VAP share, both bases | 35.42 vs 31.35 (+4.07); 34.18 vs 30.72 (+3.45) (R-L171, R-L826) | 4,510/12,733.76 = 35.418; 3,418/10,904.14 = 31.346; 4,510/13,195.80 = 34.177; 3,418/11,125.17 = 30.723 | L75, L407 | PASS |
| VAP H1 shares; release H1 FY26 | 39.55%, 45.73% (R-L171); release 33.7% | 10,146/25,651.30 = 39.554; 11,730/25,651.30 = 45.729; 7,451/22,093.54 = 33.725 (standalone base again) | L75; PR-L131-138 | PASS |
| Dairy-subsidiary net revenue share of VAP rise | 0.95 -> 15.65; 13.5% of 109.2 (R-L171, R-L344) | 9.45 / 156.51 m; 147.06 / 1,092 = 13.47%. H1: 9.73 -> 372.17 m = 13.45% of the 2,695 m H1 VAP rise | L461, L119 | PASS |
| Slide 7 sums and derived Q1 | Fat H1 161.40, Others H1 175.30; Q1 lines (R-L337-340) | Positions: 1,614 at cols 64-68 under Fat H1FY27 (cols 63-68), 1753 at cols 85-88 under Others H1FY27 (cols 81-86), P-l206-207, P-l219. Sums 13,197 / 11,126 / 26,577 / 22,493 vs L407 | P-l187-219; L407 | PASS |
| Slide 9 averages and readings | 53.83 / 40.10; A 51.08 (+3.35 vs landed, +3.98 YoY); B 42.85 (-4.88, +4.92 YoY, prior gap 5.06) (R-L361-363) | 161.48/3; 120.31/3; A 51.082, prior 47.105; B 42.848, prior 37.932; 47.73 - 42.85; 42.99 - 37.93 | P-l270-288; PR-L76-77 | PASS |
| Slide 17 vs slide 21 | 1.6%; FY26 -2.9%; sales 2.7% (R-L368) | Positional (legend procured first; H1 17.7 / 12.0 tie PR-L122, PR-L127): (16.7/15.9)^(1/3) - 1 = 1.65%; 16.7/17.2 - 1 = -2.91%; (11.8/10.9)^(1/3) - 1 = 2.68% | P-l647-674 | PASS |
| Consolidated Op EBITDA, 6 periods | 77.19 / 61.86 / 73.97 / 266.27 / 151.08 / 135.83 (R-L211) | 771.88 / 618.63 / 739.67 / 2,662.70 / 1,510.75 / 1,358.29 m | L420 + L416 + L415 - L408 | PASS |
| Consolidated margins, ETR, GM, OI/PBT, PAT margin, reported EBITDA, core PBT | all cells R-L212-218 | e.g. ETR 117.42/425.99 = 27.56%; GM 2,881.38/13,195.80 = 21.84%; H1 GM 5,718.76/26,576.74 = 21.52% (release -265 bps ties) | L407-428 | PASS |
| Standalone derived set | all cells R-L250-257 | e.g. Op EBITDA 711.17 / 718.78 / 594.02 m; GM 2,676.74/12,733.76 = 21.02% | L75-94 | PASS |
| YoY and QoQ, C and S; H1 YoY | R-L267-298 | e.g. EBIT -18.54% (464.97/570.79); S finance +104.83%; H1 core PBT -36.32% | L75-94, L407-446 | PASS |
| Segment walk | R-L317-331 | e.g. Dairy margin 3.399% vs 5.692% (-229 bps); Feed 3.905% vs 9.034% (-513 bps); C-S inter-segment 369.54 -> 546.97 m | L119-L142, L461-489 | PASS |
| KPI spread and pass-through | 13.93 -> 12.61 (-9.5%); 72% (R-L353-355) | 60.34/1.06 = 56.92; 56.92 - 42.99; 3.42/4.74 | PR-L76-84 | PASS |
| VAP price share (log split) | 40 / 41 / 39% (R-L344) | 39.5 / 40.8 / 38.5% | PR-L87-90 | PASS |
| 3A / 3B sequential | e.g. Q1 FY26 6.50%, H2 FY26 5.06%, +17.55% vs H2 avg (R-L380-394) | 738.87/11,367.55; 1,151.95/22,767.19; 13,380.94/11,383.60 | FY minus H1 columns | PASS |
| 3C seasonal step and QoQ split | Q1 FY26 GM 23.81%, H2 22.71%, -183 bps; +63 / +58 / -23 bps (R-L399) | 2,706.06/11,367.55; 5,170.46/22,767.19; 63.1 / 57.8 / -22.7 bps | L407-418 | PASS |
| 3C step-up wording | "about +17.5% over the H2 FY26 quarterly average" for H1 FY27 (R-L398) | Q1 FY27 +17.55%; H1 FY27 average 1,328.84 vs 1,138.36 = +16.73% | L407 | STYLE S18 (referent) |
| PAT bridge 4A / 4B | -201.38 m / -178.89 m, every component (R-L414-440) | identical; 4B rate effect -9.476 m | L75-94, L407-428 | PASS |
| 4C shares; OI reversion | 55.7% / 44.3%; Rs 44.40 Cr PBT, Rs 32.16 Cr PAT (R-L444-445) | 140.05/251.61; 444.00 x (1 - 0.27564) | derived | PASS |
| 5A consolidated cash and balance sheet | every row R-L460-477 | e.g. CFO/PAT 3.119 / 2.710 / 1.580; FCF -9.74 / 591.23 / -1,452.10 m; days 5.41 / 22.82 / 17.71; net debt 684.09 -> 1,053.85 m | L503-L624 | PASS |
| 5B standalone cash and balance sheet | every row R-L486-499 | e.g. CFO/PAT 3.3960 vs 2.9724; days 5.22 / 21.50 / 16.66 | L156-L278 | PASS except one delta: S13 |
| 5B CFO/PAT change | +0.43x (R-L487) | 3.3960 - 2.9724 = +0.4236 = +0.42x (A4 subtracted rounded ratios) | L250, L94 | ROUNDING (STYLE S13) |
| 5D EBITDA-basis conversion | 0.91 / 0.78 / 1.01x; 0.93x ex L592 (R-L512) | 2,422.92/2,662.70; 1,181.26/1,510.75; 1,373.94/1,358.29; 1,264.18/1,358.29 | L585-596 | PASS |
| 5E S-vs-C gap, 6 periods | all cells R-L520-525 | e.g. PAT 3.42/305.15 = 1.12%; owners 8.48/305.15 = 2.78%; FY26 108.20/1,397.01 = 7.75% | L75, L94, L407, L428, L436 | PASS |
| 5F acquisition rows | 16.22; 31.92; 20.63; 17.9%; 2.9x; 2.60 (R-L535-539) | 162.23 m; 319.20 m; 71.85 + 134.46 = 206.31 m; 206.31/1,154.48; 7.54/0.29 = 26.0 m | L600, L254-255, L507-508, L160, L440 | PASS |
| 0G rows | 0.33 = 0.326; 0.30 / 0.34; Nutrivet 4.34% / 2.61%; drag 431.10 vs 261.93 (R-L163-173) | 3,614.81/11,081.14; 3,452.25 and 3,843.98 / 11,408.26; 37/853; 19/728; 739.67 - 308.57; 771.88 - 509.95 | L533-545; PR-L142-144 | PASS |
| Q20 net-debt ratios | 0.09; 0.24 (R-L715) | 1,053.85/11,408.26 = 0.092; 2,793.10/11,408.26 = 0.245 | L517-521, L536, L544 | PASS |
| Trailing four quarters | 115.45; 12.44; 4,934.39 / 251.02 (R-L631-633) | 1,154.48 m; /92.796; 49,343.93 m; 2,510.24 m | L436, L407 | PASS |
| ROCE proxy | 12.3% on 1,486.06 Cr (R-L644) | 1,832.90 / 14,860.51 m = 12.33%; denominator 1,486.05 | L424, L415, L533, L536, L544 | PASS (denominator rounding, STYLE S13) |
| Unreviewed subsidiary | Q1 loss 0.09; 3.5% of PAT (R-L149) | 11.76 - 10.82 = 0.94 m; 10.82/308.57 = 3.51% | L721-725 | PASS |

Arithmetic result: no mismatch above rounding. Two deltas differ by rounding only (S13). One referent is loose (S18).

---

## 3. ADVERSARIAL READ

The three most positive claims left in the loop-2 review are below. Each counter uses only the extract.

### PC1. "Value-added products grew 32% YoY to Rs 451.0 Cr and are the growth engine" (R-L806; bull reading R-L667; margin engine R-L826)

Strongest bear counter:
- Price or mix is about 40% of revenue growth in curd, paneer and ice cream (PR-L87-90). Present: R-L344, R-L806, R-L827, Step 7 R-L646.
- VAP slowed from +39.75% YoY in Q1 to +31.95% in Q2 and fell 20.0% QoQ (P-l187-208). Present: R-L342, Q5.
- Gross margin fell 271 bps YoY against the mix gain (L407, L411-413). Present: R-L828.
- Under reading A, dairy-subsidiary net revenue is up to 13.5% of the Q2 VAP rise. The H1 share is the same, 13.45% (L461 minus L119: 0.97 to 37.22 Cr against +269.5 Cr), so H1 adds nothing new. Present, conditional on reading A: R-L344, R-L668, R-L827, Q31.

Survives: yes. Every part is already in the review, so nothing new needs grafting.

### PC2. "Q2 margin recovered 98 bps from the Q1 trough; opex fell 138 bps as a share of revenue" (R-L667, R-L804, R-L448)

Strongest bear counter:
- The same Q1-to-Q2 step came in FY26: Op margin +44 bps and gross margin +74 bps, then H2 gross margin ran 183 bps below Q2 (L407-418).
- The Q2 FY27 gain splits +63 / +58 / -23 bps. It came with a Rs 48.32 Cr stock drawdown (L413) while the cost level rose every month (P-l276-288).
- The opex leverage rides on price-led revenue: milk volume +2.5% against realisation +6% (PR-L126-128).
- Present: R-L399, R-L448, R-L805, R-L682, Q34.

Survives: yes, and it is present. Nothing new.

### PC3. "Subsidiaries still add; Feed still earns" (R-L527, R-L807, F5 R-L779)

Strongest bear counter:
- Consolidated PBT beat standalone PBT by Rs 1.15 Cr in Q2 (425.99 - 414.53 m; L424, L90). Nutrivet alone earned PBT Rs 3.7 Cr (PR-L143). Everything else outside the parent therefore came to about -Rs 2.55 Cr pre-tax [derived].
- About 70% of the increment went to tax (8.04 m on 11.46 m; L426-427 vs L92-93).
- About 65% of Feed's revenue growth is sales to the group: C-S inter-segment +17.74 Cr against Feed +27.14 Cr (L465, L122, L463).
- Present: R-L331, R-L447, R-L527 PBT-gap bridge, Q6, F5.

Survives: yes, and it is present. Nothing new.

### MANDATORY ACQUISITION-ECONOMICS PROBE (re-run)

Two acquisition events appear in the documents. Control of Heritage Novandie was taken on 16 Jun 2025 (L645). The release headline "Strategic Acquisitions Scaling Up" covers Novandie, "wholly owned", and Get-A-Way, "71%-owned" (PR-L146-148).
- Multiple: consideration is NOT FOUND. The cash proxy is the Rs 16.22 Cr net FY26 outflow (L600). Target earnings are below zero in every disclosed period: dairy-subsidiary segment result FY26 -Rs 3.54 Cr, H1 FY27 -Rs 3.15 Cr (L468 minus L125). About Rs 16.2 Cr / target PAT < 0: price / PAT is not meaningful, and no positive earnings multiple exists.
- Quality markers: target ROCE, debt, cash and customer tenure are NOT FOUND.
- Exposure: goodwill Rs 7.19 Cr plus Rs 13.45 Cr of other intangibles outside the parent = Rs 20.63 Cr (L507-508, L160).
- Bear reading: the deals are presented as scaling, but the release gives no revenue or profit for either, and the acquired dairy businesses lose money at a widening rate. This survives and is grafted in full: Step 5F R-L529-542, Q14, Q32, M8, F5.
- Supporting detail, not a new counter (S20): the NCI balance fell from 47.93 m to 40.39 m (L532). The fall equals the H1 NCI loss of 7.54 m (L440). On the single-NCI-entity inference, the 29% holder's share of Get-A-Way net assets fell 15.7% in six months. This supports the funding-obligation bear fork of Q15.

---

## 4. FINDINGS (tagged)

### FACTUAL
None.

### MISSING
None. Every surviving bear counter and the acquisition probe are already in the review. No orphan row and no missing ledger row.

### CONTRADICTION
None. All prior contradictions are resolved, and no new internal inconsistency changes a number, a fact or the verdict.

### STYLE (logged, no loop)
- S13. Two values subtract or sum rounded figures. (a) The 5B CFO/PAT change is "+0.43x" (R-L487); from unrounded ratios it is 3.3960 - 2.9724 = +0.42x (L250, L94). (b) The Step 7 ROCE denominator is "1,486.06 Cr" (R-L644); 11,408.26 + 3,452.25 = 14,860.51 m = 1,486.05 Cr (L533, L536, L544). The 12.3% result is unchanged.
- S14. Anchor prefixes. The anchor key (R-L14) defines "L###" as a results line. Three press-release ranges carry the bare L prefix: "PR-L81-84, L130-133" (R-L302), "PR-L76-77, L122-123" (R-L351) and "PR-L83-84, L127-128" (R-L353). Results L130-133 are segment interest-income lines. Write PR-L130-133, PR-L122-123 and PR-L127-128. The values are correct.
- S15. The YAML monitorables list (R-L918-931) has 13 items. It omits table row M6, "Strategic investments behind long-term growth", none stated (R-L751; PR-L182-183).
- S16. The VAP-basis weighting at R-L171 says "The 'Others' arithmetic fits reading B better". That overstates the evidence, and the same overstatement came from the loop-1 A5 pass.
  - Identity. The four slide-7 lines sum to consolidated revenue (L407), so Others - (C - S) = S - (Milk + VAP + Fat). "Others tracks the C-S gap" and "the parent residual moves little" are therefore one observation, not two.
  - Counter-indicator for reading A. A's parent residual (42.44 to 60.65 Cr in Q2, +42.9%; 82.86 to 119.97 Cr in H1, +44.8%) grows in step with group feed sold into the dairy segment. That C-S inter-segment revenue (L465 minus L122) went from 36.95 to 54.70 Cr in Q2 (+48.0%) and from 72.42 to 102.79 Cr in H1 (+41.9%). Under reading B the parent residual (44.88 Cr) sits below the 54.70 Cr of group feed. If the parent resells that feed as revenue, B is the harder fit [INFERENCE]. The filing does not show how the feed is booked. Standalone stock-in-trade purchases exceed consolidated by only Rs 24.45 Cr (L80 vs L412).
  - Suggested text: "The 'Others' arithmetic does not separate the readings. Under B the parent residual is stable (+8.4% Q2, +1.1% H1). Under A it grows 43-45%, in step with group feed sold into the dairy segment (C-S inter-segment +48% Q2, +42% H1; L465, L122), which the parent may resell [INFERENCE]."
  - Impact: no number, flag, question or verdict changes. A4 already picks no reading and names the separating observation (Q19, Q31).
- S17. The verdict paragraph says "two cross-statement movements do not (F7)" (R-L787). 5C lists three: L255 vs L163, L246 vs L190 / L202, and L247 vs L194 / L203 (R-L508). F7 groups the last two as one item. Say "three standalone cross-statement movements (F7)" or match the F7 grouping explicitly. This wording came from the loop-1 A5 S10 suggestion.
- S18. R-L398 says revenue "STEPPED UP in H1 FY27 (about +17.5% over the H2 FY26 quarterly average)". +17.55% is the Q1 FY27 step. The H1 FY27 quarterly average is +16.73% over the H2 FY26 average (1,328.84 vs 1,138.36; L407). Name the quarter.
- S19. Optional enrichment for Q21 / F8. Slide 14 says "Core Markets Started Firing" and "Boosted Profitability" (P-l485-490; A1 R600). Filed Dairy segment margin fell 229 bps YoY consolidated (5.69% to 3.40%; L461, L468) and from 5.82% to 3.60% standalone (L119, L125). The slogan is unquantified and may refer to Telangana only. A second deck-internal mismatch: slide 18 prints 188 chilling centres (P-l589) and slide 22 prints 191 (P-l687).
- S20. Optional for Step 5F / Q15: the NCI balance erosion (47.93 to 40.39 m, L532, equal to the H1 NCI loss, L440), as set out in the acquisition probe above.
- S21. Upstream A1. Presentation R599 swaps the slide 37 projection years. Urban population runs to 2030 (P) and healthy food to 2035 (P) (P-l1094-1095). A4 does not use these years.
- Carried, upstream A1/A2, no loop:
  - S3: agenda_items 0 vs 2 (L38, L41).
  - S4: 3 slide-8 dash cells not carried.
  - S5: number-word claims "Zero Milk Holiday" and "No Milk holiday since inception".
  - S6: R250 label.
  - S7: R178 / R181 species under a month-only flag.

---

## VERDICT

COMPLETE. No loop.
- Run-1 F1-F4, C1-C2 and M1-M7 are resolved and stay resolved in the loop-2 text. Loop-1 F1 and F2 are resolved.
- The deliverable gate passes. The ledgers reconcile (1,242 / 651 / 180 IDs), no orphan row exists, and no row is missing from a ledger.
- Every derived metric recomputes within rounding.
- The surviving bear counters to the three most positive claims and the acquisition probe are already in the review.
- The protocol verdict PROCEED WITH FLAGS is not challenged.

## STYLE NOTES

S13-S21 (new) and S3-S7 (carried) are recorded above. None triggers a re-run. A4 may apply S13-S18 as text edits at save time. S19 and S20 are optional enrichments. S21 and S3-S7 are upstream A1/A2 hygiene items.

---

```yaml
stage: A5-adversary
company: "HERITGFOOD"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop: 2
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
    - "S13: rounded-figure arithmetic: 5B CFO/PAT change +0.43x vs +0.42x unrounded (R-L487; L250, L94); ROCE denominator 1,486.06 vs 1,486.05 Cr (R-L644; L533, L536, L544)"
    - "S14: bare L prefix on press-release ranges L130-133, L122-123, L127-128 (R-L302, R-L351, R-L353); write PR-L"
    - "S15: YAML monitorables (R-L918-931) omit table row M6 (R-L751)"
    - "S16: R-L171 'Others arithmetic fits reading B better' overstates: Others-(C-S) = S-(Milk+VAP+Fat) is one identity; reading-A residual (+42.9% Q2, +44.8% H1) tracks C-S inter-segment feed (+48.0% Q2, +41.9% H1; L465, L122); say the arithmetic does not separate the readings"
    - "S17: R-L787 'two cross-statement movements' vs three listed at R-L508 (L255/L163, L246/L190+L202, L247/L194+L203)"
    - "S18: R-L398 '+17.5%' is the Q1 FY27 step; H1 FY27 average is +16.73% over the H2 FY26 average (L407)"
    - "S19: optional: slide 14 'Boosted Profitability' (P-l485-490) vs Dairy segment margin -229 bps YoY (L461, L468); slide 18 '188' vs slide 22 '191' chilling centres (P-l589, P-l687)"
    - "S20: optional: NCI balance 47.93 -> 40.39 m (L532) equals H1 NCI loss (L440); 29% holder's share of Get-A-Way net assets -15.7% in six months [INFERENCE]; supports Q15 bear fork"
    - "S21: upstream A1 R599 swaps slide 37 projection years (urban population 2030 (P), healthy food 2035 (P); P-l1094-1095)"
    - "S3-S7 carried (upstream A1/A2): agenda_items count, slide-8 dash cells, number-word rows, R250 label, R178/R181 species flag"
loop_back_to: ""
gap: ""
style_notes:
  - "S13: compute deltas and sums from unrounded figures (R-L487, R-L644)"
  - "S14: PR-L prefix on three press-release ranges (R-L302, R-L351, R-L353)"
  - "S15: add M6 to YAML monitorables"
  - "S16: replace 'fits reading B better' at R-L171 with 'does not separate the readings' plus the inter-segment feed indicator for reading A"
  - "S17: 'three' cross-statement movements, or match the F7 grouping (R-L787)"
  - "S18: name Q1 FY27 as the +17.55% step (R-L398)"
  - "S19: optional deck-claim checks for Q21 / F8"
  - "S20: optional NCI-erosion line for Step 5F / Q15"
  - "S21, S3-S7: upstream A1/A2 hygiene, logged only"
analyst_note: "Loop-2 re-audit. All 15 prior loop findings are resolved: run-1 F1-F4, C1-C2 and M1-M7, and loop-1 F1-F2. The loop-2 edits recompute: parent residual 41.41 to 44.88 Cr (Q2) and 81.85 to 82.73 Cr (H1); Others +27.6 and +53.5 Cr against C-S +24.1 and +52.6 Cr; 34.18% vs 30.72% and 35.42% vs 31.35%; 13.5% of the VAP rise. No Get-A-Way product claim remains. The gate passes, all three ledgers reconcile, and no orphan or missing row exists. Every derived metric recomputes; two values differ by rounding only. The three most positive claims carry their counters already, and the acquisition probe stands in Step 5F. Verdict COMPLETE with nine new STYLE notes. S16 matters most. 'Others tracks the C-S gap' and 'the parent residual moves little' are one identity, not two facts. Under reading A the residual grows in step with group feed sold into the dairy segment (+48% Q2). So the arithmetic does not separate the readings, and 'fits B better' overstates. My loop-1 pass made the same overstatement. No number, flag or verdict changes."
```
