# STAGE 1: GATE 0 SCORECARD — Tatva Chintan Pharma Chem Ltd (TATVA)
Run date: 2026-07-12 | Model: claude-sonnet-5 | Pipeline mode
TARGETED RE-RUN: Block E (Shareholder Alignment) recomputed from the FY2024-25
Annual Report (statutory/board's report + corporate governance report + financial
statement notes), which was not available to the prior run. Blocks A, B, C, D and
F are reused unchanged from the validated prior scorecard (screener-Data_Sheet.csv
cross-checked against the Q4/FY26 and Q3/9M-FY26 results PDFs) — no errors found
in them on review, so they are not recomputed.

Data available: 9 years (FY2018 to FY2026) for Blocks A-D, F. Block E uses the
single latest data point disclosed in the FY2024-25 Annual Report (year-end
31 March 2025), as explained per-metric below.

Primary source, Blocks A-D & F: screener-Data_Sheet.csv (consolidated basis —
cross-validated against Q4/FY26 and Q3/9M-FY26 results PDFs, figures match to the
cent). screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Cash_Flow.csv,
screener-Quarters.csv and screener-Customization.csv were exported EMPTY (headers
only, no data rows).

Primary source, Block E: Tatva Chintan Pharma Chem Ltd Annual Report FY2024-25
(file Annual_Report_2022.pdf — filename is a legacy artifact; the document content
is confirmed FY2024-25 per its cover letter dated 26 August 2025 and "2024-25"
cover branding), specifically:
 - Annexure-I to the Corporate Governance Report, "Category of Shareholding as on
   31 March 2025" (AR p.85)
 - Note 45 "Capital management" and Note 46 "Contingent liabilities and
   commitments", Notes forming part of the Consolidated Financial Statements
   (AR p.275-276)

Peers for Block F: ACUTAAS (Acutaas Chemicals), CAMLINFINE (Camlin Fine Sciences),
CLEAN (Clean Science & Technology), NEOGEN (Neogen Chemicals) — all via their own
screener-Data_Sheet.csv exports (their Profit_Loss.csv files were also empty).

---
## METHODOLOGY NOTES (read before the numbers)

1. **ROCE/ROE**: screener-Balance_Sheet.csv has "Return on Equity" / "Return on
   Capital Emp" as row labels but NO data was exported under them (empty file).
   Both are therefore COMPUTED here, per the stage formula. EBIT = PBT + Interest.
   Capital Employed = Net Worth + Total Borrowings (screener Data_Sheet does not
   split Current vs Non-Current liabilities for FY18-FY24; the FY25/FY26 results
   PDF balance sheets show non-current liabilities are a small residual — ₹13.98mn
   FY25, ₹88.00mn FY26, consolidated — confirming "Other Liabilities" in Data_Sheet
   is overwhelmingly current. Net Worth + Borrowings is used as a consistent
   long-term-capital proxy across all 9 years). Stated as "computed" throughout.
2. **Capex / FCF**: screener-Data_Sheet.csv gives only an aggregate "Cash from
   Investing Activity" line, not a clean purchase-of-PPE line, for FY18-FY24 (using
   the aggregate would overstate capex in years with large investment
   purchases, e.g. FY22 post-listing cash deployment). Capex is instead computed
   indirectly: Δ(Net Block + CWIP) + Depreciation. This was cross-checked against
   the actual capex line disclosed in the results PDFs for FY25 (₹762.72mn actual
   vs ₹772.1mn indirect, ~1.2% diff) and FY26 (₹1,137.74mn actual vs ₹1,181.9mn
   indirect, ~3.9% diff) — both within a small margin, so the indirect method is
   used for all years FY19-FY26 (FY18 capex not computable, no FY17 opening base).
3. **Payables / WC Days**: screener-Data_Sheet.csv has NO Trade Payables line at
   all (Balance Sheet only carries Receivables and Inventory). Payable Days —
   and therefore full Working Capital Days — are computable ONLY for FY25 and
   FY26, using Trade Payables disclosed in the results PDF balance sheets.
   Receivable Days and Inventory Days are computed on a revenue basis (no
   separate COGS line is provided).
