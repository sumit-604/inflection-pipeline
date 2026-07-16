# STAGE 11: ROLE 1 MULTI-MODAL VALUATION
## Fedbank Financial Services Ltd (FEDFINA)
**Run Date:** 2026-07-15 | **Report Date:** 2026-07-16
**Model:** claude-opus-4-8 | **Framework:** Master v3.3 / Section 1B v3.3 (+ Amendments, consolidated Amendment 9) / FTTCP v1.2
**Business type:** LENDER (NBFC-ND-SI, gold loans + LAP). Lender carve-outs applied throughout (Section 1B Amendment 7: ROE-based Pillar 1, Pillar 2L Asset-Quality Multiplier, P/B primary, 18x cap).
**Status:** Complete

---

## INPUT DISCIPLINE PREAMBLE

All inputs are drawn ONLY from the B10 table (`B10-valinputs.yaml`) and the assembly report (`10-assembly.md`). Stage-11 projection inputs that B10 left unresolved (FY[Y+2] expected ROE; cost of equity) are set here from evidence and stated explicitly under "UNRESOLVED INPUTS SET AT STAGE 11". Market inputs use the deliberation-corrected 15 Jul 2026 close (manifest CMP was 0.0 pre-deliberation; corrected value Rs 164 is used).

| Market input | Value | Anchor |
|---|---|---|
| CMP | Rs 164 | manifest.yaml / fttcp-deliberation.md (screener.in, 15 Jul 2026) |
| Market cap | Rs 6,132 Cr | manifest.yaml |
| Shares (diluted) | 37.42 Cr (3,742.1 lakh) | results-A.txt Q1FY27 (post-ESOP) |
| BVPS (FY26) | Rs 78.2 (net worth 2,926.10 Cr / 37.42 Cr) | results-B.txt / computed |
| Market P/B | 2.09x | fttcp-deliberation.md |
| Market P/E (screener) | 16.0x | fttcp-deliberation.md |
| Diluted EPS FY26 | Rs 9.12 | results-B.txt p.6 |
| Current P/E on our EPS | **17.98x** (164 / 9.12) | computed; used as the internally-consistent "Current PE" for the Hurdle Ratio (more conservative than the 16.0x screener quote, which implies a Rs ~10.25 EPS base) |

---

## UNRESOLVED INPUTS SET AT STAGE 11 (with reasoning)

**1. FY[Y+2] expected ROE = 15.0%** *(INPUT UNRESOLVED in B10; set here from evidence.)*
Reasoning, conservative bias:
- Current ROE 12.6%; FY26 ROA 2.28% (computed); rating.txt shows 9MFY26 annualised ROA 2.50% (CARE, 10 Apr 2026).
- Assets/equity leverage = Total Assets 16,874.78 / Net Worth 2,926.10 = 5.77x. ROE = ROA x leverage. FY26: 2.28% x 5.77 ≈ 13.2% (reconciles to the 12.6% stated on average-equity basis).
- Forward bridge to FY28: ROA improving toward ~2.5-2.6% (credit-cost normalisation off the elevated FY25 1.8% toward the guided ~0.9-1.0% band; gold-branch AUM maturation diluting fixed cost against a 56-57% cost-to-income that is 15-25 pts above peers, so only partial operating leverage credited); leverage edging to ~6.0x (CRAR 22.40% gives ample headroom). 2.55% x 6.0 ≈ 15.3% → rounded down to 15.0%.
- Cross-checks: below Five-Star peer ROE (~17-18%); at/below the non-anchored Q4 FY26 deliberation claim of RoE 14% used only as a directional sanity check, not evidence; above SBFC's ~10-12%. A modest, evidenced recovery. Anchor mix: results-B.txt (ROA/leverage), rating.txt (ROA trajectory, parentage), B06 (peer band).
- **Guardrail:** the FY-wise ROE series (FY21-FY26) is NOT FOUND (B10 unresolved). Route B of consolidated Amendment 9 (pre-cycle normalised ROE) therefore does NOT apply — its 📄 pre-depression-history gate fails. Standard FTTCP RECOVERING blend stands.

