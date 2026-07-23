# STAGE 11 — ROLE 1 DUAL-TRACK VALUATION: AYE FINANCE LIMITED

**Run date:** 2026-07-22 | **Model:** claude-opus-4-8 | **Run type:** full, first workup
**Frameworks:** Master v3.3 (Role 1) / Section 1B v3.3 as reconciled by Section 1B v3.5.1 / FTTCP v1.2
**Input source:** B10-valinputs (sole input authority); operator-approved pillars from fttcp-deliberation.md carried through B10 (AUTHORITATIVE, not re-derived)

**Tier: A | Hurdle: 25% (divisor 1.953, HR pass threshold 1.953)**
**Business model: Lending (NBFC-ML, balance-sheet lender). P/B is PRIMARY; destination PE is SECONDARY cross-check (Section 1B Amendment 7). Pillar 1 uses ROE, not ROCE. Pillar 2 is the Asset-Quality Multiplier.**

---

## 0. INTERIM CHECKPOINT LINE (framework STOP points, written then continued per pipeline override)

> Section 1 complete. Methods selected: P/B primary (theoretical P/B = ROE / CoE), Section 1B destination PE secondary, forward-EPS × destination-PE for entry/hurdle. Four-pillar destination PE (additive) = 15.4x to 16.0x (mid 15.7x); operator-approved base = 15.0x (forward basis, FY29 horizon); RRM track = 9.6x to 11.2x (mid 10.4x). Current forward PE (FY27E) = 15.4x. Hurdle Ratio base = 1.77 (FAIL), bull = 2.00 (PASS) → CONDITIONAL. Proceeding to projections and verdict in one pass.

---

## 1. INPUTS CARRIED FROM B10 (anchors on first use)

| Input | Value | Anchor (via B10) |
|---|---|---|
| CMP | Rs 183.22 (NSE, 2026-07-22) | cmp_note.md line 7 |
| Shares outstanding (diluted) | ~25.2 Cr | cmp_note.md line 9 |
| Market cap | ~Rs 4,614 Cr | cmp_note.md line 8 |
| 52-week range | Rs 88.22 (since-listing low) to Rs 197.29 | cmp_note.md line 12-13 |
| BVPS (Q1FY27, latest) | Rs 100.32 | B01 line 48 (NW Rs 2,528.01 Cr / 25.2 Cr) |
| BVPS (FY26 audited) | Rs 97.81 | results__edbf1e94 p.11 line 849 |
| FY26 PAT / EPS (basic/diluted) | Rs 193.63 Cr / Rs 9.73 / Rs 9.60 | results__edbf1e94 p.6 lines 447, 854-855 |
| Q1FY27 PAT / EPS | Rs 74.5 Cr / Rs 3.02 (basic) | B01 line 48 |
| Trailing PE (FY26) | 18.8x | B10 (183.22 / 9.73) |
| Trailing PE (Q1FY27 annualized) | 15.1x | B10 (183.22 / [3.02×4]) |
| Current P/B (Q1FY27 / FY26) | 1.83x / 1.87x | B10 multiples table |
| Pillar 1 ROE anchor (Route A, normalized) | 11.7%-13% | fttcp-deliberation.md line 50 (via B10) |
| Pillar 2 Asset-Quality Multiplier | 1.00x (Sound) | fttcp-deliberation.md line 51 (via B10) |
| Pillar 3 total | +2x (3a +2 / 3b +0 / 3c +0) | fttcp-deliberation.md line 52 (via B10) |
| Strategic premium | +0x (barred, single-credit) | fttcp-deliberation.md line 53 (via B10) |
| UA multiplier | NOT APPLIED (FII+DII 35.45%) | fttcp-deliberation.md line 54 (via B10) |
| Approved destination (exit) PE | 15x, FORWARD basis, FY29 horizon | fttcp-deliberation.md lines 27, 35 (via B10) |
| Sector cap (absolute) | 18x (Banks/NBFCs/MFIs) | Section 1B Amendment 8 (via B10) |
| Credibility grade | C (Mixed) | B10 credibility_grade |
| 4D probability weights (grade C) | 35 / 45 / 20 (bear/base/bull) | Master v3.3 / wrapper |
| FTTCP RoA/RoE forward verdict | RECOVERING | fttcp-deliberation.md line 16 |
| FTTCP cash | STRUCTURAL + residual INDETERMINATE (gain on derecognition) → caps gate at PROCEED WITH CAVEATS | fttcp-deliberation.md line 17; CLAUDE.md |

