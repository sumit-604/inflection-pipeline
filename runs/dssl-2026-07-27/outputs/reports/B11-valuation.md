# STAGE 11: ROLE 1 MULTI-METHOD VALUATION — DSSL

**Run:** dssl-2026-07-27 | **Phase:** FTTCP Phase 3 | **Model:** claude-opus-4-8
**Framework:** Master v3.3 (Role 1) / Section 1B v3.5.1 (Pillar 1 normalization authority) / FTTCP v1.2
**Sole input source:** B10-valinputs (all anchors carried from B10; every B10 figure traces to its own upstream anchor)
**Earnings basis (operator-approved at FTTCP gate):** TRAILING (FY26 audited EPS Rs 66.61)

> PIPELINE MODE: all sections executed sequentially, no stops. Interim STOP checkpoints are written as one-line state markers, then the run continues. Where my independent Section 1B derivation touches the operator-approved base, I REPORT and value on the approved base (Master v3.3 wrapper rule): I do not overwrite the operator's 30.0x additive call or the RRM ~24x cross-check.

---

## SECTION 1A: METHOD SELECTION & JUSTIFICATION

DSSL is a hybrid systems-integrator transitioning from hardware resale toward lease-funded DaaS/CBaaS annuity. Earnings are positive and clean (unmodified audit), leverage is moderate, and the four-pillar destination PE is the governing exit authority. Cash flow is structurally WC-intensive (Acuité), so DCF terminal-value sensitivity would dominate and mislead — DCF is deliberately down-weighted.

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E (Four-Pillar destination PE, Section 1B) | 70% | Asset-light-ish services earnings, clean PAT, exit PE is the sole Section 1B authority; trailing basis per operator |
| SECONDARY | EV/EBITDA | 20% | Cross-check for the lease-loaded balance sheet (Ind AS 116); leverage/depreciation differences vs peers |
| TERTIARY | P/B (theoretical = ROE ÷ CoE) | 10% | High ROE 26.9%; sanity cross-check only — book value understates relationship/qualification assets |
| Rejected | DCF | 0% | Structural WC intensity + negative FY26 FCF → terminal value would exceed 70% of value; not reliable here |

**Method-suitability notes:** P/E fits (stable, profitable, clean earnings). EV/EBITDA useful because lease liabilities Rs 155.3cr distort equity-only multiples. P/B retained only as a ceiling-sanity check (ROE-driven). DCF fails the FCF-predictability test (FCF -19.37cr FY26, structural WC per Acuité).

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE WORKSHEET (BOTH TRACKS)

### Pillar 1 — ROCE Base Multiple

- FTTCP ROCE forward verdict: **RECOVERING (+1)** (fttcp-deliberation Override 2, p.34-38; via B10)
- ROCE used for base: **30.17% CURRENT ROCE** (fttcp-deliberation Pillar 1: EBIT 131.39cr / CE 435.47cr; via B10)
- **Pillar 1 normalization route (Section 1B v3.5.1): NONE.**
  - Route A test: (CWIP + idle raised capital + capex advances) vs 20% of capital employed → idle pool ~0.6% of CE (B10 / deliberation Pillar 1 line 76) → **fails 20% gate → Route A not available.**
  - Route B test: FTTCP is RECOVERING with pre-depression history, BUT **no named, dated, 📄 unwind catalyst** (RBI go-live undated; capex payoff milestones NOT FOUND, B10 unresolved) and **ROCE FY[Y+2] = NOT FOUND** → Route B not available.
  - Neither route holds → **statutory (current) 30.17% ROCE feeds Pillar 1 directly.** Worksheet route line: "Pillar 1 normalization route: NONE. Statutory ROCE 30.17% used; Route A fails 20% denominator gate (idle pool ~0.6%); Route B fails 📄-catalyst + FY[Y+2] evidence gate."
  - Note: the RECOVERING blend (60/40 current/FY[Y+2]) is NOT computable — FY[Y+2] is NOT FOUND. Per B10/deliberation and the framework's NOT-FOUND-is-the-only-fill rule, Pillar 1 uses current 30.17% as sole anchor. This is the conservative outcome (no upward normalization credited).
