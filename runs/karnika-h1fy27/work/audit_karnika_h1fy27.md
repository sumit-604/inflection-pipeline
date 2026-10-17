# A5 ADVERSARY / COMPLETENESS AUDIT | KARNIKA (Karnika Industries Limited) | h1fy27

Agent: A5 adversary, claude-opus-5-5. Audit date 2026-10-17.
Review under audit: runs/karnika-h1fy27/work/review_karnika_h1fy27.md (1,170 lines; cited below as `rev Lnnn`).
Inputs read: A1 fulltexts (`res`, `cc`, `ppt` + fulltext line), A1 structured files (row IDs `R###`), A2 ledgers (results, concall, presentation), A4 review. Source PDFs and `inputs/` not opened. A3 notes not read (re-derived independently).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location | Status |
|---|---|---|
| 1. Summary narrative | rev L1015-1031, 15 numbered lines (10-20 required) | PRESENT, real content |
| 2. Sector intelligence | rev L1033-1040, 6 bullets with provenance tags | PRESENT, real content |
| 3. Business-model intelligence | rev L1042-1049, 6 bullets | PRESENT, real content |
| 4. Competition intelligence | rev L1051-1057, 5 bullets | PRESENT, real content |
| 5. Forward map | rev L1059-1072, make-or-break reading + 8 catalyst rows, each with bull and bear fork | PRESENT, real content (2 rows undated, STYLE S5) |

Gate result: **PASS.** All five parts present and non-empty.

---

## 1. COVERAGE AUDIT

Fresh pass: grep and line sweep over the three A1 fulltexts, diffed against the A2 ledgers; structured row IDs counted by regex `^R\d{3} \|`.

| Doc | Category | A2 count | A5 fresh count | Orphan rows (ledger, absent in A4) | Status |
|---|---|---|---|---|---|
| results | numbered notes | 18 | 18 (notes 1-6, 11-13 at res L290-351 and L584-649) | none | PASS |
| results | unnumbered notes | 2 | 2 (res L334, L632) | none | PASS |
| results | line items | 210 | 210 (per table 29 / 26 / 44 / 32 / 35 / 44, res L137-176, L189-218, L232-281, L415-457, L469-510, L526-575) | none | PASS |
| results | zero-standing | 45 | 45 (grep ZERO_STANDING) | none | PASS |
| results | agenda items | 1 | 1 (res L44-50) | none | PASS |
| results | auditor paragraphs | 8 | 8 (res L90-115, L369-394) | none | PASS |
| results | entities | 4 | 4 (Karnika, Kidcity, Elementa Lifespaces, RDB Elementa) | none | PASS |
| results | structured IDs | 780 | 780 | none | PASS |
| concall | speaker turns | 167 | 167 (speaker-label regex) | none | PASS |
| concall | participants | 8 | 8 | none | PASS |
| concall | questions | 66 | **67** | n/a | **FAIL (M6)**: T87 (cc L723 "This is across both your outlets like your…", answered "Yes" at cc L726) is a clarification question, same form A2 counted at T60, T79, T124, T130, T136; A2 listed it as an acknowledgement |
| concall | mgmt numbers | 100 | 100 in structured + **5 spelled-out units absent from structured** | n/a | **FAIL (M7)**: cc L306 "four, five, or six retail outlets"; cc L704-705 "one and a half hours, an hour"; cc L867 "four or five brands" (FirstCry); cc L901 "two methods of billing"; cc L1027 "these three". A1 captured spelled counts elsewhere (R040, R042, R044, R071, R094); A2's digit-only sweep cannot see these |
| concall | forward / qualifier / date / entity | 47 / 20 / 22 / 53 | 47 / 20 / 22 / 53 (ID ranges R158-R204, R227-R246, R205-R226, R105-R157) | none | PASS |
| concall | structured IDs | 246 | 246 | none | PASS |
| presentation | slides | 32 | 32 (page markers) | none | PASS |
| presentation | numbers | 445 | 445 (per-slide recount: cover 1, S5 12, S6 1, S7 3, S8 19, S9 8, S10 20, S13 28, S14 112, S16 8, S17 6, S18 3, S20 1, S23 1, S24 8, S26 4, S27 22, S28 4, S29 68, S30 116) | none | PASS |
| presentation | zero-standing | 42 | 42 | none | PASS |
| presentation | structured IDs | 553 | 553 | none | PASS |

Ledger-to-review accounting. rev L16 states "All 20 notes, 167 turns and 32 slides reviewed" and "results 780 of 780, concall 246 of 246, presentation 553 of 553". Accepted as an explicit "reviewed" mark for every ledger row. Spot check: every note (rev L60-70), all 66 ledgered questions (rev L671-736), 13 of the deck's data slides by finding. **Orphan rows: none.** A2-flagged rows with no individual disposition are logged as STYLE S2.

A1 data-quality note (not a loop target, carried for the orchestrator). Presentation DATE rows R525-R528 are shifted one column. By fulltext column position, ppt L538 year labels sit at cols 98-101 (2024), 116-119 (2025), 140-143 (2026); "Acquired Kidcity Stake" (ppt L529) spans cols 108-129, "Karnika Industries ... Incorporated" (ppt L540) spans cols 45-62 (2022), "IPO & NSE Emerge Listing" (ppt L532) spans cols 64-87 (2023). R525 puts KIL incorporation at 2017; the CIN L17299WB**2022**PLC253035 (res L20) confirms 2022. R528 puts Kidcity at 2024; position and note 6 (res L318) put it at 2025. This error reached the review (F2).