4. **Block E (Shareholder Alignment) — RESOLVED THIS RUN from the FY2024-25 AR**:
   E1 (promoter holding) and E4 (contingent liabilities / net worth) are directly
   disclosed in the AR and are scored on that basis. E2 (3-year promoter holding
   change) and E3 (promoter pledge) remain genuinely absent even from the AR — the
   AR's shareholding annexure is a single year-end snapshot with no pledge column
   and no prior-year comparative promoter %; that data lives only in the quarterly
   BSE/NSE shareholding-pattern (SHP) filings, which were not provided. E2 and E3
   are marked N/A (not in document) and scored 0, per the "never estimate" rule —
   this is a narrower, more specific gap than the prior run's full Block E gap.
5. Sector cap row auto-picked as "Pharma / CDMO" for D1/D2 bank-override checks
   — flagged for verification; Tatva is specialty/performance chemicals, not
   pharma/CDMO. (Not applicable here since Tatva is not a bank/NBFC, so the
   override branch was not used regardless.)
6. This is a targeted re-run of an existing Gate 0 scorecard for this ticker
   (same run folder, same date) to fill the Block E gap from the AR per the
   pipeline degradation map. No company memory file exists yet for this ticker.

---
## BLOCK A: RETURN ON CAPITAL (Max 20) — unchanged from prior run

Per-year table (₹ cr, consolidated):

| FY | PBT | Interest | EBIT=PBT+Int | Net Worth | Borrowings | Cap. Employed | ROCE (computed) | PAT | Avg Net Worth | ROE (computed) |
|----|-----|----------|--------------|-----------|------------|---------------|------------------|-----|----------------|-----------------|
| 2018 | 19.04 | 2.63 | 21.67 | 59.12 | 56.15 | 115.27 | 18.80% | 12.29 | 59.12 (closing only, no FY17 opening) | 20.79% |
| 2019 | 27.39 | 3.95 | 31.34 | 79.71 | 77.15 | 156.86 | 19.98% | 20.54 | 69.42 | 29.59% |
| 2020 | 47.60 | 4.27 | 51.87 | 117.70 | 90.69 | 208.39 | 24.89% | 37.79 | 98.71 | 38.29% |
| 2021 | 60.70 | 4.45 | 65.15 | 165.97 | 90.25 | 256.22 | 25.43% | 52.26 | 141.84 | 36.84% |
| 2022 | 104.12 | 5.11 | 109.23 | 473.09 | 119.94 | 593.03 | 18.42% | 95.87 | 319.53 | 30.00% |
| 2023 | 44.77 | 8.60 | 53.37 | 514.80 | 170.26 | 685.06 | 7.79% | 45.49 | 493.95 | 9.21% |
| 2024 | 43.56 | 6.73 | 50.29 | 737.08 | 14.27 | 751.35 | 6.69% | 30.35 | 625.94 | 4.85% |
| 2025 | 7.58 | 1.51 | 9.09 | 738.82 | 36.39 | 775.21 | 1.17% | 5.71 | 737.95 | 0.77% |
| 2026 | 57.01 | 2.85 | 59.86 | 781.76 | 120.37 | 902.13 | 6.64% | 42.05 | 760.29 | 5.53% |

(All raw inputs: screener-Data_Sheet.csv; FY26 cross-anchored to results Q4 FY26
p.8 consolidated P&L (PBT 570.09mn, Interest 28.51mn) and p.9 consolidated B/S
(Total equity 7,817.59mn, Total borrowings 1,203.73mn).)

- **A1 Median ROCE**: sorted {1.17, 6.64, 6.69, 7.79, 18.42, 18.80, 19.98, 24.89,
  25.43} → median = **18.42%** (FY2022, screener-Data_Sheet, computed) → band
  15-19.9% → **score 3**
- **A2 Minimum single-year ROCE**: **1.17%** (FY2025, computed) → band <8% →
  **score 0**
- **A3 Median ROE**: sorted {0.77, 4.85, 5.53, 9.21, 20.79, 29.59, 30.00, 36.84,
  38.29} → median = **20.79%** (FY2018, closing-net-worth-only basis stated,
  computed) → band ≥20% → **score 5**
