# Macro direction model: backtest, October 2026

Generated 2026-10-04 by `python backtest.py`. Decision months 2004-01 to 2026-08 (the last month with a known 1-month outcome). Tables are machine output; the paragraphs under each asset are the reviewer's reading of them (verdicts.md).

**Verdict: in its v1 form, the rule model does not earn the operator's attention as a forecaster.** At the 1-month horizon it beats the trend baseline by more than 2 points on two of eight series: zinc (+6.0) and aluminium (+2.2). At the 3-month horizon it clears 2 points on none of them. Gold (INR) comes closest at +1.9. It loses to trend on silver, Nifty and both INR metals. "Always up" beats the model at 3 months on all eight series. At 1 month the logistic model loses to the rules on five series, ties on one, and wins on two (Brent, Nifty). On Nifty it still trails "always up".  Keep the rules as the primary model. Neither model forecasts well.

**The data handicap is real.** Read every number with it:
- The real yield (DFII10) was never fetched, so the gold and silver driver never voted.
- The breakeven series ends in 2019-10, so the regime layer voted only from 2004 to 2019.
- The dollar series ends in 2025-12.
- FPI flows before 2020 come from a GitHub file with no stated source.

The full-rule test is therefore the 2004-2019 window, and it reads the same: zinc +5.0 and aluminium +2.7 at 1 month, Brent +5.2 at 3 months on only 99 calls, and the rest inside noise or negative. The one useful finding is in section 4. On Nifty, a trend rule scores 59.5% on monthly AVERAGE prices but only 54.7% on month-end prices. The Pink Sheet is a monthly-average series, so every commodity hit rate here may be several points better than a tradeable version would show.

## 1. Data

Full detail, URLs and fetch dates: `data/sources.md`. MIRROR means the primary host refused this cloud shell and a public GitHub copy of the same upstream file served it. FAILED series vote 0.

| Series | Status | First | Last |
|---|---|---|---|
| pinksheet_monthly_avg.csv (CMO Monthly Prices) | MIRROR | 1960-01 | 2026-09 |
| fred_DFII10.csv (DFII10) | FAILED |  |  |
| fred_DTWEXBGS.csv (DTWEXBGS) | MIRROR | 2006-01 | 2025-12 |
| fred_T10YIE.csv (T10YIE) | MIRROR | 2003-01 | 2019-10 |
| fred_FEDFUNDS.csv (FEDFUNDS) | MIRROR | 2003-01 | 2026-07 |
| fred_DEXINUS.csv (DEXINUS) | MIRROR | 1973-01 | 2026-09 |
| eia_brent_spot.csv (RBRTE) | MIRROR | 1987-05 | 2026-09 |
| yahoo_gold_fut.csv (GC=F) | FAILED |  |  |
| yahoo_silver_fut.csv (SI=F) | FAILED |  |  |
| yahoo_brent_fut.csv (BZ=F) | FAILED |  |  |
| yahoo_nifty.csv (^NSEI) | FAILED |  |  |
| nifty_monthly.csv (NIFTY 50 (NSE)) | MIRROR | 1990-07 | 2026-09 |
| nsdl_fpi_equity_monthly.csv (NSDL FPI monthly) | FAILED |  |  |
| nsdl_fpi_equity_monthly.csv (NSDL FPI monthly, equity net (INR cr)) | MIRROR | 2005-01 | 2026-03 |
| fred_DFII10 (no mirror).csv (DFII10) | NOTE |  |  |

## 2. The rules (one line each)

