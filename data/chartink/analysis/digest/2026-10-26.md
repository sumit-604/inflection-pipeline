# Market breadth digest: 2026-10-26

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-26: **75** of 79
- History available: 2019-07-01 to 2026-10-26, 704 dated rows
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 12.35 | +5.31 | -28.47 | -25.87 | 4 | 408 |
| % above 20 EMA | 10.71 | +3.00 | -22.95 | -26.33 | 3 | 408 |
| % above 50 EMA | 12.52 | +1.40 | -18.82 | -27.18 | 6 | 408 |
| % above 200 EMA | 25.62 | +0.64 | -13.47 | -18.63 | 22 | 408 |
| Net breadth (4% adv minus dec) | 3.15 | +27.50 | -1.19 | +6.06 | 56 | 408 |
| 4% advancers | 9.45 | +7.22 | +2.42 | +5.78 | 85 | 408 |
| 4% decliners | 6.30 | -20.28 | +3.60 | -0.27 | 83 | 408 |
| Net new highs minus lows | -11.47 | +5.97 | -10.88 | -11.13 | 6 | 408 |
| Net within 15% of 52wk H/L | -31.54 | +1.86 | -20.84 | -32.34 | 13 | 408 |
| Volume expansion ratio | 0.42 | -0.86 | +0.07 | +0.02 | 43 | 408 |
| Overbought count (weekly RSI>70) | 49.00 | -7.00 | -152.00 | -115.00 | 17 | 383 |
| Oversold count (weekly RSI<30) | 297.00 | -53.00 | +215.00 | +260.00 | 94 | 383 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 227.00 | -862.00 | 75 |
| `4_advance_decline_today__4_decline` | 151.00 | -483.00 | 67 |
| `4_advance_decline__4_decline` | 150.00 | -481.00 | 88 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 73.00 | -286.00 | 83 |
| `4_advance_decline__4_advance` | 225.00 | +172.00 | 91 |
| `4_advance_decline_today__4_advance` | 226.00 | +171.00 | 93 |
| `new_high_low_bearishness_bullishness__low` | 304.00 | -149.00 | 96 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 144.00 | +119.00 | 86 |
| `current_previous_yr_volumes_crores__current` | 519.15 | -91.47 | 57 |
| `breadth_above_500_trend_reversal__above_20dma` | 254.00 | +76.00 | 3 |

## At the edge of their own range

Top decile of history:

- `15_up_10_down__10_in_5d` at 28.14 (percentile 100, range 0.34 to 28.14)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 27.00 (percentile 100, range 0.00 to 33.00)
- `breadth_above_500_trend_reversal__below_20dma` at 1,987.00 (percentile 100, range 76.00 to 2,061.00)
- `breadth_above_500_trend_reversal__below_50dma` at 1,955.00 (percentile 100, range 270.00 to 1,987.00)
- `mbm_2_0_velocity_basic__10_in_5d` at 28.14 (percentile 100, range 0.18 to 37.65)
- `10_from_10dema__10_10ema` at 4.79 (percentile 99, range 0.09 to 7.08)
- `mbm_2_0_velocity_basic__10_10ema` at 4.79 (percentile 98, range 0.00 to 16.97)
- `52_wk_high_low__new_52_wk_low` at 10.59 (percentile 98, range 0.18 to 15.84)
- `new_high_low_bearishness_bullishness__low` at 304.00 (percentile 96, range 1.00 to 913.00)
- `mbm_2_0_velocity_advanced__new_52_wk_low` at 11.72 (percentile 94, range 0.00 to 39.05)
- `breadth_above_500_trend_reversal__below_200dma` at 1,644.00 (percentile 94, range 638.00 to 1,812.00)
- `oversold_overbought_rsi__oversold` at 297.00 (percentile 94, range 2.00 to 872.00)
- `4_advance_decline_today__4_advance` at 226.00 (percentile 93, range 33.00 to 296.00)
- `52_wk_high_low_today__new_52_wk_low` at 9.99 (percentile 93, range 0.85 to 14.97)
- `4_advance_decline__4_advance` at 225.00 (percentile 91, range 30.00 to 479.00)
- `weekly_rsi_50_50__below_rsi_50` at 0.78 (percentile 90, range 0.04 to 0.96)

