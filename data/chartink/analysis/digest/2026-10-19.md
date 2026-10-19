# Market breadth digest: 2026-10-19

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-19: **75** of 79
- History available: 2019-07-01 to 2026-10-19, 700 dated rows
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 25.69 | -15.17 | -4.16 | -16.55 | 19 | 404 |
| % above 20 EMA | 23.43 | -10.20 | -3.32 | -14.27 | 18 | 404 |
| % above 50 EMA | 25.36 | -5.96 | -4.24 | -14.44 | 18 | 404 |
| % above 200 EMA | 35.77 | -3.29 | -1.72 | -9.33 | 39 | 404 |
| Net breadth (4% adv minus dec) | -8.31 | -12.69 | -12.38 | -17.19 | 8 | 404 |
| 4% advancers | 2.90 | -4.13 | -4.52 | -7.87 | 14 | 404 |
| 4% decliners | 11.21 | +8.56 | +7.85 | +9.32 | 93 | 404 |
| Net new highs minus lows | -2.56 | -1.97 | -1.30 | -3.36 | 19 | 404 |
| Net within 15% of 52wk H/L | -15.74 | -4.93 | -3.12 | -16.84 | 29 | 404 |
| Volume expansion ratio | 0.29 | -0.06 | -0.01 | -0.38 | 10 | 404 |
| Overbought count (weekly RSI>70) | 102.00 | -27.00 | -98.00 | -65.00 | 37 | 382 |
| Oversold count (weekly RSI<30) | 165.00 | +33.00 | +83.00 | +134.00 | 88 | 382 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 549.00 | +429.00 | 93 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,690.00 | +234.00 | 93 |
| `breadth_above_500_trend_reversal__above_20dma` | 567.00 | -233.00 | 21 |
| `4_advance_decline__4_decline` | 267.00 | +204.00 | 97 |
| `4_advance_decline_today__4_decline` | 268.00 | +202.00 | 92 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,691.00 | +146.00 | 93 |
| `breadth_above_500_trend_reversal__above_50dma` | 566.00 | -145.00 | 17 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 154.00 | +119.00 | 93 |
| `4_advance_decline_today__4_advance` | 71.00 | -99.00 | 12 |
| `4_advance_decline__4_advance` | 69.00 | -98.00 | 10 |

## At the edge of their own range

Top decile of history:

- `10_from_10dema__10_10ema` at 1.34 (percentile 100, range 0.09 to 1.34)
- `4_advance_decline__4_decline` at 267.00 (percentile 97, range 22.00 to 561.00)
- `drawdowns_peaks__blw_3` at 549.00 (percentile 93, range 21.00 to 1,869.00)
- `breadth_above_500_trend_reversal__down_4_5_today` at 154.00 (percentile 93, range 1.00 to 961.00)
- `breadth_above_500_trend_reversal__below_20dma` at 1,690.00 (percentile 93, range 76.00 to 1,973.00)
- `breadth_above_500_trend_reversal__below_50dma` at 1,691.00 (percentile 93, range 274.00 to 1,950.00)
- `mbm_2_0_velocity_basic__4_decline` at 11.21 (percentile 93, range 0.28 to 58.24)
- `4_advance_decline_today__4_decline` at 268.00 (percentile 92, range 36.00 to 561.00)
- `52_wk_high_low__new_52_wk_low` at 3.66 (percentile 92, range 0.18 to 7.50)
- `mbm_2_0_velocity_basic__10_10ema` at 1.34 (percentile 92, range 0.00 to 16.95)
- `mbm_2_0_velocity_advanced__down_close` at 45.03 (percentile 91, range 4.97 to 72.78)
- `mbm_2_0_velocity_advanced__breakdowns` at 24.89 (percentile 91, range 2.47 to 94.86)

Bottom decile of history:

- `net_breadth__net_breadth` at -8.31 (percentile 4, range -20.71 to 19.72)
- `net_nh_nl__net_nh_nl` at -2.56 (percentile 7, range -6.32 to 3.67)
- `mbm_2_0_velocity_basic__net_breadth` at -8.31 (percentile 8, range -57.34 to 63.90)
- `volume__volume` at 0.29 (percentile 9, range 0.24 to 1.11)
- `mbm_2_0_velocity_basic__volume` at 0.29 (percentile 10, range 0.03 to 5.71)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed down through 50: 105.00 to 44.00
- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 35.00 to 154.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.34 | +0.50 | +0.17 | +0.75 | 100 |
| `15_up_10_down__10_in_5d` | 3.23 | +1.76 | +0.59 | +0.50 | 87 |
| `15_up_10_down__15_in_5d` | 2.06 | -0.30 | -0.12 | +0.67 | 44 |
| `3_above_200_ema__pct` | 33.47 | -3.58 | -1.39 | -12.38 | 25 |
| `4_advance_decline__4_advance` | 69.00 | -98.00 | -108.00 | -187.00 | 10 |
| `4_advance_decline__4_decline` | 267.00 | +204.00 | +187.00 | +222.00 | 97 |
| `4_advance_decline_today__4_advance` | 71.00 | -99.00 | -107.00 | -34.00 | 12 |
| `4_advance_decline_today__4_decline` | 268.00 | +202.00 | +188.00 | +183.00 | 92 |
| `4_advance_decline_today__net_breadth` | -8.25 | -12.60 | -12.34 | -9.08 | 12 |
| `52_week_high_low_within_10__high` | 14.70 | -2.83 | -2.61 | -8.78 | 19 |
| `52_week_high_low_within_10__low` | 30.41 | +2.21 | -0.84 | +9.40 | 77 |
| `52_wk_high_low__new_52_wk_high` | 1.50 | +0.10 | -0.10 | -0.87 | 15 |
| `52_wk_high_low__new_52_wk_low` | 3.66 | +1.63 | +0.77 | +1.89 | 92 |
| `52_wk_high_low_today__new_52_wk_high` | 1.46 | +0.10 | -0.10 | -0.03 | 31 |
| `52_wk_high_low_today__new_52_wk_low` | 3.48 | +1.40 | +0.72 | -0.13 | 73 |
| `5_advance_decline_ratio__advance` | 20.93 | -38.18 | -28.16 | -16.31 | 15 |
| `5_advance_decline_ratio__decline` | 78.03 | +38.18 | +28.16 | +16.35 | 88 |
| `above_10ma__pct` | 27.45 | -15.49 | +0.03 | -14.37 | 19 |
| `above_200ma__above_200ma` | 33.47 | -3.58 | -1.39 | -12.38 | 26 |
| `above_20_ema__pct` | 24.07 | -10.08 | +0.00 | -11.84 | 17 |
| `above_20ma__pct` | 24.07 | -10.08 | +0.00 | -11.84 | 17 |
| `above_50_ema__pct` | 23.27 | -5.74 | -2.58 | -14.85 | 16 |
| `above_50ma__above_50ma` | 33.47 | -3.58 | -1.39 | -12.38 | 26 |
| `breadth_above_500_trend_reversal__above_200dma` | 853.00 | -86.00 | -27.00 | -272.00 | 37 |
| `breadth_above_500_trend_reversal__above_20dma` | 567.00 | -233.00 | -5.00 | -280.00 | 21 |
| `breadth_above_500_trend_reversal__above_50dma` | 566.00 | -145.00 | -73.00 | -344.00 | 17 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,404.00 | +87.00 | +28.00 | +272.00 | 81 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,690.00 | +234.00 | +6.00 | +280.00 | 93 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,691.00 | +146.00 | +74.00 | +344.00 | 93 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 5.00 | +4.00 | -4.00 | -1.00 | 89 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 154.00 | +119.00 | +114.00 | +129.00 | 93 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 16.00 | -8.00 | -1.00 | +1.00 | 55 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 44.00 | -61.00 | -73.00 | -124.00 | 19 |
| `current_previous_yr_volumes_crores__1_yr_back` | 480.66 | +50.69 | +31.39 | +84.64 | 81 |
| `current_previous_yr_volumes_crores__current` | 513.87 | -82.77 | +73.55 | +3.40 | 55 |
| `drawdowns_peaks__blw_3` | 549.00 | +429.00 | +396.00 | +434.00 | 93 |
| `gold_etfs_nifty_1_month_chg__gold` | -5.01 | -2.36 | +1.67 | -8.40 | 33 |
| `gold_etfs_nifty_1_month_chg__nifty` | -3.71 | -0.94 | +2.13 | +0.37 | 23 |
| `mbm_2_0_magnitude__abv_10ma` | 25.69 | -15.17 | -4.16 | -16.55 | 19 |
| `mbm_2_0_magnitude__abv_200ma` | 35.77 | -3.29 | -1.72 | -9.33 | 39 |
| `mbm_2_0_magnitude__abv_20ma` | 23.43 | -10.20 | -3.32 | -14.27 | 18 |
| `mbm_2_0_magnitude__abv_50ma` | 25.36 | -5.96 | -4.24 | -14.44 | 18 |
| `mbm_2_0_velocity_advanced__15_52wh` | 15.66 | -2.94 | -3.38 | -8.99 | 39 |
| `mbm_2_0_velocity_advanced__15_52wl` | 31.40 | +1.98 | -0.25 | +7.84 | 70 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 49.50 | +1.47 | +1.07 | +6.84 | 58 |
| `mbm_2_0_velocity_advanced__30_52wh` | 49.58 | -2.10 | +0.31 | -3.55 | 76 |
| `mbm_2_0_velocity_advanced__breakdowns` | 24.89 | +16.10 | +15.59 | +18.12 | 91 |
| `mbm_2_0_velocity_advanced__breakouts` | 10.66 | -6.80 | -10.18 | -13.36 | 19 |
| `mbm_2_0_velocity_advanced__down_close` | 45.03 | +14.88 | +8.99 | +17.08 | 91 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -15.74 | -4.93 | -3.12 | -16.84 | 29 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 0.08 | -3.58 | -0.75 | -10.39 | 53 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -2.56 | -1.97 | -1.30 | -3.36 | 19 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.64 | +0.08 | -0.21 | -1.18 | 52 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 4.20 | +2.05 | +1.10 | +2.18 | 82 |
| `mbm_2_0_velocity_advanced__up_close` | 27.17 | -13.08 | -8.45 | -17.67 | 13 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.34 | +0.50 | +0.17 | +0.75 | 92 |
| `mbm_2_0_velocity_basic__10_in_5d` | 3.23 | +1.76 | +0.59 | +0.50 | 73 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.06 | -0.30 | -0.12 | +0.67 | 54 |
| `mbm_2_0_velocity_basic__3_range` | 30.48 | -11.78 | -5.96 | -5.83 | 24 |
| `mbm_2_0_velocity_basic__4_advance` | 2.90 | -4.13 | -4.52 | -7.87 | 14 |
| `mbm_2_0_velocity_basic__4_decline` | 11.21 | +8.56 | +7.85 | +9.32 | 93 |
| `mbm_2_0_velocity_basic__5d_range` | 5.58 | -1.36 | +2.10 | +2.22 | 52 |
| `mbm_2_0_velocity_basic__net_breadth` | -8.31 | -12.69 | -12.38 | -17.19 | 8 |
| `mbm_2_0_velocity_basic__volume` | 0.29 | -0.06 | -0.01 | -0.38 | 10 |
| `net_breadth__net_breadth` | -8.31 | -12.69 | -12.38 | -17.19 | 4 |
| `net_nh_nl__net_nh_nl` | -2.56 | -1.97 | -1.30 | -3.36 | 7 |
| `new_high_low_bearishness_bullishness__high` | 43.00 | +3.00 | -3.00 | -28.00 | 48 |
| `new_high_low_bearishness_bullishness__low` | 105.00 | +47.00 | +22.00 | +52.00 | 84 |
| `nifty_500_above_below_200_ema__above_200_ema` | 61.17 | -0.60 | -7.44 | -9.42 | 21 |
| `nifty_500_above_below_200_ema__below_200_ema` | 38.83 | +0.60 | +7.44 | +9.42 | 79 |
| `oversold_overbought_rsi__overbought` | 102.00 | -27.00 | -98.00 | -65.00 | 37 |
| `oversold_overbought_rsi__oversold` | 165.00 | +33.00 | +83.00 | +134.00 | 88 |
| `volume__volume` | 0.29 | -0.06 | -0.01 | -0.38 | 9 |
| `weekly_rsi_50_50__above_rsi_50` | 0.30 | -0.04 | -0.12 | -0.15 | 19 |
| `weekly_rsi_50_50__below_rsi_50` | 0.68 | +0.04 | +0.18 | +0.17 | 82 |


<!-- market-read -->

## Market read

Monday took back almost all of the repair in one session. On Friday 939 stocks held their 200 day line. On Monday 853 did, only 15 above the 8 October low of 838. 154 stocks fell four and a half percent or more, and only 44 rose that much. That is the third heaviest down day of the autumn, after 15 September and 8 October. About four stocks in five fell. New yearly lows jumped from 58 to 105. Only two of 35 indices rose, state banks and the VIX. The Nifty fell about one percent. Yet this was no panic. Turnover was ordinary, few stocks traded on heavy volume, and deep five day falls stayed rare. The staircase of lower peaks still stands, and the floor under it is now under test.

Full brief: briefs/2026-10-19.html
