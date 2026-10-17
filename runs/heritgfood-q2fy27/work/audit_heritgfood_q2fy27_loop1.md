# A5 ADVERSARY / COMPLETENESS AUDIT: Heritage Foods Limited (HERITGFOOD) | Q2 FY27 | LOOP 1 RE-AUDIT

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-17 | loop: 1
Under audit: runs/heritgfood-q2fy27/work/review_heritgfood_q2fy27.md (971 lines, loop-1 revision)
Prior audit checked for resolution: runs/heritgfood-q2fy27/work/audit_heritgfood_q2fy27_run1.md
Inputs read: A1 fulltexts (results 782 lines, presentation 1,328, press release 230); A1 structured files (results R001-R1242, presentation R001-R651, press release R001-R180; read by targeted row lookups); A2 ledgers (all three; count tests and row sections); A4 review (full).
Not read: source PDFs, anything under inputs/, A3 forensics. No Grep in this run touched work/forensics_*.

Anchor key: L### = results fulltext; P-l### = presentation fulltext; PR-L### = press release fulltext; R-L### = line of the loop-1 A4 review; R### = A1 structured row. Rs Cr unless marked Rs m.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PLAIN-LANGUAGE BRIEF at R-L789-850.

| Part | Location | Status | Note |
|---|---|---|---|
| (1) Summary narrative | R-L793-810 | PRESENT | 16 lines, within 10-20; real content; seasonal and cash-conversion counters now carried |
| (2) Sector intelligence | R-L812-819 | PRESENT | F3 fix in place (36% CY20, 38% CY25, 41% CY30P) |
| (3) Business-model intelligence | R-L821-828 | PRESENT | Carries F1 and F2 below (VAP basis; Get-A-Way product tag) |
| (4) Competition intelligence | R-L830-836 | PRESENT | F4 fix in place; peer set labelled [INFERENCE] |
| (5) Forward map | R-L838-850 | PRESENT | 7 catalysts, each dated or anchored to a review point, each with a bull and a bear fork |

Gate result: PASS. All five parts are present and non-empty.

---

## 1. COVERAGE AUDIT

### 1A. Fresh enumeration over the A1 fulltexts vs the A2 ledgers

The fulltexts and ledgers carry the same line counts and count-test values as in run 1 (results 782 / presentation 1,328 / release 230 lines). Categories marked "re-run" were recounted from the fulltext in this pass. Categories marked "carried" were recounted line by line in run 1 and spot-checked in this pass.

| Doc | Category | A2 count | A5 fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|---|
| Results | Pages | 16 | 16 ([page N] markers) | re-run | none | PASS |
| Results | Numbered notes (incl. CF note 1) | 12 | 12 (L275, 287, 289, 293, 296, 299; L620, 633, 635, 639, 642, 645) | re-run | none | PASS |
| Results | Statement line items | 299 | 299 (S P&L 25, S seg 21, S BS 44, S CF 53, C P&L 33, C seg 26, C BS 44, C CF 53) | re-run | none | PASS |
| Results | Statement NUMBER cells | 1,114 | 1,114 | carried; line-item x column structure unchanged | none | PASS |
| Results | Dash / zero cells | 60 | 60 (S P&L 14, S CF 6, C P&L 24, C seg 4, C BS 1, C CF 11) | re-run | none | PASS |
| Results | Entities / dates / qualifiers | 28 / 23 / 50 | 28 / 23 / 50 | carried | none | PASS |
| Results | Agenda items | 0 | 2 (L38, L41) | re-run | none: carried as R1193/R1172/R1148 | STYLE S3 (carried) |
| Results | Auditor paragraphs | section | 9 (L331, 337, 345, 364; L677, 685, 693, 713, 721) | re-run | none | PASS |
| Presentation | Slides | 45 | 45 | re-run | none | PASS |
| Presentation | Slide numbers | 535 | spot-checked slides 5, 6, 7, 8, 9, 16, 17, 21, 29, 36, 42, 43, 44: complete | carried + spot | none | PASS; R064/R066 label swap, STYLE S12 |
| Presentation | Table cells, slides 8 / 42 / 43 | 242 | 245 printed (3 slide-8 dash cells not carried) | carried | none | STYLE S4 (carried) |
| Presentation | Zero-standing | 11 | 14 (same 3 dash cells) | carried | none | STYLE S4 (carried) |
| Presentation | Forward / footnotes / entities / dates | 15 / 23 / 50 / 28 | 15 / 23 / 50 / 28 | carried | none | PASS |
| Press release | Pages | 5 | 5 | re-run | none | PASS |
| Press release | Numbers | 117 | 117; PR-L63-148 re-checked this pass | carried + spot | none | PASS |
| Press release | Entities / forward / dates / qualifiers | 27 / 8 / 12 / 13 | 27 / 8 / 12 / 13 | carried | none | PASS |

