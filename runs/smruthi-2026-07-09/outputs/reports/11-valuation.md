# STAGE 11 — ROLE 1 MULTI-MODAL VALUATION (RE-RUN on corrected B10)
## Smruthi Organics Ltd (SMRUTHI) | Run Date 2026-07-09 | Model: Opus 4.8
**Framework authority: Master Project Prompt v3.3 / Section 1B v3.3 Amendments / FTTCP v1.2. Where wrapper and framework conflict, framework wins. Section 1B is sole exit-multiple authority. Conservative bias throughout. All inputs from corrected B10 only.**

---

## 0. INPUT DISCIPLINE LEDGER (unresolved fields → conservative fills, no silent fills)

| # | Field | B10 status | Conservative assumption used | Rule / anchor |
|---|-------|-----------|------------------------------|---------------|
| 1 | ROCE latest (%) | NOT FOUND (B01 median 9.29% FY17-26; FY23-26 compressed to 7.2-7.9%) | **7.2%** (lower bound of the recent compression band) | Master conservative-assumption rule; B10 roce_2yr_trend "declining", B01 "FY23-FY26 compression to 7.2-7.9%" |
| 2 | FTTCP ROCE forward verdict | Not carried in B10 (NO-CONCALL MODE; FTTCP could not be robustly run) | **DECLINING** → Pillar 1 uses FY[Y+1] lower-bound ROCE, no recovery credit | FTTCP v1.2 "when in doubt, DECLINING"; ROCE trend declining, no confirmed forward catalyst (ANVISA/EDQM unconfirmed, revenue missed -19%) |
| 3 | 3-Year Revenue CAGR / PAT CAGR | NOT FOUND (only FY24-26 2-yr available) | 2-yr revenue CAGR **-10.04%** used as trend proxy to anchor Bear | B10 revenue_2yr_cagr_pct |
| 4 | Peer medians (P/E, EV/EBITDA, P/B, growth, ROCE) | Unresolved (B06 skipped) | Standalone multiples only; **no peer cross-check credited** | B10 unresolved; NO-CONCALL MODE |
| 5 | Current capacity utilisation | Unresolved ("single biggest unresolved input") | Base revenue CAGR held **below** SOM-implied 9.0% and below capex-embedded 6.7% capacity | B09 capacity-SOM gap |
| 6 | ANVISA/EDQM inspection outcomes | Unresolved (no update as of run date) | **No regulatory catalyst credited** (moot: EM 13.4 < 25 → Pillar 3 = +0x anyway) | B07 p.22-25 |

INPUT UNRESOLVED lines are restated in-section at first use.

---

## SECTION 1A — METHOD SELECTION & JUSTIFICATION

Business type (B04): capital-employing manufacturer of bulk drugs / drug intermediates. Commoditised price-taker, no lender carve-out (not a financial), no BOO/annuity component. Heavy depreciation+interest load (D&A 6.35 + interest 1.68 = 8.03 Cr consumes ~70% of EBITDA 11.46 Cr), so PAT is thin relative to EBITDA — capital structure matters, which favours an EV method as primary.

| Method | Suitable here? | Weight | Justification |
|--------|----------------|--------|---------------|
| **EV/EBITDA (PRIMARY)** | Yes | **60%** | Capital-intensive manufacturer; neutralises leverage and the large D&A load; B04 designates it primary. |
| **P/E (SECONDARY)** | Yes, with caution | **40%** | Profitable (thin) earnings; captures equity holder's residual after the heavy D&A+interest. Held secondary because a single depressed FY26 PAT distorts it — but conservatively material. |
| P/B | **No** | 0% | Manufacturer, not a lender; book value (Rs 64.26) does not capture value here and no lender carve-out applies (Section 1B Pillar 2L not invoked). |
| PEG | No | 0% | Growth negative/erratic (-19% FY26); PEG undefined. |
| EV/Sales | No | 0% | Mature, margin-volatile; misleads. |
| DCF | No (cross-ref only) | 0% | FCF negative 2 of last 3 years, revenue declining, credibility C — terminal value would dominate and be unreliable. Not run as a weighted method; qualitative note only. |
| EV/Capacity | No | 0% | Capacity utilisation unresolved; cannot anchor. |

