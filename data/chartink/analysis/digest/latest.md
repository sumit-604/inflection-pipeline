# Market breadth digest: 2026-09-22

Computed from `market_breadth_daily.csv`. Arithmetic only. No view is expressed and nothing is recommended.

- Metrics reporting on 2026-09-22: **69** of 79
- History available: 2019-07-01 to 2026-09-22, 682 dated rows
- Metrics with no reading for 2026-09-22: 6 (weekly series and slower tiles; see the end)
- Chart guide lines excluded: 4 (constant columns such as the 50/50 marker)

A percentile needs history. Metrics with fewer than 20 readings show `n=<count>` instead of a rank, and are never flagged as extreme.

## Core breadth

Percentile is this reading's rank against that metric's own history. 50 means mid-range, 95 means near the top of its range.

| Metric | Value | 1d | 5d | 20d | Percentile | History |
|---|---:|---:|---:|---:|---:|---:|
| % above 10 EMA | 44.77 | +0.48 | +25.92 | +0.63 | 57 | 386 |
| % above 20 EMA | 40.14 | +1.47 | +16.99 | -5.05 | 43 | 386 |
| % above 50 EMA | 40.86 | +0.38 | +8.19 | -7.92 | 49 | 386 |
| % above 200 EMA | 44.89 | -0.15 | +3.06 | -5.32 | 68 | 386 |
| Net breadth (4% adv minus dec) | 4.37 | -1.66 | +25.06 | +0.07 | 66 | 386 |
| 4% advancers | 6.56 | -2.15 | +3.75 | -0.74 | 62 | 386 |
| 4% decliners | 2.19 | -0.49 | -21.31 | -0.81 | 35 | 386 |
| Net new highs minus lows | 1.22 | -0.12 | +3.31 | -0.93 | 64 | 386 |
| Net within 15% of 52wk H/L | 1.43 | +0.97 | +6.79 | -7.21 | 59 | 386 |
| Volume expansion ratio | 0.41 | -0.01 | -0.20 | -0.11 | 38 | 386 |
| Overbought count (weekly RSI>70) (as of 2026-09-21) | 198.00 | -2.00 | -67.00 | +25.00 | 66 | 378 |
| Oversold count (weekly RSI<30) (as of 2026-09-21) | 78.00 | -4.00 | +22.00 | +57.00 | 77 | 378 |

## Largest one-day moves

| Metric | Value | 1d change | Percentile |
|---|---:|---:|---:|
| `current_previous_yr_volumes_crores__1_yr_back` | 498.24 | +77.72 | 87 |
| `4_advance_decline__4_advance` | 156.00 | -52.00 | 52 |
| `4_advance_decline_today__4_advance` | 158.00 | -50.00 | n=9 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 102.00 | -41.00 | 68 |
| `current_previous_yr_volumes_crores__current` | 469.75 | +34.33 | 33 |
| `drawdowns_peaks__blw_3` | 120.00 | -17.00 | 47 |
| `breadth_above_500_trend_reversal__above_50dma` | 916.00 | -15.00 | 47 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,336.00 | +13.00 | 73 |
| `4_advance_decline__4_decline` | 52.00 | -12.00 | 28 |
| `new_high_low_bearishness_bullishness__high` | 71.00 | -11.00 | 79 |

## At the edge of their own range

Top decile of history:

- `mbm_2_0_velocity_advanced__15_52wh` at 25.09 (percentile 92, range 2.78 to 28.64)
- `mbm_2_0_velocity_advanced__30_52wh` at 52.92 (percentile 91, range 16.60 to 55.86)

## All metrics reporting today