- **A4 ROCE trend, latest (FY2026=6.64%) vs earliest (FY2018=18.80%)**: decline
  of **12.16pp** → band decline >5pp → **score 0**

**Block A total = 3+0+5+0 = 8 / 20**

---
## BLOCK B: CASH GENERATION QUALITY (Max 20) — unchanged from prior run

CFO and PAT, ₹ cr (screener-Data_Sheet.csv, cross-anchored FY26 to results Q4
FY26 p.10 consolidated CF: CFO 314.89mn — the screener figure of 31.49cr matches
both the standalone CFO 314.89mn/10=31.49cr (p.18 standalone CF) and the
consolidated CFO on p.10, confirming consistency):

| FY | CFO | PAT | Capex (indirect, computed) | FCF=CFO−Capex |
|----|-----|-----|------------------------------|-----------------|
| 2018 | 12.59 | 12.29 | N/A (no FY17 base) | N/A |
| 2019 | 7.36 | 20.54 | 9.79 | −2.43 |
| 2020 | 25.31 | 37.79 | 48.11 | −22.80 |
| 2021 | 19.69 | 52.26 | 20.92 | −1.23 |
| 2022 | 20.38 | 95.87 | 89.02 | −68.64 |
| 2023 | 27.78 | 45.49 | 225.45 | −197.67 |
| 2024 | 98.04 | 30.35 | 102.05 | −4.01 |
| 2025 | 24.67 | 5.71 | 77.21 (actual per results 9M/Q4 FY26: 76.27) | −52.54 |
| 2026 | 31.49 | 42.05 | 118.19 (actual per results Q4 FY26 p.10: 113.77) | −86.70 |

- **B1 Cumulative CFO ÷ Cumulative PAT**: ΣCFO (9 yrs) = 267.31, ΣPAT (9 yrs) =
  342.35 → **0.781** → band 0.70-0.84 → **score 2**
- **B2 FCF-positive years proportion**: 0 of 8 computable years (FY19-FY26) were
  FCF-positive → **0%** → band <50% → **score 0**
- **B3 Cumulative FCF ÷ Cumulative PAT** (FY19-FY26 window, matching FCF
  availability): ΣFCF = −436.02, ΣPAT (same window) = 330.06 → **−1.32** →
  band <0.20 or negative → **score 0**
- **B4 Change in WC Days, latest vs earliest**: NOT COMPUTABLE per the strict
  formula — Trade Payables are not disclosed anywhere in the data for FY2018
  (earliest year). Partial window available: FY2025 WC Days = 175.33 (Rec.
  Days 78.72 + Inv. Days 127.79 − Pay. Days 31.18, using results 9M/Q4 FY26
  trade payables) vs FY2026 WC Days = 185.31 (85.90 + 141.44 − 42.03) = **+9.98
  days increase**, deteriorating, over the one window that can be measured.
  Marked N/A (not in provided data) for the required latest-vs-earliest
  comparison → **score 0**

**Block B total = 2+0+0+0 = 2 / 20**

**block_b_trend: deteriorating** — cumulative FCF has been negative every
single computable year (8 of 8, FY19-FY26), and the one WC-days window that
can be measured (FY25→FY26) shows working capital days rising by +9.98 days.

---
## BLOCK C: GROWTH (Max 20) — unchanged from prior run

Revenue and PAT, ₹ cr (screener-Data_Sheet.csv):

| FY | Revenue | YoY | PAT |
|----|---------|-----|-----|
| 2018 | 135.81 | — | 12.29 |
| 2019 | 206.31 | +51.9% | 20.54 |
| 2020 | 263.24 | +27.6% | 37.79 |
| 2021 | 300.36 | +14.1% | 52.26 |
| 2022 | 433.65 | +44.4% | 95.87 |
| 2023 | 423.61 | −2.3% | 45.49 |
| 2024 | 393.50 | −7.1% | 30.35 |
| 2025 | 382.71 | −2.7% | 5.71 |
| 2026 | 505.86 | +32.2% | 42.05 |

No loss-to-profit swing (PAT positive in every year, though FY2025 PAT of
5.71 cr was a low point).

