# CLEANMAX — FTTCP v2.1 DRAFT (plain language, decided)

**Company:** Clean Max Enviro Energy Solutions Ltd
**Ticker:** CLEANMAX (NSE) / 544717 (BSE)
**CMP:** Rs 1,247 (manifest.yaml)
**Run date:** 2026-09-01
**Entity count:** 1 (single listed company; ~103-190 project SPVs are consolidated subsidiaries, web-handover §1)
**Workup:** FIRST-WORKUP. No prior Role 1. Role-1-derived fields (destination PE, prior thesis, prior DA) marked N/A.
**Concall mode:** NOT no-concall. Three transcripts exist (Mar-2026 Q3 FY26, May-2026 Q4 FY26, Aug-2026 Q1 FY27; extraction Block V). Concall Gate CLEARED.
**Framework exception:** Option A (operator-signed 2026-09-02). EV/EBITDA primary (NCI-adjusted), DCF of contracted PPA cash flows secondary, SOTP tertiary. PE is a Section 1B sanity cross-check only (companies/CLEANMAX.md §3; web-handover §6).

This draft runs FTTCP v2.1 Part A end to end on the signed Mental Model v5. It closes every call with the conservative rule, tags genuinely uncertain items, and names the single fact that would flip each one. No questions.

---

## 1. MY RULINGS

Each ruling is a statement, a confidence tag (sure / fairly sure / genuinely uncertain), and the single fact that disproves it.

### Setup rulings (4)

**R1. Forward window: 3 months primary, 6 months secondary, 12 months for the ROCE transition.**
CleanMax reports quarterly. The next print (Q2 FY27, late October 2026) confirms or refutes the P&L catalysts. Capital-cycle effects take 12 months.
Confidence: sure. Disproving fact: the company moves to half-yearly reporting.

**R2. Business type: standard operating business, NOT a lender. Run the standard four transitions (revenue, margin, cash conversion, ROCE).**
B04 business_type is "hybrid": a renewable IPP (RE Power Sales, 73.2% of revenue, ~87% of run-rate EBITDA) plus a project/services engine (RE Services, 26.0%) (B04). No AUM, NIM, or asset-quality metrics apply. The lender transition set is not used.
Confidence: sure. Disproving fact: the business reclassifies as a financing NBFC.

**R3. Workup intent: FIRST-WORKUP. No prior finalized run.**
companies/CLEANMAX.md is this run's own memory (spear seed plus Halt 1 sign-off), opened 2026-09-01, no prior Notion row. run_type is "full". No Role 1 exists yet; FTTCP precedes Role 1. Destination PE, prior thesis, and prior DA are N/A.
Confidence: sure. Disproving fact: a prior finalized CLEANMAX run folder surfaces.

**R4. Sector cap row: City Gas Distribution, 22x. The manifest "Pharma / CDMO" is a collector error and is overridden.**
No renewable-IPP or power-utility row exists in the Section 1B cap table (Master v3.6 cap table). City Gas Distribution (22x) is the nearest actual row: a capital-heavy, quasi-regulated infrastructure utility with contracted annuity cash flows and weak pricing power. That is the closest real match for a leveraged C&I renewable IPP on 23-year PPAs. The 22x is a ceiling, not a target; under Option A the PE track is a sanity cross-check only, and EV/EBITDA is primary (spear proposed a 12x EV/EBITDA cap, companies/CLEANMAX.md §3). Recorded for Phase 3 to inherit. Flag for the operator: add a dedicated Renewable-IPP / Power-utility row to the cap table, as with the open steel and sugar rows (LESSONS OPEN ACTIONS).
Confidence: fairly sure. Disproving fact: the operator rules a different infrastructure-utility row (for example a bespoke Renewable-IPP row) or confirms 12x EV/EBITDA governs and no PE cap is carried.

### Transition forward verdicts (4)