- ROCE Base = 0.5 × 30.17 + 7.5 = 15.085 + 7.5 = **22.6x** (ROCE ≤ 33% branch; floor 9x / cap 24x not binding)
- **ROCE recovery credited via: Pillar 1 only.** Strategic Premium ROCE re-rating route is **BARRED** (single-credit rule, Amendment 4 / v3.5.1). 

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT ~53% (B01) | Latest FY26 CFO/PAT 53.8% | FCF **negative** (-19.37cr, one-time lease-premises capex)
- FTTCP cash verdict: **STAGNANT (0)** (Override 1, p.27-32; via B10)
- "If DSSL stopped growing tomorrow, would WC days still be high?" → **YES → STRUCTURAL.** Acuité verbatim: *"Working capital intensive operations… Working capital operations expected to remain intensive over the medium term."* (rating PR 31-Dec-2025 p.2, via B10). Rating-agency structural assessment takes precedence over the single-year net-WC claim.
- **Cash Multiplier = 1.00x (neutral), NO growth offset.** This is the operator-approved value (fttcp-deliberation Pillar 2 line 79). The Ind AS 116 lease-annuity portion is NOT cash-penalized (SOTP rule); the structural determination bars any growth offset. I apply the multiplier as given; I do not re-litigate the determination.
- **Quality-Adjusted Base = 22.6x × 1.00 = 22.6x**

### Pillar 3 — Growth Visibility Premium (decoupled 3a/3b/3c, +6x cap)

- 3a Growth Visibility: order book Rs 2,964cr = **2.08x** revenue (≥1.0x gate), SOM-implied 3yr CAGR **33.9%** (≥20% gate), delivery grade **B** → **+3x** (three or more qualify AND grade A/B)
- 3b Moat Formation: EM score **22.7/80 (MODEST)**, below 25 → **+0x**
- 3c Duration: visibility 2.08 years, below 2.5yr gate → **+0x**
- **Pillar 3 total = +3x** (via B10; matches deliberation line 80)
- **SHARED CATALYST flag = TRUE:** the order book (RBI Rs 750.82cr, undated go-live) drives both the Pillar 3 growth premium AND the ROCE-recovery logic behind the RECOVERING verdict. Flagged for Role 3 single-point-of-failure stress-test.

### Pillar 4 — Strategic Premium

- No licence/monopoly (B04, B07); pricing power weak; ROCE route BARRED (single-credit) → **+0x**

### Undiscovered Alpha (Amendment 3 ordering)

- Listed ≥12m (inc. 1995) ✓ | Gate 0 core 60 ≥60 ✓ | FII+DII 1.36% <3% ✓ → **all three hold → UA 1.25x applies to RAW PE, before cap.**

### Four-Pillar Summary — TRACK 2 (ADDITIVE)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | 0.5 × 30.17 + 7.5 | 22.6x |
| B. Cash Multiplier (effective) | 1.00 + 0 offset (structural) | 1.00x |
| C. Quality-Adjusted Base | 22.6 × 1.00 | 22.6x |
| D. Growth Visibility Premium | 3a +3 / 3b +0 / 3c +0 | +3.0x |
| E. Strategic Premium | ROCE route barred | +0.0x |
| F. Raw Destination PE | 22.6 + 3.0 + 0 | 25.6x |
| F2. UA-Adjusted Raw PE | 25.6 × 1.25 | 32.0x |
| G. Sector Cap (absolute) | Data centres & cloud infra, capital-heavy | 30.0x |
| **H. Final Destination PE** | **min(32.0, 30.0)** | **30.0x** |

