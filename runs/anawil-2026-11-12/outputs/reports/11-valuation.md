# STAGE 11: ROLE 1 DUAL-TRACK VALUATION, ANAWIL (Anawil Wire and Engineering Ltd, NSE SME Emerge)

- Run folder: runs/anawil-2026-11-12. Run date 2026-11-12. Phase 3 valuation written 2026-11-17.
- Model: claude-opus-5-5, effort xhigh (.claude/agents/stage-11-valuation.md frontmatter).
- Framework: Master v3.7 Role 1 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9+v3.10 (section-1b skill) / FTTCP v2.3.
- Entity count 1 (B10.entity_count; handover dossier Section 1). One valuation pass. The per-entity refusal does not trigger.
- Authority: the operator-signed deliberation (outputs/final/fttcp-deliberation.md, SIGNED OFF 2026-11-17) carried on B10. The operator-approved exit PE base and earnings basis govern. Where my own derivation differs, I report the difference and value on the approved base.
- Units: Rs Cr unless stated. B10 already converted lakh to Rs Cr. I do not convert again. Per-tower figures are in Rs lakh where marked.

Source key: H1R = H1 FY27 results filing 2026-11-06 (page-marked txt, inputs/results); PR = press release 2026-11-06; Pres = H1 FY27 deck 2026-11-08; Pros = Prospectus 2026-08-06; CRISIL = rating rationale 2026-08-19; HD = web handover dossier 15-Nov-2026 (inputs/research); DLB = deliberation record; FD = fttcp-draft.md (commit 4ef5e669); B03 to B10 = stage blocks; RL = run-log.md.

---

## SECTION 0: PRICE, INPUTS AND CONSUMED BLOCKS

### 0.1 Live price (Ruling 6)

Stage 11 has Read, Write and Grep only. It cannot fetch a live price. The orchestrator fetched it and passed it by message.

| Item | Value | Anchor |
|---|---|---|
| CMP used | Rs 381.0 | screener.in/company/ANAWIL/ read 2026-11-17 02:45 IST, last close (RL line 22, Phase 3 entry) |
| Market cap at CMP | Rs 952.49 Cr = 381 x 2,49,99,800 shares (screener prints Rs 952 Cr) | RL line 22; shares B10.identity (H1R p.4 paid-up 2,499.98 lakh / Rs 10) |
| 52-week high / low | Rs 540 / Rs 313 | RL line 22 |
| Screener stock P/E | 19.5x | RL line 22 |
| B10 CMP (shown beside) | Rs 391.0, market cap Rs 977.0 Cr, 12-Nov-2026 close | B10.identity.cmp_rs (manifest) |
| Earlier read | Rs 413, 30-Oct-2026 [SECONDARY] | DLB Ruling 6 |
| Net debt 30-Sep-2026 | Rs 33.41 Cr (includes CMD loan Rs 21.68 Cr) | B10.identity.net_debt_cr (H1R p.7) |
| EV at CMP | Rs 985.90 Cr = 952.49 + 33.41 | arithmetic |

All per-share and percent-of-CMP figures below use Rs 381 and Rs 952.49 Cr. At the B10 price of Rs 391 every percent-of-CMP figure is 2.6% smaller.

### 0.2 Input data (Master Role 1 table; B10 anchors)

| Data point | Value | Anchor |
|---|---|---|
| Business | Onshore wind tubular steel towers, build-to-spec; three contract lines (Model 1 conversion 21.2%, Model 2 conversion plus internals 10.8%, Model 3 integrated supply 64.3% of H1 FY27 revenue) | B10.identity; HD 2.2 |
| Revenue FY26 / H1 FY27 / TTM | 143.27 / 153.97 / 255.86 | B10.latest_financials (H1R p.4) |
| EBITDA FY26 / H1 FY27 / TTM | 61.23 / 36.08 / 87.17 (PBT + finance + depreciation - other income) | B10 (H1R p.4) |
| PAT FY26 / H1 FY27 / TTM | 35.95 / 14.39 / 48.09 | B10 (H1R p.4) |
| EPS FY26 / TTM | Rs 18.78 (weighted pre-IPO shares) / Rs 19.24 | B10 (H1R p.4) |
| CFO FY26 | 12.47 audited / 18.44 restated | B10 (H1R p.8; Pros p.174) |
| FCF FY26 / H1 FY27 | -80.54 / -25.11 | B10 (H1R p.8) |
| BVPS 30-Sep-2026 | Rs 90.54 (net worth 226.35) | B10 (H1R p.7) |
| EBITDA margin FY26 / H1 FY27 | 42.7% / 23.4% (steel enters revenue in Model 3) | B10 |
| ROCE FY24 / FY25 / FY26 / TTM | 16.39% / 26.25% / 26.79% (26.72% audited basis) / 26.87% | B10.roce_2yr_trend, roce_latest_pct |
| ROE FY26 | 40.16% on closing net worth | B10 (H1R p.4, p.7) |
| 3-yr revenue / PAT CAGR | 77.1% / 91.9% (FY23 ramp base) | B10 |
| CFO/PAT FY26 / cumulative | 0.35 audited, 0.50 restated / 0.48 audited, 0.58 restated | B10 |
| Capex FY26 / D&A FY26 | 93.01 / 11.30 | B10 (H1R p.8, p.4) |
| DPS | 0 | B10 (H1R p.8) |
| Guidance FY27 | Revenue Rs 450-500 Cr, PAT Rs 55-60 Cr; not the base (grade C) | B10.from_earlier_analysis (PR p.2-3) |
| Guided margin band | NOT FOUND as a number | B10 |
| Role 5 grade | C (Mixed) | B10.credibility_grade |
| FTTCP ROCE forward verdict | FIRING (+2), operator Ruling 2 | B10.roce_forward_verdict |
| FTTCP composite | 4 of 8, DEEP WATCH leaning BUY-ON-DIPS | B10.phase2_deliberation |
| Emerging Moat | 10.8, NONE | B10 (B07) |
| Evidence mix | mixed (13 documented, 6 claim, 6 inference) | B10 (B07) |
| Cash determination | INDETERMINATE (Ruling 5) | B10.cash_determination |
| Rating | CRISIL BBB/Stable, A3+; GCA 292 days at 31-Mar-2026 | B10.rating (CRISIL p.1-2) |
| Strategic asset | No | B10 |
| Peer medians | PENDING LIVE PEER TABLE | B10.unresolved |
| SOM-implied revenue CAGR | yr3 49.3%, yr5 35.1% | B10 (B09) |

### 0.3 Consumed blocks (consumption clause)

| Block | Status | Use here |
|---|---|---|
| FTTCP Part A verdicts | Present: deliberation (Rulings 2, 5) on FD Part A | Pillar 1 selection; disposition cap |
| FTTCP C.2 table | Present: FD 3.5 = B10.expectation_ledger; three downside rows, so it passes the rejection rule (section-1b chunk 09) | T2/T3 credit, ledger |
| FTTCP Part B Output Sheet | Present: FD Part B (B1 to B8) | B1 funding, B2 gate, B4 operating EPS, B7 net debt, B8 |
| Debt Capacity Assessment block | NOT FOUND (FD B1 says not in the dossier) | Gap named. B7 Year 3 net debt NOT FOUND, so net debt is held at the anchor (section-1b chunk 13) |
| Market-Implied Assumptions block | NOT FOUND (not run in claude.ai) | Gap named. Section 1B.12 resolves the recognition gap from the PE gap and shows the implied-growth arithmetic as my own destination-PE work (section-1b chunk 14) |

### 0.4 Single-credit map, verified before valuing (section-1b chunk 04)

| Item | Credited in | Check |
|---|---|---|
| ROCE recovery | Pillar 1 only (FIRING verdict, operator midpoint method) | Strategic premium 0; r carries no ROCE credit. Holds |
| Capital-cycle normalisation | NONE (Route A 19.1% at 31-Mar-2026, under 20%) | FD R17. Holds |
| Capital-base distortion / depressed base year | B6 not applicable; B3 not applicable | Holds |
| Converter through-cycle ROCE | Inside the 23.45% blend only | Holds |
| Cash quality | Pillar 2 only (1.00x); no r adjustment (12A) | Holds |
| Short record | Unproven durability band; no r surcharge (12C) | Holds |
| Complexity (Darpan) | r +0.5 only (A13) | Holds |
| Kutch profit | Option slice only (p 0.4). Not in base earnings, not in the Pillar 1 number (19.76% excludes it) | Holds. Kutch also supports the FIRING label and, in the operator's words, the Pillar 3 capacity test: SHARED CATALYST |
| Order book | Base-case revenue (FY27, Q1 FY28) and the Pillar 3a order-book qualifier | SHARED CATALYST 2. Split stated in 2C-w; touches Track 2 only |
| JSW pull | T3 slice only (p 0.4). Base FY27 is the JSW-lag reading | Holds; no double count with Ruling 1's 45-57 range |

Interim line: Section 0 complete. CMP Rs 381 (17-Nov-2026), market cap Rs 952.49 Cr. Two consumed blocks NOT FOUND (Debt Capacity, Market-Implied), gaps named.

---

## SECTION 1A: METHOD SELECTION

### Method Suitability Matrix

**Earnings-based**

| Method | Works best | Fails | Suitable here? | Weight |
|---|---|---|---|---|
| P/E | Profitable, clean earnings, low leverage | Cycle peaks, one-offs, high leverage | YES, primary. Profitable; net debt Rs 33.41 Cr after the IPO repaid Rs 115 Cr (HD 2.4). Caveats: cash conversion INDETERMINATE and the margin percent is mix-driven, so the multiple runs on PAT built from towers x EBITDA per tower. The Section 1B destination governs | 70% |
| PEG | Predictable 2-3 year growth | Sharp deceleration, tiny base | NO. FY27 revenue rises about 167% on a ramp base, then FY28 runs flat on the book. Growth is lumpy, not predictable | 0% |

**Enterprise value**

| Method | Works best | Fails | Suitable here? | Weight |
|---|---|---|---|---|
| EV/EBITDA | Capital-intensive manufacturing | Capex far above depreciation | YES, secondary. Capital structure neutral and before the depreciation step-up. Capex Rs 93.01 Cr against D&A Rs 11.30 Cr in FY26 (B10), so the multiple sits at the 0.6x end of the 0.6-0.7x PE rule | 30% |
| EV/Sales | Early-stage, unprofitable | Commodity pass-through revenue | NO. Model 3 puts steel into revenue; revenue per tower runs Rs 0.59 Cr to Rs 3.5 Cr by contract line (HD 2.1) | 0% |
| EV/Gross Profit | Pass-through platforms | Most businesses | NO | 0% |
| EV/Capacity | Capacity-driven businesses | Asset-light | CONCEPTUALLY YES, but it needs a live peer EV-per-capacity table. No listed tubular tower peer exists (B06). PENDING LIVE PEER TABLE. Information only: EV Rs 985.90 Cr / 612 towers nameplate = Rs 1.61 Cr per tower of capacity | 0% |

**Asset-based**

| Method | Works best | Fails | Suitable here? | Weight |
|---|---|---|---|---|
| P/B | Lenders, asset-heavy cyclicals at trough | Asset-light | CROSS-CHECK ONLY. Theoretical P/B = ROE / CoE = 15.7% FY28 base ROE / 14.5% = 1.08x against 4.21x paid today (381 / 90.54). Post-IPO equity is mostly repaid debt and plant; book is not the value driver | 0% |
| NAV | Real estate, holding companies | Operating businesses | NO | 0% |

**Cash flow**

| Method | Works best | Fails | Suitable here? | Weight |
|---|---|---|---|---|
| DCF | Predictable stable cash flows | High growth, negative FCF, short history | NO. FCF negative in FY26 (-80.54) and H1 FY27 (-25.11); capex plan NOT FOUND; three years of operating history. Terminal value would exceed 70% | 0% |
| DDM | Mature dividend payers | Reinvesting growth names | NO. No dividend | 0% |

**Sector-specific**: P/EV, P/AUM, EV/Subscriber not applicable. SOTP: the four option slices are carried SOTP-style on top of the core per Amendment 18 (section-1b chunk 10). This is slice treatment inside both methods, not a third method.

### Final Method Selection

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E on the Section 1B destination (both tracks), forward basis FY27 at entry and FY30 at exit | 70% | Section 1B is the exit authority; earnings carry the mix and depreciation effects the operator ruled on |
| SECONDARY | EV/EBITDA, multiple = 0.6 x PE destination (capex intensity) | 30% | Neutral to capital structure and to the tax-regime dispute (D1); a cross-check on the PAT build |
| TERTIARY | none (P/B shown as a 0% sanity line) | 0% | No third method fits without peers |
| | | 100% | |

Interim line: Section 1A complete. Two methods applied, 70/30.

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE

### 1B.0 Converter classification gate (section-1b chunk 11)

