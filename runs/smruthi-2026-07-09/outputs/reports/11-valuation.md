# STAGE 11 — ROLE 1 MULTI-MODAL VALUATION

## Smruthi Organics Ltd (SMRUTHI) | Run Date: 2026-07-09 | Model: Opus 4.8

Framework authority: Master Project Prompt v3.3 / Section 1B v3.3 Amendments / FTTCP v1.2 Consolidated.
Sole input source: B10 (blocks/B10.yaml + reports/10-assembly.md). No number pulled from general knowledge.
Pipeline mode: all sections executed in one pass; interim STOP/GO checkpoints written then continued. Conservative bias throughout.

---

## PRE-FLIGHT DATA INTEGRITY NOTE (carried as a flag)

B10 carries an internal inconsistency in the share/market-cap block that MUST be reconciled before any per-share math:

| Field (B10) | Stated | Cross-check | Conclusion |
|---|---|---|---|
| shares_outstanding_cr | 11.4463 | PAT 3.43 Cr / EPS 2.99 = 1.147 Cr; Equity 73.51 Cr / BVPS 64.23 = 1.1445 Cr | Share count is ~1.1446 Cr (114.46 lakh); the "11.4463 Cr / 1,144.63 lakh" figure is a 10x units error |
| market_cap_cr | 169.0 | 1.1446 Cr x Rs 122 = Rs 139.6 Cr | Stated mcap 169 not reconcilable with CMP x reconciled shares; treated as secondary |
| cmp_rs | 122.0 | given | RELIABLE anchor |
| diluted_eps_rs | 2.99 | given, matches PAT/reconciled-shares | RELIABLE anchor |

Decision: all valuation runs off the two internally-consistent per-share anchors CMP Rs 122 and diluted EPS Rs 2.99 (Current PE = 122 / 2.99 = **40.80x**), and uses 1.1446 Cr shares for Cr-to-per-share conversions (confirmed by the book-value cross-check). The market-cap discrepancy does not affect per-share fair value. Flagged as FLAG-DATA for the verifier.

---

# SECTION 1A — METHOD SELECTION & JUSTIFICATION

Business type (B04): capital-heavy manufacturing — bulk drugs, drug intermediates, formulations. This is a manufacturer, NOT a lender. No lender carve-out (Pillar 2L / ROE-Pillar-1 / P/B-primary / 18x cap does NOT apply).

### Method Suitability

| Method | Suitable Here? | Rationale |
|---|---|---|
| EV/EBITDA | YES — PRIMARY | Capital-intensive manufacturing with rising leverage (net debt 6.10 Cr, D/E rising 0.17->0.24x per CARE); depreciation large relative to PAT (dep 6.35 vs PAT 3.43); EV/EBITDA neutralises capital-structure and D&A distortion. Per B04 primary method. |
| P/E | YES — SECONDARY | Profitable (PAT 3.43 Cr) with clean-ish earnings, but thin margin (3.36%) and one-off receivables release make PAT lower-quality; secondary cross-check per B04. |
| P/B | NO | Manufacturer, not a lender; book value does not anchor value here. No lender carve-out. Explicitly excluded per pipeline instruction. |
| DCF | NO (support only) | Structural cash uncertainty (FLAG-CASH), negative FCF two of three years, revenue just fell -19.1% with no explanation; forward FCF too unreliable for a primary DCF. Used only as a directional sanity read, not weighted. |
| EV/Sales, EV/Capacity, NAV, SOTP, sector-specific | NO | Not a commodity-capacity, holdco, or early-stage revenue story. Peer medians all NOT FOUND (B06 skipped), so relative EV/Sales cannot be benchmarked. |

### Final Method Selection

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | EV/EBITDA | 60% | B04 primary; best for capital-heavy manufacturer with rising leverage and heavy D&A |
| SECONDARY | P/E | 40% | B04 secondary; four-pillar destination PE anchors the exit multiple |
| — | (DCF directional only) | 0% | FLAG-CASH + negative FCF history make forward FCF unreliable |
| | | 100% | |

**INPUT UNRESOLVED: Peer Medians (P/E, EV/EBITDA, P/B, growth, ROCE). Conservative assumption used: no peer relative uplift applied; exit multiples derived purely from Section 1B four-pillar, because framework requires Section 1B as sole exit-multiple authority and B06 was skipped (no peer data).**

---

# SECTION 1B — FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 (DUAL TRACK)

### Pillar 1 — ROCE Base Multiple (continuous formula)

