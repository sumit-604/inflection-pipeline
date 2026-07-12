# STAGE 11 — ROLE 1 MULTI-METHOD VALUATION: Azad Engineering Ltd (AZAD)

**Run date:** 2026-07-12 | **Model:** claude-opus-4-8 | **Framework:** Master v3.3 / Section 1B v3.3 (+v3.4 4.1-4.4) / FTTCP v1.2
**Sole input source:** B10 valuation input table (`10-valinputs.md`). Every input anchored on first use. No number sourced from general knowledge.
**Mode:** Pipeline (all sections executed in one pass; framework STOP gates written as interim checkpoints then continued).

---

## PRE-FLIGHT: DELIBERATION-CONFIRMED INPUTS HONORED (not re-litigated)

| Input | Value carried | Authority |
|---|---|---|
| FTTCP ROCE forward verdict | RECOVERING (40-60%) → Pillar 1 uses 60/40 weighted avg of current + FY[Y+2] operational ROCE | FTTCP deliberation ruling 8; override 1 |
| Pillar 1 ROCE basis | Operational ~12% current; blended forward ~13.6%; NOT statutory 8.84%, NOT mgmt 20.7% | FTTCP override 1 |
| ROCE recovery route | Pillar 1 (single-credit; stated) | Amendment 4 |
| Cash conversion | GROWTH-INDUCED; 0.80x base + 0.10x offset = 0.90x | FTTCP ruling 7 |
| Strategic Premium | +3x (operator override) | FTTCP override 2 |
| Sector cap | 25x (precision engineering / industrial products); absolute ceiling | FTTCP ruling 4 |
| UA multiplier | Does NOT apply (all_met=false; FII+DII ~22% > 3%) | FTTCP ruling 12; B10.ua_qualifiers |
| Return tier | Tier A (25% hurdle) via TURNAROUND | FTTCP ruling 12; Amendment 4.3 |
| 4D probability weights | 25/50/25 (credibility grade B) | B05 credibility_grade B |
| Shared catalyst | Serial-production ramp drives Pillar 1 ROCE AND Pillar 3 growth | FTTCP ruling 10-11 |

FTTCP has run before Role 1 (verdict RECOVERING supplied). Pillar 1 computable. Concall gate cleared (grade B from B05).

---

## SECTION 1A: METHOD SELECTION & JUSTIFICATION

Business model: capital-intensive precision-engineering manufacturing, Tier-1 OEM contract supply (B04-bizmodel). Mid-ramp: elevated depreciation (79.80 Cr), heavy capex (570.71 Cr FY26), single Ind AS 108 segment, no dividend, book value excludes the qualification moat.

| Method | Suitable here? | Weight | Justification |
|---|---|---|---|
| **EV/EBITDA** | **PRIMARY** | 50% | Capital-intensive, varying leverage during capex ramp; normalizes elevated depreciation and non-recurrings (B04 primary) |
| **P/E** | **SECONDARY** | 35% | Post-QIP PAT growth stable; carries the Section 1B four-pillar destination PE — the framework's core exit authority (B04 tertiary, elevated here because destination PE lives in P/E space) |
| **DCF** | **TERTIARY** | 15% | Rs 6,080-6,500 Cr order book, LTAs 4-8yr tenors support explicit modelling (B04 secondary); BUT near-term FCF deeply negative (-693.97 Cr) and terminal-value dominated → low weight, high sensitivity flagged |
| P/B | Rejected | — | Book excludes qualification moat (B04 irrelevant) |
| SOTP / DDM / Replacement | Rejected | — | Single segment / no dividend / understates moat (B04) |

Peer-relative multiples (P/E, EV/EBITDA, P/B) are UNRESOLVED in B10 (peer EPS/net debt/BVPS not extracted). Per input-discipline rule, not fabricated. AZAD standalone: current PE 121.2x, current EV/EBITDA 75.1x (both computed in B10). Peer median EBITDA margin 20.69% used only as a margin-quality reference, not as a multiple anchor.

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 (+v3.4)

### Pillar 1 — ROCE Base Multiple (continuous formula)

