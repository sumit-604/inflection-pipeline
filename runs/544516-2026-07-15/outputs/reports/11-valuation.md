# STAGE 11 — ROLE 1 MULTI-MODAL VALUATION (Section 1B v3.3, dual-track)
## Airfloa Rail Technology Ltd (Ticker 544516)

**Run date:** 2026-07-15 | **Operator:** Keerti Kaushik | **Model:** claude-opus-4-8
**Framework:** Master v3.3 / Section 1B v3.3 (Amendments 1-8, 4.1-4.5) / FTTCP v1.2
**Sole input source:** B10 (`outputs/reports/10-assembly.md`), authoritative deliberation (`outputs/final/fttcp-deliberation.md`)

Pipeline mode: all sections executed in one pass; framework STOP gates written as checkpoints, not halts. Exit PE derived solely from Section 1B. Conservative bias throughout.

> **CORRECTION RE-RUN NOTE (top-of-file):** This run corrects ONE framework error caught by the valuation-adherence verifier. **Pillar 3a was previously credited +2x; it is corrected here to +0x.** Under **Amendment 4.1 (Section 1B)** the SOM-implied revenue CAGR qualifies for 3a **only "with the capacity cross-check passing."** B09's capacity cross-check **FAILED**: SOM_3yr revenue Rs 568 Cr exceeds the ~Rs 450 Cr near-term capacity ceiling by ~Rs 118 Cr (B09 Section 3C; B10 Line 367). The SOM qualifier therefore does NOT count. Only the order-book qualifier (Rs 469 Cr = 1.47x FY26 revenue, ≥1.0x) legitimately holds. One qualifier pays **+0x** (any two are needed for +2x; the grade-C +2x cap is moot with one qualifier). Hence **3a = +0x, Pillar 3 total = +0x**. All downstream multiples, fair values, entry zone, hurdle and verdict are recomputed off this. EVERY OTHER judgment is held identical to the prior verified run.

---

## EPS-BASIS DECLARATION (load-bearing — read first)

B10 carries current P/E two ways, on two DIFFERENT share bases. They are NOT interchangeable:

- **16.89x** = CMP 315 / diluted TTM EPS Rs 18.67. The Rs 18.67 is struck on FY26 **weighted-average** shares (~2.094 Cr), which are lower than the current count because the IPO shares (listed 18-Sep-2025) were only part-year weighted (B10 Line 36, 229).
- **19.3x** = market cap Rs 756 Cr / PAT Rs 39.1 Cr, i.e. current EPS = 39.1 / **2.397 Cr current shares** = **Rs 16.31**, PE = 315 / 16.31 = 19.31x (B10 Line 17-18, 34).

**Basis chosen: CURRENT-SHARE basis (2.397 Cr shares), current EPS Rs 16.31, current PE 19.3x.** Rationale: forward FY27+ earnings accrue to the full 2.397 Cr shares already outstanding, so forward EPS must be divided by 2.397 Cr. To keep the Hurdle Ratio numerator and denominator on one basis, the CURRENT PE must also be struck on 2.397 Cr shares (19.3x), NOT the weighted-average 16.89x. Mixing the 16.89x current PE with current-share forward EPS growth would understate current PE by ~14% and fabricate a spurious Hurdle pass (the SFL lesson). This entire valuation holds 19.3x / Rs 16.31 / 2.397 Cr shares consistently.

---

## SECTION 1A — METHOD SELECTION

Business model: capital-heavy B2B project/tender contract manufacturer (railway components, interiors, aerospace/defence), negative FCF, government/PSU-cycle working capital (B10 Line 12, 42-48).

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E (four-pillar destination) | 60% | Profitable (PAT margin 12.2%), clean earnings, Section 1B is sole exit-PE authority. Earnings-quality drives value here. |
| SECONDARY | EV/EBITDA | 25% | Capital-intensive, carries net debt Rs 55.23 Cr; neutralises leverage vs peer TEXRAIL. |
| TERTIARY | P/B | 15% | Asset-heavy post-IPO; book Rs 98.74/sh anchors a floor; useful given negative near-term cash. |
| EXCLUDED | DCF | 0% | Negative FCF (-Rs 74.6 Cr), 21-56% growth range → terminal-value dominated and unstable. Fails the DCF suitability test. |
| EXCLUDED | DDM | 0% | No dividend history (DPS 0). |

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE (both tracks)

