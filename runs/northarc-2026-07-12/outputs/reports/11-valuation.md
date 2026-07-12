# STAGE 11: ROLE 1 MULTI-MODAL VALUATION (LENDER CARVE-OUT)
# NORTHARC (Northern Arc Capital Limited) | Run 2026-07-12
# Framework: Master v3.3 / Section 1B v3.3 (Amendments 1-8, v3.4 4.1-4.4) / FTTCP v1.2
# Model: claude-opus-4-8

**Business type: LENDER (NBFC-ML).** Per Section 1B Amendment 7 lender carve-out:
Pillar 1 uses **ROE** (not ROCE); Pillar 2 is replaced by the **Pillar 2L Asset-Quality
Multiplier**; **P/B (theoretical P/B = ROE / CoE) is the PRIMARY method**; the Section 1B
destination PE is the **SECONDARY cross-check**; sector cap **18x** (Banks/NBFCs/MFIs),
absolute. All inputs sourced solely from B10 (outputs/reports/10-valinputs.md,
outputs/blocks/B10-valinputs.yaml). Deliberation determinations (fttcp-deliberation.md,
carried on B10) supersede any conflicting pipeline value.

---

## PRE-FLIGHT RECONCILIATIONS (INPUT DISCIPLINE)

**R1 — Share count.** B10 stage-10 block originally mislabeled shares as 16.18 mn; the
B10 YAML corrects it: 5,257 Cr / 325 = 16.18 **crore = 161.8 mn** (B10 shares_diluted_mn).
All per-share math uses **161.8 mn (16.18 cr)**.

**R2 — PAT standalone vs consolidated.** Consolidated PAT 404 Cr (FTTCP-authoritative,
ICRA-verified p.241) vs standalone 429.15 Cr (results P&L p.7). The **consolidated basis
is authoritative** (matches ROE 11.1%). Forward PAT is projected on consolidated net worth,
so current EPS is taken on the consolidated basis for internal consistency:
- Consolidated: EPS = 404 / 16.18 = **Rs 24.97** → current PE = 325 / 24.97 = **13.0x** (PRIMARY)
- Reported diluted EPS 22.59 (weighted-avg shares, mid-year IPO) → PE **14.4x** (more conservative)
- Standalone: EPS = 429.15 / 16.18 = 26.52 → PE 12.3x (least conservative)
The hurdle uses the authoritative consolidated 13.0x; the STOP verdict is shown to hold on
both the authoritative (13.0x) and the more-conservative reported (14.4x) bases.

**R3 — Book value per share.** B10 carries two mutually inconsistent figures:
BVPS Rs 241 (investor-presentation slide 5, used by fttcp-deliberation to frame market
P/B ~1.35x) vs audited consolidated equity 3,388 Cr / 16.18 cr = **Rs 209.7** (implies
market P/B 1.55x). Primary book anchor = **Rs 241** (aligns with the AUTHORITATIVE
deliberation framing); the audited-consolidated Rs 210 is carried as the MORE CONSERVATIVE
sensitivity that only **widens** the AVOID margin. Flagged.

**R4 — B10 unresolved[] fields, each handled by rule (no silent fills):**
| Field | Rule applied | Effect |
|---|---|---|
| Peer median P/B/PE | NOT FOUND → no peer-relative multiple credited; theoretical P/B (ROE/CoE) is sole P/B anchor | Conservative (removes peer premium) |
| Enterprise Value | N/A for a lender (P/B and P/E methods; EV methods excluded per B04) | None |
| 3-yr cumulative FCF | N/A for a lender (CFO structurally negative by Ind AS design); no DCF | None |
| FII+DII exact % | >3% established → UA blocked; exact % moot | UA does not apply |
| DPS | NOT FOUND → assume **0 (full retention)**; realistic for a growing NBFC. Note: full retention MAXIMISES book compounding, so it is generous to fair value, yet the hurdle still fails | Generous, still STOP |