**2. Cost of Equity (CoE) = 13.5%** *(INPUT UNRESOLVED in B10; set here.)*
Reasoning: Section 1B RRM base r for a small/mid NBFC is 13-14%. FEDFINA sits at the smaller end of mid-cap (~Rs 6,100 Cr). Base 13.75% midpoint, adjusted: AA+ CARE rating + Federal Bank 60.80% parentage + CRAR 22.40% + LCR 152% + no-negative-ALM-mismatch liquidity (rating.txt) argue the low end; offset by promoter verdict CAUTION, near-total senior-management turnover in ~18 months (B08), thin PCR and the impairment spike (FLAG-ASSETQUALITY). **Net CoE = 13.5%**, bounded well inside the framework [9%, 18%]. The same figure anchors the RRM r (one required-return, one mechanism).

---

## SECTION 1A: METHOD SELECTION

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | **P/B (theoretical P/B = ROE / CoE)** | 60% | Mandatory primary for lenders (Section 1B Amendment 7, Pillar 2L). Book value is the operative capital base for an NBFC; ROE vs CoE is the value-creation test. |
| SECONDARY | **P/E (destination PE from Section 1B, ROE-based Pillar 1)** | 40% | Cross-check only for lenders. Destination PE is EARNED via the Four-Pillar worksheet, not assumed. |
| TERTIARY | — | — | EV/EBITDA, DCF, EV-based methods FAIL for a leveraged financial (finance cost is core COGS; CFO/PAT is structurally negative per NBFC Ind AS 7 — FLAG-CASH). DDM rejected: minimal payout, growth-reinvesting. |

Excluded methods and why: EV/EBITDA and EV/Sales are meaningless where interest is the primary operating cost; DCF on FCF is inapplicable (FCF/PAT -4.92x, structural, not a quality signal). P/B + P/E is the correct pair for this archetype.

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE WORKSHEET (LENDER CARVE-OUT)

**Pillar 1 normalization route (consolidated Amendment 9 worksheet line):** NONE.
- Route A (operational ROCE) — N/A: lender; CWIP/idle-capital denominator test does not apply.
- Route B (pre-cycle normalized ROE) — DOES NOT APPLY: FY-wise pre-depression ROE series NOT FOUND (B10 unresolved); the 📄 gate fails. Statutory current ROE feeds Pillar 1 via the standard FTTCP RECOVERING blend.

### Pillar 1 — ROE Base Multiple (ROE substitutes ROCE, Amendment 7)

- FTTCP return-transition forward verdict: **RECOVERING, 40-60% probability** (fttcp-deliberation.md; SHARED CATALYST = credit-cost normalisation).
- Pillar 1 table (RECOVERING 40-60%): ROE used = **60/40 weighted average of current and FY[Y+2]**.
- ROE used = 0.60 x 12.6% + 0.40 x 15.0% = 7.56 + 6.00 = **13.56%**.
- Continuous formula (Amendment 5): Base PE = 0.5 x 13.56 + 7.5 = 6.78 + 7.5 = **14.28x → 14.3x** (floor 9x, cap 24x; within range).
- **ROCE/ROE recovery credited via: Pillar 1** (single-credit rule; Strategic re-rating route barred per fttcp-deliberation.md).

### Pillar 2L — Asset-Quality Multiplier (replaces Cash Conversion Multiplier)

- GNPA 1.87%, NNPA 1.28% (results-B.txt); PCR 32.29% FY26 year-end / 38.36% Q1FY27 (thin vs 60-70% norm); credit cost delivered inside guided 1% +/- 10bps band through Q3 FY26.
- Nominal band read: GNPA <2% is elite, but PCR 32-38% is far below the "Sound" 60-70% norm → draft mechanical band would be 0.80x (Stressed).
- **OPERATOR OVERRIDE (fttcp-deliberation.md override 2): 1.00x (Sound).** Applied as given (B10 authoritative overlay; not re-litigated at Stage 11).
- **Self-withdraw condition CARRIED:** reverts to 0.80x if Q4 FY26 credit cost > 1.1% OR PCR thins further. Q4 FY26 quarter-only actuals are a NAMED DATA GAP (FLAG-Q4-FY26-DATA-GAP).
- No growth offset (loan growth cannot offset underwriting).
- **Quality-Adjusted Base = 14.3x x 1.00x = 14.3x.**

