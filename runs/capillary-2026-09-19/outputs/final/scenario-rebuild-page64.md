# CAPILLARY scenario rebuild per page 64 (operator instruction 10-Oct-2026)

Run: runs/capillary-2026-09-19. This file replaces the revenue and margin paths in dossier Section 6.5. All other Section 6 rulings stand: ESOP Rs 14/15/16/17 Cr, D&A Rs 85/90/95/100 Cr (FY27 to FY30), finance cost Rs 5 Cr, tax 25%, 8.24 crore fully diluted shares, operating EPS with no treasury income, exit 30x on FY30 EPS at end-FY29, net cash in the bridge.
Arithmetic by Claude Code (orchestrator session). Stage 11, 14 and 15 outputs were built on the old Section 6.5 paths and are not re-run here.

---

## STEP 1. PAGE 64 VERIFIED (rendered image, not OCR)

Source: Analyst and Investor Day deck, filed BSE 14-May-2026, inputs/presentation/20260514-Investor-Presentation-65pp.pdf, page 64, "Long term outlook: Adjusted EBITDA in steady-state". Rendered at 150 dpi with PyMuPDF; image saved at inputs/presentation/page-images/20260514-deck-p64.png (page 63 beside it).

| Item | Quote from page 64 | Ferry figure | Comment |
|---|---|---|---|
| FY27 revenue | "Revenue estimate FY27 ₹ 1,065 Cr ... Organic - ₹ 673 cr. Inorganic - ₹ 392 cr." | 1,065 / 673 / 392 | Matches. |
| FY27 adj. EBITDA | "Adj. EBITDA estimate FY27 ₹ 172 Cr ... Organic - ₹ 152 cr. Inorganic - ₹ 20 cr." | 172 / 152 / 20 | Matches. Organic FY27 margin 22.6%; inorganic 5.1% [arithmetic]. |
| Inorganic retention and CM | "₹ 300 cr. (75%) inorganic retained in long-term"; "~45% margins generated - ₹ 135 cr. steady-state Inorganic CM" | 75%, Rs 300 Cr; ~45%, Rs 135 Cr | Matches. 300 / 0.75 = Rs 400 Cr base, about Rs 8 Cr above the FY27 Rs 392 Cr [arithmetic]. |
| Inorganic adj. EBITDA | "100-120 cr. Adj. EBITDA from inorganic"; right column "₹ 100-120 Cr Inorganic margin turnaround" | Rs 100-120 Cr long-term | CORRECTION: shown with a plus sign as an INCREMENT on top of FY27 Rs 172 Cr, not a level. The right column adds it: 172 + 100-120 = "₹ 270-290 Cr". FY27 already holds inorganic Rs 20 Cr, so the implied long-term inorganic LEVEL is Rs 120-140 Cr [arithmetic], consistent with the Rs 135 Cr steady-state CM. |
| Organic | "100-120 cr. Adj. EBITDA from organic over next 2 - 3 years"; "At 15% CAGR, organic generates ₹ 350 cr. more topline in 3 years"; "At ~35% margins (incl. central costs), the above generates ₹ 115 cr. more margins" | 15%, Rs 350 Cr; ~35%, Rs 115 Cr | Matches. Check: 673 × 1.15³ − 673 = Rs 350.6 Cr. 35% of 350 is Rs 122.7 Cr; the slide's Rs 115 Cr implies 32.9%, inside "~35%". Also an increment on FY27 organic Rs 152 Cr: level about Rs 252-272 Cr. |
| Long-term total | "₹ 270-290 Cr Long-term visibility with only inorganic margin play"; "₹ 100-120 Cr Organic margins from new ACV"; "₹ 370-410 Cr Long-term visibility" | organic Rs 270-290 Cr; total Rs 370-410 Cr | CORRECTION on the label: Rs 270-290 Cr is FY27 total (172) plus the inorganic turnaround, labelled "with only inorganic margin play". It is not an organic figure. Total Rs 370-410 Cr matches. |
| Horizon | "over next 2 - 3 years" | "next 2-3 years" | Attached to the ORGANIC block only. The inorganic block says "long-term" with no date. The total "Long-term visibility" carries no year. |