---

## SECTION 1A — METHOD SELECTION & JUSTIFICATION

| Method | Suitable here? | Weight | Justification |
|---|---|---|---|
| **P/B (theoretical P/B = ROE ÷ CoE)** | **YES — PRIMARY** | **70%** | Lender carve-out (Amendment 7): book value is the capital base that earns spread; P/B is the mandated primary method. Anchored on ROE vs CoE. |
| **Section 1B Four-Pillar Destination PE** | YES — SECONDARY (cross-check only) | 30% | Amendment 7: PE is the SECONDARY cross-check for lenders. Both dual tracks (RRM, Additive) produced. |
| P/E (standalone) | Cross-check within Section 1B | — | Subsumed in the Four-Pillar PE. |
| EV/EBITDA, EV/Sales | NO | 0% | Interest expense is a core operating cost for a lender; EV methods inapplicable (B04 not_applicable). |
| DCF / DDM | NO | 0% | CFO structurally negative (Ind AS); no dividend. Terminal-value dominated and meaningless here. |
| Peer relative | NO | 0% | Peer P/B/PE medians NOT FOUND (B06 qualitative only). Cannot triangulate. |

**PRIMARY = P/B; SECONDARY = Section 1B destination PE (dual-track).** No peer method, no DCF.

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 (LENDER)

### Pillar 1 — ROE Base Multiple (lender: ROE in the ROCE formula)

- **FTTCP ROE forward verdict:** RECOVERING at ~50-55% probability (fttcp-deliberation via B10).
  Maps to the **60/40 weighted average** of current and FY[Y+2] expected ROE (Master Pillar 1
  table; FTTCP Pillar 1 Integration).
- ROE used = 0.60 × 11.1% (current FY26, B10) + 0.40 × 17.0% (FY28 expected midpoint of 16-18%,
  flagged STRETCHED, B10) = 6.66% + 6.80% = **13.46%**.
- ROE Base PE = 0.5 × ROE + 7.5, floor 9x, cap 24x = 0.5 × 13.46 + 7.5 = 6.73 + 7.5 = **14.2x**.
- **ROE recovery credited via: Pillar 1 (60/40 weighting).** Strategic-premium re-rating route is
  therefore BARRED (single-credit rule, Amendment 4). Stated in writing.

### Pillar 2L — Asset-Quality Multiplier (replaces Cash Conversion for lenders)

| Band evidence (B10) | Determination |
|---|---|
| GNPA 1.2% (<2% ✓), NNPA 0.6%, **PCR ~44.5% (<60%, breaches the >70% and 60-70% bands)**, credit-cost guidance missed once (2.3-2.5% → 2.7-2.8%) | **STRESSED band → 0.80x** |
| Mitigants: credit cost turned down FY26 (2.8% vs 3.2%), no growing restructured/written-off book, Stage II improved H1 FY26 (ICRA) | keeps it at 0.80x, not the 0.65x structural tier |

- Confirmed **0.80x** (matches the FTTCP deliberation determination and the Section 1B Amendment 7
  band table). **NO growth offset** for lenders (loan growth cannot offset underwriting).
- FLAG-CASH: the negative CFO is **GROWTH-INDUCED (Ind AS)**, NOT structural — so it is NOT
  double-penalised; the lender penalty is expressed once, via the asset-quality band (0.80x).
- **Quality-Adjusted Base = 14.2x × 0.80 = 11.4x** (14.23 × 0.80 = 11.38 → **11.4x**).

### Pillar 3 — Growth Visibility Premium

Two readings are shown; the current framework is **v3.4** (Amendment 4.1, dated 11-Jul-2026,
in force on the 2026-07-12 run date), so v3.4 governs; the v3.3 EM-gate is shown as the
conservative floor.

