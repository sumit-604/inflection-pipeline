# B10 VALUATION INPUTS ASSEMBLY — Fabtech Technologies Ltd (FABTECH)

**Stage 10 Output | Haiku 4.5 | Run Date 2026-08-04**

This stage assembles the complete Role 1 valuation input table. Every value is anchored to a source block or PDF; unresolved fields are listed separately. Phase 3 stage 11 receives this table and applies the operator-approved destination exit PE of 13x on a one-year-forward FY27 EPS basis.

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|---|---|---|
| Company | FABTECH | manifest |
| Ticker | FABTECH (BSE 544558, NSE FABTECH) | manifest |
| Sector (corrected) | EPC / Civil construction | fttcp-deliberation (override from Pharma/CDMO 38x) |
| Business model type | Hybrid: Turnkey EPC (75.51% revenue) + Equipment supply (24.49%) | B04 |
| Sector cap row | 20x EPC/Civil construction | fttcp-deliberation, operator-approved |
| CMP (as of 2026-08-04) | Rs 152 | manifest |
| Market cap | Rs 675 Cr | manifest (4.445 Cr shares × 152) |
| Shares outstanding (diluted) | 4.445 Cr | task briefing, verified consolidated balance sheet FY26 |
| **Enterprise Value** | **Rs 536.07 Cr** | Calc: Mcap 675 + Net Cash (-138.93) |
| — Calculation detail | Borrowings (FY26) Rs 69.64 Cr − Cash Rs 208.57 Cr = Net Cash Rs 138.93 Cr | screener-Data_Sheet.csv consolidated FY26 rows |

---

## LATEST FINANCIALS (FY26, CONSOLIDATED BASIS)

### Income Statement & Key Margins

| Field | Value | Anchor |
|---|---|---|
| **Revenue (sales)** | **Rs 410.77 Cr** | screener-Data_Sheet.csv FY26 (2026-03-31); Q4 FY26 call actual total income |
| EBITDA | Rs 55.56 Cr | B05 Q4 FY26 call actual ("FY26 actual EBITDA Rs 55.56 Cr, +18.29% YoY") |
| EBITDA margin | 13.52% | Calc: 55.56 / 410.77 |
| — Note on EBITDA | Operating EBITDA (excl. other income) is Rs 35.00 Cr (8.52% margin) | fttcp-deliberation ruling 10 |
| **PAT (net profit)** | **Rs 38.36 Cr** | consolidated audited results, year ended March 31, 2026; owners attributable Rs 3,835.80 Lakh |
| PAT margin | 9.34% | Calc: 38.36 / 410.77 |
| **Diluted EPS** | **Rs 5.75** | consolidated audited results, year ended March 31, 2026 (Diluted Earnings Per Share) |
| Other income (quality caveat) | Rs 20.56 Cr | task briefing; 42.6% of PBT before exceptional (Rs 46.10 Cr statutory basis) |

### Cash Flow & Returns

| Field | Value | Anchor |
|---|---|---|
| **CFO (Operating cash flow)** | **Rs 0.48 Cr** | consolidated cash flow statement, year ended March 31, 2026 (Rs 47.74 Lakh) |
| FCF (Free cash flow) | −Rs 4.23 Cr | Calc: CFO 0.48 − Capex 4.71 |
| **CFO / PAT (latest)** | **1.25%** | Calc: 0.48 / 38.36 |
| CFO / PAT (cumulative FY23-FY26) | 8.1% | B01, task briefing |
| FCF / PAT | −11.0% | Calc: −4.23 / 38.36 |
| P/FCF | NOT MEANINGFUL | FCF negative; cannot compute |
| **Cash conversion determination** | **STRUCTURAL** | fttcp-deliberation: CRISIL 15 October 2025 states contractual causes (Q4-heavy milestone billing, 2-year retention money) continue medium-term |
| **Cash trend direction** | **Deteriorating** | B01: FY26 CFO ~1% vs FY24 CFO 222% of PAT; FY23, FY25 both CFO-negative despite profit |