**Final selection: EV/EBITDA 60% (primary) + P/E 40% (secondary) = 100%.** P/B not applicable (manufacturer, no lender carve-out) per task discipline.

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3

### Pillar 1 — ROCE Base Multiple (continuous formula)

INPUT UNRESOLVED: ROCE Latest. Conservative assumption used: **7.2%**, because B10 marks FY26 ROCE NOT FOUND and B01 places the recent (FY23-26) band at 7.2-7.9% on a declining trend; the lower bound is the conservative fill.

INPUT UNRESOLVED: FTTCP ROCE forward verdict (not carried by B10 in NO-CONCALL MODE). Conservative assumption used: **DECLINING**, because the ROCE trend is declining, no forward catalyst is confirmed (regulated-market milestones unconfirmed, central revenue guidance missed -19%), and FTTCP v1.2 mandates "when in doubt, DECLINING." DECLINING → Pillar 1 uses FY[Y+1] lower-bound ROCE; that lower bound is not separately disclosed, so the conservative documented floor 7.2% is used with **no recovery uplift**.

- ROCE (used for base): **7.2%**
- Formula (ROCE ≤ 33%): Base PE = 0.5 × 7.2 + 7.5 = 3.6 + 7.5 = **11.1x** (floor 9x not binding; 11.1 > 9)
- **ROCE recovery credited via: NOT CREDITED** (DECLINING verdict; no midpoint smoothing, no strategic re-rating optionality). Single-credit rule satisfied trivially.

### Pillar 2 — Cash Conversion Multiplier

B10 determination (verbatim, do not re-litigate): **FLAG-CASH — "Not structural. Working-capital-driven (receivables release). FCF negative for 2 consecutive years. DSCR halved."** Rating agency (CARE, 11-Mar-2026) calls liquidity "Adequate" and does NOT classify WC as structurally negative — so the 0.65x structural band is ruled out by the framework's own evidence gate.

Band determination (show the band and why):
- Cumulative CFO/PAT = **2.80x** (280%); Latest FY CFO/PAT = 6.49x; FCF: FY26 +13.79 Cr but **FY24 -2.76, FY25 -1.44 (negative 2 of 3 years)**; CFO positive every year (B10).
- The 1.30x / 1.15x elite bands both **require FCF positive** — not met (FCF negative 2 of 3 years, and FY26 CFO is a one-time receivables-release spike in a -19% revenue year, not sustained). RULED OUT.
- The 0.80x band triggers on "CFO/PAT below 30% **or CFO negative**" — neither holds (CFO/PAT high, CFO positive every year). RULED OUT. (Verifier C confirmation: FCF-negative is NOT CFO-negative.)
- The 0.65x structural band requires rating-agency-confirmed persistent WC — CARE says liquidity Adequate. RULED OUT.
- **Remaining as-written fit: "CFO/PAT 30-50% OR volatile (some good years, some bad) → 1.00x."** The FY24/25 negative-FCF then FY26 receivables-spike pattern is textbook *volatile*. **Band applied: 1.00x (Neutral, volatile).** This is the band the framework actually prescribes for this determination (not INDETERMINATE); it also matches Verifier C's strict-as-written read.
- Structural or growth-induced? Not structural (B10) — but also **not classic growth-induced** (revenue is *declining* -19%, no capacity-building drag to offset). Growth Offset therefore **N/A / +0** (the offset only modifies the 0.80x growth-induced band, which was not assigned; and revenue CAGR is not positive-growth-induced).
- **Effective Cash Multiplier = 1.00x. Growth offset = +0.**

Destination-PE effect stated both ways (as instructed):
- **Applied (1.00x, volatile band): Quality-Adjusted Base = 11.1 × 1.00 = 11.1x → Final Destination PE 11.1x.**
- Alternative (if judged 0.80x on extra conservatism): 11.1 × 0.80 = 8.88x → Final Destination PE ≈ 8.9x (range 8.0-9.5x).
- Either way the destination PE (8.9-11.1x) sits **far below the current PE of 40.8x**, so the Hurdle verdict (below) is invariant to this choice. I apply **1.00x** because it is the band whose triggers actually hold; the 0.80x alternative is shown for transparency, not applied.

**Quality-Adjusted Base (C) = 11.1x.**

### Pillar 3 — Growth Visibility Premium