**R5. Revenue Growth forward verdict: FIRING (+2).**
Backward 3-year revenue CAGR FY23 to FY26 is 27.2% (screener Data_Sheet, cross-tied to filed per B01). The capacity pipeline is documented: 5.7-6.0 GW contracted, a 1.5 GW FY27 commissioning floor with about 33% delivered in Q1, a 4.6 GW opex base guided by 1-April-2027 (B05 guidance; extraction B4/H1). New-book tariff Rs 4.00/kWh sits above the Rs 3.57 commissioned in FY26, a mild tailwind (extraction C4).
Confidence: fairly sure. Disproving fact: FY27 commissioning tracks materially below the 1.5 GW floor, for example both Koppal bays slip past March 2027.

**R6. Margin Expansion forward verdict: STAGNANT (0).**
The RE Power Sales segment EBITDA margin is high and stable, 83% to 84%, at or near its own guided ceiling of 85-86% (B05 promise_delivery; extraction C1). The expansion to 86% is a management claim with partial delivery (83% to 84% so far), and it is offset by falling new-PPA tariffs (Rs 4.12 to Rs 3.57, FY24 to FY26), Bikaner curtailment (about Rs 170 Cr, extraction E4), and services-mix dilution. Margin is holding, not expanding. Round-down between a held-high margin and a mild decline lands on STAGNANT.
Confidence: fairly sure. Disproving fact: RE Power Sales segment EBITDA margin prints above 85% sustained while the blended margin holds.

**R7. Cash Conversion forward verdict: STAGNANT (0). Catalyst strength Moderate. Kernex cap does NOT engage.**
Net debt is still climbing toward the guided steady-state Rs 16,000 Cr, from Rs 11,809 Cr at 30-Jun-2026 (extraction F1; B05 guidance). Free cash flow is minus Rs 4,023 Cr FY26 and widening (extraction F5). So the cash transition toward self-funding is not firing forward. But documented cash catalysts exist: the Rs 599 Cr 11.50% NCD prepaid 2-April-2026 saving Rs 68.89 Cr a year (extraction F6), cost of debt falling 8.7% to 8.4% (B05), and CWIP seasoning. Catalyst is Moderate, not NONE, so the Kernex cap (DECLINING with catalyst NONE) does not engage.
Confidence: fairly sure. Disproving fact: the next cash-flow statement shows FCF turning toward positive without a capex cut, i.e. cash starts firing.

**R8. ROCE forward verdict: RECOVERING (+1), to a structurally-low plateau. Under strict round-down it is STAGNANT (0); the composite band is the same either way.**
Backward ROCE is STRUCTURALLY LOW (median 5.83%, FY26 about 4.2-5.1%, below the 15% asset-heavy threshold, sustained; B01, signed model 0.2). A young-fleet CWIP-bloat depression sits on top of that low base. Over 12 months the current Rs 5,339 Cr CWIP seasons into earning plant and lifts ROCE toward the guided 7-9% (signed model B3). That is a level-recovery driven by documented catalysts (CWIP conversion, NCD prepay, cost of debt), so RECOVERING fits the direction. The ceiling is about 8%, below the 13.5% minimum ROCE requirement, and fresh capex (1.5 GW a year) re-loads the denominator (the BOO treadmill), so it does not durably climb. The signed model itself reads "return on capital barely moves" (signed model 0.2), which argues STAGNANT under strict round-down.
Confidence: genuinely uncertain (RECOVERING vs STAGNANT). Disproving fact: FY27 ROCE prints flat or lower while the fleet grows, confirming the treadmill and forcing STAGNANT.

### The three named judgment calls

**R9. Proof gate: NOT FIRED.**
The signed gate is quarterly operating profit before other income at or above Rs 0, sustained two consecutive quarters (signed model B3). Status: FY25 (minus 62.4), FY26 (minus 33.6), Q1 FY27 (plus 51.6). Only ONE positive print exists; the gate needs two. The single print cannot be independently rebuilt (Q1 FY27 interest capitalisation is NOT DISCLOSED, extraction A1/A5), and the FY26 annual crossover reverses to minus Rs 207.72 Cr on a full borrowing-cost basis (extraction A5). The gate is one quarter short and contested.
Confidence: fairly sure. Disproving fact: Q2 FY27 operating PBT ex other income prints at or above Rs 0, making two consecutive and firing the gate.

