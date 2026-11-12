# Market breadth digest: 2026-11-12

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-11-12: **69** of 79
- History available: 2019-07-01 to 2026-11-12, 717 dated rows
- Metrics with no reading for 2026-11-12: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 75.94 | -0.34 | +3.32 | +29.25 | 91 | 421 |
| % above 20 EMA | 70.01 | +0.92 | +11.96 | +33.40 | 89 | 421 |
| % above 50 EMA | 51.64 | +3.38 | +12.89 | +17.67 | 71 | 421 |
| % above 200 EMA | 41.26 | +0.97 | +4.74 | +1.74 | 58 | 421 |
| Net breadth (4% adv minus dec) | 5.77 | -4.31 | -5.67 | -1.87 | 75 | 421 |
| 4% advancers | 7.68 | -4.24 | -7.24 | -1.73 | 72 | 421 |
| 4% decliners | 1.91 | +0.07 | -1.57 | +0.14 | 25 | 421 |
| Net new highs minus lows | 1.64 | -0.04 | -0.12 | +1.09 | 77 | 421 |
| Net within 15% of 52wk H/L | -0.20 | +1.60 | +8.63 | +8.20 | 59 | 421 |
| Volume expansion ratio | 0.61 | -0.48 | -0.79 | +0.22 | 68 | 421 |
| Overbought count (weekly RSI>70) (as of 2026-11-09) | 101.00 | +15.00 | -34.00 | -85.00 | 37 | 385 |
| Oversold count (weekly RSI<30) (as of 2026-11-09) | 52.00 | -20.00 | -151.00 | +21.00 | 68 | 385 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `4_advance_decline__4_advance` | 197.00 | -108.00 | 76 |
| `4_advance_decline_today__4_advance` | 199.00 | -108.00 | 71 |
| `current_previous_yr_volumes_crores__current` | 492.42 | -79.47 | 42 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,011.00 | -77.00 | 36 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,335.00 | +76.00 | 77 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 123.00 | -63.00 | 77 |
| `breadth_above_500_trend_reversal__below_20dma` | 632.00 | -28.00 | 17 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,714.00 | +27.00 | 95 |
| `drawdowns_peaks__blw_3` | 103.00 | +21.00 | 34 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,203.00 | -19.00 | 54 |

## At the edge of their own range

Top decile of history:

- `gold_etfs_nifty_1_month_chg__nifty` at 12.37 (percentile 100, range -6.93 to 12.37)
- `breadth_above_500_trend_reversal__above_20dma` at 1,714.00 (percentile 95, range 119.00 to 2,054.00)
- `above_10ma__pct` at 77.23 (percentile 92, range 1.54 to 96.49)
- `mbm_2_0_magnitude__abv_10ma` at 75.94 (percentile 91, range 0.40 to 96.11)

Bottom decile of history:

- `52_wk_high_low__new_52_wk_low` at 0.23 (percentile 3, range 0.04 to 14.83)
- `52_wk_high_low_today__new_52_wk_low` at 0.38 (percentile 5, range 0.38 to 14.97)
- `10_from_10dema__10_10ema` at 0.23 (percentile 8, range 0.00 to 7.07)

## Crossed the 50 line today

