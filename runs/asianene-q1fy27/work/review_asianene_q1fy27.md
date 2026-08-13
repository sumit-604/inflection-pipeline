# Q1 FY27 MERGED QUARTERLY REVIEW — Asian Energy Services Limited (ASIANENE)

**Agent:** A4 Analyst | **Model:** claude-opus-4-8 | **Date:** 13 Aug 2026
**Protocol spine:** Role 4 (Quarterly Results Review Protocol v1.2) run in FULL.
**Role 5 (Concall Analysis Protocol v1.1):** N/A this run — **there is no concall transcript in the document set** (results filing + investor presentation + press release only). No concall analysis is fabricated. turns = 0, "no concall in doc set."
**Documents merged:** results (Reg 33 filing), presentation (34-slide deck), pressrelease (4-page Reg 30 release). Presentation and press-release findings feed the Role 4 spine.

---

## LEDGER RECONCILIATION PREAMBLE (stated before Step 1, per contract)

**Ledger contains 17 notes / 0 turns / 34 slides. All reviewed. A3 findings incorporated: [listed below].**

- **Notes = 17** numbered notes in the results filing (9 consolidated notes + 8 standalone notes), per `ledger_results` summary counts. Plus 4 roman-numeral segment narrative notes, 2 EPS annualisation footnotes, 2 employee-cost reclassification sub-tables, 90 financial-statement line items, 13 auditor paragraphs, 31 consolidation entities, 5 signature blocks — every row read at its cited line.
- **Turns = 0** — no concall in doc set. Role 5 is N/A.
- **Slides = 34** in the investor presentation (`ledger_presentation`, Table 1, 34/34 slide rows, 96 number-ledger rows, 5 footnotes) — all reviewed.
- **Press release** enumerated as 41 narrative units (19 headline numbers + 2 quotes + 8 forward statements + 12 operational claims), `ledger_pressrelease` — all reviewed.
- **All ledger rows reviewed: YES.** Reconciliation 100% on all three A2 ledgers (gate_a2 pass on each). No unreviewed rows. Proceeding.

**A3 findings incorporated (every id from all three forensics files):**
- Results: A3-F1, A3-F2, A3-F3, A3-F4, A3-F5, A3-F6, A3-F10, A3-F11, A3-F12, A3-F14, A3-F15
- Presentation: F1-1, F2-1, F6-1, F6-2, F7-1, F7-2, F10-1, F14-1, F16-1, F16-2, F16-3
- Press release: FN1, FN2, FN3, FN4, FN5, FN6, FN7

Every A3 finding classified FORWARD-SIGNAL or AMBIGUOUS is carried into the Questions-for-Management table (Step 8.5) with an explicit finding-id map; NEUTRAL-FACT findings (A3-F11, A3-F14) are noted in-line.

---

## STEP 0 — PRE-FLIGHT

**0A. Thesis baseline (Notion durable memory `companies/ASIANENE.md`; no live Notion page found on search, so durable memory IS the thesis of record).**
- **Decision Status (verified BEFORE any framing): AVOID (on-valuation) at CMP Rs 340 / DEEP WATCH.** Entry range Rs 75-93, MoS Rs 75, position Small ceiling (Promoter-CONCERN), **zero at CMP.** This is a **NON-HELD** name → position logic runs the **8A-W branch**, not 8A. No trim/exit mechanics apply.
- One-line thesis: AVOID at Rs 340; 20-25% EPS growth to Rs 19.6-22.2 by FY29 against a disciplined 13.2x four-pillar destination (ROCE 13.71% STAGNANT, cash 0.85x, EM 28, 20x cap) gives Rs 249 base = -10% CAGR; Hurdle STOP, promoter CONCERN, reverse merger dilutive at 117:10 / ~53x.
- Gate on evidence (prior): PROCEED WITH FLAGS. FTTCP composite +4, DEEP WATCH leaning BUY-ON-DIPS. Devil's advocate SURVIVES; anchored SOTP ~Rs 225-277.

**0B. Unit convention.** Results filing: **Lakhs** (÷100 to Rs Cr; extract header, and "INR in lakhs" L239/L521). Presentation and press release: **Rs Crore** (x1). All analysis below in **Rs Cr**. Every cell carries the results-extract line number (Lakhs source) or ND.

**0C. Share-count changes (0C).** Paid-up equity capital rose from Rs 44.74 Cr (Q1 FY26, L293/L563 4,474.43 Lakhs) to Rs 48.63 Cr (Q1 FY27, 4,862.90 Lakhs) = **+Rs 3.89 Cr, +8.7% shares** (447.44 lakh → 486.29 lakh shares, FV Rs 10). Drivers (note 7 consol / note 6 standalone, L386-397 / L607-618): allotment of **36,62,702 equity shares on warrant conversion** (Board circular resolution 05-May-2026) + ESOP allotment; separately **10,37,298 warrants LAPSED** 05-May-2026, upfront Rs 8.69 Cr (868.74 Lakhs) forfeited to equity. **EPS comparisons are NOT share-adjusted like-for-like** — the +8.7% denominator inflation must be read against EPS growth. A further, larger dilution leg (Oilmax merger) is pending and NOT yet in the share count (A3-F6/F10, F10-1).

**0D. Numbered-notes extraction (mandatory, built before any growth metric):**

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| C1 / S1 (L345 / L574) | Basis of prep | Ind AS; Audit Committee/Board approved 13 Aug 2026 | — | All | None |
| C2 / S2 (L350 / L579) | Availability / segments | Results on website; standalone carries no segment disclosure (Ind AS 108) | — | — | None |
| C3 / S3 (L353 / L581) | Other expenses composition | Includes travel, security, legal & professional | — | All | None (composition only) |
| C4 (L355-360) | Kuiper PPA finalised | Kuiper Holdings/Group acquisition (SPA 18-Apr-2025); PPA concluded Q4 FY26, capital reserve **Rs 39.97 Cr** (3,996.59 Lakhs) recognised (Ind AS 103) | +39.97 to reserves (Q4 FY26) | Q4 FY26 / FY26 | **Kuiper integrated from 01-Sep-2025 (deck fn L297/L437); Q1 FY26 base carries NO Kuiper.** All consol YoY comparisons are apples-to-oranges. |
| C5 / S5 (L362-369 / L599-606) | **Oilmax merger by absorption** | OEPL (Transferor) into AESL (Transferee), Sec 230-232 r/w Sec 66; shareholders approved 11/12-Jun-2026; **NCLT admitted petition 07-Jul-2026, fixed for hearing; no scheme effect given** | ND (not yet recognised) | Forward | **TRIPWIRE 1 event pending.** Accounting basis (fair-value vs pooling-at-book) and dilution ratio **NOT disclosed.** |
| C6 / S4 (L370-383 / L583-597) | Employee-cost reclassification | Project-related employee cost moved from Employee Benefits to Project Related Expenses (prior-year restatement) | reclass only | All periods restated | Comparability preserved (both periods restated); gross employee cost consol Rs 26.02 Cr, Rs 7.64 Cr moved |
| C7 / S6 (L386-397 / L607-618) | **ESOP grant + warrant lapse/conversion** | 1,77,000 options granted 19-May-2026, ESOP expense **Rs 0.58 Cr**; 10,37,298 warrants lapsed (Rs 8.69 Cr forfeited); **36,62,702 shares approved on conversion** of the remainder | +0.58 expense; +equity | Q1 FY27 | Two corporate actions bundled under one note; drives the +8.7% share count (0C) |
| C8 / S7 (L398-402 / L621-622) | **Exceptional items** | FY26 charge = Rs 2.72 Cr (271.82 Lakhs) contractual-dispute write-off per Outside Expert Council + (consol only) Rs 6.69 Cr Kuiper acquisition cost | nil this Q; Rs 9.40 Cr FY26 consol / Rs 2.72 Cr FY26 standalone | Q4/FY26 | **Line armed, not retired** — nil in current Q, populated Q4 FY26 only (A3-F1) |
| C9 / S8 (L403-405 / L624-626) | Q4 balancing-figure convention | Q4 FY26 figures are balancing figures (FY audited − 9M reviewed) | — | Q4 FY26 | **Q4 FY26 is a derived, not independently-reported, quarter** — treat Q4 QoQ points with care |

**Auditor opinion check:** **Unmodified review conclusion** (SRE 2410, limited review, NOT an audit opinion) on both consolidated and standalone. **No Emphasis-of-Matter paragraph; no Going Concern paragraph** (swept absent, A3-F5). BUT two governance data points inside the "Other Matters": (a) **auditor transition** — predecessor Walker Chandiok & Co LLP (comparative Q1 FY26) → SGCO & Co LLP (current, first SGCO review) (L158-162 / L478-482); (b) **17.6% of consolidated PAT rests on entities reviewed by no auditor** — 21 subsidiaries (Rs 1.45 Cr PAT) + 5 JVs (Rs 0.79 Cr share) unreviewed, plus 1 subsidiary reviewed by another auditor posting **Rs (3.26) Cr loss on Nil revenue** (L112-114, L135-144; A3-F3/F4). Management asserts "not material to the Group." This is an **AMBER data-quality flag** on the consolidated numbers.

