# Market breadth digest: 2026-10-21

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-21: **69** of 79
- History available: 2019-07-01 to 2026-10-21, 701 dated rows
- Metrics with no reading for 2026-10-21: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 13.05 | -12.66 | -23.74 | -31.27 | 4 | 405 |
| % above 20 EMA | 13.64 | -9.80 | -16.58 | -25.06 | 5 | 405 |
| % above 50 EMA | 18.18 | -7.19 | -11.99 | -22.36 | 11 | 405 |
| % above 200 EMA | 30.93 | -4.85 | -7.54 | -14.18 | 33 | 405 |
| Net breadth (4% adv minus dec) | -23.74 | -15.46 | -26.81 | -29.69 | 3 | 405 |
| 4% advancers | 1.26 | -1.64 | -4.93 | -7.37 | 2 | 405 |
| 4% decliners | 25.00 | +13.83 | +21.88 | +22.32 | 97 | 405 |
| Net new highs minus lows | -8.67 | -6.11 | -6.61 | -10.01 | 7 | 405 |
| Net within 15% of 52wk H/L | -23.70 | -7.99 | -13.03 | -24.32 | 20 | 405 |
| Volume expansion ratio | 0.65 | +0.36 | +0.35 | +0.22 | 71 | 405 |
| Overbought count (weekly RSI>70) (as of 2026-10-19) | 72.00 | -57.00 | -128.00 | -95.00 | 25 | 382 |
| Oversold count (weekly RSI<30) (as of 2026-10-19) | 223.00 | +91.00 | +141.00 | +192.00 | 92 | 382 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 1,023.00 | +474.00 | 97 |
| `4_advance_decline_today__4_decline` | 597.00 | +330.00 | 100 |
| `4_advance_decline__4_decline` | 594.00 | +328.00 | 100 |
| `breadth_above_500_trend_reversal__above_20dma` | 319.00 | -249.00 | 5 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,933.00 | +249.00 | 100 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 384.00 | +232.00 | 98 |
| `breadth_above_500_trend_reversal__above_50dma` | 408.00 | -159.00 | 9 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,844.00 | +159.00 | 99 |
| `breadth_above_500_trend_reversal__above_200dma` | 720.00 | -133.00 | 26 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,532.00 | +133.00 | 88 |

## At the edge of their own range

Top decile of history:

- `10_from_10dema__10_10ema` at 2.15 (percentile 100, range 0.09 to 2.15)
- `15_up_10_down__10_in_5d` at 9.13 (percentile 100, range 0.34 to 9.13)
- `4_advance_decline__4_decline` at 594.00 (percentile 100, range 22.00 to 594.00)
- `4_advance_decline_today__4_decline` at 597.00 (percentile 100, range 36.00 to 597.00)
- `52_wk_high_low__new_52_wk_low` at 8.29 (percentile 100, range 0.18 to 8.29)
- `52_wk_high_low_today__new_52_wk_low` at 7.91 (percentile 100, range 0.85 to 7.91)
- `breadth_above_500_trend_reversal__below_20dma` at 1,933.00 (percentile 100, range 76.00 to 1,968.00)
- `breadth_above_500_trend_reversal__below_50dma` at 1,844.00 (percentile 99, range 273.00 to 1,945.00)
- `breadth_above_500_trend_reversal__down_4_5_today` at 384.00 (percentile 98, range 1.00 to 956.00)
- `drawdowns_peaks__blw_3` at 1,023.00 (percentile 97, range 21.00 to 1,869.00)
- `mbm_2_0_velocity_advanced__breakdowns` at 48.82 (percentile 97, range 2.47 to 94.86)
- `mbm_2_0_velocity_basic__4_decline` at 25.00 (percentile 97, range 0.28 to 58.22)
- `5_advance_decline_ratio__decline` at 83.63 (percentile 96, range 28.74 to 85.61)
- `mbm_2_0_velocity_advanced__down_close` at 51.21 (percentile 96, range 4.98 to 72.76)
- `mbm_2_0_velocity_basic__10_10ema` at 2.15 (percentile 96, range 0.00 to 16.96)
- `new_high_low_bearishness_bullishness__low` at 237.00 (percentile 95, range 1.00 to 913.00)
- `mbm_2_0_velocity_basic__10_in_5d` at 9.13 (percentile 95, range 0.18 to 37.65)
- `mbm_2_0_velocity_advanced__new_52_wk_low` at 9.47 (percentile 94, range 0.00 to 39.08)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 6.00 (percentile 93, range 0.00 to 33.00)