**Input discipline note:** Forward EPS (FY27) is in B10.unresolved (FY27 PAT not audited; Q4FY26 concall not collected). Per the pipeline conservative-assumption rule, forward EPS is built here as a LABELLED PROJECTION off the anchored base (FY26 PAT Rs 193.63 Cr; Q1FY27 PAT Rs 74.5 Cr annualized ~Rs 300 Cr) and stated as a projection everywhere it is used. It is never treated as an anchor.

---

## 2. PRIMARY METHOD — THEORETICAL P/B (LENDER, Section 1B Amendment 7)

**Formula (framework canonical):** theoretical P/B = ROE ÷ CoE.

**Cost of equity (stated):** CoE = **14.5%**. Build: risk-free ~6.7% (India 10-yr G-sec, run-window) + beta ~1.15 (small-cap NBFC) × equity risk premium ~6.5% = ~14.2%, rounded to 14.5%. This sits just below the RRM required-return r (~15-16%) used for a Tier A transition NBFC, consistent with a required-return premium over CoE. [CoE is an analyst input, not a B10 anchor; stated per instruction.]

### 2a. Static theoretical P/B on the approved ROE anchor (no growth credit)

| ROE anchor | ÷ CoE 14.5% | Fair P/B | × BVPS Rs 100.32 (Q1FY27) | Fair value/share |
|---|---|---|---|---|
| 11.7% (low) | 11.7 / 14.5 | 0.81x | 0.81 × 100.32 | **Rs 81** |
| 13.0% (high) | 13.0 / 14.5 | 0.90x | 0.90 × 100.32 | **Rs 90** |
| 12.35% (mid) | 12.35 / 14.5 | 0.85x | 0.85 × 100.32 | **Rs 86** |

**Static P/B fair value = Rs 81-90 (mid Rs 86).** Current P/B is 1.83x versus a static fair P/B of 0.81-0.90x. On a no-growth basis the stock trades at ~2.1x its static fair P/B. The recovery is deliberately NOT in this number (the approved anchor holds ROE at 11.7-13% and credits the recovery elsewhere — see the destination-PE cross-check). This static floor Rs 81-90 is a conservative downside anchor and, notably, brackets the since-listing low of Rs 88.22.

### 2b. Growth-adjusted sanity (Gordon: P/B = (ROE − g) ÷ (CoE − g))

- On the suppressed anchor (ROE 13%, g 8%, CoE 14.5%): (13 − 8) / (14.5 − 8) = 5 / 6.5 = **0.77x**. When ROE < CoE, growth destroys value — the growth-adjusted P/B is BELOW the static one, confirming the anchor alone does not support today's multiple.
- On a fully recovered destination ROE (16%, g 10%, CoE 14.5%): (16 − 10) / (14.5 − 10) = 6 / 4.5 = **1.33x**. Even a recovered ~16% ROE with premium growth justifies only ~1.2-1.4x P/B, still below the current 1.83x.

**Primary-method read:** on P/B, AYE is fully-to-richly valued at CMP. Justifying 1.83x requires the market to price forward ROE recovery to ~16-18% AND durable premium growth simultaneously. That is the transition bet; it is not yet earned (grade C, one clear AUM miss).

---

## 3. SECONDARY CROSS-CHECK — SECTION 1B DESTINATION PE, DUAL TRACK

### 3a. Pillar worksheet (lender variant; ROE feeds Pillar 1; AQ multiplier is Pillar 2)

