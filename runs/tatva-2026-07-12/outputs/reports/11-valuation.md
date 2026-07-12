# STAGE 11: ROLE 1 MULTI-MODAL VALUATION (AMENDMENT 4.5 REFRESH)
## Tatva Chintan Pharma Chem Ltd (TATVA)
**Run Date:** 2026-07-12 | **Model:** claude-opus-4-8 | **CMP:** Rs 1,326.0
**Mode:** Valuation-only refresh under Section 1B Amendment 4.5 (v3.5) Normalized-ROCE anchor.
**Framework authority:** Master v3.3 (Role 1) / Section 1B v3.3 + Amendment 4.5 (v3.5) / FTTCP v1.2. Where wrapper and framework conflict, the injected framework wins.

> **Scope note.** This is a valuation refresh in which the ONLY changed input versus the prior run is the Pillar 1 ROCE anchor. FY29 EPS projections (base Rs 30.65, bull Rs 43.74) are carried unchanged from the prior run per instruction, so that the entire delta in destination PE, fair value, entry zone and decision is attributable to the Amendment 4.5 ROCE anchor alone. Every number carries a B10 anchor the first time it is used. Missing data is NOT FOUND, never estimated.

---

## PIPELINE CHECKPOINT LINES (framework STOP gates, executed continuously)

- **After Section 1:** "Section 1 complete. Methods selected (P/E primary). Four-pillar destination PE 10.5x-12.5x additive (RRM track 8.5x-10.0x). Current PE 73.8x. Hurdle Ratio 0.22 (Track 1) / 0.26 (Track 2) -> STOP." Continuing.
- **After Section 2:** "Section 2 complete. FY29 EPS bear 21.5 / base 30.65 / bull 43.74 (base & bull carried from prior run). FTTCP-consistency row passes at RECOVERING. Continuing."
- **After Section 3:** "Section 3 complete. P/E primary, EV/EBITDA and P/B cross-checks confirm direction (deep discount to CMP). Continuing."
- **Close:** "Valuation complete. Four-pillar exit PE 11.4x additive / 9.4x RRM. Hurdle Ratio STOP. Entry Rs 118-147 (governing Track 1). Decision: AVOID (on valuation)."

---

## INPUT DISCIPLINE — UNRESOLVED FIELDS

**INPUT UNRESOLVED: rating_wc_quote. Conservative assumption used: Pillar 2 = 0.80x with NO growth offset, because** B10 marks cash conversion INDETERMINATE leaning structural and no CRISIL/CARE working-capital language is available (B10 unresolved: "No Rating PDF provided in inputs/rating/"). Framework rule (wrapper item 3; Master v3.3 Pillar 2): when B10 marks cash INDETERMINATE, use the more conservative multiplier and state so. The 0.80x band with no offset is that conservative floor; the 0.65x "structural confirmed" band is NOT used because it requires rating-agency confirmation that is NOT FOUND.

All other inputs resolved from B10. Peer medians NOT COMPUTED (B10: empty screener P&L/Balance_Sheet exports); peer-relative methods are therefore not weighted, only noted.

---

## SECTION 1A: METHOD SELECTION & JUSTIFICATION

TATVA is asset-intensive, four-product specialty chemicals manufacturing (B10: "Manufacturing, four-product specialty chemicals"), cyclical earnings, high working-capital intensity, currently trough-ROCE (6.6%, B10 Deliberation line 45), FCF-negative in all 8 computable years (B10: cumulative FCF/PAT -1.32x).

| Method | Suitable Here? | Weight | Justification |
|---|---|---|---|
| **P/E (Four-Pillar exit PE)** | YES — PRIMARY | 70% | Section 1B is the sole exit-multiple authority (CLAUDE.md NEVER rule). Earnings are the value driver; the four-pillar destination PE prices ROCE quality, cash, growth, scarcity, sector cap. |
| **EV/EBITDA** | YES — SECONDARY | 20% | Capital-intensive, leverage present (net debt Rs 114.6 Cr, B10). Cross-checks the PE anchor; capex >> depreciation caveat lowers the multiple. |
| **P/B** | YES — TERTIARY | 10% | Cyclical at/near trough; theoretical P/B = ROE/CoE is a clean floor check with ROE depressed to 5.4% (B10). |
| PEG | No | — | Growth is cyclical/volatile; PEG unreliable on a trough base. |
| EV/Sales, EV/Capacity | No | — | Margin profile shifting; capacity utilisation (64.11%/30.54%, B10) not yet stabilised. |
| DCF | No (reference only) | — | FCF negative every year (B10); terminal-value dominated and unreliable for an inflection cyclical. |
| DDM / P-EV / P-AUM / SOTP | No | — | Not a dividend compounder, insurer, AMC, lender, or conglomerate. |

