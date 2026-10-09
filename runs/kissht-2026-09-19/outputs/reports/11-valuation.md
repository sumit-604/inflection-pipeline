# STAGE 11: ROLE 1 VALUATION, OnEMI Technology Solutions Ltd (Kissht)

Ticker KISSHT (NSE) / 544754 (BSE). Run folder runs/kissht-2026-09-19. Phase 3 (finalize).
Valued 04-Oct-2026. Model claude-opus-5-5.

**Priced under Section 1B v3.11 unmerged draft (open item I5).**

Framework: Master v3.7 Role 1 (file Master_Project_Prompt_v3_6.md); Section 1B v3.3 + v3.5.1 +
v3.6 + v3.7 + v3.8 + v3.9 + v3.10 + v3.11 (v3.11 unmerged) through the preloaded section-1b
skill; FTTCP v2.3. Sole input table: outputs/blocks/B10-assembly.yaml (B10). The operator-approved
pillars (fttcp-deliberation section 5, signed 04-Oct-2026, carried on B10.operator_signed_fttcp_pillars)
are BINDING. This report derives no different exit PE and no different P/B band. Where an
independent Section 1B reading differs, the divergence is reported and the value stays on the
approved base (section-1b chunk 15, 20.9; wrapper "OPERATOR-APPROVED BASE").

Units: Rs Cr unless stated. Per-share figures use 20.8416 Cr fully diluted post-raise shares
(B10.shares_diluted_post_raise_cr; deliberation override 6). [INFERENCE] marks Stage 11 arithmetic
on anchored inputs.

Chunk files read for this run: section-1b chunks 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12,
15, 17 (skill base directory). No chunk disagreed with a source file on a point this run needed.
No frameworks/ Section 1B source file was opened. The worktree frameworks/ folder holds no v3.11
text (unmerged, I5); A27 rules come from the skill only.

---

## 0. PRE-CHECKS, CONSUMED BLOCKS, GATES

| Check | Result | Anchor |
|---|---|---|
| Entity-count gate (wrapper override 12) | entity_count 1. One valuation. The two SOTP slices (own book, partner half) are method outputs of one entity, not entities | B10.operator_signed_fttcp_pillars.entity_count; deliberation ruling 5 |
| FTTCP ran | YES. Composite +2 of 8, DEEP WATCH leaning AVOID, posture VALUE-TRAP RISK, signed 04-Oct-2026 | B10.verdict_composite_final; deliberation section 1 |
| Halt 1 / Mental Model | Signed; pillar gate approved FORWARD basis and SOTP base | deliberation section 5 |
| FTTCP RoA/RoE forward verdict (sole Pillar 1 authority) | STAGNANT | B10.roa_roe_forward_verdict; deliberation ruling 12 |
| Debt Capacity block (consumed) | NOT FOUND in B10. Not recomputed (Consumption Clause) | input gap |
| FTTCP Part B Output Sheet B1-B8 (consumed) | NOT FOUND in B10. B2 growth-premium flag, B4 operating EPS, B7 net debt and B8 re-rating rating are all NOT FOUND. Not rebuilt | input gap |
| Market-Implied block (consumed) | NOT FOUND in B10. Flag OPPORTUNITY / FAIRLY PRICED / PRICED-WE-ARE-LATE is PENDING (claude.ai). Section 4 prints Stage 11's own market-implied slice arithmetic as a labelled cross-check only | input gap |
| C.2 catalyst table with operator probabilities | NOT FOUND in B10. B10 carries catalyst names and windows only. Stage 11 builds the ledger from them with PROVISIONAL probabilities (override 3) | B10.primary_catalyst_12m, catalyst_windows |
| Live peer table (Step 1C) | NOT INJECTED. PENDING LIVE PEER TABLE | B10.peer_medians.status NOT FOUND |
| Macro sheet | macro-sheet.md, month stamp August 2026, next refresh 1-Sep-2026: **STALE** at the 04-Oct-2026 run date (FLAG-MACRO-STALE). Market CoE 6.76% + 7.31% = 14.07%, 57 bps from the RRM neutral 13.5%: below the 100 bps recalibration trigger | macro-sheet.md lines 3, 10, 15 |
| Credibility grade (Rule E) | C (Mixed), over the trailing 2 quarters of calls (Q4 FY26 Jun-2026, Q1 FY27 Aug-2026), delivery scored over one quarter | B10.credibility_grade, credibility_delivery_rating |
| Listing date (A27.1 test) | 08-May-2026. About 5 months at the run date, inside 24 months. A27.1 binds | B10 report analyst note 11 |

Single-credit map verified before valuing (section-1b chunk 04):
- ROCE (RoE) recovery: not credited (STAGNANT). Not in Pillar 1, not in Strategic Premium, not in r.
- Capital-cycle normalisation: none (no route; STAGNANT bars both routes).
- Cash quality: Pillar 2L only (lender); never in r (A12A).
- Complexity: r +0.5 only (A13).
- Post-IPO surplus cash Rs 208.05 Cr: fair value at face only; not in EPS as treasury income (amount NOT FOUND, see below); not in slice capital.
- SOTP slice quality: each slice's own rows only (A27.2).
- Catalysts: earnings path 100%, exit multiple 0% (Pillar 3 +0x, Strategic +0x).

Interim: "Section 0 complete. Gates clear for pipeline mode; four consumed blocks NOT FOUND and named."

---

## SECTION 1A: METHOD SELECTION

### Method Suitability Matrix

| Method | Fit for Kissht | Suitable here? | Weight |
|---|---|---|---|
| P/E (whole company) | Lender with two economic engines: on-book lending (capital-heavy) and an off-book partner fee half (asset-light, 5% DLG). One P/E blends a book-bound and a fee-bound earner | Cross-check only (operator ruling, deliberation section 5) | 0% |
| PEG | Growth 41% FY28 fading to 20%; too steep a fade for a stable PEG read | No | 0% |
| EV/EBITDA, EV/Sales, EV/GP, EV/Capacity | Financial firm. EBITDA undefined (B10.ebitda_note); EV n.m. for a lender (B10.enterprise_value_note) | No | 0% |
| P/B (whole company) | PRIMARY method for lenders (Pillar 2L, chunk 02). Fails for the partner half: its earnings sit on off-book AUM that consolidated book does not capture | Cross-check only (operator ruling) | 0% |
| NAV | Not a holding or real-estate company | No | 0% |
| DCF | Negative consolidated CFO by Ind AS 7 loan disbursal (B10 FLAG-CASH); FCF undefined for a lender | No | 0% |
| DDM | No dividend history (B10 report) | No | 0% |
| P/AUM, P/EV, EV/ARR | Not an AMC, insurer or platform | No | 0% |
| **SOTP (Amendment 27.2)** | Fits the two engines exactly: own book (Si Creva) on P/B, the lender's primary method; partner half on P/E, the fee engine's natural method | **PRIMARY** | **100%** |

### Final Method Selection

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | SOTP: own book P/B + partner half P/E + A27.1 cash line | 100% | Operator ruling (deliberation section 5, override 2). The SOTP is itself two methods: P/B on the capital-heavy slice, P/E on the asset-light slice |
| CROSS-CHECK | Whole-company P/E (Pillar 1 RoE ~17%) | 0% | Shown with divergence (Section 3) |
| CROSS-CHECK | Whole-company P/B (theoretical ROE / CoE) on Mar-27 BVPS | 0% | Shown with divergence (Section 3) |

**Single-method justification (wrapper override 6).** The fair value rests on the SOTP alone. A
whole-company P/B cannot see the partner half's fee earnings, because the partner AUM sits off
the consolidated book; weighting it would value the fee engine at book. A whole-company P/E prices
the own book's sub-cost-of-capital RoE (~10%) at the same multiple as the fee half's ~34% RoE; weighting
it would break the A27.2 rule that each slice earns its own multiple. The operator ruled both
cross-check only. The SOTP still carries method plurality inside it (P/B and P/E), and both
whole-company methods are printed with their divergence.

Interim: "Section 1A complete. SOTP primary 100%; P/E and P/B cross-checks at 0% weight, printed."

---

## SECTION 1B: FOUR-PILLAR WORKSHEET (operator-approved base)

### 1B.0 Opening gates

- **Classification: NON-CONVERTER** (section-1b chunk 11). Test (a) fails: the input is borrowed
  money and equity, not a traded commodity of the resin / crude / steel / agri kind. Tests (b) and
  (c) are partial (lending is spread-based; yield moves with funding cost). CONVERTER needs all three,
  so the case is not ambiguous and OR-6 does not engage. Lender carve-out applies (Pillar 2L,
  RoE-based Pillar 1, P/B primary, 18x cap; chunk 02, chunk 05).
- **Post-IPO operating basis (A27.1, section-1b chunk 01):** "Listed 08-May-2026 (about 5 months at
  run date) | cash and liquid investments: NOT FOUND in B10 | less FLDG deposits (encumbered, locked
  collateral) | surplus cash Rs 208.05 Cr (Rs 9.98/share) = the general-purpose 25% slice of the
  Rs 832.20 Cr raise | treasury income excluded: NOT FOUND (no treasury line in B10; the operator PAT
  path is built on return on AUM and states no treasury component) | Route A test on residual capital:
  not run (STAGNANT bars routes)." Anchor: B10.net_cash_surplus_cr, cash_treatment.
- **Pillar 1 normalisation route: NONE** (section-1b chunk 01). STAGNANT bars Route A and Route B.
- **Earnings basis (entry and exit): FORWARD (operator-approved: Y).** Valuation date 31-Mar-2027.
  Own book on Mar-27 book; partner half on FY28 PAT. Exit at end-Year-3 (31-Mar-2030) on Mar-30
  book and FY31 PAT (section-1b chunk 10, 18.1; A27.3).

### 1B.1 Slice 2: partner half (parent fee business), P/E on FY28 PAT

| Row | Calculation | Value | Citation |
|---|---|---|---|
| A. RoE base | RoE ex investment in Si Creva: 84.4% FY26 actual, ~34% FY27 projected; operator figure → 24.5x (elite band 24 + 0.3 x (RoE - 33)) | **24.5x** | section-1b chunk 01; B10.partner_slice_pillar1_pe |
| B. Pillar 2L asset-quality multiplier | Sound band | **1.00x** | section-1b chunk 02; B10.partner_slice_pillar2l |
| C. Quality-adjusted base | 24.5 x 1.00 | 24.5x | chunk 06 |
| D. Pillar 3 | A16 gate: B2 flag NOT FOUND. 3a: one qualifier (SOM-implied CAGR 61.4% >= 20%), grade C, no order book or capex test → +0x. 3b: EM 18.5 < 25 → +0x. 3c: no contracted revenue → +0x | **+0x** | section-1b chunks 03, 12; B10.em_score |
| E. Strategic premium | No scarce asset | **+0x** | section-1b chunk 04 |
| F. Raw PE | 24.5 + 0 + 0 | 24.5x | chunk 06 |
| F2. UA | Listed < 12 months; EM 18.5 < 25; FII/DII NOT FOUND → not qualified | 24.5x | section-1b chunk 05; B10.ua_classification |
| G. Cap | Operator-set slice cap 1/3 x 18x + 2/3 x 25x = 22.67x (override 3). Section 1B has no blended-row mechanism; this is an operator ruling, not a framework output | 22.67x | section-1b chunk 05 (no matching row); deliberation override 3 |
| G2. Category-Break Override | N | N | section-1b chunk 05 |
| G3. Override-adjusted cap | = G | 22.67x | chunk 05 |
| **H. Track 2 destination** | min(24.5, 22.67) | **22.67x (cap binds)** | chunk 06 |
| Track 1 (RRM) | 24.5 x 0.76 = 18.62x, below cap | **18.62x** | section-1b chunk 15 |

