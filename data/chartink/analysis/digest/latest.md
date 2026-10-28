# Market breadth digest: 2026-10-27

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-27: **69** of 79
- History available: 2019-07-01 to 2026-10-27, 705 dated rows
- Metrics with no reading for 2026-10-27: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 24.09 | +11.75 | -1.61 | -16.59 | 18 | 409 |
| % above 20 EMA | 17.73 | +7.03 | -5.70 | -21.01 | 9 | 409 |
| % above 50 EMA | 17.52 | +5.01 | -7.84 | -23.54 | 11 | 409 |
| % above 200 EMA | 28.26 | +2.66 | -7.52 | -16.76 | 28 | 409 |
| Net breadth (4% adv minus dec) | 13.98 | +10.84 | +22.26 | +9.85 | 94 | 409 |
| 4% advancers | 17.14 | +7.70 | +14.25 | +10.95 | 95 | 409 |
| 4% decliners | 3.16 | -3.14 | -8.01 | +1.09 | 58 | 409 |
| Net new highs minus lows | -2.86 | +8.60 | -0.30 | -2.19 | 19 | 409 |
| Net within 15% of 52wk H/L | -26.20 | +5.37 | -10.49 | -28.43 | 18 | 409 |
| Volume expansion ratio | 0.39 | -0.03 | +0.10 | +0.06 | 34 | 409 |
| Overbought count (weekly RSI>70) (as of 2026-10-26) | 63.00 | +7.00 | -138.00 | -101.00 | 22 | 383 |
| Oversold count (weekly RSI<30) (as of 2026-10-26) | 239.00 | -111.00 | +157.00 | +202.00 | 92 | 383 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `new_high_low_bearishness_bullishness__low` | 93.00 | -211.00 | 80 |
| `4_advance_decline_today__4_advance` | 409.00 | +183.00 | 100 |
| `4_advance_decline__4_advance` | 407.00 | +182.00 | 99 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,831.00 | -161.00 | 97 |
| `breadth_above_500_trend_reversal__above_20dma` | 413.00 | +159.00 | 9 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 270.00 | +126.00 | 96 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,840.00 | -120.00 | 98 |
| `breadth_above_500_trend_reversal__above_50dma` | 404.00 | +118.00 | 10 |
| `drawdowns_peaks__blw_3` | 119.00 | -108.00 | 45 |
| `4_advance_decline__4_decline` | 75.00 | -75.00 | 54 |

## At the edge of their own range

Top decile of history:

- `5_advance_decline_ratio__advance` at 70.41 (percentile 100, range 13.35 to 70.41)
- `4_advance_decline_today__4_advance` at 409.00 (percentile 100, range 33.00 to 409.00)
- `4_advance_decline_today__net_breadth` at 13.82 (percentile 100, range -24.25 to 13.82)
- `4_advance_decline__4_advance` at 407.00 (percentile 99, range 30.00 to 479.00)
- `net_breadth__net_breadth` at 13.98 (percentile 99, range -24.34 to 19.72)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 14.00 (percentile 98, range 0.00 to 33.00)
- `breadth_above_500_trend_reversal__below_50dma` at 1,840.00 (percentile 98, range 272.00 to 1,992.00)
- `breadth_above_500_trend_reversal__below_20dma` at 1,831.00 (percentile 97, range 76.00 to 2,066.00)
- `10_from_10dema__10_10ema` at 2.36 (percentile 97, range 0.09 to 7.07)
- `15_up_10_down__10_in_5d` at 11.29 (percentile 97, range 0.34 to 28.13)
- `breadth_above_500_trend_reversal__up_4_5_today` at 270.00 (percentile 96, range 6.00 to 1,121.00)
- `mbm_2_0_velocity_basic__10_in_5d` at 11.29 (percentile 96, range 0.18 to 37.65)
- `mbm_2_0_velocity_basic__4_advance` at 17.14 (percentile 95, range 0.91 to 64.61)
- `mbm_2_0_velocity_basic__10_10ema` at 2.36 (percentile 95, range 0.00 to 16.96)
- `mbm_2_0_velocity_advanced__breakouts` at 37.95 (percentile 95, range 3.51 to 86.12)
- `mbm_2_0_velocity_basic__net_breadth` at 13.98 (percentile 94, range -57.32 to 63.88)

Bottom decile of history:

