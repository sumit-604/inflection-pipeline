# Market breadth digest: 2026-10-09

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-09: **69** of 79
- History available: 2019-07-01 to 2026-10-09, 694 dated rows
- Metrics with no reading for 2026-10-09: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 23.44 | +6.52 | +2.28 | -16.46 | 15 | 398 |
| % above 20 EMA | 23.36 | +3.95 | +0.14 | -17.34 | 18 | 398 |
| % above 50 EMA | 26.52 | +0.56 | -2.47 | -19.31 | 21 | 398 |
| % above 200 EMA | 36.11 | +0.54 | -2.38 | -12.19 | 41 | 398 |
| Net breadth (4% adv minus dec) | 3.79 | +23.11 | +9.51 | +1.56 | 62 | 398 |
| 4% advancers | 6.44 | +4.63 | +3.37 | +0.27 | 62 | 398 |
| 4% decliners | 2.65 | -18.47 | -6.14 | -1.30 | 46 | 398 |
| Net new highs minus lows | -4.46 | +1.71 | +1.89 | -5.30 | 14 | 398 |
| Net within 15% of 52wk H/L | -14.06 | +1.52 | -4.25 | -19.85 | 32 | 398 |
| Volume expansion ratio | 0.31 | -0.24 | -0.37 | -0.22 | 14 | 398 |
| Overbought count (weekly RSI>70) (as of 2026-10-05) | 134.00 | -15.00 | -124.00 | -10.00 | 49 | 380 |
| Oversold count (weekly RSI<30) (as of 2026-10-05) | 207.00 | +52.00 | +137.00 | +179.00 | 91 | 380 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 125.00 | -850.00 | 50 |
| `4_advance_decline__4_decline` | 63.00 | -440.00 | 45 |
| `4_advance_decline_today__4_decline` | 67.00 | -440.00 | 40 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 27.00 | -288.00 | 43 |
| `4_advance_decline__4_advance` | 153.00 | +110.00 | 54 |
| `4_advance_decline_today__4_advance` | 155.00 | +110.00 | 65 |
| `breadth_above_500_trend_reversal__above_20dma` | 500.00 | +85.00 | 16 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,762.00 | -85.00 | 95 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 91.00 | +70.00 | 60 |
| `current_previous_yr_volumes_crores__current` | 454.27 | -67.85 | 24 |

## At the edge of their own range

Top decile of history:

- `10_from_10dema__10_10ema` at 1.09 (percentile 99, range 0.09 to 1.10)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 11.00 (percentile 96, range 0.00 to 34.00)
- `52_wk_high_low__new_52_wk_low` at 5.29 (percentile 96, range 0.18 to 7.50)
- `breadth_above_500_trend_reversal__below_20dma` at 1,762.00 (percentile 95, range 78.00 to 1,985.00)
- `breadth_above_500_trend_reversal__below_50dma` at 1,685.00 (percentile 92, range 278.00 to 1,962.00)
- `5_advance_decline_ratio__advance` at 62.17 (percentile 90, range 13.35 to 70.21)

Bottom decile of history:

- `52_wk_high_low__new_52_wk_high` at 1.05 (percentile 4, range 0.86 to 5.21)
- `net_nh_nl__net_nh_nl` at -4.46 (percentile 5, range -6.35 to 3.67)
- `52_wk_high_low_today__new_52_wk_high` at 1.04 (percentile 5, range 1.04 to 3.65)
- `gold_etfs_nifty_1_month_chg__nifty` at -5.67 (percentile 7, range -6.93 to 6.35)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed up through 50: 21.00 to 91.00
- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 315.00 to 27.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.09 | +0.00 | +0.21 | +0.51 | 99 |
| `15_up_10_down__10_in_5d` | 2.95 | -1.72 | -1.51 | +1.52 | 80 |
| `15_up_10_down__15_in_5d` | 1.77 | +0.21 | +0.21 | -1.68 | 31 |
| `3_above_200_ema__pct` | 34.15 | +1.00 | -2.00 | -15.77 | 26 |
| `4_advance_decline__4_advance` | 153.00 | +110.00 | +80.00 | +6.00 | 54 |
| `4_advance_decline__4_decline` | 63.00 | -440.00 | -146.00 | -31.00 | 45 |
| `4_advance_decline_today__4_advance` | 155.00 | +110.00 | +16.00 | NOT FOUND | 65 |
| `4_advance_decline_today__4_decline` | 67.00 | -440.00 | -33.00 | NOT FOUND | 40 |
| `4_advance_decline_today__net_breadth` | 3.68 | +22.98 | +2.05 | NOT FOUND | 70 |
| `52_week_high_low_within_10__high` | 16.41 | +1.48 | -1.70 | -10.33 | 27 |
| `52_week_high_low_within_10__low` | 31.03 | -1.80 | +1.40 | +12.42 | 79 |
| `52_wk_high_low__new_52_wk_high` | 1.05 | -0.21 | -0.52 | -2.01 | 4 |
| `52_wk_high_low__new_52_wk_low` | 5.29 | -1.87 | -2.20 | +3.20 | 96 |
| `52_wk_high_low_today__new_52_wk_high` | 1.04 | -0.20 | -1.07 | NOT FOUND | 5 |
| `52_wk_high_low_today__new_52_wk_low` | 5.08 | -1.76 | +2.18 | NOT FOUND | 85 |
| `5_advance_decline_ratio__advance` | 62.17 | +48.83 | +14.78 | NOT FOUND | 90 |
| `5_advance_decline_ratio__decline` | 36.78 | -48.83 | -14.78 | NOT FOUND | 15 |
| `above_10ma__pct` | 24.23 | +8.70 | +5.17 | -14.10 | 15 |
| `above_200ma__above_200ma` | 34.15 | +1.00 | -2.00 | -15.77 | 27 |
| `above_20_ema__pct` | 21.42 | +3.98 | +0.76 | -17.70 | 13 |
| `above_20ma__pct` | 21.42 | +3.98 | +0.76 | -17.70 | 16 |
| `above_50_ema__pct` | 23.56 | +0.73 | -1.76 | -20.89 | 16 |
| `above_50ma__above_50ma` | 34.15 | +1.00 | -2.00 | -15.77 | 27 |
| `breadth_above_500_trend_reversal__above_200dma` | 861.00 | +22.00 | -43.00 | -349.00 | 38 |
| `breadth_above_500_trend_reversal__above_20dma` | 500.00 | +85.00 | +15.00 | -416.00 | 16 |
| `breadth_above_500_trend_reversal__above_50dma` | 577.00 | +13.00 | -47.00 | -493.00 | 17 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,401.00 | -22.00 | +44.00 | +347.00 | 79 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,762.00 | -85.00 | -14.00 | +414.00 | 95 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,685.00 | -13.00 | +48.00 | +491.00 | 92 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 11.00 | -1.00 | +5.00 | +7.00 | 96 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 27.00 | -288.00 | -77.00 | -31.00 | 43 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 18.00 | +0.00 | +7.00 | -25.00 | 61 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 91.00 | +70.00 | +43.00 | -16.00 | 60 |
| `current_previous_yr_volumes_crores__1_yr_back` | 396.33 | +12.99 | +7.99 | -88.29 | 43 |
| `current_previous_yr_volumes_crores__current` | 454.27 | -67.85 | -24.95 | -83.24 | 24 |
| `drawdowns_peaks__blw_3` | 125.00 | -850.00 | -333.00 | -111.00 | 50 |
| `gold_etfs_nifty_1_month_chg__gold` | -7.18 | +1.67 | -3.81 | -14.81 | 24 |
| `gold_etfs_nifty_1_month_chg__nifty` | -5.67 | +1.26 | +0.20 | -3.19 | 7 |
| `mbm_2_0_magnitude__abv_10ma` | 23.44 | +6.52 | +2.28 | -16.46 | 15 |
| `mbm_2_0_magnitude__abv_200ma` | 36.11 | +0.54 | -2.38 | -12.19 | 41 |
| `mbm_2_0_magnitude__abv_20ma` | 23.36 | +3.95 | +0.14 | -17.34 | 18 |
| `mbm_2_0_magnitude__abv_50ma` | 26.52 | +0.56 | -2.47 | -19.31 | 21 |
| `mbm_2_0_velocity_advanced__15_52wh` | 17.76 | +0.54 | -2.47 | -9.79 | 56 |
| `mbm_2_0_velocity_advanced__15_52wl` | 31.82 | -0.98 | +1.78 | +10.06 | 70 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.78 | -0.11 | +1.87 | +7.58 | 55 |
| `mbm_2_0_velocity_advanced__30_52wh` | 48.99 | +0.61 | -1.37 | -4.69 | 75 |
| `mbm_2_0_velocity_advanced__breakdowns` | 10.77 | -28.66 | -24.82 | +0.36 | 69 |
| `mbm_2_0_velocity_advanced__breakouts` | 16.88 | +8.90 | +6.99 | +3.06 | 63 |
| `mbm_2_0_velocity_advanced__down_close` | 24.61 | -28.96 | -0.10 | -13.29 | 11 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -14.06 | +1.52 | -4.25 | -19.85 | 32 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 0.21 | +0.71 | -3.24 | -12.26 | 55 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -4.46 | +1.71 | +1.89 | -5.30 | 14 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.18 | -0.12 | -0.42 | -2.18 | 32 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 5.64 | -1.84 | -2.31 | +3.12 | 88 |
| `mbm_2_0_velocity_advanced__up_close` | 38.15 | +15.52 | +7.09 | -6.53 | 54 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.09 | +0.00 | +0.21 | +0.51 | 87 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.95 | -1.72 | -1.51 | +1.52 | 68 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.77 | +0.21 | +0.21 | -1.68 | 44 |
| `mbm_2_0_velocity_basic__3_range` | 34.93 | +16.75 | +18.53 | -9.50 | 33 |
| `mbm_2_0_velocity_basic__4_advance` | 6.44 | +4.63 | +3.37 | +0.27 | 62 |
| `mbm_2_0_velocity_basic__4_decline` | 2.65 | -18.47 | -6.14 | -1.30 | 46 |
| `mbm_2_0_velocity_basic__5d_range` | 3.41 | +0.55 | +1.60 | -6.17 | 36 |
| `mbm_2_0_velocity_basic__net_breadth` | 3.79 | +23.11 | +9.51 | +1.56 | 62 |
| `mbm_2_0_velocity_basic__volume` | 0.31 | -0.24 | -0.37 | -0.22 | 14 |
| `net_breadth__net_breadth` | 3.79 | +23.11 | +9.51 | +1.56 | 61 |
| `net_nh_nl__net_nh_nl` | -4.46 | +1.71 | +1.89 | -5.30 | 5 |
| `new_high_low_bearishness_bullishness__high` | 30.00 | -6.00 | -15.00 | -62.00 | 27 |
| `new_high_low_bearishness_bullishness__low` | 151.00 | -54.00 | -63.00 | +88.00 | 90 |
| `volume__volume` | 0.31 | -0.24 | -0.37 | -0.22 | 13 |

## No reading for 2026-10-09

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-05, 60.97
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-05, 39.03
- `oversold_overbought_rsi__overbought`: last 2026-10-05, 134.00
- `oversold_overbought_rsi__oversold`: last 2026-10-05, 207.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-05, 0.32
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-05, 0.66


<!-- market-read -->

## Market read

Friday bounced after Thursday's break, and the bounce was ordinary. 91 stocks
rose four and a half percent or more, against 27 that fell that much. About six
stocks in ten closed higher, and 32 of 35 indices rose. The Nifty gained about
1.3 percent, led by IT, consumer staples and state banks. The big
companies led. Small and micro companies barely moved. The count of stocks
above the two-hundred-day average rose only from 839 to 861. That is still
below the 1 October low near 900. New yearly lows still beat new highs by
about five to one. Fear eased, and turnover came in lighter. A thrust day
would need about 300 big risers. Friday had under a third of that. The
market repaired a little of Thursday's damage and proved nothing yet.

Full brief: briefs/2026-10-09.html
