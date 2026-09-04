# CLEANMAX — ROLE 1 VALUATION: SOTP FCFF (Option A)

**Company:** Clean Max Enviro Energy Solutions Ltd
**Ticker:** CLEANMAX (NSE) / 544717 (BSE)
**CMP:** Rs 1,247
**Valuation date:** 30-Jun-2026, rolled to 02-Sep-2026. Every schedule states its date.
**Method:** Sum-of-the-parts free cash flow to firm (SOTP FCFF), four buckets, four discount rates.
**Framework exception:** Option A, operator-signed 2026-09-02. **SOTP FCFF is the PRIMARY method.** EV/EBITDA and P/E are an END cross-check, weighted at most 15%, never primary. P/E is not applicable (B04). This overrides the signed model Part E ordering, where SOTP was tertiary; the operator's Role 1 spec makes SOTP FCFF primary.
**Units:** Rs Crore throughout. Source figures in Rs million are divided by 10.
**Fill rule:** NOT FOUND is the only fill for a missing number. No estimate substitutes for a disclosed figure.
**Tags:** [FILED] audited/exchange-filed; [MGMT] management-stated; [SECONDARY] third-party; [INFERENCE] my derivation; [spec] operator-supplied input this container cannot verify live.

> **Headline.** Base-case equity value (Bikaner Case A, Rajasthan 50%) is **Rs 178 per share on the AR net-debt basis, Rs 267 on the management net-debt basis**, against CMP Rs 1,247. Bikaner Case B lifts these to Rs 267 / Rs 357; the discount-rate and Rajasthan-siting sensitivity spans Rs -6 to Rs 405. The operational fleet alone (Bucket 1) is worth an EV of **Rs 16,239 Cr** against a current market EV of **Rs 25,889 Cr**. The market pays **Rs 9,650 Cr** above the operating fleet for growth that the SOTP values at roughly zero. All three sanity gates pass.

---

## LIVE-WEB LIMITATION (read first)

This container has no live web. Four spec inputs are "verify current" and are used as supplied, tagged, and flagged for Claude web to confirm:

| Input | Value used | Tag |
|---|---|---|
| India 10-year G-sec (Rf) | 6.5% | [spec — VERIFY LIVE] |
| Damodaran India ERP | 7.5% | [spec — VERIFY LIVE] |
| Unlevered beta, contracted power | 0.55 | [spec — VERIFY LIVE] |
| Peer FY28 multiples ACME / Adani Green | 13.1x / 14.2x | [spec — VERIFY LIVE] |

The Damodaran valuation handbook named in the spec is NOT in the repo. I apply the SOTP division-cost-of-capital method from the spec description: a separate discount rate per bucket, built from that bucket's risk, not one blended WACC.

---

## 1. COST OF CAPITAL (every step)

Group-level CAPM and WACC first, then the four bucket rates derived from it.

**Risk-free and equity risk premium.** Rf 6.5% [spec]. India ERP 7.5% [spec]. Unlevered beta 0.55 [spec].

**Leverage at market.** Net debt on the AR basis Rs 11,208.80 Cr [FILED, AR Note 37.1, twin p.431 line 26920: "Net Debt (A) 1,12,088.04" Rs mn]. Add debt-like acceptances Rs 1,730.92 Cr [FILED, Note 26B]. Debt for gearing = 12,939.72. Market cap Rs 14,680 Cr [spec; 11.75 Cr shares x Rs 1,247 = 14,652, spec rounds 14,680]. **D/E at market = 12,939.72 / 14,680 = 0.881.**

**Levered beta** (Hamada, 25% tax): 0.55 x [1 + (1 - 0.25) x 0.881] = **0.914**.

**Cost of equity:** 6.5% + 0.914 x 7.5% = **13.35%**.

**Cost of debt:** pre-tax 8.4% [MGMT, Aug-2026 call line 124: "8.4% is where we stand as of June 2026"]; post-tax at 25% = **6.30%**.

**Weights:** E = 14,680 / 27,620 = 53.2%; D = 46.8%.

**Group WACC = 0.532 x 13.35% + 0.468 x 6.30% = 10.05%.** [INFERENCE, per spec build]

### Bucket discount rates (derived, not asserted)