| Metric | Value | 1d | 5d | 20d | Percentile |
|---|---:|---:|---:|---:|---:|
| `10_from_10dema__10_10ema` | 0.29 | -0.12 | -0.75 | -0.13 | 11 |
| `15_up_10_down__10_in_5d` | 1.13 | -1.59 | -5.02 | -0.26 | 18 |
| `15_up_10_down__15_in_5d` | 3.03 | +1.18 | +1.48 | -0.05 | 73 |
| `3_above_200_ema__pct` | 45.52 | -0.27 | +3.66 | -8.57 | 55 |
| `4_advance_decline__4_advance` | 156.00 | -52.00 | +89.00 | -17.00 | 52 |
| `4_advance_decline__4_decline` | 52.00 | -12.00 | -509.00 | -19.00 | 28 |
| `4_advance_decline_today__4_advance` | 158.00 | -50.00 | +17.00 | NOT FOUND | n=9 |
| `4_advance_decline_today__4_decline` | 57.00 | -7.00 | -38.00 | NOT FOUND | n=9 |
| `4_advance_decline_today__net_breadth` | 4.22 | -1.80 | +2.28 | NOT FOUND | n=9 |
| `52_week_high_low_within_10__high` | 24.89 | +0.16 | +4.64 | -2.88 | 87 |
| `52_week_high_low_within_10__low` | 21.92 | -0.00 | -1.52 | +6.28 | 62 |
| `52_wk_high_low__new_52_wk_high` | 2.49 | -0.37 | +0.60 | -0.61 | 38 |
| `52_wk_high_low__new_52_wk_low` | 1.51 | -0.16 | -2.17 | +0.27 | 80 |
| `52_wk_high_low_today__new_52_wk_high` | 2.34 | -0.36 | -0.65 | NOT FOUND | n=9 |
| `52_wk_high_low_today__new_52_wk_low` | 1.50 | -0.13 | -0.77 | NOT FOUND | n=9 |
| `5_advance_decline_ratio__advance` | 43.83 | -5.11 | +7.26 | NOT FOUND | n=9 |
| `5_advance_decline_ratio__decline` | 55.13 | +5.11 | -7.25 | NOT FOUND | n=9 |
| `above_10ma__pct` | 41.25 | -1.93 | +23.61 | -2.63 | 44 |
| `above_200ma__above_200ma` | 45.52 | -0.27 | +3.66 | -8.57 | 54 |
| `above_20_ema__pct` | 35.89 | +0.33 | +14.84 | -9.83 | 31 |
| `above_20ma__pct` | 35.89 | +0.33 | +14.84 | -9.83 | 25 |
| `above_50_ema__pct` | 37.71 | -0.42 | +8.38 | -15.71 | 27 |
| `above_50ma__above_50ma` | 45.52 | -0.27 | +3.66 | -8.57 | 54 |
| `breadth_above_500_trend_reversal__above_200dma` | 1,116.00 | -8.00 | +87.00 | -166.00 | 73 |
| `breadth_above_500_trend_reversal__above_20dma` | 853.00 | +7.00 | +381.00 | -188.00 | 38 |
| `breadth_above_500_trend_reversal__above_50dma` | 916.00 | -15.00 | +217.00 | -322.00 | 47 |
| `breadth_above_500_trend_reversal__below_200dma` | 1,136.00 | +6.00 | -90.00 | +164.00 | 50 |
| `breadth_above_500_trend_reversal__below_20dma` | 1,399.00 | -9.00 | -384.00 | +187.00 | 75 |
| `breadth_above_500_trend_reversal__below_50dma` | 1,336.00 | +13.00 | -220.00 | +320.00 | 73 |
| `breadth_above_500_trend_reversal__down_20_in_5d` | 2.00 | +2.00 | -5.00 | +0.00 | 62 |
| `breadth_above_500_trend_reversal__down_4_5_today` | 21.00 | -6.00 | -321.00 | -17.00 | 34 |
| `breadth_above_500_trend_reversal__up_20_in_5d` | 26.00 | +9.00 | +10.00 | +2.00 | 78 |
| `breadth_above_500_trend_reversal__up_4_5_today` | 102.00 | -41.00 | +59.00 | -8.00 | 68 |
| `current_previous_yr_volumes_crores__1_yr_back` | 498.24 | +77.72 | +99.47 | +165.68 | 87 |
| `current_previous_yr_volumes_crores__current` | 469.75 | +34.33 | +4.69 | -98.35 | 33 |
| `drawdowns_peaks__blw_3` | 120.00 | -17.00 | -877.00 | -76.00 | 47 |
| `gold_etfs_nifty_1_month_chg__gold` | 0.28 | -1.40 | -5.08 | -13.44 | 47 |
| `gold_etfs_nifty_1_month_chg__nifty` | -3.83 | -0.37 | +1.62 | -3.32 | 13 |
| `mbm_2_0_magnitude__abv_10ma` | 44.77 | +0.48 | +25.92 | +0.63 | 57 |
| `mbm_2_0_magnitude__abv_200ma` | 44.89 | -0.15 | +3.06 | -5.32 | 68 |
| `mbm_2_0_magnitude__abv_20ma` | 40.14 | +1.47 | +16.99 | -5.05 | 43 |
| `mbm_2_0_magnitude__abv_50ma` | 40.86 | +0.38 | +8.19 | -7.92 | 49 |
| `mbm_2_0_velocity_advanced__15_52wh` | 25.09 | +0.52 | +3.82 | -2.43 | 92 |
| `mbm_2_0_velocity_advanced__15_52wl` | 23.67 | -0.45 | -2.97 | +4.78 | 59 |
| `mbm_2_0_velocity_advanced__30_52_wl` | 43.21 | -0.15 | -2.01 | +4.00 | 39 |
| `mbm_2_0_velocity_advanced__30_52wh` | 52.92 | -0.03 | +1.75 | -2.47 | 91 |
| `mbm_2_0_velocity_advanced__breakdowns` | 6.68 | -1.81 | -29.96 | -2.63 | 33 |
| `mbm_2_0_velocity_advanced__breakouts` | 16.90 | -0.68 | +2.66 | -2.07 | 63 |
| `mbm_2_0_velocity_advanced__down_close` | 32.70 | +1.18 | -31.41 | +0.58 | 43 |
| `mbm_2_0_velocity_advanced__net_15_h_l` | 1.43 | +0.97 | +6.79 | -7.21 | 59 |
| `mbm_2_0_velocity_advanced__net_30_h_l` | 9.71 | +0.12 | +3.76 | -6.48 | 76 |
| `mbm_2_0_velocity_advanced__net_nh_nl` | 1.22 | -0.12 | +3.31 | -0.93 | 64 |
| `mbm_2_0_velocity_advanced__new_52_wk_high` | 2.82 | -0.32 | +0.56 | -0.56 | 87 |
| `mbm_2_0_velocity_advanced__new_52_wk_low` | 1.60 | -0.20 | -2.76 | +0.37 | 62 |
| `mbm_2_0_velocity_advanced__up_close` | 38.81 | -10.72 | +19.10 | +0.36 | 57 |
| `mbm_2_0_velocity_basic__10_10ema` | 0.29 | -0.12 | -0.75 | -0.13 | 33 |
| `mbm_2_0_velocity_basic__10_in_5d` | 1.13 | -1.59 | -5.02 | -0.26 | 30 |
| `mbm_2_0_velocity_basic__15_in_5d` | 3.03 | +1.18 | +1.48 | -0.05 | 76 |
| `mbm_2_0_velocity_basic__3_range` | 43.46 | +1.86 | +26.21 | +3.88 | 59 |
| `mbm_2_0_velocity_basic__4_advance` | 6.56 | -2.15 | +3.75 | -0.74 | 62 |
| `mbm_2_0_velocity_basic__4_decline` | 2.19 | -0.49 | -21.31 | -0.81 | 35 |
| `mbm_2_0_velocity_basic__5d_range` | 5.04 | +1.78 | +0.52 | -7.56 | 48 |
| `mbm_2_0_velocity_basic__net_breadth` | 4.37 | -1.66 | +25.06 | +0.07 | 66 |
| `mbm_2_0_velocity_basic__volume` | 0.41 | -0.01 | -0.20 | -0.11 | 38 |
| `net_breadth__net_breadth` | 4.37 | -1.66 | +25.06 | +0.07 | 63 |
| `net_nh_nl__net_nh_nl` | 1.22 | -0.12 | +3.31 | -0.93 | 30 |
| `new_high_low_bearishness_bullishness__high` | 71.00 | -11.00 | +14.00 | -22.00 | 79 |
| `new_high_low_bearishness_bullishness__low` | 43.00 | -5.00 | -68.00 | +6.00 | 65 |
| `volume__volume` | 0.41 | -0.01 | -0.20 | -0.11 | 38 |