- Emerging Moat Score = **13.4** (B10) | Classification MODEST | Catalyst proximity: ANVISA/EDQM 12m but unconfirmed | Evidence: mostly documented.
- Table: **EM below 25 → +0x.** No premium regardless of catalyst timing.
- **Growth Visibility Premium (D) = +0x. Shared catalyst? No.**

### Strategic Asset Premium

- B10: "No moats confirmed. Commoditised price-taker betting on unproven regulated-market transition." No rare licence, no franchise pricing power, no institutional-backed turnaround. ROCE re-rating optionality NOT available (recovery not credited anywhere; verdict DECLINING).
- **Strategic Premium (E) = +0x.** Single-credit rule respected (nothing double-credited).

### Undiscovered Alpha Multiplier

- UA qualifiers (B10 ua_qualifiers): listed ≥12m TRUE; Gate0 ≥60 OR EM ≥25 **FALSE** (Gate0 37, EM 13.4); FII+DII <3% TRUE. **all_met = FALSE.**
- **UA NOT APPLIED.** F2 = F (no 1.25x). Sector-cap quality-uplift also not available (requires UA trigger + Moderate-Strong durability; neither holds).

### Sector Reality Cap

- Sector row (B10 / manifest): **Pharma / CDMO → 38x.** Absolute. No quality uplift (UA not triggered).

### Four-Pillar Summary (Track 2 — Additive)

| Step | Calculation | Value |
|------|-------------|-------|
| A. ROCE Base | ROCE 7.2% → 0.5×7.2+7.5 | 11.1x |
| B. Cash Multiplier (effective) | 1.00x (volatile band) + offset 0 | 1.00x |
| C. Quality-Adjusted Base | A × B = 11.1 × 1.00 | 11.1x |
| D. Growth Visibility Premium | EM 13.4 (<25) | +0x |
| E. Strategic Premium | no scarcity | +0x |
| F. Raw Destination PE | C + D + E | **11.1x** |
| F2. UA-Adjusted Raw PE | UA all_met FALSE → F unchanged | 11.1x |
| G. Sector Cap | Pharma/CDMO | 38x |
| **H. Final Destination PE** | **min(F2, G) = min(11.1, 38)** | **11.1x** |

**Destination PE Range (H ±7.5%): 11.1 × 0.925 = 10.27; 11.1 × 1.075 = 11.93 → rounded to nearest 0.5x = 10.5x to 12.0x. Mid 11.1x.**

### RRM Dual-Track Derivation

- **Track 2 (Additive):** Destination PE mid **11.1x** (10.5-12.0x), as above.
- **Track 1 (RRM):** Destination PE = Fundamental Base PE × RRM, capped at sector cap.
  - Fundamental Base PE = Quality-Adjusted Base = 11.1x (Pillar 3 and Strategic are +0, so the additive spine equals the fundamental base here).
  - Base r: small/micro-cap 14%. Adjustments: **+2%** governance CONCERN (remuneration ~125% of PAT via special resolutions; full ID turnover; 24-yr title-deed defect; ECL under-provisioning — B08); **+1%** weak durability (no confirmed moat, commoditised). **r = 17%** (within [9%,18%]).
  - RRM = 1 + (13.5% − 17%) × 0.12 = 1 + (−0.035)(0.12) = 1 − 0.0042 = **0.996** (within bound 0.70-1.60).
  - Track 1 Destination PE = 11.1 × 0.996 = **11.05x**, cap 38 → 11.05x. Range ±7.5% ≈ **10.5x to 11.9x**, mid 11.05x.
- **Divergence: (11.1 − 11.05)/11.05 = 0.45% (<15%).** The tracks converge because both Pillar 3 and Strategic premiums are +0, leaving the RRM's small coefficient nothing to move against. **Governing track: Track 1 (RRM), marginally the more conservative (11.05x); the entry zone is set on it, but the two are numerically identical to within 1%.** Both are carried through every fair value and the verdict card below.

### Hurdle Ratio (25% CAGR feasibility) — sole STOP authority