| Bucket | Rate | Build |
|---|---|---|
| 1 Operational fleet | **8.0%** | Project structure 75% debt @6.30% post-tax + 25% equity @~13% (contracted investment-grade stream): 0.75 x 6.30% + 0.25 x 13% = 7.98% -> 8.0%. [INFERENCE] |
| 2 Under-execution | **11.0%** | Bucket 1 8.0% + ~300 bps for execution, commissioning and connectivity risk (51% of the book is CTU). [INFERENCE] |
| 3 Pipeline / platform | **14.0%** | Evacuation-applied, not firm; equity-like risk on unbuilt, unfunded intent. [INFERENCE] |
| 4 RE Services | **12.0%** | Asset-light order-book run-off; book-to-bill below 1. [INFERENCE] |

The whole model runs at these rates AND at +/-150 bps on each (Section 4 sensitivity grid).

---

## 2. THE FOUR BUCKETS

### BUCKET 1 — OPERATIONAL FLEET

**Asset base:** 4,174.43 MW C&I operational at 30-Jun-2026 [FILED, Pres p.26/twin line 630: solar onsite 535.74 MWp, solar offsite 2,795.84 MWp, wind 842.85 MW].

**Generation, realised not theoretical.** Theoretical output from P90/P75 PLFs is ~7,600 GWh [spec]. Disclosed Q1 FY27 exported generation is 1,302.36 Mn kWh [FILED, Pres p.27/twin line 629], which annualises to **5,209 GWh**. The ~31% gap is Bikaner curtailment (525 MW CTU, ~70% curtailed [MGMT, Aug call]), post-COD ramp, and seasonality. I use the realised figure. Using theoretical here would double-count the curtailment I model as a Bikaner case.

**Year-1 build:**
- Generation 5,209 GWh; realised tariff Rs 4.06/kWh [FILED, Pres p.27/twin line 671].
- Revenue = 5,209 x 4.06 / 10 = **Rs 2,115 Cr**.
- EBITDA margin 83.5% [FILED, Note 55, RE Power Sales 83-84%]. **EBITDA Rs 1,766 Cr.**
- **Maintenance capex Rs 3 lakh/MW/yr** = Rs 125 Cr/yr. [INFERENCE, assumption stated] Basis: routine O&M capex (module cleaning, inverter reserve, spares), ~0.65% of estimated gross block. This is maintenance only; the initial build is sunk and already sits in EV. Not omitted.
- **Cash tax low initially.** DTA Rs 1,215.77 Cr on unabsorbed depreciation [FILED, Notes 24/48/49]. I model the shield running off: 0% cash tax years 1-4, 12.5% years 5-8, 25% thereafter. The DTA is modeled HERE, not added as a separate asset (per spec).

**Life and tail.** Weighted PPA tenor remaining 23.17 years [FILED, AR p.16-17]. Years 1-23 at the PPA tariff; years 24-30 (the 30-year asset life after the useful-life extension, Note 2(vii)) at a re-contracted **merchant tariff Rs 2.50/kWh** [INFERENCE], discounted at the same 8%. Deep discounting makes the tail small.

**Tariff escalation:** most C&I PPAs are flat or lightly escalating. Escalation is NOT DISCLOSED per contract. **Run flat (0%).** [INFERENCE, flagged]

**Degradation:** 0.4%/yr blended [INFERENCE; standard solar module degradation ~0.5%/yr applied across the solar-weighted fleet].

**BIKANER — run both, not blended:**
- **Case A (base):** 70% curtailment persists for the full life [MGMT, Aug guidance]. This is already embedded in the realised generation.
- **Case B:** Bikaner resolves in FY28, adding ~Rs 170 Cr/yr EBITDA from year 2 [MGMT/spec].

**Cash-flow schedule (Case A, Rs Cr, selected years):**

| Year | Generation GWh | Tariff | Revenue | EBITDA | Cash tax | FCFF |
|---|---|---|---|---|---|---|
| 1 | 5,209 | 4.06 | 2,115 | 1,766 | 0 | 1,641 |
| 2 | 5,189 | 4.06 | 2,107 | 1,759 | 0 | 1,634 |
| 5 | 5,127 | 4.06 | 2,081 | 1,738 | 137 | 1,476 |
| 9 | 5,045 | 4.06 | 2,048 | 1,710 | 267 | 1,319 |
| 23 | 4,770 | 4.06 | 1,937 | 1,617 | 243 | 1,249 |
| 24 | 4,751 | 2.50 | 1,188 | 992 | 87 | 780 |
| 30 | 4,638 | 2.50 | 1,159 | 968 | 81 | 762 |