### Balance Sheet & Capital Allocation

| Field | Value | Anchor |
|---|---|---|
| **Book value per share** | **Rs 94.43** | Calc: Consolidated equity 419.77 Cr / 4.445 Cr shares |
| Net debt / (cash) | −Rs 138.93 Cr (net CASH) | Calc: Borrowings 69.64 − Cash 208.57 Cr (FY26 consolidated) |
| **Capex** | **Rs 4.71 Cr** | consolidated cash flow "Payment for property, plant and equipment and intangible assets" FY26 (Rs 470.81 Lakh) |
| Depreciation | Rs 5.30 Cr | consolidated P&L, year ended March 31, 2026 |
| **DPS (final dividend FY26)** | **Rs 0.60/share** | task briefing; Board meeting 2026-07-24, total Rs 2.67 Cr for 4.445 Cr shares |

### Profitability Trends

| Field | Value | Anchor |
|---|---|---|
| **ROCE (latest FY26)** | **11.25%** (statutory) | B01-gate0.yaml; statutory basis |
| ROCE (operational, forward route) | 16.2% (Route A operational) | fttcp-deliberation operator override; also note fuller-strip 17.9% alternative |
| ROCE trend (2-year) | **Deteriorating** | FY23: 29.32% → FY25: 22.06% → FY26: 11.25% (B01) |
| Cause of ROCE depression | Rs 207.5 Cr IPO proceeds largely undeployed (Oct 2025), inflating capital employed | B01 |
| **ROE (FY26)** | **9.14%** (calculated consolidated basis) | Calc: PAT 38.36 / Equity 419.77; B01 cites 12.94% (likely using different basis or pre-IPO) |
| Revenue 3-year CAGR (FY24-FY26) | 28.4% | Calc: (410.77 / 226.14)^0.5 − 1; screener base years |
| PAT 3-year CAGR (FY24-FY26) | 18.7% | Calc: (38.36 / 27.22)^0.5 − 1 |

---

## FORWARD GUIDANCE & MANAGEMENT CREDIBILITY

| Field | Value | Anchor |
|---|---|---|
| **FY27 revenue growth guidance** | **20-25% YoY** | B05: reaffirmed Q1 FY27 call (walked down from 30-40% in Q3 FY26) |
| **FY27 PAT margin guidance** | **9.9%-10.5%** | B05: Q4 FY26 call, reaffirmed Q1 FY27 call |
| Implied FY27 revenue range | Rs 492.92 Cr to Rs 512.46 Cr | Calc: FY26 410.77 × 1.20 to 1.25 |
| Implied FY27 PAT range | Rs 48.79 Cr to Rs 53.91 Cr | Calc: implied revenue × margin guidance 9.9% to 10.5% |
| **Q1 FY27 actual (quarterly)** | Revenue Rs 74.98 Cr, PAT Rs 4.21 Cr | Q1 FY27 consolidated results, June 30, 2026 |
| Management credibility grade | **C (Mixed)** | B05: Genuine operational delivery (FY26 beat, Q4 on target) offset by guidance walkdown, unresolved revenue-recognition promise, deflected investor questions, silence on auditor KAM |
| Promise-delivery track | 3 delivered clean, 2 partial, 5 missed out of 10 tracked promises | B05 |

---

## EMERGING MOAT & CATALYSTS (12-MONTH WINDOW)