## No reading for 2026-09-22

These are weekly or slower series. The date shown is their last reading.

- `nifty_500_above_below_200_ema__above_200_ema`: last 2026-09-21, 66.47
- `nifty_500_above_below_200_ema__below_200_ema`: last 2026-09-21, 33.53
- `oversold_overbought_rsi__overbought`: last 2026-09-21, 198.00
- `oversold_overbought_rsi__oversold`: last 2026-09-21, 78.00
- `weekly_rsi_50_50__above_rsi_50`: last 2026-09-21, 0.44
- `weekly_rsi_50_50__below_rsi_50`: last 2026-09-21, 0.53


<!-- market-read -->

## Market read

The market climbed back from last Tuesday's washout without a thrust day. A
thrust day is a session where 300 or more stocks jump four and a half percent.
The best day this week had 166, on Friday, and each day since has had fewer.
The short-term count repaired fast. About 850 stocks now sit above their
twenty-day line, against about 470 a week ago. The long-term floor did not
repair. Slightly fewer stocks sit above their two-hundred-day line than below
it. Yearly highs doubled, and small companies lead them. Fear fell back to
cheap. Gold's lead over stocks shrank to a third of its size a week ago. The
Nifty sits below its long trend line, while the smallcap and microcap indices
sit above theirs. It is a quiet, thin repair of the short end, with the long
end still undecided.

Full brief: briefs/2026-09-22.html
