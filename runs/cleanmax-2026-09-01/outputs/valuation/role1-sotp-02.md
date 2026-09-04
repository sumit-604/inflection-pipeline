# CLEANMAX — ROLE 1 VALUATION: SOTP FCFF, REVISION 02 (Option A)

**Company:** Clean Max Enviro Energy Solutions Ltd · **Ticker:** CLEANMAX (NSE) / 544717 (BSE) · **CMP:** Rs 1,247
**Valuation date:** 30-Jun-2026, rolled to 02-Sep-2026 · **Method:** SOTP FCFF, four buckets, four discount rates (Option A; multiples <=15% cross-check only).
Responds to Claude web's Role 1 Query 02 (Parts A-C). Part D extraction is at `outputs/extractions/halt1-extraction-02.md`.

## WHAT CHANGED FROM role1-sotp-01, AND WHY

1. **Entry price corrected (Part B).** The Rs 91 figure was a category error and is removed. A discounted cash flow produces a present value, not a Year-3 target, so it has no compound-return entry. Entry is now on a margin-of-safety basis.
2. **Bucket 2 shown under two treatments (Part A).** The old single figure (minus Rs 517 Cr) used one discount rate (11%) across the completed asset's whole life. That is a conservative floor. A second treatment discounts the completed operating asset at 8% (the Bucket 1 rate), holding the execution risk in the two-year commissioning delay and the remaining-capex outflow. Both are reported; neither is blended.
3. **The whole valuation is reframed as a FLOOR (Part C).** Rs 178 is the value of contracted cash flows with growth, scarcity and optionality set to zero, per the build specification. It is a floor, not a central estimate. This revision labels it as one and states what sits above it.
4. **Filed anchors from Part D fold in.** CWIP ratios settle the capitalisation question; the net-debt gap is confirmed unbridged; the filed capital commitment (Rs 831 Cr) replaces nothing but reframes the remaining-capex read; Note 51 confirms the SPV equity is structurally thin.

---

## PART A — THE BUCKET 2 ARITHMETIC (answered in full)

**A1. Buckets 2, 3 and 4, stated separately (base: Bikaner A, Rajasthan 50%, AR net debt).**

| Bucket | Value Rs Cr (floor treatment) |
|---|---|
| Bucket 2 under-execution | **(517)** |
| Bucket 3 pipeline (base) | **0** |
| Bucket 4 services | **+245** |
| Sum B2+B3+B4 | **(272)** |

The minus Rs 273 you could not reconcile is Bucket 2 alone at minus 517, plus Bucket 3 at zero, plus Bucket 4 at plus 245.

**A2. Bucket 3 was run at ZERO in the base case, not negative.** The negative Rs 1,176 Cr is a separate named downside scenario (Section 6 of role1-sotp-01), never in the base. Confirmed: base Bucket 3 = 0.

**A3. The Bucket 2 build, line by line (Rajasthan 50%, floor treatment).**

| Line | Rs Cr | Basis |
|---|---|---|
| Completed-asset EBITDA at full run (Rs 4.00/kWh, 1.35 GWh/MW, 83.5%) | 1,198/yr | Pres p.15/p.11; Note 55 |
| Completed-asset PV, discounted 11% for the whole life, delayed for commissioning (half at yr 1.5, half at yr 2.5) | **6,835** | [COMPUTED] |
| Less PV of remaining capex (spread yr 0.5 and yr 1.5 at 11%) | **(7,352)** | [COMPUTED] |
| **Net Bucket 2** | **(517)** | |

Total book cost = (0.70 x 2,656.66 x Rs 3.5 + 0.30 x 2,656.66 x Rs 7.8) x 1.06 soft = **Rs 13,489 Cr** [Pres p.11 unit costs]. Less CWIP already spent Rs 5,339.21 Cr (AR Note 3, closing) = **remaining capex Rs 8,150 Cr**. PV of that at 11% over yr 0.5-1.5 = Rs 7,352 Cr.

**A4. What drives the negative, and the finding.** Under the flat 11% treatment the completed-asset PV (Rs 6,835 Cr) is slightly below the PV of the capex to finish it (Rs 7,352 Cr). Two things pull the completed-asset PV down: the 11% discount applied across the whole 30-year life, and the two-year commissioning delay before any cash arrives. **On this conservative treatment the finding stands and is real: at an 11% execution hurdle, the under-execution book is roughly value-neutral to value-destructive on contract, not merely on reinvestment.** Building a Rs 5 return asset behind an 11% hurdle does not clear.

