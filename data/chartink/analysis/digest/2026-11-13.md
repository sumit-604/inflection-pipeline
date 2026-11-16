# Market breadth digest: 2026-11-13

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-13: **69** of 79
- History available: 2019-07-01 to 2026-11-13, 718 dated rows
- Metrics with no reading for 2026-11-13: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 67.37 | -8.56 | +6.63 | +32.72 | 85 | 422 |
| % above 20 EMA | 64.29 | -5.71 | +14.19 | +34.57 | 83 | 422 |
| % above 50 EMA | 48.13 | -3.49 | +13.71 | +18.33 | 63 | 422 |
| % above 200 EMA | 40.97 | -0.25 | +5.80 | +2.66 | 57 | 422 |
| Net breadth (4% adv minus dec) | 1.17 | -4.64 | +5.92 | +6.40 | 36 | 422 |
| 4% advancers | 5.45 | -2.26 | +0.77 | +1.75 | 49 | 422 |
| 4% decliners | 4.28 | +2.37 | -5.15 | -4.65 | 71 | 422 |
| Net new highs minus lows | 1.75 | +0.08 | +1.44 | +1.67 | 80 | 422 |
| Net within 15% of 52wk H/L | -2.10 | -1.91 | +8.54 | +8.80 | 55 | 422 |
| Volume expansion ratio | 0.47 | -0.13 | -0.04 | +0.13 | 52 | 422 |
| Overbought count (weekly RSI>70) (as of 2026-11-09) | 95.00 | +9.00 | -40.00 | -91.00 | 34 | 385 |
| Oversold count (weekly RSI<30) (as of 2026-11-09) | 62.00 | -10.00 | -141.00 | +31.00 | 71 | 385 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 235.00 | +132.00 | 77 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,597.00 | -118.00 | 91 |
| `breadth_above_500_trend_reversal__below_20dma` | 754.00 | +118.00 | 22 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,262.00 | -73.00 | 70 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,089.00 | +73.00 | 44 |
| `4_advance_decline__4_decline` | 110.00 | +61.00 | 73 |
| `4_advance_decline_today__4_decline` | 114.00 | +61.00 | 67 |
| `4_advance_decline__4_advance` | 139.00 | -59.00 | 40 |
| `4_advance_decline_today__4_advance` | 143.00 | -56.00 | 44 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 75.00 | -48.00 | 46 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 11.44 (percentile 99, range -6.93 to 12.37)
- `breadth_above_500_trend_reversal__above_20dma` at 1,597.00 (percentile 91, range 119.00 to 2,058.00)

Bottom decile of history:

- `10_from_10dema__10_10ema` at 0.19 (percentile 6, range 0.00 to 7.14)
- `15_up_10_down__10_in_5d` at 0.66 (percentile 6, range 0.34 to 27.90)
- `52_wk_high_low_today__new_52_wk_low` at 0.61 (percentile 7, range 0.38 to 14.97)
- `mbm_2_0_velocity_basic__10_in_5d` at 0.66 (percentile 9, range 0.20 to 37.65)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 21.00 to 59.00
- `mbm_2_0_magnitude__abv_50ma` crossed down through 50: 51.62 to 48.13

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.19 | -0.04 | -0.51 | -0.47 | 6 |
| `15_up_10_down__10_in_5d` | 0.66 | -0.47 | -1.05 | -1.31 | 6 |
| `15_up_10_down__15_in_5d` | 2.65 | +0.66 | -2.15 | +0.29 | 59 |
| `3_above_200_ema__pct` | 46.25 | -0.37 | +5.73 | +10.14 | 60 |
| `4_advance_decline__4_advance` | 139.00 | -59.00 | +19.00 | +45.00 | 40 |
| `4_advance_decline__4_decline` | 110.00 | +61.00 | -132.00 | -116.00 | 73 |
| `4_advance_decline_today__4_advance` | 143.00 | -56.00 | -239.00 | -69.00 | 44 |
| `4_advance_decline_today__4_decline` | 114.00 | +61.00 | +17.00 | +77.00 | 67 |
| `4_advance_decline_today__net_breadth` | 1.12 | -4.53 | -9.95 | -6.19 | 35 |
| `52_week_high_low_within_10__high` | 21.33 | -0.27 | +3.90 | +5.46 | 74 |
| `52_week_high_low_within_10__low` | 14.94 | +1.07 | -5.56 | -12.09 | 33 |
| `52_wk_high_low__new_52_wk_high` | 2.22 | +0.20 | +0.72 | +0.93 | 51 |
| `52_wk_high_low__new_52_wk_low` | 0.46 | +0.23 | -0.62 | -0.76 | 15 |
| `52_wk_high_low_today__new_52_wk_high` | 2.20 | +0.19 | +0.00 | +0.86 | 81 |
| `52_wk_high_low_today__new_52_wk_low` | 0.61 | +0.22 | -0.13 | -0.50 | 7 |
| `5_advance_decline_ratio__advance` | 35.77 | -21.18 | -35.04 | -20.74 | 26 |
| `5_advance_decline_ratio__decline` | 63.18 | +21.15 | +35.01 | +20.73 | 77 |
| `above_10ma__pct` | 69.44 | -7.81 | +4.78 | +33.31 | 83 |
| `above_200ma__above_200ma` | 46.25 | -0.37 | +5.73 | +10.14 | 64 |
| `above_20_ema__pct` | 67.38 | -5.05 | +12.11 | +37.48 | 83 |
| `above_20ma__pct` | 67.38 | -5.07 | +12.13 | +37.49 | 84 |
| `above_50_ema__pct` | 53.34 | -3.13 | +12.45 | +26.12 | 63 |
| `above_50ma__above_50ma` | 46.27 | -0.36 | +5.77 | +10.18 | 64 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,132.00 | -13.00 | +147.00 | +172.00 | 75 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,597.00 | -118.00 | +316.00 | +859.00 | 91 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,262.00 | -73.00 | +313.00 | +559.00 | 70 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,219.00 | +13.00 | -146.00 | -176.00 | 56 |
| `breadth_above_500_trend_reversal__below_20dma` | 754.00 | +118.00 | -315.00 | -863.00 | 22 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,089.00 | +73.00 | -312.00 | -563.00 | 44 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 2.00 | -2.00 | +0.00 | +2.00 | 60 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 59.00 | +38.00 | -92.00 | -69.00 | 76 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 15.00 | +1.00 | -21.00 | -15.00 | 51 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 75.00 | -48.00 | -3.00 | +12.00 | 46 |
| `current_previous_yr_volumes_crores__1_yr_back` | 448.72 | +17.70 | -180.22 | +18.13 | 65 |
| `current_previous_yr_volumes_crores__current` | 446.26 | -46.16 | -109.59 | -69.19 | 18 |
| `drawdowns_peaks__blw_3` | 235.00 | +132.00 | -181.00 | -209.00 | 77 |
| `gold_etfs_nifty_1_month_chg__gold` | -7.90 | -1.22 | -1.03 | -3.49 | 20 |
| `gold_etfs_nifty_1_month_chg__nifty` | 11.44 | -0.94 | +5.82 | +15.03 | 99 |
| `mbm_2_0_magnitude__abv_10ma` | 67.37 | -8.56 | +6.63 | +32.72 | 85 |
| `mbm_2_0_magnitude__abv_200ma` | 40.97 | -0.25 | +5.80 | +2.66 | 57 |
| `mbm_2_0_magnitude__abv_20ma` | 64.29 | -5.71 | +14.19 | +34.57 | 83 |
| `mbm_2_0_magnitude__abv_50ma` | 48.13 | -3.49 | +13.71 | +18.33 | 63 |
| `mbm_2_0_velocity_advanced__15_52wh` | 18.03 | -0.51 | +3.72 | +0.94 | 61 |
| `mbm_2_0_velocity_advanced__15_52wl` | 20.13 | +1.39 | -4.82 | -7.86 | 45 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 44.82 | +0.68 | -2.98 | +0.02 | 43 |
| `mbm_2_0_velocity_advanced__30_52wh` | 48.68 | -0.80 | +4.54 | +1.00 | 77 |
| `mbm_2_0_velocity_advanced__breakdowns` | 13.12 | +6.19 | -13.27 | -5.07 | 73 |
| `mbm_2_0_velocity_advanced__breakouts` | 14.72 | -5.03 | +3.26 | +1.57 | 47 |
| `mbm_2_0_velocity_advanced__down_close` | 32.64 | +5.11 | -3.10 | -16.49 | 42 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -2.10 | -1.91 | +8.54 | +8.80 | 55 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 3.86 | -1.48 | +7.52 | +0.98 | 65 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 1.75 | +0.08 | +1.44 | +1.67 | 80 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 2.26 | +0.35 | +0.82 | +0.80 | 76 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 0.51 | +0.27 | -0.62 | -0.87 | 28 |
| `mbm_2_0_velocity_advanced__up_close` | 37.04 | -2.02 | -3.78 | +8.89 | 49 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.19 | -0.04 | -0.51 | -0.47 | 13 |
| `mbm_2_0_velocity_basic__10_in_5d` | 0.66 | -0.47 | -1.05 | -1.31 | 9 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.69 | +0.70 | -2.11 | +0.32 | 68 |
| `mbm_2_0_velocity_basic__3_range` | 40.50 | +0.06 | +11.88 | +3.10 | 52 |
| `mbm_2_0_velocity_basic__4_advance` | 5.45 | -2.26 | +0.77 | +1.75 | 49 |
| `mbm_2_0_velocity_basic__4_decline` | 4.28 | +2.37 | -5.15 | -4.65 | 71 |
| `mbm_2_0_velocity_basic__5d_range` | 5.53 | +1.79 | +4.91 | -0.06 | 54 |
| `mbm_2_0_velocity_basic__net_breadth` | 1.17 | -4.64 | +5.92 | +6.40 | 36 |
| `mbm_2_0_velocity_basic__volume` | 0.47 | -0.13 | -0.04 | +0.13 | 52 |
| `net_breadth__net_breadth` | 1.17 | -4.64 | +5.92 | +6.40 | 31 |
| `net_nh_nl__net_nh_nl` | 1.75 | +0.08 | +1.44 | +1.67 | 64 |
| `new_high_low_bearishness_bullishness__high` | 68.00 | +6.00 | +22.00 | +29.00 | 77 |
| `new_high_low_bearishness_bullishness__low` | 14.00 | +7.00 | -19.00 | -23.00 | 32 |
| `volume__volume` | 0.47 | -0.14 | -0.04 | +0.13 | 63 |

## No reading for 2026-11-13

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-09, 66.00
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-09, 34.00
- `oversold_overbought_rsi__overbought`: last 2026-11-09, 95.00
- `oversold_overbought_rsi__oversold`: last 2026-11-09, 62.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-09, 0.44
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-09, 0.48


<!-- market-read -->
## Market read

Friday was the first down day of the week, and it was a mild one. The Nifty fell about half a percent and closed near 25,150. Only two of 35 indices rose. A little over a third of all stocks rose on the day, and the rest fell. Still, 75 stocks rose four and a half percent or more, against 59 that fell that hard, so the buyers kept a small edge at the extremes. Turnover eased again to about 450 crore. The short trend gave back the most: 118 stocks slipped under their 20 day line. The count above the 50 day line fell to 1,262, back to Wednesday's level and still above half the market. The count above the 200 day line fell by only 13, to 1,132. Realty, the best index on Thursday, was the worst on Friday. Autos, metals and banks also fell. New yearly highs rose to 68, the most since 23 September. The fear gauge fell again, to 15.5, on a day when prices fell. The repair paused on light volume, and the long clock held almost all of its ground.

Full brief: briefs/2026-11-13.html