### Pillar 1 — ROCE Base Multiple

- FTTCP ROCE forward verdict: **STAGNANT** (deliberation Ruling 6/7; B10 Line 60).
- STAGNANT → Pillar 1 uses **CURRENT ROCE** = **24.9%** on the company-reported restated basis (FY24 26.42% / FY25 26.28% / FY26 ~24.9%). The Gate 0 41.30%/25.22% split is a formula artifact and is NOT used. Amendment 4.5 normalized anchor does NOT apply (no self-reversing depressed trough; deliberation Ruling 6).
- Continuous formula (Amendment 5): Base PE = 0.5 × 24.9 + 7.5 = 12.45 + 7.5 = **19.95 → 20.0x** (floor 9x, cap 24x; within bounds).
- **ROCE recovery credited via: NOT CREDITED** (STAGNANT — no forward uplift entered Pillar 1; Strategic Premium ROCE re-rating route also barred because there is no genuine recovery to credit, FTTCP single-credit rule).

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT (FY25-26): **-0.93x**; latest FY26 CFO/PAT **-1.47x**; FCF negative (-Rs 74.6 Cr) (B10 Line 46-48).
- Cash quality band: CFO negative → base band **0.80x** ("growth-phase drag").
- **Structural or growth-induced: GROWTH-INDUCED** (operator override, authoritative deliberation Override 1; falsifier on record). Evidence: debtor days stable-to-improving (217-230 FY23-25 → 195 FY26), pre-surge FY23-24 had positive OCF, negative OCF coincides with +66% revenue surge; "if growth stopped tomorrow" test passes (deliberation Override 1; B10 Line 105-106).
- **Growth offset: NOT separately added → effective multiplier 0.80x.** The operator override that moved the multiplier from the structural 0.65x to 0.80x already embeds the growth-induced credit. Adding a growth-CAGR offset (+0.20 for >40% CAGR) on top of the override would double-credit the growth-induced determination — barred by CLAUDE.md ("never credit one quality improvement through two mechanisms") and the task instruction ("do not double-credit"). This matches the authoritative deliberation preview (quality base 16.0x = 20.0 × 0.80). **growth_offset = 0.**
- **INPUT UNRESOLVED: rating_wc_quote.** Conservative assumption: Pillar 2 is already fixed at 0.80x by the operator override with a documented falsifier; no rating-agency structural-WC confirmation exists that would push to 0.65x, so proceed at 0.80x (per authoritative deliberation). Falsifier: if H1 FY27 standalone OCF still negative AND >6m receivables share still rising above 23.4% AND debtor days tick up → reverts to STRUCTURAL, multiplier 0.65x (B10 Line 104, 107).
- **Quality-Adjusted Base = 20.0 × 0.80 = 16.0x.**

### Pillar 3 — Growth Visibility Premium (decoupled, Amendments 4.1/4.2, combined +6x cap)

**3a Growth Visibility (documented machinery, 📄 only):**
- capex-embedded growth ≥15%: not documented with the specific calc → does not qualify.
- order book ≥1.0x revenue: Rs 469 Cr / 319.6 = **1.47x ≥ 1.0x → QUALIFIES** (B10 Line 106). *(This is the one qualifier that legitimately holds.)*
- SOM-implied CAGR ≥20% **with capacity cross-check passing**: SOM-implied 21.1% ≥ 20%, BUT the **capacity cross-check FAILS** — SOM_3yr revenue **Rs 568 Cr exceeds the ~Rs 450 Cr near-term capacity ceiling by ~Rs 118 Cr** (B09 Section 3C; B10 Line 367). **Amendment 4.1 requires the capacity cross-check to PASS for the SOM CAGR to qualify. It does not. → DOES NOT QUALIFY.** *(Corrected from the prior run, which wrongly credited this qualifier by testing SOM against the 20% floor alone and ignoring the capacity gate.)*
- delivery grade A/B: grade **C** → does not qualify.
- **One qualifier (order book only) → +0x.** Two qualifiers are required for +2x. The grade-C cap on 3a (+2x) is moot with a single qualifier. **3a = +0x.**