**But that treatment over-penalises.** Execution and connectivity risk belong to the build phase, not to the 23-year contracted operating life. Once a plant is commissioned and selling under a 23-year PPA to an AA counterparty, it is a Bucket 1 asset at 8%, not an 11% asset. The de-risked treatment discounts the completed operating cash flows at 8% and keeps the 11% only on the two-year delay and the remaining-capex spend.

**Bucket 2 under both treatments:**

| Rajasthan siting of residual 800 MW | FLOOR (11% whole life) | DE-RISKED (8% once operating) |
|---|---|---|
| 0% | +307 | **+2,549** |
| 50% (base) | **(517)** | **+1,492** |
| 100% | (1,342) | +435 |

Your own estimate of roughly plus Rs 2,900 Cr sits at the de-risked, Rajasthan 0% corner (plus 2,549). It was not wrong; it valued the completed assets at Bucket 1 economics. The truth is a range: Bucket 2 is worth **minus Rs 517 Cr on the conservative floor to plus Rs 1,492 Cr de-risked** at Rajasthan 50%. It is not a large positive, and it is not deeply negative. It is roughly the cost of building it.

**A5. Reconciliation (floor treatment).** Bucket 1 16,239 + Bucket 2 (517) + Bucket 3 0 + Bucket 4 245 = **gross EV 15,966**. Under de-risked Bucket 2: 16,239 + 1,492 + 0 + 245 = **gross EV 17,976**.

---

## PART B — THE ENTRY PRICE, CORRECTED

**You are right. The Rs 91 was a category error and is removed.** A discounted cash flow model produces a present value, the discounted value of all future cash flows as at today. Discounting a present value back three years produces a number with no meaning. Buying at fair value earns you the discount rate, roughly 10%, not 25%. To earn more you need a margin of safety against a fair value you believe is right.

**A discounted cash flow model does not produce a compound-return entry price. The 25% hurdle is expressed here as a margin of safety instead.**

| Basis | Fair value | Entry at 25% MoS | Entry at 30% MoS |
|---|---|---|---|
| FLOOR, AR net debt | Rs 178 | **Rs 133** | **Rs 124** |
| FLOOR, mgmt net debt | Rs 267 | Rs 200 | Rs 187 |
| DE-RISKED, AR net debt | Rs 295 | Rs 221 | Rs 207 |
| DE-RISKED, mgmt net debt | Rs 385 | Rs 289 | Rs 270 |

**Reconciliation of the two methods, for the record.** The EV/EBITDA track produces a Year-3 target price from a forward multiple on forward earnings, so it carries a compound-return entry (target divided by 1.25 cubed). The sum-of-the-parts produces a present value, so it carries a margin-of-safety entry. **They are not comparable as stated and must never be averaged.** The provisional zone of Rs 470-715 came from the EV/EBITDA track on forward FY29 EBITDA; the SOTP entry here is a different construction on a different, stricter base.

---

## PART C — THE THREE EXTERNAL SANITY CHECKS

**C1. Informed buyers paid Rs 1,053 seven months ago.** Jongsong (Temasek) took 2,819,548 new shares at Rs 1,053 on 6-Feb-2026 plus 4,397,926 from Brookfield at the same price; GSS India (Bain) took 2,687,559 from Brookfield at Rs 1,053 [FILED, RHP; extraction 01 Block G6]. At a floor of Rs 178 they paid roughly six times.

**Answer, defended: the buyers priced the growth, the platform and the scarcity that this model sets to zero by instruction.** The build specification asked for growth at zero, so the model deliberately does not value the 1.5 GW a year of intended build, the 555-customer platform, or the evacuation scarcity. Temasek and Bain, with full diligence, were buying the compounding machine and the platform, not a run-off of contracted cash flows. Two supporting facts keep this honest rather than a rationalisation. First, Brookfield was the seller into two of the three trades at Rs 1,053, so a sophisticated holder was also exiting at that price, which cuts both ways. Second, primary and pre-IPO transactions carry an anchor to the IPO price and a strategic-stake premium that a secondary-market minority does not. **Conclusion: the Rs 1,053 does not disprove the model; it prices what the model was told to ignore. It confirms that Rs 178 is a floor.**