- Current PE = CMP 122 / EPS 2.99 = **40.80x** (the crux: the market already prices ~41x for a 7% ROCE, no-moat, declining, governance-flagged bulk-drug maker).
- Destination PE mid = 11.1x (Track 2) / 11.05x (Track 1). Use 11.1x → ratio 11.1/40.8 = 0.2721.
- Base EPS CAGR = **10%** (derived in Section 2: revenue +5% + delivered cost-rationalisation margin recovery).
- Bull EPS CAGR for the HR check: **credibility grade C → Bull capped at Base + 5% = 15%** (grade A/B bull not permitted).

| Row | EPS CAGR | (1+g)³ | × 0.2721 | HR | vs 1.953 |
|-----|----------|--------|----------|----|----------|
| Base | 10% | 1.3310 | | **0.362** | FAIL |
| Bull (capped, C) | 15% | 1.5209 | | **0.414** | FAIL |

**HR(Bull) 0.414 < 1.953 → STOP.** The stock fails the 25% hurdle at current price even on bull-case earnings — the 41x current PE cannot be sustained toward an earned 11x destination. Per pipeline override, all remaining sections are completed for the record; the verdict card reads **AVOID-on-valuation.**

Would I personally pay 40.8x for a 7.2% ROCE, no-moat, -19% revenue, governance-concern bulk-drug maker? **No.**

> **CHECKPOINT (framework STOP 1):** Section 1 complete. Methods: EV/EBITDA 60% + P/E 40%. Four-pillar destination PE 10.5x-12.0x (Track 2 mid 11.1x); RRM track 10.5x-11.9x (mid 11.05x). Current PE 40.8x. Hurdle Ratio 0.36 base / 0.41 bull → **STOP**. Proceeding without halt per pipeline mode.

---

## SECTION 2 — EARNINGS & CASH FLOW PROJECTIONS

### 2A. Revenue Projection

SOM cross-check first: SOM-implied revenue CAGR = **9.0% (3-yr) / 9.6% (5-yr)** (B10); capex-embedded capacity supports only ~6.7% (B09 capacity-SOM gap). Any base assumption must stay at/below these ceilings.

| Assumption | Bear | Base | Bull |
|------------|------|------|------|
| Logic | China/Russia stays dead, no regulated-market entry, further slippage | Partial stabilisation, cost-rationalisation holds, no new export ramp | China/Russia recovers + first ANVISA/EDQM approval; revenue re-ramps |
| Revenue CAGR | **-8%** | **+5%** | **+9%** (= SOM ceiling) |
| Year 0 (FY26) | 101.97 | 101.97 | 101.97 |
| Year 3 | 101.97×0.92³ = **79.4** | 101.97×1.05³ = **118.05** | 101.97×1.09³ = **132.1** |

Cross-check verdict: **Base 5% < SOM-implied 9.0% and < 6.7% capacity → CONSISTENT (assumption below ceiling, no cut required).** Bull 9% sits at the SOM ceiling and against the 6.7% capacity limit — flagged as capacity-stretched, which is one more reason it is not credited in the Hurdle bull.

### 2B. Profitability Projection

| Assumption | Bear | Base | Bull |
|------------|------|------|------|
| EBITDA margin | 10.0% (compression on low utilisation) | 12.1% (delivered RM 54%→44% cost benefit, partial operating leverage) | 14.0% (full leverage + mix) |
| Depreciation | ~6.5 | ~6.8 | ~7.0 |
| Interest | ~1.6 | ~1.4 | ~1.3 |
| Tax rate | 25% | 25% | 25% |
| Share dilution | 0% (no raise disclosed) | 0% | 0% |

### 2C. Complete Projection Table (Base case primary)

| Line item | Year 0 (FY26) | Year 1 | Year 2 | Year 3 |
|-----------|---------------|--------|--------|--------|
| Revenue (Cr) | 101.97 | 107.07 | 112.42 | 118.05 |
| EBITDA (Cr) | 11.46 | 12.31 | 13.49 | 14.28 |
| EBITDA margin | 11.25% | 11.5% | 12.0% | 12.1% |
| PAT (Cr) | 3.43 | 3.7 | 4.1 | 4.56 |
| EPS (Rs) | 2.99 | 3.23 | 3.58 | **3.98** |
| Est. CFO (Cr) | 22.26* | 8-10 | 9-11 | 10-12 |
| Est. FCF (Cr) | 13.79* | 2-4 | 3-5 | 3-5 |
| Est. net debt (Cr) | 6.10 | ~5.5 | ~5.2 | ~5.0 |
| Est. ROCE | ~7.2% | ~7.5% | ~8% | ~9% |