**Pillar 1 normalization route (v3.5.1 consolidated Amendment 9):** **Route A governs — B suppressed** (post-IPO excess capital stripped from the denominator → operational ROE; Route B pre-cycle condition also present but suppressed per single-credit rule). Route declared per worksheet line: statutory/current ROE ~7.63% (H1FY26 annualized, B03 line 24) → Route A operational normalized ROE anchor **11.7%-13%** (fttcp-deliberation.md line 50). ROCE recovery credited via **Pillar 1 midpoint**; Strategic Premium ROE re-rating **barred** (+0x).

**Pillar 1 base PE** (Amendment 5, ROE form: 0.5 × ROE% + 7.5, floor 9x, cap 24x):
- ROE 11.7% → 0.5×11.7 + 7.5 = **13.4x**
- ROE 13.0% → 0.5×13.0 + 7.5 = **14.0x**
- ROE 12.35% (mid) → **13.7x**

**Pillar 2 (Asset-Quality Multiplier) = 1.00x (Sound):** GNPA 4.49% marginally above 4% but falling 4 consecutive quarters; PCR 63.8% inside the 60-70% Sound band; ECL 3.4x RBI floor (fttcp-deliberation.md line 29). No growth offset (loan growth cannot offset underwriting; Amendment 7). Quality base = 13.4-14.0x × 1.00 = **13.4-14.0x**.

**Pillar 3 = +2x** (3a growth visibility +2 on documented ~26% AUM machinery, capped at +2 by delivery grade C; 3b moat +0, EM 19.6 MODEST < 25; 3c duration +0, no contracted revenue).

**Strategic = +0x** (barred, single-credit). **UA not applied** (F2 UA row: not qualified — only 1 of 3 Amendment-3 qualifiers met; FII+DII 35.45% far above the 3% institutional-absence test).

### 3b. Four-Pillar Summary (F2 UA row shown)

| Step | Calculation | Value |
|---|---|---|
| A. Pillar 1 ROE base PE (ROE 11.7-13%) | 0.5×ROE + 7.5 | 13.4x - 14.0x |
| B. Pillar 2 AQ multiplier | × 1.00x (Sound) | 13.4x - 14.0x |
| C. Pillar 3 growth/duration | + 2x | 15.4x - 16.0x |
| D. Strategic premium | + 0x (barred) | 15.4x - 16.0x |
| F. Raw destination PE | — | **15.4x - 16.0x (mid 15.7x)** |
| F2. UA-adjusted raw PE | not qualified → no ×1.25 | 15.4x - 16.0x |
| G. Sector cap (absolute) | 18x | not binding |
| H = min(F2, G) | — | **15.4x - 16.0x** |
| Destination PE range (H ±7.5%) | 15.7x ±7.5% | 14.5x - 16.9x (cap 18x) |

**Additive (Track 2) destination PE ≈ 15.4-16.0x, mid 15.7x.** The **operator-approved 15.0x sits at/just below the additive floor** — a conservative choice fully supported by the additive track. Approved 15x governs (used for all fair values, entry, hurdle).

### 3c. RRM track (Track 1) — shown for transparency, does NOT override the approved 15x

RRM = 1 + (13.5 − r) × 0.12 (percentage points; Amendment 4.4), bounded ×0.70 to ×1.60. For a Tier A transition NBFC, r ~15-16%:

| r | RRM = 1 + (13.5 − r)×0.12 | Fundamental base PE (13.7x) × RRM | RRM destination PE |
|---|---|---|---|
| 15.0% | 1 + (−1.5)(0.12) = 0.82 | 13.7 × 0.82 | 11.2x |
| 15.5% (mid) | 1 + (−2.0)(0.12) = 0.76 | 13.7 × 0.76 | **10.4x** |
| 16.0% | 1 + (−2.5)(0.12) = 0.70 | 13.7 × 0.70 | 9.6x |

**RRM (Track 1) destination PE ≈ 9.6-11.2x, mid 10.4x.**