**3b Moat Formation (EM-gated table):** EM = 14.5 (< 25) → **3b = +0x** (B10 Line 91).

**3c Duration Premium:** documented contracted order book 1.47x < 2.5 years → **3c = +0x** (B10 Line 106).

**Pillar 3 total = 3a +0x + 3b +0x + 3c +0x = +0x** (within +6x cap).

**SHARED CATALYST flag: YES (forward risk, now no double-credit exposure).** The 14-acre facility capex and the BBBS JV drive both near-term growth and any future ROCE lift, and the working-capital drain competes for the same capital — single point of failure (deliberation Handoff; B10 Line 130). Note: with the Pillar 3 growth premium now **not credited**, there is no double-credit exposure this run; the flag is retained purely as a forward risk surface for Role 3 to stress-test.

### Strategic Asset Premium

- Rare licence/regulatory monopoly: NO (qualification barriers ICF/HAL/DRDO/IREPS are moderate-durability, not a monopoly licence; B10 Line 92).
- Brand/pricing power: NO (margin compressed 500bps; only ~50-60% cost pass-through).
- ROCE re-rating optionality: barred — ROCE is STAGNANT (no recovery to credit) and single-credit rule.
- **Strategic Premium = +0x.**

### Four-Pillar Summary (Track 2 — Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 24.9% → 0.5×24.9+7.5 | 20.0x |
| B. Cash Multiplier (effective) | 0.80x (growth-induced; no double-credit offset) | 0.80x |
| C. Quality-Adjusted Base | 20.0 × 0.80 | 16.0x |
| D. Growth Visibility Premium (3a+3b+3c) | +0 + 0 + 0 (3a SOM disqualified by failed capacity cross-check; order-book alone is one qualifier = +0) | +0.0x |
| E. Strategic Premium | — | +0.0x |
| F. Raw Destination PE | 16.0 + 0 + 0 | **16.0x** |
| F2. UA-Adjusted Raw PE | UA **WITHHELD** (listed ~10m < 12m) → F unchanged | 16.0x |
| G. Sector Cap | Cables / Industrial products | 25x |
| **H. Final Destination PE** | **min(16.0, 25)** | **16.0x** |

**Track 2 Destination PE range: 16.0 ±7.5% = 14.8-17.2 → 14.8x to 17.2x. Mid 16.0x.**

UA note: only 2 of 3 qualifiers met (listed ~10 months fails the 12-month gate; Gate 0 76 and FII+DII 1.07% pass). 1.25x WITHHELD this run; eligible ~Sep 2026 (B10 Line 115-119).

### RRM Dual-Track Derivation (Track 1)

- Fundamental Base PE = quality base + growth premium (the fundamental earned multiple, ex-strategic) = 16.0 + **0.0** = **16.0x**.
- Base r (small/micro) = 14%; adjust UP for grade-C credibility (order-book miss, guidance walk-back, JV slip), negative OCF, and SME/short-listing discovery risk → **r = 15%** (bounded [9%,18%]). Moderate durability = neutral.
- RRM = 1 + (13.5 − 15) × 0.12 = 1 − 0.18 = **0.82** (percentage-point reading, Amendment 4.4; within ×0.70-×1.60 bounds).
- Track 1 Destination PE = 16.0 × 0.82 = **13.12 → 13.1x**, capped at 25x (not binding).
- **Track 1 range: 13.1 ±7.5% = 12.1-14.1 → 12.1x to 14.1x. Mid 13.1x.**

### Dual-track divergence

- Track 1 mid 13.1x vs Track 2 mid 16.0x. Divergence = (16.0 − 13.1)/16.0 = **18.1% (>15%).**
- **Governing track: Track 1 (RRM), the more conservative.** Why appropriate here: a grade-C, negative-OCF, ~10-month-listed SME with a moderate-durability moat warrants the required-return discount RRM applies through r. With the growth premium now correctly at +0x, both tracks collapse toward the quality base, and RRM discounts it further. RRM governs the entry zone.

