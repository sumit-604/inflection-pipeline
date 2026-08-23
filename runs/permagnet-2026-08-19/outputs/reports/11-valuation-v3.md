# 11-VALUATION v3 — PERMANENT MAGNETS LTD (PERMAGNET)

**Stage 11 | Role 1 v2 SURGICAL RECOMPUTE | Run: runs/permagnet-2026-08-19 | Model: claude-opus-4-8**
**Framework basis: Master v3.6 (Role 1) / Section 1B v3.3 + v3.5.1 + v3.6 + v3.7 (later layers govern overlaps) / FTTCP v2.1**
**CMP Rs 882 (screener.in, 20-Aug-2026) | Shares 85,98,453 = 0.8598 Cr (AR-FY26 equity note p.106/EPS note p.107)**

> **VERSIONED RE-RUN NOTICE.** This file supersedes the committed 19-Aug records
> (`outputs/reports/B11-valuation.md`, `outputs/blocks/B11-valuation.yaml`) on TWO axes only:
> (1) the operator-approved Reading-2 exit-PE base (additive 19.6x / RRM 16.1x, from
> `fttcp-v2-deliberation.md` Section 5), and (2) the operator option-slice inputs (dossier Section 6).
> The 19-Aug records stay committed and untouched. Method, SOTP shape, bridge logic and hurdle machinery
> carry forward; the exit-PE base and option inputs are replaced.

---

## 0. AUTHORITY & CONSUMPTION NOTE

The destination multiple and earnings basis are OPERATOR-APPROVED at the FTTCP pillar gate
(`fttcp-v2-deliberation.md` Section 5, sign-off 23-Aug-2026). This stage does NOT re-derive the four
pillars. It APPLIES the approved base in a dual-track sum-of-the-parts and builds the option slices from
the operator inputs.

- **Destination PE (approved, applied exactly):** ADDITIVE **19.6x** (band 19.1-19.6x) / RRM **16.1x**
  (band 15.7-16.1x). Additive is the primary destination; RRM sets the entry zone (deliberation).
- **Pillar arithmetic (approved):** Pillar 1 core ROCE ex-QMPL **16.5%** (band 15.6-16.5%), route NONE
  → base PE **15.7x** (Amendment 11: 0.5 × 16.45 + 7.5). Pillar 2 cash **1.00x** (growth-induced).
  Pillar 3 **+0x** (Amdt 16 gate OPEN but HELD by operator, single-credit). Strategic **+0x**.
  UA **×1.25** (all 3 qualifiers). Sector cap Cables/Industrial products 25x (non-binding; 19.6x < 25x).
  Additive = 15.7 × 1.00 × 1.25 = **19.6x**; RRM = 19.6 × 0.82 = **16.1x** (r = 15.0%, RRM = 0.82).
- **Earnings basis:** ONE-YEAR-FORWARD on FY27 core operating EPS ~Rs 22.9 (grade-C build, reused from
  the 19-Aug Section 3 conservative projection).
- **Independent-read reconciliation (required, one line):** my Pillar read concurs — 0.5 × 16.45 + 7.5 =
  15.73 → 15.7x; ×1.25 = 19.63 → 19.6x; ×0.82 = 16.09 → 16.1x. No divergence from the approved base.

**Converter classification (v3.7 Amendment 17.0), stated upfront.** The CORE (meters, CTs, auto sensing,
gas, commercialised alloys) is **NON-CONVERTER** (FTTCP deliberation ruling; qualification lock-in plus
formulation IP — in-housed nano-crystalline cores — defend the spread; 17.1-17.4 do not bind). The RELAY
line is **NON-CONVERTER** (build-to-spec meter component, same qualification moat). The **NdFeB (Quantum
Magnetics) slice is CONVERTER**: primary RM is traded rare-earth, pricing is spread/commodity, no
formulation IP, 5-6 expected competitors (dossier V6/S6, mental-model declaration). Amendment 17 therefore
bars the core quality multiple from the NdFeB slice; that slice is valued at a converter exit PE (Section 3).

**Interim checkpoints logged (framework STOP points, not halted):** Section 1B → destination 19.6x /
16.1x. Section 2 → FY27 core operating earnings reused (grade-C). Section 3 → dual-track SOTP built.
Section 4 → Hurdle STOP, decision AVOID-on-valuation.

---

## 1. SECTION 1A — METHOD SUITABILITY MATRIX