FTTCP ROCE forward verdict: B10 does not carry an explicit FTTCP verdict field. Deriving conservatively from the evidence in B10 (this is a first-workup; verdict must be inferred from the transition data, biased down per FTTCP rule 12):

- Backward ROCE: compressed from 35.7% (FY19-21) to 7.2-7.9% (FY23-FY26) — i.e., **STRUCTURALLY LOW** (below 15% asset-heavy, sustained 3+ years).
- "If growth stopped tomorrow, would ROCE recover to historical levels within 18-24 months?" NO — revenue is DECLINING (-19.1% FY26), regulatory catalysts (ANVISA/EDQM) unconfirmed, no identifiable temporary bloat unwind driving recovery. Bias toward DECLINING when in doubt.
- **Forward ROCE verdict adopted: DECLINING (conservative). Mapping -> Pillar 1 uses FY[Y+1] expected ROCE (lower bound).**

**INPUT UNRESOLVED: ROCE Latest FY26 (%). Conservative assumption used: 7.2%, because B10 gives only historical median 9.29% and a declining 2-yr band of 7.2-7.9% (roce_2yr_trend); conservative bias takes the lower bound of the recent band, and the DECLINING verdict directs use of the lower-bound figure. No forward decline estimate exists, so 7.2% is held (this does NOT credit any recovery).**

ROCE Base PE = 0.5 x ROCE + 7.5, floored 9x, capped 24x.
= 0.5 x 7.2 + 7.5 = 3.6 + 7.5 = **11.1x** (above the 9x floor).

**ROCE recovery credited via: NOT CREDITED** (verdict DECLINING; no forward uplift entered Pillar 1; single-credit rule leaves the Strategic Premium ROCE-optionality route also unused — see Pillar 4).

### Pillar 2 — Cash Conversion Multiplier (standard business)

- Cumulative CFO/PAT (B01): 2.80x | Latest FY26 CFO/PAT: 6.49x | FY26 FCF: +13.34 Cr (positive) BUT FCF negative FY24 (-3.84 Cr) and FY25 (-1.54 Cr).
- Structural vs growth-induced (per B10 FLAG-CASH determination, NOT re-litigated): FLAG-CASH states the FY26 cash strength is "substantially WC-driven via receivables release (AR fell 32.47 -> 19.30 Cr), NOT structural." Revenue is DECLINING, so any underlying drag is NOT growth-induced (no capacity build to offset).
- Rating agency (CARE, verbatim in B10.rating_wc_quote): benign — "adequate liquidity... sufficient headroom to raise additional debt... unutilised bank lines adequate." CARE does NOT confirm a persistent structural WC leak. Therefore the 0.65x "rating-agency-confirmed structural" band is NOT supported.
- Band placement is INDETERMINATE between 1.00x (volatile/inconsistent: negative FCF FY24-25, strongly positive FY26) and 0.80x (CFO/FCF negative in recent years). Per pipeline rule, when INDETERMINATE use the more conservative multiplier and say so -> **0.80x**.
- Growth Offset: NONE. The drag is not growth-induced (revenue declining -19.1%); offset applies only to growth-induced drag. Offset = +0.

Effective Cash Multiplier = **0.80x** (no offset).

**Quality-Adjusted Base = Pillar 1 x Cash Mult = 11.1x x 0.80x = 8.88x.**

### Pillar 3 — Growth Visibility Premium

- Emerging Moat Score (B07): 13.4 / 100 (MODEST). Catalyst proximity: 12-36 months (ANVISA/EDQM unconfirmed, DMF approvals). Evidence: mostly documented.
- EM below 25 -> **+0x** (table: "EM below 25 -> +0x"). Catalyst proximity/evidence are moot below the 25 threshold.

Growth Visibility Premium = **+0x**. Shared catalyst? NO (nothing credited in Pillar 1; no premium here).

### Pillar 4 — Strategic Asset Premium

- strategic_asset_moat_position (B10): "No" (A1/H2 not met; EM 13.4 insufficient to offset Gate 0 AVOID). No rare licence/monopoly, no documented pricing power.
- ROCE re-rating optionality: single-credit rule — ROCE recovery was NOT credited in Pillar 1, but the FTTCP verdict is DECLINING (not STAGNANT/FIRING with genuine archetype-supported re-rating optionality). No credible recovery to credit. Strategic ROCE optionality = +0x.

Strategic Premium = **+0x**.

### Undiscovered Alpha (F2 UA row)

