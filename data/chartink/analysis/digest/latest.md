# Market breadth digest: 2026-11-04

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-04: **69** of 79
- History available: 2019-07-01 to 2026-11-04, 711 dated rows
- Metrics with no reading for 2026-11-04: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 66.96 | +20.84 | +37.23 | +28.52 | 85 | 415 |
| % above 20 EMA | 48.02 | +15.09 | +27.98 | +15.30 | 67 | 415 |
| % above 50 EMA | 30.89 | +6.69 | +12.54 | -3.51 | 32 | 415 |
| % above 200 EMA | 34.22 | +3.99 | +5.62 | -7.34 | 38 | 415 |
| Net breadth (4% adv minus dec) | 15.57 | +11.14 | +11.77 | +5.04 | 95 | 415 |
| 4% advancers | 18.10 | +9.80 | +10.72 | +5.76 | 96 | 415 |
| 4% decliners | 2.53 | -1.35 | -1.05 | +0.72 | 42 | 415 |
| Net new highs minus lows | 0.04 | +0.67 | +2.83 | -0.08 | 44 | 415 |
| Net within 15% of 52wk H/L | -15.78 | +6.31 | +10.24 | -7.91 | 31 | 415 |
| Volume expansion ratio | 0.72 | +0.16 | +0.41 | +0.36 | 77 | 415 |
| Overbought count (weekly RSI>70) (as of 2026-11-02) | 70.00 | +8.00 | -79.00 | -134.00 | 24 | 384 |
| Oversold count (weekly RSI<30) (as of 2026-11-02) | 121.00 | -162.00 | -34.00 | +96.00 | 83 | 384 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `breadth_above_500_trend_reversal__below_20dma` | 1,037.00 | -340.00 | 39 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,212.00 | +338.00 | 73 |
| `4_advance_decline__4_advance` | 429.00 | +232.00 | 99 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,414.00 | -217.00 | 76 |
| `breadth_above_500_trend_reversal__above_50dma` | 835.00 | +216.00 | 42 |
| `4_advance_decline_today__4_advance` | 430.00 | +215.00 | 100 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 309.00 | +180.00 | 97 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,377.00 | -147.00 | 76 |
| `breadth_above_500_trend_reversal__above_200dma` | 872.00 | +145.00 | 41 |
| `current_previous_yr_volumes_crores__1_yr_back` | 513.36 | -137.53 | 89 |

## At the edge of their own range

Top decile of history:

- `5_advance_decline_ratio__advance` at 77.29 (percentile 100, range 13.35 to 77.29)
- `4_advance_decline_today__4_advance` at 430.00 (percentile 100, range 33.00 to 430.00)
- `4_advance_decline_today__net_breadth` at 15.28 (percentile 100, range -24.25 to 15.28)
- `4_advance_decline__4_advance` at 429.00 (percentile 99, range 30.00 to 479.00)
- `net_breadth__net_breadth` at 15.57 (percentile 99, range -24.34 to 19.72)
- `mbm_2_0_velocity_advanced__up_close` at 53.03 (percentile 97, range 14.22 to 75.03)
- `breadth_above_500_trend_reversal__up_4_5_today` at 309.00 (percentile 97, range 6.00 to 1,125.00)
- `mbm_2_0_velocity_basic__4_advance` at 18.10 (percentile 96, range 0.91 to 64.61)
- `mbm_2_0_velocity_basic__net_breadth` at 15.57 (percentile 95, range -57.32 to 63.88)
- `mbm_2_0_velocity_advanced__breakouts` at 34.13 (percentile 93, range 3.51 to 86.12)
- `volume__volume` at 0.72 (percentile 92, range 0.24 to 1.28)

Bottom decile of history:

- `5_advance_decline_ratio__decline` at 21.67 (percentile 3, range 21.67 to 85.61)

## Crossed the 50 line today