Final selection: PRIMARY P/E 70% | SECONDARY EV/EBITDA 20% | TERTIARY P/B 10%.

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 + AMENDMENT 4.5

### FTTCP handoff (sole Pillar 1 authority)

- Backward ROCE verdict: **TEMPORARILY DEPRESSED** (B10: FY24 10.91% -> FY25 1.20% -> FY26 6.6%, capital-cycle trough from Dahej capex + post-IPO cash bloat; "if growth stopped tomorrow, would ROCE recover" test passes -> temporary, not structural).
- Forward ROCE verdict: **RECOVERING, probability 40-60%** (B10 Master Summary: "Verdict RECOVERING, probability 40-60%").
- Both conditions of Amendment 4.5 are met (TEMPORARILY DEPRESSED backward AND RECOVERING forward). **Amendment 4.5 applies.**

### Amendment 4.5 gate check (both required, both present)

| Gate | Evidence | Status |
|---|---|---|
| Historical ROCE series showing pre-depression level | B10 normalized_roce: FY18 18.8%, FY19 20.0%, FY20 24.9%, FY21 25.4%; median **22.45%**, computed on B01 EBIT/(Net Worth + Borrowings) basis, screener Data_Sheet FY18-21 | PASS (documented) |
| Specific mechanical unwind catalyst | B10: Dahej capacity commissioning entering revenue phase — new block operational Jan 2026, confirmed fully operational by Q4 FY26; reactor utilisation 64.11% / assembly-line 30.54% (FY24-25) with headroom toward 75-80% target (B05 line 51, B04 unit_economics line 60, Deliberation line 50) | PASS (documented) |

Both gates are 📄-documented. Normalized ROCE 22.45% does NOT exceed the evidenced pre-depression median (it IS the median). Amendment 4.5 is live. Had either gate been NOT FOUND, the amendment would not apply and the standard FTTCP 60/40 blend would stand.

### Pillar 1: ROCE Base Multiple (Amendment 4.5 three-anchor blend)

Amendment 4.5 replaces the RECOVERING row of the FTTCP v1.2 Pillar 1 table for the TEMPORARILY DEPRESSED case. For the **40-60% RECOVERING band**: Pillar 1 ROCE = **40% Normalized + 30% FY[Y+2] + 30% current**.

```
Pillar 1 ROCE = 0.40 x 22.45%  (Normalized, pre-depression median FY18-21, B10)
              + 0.30 x  8.5%   (FY28 = FY[Y+2] expected base, B10 Deliberation line 45)
              + 0.30 x  6.6%   (current FY26, B10 Deliberation line 45)
              = 8.98% + 2.55% + 1.98%
              = 13.51%
```

Feed into the continuous formula (Amendment 5, ROCE <= 33%): **Base PE = 0.5 x ROCE% + 7.5**, floor 9x, cap 24x.

```
Pillar 1 Base PE = 0.5 x 13.51 + 7.5 = 6.755 + 7.5 = 14.255 -> 14.26x
```
(One-decimal framework rounding = 14.3x; 14.26x carried through, immaterial.) Within floor 9x / cap 24x.

- FTTCP ROCE forward verdict: **RECOVERING, 40-60%**
- ROCE used for base (Amendment 4.5 blend): **13.51%**
- ROCE Base Multiple: **14.26x**
- **ROCE recovery credited via: Pillar 1** (Amendment 4.5 explicit; single-credit rule — the Strategic Premium ROCE re-rating option stays BARRED).

*Do NOT use the old 60/40 current+FY28 blend (that gave 7.36% -> 11.18x base). That is the prior-run anchor and is superseded here.*

### Pillar 2: Cash Conversion Multiplier