- `mbm_2_0_magnitude__abv_50ma` crossed up through 50: 48.26 to 51.64

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.23 | -0.08 | -0.16 | -0.20 | 8 |
| `15_up_10_down__10_in_5d` | 1.13 | -0.20 | -0.74 | -1.35 | 14 |
| `15_up_10_down__15_in_5d` | 1.99 | -0.71 | -1.45 | +0.02 | 42 |
| `3_above_200_ema__pct` | 46.62 | +0.82 | +4.86 | +9.88 | 62 |
| `4_advance_decline__4_advance` | 197.00 | -108.00 | -185.00 | -42.00 | 76 |
| `4_advance_decline__4_decline` | 49.00 | +2.00 | -40.00 | +4.00 | 16 |
| `4_advance_decline_today__4_advance` | 199.00 | -108.00 | -231.00 | +50.00 | 71 |
| `4_advance_decline_today__4_decline` | 53.00 | +0.00 | -12.00 | -25.00 | 12 |
| `4_advance_decline_today__net_breadth` | 5.66 | -4.18 | -9.62 | +2.69 | 74 |
| `52_week_high_low_within_10__high` | 21.60 | +0.72 | +3.42 | +3.74 | 77 |
| `52_week_high_low_within_10__low` | 13.87 | -0.21 | -5.62 | -12.58 | 28 |
| `52_wk_high_low__new_52_wk_high` | 2.02 | -0.13 | -0.17 | +0.67 | 42 |
| `52_wk_high_low__new_52_wk_low` | 0.23 | -0.00 | -0.33 | -0.70 | 3 |
| `52_wk_high_low_today__new_52_wk_high` | 2.01 | -0.13 | +0.48 | +0.61 | 69 |
| `52_wk_high_low_today__new_52_wk_low` | 0.38 | +0.00 | -1.21 | -3.00 | 5 |
| `5_advance_decline_ratio__advance` | 56.95 | -13.90 | -20.33 | -3.92 | 69 |
| `5_advance_decline_ratio__decline` | 42.03 | +13.94 | +20.36 | +3.94 | 33 |
| `above_10ma__pct` | 77.23 | -0.23 | +1.92 | +31.44 | 92 |
| `above_200ma__above_200ma` | 46.62 | +0.82 | +4.86 | +9.88 | 64 |
| `above_20_ema__pct` | 72.43 | +0.92 | +9.48 | +38.39 | 89 |
| `above_20ma__pct` | 72.43 | +0.92 | +9.48 | +38.39 | 89 |
| `above_50_ema__pct` | 56.48 | +2.96 | +11.74 | +26.24 | 71 |
| `above_50ma__above_50ma` | 46.62 | +0.82 | +4.86 | +9.88 | 64 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,143.00 | +18.00 | +119.00 | +175.00 | 76 |
| `breadth_above_500_trend_reversal__above_20dma` | 1,714.00 | +27.00 | +220.00 | +856.00 | 95 |
| `breadth_above_500_trend_reversal__above_50dma` | 1,335.00 | +76.00 | +278.00 | +551.00 | 77 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,203.00 | -19.00 | -118.00 | -180.00 | 54 |
| `breadth_above_500_trend_reversal__below_20dma` | 632.00 | -28.00 | -219.00 | -861.00 | 17 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,011.00 | -77.00 | -277.00 | -556.00 | 36 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 4.00 | -1.00 | +4.00 | +2.00 | 81 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 21.00 | +1.00 | -39.00 | +10.00 | 32 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 14.00 | -10.00 | -17.00 | -8.00 | 48 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 123.00 | -63.00 | -120.00 | -40.00 | 77 |
| `current_previous_yr_volumes_crores__1_yr_back` | 431.02 | -18.48 | -51.94 | -29.49 | 53 |
| `current_previous_yr_volumes_crores__current` | 492.42 | -79.47 | -112.42 | +0.64 | 42 |
| `drawdowns_peaks__blw_3` | 103.00 | +21.00 | -48.00 | -5.00 | 34 |
| `gold_etfs_nifty_1_month_chg__gold` | -6.67 | -1.79 | -1.25 | -0.80 | 28 |
| `gold_etfs_nifty_1_month_chg__nifty` | 12.37 | +1.14 | +8.40 | +17.74 | 100 |
| `mbm_2_0_magnitude__abv_10ma` | 75.94 | -0.34 | +3.32 | +29.25 | 91 |
| `mbm_2_0_magnitude__abv_200ma` | 41.26 | +0.97 | +4.74 | +1.74 | 58 |
| `mbm_2_0_magnitude__abv_20ma` | 70.01 | +0.92 | +11.96 | +33.40 | 89 |
| `mbm_2_0_magnitude__abv_50ma` | 51.64 | +3.38 | +12.89 | +17.67 | 71 |
| `mbm_2_0_velocity_advanced__15_52wh` | 18.53 | +0.98 | +3.45 | -0.74 | 66 |
| `mbm_2_0_velocity_advanced__15_52wl` | 18.72 | -0.62 | -5.19 | -8.94 | 41 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 44.15 | -0.48 | -2.80 | -0.26 | 40 |
| `mbm_2_0_velocity_advanced__30_52wh` | 49.53 | +0.57 | +3.75 | +0.99 | 81 |
| `mbm_2_0_velocity_advanced__breakdowns` | 6.90 | +0.30 | -1.92 | +0.01 | 33 |
| `mbm_2_0_velocity_advanced__breakouts` | 19.70 | -12.11 | -20.69 | -2.29 | 74 |
| `mbm_2_0_velocity_advanced__down_close` | 27.68 | -0.13 | -11.70 | +1.97 | 20 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -0.20 | +1.60 | +8.63 | +8.20 | 59 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 5.38 | +1.04 | +6.55 | +1.25 | 70 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 1.64 | -0.04 | -0.12 | +1.09 | 77 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.87 | -0.04 | -0.43 | +0.37 | 61 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 0.23 | -0.00 | -0.31 | -0.71 | 12 |
| `mbm_2_0_velocity_advanced__up_close` | 39.01 | +1.54 | +2.07 | -3.82 | 59 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.23 | -0.08 | -0.16 | -0.20 | 22 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.13 | -0.20 | -0.74 | -1.35 | 27 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.99 | -0.71 | -1.45 | +0.02 | 52 |
| `mbm_2_0_velocity_basic__3_range` | 40.41 | +8.01 | +15.72 | -0.73 | 52 |
| `mbm_2_0_velocity_basic__4_advance` | 7.68 | -4.24 | -7.24 | -1.73 | 72 |
| `mbm_2_0_velocity_basic__4_decline` | 1.91 | +0.07 | -1.57 | +0.14 | 25 |
| `mbm_2_0_velocity_basic__5d_range` | 3.74 | +1.20 | +3.12 | -0.83 | 40 |
| `mbm_2_0_velocity_basic__net_breadth` | 5.77 | -4.31 | -5.67 | -1.87 | 75 |
| `mbm_2_0_velocity_basic__volume` | 0.61 | -0.48 | -0.79 | +0.22 | 68 |
| `net_breadth__net_breadth` | 5.77 | -4.31 | -5.67 | -1.87 | 75 |
| `net_nh_nl__net_nh_nl` | 1.64 | -0.04 | -0.12 | +1.09 | 61 |
| `new_high_low_bearishness_bullishness__high` | 62.00 | -4.00 | -5.00 | +21.00 | 73 |
| `new_high_low_bearishness_bullishness__low` | 7.00 | +0.00 | -10.00 | -21.00 | 19 |
| `volume__volume` | 0.61 | -0.48 | -0.79 | +0.22 | 80 |

## No reading for 2026-11-12

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-11-09, 66.20
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-11-09, 33.80
- `oversold_overbought_rsi__overbought`: last 2026-11-09, 101.00
- `oversold_overbought_rsi__oversold`: last 2026-11-09, 52.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-11-09, 0.45
- `weekly_rsi_50_50__below_rsi_50`: last 2026-11-09, 0.47


<!-- market-read -->
## Market read

Thursday was a quieter up day that kept every gain from Wednesday and added a little more. The Nifty barely moved and closed near 25,300. The small and micro company indices each rose about one percent, so the smaller end led the larger end. Across the market, 123 stocks rose four and a half percent or more, and 21 fell that hard. Turnover eased to about 490 crore, from about 570 on Wednesday. Realty was the best index of the day, up about four and a half percent. Government banks led the week again, up more than eight percent. Autos fell about one percent as an index, though parts makers still crowd the leader screens. The count above the 50 day line rose to 1,335, its best since 11 August. The count above the 200 day line rose to 1,143, its best since 23 September and about 30 stocks short of half the market. The fear gauge fell about five percent to near 16.6. The repair keeps widening on lighter volume, and the long clock is now close to the halfway mark.

Full brief: briefs/2026-11-12.html