RRM line (section-1b chunk 15): "r base 14%; durability adj +0.5 (band Unproven: listed about 5
months; the band owns short-record risk, no separate surcharge per 12C); governance adj +0.5
(operator override 4); cyclical surcharge none; complexity adj +0.5 (A13: Si Creva subsidiary
structure, dense related-party flows incl. the parent guarantee and fee transfer pricing);
cash-conversion r-UP: none per 12A; short-record r-UP: none per 12C; final r 15.5% (bounded
[9%, 18%])." RRM = 1 + (13.5 - 15.5) x 0.12 = **0.76**. Anchor: B10.cost_of_equity_components,
risk_return_multiplier.

Track divergence: (22.67 - 18.62) / 22.67 = **17.9% > 15%**. Track 1 sets the entry zone
(section-1b chunk 06, open ruling OR-1 carried as written). Which track fits: Track 1. The slice
sits on two partners with a 5% DLG first-loss charge (23.4% of outside revenue, FY26), a short
listed record and a parent guarantee at 228% of net worth; a required return above the 13.5%
neutral is the evidenced reading.

Destination range (H ± 7.5%, rounded to 0.5x; chunk 06): Track 2 21.0x to 22.67x (upper capped);
Track 1 17.0x to 20.0x. The operator-approved SOTP range governs: **low 18.62x / base 20.64x
(midpoint, exact 20.6433x) / high 22.67x (exact 22.6667x)**. The deliberation's printed totals
reproduce only at the exact values; this report uses them.

**Divergences reported (value stays on the approved base):**
1. *Formula check.* At RoE 34.0% the elite formula gives 24 + 0.3 x 1.0 = 24.3x. The approved
   24.5x implies RoE 34.7%. Track 2: no effect (cap binds). Track 1: 24.3 x 0.76 = 18.47x, which is
   0.15x lower and worth Rs 2.4 per share [336.42 x 0.15 / 20.8416].
2. *Which RoE is "current" under STAGNANT (chunk 01 table: STAGNANT → current).* At the valuation
   date (31-Mar-2027) the current year is FY27, so ~34% is consistent with the forward basis. If
   the FY26 actual 84.4% were read as current, Pillar 1 = 30x (elite cap), Track 1 = min(30 x 0.76
   = 22.8x, 22.67x) = 22.67x, and Track 1 today-value rises from Rs 414.0 to Rs 479.3 [2,156.64 +
   336.42 x 22.6667 + 208.05 = 9,990.21]. The FY26 figure sits on pre-IPO parent capital that the
   slice no longer uses (FLDG deposits are operating collateral), so the operator's FY27 reading is
   the better-evidenced one.
3. *Pillar 2L band.* The 0.80x "Stressed" band lists "GNPA rising" as a criterion. GNPA rose
   sequentially from 2.12% (Mar-26) to 2.25% (Jun-26) (B10.gnpa_stage3_q1fy27_pct). The operator
   ruled 1.00x on the YoY reading (+13 bps vs +75 bps a year earlier; seasonal; override 1). At
   0.80x the slice would be Track 2 19.6x, Track 1 14.9x, and Track 1 today-value Rs 353.9.
   Separating observation: the operator's Q2 FY27 vs Q2 FY26 T3 test (STARTING if Stage 2 <= 3.3%
   and GNPA < 2.92%; DECLINING if Stage 2 > 4.11% or GNPA > 2.92%), confirm-by 30-Nov-2026.

Slice worksheet line (chunk 04): "Slice partner half | basis THREE-PILLAR | A: RoE ~34% (parent ex
Si Creva, operator figure) → 24.5x | B: 2L 1.00x | C: 24.5x | D: +0x | E: +0x (owns scarce asset:
N) | F: 24.5x | F2: 24.5x | G: operator blend 22.67x | G2: N | G3: 22.67x | H: 22.67x (Track 1
18.62x) | slice PAT FY28 Rs 336.42 Cr (54% x 623) | slice value Rs 6,264.1 Cr (Track 1) / Rs 6,944.8
Cr (midpoint) / Rs 7,625.5 Cr (Track 2)."

### 1B.2 Slice 1: own book (Si Creva), P/B on Mar-27 book

| Item | Value | Anchor |
|---|---|---|
| Mar-27 book | Rs 2,695.8 Cr = FY26 1,231.98 + IPO 636.8 + 75% of raise 624.15 + 46% of FY27 PAT 202.86 | B10.own_book_book_mar27_cr; deliberation section 5 |
| P/B low / base / high | 0.8x / 1.0x / 1.2x | B10.own_book_pb_* |
| Operator reason | "RoE ~10% post-raise, recovering toward FY26's 14% as capital is lent out" | B10.own_book_roe_reasoning |
| Slice value | Rs 2,156.6 / 2,695.8 / 3,235.0 Cr | [INFERENCE] |

Cross-checks on the slice (display only, chunk 02 "P/B = ROE ÷ CoE"; chunk 04 A27.2):
- Own-book RoE path [INFERENCE, Section 2]: FY28 10.1%, FY29 11.8%, FY30 12.9%, FY31 13.5%.
- Theoretical P/B at r 15.5%: 0.65x (FY28) to 0.87x (FY31). At 14%: 0.72x to 0.96x. The approved
  0.8x low sits inside that band; the 1.2x high needs own-book RoE ~18.6% at 15.5%, above any
  year of the path. Reported, not changed.
- Slice PE-equivalent: RoE 10% → Pillar 1 0.5 x 10 + 7.5 = 12.5x; 2L 1.00x; P3 +0; cap 18x → Track
  2 12.5x, Track 1 9.5x. On FY28 own PAT Rs 286.6 Cr: Rs 3,582 Cr (Track 2) / Rs 2,723 Cr (Track 1).
  Track 1 sits within 1% of the 1.0x P/B value.
- A16 note: own-book RoE stays below r 15.5% through FY31. Own-book growth earns below its cost of
  capital in every projection year, which is why its P/B stays at or below 1.0x on the path.

### 1B.3 Whole-company cross-check rows (not primary)

| Row | Calculation | Value | Citation |
|---|---|---|---|
| A | RoE ~17% (30-Jun equity basis; operator ruling H): 0.5 x 17 + 7.5 | 16.0x | section-1b chunk 01 |
| B | Pillar 2L Sound | 1.00x | section-1b chunk 02 |
| C | 16.0 x 1.00 | 16.0x | chunk 06 |
| D | Pillar 3 (as slice 2) | +0x | section-1b chunk 03 |
| E | Strategic | +0x | section-1b chunk 04 |
| F / F2 | UA not qualified | 16.0x | section-1b chunk 05 |
| G | Banks / NBFCs / MFIs | 18x (P/B primary; PE cross-check only) | section-1b chunk 05; B10.sector_cap_value |
| G2 / G3 | No override | 18x | chunk 05 |
| **H Track 2** | min(16.0, 18) | **16.0x** (range 15.0x to 17.0x) | chunk 06 |
| **Track 1** | 16.0 x 0.76 | **12.16x** | section-1b chunk 15 |

Relative PE expression (A15, chunk 15): "absolute H 16.0x (whole company) / 22.67x (partner slice)
| market PE 20.5x (Nifty 50 TTM, macro sheet August 2026, STALE) | relative destination PE 0.78 /
1.11 | name historical relative band NOT FOUND (listed 5 months) | sector historical relative band
NOT FOUND | B8 rating NOT FOUND (Part B not in B10) | conclusion: no basis to place H off its
operator-approved point."

**Step 1C (A20, chunk 15): PENDING LIVE PEER TABLE.** Pillar destination governs (approved base).
No peer multiple is used or quoted (Correction 6 guard).

### 1B.4 Summary of the approved destination

| Track | Own book P/B | Partner P/E | Cash | Use |
|---|---|---|---|---|
| Track 1 (RRM) | 0.8x | 18.62x | Rs 208.05 Cr at face | **Governing: entry zone, FV path, decomposition** |
| Midpoint (approved SOTP base) | 1.0x | 20.6433x | Rs 208.05 Cr | HR destination mid; cross-check |
| Track 2 (additive) | 1.2x | 22.6667x | Rs 208.05 Cr | Upper bound |

Pairing note: the deliberation pairs 0.8x with 18.62x ("Low") and 1.2x with 22.67x ("High"). This
report follows that pairing. Section 1B has no RRM track for a P/B slice.

Interim: "Section 1B complete. Approved SOTP 18.62x / 20.64x / 22.67x with own book 0.8x / 1.0x /
1.2x. Track 1 governs (17.9% divergence). Three divergences reported, none applied."

---

## SECTION 2: PROJECTIONS (operator FY27-FY28, Stage 11 extension FY29-FY32)

### 2A. AUM (the lender's revenue analog) and the fade

The operator inputs stop at FY28 (B10.pat_base_fy27_cr / fy28; aum_base_fy27_cr / fy28). Year
numbering follows the valuation date: Year 0 = FY27 (ends 31-Mar-2027), Year 1 = FY28 ... Year 3 =
FY30, Year 4 = FY31 (committed, A18.0), Year 5 = FY32.

**Basis (Rule B, section-1b chunk 07): RUN-RATE.** Q1 FY27 AUM Rs 8,001 Cr vs Rs 7,066 Cr at Mar-26
= +13.2% QoQ (B10.aum_q1fy27_cr, aum_fy26_cr). Three more quarters at that pace reach 8,001 x
1.1318^3 = Rs 11,600 Cr, the operator FY27 figure. FY28 +35.0% is the operator's step-down.

**Fade (A14, section-1b chunk 07): Emerging Moat MODEST (EM 18.5; B10.em_classification) → fades to
industry growth by Year 3 (FY30).** Industry anchor: **20%**, the India PL + LAP market growth rate
(B10.tam_growth_pct; B09.tam_source). This is a corpus-anchored figure, not a free assumption.
Step-down: FY28 35.0% → FY29 27.5% (linear midpoint) → FY30 20.0% → FY31 20.0% → FY32 20.0%.

Historical cross-check: AUM +73.0% FY26 (B10.aum_growth_fy26_yoy_pct), PAT +75.0% FY26; 3-year
CAGR NOT FOUND (B10 report: RHP restated FY23-FY25 not assembled). Base AUM CAGR FY26-FY30 35.7%
and PAT CAGR 37.4%: divergence about -37 pp each (> 10 pp), so ledger rows 1 and 2 carry the
confirming observations (chunk 09). SOM cross-check: base AUM CAGR FY26-FY29 = (19,966.5 / 7,066)^(1/3)
- 1 = 41.4% vs SOM-implied 61.4% (B10.som_3yr_revenue_cagr): **consistent**, base below SOM.

### 2B. Return on average AUM bridge (the lender's margin bridge, Rule C)

| Lever | bps | Evidence | Confirm-by |
|---|---|---|---|
| Current return on avg AUM (Q1 FY27 run-rate) | 5.05% [380.32 / 7,533.5] | results Q1 FY27 p.5; press release p.2 | n/a |
| Finance cost rises as debt is rebuilt; mix shifts to partner and LAP | net -48 bps to FY28 (lever split NOT FOUND: standalone NIM and FLDG-in-opex are NOT FOUND in B10) | deliberation section 7 T2 note; T2 DECLINING -1 | 31-May-2028 (ledger D1) |
| Credit cost -10% to -15% YoY (FY27 guidance) | offsets inside the net; bps NOT FOUND | B10.guided_margin_band | 31-May-2027 (ledger row 3) |
| **FY28 (operator)** | **4.571%** [623 / 13,630] | deliberation section 5 ("4.6%") | |
| **Year 3 FY30 (base)** | **4.571%, held** | Reading A below | |