**R10. Cash: DEFICIT is growth-induced; crossover QUALITY is INDETERMINATE.**
"If growth stopped tomorrow" test: capex stops, CFO of Rs 1,731 Cr FY26 (extraction F5) less maintenance capex swings FCF strongly positive; the operating fleet is an 83-84% margin annuity with 35-day receivables and customer advances. So the deficit is growth-induced, not structural. But whether the operating engine clears its own all-in interest is INDETERMINATE: the reported crossover leans on capitalised interest (28.43% of borrowing cost incurred vs 7.51% FY25), a mid-year useful-life extension (25 to 30 years), and an impairment-rate change, all landing in the IPO year (extraction A1/A2/A3). The full borrowing-cost rebuild flips FY26 to minus Rs 207.72 Cr (extraction A5). Per CLAUDE.md, INDETERMINATE cash caps the disposition at PROCEED WITH CAVEATS with the missing evidence named.
Confidence on growth-induced deficit: fairly sure. Confidence on crossover quality: genuinely uncertain (this is the INDETERMINATE finding). Missing evidence: consolidated construction-in-progress opening AND closing, FY25 and FY26 (operator ruled BLOCKING for Stage 11), plus the Q2 FY27 operating PBT ex-OI print.

**R11. ROCE: TEMPORARILY DEPRESSED component on a STRUCTURALLY LOW base, not a clean TEMPORARILY DEPRESSED.**
The framework's TEMPORARILY DEPRESSED needs a greater-than-500bps collapse in 12 months; ROCE moved 8% to 7% to 6% (about 200bps over two years; companies/CLEANMAX.md §4), so the collapse test does not fit. The base is STRUCTURALLY LOW (median 5.83%). The "if growth stopped tomorrow" test recovers about 2-3 points (5% toward 8%) as CWIP seasons, then stops at a structurally-low plateau below the cost of capital. So the depression is partly temporary and partly structural, and the recovered level is not a premium return.
Confidence: fairly sure. Disproving fact: audited pre-cycle filings show a durable mid-teens ROCE history, which would make the current level a true trough rather than the structural level.

### Composite and position

**R12. Composite score: +3 out of 8 (DEEP WATCH). Under strict round-down on ROCE it is +2 (DEEP WATCH leaning AVOID). Kernex cap not engaged. TRIM not engaged.**
Revenue +2, Margin 0, Cash 0, ROCE +1 = +3. No transition is forward DECLINING with catalyst NONE, so the Kernex cap does not engage. Not all four transitions are FIRING backward, so the TRIM rule does not engage. The Signal Gate passed (Role 5.5 tracker, 10 rows written, web-handover §7), so the zero-signal DEEP WATCH cap does not apply; the DEEP WATCH here is earned on the score itself.
Confidence: fairly sure. Disproving fact: Q2 FY27 fires the proof gate and moves cash and ROCE up a state each, lifting the composite into the BUY-candidate band.

**R13. Position: DEEP WATCH. No position. Overall disposition capped at PROCEED WITH CAVEATS by INDETERMINATE cash.**
Consistent with the signed model's analyst SHALLOW WATCH and the provisional entry zone Rs 470 to Rs 715 against CMP Rs 1,247 (signed model Part E). The transition posture is PRICED NARRATIVE (TRAP): proof NOT FIRED, ugliness ARTIFACT-OF-CLIMB, recognition gap resolved against at CMP (signed model B4). The call turns on one print.
Confidence: fairly sure. Disproving fact: price falls into the Rs 470-715 zone on the supply overhang while Q2 FY27 fires the gate, re-opening the recognition gap.

---