- Classification: Model 3 CONVERTER; Models 1 and 2 NON-CONVERTER (operator ruling 2026-11-15; HD Section 7 ruling 4; OR-6, section-1b chunk 11).
- Model 3 tests: (a) steel plate is a quoted input: met. (b) Cost-plus or spread pricing with no design IP, the customer owns the design: met. (c) Margin co-moving with steel: untestable (about 4 integrated towers in FY26 plus one half). Ambiguity: the steel pass-through clause is NOT FOUND (HD 2.2). Ambiguous cases classify CONVERTER (OR-6).
- Spot ROCE 26.87% (TTM) / 26.79% (FY26 restated) | through-cycle ROCE for the Model 3 slice 21.59% = midpoint of current 26.79% and trough 16.39% (FY24), because listed history is shorter than 5 years | blend used before the operator method 23.45% = 64.3% x 21.59% + 35.7% x 26.79% (FD R16; B10.pillar1_roce_current_blend_pct).
- Volume test (17.2): net trade WC per tower Rs 8.8 lakh (FY24), 21.1 (FY25), 20.5 (FY26), 18.2 (Sep-2026, trailing 255 towers) (FD 2.3, H1R p.7). WC per unit moved; WC in rupees rose. The swing is not input-price driven. Fork: not INPUT-PRICE-DRIVEN. The third fork does not open.
- CLAUDE.md guard: no spot-year ROCE and no rupee WC trend feeds Section 1B for the converter slice. Holds.

### 1B.1 Pillar 1: ROCE base (section-1b chunk 01)

Worksheet line: "FTTCP ROCE forward verdict: FIRING (+2, operator Ruling 2) | ROCE used for base: 21.61% | ROCE Base Multiple: 18.3x | ROCE recovery credited via: Pillar 1."

- Approved input: 21.61% = (23.45% + 19.76%) / 2, the operator's method (DLB Ruling 4; B10.valuation_pillars_operator_approved).
- Formula (ROCE at or below 33%): Base PE = 0.5 x 21.61 + 7.5 = 18.305, rounded 18.3x (section-1b chunk 01).
- FLAG-FRAMEWORK-CONFLICT carried, recorded not resolved: chunk 01 maps FIRING to current ROCE. The midpoint rule belongs to RECOVERING above 60% with Strong catalysts. The operator method is an override. Both numbers are shown in 1B.9.
- Normalisation route: NONE. Route A test at 31-Mar-2026: (584.80 + 3,003.57) / 18,818.53 lakh = 19.1%, under 20% (FD Part 5 card). Route B condition absent. Worksheet: "Pillar 1 normalization route: NONE" (section-1b chunk 01).
- CONVERTER line: "Spot ROCE 26.87% | through-cycle ROCE used 21.59% for the Model 3 slice (midpoint of current and cycle trough), blended to 23.45%; the operator's Pillar 1 input 21.61% then averages that blend with FY28 base-case ROCE."

**FY28 ROCE recomputed by the approved method, on my own A26.1 base case (Kutch excluded)**

The method is the deliberation's: period-end capital employed (total assets less current liabilities), capital employed rolls forward by retained PAT, debt held flat, no dividend, EBIT = PBT + finance cost.

| Step | Deliberation (recorded) | Stage 11 base case | Anchor for stage 11 |
|---|---|---|---|
| FY27 towers | 277 (scenario midpoint) | 247 = 107 (H1 actual) + 140 (H2, JSW-lag reading) | H1R p.8 derived via B04; HD V5 [INFERENCE] |
| FY27 closing capital employed | Rs 291.0 Cr | Rs 282.98 Cr = 253.87 (30-Sep-2026) + H2 FY27 PAT 29.11 | B10.roce_latest_pct (H1R p.4, p.7); 2C below |
| FY28 towers | 277, held flat | 247, held flat (RUN-RATE basis, Year 2; 2A) | 2A |
| EBITDA per tower | Rs 33.72 lakh | Rs 33.72 lakh | B10.ebitda_per_tower_lakh (H1R p.4) |
| FY28 EBITDA | Rs 93.40 Cr | Rs 83.29 Cr | arithmetic |
| Depreciation | Rs 25.74 Cr | Rs 25.73 Cr (2 x H1 FY27 1,286.53 lakh) | H1R p.4 |
| FY28 EBIT | Rs 67.66 Cr | Rs 57.56 Cr | arithmetic |
| Interest / tax | Rs 2.8 Cr / 20.75% | Rs 2.80 Cr / 20.75% | B05 trigger 5 via DLB; H1R p.4 (current 360.01 + deferred 16.71 lakh on PBT 1,815.41 lakh) |
| FY28 PAT | Rs 51.41 Cr | Rs 43.40 Cr | arithmetic |
| FY28 closing capital employed | Rs 342.41 Cr | Rs 326.38 Cr | arithmetic |
| **FY28 ROCE** | **19.76%** | **17.64%** | |
| Pillar 1 input (approved method) | 21.61% | (23.45 + 17.64) / 2 = 20.54% | |
| Base PE | 18.3x | 0.5 x 20.545 + 7.5 = 17.77, rounded 17.8x | section-1b chunk 01 |
| Track 2 / Track 1 (r 14.5%) / Track 1 (r 14.0%) | 20.3x / 16.1x / 17.2x | 19.8x / 15.7x / 16.7x | |

The two differ because I place FY27 at the JSW-lag reading and carry the JSW pull as the T3 slice (p 0.4, HD Section 7 ruling 7). That counts the JSW rupees once. The deliberation used the scenario midpoint. **Governing: the approved 18.3x base, 20.3x Track 2, 16.1x Track 1.** The 17.64% figure is a stated sensitivity only.

Method caveat (reported, not acted on): with no capex plan (NOT FOUND) and debt held flat, retained PAT piles up inside capital employed as cash. An operational ROCE that strips that cash would read higher. The cash build depends on capex, which is NOT FOUND, so the operational figure is NOT FOUND.

### 1B.2 Pillar 2: cash conversion multiplier (section-1b chunk 02)

- Cumulative CFO/PAT: 0.48 audited, 0.58 restated (FY23-FY26) | Latest FY CFO/PAT: 0.35 audited, 0.50 restated | H1 FY27 1.97 | FCF positive? No (B10).
- Cash quality band: volatile (2.03, 0.79, 0.50, then 1.97) | base multiplier 1.00x (section-1b chunk 02).
- Structural or growth-induced: INDETERMINATE (operator Ruling 5). Evidence, CRISIL p.2 verbatim (B10.rating_wc_quote): "Gross current assets have been sizeable at 180–290 days for the past three fiscals and were 292 days as on March 31, 2026, led by receivables of 99 days and inventory of 226 days. The company needs to extend high credit period to customers and hold work-in-process and raw material inventory to meet business requirement."
- No Section 1B layer sets a multiplier for INDETERMINATE (open ruling OR-5, section-1b SKILL.md). Treated as an unresolved input (override 3):

| Reading | Multiplier | Offset | Quality-adjusted base | Track 2 | Track 1 |
|---|---|---|---|---|---|
| Structural (rating agency WC language) | 0.65x | none | 18.3 x 0.65 = 11.9x | 13.9x | 11.9 x 0.88 = 10.5x |
| Growth-induced (FD R9 lean: Rs 18.38 Cr inventory release in H1 FY27) | 0.80x | +0.20 (PAT/revenue CAGR above 40%) | 18.3 x 1.00 = 18.3x | 20.3x | 16.1x |
| Applied (operator Ruling 4) | 1.00x | 0 (volatile-band neutral, equal to the growth-induced result) | 18.3x | 20.3x | 16.1x |

- Separating observation: FY27 operating cash flow at or above 70% of EBITDA with receivables under 60 days and inventory under 90 days at 31-Mar-2027 (growth-induced) against below 50% (structural). Confirm-by: FY27 audited cash flow, about Sep-2027 (FD Step 5 trigger 5).
- Effective Cash Multiplier: 1.00x. Quality-Adjusted Base: 18.3x x 1.00x = 18.3x.
- FLAG-CASH stays: the gate verdict caps at PROCEED WITH CAVEATS. Missing evidence: customer-wise receivables ageing at 31-Mar-2026 and 30-Sep-2026; vendors, order value and security behind the Rs 30.04 Cr capital advances; revenue, cost and WC by contract model per half; Model 3 payment terms and steel clause; FY27 audited cash flow (DLB Ruling 5).

### 1B.3 Pillar 3: growth visibility (section-1b chunks 03 and 12)

- Amendment 16 gate (section-1b chunk 12): FTTCP B2 reads "growth premium eligible: YES from FY27" on minimum ROCE 13.5% (FD Part B). On the valuation's r of 14.5%, my base ROCE path (21.8%, 17.6%, 17.7%, 19.3%, 18.7%; 2C) stays above it. Eligible. The bear path (8.5% FY28, 10.1% FY29) would shut the gate.
- Emerging Moat Score: 10.8 / 100 | catalyst proximity: Kutch audit about 15-Dec-2026 and H2 FY27 print about May-2027, 0-12 months | evidence quality: mixed (B10).
- 3a: +2x. Two qualifiers pass on filed evidence: capex-embedded growth 22.5% (B07) and order book 2.76x FY26 revenue / 1.55x trailing revenue (PR p.2; H1R p.4). Grade C caps 3a at +2x (section-1b chunk 03).
- 3b: +0x (EM below 25). 3c: +0x (book executes by end Q1 FY28, about 8 months; PR p.3).
- Combined +2x, inside the +6x cap.
- Amendment 22 note (OR-3 open): probabilities on the four slices are stated in the Option Resolution Calendar (2.5). No rule converts them into 3a turns.
- Shared catalyst: "Growth Visibility Premium: +2x | Shared catalyst? YES." The order-book qualifier is the same book credited at 100% in base-case revenue for FY27 and Q1 FY28. Strict single credit (section-1b chunk 03, "not credited again in Pillar 3 at full weight") would leave 3a on one qualifier, which pays +0x. Then Track 2 = 18.3x. Track 1 carries no Pillar 3, so the governing track is unaffected. Reported, not applied: the operator approved +2x with the shared catalyst flagged (FD handoff "SHARED CATALYST 2").
- Entrepreneur Ledger (Role 2 Section 3G) is stage 14's. This stage does not credit any ledger fact.

### 1B.4 Strategic premium (section-1b chunk 04)

"Strategic position: none (13 approved tower makers on EN-156, 6 on Sany [AGENCY, MNRE annexures, HD 2.5]) | Strategic Premium: +0x." "ROCE recovery credited via: Pillar 1." The re-rating-optionality route is closed because the recovery sits in Pillar 1.

### 1B.5 UA, sector cap, override (section-1b chunk 05)

- "UA qualifiers: listed 12m or more NO (listed 2026-08-10) | Gate 0 60 or more YES (core 66) | FII+DII under 3% NO (11.96%, NSE XBRL 30-Sep-2026) -> UA applied: N" (B10.ua_qualifiers).
- "Sector: Cables / Industrial products -> Cap: 25x (quality-uplifted: N, UA not triggered)" (operator ruling 2026-11-15; HD Section 7 ruling 2).
- Category-Break Override: N. Condition 1 fails (towers are not a new category) and condition 4 fails (13 approved makers on EN-156).

### 1B.6 Four-Pillar Summary, Track 2 (section-1b chunk 06)

| Step | Calculation | Value | Chunk |
|---|---|---|---|
| A. ROCE Base | 21.61% -> 0.5 x 21.61 + 7.5 | 18.3x | section-1b chunk 01 |
| B. Cash Multiplier (effective) | 1.00x + offset 0 (INDETERMINATE, OR-5) | 1.00x | section-1b chunk 02 |
| C. Quality-Adjusted Base | 18.3 x 1.00 | 18.3x | section-1b chunk 06 |
| D. Growth Visibility Premium | 3a +2, 3b +0, 3c +0; cap +6x not binding; A16 YES from FY27 | +2.0x | section-1b chunks 03, 12 |
| E. Strategic Premium | none | +0.0x | section-1b chunk 04 |
| F. Raw Destination PE | 18.3 + 2.0 + 0 | 20.3x | section-1b chunk 06 |
| F2. UA-Adjusted Raw PE | UA not applied | 20.3x | section-1b chunk 05 |
| G. Sector Cap | Cables / Industrial products, no uplift | 25.0x | section-1b chunk 05 |
| G2. Category-Break Override | N | N | section-1b chunk 05 |
| G3. Override-Adjusted Cap | = G | 25.0x | section-1b chunk 05 |
| **H. Final Destination PE** | **min(20.3, 25.0)** | **20.3x** | section-1b chunk 06 |

Range H plus or minus 7.5%: 18.8x to 21.8x (approved, DLB Ruling 4). Chunk 06 rounding to the nearest 0.5x would print 19.0x to 22.0x. The A6 rounding ruling is open (FD lessons pre-read); I carry the approved figures.

### 1B.7 Track 1 (RRM) (section-1b chunk 15)

