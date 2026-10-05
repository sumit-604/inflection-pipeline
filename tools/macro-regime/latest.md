## Macro regime read, 2026-09 (tools/macro-regime, 6-12 month horizon)

**Regime: REFLATION** (growth above its 5-year norm at z +0.59; inflation HIGH against the benchmarks CPI 3.0% / breakeven 2.5%, US CPI YoY 3.4%, breakeven 2.36%). Liquidity EASING. Global stress LOW. India stress NORMAL.

**India regime: GOLDILOCKS** (India growth on its 5-year norm at z +0.00 (on the line: the call can flip next month); India CPI YoY 4.82% against the 5.0% benchmark, IIP YoY 8.0%). **DIVERGENCE**: the India regime differs from the global one. The India regime governs Nifty and Indian rates; the global regime governs gold, silver, base metals and Brent.

| Dial | Level (z) | 6m change | Inputs voting | Reading |
|---|---|---|---|---|
| GROWTH | +0.59 | +0.04 | 6 of 6 | high, flat |
| INFLATION | -0.16 | +0.41 | 4 of 4 | mid, rising |
| LIQUIDITY | +0.34 | -0.14 | 6 of 6 | mid, falling |
| STRESS | -0.52 | -1.13 | 5 of 5 | low, falling |
| IN_STRESS | +0.02 | -0.62 | 6 of 6 | mid, falling |
| IN_GROWTH | +0.00 | +0.70 | 2 of 3 | mid, rising |

Exposure bands are switched off: the band table failed condition (a) of PASS_BAR.md (EVALUATION_2026-10.md, section 5). What each quadrant, liquidity and stress tag has meant for the six assets over the following 12 months is in that file, section 4.

Inputs, latest z-score (sign already applied; "carried" = last published value carried forward, up to 2 months):

- GROWTH: cu_au 6m log change +3.00; copper 6m log change +0.85; US industrial production YoY +0.47 (carried); US recession probability (inverted) -0.54 (carried); US 10y-2y curve level +0.69; Shanghai 6m log change -0.31
- INFLATION: US breakeven level +0.03; US breakeven 6m change +0.34; US CPI YoY -0.51 (carried); US core CPI YoY 6m change +0.07 (carried)
- LIQUIDITY: US M2 YoY +0.60 (carried); Fed assets 6m log change +0.70; Fed funds 6m change (inverted) +0.24; NFCI level (inverted) +1.13; dollar 6m change (inverted) +0.32; real yield 6m change (inverted) -1.03
- STRESS: VIX level -0.47; Baa spread level -1.28; St Louis stress index -1.07; EPU US level +0.03; EPU global level -0.34 (carried)
- IN_STRESS: India VIX level -0.43; EPU India level +1.04; USD/INR 6m log change -0.21; FPI equity 3m sum (inverted) -0.48; India call rate 6m change -0.20 (carried); India CPI YoY (MoSPI from 2014, OECD before) +0.05 (carried)
- IN_GROWTH: India IIP YoY (MoSPI) +0.91 (carried); India OECD CLI 6m change (partial, ends 2024-01) n/a; Nifty 6m log change -0.34

### Analogues

**REFLATION spells since 1998** (13, median length 3 months). What came next: GOLDILOCKS 8, STAGFLATION 4.

| Start | End | Months | Next regime |
|---|---|---|---|
| 2003-02 | 2003-03 | 2 | GOLDILOCKS |
| 2004-05 | 2004-06 | 2 | GOLDILOCKS |
| 2004-12 | 2004-12 | 1 | GOLDILOCKS |
| 2005-02 | 2005-04 | 3 | GOLDILOCKS |
| 2005-07 | 2005-09 | 3 | STAGFLATION |
| 2005-11 | 2006-08 | 10 | GOLDILOCKS |
| 2007-10 | 2007-10 | 1 | STAGFLATION |
| 2011-04 | 2011-08 | 5 | STAGFLATION |
| 2013-01 | 2013-03 | 3 | GOLDILOCKS |
| 2021-04 | 2022-02 | 11 | STAGFLATION |
| 2024-05 | 2024-05 | 1 | GOLDILOCKS |
| 2025-09 | 2025-10 | 2 | GOLDILOCKS |
| 2026-03 | 2026-09 | 7 | ongoing |

**Nearest past months to 2026-09** on the five dials, their 6-month changes, and eight inputs (real yield, curve, copper/gold, Fed funds change, Baa spread, USD/INR, Brent 12m, gold 6m). Distance is root-mean-square in z units; below 1.0 is close.

