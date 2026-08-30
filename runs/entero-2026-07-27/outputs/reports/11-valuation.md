# STAGE 11: ROLE 1 MULTI-MODAL VALUATION — ENTERO HEALTHCARE SOLUTIONS

**Company:** Entero Healthcare Solutions Ltd (ENTERO) | **Run Date:** 2026-07-27
**Model:** claude-opus-4-8 | **Status:** COMPLETE
**Framework:** Master v3.6 / Section 1B v3.3 + v3.5.1 + v3.6 + v3.7 + v3.8 + v3.9 / FTTCP v2.1
**Entity count:** 1 (single-entity pass; entity-count gate does not force a per-entity split)
**CMP for Hurdle/entry (operator-approved):** Rs 1,806 (28-Aug-2026). Manifest Rs 1,273 is stale and NOT used.

---

## 0. PAT / EPS BASIS — SETTLED FROM THE FILED RESULTS (the B10 conflict resolved)

Read from the FY26 audited results PDF (`inputs/results/5d6adb02-...pdf`, Board meeting 25-May-2026), **Consolidated** Statement of Audited Financial Results, Year ended 31-Mar-2026 (Rs in Millions):

| Line (consolidated FY26) | Rs million | Rs Cr | Anchor |
|---|---|---|---|
| Revenue from operations | 65,912.12 | 6,591.21 | results PDF p.11 (matches screener FY26) |
| Profit before exceptional items and tax | 1,875.14 | 187.51 | results PDF p.11 |
| Exceptional items (Note 8, labour-code provision) | 81.78 | 8.18 | results PDF p.11 (a CHARGE) |
| Profit before tax | 1,793.36 | 179.34 | results PDF p.11 |
| Total tax expense | 334.96 | 33.50 | results PDF p.11 |
| **Profit for the year (incl. NCI)** | **1,458.40** | **145.84** | results PDF p.11 |
| — attributable to Owners of the Company | 1,150.42 | **115.04** | results PDF p.11 |
| — attributable to Non-controlling interests | 307.98 | 30.80 | results PDF p.11 |
| Diluted EPS (owners, FY26) | — | **Rs 26.40** | results PDF p.11 |
| Basic EPS (owners, FY26) | — | Rs 26.44 | results PDF p.11 |
| Paid-up equity capital (Rs 10 FV) | 435.11 | 43.51 | results PDF p.11 -> **4.351 Cr diluted shares** |

**Conflict resolved.** The screener figure Rs 115.04 Cr is the **owners' attributable PAT** (after minority interest). The handover/B03 figure Rs 145.84 Cr is the **total consolidated PAT including NCI**. They are the same statement, two lines. Valuation runs on the **owners' basis** (Rs 115.04 Cr, diluted EPS Rs 26.40). EPS is FOUND, not NOT FOUND.

**Operating-EPS separation (FTTCP Module B4).**
- **Exceptional item:** Rs 81.78 million pre-tax charge (labour-code / gratuity provision, Note 8). Strip it. After-tax at ~25% = Rs 61.34 million; owners' share (owners = 78.9% of group PAT) = Rs 48.4 million = Rs 4.84 Cr = Rs 1.11/share.
- **NCI put/call fair value (B02 Finding 5, ~Rs 1.5 bn):** ran through **Other Equity, bypassing P&L**. It does NOT distort reported PAT, so no EPS add-back is made. It is a balance-sheet charge to owners' equity, flagged, not an earnings item.
- **Standalone Rs 175.29 m derivative fair-value gain** is intra-group (subsidiary put option at standalone level); eliminated on consolidation, absent from the consolidated P&L. No adjustment.

**Operating owners' diluted EPS FY26 (Year 0) = 26.40 + 1.11 = Rs 27.5** (reported Rs 26.40 shown alongside; the Rs 1.1 gap is immaterial to the conclusion).

---

## 1. INPUT SNAPSHOT (carried from B10 with anchors)