Bottom decile of history:

- `mbm_2_0_velocity_advanced__up_close` at 14.22 (percentile 0, range 14.22 to 75.03)
- `4_advance_decline__4_advance` at 30.00 (percentile 1, range 30.00 to 479.00)
- `52_wk_high_low__new_52_wk_high` at 0.80 (percentile 1, range 0.80 to 5.21)
- `net_breadth__net_breadth` at -23.74 (percentile 1, range -23.74 to 19.72)
- `net_nh_nl__net_nh_nl` at -8.67 (percentile 1, range -8.67 to 3.67)
- `mbm_2_0_velocity_basic__4_advance` at 1.26 (percentile 2, range 0.91 to 64.61)
- `breadth_above_500_trend_reversal__up_4_5_today` at 18.00 (percentile 3, range 6.00 to 1,126.00)
- `mbm_2_0_velocity_basic__net_breadth` at -23.74 (percentile 3, range -57.32 to 63.88)
- `4_advance_decline_today__4_advance` at 33.00 (percentile 4, range 33.00 to 296.00)
- `4_advance_decline_today__net_breadth` at -23.62 (percentile 4, range -23.62 to 10.36)
- `52_wk_high_low_today__new_52_wk_high` at 0.81 (percentile 4, range 0.81 to 3.65)
- `mbm_2_0_magnitude__abv_10ma` at 13.05 (percentile 4, range 6.70 to 96.14)
- `above_10ma__pct` at 14.10 (percentile 4, range 7.00 to 96.53)
- `above_20_ema__pct` at 14.14 (percentile 4, range 6.35 to 96.00)
- `15_up_10_down__15_in_5d` at 1.18 (percentile 4, range 0.99 to 7.11)
- `breadth_above_500_trend_reversal__above_20dma` at 319.00 (percentile 5, range 119.00 to 2,048.00)
- `mbm_2_0_magnitude__abv_20ma` at 13.64 (percentile 5, range 5.26 to 95.55)
- `mbm_2_0_velocity_basic__3_range` at 14.86 (percentile 5, range 7.44 to 63.10)
- `above_20ma__pct` at 14.14 (percentile 6, range 7.00 to 96.00)
- `mbm_2_0_velocity_advanced__net_nh_nl` at -8.67 (percentile 7, range -38.76 to 4.72)
- `5_advance_decline_ratio__advance` at 15.33 (percentile 7, range 13.35 to 70.21)
- `above_50_ema__pct` at 16.93 (percentile 9, range 7.90 to 85.55)
- `breadth_above_500_trend_reversal__above_50dma` at 408.00 (percentile 9, range 121.00 to 1,888.00)
- `mbm_2_0_velocity_advanced__breakouts` at 8.88 (percentile 10, range 3.51 to 86.12)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 2.15 | +0.80 | +1.09 | +1.73 | 100 |
| `15_up_10_down__10_in_5d` | 9.13 | +5.90 | +6.35 | +6.41 | 100 |
| `15_up_10_down__15_in_5d` | 1.18 | -0.88 | -0.09 | -0.67 | 4 |
| `3_above_200_ema__pct` | 27.96 | -5.52 | -8.14 | -17.83 | 17 |
| `4_advance_decline__4_advance` | 30.00 | -39.00 | -117.00 | -176.00 | 1 |
| `4_advance_decline__4_decline` | 594.00 | +328.00 | +520.00 | +530.00 | 100 |
| `4_advance_decline_today__4_advance` | 33.00 | -38.00 | -116.00 | -36.00 | 4 |
| `4_advance_decline_today__4_decline` | 597.00 | +330.00 | +519.00 | +36.00 | 100 |
| `4_advance_decline_today__net_breadth` | -23.62 | -15.41 | -26.59 | -3.05 | 4 |
| `52_week_high_low_within_10__high` | 10.15 | -4.55 | -8.06 | -14.59 | 13 |
| `52_week_high_low_within_10__low` | 34.39 | +3.99 | +5.23 | +12.47 | 84 |
| `52_wk_high_low__new_52_wk_high` | 0.80 | -0.69 | -0.63 | -2.05 | 1 |
| `52_wk_high_low__new_52_wk_low` | 8.29 | +4.64 | +4.86 | +6.62 | 100 |
| `52_wk_high_low_today__new_52_wk_high` | 0.81 | -0.65 | -0.59 | -1.07 | 4 |
| `52_wk_high_low_today__new_52_wk_low` | 7.91 | +4.43 | +4.52 | +4.23 | 100 |
| `5_advance_decline_ratio__advance` | 15.33 | -5.60 | -45.54 | -0.43 | 7 |
| `5_advance_decline_ratio__decline` | 83.63 | +5.60 | +45.54 | +0.43 | 96 |
| `above_10ma__pct` | 14.10 | -13.35 | -24.31 | -29.08 | 4 |
| `above_200ma__above_200ma` | 27.96 | -5.52 | -8.14 | -17.83 | 17 |
| `above_20_ema__pct` | 14.14 | -9.93 | -14.33 | -21.42 | 4 |
| `above_20ma__pct` | 14.14 | -9.93 | -14.33 | -21.42 | 6 |
| `above_50_ema__pct` | 16.93 | -6.33 | -10.17 | -21.20 | 9 |
| `above_50ma__above_50ma` | 27.96 | -5.52 | -8.14 | -17.83 | 17 |
| `breadth_above_500_trend_reversal__above_200dma` | 720.00 | -133.00 | -186.00 | -411.00 | 26 |
| `breadth_above_500_trend_reversal__above_20dma` | 319.00 | -249.00 | -349.00 | -530.00 | 5 |
| `breadth_above_500_trend_reversal__above_50dma` | 408.00 | -159.00 | -262.00 | -527.00 | 9 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,532.00 | +133.00 | +189.00 | +410.00 | 88 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,933.00 | +249.00 | +352.00 | +529.00 | 100 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,844.00 | +159.00 | +265.00 | +526.00 | 99 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 6.00 | +2.00 | +0.00 | +6.00 | 93 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 384.00 | +232.00 | +355.00 | +355.00 | 98 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 9.00 | -7.00 | -4.00 | -8.00 | 27 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 18.00 | -26.00 | -81.00 | -129.00 | 3 |
| `current_previous_yr_volumes_crores__1_yr_back` | 457.00 | -23.66 | +12.69 | +36.47 | 72 |
| `current_previous_yr_volumes_crores__current` | 557.97 | +44.01 | +142.93 | +121.07 | 75 |
| `drawdowns_peaks__blw_3` | 1,023.00 | +474.00 | +874.00 | +886.00 | 97 |
| `gold_etfs_nifty_1_month_chg__gold` | -7.11 | -2.10 | +0.29 | -8.79 | 24 |
| `gold_etfs_nifty_1_month_chg__nifty` | -4.36 | -0.65 | +0.40 | -0.90 | 15 |
| `mbm_2_0_magnitude__abv_10ma` | 13.05 | -12.66 | -23.74 | -31.27 | 4 |
| `mbm_2_0_magnitude__abv_200ma` | 30.93 | -4.85 | -7.54 | -14.18 | 33 |
| `mbm_2_0_magnitude__abv_20ma` | 13.64 | -9.80 | -16.58 | -25.06 | 5 |
| `mbm_2_0_magnitude__abv_50ma` | 18.18 | -7.19 | -11.99 | -22.36 | 11 |
| `mbm_2_0_velocity_advanced__15_52wh` | 11.11 | -4.55 | -8.61 | -13.50 | 19 |
| `mbm_2_0_velocity_advanced__15_52wl` | 34.81 | +3.43 | +4.42 | +10.82 | 75 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 52.74 | +3.26 | +4.48 | +9.47 | 66 |
| `mbm_2_0_velocity_advanced__30_52wh` | 45.75 | -3.85 | -4.95 | -7.29 | 51 |
| `mbm_2_0_velocity_advanced__breakdowns` | 48.82 | +23.96 | +36.22 | +40.35 | 97 |
| `mbm_2_0_velocity_advanced__breakouts` | 8.88 | -1.79 | -5.49 | -8.65 | 10 |
| `mbm_2_0_velocity_advanced__down_close` | 51.21 | +6.27 | +26.46 | +19.52 | 96 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -23.70 | -7.99 | -13.03 | -24.32 | 20 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -6.99 | -7.11 | -9.43 | -16.76 | 39 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -8.67 | -6.11 | -6.61 | -10.01 | 7 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 0.80 | -0.84 | -0.76 | -2.34 | 21 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 9.47 | +5.27 | +5.85 | +7.67 | 94 |
| `mbm_2_0_velocity_advanced__up_close` | 14.22 | -12.95 | -28.89 | -35.06 | 0 |
| `mbm_2_0_velocity_basic__10_10ema` | 2.15 | +0.80 | +1.09 | +1.73 | 96 |
| `mbm_2_0_velocity_basic__10_in_5d` | 9.13 | +5.90 | +6.35 | +6.41 | 95 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.18 | -0.88 | -0.09 | -0.67 | 22 |
| `mbm_2_0_velocity_basic__3_range` | 14.86 | -15.63 | -23.32 | -26.65 | 5 |
| `mbm_2_0_velocity_basic__4_advance` | 1.26 | -1.64 | -4.93 | -7.37 | 2 |
| `mbm_2_0_velocity_basic__4_decline` | 25.00 | +13.83 | +21.88 | +22.32 | 97 |
| `mbm_2_0_velocity_basic__5d_range` | 2.27 | -3.31 | -1.69 | -1.00 | 26 |
| `mbm_2_0_velocity_basic__net_breadth` | -23.74 | -15.46 | -26.81 | -29.69 | 3 |
| `mbm_2_0_velocity_basic__volume` | 0.65 | +0.36 | +0.35 | +0.22 | 71 |
| `net_breadth__net_breadth` | -23.74 | -15.46 | -26.81 | -29.69 | 1 |
| `net_nh_nl__net_nh_nl` | -8.67 | -6.11 | -6.61 | -10.01 | 1 |
| `new_high_low_bearishness_bullishness__high` | 23.00 | -20.00 | -18.00 | -59.00 | 18 |
| `new_high_low_bearishness_bullishness__low` | 237.00 | +132.00 | +139.00 | +189.00 | 95 |
| `volume__volume` | 0.65 | +0.36 | +0.35 | +0.22 | 86 |

## No reading for 2026-10-21

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-19, 58.15
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-19, 41.85
- `oversold_overbought_rsi__overbought`: last 2026-10-19, 72.00
- `oversold_overbought_rsi__oversold`: last 2026-10-19, 223.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-19, 0.25
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-19, 0.73


<!-- market-read -->

## Market read

Wednesday broke the autumn floor, and it broke it hard. Only 720 stocks now hold their 200 day line. The 8 October low was 838. The count has not been this low since mid April. 384 stocks fell four and a half percent or more, and only 18 rose that much. That is the heaviest down day since 12 May, heavier than both autumn shocks. This time the volume was heavy too, so the selling looks forced and not only a markdown. New yearly lows rose to 237, the most since late March. The Nifty fell only a third of a percent, because IT and a few large names held it up. Under the index, about two stocks in three now sit in long downtrends. The staircase of lower peaks now has a lower low under it. That is the shape of a downtrend, and it stays that way until a broad burst of buying says otherwise.

Full brief: briefs/2026-10-21.html