**Reconciliation with B10:** B10 carries raw F2 ≈ 31.6x (using Pillar 1 base 22.3x from the deliberation's exact CE figure); my formula on the anchored 30.17% ROCE gives 22.6x → F2 32.0x. **Both exceed the 30x cap, so the cap binds identically at 30.0x.** No quality uplift on the cap is applied (Master: uplift needs durability ≥ Moderate-Strong; DSSL durability is Medium and EM MODEST). Operator-approved base 30.0x confirmed.

**Additive Destination PE Range (±7.5%, Amendment 6):** 30.0 ×0.925 = 27.75 → 28.0x; upper 30.0 ×1.075 = 32.25 capped at cap → **28.0x to 30.0x** (mid 30.0x, cap-bound).

### Four-Pillar Summary — TRACK 1 (RRM)

- Base r: small/micro 14%; +1.5% durability/governance load (promoter CAUTION, Cybercons classification unresolved, accounting quality 5/10) → **r = 15.5%**, bounded [9%,18%] ✓
- **RRM = 1 + (13.5 − 15.5) × 0.12 = 1 − 0.24 = 0.76** (percentage-point reading, Amendment 4.4)
- Fundamental base (pre-UA, pre-RRM) = C + D + E = 25.6x
- RRM-track destination = 25.6 × 0.76 × 1.25 UA = **24.3x**, under the 30x cap → carried at **~24.0x** (B10-authoritative)
- **RRM Destination PE Range (±7.5%):** 24.0 → **22.5x to 26.0x** (mid 24.0x)

### Track Divergence & Governing Track

- Additive 30.0x vs RRM 24.0x → divergence (6.0 / 26.0 midpoint) = **~23%**, above the 15% line.
- **The more conservative track (RRM ~24x) GOVERNS the entry zone** (Master v3.3 Role 1 dual-track rule). Reasoning: the >15% divergence is driven by the sector-cap truncation of a UA-inflated additive raw, plus genuine quality load (RECOVERING not FIRING, MODEST EM, structural cash, governance CAUTION). The RRM prices that durability/governance risk into the discount rate rather than the premium stack, which is the correct conservative treatment for an unconfirmed transition. The operator approved 30.0x as the additive base; both tracks are carried through every fair value and the verdict card. Entry zone is set off the RRM base fair value.

**Interim checkpoint (Section 1 complete):** Four-pillar destination PE 28.0x–30.0x additive (RRM 22.5x–26.0x). Current PE 18.5x. This is a **RE-RATING setup** (destination > current), unusual for this pipeline. Hurdle Ratio computed in Section 4 → PASS on both tracks. Continuing.

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS

Management gives **NO guidance** (explicit no-guidance policy, both concalls; B10). Credibility grade **B** → Bull is permitted (grade A/B), but built off documented order-book conversion, not face-value promises.

### 2A. Revenue Projection (base year FY26 = Rs 1,424.28cr; 3yr history CAGR 21.0%)

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| Revenue growth logic | Share-gain momentum fades to near-market; RBI go-live slips; FY26 already decelerated to +12.4% YoY | Discounted order-book conversion (2.08x book, ~18-24mo cycle), below historical 21% for execution/receivables risk | Order-book + pipeline convert strongly; DC/annuity mix scales |
| Revenue CAGR | **12%** | **18%** | **25%** |
| Revenue Yr0 (FY26) | 1,424.3 | 1,424.3 | 1,424.3 |
| Revenue Yr3 (FY29) | 2,001.1 | 2,340.2 | 2,782.6 |

**SOM cross-check (Master):** base 18% is **well below** the B09 SOM-implied 3yr CAGR of 33.9% and below the 5yr 30.6% → **consistent, no cut required.** Even Bull 25% sits below SOM 33.9% (SOM lacks order-to-cash verification beyond yr2-3, so I hold Bull under it).

### 2B. Profitability Projection

FY26: EBITDA margin 10.25%, PAT margin 5.95%. History: EBITDA 7.63% (FY24) → 8.31% (FY25) → 10.25% (FY26); Q4 FY26 dipped to 9.02% (AI-hardware supply chain).

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| EBITDA margin | 8.5% (Q4 run-rate persists, current −175bps) | ~10.0% (near FY26, above 3yr avg 8.7%) | ~11.5% (normalization + DC mix, still ≤ any prior print) |
| PAT margin | **4.8%** (margin + higher lease-interest + possible ECL charge) | **5.8%** (roughly holds FY26, slight haircut) | **6.8%** (operating leverage + margin normalization) |
| Share dilution | 0% (promoter 60.89%, minimal ESOP) | 0% | 0% |

### 2C. Complete Projection Table (shares constant 1.2737cr)

| Line Item | Yr0 (FY26) | Bear Yr3 | Base Yr3 | Bull Yr3 |
|---|---|---|---|---|
| Revenue (Rs cr) | 1,424.3 | 2,001.1 | 2,340.2 | 2,782.6 |
| PAT margin | 5.95% | 4.8% | 5.8% | 6.8% |
| PAT (Rs cr) | 84.78 | 96.05 | 135.73 | 189.22 |
| **EPS (Rs, diluted)** | **66.61** | **75.41** | **106.57** | **148.56** |
| Implied EPS CAGR (3yr) | — | 4.2% | 17.0% | 30.7% |
| Est. ROCE (Yr3) | 30.2% | ~22% | ~28% | ~33% |

### 2D. Projection Sanity Checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than order book/capacity allows? | Base 18% << SOM 33.9%; order book 2.08x supports | ✓ |
| Margins require something unprecedented? | Base 10% EBITDA = FY26 actual; Bull 11.5% ≤ prior peak quarters | ✓ |
| ROCE stays above 15%? | Bear ~22%, all cases >15% | ✓ |
| FCF funds growth without excess new debt? | Structural WC intensity persists; capex normalizes post one-time lease build; watch | ⚠ (structural, priced in Pillar 2 at 1.00x) |
| EPS growth operational, not financial engineering? | Driven by revenue + margin, no buyback/dilution games | ✓ |
| Implied market share gain realistic? | FY29 base rev 2,340cr = 3.3% of SAM 70,548cr (from 2.02%) | ✓ |
| CFO/PAT trajectory consistent with Pillar 2 (1.00x neutral)? | Held flat/structural, no improvement assumed | ✓ |
| Yr3 ROCE consistent with FTTCP RECOVERING used in Pillar 1? | Base Yr3 ~28% vs current 30.17%; RECOVERING not FIRING → consistent | ✓ |

**Interim checkpoint (Section 2 complete):** Projections built; base EPS Rs 66.61 → Rs 106.57 (17.0% CAGR). Continuing.

---

## SECTION 3: APPLY EACH VALUATION METHOD

### PRIMARY — P/E (trailing-basis destination PE × Year-3 EPS)

Exit PE applied on the **operator-approved TRAILING basis**: destination multiple × Year-3 trailing (FY29) EPS. Hurdle denominator uses current trailing PE (CMP ÷ trailing FY26 EPS) — numerator and denominator EPS basis MATCH (trailing), per the SFL lesson.

**3-Year Target Price Matrix**

| EPS scenario | RRM 24.0x (governing) | Additive 30.0x (operator base) |
|---|---|---|
| Bear EPS 75.41 | Rs 1,810 → 13.7% CAGR 🟡 | Rs 2,262 → 22.5% CAGR 🟡 |
| Base EPS 106.57 | Rs 2,558 → 27.6% CAGR 🟢 | Rs 3,197 → 37.4% CAGR 🟢 |
| Bull EPS 148.56 | Rs 3,565 → 42.5% CAGR 🟢 | Rs 4,457 → 53.5% CAGR 🟢 |

(CAGR from CMP Rs 1,232; 🟢 ≥25% / 🟡 15-25% / 🔴 <15%)

**P/E Method Fair Value (Year 3), Base:** RRM Rs 2,558 | Additive Rs 3,197.

### SECONDARY — EV/EBITDA (cross-check)

Rule of thumb: exit EV/EBITDA ≈ 0.6-0.65x of destination PE, adjusted down for capex/lease intensity. Using RRM destination 24x → ~13x EV/EBITDA; additive 30x → ~16x. DSSL trades ~10.1x now (B10); peers ADSL 8.9x, AURIONPRO 14.9x. A justified exit EV/EBITDA of **11-13x** (mid-peer, growth premium to ADSL) is conservative.

Base Yr3: EBITDA = 2,340.2 × 10.0% = 234.0cr. At 12x EV/EBITDA → EV 2,808cr; less Yr3 net debt (assume ~150cr, lease-loaded, roughly flat) → equity 2,658cr ÷ 1.2737 = **Rs 2,087/share**. This sits between RRM and additive P/E base values, closer to RRM — confirms the conservative track is the right anchor.

### TERTIARY — P/B (sanity ceiling)

Theoretical P/B = ROE ÷ CoE = 26.9% ÷ 15.5% = 1.74x. On BVPS 247.3 → Rs 430 (far below CMP). This confirms book value materially understates the qualification/relationship assets (asset-light services); P/B is not a fair anchor here, used only to confirm the P/E premium is expected, not aberrant. **Weight 10%, floor only.**

### Method-wise Fair Value Summary (Base, Year 3)

| Method | Weight | RRM base | Additive base |
|---|---|---|---|
| P/E (four-pillar) | 70% | 2,558 | 3,197 |
| EV/EBITDA | 20% | 2,087 | 2,087 |
| P/B (floor) | 10% | 430 | 430 |
| **Weighted** | 100% | **2,265** | **2,713** |

**Interim checkpoint (Section 3 complete):** All methods applied; P/E governs at 70%. Continuing.

---

## SECTION 4: TRIANGULATION, ENTRY PRICE & FINAL VERDICT

### 4A. Triangulated Fair Value (Year 3, both tracks)

| | Bear | Base | Bull |
|---|---|---|---|
| **RRM track (governing)** | ~1,700 | **2,265** | ~3,100 |
| **Additive track (operator base)** | ~2,050 | **2,713** | ~3,850 |

(Blend weights P/E 70 / EV-EBITDA 20 / P/B 10; bear and bull scale the P/E and EV/EBITDA legs by scenario EPS/EBITDA.) For the decision anchors below I use the pure P/E four-pillar base values (RRM 2,558 / additive 3,197), the framework's primary method, with the triangulated blend as the conservative floor.

### 4B. Methods Agreement

Methods point the same direction (all above CMP on base). Spread P/E vs EV/EBITDA ~22% (within tolerance); P/B is a deliberate floor outlier (book understates intangibles). **Most-trusted method: P/E four-pillar** (Section 1B is the sole exit authority).

### 4C / 4D. Return & Probability-Weighted Expected Return

Credibility grade **B → weights Bear 25% / Base 50% / Bull 25%** (sole source: Role 5 grade). No 2-quarter-below-bear re-weighting trigger evidenced.

| Scenario | Prob | RRM CAGR @CMP | Additive CAGR @CMP |
|---|---|---|---|
| Bear | 25% | 13.7% | 22.5% |
| Base | 50% | 27.6% | 37.4% |
| Bull | 25% | 42.5% | 53.5% |
| **Expected CAGR** | 100% | **27.8%** | **37.7%** |

**Governing (conservative RRM) probability-weighted expected CAGR at CMP = 27.8%** — above the 25% Tier A hurdle even on the conservative track. Additive 37.7%.

### Hurdle Ratio (Amendment 2, Tier A threshold 1.953)

HR = (1 + Base EPS CAGR)³ × (Destination PE mid ÷ Current PE). Base EPS CAGR 16.96% → (1.1696)³ = 1.600. Current PE 18.5x (trailing, matched basis).

| Track | HR | Verdict |
|---|---|---|
| RRM 24.0x | 1.600 × (24.0/18.5) = **2.08** | **PASS** |
| Additive 30.0x | 1.600 × (30.0/18.5) = **2.60** | **PASS** |

Bull row (grade B permits Bull EPS CAGR 30.7%): RRM 2.89, additive 3.62 — both PASS. **Hurdle Ratio = PASS on the base case, both tracks.** This is the expected re-rating outcome (destination 24-30x >> current 18.5x); the 25% hurdle is met at CMP. Final validation — *would I pay 24-30x for this quality?* On the RRM 24x, yes, conditional on the transition confirming (margin normalization + RBI go-live); the additive 30x is cap-bound and requires the same confirmation.

### 4E. Entry Price (RRM governs — conservative track sets the zone)

| Calculation | RRM (governing) | Additive (reference) |
|---|---|---|
| Base Fair Value (Yr3) | Rs 2,558 | Rs 3,197 |
| Entry = FV ÷ 1.953 (Tier A, 25% CAGR) | **Rs 1,310** | Rs 1,637 |
| MoS price (20% below entry) | **Rs 1,048** | Rs 1,310 |
| Ideal entry range (MoS → entry) | **Rs 1,048 to Rs 1,310** | Rs 1,310 to Rs 1,637 |

**CMP Rs 1,232 sits INSIDE the RRM entry band** (between MoS 1,048 and entry 1,310), i.e. mechanically a BUY-ON-DIPS zone, and comfortably inside the additive band. Buy at the bottom of the band (near MoS Rs 1,048), never the top.

### 4F. Risk-Reward Asymmetry

| | Value |
|---|---|
| Bull target (Yr3, RRM) | Rs 3,565 → +189% |
| Base target (Yr3, RRM) | Rs 2,558 → +108% |
| Bear target (Yr3, RRM) | Rs 1,810 → +47% (still upside — re-rating setup) |
| De-rating downside floor (thesis-break: EPS ~66 flat, PE de-rates to ~15x) | ~Rs 1,000 → −19% |
| **Upside (base) / Downside (de-rating floor)** | **~5.7x** (≥2x hurdle cleared) |

Note: the modeled 3-year BEAR target sits ABOVE CMP; genuine downside requires a de-rating/thesis-break, floored near Rs 1,000-1,050. Highly asymmetric, favorable.

### 4G. Four-Pillar Exit Multiple Validation

| Check | Result | Pass? |
|---|---|---|
| Yr3 ROCE justifies base (matches FTTCP RECOVERING)? | Base ~28% vs 30.17%, RECOVERING not FIRING | ✓ |
| Yr3 CFO/PAT justifies 1.00x cash multiplier? | Held structural/flat, no improvement credited | ✓ |
| Primary catalyst fired by Yr3 (base)? | Order-book conversion assumed; RBI go-live undated (flag) | ⚠ SHARED CATALYST |
| Strategic premium justified (single-credit)? | +0x; ROCE route barred | ✓ |
| UA ordering correct — min(F×1.25, Cap)? | 32.0 capped to 30.0 | ✓ |
| Would I buy another stock at this exit PE with these Yr3 metrics? | RRM 24x yes; additive 30x cap-bound, needs confirmation | ✓ (RRM) |

### 4H. FINAL VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP Rs 1,232 | Market cap Rs 1,567.9cr | Shares 1.2737cr | Trailing FY26 EPS Rs 66.61 | Current PE 18.5x**
- **FOUR-PILLAR EXIT PE:** ROCE Base 22.6x (FTTCP RECOVERING; current ROCE 30.17% used; normalization route NONE) × Cash 1.00x (STRUCTURAL, Acuité; no growth offset) = Quality Base 22.6x; + Growth +3.0x (3a order book 2.08x, grade B, SOM 33.9%; 3b/3c +0); + Strategic +0x (ROCE route barred); Raw 25.6x; **UA applied YES** ×1.25 → 32.0x; **Sector cap 30.0x** (Data centres & cloud infra, capital-heavy; no quality uplift). **DESTINATION PE (additive) = 30.0x (range 28.0x-30.0x, cap-bound).**
- **RRM TRACK:** r = 15.5%, RRM 0.76 → **Destination PE 24.0x (range 22.5x-26.0x).** Divergence vs additive ~23% (>15%) → **RRM GOVERNS the entry zone.**
- **HURDLE RATIO: PASS** (RRM 2.08, additive 2.60 on base EPS CAGR 17.0%; bull also passes).
- **METHODS:** P/E 70% (primary) / EV/EBITDA 20% / P/B 10% (floor).
- **WEIGHTED FAIR VALUE (Yr3):** RRM Bear ~1,700 / Base ~2,265 / Bull ~3,100 · Additive Bear ~2,050 / Base ~2,713 / Bull ~3,850. **Pure P/E base:** RRM 2,558 / Additive 3,197.
- **EXPECTED CAGR (prob-weighted, grade B 25/50/25):** RRM 27.8% (governing) · Additive 37.7%.
- **UPSIDE/DOWNSIDE:** ~5.7x.
- **ENTRY (RRM-governed):** Rs 1,048 (MoS) to Rs 1,310 (25% entry). **MoS Rs 1,048.**
- **DECISION: WATCHLIST → BUY-ON-DIPS on Q1 FY27 confirmation.** Hurdle PASSES and CMP Rs 1,232 sits inside the RRM entry band, so this is mechanically a dip-buy, NOT AVOID-on-valuation. It is held at WATCHLIST (not BUY NOW) by: (1) promoter verdict CAUTION (not TRUSTWORTHY) — BUY NOW gate fails; (2) CMP Rs 1,232 > MoS Rs 1,048; (3) the ENTRY CONJUNCTION rule — RBI Rs 750.82cr go-live is undated and Q4 FY26 margin recovery is unproven, so a thesis-broken trigger is still open. Accumulate toward MoS Rs 1,048 once Q1 FY27 margin normalizes (≥11%) and RBI go-live is confirmed.
- **KEY ASSUMPTIONS THAT MOVE THE VALUATION:** ▲ Margin normalization to 11-12% (Bull PAT margin 6.8%) lifts EPS ~30%; ▲ RBI + pipeline conversion at SOM pace pushes toward additive 30x. ▼ ECL bad-debt charge on the +238% 1-2yr ageing bucket cuts PAT margin (Bear 4.8%); ▼ RBI go-live slip drops revenue CAGR toward 12% and de-rates the growth premium; ▼ Cybercons reclassification restates consolidated earnings.
- **EXIT FRAMEWORK:** target exit at destination PE (RRM 24x / additive 30x) on Yr3 EPS; thesis-broken if margin stays <9% two quarters OR RBI order cancelled OR ECL provision spikes; time stop 3-5 years; PE-compression floor ~15x (de-rating floor ~Rs 1,000).
- **ONE-LINE THESIS:** Buying DSSL at Rs 1,232 because trailing EPS grows from Rs 66.61 to ~Rs 106.6 over 3 years driven by order-book conversion (2.08x book, RBI Rs 750.82cr), at a governing RRM destination PE of 24x (ROCE 30.17%, cash 1.00x structural, EM 22.7 MODEST, sector cap 30x) = Rs 2,558 target = ~27.6% CAGR; hurdle PASSES. Key risk: undated RBI go-live is a shared catalyst single-point-of-failure. Cash quality: structural.

**FLAGS CARRIED FORWARD:** FLAG-CASH (structural WC, cash multiplier applied = 1.00x neutral); SHARED CATALYST (order book drives Pillar 3 AND RECOVERING ROCE); RBI Rs 750.82cr undated go-live = single point of failure; receivables 1-2yr ageing +238% vs frozen ECL Rs 0.14cr; Q4 FY26 margin recovery unproven; Cybercons classification unresolved.

**Valuation complete.** Four-pillar exit PE 24x (RRM, governing) to 30x (additive, operator base). Hurdle Ratio PASS. Entry price Rs 1,048 to Rs 1,310. Decision: WATCHLIST (BUY-ON-DIPS on Q1 FY27 confirmation).

---

```yaml
stage: B11-valuation
company: "DSSL"
run_date: "2026-07-27"
model: claude-opus-4-8
status: complete
input_gaps:
  - "ROCE FY[Y+2] expected: NOT FOUND — RECOVERING blend not computable; Pillar 1 uses current 30.17% as sole anchor (conservative, no upward normalization)"
  - "Forward EBITDA/revenue guidance FY27+: NOT FOUND (management no-guidance policy); projections built from history + discounted order-book conversion"
  - "Capex/CWIP go-live timeline (RBI/DaaS): NOT FOUND — blocks Route B named-catalyst gate; normalization route NONE"
  - "Cybercons final classification: NOT FOUND (FY26 AR unpublished) — consolidated-earnings restatement risk flagged"
flags:
  - "FLAG-CASH: structural WC intensity (Acuité); cash multiplier applied = 1.00x neutral, NO growth offset; Ind AS 116 lease-annuity not cash-penalized (SOTP)"
  - "SHARED CATALYST: order book (RBI Rs750.82cr, undated go-live) drives Pillar 3 growth premium AND the RECOVERING ROCE logic — single point of failure for Role 3"
  - "RBI Rs750.82cr order go-live undated = single point of failure"
  - "Receivables 1-2yr ageing +238% YoY vs ECL frozen Rs0.14cr — falsifier if bad-debt charge materializes"
  - "Q4 FY26 EBITDA margin 9.02% (from 11.92% Q3) — margin recovery unproven, Q1 FY27 confirmation required"
framework_versions: "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2"
pe_basis: "trailing"
exit_pe_base_approved: "30.0x additive (trailing EPS), sector-capped; RRM ~24x cross-check governs entry zone"
destination_pe:
  track1_rrm: {low: 22.5, mid: 24.0, high: 26.0, r_used: 15.5, rrm: 0.76}
  track2_additive: {low: 28.0, mid: 30.0, high: 30.0}
  divergence_pct: 23
  governing_track: "RRM (24x) — conservative track sets entry zone; divergence >15%; prices durability/governance risk in discount rate"
pillar_detail:
  roce_used: 30.17
  roce_base: 30.17
  roce_recovery_route: "pillar1-midpoint"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.00
  structural_or_growth: "structural"
  growth_offset: 0
  growth_premium: 3.0
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: true
  sector_cap_used: 30.0
hurdle_ratio: {base: 2.08, bull_used: false, verdict: "PASS"}
fair_values:
  track1: {bear: 1810, base: 2558, bull: 3565}
  track2: {bear: 2262, base: 3197, bull: 4457}
expected_cagr_prob_weighted: 27.8
entry_range: {low: 1048, high: 1310}
mos_price: 1048
upside_downside_ratio: 5.7
decision: "WATCHLIST (BUY-ON-DIPS on Q1 FY27 confirmation; hurdle PASSES, not AVOID-on-valuation)"
unresolved_inputs_used:
  - "ROCE FY[Y+2] NOT FOUND — RECOVERING blend skipped; current 30.17% used as sole Pillar 1 anchor (conservative, per B10/deliberation)"
  - "Forward guidance NOT FOUND — base revenue CAGR 18% from discounted order-book conversion (< SOM 33.9%); bear 12%, bull 25%"
  - "Yr3 net debt not separately projected — assumed ~Rs150cr (roughly flat, lease-loaded) for EV/EBITDA cross-check only"
som_cagr_crosscheck: "consistent"
one_line_thesis: "DSSL at Rs1,232: trailing EPS Rs66.61 to ~Rs106.6 over 3yr on order-book conversion, governing RRM destination 24x (ROCE 30.17%, cash 1.00x structural, EM MODEST, cap 30x) = Rs2,558 = ~27.6% CAGR, hurdle PASSES; key risk undated RBI go-live shared catalyst; cash quality structural."
```