**0E. Business type:** **Standard operating business** (integrated oilfield / energy & mining services + upstream E&P via merger). NOT a lender. Steps 1 and 5 (standard), not 1L/5L.

STOP cleared: Notion Decision Status fetched (AVOID / DEEP WATCH / non-held), units identified (Lakhs ÷100), share-count change noted (+8.7%), all notes extracted, auditor opinion verified (unmodified review, no EoM/GC), business type stated (standard). Proceeding.

---

## STEP 1 — DATA EXTRACTION TABLE (both bases, every cell line-anchored or ND)

All values **Rs Cr** (results extract in Lakhs ÷100). Columns: Q1 FY26 (30-Jun-25) / Q4 FY26 (31-Mar-26, balancing figure per note 9) / Q1 FY27 (30-Jun-26) / FY26. Line refs are the results-extract line numbers.

### 1A. CONSOLIDATED

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Line |
|---|---|---|---|---|---|
| Revenue from Operations | 115.37 | 338.23 | 271.19 | 791.05 | L245 |
| Other Income | 1.99 | 1.59 | 3.32 | 8.89 | L246 |
| Total Income | 117.36 | 339.83 | 274.50 | 799.94 | L247 |
| Project Related Expense (= COGS proxy) | 92.75 | 265.14 | 218.93 | 622.30 | L250 |
| Change in Inventories | 0.07 | (0.01) | 0.17 | (0.11) | L251 |
| Employee Benefits Expense (net) | 6.79 | 13.60 | 18.38 | 42.25 | L252 |
| Finance Costs | 1.50 | 3.36 | 3.76 | 10.65 | L253 |
| Depreciation, depletion & amortisation | 4.69 | 5.13 | 4.38 | 18.86 | L254 |
| Other Expenses | 4.31 | 11.75 | 12.56 | 31.25 | L255 |
| Total Expenses | 110.10 | 298.97 | 258.18 | 725.21 | L256 |
| PBT before JV share & tax | 7.25 | 40.85 | 16.32 | 74.73 | L258 |
| Share of profit from JVs | 0.60 | 1.67 | 0.79 | 3.51 | L259 |
| PBT before exceptional | 7.85 | 42.52 | 17.11 | 78.24 | L260 |
| Exceptional items (net loss) | ND (nil) | (2.79) | ND (nil) | (9.40) | L261 |
| Profit Before Tax | 7.85 | 39.73 | 17.11 | 68.84 | L262 |
| Tax Expense | 2.22 | 7.08 | 4.35 | 17.00 | L268 |
| PAT (total) | 5.63 | 32.65 | 12.76 | 51.84 | L269 |
| — PAT attributable to owners | 5.55 | 31.96 | 11.96 | 51.16 | L282 |
| — PAT to non-controlling interest | 0.08 | 0.69 | 0.80 | 0.68 | L283 |
| EPS reported (basic, Rs) | 1.24 | 7.14 | 2.53 | 11.43 | L299 |
| EPS reported (diluted, Rs) | 1.23 | 7.08 | 2.49 | 11.34 | L300 |
| EPS share-adjusted | see note ‡ | ‡ | ‡ | ‡ | — |
| Paid-up equity capital | 44.74 | 44.92 | 48.63 | 44.92 | L293 |
| Other equity (reserves) | ND | ND | **ND (blank in all interim cols)** | 449.24 | L295 |

‡ EPS share-adjustment note: no split/bonus occurred; the movement is a warrant conversion (+8.7% shares) that is a real dilution, not a mechanical split — so reported EPS is NOT restated. Weighted-avg shares implied by EPS: Q1 FY27 = PAT-owners 11.96 / 2.53 = ~4.73 cr; Q1 FY26 = 5.55 / 1.24 = ~4.48 cr (weighted +5.5%; period-end paid-up +8.7% because conversion landed 05-May-2026, ~2 months into the quarter).

### 1B. STANDALONE

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Line |
|---|---|---|---|---|---|
| Revenue from Operations | 115.37 | 207.13 | 149.28 | 491.77 | L527 |
| Other Income | 1.84 | 2.38 | 2.46 | 9.12 | L528 |
| Total Income | 117.21 | 209.51 | 151.74 | 500.88 | L529 |
| Project Related Expense | 92.72 | 153.56 | 113.35 | 366.83 | L532 |
| Change in Inventories | 0.07 | (0.01) | 0.17 | (0.11) | L533 |
| Employee Benefits Expense (net) | 6.73 | 7.24 | 11.47 | 25.00 | L534 |
| Finance Costs | 1.33 | 1.84 | 1.82 | 6.45 | L535 |
| Depreciation, depletion & amortisation | 4.06 | 4.48 | 4.10 | 16.47 | L536 |
| Other Expenses | 3.97 | 7.79 | 7.99 | 21.73 | L537 |
| Total Expenses | 108.88 | 174.90 | 138.90 | 436.35 | L538 |
| PBT before exceptional | 8.33 | 34.60 | 12.84 | 64.53 | L540 |
| Exceptional items (loss) | ND (nil) | (2.72) | ND (nil) | (2.72) | L541 |
| Profit Before Tax | 8.33 | 31.89 | 12.84 | 61.81 | L542 |
| Tax Expense | 2.22 | 9.20 | 3.29 | 16.96 | L548 |
| PAT | 6.11 | 22.69 | 9.55 | 44.85 | L550 |
| EPS reported (basic, Rs) | 1.37 | 5.07 | 2.02 | 10.02 | L568 |
| EPS reported (diluted, Rs) | 1.36 | 5.02 | 1.99 | 9.94 | L569 |
| Paid-up equity capital | 44.74 | 44.92 | 48.63 | 44.92 | L563 |
| Other equity (reserves) | ND | ND | **ND (blank in all interim cols)** | 402.66 | L565 |

### 1C. DERIVED METRICS

**Anchor definition:** *Operating EBITDA (ex-JV, ex-Other-Income)* = Revenue − Project exp − Change in inv − Employee − Other exp (equivalently PBT-before-JV&tax + D&A + Finance − Other Income). The **investor deck's "EBITDA" is non-standard** — it folds in JV share of profit Rs 0.79 Cr and excludes Other Income (A3-presentation reconciliation flag 1); I track my operating EBITDA as the anchor and reconcile to the deck below.

| Derived Metric (CONSOLIDATED) | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|
| Operating EBITDA (ex-JV, ex-OI) | 11.45 | 47.75 | **21.14** | 95.35 |
| Operating EBITDA Margin | 9.92% | 14.12% | **7.80%** | 12.05% |
| Deck EBITDA (incl JV, ex-OI) [reconciliation] | 12.05 | 49.42 | 21.93 | 98.86 |
| Deck EBITDA Margin (matches deck slide 12) | 10.44% | — | **8.09%** | 12.50% |
| Reported EBITDA (PBT-before-excep + D&A + Fin) | 14.04 | 51.01 | 25.25 | 107.75 |
| Core PBT ex-Other Income (PBT − OI) | 5.86 | 38.14 | 13.79 | 59.95 |
| Other Income / PBT | 25.4% | 4.0% | 19.4% | 12.9% |
| Effective Tax Rate | 28.3% | 17.8% | 25.4% | 24.7% |
| PAT Margin (on Revenue) | 4.88% | 9.65% | 4.71% | 6.55% |

| Derived Metric (STANDALONE) | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|
| Operating EBITDA (ex-OI) | 11.88 | 38.55 | **16.30** | 78.32 |
| Operating EBITDA Margin | 10.30% | 18.61% | **10.92%** | 15.93% |
| Core PBT ex-Other Income | 6.49 | 32.22 | 10.38 | 55.41 |
| Effective Tax Rate | 26.6% | 28.8% | 25.6% | 27.4% |
| PAT Margin (on Revenue) | 5.30% | 10.95% | 6.40% | 9.12% |

**Headline reconciliation (deck / press release vs filing):** revenue 115.4→271.2 = **+135.0%** (L245: 11,536.69→27,118.53, +135.1% — matches). Deck EBITDA 12.1→21.9 = **+81.0%** (matches; both fold in JV). PAT 5.6→12.8 = **+128.6%** (L269: 563.23→1,275.65, +126.5% on precise figures; deck rounds to 12.8/5.6=128.6%). All three headline growth rates verified against the filing. **What the headline omits: operating EBITDA margin fell ~212 bps (9.92%→7.80%); deck EBITDA margin fell ~235 bps (10.5%→8.1%).**

STOP cleared: every cell filled or ND. Proceeding to analysis.

---