| Field | Value | Anchor |
|---|---|---|
| **EM Score** | **19 (MODEST)** | B07 |
| EM Classification | MODEST | B07 |
| **Primary catalysts within 12m** | 1. SACE (Saudi) incremental order wins beyond first civil order (next 2-3 qtr); 2. Africa vaccine pipeline − three projects in discussion (next 1-2 qtr); 3. Europe/JBN acquisition close (next 2-3 qtr, already slipped); 4. H2 FY27 revenue acceleration test (Oct 2026-Mar 2027) | B07 catalysts_12m |
| Evidence mix | 20 documented, 12 claim-based, 5 inference | B07 completionist_recount |
| Summary evidence quality | Mostly-documented with material claim component | B07 evidence_mix |
| **Top 2-3 growth triggers** | **Trigger 1 (HIGH conviction):** Order book execution (>Rs 900 Cr, H2-weighted 18-24mo conversion; Trigger 2 (HIGH):** Saudi Vision 2030 localization via SACE qualification; Trigger 3 (HIGH):** Africa diversification (Kenya, Morocco, Botswana, animal health) | B05 triggers priority 1-3 |

---

## QUALITY & GOVERNANCE FLAGS

| Field | Value | Anchor |
|---|---|---|
| **Gate 0 Classification** | **AVOID (63/160)** | B01: Limited history (4 usable years post-IPO Oct 2025), cumulative CFO/PAT 8.1% triggers cap at AVERAGE |
| **Promoter verdict** | **CONCERN** | B08: Lead promoter Aasif Khan (41.52%) named in pending criminal fraud complaint; 16.7% RPT dependency; unresolved related-party loan default; 0% pledge confirmed |
| **Cash conversion verdict** | **STRUCTURAL FLAG** | fttcp-deliberation: Contractual milestone billing, Q4 concentration, retention money per CRISIL medium-term outlook |
| **Related-party risk flags** | RPT 16.7% of revenue; no non-compete with sister LISTED company Fabtech Technologies Cleanrooms Ltd (BSE 544332); material land purchase undisclosed in RPT note | B02, B03, B08 |
| **Receivables quality** | Auditor KAM: Rs 58.9 Cr overdue >365 days; gross receivables grew 38.5% vs revenue 25.7%; management silent on KAM across all three concalls | B02, B03 |
| **SHARED CATALYST FLAG** | **YES** | fttcp-deliberation: IPO proceeds deployment drives both Route A ROCE recovery and Pillar 3a capex-embedded growth; single point of failure |

---

## UNDISCOVERED ALPHA (UA) QUALIFIER CHECK

| Field | Value | Anchor |
|---|---|---|
| **Listed ≥12 months?** | **NO** | IPO 2025-10-07; run date 2026-08-04 = ~10 months; fails 12-month gate |
| **Gate 0 ≥60 OR EM ≥25?** | **NO** | Gate 0 = 63/160 AVOID (fails), EM = 19 MODEST (below 25 threshold) |
| **FII + DII < 3%?** | **YES** | Operator June 2026 data: FII 0.02% + DII 2.45% = 2.47% (passes) |
| **All three qualifiers met?** | **NO** | Fails listing and Gate0/EM tests |
| **UA Applied?** | **NO** | UA does not apply; fails on listed and quality gates (fttcp-deliberation ruling 13) |
| **Stockholding pattern (June 2026)** | Promoters 68.94% (flat three quarters), FII 0.02%, DII 2.45%, Public 28.57% | fttcp-deliberation operator input; task briefing "operator-supplied June 2026" |

---

## SECTORAL OPPORTUNITY (SOM-IMPLIED vs MANAGEMENT GUIDANCE)

| Field | Value | Anchor |
|---|---|---|
| **TAM (conservative / realistic)** | Rs 2,000 Cr / Rs 4,400 Cr | B09 |
| **SAM (serviceable addressable market)** | Rs 2,150 Cr | B09 |
| **SOM 3-year (FY26-FY29 base)** | Rs 635 Cr | B09 |
| **SOM 5-year (FY26-FY31 base)** | Rs 787 Cr | B09 |
| **SOM-implied revenue CAGR** | 3-year: 13.8%; 5-year: 12.8% | B09 |
| **Gap vs management guidance** | Management 20-25% exceeds SOM capacity ceiling | B09: "management's own 20-25% guidance would exceed the B07 capex-embedded capacity ceiling (83%) by Rs 284-526 Cr over 5 years" |
| **Capacity assessment** | 5yr +82.5% growth vs 83% capex-embedded ceiling; near-zero margin under SOM scenario | B09 |
| **Management's $30bn/$70bn claim** | INFLATED / unattributed | B09 / B05: Management claim untriangulated by all 4 comparable peers; unit-ambiguous (stock vs flow); methodology undated |

---

## FORWARD ONE-YEAR EPS ASSEMBLY (FOR 13x EXIT PE APPLICATION)

**Basis: Management guidance + Q1 FY27 actual, no invented point estimate beyond guidance support**

### Calculation Framework

| Component | Value | Anchor |
|---|---|---|
| **FY26 actual revenue (base)** | Rs 410.77 Cr | consolidated audited |
| **Guidance: 20% growth scenario** | Revenue = 410.77 × 1.20 = Rs 492.92 Cr | B05 lower-bound guidance |
| **Guidance: 25% growth scenario** | Revenue = 410.77 × 1.25 = Rs 512.46 Cr | B05 upper-bound guidance |
| **Margin guidance: 9.9% (lower)** | Rs 492.92 × 0.099 = Rs 48.79 Cr PAT | B05 |
| **Margin guidance: 10.5% (upper)** | Rs 512.46 × 0.105 = Rs 53.81 Cr PAT | B05 |
| **Diluted shares (constant)** | 4.445 Cr | manifest |

### Forward FY27 EPS Range

| Scenario | Revenue | PAT (implied) | ÷ Shares | EPS | Anchor |
|---|---|---|---|---|---|
| **Conservative** (20% growth, 9.9% margin) | Rs 492.92 Cr | Rs 48.79 Cr | 4.445 Cr | **Rs 10.98/share** | B05 guidance |
| **Base case** (midpoint 22.5% growth, 10.2% margin) | Rs 503.19 Cr | Rs 51.32 Cr | 4.445 Cr | Rs 11.55/share | calc from guidance |
| **Optimistic** (25% growth, 10.5% margin) | Rs 512.46 Cr | Rs 53.81 Cr | 4.445 Cr | **Rs 12.11/share** | B05 guidance |

**Forward FY27 EPS: Rs 10.98 to Rs 12.11 per share**

### Quality Caveats

1. **Other Income Dependency:** Rs 20.56 Cr (42.6% of PBT before exceptional) inflates reported profit quality (B05, task briefing, fttcp-deliberation ruling 10)
2. **Guidance Walkdown History:** FY27 growth already walked down from 30-40% → 25% → 20-25% within two quarters (B05)
3. **Cash Conversion Weakness:** Structural WC deterioration not addressed by margin guidance; CFO/PAT only 1.25% FY26 vs 222% FY24 (B01)
4. **Q1 FY27 Run Rate:** Revenue Rs 74.98 Cr (Q1) annualizes to ~Rs 300 Cr if sequential, materially below guidance base unless H2 acceleration (Q1 FY27 results, B05 trigger 1)
5. **No Revenue Recognition Transition Impact:** 3+ quarters of unresolved shipment vs percentage-of-completion decision creates quarterly volatility risk (B05)

---

## UNRESOLVED FIELDS

| Field | Why Missing | Where It Might Be |
|---|---|---|
| **Rating agency, rating level, outlook** | Rating PDF not provided to this stage; CRISIL commentary is embedded in deliberation record but rating level/outlook not extracted | Rating PDF or CRISIL release (Oct 15, 2025) |
| **Peer P/E, EV/EBITDA, P/B medians** | B06 peer analysis provided substantive coverage of 4 peers (Anup, HLE Glascoat, Ion Exchange, Praj) but did not tabulate specific multiples for each | B06 concall summaries or dedicated peer data sheet |
| **Revenue-recognition method (concrete disclosure basis)** | Unresolved across 3 concalls despite analyst pressure; management stated "under evaluation" with "next few years" timeline as of Q1 FY27 | Company's next quarterly/annual filing or management clarification |
| **Order book geography/segment breakdown** | Requested in all 3 concalls; Q4 FY26 promised "in a minute" but never delivered; Q1 FY27 stated company does not have the split | Next quarterly results or investor presentation breakout |
| **Proposal-to-order win-rate improvement trajectory** | FY26 claimed improvement to 16-17% but earlier cited 10-12%; inconsistent without reconciliation, not reaffirmed Q1 FY27 | Next concall or management clarification |
| **IPO proceeds deployment plan (inorganic tranche timeline)** | Only 22.2% of Rs 230.3 Cr deployed by FY26 year-end; inorganic-growth tranche 0% deployed; revised timeline not disclosed | Note 53-equivalent in next filing or exchange announcement |
| **Exact nature of the lease liability lessor (Rs 2,903 Lakh Q4 FY26)** | Circumstantial evidence points to related party Fabtech Turnkey Projects LLP but not explicitly confirmed; 11x jump unexplained | Company secretary confirmation or next audit finding |
| **Consolidated receivables balance-sheet-to-Note-13 reconciliation** | Rs 37.18 Cr (18.2%) gap on auditor's sole KAM line; unreconciled in FY26 filing | Next quarterly or annual filing reconciliation |
| **Section 164(2) director disqualification details** | Consolidated auditor's report flags at group level; quantum and individual name(s) not detailed in sources available | MCA filings or next auditor's report clarification |

---

## CONFLICTS (UPSTREAM DISAGREEMENTS)

| Field | Value A | Anchor A | Value B | Anchor B | Used in Table |
|---|---|---|---|---|---|
| ROE FY26 | 9.14% | Calculated consolidated (38.36 / 419.77) | 12.94% | B01-gate0.yaml | Calculated 9.14% marked; B01 figure noted as possibly using different basis |
| FY26 Other income magnitude | Rs 20.56 Cr | Consolidated audited (Rs 2,055.77 Lakh) | Rs 22.74 Cr | screener-Data_Sheet.csv FY26 "Other Income" row | Rs 20.56 Cr (consolidated, authoritative for consolidated PAT) |
| Guidance PAT range (FY27) | Rs 48.79–53.81 Cr | Calculated from management 20-25% growth × 9.9-10.5% margin | Rs 45–51 Cr | Alternative conservative read (B09 SOM lower range) | B05 management guidance used (48.79–53.81 Cr), flagged with SOM gap warning |

---

## CROSS-REFERENCES TO AUTHORITATIVE DELIBERATION

The **fttcp-deliberation.md** record carries operator-approved valuations that supersede earlier determinations:

1. **Pillar 1 ROCE:** Operational route 16.2% (statutory 11.25%, fuller-strip alternative 17.9%)
2. **Pillar 2 cash multiplier:** 0.65x structural, no growth offset
3. **Pillar 3 growth premium:** +2x (capped by SOM CAGR 13.8%, grade C, visibility 2.19y)
4. **Strategic premium:** +0x (no monopoly, weak pricing power)
5. **Sector cap:** 20x EPC/Civil construction (corrected from Pharma/CDMO 38x)
6. **APPROVED DESTINATION EXIT PE:** **13x** (operator override; applied to **ONE-YEAR FORWARD FY27 EPS**)
7. **Forward earnings basis:** One-year-forward FY27 EPS (operator override)
8. **Tier and hurdle:** Tier A, 25% (fails Tier B on Gate 0 AVOID + promoter CONCERN + FLAG-CASH)
9. **Active flags carried forward:** FLAG-PROMOTER (CONCERN), FLAG-CASH (STRUCTURAL), FLAG-GATE0 (AVOID 63/160)

---

## END OF ASSEMBLY

All values are anchored. Unresolved fields are listed above. No estimates beyond guidance-supported ranges. Forward EPS range ready for 13x exit PE application in phase 3 stage 11 valuation.

**Prepared by:** Claude Haiku 4.5 (stage-10-assembly-pipeline)  
**Date:** 2026-08-04  
**Status:** Complete
