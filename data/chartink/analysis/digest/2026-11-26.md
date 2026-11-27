# Market breadth digest: 2026-11-26

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-26: **69** of 79
- History available: 2019-07-01 to 2026-11-26, 726 dated rows
- Metrics with no reading for 2026-11-26: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 31.26 | +3.94 | -4.30 | +1.33 | 30 | 430 |
| % above 20 EMA | 33.84 | +2.33 | -7.39 | +13.42 | 35 | 430 |
| % above 50 EMA | 31.61 | +1.86 | -4.57 | +12.57 | 35 | 430 |
| % above 200 EMA | 34.94 | +1.08 | -1.29 | +6.18 | 38 | 430 |
| Net breadth (4% adv minus dec) | 3.71 | +5.08 | +6.60 | -0.02 | 61 | 430 |
| 4% advancers | 6.45 | +2.46 | +3.17 | -1.26 | 61 | 430 |
| 4% decliners | 2.74 | -2.62 | -3.44 | -1.24 | 45 | 430 |
| Net new highs minus lows | -0.90 | +0.39 | -0.86 | +1.58 | 30 | 430 |
| Net within 15% of 52wk H/L | -13.13 | +0.87 | -4.22 | +10.87 | 33 | 430 |
| Volume expansion ratio | 0.32 | -0.08 | +0.07 | +0.02 | 18 | 430 |
| Overbought count (weekly RSI>70) (as of 2026-11-23) | 94.00 | -29.00 | +37.00 | -125.00 | 33 | 387 |
| Oversold count (weekly RSI<30) (as of 2026-11-23) | 144.00 | +32.00 | -200.00 | +116.00 | 86 | 387 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 148.00 | -184.00 | 55 |
| `current_previous_yr_volumes_crores__current` | 451.41 | -68.86 | 21 |
| `4_advance_decline__4_decline` | 70.00 | -67.00 | 38 |
| `4_advance_decline_today__4_decline` | 74.00 | -67.00 | 31 |
| `4_advance_decline_today__4_advance` | 167.00 | +64.00 | 65 |
| `4_advance_decline__4_advance` | 165.00 | +63.00 | 55 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 29.00 | -60.00 | 46 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,391.00 | -59.00 | 70 |
| `breadth_above_500_trend_reversal__above_20dma` | 945.00 | +58.00 | 50 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,420.00 | -50.00 | 76 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 14.22 (percentile 99, range -6.93 to 17.31)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__gold` at -16.34 (percentile 1, range -17.46 to 14.14)
- `15_up_10_down__15_in_5d` at 1.06 (percentile 10, range 0.63 to 7.11)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 89.00 to 29.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.55 | -0.43 | -0.08 | -1.18 | 49 |
| `15_up_10_down__10_in_5d` | 3.40 | -1.72 | -1.09 | -1.67 | 80 |
| `15_up_10_down__15_in_5d` | 1.06 | +0.35 | -0.39 | -0.09 | 10 |
| `3_above_200_ema__pct` | 40.91 | +1.17 | -0.52 | +14.65 | 44 |
| `4_advance_decline__4_advance` | 165.00 | +63.00 | +81.00 | -31.00 | 55 |
| `4_advance_decline__4_decline` | 70.00 | -67.00 | -88.00 | -31.00 | 38 |
| `4_advance_decline_today__4_advance` | 167.00 | +64.00 | +81.00 | -242.00 | 65 |
| `4_advance_decline_today__4_decline` | 74.00 | -67.00 | -90.00 | -5.00 | 31 |
| `4_advance_decline_today__net_breadth` | 3.60 | +5.08 | +6.63 | -10.21 | 63 |
| `52_week_high_low_within_10__high` | 19.10 | +0.44 | -0.53 | +9.76 | 49 |
| `52_week_high_low_within_10__low` | 23.70 | -0.55 | +1.81 | -10.26 | 63 |
| `52_wk_high_low__new_52_wk_high` | 1.47 | +0.03 | +0.13 | +0.68 | 25 |
| `52_wk_high_low__new_52_wk_low` | 1.86 | -1.40 | +0.62 | -1.20 | 71 |
| `52_wk_high_low_today__new_52_wk_high` | 1.46 | +0.03 | +0.12 | +0.81 | 41 |
| `52_wk_high_low_today__new_52_wk_low` | 1.91 | -1.37 | +0.50 | -1.35 | 41 |
| `5_advance_decline_ratio__advance` | 55.07 | +10.95 | +28.32 | -15.34 | 69 |
| `5_advance_decline_ratio__decline` | 43.88 | -10.98 | -28.35 | +15.33 | 33 |
| `above_10ma__pct` | 38.20 | +5.05 | -0.84 | +7.70 | 39 |
| `above_200ma__above_200ma` | 40.88 | +1.17 | -0.54 | +14.62 | 45 |
| `above_20_ema__pct` | 40.81 | +2.77 | -5.51 | +21.07 | 43 |
| `above_20ma__pct` | 40.78 | +2.76 | -5.53 | +21.04 | 44 |
| `above_50_ema__pct` | 38.85 | +2.28 | -3.45 | +21.15 | 38 |
| `above_50ma__above_50ma` | 40.88 | +1.17 | -0.54 | +14.62 | 45 |
| `breadth_above_500_trend_reversal__above_200dma` | 993.00 | +26.00 | -20.00 | +288.00 | 58 |
| `breadth_above_500_trend_reversal__above_20dma` | 945.00 | +58.00 | -131.00 | +455.00 | 50 |
| `breadth_above_500_trend_reversal__above_50dma` | 917.00 | +49.00 | -73.00 | +460.00 | 50 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,344.00 | -27.00 | +18.00 | -297.00 | 72 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,391.00 | -59.00 | +129.00 | -465.00 | 70 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,420.00 | -50.00 | +71.00 | -469.00 | 76 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 4.00 | -1.00 | -1.00 | +0.00 | 82 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 29.00 | -60.00 | -42.00 | -25.00 | 46 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 11.00 | +4.00 | +3.00 | -2.00 | 38 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 102.00 | +32.00 | +60.00 | -10.00 | 67 |
| `current_previous_yr_volumes_crores__1_yr_back` | 464.58 | +30.61 | -37.10 | +26.08 | 73 |
| `current_previous_yr_volumes_crores__current` | 451.41 | -68.86 | +7.90 | -2.29 | 21 |
| `drawdowns_peaks__blw_3` | 148.00 | -184.00 | -191.00 | -50.00 | 55 |
| `gold_etfs_nifty_1_month_chg__gold` | -16.34 | +1.13 | -5.10 | -10.05 | 1 |
| `gold_etfs_nifty_1_month_chg__nifty` | 14.22 | -1.51 | +2.57 | +17.78 | 99 |
| `mbm_2_0_magnitude__abv_10ma` | 31.26 | +3.94 | -4.30 | +1.33 | 30 |
| `mbm_2_0_magnitude__abv_200ma` | 34.94 | +1.08 | -1.29 | +6.18 | 38 |
| `mbm_2_0_magnitude__abv_20ma` | 33.84 | +2.33 | -7.39 | +13.42 | 35 |
| `mbm_2_0_magnitude__abv_50ma` | 31.61 | +1.86 | -4.57 | +12.57 | 35 |
| `mbm_2_0_velocity_advanced__15_52wh` | 15.55 | +0.70 | -1.09 | +5.52 | 40 |
| `mbm_2_0_velocity_advanced__15_52wl` | 28.68 | -0.17 | +3.13 | -5.35 | 66 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.22 | -0.64 | +1.09 | -3.98 | 53 |
| `mbm_2_0_velocity_advanced__30_52wh` | 44.55 | +0.22 | -1.06 | +3.91 | 45 |
| `mbm_2_0_velocity_advanced__breakdowns` | 9.07 | -5.44 | -6.14 | -4.62 | 53 |
| `mbm_2_0_velocity_advanced__breakouts` | 17.43 | +3.04 | +7.66 | -3.03 | 63 |
| `mbm_2_0_velocity_advanced__down_close` | 30.17 | -6.75 | -10.44 | +1.15 | 30 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -13.13 | +0.87 | -4.22 | +10.87 | 33 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -3.67 | +0.86 | -2.15 | +7.89 | 45 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.90 | +0.39 | -0.86 | +1.58 | 30 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.21 | -0.16 | -0.12 | +0.42 | 33 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 2.11 | -0.55 | +0.74 | -1.15 | 68 |
| `mbm_2_0_velocity_advanced__up_close` | 37.00 | +9.28 | +3.40 | -0.70 | 49 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.55 | -0.43 | -0.08 | -1.18 | 57 |
| `mbm_2_0_velocity_basic__10_in_5d` | 3.40 | -1.72 | -1.09 | -1.67 | 74 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.06 | +0.35 | -0.39 | -0.09 | 18 |
| `mbm_2_0_velocity_basic__3_range` | 40.68 | +11.05 | +0.51 | +9.05 | 53 |
| `mbm_2_0_velocity_basic__4_advance` | 6.45 | +2.46 | +3.17 | -1.26 | 61 |
| `mbm_2_0_velocity_basic__4_decline` | 2.74 | -2.62 | -3.44 | -1.24 | 45 |
| `mbm_2_0_velocity_basic__5d_range` | 5.47 | +0.27 | +0.63 | +4.17 | 54 |
| `mbm_2_0_velocity_basic__net_breadth` | 3.71 | +5.08 | +6.60 | -0.02 | 61 |
| `mbm_2_0_velocity_basic__volume` | 0.32 | -0.08 | +0.07 | +0.02 | 18 |
| `net_breadth__net_breadth` | 3.71 | +5.08 | +6.60 | -0.02 | 60 |
| `net_nh_nl__net_nh_nl` | -0.90 | +0.39 | -0.86 | +1.58 | 20 |
| `new_high_low_bearishness_bullishness__high` | 45.00 | +1.00 | +4.00 | +21.00 | 50 |
| `new_high_low_bearishness_bullishness__low` | 57.00 | -43.00 | +19.00 | -36.00 | 70 |
| `volume__volume` | 0.32 | -0.08 | +0.07 | +0.02 | 20 |

## No reading for 2026-11-26

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-23, 64.59
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-23, 35.41
- `oversold_overbought_rsi__overbought`: last 2026-11-23, 94.00
- `oversold_overbought_rsi__oversold`: last 2026-11-23, 144.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-23, 0.38
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-23, 0.59


<!-- market-read -->