### 1B. Ledger-to-review orphan check

The loop-1 review keeps the blanket accounting line (R-L19: results R001-R1242, presentation 45 slide rows plus R001-R651, release R001-R180). No section was deleted in loop 1. Spot-check of material rows for real treatment in the revised text: R172 (~80% cow) -> R-L359; R173-R184 (slide 9 series) -> R-L356-357; R250 (slide 17 6%) -> R-L366; R598 (CY30P) -> R-L816; R052-R067 (slide 7 product split) -> R-L335-338; release R101/R102 (Top 5, 71%) -> R-L531; results R1131-R1138 (unreviewed subsidiary) -> R-L144; R1155 (HNFL name change) -> Q13; R1164-R1167 (Annexure entities) -> R-L162; R1209/R1210 (notes 4a/4b) -> R-L119-120; R1229 (note 5) -> R-L126.

Result: orphan rows none; missing from ledger (material) none. Upstream non-material items stay logged as STYLE (S3-S7 carried, S12 new).

### 1C. Resolution of run-1 findings

| Run-1 finding | Type | Resolved? | Where in the loop-1 review | Check |
|---|---|---|---|---|
| F1 (0.33 is not gross D/E) | FACTUAL | YES | R-L59, R-L166, R-L475, Q20 R-L713, F8 R-L780, YAML R-L900 | 3,614.81 / 11,081.14 = 0.326 (L533, L536-537, L544-545); 30 Sep with leases 0.337; Q20 net-debt ratios 0.092 and 0.245 recompute |
| F2 (HNFL months) | FACTUAL | YES | R-L126 | 16 Jun-30 Sep = about 3.5 months (L645) |
| F3 (organised share) | FACTUAL | YES | R-L816 | 36% / 38% / 41% sit at the CY20 / CY25 / CY30P column positions (P-l1024, P-l1034) |
| F4 (milk-holiday gloss) | FACTUAL | YES | R-L834, Q10 R-L703 | P-l600-601, P-l661-667 |
| C1 (subsidiaries "subtract") | CONTRADICTION | YES | R-L525, R-L667, R-L765, F5 R-L777, R-L805, R-L827, R-L846, YAML R-L934 | No "subtract" or "drag" claim on subsidiaries remains; 6E red threshold stated as not hit |
| C2 (cap wording) | CONTRADICTION | YES | R-L510, R-L785 | INDETERMINATE caps at PROCEED WITH CAVEATS; flags take it to PROCEED WITH FLAGS |
| M1 (slide 9 two readings) | MISSING | YES | R-L356-364, F3 R-L775, R-L814, Q29, M14, forward map | Arithmetic recomputes (Section 2) |
| M2 (slide 17 vs slide 21) | MISSING | YES | R-L366, F8, Q30 | 1.65% CAGR; FY26 -2.91% |
| M3 (8C seasonality) | MISSING | YES | Step 8C R-L679-684, 6E R-L614, M2, forward map | YoY test vs -271 bps removes the season |
| M4 (VAP counter) | MISSING | YES, but see F1 and F2 | R-L342, R-L804, R-L825, R-L666, Q31 | Price share recomputes. The subsidiary-content half rests on an unestablished basis (F1) and an out-of-corpus product tag (F2). Both entered through A5 run-1 graft text |
| M5 (cash conversion counter) | MISSING | YES | 5A R-L461, R-L465; 5C R-L503; 5D R-L510; F6; Q33; M9 | Recomputes |
| M6 (seasonal QoQ counter) | MISSING | YES | 3C R-L397, 4C R-L446, R-L803, Q34 | Recomputes |
| M7 (acquisition probe) | MISSING | YES | Step 5F R-L527-540, Q14, Q32, M8, F5 | Recomputes |
| S1, S2, S8 | STYLE | Fixed | R-L216-218, R-L301, R-L320, R-L169, R-L463-464, R-L487, R-L525; R-L21; R-L847-849 | Verified |
| S3-S7 | STYLE | Logged, not fixed (upstream A1/A2) | R-L28 hygiene line notes S6, S7 | Carried below |

---

## 2. ARITHMETIC AUDIT