---

## 2. ARITHMETIC AUDIT

All raw values in Rs Lakhs from the results fulltext; converted at x0.01. Tax = current + deferred + earlier-year (res L203-205, L483-485).

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Std Op EBITDA Q2FY26 / Q1FY27 / Q2FY27 / H1FY26 / H1FY27 / FY26 (Cr) | 14.45 / 10.33 / 15.16 / 19.43 / 25.49 / 34.93 | 1444.62 / 1032.87 / 1516.12 / 1943.23 / 2548.99 / 3492.68 L | res L190, L197, L198, L201 | PASS |
| Std Op EBITDA margin | 20.72 / 17.28 / 18.53 / 18.86 / 18.00 / 15.57% | 20.718 / 17.278 / 18.528 / 18.864 / 18.001 / 15.573% | res L189 | PASS |
| Std reported EBITDA | 14.56 / 11.95 / 16.26 / 20.46 / 28.22 / 43.61 | 1455.68 / 1195.36 / 1626.16 / 2046.48 / 2821.52 / 4360.80 L | res L197-201 | PASS |
| Std core PBT ex-OI | 12.65 / 8.77 / 13.59 / 15.87 / 22.35 / 27.91 | 1264.78 / 876.93 / 1358.56 / 1587.16 / 2235.49 / 2791.03 L | res L190, L201 | PASS |
| Std OI / PBT | 0.87 / 15.63 / 7.49 / 6.11 / 10.87 / 23.72% | 0.867 / 15.633 / 7.493 / 6.108 / 10.866 / 23.724% | res L190, L201 | PASS |
| Std ETR | 26.41 / 29.27 / 26.35 / 26.26 / 27.56 / 27.09% | 336.96/1275.84 = 26.411; 304.23 = 29.269; 386.92 = 26.346; 443.97 = 26.264; 691.15 = 27.557; 991.42 = 27.094% | res L203-205 | PASS |
| Std PAT margin | 13.47 / 12.30 / 13.22 / 12.10 / 12.83 / 11.89% | 13.465 / 12.299 / 13.219 / 12.100 / 12.830 / 11.894% | res L206 | PASS |
| Std gross margin | 38.54 / 37.48 / 38.64 / 41.99 / 38.15 / 36.37% | COGS 4285.72 / 3737.36 / 5020.98 / 5975.65 / 8758.34 / 14270.99 L: 38.536 / 37.479 / 38.640 / 41.991 / 38.150 / 36.370% | res L193-195 | PASS |
| Share-adjusted EPS (PAT / 619.975 lakh) | 1.51 / 1.19 / 1.74 / 2.01 / 2.93 / 4.30 | 1.514 / 1.186 / 1.745 / 2.011 / 2.931 / 4.303 | res L206, L214 | PASS |
| Cons Op EBITDA Q1 / Q2 / H1 / FY26 | 12.71 / 19.96 / 32.67 / 37.25 | 1271.13 / 1995.59 / 3266.72 / 3725.35 L | res L470, L477-478, L481 | PASS |
| Cons Op EBITDA margin | 17.23 / 18.79 / 18.15 / 14.99% | 17.231 / 18.791 / 18.151 / 14.993% | res L469 | PASS |
| Cons reported EBITDA; core PBT | 14.42 / 21.06 / 35.48 / 45.94; 11.07 / 18.28 / 29.35 / 30.19 | 1442.40 / 2105.76 / 3548.16 / 4594.30; 1106.63 / 1828.21 / 2934.84 / 3018.74 L | res L470-481 | PASS |
| Cons OI/PBT; ETR | 13.40 / 5.68 / 8.75 / 22.35%; 28.50 / 26.04 / 27.02 / 26.98% | 13.402 / 5.684 / 8.750 / 22.351%; 28.496 / 26.044 / 27.018 / 26.983% | res L470, L481, L483-485 | PASS |
| Cons PAT margin (after associates); gross margin | 12.39 / 13.35 / 12.96 / 11.42%; 34.29 / 34.82 / 34.61 / 33.61% | 12.386 / 13.353 / 12.956 / 11.424%; 34.290 / 34.825 / 34.606 / 33.613% | res L473-475, L488 | PASS (Q2 GM 34.825 rounds either way) |
| Cons parent EPS share-adjusted | 1.45 / 2.10 / 3.55 / 4.51 | 1.450 / 2.098 / 3.547 / 4.510 | res L498 | PASS |
| Kidcity implied (C minus S) revenue Q1 / Q2 / H1 / FY26 | 13.99 / 24.37 / 38.36 / 24.20 | 1399.42 / 2437.02 / 3836.44 / 2419.76 L | res L189, L469 | PASS |
| Kidcity implied Op EBITDA, margin; PAT, margin | 2.38 / 4.79 / 7.18 / 2.33 (17.0 / 19.7 / 18.7 / 9.6%); 1.79 / 3.52 / 5.30 / 1.71 (12.8 / 14.4 / 13.8 / 7.1%) | 238.26 / 479.47 / 717.73 / 232.67; 178.56 / 351.86 / 530.42 / 170.93 L; margins match | as above + res L206, L486 | PASS |
| Std Q2 YoY: revenue / Op EBITDA / margin / core PBT / PBT / PAT / EPS | +17.4% / +4.9% / -219 bps / +7.4% / +15.1% / +15.2% / -47.1% | +17.36% / +4.95% / -219.0 bps / +7.41% / +15.11% / +15.21% / -47.1% | res L189-217 | PASS |
| Std Q2 YoY: D&A / finance / EBIT / OI | -57.7% / +1.1% / +6.8% / +895% | -57.69% / +1.11% / +6.79% / +894.9% | res L190, L197-198 | PASS |
| Std H1 YoY: revenue / Op EBITDA / margin / EBIT / core PBT / PBT / PAT | +37.5 / +31.2% / -86 bps / +34.7 / +40.8 / +48.4 / +45.8% | +37.46 / +31.17% / -86.4 bps / +34.74 / +40.85 / +48.37 / +45.77% | res L189-206 | PASS |
| Q1FY27 vs derived Q1FY26 revenue | +79.6% (on 33.29) | 5977.78 / 3328.59 = +79.59% | res L189 | PASS |
| Gross debt rise H1 (std) | 8.44 Cr | 7892.55 - 7048.77 = 843.78 L | res L163, L168 | PASS |
| Mgmt headline growth (mixed basis) | +52.3 / +38.1 / +51.0 / +38.5 / +74.7 / +88.3 / +87.1% | +52.31 / +38.14 / +51.03 / +38.50 / +74.71 / +88.32 / +87.07% | res L189, L469, L486-498 | PASS |
| Margin-drop decomposition | Other exp 16.75 vs 14.98% (+1.77 pp); staff +0.52 pp; Q1FY26 GM 49.23% | 16.753 vs 14.980; 3.358 vs 2.838; 1689.93 / 3328.59 COGS ratio = GM 49.23% | res L193-199 | PASS |
| OI diagnostics | H2FY26 OI 7.65 Cr = 38.9% of H2 PBT 19.69; proxies 2.51 Cr = 92% of H1 OI | 764.87 / 1968.74 = 38.85%; 139.05 + 52.10 + 59.48 = 250.63 = 91.96% of 272.53 | res L190, L201, L237-243 | PASS |
| Std H2FY26 (derived) revenue / margin / core PBT | 121.27 / 12.78% / 12.04 | 12126.84 / 12.777% / 1203.87 L | res L189-201 | PASS |
| Std QoQ and run-rates | Q2FY26 +109.5%; H2 avg -13.0%; Q1FY27 -1.4%; Q2FY27 +36.9% | +109.48 / -13.04 / -1.41 / +36.89% | res L189 | PASS |
| Group H2FY26 (FY26 consol - H1FY26 std) | 145.47 / 12.25% / 14.32; OI 7.66 | 14546.60 / 12.251% / 1431.58 / 765.70 L | res L189-201, L469-481 | PASS |
| Cons QoQ | Q1 +1.4% vs H2 avg; Q2 +44.0% | +1.43% / +43.96% | res L469 | PASS |
| Latest qtr vs H1 avg | +15.6% std; +18.0% cons | +15.57% / +18.02% | res L189, L469 | PASS |
| Implied H2FY27 for guides | std 127.53-138.74 (+5.2 to +14.4%); group 143.05-155.48 (-1.7 to +6.9%) | 127.53-138.74 (+5.16 to +14.41%); 143.05-155.48 (-1.66 to +6.88%) | cc L821, L189; res L189, L469 | PASS |
| Q2 PAT bridge components (Cr) | +2.51 / -1.79 / +0.24 / -0.02 / +0.99 / -0.51 / +0.01 = +1.43 | 250.71 / -179.21 / 23.82 / -1.54 / 98.98 / -50.91 / +0.95 = 142.80 L (= 1081.68 - 938.88) | res L189-206 | PASS |
| Q2 bridge shares | 175.6 / -125.5 / 16.7 / -1.1 / 69.3 / -35.7 / 0.7% | 175.57 / -125.50 / 16.68 / -1.08 / 69.31 / -35.65 / 0.67% | derived | PASS |
| H1 PAT bridge components | +7.28 / -1.22 / +0.41 / +0.02 / +1.69 / -2.15 / -0.32 = +5.70 | 728.02 / -122.29 / 40.86 / 1.71 / 169.28 / -214.74 / -32.44 = 570.40 vs actual 570.43 L (0.03 rounding residual) | res L189-206 | PASS |
| OI share of PBT gain; OI-revert test | 51% Q2, 21% H1; PAT 10.09 Cr, +7.4% | 51.35%, 20.70%; 1008.78 L, +7.45% | res L190, L201 | PASS |
| Cons sequential | PAT +5.04; core PBT +7.21; OI -0.61 | 504.26; 721.58 (7.22); -61.10 L | res L470, L481, L488 | PASS (7.21 vs 7.22 is rounding on rounded inputs, S7) |
| Std CFO / FCF / WC | (4.88) vs 18.46; CFO/PAT -0.27x vs 1.48x; FCF (1.79) vs 18.14; WC (23.85) vs +2.57 | (487.90) / 1846.18; -0.269x / 1.481x; (179.07) / 1814.18; (2385.42) / 256.91 L | res L255, L259, L264 | PASS |
| Std receivable / inventory / payable days; CCC | 109.7 to 141.7; 129.5 to 121.0; 41.9 to 64.0; 197.3 to 198.7 (+1.4) | 109.70 to 141.66; 129.54 to 121.00; 41.90 to 63.99; 197.34 to 198.67 (+1.33) | res L145, L147, L170-171, L189, L193-195 | PASS (+1.4 vs +1.33 rounding, S7) |
| Cons CFO/PAT, FCF, WC | -0.19x; (1.36); (28.87) | -0.189x; (135.79); (2886.79) L | res L549, L553, L558, L488 | PASS |
| Cons days and CCC | 128.8 to 147.4; 128.4 to 96.2; 75.0 to 84.1; 182.2 to 159.5 | 128.79 to 147.36; 128.41 to 96.19; 74.96 to 84.08; 182.24 to 159.47 | res L425, L427, L451-452, L469, L473-475 | PASS (arithmetic); interpretation fails adversarial read 3 |
| Net debt std / cons; ND/E | 70.40 to 78.61 (+8.21), 0.74x to 0.63x; 75.23 to 83.17 (+7.94), 0.75x to 0.62x | 7039.64 to 7860.78; 0.740 / 0.626; 7523.47 to 8317.33; 0.753 / 0.623 | res L148, L159, L163, L168, L428, L440, L444, L449 | PASS |
| Loans, investments, PPE | +102.9%; +8.2%; std -47.9%; cons -46.7% | +102.95%; +8.20%; -47.85%; -46.63% | res L137, L140, L149, L415 | PASS (cons PPE -46.7 vs -46.6 rounding on rounded inputs, S7) |
| Q1 NCI test | 0.15 Cr = 25% of Kidcity Q1 tax; expected 0.45 | Kidcity Q1 tax 364.15 - 304.23 = 59.92; x25% = 14.98 L (= NCI res L499); 25% of PAT 178.56 = 44.64 L | res L203-204, L483-484, L499 | PASS |
| Mar-26 cons Other Equity gap | 36.36 vs 34.42 = 1.94 Cr = FY26 OCI | 3635.61 - 3442.02 = 193.59 L = res L494 (193.59) | res L437, L507 | PASS (see M3: gap extends to two more lines) |
| EPS-implied weighted shares; diluted shares | 285.4 / 205.3 / 416.2 lakh; ~647 lakh | 285.37 / 205.34 / 416.18; 646.96 | res L206, L217, L498, L510 | PASS |
| Warrants | 6.40% max dilution; ~36.00 Cr due | 39.6686 / 619.975 = 6.398%; 3 x 1199.98 = 3599.94 L | res L308-312 | PASS |
| FY26 cons ROCE; ex-OI | 25.2%; 20.3% on CE "175.48" | EBIT 4428.20 / CE 17548.42 = 25.23%; 3559.25 / 17548.42 = 20.28% (CE 175.49) | res L440, L444, L449, L470, L477, L481 | PASS (denominator typo, S7) |
| H1 annualised ROCE vs deck 32% | 35.7% / 32.8% on avg CE 196.28 | 7009.54 / 19628 = 35.71%; 6446.66 / 19628 = 32.84% | res L440, L444, L449, L470, L477, L481 | PASS ("matches" should read "approximates", S8) |
| Guidance parts | FY27 349.14-380.35 (+40.5 to +53.1%); FY28 502.97-550.44; CAGR 42.3-48.8% | same; sqrt(2.0242) = 1.4227, sqrt(2.2152) = 1.4884 | cc L403, L411-412, L821; res L189, L469 | PASS |
| Kidcity ratios in Q4 / 8.5 | staff ~1%; ~168 receivable days; 18% of parent PAT; parent +21.0% over std | 48.91 / 3836.44 = 1.27%; 3540.14 / 7672.88 x 365 = 168.4; 397.82 / 2199.16 = 18.09%; +21.04% | res L147, L196, L427, L476, L498 | PASS |
| Misc | market CAGR ~5.1%; MG 24-32% of ~25 Cr; sc_gap_pat 6.4 / 24.3 / 32.5 / 29.2% | 5.12%; 24 / 32%; 6.41 / 24.29 / 32.53 / 29.19% | ppt L185-187; cc L719, L1071 | PASS |
| Concall tallies | specificity 24/47 = 0.51; quantified opening claims 13/25 = 52%; Q&A share 87%; grade tally 22/28/13/2/0/1 = 66 | 0.511; 52%; 874/999 = 87.5%; tally reproduces on 66 rows | cc L112-1110; rev L671-736 | PASS (tally must extend to 67 rows after M6) |
| Hedge count, "maybe" | 3 (L547, L565, L571); other soft hedges 9 | **4** (adds cc L471 "or maybe financial year end"); other soft hedges **10** | cc L471 | **FAIL (F3)** |