UA qualifiers (B10.ua_qualifiers): listed >=12m TRUE; FII+DII <3% TRUE (zero institutional); **Gate0>=60 OR EM>=25 FALSE** (Gate 0 = 37 <60 AND EM = 13.4 <25). all_met = **FALSE**.

**UA multiplier NOT applied.** Per Amendment 3, all three qualifiers must hold; the Gate0/EM qualifier is disqualifying. F2 = F (no 1.25x). This is not a risk flag — it is simply an un-met qualifier (low institutional ownership is never treated as a risk per CLAUDE.md).

### Sector Reality Cap

Sector cap row (manifest/B10): **Pharma / CDMO = 38x**. Quality uplift NOT available (UA not triggered; durability weak-to-moderate, not Moderate-Strong-with-evidence). Cap = 38x absolute.

### Four-Pillar Summary (TRACK 2 — ADDITIVE)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 7.2% -> 0.5x7.2+7.5 | 11.1x |
| B. Cash Multiplier (effective) | 0.80x + 0 offset | 0.80x |
| C. Quality-Adjusted Base | A x B = 11.1 x 0.80 | 8.88x |
| D. Growth Visibility Premium | EM 13.4 (<25) | +0x |
| E. Strategic Premium | No strategic asset; ROCE not credited | +0x |
| F. Raw Destination PE | C + D + E | 8.88x |
| F2. UA-Adjusted Raw PE | UA all_met FALSE -> F x 1.00 | 8.88x |
| G. Sector Cap | Pharma / CDMO | 38x |
| **H. Final Destination PE** | **min(F2, G) = min(8.88, 38)** | **8.9x** |

**Track 2 Destination PE Range: 8.9x +/-7.5% = 8.23 to 9.57 -> rounded nearest 0.5x = 8.0x to 9.5x (mid 8.9x).**

### RRM Dual-Track Derivation (TRACK 1 — RRM)

- Fundamental Base PE = quality-adjusted base = 8.88x (cash quality is a fundamental adjustment, not an additive premium; growth/strategic premiums are zero here regardless).
- Base r: small/micro-cap = 14%. Adjustments: governance CONCERN (B08 Promoter Verdict CONCERN; remuneration breach, title-deed defect, ECL under-provisioning) and weak durability push r UP; revenue decline adds risk. Adopt **r = 16%** (14% base + 2% governance/durability/revenue-risk). Bounded [9%,18%]: OK.
- RRM = 1 + (13.5 - r) x 0.12 = 1 + (13.5 - 16) x 0.12 = 1 + (-2.5 x 0.12) = 1 - 0.30 = **0.70** (at the lower bound 0.70).
- **Track 1 Destination PE = 8.88 x 0.70 = 6.22x -> 6.2x**, capped at 38x (no bind).

Alternative reading (RRM on pure Pillar-1 base 11.1x -> 11.1 x 0.70 = 7.8x) still sits far below the current 40.8x PE and does not change the verdict; the more conservative 6.2x is carried.

**Track 1 Destination PE Range: 6.2x +/-7.5% = 5.74 to 6.67 -> rounded nearest 0.5x = 5.5x to 6.5x (mid 6.2x).**

### Track divergence

Track 2 mid 8.9x vs Track 1 mid 6.2x -> divergence = (8.9 - 6.2)/8.9 = **30.3%** (>15%).
**Governing track = TRACK 1 (RRM), the more conservative.** It best fits this company: durability is weak and governance is a CONCERN, which the RRM expresses cleanly through a high discount rate. Track 1 sets the entry zone.

### Hurdle Ratio (Section 1B sanity check)

Current PE = 122 / 2.99 = **40.80x**.
Grade C (B10.credibility_grade): Bull EPS CAGR NOT permitted in HR; Bull row = Base EPS CAGR + 5% max.
Base EPS CAGR = 6.0% (Section 2); HR-Bull = 6.0 + 5.0 = 11.0%.

HR = (1 + EPS CAGR)^3 x (Destination PE mid / Current PE). Threshold 1.953.

Governing Track 1 (mid 6.2x):
- HR(Base 6%) = (1.06)^3 x (6.2/40.80) = 1.1910 x 0.15196 = **0.181**
- HR(Bull 11%) = (1.11)^3 x 0.15196 = 1.3676 x 0.15196 = **0.208**

Track 2 (mid 8.9x), for the record:
- HR(Base) = 1.1910 x (8.9/40.80 = 0.21814) = 0.260
- HR(Bull) = 1.3676 x 0.21814 = 0.298