### 3d. Track divergence and governing choice

- Additive (Track 2) mid **15.7x** vs RRM (Track 1) mid **10.4x**: divergence **~34%** (>15% threshold). Against the approved 15x, RRM is **~31% lower**.
- The framework default is "the more conservative track sets the entry zone" (RRM here → ~10.4x). **However, the operator approved 15x at the FTTCP pillar-approval gate on the forward basis, and the deliberation is explicit that the RRM divergence must be SHOWN but does NOT override the approved 15x.** Governing track for the entry zone and verdict = **operator-approved 15x (additive-consistent)**.
- **Flag (carried to Role 3 / synthesis):** the RRM track — which prices durability and governance through the discount rate — counsels a materially lower destination PE (10.4x) and a fair value well below CMP. On RRM the stock is AVOID-on-valuation (see 5c). This divergence is the single most important valuation tension in the name: the approved 15x embeds a required-return assumption (~13.5% implied) below the ~15-16% an investor would reasonably demand for a grade-C, FLAG-CASH transition NBFC.

---

## 4. FORWARD EPS PROJECTION (LABELLED PROJECTION — NOT AN ANCHOR)

**Anchored base points:** FY26 PAT Rs 193.63 Cr / EPS Rs 9.73 (results__edbf1e94 p.6). Q1FY27 PAT Rs 74.5 Cr (B01 line 48) → annualized ~Rs 298-300 Cr → **FY27E EPS ≈ Rs 11.90** (Rs 300 Cr / 25.2 Cr). The Q1FY27-annualized base already embeds the credit-cost recovery (FY26 quarterly-average PAT ~Rs 48 Cr vs Q1FY27 Rs 74.5 Cr). *This is a projection; FY27 is not yet reported. Conservative caveat: if Q1FY27 is a peak recovery quarter, FY27 could land nearer Rs 270-290 Cr; the HR/entry are stress-checked against this below.*

**Scenario forward EPS CAGR (FY27→FY30, 3-year hold to FY29 exit; forward-consistent):**

| Scenario | Drivers (projection) | 3-yr EPS CAGR | Exit EPS (11.90 × (1+g)³) | Exit target @ 15x (Track 2) | Exit target @ 10.4x (Track 1 RRM) |
|---|---|---|---|---|---|
| Bear | AUM slows to ~18%, dilution from capital raise, RoA plateaus ~3.5% | 15% | 11.90 × 1.521 = 18.10 | Rs 272 | Rs 188 |
| Base | AUM ~25%, modest dilution, RoA stable ~4.0% | 22% | 11.90 × 1.816 = 21.62 | **Rs 324** | Rs 225 |
| Bull | AUM ~28%, minimal dilution, RoA to 4.5% | 28% | 11.90 × 2.097 = 24.95 | Rs 375 | Rs 260 |

**SOM cross-check (Master Role 1):** base EPS CAGR 22% sits BELOW the documented AUM-growth machinery (25-28%), the gap being dilution and a conservative RoA path. Assumption does not exceed the SOM-implied growth → **consistent** (no cut required).

**FTTCP-consistency row:** base case (RoA held ~4.0%, AUM ~25%, GNPA continuing to ease) is consistent with the FTTCP RECOVERING RoA/RoE verdict; it does not assume a return to the FY24 peak (RoA 3.7% / ROE 17.28%) nor a collapse. Bull (RoA 4.5%) matches management's 3-year 4.0-4.5% RoA target but is grade-C credibility-capped in the hurdle check below.

---

## 5. HURDLE RATIO, FAIR VALUES, ENTRY ZONE (governing track = approved 15x)

### 5a. Hurdle Ratio (forward basis — EPS basis kept CONSISTENT on numerator and denominator)

**Current forward PE = CMP / FY27E EPS = 183.22 / 11.90 = 15.4x.** De-rating term = 15 / 15.4 = 0.975. (The stock already trades at ~15.4x the recovered forward number — essentially AT the 15x destination; almost no re-rating is available, so return must come from EPS growth.)