Arithmetic verdict: every derived metric in A4's tables reproduces within rounding. One count error (F3). No arithmetic mismatch above rounding.

---

## 3. ADVERSARIAL READ

### Claim 1 (most positive): "Kidcity PAT margin 10-13% ... H1 implied 13.8% ... Delivered or above" (rev L663; rev L870 "CONFIRMED (top of band)"; rev L413), with the deck framing the Kidcity acquisition as a win (ppt L421-444).

**MANDATORY ACQUISITION-ECONOMICS PROBE (Kidcity, 75%, 04-Oct-2025, res L318-327).**
- Consideration is not disclosed, but two independent routes derive it.
  - Route A, consolidation elimination: standalone investments 2,552.91 L (res L140) minus consolidated 2,169.96 L (res L420) = 382.95 L, less the Elementa equity-method loss 15.53 L (res L487) = **367.42 L**.
  - Route B, goodwill plus NCI: NCI at 31-Mar-2026 160.53 L (res L439) minus NCI share of FY26 PAT 42.73 L (res L499) = 117.80 L at acquisition. That implies Kidcity net assets of 471.20 L. 75% of that is 353.40 L, plus goodwill 14.03 L (res L418) = **367.43 L**.
- **~Rs 3.67 Cr for 75%. Implied 100% equity ~Rs 4.90 Cr. Kidcity TTM PAT (Oct-25 to Sep-26) = 1.71 (H2 FY26) + 5.30 (H1 FY27) = Rs 7.01 Cr [derived]. Price / TTM PAT = ~0.70x. On the first post-deal half annualised (3.42 Cr), ~1.43x. Price / deal-date book ~1.04x.** Karnika's 75% share of TTM PAT (Rs 5.26 Cr) exceeds the price paid.
- Quality markers do not explain the low multiple.
  - PAT margin went from 7.1% (H2 FY26) to 13.8% (H1 FY27) [derived].
  - Staff cost is 1.27% of revenue.
  - Receivables are at least Rs 35.40 Cr, about 168 days [derived: res L427 minus L147. This is a floor, since intra-group balances eliminate].
  - Borrowings are about Rs 4.61 Cr [derived: (1221.25 + 7131.96) - (1124.55 + 6768.00) L] and cash about Rs 0.04 Cr [35.88 - 31.77 L].
  - The customer base is concentrated: Kidcity is the "sole aggregator" for Hopscotch's Kolkata goods (cc L308-311).
  - The business is not cash-rich. It is debtor-heavy and carries debt equal to its deal-date net worth.