*Note on FLAG-CASH:* CFO/PAT -5.04x (6-yr cumulative) is STRUCTURAL and mechanical per NBFC Ind AS 7 (fttcp-deliberation.md item 9), NOT a cash-quality failure. The cash multiplier is REPLACED by Pillar 2L for lenders; FLAG-CASH is carried forward but applies NO penalty here.

### Pillar 3 — Growth Visibility Premium (decoupled, Amendment 4.1/4.2, +6x combined cap)

- 3a Growth Visibility: qualifiers — SOM-implied revenue CAGR 23.6% (≥20%, B09) is ONE potential qualifier but its capacity cross-check is an inference ("achievable via productivity + co-lending", B09), not a 📄 clean pass; branch capex-embedded growth 12.6% (<15%, fails); order book N/A (lender); management delivery grade B (one qualifier). Net: only one clean qualifier → **3a = +0x** (needs any two).
- 3b Moat Formation: EM score 25.3 (STRENGTHENING, bottom edge; B07). Table: EM 25-29 any timeline → **+1x**.
- 3c Duration: N/A for a lender (no documented order book / contracted-revenue tenor) → **+0x**.
- **Pillar 3 total = +1x.** Half the active EM categories are industry-shared tailwinds (R1 gold-loan framework, H2 Federal Bank) and the two hardest FY27 promises are unverified (FLAG-EMOAT-BORDERLINE) — the conservative +1x is appropriate.

### Strategic Asset Premium

- Base **+0x** (single-credit: ROE recovery already credited in Pillar 1; ROE re-rating route barred, fttcp-deliberation.md).
- **Optional +1x argued for Federal Bank institutional backing** ("Turnaround with institutional backing +1 to +2x"): Federal Bank 60.80% parent, AA+ rated, ~Rs 471 Cr cumulative equity infusions, ~Rs 1,325.53 Cr outstanding funding, co-lending access (rating.txt / B04). This is a DISTINCT premium type from the barred ROE re-rating route, so it is permissible. **Held at +0x in the governing case** (conservative bias; deliberation left it optional for Role 3), carried as an upside sensitivity below. Verdict is robust either way (shown in the Hurdle Ratio section).

### Undiscovered Alpha Multiplier

- **UA does NOT apply.** FII 0.66% + DII 18.82% = ~19.5% (Mar-2026 shareholding, B10 note), far above the 3% test. `ua_qualifiers.all_met = NO`. No 1.25x.

### Four-Pillar Summary (Track 2 — Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROE Base | ROE 13.56% → 0.5x13.56 + 7.5 | 14.3x |
| B. Asset-Quality Multiplier (Pillar 2L) | 1.00x (Sound, operator override) | 1.00x |
| C. Quality-Adjusted Base | A x B | 14.3x |
| D. Growth Visibility Premium | 3a +0 / 3b +1 / 3c +0 | +1x |
| E. Strategic Premium | base (optional +1x noted) | +0x |
| F. Raw Destination PE | C + D + E | 15.3x |
| F2. UA-Adjusted | UA not qualified → F | 15.3x |
| G. Sector Cap | Banks/NBFCs/MFIs | 18x (absolute) |
| **H. Final Destination PE (Track 2)** | **min(F2, G)** | **15.3x** |

Track 2 destination range (±7.5%, nearest 0.5x): 15.3 x 0.925 = 14.15 → **14.0x**; 15.3 x 1.075 = 16.45 → **16.5x**. **Track 2: 14.0x–16.5x, mid 15.3x.**

### RRM Dual-Track Derivation

