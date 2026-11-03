# Market breadth digest: 2026-11-02

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-02: **75** of 79
- History available: 2019-07-01 to 2026-11-02, 709 dated rows
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 41.02 | +15.71 | +28.68 | +19.86 | 48 | 413 |
| % above 20 EMA | 27.89 | +8.55 | +17.19 | +4.67 | 25 | 413 |
| % above 50 EMA | 21.20 | +4.23 | +8.69 | -7.83 | 16 | 413 |
| % above 200 EMA | 28.78 | +1.78 | +3.17 | -9.78 | 29 | 413 |
| Net breadth (4% adv minus dec) | 11.70 | +26.42 | +8.59 | +17.38 | 92 | 413 |
| 4% advancers | 15.61 | +12.01 | +6.16 | +12.53 | 94 | 413 |
| 4% decliners | 3.91 | -14.41 | -2.43 | -4.85 | 69 | 413 |
| Net new highs minus lows | -1.94 | +2.85 | +9.53 | +4.39 | 24 | 413 |
| Net within 15% of 52wk H/L | -24.06 | +3.49 | +7.51 | -14.33 | 21 | 413 |
| Volume expansion ratio | 0.48 | -0.01 | +0.05 | -0.20 | 53 | 413 |
| Overbought count (weekly RSI>70) | 65.00 | +3.00 | -84.00 | -139.00 | 23 | 384 |
| Oversold count (weekly RSI<30) | 173.00 | -110.00 | +18.00 | +148.00 | 88 | 384 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `drawdowns_peaks__blw_3` | 158.00 | -625.00 | 61 |
| `4_advance_decline__4_decline` | 107.00 | -346.00 | 70 |
| `4_advance_decline_today__4_decline` | 107.00 | -330.00 | 63 |
| `4_advance_decline_today__4_advance` | 393.00 | +304.00 | 97 |
| `4_advance_decline__4_advance` | 393.00 | +296.00 | 98 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 61.00 | -224.00 | 77 |
| `breadth_above_500_trend_reversal__above_20dma` | 712.00 | +221.00 | 31 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,518.00 | -219.00 | 80 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 242.00 | +195.00 | 95 |
| `breadth_above_500_trend_reversal__above_50dma` | 528.00 | +129.00 | 16 |

## At the edge of their own range

Top decile of history:

- `4_advance_decline__4_advance` at 393.00 (percentile 98, range 34.00 to 479.00)
- `5_advance_decline_ratio__advance` at 70.30 (percentile 97, range 13.35 to 70.41)
- `4_advance_decline_today__4_advance` at 393.00 (percentile 97, range 33.00 to 409.00)
- `4_advance_decline_today__net_breadth` at 11.14 (percentile 97, range -24.25 to 13.82)
- `net_breadth__net_breadth` at 11.70 (percentile 97, range -24.29 to 19.72)
- `breadth_above_500_trend_reversal__up_4_5_today` at 242.00 (percentile 95, range 6.00 to 1,114.00)
- `mbm_2_0_velocity_basic__4_advance` at 15.61 (percentile 94, range 0.91 to 64.61)
- `mbm_2_0_velocity_advanced__breakouts` at 36.31 (percentile 94, range 3.51 to 86.12)
- `breadth_above_500_trend_reversal__below_50dma` at 1,702.00 (percentile 92, range 270.00 to 1,996.00)
- `mbm_2_0_velocity_basic__net_breadth` at 11.70 (percentile 92, range -57.27 to 63.88)
- `10_from_10dema__10_10ema` at 1.18 (percentile 92, range 0.09 to 7.07)

Bottom decile of history:

- `5_advance_decline_ratio__decline` at 28.61 (percentile 6, range 28.55 to 85.61)

## Crossed the 50 line today