r worksheet line: "r base 14.0% (small/micro); durability adj 0 (band: Unproven, reason: listed 2026-08-10, short record); governance adj 0 (numeric table NOT FOUND; promoter CAUTION); cyclical surcharge 0 (not applied by the operator; the 12B cap of +0.75 would bind if the band were docked for cyclicality: N); complexity adj +0.5 (Amendment 13: Darpan Infrastructure is guarantor, lender, contractor, landlord and fee recipient, and its records do not reconcile, B02, B08 via FD R20); cash-conversion r-UP: none per 12A; short-record r-UP: none per 12C; final r 14.5% (bounded [9%, 18%])."

- RRM = 1 + (13.5 - 14.5) x 0.12 = 0.88 (inside 0.70 to 1.60) (section-1b chunk 15).
- Track 1 = Fundamental Base PE x RRM = 18.3 x 0.88 = 16.1x; range 14.9x to 17.3x (approved). Chunk 06 rounding would print 15.0x to 17.5x.
- "Fundamental Base PE" is undefined in the Master and chunks 06 and 15 (NOT FOUND). Repo precedent applies RRM to the quality-adjusted base C (FD differences note (a)). Carried.
- Darpan check pending (Ruling 7): at r 14.0%, RRM 0.94, Track 1 17.2x.
- Unruled sensitivity, not applied: a cyclical surcharge of +0.75 for the converter slice would give r 15.25%, RRM 0.79, Track 1 14.5x.
- Macro check: market cost of equity 6.76% + 7.31% = 14.07% against the RRM neutral 13.5%, gap 57 bps, under the 100 bps review trigger (macro-sheet.md, August 2026). FLAG: the sheet is STALE. Its next refresh was 1-Sep-2026.

### 1B.8 Dual track

| | Track 2 (additive) | Track 1 (RRM, r 14.5%) |
|---|---|---|
| Destination PE | 20.3x (18.8x to 21.8x) | 16.1x (14.9x to 17.3x) |
| Divergence | 26% (20.3 / 16.1 - 1) | |

Divergence is above 15%. Track 1 fits this company better, for three reasons. (1) It carries no Pillar 3, so it does not pay twice for the order book that already sits in base revenue. (2) 16.1x sits in the R2 cost-advantaged converter neighbourhood (about 15-17x, CLAUDE.md quality ladder), the FROM rung the business occupies on evidence. 20.3x sits above the R3 neighbourhood (about 19x), the TO rung the dossier calls a claim, not a finding (09b Part B1). (3) It prices the Darpan complexity once, in r. Track 1 is also the more conservative track and sets the entry zone (open ruling OR-1 as written; operator Ruling 4; section-1b chunk 06).

### 1B.9 Destination PE sensitivity table (approved base governs)

| Line | Pillar 1 input | Base PE | Track 2 | Track 1 (r 14.5%) | Track 1 (r 14.0%) | Status |
|---|---|---|---|---|---|---|
| **Operator-approved (DLB Ruling 4)** | 21.61% | 18.3x | **20.3x** | **16.1x** | 17.2x | GOVERNING |
| Approved method on stage 11 base FY28 ROCE 17.64% | 20.54% | 17.8x | 19.8x | 15.7x | 16.7x | sensitivity (instruction) |
| Section 1B FIRING rule (current ROCE, chunk 01) = Claude Code draft | 23.45% | 19.2x | 21.2x | 16.9x | 18.0x | sensitivity (OR-16) |
| 4G Year-3-consistent (FY29 base ROCE 17.72%) | 17.72% | 16.4x | 18.4x | 14.4x | 15.4x | sensitivity (4G check fails, see 4G) |
| Steel clause found, no converter (FD R16 bracket) | 26.79% | 20.9x | 22.9x | 18.4x | 19.6x | sensitivity |
| Cash structural 0.65x | 21.61% | 11.9x | 13.9x | 10.5x | 11.2x | sensitivity |
| Pillar 3a strict single credit (+0x) | 21.61% | 18.3x | 18.3x | 16.1x | 17.2x | sensitivity |
| EM NONE exit haircut, minus one turn (A18.0) | 21.61% | 18.3x | 19.3x | 15.1x | 16.2x | sensitivity, flagged for operator ruling |
| Bear-consistent pillars (bear FY29 ROCE 10.1%; A16 gate shut) | 10.1% | 12.6x | 12.6x | 11.1x | 11.8x | bear sensitivity only |

Override cost on Track 1, as the deliberation recorded: 16.1x against 16.9x, 4.7%.

### 1B.10 Relative PE expression (section-1b chunk 15)

"Absolute H 16.1x (Track 1) / 20.3x (Track 2) | market PE 20.5x (Nifty 50 TTM, macro-sheet dated 17-Aug-2026, STALE) | relative destination PE 0.79 / 0.99 | name historical relative band NOT FOUND (listed 3 months) | sector historical relative band NOT FOUND | B8 rating NOT DETERMINABLE (FD Part B) | conclusion: no B8 support to move H toward the top of its range; H stays at the mid." Against the Nifty Smallcap 250 at 34.4x (07-Aug-2026, 22% above its 5-year median): 0.47 / 0.59.

### 1B.11 Step 1C relative cross-check (section-1b chunk 15, Amendment 20)

PENDING LIVE PEER TABLE. No live, dated peer table is injected (B10.peer_table). No peer multiple is used or recalled (Correction 6 guard). The pillar destination governs. For Claude web: the relative multiple would govern only if the adjusted peer base exceeds 16.1 / 0.70 = 23.0x, and it would stay capped at 25x (20.6). The operator-approved base binds (20.9).

### 1B.12 Recognition gap (09b Part B4) and market-implied readings

- Current PE: 381 / 17.33 (FY27 forward operating EPS, base) = 22.0x; 381 / 19.24 (TTM) = 19.8x (screener 19.5x).
- TO rung neighbourhood (CLAUDE.md quality ladder): R3 about 19x for the Model 2 line; Models 1 and 3 stay R2, about 15-17x (09b Part B1).
- **Resolution: the recognition gap is CLOSED.** The current PE (22.0x forward, 19.8x trailing) already sits at or above the R3 neighbourhood and above both destinations. The re-rating engine is spent. It is negative: Track 1 16.1x is 27% below the current 22.0x; Track 2 20.3x is 8% below. The return rides EPS growth alone, against a de-rating headwind. This feeds the Hurdle read and the verdict card.
- Transition posture (CLAUDE.md matrix): proof gate NOT FIRED (Ruling 3) + ugliness ARTIFACT-OF-CLIMB (provisional, 09b B5) + gap CLOSED = **PRICED NARRATIVE (TRAP)**: "AVOID or hard WATCH with no position until the proof gate fires AND the price re-opens the gap."
- Implied growth at Rs 381 (Market-Implied block NOT FOUND; this is my own PE-gap arithmetic on the chunk 14 identity, base EPS Rs 17.33, 3-year hold, r 14.5%):

| Exit multiple used | EPS CAGR the price needs to earn r (14.5%) | EPS CAGR for the 25% hurdle |
|---|---|---|
| Flat at current 22.0x | 14.5% | 25.0% |
| Track 1 destination 16.1x (governing) | 27.0% (FY30 EPS Rs 35.52) | 38.7% (FY30 EPS Rs 46.22) |
| Track 2 destination 20.3x | 17.6% (FY30 EPS Rs 28.17) | 28.4% (FY30 EPS Rs 36.66) |
| Sector cap 25x (chunk 14 reading 2 default) | 9.7% (FY30 EPS Rs 22.88) | 19.8% (FY30 EPS Rs 29.77) |

- Evidence: base EPS CAGR 14.7%; probability-weighted 17.3% (1B.13). Spread on the governing destination: price 27.0% against evidence 17.3%. Reading: PRICED-WE-ARE-LATE. On the sector cap reading the price assumes 9.7%, which would read OPPORTUNITY. The two readings separate on which multiple the Year-3 buyer pays. Section 1B is the sole exit authority, so the destination-based reading governs.

### 1B.13 Hurdle Ratio (section-1b chunk 06; OR-2, OR-27)

- Tier: A | Hurdle: 25% (FII+DII 11.96% is above 3%, but Gate 0 is AVERAGE and EM is 10.8, so the Tier B quality gates fail; FD handoff).
- EPS CAGR basis (A21/A22): probability-weighted, from the A21 base EPS Rs 17.33 (FY27) to the probability-weighted FY30 EPS Rs 27.98. FY30 PAT 65.40 (base) + 0.5 x 3.6 (EN-182) + 0.4 x 12.65 (Kutch) - 0.35 x 6.61 (D1 at FY30 PBT) = 69.95 Cr. JSW and D2 are FY27 timing items and add nothing to FY30. CAGR = (27.98 / 17.33)^(1/3) - 1 = 17.3%.
- Bull row: grade C, so Bull = base + 5 pp = 22.3% (OR-27, section-1b chunk 06).

| Track | HR (base, 17.3%) = 1.173^3 x (PE mid / 21.98) | HR (bull, 22.3%) | Threshold | Band |
|---|---|---|---|---|
| Track 1 (16.1x) | 1.614 x 0.7325 = 1.18 | 1.829 x 0.7325 = 1.34 | 1.953 | STOP band |
| Track 2 (20.3x) | 1.614 x 0.9236 = 1.49 | 1.829 x 0.9236 = 1.69 | 1.953 | STOP band |

STOP band on both tracks: the 25% hurdle is infeasible even on capped bull earnings at Rs 381. Hurdle Ratio band shown, caps no verdict (section-1b chunk 06, OR-2). To pass on Track 1 the EPS CAGR would need 38.7%.
- "Would you personally pay this destination PE for this quality of business?" 16.1x, yes: it is an R2 converter multiple for a grade C, thin-moat fabricator with INDETERMINATE cash. 20.3x, no: it pays for an R3 climb that is not yet evidenced.

> Section 1 complete. Methods selected. Four-pillar destination PE calculated at 18.8x to 21.8x (RRM track: 14.9x to 17.3x). Current PE is 22.0x (FY27 forward base; 19.8x trailing). Hurdle Ratio band: STOP (caps no verdict).

---

## SECTION 2: PROJECTIONS

### 2.0 Horizon and exit basis (section-1b chunk 10)

- "Earnings basis (entry and exit): forward (operator-approved: Y, DLB Ruling 1)."
- Year 0 = FY26 (audited). Year 1 = FY27, the operator's forward year at entry (17-Nov-2026). Hold N = 3 years, to about Nov-2029. Exit year = FY29 (Year 3). **Exit forward EPS year = FY30 (Year 4)**: exit price = destination PE x FY30 EPS (Amendment 18.1). The relation of FY30 to the exit date matches the relation of FY27 to the entry date.
- Projection to Year 5 (FY31). Year 4 rows are committed in all cases (A18.0).

### 2A. Revenue (section-1b chunk 07)

Volume is the honest unit: revenue per tower runs Rs 0.59 Cr (Model 1) to Rs 3.5 Cr (Model 3) (HD 2.1), so revenue swings with mix. I project towers x EBITDA per tower, and revenue as towers x revenue per tower.

**Rule B basis by year (A26.1)**

| Year | Basis declared | Evidence | Towers |
|---|---|---|---|
| FY27 (Y1) | ORDER-BOOK | Book Rs 395.58 Cr, 320 units (about 292 real towers) at 31-Oct-2026, executes by end Q1 FY28 (PR p.2-3; Pres p.21; HD Sec 4 item 4 [INFERENCE]); 38-tower Evren order Rs 133.98 Cr for Q4 FY27 (NSE order 2026-09-10); H1 actual 107 towers (H1R p.8 via B04). H2 = JSW-lag reading 140 towers, Rs 228 Cr revenue, Rs 51 Cr EBITDA [INFERENCE, HD V5] | 247 |
| FY28 (Y2) | RUN-RATE (FY27 full year held; seasonal, so a full-year run-rate, not H1 annualised) | Same as the DLB Ruling 4 construction ("held flat; no FY28 order book exists beyond Q1 FY28") | 247 |
| FY29-FY31 (Y3-Y5) | Industry fade path from the Rule B level (A14, EM NONE) | Wind roadmap 9, 10, 12, 13.2 GW for FY28 to FY31 (B09 tam_growth_pct note; MNRE/IWTMA roadmap). Named assumption: not on B10 | 274, 329, 362 |

**FY28 reconciliation against the book (why 247 is the most evidenced point)**

- Book left after the JSW-lag H2: at least 152 towers (292 real towers less 140 H2 towers if all come from the 31-Oct book; more if October dispatches, NOT FOUND, sat outside it). Plus LOIs Rs 44.05 Cr, 44 towers (Pres p.7, p.20 via B07; the one prior LOI converted at 112%, B05). Floor: 196 towers, about Rs 212 Cr (FD 2.1 low reading).
- New inflow pace: Rs 189.73 Cr, 48 towers, from April to October 2026 (B03: 395.58 + 153.97 - 359.82; 12b R21: the 48 towers are the two filed orders). That is about 6.9 towers a month. Orders placed November 2026 to July 2027 execute inside FY28 on the disclosed 8-month cycle: about 62 towers at that pace.
- 247 needs at most 51 new towers inside FY28: at most 82% of the trailing pace, and fewer if October dispatches sat outside the book.
- Two readings. (A) Book-only, no new orders: 196 towers. (B) Inflow at the trailing pace: about 258 towers or more. Separating observation: new order intimations from November 2026 to March 2027 of 34 towers or more (the trailing pace for five months), and the order book in the H2 FY27 deck. Confirm-by 31-Mar-2027 (tracker row 3) and the H2 FY27 deck, about May-2027.
- Cross-check against the rating agency: CRISIL projects cash accrual of Rs 80 Cr a year (CRISIL p.2). My base FY28 accrual is PAT 43.40 + D&A 25.73 = Rs 69.13 Cr, 14% lower. The agency figure rests on company projections (grade C). It sits nearer the JSW-pull reading (FY27 accrual Rs 81.73 Cr).