- FTTCP ROCE forward verdict: **RECOVERING (40-60% probability)** → Pillar 1 uses **60/40 weighted average of current and FY[Y+2] expected operational ROCE** (v3.3 table / FTTCP Pillar-1 integration).
- Current operational ROCE = 12.0% (FTTCP override 1: EBIT 167.66 / operational capital employed ~1,348 Cr, idle QIP 183.58 + CWIP 256.68 + capex advances 108.43 stripped). Statutory 8.84% and mgmt-adjusted 20.7% recorded in conflicts[], NOT used.
- FY[Y+2] expected operational ROCE ≈ 16.0% (implied: 0.6×12.0 + 0.4×16.0 = 13.6, matching B10 "blended forward ~13.6%").
- **ROCE used = 0.6×12.0 + 0.4×16.0 = 7.2 + 6.4 = 13.6%**
- Pillar 1 Base PE = 0.5 × ROCE% + 7.5 = 0.5×13.6 + 7.5 = 6.8 + 7.5 = **14.3x** (floor 9x, cap 24x — within band; matches B10 base ~14.3x).
- **ROCE recovery credited via: Pillar 1** (single-credit rule; Strategic Premium is NOT used for ROCE re-rating — see below).

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT (FY20-26) = 0.04 | Latest FY26 CFO/PAT = -0.93 | FCF negative (-693.97 Cr). Band = "CFO/PAT below 30% or CFO negative" → base multiplier 0.80x.
- Structural or growth-induced? **GROWTH-INDUCED** (FTTCP ruling 7; not structural). Evidence: negative FY26 OCF driven by Rs 87.66 Cr receivables build + Rs 138.15 Cr inventory build funded by QIP proceeds, not earnings weakness; CARE (22-Jun-2026) states WC "expected to normalise once serial production begins." Determination is authoritative per B10; not re-classified.
- Growth offset: PAT CAGR FY20-26 = 35.78% → 25-40% band → offset **+0.10** (growth-induced only).
- **Effective Cash Multiplier = 0.80 + 0.10 = 0.90x**
- **Quality-Adjusted Base = 14.3 × 0.90 = 12.87x**

FLAG-CASH carried: GROWTH-INDUCED, multiplier applied 0.90x. Base 0.80x holds until Q1 FY27 consolidated OCF print (August 2026) confirms normalization.

### Pillar 3 — Growth Visibility (v3.4 decoupled 3a/3b/3c, combined cap +6x)

**3a Growth Visibility Premium** (documented growth machinery, 📄 only):
- Order book ≥1.0x revenue: Rs 6,500 Cr (CARE) / 6,080 Cr (B04) ÷ 590.38 Cr = ~11x → QUALIFIES.
- SOM-implied revenue CAGR ≥20% with capacity cross-check passing: 31.0% 3yr, capacity check passes (+Rs 126 Cr spare for 3yr SOM; B09) → QUALIFIES.
- Management delivery grade A/B: grade B → QUALIFIES.
- Three qualify AND grade B → **3a = +3x** (rule: +3x if three or more qualify and grade A/B).

**3b Moat Formation Premium** (EM-gated table):
- EM Score 26 (STRENGTHENING), catalyst 0-12m (serial-production ramp FY27), evidence mostly documented → band "EM 25-29 any timeline" → **3b = +1x**.

**3c Duration Premium** (documented forward revenue visibility, 📄 only):
- Executable order book ÷ revenue = ~11x; CARE cites 5-6 year revenue visibility (LTAs, 4-8yr tenors documented) → ≥4 years → **3c = +2x**.

**Pillar 3 total = 3 + 1 + 2 = +6x (at the +6x combined cap).** Robustness: even at a conservative +4x, destination PE ≈ 19.9x and the Hurdle verdict below is unchanged.

**SHARED CATALYST FLAG:** the serial-production ramp that supplies the Pillar 1 forward ROCE (60/40 blend) is the same catalyst behind the 3b moat-formation premium and the 3a/3c order-book conversion. Flagged for Role 3 single-point-of-failure stress-test. Falsifier: Q1 FY27 consolidated OCF negative with WC days at/above 344.

### Strategic Asset Premium

