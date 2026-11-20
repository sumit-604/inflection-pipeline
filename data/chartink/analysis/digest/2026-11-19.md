# Market breadth digest: 2026-11-19

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-19: **69** of 79
- History available: 2019-07-01 to 2026-11-19, 722 dated rows
- Metrics with no reading for 2026-11-19: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 40.33 | +4.74 | -35.56 | +28.53 | 45 | 426 |
| % above 20 EMA | 42.44 | +1.19 | -27.52 | +30.29 | 50 | 426 |
| % above 50 EMA | 37.87 | +1.66 | -13.71 | +22.60 | 45 | 426 |
| % above 200 EMA | 37.32 | +1.11 | -3.92 | +8.36 | 45 | 426 |
| Net breadth (4% adv minus dec) | 2.31 | +5.24 | -3.59 | +10.27 | 47 | 426 |
| 4% advancers | 5.04 | +1.76 | -2.68 | +2.36 | 43 | 426 |
| 4% decliners | 2.74 | -3.48 | +0.90 | -7.92 | 45 | 426 |
| Net new highs minus lows | -0.35 | -0.31 | -2.03 | +10.54 | 37 | 426 |
| Net within 15% of 52wk H/L | -7.47 | +1.44 | -7.31 | +17.40 | 43 | 426 |
| Volume expansion ratio | 0.34 | +0.09 | -0.27 | -0.04 | 24 | 426 |
| Overbought count (weekly RSI>70) (as of 2026-11-16) | 111.00 | +16.00 | -19.00 | -124.00 | 40 | 386 |
| Oversold count (weekly RSI<30) (as of 2026-11-16) | 84.00 | +22.00 | -43.00 | +60.00 | 77 | 386 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 138.00 | -201.00 | 52 |
| `4_advance_decline__4_decline` | 70.00 | -89.00 | 40 |
| `4_advance_decline_today__4_decline` | 76.00 | -88.00 | 34 |
| `4_advance_decline__4_advance` | 129.00 | +45.00 | 35 |
| `4_advance_decline_today__4_advance` | 131.00 | +45.00 | 36 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,036.00 | +43.00 | 57 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,308.00 | -43.00 | 66 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,122.00 | +42.00 | 66 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,221.00 | -42.00 | 57 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 36.00 | -35.00 | 56 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 13.71 (percentile 100, range -6.93 to 13.71)
- `15_up_10_down__10_in_5d` at 5.63 (percentile 94, range 0.34 to 27.87)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__gold` at -12.12 (percentile 3, range -15.78 to 14.14)
- `15_up_10_down__15_in_5d` at 0.98 (percentile 4, range 0.63 to 7.11)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed up through 50: 43.00 to 76.00
- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 71.00 to 36.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.55 | -0.08 | +0.31 | -2.96 | 50 |
| `15_up_10_down__10_in_5d` | 5.63 | +1.14 | +4.50 | -12.29 | 94 |
| `15_up_10_down__15_in_5d` | 0.98 | -0.47 | -1.01 | -0.01 | 4 |
| `3_above_200_ema__pct` | 42.74 | +1.30 | -3.88 | +16.44 | 49 |
| `4_advance_decline__4_advance` | 129.00 | +45.00 | -69.00 | +61.00 | 35 |
| `4_advance_decline__4_decline` | 70.00 | -89.00 | +23.00 | -200.00 | 40 |
| `4_advance_decline_today__4_advance` | 131.00 | +45.00 | -68.00 | +98.00 | 36 |
| `4_advance_decline_today__4_decline` | 76.00 | -88.00 | +23.00 | -521.00 | 34 |
| `4_advance_decline_today__net_breadth` | 2.13 | +5.16 | -3.52 | +25.75 | 47 |
| `52_week_high_low_within_10__high` | 20.44 | +0.78 | -1.16 | +12.25 | 65 |
| `52_week_high_low_within_10__low` | 20.93 | -0.98 | +7.06 | -12.95 | 57 |
| `52_wk_high_low__new_52_wk_high` | 1.27 | -0.07 | -0.75 | +0.98 | 14 |
| `52_wk_high_low__new_52_wk_low` | 1.27 | +0.03 | +1.04 | -8.76 | 61 |
| `52_wk_high_low_today__new_52_wk_high` | 1.28 | -0.06 | -0.73 | +0.46 | 23 |
| `52_wk_high_low_today__new_52_wk_low` | 1.43 | +0.03 | +1.05 | -6.48 | 30 |
| `5_advance_decline_ratio__advance` | 57.26 | +30.51 | +0.31 | +41.93 | 72 |
| `5_advance_decline_ratio__decline` | 41.72 | -30.51 | -0.31 | -41.91 | 30 |
| `above_10ma__pct` | 45.97 | +6.92 | -31.26 | +33.46 | 58 |
| `above_200ma__above_200ma` | 42.74 | +1.31 | -3.89 | +16.42 | 51 |
| `above_20_ema__pct` | 48.09 | +1.76 | -24.34 | +35.48 | 58 |
| `above_20ma__pct` | 48.12 | +1.79 | -24.32 | +35.52 | 59 |
| `above_50_ema__pct` | 44.11 | +1.80 | -12.37 | +29.68 | 43 |
| `above_50ma__above_50ma` | 42.74 | +1.30 | -3.88 | +16.44 | 51 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,043.00 | +28.00 | -106.00 | +337.00 | 68 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,122.00 | +42.00 | -594.00 | +820.00 | 66 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,036.00 | +43.00 | -307.00 | +667.00 | 57 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,301.00 | -28.00 | +104.00 | -345.00 | 67 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,221.00 | -42.00 | +591.00 | -829.00 | 57 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,308.00 | -43.00 | +305.00 | -675.00 | 66 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 5.00 | +0.00 | +1.00 | -16.00 | 89 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 36.00 | -35.00 | +15.00 | -104.00 | 56 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 5.00 | -3.00 | -7.00 | -6.00 | 11 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 76.00 | +33.00 | -48.00 | +44.00 | 49 |
| `current_previous_yr_volumes_crores__1_yr_back` | 518.29 | +16.62 | +87.28 | +49.14 | 88 |
| `current_previous_yr_volumes_crores__current` | 463.78 | +20.39 | -28.64 | -150.81 | 28 |
| `drawdowns_peaks__blw_3` | 138.00 | -201.00 | +35.00 | -368.00 | 52 |
| `gold_etfs_nifty_1_month_chg__gold` | -12.12 | -0.88 | -5.45 | -5.69 | 3 |
| `gold_etfs_nifty_1_month_chg__nifty` | 13.71 | +2.06 | +1.34 | +17.90 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 40.33 | +4.74 | -35.56 | +28.53 | 45 |
| `mbm_2_0_magnitude__abv_200ma` | 37.32 | +1.11 | -3.92 | +8.36 | 45 |
| `mbm_2_0_magnitude__abv_20ma` | 42.44 | +1.19 | -27.52 | +30.29 | 50 |
| `mbm_2_0_magnitude__abv_50ma` | 37.87 | +1.66 | -13.71 | +22.60 | 45 |
| `mbm_2_0_velocity_advanced__15_52wh` | 17.47 | +0.83 | -1.10 | +8.04 | 55 |
| `mbm_2_0_velocity_advanced__15_52wl` | 24.94 | -0.62 | +6.21 | -9.35 | 59 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 46.79 | -0.37 | +2.65 | -3.99 | 48 |
| `mbm_2_0_velocity_advanced__30_52wh` | 46.48 | +0.88 | -3.09 | +4.77 | 58 |
| `mbm_2_0_velocity_advanced__breakdowns` | 9.07 | -6.17 | +2.24 | -17.29 | 54 |
| `mbm_2_0_velocity_advanced__breakouts` | 14.82 | +5.01 | -4.97 | +1.32 | 47 |
| `mbm_2_0_velocity_advanced__down_close` | 30.17 | -10.60 | +3.32 | -10.25 | 29 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -7.47 | +1.44 | -7.31 | +17.40 | 43 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -0.31 | +1.25 | -5.74 | +8.76 | 53 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.35 | -0.31 | -2.03 | +10.54 | 37 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.13 | -0.19 | -0.78 | +0.86 | 31 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.49 | +0.12 | +1.25 | -9.68 | 59 |
| `mbm_2_0_velocity_advanced__up_close` | 34.04 | +0.57 | -5.02 | +14.15 | 35 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.55 | -0.08 | +0.31 | -2.96 | 57 |
| `mbm_2_0_velocity_basic__10_in_5d` | 5.63 | +1.13 | +4.50 | -12.32 | 87 |
| `mbm_2_0_velocity_basic__15_in_5d` | 0.98 | -0.47 | -1.01 | -0.01 | 15 |
| `mbm_2_0_velocity_basic__3_range` | 42.24 | +2.05 | +1.78 | +16.21 | 59 |
| `mbm_2_0_velocity_basic__4_advance` | 5.04 | +1.76 | -2.68 | +2.36 | 43 |
| `mbm_2_0_velocity_basic__4_decline` | 2.74 | -3.48 | +0.90 | -7.92 | 45 |
| `mbm_2_0_velocity_basic__5d_range` | 5.71 | +0.86 | +1.96 | +4.56 | 56 |
| `mbm_2_0_velocity_basic__net_breadth` | 2.31 | +5.24 | -3.59 | +10.27 | 47 |
| `mbm_2_0_velocity_basic__volume` | 0.34 | +0.09 | -0.27 | -0.04 | 24 |
| `net_breadth__net_breadth` | 2.31 | +5.24 | -3.59 | +10.27 | 45 |
| `net_nh_nl__net_nh_nl` | -0.35 | -0.31 | -2.03 | +10.54 | 25 |
| `new_high_low_bearishness_bullishness__high` | 39.00 | -2.00 | -23.00 | +30.00 | 40 |
| `new_high_low_bearishness_bullishness__low` | 39.00 | +1.00 | +32.00 | -265.00 | 60 |
| `volume__volume` | 0.34 | +0.09 | -0.27 | -0.04 | 25 |

## No reading for 2026-11-19

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-16, 64.39
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-16, 35.61
- `oversold_overbought_rsi__overbought`: last 2026-11-16, 111.00
- `oversold_overbought_rsi__oversold`: last 2026-11-16, 84.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-16, 0.40
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-16, 0.52


<!-- market-read -->

## Market read

The week ended with the big companies holding the index up while the average stock slipped. The Nifty closed Thursday near 25,510, up about one and a half percent on the week. Banks led the week, and car makers and staples joined them on Thursday. Under that, the short, middle and long trend counts all ended below half the market. The long count fell from 1,149 a week earlier to 1,043. New yearly highs and new yearly lows finished level at 39 each. More stocks now trade near their yearly low than near their yearly high. Thursday's lift was broad but light, on modest turnover, and fear rose with prices. So the bounce off the October low still stands, but it rests on fewer shoulders than it did a week ago. The next move depends on whether the average stock follows the large ones up or drags them down.

Full brief: briefs/2026-11-19.html
