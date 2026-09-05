# STAGE 1: GATE 0 SCORECARD — AEQUS (Aequs Ltd), consolidated

Run date: 2026-09-05. CMP Rs 242.18, market cap Rs 16,242.18 cr (screener-data).
Listed 10-Dec-2025 (IPO); AR FY2025-26 signed 26-May-2026; Q1 FY27 result 29-Jul-2026.

Data available: 4 years (FY23 to FY26) for revenue, PAT, borrowings, net worth, cash
flow totals (screener-Data_Sheet.csv). Scoring adapted to 4-year history.
SUB-CONSTRAINT: the sole Annual Report in this corpus (FY2025-26) discloses a
consolidated balance sheet with current/non-current split and Trade Payables only
for FY26 and FY25 (2 years; no prior-year AR in corpus). ROCE (A1/A2/A4), Working
Capital Days (B4) and FCF/Capex (B2/B3) are therefore computable only for FY25-FY26,
not the full FY23-FY26 window. This is stated at every affected line below, not
silently narrowed.

No results PDFs, no rating PDF, no shareholding pattern, no prospectus in this
corpus (input_gaps carried from B00). Block E (shareholder alignment) is
therefore N/A across three of four sub-tests.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE = EBIT ÷ (Total Assets − Current Liabilities). Computed (not screener-supplied;
screener-Data_Sheet carries no ratios tab, only raw P&L/BS/CF lines). EBIT = PBT +
Interest (screener-data). Capital employed = Total Assets − Total Current
Liabilities, both from the AR Consolidated Balance Sheet (AR p.227) — the only
source in corpus with the current/non-current split, hence FY25-FY26 only.

| Year | PBT (cr) | Interest (cr) | EBIT (cr) | Total Assets (cr) | Curr. Liab (cr) | Cap. Employed (cr) | ROCE |
|---|---|---|---|---|---|---|---|
| FY25 | -94.01 (screener-data) | 64.33 (screener-data) | -29.68 (computed) | 1,859.84 (AR p.227) | 676.42 (AR p.227) | 1,183.42 (computed) | -2.51% (computed) |
| FY26 | -71.49 (screener-data) | 94.36 (screener-data) | 22.87 (computed) | 2,690.47 (AR p.227) | 822.65 (AR p.227) | 1,867.82 (computed) | 1.22% (computed) |
| FY23, FY24 | -103.45 / -4.28 (screener-data) | 68.58 / 69.16 (screener-data) | — | NOT FOUND (no current-liability split in any corpus source for FY23/FY24) | — | — | NOT FOUND |

- A1 Median ROCE (2 of 4 years available): median(-2.51%, 1.22%) = -0.65% → **<10% → score 0**
- A2 Minimum single-year ROCE (2 of 4 years): -2.51% (FY25) → **<8% → score 0**
- A3 Median ROE (PAT ÷ avg Net Worth; FY23 uses closing Net Worth only, opening
  unavailable, stated per formula rule):
  - FY23: PAT -98.83 (screener-data) ÷ NW 278.61 (screener-data, closing only) = -35.47% (computed)
  - FY24: PAT -10.84 ÷ avgNW 344.03 = -3.15% (computed)
  - FY25: PAT -102.35 ÷ avgNW 563.19 = -18.17% (computed)
  - FY26: PAT -113.25 ÷ avgNW 1,101.71 = -10.28% (computed)
  - Median = -14.23% → **<12% → score 0**
- A4 ROCE trend, latest (FY26 1.22%) vs earliest available (FY25 -2.51%): +3.73pp,
  latest ≥ earliest → **score 5**. FLAG: this is a 2-year window with both values
  near zero; not a robust multi-year trend, applied mechanically per the rule.

**Block A = 0+0+0+5 = 5 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