**HR = (1 + forward EPS CAGR)³ × (Destination PE ÷ Current forward PE):**

| Scenario | (1+CAGR)³ | × 0.975 | HR | Pass ≥1.953? |
|---|---|---|---|---|
| Bear (15%) | 1.521 | | 1.48 | FAIL |
| Base (22%) | 1.816 | | **1.77** | FAIL |
| Bull (grade-C capped 27% = base+5%) | 2.048 | | **2.00** | PASS |

Bull EPS CAGR for the HR is capped at Base + 5% = **27%** because credibility grade is **C (Mixed)** (Amendment 2 conservative-bias rule; the true 28% bull is used only for the fair-value target, not the hurdle test).

**HR verdict = CONDITIONAL** (base fails, bull passes). Flag: **"growth-dependent with de-rating headwind."** Verdict capped at WATCHLIST / BUY-ON-DIPS; no BUY NOW at CMP.

### 5b. Fair values, entry zone, MoS (governing = Track 2, approved 15x)

- Bear / Base / Bull 3-year targets: **Rs 272 / Rs 324 / Rs 375**.
- **Entry price = base fair value ÷ 1.953 (Tier A) = 324 / 1.953 = Rs 166.**
- **MoS = 20% below entry = 166 × 0.80 = Rs 133.**
- **Buy zone (accumulate) = Rs 133 - Rs 166.**
- CMP Rs 183.22 is **~10% ABOVE the Rs 166 hurdle entry** → not a buy at CMP; watch for the zone.

### 5c. RRM (Track 1) fair values — the conservative counterpoint (flagged, non-governing)

- Bear / Base / Bull targets: **Rs 188 / Rs 225 / Rs 260**. Entry = 225 / 1.953 = **Rs 115**; MoS **Rs 92**. On RRM the stock is **AVOID-on-valuation at CMP** (CMP Rs 183 vs RRM base fair value Rs 225 and RRM entry Rs 115). Shown per deliberation; does not override the approved 15x.

### 5d. Probability-weighted expected return at CMP (grade C: 35/45/20)

Price CAGR to Track-2 targets over 3 years: bear (272/183.22)^⅓−1 = 14.1%; base (324/183.22)^⅓−1 = 20.9%; bull (375/183.22)^⅓−1 = 27.0%.
**Prob-weighted CAGR = 0.35×14.1 + 0.45×20.9 + 0.20×27.0 = 19.7%.** Below the 25% Tier A hurdle at CMP.

### 5e. Risk / reward at CMP

- Reward = base target Rs 324 − CMP Rs 183.22 = **+Rs 141 (+76.8% over 3 yrs)**.
- Risk = CMP Rs 183.22 − static-P/B floor ~Rs 86 (Section 2a; ≈ since-listing low Rs 88.22) = **−Rs 97 (−53%)**.
- **Upside/downside ≈ 1.45x.** Modest — the recovery is largely priced.

---

## 6. TRIANGULATION

| Method | Role | Fair value read at CMP |
|---|---|---|
| Theoretical P/B (PRIMARY), static anchor | Primary | Rs 81-90; CMP richly valued (1.83x vs 0.81-0.90x static) |
| Theoretical P/B, recovered-ROE Gordon | Primary sanity | ~1.2-1.4x P/B; CMP still above |
| Destination PE 15x forward, Track 2 (approved) | Secondary | 3-yr base target Rs 324; entry Rs 166; CMP ~10% above entry |
| Destination PE RRM 10.4x, Track 1 | Secondary (flagged) | 3-yr base target Rs 225; AVOID-on-valuation at CMP |
| Hurdle Ratio (forward) | Gate | CONDITIONAL (base 1.77 fail, bull 2.00 pass) |
| Prob-weighted CAGR | Return test | 19.7% < 25% at CMP |

