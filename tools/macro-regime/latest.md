## Macro regime read, 2026-09 (tools/macro-regime, 6-12 month horizon)

**Regime: REFLATION** (growth rising, inflation rising). Liquidity EASING. Global stress LOW. India stress NORMAL.

| Dial | Level (z) | 6m change | Inputs voting | Reading |
|---|---|---|---|---|
| GROWTH | +0.59 | +0.04 | 6 of 6 | high, flat |
| INFLATION | -0.16 | +0.41 | 4 of 4 | mid, rising |
| LIQUIDITY | +0.34 | -0.14 | 6 of 6 | mid, falling |
| STRESS | -0.52 | -1.13 | 5 of 5 | low, falling |
| IN_STRESS | +0.03 | -0.94 | 5 of 6 | mid, falling |

| Asset | Band | How the band was set |
|---|---|---|
| gold | OVERWEIGHT | reflation base +0, +1 easing |
| silver | OVERWEIGHT | reflation base +1, +1 easing |
| aluminium | OVERWEIGHT | reflation base +1, +1 easing |
| zinc | OVERWEIGHT | reflation base +1, +1 easing |
| brent | OVERWEIGHT | reflation base +1 |
| nifty | OVERWEIGHT | reflation base +0, +1 easing |

Inputs, latest z-score (sign already applied):

- GROWTH: cu_au 6m log change +3.00; copper 6m log change +0.85; US industrial production YoY n/a; US recession probability (inverted) n/a; US 10y-2y curve level +0.69; Shanghai 6m log change -0.31
- INFLATION: US breakeven level +0.03; US breakeven 6m change +0.34; US CPI YoY n/a; US core CPI YoY 6m change n/a
- LIQUIDITY: US M2 YoY n/a; Fed assets 6m log change +0.70; Fed funds 6m change (inverted) +0.24; NFCI level (inverted) +1.13; dollar 6m change (inverted) +0.32; real yield 6m change (inverted) -1.03
- STRESS: VIX level -0.47; Baa spread level -1.28; St Louis stress index -1.07; EPU US level +0.03; EPU global level n/a
- IN_STRESS: India VIX level -0.43; EPU India level +1.04; USD/INR 6m log change -0.21; FPI equity 3m sum (inverted) -0.48; India call rate 6m change n/a; India CPI YoY (partial, ends 2025-03) n/a

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

No direction call is made for any horizon under 6 months. Bands are exposure tilts conditional on the regime, not forecasts. Evaluation: EVALUATION_2026-10.md; bar: PASS_BAR.md.
