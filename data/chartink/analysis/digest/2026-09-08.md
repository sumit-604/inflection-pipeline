# Market breadth digest: 2026-09-08

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-09-08: **69** of 79
- History available: 2019-07-01 to 2026-09-08, 673 dated rows
- Metrics with no reading for 2026-09-08: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 43.31 | +0.75 | +7.33 | -5.02 | 51 | 377 |
| % above 20 EMA | 43.56 | +0.67 | +4.19 | -6.16 | 51 | 377 |
| % above 50 EMA | 46.02 | -0.73 | +1.27 | -7.23 | 56 | 377 |
| % above 200 EMA | 48.90 | +0.08 | +0.30 | -2.53 | 81 | 377 |
| Net breadth (4% adv minus dec) | 3.64 | +0.34 | +4.03 | +1.69 | 61 | 377 |
| 4% advancers | 6.65 | -0.45 | +2.37 | +0.15 | 63 | 377 |
| 4% decliners | 3.01 | -0.80 | -1.65 | -1.54 | 56 | 377 |
| Net new highs minus lows | 2.25 | -0.17 | +1.14 | -0.05 | 88 | 377 |
| Net within 15% of 52wk H/L | 5.97 | -1.56 | +0.76 | -3.93 | 72 | 377 |
| Volume expansion ratio | 0.51 | -0.05 | +0.10 | -0.17 | 54 | 377 |
| Overbought count (weekly RSI>70) (as of 2026-09-07) | 258.00 | +0.00 | -6.00 | +161.00 | 74 | 376 |
| Oversold count (weekly RSI<30) (as of 2026-09-07) | 85.00 | +7.00 | +37.00 | +56.00 | 78 | 376 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__current` | 517.82 | -141.41 | 54 |
| `drawdowns_peaks__blw_3` | 158.00 | -40.00 | 62 |
| `breadth_above_500_trend_reversal__above_20dma` | 946.00 | +25.00 | 47 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,315.00 | -25.00 | 67 |
| `current_previous_yr_volumes_crores__1_yr_back` | 425.10 | +23.15 | 62 |
| `4_advance_decline__4_decline` | 71.00 | -19.00 | 53 |
| `4_advance_decline_today__4_decline` | 73.00 | -17.00 | n=3 |
| `new_high_low_bearishness_bullishness__low` | 38.00 | -11.00 | 63 |
| `4_advance_decline__4_advance` | 157.00 | -11.00 | 55 |
| `4_advance_decline_today__4_advance` | 157.00 | -11.00 | n=3 |

## At the edge of their own range

Top decile of history:

- `mbm_2_0_velocity_advanced__15_52wh` at 28.26 (percentile 99, range 2.78 to 28.64)
- `mbm_2_0_velocity_advanced__new_52_wk_high` at 3.73 (percentile 97, range 0.15 to 4.75)
- `52_week_high_low_within_10__high` at 27.40 (percentile 96, range 3.64 to 28.32)
- `new_high_low_bearishness_bullishness__high` at 100.00 (percentile 95, range 5.00 to 148.00)
- `mbm_2_0_velocity_advanced__30_52wh` at 54.24 (percentile 94, range 16.60 to 55.81)
- `15_up_10_down__15_in_5d` at 3.90 (percentile 94, range 0.99 to 7.11)
- `breadth_above_500_trend_reversal__up_20_in_5d` at 36.00 (percentile 90, range 1.00 to 402.00)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.59 | -0.25 | -0.34 | +0.04 | 52 |
| `15_up_10_down__10_in_5d` | 1.19 | -0.38 | -0.38 | -1.62 | 19 |
| `15_up_10_down__15_in_5d` | 3.90 | +1.06 | +1.74 | +0.75 | 94 |
| `3_above_200_ema__pct` | 51.21 | +0.09 | -0.47 | -5.30 | 75 |
| `4_advance_decline__4_advance` | 157.00 | -11.00 | +56.00 | +4.00 | 55 |
| `4_advance_decline__4_decline` | 71.00 | -19.00 | -39.00 | -36.00 | 53 |
| `4_advance_decline_today__4_advance` | 157.00 | -11.00 | NOT FOUND | NOT FOUND | n=3 |
| `4_advance_decline_today__4_decline` | 73.00 | -17.00 | NOT FOUND | NOT FOUND | n=3 |
| `4_advance_decline_today__net_breadth` | 3.55 | +0.25 | NOT FOUND | NOT FOUND | n=3 |
| `52_week_high_low_within_10__high` | 27.40 | -0.27 | +0.61 | -0.83 | 96 |
| `52_week_high_low_within_10__low` | 18.86 | +0.77 | +0.91 | +4.67 | 53 |
| `52_wk_high_low__new_52_wk_high` | 3.36 | -0.32 | +0.67 | -0.46 | 69 |
| `52_wk_high_low__new_52_wk_low` | 1.28 | -0.36 | -0.54 | +0.04 | 82 |
| `52_wk_high_low_today__new_52_wk_high` | 3.32 | -0.33 | NOT FOUND | NOT FOUND | n=3 |
| `52_wk_high_low_today__new_52_wk_low` | 1.41 | -0.30 | NOT FOUND | NOT FOUND | n=3 |
| `5_advance_decline_ratio__advance` | 45.51 | +6.65 | NOT FOUND | NOT FOUND | n=3 |
| `5_advance_decline_ratio__decline` | 53.44 | -6.65 | NOT FOUND | NOT FOUND | n=3 |
| `above_10ma__pct` | 40.32 | +1.62 | +7.03 | -12.59 | 40 |
| `above_200ma__above_200ma` | 51.18 | +0.09 | -0.47 | -5.33 | 70 |
| `above_20_ema__pct` | 40.52 | +1.09 | +3.29 | -14.50 | 38 |
| `above_20ma__pct` | 40.52 | +1.09 | +3.29 | -14.50 | 34 |
| `above_50_ema__pct` | 45.23 | +0.47 | -0.20 | -13.23 | 32 |
| `above_50ma__above_50ma` | 51.21 | +0.09 | -0.47 | -5.30 | 70 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,230.00 | -2.00 | -11.00 | -122.00 | 84 |
| `breadth_above_500_trend_reversal__above_20dma` | 946.00 | +25.00 | +74.00 | -302.00 | 47 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,058.00 | +2.00 | -12.00 | -299.00 | 54 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,031.00 | +2.00 | +11.00 | +122.00 | 36 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,315.00 | -25.00 | -74.00 | +303.00 | 67 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,203.00 | -2.00 | +12.00 | +299.00 | 62 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 5.00 | +0.00 | +1.00 | +0.00 | 85 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 36.00 | -5.00 | -16.00 | -36.00 | 58 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 36.00 | +7.00 | +9.00 | +6.00 | 90 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 112.00 | -4.00 | +35.00 | +12.00 | 73 |
| `current_previous_yr_volumes_crores__1_yr_back` | 425.10 | +23.15 | +25.00 | +54.65 | 62 |
| `current_previous_yr_volumes_crores__current` | 517.82 | -141.41 | +37.20 | +30.79 | 54 |
| `drawdowns_peaks__blw_3` | 158.00 | -40.00 | -117.00 | -33.00 | 62 |
| `gold_etfs_nifty_1_month_chg__gold` | 7.83 | +2.05 | +1.38 | -0.45 | 85 |
| `gold_etfs_nifty_1_month_chg__nifty` | -0.71 | -0.26 | -0.07 | -1.90 | 24 |
| `mbm_2_0_magnitude__abv_10ma` | 43.31 | +0.75 | +7.33 | -5.02 | 51 |
| `mbm_2_0_magnitude__abv_200ma` | 48.90 | +0.08 | +0.30 | -2.53 | 81 |
| `mbm_2_0_magnitude__abv_20ma` | 43.56 | +0.67 | +4.19 | -6.16 | 51 |
| `mbm_2_0_magnitude__abv_50ma` | 46.02 | -0.73 | +1.27 | -7.23 | 56 |
| `mbm_2_0_velocity_advanced__15_52wh` | 28.26 | -0.38 | +1.36 | +1.53 | 99 |
| `mbm_2_0_velocity_advanced__15_52wl` | 22.29 | +1.18 | +0.59 | +5.46 | 53 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 40.93 | -0.14 | +0.21 | +2.94 | 29 |
| `mbm_2_0_velocity_advanced__30_52wh` | 54.24 | -0.46 | -0.30 | -0.71 | 94 |
| `mbm_2_0_velocity_advanced__breakdowns` | 8.81 | -0.75 | -4.62 | -1.98 | 56 |
| `mbm_2_0_velocity_advanced__breakouts` | 15.00 | -2.64 | +1.82 | -0.43 | 50 |
| `mbm_2_0_velocity_advanced__down_close` | 34.13 | -5.69 | -0.57 | -7.99 | 52 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | 5.97 | -1.56 | +0.76 | -3.93 | 72 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 13.31 | -0.32 | -0.51 | -3.65 | 86 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 2.25 | -0.17 | +1.14 | -0.05 | 88 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 3.73 | -0.46 | +0.64 | +0.20 | 97 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.48 | -0.29 | -0.51 | +0.25 | 62 |
| `mbm_2_0_velocity_advanced__up_close` | 44.35 | +4.06 | +11.87 | +2.20 | 84 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.59 | -0.25 | -0.34 | +0.04 | 62 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.19 | -0.38 | -0.38 | -1.62 | 31 |
| `mbm_2_0_velocity_basic__15_in_5d` | 3.90 | +1.06 | +1.74 | +0.75 | 88 |
| `mbm_2_0_velocity_basic__3_range` | 45.76 | +4.65 | +6.95 | +0.67 | 64 |
| `mbm_2_0_velocity_basic__4_advance` | 6.65 | -0.45 | +2.37 | +0.15 | 63 |
| `mbm_2_0_velocity_basic__4_decline` | 3.01 | -0.80 | -1.65 | -1.54 | 56 |
| `mbm_2_0_velocity_basic__5d_range` | 10.55 | +1.75 | +2.50 | +0.65 | 76 |
| `mbm_2_0_velocity_basic__net_breadth` | 3.64 | +0.34 | +4.03 | +1.69 | 61 |
| `mbm_2_0_velocity_basic__volume` | 0.51 | -0.05 | +0.10 | -0.17 | 54 |
| `net_breadth__net_breadth` | 3.64 | +0.34 | +4.03 | +1.69 | 58 |
| `net_nh_nl__net_nh_nl` | 2.25 | -0.17 | +1.14 | -0.05 | 68 |
| `new_high_low_bearishness_bullishness__high` | 100.00 | -10.00 | +20.00 | -8.00 | 95 |
| `new_high_low_bearishness_bullishness__low` | 38.00 | -11.00 | -16.00 | +3.00 | 63 |
| `volume__volume` | 0.51 | -0.05 | +0.10 | -0.17 | 65 |

## No reading for 2026-09-08

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-09-07, 68.66
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-09-07, 31.34
- `oversold_overbought_rsi__overbought`: last 2026-09-07, 258.00
- `oversold_overbought_rsi__oversold`: last 2026-09-07, 85.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-09-07, 0.48
- `weekly_rsi_50_50__below_rsi_50`: last 2026-09-07, 0.46


<!-- market-read -->

## Market read

The market spread out today and the index did not notice. Nineteen of
thirty-five indices rose. The Nifty still fell about half a percent, because
the selling sat in the largest banks and lenders. Underneath, the repair that
began last week carried on. Nine hundred and forty-six stocks now sit above
their twenty-day line, up from a low of 801 six sessions ago. More stocks sit
within fifteen percent of a one-year high than at any point in this data.
Defence became the clear leader today, on the index and in its breadth at the
same time. But six in ten stocks still sit below their twenty-day line, and
the fast tail is the fullest it has been all month. This is a market healing
at its edges while its middle stays empty. The index will pay you little. The
right group will pay you a lot.

Full brief: briefs/2026-09-08.html
