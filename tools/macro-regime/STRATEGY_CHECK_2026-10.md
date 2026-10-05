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
