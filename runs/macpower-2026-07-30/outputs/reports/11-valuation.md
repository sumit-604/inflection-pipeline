# STAGE 11: ROLE 1 MULTI-METHOD VALUATION

**Company:** Macpower CNC Machines Limited (MACPOWER) | **Run Date:** 2026-07-30
**Model:** claude-opus-4-8 | **Frameworks:** Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2
**Input source:** B10-valinputs (sole input table) + OPERATOR-APPROVED VALUATION PILLARS block

> PIPELINE MODE: all sections executed in one pass. Framework STOP gates are written as checkpoint lines, then continued. Every number carries a B10 anchor on first use. Conservative bias throughout. Missing numbers are NOT FOUND, never estimated.

---

## SECTION 1A: METHOD SELECTION

MACPOWER is a capital-goods manufacturer of CNC machine tools (B04): medium asset intensity, HIGH working-capital intensity, moderate pricing power, cyclical (customer capex-cycle dependent). Earnings are real but cash-conversion is INDETERMINATE (CFO/PAT 0.41x FY26; B10). This profile makes an earnings multiple appropriate as the primary lens (the Section 1B four-pillar destination PE is a P/E-based construct), with EV/EBITDA as the capital-intensity cross-check and P/B as a tertiary floor check.

| Role | Method | Weight | Justification |
|------|--------|--------|---------------|
| PRIMARY | P/E via Section 1B Four-Pillar destination PE | 60% | Profitable, promoter-run manufacturer with clean-enough PAT; exit multiple is EARNED via the four pillars, not assumed. Operator approved a one-year-forward P/E basis at the FTTCP gate. |
| SECONDARY | EV/EBITDA | 30% | Standard for capital-intensive, varying-leverage manufacturers (B04 names it primary sector method). Used here as the capital-intensity cross-check on the PE destination. |
| TERTIARY | P/B | 10% | Asset-heavy cyclical; a floor/sanity check only (BVPS FY25 Rs 142.77, B10). Not decisive for an earnings-driven grower. |

DCF is rejected: high-growth + INDETERMINATE cash conversion make terminal value dominant and unreliable (framework caveat). NAV/SOTP/sector-specific not applicable.

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 (with v3.5.1 normalization guard)

All pillar determinations are carried verbatim from the OPERATOR-APPROVED VALUATION PILLARS block on B10 (deliberation record, authoritative). They are applied, not re-litigated.

### Pillar 1 — ROCE Base Multiple (continuous formula, v3.3 Amendment 5)

- FTTCP ROCE forward verdict: **STAGNANT** (B10 flags; deliberation p.23) -> Pillar 1 uses **CURRENT ROCE**.
- ROCE used: **23.75%** (AR Note 38(vi), FY25 audited capital-employed basis; B10 roce_fy25_pct).
- **Pillar 1 normalization route (v3.5.1 consolidated Amendment 9): NONE.**
  - Route A (operational ROCE / denominator fix) FAILS the 20% idle-capital test: CWIP ~Rs 4.86 cr plus near-zero net cash (net cash -Rs 0.28 cr, B10) is far below 20% of capital employed.
  - Route B (pre-cycle normalized ROCE / numerator fix) is BARRED: neither route may be invoked on a STAGNANT verdict (v3.5.1 interaction rule). Amendment 4.5 standalone is retired and not applied.
- Base PE = 0.5 x 23.75 + 7.5 = 11.875 + 7.5 = **19.375x -> 19.4x** (floor 9x, cap 24x; not binding).
- **ROCE recovery credited via: NOT CREDITED** (STAGNANT; single-credit rule leaves Strategic Premium ROCE re-rating barred as well).

