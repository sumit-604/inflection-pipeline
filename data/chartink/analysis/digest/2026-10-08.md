# Market breadth digest: 2026-10-08

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-08: **69** of 79
- History available: 2019-07-01 to 2026-10-08, 693 dated rows
- Metrics with no reading for 2026-10-08: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 16.93 | -21.47 | -13.56 | -26.51 | 7 | 397 |
| % above 20 EMA | 19.40 | -14.11 | -10.91 | -24.28 | 10 | 397 |
| % above 50 EMA | 25.96 | -8.99 | -8.53 | -20.16 | 20 | 397 |
| % above 200 EMA | 35.57 | -5.68 | -6.11 | -13.57 | 39 | 397 |
| Net breadth (4% adv minus dec) | -19.32 | -22.89 | -21.21 | -22.84 | 4 | 397 |
| 4% advancers | 1.81 | -4.38 | -3.96 | -4.91 | 4 | 397 |
| 4% decliners | 21.13 | +18.52 | +17.25 | +17.94 | 96 | 397 |
| Net new highs minus lows | -6.17 | -5.59 | -5.46 | -8.48 | 10 | 397 |
| Net within 15% of 52wk H/L | -15.58 | -7.80 | -10.61 | -22.04 | 31 | 397 |
| Volume expansion ratio | 0.54 | +0.19 | +0.07 | +0.04 | 60 | 397 |
| Overbought count (weekly RSI>70) (as of 2026-10-05) | 126.00 | -23.00 | -132.00 | -18.00 | 46 | 380 |
| Oversold count (weekly RSI<30) (as of 2026-10-05) | 260.00 | +105.00 | +190.00 | +232.00 | 94 | 380 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 975.00 | +849.00 | 97 |
| `4_advance_decline__4_decline` | 503.00 | +441.00 | 99 |
| `4_advance_decline_today__4_decline` | 507.00 | +441.00 | n=19 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,846.00 | +312.00 | 97 |
| `breadth_above_500_trend_reversal__above_20dma` | 412.00 | -311.00 | 8 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 314.00 | +284.00 | 97 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,697.00 | +198.00 | 93 |
| `breadth_above_500_trend_reversal__above_50dma` | 561.00 | -197.00 | 16 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,422.00 | +130.00 | 82 |
| `breadth_above_500_trend_reversal__above_200dma` | 836.00 | -129.00 | 36 |

## At the edge of their own range

Top decile of history:

- `10_from_10dema__10_10ema` at 1.09 (percentile 99, range 0.09 to 1.10)
- `4_advance_decline__4_decline` at 503.00 (percentile 99, range 22.00 to 561.00)
- `52_wk_high_low__new_52_wk_low` at 7.17 (percentile 99, range 0.18 to 7.50)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 12.00 (percentile 98, range 0.00 to 35.00)
- `breadth_above_500_trend_reversal__below_20dma` at 1,846.00 (percentile 97, range 78.00 to 1,982.00)
- `drawdowns_peaks__blw_3` at 975.00 (percentile 97, range 21.00 to 1,869.00)
- `breadth_above_500_trend_reversal__down_4_5_today` at 314.00 (percentile 97, range 1.00 to 966.00)
- `mbm_2_0_velocity_advanced__down_close` at 53.57 (percentile 97, range 4.96 to 72.81)
- `15_up_10_down__10_in_5d` at 4.66 (percentile 96, range 0.34 to 6.55)
- `mbm_2_0_velocity_basic__4_decline` at 21.13 (percentile 96, range 0.28 to 58.23)
- `mbm_2_0_velocity_advanced__breakdowns` at 39.44 (percentile 95, range 2.51 to 94.87)
- `breadth_above_500_trend_reversal__below_50dma` at 1,697.00 (percentile 93, range 276.00 to 1,959.00)
- `new_high_low_bearishness_bullishness__low` at 205.00 (percentile 92, range 1.00 to 913.00)
- `mbm_2_0_velocity_advanced__new_52_wk_low` at 7.48 (percentile 91, range 0.00 to 39.12)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at -6.93 (percentile 1, range -6.93 to 6.35)
- `4_advance_decline__4_advance` at 43.00 (percentile 1, range 43.00 to 479.00)
- `net_breadth__net_breadth` at -19.32 (percentile 2, range -20.64 to 19.72)
- `net_nh_nl__net_nh_nl` at -6.17 (percentile 2, range -6.35 to 3.67)
- `breadth_above_500_trend_reversal__up_4_5_today` at 19.00 (percentile 4, range 6.00 to 1,132.00)
- `mbm_2_0_velocity_basic__4_advance` at 1.81 (percentile 4, range 0.90 to 64.63)
- `mbm_2_0_velocity_basic__net_breadth` at -19.32 (percentile 4, range -57.32 to 63.90)
- `52_wk_high_low__new_52_wk_high` at 1.26 (percentile 5, range 0.86 to 5.21)
- `above_10ma__pct` at 15.52 (percentile 5, range 7.00 to 96.53)
- `above_20_ema__pct` at 17.45 (percentile 6, range 6.35 to 96.00)
- `mbm_2_0_velocity_advanced__breakouts` at 7.98 (percentile 6, range 3.50 to 86.14)
- `mbm_2_0_magnitude__abv_10ma` at 16.93 (percentile 7, range 6.70 to 96.11)
- `mbm_2_0_velocity_advanced__up_close` at 22.63 (percentile 7, range 14.73 to 75.03)
- `above_20ma__pct` at 17.45 (percentile 7, range 7.00 to 96.00)
- `breadth_above_500_trend_reversal__above_20dma` at 412.00 (percentile 8, range 119.00 to 2,061.00)
- `mbm_2_0_velocity_basic__3_range` at 18.19 (percentile 9, range 7.46 to 63.03)
- `mbm_2_0_magnitude__abv_20ma` at 19.40 (percentile 10, range 5.26 to 95.52)
- `mbm_2_0_velocity_advanced__net_nh_nl` at -6.17 (percentile 10, range -38.81 to 4.67)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed down through 50: 96.00 to 19.00
- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 30.00 to 314.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.09 | +0.34 | +0.38 | +0.59 | 99 |
| `15_up_10_down__10_in_5d` | 4.66 | +2.18 | +0.83 | +3.53 | 96 |
| `15_up_10_down__15_in_5d` | 1.55 | -1.01 | -0.26 | -2.43 | 21 |
| `3_above_200_ema__pct` | 33.15 | -5.54 | -5.97 | -18.23 | 24 |
| `4_advance_decline__4_advance` | 43.00 | -104.00 | -94.00 | -117.00 | 1 |
| `4_advance_decline__4_decline` | 503.00 | +441.00 | +411.00 | +427.00 | 99 |
| `4_advance_decline_today__4_advance` | 45.00 | -105.00 | -94.00 | NOT FOUND | n=19 |
| `4_advance_decline_today__4_decline` | 507.00 | +441.00 | +396.00 | NOT FOUND | n=19 |
| `4_advance_decline_today__net_breadth` | -19.31 | -22.82 | -20.48 | NOT FOUND | n=19 |
| `52_week_high_low_within_10__high` | 14.93 | -5.41 | -5.68 | -12.42 | 20 |
| `52_week_high_low_within_10__low` | 32.83 | +3.84 | +6.16 | +14.43 | 82 |
| `52_wk_high_low__new_52_wk_high` | 1.26 | -0.88 | -0.95 | -2.14 | 5 |
| `52_wk_high_low__new_52_wk_low` | 7.17 | +4.37 | +4.26 | +5.94 | 99 |
| `52_wk_high_low_today__new_52_wk_high` | 1.24 | -0.81 | -0.13 | NOT FOUND | n=19 |
| `52_wk_high_low_today__new_52_wk_low` | 6.84 | +4.07 | +1.27 | NOT FOUND | n=19 |
| `5_advance_decline_ratio__advance` | 13.35 | -27.02 | -26.46 | NOT FOUND | n=19 |
| `5_advance_decline_ratio__decline` | 85.61 | +27.02 | +26.46 | NOT FOUND | n=19 |
| `above_10ma__pct` | 15.52 | -19.80 | -11.29 | -24.91 | 5 |
| `above_200ma__above_200ma` | 33.15 | -5.54 | -5.97 | -18.23 | 24 |
| `above_20_ema__pct` | 17.45 | -12.70 | -9.09 | -23.22 | 6 |
| `above_20ma__pct` | 17.45 | -12.70 | -9.09 | -23.22 | 7 |
| `above_50_ema__pct` | 22.83 | -7.95 | -7.17 | -22.53 | 16 |
| `above_50ma__above_50ma` | 33.15 | -5.54 | -5.97 | -18.23 | 24 |
| `breadth_above_500_trend_reversal__above_200dma` | 836.00 | -129.00 | -137.00 | -417.00 | 36 |
| `breadth_above_500_trend_reversal__above_20dma` | 412.00 | -311.00 | -218.00 | -554.00 | 8 |
| `breadth_above_500_trend_reversal__above_50dma` | 561.00 | -197.00 | -172.00 | -519.00 | 16 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,422.00 | +130.00 | +139.00 | +414.00 | 82 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,846.00 | +312.00 | +220.00 | +551.00 | 97 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,697.00 | +198.00 | +174.00 | +516.00 | 93 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 12.00 | +4.00 | +7.00 | +11.00 | 98 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 314.00 | +284.00 | +266.00 | +278.00 | 97 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 17.00 | -9.00 | +7.00 | -22.00 | 57 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 19.00 | -77.00 | -70.00 | -94.00 | 4 |
| `current_previous_yr_volumes_crores__1_yr_back` | 383.34 | -54.52 | -81.11 | -43.26 | 33 |
| `current_previous_yr_volumes_crores__current` | 522.12 | +110.20 | +53.40 | -8.60 | 59 |
| `drawdowns_peaks__blw_3` | 975.00 | +849.00 | +792.00 | +812.00 | 97 |
| `gold_etfs_nifty_1_month_chg__gold` | -8.84 | +0.11 | -5.08 | -16.67 | 15 |
| `gold_etfs_nifty_1_month_chg__nifty` | -6.93 | -1.44 | -1.46 | -6.22 | 1 |
| `mbm_2_0_magnitude__abv_10ma` | 16.93 | -21.47 | -13.56 | -26.51 | 7 |
| `mbm_2_0_magnitude__abv_200ma` | 35.57 | -5.68 | -6.11 | -13.57 | 39 |
| `mbm_2_0_magnitude__abv_20ma` | 19.40 | -14.11 | -10.91 | -24.28 | 10 |
| `mbm_2_0_magnitude__abv_50ma` | 25.96 | -8.99 | -8.53 | -20.16 | 20 |
| `mbm_2_0_velocity_advanced__15_52wh` | 17.22 | -5.03 | -5.26 | -11.02 | 52 |
| `mbm_2_0_velocity_advanced__15_52wl` | 32.80 | +2.78 | +5.35 | +11.02 | 71 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.89 | +2.42 | +3.41 | +8.52 | 56 |
| `mbm_2_0_velocity_advanced__30_52wh` | 48.38 | -2.92 | -3.41 | -5.71 | 73 |
| `mbm_2_0_velocity_advanced__breakdowns` | 39.44 | +31.95 | +29.84 | +30.46 | 95 |
| `mbm_2_0_velocity_advanced__breakouts` | 7.98 | -7.07 | -11.60 | -7.04 | 6 |
| `mbm_2_0_velocity_advanced__down_close` | 53.57 | +18.74 | +13.22 | +18.05 | 97 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -15.58 | -7.80 | -10.61 | -22.04 | 31 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -0.50 | -5.34 | -6.82 | -14.23 | 53 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -6.17 | -5.59 | -5.46 | -8.48 | 10 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.30 | -1.09 | -1.27 | -2.47 | 38 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 7.48 | +4.49 | +4.19 | +6.01 | 91 |
| `mbm_2_0_velocity_advanced__up_close` | 22.63 | -18.43 | -6.83 | -22.06 | 7 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.09 | +0.34 | +0.38 | +0.59 | 87 |
| `mbm_2_0_velocity_basic__10_in_5d` | 4.66 | +2.18 | +0.83 | +3.53 | 85 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.55 | -1.01 | -0.26 | -2.43 | 36 |
| `mbm_2_0_velocity_basic__3_range` | 18.19 | -25.51 | -15.46 | -27.30 | 9 |
| `mbm_2_0_velocity_basic__4_advance` | 1.81 | -4.38 | -3.96 | -4.91 | 4 |
| `mbm_2_0_velocity_basic__4_decline` | 21.13 | +18.52 | +17.25 | +17.94 | 96 |
| `mbm_2_0_velocity_basic__5d_range` | 2.86 | -0.00 | -0.01 | -7.59 | 30 |
| `mbm_2_0_velocity_basic__net_breadth` | -19.32 | -22.89 | -21.21 | -22.84 | 4 |
| `mbm_2_0_velocity_basic__volume` | 0.54 | +0.19 | +0.07 | +0.04 | 60 |
| `net_breadth__net_breadth` | -19.32 | -22.89 | -21.21 | -22.84 | 2 |
| `net_nh_nl__net_nh_nl` | -6.17 | -5.59 | -5.46 | -8.48 | 2 |
| `new_high_low_bearishness_bullishness__high` | 36.00 | -25.00 | -27.00 | -66.00 | 37 |
| `new_high_low_bearishness_bullishness__low` | 205.00 | +125.00 | +122.00 | +168.00 | 92 |
| `volume__volume` | 0.54 | +0.19 | +0.07 | +0.04 | 73 |

## No reading for 2026-10-08

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-05, 58.28
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-05, 41.72
- `oversold_overbought_rsi__overbought`: last 2026-10-05, 126.00
- `oversold_overbought_rsi__oversold`: last 2026-10-05, 260.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-05, 0.30
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-05, 0.68


<!-- market-read -->

## Market read

Thursday was a heavy, wide selling day that broke the base of the past week.
314 stocks fell four and a half percent or more, and only 19 rose that much.
Almost nine stocks in ten closed lower, and no stock index rose. The count of
stocks above the two-hundred-day average fell to 836, below the 1 October low
near 900 and the lowest since mid-April. The count above the fifty-day
average fell to 561. New yearly lows beat new highs by more than five to one.
Turnover ran about a third above a year ago, so sellers came with size. Fear
rose by a tenth. A small set of groups held up: jewellers, a few small metal
names, sugar, small pharma leaders and defence. Friday's data has not yet
arrived, so the market stands, for now, at a fresh lower low with no sign
yet of buyers returning.

Full brief: briefs/2026-10-08.html
