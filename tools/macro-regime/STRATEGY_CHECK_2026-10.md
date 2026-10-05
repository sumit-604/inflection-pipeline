# Strategy check, 2026-10-05

Monthly long/flat strategies on the regime read, 2004-01 to 2026-09, run in
Python on the data in 284324b with the rules in 0ca0acc. Signal is the
month-end regime, applied to the following month (one-month lag, no
look-ahead). No costs. Aluminium and zinc are monthly averages. These are
the reference numbers for the TradingView strategy
(pine/macro_regime_backtest.pine); a faithful port lands near them.

Columns: annualised return %, annualised volatility %, worst drawdown %.

| Asset | Buy and hold | Long R+G only | Flat only in S | Trend 12m long/flat | Band +1 long/flat |
|---|---|---|---|---|---|
| gold | 10.7 / 17.2 / -42 | 6.2 / 12.8 / -23 | 9.9 / 15.6 / -31 | 9.2 / 15.3 / -27 | 2.1 / 10.2 / -19 |
| silver | 10.7 / 32.7 / -72 | 7.6 / 25.5 / -55 | 12.1 / 29.8 / -68 | 7.3 / 27.6 / -71 | 0.3 / 20.5 / -76 |
| aluminium | 3.3 / 17.7 / -57 | 4.2 / 12.2 / -32 | 5.3 / 15.6 / -56 | 3.7 / 13.9 / -40 | 4.4 / 9.9 / -31 |
| zinc | 6.4 / 23.2 / -75 | 6.0 / 15.7 / -43 | 10.9 / 20.8 / -61 | 8.5 / 18.0 / -40 | 3.3 / 10.9 / -33 |
| brent | 6.0 / 45.3 / -89 | 4.2 / 38.1 / -88 | 4.9 / 43.6 / -86 | 3.0 / 25.0 / -68 | -1.9 / 26.5 / -83 |
| nifty | 11.6 / 20.7 / -55 | 7.7 / 15.1 / -32 | 11.7 / 18.9 / -38 | 7.7 / 17.0 / -34 | -0.2 / 8.7 / -28 |

Reading. Long only in R and G matches trend, not buy-and-hold: being flat
in deflation months misses the recoveries. Flat only in stagflation is the
one rule that helps on five of six assets: it keeps the return and cuts
the drawdown on Nifty (55% to 38%), and adds return on zinc, silver and
aluminium. Gold is best held. The band rule loses everywhere, as
EVALUATION_2026-10.md section 2 showed. Two cycles, no costs; a rule, not
a result.

## Grid search with an out-of-sample split, 2026-10-05

135 rules per asset: every non-empty set of quadrants to be long in (15),
times a liquidity filter (any / not TIGHT / only EASING), times a stress
filter (any / not HIGH / also long when HIGH). Each rule had to be invested
at least 30% of months. Winner chosen by return per unit of volatility on
2004-01 to 2015-12, then run blind on 2016-01 to 2026-09.

| Asset | In-sample winner | IS ann/vol/dd | OOS ann/vol/dd | OOS buy-hold | OOS trend | Held |
|---|---|---|---|---|---|---|
| gold | long R G S | 7.8 / 15.7 / -27 | 6.1 / 13.4 / -23 | 13.6 / 15.2 / -23 | 8.6 / 14.0 / -24 | no |
| silver | R G D, stress not HIGH | 8.9 / 27.9 / -64 | 9.7 / 25.2 / -38 | 14.7 / 30.3 / -38 | 5.5 / 26.5 / -41 | no |
| aluminium | R D, stress not HIGH | 6.8 / 12.6 / -18 | 6.1 / 11.3 / -27 | 7.6 / 15.8 / -39 | 6.8 / 13.5 / -36 | yes |
| zinc | R D, stress not HIGH | 10.3 / 18.6 / -29 | 9.4 / 15.5 / -26 | 9.4 / 20.0 / -46 | 5.3 / 15.3 / -40 | yes |
| brent | R S D, not TIGHT | 12.0 / 20.0 / -33 | 1.2 / 33.9 / -78 | 11.1 / 54.9 / -82 | -0.7 / 25.8 / -68 | no |
| nifty | R G S D, stress not HIGH | 16.4 / 18.0 / -23 | 5.1 / 14.9 / -31 | 10.2 / 16.4 / -29 | 3.5 / 13.8 / -31 | no |

Four of six in-sample winners failed out of sample. The Nifty winner,
"sell when stress is HIGH", fit 2008 and sold the 2020 bottom.

The one rule that held: flat only in STAGFLATION, long otherwise. It was
not the in-sample winner on any asset. Out-of-sample return per unit of
volatility against buy-and-hold: gold 0.98 vs 0.90, silver 0.56 vs 0.48,
aluminium 0.78 vs 0.48, zinc 0.66 vs 0.47, brent 0.14 vs 0.20, nifty 0.73
vs 0.62. It improved from the first half to the second, the opposite of a
fitted rule. It is now the default in pine/macro_regime_backtest.pine.

Reading: with two cycles of data an optimiser finds the rule that explains
the past. The rule to carry is the simplest one that survived a blind
half, and it is one rule, not a per-asset table.

## Regime definition changed to LEVEL, 2026-10-05 (operator ruling)

Direction (sign of the 6-month change in each dial) produced 69 regime
changes in 2004-2026 and called "rising" what the operator means by
"high". The definition is now LEVEL against benchmarks: inflation HIGH
when US CPI YoY is above 3.0% or the 10-year breakeven above 2.5%; growth
HIGH when the smoothed GROWTH dial is above its five-year norm (z > 0).
41 regime changes in the same span. 2008 reads S from January to October,
2022 and 2023 read S throughout, 2015-16 D, 2017 G. September 2026 reads
R under both definitions. Direction stays available (REGIME_MODE in
model.py; "Regime definition" input in Pine). EVALUATION_2026-10.md and
the grid search above were run under the direction definition and are
not rerun; a level-definition evaluation needs its own bar.

Level regime, months 2004-2026 and median 12-month forward return:

| Regime | Months | gold | silver | aluminium | zinc | brent | nifty |
|---|---|---|---|---|---|---|---|
| REFLATION | 49 | +5.7 | +2.3 | +3.2 | +11.7 | +3.0 | +12.3 |
| GOLDILOCKS | 96 | +9.9 | +0.6 | +9.5 | +8.4 | +26.5 | +13.0 |
| STAGFLATION | 46 | +11.8 | +9.0 | -7.7 | -3.6 | -8.7 | +15.0 |
| DEFLATION | 82 | +16.6 | +19.9 | +5.6 | +5.9 | -1.4 | +10.5 |