> NOTE (ROCE reconciliation, phase-3 dependency): B10 carries an unreconciled higher basis — screener ROCE 29.1% vs AR Note 38 23.75% (conflicts[]; capital-employed definition difference, likely lease-liability treatment). The deliberation fixed Pillar 1 on the AR Note 38 23.75%. If the screener 29.1% were used instead: Pillar 1 = 0.5 x 29.1 + 7.5 = 22.05x; Raw = 22.05 + 2 = 24.05x; x1.25 UA = 30.06x; min(30.06, 25 cap) = **25.0x — identical**. The destination is cap-bound either way, so the reconciliation does not move the ceiling. Stated as a NOTE per instruction.

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT (FY24-26): 0.4538x (B10; below 0.50x) | Latest FY26 CFO/PAT: 0.41x (B10) | FCF positive but thin (FCF/PAT 0.090x, B10).
- Determination: **INDETERMINATE** (operator-confirmed; deliberation p.71). Trajectory 0.70x (FY24) -> 0.27x (FY25) -> 0.41x (FY26) is non-monotonic; structural-vs-growth cannot be cleanly resolved and the rating PDF is NOT PROVIDED (B10).
- Per wrapper rule, INDETERMINATE takes the more conservative treatment and no clean pass above neutral: **effective cash multiplier = 1.00x (provisional); downside 0.80x** if the next print confirms structural deterioration.
- **Quality-Adjusted Base = 19.375 x 1.00 = 19.375x -> 19.4x.**
- FLAG-CASH carried forward. Receivables deteriorating: >6mo ageing 15.4% from 12.2%, net receivables +57.5% YoY vs revenue +8.6% (B10 flags; B02 Finding #1).

### Pillar 3 — Growth Visibility Premium (decoupled, v3.4 Amendments 4.1/4.2)

- 3a Growth Visibility: **+2x** — order book ~1.37x FY26 revenue (Rs 456 cr / Rs 333.18 cr, B10), capex-embedded growth ~70% (B07), management delivery grade B. Two documented qualifiers -> +2x (grade B, not A, so no +3x uplift).
- 3b Moat Formation: **+0x** — EM score 15.0 < 25 (B10 em_score; MODEST).
- 3c Duration: **+0x** — executable order book <2.5x annual revenue tenor.
- **Pillar 3 total = +2x** (within the +6x combined cap).

### Strategic Asset Premium

- **+0x.** No rare licence/regulatory monopoly; no documented pricing power (moderate pricing, B04); ROCE re-rating optionality is barred (recovery not credited, STAGNANT; single-credit rule). B10 strategic_premium_x 0.0.

### Undiscovered Alpha Multiplier — APPLIES x1.25

All three qualifiers hold (B10 ua_qualifiers.all_met = true):
1. Listed >=12 months — listed 2018, NSE main board 2020 (B08).
2. Gate 0 >=60 OR EM >=25 — Gate 0 core score 67 (B10 gate0_core_score).
3. FII+DII <3% — 0.96% Jun-2026 (B08).

Applied to the RAW destination PE BEFORE the sector cap (Amendment 3 order).

### Sector Reality Cap

**25x — Cables / Industrial products (ABSOLUTE).** Corrected from the manifest's erroneous Pharma/CDMO 38x (B10 flag; deliberation p.15). The 38x is NOT used anywhere.

### Four-Pillar Summary (Track 2 — Additive)

| Step | Calculation | Value |
|------|-------------|-------|
| A. ROCE Base | 23.75% -> 0.5 x 23.75 + 7.5 | 19.375x |
| B. Cash Multiplier (effective) | 1.00x (INDETERMINATE, provisional) | 1.00x |
| C. Quality-Adjusted Base | 19.375 x 1.00 | 19.375x |
| D. Growth Visibility Premium | 3a +2 / 3b +0 / 3c +0 | +2x |
| E. Strategic Premium | none | +0x |
| F. Raw Destination PE | 19.375 + 2 + 0 | 21.375x (21.4x) |
| F2. UA-Adjusted Raw PE | 21.375 x 1.25 | 26.72x (~26.75x) |
| G. Sector Cap (absolute) | Cables / Industrial products | 25.0x |
| **H. Final Destination PE** | **min(26.72, 25.0)** | **25.0x** |

**Track 2 Destination PE (additive) = 25.0x**, cap-bound. Range H ±7.5% = 23.1 to 26.9, upper capped -> **23.0x to 25.0x, mid 25.0x**.

This reconciles exactly to the OPERATOR-APPROVED DESTINATION PE = 25.0x. Additive raw (19.4 x 1.00) + 2 = 21.4x, x1.25 UA = 26.75x, min(26.75, 25) = 25.0x.

### RRM Dual-Track Derivation (Track 1) — computed independently

- Fundamental Base PE = quality-adjusted base = 19.375x (Pillar 1 x cash multiplier; the RRM track replaces the additive premiums and UA with a durability/governance-driven discount rate, not additive points).
- Base r for small/micro = 14%. Adjustment: +0.75% for a cyclical capital-goods name carrying INDETERMINATE / deteriorating cash conversion (FLAG-CASH) and credibility grade B, partly offset by a TRUSTWORTHY promoter (73.2% holding, 0% pledge, B08) and a net-cash balance sheet. **r used = 14.75%** (bounded [9%, 18%]).
- RRM = 1 + (13.5 − r) x 0.12 = 1 + (13.5 − 14.75) x 0.12 = 1 + (−1.25)(0.12) = 1 − 0.15 = **0.85x** (bounds 0.70–1.60; not binding). Percentage-point reading per Amendment 4.4.
- **Track 1 Destination PE (RRM) = 19.375 x 0.85 = 16.47x -> 16.5x**, capped at 25x (cap not binding). Range ±7.5% = **15.0x to 17.5x, mid 16.5x**. This matches the deliberation's "RRM track 16-17x, lower reality track" note (B10).

### Track divergence and governing track

- Track 2 (additive) mid 25.0x vs Track 1 (RRM) mid 16.5x. Divergence = (25.0 − 16.5)/25.0 = **34%** (>15%, material).
- **Governing track: Track 2 additive (25.0x), by OPERATOR APPROVAL at the FTTCP pillar-approval gate** (wrapper: value on the operator-approved base; do not overwrite the operator's call). The additive 25x sets the reported fair value and entry zone, consistent with the deliberation (fair value ~Rs 1,100, entry Rs 563 = 1,100/1.953).
- **RRM (16.5x) is the more conservative track and is FLAGGED as the downside reality.** Under the default framework rule the more conservative track would set an even lower entry (RRM base entry ~Rs 364). Because the decision is AVOID even on the generous additive track, the RRM track only DEEPENS the AVOID; it does not change it. Both tracks are carried through all fair values below.

### CHECKPOINT (framework STOP after Section 1): Four-pillar destination PE 23.0x-25.0x (additive), 15.0x-17.5x (RRM). Current PE 38.1x trailing / 34.4x forward. Hurdle Ratio computed in Section 4E -> STOP. Proceeding.

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS

### Forward FY27 EPS derivation (operator basis: ONE-YEAR-FORWARD; FY27 EPS not published, DERIVED)

- FY26 revenue = Rs 333.18 cr (B10). Guidance FY27 revenue growth +28-30% (B10 guidance_revenue_growth_fy27_pct) -> FY27 revenue Rs 426.5 cr (+28%) to Rs 433.1 cr (+30%).
- PAT margin band: FY26 9.72% (B10 pat_margin_pct); Q1 FY27 ~10.1% (B10 note). Use 9.5%-10.15%.
- Shares = 1.0007 crore (B10 shares_crore; the B10 shares_million:100.042 was a 10x transcription slip, corrected — EPS 33.86 on PAT Rs 33.87 cr anchors 1.0007 crore).

| Case | FY27 Revenue | PAT margin | FY27 PAT | Forward FY27 EPS |
|------|--------------|-----------|----------|------------------|
| Bear | Rs 426.5 cr (+28%) | 9.5% | Rs 40.5 cr | **Rs 40.5** |
| Base | Rs 429.8 cr (+29%) | 10.0% | Rs 43.0 cr | **Rs 43.0** |
| Bull | Rs 433.1 cr (+30%) | 10.15% | Rs 44.0 cr | **Rs 44.0** |

**Forward FY27 EPS used: Bear Rs 40.5 / Base Rs 43.0 / Bull Rs 44.0.** The deliberation preview used ~Rs 44 (my bull end). Base Rs 43.0 is the conservative midpoint of the Rs 42-44 band. FY26 (Year 0) EPS Rs 33.86 (B10).

### Three-year EPS CAGR assumptions (for the Hurdle Ratio, forward basis)

- Base EPS CAGR (FY27 onward, over the 3-year hold) = **18%** — anchored to historical 3-yr PAT CAGR 18.1% (B10); the 28-30% near-term guidance is front-loaded into FY27 and decelerates.
- Bull EPS CAGR = **24%** — grade B permits bull use; set at the SOM-implied 24.3% ceiling (B10 som_implied), guidance-supported. (Grade B -> Bull is a genuine bull, not Base+5%.)

### SOM cross-check

Base 18% EPS CAGR < SOM-implied 24.3% (B10). **Consistent — assumption does not exceed the SOM ceiling.** Bull 24% sits at the SOM ceiling, justified by order book 1.37x revenue and grade B delivery.

### Sanity checks (2D)

| Check | Result | Pass? |
|-------|--------|-------|
| Revenue growth within capacity? | 28-30% is capex/land-gated (13-acre + shared 60-acre catalyst); base uses guidance | ~ (capacity-gated) |
| Margins require the unprecedented? | Base 10.0% PAT margin is near FY26 9.72% + Q1 10.1%; no heroics | Yes |
| ROCE stays >15%? | Current 23.75%, STAGNANT | Yes |
| FCF funds growth without excess debt? | Net cash -Rs 0.28 cr; capex self-funded but CFO thin (0.41x) | Marginal |
| EPS growth operational, not engineered? | Volume/mix driven; margin flat | Yes |
| Year-3 ROCE consistent with FTTCP STAGNANT? | Yes — no ROCE uplift assumed | Yes |
| CFO/PAT trajectory consistent with Pillar 2 1.00x? | INDETERMINATE; downside 0.80x flagged | ~ (flagged) |

### CHECKPOINT (framework STOP after Section 2): Projections built. Proceeding to Section 3.

---

## SECTION 3: APPLY EACH VALUATION METHOD

### PRIMARY — P/E (Section 1B destination PE on one-year-forward FY27 EPS)

| Source | Exit PE |
|--------|---------|
| Four-Pillar destination (additive, governing) | 23.0x - 25.0x, mid 25.0x |
| RRM-track destination (conservative shadow) | 15.0x - 17.5x, mid 16.5x |
| Sector cap (absolute) | 25.0x |
| Applied exit PE (additive, per operator approval) | 25.0x |

**Fair value = destination PE x forward FY27 EPS** (one-year-forward basis, per operator).

Track 2 (additive, 25.0x):
| Case | FY27 EPS | Fair Value |
|------|----------|-----------|
| Bear | Rs 40.5 | Rs 1,013 |
| Base | Rs 43.0 | **Rs 1,075** |
| Bull | Rs 44.0 | Rs 1,100 |

Track 1 (RRM, 16.5x):
| Case | FY27 EPS | Fair Value |
|------|----------|-----------|
| Bear | Rs 40.5 | Rs 668 |
| Base | Rs 43.0 | **Rs 710** |
| Bull | Rs 44.0 | Rs 726 |

Downside cash scenario (Pillar 2 -> 0.80x): additive destination = min((19.375 x 0.80 + 2) x 1.25, 25) = min(21.9, 25) = 21.9x -> base fair value 21.9 x 43.0 = Rs 942. Flagged, not the base case.

### SECONDARY — EV/EBITDA cross-check

Destination PE 25.0x implies EV/EBITDA ~0.65 x 25 = **16.3x**. MACPOWER trades at EV/EBITDA 27.5x today (FY26, B10) — well above the justified exit multiple. The cross-check independently confirms the stock is richly priced versus its earned multiple.

### TERTIARY — P/B floor

P/B 10.4x on BVPS FY25 Rs 142.77 (B10). Theoretical P/B = ROE / CoE = 17.65% / 14.75% = 1.20x -> justified price ~Rs 171. Current P/B is ~9x the theoretical fair P/B — an asset-based floor far below CMP, consistent with an earnings-growth premium already fully priced. Tertiary weight only.

### Method-wise fair value (Base, governing additive track)

| Method | Weight | Base Fair Value |
|--------|--------|-----------------|
| P/E (Section 1B, 25x fwd) | 60% | Rs 1,075 |
| EV/EBITDA (16.3x exit) | 30% | ~Rs 1,010 |
| P/B (floor) | 10% | (floor only, ~Rs 171; treated as non-binding sanity) |

Weighted base fair value converges near **Rs 1,000-1,075** on the additive track. The governing headline is the P/E-primary Rs 1,075 (base).

### CHECKPOINT (framework STOP after Section 3): Methods applied. Proceeding to Section 4.

---

## SECTION 4: TRIANGULATION, ENTRY PRICE & VERDICT

### 4A. Triangulated fair value (both tracks)

| | Bear | Base | Bull |
|---|------|------|------|
| Track 2 (additive, 25x) | Rs 1,013 | **Rs 1,075** | Rs 1,100 |
| Track 1 (RRM, 16.5x) | Rs 668 | **Rs 710** | Rs 726 |

### 4B. Methods agreement

P/E and EV/EBITDA agree (both ~Rs 1,010-1,075 base, additive). Spread <10%. Both point the same direction: fair value materially below CMP Rs 1,481. The RRM track sits ~34% below the additive track (governance/durability discount) and reinforces the direction.

### 4C. Return expectation at CMP Rs 1,481 (fair values treated as 3-year targets, conservative)

| Scenario | Fair Value (target) | CMP | 3-yr Total Return | 3-yr CAGR | Meets 25%? |
|----------|--------------------|----|-------------------|-----------|-----------|
| Bear (additive) | Rs 1,013 | Rs 1,481 | −31.6% | −11.9% | RED |
| Base (additive) | Rs 1,075 | Rs 1,481 | −27.4% | −10.1% | RED |
| Bull (additive) | Rs 1,100 | Rs 1,481 | −25.7% | −9.4% | RED |

Even the bull-case fair value is BELOW CMP. On the RRM track the losses are far deeper.

### 4D. Probability-weighted expected return (grade B: 25/50/25)

| Scenario | Probability | 3-yr CAGR | Weighted |
|----------|-------------|-----------|----------|
| Bear | 25% | −11.9% | −2.98% |
| Base | 50% | −10.1% | −5.05% |
| Bull | 25% | −9.4% | −2.35% |
| **Expected CAGR** | 100% | | **−10.4%** |

Probability weights sourced solely from B10 credibility_grade = B (Master v3.3 4D mapping). Expected 3-year CAGR is deeply negative at CMP.

### 4E. Entry price and Margin of Safety — the Hurdle Ratio (v3.3)

**Consistent-basis current PE (forward):** Current PE = CMP / forward FY27 EPS = 1481 / 43.0 = **34.4x**. (Basis kept consistent with the forward valuation, per instruction. Trailing PE 38.1x on TTM EPS ~Rs 38.9 would make the hurdle even harder.)

**HR = (1 + EPS CAGR)^3 x (Destination PE mid / Current PE), pass >= 1.953.**

Governing (additive) destination mid 25.0x:
- HR(Base 18%) = (1.18)^3 x (25.0 / 34.4) = 1.643 x 0.7259 = **1.19**
- HR(Bull 24%) = (1.24)^3 x (25.0 / 34.4) = 1.907 x 0.7259 = **1.38**

Both below 1.953. **Bull fails -> HURDLE = STOP.** 25% CAGR is infeasible even on bull-case earnings at CMP. (On the RRM 16.5x track: HR(Base) = 1.643 x 0.48 = 0.79 — far worse.)

**Entry price (governing additive track, Tier A divisor 1.953):**
- Base fair value Rs 1,075 / 1.953 = **Rs 550** (25% CAGR entry)
- Extra-safety (30% CAGR) = 1,075 / 2.197 = Rs 489
- **Margin of Safety price = Rs 550 x 0.80 = Rs 440**
- **Ideal entry range: Rs 440 to Rs 550** (buy at the bottom of the band)
- RRM-track entry (conservative shadow): Rs 710 / 1.953 = Rs 364; MoS Rs 291.

CMP Rs 1,481 is ~2.7x the additive entry and ~4.1x the RRM entry. The framework's PROCEED-with-CAVEATS quality does not translate into a buyable price anywhere near CMP.

### 4F. Risk-reward asymmetry

| | Value at CMP 1,481 |
|---|---|
| Bull target Rs 1,100 | −25.7% (downside even in bull) |
| Base target Rs 1,075 | −27.4% |
| Bear floor Rs 1,013 | −31.6% |
| Upside / Downside ratio | **~0.0x** (no positive upside exists; stock is above even bull fair value) — fails the >=2x requirement |

### 4G. Four-pillar exit multiple validation

| Check | Result | Pass? |
|-------|--------|-------|
| Year-3 ROCE justifies base used, matches FTTCP? | 23.75% STAGNANT, no uplift assumed | Yes |
| Year-3 CFO/PAT justifies cash multiplier? | INDETERMINATE 1.00x provisional; 0.80x downside flagged | Conditional |
| Primary catalyst fired by Year 3 (base)? | 13-acre ramp assumed; 60-acre SHARED CATALYST slipped 3x | Flagged |
| Strategic premium justified (single-credit)? | +0x, respected | Yes |
| UA ordering correct min(F x 1.25, Cap)? | min(26.72, 25) = 25.0x | Yes |
| Would you buy another stock at 25x fwd with these metrics? | Only well below CMP | — |

### 4H. FINAL VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP Rs 1,481 | Market Cap Rs 1,482 cr | Shares 1.0007 cr** (B10)
- **FOUR-PILLAR EXIT PE (additive, governing):** ROCE Base 19.4x (FTTCP STAGNANT, ROCE 23.75% AR Note 38, recovery NOT credited, normalization route NONE) | Cash Mult 1.00x (INDETERMINATE, FLAG-CASH; 0.80x downside) | Quality Base 19.4x | Growth +2x (3a order book 1.37x, capex 70%, grade B) | Strategic +0x | Raw 21.4x | UA applied YES x1.25 -> 26.75x | Sector Cap 25x ABSOLUTE (Cables/Industrial products; 38x manifest error rejected) | **DESTINATION PE 23.0x-25.0x, mid 25.0x**
- **RRM TRACK:** r 14.75%, RRM 0.85x, **destination 15.0x-17.5x, mid 16.5x** — more conservative, flagged as downside reality; deepens AVOID.
- **DIVERGENCE:** 34% (>15%); governing track = additive 25.0x by operator approval at the FTTCP gate.
- **HURDLE RATIO:** Base 1.19 / Bull 1.38 (both < 1.953) -> **STOP.**
- **METHODS:** P/E 60% (Rs 1,075 base) | EV/EBITDA 30% (~Rs 1,010; implied exit 16.3x vs current 27.5x) | P/B 10% (floor).
- **WEIGHTED FAIR VALUE (Base):** additive Rs 1,075 | RRM Rs 710.
- **EXPECTED CAGR (prob-weighted, grade B 25/50/25):** −10.4%.
- **UPSIDE/DOWNSIDE:** ~0.0x (no upside at CMP).
- **ENTRY RANGE:** Rs 440 to Rs 550 (additive) | **MoS Rs 440** | RRM shadow entry Rs 364.
- **DECISION: AVOID (on valuation).** FTTCP disposition is PROCEED WITH CAVEATS on quality, but the price is ~2.7x the entry zone; the 25% hurdle STOPS on both base and bull earnings.
- **KEY ASSUMPTIONS THAT COULD CHANGE THIS:**
  - Up-arrow: cash conversion resolves clean (CFO/PAT >70% sustained) -> Pillar 2 to 1.15-1.30x; a FIRING ROCE re-rate -> Pillar 1 higher. Both are cap-bound at 25x, so they change the entry zone only modestly, not the AVOID at CMP.
  - Down-arrow: next print confirms structural cash leak -> Pillar 2 0.80x -> destination 21.9x -> base fair value Rs 942, entry Rs 483. Receivables ageing worsening (>6mo 15.4%) is the leading tell.
- **EXIT FRAMEWORK:** target exit 25x fwd; thesis broken if cash conversion prints structural (<0.30x) or 60-acre catalyst dies; time stop 5 years; PE compression floor 16.5x (RRM).
- **SHARED CATALYST FLAG:** 13-acre capex + 60-acre land is the single point of failure behind BOTH revenue fulfilment and the margin/ROCE aspiration (slipped 3x) — for Role 3 stress-test.

**ONE-LINE THESIS:** MACPOWER is a grade-B, PROCEED-WITH-CAVEATS CNC-tools grower whose four-pillar destination PE is cap-bound at 25.0x (ROCE 23.75%, cash 1.00x INDETERMINATE, EM 15, Cables/Industrial 25x cap) giving a one-year-forward base fair value of ~Rs 1,075 against CMP Rs 1,481, so it is AVOID-on-valuation with the 25% hurdle STOPPING on both base and bull earnings; entry only at Rs 440-550.

### CHECKPOINT (framework STOP after Section 4): Valuation complete. Four-pillar exit PE 23.0x-25.0x (RRM 15.0x-17.5x). Hurdle Ratio STOP. Entry Rs 440-Rs 550. Decision AVOID-on-valuation.

---

```yaml
stage: B11-valuation
company: "MACPOWER"
run_date: "2026-07-30"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Forward FY27 EPS not published; derived from revenue guidance x margin (Base Rs 43.0, band Rs 40.5-44.0)"
  - "FY26 ROCE reconciliation (AR Note 38 23.75% vs screener 29.1%); cap-bound at 25x either way, stated as NOTE"
  - "Credit rating PDF NOT PROVIDED; cash conversion stays INDETERMINATE"
  - "BVPS FY26 NOT FOUND; FY25 Rs 142.77 used for P/B floor"
  - "Peer multiples (JYOTICNC/ADOR/KLBRENG) NOT PROVIDED; EV/EBITDA cross-check done on own metrics"
flags:
  - "FLAG-CASH: cash conversion INDETERMINATE; Pillar 2 multiplier APPLIED = 1.00x provisional, 0.80x downside (-> destination 21.9x, base FV Rs 942)"
  - "SHARED CATALYST: 13-acre capex + 60-acre land gates both revenue and margin/ROCE narratives; slipped 3x"
  - "Track divergence 34%: additive 25.0x governs by operator approval; RRM 16.5x flagged as more conservative reality, deepens AVOID"
  - "Sector cap corrected to 25x (Cables/Industrial products); manifest 38x rejected"
framework_versions: "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2"
pe_basis: "forward"
exit_pe_base_approved: 25.0
destination_pe:
  track1_rrm: {low: 15.0, mid: 16.5, high: 17.5, r_used: 14.75, rrm: 0.85}
  track2_additive: {low: 23.0, mid: 25.0, high: 25.0}
  divergence_pct: 34
  governing_track: "Track 2 additive (25.0x) per operator approval at FTTCP gate; RRM 16.5x flagged more conservative, deepens AVOID"
pillar_detail:
  roce_used: 23.75
  roce_base: 19.375
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.00
  structural_or_growth: "INDETERMINATE"
  growth_offset: 0
  growth_premium: 2
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: true
  sector_cap_used: 25.0
hurdle_ratio: {base: 1.19, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 668, base: 710, bull: 726}
  track2: {bear: 1013, base: 1075, bull: 1100}
expected_cagr_prob_weighted: -10.4
entry_range: {low: 440, high: 550}
mos_price: 440
upside_downside_ratio: 0.0
decision: "AVOID (on valuation); FTTCP PROCEED WITH CAVEATS on quality, price ~2.7x entry zone, Hurdle STOP on base and bull"
unresolved_inputs_used:
  - "Forward FY27 EPS: conservative assumption Base Rs 43.0 (revenue +29% x 10.0% margin), because full-year EPS not published; band Rs 40.5-44.0 shown"
  - "BVPS FY26: conservative assumption Rs 142.77 (FY25), because FY26 audited BVPS NOT FOUND; P/B is tertiary floor only"
som_cagr_crosscheck: "consistent"
one_line_thesis: "MACPOWER four-pillar destination cap-bound at 25.0x forward gives base fair value ~Rs 1,075 vs CMP Rs 1,481; AVOID-on-valuation, 25% hurdle STOPS on base and bull, entry only at Rs 440-550."
```