Bottom decile of history:

- `15_up_10_down__15_in_5d` at 0.63 (percentile 1, range 0.63 to 7.11)
- `mbm_2_0_velocity_advanced__new_52_wk_high` at 0.25 (percentile 2, range 0.15 to 4.76)
- `above_20_ema__pct` at 11.08 (percentile 2, range 6.35 to 96.00)
- `breadth_above_500_trend_reversal__above_20dma` at 254.00 (percentile 3, range 119.00 to 2,033.00)
- `mbm_2_0_magnitude__abv_20ma` at 10.71 (percentile 3, range 5.26 to 95.55)
- `52_wk_high_low__new_52_wk_high` at 0.31 (percentile 3, range 0.28 to 5.21)
- `net_nh_nl__net_nh_nl` at -11.47 (percentile 3, range -17.44 to 3.67)
- `above_20ma__pct` at 11.08 (percentile 3, range 7.00 to 96.00)
- `mbm_2_0_magnitude__abv_10ma` at 12.35 (percentile 4, range 6.70 to 96.14)
- `mbm_2_0_velocity_basic__15_in_5d` at 0.63 (percentile 4, range 0.23 to 42.59)
- `new_high_low_bearishness_bullishness__high` at 9.00 (percentile 4, range 5.00 to 148.00)
- `above_50_ema__pct` at 11.95 (percentile 4, range 7.90 to 85.55)
- `mbm_2_0_velocity_basic__5d_range` at 0.59 (percentile 5, range 0.32 to 19.44)
- `above_10ma__pct` at 13.66 (percentile 5, range 7.00 to 96.53)
- `breadth_above_500_trend_reversal__above_50dma` at 286.00 (percentile 5, range 121.00 to 1,873.00)
- `mbm_2_0_magnitude__abv_50ma` at 12.52 (percentile 6, range 4.10 to 84.34)
- `mbm_2_0_velocity_advanced__net_nh_nl` at -11.47 (percentile 6, range -38.73 to 4.72)
- `52_week_high_low_within_10__high` at 7.18 (percentile 7, range 3.64 to 28.39)
- `mbm_2_0_velocity_basic__3_range` at 16.67 (percentile 8, range 7.46 to 63.04)
- `52_wk_high_low_today__new_52_wk_high` at 0.36 (percentile 10, range 0.32 to 3.65)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed up through 50: 25.00 to 144.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 4.79 | -2.29 | +3.95 | +4.58 | 99 |
| `15_up_10_down__10_in_5d` | 28.14 | +0.30 | +26.67 | +27.17 | 100 |
| `15_up_10_down__15_in_5d` | 0.63 | -0.13 | -1.73 | -2.49 | 1 |
| `3_above_200_ema__pct` | 23.07 | +0.47 | -13.99 | -21.02 | 12 |
| `4_advance_decline__4_advance` | 225.00 | +172.00 | +58.00 | +138.00 | 91 |
| `4_advance_decline__4_decline` | 150.00 | -481.00 | +86.00 | -6.00 | 88 |
| `4_advance_decline_today__4_advance` | 226.00 | +171.00 | +56.00 | -10.00 | 93 |
| `4_advance_decline_today__4_decline` | 151.00 | -483.00 | +85.00 | +115.00 | 67 |
| `4_advance_decline_today__net_breadth` | 3.14 | +27.39 | -1.21 | -5.22 | 57 |
| `52_week_high_low_within_10__high` | 7.18 | +1.20 | -10.35 | -17.09 | 7 |
| `52_week_high_low_within_10__low` | 39.48 | -0.85 | +11.28 | +17.00 | 89 |
| `52_wk_high_low__new_52_wk_high` | 0.31 | +0.03 | -1.09 | -1.51 | 3 |
| `52_wk_high_low__new_52_wk_low` | 10.59 | -5.25 | +8.56 | +8.39 | 98 |
| `52_wk_high_low_today__new_52_wk_high` | 0.36 | +0.03 | -1.01 | -2.25 | 10 |
| `52_wk_high_low_today__new_52_wk_low` | 9.99 | -4.98 | +7.91 | +9.15 | 93 |
| `5_advance_decline_ratio__advance` | 59.83 | +45.21 | +0.72 | -7.70 | 87 |
| `5_advance_decline_ratio__decline` | 39.13 | -45.21 | -0.72 | +7.70 | 17 |
| `above_10ma__pct` | 13.66 | +5.96 | -29.27 | -20.27 | 5 |
| `above_200ma__above_200ma` | 23.07 | +0.47 | -13.99 | -21.02 | 13 |
| `above_20_ema__pct` | 11.08 | +2.86 | -23.07 | -21.62 | 2 |
| `above_20ma__pct` | 11.08 | +2.86 | -23.07 | -21.62 | 3 |
| `above_50_ema__pct` | 11.95 | +1.25 | -17.06 | -23.48 | 4 |
| `above_50ma__above_50ma` | 23.07 | +0.47 | -13.99 | -21.02 | 13 |
| `breadth_above_500_trend_reversal__above_200dma` | 597.00 | +20.00 | -338.00 | -486.00 | 18 |
| `breadth_above_500_trend_reversal__above_20dma` | 254.00 | +76.00 | -543.00 | -525.00 | 3 |
| `breadth_above_500_trend_reversal__above_50dma` | 286.00 | +34.00 | -423.00 | -561.00 | 5 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,644.00 | -18.00 | +340.00 | +488.00 | 94 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,987.00 | -74.00 | +545.00 | +527.00 | 100 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,955.00 | -32.00 | +425.00 | +563.00 | 100 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 27.00 | +1.00 | +26.00 | +24.00 | 100 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 73.00 | -286.00 | +38.00 | -14.00 | 83 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 8.00 | +1.00 | -16.00 | -23.00 | 25 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 144.00 | +119.00 | +41.00 | +91.00 | 86 |
| `current_previous_yr_volumes_crores__1_yr_back` | 434.33 | +3.18 | +4.36 | -52.53 | 58 |
| `current_previous_yr_volumes_crores__current` | 519.15 | -91.47 | -77.50 | +34.39 | 57 |
| `drawdowns_peaks__blw_3` | 227.00 | -862.00 | +107.00 | -119.00 | 75 |
| `gold_etfs_nifty_1_month_chg__gold` | -7.67 | +0.30 | -5.03 | -5.37 | 20 |
| `gold_etfs_nifty_1_month_chg__nifty` | -3.16 | +1.22 | -0.39 | +1.76 | 28 |
| `mbm_2_0_magnitude__abv_10ma` | 12.35 | +5.31 | -28.47 | -25.87 | 4 |
| `mbm_2_0_magnitude__abv_200ma` | 25.62 | +0.64 | -13.47 | -18.63 | 22 |
| `mbm_2_0_magnitude__abv_20ma` | 10.71 | +3.00 | -22.95 | -26.33 | 3 |
| `mbm_2_0_magnitude__abv_50ma` | 12.52 | +1.40 | -18.82 | -27.18 | 6 |
| `mbm_2_0_velocity_advanced__15_52wh` | 8.74 | +1.36 | -9.88 | -16.34 | 13 |
| `mbm_2_0_velocity_advanced__15_52wl` | 40.28 | -0.50 | +10.96 | +16.00 | 84 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 57.58 | -0.17 | +9.60 | +14.18 | 75 |
| `mbm_2_0_velocity_advanced__30_52wh` | 40.53 | +0.85 | -11.20 | -12.44 | 25 |
| `mbm_2_0_velocity_advanced__breakdowns` | 18.90 | -49.59 | +10.10 | +2.63 | 84 |
| `mbm_2_0_velocity_advanced__breakouts` | 24.99 | +16.06 | +7.55 | +14.83 | 87 |
| `mbm_2_0_velocity_advanced__down_close` | 33.33 | -5.47 | +2.71 | -7.08 | 48 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -31.54 | +1.86 | -20.84 | -32.34 | 13 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -17.05 | +1.02 | -20.80 | -26.62 | 24 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -11.47 | +5.97 | -10.88 | -11.13 | 6 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 0.25 | -0.00 | -1.31 | -1.69 | 2 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 11.72 | -5.97 | +9.57 | +9.44 | 94 |
| `mbm_2_0_velocity_advanced__up_close` | 37.82 | +12.82 | -2.52 | +1.72 | 52 |
| `mbm_2_0_velocity_basic__10_10ema` | 4.79 | -2.29 | +3.95 | +4.58 | 98 |
| `mbm_2_0_velocity_basic__10_in_5d` | 28.14 | +0.30 | +26.67 | +27.17 | 100 |
| `mbm_2_0_velocity_basic__15_in_5d` | 0.63 | -0.13 | -1.73 | -2.49 | 4 |
| `mbm_2_0_velocity_basic__3_range` | 16.67 | +8.33 | -25.58 | -24.92 | 8 |
| `mbm_2_0_velocity_basic__4_advance` | 9.45 | +7.22 | +2.42 | +5.78 | 85 |
| `mbm_2_0_velocity_basic__4_decline` | 6.30 | -20.28 | +3.60 | -0.27 | 83 |
| `mbm_2_0_velocity_basic__5d_range` | 0.59 | -0.21 | -6.36 | -7.67 | 5 |
| `mbm_2_0_velocity_basic__net_breadth` | 3.15 | +27.50 | -1.19 | +6.06 | 56 |
| `mbm_2_0_velocity_basic__volume` | 0.42 | -0.86 | +0.07 | +0.02 | 43 |
| `net_breadth__net_breadth` | 3.15 | +27.50 | -1.19 | +6.06 | 55 |
| `net_nh_nl__net_nh_nl` | -11.47 | +5.97 | -10.88 | -11.13 | 3 |
| `new_high_low_bearishness_bullishness__high` | 9.00 | +1.00 | -31.00 | -43.00 | 4 |
| `new_high_low_bearishness_bullishness__low` | 304.00 | -149.00 | +246.00 | +241.00 | 96 |
| `nifty_500_above_below_200_ema__above_200_ema` | 53.92 | +0.80 | -13.68 | -16.46 | 18 |
| `nifty_500_above_below_200_ema__below_200_ema` | 46.08 | -0.80 | +13.68 | +16.46 | 83 |
| `oversold_overbought_rsi__overbought` | 49.00 | -7.00 | -152.00 | -115.00 | 17 |
| `oversold_overbought_rsi__oversold` | 297.00 | -53.00 | +215.00 | +260.00 | 94 |
| `volume__volume` | 0.42 | -0.86 | +0.07 | +0.02 | 46 |
| `weekly_rsi_50_50__above_rsi_50` | 0.20 | +0.01 | -0.23 | -0.26 | 10 |
| `weekly_rsi_50_50__below_rsi_50` | 0.78 | -0.01 | +0.24 | +0.28 | 90 |


<!-- market-read -->

## Market read

The market bounced on Monday after two heavy down days last week. 144 stocks rose four and a half percent or more, against 73 that fell that much. That is the first day since 16 October when risers beat fallers, and 33 of 35 indices closed up. The bounce came on light volume. Turnover fell well below Friday's, and the share of stocks on heavy volume dropped by about two thirds. The damage underneath barely moved. Only 597 stocks hold their 200 day line, about one in four, up 20 from Friday. 304 stocks still made new yearly lows, against nine new highs. The rally had no thrust behind it. A thrust day needs about 250 or more big risers on heavy turnover, and the last one came on 12 June. Fear rose with the prices: the VIX closed above 17. This is a relief day inside a confirmed slide in breadth, and the slide holds until buying arrives wide, heavy and repeated.

Full brief: briefs/2026-10-26.html