| Method | Suitability | Weight | Justification |
|---|---|---|---|
| **SUM-OF-THE-PARTS (SOTP)** | PRIMARY | 100% | Operator-mandated shape. One earning core plus two pre-commercial optionality lines (relay, NdFeB) with different risk profiles and different economics. A single blended multiple would either overpay the pre-revenue slices or bury the option value. |
| P/E on forward core operating EPS × Section 1B destination PE | core-slice engine | — | Approved earnings basis is one-year-forward operating EPS; Section 1B is the sole exit-multiple authority. |
| Probability-weighted real-option value | option-slice engine | — | Relay and NdFeB are pre-commercial / pre-revenue; not in FY27 core earnings; each priced as an option (revenue × margin × probability × exit PE × PV). |
| EV/EBITDA, DCF | context only | 0% | Consolidated FCF is negative (−Rs 25.75 Cr, driven by subsidiary CWIP); DCF is unreliable and would double-count the NdFeB option capex. EV/EBITDA folds the subsidiary drag into the core. Both rejected as primary. |

Two applied methods (core P/E and option valuation) triangulate inside the SOTP; the SOTP is the primary,
weighting 100%. Do NOT price as one blended multiple (operator mandate; CLAUDE.md non-negotiable).

---

## 2. SECTION 1B — FOUR-PILLAR WORKSHEET (APPROVED BASE, APPLIED NOT RE-DERIVED)

### Core operating business only

| Step | Calculation | Value | Anchor |
|---|---|---|---|
| A. ROCE base | Core ROCE ex-QMPL 16.5% → 0.5 × 16.45 + 7.5 (v3.6 Amdt 11, ≤33% branch) | **15.7x** (band 15.3-15.7x) | fttcp-v2-core-roce-recompute.md §5,§7; AR-FY26 |
| Pillar 1 normalization route | **NONE** (Route A fails: CWIP+advances < 20% CE; Route B barred on STAGNANT verdict) | none | Section 1B v3.5.1 |
| B. Cash multiplier | Growth-induced, repaired series (dossier S1: FY25 CFO 36.30/PAT 15.16, FY26 CFO 31.40/PAT 20.69); FCF −25.75 Cr blocks elite band | **1.00x** | operator; AR-FY26 p.121-122 |
| ROCE recovery credited via | **NOT credited** — STAGNANT forward verdict; route NONE | none | FTTCP v2 |
| C. Quality-adjusted base | 15.7 × 1.00 | **15.7x** | |
| D. Growth premium (Pillar 3) | **+0x** — Amdt 16 gate now OPEN at 16.5% > ~13.5% CoC but HELD by operator (single-credit: transformation priced in the option slices; alloys catalyst SHARED, already in the forward ROCE read) | **+0.0x** | deliberation §3 Override 2 |
| E. Strategic premium | ROCE-recovery route not used | **+0.0x** | |
| F. Raw destination PE | 15.7 + 0 + 0 | **15.7x** | |
| F2. UA-adjusted raw PE | 15.7 × 1.25 (all three qualifiers: listed since 1960; EM 26 ≥ 25; FII+DII ~0.01% < 3%) | **19.6x** | Amendment 3 |
| G. Sector cap | Cables / Industrial products (manifest defect corrected) | **25x** (non-binding) | Section 1B cap table; 19.6x < 25x |
| **H. DESTINATION PE — ADDITIVE** | **min(19.63, 25)** | **19.6x** (19.1-19.6x) | approved |
| **DESTINATION PE — RRM** | 19.6 × 0.82 | **16.1x** (15.7-16.1x) | approved; r = 15.0% |

**r-adjustment audit (v3.6 Amdts 12-13, as approved):** r base 14.0% (small cap); durability/governance
adj +0.5 (promoter CAUTION, accounting quality 4/10); complexity adj +0.5 (Amdt 13: subsidiary opacity,
going-concern EoM, unreconciled MD-pay figures); cash-conversion r-UP none (12A, Pillar 2 owns it);
short-record r-UP none (12C, listed 1960). **Final r = 15.0%** (bounded [9%,18%]). **RRM = 1 + (13.5 −
15.0) × 0.12 = 0.82.**

**Relative-PE expression (Amdt 15).** Market PE denominator NOT FOUND (no macro-sheet.md in inputs).
Against the name's own basis: current forward-core PE = 882 / 22.9 = **38.5x**. The destination 19.6x/16.1x
therefore bakes in a **large DE-RATING**, not a re-rating. FTTCP Module B8 re-rating rating not produced
(NO-CONCALL); the relative read confirms the destination is conservative on the multiple.

**SHARED-CATALYST flag: MOOT.** Pillar 3 +0x and no forward ROCE credited in Pillar 1, so the
alloys-furnace catalyst is paid through no premium and cannot be double-counted (deliberation §3).