### Hurdle Ratio (Section 1B sanity check) — CHECKPOINT

Current PE = **19.3x** (current-share basis, consistent). Base EPS CAGR = **21%** (SOM-capped; see 2A). Grade C → **Bull EPS CAGR capped at Base + 5% = 26%** (raw management bull NOT usable at grade C).

HR = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE). Pass ≥ 1.953 (Tier A, 25%).

| Track | Dest PE mid | PE ratio | Base HR (21%) | Bull HR (26%) | Verdict |
|---|---|---|---|---|---|
| Track 1 (governing) | 13.1x | 0.6788 | 1.7716×0.6788 = **1.20** | 2.0004×0.6788 = **1.36** | STOP |
| Track 2 | 16.0x | 0.8290 | 1.7716×0.8290 = **1.47** | 2.0004×0.8290 = **1.66** | STOP |

**Both tracks: HR(Bull) < 1.953 → STOP.** 25% CAGR is infeasible at Rs 315 even on grade-C-capped bull earnings. To clear 1.953 requires EPS CAGR ≈ **33.0%** on Track 2 and ≈ **42.2%** on Track 1 — both far above the 26% grade-C bull ceiling.

Divergence from the deliberation preview (which guessed CONDITIONAL): the preview used a ~16x raw destination and did not fix the current-PE basis. On the correct consistent 19.3x basis with SOM-capped 21% base growth and the grade-C 26% bull ceiling, the honest result is STOP — and the corrected +0x Pillar 3 brings the Track 2 raw destination to exactly the preview's ~16x, so the STOP is confirmed on the preview's own multiple. The verdict is robust: STOP holds decisively on both tracks.

🛑 Section 1 checkpoint: Four-pillar destination PE 14.8-17.2x (Track 2) / 12.1-14.1x (Track 1 RRM). Current PE 19.3x. Hurdle Ratio → **STOP**. Continuing to Section 2 for the record.

---

## SECTION 2 — EARNINGS & CASH FLOW PROJECTIONS

### 2A. Revenue (current-share basis; SOM cross-check binding)

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| Logic | Order book stalls, margin compresses, JV slips again | Order book executes, growth normalises to SOM ceiling | Guidance partly met, mild margin recovery |
| Revenue CAGR | 12% | **21%** | ~24% |
| FY26 Revenue (Yr0) | 319.6 | 319.6 | 319.6 |
| Yr3 Revenue | 449 | 566 | 610 |

**SOM cross-check:** SOM-implied 3yr CAGR = 21.1% (Yr3 revenue Rs 568 Cr; B10 Line 367-368). Base assumption 21% (Yr3 Rs 566 Cr) **sits at the SOM ceiling — CONSISTENT, not cut, not exceeded** (base EPS CAGR held per task instruction). FY27 guidance Rs 500 Cr (56.5%) is NOT used for the 3yr base because it exceeds SOM and rests on grade-C credibility; order book covers only ~70% of it.

**Capacity caveat (new, load-bearing):** the same capacity cross-check that disqualified the Pillar 3a SOM qualifier also flags a DOWNSIDE risk to the base: the near-term capacity ceiling (~Rs 450 Cr, B09 Section 3C) sits **below** the Yr3 base revenue (Rs 566 Cr) by ~Rs 116 Cr. The base therefore assumes the 14-acre expansion lands on time and on budget; if it slips, base revenue is capacity-constrained toward the bear path. This asymmetry reinforces the conservative posture and the AVOID verdict.

### 2B. Profitability

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| PAT margin | 10.5% (raw-material inflation, no pass-through) | 12.2% (held at FY26; no recovery guided) | 12.8% (mild leverage) |
| Dilution over 3yr | 0% | 0% | 0% (base; watch BBBS JV Rs 25 Cr) |

### 2C. Projection table (BASE case primary)

| Line | Yr0 (FY26) | Yr3 (base) |
|---|---|---|
| Revenue (Rs Cr) | 319.6 | 566.2 |
| PAT (Rs Cr) | 39.1 | 69.1 |
| EPS (Rs, /2.397 Cr) | **16.31** | **28.83** |
| ROCE (est) | 24.9% | ~24-25% (stagnant, per FTTCP) |