Every derived metric added or changed in loop 1 was recomputed from the Rs m source lines. The core P&L, bridge, cash, balance-sheet and S-vs-C set was re-run as well. PASS = within 0.01 Cr or 1 bp.

| Metric | A4 value (R-L) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Deck "Net Debt/Equity 0.33" (F1 fix) | borrowings + leases / equity = 0.33; 30 Sep 0.30 / 0.34 (R-L166) | 3,614.81 / 11,081.14 = 0.326; 3,452.25 / 11,408.26 = 0.303; 3,843.98 / 11,408.26 = 0.337 | L533, L536-537, L544-545 | PASS |
| Q20 net debt / equity | 0.09; 0.24 (R-L713) | 1,053.85 / 11,408.26 = 0.092; 2,793.10 / 11,408.26 = 0.245 | L517-521, L536, L544 | PASS |
| Slide 9 Q2 averages; reading A; reading B | 53.83 / 40.10; A 51.08 (+3.35 vs landed), +3.98 YoY; B 42.85 (-4.88), +4.92 YoY, prior gap 5.06 (R-L359-361) | 161.48/3 = 53.827; 120.31/3 = 40.103; A 0.8x53.827+0.2x40.103 = 51.082, prior 47.105; B 42.848, prior 37.932; 47.73-42.85 = 4.88; 42.99-37.93 = 5.06 | P-l270-288; PR-L76-77 | PASS |
| Slide 9 series YoY, monthly | S1 +4.8 to +8.3%; S2 +9.1, +9.5, +13.5, +15.5, +15.0, +14.5% (R-L356-357) | Label x-positions align with each series' value labels in every month | P-l270-288 | PASS |
| Slide 17 vs slide 21 | 1.6% CAGR; FY26 -2.9%; sales 2.7% (R-L366) | (16.7/15.9)^(1/3)-1 = 1.65%; 16.7/17.2-1 = -2.91%; (11.8/10.9)^(1/3)-1 = 2.68% | P-l647-671 | PASS |
| VAP price share (log split) | curd 40%, paneer 41%, ice cream 39%; buttermilk +6.4%, lassi +1.1% (R-L342) | ln(1.26/1.15)/ln(1.26) = 39.5%; 40.8%; 38.5%; 1.66/1.56 = 1.064; 1.91/1.89 = 1.011 | PR-L87-90 | PASS |
| Dairy subsidiaries (C minus S Dairy) | result Q2 FY26 -1.33, Q2 FY27 -2.05, H1 FY26 -1.76, H1 FY27 -3.15, FY26 -3.54; revenue Q2 FY27 15.65 (R-L327) | -13.29 / -20.51 / -17.57 / -31.48 / -35.36 m; 156.51 m | L468 minus L125; L461 minus L119 | PASS |
| FY26 seasonal step | Q1 FY26 GM 23.81%, Q2 24.54%, H2 avg 22.71%, -183 bps; Op margin 6.50 / 6.94 / 5.06% (R-L397) | 2,706.06/11,367.55; 2,730.61/11,125.17; 5,170.46/22,767.19; 738.87/11,367.55; 1,151.95/22,767.19 | L407-L420 (H1, Q2, FY columns) | PASS |
| QoQ split of +98 bps | GM +63, other exp +58, employee -23; other exp -7.2% (R-L397) | +63.1 / +57.8 / -22.7 bps; 1,206.51/1,300.80 = -7.25% | L407-418 | PASS |
| 8C seasonal projection | about 20.0% (R-L680) | 21.84 - 1.83 = 20.01% | derived | PASS |
| 5D cash conversion, EBITDA basis | D&A 53.9% / 96.7% of PAT; 0.91x / 0.78x / 1.01x (0.93x ex L592) (R-L510) | 809.83/1,501.38; 539.57/558.26; 2,422.92/2,662.70; 1,181.26/1,510.75; 1,373.94/1,358.29; 1,264.18/1,358.29 | L570, L428, L586, L592, L594 | PASS |
| Non-inventory WC change | -43.31 / -0.30 / -38.82; +43.01; FY26 parts -37.86, -27.39, -8.95, +36.40 (R-L465, R-L503) | -433.14 / -2.98 / -388.21 m; L587-593 FY26 column sums to -388.21 | L585-594 | PASS |
| 5F cash proxy | 16.22; 31.92 (R-L533) | 162.23 m; 175.00+72.00+67.34+4.86 = 319.20 m | L600; L254-255 | PASS |
| 5F goodwill + intangibles outside parent | 20.63; 17.9% of 115.45; 2.9x goodwill (R-L537) | 71.85 + (145.07-10.61) = 206.31 m; 17.87%; 2.87x | L507-508, L160 | PASS |
| NCI-implied Get-A-Way loss | Q2 1.74, H1 2.60 (R-L525, R-L534) | 5.06/0.29 = 17.45 m; 7.54/0.29 = 26.0 m | L440 | PASS (labelled INFERENCE) |
| 5E S-vs-C gap, 6 periods, all cells | e.g. Q2 FY27 PAT gap 0.34 / 1.12%, owners 2.78% (R-L518-523) | 3.42/305.15; 8.48/305.15; all 54 cells recompute | L75/L407, L94/L428, L436, Op EBITDA build | PASS |
| 5E narrowing; EBITDA contribution | 4.23 pp Q2, 5.27 pp H1; -46% (R-L525) | 5.35-1.12; 6.243-0.977 = 5.266; 28.50/53.10 = -46.3% | derived | PASS |
| Slide 7 product split and derived Q1 | Fat H1 156.20/161.40; Others H1 121.80/175.30 and all YoY (R-L335-338) | Positions: 1,614 sits under Fat H1FY27 (P-l207 vs P-l219), 1753 under Others H1FY27 (P-l206 vs P-l219) | P-l187-219 | PASS (A4 correct; A1 R064/R066 labels swapped, S12) |
| VAP share "consistent base" and mixed-basis charge | "RESOLVED ... Mixed basis ... +3.45 pp, not +4.1 pp" (R-L169; Q19 R-L712; R-L824; F8 R-L780) | +3.45 pp holds only if the VAP line holds the subsidiaries. If the VAP line is standalone, the printed 35.42% vs 31.35% (+4.07 pp) is consistent. The extract does not settle it, and the "Others" arithmetic fits the standalone reading (F1) | L75, L407; P-l187-219 | FAIL (F1) |
| Core P&L set (Op EBITDA, margins, ETR, GM, YoY, QoQ, H1) | as run 1 | unchanged; re-run | L75-104, L407-446 | PASS |
| PAT bridge 4A / 4B; 4C shares | -201.38 m / -178.89 m; 55.7% / 44.3% | re-run, identical | L75-94, L407-428 | PASS |
| 0G PR-A3-02 drag | 431.10 vs 261.93 m (+169.17) | 739.67-308.57; 771.88-509.95 | derived | PASS |
| 3A / 3B sequential tables | H2 FY26 2,276.72 / 5.06% / 63.84; S 2,205.71 / 4.81% / 57.88 | re-run, identical | FY minus H1 columns | PASS |
| 5A / 5B cash and balance-sheet rows | CFO, CFO/PAT, FCF, days, CCC, net debt, borrowings | re-run, identical | L156-278, L503-624 | PASS |
| Trailing 4Q | owners' PAT 115.45; EPS 12.44; revenue 4,934.39; Op EBITDA 251.02 (5.09%) | 1,154.48 m; /92.796; 49,343.93 m; 2,510.24 m | L436, L443, L407 | PASS |
| ROCE proxy | 12.3% (R-L642) | 183.29 / 1,486.05 = 12.33% | L424, L415, L533, L536, L544 | PASS |
| Run-1 S1 deltas | -271; +99; -513; +3.45; -60.10; -52.84; -55.75; 5.27 | all now from unrounded ratios | various | PASS |