- **C1 Revenue CAGR** (FY2018→FY2026, 8 yrs): (505.86/135.81)^(1/8)−1 =
  **17.87%**, computed → band 15-19.9% → **score 4**
- **C2 PAT CAGR** (FY2018→FY2026, 8 yrs): (42.05/12.29)^(1/8)−1 = **16.62%**,
  computed → band 15-19.9% → **score 4**
- **C3 Positive YoY revenue years**: 5 of 8 comparisons (FY19,20,21,22,26)
  positive; 3 (FY23,24,25) negative → **62.5%** → band 50-74% → **score 1**
- **C4 PAT CAGR minus Revenue CAGR**: 16.62% − 17.87% = **−1.25pp** → band
  ±3pp → **score 3**

**Block C total = 4+4+1+3 = 12 / 20**

---
## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY2026) — unchanged from prior run

- Net Debt = Borrowings 120.37 − Cash & Bank 8.79 = 111.58 cr (screener-Data_Sheet,
  cross-anchored results Q4 FY26 p.9: consol borrowings 1,203.73mn, cash+bank
  balances 57.64+30.27=87.91mn ≈ 8.79cr per Data_Sheet rounding)
- EBITDA FY2026 = PBT 57.01 + Dep 36.85 + Interest 2.85 − Other Income 3.55 =
  **93.16 cr**, computed (cross-anchored results Q4 FY26 p.8)

- **D1 Net Debt ÷ EBITDA**: 111.58/93.16 = **1.20x** → band 1-2x → **score 3**
- **D2 Interest Coverage (EBIT÷Interest)**: EBIT = PBT+Interest = 59.86;
  59.86/2.85 = **21.0x** → band ≥10x → **score 5**
- **D3 Debt ÷ Equity**: Borrowings 120.37 / Net Worth 781.76 = **0.154** →
  band 0.1-0.5 → **score 4**
- **D4 Current Ratio**: Total current assets 3,495.12mn / Total current
  liabilities 2,131.35mn (results Q4 FY26 p.9, consolidated) = **1.64** → band
  1.5-1.99 → **score 4**

**Block D total = 3+5+4+4 = 16 / 20**

---
## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — RECOMPUTED THIS RUN FROM FY2024-25 AR

- **E1 Promoter holding (latest quarter)**: **72.02%** — Promoter and Promoter
  Group held 16,846,958 shares out of 23,392,055 total shares as on 31 March
  2025 (AR, Annexure-I to Corporate Governance Report, "Category of Shareholding
  as on 31 March 2025", p.85). Band ≥60% → **score 5**
- **E2 Promoter holding change, 3 years**: **N/A (not in document)**. The AR
  discloses only the single year-end snapshot above (31 March 2025); it contains
  no prior-year comparative promoter % and no multi-year shareholding-pattern
  table. This data point exists only in the quarterly BSE/NSE shareholding-
  pattern (SHP) filings across the relevant quarters, none of which were
  provided. Genuinely absent even from the AR → **score 0**
- **E3 Promoter pledge (latest)**: **N/A (not in document)**. No pledge or
  encumbrance disclosure appears anywhere in the AR — the Annexure-I
  shareholding table (p.85) has no pledge column, and no other section of the
  Board's Report or Corporate Governance Report (checked pp.50-91 in full,
  including "General Shareholders' Information" and "Other Disclosures")
  discloses promoter pledge/encumbrance status. This is the SEBI Reg. 31(1)(b)
  quarterly SHP disclosure, not an AR-native disclosure, and was not provided.
  Genuinely absent even from the AR → **score 0**
- **E4 Contingent liabilities ÷ Net Worth (latest)**: Contingent liabilities
  (claims against the Group not acknowledged as debts) = ₹52.35 million
  (Indirect tax matters ₹11.99mn + Direct tax matters ₹11.20mn + Outstanding
  letter of credit ₹29.16mn), per Note 46 "Contingent liabilities and
  commitments", Notes forming part of the Consolidated Financial Statements,
  year ended 31 March 2025 (AR p.276). Net worth (consolidated Total equity) =
  ₹7,388.24 million, per Note 45 "Capital management", Consolidated Financial
  Statements (AR p.275). Ratio = 52.35 / 7,388.24 = **0.71%** → band <5% →
  **score 5**. (Sensitivity check: even if capital/other commitments — ₹118.66mn
  estimated capital contracts + ₹0.64mn export obligation, which are commitments
  rather than contingent liabilities under the standard definition — are added
  in, Total = ₹171.65mn / ₹7,388.24mn = 2.32%, still <5%, same score either way.)