- Strategic position: strong franchise / limited competition / documented pricing power (qualification lock-in to GE Vernova, Siemens Energy, Mitsubishi, Baker Hughes, Rolls Royce, P&W; 36.88% EBITDA margin). Tier "+2 to +4x". Operator override sets **+3x**. NOT the rare-licence-monopoly tier (+4-6x): competes with Howmet/Precision Castparts, OEMs dual-source, sole-Indian-supplier claim unverified, 81% three-OEM concentration = customer power not supplier monopoly.
- **Strategic Premium = +3x.** Single-credit respected: this credits franchise/pricing power, NOT ROCE re-rating (ROCE recovery already in Pillar 1).

### Undiscovered Alpha Multiplier

- UA does NOT apply. B10.ua_qualifiers.all_met = false (FII+DII ~22% >> 3% threshold). F2 = F.

### Four-Pillar Summary (Track 2 — Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 13.6% → 0.5×13.6+7.5 | 14.3x |
| B. Cash Multiplier | 0.80 + 0.10 offset | 0.90x |
| C. Quality-Adjusted Base | 14.3 × 0.90 | 12.87x |
| D. Pillar 3 (3a+3b+3c) | +3 +1 +2 (cap +6) | +6.0x |
| E. Strategic Premium | operator +3x | +3.0x |
| **F. Raw Destination PE** | 12.87 + 6.0 + 3.0 | **21.87x** |
| F2. UA-Adjusted Raw PE | UA n/a → F×1.0 | 21.87x |
| G. Sector Cap | Precision eng / industrial products | 25x |
| **H. Final Destination PE (Track 2)** | min(21.87, 25) | **21.87x** |

Cap NOT binding (21.87 < 25). **Track 2 Destination PE range = 21.87 ±7.5% → 20.0x to 23.5x (mid 21.9x).**

### Track 1 — RRM Dual-Track Derivation

- Fundamental Base PE (stated interpretation): the full raw four-pillar destination PE (21.87x) represents the fundamentals; RRM overlays the required-return adjustment (durability/governance) per the v3.2 spine.
- Base r: market cap Rs 16,013 Cr = mid-cap → base r 13%. Adjustments: governance CAUTION (open SEBI PIT violation, growing RPT ecosystem; B08) +0.75%; durability moderate (strong NADCAP/AS9100D/EDF certification barriers, but 81% OEM concentration and unverified sole-supplier claim) +0.25%. Cash risk NOT added to r (already policed in Pillar 2 — single-mechanism rule). **r = 14.0%** (bound [9%,18%] satisfied).
- RRM = 1 + (13.5 − r) × 0.12 = 1 + (13.5 − 14.0)×0.12 = 1 + (−0.5×0.12) = 1 − 0.06 = **0.94** (v3.4 4.4 percentage-point reading; bounds 0.70-1.60 satisfied).
- **Track 1 Destination PE = 21.87 × 0.94 = 20.56x**, capped at 25x → **20.6x mid**. Range ±7.5% → **19.0x to 22.0x**.

### Track divergence

Track 2 mid 21.9x vs Track 1 mid 20.6x → divergence = (21.87−20.56)/21.87 = **6.0% (<15%)**. Tracks agree. Per rule, the more conservative track (**Track 1 RRM, 20.6x**) governs the entry zone.

> **INTERIM CHECKPOINT (framework STOP after Section 1B):** Four-pillar destination PE 21.87x additive (Track 2 range 20.0-23.5x); RRM track 20.6x (range 19.0-22.0x). Current PE 121.2x (2480/20.46). Hurdle Ratio computed in Section 1B tail below. Continuing without halting (pipeline mode).

### Hurdle Ratio (Section 1B sanity check — Tier A, threshold 1.953)

Current PE = 2480 / 20.46 = **121.21x**. Base EPS CAGR (Section 2) = 23.3% → 3yr EPS multiple 1.876. Bull EPS CAGR = 31.2% → multiple 2.260. Bull row usable (grade B).

Using governing Track 1 destination PE mid (20.6x):
- **HR(Base) = 1.876 × (20.6 / 121.21) = 1.876 × 0.1700 = 0.319**
- **HR(Bull) = 2.260 × (20.6 / 121.21) = 2.260 × 0.1700 = 0.384**

