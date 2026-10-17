# Market breadth digest: 2026-10-16

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-16: **69** of 79
- History available: 2019-07-01 to 2026-10-16, 699 dated rows
- Metrics with no reading for 2026-10-16: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 40.87 | +6.80 | +17.44 | +12.98 | 46 | 403 |
| % above 20 EMA | 33.63 | +4.71 | +10.28 | +5.36 | 35 | 403 |
| % above 50 EMA | 31.31 | +2.22 | +4.81 | -3.48 | 33 | 403 |
| % above 200 EMA | 39.06 | +1.11 | +2.90 | -3.82 | 48 | 403 |
| Net breadth (4% adv minus dec) | 4.38 | +9.39 | +0.58 | -1.23 | 67 | 403 |
| 4% advancers | 7.03 | +3.57 | +0.58 | -0.93 | 67 | 403 |
| 4% decliners | 2.65 | -5.82 | -0.00 | +0.29 | 47 | 403 |
| Net new highs minus lows | -0.59 | -0.55 | +3.84 | +0.08 | 33 | 403 |
| Net within 15% of 52wk H/L | -10.82 | +1.03 | +3.22 | -8.67 | 35 | 403 |
| Volume expansion ratio | 0.35 | -0.01 | +0.04 | +0.08 | 25 | 403 |
| Overbought count (weekly RSI>70) (as of 2026-10-12) | 129.00 | -5.00 | -118.00 | -34.00 | 46 | 381 |
| Oversold count (weekly RSI<30) (as of 2026-10-12) | 132.00 | -75.00 | +43.00 | +98.00 | 85 | 381 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 120.00 | -287.00 | 46 |
| `4_advance_decline__4_decline` | 63.00 | -138.00 | 44 |
| `4_advance_decline_today__4_decline` | 66.00 | -138.00 | 36 |
| `breadth_above_500_trend_reversal__above_20dma` | 799.00 | +114.00 | 36 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,466.00 | -113.00 | 77 |
| `current_previous_yr_volumes_crores__current` | 596.64 | +97.85 | 84 |
| `4_advance_decline__4_advance` | 167.00 | +85.00 | 61 |
| `4_advance_decline_today__4_advance` | 170.00 | +84.00 | 76 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 35.00 | -81.00 | 56 |
| `breadth_above_500_trend_reversal__above_50dma` | 707.00 | +57.00 | 28 |

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 116.00 to 35.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.84 | -0.04 | -0.25 | -0.08 | 85 |
| `15_up_10_down__10_in_5d` | 1.47 | -0.30 | -1.48 | -2.70 | 36 |
| `15_up_10_down__15_in_5d` | 2.36 | +0.16 | +0.59 | +1.18 | 51 |
| `3_above_200_ema__pct` | 37.05 | +1.40 | +2.90 | -6.20 | 32 |
| `4_advance_decline__4_advance` | 167.00 | +85.00 | +14.00 | -22.00 | 61 |
| `4_advance_decline__4_decline` | 63.00 | -138.00 | +0.00 | +7.00 | 44 |
| `4_advance_decline_today__4_advance` | 170.00 | +84.00 | +15.00 | +31.00 | 76 |
| `4_advance_decline_today__4_decline` | 66.00 | -138.00 | -1.00 | -20.00 | 36 |
| `4_advance_decline_today__net_breadth` | 4.35 | +9.29 | +0.68 | +2.11 | 80 |
| `52_week_high_low_within_10__high` | 17.53 | +0.75 | +1.12 | -4.05 | 34 |
| `52_week_high_low_within_10__low` | 28.20 | -0.52 | -2.83 | +6.22 | 71 |
| `52_wk_high_low__new_52_wk_high` | 1.40 | +0.07 | +0.35 | +0.13 | 11 |
| `52_wk_high_low__new_52_wk_low` | 2.03 | +0.66 | -3.27 | +0.23 | 78 |
| `52_wk_high_low_today__new_52_wk_high` | 1.37 | +0.07 | +0.33 | -0.84 | 24 |
| `52_wk_high_low_today__new_52_wk_low` | 2.08 | +0.62 | -2.99 | -0.35 | 40 |
| `5_advance_decline_ratio__advance` | 59.11 | +22.79 | -3.06 | +22.26 | 84 |
| `5_advance_decline_ratio__decline` | 39.84 | -22.79 | +3.06 | -22.25 | 20 |
| `above_10ma__pct` | 42.93 | +7.03 | +18.70 | +17.08 | 51 |
| `above_200ma__above_200ma` | 37.05 | +1.40 | +2.90 | -6.20 | 33 |
| `above_20_ema__pct` | 34.15 | +4.80 | +12.73 | +8.53 | 31 |
| `above_20ma__pct` | 34.15 | +4.80 | +12.73 | +8.53 | 30 |
| `above_50_ema__pct` | 29.01 | +2.53 | +5.44 | -2.59 | 20 |
| `above_50ma__above_50ma` | 37.05 | +1.40 | +2.90 | -6.20 | 33 |
| `breadth_above_500_trend_reversal__above_200dma` | 936.00 | +26.00 | +77.00 | -130.00 | 46 |
| `breadth_above_500_trend_reversal__above_20dma` | 799.00 | +114.00 | +301.00 | +200.00 | 36 |
| `breadth_above_500_trend_reversal__above_50dma` | 707.00 | +57.00 | +133.00 | -58.00 | 28 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,329.00 | -25.00 | -76.00 | +130.00 | 72 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,466.00 | -113.00 | -300.00 | -200.00 | 77 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,558.00 | -56.00 | -132.00 | +58.00 | 85 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 1.00 | -1.00 | -10.00 | -2.00 | 43 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 35.00 | -81.00 | +8.00 | +12.00 | 56 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 24.00 | -1.00 | +6.00 | +14.00 | 76 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 103.00 | +47.00 | +12.00 | -21.00 | 68 |
| `current_previous_yr_volumes_crores__1_yr_back` | 429.97 | +0.45 | +33.64 | +22.13 | 59 |
| `current_previous_yr_volumes_crores__current` | 596.64 | +97.85 | +142.37 | +217.84 | 84 |
| `drawdowns_peaks__blw_3` | 120.00 | -287.00 | -5.00 | +2.00 | 46 |
| `gold_etfs_nifty_1_month_chg__gold` | -2.64 | +1.76 | +4.53 | -6.77 | 45 |
| `gold_etfs_nifty_1_month_chg__nifty` | -2.77 | +0.82 | +2.90 | +1.44 | 27 |
| `mbm_2_0_magnitude__abv_10ma` | 40.87 | +6.80 | +17.44 | +12.98 | 46 |
| `mbm_2_0_magnitude__abv_200ma` | 39.06 | +1.11 | +2.90 | -3.82 | 48 |
| `mbm_2_0_magnitude__abv_20ma` | 33.63 | +4.71 | +10.28 | +5.36 | 35 |
| `mbm_2_0_magnitude__abv_50ma` | 31.31 | +2.22 | +4.81 | -3.48 | 33 |
| `mbm_2_0_velocity_advanced__15_52wh` | 18.60 | +0.39 | +0.82 | -4.27 | 64 |
| `mbm_2_0_velocity_advanced__15_52wl` | 29.42 | -0.64 | -2.40 | +4.40 | 67 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.02 | +0.05 | -0.73 | +3.83 | 52 |
| `mbm_2_0_velocity_advanced__30_52wh` | 51.68 | +0.80 | +2.63 | -0.09 | 85 |
| `mbm_2_0_velocity_advanced__breakdowns` | 8.80 | -8.62 | -1.99 | +1.21 | 54 |
| `mbm_2_0_velocity_advanced__breakouts` | 17.47 | +5.32 | +0.57 | -4.06 | 66 |
| `mbm_2_0_velocity_advanced__down_close` | 30.14 | -18.52 | +5.53 | -0.97 | 30 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -10.82 | +1.03 | +3.22 | -8.67 | 35 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 3.66 | +0.75 | +3.37 | -3.92 | 63 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.59 | -0.55 | +3.84 | +0.08 | 33 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.56 | +0.04 | +0.38 | +0.12 | 48 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 2.15 | +0.59 | -3.46 | +0.04 | 69 |
| `mbm_2_0_velocity_advanced__up_close` | 40.24 | +11.77 | +2.09 | +3.25 | 65 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.84 | -0.04 | -0.25 | -0.08 | 78 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.47 | -0.30 | -1.48 | -2.70 | 42 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.36 | +0.16 | +0.59 | +1.18 | 60 |
| `mbm_2_0_velocity_basic__3_range` | 42.26 | +3.68 | +7.36 | +2.11 | 56 |
| `mbm_2_0_velocity_basic__4_advance` | 7.03 | +3.57 | +0.58 | -0.93 | 67 |
| `mbm_2_0_velocity_basic__4_decline` | 2.65 | -5.82 | -0.00 | +0.29 | 47 |
| `mbm_2_0_velocity_basic__5d_range` | 6.94 | +1.08 | +3.57 | +3.28 | 60 |
| `mbm_2_0_velocity_basic__net_breadth` | 4.38 | +9.39 | +0.58 | -1.23 | 67 |
| `mbm_2_0_velocity_basic__volume` | 0.35 | -0.01 | +0.04 | +0.08 | 25 |
| `net_breadth__net_breadth` | 4.38 | +9.39 | +0.58 | -1.23 | 67 |
| `net_nh_nl__net_nh_nl` | -0.59 | -0.55 | +3.84 | +0.08 | 17 |
| `new_high_low_bearishness_bullishness__high` | 40.00 | +2.00 | +10.00 | +2.00 | 42 |
| `new_high_low_bearishness_bullishness__low` | 58.00 | +19.00 | -93.00 | +4.00 | 72 |
| `volume__volume` | 0.35 | -0.01 | +0.04 | +0.08 | 27 |

## No reading for 2026-10-16

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-12, 61.77
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-12, 38.23
- `oversold_overbought_rsi__overbought`: last 2026-10-12, 129.00
- `oversold_overbought_rsi__oversold`: last 2026-10-12, 132.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-12, 0.34
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-12, 0.64


<!-- market-read -->

## Market read

Friday answered Thursday's question, and the answer was mild repair. Thursday had 116 hard fallers and only 56 hard risers. Friday flipped that to 103 risers against 35 fallers. The count of stocks above their 200 day line rose from 910 to 936, the best reading since the 8 October break. The short trend won back everything it lost on Thursday. Turnover hit about 600 crore, the heaviest day in more than two weeks. Yet this was no thrust. A thrust has several hundred hard risers, and Friday had about a hundred. The Nifty rose about 0.7 percent, and IT carried the board with a gain of about four percent. Over the week the broad market repaired a little. Six stocks in ten still sit in long downtrends, and the staircase of lower peaks still stands.

Full brief: briefs/2026-10-16.html