**Block E total = 5+0+0+5 = 10 / 20** — E1 and E4 resolved from the AR; E2 and
E3 remain a genuine, narrower input gap (quarterly SHP data, not AR-native).

---
## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — unchanged from prior run

Peer EBITDA margin and gross-margin proxy, FY2026, computed the same way as
Tatva (PBT+Dep+Int−OtherIncome)/Sales and (Sales−RawMaterialCost)/Sales, from
each peer's screener-Data_Sheet.csv:

| Company | FY26 Sales | FY26 OPM | FY26 GM proxy | FY26 Mcap (cr) |
|---|---|---|---|---|
| TATVA | 505.86 | 18.42% | 46.78% | 3,102.96 |
| ACUTAAS | 1,339.37 | 35.87% | 55.58% | 27,842.73 |
| CAMLINFINE | 1,723.31 | 6.20% | 47.09% | 2,469.02 |
| CLEAN | 956.55 | 37.12% | 62.40% | 8,184.29 |
| NEOGEN | 861.96 | 15.93% | 25.98% | 5,709.35 |

Peer median OPM = 25.90% | Peer median GM proxy = 51.34%

- **M1 Pricing Power**: OPM FY2018 17.06% → FY2026 18.42%, change +1.36pp
  (stable ±2pp); Revenue CAGR 17.87% (≥10%) → **score 3** (PRESENT)
- **M2 Cost Advantage vs peer median EBITDA margin**: Tatva 18.42% vs peer
  median 25.90% → Tatva is **7.48pp below** → band "below" → **score 0**
- **M3 Capital Efficiency**: FAT (Sales/Net Block, FY2026) = 505.86/610.97 =
  **0.83x** (< 1x threshold), ROCE 6.64% → **score 0**
- **M4 Customer Stickiness**: 3 revenue-decline years (FY23,24,25) → band "3+
  decline years" → **score 0**
- **M5 Scale & Dominance**: Tatva ranks 4th of 5 by mcap (ACUTAAS 27,843 >
  CLEAN 8,184 > NEOGEN 5,709 > TATVA 3,103 > CAMLINFINE 2,469); by FY26 OPM,
  Tatva ranks 3rd of 5 (CLEAN 37.1% > ACUTAAS 35.9% > TATVA 18.4% > NEOGEN
  15.9% > CAMLINFINE 6.2%) — not largest mcap, not top-3 mcap, but is top-5 →
  **score 1** (peer set limited to the 4 provided peers + Tatva; wider
  segment universe not in provided data)
- **M6 Technology / R&D**: N/A (not in provided data) — no R&D expense line
  item anywhere in Tatva's P&L data → **score 0**
- **M7 Regulatory / License**: no evidence in provided data of a licensed/
  restricted-player regulatory segment (specialty/performance chemicals, not
  a regulated-license business per available information) → **score 0**
- **M8 Distribution**: N/A (not in provided data) — no distribution reach,
  network or outlet data provided → **score 0**
- **M9 Brand**: GM proxy 46.78% vs peer median 51.34% → Tatva **4.56pp
  below** peer median → band "at/below" → **score 0**
- **M10 Switching Costs**: overall revenue growth FY18→FY26, but 3 decline
  years (2+) → band "overall growth, 2+ decline years" → **score 1**
- **M11 Network Effects** (9 years available, ≥6-year test applies):
  latest 3yr CAGR (FY23→FY26) = 6.10% vs prior 3yr CAGR (FY20→FY23) = 17.19%
  — latest is LOWER than prior (decelerating), fails the "accelerating"
  condition; overall CAGR 17.87% is <20%, fails that band too; selling
  expense % of revenue is roughly flat FY18 (11.89%) to FY25 (11.22%, last
  year with a discrete Selling & Admin line — FY26 line is folded into
  "Other Expenses" in screener-Data_Sheet and not separately available) →
  **score 0**