*FY26 CFO/FCF are inflated by a one-time receivables release (AR 32.47→19.30 Cr); normalised forward CFO reverts toward net-accrual levels — this is the FLAG-CASH point and the reason the Pillar 2 multiplier is not credited above 1.00x.

Scenario EPS Year 3: **Bear 2.33** (2.99×0.92³, ≈ -8% EPS CAGR under compression), **Base 3.98** (+10%), **Bull 5.17** (+20%, projections-only; hurdle uses capped 15%).

### 2D. Projection Sanity Checks

| Check | Result | Pass? |
|-------|--------|-------|
| Revenue faster than capacity? | Base 5% < 6.7% capacity | PASS |
| Margins require something unprecedented? | 12.1% below FY-prior highs; cost benefit delivered | PASS |
| ROCE stays above 15%? | No — stays ~7-9% | **FAIL (consistent with low destination PE)** |
| FCF funds growth without excess debt? | Marginal; forward FCF thin | CAUTION |
| EPS growth operational not engineered? | Yes (margin + slight leverage) | PASS |
| Implied market-share gain realistic? | Base holds ~1.4% of SAM | PASS |
| CFO/PAT trajectory consistent with Pillar 2 (1.00x)? | Yes — normalises off the one-time spike to volatile/neutral | PASS |
| **Year 3 ROCE consistent with FTTCP verdict used (DECLINING/low)?** | Yes — ~9% stays sub-15%, no recovery credited | PASS (FTTCP-consistency row) |

> **CHECKPOINT (framework STOP 2):** Section 2 complete. Base Year-3 EPS Rs 3.98; ROCE stays ~7-9% (sub-15%, consistent with the DECLINING Pillar-1 input). Proceeding.

---

## SECTION 3 — APPLY EACH VALUATION METHOD

### 3.1 EV/EBITDA (PRIMARY, 60%)

- Four-pillar PE destination 11.1x → implied EV/EBITDA ≈ 0.6-0.7× = 6.7-7.8x. Capex (8.47) > depreciation (6.35), so EBITDA overstates cash → use the **lower end**. **Exit EV/EBITDA range 6.5-7.5x, mid 7.0x.** (Current EV/EBITDA = 145.70/11.46 = 12.7x — the de-rating gap is the whole story.)

| Year-3 | Bear (EBITDA 8.0) | Base (EBITDA 14.28) | Bull (EBITDA 18.5) |
|--------|-------------------|---------------------|--------------------|
| EV @ mid 7.0x | 56.0 | 100.0 | 129.5 |
| Less net debt Y3 | 6.0 | 5.0 | 4.0 |
| Equity value (Cr) | 50.0 | 95.0 | 125.5 |
| ÷ 1.14463 Cr shares | **Rs 43.7** | **Rs 83.0** | **Rs 109.6** |

EV/EBITDA fair value (Year 3): **Bear ~Rs 44 · Base ~Rs 83 · Bull ~Rs 110.**

### 3.2 P/E (SECONDARY, 40%)

Exit PE = Section 1B destination ONLY. Applied range 10.5x (low) / 11.1x (mid) / 12.0x (high). No other exit PE used.

| Year-3 EPS | @10.5x | @11.1x | @12.0x |
|------------|--------|--------|--------|
| Bear 2.33 | 24.5 | 25.9 | 28.0 |
| Base 3.98 | 41.8 | **44.2** | 47.8 |
| Bull 5.17 | 54.3 | 57.4 | **62.0** |

P/E fair value (Year 3): **Bear ~Rs 24.5 · Base ~Rs 44.2 · Bull ~Rs 62.**

### 3.3 Method-wise Fair Value Summary (Track 2 / Additive)

| Method | Weight | Bear | Base | Bull |
|--------|--------|------|------|------|
| EV/EBITDA (primary) | 60% | 44 | 83 | 110 |
| P/E (secondary) | 40% | 24.5 | 44 | 62 |

