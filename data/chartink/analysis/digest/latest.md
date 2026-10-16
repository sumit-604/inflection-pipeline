# Market breadth digest: 2026-10-15

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-15: **69** of 79
- History available: 2019-07-01 to 2026-10-15, 698 dated rows
- Metrics with no reading for 2026-10-15: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 34.08 | -12.43 | +17.18 | +15.15 | 34 | 402 |
| % above 20 EMA | 28.90 | -7.00 | +9.52 | +5.81 | 26 | 402 |
| % above 50 EMA | 29.06 | -4.48 | +3.13 | -2.73 | 27 | 402 |
| % above 200 EMA | 37.91 | -1.15 | +2.31 | -3.89 | 45 | 402 |
| Net breadth (4% adv minus dec) | -4.97 | -12.42 | +14.37 | -4.21 | 12 | 402 |
| 4% advancers | 3.50 | -5.34 | +1.69 | -1.30 | 22 | 402 |
| 4% decliners | 8.47 | +7.08 | -12.68 | +2.92 | 88 | 402 |
| Net new highs minus lows | -0.04 | -0.59 | +6.09 | +4.16 | 42 | 402 |
| Net within 15% of 52wk H/L | -11.88 | -2.75 | +3.67 | -6.29 | 34 | 402 |
| Volume expansion ratio | 0.36 | -0.04 | -0.19 | -0.11 | 27 | 402 |
| Overbought count (weekly RSI>70) (as of 2026-10-12) | 126.00 | -8.00 | -121.00 | -37.00 | 45 | 381 |
| Oversold count (weekly RSI<30) (as of 2026-10-12) | 144.00 | -63.00 | +55.00 | +110.00 | 86 | 381 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 407.00 | +322.00 | 89 |
| `4_advance_decline__4_decline` | 201.00 | +168.00 | 94 |
| `4_advance_decline_today__4_decline` | 204.00 | +167.00 | 83 |
| `4_advance_decline__4_advance` | 83.00 | -127.00 | 14 |
| `4_advance_decline_today__4_advance` | 86.00 | -126.00 | 21 |
| `breadth_above_500_trend_reversal__above_20dma` | 683.00 | -117.00 | 27 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,579.00 | +116.00 | 86 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 116.00 | +105.00 | 91 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 56.00 | -90.00 | 30 |
| `breadth_above_500_trend_reversal__above_50dma` | 649.00 | -85.00 | 23 |

## At the edge of their own range

Top decile of history:

- `mbm_2_0_velocity_advanced__down_close` at 48.67 (percentile 95, range 4.97 to 72.79)
- `4_advance_decline__4_decline` at 201.00 (percentile 94, range 22.00 to 561.00)
- `breadth_above_500_trend_reversal__down_4_5_today` at 116.00 (percentile 91, range 1.00 to 964.00)

Bottom decile of history:

- `net_breadth__net_breadth` at -4.97 (percentile 7, range -20.70 to 19.72)
- `52_wk_high_low__new_52_wk_high` at 1.33 (percentile 9, range 0.86 to 5.21)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 11.00 to 116.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.88 | +0.17 | -0.21 | -0.04 | 89 |
| `15_up_10_down__10_in_5d` | 1.77 | -0.59 | -2.90 | -4.79 | 52 |
| `15_up_10_down__15_in_5d` | 2.19 | +0.46 | +0.64 | +0.89 | 49 |
| `3_above_200_ema__pct` | 35.66 | -0.56 | +2.51 | -6.40 | 28 |
| `4_advance_decline__4_advance` | 83.00 | -127.00 | +40.00 | -31.00 | 14 |
| `4_advance_decline__4_decline` | 201.00 | +168.00 | -302.00 | +69.00 | 94 |
| `4_advance_decline_today__4_advance` | 86.00 | -126.00 | +41.00 | -55.00 | 21 |
| `4_advance_decline_today__4_decline` | 204.00 | +167.00 | -303.00 | +109.00 | 83 |
| `4_advance_decline_today__net_breadth` | -4.94 | -12.25 | +14.37 | -6.88 | 21 |
| `52_week_high_low_within_10__high` | 16.78 | -2.07 | +1.85 | -3.54 | 30 |
| `52_week_high_low_within_10__low` | 28.72 | +0.63 | -4.11 | +5.41 | 72 |
| `52_wk_high_low__new_52_wk_high` | 1.33 | -0.07 | +0.07 | +0.46 | 9 |
| `52_wk_high_low__new_52_wk_low` | 1.37 | +0.39 | -5.80 | -2.94 | 66 |
| `52_wk_high_low_today__new_52_wk_high` | 1.30 | -0.03 | +0.07 | -1.69 | 12 |
| `52_wk_high_low_today__new_52_wk_low` | 1.46 | +0.36 | -5.37 | -0.80 | 21 |
| `5_advance_decline_ratio__advance` | 36.33 | -20.18 | +22.98 | -0.24 | 25 |
| `5_advance_decline_ratio__decline` | 62.63 | +20.18 | -22.98 | +0.25 | 79 |
| `above_10ma__pct` | 35.90 | -9.74 | +20.38 | +18.02 | 34 |
| `above_200ma__above_200ma` | 35.66 | -0.56 | +2.51 | -6.40 | 28 |
| `above_20_ema__pct` | 29.35 | -3.96 | +11.90 | +8.14 | 24 |
| `above_20ma__pct` | 29.35 | -3.96 | +11.90 | +8.14 | 23 |
| `above_50_ema__pct` | 26.48 | -3.22 | +3.65 | -2.91 | 19 |
| `above_50ma__above_50ma` | 35.66 | -0.56 | +2.51 | -6.40 | 28 |
| `breadth_above_500_trend_reversal__above_200dma` | 909.00 | -11.00 | +72.00 | -129.00 | 44 |
| `breadth_above_500_trend_reversal__above_20dma` | 683.00 | -117.00 | +269.00 | +204.00 | 27 |
| `breadth_above_500_trend_reversal__above_50dma` | 649.00 | -85.00 | +87.00 | -56.00 | 23 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,353.00 | +10.00 | -72.00 | +128.00 | 75 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,579.00 | +116.00 | -269.00 | -205.00 | 86 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,613.00 | +84.00 | -87.00 | +55.00 | 88 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 2.00 | -4.00 | -10.00 | -1.00 | 59 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 116.00 | +105.00 | -199.00 | +51.00 | 91 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 25.00 | +9.00 | +7.00 | +11.00 | 78 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 56.00 | -90.00 | +35.00 | -19.00 | 30 |
| `current_previous_yr_volumes_crores__1_yr_back` | 429.51 | -30.77 | +46.17 | +63.12 | 58 |
| `current_previous_yr_volumes_crores__current` | 498.79 | +33.83 | -23.33 | +27.54 | 50 |
| `drawdowns_peaks__blw_3` | 407.00 | +322.00 | -568.00 | +152.00 | 89 |
| `gold_etfs_nifty_1_month_chg__gold` | -4.41 | +1.46 | +4.43 | -10.97 | 36 |
| `gold_etfs_nifty_1_month_chg__nifty` | -3.59 | +1.77 | +3.34 | +0.64 | 24 |
| `mbm_2_0_magnitude__abv_10ma` | 34.08 | -12.43 | +17.18 | +15.15 | 34 |
| `mbm_2_0_magnitude__abv_200ma` | 37.91 | -1.15 | +2.31 | -3.89 | 45 |
| `mbm_2_0_magnitude__abv_20ma` | 28.90 | -7.00 | +9.52 | +5.81 | 26 |
| `mbm_2_0_magnitude__abv_50ma` | 29.06 | -4.48 | +3.13 | -2.73 | 27 |
| `mbm_2_0_velocity_advanced__15_52wh` | 18.20 | -2.30 | +0.96 | -2.70 | 61 |
| `mbm_2_0_velocity_advanced__15_52wl` | 30.08 | +0.45 | -2.71 | +3.58 | 68 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.02 | +0.42 | -0.87 | +2.77 | 51 |
| `mbm_2_0_velocity_advanced__30_52wh` | 50.84 | -0.88 | +2.42 | -0.21 | 82 |
| `mbm_2_0_velocity_advanced__breakdowns` | 17.40 | +11.67 | -22.07 | -6.57 | 83 |
| `mbm_2_0_velocity_advanced__breakouts` | 12.17 | -9.00 | +4.19 | -1.16 | 30 |
| `mbm_2_0_velocity_advanced__down_close` | 48.67 | +24.40 | -4.90 | +25.51 | 95 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -11.88 | -2.75 | +3.67 | -6.29 | 34 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 2.82 | -1.30 | +3.28 | -2.98 | 61 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.04 | -0.59 | +6.09 | +4.16 | 42 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.52 | -0.04 | +0.21 | +0.55 | 47 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.56 | +0.55 | -5.88 | -3.61 | 60 |
| `mbm_2_0_velocity_advanced__up_close` | 28.72 | -13.03 | +6.09 | -7.24 | 17 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.88 | +0.17 | -0.21 | -0.04 | 80 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.77 | -0.59 | -2.90 | -4.79 | 50 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.19 | +0.46 | +0.64 | +0.89 | 57 |
| `mbm_2_0_velocity_basic__3_range` | 38.58 | -4.05 | +20.47 | +14.95 | 44 |
| `mbm_2_0_velocity_basic__4_advance` | 3.50 | -5.34 | +1.69 | -1.30 | 22 |
| `mbm_2_0_velocity_basic__4_decline` | 8.47 | +7.08 | -12.68 | +2.92 | 88 |
| `mbm_2_0_velocity_basic__5d_range` | 5.86 | +1.10 | +3.04 | +2.83 | 55 |
| `mbm_2_0_velocity_basic__net_breadth` | -4.97 | -12.42 | +14.37 | -4.21 | 12 |
| `mbm_2_0_velocity_basic__volume` | 0.36 | -0.04 | -0.19 | -0.11 | 27 |
| `net_breadth__net_breadth` | -4.97 | -12.42 | +14.37 | -4.21 | 7 |
| `net_nh_nl__net_nh_nl` | -0.04 | -0.59 | +6.09 | +4.16 | 23 |
| `new_high_low_bearishness_bullishness__high` | 38.00 | -2.00 | +2.00 | +12.00 | 40 |
| `new_high_low_bearishness_bullishness__low` | 39.00 | +11.00 | -166.00 | -90.00 | 60 |
| `volume__volume` | 0.36 | -0.04 | -0.19 | -0.11 | 29 |

## No reading for 2026-10-15

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-12, 63.18
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-12, 36.82
- `oversold_overbought_rsi__overbought`: last 2026-10-12, 126.00
- `oversold_overbought_rsi__oversold`: last 2026-10-12, 144.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-12, 0.33
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-12, 0.65


<!-- market-read -->

## Market read

Thursday turned the repair inside out. The Nifty rose about 1.7 percent, led by private banks, IT, auto and finance. Under
it, most stocks fell. 116 stocks dropped four and a half percent or more, and
only 56 rose that much. The microcap and small company indices fell more than
one percent each. This is the same shape as 24 September, the day after the
last repair peaked, with one difference. Then the long trend lost about a
hundred stocks in a day. On Thursday it lost only 11, and 909 stocks still
hold the 200 day line. The damage sat in the short trend, which gave back
about a third of its repair. The money moved from the small end to the big
names, on turnover well above a year ago, while the VIX fell. The broad
repair has stalled. It has not broken.

Full brief: briefs/2026-10-15.html
