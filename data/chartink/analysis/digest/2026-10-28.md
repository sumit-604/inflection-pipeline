# Market breadth digest: 2026-10-28

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-28: **69** of 79
- History available: 2019-07-01 to 2026-10-28, 706 dated rows
- Metrics with no reading for 2026-10-28: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 29.73 | +5.64 | +16.73 | +3.43 | 27 | 410 |
| % above 20 EMA | 20.03 | +2.30 | +6.40 | -7.65 | 11 | 410 |
| % above 50 EMA | 18.35 | +0.82 | +0.16 | -15.59 | 12 | 410 |
| % above 200 EMA | 28.60 | +0.33 | -2.34 | -13.23 | 28 | 410 |
| Net breadth (4% adv minus dec) | 3.80 | -10.19 | +27.53 | +10.13 | 62 | 410 |
| 4% advancers | 7.38 | -9.76 | +6.12 | +4.28 | 71 | 410 |
| 4% decliners | 3.58 | +0.43 | -21.41 | -5.85 | 63 | 410 |
| Net new highs minus lows | -2.74 | +0.12 | +5.93 | -1.15 | 20 | 410 |
| Net within 15% of 52wk H/L | -25.98 | +0.22 | -2.33 | -22.29 | 18 | 410 |
| Volume expansion ratio | 0.31 | -0.08 | -0.35 | -0.08 | 14 | 410 |
| Overbought count (weekly RSI>70) (as of 2026-10-26) | 57.00 | +1.00 | -144.00 | -107.00 | 19 | 383 |
| Oversold count (weekly RSI<30) (as of 2026-10-26) | 243.00 | -107.00 | +161.00 | +206.00 | 92 | 383 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `4_advance_decline__4_advance` | 175.00 | -232.00 | 71 |
| `4_advance_decline_today__4_advance` | 178.00 | -231.00 | 78 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 103.00 | -168.00 | 69 |
| `current_previous_yr_volumes_crores__current` | 421.99 | -101.86 | 11 |
| `drawdowns_peaks__blw_3` | 170.00 | +51.00 | 63 |
| `breadth_above_500_trend_reversal__above_20dma` | 458.00 | +43.00 | 13 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,788.00 | -43.00 | 95 |
| `current_previous_yr_volumes_crores__1_yr_back` | 439.30 | +23.37 | 61 |
| `mbm_2_0_velocity_advanced__breakouts` | 19.74 | -18.21 | 76 |
| `5_advance_decline_ratio__advance` | 53.48 | -16.93 | 72 |

## At the edge of their own range

Top decile of history:

- `breadth_above_500_trend_reversal__below_50dma` at 1,829.00 (percentile 97, range 271.00 to 1,994.00)
- `breadth_above_500_trend_reversal__below_20dma` at 1,788.00 (percentile 95, range 76.00 to 2,068.00)
- `10_from_10dema__10_10ema` at 1.86 (percentile 95, range 0.09 to 7.07)
- `mbm_2_0_velocity_basic__10_10ema` at 1.86 (percentile 93, range 0.00 to 16.96)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 6.00 (percentile 92, range 0.00 to 33.00)
- `15_up_10_down__10_in_5d` at 4.89 (percentile 92, range 0.34 to 28.13)

Bottom decile of history:

- `52_wk_high_low__new_52_wk_high` at 0.81 (percentile 6, range 0.28 to 5.21)
- `15_up_10_down__15_in_5d` at 1.10 (percentile 8, range 0.59 to 7.11)
- `above_20_ema__pct` at 19.47 (percentile 9, range 6.35 to 96.00)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 41.00 to 53.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.86 | -0.50 | -0.29 | +1.14 | 95 |
| `15_up_10_down__10_in_5d` | 4.89 | -6.40 | -4.24 | +2.33 | 92 |
| `15_up_10_down__15_in_5d` | 1.10 | +0.51 | -0.08 | -1.42 | 8 |
| `3_above_200_ema__pct` | 26.06 | +0.33 | -1.90 | -13.63 | 15 |
| `4_advance_decline__4_advance` | 175.00 | -232.00 | +145.00 | +101.00 | 71 |
| `4_advance_decline__4_decline` | 85.00 | +10.00 | -509.00 | -140.00 | 60 |
| `4_advance_decline_today__4_advance` | 178.00 | -231.00 | +145.00 | +28.00 | 78 |
| `4_advance_decline_today__4_decline` | 89.00 | +10.00 | -508.00 | +34.00 | 53 |
| `4_advance_decline_today__net_breadth` | 3.73 | -10.09 | +27.35 | -0.24 | 69 |
| `52_week_high_low_within_10__high` | 9.89 | +0.20 | -0.26 | -11.43 | 13 |
| `52_week_high_low_within_10__low` | 36.23 | -1.08 | +1.84 | +9.86 | 86 |
| `52_wk_high_low__new_52_wk_high` | 0.81 | +0.18 | +0.00 | -1.32 | 6 |
| `52_wk_high_low__new_52_wk_low` | 3.26 | +0.01 | -5.03 | -0.50 | 85 |
| `52_wk_high_low_today__new_52_wk_high` | 0.81 | +0.16 | +0.00 | -1.07 | 19 |
| `52_wk_high_low_today__new_52_wk_low` | 3.26 | +0.00 | -4.65 | +0.59 | 59 |
| `5_advance_decline_ratio__advance` | 53.48 | -16.93 | +38.15 | +0.88 | 72 |
| `5_advance_decline_ratio__decline` | 45.48 | +16.93 | -38.15 | -0.85 | 31 |
| `above_10ma__pct` | 30.48 | +5.00 | +16.38 | +7.31 | 27 |
| `above_200ma__above_200ma` | 26.06 | +0.33 | -1.90 | -13.63 | 17 |
| `above_20_ema__pct` | 19.47 | +1.76 | +5.33 | -4.85 | 9 |
| `above_20ma__pct` | 19.47 | +1.76 | +5.33 | -4.85 | 11 |
| `above_50_ema__pct` | 17.08 | +0.63 | +0.15 | -12.57 | 11 |
| `above_50ma__above_50ma` | 26.06 | +0.33 | -1.90 | -13.63 | 17 |
| `breadth_above_500_trend_reversal__above_200dma` | 663.00 | +5.00 | -54.00 | -324.00 | 21 |
| `breadth_above_500_trend_reversal__above_20dma` | 458.00 | +43.00 | +139.00 | -116.00 | 13 |
| `breadth_above_500_trend_reversal__above_50dma` | 417.00 | +13.00 | +10.00 | -311.00 | 11 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,583.00 | -5.00 | +53.00 | +324.00 | 90 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,788.00 | -43.00 | -140.00 | +116.00 | 95 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,829.00 | -13.00 | -11.00 | +311.00 | 97 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 6.00 | -8.00 | +0.00 | +1.00 | 92 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 53.00 | +12.00 | -332.00 | -53.00 | 73 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 13.00 | +6.00 | +3.00 | -9.00 | 45 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 103.00 | -168.00 | +83.00 | +57.00 | 69 |
| `current_previous_yr_volumes_crores__1_yr_back` | 439.30 | +23.37 | -17.69 | -276.41 | 61 |
| `current_previous_yr_volumes_crores__current` | 421.99 | -101.86 | -135.98 | -50.20 | 11 |
| `drawdowns_peaks__blw_3` | 170.00 | +51.00 | -853.00 | -362.00 | 63 |
| `gold_etfs_nifty_1_month_chg__gold` | -6.29 | +2.10 | +0.82 | -3.15 | 27 |
| `gold_etfs_nifty_1_month_chg__nifty` | -3.56 | +0.20 | +0.80 | +2.32 | 27 |
| `mbm_2_0_magnitude__abv_10ma` | 29.73 | +5.64 | +16.73 | +3.43 | 27 |
| `mbm_2_0_magnitude__abv_200ma` | 28.60 | +0.33 | -2.34 | -13.23 | 28 |
| `mbm_2_0_magnitude__abv_20ma` | 20.03 | +2.30 | +6.40 | -7.65 | 11 |
| `mbm_2_0_magnitude__abv_50ma` | 18.35 | +0.82 | +0.16 | -15.59 | 12 |
| `mbm_2_0_velocity_advanced__15_52wh` | 10.67 | -0.37 | -0.44 | -12.19 | 18 |
| `mbm_2_0_velocity_advanced__15_52wl` | 36.65 | -0.59 | +1.89 | +10.10 | 78 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 56.09 | +0.41 | +3.36 | +11.38 | 71 |
| `mbm_2_0_velocity_advanced__30_52wh` | 43.32 | +0.27 | -2.43 | -8.45 | 37 |
| `mbm_2_0_velocity_advanced__breakdowns` | 12.65 | +5.20 | -36.17 | -9.03 | 72 |
| `mbm_2_0_velocity_advanced__breakouts` | 19.74 | -18.21 | +10.90 | +9.04 | 76 |
| `mbm_2_0_velocity_advanced__down_close` | 28.33 | -14.04 | -22.87 | -15.19 | 23 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -25.98 | +0.22 | -2.33 | -22.29 | 18 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -12.78 | -0.14 | -5.79 | -19.83 | 30 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -2.74 | +0.12 | +5.93 | -1.15 | 20 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 0.76 | +0.13 | -0.04 | -1.55 | 20 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 3.50 | +0.00 | -5.97 | -0.40 | 78 |
| `mbm_2_0_velocity_advanced__up_close` | 37.39 | -7.78 | +23.11 | +8.37 | 50 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.86 | -0.50 | -0.29 | +1.14 | 93 |
| `mbm_2_0_velocity_basic__10_in_5d` | 4.89 | -6.40 | -4.24 | +2.33 | 85 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.10 | +0.51 | -0.08 | -1.42 | 20 |
| `mbm_2_0_velocity_basic__3_range` | 32.01 | +9.98 | +17.11 | -0.41 | 29 |
| `mbm_2_0_velocity_basic__4_advance` | 7.38 | -9.76 | +6.12 | +4.28 | 71 |
| `mbm_2_0_velocity_basic__4_decline` | 3.58 | +0.43 | -21.41 | -5.85 | 63 |
| `mbm_2_0_velocity_basic__5d_range` | 1.31 | +0.51 | -0.97 | -4.82 | 16 |
| `mbm_2_0_velocity_basic__net_breadth` | 3.80 | -10.19 | +27.53 | +10.13 | 62 |
| `mbm_2_0_velocity_basic__volume` | 0.31 | -0.08 | -0.35 | -0.08 | 14 |
| `net_breadth__net_breadth` | 3.80 | -10.19 | +27.53 | +10.13 | 62 |
| `net_nh_nl__net_nh_nl` | -2.74 | +0.12 | +5.93 | -1.15 | 12 |
| `new_high_low_bearishness_bullishness__high` | 23.00 | +5.00 | +0.00 | -38.00 | 19 |
| `new_high_low_bearishness_bullishness__low` | 93.00 | +0.00 | -144.00 | -15.00 | 80 |
| `volume__volume` | 0.31 | -0.08 | -0.35 | -0.08 | 15 |

## No reading for 2026-10-28

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-26, 55.73
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-26, 44.27
- `oversold_overbought_rsi__overbought`: last 2026-10-26, 57.00
- `oversold_overbought_rsi__oversold`: last 2026-10-26, 243.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-26, 0.23
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-26, 0.75


<!-- market-read -->

## Market read

Wednesday was the third up day in a row, and the quietest of the three. About 100 stocks rose four and a half percent or more, against about 50 that fell that hard. On Tuesday the count was 270 against 41. Turnover fell to about 422 crore, the lowest of the last four sessions and below the level a year ago. The Nifty slipped a fifth of a percent while the small company index rose more than one percent. Oil and gas and IT fell about two percent each. Autos, pharma and media led. The long trend count edged up to 663 stocks above the 200 day line, about three in ten. New lows held at 93 and new highs rose to 23. The bounce did not fail. It did not confirm either. The market paused on light volume, with four stocks in five still below their short trend lines. The staircase down from August stands until a wide day arrives on heavier volume than last Friday's selling.

Full brief: briefs/2026-10-28.html