- B1 Cumulative CFO ÷ Cumulative PAT (4 years, screener-data):
  CFO: 9.81, -19.11, 26.14, -98.75 (FY23-26) → cum. -81.91
  PAT: -98.83, -10.84, -102.35, -113.25 → cum. -325.27
  Ratio = 0.2518 (both negative; magnitude ratio only) → **<0.50 → score 0**
- B2 FCF-positive years as proportion. Capex (= "Acquisition of property, plant
  and equipment", AR Consolidated Statement of Cash Flows, AR p.231) is available
  only for FY25 (265.16 cr) and FY26 (342.55 cr); FY23/FY24 capex NOT FOUND (no
  prior AR, screener aggregates investing cash flow without a capex line).
  FY25 FCF = 26.14 - 265.16 = -239.02 cr (computed). FY26 FCF = -98.75 - 342.55 =
  -441.30 cr (computed). 0 of 2 computable years positive → **score 0**
- B3 Cumulative FCF ÷ Cumulative PAT (same 2-year window, FY25-FY26 only):
  cum. FCF = -680.32, cum. PAT = -215.60. Arithmetic ratio = 3.155, but BOTH
  numerator and denominator are negative (deep cash burn AND deep losses, not
  cash-backed earnings). Mechanically applying the band would misread this as a
  "5" (≥0.60); overridden to **score 0** with the actual negative figures shown,
  since the band assumes a profitable base the company does not have.
- B4 Change in WC Days, latest vs earliest available (FY26 vs FY25, the only
  2-year window with Trade Payables, AR p.227):
  - FY25: Receivable Days 61.83 + Inventory Days 161.18 - Payable Days 91.14 =
    131.87 days (computed; revenue basis, COGS not separately disclosed)
  - FY26: Receivable Days 78.49 + Inventory Days 168.58 - Payable Days 95.63 =
    151.44 days (computed)
  - Change = +19.6 days → **increased >15 → score 0**

**Block B = 0+0+0+0 = 0 / 20**

block_b_trend basis: CFO swung from +Rs 26.14 cr (FY25) to -Rs 98.75 cr (FY26)
(screener-data) while WC days rose +19.6 days (131.9→151.4) (AR p.227,231) —
**DETERIORATING**.

---

## BLOCK C: GROWTH (Max 20)

- C1 Revenue CAGR (FY23 812.13 cr → FY26 1,230.44 cr, screener-data, 3 years):
  (1230.44/812.13)^(1/3)-1 = 14.85% (computed) → **10-14.9% → score 3**
- C2 PAT CAGR: FY23 -98.83, FY26 -113.25 — both endpoints negative →
  **N/M (negative endpoint) → score 0**. Not a loss-to-profit swing (PAT never
  turned positive in any of FY23-26); losses widened then narrowed then widened
  again (FY23 -98.83 → FY24 -10.84 → FY25 -102.35 → FY26 -113.25, screener-data).
- C3 Positive YoY revenue years, 3 YoY comparisons available (FY24 vs FY23,
  FY25 vs FY24, FY26 vs FY25): FY24 +18.8% (screener-data), FY25 -4.2%
  (screener-data, decline), FY26 +33.1% (screener-data). 2 of 3 positive = 66.7%
  → **50-74% → score 1**
- C4 PAT CAGR minus Revenue CAGR: PAT CAGR is N/M → **score 0 per rule**

**Block C = 3+0+1+0 = 4 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

EBITDA (used in D1 only; not a screener-supplied field) = PBT + Interest +
Depreciation, screener-data, **computed**, includes Other Income. Basis chosen
because it reproduces the company/press-reported FY26 figure (Rs 154.5 cr, 13%
margin, per company memory sourcing) almost exactly: computed FY26 = Rs 160.56 cr,
margin 13.05%.
| Year | PBT | Interest | Depreciation | EBITDA (computed) | Margin |
|---|---|---|---|---|---|
| FY23 | -103.45 | 68.58 | 99.52 | 64.65 | 7.96% |
| FY24 | -4.28 | 69.16 | 107.69 | 172.57 | 17.88% |
| FY25 | -94.01 | 64.33 | 103.41 | 73.73 | 7.97% |
| FY26 | -71.49 | 94.36 | 137.69 | 160.56 | 13.05% |
(all screener-data inputs; EBITDA and margin computed)

- D1 Net Debt ÷ EBITDA (latest, FY26): Net debt = Rs 250.05 cr, the AR's own
  audited figure (Note 29, Capital management, AR p.282: "Net debt (Refer note
  15) 2,500.49" INR mn, cross-validated against the AR's own disclosed Net
  debt/equity ratio of 0.17 = 250.05/1,486.49). A cruder screener-only calc
  (Borrowings 700.93 cr − Cash&Bank 356.65 cr = Net debt 344.28 cr, screener-data)
  is noted for comparison but not used, since the AR figure is the company's own
  audited number. 250.05 ÷ 160.56 = 1.56x → **1-2x → score 3**