- Cumulative CFO/PAT (FY19-26): -1.32x (B10). Latest FY CFO/PAT: 0.75x (B10). FCF positive? **No** — FCF -Rs 822.8 Mn FY26, negative all 8 years (B10).
- Cash quality band: CFO/PAT below 30% cumulative / negative FCF -> **0.80x** band.
- Structural or growth-induced? **INDETERMINATE leaning structural** (B10 Deliberation line 21): receivables +18.1% while revenue fell; top-3 receivables concentration 61%; zero ECL; debtor days 48 -> 86 across FY22-26 through flat-revenue years (growth does not explain -> leans structural).
- **INPUT UNRESOLVED: rating_wc_quote = NOT FOUND.** Per framework, INDETERMINATE resolves to the more conservative treatment: **0.80x, NO growth offset** (the 0.65x structural-confirmed band requires rating-agency confirmation that is NOT FOUND, so it is not used; and the growth offset is barred because the drag is not cleanly growth-induced).
- Effective Cash Multiplier: **0.80x**
- **Quality-Adjusted Base = 14.26x x 0.80x = 11.408x -> 11.41x**

FLAG-CASH carried forward with the multiplier actually applied (0.80x).

### Pillar 3: Growth Visibility Premium (3a + 3b + 3c, combined cap +6x)

**3a Growth Visibility** (documented tier only): capex-embedded growth >=15%? NOT DOCUMENTED. Order book >=1.0x revenue / book-to-bill >=1.2x? NO (B10: no documented order book). SOM-implied revenue CAGR >=20%? NO (14.3% 3yr, B10). Delivery grade A or B? YES (grade B, B10). -> Only 1 of 4 qualifies; need any two for +2x. **3a = +0x.**

**3b Moat Formation** (EM-gated): EM 19.2/80 (B10), below the 25 threshold. **3b = +0x.**

**3c Duration Premium** (documented order book / contracted revenue tenor): no documented order book of any tenor (B10). **3c = +0x.**

**Pillar 3 total = +0x.**

### Strategic Asset Premium

Documented moats exist (switching costs, proprietary electrolysis route, DSIR/REACH/ZLD barriers — B10), but the ROCE re-rating optionality route is **BARRED by the single-credit rule** (recovery already credited in Pillar 1 via Amendment 4.5). No rare licence / regulatory monopoly of the +4-6x class is evidenced; moats are graded moderate durability, not genuine scarcity that limits entry. **Strategic Premium = +0x.** Single-credit state: recovery in Pillar 1 only.

### Shared-catalyst flag

Dahej commissioning drives **both** the Pillar 1 forward ROCE (Amendment 4.5 unwind catalyst) **and** the notional Pillar 3a growth premium (B10 Deliberation line 50). Flagged **SHARED CATALYST = TRUE** so Role 3 stress-tests the single point of failure. Note: because 3a paid +0x, no actual double-credit occurred; the flag is carried for the devil's advocate regardless.

### Undiscovered Alpha Multiplier

Qualifiers (all three required): listed >=12m = YES (IPO Jul 2021); Gate 0 >=60 OR EM >=25 = NO (Gate 0 48, EM 19.2, B10); FII+DII <3% = NO (B10). **all_met = false -> UA NOT applied. F2 = F.** (Per CLAUDE.md Amendment 3, low institutional ownership is not treated as a risk; the gate is simply not cleared.)

### Four-Pillar Summary Calculation

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 13.51% (4.5 blend) -> 0.5x13.51+7.5 | **14.26x** |
| B. Cash Multiplier (effective) | 0.80x band + offset 0 (INDETERMINATE leaning structural; rating NOT FOUND) | **0.80x** |
| C. Quality-Adjusted Base | A x B = 14.26 x 0.80 | **11.41x** |
| D. Growth Visibility Premium | 3a +0 / 3b +0 (EM 19.2<25) / 3c +0 | **+0x** |
| E. Strategic Premium | ROCE route barred (single-credit); no scarcity licence | **+0x** |
| F. Raw Destination PE | C + D + E | **11.41x** |
| F2. UA-Adjusted Raw PE | all_met false -> F2 = F | **11.41x** |
| G. Sector Cap | Specialty Chemicals (B10 corrected, overrides manifest 38x) | **35x (absolute)** |
| **H. Final Destination PE** | **min(F2, G) = min(11.41, 35)** | **11.4x** |

**Additive (Track 2) Destination PE Range: 11.41x +/-7.5% = 10.55x to 12.26x -> nearest 0.5x -> 10.5x to 12.5x (mid 11.4x).**

### RRM Dual-Track Derivation (both carried through)