| Month | Dist | Regime then | India then | Liq | Stress | +6m | +12m | gold 12m | silver 12m | aluminium 12m | zinc 12m | brent 12m | nifty 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016-11 | 0.79 | DEFLATION | DEFLATION | TIGHT | NORMAL | GOLDILOCKS | GOLDILOCKS | +9% | -0% | +21% | +26% | +32% | +24% |
| 2013-12 | 0.85 | GOLDILOCKS | REFLATION | NEUTRAL | LOW | DEFLATION | GOLDILOCKS | -1% | -20% | +10% | +10% | -50% | +31% |
| 2013-06 | 0.97 | GOLDILOCKS | STAGFLATION | NEUTRAL | LOW | GOLDILOCKS | DEFLATION | +8% | +8% | +1% | +16% | +8% | +30% |
| 2017-10 | 1.03 | GOLDILOCKS | GOLDILOCKS | TIGHT | LOW | GOLDILOCKS | DEFLATION | -4% | -15% | -5% | -18% | +22% | +0% |
| 2021-02 | 1.04 | GOLDILOCKS | REFLATION | EASING | NORMAL | REFLATION | REFLATION | +10% | -8% | +56% | +32% | +57% | +16% |
| 2023-11 | 1.05 | STAGFLATION | REFLATION | TIGHT | LOW | REFLATION | DEFLATION | +30% | +21% | +17% | +18% | -9% | +20% |
| 2014-09 | 1.05 | GOLDILOCKS | REFLATION | NEUTRAL | LOW | DEFLATION | DEFLATION | -8% | -15% | -20% | -25% | -50% | -0% |
| 2007-08 | 1.05 | GOLDILOCKS | REFLATION | TIGHT | NORMAL | STAGFLATION | STAGFLATION | +23% | +13% | +10% | -47% | +57% | -2% |

Now, same features (z): G +0.59, I -0.16, L +0.34, S -0.52, IN +0.02, G6 +0.04, I6 +0.41, L6 -0.14, real yield +1.52, curve +0.69, cu/au 6m +3.00, fed funds 6m -0.24, Baa spread -1.28, USD/INR 6m -0.21, Brent 12m +1.50, gold 6m -1.70

### India regime analogues

**India GOLDILOCKS spells since 1998** (17, median length 3 months). What came next: REFLATION 12, DEFLATION 3, STAGFLATION 1.

| Start | End | Months | Next India regime | Global regime at end |
|---|---|---|---|---|
| 1999-07 | 2000-03 | 9 | REFLATION | STAGFLATION |
| 2002-12 | 2003-03 | 4 | REFLATION | REFLATION |
| 2003-05 | 2004-06 | 14 | DEFLATION | REFLATION |
| 2004-11 | 2005-10 | 12 | REFLATION | STAGFLATION |
| 2006-01 | 2006-04 | 4 | REFLATION | REFLATION |
| 2014-10 | 2014-12 | 3 | REFLATION | GOLDILOCKS |
| 2015-04 | 2015-04 | 1 | STAGFLATION | DEFLATION |
| 2016-09 | 2016-10 | 2 | DEFLATION | DEFLATION |
| 2017-05 | 2017-11 | 7 | REFLATION | GOLDILOCKS |
| 2018-02 | 2018-10 | 9 | DEFLATION | DEFLATION |
| 2020-12 | 2021-01 | 2 | REFLATION | GOLDILOCKS |
| 2021-04 | 2021-04 | 1 | REFLATION | REFLATION |
| 2021-09 | 2021-11 | 3 | REFLATION | REFLATION |
| 2023-10 | 2023-10 | 1 | REFLATION | STAGFLATION |
| 2024-03 | 2024-05 | 3 | REFLATION | REFLATION |
| 2024-07 | 2024-08 | 2 | REFLATION | DEFLATION |
| 2026-09 | 2026-09 | 1 | ongoing | REFLATION |

**Nifty 12 months on, by global x India pair** (months since 1998-05; the pair now is global REFLATION / India GOLDILOCKS). Regimes differ in 69% of months.

| Global | India | Months | Nifty 12m median |
|---|---|---|---|
| DEFLATION | DEFLATION | 27 | -0.4% |
| DEFLATION | GOLDILOCKS | 10 | +7.5% |
| DEFLATION | REFLATION | 25 | +21.9% |
| DEFLATION | STAGFLATION | 43 | +18.5% |
| GOLDILOCKS | DEFLATION | 21 | +18.2% |
| GOLDILOCKS | GOLDILOCKS | 40 | +12.6% |
| GOLDILOCKS | REFLATION | 39 | +15.9% |
| GOLDILOCKS | STAGFLATION | 19 | +2.1% |
| REFLATION | DEFLATION | 1 | -8.1% |
| REFLATION | GOLDILOCKS | 20 | +36.2% **<- now** |
| REFLATION | REFLATION | 14 | +13.4% |
| REFLATION | STAGFLATION | 8 | -1.9% |
| STAGFLATION | DEFLATION | 15 | -15.5% |
| STAGFLATION | GOLDILOCKS | 7 | +7.7% |
| STAGFLATION | REFLATION | 16 | +8.5% |
| STAGFLATION | STAGFLATION | 24 | +7.9% |

Series ending before the read month:

- us_cpi.csv ends 2026-08
- us_core_cpi.csv ends 2026-08
- us_m2.csv ends 2026-08
- us_monetary_base.csv ends 2026-08
- us_indpro.csv ends 2026-08
- us_recession_prob.csv ends 2026-08
- epu_global.csv ends 2026-07
- in_call_rate.csv ends 2026-07
- in_gsec_10y.csv ends 2026-07
- in_policy_rate_imf.csv ends 2022-07
- in_cpi_yoy.csv ends 2025-03
- in_m3.csv ends 2023-09
- in_cli.csv ends 2024-01
- imf_copper.csv ends 2026-07
- imf_aluminium.csv ends 2026-07
- imf_zinc.csv ends 2026-07
- in_iip_yoy.csv ends 2011-12
- in_cpi_yoy_mospi.csv ends 2026-08

No direction call is made for any horizon. This is a regime read, not a forecast. Evaluation: EVALUATION_2026-10.md; bar: PASS_BAR.md; reading: VERDICT_2026-10.md.