- **M12 Negative WC / Float**: WC Days computable only for FY2025 (175.33)
  and FY2026 (185.31), both far above the 45-day threshold (payables data
  unavailable FY18-FY24) → **score 0**

Moat profile:
```
M1  Pricing Power        [███░░] 3/5  PRESENT
M2  Cost Advantage        [░░░░░] 0/5
M3  Capital Efficiency    [░░░░░] 0/5
M4  Customer Stickiness   [░░░░░] 0/5
M5  Scale & Dominance     [█░░░░] 1/5
M6  Technology / R&D      [░░░░░] 0/5
M7  Regulatory / License  [░░░░░] 0/5
M8  Distribution          [░░░░░] 0/5
M9  Brand                 [░░░░░] 0/5
M10 Switching Costs       [█░░░░] 1/5
M11 Network Effects       [░░░░░] 0/5
M12 Negative WC / Float   [░░░░░] 0/5
```

**Block F (moat) total = 3+0+0+0+1+0+0+0+0+1+0+0 = 5 / 60**

Moats present (score ≥3): M1 only → **moats_confirmed = 1**
Moat classification: 1 present → **THIN**

---
## CLASSIFICATION

Data confidence: 9 years (Blocks A-D, F) → 7-9 band → **moderate**. No history
downgrade (9 years is not in the 3-4 LIMITED band).

**Core score = A(8) + B(2) + C(12) + D(16) + E(10) = 48 / 100** (up from 38/100
in the prior run, entirely from Block E rising 0→10 on AR-sourced E1 and E4)
**Moat score = 5 / 60**
**Grand total = 53** (up from 43)

Classification matrix: Core 40-59 → **AVERAGE**

Deal-breaker check:
1. Block A <8 → NOT triggered (Block A = 8, boundary, not <8)
2. Block B <8 → **TRIGGERED** (Block B = 2) → caps at max GOOD (non-binding here:
   the matrix result AVERAGE is already below the GOOD cap)