| Field | Value | Anchor |
|---|---|---|
| CMP | Rs 1,806 (28-Aug-2026) | fttcp-deliberation / handover (B10 cmp_note) |
| Diluted shares | 4.351 Cr | results PDF p.11 (paid-up 435.11 m / Rs 10) |
| Market cap at CMP | Rs 7,858 Cr | 1,806 x 4.351 |
| Net debt FY26 | Rs 327.36 Cr | screener; B02 Finding 6 (Borrowings 677.15 - Cash 161.79) |
| Enterprise value at CMP | Rs 8,185 Cr | 7,858 + 327 |
| FY26 revenue | Rs 6,591.21 Cr | results PDF p.11 |
| FY26 EBITDA margin | 4.03% | B05 |
| FY26 operating owners' EPS (Y0) | Rs 27.5 | Section 0 above |
| ROCE (Pillar 1, operator) | 20-25% forward-capital | fttcp-deliberation (dissent 9.7%/12x recorded) |
| Credibility grade | B (8 delivered / 4 partial / 0 missed) | B05 |
| EM score / class | 19 / MODEST | B07 |
| Sector cap (operator) | 18-20x absolute | fttcp-deliberation (overrides manifest Pharma/CDMO) |
| Destination PE (operator, both tracks) | 18-20x | fttcp-deliberation |
| Earnings basis (operator) | ONE-YEAR-FORWARD P/E | fttcp-deliberation; Amdt 18.1 symmetry |

**Converter classification (v3.7 Amendment 17.0): NON-CONVERTER.** Entero is a pharma/MedTech distribution roll-up. Its inputs are finished drugs and devices bought for resale, not a traded/quoted commodity; margin is a distribution spread on volume, not an input-price spread. 17.1-17.4 do not bind. (Archetype: outsourcing/distribution partner, working-capital-heavy trading.)

**Consumption-clause single-credit check.** ROCE recovery is credited **once**, in Pillar 1 (Strategic Premium ROCE route BARRED per operator). Cash quality is priced **once**, in Pillar 2 (INDETERMINATE). Complexity is priced **once**, in r. No double-credit.

---

## SECTION 1A: METHOD SELECTION

### Method Suitability Matrix (subject-specific)

| Method | Suitable here? | Why |
|---|---|---|
| **P/E** | **YES — PRIMARY** | Profitable, single reportable segment, asset-light trading; earnings basis operator-fixed forward. Section 1B destination PE is the framework's default primary. |
| **EV/EBITDA** | **YES — SECONDARY** | Distributor with rising leverage (D/E 0.17->0.32x); EV normalises the capital-structure shift and cross-checks the thin PAT margin. |
| PEG | Weak | Owners' EPS CAGR distorted by minority-interest drag and loss-to-profit history; PEG unreliable. |
| EV/Sales | Weak | 4-5% EBITDA margin makes sales a poor value proxy; sanity only. |
| **P/B** | **NO** | Goodwill Rs 7,490.9 Cr = 43.8% of net worth (B02 Finding 1); book value distorted by IPO equity + NCI put option through equity. Not applicable (B04). |
| **DCF** | **NO** | FCF INDETERMINATE (no consolidated capex line); CFO negative six of seven years. Too unstable for a terminal-value model. |
| NAV / SOTP | NO | Operating business, single segment; no separable asset value. |
| Lender methods | N/A | Not a lender. |

### Final Method Selection

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E (Section 1B destination) | 70% | Operator-fixed forward basis; single-segment clean earnings after operating-EPS strip. |
| SECONDARY | EV/EBITDA (cross-check) | 30% | Captures leverage; disciplines the thin-margin PAT read. |
| | | 100% | |

Two applied methods with a primary/secondary weighting. Triangulation in Section 3.

---

## SECTION 1B: FOUR-PILLAR DESTINATION PE (operator-approved bases, both tracks)