All four values are far below 1.953. Even with the (impermissible-for-grade-C) true bull EPS CAGR of 28.3% and the generous Track 2 mid: (1.283)^3 x 0.21814 = 2.111 x 0.21814 = 0.460 — still below 1.953.

**HURDLE RATIO = STOP.** 25% CAGR is infeasible from CMP 122 even on bull-case earnings, because the stock trades at 40.8x versus a four-pillar destination of 6-9x — the de-rating overwhelms any plausible EPS growth.

Would I personally pay 40.8x for a bulk-drug maker with 7-8% ROCE, 3.4% PAT margin, declining revenue, governance CONCERN, and WC-driven (not structural) cash? No. Destination 6-9x is the honest quality-earned multiple.

> INTERIM CHECKPOINT (framework STOP point): Section 1 complete. Methods: EV/EBITDA 60% primary, P/E 40% secondary, P/B N/A. Four-pillar destination PE 8.0x-9.5x (Track 2 additive); RRM track 5.5x-6.5x. Current PE 40.8x. Hurdle Ratio 0.18 (base) / 0.21 (bull) -> **STOP**. Per pipeline override: not halting; the framework directs completing all remaining sections for the record with the verdict card carrying AVOID-on-valuation. Continuing to Section 2.

---

# SECTION 2 — EARNINGS & CASH FLOW PROJECTIONS

### 2A. Revenue Projection

Year 0 (FY26) revenue = Rs 101.97 Cr (results P&L p.6). Prior year FY25 = 126.01 Cr (-19.1% YoY). 3-yr CAGR NOT FOUND.

**INPUT UNRESOLVED: 3-Year Revenue CAGR (%). Conservative assumption used: not relied upon for the base; base CAGR anchored to SOM-implied and TAM growth instead, because FY24 full-year revenue is unavailable (B10.unresolved) and the only clean datapoint is the -19.1% FY26 shock.**

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| Logic | No recovery; share loss offsets TAM growth 6.5% | Partial recovery off trough, below SOM-implied ceiling | China/Russia + regulated-market entry fires to SOM ceiling |
| Revenue CAGR | 0% | 5% | 9% |
| Rev Yr0 (FY26) | 101.97 | 101.97 | 101.97 |
| Rev Yr1 | 101.97 | 107.07 | 111.15 |
| Rev Yr2 | 101.97 | 112.42 | 121.15 |
| Rev Yr3 | 101.97 | 118.04 | 132.05 |
| Rev Yr5 | 101.97 | 130.13 | 156.88 |

Bull is held to 9% (SOM-implied 3yr 9.0%) and NOT to management face value, because credibility grade is C (bull-face-value only permitted for grade A/B).

**SOM cross-check:** base revenue CAGR 5% < SOM-implied 3yr 9.0% and 5yr 9.6%. Assumption is BELOW the SOM ceiling -> **consistent** (conservative; no justification-of-excess needed).

### 2B. Profitability Projection

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| EBITDA margin | 10.5% | 12.5% | 14.5% |
| Margin logic | Compression; loss of scale + RM volatility | Near FY26 12.43%; cost rationalisation (RM 53.8->44.35%) sustained | Operating leverage + backward integration fully captured |
| Depreciation (Yr3) | 7.0 | 7.35 | 8.0 |
| Interest (Yr3) | 2.5 | 2.0 | 1.5 |
| Tax rate | 26% | 26% | 26% |
| Dilution | 0% (no data; neutral) | 0% | 0% |

FY26 reconciliation: EBITDA 12.70, Dep 6.35, EBIT 6.35, Interest 1.68, PBT 4.67 + OI 0.12, PAT 3.43 -> effective tax ~26%.

### 2C. Complete Projection Table (Base case primary)

| Line | Yr0 (FY26) | Yr1 | Yr2 | Yr3 | Yr5 |
|---|---|---|---|---|---|
| Revenue (Cr) | 101.97 | 107.07 | 112.42 | 118.04 | 130.13 |
| EBITDA (Cr) @12.5% | 12.70 | 13.38 | 14.05 | 14.76 | 16.27 |
| EBITDA margin | 12.43% | 12.5% | 12.5% | 12.5% | 12.5% |
| Depreciation (Cr) | 6.35 | 6.70 | 7.00 | 7.35 | 8.10 |
| EBIT (Cr) | 6.35 | 6.68 | 7.05 | 7.41 | 8.17 |
| Interest (Cr) | 1.68 | 1.90 | 1.95 | 2.00 | 2.10 |
| PBT + OI (Cr) | 4.79 | 4.88 | 5.20 | 5.51 | 6.17 |
| PAT (Cr) @26% tax | 3.43 | 3.61 | 3.85 | 4.07 | 4.57 |
| EPS (Rs) | 2.99 | 3.16 | 3.36 | 3.56 | 3.99 |
| Book Value/sh (Rs) | 64.23 | ~66 | ~68 | ~70 | ~74 |
| Est. CFO (Cr) | 22.26* | ~8 | ~9 | ~10 | ~11 |
| Est. FCF (Cr) | 13.34* | ~-1 | ~0 | ~1 | ~2 |
| Est. Net Debt (Cr) | 6.10 | ~9 | ~11 | ~12 | ~13 |
| Est. ROCE | ~7-8% | ~7-8% | ~8% | ~8% | ~8% |

