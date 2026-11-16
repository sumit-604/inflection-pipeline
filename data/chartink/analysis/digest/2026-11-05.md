# Market breadth digest: 2026-11-05

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-05: **69** of 79
- History available: 2019-07-01 to 2026-11-05, 712 dated rows
- Metrics with no reading for 2026-11-05: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 73.84 | +6.87 | +36.60 | +35.40 | 90 | 416 |
| % above 20 EMA | 58.72 | +10.68 | +34.25 | +25.16 | 79 | 416 |
| % above 50 EMA | 38.75 | +7.84 | +17.31 | +3.72 | 47 | 416 |
| % above 200 EMA | 36.31 | +2.11 | +6.53 | -5.00 | 43 | 416 |
| Net breadth (4% adv minus dec) | 11.75 | -3.85 | +5.01 | +8.13 | 92 | 416 |
| 4% advancers | 14.91 | -3.22 | +5.27 | +8.72 | 93 | 416 |
| 4% decliners | 3.16 | +0.63 | +0.25 | +0.59 | 58 | 416 |
| Net new highs minus lows | 1.90 | +1.85 | +3.24 | +2.44 | 82 | 416 |
| Net within 15% of 52wk H/L | -9.65 | +6.13 | +13.90 | -1.94 | 40 | 416 |
| Volume expansion ratio | 1.52 | +0.80 | +1.16 | +1.17 | 94 | 416 |
| Overbought count (weekly RSI>70) (as of 2026-11-02) | 77.00 | +15.00 | -72.00 | -127.00 | 27 | 384 |
| Oversold count (weekly RSI<30) (as of 2026-11-02) | 92.00 | -192.00 | -63.00 | +68.00 | 79 | 384 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `breadth_above_500_trend_reversal__above_20dma` | 1,444.00 | +229.00 | 85 |
| `breadth_above_500_trend_reversal__below_20dma` | 810.00 | -227.00 | 25 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,016.00 | +179.00 | 56 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,238.00 | -177.00 | 59 |
| `breadth_above_500_trend_reversal__above_200dma` | 977.00 | +104.00 | 55 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,277.00 | -102.00 | 64 |
| `4_advance_decline__4_advance` | 381.00 | -79.00 | 96 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 233.00 | -76.00 | 94 |
| `4_advance_decline_today__4_advance` | 382.00 | -48.00 | 92 |
| `current_previous_yr_volumes_crores__current` | 571.67 | +39.81 | 79 |

## At the edge of their own range

Top decile of history:

- `volume__volume` at 1.40 (percentile 100, range 0.24 to 1.40)
- `5_advance_decline_ratio__advance` at 70.81 (percentile 97, range 13.35 to 77.29)
- `4_advance_decline__4_advance` at 381.00 (percentile 96, range 34.00 to 479.00)
- `net_breadth__net_breadth` at 11.35 (percentile 96, range -24.74 to 19.72)
- `mbm_2_0_velocity_advanced__breakouts` at 40.31 (percentile 96, range 3.51 to 86.12)
- `mbm_2_0_velocity_basic__volume` at 1.52 (percentile 94, range 0.03 to 5.71)
- `breadth_above_500_trend_reversal__up_4_5_today` at 233.00 (percentile 94, range 6.00 to 1,125.00)
- `mbm_2_0_velocity_basic__4_advance` at 14.91 (percentile 93, range 0.91 to 64.63)
- `4_advance_decline_today__4_advance` at 382.00 (percentile 92, range 33.00 to 430.00)
- `4_advance_decline_today__net_breadth` at 11.08 (percentile 92, range -24.25 to 15.28)
- `mbm_2_0_velocity_basic__net_breadth` at 11.75 (percentile 92, range -57.34 to 63.90)
- `above_10ma__pct` at 75.20 (percentile 91, range 7.00 to 96.49)

Bottom decile of history:

- `52_wk_high_low_today__new_52_wk_low` at 0.73 (percentile 3, range 0.73 to 14.97)
- `mbm_2_0_velocity_basic__5d_range` at 0.55 (percentile 5, range 0.32 to 19.47)
- `5_advance_decline_ratio__decline` at 28.18 (percentile 5, range 21.67 to 85.61)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__down_4_5_today` crossed up through 50: 37.00 to 55.00
- `mbm_2_0_magnitude__abv_20ma` crossed up through 50: 48.04 to 58.72

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.63 | +0.08 | -0.67 | -0.12 | 63 |
| `15_up_10_down__10_in_5d` | 1.94 | +0.12 | -1.22 | -0.55 | 51 |
| `15_up_10_down__15_in_5d` | 3.37 | +0.54 | +1.52 | +0.80 | 88 |
| `3_above_200_ema__pct` | 41.52 | +5.45 | +14.08 | +2.83 | 45 |
| `4_advance_decline__4_advance` | 381.00 | -79.00 | +127.00 | +198.00 | 96 |
| `4_advance_decline__4_decline` | 91.00 | +23.00 | +13.00 | +15.00 | 56 |
| `4_advance_decline_today__4_advance` | 382.00 | -48.00 | +150.00 | +232.00 | 92 |
| `4_advance_decline_today__4_decline` | 97.00 | +32.00 | +24.00 | +31.00 | 58 |
| `4_advance_decline_today__net_breadth` | 11.08 | -4.20 | +4.42 | +7.57 | 92 |
| `52_week_high_low_within_10__high` | 17.99 | +1.96 | +6.88 | -1.22 | 38 |
| `52_week_high_low_within_10__low` | 19.50 | -5.54 | -13.17 | -7.91 | 51 |
| `52_wk_high_low__new_52_wk_high` | 2.19 | +0.72 | +1.04 | +0.18 | 47 |
| `52_wk_high_low__new_52_wk_low` | 0.56 | -0.79 | -1.61 | -2.09 | 17 |
| `52_wk_high_low_today__new_52_wk_high` | 2.20 | +0.67 | +0.99 | +0.15 | 79 |
| `52_wk_high_low_today__new_52_wk_low` | 0.73 | -0.86 | -1.64 | -2.03 | 3 |
| `5_advance_decline_ratio__advance` | 70.81 | -6.48 | +8.57 | +30.44 | 97 |
| `5_advance_decline_ratio__decline` | 28.18 | +6.50 | -8.54 | -30.42 | 5 |
| `above_10ma__pct` | 75.20 | +5.78 | +32.48 | +39.77 | 91 |
| `above_200ma__above_200ma` | 41.64 | +5.16 | +14.00 | +2.67 | 48 |
| `above_20_ema__pct` | 62.77 | +9.64 | +35.76 | +32.23 | 79 |
| `above_20ma__pct` | 63.58 | +10.15 | +36.60 | +33.43 | 83 |
| `above_50_ema__pct` | 44.62 | +7.65 | +23.75 | +13.38 | 45 |
| `above_50ma__above_50ma` | 41.52 | +5.45 | +14.08 | +2.83 | 47 |
| `breadth_above_500_trend_reversal__above_200dma` | 977.00 | +104.00 | +275.00 | +5.00 | 55 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,444.00 | +229.00 | +827.00 | +712.00 | 85 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,016.00 | +179.00 | +512.00 | +248.00 | 56 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,277.00 | -102.00 | -291.00 | -20.00 | 64 |
| `breadth_above_500_trend_reversal__below_20dma` | 810.00 | -227.00 | -842.00 | -727.00 | 25 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,238.00 | -177.00 | -528.00 | -263.00 | 59 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 1.00 | -1.00 | -1.00 | -7.00 | 42 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 55.00 | +18.00 | +10.00 | +25.00 | 75 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 30.00 | +11.00 | +17.00 | +4.00 | 85 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 233.00 | -76.00 | +89.00 | +133.00 | 94 |
| `current_previous_yr_volumes_crores__1_yr_back` | 475.59 | -37.77 | +355.41 | +37.72 | 80 |
| `current_previous_yr_volumes_crores__current` | 571.67 | +39.81 | +130.20 | +159.75 | 79 |
| `drawdowns_peaks__blw_3` | 128.00 | +21.00 | +3.00 | +2.00 | 50 |
| `gold_etfs_nifty_1_month_chg__gold` | -5.39 | +1.72 | +0.35 | +3.56 | 35 |
| `gold_etfs_nifty_1_month_chg__nifty` | 3.97 | +3.30 | +5.16 | +9.46 | 86 |
| `mbm_2_0_magnitude__abv_10ma` | 73.84 | +6.87 | +36.60 | +35.40 | 90 |
| `mbm_2_0_magnitude__abv_200ma` | 36.31 | +2.11 | +6.53 | -5.00 | 43 |
| `mbm_2_0_magnitude__abv_20ma` | 58.72 | +10.68 | +34.25 | +25.16 | 79 |
| `mbm_2_0_magnitude__abv_50ma` | 38.75 | +7.84 | +17.31 | +3.72 | 47 |
| `mbm_2_0_velocity_advanced__15_52wh` | 16.13 | +1.54 | +4.04 | -6.14 | 44 |
| `mbm_2_0_velocity_advanced__15_52wl` | 25.78 | -4.59 | -9.86 | -4.20 | 59 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 50.76 | -1.58 | -4.25 | +4.32 | 59 |
| `mbm_2_0_velocity_advanced__30_52wh` | 49.12 | +1.79 | +5.18 | -2.25 | 74 |
| `mbm_2_0_velocity_advanced__breakdowns` | 8.30 | -1.32 | -1.26 | +0.89 | 48 |
| `mbm_2_0_velocity_advanced__breakouts` | 40.31 | +6.15 | +18.32 | +25.24 | 96 |
| `mbm_2_0_velocity_advanced__down_close` | 38.07 | +11.76 | +7.67 | +3.41 | 70 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -9.65 | +6.13 | +13.90 | -1.94 | 40 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -1.64 | +3.38 | +9.44 | -6.57 | 50 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 1.90 | +1.85 | +3.24 | +2.44 | 82 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 2.49 | +0.88 | +1.22 | +0.09 | 81 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 0.59 | -0.97 | -2.02 | -2.36 | 32 |
| `mbm_2_0_velocity_advanced__up_close` | 36.99 | -16.10 | -6.88 | -4.07 | 48 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.63 | +0.08 | -0.51 | -0.13 | 65 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.94 | +0.12 | -1.22 | -0.55 | 53 |
| `mbm_2_0_velocity_basic__15_in_5d` | 3.37 | +0.54 | +1.52 | +0.80 | 83 |
| `mbm_2_0_velocity_basic__3_range` | 25.23 | +3.43 | -9.22 | -18.43 | 17 |
| `mbm_2_0_velocity_basic__4_advance` | 14.91 | -3.22 | +5.27 | +8.72 | 93 |
| `mbm_2_0_velocity_basic__4_decline` | 3.16 | +0.63 | +0.25 | +0.59 | 58 |
| `mbm_2_0_velocity_basic__5d_range` | 0.55 | -0.89 | -0.72 | -2.27 | 5 |
| `mbm_2_0_velocity_basic__net_breadth` | 11.75 | -3.85 | +5.01 | +8.13 | 92 |
| `mbm_2_0_velocity_basic__volume` | 1.52 | +0.80 | +1.16 | +1.17 | 94 |
| `net_breadth__net_breadth` | 11.35 | -4.03 | +4.44 | +7.13 | 96 |
| `net_nh_nl__net_nh_nl` | 1.76 | +1.72 | +3.02 | +2.27 | 62 |
| `new_high_low_bearishness_bullishness__high` | 67.00 | +22.00 | +32.00 | +6.00 | 76 |
| `new_high_low_bearishness_bullishness__low` | 17.00 | -24.00 | -49.00 | -63.00 | 36 |
| `volume__volume` | 1.40 | +0.73 | +1.05 | +1.05 | 100 |

## No reading for 2026-11-05

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-02, 64.59
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-02, 35.41
- `oversold_overbought_rsi__overbought`: last 2026-11-02, 77.00
- `oversold_overbought_rsi__oversold`: last 2026-11-02, 92.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-02, 0.39
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-02, 0.53


<!-- market-read -->

## Market read

Thursday was the second wide up day in a row. 233 stocks rose four and a half percent or more, against 55 that fell that hard. The market last strung two days this wide together in April 2025. Almost two stocks in three now stand above their 20 day line, the most since early August. The count above the 200 day line rose to 977 and passed the mid October repair high. New yearly highs reached 67 against only 17 new lows. This time the large companies led. Autos, finance, banks and realty carried the Nifty up more than two percent, while the small company index rose less than one percent. For the first time in this bounce, heavy volume stocks outnumbered light volume stocks. Turnover rose to about 570 crore, the most on an up day since mid October, but still short of the selling days. Fear did not ease, and late selling trimmed many gains. The repair has become an early uptrend on the short and middle clocks, with the long clock now joining. The money and the fear gauge have not yet confirmed it.

Full brief: briefs/2026-11-05.html