**Supersession recorded.** The 19-Aug approved base (Pillar 1 13.8x, additive 17.3x, RRM 14.1x) is
superseded by this anchored Reading-2 recompute (15.7x / 19.6x / 16.1x). The 19-Aug B11 record stays
committed for audit.

---

## 3. SECTION 2 — FY27 CORE OPERATING EARNINGS (REUSED, GRADE-C)

Reused verbatim from the 19-Aug Section 3 conservative build (operator-confirmed basis). FY27 has not
printed; Q1FY27 consolidated profit fell 38% YoY on +19% revenue with no MD&A (RESULTS-Q1FY27 p.3);
standalone Q1FY27 held (PAT 6.25 Cr). Growth held below the SOM-implied 3-yr core CAGR 20.1% (B09).
Emerging-Moat class STRENGTHENING → growth fades by Year 4 (Amdt 14; step-down shown FY28-FY29).

FY26 adjusted core operating PAT (ex other income, ex ~Rs 2.0 Cr relay strip) = Rs 17.55 Cr (EPS Rs 20.41;
19-Aug Section 3.1, AR-FY26 p.19).

| Case | FY27 rev growth | **FY27 core op PAT** | **FY27 core EPS** | FY28 EPS (fade) | FY29 EPS (fade, Yr-3) |
|---|---|---|---|---|---|
| Bear | +6% (margin compresses to ~7.0%) | **Rs 16.7 Cr** | **Rs 19.4** | +5% → 20.37 | +4% → **21.18** |
| Base | +12% (margin ~7.8%, flat vs FY26 core) | **Rs 19.7 Cr** | **Rs 22.9** | +11% → 25.42 | +10% → **27.96** |
| Bull | +16% (alloys mix) | **Rs 21.4 Cr** | **Rs 24.9** | +14% → 28.39 | +12% → **31.79** |

**SOM cross-check:** base core revenue growth 12% < SOM-implied 3-yr 20.1% → **CONSISTENT** (conservative,
no cut). **FTTCP-consistency row:** STAGNANT forward verdict, ROCE 16.5% below no crossover requirement
credited; Pillar 3 +0x; matches. **Sanity:** revenue < capacity (12% << 32.7% capex-embedded growth);
margins held near FY26 core; ROCE 16.5% now above ~13.5% CoC (this is what opened the Amdt 16 gate, held
by operator); consolidated FCF negative but the driver is subsidiary CWIP (Slice 3), not the core.

---

## 4. SECTION 3 — DUAL-TRACK SUM-OF-THE-PARTS

Both tracks carried through every slice. Core and relay earn the core destination PE (build-to-spec,
qualification moat). NdFeB earns a **converter exit PE** per v3.7 Amendment 17.0 (see below). Option
slices are probability-weighted expected values held constant across bear/base/bull, EXCEPT the NdFeB full
plan, which is **0 in bear** (operator instruction). PV discounts use r = 15.0% (the approved RRM r).

### 4.1 Slice 1 — CORE (FY27 forward core op PAT × destination PE)

| Case | FY27 core op PAT | ADDITIVE 19.6x | RRM 16.1x |
|---|---|---|---|
| Bear | 16.7 Cr | **327.32 Cr** | **268.87 Cr** |
| Base | 19.7 Cr | **386.12 Cr** | **317.17 Cr** |
| Bull | 21.4 Cr | **419.44 Cr** | **344.54 Cr** |

### 4.2 Slice 2 — RELAY OPTION (build-to-spec, core multiple)

Operator inputs (dossier S6): mature annual revenue **Rs 75 Cr** (rungs 1-2 of the content ladder; NO
rung-3 assembly pull-through credit). Net margin **8%** (prior/operator; consistent with core ~7.8%) →
mature PAT **Rs 6.0 Cr**. Probability of meaningful commercialization by FY29 **45%** (dossier S6).

- **Discount treatment (documented):** the 45% is the commercialization probability and already carries
  execution risk (failure so far is slowness, not rejection). I apply **NO additional execution discount**
  (would double-discount). I apply ONE present-value discount for time only: relay maturity ~FY29, ~3 years
  from the FY26 base, PV = 1/1.15³ = **0.6575**. This is time value, distinct from execution risk; the core
  is valued at a today's-destination basis while relay earns later, so the asymmetry is correct.
- Track used: **each track's core destination PE** (relay is a build-to-spec extension of the core).

| Track | Mature PAT × prob × PE × PV | **Slice value** | Per share |
|---|---|---|---|
| ADDITIVE | 6.0 × 0.45 × 19.6 × 0.6575 | **34.80 Cr** | Rs 40.47 |
| RRM | 6.0 × 0.45 × 16.1 × 0.6575 | **28.58 Cr** | Rs 33.24 |