**C2. The model values the enterprise below what the assets cost to build.** Invested capital = total debt 12,410.76 + total equity including NCI ~5,524 - cash 1,201.96 = **Rs 16,733 Cr** [COMPUTED; debt and cash FILED, Note 37.1/14]. Gross EV in the floor case is Rs 15,966 Cr, so **EV/IC = 0.95x**. Indian renewable assets transact at roughly 1.2 to 1.5 times invested capital, and a competitor is committing about five billion dollars to build the same asset class.

**Answer: 0.95x is a floor, not a central fair value.** No rational holder sells 4,174 MW of contracted, investment-grade-counterparty capacity below replacement cost in a market where connectivity is the binding constraint and a competitor pays up to build it. At the transaction range of 1.2-1.5x IC the enterprise is worth Rs 20,000-25,000 Cr, close to the current market EV of Rs 25,889 Cr. The gap between the DCF EV (Rs 16,000 Cr) and the replacement-cost EV (Rs 20,000-25,000 Cr) is the difference between valuing the cash flows the assets throw off at their sub-cost-of-capital return, and valuing the assets at what it costs to reproduce them. Both are legitimate; the first is a floor when return is below cost of capital, the second is where a strategic buyer transacts.

**C3. Three assets with value and no modelled cash flow.**

- **Evacuation rights.** 3,424 MW connected available plus 2,668 MW applied [FILED, Pres p.35]. In a corridor where connectivity binds nationally, this is scarce and, at the SPV level, transferable with the asset. **Disclosed standalone value, transfer precedent or regulatory valuation basis: NOT DISCLOSED.** Written off in the DCF, and flagged: this is the single most valuable off-model item, because grid access is exactly the scarce resource the whole thesis rests on.
- **The customer platform.** 555 customers, 74% repeat volume, group-captive equity relationships [FILED, Pres/AR]. This is the asset Serentica is spending billions to construct. **No disclosed platform or intangible value; NOT DISCLOSED. Written off in the DCF, flagged as material.**
- **The repowering tail.** Asset life is 30 years for new-technology assets against a 23.17-year weighted PPA tenor. **Bucket 1 already values years 24 to 30, at a re-contracted merchant tariff of Rs 2.50/kWh discounted at 8%** (role1-sotp-01 Bucket 1 schedule). So the PPA-to-merchant tail is IN the model and this item is partly closed. What is NOT modelled is the persistence of the land, evacuation and grid connection beyond 30 years and the repowering option on them; that optionality is written off.

**The model's own position, stated plainly. Rs 178 is a FLOOR, not a fair value.** It is the discounted value of contracted cash flows with growth, scarcity and optionality set to zero, which is exactly what the build specification asked for. A floor is a legitimate and useful answer: it is the price below which the equity is cheap even if nothing goes right and the growth is worth nothing. It is not the central estimate of what the business is worth to a strategic owner, which the informed-buyer price and the replacement-cost multiple both put materially higher.

**Where that leaves the number:**

| Read | Per share (AR net debt) | What it captures |
|---|---|---|
| FLOOR (contracted cash flows, growth/scarcity zeroed, Bucket 2 at 11%) | **Rs 178** | The hard downside |
| CENTRAL (Bucket 2 de-risked to 8% once operating) | **Rs 295** | Contracted assets valued as operating annuities |
| Replacement cost (1.2-1.5x IC, EV Rs 20,000-25,000 Cr) | ~Rs 500-950 | What a strategic buyer pays for the fleet |
| Informed-buyer / market | Rs 1,053 / Rs 1,247 | Growth, platform and scarcity priced in full |

The point is not that Rs 178 is wrong. It is that Rs 178 is the floor and Rs 1,247 is the full-growth price, and the entire gap between them is the value of the growth, scarcity and optionality that the DCF was instructed to zero. Even the replacement-cost read (Rs 500-950) sits below CMP, so the price still prices the growth in full, on any method.

---

## THE CORRECTED BRIDGE AND SENSITIVITY