**Extension uncertainty: the two readings (A26.3).**
- **Reading A (base, most evidenced): return on avg AUM holds at 4.571% from FY28.** The signed
  FTTCP verdict set reads T2 NIM DECLINING (-1), T3 asset quality STARTING (+1), T4 RoA/RoE
  STAGNANT (0). A falling spread offset by falling credit cost gives a flat RoA, and T4 STAGNANT is
  the sole forward RoA authority. Leverage stabilises once AUM growth (20%) meets RoE (~19.5%), so
  the debt-rebuild drag ends by about FY30.
- **Reading B: the operator's FY27→FY28 slide (-15 bps a year) continues** (4.42% / 4.27% / 4.12%
  for FY29-FY31), as T2 DECLINING and the debt rebuild run on.
- **Separating observation:** FY27 return on average AUM vs 4.75% at the Q4 FY27 results
  (confirm-by 31-May-2027), then FY28 vs 4.571% (31-May-2028). Ledger row D1 tracks it.
- Effect: Reading B lowers FY31 PAT from Rs 1,204.7 Cr to Rs 1,086.1 Cr (-9.8%), Track 1 end-Year-3
  FV from Rs 737.7 to Rs 678.9, and **flips the A19 label from COMPOUNDER (21.2%) to HYBRID
  (17.9%)**. The doubt goes to position size (A25), not into the base number.

**46 / 54 split: kept** (B10.split_own_partner_pct). B10 carries no evidence for another split;
disbursement by book is open item DBB. Readings: (A) 46/54 holds at the Q1 FY27 AUM share; (B)
partner share keeps rising (deliberation section 7: "partner share rising"). Each 1 pp of FY28 PAT
moved from own to partner adds Rs 5.3 per share at Track 1 [6.23 x (18.62 - 0.8) / 20.8416] and
Rs 5.9 at the midpoint; Rs 10 Cr moved adds Rs 9.4 at the midpoint (deliberation section 5 alignment
note). Reading B also moves the partner-cap revisit triggers closer (FLDG > 40% of partner revenue;
top-two partners > 90%). Separating observation: the DBB IR reply and the Q2 FY27 deck AUM mix,
confirm-by 30-Nov-2026.

### 2C. Projection table (base case)

| Line | FY26 actual | FY27 Y0 | FY28 Y1 | FY29 Y2 | FY30 Y3 | FY31 Y4 | FY32 Y5 |
|---|---|---|---|---|---|---|---|
| AUM, Mar (Rs Cr) | 7,066 | 11,600 | 15,660 | 19,966.5 | 23,959.8 | 28,751.8 | 34,502.1 |
| AUM growth | +73.0% | +64.2% | +35.0% | +27.5% | +20.0% | +20.0% | +20.0% |
| Average AUM | ~5,575 [FY25 7,066/1.73] | 9,333 | 13,630 | 17,813.3 | 21,963.2 | 26,355.8 | 31,627.0 |
| Return on avg AUM | ~5.05% | 4.73% (operator "4.75%") | 4.571% | 4.571% | 4.571% | 4.571% | 4.571% |
| **PAT** | 281.45 | **441** | **623** | **814.2** | **1,003.9** | **1,204.7** | **1,445.6** |
| PAT growth | +75.0% | +56.7% | +41.3% | +30.7% | +23.3% | +20.0% | +20.0% |
| EPS, diluted 20.8416 Cr (Rs) | 21.39 (reported, pre-raise count) | 21.16 | 29.89 | 39.07 | 48.17 | 57.80 | 69.36 |
| Own book, Mar (46% of PAT retained) | | 2,695.8 | 2,982.4 | 3,356.9 | 3,818.7 | 4,372.9 | 5,037.8 |
| Consolidated equity, Mar (SOTP roll) | 1,231.98 | 3,142.0 | 3,765.0 | 4,579.2 | 5,583.1 | 6,787.8 | 8,233.4 |
| BVPS (Rs) | 131.33 (B10) | 150.76 (alt. 164.3, see flag) | 180.65 | 219.71 | 267.88 | 325.68 | 395.04 |
| RoE, average equity | 23.97% | n.m. (IPO and raise mid-year) | 18.0% | 19.5% | 19.8% | 19.5% | 19.2% |
| Own-book RoE | | ~10% (operator) | 10.1% | 11.8% | 12.9% | 13.5% | |
| AUM / equity | 5.74x | 3.69x | 4.16x | 4.36x | 4.29x | 4.24x | 4.19x |
| Revenue, EBITDA, CFO, FCF, net debt | NOT PROJECTED: lender. Valuation runs on AUM x return on AUM; EBITDA n/a; CFO negative by Ind AS 7 (GROWTH INDUCED); net debt n.m. (B10) |

Assumptions stated: no dividend (B10: no dividend history), share count constant at 20.8416 Cr (ESOPs
already in the fully diluted count), no further equity raise (AUM/equity stays below the FY26 5.74x).

**Bear and bull (PAT, Rs Cr):**

| Case | FY27 | FY28 | FY29 | FY30 | FY31 (Y4) | FY32 | Rule |
|---|---|---|---|---|---|---|---|
| Bear | 400 | 500 | 580.3 | 672.7 | 778.9 | 900.7 | Operator FY27-28. Then industry 20% AUM growth from FY29 (immediate fade) with Reading B's -15 bps/yr return slide: growth 16.1% / 15.9% / 15.8% / 15.6% (chunk 07 bear rule: industry growth or triggers fail) |
| Base | 441 | 623 | 814.2 | 1,003.9 | 1,204.7 | 1,445.6 | Above |
| Bull | 470 | 700 | 949.8 | 1,218.6 | 1,523.3 | 1,904.1 | Operator FY27-28. Then base growth + 5 pp (grade C: guidance not at face value; chunk 17 bull gate) |

### 2C-w worksheet line (section-1b chunk 17)

"Base-case basis: RUN-RATE (AUM). Evidence: Q1 FY27 results p.5 and press release
20260729-74639f09 p.2, 29-Jul-2026 (AUM 8,001 vs 7,066, +13.2% QoQ); operator-approved AUM 11,600 /
15,660 and PAT 441 / 623 (fttcp-deliberation section 5, 04-Oct-2026); A14 MODEST fade to the 20%
industry anchor (B10.tam_growth_pct) by FY30. Historical CAGR cross-check: AUM +73.0% / PAT +75.0%
(FY26, one year; 3-year NOT FOUND) (divergence -37.3 pp AUM / -37.6 pp PAT, confirm-by observation:
AUM >= 11,600 at Mar-27 and >= 15,660 at Mar-28, ledger rows 1-2, date: 31-May-2027 / 31-May-2028).
Margin bridge: current 5.05% (return on avg AUM, Q1 FY27 run-rate) -> Year 3 4.571% via [finance
cost and mix: -48 bps net, deliberation section 7] + [credit cost guidance -10% to -15% YoY: inside
the net, bps NOT FOUND] x 2. Track-record period for weighting: trailing 2 quarters (delivery scored
over 1), Role 5 grade C. Catalyst credit split: revenue (earnings path) 100% / Pillar 3 0%."

### 2D. Projection sanity checks (section-1b chunk 06)

| Check | Result | Pass? |
|---|---|---|
| Growth faster than capacity allows? | Capacity = capital. AUM/equity 3.7x-4.4x vs 5.74x at FY26; CRAR 40.2% post-raise (B10 FLAG-CAPITAL-RAISE) | PASS |
| Margins require something unprecedented? | Return on AUM 4.571%, below FY26 ~5.05% and the Q1 run-rate 5.05% | PASS |
| ROCE (RoE) stays above 15%? | Whole company 18.0%-19.8%. Own book 10.1%-13.5%, below r 15.5% | PASS whole company; FLAG own book |
| FCF funds growth without excessive new debt? | Retained earnings hold AUM/equity below FY26 leverage. The debt rebuild runs through Si Creva borrowings that the parent guarantees (228% of parent net worth FY26; B10 FLAG-CAPITAL-STRUCTURE) | PASS with FLAG |
| EPS growth from operations? | AUM growth at a flat return; no buyback; share count fixed | PASS |
| Implied market share realistic? | FY29 AUM 19,967 = 59% of the 3-year SOM 33,620 (B10.som_3yr_cr) | PASS |
| CFO/PAT consistent with Pillar 2? | Lender: Pillar 2L governs. Consolidated CFO stays negative while AUM grows (Ind AS 7), as GROWTH INDUCED predicts | PASS |
| Year 3 ROE consistent with FTTCP verdict? | RoA flat (STAGNANT) by construction. RoE drifts 17% → 19.8% through leverage. Not credited in Pillar 1, premium or r | PASS with note |
| **Did the base credit the transition, or price the audited past?** | The base runs off the Q1 FY27 run-rate and the operator's forward PAT, not the audited +75%. It credits the volume path. It does NOT credit the rung climb: the proof gate (all-in loss < 10.5%) adds nothing to the flat return; that climb sits only in ledger row 3 at p 0.20 | Forward path credited; climb uncredited by design |

Interim: "Section 2 complete. Projections built to FY32; Year 4 (FY31) PAT Rs 1,204.7 Cr committed."

---

## SECTION 3: METHODS APPLIED

### 3.1 SOTP (primary)

Formula at date t (31-Mar): FV_t = P/B x own book_t + partner P/E x 54% x PAT(FY t+1) + Rs 208.05 Cr.

**Today-value at the valuation date, 31-Mar-2027** (reproduces deliberation section 5 exactly):

| Case | Track 1 (0.8x / 18.62x) | Midpoint (1.0x / 20.64x) | Track 2 (1.2x / 22.67x) |
|---|---|---|---|
| Bear (400/500) | 7,377.0 → **Rs 354.0** | 8,458.7 → Rs 405.9 | 9,540.4 → Rs 457.8 |
| Base (441/623) | 8,628.8 → **Rs 414.0** | 9,848.7 → Rs 472.5 | 11,068.5 → Rs 531.1 |
| Bull (470/700) | 9,413.7 → Rs 451.7 | 10,720.4 → Rs 514.4 | 12,027.0 → Rs 577.1 |

Base Track 1 build: 0.8 x 2,695.8 = 2,156.64 | 18.62 x 336.42 = 6,264.14 | cash 208.05 | total
8,628.83 | / 20.8416 = Rs 414.02.

**Year-3 value, 31-Mar-2030** (Mar-30 book; FY31 PAT):

| Case | Track 1 | Midpoint | Track 2 |
|---|---|---|---|
| Bear | Rs 519.5 | Rs 593.7 | Rs 668.0 |
| Base | **Rs 737.7** | Rs 837.5 | Rs 937.3 |
| Bull | Rs 899.5 | Rs 1,018.0 | Rs 1,136.5 |

Base Track 1 build: 0.8 x 3,818.71 = 3,054.97 | 18.62 x 650.52 (54% x 1,204.67) = 12,112.71 | cash
208.05 | total 15,375.73 | / 20.8416 = Rs 737.74. Bear: own book 3,483.33; partner PAT 420.63.
Bull: own book 4,028.62; partner PAT 822.56.

### 3.2 Whole-company P/E cross-check (operating EPS + A27.1 cash line)

| Date | Track 1 12.16x | Track 2 16.0x | SOTP same track | Divergence |
|---|---|---|---|---|
| 31-Mar-2027 (FY28 EPS Rs 29.89) | 363.5 + 9.98 = **Rs 373.5** | 478.3 + 9.98 = **Rs 488.3** | Rs 414.0 / Rs 531.1 | SOTP +10.9% / +8.8% |
| 31-Mar-2030 (FY31 EPS Rs 57.80) | Rs 712.8 | Rs 934.8 | Rs 737.7 / Rs 937.3 | SOTP +3.5% / +0.3% |