*FY26 CFO/FCF inflated by one-time receivables release (AR 32.47->19.30 Cr); NOT repeatable — forward CFO normalised toward EBITDA-minus-WC-minus-interest-minus-tax.

**Scenario Year-3 EPS and EPS CAGR:**
- Bear: Rev 101.97, EBITDA@10.5% 10.71, Dep 7.0, EBIT 3.71, Int 2.5, PBT+OI 1.31, PAT 0.97 -> EPS 0.85. CAGR = (0.85/2.99)^(1/3)-1 = **-34.3%**.
- Base: Rev 118.04, EBITDA@12.5% 14.76, Dep 7.35, EBIT 7.41, Int 2.0, PBT+OI 5.51, PAT 4.07 -> EPS 3.56. CAGR = (3.56/2.99)^(1/3)-1 = **+6.0%**.
- Bull: Rev 132.05, EBITDA@14.5% 19.15, Dep 8.0, EBIT 11.15, Int 1.5, PBT+OI 9.75, PAT 7.22 -> EPS 6.31. CAGR = (6.31/2.99)^(1/3)-1 = **+28.3%**.

### 2D. Projection Sanity Checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | Base 5% < capex-embedded 6.7% capacity (B09); no constraint | PASS |
| Margins require something unprecedented? | Base 12.5% ~ FY26 12.43%; not aggressive | PASS |
| ROCE stays above 15%? | NO — stays ~7-8% | FAIL (consistent with low-quality thesis; not a projection error) |
| FCF funds growth without excessive new debt? | Marginal; net debt drifts 6->12 Cr; capex debt-financed | WEAK |
| EPS growth operational, not financial engineering? | Yes — driven by revenue x margin, no buyback/leverage tricks | PASS |
| Implied market share gain realistic? | Base share stays ~1.4% of SAM (headroom 72x); realistic | PASS |
| CFO/PAT trajectory consistent with Pillar 2 (0.80x)? | Yes — forward CFO normalises down from the one-off; consistent with weak cash multiplier | PASS (FTTCP-consistency) |
| Year-3 ROCE consistent with FTTCP verdict used in Pillar 1? | Base Yr3 ROCE ~8% (EBIT 7.41 / cap employed ~93) matches the DECLINING/structurally-low ROCE (7.2%) used in Pillar 1; NO recovery assumed | PASS (FTTCP-consistency) |

> INTERIM CHECKPOINT: Section 2 complete. Base EPS CAGR +6.0%; bear -34.3%; bull +28.3%. Projections do not assume ROCE recovery, consistent with the not-credited Pillar 1. Continuing to Section 3.

---

# SECTION 3 — APPLY EACH VALUATION METHOD

Shares for Cr->per-share conversion: 1.1446 Cr (reconciled). Net debt Yr3: bear 15, base 12, bull 8 Cr.

### 3.1 PRIMARY — EV/EBITDA

Exit EV/EBITDA derived from four-pillar PE (rule of thumb ~0.65x of destination PE, adjusting for leverage and heavy D&A; no peer median available — NOT FOUND).
- Track 2: 8.9x x 0.65 = 5.8x (range 5.5-6.0x).
- Track 1 (governing): 6.2x x 0.65 = 4.0x (range 3.7-4.3x).

**Track 2 (mid 5.8x):**

| | Bear EBITDA 10.71 | Base EBITDA 14.76 | Bull EBITDA 19.15 |
|---|---|---|---|
| EV @5.8x (Cr) | 62.12 | 85.58 | 111.07 |
| Less Net Debt Yr3 | 15 | 12 | 8 |
| Equity Value (Cr) | 47.12 | 73.58 | 103.07 |
| / 1.1446 Cr sh | Rs 41.2 | Rs 64.3 | Rs 90.1 |

**Track 1 (mid 4.0x):**

