# STAGE 11 — ROLE 1 DUAL-TRACK SUM-OF-THE-PARTS VALUATION

**Company:** Jubilant Agri and Consumer Products Ltd (JACPL) | **Ticker:** JUBLCPL
**Run date:** 2026-08-18 | **CMP:** Rs 2,342.40 (18-Aug-2026, B00) | **Shares:** 1.5152 Cr (B00) | **Market cap:** Rs 3,549 Cr (B00)
**Framework authority:** Master v3.3 / Section 1B v3.3 Amendments / Section 1B v3.5.1 Reconciliation / FTTCP v1.2
**Method:** SUM OF THE PARTS (operator direction 18-Aug-2026, deliberation.md). Dual track (Track 1 RRM, Track 2 additive) carried through both businesses.
**Model:** claude-opus-4-8 | **Mode:** pipeline (no interactive STOP gates; interim checkpoints written inline)

---

## 0. EARNINGS PERIMETER (STATED EXPLICITLY, PER OPERATOR DIRECTION)

The operator-approved earnings basis is **ONE-YEAR FORWARD (blended)**. Three perimeter facts govern every number below and are NOT estimated away:

1. **Forward earnings still contain the agri division until the demerger scheme is effective.** NCLT First Motion cleared 08-Jul-2026; shareholder/creditor meetings 05-Sep-2026; final order and JASL listing pending at run date (AR Note 32 p.138-139; Reg 30 09-Jul-2026). Until the scheme is effective, JACPL as it trades is the blended entity.
2. **Per-entity PAT is illustrative-allocated, not audited.** No standalone accounts exist pre-demerger (B10 input_gaps: standalone_accounts, HIGH/MEDIUM). Business A and Business B PAT, cash flow, and ROCE are allocations from group segment data (Note 39 p.150), not company financials. FY26 group non-segment items (interest Rs 6.58 Cr, exceptional Rs 3.47 Cr, unallocable corporate Rs 30.91 Cr) were allocated per valuation-sotp.md: interest onto agri, corporate split by segment PBIT, tax 25.7-25.9%.
3. **Forward EPS is un-guided and provisional.** No numeric FY27 guidance published (B10 input_gaps: forward_guidance, MEDIUM). Forward EPS annualizes a seasonally strong Q1 FY27 that still contains agri. This is the least-anchored of the three bases; per operator direction the **forward polymer-only earnings figure is built as the primary value driver** (Business A below), because the retained business is where the value sits.

FY26 segment figures (Note 39, AR p.150) and Q1 FY27 segment figures (results 11-Aug-2026) are ANCHORED. Every FY27+ figure is PROJECTED and labelled.

---

## 1. METHOD SELECTION

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | SOTP (P/E per part) | 100% | Demerger special situation; two structurally different businesses (67.5%-ROCE specialty-chemicals compounder vs subsidy-linked commodity cyclical). Blended multiple destroys information. Operator direction 18-Aug-2026. |
| Cross-check (A) | EV/EBITDA implied | context | Specialty chemicals; PE destination 35x implies EV/EBITDA ~21-24x — consistent with the branded-adhesives + high-ROCE-latex mix. |
| Cross-check (B) | Normalized-earnings P/E | context | Agri valued on mid-cycle PAT, not FY26 placement peak, to avoid pricing a cyclical top as permanent. |

P/E is the primary metric for each part; exit PE comes SOLELY from Section 1B (operator-approved bases below). No round-number default is used anywhere.

**INTERIM CHECKPOINT (Section 1A):** Method = SOTP, per-part P/E, exit PE from Section 1B only. Proceeding.

---

## 2. BUSINESS A — PERFORMANCE POLYMERS & CHEMICALS (retained, becomes Jubilant Industries Ltd)

