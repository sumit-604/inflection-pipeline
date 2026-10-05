# Pass bar, macro regime model v2

Written 2026-10-05 and committed before evaluate.py first ran on the data
in commit 284324b. It is fixed. The evaluation is judged against it; the
rules are not tuned to the evaluation.

## Why episodes, not hit rates

From 2004-01 to 2026-09 there are about 44 non-overlapping 6-month periods
and 22 non-overlapping 12-month periods. No hit-rate table on that sample
distinguishes skill from luck. Hit rates and bucket medians are reported,
but the test that decides is whether the regime read, as of the month-end
before each large move, pointed the right way, and how early the stress
and liquidity dials moved.

## Episodes (regime read as of this month-end; forward 6m and 12m returns)

2007-06, 2008-06, 2009-03, 2011-04, 2013-05, 2014-06, 2016-02, 2018-09,
2020-02, 2020-04, 2021-06, 2022-03, 2022-10, 2024-09, plus the latest month
(not scored).

## Conditions

(a) In at least 10 of the 14 episodes, the band for gold AND the band for
    Nifty, as of that month-end, point the same way as the asset's
    subsequent 12-month return. OVERWEIGHT points up, UNDERWEIGHT points
    down, NEUTRAL counts as a half for either direction.

(b) Across all months 2004-01 to the last month with a 12-month forward
    return, the OVERWEIGHT bucket's median 12-month return beats the
    UNDERWEIGHT bucket's for at least 4 of the 6 assets.

(c) A trend-only read (OVERWEIGHT if the 12-month return is positive,
    UNDERWEIGHT otherwise) does not satisfy (a) and (b) equally well: it
    scores fewer episodes in (a), or fewer assets in (b), or both.

Lead time: for 2008-06, 2020-02 and 2022-03, state the first month in the
preceding 12 in which STRESS crossed HIGH or LIQUIDITY crossed TIGHT.

## Consequences

Miss (a) or (b): the tool is a dashboard. latest.md shows the dials and the
regime; no exposure bands.

Miss only (c): keep the dashboard and drop the bands; say that the 12-month
trend sign is enough.

Pass all three: keep the bands; latest.md becomes a monthly section in
macro-sheet.md.

## What the bar does not test

Anything about next month. Transaction costs. Currency hedging. The
aluminium and zinc series are monthly averages, not month-end prices.