## 2. THE FOUR TRANSITIONS

Actuals FY22-FY26 are anchored. FY27-FY31 are EXPECTED and illustrative, built from guidance and catalysts, not projected as fact.

### 2.1 Revenue Growth — forward FIRING

Consolidated revenue, Rs Cr (screener Data_Sheet, cross-tied to filed accounts per B01 data_notes; FY23 also RHP restated Rs 929.58 Cr, extraction I1):

| Year | Revenue (Rs Cr) | YoY | Basis |
|---|---|---|---|
| FY22 ACTUAL | 701.73 | — | screener Data_Sheet |
| FY23 ACTUAL | 929.58 | +32.5% | screener; RHP restated |
| FY24 ACTUAL | 1,389.84 | +49.5% | screener; RHP restated |
| FY25 ACTUAL | 1,495.70 | +7.6% | screener; AR consol |
| FY26 ACTUAL | 1,912.87 | +27.9% | screener; AR consol (extraction B2) |
| FY27 EXPECTED (illustrative) | ~2,600-2,800 | ~+40% | 1.5 GW FY27 floor, ~33% delivered Q1 (B05) |
| FY28 EXPECTED (illustrative) | ~3,700-4,000 | ~+40% | 4.6 GW base, signed model 0.4 |
| FY29-FY31 EXPECTED (illustrative) | fades toward industry | fading | EM STRENGTHENING, fade by Year 4 (v3.6 Amendment 14; B07) |

Plain line: revenue is firing and the pipeline is contracted, not narrated. The one caveat is that headline growth is inflated by lumpy RE Services (7.3x swing in Q1 FY27, order book 215 MW to 147 MW; B05); RE Power Sales alone grew 47% in Q1 (signed model C2), still well above the 20% FIRING bar.

### 2.2 Margin Expansion — forward STAGNANT

RE Power Sales segment EBITDA margin (annuity engine) and blended margin:

| Year | Power Sales segment EBITDA margin | Blended read | Basis |
|---|---|---|---|
| FY24 ACTUAL | ~77% (667/866) | operating margin ~51% | extraction C1 |
| FY25 ACTUAL | ~86% (955/1,107) | operating margin ~60% | extraction C1 |
| FY26 ACTUAL | ~88% (1,232/1,399) | operating margin ~59% | extraction C1 |
| Q1 FY27 ACTUAL | ~87% (460/528) | blended fell 66% to 51% on services mix | extraction C1; signed model C2 |
| FY27-FY28 EXPECTED (illustrative) | guided toward 85-86% | mix-dependent | B05 promise_delivery (partial) |

Plain line: the annuity margin is high and holding, not expanding. The guided climb to 86% is a claim with partial delivery, offset by falling new-PPA tariffs, Bikaner curtailment, and services dilution. Margin is not the firing transition here.

### 2.3 Cash Conversion — forward STAGNANT (growth-induced deficit, INDETERMINATE crossover quality)

Consolidated, Rs Cr (extraction F5; B01; companies/CLEANMAX.md §4):

| Year | CFO | Capex | FCF | Net debt | Debtor days |
|---|---|---|---|---|---|
| FY24 ACTUAL | 86 | 1,866 | (1,780) | ~5,570 borrowings | 55 |
| FY25 ACTUAL | 1,404 | 2,911 | (1,506) | ~8,087 borrowings | 54 |
| FY26 ACTUAL | 1,731 | 5,754 | (4,023) | 12,684 borrowings / 11,209 net debt | 42 |
| Q1 FY27 ACTUAL | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | 11,809 net debt (mgmt) | 35 |
| FY27-FY28 EXPECTED (illustrative) | rising with fleet | heavy build continues | stays negative | toward Rs 16,000 guided | stable/low |