**Bridge, both Bucket 2 treatments (Bikaner A, Rajasthan 50%, AR net debt):**

| Line | FLOOR Rs Cr | DE-RISKED Rs Cr |
|---|---|---|
| Gross EV (four buckets) | 15,966 | 17,976 |
| Less net debt (AR) | (11,208.80) | (11,208.80) |
| Less acceptances | (1,730.92) | (1,730.92) |
| Equity, 100% consolidated | 3,027 | 5,037 |
| Less NCI at fair value | (378) | (629) |
| Less complexity 12.5%, then x 90% survival | (563) | (937) |
| **Final equity** | **2,086** | **3,470** |
| **Per share (11.75 Cr shares)** | **Rs 178** | **Rs 295** |

Management net-debt basis (gap Rs 1,524.80 Cr, still unbridged, worth ~Rs 90/share): **Rs 267 floor, Rs 385 de-risked.**

**Full sensitivity, per share, AR net debt (discount +/-150bps x Rajasthan siting):**

FLOOR (Bucket 2 at 11%):

| | Raj 0% | Raj 50% | Raj 100% |
|---|---|---|---|
| -150bps | Rs 405 | Rs 351 | Rs 296 |
| base | Rs 226 | **Rs 178** | Rs 129 |
| +150bps | Rs 81 | Rs 38 | Rs (6) |

DE-RISKED (Bucket 2 operating at 8%):

| | Raj 0% | Raj 50% | Raj 100% |
|---|---|---|---|
| -150bps | Rs 569 | Rs 497 | Rs 426 |
| base | Rs 357 | **Rs 295** | Rs 233 |
| +150bps | Rs 188 | Rs 134 | Rs 79 |

**Every cell across both treatments, from Rs -6 to Rs 569, sits below CMP Rs 1,247.** The friendliest defensible combination (de-risked Bucket 2, management net debt, Bikaner B, Rajasthan 0%, -150bps) reaches roughly Rs 700-750, still below the price. The AVOID-on-valuation conclusion does not depend on the Bucket 2 treatment.

---

## PART D ANCHORS FOLDED IN (from halt1-extraction-02)

- **Capitalisation question settled (D1).** On the filed average CWIP of Rs 3,625.87 Cr, interest-only over average CWIP is 5.12% FY26 (conservative), and interest plus LC/BG is 8.61% FY26, which sits 0.21pp ABOVE the 8.4% cost of debt. FY25: 2.58% / 4.16%. So capitalisation is conservative on interest alone and at the ceiling once LC/BG fees are included. FY25 cost of debt is NOT DISCLOSED. This is a capitalisation-quality flag, not a valuation input; the DCF uses only the closing CWIP as sunk cost.
- **Net-debt gap unbridged (D2).** No corpus reconciliation of the Rs 1,524.80 Cr gap exists. The AR nets cash and cash equivalents alone (Rs 1,201.96 Cr) off total debt (Rs 12,410.76 Cr). The Rs 599 Cr of 11.5% NCDs sits inside total debt and was prepaid 2-Apr-2026; if management excludes it, that explains 599 of the gap and leaves Rs 925.80 Cr unexplained. Extraction 01's "current investments Rs 1,021.08 Cr" was a unit error (it is Rs 102.108 Cr). No filed combination lands on Rs 9,684 Cr. Both net-debt bases are carried separately; the gap moves the answer by ~Rs 90/share.
- **LC/BG 6.2x unexplained (D3).** Capitalised LC/BG rose Rs 20.45 -> Rs 126.76 Cr (Note 36c), a 6.2x jump against capex that roughly doubled. LC/BG were also expensed to P&L inside "other borrowing costs" (Rs 48.04 Cr FY26 / Rs 23.77 Cr FY25, bundled with working-capital fees, LC/BG split NOT DISCLOSED). No narrative in the AR, RHP or any concall explains the rise. Carried as a governance/quality flag, not a valuation input.
- **Remaining capex is not filed as a total (D4).** The filed "contracts remaining to be executed on capital account, not provided for" is Rs 830.93 Cr FY26 (Rs 1,513.29 Cr FY25, Rs 3,960.78 Cr at 30-Sep-2025). It is a point-in-time floor on committed spend, not the total remaining cost of the 2,656.66 MW book. **Finding: only ~Rs 831 Cr of the ~Rs 8,150 Cr bottom-up remaining capex is contractually committed at year-end.** The model keeps the Rs 8,150 Cr bottom-up estimate for Bucket 2 (the filed number understates total remaining cost); the low committed figure means the build carries funding and pacing flexibility, which is a mild positive for survival and a mild negative for growth certainty.
- **NCI cross-check (D5).** Note 51 gives per-subsidiary net assets for the three material-NCI subs: Eliora Rs 182.59 Cr (26%), Sapphire Rs 166.31 Cr (26%), Alpha LeaseCo Rs 113.10 Cr (50%). Their accumulated NCI (Rs 147.26 Cr) is only 16.6% of the Rs 885.27 Cr book NCI; the rest sits in non-material subs. Each sub's net assets are a small fraction of its gross assets (Eliora Rs 182.59 Cr net on Rs 552.19 Cr total assets), confirming the SPV equity is structurally thin because the SPVs are debt-funded. This supports valuing NCI below book. The model's NCI fair value (Rs 378 Cr floor, Rs 629 Cr de-risked) is a group-level allocation, flagged [INFERENCE]; the filed material-sub net assets are consistent with a fair-value NCI below the Rs 885 Cr book.