The SOTP-implied whole-company forward PE falls over the hold (midpoint 15.5x at Mar-27, 14.3x at
Mar-30), because the own book is valued on book while its PAT grows faster than book. By Year 3 the
two methods converge.

### 3.3 Whole-company P/B cross-check

Theoretical P/B = RoE / CoE = 17% / 15.5% = **1.10x** (Track 1 r); 17% / 14% = **1.21x** (base r,
chunk 15 range 12-14%).

| Date | BVPS | P/B value at 1.10x / 1.21x | SOTP midpoint | Divergence |
|---|---|---|---|---|
| 31-Mar-2027 | Rs 164.3 (B10.bvps_mar27_rs) | Rs 180.2 / Rs 199.5 | Rs 472.5 | SOTP **+137%** over 1.21x |
| 31-Mar-2030 | Rs 267.9 (SOTP roll) | Rs 293.9 / Rs 325.3 | Rs 837.5 | SOTP +157% |

The SOTP midpoint is 2.88x Mar-27 book [472.5 / 164.3]. Implied perpetual growth at 17% RoE:
12.4% at 14% CoE and 14.7% at 15.5% [P/B = (ROE - g) / (CoE - g)]. This matches deliberation override
5 and is the operator's stated reason for holding the entry zone at ~Rs 350.

**FLAG-BOOK-BASE-CONFLICT (B10 internal).** Two Mar-27 consolidated book figures are in B10:
- BVPS route: Jun-26 net worth 2,245.9 (Q1 deck BVPS 133.3 x 16.85 Cr) + Q2-Q4 FY27 PAT 345.9 + raise
  832.20 = **Rs 3,424.0 Cr (Rs 164.3/share)**.
- SOTP route: own book 2,695.8 + cash 208.05 + partner share of FY27 PAT 238.14 = **Rs 3,142.0 Cr
  (Rs 150.8/share)**.
- Gap Rs 282.0 Cr (Rs 13.5/share). The root sits at Jun-26: FY26 1,231.98 + IPO 636.8 + Q1 PAT 95.08
  = 1,963.9, against the deck-implied 2,245.9.
- Readings: (a) 1,231.98 is the consolidated FY26 net worth and the deck BVPS overstates; (b)
  consolidated FY26 net worth is higher and the own book is understated by up to Rs 282 Cr (+Rs 10.8
  per share at 0.8x, +Rs 13.5 at 1.0x).
- Separating observation: the AR consolidated balance sheet total equity at 31-Mar-2026 and the
  IPO fresh-issue net proceeds; confirm by Claude Code extraction before /finalize sign-off.
- Valued on the approved 2,695.8 Cr.

### 3.4 Method summary (Year 3, 31-Mar-2030)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| SOTP Track 1 (governing) | 100% | Rs 519.5 | Rs 737.7 | Rs 899.5 |
| SOTP Track 2 | (track) | Rs 668.0 | Rs 937.3 | Rs 1,136.5 |
| P/E whole company Track 1 / Track 2 | 0% | Rs 464.5 / Rs 608.0 | Rs 712.8 / Rs 934.8 | Rs 898.7 / Rs 1,179.4 |
| P/B whole company 1.10x / 1.21x | 0% | n.c. | Rs 293.9 / Rs 325.3 | n.c. |

P/E cross-check bear and bull at FY31 EPS Rs 37.37 / Rs 73.09 [778.9 and 1,523.3 / 20.8416], + cash.

Interim: "Section 3 complete. SOTP applied on both tracks; P/E converges by Year 3; P/B diverges by
over 130% and is the outlier."

---

## SECTION 4: TRIANGULATION, ENTRY, VERDICT

### 4A. Triangulated fair value (both tracks; SOTP 100%)

| | Bear | Base | Bull |
|---|---|---|---|
| Track 1, Year 3 (31-Mar-2030) | Rs 519.5 | **Rs 737.7** | Rs 899.5 |
| Track 2, Year 3 | Rs 668.0 | Rs 937.3 | Rs 1,136.5 |
| Track 1, today (31-Mar-2027) | Rs 354.0 | Rs 414.0 | Rs 451.7 |
| Track 2, today | Rs 457.8 | Rs 531.1 | Rs 577.1 |

### 4B. Methods agreement

| Check | Result |
|---|---|
| Same direction? | SOTP and P/E: yes, both above CMP. P/B: no, far below CMP |
| Spread highest to lowest (today, base) | SOTP midpoint Rs 472.5 vs P/B Rs 199.5: 137% |
| Outlier and why | P/B. Consolidated book cannot see the partner half's off-book fee earnings |
| Most trusted here | SOTP, with the P/B gap kept on the card as the book-value caution the operator priced into the override |

### 4C. Return at CMP Rs 369.55 (04-Oct-2026 to 31-Mar-2030 = 3.487 years)

| Scenario | Track 1 FV | CAGR | Track 2 FV | CAGR | Meets 25%? |
|---|---|---|---|---|---|
| Bear | Rs 519.5 | 10.3% | Rs 668.0 | 18.5% | No / No |
| Base | Rs 737.7 | 21.9% | Rs 937.3 | 30.6% | No / Yes |
| Bull | Rs 899.5 | 29.1% | Rs 1,136.5 | 38.0% | Yes / Yes |

### 4D. Probability-weighted expected return (grade C: 35 / 45 / 20; section-1b chunk 17)

| Scenario | Probability | Track 1 CAGR | Weighted | Track 2 CAGR | Weighted |
|---|---|---|---|---|---|
| Bear | 35% | 10.3% | 3.6% | 18.5% | 6.5% |
| Base | 45% | 21.9% | 9.9% | 30.6% | 13.8% |
| Bull | 20% | 29.1% | 5.8% | 38.0% | 7.6% |
| **Expected CAGR** | 100% | | **19.3%** | | **27.8%** |

Grade source: B10.credibility_grade C, trailing 2 quarters (Rule E). Re-weighting rule not
triggered (no two consecutive quarters below bear). Midpoint expected CAGR 23.7%.

### 4D-2. Amendment 21 run-rate base (section-1b chunk 08)

"Earnings base: single-quarter-annualised | PAT run-rate Rs 380.32 Cr (Q1 FY27 Rs 95.08 Cr x 4;
results Q1 FY27 p.5) | one-offs adjusted: none stripped. Treasury income on IPO proceeds (listed
08-May-2026) is NOT FOUND; the Rs 832 Cr raise is not in Q1. B10 sets no seasonal flag | annual model
divergence -13.8% vs FY27 base 441 (under 25%); -39.0% vs FY28 forward 623 (governing: the
operator-approved FORWARD basis governs every fair value; the A21 base governs T1 in the price
decomposition)." Run-rate EPS Rs 18.25 on 20.8416 Cr.

### 4D-3. Price decomposition (A24, section-1b chunk 08) and Expectation Ledger (A22-A23, chunk 09)

Ledger written to outputs/expectation-ledger.md. Probabilities are **PROVISIONAL** Stage 11
proposals: B10 carries none (override 3; see Unresolved inputs).

| # | Catalyst | PAT increment | p | Prob-weighted | Tier |
|---|---|---|---|---|---|
| 1 | FY27-exit AUM 11,600 | +205.29 | 0.70 | +143.70 | T2 |
| 2 | FY28 AUM 15,660 | +102.48 | 0.60 | +61.49 | T2 |
| 3 | Bull state FY28 PAT 700 (credit cost, rating upgrade, proof gate) | +77.00 | 0.20 | +15.40 | T3 |
| D1 | Return on AUM 5.05% → 4.571% (mandatory downside) | -65.09 | 0.70 | -45.57 | nets T2 |
| D2 | Partner exit, partner PAT -1/3 | -112.14 | 0.15 | -16.82 | nets T2 |
| D3 | Asset-quality reversal | NOT FOUND | n/a | not credited | watch |

Base rows reconcile: 380.32 + 205.29 + 102.48 - 65.09 = 623.00.

Translation to value: T1 runs the SOTP on confirmed inputs; increments take the effective Track 1
SOTP multiple 10.58x per Rs 1 Cr of FY28 PAT [(8,420.78 - 5,853.38) / (623 - 380.32)].

T1 build (Track 1): confirmed own book Rs 2,536.67 Cr (FY26 1,231.98 + IPO 636.8 + 75% of raise 624.15
+ 46% of Q1 FY27 PAT 43.74) x 0.8 = 2,029.34 | partner 54% x 380.32 = 205.37 x 18.62 = 3,824.04 | cash
208.05 | **T1 = 6,061.43**.

**Decomposition at the B10 market value Rs 7,555.1 Cr (Rs 362.50 per diluted share), governing Track 1:**

| Tier | Rs Cr | Rs/share | % of market value |
|---|---|---|---|
| T1 Confirmed | 6,061.4 | 290.83 | **80.2%** |
| T2 High-probability (net of D1, D2) | 1,510.8 | 72.49 | **20.0%** |
| T3 Speculative | 162.9 | 7.82 | **2.2%** |
| Residual (unsupported premium) | -180.1 | -8.64 | **-2.4%** |

Midpoint cross-check (1.0x / 20.64x; effective 11.80x): T1 92.4% | T2 22.3% | T3 2.4% | residual -17.2%.
At CMP x diluted shares (Rs 7,702.0 Cr) the Track 1 residual is -0.4%.
Sensitivity: with rows 1, 2 and D1 at p = 1.0, T2 rises to 31.6% and the residual to -14.0%.

"Decomposition at Rs 369.55: T1 80.2% | T2 20.0% | T3 2.2% | residual -2.4% | governing multiple:
pillar (approved SOTP Track 1: 0.8x P/B, 18.62x P/E; effective 10.58x)."
Step 1C cross-check on the tier multiple: PENDING LIVE PEER TABLE.

Reading: the price is fully covered by confirmed plus high-probability value on Track 1. The market
pays nothing for the speculative tier. The residual is below 25%, so no starter cap engages from it.

### 4D-4. Hurdle Ratio (feasibility only; section-1b chunk 06, OR-2)

"Hurdle basis (A27.3): FORWARD, same at entry and exit (A18.1) | Current PE 19.70x = (CMP Rs 369.55
- surplus cash Rs 9.98/share) / A21 run-rate EPS Rs 18.25 (treasury income on the cash NOT FOUND, not
stripped) | EPS CAGR (prob-weighted) 39.9% (Rs 18.25 → Rs 49.96, FY31 forward EPS on the ledger's
prob-weighted FY28 PAT 538.53, rolled at the base fade) | Destination PE mid 14.67x (SOTP-implied whole
company at 31-Mar-2030, midpoint slice multiples 1.0x / 20.64x) | Catalysts: rows 1-2 earnings path 100%
/ exit multiple 0%; row 3 earnings path 100% / exit multiple 0%; each sums to 100%."

| HR line | Calculation | HR | vs 1.953 (Tier A) |
|---|---|---|---|
| **Prob-weighted (governing)** | 1.399^3 x 14.67 / 19.70 = 2.738 x 0.744 | **2.04** | PASS |
| Base point | 1.469^3 x 14.32 / 19.70 (A21 start; equals FY31 base operating FV Rs 827.6 / Rs 359.6) | 2.30 | PASS |
| Bull (grade C: base + 5 pp, bull EPS not used) | 1.519^3 x 14.32 / 19.70 | 2.54 | PASS |

**Band: PASS** (the tier hurdle is feasible on base earnings). It caps no verdict.

Two notes the card carries:
- On Track 1 multiples (the governing entry track) the prob-weighted HR is **1.79**, below 1.953.
  The PASS rests on the midpoint destination.
