# B11 — ROLE 1 MULTI-MODAL VALUATION

**Company:** Gaudium IVF and Women Health Ltd (GAUDIUMIVF)
**Run date:** 2026-07-16 | **Model:** claude-opus-4-8
**Frameworks:** Master v3.3 (Role 1) / Section 1B v3.3 Amendments / FTTCP v1.2
**Valuation basis (operator override, Override 3):** ONE-YEAR-FORWARD earnings multiples. Current multiple on FY27E EPS; exit priced at the FY29 exit on the year-ahead (FY30E) EPS. Three-year hold FY27→FY30.

All inputs sourced solely from B10-valinputs.yaml. FTTCP forward verdicts and operator overrides from fttcp-deliberation.md (authoritative, phase-3). Nothing pulled from general knowledge.

---

## 0. INPUT ANCHORS (carried from B10, first use)

| Field | Value | Anchor |
|---|---|---|
| CMP | Rs 137.00 | B10 company_identity.cmp_rs |
| Shares (diluted) | 7.28 Cr | B10 shares_outstanding_diluted_cr |
| Market cap | Rs 997.04 Cr | B10 market_cap_cr |
| FY26 consol PAT | Rs 24.49 Cr | B10 latest_financials.pat_cr |
| FY26 diluted EPS | Rs 3.37 | B10 diluted_eps_rs |
| FY26 revenue | Rs 104.36 Cr | B10 revenue_cr |
| FY26 EBITDA / margin | Rs 37.70 Cr / 36.13% | B10 ebitda_cr / ebitda_margin_pct |
| Total debt | Rs 24.57 Cr | B10 total_debt_cr |
| Surplus cash | Rs 81.00 Cr | B10 surplus_cash_cr |
| Net debt | Rs 15.78 Cr | B10 net_debt_cr |
| Operating ROCE (ex surplus cash) | 37.0% | B10 roce_latest_pct (operator standing rule) |
| Cash multiplier | 0.80x | B10 cash_multiplier / deliberation p.19 |
| CFO/PAT FY26 | 0.30x (0.33 reported ratio) | B10 cfo_pat_ratio_fy26 |
| EM score | 13 (MODEST) | B10 em_score |
| Credibility grade | C (Mixed) | B10 credibility_grade |
| Sector cap | 35x Hospitals/dialysis/healthcare | B10 sector_cap_row (corrected from manifest) |
| SOM-implied rev CAGR 3yr | 31.4% | B10 som_implied_revenue_cagr_3yr_pct |
| UA qualifiers all met | FALSE | B10 ua_qualifiers.all_met |

**INPUT UNRESOLVED — forward margin guidance (B10 margin_guidance NOT FOUND).** Conservative assumption used: hold FY26 consolidated EBITDA margin 36.13% flat across the projection (no expansion credited), because the framework's bear/base margin rules bar assuming unprecedented expansion without evidence.
**INPUT UNRESOLVED — peer financial medians (B10 peer_financial_medians NOT FOUND).** Conservative assumption: no relative-multiple method is run; the four-pillar destination PE is the sole exit-multiple authority (Section 1B v3.3, per NEVER rule).
**INPUT UNRESOLVED — 3yr revenue/PAT CAGR (B10 NOT FOUND).** Base EPS CAGR set per deliberation at 25%, cross-checked below against the SOM-implied 31.4% and the FY25→FY26 prints (rev +47.6%, PAT +27.8%).

---

## SECTION 1A — METHOD SELECTION

Asset-light single-specialty healthcare-services chain (IVF 64% / pharmacy trading 31% / hospital 4%), profitable, positive equity, premium operating ROCE. Not a lender.

| Method | Role | Weight | Rationale |
|---|---|---|---|
| **P/E (one-year-forward)** | PRIMARY | 80% | Operator basis (Override 3); Section 1B destination PE is the sole exit authority; clean positive EPS |
| **EV/EBITDA** | SECONDARY | 20% | Cross-check on the PE anchor; asset-light, low leverage |
| P/B | Not used | — | Not a lender/financial; ROE 16% not the driver |
| DCF | Not used | — | Cash conversion INDETERMINATE (0.80x) makes FCF projection unreliable; would require assuming a cash fix that has not printed |
| SOTP cash add-back | Framing note | — | Surplus cash treated per Section 1B worksheet note below (NOT added at Year-3 exit — see double-count guard) |