- Base r for small/micro cap 14%, raised to **r = 15%** for durability/governance drag (FLAG-PROMOTER: GPCB plant closure Sep 2024, two CRISIL downgrades within review window, remuneration +27.89% while PAT fell 98.9%, B10 flags; FLAG-EMOAT weak execution). Bound [9%,18%] respected.
- **RRM = 1 + (13.5 - 15) x 0.12 = 1 + (-1.5)(0.12) = 1 - 0.18 = 0.82** (Amendment 4.4 percentage-point reading).
- **Track 1 (RRM) Destination PE = Quality-Adjusted/Raw Base 11.408x x 0.82 = 9.355x -> 9.4x**, capped at 35x (not binding).
- **Track 1 Range: 9.355x +/-7.5% = 8.65x to 10.06x -> 8.5x to 10.0x (mid 9.4x).**

**Track divergence:** (11.408 - 9.355) / 9.355 = **22.0% (>15%).** Governing track = **Track 1 (RRM)** — the more conservative (lower) FV, and the more appropriate track for a governance-flagged, cyclical micro-cap where the elevated discount rate (r=15%) is warranted. **Track 1 sets the entry zone.**

### Hurdle Ratio (Amendment 2 / 4.3 — Tier A, threshold 1.953)

Tier assignment: **Tier A (25% hurdle, divisor 1.953)** — default sleeve; the FII+DII test and Gate0/EM do not qualify it for Tier B, and structural FLAG-CASH bars Tier B outright.

Current PE = 1,326 / 17.98 (FY26 diluted EPS, B10) = **73.75x**.
Base EPS CAGR (FY26 17.98 -> FY29 30.65) = (30.65/17.98)^(1/3) - 1 = **19.5%**; (1+CAGR)^3 = 1.7047.
Bull EPS CAGR (17.98 -> 43.74) = **34.5%**; (1+CAGR)^3 = 2.4327. Grade B permits bull EPS in the HR check.

HR = (1 + EPS CAGR)^3 x (Destination PE mid / Current PE):

| Track | Base HR | Bull HR |
|---|---|---|
| Track 1 (RRM, mid 9.355x) | 1.7047 x (9.355/73.75) = **0.216** | 2.4327 x (9.355/73.75) = **0.309** |
| Track 2 (additive, mid 11.408x) | 1.7047 x (11.408/73.75) = **0.264** | 2.4327 x (11.408/73.75) = **0.376** |

**HR(Bull) = 0.31 / 0.38 << 1.953 -> STOP.** 25% CAGR is infeasible even on bull-case earnings, on either track. Would I personally pay 73.8x today for a business earning trough ROCE with negative FCF, to exit at ~11x? No.

*STOP does not halt the run (CLAUDE.md: only mechanical failures halt). Remaining sections completed for the record; the verdict card reads AVOID-on-valuation.*

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS

Base and bull FY29 (Year 3) EPS carried unchanged from the prior run per instruction (isolates the ROCE-anchor delta). Bear derived this run (prior bear not specified).

### 2A/2B/2C Projection (Year 0 = FY26, Year 3 = FY29)

| Line item | Bear | Base | Bull |
|---|---|---|---|
| Revenue CAGR (3yr) | 10% | 14.3% (= SOM 3yr) | 25% (FY27 guidance) |
| Revenue FY29 (Rs Cr) | 673 | 755 | 988 |
| EBITDA margin | 18.5% | 20% | 21% |
| FY29 EPS (Rs) | **21.5** | **30.65** | **43.74** |
| Implied FY29 PAT (Rs Cr) | 50.3 | 71.7 | 102.3 |
| Implied FY29 PAT margin | 7.5% | 9.5% | 10.4% |
| FY29 ROCE (est) | ~7% | ~9-10% | ~11-12% |

Base FY26 EPS 17.98 (B10). Base 3yr EPS CAGR 19.5%; bull 34.5%; bear 6.1%.

### 2D Sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth beyond capacity? | Base 14.3% = SOM ceiling; bull 25% exceeds SOM (flagged) | Base yes / Bull caveat |
| Margins require the unprecedented? | Base 20% is within guided 20-22% band and achieved 20.9% in Q4 FY26 (B10) | Yes |
| ROCE stays above 15%? | NO — projected 7-12%, still sub-15% even in base/bull | **FAIL (noted)** |
| FCF funds growth without excessive debt? | Doubtful — FCF negative history; capex-heavy | Caution |
| EPS growth operational, not engineered? | Yes — volume + margin recovery | Yes |
| Implied market-share gain realistic? | Base yes; bull optimistic vs SOM | Base yes |
| CFO/PAT trajectory consistent with Pillar 2 0.80x? | Yes — remains sub-elite | Yes |
| **FTTCP-consistency: Year 3 ROCE consistent with the RECOVERING verdict used in Pillar 1?** | Year 3 ROCE ~9-12% is a partial recovery off the 6.6% trough toward normalized 22.45% — consistent with RECOVERING (40-60%), NOT yet FIRING. The Amendment 4.5 blend (13.51%) sits between projected FY29 ROCE and the normalized anchor, as designed. | **Consistent** |

