# Market breadth digest: 2026-09-04

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-09-04: **69** of 79
- History available: 2019-07-01 to 2026-09-04, 671 dated rows
- Metrics with no reading for 2026-09-04: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 46.23 | +3.37 | +0.00 | -9.05 | 59 | 375 |
| % above 20 EMA | 44.32 | +1.80 | -2.25 | -10.79 | 53 | 375 |
| % above 50 EMA | 48.09 | +1.84 | -1.53 | -7.48 | 60 | 375 |
| % above 200 EMA | 48.98 | +0.78 | -1.70 | -3.32 | 82 | 375 |
| Net breadth (4% adv minus dec) | 5.94 | -0.08 | +0.25 | +4.87 | 77 | 375 |
| 4% advancers | 8.14 | +0.43 | +0.64 | +2.44 | 79 | 375 |
| 4% decliners | 2.21 | +0.51 | +0.38 | -2.43 | 36 | 375 |
| Net new highs minus lows | 2.54 | +0.43 | +0.47 | +0.37 | 91 | 375 |
| Net within 15% of 52wk H/L | 7.29 | +0.85 | -1.31 | -3.51 | 78 | 375 |
| Volume expansion ratio | 0.47 | +0.07 | +0.16 | -0.19 | 50 | 375 |
| Overbought count (weekly RSI>70) (as of 2026-08-31) | 258.00 | +11.00 | +68.00 | +159.00 | 74 | 375 |
| Oversold count (weekly RSI<30) (as of 2026-08-31) | 78.00 | +11.00 | +30.00 | +56.00 | 78 | 375 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__current` | 584.25 | +130.57 | 81 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,014.00 | +68.00 | 52 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,254.00 | -68.00 | 63 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,162.00 | +58.00 | 61 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,106.00 | -58.00 | 49 |
| `drawdowns_peaks__blw_3` | 120.00 | +29.00 | 48 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,247.00 | +12.00 | 88 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,021.00 | -12.00 | 30 |
| `4_advance_decline__4_decline` | 52.00 | +12.00 | 30 |
| `current_previous_yr_volumes_crores__1_yr_back` | 400.85 | -11.38 | 52 |

## At the edge of their own range

Top decile of history:

- `mbm_2_0_velocity_advanced__15_52wh` at 28.24 (percentile 100, range 2.78 to 28.41)
- `52_week_high_low_within_10__high` at 28.21 (percentile 99, range 3.64 to 28.32)
- `mbm_2_0_velocity_advanced__30_52wh` at 55.00 (percentile 98, range 16.60 to 55.81)
- `mbm_2_0_velocity_advanced__new_52_wk_high` at 3.60 (percentile 96, range 0.15 to 4.75)
- `new_high_low_bearishness_bullishness__high` at 92.00 (percentile 91, range 5.00 to 148.00)
- `mbm_2_0_velocity_advanced__net_nh_nl` at 2.54 (percentile 91, range -38.70 to 4.66)
- `4_advance_decline__4_advance` at 192.00 (percentile 90, range 45.00 to 479.00)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.72 | -0.13 | +0.08 | +0.08 | 83 |
| `15_up_10_down__10_in_5d` | 1.74 | +0.17 | +0.34 | +0.04 | 58 |
| `15_up_10_down__15_in_5d` | 2.33 | +0.00 | -0.04 | -1.41 | 52 |
| `3_above_200_ema__pct` | 51.97 | +0.72 | -2.25 | -5.42 | 78 |
| `4_advance_decline__4_advance` | 192.00 | +10.00 | +15.00 | +58.00 | 90 |
| `4_advance_decline__4_decline` | 52.00 | +12.00 | +9.00 | -57.00 | 30 |
| `4_advance_decline_today__4_advance` | 192.00 | NOT FOUND | NOT FOUND | NOT FOUND | n=1 |
| `4_advance_decline_today__4_decline` | 54.00 | NOT FOUND | NOT FOUND | NOT FOUND | n=1 |
| `4_advance_decline_today__net_breadth` | 5.83 | NOT FOUND | NOT FOUND | NOT FOUND | n=1 |
| `52_week_high_low_within_10__high` | 28.21 | +0.50 | +0.61 | +0.01 | 99 |
| `52_week_high_low_within_10__low` | 17.67 | -0.34 | +1.38 | +4.67 | 50 |
| `52_wk_high_low__new_52_wk_high` | 3.10 | +0.34 | +0.20 | -0.55 | 62 |
| `52_wk_high_low__new_52_wk_low` | 1.04 | -0.10 | -0.13 | +0.05 | 63 |
| `52_wk_high_low_today__new_52_wk_high` | 3.09 | NOT FOUND | NOT FOUND | NOT FOUND | n=1 |
| `52_wk_high_low_today__new_52_wk_low` | 1.25 | NOT FOUND | NOT FOUND | NOT FOUND | n=1 |
| `5_advance_decline_ratio__advance` | 54.69 | NOT FOUND | NOT FOUND | NOT FOUND | n=1 |
| `5_advance_decline_ratio__decline` | 44.26 | NOT FOUND | NOT FOUND | NOT FOUND | n=1 |
| `above_10ma__pct` | 43.83 | +4.63 | -2.69 | -16.32 | 47 |
| `above_200ma__above_200ma` | 51.97 | +0.69 | -2.26 | -5.42 | 77 |
| `above_20_ema__pct` | 43.29 | +3.48 | -4.81 | -16.89 | 43 |
| `above_20ma__pct` | 43.29 | +3.48 | -4.81 | -16.89 | 39 |
| `above_50_ema__pct` | 48.87 | +2.68 | -4.74 | -11.81 | 41 |
| `above_50ma__above_50ma` | 51.97 | +0.69 | -2.26 | -5.42 | 77 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,247.00 | +12.00 | -51.00 | -123.00 | 88 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,014.00 | +68.00 | -90.00 | -360.00 | 52 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,162.00 | +58.00 | -89.00 | -256.00 | 61 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,021.00 | -12.00 | +51.00 | +125.00 | 30 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,254.00 | -68.00 | +90.00 | +363.00 | 63 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,106.00 | -58.00 | +89.00 | +258.00 | 49 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 5.00 | +0.00 | -1.00 | +1.00 | 84 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 25.00 | +11.00 | +5.00 | -43.00 | 40 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 26.00 | -7.00 | +7.00 | -9.00 | 79 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 129.00 | -4.00 | +4.00 | +44.00 | 81 |
| `current_previous_yr_volumes_crores__1_yr_back` | 400.85 | -11.38 | +19.55 | +74.75 | 52 |
| `current_previous_yr_volumes_crores__current` | 584.25 | +130.57 | +126.99 | +183.64 | 81 |
| `drawdowns_peaks__blw_3` | 120.00 | +29.00 | +8.00 | -62.00 | 48 |
| `gold_etfs_nifty_1_month_chg__gold` | 7.87 | +1.53 | -4.95 | +0.68 | 86 |
| `gold_etfs_nifty_1_month_chg__nifty` | 0.87 | +0.17 | +2.07 | +0.17 | 50 |
| `mbm_2_0_magnitude__abv_10ma` | 46.23 | +3.37 | +0.00 | -9.05 | 59 |
| `mbm_2_0_magnitude__abv_200ma` | 48.98 | +0.78 | -1.70 | -3.32 | 82 |
| `mbm_2_0_magnitude__abv_20ma` | 44.32 | +1.80 | -2.25 | -10.79 | 53 |
| `mbm_2_0_magnitude__abv_50ma` | 48.09 | +1.84 | -1.53 | -7.48 | 60 |
| `mbm_2_0_velocity_advanced__15_52wh` | 28.24 | +0.27 | -0.17 | +1.90 | 100 |
| `mbm_2_0_velocity_advanced__15_52wl` | 20.95 | -0.58 | +1.15 | +5.42 | 50 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 40.63 | -0.32 | +1.27 | +2.50 | 28 |
| `mbm_2_0_velocity_advanced__30_52wh` | 55.00 | +0.28 | -0.81 | +0.11 | 98 |
| `mbm_2_0_velocity_advanced__breakdowns` | 7.08 | +2.08 | +0.98 | -3.77 | 39 |
| `mbm_2_0_velocity_advanced__breakouts` | 18.45 | -1.26 | +1.27 | +3.51 | 72 |
| `mbm_2_0_velocity_advanced__down_close` | 31.14 | -2.76 | +1.28 | -11.61 | 32 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | 7.29 | +0.85 | -1.31 | -3.51 | 78 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 14.38 | +0.60 | -2.08 | -2.39 | 89 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 2.54 | +0.43 | +0.47 | +0.37 | 91 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 3.60 | +0.21 | +0.30 | +0.46 | 96 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.06 | -0.21 | -0.17 | +0.08 | 52 |
| `mbm_2_0_velocity_advanced__up_close` | 44.14 | +5.00 | +0.43 | +5.96 | 83 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.72 | -0.13 | +0.08 | +0.08 | 72 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.74 | +0.17 | +0.34 | +0.04 | 51 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.33 | +0.00 | -0.04 | -1.41 | 61 |
| `mbm_2_0_velocity_basic__3_range` | 46.06 | -0.19 | -4.20 | +0.40 | 65 |
| `mbm_2_0_velocity_basic__4_advance` | 8.14 | +0.43 | +0.64 | +2.44 | 79 |
| `mbm_2_0_velocity_basic__4_decline` | 2.21 | +0.51 | +0.38 | -2.43 | 36 |
| `mbm_2_0_velocity_basic__5d_range` | 7.38 | +0.47 | -4.96 | -2.79 | 61 |
| `mbm_2_0_velocity_basic__net_breadth` | 5.94 | -0.08 | +0.25 | +4.87 | 77 |
| `mbm_2_0_velocity_basic__volume` | 0.47 | +0.07 | +0.16 | -0.19 | 50 |
| `net_breadth__net_breadth` | 5.94 | -0.08 | +0.25 | +4.87 | 83 |
| `net_nh_nl__net_nh_nl` | 2.54 | +0.43 | +0.47 | +0.37 | 73 |
| `new_high_low_bearishness_bullishness__high` | 92.00 | +10.00 | +6.00 | -11.00 | 91 |
| `new_high_low_bearishness_bullishness__low` | 31.00 | -3.00 | -4.00 | +3.00 | 56 |
| `volume__volume` | 0.47 | +0.07 | +0.16 | -0.19 | 62 |

## No reading for 2026-09-04

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-08-31, 69.66
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-08-31, 30.34
- `oversold_overbought_rsi__overbought`: last 2026-08-31, 258.00
- `oversold_overbought_rsi__oversold`: last 2026-08-31, 78.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-08-31, 0.50
- `weekly_rsi_50_50__below_rsi_50`: last 2026-08-31, 0.43


<!-- market-read -->

## Market read

The big index has gone nowhere for three months. Small companies have gone
up a lot in the same time. Under the surface, the market has split into two
crowds. One crowd of stocks sits near its highest price of the year. That
crowd is as large as it has ever been in this data. The other crowd sits
near its lowest price of the year, and that crowd grew this month. The
middle, the ordinary stock that just drifts along, is emptying out. This
is a market for picking stocks, not for buying the index.

Full brief: briefs/2026-09-04.html