### Pillar 1 — ROCE Base Multiple
- FTTCP ROCE forward verdict: **RECOVERING** (TEMPORARILY DEPRESSED -> RECOVERING).
- ROCE used (operator forward-capital ruling): **20-25%**, midpoint ~22.5%.
- Continuous formula: Base PE = 0.5 x 22.5 + 7.5 = 18.75 -> operator rounds to **19x**.
- **Pillar 1 normalization route (v3.5.1): NONE at the pillar-math level.** The operator did not run Route A (no >20% CWIP/idle-capital denominator strip evidenced) nor Route B (no dated pre-cycle numerator anchor); the 20-25% is an operator forward-capital ruling carried from FTTCP, not a framework normalization route. Declared: route = none; ROCE recovery credited via Pillar 1.
- ROCE recovery credited via: **Pillar 1** (Strategic Premium route BARRED — single-credit).
- **Dissent recorded:** 12x (standard goodwill-inclusive EBIT/capital, ~9.7% FY26 ROCE). **Reverts to 12x on new M&A > ~Rs 200 Cr / rolling 12m.** Shown as the conservative default-track sensitivity below.

### Pillar 2 — Cash Conversion Multiplier
- Cumulative CFO/PAT FY20-26: **-1.05** (six of seven years negative). FY26 CFO +96.2 Cr (first positive). FCF: **NOT FOUND — INDETERMINATE** (no consolidated capex line; consolidated cash flow shows PP&E purchase Rs 87.42 Cr but the FCF line is not cleanly separable and Pillar 2 was ruled INDETERMINATE upstream).
- Ind-Ra verbatim: "cash flow from operations and free cash flow are likely to remain negative... in the near term" (ratings.pdf p.3). This leans **structural**, but with FCF uncomputable the pillar is **INDETERMINATE**.
- **Determination: INDETERMINATE (<=1.0x, never a clean pass).** Per the wrapper INDETERMINATE rule, the conservative treatment applies: no cash uplift, no growth offset. Operator held the destination at Pillar-1 19x and made Pillar 2 a **disposition cap**, not a numeric PE reduction: the INDETERMINATE cash caps the verdict at **PROCEED WITH CAVEATS / WATCHLIST — no BUY NOW** — it does not lift the 19x.
- Growth offset: **0** (INDETERMINATE / structural lean; no offset).
- **Quality-Adjusted Base = 19x** (Pillar 1, with Pillar 2 acting as a disposition cap, not a multiplier).

### Pillar 3 — Growth Visibility Premium
- EM 19 (MODEST), catalyst near (<12m: margin to 5%, MedTech Rs 1,000 Cr), evidence mostly documented.
- Table: EM below 25 -> **+0x**. Even if the eligibility gate opens on the 20-25% forward ROCE (Amdt 16), EM 19 earns nothing.
- **Growth premium = +0x.** (Sector cap would cap any premium away regardless.)

### Strategic Premium
- **+0x — BARRED.** ROCE re-rating already credited in Pillar 1 (single-credit).

### Undiscovered Alpha
- **DOES NOT APPLY.** FII+DII ~19.8% (Jun-26) > 3%; institutional-absence qualifier fails. UA multiplier NOT applied.

### Sector Reality Cap
- **18-20x (operator-approved, absolute).** Overrides the manifest "Pharma / CDMO" auto-pick. No pharma/MedTech-distribution row exists in Section 1B; the operator substituted 18-20x. Category-Break Override: NOT invoked (no new category, no exclusive binding contract of the qualifying kind). Quality uplift: not available (UA not triggered).

### Four-Pillar Summary (Track 2 — Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 22.5% -> 0.5x22.5+7.5 | 19.0x |
| B. Cash Multiplier | INDETERMINATE — disposition cap, no numeric uplift | (cap only) |
| C. Quality-Adjusted Base | A (Pillar 2 = disposition cap) | 19.0x |
| D. Growth Premium | EM 19 -> +0x | +0x |
| E. Strategic Premium | BARRED | +0x |
| F. Raw Destination PE | C + D + E | 19.0x |
| F2. UA-Adjusted | UA does not apply -> F | 19.0x |
| G. Sector Cap | 18-20x operator, absolute | 20.0x (ceiling) |
| G2. Category-Break Override | N | — |
| G3. Override-Adjusted Cap | = G | 20.0x |
| **H. Final Destination PE (Track 2)** | **min(F2, G3)** | **19.0x** |