- Time-exact: from 04-Oct-2026 the exit at 31-Mar-2030 is 3.487 years away; 1.25^3.487 = 2.177. The
  prob-weighted HR (2.04) falls short of that; the base point HR (2.30) clears it.

Tier line: "Tier: A | Hurdle: 25%" (B10.hurdle_tier; FII+DII NOT FOUND, Gate 0 / EM below Tier B
gates).

### 4D-5. Amendment 18 and Amendment 19: FV path (section-1b chunks 10, 12)

Horizon: Year 4 (FY31) and Year 5 (FY32) committed in Section 2 (18.0). No exit haircut: a Year 4-5
story exists (EM MODEST, SOM runway MASSIVE per B10.runway_class).

**Option Resolution Calendar (18.2): no option slices.** Both SOTP slices are operating earnings today.
Invincible Minds Pvt Ltd (incorporated 17-Jun-2026; B10.ar_new_downstream_entities) has no named
resolution event in B10. It is narrative and takes zero value. 18.3 / 18.4 / 18.7: not applicable.
18.6 dual display: static-carry exit and resolution-based exit are identical (no options).

**FV path, governing Track 1 (0.8x / 18.62x), base case:**

| Row | Date | Own book x 0.8 | Partner: 54% x PAT(t+1) x 18.62 | Cash (constant) | Total (Rs Cr) | Rs/share | YoY |
|---|---|---|---|---|---|---|---|
| Today (valuation date) | 31-Mar-2027 | 2,156.6 | 336.42 (FY28) → 6,264.1 | 208.05 | 8,628.8 | **414.0** | |
| End-Year-1 | 31-Mar-2028 | 2,385.9 | 439.67 (FY29) → 8,186.7 | 208.05 | 10,780.7 | 517.3 | +24.9% |
| End-Year-2 | 31-Mar-2029 | 2,685.5 | 542.10 (FY30) → 10,093.9 | 208.05 | 12,987.5 | 623.2 | +20.5% |
| End-Year-3 (exit) | 31-Mar-2030 | 3,055.0 | 650.52 (FY31) → 12,112.7 | 208.05 | 15,375.7 | **737.7** | +18.4% |

Cross-check paths (same machinery): midpoint 472.5 → 588.6 → 708.0 → 837.5; Track 2 531.1 → 659.9 →
792.8 → 937.3.

**FV CAGR line (19.1): "FV CAGR over the hold: 21.2% (today Rs 414.0 to end-Year-3 Rs 737.7, governing
Track 1, base case)."** [(737.74 / 414.02)^(1/3) - 1]

**Return-source label (19.2): COMPOUNDER** (>= 20%). Margin: 1.2 pp above the threshold.

| Path | FV CAGR | Label |
|---|---|---|
| Track 1 base (classification input) | **21.2%** | **COMPOUNDER** |
| Midpoint base | 21.0% | COMPOUNDER |
| Track 2 base | 20.9% | COMPOUNDER |
| Track 1, Reading B (return slides 15 bps/yr) | 17.9% | HYBRID |
| Track 1, prob-weighted ledger path | 20.5% | COMPOUNDER |
| Track 1 bear | 13.6% | HYBRID |
| Track 1 bull | 25.8% | COMPOUNDER |

**Decomposition line (19.3):** "2.4% of fair value today (1.4% at exit) is the static A27.1 cash line
(Rs 208.05 Cr, Rs 9.98/share), never compounded. No fair value is non-compounding option value: the SOTP
has no option slice. The growing fraction is the partner half (72.6% of today's Track 1 value),
compounding with FY28-FY31 PAT at 24.6% a year, and the own book (25.0%), compounding at 12.3% a year
through retained earnings at a held 0.8x. The MODEST fade drags PAT growth from 41.3% (FY28) to 20.0%
(FY31). No re-rating lever is credited: both slice multiples stay at the approved Track 1 destination.
The market's discount to that destination (Section 4F-2) is a return source outside the FV CAGR."

FV-step events (19.4): none (no within-hold option resolutions).

COMPOUNDER does not override the FTTCP verdict (DEEP WATCH leaning AVOID) or the VALUE-TRAP RISK
posture (chunk 12, 19.2). The label sits 1.2 pp above the threshold and flips to HYBRID under Reading B.
The separating observation is the FY27 return on average AUM vs 4.75% (31-May-2027).

### 4E. Entry price (section-1b chunk 06; OR-8; A27.1)

Entry = Track 1 end-Year-3 operating FV / (1.25)^N + cash per share. N = 3.487 years (04-Oct-2026 to
31-Mar-2030); 1.25^3.487 = 2.1773. Operating FV = Rs 737.74 - 9.98 = Rs 727.76.

| Calculation | Value |
|---|---|
| Base case FV, Year 3, Track 1 (operating line) | Rs 727.76 |
| Surplus cash per share, separate line at face (A27.1) | Rs 9.98 |
| Price for the tier hurdle = 727.76 / 2.1773 = 334.24, + 9.98 | **Rs 344.2** |
| FV CAGR and return-source label | **21.2% COMPOUNDER** |
| Price for 30% CAGR = 727.76 / 2.4964 (1.30^3.487) + 9.98 | **Rs 301.5** |
| MoS price (reference only; FAST-GROWTH carve-out puts MoS in size): 30% row (mixed evidence) → 334.24 x 0.70 + 9.98 | Rs 243.9 |
| **Mechanical entry range** | **Rs 301.5 to Rs 344.2** |

**Entry zone, side by side:**

| Line | Rs/share | Basis |
|---|---|---|
| **Operator override (BINDING)** | **~Rs 350** | Deliberation override 5. Operator's reasoning: "book-value cross-check: base implies 2.81x Mar-27 book, needing ~13% perpetual growth at 17% RoE." At the ruled multiples the base is 2.88x book, needing 12.4% growth at 14% CoE and 14.7% at 15.5%. Revisit "when disbursement-by-book and the Amendment 19 three-year FV CAGR are available." The FV CAGR is now available (21.2%); disbursement by book is still open (DBB) |
| Mechanical, chunk 06, Year-3 FV (governing formula) | **Rs 344.2** | This report |
| Mechanical, deliberation today-value method | Rs 371.4 | 414.0 / 1.25^0.487 (the cash line was discounted too) |
| Same method, A27.1-consistent | Rs 372.4 | (414.02 - 9.98) / 1.1148 + 9.98 |
| Midpoint, chunk 06 | Rs 390.1 | Cross-check |
| Track 1, Reading B, chunk 06 | Rs 317.2 | Return slides 15 bps/yr |

Plain reading:
- The operator set ~Rs 350 as a prudent hold below the Rs 371.4 mechanical figure.
- On the chunk 06 formula (Year-3 FV, A27.1 cash treatment), the mechanical entry is **Rs 344.2**.
  The override sits **1.7% above** it, not below.
- At Rs 350 the total-return CAGR to the Track 1 Year-3 value is 23.8%; to the midpoint 28.4%.
- Under Reading B the mechanical entry falls to Rs 317.2. The override holds only on Reading A.
- The override stays the operator's binding number. This report does not overwrite it.
- CMP Rs 369.55 sits 5.6% above the override and 7.4% above the mechanical entry.

### 4F. Risk-reward

| | Value |
|---|---|
| Bull Y3 (Track 1) Rs 899.5 | +143.4% vs CMP |
| Base Y3 (Track 1) Rs 737.7 | +99.6% |
| Bear Y3 (Track 1) Rs 519.5 | +40.6% (no Year-3 downside) |
| Upside / downside, Year 3 | n.m.: every Year-3 state sits above CMP |
| Upside / downside, valuation-date headline (operator's lens) | base Track 1 Rs 414.0 (+12.0%) / partner-exit headline Rs 313.8 (-15.1%) = **0.80x**, below 2x. Against the bear headline Rs 354.0 (-4.2%): 2.9x |

**Stress table (today-value, 31-Mar-2027; headline at low multiples; vs post-raise value Rs 362.5 and
vs CMP Rs 369.55):**

| Case | Total (Rs Cr) | Rs/share | vs Rs 362.5 | vs CMP | Year-3 Track 1 / midpoint |
|---|---|---|---|---|---|
| Low (0.8x / 18.62x) | 8,628.8 | 414.0 | +14.2% | +12.0% | 737.7 / 837.5 |
| Base (1.0x / 20.64x) | 9,848.7 | 472.5 | +30.4% | +27.9% | |
| High (1.2x / 22.67x) | 11,068.5 | 531.1 | +46.5% | +43.7% | 937.3 (Track 2) |
| **Bear, low multiples (HEADLINE)** | 7,377.0 | **354.0** | -2.4% | -4.2% | 519.5 / 593.7 |
| Bear, base multiples | 8,458.7 | 405.9 | +12.0% | +9.8% | |
| **Partner exit, low multiples (HEADLINE)** | 6,540.8 | **313.8** | -13.4% | -15.1% | 544.0 / 622.8 |
| Partner exit, base multiples | 7,533.7 | 361.5 | -0.3% | -2.2% | |
| Bull, base multiples | 10,720.4 | 514.4 | +41.9% | +39.2% | 1,018.0 (midpoint) |
| Bear + partner exit, low (compound tail) | 5,701.2 | 273.5 | -24.5% | -26.0% | |
| Pillar 2L at 0.80x reading, low | 7,376.0 | 353.9 | -2.4% | -4.2% | |
| Whole-company P/E Track 1 on bear FY28 (cross-check) | | 301.7 | -16.8% | -18.4% | |
| Whole-company P/B 1.10x on BVPS 164.3 (cross-check) | | 180.2 | -50.3% | -51.2% | |

All figures [INFERENCE]; the first eight rows reproduce deliberation section 5 at the ruled multiples.

### 4F-2. Recognition gap and transition posture (wrapper override 13)

Quality-ladder question (B10.recognition_gap_status): does the price already sit at the TO rung?
B10 frames FROM = cost-advantaged (R2, ~15-17x neighbourhood) and TO = franchise (R4, ~21x).

| Lens (approved FORWARD basis, ex cash) | Market | Destination | Gap |
|---|---|---|---|
| Whole company, forward PE on FY28 EPS | 12.03x [359.57 / 29.89] (11.79x at the B10 market value) | SOTP-implied 13.5x (Track 1) / 15.5x (mid) / 17.4x (Track 2); Pillar cross-check 12.2x / 16.0x | Market below every SOTP track: OPEN |
| Partner half, market-implied multiple [(7,347.05 - own book at P/B) / 336.42] | 15.4x (own 0.8x) / 13.8x (1.0x) / 12.2x (1.2x) | 18.62x (Track 1, ~R3) / 22.67x (Track 2, ~R4) | Market prices the fee half at or below R2: OPEN |
| Re-rating engine (destination / current, whole company) | | +12.4% (Track 1), +28.6% (mid), +44.9% (Track 2) | Not spent |

**Resolution: recognition gap OPEN on the governing forward basis.** The market prices the fee half at
the cost-advantaged rung, not the franchise rung.

Counter-reading, stated plainly: on book, the price already pays a franchise premium. CMP is 2.25x
Mar-27 BVPS Rs 164.3 (2.45x on the SOTP-roll Rs 150.8), against a theoretical 1.10x-1.21x. That
premium implies 11.6% perpetual growth at 17% RoE (14% CoE). The forward-PE discount exists only
because FY28 PAT is Rs 623 Cr, 121% above FY26. If FY27 PAT 441 does not print, the forward discount
disappears, the price sits on a franchise premium to book, and the gap reads CLOSED. Separating
observation: FY27 PAT vs Rs 441 Cr and FY27-exit AUM vs Rs 11,600 Cr at the Q4 FY27 results,
confirm-by 31-May-2027.

**Transition posture (CLAUDE.md matrix):** proof gate NOT FIRED (B10.proof_gate) + ugliness
STRUCTURAL-FEATURE (B10.ugliness_classification) → **VALUE-TRAP RISK**: DEEP WATCH or AVOID unless the
STRUCTURAL classification is disproven. With the gap OPEN, the "gap CLOSED + STRUCTURAL → AVOID"
overlay does not engage on the governing basis. It engages if the book-basis counter-reading prevails.

FLAG-UGLINESS-TEXT: the recorded classification reads "STRUCTURAL-FEATURE (negative CFO and
cost-to-income optics are artifacts)". "Artifacts" describes ARTIFACT-OF-CLIMB. B10 also records that
the operator has not named which optic is structural (off-book loss in opex, partner concentration,
parent guarantee). If the operator rules ARTIFACT, the posture reads RESEARCH / WATCH (proof NOT FIRED
+ ARTIFACT + gap OPEN). Neither cell is a trade before the proof gate fires: all-in loss / avg AUM below
10.5% in H2 FY27 (FY26 10.97%), with the off-book loss rate not rising, confirm-by 31-May-2027.

### 4F-3. Amendment 25 size state (section-1b chunk 08)

"Fast-growth: Y (basis: Q1 FY27 revenue +44.8% YoY, PAT +59.2% YoY; B10) | size: STARTER (Small,
2-3%); Small ceiling (Part 2.6) binds | next add trigger: none inside the ceiling. Above it: ledger row 1
CONFIRMED (Mar-27 AUM >= 11,600) AND proof gate fired (H2 FY27), plus an operator ruling that lifts the
Small ceiling."

