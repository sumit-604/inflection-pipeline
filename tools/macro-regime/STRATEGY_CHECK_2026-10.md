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

"Flat only in stagflation" rerun under the level definition, same
2004-01 to 2015-12 / 2016-01 to 2026-09 split. It held out of sample on
three of six assets (the direction definition held on five). Columns:
buy-and-hold | flat only in S, each as annualised return / volatility /
worst drawdown.

| Asset | Full, hold | Full, flat in S | IS hold | IS flat in S | OOS hold | OOS flat in S | Held OOS |
|---|---|---|---|---|---|---|---|
| gold | 10.7 / 17.2 / -42 | 9.0 / 15.0 / -45 | 8.1 / 18.8 / -42 | 6.5 / 15.8 / -45 | 13.6 / 15.2 / -23 | 11.8 / 14.0 / -23 | no |
| silver | 10.7 / 32.7 / -72 | 10.5 / 29.5 / -75 | 7.2 / 34.8 / -72 | 8.6 / 31.1 / -75 | 14.7 / 30.3 / -38 | 12.7 / 27.7 / -38 | no |
| aluminium | 3.3 / 17.7 / -57 | 6.0 / 15.3 / -43 | -0.3 / 19.3 / -57 | 1.9 / 16.8 / -43 | 7.6 / 15.8 / -39 | 10.7 / 13.4 / -37 | yes |
| zinc | 6.4 / 23.2 / -75 | 10.7 / 20.0 / -46 | 3.8 / 25.8 / -75 | 9.3 / 23.2 / -45 | 9.4 / 20.0 / -46 | 12.4 / 15.9 / -46 | yes |
| brent | 6.0 / 45.3 / -89 | 11.0 / 43.0 / -90 | 1.6 / 34.7 / -74 | 8.1 / 30.6 / -75 | 11.1 / 54.9 / -82 | 14.3 / 53.5 / -82 | yes |
| nifty | 11.6 / 20.7 / -55 | 12.2 / 17.7 / -29 | 12.8 / 24.0 / -55 | 16.5 / 19.5 / -26 | 10.2 / 16.4 / -29 | 7.6 / 15.4 / -29 | no |

Reading. Under the level definition the stagflation flag is a metals and
oil rule. For Nifty it cut the 2008 drawdown (55% to 29%) but cost 2.6
points a year after 2016. The Pine strategy default (long R, G, D; flat
S) is unchanged; use it on the metals and Brent, and read this table
before using it on Nifty.

## India regime, 2026-10-05 (operator request)

The operator asked for an India-specific regime beside the global one:
growth or inflation can be present in India and absent in the US, or the
reverse. Added to model.py, run.py, analogues.py and the Pine indicator.