**Destination PE range (Amdt 6, H +/- 7.5%): 19 x (1 -/+ 0.075) = 17.6-20.4, rounded to 0.5x = 17.5-20.5x, aligned to the operator's absolute 18-20x -> 18.0-20.0x, mid 19.0x.**

### Track 1 — RRM Derivation
- **Operator-approved RRM track = ~19x at r 13.5%** (RRM = 1 + (13.5-13.5)x0.12 = 1.00 -> 19x). Both tracks land 18-20x. Value on this approved base.
- **Independent RRM divergence (reported, per wrapper rule — valued-on-approved, not overwritten):**
  r-worksheet: r base 14.0% (small/micro); durability adj +0.5 (Unproven band, listed Feb-2024 <5yr — short record priced here, not in r per 12C); governance adj +0.5 (goodwill 44% NW, 40/65 subsidiaries adverse/qualified CARO); cyclical surcharge 0 (not cyclical); complexity adj +0.5 (Amdt 13: high subsidiary count, dense RPT); cash-conversion r-UP: none (12A, priced in Pillar 2); short-record r-UP: none (12C). **Final r = 15.5%** (bounded [9,18]).
  RRM = 1 + (13.5 - 15.5) x 0.12 = 1 - 0.24 = **0.76**. RRM-track destination = 19 x 0.76 = **14.4x**.
  **Divergence flagged:** my independent RRM (14.4x at r 15.5%) sits ~24% below the operator's 19x (r 13.5%). I value on the operator-approved 18-20x, and carry 14.4x as a **conservative sensitivity** alongside the 12x ROCE dissent. Both point the same way: the stock is even more overvalued than the base case shows.

### Dual-track summary

| Track | Low | Mid | High |
|---|---|---|---|
| Track 1 (RRM, operator-approved) | 18.0x | 19.0x | 20.0x |
| Track 2 (Additive, operator-approved) | 18.0x | 19.0x | 20.0x |
| Divergence | 0% | | |
| Conservative sensitivities (reported, not governing) | RRM at r15.5% = 14.4x; ROCE dissent = 12x | | |

**Governing track:** both operator-approved tracks are identical at 18-20x; mid 19x governs the entry zone. The lower conservative sensitivities (14.4x, 12x) are shown but do not overwrite the operator's call.

---

## SECTION 1C: RELATIVE VALUATION CROSS-CHECK (Amendment 20)

**PENDING LIVE PEER TABLE.** This run has no live web access; no live, dated peer table exists. Per Amendment 20.1 and Correction 6, peer multiples are NOT fabricated or pulled from memory. **The pillar destination (19x) GOVERNS this run.** The cross-check to be filled in claude.ai:

| Peer (to fill live) | Trailing PE | Fwd PE | ROCE | Growth | Net debt | Gov flag |
|---|---|---|---|---|---|---|
| Apollo HealthCo / Keimed | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |
| MedPlus Health Services | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |
| (3-4 more listed distributors) | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |

When the live table arrives, apply 20.2-20.4: cluster on normalised earnings, place Entero with named adjustments (lower ROCE on goodwill-inclusive basis, net debt vs peers, governance flags — subsidiary distress, goodwill concentration), rule bear/base/bull relative exit multiples bounded by the 18-20x sector cap, and if the pillar 19x sits >30% below the adjusted peer base, the relative multiple governs and every Amendment 19 line is recomputed on it. **Provisional read:** even a peer cluster near 30x cannot lift Entero's exit above the operator's absolute 18-20x sector cap (20.5 — the cap binds the relative multiple too). So the cross-check is unlikely to move the exit; it is flagged PENDING for completeness, not because it is expected to govern.

---

## SECTION 1B SANITY — THE HURDLE RATIO (Amendment 2)