**Bucket 1 EV, discounted at 8.0%:**
- **Case A: Rs 16,239 Cr.**
- **Case B: Rs 17,767 Cr.**

---

### BUCKET 2 — UNDER-EXECUTION

**Book:** 2,656.66 MW contracted yet to execute [FILED, Pres p.26/twin line 635]. Method per spec: value the completed asset on Bucket-1 economics at the contracted Rs 4.00/kWh [FILED, Pres p.35], then SUBTRACT the PV of remaining capex.

**Completed-asset economics.** Clean per-MW generation 1.35 GWh/MW/yr [INFERENCE, fleet realised ex-Bikaner drag], tariff Rs 4.00, margin 83.5%. Full-book EBITDA at completion ~Rs 1,198 Cr/yr (Rajasthan 0% case). Same 30-year life, degradation, tax schedule and maintenance capex as Bucket 1.

**Remaining capex.** Total book cost = (solar 0.70 x 2,656.66 x Rs 3.5 Cr/MWp + wind 0.30 x 2,656.66 x Rs 7.8 Cr/MW) x 1.06 soft cost = **Rs 13,489 Cr** [FILED unit costs, Pres p.11/twin line 276; 70/30 split Pres note 2]. Less CWIP already spent Rs 5,339.21 Cr (closing, AR Note 3) = **remaining capex Rs 8,150 Cr.** The Rs 5,339 already spent is sunk and funded by the net debt I subtract later; only the remaining Rs 8,150 is a future outflow.

**CWIP movement and capitalisation-rate reconciliation** [FILED, AR Note 3, blocking input now resolved]. FY26 CWIP: opening 1,912.54 + additions 7,142.28 - transfer to PPE 3,720.54 + FX 4.93 = **closing 5,339.21**; average 3,625.87. FY25 average 1,295.00. Interest capitalised FY26 185.51 (FY25 33.42); other attributable capitalised costs (LC/BG, employee, insurance, legal, overheads) FY26 242.81. Capitalisation rate on average CWIP 3,625.87: **interest-only 5.1%; interest + LC/BG (~126.76) ~8.6%; cost of debt 8.4%.** On interest alone the capitalisation is conservative; adding LC/BG charges puts it at or just above the cost of debt, i.e. MARGINAL, matching the signed model §B3 restatement. This is a capitalisation-quality flag, not a valuation input; the DCF uses the closing CWIP 5,339.21 as sunk cost only.

**Commissioning profile.** >=1.5 GW in FY27, 4.6 GW by 1-Apr-2027 [MGMT]. I model a two-year profile: half the book's cash flows start ~year 1.5, half ~year 2.5, after the post-COD ramp (revenue 3-6 months, financial 9-12 months [MGMT, May call]). Remaining capex is spent across years 0.5 and 1.5.

**Connectivity / Rajasthan-siting risk (probability-weighted, not blanket).** Koppal ~543 MW carries a low haircut (Koppal-Gadag scheme ~end-Sep-2026, ahead of the October first-bay; southern curtailment limited) [MGMT/SECONDARY]. The residual ~800 MW is unnamed. I run it at **0% / 50% / 100% Rajasthan siting**; a Rajasthan-sited MW carries Bikaner economics (70% curtailment, output 30%).

**Bucket 2 value (Rs Cr):**

| Rajasthan siting of residual 800 MW | Completed-asset PV | Less PV remaining capex | Net value |
|---|---|---|---|
| 0% | 7,659 | (7,352) | **+307** |
| 50% (base) | 6,835 | (7,352) | **(517)** |
| 100% | 6,010 | (7,352) | **(1,342)** |

**The under-execution book is roughly value-neutral to value-destructive.** After the money already sunk, the PV of the completed assets barely covers the cost to finish them. Building assets that earn a ~5% unlevered return does not clear an 11% execution-risk hurdle. This is the same finding the FTTCP reached: growth below the cost of capital.

---

### BUCKET 3 — PIPELINE / PLATFORM

**Book:** 2,668 MW evacuation-applied, not firm [FILED, Pres p.35], plus stated intent ~1.5 GW/yr.

**Base case: ZERO.** Post-tax ROIC is 3.4% today and ~5.4% at guided FY28, against a WACC of ~10% [signed model 0.2; spec]. Reinvestment below the cost of capital destroys value; unbuilt, unfunded intent has no claim to positive value.