All methods agree on direction: **AYE is fairly-to-richly valued at CMP Rs 183.22; the 25% hurdle is not met at current price; it becomes a buy in the Rs 133-166 zone.** The primary (P/B) and the RRM secondary are more bearish than the approved-15x secondary; the approved 15x is the governing, most generous supported multiple, and even on it CMP does not clear the hurdle.

---

## 7. FTTCP GATE (separate from the buy decision)

- RoA/RoE forward verdict: **RECOVERING**.
- Cash: **STRUCTURAL** (negative CFO by design for a growing balance-sheet lender under Ind AS 7) **with a residual INDETERMINATE earnings-quality element** — gain on derecognition (securitisation) rising to 5.8% of revenue / ~3.65% of total income (FY26), inflating reported PAT growth.
- **FLAG-CASH carried forward.** Pillar 2 Asset-Quality Multiplier actually applied = **1.00x** (the FLAG is on earnings-quality via derecognition, not on the AQ band). Per CLAUDE.md the INDETERMINATE element caps the FTTCP gate at **PROCEED WITH CAVEATS**, with the missing evidence named: normalized PAT ex-derecognition by product line (B10 unresolved), and FY27 audited PAT.

---

## 8. VERDICT CARD

**Tier: A | Hurdle: 25%**

| Field | Value |
|---|---|
| CMP / Market cap | Rs 183.22 / ~Rs 4,614 Cr |
| PRIMARY method (P/B) fair value | Rs 81-90 static (0.81-0.90x); ~1.2-1.4x P/B even on recovered ROE — CMP richly valued |
| Destination PE — approved (governing) | 15.0x, FORWARD basis, FY29 horizon (additive-consistent; additive mid 15.7x) |
| Destination PE — RRM (flagged) | 10.4x mid (r 15.5%, RRM 0.76) — 31% below approved; AVOID-on-valuation on this track |
| Current forward PE (FY27E) | 15.4x |
| Hurdle Ratio (forward) | Base 1.77 FAIL / Bull(cap 27%) 2.00 PASS → **CONDITIONAL** ("growth-dependent with de-rating headwind") |
| Fair values (Track 2, 15x): Bear/Base/Bull | Rs 272 / Rs 324 / Rs 375 |
| Fair values (Track 1, RRM 10.4x): Bear/Base/Bull | Rs 188 / Rs 225 / Rs 260 |
| Entry zone (base 324 ÷ 1.953) | **Rs 166** (buy zone Rs 133-166 with MoS) |
| MoS price | Rs 133 |
| Prob-weighted CAGR at CMP (35/45/20) | 19.7% (< 25%) |
| Upside/downside | ~1.45x |
| FTTCP gate | PROCEED WITH CAVEATS (FLAG-CASH INDETERMINATE earnings-quality; AQ multiplier applied 1.00x) |
| **DECISION** | **WATCHLIST (BUY-ON-DIPS)** — accumulate Rs 133-166; not a buy at CMP (on-valuation) |

**One-line thesis:** Recovering micro-enterprise NBFC priced at fair value on the approved 15x forward; 25% returns need >26% forward EPS CAGR that a grade-C record and rising derecognition gains have not yet earned — watch, buy below Rs 166.

---