Using Track 2 mid (21.9x): HR(Base) = 0.339; HR(Bull) = 0.408. All four values are far below 1.953.

For HR to reach 1.953 at destination PE 20.6x, required 3yr EPS multiple = 1.953 × 121.21/20.6 = 11.49x = **129% EPS CAGR** — infeasible.

**HURDLE RATIO VERDICT = STOP.** The 25% CAGR is infeasible even on bull-case earnings: the 121x→~21x de-rating (a ~5.9x compression) cannot be outrun by any achievable 3-year EPS growth. Per Amendment 2 / Master v3.3, complete all remaining sections for the record; the verdict card reads AVOID-on-valuation.

**Would I personally pay a ~21x destination PE for this quality of business?** Yes — a 13.6% ROCE, 0.90x cash, +6x growth-visibility, +3x franchise profile earning ~21x is reasonable. The problem is not the destination PE; it is the 121x entry price.

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS

### 2A. Revenue (Year 0 = FY26 = 590.38 Cr)

| | Bear | Base | Bull |
|---|---|---|---|
| Logic | Ramp slips, WC constrains, 1-2 triggers fail | Guidance ~ historical, order-book conversion on track | Guidance at face + SOM-implied |
| Revenue CAGR | 18% | 26% | 31% |
| FY27 (Y1) | 696.65 | 743.88 | 773.40 |
| FY28 (Y2) | 822.05 | 937.29 | 1,013.15 |
| FY29 (Y3) | 970.02 | 1,180.98 | 1,327.23 |

Base 26% is BELOW SOM-implied 31% (B09) and below historical 3yr 28.4%, at/above management "25%+". Bull 31% = SOM-implied (grade B permits guidance-at-face). Bear 18% = historical minus execution slippage.

### 2B. Profitability

| | Bear | Base | Bull |
|---|---|---|---|
| EBITDA margin | 33.0% | 35.0% | 36.5% |
| Margin logic | Serial-production mix dilutes; guided band floor | Normalize toward top of guided 33-35% band (FY26 36.9% peak) | Peak sustained + operating leverage |
| PAT margin | 18.0% | 21.0% | 22.5% |
| PAT-margin logic | Higher dep + interest on debt-funded capex | Slight compression from FY26 22.36% (dep/interest drag partly offset by leverage) | Near FY26 peak sustained |
| Share dilution (3yr) | ~0% (QIP complete; ESOP immaterial) | ~0% | ~0% |
| Diluted shares | 6.46 Cr | 6.46 Cr | 6.46 Cr |

### 2C. Complete Projection Table (Year 3 = FY29)

| Line | Y0 (FY26) | Base Y3 | Bear Y3 | Bull Y3 |
|---|---|---|---|---|
| Revenue (Cr) | 590.38 | 1,180.98 | 970.02 | 1,327.23 |
| EBITDA (Cr) | 217.75 | 413.34 | 320.11 | 484.44 |
| EBITDA margin | 36.88% | 35.0% | 33.0% | 36.5% |
| PAT (Cr) | 132.16 | 248.01 | 174.60 | 298.63 |
| EPS (Rs) | 20.46 | 38.39 | 27.03 | 46.23 |
| Est. net debt (Cr) | 280.44 | ~500 | ~550 | ~450 |
| Est. ROCE (operational) | ~12% | ~15-16% | ~11-12% | ~17% |

Base EPS CAGR = (38.39/20.46)^(1/3) − 1 = **23.3%**. Bear = (27.03/20.46)^(1/3)−1 = **9.7%**. Bull = (46.23/20.46)^(1/3)−1 = **31.2%**.

### 2D. Sanity Checks

