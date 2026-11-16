# Market breadth digest: 2026-11-16

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-16: **75** of 79
- History available: 2019-07-01 to 2026-11-16, 719 dated rows
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 47.07 | -20.31 | -29.56 | +6.04 | 62 | 423 |
| % above 20 EMA | 49.75 | -14.52 | -13.82 | +15.53 | 69 | 423 |
| % above 50 EMA | 40.62 | -7.51 | -1.77 | +8.69 | 51 | 423 |
| % above 200 EMA | 37.63 | -3.33 | -1.15 | -2.13 | 46 | 423 |
| Net breadth (4% adv minus dec) | -9.24 | -10.37 | -17.95 | -13.42 | 7 | 423 |
| 4% advancers | 4.08 | -1.34 | -5.61 | -3.13 | 30 | 423 |
| 4% decliners | 13.32 | +9.03 | +12.34 | +10.29 | 94 | 423 |
| Net new highs minus lows | 0.85 | -0.90 | -0.60 | +1.25 | 55 | 423 |
| Net within 15% of 52wk H/L | -6.56 | -4.50 | -0.05 | +3.28 | 46 | 423 |
| Volume expansion ratio | 0.52 | +0.05 | +0.49 | +0.18 | 58 | 423 |
| Overbought count (weekly RSI>70) | 90.00 | -5.00 | -40.00 | -145.00 | 32 | 386 |
| Oversold count (weekly RSI<30) | 88.00 | +26.00 | -39.00 | +64.00 | 78 | 386 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 587.00 | +352.00 | 93 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,273.00 | -317.00 | 75 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,066.00 | +317.00 | 43 |
| `4_advance_decline__4_decline` | 343.00 | +233.00 | 95 |
| `4_advance_decline_today__4_decline` | 343.00 | +229.00 | 89 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,081.00 | -179.00 | 60 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,258.00 | +179.00 | 62 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 215.00 | +156.00 | 94 |
| `current_previous_yr_volumes_crores__1_yr_back` | 369.68 | -79.04 | 21 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,053.00 | -77.00 | 69 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 12.94 (percentile 100, range -6.93 to 12.94)
- `mbm_2_0_velocity_advanced__down_close` at 54.19 (percentile 97, range 4.96 to 72.81)
- `4_advance_decline__4_decline` at 343.00 (percentile 95, range 22.00 to 688.00)
- `breadth_above_500_trend_reversal__down_4_5_today` at 215.00 (percentile 94, range 1.00 to 957.00)
- `mbm_2_0_velocity_basic__4_decline` at 13.32 (percentile 94, range 0.28 to 58.25)
- `drawdowns_peaks__blw_3` at 587.00 (percentile 93, range 16.00 to 1,868.00)

Bottom decile of history:

- `net_breadth__net_breadth` at -9.24 (percentile 6, range -24.75 to 19.72)
- `mbm_2_0_velocity_basic__net_breadth` at -9.24 (percentile 7, range -57.35 to 63.93)

## Crossed the 50 line today