**Revenue table (Rs Cr)**

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| Logic | Book-only FY28 (no new orders for 12 months), then flat at that pace (industry floor 0%, B09); triggers failed: JSW, EN-182 repeat, Kutch | Order book FY27, run-rate FY28, industry growth FY29-FY31 | JSW pulls Sany towers in FY27 (307 towers, HD V5), then industry growth to Koppal nameplate 420 (Kutch in the slice only) |
| Towers FY27 / FY28 / FY29 / FY30 / FY31 | 247 / 196 / 196 / 196 / 196 | 247 / 247 / 274.4 / 329.3 / 362.3 | 307 / 345.4 / 383.8 / 410 + 10 EN-182 slice / 410 + 10 |
| Revenue per tower FY28 onward | Rs 1.08 Cr (residual book, conversion-heavy) | Rs 1.355 Cr (book Rs 395.58 Cr / about 292 towers [INFERENCE]) | Rs 1.355 Cr |
| Revenue Year 0 (FY26) | 143.27 | 143.27 | 143.27 |
| Revenue Year 1 (FY27) | 381.97 | 381.97 | 417.97 |
| Revenue Year 2 (FY28) | 211.7 | 334.7 | 468.0 |
| Revenue Year 3 (FY29) | 211.7 | 371.9 | 520.0 |
| Revenue Year 4 (FY30) | 211.7 | 446.2 | 555.6 |
| Revenue Year 5 (FY31) | 211.7 | 490.9 | 555.6 |
| Revenue CAGR FY26-FY29 | 13.9% | 37.4% | 53.7% |

- Bull is NOT guidance at face value: grade C bars that (section-1b chunk 17). Guidance needs Rs 296-346 Cr in H2 against scenarios of Rs 228-264 Cr (HD Section 5).
- Historical CAGR cross-check: 77.1% (FY23-FY26, ramp base). Base FY26-FY29 37.4%: divergence -39.7 pp. Confirm-by observation: H2 FY27 revenue of Rs 228 Cr or more with new inflow in the book; date: H2 FY27 results, about May-2027. It feeds the Expectation Ledger (row B1).
- SOM cross-check: base 37.4% (3 yr) and 27.9% (5 yr, FY26-FY31) sit below the SOM-implied 49.3% and 35.1% (B10). Consistent. No cut needed. Bull 53.7% exceeds the 3-year SOM; that is the bull.
- Capacity: base FY31 362 towers = 86% of Koppal 420 (Kutch excluded); the best half (148 towers, H2 FY26) annualises to 70% of Koppal. Realistic peak utilisation NOT FOUND (FD B1). Bull FY30 reaches 100% of Koppal nameplate.
- Named assumption: tower-equivalent growth equals GW growth. Larger turbines cut towers per GW but raise tonnes and value per tower. The net effect is NOT FOUND.

**Amendment 14 fade sensitivity (operator instruction: EM NONE, industry growth from Year 1 on the FY26 base)**

| | FY27 | FY28 | FY29 | FY30 | FY31 |
|---|---|---|---|---|---|
| Industry growth (GW roadmap 6.05 -> 8 -> 9 -> 10 -> 12 -> 13.2, B09) | +32.2% | +12.5% | +11.1% | +20.0% | +10.0% |
| Towers (210 FY26 base, Koppal cap 420) | 277.7 | 312.4 | 347.1 | 416.5 | 420 (458 uncapped) |
| EBITDA at Rs 33.72 lakh | 93.64 | 105.34 | 117.04 | 140.44 | 141.62 |
| PAT | 48.52 | 60.87 | 70.14 | 88.69 | 89.62 |
| EPS | Rs 19.41 | Rs 24.35 | Rs 28.06 | Rs 35.48 | Rs 35.85 |

- EPS CAGR FY27-FY30 22.3%. Year-3 Track 1 core value 16.1 x 35.48 = Rs 571.2 (14.4% CAGR from Rs 381). HR on this path: 1.829 x (16.1 / 19.6) = 1.50, still below 1.953.
- Here the fade path sits ABOVE the base. Industry growth from Year 1 holds Anawil's FY26 tower share (about 11.8% at 3.4 MW a tower). The base lets that share fall to about 9.3% by FY31, because the evidence points that way: turbine makers that build their own towers were about 49% of FY26 installs [SECONDARY, HD V5]; DEE Fabricom, KP Green and Inox add tower capacity [COUNTERPARTY, HD 2.5]; firm inflow outside two orders was about zero for seven months (B05). Separating observation: the same order-inflow test as 2A (34 towers or more by 31-Mar-2027).

### 2B. Profitability (section-1b chunk 07)

Cyclical override: the archetype is flagged (asset-heavy manufacturing), but no full cycle is printed. Peak, trough and average are NOT DETERMINABLE (FD Part B). The name is a margin-reset name under OR-11 (FD handoff). Base = the Rule C bridge on EBITDA per tower. Bear = the evidence bridge, not the trailing 3-year average (40.6%, which predates steel in revenue).

**Base margin bridge (Rule C, A26.2)**

| Lever | bps contribution | Evidence | Confirm-by |
|---|---|---|---|
| Current margin | 23.4% (H1 FY27, EBITDA per tower Rs 33.72 lakh, revenue per tower Rs 1.439 Cr) | H1R p.4 via B10 | n/a |
| Mix shift: order-book mix (Model 3 51.3% of book against 64.3% of H1 revenue) lowers revenue per tower to Rs 1.355 Cr at the same EBITDA per tower | +145 bps | Pres p.21 book mix (B04); per-tower EBITDA at band midpoints of the book about Rs 33-34 lakh (FD 2.2 [INFERENCE]) | H2 FY27 results with revenue and cost by model per half, about May-2027 |
| Operating leverage on fixed cost | dropped | no evidence line | n/a |
| Steel pass-through | dropped | clause NOT FOUND | n/a |
| **Base margin Year 3 (FY29)** | **24.9%** | | |

The bridge lifts margin by 145 bps, under 400 bps, so no Rule F chain is required.

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| EBITDA per tower FY28 onward | Rs 29.1 lakh (FY26, FD 2.2; the B6 falsifier line is Rs 29 lakh). FY28 steel mean-reversion year: Rs 25.6 lakh | Rs 33.72 lakh (H1 FY27) | Rs 34.5 lakh (H2 FY26, highest printed half, FD 2.2) |
| EBITDA margin FY29 | 26.9% (conversion-heavy revenue; read per tower, not per cent) | 24.9% | 25.5% |
| Margin logic | Share loss plus one steel year (A17.3). The 5-year median spread is NOT FOUND (about 1.5 years of Model 3 history); stand-in = median of printed EBITDA per tower (FY24 19.5, FY25 about 22, FY26 29.1, H1 FY27 33.7) = Rs 25.6 lakh | Destination mix, per-tower level held | Integrated mix at the best printed half |
| Depreciation | Rs 25.73 Cr | Rs 25.73 Cr (2 x H1 FY27, H1R p.4). CWIP Rs 30.69 Cr (H1R p.7) and maintenance capex would add more; capex plan NOT FOUND | Rs 25.73 Cr |
| Interest | FY27 Rs 6.68 Cr (H1 5.28 + H2 1.40), then Rs 2.80 Cr | same | same |
| Tax rate | 28.76% (20.75% + 8.008 pp if Section 115BAB is denied: 25.168% against 17.16%, Pros p.240-241) plus a one-off Rs 5.2 Cr for FY24-FY26 in the equity bridge | 20.75% (H1R p.4) | 20.75% |
| PAT margin FY29 | 9.6% | 13.6% | 15.8% |
| Dilution | 0% | 0% | 0% |

Operating earnings only (FTTCP B4): other income (H1 FY27 Rs 0.22 Cr, H1R p.4) is stripped from every multiplied EPS. Cash was Rs 0.20 Cr at Sep-2026, so the stripped item is immaterial.

### 2C. Projection table, BASE CASE (Rs Cr unless stated)

| Line item | Year 0 FY26 | Year 1 FY27 | Year 2 FY28 | Year 3 FY29 | Year 4 FY30 | Year 5 FY31 |
|---|---|---|---|---|---|---|
| Towers | 210 | 247 | 247 | 274.4 | 329.3 | 362.3 |
| Revenue | 143.27 | 381.97 | 334.7 | 371.9 | 446.2 | 490.9 |
| EBITDA | 61.23 | 87.08 | 83.29 | 92.54 | 111.05 | 122.16 |
| EBITDA margin | 42.7% | 22.8% | 24.9% | 24.9% | 24.9% | 24.9% |
| D&A / interest | 11.30 / 5.79 | 25.73 / 6.68 | 25.73 / 2.80 | 25.73 / 2.80 | 25.73 / 2.80 | 25.73 / 2.80 |
| Operating PBT | 44.14 | 54.67 | 54.76 | 64.01 | 82.52 | 93.63 |
| PAT (operating) | 35.95 reported | 43.33 (reported 43.50) | 43.40 | 50.73 | 65.40 | 74.20 |
| EPS (operating, 2.49998 Cr shares) | Rs 18.78 filed (Rs 14.38 on post-IPO shares) | Rs 17.33 | Rs 17.36 | Rs 20.29 | Rs 26.16 | Rs 29.68 |
| Book value / share (year end) | Rs 90.54 at 30-Sep-2026 | Rs 102.18 | Rs 119.54 | Rs 139.84 | Rs 166.00 | Rs 195.68 |
| Est. CFO = PAT + D&A - change in WC (WC Rs 18.2 lakh a tower) [INFERENCE] | 12.47 audited | 67.25 (H1 actual 28.28) | 69.13 | 71.47 | 81.14 | 93.93 |
| Est. FCF | -80.54 | NOT FOUND (H2 capex) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND (capex plan NOT FOUND) |
| Est. net debt | 126.65 (31-Mar-2026) | 33.41 held | 33.41 held | 33.41 held | 33.41 held | 33.41 held (no committed projection; A19.0) |
| Est. ROCE (period end, deliberation method) | 26.72% | 21.76% | 17.64% | 17.72% | 19.28% | 18.66% |
| Est. ROE (average equity) | 40.16% (closing) | 25.2% (IPO mid-year) | 15.7% | 15.6% | 17.1% | 16.4% |

FY27 build: EBITDA 36.08 (H1) + 51.0 (H2) = 87.08; PBT 87.08 - 25.73 - 6.68 = 54.67; tax 11.34; PAT 43.33. H2 PAT 29.11 rolls capital employed from 253.87 to 282.98.

FY27 base against Ruling 1's range: my FY27 PAT is 43.3 (JSW lag) and 56.0 (JSW pull) against the "about 45 to 57" the operator cited [INFERENCE, HD V5]. The gap is the tax rate. The HD figures reproduce at about 17.2% (the 115BAB rate); I use the filed H1 FY27 effective 20.75%, as the deliberation's own FY28 build does. This is an EPS input, not an exit-multiple change.

**Bear and bull rows**

| | FY27 | FY28 | FY29 | FY30 | FY31 |
|---|---|---|---|---|---|
| Bear EBITDA | 87.08 | 50.18 | 57.04 | 57.04 | 57.04 |
| Bear PAT | 38.95 | 15.42 | 20.31 | 20.31 | 20.31 |
| Bear EPS | Rs 15.58 | Rs 6.17 | Rs 8.12 | Rs 8.12 | Rs 8.12 |
| Bear ROCE | 22.5% | 8.5% | 10.1% | 9.5% | 9.0% |
| Bull EBITDA | 103.08 | 119.16 | 132.41 | 141.45 | 141.45 |
| Bull PAT | 56.00 | 71.82 | 82.33 | 89.49 | 89.49 |
| Bull EPS | Rs 22.40 | Rs 28.73 | Rs 32.93 | Rs 35.80 | Rs 35.80 |

### 2C-w. Section 2 worksheet line (section-1b chunk 17)