**Method divergence flag:** EV/EBITDA base (Rs 83) vs P/E base (Rs 44) spread is **~47% (>30%)**. Driver: the heavy D&A+interest load leaves PAT thin (3.36% margin) versus EBITDA (11.25%), so P/E de-rates far harder than EV/EBITDA. Both nevertheless sit **well below CMP 122**, so the AVOID conclusion is invariant to the blend. Conservative note: the equity-holder (P/E) view is the lower, and it governs the safety read.

> **CHECKPOINT (framework STOP 3):** Section 3 complete. All methods point down from CMP 122; base blended fair value ~Rs 68 (Year 3). Proceeding.

---

## SECTION 4 — TRIANGULATION, ENTRY & VERDICT

### 4A. Triangulated Fair Value (Year 3) — BOTH TRACKS

Track 2 (Additive, destination PE mid 11.1x):

| | Bear | Base | Bull |
|--|------|------|------|
| EV/EBITDA × 60% | 44×0.6 = 26.4 | 83×0.6 = 49.8 | 110×0.6 = 66.0 |
| P/E × 40% | 24.5×0.4 = 9.8 | 44×0.4 = 17.6 | 62×0.4 = 24.8 |
| **Weighted FV** | **~Rs 42** | **~Rs 68** | **~Rs 89** |

Track 1 (RRM, destination PE mid 11.05x ≈ Track 2 within 0.5%): weighted FV **Bear ~Rs 42 · Base ~Rs 67 · Bull ~Rs 88** (identical within 1%). The tracks do not diverge materially; the conservative Track 1 governs entry.

### 4B. Methods Agreement

- All methods point the same direction: **DOWN from CMP.** Highest-lowest base spread ~47% (EV/EBITDA vs P/E). Outlier: EV/EBITDA (flattered by high D&A). Most-trusted for THIS company: a blend, leaning to the P/E floor for safety. Even the most generous single method (EV/EBITDA base Rs 83) is 32% below CMP 122.

### 4C. Return at Current Price (Year 3, Track 2 base)

| Scenario | Weighted FV (Y3) | CMP | Total return | 3-yr CAGR | ≥25%? |
|----------|------------------|-----|--------------|-----------|-------|
| Bear | 42 | 122 | -66% | -29.9% | 🔴 |
| Base | 68 | 122 | -44% | -17.7% | 🔴 |
| Bull | 89 | 122 | -27% | -10.0% | 🔴 |

Every cell negative. 0/9 matrix cells reach 25%; 0/9 reach 15%.

### 4D. Probability-Weighted Expected Return

Credibility grade **C → weights 35 / 45 / 20** (sole source: B10 credibility_grade).

| Scenario | Probability | 3-yr CAGR | Weighted |
|----------|-------------|-----------|----------|
| Bear | 35% | -29.9% | -10.47% |
| Base | 45% | -17.7% | -7.97% |
| Bull | 20% | -10.0% | -2.00% |
| **Expected CAGR** | 100% | | **-20.4%** |

### 4E. Entry Price (governed by conservative Track 1, base FV Rs 67-68)

| Calc | Value |
|------|-------|
| Base FV Year 3 | Rs 68 |
| 25% CAGR entry = 68 / 1.953 | **Rs 34.8** |
| 30% CAGR entry = 68 / 2.197 | Rs 30.9 |
| MoS price (20% below 25% entry) | **Rs 27.8** |
| **Ideal entry range** | **Rs 28 to Rs 35** |

CMP 122 is ~3.5x the top of the entry zone. Not remotely investable at current price.

### 4F. Risk-Reward Asymmetry

| | Value |
|--|-------|
| Bull target (Y3) Rs 89 | Upside -27% |
| Base target (Y3) Rs 68 | Upside -44% |
| Bear floor (Y3) Rs 42 | Downside -66% |
| Upside(base)/Downside(bear) | **Negative — both below CMP; ratio fails the ≥2x test (reported 0.0)** |

### 4G. Four-Pillar Validation

| Check | Result | Pass? |
|-------|--------|-------|
| Year-3 ROCE justifies ROCE base & matches FTTCP? | ~9% sub-15%; DECLINING input honoured, no recovery credited | PASS |
| Year-3 CFO/PAT justifies cash multiplier? | Normalises off one-time spike to volatile/neutral 1.00x | PASS |
| Primary catalyst fired by Year 3 (base)? | No — ANVISA/EDQM unconfirmed; not credited | PASS (nothing over-credited) |
| Strategic premium justified (single-credit)? | +0x; nothing double-counted | PASS |
| UA ordering correct — min(F×1.25, Cap)? | UA not applied (all_met false); min(11.1, 38) | PASS |
| Would I buy a different stock at this exit PE with these Y3 metrics? | 11x for 9% ROCE — yes, that is fair; the problem is the 41x ENTRY, not the exit | PASS |

