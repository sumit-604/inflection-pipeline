# No money measure leads small caps

Window: Feb 2023 to Oct 2026, 45 monthly returns. Data built 2026-11-17.
Chart: out/liquidity_smallcap.png. Table: out/lag_table.md. Gaps: data/gaps.md.

## The answer

None of the three money measures leads the Nifty Smallcap 250 by one, two
or three months. Every lead correlation is under 0.20. With 45 months, a
correlation needs to pass about 0.30 to stand clear of chance.

| Measure (monthly change) | Lag 0 | Lag 1 | Lag 2 | Lag 3 |
|---|---|---|---|---|
| Net LAF, monthly mean | +0.25 | -0.01 | +0.11 | -0.09 |
| 3M CD rate, monthly mean | **-0.43** | -0.08 | -0.07 | +0.23 |
| MTF book, NSE + BSE | **+0.64** | -0.12 | -0.17 | 0.00 |

Bold = passes the 0.30 bar. Lag k: money change in month t, Smallcap 250
return in month t+k.

The best "lead" on paper is net LAF at two months, r +0.11. That is noise.

## What does move with small caps

**The 3-month CD rate moves in the same month, in the opposite direction.**
When the rate rises, small caps fall that month (r -0.43). This held in
every rolling 12-month window, from -0.12 to -0.78. It is the steadiest
link in the data. It tells you the regime you are in, not what comes next.

**The MTF book follows small caps; it does not lead them.** It moves with
them in the same month (r +0.64). Small-cap returns also predict the MTF
change one and two months later (r +0.44, +0.31). The MTF book is a rupee
value of funded positions, so prices push it up. Traders then add loans
after a rise. Read it as a crowding gauge, not a signal.

**Net LAF sets the average, not the timing.** In the 15 deficit months,
the Smallcap 250 averaged +0.56% a month (median -0.65%). In the 30
surplus months it averaged +1.98% (median +1.44%). The month-to-month
link is weak (r +0.25, below the bar).

## Where the link worked

- **Dec 2024 to Feb 2025.** Net LAF swung from surplus to a Rs 2.1 lakh
  crore deficit in January. The CD rate rose from 7.2% to 7.5%. The
  Smallcap 250 fell 10.7% in January and 12.7% in February.
- **Apr to Jun 2025.** Liquidity returned to a surplus of Rs 1.4 to 2.8
  lakh crore. The CD rate fell to 5.9%. Small caps gained 1.7%, 9.6% and
  5.7%.

## Where the link failed

- **Nov 2023 to Jan 2024.** The deficit deepened from Rs 0.7 to Rs 2.0
  lakh crore, and the CD rate climbed from 7.3% to 7.5%. Small caps rose
  10.2%, 6.0% and 7.3%. Earnings momentum and retail flows beat tight
  money.
- **Jun 2024.** Net LAF was in deficit. Small caps rose 9.5% after the
  election result.
- **Jul to Aug 2025.** Surplus near Rs 3 lakh crore and the lowest CD rate
  in the window, 5.8%. Small caps fell 3.7% in each month.
- **Jan to Mar 2026.** Net LAF stayed in surplus. Small caps fell 5.5% in
  January and 10.0% in March. The CD rate did warn here: it rose from 6.0%
  to 7.3%.
- **Sep to Oct 2026.** Record surplus, a September mean of Rs 7.5 lakh
  crore. Small caps fell 3.1% and 5.8%.

The pattern in the failures: surplus cash is necessary for a good small-cap
year, but not sufficient. A deficit hurt when it came with a valuation
shock (early 2025). It did not hurt when earnings and flows were strong
(late 2023).

## How to use this

- Do not time small-cap entries off net LAF, the CD rate or the MTF book.
  None gives a one-to-three-month warning in this window.
- Use the 3M CD rate as a same-month regime check. A rising rate and
  falling small caps together have been the consistent pairing.
- Use the MTF book to judge crowding after a rally, not to forecast one.

## Limits

- 45 monthly points over one cycle of tightening and easing. One more
  cycle could change these numbers.
- Correlation only. The test does not control for earnings, FPI flows or
  valuation.
- MTF: indiamtf's API note says BSE data starts around 2025-10-15. Its own
  file has daily BSE values from 2017-07-03, with no jump in 2025. The test
  uses NSE + BSE throughout; NSE alone gives the same result (+0.65 at lag 0).
- Three checks were added after the first run and are labelled so: reverse
  lags, a lag-0 rolling window, and returns by LAF regime.
