# Verdict and reading, macro regime model v2, 2026-10-05

Numbers below are from EVALUATION_2026-10.md, run on the data in commit
284324b with the rules in commit 0ca0acc. The bar is PASS_BAR.md, written
before the run.

## The verdict

The bands fail the bar. Condition (a) asked that the gold band and the Nifty
band point the right way in 10 of 14 episodes. Gold scored 7.5, Nifty 5.5.
Condition (b) passed: the OVERWEIGHT bucket beat the UNDERWEIGHT bucket at
12 months on 4 of 6 assets. Condition (c) failed: the 12-month trend sign
scored the two judging assets better (16 against 13).

By the bar, latest.md shows the dials and the regime and no exposure
bands. That is what run.py now does.

## What the tables say, beyond the verdict

The bar judged on gold and Nifty. Those are the two assets where the
textbook regime table is wrong at this horizon. On the four commodities
the same table works.

**Industrial metals.** The growth dial does its job. Aluminium OVERWEIGHT
months returned a median +10.5% over 12 months; UNDERWEIGHT months -4.7%.
Zinc: +14.5% against -2.4%. Each scored 10 of 14 episodes. The trend sign
scored 6 of 14 and had a spread near zero. For aluminium and zinc the
regime read beats trend by a wide margin and is the only one of the six
where the bands as written would have earned their place.

**Gold.** Gold rose in every regime in this sample. Its best 12-month
returns came in DEFLATION months (+18.2%) and in TIGHT liquidity months
(+12.7%), which is the opposite of the base table (DEFLATION 0,
TIGHT -1). The reason is the sample: 2004 to 2026 is one long gold bull
market with three drawdowns, and the macro dials catch the drawdowns
late. The 12-month trend sign scored 10 of 14. For gold, trend is the
better read.

**Nifty.** Nifty rose in every regime too (12-month medians +7.6% to
+15.4%). The base table marked STAGFLATION -1 and the India stress shade
-1. Both are right for one month and wrong for twelve: HIGH stress months
were followed by the best 12-month Nifty returns in the sample (+30.3%
median, 32 months), and HIGH India stress by +74% in 2009 and +48% in
2020. The band logic sold stress; the market paid for buying it.

**Stress is a buy signal at this horizon.** This is the finding that most
surprised. HIGH stress months were followed by the best 12-month returns
for silver, aluminium, zinc, Brent and Nifty, and roughly average for
gold. The STRESS shade in the band table has the sign right for a trader
and wrong for a 6 to 12 month allocator. The dial itself is sound; the
use of it was not.

**Liquidity.** EASING months were followed by the best 12-month returns
for every asset but gold. NEUTRAL was the worst bucket for the metals, not
TIGHT, because tightening happens in booms. Liquidity as a dial is
informative; as a one-step shade it is too blunt.

**Lead time.** Before June 2008 the liquidity dial read TIGHT from July
2007 and the stress dial HIGH from December 2007: six months of warning.
Before February 2020 neither dial moved; the shock was not macro. Before
March 2022 the liquidity dial crossed TIGHT in the episode month itself,
with no lead.

## What this means for the tool

The dashboard is worth keeping. The regime quadrant, the liquidity tag and
the stress tag each sort the following 12 months in a way the tables show,
and the inputs are now all primary and current to 2026-09.

The bands are not worth keeping as written. A second version would have
to change three things, and each is a new bar, not a tuning of this one:
treat HIGH stress as a reason to add, not cut; drop the regime table for
gold and Nifty and use the 12-month trend sign for those two; keep the
regime table for the four commodities. That is a different model and it
gets its own PASS_BAR before anyone runs it.

## Unknowns

- The India CPI, M3 and CLI series end in 2025-03, 2023-09 and 2024-01.
  The India stress dial ran on five of six inputs in the last 18 months.
- Aluminium and zinc are monthly averages, which flatter any rule. Their
  bucket spreads (+15 and +17 points) are large enough to survive the
  haircut the v1 check measured (about 5 points) but the month-end test
  has not been run.
- The regime table was written knowing how 2008, 2020 and 2022 played
  out. The metals edge is concentrated there: in 2004 to 2007 zinc's
  UNDERWEIGHT months did better than its OVERWEIGHT months (+36% against
  +23%), and in 2010 to 2019 the aluminium and zinc spreads are one to two
  points. The regime read earns its keep in the two big cycles and is
  silent in between. That is consistent with what a regime read is for,
  and it is also what a table written with hindsight would show.
- India stress read HIGH in April to June 2026, after the March 2026 FPI
  outflow of Rs 1.18 lakh crore. The 21 HIGH months in the sample were
  followed by a median 12-month Nifty return of +46%, nearly all of it
  from 2008 to 2009 and 2020. Two cycles, not a law.
- 14 episodes is 14 episodes.
