# Market breadth digest: 2026-11-11

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-11: **69** of 79
- History available: 2019-07-01 to 2026-11-11, 716 dated rows
- Metrics with no reading for 2026-11-11: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 76.24 | +7.85 | +9.93 | +39.16 | 92 | 420 |
| % above 20 EMA | 69.05 | +9.78 | +21.03 | +38.36 | 88 | 420 |
| % above 50 EMA | 48.26 | +7.96 | +16.77 | +17.65 | 64 | 420 |
| % above 200 EMA | 40.33 | +2.72 | +5.70 | +1.52 | 55 | 420 |
| Net breadth (4% adv minus dec) | 9.96 | +9.54 | -5.47 | +6.93 | 89 | 420 |
| 4% advancers | 11.84 | +6.97 | -6.22 | +5.26 | 89 | 420 |
| 4% decliners | 1.88 | -2.57 | -0.75 | -1.67 | 24 | 420 |
| Net new highs minus lows | 1.68 | +0.78 | +1.60 | +3.53 | 78 | 420 |
| Net within 15% of 52wk H/L | -1.84 | +5.57 | +12.70 | +8.01 | 55 | 420 |
| Volume expansion ratio | 1.09 | +0.80 | +0.42 | +0.78 | 90 | 420 |
| Overbought count (weekly RSI>70) (as of 2026-11-09) | 85.00 | -1.00 | -50.00 | -101.00 | 30 | 385 |
| Oversold count (weekly RSI<30) (as of 2026-11-09) | 54.00 | -18.00 | -149.00 | +23.00 | 69 | 385 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `breadth_above_500_trend_reversal__above_20dma` | 1,681.00 | +216.00 | 94 |
| `breadth_above_500_trend_reversal__below_20dma` | 659.00 | -216.00 | 18 |
| `4_advance_decline_today__4_advance` | 307.00 | +179.00 | 90 |
| `4_advance_decline__4_advance` | 303.00 | +178.00 | 93 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,255.00 | +172.00 | 70 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,085.00 | -172.00 | 44 |
| `current_previous_yr_volumes_crores__current` | 571.89 | +167.45 | 78 |
| `drawdowns_peaks__blw_3` | 82.00 | -149.00 | 23 |
| `current_previous_yr_volumes_crores__1_yr_back` | 449.49 | -121.52 | 66 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 184.00 | +108.00 | 90 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 11.23 (percentile 100, range -6.93 to 11.23)
- `5_advance_decline_ratio__advance` at 70.85 (percentile 98, range 13.35 to 77.29)
- `volume__volume` at 1.09 (percentile 97, range 0.03 to 1.40)
- `breadth_above_500_trend_reversal__above_20dma` at 1,681.00 (percentile 94, range 119.00 to 2,052.00)
- `4_advance_decline__4_advance` at 303.00 (percentile 93, range 34.00 to 479.00)
- `mbm_2_0_velocity_advanced__breakouts` at 31.73 (percentile 92, range 3.51 to 86.09)
- `net_breadth__net_breadth` at 9.96 (percentile 92, range -24.73 to 19.72)
- `above_10ma__pct` at 77.46 (percentile 92, range 1.54 to 96.49)
- `mbm_2_0_magnitude__abv_10ma` at 76.24 (percentile 92, range 0.40 to 96.11)
- `breadth_above_500_trend_reversal__up_4_5_today` at 184.00 (percentile 90, range 6.00 to 1,127.00)
- `4_advance_decline_today__4_advance` at 307.00 (percentile 90, range 33.00 to 430.00)
- `mbm_2_0_velocity_basic__volume` at 1.09 (percentile 90, range 0.03 to 5.71)

Bottom decile of history:

- `52_wk_high_low_today__new_52_wk_low` at 0.38 (percentile 2, range 0.38 to 14.97)
- `52_wk_high_low__new_52_wk_low` at 0.23 (percentile 3, range 0.04 to 14.83)
- `5_advance_decline_ratio__decline` at 28.09 (percentile 5, range 21.67 to 85.61)
- `4_advance_decline_today__4_decline` at 53.00 (percentile 10, range 36.00 to 634.00)

## Crossed the 50 line today