- `breadth_above_500_trend_reversal__up_4_5_today` crossed up through 50: 47.00 to 242.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.18 | -0.90 | -3.61 | +0.29 | 92 |
| `15_up_10_down__10_in_5d` | 2.39 | -0.53 | -25.46 | -2.07 | 56 |
| `15_up_10_down__15_in_5d` | 3.10 | +0.14 | +2.47 | +1.52 | 80 |
| `3_above_200_ema__pct` | 26.77 | +1.96 | +3.71 | -9.38 | 16 |
| `4_advance_decline__4_advance` | 393.00 | +296.00 | +137.00 | +313.00 | 98 |
| `4_advance_decline__4_decline` | 107.00 | -346.00 | -67.00 | -122.00 | 70 |
| `4_advance_decline_today__4_advance` | 393.00 | +304.00 | +167.00 | +254.00 | 97 |
| `4_advance_decline_today__4_decline` | 107.00 | -330.00 | -44.00 | +7.00 | 63 |
| `4_advance_decline_today__net_breadth` | 11.14 | +25.71 | +8.00 | +9.51 | 97 |
| `52_week_high_low_within_10__high` | 12.53 | +2.22 | +5.35 | -5.58 | 17 |
| `52_week_high_low_within_10__low` | 34.18 | -2.96 | -5.30 | +4.54 | 82 |
| `52_wk_high_low__new_52_wk_high` | 1.28 | -0.07 | +0.99 | -0.21 | 15 |
| `52_wk_high_low__new_52_wk_low` | 2.99 | -2.17 | -6.96 | -4.09 | 82 |
| `52_wk_high_low_today__new_52_wk_high` | 1.31 | -0.09 | +0.96 | -0.80 | 31 |
| `52_wk_high_low_today__new_52_wk_low` | 2.95 | -2.36 | -7.05 | +0.05 | 54 |
| `5_advance_decline_ratio__advance` | 70.30 | +43.84 | +10.47 | +22.90 | 97 |
| `5_advance_decline_ratio__decline` | 28.61 | -43.86 | -10.52 | -22.95 | 6 |
| `above_10ma__pct` | 46.46 | +17.19 | +32.80 | +27.40 | 61 |
| `above_200ma__above_200ma` | 27.14 | +2.00 | +3.85 | -9.22 | 19 |
| `above_20_ema__pct` | 33.12 | +11.27 | +22.04 | +12.46 | 31 |
| `above_20ma__pct` | 33.12 | +11.27 | +22.04 | +12.46 | 32 |
| `above_50_ema__pct` | 23.04 | +5.64 | +10.60 | -2.81 | 19 |
| `above_50ma__above_50ma` | 26.77 | +1.96 | +3.71 | -9.38 | 19 |
| `breadth_above_500_trend_reversal__above_200dma` | 678.00 | +50.00 | +78.00 | -226.00 | 23 |
| `breadth_above_500_trend_reversal__above_20dma` | 712.00 | +221.00 | +460.00 | +225.00 | 31 |
| `breadth_above_500_trend_reversal__above_50dma` | 528.00 | +129.00 | +242.00 | -97.00 | 16 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,552.00 | -48.00 | -98.00 | +209.00 | 88 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,518.00 | -219.00 | -480.00 | -242.00 | 80 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,702.00 | -127.00 | -262.00 | +80.00 | 92 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 1.00 | +0.00 | -28.00 | -5.00 | 43 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 61.00 | -224.00 | -10.00 | -43.00 | 77 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 24.00 | -1.00 | +16.00 | +12.00 | 77 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 242.00 | +195.00 | +95.00 | +196.00 | 95 |
| `current_previous_yr_volumes_crores__1_yr_back` | 431.34 | -114.03 | -2.99 | +43.00 | 57 |
| `current_previous_yr_volumes_crores__current` | 493.98 | -115.52 | -25.30 | +14.76 | 46 |
| `drawdowns_peaks__blw_3` | 158.00 | -625.00 | -69.00 | -300.00 | 61 |
| `gold_etfs_nifty_1_month_chg__gold` | -9.42 | -1.69 | -1.75 | -6.06 | 10 |
| `gold_etfs_nifty_1_month_chg__nifty` | -0.57 | +1.21 | +2.59 | +5.30 | 44 |
| `mbm_2_0_magnitude__abv_10ma` | 41.02 | +15.71 | +28.68 | +19.86 | 48 |
| `mbm_2_0_magnitude__abv_200ma` | 28.78 | +1.78 | +3.17 | -9.78 | 29 |
| `mbm_2_0_magnitude__abv_20ma` | 27.89 | +8.55 | +17.19 | +4.67 | 25 |
| `mbm_2_0_magnitude__abv_50ma` | 21.20 | +4.23 | +8.69 | -7.83 | 16 |
| `mbm_2_0_velocity_advanced__15_52wh` | 11.19 | +1.03 | +2.46 | -9.08 | 20 |
| `mbm_2_0_velocity_advanced__15_52wl` | 35.25 | -2.45 | -5.05 | +5.25 | 75 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 54.14 | -2.56 | -3.45 | +7.28 | 65 |
| `mbm_2_0_velocity_advanced__30_52wh` | 43.58 | +2.11 | +3.07 | -6.86 | 39 |
| `mbm_2_0_velocity_advanced__breakdowns` | 12.16 | -22.04 | -6.78 | -23.41 | 70 |
| `mbm_2_0_velocity_advanced__breakouts` | 36.31 | +24.46 | +11.29 | +26.45 | 94 |
| `mbm_2_0_velocity_advanced__down_close` | 32.18 | -21.41 | -1.30 | +7.54 | 39 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -24.06 | +3.49 | +7.51 | -14.33 | 21 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -10.56 | +4.68 | +6.53 | -14.14 | 34 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -1.94 | +2.85 | +9.53 | +4.39 | 24 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.47 | -0.01 | +1.22 | -0.13 | 45 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 3.41 | -2.86 | -8.31 | -4.51 | 77 |
| `mbm_2_0_velocity_advanced__up_close` | 42.99 | +12.63 | +5.24 | +11.79 | 78 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.18 | -0.90 | -3.61 | +0.29 | 88 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.44 | -0.48 | -25.69 | -1.98 | 59 |
| `mbm_2_0_velocity_basic__15_in_5d` | 3.20 | +0.32 | +2.57 | +1.64 | 79 |
| `mbm_2_0_velocity_basic__3_range` | 21.50 | -2.20 | +4.83 | +5.19 | 13 |
| `mbm_2_0_velocity_basic__4_advance` | 15.61 | +12.01 | +6.16 | +12.53 | 94 |
| `mbm_2_0_velocity_basic__4_decline` | 3.91 | -14.41 | -2.43 | -4.85 | 69 |
| `mbm_2_0_velocity_basic__5d_range` | 2.23 | +0.16 | +1.64 | +0.50 | 27 |
| `mbm_2_0_velocity_basic__net_breadth` | 11.70 | +26.42 | +8.59 | +17.38 | 92 |
| `mbm_2_0_velocity_basic__volume` | 0.48 | -0.01 | +0.05 | -0.20 | 53 |
| `net_breadth__net_breadth` | 11.70 | +26.42 | +8.59 | +17.38 | 97 |
| `net_nh_nl__net_nh_nl` | -1.94 | +2.85 | +9.53 | +4.39 | 16 |
| `new_high_low_bearishness_bullishness__high` | 39.00 | -2.00 | +30.00 | -6.00 | 41 |
| `new_high_low_bearishness_bullishness__low` | 91.00 | -65.00 | -213.00 | -123.00 | 79 |
| `nifty_500_above_below_200_ema__above_200_ema` | 59.15 | +3.42 | -3.22 | -14.29 | 21 |
| `nifty_500_above_below_200_ema__below_200_ema` | 40.85 | -3.42 | +3.22 | +15.09 | 80 |
| `oversold_overbought_rsi__overbought` | 65.00 | +3.00 | -84.00 | -139.00 | 23 |
| `oversold_overbought_rsi__oversold` | 173.00 | -110.00 | +18.00 | +148.00 | 88 |
| `volume__volume` | 0.48 | -0.01 | +0.05 | -0.20 | 64 |
| `weekly_rsi_50_50__above_rsi_50` | 0.25 | +0.03 | -0.08 | -0.29 | 15 |
| `weekly_rsi_50_50__below_rsi_50` | 0.74 | -0.03 | +0.09 | +0.32 | 86 |


<!-- market-read -->

## Market read

The latest data is still Monday 2 November, and Monday was a wide, light up day after a heavy down day. On Friday 285 stocks fell four and a half percent or more. On Monday 242 rose that hard. The count of stocks above their 20 day line jumped to 712, the best since mid October. The count above the 200 day line closed at 678, about three stocks in ten, well clear of the 23 October low of 579. Oil and gas, metals and infrastructure led the index board, and Reliance alone rose more than eleven percent. The money did not match the width. Friday's selling carried about 609 crore of turnover and Monday's buying about 494. The big companies hold their long trends far better than the rest, with about six in ten Nifty 500 stocks above the long line. The bounce passed one hard test. It has not yet shown heavy buying, and no newer session has tested it.

Full brief: briefs/2026-11-02.html
