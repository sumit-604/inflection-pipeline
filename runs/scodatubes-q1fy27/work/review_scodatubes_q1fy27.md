# A4 ANALYST — MERGED QUARTERLY REVIEW (RESULTS + INVESTOR PRESENTATION)

**Company:** Scoda Tubes Limited (SCODATUBES) | **Quarter:** Q1 FY27 (quarter ended 30 June 2026)
**Docs in scope (TWO, merged):** (1) Reg 33 RESULTS filing (Board Outcome + Limited Review Report); (2) Q1 FY27 INVESTOR PRESENTATION (40-slide earnings deck, filed 13 Aug 2026).
**Role 4 (Quarterly Results Review Protocol v1.2):** executed in full step sequence below — the **spine** of this review. The presentation findings **feed Role 4** (they resolve, corroborate, or worsen Role-4 line items and are woven into the relevant steps).
**Role 5 (Quarterly Concall Analysis Protocol v1.1):** **N.A. this run.** There is still **no concall transcript** in scope. All Role 5 steps (claims inventory, forward-guidance table, promise-vs-delivery credibility ratio, Q&A decomposition, tone/specificity archetype) are therefore **not executed and marked N.A.**; the concall-silence consequences and the deck's forward statements are instead carried as commitment-register items, ND-register monitorables, and management questions. Role 5 begins at the H1 FY27 concall (if held, Nov 2026).
**Model:** claude-opus-4-8 | **Conservative bias on interpretation; zero bias on extraction.**
**Units:** RESULTS filing filed in **Rs Millions** (Rs Crore = Millions x 0.1); DECK filed in **Rs Crore** (x1, per slide qualifiers "INR Crores Unless Otherwise Mentioned"). All analysis in **Rs Crore**. Every table cell is a line-anchored number (results `L##` = line in the results A1 extract; deck `p##`/`dL##` = slide/line in the presentation A1 extract) or the literal **ND**.
**Provenance tags used throughout:** `[RESULTS]` = this-quarter results filing (reviewed/audited by LRR); `[DECK]` = this-quarter investor presentation (UNAUDITED management representation, to be confirmed at audited H1 FY27); `[NOTION]` = prior thesis / peer work.

> **THIS FILE OVERWRITES the prior results-only review at the same path.** It is the complete MERGED review (complete tables, not summaries). No corrected grid number is regressed; the deck independently confirms the corrected results grid (deck EBITDA -172 bps, PAT -25.9%/-305 bps match the pipeline's corrected filing — A3 F16-5).

> **A5 ADVERSARY GRAFT 1 (retained):** the −172 bps operating EBITDA margin miss is an **ABOVE-EBITDA** event driven by **Other Expenses +80.9% YoY**, NOT a depreciation/finance (below-EBITDA) event. Operating EBITDA excludes depreciation and finance by construction. The deck now supplies the causal narrative for this line (A3 F7-1: freight/RM volatility, 3-4 month pass-through lag, April gas outage, manpower) — folded into Step 2, Step 4, Q9.
>
> **A5 ADVERSARY GRAFT 2 (retained):** the +283 bps net-material "improvement" is an **inventory-build cost-deferral artifact, NOT a unit-economics gain**. Raw material CONSUMED / revenue WORSENED +434 bps (76.22% → 80.55%, `[RESULTS]` L85/L81); the FG/WIP build credit rose +717 bps (5.39% → 12.56%, L86/L81); net −434 + 717 = +283 bps. The same Rs15.61 Cr FG/WIP build (+197.6% YoY, L86) that flatters gross margin is the negative cash-conversion proxy in Step 5. The DECK now confirms the cash face of this event directly: FY26 annual CFO −13.8 Cr and inventory days 217 (A3 F16-1/F16-4/F16-6). One event, both faces now evidenced.

---

## LEDGER RECONCILIATION PREAMBLE (mandatory, BOTH ledgers, before Step 1)

**RESULTS ledger contains 7 notes / 25 line-items / 3 zero-standing items / 1 agenda item / 4 auditor paras / 1 entity / 3 signatories. All reviewed.**
**PRESENTATION ledger contains 40 slides / 624 numbers / 48 footnotes (0 dropped-slide checks — first deck for this ticker, no prior deck to diff). All reviewed.**
(There are still **no concall turns** in scope: turns = 0, N.A.)

RESULTS ledger rows read verbatim at their A1 lines:
- Notes (7): L115, L118, L120, L122, L123, L125, L127.
- Line-items (25): L81–L112 value-bearing rows.
- Zero-standing (3): L93 Exceptional items, L97 Earlier-year taxes, L111 EPS-Discontinued — blank in all 4 periods.
- Agenda (1): L38-39. Auditor paras (4): L158-161/162-167/169-178/179-185. Entity (1): L123-124 (standalone; no subsidiary/JV/associate). Signatories (3): L51-53 (MD, DIN 06785595), L141-143 (Chairman/WTD, DIN 08036100), L188-197 (auditor partner M.No.134475, UDIN 26134475LRVGGI8483).

PRESENTATION ledger rows read verbatim: all 40 slide rows (Table 1), all 624 number rows (Table 3, dL83-708), all 48 footnote rows (Table 4, dL716-763), both ZERO_STANDING rows (p25 dL875 FY25 opening-cash dash; p10 dL360 FY23 blank YoY). A2 GATE PASS on both (results 7/25/3/1/4/1/3; deck 40/624/48). Deck count-test: raw grep 624 = sweep 624 (net-zero 5-item correction documented).

**A3 findings incorporated — BOTH forensics (19 total):**
- **RESULTS forensics (6):** F8-1 (FORWARD-SIGNAL), F9-1 (AMBIGUOUS), F10-1 (AMBIGUOUS → now resolved-with-explanation via deck, see Step 0C), F14-1 (CONFIRMATORY-NEGATIVE, data-integrity catch), F14-2 (FORWARD-SIGNAL), F14-3 (CONFIRMATORY-NEGATIVE). Results checklist 17/17, GATE A3 PASS.
- **PRESENTATION forensics (13):** F16-1 (CONFIRMATORY-NEGATIVE, CFO −13.8/cum 0.27x), F16-2 (AMBIGUOUS, Q1/FY26 period-blend), F16-3 (FORWARD-SIGNAL, ROCE 11.6% vs pillar), F16-4 (CONFIRMATORY-NEGATIVE, selective gross-margin framing), F16-5 (CONFIRMATORY-NEGATIVE, corrected-grid corroboration), F16-6 (FORWARD-SIGNAL, WC deterioration), F16-7 (AMBIGUOUS, D&A anomaly), F16-8 (CONFIRMATORY-NEGATIVE, withheld catalysts), F16-9 (AMBIGUOUS, capacity cross-slide), F6-1 (FORWARD-SIGNAL, H2 FY27 commissioning + reaffirmed guidance), F7-1 (FORWARD-SIGNAL, transient-headwinds narrative), F10-1/deck (NEUTRAL-FACT, IPO dilution), F14-1/deck (AMBIGUOUS, dual-Chairman), F14-2/deck (NEUTRAL-FACT, minor cross-slide discrepancies). Presentation checklist 17/17, GATE A3 PASS.

**No ledger row on either ledger is unreviewed. Proceeding to Step 1.**

**Data-integrity note carried forward:** the source RESULTS PDF embedded text layer carried a systematic "7-rendered-as-1" digit corruption across the three comparative columns (Q1FY27/Q4FY26/Q1FY26). It was caught by the footing test (A3 F14-1) and corrected by an A1 400-DPI OCR + footing re-extraction now footing 20/20 (extract L257-289). **This review uses the CORRECTED values.** Most material correction: Q1FY26 PAT corrupt 10.83 → corrected **70.83** (L99). **The DECK independently confirms the corrected grid** (deck Slide 8/36 print EBITDA margin −172 bps, PAT −25.9%, PAT margin −305 bps, EPS −39.1% — A3 F16-5), so the correction is now cross-validated against a second, management-sourced document.

---

## STEP 0 — PRE-FLIGHT

### 0A. Notion baseline (verified before any framing)
- **Decision Status: AVOID (mildly). Position Size: ZERO (tracking only)** `[NOTION]`. Analysis date 02 Jun 2026, CMP then Rs122.88, market cap Rs736.10 Cr, diluted shares 5.9909 Cr, promoter 66.43% EXEMPLARY. **NON-HELD name → Step 8A-W branch applies, not 8A. No trim/exit mechanics.**
- One-line thesis `[NOTION]`: AVOID at CMP Rs122.88; FY26 EPS base → FY29 base Rs185 at destination PE 15x = ~14.6% CAGR; prob-weighted 9.9% vs 25% hurdle. Re-engage at Rs95 IF 6 of 9 operating triggers clear by Q2 FY27 (Nov 2026).
- Entry framework `[NOTION]`: BUY < Rs95; WATCHLIST Rs95-115; AVOID > Rs115. MoS Rs76. Destination PE 15x (13-17x), Venus-anchored, Pillar-1 ROCE assumption ~16-17%. FY29 fair values Bear Rs91 / Base Rs185 / Bull Rs284.
- THESIS BROKEN IF `[NOTION]`: cumulative FY22-FY27 CFO/PAT < 0.30x (measured at FY27-end) OR inventory days >180 at end FY27 OR welded utilisation <25% at end FY28 OR BHEL tender lost / volumes <Rs75 Cr.
- Nine re-engagement triggers, all Pending. Gate 0 AVOID (deal-breakers: <5yr history, cash 5/20, cumulative CFO/PAT −0.09x FY22-25). Peer context (Sheet 3): Scoda materially worse on cash conversion/inventory/receivables/disclosure/scale; better on promoter quality (EXEMPLARY 66.43%)/anchors; destination PE 15x vs Venus 22x.

### 0B. Unit convention
RESULTS header L71: "(Rs in Millions except Earnings per share)" → **Millions, x0.1 to Cr**. DECK: "INR Crores Unless Otherwise Mentioned" (dL788/818/853/1279) → **Crore, x1**. Both reconcile: results Revenue 1,243.45 Mn = 124.345 Cr `[RESULTS]` L81 ↔ deck 124.3 Cr `[DECK]` p8 dL274 / p36 dL1283. EPS per-share, not annualised.

### 0C. Share-count changes — F10-1 now RESOLVED-WITH-EXPLANATION (deck)
Paid-up equity flat **Rs599.09M = 59.909M shares** across all four period-ends `[RESULTS]` L106. The results filing's EPS comparatives did NOT reconcile to that flat base (A3 results F10-1): Q1FY26 EPS 1.44 on PAT 70.83 implies ~49.2M weighted shares; FY26 6.79 implies ~57.2M; only Q1FY27 ties (52.50/59.909 = 0.88). **The DECK resolves this** (A3 F10-1/deck, NEUTRAL-FACT): deck EPS FY25 **7.6** EXCEEDS FY26 **6.8** despite FY26 PAT (38.8) > FY25 PAT (31.7) `[DECK]` p23 dL806/dL809 — the signature of **IPO share-count dilution**. Deck confirms "Raised INR 220 crores through public issue" (p12 dL436) and equity+reserves jumping **150.4 → 390.3** (p24 dL834). The listing occurred within FY26 (deck Slide 12 milestone year 2026), so weighted average shares stepped up mid-FY26, explaining the non-reconciliation. **F10-1 status: AMBIGUOUS → RESOLVED-WITH-EXPLANATION (IPO dilution).** Residual (not resolvable from deck's combined "equity capital and reserves"): the exact paid-up split and whether prior-period EPS is restated per Ind AS 33 — kept as a narrower management question (Q3). Share-adjusted EPS across periods still marked ND at the filing level.

### 0D. Numbered-notes extraction (RESULTS, mandatory, full)