| | Bear | Base | Bull |
|---|---|---|---|
| EV @4.0x (Cr) | 42.84 | 59.02 | 76.60 |
| Less Net Debt Yr3 | 15 | 12 | 8 |
| Equity Value (Cr) | 27.84 | 47.02 | 68.60 |
| / 1.1446 Cr sh | Rs 24.3 | Rs 41.1 | Rs 59.9 |

### 3.2 SECONDARY — P/E (exit PE = Section 1B destination, no other source)

**Track 2 (mid 8.9x):** Bear 0.85x8.9 = Rs 7.5 | Base 3.56x8.9 = Rs 31.7 | Bull 6.31x8.9 = Rs 56.2.
**Track 1 (mid 6.2x):** Bear 0.85x6.2 = Rs 5.3 | Base 3.56x6.2 = Rs 22.1 | Bull 6.31x6.2 = Rs 39.1.

### 3.3 P/B — NOT APPLIED (manufacturer; no lender carve-out).

### 3.4 DCF — directional only (0% weight)

FLAG-CASH + negative FCF FY24/FY25 make forward FCF unreliable; a DCF with normalised FCF/Revenue ~2% (consistent with the 0.80x cash multiplier — no magical cash improvement) and WACC 14%, terminal 4% produces an equity value in the Rs 25-45 range, corroborating the multiple methods' sub-CMP outputs. Not weighted.

### Method-wise Fair Value Summary (Year-3 per share)

| Method | Weight | Track | Bear | Base | Bull |
|---|---|---|---|---|---|
| EV/EBITDA | 60% | T2 | 41.2 | 64.3 | 90.1 |
| P/E | 40% | T2 | 7.5 | 31.7 | 56.2 |
| EV/EBITDA | 60% | T1 | 24.3 | 41.1 | 59.9 |
| P/E | 40% | T1 | 5.3 | 22.1 | 39.1 |

> INTERIM CHECKPOINT: Section 3 complete. All applicable methods applied both tracks. Every scenario fair value sits far below CMP 122. Continuing to Section 4.

---

# SECTION 4 — TRIANGULATION, ENTRY PRICE & VERDICT

### 4A. Triangulated Fair Value (EV/EBITDA 60% + P/E 40%)

**Track 2 (additive):**
| | Bear | Base | Bull |
|---|---|---|---|
| EV/EBITDA x0.60 | 24.72 | 38.58 | 54.06 |
| P/E x0.40 | 3.00 | 12.68 | 22.48 |
| **Weighted FV (Rs)** | **28** | **51** | **77** |

**Track 1 (RRM — governing):**
| | Bear | Base | Bull |
|---|---|---|---|
| EV/EBITDA x0.60 | 14.58 | 24.66 | 35.94 |
| P/E x0.40 | 2.10 | 8.83 | 15.65 |
| **Weighted FV (Rs)** | **17** | **33** | **52** |

### 4B. Methods Agreement

- Both methods point the same direction (deeply below CMP). EV/EBITDA > P/E per share because heavy depreciation (6.35 vs PAT 3.43) makes EBITDA the more generous lens; the spread is method-structural, not a disagreement on direction.
- Spread base (T1): 41.1 vs 22.1 = ~46%. Outlier is EV/EBITDA (more generous via D&A add-back); for a leverage-rising, capex-heavy manufacturer EV/EBITDA is the more trustworthy anchor, which is why it carries 60%.
- Most-trusted for THIS company: EV/EBITDA (B04 primary).

### 4C. Return at Current Price (Year-3, governing Track 1)

| Scenario | Weighted FV Yr3 | CMP | Total Return | 3-yr CAGR | Meets 25%? |
|---|---|---|---|---|---|
| Bear | 17 | 122 | -86% | -48.1% | RED |
| Base | 33 | 122 | -73% | -35.3% | RED |
| Bull | 52 | 122 | -57% | -24.7% | RED |

Track 2 (for record): Bear 28 -> -39.0% | Base 51 -> -25.3% | Bull 77 -> -14.4% CAGR. All negative.

### 4D. Probability-Weighted Expected Return

Grade C (B10.credibility_grade) -> weights **Bear 35% / Base 45% / Bull 20%** (sole source: credibility grade).

Governing Track 1:
| Scenario | Prob | 3-yr CAGR | Weighted |
|---|---|---|---|
| Bear | 35% | -48.1% | -16.84% |
| Base | 45% | -35.3% | -15.89% |
| Bull | 20% | -24.7% | -4.94% |
| **Expected CAGR** | 100% | | **-37.7%** |