Page 63 ("Capital Allocation Priorities"): "20%+ Organic Revenue CAGR", "2x Operating Leverage on Non-CoGS", "75% Revenue Retention post integration", "45%+ FCF post integration"; guiding principle "20% organic growth". Use: page 64 is a quantified outlook with a stated base and governs the BASE case. Page 63 is a stated target with no base or date and governs the BULL case only.

SessionM months in FY27 Rs 392 Cr: NOT DISCLOSED on page 63 or 64. SessionM closed 01-May-2026 (AR Note 44 p.259), so FY27 can hold at most 11 months [INFERENCE]. Where it would be found: the Q4 FY26 call guidance bridge or the H1 FY27 results notes. A full FY28 year adds one month of SessionM, about Rs 22-23 Cr at USD 32 m ARR and about Rs 85 per USD [INFERENCE]. The slide's own Rs 400 Cr base (300 / 0.75) sits Rs 8 Cr above Rs 392 Cr. This rebuild applies retention to the slide-implied Rs 400 Cr base.

---

## STEP 2. SCENARIOS BY LINE

### Inputs

| Input | Bear | Base | Bull | Tag |
|---|---|---|---|---|
| FY27 consolidated revenue | 1,020 | 1,065 | 1,100 | approved (6.5) |
| FY27 organic revenue (deviation from 1,065 goes to organic) | 628 | 673 | 708 | [MGMT] p.64 base; [INFERENCE] allocation |
| FY27 inorganic revenue | 392 | 392 | 392 | [MGMT] p.64 |
| Organic growth FY28 to FY30 | 10% | 15% (p.64) | 20% (p.63) | [MGMT] base and bull; [INFERENCE] bear |
| Incremental margin on new organic revenue | 25% | 35% (p.64) | 40% | [MGMT] base; [INFERENCE] bear, bull |
| FY27 organic adj. EBITDA | 140.75 | 152 | 166 | [MGMT] base; bear and bull = 152 + margin × (organic revenue − 673) [INFERENCE] |
| Inorganic retention (on Rs 400 Cr), linear FY28 to FY29, flat FY30 | 65% (filed history about 67%, RHP pp.281-283 per dossier V3) | 75% (p.64) | 80% | [MGMT] base; [FILED] bear anchor via claude.ai; [INFERENCE] bull |
| Inorganic adj. EBITDA target level | 20 + 55 = 75 (50% of the Rs 110 Cr increment midpoint) by FY30 | 20 + 110 = 130 by FY30 | 20 + 120 = 140 by FY29 | [MGMT] p.64 increment, level read per the Step 1 correction |
| Inorganic adj. EBITDA ramp | linear from Rs 20 Cr (FY27) | same | same | [INFERENCE] |
| ESOP / D&A / finance cost / tax / shares | 14-17 / 85-100 / 5 / 25% / 8.24 Cr | same | same | approved (6.4, 6.5) |

### Formulas

- Organic revenue(t) = FY27 organic × (1 + g)^(t − FY27).
- Organic adj. EBITDA(t) = FY27 organic EBITDA + incremental margin × (organic revenue(t) − FY27 organic revenue).
- Inorganic revenue: FY27 392; FY28 = 392 + (target − 392) / 2; FY29 = FY30 = target, where target = 400 × retention.
- Inorganic adj. EBITDA: linear from 20 to the target level by FY30 (bear, base) or FY29 (bull), flat after.
- PBT = total adj. EBITDA − ESOP − D&A − finance cost. PAT = 0.75 × PBT. EPS = PAT / 8.24.

### Bear

| Rs Cr | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|
| Organic revenue | 628.0 | 690.8 | 759.9 | 835.9 |
| Inorganic revenue | 392.0 | 326.0 | 260.0 | 260.0 |
| Total revenue | 1,020.0 | 1,016.8 | 1,019.9 | 1,095.9 |
| Organic adj. EBITDA | 140.8 | 156.5 | 173.7 | 192.7 |
| Inorganic adj. EBITDA | 20.0 | 38.3 | 56.7 | 75.0 |
| Total adj. EBITDA | 160.8 | 194.8 | 230.4 | 267.7 |
| Adj. EBITDA margin | 15.8% | 19.2% | 22.6% | 24.4% |
| PBT | 56.8 | 84.8 | 114.4 | 145.7 |
| PAT | 42.6 | 63.6 | 85.8 | 109.3 |
| EPS (Rs) | 5.17 | 7.72 | 10.41 | 13.26 |