The sub-15% ROCE failure is exactly why the sector-cap and Hurdle discipline bind: the Amendment 4.5 anchor credits *sustainable* earning power (normalized 22.45%), not the projection window's still-recovering ROCE, but it does not manufacture a price the earnings cannot support.

---

## SECTION 3: APPLY EACH VALUATION METHOD

### PRIMARY — P/E (four-pillar exit PE, both tracks)

Exit PE: Track 1 (governing) 8.5x-10.0x (mid 9.355x); Track 2 10.5x-12.5x (mid 11.408x). No other exit PE used.

Year 3 (FY29) target = EPS x destination PE mid:

| | Track 1 (RRM, 9.355x) | Track 2 (additive, 11.408x) |
|---|---|---|
| Bear EPS 21.5 | Rs 201 | Rs 245 |
| Base EPS 30.65 | **Rs 287** | **Rs 350** |
| Bull EPS 43.74 | Rs 409 | Rs 499 |

Every cell is far below CMP Rs 1,326 -> all 🔴 (<15% CAGR); every scenario is a capital loss from today.

### SECONDARY — EV/EBITDA (cross-check)

Destination EV/EBITDA ~0.65x of PE destination -> Track 2 11.4x -> ~7.4x (capex >> depreciation argues the low end). Base FY29 EBITDA ~Rs 151 Cr x 7.4x = EV Rs 1,117 Cr; less net debt ~Rs 115 Cr = equity Rs 1,002 Cr / 2.339 Cr = **Rs 428 base**. Confirms direction (deep discount to CMP); slightly above the PE base because EBITDA masks the depreciation drag — hence P/E is weighted primary.

### TERTIARY — P/B (floor check)

Theoretical P/B = ROE / CoE. Base FY29 ROE ~9% / CoE ~14.5% = **0.62x**. FY29 BVPS ~Rs 405 (FY26 334.6 + ~3yr retained) x 0.62 = **Rs 251 base**. At CMP the stock trades at P/B 3.96x (B10) versus a theoretical ~0.6x — a ~6x premium to book-justified value. Reinforces AVOID.

### Method-wise Fair Value Summary (Year 3, base case)

| Method | Weight | Track 1 base | Track 2 base |
|---|---|---|---|
| P/E (four-pillar) | 70% | Rs 287 | Rs 350 |
| EV/EBITDA | 20% | Rs 350* | Rs 428 |
| P/B | 10% | Rs 251 | Rs 251 |
| **Weighted base FV** | 100% | **~Rs 292** | **~Rs 359** |

*EV/EBITDA is track-agnostic; RRM-scaled to ~Rs 350 for the Track 1 column. P/E dominates by weight; weighted values track the P/E anchor closely and the verdict is unchanged either way. For the entry/verdict below, the pure four-pillar P/E fair value is used as the primary anchor (Track 1 base Rs 287).*

---

## SECTION 4: TRIANGULATION, ENTRY PRICE & FINAL VERDICT

### 4A. Triangulated Fair Value (both tracks, Year 3 / FY29)

| | Bear | Base | Bull |
|---|---|---|---|
| **Track 1 (RRM) — governing** | Rs 201 | **Rs 287** | Rs 409 |
| **Track 2 (additive)** | Rs 245 | Rs 350 | Rs 499 |

### 4B. Methods agreement

All three methods point the same direction (deeply below CMP). Spread P/E vs EV/EBITDA vs P/B base = Rs 251-428, ~52% high-low, driven by depreciation treatment; P/E trusted most for this earnings-driven cyclical. No method comes within 3x of CMP.

### 4C / 4D. Return at CMP and probability-weighted expected return

Grade B weights (B10): Bear 25% / Base 50% / Bull 25%.