Arithmetic result: every number A4 added in loop 1 recomputes. One basis claim fails (F1). It changes a stated conclusion and a disclosure-quality charge, not a recomputed value.

Detail for F1 (the second reading, from the extract):

| Measure | Q2 FY26 | Q2 FY27 | Change | H1 FY26 | H1 FY27 | Change |
|---|---|---|---|---|---|---|
| Deck "Others" line (R058/R059; P-l187, P-l195; H1 P-l206, P-l214) | 63.6 | 91.2 | +27.6 | 121.8 | 175.3 | +53.5 |
| Consolidated minus standalone revenue (L407 minus L75) | 22.10 | 46.20 | +24.1 | 39.92 | 92.54 | +52.6 |
| Standalone revenue less deck Milk + VAP + Fat (reading B residual) | 41.41 | 44.88 | +8.4% | 81.85 | 82.73 | +1.1% |
| Same residual under reading A (Others less Feed net external revenue) | 42.44 | 60.65 | +42.9% | 82.86 | 119.97 | +44.8% |
| Dairy subsidiaries' net segment revenue (L461 minus L119) | 0.95 | 15.65 | +14.7 | 0.97 | 37.22 | +36.2 |

- Reading A (VAP line holds the subsidiaries): the company's 35.4% mixes a consolidated numerator with a standalone denominator. On consolidated revenue the share is 34.18% vs 30.72% (+3.45 pp). The dairy subsidiaries' net revenue (0.95 to 15.65 Cr) is up to 13.5% of the Rs 109.2 Cr VAP rise. Excluding it, VAP growth is about +27.7%. On this reading the parent's own "Others" must have grown about 43-45%.
- Reading B (VAP line is standalone; all subsidiary revenue sits in "Others"): "Others" growth tracks the subsidiary revenue gap (H1 +53.5 vs +52.6 Cr). The parent's residual moves little (+8.4% Q2, +1.1% H1). The 35.42% vs 31.35% (+4.07 pp) is then on one consistent basis, and VAP growth carries no shown subsidiary content.
- The deck titles slide 7 "Consolidated" (P-l181), and the split sums to L407. That makes reading A a fair default. It does not prove that the VAP line itself holds subsidiary revenue. The review marks the question RESOLVED and charges management with a mixed basis. Rule J sets the same evidence bar for a bear claim, so both readings must stand until the separating observation arrives: management's basis for the VAP line, or subsidiary revenue by product line (Q31).