---

## VERDICT (unchanged in direction, sharpened in framing)

The valuation does not change the answer, it clarifies what the answer is. **Rs 178 is a floor, not a fair value.** The central DCF read on de-risked contracted assets is Rs 178 to Rs 295 on the AR basis, Rs 267 to Rs 385 on the management basis. Replacement cost puts the fleet at roughly Rs 500-950. Informed buyers and the market pay Rs 1,053 to Rs 1,247. On every one of these methods the price sits above the value, because the price pays in full for the growth, scarcity and platform that the DCF was instructed to value at zero. The under-execution book is worth roughly what it costs to build, no more. The pipeline earns below its cost of capital. The margin-of-safety entry is Rs 124-133 on the floor and Rs 207-221 on the de-risked central, against a price of Rs 1,247.

*Role 1 SOTP FCFF revision 02, Option A. Valuation date 30-Jun-2026 rolled to 02-Sep-2026. Every number carries its source; NOT FOUND is the only fill. Model in `role1-sotp-model.py`. Bikaner cases, Rajasthan probabilities, and the two net-debt bases are reported separately, never blended. Open items unchanged: the Rs 1,524.80 Cr net-debt gap (NOT DISCLOSED in corpus) and the four VERIFY-LIVE market inputs (G-sec, ERP, beta, peer multiples).*

---

## ADDENDUM 2026-09-04 — RERUN AT LIVE-VERIFIED INPUTS (Task 0.2)

The four VERIFY-LIVE cost-of-capital inputs are now live-verified per Mental Model v7: **risk-free 6.96%** (was 6.5%), **India ERP 7.0%** (was 7.5%), **beta 0.55 unchanged**. The two changes offset almost exactly:

| Item | role1-sotp-02 | Rerun (v7 verified) |
|---|---|---|
| Cost of equity Ke | 13.35% | **13.36%** |
| Group WACC | 10.05% | **10.05%** |
| Bucket rates (1/2/3/4) | 8 / 11 / 14 / 12% | **unchanged** |

Rf rose 0.46pp and ERP fell 0.50pp; with a levered beta of 0.914 the two nearly cancel (Ke +0.01pp). The bucket discount rates are unchanged, so **the equity values are unchanged**:

| Read | AR net debt | Mgmt net debt |
|---|---|---|
| FLOOR (Bucket 2 at 11%) | **Rs 178** | Rs 267 |
| DE-RISKED (Bucket 2 at 8% once operating) | **Rs 295** | Rs 385 |
| EV/IC | 0.95x | — |
| Bucket 2 (Raj 50%): floor / de-risked | (517) / +1,492 | — |

Bucket-level sensitivity is unchanged from Section "Full sensitivity" above (FLOOR span Rs -6 to 405; DE-RISKED span Rs 79 to 569; every cell below CMP Rs 1,247). The live-verified inputs do not move the SOTP dissent. Under Mental Model v7 the governing thesis method is EV/EBITDA forward; this SOTP remains the recorded dissent, not averaged with it.