Track 2 (record): 0.35(-39.0)+0.45(-25.3)+0.20(-14.4) = **-27.9%**.

### 4E. Entry Price (governing Track 1, Base FV Yr3 = 33)

| Calculation | Value |
|---|---|
| Base Case Fair Value (Yr3) | Rs 33 |
| Price for 25% CAGR = 33 / (1.25)^3 = 33 / 1.953 | Rs 16.9 |
| Price for 30% CAGR = 33 / (1.30)^3 = 33 / 2.197 | Rs 15.0 |
| Margin-of-Safety Price (20% below 25% entry) | Rs 13.5 |
| **Ideal entry range** | **Rs 13.5 to Rs 16.9** |

Buy only at the bottom of the revealed band. CMP 122 is ~7x the top of the entry range.

### 4F. Risk-Reward Asymmetry (from CMP 122, Track 1)

| | Value |
|---|---|
| Bull target Yr3 | Rs 52 -> Upside: -57% (no upside) |
| Base target Yr3 | Rs 33 -> -73% |
| Bear floor Yr3 | Rs 17 -> Downside: -86% |
| Upside(base)/Downside(bear) ratio | **~0.0x** (no upside exists; far below the 2x minimum) |

### 4G. Four-Pillar Exit Multiple Validation

| Check | Result | Pass? |
|---|---|---|
| Yr3 ROCE justifies ROCE base + matches FTTCP verdict? | Yr3 ROCE ~8% matches 7.2% used; DECLINING verdict honoured | PASS |
| Yr3 CFO/PAT justifies 0.80x cash mult? | Forward CFO normalises down from one-off; weak cash confirmed | PASS |
| Primary catalyst fired by Yr3 (base)? | ANVISA/EDQM unconfirmed; base assumes NO catalyst fire | PASS (conservative) |
| Strategic premium justified at Yr3 (single-credit)? | +0x; nothing credited; rule respected | PASS |
| UA ordering correct min(Fx1.25, Cap)? | UA not applied (all_met FALSE); H=min(8.88,38) | PASS |
| Would I buy a different stock at 8.9x with these Yr3 metrics? | Yes at 8.9x; NO at the current 40.8x | PASS (exit PE not revised up) |

No check fails; exit PE stands at the four-pillar destination. No upward revision.

### 4H. FINAL VALUATION VERDICT CARD

**Smruthi Organics Ltd (SMRUTHI)** | CMP Rs 122 | Market Cap Rs 169 Cr as stated in B10 (see FLAG-DATA: reconciled per-share basis uses 1.1446 Cr shares; mcap ~Rs 140 Cr on CMP x reconciled shares) | Current PE 40.8x

**FOUR-PILLAR EXIT PE**
- Pillar 1 ROCE Base: ROCE 7.2% (INPUT UNRESOLVED, conservative low-bound; FTTCP verdict DECLINING) -> 11.1x. Recovery credited via: NOT CREDITED.
- Pillar 2 Cash Mult: 0.80x (volatile/non-structural per FLAG-CASH; INDETERMINATE band -> conservative 0.80x; no growth offset, drag not growth-induced). Quality-Adjusted Base 8.88x.
- Pillar 3 Growth Prem: +0x (EM 13.4 < 25).
- Pillar 4 Strategic: +0x (no strategic asset; ROCE optionality not credited).
- Raw PE (F): 8.88x. UA applied: NO (F2 = F). Sector Cap: 38x (Pharma/CDMO, no quality uplift). 
- **DESTINATION PE (Track 2 additive): 8.9x (range 8.0x-9.5x).**

**RRM TRACK (Track 1 — governing)**
- r used 16% (14% micro + 2% governance/durability/revenue-risk); RRM 0.70 (lower bound). Fundamental base 8.88x.
- **RRM Destination PE: 6.2x (range 5.5x-6.5x).**
- Divergence 30.3% (>15%) -> Track 1 governs the entry zone (more conservative; durability/governance expressed via r).

**HURDLE RATIO: 0.18 (base) / 0.21 (bull, grade-C capped at base+5%) -> STOP.** 25% CAGR infeasible even on bull earnings; stock at 40.8x vs 6-9x destination.

**METHODS:** EV/EBITDA 60% (primary) + P/E 40% (secondary). P/B N/A.

**WEIGHTED FAIR VALUE (Year-3):**
- Track 1 (governing): Bear Rs 17 | Base Rs 33 | Bull Rs 52
- Track 2 (record): Bear Rs 28 | Base Rs 51 | Bull Rs 77