---

## 3. ADVERSARIAL READ

The run-1 counters to the cash-conversion claim moved it to INDETERMINATE, so it is no longer a positive claim. The three most positive claims left in the loop-1 review are below. Each counter uses only the extract.

### PC1. "Value-added products grew 32% YoY to Rs 451.0 Cr and are the growth engine; VAP share rose 30.72% to 34.18% on a consistent base" (R-L804, R-L824, R-L665)

Strongest bear counter:
- Price or mix makes up about 40% of growth in curd, paneer and ice cream (PR-L87-90). This counter is present (R-L342, R-L825) and recomputes.
- VAP slowed from +39.75% YoY in Q1 to +31.95% in Q2, and fell 20.0% QoQ (R-L340). Gross margin fell 271 bps against the mix gain (R-L826). Both are present.
- Under reading A, up to 13.5% of the VAP rise is dairy-subsidiary net revenue. That revenue was Rs 0.95 Cr a year earlier and Rs 15.65 Cr now (L461 minus L119), so organic VAP growth is nearer +27.7%. This counter does not survive as a fact. It holds only under reading A, and the review asserts reading A as RESOLVED without the extract settling it (F1). The review's grafted "consolidated VAP holds loss-making subsidiaries" line has the same gap, plus an out-of-corpus product tag for Get-A-Way (F2).

Survives: the price and deceleration counters survive and are present. The subsidiary-content counter must be re-stated as one of two readings (F1, F2).

### PC2. "Q2 margin recovered 98 bps from the Q1 trough; core PBT +44.6% QoQ; opex fell 138 bps as a share of revenue" (R-L802, R-L665, R-L382, R-L446)

Strongest bear counter:
- The same Q1-to-Q2 step happened in FY26 (+44 bps Op margin, +74 bps gross margin). H2 FY26 gross margin then ran 183 bps below Q2. The Q2 FY27 gain splits +63 / +58 / -23 bps and came with a Rs 48.32 Cr stock drawdown. Opex leverage rides on price-led revenue: milk volume +2.5% against realisation +6%. All of this is present (R-L397, R-L446, R-L803, Q34) and recomputes.
- Scope check: Q2 FY26 also drew stock down, by Rs 66.67 Cr (L413). The drawdown counter therefore applies to the QoQ reading, not the YoY one, and the review scopes it QoQ. That is correct.

Survives: yes, and it is present. Nothing new survives.

### PC3. "Mechanics are clean: unmodified limited-review conclusions, every statement ties" (R-L785; "clean limited-review conclusions", R-L665)

Strongest bear counter:
- One subsidiary was not reviewed by its auditor. Its Q2 revenue was Rs 14.26 Cr and its Q2 loss Rs 1.08 Cr, and the conclusion rests on management-certified figures (L721-733). A limited review is not an audit (L349-353).
- Two cross-statement movements do not tie. Standalone other financial liabilities show +Rs 27.01 Cr in the cash flow (L246) against -Rs 14.81 Cr on the balance sheet (L190, L202). The Rs 7.20 Cr cash investment in subsidiaries (L255) compares with a Rs 0.05 Cr rise in the investment line (L163).

Survives: yes. It is present at R-L144, R-L506 and F7 (R-L779). The verdict sentence "every statement ties" sits beside F7 without a qualifier; that is wording only (S10).

