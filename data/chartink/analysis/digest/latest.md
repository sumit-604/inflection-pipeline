# Market breadth digest: 2026-10-13

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-10-13: **69** of 79
- History available: 2019-07-01 to 2026-10-13, 696 dated rows
- Metrics with no reading for 2026-10-13: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 36.81 | +6.91 | -1.67 | +3.18 | 39 | 400 |
| % above 20 EMA | 30.21 | +3.41 | -2.51 | -6.57 | 29 | 400 |
| % above 50 EMA | 30.12 | +0.56 | -4.23 | -12.42 | 28 | 400 |
| % above 200 EMA | 38.41 | +0.97 | -3.10 | -8.92 | 46 | 400 |
| Net breadth (4% adv minus dec) | 3.03 | -1.03 | -7.48 | +2.06 | 55 | 400 |
| 4% advancers | 6.18 | -1.23 | -6.14 | +1.73 | 59 | 400 |
| 4% decliners | 3.16 | -0.19 | +1.35 | -0.33 | 58 | 400 |
| Net new highs minus lows | -2.06 | -0.81 | -2.19 | -0.13 | 23 | 400 |
| Net within 15% of 52wk H/L | -10.73 | +1.88 | -2.82 | -14.43 | 35 | 400 |
| Volume expansion ratio | 0.30 | +0.00 | -0.06 | -0.18 | 13 | 400 |
| Overbought count (weekly RSI>70) (as of 2026-10-12) | 131.00 | -3.00 | -116.00 | -32.00 | 46 | 381 |
| Oversold count (weekly RSI<30) (as of 2026-10-12) | 140.00 | -67.00 | +51.00 | +106.00 | 86 | 381 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `breadth_above_500_trend_reversal__below_20dma` | 1,589.00 | -101.00 | 87 |
| `breadth_above_500_trend_reversal__above_20dma` | 670.00 | +100.00 | 26 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,593.00 | -33.00 | 86 |
| `breadth_above_500_trend_reversal__above_50dma` | 666.00 | +32.00 | 24 |
| `4_advance_decline__4_advance` | 147.00 | -30.00 | 51 |
| `4_advance_decline_today__4_advance` | 149.00 | -29.00 | 50 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,357.00 | -27.00 | 76 |
| `breadth_above_500_trend_reversal__above_200dma` | 902.00 | +26.00 | 42 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 101.00 | -17.00 | 68 |
| `new_high_low_bearishness_bullishness__low` | 98.00 | +15.00 | 82 |

## At the edge of their own range

Top decile of history:

- `10_from_10dema__10_10ema` at 1.05 (percentile 95, range 0.09 to 1.17)
- `breadth_above_500_trend_reversal__down_20_in_5d` at 6.00 (percentile 92, range 0.00 to 35.00)
- `52_wk_high_low__new_52_wk_low` at 3.43 (percentile 92, range 0.18 to 7.50)

Bottom decile of history:

- `15_up_10_down__15_in_5d` at 1.26 (percentile 7, range 0.99 to 7.11)
- `net_nh_nl__net_nh_nl` at -2.06 (percentile 8, range -6.31 to 3.67)
- `current_previous_yr_volumes_crores__current` at 415.04 (percentile 9, range 378.80 to 956.94)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 1.05 | -0.12 | +0.17 | +0.46 | 95 |
| `15_up_10_down__10_in_5d` | 2.78 | +0.14 | +0.34 | +0.76 | 79 |
| `15_up_10_down__15_in_5d` | 1.26 | -0.92 | -1.22 | -1.60 | 7 |
| `3_above_200_ema__pct` | 36.10 | +1.23 | -3.04 | -12.72 | 29 |
| `4_advance_decline__4_advance` | 147.00 | -30.00 | -146.00 | +41.00 | 51 |
| `4_advance_decline__4_decline` | 75.00 | -5.00 | +32.00 | -8.00 | 56 |
| `4_advance_decline_today__4_advance` | 149.00 | -29.00 | -147.00 | -19.00 | 50 |
| `4_advance_decline_today__4_decline` | 78.00 | -2.00 | +30.00 | -12.00 | 45 |
| `4_advance_decline_today__net_breadth` | 2.97 | -1.13 | -7.39 | -0.33 | 50 |
| `52_week_high_low_within_10__high` | 18.21 | +0.90 | -2.18 | -7.05 | 37 |
| `52_week_high_low_within_10__low` | 29.17 | -2.08 | +0.77 | +8.67 | 73 |
| `52_wk_high_low__new_52_wk_high` | 1.44 | -0.17 | -0.52 | -0.13 | 11 |
| `52_wk_high_low__new_52_wk_low` | 3.43 | +0.54 | +1.44 | +0.17 | 92 |
| `52_wk_high_low_today__new_52_wk_high` | 1.40 | -0.16 | -0.49 | -2.25 | 18 |
| `52_wk_high_low_today__new_52_wk_low` | 3.39 | +0.62 | +1.37 | +1.67 | 68 |
| `5_advance_decline_ratio__advance` | 60.87 | +11.78 | -9.34 | +22.01 | 86 |
| `5_advance_decline_ratio__decline` | 38.09 | -11.78 | +9.34 | -22.00 | 18 |
| `above_10ma__pct` | 38.41 | +11.00 | +2.63 | +7.79 | 39 |
| `above_200ma__above_200ma` | 36.10 | +1.23 | -3.04 | -12.72 | 29 |
| `above_20_ema__pct` | 28.47 | +4.40 | -0.56 | -4.82 | 23 |
| `above_20ma__pct` | 28.47 | +4.40 | -0.56 | -4.82 | 21 |
| `above_50_ema__pct` | 27.10 | +1.26 | -2.91 | -13.25 | 19 |
| `above_50ma__above_50ma` | 36.10 | +1.23 | -3.04 | -12.72 | 29 |
| `breadth_above_500_trend_reversal__above_200dma` | 902.00 | +26.00 | -73.00 | -277.00 | 42 |
| `breadth_above_500_trend_reversal__above_20dma` | 670.00 | +100.00 | -33.00 | -118.00 | 26 |
| `breadth_above_500_trend_reversal__above_50dma` | 666.00 | +32.00 | -83.00 | -298.00 | 24 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,357.00 | -27.00 | +72.00 | +275.00 | 76 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,589.00 | -101.00 | +32.00 | +116.00 | 87 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,593.00 | -33.00 | +82.00 | +296.00 | 86 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 6.00 | -3.00 | +1.00 | +2.00 | 92 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 28.00 | -10.00 | +5.00 | -10.00 | 46 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 13.00 | -4.00 | -8.00 | -15.00 | 44 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 101.00 | -17.00 | -102.00 | +29.00 | 68 |
| `current_previous_yr_volumes_crores__1_yr_back` | 444.30 | -4.96 | -46.47 | -47.38 | 66 |
| `current_previous_yr_volumes_crores__current` | 415.04 | -12.26 | +24.23 | -114.73 | 9 |
| `drawdowns_peaks__blw_3` | 149.00 | -4.00 | +71.00 | -52.00 | 58 |
| `gold_etfs_nifty_1_month_chg__gold` | -7.40 | -0.72 | +0.03 | -14.13 | 23 |
| `gold_etfs_nifty_1_month_chg__nifty` | -4.76 | +1.08 | +0.56 | -2.16 | 14 |
| `mbm_2_0_magnitude__abv_10ma` | 36.81 | +6.91 | -1.67 | +3.18 | 39 |
| `mbm_2_0_magnitude__abv_200ma` | 38.41 | +0.97 | -3.10 | -8.92 | 46 |
| `mbm_2_0_magnitude__abv_20ma` | 30.21 | +3.41 | -2.51 | -6.57 | 29 |
| `mbm_2_0_magnitude__abv_50ma` | 30.12 | +0.56 | -4.23 | -12.42 | 28 |
| `mbm_2_0_velocity_advanced__15_52wh` | 19.69 | +0.68 | -1.88 | -6.62 | 73 |
| `mbm_2_0_velocity_advanced__15_52wl` | 30.42 | -1.20 | +0.94 | +7.80 | 68 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 48.30 | -0.15 | +2.25 | +6.68 | 53 |
| `mbm_2_0_velocity_advanced__30_52wh` | 50.61 | +1.41 | -0.90 | -2.69 | 81 |
| `mbm_2_0_velocity_advanced__breakdowns` | 12.66 | +3.32 | +6.73 | -1.80 | 73 |
| `mbm_2_0_velocity_advanced__breakouts` | 14.35 | -6.51 | -11.39 | +3.33 | 45 |
| `mbm_2_0_velocity_advanced__down_close` | 24.92 | -10.96 | -5.58 | +0.79 | 13 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | -10.73 | +1.88 | -2.82 | -14.43 | 35 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 2.31 | +1.56 | -3.15 | -9.37 | 59 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | -2.06 | -0.81 | -2.19 | -0.13 | 23 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 1.56 | -0.29 | -0.67 | -0.29 | 48 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 3.62 | +0.52 | +1.52 | -0.17 | 80 |
| `mbm_2_0_velocity_advanced__up_close` | 43.11 | +7.57 | -4.77 | +2.65 | 79 |
| `mbm_2_0_velocity_basic__10_10ema` | 1.05 | -0.12 | +0.17 | +0.46 | 86 |
| `mbm_2_0_velocity_basic__10_in_5d` | 2.78 | +0.14 | +0.34 | +0.76 | 67 |
| `mbm_2_0_velocity_basic__15_in_5d` | 1.26 | -0.92 | -1.22 | -1.60 | 25 |
| `mbm_2_0_velocity_basic__3_range` | 38.20 | +1.73 | -1.96 | -3.92 | 42 |
| `mbm_2_0_velocity_basic__4_advance` | 6.18 | -1.23 | -6.14 | +1.73 | 59 |
| `mbm_2_0_velocity_basic__4_decline` | 3.16 | -0.19 | +1.35 | -0.33 | 58 |
| `mbm_2_0_velocity_basic__5d_range` | 3.95 | +0.48 | +1.56 | -2.52 | 40 |
| `mbm_2_0_velocity_basic__net_breadth` | 3.03 | -1.03 | -7.48 | +2.06 | 55 |
| `mbm_2_0_velocity_basic__volume` | 0.30 | +0.00 | -0.06 | -0.18 | 13 |
| `net_breadth__net_breadth` | 3.03 | -1.03 | -7.48 | +2.06 | 53 |
| `net_nh_nl__net_nh_nl` | -2.06 | -0.81 | -2.19 | -0.13 | 8 |
| `new_high_low_bearishness_bullishness__high` | 41.00 | -5.00 | -15.00 | -6.00 | 44 |
| `new_high_low_bearishness_bullishness__low` | 98.00 | +15.00 | +41.00 | +0.00 | 82 |
| `volume__volume` | 0.30 | +0.00 | -0.06 | -0.18 | 11 |

## No reading for 2026-10-13

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-10-12, 62.98
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-10-12, 37.02
- `oversold_overbought_rsi__overbought`: last 2026-10-12, 131.00
- `oversold_overbought_rsi__oversold`: last 2026-10-12, 140.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-10-12, 0.33
- `weekly_rsi_50_50__below_rsi_50`: last 2026-10-12, 0.65


<!-- market-read -->

## Market read

Tuesday was the third repair day since the 8 October break, and the broadest
for the big names. The Nifty rose about 1.6 percent and the IT index jumped
about five. About six stocks in ten rose. This time the big names led, and the
small company index barely moved. 101 stocks jumped four and a half percent or
more, against 28 that fell that much. Fear eased: the VIX fell about seven
percent to about 14. The count of stocks above the two-hundred-day average
reached 902, a single stock past its 1 October low. That one number says the
long trend picture has just come back to its 1 October level. It has not yet
made back the whole break. Turnover ran below a year ago for a second day, and
new yearly lows ticked up from 83 to 98. The repair is three days old. It is
broad and steady, and it is still quiet.

Full brief: briefs/2026-10-13.html