- Track 1 (RRM): Destination PE = Fundamental (Quality-Adjusted) Base PE x RRM, capped at sector cap.
- r = CoE = **13.5%** (derivation above; aligned to CoE, one mechanism).
- RRM = 1 + (13.5 − r) x 0.12, percentage-point reading (Amendment 4.4) = 1 + (13.5 − 13.5) x 0.12 = **1.00** (within bounds 0.70–1.60).
- Track 1 Destination PE = 14.3x x 1.00 = **14.3x** (cap 18x — clears).
- Track 1 range (±7.5%): 14.3 x 0.925 = 13.2 → **13.0x**; 14.3 x 1.075 = 15.4 → **15.5x**. **Track 1: 13.0x–15.5x, mid 14.3x.**

**Track divergence:** (15.3 − 14.3)/14.3 = **7.0%** (<15%). Tracks converge. **Governing track = Track 1 (RRM, 14.3x mid) — the more conservative; it sets the entry zone.** Both tracks sit BELOW the current ~18x market PE, i.e., a de-rating headwind is embedded.

### PRIMARY METHOD — Theoretical / Justified P/B (ROE / CoE)

- Justified P/B = ROE / CoE. At blended ROE 13.56% / CoE 13.5% = **1.00x**. The decisive fundamental fact: **ROE ≈ CoE, so FEDFINA creates ~zero economic spread and justifies ~1.0x book** — versus a market P/B of 2.09x. To justify 2.09x on ROE/CoE requires ROE ≈ 28% (13.5% x 2.09), which FEDFINA will not reach.
- Gordon cross-check: justified P/B = (ROE − g)/(CoE − g); when ROE = CoE this equals 1.0x for any g. Growth does not rescue the multiple when the spread is zero.
- For the exit (Year 3) I credit the evidenced forward recovery toward ~14.5% sustainable ROE: justified exit P/B base ≈ **1.05x**; bear (ROE ~11.5%) ≈ 0.85x; bull (ROE ~17%) ≈ 1.25x.

### Hurdle Ratio (Section 1B sanity check)

**HR = (1 + EPS CAGR)³ x (Destination PE mid ÷ Current PE). Pass ≥ 1.953.**
Current PE = 17.98x (CMP/EPS, internally consistent). Governing destination PE mid = 14.3x (Track 1). Bull EPS CAGR usable (credibility grade B).

| Row | Calculation | HR |
|---|---|---|
| Base (EPS CAGR 15%) | 1.15³ x (14.3/17.98) = 1.5209 x 0.7953 | **1.21** |
| Bull (EPS CAGR 20%) | 1.20³ x (14.3/17.98) = 1.728 x 0.7953 | **1.37** |

Robustness checks — all still fail 1.953:
- Track 2 mid 15.3x: HR base 1.29 / bull 1.47.
- Current PE at the 16.0x screener quote: HR base 1.36 / bull 1.54.
- Even crediting optional +1x strategic (mid ~16.3x): HR base 1.38.
- Break-even EPS CAGR to pass = 32%+ (not credible).

**Hurdle Ratio verdict = STOP.** The stock fails the 25% hurdle even on bull-case earnings — a de-rating headwind (destination PE ~14-15x below current ~18x) combined with moderate EPS growth. Per Amendment 2 / Master v3.3: complete the remaining sections for the record; verdict card says AVOID-on-valuation.

> **INTERIM CHECKPOINT (framework STOP point, pipeline continues):** Section 1 complete. Methods: P/B primary (60%), P/E secondary (40%). Four-pillar destination PE 14.0x–16.5x (Track 2), RRM track 13.0x–15.5x. Current PE ~18x. Hurdle Ratio 1.21 (base) / 1.37 (bull) → STOP.

---

## SECTION 2: EARNINGS, BOOK VALUE & PROJECTIONS

### 2A. Growth assumptions

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| EPS CAGR logic | ST-LAP in-housing slips again; credit cost breaks 1.1% (Pillar 2L self-withdraws to 0.80x); dilution | Historical PAT CAGR 18.5% discounted for grade-B delivery + ESOP/future dilution | Management guidance at face value (grade B permits); AUM ~20%, gold-branch maturation |
| EPS CAGR | 10% | **15%** | 20% |

