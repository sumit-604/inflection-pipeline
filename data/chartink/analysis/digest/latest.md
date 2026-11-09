# Market breadth digest: 2026-11-09

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-09: **75** of 79
- History available: 2019-07-01 to 2026-11-09, 715 dated rows
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 68.32 | +7.70 | +27.53 | +44.14 | 86 | 418 |
| % above 20 EMA | 59.06 | +9.20 | +31.16 | +35.16 | 79 | 418 |
| % above 50 EMA | 40.00 | +5.74 | +18.45 | +12.98 | 50 | 418 |
| % above 200 EMA | 37.30 | +2.30 | +8.31 | +0.89 | 45 | 418 |
| Net breadth (4% adv minus dec) | 0.71 | -7.41 | -3.79 | -3.35 | 33 | 419 |
| 4% advancers | 4.61 | -4.39 | -3.77 | -2.80 | 37 | 419 |
| 4% decliners | 3.90 | +3.02 | +0.03 | +0.55 | 68 | 419 |
| Net new highs minus lows | 0.92 | +0.33 | +1.55 | +2.18 | 58 | 419 |
| Net within 15% of 52wk H/L | -8.22 | -0.86 | +13.98 | +4.44 | 44 | 419 |
| Volume expansion ratio | 0.24 | -1.40 | -0.32 | -0.06 | 4 | 419 |
| Overbought count (weekly RSI>70) | 81.00 | -3.00 | -53.00 | -105.00 | 29 | 385 |
| Oversold count (weekly RSI<30) | 79.00 | +0.00 | -128.00 | +48.00 | 76 | 385 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__current` | 390.08 | -259.45 | 1 |
| `drawdowns_peaks__blw_3` | 230.00 | -187.00 | 76 |
| `4_advance_decline_today__4_decline` | 114.00 | -115.00 | 68 |
| `current_previous_yr_volumes_crores__1_yr_back` | 567.85 | +112.09 | 94 |
| `4_advance_decline__4_advance` | 110.00 | -104.00 | 28 |
| `breadth_above_500_trend_reversal__below_20dma` | 843.00 | +76.00 | 27 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,407.00 | -75.00 | 84 |
| `4_advance_decline__4_decline` | 93.00 | +72.00 | 65 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 47.00 | +33.00 | 69 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 68.00 | -32.00 | 42 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 8.18 (percentile 100, range -6.93 to 8.18)
- `current_previous_yr_volumes_crores__1_yr_back` at 567.85 (percentile 94, range 120.18 to 715.72)

Bottom decile of history:

- `volume__volume` at 0.24 (percentile 1, range 0.24 to 1.64)
- `current_previous_yr_volumes_crores__current` at 390.08 (percentile 1, range 378.80 to 956.94)
- `52_wk_high_low_today__new_52_wk_low` at 0.67 (percentile 2, range 0.67 to 14.97)
- `mbm_2_0_velocity_basic__volume` at 0.24 (percentile 4, range 0.03 to 5.68)

## Crossed the 50 line today

- `mbm_2_0_magnitude__abv_20ma` crossed up through 50: 49.86 to 59.06

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.90 | -0.12 | -0.36 | -0.17 | 79 |
| `15_up_10_down__10_in_5d` | 1.43 | +0.42 | -1.06 | -1.21 | 30 |
| `15_up_10_down__15_in_5d` | 3.40 | -0.90 | +1.46 | +1.22 | 87 |
| `3_above_200_ema__pct` | 42.76 | -0.69 | +13.66 | +7.89 | 49 |
| `4_advance_decline__4_advance` | 110.00 | -104.00 | -89.00 | -67.00 | 28 |
| `4_advance_decline__4_decline` | 93.00 | +72.00 | +1.00 | +13.00 | 65 |
| `4_advance_decline_today__4_advance` | 127.00 | +21.00 | -266.00 | -28.00 | 35 |
| `4_advance_decline_today__4_decline` | 114.00 | -115.00 | +7.00 | +47.00 | 68 |
| `4_advance_decline_today__net_breadth` | 0.50 | +5.64 | -10.64 | -3.17 | 32 |
| `52_week_high_low_within_10__high` | 20.08 | +0.06 | +5.52 | +2.77 | 59 |
| `52_week_high_low_within_10__low` | 18.86 | +0.21 | -13.05 | -12.38 | 49 |
| `52_wk_high_low__new_52_wk_high` | 1.66 | +0.16 | +0.38 | +0.67 | 31 |
| `52_wk_high_low__new_52_wk_low` | 0.65 | -0.46 | -2.33 | -4.35 | 25 |
| `52_wk_high_low_today__new_52_wk_high` | 1.69 | +0.12 | +0.37 | +0.64 | 60 |
| `52_wk_high_low_today__new_52_wk_low` | 0.67 | -0.70 | -2.28 | -4.41 | 2 |
| `5_advance_decline_ratio__advance` | 44.60 | +5.60 | -25.70 | -17.57 | 50 |
| `5_advance_decline_ratio__decline` | 54.36 | -5.56 | +25.75 | +17.58 | 52 |
| `above_10ma__pct` | 71.51 | +6.96 | +25.70 | +46.62 | 86 |
| `above_200ma__above_200ma` | 42.76 | -0.69 | +13.66 | +7.89 | 52 |
| `above_20_ema__pct` | 63.01 | +7.93 | +30.19 | +40.97 | 80 |
| `above_20ma__pct` | 63.51 | -3.34 | +23.99 | +39.44 | 82 |
| `above_50_ema__pct` | 46.19 | -1.72 | +19.23 | +20.34 | 48 |
| `above_50ma__above_50ma` | 42.76 | -0.69 | +13.66 | +7.89 | 52 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,003.00 | -15.00 | +276.00 | +122.00 | 62 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,407.00 | -75.00 | +532.00 | +830.00 | 84 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,036.00 | -31.00 | +414.00 | +391.00 | 58 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,247.00 | +16.00 | -275.00 | -136.00 | 61 |
| `breadth_above_500_trend_reversal__below_20dma` | 843.00 | +76.00 | -531.00 | -844.00 | 27 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,214.00 | +32.00 | -412.00 | -405.00 | 57 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 5.00 | +0.00 | +4.00 | -4.00 | 87 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 47.00 | +33.00 | -3.00 | +5.00 | 69 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 25.00 | -6.00 | +10.00 | +5.00 | 78 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 68.00 | -32.00 | -60.00 | -52.00 | 42 |
| `current_previous_yr_volumes_crores__1_yr_back` | 567.85 | +112.09 | -83.04 | +118.58 | 94 |
| `current_previous_yr_volumes_crores__current` | 390.08 | -259.45 | -60.13 | -50.24 | 1 |
| `drawdowns_peaks__blw_3` | 230.00 | -187.00 | +46.00 | +69.00 | 76 |
| `gold_etfs_nifty_1_month_chg__gold` | -6.03 | +0.83 | +3.40 | +1.15 | 30 |
| `gold_etfs_nifty_1_month_chg__nifty` | 8.18 | +2.56 | +8.75 | +13.85 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 68.32 | +7.70 | +27.53 | +44.14 | 86 |
| `mbm_2_0_magnitude__abv_200ma` | 37.30 | +2.30 | +8.31 | +0.89 | 45 |
| `mbm_2_0_magnitude__abv_20ma` | 59.06 | +9.20 | +31.16 | +35.16 | 79 |
| `mbm_2_0_magnitude__abv_50ma` | 40.00 | +5.74 | +18.45 | +12.98 | 50 |
| `mbm_2_0_velocity_advanced__15_52wh` | 16.15 | -0.43 | +4.02 | -2.84 | 44 |
| `mbm_2_0_velocity_advanced__15_52wl` | 24.37 | +0.42 | -9.96 | -7.27 | 56 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 49.83 | -0.17 | -4.84 | +1.34 | 57 |
| `mbm_2_0_velocity_advanced__30_52wh` | 49.12 | -0.88 | +4.68 | -0.08 | 74 |
| `mbm_2_0_velocity_advanced__breakdowns` | 12.37 | -5.51 | +1.80 | +3.03 | 71 |
| `mbm_2_0_velocity_advanced__breakouts` | 12.58 | -22.10 | -14.37 | -8.29 | 33 |
| `mbm_2_0_velocity_advanced__down_close` | 31.53 | +26.58 | -5.13 | -4.35 | 34 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -8.22 | -0.86 | +13.98 | +4.44 | 44 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -0.71 | -0.71 | +9.52 | -1.43 | 53 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 0.92 | +0.33 | +1.55 | +2.18 | 58 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.68 | -0.51 | +0.46 | -0.17 | 55 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 0.76 | -0.84 | -1.10 | -2.35 | 38 |
| `mbm_2_0_velocity_advanced__up_close` | 36.67 | +10.70 | +5.57 | +1.12 | 47 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.80 | +0.29 | +0.12 | -0.38 | 75 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.43 | +0.42 | -1.06 | -1.21 | 39 |
| `mbm_2_0_velocity_basic__15_in_5d` | 3.40 | -0.90 | +1.46 | +1.22 | 83 |
| `mbm_2_0_velocity_basic__3_range` | 39.39 | +29.67 | +10.58 | +3.01 | 48 |
| `mbm_2_0_velocity_basic__4_advance` | 4.61 | -4.39 | -3.77 | -2.80 | 37 |
| `mbm_2_0_velocity_basic__4_decline` | 3.90 | +3.02 | +0.03 | +0.55 | 68 |
| `mbm_2_0_velocity_basic__5d_range` | 1.17 | +0.63 | -0.51 | -2.26 | 14 |
| `mbm_2_0_velocity_basic__net_breadth` | 0.71 | -7.41 | -3.79 | -3.35 | 33 |
| `mbm_2_0_velocity_basic__volume` | 0.24 | -1.40 | -0.32 | -0.06 | 4 |
| `net_breadth__net_breadth` | 0.71 | -7.41 | -3.79 | -3.35 | 30 |
| `net_nh_nl__net_nh_nl` | 0.86 | +0.62 | +2.66 | +5.00 | 42 |
| `new_high_low_bearishness_bullishness__high` | 51.00 | +5.00 | +12.00 | +21.00 | 58 |
| `new_high_low_bearishness_bullishness__low` | 20.00 | -14.00 | -71.00 | -131.00 | 39 |
| `nifty_500_above_below_200_ema__above_200_ema` | 63.58 | -1.81 | +2.62 | -10.46 | 22 |
| `nifty_500_above_below_200_ema__below_200_ema` | 36.42 | +1.81 | -2.62 | +10.46 | 78 |
| `oversold_overbought_rsi__overbought` | 81.00 | -3.00 | -53.00 | -105.00 | 29 |
| `oversold_overbought_rsi__oversold` | 79.00 | +0.00 | -128.00 | +48.00 | 76 |
| `volume__volume` | 0.24 | -1.40 | -0.32 | -0.06 | 1 |
| `weekly_rsi_50_50__above_rsi_50` | 0.40 | -0.01 | +0.10 | -0.12 | 30 |
| `weekly_rsi_50_50__below_rsi_50` | 0.53 | +0.01 | -0.10 | +0.10 | 66 |


<!-- market-read -->

## Market read

Monday was a quiet day with one loud corner. The Nifty barely moved and closed just above 25,000. Across the market, 68 stocks rose four and a half percent or more, against 47 that fell that hard. Turnover dropped to about 390 crore, the lowest since mid September. About one stock traded on heavy volume for every four on light volume. The loud corner was pharma and the government banks, each index up more than three percent. Healthcare names traded at many times their normal volume and took the largest share of new yearly highs. The repair still stands. More than six stocks in ten sit above the 20 day line. The count above the 200 day line passed 1,000 and held there on Monday. It last stood there in late September. Friday's pullback did little damage. The market still waits for heavy money on a wide up day. The fear gauge stands near 17, up more than half in three months.

Full brief: briefs/2026-11-09.html