Plain line: the deficit is growth-induced (capex outran a scaling operating cash base; debtor days compressed 55 to 35). If growth stopped, FCF would swing positive. But net debt still climbs to the guided Rs 16,000 Cr, so the cash transition is not firing forward. The crossover quality is INDETERMINATE pending the BLOCKING CWIP number; reverse factoring of Rs 1,730.92 Cr (up 4.1x, routed through investing / non-cash; extraction F2) and current liabilities exceeding current assets by Rs 1,724 Cr (gate-recommendation FLAG-CASH) sit inside that indeterminacy.

### 2.4 ROCE / Capital Efficiency — forward RECOVERING (to a low plateau)

ROCE, consolidated (companies/CLEANMAX.md §4; B01 median 5.83%; signed model 0.2):

| Year | ROCE | Note |
|---|---|---|
| FY22 ACTUAL | NOT FOUND (capital-employed split pre-RHP NOT FOUND, B01) | — |
| FY23 ACTUAL | NOT FOUND | loss year (PAT minus 65.3 Cr, screener) |
| FY24 ACTUAL | ~8% | companies/CLEANMAX.md §4 |
| FY25 ACTUAL | ~7% | companies/CLEANMAX.md §4 |
| FY26 ACTUAL | ~4.2-6% (median window 5.83%) | signed model 0.2; B01 |
| FY27-FY28 EXPECTED (illustrative) | recovers toward 7-9% | guided FY28 state, signed model 0.2/B1 |
| FY29-FY31 EXPECTED (illustrative) | range-bound ~7-9% | BOO treadmill re-loads denominator |

Plain line: ROCE recovers in level as the Rs 5,339 Cr CWIP seasons, but to a structurally-low ~8% plateau below the 13.5% cost-of-capital bar. This is a level-recovery, not a climb up the quality ladder (R1 to R1+, not R1 to R3). The "if growth stopped tomorrow" test recovers 2-3 points then stops.

---

## 3. THE CATALYST STORY (plain words)

**Revenue fires on volume.** 5.7-6.0 GW contracted, a 1.5 GW FY27 floor (33% delivered), 4.6 GW by April 2027, Data and AI at 42% of contracted capacity (extraction I2). Evidence is documented (contracted book, exchange-filed guidance). Confirm: FY27 commissioning tracks the 1.5 GW pace. Kill: Koppal bays slip past March 2027, or the unnamed ~800 MW central-grid pipeline lands in the impaired Rajasthan corridor (signed model B6c; extraction E6).

**Margin does not fire; it holds.** The annuity margin is already near its 86% ceiling. The expansion catalyst is a claim, netted against tariff erosion (Rs 4.12 to Rs 3.57) and curtailment. Confirm: Power Sales margin above 85% sustained. Kill: services mix or curtailment drags the blend down.

**Cash has real micro-catalysts but no firing transition.** NCD prepay saves Rs 68.89 Cr a year (documented, done); cost of debt falls; CWIP seasons. But net debt still climbs to Rs 16,000 Cr, so cash conversion stays stagnant. Confirm: FCF turns toward positive without a capex cut. Kill: reverse factoring keeps flattering operating cash while the current-liability shortfall hardens into an auditor Emphasis of Matter (signed model C3a).

**ROCE recovers in level on CWIP seasoning.** The single Rs 5,339 Cr construction block converting to earning plant lifts ROCE toward 7-9%. Confirm: FY27 ROCE prints above FY26 while the fleet grows. Kill: fresh capex re-loads the denominator faster than old CWIP seasons, and ROCE stays flat (the treadmill).

**The one event the whole story hangs on: Q2 FY27 operating profit before other income, late October 2026.** A second positive print fires the proof gate, confirms the crossover, and lifts both cash and ROCE reads. A negative print falsifies the transition (signed model B6a; companies/CLEANMAX.md §8).

---

## 4. THE VERDICT