- **v3.3 EM-gate:** EM score 22 (<25) → **+0x**.
- **v3.4 decoupled (applied):**
  - **3a Growth Visibility** — documented qualifiers: (i) SOM-implied revenue CAGR 26% ≥20%
    with capacity cross-check passing (CRAR 22.6%, gearing 3.13x with room to ~4x supports
    20-24% AUM growth) ✓; (ii) management delivery grade **B** (A/B qualifies) ✓. Two qualifiers
    → **+2x** (grade B does not cap 3a). 
  - **3b Moat Formation** — EM 22 (<25) → **+0x**.
  - **3c Duration Premium** — no order book / no contracted-tenor revenue for a lender → **+0x**.
  - Combined Pillar 3 = **+2x** (within the +6x cap).
- **Applied: +2x** (v3.4). Conservative floor +0x (v3.3) is carried; the verdict does not depend
  on this choice (shown below). **SHARED CATALYST flag SET** — credit-cost normalisation drives
  BOTH the Pillar 1 ROE recovery AND the Pillar 2L band (single point of failure; Role 3 to
  stress-test).

### Strategic Asset Premium

- Rare-licence monopoly: NO (RBI NBFC-ML licence is not a scarcity monopoly).
- ROE re-rating optionality: **BARRED** — recovery already credited in Pillar 1 (single-credit).
- Turnaround with institutional backing: FII+DII >50% exists, but this is a *strengthening
  lender that the market has already found*, not a classic backed turnaround; no discount-to-book
  distress. Per deliberation, justify explicitly or use +0x → **+0x**.

### Undiscovered Alpha Multiplier

- Qualifiers (all three required): listed ≥12m ✓; Gate0 ≥60 OR EM ≥25 ✗ (Gate0 AVERAGE, EM 22);
  FII+DII <3% ✗ (>3%). **1 of 3 → UA does NOT apply.** F2 = F. No sector-cap quality uplift.

### Four-Pillar Summary — Track 2 (Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROE Base | ROE 13.46% → 0.5×13.46+7.5 | 14.2x |
| B. Asset-Quality Multiplier (Pillar 2L) | STRESSED, no offset | 0.80x |
| C. Quality-Adjusted Base | 14.23 × 0.80 | 11.4x |
| D. Growth Visibility Premium | v3.4 3a +2x / 3b +0 / 3c +0 (v3.3 floor +0x) | +2x |
| E. Strategic Premium | recovery barred; no scarcity | +0x |
| F. Raw Destination PE | 11.38 + 2 + 0 | 13.4x |
| F2. UA-Adjusted Raw PE | UA not applied → F2 = F | 13.4x |
| G. Sector Cap (no uplift) | Banks/NBFCs/MFIs | 18x |
| **H. Final Destination PE** | **min(F2, G) = min(13.4, 18)** | **13.4x** |

**Track 2 Destination PE range = 13.4x ±7.5% = 12.4-14.4x → 12.5x to 14.5x.**
(Conservative floor, v3.3 Pillar 3 = +0x: raw 11.4x, range 10.5-12.5x — the verdict is unchanged.)

### RRM Dual-Track Derivation — Track 1 (RRM)

- Base r: small-cap lender (mkt cap 5,257 Cr) = 14%; +0.5% for asset-quality stress + shared-catalyst
  single-point-of-failure, tempered by AA- rating → **r = 14.5%** (bounded [9%,18%]).
- **RRM = 1 + (13.5 − 14.5) × 0.12 = 1 − 0.12 = 0.88** (percentage-point reading, Amendment 4.4;
  bounded 0.70-1.60).
- Track 1 Destination PE = Fundamental Base PE × RRM = **11.38 × 0.88 = 10.0x** (cap 18x → 10.0x).
- **Track 1 range = 10.0x ±7.5% = 9.3-10.75x → 9.5x to 11.0x.**

### Track divergence