**Downside: NEGATIVE.** Reinvest ~Rs 6,750 Cr/yr at a -4.6 pp spread destroys ~Rs 310 Cr/yr. PV of five years at WACC 10.05% = **-Rs 1,176 Cr.**

**Upside: NONE.** If ROIC reaches the guided 10% by FY30, ROIC equals WACC and the value is zero, not positive. **There is no upside case in which this growth creates value at the guided return.** This is the direct test of the ~Rs 10,200 Cr of EV the market pays above the operational fleet.

---

### BUCKET 4 — RE SERVICES

**FY26 revenue Rs 497.33 Cr, ~19.6% margin** [FILED, Q4]. Order book fell 215 -> 147 MW while Q1 FY27 revenue rose 7.3x: book-to-bill below 1 [MGMT]. PoC revenue is a Key Audit Matter. I do NOT extrapolate the Q1 spike.

Value on a 3-year run-off plus a low exit multiple. Year-1 EBITDA Rs 97.5 Cr, declining 20%/yr (78.0, 62.4); FCFF = EBITDA x (1 - 25% tax), asset-light; exit at 3x year-3 post-tax EBITDA. Discount at 12.0%.

**Bucket 4 EV = Rs 245 Cr.**

---

## 3. EV -> EQUITY -> PER-SHARE BRIDGE (every deduction itemised)

**Gross EV (base: Case A, Rajasthan 50%):** 16,239 + (517) + 0 + 245 = **Rs 15,966 Cr.**

**Deductions:**

| Item | Value Rs Cr | Basis |
|---|---|---|
| Gross EV (sum of buckets) | 15,966 | Sections above |
| Less net debt | (11,208.80) *AR basis* | [FILED, Note 37.1]. Run alternate 9,684 [MGMT] |
| Less acceptances / reverse factoring | (1,730.92) | [FILED, Note 26B]. Debt-like: it finances working capital and must be repaid; ADD to net debt per spec |
| = Equity value, 100% consolidated | 3,027 | |
| Less NCI at FAIR VALUE | (378) | See below. NOT the book 885.27 |
| = Equity attributable to parent | 2,649 | |
| Less complexity discount 12.5% | (331) | See Section 5 |
| = After complexity | 2,318 | |
| x Survival probability 90% | (232) | See Section 5 |
| **= FINAL EQUITY VALUE** | **2,086** | |
| **Per share (11.75 Cr shares)** | **Rs 178** | |

**NCI at fair value, not book.** Book NCI is Rs 885.27 Cr [FILED, Note 20B] and the recognised put liability is Rs 19.20 Cr [FILED, Note 22]. The put is struck at FAIR MARKET VALUE [FILED, Note 38(ii)], so the economic NCI is the co-owners' 26% of the fair value of the SPVs they hold, not the book figure. Method: 26% x (co-owned share of levered equity). Co-owned fraction = the group-captive share, ~48% of the operational book (STU Group Captive 1,995 MW of 4,174) [FILED, Pres connectivity table twin line 847]. Onsite (13%), third-party open access, Bucket 3 and Bucket 4 are parent-100% and carry no NCI. **NCI FMV Rs 378 Cr** at 48% co-owned; the recognised put Rs 19.20 Cr is subsumed, not added again. This is material and no prior stage sized it. Sensitivity on the co-owned fraction:

| Co-owned fraction | NCI FMV Rs Cr | Final equity Rs Cr | Per share |
|---|---|---|---|
| 35% | 275 | 2,167 | Rs 184 |
| 48% (base) | 378 | 2,086 | Rs 178 |
| 60% | 472 | 2,012 | Rs 171 |

**DTA Rs 1,215.77 Cr is NOT added as an asset.** Its shield is modeled inside Bucket 1 cash tax (per spec; avoids double-counting).

**Net-debt basis and Bikaner case (base range, Rajasthan 50%):**

| Case | Net debt | Gross EV | Final equity Rs Cr | Per share |
|---|---|---|---|---|
| Bikaner A, net debt AR 11,208.80 | 11,208.80 | 15,966 | 2,086 | **Rs 178** |
| Bikaner A, net debt mgmt 9,684 | 9,684 | 15,966 | 3,137 | **Rs 267** |
| Bikaner B, net debt AR 11,208.80 | 11,208.80 | 17,495 | 3,139 | **Rs 267** |
| Bikaner B, net debt mgmt 9,684 | 9,684 | 17,495 | 4,190 | **Rs 357** |

