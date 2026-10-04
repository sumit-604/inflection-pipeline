# Verdict paragraphs for BACKTEST_2026-10.md

report.py copies each section into the report under its asset. Numbers
quoted here come from the 2026-10-04 run. If a re-run changes the tables,
rewrite these paragraphs. Do not keep stale prose.

## HEADLINE

**Verdict: in its v1 form, the rule model does not earn the operator's attention as a forecaster.** At the 1-month horizon it beats the trend baseline by more than 2 points on two of eight series: zinc (+6.0) and aluminium (+2.2). At the 3-month horizon it clears 2 points on none of them. Gold (INR) comes closest at +1.9. It loses to trend on silver, Nifty and both INR metals. "Always up" beats the model at 3 months on all eight series. At 1 month the logistic model loses to the rules on five series, ties on one, and wins on two (Brent, Nifty). On Nifty it still trails "always up".  Keep the rules as the primary model. Neither model forecasts well.

**The data handicap is real.** Read every number with it:
- The real yield (DFII10) was never fetched, so the gold and silver driver never voted.
- The breakeven series ends in 2019-10, so the regime layer voted only from 2004 to 2019.
- The dollar series ends in 2025-12.
- FPI flows before 2020 come from a GitHub file with no stated source.

The full-rule test is therefore the 2004-2019 window, and it reads the same: zinc +5.0 and aluminium +2.7 at 1 month, Brent +5.2 at 3 months on only 99 calls, and the rest inside noise or negative. The one useful finding is in section 4. On Nifty, a trend rule scores 59.5% on monthly AVERAGE prices but only 54.7% on month-end prices. The Pink Sheet is a monthly-average series, so every commodity hit rate here may be several points better than a tradeable version would show.

## gold

Gold (USD). The model hits 57.1% at 1 month against 56.7% for trend: a 0.4-point gain, which is nothing. At 3 months it hits 59.4%. That is below "always up" at 62.6%. Its one real use is the drawdown cut. Long/flat lost 20% at worst against 39% for buy-and-hold. The trend rule alone does the same (21%), so the regime layer adds nothing here. The worst stretches are 2008-09, 2015-16 and 2022-23. The 2022-23 loss came while real yields rose fast. The real-yield driver exists to catch that shock, and it never voted (DFII10 missing). Re-test once DFII10 is cached. Until then the model does not beat trend.

## silver

Silver (USD). The model hits 51.7% at 1 month against 54.3% for trend: 2.7 points WORSE. At 3 months it is 1.2 points worse. The regime layer hurts. It votes silver down in deflation readings, and silver did not follow that pattern. Long/short lost 40% in 2022-23 with an 11% hit rate. Long/flat returned 8.0% a year against 10.8% for buy-and-hold. It does not beat the trend baseline. Do not use it for silver.

## aluminium

Aluminium (USD, LME). The model hits 56.2% at 1 month against 54.0% for trend (+2.2). That is inside the noise band. HIGH-confidence calls hit 64.3% on 56 months. That is the only bucket that looks like signal, but the scale is not calibrated: MEDIUM hits only 49.2%. Long/short made 6.2% a year against 3.2% for buy-and-hold, with a worst drawdown of 34% against 57%. Trend alone made 2.1% long/short, so here the regime and dollar/copper layers do add something. At 3 months the edge falls to +0.9. Worth watching HIGH calls only. Not worth trading on yet.

## zinc

Zinc (USD, LME). This is the best result: 60.4% at 1 month against 54.4% for trend (+6.0). That is about 1.7 standard errors, so it is suggestive and not proven. Long/short made 12.9% a year against 6.3% for buy-and-hold, with a worst drawdown of 42% against 75%. Two facts weaken it. First, at 3 months the model hits 49.0%, below trend (51.4%) and far below "always up" (58.9%). Second, confidence is not calibrated: LOW 63%, MEDIUM 55%, HIGH 62%. It also runs on monthly averages (section 4). Treat it as a hypothesis to re-test on month-end LME prices. Do not treat it as an edge yet.