### Base

| Rs Cr | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|
| Organic revenue | 673.0 | 773.9 | 890.0 | 1,023.5 |
| Inorganic revenue | 392.0 | 346.0 | 300.0 | 300.0 |
| Total revenue | 1,065.0 | 1,119.9 | 1,190.0 | 1,323.5 |
| Organic adj. EBITDA | 152.0 | 187.3 | 228.0 | 274.7 |
| Inorganic adj. EBITDA | 20.0 | 56.7 | 93.3 | 130.0 |
| Total adj. EBITDA | 172.0 | 244.0 | 321.3 | 404.7 |
| Adj. EBITDA margin | 16.2% | 21.8% | 27.0% | 30.6% |
| PBT | 68.0 | 134.0 | 205.3 | 282.7 |
| PAT | 51.0 | 100.5 | 154.0 | 212.0 |
| EPS (Rs) | 6.19 | 12.20 | 18.69 | 25.73 |

### Bull

| Rs Cr | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|
| Organic revenue | 708.0 | 849.6 | 1,019.5 | 1,223.4 |
| Inorganic revenue | 392.0 | 356.0 | 320.0 | 320.0 |
| Total revenue | 1,100.0 | 1,205.6 | 1,339.5 | 1,543.4 |
| Organic adj. EBITDA | 166.0 | 222.6 | 290.6 | 372.2 |
| Inorganic adj. EBITDA | 20.0 | 80.0 | 140.0 | 140.0 |
| Total adj. EBITDA | 186.0 | 302.6 | 430.6 | 512.2 |
| Adj. EBITDA margin | 16.9% | 25.1% | 32.1% | 33.2% |
| PBT | 82.0 | 192.6 | 314.6 | 390.2 |
| PAT | 61.5 | 144.5 | 236.0 | 292.6 |
| EPS (Rs) | 7.46 | 17.53 | 28.64 | 35.51 |

Sensitivity, literal ferry reading (inorganic LEVEL Rs 55 / 110 / 120 Cr): FY30 EPS Rs 11.44 / 23.91 / 33.69; FY30 total adj. EBITDA Rs 247.7 / 384.7 / 492.2 Cr; value Rs 400 / 774 / 1,068.

---

## STEP 3. REVALUATION AT 30x FY30 EPS, END-FY29

- Net cash: Rs 57 per share, the approved bridge (31-Mar-2026; deck May-2026 p.59, cash and investments Rs 506.99 Cr less borrowings). Latest reading Rs 51.5 (30-Jun-2026, diluted; B11). Using Rs 51.5 lowers every value by Rs 5.5.
- CMP: two readings for 09-Oct-2026. Sharekhan Rs 566.65 (the ruled CMP, dossier Section 2) and Torus Rs 538.35. Claude Code does not hold the NSE close. Trendlyne's price tool refused on plan level. The tables use Rs 566.65 and show Rs 538.35 beside it. The NSE bhavcopy for 09-Oct-2026 settles it.

| Case | FY30 EPS | Value per share | CAGR from Rs 566.65 | CAGR from Rs 538.35 | Entry for 25% (÷ 1.953) | Entry for 30% (÷ 2.197) |
|---|---|---|---|---|---|---|
| Bear | 13.26 | 454.9 | −7.1% | −5.5% | 232.9 | 207.1 |
| Base | 25.73 | 828.9 | 13.5% | 15.5% | 424.4 | 377.3 |
| Bull | 35.51 | 1,122.4 | 25.6% | 27.7% | 574.7 | 510.9 |
| Weighted, Good 25/50/25 | | 808.8 | 12.6% | 14.5% | 414.1 | 368.1 |
| Weighted, Excellent 20/50/30 | | 842.2 | 14.1% | 16.1% | 431.2 | 383.3 |

