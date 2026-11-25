# Market breadth digest: 2026-11-23

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-23: **75** of 79
- History available: 2019-07-01 to 2026-11-23, 724 dated rows
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 28.09 | -7.43 | -19.05 | +15.16 | 24 | 428 |
| % above 20 EMA | 32.81 | -5.88 | -16.93 | +21.49 | 32 | 428 |
| % above 50 EMA | 31.29 | -3.61 | -9.35 | +18.20 | 34 | 428 |
| % above 200 EMA | 33.75 | -2.56 | -3.97 | +7.93 | 36 | 428 |
| Net breadth (4% adv minus dec) | -2.65 | -0.74 | +6.49 | -5.91 | 18 | 428 |
| 4% advancers | 3.12 | -0.05 | -0.93 | -6.91 | 16 | 428 |
| 4% decliners | 5.77 | +0.69 | -7.42 | -1.00 | 81 | 428 |
| Net new highs minus lows | -0.55 | -0.08 | -1.40 | +9.99 | 33 | 428 |
| Net within 15% of 52wk H/L | -12.88 | -4.03 | -6.34 | +16.40 | 33 | 428 |
| Volume expansion ratio | 0.30 | -0.11 | -0.23 | -0.10 | 13 | 428 |
| Overbought count (weekly RSI>70) | 81.00 | -42.00 | +24.00 | -138.00 | 28 | 387 |
| Oversold count (weekly RSI<30) | 112.00 | +0.00 | -232.00 | +84.00 | 83 | 387 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `breadth_above_500_trend_reversal__above_20dma` | 916.00 | -134.00 | 47 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,415.00 | +133.00 | 72 |
| `breadth_above_500_trend_reversal__above_50dma` | 901.00 | -81.00 | 48 |
| `current_previous_yr_volumes_crores__1_yr_back` | 491.67 | -80.98 | 82 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,431.00 | +80.00 | 78 |
| `current_previous_yr_volumes_crores__current` | 488.42 | -79.69 | 40 |
| `breadth_above_500_trend_reversal__above_200dma` | 965.00 | -54.00 | 53 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,367.00 | +53.00 | 75 |
| `oversold_overbought_rsi__overbought` | 81.00 | -42.00 | 28 |
| `drawdowns_peaks__blw_3` | 372.00 | +31.00 | 86 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 12.91 (percentile 97, range -6.93 to 17.31)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__gold` at -15.95 (percentile 1, range -15.95 to 14.14)
- `15_up_10_down__15_in_5d` at 0.66 (percentile 3, range 0.63 to 7.11)
- `breadth_above_500_trend_reversal__up_20_in_5d` at 3.00 (percentile 4, range 1.00 to 388.00)
- `mbm_2_0_velocity_basic__15_in_5d` at 0.66 (percentile 4, range 0.23 to 42.62)
- `mbm_2_0_velocity_advanced__up_close` at 24.54 (percentile 9, range 14.46 to 75.03)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.78 | +0.23 | +0.08 | -3.92 | 81 |
| `15_up_10_down__10_in_5d` | 4.33 | -1.77 | +2.19 | -23.57 | 86 |
| `15_up_10_down__15_in_5d` | 0.66 | -0.04 | -1.24 | +0.04 | 3 |
| `3_above_200_ema__pct` | 39.36 | -2.54 | -3.88 | +16.00 | 39 |
| `4_advance_decline__4_advance` | 80.00 | -1.00 | -24.00 | -176.00 | 12 |
| `4_advance_decline__4_decline` | 148.00 | +18.00 | -191.00 | -25.00 | 83 |
| `4_advance_decline_today__4_advance` | 80.00 | -3.00 | -25.00 | +25.00 | 18 |
| `4_advance_decline_today__4_decline` | 150.00 | +14.00 | -193.00 | -484.00 | 69 |
| `4_advance_decline_today__net_breadth` | -2.72 | -0.66 | +6.50 | +21.53 | 31 |
| `52_week_high_low_within_10__high` | 18.91 | -1.31 | -1.16 | +12.14 | 46 |
| `52_week_high_low_within_10__low` | 24.05 | +1.99 | +5.30 | -12.95 | 65 |
| `52_wk_high_low__new_52_wk_high` | 2.57 | +0.38 | +0.43 | +2.24 | 65 |
| `52_wk_high_low__new_52_wk_low` | 1.95 | -0.27 | +0.72 | -7.90 | 73 |
| `52_wk_high_low_today__new_52_wk_high` | 2.54 | +0.38 | +0.41 | +2.22 | 88 |
| `52_wk_high_low_today__new_52_wk_low` | 1.94 | -0.42 | +0.70 | -13.03 | 43 |
| `5_advance_decline_ratio__advance` | 27.93 | -11.51 | -2.87 | +13.31 | 24 |
| `5_advance_decline_ratio__decline` | 71.06 | +11.51 | +2.87 | -13.29 | 78 |
| `above_10ma__pct` | 33.41 | -7.63 | -18.07 | +19.31 | 29 |
| `above_200ma__above_200ma` | 39.36 | -2.54 | -3.88 | +16.00 | 39 |
| `above_20_ema__pct` | 39.26 | -5.34 | -15.40 | +27.65 | 39 |
| `above_20ma__pct` | 39.26 | -5.34 | -15.40 | +27.65 | 40 |
| `above_50_ema__pct` | 38.12 | -3.51 | -8.59 | +25.66 | 36 |
| `above_50ma__above_50ma` | 39.36 | -2.54 | -3.88 | +16.00 | 39 |
| `breadth_above_500_trend_reversal__above_200dma` | 965.00 | -54.00 | -88.00 | +334.00 | 53 |
| `breadth_above_500_trend_reversal__above_20dma` | 916.00 | -134.00 | -357.00 | +644.00 | 47 |
| `breadth_above_500_trend_reversal__above_50dma` | 901.00 | -81.00 | -181.00 | +587.00 | 48 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,367.00 | +53.00 | +83.00 | -345.00 | 75 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,415.00 | +133.00 | +351.00 | -656.00 | 72 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,431.00 | +80.00 | +176.00 | -598.00 | 78 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 3.00 | -3.00 | +0.00 | -29.00 | 73 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 75.00 | -7.00 | -143.00 | -2.00 | 83 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 3.00 | -2.00 | -13.00 | -5.00 | 4 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 47.00 | +1.00 | -21.00 | -117.00 | 22 |
| `current_previous_yr_volumes_crores__1_yr_back` | 491.67 | -80.98 | +121.99 | +57.74 | 82 |
| `current_previous_yr_volumes_crores__current` | 488.42 | -79.69 | +38.69 | -57.33 | 40 |
| `drawdowns_peaks__blw_3` | 372.00 | +31.00 | -216.00 | +112.00 | 86 |
| `gold_etfs_nifty_1_month_chg__gold` | -15.95 | -0.10 | -6.58 | -8.28 | 1 |
| `gold_etfs_nifty_1_month_chg__nifty` | 12.91 | -4.40 | -0.03 | +16.07 | 97 |
| `mbm_2_0_magnitude__abv_10ma` | 28.09 | -7.43 | -19.05 | +15.16 | 24 |
| `mbm_2_0_magnitude__abv_200ma` | 33.75 | -2.56 | -3.97 | +7.93 | 36 |
| `mbm_2_0_magnitude__abv_20ma` | 32.81 | -5.88 | -16.93 | +21.49 | 32 |
| `mbm_2_0_magnitude__abv_50ma` | 31.29 | -3.61 | -9.35 | +18.20 | 34 |
| `mbm_2_0_velocity_advanced__15_52wh` | 15.57 | -1.49 | -1.48 | +7.38 | 40 |
| `mbm_2_0_velocity_advanced__15_52wl` | 28.44 | +2.54 | +4.85 | -9.02 | 66 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.26 | +1.20 | +2.60 | -5.38 | 54 |
| `mbm_2_0_velocity_advanced__30_52wh` | 44.67 | -0.67 | -1.84 | +6.66 | 45 |
| `mbm_2_0_velocity_advanced__breakdowns` | 16.04 | +0.70 | -8.41 | -3.63 | 81 |
| `mbm_2_0_velocity_advanced__breakouts` | 12.72 | +2.66 | +0.26 | -13.22 | 33 |
| `mbm_2_0_velocity_advanced__down_close` | 36.01 | +2.85 | -17.97 | +1.55 | 60 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -12.88 | -4.03 | -6.34 | +16.40 | 33 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -3.59 | -1.87 | -4.45 | +12.05 | 45 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.55 | -0.08 | -1.40 | +9.99 | 33 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.68 | +0.23 | -0.50 | +1.40 | 54 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 2.22 | +0.31 | +0.90 | -8.59 | 70 |
| `mbm_2_0_velocity_advanced__up_close` | 24.54 | -6.98 | -7.96 | -14.13 | 9 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.78 | +0.23 | +0.08 | -3.92 | 75 |
| `mbm_2_0_velocity_basic__10_in_5d` | 4.33 | -1.77 | +2.19 | -23.57 | 82 |
| `mbm_2_0_velocity_basic__15_in_5d` | 0.66 | -0.04 | -1.24 | +0.04 | 4 |
| `mbm_2_0_velocity_basic__3_range` | 31.37 | -10.18 | -0.00 | +14.64 | 28 |
| `mbm_2_0_velocity_basic__4_advance` | 3.12 | -0.05 | -0.93 | -6.91 | 16 |
| `mbm_2_0_velocity_basic__4_decline` | 5.77 | +0.69 | -7.42 | -1.00 | 81 |
| `mbm_2_0_velocity_basic__5d_range` | 5.46 | +0.18 | +1.88 | +4.87 | 53 |
| `mbm_2_0_velocity_basic__net_breadth` | -2.65 | -0.74 | +6.49 | -5.91 | 18 |
| `mbm_2_0_velocity_basic__volume` | 0.30 | -0.11 | -0.23 | -0.10 | 13 |
| `net_breadth__net_breadth` | -2.65 | -0.74 | +6.49 | -5.91 | 15 |
| `net_nh_nl__net_nh_nl` | -0.55 | -0.08 | -1.40 | +9.99 | 22 |
| `new_high_low_bearishness_bullishness__high` | 79.00 | +12.00 | +13.00 | +69.00 | 86 |
| `new_high_low_bearishness_bullishness__low` | 60.00 | -8.00 | +22.00 | -241.00 | 72 |
| `nifty_500_above_below_200_ema__above_200_ema` | 64.59 | -0.60 | +11.47 | -11.47 | 23 |
| `nifty_500_above_below_200_ema__below_200_ema` | 35.41 | +0.60 | -11.47 | +11.47 | 78 |
| `oversold_overbought_rsi__overbought` | 81.00 | -42.00 | +24.00 | -138.00 | 28 |
| `oversold_overbought_rsi__oversold` | 112.00 | +0.00 | -232.00 | +84.00 | 83 |
| `volume__volume` | 0.30 | -0.11 | -0.23 | -0.10 | 12 |
| `weekly_rsi_50_50__above_rsi_50` | 0.37 | -0.01 | +0.20 | -0.17 | 28 |
| `weekly_rsi_50_50__below_rsi_50` | 0.60 | +0.06 | -0.15 | +0.18 | 72 |


<!-- market-read -->

## Market read

This is the picture of Monday 23 November, the latest session on record. On Friday the banks carried the index while the average stock fell. On Monday the banks fell too. The Nifty lost about one and three quarter percent and closed near 25,350. The three bank indices each lost more than three percent, and metals lost more. About seven stocks in ten closed lower. The count of stocks above their long trend line fell to 965, the first close under 1,000 since the first week of November. The Friday brief named that level as the line where the hopeful view starts to fail. The short and middle counts fell further and now sit near 900 each. Yet the day was a slide, not a rout. Only 75 stocks fell hard, turnover was lower than Friday, and fear rose only a little. The bounce off the October low has now given back about a third of its climb. The question for the coming sessions has changed. Last week it asked whether the members would follow the banks up. Monday answered the other way, and the open question now is how far.

Full brief: briefs/2026-11-23.html