| Scenario | Track 1 FV | CAGR from CMP 1,326 | Weight | Weighted |
|---|---|---|---|---|
| Bear | Rs 201 | -46.7% | 25% | -11.7% |
| Base | Rs 287 | -40.0% | 50% | -20.0% |
| Bull | Rs 409 | -32.4% | 25% | -8.1% |
| **Expected 3yr CAGR (Track 1 governing)** | | | 100% | **-39.8%** |

(Track 2 expected CAGR = -35.6%.) Every scenario is a large negative CAGR; the stock is priced far above any four-pillar-justified value.

### 4E. Entry price (governing Track 1, Tier A divisor 1.953)

| Calculation | Value |
|---|---|
| Base fair value (Year 3, Track 1) | Rs 287 |
| Entry for 25% CAGR = 287 / 1.953 | **Rs 147** |
| Entry for 30% CAGR = 287 / 2.197 | Rs 131 |
| Margin-of-Safety price (20% below 25% entry) | **Rs 118** |
| **Ideal entry range** | **Rs 118 to Rs 147** |

Entry conjunction (anti-value-trap): a buy would execute only inside the zone AND with no thesis-broken trigger fired; here CMP Rs 1,326 is ~9x above the entry zone, so the point is academic.

### 4F. Risk-reward asymmetry

Bull target Rs 409, base Rs 287, bear Rs 201 — all below CMP Rs 1,326. Upside (base) = negative (-78%); downside (bear) = -85%. **Upside/downside ratio is not meaningful (effectively 0);** CMP trades at ~4.6x the Track 1 base fair value (~3.8x on Track 2). Fails the >=2x asymmetry test by construction.

### 4G. Four-Pillar exit-multiple validation

| Check | Result | Pass? |
|---|---|---|
| Year 3 ROCE justifies the ROCE base used? | Base used is the Amendment 4.5 *normalized-blend* 13.51% (sustainable earning power), explicitly above the FY29 projected 9-12% recovering ROCE — validated by the pre-depression 22.45% median + Dahej unwind, not by the projection window. Consistent with the amendment's design. | Yes (by amendment) |
| Year 3 CFO/PAT justifies 0.80x? | Yes — remains sub-elite, INDETERMINATE. | Yes |
| Primary catalyst fired by Year 3 (base)? | SDA invoicing ~Aug 2026 + Dahej ramp — yes in base. | Yes |
| Strategic premium justified (single-credit)? | +0x; ROCE route barred; respected. | Yes |
| UA ordering min(F x 1.25, Cap)? | UA not applied (all_met false); F2 = F. | Yes |
| Would you buy another stock at ~11x with these Year 3 metrics? | Only far below CMP. | N/A at CMP |

### 4H. FINAL VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP Rs 1,326.0 | Market Cap Rs 3,103 Cr** (B10)
- **FOUR-PILLAR EXIT PE (Amendment 4.5):**
  - Pillar 1 (ROCE base): FTTCP RECOVERING 40-60% -> **Amendment 4.5 three-anchor blend 0.40x22.45% + 0.30x8.5% + 0.30x6.6% = 13.51%** -> 0.5x13.51+7.5 = **14.26x**. ROCE recovery credited via **Pillar 1** (strategic ROCE route barred).
  - Pillar 2 (cash): **0.80x** (INDETERMINATE leaning structural, no offset; rating_wc_quote NOT FOUND -> conservative assumption). Quality-adjusted base **11.41x**.
  - Pillar 3: 3a +0 / 3b +0 (EM 19.2<25) / 3c +0 = **+0x**.
  - Strategic: **+0x** (single-credit).
  - Raw PE (F) **11.41x**; UA applied **N** (F2 = F); Sector cap **35x** (absolute, not binding).
  - **DESTINATION PE (additive): 11.4x, range 10.5x-12.5x (+/-7.5%).**
