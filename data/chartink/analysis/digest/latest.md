# Market breadth digest: 2026-10-23

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-23: **69** of 79
- History available: 2019-07-01 to 2026-10-23, 703 dated rows
- Metrics with no reading for 2026-10-23: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 7.03 | -4.43 | -27.05 | -50.30 | 0 | 407 |
| % above 20 EMA | 7.71 | -4.39 | -21.19 | -40.48 | 1 | 407 |
| % above 50 EMA | 11.12 | -3.93 | -17.99 | -34.50 | 4 | 407 |
| % above 200 EMA | 24.97 | -4.02 | -12.99 | -22.29 | 21 | 407 |
| Net breadth (4% adv minus dec) | -24.34 | -16.67 | -19.36 | -32.85 | 3 | 407 |
| 4% advancers | 2.23 | -0.25 | -1.27 | -7.58 | 7 | 407 |
| 4% decliners | 26.57 | +16.41 | +18.09 | +25.26 | 97 | 407 |
| Net new highs minus lows | -17.47 | -5.67 | -17.43 | -19.79 | 3 | 407 |
| Net within 15% of 52wk H/L | -33.43 | -6.63 | -21.66 | -37.81 | 12 | 407 |
| Volume expansion ratio | 1.27 | +0.87 | +0.92 | +0.78 | 92 | 407 |
| Overbought count (weekly RSI>70) (as of 2026-10-19) | 56.00 | -73.00 | -144.00 | -111.00 | 19 | 382 |
| Oversold count (weekly RSI<30) (as of 2026-10-19) | 350.00 | +218.00 | +268.00 | +319.00 | 96 | 382 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 1,089.00 | +627.00 | 99 |
| `4_advance_decline__4_decline` | 631.00 | +390.00 | 100 |
| `4_advance_decline_today__4_decline` | 634.00 | +390.00 | 100 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 360.00 | +233.00 | 97 |
| `new_high_low_bearishness_bullishness__low` | 453.00 | +146.00 | 97 |
| `breadth_above_500_trend_reversal__above_20dma` | 178.00 | -108.00 | 1 |
| `breadth_above_500_trend_reversal__below_20dma` | 2,068.00 | +107.00 | 100 |
| `breadth_above_500_trend_reversal__above_200dma` | 579.00 | -94.00 | 17 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,667.00 | +93.00 | 95 |
| `breadth_above_500_trend_reversal__above_50dma` | 253.00 | -88.00 | 4 |

## At the edge of their own range

Top decile of history:

- `breadth_above_500_trend_reversal__below_20dma` at 2,068.00 (percentile 100, range 76.00 to 2,068.00)
- `breadth_above_500_trend_reversal__below_50dma` at 1,993.00 (percentile 100, range 273.00 to 1,993.00)
- `10_from_10dema__10_10ema` at 7.07 (percentile 100, range 0.09 to 7.07)
- `15_up_10_down__10_in_5d` at 27.83 (percentile 100, range 0.34 to 27.83)
- `4_advance_decline__4_decline` at 631.00 (percentile 100, range 22.00 to 631.00)
- `4_advance_decline_today__4_decline` at 634.00 (percentile 100, range 36.00 to 634.00)
- `52_wk_high_low__new_52_wk_low` at 15.84 (percentile 100, range 0.18 to 15.84)
- `52_wk_high_low_today__new_52_wk_low` at 14.97 (percentile 100, range 0.85 to 14.97)
- `volume__volume` at 1.27 (percentile 100, range 0.24 to 1.27)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 26.00 (percentile 100, range 0.00 to 33.00)
- `mbm_2_0_velocity_basic__10_in_5d` at 27.83 (percentile 100, range 0.18 to 37.65)
- `mbm_2_0_velocity_basic__10_10ema` at 7.07 (percentile 99, range 0.00 to 16.96)
- `mbm_2_0_velocity_advanced__breakdowns` at 68.51 (percentile 99, range 2.47 to 94.86)
- `drawdowns_peaks__blw_3` at 1,089.00 (percentile 99, range 21.00 to 1,869.00)
- `breadth_above_500_trend_reversal__down_4_5_today` at 360.00 (percentile 97, range 1.00 to 952.00)
- `new_high_low_bearishness_bullishness__low` at 453.00 (percentile 97, range 1.00 to 913.00)
- `mbm_2_0_velocity_basic__4_decline` at 26.57 (percentile 97, range 0.28 to 58.22)
- `mbm_2_0_velocity_advanced__new_52_wk_low` at 17.73 (percentile 97, range 0.00 to 39.08)
- `5_advance_decline_ratio__decline` at 84.34 (percentile 97, range 28.74 to 85.61)
- `breadth_above_500_trend_reversal__below_200dma` at 1,667.00 (percentile 95, range 644.00 to 1,821.00)
- `mbm_2_0_velocity_basic__volume` at 1.27 (percentile 92, range 0.03 to 5.67)
- `current_previous_yr_volumes_crores__current` at 610.62 (percentile 91, range 378.80 to 956.94)
- `52_week_high_low_within_10__low` at 40.33 (percentile 90, range 5.02 to 61.95)