The net-debt gap Rs 1,524.80 Cr, with no corpus bridge [Open Item 1], moves the answer by ~Rs 90/share because it lands entirely on a thin equity slice. At 30-Jun-2026 net debt was already Rs 11,809 Cr [MGMT, Aug call], above the AR figure; using that would lower each row by a further ~Rs 50/share.

---

## 4. SENSITIVITY GRID (discount rate +/-150 bps x Rajasthan probability)

Per share, net-debt AR basis, Bikaner Case A, base complexity and survival. Each column is a separate Rajasthan-siting case (not blended).

| Discount shift | Rajasthan 0% | Rajasthan 50% | Rajasthan 100% |
|---|---|---|---|
| **-150 bps** | Rs 405 | Rs 351 | Rs 296 |
| **base rates** | Rs 226 | **Rs 178** | Rs 129 |
| **+150 bps** | Rs 81 | Rs 38 | Rs (6) |

The full base-case span is **Rs -6 to Rs 405**. Equity is hypersensitive because ~Rs 13,000 Cr of net debt plus acceptances sits above a thin equity residual: a 150 bps rate move or a full-Rajasthan siting swings per-share value by more than 100%. Every cell is far below CMP Rs 1,247.

---

## 5. BIKANER CASE A vs B (side by side, not blended)

Net-debt AR, Rajasthan 50%.

| | Bucket 1 EV | Gross EV | Final equity Rs Cr | Per share |
|---|---|---|---|---|
| **Case A** — 70% curtailment persists full life (base, Aug guidance) | 16,239 | 15,966 | 2,086 | **Rs 178** |
| **Case B** — resolves FY28, +Rs 170 Cr/yr EBITDA thereafter | 17,767 | 17,495 | 3,139 | **Rs 267** |

Bikaner resolution is worth ~Rs 89/share. It does not close the gap to CMP.

---

## 6. BUCKET 3 SCENARIOS (zero / negative / no-upside)

| Scenario | Value Rs Cr | Logic |
|---|---|---|
| **Base** | **0** | ROIC 3.4-5.4% below WACC 10%; unfunded intent has no positive claim |
| **Downside** | **(1,176)** | Reinvest ~6,750/yr at -4.6 pp spread = -310/yr; PV five years at 10.05% |
| **Upside** | **0 (no positive case)** | At the guided 10% ROIC by FY30, ROIC = WACC, value = 0. No growth rate at the guided return creates value |

---

## 7. THE KEY COMPARISON (Bucket 1 standalone vs current EV)

| | Rs Cr |
|---|---|
| Bucket 1 operational fleet, standalone EV (Case A) | 16,239 |
| Current market EV | 25,889 [spec] |
| **Market pays above the operating fleet** | **9,650** |
| SOTP value of Buckets 2 + 3 + 4 (Raj 50%) | (272) |
| Share of the Rs 9,650 growth premium the SOTP justifies | **~0%** |

The market pays Rs 9,650 Cr for the growth engine (under-execution + pipeline + services). The SOTP values that same engine at roughly zero, and negative in several cells. **The entire premium over the operating fleet is unsupported by discounted cash flow at the guided returns.** Buckets 2 and 3 do not justify it: the under-execution book barely covers its remaining capex, and the pipeline earns below its cost of capital. Even on the friendliest bucket assumptions (Bikaner B, mgmt net debt, Rajasthan 0%, -150 bps), gross EV reaches ~Rs 19,300 Cr, still Rs 6,600 Cr below the market EV.

---

## 8. ENTRY PRICE AND MARGIN OF SAFETY

Base fair value Rs 178/share (Case A, net debt AR, Raj 50%). For a 25% CAGR over three years, exiting at fair value: entry = FV / 1.25^3 = FV / 1.953.

| | Per share |
|---|---|
| Base-case fair value | Rs 178 |
| **Entry for 25% 3-year CAGR** | **Rs 91** |
| **With 20% margin of safety** | **Rs 73** |
| CMP | Rs 1,247 |
| Implied 3-year CAGR buying at CMP to base FV | **-48%/yr** |

Even on the friendlier base (Bikaner B or mgmt net debt, Rs 267/share), the 25%-CAGR entry is ~Rs 137 and the MoS price ~Rs 109. Both sit **below** the signed model's provisional entry zone of Rs 470-715. The Role 1 SOTP FCFF is a materially more bearish tool than the EV/EBITDA-anchored provisional zone, because it discounts the actual sub-WACC returns rather than applying a peer multiple. This divergence is a finding for the operator, not an error: the provisional zone was set on EV/EBITDA; this primary method is DCF.