Definition (level): India inflation HIGH when MoSPI CPI (Combined, All
India, General) YoY is above 5.0%, the RBI 4% target plus one point (the
same margin the US benchmark gives the Fed's 2%). India growth HIGH when
the IN_GROWTH dial (IIP YoY, OECD CLI 6-month change, Nifty 6-month log
change; trailing 5-year z, 3-month smoothed) is above zero. Data: MoSPI
API (api.mospi.gov.in; raw JSON under data/raw/mospi_*.json). IIP is
four base years spliced, each used from its second year, 1995-04 to
2026-08 with 2004-04 to 2005-03 null at source. CPI is MoSPI from
2014-01 (base 2012 to 2025-12, base 2024 from 2026-01) and the FRED OECD
series before; on the overlap the OECD series differs from MoSPI by up to
5.6 points, so MoSPI wins where it exists.

What the India regime governs: Nifty and Indian rates. The global regime
governs gold, silver, the base metals and Brent. When the two differ the
read says DIVERGENCE. They differed in 69% of months, 1998-05 to 2026-09
(341 months). India changed regime 63 times in that span, the global
regime 50; median India spell 3 months.

Nifty 12 months on, median, by regime (months since 1998-05):

| Regime | India: months | India: Nifty 12m | Global: months | Global: Nifty 12m |
|---|---|---|---|---|
| REFLATION | 94 | +16.6% | 43 | +14.9% |
| GOLDILOCKS | 77 | +13.7% | 119 | +13.4% |
| STAGFLATION | 94 | +10.4% | 62 | +7.0% |
| DEFLATION | 64 | +0.4% | 105 | +10.8% |

The India DEFLATION bucket (growth below norm, CPI under 5%) is the one
cell where Nifty's forward median is near zero. The full global x India
cross-table is printed in latest.md each month under "India regime
analogues".

As a Nifty timing rule the India regime did not beat holding. Monthly
long/flat, signal at month close applied next month, no costs, 2004-01
to 2026-09, then the 2004-2015 / 2016-2026 split:

| Rule | Full | IS 2004-15 | OOS 2016-26 |
|---|---|---|---|
| Buy and hold | 11.6 / 20.7 / -55 | 12.8 / 24.0 / -55 | 10.2 / 16.4 / -29 |
| Global: flat only in S | 12.2 / 17.7 / -29 | 16.5 / 19.5 / -26 | 7.6 / 15.4 / -29 |
| India: flat only in d | 9.4 / 20.0 / -55 | 11.7 / 23.7 / -55 | 6.9 / 14.8 / -34 |
| India: long r and g only | 8.9 / 13.5 / -23 | 11.3 / 16.2 / -23 | 6.3 / 9.5 / -12 |
| Both: flat if global S or India d | 11.0 / 16.9 / -34 | 16.3 / 19.3 / -26 | 5.3 / 13.7 / -34 |

Reading. The India regime is a read of where India stands, and it is
right to show it beside the global one: the two disagree more often than
they agree. It is not a switch to trade Nifty on. Its spells are short
(median 3 months) and the one-month lag eats the DEFLATION signal. The
Pine indicator exports "india quadrant 0-3" so the operator can test her
own rules; the numbers above are the reference.

Current read (2026-09): global REFLATION, India GOLDILOCKS, DIVERGENCE.
India CPI 4.82% in August against the 5.0% line and rising for ten
months; IN_GROWTH z +0.00 (IIP +8.0% YoY pulls up, Nifty 6m change pulls
down). Both India inputs sit on their lines; the likeliest next India
read is REFLATION (CPI crosses 5%), which is what followed 12 of the 16
closed India GOLDILOCKS spells since 1998.

## India growth test rebuilt on fixed benchmarks (Design A), 2026-10-05

Operator ruling 2026-10-05. The India growth dial (z-scores of IIP, OECD
CLI and Nifty 6m change against their 5-year norm) is replaced as the
default by a majority vote on three fixed benchmarks, in line with the
inflation rule: IIP YoY 3-month mean above 4% (industry); services GVA
YoY above 7% (the 55% of GVA that IIP misses; quarterly, MoSPI national
accounts, known two months after quarter end, held for the quarter);
bank credit YoY above 12% (BIS credit from domestic banks, FRED
CRDQINBPABIS, quarterly, held; the TradingView port reads the RBI
monthly loan-growth feed instead). Growth HIGH when a strict majority
of the available tests pass: two of three, or both of two before the
quarterly GVA series starts (2012-08). Nifty is out of the India test.
The PMIs were the first choice for the services leg but are not in the
Pine economic-data list, so services GVA stands in on both sides.

India strip by year, new (vote) and old (z-score dial). One letter per
month; . = not computable.

| Year | New: vote on benchmarks | Old: z-score dial |
|---|---|---|
| 2005 | `....GGGGGGRR` | `GGGGGGGGGGRR` |
| 2006 | `GGGGRRRRRRRR` | `GGGGRRRRRRRR` |
| 2007 | `RRRRRRRRRRRR` | `RRRRRRRRRRRR` |
| 2008 | `RRRRRRRRRRRS` | `RRSSSSSSSSSS` |
| 2009 | `SSSSSSSSSSSR` | `SSSSSRRRRRRR` |
| 2010 | `SSSRRRRRRRRR` | `RRRRRRSSSSSS` |
| 2011 | `RRRRRRRRSSSS` | `SSSSSSSSSSSS` |
| 2012 | `SSSSSSSRRRRR` | `SSSSSSSSSSSS` |
| 2013 | `RRRRRSSRRRRR` | `SSRRRSSSSRRR` |
| 2014 | `RRRRSRRRRDDD` | `RRRRRRRRRGGG` |
| 2015 | `RSSDSSDDDGSR` | `RRRGSSDDDDSS` |
| 2016 | `SRGRRRRRGGGD` | `SSDSSRRRGGDD` |
| 2017 | `DDDDDDDDDDDS` | `DDDDGGGGGGGR` |
| 2018 | `SGGGDDGGGGGD` | `RGGGGGGGGGDD` |
| 2019 | `GDDDGGDDDDSS` | `DDDDDDDDDDSS` |
| 2020 | `SSSSSSSSSSSD` | `SSSSSSSSRRRG` |
| 2021 | `DSSDSSSRGGDS` | `GRRGRRRRGGGR` |
| 2022 | `SSSSSSSRSRRR` | `RSSSSSSSSSSR` |
| 2023 | `RRRGGGRRRGRR` | `RRSDDDRRRGRR` |
| 2024 | `SRGGGRGGRRRR` | `RRGGGRGGRRRS` |
| 2025 | `GGGGDDDGGGGG` | `DDDDDDDDDDDD` |
| 2026 | `GGGGGGGGG` | `DDDDDDDDG` |

Regime changes: new 86 in 367 months (median spell 2), old 63 in 341 months (median spell 3). Most flips on both sides come from CPI crossing the 5% line, not from growth.

Nifty 12 months on, median, by India regime:

| Regime | New: months | New: Nifty 12m | Old: months | Old: Nifty 12m |
|---|---|---|---|---|
| REFLATION | 136 | +9.3% | 94 | +16.6% |
| GOLDILOCKS | 74 | +9.6% | 77 | +13.7% |
| STAGFLATION | 85 | +13.2% | 94 | +10.4% |
| DEFLATION | 60 | +4.6% | 64 | +0.4% |

Reading. The two definitions disagree most where it matters now. The
old dial read India DEFLATION for all of 2025 and to August 2026 because
IIP growth of 2 to 5% sat below a five-year norm that still held the
2021-23 rebound, and Nifty's 6-month change was negative. The vote reads
2025 as GOLDILOCKS with a two-month DEFLATION dip (May-June 2025, all
three tests failing): services GVA ran 7.5 to 9%, credit 12%, IIP mixed.
That is the official-data picture of 2025: inflation collapsing, growth
intact, markets weak. 2020 reads STAGFLATION all year (CPI above 6%,
growth tests failing), 2017 DEFLATION (demonetisation and GST year, CPI
under 5%), 2008 REFLATION until the last quarter. The new strip
separates Nifty's forward return less than the old one did, which is
expected: the old dial carried Nifty's own 6-month change inside it.

Current read (2026-09): 2 of 2 tests pass (IIP 3m mean 7.8%, services
GVA 10.0% for Apr-Jun 2026; the BIS credit series ends 2025-12 and is
NOT FOUND for 2026-05 on). India GOLDILOCKS, CPI 4.82% against 5.0%.

### India z-score dial rebuilt on the vote's inputs, 2026-10-05

Operator ruling 2026-10-05, after seeing the two definitions read 2025
opposite ways (dial D, vote G). The dial had three inputs: IIP, the OECD
leading indicator (ended 2024-01) and Nifty's 6-month change, so from
2024 it was half IIP and half Nifty, reading the market and calling it
growth. It now reads the same three inputs as the vote (IIP YoY 3-month
mean, services GVA YoY, bank credit YoY) as z-scores against their
5-year norm. The vote asks the absolute question (healthy pace or not);
the dial asks the relative one (faster or slower than the recent past).
Neither uses a price. Both sides (model.py, Pine) changed.

| Year | Vote (default) | Dial, rebuilt |
|---|---|---|
| 2005 | `....GGGGGGRR` | `GGGGGGGGGGRR` |
| 2006 | `GGGGRRRRRRRR` | `GGGGRRRRRRRR` |
| 2007 | `RRRRRRRRRRRR` | `RRRRRRRRRRRR` |
| 2008 | `RRRRRRRRRRRS` | `RRRRRSSSSSSS` |
| 2009 | `SSSSSSSSSSSR` | `SSSSSSSSSSSS` |
| 2010 | `SSSRRRRRRRRR` | `SSSSSSSSSSSS` |
| 2011 | `RRRRRRRRSSSS` | `SRRRRSSSSSSS` |
| 2012 | `SSSSSSSRRRRR` | `SSSSSSSSSSSS` |
| 2013 | `RRRRRSSRRRRR` | `SSSSSSSSSSSS` |
| 2014 | `RRRRSRRRRDDD` | `SSSSSSSSSDDD` |
| 2015 | `RSSDSSDDDGSR` | `SSSDSSDDDDSS` |
| 2016 | `SRGRRRRRGGGD` | `SSDRRRRRGGGG` |
| 2017 | `DDDDDDDDDDDS` | `DDDDDDDDDDDS` |
| 2018 | `SGGGDDGGGGGD` | `SDGGDDDGGGGG` |
| 2019 | `GDDDGGDDDDSS` | `DDDDDGGDDDSS` |
| 2020 | `SSSSSSSSSSSD` | `SSSSSSSSSSSD` |
| 2021 | `DSSDSSSRGGDS` | `DSSDSRRRGGGR` |
| 2022 | `SSSSSSSRSRRR` | `RRSSRRRRRRRR` |
| 2023 | `RRRGGGRRRGRR` | `RRRGGGRRRGRR` |
| 2024 | `SRGGGRGGRRRR` | `RRGGGRGGRRRR` |
| 2025 | `GGGGDDDGGGGG` | `GGGGGGGGGGGG` |
| 2026 | `GGGGGGGGG` | `GGGGGGGGG` |

The two agree in 70% of months since 1998-02 (the old dial agreed with the vote far less). Dial regime changes 62 in 344 months; vote 86 in 367. Both read 2025 and 2026 as GOLDILOCKS. Where they still differ (2010-2014) the dial reads S where the vote reads R: growth was healthy in absolute terms but below the 2005-2010 norm while CPI ran above 5%.

Current read (2026-09): dial z +0.83 (2 of 3 inputs, credit NOT FOUND after 2026-04), vote 2 of 2. India GOLDILOCKS on both.

## Asset read by regime, 2026-10-07 (reference numbers in the Pine table)

Operator question 2026-10-07: what do the current regime and liquidity
say for zinc and aluminium, and how to see it on the chart. The indicator
now carries two "asset read" rows (inputs: Asset read, row 1 and row 2;
defaults aluminium and zinc) that print, for the current global regime
(India regime for nifty), the numbers below. They are hard-coded from this
table, not computed on the chart, and are reference only: the exposure
bands failed their bar and nothing here is a forecast.

Level definition, months 2004-01 to 2025-09 (12-month forward windows).
up = share of windows that ended higher; med = median 12m return; holds =
median when the same regime was still in place 6 months later; turns =
median when it had changed. n = months in the regime.

| Asset | Regime | n | up | med | holds | turns |
|---|---|---|---|---|---|---|
| gold | REFLATION | 41 | 66% | +5.7% | +16.7% (n=16) | +2.9% (n=25) |
| gold | GOLDILOCKS | 92 | 62% | +9.9% | +10.1% (n=43) | +5.7% (n=49) |
| gold | STAGFLATION | 46 | 91% | +11.8% | +11.8% (n=26) | +12.5% (n=20) |
| gold | DEFLATION | 82 | 77% | +16.6% | +17.7% (n=45) | +8.6% (n=37) |
| silver | REFLATION | 41 | 51% | +2.3% | +34.6% (n=16) | -6.5% (n=25) |
| silver | GOLDILOCKS | 92 | 52% | +0.6% | +7.9% (n=43) | -4.8% (n=49) |
| silver | STAGFLATION | 46 | 70% | +9.0% | +8.5% (n=26) | +12.2% (n=20) |
| silver | DEFLATION | 82 | 68% | +19.9% | +19.5% (n=45) | +22.7% (n=37) |
| aluminium | REFLATION | 41 | 54% | +3.2% | +23.2% (n=16) | -10.9% (n=25) |
| aluminium | GOLDILOCKS | 92 | 68% | +9.5% | +14.2% (n=43) | +1.1% (n=49) |
| aluminium | STAGFLATION | 46 | 35% | -7.7% | -10.1% (n=26) | -5.1% (n=20) |
| aluminium | DEFLATION | 82 | 57% | +5.6% | -4.4% (n=45) | +20.7% (n=37) |
| zinc | REFLATION | 41 | 66% | +11.7% | +60.7% (n=16) | -4.4% (n=25) |
| zinc | GOLDILOCKS | 92 | 57% | +8.4% | +15.7% (n=43) | -7.3% (n=49) |
| zinc | STAGFLATION | 46 | 43% | -3.6% | -23.3% (n=26) | +7.8% (n=20) |
| zinc | DEFLATION | 82 | 60% | +5.9% | -0.4% (n=45) | +24.0% (n=37) |
| brent | REFLATION | 41 | 59% | +3.0% | +24.5% (n=16) | -2.2% (n=25) |
| brent | GOLDILOCKS | 92 | 72% | +26.5% | +32.2% (n=43) | +11.4% (n=49) |
| brent | STAGFLATION | 46 | 28% | -8.7% | -12.6% (n=26) | -5.5% (n=20) |
| brent | DEFLATION | 82 | 48% | -1.4% | -17.7% (n=45) | +27.6% (n=37) |
| nifty | REFLATION | 41 | 83% | +12.3% | +36.0% (n=16) | +9.9% (n=25) |
| nifty | GOLDILOCKS | 92 | 77% | +13.0% | +15.4% (n=43) | +7.3% (n=49) |
| nifty | STAGFLATION | 46 | 83% | +15.0% | +15.0% (n=26) | +12.1% (n=20) |
| nifty | DEFLATION | 82 | 77% | +10.5% | +7.1% (n=45) | +19.6% (n=37) |

Reading for the metals in REFLATION. On their own the REFLATION months
are near a coin toss (aluminium up 54%, zinc 66%). The split is by what
came next. When REFLATION was still in place six months on (16 months),
aluminium's 12m median was +23% and zinc's +61%, up 88% and 100% of
the time. When it had turned to STAGFLATION six months on (13 months),
aluminium's median was -22% and zinc's -11%, up 15% and 23% of the
time. Both metals were already up more than 20% on the year in the
2006, 2011 and 2021-22 reflation months; after those, aluminium was
flat (median -2.4%, n=23) and zinc still rose (median +22%, n=32).
Small samples, three episodes; a prior, not a probability.

## RBI publications as the India source, 2026-10-08 (operator ruling)

Operator ruling 2026-10-08: India macro data is taken from RBI's own
publications. First two in use: the Monetary Policy Report of October 2026
and the Governor's Statement of 7 October 2026 (verbatim text under
data/raw/rbi_*; parsed by build_data.py rbi(), no number typed).

