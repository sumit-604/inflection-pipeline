# Market breadth digest: 2026-10-12

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-12: **75** of 79
- History available: 2019-07-01 to 2026-10-12, 695 dated rows
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 29.90 | +6.45 | +6.18 | -7.29 | 26 | 399 |
| % above 20 EMA | 26.80 | +3.43 | +2.87 | -12.45 | 21 | 399 |
| % above 50 EMA | 29.56 | +3.04 | -0.61 | -14.52 | 28 | 399 |
| % above 200 EMA | 37.44 | +1.31 | -1.54 | -10.40 | 44 | 399 |
| Net breadth (4% adv minus dec) | 4.06 | +0.27 | +3.39 | +1.54 | 65 | 399 |
| 4% advancers | 7.41 | +0.97 | +1.17 | +1.31 | 72 | 399 |
| 4% decliners | 3.35 | +0.70 | -2.22 | -0.23 | 61 | 399 |
| Net new highs minus lows | -1.26 | +3.16 | +0.55 | -1.38 | 28 | 399 |
| Net within 15% of 52wk H/L | -12.60 | +1.42 | -2.00 | -17.91 | 33 | 399 |
| Volume expansion ratio | 0.29 | -0.01 | -0.06 | -0.16 | 11 | 399 |
| Overbought count (weekly RSI>70) | 139.00 | +5.00 | -108.00 | -24.00 | 50 | 381 |
| Oversold count (weekly RSI<30) | 204.00 | -3.00 | +115.00 | +170.00 | 91 | 381 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `breadth_above_500_trend_reversal__above_20dma` | 570.00 | +74.00 | 21 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,683.00 | -74.00 | 93 |
| `new_high_low_bearishness_bullishness__low` | 83.00 | -68.00 | 79 |
| `breadth_above_500_trend_reversal__above_50dma` | 634.00 | +61.00 | 23 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,619.00 | -61.00 | 88 |
| `current_previous_yr_volumes_crores__1_yr_back` | 449.26 | +52.93 | 69 |
| `current_previous_yr_volumes_crores__current` | 422.93 | -31.34 | 12 |
| `drawdowns_peaks__blw_3` | 153.00 | +28.00 | 59 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 118.00 | +28.00 | 75 |
| `4_advance_decline__4_advance` | 177.00 | +24.00 | 73 |

## At the edge of their own range

Top decile of history:

- `10_from_10dema__10_10ema` at 1.17 (percentile 100, range 0.09 to 1.17)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 9.00 (percentile 96, range 0.00 to 35.00)
- `breadth_above_500_trend_reversal__below_20dma` at 1,683.00 (percentile 93, range 77.00 to 1,975.00)
- `oversold_overbought_rsi__oversold` at 204.00 (percentile 91, range 2.00 to 872.00)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at -5.84 (percentile 6, range -6.93 to 6.35)
- `volume__volume` at 0.29 (percentile 10, range 0.24 to 1.11)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.17 | +0.08 | +0.21 | +0.67 | 100 |
| `15_up_10_down__10_in_5d` | 2.64 | -0.31 | -3.10 | +0.96 | 75 |
| `15_up_10_down__15_in_5d` | 2.18 | +0.41 | +0.54 | -0.89 | 48 |
| `3_above_200_ema__pct` | 34.87 | +0.71 | -2.20 | -14.28 | 27 |
| `4_advance_decline__4_advance` | 177.00 | +24.00 | +28.00 | +32.00 | 73 |
| `4_advance_decline__4_decline` | 80.00 | +17.00 | -53.00 | -5.00 | 57 |
| `4_advance_decline_today__4_advance` | 178.00 | +23.00 | +102.00 | -14.00 | 81 |
| `4_advance_decline_today__4_decline` | 80.00 | +13.00 | -135.00 | +26.00 | 48 |
| `4_advance_decline_today__net_breadth` | 4.10 | +0.42 | +9.91 | -1.73 | 76 |
| `52_week_high_low_within_10__high` | 17.31 | +0.90 | -0.79 | -8.76 | 32 |
| `52_week_high_low_within_10__low` | 31.24 | +0.21 | +1.01 | +11.47 | 79 |
| `52_wk_high_low__new_52_wk_high` | 1.60 | +0.55 | +0.10 | -0.67 | 14 |
| `52_wk_high_low__new_52_wk_low` | 2.89 | -2.40 | -0.25 | +0.72 | 88 |
| `52_wk_high_low_today__new_52_wk_high` | 1.56 | +0.52 | +0.00 | -1.53 | 29 |
| `52_wk_high_low_today__new_52_wk_low` | 2.77 | -2.31 | -4.39 | +1.52 | 62 |
| `5_advance_decline_ratio__advance` | 49.09 | -13.09 | +25.13 | -5.60 | 76 |
| `5_advance_decline_ratio__decline` | 49.87 | +13.09 | -25.13 | +5.61 | 29 |
| `above_10ma__pct` | 27.41 | +3.18 | +6.11 | -7.47 | 19 |
| `above_200ma__above_200ma` | 34.87 | +0.71 | -2.20 | -14.28 | 28 |
| `above_20_ema__pct` | 24.07 | +2.64 | +2.83 | -12.98 | 17 |
| `above_20ma__pct` | 24.07 | +2.64 | +2.83 | -12.98 | 17 |
| `above_50_ema__pct` | 25.84 | +2.28 | -0.45 | -16.97 | 18 |
| `above_50ma__above_50ma` | 34.87 | +0.71 | -2.20 | -14.28 | 28 |
| `breadth_above_500_trend_reversal__above_200dma` | 875.00 | +19.00 | -50.00 | -311.00 | 40 |
| `breadth_above_500_trend_reversal__above_20dma` | 570.00 | +74.00 | +67.00 | -297.00 | 21 |
| `breadth_above_500_trend_reversal__above_50dma` | 634.00 | +61.00 | -11.00 | -389.00 | 23 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,378.00 | -19.00 | +50.00 | +310.00 | 78 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,683.00 | -74.00 | -67.00 | +296.00 | 93 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,619.00 | -61.00 | +11.00 | +388.00 | 88 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 9.00 | -2.00 | +2.00 | +4.00 | 96 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 38.00 | +11.00 | -30.00 | -13.00 | 62 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 17.00 | -1.00 | +8.00 | -15.00 | 58 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 118.00 | +28.00 | +18.00 | +23.00 | 75 |
| `current_previous_yr_volumes_crores__1_yr_back` | 449.26 | +52.93 | +33.67 | -9.24 | 69 |
| `current_previous_yr_volumes_crores__current` | 422.93 | -31.34 | +3.21 | -95.91 | 12 |
| `drawdowns_peaks__blw_3` | 153.00 | +28.00 | -77.00 | -53.00 | 59 |
| `gold_etfs_nifty_1_month_chg__gold` | -6.68 | +0.50 | -1.07 | -14.13 | 24 |
| `gold_etfs_nifty_1_month_chg__nifty` | -5.84 | -0.17 | +0.04 | -3.52 | 6 |
| `mbm_2_0_magnitude__abv_10ma` | 29.90 | +6.45 | +6.18 | -7.29 | 26 |
| `mbm_2_0_magnitude__abv_200ma` | 37.44 | +1.31 | -1.54 | -10.40 | 44 |
| `mbm_2_0_magnitude__abv_20ma` | 26.80 | +3.43 | +2.87 | -12.45 | 21 |
| `mbm_2_0_magnitude__abv_50ma` | 29.56 | +3.04 | -0.61 | -14.52 | 28 |
| `mbm_2_0_velocity_advanced__15_52wh` | 19.01 | +1.24 | -1.02 | -8.08 | 68 |
| `mbm_2_0_velocity_advanced__15_52wl` | 31.62 | -0.17 | +0.98 | +9.82 | 70 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.45 | -0.31 | +1.05 | +7.05 | 54 |
| `mbm_2_0_velocity_advanced__30_52wh` | 49.20 | +0.19 | -0.63 | -4.65 | 75 |
| `mbm_2_0_velocity_advanced__breakdowns` | 9.34 | -1.44 | -3.53 | -0.84 | 58 |
| `mbm_2_0_velocity_advanced__breakouts` | 20.85 | +3.97 | +1.41 | +5.79 | 79 |
| `mbm_2_0_velocity_advanced__down_close` | 35.87 | +11.27 | -7.45 | +0.75 | 60 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -12.60 | +1.42 | -2.00 | -17.91 | 33 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 0.75 | +0.50 | -1.68 | -11.70 | 55 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -1.26 | +3.16 | +0.55 | -1.38 | 28 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.84 | +0.66 | +0.17 | -0.89 | 58 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 3.10 | -2.50 | -0.38 | +0.49 | 77 |
| `mbm_2_0_velocity_advanced__up_close` | 35.54 | -2.61 | +3.43 | -4.96 | 42 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.17 | +0.08 | +0.21 | +0.67 | 89 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.64 | -0.31 | -3.10 | +0.96 | 64 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.18 | +0.41 | +0.54 | -0.89 | 56 |
| `mbm_2_0_velocity_basic__3_range` | 36.47 | +1.57 | +7.26 | -7.32 | 37 |
| `mbm_2_0_velocity_basic__4_advance` | 7.41 | +0.97 | +1.17 | +1.31 | 72 |
| `mbm_2_0_velocity_basic__4_decline` | 3.35 | +0.70 | -2.22 | -0.23 | 61 |
| `mbm_2_0_velocity_basic__5d_range` | 3.48 | +0.11 | +1.46 | -5.74 | 37 |
| `mbm_2_0_velocity_basic__net_breadth` | 4.06 | +0.27 | +3.39 | +1.54 | 65 |
| `mbm_2_0_velocity_basic__volume` | 0.29 | -0.01 | -0.06 | -0.16 | 11 |
| `net_breadth__net_breadth` | 4.06 | +0.27 | +3.39 | +1.54 | 63 |
| `net_nh_nl__net_nh_nl` | -1.26 | +3.16 | +0.55 | -1.38 | 12 |
| `new_high_low_bearishness_bullishness__high` | 46.00 | +16.00 | +3.00 | -22.00 | 50 |
| `new_high_low_bearishness_bullishness__low` | 83.00 | -68.00 | -7.00 | +18.00 | 79 |
| `nifty_500_above_below_200_ema__above_200_ema` | 60.16 | -0.80 | -8.85 | -11.85 | 21 |
| `nifty_500_above_below_200_ema__below_200_ema` | 39.84 | +0.80 | +8.85 | +11.85 | 80 |
| `oversold_overbought_rsi__overbought` | 139.00 | +5.00 | -108.00 | -24.00 | 50 |
| `oversold_overbought_rsi__oversold` | 204.00 | -3.00 | +115.00 | +170.00 | 91 |
| `volume__volume` | 0.29 | -0.01 | -0.06 | -0.16 | 10 |
| `weekly_rsi_50_50__above_rsi_50` | 0.32 | +0.00 | -0.12 | -0.14 | 22 |
| `weekly_rsi_50_50__below_rsi_50` | 0.66 | +0.00 | +0.17 | +0.17 | 78 |


<!-- market-read -->

## Market read

Monday split the market in two. The Nifty fell about 0.7 percent, and the
small company index rose about 1.4 percent. About as many stocks rose as
fell. Yet 118 stocks jumped four and a half percent or more, against 38 that
fell that much. New yearly lows almost halved, from 151 to 83, and new highs
rose from 30 to 46. The count of stocks above the fifty-day average climbed
back above its 1 October low. The count above the two-hundred-day average
did not. It stands at 875, still under the 1 October mark of about 900. Fear
rose while small stocks rose: the VIX climbed about six percent to about 15.
Turnover ran below a year ago. The repair under the surface kept going for a
second day, while the big names sagged. It is a slow repair, not a thrust.

Full brief: briefs/2026-10-12.html