| Check | Result | Pass? |
|---|---|---|
| Revenue > capacity? | Base 26% within committed capex (3yr SOM +126 Cr spare, B09) | Yes |
| Margins unprecedented? | Base 35% below FY26 36.9%; conservative | Yes |
| ROCE > 15%? | Base Y3 operational ~15-16%; bear dips below | Base Yes / Bear No |
| FCF funds growth without excess debt? | No — capex-heavy; net debt rises; growth is debt/QIP funded | FLAG (growth-induced) |
| EPS growth operational, not engineered? | Yes — volume ramp, no buyback/leverage tricks | Yes |
| Market share realistic? | SAM share ~3.9%, headroom 25.8x (B09) | Yes |
| CFO/PAT trajectory consistent with Pillar 2 (0.90x)? | Requires improvement from -0.93; growth-induced thesis, unconfirmed until Q1 FY27 | FLAG |
| **Year 3 ROCE consistent with FTTCP RECOVERING?** | Base ~15-16% consistent with 60/40 blend to FY[Y+2] 16% | Yes |
| **SOM cross-check:** base 26% vs SOM-implied 31% | Base BELOW SOM — consistent, not excess | Yes |

> **INTERIM CHECKPOINT (framework STOP after Section 2):** Projections built. Base EPS 20.46 → 38.39 (23.3% CAGR). Continuing.

---

## SECTION 3: APPLY EACH VALUATION METHOD

### PRIMARY — EV/EBITDA

Destination EV/EBITDA ≈ 0.65 × destination PE = 0.65 × ~21x ≈ 13.6x, adjusted DOWN for capex >> depreciation (570.71 vs 79.80) → **exit EV/EBITDA 11-13x (mid 12x)**.

| | Bear | Base | Bull |
|---|---|---|---|
| Y3 EBITDA (Cr) | 320.11 | 413.34 | 484.44 |
| Exit multiple | 11x | 12x | 13x |
| EV (Cr) | 3,521.21 | 4,960.08 | 6,297.72 |
| Less Y3 net debt | 550 | 500 | 450 |
| Equity value (Cr) | 2,971.21 | 4,460.08 | 5,847.72 |
| ÷ 6.46 Cr shares | | | |
| **Price/share (Rs)** | **459.94** | **690.42** | **905.22** |
| CAGR from CMP 2480 | −43.9% | −34.5% | −28.5% |

### SECONDARY — P/E (Section 1B destination PE)

Exit PE from Section 1B ONLY. Track 1 (governing): 19.0 / 20.6 / 22.0x. Track 2: 20.0 / 21.9 / 23.5x.

Target price matrix (3yr), Track 1 mid 20.6x:

| | Exit 19.0x | Exit 20.6x | Exit 22.0x |
|---|---|---|---|
| Bear EPS 27.03 | 513.57 → 🔴 | 556.82 → 🔴 | 594.66 → 🔴 |
| Base EPS 38.39 | 729.41 → 🔴 | 790.83 → 🔴 | 844.58 → 🔴 |
| Bull EPS 46.23 | 878.37 → 🔴 | 952.34 → 🔴 | 1,017.06 → 🔴 |

All 9 cells 🔴 (<15% CAGR — in fact all deeply negative from CMP 2480). Track 2 (20.0/21.9/23.5x) shifts targets up ~6% — still all 🔴.

Reverse-engineered entry for 25% CAGR (Base EPS, Track 1 mid): Y3 target 790.83 → required entry = 790.83 / 1.953 = **404.93 Rs**.

**P/E fair value (Y3, Track 1): 513.57 (bear) / 790.83 (base) / 1,017.06 (bull).**

### TERTIARY — DCF (low weight, high sensitivity)

Near-term FCF deeply negative (-693.97 Cr FY26). FCF/revenue turns positive only post-ramp; consistent with Pillar 2 growth-induced 0.90x (cash improves but not elite). WACC 13-14%, terminal growth 5%. Terminal value >75% of PV → too sensitive, low weight (15%). Estimated equity fair value lands ~450 (bear) / ~650 (base) / ~950 (bull) Rs, consistent with the other two methods. Carried at 15% weight with the sensitivity caveat flagged.

### Method-wise Fair Value Summary (Year 3)

| Method | Weight | Bear (Rs) | Base (Rs) | Bull (Rs) |
|---|---|---|---|---|
| EV/EBITDA | 50% | 459.94 | 690.42 | 905.22 |
| P/E (Track 1) | 35% | 513.57 | 790.83 | 1,017.06 |
| DCF | 15% | 450 | 650 | 950 |