- Upside/downside at Rs 566.65: (828.9 − 566.65) / (566.65 − 454.9) = 2.35x on base; 2.17x on the Good-weighted value. At Rs 538.35: 3.48x / 3.24x. The 2x line on base sits at Rs 579.6.
- Revised entry zone (30x P/E only, Good-weighted value): Rs 368 to Rs 414 (30% to 25% Tier A). Old zone: Rs 291 to Rs 328 (B11, triangulated with DCF at 20% weight); old 30x-only 25% entry: Rs 357.
- Dispersion: (1,122.4 − 454.9) / 828.9 = 80.5% (82.5% on the weighted value). Above 80%: the Small cap still binds, by a margin of 0.5 points.
- Starter price (A25): NOT RECOMPUTED. T1 stays Rs 265.8 per share (run-rate EPS Rs 6.96 × 30 + Rs 57), because the run rate does not change. T2 and T3 come from the expectation ledger, which stage 11 built on the old base. On the old ledger the starter price stays Rs 415. The new base adds about Rs 36 Cr of FY30 PAT, which would enlarge the ledger rows and lower the starter price once the ledger is refreshed.

---

## STEP 4. CROSS-CHECKS

- Base FY30 total adj. EBITDA Rs 404.7 Cr sits inside page 64's Rs 370-410 Cr. It is near the top because the base uses 35% on Rs 350.6 Cr of new organic revenue (Rs 122.7 Cr), where the slide prints Rs 115 Cr.
- Bull FY30 Rs 512.2 Cr exceeds the page-64 top of Rs 410 Cr. Stated reason: the bull uses page 63's 20% organic CAGR and a 40% incremental margin, where page 64 assumes 15% and ~35%. Page 64 caps the base, not the bull. Flag: the bull FY30 margin of 33.2% sits above management's stated 25-30%+ steady state (Q4 FY26 call, B05 guidance).
- Base FY30 margin 30.6% sits at the top of the 25-30%+ steady-state band.

What moved:

| FY30 base | Old (revenue-led, 6.5) | New (margin-led, page 64) | Change |
|---|---|---|---|
| Revenue | Rs 1,620 Cr | Rs 1,323.5 Cr | −Rs 296.5 Cr (−18%) |
| Adj. EBITDA | Rs 356.4 Cr (22.0%) | Rs 404.7 Cr (30.6%) | +Rs 48.3 Cr |
| PAT | Rs 176 Cr | Rs 212.0 Cr | +Rs 36 Cr |
| EPS | Rs 21.3 | Rs 25.73 | +21% |
| Value at 30x | Rs 696 | Rs 828.9 | +Rs 133 |
| Bear value | Rs 279 | Rs 454.9 | +Rs 176 |

The bear moved most. The old bear held a flat 15% margin on rising revenue. The new bear lets margin climb on the inorganic turnaround even as inorganic revenue falls. The new base needs less revenue and more margin, so it rests on the acquired-book turnaround.

Separating observation: inorganic contribution margin by Q4 FY27 (May-2027 results). Tracker row 4 (SessionM ARR at least USD 27 m and contribution margin at least 15%) and row 5 (Kognitiv migration and retained revenue). If inorganic adj. EBITDA is not on a path to Rs 56.7 Cr in FY28, the new base falls back toward the old one.

---

## PLAIN SUMMARY

1. Page 64 reads as the ferry block said, with one correction: Rs 100-120 Cr is the added inorganic EBITDA, so the long-term inorganic level is about Rs 120-140 Cr.
2. The new base earns Rs 25.73 a share in FY30 on less revenue (Rs 1,324 Cr) and a 30.6% margin; that is Rs 829 at 30x, or 13.5% a year from Rs 566.65.
3. The weighted value is Rs 809, a 12.6% CAGR. The 25% entry is Rs 414 and the 30% entry Rs 368.
4. Upside/downside now clears 2x at today's price (2.35x), because the bear rose to Rs 455. Gate 0 still blocks under Role 2 Section 7, and the dispersion cap still binds at Small.
5. The base now rests on the acquired books turning profitable; the Q4 FY27 inorganic contribution margin decides whether it holds.