- Is the earnings year representative? No. H1 FY27 holds the festive Q2 (Kidcity Q2 margin 14.4% vs Q1 12.8%). The margin step-up came after Karnika began producing 60% of Kidcity's goods (cc L425-426).

**Strongest bear counter (same extract).** The price is low because the pre-deal business was small (net assets about Rs 4.71 Cr). The earnings that make it look cheap were produced after the deal, inside the group, partly on goods Karnika makes (cc L425-426). Transfer prices therefore set Kidcity's margin. Each rupee of margin booked in 75%-owned Kidcity instead of 100%-owned Karnika passes 25 paise to the NCI holder. That holder took Rs 1.33 Cr in H1 FY27 (res L499) and is not named. The seller, the consideration and the 25% holder are all undisclosed (note 6, res L318-327). The 13.8% "delivery" is therefore a group allocation, not an arm's-length margin. Separating observation: Karnika's H1 sales to Kidcity with their margin, plus the identity of the 25% holder.

**Survives: YES.** Graft into rev L663, L870 and L413 (qualify "Delivered/CONFIRMED"), Q15 and Q27 (rev L514, L526), and Brief section 3. Type: MISSING (M1).

Secondary probe, Elementa Lifespaces (res L343-348): Rs 2.00 Cr for 40% (20,00,000 shares). Implied 100% value is Rs 5.00 Cr. The group's share of loss is Rs 15.53 L in 69 days. That annualises to about Rs 2.05 Cr of loss a year at 100% [derived: 15.53 / 0.40 x 365/69], about 41% of implied equity. P/E is not meaningful. This is cash put into a loss-making non-kidswear associate during a negative-CFO half. Survives as a one-line graft to Q6 (rev L505). RDB Elementa (Rs 5.20 L for 26%, implied 100% value Rs 20 L, not allotted) is immaterial. Its multiple is not computable (no earnings disclosed).

