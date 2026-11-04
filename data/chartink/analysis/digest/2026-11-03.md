# Market breadth digest: 2026-11-03

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-03: **69** of 79
- History available: 2019-07-01 to 2026-11-03, 710 dated rows
- Metrics with no reading for 2026-11-03: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 45.70 | +4.84 | +21.25 | +21.80 | 61 | 414 |
| % above 20 EMA | 32.91 | +4.95 | +14.72 | +8.65 | 34 | 414 |
| % above 50 EMA | 24.56 | +2.95 | +6.48 | -5.81 | 20 | 414 |
| % above 200 EMA | 30.48 | +1.42 | +2.06 | -8.47 | 33 | 414 |
| Net breadth (4% adv minus dec) | 4.16 | -7.06 | -9.68 | +3.92 | 65 | 414 |
| 4% advancers | 8.40 | -7.02 | -8.94 | +2.13 | 79 | 414 |
| 4% decliners | 4.24 | +0.04 | +0.74 | -1.79 | 71 | 414 |
| Net new highs minus lows | -0.59 | +1.35 | +2.32 | +1.21 | 34 | 414 |
| Net within 15% of 52wk H/L | -22.09 | +1.97 | +4.11 | -11.51 | 24 | 414 |
| Volume expansion ratio | 0.54 | +0.07 | +0.16 | +0.20 | 61 | 414 |
| Overbought count (weekly RSI>70) (as of 2026-11-02) | 62.00 | +0.00 | -87.00 | -142.00 | 21 | 384 |
| Oversold count (weekly RSI<30) (as of 2026-11-02) | 170.00 | -114.00 | +15.00 | +146.00 | 88 | 384 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__1_yr_back` | 650.89 | +219.55 | 98 |
| `4_advance_decline_today__4_advance` | 215.00 | -178.00 | 83 |
| `4_advance_decline__4_advance` | 197.00 | -174.00 | 85 |
| `breadth_above_500_trend_reversal__above_20dma` | 897.00 | +163.00 | 45 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,416.00 | -161.00 | 71 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 131.00 | -121.00 | 81 |
| `breadth_above_500_trend_reversal__above_50dma` | 643.00 | +92.00 | 24 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,669.00 | -91.00 | 89 |
| `breadth_above_500_trend_reversal__above_200dma` | 756.00 | +49.00 | 30 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,557.00 | -47.00 | 87 |

## At the edge of their own range

Top decile of history:

- `current_previous_yr_volumes_crores__1_yr_back` at 650.89 (percentile 98, range 120.18 to 715.72)

Bottom decile of history:

- `gold_etfs_nifty_1_month_chg__gold` at -10.81 (percentile 6, range -15.78 to 14.14)

## Crossed the 50 line today

- `above_10ma__pct` crossed up through 50: 46.01 to 51.20

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.71 | -0.55 | -1.81 | -0.36 | 74 |
| `15_up_10_down__10_in_5d` | 2.43 | +0.04 | -9.12 | -3.20 | 58 |
| `15_up_10_down__15_in_5d` | 1.84 | -1.25 | +1.25 | +0.15 | 37 |
| `3_above_200_ema__pct` | 29.10 | +2.33 | +3.37 | -7.96 | 19 |
| `4_advance_decline__4_advance` | 197.00 | -174.00 | -211.00 | +48.00 | 85 |
| `4_advance_decline__4_decline` | 91.00 | -2.00 | +16.00 | -42.00 | 64 |
| `4_advance_decline_today__4_advance` | 215.00 | -178.00 | -194.00 | +139.00 | 83 |
| `4_advance_decline_today__4_decline` | 114.00 | +7.00 | +35.00 | -101.00 | 67 |
| `4_advance_decline_today__net_breadth` | 3.93 | -7.21 | -9.88 | +9.75 | 67 |
| `52_week_high_low_within_10__high` | 13.62 | +1.89 | +4.52 | -3.48 | 18 |
| `52_week_high_low_within_10__low` | 29.85 | -2.20 | -5.23 | +1.24 | 74 |
| `52_wk_high_low__new_52_wk_high` | 1.09 | -0.20 | +0.49 | -0.33 | 10 |
| `52_wk_high_low__new_52_wk_low` | 1.61 | -1.38 | -1.44 | -1.39 | 64 |
| `52_wk_high_low_today__new_52_wk_high` | 1.14 | -0.17 | +0.49 | -0.42 | 22 |
| `52_wk_high_low_today__new_52_wk_low` | 1.85 | -1.09 | -1.40 | -5.31 | 25 |
| `5_advance_decline_ratio__advance` | 59.02 | -11.28 | -11.39 | +35.06 | 75 |
| `5_advance_decline_ratio__decline` | 39.96 | +11.34 | +11.41 | -35.04 | 28 |
| `above_10ma__pct` | 51.20 | +5.19 | +25.63 | +29.61 | 69 |
| `above_200ma__above_200ma` | 29.10 | +2.33 | +3.37 | -7.96 | 21 |
| `above_20_ema__pct` | 39.51 | +6.39 | +21.80 | +18.28 | 41 |
| `above_20ma__pct` | 39.06 | +6.10 | +21.01 | +17.40 | 41 |
| `above_50_ema__pct` | 27.11 | +4.08 | +10.18 | +0.52 | 23 |
| `above_50ma__above_50ma` | 29.10 | +2.33 | +3.37 | -7.96 | 21 |
| `breadth_above_500_trend_reversal__above_200dma` | 756.00 | +49.00 | +66.00 | -202.00 | 30 |
| `breadth_above_500_trend_reversal__above_20dma` | 897.00 | +163.00 | +461.00 | +369.00 | 45 |
| `breadth_above_500_trend_reversal__above_50dma` | 643.00 | +92.00 | +215.00 | -35.00 | 24 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,557.00 | -47.00 | -81.00 | +186.00 | 87 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,416.00 | -161.00 | -476.00 | -385.00 | 71 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,669.00 | -91.00 | -231.00 | +18.00 | 89 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 1.00 | -1.00 | -13.00 | -6.00 | 43 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 56.00 | -12.00 | +14.00 | -18.00 | 75 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 16.00 | -8.00 | +8.00 | +4.00 | 55 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 131.00 | -121.00 | -156.00 | +26.00 | 81 |
| `current_previous_yr_volumes_crores__1_yr_back` | 650.89 | +219.55 | +234.95 | +235.29 | 98 |
| `current_previous_yr_volumes_crores__current` | 450.20 | -43.83 | -73.65 | +30.48 | 23 |
| `drawdowns_peaks__blw_3` | 198.00 | +14.00 | +59.00 | -71.00 | 71 |
| `gold_etfs_nifty_1_month_chg__gold` | -10.81 | -1.39 | -2.42 | -5.20 | 6 |
| `gold_etfs_nifty_1_month_chg__nifty` | 0.27 | +0.84 | +4.03 | +6.15 | 56 |
| `mbm_2_0_magnitude__abv_10ma` | 45.70 | +4.84 | +21.25 | +21.80 | 61 |
| `mbm_2_0_magnitude__abv_200ma` | 30.48 | +1.42 | +2.06 | -8.47 | 33 |
| `mbm_2_0_magnitude__abv_20ma` | 32.91 | +4.95 | +14.72 | +8.65 | 34 |
| `mbm_2_0_magnitude__abv_50ma` | 24.56 | +2.95 | +6.48 | -5.81 | 20 |
| `mbm_2_0_velocity_advanced__15_52wh` | 12.18 | +0.99 | +1.15 | -7.88 | 22 |
| `mbm_2_0_velocity_advanced__15_52wl` | 34.27 | -0.98 | -2.96 | +3.63 | 72 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 54.60 | +0.45 | -1.09 | +7.24 | 66 |
| `mbm_2_0_velocity_advanced__30_52wh` | 44.52 | +0.93 | +1.47 | -5.40 | 45 |
| `mbm_2_0_velocity_advanced__breakdowns` | 10.54 | -1.62 | +3.08 | -2.31 | 66 |
| `mbm_2_0_velocity_advanced__breakouts` | 26.90 | -9.41 | -11.10 | +7.46 | 89 |
| `mbm_2_0_velocity_advanced__down_close` | 36.40 | +4.22 | -5.97 | -7.06 | 62 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -22.09 | +1.97 | +4.11 | -11.51 | 24 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | -10.08 | +0.48 | +2.56 | -12.64 | 36 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -0.59 | +1.35 | +2.32 | +1.21 | 34 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.22 | -0.25 | +0.59 | -0.46 | 36 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.81 | -1.59 | -1.73 | -1.67 | 62 |
| `mbm_2_0_velocity_advanced__up_close` | 30.88 | -12.11 | -14.36 | -1.30 | 25 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.71 | -0.55 | -1.81 | -0.36 | 70 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.43 | +0.04 | -9.12 | -3.20 | 59 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.84 | -1.25 | +1.25 | +0.15 | 47 |
| `mbm_2_0_velocity_basic__3_range` | 28.13 | +6.80 | +6.27 | -0.07 | 22 |
| `mbm_2_0_velocity_basic__4_advance` | 8.40 | -7.02 | -8.94 | +2.13 | 79 |
| `mbm_2_0_velocity_basic__4_decline` | 4.24 | +0.04 | +0.74 | -1.79 | 71 |
| `mbm_2_0_velocity_basic__5d_range` | 1.65 | -0.55 | +0.82 | -0.28 | 20 |
| `mbm_2_0_velocity_basic__net_breadth` | 4.16 | -7.06 | -9.68 | +3.92 | 65 |
| `mbm_2_0_velocity_basic__volume` | 0.54 | +0.07 | +0.16 | +0.20 | 61 |
| `net_breadth__net_breadth` | 4.47 | -7.23 | -9.56 | +3.80 | 68 |
| `net_nh_nl__net_nh_nl` | -0.55 | +1.25 | +2.16 | +1.18 | 27 |
| `new_high_low_bearishness_bullishness__high` | 33.00 | -6.00 | +15.00 | -10.00 | 32 |
| `new_high_low_bearishness_bullishness__low` | 49.00 | -42.00 | -44.00 | -41.00 | 67 |
| `volume__volume` | 0.56 | +0.08 | +0.17 | +0.21 | 79 |

## No reading for 2026-11-03

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-02, 59.36
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-02, 40.64
- `oversold_overbought_rsi__overbought`: last 2026-11-02, 62.00
- `oversold_overbought_rsi__oversold`: last 2026-11-02, 170.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-02, 0.28
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-02, 0.70


<!-- market-read -->

## Market read

The bounce kept going on Tuesday, but it narrowed and changed hands. The count of stocks above their 20 day line rose to 897, the best since at least late September and past the level where the mid October repair stalled. The count above the 200 day line rose to 756, about one stock in three. The Nifty rose about 1.6 percent and closed back above its thirty week line. The day belonged to the big consumer and finance names: staples, private banks, realty and consumption led, while Monday's oil, metal and energy leaders stood still. The small company indices barely rose. Only 131 stocks rose four and a half percent or more, about half Monday's count, and fewer of the day's risers held their gains. New yearly lows fell to 49, the fewest since mid October. Turnover was about 450 crore, still far below the 610 of the heavy selling days. The bounce now looks stronger on the trend counts, but buyers still have not come in size, and the lift is coming from the top of the market.

Full brief: briefs/2026-11-03.html