**Surplus-cash / SOTP double-count guard.** Operating ROCE is measured at 37% by removing the ~Rs 81 Cr idle IPO deposits from the denominator (deliberation Override 1). That surplus cash is the documented capex earmark for the hub build-out (7→26 hubs) that drives the forward EPS ladder. By the FY29 exit the cash is deployed into earning hubs and is therefore captured inside FY30E EPS. Adding it again as idle cash at exit would double-credit one asset. It is valued separately only in the *entry-basis* framing (to keep ROCE honest); the Year-3 target = destination PE × FY30E EPS with **no separate cash add-back**. This reproduces the deliberation's base exit of Rs 181 (not Rs 192). One asset, one mechanism.

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE WORKSHEET (Track 2, additive)

### Pillar 1 — ROCE Base
- FTTCP ROCE forward verdict (sole authority): **SUSTAINED premium** (deliberation p.20, phase-3 handoff).
- ROCE used: **37.0% current operating ROCE, surplus cash removed** (Override 1). NOT reported 20.11%, NOT a normalized-recovery blend. Amendment 4.5 does NOT apply (verdict is SUSTAINED, not TEMPORARILY DEPRESSED + RECOVERING).
- Continuous formula (Amendment 5): 0.5 × 37 + 7.5 = 26.0x, **capped at 24x**.
- **ROCE Base PE = 24.0x.**
- **ROCE recovery credited via: Pillar 1.** The Strategic Premium ROCE re-rating option is BARRED (single-credit rule, Amendment 4 / FTTCP Pillar-1 integration).

### Pillar 2 — Cash Conversion Multiplier
- Determination from B10: **INDETERMINATE (deteriorating)**, CFO/PAT 0.30x FY26, receivable days ~187 (B10 cash_conversion_determination).
- Per wrapper rule, INDETERMINATE takes the more conservative multiplier: **0.80x** (deliberation p.19).
- No growth offset (INDETERMINATE never resolves to a clean pass).
- **Cash Multiplier (effective) = 0.80x.**

### Pillar 3 — Growth (decoupled, v3.4), hard cap +6x
- **3a Growth Visibility Premium: +2x.** Qualifies on two documented (📄) tests: (i) IPO proceeds earmarked to take hubs 7→26 (capex-embedded growth 335%, B10 capex_embedded_growth_pct); (ii) SOM-implied revenue CAGR 31.4% (>20%) with the 3-yr capacity check passing (B10 capacity_check_3yr "fits within 75% utilization"). Grade C caps 3a at +2x.
- **3b Moat Formation Premium: +0x** (EM 13, below the 25 threshold; B10 em_score).
- **3c Duration Premium: +0x** (no executable order book / contracted revenue).
- **Pillar 3 total = +2x.**

### Strategic Asset Premium
- **+1x.** Founder-clinician brand + ART-Act licensing barrier + premium clinic pricing (deliberation p.46). Below the +2 to +4x franchise band because competition is not limited and the company is a small player. Not a monopoly.
- ROCE re-rating optionality NOT credited here (barred by single-credit; ROCE sits in Pillar 1).

### Four-Pillar Summary

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | 0.5 × 37% + 7.5 = 26, capped 24 | 24.0x |
| B. Cash Multiplier (effective) | 0.80x, no offset (INDETERMINATE) | 0.80x |
| C. Quality-Adjusted Base | 24.0 × 0.80 | 19.2x |
| D. Growth Visibility Premium | 3a +2 / 3b +0 / 3c +0 | +2.0x |
| E. Strategic Premium | founder brand + ART licence | +1.0x |
| F. Raw Destination PE | 19.2 + 2 + 1 | 22.2x |
| F2. UA-Adjusted Raw PE | UA NOT applied (all_met=false) → F | 22.2x |
| G. Sector Cap | Hospitals/healthcare, no quality uplift | 35.0x |
| **H. Final Destination PE** | **min(22.2, 35)** | **22.2x → 22x** |