"Base-case basis: ORDER-BOOK (FY27) then RUN-RATE (FY28 held) then the A14 industry fade path (FY29-FY31). Evidence: order book Rs 395.58 Cr at 31-Oct-2026 (PR 2026-11-06 p.2; Pres 2026-11-08 p.21); NSE order 2026-09-10 (38 towers, Rs 133.98 Cr); NSE intimation 2026-10-29 (10 EN-182 towers); H1 FY27 results (H1R p.4, p.8, filed 2026-11-06); H2 per the HD V5 JSW-lag reading [INFERENCE]. Historical CAGR cross-check: 77.1% (divergence -39.7 pp, confirm-by observation: H2 FY27 revenue of Rs 228 Cr or more and new order inflow of 34 towers or more by 31-Mar-2027, date: H2 FY27 results, about May-2027). Margin bridge: current 23.4% -> Year 3 24.9% via [order-book mix shift: +145 bps, Pres p.21] x 1 (operating leverage and steel pass-through dropped: no evidence line). Track-record period for weighting: trailing about one half-year since listing on 2026-08-10 (Role 5 history under four quarters; 2 delivered, 3 partial, 1 missed, B05), Role 5 grade C. Catalyst credit split: revenue 100% (filed order book for FY27 and Q1 FY28) / Pillar 3 0% on governing Track 1; Track 2 carries the operator-approved 3a +2x, which shares the order-book qualifier (SHARED CATALYST 2; strict single credit would pay +0x)."

### 2D. Projection sanity checks (section-1b chunk 06)

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | Base to FY29 needs 274 towers, 65% of Koppal 420. FY30-FY31 need 78% to 86%, above the best printed half (70%). Realistic peak utilisation and plant-wise tonnage NOT FOUND; 474 t towers cap the company at about 437 towers on 207,000 t (B03) | PASS to FY29; CAUTION FY30-FY31 |
| Margins require something unprecedented? | EBITDA per tower Rs 33.72 lakh = H1 FY27 print; H2 FY26 printed 34.5 | PASS |
| ROCE stays above 15%? | Base 17.6% to 21.8% | PASS (bear fails: 8.5% to 10.1%) |
| FCF sufficient to fund growth without excessive new debt? | No capacity capex needed to FY31 on Koppal. But H1 FY27 capex Rs 53.39 Cr exceeded CFO Rs 28.28 Cr; a CMD loan of Rs 21.68 Cr filled the gap (FD 3.3). Capex plan NOT FOUND | INDETERMINATE |
| EPS growth from operations, not financial engineering? | Volume x per-tower EBITDA; no dilution or buyback. Flat D&A flatters FY29-FY31 a little (CWIP Rs 30.69 Cr not depreciated in the model) | PASS, with the note |
| Implied market share realistic? | Tower share about 11.8% (FY26, 210 of about 1,779 at 3.4 MW, B09 method 2) falls to about 9.3% by FY31 (362 of about 3,882). A falling share fits the OEM in-house trend | PASS |
| CFO/PAT consistent with Pillar 2? | Mechanical base CFO/PAT 1.2-1.6 holds only if WC per tower stays near Rs 18-21 lakh. The structural reading (CRISIL 292 GCA days) would break it. 1.00x is the neutral reading of an INDETERMINATE input | INDETERMINATE (FLAG-CASH) |
| Year 3 ROCE consistent with the FTTCP ROCE forward verdict used in Pillar 1? | FY29 base ROCE 17.7% against 23.45% current blend and 26.79% FY26. ROCE falls in the base. FIRING (+2) rests on Kutch approval and fill, which single credit keeps out of the base. Falsifier: no Kutch approval by 31-Mar-2027 reverts to STAGNANT (Ruling 2) | FAIL: flagged (FLAG-ROCE-PATH); approved multiple governs |
| **Did the base case credit the transition, or price the audited past?** | It credits the transition at evidenced levels: revenue runs on the order book and run-rate, not the 77.1% historical CAGR; margin runs on the H1 FY27 EBITDA per tower (up from Rs 29.1 lakh in FY26) and the book mix, not the 40.6% trailing average. It does not credit Kutch (slice) or the R3 rung (unproven) | PASS |

> Section 2 complete. Projections built.

### 2.4 A21 run-rate earnings base (section-1b chunk 08)

"Earnings base: full-year FY27 forward scenario (seasonal half-yearly filer: H2 is 70-80% of the year, B10.seasonal; operator Ruling 1; the dossier pre-ruling's full-year branch) | PAT run-rate Rs 43.33 Cr (EPS Rs 17.33) | one-offs adjusted: other income Rs 0.22 Cr stripped (operating earnings, B4); Section 115BAB back-tax of about Rs 5.2 Cr for FY24-FY26 kept out of earnings (D1 row; equity bridge in the bear); H1 not annualised | annual model divergence: -9.9% against TTM PAT Rs 48.09 Cr; +20.5% against FY26 audited Rs 35.95 Cr (the floor), both under 25% (governing: the forward base, because the operator ruled the basis and the TTM carries an H2 FY26 margin of 50.1% that stage 3 reads as timing)."

### 2.5 Option Resolution Calendar (section-1b chunk 10, A18.2)

| Slice | Window | Class | Resolution event | Tracker row (HD Sec 6) | p (operator, HD Sec 7 r7) | SUCCESS PAT x own multiple |
|---|---|---|---|---|---|---|
| 1. Second EN-182 order | by 30-Jun-2027 | RESOLVES-WITHIN-HOLD | NSE order intimation for EN-182 towers | row 1 | 0.50 (unconditional) | Rs 3.6 Cr (10 towers at Rs 40-50 lakh, B10 row 1) x 16.1x T1 / 18.3x T2. Model 3 converter slice: own PE on through-cycle 21.59% = 18.3x base (FD R16 bracket); T2 slice carries no Pillar 3 |
| 2. Kutch approved and over 30% used | by 31-Mar-2028 (first read about 15-Dec-2026) | RESOLVES-WITHIN-HOLD | Customer approval filed and Gujarat revenue above Rs 8.78 Cr a half; 58 towers a year | row 4 | 0.40 | Rs 12.65 Cr (mid of 11.5-13.8, B10 row 2) x 16.1x T1 / 18.3x T2. Non-converter (Model 1); slice ROCE NOT FOUND, so entity base 18.3x without Pillar 3, so the slice and 3a do not pay for the same towers |
| 3. JSW Q3 wind over 300 MW | late Jan-2027 | RESOLVES-WITHIN-HOLD | JSW Energy Q3 FY27 disclosure | row 2 | 0.40 | FY27 PAT +Rs 12.67 Cr (my build; B10 "about +12"). A timing item: adds nothing to FY30 earnings, so 0 at exit |
| 4. CleanMax phase with Anawil towers | FY28 (phases by 31-Dec-2028) | RESOLVES-WITHIN-HOLD | Definitive agreement naming Karnataka sites and Anawil towers | row 6 | 0.25 | NOT FOUND (no phase signed, no Anawil share). Zero value: a slice with no sized value is not creditable |

Downside terms (not option slices; ledger rows D1-D3; probabilities are Claude Code proposals, NOT operator rulings): D1 115BAB denial (p 0.35), D2 Evren call-offs slip (p 0.30), D3 depreciation step-up (p 0.90; moot on the forward basis, already in the base).

Bear carries all four slices at FAILURE (A18.3). Role 3 standing question (A18.7): on a grade C management with timeline misses, slippage is the base case for dates. A one-year slip of slice 1 (to Jun-2028) or slice 2 (to end FY29) still resolves before the Nov-2029 exit. The exit price does not change; the FV path shifts by a year.

---

## SECTION 3: METHODS APPLIED

### 3.1 P/E (primary)

| Source | Exit PE range |
|---|---|
| Four-Pillar destination, Track 2 | 18.8x to 21.8x (mid 20.3x) |
| RRM-track destination, Track 1 | 14.9x to 17.3x (mid 16.1x) |
| Sector cap | 25x (not binding) |
| Applied | Track 1 governs; both carried |

Target price matrix, Year 3 (exit on FY30 EPS), core only (slices and the bear one-off excluded):

Track 1:

| | 14.9x | 16.1x | 17.3x |
|---|---|---|---|
| Bear EPS Rs 8.12 | Rs 121.0 -> -31.8% | Rs 130.7 -> -30.0% | Rs 140.5 -> -28.3% |
| Base EPS Rs 26.16 | Rs 389.8 -> 0.8% | Rs 421.2 -> 3.4% | Rs 452.6 -> 5.9% |
| Bull EPS Rs 35.80 | Rs 533.4 -> 11.9% | Rs 576.4 -> 14.8% | Rs 619.3 -> 17.6% |

Track 2:

| | 18.8x | 20.3x | 21.8x |
|---|---|---|---|
| Bear EPS Rs 8.12 | Rs 152.7 -> -26.3% | Rs 164.8 -> -24.4% | Rs 177.0 -> -22.5% |
| Base EPS Rs 26.16 | Rs 491.8 -> 8.9% | Rs 531.0 -> 11.7% | Rs 570.3 -> 14.4% |
| Bull EPS Rs 35.80 | Rs 673.0 -> 20.9% | Rs 726.7 -> 24.0% | Rs 780.4 -> 27.0% |

Colour key (green 25% or more, amber 15-25%, red under 15%): one of 18 cells is green, Track 2 bull EPS at 21.8x (27.0%). Every Track 1 cell is red except the bull at 17.3x (17.6%, amber).

Reverse-engineered entry (Track 1, base, mid): Year-3 target = 26.16 x 16.1 = Rs 421.2 core + Rs 23.2 EN-182 slice = Rs 444.4; required entry = 444.4 / 1.953125 = Rs 227.5.

P/E method Year-3 values (resolution-based, slices included): Track 1 bear Rs 118.9 (14.9 x 8.12 - 2.08 one-off tax a share), base Rs 444.4, bull Rs 724.0 (17.3 x 35.80 + 23.2 + 81.5). Track 2 bear Rs 150.6, base Rs 557.4 (20.3 x 26.16 + 26.4), bull Rs 899.4 (21.8 x 35.80 + 26.4 + 92.6).

### 3.2 EV/EBITDA (secondary)

| Factor | Assessment | Impact |
|---|---|---|
| Industry EV/EBITDA range | NOT FOUND (no live peer table) | none |
| PE destination -> implied EV/EBITDA at 0.6x | Track 1 16.1x -> 9.7x (8.9x to 10.4x); Track 2 20.3x -> 12.2x (11.3x to 13.1x) | 0.6x end chosen |
| Capex intensity | Capex Rs 93.01 Cr against D&A Rs 11.30 Cr (FY26); H1 FY27 53.39 against 12.87 | lower end |
| Check | Base FY30 PE-implied EV/EBITDA = (16.1 x 65.40 + 33.41) / 111.05 = 9.8x | consistent |

Year-3 values (exit on FY30 EBITDA; net debt Year 3 = Rs 33.41 Cr held, B7 NOT FOUND; slices added at their P/E-method value; bear also deducts the Rs 5.2 Cr one-off):

| | Bear | Base | Bull |
|---|---|---|---|
| FY30 EBITDA | 57.04 | 111.05 | 141.45 |
| Track 1 EV (8.9x / 9.7x / 10.4x) | 507.7 | 1,077.2 | 1,471.1 |
| Less net debt (and one-off) | 38.61 | 33.41 | 33.41 |
| Equity | 469.1 | 1,043.8 | 1,437.7 |
| Per share, core | Rs 187.6 | Rs 417.5 | Rs 575.1 |
| Plus resolved slices | 0 | +23.2 | +104.7 |
| **Track 1 per share** | **Rs 187.6** | **Rs 440.7** | **Rs 679.7** |
| Track 2 (11.3x / 12.2x / 13.1x) per share | Rs 242.4 | Rs 554.9 | Rs 846.8 |
| CAGR from Rs 381 (Track 1) | -21.0% | 5.0% | 21.3% |

### 3.3 Exit construction, dual display (A18.6; section-1b chunk 10)

Resolution-based exit (governs): bear = all slices FAILURE; base = slices at p 0.50 or more SUCCESS (EN-182), below 0.50 FAILURE (Kutch, JSW, CleanMax); bull = all sized slices SUCCESS. Static-carry exit: core plus each slice at p x resolved value.

| Track 1 P/E, Year 3 | Resolution-based | Static-carry | Delta per share |
|---|---|---|---|
| Bear | Rs 118.9 | Rs 163.1 | -44.2 |
| Base | Rs 444.4 | Rs 465.4 | -21.0 |
| Bull | Rs 724.0 | Rs 663.5 | +60.5 |

### 3.4 Method-wise fair value summary (Year 3, Track 1 governing; Track 2 in brackets)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E (Section 1B) | 70% | Rs 118.9 (150.6) | Rs 444.4 (557.4) | Rs 724.0 (899.4) |
| EV/EBITDA | 30% | Rs 187.6 (242.4) | Rs 440.7 (554.9) | Rs 679.7 (846.8) |

> Section 3 complete. All valuation methods applied.

---

## SECTION 4: TRIANGULATION, ENTRY AND VERDICT

### 4A. Triangulated fair value (Year 3, exit end FY29 on FY30 earnings)

Track 1 (RRM, governing):

