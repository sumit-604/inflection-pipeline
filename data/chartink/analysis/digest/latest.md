# Market breadth digest: 2026-10-07

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-07: **69** of 79
- History available: 2019-07-01 to 2026-10-07, 692 dated rows
- Metrics with no reading for 2026-10-07: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 38.39 | -0.07 | +10.90 | -4.36 | 40 | 396 |
| % above 20 EMA | 33.52 | +0.81 | +4.60 | -9.65 | 34 | 396 |
| % above 50 EMA | 34.95 | +0.60 | +1.19 | -12.04 | 40 | 396 |
| % above 200 EMA | 41.25 | -0.23 | -0.23 | -7.95 | 55 | 396 |
| Net breadth (4% adv minus dec) | 3.57 | -6.93 | +2.27 | +0.22 | 60 | 396 |
| 4% advancers | 6.18 | -6.13 | +0.46 | -1.07 | 59 | 396 |
| 4% decliners | 2.61 | +0.80 | -1.81 | -1.29 | 45 | 396 |
| Net new highs minus lows | -0.59 | -0.71 | +4.16 | -3.19 | 33 | 396 |
| Net within 15% of 52wk H/L | -7.78 | +0.16 | -2.95 | -15.78 | 41 | 396 |
| Volume expansion ratio | 0.35 | -0.02 | -0.41 | -0.20 | 24 | 396 |
| Overbought count (weekly RSI>70) (as of 2026-10-05) | 167.00 | +18.00 | -91.00 | +23.00 | 61 | 380 |
| Oversold count (weekly RSI<30) (as of 2026-10-05) | 152.00 | -3.00 | +82.00 | +124.00 | 86 | 380 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `4_advance_decline__4_advance` | 147.00 | -146.00 | 51 |
| `4_advance_decline_today__4_advance` | 150.00 | -146.00 | n=18 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 96.00 | -106.00 | 63 |
| `current_previous_yr_volumes_crores__1_yr_back` | 437.87 | -52.91 | 62 |
| `drawdowns_peaks__blw_3` | 126.00 | +48.00 | 50 |
| `5_advance_decline_ratio__decline` | 58.59 | +29.85 | n=18 |
| `5_advance_decline_ratio__advance` | 40.36 | -29.85 | n=18 |
| `new_high_low_bearishness_bullishness__low` | 80.00 | +23.00 | 79 |
| `current_previous_yr_volumes_crores__current` | 411.92 | +21.11 | 7 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,538.00 | -19.00 | 83 |

## At the edge of their own range

Top decile of history:

- `breadth_above_500_trend_reversal__down_20_in_5d` at 8.00 (percentile 96, range 0.00 to 35.00)
- `52_wk_high_low__new_52_wk_low` at 2.80 (percentile 90, range 0.18 to 7.50)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at -5.48 (percentile 6, range -6.72 to 6.35)
- `current_previous_yr_volumes_crores__current` at 411.92 (percentile 7, range 378.80 to 956.94)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.76 | -0.13 | +0.13 | +0.04 | 89 |
| `15_up_10_down__10_in_5d` | 2.48 | +0.04 | -0.80 | +1.01 | 70 |
| `15_up_10_down__15_in_5d` | 2.57 | +0.09 | +0.55 | -0.37 | 57 |
| `3_above_200_ema__pct` | 38.69 | -0.45 | -0.18 | -12.70 | 35 |
| `4_advance_decline__4_advance` | 147.00 | -146.00 | +11.00 | -26.00 | 51 |
| `4_advance_decline__4_decline` | 62.00 | +19.00 | -43.00 | -31.00 | 44 |
| `4_advance_decline_today__4_advance` | 150.00 | -146.00 | +75.00 | NOT FOUND | n=18 |
| `4_advance_decline_today__4_decline` | 66.00 | +18.00 | -159.00 | NOT FOUND | n=18 |
| `4_advance_decline_today__net_breadth` | 3.51 | -6.85 | +9.78 | NOT FOUND | n=18 |
| `52_week_high_low_within_10__high` | 20.34 | -0.05 | -0.90 | -7.24 | 61 |
| `52_week_high_low_within_10__low` | 28.99 | +0.59 | +2.29 | +11.35 | 73 |
| `52_wk_high_low__new_52_wk_high` | 2.14 | +0.18 | +0.74 | -1.61 | 28 |
| `52_wk_high_low__new_52_wk_low` | 2.80 | +0.81 | -2.97 | +1.28 | 90 |
| `52_wk_high_low_today__new_52_wk_high` | 2.05 | +0.16 | +0.00 | NOT FOUND | n=18 |
| `52_wk_high_low_today__new_52_wk_low` | 2.77 | +0.75 | -0.81 | NOT FOUND | n=18 |
| `5_advance_decline_ratio__advance` | 40.36 | -29.85 | +19.79 | NOT FOUND | n=18 |
| `5_advance_decline_ratio__decline` | 58.59 | +29.85 | -19.79 | NOT FOUND | n=18 |
| `above_10ma__pct` | 35.33 | -0.45 | +11.01 | -3.50 | 32 |
| `above_200ma__above_200ma` | 38.69 | -0.45 | -0.18 | -12.70 | 33 |
| `above_20_ema__pct` | 30.15 | +1.12 | +4.64 | -9.51 | 24 |
| `above_20ma__pct` | 30.15 | +1.12 | +4.64 | -9.51 | 21 |
| `above_50_ema__pct` | 30.78 | +0.77 | +1.11 | -14.22 | 22 |
| `above_50ma__above_50ma` | 38.69 | -0.45 | -0.18 | -12.70 | 33 |
| `breadth_above_500_trend_reversal__above_200dma` | 964.00 | -13.00 | -9.00 | -290.00 | 49 |
| `breadth_above_500_trend_reversal__above_20dma` | 722.00 | +18.00 | +109.00 | -214.00 | 29 |
| `breadth_above_500_trend_reversal__above_50dma` | 757.00 | +7.00 | +22.00 | -319.00 | 32 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,296.00 | +12.00 | +9.00 | +286.00 | 70 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,538.00 | -19.00 | -109.00 | +210.00 | 83 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,503.00 | -8.00 | -22.00 | +315.00 | 83 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 8.00 | +3.00 | +3.00 | +7.00 | 96 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 31.00 | +8.00 | -16.00 | -8.00 | 50 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 26.00 | +5.00 | +9.00 | -4.00 | 78 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 96.00 | -106.00 | +7.00 | -24.00 | 63 |
| `current_previous_yr_volumes_crores__1_yr_back` | 437.87 | -52.91 | +2.55 | +33.64 | 62 |
| `current_previous_yr_volumes_crores__current` | 411.92 | +21.11 | -191.10 | -269.30 | 7 |
| `drawdowns_peaks__blw_3` | 126.00 | +48.00 | -104.00 | -77.00 | 50 |
| `gold_etfs_nifty_1_month_chg__gold` | -8.95 | -1.52 | -4.51 | -14.74 | 14 |
| `gold_etfs_nifty_1_month_chg__nifty` | -5.48 | -0.16 | +0.57 | -5.03 | 6 |
| `mbm_2_0_magnitude__abv_10ma` | 38.39 | -0.07 | +10.90 | -4.36 | 40 |
| `mbm_2_0_magnitude__abv_200ma` | 41.25 | -0.23 | -0.23 | -7.95 | 55 |
| `mbm_2_0_magnitude__abv_20ma` | 33.52 | +0.81 | +4.60 | -9.65 | 34 |
| `mbm_2_0_magnitude__abv_50ma` | 34.95 | +0.60 | +1.19 | -12.04 | 40 |
| `mbm_2_0_velocity_advanced__15_52wh` | 22.25 | +0.68 | -0.37 | -6.38 | 83 |
| `mbm_2_0_velocity_advanced__15_52wl` | 30.03 | +0.52 | +2.58 | +9.40 | 68 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 46.47 | +0.40 | +1.07 | +5.94 | 47 |
| `mbm_2_0_velocity_advanced__30_52wh` | 51.30 | -0.19 | +0.11 | -3.22 | 84 |
| `mbm_2_0_velocity_advanced__breakdowns` | 7.49 | +1.56 | -7.61 | -2.28 | 44 |
| `mbm_2_0_velocity_advanced__breakouts` | 15.05 | -10.67 | +0.26 | -2.84 | 51 |
| `mbm_2_0_velocity_advanced__down_close` | 34.83 | +4.33 | +5.58 | -5.08 | 54 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -7.78 | +0.16 | -2.95 | -15.78 | 41 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 4.84 | -0.59 | -0.96 | -9.16 | 66 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.59 | -0.71 | +4.16 | -3.19 | 33 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 2.40 | +0.17 | +0.88 | -1.88 | 77 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 2.99 | +0.88 | -3.28 | +1.31 | 77 |
| `mbm_2_0_velocity_advanced__up_close` | 41.06 | -6.81 | +2.43 | +0.55 | 68 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.76 | -0.13 | +0.13 | +0.04 | 75 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.48 | +0.04 | -0.80 | +1.01 | 62 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.57 | +0.09 | +0.55 | -0.37 | 65 |
| `mbm_2_0_velocity_basic__3_range` | 43.69 | +3.51 | +13.30 | +2.79 | 59 |
| `mbm_2_0_velocity_basic__4_advance` | 6.18 | -6.13 | +0.46 | -1.07 | 59 |
| `mbm_2_0_velocity_basic__4_decline` | 2.61 | +0.80 | -1.81 | -1.29 | 45 |
| `mbm_2_0_velocity_basic__5d_range` | 2.86 | +0.42 | +0.34 | -5.86 | 30 |
| `mbm_2_0_velocity_basic__net_breadth` | 3.57 | -6.93 | +2.27 | +0.22 | 60 |
| `mbm_2_0_velocity_basic__volume` | 0.35 | -0.02 | -0.41 | -0.20 | 24 |
| `net_breadth__net_breadth` | 3.57 | -6.93 | +2.27 | +0.22 | 58 |
| `net_nh_nl__net_nh_nl` | -0.59 | -0.71 | +4.16 | -3.19 | 14 |
| `new_high_low_bearishness_bullishness__high` | 61.00 | +5.00 | +21.00 | -52.00 | 70 |
| `new_high_low_bearishness_bullishness__low` | 80.00 | +23.00 | -85.00 | +34.00 | 79 |
| `volume__volume` | 0.35 | -0.02 | -0.41 | -0.20 | 23 |

## No reading for 2026-10-07

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-05, 61.28
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-05, 38.72
- `oversold_overbought_rsi__overbought`: last 2026-10-05, 167.00
- `oversold_overbought_rsi__oversold`: last 2026-10-05, 152.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-05, 0.37
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-05, 0.61


<!-- market-read -->

## Market read

The market is trying to heal after a bad September, and on Wednesday it
paused. The big names fell. The Nifty lost about three quarters of a percent,
and only 7 of 35 indices closed higher. Most stocks slipped a little too.
Yet among the stocks that moved hard, the risers won by three to one. The
short repair held. 757 stocks sit above their fifty-day average, well clear
of the washout level near 700. The long repair stalled. 964 stocks sit above
their two-hundred-day average, a hair under the shelf near 970. That is only
about four stocks in ten. New yearly lows still beat new highs, 80 to 61. The
small companies hold their uptrend and the large ones sit below theirs. Fear
is low. The picture is a market that has stopped falling but has not yet
proved it is rising. It needs one wide, heavy buying day to prove it.

Full brief: briefs/2026-10-07.html