**Earnings basis: ONE-YEAR-FORWARD (Amdt 18.1). Current PE and destination PE both on forward EPS.**

- Year 0 operating owners' EPS = Rs 27.5. Base Y1 (FY27) EPS = Rs 32.5 (see Section 2).
- **Current forward PE = 1,806 / 32.5 = 55.6x** (trailing-basis cross-check: 1,806 / 27.5 = 65.7x).
- Destination PE mid = 19x.
- Tier A 25% hurdle default (UA / Tier-B quality gates not all met). Pass threshold HR >= 1.953.

| Case | EPS CAGR (3yr) | (1+g)^3 | Dest PE / Current PE | **HR** | Verdict |
|---|---|---|---|---|---|
| Base | 16.7% | 1.589 | 19 / 55.6 = 0.342 | **0.54** | STOP |
| Bull (grade B, usable) | 23.0% | 1.861 | 19 / 52.5 = 0.362 | **0.67** | STOP |

**HURDLE RATIO VERDICT: STOP.** HR(bull) = 0.67 << 1.953. The 25% CAGR is infeasible even on bull-case earnings, because the stock must **de-rate from ~55x forward to ~19x forward** over the hold. Per the rule, the remaining sections are completed for the record and the verdict card reads **AVOID-on-valuation**.

**Would I personally pay 55x forward for a 4-5% margin distributor with structurally negative cash flow, 44% goodwill, and 40 distressed subsidiaries?** No.

*Interim checkpoint (framework STOP point, pipeline continues):* Section 1 complete. Methods P/E primary, EV/EBITDA secondary. Destination PE 18-20x (RRM and additive identical, mid 19x). Current forward PE 55.6x. Hurdle Ratio 0.54 base / 0.67 bull -> STOP. Continuing to Section 2.

---

## SECTION 2: PROJECTIONS (Year 0 to Year 4; hold = 3yr, Year 4 mandatory per Amdt 18.0)

### 2A. Revenue (MODEST EM -> fade to industry ~9% IPM by Year 3, Amdt 14)

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue CAGR (Y0->Y3) | ~11% | ~16% | ~20% |
| Logic | Organic converges to IPM; WC funding gap bites; M&A pause bites growth | Guidance 23% ex-M&A discounted for grade B, fading | Guidance at face (grade B allows); MedTech scales |

### 2B. Profitability
- EBITDA margin: 4.03% (FY26) -> 5.0% by Y1-Y2 (already hit 5.0% Q1 FY27), held thereafter.
- Owners' PAT margin thin (~1.8% operating FY26); expands modestly with operating leverage, **partly offset by rising minority interest (~27% of PBT-minority) and rising interest cost** (D/E 0.17->0.32x). Note: FY26 owners' PAT grew +21.3% while revenue grew +29.4% — owners' EPS grows SLOWER than revenue historically; projections respect that drag.

### 2C. Projection table — operating owners' diluted EPS (Rs), BASE case primary

| Line | Y0 FY26 | Y1 FY27 | Y2 FY28 | Y3 FY29 | Y4 FY30 |
|---|---|---|---|---|---|
| Revenue (Rs Cr) | 6,591 | 7,909 | 9,175 | 10,275 | 11,300 |
| Revenue growth | — | +20% | +16% | +12% | +10% |
| EBITDA margin | 4.03% | 4.8% | 5.0% | 5.0% | 5.0% |
| **Operating owners' EPS (base)** | **27.5** | **32.5** | **38.0** | **43.7** | **48.9** |
| EPS growth (base) | — | +18% | +17% | +15% | +12% |
| Operating owners' EPS (bear) | 27.5 | 29.7 | 32.0 | 34.5 | 36.5 |
| Operating owners' EPS (bull) | 27.5 | 34.4 | 42.6 | 51.6 | 60.9 |
| Est. net debt (Rs Cr) | 327 | rising (WC gap ~Rs 1,000-1,100 Cr by yr3, B09) | | | |
| Est. ROCE (owners forward-capital) | 20-25% | flat-to-up | | | |