## STEP 2 — Q1 FY27 YoY COMPARISON (CONSOLIDATED — the most important step)

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 115.37 | 271.19 | **+135.1%** | Strong — but ~Rs 121.9 Cr is Kuiper/subsidiary revenue absent from the base (integrated 01-Sep-2025) |
| Operating EBITDA (ex-JV, ex-OI) | 11.45 | 21.14 | +84.6% | Grew, but far slower than revenue |
| Operating EBITDA Margin | 9.92% | 7.80% | **−212 bps** | **CONTRACTED** — Kuiper leg dilutive |
| Depreciation | 4.69 | 4.38 | −6.6% | Falling despite 2.4x revenue → asset-light subs (A3-F3) |
| Finance Costs | 1.50 | 3.76 | +150.3% | Scaling far faster than operating profit |
| EBIT (op EBITDA − D&A) | 6.76 | 16.76 | +147.9% | Flattered by low D&A |
| Other Income | 1.99 | 3.32 | +66.8% | 19.4% of PBT |
| **Core Operating PBT (PBT − OI)** | 5.86 | 13.79 | **+135.3%** | Grew in line with revenue — core is real, but margin-thin |
| Reported PBT | 7.85 | 17.11 | +118.0% | |
| PAT (total) | 5.63 | 12.76 | +126.5% | |
| EPS basic (Rs) | 1.24 | 2.53 | +104.0% | **Lags PAT growth by ~22 pp — share count +8.7% + higher NCI** |

**Mandatory diagnostics:**
1. **Did revenue grow YoY?** Yes, +135.1% consolidated. But this is a **base-effect illusion**: Kuiper was integrated only from 01-Sep-2025, so Q1 FY26 carries zero Kuiper. Standalone (ex-Kuiper) revenue grew **+29.4%** (L527: 11,536.69→14,927.67) — that is the like-for-like organic number, and it sits **marginally below the 30-40% order-backed guide** (TRIPWIRE 4 territory, see Step 6C).
2. **Did operating EBITDA margin expand/contract/flat?** **Contracted.** Q1 FY27 operating margin 7.80% vs Q1 FY26 9.92% = **−212 bps**. Deck's own EBITDA margin fell 10.5%→8.1%. Standalone margin, by contrast, *improved* 10.30%→10.92%. **The entire consolidated margin compression is the Kuiper/subsidiary leg**: incremental Rs 121.9 Cr subsidiary revenue (consol 271.19 − standalone 149.28) earned only Rs 4.85 Cr incremental operating EBITDA (21.14 − 16.30) = **~4.0% incremental margin** vs ~11% standalone (A3-F2, F2-1, FN5).
3. **Did core operating PBT (ex-OI) grow YoY?** Yes, +135.3% — so headline growth is *directionally* real, not a treasury illusion. Other Income (Rs 3.32 Cr, +66.8%) is 19.4% of PBT but did not manufacture the growth. The quality problem is **margin mix and audit coverage, not other-income padding.**
4. **What drove the gap between core-PBT growth (+135%) and PAT growth (+126.5%)?** Finance costs +150.3% (Rs +2.26 Cr) is the main drag; partly offset by falling D&A (−6.6%) and a lower ETR (28.3%→25.4%). NCI took Rs 0.80 Cr (vs Rs 0.08 Cr) — minority partners now claim a real slice, widening the PAT-owners vs PAT gap.
5. **Are D&A and finance costs scaling faster than revenue?** Finance costs, yes (+150% vs revenue +135%). D&A is *falling* — consolidated D&A (Rs 4.38 Cr) is only Rs 0.28 Cr above standalone (Rs 4.10 Cr) despite Rs 121.9 Cr of extra revenue. This confirms A3-F3: the 26 subsidiaries are **asset-light manpower/crew shells** (Kuiper Labour Supply, Nexus People Management, Kuiper HR). Low capital intensity is good for ROCE but means the subsidiary earnings are **thin-margin, people-cost pass-through** work, not asset-backed annuity.
6. **Is Other Income concentration changing?** OI/PBT fell from 25.4% (Q1 FY26) to 19.4% (Q1 FY27) — treasury is a smaller share this quarter, so the growth is not OI-timing-driven. Neutral.

STOP cleared.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY (CONSOLIDATED)

Only three quarters are present in this filing (Q1 FY26, Q4 FY26, Q1 FY27); **Q2 and Q3 FY26 are ND (not in the Q1 filing)**, so run-rate stepping analysis is limited and Q4 FY26 is a *balancing figure* (note 9, not independently reported).

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT ex-OI | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 (30-Jun-25) | 115.37 | 9.92% | 5.86 | none (pre-Kuiper) | base |
| Q2 FY26 | ND | ND | ND | Kuiper integrated 01-Sep-2025 (part-qtr) | ND |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 (31-Mar-26) | 338.23 | 14.12% | 38.14 | Rs (2.79) Cr exceptional (note 8); balancing figure (note 9) | seasonal peak |
| Q1 FY27 (30-Jun-26) | 271.19 | 7.80% | 13.79 | ESOP Rs 0.58 Cr; warrant conversion | **−19.8% QoQ rev; margin −632 bps QoQ** |

**Diagnostics:**
- **Run-rate:** Q1 FY27 revenue (271.19) is down −19.8% QoQ from Q4 FY26 (338.23) and operating margin collapsed −632 bps QoQ. This is partly **structural seasonality** (Q4 is the peak execution quarter; Mineral segment revenue −68% QoQ, L312 8,223.60→2,640.94, A3-F12) and partly the Kuiper drag now sitting in a non-peak quarter.
- **Segment-result read (feeds Step 6B/6D GSECL framing):** on a YoY basis the Mineral & other energy segment RESULT actually **FELL Rs 4.69→4.07 Cr, −13.2% (L317: 469.05→406.97 Lakhs)**, while **all** group segment-profit growth came from Oil & Gas, up Rs 18.86→33.30 Cr (L316: 1,886.34→3,329.93 Lakhs). Both segment margins compressed YoY (O&G 20.4%→13.6%; Mineral 20.3%→15.4%, A3-F12).
- **One-off distortion:** Q4 FY26 carried a Rs 2.79 Cr exceptional charge and is a balancing figure — not clean. Q1 FY27 carries an ESOP expense Rs 0.58 Cr (note 7).
- **H1-vs-peak test:** cannot be run (Q2/Q3 FY26 ND). Flag for Q2 FY27 review.
- **Implied Q2 FY27 base:** to hold the FY26 full-year 12.05% operating margin, Q2 must recover well above 7.80%; a second sub-12% quarter arms TRIPWIRE 5 (see Step 6C).

STOP cleared.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, CONSOLIDATED, Q1 FY27 vs Q1 FY26)

Reported PAT change = 5.63 → 12.76 = **+Rs 7.13 Cr**.

| Component | YoY change (Rs Cr) | YoY change (%) | Recurring? |
|---|---|---|---|
| Operating EBITDA (revenue growth × margin, net) | +9.70 | +84.6% | Recurring (but margin-dilutive mix) |
| D&A change (favourable, D&A fell) | +0.31 | −6.6% | Recurring (asset-light subs) |
| Finance cost change (unfavourable) | −2.26 | +150.3% | Recurring (post-Kuiper debt) |
| Other Income change | +1.33 | +66.8% | NON-RECURRING typically |
| JV share of profit change | +0.19 | +32.0% | Semi-recurring (unreviewed, RP overlay) |
| Exceptional items | 0.00 | nil both periods | n/a (armed, A3-F1) |
| Effective tax-rate change | +2.13 credit to PAT vs proportional | −290 bps ETR | Mixed |
| **Reported PAT YoY change** | **+7.13** | **+126.5%** | |

**Answers:**
- **% from recurring core vs non-recurring:** Recurring operating (EBITDA + D&A) contributed +Rs 10.01 Cr, offset by recurring finance −Rs 2.26 Cr = **+Rs 7.75 Cr net recurring**. Non-recurring/lower-quality items (Other Income +1.33, JV +0.19) added +Rs 1.52 Cr; higher tax took −Rs 2.13 Cr. So **~100%+ of the PAT increase is core-operations-driven** — the *quality concern is not fabrication, it is (a) margin dilution, (b) 17.6% of PAT unaudited, (c) Rs 0.79 Cr from unreviewed related-party JVs, and (d) a share-count and merger dilution overhang.**
- **If Other Income reverts to prior level (Rs 1.99 Cr):** PAT would be ~Rs 1.0 Cr lower (~Rs 11.8 Cr) — not thesis-altering.
- **D&A/finance steady-state:** finance is still ramping post-Kuiper (+150%); once Oilmax (an asset-heavy E&P) consolidates, both D&A and finance will step up materially — today's asset-light D&A profile does NOT survive the merger.
- **Tax:** ETR 25.4% ≈ statutory 25.17%; deferred tax a small charge (Rs 0.34 Cr, L267); no tax shenanigans (A3 F8 PASS).

STOP cleared.

---

## STEP 4S — STANDALONE-vs-CONSOLIDATED GAP (first-class metric, from A3-F2 / FN1)

This is the single most important structural signal this quarter.

| Metric | Q1 FY26 | Q4 FY26 | Q1 FY27 | Source |
|---|---|---|---|---|
| Consolidated PAT (total) | 5.63 | 32.65 | 12.76 | L269 |
| Standalone PAT | 6.11 | 22.69 | 9.55 | L550 |
| **S-vs-C PAT gap (Cons − Stand), Rs Cr** | **(0.48)** | +9.96 | **+3.21** | derived |
| **Gap as % of standalone PAT** | **−7.8%** | +43.9% | **+33.5%** | derived |
| Consolidated revenue | 115.37 | 338.23 | 271.19 | L245 |
| Standalone revenue | 115.37 | 207.13 | 149.28 | L527 |
| **Revenue gap (subs/Kuiper), Rs Cr** | **0.00** | +131.10 | **+121.91** | derived |