### 4.3 Slice 3 — NdFeB OPTION (CONVERTER, two scenarios valued separately and summed)

**Converter exit PE (v3.7 Amdt 17.0, NOT the core quality multiple).** NdFeB magnet-making is a commodity
converter (traded rare-earth RM, spread economics, no formulation IP, 5-6 competitors incl. China at 92%
share). It cannot earn the core's 16.1x/19.6x. Converter PE derived on the Amendment 11 formula from a
stated through-cycle ROCE assumption: assume through-cycle ROCE **12%** (generous for a new entrant with no
cost-curve advantage) → 0.5 × 12 + 7.5 = **13.5x**; cash 1.00x (17.2 neutral converter); +0x growth;
no UA (a hypothetical future segment does not carry the parent's discovered-alpha qualifiers). **Converter
exit PE = 13.5x**, identical in both tracks (converter economics are track-independent). Margin kept at
**10%** per operator (flagged optimistic; see KEY NOTES sensitivity). Probabilities are operator inputs
(dossier S6).

**Scenario 3A — MODEST (Phase 2-3 scale, Rs 50-150 Cr class).** Revenue midpoint **Rs 100 Cr** × 10% =
mature PAT **Rs 10.0 Cr**. Probability **40%**. No capital netting (already-funded phases; dossier S6 "no
heroic raise"). Horizon ~FY29, PV 0.6575.

- Value = 10.0 × 0.40 × 13.5 × 0.6575 = **35.51 Cr** (Rs 41.30/sh), both tracks.

**Scenario 3B — FULL PLAN (5,000t, Rs 3,000-4,000 Cr revenue by FY30-31).** Revenue midpoint **Rs 3,500
Cr** × 10% = mature PAT **Rs 350 Cr**. Mature equity value = 350 × 13.5 = **Rs 4,725 Cr**. Net the
unraised capital **Rs 650 Cr** (dossier S6/V6: Rs 550-750 Cr unraised against a Rs 225 Cr revenue company;
midpoint), a hard evidenced deduction → net project equity **Rs 4,075 Cr**. Probability **12%**. Longer
dated: horizon FY30-31 ≈ 5 years, PV = 1/1.15⁵ = **0.4972** (Amdt 14 fade — the single maturity-year equity
value is discounted, growth is NOT perpetuity-capitalized past the exit multiple). **Bear = 0** (operator).

- Value (base/bull) = 4,075 × 0.12 × 0.4972 = **243.13 Cr** (Rs 282.77/sh), both tracks.

### 4.4 Equity bridge (ANCHORED, supersedes B11 Rs 7.72 Cr)

Anchored to the actual FY26 consolidated balance sheet (AR-FY26 p.120; Note 16 p.131-132):

| Component | Rs Cr | Anchor |
|---|---|---|
| Non-current borrowings (incl. full Rs 47.81 Cr QMPL ECB) | 66.84 | Consol BS, Note 16; ECB line "Rupee Loan from FI 47.81" |
| Current borrowings | 3.47 | Consol BS, Note 20 |
| = Total borrowings | 70.31 | derived |
| Less cash & cash equivalents | (28.11) | Consol BS line 10 |
| Less bank balances (current) | (23.20) | Consol BS line 11 |
| **= Consolidated net debt** | **19.00** | derived |

- **Supersession / FLAG (carried and flagged per task).** B11 used net debt Rs 7.72 Cr on the assumption
  the ECB was only ~Rs 28.86 Cr drawn (undrawn ~Rs 19 Cr flagged as a bear overlay). The filed consolidated
  balance sheet shows the **FULL Rs 47.81 Cr ECB drawn** (non-current borrowings 66.84 = parent 19.03 +
  QMPL 47.81), confirmed by the operator-approved 23-Aug core-ROCE recompute. The full-draw is therefore
  the correct **base**, giving anchored net debt **Rs 19.0 Cr**, not Rs 7.72 Cr. This is what B11 had carried
  as its bear overlay; it is now the base. The difference is Rs ~11 Cr = Rs ~13/share, immaterial to the
  decision. The future NdFeB full-plan capital (Rs 650 Cr) is netted inside Slice 3B, not here — no double
  count. Restricted-cash risk: if the Rs 23.20 Cr bank balances are LC/margin-restricted (rating cites LCs
  up to 180 days), net debt rises toward Rs 42 Cr (Rs ~49/share) — a bear overlay.
- Net debt / share = 19.0 / 0.8598 = **Rs 22.10**.

---

## 5. SOTP FAIR VALUE (both tracks, forward FY27 basis)

**Equity value = Slice 1 core + Slice 2 relay + Slice 3A modest + Slice 3B full − net debt 19.0 Cr;
÷ 0.8598 Cr shares.**

### Track 2 — ADDITIVE (core/relay 19.6x; NdFeB 13.5x converter) — PRIMARY DESTINATION

| Case | Core | Relay | NdFeB modest | NdFeB full | Net debt | Equity | **Per share** |
|---|---|---|---|---|---|---|---|
| Bear | 327.32 | 34.80 | 35.51 | 0 | (19.0) | 378.63 | **Rs 440** |
| Base | 386.12 | 34.80 | 35.51 | 243.13 | (19.0) | 680.56 | **Rs 791** |
| Bull | 419.44 | 34.80 | 35.51 | 243.13 | (19.0) | 713.88 | **Rs 830** |

### Track 1 — RRM (core/relay 16.1x; NdFeB 13.5x converter) — GOVERNING / sets entry zone

| Case | Core | Relay | NdFeB modest | NdFeB full | Net debt | Equity | **Per share** |
|---|---|---|---|---|---|---|---|
| Bear | 268.87 | 28.58 | 35.51 | 0 | (19.0) | 313.96 | **Rs 365** |
| Base | 317.17 | 28.58 | 35.51 | 243.13 | (19.0) | 605.39 | **Rs 704** |
| Bull | 344.54 | 28.58 | 35.51 | 243.13 | (19.0) | 632.76 | **Rs 736** |

**Track divergence (base):** (791 − 704) / 704 = **12.4%** (< 15%). The tracks are close because the
converter NdFeB slices (same multiple both tracks) and the capital-netted full plan dominate the SOTP,
compressing the RRM-vs-additive gap. RRM still governs the entry zone (more conservative; correct for
subsidiary opacity + going-concern complexity per the approved r decomposition).

**Every case on both tracks sits below CMP Rs 882** (highest is additive bull Rs 830). The AVOID survives
on fair value even with the higher Reading-2 base and the operator's generous option inputs.

---

## 6. SECTION 4 — HURDLE, ENTRY, EXPECTED RETURN, VERDICT

### 6.1 Hurdle Ratio (Tier A, pass ≥ 1.953)

Current forward-core PE = 882 / 22.9 = **38.5x**. HR = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE).
Base core EPS CAGR ≈ **12%**; Bull capped at Base + 5% = **17%** (credibility grade C bars face-value bull).

| Track | Base HR (12%) | Bull HR (17%) |
|---|---|---|
| RRM (16.1x) | 1.12³ × (16.1/38.5) = 1.405 × 0.418 = **0.59** | 1.17³ × 0.418 = **0.67** |
| Additive (19.6x) | 1.405 × (19.6/38.5) = 1.405 × 0.509 = **0.72** | 1.602 × 0.509 = **0.82** |

Every cell — including bull on the primary additive track — is far below 1.953. The de-rating term (16-20x
destination vs 38.5x current forward) sinks the ratio. **HURDLE = STOP.** Ratios are higher than the
19-Aug 0.52 (base PE rose ~2x) but the verdict is unchanged.

### 6.2 Value vs price (mandatory two lines)

1. **Worth:** on the approved base the business is worth **Rs 704 (RRM base) to Rs 791 (additive base)** per
   share — an earning core at 16.5% core ROCE plus a build-to-spec relay option and a converter-valued NdFeB
   option (~Rs 324/share combined on the RRM base, of which the Rs 3,000-4,000 Cr full plan is ~Rs 283 at
   12% probability).
2. **Price:** CMP Rs 882 already assumes ~38.5x forward-core AND full success of both option lines at scale
   that has not printed. Even additive bull Rs 830 is 6% below CMP. **Market-implied flag:
   PRICED-WE-ARE-LATE** — the option value is in the safe box, not available at the entry.

### 6.3 Evidence-scaled margin of safety

Core evidence mostly documented; option catalysts execution-uncertain (relay slipped 3 checkpoints, zero
orders in 4 years; NdFeB pre-revenue, going-concern EoM, Rs 550-750 Cr unraised). FY27 forward unprinted
(grade C). Net → **MIXED evidence → MoS = 30%.**

### 6.4 Entry zone & MoS price (RRM governing)

| | RRM (governing) | Additive |
|---|---|---|
| Base fair value | Rs 704 | Rs 791 |
| 25% CAGR entry = FV ÷ 1.953 | **Rs 361** | Rs 406 |
| MoS price = 25% entry × (1 − 0.30) | **Rs 252** | Rs 284 |

**Entry zone (RRM): Rs 252 (ideal MoS buy) to Rs 361 (acceptable 25%-CAGR entry).** CMP Rs 882 is **3.5x
above the MoS price and 2.45x above the 25% entry** — no entry available.

### 6.5 Probability-weighted 3-year CAGR (grade C → Bear 35% / Base 45% / Bull 20%)

Year-3 (FY29) core EPS (faded per Amdt 14): Bear 21.18 / Base 27.96 / Bull 31.79. Year-3 price =
destination PE × FY29 core EPS + option slices (held constant, conservative) − net debt/share 22.10.

| Case | RRM Yr-3 | CAGR from 882 | Additive Yr-3 | CAGR from 882 |
|---|---|---|---|---|
| Bear (35%) | Rs 393 | −23.6% | Rs 475 | −18.7% |
| Base (45%) | Rs 785 | −3.8% | Rs 890 | +0.3% |
| Bull (20%) | Rs 847 | −1.3% | Rs 965 | +3.1% |
| **Prob-weighted** | | **−10.2%** | | **−5.8%** |

Both tracks negative versus the +25% target. No scenario clears the hurdle; even additive base/bull only
reach roughly flat. **Expected return does not compensate at CMP.**

### 6.6 Risk-reward asymmetry

Upside (additive bull Rs 965 = +9.5% vs 882) ÷ downside (RRM bear Rs 393 = −55.4%) = **0.17**. Deeply
unfavourable asymmetry.

### 6.7 Four-Pillar validation

| Check | Result |
|---|---|
| Year-3 ROCE justifies base & matches FTTCP? | Yes — STAGNANT, core 16.5%, no crossover credited; Pillar 3 held +0x |
| CFO/PAT justifies cash multiplier? | 1.00x applied; consolidated FCF negative — no elite band, correct |
| Primary catalyst fired by Year 3 (base)? | Alloys DELIVERED; relay/NdFeB sized as options, not in core |
| Strategic premium justified? | No — +0x, single-credit respected |
| UA ordering min(F×1.25, cap)? | Yes — 19.63 < 25 cap |
| Would you pay 38.5x forward for a 16.5% core plus lottery tickets? | No — the thesis at CMP rests on both options succeeding at scale |

---

## 7. VERDICT CARD

| Field | Value |
|---|---|
| CMP / Market cap | Rs 882 / Rs 758 Cr (0.8598 Cr shares) |
| Pillar 1 (core ROCE 16.5%, STAGNANT, route NONE) | 15.7x, recovery NOT credited |
| Cash multiplier (growth-induced) | 1.00x (FLAG-CASH; FCF −25.75 Cr blocks elite band) |
| Quality base / Growth prem / Strategic | 15.7x / +0x (Amdt 16 gate OPEN, HELD) / +0x |
| Raw PE / UA / Sector cap | 15.7x / ×1.25 applied / 25x (non-binding) |
| **DESTINATION PE — ADDITIVE** (primary) | **19.6x** (19.1-19.6x) |
| **DESTINATION PE — RRM** (r=15.0%, RRM 0.82) | **16.1x** (15.7-16.1x) — GOVERNING, sets entry zone |
| NdFeB slice multiple (v3.7 Amdt 17 converter) | 13.5x (0.5×12+7.5), both tracks |
| **HURDLE RATIO** | Base 0.59 (RRM) / 0.72 (additive); Bull 0.67 / 0.82 → **STOP** |
| Method | SOTP (core P/E + relay option + NdFeB two-scenario converter option) |
| **FAIR VALUE (SOTP, per share)** | RRM Bear 365 / Base 704 / Bull 736 · Additive Bear 440 / Base 791 / Bull 830 |
| Expected 3-yr CAGR (prob-weighted, grade C) | Additive −5.8% / RRM −10.2% |
| Upside/Downside ratio | 0.17 (unfavourable) |
| Entry zone (RRM) / MoS price | Rs 252 – Rs 361 / Rs 252 |
| VALUE VS PRICE | Worth Rs 704-791 base; price assumes ~38.5x forward + both options at scale → **PRICED-WE-ARE-LATE** |
| MARGIN OF SAFETY | 30% (mixed evidence; option catalysts execution-uncertain, grade C forward) |
| SHARED CATALYST | **MOOT** (Pillar 3 +0x; no double-count) |
| **DECISION** | **AVOID (on valuation).** Fair value Rs 704-791 base vs CMP 882; Hurdle STOP; no entry until Rs 252-361 (RRM). |
| EXIT FRAMEWORK | n/a at CMP (no position); re-underwrite if price enters Rs 252-361 AND no thesis-broken trigger fired |

**ONE-LINE THESIS:** Avoiding PERMAGNET at Rs 882 — the Reading-2 recompute lifts the earning core to a
19.6x additive / 16.1x RRM destination on ~Rs 22.9 FY27 forward core EPS and prices the relay and NdFeB
lotteries at the operator's own generous inputs (Rs 75 Cr relay at 45%; NdFeB 12% full / 40% modest, the
commodity plant held to a 13.5x converter multiple per v3.7 Amdt 17), yet the base SOTP fair value of
Rs 704-791 still sits below price, the 25% hurdle STOPS on the 38.5x-to-16x de-rating, and expected CAGR is
negative; the future is paid for, in the safe box, not the entry.

