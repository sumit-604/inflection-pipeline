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
| % above 10 EMA | 68.39 | -8.22 | +22.64 | +38.16 | 86 | 419 |
| % above 20 EMA | 59.28 | -4.28 | +26.27 | +31.71 | 79 | 419 |
| % above 50 EMA | 40.30 | -2.15 | +15.70 | +10.22 | 50 | 419 |
| % above 200 EMA | 37.61 | -1.23 | +7.10 | -0.35 | 46 | 419 |
| Net breadth (4% adv minus dec) | 0.43 | -8.28 | -3.68 | -3.41 | 31 | 419 |
| 4% advancers | 4.87 | -4.82 | -3.54 | -2.89 | 40 | 419 |
| 4% decliners | 4.44 | +3.46 | +0.14 | +0.52 | 73 | 419 |
| Net new highs minus lows | 0.92 | +0.33 | +1.56 | +2.18 | 58 | 419 |
| Net within 15% of 52wk H/L | -8.22 | -0.86 | +13.94 | +4.44 | 44 | 419 |
| Volume expansion ratio | 0.29 | +0.26 | -0.24 | -0.01 | 11 | 419 |
| Overbought count (weekly RSI>70) | 81.00 | -2.00 | -53.00 | -105.00 | 29 | 385 |
| Oversold count (weekly RSI<30) | 79.00 | +0.00 | -128.00 | +47.00 | 76 | 385 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__current` | 390.08 | -259.45 | 1 |
| `drawdowns_peaks__blw_3` | 231.00 | +188.00 | 76 |
| `4_advance_decline_today__4_decline` | 115.00 | -114.00 | 68 |
| `current_previous_yr_volumes_crores__1_yr_back` | 567.85 | +112.09 | 94 |
| `4_advance_decline__4_advance` | 110.00 | -104.00 | 28 |
| `breadth_above_500_trend_reversal__below_20dma` | 869.00 | +80.00 | 28 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,461.00 | -74.00 | 87 |
| `4_advance_decline__4_decline` | 93.00 | +72.00 | 65 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 53.00 | +39.00 | 73 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,250.00 | +38.00 | 61 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 9.81 (percentile 100, range -6.93 to 9.81)
- `current_previous_yr_volumes_crores__1_yr_back` at 567.85 (percentile 94, range 120.18 to 715.72)

Bottom decile of history:

- `volume__volume` at 0.24 (percentile 1, range 0.24 to 1.64)
- `current_previous_yr_volumes_crores__current` at 390.08 (percentile 1, range 378.80 to 956.94)
- `52_wk_high_low_today__new_52_wk_low` at 0.75 (percentile 5, range 0.73 to 14.97)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 14.00 to 53.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.80 | +0.29 | +0.12 | -0.38 | 75 |
| `15_up_10_down__10_in_5d` | 1.36 | +0.50 | -1.06 | -1.18 | 25 |
| `15_up_10_down__15_in_5d` | 3.43 | -0.93 | +1.55 | +1.00 | 85 |
| `3_above_200_ema__pct` | 42.76 | -0.69 | +13.66 | +7.89 | 49 |
| `4_advance_decline__4_advance` | 110.00 | -104.00 | -88.00 | -67.00 | 28 |
| `4_advance_decline__4_decline` | 93.00 | +72.00 | +1.00 | +13.00 | 65 |
| `4_advance_decline_today__4_advance` | 128.00 | +22.00 | -265.00 | -27.00 | 35 |
| `4_advance_decline_today__4_decline` | 115.00 | -114.00 | +8.00 | +48.00 | 68 |
| `4_advance_decline_today__net_breadth` | 0.50 | +5.64 | -10.64 | -3.17 | 32 |
| `52_week_high_low_within_10__high` | 20.08 | +0.06 | +5.52 | +2.77 | 59 |
| `52_week_high_low_within_10__low` | 18.86 | +0.21 | -13.05 | -12.38 | 49 |
| `52_wk_high_low__new_52_wk_high` | 1.75 | -0.67 | +0.59 | +0.15 | 31 |
| `52_wk_high_low__new_52_wk_low` | 0.70 | -0.81 | -1.02 | -2.19 | 28 |
| `52_wk_high_low_today__new_52_wk_high` | 1.69 | +0.13 | +0.38 | +0.65 | 60 |
| `52_wk_high_low_today__new_52_wk_low` | 0.75 | -0.62 | -2.20 | -4.33 | 5 |
| `5_advance_decline_ratio__advance` | 44.60 | +5.60 | -25.70 | -17.57 | 50 |
| `5_advance_decline_ratio__decline` | 54.36 | -5.56 | +25.75 | +17.58 | 52 |
| `above_10ma__pct` | 71.67 | -7.21 | +20.26 | +43.68 | 86 |
| `above_200ma__above_200ma` | 42.95 | -1.10 | +13.38 | +7.47 | 52 |
| `above_20_ema__pct` | 63.51 | -3.34 | +23.99 | +39.44 | 80 |
| `above_20ma__pct` | 63.20 | -3.74 | +23.88 | +38.24 | 82 |
| `above_50_ema__pct` | 46.40 | -2.07 | +19.09 | +19.89 | 48 |
| `above_50ma__above_50ma` | 42.76 | -0.69 | +13.66 | +7.89 | 52 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,048.00 | -15.00 | +285.00 | +125.00 | 69 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,461.00 | -74.00 | +551.00 | +851.00 | 87 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,080.00 | -32.00 | +426.00 | +402.00 | 60 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,282.00 | +21.00 | -283.00 | -131.00 | 65 |
| `breadth_above_500_trend_reversal__below_20dma` | 869.00 | +80.00 | -549.00 | -857.00 | 28 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,250.00 | +38.00 | -423.00 | -408.00 | 61 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 4.00 | +1.00 | +3.00 | -1.00 | 81 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 53.00 | +39.00 | -3.00 | +3.00 | 73 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 28.00 | -4.00 | +13.00 | +5.00 | 82 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 75.00 | -33.00 | -56.00 | -54.00 | 47 |
| `current_previous_yr_volumes_crores__1_yr_back` | 567.85 | +112.09 | -83.04 | +118.58 | 94 |
| `current_previous_yr_volumes_crores__current` | 390.08 | -259.45 | -60.13 | -50.24 | 1 |
| `drawdowns_peaks__blw_3` | 231.00 | +188.00 | +33.00 | +46.00 | 76 |
| `gold_etfs_nifty_1_month_chg__gold` | -6.03 | -0.60 | +4.79 | +0.65 | 30 |
| `gold_etfs_nifty_1_month_chg__nifty` | 9.81 | +2.56 | +9.54 | +15.65 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 68.39 | -8.22 | +22.64 | +38.16 | 86 |
| `mbm_2_0_magnitude__abv_200ma` | 37.61 | -1.23 | +7.10 | -0.35 | 46 |
| `mbm_2_0_magnitude__abv_20ma` | 59.28 | -4.28 | +26.27 | +31.71 | 79 |
| `mbm_2_0_magnitude__abv_50ma` | 40.30 | -2.15 | +15.70 | +10.22 | 50 |
| `mbm_2_0_velocity_advanced__15_52wh` | 16.16 | -0.43 | +4.02 | -2.84 | 44 |
| `mbm_2_0_velocity_advanced__15_52wl` | 24.38 | +0.42 | -9.92 | -7.28 | 56 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 49.81 | -0.17 | -4.85 | +1.34 | 57 |
| `mbm_2_0_velocity_advanced__30_52wh` | 49.14 | -0.88 | +4.68 | -0.08 | 74 |
| `mbm_2_0_velocity_advanced__breakdowns` | 12.38 | -5.47 | +1.80 | +3.07 | 71 |
| `mbm_2_0_velocity_advanced__breakouts` | 12.59 | -22.11 | -14.34 | -8.25 | 33 |
| `mbm_2_0_velocity_advanced__down_close` | 31.53 | +26.57 | -5.13 | -4.51 | 34 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -8.22 | -0.86 | +13.94 | +4.44 | 44 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -0.67 | -0.71 | +9.53 | -1.43 | 53 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 0.92 | +0.33 | +1.56 | +2.18 | 58 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.68 | -0.51 | +0.46 | -0.17 | 55 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 0.76 | -0.84 | -1.10 | -2.35 | 38 |
| `mbm_2_0_velocity_advanced__up_close` | 36.67 | +10.70 | +5.68 | +1.05 | 47 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.66 | +0.43 | +0.08 | -0.40 | 68 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.36 | +0.50 | -1.06 | -1.18 | 36 |
| `mbm_2_0_velocity_basic__15_in_5d` | 3.43 | -0.93 | +1.55 | +1.00 | 83 |
| `mbm_2_0_velocity_basic__3_range` | 38.35 | -9.63 | +10.23 | +2.86 | 44 |
| `mbm_2_0_velocity_basic__4_advance` | 4.87 | -4.82 | -3.54 | -2.89 | 40 |
| `mbm_2_0_velocity_basic__4_decline` | 4.44 | +3.46 | +0.14 | +0.52 | 73 |
| `mbm_2_0_velocity_basic__5d_range` | 1.05 | +0.54 | -0.59 | -2.32 | 13 |
| `mbm_2_0_velocity_basic__net_breadth` | 0.43 | -8.28 | -3.68 | -3.41 | 31 |
| `mbm_2_0_velocity_basic__volume` | 0.29 | +0.26 | -0.24 | -0.01 | 11 |
| `net_breadth__net_breadth` | 0.43 | -8.28 | -3.68 | -3.41 | 29 |
| `net_nh_nl__net_nh_nl` | 0.90 | -0.52 | +1.44 | +2.03 | 41 |
| `new_high_low_bearishness_bullishness__high` | 50.00 | -12.00 | +16.00 | +3.00 | 57 |
| `new_high_low_bearishness_bullishness__low` | 19.00 | +9.00 | -30.00 | -64.00 | 38 |
| `nifty_500_above_below_200_ema__above_200_ema` | 63.58 | -1.81 | +2.62 | -10.46 | 22 |
| `nifty_500_above_below_200_ema__below_200_ema` | 36.42 | +1.81 | -2.62 | +10.46 | 78 |
| `oversold_overbought_rsi__overbought` | 81.00 | -2.00 | -53.00 | -105.00 | 29 |
| `oversold_overbought_rsi__oversold` | 79.00 | +0.00 | -128.00 | +47.00 | 76 |
| `volume__volume` | 0.24 | -1.40 | -0.32 | -0.06 | 1 |
| `weekly_rsi_50_50__above_rsi_50` | 0.40 | -0.01 | +0.10 | -0.12 | 30 |
| `weekly_rsi_50_50__below_rsi_50` | 0.52 | +0.01 | -0.10 | +0.09 | 65 |


<!-- market-read -->

## Market read

Monday was a quiet day, and the refreshed figures make it a slightly better one. The Nifty rose about a quarter of a percent and closed near 25,045. Across the market, 75 stocks rose four and a half percent or more, against 53 that fell that hard. Turnover dropped to about 390 crore, the lowest since mid September. About three stocks traded on heavy volume for every ten on light volume. The loud corner was the government banks, with their index up almost four percent. Pharma rose less than two percent, yet healthcare names took the heavy volume and the largest share of new yearly highs. The repair still stands. More than six stocks in ten sit above the 20 day line. The count above the 200 day line is 1,048, its best level since late September apart from Sunday's short session. Friday's pullback did little damage. The market still waits for heavy money on a wide up day. The fear gauge fell on Monday and stands near 17, up more than half in three months.

Full brief: briefs/2026-11-09.html