**Reading:** the S-vs-C PAT gap swung **~41.3 pp** (from −7.8% to +33.5% of standalone PAT) in one year, driven entirely by the Kuiper consolidation (revenue gap Rs 0.00 → Rs 121.91 Cr). **A year ago the consolidated entity earned LESS than the standalone (loss-making subs dragged it below); today subsidiaries add a third to group PAT.** Group earnings now materially depend on entities that (a) contributed nothing a year ago, (b) are ~4%-margin manpower shells, and (c) include Rs 2.24 Cr (17.6% of consol PAT) reviewed by no auditor and one subsidiary bleeding Rs 3.26 Cr on nil revenue. **This is a fragile, low-visibility earnings base wearing a +129% PAT headline.** The 41 pp swing is far above the 5 pp materiality trigger.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET (CONSOLIDATED + STANDALONE)

**Data-availability rule (v1.2):** Reg 33 mandates half-yearly cash flow and balance sheet. **This is a Q1 review → CFO and balance sheet are NOT required and are NOT in the filing.** The cash-quality rows are ND this quarter by regulation, not by omission.

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (consol / standalone) | ND | **ND** | ND | Not disclosed at Q1 (Reg 33) |
| CFO/PAT ratio | ND | **ND** | ND | **INDETERMINATE this quarter** |
| Capex (PPE + CWIP) | ND | ND | ND | Not disclosed |
| FCF (CFO − Capex) | ND | ND | ND | Not disclosed |
| Working-capital change | ND | ND | ND | Not disclosed |
| Receivable days | ND | ND | ND | Not disclosed (TRIPWIRE 3 not testable) |
| Inventory days | ND | ND | ND | Not disclosed |
| Payable days | ND | ND | ND | Not disclosed |
| Cash Conversion Cycle | ND | ND | ND | Not disclosed |
| PPE | ND | ND | ND | Not disclosed |
| CWIP | ND | ND | ND | Not disclosed |
| Net Debt / (Net Cash) | ND | ND | ND | Not disclosed (net-debt/EBITDA leg of TRIPWIRE 5 not testable) |
| Other equity (net worth proxy) | Mar-26 consol Rs 449.24 Cr / stand Rs 402.66 Cr (L295/L565) | **ND (blank all interim cols)** | ND | Net worth cannot be tied out at 30-Jun-2026 (A3-F11) |
| Promoter Pledge | ND (not in filing) | ND | ND | Not disclosed |

**Mandatory questions:**
- **CFO/PAT vs Pillar-2 cash multiplier (0.85x thesis assumption):** **cannot be tested this quarter — no CFO in a Q1 filing.** Cash conversion is therefore **INDETERMINATE for Q1 FY27**. Per house rule, INDETERMINATE cash conversion **must not resolve silently to PROCEED; it caps the verdict at PROCEED WITH CAVEATS with the missing evidence named** (missing evidence: consolidated and standalone CFO, working-capital movement, receivable ageing, net debt). The **Q2 FY27 half-yearly filing is the first mandatory cash reading** and is the pivotal monitorable.
- **WC drag structural vs growth-induced:** operator ruling (durable) already classifies cash as **GROWTH-INDUCED with a related-party collection overlay** (single positive FY26 CFO print after two negative years). Nothing this quarter changes that; nothing this quarter confirms it either.
- **CWIP capitalisation:** ND. **Net debt within range:** ND — but finance costs +150% YoY (Rs 3.76 Cr) signal higher gross debt post-Kuiper; the Oilmax E&P merger will add asset-heavy debt.

**Cash-conversion classification for this review: INDETERMINATE (this quarter) — prior operator ruling GROWTH-INDUCED with RP overlay carried forward, unrefreshed.** Missing evidence named above. This is the binding cap on the verdict (see Step 8).

STOP cleared.

---

## STEP 6 — RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

Notion durable memory carries the thesis at ANNUAL granularity (FY29 EPS Rs 19.6-22.2, destination 13.2x, base Rs 249, EPS CAGR 20-25%); it does not carry quarterly Bear/Base/Bull cells, so quarterly projection cells are **ND** and the annual read is applied qualitatively.

| Metric | Bear | Base | Bull | Actual Q1 FY27 (annualised where noted) | Lands in |
|---|---|---|---|---|---|
| Revenue growth — standalone (organic) | ND | ~30-40% (order-backed guide) | ND | **+29.4%** (L527) | **Just BELOW base guide floor** |
| Revenue growth — consolidated | ND | ND | ND | +135.1% (Kuiper base effect) | Not comparable (inorganic) |
| Op EBITDA margin — consolidated | ND | ~12% (FY26 exit) | ND | **7.80%** (deck 8.1%) | **BELOW** |
| Op EBITDA margin — standalone | ND | ND | ND | 10.92% | roughly in line |
| PAT — consolidated | ND | ND | ND | Rs 12.76 Cr (Rs ~51 Cr annualised run-rate) | ≈ FY26 run-rate |
| EPS (basic, consol) | ND | Rs 19.6-22.2 by FY29 | ND | Rs 2.53 (Rs ~10 annualised) | on the long glide-path, dilution-flattered |
| Net Debt | ND | ND | ND | ND (not disclosed) | ND |
| ROCE | ND | 13.71% (STAGNANT) | ND | **ND** (Other equity blank; not computable) | ND |

**Probability re-weighting rule (v1.2):** requires actuals BELOW BEAR on 2+ key metrics for 2 CONSECUTIVE quarters. Notion carries no quarterly bear cells to test "below bear", and this is the **first** quarterly review under the pipeline. **Rule does NOT fire this quarter.** Flag: standalone revenue growth (29.4%) below the 30-40% guide floor is the first potential miss; a second consecutive soft/miss in Q2 begins the pattern.

### 6B. Watchlist / monitoring-checklist status

| # | Watchlist item (from Notion optionality/monitoring) | Green | Red | This-quarter reading | Status |
|---|---|---|---|---|---|
| 1 | Oilmax merger completion + accounting basis | Fair-value disclosed, non-dilutive terms | Pooling-at-book confirming 35-51% dilution | NCLT admitted 07-Jul; hearing 28-Aug; completion Sep/Oct 2026; **basis NOT disclosed** | **AMBER** (approaching, basis silent) |
| 2 | Duarmara production (JV Antelopus/Selan) | Commercial production | Slip | "160x reserves to 40 MMBOE; testing underway"; FY27 focus (deck L658) | AMBER (pre-commercial) |
| 3 | Kuiper expansion / stabilisation | Stable ~8% margin, US$100Mn by FY29 | Loss / customer loss | "stabilized in June" (implies Apr-May weak); ~4% incremental consol margin | **AMBER** (thin margin, geopolitics-exposed) |
| 4 | Coal handling beyond MCL — GSECL | New order won into a **growing** segment | Order into a **shrinking-profit** segment | **GSECL Ukai Rs 187.6 Cr won, work commenced (deck L232) — BUT it lands in the Mineral & other energy segment whose YoY segment RESULT FELL Rs 4.69→4.07 Cr, −13.2% (L317); all group segment-profit growth is O&G, Rs 18.86→33.30 Cr (L316)** | **AMBER** (order-level win into a declining-profit segment; a large order over a segment whose YoY result is shrinking) |
| 5 | South Rewa / Chhattisgarh CBM clearance | Clearance obtained | Delay | "~2-yr timeline, drilling/test-well" (deck L655) | AMBER (early) |
| 6 | L1 NE India O&M contract | Award | — | Not mentioned this quarter | UNKNOWN |
| 7 | Standalone revenue vs 30-40% guide | ≥30-40% | <30% | **+29.4%** | **AMBER** (just below floor) |
| 8 | Consolidated EBITDA margin | ≥12% | <12% two quarters | **7.80% / deck 8.1%** | **RED-leaning AMBER** (first sub-12% quarter) |

### 6C. Thesis-broken / active-tripwire check (explicit fired / not-fired / cannot-assess)