---

## 8. KEY NOTES (conflicts, sensitivities, gaps)

1. **NdFeB multiple — v3.7 Amdt 17 vs the literal "× PE" instruction (conflict, resolved toward the
   framework).** The task's slice formula reads "× PE," which a reader takes as the core destination PE. I
   value the NdFeB slices at a **13.5x converter exit PE**, not the core 16.1x/19.6x, because v3.7 Amendment
   17.0 (and the signed mental model: "NdFeB is a licence/commodity bet, price the option") bars the core
   quality multiple from a commodity converter, and CLAUDE.md forbids feeding core quality metrics into a
   CONVERTER-classified name. This is not overriding the operator-approved base (which governs the CORE exit
   PE only); it correctly declines to extend that base to a different, commodity business.
   **Sensitivity (instruction-literal):** at the core destination PE the NdFeB full plan is worth Rs 346/sh
   (RRM) / Rs 431/sh (additive) and the modest Rs 49/60, lifting **additive base fair value to ~Rs 959 —
   ABOVE CMP 882.** The converter discipline is what keeps fair value below price; without it the AVOID
   would rest on the hurdle and entry logic alone.
2. **NdFeB margin (operator-locked, flagged optimistic).** Kept at 10% per operator; the dossier frames the
   business as a China-dominated commodity with 5-6 competitors and no cost-curve edge. At a realistic
   commodity net margin of ~5%, the NdFeB slices halve and **RRM base fair value falls to ~Rs 540** — a
   deeper AVOID. Direction of the conservatism is stated.
