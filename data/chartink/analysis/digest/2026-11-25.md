# Market breadth digest: 2026-11-25

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-25: **69** of 79
- History available: 2019-07-01 to 2026-11-25, 725 dated rows
- Metrics with no reading for 2026-11-25: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 27.34 | -0.76 | -18.84 | +2.85 | 22 | 429 |
| % above 20 EMA | 31.52 | -1.29 | -17.35 | +13.32 | 31 | 429 |
| % above 50 EMA | 29.76 | -1.53 | -11.03 | +11.68 | 28 | 429 |
| % above 200 EMA | 33.87 | +0.12 | -4.19 | +5.33 | 37 | 429 |
| Net breadth (4% adv minus dec) | -1.37 | +1.28 | -2.54 | -15.17 | 23 | 429 |
| 4% advancers | 3.99 | +0.87 | -1.12 | -13.35 | 29 | 429 |
| 4% decliners | 5.36 | -0.42 | +1.42 | +1.82 | 78 | 429 |
| Net new highs minus lows | -1.29 | -0.74 | -2.70 | +1.30 | 28 | 429 |
| Net within 15% of 52wk H/L | -13.96 | -1.09 | -7.40 | +10.29 | 32 | 429 |
| Volume expansion ratio | 0.40 | +0.10 | -0.01 | +0.03 | 39 | 429 |
| Overbought count (weekly RSI>70) (as of 2026-11-23) | 99.00 | -24.00 | +42.00 | -120.00 | 36 | 387 |
| Oversold count (weekly RSI<30) (as of 2026-11-23) | 144.00 | +32.00 | -200.00 | +116.00 | 86 | 387 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__1_yr_back` | 433.97 | -57.70 | 54 |
| `drawdowns_peaks__blw_3` | 332.00 | -40.00 | 85 |
| `new_high_low_bearishness_bullishness__low` | 100.00 | +40.00 | 82 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,467.00 | +35.00 | 79 |
| `new_high_low_bearishness_bullishness__high` | 44.00 | -35.00 | 49 |
| `breadth_above_500_trend_reversal__above_50dma` | 868.00 | -34.00 | 44 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,447.00 | +32.00 | 75 |
| `current_previous_yr_volumes_crores__current` | 520.27 | +31.79 | 56 |
| `breadth_above_500_trend_reversal__above_20dma` | 887.00 | -31.00 | 43 |
| `4_advance_decline_today__4_advance` | 103.00 | +23.00 | 30 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 15.73 (percentile 99, range -6.93 to 17.31)
- `15_up_10_down__10_in_5d` at 5.12 (percentile 91, range 0.34 to 27.94)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__gold` at -17.46 (percentile 1, range -17.46 to 14.14)
- `15_up_10_down__15_in_5d` at 0.70 (percentile 4, range 0.63 to 7.11)
- `mbm_2_0_velocity_basic__15_in_5d` at 0.70 (percentile 6, range 0.23 to 42.59)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed up through 50: 47.00 to 69.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.98 | +0.20 | +0.39 | -1.30 | 87 |
| `15_up_10_down__10_in_5d` | 5.12 | +0.79 | +2.55 | -6.43 | 91 |
| `15_up_10_down__15_in_5d` | 0.70 | +0.04 | -1.79 | +0.07 | 4 |
| `3_above_200_ema__pct` | 39.74 | +0.38 | -3.71 | +13.71 | 40 |
| `4_advance_decline__4_advance` | 102.00 | +22.00 | -29.00 | -339.00 | 25 |
| `4_advance_decline__4_decline` | 137.00 | -11.00 | +36.00 | +47.00 | 81 |
| `4_advance_decline_today__4_advance` | 103.00 | +23.00 | -31.00 | -123.00 | 30 |
| `4_advance_decline_today__4_decline` | 141.00 | -9.00 | +34.00 | -10.00 | 68 |
| `4_advance_decline_today__net_breadth` | -1.47 | +1.24 | -2.52 | -4.62 | 34 |
| `52_week_high_low_within_10__high` | 18.66 | -0.25 | -1.57 | +9.49 | 42 |
| `52_week_high_low_within_10__low` | 24.24 | +0.19 | +5.25 | -10.72 | 65 |
| `52_wk_high_low__new_52_wk_high` | 1.44 | -1.13 | -0.91 | +0.81 | 24 |
| `52_wk_high_low__new_52_wk_low` | 3.26 | +1.31 | +2.58 | +0.21 | 88 |
| `52_wk_high_low_today__new_52_wk_high` | 1.43 | -1.11 | -0.90 | +1.07 | 40 |
| `52_wk_high_low_today__new_52_wk_low` | 3.28 | +1.34 | +2.42 | -6.72 | 72 |
| `5_advance_decline_ratio__advance` | 44.12 | +16.19 | -4.72 | -15.71 | 50 |
| `5_advance_decline_ratio__decline` | 54.87 | -16.19 | +4.72 | +15.74 | 52 |
| `above_10ma__pct` | 33.15 | -0.26 | -17.67 | +7.52 | 28 |
| `above_200ma__above_200ma` | 39.71 | +0.35 | -3.75 | +13.68 | 41 |
| `above_20_ema__pct` | 38.04 | -1.22 | -15.61 | +19.97 | 38 |
| `above_20ma__pct` | 38.04 | -1.22 | -15.61 | +19.97 | 37 |
| `above_50_ema__pct` | 36.57 | -1.55 | -10.33 | +19.62 | 34 |
| `above_50ma__above_50ma` | 39.71 | +0.35 | -3.75 | +13.68 | 41 |
| `breadth_above_500_trend_reversal__above_200dma` | 967.00 | +0.00 | -98.00 | +266.00 | 53 |
| `breadth_above_500_trend_reversal__above_20dma` | 887.00 | -31.00 | -362.00 | +443.00 | 43 |
| `breadth_above_500_trend_reversal__above_50dma` | 868.00 | -34.00 | -235.00 | +429.00 | 44 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,368.00 | +1.00 | +94.00 | -274.00 | 75 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,447.00 | +32.00 | +358.00 | -452.00 | 75 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,467.00 | +35.00 | +231.00 | -437.00 | 79 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 5.00 | +2.00 | +1.00 | -6.00 | 90 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 89.00 | +16.00 | +43.00 | +48.00 | 86 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 7.00 | +4.00 | -8.00 | -1.00 | 20 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 69.00 | +22.00 | -4.00 | -219.00 | 43 |
| `current_previous_yr_volumes_crores__1_yr_back` | 433.97 | -57.70 | -88.64 | +17.91 | 54 |
| `current_previous_yr_volumes_crores__current` | 520.27 | +31.79 | +64.25 | -23.14 | 56 |
| `drawdowns_peaks__blw_3` | 332.00 | -40.00 | +135.00 | +193.00 | 85 |
| `gold_etfs_nifty_1_month_chg__gold` | -17.46 | -1.51 | -8.00 | -9.07 | 1 |
| `gold_etfs_nifty_1_month_chg__nifty` | 15.73 | +2.81 | +2.54 | +19.49 | 99 |
| `mbm_2_0_magnitude__abv_10ma` | 27.34 | -0.76 | -18.84 | +2.85 | 22 |
| `mbm_2_0_magnitude__abv_200ma` | 33.87 | +0.12 | -4.19 | +5.33 | 37 |
| `mbm_2_0_magnitude__abv_20ma` | 31.52 | -1.29 | -17.35 | +13.32 | 31 |
| `mbm_2_0_magnitude__abv_50ma` | 29.76 | -1.53 | -11.03 | +11.68 | 28 |
| `mbm_2_0_velocity_advanced__15_52wh` | 14.86 | -0.71 | -2.55 | +4.48 | 33 |
| `mbm_2_0_velocity_advanced__15_52wl` | 28.82 | +0.38 | +4.86 | -5.81 | 67 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.85 | +0.62 | +3.10 | -3.00 | 57 |
| `mbm_2_0_velocity_advanced__30_52wh` | 44.35 | -0.33 | -2.14 | +3.94 | 44 |
| `mbm_2_0_velocity_advanced__breakdowns` | 14.51 | -1.53 | +3.15 | +5.98 | 77 |
| `mbm_2_0_velocity_advanced__breakouts` | 14.39 | +1.63 | -1.22 | -23.85 | 45 |
| `mbm_2_0_velocity_advanced__down_close` | 36.93 | +0.92 | +2.22 | -4.55 | 64 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -13.96 | -1.09 | -7.40 | +10.29 | 32 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -4.50 | -0.95 | -5.24 | +6.94 | 42 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -1.29 | -0.74 | -2.70 | +1.30 | 28 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.37 | -0.31 | -0.86 | +0.70 | 41 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 2.66 | +0.44 | +1.84 | -0.60 | 73 |
| `mbm_2_0_velocity_advanced__up_close` | 27.72 | +3.25 | -5.03 | -17.61 | 15 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.98 | +0.20 | +0.39 | -1.30 | 83 |
| `mbm_2_0_velocity_basic__10_in_5d` | 5.12 | +0.79 | +2.55 | -6.43 | 85 |
| `mbm_2_0_velocity_basic__15_in_5d` | 0.70 | +0.04 | -1.79 | +0.07 | 6 |
| `mbm_2_0_velocity_basic__3_range` | 29.61 | -1.76 | -9.39 | +7.71 | 24 |
| `mbm_2_0_velocity_basic__4_advance` | 3.99 | +0.87 | -1.12 | -13.35 | 29 |
| `mbm_2_0_velocity_basic__4_decline` | 5.36 | -0.42 | +1.42 | +1.82 | 78 |
| `mbm_2_0_velocity_basic__5d_range` | 5.24 | -0.22 | +1.03 | +4.42 | 52 |
| `mbm_2_0_velocity_basic__net_breadth` | -1.37 | +1.28 | -2.54 | -15.17 | 23 |
| `mbm_2_0_velocity_basic__volume` | 0.40 | +0.10 | -0.01 | +0.03 | 39 |
| `net_breadth__net_breadth` | -1.37 | +1.28 | -2.54 | -15.17 | 22 |
| `net_nh_nl__net_nh_nl` | -1.29 | -0.74 | -2.70 | +1.30 | 18 |
| `new_high_low_bearishness_bullishness__high` | 44.00 | -35.00 | -28.00 | +25.00 | 49 |
| `new_high_low_bearishness_bullishness__low` | 100.00 | +40.00 | +79.00 | +7.00 | 82 |
| `volume__volume` | 0.40 | +0.10 | -0.01 | +0.03 | 43 |

## No reading for 2026-11-25

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-23, 64.99
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-23, 35.01
- `oversold_overbought_rsi__overbought`: last 2026-11-23, 99.00
- `oversold_overbought_rsi__oversold`: last 2026-11-23, 144.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-23, 0.37
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-23, 0.60


<!-- market-read -->