- D2 Interest Coverage, EBIT ÷ Interest (latest, FY26): EBIT = 22.87 cr (computed
  above) ÷ Interest 94.36 cr (screener-data) = 0.24x → **<1.5x → score 0**
- D3 Debt ÷ Equity (latest, FY26): Debt = Borrowings 700.93 cr (screener-data;
  reconciles exactly to AR Note 15 Borrowings 403.58 cr + Lease liabilities
  297.35 cr = 700.93 cr, AR p.227). Equity = Share Capital 670.67 + Reserves
  815.82 = 1,486.49 cr (screener-data; matches AR Total Equity 1,485.55 cr almost
  exactly). D/E = 0.4716 → **0.1-0.5 → score 4**. (Supplementary: AR's own
  Net-debt/equity is 0.17, AR p.282.)
- D4 Current Ratio (latest, FY26): Total Current Assets 1,303.03 cr ÷ Total
  Current Liabilities 822.65 cr (both AR p.227) = 1.58x → **1.5-1.99 → score 4**

**Block D = 3+0+4+4 = 11 / 20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding pattern, no prospectus, no promoter pledge disclosure anywhere in
this corpus (input_gaps: shareholding ABSENT).

- E1 Promoter holding (latest quarter): **N/A (not in provided data) → score 0**
- E2 Promoter holding change over 3 years: **N/A (not in provided data) → score 0**
- E3 Promoter pledge (latest): **N/A (not in provided data) → score 0**
- E4 Contingent Liabilities ÷ Net Worth (latest, FY26): Contingent liabilities =
  Labour matters Rs 69.00 mn + Tax matters Rs 80.58 mn = Rs 149.58 mn = Rs 14.96 cr
  (AR Note 30, p.282). Related-party corporate guarantees are referenced (AR Note
  30(x), Note 34) but not quantified in the extract reviewed; not included, flagged
  as a caveat. Net Worth = AR Total Equity attributable to owners, Rs 1,486.49 cr
  (AR p.227). Ratio = 14.96 ÷ 1,486.49 = 1.01% → **<5% → score 5**