- Historical anchors: PAT 3-yr CAGR 18.5%, revenue 17.3%, AUM 19.8% (B10). Base 15% sits below all three (dilution + conservatism). **SOM cross-check:** B09 SOM-implied revenue CAGR 23.6% (3-yr); my base ~15-17% revenue is BELOW it → CONSISTENT, no cut needed.

### 2B. Projection table (Year 0 = FY26)

| Line | Bear Y3 | Base Y3 | Bull Y3 |
|---|---|---|---|
| EPS (from 9.12) | 9.12 x 1.10³ = **12.14** | 9.12 x 1.15³ = **13.87** | 9.12 x 1.20³ = **15.76** |
| Book CAGR (ROE x ~0.95 retention) | ~10.5% | ~12.8% | ~14.7% |
| BVPS Y3 (from 78.2) | **105.4** | **112.2** | **118.0** |
| Est. ROE trajectory | ~11.5% | ~14.5% | ~17% |

### 2C. Sanity checks

| Check | Result | Pass? |
|---|---|---|
| AUM growth within branch/co-lending capacity? | Base 15-17% << SOM 23.6% ceiling; capex-embedded 12.6% supports | Yes |
| ROE stays consistent with FTTCP RECOVERING verdict used in Pillar 1? | Base Y3 ROE ~14.5% aligns with the 13.56% blend and 15% FY[Y+2] input | Yes |
| EPS growth operations-driven, not engineering? | Yes — AUM + NIM + credit-cost normalisation | Yes |
| FTTCP-consistency (Pillar 2L 1.00x vs asset-quality trajectory)? | Holds ONLY while Q4 FY26 credit cost ≤1.1% and PCR does not thin — self-withdraw live | Conditional |
| Dilution realistic? | CRAR 22.40% reduces near-term raise need; ESOP creep captured in the 15% base | Yes |

> **INTERIM CHECKPOINT:** Section 2 complete. Base EPS Rs 13.87, BVPS Rs 112.2 at Year 3. SOM cross-check consistent.

---

## SECTION 3: APPLY EACH METHOD

### PRIMARY — P/B (justified exit P/B x Year-3 book)

| | Bear | Base | Bull |
|---|---|---|---|
| BVPS Y3 | 105.4 | 112.2 | 118.0 |
| Justified exit P/B | 0.85x | 1.05x | 1.25x |
| **P/B fair value Y3** | **Rs 89.6** | **Rs 117.8** | **Rs 147.5** |

Base P/B fair value Rs 117.8 is **28% BELOW CMP 164**. The primary lender method alone says overvalued.

### SECONDARY — P/E (destination PE x Year-3 EPS)

Using governing Track 1 range (13.0 / 14.3 / 15.5x):

| | Exit PE low 13.0 | Exit PE mid 14.3 | Exit PE high 15.5 |
|---|---|---|---|
| Bear EPS 12.14 | 157.8 | 173.6 | 188.2 |
| Base EPS 13.87 | 180.3 | **198.3** | 215.0 |
| Bull EPS 15.76 | 204.9 | 225.4 | **244.3** |

P/E fair values (diagonal): Bear Rs 157.8 (low PE), Base Rs 198.3 (mid), Bull Rs 244.3 (high).

**Method disagreement is material and diagnostic:** P/B base Rs 117.8 vs P/E base Rs 198.3 (~68% spread). The gap exists because the Section 1B PE (14.3x x ROE 13.56% = ~1.9x implied P/B) is generous relative to the fundamental justified P/B of ~1.0x when ROE ≈ CoE. This is exactly why the framework designates **P/B as PRIMARY and the destination PE as a SECONDARY cross-check for lenders** — the P/B read is the more conservative and more appropriate, and it governs.

### Method-wise fair value summary

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/B (primary) | 60% | 89.6 | 117.8 | 147.5 |
| P/E (secondary) | 40% | 157.8 | 198.3 | 244.3 |

