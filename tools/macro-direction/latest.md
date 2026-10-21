## CROSS-ASSET DIRECTION (September 2026 data, call for October 2026)

Generated 2026-10-04 by tools/macro-direction/run.py. Direction only, not price. Rule model v1; backtest in tools/macro-direction/BACKTEST_2026-10.md.

**Regime:** NOT AVAILABLE (input missing)

| Input | Value | Reading |
|---|---|---|
| Copper/gold 3m change | +4.6% | vs its 12m average +4.4%: growth RISING |
| 10y breakeven 3m change | NOT FOUND (series ends 2019-10) pts | vs its 12m average NOT FOUND pts: inflation NOT AVAILABLE |
| 10y real yield (level, 3m change) | NOT FOUND%, NOT FOUND pts (not fetched) | gold/silver driver |
| Broad dollar 3m change | NOT FOUND (series ends 2025-12) | metals driver |
| Fed funds 6m change | NOT FOUND pts (series ends 2026-07) | context only |
| USD/INR 3m change | +1.2% | context only |
| Brent 3m change | +61.7% | Nifty driver |
| Net FPI equity flow (month) | NOT FOUND (series ends 2026-03) | Nifty driver |

| Asset | Call | Confidence | L1 trend | L2 regime | L3 driver | Reason |
|---|---|---|---|---|---|---|
| Gold (USD) | UP | LOW | +1 | +0 | +0 | trend up; regime n/a neutral for it; real yield NOT FOUND pts 3m |
| Silver (USD) | UP | LOW | +1 | +0 | +0 | trend up; regime n/a neutral for it; real yield NOT FOUND pts 3m |
| Aluminium (USD, LME) | UP | MEDIUM | +1 | +0 | +1 | trend up; regime n/a neutral for it; dollar NOT FOUND 3m, Cu/Au +4.6% 3m |
| Zinc (USD, LME) | UP | MEDIUM | +1 | +0 | +1 | trend up; regime n/a neutral for it; dollar NOT FOUND 3m, Cu/Au +4.6% 3m |
| Brent (USD) | UP | LOW | +1 | +0 | +0 | trend up; regime n/a neutral for it; no driver vote (v1) |
| Nifty 50 (INR) | DOWN | MEDIUM | -1 | +0 | -1 | trend down; regime n/a neutral for it; FPI NOT FOUND, Brent +61.7% 3m |
| Gold (INR) | UP | LOW | +1 | +0 | +0 | trend up; regime n/a neutral for it; real yield NOT FOUND pts 3m |
| Silver (INR) | UP | LOW | +1 | +0 | +0 | trend up; regime n/a neutral for it; real yield NOT FOUND pts 3m |

**What would flip each call next month**

- **Gold (USD)** (2026-09): score +1; a 1-point move toward zero gives NO CALL, 2 points flips it. L1 leaves +1 if next month's month-average price is below 4,058.0 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL +0, GOLD -1, REFL +0, STAG +1); L3 flips if the 10y real yield ends next month on the other side of NOT FOUND%.
- **Silver (USD)** (2026-09): score +1; a 1-point move toward zero gives NO CALL, 2 points flips it. L1 leaves +1 if next month's month-average price is below 49.4 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL -1, GOLD +0, REFL +1, STAG +0); L3 flips if the 10y real yield ends next month on the other side of NOT FOUND%.
- **Aluminium (USD, LME)** (2026-09): score +2; a 2-point move toward zero gives NO CALL, 3 points flips it. L1 leaves +1 if next month's month-average price is below 2,793.0 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL -1, GOLD +1, REFL +1, STAG -1); L3 moves if the dollar or the Cu/Au 3m change reverses.
- **Zinc (USD, LME)** (2026-09): score +2; a 2-point move toward zero gives NO CALL, 3 points flips it. L1 leaves +1 if next month's month-average price is below 3,152.0 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL -1, GOLD +1, REFL +1, STAG -1); L3 moves if the dollar or the Cu/Au 3m change reverses.
- **Brent (USD)** (2026-09): score +1; a 1-point move toward zero gives NO CALL, 2 points flips it. L1 leaves +1 if next month's month-average price is below 64.7 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL -1, GOLD -1, REFL +1, STAG +1).
- **Nifty 50 (INR)** (2026-09): score -2; a 2-point move toward zero gives NO CALL, 3 points flips it. L1 leaves -1 if next month's month-end close is above 25,722.1 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL +0, GOLD +1, REFL +0, STAG -1); L3 moves on the sign of next month's FPI flow or a reversal in the Brent 3m change.
- **Gold (INR)** (2026-09): score +1; a 1-point move toward zero gives NO CALL, 2 points flips it. L1 leaves +1 if next month's month-average price is below 358,601.8 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL +0, GOLD -1, REFL +0, STAG +1); L3 flips if the 10y real yield ends next month on the other side of NOT FOUND%.
- **Silver (INR)** (2026-09): score +1; a 1-point move toward zero gives NO CALL, 2 points flips it. L1 leaves +1 if next month's month-average price is below 4,365.4 (or the 12m-minus-1m sign turns); L2 votes 0 until the breakeven series is refreshed (then: DEFL -1, GOLD +0, REFL +1, STAG +0); L3 flips if the 10y real yield ends next month on the other side of NOT FOUND%.