- `above_50_ema__pct` crossed down through 50: 53.34 to 46.71
- `mbm_2_0_magnitude__abv_10ma` crossed down through 50: 67.38 to 47.07
- `mbm_2_0_magnitude__abv_20ma` crossed down through 50: 64.26 to 49.75

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.70 | +0.50 | +0.46 | +0.03 | 74 |
| `15_up_10_down__10_in_5d` | 2.14 | +1.47 | +1.27 | +0.52 | 57 |
| `15_up_10_down__15_in_5d` | 1.94 | -0.75 | -2.41 | -0.54 | 39 |
| `3_above_200_ema__pct` | 43.24 | -3.03 | -0.80 | +5.47 | 51 |
| `4_advance_decline__4_advance` | 105.00 | -34.00 | -142.00 | -78.00 | 23 |
| `4_advance_decline__4_decline` | 343.00 | +233.00 | +318.00 | +266.00 | 95 |
| `4_advance_decline_today__4_advance` | 105.00 | -38.00 | -1.00 | +19.00 | 30 |
| `4_advance_decline_today__4_decline` | 343.00 | +229.00 | +114.00 | +139.00 | 89 |
| `4_advance_decline_today__net_breadth` | -9.21 | -10.34 | -4.07 | -4.28 | 14 |
| `52_week_high_low_within_10__high` | 20.08 | -1.23 | +1.16 | +3.50 | 60 |
| `52_week_high_low_within_10__low` | 18.75 | +3.82 | +1.47 | -7.75 | 49 |
| `52_wk_high_low__new_52_wk_high` | 2.14 | -0.08 | +0.11 | +0.79 | 45 |
| `52_wk_high_low__new_52_wk_low` | 1.23 | +0.78 | +0.91 | -0.58 | 58 |
| `52_wk_high_low_today__new_52_wk_high` | 2.14 | -0.06 | +0.57 | +0.83 | 75 |
| `52_wk_high_low_today__new_52_wk_low` | 1.24 | +0.64 | -0.12 | -0.22 | 18 |
| `5_advance_decline_ratio__advance` | 30.79 | -4.97 | -8.21 | -5.53 | 25 |
| `5_advance_decline_ratio__decline` | 68.19 | +5.00 | +8.26 | +5.56 | 77 |
| `above_10ma__pct` | 51.46 | -17.98 | -27.42 | +8.57 | 67 |
| `above_200ma__above_200ma` | 43.21 | -3.03 | -0.83 | +5.43 | 54 |
| `above_20_ema__pct` | 54.65 | -12.73 | -12.26 | +20.05 | 70 |
| `above_20ma__pct` | 54.64 | -12.74 | -12.30 | +20.02 | 70 |
| `above_50_ema__pct` | 46.71 | -6.63 | -1.75 | +17.04 | 48 |
| `above_50ma__above_50ma` | 43.21 | -3.03 | -0.83 | +5.43 | 54 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,053.00 | -77.00 | -14.00 | +62.00 | 69 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,273.00 | -317.00 | -266.00 | +415.00 | 75 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,081.00 | -179.00 | -35.00 | +324.00 | 60 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,286.00 | +77.00 | +19.00 | -67.00 | 66 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,066.00 | +317.00 | +271.00 | -420.00 | 43 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,258.00 | +179.00 | +40.00 | -329.00 | 62 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 3.00 | +1.00 | +0.00 | +3.00 | 74 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 215.00 | +156.00 | +201.00 | +177.00 | 94 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 15.00 | +1.00 | -17.00 | -13.00 | 52 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 69.00 | -3.00 | -37.00 | -43.00 | 42 |
| `current_previous_yr_volumes_crores__1_yr_back` | 369.68 | -79.04 | -87.65 | -61.51 | 21 |
| `current_previous_yr_volumes_crores__current` | 449.58 | +2.94 | +334.00 | -165.35 | 20 |
| `drawdowns_peaks__blw_3` | 587.00 | +352.00 | +544.00 | +447.00 | 93 |
| `gold_etfs_nifty_1_month_chg__gold` | -9.37 | -1.47 | -3.87 | -6.73 | 11 |
| `gold_etfs_nifty_1_month_chg__nifty` | 12.94 | +1.50 | +5.69 | +15.71 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 47.07 | -20.31 | -29.56 | +6.04 | 62 |
| `mbm_2_0_magnitude__abv_200ma` | 37.63 | -3.33 | -1.15 | -2.13 | 46 |
| `mbm_2_0_magnitude__abv_20ma` | 49.75 | -14.52 | -13.82 | +15.53 | 69 |
| `mbm_2_0_magnitude__abv_50ma` | 40.62 | -7.51 | -1.77 | +8.69 | 51 |
| `mbm_2_0_velocity_advanced__15_52wh` | 17.00 | -1.03 | +1.36 | -0.51 | 51 |
| `mbm_2_0_velocity_advanced__15_52wl` | 23.56 | +3.46 | +1.42 | -3.79 | 56 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 45.65 | +0.85 | -0.68 | +0.83 | 45 |
| `mbm_2_0_velocity_advanced__30_52wh` | 46.39 | -2.31 | -0.49 | -2.13 | 58 |
| `mbm_2_0_velocity_advanced__breakdowns` | 24.57 | +11.44 | +18.14 | +15.01 | 89 |
| `mbm_2_0_velocity_advanced__breakouts` | 12.54 | -2.19 | -14.31 | -5.76 | 32 |
| `mbm_2_0_velocity_advanced__down_close` | 54.19 | +21.55 | +38.94 | +22.50 | 97 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -6.56 | -4.50 | -0.05 | +3.28 | 46 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 0.74 | -3.16 | +0.19 | -2.96 | 56 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 0.85 | -0.90 | -0.60 | +1.25 | 55 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 2.17 | -0.09 | +0.37 | +0.68 | 73 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.32 | +0.81 | +0.97 | -0.57 | 55 |
| `mbm_2_0_velocity_advanced__up_close` | 32.51 | -4.53 | -3.55 | -6.85 | 29 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.70 | +0.50 | +0.46 | +0.03 | 70 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.14 | +1.47 | +1.27 | +0.52 | 56 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.90 | -0.75 | -2.45 | -0.58 | 48 |
| `mbm_2_0_velocity_basic__3_range` | 31.34 | -9.19 | -16.62 | -9.72 | 28 |
| `mbm_2_0_velocity_basic__4_advance` | 4.08 | -1.34 | -5.61 | -3.13 | 30 |
| `mbm_2_0_velocity_basic__4_decline` | 13.32 | +9.03 | +12.34 | +10.29 | 94 |
| `mbm_2_0_velocity_basic__5d_range` | 3.57 | -1.96 | +3.06 | -3.04 | 39 |
| `mbm_2_0_velocity_basic__net_breadth` | -9.24 | -10.37 | -17.95 | -13.42 | 7 |
| `mbm_2_0_velocity_basic__volume` | 0.52 | +0.05 | +0.49 | +0.18 | 58 |
| `net_breadth__net_breadth` | -9.24 | -10.41 | -17.94 | -13.41 | 6 |
| `net_nh_nl__net_nh_nl` | 0.85 | -0.90 | -0.60 | +1.25 | 40 |
| `new_high_low_bearishness_bullishness__high` | 66.00 | -2.00 | +4.00 | +25.00 | 76 |
| `new_high_low_bearishness_bullishness__low` | 38.00 | +24.00 | +28.00 | -17.00 | 59 |
| `nifty_500_above_below_200_ema__above_200_ema` | 65.39 | -0.60 | +3.62 | -10.06 | 23 |
| `nifty_500_above_below_200_ema__below_200_ema` | 34.61 | +0.60 | -3.62 | +10.06 | 77 |
| `oversold_overbought_rsi__overbought` | 90.00 | -5.00 | -40.00 | -145.00 | 32 |
| `oversold_overbought_rsi__oversold` | 88.00 | +26.00 | -39.00 | +64.00 | 78 |
| `volume__volume` | 0.52 | +0.05 | +0.49 | +0.18 | 69 |
| `weekly_rsi_50_50__above_rsi_50` | 0.41 | -0.03 | +0.08 | -0.17 | 30 |
| `weekly_rsi_50_50__below_rsi_50` | 0.52 | +0.03 | -0.08 | +0.13 | 65 |


<!-- market-read -->

## Market read

Monday split the market in two. The Nifty rose about half a percent and closed near 25,290, lifted by consumer staples and banks. Under it, more than two stocks fell for each one that rose. 215 stocks fell four and a half percent or more, against 69 that rose that hard. That is the most hard fallers since 30 October. The count above the 50 day line dropped by 179 to 1,081. That is back under half the market, and it is the same count as one week ago. The short count lost 317 stocks in one session. The long count fell by 77 to 1,053. Small and micro companies took the damage, along with pharma, metals, autos and realty. Turnover stayed ordinary at about 450 crore, so the selling was wide but not heavy. New yearly highs held at 66, and new yearly lows rose to 38. The fear gauge edged up to 15.7. The index says the week began well. The average stock says the repair lost three days of work.

Full brief: briefs/2026-11-16.html