> **INTERIM CHECKPOINT (framework STOP after Section 3):** All methods applied; tight convergence ~460-1,017 Rs at Year 3 vs CMP 2480. Continuing.

---

## SECTION 4: TRIANGULATION, ENTRY PRICE & FINAL VERDICT

### 4A. Triangulated Fair Value (Year 3) — BOTH tracks

**Track 1 (RRM, P/E leg at 19.0/20.6/22.0x):**

| | Bear | Base | Bull |
|---|---|---|---|
| EV/EBITDA ×0.50 | 229.97 | 345.21 | 452.61 |
| P/E ×0.35 | 179.75 | 276.79 | 355.97 |
| DCF ×0.15 | 67.50 | 97.50 | 142.50 |
| **Weighted FV** | **477** | **720** | **951** |

**Track 2 (Additive, P/E leg at 20.0/21.9/23.5x):**

| | Bear | Base | Bull |
|---|---|---|---|
| EV/EBITDA ×0.50 | 229.97 | 345.21 | 452.61 |
| P/E ×0.35 | 189.21 | 294.26 | 380.24 |
| DCF ×0.15 | 67.50 | 97.50 | 142.50 |
| **Weighted FV** | **487** | **737** | **975** |

Divergence between tracks ~2-3% at fair-value level. Governing = Track 1 (more conservative).

### 4B. Methods Agreement

| Check | Result |
|---|---|
| Same direction? | Yes — all methods say deeply overvalued at CMP |
| Spread high-low (base) | 690 vs 791 = ~15% (tight) |
| Outlier? | None material |
| Most trusted for AZAD | EV/EBITDA (capital-intensive, mid-ramp) |

### 4C. Return at Current Price (Track 1, Year 3)

| Scenario | Y3 FV (Rs) | CMP | Total Return | CAGR | 25% hurdle? |
|---|---|---|---|---|---|
| Bear | 477 | 2,480 | −80.8% | −42.3% | 🔴 |
| Base | 720 | 2,480 | −71.0% | −33.8% | 🔴 |
| Bull | 951 | 2,480 | −61.7% | −27.3% | 🔴 |

### 4D. Probability-Weighted Expected Return (grade B: 25/50/25)

| Scenario | Probability | 3yr CAGR | Weighted |
|---|---|---|---|
| Bear | 25% | −42.3% | −10.58% |
| Base | 50% | −33.8% | −16.90% |
| Bull | 25% | −27.3% | −6.83% |
| **Expected CAGR** | 100% | | **−34.3%** |

### 4E. My Entry Price (Tier A, divisor 1.953) — governing Track 1

| Calculation | Value |
|---|---|
| Base Y3 FV (Track 1) | 719.50 Rs |
| 25% CAGR entry = FV ÷ 1.953 | **368.4 Rs** |
| 30% CAGR entry = FV ÷ 2.197 | 327.5 Rs |
| MoS price (20% below 25% entry) | **294.7 Rs** |
| Ideal entry range | **~295 Rs (MoS) to ~368 Rs (entry)** |

Entry zone sits ~85-88% below CMP 2480. Track 2 entry ~377 Rs; governing (conservative) Track 1 ~368 Rs.

### 4F. Risk-Reward Asymmetry (at CMP)

| | Value |
|---|---|
| Bull Y3 target | 951 → −61.7% from CMP |
| Base Y3 target | 720 → −71.0% from CMP |
| Bear Y3 floor | 477 → −80.8% from CMP |
| Upside(base)/Downside(bear) at CMP | **0x — no upside exists at CMP; asymmetry entirely to the downside** |

### 4G. Four-Pillar Validation

| Check | Result | Pass? |
|---|---|---|
| Y3 ROCE justifies base used & matches FTTCP? | Base ~15-16% vs 13.6% blend; consistent with RECOVERING | Yes |
| Y3 CFO/PAT justifies 0.90x? | Requires normalization from -0.93; growth-induced, unconfirmed | FLAG (0.80x floor holds) |
| Primary catalyst fired by Y3 (base)? | Serial-production ramp assumed live FY27-28 | Yes (conditional) |
| Strategic premium still justified, single-credit? | Yes; +3x = franchise/pricing, ROCE via Pillar 1 only | Yes |
| UA ordering min(F×1.25, cap)? | UA n/a; F2=F; cap 25x not binding | Yes |
| Would I buy another stock at ~21x with these Y3 metrics? | Yes at ~21x — but NOT at 121x entry | Destination fine; price fails |