```yaml
stage: B11-valuation
company: "AYE"
run_date: "2026-07-22"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Forward EPS (FY27): FY27 PAT not audited; Q4FY26 concall not collected. Built here as a LABELLED PROJECTION off anchored base (FY26 PAT Rs 193.63 Cr; Q1FY27 PAT Rs 74.5 Cr annualized ~Rs 300 Cr, FY27E EPS ~Rs 11.90). Never treated as an anchor."
  - "Normalized PAT ex-derecognition by product line: unresolved in B10; needed to fully clear the residual INDETERMINATE earnings-quality element."
  - "Peer P/E, P/B, ROCE/RoA medians: unresolved in B10; peer cross-check is secondary for a lender (P/B primary) and not blocking."
flags:
  - "FLAG-CASH: STRUCTURAL negative CFO (balance-sheet lender, Ind AS 7) with residual INDETERMINATE earnings-quality element (gain on derecognition 5.8% of revenue / ~3.65% of total income, FY26). Pillar 2 Asset-Quality Multiplier ACTUALLY APPLIED = 1.00x. Caps FTTCP gate at PROCEED WITH CAVEATS (CLAUDE.md NEVER rule); missing evidence named: normalized PAT ex-derecognition, FY27 audited PAT."
  - "FLAG-RRM-DIVERGENCE: RRM track destination PE 10.4x is ~31% below the approved 15x; on RRM AYE is AVOID-on-valuation at CMP (base fair value Rs 225, entry Rs 115). Shown per deliberation; approved 15x governs and does NOT get overridden, but the required-return gap (approved implies ~13.5% vs ~15-16% reasonable for a grade-C FLAG-CASH transition NBFC) is the key valuation tension for Role 3/synthesis."
  - "FLAG-HURDLE-CONDITIONAL: base HR 1.77 fails; only the grade-C-capped bull (27%) clears at 2.00. Growth-dependent with de-rating headwind; verdict capped at WATCHLIST/BUY-ON-DIPS."
  - "FLAG-EARNINGS-QUALITY / FLAG-ASSET-QUALITY / FLAG-GATE0 / FLAG-EXTERNAL-TRIPWIRES carried forward from B10 unchanged."
framework_versions: "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2"
pe_basis: "forward"
exit_pe_base_approved: 15.0
destination_pe:
  track1_rrm: {low: 9.6, mid: 10.4, high: 11.2, r_used: 15.5, rrm: 0.76}
  track2_additive: {low: 15.4, mid: 15.7, high: 16.0}
  divergence_pct: 31
  governing_track: "operator-approved 15x (additive-consistent, sits at additive floor = conservative); RRM 10.4x shown for transparency, does NOT override per FTTCP deliberation gate"
pillar_detail:
  roce_used: 12.35
  roce_base: 7.63
  roce_recovery_route: "pillar1-midpoint"
  pillar1_normalization_route: "A-governs-B-suppressed"
  cash_multiplier: 1.00
  structural_or_growth: "lender Asset-Quality Multiplier 1.00x (Sound); FTTCP cash STRUCTURAL with residual INDETERMINATE earnings-quality element (gain on derecognition)"
  growth_offset: 0
  growth_premium: 2
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 18
hurdle_ratio: {base: 1.77, bull_used: true, verdict: "CONDITIONAL"}
fair_values:
  track1: {bear: 188, base: 225, bull: 260}
  track2: {bear: 272, base: 324, bull: 375}
expected_cagr_prob_weighted: 19.7
entry_range: {low: 133, high: 166}
mos_price: 133
upside_downside_ratio: 1.45
decision: "WATCHLIST (BUY-ON-DIPS); on-valuation — accumulate Rs 133-166, not a buy at CMP Rs 183.22 (base hurdle fails, prob-weighted CAGR 19.7% < 25%)"
unresolved_inputs_used:
  - "Forward EPS FY27: conservative projection FY27E EPS ~Rs 11.90 from Q1FY27 PAT Rs 74.5 Cr annualized (~Rs 300 Cr / 25.2 Cr), because FY27 is unaudited and the framework requires a labelled forward projection for the operator-approved forward-basis PE and hurdle; stress-noted that a peak-quarter Q1 could imply FY27 nearer Rs 270-290 Cr."
  - "CoE 14.5%: analyst input (not a B10 anchor), stated per instruction for the primary theoretical P/B; built from risk-free ~6.7% + beta ~1.15 x ERP ~6.5%, consistent with RRM r ~15-16% region."
som_cagr_crosscheck: "consistent"
one_line_thesis: "Recovering micro-enterprise NBFC priced at fair value on the approved 15x forward; 25% returns need >26% forward EPS CAGR a grade-C record and rising derecognition gains have not yet earned — watch, buy below Rs 166."
```