3. **Equity bridge net debt superseded, not reused.** The task asked to reuse B11's Rs 7.72 Cr bridge and
   carry the drawn-28.86/undrawn-19 treatment. The filed consolidated balance sheet (AR-FY26 p.120) shows
   the FULL Rs 47.81 Cr ECB drawn (non-current borrowings 66.84), confirmed by the operator-approved 23-Aug
   core-ROCE recompute, so anchored net debt is **Rs 19.0 Cr**, which is B11's own bear overlay now promoted
   to base. Filed document beats inference; impact Rs ~13/share, immaterial. Flagged.
4. **NdFeB full-plan dilution risk (bear overlay).** Netting Rs 650 Cr assumes a value-neutral raise. Raising
   Rs 550-750 Cr against a Rs 758 Cr market cap could more than double the share count at a pre-success
   price; the funding mix is unresolved ("debt and equity, yet to finalize," dossier V6). This is the single
   most valuation-relevant open unknown.
5. **Option-slice bear/base/bull construction.** Relay and NdFeB-modest are held constant across cases as
   probability-weighted expected values (operator fixed the inputs); the case spread is driven by core
   earnings and the NdFeB full plan (0 in bear). Documented, not estimated.
6. **NOT FOUND / unresolved (never estimated):** market PE denominator (no macro-sheet.md); QMPL own
   operating EBIT (interest-capitalisation split undisclosed); segment-level core-vs-relay cost split
   (single IND AS 108 segment); FY27 forward revenue/margin guidance (NO-CONCALL); NdFeB through-cycle ROCE
   (pre-revenue — 12% is a stated generous assumption, flagged); restricted-cash split of the Rs 23.20 Cr
   bank balances.

