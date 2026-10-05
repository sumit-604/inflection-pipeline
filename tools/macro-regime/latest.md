## Macro regime read, 2026-09 (tools/macro-regime, 6-12 month horizon)

**Regime: REFLATION** (growth above its 5-year norm at z +0.59; inflation HIGH against the benchmarks CPI 3.0% / breakeven 2.5%, US CPI YoY 3.4%, breakeven 2.36%). Liquidity EASING. Global stress LOW. India stress NORMAL.

| Dial | Level (z) | 6m change | Inputs voting | Reading |
|---|---|---|---|---|
| GROWTH | +0.59 | +0.04 | 6 of 6 | high, flat |
| INFLATION | -0.16 | +0.41 | 4 of 4 | mid, rising |
| LIQUIDITY | +0.34 | -0.14 | 6 of 6 | mid, falling |
| STRESS | -0.52 | -1.13 | 5 of 5 | low, falling |
| IN_STRESS | +0.03 | -0.94 | 5 of 6 | mid, falling |

Exposure bands are switched off: the band table failed condition (a) of PASS_BAR.md (EVALUATION_2026-10.md, section 5). What each quadrant, liquidity and stress tag has meant for the six assets over the following 12 months is in that file, section 4.

Inputs, latest z-score (sign already applied):

- GROWTH: cu_au 6m log change +3.00; copper 6m log change +0.85; US industrial production YoY n/a; US recession probability (inverted) n/a; US 10y-2y curve level +0.69; Shanghai 6m log change -0.31
- INFLATION: US breakeven level +0.03; US breakeven 6m change +0.34; US CPI YoY n/a; US core CPI YoY 6m change n/a
- LIQUIDITY: US M2 YoY n/a; Fed assets 6m log change +0.70; Fed funds 6m change (inverted) +0.24; NFCI level (inverted) +1.13; dollar 6m change (inverted) +0.32; real yield 6m change (inverted) -1.03
- STRESS: VIX level -0.47; Baa spread level -1.28; St Louis stress index -1.07; EPU US level +0.03; EPU global level n/a
- IN_STRESS: India VIX level -0.43; EPU India level +1.04; USD/INR 6m log change -0.21; FPI equity 3m sum (inverted) -0.48; India call rate 6m change n/a; India CPI YoY (partial, ends 2025-03) n/a

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

| Month | Dist | Regime then | Liq | Stress | +6m | +12m | gold 12m | silver 12m | aluminium 12m | zinc 12m | brent 12m | nifty 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016-11 | 0.8 | DEFLATION | TIGHT | NORMAL | GOLDILOCKS | GOLDILOCKS | +9% | -0% | +21% | +26% | +32% | +24% |
| 2013-12 | 0.85 | GOLDILOCKS | NEUTRAL | LOW | DEFLATION | GOLDILOCKS | -1% | -20% | +10% | +10% | -50% | +31% |
| 2013-06 | 0.97 | GOLDILOCKS | NEUTRAL | LOW | GOLDILOCKS | DEFLATION | +8% | +8% | +1% | +16% | +8% | +30% |
| 2017-10 | 1.03 | GOLDILOCKS | TIGHT | LOW | GOLDILOCKS | DEFLATION | -4% | -15% | -5% | -18% | +22% | +0% |
| 2021-02 | 1.04 | GOLDILOCKS | EASING | NORMAL | REFLATION | REFLATION | +10% | -8% | +56% | +32% | +57% | +16% |
| 2014-09 | 1.05 | GOLDILOCKS | NEUTRAL | LOW | DEFLATION | DEFLATION | -8% | -15% | -20% | -25% | -50% | -0% |
| 2023-11 | 1.05 | STAGFLATION | TIGHT | LOW | REFLATION | DEFLATION | +30% | +21% | +17% | +18% | -9% | +20% |
| 2007-08 | 1.05 | GOLDILOCKS | TIGHT | NORMAL | STAGFLATION | STAGFLATION | +23% | +13% | +10% | -47% | +57% | -2% |

Now, same features (z): G +0.59, I -0.16, L +0.34, S -0.52, IN +0.03, G6 +0.04, I6 +0.41, L6 -0.14, real yield +1.52, curve +0.69, cu/au 6m +3.00, fed funds 6m -0.24, Baa spread -1.28, USD/INR 6m -0.21, Brent 12m +1.50, gold 6m -1.70

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

No direction call is made for any horizon. This is a regime read, not a forecast. Evaluation: EVALUATION_2026-10.md; bar: PASS_BAR.md; reading: VERDICT_2026-10.md.