3. Median ROCE <10% → NOT triggered (18.42%)
4. Cumulative CFO/PAT <0.50 → NOT triggered (0.781)
5. Pledge >15% → **STILL NOT ASSESSABLE** — promoter pledge is not disclosed
   anywhere in the FY2024-25 AR either (checked the full Corporate Governance
   Report and Board's Report); this is a genuine residual gap, narrower than
   before but not resolved. Cannot confirm or rule out.
6. ND/EBITDA >3x AND IC <3x → NOT triggered (1.20x / 21.0x)
7. Revenue declined in majority of years → NOT triggered (3 of 8 = 37.5%)
8. PAT negative in any of last 3 years → NOT triggered (FY24/25/26 all
   positive)
9. History <3 years → NOT triggered (9 years)

The Core 40-59 matrix result (AVERAGE) is the governing classification; the
Block-B deal-breaker cap (max GOOD) is not more restrictive than AVERAGE, so
it does not change the outcome. Deal-breaker 5 remains unresolved as a genuine
data gap, distinct from and narrower than the prior run's full Block E gap.

**Classification: AVERAGE**

**Note on this re-run**: Filling Block E from the FY2024-25 Annual Report (per
the pipeline degradation map) raised the classification from AVOID (grand
total 43, core 38) to AVERAGE (grand total 53, core 48) — a one-tier move, not
the multi-tier jump a full resolution of Block E might have suggested, because
two of the four Block E metrics (E2 promoter holding change, E3 promoter
pledge) are quarterly-SHP-filing data that is genuinely absent even from the
AR and remains an open input gap. The classification is no longer being held
down by a fillable data gap on E1/E4; it is now driven by (a) the remaining
E2/E3 gap (narrower, specifically named) and (b) a genuine, AR-independent
cash-generation weakness in Block B (2/20): FCF negative in all 8 computable
years (FY19-FY26), cumulative FCF/PAT −1.32, against a FY22-FY26 capex cycle
(Dahej SEZ expansion) that has depressed ROCE from ~19-25% (FY18-FY21) to
single digits (FY23-FY26, min 1.17% in FY25).

---
## STRONGEST / WEAKEST BLOCK

- **Strongest**: Block D, Balance Sheet Strength (16/20) — low leverage
  (D/E 0.15x), strong interest coverage (21.0x), manageable net debt (1.2x
  EBITDA).
- **Weakest**: Block B, Cash Generation Quality (2/20) — genuine weakness:
  FCF negative in all 8 computable years, cumulative FCF/PAT of −1.32, driven
  by a capex cycle that has outpaced operating cash generation. (Block E, at
  10/20, is no longer the weakest block now that E1 and E4 are AR-sourced; its
  remaining E2/E3 gap is a narrower, specifically named residual.)

---
## DECISION LINE

Gate 0 mechanical score: AVERAGE (core 48/100, moat THIN 5/60, grand total 53),
up one tier from the prior AVOID once Block E's promoter-holding (E1) and
contingent-liability (E4) metrics were sourced from the FY2024-25 Annual
Report. Two distinct drivers remain: (1) a genuine cash-quality problem — FCF
has been negative every year since FY2019 against a capex programme running
well ahead of CFO, and ROCE has fallen from ~19-25% in FY2018-FY2021 to single
digits in FY2023-FY2026; (2) a narrower residual data-availability problem —
promoter holding change (E2) and promoter pledge (E3) are not disclosed
anywhere in the AR and remain unscored pending the quarterly BSE/NSE
shareholding-pattern filings. Flags propagate per NEVER rule; no STOP verdict
is issued here — downstream stages carry both the mechanical AVERAGE and the
specific residual input gap forward for human review.

---
```yaml
stage: B01-gate0
company: "TATVA"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps:
  - "no rating PDF provided"
  - "sector_cap_row 'Pharma / CDMO' auto-picked for D1/D2 bank-override check and flagged for verification; Tatva is specialty/performance chemicals, not pharma/CDMO (override branch not triggered since Tatva is not a bank/NBFC)"
  - "promoter holding change over 3 years (E2) not present anywhere in the FY2024-25 Annual Report -- AR discloses only the single 31 March 2025 shareholding snapshot (Annexure-I to Corporate Governance Report, p.85), with no prior-year comparative promoter % and no multi-year shareholding table; this requires the quarterly BSE/NSE shareholding-pattern (SHP) filings across the relevant quarters, none of which were provided -- E2 N/A, scored 0"
  - "promoter pledge / encumbrance (E3) not present anywhere in the FY2024-25 Annual Report -- checked the full Corporate Governance Report (pp.50-91) including the Annexure-I shareholding table and General Shareholders' Information / Other Disclosures sections; no pledge column or pledge disclosure found. This is a SEBI Reg. 31(1)(b) quarterly SHP disclosure, not an AR-native disclosure -- E3 N/A, scored 0; deal-breaker 5 (pledge >15%) remains NOT ASSESSABLE"
  - "Trade Payables not disclosed anywhere for FY2018-FY2024 (screener-Data_Sheet.csv Balance Sheet section has no Payables line); Payable Days / full WC Days only computable for FY2025-FY2026 using results PDF balance sheets -- B4 not computable per strict latest-vs-earliest formula, scored 0"
  - "R&D expense not disclosed in provided data (no R&D line item in P&L) -- M6 scored 0"
  - "screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv and screener-Customization.csv (subject and all four peers) exported empty; screener-Data_Sheet.csv used as sole screener source, cross-validated against results PDFs"
  - "targeted re-run of an existing Gate 0 scorecard for this ticker (same run folder/date) to fill Block E from the FY2024-25 Annual Report per the pipeline degradation map; no company memory file exists yet"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE (core 48/100), up one tier from the prior run's AVOID (core 38/100) once Block E's E1 (promoter holding, 72.02%, AR p.85) and E4 (contingent liabilities/net worth, 0.71%, AR p.275-276) were sourced from the FY2024-25 Annual Report. Two remaining drivers: (a) Block E's E2 (3-year promoter holding change) and E3 (promoter pledge) are genuinely absent even from the AR -- quarterly BSE/NSE shareholding-pattern data not provided -- deal-breaker 5 (pledge >15%) stays NOT ASSESSABLE; (b) a genuine Block B weakness (2/20): FCF negative in all 8 computable years (FY19-FY26), cumulative FCF/PAT -1.32, against a FY22-FY26 capex cycle (Dahej SEZ expansion) that has depressed ROCE from ~19-25% (FY18-FY21) to single digits (FY23-FY26, min 1.17% in FY25). Recommend sourcing quarterly SHP filings (E2/E3) before treating AVERAGE as final."
data_years: 9
fy_range: "FY2018 to FY2026"
blocks: {A: 8, B: 2, C: 12, D: 16, E: 10}
core_score: 48
moat_score: 5
grand_total: 53
moats_confirmed: 1
moat_class: "THIN"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 (Block B = 2) -> caps at max GOOD; non-binding, matrix result Core 40-59 -> AVERAGE is already below the GOOD cap"
  - "Deal-breaker 5 (pledge >15%) STILL NOT ASSESSABLE -- promoter pledge not disclosed anywhere in the FY2024-25 Annual Report either; requires quarterly BSE/NSE shareholding-pattern filings"
history_downgrade: false
data_notes:
  - "No loss-to-profit PAT swing across FY2018-FY2026 (PAT positive every year, low of 5.71cr in FY2025)"
  - "Capex computed indirectly as Delta(Net Block+CWIP)+Depreciation for FY19-FY26 (screener Data_Sheet lacks a purchase-of-PPE cash flow line); cross-validated against results-PDF actual capex for FY25 (762.72mn actual vs 772.1mn indirect, ~1.2% diff) and FY26 (1,137.74mn actual vs 1,181.9mn indirect, ~3.9% diff)"
  - "GM proxy used per M9 formula: (Revenue - Raw Material Cost) / Revenue, for Tatva and all four peers"
  - "Receivable Days and Inventory Days computed on revenue basis (no separate COGS line disclosed); Payable Days computed on revenue basis using results-PDF trade payables, available only FY2025-FY2026"
  - "M5 Scale & Dominance peer set limited to the 4 provided peers (ACUTAAS, CAMLINFINE, CLEAN, NEOGEN) plus Tatva; wider specialty-chemicals listed universe not in provided data"
  - "Capital Employed for ROCE computed as Net Worth + Total Borrowings for all 9 years (screener Data_Sheet does not split current/non-current liabilities FY18-FY24; FY25/FY26 results-PDF balance sheets confirm non-current liabilities are a small residual, supporting this as a consistent proxy)"
  - "PEER DATA NEEDED: none -- ACUTAAS, CAMLINFINE, CLEAN, NEOGEN screener-Data_Sheet.csv exports provided sufficient data for M2, M5, M9; M6 gap is Tatva's own missing R&D line, not a peer-data gap"
  - "Block E sourced from the FY2024-25 Annual Report this run because the screener export omitted shareholding/pledge/contingent-liability data entirely -- E1 (promoter holding 72.02%, Annexure-I to Corporate Governance Report, AR p.85) and E4 (contingent liabilities Rs52.35mn / consolidated net worth Rs7,388.24mn = 0.71%, Notes 45-46 to Consolidated Financial Statements, AR p.275-276) resolved; E2 and E3 remain unresolved as they are not present even in the AR (quarterly SHP-filing data)"
  - "E4 contingent-liabilities figure uses Part A only (claims not acknowledged as debts: indirect tax 11.99mn + direct tax 11.20mn + outstanding LC 29.16mn = 52.35mn), excluding Part B capital/other commitments (118.66mn + 0.64mn), per the standard contingent-liability definition; including Part B would still give 171.65/7388.24 = 2.32%, same score band (<5%)"
block_b_trend: "deteriorating -- FCF negative in all 8 computable years (FY19-FY26, cumulative FCF/PAT -1.32); the one WC-days window that can be measured (FY2025 to FY2026, limited by missing payables data pre-FY2025) shows WC Days rising from 175.3 to 185.3, +9.98 days"
```