Bottom decile of history:

- `mbm_2_0_magnitude__abv_10ma` at 7.03 (percentile 0, range 6.70 to 96.14)
- `above_20_ema__pct` at 8.22 (percentile 1, range 6.35 to 96.00)
- `breadth_above_500_trend_reversal__above_20dma` at 178.00 (percentile 1, range 119.00 to 2,043.00)
- `mbm_2_0_velocity_basic__3_range` at 8.34 (percentile 1, range 7.46 to 63.05)
- `15_up_10_down__15_in_5d` at 0.76 (percentile 1, range 0.76 to 7.11)
- `52_wk_high_low__new_52_wk_high` at 0.28 (percentile 1, range 0.28 to 5.21)
- `net_breadth__net_breadth` at -24.34 (percentile 1, range -24.34 to 19.72)
- `net_nh_nl__net_nh_nl` at -17.47 (percentile 1, range -17.47 to 3.67)
- `above_10ma__pct` at 7.70 (percentile 1, range 7.00 to 96.53)
- `above_20ma__pct` at 8.22 (percentile 1, range 7.00 to 96.00)
- `mbm_2_0_magnitude__abv_20ma` at 7.71 (percentile 1, range 5.26 to 95.55)
- `above_50_ema__pct` at 10.70 (percentile 2, range 7.90 to 85.55)
- `mbm_2_0_velocity_advanced__new_52_wk_high` at 0.25 (percentile 2, range 0.15 to 4.76)
- `new_high_low_bearishness_bullishness__high` at 8.00 (percentile 2, range 5.00 to 148.00)
- `mbm_2_0_velocity_basic__net_breadth` at -24.34 (percentile 3, range -57.32 to 63.88)
- `mbm_2_0_velocity_advanced__net_nh_nl` at -17.47 (percentile 3, range -38.76 to 4.72)
- `4_advance_decline_today__net_breadth` at -24.25 (percentile 3, range -24.25 to 10.36)
- `breadth_above_500_trend_reversal__above_50dma` at 253.00 (percentile 4, range 121.00 to 1,883.00)
- `mbm_2_0_magnitude__abv_50ma` at 11.12 (percentile 4, range 4.10 to 84.35)
- `4_advance_decline__4_advance` at 53.00 (percentile 4, range 30.00 to 479.00)
- `52_week_high_low_within_10__high` at 5.98 (percentile 5, range 3.64 to 28.39)
- `breadth_above_500_trend_reversal__up_4_5_today` at 25.00 (percentile 5, range 6.00 to 1,125.00)
- `5_advance_decline_ratio__advance` at 14.62 (percentile 7, range 13.35 to 70.21)
- `52_wk_high_low_today__new_52_wk_high` at 0.33 (percentile 7, range 0.32 to 3.65)
- `mbm_2_0_velocity_basic__4_advance` at 2.23 (percentile 7, range 0.91 to 64.61)
- `mbm_2_0_velocity_basic__15_in_5d` at 0.76 (percentile 7, range 0.23 to 42.62)
- `mbm_2_0_velocity_advanced__15_52wh` at 7.37 (percentile 8, range 2.78 to 28.69)
- `mbm_2_0_velocity_basic__5d_range` at 0.80 (percentile 9, range 0.32 to 19.43)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 7.07 | +3.41 | +6.19 | +6.82 | 100 |
| `15_up_10_down__10_in_5d` | 27.83 | +9.92 | +26.06 | +27.16 | 100 |
| `15_up_10_down__15_in_5d` | 0.76 | -0.17 | -1.44 | -3.37 | 1 |
| `3_above_200_ema__pct` | 22.60 | -3.57 | -13.06 | -25.55 | 11 |
| `4_advance_decline__4_advance` | 53.00 | -6.00 | -30.00 | -180.00 | 4 |
| `4_advance_decline__4_decline` | 631.00 | +390.00 | +430.00 | +600.00 | 100 |
| `4_advance_decline_today__4_advance` | 55.00 | -6.00 | -31.00 | -103.00 | 10 |
| `4_advance_decline_today__4_decline` | 634.00 | +390.00 | +430.00 | +577.00 | 100 |
| `4_advance_decline_today__net_breadth` | -24.25 | -16.59 | -19.31 | -28.47 | 3 |
| `52_week_high_low_within_10__high` | 5.98 | -2.67 | -10.80 | -20.35 | 5 |
| `52_week_high_low_within_10__low` | 40.33 | +4.25 | +11.61 | +19.15 | 90 |
| `52_wk_high_low__new_52_wk_high` | 0.28 | -0.00 | -1.05 | -2.49 | 1 |
| `52_wk_high_low__new_52_wk_low` | 15.84 | +5.09 | +14.48 | +15.04 | 100 |
| `52_wk_high_low_today__new_52_wk_high` | 0.33 | +0.00 | -0.98 | -2.02 | 7 |
| `52_wk_high_low_today__new_52_wk_low` | 14.97 | +4.93 | +13.51 | +13.48 | 100 |
| `5_advance_decline_ratio__advance` | 14.62 | -12.96 | -21.71 | -29.21 | 7 |
| `5_advance_decline_ratio__decline` | 84.34 | +12.96 | +21.71 | +29.21 | 97 |
| `above_10ma__pct` | 7.70 | -4.53 | -28.21 | -49.52 | 1 |
| `above_200ma__above_200ma` | 22.60 | -3.57 | -13.06 | -25.55 | 13 |
| `above_20_ema__pct` | 8.22 | -4.25 | -21.13 | -36.18 | 1 |
| `above_20ma__pct` | 8.22 | -4.25 | -21.13 | -36.18 | 1 |
| `above_50_ema__pct` | 10.70 | -3.41 | -15.78 | -31.63 | 2 |
| `above_50ma__above_50ma` | 22.60 | -3.57 | -13.06 | -25.55 | 13 |
| `breadth_above_500_trend_reversal__above_200dma` | 579.00 | -94.00 | -332.00 | -602.00 | 17 |
| `breadth_above_500_trend_reversal__above_20dma` | 178.00 | -108.00 | -504.00 | -876.00 | 1 |
| `breadth_above_500_trend_reversal__above_50dma` | 253.00 | -88.00 | -401.00 | -771.00 | 4 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,667.00 | +93.00 | +333.00 | +602.00 | 95 |
| `breadth_above_500_trend_reversal__below_20dma` | 2,068.00 | +107.00 | +505.00 | +876.00 | 100 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,993.00 | +87.00 | +402.00 | +771.00 | 100 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 26.00 | +8.00 | +24.00 | +23.00 | 100 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 360.00 | +233.00 | +243.00 | +348.00 | 97 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 7.00 | -2.00 | -18.00 | -31.00 | 18 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 25.00 | -7.00 | -31.00 | -130.00 | 5 |
| `current_previous_yr_volumes_crores__1_yr_back` | 431.14 | -37.62 | +1.63 | -5.64 | 58 |
| `current_previous_yr_volumes_crores__current` | 610.62 | +16.59 | +111.83 | +88.94 | 91 |
| `drawdowns_peaks__blw_3` | 1,089.00 | +627.00 | +682.00 | +1,025.00 | 99 |
| `gold_etfs_nifty_1_month_chg__gold` | -7.97 | -1.54 | -3.56 | -7.35 | 20 |
| `gold_etfs_nifty_1_month_chg__nifty` | -4.38 | -0.19 | -0.79 | -1.51 | 14 |
| `mbm_2_0_magnitude__abv_10ma` | 7.03 | -4.43 | -27.05 | -50.30 | 0 |
| `mbm_2_0_magnitude__abv_200ma` | 24.97 | -4.02 | -12.99 | -22.29 | 21 |
| `mbm_2_0_magnitude__abv_20ma` | 7.71 | -4.39 | -21.19 | -40.48 | 1 |
| `mbm_2_0_magnitude__abv_50ma` | 11.12 | -3.93 | -17.99 | -34.50 | 4 |
| `mbm_2_0_velocity_advanced__15_52wh` | 7.37 | -2.62 | -10.85 | -19.34 | 8 |
| `mbm_2_0_velocity_advanced__15_52wl` | 40.80 | +4.01 | +10.81 | +18.47 | 86 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 57.77 | +3.41 | +9.81 | +15.65 | 75 |
| `mbm_2_0_velocity_advanced__30_52wh` | 39.66 | -4.63 | -11.24 | -14.51 | 23 |
| `mbm_2_0_velocity_advanced__breakdowns` | 68.51 | +43.14 | +51.09 | +63.58 | 99 |
| `mbm_2_0_velocity_advanced__breakouts` | 8.93 | -4.05 | -3.26 | -11.92 | 10 |
| `mbm_2_0_velocity_advanced__down_close` | 38.78 | -1.25 | -9.89 | +12.29 | 73 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -33.43 | -6.63 | -21.66 | -37.81 | 12 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -18.11 | -8.03 | -21.06 | -30.15 | 23 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -17.47 | -5.67 | -17.43 | -19.79 | 3 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 0.25 | -0.00 | -1.27 | -2.91 | 2 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 17.73 | +5.67 | +16.17 | +16.88 | 97 |
| `mbm_2_0_velocity_advanced__up_close` | 25.00 | +5.84 | -3.72 | -22.07 | 10 |
| `mbm_2_0_velocity_basic__10_10ema` | 7.07 | +3.41 | +6.19 | +6.82 | 99 |
| `mbm_2_0_velocity_basic__10_in_5d` | 27.83 | +9.92 | +26.06 | +27.16 | 100 |
| `mbm_2_0_velocity_basic__15_in_5d` | 0.76 | -0.17 | -1.44 | -3.37 | 7 |
| `mbm_2_0_velocity_basic__3_range` | 8.34 | -18.21 | -30.21 | -36.69 | 1 |
| `mbm_2_0_velocity_basic__4_advance` | 2.23 | -0.25 | -1.27 | -7.58 | 7 |
| `mbm_2_0_velocity_basic__4_decline` | 26.57 | +16.41 | +18.09 | +25.26 | 97 |
| `mbm_2_0_velocity_basic__5d_range` | 0.80 | -0.42 | -5.06 | -7.50 | 9 |
| `mbm_2_0_velocity_basic__net_breadth` | -24.34 | -16.67 | -19.36 | -32.85 | 3 |
| `mbm_2_0_velocity_basic__volume` | 1.27 | +0.87 | +0.92 | +0.78 | 92 |
| `net_breadth__net_breadth` | -24.34 | -16.67 | -19.36 | -32.85 | 1 |
| `net_nh_nl__net_nh_nl` | -17.47 | -5.67 | -17.43 | -19.79 | 1 |
| `new_high_low_bearishness_bullishness__high` | 8.00 | +0.00 | -30.00 | -71.00 | 2 |
| `new_high_low_bearishness_bullishness__low` | 453.00 | +146.00 | +414.00 | +430.00 | 97 |
| `volume__volume` | 1.27 | +0.87 | +0.92 | +0.78 | 100 |

## No reading for 2026-10-23

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-19, 53.12
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-19, 46.88
- `oversold_overbought_rsi__overbought`: last 2026-10-19, 56.00
- `oversold_overbought_rsi__oversold`: last 2026-10-19, 350.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-19, 0.18
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-19, 0.80


<!-- market-read -->

## Market read

The break on Wednesday did not hold as a single bad day. It became a slide. On Friday 360 stocks fell four and a half percent or more, and only 25 rose that much. That is the second day this heavy in three sessions. Only 579 stocks now trade above their 200 day line, about one in four. The count has not been this low since 9 April. 453 stocks made new yearly lows, the most since the March bottom. Turnover was the heaviest since early September, so holders are being pushed out, not drifting away. The Nifty fell less than half a percent, because IT and a few large names still hold it up. The small company indices fell about three percent. Every test the last brief set for a worse market fired except one, and every test for a better market failed. The breadth downtrend is now confirmed, and it holds until a broad day of buying says otherwise.

Full brief: briefs/2026-10-23.html