| Test | Result |
|---|---|
| Starter: T1 + T2 >= 75% and residual <= 25% | 100.2% and -2.4%: met (Track 1, at CMP) |
| Add ladder to Medium: T1 >= 60% | 80.2%: met arithmetically; blocked by the Small ceiling |
| Large: T1 >= 80% AND Gate 0 EXCELLENT AND promoter TRUSTWORTHY | Not met (Gate 0 / EM Core 51 AVERAGE, B10 FLAG-EM-SCORE) |
| Dispersion cap (Year-3 Track 1: (899.5 - 519.5) / 737.7) | 51.5% → Medium cap |
| Tightest cap | **Small ceiling** (operator; deliberation section 5) |
| Trim ladder | Trim 25% for each ledger row that decays (rows 1, 2 first tested 31-May-2027 / 30-Nov-2026 interim); trim 50% if the residual exceeds 40% after a decay |
| Posture overlay | VALUE-TRAP RISK: the starter is executable only at or below the operator zone (~Rs 350), and the posture flag stands on the card. The decision stays with the operator |

### 4G. Exit multiple validation

| Check | Result | Pass? |
|---|---|---|
| Year 3 RoE justifies the RoE base and matches FTTCP? | FY30 RoE 19.8% >= 17% base; RoA flat = STAGNANT | PASS |
| Year 3 asset quality justifies Pillar 2L 1.00x? | No GNPA path in B10; rests on the Q2 FY27 T3 test | CONDITIONAL |
| Primary catalyst fired by Year 3 in base? | AUM path yes; proof gate not assumed | PARTIAL |
| Strategic premium justified, single credit kept? | +0x | PASS |
| UA ordering min(F x 1.25, cap)? | UA not applied | PASS |
| Buy a different stock at this exit with similar Year 3 metrics? | Whole company at a 12.6x (Track 1) to 14.3x (mid) implied forward PE for a ~19-20% RoE lender growing 20%: yes. Partner half at 18.62x-22.67x on a two-partner fee stream with 5% first-loss exposure: only once DBB and partner concentration are evidenced. The 22.67x cap rests on an operator blend Section 1B does not carry | CONDITIONAL |

"Would you personally pay this destination PE?" Track 1 (18.62x on the fee half, 0.8x on the book):
yes, within the Small ceiling. Track 2's 22.67x on the fee half: not before DBB and the partner-
concentration revisit. Per the wrapper, the approved base stands; the failed and conditional checks
are reported, not used to revise the multiple.

### 4H-pre. Mandatory conclusion elements

1. **Value vs price.**
   - Worth: Rs 414.0 (Track 1) to Rs 531.1 (Track 2) per share at 31-Mar-2027, compounding to Rs 737.7
     / Rs 937.3 by 31-Mar-2030. The single driver is the partner half's PAT (72.6% of Track 1 value)
     at 18.62x.
   - Price: the market pays 12.2x-15.4x for the fee half, at the cost-advantaged rung. Market-Implied
     flag: PENDING (block not in B10). The gap closes if FY27 PAT Rs 441 Cr and Mar-27 AUM Rs 11,600 Cr
     print (31-May-2027) and the proof gate fires in H2 FY27. It closes against the name (AVOID overlay)
     if the Q2 FY27 T3 test reads DECLINING (30-Nov-2026).
2. **Margin of safety row:** mixed evidence (B10.evidence_mix_summary: documented 11, claim 8,
   inference 4) → 30%. FAST-GROWTH carve-out: MoS is expressed as the starter size, not a price haircut.
3. **Dispersion:** (899.5 - 519.5) / 737.7 = 51.5% → Medium cap; the Small ceiling binds tighter.
4. **Edge claimed: PROCESS.** The pipeline read the AR notes that show the 228% parent guarantee
   (B02 rank 1) and the write-off-assisted GNPA (B02 rank 2), and rebuilt the SOTP to the rupee.

### 4H. VERDICT CARD

```
Tier: A | Hurdle: 25%
Priced under Section 1B v3.11 unmerged draft (open item I5)
CMP Rs 369.55 (01-Oct-2026) | Market value post-raise Rs 7,555.1 Cr (Rs 362.50/share, 20.8416 Cr FD)
CONVERTER classification: NON-CONVERTER (lender; A17 test a fails)
Entity count: 1 (SOTP slices are method outputs)
Method: SOTP primary 100% (A27.2) | P/E and P/B cross-checks 0%

DESTINATION (operator-approved, FORWARD, valuation date 31-Mar-2027)
  Own book (Si Creva): P/B 0.8 / 1.0 / 1.2x on Mar-27 book Rs 2,695.8 Cr
  Partner half: Pillar 1 24.5x (RoE ~34%) | 2L 1.00x | P3 +0 | Strategic +0 | UA N
                cap 22.67x (operator blend) | Track 2 22.67x | Track 1 18.62x (r 15.5%, RRM 0.76)
  SOTP P/E low / base / high 18.62 / 20.64 / 22.67x | divergence 17.9% → Track 1 sets entry (OR-1)
  Cash line Rs 208.05 Cr (Rs 9.98/share) at face, constant (A27.1)
  Whole-company cross-check: 16.0x Track 2 / 12.16x Track 1 / cap 18x
  Step 1C: pillar (approved) governs | adjusted peer base PENDING LIVE PEER TABLE | gap n/a

FAIR VALUE (Rs/share)        Bear     Base     Bull
  Track 1, 31-Mar-2027      354.0    414.0    451.7
  Track 2, 31-Mar-2027      457.8    531.1    577.1
  Track 1, 31-Mar-2030      519.5    737.7    899.5
  Track 2, 31-Mar-2030      668.0    937.3   1136.5
FV CAGR: 21.2% COMPOUNDER (Track 1 base; HYBRID 17.9% under Reading B)
  Static share: cash line 2.4% of FV today; no option value

HURDLE RATIO: prob-weighted 2.04 | base 2.30 | bull (base+5pp) 2.54 → PASS (feasibility; caps nothing)
  Track 1 multiples: 1.79 (below 1.953) | time-exact 3.487y threshold 2.177
EXPECTED CAGR (grade C 35/45/20): 19.3% Track 1 | 27.8% Track 2
PRICE DECOMPOSITION (Track 1): T1 80.2% | T2 20.0% | T3 2.2% | residual -2.4%
  (probabilities PROVISIONAL pending operator)
ENTRY: operator override ~Rs 350 (BINDING)
  mechanical (chunk 06, Year-3 FV) Rs 344.2 | 30% CAGR Rs 301.5 | MoS ref Rs 243.9
  deliberation today-value method Rs 371.4 (A27.1-consistent Rs 372.4)
UPSIDE/DOWNSIDE: Year 3 n.m. (all states above CMP) | headline 0.80x (partner exit Rs 313.8)
STRESS HEADLINES (low multiples): bear Rs 354.0 (-4.2%) | partner exit Rs 313.8 (-15.1%)
RECOGNITION GAP: OPEN on forward basis (market prices fee half 12.2-15.4x vs 18.62x)
  counter-reading: CLOSED on book (2.25x BVPS vs 1.10-1.21x theoretical)
POSTURE: VALUE-TRAP RISK (proof NOT FIRED + STRUCTURAL) | FTTCP +2 DEEP WATCH leaning AVOID
SIZE: FAST-GROWTH Y | A25 STARTER, Small ceiling binds | dispersion 51.5% (Medium cap)
MoS ROW: 30% (mixed evidence), expressed as size
EDGE: PROCESS
DECISION: WATCHLIST (on valuation: CMP 5.6% above the binding zone; posture VALUE-TRAP RISK)
```

**Key assumptions that move the valuation:**
- ▼ Return on AUM slides 15 bps a year (Reading B): Year-3 Track 1 FV -8.0%, label HYBRID, entry Rs 317.2.
- ▼ Pillar 2L at 0.80x (GNPA rising reading): partner Track 1 14.9x, today-value Rs 353.9.
- ▼ Partner exit: headline Rs 313.8.
- ▲ Partner-slice RoE read at the FY26 84.4%: Track 1 = cap 22.67x, today-value Rs 479.3.
- ▲ Partner share of PAT +1 pp: +Rs 5.3 per share at Track 1.
- ▲/▼ Book-base conflict: up to +Rs 10.8 per share at 0.8x if the higher Jun-26 book is right.

**Exit framework:**
- Target exit: Track 1 end-Year-3 value Rs 737.7 (31-Mar-2030).
- Thesis-broken: the T3 test reads DECLINING (Stage 2 > 4.11% or GNPA > 2.92% at Q2 FY27), or the
  proof gate fails for H2 FY27 with the off-book loss rate rising.
- Time stop: proof gate not fired by the FY27 results (31-May-2027).
- PE compression floor: whole-company Track 1 12.16x on forward EPS.

**One-line thesis:** "Buying KISSHT at or below ~Rs 350 because forward EPS grows from Rs 29.9 (FY28) to
Rs 57.8 (FY31) as AUM compounds from Rs 15,660 Cr to Rs 28,752 Cr at a held 4.57% return, valued as an
SOTP at Track 1 (own book 0.8x P/B; partner half 18.62x, RoE ~34%, Pillar 2L 1.00x, EM 18.5, caps 18x /
22.67x) = Rs 737.7 end-FY30 = 23.8% CAGR from Rs 350. FV CAGR 21.2% COMPOUNDER. Key risk: two-partner
concentration and the 228% parent guarantee behind a write-off-assisted GNPA. Cash quality: growth-induced."

Say: "Valuation complete. SOTP destination 18.62x to 22.67x on the partner half, 0.8x to 1.2x on the
own book. Hurdle Ratio PASS. Entry price: Rs 301.5 to Rs 344.2 mechanical; operator zone ~Rs 350
binding. Decision: WATCHLIST."

---

## INPUT DISCIPLINE: UNRESOLVED INPUTS USED (override 3)