Exit PE needs no downward revision — it is already conservative. The failure is the entry price, correctly caught by the Hurdle Ratio.

### 4H. FINAL VALUATION VERDICT CARD

- **CMP Rs 122 | Market Cap Rs 139.6 Cr** (reconciled; manifest 169.0 recorded as conflict, not used) | EV Rs 145.70 Cr | Shares 1.14463 Cr
- **FOUR-PILLAR EXIT PE:** ROCE Base 11.1x (FTTCP verdict DECLINING; ROCE used 7.2%, recovery NOT credited) × Cash Mult 1.00x (not-structural / WC-driven, *volatile* band; offset +0) = Quality Base 11.1x; Growth Prem +0x (EM 13.4 <25); Strategic +0x; **Raw PE 11.1x**; UA NOT applied (all_met false); Sector Cap 38x (Pharma/CDMO, no uplift); **DESTINATION PE 10.5x-12.0x (mid 11.1x, ±7.5%).**
- **RRM TRACK:** r 17% (14 base +2 governance +1 durability); RRM 0.996; destination 10.5x-11.9x (mid 11.05x). Divergence vs additive 0.45% (<15%); tracks converge; RRM governs entry.
- **HURDLE RATIO:** Base 0.36 / Bull(capped 15%, grade C) 0.41 → **STOP** (fails even on bull earnings).
- **METHODS:** EV/EBITDA 60% (6.5-7.5x) + P/E 40% (10.5-12.0x). Method spread ~47% flagged.
- **WEIGHTED FAIR VALUE (Year 3):** Track 2 — Bear 42 / Base 68 / Bull 89. Track 1 — Bear 42 / Base 67 / Bull 88.
- **EXPECTED CAGR (prob-weighted, grade C 35/45/20):** **-20.4%.**
- **UPSIDE/DOWNSIDE:** negative on all scenarios — fails ≥2x (0.0).
- **ENTRY Rs 28-35 | MoS Rs 28.** CMP is ~3.5x above entry.
- **DECISION: AVOID (on valuation).** Bands: MoS Rs 28 / Entry Rs 35 / all Year-3 targets (42/68/89) below CMP 122.
- **KEY ASSUMPTIONS THAT COULD CHANGE IT:** ▲ a *confirmed* ANVISA/EDQM approval with order flow (would lift EM above 25 → Pillar 3 premium, and could re-rate FTTCP ROCE off DECLINING) — unconfirmed today; ▲ sustained ROCE recovery above 15% (would raise Pillar 1 base) — not visible; ▼ a further revenue leg down or ECL true-up (would deepen the de-rating). None reverse the STOP at Rs 122.
- **EXIT FRAMEWORK:** target exit moot (AVOID); thesis-turn condition = EM >25 on a documented regulatory approval AND ROCE forward verdict off DECLINING; time stop N/A (not held); PE compression floor: fair value only near entry Rs 28-35.
- **ONE-LINE THESIS:** Avoiding Smruthi at Rs 122 because a 7.2% ROCE, no-moat, -19%-revenue bulk-drug maker earns only an ~11x four-pillar destination PE (cash 1.00x volatile, EM 13.4, sector cap 38x) while the market already prices 40.8x, so the Hurdle Ratio STOPs even on bull earnings and the probability-weighted return is -20% CAGR. Key risk to the AVOID: a confirmed regulated-market approval. Cash quality: working-capital-driven, not structural.

> **CHECKPOINT (framework STOP 4 / final):** Valuation complete. Four-pillar exit PE 10.5x-12.0x. Hurdle Ratio STOP. Entry Rs 28-35. Decision AVOID (on valuation).

---

*Stage 11 complete. Framework: Master v3.3 / Section 1B v3.3 / FTTCP v1.2. All numbers anchored to corrected B10 or marked INPUT UNRESOLVED with the conservative fill named. FLAG-CASH carried forward with the applied multiplier (1.00x, volatile band).*