Track 2 mid 13.4x vs Track 1 mid 10.0x → divergence **29%** (>15%). For lenders **P/B is the
PRIMARY method and governs the decision**; the PE tracks are cross-checks. Between them, the
**RRM track (10.0x) is the more conservative and more appropriate** given stretched FY28 ROE
guidance and the shared-catalyst risk, and it corroborates the P/B result. Track 2 (13.4x)
embeds an **unjustified implied exit P/B of 13.4 × 0.14 = 1.88x** vs a theoretical fair P/B of
~0.97x — i.e., the additive PE method silently re-rates a sub-CoE lender and must be treated as
a ceiling cross-check only.

### Hurdle Ratio (Section 1B sanity check — this replaces the binary STOP)

**HR = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE). Tier A pass ≥ 1.953.**

Current PE = **13.0x** (consolidated, authoritative). Destination PE mid (Track 2) = 13.4x.
EPS CAGR base 14.1%, bull 22.8% (grade B → bull permitted).

| Row | Computation | HR | vs 1.953 |
|---|---|---|---|
| HR(Base) | (1.141)³ × (13.4/13.0) = 1.4858 × 1.0308 | **1.53** | FAIL |
| HR(Bull) | (1.228)³ × (13.4/13.0) = 1.8524 × 1.0308 | **1.91** | FAIL (by 0.04) |

**Verdict: STOP** — even bull-case earnings do not deliver a 25% CAGR at CMP 325. Robustness:
on the more-conservative reported PE 14.4x, HR(Bull) = 1.8524 × (13.4/14.4) = 1.72 → STOP more
clearly; on the RRM track (10.0x), HR(Base) = 1.4858 × (10.0/13.0) = 1.14 → STOP. The only basis
that flirts with CONDITIONAL is the least-conservative standalone PE 12.3x
(HR(Bull) = 1.8524 × 13.4/12.3 = 2.02, marginal pass) — rejected under conservative bias and the
authoritative consolidated basis. **HURDLE = STOP holds.**

*Would I personally pay 13.4x for a lender whose sustainable ROE (13.5%) sits below its cost of
equity (14.5%)? No — the theoretically consistent PE for a lender with ROE < CoE is far below
13x. This is exactly why P/B is primary here.*

> INTERIM CHECKPOINT: Section 1 complete. Destination PE 13.4x additive (12.5-14.5x) / 10.0x RRM
> (9.5-11.0x). Current PE 13.0x. Hurdle Ratio STOP. P/B is primary; PE is cross-check. Proceeding.

---

## SECTION 2 — PROJECTIONS (BASE primary; Bear/Bull ranges)

Growth is modelled on the lender drivers: AUM growth (leverage-funded) drives revenue; book
value compounds at retained ROE (DPS = 0, full retention per R4); PAT = ROE × book.

### 2A/2B assumptions

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| AUM/revenue growth logic | credit-cost re-accel, MFI stress | 20% AUM (guidance 22-25% discounted for track record) | guidance at face value (grade B) |
| Revenue CAGR | 15% | **20%** | 24% |
| ROE path (Yr1→Yr3) | flat ~11% | 12% → 13% → **14%** | 13% → 15% → **17%** |
| Book growth (=retained ROE, DPS 0) | ~11% | ~13% | ~14.5% |

### 2C Projection table (consolidated basis; shares 16.18 cr)

| Line | Year 0 (FY26) | Base Yr1 | Base Yr2 | Base Yr3 |
|---|---|---|---|---|
| Revenue (Rs Cr) | 2,709 | 3,251 | 3,901 | 4,681 |
| Net worth (Rs Cr) | 3,388 | 3,795 | 4,288 | 4,888 |
| ROE % | 11.1 | 12.0 | 13.0 | 14.0 |
| PAT (Rs Cr) | 404 | 407 | 493 | 600 |
| EPS (Rs) | 24.97 | 25.1 | 30.5 | **37.1** |
| BVPS (Rs, IP basis 241) | 241 | 273 | 309 | **347.7** |
| BVPS (Rs, audited basis 210) | 209.7 | 237 | 269 | 303 |

