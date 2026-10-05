# Evaluation, macro regime model v2 (2026-10)

Judged against PASS_BAR.md, committed before this file existed (0ca0acc). Data: data/sources.md. Rules: `python -c "import model; print(*model.rules(), sep=chr(10))"`.

## 1. Episodes

Regime read as of the month-end, bands, and what each asset did over the next 6 and 12 months (%). Trend = 12-month sign at the same date, the baseline for condition (c).

| Month | Regime | Liq | Stress | IN | gold band / 6m / 12m / trend | silver band / 6m / 12m / trend | aluminium band / 6m / 12m / trend | zinc band / 6m / 12m / trend | brent band / 6m / 12m / trend | nifty band / 6m / 12m / trend |
|---|---|---|---|---|---|---|---|---|---|---|
| 2007-06 | REFLATION | NEUTRAL | LOW | NORMAL | NE / +29 / +43 / up | OV / +20 / +41 / up | OV / -11 / +10 / up | OV / -35 / -47 / up | OV / +30 / +92 / dn | NE / +42 / -6 / up |
| 2008-06 | STAGFLATION | NEUTRAL | HIGH | HIGH | OV / -5 / +0 / up | UN / -35 / -22 / up | UN / -50 / -47 / up | UN / -42 / -18 / dn | NE / -74 / -51 / up | UN / -27 / +6 / dn |
| 2009-03 | DEFLATION | EASING | HIGH | HIGH | OV / +9 / +21 / up | UN / +28 / +35 / dn | UN / +37 / +65 / dn | UN / +55 / +87 / dn | UN / +43 / +74 / dn | UN / +68 / +74 / dn |
| 2011-04 | REFLATION | NEUTRAL | NORMAL | NORMAL | NE / +11 / +7 / up | OV / -29 / -36 / up | OV / -19 / -23 / up | OV / -21 / -15 / dn | OV / -14 / -6 / up | NE / -7 / -9 / up |
| 2013-05 | GOLDILOCKS | NEUTRAL | LOW | NORMAL | UN / -10 / -11 / dn | NE / -10 / -16 / dn | OV / -5 / -4 / dn | OV / +2 / +12 / dn | UN / +11 / +9 / dn | OV / +3 / +21 / up |
| 2014-06 | STAGFLATION | NEUTRAL | LOW | LOW | OV / -10 / -11 / up | NE / -26 / -26 / up | UN / +4 / -8 / up | UN / +2 / -2 / up | OV / -50 / -46 / up | UN / +9 / +10 / up |
| 2016-02 | DEFLATION | TIGHT | NORMAL | NORMAL | UN / +6 / +2 / up | UN / +25 / +24 / dn | UN / +7 / +22 / dn | UN / +33 / +66 / dn | UN / +33 / +49 / dn | UN / +26 / +27 / dn |
| 2018-09 | DEFLATION | TIGHT | NORMAL | NORMAL | UN / +9 / +23 / dn | UN / +3 / +16 / dn | UN / -8 / -13 / dn | UN / +17 / -4 / dn | UN / -18 / -26 / up | UN / +6 / +5 / up |
| 2020-02 | REFLATION | EASING | NORMAL | NORMAL | OV / +27 / +11 / up | OV / +74 / +61 / up | OV / +3 / +23 / dn | OV / +14 / +30 / dn | OV / -12 / +28 / dn | OV / +2 / +30 / up |
| 2020-04 | GOLDILOCKS | EASING | HIGH | HIGH | OV / +12 / +5 / up | NE / +59 / +74 / dn | OV / +24 / +59 / dn | OV / +28 / +49 / dn | UN / +101 / +274 / dn | NE / +18 / +48 / dn |
| 2021-06 | REFLATION | EASING | LOW | NORMAL | OV / +3 / +2 / dn | OV / -11 / -22 / up | OV / +10 / +5 / up | OV / +15 / +23 / up | OV / +0 / +56 / up | OV / +10 / +0 / up |
| 2022-03 | STAGFLATION | TIGHT | NORMAL | NORMAL | NE / -14 / +1 / up | UN / -25 / -4 / up | UN / -36 / -34 / up | UN / -21 / -25 / up | OV / -17 / -26 / up | UN / -2 / -1 / up |
| 2022-10 | DEFLATION | TIGHT | NORMAL | NORMAL | UN / +22 / +22 / dn | UN / +31 / +19 / dn | UN / +4 / -3 / dn | UN / -7 / -17 / dn | UN / -13 / -7 / up | UN / +0 / +6 / up |
| 2024-09 | GOLDILOCKS | NEUTRAL | LOW | NORMAL | UN / +17 / +46 / up | NE / +11 / +48 / up | OV / +8 / +8 / up | OV / +2 / +3 / up | UN / +7 / -5 / dn | OV / -9 / -5 / up |
| 2026-09 | REFLATION | EASING | LOW | NORMAL | OV /  /  / up | OV /  /  / up | OV /  /  / up | OV /  /  / up | OV /  /  / up | OV /  /  / dn |

OV = OVERWEIGHT, NE = NEUTRAL, UN = UNDERWEIGHT. The last row is the current read and is not scored.

### Condition (a): gold and Nifty bands vs the next 12 months

| | Gold agrees | Nifty agrees | Both needed: 10 of 14 |
|---|---|---|---|
| Model bands | 7.5 / 14 | 5.5 / 14 | FAIL |
| Trend (12m sign) | 10.0 / 14 | 6.0 / 14 | FAIL |

All six assets, same scoring:

| Asset | Model agrees / 14 | Trend agrees / 14 |
|---|---|---|
| gold | 7.5 | 10.0 |
| silver | 6.0 | 4.0 |
| aluminium | 10.0 | 6.0 |
| zinc | 10.0 | 6.0 |
| brent | 6.5 | 2.0 |
| nifty | 5.5 | 6.0 |