## brent

Brent (USD). The model hits 53.1% at 1 month against 52.2% for trend and 56.2% for "always up". It loses to the simplest rule. Long/short made 1.1% a year with an 88% drawdown. The worst stretch: it sat short through the 2020-21 rebound (-71.5% against +178% for the asset). The logistic 1-month model made 17.5% a year long/short. This is the one striking logistic result, but it is one of 16 logistic tests. Treat it as luck until a second window confirms it. On month-end EIA prices the rules score almost the same (52.8%), so averaging is not the issue for Brent. With no driver vote (v1), Brent is trend plus an inflation tag. It does not beat the baseline.

## nifty

Nifty 50 (INR). This is the worst result. The model hits 50.5% at 1 month against 54.7% for trend and 58.8% for "always up". At 3 months it hits 49.5% against 55.5% and 63.3%. Long/flat returned 1.6% a year against 11.9% for buy-and-hold. The crude-shock vote and the regime vote both pull it toward DOWN calls in a market that rose in most months. In 2020 it hit 9% of its calls. With the FPI vote switched off, the hit rate falls to 47.8%, so the FPI sign is the only input that helps. For Indian equities this model is worse than doing nothing. Do not use it to time Nifty.

## gold_inr

Gold (INR). The model hits 58.5% at 1 month against 59.1% for trend and 61.0% for "always up". At 3 months it hits 65.1% against 63.1% and 67.0%. Rupee depreciation adds a steady upward drift, and no layer beats that drift. Long/flat returned 12.7% a year against 14.6% for buy-and-hold, with a worst drawdown of 15% against 25%. Its only use is the smaller drawdown, which trend alone gives almost as well (20%). It does not beat the baseline.

## silver_inr

Silver (INR). The model hits 47.8% at 1 month and 47.8% at 3 months, worse than a coin toss. Trend is 50.6% and "always up" is 55.9% / 58.9%. Long/flat returned 7.6% a year against 14.5% for buy-and-hold. It fails. Do not use it.

## PORTFOLIO

The top-2 portfolio returned 12.5% a year against 10.0% for equal weight. Volatility was higher (17.7% against 14.7%). The drawdown was about the same (45% against 44%). Per unit of risk the two are level. Top-2 beat equal weight in 53% of months. The ranking carries some information: bottom-2 returned 7.6%, a spread of about 5 points a year. But ranking by trend alone returned 11.2%, so the extra layers add about 1.3 points a year. That gain is inside the noise for 272 months of mixed, average-priced returns. The most usable variant holds the top two only when their score is above zero, and cash otherwise. It returned 12.0% with a 30% worst drawdown. That gain is drawdown control, not forecasting.

## LIMITS

- **Data provenance.** Every series came from a public GitHub copy, because this shell could not reach FRED, Yahoo, the World Bank or NSDL. The copies match the stated upstream where checked: Pink Sheet Brent against EIA, and the two NSE Nifty files against each other (0.000% gap over 3,087 days). Gold and silver were not cross-checked. Re-run `python fetch.py --primary` on the operator laptop, then `python backtest.py`.
- **Missing inputs.** The model was not tested as designed. DFII10 is missing, T10YIE ends 2019-10, DTWEXBGS ends 2025-12, and FPI before 2020 is unverified. The gold/silver driver and the 2020-2026 regime layer are untested.
- **Monthly averages.** Pink Sheet returns are average-to-average. They cannot be traded, and section 4 shows they can flatter a trend rule. The strategy rows for commodities are a ranking test, not a P&L.
- **Hindsight in the rules.** The regime table was written by people who know how 2008, 2020 and 2022 played out. No walk-forward procedure removes that.
- **Multiple tests.** 8 series, 2 horizons, 3 confidence buckets and 2 models give over 60 hit rates. A few will look good by chance. The zinc and Brent-logistic results are the ones most likely to be such accidents.
- **No costs, no slippage, no currency hedging.** None of these is modelled.
