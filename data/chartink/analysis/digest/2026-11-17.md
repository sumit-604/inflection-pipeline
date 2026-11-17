# Market breadth digest: 2026-11-17

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-17: **69** of 79
- History available: 2019-07-01 to 2026-11-17, 720 dated rows
- Metrics with no reading for 2026-11-17: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 46.14 | -0.95 | -22.19 | +19.91 | 61 | 424 |
| % above 20 EMA | 48.83 | -0.90 | -10.34 | +24.96 | 67 | 424 |
| % above 50 EMA | 40.76 | +0.17 | +0.51 | +14.61 | 51 | 424 |
| % above 200 EMA | 38.03 | +0.39 | +0.47 | +1.65 | 46 | 424 |
| Net breadth (4% adv minus dec) | 1.13 | +10.31 | +0.82 | +9.39 | 35 | 424 |
| 4% advancers | 5.11 | +1.03 | +0.31 | +1.92 | 44 | 424 |
| 4% decliners | 3.98 | -9.28 | -0.51 | -7.46 | 68 | 424 |
| Net new highs minus lows | 1.40 | +0.55 | +0.47 | +3.68 | 71 | 424 |
| Net within 15% of 52wk H/L | -6.55 | -0.02 | +0.78 | +8.00 | 46 | 424 |
| Volume expansion ratio | 0.41 | -0.12 | +0.12 | +0.13 | 40 | 424 |
| Overbought count (weekly RSI>70) (as of 2026-11-16) | 97.00 | +2.00 | -33.00 | -138.00 | 35 | 386 |
| Oversold count (weekly RSI<30) (as of 2026-11-16) | 79.00 | +17.00 | -48.00 | +55.00 | 76 | 386 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 197.00 | -390.00 | 70 |
| `4_advance_decline__4_decline` | 102.00 | -239.00 | 63 |
| `4_advance_decline_today__4_decline` | 107.00 | -236.00 | 60 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 46.00 | -169.00 | 68 |
| `current_previous_yr_volumes_crores__1_yr_back` | 522.61 | +152.93 | 89 |
| `4_advance_decline_today__4_advance` | 134.00 | +29.00 | 36 |
| `4_advance_decline__4_advance` | 131.00 | +26.00 | 35 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,253.00 | -22.00 | 74 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,086.00 | +21.00 | 46 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,103.00 | +20.00 | 62 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 13.18 (percentile 100, range -6.93 to 13.18)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 215.00 to 46.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.58 | -0.11 | -0.08 | -0.63 | 59 |
| `15_up_10_down__10_in_5d` | 2.61 | +0.47 | +1.25 | -0.97 | 71 |
| `15_up_10_down__15_in_5d` | 2.50 | +0.59 | -0.90 | +0.33 | 54 |
| `3_above_200_ema__pct` | 43.45 | +0.23 | +0.50 | +9.36 | 52 |
| `4_advance_decline__4_advance` | 131.00 | +26.00 | +8.00 | +50.00 | 35 |
| `4_advance_decline__4_decline` | 102.00 | -239.00 | -13.00 | -189.00 | 63 |
| `4_advance_decline_today__4_advance` | 134.00 | +29.00 | +6.00 | -36.00 | 36 |
| `4_advance_decline_today__4_decline` | 107.00 | -236.00 | -8.00 | +41.00 | 60 |
| `4_advance_decline_today__net_breadth` | 1.05 | +10.26 | +0.54 | -3.31 | 36 |
| `52_week_high_low_within_10__high` | 20.24 | +0.14 | +1.29 | +6.35 | 62 |
| `52_week_high_low_within_10__low` | 19.00 | +0.24 | +1.52 | -9.60 | 50 |
| `52_wk_high_low__new_52_wk_high` | 2.35 | +0.20 | +0.72 | +0.90 | 54 |
| `52_wk_high_low__new_52_wk_low` | 0.68 | -0.55 | +0.07 | -2.70 | 31 |
| `52_wk_high_low_today__new_52_wk_high` | 2.33 | +0.19 | +0.64 | +0.96 | 84 |
| `52_wk_high_low_today__new_52_wk_low` | 0.86 | -0.38 | +0.11 | -1.22 | 16 |
| `5_advance_decline_ratio__advance` | 48.84 | +18.04 | +4.24 | -10.28 | 56 |
| `5_advance_decline_ratio__decline` | 50.14 | -18.04 | -4.22 | +10.30 | 47 |
| `above_10ma__pct` | 50.78 | -0.68 | -20.89 | +23.00 | 66 |
| `above_200ma__above_200ma` | 43.45 | +0.23 | +0.50 | +9.36 | 55 |
| `above_20_ema__pct` | 53.62 | -1.02 | -9.59 | +29.15 | 69 |
| `above_20ma__pct` | 53.62 | -1.02 | -9.59 | +29.15 | 69 |
| `above_50_ema__pct` | 46.87 | +0.18 | +0.47 | +22.80 | 48 |
| `above_50ma__above_50ma` | 43.45 | +0.23 | +0.50 | +9.36 | 55 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,065.00 | +10.00 | +12.00 | +163.00 | 71 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,253.00 | -22.00 | -210.00 | +646.00 | 74 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,103.00 | +20.00 | +21.00 | +491.00 | 62 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,275.00 | -10.00 | -11.00 | -169.00 | 64 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,086.00 | +21.00 | +210.00 | -653.00 | 46 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,237.00 | -20.00 | -20.00 | -497.00 | 60 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 4.00 | +1.00 | +0.00 | -3.00 | 82 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 46.00 | -169.00 | -9.00 | -117.00 | 68 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 15.00 | -1.00 | -13.00 | -5.00 | 52 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 70.00 | +0.00 | -4.00 | +25.00 | 44 |
| `current_previous_yr_volumes_crores__1_yr_back` | 522.61 | +152.93 | -48.40 | +41.20 | 89 |
| `current_previous_yr_volumes_crores__current` | 455.95 | +6.45 | +51.37 | -70.49 | 23 |
| `drawdowns_peaks__blw_3` | 197.00 | -390.00 | -34.00 | -400.00 | 70 |
| `gold_etfs_nifty_1_month_chg__gold` | -9.46 | -0.09 | -3.48 | -4.46 | 10 |
| `gold_etfs_nifty_1_month_chg__nifty` | 13.18 | +0.24 | +5.33 | +16.90 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 46.14 | -0.95 | -22.19 | +19.91 | 61 |
| `mbm_2_0_magnitude__abv_200ma` | 38.03 | +0.39 | +0.47 | +1.65 | 46 |
| `mbm_2_0_magnitude__abv_20ma` | 48.83 | -0.90 | -10.34 | +24.96 | 67 |
| `mbm_2_0_magnitude__abv_50ma` | 40.76 | +0.17 | +0.51 | +14.61 | 51 |
| `mbm_2_0_velocity_advanced__15_52wh` | 17.39 | +0.37 | +2.22 | +2.69 | 54 |
| `mbm_2_0_velocity_advanced__15_52wl` | 23.95 | +0.39 | +1.44 | -5.31 | 57 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 45.79 | +0.10 | -0.35 | -0.42 | 46 |
| `mbm_2_0_velocity_advanced__30_52wh` | 46.45 | -0.01 | +0.43 | -0.19 | 58 |
| `mbm_2_0_velocity_advanced__breakdowns` | 11.35 | -13.11 | -2.14 | -14.45 | 67 |
| `mbm_2_0_velocity_advanced__breakouts` | 15.64 | +3.12 | +2.22 | +4.43 | 53 |
| `mbm_2_0_velocity_advanced__down_close` | 35.05 | -19.16 | +1.81 | -9.31 | 55 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -6.55 | -0.02 | +0.78 | +8.00 | 46 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 0.66 | -0.11 | +0.78 | +0.23 | 56 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 1.40 | +0.55 | +0.47 | +3.68 | 71 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 2.22 | +0.05 | +0.62 | +0.65 | 74 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 0.82 | -0.50 | +0.16 | -3.03 | 40 |
| `mbm_2_0_velocity_advanced__up_close` | 32.67 | +0.06 | -3.09 | +4.25 | 30 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.58 | -0.11 | -0.08 | -0.63 | 61 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.61 | +0.47 | +1.25 | -0.97 | 64 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.50 | +0.59 | -0.90 | +0.33 | 63 |
| `mbm_2_0_velocity_basic__3_range` | 39.00 | +7.66 | +0.62 | +9.35 | 47 |
| `mbm_2_0_velocity_basic__4_advance` | 5.11 | +1.03 | +0.31 | +1.92 | 44 |
| `mbm_2_0_velocity_basic__4_decline` | 3.98 | -9.28 | -0.51 | -7.46 | 68 |
| `mbm_2_0_velocity_basic__5d_range` | 4.21 | +0.64 | +3.16 | -1.14 | 45 |
| `mbm_2_0_velocity_basic__net_breadth` | 1.13 | +10.31 | +0.82 | +9.39 | 35 |
| `mbm_2_0_velocity_basic__volume` | 0.41 | -0.12 | +0.12 | +0.13 | 40 |
| `net_breadth__net_breadth` | 1.13 | +10.31 | +0.82 | +9.39 | 31 |
| `net_nh_nl__net_nh_nl` | 1.40 | +0.55 | +0.47 | +3.68 | 52 |
| `new_high_low_bearishness_bullishness__high` | 72.00 | +6.00 | +22.00 | +28.00 | 82 |
| `new_high_low_bearishness_bullishness__low` | 21.00 | -17.00 | +2.00 | -82.00 | 41 |
| `volume__volume` | 0.41 | -0.12 | +0.12 | +0.13 | 44 |

## No reading for 2026-11-17

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-16, 64.59
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-16, 35.41
- `oversold_overbought_rsi__overbought`: last 2026-11-16, 97.00
- `oversold_overbought_rsi__oversold`: last 2026-11-16, 79.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-16, 0.41
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-16, 0.52


<!-- market-read -->

## Market read

Tuesday was a quiet day after a hard one, and the quiet favoured the buyers a little. The Nifty rose about a third of a percent and closed near 25,390. Banks and realty did the lifting, with the PSU bank index up about two percent. Under the index, about as many stocks rose as fell. Only 46 stocks fell four and a half percent or more, against 215 on Monday. 70 rose that hard, the same as Monday. So the selling stopped, but no buying wave came to replace it. The count above the 50 day line rose by 20 to 1,103, still about 70 stocks short of half the market. The count above the 200 day line rose by 10 to 1,065. The short count slipped by 22 to 1,253, still a little over half. New yearly highs rose to 72, and new yearly lows fell to 21. Turnover was ordinary at about 456 crore. The fear gauge eased to 15.5. Monday did not repeat. Tuesday did not repair it either. The market is resting at the level Monday left it.

Full brief: briefs/2026-11-17.html