EPS CAGR (Y0->Y3): **bear 7.8% | base 16.7% | bull 23.3%.**

### 2D. Sanity checks

| Check | Result | Pass |
|---|---|---|
| Revenue faster than capacity? | No — financing-constrained (WC gap), not capacity; base 16% < SOM-implied 26.4% | OK |
| Margins unprecedented? | No — 5% already printed Q1 FY27 | OK |
| ROCE > 15%? | Operator forward-capital 20-25%; goodwill-inclusive dissent 9.7% flagged | FLAG |
| FCF funds growth without excess debt? | **NO** — WC gap Rs 1,000-1,100 Cr by yr3; net debt rising; FCF INDETERMINATE | **FLAG-CASH** |
| EPS growth operational, not engineered? | Yes, but minority drag caps owners' share | OK |
| Market-share gain realistic? | Yes — 2.5% SAM share, 39.9x headroom (B09) | OK |
| CFO/PAT consistent with Pillar 2? | INDETERMINATE; single positive year only | FLAG |
| Y3 ROCE consistent with Pillar 1 verdict (RECOVERING)? | Yes on forward-capital basis | OK |

**SOM cross-check:** base revenue CAGR 16% is **below** SOM-implied 26.4% (B09). Consistent — the base is conservative, no cut needed.

*Interim checkpoint:* Section 2 complete. Year 4 built (Amdt 18.0). Continuing to Section 3.

---

## SECTION 3: APPLY METHODS

### PRIMARY — P/E (Section 1B destination, forward exit basis)

Exit price (3-yr hold) = Destination PE x **Year 4 (FY30) forward EPS** (Amdt 18.1: forward entry -> forward exit; exit at end-Year-3 prices on FY30 EPS).

**Target price matrix (3-year), vs CMP Rs 1,806:**

| | Exit PE 18x | Exit PE 19x (mid) | Exit PE 20x |
|---|---|---|---|
| **Bear EPS Y4 = 36.5** | Rs 657 -> -27.9% | Rs 694 -> -27.3% | Rs 730 -> -25.5% |
| **Base EPS Y4 = 48.9** | Rs 880 -> -21.3% | Rs 929 -> -20.2% | Rs 978 -> -18.6% |
| **Bull EPS Y4 = 60.9** | Rs 1,096 -> -15.4% | Rs 1,157 -> -13.8% | Rs 1,218 -> -12.3% |

Colour: every cell RED (all < 15% CAGR; all negative). **No scenario, on any exit multiple in the operator's range, returns capital at CMP.** Best case (bull EPS x 20x) = Rs 1,218 = -12.3% CAGR.

### SECONDARY — EV/EBITDA (cross-check)
- Fair-value EV at destination (base): fair mcap = 19 x 32.5 x 4.351 = Rs 2,687 Cr; +net debt 327 = **EV ~Rs 3,014 Cr**. FY27 EBITDA = 7,909 x 4.8% = Rs 380 Cr. **Implied fair EV/EBITDA ~7.9x forward** — reasonable for a thin-margin pharma distributor.
- At CMP: EV Rs 8,185 Cr / FY27 EBITDA Rs 380 Cr = **21.6x forward EV/EBITDA** — rich for a 4-5% margin distributor with negative FCF. Confirms overvaluation. Divergence from the P/E read is < 25%; no governing-choice override needed. Both methods agree: fair value ~Rs 585-650, CMP ~Rs 1,806.

### Triangulation

| Method | Weight | Fair value (base, today, forward) |
|---|---|---|
| P/E (primary) | 70% | Rs 617 (19 x 32.5) |
| EV/EBITDA (secondary) | 30% | Rs ~605 (7.9x fwd EBITDA, equity-bridged) |
| **Weighted fair value (today)** | 100% | **~Rs 613** |

---

## SECTION 4: ENTRY ZONE, FV PATH, RISK-REWARD (Amendments 18-19)