**Scenario Yr3 EPS (current-share basis):**
- Bear (6% EPS CAGR): 16.31 × 1.06³ = **Rs 19.43**
- Base (21% EPS CAGR): 16.31 × 1.21³ = **Rs 28.83**
- Bull (26% EPS CAGR, grade-C capped): 16.31 × 1.26³ = **Rs 32.63**

### 2D. Sanity checks

| Check | Result | Pass |
|---|---|---|
| Revenue growth within capacity? | 21% base ≤ SOM 21.1% BUT Yr3 Rs 566 Cr > ~Rs 450 Cr near-term ceiling → needs 14-acre expansion on time | FLAG-CAPACITY |
| Margins require the unprecedented? | Base holds FY26 12.2%, no expansion assumed | Yes |
| ROCE stays >15%? | ~25% stagnant | Yes |
| FCF funds growth without excess debt? | NO — OCF negative; falsifier-gated (0.80x) | FLAG-CASH |
| EPS growth operational not engineered? | Volume/order-book driven | Yes |
| Implied share gain realistic? | SOM share 3.7% → modest; consistent | Yes |
| CFO/PAT trajectory vs Pillar 2? | Must turn ≥0 in H1 FY27 or reverts to 0.65x | Falsifier tracked |
| Yr3 ROCE consistent with FTTCP STAGNANT? | Yes, ~25% flat | Yes |

🛑 Section 2 checkpoint complete. Continuing to Section 3.

---

## SECTION 3 — VALUATION METHODS APPLIED

### PRIMARY — P/E (Section 1B destination), both tracks

Applied exit PE = Track 1 13.1x (governing) and Track 2 16.0x. Target price = Yr3 EPS × exit PE.

**3-year target matrix (Rs), CAGR from CMP 315:**

| EPS \ Exit PE | Track 1 mid 13.1x | Track 2 mid 16.0x |
|---|---|---|
| Bear (19.43) | 255 → -6.8% 🔴 | 311 → -0.4% 🔴 |
| Base (28.83) | 378 → +6.3% 🔴 | 461 → +13.5% 🟡 |
| Bull (32.63) | 427 → +10.7% 🔴 | 522 → +18.3% 🟡 |

No cell reaches 25% CAGR (0/6 green), corroborating the Hurdle STOP. The corrected +0x Pillar 3 lowers every cell vs the prior run; the highest path is now Track 2 bull at +18.3%.

### SECONDARY — EV/EBITDA (cross-check)

Destination PE 16x → implied exit EV/EBITDA ≈ 0.55-0.65× ≈ **9-10x** for a capex-heavy manufacturer. Peer TEXRAIL trades ~12x, Airfloa ~12.6x today (B10 Line 147). A de-rate toward 9-10x on Yr3 base EBITDA (~Rs 113 Cr at 20% margin on Rs 566 Cr) gives EV ~Rs 1,020-1,130 Cr, less Yr3 net debt (~Rs 55-100 Cr) / 2.397 Cr shares ≈ Rs 385-448 → consistent with the P/E base-to-bull band. Corroborates, does not lift.

### TERTIARY — P/B (floor)

Book Rs 98.74/sh, growing with retained earnings to ~Rs 175-185/sh by Yr3 (base). Theoretical fair P/B = ROE/CoE = 22.4%/15% ≈ 1.5x → ~Rs 265-280 floor-ish; current P/B 3.19x is already rich. Signals limited downside protection at Rs 315.

### Method-wise fair value (Yr3, Rs) — governing Track 1

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E (Track 1) | 60% | 255 | 378 | 427 |
| EV/EBITDA | 25% | 270 | 410 | 460 |
| P/B | 15% | 270 | 340 | 380 |
| Weighted | 100% | **261** | **380** | **428** |

The P/E and blended values are within ~3% at base/bull; the reported fair values below use the pure P/E-track targets (consistent with the entry-price calc).

🛑 Section 3 checkpoint complete. Continuing to Section 4.

---

## SECTION 4 — TRIANGULATION, ENTRY & VERDICT