| Note # | Line | Subject | What It Says (1 sentence) | Rs Cr Impact | Period | Comparability Impact |
|---|---|---|---|---|---|---|
| 1 | L115 | Approval / review | Reviewed by Audit Committee, approved by Board 12 Aug 2026; auditor **unmodified** conclusion. | None | Q1FY27 | Clean. Drafting slip (F14-3): "quarter **and year** ended June 30, 2026" — template carry-over. Cosmetic. |
| 2 | L118 | Basis | Ind AS (s.133). | None | All | None. |
| 3 | L120 | Format | SEBI circular format modified per Ind AS / Sch III Div II. | None | All | None. |
| 4 | L122 | Single segment | "SS pipes and tubes only. Hence segment reporting ... not applicable." | None | All | **Material:** suppresses welded-vs-seamless split & utilisation (triggers 4, 8). **Deck also withholds these** (F16-8) — not cured by the deck. |
| 5 | L123 | No subsidiary | No subsidiary/JV/associate as on 30 Jun 2026; consol not applicable. | None | All | **S-vs-C gap structurally zero** (Step 4A). |
| 6 | L125 | Balancing figure | Q4FY26 column is the balancing figure between audited FY26 and unaudited 9M FY26. | None | Q4FY26 | Q4FY26 is DERIVED; QoQ caveat. |
| 7 | L127 | Regrouping | Prior figures regrouped/restated where necessary. | ND | Prior | Boilerplate (F7 PASS). |

**Auditor opinion (L179-185):** **Unmodified.** No EoM / Other Matters / Going Concern (F5 PASS). Firm Dhirubhai Shah & Co LLP, FRN 102511W/W100298 (L190); partner M.No.134475; UDIN 26134475LRVGGI8483 (L197). No AMBER from the opinion. **The DECK is UNAUDITED throughout** (deck Safe Harbor p39 dL1368 "can give no assurance") — every deck-only metric (CFO, ROCE, WC days, ratios) is a management representation to confirm at audited H1 FY27.

### 0E. Business type
**Standard operating (manufacturing)** — specialty stainless-steel seamless & welded pipes/tubes (deck Slide 15 product table; Slide 38 welded vs seamless process flows). Steps 1/5 (not lender 1L/5L) apply.

**STOP-0 cleared:** both docs' baselines fetched (Decision Status AVOID/ZERO verified `[NOTION]`), units reconciled (Millions x0.1 ↔ Crore x1), share-count change resolved (F10-1 = IPO dilution), all 7 notes + 40 slides extracted, auditor opinion unmodified, deck unaudited flagged, business type standard.

---

## STEP 1 — DATA EXTRACTION TABLE (STANDARD BUSINESS)

### 1.1 RESULTS grid (the spine — Rs Crore; filed Millions x0.1). Column map per header L76.

| Line Item | Q1 FY26 (L) | Q4 FY26 (L) | Q1 FY27 (L) | FY26 (L) |
|---|---|---|---|---|
| Revenue from Operations | 97.417 (L81) | 123.569 (L81) | 124.345 (L81) | 518.650 (L81) |
| Other Income | 1.761 (L82) | 4.403 (L82) | 1.630 (L82) | 10.571 (L82) |
| Total Income | 99.178 (L83) | 127.972 (L83) | 125.975 (L83) | 529.221 (L83) |
| Cost of Materials Consumed | 74.249 (L85) | 100.773 (L85) | 100.165 (L85) | 414.375 (L85) |
| Change in Inventories | (5.247) (L86) | (18.341) (L86) | (15.614) (L86) | (61.144) (L86) |
| Employee Benefits | 2.420 (L87) | 2.634 (L87) | 2.462 (L87) | 10.454 (L87) |
| Finance Costs | 5.104 (L88) | 8.139 (L88) | 6.481 (L88) | 24.866 (L88) |
| Depreciation & Amortization | 1.572 (L89) | 3.612 (L89) | 4.131 (L89) | 9.217 (L89) |
| Other Expenses | 11.805 (L90) | 21.798 (L90) | 21.353 (L90) | 78.721 (L90) |
| Total Expenses | 89.903 (L91) | 118.615 (L91) | 118.978 (L91) | 476.489 (L91) |
| Exceptional Items | ND (nil, L93) | ND (nil, L93) | ND (nil, L93) | ND (nil, L93) |
| Profit Before Tax | 9.275 (L94) | 9.357 (L94) | 6.997 (L94) | 52.732 (L94) |
| Current Tax | 1.890 (L96) | 2.572 (L96) | 0.625 (L96) | 11.633 (L96) |
| Deferred Tax | 0.302 (L98) | 0.466 (L98) | 1.122 (L98) | 2.256 (L98) |
| Total Tax Expense | 2.192 (L96+98) | 3.038 (L96+98) | 1.747 (L96+98) | 13.889 (L96+98) |
| PAT | 7.083 (L99) | 6.319 (L99) | 5.250 (L99) | 38.843 (L99) |
| OCI (net of tax) | 0.110 (L102+103) | (0.110) (L102+103) | 0.128 (L102+103) | 0.088 (L102+103) |
| Total Comprehensive Income | 7.193 (L104) | 6.209 (L104) | 5.378 (L104) | 38.931 (L104) |
| Paid-up Equity Capital | 59.909 (L106) | 59.909 (L106) | 59.909 (L106) | 59.909 (L106) |
| Other Equity | ND (L107) | ND (L107) | ND (L107) | 330.400 (L107) |
| EPS reported (Rs, not annualised) | 1.44 (L110) | 1.02 (L110) | 0.88 (L110) | 6.79 (L110) |
| EPS share-adjusted (Rs) | ND (F10-1) | ND (F10-1) | 0.88 (L110) | ND (F10-1) |

**Deck Q1 cross-check (A3 F16-5 — independent corroboration)** `[DECK]` p36 (Rs Cr, rounded): Revenue 124.3/97.4 (dL1283), Gross profit 39.8/28.4 +40.0% (dL1285), Employee 2.5/2.4 (dL1287), Other exp 21.4/11.8 +80.9% (dL1288), EBITDA 16.0/14.2 +12.6% (dL1290), EBITDA margin 12.9%/14.6% −172 bps (dL1292), Other income 1.6/1.8 (dL1294), D&A 4.1/1.6 +162.8% (dL1295), Finance 6.5/5.1 +27.0% (dL1296), PBT 7.0/9.3 −24.6% (dL1297), Tax 1.7/2.2 (dL1298), PAT 5.3/7.1 −25.9% (dL1300), PAT margin 4.2%/7.3% −305 bps (dL1302), EPS 0.9/1.4 −39.1% (dL1304). **Every deck line reconciles to the corrected results grid within rounding.** Note the deck's "EBITDA" is the OPERATING basis (GP − employee − other exp = 15.9 ≈ 16.0), matching my constructed operating EBITDA 15.979, so the deck itself confirms operating EBITDA margin ~12.85%.

### 1.2 Derived metrics (Rs Crore; each raw input anchored to its line)

| Derived Metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| **Operating EBITDA** | PBT + D + FinCost − OthInc | **14.190** | **16.705** | **15.979** | **76.244** |
| — working | | 9.275+1.572+5.104−1.761 | 9.357+3.612+8.139−4.403 | 6.997+4.131+6.481−1.630 | 52.732+9.217+24.866−10.571 |
| Operating EBITDA Margin | OpEBITDA/Rev | 14.57% | 13.52% | **12.85%** | 14.70% |
| Reported EBITDA | PBT + D + FinCost | 15.951 | 21.108 | 17.609 | 86.815 |
| Reported EBITDA Margin | RepEBITDA/Rev | 16.37% | 17.08% | 14.16% | 16.74% |
| Core PBT (ex-Other Income) | PBT − OthInc | 7.514 | 4.954 | 5.367 | 42.161 |
| Other Income / PBT | OI/PBT | 19.0% | 47.1% | 23.3% | 20.0% |
| Effective Tax Rate | TotalTax/PBT | 23.63% | 32.47% | 24.97% | 26.34% |
| Current-tax share of PBT | CurrTax/PBT | 20.38% | 27.49% | **8.93%** | 22.06% |
| PAT Margin (on Revenue) | PAT/Rev | 7.27% | 5.11% | 4.22% | 7.49% |

My FY26 Operating EBITDA 76.244 Cr ties to deck FY26 EBITDA **76.2** `[DECK]` p23 dL798 and FY26 margin 14.70% ties to deck **14.7%** dL799 — construction validated against the deck. Q4FY26 is a Note-6 balancing figure.

### 1.3 DECK-ONLY multi-year panels (supplementary — UNAUDITED management representation; used in Steps 5/6/7)

**Historic Income Statement (Slide 23, Rs Cr, FY26/FY25/FY24/FY23)** `[DECK]`:
Revenue 518.7/484.9/399.9/305.1 (3yr CAGR 19.3%, dL790); Gross profit 165.4/148.5/137.9/92.5 (21.4%, dL793); GP margin 31.9/30.6/34.5/30.3% (dL794); Employee 10.5/8.1/7.4/5.5 (dL795); Other exp 78.7/62.4/71.7/52.3 (dL796); EBITDA 76.2/78.1/58.8/34.8 (29.9%, dL798); EBITDA margin 14.7/16.1/14.7/11.4% (dL799); Other income 10.6/4.0/2.6/2.7 (dL800); **D&A 9.2/18.1/16.4/11.5 (dL801 — see F16-7 anomaly)**; Finance 24.9/22.0/19.1/11.6 (dL802); PBT 52.7/41.9/25.9/14.4 (54.2%, dL803); Tax 13.9/10.2/7.6/4.0 (dL804); PAT 38.8/31.7/18.3/10.3 (55.4%, dL806); PAT margin 7.5/6.5/4.6/3.4% (dL808); EPS 6.8/7.6/4.6/2.6 (dL809).

**Historic Balance Sheet (Slide 24, Rs Cr, FY26/FY25/FY24/FY23)** `[DECK]`:
Fixed assets 194.0/103.5/81.6/62.1 (dL820); Inventories 209.8/149.8/111.9/99.5 (dL823); Trade receivables 138.0/101.0/89.3/51.6 (dL825); Cash 74.2/43.9/22.4/10.4 (dL827); Total 687.9/446.4/330.4/238.3 (dL831); Equity+reserves 390.3/150.4/63.6/45.3 (dL834); Borrowings 185.3/210.2/202.7/139.3 (dL835); Trade payables 99.4/68.5/53.9/47.5 (dL837).

**Historic Cashflow (Slide 25, Rs Cr, FY26/FY25/FY24/FY23)** `[DECK]`:
CFO before WC 82.8/79.5/60.1/37.2 (dL861); Changes in WC −78.9/−54.6/−54.5/−15.0 (dL863); Taxes −17.6/−6.5/−3.4/−1.9 (dL865); **CFO −13.8/18.4/2.2/20.3 (dL867)**; CFI −149.9/−43.9/−46.6/−38.5 (dL869); CFF 152.7/40.6/44.3/17.9 (dL871).