### MANDATORY ACQUISITION-ECONOMICS PROBE (re-run)

The documents describe acquisitions: control of Heritage Novandie from 16 Jun 2025 (L645), and "Strategic Acquisitions Scaling Up" with Novandie "wholly owned" and Get-A-Way "71%-owned" (PR-L146-148).

- Multiple: consideration is NOT FOUND. Cash proxy: Rs 16.22 Cr net FY26 consolidated outflow (L600) against target earnings below zero in every disclosed period. Dairy-subsidiary segment result was -Rs 3.54 Cr in FY26 and -Rs 3.15 Cr in H1 FY27 (L468 minus L125). Price / target PAT = not meaningful; no positive earnings multiple exists.
- Quality markers: target ROCE, debt, cash and customer tenure are NOT FOUND.
- Exposure: goodwill Rs 7.19 Cr plus Rs 13.45 Cr of other intangibles outside the parent = Rs 20.63 Cr (L507-508, L160), 2.9x the goodwill alone.
- Bear reading: the deals are presented as scaling with no revenue or profit disclosed, and the acquired dairy businesses lose money at a widening rate. Survives. It is grafted in full at Step 5F (R-L527-540), Q14, Q32, M8 and F5, and every number recomputes. Nothing further to graft.

---

## 4. FINDINGS (tagged)

### FACTUAL (loop A4)
- F1. VAP-share basis asserted as resolved. R-L169 marks the question "RESOLVED ... Mixed basis ... +3.45 pp, not +4.1 pp". Q19 (R-L712, YAML R-L899) tells management that mixed bases overstate the mix shift. Brief part 3 (R-L824) calls 34.18% vs 30.72% "a consistent base". F8 (R-L780) and the YAML flags (R-L937) list "VAP share on a mixed base". The extract proves only the denominator (standalone revenue, L75). It does not prove that the VAP line holds subsidiary revenue. The deck "Others" line rose Rs 27.6 Cr in Q2 and Rs 53.5 Cr in H1. Consolidated minus standalone revenue rose Rs 24.1 Cr and Rs 52.6 Cr over the same periods (L407, L75; P-l187-219). Standalone revenue less Milk, VAP and Fat moves only from Rs 41.4 to 44.9 Cr (Q2, +8.4%) and Rs 81.9 to 82.7 Cr (H1, +1.1%). Under reading A the same residual would have to grow about 43-45%. That fits a standalone VAP line, under which the printed 35.4% and +4.1 pp are consistent. The subsidiary-content counter at R-L342, R-L666 and R-L825 rests on the same unestablished premise. Fix: state two readings and the separating observation (graft text 1).
- F2. Out-of-corpus product tag. R-L827 says "ice cream (Get-A-Way, 71%-owned)" under [MGMT/FILED]. R-L342 and R-L825 say "yogurt and ice-cream subsidiaries", and R-L836 says "subsidiaries (ice cream, yogurt)". The extract names Get-A-Way only as "71%-owned" with "robust revenue growth" (PR-L147). No line in any fulltext ties it to ice cream; Alpenvie is the ice-cream range named (PR-L159). Fix: drop the product or tag it [INFERENCE, outside corpus] (graft text 2). The attribution entered through A5 run-1 graft text.

### MISSING
None. The three run-1 surviving bear counters and the acquisition probe are now in the review. No new counter survives outside F1.

### CONTRADICTION
None. C1 and C2 are resolved; no new internal inconsistency was found.

### STYLE (logged, no loop)
- S9. Slide 9 has a second extract indicator for reading B that the review does not use. The legend lists "Cow milk" first and "Buffalo milk" second (P-l295). In every month, the lower series' value label sits left of the month label and the higher series' label sits right of it (Apr: 38.80 at col 7, "Apr" at col 15, 51.59 at col 21; P-l276-293). Under the usual clustered-chart convention (legend order = bar order), cow is the lower, Rs 39-41/L series. Add this as supporting evidence at R-L362; keep both readings and the separating observation.
- S10. R-L785 says "every statement ties" while F7 (R-L779) lists two cross-statement mismatches. Suggested wording: "each statement's internal arithmetic ties; two cross-statement movements do not (F7)".
- S11. R-L804 says the price share is "price, not volume". The derivation (R-L342, R-L825) says "price or mix". Align the wording.
- S12. A1 R064/R066 swap the category labels for the H1 FY27 slide 7 values. 1753 sits under the Others H1FY27 header (P-l206 col 86; header P-l219 cols 82-87), and 1,614 sits under Fat H1FY27 (P-l207 col 65; header cols 64-69). A4's table (R-L337-338) uses the correct positions. Add the swap to the ledger-hygiene line.
- Carried from run 1, upstream A1/A2, no loop: S3 (agenda_items 0 vs 2), S4 (3 slide-8 dash cells), S5 (number-word claims), S6 (R250 label), S7 (R178/R181 species under a month-only flag).