Composite FTTCP score is +3 out of 8, which lands DEEP WATCH; under strict round-down on the ROCE call it is +2, DEEP WATCH leaning AVOID, so the band holds either way. Neither the Kernex cap nor the TRIM rule engages: no transition is forward DECLINING with catalyst NONE, and the four transitions are not all FIRING backward. The overall disposition caps at PROCEED WITH CAVEATS because cash-conversion crossover quality is INDETERMINATE, with the missing evidence named (consolidated CWIP opening and closing FY25-FY26, and the Q2 FY27 operating PBT ex other income print). The call turns on that Q2 FY27 print, due late October 2026: two consecutive positive quarters fire the proof gate and re-open the case; a negative print falsifies the transition.

---

## 5. THE P/E BASE CARD (single entity)

Under Option A, EV/EBITDA is primary and the PE tracks are a sanity cross-check only. The card is computed per Section 1B and is PROVISIONAL on two inputs marked below. CONVERTER classification: NON-CONVERTER (contracted-annuity IPP; no traded-commodity input spread; 83-84% margin does not co-move with an input price; v3.7 Amendment 17.0). So converter smoothing does not apply.

| Input | CLAUDE CODE DRAFT | DOSSIER §6 PRE-RULING | Anchor |
|---|---|---|---|
| Pillar 1 ROCE forward verdict | RECOVERING (to ~8% plateau) | no pre-ruling; Code drafts | R8; FTTCP Pillar 1 table |
| Pillar 1 normalization route | A-Operational (CWIP > 20% of CE) | no pre-ruling | v3.5.1 route rule |
| ROCE fed to Pillar 1 | operational/mid-cycle ~8% PROVISIONAL (statutory ~5.83%; operational lift pending BLOCKING CWIP) | no pre-ruling | v3.5.1 Route A; B01 |
| Pillar 1 base PE | ~11.5x on ~8% ROCE (0.5x8+7.5); ~10.4x on 5.83% | no pre-ruling | v3.3 Amendment 5; v3.6 Amendment 11 (floor 9x, cap 30x) |
| Pillar 2 cash multiplier | INDETERMINATE, leaning growth-induced (not the 0.65x structural penalty) | growth-induced deficit, INDETERMINATE crossover, caps at PROCEED WITH CAVEATS | R10; web-handover §6; gate-recommendation |
| Pillar 3 growth / moat premium | +0x | no pre-ruling | v3.6 Amendment 16: projected ROCE (7-9%) never crosses 13.5% min ROCE, so B2 reads growth-premium eligible NO; zeroes 3a/3b/3c |
| Strategic premium | +0x; ROCE recovery credited via Pillar 1 (single-credit); BOO treadmill re-rating optionality 0x | no pre-ruling | v3.3 Amendment 4; FTTCP Pillar 1 Integration |
| Undiscovered Alpha | NOT APPLIED (listed ~7 months < 12; FII+DII > 3% after FII 29.8% to 11.21%) | no pre-ruling | v3.3 Amendment 3 qualifiers; companies/CLEANMAX.md §9 |
| Sector cap | City Gas Distribution 22x (nearest actual infra-utility row) | Code drafts; operator rules | R4; Master v3.6 cap table |
| DESTINATION PE — additive track | ~10-11x = [Pillar 1 ~11.5x x cash mult ~0.95] + 0 + 0; min(~11, 22 cap); UA not applied; ±7.5% ~10-12x | — | v3.3 Amendment 3 ordering |
| DESTINATION PE — RRM track | ~9x = base ~11.5x x RRM ~0.79 (r ~15-15.5%: base 14% + complexity +0.5 for ~103 SPVs/dense RPT + governance +0.5-1.0; no cyclical surcharge; no cash r-UP per Amendment 12A; no short-record r-UP per Amendment 12C), floored 9x | — | Master v3.6 RRM; v3.6 Amendments 12/13 |

Both PE tracks land ~9-11x, far below the CMP-implied ~27-37x guided FY28 earnings and ~94x trailing (companies/CLEANMAX.md §3). This confirms PRICED NARRATIVE on the PE sanity track. Under Option A the primary read is EV/EBITDA (~10-12x pillar-consistent; spear proposed a 12x cap).

