# STAGE 1: GATE 0 SCORECARD — Apex Ecotech Ltd (APEXECO)
Run date: 2026-07-10
Data sources: screener.in CSV exports (company + 4 peers) + 2 results PDFs (Q4 FY26 signed 06-May-2026; Q2 FY26, 07-Nov-2025). No annual report FY25 file was actually supplied to this stage despite being named in DATA_SOURCES — treated as NOT PROVIDED.

Data available: 9 years (FY18 to FY26). Scoring adapted to 9-year history.
Sub-note: cash flow statement data (screener-data) begins FY20 (7 years); balance-sheet current-liability granularity (needed for ROCE and working-capital-day metrics) is only available for FY25 and FY26, sourced from the two results PDFs. Where full-period data does not exist, the metric is marked N/A and scored 0 per the "never estimate" rule — it is never filled with a proxy.

---

## KEY DATA RECONCILIATION NOTE (read before the blocks)

The two results PDFs report **different FY25 CFO figures for the same audited year**:
- Screener Data Sheet (screener-data) and the 07-Nov-2025 filing (results Q2 FY26, p.5): CFO FY25 = **−14.08 Cr** (−1,408.02 Lakhs)
- FY26 annual audited report (results Q4 FY26, p.9), comparative column: CFO FY25 = **−5.24 Cr** (−524.20 Lakhs)

Reconciled: the FY26 annual report's Note 7 (results Q4 FY26, p.10) discloses a regrouping of "trade retentions" from Trade Receivables to Other Current Assets, which changed the "(Increase)/Decrease in Other Current Assets" working-capital line from −1,305.86 Lakhs (Nov-2025 filing) to −422.04 Lakhs (final FY26 report), flowing through to CFO. The final FY26 audited report (unmodified opinion, most recent, restated) is used as the primary FY25 CFO figure below: **−5.24 Cr**. The discrepancy is noted in data_notes; it does not change any B1/B3 score band (both values land in the same scoring band).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE requires Total Assets − Current Liabilities. Screener's Data Sheet only provides an aggregate "Other Liabilities" line (current + non-current combined) with no split — confirmed by reconciling screener's FY26 "Other Liabilities" (24.61 Cr) against the FY26 PDF balance sheet (Non-current other liabilities+LT provisions 0.76 Cr + Current trade payables/other current liab/ST provisions 23.85 Cr = 24.61 Cr, screener-data / results Q4 FY26 p.8). The split is only recoverable for FY25 and FY26 (the two years with a PDF balance sheet). **ROCE is therefore computed (not sourced — screener's own ROCE/ROE rows were blank in this export) for FY25 and FY26 only; FY18–FY24 are marked N/A (not in provided data).**

- FY26: EBIT = PBT 22.76 + Interest 0.09 = 22.85 (screener-data); Current Liabilities = 24.89+498.90+166.84+1,092.24+627.11 = 2,409.98 Lakhs = 24.10 Cr (results Q4 FY26 p.8); Capital Employed = 89.18 − 24.10 = 65.08 Cr; **ROCE FY26 = 35.12%** (computed)
- FY25: EBIT = PBT 11.38 + Interest 0.17 = 11.55 (screener-data); Current Liabilities = 14.73+287.71+67.78+591.07+331.04 = 1,292.33 Lakhs = 12.92 Cr (results Q4 FY26 p.8, comparative col.); Capital Employed = 59.69 − 12.92 = 46.77 Cr; **ROCE FY25 = 24.70%** (computed)

A1 Median ROCE (n=2): 29.91% → ≥25% = **5**
A2 Minimum single-year ROCE: 24.70% → ≥15% = **5**
A3 Median ROE (n=9, full history, PAT ÷ avg Net Worth; FY18 uses closing NW, opening unavailable, stated): values FY18 13.08%, FY19 20.42%, FY20 53.67%, FY21 −31.82%, FY22 −16.38%, FY23 64.47%, FY24 60.38%, FY25 28.08%, FY26 31.09% (all computed, screener-data). Median = 28.08% → ≥20% = **5**
A4 ROCE trend, latest (FY26 35.12%) vs earliest-available (FY25 24.70%): latest ≥ earliest = **5**