---

## 5. GRAFT TEXT FOR A4 (ready to paste; numbers anchored)

1. F1, Step 0G row PR-A3-03 / PRE-A3-19 (R-L169), replacing the Status cell. Disposition index R-L68 and R-L73 become "Cross-doc partly resolved (denominator)":
"PARTLY RESOLVED. The denominator is standalone revenue (4,510 / 12,733.76 = 35.42%, L75). The numerator's basis is open, with two readings. Reading A: the VAP line is consolidated and holds the dairy subsidiaries. Their net dairy segment revenue rose from Rs 0.95 Cr to Rs 15.65 Cr YoY (L461 minus L119), up to 13.5% of the Rs 109.2 Cr VAP rise. The 35.4% then mixes bases, and the consistent consolidated share is 34.18% vs 30.72% (+3.45 pp). Reading B: the VAP line is standalone and all subsidiary revenue sits in 'Others'. 'Others' rose Rs 27.6 Cr in Q2 and Rs 53.5 Cr in H1, against a consolidated-minus-standalone revenue rise of Rs 24.1 Cr and Rs 52.6 Cr (L407, L75; P-l187-219). Standalone revenue less Milk, VAP and Fat moves little (Rs 41.4 to 44.9 Cr in Q2; Rs 81.9 to 82.7 Cr in H1). The printed 35.4% and +4.1 pp are then consistent. Separating observation: management's basis for the VAP line, or subsidiary revenue by product line (Q31)."
   - Q19 (R-L712, YAML R-L899): "Is the Rs 451.0 Cr VAP figure standalone or consolidated? If consolidated, will you restate VAP share on consolidated revenue (34.2%)?" Why: "On a consolidated numerator the 35.4% mixes bases (+3.45 pp); on a standalone numerator it is consistent (+4.1 pp)." Bull: "Standalone; the ratio is consistent." Bear: "Consolidated numerator kept over a standalone denominator."
   - Brief part 3 (R-L824): "VAP share rose 3.5 to 4.1 pp YoY: 35.42% vs 31.35% if the VAP line is standalone, or 34.18% vs 30.72% on consolidated revenue if it holds the subsidiaries. The filings do not say which [FILED/MGMT, derived]."
   - F8 (R-L780) and YAML flags (R-L937): replace "VAP share on a mixed base" with "VAP-share basis undisclosed (standalone or consolidated numerator)".
   - R-L342, R-L666, R-L825: open the subsidiary-content sentence with "If the VAP line is consolidated (reading A), ...".
2. F2 (R-L827): "Get-A-Way, 71%-owned (product line not stated in this corpus)". R-L342 and R-L825: "the yogurt subsidiary (Heritage Novandie) and Get-A-Way". R-L836: "the yogurt subsidiary and Get-A-Way competing against larger national brands at a loss". Where a product label is kept, tag it [INFERENCE, outside corpus].
3. S9 (optional, R-L362): "A second indicator also favours B. The legend lists cow first, and in every month the lower-series label sits left of the month label (P-l276-295). Under the usual chart convention, cow is the lower series [INFERENCE, positional]."

---

## VERDICT

INCOMPLETE. Loop back to: A4.
- FACTUAL: F1 (VAP-share basis asserted as RESOLVED and mixed; the extract supports a second, standalone reading); F2 ("Get-A-Way = ice cream" is not in the corpus but is tagged [MGMT/FILED]).
- MISSING: none. CONTRADICTION: none.
- All 13 run-1 loop findings (F1-F4, C1-C2, M1-M7) are resolved, and every loop-1 number recomputes. The deliverable gate passes, ledgers reconcile, and no orphan rows exist. The protocol verdict PROCEED WITH FLAGS is not challenged; F8 stands on its other items. Both fixes are text-only edits within A4.

## STYLE NOTES

S9-S12 (new) and S3-S7 (carried), recorded above. No re-run is triggered by any of them.

---