### Today's fair value (governing track, base, forward basis)
- FV today = 19 x FY27 EPS (32.5) = **Rs 617** (range on 18-20x: Rs 585-650).
- **CMP Rs 1,806 = ~2.9x fair value.** Downside to fair value = -66%.

### Entry zone for 25% CAGR (entry = base exit / 1.25^3 = exit / 1.953)
- Base exit (mid 19x, Y4 EPS 48.9) = Rs 929 -> entry = 929 / 1.953 = **Rs 476**.
- Range: low (18x exit 880)/1.953 = Rs 451; high (20x exit 978)/1.953 = Rs 501.
- **Entry zone: Rs 451-501 (mid ~476).**

### Margin-of-safety price
- Evidence mostly-documented but with INDETERMINATE cash and the network-reach contradiction (FLAG-EMOAT-NETWORK) -> the more conservative **30% MoS** (mixed evidence quality), not 20%.
- MoS price = today's FV mid (Rs 617) x (1 - 0.30) = **Rs 432.**
- Binding buy trigger = the lower of the 25%-CAGR entry and the MoS price = **Rs 432** (and the whole zone Rs 432-501 sits ~72-76% below CMP).

### FV Path Table (Amendment 19.0 — governing track, base case, forward basis)

| Point | Forward EPS used | FV = 19x x EPS |
|---|---|---|
| Today | FY27 = 32.5 | Rs 617 |
| End-Year-1 | FY28 = 38.0 | Rs 722 |
| End-Year-2 | FY29 = 43.7 | Rs 830 |
| End-Year-3 (exit) | FY30 = 48.9 | Rs 929 |

**FV CAGR over the hold: 14.6% (today Rs 617 to end-Year-3 Rs 929, governing track, base case).** [(929/617)^(1/3) - 1]

**Return-source classification (19.2): HYBRID (FV CAGR 10-20%).**

**Decomposition (19.3):** Fair value compounds ~14.6% on owners' EPS growth (revenue mid-teens fading to IPM + EBITDA margin 4->5% operating leverage, net of rising minority interest and interest cost). There are **zero option/SOTP slices** (single operating entity), so 0% of FV is non-compounding static value. **No re-rating lever remains in fair value** — the multiple is already held at the destination 19x. Critically, the LIVE market multiple (~55x forward) sits ~2.9x ABOVE the destination, so the only re-rating available to a buyer at CMP is a ~66% DE-RATING. At CMP the realised return is the FV CAGR MINUS a ~19%/yr multiple compression = deeply negative (see below). The entry zone does ALL the work and is ~74% below CMP; reaching it needs a market fall, not price drift.

**FV-step events (19.4): NONE.** No within-hold option slices (single-entity operating business; no resolution calendar). N/A.

### Probability-weighted expected return at CMP (weights 25/50/25, grade B)
Exit prices (mid 19x, Y4 EPS): bear Rs 694 (-27.3%), base Rs 929 (-20.2%), bull Rs 1,157 (-13.8%).
**Expected 3-yr price CAGR = 0.25(-27.3) + 0.50(-20.2) + 0.25(-13.8) = -20.4%.**

### Upside/Downside at CMP
- Best-case (bull, 20x) exit Rs 1,218 = still -33% below CMP; worst-case (bear, 18x) exit Rs 657 = -64%.
- **No scenario exceeds CMP. Upside/downside ratio = 0 (no upside at CMP).**

---

## RECOGNITION-GAP RESOLUTION (override 13)

The signed mental model's RECOGNITION GAP resolves here as the PE-gap check. Current forward PE ~55x (trailing ~66x) sits FAR ABOVE the TO-rung neighbourhood (R3 value-added supplier ~19x / R4 franchise ~21x). The market has priced the stock **beyond** any TO rung the transition could reach. **The re-rating engine is not spent — it is negative:** the destination-PE delta over the current PE is a ~36-turn COMPRESSION. Per the Transition Decision Matrix, this is a **gap CLOSED (over-closed)** state; the return cannot ride re-rating and must ride EPS CAGR alone against a large de-rating headwind. On the matrix, absent a fired-and-artifact reading at this price, the posture is a **PRICED NARRATIVE** overlay — clean-looking optics, transition partly narrated, TO state already over-priced. Verdict-card consequence: the return is EPS-only, and even EPS-only fails the Hurdle at CMP.