**Block A = 20/20** — flagged low-confidence: A1/A2/A4 rest on only 2 of 9 years.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO available FY20–FY26 (screener-data; FY25 uses the restated −5.24 Cr, see reconciliation note).
CFO (Cr): FY20 5.0, FY21 −0.91, FY22 −0.07, FY23 2.6, FY24 6.69, FY25 −5.24, FY26 6.77 (screener-data; FY25 restated per results Q4 FY26 p.9)
PAT (Cr), same window: FY20 2.67, FY21 −1.65, FY22 −0.66, FY23 3.52, FY24 6.63, FY25 8.56, FY26 17.02 (screener-data)

B1 Cumulative CFO ÷ Cumulative PAT (FY20–26): 14.84 ÷ 36.09 = **0.41** → <0.50 = **0** (unchanged if screener's unrestated FY25 CFO of −14.08 is used instead: 6.00 ÷ 36.09 = 0.166, same band)

Capex (purchase of fixed assets + intangibles, ex-acquisitions) is only itemized in the PDFs, for FY25 and FY26:
FY26 capex = 196.32 Lakhs = 1.96 Cr (results Q4 FY26 p.9); FY25 capex = 10.08 Lakhs = 0.10 Cr (results Q4 FY26 p.9, comparative col.)
FCF FY26 = 6.77 − 1.96 = **+4.81 Cr**; FCF FY25 = −5.24 − 0.10 = **−5.34 Cr**

B2 FCF-positive years as proportion (n=2, only years with capex data): 1 of 2 = 50% → 50-74% = **2**
B3 Cumulative FCF ÷ Cumulative PAT (FY25–26 only, same 2-year window): −0.53 ÷ 25.58 = **−0.02** → negative = **0**
B4 Change in WC Days, FY26 vs FY25 (only 2 years with full Receivable+Inventory+Payable data — payables only disclosed in the PDFs; this is NOT a true latest-vs-earliest-of-9-years comparison, flagged):
  - FY25: Receivable Days = 22.13/70.96×365 = 113.85; Inventory Days = 2.39/70.96×365 = 12.29; Payable Days = (287.71+67.78)/100/70.96×365 = 3.5549/70.96×365 = 18.29 (results Q4 FY26 p.8, comparative col.) → WC Days FY25 = 107.85
  - FY26: Receivable Days = 16.76/148.65×365 = 41.15; Inventory Days = 4.42/148.65×365 = 10.85; Payable Days = (498.90+166.84)/100/148.65×365 = 6.6574/148.65×365 = 16.35 (results Q4 FY26 p.8) → WC Days FY26 = 35.65
  - Change = 35.65 − 107.85 = **−72.2 days** → decreased >5 days = **5**

**Block B = 0+2+0+5 = 7/20** — DEAL-BREAKER #2 TRIGGERED (Block B <8 → max GOOD) and DEAL-BREAKER #4 TRIGGERED (cumulative CFO/PAT <0.50 → max AVERAGE).

Block B trend: **deteriorating**. The one number: cash conversion (CFO÷PAT) fell from 100.9% in FY24 (CFO 6.69 ÷ PAT 6.63) to 39.8% in FY26 (CFO 6.77 ÷ PAT 17.02) even in the "recovered" year — PAT growth is outrunning cash generation. FY25 itself was CFO-negative (−5.24) against PAT-positive (+8.56), driven by a working-capital build (Trade Receivables −943.25 Lakhs, Other Current Assets −422.04 Lakhs, ST Loans & Advances −191.75 Lakhs; results Q4 FY26 p.9) in the year immediately following the company's Dec-04-2024 IPO listing on NSE Emerge (results Q4 FY26 p.10, Note 8) — a pattern consistent with the CLAUDE.md "documented post-IPO rebase" carve-out flagged for downstream review, though Gate 0 itself applies the mechanical cap.

---

## BLOCK C: GROWTH (Max 20)

Revenue (Cr, screener-data): FY18 17.4, FY19 31.0, FY20 44.47, FY21 11.7, FY22 19.51, FY23 34.57, FY24 53.08, FY25 70.96, FY26 148.65
PAT (Cr, screener-data): FY18 0.42, FY19 0.73, FY20 2.67, FY21 −1.65, FY22 −0.66, FY23 3.52, FY24 6.63, FY25 8.56, FY26 17.02

C1 Revenue CAGR FY18→FY26 (8yr, both endpoints positive): (148.65/17.4)^(1/8)−1 = **30.75%** (computed) → ≥20% = **5**
C2 PAT CAGR FY18→FY26 (8yr, both endpoints positive): (17.02/0.42)^(1/8)−1 = **58.86%** (computed) → ≥20% = **5** (note: PAT dipped negative in FY21 −1.65 and FY22 −0.66 mid-window, both recovered by FY23; this is not a loss-to-profit "swing across the window" since both endpoints FY18/FY26 are already positive, flagged for context only)
C3 Positive YoY revenue years: 7 of 8 YoY periods positive (only FY21 vs FY20 declined, −73.7%, screener-data) = 87.5% → 75-99% = **3**
C4 PAT CAGR − Revenue CAGR: 58.86% − 30.75% = **+28.11pp** → ≥+3pp = **5**

**Block C = 5+5+3+5 = 18/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

D1 Net Debt ÷ EBITDA: Borrowings 1.31 Cr − Cash&Bank 35.06 Cr = **−33.75 Cr (net cash)** (screener-data) → **5**
D2 Interest Coverage: EBIT 22.85 ÷ Interest 0.09 = **253.9x** (computed) → ≥10x = **5**
D3 Debt ÷ Equity: Borrowings 1.31 ÷ Net Worth 63.26 = **0.021** (screener-data) → <0.1 = **5**
D4 Current Ratio: Current Assets 85.82 Cr (Inventories 441.93 + Trade Receivables 1,675.73 + Cash&Bank 3,505.94 + ST Loans&Adv 1,200.77 + Other Current Assets 1,757.76 Lakhs, results Q4 FY26 p.8) ÷ Current Liabilities 24.10 Cr = **3.56x** → ≥2.0 = **5**

**Block D = 20/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding pattern, promoter holding, pledge, or contingent-liability data is present anywhere in the six screener CSV exports or the two results PDFs (results PDFs cover only P&L/BS/CF for the half-year and annual filings, not SHP disclosures). Per the "never estimate" rule, all four sub-metrics are marked N/A and scored 0.

E1 Promoter holding: N/A (not in provided data) → **0**
E2 Promoter holding change (3yr): N/A (not in provided data) → **0**
E3 Promoter pledge: N/A (not in provided data) → **0**
E4 Contingent liabilities ÷ Net Worth: N/A (not in provided data) → **0**

**Block E = 0/20** — this is a data-availability gap, not a governance finding; do not read as a governance red flag.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA note: direct summation of screener's individual expense line items reconciled to reported PBT for APEXECO FY23–FY26 but NOT for FY18–FY22 (incomplete sub-line disclosure in the export for those years — e.g. FY18 direct-sum EBITDA of 2.92 implies a PBT of 1.93 against an actual reported PBT of 0.61). EBITDA is therefore back-solved as **PBT + Interest + Depreciation − Other Income** for every year and every company in this block (this ties exactly to reported PBT by construction and was cross-checked against the years that did reconcile). Stated as "computed."

APEXECO EBITDA margin by year (computed, screener-data): FY18 9.20%, FY19 5.90%, FY20 11.92%, FY21 −9.66%, FY22 −1.64%, FY23 12.41%, FY24 16.82%, FY25 15.72%, FY26 14.65%

**M1 Pricing Power**: margin FY18 9.20% → FY26 14.65% = **+5.45pp expansion**; Revenue CAGR 30.75% (≥10%) → expanded ≥2pp AND CAGR≥10% = **5**

**M2 Cost Advantage vs peer median EBITDA margin** (FY26, computed same method for peers):
- CEWATER (Concord Enviro): PBT 22.67+Int 20.93+Dep 16.57−OI 24.77 = 35.40 ÷ Sales 557.86 = 6.35% (CEWATER-Data_Sheet)
- EIEL (Enviro Infra Engineers): PBT 249.63+Int 36.01+Dep 24.80−OI 33.62 = 276.82 ÷ Sales 1,145.60 = 24.16% (EIEL-Data_Sheet)
- EMSLIMITED: PBT 129.22+Int 13.25+Dep 10.21−OI 12.25 = 140.43 ÷ Sales 732.75 = 19.16% (EMSLIMITED-Data_Sheet)
- FELIX: PBT 26.69+Int 3.16+Dep 2.02−OI 3.66 = 28.21 ÷ Sales 102.21 = 27.60% (FELIX-Data_Sheet)
- Peer median = 21.66%; APEXECO FY26 = 14.65%, **7.01pp below** median → below = **0**

**M3 Capital Efficiency**: FAT = Sales 148.65 ÷ Net Block 1.96 = **75.8x** (screener-data); ROCE FY26 35.12% (computed above). FAT>3x AND ROCE>20% = **5**

**M4 Customer Stickiness**: 1 revenue-decline year only (FY21, screener-data), recovered and surpassed the prior peak by FY24 (53.08 > FY20's 44.47) → max 1 decline year, fully recovered = **3** (receivable days not stable ±10 across the period — range 41 to 138 days — so the 5-band does not apply)

**M5 Scale & Dominance**: Market Cap (screener-data headers): EIEL 4,008.93 Cr > EMSLIMITED 2,328.41 Cr > CEWATER 661.24 Cr > **APEXECO 319.21 Cr** > FELIX 314.79 Cr. APEXECO ranks 4th of 5 — within top 5, not top 3 → **1**

**M6 Technology/R&D**: no R&D line item disclosed anywhere in the data → N/A (not in provided data) → **0**

**M7 Regulatory/License**: no authoritative count of listed players in the ETP/STP/ZLD segment, nor confirmation of a license-scarcity dynamic, is present in provided data (4 named peers is not confirmed as the full universe) → N/A, "PEER DATA NEEDED" for a definitive count → **0**

**M8 Distribution**: no distribution/outlet/reach data provided (B2B project business, no network disclosed) → N/A (not in provided data) → **0**

**M9 Brand**: gross-margin proxy = (Revenue − Material Cost) ÷ Revenue, stated as proxy, FY26:
- APEXECO: (148.65−112.33)/148.65 = **24.43%** (screener-data)
- CEWATER: (557.86−302.02)/557.86 = 45.86% (CEWATER-Data_Sheet)
- EIEL: (1,145.60−747.65)/1,145.60 = 34.74% (EIEL-Data_Sheet)
- EMSLIMITED: Raw Material Cost not disclosed in export (blank) → excluded from peer median, "PEER DATA NEEDED" for this one company
- FELIX: (102.21−35.93)/102.21 = 64.85% (FELIX-Data_Sheet)
- Peer median (3 peers) = 45.86%; APEXECO 24.43% is **below** median → at/below = **0**

**M10 Switching Costs**: revenue grew all but 1 year (FY21 decline, screener-data); receivable days moved from 101.75 (FY18) to 41.15 (FY26) — a large decrease, not a rise, so "stable" condition is satisfied → growth all but 1 year AND stable = **3**

**M11 Network Effects** (9 years available, ≥6yr test applies): latest-3yr revenue CAGR (FY23→FY26): (148.65/34.57)^(1/3)−1 = **62.65%**; prior-3yr CAGR (FY20→FY23): (34.57/44.47)^(1/3)−1 = **−8.05%**. Latest > prior. Selling & admin % of sales: FY23 5.50%, FY24 5.92%, FY25 5.78% (screener-data) — FY26 selling & admin not separately disclosed (lumped into "Other Expenses"), so the full-window trend cannot be confirmed; available years show roughly stable, not clearly declining → scored on the growth condition plus available-year stability: rev CAGR ≥20% AND selling% stable/declining (partial data) = **3**, flagged for the FY26 data gap

**M12 Negative WC / Float**: WC days only fully computable for 2 years (FY25 107.85, FY26 35.65, both computed above) — neither negative, and this is not a "majority of years" sample. Latest year (FY26, 35.65) falls in the 15-45 band → **1**, flagged as a 2-year sample, not a multi-year "consistently" read

**Block F (Moat) = 5+0+5+3+1+0+0+0+0+3+3+1 = 21/60**

Moats present (score ≥3): M1 (5), M3 (5), M4 (3), M10 (3), M11 (3) = **5 moats confirmed**
Moat classification: 4-5 present = STRONG → **STRONG**

---

## MOAT PROFILE

```
M1  Pricing Power        [#####] 5  PRESENT
M2  Cost Advantage       [     ] 0
M3  Capital Efficiency   [#####] 5  PRESENT
M4  Customer Stickiness  [###  ] 3  PRESENT
M5  Scale & Dominance    [#    ] 1
M6  Technology/R&D       [     ] 0  N/A no data
M7  Regulatory/License   [     ] 0  N/A no data
M8  Distribution         [     ] 0  N/A no data
M9  Brand                [     ] 0
M10 Switching Costs      [###  ] 3  PRESENT
M11 Network Effects      [###  ] 3  PRESENT (partial data)
M12 Negative WC/Float    [#    ] 1  (2-yr sample only)
```

---

## CLASSIFICATION BOX

```
Block A (Return on Capital)      20 / 20   [LOW CONFIDENCE: n=2 yrs for ROCE]
Block B (Cash Generation)         7 / 20   [DEAL-BREAKER x2]
Block C (Growth)                 18 / 20
Block D (Balance Sheet)          20 / 20
Block E (Shareholder Alignment)   0 / 20   [DATA GAP, not a governance finding]
------------------------------------------
CORE SCORE                       65 / 100

Moat Score (Block F)             21 / 60   → 5 moats confirmed → STRONG
------------------------------------------
GRAND TOTAL                      86 / 160
```

Data confidence: 9 years of P&L/BS history = "7-9 moderate" band. No automatic history-based classification downgrade (only applies at 3-4 years). history_downgrade = false.

Pre-override matrix result: Core 65 (60-79 band) + STRONG moat → **GOOD+**

Deal-breaker overrides triggered:
- #2 Block B <8 (actual 7) → caps at max GOOD
- #4 Cumulative CFO ÷ PAT <0.50 (actual 0.41) → caps at max AVERAGE

Most restrictive cap applies: **AVERAGE**

Years driving the deal-breakers (per CLAUDE.md instruction to name them for downstream position-sizing review): FY25 is the primary driver — CFO −5.24 Cr against PAT +8.56 Cr, a working-capital build in the year immediately following the Dec-04-2024 IPO listing (results Q4 FY26 p.10, Note 8). FY20-FY22 (COVID-period, PAT swung negative in FY21/FY22) also weigh down the cumulative CFO/PAT ratio. This has the shape of the CLAUDE.md-referenced "documented post-IPO rebase" case eligible for downstream position-sizing override, but Gate 0 applies the mechanical cap regardless per pipeline rules (company-quality flags never halt the run; only mechanical failures halt, and there is no STOP verdict at this stage).

**Strongest block**: Block D (Balance Sheet Strength), 20/20, net-cash, near-zero leverage, high liquidity — full marks with no data caveats (contrast with Block A's also-20/20 score, which carries a 2-year-sample caveat).
**Weakest block**: Block E (Shareholder Alignment), 0/20, entirely a data-availability gap (no SHP data provided) rather than a scored deficiency.

---

## DECISION LINE

**Classification: AVERAGE** (capped from a pre-override GOOD+ by deal-breakers #2 and #4). Core 65/100, moat STRONG (5 of 12 tests confirmed present), grand total 86/160. Flag for downstream: the cash-conversion deal-breaker is concentrated in FY25, the year following the company's Dec-2024 IPO listing, and may warrant a documented post-IPO rebase override at the position-sizing stage — but that determination sits outside Gate 0's mechanical scope. Block E (shareholder alignment) is unscored due to missing data, not a governance finding; a shareholding-pattern source is needed before any alignment conclusion can be drawn. No credit-rating PDF was provided either (carried forward as an input gap).

---

```yaml
stage: B01-gate0
company: "APEXECO"
run_date: "2026-07-10"
model: claude-sonnet-5
status: complete
input_gaps:
  - {type: rating, detail: "no credit rating PDF provided"}
  - {type: shareholding, detail: "no shareholding pattern / promoter holding / pledge / contingent liabilities data provided in screener exports or results PDFs; Block E scored 0/20 as a data gap, not a governance finding"}
flags:
  - {type: FLAG-GATE0, reason: "Classification capped at AVERAGE (pre-override GOOD+) by deal-breaker #2 (Block B=7, <8) and deal-breaker #4 (cumulative CFO/PAT=0.41, <0.50). Primary driver is FY25: CFO -5.24 Cr (restated per results Q4 FY26 p.9; screener/Nov-2025 filing shows -14.08 Cr) against PAT +8.56 Cr, a working-capital build in the year immediately following the Dec-04-2024 IPO listing (results Q4 FY26 p.10, Note 8). FY20-FY22 COVID-period CFO/PAT weakness also contributes. Possible documented post-IPO rebase case for downstream position-sizing review."}
  - {type: FLAG-DATA-GAP, reason: "Block A (20/20) rests on only 2 of 9 years (FY25-FY26) of computable ROCE; FY18-FY24 ROCE is N/A because screener's Data Sheet 'Other Liabilities' line combines current and non-current liabilities with no split, and no balance sheet source exists for those years beyond screener. Treat Block A's full score as low-confidence."}
  - {type: FLAG-DATA-GAP, reason: "Block E (shareholder alignment) is 0/20 solely because no shareholding pattern, pledge, or contingent-liability data was provided anywhere in the input set."}
  - {type: FLAG-DATA-GAP, reason: "FY25 CFO conflicts between the 07-Nov-2025 filing (-14.08 Cr) and the FY26 annual audited report's restated comparative (-5.24 Cr), traced to a Note 7 reclassification of trade retentions between Trade Receivables and Other Current Assets. Restated audited figure used; does not change any score band."}
data_years: 9
fy_range: "FY18 to FY26"
blocks: {A: 20, B: 7, C: 18, D: 20, E: 0}
core_score: 65
moat_score: 21
grand_total: 86
moats_confirmed: 5
moat_class: "STRONG"
classification: "AVERAGE"
deal_breakers:
  - "#2 Block A/B threshold: Block B = 7 (<8) -> caps at max GOOD"
  - "#4 Cumulative CFO/PAT = 0.41 (<0.50) -> caps at max AVERAGE (most restrictive, applied)"
history_downgrade: false
data_notes:
  - "FY25 CFO discrepancy between filings (see flags); restated audited figure -5.24 Cr used as primary"
  - "ROCE computable only for FY25 and FY26 (current-liability split unavailable pre-FY25 in provided data); FY18-FY24 marked N/A"
  - "WC Days (B4) computable only FY25->FY26 (payables data only in PDFs for those 2 years), not a true 9-year latest-vs-earliest comparison"
  - "FCF/Capex (B2, B3) computable only FY25 and FY26 (purchase of fixed assets only itemized in PDFs for those years)"
  - "EBITDA back-solved as PBT + Interest + Depreciation - Other Income for all years/companies because direct expense-line summation did not reconcile to reported PBT for APEXECO FY18-FY22 (incomplete sub-line disclosure in screener export)"
  - "M9 gross-margin proxy used: (Revenue - Material Cost) / Revenue; EMS Ltd excluded from peer median for M9 (Raw Material Cost not disclosed in its screener export), PEER DATA NEEDED for that one comparison"
  - "M7 scored 0: PEER DATA NEEDED for an authoritative count of listed players in the ETP/STP/ZLD segment"
  - "M11 selling-expense trend assessed only FY23-FY25; FY26 selling & admin expense not separately disclosed (lumped into Other Expenses)"
  - "PAT dipped negative in FY21 (-1.65 Cr) and FY22 (-0.66 Cr), both recovered by FY23; not a loss-to-profit swing across the CAGR window since both endpoints (FY18, FY26) are already positive, noted for context"
block_b_trend: "deteriorating - cash conversion (CFO/PAT) fell from 100.9% in FY24 (6.69/6.63) to 39.8% in FY26 (6.77/17.02) even as CFO nominally recovered from FY25's negative print"
```