| Tripwire | Threshold | Current reading (line-anchored) | FIRED? |
|---|---|---|---|
| **1 — Oilmax merger on fair-value (non-pooling-at-book) basis confirming 35-51% EPS dilution** | Merger closes on fair-value basis, dilution confirmed | Note 5 (L362-369): NCLT admitted petition 07-Jul-2026, hearing fixed, **no scheme effect given; accounting basis NOT disclosed** anywhere in any of the three documents. Deck (slide 8/20) says completion Sep/Oct 2026, NCLT final hearing 28-Aug-2026. | **NOT FIRED** — event pending; **moving closer** (dilution leg not yet in the +8.7% share count). Basis remains the pivotal unverified fact. |
| **2 — Negative CFO quarter in FY27 while revenue grows, OR TTM CFO/PAT < 0.5x** | CFO<0 or TTM CFO/PAT<0.5x | **No cash-flow statement in a Q1 Reg 33 filing** — CFO ND. | **CANNOT ASSESS** — missing evidence: Q1 CFO. First testable at Q2 FY27 half-yearly (mandatory CFO). |
| **3 — Related-party receivable ageing past 180 days (RP already 56.4% of gross book; Asian Indwell JV 26.9%)** | RP receivable >180 days | **No balance sheet / receivables ageing in Q1 filing** — ND. Note the 5 JVs (incl Asian Indwell) contributed Rs 0.79 Cr UNREVIEWED share of profit (L138-140), the RP overlay, but ageing not disclosed. | **CANNOT ASSESS** — missing evidence: receivables ageing schedule. |
| **4 — Standalone revenue ex-Kuiper below 30-40% order-backed guide (third consecutive reaffirm-then-miss)** | <30-40%, third consecutive | Standalone revenue +29.4% YoY (L527: 11,536.69→14,927.67) — **just below the 30% floor**; but this is the FIRST quarter in the pipeline record, not the third consecutive. | **NOT FIRED** (soft) — **FLAG: marginal miss of the guide floor, first data point.** A second miss in Q2 advances the pattern. |
| **5 — Consolidated EBITDA margin below 12% for two consecutive quarters; net debt/EBITDA above 1.5x** | <12% two quarters AND/OR ND/E>1.5x | Consol operating EBITDA margin 7.80% (deck EBITDA margin 8.1%, L408) — **below 12% this quarter (first of two)**; FY26 full-year was 12.05% (deck 12.5%), Q4 FY26 14.12%. Net debt ND. | **NOT FIRED — ARMED (first sub-12% quarter).** Second consecutive sub-12% quarter in Q2 FY27 FIRES the margin leg. Net-debt/EBITDA leg CANNOT ASSESS (net debt ND). |

**No tripwire has formally FIRED.** Two are ARMED/approaching (4 marginal miss, 5 first sub-12% quarter); two CANNOT ASSESS pending the Q2 half-yearly (2, 3); one is AMBER pending the merger close (1). Per discipline, I **flag; the human decides.** Decision Status remains **AVOID / DEEP WATCH** unchanged.

### 6D. Growth-trigger status

| Trigger | Original confidence | Confirming evidence (this Q) | Killing evidence | Updated status |
|---|---|---|---|---|
| Oilmax reverse merger (optionality + dilution) | Medium | NCLT admitted; shareholder approval; hearing 28-Aug | Basis undisclosed; dilution unpriced | **ON TRACK (timeline); WEAKENED (transparency)** |
| Kuiper Nigeria/ME expansion to US$100Mn FY29 | Medium | "stabilized in June", integrated | ~4% incremental margin; ME volatility hedge x2 | **DELAYED/WEAKENED** (thin margin) |
| Duarmara / Mewad / Amguri / Tiphuk production | Low-Med | 40 MMBOE, 50,000 SCMD EWT, rig mobilised | All FY27 "focus", none commercial yet | **ON TRACK (early)** |
| Coal handling beyond MCL (GSECL) | Low | Rs 187.6 Cr GSECL order won, work commenced (deck L232) | **Order lands in the Mineral & other energy segment whose YoY segment RESULT FELL Rs 4.69→4.07 Cr, −13.2% (L317); all group segment-profit growth is O&G, Rs 18.86→33.30 Cr (L316)** | **AMBER — order-level win into a shrinking-profit segment; NOT a profit-level FIRE.** A large order over a segment whose YoY result is declining; re-rate to FIRED only when Mineral segment result turns up. |
| Order book → revenue conversion (Rs 1,754 Cr) | Medium | Reaffirmed, 60/40 O&G/Mineral | Standalone rev +29.4% below guide floor; Mineral backlog Rs 699 Cr vs ~Rs 26 Cr/qtr run-rate = thin execution | **WEAKENED** |

STOP cleared.

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

The destination PE (13.2x) was set under Section 1B v3.3 in the first workup. This quarter provides **no balance-sheet data** (Other equity blank, no capital-employed), so ROCE and cash-multiplier pillars **cannot be recomputed** — they HOLD by absence of new data, with the margin-compression signal flagged as downward pressure.

| Pillar / Input | Original assumption | Current reading (Q1 FY27) | Action |
|---|---|---|---|
| ROCE Base (0.5×ROCE+7.5, floor 9x cap 24x) | ROCE 13.71% STAGNANT → ~14.4x pre-cap | **ND** — Other equity blank (L295), capital employed not derivable; margin compression (op EBITDA −212 bps) is a *negative* forward signal for ROCE | **HOLD pending Q2 balance sheet.** FTTCP verdict remains sole Pillar-1 authority; no ad-hoc revision. Flag margin pressure. |
| Cash Multiplier | 0.85x (growth-induced) | **INDETERMINATE** — no CFO at Q1 | HOLD; re-test at Q2 half-yearly CFO |
| Growth Visibility Premium | +(embedded, EM 28) | GSECL order won but into a declining-profit segment (see 6D); catalysts intact but early | HOLD |
| Strategic Premium | + (single-credit: ROCE recovery NOT double-credited) | Integrated-platform narrative reaffirmed; no moat change | HOLD |
| UA Multiplier | 1.25x applies / per Amendment 3 (if applied) | No change in the three qualifiers this quarter | HOLD |
| Sector Cap | **20x** (EPC/Civil primary; oilfield/energy-services, NOT agri — operator ruling) | No reclassification. Note press-release mention of OEPL "advanced agriculture" subsidiary (L176-177) does NOT reclassify AESL to agri | HOLD 20x |
| **Hurdle Ratio recheck** | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) ≥ 1.953 → prior verdict **STOP** at CMP Rs 340 | Cannot fully recompute (ROCE/dest-PE inputs unchanged; CMP not in filing). At the thesis's Rs 249 base vs Rs 340 CMP, HR stays **STOP** | **STOP (unchanged)** |

**Destination PE:** unchanged at ~13.2x (±7.5%) — **no pillar changed on evidence this quarter** (the two that could move, ROCE and cash, are ND). No revision to Bear/Base/Bull fair values. Entry zone Rs 75-93 / MoS Rs 75 **unchanged.**

STOP cleared.

---

## STEP 8 — POSITION DECISION (branch 8A-W — NON-HELD name)

**Decision Status verified in Step 0A: AVOID / DEEP WATCH, zero position at CMP.** This is a non-held name → **8A-W branch** (no trim/exit mechanics; output is updated entry zone / gate / status).

- **Any thesis-broken condition FIRED?** No — no tripwire formally fired (Step 6C). Two armed (4, 5), two cannot-assess (2, 3), one AMBER (1). → do NOT reclassify to a harder AVOID; **remain AVOID / DEEP WATCH.**
- **Actuals below bear on 2+ metrics?** Cannot establish (no quarterly bear cells; first pipeline quarter). Standalone revenue +29.4% is a *soft* miss of the guide floor; consolidated margin 7.8% is below the ~12% thesis anchor. → **projections lean toward the softer end; entry zone held, not lowered, pending Q2 confirmation.**
- **Actuals between bear and base / at-or-above base?** Mixed: standalone operations roughly in line (revenue +29.4%, PAT +56%, margin +62 bps); consolidated quality **below** thesis (margin −212 bps, 17.6% PAT unaudited, dilution overhang). → **Thesis INTACT (AVOID confirmed); no upgrade.**

**8A-W output:**
- **Decision Status: AVOID / DEEP WATCH — UNCHANGED.**
- **Entry zone: Rs 75-93, MoS Rs 75 — UNCHANGED** (no pillar moved on evidence).
- **Master decision gate: PUSHED to Q2 FY27 half-yearly filing** — the first quarter with mandatory CFO/balance sheet, which resolves (a) tripwire 2 (CFO), (b) tripwire 3 (RP receivable ageing), (c) the net-debt leg of tripwire 5, and (d) whether the sub-12% margin becomes the second consecutive quarter that FIRES tripwire 5. The Oilmax NCLT hearing (28-Aug-2026) and completion (Sep/Oct 2026) with its accounting basis is the parallel gate for tripwire 1.
- **Position action: NONE** (zero at CMP; no add — CMP Rs 340 is ~4.5x the top of the Rs 75-93 entry zone).

**8B. Add-back / trim trigger refinement.** No trim ladder (not held). Add-back gate refined: **require (i) Oilmax accounting basis disclosed as fair-value with dilution ≤ prior-modelled AND (ii) consolidated EBITDA margin recovered ≥12% AND (iii) Q2 CFO/PAT ≥0.5x, before any re-engagement even within the Rs 75-93 zone.**

**8C. Single cleanest metric for Q2 FY27:** **Consolidated operating EBITDA margin (ex-JV).** Bull threshold: **≥12%** (recovers, disarms tripwire 5, validates Kuiper "stabilisation"). Bear threshold: **<12%** (second consecutive sub-12% quarter → **FIRES tripwire 5 margin leg**). Secondary (event, not metric): Oilmax scheme accounting basis at NCLT sanction. Tertiary: Q2 consolidated CFO/PAT ≥0.5x (first cash reading).

STOP cleared.

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT

Channel: **SME/IR — no concall was hosted this quarter.** Deliver via IR email / AGM Q&A. Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to ≥1 question (finding-id map in the last column).