---

```yaml
stage: B11-valuation
company: "PERMAGNET"
run_date: "2026-08-19"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Market PE denominator for relative-PE expression NOT FOUND (no macro-sheet.md in inputs)"
  - "Segment-level core-vs-relay operating cost split NOT SEPARATELY DISCLOSED (single IND AS 108 segment)"
  - "FY27 forward revenue/margin guidance NOT QUANTIFIED (NO-CONCALL mode)"
  - "NdFeB through-cycle ROCE NOT FOUND (pre-revenue); 12% stated generous assumption -> converter PE 13.5x, flagged"
  - "Restricted-cash split of Rs 23.20 Cr consol bank balances NOT DISCLOSED (LC/margin possible); net-debt bear overlay ~Rs 42 Cr"
  - "NdFeB full-plan funding mix unresolved (debt/equity 'yet to finalize'); dilution bear overlay if Rs 550-750 Cr raised"
flags:
  - "FLAG-CASH (MAJOR): receivables +39.4% vs revenue +13.0%; consol CFO -55% vs PAT -6%; cash multiplier 1.00x APPLIED"
  - "FLAG-SUBSIDIARY (MAJOR): QMPL revenue -85.5%, full Rs 47.81 Cr ECB DRAWN (consol NC borrowings 66.84), negative net worth, going-concern EoM"
  - "FLAG-EXECUTION (MAJOR): relay slipped 3 checkpoints, zero orders in 4yr; NdFeB pre-revenue Phase 2 Q3FY27"
  - "FLAG-BRIDGE: anchored consol net debt Rs 19.0 Cr supersedes B11 Rs 7.72 Cr (full ECB draw confirmed); Rs ~13/share, immaterial"
  - "FLAG-CONVERTER: NdFeB valued at 13.5x converter PE per v3.7 Amdt 17, NOT the core destination PE; at core PE additive base FV ~Rs 959 > CMP"
  - "SHARED-CATALYST: MOOT (Pillar 3 +0x, no double-count)"
framework_versions: "Master v3.6 / Section 1B v3.3+v3.5.1+v3.6+v3.7 / FTTCP v2.1"
pe_basis: "forward"
exit_pe_base_approved: "Reading-2 core additive 19.6x (19.1-19.6x) / RRM 16.1x (15.7-16.1x); Pillar 1 15.7x on core ROCE 16.5%; Pillar 3 +0x held; operator-approved 2026-08-23 (fttcp-v2-deliberation Section 5). SUPERSEDES 19-Aug base 17.3x/14.1x."
destination_pe:
  track1_rrm: {low: 15.7, mid: 16.1, high: 16.1, r_used: 15.0, rrm: 0.82}
  track2_additive: {low: 19.1, mid: 19.6, high: 19.6}
  divergence_pct: 12.4
  governing_track: "RRM 16.1x - more conservative; sets entry zone. Additive 19.6x is the primary destination per deliberation."
pillar_detail:
  roce_used: 16.5
  roce_base: 15.7
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.00
  structural_or_growth: "growth-induced (operator-confirmed; repaired series dossier S1)"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: false
  ua_applied: true
  sector_cap_used: 25
hurdle_ratio: {base: 0.59, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 365, base: 704, bull: 736}
  track2: {bear: 440, base: 791, bull: 830}
expected_cagr_prob_weighted: -5.8
entry_range: {low: 252, high: 361}
mos_price: 252
upside_downside_ratio: 0.17
decision: "AVOID (on-valuation)"
unresolved_inputs_used:
  - "Relay slice: Rs 75 Cr rev (operator S6) / 8% margin / 45% prob (operator) / PV 0.6575 (FY29, r15%), core PE -> ~Rs 34.8 Cr additive / ~Rs 28.6 Cr RRM; NO extra execution discount (45% carries it)"
  - "NdFeB modest: Rs 100 Cr rev (50-150 midpoint) / 10% margin / 40% prob (operator) / PV 0.6575 / 13.5x converter PE = ~Rs 35.5 Cr, both tracks"
  - "NdFeB full plan: Rs 3,500 Cr rev (3,000-4,000 midpoint) / 10% margin / 350 Cr PAT / 13.5x = 4,725; net Rs 650 Cr unraised capital = 4,075; x 12% prob x PV 0.4972 (FY30-31, ~5yr) = ~Rs 243 Cr; bear = 0"
  - "NdFeB converter PE 13.5x = 0.5x12+7.5 on assumed 12% through-cycle ROCE (pre-revenue; generous), cash 1.00x, +0x, no UA; v3.7 Amdt 17"
  - "Net debt: anchored consol Rs 19.0 Cr (borrowings 70.31 - cash 28.11 - bank 23.20); supersedes B11 Rs 7.72 Cr (full ECB draw confirmed)"
  - "Current forward PE: CMP 882 / FY27 base core EPS 22.9 = 38.5x (forward-core basis for HR)"
som_cagr_crosscheck: "consistent (base core revenue growth 12% below SOM-implied 3yr 20.1%)"
one_line_thesis: "AVOID PERMAGNET at Rs 882: Reading-2 lifts the core to 19.6x/16.1x on ~Rs 22.9 FY27 forward core EPS and prices the relay (Rs 75 Cr, 45%) and NdFeB (12% full / 40% modest, held to a 13.5x converter multiple per v3.7 Amdt 17) options at operator inputs, yet base SOTP fair value Rs 704-791 stays below price, Hurdle STOPs on the 38.5x-to-16x de-rating, expected CAGR negative; future paid for, in the safe box not the entry."
```