- `15_up_10_down__15_in_5d` at 0.59 (percentile 1, range 0.59 to 7.11)
- `5_advance_decline_ratio__decline` at 28.55 (percentile 3, range 28.55 to 85.61)
- `mbm_2_0_velocity_basic__15_in_5d` at 0.59 (percentile 3, range 0.23 to 42.62)
- `52_wk_high_low__new_52_wk_high` at 0.63 (percentile 4, range 0.28 to 5.21)
- `above_20_ema__pct` at 17.71 (percentile 7, range 6.35 to 96.00)
- `mbm_2_0_magnitude__abv_20ma` at 17.73 (percentile 9, range 5.26 to 95.55)
- `mbm_2_0_velocity_basic__5d_range` at 0.80 (percentile 9, range 0.32 to 19.43)
- `above_20ma__pct` at 17.71 (percentile 9, range 7.00 to 96.00)
- `breadth_above_500_trend_reversal__above_20dma` at 413.00 (percentile 9, range 119.00 to 2,038.00)
- `breadth_above_500_trend_reversal__above_50dma` at 404.00 (percentile 10, range 121.00 to 1,878.00)
- `above_50_ema__pct` at 16.45 (percentile 10, range 7.90 to 85.55)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 74.00 to 41.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 2.36 | -2.43 | +1.01 | +1.90 | 97 |
| `15_up_10_down__10_in_5d` | 11.29 | -16.84 | +8.06 | +9.98 | 97 |
| `15_up_10_down__15_in_5d` | 0.59 | -0.04 | -1.47 | -2.78 | 1 |
| `3_above_200_ema__pct` | 25.73 | +2.66 | -7.75 | -19.09 | 15 |
| `4_advance_decline__4_advance` | 407.00 | +182.00 | +338.00 | +260.00 | 99 |
| `4_advance_decline__4_decline` | 75.00 | -75.00 | -191.00 | +26.00 | 54 |
| `4_advance_decline_today__4_advance` | 409.00 | +183.00 | +338.00 | +319.00 | 100 |
| `4_advance_decline_today__4_decline` | 79.00 | -72.00 | -188.00 | -82.00 | 42 |
| `4_advance_decline_today__net_breadth` | 13.82 | +10.68 | +22.03 | +16.79 | 100 |
| `52_week_high_low_within_10__high` | 9.70 | +2.52 | -5.00 | -15.39 | 12 |
| `52_week_high_low_within_10__low` | 37.31 | -2.17 | +6.90 | +14.85 | 87 |
| `52_wk_high_low__new_52_wk_high` | 0.63 | +0.32 | -0.87 | -1.33 | 4 |
| `52_wk_high_low__new_52_wk_low` | 3.26 | -7.34 | -0.40 | +0.49 | 85 |
| `52_wk_high_low_today__new_52_wk_high` | 0.65 | +0.29 | -0.81 | -1.07 | 13 |
| `52_wk_high_low_today__new_52_wk_low` | 3.26 | -6.74 | -0.23 | +1.11 | 58 |
| `5_advance_decline_ratio__advance` | 70.41 | +10.58 | +49.48 | +48.33 | 100 |
| `5_advance_decline_ratio__decline` | 28.55 | -10.58 | -49.48 | -48.33 | 3 |
| `above_10ma__pct` | 25.48 | +11.82 | -1.97 | -10.82 | 18 |
| `above_200ma__above_200ma` | 25.73 | +2.66 | -7.75 | -19.09 | 16 |
| `above_20_ema__pct` | 17.71 | +6.63 | -6.36 | -16.49 | 7 |
| `above_20ma__pct` | 17.71 | +6.63 | -6.36 | -16.49 | 9 |
| `above_50_ema__pct` | 16.45 | +4.50 | -6.82 | -20.13 | 10 |
| `above_50ma__above_50ma` | 25.73 | +2.66 | -7.75 | -19.09 | 16 |
| `breadth_above_500_trend_reversal__above_200dma` | 658.00 | +61.00 | -193.00 | -436.00 | 21 |
| `breadth_above_500_trend_reversal__above_20dma` | 413.00 | +159.00 | -153.00 | -401.00 | 9 |
| `breadth_above_500_trend_reversal__above_50dma` | 404.00 | +118.00 | -161.00 | -484.00 | 10 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,586.00 | -63.00 | +192.00 | +437.00 | 90 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,831.00 | -161.00 | +152.00 | +402.00 | 97 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,840.00 | -120.00 | +160.00 | +485.00 | 98 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 14.00 | -13.00 | +10.00 | +8.00 | 98 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 41.00 | -33.00 | -111.00 | +17.00 | 65 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 7.00 | -1.00 | -9.00 | -18.00 | 19 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 270.00 | +126.00 | +226.00 | +163.00 | 96 |
| `current_previous_yr_volumes_crores__1_yr_back` | 415.94 | -18.39 | -64.72 | -27.51 | 51 |
| `current_previous_yr_volumes_crores__current` | 523.85 | +4.67 | +9.73 | +121.49 | 60 |
| `drawdowns_peaks__blw_3` | 119.00 | -108.00 | -430.00 | -2.00 | 45 |
| `gold_etfs_nifty_1_month_chg__gold` | -8.39 | -0.72 | -3.39 | -7.52 | 18 |
| `gold_etfs_nifty_1_month_chg__nifty` | -3.76 | -0.60 | -0.05 | +0.59 | 24 |
| `mbm_2_0_magnitude__abv_10ma` | 24.09 | +11.75 | -1.61 | -16.59 | 18 |
| `mbm_2_0_magnitude__abv_200ma` | 28.26 | +2.66 | -7.52 | -16.76 | 28 |
| `mbm_2_0_magnitude__abv_20ma` | 17.73 | +7.03 | -5.70 | -21.01 | 9 |
| `mbm_2_0_magnitude__abv_50ma` | 17.52 | +5.01 | -7.84 | -23.54 | 11 |
| `mbm_2_0_velocity_advanced__15_52wh` | 11.04 | +2.30 | -4.63 | -14.98 | 19 |
| `mbm_2_0_velocity_advanced__15_52wl` | 37.24 | -3.07 | +5.86 | +13.46 | 80 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 55.69 | -1.91 | +6.21 | +12.43 | 69 |
| `mbm_2_0_velocity_advanced__30_52wh` | 43.05 | +2.54 | -6.55 | -10.79 | 36 |
| `mbm_2_0_velocity_advanced__breakdowns` | 7.46 | -11.44 | -17.41 | -1.19 | 43 |
| `mbm_2_0_velocity_advanced__breakouts` | 37.95 | +12.97 | +27.24 | +22.61 | 95 |
| `mbm_2_0_velocity_advanced__down_close` | 42.37 | +9.04 | -2.56 | +18.47 | 86 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -26.20 | +5.37 | -10.49 | -28.43 | 18 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -12.64 | +4.45 | -12.76 | -23.22 | 31 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -2.86 | +8.60 | -0.30 | -2.19 | 19 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 0.63 | +0.38 | -1.01 | -1.56 | 15 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 3.50 | -8.22 | -0.70 | +0.63 | 78 |
| `mbm_2_0_velocity_advanced__up_close` | 45.17 | +7.36 | +18.11 | +4.79 | 87 |
| `mbm_2_0_velocity_basic__10_10ema` | 2.36 | -2.43 | +1.01 | +1.90 | 95 |
| `mbm_2_0_velocity_basic__10_in_5d` | 11.29 | -16.84 | +8.06 | +9.98 | 96 |
| `mbm_2_0_velocity_basic__15_in_5d` | 0.59 | -0.04 | -1.47 | -2.78 | 3 |
| `mbm_2_0_velocity_basic__3_range` | 22.03 | +5.32 | -8.42 | -22.40 | 13 |
| `mbm_2_0_velocity_basic__4_advance` | 17.14 | +7.70 | +14.25 | +10.95 | 95 |
| `mbm_2_0_velocity_basic__4_decline` | 3.16 | -3.14 | -8.01 | +1.09 | 58 |
| `mbm_2_0_velocity_basic__5d_range` | 0.80 | +0.21 | -4.79 | -8.43 | 9 |
| `mbm_2_0_velocity_basic__net_breadth` | 13.98 | +10.84 | +22.26 | +9.85 | 94 |
| `mbm_2_0_velocity_basic__volume` | 0.39 | -0.03 | +0.10 | +0.06 | 34 |
| `net_breadth__net_breadth` | 13.98 | +10.84 | +22.26 | +9.85 | 99 |
| `net_nh_nl__net_nh_nl` | -2.86 | +8.60 | -0.30 | -2.19 | 11 |
| `new_high_low_bearishness_bullishness__high` | 18.00 | +9.00 | -25.00 | -38.00 | 13 |
| `new_high_low_bearishness_bullishness__low` | 93.00 | -211.00 | -12.00 | +14.00 | 80 |
| `volume__volume` | 0.39 | -0.03 | +0.10 | +0.06 | 36 |

## No reading for 2026-10-27

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-26, 55.94
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-26, 44.06
- `oversold_overbought_rsi__overbought`: last 2026-10-26, 63.00
- `oversold_overbought_rsi__oversold`: last 2026-10-26, 239.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-26, 0.23
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-26, 0.75


<!-- market-read -->

## Market read

Tuesday was the widest buying day since 12 June, and the Nifty closed flat. 270 stocks rose four and a half percent or more, against 41 that fell that hard. About seven stocks in ten closed up. The small company indices rose almost three percent while the banks and IT slipped. The buying was wide and it was not heavy. Turnover stayed near Monday's level, below Friday's selling day, and the heavy volume share stayed low. The new lows shrank from 304 to 93. The long trend count rose to 658 stocks above the 200 day line, about three in ten. That is still far below the 1,357 of early August. Two up days in a row now sit on top of a falling staircase. The spring showed that days of this size can fail. A real turn needs a third day, heavier volume, and a long count back above the autumn floor.

Full brief: briefs/2026-10-27.html