**Block E = 0+0+0+5 = 5 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peers: AZAD (Azad Engineering), DYNAMATECH (Dynamatic Technologies), UNIMECH
(Unimech Aerospace) — peer Data_Sheets populated, FY26 latest year used for
cross-sectional tests. AZAD's FY26 "Other Mfr. Exp" and "Selling and admin" cells
are blank in its Data_Sheet (collector defect, likely folded into "Other
Expenses" 184.02 cr); this does not affect the PBT-based EBITDA calc used below
(PBT is a clean bottom-line figure, not assembled from those sub-lines).

| Test | Score | Basis |
|---|---|---|
| M1 Pricing Power | 5 | EBITDA margin FY23 7.96% → FY26 13.05% (computed, above), +5.09pp expansion (≥2pp); Revenue CAGR 14.85% (≥10%). Path non-monotonic (peaked 17.88% FY24, dipped 7.97% FY25); flagged, not a smooth climb. |
| M2 Cost Advantage vs peer median EBITDA margin | 0 | FY26 EBITDA margin (PBT+Interest+Depreciation basis, computed for all four): AEQUS 13.05%, AZAD 44.94%, DYNAMATECH 16.93%, UNIMECH 50.92% (all screener-data inputs). Peer median 44.94%. AEQUS is 31.9pp BELOW → score 0. Peer margins are inflated by large Other Income (UNIMECH Other Income Rs 46.07 cr on Sales Rs 240.49 cr = 19% of sales, likely IPO-cash treasury income, screener-data); an ex-Other-Income basis still shows AEQUS (7.46%) 24.3pp below the peer median (31.76%) — conclusion is robust to basis. |
| M3 Capital Efficiency | 0 | FAT FY26 = Sales 1,230.44 ÷ Net Block 1,070.19 (screener-data) = 1.15x. ROCE FY26 = 1.22% (computed, Block A). FAT>1x met, but ROCE>12% fails → score 0. |
| M4 Customer Stickiness | 3 | 1 decline year (FY25, -4.2%), fully recovered and exceeded by FY26 (+33.1%, screener-data) → max-1-decline-year-fully-recovered tier. |
| M5 Scale & Dominance | 1 | Mcap: AZAD 17,936 > AEQUS 16,242 > DYNAMATECH 7,915 > UNIMECH 7,649 cr (screener-data) — AEQUS #2 of 4 (top3/top5). Margin (FY26, incl-OI basis): UNIMECH 50.92% > AZAD 44.94% > DYNAMATECH 16.93% > AEQUS 13.05% — AEQUS is LAST, not top2 → only "top5 mcap" tier qualifies. |
| M6 Technology / R&D | 0 | AR: "Expenditure incurred on Research and Development - NIL" (AR p.?, Directors' Report technology-absorption section, grep-located, page marker not captured in extract). R&D/Revenue effectively 0%. |
| M7 Regulatory / License | 0 | Aerospace certification (AS9100/NADCAP/ITAR) is a customer-qualification barrier, not a government license/quota in the M7 sense; classified unregulated for this test. Even under a generous "regulated" reading, margin swings 7.96%→17.88%→7.97%→13.05% (computed) exceed the ±3pp/±5pp stability bands either way. |
| M8 Distribution | 0 | B2B contract manufacturer to OEMs (Airbus/Boeing/Safran) and consumer-goods OEM customers; no outlet/distribution-network model applies. |
| M9 Brand | 0 | GM proxy = (Sales − Raw Material Cost) ÷ Sales, screener-data, stated proxy. FY26: AEQUS 57.55%, AZAD 78.36%, DYNAMATECH 41.90%, UNIMECH 74.55%. Peer median 74.55%. AEQUS is 17.0pp BELOW → score 0. |
| M10 Switching Costs | 0 | Revenue grew all but 1 year (FY25 decline) — satisfies growth leg of the "3" tier, but Receivable Days rose +16.7 days over the only computable window (FY25→FY26, AR p.227) — fails the "stable" leg. Falls to "else" → 0. |
| M11 Network Effects | 0 | Only 4 of the required ≥6 years available; scored conservatively per rule. Revenue CAGR 14.85% (just under the 15%/20% thresholds in either qualifying tier); Selling & admin % of sales FY23 6.02% → FY24 5.31% → FY25 6.83% → FY26 6.72% (screener-data) — not clearly declining. |
| M12 Negative WC / Float | 0 | WC Days computable only FY25 (131.9) and FY26 (151.4, computed above) — both far exceed 45 days. |

**Moat score = 5+0+0+3+1+0+0+0+0+0+0+0 = 9 / 60**
Moats "present" (score ≥3): M1, M4 → **2 confirmed**

Moat profile:
```
M1  [#####]  5  PRESENT
M2  [     ]  0
M3  [     ]  0
M4  [###  ]  3  PRESENT
M5  [#    ]  1
M6  [     ]  0
M7  [     ]  0
M8  [     ]  0
M9  [     ]  0
M10 [     ]  0
M11 [     ]  0
M12 [     ]  0
```

**Moat classification: 2 confirmed → MODERATE**

---

## CLASSIFICATION

Core score = Block A(5) + B(0) + C(4) + D(11) + E(5) = **25 / 80**
Moat score = **9 / 60**
Grand total = **34 / 140**

Data confidence: 4 years of P&L/CF history → "3-4 LIMITED, downgrade
classification one tier" band applies (history_downgrade = true). Classification
matrix: Core <40 → **AVOID** outright (the one-tier downgrade has no further
effect since AVOID is already the floor of the matrix).

Deal-breaker overrides triggered (recorded; ceilings already below the raw AVOID
result so none change the outcome):
1. Block A < 8 (5) → max GOOD
2. Block B < 8 (0) → max GOOD
3. Median ROCE < 10% (-0.65%) → max AVERAGE
4. Cumulative CFO/PAT < 0.50 (0.25) → max AVERAGE
8. PAT negative in FY24, FY25, FY26 (all of the last 3 years) → max AVERAGE
Not triggered: #5 pledge (data ABSENT, not evaluable), #6 ND/EBITDA>3x AND IC<3x
(ND/EBITDA is 1.56x, does not exceed 3x), #7 revenue declined in majority of years
(1 of 3 YoY periods, not majority), #9 history <3 years (have 4).

**CLASSIFICATION: AVOID**

Strongest block: D (Balance Sheet Strength), 11/20 — moderate leverage (D/E
0.47x, Current Ratio 1.58x), undermined by weak interest cover (0.24x).
Weakest block: B (Cash Generation Quality), 0/20 — every sub-test scores zero;
CFO turned negative in FY26, FCF deeply negative both computable years, WC days
rising.

Decision line: Gate 0 is a mechanical screen; it does not halt the pipeline on
company quality (CLAUDE.md — flags propagate, only mechanical failures halt).
FLAG-GATE0 is raised below for the AVOID classification with named historical
depressors; the run proceeds through evidence stages 2-9 with this flag carried
forward to Halt 1.

---

## LOAD-BEARING FACTS CHECK (first verification priority)

1. GUIDANCE VS DELIVERY. The specific FY27 aerospace guidance quoted in company
   memory ("aerospace revenue +25-30%, segment EBITDA margin above 20%, ~20%
   manufacturing ROCE") is **NOT FOUND verbatim** in the AR or the Q1 FY27
   presentation text in this corpus (likely sourced from a news article outside
   the provided documents). What IS found: AR Chairman's letter states "Vision
   2031" (set out at an Investor Day in Jun-2026, after FY26 close): revenue
   growth 4-6x over the FY26 base, EBITDA margin 18-22%, steady-state ROCE ~20%
   by FY2030-31 (AR p.10) — a medium-term target, not a FY27 number. Actual FY26
   Aerospace segment result (=EBITDA per Note 36 definition) = Rs 281.27 cr on
   revenue Rs 1,046.38 cr = **26.9% margin** (AR p.292), up from 19.4% in FY25 —
   already above the ">20%" bar cited in memory. Q1 FY27 Aerospace segment ROCE =
   21.69% (Q1 FY26: 21.96%) (Inv. Pres. slide 12) — consistent with "~20%
   manufacturing ROCE."
2. CONSUMER DRAG AND CAPITAL ALLOCATION. Actual FY26 full-year Consumer segment
   result = Rs -78.27 cr on revenue Rs 184.06 cr = **-42.5% margin** (AR Note 36,
   p.292) — materially WORSE than the -24% H1FY26 figure carried in company
   memory. Quarterly prints corroborate the deterioration: Consumer EBITDA
   -Rs 74 mn (Q1FY26, margin -29.2%) to -Rs 361 mn (Q1FY27, margin -49.2%) (Inv.
   Pres. slide 11). The specific "~Rs 500 cr of ~Rs 660 cr FY27 capex to consumer"
   split cited in memory is **NOT FOUND** in the AR or Q1FY27 presentation text
   in this corpus. What is found: Consumer segment assets grew from Rs 870.16 cr
   (FY25) to Rs 1,286.86 cr (FY26), +47.9% in one year (AR p.293), on revenue of
   only Rs 184 cr — a capital-intensity mismatch consistent with the flagged
   capital-allocation concern even without the precise FY27 split figure.
3. CASH CONVERSION AND BALANCE SHEET. Confirmed: net loss FY25 Rs 102.35 cr
   (screener-data; AR Note 36 total FY25 PAT -102.42 cr, AR p.292, near-exact
   match). FY26 net loss widened to Rs 113.25 cr (screener-data). Consolidated
   debt (Borrowings incl. lease liabilities) Rs 700.93 cr FY26 (screener-data,
   reconciled to AR p.227). Interest Rs 94.36 cr FY26, interest coverage 0.24x
   (Block D2). OCF vs capex: OCF -Rs 98.75 cr FY26 vs capex Rs 342.55 cr FY26
   (AR p.231) — FCF -Rs 441.30 cr. Receivables Rs 264.61 cr FY26 (+69% YoY,
   screener-data), Inventory Rs 567.44 cr FY26 (AR p.227, +39% YoY) — both
   growing faster than the +33% revenue growth. WC days rose 131.9→151.4 days
   FY25→FY26 (computed, Block B4). This is the FLAG-CASH input (block_b_trend =
   DETERIORATING, above).
4. ORDER BOOK AND VISIBILITY. Confirmed: Q1 FY27 (Jun-2026) aerospace order book
   = USD 1,004 mn, +13% QoQ (Inv. Pres. slide 8). AR states an order book of
   USD 889 mn footnoted "as of June 2026" (AR p.44) — the two figures are
   consistent with the +13% QoQ growth claim if the AR's $889 mn actually
   reflects the Mar-2026 (FY26 year-end) position and the AR's own footnote date
   is an authoring artifact; flagged as a minor date-labelling inconsistency in
   the AR, not a numerical contradiction. The 15-year Safran A320 wheel agreement
   (deliveries from FY28) is confirmed at Inv. Pres. slide 8 ("first contract for
   fully assembled Airbus A320 wheels with Safran Landing Systems... manufactured
   end-to-end in India"). No Reg 30 announcement PDF is in this corpus to verify
   independently (input_gaps: announcements ABSENT).

---

## DATA QUALITY NOTES

- The AR p.14 "Key Financial Highlights" 3-year bar-chart page (Revenue,
  Net Debt/Equity, Fixed Asset Turnover, ROCE, EBITDA, PAT with FY24/FY25/FY26
  labels) was **NOT used as an anchor anywhere in this report**. Its text
  extraction interleaves values and year labels in an order that could not be
  reliably reconstructed: a cross-check of its Net Debt/Equity FY24 value
  (chart-implied 0.55x) against an independent computation from screener-data
  (Borrowings 1,106.05 − Cash 251.98, ÷ Net Worth 409.45 = 2.09x) failed by
  roughly 4x, showing the chart's label-to-value mapping is not trustworthy from
  text extraction alone (pdftoppm/poppler-utils is not installed in this
  environment, so the page could not be visually re-rendered to resolve it).
- AEQUS consolidated Inventory: screener-Data_Sheet shows Rs 609.65 cr (FY26) /
  Rs 451.21 cr (FY25); AR Note 11 shows Rs 567.44 cr (FY26) / Rs 408.27 cr (FY25)
  (AR p.252, cross-checked against AR p.227 balance sheet, internally
  consistent). A constant ~Rs 42-43 cr gap exists between the two sources for
  both years; cause not identified. Block B4 (WC Days) uses the AR figures
  throughout for internal consistency with AR-sourced Receivables and Payables
  (screener has no Payables line at all).
- Peer AZAD's FY26 Data_Sheet has blank "Other Mfr. Exp" and "Selling and admin"
  cells (collector defect); PBT-based calculations used here are unaffected.


## HANDOFF BLOCK (B01-gate0, as returned by the stage)

```yaml
stage: B01-gate0
company: "AEQUS"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - prospectus (ABSENT; HIGH gap; listed 10-Dec-2025, inside ~3y window)
  - results (ABSENT; no results filings; Gate 0 from screener Data_Sheet + AR; Q1 FY27 via presentation + concall only)
  - rating (ABSENT; no rating rationale)
  - announcements (ABSENT; no Reg 30 record)
  - shareholding (ABSENT; FII+DII UA qualifier unresolved; Block E1-E3 scored 0/NOT FOUND)
  - research (ABSENT)
  - other (ABSENT)
  - screening (collector v3 defect: Profit_Loss/Balance_Sheet/Cash_Flow/Quarters/Customization CSVs header-only for AEQUS and all 3 peers; Data_Sheet populated FY23-FY26 + 7 quarters to Jun-2026)
  - peer-concalls (DYNAMATECH single transcript Feb-2024, ~30 months stale)
  - manifest (no listed_date; sector_cap_row set by Step 1 brief to "Defence / strategic"; phase 3 confirms row)
  - prior-year ARs (FY24, FY25 ARs ABSENT; only the FY2025-26 AR's 2-year comparative balance sheet gives a current/non-current split, so ROCE A1/A2/A4, WC Days B4, and Capex/FCF B2/B3 are computable only for FY25-FY26, not the full FY23-FY26 window)
  - PDF page rendering (pdftoppm/poppler-utils not installed in this environment; AR p.14 "Key Financial Highlights" 3-year chart could not be visually verified and was excluded as an anchor after a Net Debt/Equity FY24 cross-check failed by ~4x on text extraction alone)
freshness_verdict: FRESHNESS PAIRS OK
flags:
  - type: FLAG-GATE0
    reason: >
      Classification AVOID (core 25/80, moat 9/60). Historical depressors:
      PAT negative FY23-FY26 (4 consecutive years); cumulative CFO/PAT 0.25x;
      FY26 FCF -Rs441.30cr, FY25 FCF -Rs239.02cr (both computable years
      negative); WC days rose +19.6 days FY25-FY26; interest coverage 0.24x
      FY26; Consumer segment FY26 full-year margin -42.5% (AR Note 36),
      worse than the -24% H1FY26 figure in company memory.
data_years: 4
fy_range: "FY23 to FY26"
blocks: {A: 5, B: 0, C: 4, D: 11, E: 5}
core_score: 25
moat_score: 9
grand_total: 34
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "1: Block A <8 (5) -> max GOOD"
  - "2: Block B <8 (0) -> max GOOD"
  - "3: median ROCE <10% (-0.65%) -> max AVERAGE"
  - "4: cumulative CFO/PAT <0.50 (0.25) -> max AVERAGE"
  - "8: PAT negative in FY24, FY25, FY26 (all of last 3 years) -> max AVERAGE"
history_downgrade: true
data_notes:
  - "ROCE (A1/A2/A4) and WC Days (B4) computable only for FY25-FY26 (2 of 4 years); FY23/FY24 balance sheet lacks current/non-current split and Trade Payables in any corpus source"
  - "Capex/FCF (B2/B3) computable only for FY25-FY26 (AR Consolidated Cash Flow Statement, AR p.231, gives one comparative year only; no prior AR in corpus)"
  - "B3 cumulative FCF/PAT arithmetic ratio (3.155) overridden to score 0: both cumulative FCF (-680.32cr) and cumulative PAT (-215.60cr) are negative, not cash-backed earnings"
  - "WC Days (B4) computed on AR-sourced Receivables/Inventory/Payables (AR p.227, p.252) for internal consistency, not screener-Data_Sheet Inventory, which differs from AR by a constant ~Rs42-43cr in both FY25 and FY26 for reasons not identified"
  - "EBITDA (Block D1, M1, M2) computed as PBT+Interest+Depreciation (screener-data), includes Other Income; basis chosen because FY26 computed value (Rs160.56cr, 13.05% margin) reproduces the company/press-reported FY26 figure (Rs154.5cr, 13% margin per company memory sourcing) almost exactly"
  - "D1 Net Debt uses the AR's own audited figure (Rs250.05cr FY26, Note 29 Capital management, AR p.282, cross-validated against AR's own 0.17x Net debt/equity ratio), not the cruder screener Borrowings-minus-Cash calc (Rs344.28cr)"
  - "M9 Brand and M2 Cost Advantage use GM/EBITDA-margin proxies stated explicitly (GM = (Sales-Raw Material Cost)/Sales; EBITDA = PBT+Interest+Depreciation); both computed identically for AEQUS and all 3 peers (AZAD, DYNAMATECH, UNIMECH) from their screener-Data_Sheets"
  - "No loss-to-profit swing: PAT negative in all of FY23-FY26 (screener-data); C2/C4 scored 0 as N/M per rule, not a swing"
  - "FY27 aerospace-specific guidance (+25-30% revenue, >20% segment EBITDA margin, ~20% manufacturing ROCE) cited in company memory NOT FOUND verbatim in AR or Q1FY27 presentation; only AR's medium-term 'Vision 2031' target (4-6x revenue by FY30-31, 18-22% EBITDA margin, ~20% steady-state ROCE) is confirmed in corpus (AR p.10)"
  - "FY27 capex plan (~Rs660cr, ~Rs500cr to Consumer) cited in company memory NOT FOUND in AR or Q1FY27 presentation text in this corpus"
  - "AR p.14 'Key Financial Highlights' 3-year chart NOT used as an anchor anywhere; text-extraction order could not be reliably mapped to FY24/FY25/FY26 (Net Debt/Equity FY24 cross-check: chart-implied 0.55x vs independently computed 2.09x, ~4x off)"
  - "PEER DATA NEEDED: none — peer Data_Sheets (AZAD, DYNAMATECH, UNIMECH) were available and used for all tests requiring peer comparison (M2, M5, M9)"
block_b_trend: "deteriorating -- CFO swung from +Rs26.14cr (FY25, screener-data) to -Rs98.75cr (FY26, screener-data) while WC days rose +19.6 days (131.9->151.4, computed from AR p.227,231)"
analyst_note: >
  AVOID is driven almost entirely by Blocks A/B (returns, cash), not by the
  aerospace story. Aerospace segment margin (26.9% FY26, AR Note 36) and Q1FY27
  segment ROCE (21.7%, Inv Pres slide 12) already clear the bar company memory
  flagged for verification. The drag is Consumer: full-year FY26 segment margin
  (-42.5%) is materially worse than the -24% H1FY26 figure carried into this
  run, and Consumer segment assets grew 48% in one year against Rs184cr of
  revenue, a capital-intensity mismatch. Group cash conversion is the real
  deal-breaker: CFO turned negative FY26, FCF deeply negative both computable
  years, WC days rising, interest coverage 0.24x. ROCE/WC-days scoring is
  structurally limited to a 2-year window (FY25-FY26) because the sole AR in
  corpus gives the current/non-current balance-sheet split for only those two
  years; FY23/FY24 equivalents are NOT FOUND, not estimated. The AR's own p.14
  highlight chart was excluded as an anchor after a Net Debt/Equity cross-check
  failed by ~4x on text extraction alone (poppler-utils unavailable to
  visually re-render).
```