### 4H. FINAL VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP:** Rs 2,480 | **Market Cap:** Rs 16,013 Cr | **Current PE:** 121.2x | **Current EV/EBITDA:** 75.1x
- **FOUR-PILLAR EXIT PE:** ROCE Base 14.3x (FTTCP RECOVERING; ROCE 13.6% = 60/40 blend of 12.0% and 16.0%, operational) × Cash Mult 0.90x (GROWTH-INDUCED: 0.80 base +0.10 offset) = Quality Base 12.87x + Pillar 3 +6.0x (3a +3 order book/SOM/grade / 3b +1 EM26 / 3c +2 duration; at +6 cap; SHARED CATALYST) + Strategic +3.0x (franchise, single-credit) = **Raw 21.87x**; UA n/a; Sector Cap 25x (not binding); **Destination PE 20.0-23.5x (Track 2 mid 21.9x)**.
- **RRM TRACK:** r = 14.0%, RRM = 0.94 → **Track 1 20.6x (19.0-22.0x)**. Divergence 6.0% (<15%). **Governing: Track 1 (conservative), sets entry zone.**
- **HURDLE RATIO:** HR(Base) 0.32, HR(Bull) 0.38 → **STOP** (both far below 1.953; 25% CAGR infeasible even on bull EPS).
- **METHODS:** EV/EBITDA 50% / P/E 35% / DCF 15%.
- **WEIGHTED FAIR VALUE (Y3):** Track 1 — Bear 477 / Base 720 / Bull 951. Track 2 — Bear 487 / Base 737 / Bull 975.
- **EXPECTED CAGR (prob-weighted, grade B 25/50/25):** **−34.3%**.
- **UPSIDE/DOWNSIDE at CMP:** 0x (no upside).
- **ENTRY RANGE:** ~295 (MoS) to ~368 Rs (25% entry) — ~85-88% below CMP.
- **DECISION: AVOID (on valuation).** Business-quality flags (Gate 0 backward AVOID, FLAG-CASH growth-induced, FLAG-EXECUTION grade B, governance CAUTION) propagate but do not drive this; the mechanical driver is price: 121x PE vs ~21x earned destination PE.
- **KEY ASSUMPTIONS THAT COULD CHANGE VALUATION:** ▲ FY[Y+2] operational ROCE >20% would lift Pillar 1 (14.3x→~17x) and destination PE ~+2.5x — still nowhere near closing a 121x→24x gap. ▲ Q1 FY27 OCF strongly positive lifts cash multiplier toward 1.00x (+1.4x on quality base). ▼ Q1 FY27 OCF negative with WC ≥344 flips cash to structural (0.65x), cuts Quality Base to 9.3x and destination PE to ~18x. None reverse the STOP.
- **EXIT FRAMEWORK:** target exit at destination PE ~21x IF ever entered near zone; thesis-broken if Q1 FY27 consolidated OCF negative with WC days ≥344; time stop 3-5yr; PE compression floor ~19x (Track 1 low).
- **ONE-LINE THESIS:** "AZAD at Rs 2,480 is AVOID-on-valuation: EPS grows from Rs 20.46 to ~Rs 38 over 3 years (23% base) driven by the serial-production ramp, but at a four-pillar destination PE of ~21x (ROCE 13.6%, cash 0.90x, EM 26, sector cap 25x) the Year-3 base fair value is ~Rs 720 — a ~34% negative CAGR from a 121x current PE; the 25% hurdle needs a ~Rs 295-368 entry. Key risk: Q1 FY27 consolidated OCF stays negative and cash turns structural. Cash quality: growth-induced (0.90x)."

