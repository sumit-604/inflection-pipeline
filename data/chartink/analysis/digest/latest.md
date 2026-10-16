# Market breadth digest: 2026-10-14

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-14: **69** of 79
- History available: 2019-07-01 to 2026-10-14, 697 dated rows
- Metrics with no reading for 2026-10-14: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 46.49 | +9.68 | +8.08 | +27.60 | 62 | 401 |
| % above 20 EMA | 35.93 | +5.72 | +2.40 | +12.77 | 37 | 401 |
| % above 50 EMA | 33.53 | +3.41 | -1.43 | +0.87 | 36 | 401 |
| % above 200 EMA | 39.04 | +0.63 | -2.23 | -2.79 | 48 | 401 |
| Net breadth (4% adv minus dec) | 7.40 | +4.33 | +3.83 | +28.01 | 84 | 401 |
| 4% advancers | 8.79 | +2.61 | +2.61 | +5.95 | 82 | 401 |
| 4% decliners | 1.39 | -1.72 | -1.22 | -22.06 | 13 | 401 |
| Net new highs minus lows | 0.55 | +2.65 | +1.14 | +2.60 | 48 | 401 |
| Net within 15% of 52wk H/L | -9.13 | +1.60 | -1.39 | -3.81 | 39 | 401 |
| Volume expansion ratio | 0.39 | +0.09 | +0.05 | -0.21 | 36 | 401 |
| Overbought count (weekly RSI>70) (as of 2026-10-12) | 149.00 | +15.00 | -98.00 | -14.00 | 55 | 381 |
| Oversold count (weekly RSI<30) (as of 2026-10-12) | 131.00 | -76.00 | +42.00 | +97.00 | 85 | 381 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `breadth_above_500_trend_reversal__above_20dma` | 799.00 | +128.00 | 36 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,463.00 | -126.00 | 77 |
| `new_high_low_bearishness_bullishness__low` | 28.00 | -70.00 | 49 |
| `breadth_above_500_trend_reversal__above_50dma` | 733.00 | +66.00 | 29 |
| `drawdowns_peaks__blw_3` | 85.00 | -64.00 | 26 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,529.00 | -64.00 | 84 |
| `4_advance_decline_today__4_advance` | 212.00 | +63.00 | 91 |
| `4_advance_decline__4_advance` | 209.00 | +62.00 | 91 |
| `current_previous_yr_volumes_crores__current` | 464.92 | +49.88 | 32 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 145.00 | +44.00 | 86 |

## At the edge of their own range

Top decile of history:

- `breadth_above_500_trend_reversal__down_20_in_5d` at 6.00 (percentile 93, range 0.00 to 34.00)
- `4_advance_decline_today__4_advance` at 212.00 (percentile 91, range 45.00 to 296.00)
- `4_advance_decline_today__net_breadth` at 7.32 (percentile 91, range -20.57 to 10.36)
- `4_advance_decline__4_advance` at 209.00 (percentile 91, range 43.00 to 479.00)
- `net_breadth__net_breadth` at 7.40 (percentile 91, range -20.60 to 19.72)

Bottom decile of history:

- `4_advance_decline__4_decline` at 33.00 (percentile 6, range 22.00 to 560.00)
- `breadth_above_500_trend_reversal__down_4_5_today` at 10.00 (percentile 8, range 1.00 to 966.00)
- `4_advance_decline_today__4_decline` at 37.00 (percentile 9, range 36.00 to 561.00)
- `52_wk_high_low_today__new_52_wk_low` at 1.11 (percentile 9, range 0.85 to 7.16)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.72 | -0.34 | -0.04 | -0.29 | 81 |
| `15_up_10_down__10_in_5d` | 2.36 | -0.42 | -0.13 | -3.76 | 62 |
| `15_up_10_down__15_in_5d` | 1.72 | +0.46 | -0.84 | +0.18 | 30 |
| `3_above_200_ema__pct` | 36.22 | +0.12 | -2.47 | -5.65 | 30 |
| `4_advance_decline__4_advance` | 209.00 | +62.00 | +62.00 | +141.00 | 91 |
| `4_advance_decline__4_decline` | 33.00 | -41.00 | -29.00 | -527.00 | 6 |
| `4_advance_decline_today__4_advance` | 212.00 | +63.00 | +62.00 | +55.00 | 91 |
| `4_advance_decline_today__4_decline` | 37.00 | -41.00 | -29.00 | -36.00 | 9 |
| `4_advance_decline_today__net_breadth` | 7.32 | +4.35 | +3.81 | +3.77 | 91 |
| `52_week_high_low_within_10__high` | 18.84 | +0.64 | -1.50 | -1.41 | 43 |
| `52_week_high_low_within_10__low` | 28.09 | -1.08 | -0.90 | +4.66 | 71 |
| `52_wk_high_low__new_52_wk_high` | 1.40 | -0.03 | -0.73 | -0.49 | 10 |
| `52_wk_high_low__new_52_wk_low` | 0.98 | -2.45 | -1.82 | -2.70 | 47 |
| `52_wk_high_low_today__new_52_wk_high` | 1.33 | -0.07 | -0.72 | -1.99 | 13 |
| `52_wk_high_low_today__new_52_wk_low` | 1.11 | -2.28 | -1.66 | -0.31 | 9 |
| `5_advance_decline_ratio__advance` | 56.51 | -4.36 | +16.15 | +11.00 | 83 |
| `5_advance_decline_ratio__decline` | 42.45 | +4.36 | -16.15 | -10.99 | 22 |
| `above_10ma__pct` | 45.64 | +7.23 | +10.31 | +28.01 | 58 |
| `above_200ma__above_200ma` | 36.22 | +0.12 | -2.47 | -5.65 | 30 |
| `above_20_ema__pct` | 33.31 | +4.84 | +3.16 | +12.26 | 30 |
| `above_20ma__pct` | 33.31 | +4.84 | +3.16 | +12.26 | 29 |
| `above_50_ema__pct` | 29.70 | +2.60 | -1.07 | +0.37 | 22 |
| `above_50ma__above_50ma` | 36.22 | +0.12 | -2.47 | -5.65 | 30 |
| `breadth_above_500_trend_reversal__above_200dma` | 919.00 | +16.00 | -46.00 | -118.00 | 45 |
| `breadth_above_500_trend_reversal__above_20dma` | 799.00 | +128.00 | +78.00 | +323.00 | 36 |
| `breadth_above_500_trend_reversal__above_50dma` | 733.00 | +66.00 | -26.00 | +30.00 | 29 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,343.00 | -14.00 | +47.00 | +117.00 | 75 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,463.00 | -126.00 | -77.00 | -324.00 | 77 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,529.00 | -64.00 | +27.00 | -31.00 | 84 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 6.00 | +0.00 | -2.00 | -1.00 | 93 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 10.00 | -19.00 | -22.00 | -338.00 | 8 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 16.00 | +3.00 | -11.00 | +1.00 | 54 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 145.00 | +44.00 | +48.00 | +103.00 | 86 |
| `current_previous_yr_volumes_crores__1_yr_back` | 460.28 | +15.97 | +22.41 | +61.51 | 75 |
| `current_previous_yr_volumes_crores__current` | 464.92 | +49.88 | +53.00 | -0.30 | 32 |
| `drawdowns_peaks__blw_3` | 85.00 | -64.00 | -41.00 | -912.00 | 26 |
| `gold_etfs_nifty_1_month_chg__gold` | -5.87 | +1.53 | +3.08 | -11.23 | 27 |
| `gold_etfs_nifty_1_month_chg__nifty` | -5.36 | -0.60 | +0.12 | +0.09 | 10 |
| `mbm_2_0_magnitude__abv_10ma` | 46.49 | +9.68 | +8.08 | +27.60 | 62 |
| `mbm_2_0_magnitude__abv_200ma` | 39.04 | +0.63 | -2.23 | -2.79 | 48 |
| `mbm_2_0_magnitude__abv_20ma` | 35.93 | +5.72 | +2.40 | +12.77 | 37 |
| `mbm_2_0_magnitude__abv_50ma` | 33.53 | +3.41 | -1.43 | +0.87 | 36 |
| `mbm_2_0_velocity_advanced__15_52wh` | 20.49 | +0.80 | -1.77 | -0.79 | 77 |
| `mbm_2_0_velocity_advanced__15_52wl` | 29.62 | -0.80 | -0.38 | +3.03 | 67 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 47.58 | -0.72 | +1.14 | +2.35 | 50 |
| `mbm_2_0_velocity_advanced__30_52wh` | 51.70 | +1.09 | +0.38 | +0.53 | 85 |
| `mbm_2_0_velocity_advanced__breakdowns` | 5.72 | -6.90 | -1.72 | -30.88 | 20 |
| `mbm_2_0_velocity_advanced__breakouts` | 21.12 | +6.77 | +6.06 | +6.84 | 80 |
| `mbm_2_0_velocity_advanced__down_close` | 24.26 | -0.40 | -10.76 | -39.81 | 11 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -9.13 | +1.60 | -1.39 | -3.81 | 39 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 4.12 | +1.81 | -0.76 | -1.82 | 65 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 0.55 | +2.65 | +1.14 | +2.60 | 48 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.56 | +0.00 | -0.84 | -0.70 | 49 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.01 | -2.65 | -1.98 | -3.30 | 47 |
| `mbm_2_0_velocity_advanced__up_close` | 41.63 | -1.48 | +0.57 | +21.69 | 72 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.72 | -0.34 | -0.04 | -0.29 | 72 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.36 | -0.42 | -0.13 | -3.76 | 59 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.72 | +0.46 | -0.84 | +0.18 | 42 |
| `mbm_2_0_velocity_basic__3_range` | 42.66 | +4.42 | -1.05 | +25.41 | 56 |
| `mbm_2_0_velocity_basic__4_advance` | 8.79 | +2.61 | +2.61 | +5.95 | 82 |
| `mbm_2_0_velocity_basic__4_decline` | 1.39 | -1.72 | -1.22 | -22.06 | 13 |
| `mbm_2_0_velocity_basic__5d_range` | 4.75 | +0.80 | +1.89 | +0.23 | 47 |
| `mbm_2_0_velocity_basic__net_breadth` | 7.40 | +4.33 | +3.83 | +28.01 | 84 |
| `mbm_2_0_velocity_basic__volume` | 0.39 | +0.09 | +0.05 | -0.21 | 36 |
| `net_breadth__net_breadth` | 7.40 | +4.33 | +3.83 | +28.01 | 91 |
| `net_nh_nl__net_nh_nl` | 0.55 | +2.65 | +1.14 | +2.60 | 27 |
| `new_high_low_bearishness_bullishness__high` | 40.00 | -1.00 | -21.00 | -17.00 | 42 |
| `new_high_low_bearishness_bullishness__low` | 28.00 | -70.00 | -52.00 | -83.00 | 49 |
| `volume__volume` | 0.39 | +0.09 | +0.05 | -0.21 | 38 |

## No reading for 2026-10-14

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-12, 62.78
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-12, 37.22
- `oversold_overbought_rsi__overbought`: last 2026-10-12, 149.00
- `oversold_overbought_rsi__oversold`: last 2026-10-12, 131.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-12, 0.35
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-12, 0.63


<!-- market-read -->

## Market read

Wednesday 14 October is still the latest day on file, because the Thursday
download did not arrive. It was the fourth repair day after the 8 October
break, and the cleanest. The Nifty slipped about half a percent, yet most
stocks rose. 145 stocks jumped four and a half percent or more, and only 10
fell that much, the fewest since July. New yearly lows dropped to 28. The
count of stocks above the 200 day average reached 919, about two thirds of the
way back to its level before the break. That is almost exactly the pace of the
September repair. That repair got all the way back, peaked on 23 September
with a day very like this one, and then rolled over the next session. So the
market underneath is healing, the index lags, the VIX is rising, and the last
two repairs failed at the moment they looked best.

Full brief: briefs/2026-10-14.html