Bear Yr3: PAT ~459 Cr, EPS ~28.4, BVPS(241) ~329.6. Bull Yr3: PAT ~748 Cr, EPS ~46.3,
BVPS(241) ~361.7.

**EPS CAGR (Yr0→Yr3, consolidated): Bear 4.4% | Base 14.1% | Bull 22.8%.**

### 2D Sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capital allows? | CRAR 22.6%, gearing 3.13x→~4x room; 20-24% AUM feasible | Pass |
| Base revenue CAGR 20% vs SOM-implied 26% | below the SOM ceiling → **consistent** | Pass |
| ROE stays above 15%? | Base reaches only 14% by Yr3; **below 15% and below CoE 14.5% until bull** | **FLAG** |
| FCF funds growth? | N/A lender (Ind AS CFO negative by design) | N/A |
| EPS growth operational, not engineered? | driven by ROE recovery + retained-earnings book growth | Pass (recovery is the stretched input) |
| Year-3 ROE consistent with FTTCP verdict? | base 14% by Yr3, 17% FY28 = RECOVERING (not FIRING) | Pass |
| Asset-quality trajectory consistent with 0.80x band? | credit-cost normalisation assumed; SHARED CATALYST | Pass, flagged |

> INTERIM CHECKPOINT: Section 2 complete. Base EPS Rs 24.97 → Rs 37.1 (14.1% CAGR). Proceeding.

---

## SECTION 3 — VALUATION METHODS

### PRIMARY — P/B (theoretical P/B = ROE ÷ CoE)