| | Bear | Base | Bull |
|---|---|---|---|
| P/E x 70% | 118.9 x 0.7 = 83.2 | 444.4 x 0.7 = 311.1 | 724.0 x 0.7 = 506.8 |
| EV/EBITDA x 30% | 187.6 x 0.3 = 56.3 | 440.7 x 0.3 = 132.2 | 679.7 x 0.3 = 203.9 |
| **Weighted FV** | **Rs 139.5** | **Rs 443.3** | **Rs 710.7** |

Track 2 (additive):

| | Bear | Base | Bull |
|---|---|---|---|
| P/E x 70% | 150.6 x 0.7 = 105.4 | 557.4 x 0.7 = 390.2 | 899.4 x 0.7 = 629.6 |
| EV/EBITDA x 30% | 242.4 x 0.3 = 72.7 | 554.9 x 0.3 = 166.5 | 846.8 x 0.3 = 254.0 |
| **Weighted FV** | **Rs 178.1** | **Rs 556.6** | **Rs 883.6** |

### 4B. Methods agreement

| Check | Result |
|---|---|
| Same direction? | Yes in base and bull (within 1% and 6%) |
| Spread, highest to lowest | Base 0.8%; bull 6.5%; bear 57.8% |
| Outlier above 30% | EV/EBITDA in the bear. D&A of Rs 25.73 Cr is 45% of bear EBITDA, and the 115BAB denial hits PAT, not EBITDA. EV/EBITDA overstates when depreciation is heavy |
| Most trusted for this company | P/E: it carries the depreciation step-up and the tax dispute the business actually bears |

### 4C. Return at current price (Rs 381)

| Scenario | Track 1 FV | CAGR | Track 2 FV | CAGR | Meets 25%? |
|---|---|---|---|---|---|
| Bear | Rs 139.5 | -28.5% | Rs 178.1 | -22.4% | No |
| Base | Rs 443.3 | 5.2% | Rs 556.6 | 13.5% | No |
| Bull | Rs 710.7 | 23.1% | Rs 883.6 | 32.4% | No on Track 1; yes on Track 2 bull only |

### 4D. Probability-weighted expected return (grade C, section-1b chunk 17)

Weights from B10.credibility_grade C (Mixed): 35 / 45 / 20. Grade period: under four quarters (about one half-year since listing), stated per Rule E. The re-weighting rule (below bear on 2+ metrics for 2 quarters) has no history to test.

| Scenario | Probability | Track 1 CAGR | Weighted | Track 2 CAGR | Weighted |
|---|---|---|---|---|---|
| Bear | 35% | -28.5% | -10.0% | -22.4% | -7.8% |
| Base | 45% | 5.2% | 2.3% | 13.5% | 6.1% |
| Bull | 20% | 23.1% | 4.6% | 32.4% | 6.5% |
| **Expected CAGR** | 100% | | **-3.0%** | | **4.7%** |

Probability-weighted EPS CAGR (A21/A22, the Hurdle input): 17.3%.

### 4.A24 Price decomposition at Rs 381 (section-1b chunk 08)

Tier multiple = governing Section 1B destination, Track 1 16.1x (operator-approved). Step 1C cross-check: PENDING LIVE PEER TABLE.

| Tier | Earnings (Rs Cr PAT) | Rs Cr | Rs / share | % of CMP |
|---|---|---|---|---|
| T1 Confirmed (A21 base 43.33 x 16.1) | 43.33 | 697.6 | 279.0 | 73.2% |
| T2 High-probability: row 1 +1.80, net of D1 -1.53 and D2 -4.05 | -3.78 | -60.9 | -24.4 | -6.4% |
| T3 Speculative: row 2 +5.06, row 3 +5.07, row 4 0 | +10.13 | 163.1 | 65.2 | 17.1% |
| Residual (unsupported) | | 152.8 | 61.1 | 16.0% |
| Total | | 952.5 | 381.0 | 100% |

- Verdict as four numbers: **T1 73.2% | T2 -6.4% | T3 17.1% | residual 16.0%.**
- Starter test (A25): T1 + T2 = 66.8%, below 75%: **FAILS.** Residual 16.0%, under 25%: passes. The starter test passes on Track 1 at a price of Rs 339 or lower (T1 + T2 = Rs 636.6 Cr = 75% of a Rs 848.9 Cr market cap).
- Without D2 (an unruled proposal): T2 +0.27, T1 + T2 = 73.6%, still below 75%.
- Track 2 (20.3x, sensitivity): T1 92.3% | T2 -8.1% | T3 21.6% | residual -5.9%; T1 + T2 = 84.3% passes.
- Note: rows 3 and D2 are one-year timing items. Capitalising them at 16.1x follows the A24 mechanics. A strict one-off reading would move about Rs 6 a share of net value out of T2/T3 into the residual.
- Position size is set to T1 + T2 (A24). T3 is the disclosed bet.

### 4E. Entry price (section-1b chunk 06; OR-8)

| Calculation | Track 1 (governs) | Track 2 |
|---|---|---|
| Base case FV, Year 3 (exit-consistent, forward FY30) | Rs 443.3 | Rs 556.6 |
| Price for the 25% hurdle = FV / 1.25^3 (1.953125) | Rs 227.0 | Rs 285.0 |
| FV CAGR and return-source label (A19) | 12.3% HYBRID | 12.5% HYBRID |
| Price for 30% CAGR = FV / 2.197 | Rs 201.8 | Rs 253.3 |
| Margin of safety price | Fast-growth name (A25; OR-12: forward Revenue FIRING): margin of safety is position size, not a price haircut. Evidence-scaled reference only (mixed evidence, 30%): 227.0 x 0.70 = Rs 158.9 | Rs 199.5 reference |
| **Ideal entry range** | **Rs 202 to Rs 227** | Rs 253 to Rs 285 |

CMP Rs 381 sits 68% above the top of the Track 1 zone. The zone also sits below the 52-week low of Rs 313. Reaching it needs an event, most likely an H2 FY27 miss, not drift. On base earnings no permitted multiple clears 25% at Rs 381: the Year-3 value would need 27.6x FY30 EPS, above the 25x cap. Rs 381 clears 25% only on bull earnings (FY30 EPS Rs 35.80 with both slices resolved) at 17.9x or more.

### 4.A19 Fair-value path, FV CAGR, return-source label (section-1b chunk 12)

Governing Track 1, base case. Today carries slices at p x value, discounted at r 14.5% to their resolution dates (A18.5). Net debt held at Rs 33.41 Cr.

| Point | Earnings basis | Core (16.1x) | Slices and downside terms | FV |
|---|---|---|---|---|
| Today (17-Nov-2026) | FY27 EPS Rs 17.33 | Rs 279.0 | EN-182 +10.7; Kutch +27.1; JSW +31.8; D1 -9.9; D2 -24.8 | **Rs 313.8** |
| End Year 1 (Nov-2027) | FY28 EPS Rs 17.36 | Rs 279.5 | EN-182 resolved SUCCESS +23.2; Kutch unresolved +31.0; D1, D2, JSW resolved, 0 | Rs 333.7 |
| End Year 2 (Nov-2028) | FY29 EPS Rs 20.29 | Rs 326.7 | EN-182 +23.2; Kutch resolved FAILURE 0 | Rs 349.9 |
| End Year 3 (Nov-2029, exit) | FY30 EPS Rs 26.16 | Rs 421.2 | EN-182 +23.2 | **Rs 444.4** |

- "FV CAGR over the hold: 12.3% (today Rs 313.8 to end-Year-3 Rs 444.4, governing track, base case)."
- Return-source label: **HYBRID** (10-20%). Track 2 cross-check: Rs 391.2 to Rs 557.4, 12.5%, HYBRID.
- Decomposition line: the core compounds at 14.7% a year (EPS Rs 17.33 to Rs 26.16 at a constant 16.1x). Rs 34.8 of today's Rs 313.8 (11%) is static slice and timing value, and the Kutch part (Rs 27.1) decays to zero in the base when it resolves as FAILURE. The fade drag is the flat FY28. No re-rating lever remains: at 22.0x the price already sits 27% above the 16.1x destination, so a de-rating is embedded.
- FV-step events (per share, at each resolution date, no discounting, no new probabilities):
  - EN-182 order by 30-Jun-2027: SUCCESS +11.6; FAILURE -11.6.
  - Kutch approval and fill by 31-Mar-2028: SUCCESS +48.9; FAILURE -32.6.
  - JSW Q3 FY27 disclosure, late Jan-2027: SUCCESS +49.0, FAILURE -32.6, both transient. They unwind when the basis rolls to FY28 in April 2027.
  - D1 order at the FY27 results, May-2027: fired -19.7; not fired +10.6.
  - D2 Evren call-offs by 31-Mar-2027: slip -60.9; on time +26.1, both transient on the same roll.

### 4F. Risk-reward (Track 1; Track 2 in brackets)

| | Value |
|---|---|
| Bull target, Year 3 | Rs 710.7 -> +86.5% (Rs 883.6, +131.9%) |
| Base target, Year 3 | Rs 443.3 -> +16.4% (Rs 556.6, +46.1%) |
| Bear floor, Year 3 | Rs 139.5 -> -63.4% (Rs 178.1, -53.3%) |
| Upside (base) / downside (bear) | **0.26x** (0.87x). Below the 2x line: FAIL |

### 4G. Exit multiple validation

| Check | Result | Pass? |
|---|---|---|
| Year 3 ROCE justifies the ROCE base and matches FTTCP? | FY29 base ROCE 17.7% against the 21.61% Pillar 1 input and a FIRING verdict | FAIL. Year-3-consistent Pillar 1 = 16.4x base, Track 1 14.4x (1B.9). Approved base governs; reported |
| Year 3 CFO/PAT justifies the cash multiplier? | Mechanical CFO/PAT above 1 on WC Rs 18.2 lakh a tower; determination INDETERMINATE | INDETERMINATE |
| Primary catalyst fired by Year 3 in the base? | Proof gate (H2 FY27 towers 206 or more) does NOT fire in the base (140 H2 towers). Kutch resolves FAILURE in the base | No: the base values the R2 business, not the transition |
| Strategic premium still justified, single credit? | +0x; ROCE recovery in Pillar 1 only | PASS |
| UA ordering min(F x 1.25, cap)? | UA not applied; min(20.3, 25) = 20.3x | PASS |
| Would you buy another stock at this exit PE with similar Year 3 metrics? | At 16.1x for 17-19% ROCE, grade C, INDETERMINATE cash: yes. At 20.3x: no | PASS on Track 1 only |

The first check fails. The framework says revise the exit PE downward. The operator-approved base binds and the deliberation forbids a silent change, so I report the revision as a sensitivity (Track 1 14.4x, entry about Rs 205 on the P/E method) and keep 16.1x governing. The operator should rule on it.

### 4H-pre. Mandatory conclusion elements

1. **Value vs price.** Line one: the business is worth about Rs 314 a share today on the governing track (16.1x FY27 base EPS Rs 17.33, plus probability-weighted slices). The single most important driver is tower volume after the order book runs out in Q1 FY28. Line two: at Rs 381 the price is 22.0x forward base EPS and assumes about 27% EPS growth a year to earn its cost of capital at the 16.1x destination, against 17.3% probability-weighted evidence. The Market-Implied block is NOT FOUND; my PE-gap reading is PRICED-WE-ARE-LATE, and the recognition gap is CLOSED. What closes the gap: the H2 FY27 print (about May-2027) firing the proof gate (206 or more H2 towers, Rs 33 lakh or more a tower with Model 3 above 50%), Kutch approval (first read about 15-Dec-2026), and new orders by 31-Mar-2027. Or a price at or below Rs 339 (starter test) or Rs 202-227 (entry zone).
2. **Margin of safety.** Fast-growth name (A25, OR-12): margin of safety = position size. Price-based row for reference: mixed evidence (B07 13 documented / 6 claim / 6 inference) gives 30%; catalyst inside 12 months.
3. **Dispersion sizing.** Width = (710.7 - 139.5) / 443.3 = 128.9% (Track 2: 126.8%). Above 80%: position capped at **Small**, regardless of conviction.
4. **Edge.** "Edge claimed: PROCESS, because the pipeline rebuilt the order book in towers from filings: the 48-tower inflow since March equals the two filed orders; about 292 of the 320 book units are real towers; the deck's Rs 32.82 lakh 'EBITDA per tower' is a cash-flow subtotal. None of these sits in the company's headline numbers."

### 4H. VALUATION VERDICT CARD