Cross-check against what the model already held:

| Series | Model before | RBI | Effect |
|---|---|---|---|
| Manufacturing GVA YoY, Q1 FY26 to Q1 FY27 | 8.3, 10.0, 9.0, 7.9, 9.2 (MoSPI) | 8.3, 10.0, 9.0, 7.9, 9.2 (MPR Table III.9, p63) | identical |
| Services GVA YoY, same quarters | 8.0, 9.1, 10.1, 11.5, 10.0 (MoSPI, three service industries) | 7.6, 8.9, 9.6, 11.0, 9.7 (RBI "Services" includes construction) | definition gap of 0.2 to 0.5 points; no quarter crosses 7% |
| Bank credit YoY, Mar-25 to Dec-25 | 11.7, 12.5, 13.2, 16.8 (BIS via FRED) | 11.0, 9.5 (Jun), 10.4 (Sep), 14.5 (MPR Table II.5, p42) | BIS ran 0.7 to 3.0 points high; RBI now governs from 2025-03 |

The credit correction moves the 2025 India read. With RBI credit at 9.5 to
10.4% from June to September 2025, the credit test fails where BIS had it
passing. The vote now reads 2025 as `GGGGDDDGGDGG` (was `GGGGDDDGGGGG`);
the z-score dial reads `GGGGGGDDDDDD` (was all G). Python now agrees with
the TradingView strip, which already read the RBI loan-growth feed.

Current read (2026-09): India GOLDILOCKS, 3 of 3 growth tests pass (IIP
3m mean 7.8%, services GVA 10.0%, RBI bank credit 19.1% in August).

RBI's own outlook (Governor's Statement, 7 October 2026): repo rate
raised 25 bps to 5.50%, stance changed to calibrated tightening, "rate
cuts are off the table in the near term". CPI projected 4.9% Jul-Sep,
6.0% Oct-Dec, 5.7% Jan-Mar, 5.6% Apr-Jun 2027; real GDP 7.2%, 6.9%, 6.8%,
7.1%. On RBI's path India CPI crosses the 5% benchmark in Oct-Dec with
growth still passing every test: the model's next India read would be
REFLATION. latest.md now prints this line; it is a forecast and the model
still switches only on the published CPI print.

Open: RBI bank credit history before 2025-03 is still BIS. The RBI series
(Handbook of Statistics / DBIE, SCB non-food credit) would replace it.