> **INTERIM CHECKPOINT:** Section 3 complete. Primary P/B base Rs 117.8 (below CMP). Secondary P/E base Rs 198.3.

---

## SECTION 4: TRIANGULATION, ENTRY & VERDICT

### 4A. Triangulated fair value (both tracks)

**Track 1 (RRM, governing)** — P/E leg uses 13.0/14.3/15.5x:

| | Bear | Base | Bull |
|---|---|---|---|
| P/B x 60% | 53.8 | 70.7 | 88.5 |
| P/E x 40% | 63.1 | 79.3 | 97.7 |
| **Weighted FV (Y3)** | **Rs 116.9** | **Rs 150.0** | **Rs 186.2** |

**Track 2 (Additive)** — P/E leg uses 14.0/15.3/16.5x:

| | Bear | Base | Bull |
|---|---|---|---|
| P/B x 60% | 53.8 | 70.7 | 88.5 |
| P/E x 40% | 68.0 | 84.9 | 104.0 |
| **Weighted FV (Y3)** | **Rs 121.8** | **Rs 155.6** | **Rs 192.5** |

### 4B. Methods agreement

- Direction: both methods point the same way at the base — fair value at/below CMP. Spread ~68% at the method level; P/B is the trusted primary for this archetype and the outlier is the PE, which embeds a multiple the ROE does not support.

### 4C / 4D. Return expectation and probability-weighted CAGR (Track 1, governing)

Credibility grade **B → weights Bear 25% / Base 50% / Bull 25%** (sole source: Master v3.3 4D). No Role-4 re-weighting trigger evidenced.

| Scenario | Weighted FV (Y3) | 3-yr CAGR from CMP 164 | Prob | Contribution | ≥25%? |
|---|---|---|---|---|---|
| Bear | 116.9 | −10.7% | 25% | −2.68% | No |
| Base | 150.0 | −2.9% | 50% | −1.45% | No |
| Bull | 186.2 | +4.3% | 25% | +1.08% | No |
| **Expected CAGR** | | | 100% | **−3.1%** | **No** |

### 4E. Entry price (off Track 1 base FV Rs 150.0)

| Calculation | Value |
|---|---|
| Base fair value (Y3) | Rs 150.0 |
| 25% CAGR entry = FV / 1.953 | Rs 76.8 |
| 30% CAGR entry = FV / 2.197 | Rs 68.3 |
| MoS price (20% below 25% entry) | Rs 61.4 |
| **Entry range** | **Rs 68 – 77** |

### 4F. Risk-reward asymmetry

- Bull upside from CMP: (186.2/164) − 1 = **+13.5%**.
- Base upside: (150.0/164) − 1 = **−8.5%** (no upside).
- Bear downside: (116.9/164) − 1 = **−28.7%**.
- Upside/downside (bull upside ÷ bear downside) = 13.5 / 28.7 = **0.47x** (must be ≥2x — FAILS badly; base case has no upside at all).

### 4G. Exit-multiple validation

| Check | Result | Pass? |
|---|---|---|
| Year-3 ROE justifies ROE base + matches FTTCP RECOVERING? | ~14.5% base vs 13.56% blend | Yes |
| Year-3 asset-quality justifies Pillar 2L 1.00x? | Only while Q4 FY26 credit cost ≤1.1% + PCR holds; self-withdraw live | Conditional |
| Primary catalyst (credit-cost normalisation) fired by Y3 base? | Assumed yes | Yes |
| Strategic premium single-credit respected? | Yes — ROE recovery in Pillar 1 only; strategic +0x | Yes |
| UA ordering correct — min(F x1.25, Cap)? | UA not qualified; F=F2 | Yes |
| Would I buy this at ~18x / 2.09x book for a 12.6% ROE recovering NBFC? | No | No |

### 4H. VERDICT CARD