**Consistency ratios (Slide 22, %, FY23/FY24/FY25/FY26)** `[DECK]`:
ROCE 12.6/15.9/16.6/**11.6** (dL770-774); ROE 28.8/22.8/21.1/**9.9** (dL752-757); Inventory Days 156/171/163/**217** (dL751-754); Debtor Days 62/82/76/**97** (dL770-775); CCC 151/162/164/**211** (dL770-773); Net D/E FY25 1.1 → FY26 **0.3** (dL756/dL759).

**STOP-1 cleared:** every results cell filled or ND; deck panels extracted with slide/line anchors and flagged UNAUDITED.

---

## STEP 2 — Q1 FY27 YoY COMPARISON (THE MOST IMPORTANT STEP)

Q1 FY27 (30/06/2026) vs Q1 FY26 (30/06/2025). All Rs Crore. `[RESULTS]` grid; `[DECK]` corroboration noted.

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 97.417 | 124.345 | **+27.64%** | Strong top-line (deck +27.6%, dL1283) |
| Operating EBITDA | 14.190 | 15.979 | +12.61% | Grew < revenue; **level partly inventory-inflated** |
| Operating EBITDA Margin | 14.57% | 12.85% | **−172 bps** | CONTRACTED (deck −172 bps, dL1292) |
| Depreciation | 1.572 | 4.131 | **+162.8%** | Capex absorption gap (BELOW EBITDA; deck dL1295) |
| Finance Costs | 5.104 | 6.481 | +26.98% | Debt-funded capacity (BELOW EBITDA; deck dL1296) |
| EBIT (operating) = OpEBITDA − D | 12.618 | 11.848 | **−6.10%** | Core operating profit fell |
| Other Income | 1.761 | 1.630 | −7.44% | Immaterial, down |
| **Core Operating PBT (PBT − OI)** | 7.514 | 5.367 | **−28.57%** | CONTRACTED — cleanest health test |
| Reported PBT | 9.275 | 6.997 | **−24.56%** | Down (deck −24.6%, dL1297) |
| PAT | 7.083 | 5.250 | **−25.88%** | Down (deck −25.9%, dL1300) |
| EPS reported (not annualised) | 1.44 | 0.88 | **−38.89%** | Worse than PAT (IPO dilution, F10-1; deck −39.1%, dL1304) |

### Operating EBITDA margin decomposition — ABOVE-EBITDA drivers (A5 graft 1 + graft 2)

**Operating EBITDA excludes depreciation and finance by construction, so those two lines CANNOT explain the −172 bps.** The contraction is entirely above-EBITDA. Ratios are (line/Revenue L81); raw values line-anchored `[RESULTS]`.

| Cost line (% of Revenue) | Q1 FY26 | Q1 FY27 | bps change | Effect on Op EBITDA margin |
|---|---|---|---|---|
| Raw material CONSUMED (L85) | 76.22% | 80.55% | **+434 bps** | **−434 bps (ADVERSE — RM intensity WORSENED)** |
| less: FG/WIP build credit (L86) | 5.39% | 12.56% | **+717 bps** | **+717 bps (favourable, but a build CREDIT = cost deferred to balance sheet)** |
| **= Net material (L85+L86)** | **70.83%** | **68.00%** | **−283 bps** | **+283 bps net — INVENTORY-BUILD-DRIVEN, not a unit-cost gain** |
| Employee benefits (L87) | 2.484% | 1.980% | **−50 bps** | **+50 bps (operating leverage on fixed labour)** |
| Other expenses (L90) | 12.117% | 17.173% | **+505 bps** | **−505 bps (adverse — the whole miss)** |
| **Net = Op EBITDA margin change** | **14.57%** | **12.85%** | | **+283 + 50 − 505 = −172 bps (reconciles)** |

**Read (two things, kept distinct):**
1. **The −172 bps operating margin miss (trigger 9 RED) is caused by Other Expenses +80.9% YoY** (L90: 11.805 → 21.353 Cr; 12.12% → 17.17% of revenue = −505 bps). Above EBITDA; nothing to do with depreciation/finance. **DECK NOW EXPLAINS THIS LINE (A3 F7-1 / F6-1):** the Chairman's commentary `[DECK]` p6 (dL192-206) attributes the quarter to freight/supply-chain cost increases, RM price volatility, a **3-4 month advance order-booking cycle** that "limited our ability to immediately pass on higher input costs" (dL194), an **April gas-supply disruption of ~2 weeks** (dL197), and manpower shortage — claimed "largely transient" (dL200), with FY27 guidance reaffirmed (no numeric target) and welded expansion "expected to be commissioned during H2 FY27" (dL205-206). The deck also confirms Other Expenses +80.9% is the driver (p36 dL1288). **This ANSWERS the prior results-review Q9** — see Step 8.5, Q9 now "management-answered, verify recovery at Q2." Conservative: a claim of transience is not proof; testable next quarter.
2. **The +283 bps net-material "improvement" is NOT a unit-economics gain — it is an inventory-build cost-deferral artifact.** RM consumed intensity WORSENED +434 bps (76.22% → 80.55%, L85); the offset is a bigger FG/WIP build credit +717 bps (5.39% → 12.56%, L86) — production ran ahead of sales, deferring Rs15.61 Cr of conversion cost onto the balance sheet. This is the SAME build that Step 5 flags as the cash burn. **DECK CONFIRMS BOTH FACES:** it headlines "Gross Profit +40.0% / +283 bps" as a win (p5 dL153, p8 dL292, p36 dL1286) while SUPPRESSING that (a) FY26 CFO was −13.8 Cr (p25 dL867) and (b) inventory days rose to 217 (p22 dL751) — the same build (A3 F16-4, selective disclosure). Marked ND on how much reverses → Q10.

**Six mandatory diagnostics:**
1. **Revenue grow YoY?** Yes, **+27.64%** — well above FY26 full-year +7% (`[DECK]` FY26 rev 518.7 vs FY25 484.9 = +7.0%, dL790/dL360). Deck's own FY26 YoY growth is 7.0% (dL360), confirming this quarter's +27.6% is a genuine acceleration. Top-line is the one good number.
2. **Op EBITDA margin?** **Contracted −172 bps to 12.85%** (deck 12.9%). Driver Other Expenses +80.9% (above EBITDA); net-material line looks favourable only on the inventory build (RM intensity actually rose +434 bps).
3. **Core operating PBT (ex-OI) grow?** **No — FELL 28.57%** (5.367 vs 7.514). Both core and reported PAT negative; headline masks no hidden strength — and this decline is UNDERSTATED to the extent the build props gross profit.
4. **Gap between core-PBT and reported-PAT changes?** They move together (−28.6% / −25.9%). Tax cushioned PAT by Rs0.445 Cr — but that is a **deferred-tax timing shield** (F8-1), not durable: current tax collapsed 20.38% → **8.93%** of PBT, offset by deferred tax rising 0.302 → 1.122 Cr.
5. **D&A / finance scaling faster than revenue?** **Yes.** Depreciation +162.8% and finance +27.0% vs revenue +27.6%. BELOW EBITDA — they convert ~+12.6% operating-EBITDA growth into −25.9% PAT (Step 4 bridge). Textbook capex absorption deficit; ROCE compresses until volume catches up. **Deck compounds this via F16-7 (see Step 4/7):** FY26 annual D&A was abnormally LOW (9.2, half FY25's 18.1) despite fixed assets nearly doubling — so the true run-rate D&A is far higher than FY26 suggests, and Q1's 4.1/qtr annualises to ~16.4.
6. **Other Income concentration?** No — small and stable (1.630 vs 1.761); not masking trajectory. Deck agrees (1.6 vs 1.8, dL1294).

**Step-2 read (corrected):** Revenue +27.6% but PAT −25.9%. **(a) ABOVE EBITDA** — Other-Expenses surge (+505 bps of revenue) compressed operating EBITDA margin −172 bps (trigger 9 RED); net-material cushion is an inventory-build credit masking a +434 bps RM-intensity worsening. The DECK supplies the causal story (transient freight/RM/gas/manpower) and confirms the number. **(b) BELOW EBITDA** — depreciation (+162.8%) and finance (+27.0%) turned positive operating-EBITDA growth into a −25.9% PAT decline, and FY26's understated D&A (F16-7) means the normalised fixed-cost base is heavier still.

**STOP-2 cleared.**

---

## STEP 3 — SEQUENTIAL QoQ + MULTI-YEAR TRAJECTORY

**3.1 QoQ (results):** Only three quarters extractable from the filing (Q1FY26, Q4FY26-balancing, Q1FY27). Q2/Q3 FY26 not separately disclosed → ND (not estimated).

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT ex-OI (Rs Cr) | One-offs Flagged | QoQ Run-Rate |
|---|---|---|---|---|---|
| Q1 FY26 | 97.417 (L81) | 14.57% | 7.514 | none | base |
| Q2 FY26 | ND | ND | ND | ND | ND |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 (balancing, Note 6) | 123.569 (L81) | 13.52% | 4.954 | Derived column; OI 4.403 elevated | step-up on revenue |
| Q1 FY27 | 124.345 (L81) | 12.85% | 5.367 | Deferred-tax shield (F8-1); OCI reset (F9-1); Other Expenses surge (L90); FG/WIP build (L86) | **plateau on revenue, margin still sliding** |

**3.2 Multi-year annual trajectory (deck Slide 23 — NEW context)** `[DECK]`: Revenue 305.1→399.9→484.9→518.7 (FY23-26); EBITDA margin 11.4→14.7→16.1→14.7%; PAT 10.3→18.3→31.7→38.8; **but FY26 revenue growth only +7.0% (dL360)** vs the 19-31% of prior years — the top-line had already decelerated sharply into FY26 before Q1 FY27's +27.6% re-acceleration.

**Diagnostics:**
- **Run-rate:** Revenue **plateaued** QoQ (+0.63% vs Q4FY26). Operating EBITDA margin slid three visible readings: 14.57% → 13.52% → 12.85%. PAT fell QoQ −16.92%.
- **One-offs:** Q4FY26 is Note-6 balancing (derived, elevated OI 4.403); Q1FY27 carries the deferred-tax shield, Other-Expenses step-up, and the gross-margin-flattering build. Neither is a clean comparator.
- **H1-vs-Q4 capex-commissioning test:** the welded plant is capitalising and depreciating (depreciation 3.612 → 4.131 QoQ; +162.8% YoY), yet Q1FY27 revenue is essentially flat on Q4FY26. **A commissioned plant that does not lift the run-rate above the pre-commissioning quarter is the protocol's named red flag.** Deck confirms welded commissioning is still forward ("expected to be commissioned during H2 FY27", F6-1) — i.e., the fixed-cost signature already in the P&L is largely the seamless-expansion/general capex, and the welded revenue ramp is still ahead.
- **Implied Q2 base:** revenue must exceed ~Rs124.3 Cr AND operating EBITDA margin must stop falling (≥12.85%) to arrest the slide; to clear trigger 9 it must reach ≥14% operating, which needs Other-Expenses (17.17%) to fall AND gross margin to hold as the build normalises.

**STOP-3 cleared.**

---

## STEP 4 — OPERATIONAL DECOMPOSITION

### 4A. Standalone-vs-Consolidated gap (first-class metric, A3 F2)
**Structurally ZERO.** Note 5 (L123-124): no subsidiary/JV/associate; no consolidated statement exists — standalone IS the group. Deck is likewise standalone (cover letter dL54 "Unaudited Standalone Financial Results"), so no S-vs-C gap appears in either document.

| Period | Standalone PAT (Rs Cr) | Consolidated PAT | S-vs-C PAT gap |
|---|---|---|---|
| Q1 FY26 | 7.083 (L99) | N.A. (none exists) | **0.00%** |
| Q4 FY26 | 6.319 (L99) | N.A. | **0.00%** |
| Q1 FY27 | 5.250 (L99) | N.A. | **0.00%** |
| FY26 | 38.843 (L99) | N.A. | **0.00%** |

A3 F3/F4 (shell-entity, unaudited-contribution) correspondingly N.A.

### 4B. PAT bridge — Reported PAT YoY change (Q1 FY27 vs Q1 FY26), Rs Crore
Reported PAT change = 5.250 − 7.083 = **−1.833 Cr (−25.88%)**.

| Component | YoY Change (Rs Cr) | Recurring? | Basis |
|---|---|---|---|
| Gross profit (Rev − RM − Δinv) | **+11.379** | **Inventory-inflated (see note)** | Q1FY27 39.794 vs Q1FY26 28.415; the Rs15.614 Cr FG/WIP build (L86) props this |
| Employee benefits | −0.042 | Recurring | 2.462 vs 2.420 (L87) |
| Other expenses | **−9.548** | Recurring | 21.353 vs 11.805 (L90) — **the −172 bps driver** |
| = Operating EBITDA change | **+1.789** | Recurring in part; **level partly inventory-inflated** | 15.979 vs 14.190 (**still +12.6%**) |
| Depreciation | **−2.559** | Recurring (post-capex) | 4.131 vs 1.572 (L89) — BELOW EBITDA |
| Finance costs | **−1.377** | Recurring (post-debt) | 6.481 vs 5.104 (L88) — BELOW EBITDA |
| Other Income | −0.131 | Non-recurring typically | 1.630 vs 1.761 (L82) |
| = PBT change | **−2.278** | | 6.997 vs 9.275 |
| Current tax lower | +1.265 | Mixed | 0.625 vs 1.890 (L96) |
| Deferred tax higher (shield) | −0.820 | Mixed (timing) | 1.122 vs 0.302 (L98) |
| = Total tax change | +0.445 | | 1.747 vs 2.192 |
| Exceptional items | 0.000 | Non-recurring | nil both (L93) |
| **Reported PAT YoY change** | **−1.833** | | 5.250 vs 7.083 |

**Double-scoring reconciliation (A5 graft 2):** the +Rs11.379 Cr gross-profit gain (and part of the +Rs1.789 Cr Operating EBITDA level) is inflated by the **SAME Rs15.614 Cr FG/WIP build (+197.6% YoY, L86)** that Step 5 flags as the **negative cash-conversion proxy** — one economic event with two faces. Gross-profit gain reclassified from "Recurring" to **"inventory-inflated, pending H1 CFO + balance-sheet verification."** The DECK now closes the loop: the annual analogue of exactly this pattern is FY26's CFO −13.8 Cr against PAT 38.8 (`[DECK]` dL867/dL806) driven by −78.9 Cr of WC change (dL863), i.e. a full-year confirmation that Scoda's reported profit is not converting to cash when inventory builds.

### 4C. DEPRECIATION / EARNINGS-QUALITY ANOMALY (A3 F16-7 — NEW from deck)
Deck Historic IS shows **FY26 D&A 9.2 vs FY25 18.1** (roughly halved) `[DECK]` p23 dL801, despite **fixed assets nearly doubling 103.5 → 194.0** (p24 dL820). Yet **Q1 FY27 D&A is +162.8% YoY** (4.1 vs 1.6, p36 dL1295) and ramping; 4.1/quarter annualises to ~16.4 — about **1.8x the entire FY26 print**. An abnormally low FY26 D&A **flatters FY26 PBT (52.7), PAT (38.8), EPS (6.8) and ROCE (11.6%)** — the very inputs that feed the valuation pillar and the FY26 EPS base — by an estimated ~Rs7-9 Cr of normalised charge. Possible causes: reclassification, prior-period item, component-life revision, or extraction error; unresolved from the deck. **This compounds the bear read: true run-rate D&A is far higher than FY26 suggests, so both the FY26 earnings base and the near-term run-rate are worse than the headline.** Raised as a Step-4/Step-7 flag and management question (Q11).

**Mandatory questions:**
- **% of PAT change recurring vs non-recurring?** Essentially all −1.833 Cr is recurring/operating; non-recurring OI only −0.131. But the gross-profit leg is propped by the build and should be read down.
- **If OI reverts?** Immaterial (<0.15 Cr).
- **D&A / finance steady state?** **Still ramping** — and FY26's understated D&A (4C) means the steady-state fixed-cost base is heavier than either FY26 or even Q1 FY27 alone shows.
- **Tax adjustment inflating PAT?** **Yes (F8-1).** Current tax only 8.93% of PBT; deferred-tax charge Rs1.122 Cr **(~1,603 bps; 16.0% of PBT; 11.22/69.97)** holds ETR at ~25.0%. Accelerated-depreciation timing shield on the new plant — flatters cash-tax now, reverses later. (Note the earnings-quality tension: FY26's low D&A flatters the P&L while the same accelerated depreciation for tax builds the DTL — the tax books and the reporting books are telling different depreciation stories, worth probing.)

**STOP-4 cleared.**

---

## STEP 5 — CASH QUALITY & BALANCE SHEET (Q1 INDETERMINATE; ANNUAL resolved by deck)

**Data-availability rule (v1.2):** Reg 33 mandates cash flow + balance sheet only at HALF-YEAR (Q2) and full-year (Q4). **This is a Q1 interim — the RESULTS filing carries NO CFO and NO balance sheet → Q1-specific rows ND.** **The DECK now voluntarily discloses ANNUAL (FY23-FY26) cash flow, balance sheet, and working-capital days** — UNAUDITED management representation, confirm at audited H1 FY27. Both levels are shown below.

### 5.1 Q1-specific (results) — still ND / INDETERMINATE

| Metric | Prior period | Q1 FY27 | Change | Verdict |
|---|---|---|---|---|
| CFO (Q1) | ND | ND | ND | Not in a Q1 interim |
| CFO/PAT ratio (Q1) | ND | ND | ND | **INDETERMINATE — see 5.3** |
| Capex (PPE+CWIP) (Q1) | ND | ND | ND | Not filed |
| FCF (Q1) | ND | ND | ND | Not filed |
| Working-capital change (Q1) | ND | **FG/WIP build Rs15.614 Cr (L86)** | +197.6% YoY (15.614 vs 5.247) | Bear-leaning proxy; same build inflating Step 2/4B gross margin |
| Receivable days (Q1) | ND | ND | ND | Not filed |
| Inventory days (Q1) | ND | ND | ND | Not filed |
| CCC (Q1) | ND | ND | ND | Not filed |
| Net Debt (Q1) | ND | ND | ND | Not filed (finance +27% implies debt up) |
| Promoter Pledge | ND (Notion 66.43% EXEMPLARY) | ND | ND | Not in this filing/deck |

### 5.2 ANNUAL (deck Slide 22/24/25 — NEW; UNAUDITED) `[DECK]`

| Metric | FY25 | FY26 | Change | Verdict |
|---|---|---|---|---|
| CFO (annual) | 18.4 (dL867) | **−13.8 (dL867)** | swung negative | **CONFIRMATORY-NEGATIVE (F16-1)** |
| CFO/PAT (FY, single-year) | 18.4/31.7 = 0.58x | −13.8/38.8 = **−0.36x** | collapsed | Single-year FY26 negative |
| **Cumulative FY23-FY26 CFO/PAT** | — | **(20.3+2.2+18.4−13.8)/(10.3+18.3+31.7+38.8) = 27.1/99.1 = 0.27x** | — | **BELOW the 0.30x thesis-break line — see 5.3** |
| Inventories (Rs Cr) | 149.8 (dL823) | 209.8 (dL823) | +40.1% | Build (vs revenue +7% FY26) |
| Inventory Days | 163 (dL753) | **217 (dL751)** | +54 days | **WORSENING (trigger 2 wrong way)** |
| Trade receivables (Rs Cr) | 101.0 (dL825) | 138.0 (dL825) | +36.6% | Outpaced revenue +7% |
| Debtor Days | 76 (dL773) | **97 (dL770)** | +21 days | **WORSENING (trigger 7 wrong way)** |
| Cash Conversion Cycle | 164 (dL773) | **211 (dL770)** | +47 days | **WORSENING** |
| ROE | 21.1% (dL754) | **9.9% (dL757)** | −11.2 pp | Collapse (reinforces negative) |
| Borrowings (Rs Cr) | 210.2 (dL835) | 185.3 (dL835) | −24.9 | Down (post-IPO) |
| Net Debt/Equity | 1.1x (dL756) | **0.3x (dL759)** | improved | **NEUTRAL-FACT — post-IPO equity infusion, NOT operational deleveraging** |
| Fixed assets (Rs Cr) | 103.5 (dL820) | 194.0 (dL820) | +87.4% | Capex confirmed (CFI −149.9, dL869) |

### 5.3 CASH-CONVERSION VERDICT — Q1 STILL INDETERMINATE; capped at PROCEED WITH CAVEATS
**The deck's headline "Cashflow from Operations INR −13.8 crores (vs 18.4 crores in FY25)" (p5 dL144-145) is the FY26 ANNUAL figure, NOT Q1 FY27** — confirmed by the Historic Cashflow table (p25 dL867 shows −13.8 in the FY26 column). A3 F16-1/F16-2 flag that the "Performance Snapshot – Q1 FY27" slide (p5) **blends genuine Q1 P&L KPIs with UNLABELLED FY26 annual CFO/ROE/working-capital KPIs**. Therefore:
- **(a) Q1 FY27 CFO is STILL NOT disclosed → Q1 cash conversion remains INDETERMINATE → protocol verdict stays capped at PROCEED WITH CAVEATS.** Per house rule, INDETERMINATE cash conversion must not resolve silently to PROCEED. **Do NOT report −13.8 as Q1, and do NOT let the annual disclosure silently upgrade the Q1 INDETERMINATE.** Named missing evidence: **standalone Q1/H1 FY27 CFO, Q1/H1 balance sheet, Q1 ROE/WC days.** → management question Q4 (F16-2).
- **(b) BUT the newly disclosed FY26 annual CFO −13.8 Cr is a strong CONFIRMATORY-NEGATIVE.** From the deck's own cashflow rows, **cumulative FY23-FY26 CFO/PAT ≈ 0.27x (27.1/99.1), BELOW the 0.30x thesis-break line** — on management's own unaudited number. **Precise status:** the THESIS-BROKEN window is **FY22-FY27 measured at FY27-end**; the deck covers FY23-FY26 only (no FY22, no FY27). So the condition is **NOT FORMALLY FIRED** (wrong window, and one year short at each end) — **but the trajectory is now demonstrably below the line.** (Contrast the prior Notion cumulative FY22-FY25 −0.09x: a different, narrower window; the deck's FY23-FY26 0.27x is a distinct measure — both sit below 0.30x.) This is the single most important thing the deck adds: it converts an untestable INDETERMINATE at the annual level into a below-the-line confirmatory-negative, while leaving the Q1-specific test genuinely open.

**Mandatory questions:**
- **CFO/PAT vs Pillar-2 band (0.65/0.80/1.00/1.15/1.30x)?** FY26 single-year −0.36x and cumulative FY23-26 0.27x sit BELOW even the lowest 0.65x band. **Hold the conservative band; do NOT upgrade.**
- **WC drag structural or growth-induced?** The deck now shows it WORSENING across the board at the annual level (inventory days 163→217, debtor 76→97, CCC 164→211) — not a one-year blip and not improving. Structural read reinforced.
- **CWIP capitalise as expected?** Fixed assets +87.4% (103.5→194.0) and CFI −149.9 Cr FY26 (dL869) confirm heavy capex is on the books and depreciating (consistent with Q1 depreciation +162.8%). Rs amount capitalised in Q1: ND.
- **Net debt within projection?** Borrowings fell 210.2→185.3 but ONLY because of the Rs220 Cr IPO raise (CFF +152.7 FY26, dL871); net D/E 0.3x is **equity-funded, not cash-generative** deleveraging (F16-6, NEUTRAL-FACT).

**STOP-5 cleared (Q1 cash conversion INDETERMINATE, capping the verdict; annual cash/WC resolved by the deck as confirmatory-negative).**

---

## STEP 6 — RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

| Metric | Bear | Base | Bull | Actual | Lands In |
|---|---|---|---|---|---|
| Revenue (quarterly) | ND (no Q proj) | ND | ND | 124.345 (L81) | +27.6% YoY; **at/above base on top-line** |
| Op EBITDA Margin | ND | FY27 guide 14-15% (walked back) `[NOTION]` | ND | **12.85% op / 14.16% rep** | **Below the 14-15% guide (operating)** |
| PAT (quarterly) | ND | ND | ND | 5.250 (L99), −25.9% | **Below** a base FY27 path |
| ROCE (annual) | ND | ~16-17% `[NOTION]` | ND | **FY26 11.6% (deck dL774)** | **BELOW base — materially (F16-3)** |
| EPS (FY29 anchor, context) | 7.01 | 12.35 | 16.69 | 0.88 Q1 (L110); FY26 6.8 (deck dL809) | FY26 6.8 below FY29 base path start |
| Net Debt / DE | ND | ND | ND | 0.3x (deck dL759) | Improved but equity-funded (neutral) |

**Landing verdict:** Revenue **at/above base**; **operating margin BELOW guide**; **ROCE FY26 11.6% materially below the ~16-17% base assumption** (deck-disclosed, F16-3); PAT trajectory **below base**. Mixed, tilted negative below the top line — and the deck's annual ROCE/CFO/ROE reads make the "below" firmer than the results filing alone could show. Probability-reweighting rule requires below-bear on 2+ metrics for **2 consecutive quarters**; this is the first in-pipeline quarter and revenue is not below bear, so **no mechanical re-weight fires now.** Logged as quarter 1 of a potential sequence.

### 6B. Watchlist / monitoring status (Notion nine-trigger checklist) — UPDATED with deck reads

| # | Trigger | Green | Red | Q1 FY27 Reading (results + deck) | Status |
|---|---|---|---|---|---|
| 1 | H1 CFO+ AND cum FY22-27 CFO/PAT >0.30x | CFO+ & >0.30x | CFO− / <0.30x | Q1 CFO ND (results); **deck FY26 annual CFO −13.8, cum FY23-26 0.27x < 0.30x (F16-1)** | **RED-leaning (annual below line; Q1 untestable)** |
| 2 | Inventory days <170 (Q2), <150 (Q4) | <170 | >180 (thesis-break) | Q1 BS ND; **deck FY26 inventory days 217 (F16-6), rising 163→217** | **RED (annual 217 > 180; Q1 untestable)** |
| 3 | Customer concentration disclosed, top <20% | disclosed & <20% | undisclosed / >20% | No Note 36 in interim; **deck withholds concentration too — "349 clients", sector split only (F16-8)** | **RED (still undisclosed)** |
| 4 | Welded commercial revenue >Rs30 Cr Q3/Q4 | >Rs30 Cr | none | Single-segment (L122); **deck: welded commissioning H2 FY27 (F6-1), no welded revenue/utilisation disclosed (F16-8)** | **UNKNOWN (not due until Q3/Q4)** |
| 5 | BHEL/NTPC tender won, >Rs75 Cr | won >Rs75 Cr | lost/<Rs75 Cr (thesis-break) | Silent in filing; **deck: only "healthy order pipeline", no value (F16-8)** | **UNKNOWN (unquantified)** |
| 6 | Marine approvals RINA + BV + first PO | all + PO | none by window | **Deck: RINA + Bureau Veritas Marine "currently applied for", NOT granted (F16-8, p16 dL569)** | **RED-leaning (pending, not cleared)** |
| 7 | Receivables growth ≤ revenue growth, 2 q | ≤ rev | > rev | Q1 BS ND; **deck FY26 debtor days 76→97, receivables +36.6% vs revenue +7% (F16-6)** | **RED (annual outpaced; Q1 untestable)** |
| 8 | Volume/utilisation/segment disclosure begins | begins | continued refusal | **Note 4 single-segment (L122); deck ALSO withholds welded/seamless split & utilisation (F16-8); capacity figures internally inconsistent (F16-9)** | **RED (still refused, even in the deck)** |
| 9 | FY27 EBITDA margin ≥14% all quarters | ≥14% every q | <14% any q | **Operating 12.85% <14% (Other Expenses +80.9%; gross margin build-propped); reported 14.16%; deck confirms 12.9% −172 bps** | **RED (operating) / AMBER (reported)** |

**Trigger scoreboard: still 0 of 9 GREEN — NOTHING cleared.** The deck moved several from UNKNOWN to RED on the FY26 annual reads: **1 (cum CFO/PAT 0.27x < 0.30x), 2 (inventory days 217 > 180), 7 (receivables outpacing revenue)** are now RED at the ANNUAL level (Q1-specific still ND); **6** moved to RED-leaning (marine "applied for", not granted); **8** stays RED (disclosure still refused even in a disclosure-rich deck); **9** stays RED on the operating basis. **4 and 5 remain UNKNOWN/unquantified.** The re-engagement rule (6/9 GREEN AND CMP<Rs95) is nowhere near met — and the deck evidence makes the AVOID materially firmer.

### 6C. Thesis-broken trigger check

| Thesis-Broken Condition | Threshold | Q1 FY27 Reading (results + deck) | FIRED? |
|---|---|---|---|
| Cumulative FY22-FY27 CFO/PAT < 0.30x (at FY27-end) | <0.30x | Q1 CFO ND; **deck FY23-FY26 cum 0.27x < 0.30x** — but WRONG WINDOW (no FY22, no FY27) and measured before FY27-end | **NOT FORMALLY FIRED (trajectory below line — F16-1)** |
| Inventory days >180 at end FY27 | >180 | Q1 BS ND; **deck FY26 = 217 > 180**, but measured at end FY27, not FY26 | **NOT FIRED (FY26 already 217 > 180; FY27-end pending)** |
| Welded utilisation <25% at end FY28 | <25% | ND; measured at FY28-end; welded not yet commissioned (H2 FY27) | **NOT FIRED (untestable now)** |
| BHEL tender lost OR volumes <Rs75 Cr | lost / <Rs75 Cr | ND (silent in filing; deck only "healthy pipeline") | **NOT FIRED (untestable now)** |

**No thesis-broken condition has FORMALLY FIRED** (each is measured at a future date or a different window). **BUT the deck makes two of the four demonstrably adverse on the latest available annual data:** cumulative CFO/PAT is 0.27x (below 0.30x) and FY26 inventory days are 217 (above 180). These are not FY27-end readings, so no exit trigger is live — **but the AVOID is materially firmer, and I flag; the human decides.** Conservative note: none-fired ≠ cleared.

### 6D. Growth-trigger status — UPDATED with deck

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| Revenue re-acceleration to 20%+ | Base (FY26 +7%) | **Revenue +27.6% YoY** (L81; deck dL1283) | Margin −172 bps; sales < production (build); deck FY26 had decelerated to +7% | **ON TRACK (top-line) / WEAKENED (quality)** |
| Welded plant commissioning & ramp | Delayed Q1→H2 FY27 | Depreciation +162.8% (plant capex capitalised); **deck: "expected to be commissioned during H2 FY27", "progressing as planned" (F6-1)** | No welded revenue disclosed; revenue flat QoQ | **DELAYED / underway (fixed cost in, volume not)** |
| Margin sustained ≥14% (FY27) | Guided, walked to 14-15% | Reported 14.16% | **Operating 12.85% <14%; deck confirms 12.9% (F16-5)** | **WEAKENED** |
| BHEL/NTPC tender & marine approvals | Imminent (Jun-Sep 2026) | none | **Deck: order book only "healthy pipeline" (no value); marine RINA+BV "applied for", not granted (F16-8)** | **DELAYED / UNCONFIRMED** |
| Cash conversion turn (CFO+) | Weak | none | **Deck: FY26 CFO −13.8, cum FY23-26 0.27x (F16-1); WC worsening (F16-6)** | **WEAKENED → firmly bear (annual evidence)** |
| ROCE base holding ~16-17% | Base pillar `[NOTION]` | — | **Deck: FY26 ROCE 11.6% vs ~16-17% assumption (F16-3); FY26 flattered by understated D&A (F16-7)** | **WEAKENED (pillar downside — Step 7)** |

**STOP-6 cleared (6A-6D complete, with deck reads folded into the scoreboard).**

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

The deck now supplies FY26 annual ROCE and D&A, so Pillar-1 CAN be flagged with hard (if unaudited) evidence — but per protocol the **FTTCP ROCE forward verdict is the SOLE authority for Pillar-1 ROCE selection; I flag the downside, I do NOT re-run the valuation** (FTTCP / Role 1 own that). Destination PE is NOT recomputed here.

| Pillar / Input | Original Assumption `[NOTION]` | Q1 FY27 Reading (results + deck) | Action |
|---|---|---|---|
| **ROCE Base** (0.5×ROCE + 7.5, floor 9x, cap 24x) | ROCE ~16-17% → ~16x (capped) | **Deck FY26 ROCE 11.6% (F16-3, dL774)** — materially below assumption; **and FY26 is FLATTERED by understated D&A 9.2 (F16-7), so true ROCE is lower still**; Q1 depreciation +162.8%, finance +27.0%, EBIT −6.1% all imply near-term compression | **HOLD Notion pending FTTCP; FLAG DOWNSIDE to the ROCE base pillar (0.5×11.6 + 7.5 ≈ 13.3x vs ~16x). Do NOT re-run valuation — flag for the human.** |
| Cash Multiplier | Low band (cum CFO/PAT prior −0.09x; Gate 0 cash 5/20) | **Q1 INDETERMINATE; deck FY26 CFO −13.8, cum FY23-26 0.27x (F16-1)** — below lowest 0.65x band | **HOLD conservative band; do NOT upgrade. Deck confirms the low band.** |
| Growth Visibility Premium | +x (EM score, catalyst proximity) | No catalyst confirmed; order book/tender/marine unquantified or "applied for" (F16-8) | **HOLD (no upgrade; slight downside on unconfirmed catalysts)** |
| Strategic Premium | +x (moat) | Nothing moves the moat; disclosure asymmetry (F16-8) | **HOLD** |
| UA Multiplier | **NOT applied** (Gate 0 deal-breakers) | Deal-breakers unchanged | **HOLD — remains NOT applied** |
| Sector Cap | Specialty SS pipes cap | No reclassification | **HOLD** |
| Hurdle Ratio recheck | Prob-weighted CAGR 9.9% vs 25%; up/down ~1.92x (<1.953) | Q1 PAT −25.9%, ROCE 11.6%, cum CFO/PAT 0.27x all weaken the EPS path; nothing improves the ratio | **STILL FAILS (consistent with AVOID)** |

**Destination PE: HELD at 15x (range 13-17x). No fair-value recompute here** — the pillar re-validation is a FLAG to FTTCP/Role 1, not a recompute; Notion FY29 fair values (Bear Rs91 / Base Rs185 / Bull Rs284) stand pending the FTTCP re-run. **The material new flag is the ROCE-base downside: FY26 ROCE 11.6% (deck) is ~5 pp below the ~16-17% Pillar-1 assumption, and FY26 is additionally flattered by understated D&A — so the ROCE base pillar has clear downside that FTTCP should re-price.** Logged; not self-actioned.

**STOP-7 cleared.**

---

## STEP 8 — POSITION DECISION (Branch 8A-W — NON-HELD NAME)

**Decision Status verified at Step 0A: AVOID (mildly), Position ZERO (tracking only)** `[NOTION]`. NOT held → **8A-W governs; no trim/exit mechanics.**

**8A-W walk:**
- **Any thesis-broken condition FORMALLY FIRED?** No (Step 6C) — each is measured at a future date/window. **But two are demonstrably adverse on the latest annual data (cum CFO/PAT 0.27x < 0.30x; FY26 inventory days 217 > 180).** → Do not reclassify on a fired trigger; flag the firmer bear.
- **Actuals below BEAR on 2+ metrics?** Not demonstrably at the quarterly level (revenue strongly above bear; no quarterly bear print to breach; first in-pipeline quarter) → the mechanical "push the gate out" does not fire.
- **Between bear and base?** **Yes, tilted below base** — strong revenue, sub-guide operating margin, inventory-inflated gross margin, negative PAT trajectory, and now deck-confirmed FY26 ROCE 11.6%, CFO −13.8, WC worsening. → Revise near-term margin/EPS/ROCE projections cautiously downward; entry zone unchanged pending standalone H1 cash/BS.

**DECISION: Decision Status HELD at AVOID. Position remains ZERO (tracking only). Entry zone UNCHANGED: BUY < Rs95, WATCHLIST Rs95-115, AVOID > Rs115; MoS Rs76. Master decision gate remains Q2 FY27 (Nov 2026)**, when standalone H1 CFO + balance sheet arrive and the 6-of-9 re-engagement test can be run. **This merged review moved 0 of 9 re-engagement triggers to GREEN, put/kept triggers 1/2/6/7/8/9 at RED or RED-leaning, and — via the deck — makes the AVOID materially firmer** (CFO −13.8, cum 0.27x, ROCE 11.6%, D&A understatement). **Nothing here authorises re-engagement; I flag, the human decides.**

### 8B. Add-Back / Trim trigger refinement
- Not held → no trim ladder. **Re-engagement trigger unchanged:** 6/9 operating triggers clear AND CMP < Rs95 → STARTER 1.5-2%; 8/9 AND CMP < Rs95 → 3%.
- **Refinements flagged for the human (deck-informed):** (i) read trigger 9 on the **operating** basis (≥14% operating); (ii) add an explicit watch on Other-Expenses/revenue normalising below ~13% AND on whether the "transient" headwinds (freight/RM/gas/manpower, F7-1) actually reverse in Q2; (iii) add a watch that gross margin holds once the FG/WIP build unwinds; (iv) **add a Pillar-1 ROCE watch — require FY27 ROCE recovering toward ~16% before any re-rate, given deck FY26 11.6%**; (v) require **standalone Q1/H1 CFO** (not the annual figure) before trigger 1 can be scored. Recorded as proposed tightenings; not self-actioned.

### 8C. Single cleanest metric for next quarter (Q2 FY27)
**Standalone H1 FY27 CFO (and the derived cumulative FY22-H1FY27 CFO/PAT).** Q2 is a half-year filing → the cash flow statement becomes mandatory (Reg 33). It most cleanly resolves the bull/bear split because the entire AVOID rests on structural cash-conversion failure, it directly tests the hardest thesis-broken line (<0.30x), and it reveals whether the Q1 gross-margin prop was real or the inventory-build artifact — AND it disambiguates the deck's period-blended −13.8 (annual) from the genuinely-undisclosed standalone Q1/H1 figure (F16-2).
- **Bull threshold:** H1 FY27 CFO positive AND cumulative CFO/PAT tracking above 0.30x (with inventory days <170 and gross margin holding as the build unwinds).
- **Bear threshold:** H1 FY27 CFO negative OR cumulative CFO/PAT still <0.30x — which, if sustained to FY27-end, fires the thesis-broken condition (the deck's FY23-26 0.27x already points here).

**STOP-8 cleared.**

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT (refreshed for the merged review)

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding across BOTH forensics generates ≥1 question. **Cross-quarter answer-status tracking begins here.** Mapping: **F14-2 → Q1; F8-1 → Q2; F10-1(results) partially RESOLVED by deck → narrowed to Q3; Q4 = F16-2 standalone-Q1 CFO/ROE/WC; F9-1 → Q5; F16-6 → Q6; F16-8/F16-9 → Q7; Q8 concentration; F7-1/F6-1 → Q9 (now MANAGEMENT-ANSWERED, verify Q2); Q10 = graft-2 build; F16-3 → Q11 ROCE; F16-7 → Q12 D&A anomaly; F14-1(deck) → Q13 Chairman.**

| # | Question | From finding | Why It Matters | Bull Answer | Bear Answer |
|---|---|---|---|---|---|
| 1 | Depreciation +162.8% and finance +27.0% YoY while PAT fell 25.9%. What is the commissioned welded-plant gross block now depreciating, the full-quarter run-rate depreciation & interest once fully ramped, and the welded revenue/utilisation to absorb them by Q3/Q4 FY27? | F14-2 | Isolates timing ramp vs structural reset | Specific gross block, dated utilisation ramp, quantified welded revenue | Vague "ramping well"; refuses volume/utilisation |
| 2 | Current tax only 8.9% of PBT with a Rs1.12 Cr deferred-tax charge (~1,603 bps). What is the DTL balance and its reversal profile — when does cash-tax ETR normalise toward ~25%? | F8-1 | Quantifies the timing shield in reported PAT | Modest DTL, long runway | Large DTL, near-term reversal |
| 3 | The deck attributes the EPS non-reconciliation (FY25 7.6 > FY26 6.8 despite higher PAT) to the Rs220 Cr IPO. Confirm the weighted-average share counts used for FY25/FY26/Q1FY26 EPS, and are prior-period EPS restated per Ind AS 33? | F10-1 (results, now partially resolved) | Confirms the true share base and restatement compliance | Clean IPO-timing weighting, EPS restated | Unexplained residual / unrestated base |
| 4 | The Rs−13.8 Cr CFO on the "Q1 FY27" snapshot slide is the FY26 ANNUAL figure. What is the STANDALONE Q1 FY27 (and H1 FY27) CFO, Q1 ROE, and Q1 working-capital days? | F16-2 | The Q1 cash conversion is still undisclosed (period-blend); the crux of the AVOID | Standalone Q1 CFO positive; days improving | Refuses / only repeats annual figure |
| 5 | Q1 defined-benefit remeasurement (Rs1.71M) exceeds all of FY26 (Rs1.18M) on a sign-flipping series. Which actuarial assumption changed (discount rate, salary escalation, plan-asset return)? | F9-1 | Flags an assumption reset for AR scrutiny | Routine discount-rate move | Opaque material reset |
| 6 | FY26 annual working capital worsened (inventory days 163→217, debtor 76→97, CCC 164→211). What is the Q1 FY27 standalone inventory/debtor-day position vs the <170-by-Q2 target, and is the deterioration cyclical or structural? | F16-6 | Directly tests triggers 2 and 7, the WC legs of the AVOID | Days falling toward <170 | Days flat/rising |
| 7 | Order-book VALUE, welded/seamless utilisation %, and current-vs-post-expansion seamless capacity (Slide 10 shows 20,068 MTPA as current; Slide 28 as a post-expansion target with 10,068 existing)? | F16-8, F16-9 | Tests triggers 4/5/8 and the capacity/utilisation basis | Concrete order value, utilisation %, reconciled capacity | Continued single-segment refusal; capacity ambiguity persists |
| 8 | Top-customer concentration at FY26 — is the single-customer share still ~26.7% (FY25), and will it be disclosed in the FY26 AR? | ND / trigger 3 | Tests hidden concentration (trigger 3) | Disclosed and <20% | Undisclosed / concentrated |
| 9 | **[MANAGEMENT-ANSWERED — verify at Q2]** The deck attributes the −172 bps margin/Other Expenses +80.9% to freight/RM volatility, a 3-4 month pass-through lag, an April gas outage (~2 weeks), and manpower, claimed "largely transient". Confirm the Rs quantum of each in Q1, and demonstrate the recovery in Q2 (Other Expenses/revenue back below ~13%). | F7-1, F6-1 | Tests whether "transient" is real; the sole margin driver | Quantified one-offs that reverse in Q2; ratio <13% | Structural step-up that persists; ratio stays elevated |
| 10 | FG/WIP built Rs15.61 Cr (+197.6% YoY) while RM-consumed intensity rose +434 bps; the +283 bps net-material "gain" is a build credit. How much of the Q1 gross-profit gain reverses once production/sales re-align, and does gross margin hold at current dispatch levels? | A5 graft-2 (L85/L86); F16-4 | Tests whether the one favourable P&L line is real or a cost-deferral optic | Order-backed pre-build for dispatched Q2 volume | Production outran demand; margin reverses |
| 11 | Deck-disclosed FY26 ROCE is 11.6%, materially below the ~16-17% our valuation pillar assumes. Is 11.6% the normalised base, or transitional on the capex ramp — and what is the FY27/FY28 ROCE path? | F16-3 | Pillar-1 downside; drives destination PE | Sharp ROCE recovery path as volume ramps | ROCE stays ~12% → pillar/PE cut |
| 12 | Deck FY26 D&A is Rs9.2 Cr, roughly half FY25's Rs18.1 Cr, despite fixed assets nearly doubling; yet Q1 FY27 D&A annualises to ~Rs16.4 Cr. Explain the low FY26 D&A (reclassification / component-life / prior-period), and confirm the true run-rate depreciation. | F16-7 | FY26 PBT/EPS/ROCE base may be flattered ~Rs7-9 Cr | Benign reclassification with unchanged run-rate | Understated FY26 charge inflating the base |
| 13 | The deck names Samarth B Patel "Chairman & Executive Director"; the Reg 33 filing was signed by Bharatbhai Patel "Chairman and Whole-time Director" (DIN 08036100), with MD Jagrutkumar Rameshbhai Patel (DIN 06785595). Who chairs the board, and is there a Chairman transition? | F14-1 (deck) | Governance clarity across two same-quarter documents | Clear single Chairman / disclosed transition | Unexplained dual designation |

**Top 3 by likelihood of thesis-changing information:**
1. **Q4 (standalone Q1/H1 CFO)** — disambiguates the period-blended −13.8 and is the single strongest bull/bear resolver; a positive standalone print re-rates, a negative one near-confirms the structural bear.
2. **Q11 (FY26 ROCE 11.6% vs pillar) + Q12 (D&A understatement)** — together resolve whether the valuation pillar and the FY26 earnings base are as strong as Notion assumes; deck evidence says both have downside.
3. **Q9/Q10 (transient-headwinds recovery + inventory-build reversal)** — resolve whether the margin miss and the one favourable cost line are temporary or structural.

**Channel recommendation:** No concall scheduled with this filing (half-yearly cadence; Role 5 N.A. this run). **Send a formal IR letter now with all 13 questions verbatim; prioritise the top set for the H1 FY27 concall Q&A (Nov 2026).** Log each for cross-quarter answer-status tracking (ANSWERED / PARTIAL / EVADED / NOT ADDRESSED) at Q2 — Q9 already carries a management NARRATIVE (deck), to be scored on Q2 delivery.

**STOP-8.5 cleared.**

---

## STEP 9 — ROLE 5 (CONCALL) — N.A. THIS RUN
No concall transcript is in scope (only the results filing and the investor deck). **All Role 5 steps are N.A.**: Step 1 claims inventory, Step 2 forward-guidance table, Step 3 promise-vs-delivery / credibility ratio, Step 4 Q&A decomposition, Step 5 new-information/silence, Step 6 tone-specificity archetype, Steps 7-8 cross-reference/position, Step 8F forward questions — none executed. The deck's forward statements (welded H2 FY27, reaffirmed FY27 guidance, "largely transient" recovery) are captured in the commitment register and Step 8.5 questions, and will seed the Role 5 promise-vs-delivery tracker at the first concall. The half-yearly concall cadence (a Notion-flagged transparency concern) persists.

---

## MONITORABLES / CATALYST LIST (refreshed with deck disclosures)

**A3 RESULTS Commitment Register (F6): EMPTY** — no forward-commitment phrases in the 7 notes or board letter. **A3 PRESENTATION Commitment Register (F6-1): now POPULATED by the deck** — see below. **A3 Board-Outcome forward items (F13): NONE** (sole agenda item = approval of results + LRR, L38-39).

### Commitment register (from deck F6-1)
| Commitment | Implied date | Ref | Status word |
|---|---|---|---|
| Welded-segment capacity expansion commissioned | **H2 FY27** | `[DECK]` Slide 6 dL205-206 | **underway ("progressing as planned")** |
| Achieve FY27 guidance (NO numeric target stated anywhere in deck) | FY27 full year | `[DECK]` Slide 6 dL204 | **reaffirmed (unquantified)** |
| Seamless facility production ramp-up | coming quarters | `[DECK]` Slide 6 dL204 | underway |
| Improve operational performance ("largely transient" headwinds reverse) | coming quarters | `[DECK]` Slide 6 dL202 | intended / confident |
| Marine standards (Bureau Veritas Marine, Rina Marine) | not dated | `[DECK]` Slide 16 dL536/dL569 | **applied-for (NOT granted)** |

### Monitorables
| Monitorable | Source | Implied date | This review's read |
|---|---|---|---|
| **Standalone Q1/H1 FY27 CFO + cumulative CFO/PAT >0.30x** | Trigger 1 / thesis-break; F16-1/F16-2 | Q2 FY27 (Nov 2026) | **Deck FY26 annual CFO −13.8, cum FY23-26 0.27x < 0.30x — below line at annual level; Q1-specific still ND** |
| Inventory days <170 (Q2), <150 (Q4) | Trigger 2 / thesis-break >180; F16-6 | Q2/Q4 FY27 | **Deck FY26 = 217 (>180) — RED at annual level; Q1 standalone ND** |
| Debtor days / receivables ≤ revenue growth | Trigger 7; F16-6 | Q2+Q3 FY27 | **Deck FY26 debtor 76→97, receivables +36.6% vs rev +7% — RED at annual level** |
| Customer concentration (top <20%) | Trigger 3; F16-8 | FY26 AR | **Withheld even in deck; still undisclosed** |
| Welded commercial revenue >Rs30 Cr; welded/seamless utilisation | Trigger 4/8; F16-8/F16-9 | Q3/Q4 FY27 | **Commissioning H2 FY27; split & utilisation withheld; capacity cross-slide inconsistent** |
| BHEL/NTPC tender won >Rs75 Cr; order-book VALUE | Trigger 5; F16-8 | Jul-Aug FY27 | **Deck: only "healthy pipeline", no value** |
| Marine approvals RINA + BV + first PO | Trigger 6; F16-8 | Jun-Sep 2026 | **"Applied for", NOT granted — pending, not cleared** |
| FY27 EBITDA margin ≥14% all quarters | Trigger 9; A5 graft-1 | every FY27 q | **RED — operating 12.85% in Q1; deck confirms 12.9%** |
| Other Expenses / revenue normalising <~13%; "transient" headwinds reverse | A5 graft-1 / L90; F7-1 | Q2 FY27 | **Surged to 17.17%; management calls it transient (deck) — VERIFY recovery at Q2** |
| Gross margin durability as FG/WIP build unwinds; RM-intensity normalising | A5 graft-2 / L85,L86; F16-4 | Q2 FY27 | **RM intensity worsened +434 bps; +283 bps "gain" is a build credit = negative cash proxy** |
| **Pillar-1 ROCE recovering toward ~16%** | F16-3 | FY27 | **Deck FY26 ROCE 11.6% vs ~16-17% assumption — pillar downside flagged to FTTCP** |
| **FY26 D&A understatement / true run-rate depreciation** | F16-7 | FY26 AR | **Deck FY26 D&A 9.2 (half FY25's 18.1) while fixed assets doubled; flatters FY26 base ~Rs7-9 Cr** |
| **Chairman / governance clarification** | F14-1 (deck) | FY26 AR / IR | **Deck "Samarth B Patel Chairman & ED" vs filing "Bharatbhai Patel Chairman & WTD"** |
| Actuarial assumption reset (AR verify) | F9-1 | FY26 AR | OCI 1.71 > full FY26 1.18 |
| DTL reversal / cash-tax normalisation | F8-1 | ongoing | Current tax 8.9% of PBT (~1,603 bps shield) |
| EPS restatement clarity (residual after IPO-dilution explanation) | F10-1 | FY26 AR / IR | Deck explains via IPO; confirm weighted-share/restatement |

**Nine-trigger net read:** 0/9 GREEN, 6/9 RED or RED-leaning (1/2/6/7/8/9), 2/9 UNKNOWN/unquantified (4/5), plus the ROCE pillar now flagged downside. The re-engagement gate (6/9 GREEN AND CMP<Rs95) is not close; the deck made the AVOID firmer.

---

## PROTOCOL VERDICT

**PROCEED WITH CAVEATS.** Extraction on both documents is clean (results foots 20/20 on the corrected grid; deck reconciles to it — A3 F16-5; no REWORK, no INSUFFICIENT EVIDENCE). The verdict is **capped at PROCEED WITH CAVEATS — it cannot be PROCEED** — because **STANDALONE Q1 FY27 cash conversion is INDETERMINATE**: the deck's −13.8 Cr CFO is the FY26 ANNUAL figure period-blended onto a "Q1 FY27" snapshot (F16-1/F16-2), so the Q1-specific CFO is still undisclosed and must not resolve silently to PROCEED. **Named missing evidence:** standalone Q1/H1 FY27 CFO; Q1/H1 balance sheet (inventory/receivable days, net debt); Q1 ROE; Note-36 customer concentration; welded/seamless split & utilisation; order-book value; reconciled seamless capacity; Other-Expenses composition; the reversibility of the inventory-build gross-margin prop.

**Flags propagate to the human (they do not halt):** (1) operating EBITDA margin −172 bps to 12.85% (trigger 9 RED) driven by Other Expenses +80.9% (above EBITDA), now with a management "transient" narrative to verify (F7-1); (2) the +283 bps net-material "gain" is an inventory-build cost-deferral artifact (RM intensity worsened +434 bps) — the same Rs15.61 Cr build that the deck's FY26 CFO −13.8 confirms as cash burn; (3) below EBITDA, depreciation +162.8% and finance +27.0% convert +12.6% operating-EBITDA growth into PAT −25.9%; (4) **deck-confirmed FY26 annual reads that make the AVOID firmer: CFO −13.8, cumulative FY23-26 CFO/PAT 0.27x (below the 0.30x thesis-break line, though not formally fired — wrong window), inventory days 217 (>180), debtor days 97, CCC 211, ROE 9.9%, ROCE 11.6% (vs ~16-17% Pillar-1 assumption)**; (5) FY26 D&A understated (9.2 vs FY25 18.1) flattering the FY26 base ~Rs7-9 Cr (F16-7); (6) deferred-tax timing shield (~1,603 bps, F8-1); (7) EPS/IPO dilution now explained (F10-1 resolved-with-explanation); (8) continued single-segment / catalyst non-disclosure even in the deck (trigger 8 RED; F16-8); (9) governance dual-Chairman designation across the two same-quarter documents (F14-1).

**Decision Status stays AVOID / Position ZERO; NO pre-committed trigger has FORMALLY FIRED (I flag, the human decides) — but the deck evidence (CFO −13.8/cum 0.27x, ROCE 11.6%, D&A understatement, WC worsening) makes the AVOID materially firmer.** These deck reads REINFORCE the caveats; they do not change the verdict.

---

## PLAIN-LANGUAGE BRIEF (mandatory final narrative section)

### 1. SUMMARY NARRATIVE
Scoda Tubes reported Q1 FY27 (quarter to 30 June 2026) revenue of Rs124.35 Cr `[RESULTS]` L81, up 27.6% from Rs97.42 Cr a year ago `[RESULTS]` L81, and the investor deck confirms the same number `[DECK]` p36. That growth is the good news, and it is real. Everything below it is not. PAT fell to Rs5.25 Cr from Rs7.08 Cr `[RESULTS]` L99, down 25.9%, and reported EPS fell 39% to Rs0.88 `[RESULTS]` L110 — the deck prints the identical figures, independently confirming the corrected results grid `[DECK]` p8/p36. There are two distinct problems. First, above the EBITDA line: operating EBITDA margin fell 172 bps to 12.85% `[RESULTS]` computed, below the company's own walked-back FY27 guide of 14-15% `[NOTION]`, driven by Other Expenses jumping 80.9% (Rs11.81 to Rs21.35 Cr) `[RESULTS]` L90. The deck now supplies the cause: management calls it freight and raw-material cost volatility, a 3-4 month order-booking lag that blocked cost pass-through, a two-week April gas outage, and a manpower shortage — "largely transient" `[DECK]` p6. That is a testable claim, not proof; we verify it at Q2. The one cost line that looks like it helped — net material cost falling to 68% of revenue — is a mirage: raw material actually consumed rose to 80.55% from 76.22% `[RESULTS]` L85, and the apparent gain is a Rs15.61 Cr inventory build (up 197.6%) `[RESULTS]` L86 that pushed cost onto the balance sheet. Second, below the EBITDA line: operating EBITDA still grew about 12.6%, but depreciation jumped 162.8% and finance costs rose 27% `[RESULTS]` L89/L88 as the debt-funded new plant began depreciating, turning that into the 25.9% PAT decline. Revenue was flat sequentially `[RESULTS]` L81, so the new capacity has not yet lifted the run-rate. The deck's biggest contribution is on cash and returns. It voluntarily prints FY26 annual operating cash flow of MINUS Rs13.8 Cr `[DECK]` p25, and its own four-year cash flows imply cumulative FY23-26 CFO/PAT of about 0.27x — below the 0.30x line our thesis calls a break, though the formal test is FY22-FY27 measured at FY27-end, so it is not yet fired. It also discloses FY26 ROCE of 11.6% `[DECK]` p22, well under the ~16-17% our valuation assumes, and FY26 depreciation of Rs9.2 Cr `[DECK]` p23 that is oddly half the prior year's while fixed assets doubled — meaning FY26 profit and ROCE are flattered. Crucially, the deck's −13.8 CFO is the ANNUAL figure printed on a slide titled "Q1 FY27", so the standalone Q1 cash flow is still undisclosed: Q1 cash conversion stays INDETERMINATE. The Notion Decision Status is AVOID with a zero position `[NOTION]`, and nothing changes it: 0 of 9 re-engagement triggers went green, six are red or red-leaning, no thesis-broken condition formally fired but none cleared. The verdict is PROCEED WITH CAVEATS, and the deck evidence makes the AVOID firmer. The next real test is standalone H1 FY27 cash flow in November 2026.

### 2. SECTOR INTELLIGENCE
Scoda operates in specialty stainless-steel seamless and welded pipes/tubes, serving oil & gas, process/chemical, fertilizer, power, water treatment and automobile/railways/transportation `[DECK]` p33/p34. The deck adds a proper industry frame: global SS pipe & tube demand grew ~3% CAGR CY19-23 and is projected 3-4% to CY28, with oil & gas and process industries dominating `[DECK]` p33 dL1207-1208; the India outlook shows demand rising with anti-dumping duty protection cited explicitly `[DECK]` p34 dL1223, and Indian end-segments (process 28-32%, oil & gas 22-25%, ART 20-23%) growing 6-10% CAGR FY24-29 `[DECK]` p34. That import-substitution-behind-protection tailwind is the structural case `[NOTION]` and the deck substantiates it. The demand read this quarter is favourable on volume (revenue +27.6% YoY `[RESULTS]` L81; deck FY26 growth had decelerated to just +7% `[DECK]` dL360, so Q1 is a re-acceleration). But the live sector-specific headwind is now input cost: management pins the margin miss on freight, RM price volatility and an April gas-supply outage `[DECK]` p6 — if a gas/power or stainless-input step is the cause, it is a sector-wide cost headwind, not company-specific, and its persistence matters for every domestic specialty-pipe maker. Geographic mix (new deck detail): exports are ~46% of Q1 revenue (Rs57 Cr) `[DECK]` p7/p30, spanning 32 countries `[DECK]` p17 — a genuine export franchise, but the marine-certification catalysts (RINA, Bureau Veritas) that would open higher-value marine end-markets are only "applied for", not granted `[DECK]` p16. Net: demand supports the top-line, the sector shares an input-cost problem this quarter, and the regulatory/certification catalysts are unconfirmed.

### 3. BUSINESS-MODEL INTELLIGENCE
Scoda makes money manufacturing SS pipes/tubes across seamless (established) and welded (new, commissioning H2 FY27) lines `[DECK]` p6/p15/p38. The deck confirms a capex-heavy, backward-integrating model: fixed assets nearly doubled to Rs194 Cr in FY26 `[DECK]` p24, funded by a Rs220 Cr IPO plus debt, with a captive mother-hollow and captive solar (3.9 MW) `[DECK]` p28/p29 supporting cost. This quarter is the model's stress point made visible on two fronts. Above EBITDA, unit economics deteriorated: Other Expenses rose to 17.17% of revenue from 12.12% `[RESULTS]` L90 and raw-material-consumed intensity ROSE to 80.55% from 76.22% `[RESULTS]` L85 — metal buying got worse; the "better" reported net-material line is purely a Rs15.61 Cr inventory build `[RESULTS]` L86 deferring cost, which reverses when sales catch up. Below EBITDA, the fixed costs of the ramp (depreciation +162.8%, finance +27% `[RESULTS]` L89/L88) are in the P&L while the volume is not — and the deck reveals FY26 depreciation was abnormally low (Rs9.2 Cr vs FY25's Rs18.1 Cr `[DECK]` p23), so the normalised fixed-cost base is heavier than even Q1 shows. The clearest model-drift signals are all deck-sourced: FY26 ROCE fell to 11.6% `[DECK]` p22 (from 16.6%), ROE to 9.9% (from 21.1%), and — the Achilles heel — FY26 operating cash flow was MINUS Rs13.8 Cr `[DECK]` p25, with cumulative FY23-26 CFO/PAT ~0.27x. The model reports profit it does not convert to cash when inventory builds; the same Rs15.61 Cr build that flatters this quarter's gross margin is the annual pattern the deck's own cash flow confirms. A deferred-tax timing shield (current tax only 8.9% of PBT `[RESULTS]` L96) flatters reported profit further. The one thing the deck does NOT resolve is the standalone Q1 cash flow (period-blended with the annual figure), so the quarter-level cash test stays open.

### 4. COMPETITION INTELLIGENCE
Against named peers, Scoda is the smaller, weaker-cash-converting operator, and the deck's own disclosures widen the gap rather than narrow it. On scale, FY26 revenue was Rs518.7 Cr `[DECK]` p23 versus Venus Pipes ~Rs1,167 Cr, Ratnamani ~Rs5,200 Cr and Welspun ~Rs13,000 Cr `[NOTION]` Sheet 3. On margin, Scoda's FY26 EBITDA margin 14.7% `[DECK]` p23 trails Venus ~16% and Ratnamani ~17% `[NOTION]`, and this quarter's operating margin 12.85% `[RESULTS]` widens it. Do NOT read the lower reported net-material cost as a raw-material advantage: consumed intensity actually rose +434 bps `[RESULTS]` L85 and the optics come from the inventory build `[RESULTS]` L86 — on true input economics Scoda slipped this quarter. Where Scoda is decisively weaker is cash and working capital, and the deck now quantifies it on Scoda's own numbers: FY26 CFO −13.8 Cr with cumulative FY23-26 CFO/PAT ~0.27x `[DECK]` p25 (vs Venus ~0.83x, Ratnamani ~0.95x+ `[NOTION]`), inventory days 217 (vs Venus ~121 `[NOTION]`), debtor days 97, and a cash conversion cycle of 211 days (vs Venus ~75-80 `[NOTION]`) `[DECK]` p22 — all worsening year over year. Scoda also lags on disclosure: even in a 40-slide deck it withholds order-book value, welded/seamless utilisation and customer concentration `[DECK]` p6/p16, and posts a capacity figure that is internally inconsistent across slides `[DECK]` p10 vs p28 — versus quarterly-disclosing peers. Where Scoda is BETTER `[NOTION]`: promoter quality (66.43% EXEMPLARY), pre-IPO anchors (Malabar, Carnelian), capex execution, and anti-dumping exposure. The competitive risk to watch: peers convert cash and disclose while Scoda does neither — which is exactly why the destination PE sits at 15x, seven points below Venus's 22x `[NOTION]`. Nothing this quarter narrows the gap; the deck's margin, ROCE, input-intensity and working-capital reads widen it.

---

```yaml
stage: A4-analyst
company: "SCODATUBES"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation]
ledger_reconciliation:
  notes: 7
  turns: 0
  slides: 40
  all_reviewed: true
  a3_findings_incorporated: ["F8-1", "F9-1", "F10-1(results)", "F14-1(results)", "F14-2(results)", "F14-3(results)", "F16-1", "F16-2", "F16-3", "F16-4", "F16-5", "F16-6", "F16-7", "F16-8", "F16-9", "F6-1(deck)", "F7-1(deck)", "F10-1(deck)", "F14-1(deck)", "F14-2(deck)"]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "AVOID (mildly) — Position ZERO (tracking only)"
position_branch: "8A-W"
sc_gap_pat_pct: [0.00, 0.00, 0.00, 0.00]   # Q1FY26, Q4FY26, Q1FY27, FY26 — structurally zero, standalone-only (Note 5, L123; deck also standalone)
questions_for_management:
  - {q: "Welded-plant gross block, full-quarter run-rate depreciation & interest, and welded revenue/utilisation to absorb them by Q3/Q4 FY27?", from_finding_id: "F14-2(results)"}
  - {q: "DTL balance and reversal profile — when does cash-tax ETR normalise toward 25% (current tax only 8.9% of PBT, ~1,603 bps shield)?", from_finding_id: "F8-1"}
  - {q: "Confirm weighted-average share counts for FY25/FY26/Q1FY26 EPS (deck attributes the non-reconciliation to the Rs220 Cr IPO); are prior EPS restated per Ind AS 33?", from_finding_id: "F10-1(results, partially resolved by F10-1 deck)"}
  - {q: "The Rs-13.8 Cr CFO on the 'Q1 FY27' snapshot is the FY26 ANNUAL figure — what is STANDALONE Q1/H1 FY27 CFO, Q1 ROE, and Q1 working-capital days?", from_finding_id: "F16-2"}
  - {q: "Which actuarial assumption changed — Q1 OCI remeasurement 1.71 exceeds full FY26 1.18?", from_finding_id: "F9-1"}
  - {q: "FY26 WC worsened (inv days 163->217, debtor 76->97, CCC 164->211) — Q1 FY27 standalone days vs the <170-by-Q2 target; cyclical or structural?", from_finding_id: "F16-6"}
  - {q: "Order-book VALUE, welded/seamless utilisation %, and current-vs-post-expansion seamless capacity (Slide10 20,068 as current vs Slide28 as post-expansion target with 10,068 existing)?", from_finding_id: "F16-8, F16-9"}
  - {q: "Top-customer concentration at FY26 (still ~26.7%?) and will it be disclosed in the FY26 AR?", from_finding_id: "ND-register/trigger3"}
  - {q: "[MANAGEMENT-ANSWERED, VERIFY Q2] Quantify the freight/RM/April-gas/manpower headwinds behind Other Expenses +80.9% and demonstrate Q2 recovery (Other Exp/revenue back <~13%).", from_finding_id: "F7-1, F6-1"}
  - {q: "FG/WIP built Rs15.61 Cr (+197.6% YoY) while RM-consumed intensity rose +434 bps; how much of the Q1 gross-profit gain reverses as production/sales re-align, and does gross margin hold?", from_finding_id: "A5-graft2/L85,L86; F16-4"}
  - {q: "Deck FY26 ROCE 11.6% is materially below the ~16-17% valuation pillar — is 11.6% the normalised base or transitional, and what is the FY27/FY28 ROCE path?", from_finding_id: "F16-3"}
  - {q: "Deck FY26 D&A Rs9.2 Cr is ~half FY25's Rs18.1 Cr despite fixed assets doubling, yet Q1 annualises to ~Rs16.4 Cr — explain the low FY26 charge and confirm the true run-rate.", from_finding_id: "F16-7"}
  - {q: "Deck names Samarth B Patel 'Chairman & Executive Director' vs filing's Bharatbhai Patel 'Chairman & WTD' (DIN 08036100); MD Jagrutkumar (DIN 06785595). Who chairs the board — is there a transition?", from_finding_id: "F14-1(deck)"}
monitorables:
  - {item: "Standalone Q1/H1 FY27 CFO + cumulative CFO/PAT >0.30x (deck FY26 annual CFO -13.8; cum FY23-26 0.27x < 0.30x)", implied_date: "Q2 FY27 (Nov 2026)", source_ref: "Notion trigger1/thesis-break; F16-1/F16-2"}
  - {item: "Inventory days <170 (Q2), <150 (Q4) — deck FY26 = 217 (>180)", implied_date: "Q2/Q4 FY27", source_ref: "Notion trigger2/thesis-break; F16-6"}
  - {item: "Debtor days / receivables <= revenue growth — deck FY26 76->97, receivables +36.6% vs rev +7%", implied_date: "Q2+Q3 FY27", source_ref: "Notion trigger7; F16-6"}
  - {item: "Customer concentration disclosure (top <20%) — withheld even in deck", implied_date: "FY26 AR", source_ref: "Notion trigger3; F16-8"}
  - {item: "Welded commercial revenue >Rs30 Cr; welded/seamless utilisation; reconciled seamless capacity", implied_date: "Q3/Q4 FY27", source_ref: "Notion trigger4/8; F16-8/F16-9"}
  - {item: "BHEL/NTPC tender won >Rs75 Cr; order-book VALUE (deck only 'healthy pipeline')", implied_date: "Jul-Aug FY27", source_ref: "Notion trigger5; F16-8"}
  - {item: "Marine approvals RINA + BV + first PO — 'applied for', NOT granted", implied_date: "Jun-Sep 2026", source_ref: "Notion trigger6; F16-8"}
  - {item: "FY27 EBITDA margin >=14% all quarters — Q1 operating 12.85% (RED); deck confirms 12.9%", implied_date: "every FY27 q", source_ref: "Notion trigger9; F16-5; A5-graft1"}
  - {item: "Other Expenses/revenue normalising <~13%; 'transient' headwinds reverse (management-answered, verify Q2)", implied_date: "Q2 FY27", source_ref: "A5-graft1/L90; F7-1"}
  - {item: "Gross margin durability as FG/WIP build unwinds; RM-intensity normalising", implied_date: "Q2 FY27", source_ref: "A5-graft2/L85,L86; F16-4"}
  - {item: "Pillar-1 ROCE recovering toward ~16% (deck FY26 ROCE 11.6% vs ~16-17% assumption)", implied_date: "FY27", source_ref: "F16-3"}
  - {item: "FY26 D&A understatement / true run-rate depreciation (deck 9.2 vs FY25 18.1; flatters base ~Rs7-9 Cr)", implied_date: "FY26 AR", source_ref: "F16-7"}
  - {item: "Chairman / governance clarification (deck 'Samarth B Patel Chairman & ED' vs filing 'Bharatbhai Patel Chairman & WTD')", implied_date: "FY26 AR / IR", source_ref: "F14-1(deck)"}
  - {item: "Actuarial assumption reset verification", implied_date: "FY26 AR", source_ref: "F9-1"}
  - {item: "DTL reversal / cash-tax normalisation (current tax 8.9% of PBT)", implied_date: "ongoing", source_ref: "F8-1"}
  - {item: "EPS restatement clarity (residual after IPO-dilution explanation)", implied_date: "FY26 AR / IR", source_ref: "F10-1"}
commitment_register:
  - {commitment: "Welded-segment capacity expansion commissioned", implied_date: "H2 FY27", ref: "Deck Slide6 dL205-206", status_word: "underway"}
  - {commitment: "Achieve FY27 guidance (no numeric target stated in deck)", implied_date: "FY27", ref: "Deck Slide6 dL204", status_word: "reaffirmed-unquantified"}
  - {commitment: "Seamless facility production ramp-up", implied_date: "coming quarters", ref: "Deck Slide6 dL204", status_word: "underway"}
  - {commitment: "Improve operational performance (transient headwinds reverse)", implied_date: "coming quarters", ref: "Deck Slide6 dL202", status_word: "intended"}
  - {commitment: "Marine standards (Bureau Veritas Marine, Rina Marine)", implied_date: "undated", ref: "Deck Slide16 dL536,dL569", status_word: "applied-for"}
flags:
  - "Q1 cash conversion INDETERMINATE: deck's -13.8 Cr CFO is FY26 ANNUAL, period-blended onto a 'Q1 FY27' snapshot (F16-1/F16-2); standalone Q1 CFO still undisclosed; verdict capped at PROCEED WITH CAVEATS"
  - "Deck FY26 annual CFO -13.8; cumulative FY23-26 CFO/PAT 0.27x — BELOW the 0.30x thesis-break line (NOT formally fired: window is FY22-FY27 at FY27-end) — AVOID materially firmer (F16-1)"
  - "Operating EBITDA margin -172 bps to 12.85% (trigger9 RED) driven by Other Expenses +80.9% (ABOVE EBITDA); deck supplies 'largely transient' narrative (freight/RM/April-gas/manpower) to VERIFY at Q2 (F7-1)"
  - "Net material +283 bps 'gain' is an inventory-build cost-deferral artifact: RM-consumed intensity WORSENED +434 bps; same Rs15.61 Cr build is the deck-confirmed cash burn (F16-4)"
  - "Below-EBITDA: depreciation +162.8% and finance +27.0% convert +12.6% operating-EBITDA growth into PAT -25.9%"
  - "Deck FY26 working capital worsening: inventory days 163->217 (>180), debtor 76->97, CCC 164->211, ROE 21.1->9.9% (F16-6); net-D/E 0.3x improvement is post-IPO equity (NEUTRAL)"
  - "Pillar-1 downside: deck FY26 ROCE 11.6% vs ~16-17% assumption (F16-3); flagged to FTTCP, valuation NOT re-run here"
  - "Earnings-quality anomaly: deck FY26 D&A 9.2 (half FY25 18.1) while fixed assets doubled, flatters FY26 PBT/EPS/ROCE ~Rs7-9 Cr (F16-7)"
  - "Deferred-tax timing shield: current tax only 8.9% of PBT (~1,603 bps) (F8-1)"
  - "EPS/IPO dilution RESOLVED-WITH-EXPLANATION: deck EPS FY25 7.6 > FY26 6.8 despite higher PAT = Rs220 Cr IPO dilution (F10-1 deck)"
  - "Single-segment / catalyst non-disclosure continues EVEN IN the deck (trigger8 RED): order-book value, utilisation %, concentration withheld; marine RINA+BV 'applied for' not granted; capacity cross-slide inconsistent (F16-8/F16-9)"
  - "Governance: deck 'Samarth B Patel Chairman & Executive Director' vs filing 'Bharatbhai Patel Chairman & WTD' (DIN 08036100); MD Jagrutkumar (DIN 06785595) confirmed (F14-1 deck)"
  - "Deck independently confirms the corrected results grid (EBITDA -172 bps, PAT -25.9%/-305 bps) — the 7->1 correction cross-validated (F16-5)"
  - "0 of 9 re-engagement triggers GREEN; 6/9 RED or RED-leaning (1/2/6/7/8/9); no thesis-broken condition formally fired"
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/scodatubes-q1fy27/work/review_scodatubes_q1fy27.md"
```