### Claim 2: "pass-through worked in Q2 at gross level" (rev L233); Brief: "Raw material cost was passed on" (rev L1020).

**Bear counter.**
- The flat Q2 gross margin (38.64% vs 38.54%) is against a base that had already fallen 1,069 bps from Q1 FY26 (49.23%, rev L233).
- On the half, standalone gross margin fell 384 bps (41.99% to 38.15%; A4's own table, rev L120). The deck shows gross margin down from 44.6% (FY25) to 33.6% (FY26) (ppt L559).
- The CFO's cause list includes "processing charges" (cc L217-218). After the PPE sale and the job-work shift (cc L1000-1002), processing cost sits partly in Other Expenses, and A4's own Q17 says the COGS/other-expense split is unconfirmed (rev L516). Material-plus-conversion spread, 1 - (COGS + other expenses)/revenue, fell to 21.89% from 23.56% (-167 bps) YoY in Q2 [derived: res L189, L193-195, L199].
- The CFO says the next increase will again be absorbed for a quarter (cc L362-363).
- "Passed on" holds only for the Q2 YoY gross line and on an unconfirmed classification.

**Survives: YES (as a qualifier).** Graft into rev L233 and brief line 4 (rev L1020). Type: MISSING (M4).

### Claim 3: consolidated CCC "Better on this basis" 182.2 to 159.5 days (rev L344); management's 178 to 143 days "direction partly supported on consolidated basis" (rev L865).

**Bear counter.**
- The Mar-26 consolidated days divide full year-end balances (all of Kidcity) by FY26 flows that hold only about 6 months of Kidcity. A4 notes this for receivables only (rev L341).
- On a scope-matched basis (Mar-26 balances over annualised H2 FY26 group flows: revenue 145.47 Cr, rev L255; COGS 164.96 - 59.76 = 105.20 Cr), Mar-26 receivable days were 110.0, inventory days 100.7, payable days 58.8, CCC 151.9 [derived: res L425, L427, L451-452]. Against A4's Sep-26 159.5, CCC **worsened by about 7.6 days**. Receivable days rose 110.0 to 147.4.
- In rupees, consolidated net working capital (receivables + inventory - payables) rose from 111.83 to 153.13 Cr (+41.30 Cr, +36.9%) [derived].
- The like-for-like standalone CCC is flat (rev L323), and the CFO says WC intensity stays the same (cc L835-838).
- Seasonal mismatch (festive H1 vs weak H2) affects A4's basis and this one alike. Neither supports "improved".

**Survives: YES.** Graft into rev L344 and L865 ("direction not supported on a scope-matched basis"). Type: MISSING (M5).

---

## 4. FINDINGS (tagged)

### FACTUAL (loop A4)
- **F1.** Q27 (rev L526; YAML rev L1121) asks "why is there no goodwill?". The consolidated balance sheet carries **Goodwill Rs 14.03 lakh** at both 31-Mar-2026 and 30-Sep-2026 (res L418). Fix: "why is goodwill only Rs 0.14 Cr on a ~Rs 3.67 Cr purchase [derived]".
- **F2.** Q27 (rev L526) states "Deck timeline says 2024; note 6 says 04-Oct-2025". The extract does not support this. Fulltext column positions put "Acquired Kidcity Stake" (ppt L529, cols 108-129) on the 2025 label (ppt L538, cols 116-119), not 2024 (cols 98-101). This matches note 6 (res L318). The source is A1 rows R525-R528, which are shifted one column (R525 dates KIL incorporation to 2017 against CIN ...WB2022PLC..., res L20). Remove the deck-vs-filing date contradiction.
- **F3.** Step 6C (rev L841) counts "maybe" 3 (L547, L565, L571). cc L471 also carries "maybe" ("calendar year end or maybe financial year end"). The count is 4 and other soft hedges are 10, not 9. The protocol-list total (6) and the hedge-heavy reading are unchanged.

### MISSING
- **M1 (A4; mandatory probe).** No Kidcity purchase multiple stated anywhere. Derived ~Rs 3.67 Cr for 75% = ~0.70x TTM PAT (Rs 7.01 Cr), ~1.04x book. The group-routed-earnings / NCI-leakage bear reading survives (section 3, claim 1). Also add the Elementa ~Rs 2.05 Cr annualised loss (41% of implied equity) to Q6.
- **M2 (A4).** Concall-vs-filing contradiction absent from Step 7A (rev L858-874). The CFO says of Kidcity "you do not have debtors here, you realize cash ... Here there is no debtor cycle" (cc L828-831). The filing implies Kidcity receivables of **at least Rs 35.40 Cr** at 30-Sep-2026 (consolidated 145.32 minus standalone 109.91; res L427, L147), about 168 days, rising Rs 14.85 Cr in H1 (res L542 minus L248). Kidcity's own described aggregation and B2B models (cc L268-270, L307-318) fit the filing, not the answer. Add a 7A row "CONTRADICTED". Re-grade Q&A row 43 (rev L713, graded B). Link to Q4 (rev L503), which already holds the 168 days.
- **M3 (A4).** Q8 (rev L507) treats the Mar-26 consolidated Other Equity gap as one cell, with a "typo" bull fork. The extract ties a three-line omission of the FY26 FVOCI loss in the Mar-26 consolidated balance sheet (labelled audited):
  - Investments are 251.03 L too high: 2,359.43 + 251.03 - 367.42 = 2,243.04 exactly (res L140, L420, L208).
  - DTA is 57.43 L too low: 85.16 - 57.43 + Kidcity 0.69 = 28.42. Kidcity's DTA of 0.69 rolls to 0.85 with its 0.16 H1 deferred credit (res L142, L422, L204, L484, L209).
  - Other Equity is 193.59 L too high (res L437 vs L507).
  - The Sep-26 consolidated OE rolls exactly from 34.42 Cr plus H1 parent TCI: 3,442.02 + 2,219.80 = 5,661.82 (res L437, L504, L507).
  - A typo would not balance across three lines, so the bull fork is weak. Sensitivity: FY26 consolidated ROCE becomes 25.5% (not 25.2%) and Mar-26 ND/E 0.77x (not 0.75x) on corrected equity Rs 98.02 Cr [derived].
- **M4 (A4).** Pass-through qualifier (section 3, claim 2).
- **M5 (A4).** CCC scope-matched counter (section 3, claim 3).
- **M6 (A2).** Concall question ledger misses T87 (cc L723), answered at cc L726 ("This is across our airport and malls revenue, consolidation"). Fresh count is 67 vs ledger 66. A4's Q&A inventory (rev L667-738), "66 questions" (rev L576) and grade tally follow. Content: the Rs 50 lakh per EBO at 13-14% target (cc L719-720) is a blend that includes airports, which the CFO earlier put at break-even (cc L547-548, L562).
- **M7 (A2).** Five spelled-out management numbers are absent from the concall structured file and not flagged MISSING_FROM_STRUCTURED: cc L306, L704-705, L867, L901, L1027. Low materiality. cc L867 ("four or five brands" for FirstCry) vs cc L1027 ("these three") is a minor internal inconsistency A3 can log.

### CONTRADICTION
- None beyond M2, which is tagged MISSING because the omission is in A4's cross-reference.

### STYLE (logged, no loop)
- **S1.** Six A3 IDs appear only in the YAML `a3_findings_incorporated` list (rev L1088), with no body anchor: R-A3-20, R-A3-23, P-A3-10, P-A3-14, P-A3-23, P-A3-24. Add a one-line "reviewed, no thesis impact" disposition.
- **S2.** A2-flagged rows with no individual disposition. They are covered by the blanket statement at rev L16, which is accepted:
  - finance cost P&L 272.49 vs cash flow 271.94 L (R104/R214)
  - H1 FY26 PBT 1690.41 vs 1690.42 (R129/R211)
  - signature after meeting end (R697)
  - ISIN OCR (R620)
  - cash asterisk with no footnote (R745)
  - concall transcription anomaly (R240)
- **S3.** Brief competition bullet 4 (rev L1056): "Established brands already own mall and airport space" carries no provenance tag. Anchor the airport half to cc L568-570 and mark the rest INFERENCE.
- **S4.** Brief competition bullet 2 (rev L1054) tags analyst-raised peers (Purple United, cc L862) as MGMT.
- **S5.** Forward map rows "Pending (IR email)" and "Undated" (rev L1066, L1070) carry no date.
- **S6.** rev L450, "associate loss (0.16) Cr per quarter and rising": 0.16 is a 69-day stub (res L348). Restate as about 0.21 Cr for a full quarter at the stub rate [derived], labelled INFERENCE.
- **S7.** Rounding on rounded inputs:
  - cons PPE -46.7% (raw -46.63%)
  - ROCE denominator "175.48" (raw 175.49)
  - cons core PBT QoQ +7.21 (raw +7.22)
  - std CCC +1.4 (raw +1.33)
- **S8.** rev L460: deck 32% ROCE "matches" a derived 32.8%. Say "approximates".

---

## VERDICT

**INCOMPLETE.** The gate passes and the arithmetic passes. The audit fails on MISSING (M1-M7) and FACTUAL (F1-F3) findings.
- Loop back to **A2** first: concall question ledger +1 (T87) and 5 MISSING_FROM_STRUCTURED units. This is a delta, not a re-enumeration.
- **A3**: delta review of the T87/T88 exchange and the 5 units only.
- **A4**: graft M1-M5, correct F1-F3, extend the Q&A inventory and tally to 67, and tidy S1-S8 while in the file.

---

## STYLE NOTES
S1-S8 above. Recorded only; none triggers a re-run by itself.

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
  missing_from_ledger:
    - "concall question 67 = T87 (cc L723, answered cc L726); A2 classed it as acknowledgement; fresh count 67 vs ledger 66"
    - "concall MISSING_FROM_STRUCTURED spelled-out mgmt numbers: cc L306, L704-705, L867, L901, L1027"
arithmetic_mismatches:
  - {metric: "Step 6C 'maybe' hedge count (other soft hedges)", a4_value: "3 (L547, L565, L571); other soft hedges 9", recomputed: "4 (adds cc L471); other soft hedges 10", source_line: "cc L471"}
surviving_bear_counters:
  - {claim: "Kidcity PAT margin 10-13% delivered or above at 13.8% H1 (rev L663, L870, L413); deck frames Kidcity deal as a win", counter: "Derived consideration ~Rs 3.67 Cr for 75% (two routes: investment elimination 367.42 L; goodwill 14.03 L + 75% of NCI-implied net assets 353.40 L) = ~0.70x Kidcity TTM PAT Rs 7.01 Cr, ~1.04x book. Cheap because pre-deal base was ~Rs 4.71 Cr; post-deal margin doubled 7.1% to 13.8% while Karnika makes 60% of Kidcity goods, so transfer prices set the margin and 25% leaks to an undisclosed NCI holder (Rs 1.33 Cr H1). Kidcity holds >= Rs 35.40 Cr receivables and ~Rs 4.61 Cr debt.", source_line: "res L140, L418, L420, L439, L487, L499; cc L425-426, L308-311", type: MISSING}
  - {claim: "Pass-through worked in Q2 at gross level; brief: raw material cost was passed on (rev L233, L1020)", counter: "Holds only on Q2 YoY gross line against a base already 1,069 bps below Q1 FY26; H1 gross margin -384 bps; COGS/other-expense split unconfirmed (A4 Q17); material-plus-conversion spread -167 bps YoY in Q2; CFO says next increase absorbed for a quarter", source_line: "res L189, L193-195, L199; cc L217-218, L362-363; ppt L559", type: MISSING}
  - {claim: "Consolidated CCC better 182.2 to 159.5; mgmt 178 to 143 direction partly supported (rev L344, L865)", counter: "Mar-26 days mix full Kidcity balances with ~6 months of Kidcity flows; scope-matched Mar-26 CCC 151.9 (rec 110.0, inv 100.7, pay 58.8 on annualised H2 FY26 group flows) so CCC worsened ~7.6 days and receivable days rose 110.0 to 147.4; net WC +Rs 41.30 Cr (+36.9%)", source_line: "res L425, L427, L451-452, L469, L473-475; cc L835-838", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): Q27 'why is there no goodwill?' wrong; consolidated Goodwill Rs 14.03 lakh at both dates (res L418)"
    - "F2 (A4): Q27 'Deck timeline says 2024' unsupported; ppt L529 cols 108-129 sit on 2025 label (ppt L538 cols 116-119); A1 rows R525-R528 shifted one column (CIN 2022, res L20)"
    - "F3 (A4): 'maybe' count 3 should be 4 (cc L471); other soft hedges 10 not 9"
  missing:
    - "M1 (A4): mandatory acquisition multiple absent; Kidcity ~Rs 3.67 Cr / TTM PAT 7.01 Cr = ~0.70x, ~1.04x book; bear reading survives; add Elementa ~Rs 2.05 Cr annualised loss (41% of implied equity) to Q6"
    - "M2 (A4): 7A omits CFO 'no debtors at Kidcity' (cc L828-831) vs >= Rs 35.40 Cr Kidcity receivables (~168 days, +14.85 Cr in H1; res L427, L147, L542, L248); regrade Q&A row 43"
    - "M3 (A4): Mar-26 consolidated BS omits FY26 FVOCI loss across three lines (investments +2.51 Cr, DTA -0.57 Cr, OE +1.94 Cr; res L420, L422, L437, L208-209, L507); Sep-26 OE rolls exactly from 34.42; Q8 'typo' fork weak"
    - "M4 (A4): pass-through qualifier (H1 GM -384 bps; Q2 conversion spread -167 bps)"
    - "M5 (A4): CCC scope-matched counter (Mar-26 151.9 vs Sep-26 159.5 days; net WC +41.30 Cr)"
    - "M6 (A2): concall T87 question missing from question ledger (66 vs 67)"
    - "M7 (A2): 5 spelled-out mgmt numbers missing from structured (cc L306, L704-705, L867, L901, L1027)"
  contradiction: []
  style:
    - "S1: six A3 IDs only in YAML list, no body anchor (R-A3-20, R-A3-23, P-A3-10, P-A3-14, P-A3-23, P-A3-24)"
    - "S2: A2-flagged rows lack individual disposition (R104/R214, R129/R211, R697, R620, R745, cc R240)"
    - "S3: brief competition bullet 4 sentence 2 untagged; anchor airport half to cc L568-570"
    - "S4: brief competition bullet 2 tags analyst-raised peers as MGMT"
    - "S5: two forward-map rows undated"
    - "S6: associate loss '(0.16) per quarter and rising' is a 69-day stub; ~0.21 Cr full-quarter [INFERENCE]"
    - "S7: rounding on rounded inputs (cons PPE -46.7 vs -46.63; CE 175.48 vs 175.49; +7.21 vs +7.22; CCC +1.4 vs +1.33)"
    - "S8: deck 32% ROCE 'matches' derived 32.8%; say 'approximates'"
loop_back_to: "A2"
gap: "A2: add concall question 67 (T87, cc L723-726) and flag 5 MISSING_FROM_STRUCTURED spelled-out numbers (cc L306, L704-705, L867, L901, L1027); delta only. A3: review those units only. A4: (a) state Kidcity purchase multiple (~Rs 3.67 Cr for 75% = ~0.70x TTM PAT 7.01 Cr, ~1.04x book) and graft the group-routed-earnings / NCI-leakage bear reading into rev L663, L870, L413, Q15, Q27, brief s3, plus Elementa annualised loss into Q6; (b) add 7A CONTRADICTED row: CFO 'no debtors' at Kidcity (cc L828-831) vs >= Rs 35.40 Cr Kidcity receivables, regrade row 43; (c) fix Q27: goodwill Rs 14.03 lakh exists (res L418) and deck places Kidcity at 2025 not 2024; (d) graft three-line Mar-26 FVOCI omission into Q8; (e) qualify pass-through (rev L233, L1020) and CCC (rev L344, L865); (f) 'maybe' count 4; extend Q&A inventory and tally to 67."
style_notes:
  - "S1: anchor six YAML-only A3 IDs in body"
  - "S2: add one-line dispositions for A2-flagged rows R104/R214, R129/R211, R697, R620, R745, cc R240"
  - "S3: tag brief competition bullet 4 sentence 2 (INFERENCE; airport half cc L568-570)"
  - "S4: retag analyst-raised peers in brief competition bullet 2"
  - "S5: date or mark the two undated forward-map rows"
  - "S6: restate associate loss as 69-day stub, ~0.21 Cr full quarter [INFERENCE]"
  - "S7: compute from raw lakhs, not rounded crores"
  - "S8: 'approximates' not 'matches' for deck ROCE 32% vs 32.8%"
analyst_note: "Arithmetic is clean: every derived cell reproduces from res/cc/ppt lines within rounding. The audit fails on content. (1) Mandatory acquisition probe: two independent routes (investment elimination; goodwill plus NCI) put the Kidcity price at ~Rs 3.67 Cr for 75%, ~0.70x Kidcity TTM PAT of Rs 7.01 Cr and ~1.04x deal-date book. The low multiple fits a small pre-deal base plus a post-deal margin doubling (7.1% to 13.8%) on goods Karnika makes; 25% of profit booked there goes to an undisclosed holder. (2) The CFO's 'no debtors at Kidcity' is contradicted by at least Rs 35.40 Cr of Kidcity receivables. (3) The Mar-26 consolidated balance sheet omits the FY26 FVOCI loss across investments, DTA and Other Equity, tied to the lakh; Q8's typo fork is weak. (4) Q27 errs twice: goodwill exists (Rs 0.14 Cr) and the deck dates Kidcity to 2025; A1 timeline DATE rows R525-R528 are shifted one column. A2 misclassified T87 and missed five spelled-out numbers; low materiality, but they are ledger gaps, so the loop starts at A2 as a delta."
```