### 4A. Triangulated fair value (Yr3), BOTH tracks (P/E-led)

| | Bear | Base | Bull |
|---|---|---|---|
| **Track 1 (RRM, governing)** | Rs 255 | Rs 378 | Rs 427 |
| **Track 2 (Additive)** | Rs 311 | Rs 461 | Rs 522 |

More conservative track (Track 1) sets the entry zone.

### 4B. Methods agreement

All methods point the same direction: modest-to-negative return at Rs 315, no 25% path. Spread base-case P/E vs EV/EBITDA vs P/B ~20%, within tolerance; P/B is the low outlier (asset floor, ignores earnings quality). Most trusted for this company: P/E four-pillar (earnings-quality driven).

### 4C. Return at current price (Track 1 governing)

| Scenario | Yr3 FV | CMP | CAGR | ≥25%? |
|---|---|---|---|---|
| Bear | 255 | 315 | -6.8% | 🔴 |
| Base | 378 | 315 | +6.3% | 🔴 |
| Bull | 427 | 315 | +10.7% | 🔴 |

(Track 2: bear -0.4% / base +13.5% / bull +18.3% — still none ≥25%.)

### 4D. Probability-weighted expected return

Grade C (Mixed) → **Bear 35% / Base 45% / Bull 20%** (sole source: Role 5 credibility grade; B10 Line 77).

| Scenario | Prob | Track 1 CAGR | Weighted |
|---|---|---|---|
| Bear | 35% | -6.8% | -2.38% |
| Base | 45% | +6.3% | +2.84% |
| Bull | 20% | +10.7% | +2.14% |
| **Expected CAGR** | 100% | | **2.6%** |

(Track 2 expected CAGR = 9.6%.) Both far below the 25% Tier A hurdle; the corrected +0x Pillar 3 cuts the Track 1 expected CAGR from 6.8% to 2.6%.

### 4E. Entry price (Tier A, divisor 1.953; conservative Track 1 base FV Rs 378)

| Calculation | Value |
|---|---|
| Base FV (Yr3, Track 1) | Rs 378 |
| 25% CAGR entry = 378 / 1.953 | **Rs 193** |
| 30% CAGR entry = 378 / 2.197 | Rs 172 |
| MoS price (20% below 25% entry) | **Rs 155** |
| Ideal entry range | **Rs 155 - Rs 193** |

(Track 2 base FV Rs 461 → 25% entry Rs 236; conservative Track 1 governs at Rs 193.) CMP Rs 315 is **63-103% above** the entry zone.

### 4F. Risk-reward asymmetry (Track 1)

| | Value |
|---|---|
| Bull Yr3 427 → upside | +35.6% |
| Base Yr3 378 → upside | +20.0% |
| Bear Yr3 255 → downside | -19.0% |
| Upside(base)/Downside(bear) | **1.05x** (< 2x) |

Note: with the corrected +0x Pillar 3, the asymmetry collapses from the prior 4.1x to **~1.05x** — base upside (+20.0%) barely exceeds bear downside (-19.0%). At Rs 315 this is no longer a favourably-skewed setup; it is a fully-to-richly-valued name. Both the Hurdle and now the risk-reward ratio point the same way, hardening AVOID.

### 4G. Four-pillar validation

| Check | Result | Pass |
|---|---|---|
| Yr3 ROCE justifies base (matches FTTCP)? | ~25% stagnant = 24.9% used | Yes |
| Yr3 CFO/PAT justifies 0.80x? | Only if H1 FY27 OCF turns; else 0.65x | Falsifier |
| Growth premium (3a) capacity cross-check? | FAILED (SOM Rs 568 > ~Rs 450 ceiling) → 3a +0x | Corrected |
| Strategic premium justified? | +0x applied (single-credit clean) | Yes |
| UA ordering min(F×1.25, Cap)? | UA withheld; H=min(16,25) | Yes |
| Pay 16x for this quality? | Only below the entry zone, not at 19.3x current | No at CMP |