**Destination PE Range: 22.2 ±7.5% = 20.5x to 24.0x** (Amendment 6; 20.535 and 23.865 rounded to nearest 0.5x). Mid **22x**. Sector cap 35x NOT binding.

**UA multiplier NOT applied:** listed <12 months (~5 months), FII+DII ~5.23% (>3%); qualifiers fail (B10 ua_qualifiers.all_met=false). Amendment 3 ordering therefore never engages.

**ROCE recovery credited via: Pillar 1.**
**SHARED CATALYST flag: TRUE** — deploying the IPO cash into hubs drives BOTH the Pillar 3a growth premium AND the Pillar 1 operating ROCE, and the receivables book sits across cash conversion, ROCE and the growth-funding model at once. Role 3 must stress-test this single point of failure (deliberation p.28, phase-3 handoff).

---

## SECTION 1B (cont.) — RRM DUAL-TRACK (Track 1)

- Base r (small/micro): 14%. Adjusted **UP to 16%** for promoter CONCERN + INDETERMINATE cash + <1yr listed history (deliberation). Bounded within [9%, 18%]. ✓
- **RRM = 1 + (13.5 − 16) × 0.12 = 1 + (−2.5)(0.12) = 1 − 0.30 = 0.70** (percentage-point reading, Amendment 4.4; floored at the ×0.70 lower bound).
- Fundamental Base PE for RRM = the quality-adjusted fundamental base **19.2x** (ROCE 24x × cash 0.80x — durability/governance are priced through r, not through additive premiums, per the RRM philosophy).
- **RRM-track Destination PE = 19.2 × 0.70 = 13.4x → 13.5x** (range ±7.5% = 12.5x to 14.5x). Consistent with the deliberation's "conservative floor near 14x at r 16%."

**Track divergence.** Track 2 destination 22x vs Track 1 13.5x → divergence 38.6% (>15%). Under the default rule the more conservative track (RRM) sets the entry zone. **Operator override (deliberation p.74): the additive track carries the decision** — the four-pillar destination correctly prices a documented high-growth business, and the RRM floor is retained as a conservative sanity reference, not the governing number. This is an explicit, recorded override of the default "conservative track governs" rule. Governing track = **Track 2 (additive)**.

---

## SECTION 1B (cont.) — HURDLE RATIO (Tier A, 25%)