- `above_20_ema__pct` crossed up through 50: 39.51 to 53.43
- `above_20ma__pct` crossed up through 50: 39.51 to 53.43
- `mbm_2_0_magnitude__abv_10ma` crossed up through 50: 46.12 to 66.96

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.55 | -0.13 | -1.31 | -0.34 | 52 |
| `15_up_10_down__10_in_5d` | 1.81 | -0.67 | -3.08 | -0.59 | 49 |
| `15_up_10_down__15_in_5d` | 2.78 | +0.89 | +1.69 | +0.30 | 68 |
| `3_above_200_ema__pct` | 36.07 | +6.97 | +10.01 | -3.07 | 31 |
| `4_advance_decline__4_advance` | 429.00 | +232.00 | +254.00 | +136.00 | 99 |
| `4_advance_decline__4_decline` | 60.00 | -32.00 | -25.00 | +17.00 | 34 |
| `4_advance_decline_today__4_advance` | 430.00 | +215.00 | +252.00 | +134.00 | 100 |
| `4_advance_decline_today__4_decline` | 65.00 | -49.00 | -24.00 | +17.00 | 22 |
| `4_advance_decline_today__net_breadth` | 15.28 | +11.34 | +11.55 | +4.92 | 100 |
| `52_week_high_low_within_10__high` | 17.22 | +2.66 | +7.33 | -3.17 | 34 |
| `52_week_high_low_within_10__low` | 26.91 | -5.00 | -9.32 | -1.49 | 67 |
| `52_wk_high_low__new_52_wk_high` | 1.59 | +0.42 | +0.78 | -0.37 | 27 |
| `52_wk_high_low__new_52_wk_low` | 1.44 | -0.28 | -1.82 | -0.55 | 59 |
| `52_wk_high_low_today__new_52_wk_high` | 1.53 | +0.39 | +0.72 | -0.36 | 54 |
| `52_wk_high_low_today__new_52_wk_low` | 1.59 | -0.26 | -1.66 | -0.42 | 19 |
| `5_advance_decline_ratio__advance` | 77.29 | +18.27 | +23.80 | +7.07 | 100 |
| `5_advance_decline_ratio__decline` | 21.67 | -18.28 | -23.80 | -7.07 | 3 |
| `above_10ma__pct` | 70.31 | +18.30 | +39.83 | +34.52 | 86 |
| `above_200ma__above_200ma` | 36.07 | +6.97 | +10.01 | -3.07 | 33 |
| `above_20_ema__pct` | 53.43 | +13.92 | +33.97 | +24.40 | 70 |
| `above_20ma__pct` | 53.43 | +13.92 | +33.97 | +24.40 | 72 |
| `above_50_ema__pct` | 36.63 | +9.68 | +19.55 | +6.62 | 37 |
| `above_50ma__above_50ma` | 36.07 | +6.97 | +10.01 | -3.07 | 33 |
| `breadth_above_500_trend_reversal__above_200dma` | 872.00 | +145.00 | +204.00 | -107.00 | 41 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,212.00 | +338.00 | +753.00 | +505.00 | 73 |
| `breadth_above_500_trend_reversal__above_50dma` | 835.00 | +216.00 | +416.00 | +80.00 | 42 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,377.00 | -147.00 | -221.00 | +90.00 | 76 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,037.00 | -340.00 | -770.00 | -522.00 | 39 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,414.00 | -217.00 | -433.00 | -97.00 | 76 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 2.00 | +1.00 | -4.00 | -4.00 | 60 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 36.00 | -13.00 | -18.00 | +12.00 | 57 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 20.00 | +4.00 | +7.00 | -2.00 | 67 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 309.00 | +180.00 | +205.00 | +109.00 | 97 |
| `current_previous_yr_volumes_crores__1_yr_back` | 513.36 | -137.53 | +74.06 | +22.58 | 89 |
| `current_previous_yr_volumes_crores__current` | 531.84 | +81.64 | +109.85 | +141.04 | 65 |
| `drawdowns_peaks__blw_3` | 107.00 | -60.00 | -63.00 | +29.00 | 37 |
| `gold_etfs_nifty_1_month_chg__gold` | -7.11 | +3.70 | -0.83 | +0.32 | 26 |
| `gold_etfs_nifty_1_month_chg__nifty` | 0.67 | +0.40 | +4.23 | +6.00 | 59 |
| `mbm_2_0_magnitude__abv_10ma` | 66.96 | +20.84 | +37.23 | +28.52 | 85 |
| `mbm_2_0_magnitude__abv_200ma` | 34.22 | +3.99 | +5.62 | -7.34 | 38 |
| `mbm_2_0_magnitude__abv_20ma` | 48.02 | +15.09 | +27.98 | +15.30 | 67 |
| `mbm_2_0_magnitude__abv_50ma` | 30.89 | +6.69 | +12.54 | -3.51 | 32 |
| `mbm_2_0_velocity_advanced__15_52wh` | 14.60 | +2.42 | +3.93 | -7.00 | 32 |
| `mbm_2_0_velocity_advanced__15_52wl` | 30.38 | -3.90 | -6.31 | +0.91 | 67 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 52.36 | -2.27 | -3.73 | +6.34 | 63 |
| `mbm_2_0_velocity_advanced__30_52wh` | 47.34 | +2.82 | +4.03 | -4.24 | 64 |
| `mbm_2_0_velocity_advanced__breakdowns` | 9.62 | -0.96 | -3.03 | +3.73 | 60 |
| `mbm_2_0_velocity_advanced__breakouts` | 34.13 | +7.28 | +14.40 | +8.37 | 93 |
| `mbm_2_0_velocity_advanced__down_close` | 26.32 | -10.34 | -2.02 | -4.40 | 16 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -15.78 | +6.31 | +10.24 | -7.91 | 31 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -5.02 | +5.10 | +7.76 | -10.58 | 43 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 0.04 | +0.67 | +2.83 | -0.08 | 44 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.60 | +0.38 | +0.84 | -0.63 | 52 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.56 | -0.29 | -1.98 | -0.54 | 59 |
| `mbm_2_0_velocity_advanced__up_close` | 53.03 | +22.10 | +15.64 | +5.15 | 97 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.55 | -0.13 | -1.31 | -0.34 | 59 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.81 | -0.67 | -3.08 | -0.59 | 51 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.78 | +0.89 | +1.69 | +0.30 | 73 |
| `mbm_2_0_velocity_basic__3_range` | 21.81 | -6.98 | -10.20 | -18.35 | 13 |
| `mbm_2_0_velocity_basic__4_advance` | 18.10 | +9.80 | +10.72 | +5.76 | 96 |
| `mbm_2_0_velocity_basic__4_decline` | 2.53 | -1.35 | -1.05 | +0.72 | 42 |
| `mbm_2_0_velocity_basic__5d_range` | 1.43 | -0.25 | +0.17 | -0.97 | 17 |
| `mbm_2_0_velocity_basic__net_breadth` | 15.57 | +11.14 | +11.77 | +5.04 | 95 |
| `mbm_2_0_velocity_basic__volume` | 0.72 | +0.16 | +0.41 | +0.36 | 77 |
| `net_breadth__net_breadth` | 15.57 | +11.14 | +11.77 | +5.04 | 99 |
| `net_nh_nl__net_nh_nl` | 0.04 | +0.67 | +2.83 | -0.08 | 33 |
| `new_high_low_bearishness_bullishness__high` | 45.00 | +12.00 | +22.00 | -11.00 | 51 |
| `new_high_low_bearishness_bullishness__low` | 41.00 | -8.00 | -52.00 | -16.00 | 60 |
| `volume__volume` | 0.72 | +0.16 | +0.41 | +0.36 | 92 |

## No reading for 2026-11-04

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-02, 61.77
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-02, 38.23
- `oversold_overbought_rsi__overbought`: last 2026-11-02, 70.00
- `oversold_overbought_rsi__oversold`: last 2026-11-02, 121.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-02, 0.35
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-02, 0.63


<!-- market-read -->

## Market read

Wednesday was the widest up day since mid June. 309 stocks rose four and a half percent or more, against only 36 that fell that hard. More than half the market now stands above its 20 day line, the first time since 11 August. The count above the 200 day line rose to 872, about four stocks in ten, and passed the lows of the early October floor. The Nifty rose less than one percent, while the small and micro company indices rose about two percent each. Media, realty, metals, defence and energy led. IT was the only stock index that fell. New yearly highs outnumbered new yearly lows for the first time since mid October. Turnover rose to about 530 crore, the most on an up day since 16 October, but still short of the 610 crore of the heavy selling days. The bounce has turned into a broad repair on the short and middle clocks. The long clock and the money behind it have not yet confirmed it.

Full brief: briefs/2026-11-04.html