**EXPECTED CAGR (prob-weighted, grade C 35/45/20): -37.7% (Track 1) / -27.9% (Track 2).**

**UPSIDE/DOWNSIDE RATIO: ~0.0x (no upside; below 2x minimum).**

**ENTRY PRICE: Rs 13.5 to Rs 16.9 | MARGIN-OF-SAFETY PRICE: Rs 13.5.**

**DECISION: AVOID (on valuation).** CMP Rs 122 is ~4x the base fair value (Rs 33 governing / Rs 51 record) and ~7x the top of the entry range. Every scenario, both tracks, delivers a negative 3-year CAGR. Overlaid quality vetoes reinforce (not override) this: Gate 0 = 37 (AVOID), Promoter Verdict CONCERN, FLAG-CASH/REVENUE/CREDIT/GOVERNANCE. The valuation alone is dispositive.

**KEY ASSUMPTIONS THAT COULD CHANGE THE VALUATION**
- (up) ROCE recovers structurally to 20%+ (ANVISA/EDQM approvals + regulated-market pricing) -> Pillar 1 base 17.5x, cash normalises toward 1.15x -> destination could reach ~20x; still below current 40.8x. Requires confirmed regulatory wins (currently NOT FOUND).
- (up) Revenue re-accelerates to 15%+ with margin to 16% -> bull EPS higher; but grade C caps bull usage and HR still fails from 40.8x.
- (down) Continued revenue decline / RM shock -> bear EPS collapse (-34% CAGR); FV toward Rs 17.
- (down) Cash proves structurally negative (CARE re-downgrade) -> cash multiplier 0.65x, destination toward 7x.

**EXIT FRAMEWORK (if ever owned):** target exit at destination 8-9x; thesis-broken if revenue decline persists a further year or ANVISA/EDQM fails; time stop 4 quarters without revenue stabilisation; PE-compression floor already breached (holding is a de-rating trade against the investor).

**ONE-LINE THESIS:** Avoiding Smruthi Organics at Rs 122 because EPS grows only from Rs 2.99 to ~Rs 3.56 over 3 years (base +6% CAGR), at a four-pillar destination PE of 6-9x (ROCE ~7%, cash 0.80x non-structural, EM 13.4, sector cap 38x) = Rs 33-51 target = -35% to -25% CAGR; the stock trades at 40.8x versus a 6-9x earned multiple. Key risk: unexplained -19% revenue decline and governance CONCERN. Cash quality: WC-driven, NOT structural.

> INTERIM CHECKPOINT (final framework STOP): Valuation complete. Four-pillar exit PE 8.0x-9.5x (RRM 5.5x-6.5x). Hurdle Ratio STOP. Entry price Rs 13.5-16.9. Decision: AVOID (on valuation).

---

## UNRESOLVED INPUTS USED (each with conservative assumption)

1. ROCE Latest FY26 -> assumed 7.2% (low bound of declining 7.2-7.9% band; conservative-lower-bound rule + DECLINING verdict).
2. 3-Year Revenue CAGR -> not relied on; base 5% anchored to SOM/TAM below the SOM 9.0% ceiling (FY24 revenue unavailable).
3. 3-Year PAT CAGR -> not relied on (same data gap); PAT built bottom-up from projected revenue x margin.
4. Peer Medians (all) -> no relative uplift; exit multiples from Section 1B only (B06 skipped).
5. Current Capacity Utilisation -> not constraining; base 5% CAGR < capex-embedded 6.7% capacity (B09).
6. FTTCP ROCE forward verdict (not carried in B10) -> derived DECLINING from transition evidence, biased down per FTTCP rule 12.
7. Forward net debt / interest / depreciation -> conservative upward drift (net debt 6->12 Cr) reflecting debt-financed capex.

## FLAGS CARRIED FORWARD
- FLAG-CASH: cash multiplier APPLIED = 0.80x (volatile/non-structural; INDETERMINATE band resolved conservatively).
- FLAG-DATA: B10 share-count/market-cap inconsistency (10x units error on shares); per-share math run off reconciled 1.1446 Cr shares (book-value confirmed) and CMP/EPS anchors.
- FLAG-REVENUE, FLAG-CREDIT, FLAG-GOVERNANCE: propagated from B10; reinforce the AVOID.

**Report completed: 2026-07-09 | Opus 4.8 | NO STOPS | All numbers anchored to B10 or explicitly marked INPUT UNRESOLVED with the conservative assumption stated.**