1. INPUT UNRESOLVED: C.2 catalyst probabilities. Assumption used: rows 1 / 2 / 3 / D1 / D2 at 0.70 /
   0.60 / 0.20 / 0.70 / 0.15, because chunk 09 maps Section C bands (T1 FIRING → HIGH 0.60-0.90, less
   the grade-C discount; T2 DECLINING → HIGH for the downside) and chunk 17 gives the grade-C bull weight
   0.20. Both readings: operator ratifies them / operator sets other numbers (at all-base p = 1.0 the
   residual is -14.0%). Separating observation: the operator's C.2 ruling, confirm-by /finalize.
2. INPUT UNRESOLVED: treasury income on the Rs 208.05 Cr surplus cash. Assumption used: none stripped,
   because the operator PAT path is built on return on AUM with no treasury line. Both readings: no
   treasury income in the path / some treasury income in FY27-FY28 PAT (then EPS overstates and the HR
   Current PE understates). Separating observation: Q2 FY27 other-income line, confirm-by 30-Nov-2026.
3. INPUT UNRESOLVED: return on AUM beyond FY28. Assumption used: 4.571% held (Reading A), because T4
   STAGNANT is the sole forward RoA authority. Both readings: A held / B slides 15 bps a year. Separating
   observation: FY27 return on avg AUM vs 4.75%, confirm-by 31-May-2027.
4. INPUT UNRESOLVED: Mar-27 consolidated book (Rs 3,142.0 Cr vs Rs 3,424.0 Cr). Assumption used: the
   approved own book Rs 2,695.8 Cr, because the operator approved it. Both readings in Section 3.3.
   Separating observation: AR consolidated total equity at 31-Mar-2026, confirm-by /finalize.
5. INPUT UNRESOLVED: industry growth anchor for the fade. Assumption used: 20% (B10.tam_growth_pct),
   because it is the only market growth rate in B10. Both readings: 20% PL+LAP market / 46.9% digital-
   lender SAM growth (B10.sam_definition), which would hold the base nearer the bull. Separating
   observation: FY28 AUM growth vs 35%, confirm-by 31-May-2028.

## FLAGS (carried and new)

Carried from B10: FLAG-CASH (GROWTH INDUCED; lender, so the multiplier applied is Pillar 2L 1.00x, not a
cash multiplier), FLAG-CAPITAL-STRUCTURE, FLAG-ASSET-QUALITY, FLAG-CAPITAL-RAISE, FLAG-COST-OF-BORROWING,
FLAG-PROOF-GATE, FLAG-CREDENTIAL-GRADE, FLAG-EM-SCORE.

New this stage:
- FLAG-I5: priced under unmerged v3.11. Stage 11 sign-off and downstream presentation stay gated.
- FLAG-ENTRY-OVERRIDE-VS-MECHANICAL: override ~Rs 350 sits 1.7% above the chunk-06 mechanical Rs 344.2.
- FLAG-FV-LABEL-MARGIN: COMPOUNDER by 1.2 pp; flips to HYBRID under Reading B.
- FLAG-HURDLE-TRACK1: prob-weighted HR 1.79 on Track 1 multiples; PASS rests on the midpoint.
- FLAG-BOOK-BASE-CONFLICT: Rs 282.0 Cr gap between two Mar-27 book figures in B10.
- FLAG-PILLAR2L-READING: sequential GNPA rise meets the 0.80x criterion; operator ruled 1.00x.
- FLAG-DECOMP-PROBABILITIES-PROVISIONAL.
- FLAG-UGLINESS-TEXT: "STRUCTURAL-FEATURE" recorded with "artifacts" wording.
- FLAG-MACRO-STALE: August 2026 sheet past its 1-Sep-2026 refresh.
- FLAG-CONSUMED-BLOCKS-MISSING: Debt Capacity, FTTCP Part B, Market-Implied not in B10.

## OPEN ITEMS CARRIED TO B11

| # | Item | Owner | Blocks | Status after Stage 11 |
|---|---|---|---|---|
| I4 | Q2 FY27 business update (03-Oct-2026) not in corpus; BSE API Access Denied 04-Oct-2026 | operator: drop PDF into inputs/announcements/ | none; feeds ledger row 1 interim and the T3 test | OPEN |
| I5 | Section 1B v3.11 (Amendment 27) not merged to main | operator, separate framework PR | Stage 11 sign-off and downstream presentation | OPEN |
| DBB | Disbursement by book, on-book vs off-book, FY25 / FY26 / Q1 FY27 (IR question 1) | IR reply | the entry-override revisit; the 46/54 split; transfer pricing | OPEN |
| A19 | Amendment 19 FV CAGR and return-source label | Stage 11 | entry-zone presentation | **RESOLVED**: 21.2% COMPOUNDER (Track 1 base) |
| BOOK | Mar-27 book base conflict (Rs 282.0 Cr) | Claude Code extraction | none; sensitivity up to Rs 13.5/share | NEW, OPEN |
| C2P | Operator ratification of ledger probabilities | operator | price decomposition finality | NEW, OPEN |

---