## 2. Buckets, all months 2004-01 onward

Median forward return by band, with the number of months in each bucket. Overlapping windows: the effective sample is about n/12 for 12-month returns.

| Asset | Horizon | OVERWEIGHT median (n) | NEUTRAL median (n) | UNDERWEIGHT median (n) | OW minus UW | Trend up median (n) | Trend down median (n) | Trend spread |
|---|---|---|---|---|---|---|---|---|
| gold | 6m | +3.5 (69) | +5.7 (93) | +6.1 (105) | -2.6 | +6.9 (195) | +2.5 (72) | +4.4 |
| gold | 12m | +7.4 (68) | +14.0 (88) | +11.4 (105) | -3.9 | +14.2 (189) | +1.9 (72) | +12.3 |
| silver | 6m | +4.9 (69) | +0.2 (72) | +4.7 (126) | +0.2 | +4.7 (163) | +2.8 (104) | +1.9 |
| silver | 12m | +7.9 (63) | -4.1 (72) | +15.6 (126) | -7.8 | +15.4 (157) | +4.7 (104) | +10.8 |
| aluminium | 6m | +8.3 (83) | +5.7 (55) | -2.7 (129) | +11.0 | +3.4 (154) | +1.5 (113) | +1.9 |
| aluminium | 12m | +10.5 (77) | +8.8 (55) | -4.7 (129) | +15.2 | +6.4 (148) | +5.1 (113) | +1.3 |
| zinc | 6m | +8.9 (83) | +2.7 (55) | -2.0 (129) | +10.8 | +2.9 (154) | +1.9 (113) | +1.0 |
| zinc | 12m | +14.5 (77) | +10.2 (55) | -2.4 (129) | +16.9 | +4.1 (148) | +7.1 (113) | -3.0 |
| brent | 6m | +1.6 (121) | +14.8 (14) | +6.3 (132) | -4.7 | +4.3 (146) | +4.9 (121) | -0.6 |
| brent | 12m | +6.2 (120) | -46.4 (14) | +1.9 (127) | +4.3 | +3.0 (145) | +2.7 (116) | +0.3 |
| nifty | 6m | +3.2 (47) | +6.6 (92) | +6.5 (128) | -3.3 | +6.0 (218) | +7.7 (49) | -1.7 |
| nifty | 12m | +14.0 (41) | +13.7 (92) | +10.9 (128) | +3.0 | +11.1 (213) | +15.7 (48) | -4.6 |

### Condition (b): OVERWEIGHT median beats UNDERWEIGHT at 12 months on 4 of 6 assets: PASS. Trend does so on 4 of 6.

### Condition (c): does the model beat the trend sign?

Episodes, gold + Nifty agreement: model 13.0, trend 16.0. Buckets, assets with positive 12m spread: model 4, trend 4. FAIL: the model does not beat the trend sign on at least one of the two counts without losing on the other.

## 3. Lead time of the stress and liquidity dials

First month in the 12 before the episode in which STRESS read HIGH or LIQUIDITY read TIGHT.

| Episode | First STRESS HIGH | First LIQUIDITY TIGHT | Read at the episode |
|---|---|---|---|
| 2008-06 | 2007-12 | 2007-07 | STAGFLATION, NEUTRAL, HIGH |
| 2020-02 | none | 2019-02 | REFLATION, EASING, NORMAL |
| 2022-03 | none | 2022-03 | STAGFLATION, TIGHT, NORMAL |

## 4. Regime history, months per quadrant and forward returns

| Quadrant | Months | gold 12m median | silver 12m median | aluminium 12m median | zinc 12m median | brent 12m median | nifty 12m median |
|---|---|---|---|---|---|---|---|
| REFLATION | 89 | +8.7 | +2.5 | +13.7 | +17.4 | +10.6 | +15.4 |
| GOLDILOCKS | 48 | +10.1 | +8.1 | +7.1 | +3.1 | +2.6 | +12.3 |
| STAGFLATION | 51 | +5.8 | -4.2 | -13.7 | -3.1 | -12.6 | +7.6 |
| DEFLATION | 85 | +18.2 | +17.4 | -1.8 | -0.4 | +1.3 | +12.7 |

By liquidity tag:

| Liquidity | Months | gold 12m median | silver 12m median | aluminium 12m median | zinc 12m median | brent 12m median | nifty 12m median |
|---|---|---|---|---|---|---|---|
| EASING | 61 | +9.3 | +18.0 | +21.3 | +23.0 | +28.4 | +15.6 |
| NEUTRAL | 97 | +6.7 | +0.3 | -4.4 | -1.1 | +1.9 | +9.9 |
| TIGHT | 115 | +12.7 | +13.2 | +7.0 | +8.6 | -0.7 | +13.2 |

By stress tag:

| Stress | Months | gold 12m median | silver 12m median | aluminium 12m median | zinc 12m median | brent 12m median | nifty 12m median |
|---|---|---|---|---|---|---|---|
| LOW | 96 | +11.0 | +13.2 | +7.6 | +10.2 | -1.3 | +21.8 |
| NORMAL | 145 | +10.7 | +5.8 | -0.6 | +0.0 | +4.1 | +8.9 |
| HIGH | 32 | +8.4 | +13.5 | +20.6 | +24.2 | +39.2 | +30.3 |

## 5. Verdict against PASS_BAR.md

- (a) episodes: FAIL (gold 7.5, Nifty 5.5; need 10 each)
- (b) buckets: PASS (4 of 6; need 4)
- (c) vs trend: FAIL

**(a) or (b) fails: the tool is a dashboard. latest.md shows dials and regime, no exposure bands.**