- **Layer 1, trend.** Vote +1 when the 12-month return and the 12-month return minus the 1-month return are both positive, -1 when both are negative, 0 when they disagree. Layer 1 alone is the baseline.
- **Layer 2, regime.** Growth is rising when the 3-month change of copper/gold is above its own trailing 12-month average; inflation is rising when the 3-month change of the 10-year breakeven (T10YIE) is above its trailing 12-month average. The asset votes the table entry for the quadrant.
- **Layer 3, driver.** Gold and silver: minus the sign of the 3-month change in the 10-year real yield. Aluminium and zinc: sign of (minus sign of the 3-month dollar change, plus sign of the 3-month copper/gold change). Nifty: sign of (sign of last month's net FPI equity flow, minus sign of the 3-month Brent change). Brent: none.
- **Combine.** Score = L1 + L2 + L3. Call = sign of score. Confidence LOW / MEDIUM / HIGH = |score| 1 / 2 / 3. Score 0 = NO CALL.
- **Timing.** Pink Sheet assets are monthly AVERAGE prices: the call is made when month t is published and predicts avg(t+h) vs avg(t). Nifty uses month-end closes; monthly-published inputs enter it one month late. Nothing uses a value dated after the decision.

Regime table (+1 up, -1 down, 0 no view):

| Asset group | Reflation (G up, I up) | Goldilocks (G up, I down) | Stagflation (G down, I up) | Deflation (G down, I down) | Why |
|---|---|---|---|---|---|
| gold | +0 | -1 | +1 | +0 | gold is the hedge for inflation and for weak growth |
| metal | +1 | +1 | -1 | -1 | industrial metals are priced off factory demand |
| equity | +0 | +1 | -1 | +0 | equities want growth with falling inflation |
| crude | +1 | -1 | +1 | -1 | crude prices move with the inflation impulse |
| silver | +1 | +0 | +0 | -1 | silver is half monetary metal, half industrial metal |

Logistic comparison: L2-regularised logistic regression (scikit-learn default C=1) on the same inputs (12-month return, 12m minus 1m, copper/gold 3m, breakeven 3m, real yield level and 3m change, dollar 3m, Fed funds 6m, USD/INR 3m, Brent 3m except for Brent, FPI flow). Inputs standardised on the training window. 120-month rolling window, refit each January, training rows only where the target was already realised at the refit date. One model per asset and horizon.

## 3. Hit rates

Hit rate = share of months with a call where the call matched the sign of the forward return; (n) = months with a call. Coverage = share of months the model made any call. Noise band: with 200 calls, one standard error of a hit rate near 55% is 3.5 points, so a gap under about 7 points between two rules is not distinguishable from luck. 3-month outcomes overlap month to month, so their effective sample is about a third of n.

### 1-month horizon, full window

| Asset | Model | Coverage | LOW | MEDIUM | HIGH | Trend L1 (baseline) | 12m sign only | Always up | Model minus trend |
|---|---|---|---|---|---|---|---|---|---|
| Gold (USD) | 57.1% (226) | 83% | 57.4% (183) | 55.8% (43) | n/a | 56.7% (254) | 54.8% (272) | 55.1% (272) | +0.4 pts |
| Silver (USD) | 51.7% (209) | 77% | 51.6% (161) | 52.1% (48) | n/a | 54.3% (254) | 54.6% (269) | 51.5% (272) | -2.7 pts |
| Aluminium (USD, LME) | 56.2% (201) | 74% | 56.0% (84) | 49.2% (61) | 64.3% (56) | 54.0% (263) | 53.7% (272) | 54.0% (272) | +2.2 pts |
| Zinc (USD, LME) | 60.4% (202) | 74% | 63.1% (84) | 55.0% (60) | 62.1% (58) | 54.4% (259) | 55.1% (272) | 55.5% (272) | +6.0 pts |
| Brent (USD) | 53.1% (177) | 65% | 49.5% (95) | 57.3% (82) | n/a | 52.2% (249) | 52.8% (271) | 56.2% (272) | +0.9 pts |
| Nifty 50 (INR) | 50.5% (184) | 68% | 47.2% (106) | 53.7% (67) | 63.6% (11) | 54.7% (258) | 55.1% (272) | 58.8% (272) | -4.1 pts |
| Gold (INR) | 58.5% (234) | 86% | 58.9% (192) | 57.1% (42) | n/a | 59.1% (257) | 60.3% (272) | 61.0% (272) | -0.6 pts |
| Silver (INR) | 47.8% (209) | 77% | 48.1% (160) | 46.9% (49) | n/a | 50.6% (251) | 52.2% (272) | 55.9% (272) | -2.8 pts |

### 1-month horizon, logistic window (rules vs logistic on the same months)

| Asset | Logistic starts | Logistic | Rules | Trend L1 | Always up |
|---|---|---|---|---|---|
| Gold (USD) | 2004-01 | 49.3% (272) | 57.1% (226) | 56.7% (254) | 55.1% (272) |
| Silver (USD) | 2004-01 | 43.4% (272) | 51.7% (209) | 54.3% (254) | 51.5% (272) |
| Aluminium (USD, LME) | 2004-01 | 48.5% (272) | 56.2% (201) | 54.0% (263) | 54.0% (272) |
| Zinc (USD, LME) | 2004-01 | 55.5% (272) | 60.4% (202) | 54.4% (259) | 55.5% (272) |
| Brent (USD) | 2004-01 | 57.7% (272) | 53.1% (177) | 52.2% (249) | 56.2% (272) |
| Nifty 50 (INR) | 2004-01 | 56.6% (272) | 50.5% (184) | 54.7% (258) | 58.8% (272) |
| Gold (INR) | 2004-01 | 54.0% (272) | 58.5% (234) | 59.1% (257) | 61.0% (272) |
| Silver (INR) | 2004-01 | 47.8% (272) | 47.8% (209) | 50.6% (251) | 55.9% (272) |

### 3-month horizon, full window

| Asset | Model | Coverage | LOW | MEDIUM | HIGH | Trend L1 (baseline) | 12m sign only | Always up | Model minus trend |
|---|---|---|---|---|---|---|---|---|---|
| Gold (USD) | 59.4% (224) | 83% | 58.6% (181) | 62.8% (43) | n/a | 58.7% (252) | 57.8% (270) | 62.6% (270) | +0.6 pts |
| Silver (USD) | 53.1% (207) | 77% | 54.7% (159) | 47.9% (48) | n/a | 54.4% (252) | 54.3% (267) | 54.4% (270) | -1.2 pts |
| Aluminium (USD, LME) | 55.3% (199) | 74% | 60.7% (84) | 50.8% (59) | 51.8% (56) | 54.4% (261) | 54.4% (270) | 55.6% (270) | +0.9 pts |
| Zinc (USD, LME) | 49.0% (200) | 74% | 50.0% (84) | 50.0% (58) | 46.6% (58) | 51.4% (257) | 51.9% (270) | 58.9% (270) | -2.4 pts |
| Brent (USD) | 52.0% (175) | 65% | 43.0% (93) | 62.2% (82) | n/a | 50.6% (247) | 50.6% (269) | 57.4% (270) | +1.4 pts |
| Nifty 50 (INR) | 49.5% (184) | 68% | 45.3% (106) | 53.7% (67) | 63.6% (11) | 55.5% (256) | 55.2% (270) | 63.3% (270) | -6.0 pts |
| Gold (INR) | 65.1% (232) | 86% | 68.4% (190) | 50.0% (42) | n/a | 63.1% (255) | 61.9% (270) | 67.0% (270) | +1.9 pts |
| Silver (INR) | 47.8% (207) | 77% | 48.1% (158) | 46.9% (49) | n/a | 50.6% (249) | 50.7% (270) | 58.9% (270) | -2.8 pts |

### 3-month horizon, logistic window (rules vs logistic on the same months)

| Asset | Logistic starts | Logistic | Rules | Trend L1 | Always up |
|---|---|---|---|---|---|
| Gold (USD) | 2004-01 | 54.1% (270) | 59.4% (224) | 58.7% (252) | 62.6% (270) |
| Silver (USD) | 2004-01 | 37.8% (270) | 53.1% (207) | 54.4% (252) | 54.4% (270) |
| Aluminium (USD, LME) | 2004-01 | 53.0% (270) | 55.3% (199) | 54.4% (261) | 55.6% (270) |
| Zinc (USD, LME) | 2004-01 | 49.6% (270) | 49.0% (200) | 51.4% (257) | 58.9% (270) |
| Brent (USD) | 2004-01 | 51.9% (270) | 52.0% (175) | 50.6% (247) | 57.4% (270) |
| Nifty 50 (INR) | 2004-01 | 53.0% (270) | 49.5% (184) | 55.5% (256) | 63.3% (270) |
| Gold (INR) | 2004-01 | 59.3% (270) | 65.1% (232) | 63.1% (255) | 67.0% (270) |
| Silver (INR) | 2004-01 | 47.0% (270) | 47.8% (207) | 50.6% (249) | 58.9% (270) |

### Where all three layers could vote (breakeven data ends 2019-10)

Same tables restricted to months with a regime reading. After 2019-10 the regime layer votes 0 for every asset (input missing), so this is the only fair test of the full rule set.

| Asset (1m) | Model | LOW | MEDIUM | HIGH | Trend L1 | Always up | Logistic | Model minus trend |
|---|---|---|---|---|---|---|---|---|
| Gold (USD) | 58.1% (148) | 59.0% (105) | 55.8% (43) | n/a | 57.4% (176) | 54.3% (188) | 51.1% (188) | +0.7 pts |
| Silver (USD) | 52.3% (132) | 52.4% (84) | 52.1% (48) | n/a | 55.9% (177) | 48.9% (188) | 44.1% (188) | -3.7 pts |
| Aluminium (USD, LME) | 56.8% (148) | 58.1% (62) | 40.0% (30) | 64.3% (56) | 54.1% (183) | 50.0% (188) | 47.9% (188) | +2.7 pts |
| Zinc (USD, LME) | 60.3% (151) | 64.5% (62) | 48.4% (31) | 62.1% (58) | 55.3% (179) | 52.7% (188) | 55.3% (188) | +5.0 pts |
| Brent (USD) | 54.5% (99) | 41.2% (17) | 57.3% (82) | n/a | 52.6% (171) | 59.0% (188) | 61.2% (188) | +1.9 pts |
| Nifty 50 (INR) | 53.8% (130) | 50.7% (71) | 56.2% (48) | 63.6% (11) | 58.9% (180) | 60.1% (188) | 57.4% (188) | -5.0 pts |
| Gold (INR) | 57.0% (151) | 56.9% (109) | 57.1% (42) | n/a | 58.0% (174) | 60.1% (188) | 53.2% (188) | -1.1 pts |
| Silver (INR) | 43.5% (131) | 41.5% (82) | 46.9% (49) | n/a | 48.6% (173) | 54.3% (188) | 52.1% (188) | -5.0 pts |

| Asset (3m) | Model | LOW | MEDIUM | HIGH | Trend L1 | Always up | Logistic | Model minus trend |
|---|---|---|---|---|---|---|---|---|
| Gold (USD) | 60.1% (148) | 59.0% (105) | 62.8% (43) | n/a | 59.1% (176) | 60.6% (188) | 57.4% (188) | +1.0 pts |
| Silver (USD) | 51.5% (132) | 53.6% (84) | 47.9% (48) | n/a | 53.7% (177) | 52.1% (188) | 40.4% (188) | -2.2 pts |
| Aluminium (USD, LME) | 54.1% (148) | 62.9% (62) | 40.0% (30) | 51.8% (56) | 53.0% (183) | 53.7% (188) | 54.8% (188) | +1.0 pts |
| Zinc (USD, LME) | 45.0% (151) | 46.8% (62) | 38.7% (31) | 46.6% (58) | 49.2% (179) | 54.8% (188) | 50.5% (188) | -4.1 pts |
| Brent (USD) | 59.6% (99) | 47.1% (17) | 62.2% (82) | n/a | 54.4% (171) | 60.1% (188) | 58.5% (188) | +5.2 pts |
| Nifty 50 (INR) | 53.8% (130) | 47.9% (71) | 60.4% (48) | 63.6% (11) | 59.4% (180) | 63.8% (188) | 52.1% (188) | -5.6 pts |
| Gold (INR) | 65.6% (151) | 71.6% (109) | 50.0% (42) | n/a | 62.6% (174) | 65.4% (188) | 60.1% (188) | +2.9 pts |
| Silver (INR) | 41.2% (131) | 37.8% (82) | 46.9% (49) | n/a | 46.8% (173) | 57.4% (188) | 50.0% (188) | -5.6 pts |

Nifty with the FPI vote switched off (FPI history before 2020 is unverified, see data): 1m 47.8% (161), 3m 44.7% (161).

Calibration reads off the LOW / MEDIUM / HIGH columns: a calibrated model shows hit rate rising with confidence.

Cross-check, Pink Sheet Brent vs EIA Brent spot (monthly average): 273 months from 2004, median level gap 0.40%, max 26.78% (2020-04), monthly direction agrees in 97.1% of months. Gold and silver could not be cross-checked: Yahoo futures (GC=F, SI=F) were refused and no copy was found.

## 4. Averaging check: monthly-average vs month-end prices

Pink Sheet prices are monthly averages. Averaging a random walk creates positive autocorrelation in its monthly changes, so a trend rule looks better on averages than on prices anyone can trade. This table runs the same rules, same months, on both series where a month-end series exists.

| Asset | Months | Rules on averages | Trend on averages | Rules on month-end | Trend on month-end |
|---|---|---|---|---|---|
| brent_eia_avg | 273 | 53.1% (179) | 52.9% (244) | 52.8% (176) | 52.8% (246) |
| nifty_avg | 273 | 58.6% (186) | 59.5% (257) | 50.5% (184) | 54.7% (258) |
| gold | no month-end series fetched | | | | |
| silver | no month-end series fetched | | | | |

## 5. Strategies (monthly rebalance, 1-month returns, no costs)

Long/flat: long when the call is up, flat otherwise. Long/short: long on up, short on down, flat on NO CALL. Rule calls are the same for both horizons, so one row covers both; the logistic rows use the 1-month and the 3-month model's call for the next month. Returns on Pink Sheet assets are average-to-average and NOT tradeable as shown (see section 4).

### Gold (USD)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 10.9% | 13.4% | -39.3% | 272 |
| Rules long/flat | 8.7% | 11.4% | -20.3% | 272 |
| Rules long/short | 7.8% | 12.6% | -32.4% | 272 |
| Trend (L1) long/flat | 9.5% | 11.8% | -21.4% | 272 |
| Trend (L1) long/short | 8.4% | 13.3% | -33.3% | 272 |
| Logit 1m long/flat | 5.2% | 11.1% | -38.0% | 272 |
| Logit 1m long/short | -0.8% | 13.8% | -48.4% | 272 |
| Buy and hold (logit window) | 10.9% | 13.4% | -39.3% | 272 |
| Logit 3m long/flat | 7.9% | 12.7% | -39.7% | 272 |
| Logit 3m long/short | 4.8% | 13.7% | -40.7% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2008-03 to 2009-02 | -20.3% | -4.5% | 14% | DEFL 4, REFL 3, STAG 3, GOLD 2 |
| 2015-12 to 2016-11 | -19.0% | 7.5% | 30% | REFL 6, DEFL 3, STAG 2, GOLD 1 |
| 2022-04 to 2023-03 | -16.1% | 3.3% | 29% | no regime data (after 2019-10) |

Gold (USD). The model hits 57.1% at 1 month against 56.7% for trend: a 0.4-point gain, which is nothing. At 3 months it hits 59.4%. That is below "always up" at 62.6%. Its one real use is the drawdown cut. Long/flat lost 20% at worst against 39% for buy-and-hold. The trend rule alone does the same (21%), so the regime layer adds nothing here. The worst stretches are 2008-09, 2015-16 and 2022-23. The 2022-23 loss came while real yields rose fast. The real-yield driver exists to catch that shock, and it never voted (DFII10 missing). Re-test once DFII10 is cached. Until then the model does not beat trend.

### Silver (USD)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 10.8% | 27.2% | -67.0% | 272 |
| Rules long/flat | 8.0% | 22.2% | -36.2% | 272 |
| Rules long/short | 5.9% | 25.4% | -51.4% | 272 |
| Trend (L1) long/flat | 10.9% | 23.6% | -40.9% | 272 |
| Trend (L1) long/short | 8.7% | 26.8% | -64.3% | 272 |
| Logit 1m long/flat | 0.5% | 17.8% | -59.7% | 272 |
| Logit 1m long/short | -13.0% | 27.3% | -96.8% | 272 |
| Buy and hold (logit window) | 10.8% | 27.2% | -67.0% | 272 |
| Logit 3m long/flat | -5.0% | 15.5% | -77.7% | 272 |
| Logit 3m long/short | -22.7% | 26.8% | -99.7% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2008-03 to 2009-02 | -43.6% | -32.1% | 33% | DEFL 4, REFL 3, STAG 3, GOLD 2 |
| 2022-10 to 2023-09 | -39.9% | 15.5% | 11% | no regime data (after 2019-10) |
| 2019-05 to 2020-04 | -32.6% | 10.9% | 12% | DEFL 6 |

Silver (USD). The model hits 51.7% at 1 month against 54.3% for trend: 2.7 points WORSE. At 3 months it is 1.2 points worse. The regime layer hurts. It votes silver down in deflation readings, and silver did not follow that pattern. Long/short lost 40% in 2022-23 with an 11% hit rate. Long/flat returned 8.0% a year against 10.8% for buy-and-hold. It does not beat the trend baseline. Do not use it for silver.

### Aluminium (USD, LME)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 3.2% | 17.7% | -56.7% | 272 |
| Rules long/flat | 4.9% | 11.7% | -22.8% | 272 |
| Rules long/short | 6.2% | 15.4% | -34.0% | 272 |
| Trend (L1) long/flat | 3.2% | 13.8% | -41.6% | 272 |
| Trend (L1) long/short | 2.1% | 17.4% | -58.1% | 272 |
| Logit 1m long/flat | 1.5% | 15.2% | -56.7% | 272 |
| Logit 1m long/short | -0.9% | 17.8% | -64.0% | 272 |
| Buy and hold (logit window) | 3.2% | 17.7% | -56.7% | 272 |
| Logit 3m long/flat | 3.7% | 14.1% | -30.4% | 272 |
| Logit 3m long/short | 3.1% | 17.7% | -42.8% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2011-12 to 2012-11 | -27.4% | 3.2% | 33% | REFL 6, STAG 4, GOLD 1, DEFL 1 |
| 2007-05 to 2008-04 | -26.8% | 3.9% | 20% | REFL 4, DEFL 3, STAG 3, GOLD 2 |
| 2023-09 to 2024-08 | -23.3% | 12.1% | 20% | no regime data (after 2019-10) |

Aluminium (USD, LME). The model hits 56.2% at 1 month against 54.0% for trend (+2.2). That is inside the noise band. HIGH-confidence calls hit 64.3% on 56 months. That is the only bucket that looks like signal, but the scale is not calibrated: MEDIUM hits only 49.2%. Long/short made 6.2% a year against 3.2% for buy-and-hold, with a worst drawdown of 34% against 57%. Trend alone made 2.1% long/short, so here the regime and dollar/copper layers do add something. At 3 months the edge falls to +0.9. Worth watching HIGH calls only. Not worth trading on yet.

### Zinc (USD, LME)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 6.3% | 23.3% | -75.0% | 272 |
| Rules long/flat | 10.6% | 15.4% | -36.0% | 272 |
| Rules long/short | 12.9% | 20.2% | -41.9% | 272 |
| Trend (L1) long/flat | 8.5% | 17.8% | -39.7% | 272 |
| Trend (L1) long/short | 6.7% | 22.8% | -57.2% | 272 |
| Logit 1m long/flat | 8.7% | 18.0% | -47.1% | 272 |
| Logit 1m long/short | 8.8% | 23.2% | -52.5% | 272 |
| Buy and hold (logit window) | 6.3% | 23.3% | -75.0% | 272 |
| Logit 3m long/flat | 2.8% | 18.4% | -65.0% | 272 |
| Logit 3m long/short | -2.7% | 23.4% | -91.1% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2012-04 to 2013-03 | -24.9% | -7.3% | 33% | GOLD 4, STAG 4, REFL 3, DEFL 1 |
| 2023-06 to 2024-05 | -23.1% | 18.3% | 27% | no regime data (after 2019-10) |
| 2018-05 to 2019-04 | -21.7% | -10.4% | 44% | DEFL 6, GOLD 3, REFL 2, STAG 1 |

Zinc (USD, LME). This is the best result: 60.4% at 1 month against 54.4% for trend (+6.0). That is about 1.7 standard errors, so it is suggestive and not proven. Long/short made 12.9% a year against 6.3% for buy-and-hold, with a worst drawdown of 42% against 75%. Two facts weaken it. First, at 3 months the model hits 49.0%, below trend (51.4%) and far below "always up" (58.9%). Second, confidence is not calibrated: LOW 63%, MEDIUM 55%, HIGH 62%. It also runs on monthly averages (section 4). Treat it as a hypothesis to re-test on month-end LME prices. Do not treat it as an edge yet.

### Brent (USD)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 6.0% | 33.6% | -82.6% | 272 |
| Rules long/flat | 4.1% | 16.3% | -54.6% | 272 |
| Rules long/short | 1.1% | 28.7% | -87.8% | 272 |
| Trend (L1) long/flat | 5.1% | 21.0% | -54.6% | 272 |
| Trend (L1) long/short | -3.9% | 32.6% | -89.2% | 272 |
| Logit 1m long/flat | 14.8% | 23.7% | -43.6% | 272 |
| Logit 1m long/short | 17.5% | 33.2% | -58.2% | 272 |
| Buy and hold (logit window) | 6.0% | 33.6% | -82.6% | 272 |
| Logit 3m long/flat | 4.5% | 28.7% | -80.2% | 272 |
| Logit 3m long/short | -0.1% | 33.7% | -95.3% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2020-04 to 2021-03 | -71.5% | 178.1% | 18% | no regime data (after 2019-10) |
| 2025-07 to 2026-06 | -63.0% | 17.5% | 45% | no regime data (after 2019-10) |
| 2015-11 to 2016-10 | -25.9% | 4.5% | 20% | REFL 6, DEFL 3, STAG 2, GOLD 1 |

Brent (USD). The model hits 53.1% at 1 month against 52.2% for trend and 56.2% for "always up". It loses to the simplest rule. Long/short made 1.1% a year with an 88% drawdown. The worst stretch: it sat short through the 2020-21 rebound (-71.5% against +178% for the asset). The logistic 1-month model made 17.5% a year long/short. This is the one striking logistic result, but it is one of 16 logistic tests. Treat it as luck until a second window confirms it. On month-end EIA prices the rules score almost the same (52.8%), so averaging is not the issue for Brent. With no driver vote (v1), Brent is trend plus an inflation tag. It does not beat the baseline.

### Nifty 50 (INR)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 11.9% | 20.7% | -55.1% | 272 |
| Rules long/flat | 1.6% | 13.2% | -43.0% | 272 |
| Rules long/short | -5.4% | 17.0% | -82.6% | 272 |
| Trend (L1) long/flat | 6.7% | 16.8% | -34.2% | 272 |
| Trend (L1) long/short | 2.2% | 20.7% | -61.7% | 272 |
| Logit 1m long/flat | 8.4% | 16.9% | -49.8% | 272 |
| Logit 1m long/short | 3.3% | 21.0% | -73.1% | 272 |
| Buy and hold (logit window) | 11.9% | 20.7% | -55.1% | 272 |
| Logit 3m long/flat | 5.4% | 16.8% | -68.4% | 272 |
| Logit 3m long/short | -2.3% | 21.1% | -89.2% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2020-01 to 2020-12 | -56.8% | 14.0% | 9% | no regime data (after 2019-10) |
| 2008-05 to 2009-04 | -43.4% | -8.6% | 33% | REFL 4, DEFL 4, STAG 3, GOLD 1 |
| 2004-04 to 2005-03 | -29.2% | 5.9% | 17% | DEFL 6, STAG 3, REFL 2, GOLD 1 |

Nifty 50 (INR). This is the worst result. The model hits 50.5% at 1 month against 54.7% for trend and 58.8% for "always up". At 3 months it hits 49.5% against 55.5% and 63.3%. Long/flat returned 1.6% a year against 11.9% for buy-and-hold. The crude-shock vote and the regime vote both pull it toward DOWN calls in a market that rose in most months. In 2020 it hit 9% of its calls. With the FPI vote switched off, the hit rate falls to 47.8%, so the FPI sign is the only input that helps. For Indian equities this model is worse than doing nothing. Do not use it to time Nifty.

### Gold (INR)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 14.6% | 13.5% | -24.6% | 272 |
| Rules long/flat | 12.7% | 12.2% | -14.8% | 272 |
| Rules long/short | 10.7% | 13.1% | -34.9% | 272 |
| Trend (L1) long/flat | 13.4% | 12.5% | -19.7% | 272 |
| Trend (L1) long/short | 11.9% | 13.5% | -34.0% | 272 |
| Logit 1m long/flat | 9.0% | 11.5% | -31.5% | 272 |
| Logit 1m long/short | 3.1% | 14.1% | -46.8% | 272 |
| Buy and hold (logit window) | 14.6% | 13.5% | -24.6% | 272 |
| Logit 3m long/flat | 11.4% | 12.6% | -29.4% | 272 |
| Logit 3m long/short | 8.0% | 13.9% | -39.9% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2013-07 to 2014-06 | -19.1% | 2.5% | 12% | STAG 6, REFL 3, GOLD 2, DEFL 1 |
| 2015-04 to 2016-03 | -16.3% | 9.8% | 14% | DEFL 6, REFL 3, STAG 3 |
| 2006-05 to 2007-04 | -11.3% | -11.3% | 27% | DEFL 5, REFL 3, STAG 3, GOLD 1 |

Gold (INR). The model hits 58.5% at 1 month against 59.1% for trend and 61.0% for "always up". At 3 months it hits 65.1% against 63.1% and 67.0%. Rupee depreciation adds a steady upward drift, and no layer beats that drift. Long/flat returned 12.7% a year against 14.6% for buy-and-hold, with a worst drawdown of 15% against 25%. Its only use is the smaller drawdown, which trend alone gives almost as well (20%). It does not beat the baseline.

### Silver (INR)

| Strategy | Ann. return | Volatility | Max drawdown | Months |
|---|---|---|---|---|
| Buy and hold | 14.5% | 26.5% | -50.4% | 272 |
| Rules long/flat | 7.6% | 22.0% | -45.9% | 272 |
| Rules long/short | 2.5% | 24.9% | -61.0% | 272 |
| Trend (L1) long/flat | 10.1% | 23.3% | -40.8% | 272 |
| Trend (L1) long/short | 4.9% | 26.3% | -68.6% | 272 |
| Logit 1m long/flat | 6.0% | 18.1% | -43.0% | 272 |
| Logit 1m long/short | -5.8% | 26.9% | -89.1% | 272 |
| Buy and hold (logit window) | 14.5% | 26.5% | -50.4% | 272 |
| Logit 3m long/flat | 1.3% | 17.8% | -47.3% | 272 |
| Logit 3m long/short | -14.0% | 26.7% | -97.2% | 272 |

Worst three 12-month stretches (rules long/short, non-overlapping; decision months shown; regime mix = months per quadrant):

| Decision months | Long/short | Buy and hold | Hit rate | Regime mix |
|---|---|---|---|---|
| 2008-03 to 2009-02 | -47.9% | -13.6% | 36% | DEFL 4, REFL 3, STAG 3, GOLD 2 |
| 2022-09 to 2023-08 | -39.5% | 26.5% | 27% | no regime data (after 2019-10) |
| 2007-02 to 2008-01 | -32.6% | 14.1% | 0% | STAG 5, REFL 3, DEFL 3, GOLD 1 |

Silver (INR). The model hits 47.8% at 1 month and 47.8% at 3 months, worse than a coin toss. Trend is 50.6% and "always up" is 55.9% / 58.9%. Long/flat returned 7.6% a year against 14.5% for buy-and-hold. It fails. Do not use it.

## 6. Cross-asset: top-2 of 6 by score

Assets: gold, silver, aluminium, zinc, brent, nifty. Each month, hold the two highest scores in equal weight (ties broken by 12-month momentum rank); compare with equal weight in all six. Months 2004-01 to 2026-08 (272). Mixed currency (Nifty in INR, the rest USD) and Pink Sheet average returns: read as a ranking test, not a tradeable portfolio.

| Portfolio | Ann. return | Volatility | Max drawdown |
|---|---|---|---|
| Top-2 by score | 12.5% | 17.7% | -45.1% |
| Top-2, only scores > 0 (else cash) | 12.0% | 15.8% | -29.9% |
| Top-2 by trend L1 alone (baseline ranking) | 11.2% | 20.9% | -45.7% |
| Bottom-2 by score (sanity check) | 7.6% | 18.5% | -51.2% |
| Equal weight, all six | 10.0% | 14.7% | -44.4% |

Top-2 beat equal weight in 53% of months. Times each asset was picked: gold 129, nifty 112, zinc 94, brent 84, aluminium 65, silver 60.

The top-2 portfolio returned 12.5% a year against 10.0% for equal weight. Volatility was higher (17.7% against 14.7%). The drawdown was about the same (45% against 44%). Per unit of risk the two are level. Top-2 beat equal weight in 53% of months. The ranking carries some information: bottom-2 returned 7.6%, a spread of about 5 points a year. But ranking by trend alone returned 11.2%, so the extra layers add about 1.3 points a year. That gain is inside the noise for 272 months of mixed, average-priced returns. The most usable variant holds the top two only when their score is above zero, and cash otherwise. It returned 12.0% with a 30% worst drawdown. That gain is drawdown control, not forecasting.

## 7. What this backtest cannot tell you

- **Data provenance.** Every series came from a public GitHub copy, because this shell could not reach FRED, Yahoo, the World Bank or NSDL. The copies match the stated upstream where checked: Pink Sheet Brent against EIA, and the two NSE Nifty files against each other (0.000% gap over 3,087 days). Gold and silver were not cross-checked. Re-run `python fetch.py --primary` on the operator laptop, then `python backtest.py`.
- **Missing inputs.** The model was not tested as designed. DFII10 is missing, T10YIE ends 2019-10, DTWEXBGS ends 2025-12, and FPI before 2020 is unverified. The gold/silver driver and the 2020-2026 regime layer are untested.
- **Monthly averages.** Pink Sheet returns are average-to-average. They cannot be traded, and section 4 shows they can flatter a trend rule. The strategy rows for commodities are a ranking test, not a P&L.
- **Hindsight in the rules.** The regime table was written by people who know how 2008, 2020 and 2022 played out. No walk-forward procedure removes that.
- **Multiple tests.** 8 series, 2 horizons, 3 confidence buckets and 2 models give over 60 hit rates. A few will look good by chance. The zinc and Brent-logistic results are the ones most likely to be such accidents.
- **No costs, no slippage, no currency hedging.** None of these is modelled.