| Field | Value |
|---|---|
| **Tier** | **Tier: A \| Hurdle: 25%** |
| CMP / market cap | Rs 381.0 (17-Nov-2026, screener via orchestrator, RL line 22) / Rs 952.49 Cr. B10: Rs 391, Rs 977.0 Cr (12-Nov-2026) |
| CONVERTER classification (A17) | Model 3 CONVERTER (OR-6, steel clause NOT FOUND); Models 1 and 2 NON-CONVERTER; volume test: WC per tower moved, input-price fork closed |
| ROCE base | FTTCP ROCE forward FIRING (operator Ruling 2); ROCE used 21.61% (operator midpoint method; FLAG-FRAMEWORK-CONFLICT) -> 18.3x |
| Cash multiplier | 1.00x, INDETERMINATE (structural 0.65x reading: Track 1 10.5x) |
| Quality base | 18.3x |
| Growth premium | +2x (3a; EM 10.8 NONE; catalyst 0-12 months; mixed evidence; A16 YES from FY27; SHARED CATALYST) |
| Strategic | +0x; ROCE recovery via Pillar 1 only |
| Raw PE / UA / cap | 20.3x / UA N / 25x Cables-Industrial, no uplift, no override |
| **Track 2 destination** | **20.3x (18.8x to 21.8x)** |
| **Track 1 destination (governs)** | **16.1x (14.9x to 17.3x); r 14.5%, RRM 0.88** (17.2x if the Darpan check clears) |
| Sensitivity lines | Stage 11 FY28 ROCE 17.64% (recorded 19.76%) -> approved method 17.8x base / 19.8x / 15.7x. Section 1B FIRING rule: 19.2x / 21.2x / 16.9x |
| Earnings basis | Forward: entry FY27 EPS Rs 17.33; exit FY30 EPS Rs 26.16 (exit year FY29) |
| Hurdle Ratio | Track 1 1.18 (bull 1.34); Track 2 1.49 (bull 1.69): **STOP band** on both, on probability-weighted EPS CAGR 17.3% (bull = base + 5 pp, grade C). Caps no verdict (OR-2) |
| Methods | P/E 70%, EV/EBITDA 30% |
| Weighted FV Year 3, Track 1 | Bear Rs 139.5 \| Base Rs 443.3 \| Bull Rs 710.7 |
| Weighted FV Year 3, Track 2 | Bear Rs 178.1 \| Base Rs 556.6 \| Bull Rs 883.6 |
| FV today (governing) | Rs 313.8 (Track 2 Rs 391.2) |
| **FV CAGR** | **12.3% HYBRID** (Track 2 12.5% HYBRID) |
| Expected CAGR (4D, grade C weights 35/45/20) | Track 1 -3.0%; Track 2 4.7%. Probability-weighted EPS CAGR 17.3% |
| Upside / downside | 0.26x (Track 2 0.87x) |
| Entry range / MoS | **Rs 202 to Rs 227** (Track 1). MoS = position size (A25); reference price Rs 159 |
| Step 1C | Pillar destination 16.1x \| adjusted peer base PENDING LIVE PEER TABLE \| gap n/a \| governing: pillar (relative only if peer base above 23.0x, capped 25x) |
| **Price decomposition (A24)** | **T1 73.2% \| T2 -6.4% \| T3 17.1% \| residual 16.0%**. Starter test FAILS (T1 + T2 66.8% below 75%); passes at Rs 339 or lower |
| Recognition gap | **CLOSED**: current PE 22.0x forward / 19.8x trailing already at or above the R3 neighbourhood (about 19x). Re-rating engine spent; return rides EPS growth against a 27% de-rating to 16.1x |
| Transition posture | Proof NOT FIRED + ARTIFACT (provisional) + gap CLOSED = PRICED NARRATIVE (TRAP) |
| Value vs price | Worth about Rs 314 today on the governing track; volume after Q1 FY28 drives it. The price assumes about 27% EPS growth to earn its cost of capital at 16.1x against 17.3% evidence: PRICED-WE-ARE-LATE (Market-Implied block NOT FOUND). Closed by the May-2027 proof gate and Kutch approval, or by a price at or below Rs 339 |
| Margin of safety row | A25 fast-growth: size, not price. Reference row: mixed evidence, 30% |
| Dispersion sizing | 128.9% -> **Small** cap |
| Edge | PROCESS (tower-level order-book reconstruction from filings) |
| FTTCP | Composite 4 of 8 (DEEP WATCH leaning BUY-ON-DIPS); disposition PROCEED WITH CAVEATS (cash INDETERMINATE) |
| **DECISION** | **WATCHLIST, on valuation. Hard watch, no position.** Bands: no position above Rs 339; starter test met at Rs 339 or lower (Small, 2-3%, if the operator rules OR-9 that way); entry zone Rs 202 to Rs 227. Decision stays with the operator |
| Key assumptions | ▲ Steel clause pass-through -> NON-CONVERTER, Track 1 18.4x, entry about Rs 260. ▲ Darpan check clears -> r 14.0%, Track 1 17.2x, entry about Rs 243. ▲ Order inflow at the trailing pace (34 towers or more by 31-Mar-2027) -> FY28 about 258 towers or more; the A14 path (share held) gives FY30 EPS Rs 35.48, Year-3 core Rs 571. ▲ Kutch approved and filling -> +Rs 48.9 a share step; ROCE FIRING confirmed. ▼ Cash structural -> Pillar 2 0.65x, Track 1 10.5x, entry about Rs 148. ▼ No new orders -> FY28 196 towers (bear path). ▼ 115BAB denied -> tax +8.0 pp, -Rs 19.7 a share step. ▼ EM NONE exit haircut (not applied, for ruling) -> Track 1 15.1x, entry about Rs 214. ▼ Kutch not approved by 31-Mar-2027 -> ROCE verdict STAGNANT (composite 2 of 8) |
| Exit framework | Target exit: Year-3 Track 1 base Rs 443. Thesis-broken: EBITDA per tower below Rs 29 lakh with Model 3 above 50%; a conversion order below Rs 58.7 lakh a tower; Customer A above 40% of the book or the book falling; FY27 operating cash flow below 50% of EBITDA (structural). Time stop: proof gate not fired by the H1 FY28 print (about Nov-2027) -> full re-run. PE compression floor: Track 1 low 14.9x; structural-cash case 10.5x |
| One-line thesis | Not buying ANAWIL at Rs 381: base EPS grows from Rs 17.33 (FY27) to Rs 26.16 (FY30) on order-book then industry-paced tower volume, at a four-pillar Track 1 destination PE of 16.1x (ROCE 21.61%, cash 1.00x, EM 10.8, sector cap 25x) = Rs 443 Year-3 target = 5.2% CAGR. Key risk: no order book beyond Q1 FY28 and towers lost to OEMs that build their own. Cash quality: INDETERMINATE |

> Valuation complete. Four-pillar exit PE of 18.8x to 21.8x (Track 2) and 14.9x to 17.3x (Track 1, governs). Hurdle Ratio STOP band (caps no verdict). Entry price: Rs 202 to Rs 227. Decision: WATCHLIST (no position).

---

## EXPECTATION LEDGER

Written to runs/anawil-2026-11-12/outputs/expectation-ledger.md (Appendix A schema).

"Ledger: 9 items (T2 1, T3 3 with one unsized, downside 3, base-case confirm rows 2) | prob-weighted T2 net Rs -3.78 Cr | T3 Rs 10.13 Cr | items past confirm-by: 0 (status all OPEN)."

---

## UNRESOLVED INPUTS USED (override 3)

1. INPUT UNRESOLVED: cash conversion, structural or growth-induced. Assumption used: 1.00x, because the operator approved it (Ruling 4) and no multiplier exists for INDETERMINATE (OR-5). Both readings: structural 0.65x (Track 1 10.5x) / growth-induced 0.80x + 0.20 = 1.00x. Separating observation: FY27 operating cash flow against EBITDA (70% or more vs below 50%) with receivables and inventory days. Confirm-by: FY27 audited statements, about Sep-2027.
2. INPUT UNRESOLVED: Darpan r adjustment. Assumption used: r 14.5%, because the operator approved it (Ruling 4). Both readings: 14.5% (Track 1 16.1x) / 14.0% (17.2x). Separating observation: Claude web Darpan check (Ruling 7). Confirm-by: before /finalize.
3. INPUT UNRESOLVED: numeric r table and the Track 1 base definition. Assumption used: RRM on the quality-adjusted base, governance adj 0, because the operator approved r and repo precedent defines the base. Both readings: as used / a non-zero governance adjustment (promoter CAUTION). Separating observation: an operator ruling. Confirm-by: operator, open.
4. INPUT UNRESOLVED: peer medians / live peer table. Assumption used: pillar destination governs, because no live table is injected (Correction 6). Both readings: pillar governs / relative governs if the adjusted peer base exceeds 23.0x. Separating observation: the Claude web Step 1C table. Confirm-by: before /finalize.
5. INPUT UNRESOLVED: Model 3 steel clause and slice ROCE/WC. Assumption used: CONVERTER, because OR-6 defaults ambiguity to CONVERTER. Both readings: converter (18.3x base) / non-converter (26.79% -> 20.9x base, Track 1 18.4x). Separating observation: the 9-Nov-2026 transcript or an IR reply (tracker row 5). Confirm-by: when the transcript is filed.
6. INPUT UNRESOLVED: guided margin band. Assumption used: EBITDA per tower Rs 33.72 lakh (H1 FY27), because it is the latest print. Both readings: per-tower holds / falls toward Rs 29 lakh. Separating observation: H2 FY27 per-model revenue and cost. Confirm-by: about May-2027.
7. INPUT UNRESOLVED: October 2026 dispatches (FY28 book left). Assumption used: floor of 196 towers for the bear, because the floor needs no estimate. Both readings: 196 / higher if October dispatches sat outside the book. Separating observation: the H2 FY27 deck tower count by month. Confirm-by: about May-2027.
8. Not used: TTM CFO / FCF / P/FCF (no cash-flow method); H2 FY25 PAT (forward basis); FY23 ROCE/WC (not needed).

## INPUTS TAKEN FROM OUTSIDE B10 (input-discipline note)