```yaml
stage: B11-valuation
company: "KISSHT"
run_date: "2026-09-19"
model: "claude-opus-5-5"
status: complete
entity: "consolidated single-entity (OnEMI Technology Solutions Ltd incl. Si Creva Capital Services); SOTP slices own book and partner half are method outputs, not entities"
entity_count: 1
framework_state: "Priced under Section 1B v3.11 unmerged draft (open item I5)"
framework_versions: "Master v3.7 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9+v3.10+v3.11 (v3.11 unmerged, I5) / FTTCP v2.3"
input_gaps:
  - "Debt Capacity block: NOT FOUND in B10 (consumed, not recomputed)"
  - "FTTCP Part B Output Sheet B1-B8: NOT FOUND in B10 (B2 flag, B4 operating EPS, B7, B8 not available)"
  - "Market-Implied block: NOT FOUND in B10; flag PENDING (claude.ai)"
  - "C.2 operator probabilities: NOT FOUND in B10; Stage 11 provisional probabilities used"
  - "Treasury income on surplus cash Rs 208.05 Cr: NOT FOUND; not stripped"
  - "Tax rate and credit-cost base: NOT FOUND; asset-quality downside row D3 uncredited"
  - "Live peer table: PENDING LIVE PEER TABLE (Step 1C)"
  - "Revenue / total-income yield path: NOT PROJECTED (lender; valuation on AUM x return on AUM)"
  - "AUM 3-year historical CAGR: NOT FOUND (one-year +73% only)"
  - "Macro sheet stale: August 2026 stamp, next refresh 1-Sep-2026 passed"
flags:
  - {type: "FLAG-CASH", reason: "GROWTH INDUCED (operator); lender, so multiplier applied is Pillar 2L 1.00x, not a cash multiplier; cumulative CFO/PAT -2.46x by Ind AS 7"}
  - {type: "FLAG-I5", reason: "Priced under Section 1B v3.11 unmerged draft; Stage 11 sign-off and downstream presentation gated on merge"}
  - {type: "FLAG-ENTRY-OVERRIDE-VS-MECHANICAL", reason: "Operator override ~Rs 350 sits 1.7% above chunk-06 mechanical Rs 344.2 (Track 1 Year-3 FV / 1.25^3.487 + cash); deliberation today-value method gave Rs 371.4 (Rs 372.4 A27.1-consistent)"}
  - {type: "FLAG-FV-LABEL-MARGIN", reason: "FV CAGR 21.2% COMPOUNDER by 1.2 pp; Reading B (return on AUM -15 bps/yr) gives 17.9% HYBRID; separating observation FY27 return on avg AUM vs 4.75% by 31-May-2027"}
  - {type: "FLAG-HURDLE-TRACK1", reason: "Prob-weighted HR 2.04 PASS on midpoint destination; 1.79 on Track 1 multiples; time-exact threshold 2.177 over 3.487 years"}
  - {type: "FLAG-BOOK-BASE-CONFLICT", reason: "B10 carries Mar-27 consolidated book Rs 3,424.0 Cr (BVPS 164.3 route) vs Rs 3,142.0 Cr (SOTP roll); gap Rs 282.0 Cr = Rs 13.5/share; root at Jun-26 net worth"}
  - {type: "FLAG-PILLAR2L-READING", reason: "GNPA rose 2.12% to 2.25% sequentially, a 0.80x Stressed criterion; operator ruled 1.00x on YoY; at 0.80x partner Track 1 14.9x and today-value Rs 353.9; resolves at Q2 FY27 T3 test"}
  - {type: "FLAG-DECOMP-PROBABILITIES-PROVISIONAL", reason: "Ledger probabilities are Stage 11 proposals from chunk 09 bands and chunk 17 grade-C weights; operator ratifies at /finalize"}
  - {type: "FLAG-UGLINESS-TEXT", reason: "Classification recorded as STRUCTURAL-FEATURE with 'artifacts' wording; ARTIFACT reading gives RESEARCH / WATCH; neither is a trade before the proof gate"}
  - {type: "FLAG-MACRO-STALE", reason: "macro-sheet.md August 2026, next refresh 1-Sep-2026 passed at run date 04-Oct-2026"}
  - {type: "FLAG-CONSUMED-BLOCKS-MISSING", reason: "Debt Capacity, FTTCP Part B, Market-Implied blocks not in B10"}
  - {type: "FLAG-CAPITAL-STRUCTURE", reason: "carried from B10: parent guarantee 228% of parent net worth FY26"}
  - {type: "FLAG-ASSET-QUALITY", reason: "carried from B10: write-off-assisted GNPA; Q1 FY27 GNPA 2.25%"}
  - {type: "FLAG-CAPITAL-RAISE", reason: "carried from B10: Rs 832 Cr preferential, no numeric rationale, EGM 14-Oct-2026"}
  - {type: "FLAG-COST-OF-BORROWING", reason: "carried from B10: FCNR(B) tailwind contradicted by peers"}
  - {type: "FLAG-PROOF-GATE", reason: "carried from B10: NOT FIRED; H2 FY27 all-in loss test (< 10.5% of avg AUM)"}
  - {type: "FLAG-CREDENTIAL-GRADE", reason: "carried from B10: grade C at the C/B boundary"}
  - {type: "FLAG-EM-SCORE", reason: "carried from B10: EM 18.5 MODEST"}
pe_basis: "forward"
exit_pe_base_approved: "SOTP (A27.2), valuation date 31-Mar-2027: own book P/B 0.8/1.0/1.2x on Mar-27 book Rs 2,695.8 Cr; partner half P/E on FY28 PAT 18.62x (Track 1) / 20.6433x (midpoint) / 22.6667x (Track 2 at operator-set slice cap); cash Rs 208.05 Cr at face (A27.1); same basis at exit (A27.3)"
destination_pe:
  track1_rrm: {low: 17.0, mid: 18.62, high: 20.0, r_used: 15.5, rrm: 0.76}
  track2_additive: {low: 21.0, mid: 22.67, high: 22.67}
  sotp_range_approved: {low: 18.62, base: 20.64, high: 22.67}
  own_book_pb_approved: {low: 0.8, base: 1.0, high: 1.2}
  whole_company_crosscheck: {track1: 12.16, track2: 16.0, sector_cap: 18.0}
  divergence_pct: 17.9
  governing_track: "Track 1 (partner 18.62x with own book 0.8x): tracks diverge 17.9% > 15%; more conservative track sets the entry zone (section-1b chunk 06, OR-1)"
pillar_detail:
  slice_reported: "partner half (primary P/E slice)"
  roce_used: 34.0
  roce_base: 24.5
  roce_note: "RoE ex investment in Si Creva ~34% FY27 (operator); formula at 34.0% gives 24.3x; approved 24.5x implies 34.7%; FY26 actual 84.4% would give 30x"
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.00
  cash_multiplier_type: "Pillar 2L asset-quality, Sound (lender)"
  structural_or_growth: "GROWTH INDUCED"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: false
  ua_applied: false
  sector_cap_used: 22.67
  sector_cap_whole_company: 18.0
  converter_classification: "NON-CONVERTER"
hurdle_ratio: {base: 2.30, prob_weighted: 2.04, bull: 2.54, bull_used: false, track1_prob_weighted: 1.79, threshold: 1.953, verdict: "PASS", basis: "FORWARD; Current PE 19.70x = (369.55 - 9.98) / A21 EPS 18.25; prob-weighted EPS CAGR 39.9%; destination PE mid 14.67x (SOTP-implied at 31-Mar-2030); feasibility only, caps no verdict (OR-2)"}
run_rate_base:
  basis: "single-quarter-annualised"
  pat_run_rate_cr: 380.32
  eps_run_rate_rs: 18.25
  one_offs_adjusted: "none stripped; treasury income on IPO proceeds NOT FOUND; Rs 832 Cr raise not in Q1; no seasonal flag in B10"
  annual_model_divergence_pct: -13.8
  annual_model_divergence_note: "-13.8% vs FY27 base 441; -39.0% vs FY28 forward 623; approved FORWARD basis governs fair values, A21 base governs T1"
price_decomposition:
  denominator: "B10 market value post-raise Rs 7,555.1 Cr (Rs 362.50 per diluted share)"
  t1_confirmed: {rs_cr: 6061.4, rs_per_share: 290.83, pct_cmp: 80.2}
  t2_high_prob: {rs_cr: 1510.8, rs_per_share: 72.49, pct_cmp: 20.0}
  t3_speculative: {rs_cr: 162.9, rs_per_share: 7.82, pct_cmp: 2.2}
  residual: {rs_cr: -180.1, rs_per_share: -8.64, pct_cmp: -2.4}
  midpoint_crosscheck_pct: {t1: 92.4, t2: 22.3, t3: 2.4, residual: -17.2}
  step1c_peer_base_crosscheck: "PENDING LIVE PEER TABLE"
  governing_multiple: "pillar (approved SOTP Track 1: own book 0.8x P/B, partner 18.62x; effective 10.58x per Rs 1 Cr FY28 PAT increment)"
  probabilities_status: "PROVISIONAL, operator to ratify"
expectation_ledger: "runs/kissht-2026-09-19/outputs/expectation-ledger.md"
fair_values:
  basis_date_year3: "31-Mar-2030 (Mar-30 book, FY31 PAT)"
  track1: {bear: 519.5, base: 737.7, bull: 899.5}
  track2: {bear: 668.0, base: 937.3, bull: 1136.5}
  midpoint: {bear: 593.7, base: 837.5, bull: 1018.0}
  today_31mar2027:
    track1: {bear: 354.0, base: 414.0, bull: 451.7}
    midpoint: {bear: 405.9, base: 472.5, bull: 514.4}
    track2: {bear: 457.8, base: 531.1, bull: 577.1}
projection_extension:
  pat_base_cr: {fy27: 441, fy28: 623, fy29: 814.2, fy30: 1003.9, fy31: 1204.7, fy32: 1445.6}
  pat_bear_cr: {fy27: 400, fy28: 500, fy29: 580.3, fy30: 672.7, fy31: 778.9, fy32: 900.7}
  pat_bull_cr: {fy27: 470, fy28: 700, fy29: 949.8, fy30: 1218.6, fy31: 1523.3, fy32: 1904.1}
  aum_base_cr: {fy27: 11600, fy28: 15660, fy29: 19966.5, fy30: 23959.8, fy31: 28751.8, fy32: 34502.1}
  basis: "RUN-RATE (Q1 FY27 AUM pace) to FY27; A14 MODEST fade to 20% industry anchor (B10.tam_growth_pct) by FY30; return on avg AUM held 4.571% (Reading A, T4 STAGNANT)"
  split_own_partner: "46/54 kept; B10 evidences no other split (DBB open)"
  two_readings: "A: return on AUM held 4.571% / B: slides 15 bps a year; separating observation FY27 return on avg AUM vs 4.75% by 31-May-2027"
fv_path_track1_base: {today_31mar2027: 414.0, end_y1_31mar2028: 517.3, end_y2_31mar2029: 623.2, end_y3_31mar2030: 737.7}
fv_cagr: 21.2
fv_cagr_line: "FV CAGR over the hold: 21.2% (today Rs 414.0 to end-Year-3 Rs 737.7, governing Track 1, base case)"
return_source_label: "COMPOUNDER"
fv_cagr_sensitivity: {midpoint: 21.0, track2: 20.9, reading_b: 17.9, prob_weighted: 20.5, bear: 13.6, bull: 25.8}
decomposition_19_3: "2.4% of FV today (1.4% at exit) is the static A27.1 cash line; no option value; partner half 72.6% compounds at 24.6%/yr with FY28-FY31 PAT, own book 25.0% at 12.3%/yr via retained earnings; MODEST fade drags PAT growth 41.3% to 20.0%; no re-rating lever credited"
option_resolution_calendar: "none (no option slices); 18.6 dual display identical"
expected_cagr_prob_weighted: 19.3
expected_cagr_note: "Track 1, grade C 35/45/20, CMP to 31-Mar-2030 (3.487 years); Track 2 27.8%; midpoint 23.7%"
entry_zone:
  operator_override_rs: 350
  operator_override_status: "BINDING (deliberation override 5)"
  operator_override_reasoning: "book-value cross-check: SOTP base 2.88x Mar-27 book needs 12.4% perpetual growth at 17% RoE and 14% CoE (14.7% at 15.5%)"
  mechanical_chunk06_rs: 344.2
  mechanical_chunk06_basis: "Track 1 Year-3 operating FV Rs 727.76 / 1.25^3.487 + cash Rs 9.98 (A27.1)"
  mechanical_30pct_rs: 301.5
  mechanical_deliberation_today_value_rs: 371.4
  mechanical_deliberation_a27_1_consistent_rs: 372.4
  midpoint_chunk06_rs: 390.1
  reading_b_track1_rs: 317.2
  override_vs_mechanical_pct: 1.7
entry_range: {low: 301.5, high: 344.2}
mos_price: 243.9
mos_note: "reference only; FAST-GROWTH carve-out puts MoS in size (A25); 30% row, mixed evidence"
upside_downside_ratio: 0.8
upside_downside_note: "valuation-date headline: base Track 1 Rs 414.0 (+12.0%) vs partner-exit Rs 313.8 (-15.1%); Year-3 ratio n.m. (all Year-3 states above CMP)"
stress_headlines: {bear_low_rs: 354.0, partner_exit_low_rs: 313.8, bear_base_rs: 405.9, partner_exit_base_rs: 361.5, compound_bear_partner_exit_low_rs: 273.5}
recognition_gap:
  status: "OPEN on governing forward basis"
  current_forward_pe: 12.03
  sotp_implied_destination_pe: {track1: 13.5, midpoint: 15.5, track2: 17.4}
  market_implied_partner_pe: {own_0_8x: 15.4, own_1_0x: 13.8, own_1_2x: 12.2}
  counter_reading: "CLOSED on book: CMP 2.25x Mar-27 BVPS 164.3 vs theoretical 1.10-1.21x; implies 11.6% perpetual growth at 17% RoE"
  separating_observation: "FY27 PAT vs Rs 441 Cr and Mar-27 AUM vs Rs 11,600 Cr at Q4 FY27 results, confirm-by 31-May-2027"
transition_posture: "VALUE-TRAP RISK (proof gate NOT FIRED + STRUCTURAL-FEATURE); gap OPEN so AVOID overlay not engaged on forward basis"
size_state:
  fast_growth: true
  fast_growth_basis: "Q1 FY27 revenue +44.8% YoY, PAT +59.2% YoY"
  a25_state: "STARTER (Small, 2-3%)"
  ceiling: "Small (Part 2.6, operator)"
  dispersion_pct: 51.5
  dispersion_cap: "Medium"
  add_trigger: "none inside the Small ceiling; above it: ledger row 1 CONFIRMED and proof gate fired, plus operator ruling lifting the ceiling"
  trim_trigger: "25% per decayed ledger row; 50% if residual > 40% after a decay"
decision: "WATCHLIST (on valuation: CMP Rs 369.55 is 5.6% above the binding ~Rs 350 zone; posture VALUE-TRAP RISK; FTTCP +2 DEEP WATCH leaning AVOID)"
open_items:
  - {item_id: "I4", description: "Q2 FY27 business update (03-Oct-2026) not in corpus", owner: "operator", blocks: "none; feeds ledger row 1 interim and T3 test", status: "OPEN"}
  - {item_id: "I5", description: "Section 1B v3.11 (Amendment 27) not merged to main", owner: "operator, separate framework PR", blocks: "Stage 11 sign-off and downstream presentation", status: "OPEN"}
  - {item_id: "DBB", description: "Disbursement by book, on-book vs off-book, FY25/FY26/Q1 FY27", owner: "IR reply", blocks: "entry-override revisit; 46/54 split; transfer pricing", status: "OPEN"}
  - {item_id: "A19", description: "Amendment 19 FV CAGR and return-source label", owner: "Stage 11", blocks: "entry-zone presentation", status: "RESOLVED: 21.2% COMPOUNDER (Track 1 base)"}
  - {item_id: "BOOK", description: "Mar-27 consolidated book conflict Rs 3,424.0 Cr vs Rs 3,142.0 Cr", owner: "Claude Code extraction (AR consolidated total equity 31-Mar-2026)", blocks: "none; sensitivity up to Rs 13.5/share", status: "OPEN (new)"}
  - {item_id: "C2P", description: "Operator ratification of ledger probabilities", owner: "operator", blocks: "price decomposition finality", status: "OPEN (new)"}
unresolved_inputs_used:
  - {field: "C.2 probabilities", assumption: "rows 1/2/3/D1/D2 = 0.70/0.60/0.20/0.70/0.15", rule: "chunk 09 band mapping, chunk 17 grade-C bull weight", readings: "operator ratifies / operator resets (all base rows p=1.0 gives residual -14.0%)", separating_observation: "operator C.2 ruling at /finalize"}
  - {field: "treasury income on surplus cash", assumption: "none stripped", rule: "operator PAT path built on return on AUM", readings: "none in path / some in FY27-28 PAT", separating_observation: "Q2 FY27 other income, by 30-Nov-2026"}
  - {field: "return on AUM beyond FY28", assumption: "4.571% held", rule: "T4 STAGNANT sole RoA authority", readings: "A held / B -15 bps per year", separating_observation: "FY27 return on avg AUM vs 4.75%, by 31-May-2027"}
  - {field: "Mar-27 consolidated book", assumption: "approved own book Rs 2,695.8 Cr", rule: "operator-approved base binds", readings: "Rs 3,142.0 Cr / Rs 3,424.0 Cr", separating_observation: "AR consolidated total equity 31-Mar-2026"}
  - {field: "fade industry anchor", assumption: "20% (B10.tam_growth_pct)", rule: "A14 MODEST fade needs a named anchor", readings: "20% market / 46.9% digital-lender SAM", separating_observation: "FY28 AUM growth vs 35%, by 31-May-2028"}
som_cagr_crosscheck: "consistent (base AUM CAGR FY26-FY29 41.4% vs SOM-implied 61.4%)"
one_line_thesis: "Buying KISSHT at or below ~Rs 350 because forward EPS grows from Rs 29.9 (FY28) to Rs 57.8 (FY31) as AUM compounds at a held 4.57% return, valued as an SOTP at Track 1 (own book 0.8x P/B; partner half 18.62x) = Rs 737.7 end-FY30 = 23.8% CAGR from Rs 350; FV CAGR 21.2% COMPOUNDER; key risk two-partner concentration and the 228% parent guarantee behind write-off-assisted GNPA; cash quality growth-induced."
```