```yaml
stage: A5-adversary
company: "HERITGFOOD"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop: 1
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
  - {metric: "VAP share consistent-base mix shift and mixed-basis charge (Q2 FY27 vs Q2 FY26)", a4_value: "RESOLVED: mixed basis; +3.45 pp on consolidated revenue, not +4.1 pp (R-L169, Q19 R-L712, R-L824, F8 R-L780)", recomputed: "+3.45 pp only if the VAP line holds subsidiaries; +4.07 pp (35.42% vs 31.35%) if the VAP line is standalone; basis not established. Others +27.6 Cr Q2 / +53.5 Cr H1 vs C-S revenue gap +24.1 / +52.6 Cr; parent residual 41.4->44.9 Cr Q2 (+8.4%), 81.9->82.7 Cr H1 (+1.1%) vs about +43-45% needed under reading A", source_line: "L75, L407, L461, L119; P-l187-219 (R052-R067)"}
surviving_bear_counters: []
findings_by_type:
  factual:
    - "F1: VAP-share basis asserted RESOLVED as mixed (R-L169, Q19 R-L712/R-L899, brief R-L824, F8 R-L780, YAML flags R-L937); subsidiary-content counter rests on it (R-L342, R-L666, R-L825). Extract proves only the standalone denominator; deck 'Others' growth tracks the C-S revenue gap (H1 +53.5 vs +52.6 Cr), fitting a standalone VAP line under which 35.4% / +4.1 pp is consistent. State two readings and the separating observation."
    - "F2: 'Get-A-Way = ice cream' is not in the corpus (PR-L147 gives only '71%-owned', 'robust revenue growth') but is tagged [MGMT/FILED] at R-L827 and stated as fact at R-L342, R-L825, R-L836. Drop it or tag [INFERENCE, outside corpus]."
  missing: []
  contradiction: []
  style:
    - "S9: slide 9 legend order (cow first, P-l295) plus left/right label positions per month (P-l276-293) is a second extract indicator for reading B; add as support at R-L362, keep both readings"
    - "S10: R-L785 'every statement ties' sits beside F7 cross-statement mismatches; qualify as internal arithmetic"
    - "S11: R-L804 says 'price, not volume'; derivation says 'price or mix'"
    - "S12: A1 R064/R066 swap Fat/Others labels for H1 FY27 slide 7 values (1753 = Others, 1,614 = Fat by position P-l206-219); A4 table correct; note in hygiene line"
    - "S3-S7 carried from run 1 (upstream A1/A2): agenda_items count, slide-8 dash cells, number-word rows, R250 label, R178/R181 species flag"
loop_back_to: "A4"
gap: "A4 to fix F1 and F2 using audit Section 5 graft text. F1: restate the VAP-share basis as two readings (A: consolidated VAP line, +3.45 pp, mixed basis; B: standalone VAP line, +4.07 pp, consistent) with the separating observation (management's VAP basis or subsidiary revenue by product line, Q31) at R-L169, Q19 (R-L712, R-L899), brief R-L824, F8 R-L780, YAML flags R-L937; make the subsidiary-content counter conditional on reading A at R-L342, R-L666, R-L825. F2: remove or re-tag the 'Get-A-Way = ice cream' attribution at R-L342, R-L825, R-L827, R-L836."
style_notes:
  - "S9: add slide 9 legend-order and label-position evidence for reading B"
  - "S10: qualify 'every statement ties' against F7"
  - "S11: 'price or mix', not 'price, not volume'"
  - "S12: record A1 R064/R066 label swap in the ledger-hygiene line"
  - "S3-S7: carried upstream A1/A2 items, logged only"
analyst_note: "Loop-1 re-audit. All 13 run-1 loop findings are resolved and every new number recomputes: slide 9 readings, slide 17 vs 21 CAGR, the seasonal step, EBITDA-basis cash conversion, the acquisition probe and the S-vs-C table. The gate passes, the ledgers reconcile and no orphan rows exist. Two FACTUAL findings keep the verdict INCOMPLETE. Both are text-only fixes for A4, and neither moves PROCEED WITH FLAGS. F1: the review marks the VAP-share basis RESOLVED as mixed and tells management its +4.1 pp overstates the shift. The extract proves only the standalone denominator. The deck's Others line grows almost exactly with the consolidated-minus-standalone revenue gap (H1 +53.5 vs +52.6 Cr), which fits a standalone VAP line. Rule J applies the same bar to a bear claim, so both readings must stand. F2: the corpus never says Get-A-Way makes ice cream. Both errors entered partly through A5 run-1 graft text, and this fresh pass corrects them. The slide 9 legend order also favours reading B (S9)."
```