| # | Question (references a filed number) | Why it matters | Bull answer | Bear answer | A3 findings covered |
|---|---|---|---|---|---|
| 1 | The Oilmax merger (NCLT hearing 28-Aug, completion Sep/Oct 2026): will the scheme be accounted on a **fair-value / acquisition basis or pooling-at-book**? State the exact share-exchange ratio, the number of new AESL shares to be issued, and the resulting pro-forma EPS dilution. Does the previously disclosed 117:10 ratio / ~53x implied valuation stand? | Pivotal unverified fact behind TRIPWIRE 1 (35-51% EPS dilution); the +8.7% share count so far excludes this leg | Fair-value basis, dilution ≤ modelled, ratio improved | Pooling-at-book, 35-51% dilution confirmed, "subject to further clearances" | A3-F6, A3-F10, F10-1, FN2, F7-2, F14-1 |
| 2 | Consolidated EBITDA margin fell to 8.1% from 10.5% YoY (operating ex-JV 7.8% from 9.9%); the incremental Rs 121.9 Cr of subsidiary revenue earned only ~4% EBITDA margin. What is the **sustainable Kuiper EBITDA margin** once "stabilised", and what **consolidated EBITDA margin do you guide to for FY27**? | Directly tests TRIPWIRE 5 (consol margin <12% two quarters) and Kuiper economics | Kuiper to ~8% margin, consol back ≥12% | Kuiper stays ~4%, consol margin stays sub-10% | A3-F2, A3-F3, F2-1, FN1, FN5, FN6 |
| 3 | 17.6% of consolidated Q1 PAT (Rs 2.24 Cr of Rs 12.76 Cr) comes from 21 subsidiaries and 5 JVs **reviewed by no auditor**, and one subsidiary posted a **Rs 3.26 Cr loss on nil revenue**. Which entities are these, why is the loss shell consolidated, and will the **4 subsidiaries unbucketed in the review paragraphs** be brought under SGCO review? | Audit-coverage / data-quality of the consolidated numbers (A3-F4/F15/F3) | All Indian subs SGCO-reviewed next quarter; loss shell being wound down | Continued reliance on unreviewed, management-furnished numbers | A3-F4, A3-F15, A3-F3 |
| 4 | The 5 JVs (including **Asian Indwell**, prior work put at 26.9% of the related-party book) contributed Rs 0.79 Cr unreviewed share of profit. As of 30-Jun-2026, what is the **ageing of related-party receivables**, and how much is past **180 days**? | TRIPWIRE 3; RP receivables already ~56.4% of gross book | No RP receivable >180 days; collections current | Ageing >180 days, RP book growing | A3-F4, A3-F15 (RP overlay) |
| 5 | Standalone revenue grew **29.4% YoY — just below your 30-40% order-backed guide**. What is the **specific numeric FY27 revenue and EBITDA guidance** for standalone AESL and for Kuiper separately, and does the Rs 1,754 Cr order book (which excludes Kuiper and Oilmax) underwrite the 30-40%? | TRIPWIRE 4; deck reaffirms "FY27 guidance" but gives no number (F6-2) | Numeric guide given, standalone on ≥30% | No number; "confident" only; standalone slipping | A3-F12, F6-2, FN1 |
| 6 | The exceptional-items line printed nil this quarter but carried **Rs 9.4 Cr in FY26** (Rs 2.72 Cr contractual-dispute write-off per the Outside Expert Council + Rs 6.69 Cr Kuiper acquisition cost). Is the **Outside Expert Council contractual dispute fully and finally closed**, or could the line reappear around the merger close? | Armed exceptional line (A3-F1); merger-close cost risk | Dispute closed, no further charge | Dispute open; further write-off possible | A3-F1, F1-1 |
| 7 | Why did **Walker Chandiok & Co LLP exit** and SGCO & Co LLP take over as statutory auditor from this quarter? Were there any disagreements on accounting or disclosure, and does SGCO concur with all prior-period classifications? | Auditor transition + first-review continuity risk (A3-F5); note-drafting errors (A3-F14) | Routine rotation, clean handover | Disagreement / restatement risk | A3-F5, A3-F14 |
| 8 | The Q1 interim gives no cash-flow statement. What were **standalone and consolidated CFO for Q1 FY27**, and TTM CFO/PAT, given prior-year cash conversion was a single positive FY26 print after two negative years? | TRIPWIRE 2; cash conversion INDETERMINATE this quarter | Positive CFO, TTM CFO/PAT ≥1x | Negative CFO while revenue grows | Cash tripwire 2 (all-doc silence) |
| 9 | Kuiper "stabilized in June" after a "volatile Middle East situation" — implying **April-May weakness**. What was Kuiper's monthly revenue/EBITDA trajectory in Q1, its **customer concentration**, and Middle East/Nigeria exposure as % of Kuiper revenue? | Kuiper lumpiness/geopolitics (F7-1, FN4) | Diversified, monthly recovery structural | Concentrated, single-customer, geopolitics-driven | F7-1, FN4 |
| 10 | The investor-deck P&L shows YoY growth **only on revenue/EBITDA/PAT** and leaves every **cost line (all up faster than revenue) and EPS blank**; paid-up capital rose 8.7% YoY. Will you disclose full YoY cost lines and reconcile the share-count increase to the warrant conversion? | Selective-disclosure governance (F16-1) + dilution (F10-1) | Full disclosure, clean reconciliation | Continued selective framing | F16-1, F10-1 |
| 11 | Confirm the **Rs 1,754 Cr order-book definition** (standalone, ex-Kuiper/Oilmax, ex-GST, no as-on date): gross or net, executed or pending, and does it include the **GSECL Rs 187.6 Cr** order? When do the **DSF-IV block and Pakro mine "preferred bidder"** awards convert to signed contracts? | Order-book integrity (F16-2, FN7) + preferred-bidder conversion (FN3, F16-3) | Clear definition, awards converting on schedule | Definition drifts; awards stall | F16-2, F16-3, FN3, FN7 |
| 12 | Of the FY27 production-start commitments (**Amguri IGGL, Tiphuk, Duarmara, Quartzite Mine, Mewad ~1,000 bopd**), which are contracted to contribute **revenue in FY27**, and what boe/revenue contribution is expected? | Catalyst timeline into FTTCP (F6-1, A3-F6) | Named FY27 revenue contribution | All "focus", none contracted for FY27 revenue | F6-1, A3-F6 |

**Top 3 by likelihood of thesis-changing information:**
1. **Q1 (Oilmax accounting basis + dilution)** — a fair-value / low-dilution answer would raise the bull case; a pooling-at-book / 35-51% dilution answer confirms the core bear thesis and moves toward firing tripwire 1.
2. **Q2 (Kuiper sustainable margin + FY27 consol margin guide)** — the answer that most directly confirms or refutes tripwire 5.
3. **Q7 (auditor transition)** — tests management transparency; an evasive answer on why Walker Chandiok exited, combined with the 17.6% unaudited-PAT reliance, is itself a governance signal.

**Channel recommendation:** **IR email with all 12 questions verbatim**, plus AGM Q&A. No concall was hosted; these become the pre-committed watchpoints for the Q2 FY27 review's answer-status audit.

STOP cleared.

---

## STEP 9 — NOTION UPDATE (state, not executed here)

No live Notion page exists for this ticker (search returned none; durable memory `companies/ASIANENE.md` is the record). Row properties **unchanged**: Decision Status AVOID / DEEP WATCH; Position zero at CMP; Promoter Verdict CONCERN; entry Rs 75-93 / MoS Rs 75. Key Note to prepend at /finalize: *"2026-08-13 Q1FY27: AVOID confirmed; +135% rev / +129% PAT is Kuiper base-effect; consol op-EBITDA margin 7.8% (tripwire-5 armed, 1st sub-12% qtr); standalone rev +29.4% just below guide (tripwire-4 soft miss); GSECL Rs 187.6 Cr order won but into a declining-profit Mineral segment (result −13.2% YoY), all segment-profit growth is O&G; 17.6% of PAT unaudited; Oilmax dilution basis still undisclosed; cash INDETERMINATE (no Q1 CFO). No tripwire fired; gate → Q2 half-yearly."* This review is the institutional-memory artifact.

---

## MONITORABLES / CATALYST LIST (seeded by A3 commitment registers F6 + board-outcome forward items)