- **RRM TRACK:** r = 15%, RRM = 0.82 -> **Destination PE 9.4x, range 8.5x-10.0x.** Track divergence 22% (>15%) -> **governing track = Track 1 (RRM)**, sets entry zone.
- **HURDLE RATIO: Base 0.22 (T1) / 0.26 (T2); Bull 0.31 (T1) / 0.38 (T2) -> STOP** (bull fails; 25% CAGR infeasible even on bull earnings).
- **METHODS:** P/E 70% (primary), EV/EBITDA 20%, P/B 10%.
- **WEIGHTED FAIR VALUE (Year 3 / FY29):** Track 1 (governing) Bear Rs 201 / Base **Rs 287** / Bull Rs 409. Track 2 Bear Rs 245 / Base Rs 350 / Bull Rs 499.
- **EXPECTED 3yr CAGR (prob-weighted, grade B 25/50/25):** **-39.8%** (Track 1) / -35.6% (Track 2).
- **UPSIDE/DOWNSIDE:** not meaningful (~0); CMP ~4.6x base fair value.
- **ENTRY Rs 118-147 | MoS Rs 118** (governing Track 1).
- **DECISION: AVOID (on valuation).** Hurdle STOP. Gate 0 AVERAGE and structural FLAG-CASH independently support AVOID.
- **KEY ASSUMPTIONS THAT COULD MOVE THE VALUE:**
  - ▲ ROCE prints recovery ahead of schedule toward 22.45% -> Amendment 4.5 blend rises, Pillar 1 base lifts. ▼ Recovery fails to print -> **Amendment 4.5 self-withdrawal guard fires** (see below), reverting Pillar 1 to the current-weighted blend (~7.36% -> 11.18x base) and cutting fair value back toward the prior run.
  - ▲ Cash conversion turns (CFO/PAT >0.70x, debtor days compress, rating WC language obtained) -> Pillar 2 to 1.00x-1.15x. ▼ Structural confirmation -> 0.65x.
  - ▲ EM/order book documented -> Pillar 3 premiums unlock (currently +0x).
- **EXIT FRAMEWORK (for a future entry, not now):** target exit at destination PE 9-11x on recovered EPS; thesis-broken if ROCE fails to recover toward the pre-depression band or cash stays structurally negative; time stop 3-5y; PE compression floor already well below sector cap.
- **ONE-LINE THESIS:** "AVOID TATVA at Rs 1,326: even crediting sustainable ROCE via the Amendment 4.5 normalized anchor (13.51% blend of pre-depression 22.45% / FY28 8.5% / current 6.6%), the four-pillar destination PE is only 11.4x additive / 9.4x RRM, giving an FY29 base fair value of ~Rs 287-350 against a CMP that is ~4.6x higher; Hurdle Ratio STOP, expected 3yr CAGR ~ -40%. Cash quality: INDETERMINATE leaning structural."

### Amendment 4.5 self-withdrawal guard note

The normalized anchor (22.45%) is a **forward credit that must keep earning its place.** If, at the next quarterly refresh, the recovery does not show in the reported ROCE print (fails the FTTCP re-engagement threshold), OR the forward probability slips below the 40-60% RECOVERING band, OR the Dahej unwind catalyst dies, the **Normalized anchor is WITHDRAWN** and Pillar 1 reverts to the current-weighted (60/40) blend. This is the DECLINING backstop; a recovery that does not materialise is removed, not grandfathered. The re-open condition for this DEEP WATCH name keys off **evidence** (ROCE reverting toward the pre-depression level AND cash conversion turning), not a fixed trough-anchored price line.

### SOM cross-check

Base revenue CAGR 14.3% = SOM-implied 3yr CAGR 14.3% (B10) — **consistent, not cut.** Bull revenue CAGR 25% (FY27 guidance) exceeds SOM 14.3%; retained only because grade B permits guidance-at-face and TAM runway is GOOD (conservative TAM Rs 15,237 Cr vs SOM 3yr Rs 754 Cr), but flagged growth-dependent with a capacity-ceiling caveat (Jolva 4th-slip risk would make SOM binding, B10). Verdict: base consistent; bull a justified-but-flagged excess.

---

## HOW THE VALUATION MOVED VERSUS THE PRE-4.5 RUN

Only the Pillar 1 ROCE anchor changed; FY29 EPS held constant, so the entire delta is attributable to the ROCE anchor.

| Item | Prior run (60/40 current+FY28) | This run (Amendment 4.5 three-anchor) | Move |
|---|---|---|---|
| Pillar 1 ROCE | 7.36% (0.6x6.6 + 0.4x8.5) | **13.51%** (0.40x22.45 + 0.30x8.5 + 0.30x6.6) | +615 bps |
| Pillar 1 base PE | 11.18x | **14.26x** | +3.08x |
| Quality-adjusted base (x0.80) | 8.94x | **11.41x** | +2.47x |
| Destination PE (additive / RRM) | 9.0x / 7.3x | **11.4x / 9.4x** | ~+27% |
| Base FV Year 3 (Track 1 governing) | ~Rs 225 (prior reported band) | **Rs 287** | ~+22-28% |
| Entry zone | Rs 97-121 | **Rs 118-147** | ~+22% up |
| MoS price | Rs 97 | **Rs 118** | +Rs 21 |
| Hurdle Ratio | STOP | **STOP** | unchanged |
| Decision | AVOID (Hurdle STOP) | **AVOID (Hurdle STOP)** | unchanged |