**THE EARNINGS-BASIS QUESTION (operator decides; I do not pick).** Trailing EPS (~Rs 8 FY26) is mechanically depressed by young-fleet interest and depreciation timing and the NCI wedge (B04 irrelevant_ratios), so a trailing PE reads ~156x and is not usable. Forward FY28 EPS (~Rs 34-47, signed model 0.4) gives ~27-37x but relies on the un-reconciled FY28 guidance (EBITDA basis and other-income treatment NOT DISCLOSED; extraction B4) and the INDETERMINATE crossover. A forward basis better fits a young-fleet IPP; a trailing basis is cleaner evidence but understates a genuine seasoning. Amendment 18.1 requires the SAME basis at entry and exit. The operator chooses at the gate.

**Card provisional on:** (1) consolidated CWIP opening AND closing, FY25 and FY26 — BLOCKING for the Route A operational ROCE and the Pillar 2 cash determination (NOT FOUND in corpus; signed model Part F item 10); (2) Q2 FY27 operating PBT ex other income (not yet printed). Until both land, the destination PE and the cash multiplier are provisional.

---

## 6. STEP 3 SCORECARD

| Transition | Backward Verdict | Catalyst Strength | Forward Probability | Forward Verdict | Score |
|---|---|---|---|---|---|
| Revenue Growth | FIRING (3yr CAGR 27.2%) | Strong (documented pipeline) | 3-6m: >60% | FIRING | +2 |
| Margin Expansion | SUSTAINED (segment 83-84%, high/stable) | Weak-Moderate (claim, tariff offset) | 3-6m: ~30-40% | STAGNANT | 0 |
| Cash Conversion | DETERIORATING (FCF widening; CFO/PAT distorted) | Moderate (NCD prepay, cost of debt, seasoning) | 3-6m: ~30% | STAGNANT | 0 |
| ROCE / Capital Efficiency | STRUCTURALLY LOW + temporary CWIP bloat | Moderate (seasoning) vs BOO treadmill | 12m: ~40-50% | RECOVERING | +1 |
| | | | | **COMPOSITE** | **+3 / 8** |

Kernex cap: NOT engaged (no transition DECLINING with catalyst NONE). TRIM rule: NOT engaged (not all four FIRING backward). Signal Gate: PASSED (10 tracker rows, web-handover §7). Band: DEEP WATCH (+3); DEEP WATCH leaning AVOID if ROCE rounds to STAGNANT (+2).

---

## 7. STEP 5 MONITORING TRIGGERS (90-180 days)

| # | Trigger | Threshold | Horizon | What it changes in FTTCP |
|---|---|---|---|---|
| 1 | Q2 FY27 operating PBT ex other income | at or above Rs 0 (two consecutive with Q1) | late Oct 2026 | Fires the proof gate; lifts Cash and ROCE a state each; re-run FTTCP |
| 2 | Consolidated CWIP opening AND closing, FY25-FY26 (BLOCKING) | disclosed | next AR / Stage 11 | Resolves INDETERMINATE cash and the Route A operational ROCE |
| 3 | Interest capitalisation ratio | reverts toward 7-10% (FY25 norm) vs 28.4% | FY27 Notes 3/36 | Staying near 28-30% confirms the accounting-lift concern; caps crossover quality |
| 4 | FY27 capacity commissioned | tracking 1.5 GW floor; 4.6 GW by Apr-2027 | quarterly | Below pace weakens Revenue FIRING toward STARTING |
| 5 | RE Power Sales EBITDA/MW (nameplate) | at or above Rs 55 lakh vs Rs 56.0 Q1 FY27 | quarterly | Below Rs 50 lakh with fleet growing falsifies the engine (signed model B6f) |
| 6 | Bikaner curtailment / Koppal spread | firm PGCIL date that holds; no Koppal CTU curtailment | quarterly / Dec 2026 | Spread to Koppal moves Revenue and Margin down |
| 7 | Net debt vs guided Rs 16,000 Cr; CARE opening ND/EBITDA vs 5.5x trigger | on or below trajectory; not breaching 5.5x sustained | semi-annual | Breach moves Cash toward DECLINING |
| 8 | Storage / firmed round-the-clock PPA share | first signed firmed data-centre PPA disclosed | 2 quarters | Converts the product-shape gap; supports Revenue durability (signed model B6d) |
| 9 | NCI share of profit | turns positive vs minus Rs 8.56 Cr FY26 | annual (Jun 2027) | Confirms per-share economics; supports ROCE recovery quality |
| 10 | Catalyst-absence check | no reconciled EBITDA definition AND no CWIP disclosure in next results | Q2 FY27 | INDETERMINATE cash persists; disposition stays PROCEED WITH CAVEATS |
| 11 | Promoter pledge / supply overhang | no increase past 20.02%; 360 One cover above ~2.25x trigger | weekly to Dec | Governance tripwire; not a transition score but a kill risk (signed model C3) |