**CoE = 14.5%.** Rationale: Rf (India 10-yr G-sec) ~6.8-7.0%, ERP ~6.5-7.0%, beta ~1.1-1.2 for a
small-cap NBFC → CoE ~14-15%; midpoint 14.5% (matches the deliberation's stated ~14-15%).

Fair P/B by scenario (exit ROE ÷ CoE): Bear 11.1%/14.5% = **0.77x**; Base (exit ROE 14%)
14.0/14.5 = **0.97x**; Bull (exit ROE 17%) 17.0/14.5 = **1.17x**. Note base sustainable ROE
13.46%/14.5% = 0.93x — **theoretical fair P/B < 1.0x because ROE < CoE**. This is the central
finding: the stock trades at **1.35x book (BVPS 241)** / **1.55x (audited 210)** — a 40-70%
premium to theoretical fair P/B.

**Fair value today (fair P/B × current BVPS 241):** Bear 186 | Base 224 | Bull 282 — all **below
CMP 325**. Stock is overvalued on static P/B.

**3-year target (book compounds at retained ROE; exit at fair P/B), BVPS 241 basis:**

| | Yr3 BVPS | Exit P/B | Target (Rs) | CAGR from 325 |
|---|---|---|---|---|
| Bear | 329.6 | 0.77x | **254** | -7.9% |
| Base | 347.7 | 0.97x | **337** | +1.2% |
| Bull | 361.7 | 1.17x | **423** | +9.2% |

(Audited BVPS 210 basis is more conservative: Base target ~294 → -3.3% CAGR. Verdict unchanged.)

**P/B PRIMARY fair values (Yr3): Bear 254 | Base 337 | Bull 423.**

### SECONDARY — Section 1B Destination PE (cross-check, dual-track)

Target = Exit PE × EPS Yr3. **These OVERSTATE for a sub-CoE lender** (implied exit P/B >> 1.0x)
and are reported as a ceiling cross-check only.

| Track | Exit PE mid | Bear (EPS 28.4) | Base (EPS 37.1) | Bull (EPS 46.3) |
|---|---|---|---|---|
| **Track 2 Additive** | 13.4x | 381 (+5.4%) | 497 (+15.2%) | 620 (+24.0%) |
| **Track 1 RRM** | 10.0x | 284 (-4.4%) | 371 (+4.5%) | 463 (+12.5%) |

Implied exit P/B: Track 2 base 13.4 × 0.14 = **1.88x** (unjustified); Track 1 base 10.0 × 0.14 =
**1.40x** (still above theoretical 0.97x). Both confirm the additive PE is generous; the P/B
primary is the disciplined anchor.

### Method-wise fair-value summary (Yr3)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/B primary | 70% | 254 | 337 | 423 |
| Section 1B PE (RRM-conservative cross-check) | 30% | 284 | 371 | 463 |

> INTERIM CHECKPOINT: Section 3 complete. P/B primary base fair value Rs 337 (Yr3). Proceeding.

---

## SECTION 4 — TRIANGULATION, ENTRY & VERDICT

### 4A Triangulated fair value (P/B 70% + RRM-PE cross-check 30%)

| | Bear | Base | Bull |
|---|---|---|---|
| P/B primary × 0.70 | 178 | 236 | 296 |
| RRM-PE × 0.30 | 85 | 111 | 139 |
| **Weighted (Yr3)** | **263** | **347** | **435** |

The governing entry zone is set by the **P/B primary (base Rs 337)** — the more conservative,
lender-appropriate method — not the blended figure, which the PE cross-check pulls up.

### 4B Methods agreement

All methods point the SAME direction: **below the 25% hurdle**. Spread (P/B base 337 vs Track 2
additive 497) = 47%, driven entirely by the additive PE embedding an exit P/B (1.88x) the ROE
cannot support. P/B primary is trusted for a lender with ROE < CoE.

### 4C / 4D Return expectation and probability weighting (grade B → 25/50/25)

| Scenario | Prob | P/B primary Yr3 | CAGR | Weighted |
|---|---|---|---|---|
| Bear | 25% | 254 | -7.9% | -1.98% |
| Base | 50% | 337 | +1.2% | +0.60% |
| Bull | 25% | 423 | +9.2% | +2.30% |
| **Expected CAGR (P/B primary)** | 100% | | | **~+1.3%** |

Cross-check expected CAGR: RRM-PE ~4.3%; Additive-PE ~15.0% (ceiling, overstated). **Every method
is far below the Tier A 25% hurdle; the primary method is ~+1.3%.**

### 4E Entry price (Tier A divisor 1.953)

| Calculation | Value |
|---|---|
| Base fair value (P/B primary, Yr3) | Rs 337 |
| Entry for 25% CAGR = 337 ÷ 1.953 | **Rs 173** |
| Entry for 30% CAGR = 337 ÷ 2.197 | Rs 153 |
| **Entry range** | **Rs 153 to Rs 173** |
| **MoS price (20% below 25%-CAGR entry)** | **Rs 138** |

CMP 325 sits **88% above the top of the entry zone** — no margin of safety for a 25% hurdle.

### 4F Risk-reward asymmetry (P/B primary, from CMP 325)

| | Value |
|---|---|
| Bull Yr3 423 → upside | +30.2% |
| Base Yr3 337 → upside | +3.7% |
| Bear Yr3 254 → downside | -21.8% |
| **Upside(base)/Downside(bear)** | **0.17x** (fails ≥2x badly) |

### 4G Four-Pillar validation

| Check | Result | Pass? |
|---|---|---|
| Yr3 ROE justifies the ROE base + matches FTTCP RECOVERING? | base 14% by Yr3, 60/40 blend 13.46% used | Pass |
| Yr3 asset-quality justifies 0.80x band? | credit-cost normalisation assumed; SHARED CATALYST | Pass, flagged |
| Primary catalyst fired by Yr3 (base)? | D2C-mix / credit-cost normalisation partially, not fully | Partial |
| Strategic premium justified (single-credit respected)? | +0x; recovery in Pillar 1 only | Pass |
| UA ordering min(F×1.25, cap) correct? | UA not applied; F2 = F | Pass |
| Would I buy another stock at 13.4x with ROE < CoE? | No → confirms PE is a ceiling cross-check | Note |

### 4H FINAL VERDICT CARD

**Tier: A | Hurdle: 25% CAGR** (UA blocked, FII+DII >3%; Gate0 AVERAGE + EM 22 fail Tier B gate)

- **CMP Rs 325 | Market Cap Rs 5,257 Cr | Shares 161.8 mn**
- **FOUR-PILLAR EXIT PE:** ROE base 14.2x (FTTCP RECOVERING 50-55% → ROE 13.46% via 60/40, recovery
  credited via **Pillar 1**) × **Asset-Quality 0.80x** (STRESSED: PCR 44.5%<60%, CFO growth-induced
  not double-penalised) = Quality base **11.4x**; + Growth Visibility **+2x** (v3.4 3a; v3.3 floor
  +0x); + Strategic **+0x**; Raw **13.4x**; UA **N**; Sector Cap **18x** (no uplift) →
  **DESTINATION PE 13.4x (12.5-14.5x)**.
- **RRM TRACK:** r 14.5%, RRM 0.88 → **10.0x (9.5-11.0x)**. Divergence 29%; P/B governs.
- **PRIMARY P/B:** CoE 14.5%; fair P/B base **0.97x** vs market **1.35x** (241) / 1.55x (210) →
  **overvalued to theoretical fair P/B by 40-70%.**
- **HURDLE RATIO: STOP** (HR base 1.53, bull 1.91; both < 1.953).
- **WEIGHTED FAIR VALUE (Yr3):** P/B primary Bear 254 | Base 337 | Bull 423. RRM-PE cross-check
  284 | 371 | 463. Additive-PE ceiling 381 | 497 | 620.
- **EXPECTED CAGR (prob-weighted, grade B 25/50/25): ~+1.3% (P/B primary).**
- **UPSIDE/DOWNSIDE: 0.17x** (fails ≥2x).
- **ENTRY Rs 153-173 | MoS Rs 138.** CMP 325 is 88% above entry.
- **DECISION: AVOID (on valuation).** Quality watch, not a quality reject — a strengthening AA-
  lender priced with zero margin of safety for the operator's 25% hurdle. Re-engage toward
  WATCHLIST/BUY only near the entry zone (Rs 153-173) or if ROE recovery decisively beats
  guidance (sustained >17% with PCR rebuilt >60%).
- **KEY ASSUMPTIONS (▲/▼):** ▲ ROE sustains above CoE (→ fair P/B >1.0x, lifts every target);
  ▼ credit-cost re-acceleration >3.2% + GNPA >1.5% fails BOTH pillars (shared catalyst); ▼ PCR
  stays <60% caps the asset-quality band at 0.80x.
- **EXIT FRAMEWORK:** target exit at destination PE 13.4x / fair P/B on realised ROE; thesis broken
  if ROE recovery stalls below 12% for 2 quarters; PE compression floor ~10x (RRM). 
- **ONE-LINE THESIS:** "AVOID Northern Arc at Rs 325: EPS grows Rs 24.97 → Rs 37.1 over 3 years on
  a recovering ROE, but at a four-pillar destination PE of 13.4x (ROE 13.5%, asset-quality 0.80x,
  EM 22, cap 18x) and a theoretical fair P/B of 0.97x (ROE 13.5% < CoE 14.5%), fair value is
  Rs 337 = ~+1.3% CAGR; the market's 1.35x book already prices the recovery. Entry Rs 153-173.
  Key risk: credit-cost re-acceleration fails both pillars (SHARED CATALYST). Cash: growth-induced."

> Valuation complete. Four-pillar exit PE 13.4x (RRM 10.0x). Hurdle Ratio STOP. P/B primary base
> fair value Rs 337; expected CAGR ~+1.3%. Entry Rs 153-173, MoS Rs 138. Decision: AVOID (on
> valuation) — quality watch.

---

```yaml
stage: B11-valuation
company: "NORTHARC"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Peer median P/B/PE NOT FOUND (B06 qualitative only) — no peer-relative multiple credited; theoretical P/B is sole P/B anchor"
  - "Enterprise Value / 3-yr FCF N/A for lender (Ind AS CFO negative by design); no EV or DCF method"
  - "FII+DII exact % NOT FOUND (>3% established, UA blocked; exact figure moot)"
  - "DPS NOT FOUND — assumed 0 (full retention); generous to book compounding yet hurdle still STOP"
flags:
  - "FLAG-CASH: CFO growth-induced (Ind AS), NOT structural; expressed ONCE via Pillar 2L Asset-Quality Multiplier 0.80x (STRESSED); Kernex cap NOT applied"
  - "SHARED CATALYST SET: credit-cost normalisation drives BOTH Pillar 1 ROE recovery AND Pillar 2L band; DA to stress-test single point of failure (credit cost >3.2% + GNPA >1.5%)"
  - "BVPS inconsistency: Rs 241 (IP/deliberation, market P/B 1.35x) vs audited consolidated Rs 210 (P/B 1.55x); 241 used as primary, 210 as conservative sensitivity that widens AVOID"
  - "FY28 ROE guidance 16-18% flagged STRETCHED; sustainable ROE 13.5% sits BELOW CoE 14.5% -> theoretical fair P/B <1.0x"
  - "Additive-PE cross-check overstates: implied exit P/B 1.88x vs theoretical 0.97x; treated as ceiling only. P/B primary governs"
  - "Current PE basis: consolidated 13.0x authoritative (STOP); standalone 12.3x marginal-CONDITIONAL rejected under conservative bias"
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 9.5, mid: 10.0, high: 11.0, r_used: 14.5, rrm: 0.88}
  track2_additive: {low: 12.5, mid: 13.4, high: 14.5}
  divergence_pct: 29
  governing_track: "P/B primary governs (lender carve-out); RRM 10.0x is the conservative PE cross-check and corroborates AVOID"
pillar_detail:
  roce_used: 13.46
  roce_base: 14.2
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 0.80
  structural_or_growth: "growth-induced CFO; Pillar 2L asset-quality STRESSED band applied (0.80x)"
  growth_offset: 0
  growth_premium: 2
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 18
hurdle_ratio: {base: 1.53, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 284, base: 371, bull: 463}
  track2: {bear: 381, base: 497, bull: 620}
expected_cagr_prob_weighted: 1.3
entry_range: {low: 153, high: 173}
mos_price: 138
upside_downside_ratio: 0.17
decision: "AVOID (on-valuation) — quality watch; re-engage near Rs 153-173 or if ROE decisively beats guidance"
unresolved_inputs_used:
  - "DPS NOT FOUND -> assumed 0 full retention (realistic for growing NBFC; generous to fair value, hurdle still STOP)"
  - "Peer median P/B NOT FOUND -> no peer premium; theoretical P/B (ROE/CoE) sole anchor (conservative)"
  - "BVPS ambiguity -> Rs 241 primary (deliberation-aligned), audited Rs 210 conservative sensitivity"
  - "PAT basis -> consolidated 404 Cr authoritative for EPS/PE 13.0x; standalone/reported noted"
som_cagr_crosscheck: "consistent"
one_line_thesis: "AVOID Northern Arc at Rs 325: recovering ROE grows EPS Rs 24.97->37.1 over 3yr, but at destination PE 13.4x and theoretical fair P/B 0.97x (ROE 13.5% < CoE 14.5%) fair value is Rs 337 = ~+1.3% CAGR; market's 1.35x book already prices the recovery. Entry Rs 153-173. Key risk: credit-cost re-acceleration fails both pillars (SHARED CATALYST)."
```