### 4H. VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP Rs 315 | Market cap Rs 756 Cr | Shares 2.397 Cr | Net debt Rs 55.23 Cr**
- **FOUR-PILLAR EXIT PE:** ROCE base 20.0x (FTTCP STAGNANT, ROCE 24.9%, not credited) × cash 0.80x (growth-induced, no double-credit offset) = quality base 16.0x; + growth **+0.0x** (3a SOM disqualified by FAILED capacity cross-check per Amendment 4.1; order book 1.47x is only one qualifier = +0; 3b EM 14.5 / 3c both 0) + strategic 0 = **Raw 16.0x**; UA withheld; sector cap 25x (Cables/Industrial products) → **Destination PE 14.8-17.2x (mid 16.0x).**
- **RRM TRACK:** r 15%, RRM 0.82 → **Destination PE 12.1-14.1x (mid 13.1x).** Divergence 18.1% (>15%) → RRM governs.
- **HURDLE RATIO:** Base 1.20 / Bull 1.36 (Track 1); Base 1.47 / Bull 1.66 (Track 2) → **STOP** (bull fails both tracks; needs ~33-42% EPS CAGR to clear).
- **METHODS:** P/E 60% / EV/EBITDA 25% / P/B 15%.
- **WEIGHTED FAIR VALUE (Yr3):** Track 1 Bear 255 / Base 378 / Bull 427; Track 2 Bear 311 / Base 461 / Bull 522.
- **EXPECTED CAGR (prob-weighted, grade C 35/45/20):** 2.6% (Track 1) / 9.6% (Track 2).
- **UPSIDE/DOWNSIDE:** 1.05x (below 2x — no favourable skew at CMP).
- **ENTRY RANGE Rs 155 - Rs 193 | MoS Rs 155** (conservative Track 1, Tier A 1.953).
- **DECISION: AVOID (on-valuation), hardened.** Hurdle STOP on both tracks; CMP Rs 315 is 63-103% above the entry zone; risk-reward now ~1.05x. Not a quality-fail — a price-fail, deepened by the corrected +0x growth premium. Re-engage to WATCHLIST if price reaches Rs 155-193 **AND** the H1 FY27 cash falsifier resolves favourably (standalone OCF ≥0, >6m receivables share ≤23.4%, debtor days ~195-200); if the falsifier trips, cash reverts to structural 0.65x, quality base drops to ~13x, and fair value falls further.
- **KEY ASSUMPTIONS THAT MOVE VALUATION:** ▲ cash turns structural-positive → 0.80x holds/rises; ▲ order book re-loads AND capacity expansion lands (both needed to legitimately re-open 3a at +2x); ▲ grade migrates to B → bull uncapped, hurdle could improve. ▼ H1 FY27 OCF negative → 0.65x, base ~13x; ▼ order book shrinks below 1.0x → last 3a qualifier gone; ▼ 14-acre expansion slips → base revenue capacity-constrained toward bear (Rs 566 > Rs 450 ceiling); ▼ BBBS JV second slip → shared-catalyst single-point failure.
- **EXIT FRAMEWORK:** target exit at destination 16x if bought in-zone; thesis-broken if two consecutive negative-OCF halves with rising ageing; time stop 4 quarters on the cash falsifier; PE compression floor ~13x (structural-cash case).
- **ONE-LINE THESIS:** "Avoiding Airfloa at Rs 315 because at a four-pillar destination PE of 16x (ROCE 24.9%, cash 0.80x growth-induced, growth premium +0x after the SOM qualifier fails Amendment 4.1's capacity cross-check, EM 14.5, sector cap 25x) the SOM-capped 21% base EPS CAGR (Rs 16.31 to Rs 28.83) yields only ~6-13% 3-year CAGR and the Hurdle Ratio STOPs on both tracks; entry re-opens at Rs 155-193. Key risk: H1 FY27 OCF stays negative and cash reverts to structural 0.65x."

🛑 Valuation complete. Four-pillar exit PE 14.8-17.2x (RRM 12.1-14.1x). Hurdle Ratio STOP. Entry Rs 155-193. Decision: AVOID (on-valuation), hardened.

---

