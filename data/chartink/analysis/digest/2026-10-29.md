# Market breadth digest: 2026-10-29

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-29: **69** of 79
- History available: 2019-07-01 to 2026-10-29, 707 dated rows
- Metrics with no reading for 2026-10-29: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 37.26 | +7.47 | +25.81 | +9.79 | 41 | 411 |
| % above 20 EMA | 24.46 | +4.40 | +12.38 | -4.44 | 20 | 411 |
| % above 50 EMA | 21.47 | +3.10 | +6.44 | -12.31 | 16 | 411 |
| % above 200 EMA | 29.77 | +1.20 | +0.80 | -11.75 | 31 | 411 |
| Net breadth (4% adv minus dec) | 6.78 | +2.94 | +14.44 | +5.47 | 81 | 411 |
| 4% advancers | 9.68 | +2.27 | +7.20 | +3.96 | 85 | 411 |
| 4% decliners | 2.91 | -0.68 | -7.24 | -1.51 | 53 | 411 |
| Net new highs minus lows | -1.35 | +1.39 | +10.53 | +3.41 | 29 | 411 |
| Net within 15% of 52wk H/L | -23.54 | +2.46 | +3.33 | -18.74 | 22 | 411 |
| Volume expansion ratio | 0.36 | +0.05 | -0.04 | -0.40 | 27 | 411 |
| Overbought count (weekly RSI>70) (as of 2026-10-26) | 66.00 | +10.00 | -135.00 | -98.00 | 23 | 383 |
| Oversold count (weekly RSI<30) (as of 2026-10-26) | 214.00 | -136.00 | +132.00 | +177.00 | 91 | 383 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__1_yr_back` | 120.18 | -319.12 | 1 |
| `breadth_above_500_trend_reversal__above_20dma` | 614.00 | +155.00 | 25 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,634.00 | -155.00 | 88 |
| `breadth_above_500_trend_reversal__above_50dma` | 502.00 | +84.00 | 15 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,747.00 | -83.00 | 94 |
| `4_advance_decline__4_advance` | 230.00 | +54.00 | 91 |
| `4_advance_decline_today__4_advance` | 232.00 | +54.00 | 91 |
| `drawdowns_peaks__blw_3` | 125.00 | -45.00 | 49 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 144.00 | +38.00 | 86 |
| `breadth_above_500_trend_reversal__above_200dma` | 699.00 | +35.00 | 25 |

## At the edge of their own range

Top decile of history:

- `breadth_above_500_trend_reversal__below_50dma` at 1,747.00 (percentile 94, range 272.00 to 1,996.00)
- `10_from_10dema__10_10ema` at 1.14 (percentile 92, range 0.09 to 7.07)
- `5_advance_decline_ratio__advance` at 62.24 (percentile 91, range 13.35 to 70.41)
- `4_advance_decline_today__4_advance` at 232.00 (percentile 91, range 33.00 to 409.00)
- `4_advance_decline__4_advance` at 230.00 (percentile 91, range 30.00 to 479.00)

Bottom decile of history:

- `current_previous_yr_volumes_crores__1_yr_back` at 120.18 (percentile 1, range 120.18 to 715.72)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 53.00 to 45.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.14 | -0.72 | -2.53 | +0.51 | 92 |
| `15_up_10_down__10_in_5d` | 3.16 | -1.73 | -14.74 | -0.12 | 78 |
| `15_up_10_down__15_in_5d` | 1.89 | +0.80 | +0.97 | -0.12 | 44 |
| `3_above_200_ema__pct` | 27.44 | +1.37 | +1.27 | -11.44 | 17 |
| `4_advance_decline__4_advance` | 230.00 | +54.00 | +171.00 | +94.00 | 91 |
| `4_advance_decline__4_decline` | 69.00 | -16.00 | -172.00 | -36.00 | 45 |
| `4_advance_decline_today__4_advance` | 232.00 | +54.00 | +171.00 | +157.00 | 91 |
| `4_advance_decline_today__4_decline` | 73.00 | -16.00 | -171.00 | -152.00 | 36 |
| `4_advance_decline_today__net_breadth` | 6.65 | +2.93 | +14.31 | +12.92 | 88 |
| `52_week_high_low_within_10__high` | 11.84 | +1.95 | +3.19 | -9.40 | 16 |
| `52_week_high_low_within_10__low` | 34.79 | -1.44 | -1.28 | +8.10 | 83 |
| `52_wk_high_low__new_52_wk_high` | 1.23 | +0.42 | +0.95 | -0.17 | 10 |
| `52_wk_high_low__new_52_wk_low` | 2.31 | -0.95 | -8.44 | -3.46 | 77 |
| `52_wk_high_low_today__new_52_wk_high` | 1.20 | +0.39 | +0.88 | -0.85 | 24 |
| `52_wk_high_low_today__new_52_wk_low` | 2.38 | -0.88 | -7.67 | -1.20 | 39 |
| `5_advance_decline_ratio__advance` | 62.24 | +8.76 | +34.67 | +41.67 | 91 |
| `5_advance_decline_ratio__decline` | 36.72 | -8.76 | -34.67 | -41.67 | 12 |
| `above_10ma__pct` | 42.75 | +12.27 | +30.52 | +18.43 | 52 |
| `above_200ma__above_200ma` | 27.44 | +1.37 | +1.27 | -11.44 | 18 |
| `above_20_ema__pct` | 26.98 | +7.51 | +14.51 | +1.47 | 22 |
| `above_20ma__pct` | 26.98 | +7.51 | +14.51 | +1.47 | 23 |
| `above_50_ema__pct` | 20.57 | +3.49 | +6.45 | -9.10 | 16 |
| `above_50ma__above_50ma` | 27.44 | +1.37 | +1.27 | -11.44 | 18 |
| `breadth_above_500_trend_reversal__above_200dma` | 699.00 | +35.00 | +28.00 | -274.00 | 25 |
| `breadth_above_500_trend_reversal__above_20dma` | 614.00 | +155.00 | +328.00 | +0.00 | 25 |
| `breadth_above_500_trend_reversal__above_50dma` | 502.00 | +84.00 | +162.00 | -230.00 | 15 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,550.00 | -34.00 | -28.00 | +276.00 | 88 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,634.00 | -155.00 | -329.00 | +1.00 | 88 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,747.00 | -83.00 | -162.00 | +232.00 | 94 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 2.00 | -4.00 | -17.00 | -2.00 | 60 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 45.00 | -8.00 | -85.00 | +0.00 | 67 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 15.00 | +2.00 | +6.00 | -1.00 | 53 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 144.00 | +38.00 | +112.00 | +53.00 | 86 |
| `current_previous_yr_volumes_crores__1_yr_back` | 120.18 | -319.12 | -348.58 | -315.13 | 1 |
| `current_previous_yr_volumes_crores__current` | 439.65 | +17.66 | -154.38 | -163.36 | 21 |
| `drawdowns_peaks__blw_3` | 125.00 | -45.00 | -337.00 | -105.00 | 49 |
| `gold_etfs_nifty_1_month_chg__gold` | -5.74 | +0.55 | +0.69 | -1.29 | 31 |
| `gold_etfs_nifty_1_month_chg__nifty` | -1.19 | +2.37 | +3.00 | +4.86 | 39 |
| `mbm_2_0_magnitude__abv_10ma` | 37.26 | +7.47 | +25.81 | +9.79 | 41 |
| `mbm_2_0_magnitude__abv_200ma` | 29.77 | +1.20 | +0.80 | -11.75 | 31 |
| `mbm_2_0_magnitude__abv_20ma` | 24.46 | +4.40 | +12.38 | -4.44 | 20 |
| `mbm_2_0_magnitude__abv_50ma` | 21.47 | +3.10 | +6.44 | -12.31 | 16 |
| `mbm_2_0_velocity_advanced__15_52wh` | 12.08 | +1.42 | +2.11 | -10.55 | 22 |
| `mbm_2_0_velocity_advanced__15_52wl` | 35.62 | -1.04 | -1.22 | +8.19 | 76 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 54.99 | -1.14 | +0.59 | +9.60 | 67 |
| `mbm_2_0_velocity_advanced__30_52wh` | 43.92 | +0.64 | -0.34 | -7.33 | 40 |
| `mbm_2_0_velocity_advanced__breakdowns` | 9.60 | -3.08 | -15.79 | -5.50 | 60 |
| `mbm_2_0_velocity_advanced__breakouts` | 22.02 | +2.21 | +9.05 | +7.21 | 81 |
| `mbm_2_0_velocity_advanced__down_close` | 30.26 | +2.02 | -9.70 | +1.02 | 30 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -23.54 | +2.46 | +3.33 | -18.74 | 22 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -11.07 | +1.78 | -0.93 | -16.92 | 33 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -1.35 | +1.39 | +10.53 | +3.41 | 29 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.26 | +0.50 | +1.01 | -0.25 | 38 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 2.61 | -0.89 | -9.52 | -3.66 | 72 |
| `mbm_2_0_velocity_advanced__up_close` | 43.98 | +6.53 | +24.82 | +5.34 | 82 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.14 | -0.72 | -2.53 | +0.51 | 87 |
| `mbm_2_0_velocity_basic__10_in_5d` | 3.16 | -1.73 | -14.74 | -0.12 | 70 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.89 | +0.80 | +0.97 | -0.12 | 50 |
| `mbm_2_0_velocity_basic__3_range` | 34.40 | +2.42 | +7.83 | +4.11 | 33 |
| `mbm_2_0_velocity_basic__4_advance` | 9.68 | +2.27 | +7.20 | +3.96 | 85 |
| `mbm_2_0_velocity_basic__4_decline` | 2.91 | -0.68 | -7.24 | -1.51 | 53 |
| `mbm_2_0_velocity_basic__5d_range` | 1.31 | -0.00 | +0.08 | -1.22 | 16 |
| `mbm_2_0_velocity_basic__net_breadth` | 6.78 | +2.94 | +14.44 | +5.47 | 81 |
| `mbm_2_0_velocity_basic__volume` | 0.36 | +0.05 | -0.04 | -0.40 | 27 |
| `net_breadth__net_breadth` | 6.78 | +2.94 | +14.44 | +5.47 | 89 |
| `net_nh_nl__net_nh_nl` | -1.35 | +1.39 | +10.53 | +3.41 | 19 |
| `new_high_low_bearishness_bullishness__high` | 35.00 | +12.00 | +27.00 | -5.00 | 36 |
| `new_high_low_bearishness_bullishness__low` | 66.00 | -27.00 | -241.00 | -99.00 | 74 |
| `volume__volume` | 0.36 | +0.05 | -0.04 | -0.40 | 31 |

## No reading for 2026-10-29

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-26, 57.75
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-26, 42.25
- `oversold_overbought_rsi__overbought`: last 2026-10-26, 66.00
- `oversold_overbought_rsi__oversold`: last 2026-10-26, 214.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-26, 0.25
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-26, 0.74


<!-- market-read -->

## Market read

Thursday was the fourth up day in a row, and wider than Wednesday. 144 stocks rose four and a half percent or more, against 45 that fell that hard. The Nifty rose about one percent, and 32 of 35 indices closed higher. Banks, staples and realty led, so the heavy weights joined the small names for the first time this week. The short trend count has more than tripled since Friday, to 614 stocks above the 20 day line. The long count rose to 699, about three stocks in ten. New yearly lows fell to 66, the fewest since 16 October, and new highs rose to 35. Fear dropped about seven percent, and the VIX closed just above 15. The one thing missing is money. Turnover came to about 440 crore, well under Friday's selling day at about 611. The bounce is now wide and four days old. It is not yet heavy, and the staircase down from August still stands.

Full brief: briefs/2026-10-29.html
