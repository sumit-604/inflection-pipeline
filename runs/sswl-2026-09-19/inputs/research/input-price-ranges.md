# SSWL input-price ranges for the Amendment 17.4 entry check

Run: `runs/sswl-2026-09-19`. Prepared by Claude Code on 05-Oct-2026 with live web.
Purpose: input-cycle position for the Section 1B v3.7 Amendment 17.4 entry
conjunction ("Input in the TOP QUINTILE of its 5-year range → ceiling verdict
WATCHLIST"; `frameworks/Section_1B_v3_7_Amendments.md`, line 19).

Position = (spot − low) ÷ (high − low). TOP QUINTILE = position of 80% or more.
Window: 5 years ending on the latest date each series is published.
Daily data used for the LME and FX rows is saved beside this file in
`input-price-ranges-data.csv`, so every figure can be re-checked.

## Summary table

| # | Input | 5-yr high | 5-yr low | Latest spot | Position | TOP QUINTILE |
|---|---|---|---|---|---|---|
| 1 | LME aluminium cash, USD/t | 3,984.50 (07-Mar-2022) | 2,068.50 (21-Aug-2023) | 3,109.50 (02-Oct-2026) | 54.3% | **NO** |
| 2a | LME aluminium, INR/t, converted on the three dates only (method as specified) | 3,06,503 (07-Mar-2022; FBIL 76.9239) | 1,71,923 (21-Aug-2023; FBIL 83.1146) | 2,98,176 (LME 02-Oct-2026 × FBIL 25-Sep-2026, 95.8918) | 93.8% | **YES** (see warning) |
| 2b | LME aluminium, INR/t, true daily series (LME × FBIL, same date) | 3,66,881 (02-Jun-2026; 3,855.00 × 95.1702) | 1,70,353 (28-Sep-2022; 2,080.00 × 81.9005) | 3,12,032 (25-Sep-2026; 3,254.00 × 95.8918) | 72.1% | **NO** |
| 3 | Indian HRC, INR/t, BigMint (ex-SteelMint) Mumbai, IS2062 E250, 2.5-8 mm | 76,025 (Apr-2022, **monthly average**) | **NOT FOUND** on this series. Lowest sourced print: 47,000 (31-Oct-2025) | 64,100 (01-Oct-2026) | 58.9% (on the bounds; see sensitivity) | **NO** |
| 4 | Indian HRC, USD/t (same conversion rule) | 998 (Apr-2022 avg ÷ Apr-2022 avg FBIL 76.1678) | NOT FOUND. Bound: 530 (47,000 ÷ FBIL 31-Oct-2025, 88.7241) | 668 (64,100 ÷ FBIL 25-Sep-2026, 95.8918) | 29.6% | **NO** |

## Warning on row 2: the specified method gives the wrong answer here

The task asked for the INR series to be built by converting the three USD
points at the reference rate on each date. That method assumes the INR high
and low fall on the same dates as the USD high and low. They do not. The rupee
fell from ₹76.92 (07-Mar-2022) to ₹95.89 (25-Sep-2026), a 25% move, so:

- The INR high is 02-Jun-2026 (₹3,66,881/t), not 07-Mar-2022 (₹3,06,503/t).
- The INR low is 28-Sep-2022 (₹1,70,353/t), close to but not on 21-Aug-2023.

On the specified method aluminium reads 93.8%, TOP QUINTILE YES. On the true
daily INR series it reads 72.1%, NO. If the 02-Oct-2026 LME print is used with
the 25-Sep-2026 rate instead of the same-date pair, it reads 65.0%, also NO.

Amendment 17.4 names no currency. That choice is an operator ruling. Two
readings:

- **INR basis (the more evidenced reading).** SSWL buys aluminium in India,
  priced off LME in rupees, and passes it through to OEMs in rupees on a
  roughly monthly settlement (B04, B06 in this run). The cost the business
  carries is the INR cost. On this basis: 72.1%, NO.
- **USD basis.** It isolates the commodity cycle from the currency. On this
  basis: 54.3%, NO.

Both correct readings say NO. Only the three-date shortcut says YES.

## Row-by-row sources

### 1. LME aluminium cash settlement, USD/t

- Source: Westmetall republication of the LME official cash settlement, daily
  tables by year. The LME's own historical data is behind its data licence.
  - 2022: https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Al_cash&year=2022
    (row "07. March 2022", cash 3,984.50)
  - 2023: https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Al_cash&year=2023
    (row "21. August 2023", cash 2,068.50)
  - 2026: https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Al_cash
    (row "02. October 2026", cash 3,109.50; latest row on the page)
- Published: one row per LME settlement date; retrieved 05-Oct-2026.
- Window: 03-Oct-2021 to 02-Oct-2026, 1,263 settlement days.
- Context: the 2026 high so far is 3,855.00 on 02-Jun-2026, below the 2022 peak.
- Note: the 07-Mar-2022 figure is the cash settlement. The intraday 3-month
  peak that day was higher; it is not the series asked for.

### 2. USD/INR reference rate

- RBI stopped publishing the USD/INR reference rate in July 2018. FBIL
  (Financial Benchmarks India Pvt Ltd) has published it since. These are the
  FBIL figures, the official successor to the RBI reference rate.
- Source: FBIL's own data service,
  `https://www.fbil.org.in/wasdm/refrates/fetchfiltered?fromDate=YYYY-MM-DD&toDate=YYYY-MM-DD&authenticated=false`
  - 07-Mar-2022: ₹76.9239 (published 07-Mar-2022, 13:30 IST)
  - 21-Aug-2023: ₹83.1146 (published 21-Aug-2023, 13:30 IST)
  - 25-Sep-2026: ₹95.8918 (published 25-Sep-2026, 13:00 IST)
  - 02-Jun-2026: ₹95.1702; 28-Sep-2022: ₹81.9005; 31-Oct-2025: ₹88.7241
  - April 2022 average: ₹76.1678 (18 published days)
- **Gap:** FBIL returns no rate after 25-Sep-2026. 02-Oct-2026 is a Mumbai
  holiday (Gandhi Jayanti), but 28-Sep to 01-Oct-2026 should carry rates and
  the service returns none. The latest published rate (25-Sep-2026) is used
  for every October spot conversion. Where it would be found: fbil.org.in
  once the service updates, or the RBI Weekly Statistical Supplement.

### 3. Indian HRC, INR/t

- Series: BigMint benchmark, Mumbai HRC, IS 2062 Grade E250 BR, 2.5-8 mm/CTL,
  ex-Mumbai. BigMint is the renamed SteelMint, so the 2022 and 2026 figures
  come from the same publisher's Mumbai HRC series. BigMint's daily report
  states its HRC prices are basic, "GST @ 18% extra".
- **Spot: ₹64,100/t, assessed 01-Oct-2026.** BigMint, "Weekly round-up: Steel
  and raw material prices surge on tight supply, higher input costs",
  published 03-Oct-2026 14:20 IST:
  https://www.bigmint.co/insights/detail/weekly-round-up-steel-and-raw-material-prices-surge-on-tight-supply-higher-input-costs-795511
  Prior print ₹63,900/t on 29-Sep-2026 (published 30-Sep-2026):
  https://www.bigmint.co/insights/detail/india-hrc-crc-prices-edge-higher-amid-improving-market-sentiment-794313
- **High: ₹76,025/t, April 2022, a MONTHLY AVERAGE.** SteelMint data, quoted
  in Business Standard, "Major Indian steelmakers say prices have bottomed
  out", published 29-Jun-2023:
  https://www.business-standard.com/industry/news/major-indian-steelmakers-say-prices-have-bottomed-out-shows-data-123062900469_1.html
  Corroboration: SteelMint, "India: SteelMint HRC index, WPI show strong
  correlation", published 04-May-2023, "over INR 75,000/t around April 2022":
  https://www.linkedin.com/pulse/india-steelmint-hrc-index-wpi-show-strong-correlation-steelmint
  The single-day peak is NOT FOUND. It is at least the monthly average.
  The source does not state the GST basis of the ₹76,025 figure.
- **Low: NOT FOUND on this series.** The full BigMint history is behind a
  subscription (https://www.bigmint.co/prices/ferrous/steel/hrc).
  - Lowest BigMint print sourced: ₹47,000/t ex-Mumbai on 31-Oct-2025, BigMint
    Daily Steel Report issue 1575, 01-Nov-2025, p.5 (3-month change −3,200, so
    the series was still falling):
    https://cetapps.in/webportal/u_pnl/alerts/BigMint_Daily_Report_as_on_01_Nov_2025.pdf
  - Other publishers place December 2025 lower. They are different series and
    are not used in the calculation:
    - SteelOrbis, ex-Mumbai ₹45,700/t, up ₹200 (so ₹45,500 before), published
      22-Dec-2025:
      https://www.steelorbis.com/steel-prices/steel-prices-market-analyses/flats-and-slab/local-indian-hrc-prices-up-slightly-on-mills-base-price-hikes-but-moderate-bookings-seen-at-discounts-1425780.htm
    - Argus, December 2025 average ₹45,775/t as of 12-Dec (search-result
      snippet; page not opened, publication date not verified):
      https://www.argusmedia.com/en/news-and-insights/latest-market-news/2769606-oversupply-rains-drag-indian-hrc-prices-lower-in-2025
- **Sensitivity (why the verdict holds without the true low).**
  - On the sourced bounds (high 76,025, low 47,000): 58.9%.
  - With a low of 45,500, the level other publishers reached: 60.9%.
  - A lower true low raises the position, but to reach 80% the low would have
    to be ₹16,400/t. No source places Mumbai HRC anywhere near that.
  - A true single-day high above 76,025 lowers the position.
  - Verdict: NO, under every plausible value of the missing figures.

### 4. Indian HRC, USD/t

- Converted with the same FBIL rates: high ÷ April-2022 average rate (because
  the high is a monthly average), low ÷ the 31-Oct-2025 rate, spot ÷ the latest
  published rate (25-Sep-2026).
- Result: high ~$998/t, low bound ~$530/t, spot ~$668/t, position 29.6%. With
  the ₹45,500 December print as the low (~$508/t): 32.7%.
- Same caveat as row 2: USD extremes of the HRC series may fall on other
  dates. The daily HRC series is paywalled, so the true USD range cannot be
  built. The verdict is NO with a wide margin either way.

## What this means for 17.4

- Aluminium (alloy wheels, knuckles): NO on the INR daily series and on USD.
  The three-date shortcut alone reads YES.
- HRC (steel wheels): NO in INR and in USD.
- Two points for the operator before 17.4 is applied:
  1. Rule the currency basis (INR recommended; it is the cost SSWL carries).
  2. Rule which input is "the named input". Steel wheels are about 63% of
     revenue and alloy about 36%. The amendment names one input, but SSWL
     converts two.

## Gaps

- HRC 5-year low on the BigMint series: NOT FOUND (subscription).
- HRC single-day 5-year high: NOT FOUND (only the April-2022 monthly average
  is public).
- FBIL USD/INR for 28-Sep to 02-Oct-2026: NOT FOUND (service returns nothing
  after 25-Sep-2026).