```yaml
stage: B11-valuation
company: "544516"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
input_gaps:
  - type: rating_wc_quote
    severity: LOW
    note: "Rating-agency structural-WC quote NOT FOUND; Pillar 2 already fixed at 0.80x by operator override with falsifier, so proceed. No 0.65x structural confirmation available."
flags:
  - "PILLAR-3a CORRECTED: SOM-implied CAGR qualifier DISQUALIFIED under Amendment 4.1 (capacity cross-check FAILED: SOM_3yr Rs 568 Cr > ~Rs 450 Cr ceiling, B09 Section 3C). Only order-book qualifier (1.47x) holds = one qualifier = +0x. Pillar 3 total +0x; raw destination PE 16.0x."
  - "FLAG-CASH: negative operating cash flow (-Rs 57.45 Cr FY26); cash multiplier 0.80x GROWTH-INDUCED applied (operator override), NO double-credit growth offset; reverts to 0.65x STRUCTURAL if H1 FY27 falsifier trips (OCF still negative AND >6m receivables >23.4% AND debtor days rise)."
  - "FLAG-CAPACITY: Yr3 base revenue Rs 566 Cr exceeds ~Rs 450 Cr near-term capacity ceiling (B09 Section 3C); base assumes 14-acre expansion lands on time; slip pushes base toward bear (capacity-constrained)."
  - "SHARED CATALYST: 14-acre facility capex + BBBS JV drive near-term growth and future ROCE; working-capital drain competes for same capital; single point of failure. No double-credit exposure this run since growth premium not credited; retained as forward risk."
  - "Hurdle Ratio STOP on BOTH tracks: 25% CAGR infeasible at CMP even on grade-C-capped bull EPS CAGR (26%); requires ~33% (Track 2) / ~42% (Track 1)."
  - "EPS-basis: current PE fixed at 19.3x (current 2.397 Cr shares), NOT the 16.89x weighted-average-share figure; mixing them would fabricate a spurious hurdle pass."
  - "Grade C credibility: bull EPS CAGR capped at Base+5%=26%; order-book miss (Rs469 vs Rs1000 Cr), FY27 guidance walked back, BBBS JV slipped."
  - "Risk-reward asymmetry collapsed to ~1.05x (below 2x) after the +0x Pillar 3 correction."
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 12.1, mid: 13.1, high: 14.1, r_used: 15, rrm: 0.82}
  track2_additive: {low: 14.8, mid: 16.0, high: 17.2}
  divergence_pct: 18.1
  governing_track: "Track 1 RRM (conservative); divergence 18.1% >15% so RRM sets the entry zone"
pillar_detail:
  roce_used: 24.9
  roce_base: 20.0
  roce_recovery_route: "not-credited"
  cash_multiplier: 0.80
  structural_or_growth: "growth-induced"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 1.20, bull_used: false, verdict: "STOP"}
fair_values:
  track1: {bear: 255, base: 378, bull: 427}
  track2: {bear: 311, base: 461, bull: 522}
expected_cagr_prob_weighted: 2.6
entry_range: {low: 155, high: 193}
mos_price: 155
upside_downside_ratio: 1.05
decision: "AVOID (on-valuation)"
unresolved_inputs_used:
  - "rating_wc_quote: NOT FOUND. Conservative assumption: proceed at Pillar 2 0.80x (operator override with falsifier on record); no rating-agency structural-WC confirmation to force 0.65x this run."
som_cagr_crosscheck: "consistent-for-base-EPS (21% at SOM ceiling), BUT capacity cross-check FAILED (SOM 3yr Rs 568 Cr > ~Rs 450 Cr ceiling) — disqualifies Pillar 3a SOM qualifier per Amendment 4.1 and flags base-revenue capacity risk"
one_line_thesis: "Avoiding Airfloa at Rs 315 because at a four-pillar destination PE of 16x (ROCE 24.9%, cash 0.80x growth-induced, growth premium +0x after the SOM qualifier fails Amendment 4.1's capacity cross-check, EM 14.5, sector cap 25x) the SOM-capped 21% base EPS CAGR (Rs 16.31 to Rs 28.83) yields only 6-13% 3-year CAGR and the Hurdle Ratio STOPs on both tracks; entry re-opens at Rs 155-193. Key risk: H1 FY27 OCF stays negative and cash reverts to structural 0.65x."
```