---

## 8. PILLAR 1 HANDOFF / HANDOFF-TO-VALUATION BLOCK

- **ROCE forward verdict:** RECOVERING (level-recovery to a structurally-low ~8% plateau; STAGNANT under strict round-down).
- **Implied Pillar 1 ROCE:** operational / mid-cycle ~8% via Route A (Operational ROCE; CWIP > 20% of capital employed), PROVISIONAL on the BLOCKING consolidated CWIP number; statutory anchor 5.83%. Base PE ~10.4-11.5x (0.5 x ROCE + 7.5; v3.6 Amendment 11 cap 30x, floor 9x). CONVERTER classification: NON-CONVERTER.
- **ROCE recovery credited via:** Pillar 1 (single-credit; Strategic Premium barred; BOO treadmill re-rating optionality 0x).
- **Credit route:** A-Operational (denominator fix). Route B (pre-cycle) condition is NOT present (no evidenced pre-depression mid-teens ROCE history; median 5.83%).
- **Growth-premium eligibility (Module B2):** NO. Projected ROCE (7-9%) never crosses the 13.5% minimum ROCE requirement, so Pillar 3 pays +0x (v3.6 Amendment 16). This is the load-bearing Section 1B finding: a large, long-duration, documented growth machine that earns zero growth premium because it grows below its cost of capital.
- **Cash multiplier (Pillar 2):** INDETERMINATE, leaning growth-induced. Do not apply the 0.65x structural penalty; do not credit clean growth-induced either, until the BLOCKING CWIP number and Q2 FY27 print land. Caps the disposition at PROCEED WITH CAVEATS.
- **Sector cap row Phase 3 must use:** City Gas Distribution 22x (nearest actual infrastructure-utility row; no renewable-IPP row exists — flag to add one). PE track is a sanity cross-check only under Option A; EV/EBITDA primary (spear 12x). Step 1C (v3.9 Amendment 20) relative peer table is PENDING LIVE PEER TABLE (Claude web supplies; Code cannot).
- **Fade horizon:** EM STRENGTHENING (B07), so growth fades by Year 4 (v3.6 Amendment 14); projection runs to Year 4/5 (v3.8 Amendment 18.0).
- **SHARED CATALYST flag:** the CWIP-seasoning catalyst drives BOTH the Pillar 1 forward ROCE (Route A denominator normalization) AND the Revenue/EBITDA growth. If commissioning or seasoning slips, the ROCE recovery and the revenue firing miss together. Role 3 must stress-test this single point of failure, and the one-year-slip exit (v3.8 Amendment 18.7) on the Q2 FY27 gate.

---

*FTTCP v2.1 Part A draft. Part B (Financial Normalization Engine, B1-B8) not run here; Stage 11 consumes B2 (growth-premium NO) and the Pillar 1 handoff above. Every number carries its source; NOT FOUND is the only fill for a missing number. Card provisional on the BLOCKING CWIP input and the Q2 FY27 print.*