B10 is the sole input table, but it does not carry these. Each is a filed or stage-block figure with its anchor, used as a named input:
- Industry growth anchor: wind roadmap 8 / 9 / 10 / 12 / 13.2 GW (B09 tam_growth_pct note; MNRE/IWTMA roadmap). Named assumption per A18.0.
- Capacity 612 towers (Koppal 420, Kutch 192) (B05; H1 deck p.18; PR p.3); 474 t tonnage limit about 437 towers (B03).
- Order inflow Rs 189.73 Cr / 48 towers since March 2026 (B03; 12b R21); March book Rs 359.82 Cr / 379 towers (Pros p.114).
- LOIs Rs 44.05 Cr, 44 towers (B07; Pres p.7).
- H1 FY27 tax lines (H1R p.4), checked against the page-marked results text.
- FTTCP Part B and FD tables 2.1 to 3.5 (the deliberation's stated input source).

## NAMED LIMITATIONS (DLB Ruling 7) AND OTHER GAPS

- Darpan Infrastructure check pending (moves r by 0.5). Model 3 steel clause NOT FOUND. 9-Nov-2026 call transcript not filed.
- Debt Capacity block and Market-Implied block NOT FOUND (not run).
- Capex plan NOT FOUND: FCF and net debt paths NOT FOUND; net debt held at Rs 33.41 Cr.
- Macro sheet stale (August 2026; next refresh was 1-Sep-2026).
- Live price fetched by the orchestrator, not by this stage.
- Downside probabilities D1-D3 are Claude Code proposals, not operator rulings.
- OR-9 (starter size under A24/A25: zero or 2-3%) is open; the starter test fails here in any case.
- EM NONE exit haircut (A18.0) not addressed by the deliberation; shown as a sensitivity, not applied, for operator ruling.

## FLAGS

- FLAG-CASH: INDETERMINATE; 1.00x applied; caps the gate verdict at PROCEED WITH CAVEATS; missing evidence named in 1B.2.
- FLAG-FRAMEWORK-CONFLICT: operator midpoint method overrides the chunk 01 FIRING rule; carried.
- FLAG-ROCE-PATH: base ROCE falls 26.9% -> 21.8% -> 17.6% -> 17.7%; inconsistent with FIRING; stage 11 FY28 ROCE 17.64% against 19.76%.
- FLAG-4G-ROCE: Year 3 ROCE fails the 4G check; approved base kept.
- FLAG-RECOGNITION-GAP: CLOSED; posture PRICED NARRATIVE (TRAP).
- FLAG-HURDLE: STOP band, both tracks; caps no verdict.
- FLAG-STARTER-FAIL: T1 + T2 66.8% (Track 1); passes at Rs 339 or lower.
- FLAG-DISPERSION: 128.9%, Small cap.
- FLAG-UPDOWN: 0.26x, below 2x.
- FLAG-SHARED-CATALYST: Kutch (FIRING label, 3a capacity, slice) and the order book (base revenue, 3a). Role 3 stress test.
- FLAG-EXIT-HAIRCUT: EM NONE haircut not applied; for ruling.
- FLAG-MACRO-STALE, FLAG-PRICE (Rs 381 vs B10 Rs 391), FLAG-DOWNSIDE-UNRULED, FLAG-GATE0 (AVERAGE, THIN), FLAG-KUTCH-CONTRADICTION, FLAG-PROVISIONAL (carried from B10).

---

```yaml
stage: B11-valuation
company: "ANAWIL"
run_date: "2026-11-12"
model: "claude-opus-5-5"
status: complete
entity: "consolidated single-entity"
entity_count: 1
input_gaps:
  - "No annual report; 9-Nov-2026 call transcript not filed (named limitation, Ruling 7)"
  - "Debt Capacity Assessment block NOT FOUND; FTTCP B7 Year 3 net debt NOT FOUND; net debt held at Rs 33.41 Cr (H1R p.7)"
  - "Market-Implied Assumptions block NOT FOUND; recognition gap resolved from the PE gap"
  - "Live peer table absent: Step 1C PENDING LIVE PEER TABLE"
  - "Capex plan NOT FOUND: FCF and net debt projections NOT FOUND"
  - "Model 3 steel clause, slice ROCE and WC NOT FOUND; A17.3 5-year median spread NOT FOUND (stand-in Rs 25.6 lakh a tower, median of printed series)"
  - "October 2026 dispatches NOT FOUND; realistic peak utilisation and plant-wise tonnage NOT FOUND"
  - "Industry growth anchor not on B10: wind roadmap 8/9/10/12/13.2 GW from B09, named assumption"
  - "Live price fetched by orchestrator (stage 11 has no web tools): Rs 381, 17-Nov-2026, run-log.md Phase 3"
  - "macro-sheet.md stale (August 2026; next refresh 1-Sep-2026)"
  - "Numeric r table and Track 1 base definition NOT FOUND in frameworks"
flags:
  - {type: FLAG-CASH, reason: "Cash INDETERMINATE (operator Ruling 5). Pillar 2 multiplier applied 1.00x (operator Ruling 4; OR-5). Structural 0.65x reading gives Track 1 10.5x, Track 2 13.9x. Caps the gate verdict at PROCEED WITH CAVEATS. Missing: customer-wise ageing 31-Mar-2026 and 30-Sep-2026; Rs 30.04 Cr capital advances; revenue, cost and WC by model per half; Model 3 payment terms and steel clause; FY27 audited cash flow."}
  - {type: FLAG-FRAMEWORK-CONFLICT, reason: "Operator Pillar 1 method (midpoint 21.61%) overrides chunk 01 FIRING rule (current 23.45%, 19.2x / 21.2x / 16.9x). Carried, approved base governs."}
  - {type: FLAG-ROCE-PATH, reason: "Stage 11 base ROCE 21.76% FY27, 17.64% FY28, 17.72% FY29, 19.28% FY30. FY28 17.64% vs recorded 19.76% gives approved-method base 17.8x, Track 2 19.8x, Track 1 15.7x (sensitivity). Base path inconsistent with ROCE FIRING, which rests on Kutch (excluded from base by single credit)."}
  - {type: FLAG-4G-ROCE, reason: "4G check fails: Year 3 ROCE 17.7% below the 21.61% Pillar 1 input. Year-3-consistent Track 1 14.4x shown as sensitivity; approved 16.1x kept (no silent override of the operator base)."}
  - {type: FLAG-RECOGNITION-GAP, reason: "CLOSED. Current PE 22.0x forward (FY27 base EPS Rs 17.33) / 19.8x trailing, at or above the R3 neighbourhood (about 19x) and above both destinations. Posture: PRICED NARRATIVE (TRAP). Return rides EPS growth against a 27% de-rating to 16.1x."}
  - {type: FLAG-HURDLE, reason: "STOP band on both tracks: Track 1 HR 1.18 (bull 1.34), Track 2 1.49 (bull 1.69), threshold 1.953, on probability-weighted EPS CAGR 17.3%. Caps no verdict (OR-2)."}
  - {type: FLAG-STARTER-FAIL, reason: "A25 starter test fails on governing Track 1: T1 + T2 = 66.8% of CMP (below 75%); residual 16.0%. Passes at Rs 339 or lower. OR-9 open."}
  - {type: FLAG-DISPERSION, reason: "FV range width 128.9% (Track 2 126.8%): position capped at Small."}
  - {type: FLAG-UPDOWN, reason: "Upside/downside 0.26x on Track 1 (0.87x Track 2), below 2x."}
  - {type: FLAG-SHARED-CATALYST, reason: "Kutch supports the ROCE FIRING label, the Pillar 3 capacity test and the p 0.4 slice; Kutch rupees counted once (slice; Track 2 slice valued at 18.3x without Pillar 3). Order book sits in base revenue and in the 3a qualifier; strict single credit would set 3a +0x, Track 2 18.3x; Track 1 unaffected. Role 3 stress test."}
  - {type: FLAG-EXIT-HAIRCUT, reason: "EM NONE is the typical A18.0 trigger for a minus-one-turn exit haircut. Not applied: the Year 4-5 industry-growth story is evidenced (B09 roadmap; Koppal headroom). Deliberation silent. Sensitivity Track 1 15.1x, Track 2 19.3x. Operator to rule."}
  - {type: FLAG-PRICE, reason: "CMP Rs 381 (17-Nov-2026 screener close, orchestrator fetch, run-log.md Phase 3) used; B10 Rs 391 (12-Nov-2026) shown beside."}
  - {type: FLAG-MACRO-STALE, reason: "macro-sheet.md is the August 2026 fill; next refresh 1-Sep-2026 has passed."}
  - {type: FLAG-DOWNSIDE-UNRULED, reason: "Ledger D1-D3 probabilities (0.35 / 0.30 / 0.90) are Claude Code proposals, not operator rulings."}
  - {type: FLAG-GATE0, reason: "Carried: Gate 0 AVERAGE, core 66, grand 71, moat THIN (B01)."}
  - {type: FLAG-KUTCH-CONTRADICTION, reason: "Carried: Pros p.232 'commenced March 2026, 16 towers' vs PR 2026-11-06 p.3 'trial runs underway'."}
  - {type: FLAG-PROVISIONAL, reason: "Carried: card provisional on cash INDETERMINATE, steel clause NOT FOUND, slice ROCE/WC NOT FOUND, r table NOT FOUND, Darpan check pending."}
framework_versions: "Master v3.7 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9+v3.10 / FTTCP v2.3"
pe_basis: "forward"   # entry FY27 EPS; exit year FY29, exit EPS FY30 (Amendment 18.1; operator Ruling 1)
exit_pe_base_approved: "Pillar 1 base 18.3x (ROCE input 21.61%) x Pillar 2 1.00x + Pillar 3 +2x + strategic 0 = 20.3x Track 2 (18.8x-21.8x); Track 1 RRM r 14.5% = 16.1x (14.9x-17.3x; 17.2x on r 14.0%); Track 1 sets entry zone (OR-1); sector cap 25x not binding. Deliberation Ruling 4, SIGNED OFF 2026-11-17."
destination_pe:
  track1_rrm: {low: 14.9, mid: 16.1, high: 17.3, r_used: 14.5, rrm: 0.88}
  track2_additive: {low: 18.8, mid: 20.3, high: 21.8}
  divergence_pct: 26
  governing_track: "Track 1 (RRM): the more conservative track sets the entry zone (OR-1 as written, operator Ruling 4); it also fits best, carrying no Pillar 3 paid twice for the order book and sitting in the R2 converter neighbourhood the business occupies on evidence"
pillar_detail:
  roce_used: 21.61
  roce_base: 18.3
  roce_recovery_route: "pillar1-midpoint"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.00
  structural_or_growth: "INDETERMINATE (operator Ruling 5); 1.00x volatile-band neutral as approved (equal to growth-induced 0.80 + 0.20); structural 0.65x shown"
  growth_offset: 0
  growth_premium: 2
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 1.18, bull_used: false, verdict: "STOP"}   # Track 1; bull row = base + 5 pp (grade C) gives 1.34; Track 2 1.49 / 1.69; caps no verdict
run_rate_base:
  basis: "full-year FY27 forward scenario (seasonal half-yearly filer; operator Ruling 1; neither single-quarter-annualised nor trailing-4q)"
  pat_run_rate_cr: 43.33
  one_offs_adjusted: "Other income Rs 0.22 Cr stripped (operating earnings, FTTCP B4); Section 115BAB back-tax about Rs 5.2 Cr for FY24-FY26 kept out of earnings (D1, bear equity bridge); H1 not annualised; H2 at the HD V5 JSW-lag reading with JSW pull carried as T3"
  annual_model_divergence_pct: -9.9   # vs TTM PAT Rs 48.09 Cr; +20.5% vs FY26 audited Rs 35.95 Cr (floor)
price_decomposition:
  t1_confirmed: {rs_cr: 697.6, rs_per_share: 279.0, pct_cmp: 73.2}
  t2_high_prob: {rs_cr: -60.9, rs_per_share: -24.4, pct_cmp: -6.4}
  t3_speculative: {rs_cr: 163.1, rs_per_share: 65.2, pct_cmp: 17.1}
  residual: {rs_cr: 152.8, rs_per_share: 61.1, pct_cmp: 16.0}
  step1c_peer_base_crosscheck: "PENDING LIVE PEER TABLE (relative would govern only if adjusted peer base exceeds 23.0x, capped 25x)"
  governing_multiple: "pillar (Track 1 16.1x, operator-approved)"
fair_values:   # Year 3 (exit end FY29 on FY30 EPS), triangulated P/E 70% / EV-EBITDA 30%, resolution-based slices; today governing FV Rs 313.8 (Track 2 Rs 391.2)
  track1: {bear: 139.5, base: 443.3, bull: 710.7}
  track2: {bear: 178.1, base: 556.6, bull: 883.6}
expected_cagr_prob_weighted: 17.3   # probability-weighted EPS CAGR on the A21 base (Hurdle input, wrapper rule); 4D expected price CAGR at Rs 381: Track 1 -3.0%, Track 2 4.7%
entry_range: {low: 202, high: 227}   # Track 1: 30% CAGR price to 25% hurdle price; FV CAGR 12.3% HYBRID
mos_price: 159   # reference only (mixed evidence 30%); A25 fast-growth: margin of safety is position size, not a price haircut
upside_downside_ratio: 0.26
decision: "WATCHLIST (on valuation): hard watch, no position. CMP Rs 381 is 21% above today's governing FV Rs 313.8 and 68% above the Track 1 entry zone Rs 202-227; A25 starter test met only at Rs 339 or lower; recognition gap CLOSED, posture PRICED NARRATIVE (TRAP). Decision stays with the operator."
unresolved_inputs_used:
  - {field: "cash structural vs growth-induced", assumption: "1.00x (operator Ruling 4; OR-5)", readings: "structural 0.65x -> Track 1 10.5x / growth-induced 0.80+0.20 = 1.00x -> 16.1x", separating_observation: "FY27 CFO at or above 70% of EBITDA with receivables under 60 days and inventory under 90 days, vs below 50%", confirm_by: "FY27 audited statements, about Sep-2027"}
  - {field: "Darpan r adjustment", assumption: "r 14.5% (operator Ruling 4)", readings: "14.5% -> 16.1x / 14.0% -> 17.2x", separating_observation: "Claude web Darpan check (Ruling 7)", confirm_by: "before /finalize"}
  - {field: "numeric r table and Track 1 base definition", assumption: "RRM on quality-adjusted base, governance adj 0 (repo precedent; operator r)", readings: "as used / non-zero governance adjustment for promoter CAUTION", separating_observation: "operator ruling", confirm_by: "open"}
  - {field: "peer medians / live peer table", assumption: "pillar destination governs (Correction 6)", readings: "pillar governs / relative governs if adjusted peer base above 23.0x (cap 25x)", separating_observation: "Claude web Step 1C table", confirm_by: "before /finalize"}
  - {field: "Model 3 steel clause and slice ROCE/WC", assumption: "CONVERTER (OR-6)", readings: "converter 18.3x base / non-converter 26.79% -> 20.9x base, Track 1 18.4x", separating_observation: "9-Nov-2026 transcript or IR reply (tracker row 5)", confirm_by: "when the transcript is filed"}
  - {field: "guided margin band", assumption: "EBITDA per tower Rs 33.72 lakh (H1 FY27)", readings: "per-tower holds / falls toward Rs 29 lakh", separating_observation: "H2 FY27 revenue and cost by model", confirm_by: "about May-2027"}
  - {field: "October 2026 dispatches (FY28 book left)", assumption: "bear floor 196 towers (no estimate needed)", readings: "196 / higher if October dispatches sat outside the 31-Oct book", separating_observation: "H2 FY27 deck tower count", confirm_by: "about May-2027"}
som_cagr_crosscheck: "consistent: base revenue CAGR 37.4% FY26-FY29 and 27.9% FY26-FY31 sit below SOM-implied 49.3% (yr3) and 35.1% (yr5)"
one_line_thesis: "Not buying ANAWIL at Rs 381: base EPS grows from Rs 17.33 (FY27) to Rs 26.16 (FY30) on order-book then industry-paced tower volume, at a Track 1 destination PE of 16.1x (ROCE 21.61%, cash 1.00x, EM 10.8, cap 25x) = Rs 443 Year-3 target = 5.2% CAGR; the price already sits above the destination. Key risk: no order book beyond Q1 FY28 and towers lost to OEMs that build their own. Cash quality: INDETERMINATE."
```