- `above_50_ema__pct` crossed up through 50: 46.40 to 53.51
- `breadth_above_500_trend_reversal__down_4_5_today` crossed down through 50: 54.00 to 19.00

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.31 | -0.35 | -0.04 | -0.59 | 13 |
| `15_up_10_down__10_in_5d` | 1.33 | -0.04 | -0.43 | -1.71 | 23 |
| `15_up_10_down__15_in_5d` | 2.66 | -0.77 | -0.05 | +1.16 | 59 |
| `3_above_200_ema__pct` | 45.80 | +2.85 | +9.22 | +9.22 | 59 |
| `4_advance_decline__4_advance` | 303.00 | +178.00 | -158.00 | +136.00 | 93 |
| `4_advance_decline__4_decline` | 48.00 | -66.00 | -19.00 | -42.00 | 15 |
| `4_advance_decline_today__4_advance` | 307.00 | +179.00 | +92.00 | +129.00 | 90 |
| `4_advance_decline_today__4_decline` | 53.00 | -62.00 | -61.00 | -27.00 | 10 |
| `4_advance_decline_today__net_breadth` | 9.84 | +9.34 | +5.91 | +5.74 | 88 |
| `52_week_high_low_within_10__high` | 20.88 | +1.92 | +4.59 | +3.58 | 68 |
| `52_week_high_low_within_10__low` | 14.08 | -3.41 | -10.99 | -13.39 | 29 |
| `52_wk_high_low__new_52_wk_high` | 2.16 | +0.53 | +0.68 | +0.74 | 47 |
| `52_wk_high_low__new_52_wk_low` | 0.23 | -0.39 | -1.08 | -3.01 | 3 |
| `52_wk_high_low_today__new_52_wk_high` | 2.14 | +0.44 | +1.00 | +0.57 | 78 |
| `52_wk_high_low_today__new_52_wk_low` | 0.38 | -0.37 | -1.47 | -2.38 | 2 |
| `5_advance_decline_ratio__advance` | 70.85 | +26.25 | +11.84 | +21.77 | 98 |
| `5_advance_decline_ratio__decline` | 28.09 | -26.27 | -11.86 | -21.78 | 5 |
| `above_10ma__pct` | 77.46 | +5.79 | +7.84 | +38.86 | 92 |
| `above_200ma__above_200ma` | 45.80 | +2.85 | +9.22 | +9.22 | 62 |
| `above_20_ema__pct` | 71.51 | +8.31 | +18.22 | +42.46 | 88 |
| `above_20ma__pct` | 71.51 | +8.31 | +18.22 | +42.46 | 88 |
| `above_50_ema__pct` | 53.51 | +7.11 | +16.44 | +25.81 | 65 |
| `above_50ma__above_50ma` | 45.80 | +2.85 | +9.22 | +9.22 | 62 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,124.00 | +74.00 | +209.00 | +175.00 | 75 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,681.00 | +216.00 | +424.00 | +966.00 | 94 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,255.00 | +172.00 | +377.00 | +539.00 | 70 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,216.00 | -74.00 | -205.00 | -178.00 | 56 |
| `breadth_above_500_trend_reversal__below_20dma` | 659.00 | -216.00 | -420.00 | -969.00 | 18 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,085.00 | -172.00 | -373.00 | -542.00 | 44 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 5.00 | +1.00 | +4.00 | +3.00 | 88 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 19.00 | -35.00 | -18.00 | -14.00 | 28 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 23.00 | -5.00 | +4.00 | +5.00 | 73 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 184.00 | +108.00 | -134.00 | +76.00 | 90 |
| `current_previous_yr_volumes_crores__1_yr_back` | 449.49 | -121.52 | -68.82 | +4.99 | 66 |
| `current_previous_yr_volumes_crores__current` | 571.89 | +167.45 | +13.32 | +130.16 | 78 |
| `drawdowns_peaks__blw_3` | 82.00 | -149.00 | -35.00 | -87.00 | 23 |
| `gold_etfs_nifty_1_month_chg__gold` | -4.89 | +1.09 | +2.28 | +2.51 | 41 |
| `gold_etfs_nifty_1_month_chg__nifty` | 11.23 | +3.38 | +10.56 | +15.99 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 76.24 | +7.85 | +9.93 | +39.16 | 92 |
| `mbm_2_0_magnitude__abv_200ma` | 40.33 | +2.72 | +5.70 | +1.52 | 55 |
| `mbm_2_0_magnitude__abv_20ma` | 69.05 | +9.78 | +21.03 | +38.36 | 88 |
| `mbm_2_0_magnitude__abv_50ma` | 48.26 | +7.96 | +16.77 | +17.65 | 64 |
| `mbm_2_0_velocity_advanced__15_52wh` | 17.59 | +2.43 | +3.91 | -1.01 | 56 |
| `mbm_2_0_velocity_advanced__15_52wl` | 19.42 | -3.14 | -8.78 | -9.03 | 42 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 44.67 | -1.48 | -3.87 | -0.45 | 43 |
| `mbm_2_0_velocity_advanced__30_52wh` | 49.00 | +2.98 | +4.78 | +1.41 | 78 |
| `mbm_2_0_velocity_advanced__breakdowns` | 6.64 | -6.92 | -3.78 | -6.87 | 29 |
| `mbm_2_0_velocity_advanced__breakouts` | 31.73 | +18.25 | -2.89 | +16.72 | 92 |
| `mbm_2_0_velocity_advanced__down_close` | 28.24 | -4.52 | +3.05 | +2.00 | 23 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -1.84 | +5.57 | +12.70 | +8.01 | 55 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 4.34 | +4.45 | +8.65 | +1.86 | 66 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 1.68 | +0.78 | +1.60 | +3.53 | 78 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.91 | +0.36 | +0.43 | +0.38 | 62 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 0.23 | -0.43 | -1.18 | -3.15 | 12 |
| `mbm_2_0_velocity_advanced__up_close` | 37.32 | +1.19 | -14.83 | -6.52 | 50 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.31 | -0.35 | -0.04 | -0.59 | 32 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.33 | -0.04 | -0.43 | -1.71 | 34 |
| `mbm_2_0_velocity_basic__15_in_5d` | 2.66 | -0.77 | -0.05 | +1.16 | 68 |
| `mbm_2_0_velocity_basic__3_range` | 32.43 | -5.91 | +11.01 | -5.11 | 30 |
| `mbm_2_0_velocity_basic__4_advance` | 11.84 | +6.97 | -6.22 | +5.26 | 89 |
| `mbm_2_0_velocity_basic__4_decline` | 1.88 | -2.57 | -0.75 | -1.67 | 24 |
| `mbm_2_0_velocity_basic__5d_range` | 2.54 | +1.49 | +1.13 | -1.36 | 30 |
| `mbm_2_0_velocity_basic__net_breadth` | 9.96 | +9.54 | -5.47 | +6.93 | 89 |
| `mbm_2_0_velocity_basic__volume` | 1.09 | +0.80 | +0.42 | +0.78 | 90 |
| `net_breadth__net_breadth` | 9.96 | +9.54 | -5.47 | +6.93 | 92 |
| `net_nh_nl__net_nh_nl` | 1.68 | +0.78 | +1.60 | +3.53 | 62 |
| `new_high_low_bearishness_bullishness__high` | 66.00 | +16.00 | +21.00 | +23.00 | 76 |
| `new_high_low_bearishness_bullishness__low` | 7.00 | -12.00 | -33.00 | -91.00 | 19 |
| `volume__volume` | 1.09 | +0.80 | +0.42 | +0.78 | 97 |

## No reading for 2026-11-11

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-09, 64.99
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-09, 35.01
- `oversold_overbought_rsi__overbought`: last 2026-11-09, 85.00
- `oversold_overbought_rsi__oversold`: last 2026-11-09, 54.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-09, 0.43
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-09, 0.49


<!-- market-read -->

## Market read

Wednesday was the widest up day in a week, and the money came back to watch it. The Nifty rose a little under one percent and closed near 25,255. Across the market, 184 stocks rose four and a half percent or more, and only 19 fell that hard. Turnover climbed to about 570 crore, from about 400 on Monday. About as many stocks traded on heavy volume as on light volume, the best mix since last Thursday. Banks led, with the government banks up almost three percent on the day and almost seven on the week. Autos came next. Healthcare, the leader of the past weeks, slipped on the day and let others carry the market. More than half the market now sits above its 50 day line, for the first time since late August. The count above the 200 day line is 1,124, its best since late September. New yearly lows fell to seven, the fewest since June. The repair has widened into most of the market. It still falls short of half the market on the long clock, and the fear gauge still sits near 17.5.

Full brief: briefs/2026-11-11.html