**Tier: A | Hurdle: 25%** (default sleeve; Tier B fails — screen AVERAGE and promoter CONCERN break Tier B's quality gates, Amendment 4.3).

- Current PE (one-year-forward, FY27E EPS): 137 / 4.2125 = **32.5x** (trailing = 137/3.37 = 40.7x).
- Destination PE mid: 22x.
- **HR = (1 + EPS CAGR)³ × (22 ÷ 32.5)**, pass threshold 1.953.

| Row | EPS CAGR | (1+g)³ | × (22/32.5) | HR | Result |
|---|---|---|---|---|---|
| Base | 25% | 1.9531 | 0.6765 | **1.32** | FAIL |
| Bull (C-grade cap: base+5% = 30%) | 30% | 2.1970 | 0.6765 | **1.49** | FAIL |

Bull EPS CAGR is capped at Base + 5% = 30% because credibility grade is C (not A/B). Both rows fail 1.953.

**HURDLE RATIO VERDICT: STOP.** A 25% CAGR is infeasible at CMP even on bull-case earnings, because entry is at ~32.5x forward against a 22x destination (de-rating headwind). At current price this is AVOID-on-valuation; the reachable entry zone below keeps the name on the watchlist rather than a hard avoid.

*Interim checkpoint (framework STOP point):* Section 1 complete. Destination PE 20.5-24x (RRM 12.5-14.5x). Current forward PE 32.5x. Hurdle Ratio STOP. Continuing to Section 2.

---

## SECTION 2 — PROJECTIONS (one-year-forward basis)

### 2A/2B assumptions

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| EPS CAGR | 15% | 25% | 30% (C-cap = base+5%) |
| Growth logic | Hub delays + receivables drag; 1-2 triggers fail | IPO-funded hubs ramp; SOM headroom 28x | Hubs + AI-embryology + international spokes all fire |
| EBITDA margin | 34% (−200bps) | 36% (hold FY26) | 38% (mix toward IVF core) |
| Dilution | nil assumed | nil | nil |

Margin held flat/conservative because forward margin guidance is NOT FOUND (unresolved-input rule).

### 2C — EPS ladder (Rs, diluted), from FY26 Rs 3.37

| FY | Bear (15%) | Base (25%) | Bull (30%) |
|---|---|---|---|
| FY26 (actual) | 3.37 | 3.37 | 3.37 |
| FY27 | 3.88 | 4.21 | 4.38 |
| FY28 | 4.46 | 5.27 | 5.70 |
| FY29 | 5.13 | 6.58 | 7.40 |
| **FY30 (exit-year, year-ahead)** | **5.89** | **8.23** | **9.63** |

Base revenue (illustrative, 25% ≈ EPS CAGR at flat margin/nil dilution): FY26 104.36 → FY30 ~254.8 Cr; base FY30 EBITDA ~91.7 Cr at 36%.

### 2D — Sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | Base 25% < SOM-implied 31.4%; 3yr capacity fits within 75% util | ✓ |
| Margins require something unprecedented? | Base holds FY26 36.13%; no expansion credited | ✓ |
| ROCE stays above 15%? | Operating ROCE ~37% SUSTAINED; well above | ✓ |
| FCF funds growth without excessive new debt? | Hubs funded by the Rs 81 Cr IPO earmark, not new debt | ✓ |
| EPS growth operational, not financial engineering? | Driven by hub volume + core IVF pricing | ✓ |
| Implied market-share gain realistic? | 3.52% → mid-single-digit SAM share; STRONG runway (28.4x headroom) | ✓ |
| CFO/PAT trajectory consistent with Pillar 2 (0.80x)? | Base does NOT assume a cash fix; 0.80x conservatism preserved | ✓ |
| **Year-3 ROCE consistent with FTTCP verdict used in Pillar 1?** | Yes — SUSTAINED premium ~37% operating holds as hubs deploy and earn | ✓ |

*Interim checkpoint:* Section 2 complete. Continuing to Section 3.

---

## SECTION 3 — METHODS APPLIED

### PRIMARY — P/E (one-year-forward)

Exit priced at FY29 on the year-ahead FY30E EPS × destination PE.

| Source | Exit PE |
|---|---|
| Four-Pillar Destination PE | 20.5x – 24.0x |
| RRM-track Destination PE | 12.5x – 14.5x |
| Sector Cap | 35x |
| **Applied Exit PE (Track 2, governing)** | **20.5x (bear) / 22x (base) / 24x (bull)** |

**Target price matrix (Year-3 = FY29 exit, on FY30E EPS), Track 2:**

| | Exit 20.5x | Exit 22x | Exit 24x |
|---|---|---|---|
| Bear EPS 5.89 | 🔴 Rs 121 | Rs 130 | Rs 141 |
| Base EPS 8.23 | Rs 169 | 🟡 **Rs 181** | Rs 197 |
| Bull EPS 9.63 | Rs 197 | Rs 212 | 🟢 **Rs 231** |

CAGR colour vs CMP 137 over 3 years: 🟢 ≥25% | 🟡 15-25% | 🔴 <15%.
- Base @ 22x = Rs 181 → +32.1% total / **+9.7% CAGR** (🔴 below 25%).
- Bull @ 24x = Rs 231 → +68.6% total / **+19.0% CAGR** (🟡).
- Bear @ 20.5x = Rs 121 → −11.8% / **−4.1% CAGR** (🔴).

Reverse-engineered entry (base, 22x): Year-3 target Rs 181 ÷ 1.953 = **Rs 92.7**.

**P/E Method Fair Value (Year-3): Rs 121 (bear) / Rs 181 (base) / Rs 231 (bull).**

### SECONDARY — EV/EBITDA (cross-check)

Destination EV/EBITDA ≈ 0.65 × 22 = ~14.5x. Base FY30E EBITDA ~91.7 Cr → EV ~1,330 Cr; less net debt ~15.8 Cr = equity ~1,314 Cr ÷ 7.28 Cr = **Rs 180**. Agrees with the PE base (Rs 181), no outlier.

### Method-wise summary

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E forward (primary) | 80% | 121 | 181 | 231 |
| EV/EBITDA (secondary) | 20% | ~120 | ~180 | ~229 |
| **Weighted** | 100% | **~121** | **~181** | **~231** |

*Interim checkpoint:* Section 3 complete. Continuing to Section 4.

---

## SECTION 4 — TRIANGULATION, ENTRY, VERDICT

### 4A. Triangulated Fair Value (Year-3), both tracks

| | Bear | Base | Bull |
|---|---|---|---|
| **Track 2 (additive) — governing** | Rs 121 | **Rs 181** | Rs 231 |
| Track 1 (RRM floor) | Rs 74 | Rs 111 | Rs 140 |

RRM: bear 12.5 × 5.89 = 74; base 13.5 × 8.23 = 111; bull 14.5 × 9.63 = 140.

### 4B. Agreement
PE and EV/EBITDA agree within ~1% on base. Track1 vs Track2 diverge 38.6%; RRM is the conservative floor, additive governs per operator endorsement.

### 4C. Return at CMP (Rs 137)

| Scenario | Year-3 FV | Total Return | CAGR | Meets 25%? |
|---|---|---|---|---|
| Bear | 121 | −11.8% | −4.1% | 🔴 |
| Base | 181 | +32.1% | +9.7% | 🔴 |
| Bull | 231 | +68.6% | +19.0% | 🔴 |

### 4D. Probability-weighted expected return
Credibility grade C (Mixed) → **Bear 35% / Base 45% / Bull 20%**.

| Scenario | Prob | 3yr CAGR | Weighted |
|---|---|---|---|
| Bear | 35% | −4.1% | −1.44% |
| Base | 45% | +9.7% | +4.38% |
| Bull | 20% | +19.0% | +3.80% |
| **Expected CAGR** | 100% | | **+6.7%** |

### 4E. Entry price (Tier A divisor 1.953)

| Calculation | Value |
|---|---|
| Base FV (Year-3, Track 2) | Rs 181 |
| Entry for 25% CAGR = 181 ÷ 1.953 | Rs 92.7 |
| Entry for 30% CAGR = 181 ÷ 2.197 | Rs 82.4 |
| **Ideal entry range** | **Rs 90 – Rs 93** |
| MoS price (20% below the 25% entry) | Rs 74 |

Rs 93 is the mechanical 25%-CAGR entry off base FV Rs 181; Rs 90 is a modest lower buffer within the zone. MoS Rs 74 = 0.80 × 92.7. Entry zone is ~15% above the Rs 79 IPO price and ~32% below CMP — a reachable watchlist level on a normal drawdown, not a market-unlikely zone (deliberation p.64).

### 4F. Risk-reward asymmetry

| | Value |
|---|---|
| Bull target | Rs 231 → +68.6% |
| Base target | Rs 181 → +32.1% |
| Bear floor | Rs 121 → −11.8% |
| **Upside(base) / Downside(bear)** | +44 / −16 = **2.7x** (≥2x ✓) |

### 4G. Four-Pillar exit-multiple validation

| Check | Result | Pass? |
|---|---|---|
| Year-3 ROCE justifies 24x ROCE base (matches FTTCP SUSTAINED)? | ~37% operating sustained | ✓ |
| Year-3 CFO/PAT justifies 0.80x cash mult? | Base holds INDETERMINATE, no fix assumed | ✓ |
| Primary catalyst (hub openings) fired by Year-3 base? | 19-hub build-out underway by FY29 | ✓ |
| Strategic premium still justified, single-credit respected? | +1x brand/licence; ROCE re-rating barred | ✓ |
| UA ordering correct — min(F×1.25, Cap)? | UA not applied; H=min(22.2,35) | ✓ |
| Would you buy another stock at 22x with these Year-3 metrics? | Yes for the quality; but not at 32.5x entry | ✓ |

### 4H. VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP:** Rs 137 | **Market cap:** Rs 997 Cr
- **FOUR-PILLAR EXIT PE:** ROCE Base 24.0x (FTTCP SUSTAINED premium; ROCE used 37% operating, surplus cash removed) × Cash Mult 0.80x (INDETERMINATE, no offset) = Quality Base 19.2x; + Growth 3a +2x (EM 13, SOM 31.4% + capex earmark, 📄) + 3b/3c +0x; + Strategic +1x (founder brand + ART licence, single-credit — ROCE re-rating barred); Raw 22.2x; UA applied N; Sector Cap 35x (not binding, no uplift); **DESTINATION PE 20.5x – 24x (mid 22x)**.
- **RRM TRACK:** r 16%, RRM 0.70; RRM destination 12.5x – 14.5x (mid 13.5x); RRM fair values Rs 74 / 111 / 140.
- **HURDLE RATIO:** Base 1.32, Bull 1.49 (both < 1.953) → **STOP** (25% infeasible at CMP even on bull earnings; de-rating headwind 32.5x→22x).
- **METHODS:** P/E forward (80%) + EV/EBITDA (20%).
- **WEIGHTED FAIR VALUE (Year-3):** Track 2 Bear Rs 121 / Base Rs 181 / Bull Rs 231; Track 1 (RRM) Rs 74 / 111 / 140.
- **EXPECTED CAGR (prob-weighted, grade C 35/45/20):** +6.7%.
- **UPSIDE/DOWNSIDE:** 2.7x.
- **ENTRY RANGE:** Rs 90 – Rs 93 | **MARGIN OF SAFETY:** Rs 74.
- **DECISION: WATCHLIST (on-valuation).** Business quality and growth are real; the price is the problem. Not a buy at CMP (Hurdle STOP). Buy only in the Rs 90-93 zone. Two catalysts would turn it toward a buy nearer CMP: the cash multiplier earning 1.0x once receivable days turn, and a B credibility grade once two quarters print.
- **KEY ASSUMPTIONS THAT COULD CHANGE VALUATION:** ▲ cash multiplier 0.80x→1.0x (receivable days revert) lifts quality base 19.2x→24x and destination toward ~27x; ▲ credibility C→B uncaps growth premium and lifts bull EPS in the Hurdle; ▼ hub-opening delay (zero capex utilised as of 31-Mar-FY26) cuts base EPS CAGR below 25%; ▼ promoter CONCERN / Rs 49.75 Cr contingent tax crystallising.
- **EXIT FRAMEWORK:** target exit at destination 22x on year-ahead EPS; thesis broken if Q1/Q2 FY27 receivable days stay >180 with no hub openings; time stop 8 quarters if EPS CAGR runs <15%; PE compression floor RRM ~13.5x.
- **ONE-LINE THESIS:** Buying GAUDIUMIVF at Rs 90-93 (not Rs 137) because EPS grows from Rs 3.37 to ~Rs 8.2 (FY30E) over the hold driven by a 7→26 hub build-out funded by the IPO cash, at a four-pillar destination PE of 22x (ROCE 37% operating, cash 0.80x, EM 13, sector cap 35x) = Rs 181 target = ~25% CAGR from entry. Key risk: cash conversion INDETERMINATE and promoter CONCERN (shared receivables/hub catalyst). Cash quality: INDETERMINATE (deteriorating).

**ROCE recovery credited via: Pillar 1.**
**SHARED CATALYST flag: TRUE** (IPO-cash hub deployment drives Pillar 1 ROCE and Pillar 3a growth; receivables book straddles cash/ROCE/growth-funding — Role 3 stress-test the single point of failure).

*Valuation complete. Four-pillar exit PE 20.5x–24x (RRM 12.5x–14.5x). Hurdle Ratio STOP. Entry Rs 90-93. Decision: WATCHLIST (on-valuation).*

---

## RECONCILIATION WITH DELIBERATION PREVIEW

Deliberation preview: destination ~22x, WATCHLIST at CMP, Hurdle STOP on base and bull, entry Rs 90-93, MoS Rs 74, 3yr base return from CMP ~10%. **Formal recompute CONFIRMS all six.** Base exit Rs 181 (22 × FY30E 8.23), base 3yr return +9.7% (~10%), Hurdle Base 1.32 / Bull 1.49 (STOP), entry Rs 92.7 (zone 90-93), MoS Rs 74. No divergence.

```yaml
stage: B11-valuation
company: "GAUDIUMIVF"
run_date: "2026-07-16"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Forward margin guidance NOT FOUND — held FY26 EBITDA margin 36.13% flat"
  - "Peer financial medians NOT FOUND — no relative-multiple method; four-pillar PE sole authority"
  - "3yr revenue/PAT CAGR NOT FOUND — base EPS CAGR set at 25% per deliberation, SOM cross-checked"
  - "Rating agency WC/cash quote NOT FOUND — cash multiplier held conservative at 0.80x"
flags:
  - "FLAG-CASH: INDETERMINATE (deteriorating), cash multiplier 0.80x applied, no growth offset"
  - "FLAG-PROMOTER: CONCERN — Rs 49.75 Cr contingent tax (~85% net worth), RPTs, ID exits"
  - "SHARED CATALYST: IPO-cash hub deployment drives Pillar 1 ROCE and Pillar 3a growth; receivables book straddles cash/ROCE/growth-funding"
  - "CREDIBILITY-C: bull EPS CAGR capped at base+5% (30%) in Hurdle; growth premium 3a capped +2x"
  - "UA NOT applied: listed <12m, FII+DII ~5.23% (>3%)"
  - "GOVERNING-TRACK OVERRIDE: additive governs over more-conservative RRM per operator endorsement (deliberation p.74)"
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 12.5, mid: 13.5, high: 14.5, r_used: 16, rrm: 0.70}
  track2_additive: {low: 20.5, mid: 22.0, high: 24.0}
  divergence_pct: 38.6
  governing_track: "Track 2 additive — operator-endorsed; RRM retained as conservative floor (overrides default conservative-track rule)"
pillar_detail:
  roce_used: 37.0
  roce_base: 24.0
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 0.80
  structural_or_growth: "INDETERMINATE (deteriorating) — conservative 0.80x, no offset"
  growth_offset: 0
  growth_premium: 2
  strategic_premium: 1
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 35
hurdle_ratio: {base: 1.32, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 74, base: 111, bull: 140}
  track2: {bear: 121, base: 181, bull: 231}
expected_cagr_prob_weighted: 6.7
entry_range: {low: 90, high: 93}
mos_price: 74
upside_downside_ratio: 2.7
decision: "WATCHLIST (on-valuation) — not a buy at CMP (Hurdle STOP); buy only Rs 90-93"
unresolved_inputs_used:
  - "Forward margin guidance NOT FOUND → held FY26 EBITDA margin 36.13% flat (no expansion credited), per bear/base margin rule"
  - "Peer medians NOT FOUND → no relative-multiple method; four-pillar destination PE is sole exit authority"
  - "3yr CAGR NOT FOUND → base EPS CAGR 25% (deliberation), below SOM-implied 31.4%; conservative"
som_cagr_crosscheck: "consistent — base 25% below SOM-implied 31.4% (3yr), capacity check passes"
one_line_thesis: "Buying GAUDIUMIVF at Rs 90-93 (not Rs 137) because IPO-funded 7-to-26 hub build-out grows EPS Rs 3.37 to ~Rs 8.2 (FY30E) at a 22x four-pillar destination PE (ROCE 37% operating, cash 0.80x, EM 13, cap 35x) = Rs 181 target; Hurdle STOP at CMP, WATCHLIST; key risk cash INDETERMINATE + promoter CONCERN (shared catalyst)."
```