---

## 9. MULTIPLES CROSS-CHECK (end only, <=15% weight)

Not an anchor. Run last, weighted at most 15%, to confirm the SOTP EV is not wildly off.

| Multiple x run-rate EBITDA 1,870 | Implied EV Rs Cr |
|---|---|
| 8x | 14,960 |
| 9x (cross-check point) | 16,830 |
| 13.1x (ACME FY28) [spec — VERIFY] | 24,497 |
| 14.2x (Adani Green FY28) [spec — VERIFY] | 26,554 |

At 9x run-rate EBITDA the cross-check EV is Rs 16,830 Cr, within 5% of the SOTP gross EV Rs 15,966 Cr. **The two methods agree on the EV.** An 85/15 SOTP/multiples blend gives Rs 185/share, one rupee-band off the SOTP. The peer FY28 multiples (13-14x) imply an EV of ~Rs 24,500-26,600 Cr, close to the current market EV: the market is applying peer multiples to run-rate EBITDA, i.e. pricing the FY28 state today. The disagreement is not on EV method; it is that the equity is thin and geared, so a defensible EV leaves little equity.

---

## 10. SANITY GATES (each checked before writing)

| Gate | Test | Result |
|---|---|---|
| **G1** | Bucket 1 EV broadly consistent with run-rate EBITDA 1,870 scaled to the June fleet at a mid-single-digit multiple | Run-rate scaled to June fleet = 1,870 x 4,174.43 / 3,088 = Rs 2,527 Cr. Bucket 1 EV 16,239 / 2,527 = **6.4x. PASS** (mid-single-digit). Against curtailment-dragged realised EBITDA 1,766 it is 9.2x; the intended run-rate basis is 6.4x. No arithmetic error. |
| **G2** | Sum of bucket year-1 revenues reconciles to annualised Q1 FY27 revenue ~Rs 3,329 Cr | Bucket 1 (power) 2,115 + Bucket 4 (services, Q1 303.9 x 4) 1,216 = **Rs 3,331 Cr** vs 3,329. **PASS** (Q1 FY27 total revenue 832.16 x 4 = 3,329). |
| **G3** | Equity + net debt + acceptances + NCI = gross EV less nothing unaccounted | Attributable equity (pre-adjustment) 2,649 + net debt 11,208.80 + acceptances 1,730.92 + NCI 378 = **15,966** = gross EV. **PASS.** |

All three gates pass. No error found or fixed; G1's realised-EBITDA reading (9.2x) is reconciled to the run-rate basis the gate intends (6.4x).

---

## 11. WHAT WAS NOT DONE (per spec)

- No EV/EBITDA as the primary method (capex is 15x depreciation; the multiple misreads a fleet mid-build). Used only as the <=15% end cross-check.
- No P/E (trailing ~94x, forward ~29x; neither describes a young-fleet IPP). Ruled not applicable by B04.
- No growing perpetuity (finite contracts on 30-year assets; a literal perpetuity at 5.4% return / 10% WACC / 4% g gives EV ~0.23x invested capital and negative equity, the wrong tool).
- No peer multiples as an anchor (ACME 13.1x, Adani 14.2x are FY28 cross-checks at the end only).
- The Bikaner cases, the Rajasthan probabilities, and the two net-debt figures are reported separately, never blended.

---

## 12. ASSUMPTION REGISTER (every assumption tagged)