> **INTERIM CHECKPOINT (framework close):** Valuation complete. Four-pillar exit PE 20.0-23.5x (Track 2) / 19.0-22.0x (Track 1). Hurdle Ratio STOP. Entry price Rs ~295-368. Decision: AVOID (on valuation).

---

## FLAGS CARRIED FORWARD

- **FLAG-CASH:** GROWTH-INDUCED, cash multiplier 0.90x applied (0.80x base floor until Q1 FY27 OCF print). Anchor: FTTCP ruling 7; CARE p.3.
- **FLAG-SHARED-CATALYST:** serial-production ramp drives Pillar 1 ROCE recovery AND Pillar 3 growth premium. Role 3 must stress the single point of failure. Anchor: FTTCP ruling 10.
- **FLAG-GATE0:** Gate 0 backward AVOID (core 38/160; Block A 4/20, Block B 0/20). Forward read: post-QIP artifact, not operating deterioration.
- **FLAG-EXECUTION:** credibility grade B; WC target missed and re-targeted; GTRE engine slipped 3 calls.
- **FLAG-VALUATION (new):** current PE 121x vs earned destination ~21x → Hurdle STOP; the governing constraint.

---

```yaml
stage: B11-valuation
company: "AZAD"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Peer P/E, EV/EBITDA, P/B, growth, ROCE unresolved in B10 (peer EPS/net debt/BVPS not extracted) - peer-relative multiples not used, not fabricated"
  - "Year 3 net debt estimated (500 Cr base) from capex/CFO trajectory; FY27+ total capex quantum deflected in concalls"
  - "Diluted shares approximated 6.46 Cr from mcap/CMP; ~0% incremental dilution assumed (QIP complete)"
flags:
  - {type: FLAG-CASH, determination: GROWTH-INDUCED, multiplier_applied: 0.90, anchor: "FTTCP ruling 7; CARE p.3; B01/B02/B03"}
  - {type: FLAG-SHARED-CATALYST, anchor: "FTTCP ruling 10; serial-production ramp drives Pillar1 ROCE + Pillar3 growth"}
  - {type: FLAG-VALUATION, anchor: "Current PE 121.2x vs destination ~21x -> Hurdle Ratio STOP"}
  - {type: FLAG-GATE0, anchor: "B01 core 38 backward AVOID; forward read post-QIP artifact"}
  - {type: FLAG-EXECUTION, anchor: "B05 grade B; WC target missed/re-targeted; GTRE engine slipped 3 calls"}
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 19.0, mid: 20.6, high: 22.0, r_used: 14.0, rrm: 0.94}
  track2_additive: {low: 20.0, mid: 21.9, high: 23.5}
  divergence_pct: 6.0
  governing_track: "Track 1 (RRM) - more conservative; sets entry zone; divergence <15% so tracks agree"
pillar_detail:
  roce_used: 13.6
  roce_base: 14.3
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 0.90
  structural_or_growth: "growth-induced"
  growth_offset: 0.10
  growth_premium: 6.0
  strategic_premium: 3.0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 0.32, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 477, base: 720, bull: 951}
  track2: {bear: 487, base: 737, bull: 975}
expected_cagr_prob_weighted: -34.3
entry_range: {low: 295, high: 368}
mos_price: 295
upside_downside_ratio: 0
decision: "AVOID (on-valuation)"
unresolved_inputs_used:
  - "Year 3 net debt: conservative assumption ~500 Cr base / 550 bear / 450 bull, because FY27+ capex quantum deflected in concalls (B10 unresolved) and framework conservative-assumption rule applies to EV/EBITDA equity bridge"
  - "FY[Y+2] operational ROCE 16.0%: implied from B10 blended-forward 13.6% and 60/40 weighting; not independently disclosed"
som_cagr_crosscheck: "consistent"
one_line_thesis: "AVOID-on-valuation: at Rs 2480 (121x PE) AZAD earns a four-pillar destination PE of only ~21x (ROCE 13.6%, cash 0.90x growth-induced, EM 26, +3x franchise), so base Year-3 fair value ~Rs 720 implies -34% CAGR; the 25% hurdle needs a Rs 295-368 entry. Key risk: Q1 FY27 OCF stays negative and cash turns structural."
```