---

## SECTION 5: VERDICT CARD

| Field | Value |
|---|---|
| **Company** | Entero Healthcare Solutions Ltd (ENTERO) |
| **CMP** | Rs 1,806 (28-Aug-2026) |
| **Earnings basis** | One-year-forward P/E (Amdt 18.1 symmetry, both ends) |
| **Destination PE — Track 1 (RRM)** | 18-20x, mid 19x (operator-approved; independent RRM at r15.5% = 14.4x flagged conservative) |
| **Destination PE — Track 2 (Additive)** | 18-20x, mid 19x |
| **Track divergence** | 0% (both operator-approved at 18-20x) |
| **Governing track** | Both identical; mid 19x governs. Conservative sensitivities: 14.4x (RRM r15.5%), 12x (ROCE dissent) |
| **Fair value today (base)** | Rs 617 (range 585-650) |
| **Hurdle Ratio** | 0.54 base / 0.67 bull -> **STOP** |
| **FV CAGR** | **14.6% — HYBRID** |
| **Recognition gap** | Over-closed; re-rating engine NEGATIVE (~55x fwd -> 19x); return is EPS-only and still fails |
| **Entry zone (25% CAGR)** | Rs 451-501 |
| **MoS price (30%)** | Rs 432 |
| **Binding entry trigger** | Rs 432 (~76% below CMP) |
| **Expected 3-yr CAGR at CMP** | -20.4% (prob-weighted 25/50/25) |
| **Upside/Downside at CMP** | 0 (no scenario exceeds CMP) |
| **Cash cap** | INDETERMINATE -> caps disposition at PROCEED WITH CAVEATS / WATCHLIST; NO BUY NOW even in the entry zone until H1 FY27 (~Nov 2026) resolves capex/FCF |
| **Amendment 20 (Step 1C)** | PENDING LIVE PEER TABLE; pillar 19x governs this run |
| **SHARED CATALYST** | M&A pause drives both Pillar 1 ROCE recovery and Pillar 3 margin/MedTech story — Role 3 must stress-test the single lever |
| **Converter class** | NON-CONVERTER (Amdt 17 does not bind) |
| **DECISION** | **AVOID (on valuation)** |

### Flags carried forward
- **FLAG-CASH (MAJOR):** Pillar 2 INDETERMINATE; FCF uncomputable; CFO negative six of seven years; caps any future positive verdict at WATCHLIST / PROCEED WITH CAVEATS. Applied multiplier: none (disposition cap).
- **FLAG-EMOAT-NETWORK (HIGH):** reach -28 to -36% while warehouses rose; unreconciled; TOP Halt-1 item.
- **FLAG-GOODWILL-CONCENTRATION (MAJOR):** goodwill 43.8% of net worth; impairment risk to book.
- **FLAG-SUBSIDIARY-DISTRESS (HIGH):** 40 of ~65 subsidiaries adverse/qualified CARO.
- **FLAG-LEVERAGE-DIRECTION (MEDIUM):** gross D/E 0.17->0.32x; net cash to net debt Rs 327 Cr.
- **ROCE dissent / M&A reversion:** 12x dissent (goodwill-inclusive ~9.7%); reverts to 12x on new M&A > ~Rs 200 Cr / rolling 12m — every fair value then falls ~1/3.
- **RRM divergence (reported):** independent RRM at r 15.5% = 14.4x, ~24% below the operator's 19x; valued on operator base, sensitivity carried.

### One-line thesis
A 4-5% margin pharma distributor priced at ~55x forward (2.9x its Rs 617 fair value) must de-rate to ~19x; even bull earnings return -12%/yr from CMP, so this is AVOID-on-valuation, actionable only near Rs 432-501 and only after the INDETERMINATE cash resolves.

---

## END OF ROLE 1 VALUATION
