# Market breadth digest: 2026-11-20

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-20: **69** of 79
- History available: 2019-07-01 to 2026-11-20, 723 dated rows
- Metrics with no reading for 2026-11-20: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 35.50 | -4.80 | -31.86 | +28.38 | 37 | 427 |
| % above 20 EMA | 38.67 | -3.74 | -25.56 | +30.77 | 43 | 427 |
| % above 50 EMA | 34.87 | -2.96 | -13.23 | +23.74 | 41 | 427 |
| % above 200 EMA | 36.32 | -1.04 | -4.68 | +11.51 | 42 | 427 |
| Net breadth (4% adv minus dec) | -1.88 | -4.22 | -3.13 | +22.81 | 20 | 427 |
| 4% advancers | 3.17 | -1.88 | -2.30 | +0.89 | 16 | 427 |
| 4% decliners | 5.05 | +2.35 | +0.83 | -21.92 | 77 | 427 |
| Net new highs minus lows | -0.47 | -0.12 | -2.23 | +15.73 | 35 | 427 |
| Net within 15% of 52wk H/L | -8.88 | -1.41 | -6.81 | +22.14 | 41 | 427 |
| Volume expansion ratio | 0.40 | +0.06 | -0.07 | -0.75 | 39 | 427 |
| Overbought count (weekly RSI>70) (as of 2026-11-16) | 123.00 | +28.00 | -7.00 | -112.00 | 45 | 386 |
| Oversold count (weekly RSI<30) (as of 2026-11-16) | 112.00 | +50.00 | -15.00 | +88.00 | 83 | 386 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 339.00 | +201.00 | 86 |
| `current_previous_yr_volumes_crores__current` | 567.61 | +103.47 | 76 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,060.00 | -64.00 | 60 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,285.00 | +63.00 | 61 |
| `4_advance_decline__4_decline` | 129.00 | +60.00 | 79 |
| `4_advance_decline_today__4_decline` | 136.00 | +60.00 | 69 |
| `current_previous_yr_volumes_crores__1_yr_back` | 572.64 | +54.35 | 95 |
| `breadth_above_500_trend_reversal__above_50dma` | 989.00 | -48.00 | 53 |
| `4_advance_decline__4_advance` | 81.00 | -48.00 | 13 |
| `4_advance_decline_today__4_advance` | 83.00 | -48.00 | 19 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 17.31 (percentile 100, range -6.93 to 17.31)
- `current_previous_yr_volumes_crores__1_yr_back` at 572.64 (percentile 95, range 118.99 to 716.05)
- `15_up_10_down__10_in_5d` at 6.11 (percentile 95, range 0.34 to 27.85)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 6.00 (percentile 92, range 0.00 to 33.00)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__gold` at -15.85 (percentile 1, range -15.85 to 14.14)
- `15_up_10_down__15_in_5d` at 0.70 (percentile 3, range 0.63 to 7.11)
- `mbm_2_0_velocity_basic__15_in_5d` at 0.70 (percentile 5, range 0.23 to 42.64)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed down through 50: 76.00 to 48.00
- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 36.00 to 81.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.55 | +0.04 | +0.35 | -6.57 | 51 |
| `15_up_10_down__10_in_5d` | 6.11 | +0.51 | +5.48 | -21.18 | 95 |
| `15_up_10_down__15_in_5d` | 0.70 | -0.27 | -1.91 | -0.12 | 3 |
| `3_above_200_ema__pct` | 41.91 | -0.83 | -4.35 | +19.34 | 46 |
| `4_advance_decline__4_advance` | 81.00 | -48.00 | -58.00 | +23.00 | 13 |
| `4_advance_decline__4_decline` | 129.00 | +60.00 | +21.00 | -556.00 | 79 |
| `4_advance_decline_today__4_advance` | 83.00 | -48.00 | -60.00 | +22.00 | 19 |
| `4_advance_decline_today__4_decline` | 136.00 | +60.00 | +22.00 | -108.00 | 69 |
| `4_advance_decline_today__net_breadth` | -2.06 | -4.19 | -3.18 | +5.61 | 31 |
| `52_week_high_low_within_10__high` | 20.25 | -0.17 | -1.06 | +14.60 | 62 |
| `52_week_high_low_within_10__low` | 22.08 | +1.17 | +7.16 | -15.77 | 61 |
| `52_wk_high_low__new_52_wk_high` | 2.19 | +0.92 | -0.03 | +1.89 | 50 |
| `52_wk_high_low__new_52_wk_low` | 2.22 | +0.95 | +1.77 | -12.60 | 79 |
| `52_wk_high_low_today__new_52_wk_high` | 2.17 | +0.89 | -0.03 | +1.85 | 77 |
| `52_wk_high_low_today__new_52_wk_low` | 2.36 | +0.92 | +1.75 | -7.69 | 52 |
| `5_advance_decline_ratio__advance` | 39.43 | -17.83 | +3.67 | +11.86 | 42 |
| `5_advance_decline_ratio__decline` | 59.55 | +17.83 | -3.63 | -11.84 | 60 |
| `above_10ma__pct` | 41.06 | -4.94 | -28.37 | +33.38 | 47 |
| `above_200ma__above_200ma` | 41.91 | -0.83 | -4.35 | +19.34 | 48 |
| `above_20_ema__pct` | 44.59 | -3.50 | -22.79 | +36.27 | 50 |
| `above_20ma__pct` | 44.59 | -3.50 | -22.79 | +36.27 | 51 |
| `above_50_ema__pct` | 41.65 | -2.49 | -11.69 | +30.94 | 41 |
| `above_50ma__above_50ma` | 41.91 | -0.83 | -4.34 | +19.33 | 48 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,026.00 | -20.00 | -111.00 | +419.00 | 64 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,060.00 | -64.00 | -538.00 | +871.00 | 60 |
| `breadth_above_500_trend_reversal__above_50dma` | 989.00 | -48.00 | -280.00 | +719.00 | 53 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,320.00 | +19.00 | +108.00 | -427.00 | 69 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,285.00 | +63.00 | +534.00 | -880.00 | 61 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,357.00 | +47.00 | +277.00 | -727.00 | 71 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 6.00 | +1.00 | +4.00 | -25.00 | 92 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 81.00 | +45.00 | +20.00 | -309.00 | 84 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 5.00 | +0.00 | -9.00 | -2.00 | 11 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 48.00 | -28.00 | -26.00 | +22.00 | 22 |
| `current_previous_yr_volumes_crores__1_yr_back` | 572.64 | +54.35 | +123.93 | +140.28 | 95 |
| `current_previous_yr_volumes_crores__current` | 567.61 | +103.47 | +120.93 | -79.03 | 76 |
| `drawdowns_peaks__blw_3` | 339.00 | +201.00 | +104.00 | -828.00 | 86 |
| `gold_etfs_nifty_1_month_chg__gold` | -15.85 | -3.73 | -7.95 | -7.88 | 1 |
| `gold_etfs_nifty_1_month_chg__nifty` | 17.31 | +3.60 | +5.87 | +21.69 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 35.50 | -4.80 | -31.86 | +28.38 | 37 |
| `mbm_2_0_magnitude__abv_200ma` | 36.32 | -1.04 | -4.68 | +11.51 | 42 |
| `mbm_2_0_magnitude__abv_20ma` | 38.67 | -3.74 | -25.56 | +30.77 | 43 |
| `mbm_2_0_magnitude__abv_50ma` | 34.87 | -2.96 | -13.23 | +23.74 | 41 |
| `mbm_2_0_velocity_advanced__15_52wh` | 17.06 | -0.42 | -1.01 | +10.06 | 52 |
| `mbm_2_0_velocity_advanced__15_52wl` | 25.95 | +0.99 | +5.80 | -12.08 | 61 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 47.12 | +0.29 | +2.26 | -6.75 | 49 |
| `mbm_2_0_velocity_advanced__30_52wh` | 45.36 | -1.16 | -3.45 | +8.08 | 51 |
| `mbm_2_0_velocity_advanced__breakdowns` | 15.26 | +6.23 | +2.26 | -53.20 | 79 |
| `mbm_2_0_velocity_advanced__breakouts` | 10.06 | -4.77 | -4.58 | +0.66 | 15 |
| `mbm_2_0_velocity_advanced__down_close` | 33.08 | +3.21 | +0.64 | -6.27 | 45 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -8.88 | -1.41 | -6.81 | +22.14 | 41 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -1.76 | -1.45 | -5.71 | +14.83 | 49 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.47 | -0.12 | -2.23 | +15.73 | 35 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.45 | +0.31 | -0.82 | +1.17 | 44 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.92 | +0.43 | +1.41 | -14.56 | 65 |
| `mbm_2_0_velocity_advanced__up_close` | 31.52 | -2.52 | -5.55 | +7.25 | 27 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.55 | +0.04 | +0.35 | -6.57 | 57 |
| `mbm_2_0_velocity_basic__10_in_5d` | 6.10 | +0.51 | +5.48 | -21.22 | 89 |
| `mbm_2_0_velocity_basic__15_in_5d` | 0.70 | -0.27 | -1.95 | -0.12 | 5 |
| `mbm_2_0_velocity_basic__3_range` | 41.51 | -0.77 | +0.92 | +33.02 | 56 |
| `mbm_2_0_velocity_basic__4_advance` | 3.17 | -1.88 | -2.30 | +0.89 | 16 |
| `mbm_2_0_velocity_basic__4_decline` | 5.05 | +2.35 | +0.83 | -21.92 | 77 |
| `mbm_2_0_velocity_basic__5d_range` | 5.28 | -0.43 | -0.26 | +4.53 | 52 |
| `mbm_2_0_velocity_basic__net_breadth` | -1.88 | -4.22 | -3.13 | +22.81 | 20 |
| `mbm_2_0_velocity_basic__volume` | 0.40 | +0.06 | -0.07 | -0.75 | 39 |
| `net_breadth__net_breadth` | -1.88 | -4.22 | -3.13 | +22.81 | 18 |
| `net_nh_nl__net_nh_nl` | -0.47 | -0.12 | -2.23 | +15.73 | 24 |
| `new_high_low_bearishness_bullishness__high` | 67.00 | +28.00 | -1.00 | +58.00 | 76 |
| `new_high_low_bearishness_bullishness__low` | 68.00 | +29.00 | +54.00 | -383.00 | 75 |
| `volume__volume` | 0.40 | +0.06 | -0.07 | -0.75 | 44 |

## No reading for 2026-11-20

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-16, 65.19
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-16, 34.81
- `oversold_overbought_rsi__overbought`: last 2026-11-16, 123.00
- `oversold_overbought_rsi__oversold`: last 2026-11-16, 112.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-16, 0.38
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-16, 0.54


<!-- market-read -->

## Market read

The index and the average stock walked in opposite directions this week. The Nifty closed Friday near 25,800, up about two and a half percent on the week and about one percent on the day. Banks did most of that lifting. Under the index, the short trend count lost about 540 stocks over the week, and Friday added more losers than gainers. About six stocks in ten closed lower on a day the Nifty rose. The short, middle and long trend counts all sit below half the market and all slipped again on Friday. New yearly highs and new yearly lows finished level, and the share of stocks down ten percent in a week rose for a fifth straight session. Fear rose with the index. So the bounce off the October low still stands, but it now rests on a few large shoulders. The coming sessions turn on one question: do the members follow the banks up, or do the banks tire and follow the members down?

Full brief: briefs/2026-11-20.html