| Item | Implied date | Source ref | Status word |
|---|---|---|---|
| Oilmax merger — final NCLT hearing | 28 Aug 2026 | deck slide 8 L226 | scheduled |
| Oilmax merger — completion + **accounting basis disclosure** (TRIPWIRE 1) | Sep/Oct 2026 | results note 5 L362-369; deck L714; PR L115-116 | underway |
| **Q2 FY27 half-yearly filing — mandatory CFO + balance sheet** (resolves TRIPWIRE 2, 3, net-debt leg of 5) | ~Nov 2026 | Reg 33 | pending |
| GSECL Ukai coal-handling plant Rs 187.6 Cr — execution | FY27 | deck slide 8 L232-233 | commenced (**AMBER — order into declining-profit Mineral segment; segment result −13.2% YoY, L317**) |
| Amguri IGGL connections — ramp production | FY27 | deck slide 19 L669 | underway |
| Tiphuk — start commercial production (50,000 SCMD in EWT) | FY27 | deck slide 19 L653, L670 | initiated |
| Duarmara — commercial production (40 MMBOE, testing underway) | FY27 | deck slide 19 L658-659 | underway |
| Chhattisgarh CBM — core drilling / test-well (~2-yr) | FY27 / ~2yr | deck slide 19 L655-657 | underway |
| Uttarakhand Quartzite Mine (7.6 MMT) — permissions & start | FY27 | deck slide 19 L668-671 | initiated |
| Mewad/Indrora — scale to ~1,000 bopd | FY27 onwards | deck slide 18 L611-632 | underway (rig mobilised) |
| Oilmax production ~2,500 → ~10,000 boepd | FY29/30E | deck slide 19 L640; slide 21 L729 | target |
| Kuiper revenue ~US$60-70Mn → ~US$100Mn (~8% margin) | by FY29 | deck slide 21 L734-736 | target |
| DSF-IV block + Pakro critical-mineral mine — preferred-bidder → signed award | pending | deck slide 8 L242-243; PR L119-120 | pre-award |
| Warrant conversion 36,62,702 shares — reflected in paid-up | done (05-May-2026) | results note 7 L396-397 | completed |
| Kuiper PPA / capital reserve Rs 39.97 Cr | done (Q4 FY26) | results note 4 L355-360 | completed |

---

## PLAIN-LANGUAGE BRIEF (mandatory; provenance-labelled: [Notion/prior] vs [this-quarter filing] vs [not disclosed])

### 1. SUMMARY NARRATIVE

Asian Energy reported a loud quarter: revenue up 135% to Rs 271.2 crore, EBITDA up 81% to Rs 21.9 crore, PAT up 129% to Rs 12.8 crore [this-quarter filing, L245/L269; deck slide 9]. Almost all of the growth is optical. The Kuiper business was folded in only from 1 September 2025, so the June-2025 base carries none of it [this-quarter filing, deck footnote L297]. Strip Kuiper out and the standalone company grew revenue 29.4% and PAT 56%, with margins actually improving [this-quarter filing, L527/L550] — a decent but unspectacular quarter that sits just under the company's own 30-40% growth guide [Notion/prior guide]. The consolidated picture is weaker than the headline: operating EBITDA margin fell from 9.9% to 7.8% (the deck's own EBITDA margin fell from 10.5% to 8.1%), because the extra Rs 122 crore of subsidiary revenue earned only about 4% margin [this-quarter filing, derived from L245/L527]. The subsidiaries are asset-light manpower shells — consolidated depreciation barely moved despite 2.4x the revenue [this-quarter filing, L254 vs L536]. Earnings quality is the real story: 17.6% of consolidated PAT (Rs 2.24 crore) was reviewed by no auditor, one subsidiary lost Rs 3.26 crore on zero revenue, and the statutory auditor changed this year from Walker Chandiok to SGCO [this-quarter filing, L112-144, L158-162]. Share count rose 8.7% on a warrant conversion [this-quarter filing, L293], and the far larger Oilmax reverse-merger dilution — the pivotal thesis risk — is still not in the numbers, with its accounting basis (fair-value vs pooling-at-book) undisclosed [not disclosed]. The one order-win of the quarter (GSECL Ukai, Rs 187.6 crore) reads as a positive but lands in the Mineral & other energy segment whose YoY segment result actually shrank Rs 4.69 to 4.07 crore, −13.2% [this-quarter filing, L317], with every rupee of group segment-profit growth coming from Oil & Gas [L316]. No cash-flow statement is required at Q1, so cash conversion is INDETERMINATE this quarter [this-quarter filing, Reg 33]. Against the thesis [Notion/prior], nothing changes: the name stays AVOID / DEEP WATCH at CMP Rs 340, entry zone Rs 75-93 unchanged. No tripwire formally fired, but two are armed — consolidated margin below 12% (first of two quarters needed) and standalone growth just under the guide floor — and two more (negative CFO, related-party receivable ageing) can only be tested at the Q2 half-yearly filing. The decision gate moves to Q2 and to the Oilmax NCLT sanction (hearing 28 August, completion September/October 2026).

### 2. SECTOR INTELLIGENCE