**Interpretation.** Amendment 4.5 does exactly what it was designed to do: it stops pricing the FY26 capital-cycle trough as permanent, lifting the destination PE ~27% and the entry/MoS zone ~22% by crediting the evidenced pre-depression 22.45% ROCE through the normalized anchor. But it does NOT relax the cap or the Hurdle — cash quality is still policed at 0.80x, premiums are still +0x, the sector cap is untouched. Because CMP Rs 1,326 sits ~4.6x above even the lifted base fair value, the Hurdle Ratio remains a decisive STOP and the decision stays **AVOID (on valuation)**. The amendment corrects the fair value and the re-open zone (so the process will not miss a genuine capital-cycle recovery); it does not turn an overvalued price into a buy. The anchor is self-withdrawing if the recovery fails to print.

---

```yaml
stage: B11-valuation
company: "TATVA"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
input_gaps:
  - "rating_wc_quote NOT FOUND (no Rating PDF in run inputs); Pillar 2 held at conservative 0.80x, no offset"
  - "Peer medians NOT COMPUTED (empty screener P&L/Balance_Sheet exports); peer-relative methods noted, not weighted"
flags:
  - type: "FLAG-CASH"
    multiplier_applied: 0.80
    reason: "INDETERMINATE leaning structural; FCF negative 8 years, cumulative FCF/PAT -1.32x; debtor days 48->86 FY22-26; top-3 receivables 61%, zero ECL; rating WC language NOT FOUND. Conservative 0.80x, no growth offset."
  - type: "FLAG-EMOAT"
    reason: "EM 19.2/80 MODEST; Pillar 3 premiums all +0x; Jolva execution slipped 3x; credit downgrades."
  - type: "FLAG-PROMOTER"
    reason: "CAUTION: GPCB plant closure Sep 2024 (revoked); two CRISIL downgrades in window; remuneration +27.89% while PAT fell 98.9%."
  - type: "SHARED-CATALYST"
    reason: "Dahej commissioning drives both Pillar 1 (Amendment 4.5 unwind) and notional Pillar 3a; 3a paid +0x so no double-credit, flagged for Role 3."
framework_versions: "Master v3.3 / Section 1B v3.3 + Amendment 4.5 (v3.5) / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 8.5, mid: 9.4, high: 10.0, r_used: 15, rrm: 0.82}
  track2_additive: {low: 10.5, mid: 11.4, high: 12.5}
  divergence_pct: 22
  governing_track: "Track 1 RRM — more conservative (lower FV) and appropriate for a governance-flagged cyclical micro-cap at r=15%; sets entry zone"
pillar_detail:
  roce_used: 13.51
  roce_base: 14.26
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 0.80
  structural_or_growth: "INDETERMINATE leaning structural (conservative 0.80x, no offset; rating_wc_quote NOT FOUND)"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 35
hurdle_ratio: {base: 0.22, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 201, base: 287, bull: 409}
  track2: {bear: 245, base: 350, bull: 499}
expected_cagr_prob_weighted: -39.8
entry_range: {low: 118, high: 147}
mos_price: 118
upside_downside_ratio: 0
decision: "AVOID (on valuation) — Hurdle STOP; CMP ~4.6x base fair value; unchanged from pre-4.5 run despite ~27% higher destination PE"
unresolved_inputs_used:
  - "rating_wc_quote NOT FOUND -> Pillar 2 held at 0.80x with no growth offset (INDETERMINATE leaning structural, conservative treatment per framework)"
som_cagr_crosscheck: "base 14.3% consistent with SOM 14.3%; bull 25% exceeds SOM (guidance-at-face, grade B), flagged growth-dependent with capacity-ceiling caveat"
one_line_thesis: "AVOID TATVA at Rs 1,326: even crediting sustainable ROCE via the Amendment 4.5 normalized anchor (13.51% blend of pre-depression 22.45% / FY28 8.5% / current 6.6%), four-pillar destination PE is only 11.4x additive / 9.4x RRM, FY29 base fair value ~Rs 287-350 vs CMP ~4.6x higher; Hurdle STOP, expected 3yr CAGR ~ -40%. Cash quality: INDETERMINATE leaning structural."
```