```
FEDBANK FINANCIAL SERVICES (FEDFINA) — ROLE 1 VALUATION
CMP Rs 164 | Market cap Rs 6,132 Cr | BVPS Rs 78.2 | Mkt P/B 2.09x | Mkt P/E 16.0x (CMP/EPS 18.0x)

FOUR-PILLAR EXIT PE (lender carve-out):
  Pillar 1 (ROE): FTTCP RECOVERING 40-60% → 60/40 blend of 12.6% + 15.0% = 13.56%
                  → 0.5x13.56 + 7.5 = 14.3x base. Recovery credited via Pillar 1.
  Pillar 2L (Asset-Quality): 1.00x Sound (OPERATOR OVERRIDE; self-withdraws to 0.80x
                  if Q4 FY26 credit cost >1.1% or PCR thins). Quality-Adjusted Base 14.3x.
  Pillar 3 (Growth Visibility): +1x (3a +0 / 3b +1 EM 25.3 / 3c +0).
  Strategic: +0x base (optional +1x Federal Bank backing noted; verdict robust either way).
  Raw PE (F) 15.3x | UA not applied | Sector cap 18x absolute.
  DESTINATION PE (Track 2 additive): 14.0x – 16.5x (mid 15.3x)
RRM TRACK: r = CoE 13.5% → RRM 1.00 → Track 1 destination 13.0x – 15.5x (mid 14.3x)
  Divergence 7.0% (<15%). GOVERNING = Track 1 (conservative). Both below current ~18x → de-rate.
PRIMARY (P/B): justified P/B = ROE/CoE ≈ 1.0x (ROE≈CoE, zero spread) vs market 2.09x.
HURDLE RATIO: base 1.21 / bull 1.37 (threshold 1.953) → STOP.
METHODS: P/B 60% + P/E 40%.
WEIGHTED FAIR VALUE (Y3):  Track 1  Bear 117 | Base 150 | Bull 186
                           Track 2  Bear 122 | Base 156 | Bull 193
EXPECTED CAGR (prob-weighted, grade B 25/50/25): -3.1%
UPSIDE/DOWNSIDE: 0.47x (fails ≥2x; base case has no upside)
ENTRY RANGE: Rs 68 – 77 | MoS PRICE: Rs 61
DECISION: AVOID (on valuation)
```

**Key assumptions that could change the valuation:**
- ▲ Q4 FY26 + subsequent prints confirming ROE toward 16-18% (peer level) would lift justified P/B toward 1.2-1.3x and Pillar 1 base — but even then the entry sits well below CMP.
- ▲ Optional +1x Federal Bank strategic premium (destination ~16.3x) — still HR STOP.
- ▼ Q4 FY26 credit cost >1.1% or PCR thinning → Pillar 2L self-withdraws to 0.80x → Quality-Adjusted Base falls to ~11.4x, destination ~12.4x, fair value cut further.
- ▼ ST-LAP in-housing slips again / DA reliance not wound down → EPS bear path.

**Exit framework (for the record):** target exit at destination ~15x if ever bought in-zone; thesis-broken if ROE fails to cross 14% by FY28 or credit cost breaks 1.1%; PE-compression floor ~13x; time stop 3 years.

**SHARED CATALYST (carried for Role 3):** credit-cost normalisation drives BOTH the asset-quality transition (Pillar 2L) and the return transition (Pillar 1 ROE). Single point of failure — Role 3 must stress-test it.

**FLAGS CARRIED:** FLAG-CASH (structural, no multiplier penalty — Pillar 2L used); FLAG-ASSETQUALITY; FLAG-EMOAT-BORDERLINE; FLAG-GUIDANCE-SLIPPAGE; FLAG-ASSET-QUALITY-OVERRIDE (Pillar 2L 1.00x, self-withdraw); FLAG-Q4-FY26-DATA-GAP.

> **CLOSING:** Valuation complete. Four-pillar exit PE 14.0x–16.5x (RRM 13.0x–15.5x). Hurdle Ratio STOP. Entry range Rs 68–77, MoS Rs 61. Decision: AVOID (on valuation). At Rs 164 the market already pays ~2.09x book / ~18x earnings for a 12.6% ROE (ROE ≈ CoE) recovering NBFC; the multiple it earns sits below where it trades, and no 25% CAGR path exists at this price even on bull earnings.