The company sits in Indian oilfield / energy & mining services plus, increasingly, upstream E&P [this-quarter filing, press release L160-167]. The demand backdrop is genuinely supportive: government policy is pushing domestic energy security and import substitution — Samudra Manthan (Rs 84,084 crore upfront E&P capex), the ORDA Act 2025 (single petroleum lease for oil/gas/CBM), the Critical Minerals Mission, and DSF/CBM auction rounds [this-quarter filing, deck slides 14/19]. This is a structural tailwind for outsourced seismic, O&M, production-enhancement and material-handling work, and it is real, not narrative. The sector caveat the thesis already encodes: this is project/contract revenue, lumpy and tender-driven, with working-capital intensity and a related-party collection overlay [Notion/prior operator ruling: cash growth-induced with RP overlay]. This quarter shows how uneven the demand pull is across the two segments — all group segment-profit growth came from Oil & Gas (Rs 18.86 → 33.30 crore, L316) while the Mineral & other energy segment result fell −13.2% YoY (Rs 4.69 → 4.07 crore, L317) even as the company won a large Mineral order (GSECL) [this-quarter filing]. The Kuiper international leg (Middle East / Southeast Asia / Nigeria manpower) adds geopolitical exposure — management itself flagged "volatile Middle East situation" twice and said Kuiper only "stabilized in June" [this-quarter filing, deck L201/L291]. Sector cap for valuation is 20x (EPC/energy-services, explicitly NOT agri, despite the parent's agriculture subsidiary) [Notion/prior operator ruling]. Peer-level margin, order-book conversion, and receivable-cycle benchmarks are [not disclosed] in this document set; no peer reported in a comparable window for cross-check (no concall this quarter).

### 3. BUSINESS-MODEL INTELLIGENCE

AESL makes money three ways. (1) The core standalone business is asset-light integrated oil-&-gas services — seismic, O&M, production enhancement — plus mining material-handling; this quarter it ran a ~11% operating EBITDA margin on Rs 149 crore of revenue and is the healthiest piece [this-quarter filing, L527/derived]. (2) The consolidated overlay is Kuiper, a low-margin (~4% incremental this quarter, guided ~8%) international manpower/crew business bought in 2025; it triples reported revenue but adds little margin and carries the audit-coverage and geopolitics problems [this-quarter filing, derived]. (3) The forward model is upstream E&P via the Oilmax merger — owned oil-&-gas blocks (~70 mn barrels, five blocks, >50% EBITDA margin, ~US$5/bbl cost) targeting ~2,500 → 10,000 boepd by FY29/30 [this-quarter filing, deck slide 21] — which would shift the company from asset-light services toward asset-heavy production, meaningfully changing its depreciation, debt and ROCE profile. Model drift this quarter: the reported entity is being marketed as "An Oilmax Company" and "Oilmax-Asian" before the merger is legally effective [this-quarter filing, deck L143/L808], and the P&L is presented selectively (growth shown only on favourable lines, cost lines and EPS left blank) [this-quarter filing, deck slide 12]. Unit economics to watch: the Mineral order book (~Rs 699 crore) is very large against a ~Rs 26 crore/quarter Mineral revenue run-rate [this-quarter filing, L312/deck slide 26] — a long backlog with thin execution, and the segment's YoY profit is currently shrinking (−13.2%, L317) even as new Mineral orders are booked. Structural cash quality was already judged growth-induced with a related-party overlay [Notion/prior]; this quarter adds no CFO evidence either way [not disclosed at Q1].

### 4. COMPETITION INTELLIGENCE

Where AESL wins: an integrated, end-to-end upstream service spectrum (exploration → development → production → abandonment) with in-house technical depth, a Rs 1,754 crore standalone third-party order book giving 2-3 years of visibility, and marquee anchor work (Vedanta contract on "firm footing", ONGC/Oil India pipeline, and a new GSECL Rs 187.6 crore coal-handling order — though that order lands in the Mineral & other energy segment whose YoY segment result actually fell Rs 4.69 to 4.07 crore, −13.2% [this-quarter filing, L317], with all group segment-profit growth coming from Oil & Gas [L316], so the win is an order-level positive over a shrinking-profit segment, not yet a profit-level one) [this-quarter filing, deck slides 8/11/21/26]. The Oilmax combination is pitched as making it a rare listed integrated "asset-light services + owned E&P assets" platform [this-quarter filing, deck slide 15]. Where it is structurally weaker: it is a small-cap contractor competing for tenders against larger, better-capitalised oilfield-service and EPC players; its consolidated margin (~8%) is thin and Kuiper is a commoditised manpower business exposed to single-region geopolitics; and its governance profile (promoter CONCERN, 55.99% promoter-parent OEPL, dense related-party structure, 17.6% of PAT unaudited, selective disclosure, auditor change) is a competitive disadvantage in the one thing small-caps must earn — investor trust [this-quarter filing, L171, L112-144; Notion/prior promoter CONCERN]. Named-peer win/loss and market-share data are [not disclosed] in this document set. The competitive risk to watch: order-book conversion slipping (standalone growth already just below guide) while the low-margin Kuiper leg and an unpriced Oilmax dilution absorb the equity story — the classic small-cap trap of growing revenue and share count faster than per-share value. This is exactly why the standing verdict is AVOID at Rs 340 and re-engage only at Rs 75-93 with the entry conjunction satisfied [Notion/prior].

---

```yaml
stage: A4-analyst
company: "ASIANENE"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation, pressrelease]   # no concall in doc set; Role 5 N/A
ledger_reconciliation:
  notes: 17
  turns: 0            # no concall in doc set
  slides: 34
  all_reviewed: true
  a3_findings_incorporated: ["A3-F1","A3-F2","A3-F3","A3-F4","A3-F5","A3-F6","A3-F10","A3-F11","A3-F12","A3-F14","A3-F15","F1-1","F2-1","F6-1","F6-2","F7-1","F7-2","F10-1","F14-1","F16-1","F16-2","F16-3","FN1","FN2","FN3","FN4","FN5","FN6","FN7"]
protocol_verdict: "PROCEED WITH FLAGS"   # capped at/below PROCEED WITH CAVEATS by INDETERMINATE cash conversion (missing Q1 CFO); flags surfaced, no mechanical failure, no tripwire fired
cash_conversion: "INDETERMINATE"   # no cash-flow statement in a Q1 Reg 33 filing; prior operator ruling growth-induced with RP overlay carried forward unrefreshed; missing evidence: consol+standalone CFO, WC movement, receivable ageing, net debt
decision_status_verified: "AVOID (on-valuation) / DEEP WATCH — CMP Rs 340, entry Rs 75-93, zero position at CMP (non-held)"
position_branch: "8A-W"
sc_gap_pat_pct: ["Q1FY26: -7.8%", "Q4FY26: +43.9%", "Q1FY27: +33.5%"]
questions_for_management:
  - {q: "Oilmax merger accounting basis (fair-value vs pooling-at-book), exact share-exchange ratio, new shares, pro-forma EPS dilution; does 117:10 / ~53x stand?", from_finding_id: ["A3-F6","A3-F10","F10-1","FN2","F7-2","F14-1"]}
  - {q: "Sustainable Kuiper EBITDA margin and FY27 consolidated EBITDA-margin guide, given consol margin fell to 8.1% and ~4% incremental subsidiary margin", from_finding_id: ["A3-F2","A3-F3","F2-1","FN1","FN5","FN6"]}
  - {q: "Identity of the 21 unreviewed subs + 5 unreviewed JVs (17.6% of PAT) and the Rs 3.26 Cr nil-revenue loss shell; will the 4 unbucketed subs come under SGCO review?", from_finding_id: ["A3-F4","A3-F15","A3-F3"]}
  - {q: "Related-party receivable ageing at 30-Jun-2026 and amount past 180 days (RP ~56.4% of gross book; Asian Indwell JV)", from_finding_id: ["A3-F4","A3-F15"]}
  - {q: "Specific numeric FY27 revenue/EBITDA guidance for standalone AESL and Kuiper separately; does the Rs 1,754 Cr order book underwrite 30-40% given standalone rev +29.4%?", from_finding_id: ["A3-F12","F6-2","FN1"]}
  - {q: "Is the Outside Expert Council contractual dispute fully closed, or could the exceptional line (Rs 9.4 Cr FY26) reappear around the merger close?", from_finding_id: ["A3-F1","F1-1"]}
  - {q: "Why did Walker Chandiok exit and SGCO take over; any disagreements; does SGCO concur with all prior-period classifications?", from_finding_id: ["A3-F5","A3-F14"]}
  - {q: "Standalone and consolidated Q1 FY27 CFO and TTM CFO/PAT (no cash-flow statement in the Q1 filing)", from_finding_id: ["cash-tripwire-2"]}
  - {q: "Kuiper monthly Q1 trajectory, customer concentration, and Middle East/Nigeria exposure as % of Kuiper revenue ('stabilized in June')", from_finding_id: ["F7-1","FN4"]}
  - {q: "Disclose full YoY cost lines and EPS on the deck P&L; reconcile the +8.7% share count to the warrant conversion", from_finding_id: ["F16-1","F10-1"]}
  - {q: "Confirm Rs 1,754 Cr order-book definition (gross/net, executed/pending, GSECL inclusion, as-on date); DSF-IV + Pakro preferred-bidder → signed-contract timeline", from_finding_id: ["F16-2","F16-3","FN3","FN7"]}
  - {q: "Which FY27 production-start commitments (Amguri/Tiphuk/Duarmara/Quartzite/Mewad) are contracted to contribute FY27 revenue, and how much?", from_finding_id: ["F6-1","A3-F6"]}
monitorables:
  - {item: "Oilmax merger final NCLT hearing", implied_date: "2026-08-28", source_ref: "deck slide 8 L226"}
  - {item: "Oilmax merger completion + accounting-basis disclosure (TRIPWIRE 1)", implied_date: "2026-09/10", source_ref: "results note 5 L362-369; PR L115-116"}
  - {item: "Q2 FY27 half-yearly filing — mandatory CFO + balance sheet (resolves TRIPWIRE 2, 3, net-debt leg of 5)", implied_date: "2026-11 (approx)", source_ref: "Reg 33"}
  - {item: "GSECL Ukai coal-handling plant Rs 187.6 Cr execution — AMBER: order into declining-profit Mineral segment (segment result -13.2% YoY, L317; all segment-profit growth is O&G, L316)", implied_date: "FY27", source_ref: "deck slide 8 L232-233; results L316-L317"}
  - {item: "Amguri IGGL / Tiphuk / Duarmara production starts", implied_date: "FY27", source_ref: "deck slide 19 L653-670"}
  - {item: "Uttarakhand Quartzite Mine permissions & production", implied_date: "FY27", source_ref: "deck slide 19 L668-671"}
  - {item: "Mewad/Indrora scale to ~1,000 bopd", implied_date: "FY27 onwards", source_ref: "deck slide 18 L611-632"}
  - {item: "Oilmax ~2,500 → 10,000 boepd", implied_date: "FY29/30E", source_ref: "deck slide 19 L640; slide 21 L729"}
  - {item: "Kuiper revenue to ~US$100Mn (~8% margin)", implied_date: "FY29", source_ref: "deck slide 21 L734-736"}
  - {item: "DSF-IV block + Pakro mine preferred-bidder → signed award", implied_date: "pending", source_ref: "deck slide 8 L242-243; PR L119-120"}
flags:
  - "GSECL RE-CAST (A5 loop-back): Rs 187.6 Cr GSECL Ukai order won BUT into the Mineral & other energy segment whose YoY segment RESULT FELL Rs 4.69->4.07 Cr, -13.2% (L317); all group segment-profit growth is O&G Rs 18.86->33.30 Cr (L316). Watchlist item 4 and growth-trigger GSECL re-cast GREEN/FIRED -> AMBER (order-level win into a shrinking-profit segment)"
  - "TRIPWIRE 5 ARMED: consolidated operating EBITDA margin 7.80% (deck 8.1%), first sub-12% quarter; a second sub-12% quarter in Q2 FY27 fires the margin leg (net-debt leg cannot assess, net debt ND)"
  - "TRIPWIRE 4 SOFT MISS: standalone revenue +29.4% YoY, just below the 30-40% order-backed guide floor; first data point, not the third consecutive"
  - "TRIPWIRE 2 CANNOT ASSESS: no cash-flow statement in a Q1 Reg 33 filing; cash conversion INDETERMINATE; first testable at Q2 half-yearly"
  - "TRIPWIRE 3 CANNOT ASSESS: no balance sheet/receivable ageing at Q1; RP overlay present (5 unreviewed JVs incl Asian Indwell, Rs 0.79 Cr share of profit)"
  - "TRIPWIRE 1 AMBER: Oilmax merger accounting basis (fair-value vs pooling-at-book) and dilution ratio undisclosed; NCLT hearing 28-Aug, completion Sep/Oct 2026; dilution not yet in the +8.7% share count"
  - "EARNINGS QUALITY: 17.6% of consolidated PAT (Rs 2.24 Cr) reviewed by no auditor; one subsidiary Rs 3.26 Cr loss on nil revenue; 4 subs unbucketed in review paras; auditor changed Walker Chandiok -> SGCO (first SGCO review)"
  - "S-vs-C PAT gap swung ~41 pp (-7.8% -> +33.5% of standalone PAT) on Kuiper consolidation; group earnings now depend on ~4%-margin asset-light manpower shells"
  - "DISCLOSURE FRAMING: deck shows YoY growth only on favourable lines, cost lines + EPS blank; margin compression buried; 'An Oilmax Company' branding pre-merger-effectiveness"
  - "DILUTION STACK: +8.7% shares YoY (warrant conversion) already in; Oilmax reverse-merger 35-51% dilution still ahead and unpriced"
  - "Other equity blank in all interim columns (L295/L565); consolidated net worth and ROCE not derivable at 30-Jun-2026"
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/asianene-q1fy27/work/review_asianene_q1fy27.md"
```