The "adhesive" business and the primary value driver. Two sub-businesses: branded adhesives (Jivanjor, ~28% of mix, ~35% 5-yr CAGR, growth engine) on a stable high-margin industrial backbone (VP latex #1 India/#2 global ex-China, sole food-grade PVAc in India, ~72% of mix, ~65% segment ROCE). Anchored FY26 revenue Rs 1,164.84 Cr external (Note 39 p.150); segment EBIT Rs 165.46 Cr.

### 2.1 Section 1B Four-Pillar Worksheet — Business A (Track 2 additive)

| Step | Input (anchor) | Value |
|---|---|---|
| A. Pillar 1 base | ROCE **FIRING** (deliberation). Current ROCE: group 36% (AR p.7), segment 67.5% (Note 39). Continuous formula for ROCE>33%: 24 + 0.3×(67.5−33) = 34.35, **capped at 30x**. Operator-approved base **30.0x**. | 30.0x |
| — Pillar 1 normalization route | **NONE.** Route A fails the 20% test (no CWIP/idle-capital bloat >20% of capital employed). Route B barred (needs TEMPORARILY DEPRESSED/RECOVERING; this is FIRING). v3.5.1 route declared. | NONE |
| — ROCE recovery credited via | **NOT credited** — 36% is the current high, there is no recovery to credit. Strategic Premium ROCE re-rating route stays barred (single-credit rule). | not-credited |
| B. Pillar 2 cash multiplier | **1.15x** (deliberation). CFO/PAT band; clean at segment level but unconfirmable without a standalone cash statement. Structural cash drag (FLAG-CASH) is located in the demerging AGRI division, not here (deliberation §1). | 1.15x |
| C. Quality-adjusted base | A × B = 30.0 × 1.15 | 34.5x |
| D. Pillar 3 | EM 22.5 (<25 gate), growth visibility passes 1 of 2 tests, delivery grade C. Per amendment 4.1, grade C caps 3a at +2x but EM<25 pays 3b +0x; visibility 1-of-2 fails the "any two" test → **+0x**. | +0x |
| E. Strategic premium | **+2x** — niche scarcity: VP latex #1 India/#2 global ex-China; PVAc sole food-grade in India (strong franchise, limited competition, documented pricing tier). This is scarcity, NOT ROCE re-rating, so permitted alongside the not-credited Pillar 1 recovery. | +2x |
| F. Raw destination PE | C + D + E = 34.5 + 0 + 2 | 36.5x |
| F2. UA-adjusted raw | UA **applies** (all three qualifiers met: JACPL listed >12m, Gate0 71≥60, FII+DII 0.45%<3%). F × 1.25 = 36.5 × 1.25 | 45.6x |
| G. Sector cap | **Specialty chemicals 35x**, no quality uplift (operator-approved). Absolute. | 35x |
| **H. Destination PE (Track 2 additive)** | **min(F2, G) = min(45.6, 35)** | **35.0x** |

### 2.2 Track 1 RRM derivation — Business A

- Base r: small/micro-cap 14%, adjusted to **13.5%** for the strong specialty-chemicals franchise and near-debt-free balance sheet (durability Moderate-Strong).
- RRM = 1 + (13.5 − 13.5) × 0.12 = **1.00** (percentage-point reading, Amendment 4.4).
- Track 1 destination PE = Fundamental base 36.5x × RRM 1.00 = 36.5x, × 1.25 UA = 45.6x, capped at 35x → **35.0x**.

**Both tracks land on the 35x specialty-chemicals cap. Divergence = 0%.** The cap is the governing constraint; it binds identically on Track 1 and Track 2. Destination PE range = 35x ±7.5% capped = **32.5x to 35.0x**.

### 2.3 Earnings base — Business A (grounded, primary value driver)

Growth built bottom-up (valuation-sotp.md): adhesives ~18% easing to 15%, industrial backbone ~10% → PP&C revenue CAGR ~13-14%; ~60 bps/yr margin expansion off the Q1 FY27 17.1% segment print. FY26 anchored; FY27/FY28 projected (illustrative allocation).

| Rs Cr | FY26 actual | FY27 proj | FY28 proj |
|---|---|---|---|
| Revenue | 1,199 (anchor Note 39 basis) | 1,367 (+14%) | 1,545 (+13%) |
| Segment EBIT | 166 | 198 (+19%) | 232 (+17%) |
| **PAT (25.7% tax, illustrative)** | ~102 | **~125** | **~149** |
| EPS (1.5152 Cr sh) | ~67 | **~83** | ~98 |

Scenario PAT / EPS (FY27, one-year forward base):

| Case | FY27 PAT | FY27 EPS | FY27-30 EPS CAGR | FY30 EPS | Target @ 35x |
|---|---|---|---|---|---|
| Bear (rev +9%, margin flat ~14%) | ~112 | ~74 | 9% | ~96 | **Rs 3,360** |
| Base (rev +13-14%, margin 14.5-15%) | ~125 | ~83 | 13% | ~114 | **Rs 3,990** |
| Bull (rev +17%, margin to 16%) | ~135 | ~89 | 17% | ~125 | **Rs 4,375** |

**SOM cross-check:** B10 SOM-implied 3-yr revenue CAGR 24.3% (upper-range, above audited 7.5%, capacity ceiling binds yr3+, gap Rs 633 Cr). My base polymer revenue CAGR ~13-14% sits WELL BELOW the SOM ceiling → **consistent** (assumption is conservative against the runway, not stretched to it).

**FTTCP-consistency row:** Year-3 ROCE assumption (sustained premium, 60-67% segment) is consistent with the FIRING verdict used in Pillar 1. Margin-led EBIT growth is conservative vs the Q1 FY27 17.1% run-rate (14.5% then 15.0% assumed). Pass.

### 2.4 Fair value — Business A, 3-year hold (both tracks identical at 35x)

Target = 35x × FY30 EPS. Entry = target ÷ 1.953 (Tier A, 25%). MoS = 20% below entry.

| Case | FY30 target (per share) | Entry (÷1.953) | MoS (−20%) |
|---|---|---|---|
| Bear | Rs 3,360 | Rs 1,721 | Rs 1,377 |
| Base | Rs 3,990 | Rs 2,043 | Rs 1,634 |
| Bull | Rs 4,375 | Rs 2,240 | Rs 1,792 |

Illustrative equity value TODAY (35x × FY27 PAT 125) = **~Rs 4,375 Cr**, rising toward the FY30 base target of ~Rs 6,045 Cr equity.

### 2.5 Hurdle Ratio — Business A (at imputed CMP)

The polymer business is not separately quoted. Imputed price = whole company Rs 3,549 Cr − agri base ~Rs 180 Cr = **~Rs 3,370 Cr** → on FY27 PAT Rs 125 Cr = **~27x forward PE**; per-share imputed ~Rs 2,224.

- **HR(Base) = (1 + 0.13)³ × (35 / 27) = 1.443 × 1.296 = 1.87.** Below 1.953.
- Bull EPS CAGR for the HR check: grade is **C**, so bull is capped at Base + 5% = **18%** (not the modelled 17%; use the lower of the two → 17-18%). HR(Bull) = (1.18)³ × (35/27) = 1.643 × 1.296 = **2.13.** Passes.
- **Verdict: CONDITIONAL** — base fails, bull passes. Flag "growth-dependent with de-rating headwind"; verdict capped at WATCHLIST / BUY-ON-DIPS; no BUY NOW. Clears 25% comfortably on a 12-15% dip or on the first standalone accounts confirming the 67.5% return.

### 2.6 Decision — Business A

CMP-imputed ~Rs 2,224 sits ~9% above the base entry Rs 2,043 and ~15% above on the whole-share CMP Rs 2,342. HR CONDITIONAL caps the verdict. **DECISION: WATCHLIST** (DEEP WATCH at zone; BUY-on-dips on a 6-15% pullback or first standalone polymer accounts). Entry zone Rs 2,043, MoS Rs 1,634.

---

## 3. BUSINESS B — AGRI (P&K Fertilizers + Agri Nutrients, demerges as Jubilant Agri Solutions Ltd)

Subsidy-linked commodity cyclical. FY26 revenue Rs 692.34 Cr (P&K Fert 681.19 + Agri Nuts 11.15, Note 39 p.150), a placement PEAK (P&K Fert swung +Rs 57.17 Cr from the FY25 loss). Q1 FY27 EBIT fell 62% YoY on a weak monsoon. Valued on NORMALIZED mid-cycle earnings, NOT the FY26 peak.

### 3.1 Section 1B Four-Pillar Worksheet — Business B

| Step | Input (anchor) | Value |
|---|---|---|
| A. Pillar 1 base | ROCE **STAGNANT** (deliberation). Current ROCE 19.9% (Note 39 segment), normalized below the FY26 peak. Formula: 0.5×19.9 + 7.5 = **17.45 ≈ 17.5x** (floor 9x, cap 24x). Operator-approved base 17.5x. | 17.5x |
| — Pillar 1 normalization route | **NONE** — neither Route A nor Route B; verdict is STAGNANT (route barred on STAGNANT). | NONE |
| — ROCE recovery credited via | **not credited** (no recovery; STAGNANT). | not-credited |
| B. Pillar 2 cash multiplier | **0.80x**, STRUCTURAL (the >Rs 400 Cr NBS subsidy receivable; FY26 CFO/PAT 0.59x; +92.2% YoY subsidy surge). Structural → NO growth offset. | 0.80x |
| C. Quality-adjusted base | 17.5 × 0.80 | 14.0x |
| D. Pillar 3 / E. Strategic | commodity, no moat, no scarcity | +0x / +0x |
| F. Raw destination PE | 14.0 + 0 + 0 | 14.0x |
| F2. UA | **does NOT apply** — JASL is a fresh listing (<12m). No 1.25x. | 14.0x |
| G. Sector cap | **Agri processing 20x**, not binding. | 20x |
| **H. Destination PE** | min(14.0, 20) = **14.0x** on NORMALIZED earnings. Operator-approved band 14x-17.5x across the cycle. | 14.0x |

### 3.2 Track 1 RRM — Business B

Base r 14% (small-cap, cyclical, structural cash drag → durability Weak-Moderate, no downward adjustment). RRM = 1 + (13.5 − 14) × 0.12 = 1 − 0.06 = **0.94**. Track 1 destination = 14.0 × 0.94 = **13.2x**, within the approved 14x-17.5x band and below cap. Divergence vs Track 2 (14.0x) = ~6%, immaterial; the more conservative Track 1 (13.2x) would set the entry if agri were a compounder, but it is a value stub (below).

### 3.3 Earnings and fair value — Business B (normalized)

FY26 anchored (peak); FY27/FY28 projected. Normalized mid-cycle PAT ~Rs 16-18 Cr (vs Rs 23 Cr FY26 peak and a FY25 loss).

| Case | Normalized PAT | Multiple | Equity value | Per JASL share (1.515 Cr) |
|---|---|---|---|---|
| Bear (trough) | ~Rs 10 Cr | 12x | ~Rs 120 Cr | ~Rs 79 |
| Base | ~Rs 18 Cr | 14x | ~Rs 250 Cr | ~Rs 165 |
| Bull (near peak) | ~Rs 23 Cr | 17.5x | ~Rs 400 Cr | ~Rs 264 |

### 3.4 Hurdle Ratio and decision — Business B

Agri fails the 25% Tier A hurdle **by nature**: revenue grows 5-6%, earnings are cyclical, no growth premium. HR ≈ (1.03)³ × (14/14) ≈ **1.09 → STOP** as a 25% compounder. Consistent with FTTCP composite −2, AVOID, Kernex cash cap engaged. **DECISION: AVOID** as a transition-alpha buy — it is a value / monetization stub. Hold small if received in the demerger; sell into an agri up-cycle. Do not size on the polymer thesis.

---

## 4. BLENDED ENTITY (pre-demerger, JACPL as it trades today) — CONTEXT ONLY

Per operator direction the blended multiple is for the pre-demerger entity only; the SOTP is the primary lens.

| Step | Input | Value |
|---|---|---|
| Pillar 1 base | ROCE 36% (AR p.7) FIRING, route NONE. Formula: 24 + 0.3×(36−33) = **24.9x** | 24.9x |
| Pillar 2 cash | 1.15x, STRUCTURAL, located in demerging division | 1.15x |
| Quality-adjusted base | 24.9 × 1.15 | 28.6x |
| Strategic | +2x | +2x |
| Raw / F2 UA | 30.6x × 1.25 = 38.3x | 38.3x |
| Sector cap | **29.5x** revenue-weighted (62.7% at 35x + 37.3% at 20x), no quality uplift | 29.5x |
| **Destination PE (both tracks)** | min(38.3, 29.5) = **29.5x**; range 27.5x-31.5x | 29.5x |

Blended context HR: FY27 blended PAT ~140 Cr (polymer 125 + agri 15) → current PE 3,549/140 = 25.35x. HR = (1.12)³ × (29.5/25.35) = 1.405 × 1.164 = **1.64 → CONDITIONAL.** Consistent with the SOTP read.

---

## 5. COMBINED SUM OF THE PARTS

**Intrinsic fair value today** (destination PE on FY27 projected PAT):
- Polymer: 35x × Rs 125 Cr = **~Rs 4,375 Cr**
- Agri: 14x × ~Rs 18 Cr normalized = **~Rs 250 Cr**
- **SOTP fair value ~Rs 4,625 Cr** vs market cap **Rs 3,549 Cr → ~30% above CMP.** ~88% of value and essentially all of the undervaluation sit in the polymer business.

**25% CAGR (Tier A) entry basis** (what the strategy pays for a 25% 3-yr return):
- Polymer entry zone ~Rs 3,095 Cr (Rs 2,043/sh × 1.515 Cr)
- Agri ~Rs 250 Cr (no growth premium; value ≈ fair, not an entry discount)
- **Combined Tier A entry ~Rs 3,345 Cr** = ~Rs 2,208/sh. **CMP Rs 3,549 Cr sits ~6% ABOVE this entry.** Combined MoS (20% below entry) ~Rs 2,676 Cr = ~Rs 1,766/sh.

**Probability-weighted expected CAGR (grade C: 35/45/20), polymer claim at imputed CMP ~Rs 2,224:**
- Bear ~14.7% × 0.35 = 5.15 | Base ~21.5% × 0.45 = 9.68 | Bull ~25.3% × 0.20 = 5.06 → **~19.9%** expected CAGR. Below the 25% hurdle at current price; combined-package base ~21%. Confirms CONDITIONAL, not a current BUY.

**Risk-reward asymmetry:** in a 3-year hold even the bear FY30 polymer target (Rs 3,360/sh) sits above the CMP-imputed price, so the genuine downside is not a price floor but a **Samlaya-delay + de-rating** path: if forward polymer earnings do not hold and the multiple compresses toward ~20x on FY27 PAT 125 (~Rs 2,500 Cr → ~Rs 1,650/sh), that is ~30% drawdown. Base upside ~77% / ~30% drawdown ≈ **2.6x** — favorable, but time- and catalyst-dependent, not price-protected.

---

## 6. SHARED CATALYST AND SINGLE POINT OF FAILURE

**SHARED CATALYST — Samlaya (flagged).** The Samlaya adhesive plant (Phase 1 partial 03-Jun-2026; full run-rate end Q1 FY27; Phase 2 SBR latex end Q3 FY27) drives BOTH Business A revenue STARTING and Business A ROCE FIRING (B10 SHARED-CATALYST flag; deliberation §handoff). It is the same event carrying the forward earnings that back the 35x cap AND the ROCE quality that earns the Pillar 1 base.

**Stress test — Samlaya delay as single point of failure:** if Samlaya's full run-rate slips 2-4 quarters, FY27 polymer revenue misses ~Rs 1,367 Cr toward the bear ~+9% path, margin expansion stalls, and FY27 PAT lands nearer the bear ~Rs 112 Cr. The imputed forward PE re-rates against a lower E, and HR falls further below 1.953. This single delay simultaneously weakens revenue, margin and the ROCE-quality claim — the exact concentration the shared-catalyst flag exists to surface. Role 3 must treat it as one point of failure, not three independent risks.

**Single-credit compliance:** Business A ROCE is FIRING at the current 36-67.5% high — there is no recovery to credit, so Pillar 1 credits nothing on trajectory and the Strategic Premium's ROCE re-rating route stays barred. The +2x strategic premium is paid for **scarcity** (VP latex / PVAc leadership), a different lever than ROCE re-rating. No quality improvement is credited twice.

---

## 7. VERDICT CARD (dual track, SOTP)

**Tier: A | Hurdle: 25% | Method: SOTP**

| Field | Business A (Polymer) | Business B (Agri) | Combined SOTP |
|---|---|---|---|
| Destination PE (Track 2 additive) | 35.0x (32.5-35.0) | 14.0x | 29.5x blended (context) |
| Destination PE (Track 1 RRM) | 35.0x (cap binds) | 13.2x | 29.5x (cap binds) |
| Divergence | 0% (cap binds both) | ~6% | 0% |
| Cash multiplier | 1.15x (drag located in B) | 0.80x STRUCTURAL | 1.15x STRUCTURAL |
| UA applied | Yes (×1.25, capped) | No (fresh listing) | Yes (capped) |
| Sector cap | 35x specialty chemicals | 20x agri processing | 29.5x weighted |
| Fair value today | ~Rs 4,375 Cr | ~Rs 250 Cr | **~Rs 4,625 Cr (~30% > CMP)** |
| FY30 base target (per share) | Rs 3,990 | value stub | package ~Rs 4,155 |
| Hurdle Ratio | Base 1.87 / Bull 2.13 → **CONDITIONAL** | ~1.09 → **STOP** (by nature) | 1.64 → CONDITIONAL |
| Entry zone (per share) | Rs 1,634 (MoS) – Rs 2,043 | value ≈ fair | Rs 1,766 (MoS) – Rs 2,208 |
| Decision | **WATCHLIST** (BUY-on-dips) | **AVOID** (hold small if received) | **WATCHLIST** |

**Expected CAGR (prob-weighted, grade C):** ~20% at current price (below the 25% hurdle) → not a current BUY.

**Key valuation swing factors:** ▲ first standalone polymer accounts confirming ~67.5% ROCE and the Q1 adhesives acceleration (would move HR to PASS and confirm the 35x). ▼ Samlaya delay (shared catalyst) pulling FY27 PAT toward bear and de-rating the imputed multiple. ▼ input-cost spikes (sulphur/VAM/butadiene, peer-confirmed) compressing polymer margin. ▼ subsidy-receivable build in agri worsening the blended cash print pre-scheme.

**Exit framework:** target exit at the 35x polymer destination on realized standalone earnings; thesis-broken if retained-entity CFO:PAT <0.70x for a second consecutive quarter with the >6m subsidy bucket >8% (FLAG-CASH falsification), or if Samlaya full run-rate slips beyond Q3 FY27.

**ONE-LINE THESIS:** WATCHLIST JACPL at Rs 2,342 — the SOTP fair value ~Rs 4,625 Cr sits ~30% above the Rs 3,549 Cr market cap with ~88% in the retained polymer business (67.5% segment ROCE, VP-latex/PVAc scarcity, adhesives compounding high-teens), destination 35x specialty-chemicals cap on ~Rs 125 Cr FY27 forward PAT; but the imputed ~27x forward PE gives Hurdle Ratio 1.87 (CONDITIONAL, clears 25% only on bull earnings or a 12-15% dip), so it is a BUY-on-dips at zone, not a BUY now. Key risk: Samlaya delay is a single point of failure hitting revenue, margin and ROCE together; forward EPS is un-guided and built off one quarter that still contains the agri stub.

---

## 8. INPUT DISCIPLINE LOG

- **Un-guided forward earnings** (B10 forward_guidance MEDIUM): FY27/FY28 PAT are operator-engaged illustrative allocations per valuation-sotp.md; used as the approved earnings base, labelled provisional throughout. Not a general-knowledge fill.
- **No standalone accounts** (B10 standalone_accounts): per-entity PAT/ROCE/cash are illustrative allocations; stated explicitly.
- **rating_wc_quote NOT FOUND** (B10): cash multiplier 1.15x (A) / 0.80x (B) applied on the deliberation-approved structural determination; no rating-agency confirmation of persistent WC on the retained entity, so A stays 1.15x per deliberation.
- **unit_economics_mt_kg NOT FOUND**: unit-level validation of growth not performed; base revenue CAGR held conservative (~13-14%, below SOM 24.3%).
- Exit PE bases used EXACTLY as operator-approved (A 35x, B 14x, blended 29.5x). No independent re-derivation overrode the approved bases; the independent four-pillar math reproduces them (A raw 36.5x → cap 35x; B raw 14.0x).