---

```yaml
stage: B11-valuation
company: "FEDFINA"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
input_gaps:
  - "FY-wise ROE/ROA series FY21-FY26 NOT FOUND — blocks Amendment 9 Route B (pre-cycle normalized ROE); standard FTTCP RECOVERING blend used instead"
  - "Q4 FY26 quarter-only credit cost / RoA / RoE not anchored — Pillar 2L 1.00x self-withdraw condition cannot be confirmed"
flags:
  - "FLAG-CASH: structural NBFC Ind AS 7 (CFO/PAT -5.04x); Pillar 2L used, NO cash multiplier penalty applied"
  - "FLAG-ASSETQUALITY: PCR thin 32-38% vs 60-70% norm; impairment spike"
  - "FLAG-ASSET-QUALITY-OVERRIDE: Pillar 2L 1.00x is operator override; self-withdraws to 0.80x if Q4 FY26 credit cost >1.1% or PCR thins"
  - "FLAG-Q4-FY26-DATA-GAP: Q4 FY26 quarter-only actuals non-anchored"
  - "FLAG-EMOAT-BORDERLINE: EM 25.3 bottom edge; Pillar 3 +1x"
  - "FLAG-GUIDANCE-SLIPPAGE: ST-LAP in-housing slipped Q2->Q3->Q4"
  - "SHARED-CATALYST: credit-cost normalisation drives both Pillar 1 (ROE) and Pillar 2L (asset quality) — Role 3 stress-test"
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 13.0, mid: 14.3, high: 15.5, r_used: 13.5, rrm: 1.00}
  track2_additive: {low: 14.0, mid: 15.3, high: 16.5}
  divergence_pct: 7.0
  governing_track: "Track 1 RRM (14.3x mid, more conservative); tracks converge within 7%, both below current ~18x PE (de-rating headwind)"
pillar_detail:
  roce_used: 13.56              # ROE blend (60% x 12.6 + 40% x 15.0), lender uses ROE
  roce_base: 12.6               # current ROE
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 1.00         # Pillar 2L Asset-Quality Multiplier (Sound, override); NOT the cash multiplier
  structural_or_growth: "structural (lender; FLAG-CASH structural per Ind AS 7, no penalty; Pillar 2L applied)"
  growth_offset: 0
  growth_premium: 1
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 18
hurdle_ratio: {base: 1.21, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 117, base: 150, bull: 186}
  track2: {bear: 122, base: 156, bull: 193}
expected_cagr_prob_weighted: -3.1
entry_range: {low: 68, high: 77}
mos_price: 61
upside_downside_ratio: 0.47
decision: "AVOID (on valuation)"
unresolved_inputs_used:
  - "FY[Y+2] expected ROE = 15.0% (set from ROA ~2.55% x leverage ~6.0x; rating agency ROA 2.50%, peer band; capped below peer best, conservative)"
  - "Cost of Equity = 13.5% (small/mid NBFC base 13-14%; AA+ Federal Bank parentage offset by governance CAUTION and asset-quality flags)"
  - "Pillar 2L 1.00x carried from operator override with self-withdraw condition (Q4 FY26 credit cost >1.1% or PCR thins -> 0.80x)"
som_cagr_crosscheck: "consistent — base EPS CAGR 15% and implied revenue CAGR ~15-17% sit below B09 SOM-implied 23.6% (3-yr); no cut needed"
one_line_thesis: "AVOID FEDFINA at Rs 164: a 12.6% ROE (ROE approx CoE 13.5%, near-zero economic spread) recovering NBFC already priced at 2.09x book / ~18x earnings, whose earned four-pillar destination PE of 14-16x sits BELOW the current multiple, so the Hurdle Ratio is STOP and probability-weighted 3-yr CAGR is -3.1%; entry only at Rs 68-77 (MoS Rs 61). Key risk / shared catalyst: credit-cost normalisation drives both the asset-quality and ROE transitions."
```