| # | Assumption | Value | Tag |
|---|---|---|---|
| 1 | Rf / ERP / unlevered beta | 6.5% / 7.5% / 0.55 | [spec — VERIFY LIVE] |
| 2 | Cost of debt pre-tax | 8.4% | [MGMT, Aug call] |
| 3 | Bucket rates 1/2/3/4 | 8 / 11 / 14 / 12% | [INFERENCE, derived Section 1] |
| 4 | Asset base operational | 4,174.43 MW | [FILED, Pres p.26] |
| 5 | Year-1 generation (realised, annualised Q1) | 5,209 GWh | [FILED, Pres p.27] |
| 6 | Realised tariff / under-execution tariff / merchant tail | 4.06 / 4.00 / 2.50 Rs/kWh | [FILED / FILED / INFERENCE] |
| 7 | RE Power Sales EBITDA margin | 83.5% | [FILED, Note 55] |
| 8 | Maintenance capex | Rs 3 lakh/MW/yr | [INFERENCE] |
| 9 | Cash-tax schedule (DTA shield runoff) | 0% y1-4, 12.5% y5-8, 25% y9+ | [INFERENCE; DTA 1,215.77 FILED] |
| 10 | PPA tenor remaining / asset life | 23.17 / 30 yr | [FILED] |
| 11 | Tariff escalation | 0% (flat) | [INFERENCE, NOT DISCLOSED per contract] |
| 12 | Degradation | 0.4%/yr | [INFERENCE] |
| 13 | Bikaner Case A / B | 70% persists / resolves FY28 +170 Cr | [MGMT] |
| 14 | Under-execution unit costs | solar 3.5, wind 7.8 Cr/MW, +6% soft | [FILED, Pres p.11] |
| 15 | CWIP already spent (closing) | 5,339.21 | [FILED, AR Note 3] |
| 16 | Clean per-MW generation (Bucket 2) | 1.35 GWh/MW/yr | [INFERENCE] |
| 17 | Rajasthan siting of residual 800 MW | 0 / 50 / 100% | [INFERENCE, scenario] |
| 18 | Bucket 3 base / downside | 0 / -1,176 | [INFERENCE] |
| 19 | Services run-off / exit | -20%/yr, 3x exit | [INFERENCE] |
| 20 | Net debt AR / mgmt / acceptances | 11,208.80 / 9,684 / 1,730.92 | [FILED / MGMT / FILED] |
| 21 | NCI FMV co-owned fraction | 48% (35-60% range) | [INFERENCE; group-captive share FILED] |
| 22 | Complexity discount | 12.5% | [INFERENCE, Section 5 scoring] |
| 23 | Survival probability | 90% | [INFERENCE, Section 5 scoring] |
| 24 | Shares outstanding | 11.75 Cr | [spec] |

### Complexity discount, scored (Damodaran opacity framework) [INFERENCE]

Information-cost and consolidation-opacity discount. Contributing facts, each [FILED] or [MGMT]: 190+ subsidiaries; 103 CARO entities, 93 in two-year cash losses; 859-page AR; five distinct EBITDA definitions in the corpus; unreconciled Rs 1,524.80 Cr net-debt gap; other income 58.8% one-off or non-cash; 17 cash pools disclosed for 9 uses. Damodaran opacity discounts for hard-to-monitor consolidated structures run 5-20%. I set **12.5%**: the structure is opaque and the net-debt gap is unbridged, but the accounts are audited, conservative on capitalisation (interest-only basis) and tested clean in the FTTCP. Defensible midpoint.

### Survival probability, scored [INFERENCE]

Distress-tail scaling. Contributing facts: ND/EBITDA ~5.3x guided against the CARE 5.5x downgrade trigger; current liabilities exceed current assets by Rs 1,724.10 Cr with going-concern language; one FY26 facility covenant breached and rectified (facility unidentified); promoter personal guarantees on six SPV facilities plus 51% parent-equity pledges; SPV debt not ring-fenced. Against these: A+/AA rating, 99.35% uptime, 25-35 day receivables, cost of debt falling, board and marquee investors (Temasek, Bain at Rs 1,053). I set survival **90%** (10% distress probability over the hold), scaling equity value down 10%. A harder 85% would cut per-share value a further ~Rs 12.

---

## APPENDIX — DISCOUNTED SCHEDULES SOURCE

All DCF arithmetic computed in Python (`outputs/valuation/role1-sotp-model.py`), not by hand. The script builds each bucket's year-by-year FCFF, discounts at the bucket rate, runs the +/-150 bps and Rajasthan grids, the Bikaner cases, the two net-debt bases, the NCI-fraction sensitivity, the entry price, the multiples cross-check, and the three sanity gates. Numbers in this report are its outputs.

---

*Role 1 SOTP FCFF, Option A (SOTP primary, multiples <=15% cross-check). Valuation date 30-Jun-2026 rolled to 02-Sep-2026. Every number carries its source; NOT FOUND is the only fill; provisional inputs marked [spec — VERIFY LIVE] or [INFERENCE]. Two inputs remain open and material: the Rs 1,524.80 Cr net-debt gap (Open Item 1) and the consolidated CWIP opening/closing series (Open Item 10, now resolved for FY26 via the blocking input; the capitalisation-quality note stands). This valuation does not resolve them; it reports each basis separately.*
