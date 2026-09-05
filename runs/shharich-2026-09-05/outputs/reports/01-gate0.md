# STAGE 1: GATE 0 SCORECARD — Shree Hari Chemicals Export Ltd (SHHARICH, BSE 524336)

Run date: 2026-09-05. CMP Rs 248.0, market cap Rs 156 cr (manifest, 2026-09-05).

Data available: 3 years (FY2024 to FY2026). Scoring adapted to 3-year history.
Data sources: screener.in Data_Sheet CSV (consolidated basis, verified below) and
Annual Report FY2025-26 (181 pages, page-marked text extract). No results PDFs,
no rating document, no quarterly shareholding pattern in this corpus (NO-CONCALL
mode; see input gaps in the YAML block).

## BASIS CONFIRMATION

The screener-data Data_Sheet is CONSOLIDATED. Cross-checked line by line against
the AR for FY25 and FY26:
- Sales FY26: screener 184.50 cr = AR consolidated Revenue from Operations
  18,450.48 lakh (AR FY26, p.145). FY25: screener 141.20 cr = AR 14,119.58 lakh
  (AR FY26, p.145, comparative column).
- Net profit FY26: screener 4.12 cr = AR consolidated PAT 411.81/414.95 lakh
  (AR FY26, p.145; two figures appear in the AR — 411.81 in the Board's Report
  summary table p.59 "Profit for the Year" before OCI split, 414.95 in the
  formal consolidated P&L "Profit for the Year attributable to Owners" p.145;
  screener's 4.12 cr matches 411.81 more closely). FY25: screener 5.10 cr = AR
  509.75 lakh (AR FY26, p.145 comparative).
- CFO FY26: screener 6.63 cr = AR consolidated Cash Generated from Operating
  Activities 662.80 lakh (AR FY26, p.146). FY25: screener -0.80 cr = AR -79.50
  lakh (AR FY26, p.146 comparative).
- Total Assets FY26: screener 107.12 cr = AR consolidated Balance Sheet total
  10,711.52 lakh (AR FY26, p.144). Equity FY26: screener 44.30 cr (5.54+38.76)
  = AR consolidated Equity 4,430.28 lakh (AR FY26, p.144).
- Receivables/Inventory FY26: screener 24.38/12.76 cr = AR consolidated
  2,437.57/1,275.95 lakh (AR FY26, p.144).
- Borrowings FY26: screener 33.21 cr = AR consolidated financial borrowings
  (NC 727.88 + Current 2,563.39 = 3,291.27 lakh) + lease liabilities (NC 17.93
  + Current 11.50 = 29.43 lakh) = 3,320.70 lakh = 33.21 cr (AR FY26, p.144).
  Screener's "Borrowings" line bundles lease liabilities with financial debt.

FY24 basis is assumed consolidated = standalone (no FY24 AR in this corpus to
verify against; the subsidiary SDPL appears pre-operational through FY24-FY26,
since standalone and consolidated Revenue from Operations are IDENTICAL in
both FY26 and FY25 per the Board's Report table, AR FY26 p.59).

## FORMULA BASIS NOTES (read before the blocks)

- ROCE: AR discloses its own ROCE ("Return on Capital employed, EBIT/Capital
  Employed") in Note 35.22 Financial Ratios for FY26 and FY25 only (standalone
  AR FY26 p.137; consolidated AR FY26 p.176). Used as the source figure per the
  fixed formula rule. FY24 NOT FOUND — the FY26 AR's balance sheet only carries
  a FY26/FY25 comparative; no source in this corpus splits FY24 current vs
  non-current liabilities, so Capital Employed (Total Assets − Current
  Liabilities) cannot be computed for FY24 from any provided file.
- ROE: computed per the fixed formula (PAT ÷ average Net Worth), NOT the AR's
  own ROE note (AR's note formula is PAT ÷ closing Equity, undated-average
  basis, and its standalone FY25 cell shows an apparent typographical error —
  "2.48," a duplicate of the row above — so it is not used). FY24 uses closing
  Net Worth only; FY23 opening Net Worth is not in this corpus.
- Inventory Days and Payable Days: computed on a COGS basis (Cost of Material
  Consumed + Purchase of Stock-in-Trade + Changes in Inventories, per the AR
  P&L, since COGS is explicitly available there). Receivable Days: Revenue
  basis (the only option the formula offers).
- Trade Payables exist only for FY25 and FY26 (AR Note 22, standalone p.131 /
  consolidated p.170 area); screener's Data_Sheet carries no payables line and
  no FY24 AR is in this corpus. WC Days and B4 therefore compare FY26 to FY25,
  not FY26 to FY24.
- Capex is isolated only for FY25 and FY26, from the AR consolidated cash flow
  statement line "Sale/(Purchase) of Fixed Assets including ROU and CWIP" (AR
  FY26, p.146): FY26 Rs 12.93 cr, FY25 Rs 5.30 cr. Screener's Data_Sheet gives
  only a lump "Cash from Investing Activity" total for FY24 (-1.47 cr, includes
  non-capex items), so FY24 capex and FY24 FCF are NOT FOUND.
- EBITDA (for D1 Net Debt/EBITDA): computed as PBT + Depreciation + Interest
  from screener-data, which reproduces the AR's own disclosed consolidated
  "Earnings before interest, depreciation & taxes" line exactly for FY25 (Rs
  11.45 cr) and FY26 (Rs 9.70 cr) (AR FY26 MD&A p.77). This AR convention
  INCLUDES Other Income (Rs 3.13 cr in FY26). A stricter operating-EBITDA-only
  measure (Revenue − operating costs, excluding Other Income, built from the
  AR's P&L cost lines) gives Rs 6.57 cr for FY26 instead of Rs 9.70 cr — this
  would move Net Debt/EBITDA from 2.64x to 3.90x (D1 score 0 instead of 1,
  Block D total 5/20 instead of 6/20). Reported using the AR's own disclosed
  convention as primary since the prompt's formula set does not define an
  EBITDA basis; the sensitivity is flagged here for the downstream verifier.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score 9/20

| Metric | FY24 | FY25 | FY26 | Score |
|---|---|---|---|---|
| ROCE (source-reported, consolidated) | NOT FOUND (no current/non-current BS split for FY24 in any provided source) | 29% (AR FY26, p.176, Note 35.22) | 17% (AR FY26, p.176, Note 35.22) | — |
| ROE (computed, PAT÷avg NW) | 11.29% (2.29÷20.29, closing-NW basis; screener-data) | 19.51% (5.10÷avg(20.29,31.98); screener-data) | 10.80% (4.12÷avg(31.98,44.30); screener-data) | — |

- A1 Median ROCE (of 2 available years, FY25/FY26): (29+17)/2 = 23% → band
  20-24.9% = **4**
- A2 Minimum single-year ROCE: 17% (FY26) → band ≥15% = **5**
- A3 Median ROE (3 years, computed): sorted {10.80, 11.29, 19.51}, median =
  11.29% → band <12% = **0**
- A4 ROCE trend, latest vs earliest AVAILABLE (FY26 17% vs FY25 29%, FY24
  substituted out — NOT FOUND): decline of 12pp → band decline >5pp = **0**

Block A = 4+5+0+0 = **9/20**

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score 8/20

| Metric (Rs cr) | FY24 | FY25 | FY26 |
|---|---|---|---|
| CFO (screener-data) | 9.96 | -0.80 | 6.63 |
| PAT (screener-data) | 2.29 | 5.10 | 4.12 |
| Capex (AR FY26, p.146, consolidated CF) | NOT FOUND | 5.30 | 12.93 |
| FCF = CFO − Capex | NOT FOUND | -6.10 | -6.30 |

- B1 Cumulative CFO ÷ Cumulative PAT (3 yrs): (9.96-0.80+6.63) ÷
  (2.29+5.10+4.12) = 15.79 ÷ 11.51 = 1.37 → band ≥1.00 = **5**
- B2 FCF-positive years, of the 2 years assessable (FY24 excluded, capex NOT
  FOUND): 0 of 2 positive = 0% → band <50% = **0**
- B3 Cumulative FCF ÷ Cumulative PAT, same 2-year window (FY25+FY26): FCF
  (-6.10-6.30=-12.40) ÷ PAT (5.10+4.12=9.22) = -1.35 → band <0.20/negative = **0**
- B4 Change in WC Days, FY26 vs FY25 (FY24 substituted out — Trade Payables
  NOT FOUND for FY24): WC Days FY25 = 72.83 (receivable) + 56.35 (inventory) −
  115.47 (payable) = 13.71 days. WC Days FY26 = 48.22 + 37.06 − 72.58 = 12.70
  days. Change = -1.01 days → band ±5 days = **3**

Block B = 5+0+0+3 = **8/20**

## BLOCK C: GROWTH (Max 20) — Score 19/20

| Metric (Rs cr) | FY24 | FY25 | FY26 |
|---|---|---|---|
| Revenue (screener-data) | 138.33 | 141.20 | 184.50 |
| PAT (screener-data) | 2.29 | 5.10 | 4.12 |

- C1 Revenue CAGR (FY24→FY26, 2 yrs): (184.50÷138.33)^(1/2)-1 = 15.49% →
  band 15-19.9% = **4**
- C2 PAT CAGR (FY24→FY26, 2 yrs): (4.12÷2.29)^(1/2)-1 = 34.13% → band ≥20% = **5**
- C3 Positive YoY revenue years: FY25 (+2.07%) and FY26 (+30.66%), 2 of 2 =
  100% → **5**
- C4 PAT CAGR − Revenue CAGR = 34.13 − 15.49 = +18.64pp → band ≥+3pp = **5**

Block C = 4+5+5+5 = **19/20**

CAVEAT (data_notes): the PAT CAGR is an endpoint calculation and does not
capture the path — FY25 was a cyclical PAT peak (Rs 5.10 cr) and FY26 PAT fell
19.2% YoY to Rs 4.12 cr despite 30.7% revenue growth (AR FY26, p.59, cites a
labour-code provision and raw-material cost pressure; p.77 MD&A cites "increase
in Raw Material Price"). C2/C4 read as strong only because the 2-year window
starts before the peak and ends after the fall. This is exactly the "volume vs
spread" question flagged in COMPANY MEMORY; not re-litigated here, only noted
so a downstream stage does not read C2/C4 as clean compounding growth quality.

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score 6/20

| Metric | FY24 | FY25 | FY26 (latest, scored) |
|---|---|---|---|
| Net Debt (Borrowings − Cash&Bank, screener-data, cr) | 22.97 | 25.53 | 25.60 |
| EBITDA (PBT+Dep+Interest, screener-data, cr) | 8.11 | 11.45 | 9.70 |
| Net Debt ÷ EBITDA | 2.83x | 2.23x | **2.64x** |
| EBIT (PBT+Interest, screener-data, cr) | 5.83 | 9.30 | 7.36 |
| Interest (screener-data, cr) | 2.62 | 2.37 | 2.16 |
| EBIT ÷ Interest | 2.23x | 3.92x | **3.41x** |
| Debt ÷ Equity (Borrowings÷Equity, screener-data) | 1.32x | 0.82x | **0.75x** |
| Current Ratio (source-reported, consolidated) | NOT FOUND | 0.87 (AR FY26 p.176) | **0.95** (AR FY26 p.176) |

- D1 Net Debt÷EBITDA (latest) 2.64x → band 2-3x = **1**
- D2 Interest Coverage (latest) 3.41x → band 3-4.9x = **2**
- D3 Debt÷Equity (latest) 0.75x → band 0.5-1.0x = **3** (AR Note 35.22 shows a
  lower consolidated D/E of 0.58x FY26/0.82x FY25, AR FY26 p.176, but that
  figure appears to net cash against debt; this scorecard uses gross Debt ÷
  Equity per the plain formula. Both bases land in the same 0.5-1.0x band, so
  the score is unaffected.)
- D4 Current Ratio (latest) 0.95x → band <1.0 = **0**

Block D = 1+2+3+0 = **6/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score 14/20

- E1 Promoter holding (latest available — AR fallback pattern at 31-Mar-2026,
  no quarterly pattern in this corpus): 59.25% (AR FY26, p.89, Category of
  Shareholders) → band 50-59.9% = **4**
- E2 Promoter holding change: only a 1-year comparison exists in this corpus
  (AR carries 31-Mar-2025 and 31-Mar-2026 only, AR FY26 p.125, Note 35.1 iii):
  54.21% → 59.25%, +5.04pp. Scored on this 1-year change as the best available
  proxy for the "3-year change" metric (no FY23 figure in this corpus) → band
  increased ≥1% = **5**
- E3 Promoter pledge (latest): N/A (not in provided data) — no pledge
  disclosure found in the AR Corporate Governance Report, and no quarterly
  shareholding pattern (which normally carries the pledge column) exists in
  this corpus (see input gap). Scored **0** per the N/A rule; NOT asserted as
  zero pledge.
- E4 Contingent Liabilities ÷ Net Worth (latest): Contingent liabilities FY26 =
  Bank Guarantees 117.21 + Show Cause/Demand Notice 12.68 + TDS demand 4.83 =
  134.72 lakh = Rs 1.35 cr (AR FY26, p.131 standalone / p.170 consolidated,
  Note 35.12). ÷ Net Worth (consolidated, 44.30 cr) = 3.04% → band <5% = **5**

Block E = 4+5+0+5 = **14/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score 17/60, 5 tests present

Peer set: BODALCHEM (mcap Rs 1,959.94 cr), AKSHARCHEM (mcap Rs 357.35 cr),
SHREEPUSHK (mcap Rs 1,536.85 cr) — all peer-Data_Sheet.csv. AKSHARCHEM's
Data_Sheet carries only FY2015-16 figures (stale, unusable for a FY26
comparison); M2 and M9 below use the 2 usable peers (BODALCHEM, SHREEPUSHK)
only, not scored 0/"PEER DATA NEEDED" since sufficient peer data existed.

SHHARICH operating EBITDA margin (excl. Other Income, screener/AR-derived):
FY24 2.71%, FY25 7.49%, FY26 3.57%. SHHARICH gross-margin proxy
(Revenue−Material Cost)÷Revenue, FY26: 31.76%.
Peer FY26 operating EBITDA margin: BODALCHEM 8.36%, SHREEPUSHK 10.19% (median
9.28%). Peer FY26 GM proxy: BODALCHEM 46.57%, SHREEPUSHK 35.99% (median
41.28%).

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | 3 | Margin latest(3.57%) vs earliest(2.71%) FY24: +0.86pp = stable ±2pp; Revenue CAGR 15.49% ≥10% → "stable AND ≥10%" band. Margin was NOT stable in between (peaked 7.49% FY25) — endpoint test only; flagged. |
| M2 | Cost Advantage vs peer | 0 | SHHARICH FY26 3.57% vs peer median 9.28% = 5.71pp BELOW → "below" band |
| M3 | Capital Efficiency | 3 | FAT (Rev÷Net Block) FY26 = 184.50÷20.92 = 8.82x >2x; ROCE(latest)=17% >15%, not >20% → "FAT>2x AND ROCE>15%" band |
| M4 | Customer Stickiness | 3 | Zero revenue-decline years (both YoY periods positive), but receivable days moved -24.6 days FY25→FY26 (not stable ±10). No band literally fits "0 decline years, unstable days"; scored at the middle band as the closest fit to a record with no decline years. Judgment call, flagged. |
| M5 | Scale & Dominance | 0 | SHHARICH mcap Rs 156 cr is the smallest of the 4 compared (vs 357-1,960 cr); not top 3. True segment likely wider (Kiri, Bhageria, Sudarshan per company memory, no data provided) — directionally consistent with sub-top-5, not a guessed figure |
| M6 | Technology/R&D | 0 | AR: "Expenditure incurred on Research and Development: NIL" (AR FY26, p.63) |
| M7 | Regulatory/License | 0 | Unregulated commodity dye-intermediate manufacturing, more than 10 listed competitors (company memory names Kiri, Bhageria, Sudarshan, Bodal, AksharChem, Shree Pushkar) |
| M8 | Distribution | 0 | No quantified distribution/reach disclosure found (direct B2B export/domestic supply) |
| M9 | Brand | 0 | GM proxy 31.76% vs peer median 41.28% — below peers → "at/below" band |
| M10 | Switching Costs | 5 | Revenue grew every year (FY24-26); receivable days FY24→FY26 = 57.53→48.22 days, a DECREASE (satisfies "rose ≤10 days") → top band |
| M11 | Network Effects | 0 | Only 3 years available, not the ≥6 needed for the two-window test; scored conservatively. Revenue CAGR 15.49% <20% threshold; FY26 selling-expense % not isolable (folded into "Other Expenses" in the latest screener year) |
| M12 | Negative WC/Float | 3 | WC Days FY25=13.71, FY26=12.70 (FY24 NOT FOUND, payables missing) — both available years in 0-15 day band → "0-15 days consistently" |

Moat score (sum) = 3+0+3+3+0+0+0+0+0+5+0+3 = **17/60**
Moats present (score ≥3): M1, M3, M4, M10, M12 = **5**
Moat classification: 4-5 present = **STRONG**

---

## CLASSIFICATION

Core score = A(9)+B(8)+C(19)+D(6)+E(14) = **56/100**
Moat score = **17/60**
Grand total = 56+17 = **73**

Classification matrix: Core 56 falls in "Core 40-59 = AVERAGE" (moat class does
not change this band). Computed classification (pre-downgrade) = **AVERAGE**.

Deal-breaker check (none triggered):
1. Block A (9) not <8 — no trigger
2. Block B (8) not <8 — no trigger
3. Median ROCE (23%) not <10% — no trigger
4. Cumulative CFO/PAT (1.37) not <0.50 — no trigger
5. Pledge unknown (N/A), not asserted >15% — no trigger
6. ND/EBITDA (2.64x) not >3x AND IC (3.41x) not <3x — no trigger either way (even
   under the alternative operating-EBITDA basis, ND/EBITDA would be 3.90x but
   IC would remain 3.41x, still not <3x, so this deal-breaker cannot fire under
   either EBITDA basis)
7. Revenue grew both YoY periods — no trigger
8. PAT positive all 3 years (2.29, 5.10, 4.12) — no trigger
9. History = 3 years, not <3 — no trigger (this instead triggers the data
   confidence downgrade below, a separate rule)

Data confidence: 3 years of history (FY24-FY26) falls in the "3-4 years =
LIMITED, downgrade classification one tier" band. AVERAGE → **AVOID** (one
tier down the EXCELLENT > GOOD+ > GOOD > AVERAGE > AVOID ladder).

**FINAL CLASSIFICATION: AVOID** (history_downgrade applied; pre-downgrade
computed classification was AVERAGE)

Strongest block: C (Growth), 19/20 — but see the CAVEAT above on CAGR
inflation from the FY25 cyclical peak.
Weakest block: D (Balance Sheet Strength), 6/20 — sub-1.0x current ratio and
Net Debt/EBITDA in the 2-3x band.

Decision line: Gate 0 is a mechanical scorecard, not a company-quality halt
(per pipeline rule, no STOP verdict exists at this stage). AVOID here is driven
primarily by the 3-year LIMITED-history downgrade rule acting on a Core score
that already sat at the bottom of the AVERAGE band, compounded by a genuine
commodity-converter moat profile (5 of 12 tests present, concentrated in
capital efficiency and switching-cost proxies, not pricing power or scale).
Flagged for the pipeline; the run proceeds per the pipeline sequence.

## FLAG-CASH INPUT (block_b_trend)

block_b_trend = deteriorating. The one number: cumulative FCF over the only 2
assessable years is -Rs 12.40 cr (FY25 -6.10 cr, FY26 -6.30 cr), both negative,
on rising capex (Rs 5.30 cr → Rs 12.93 cr) funding the SDPL expansion. CFO
itself improved (FY25 -0.80 cr → FY26 +6.63 cr) but did not outpace the capex
increase. FY25's negative CFO despite a positive PAT of Rs 5.10 cr is the
sharpest single cash-quality data point in the 3-year window.

## ANALYST NOTE

Classification lands at AVOID mainly because of the 3-year LIMITED-history
downgrade rule: Core score 56/100 sits inside the AVERAGE band (40-59), and a
3-year-only record forces one tier down regardless of the underlying profile.
The scorecard itself reads as a commodity converter mid-cycle, not a broken
business: strong revenue/PAT CAGR are inflated by FY25 being a cyclical spread
peak (PAT fell 19% YoY in FY26 despite 31% revenue growth); FCF was negative
in both computable years on subsidiary-expansion capex; current ratio sits
below 1.0x; and moat tests fail on cost position (M2), scale (M5), and brand
(M9) against BODALCHEM/SHREEPUSHK. ROCE, ROE-trend, and WC-day-trend metrics
could only be built from 2 of 3 years because no source in this corpus splits
FY24's balance sheet into current/non-current liabilities or carries FY24
trade payables — A4 and B4 compare FY25 to FY26, not FY24 to FY26. Per
Amendment 17 (converter treatment), none of this spot-year data should feed
Section 1B or FTTCP directly; that gate sits downstream of this stage. The one
unambiguously strong signal is M10 (switching costs, full marks): revenue grew
every year while receivable days fell rather than rose.

```yaml
stage: B01-gate0
company: "SHHARICH"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - "results: no quarterly or annual results filing; Q1 FY27 (Jun-2026) results absent; FY26 audited annual results filing absent (AR carries audited FY26 statements)"
  - "rating: no credit rating document"
  - "announcements: no Reg 30 filings; AGM notice inside the AR is the partial substitute"
  - "shareholding: no quarterly shareholding pattern; fallback AR pattern at 31-Mar-2026"
  - "screening: only Data_Sheet CSVs populated (3 annual years FY24-FY26); other screener CSVs are empty templates"
  - "concalls: declared unavailable (NO-CONCALL MODE); not a gap"
  - "prospectus: not expected (listed 1987); not a gap"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID driven primarily by the 3-year LIMITED-history downgrade (Core 56/100 = AVERAGE band, downgraded one tier per data-confidence rule), not by a clean deal-breaker; historical depressors: only 2 of 3 years have ROCE (FY24 BS lacks current/non-current split anywhere in this corpus), only 2 of 3 years have Trade Payables (FY24 NOT FOUND), zero FCF-positive years in the 2 assessable years, current ratio 0.95x, and a moat profile with only 5/12 tests present, weak on cost position (M2), scale (M5) and brand (M9) vs BODALCHEM/SHREEPUSHK."
data_years: 3
fy_range: "FY2024 to FY2026"
blocks: {A: 9, B: 8, C: 19, D: 6, E: 14}
core_score: 56
moat_score: 17
grand_total: 73
moats_confirmed: 5
moat_class: "STRONG"
classification: "AVOID"
deal_breakers: []
history_downgrade: true
data_notes:
  - "ROCE: source-reported (AR Note 35.22, consolidated p.176/standalone p.137) available for FY25 (29%) and FY26 (17%) only; FY24 NOT FOUND (no current/non-current BS split for FY24 in any provided source). A4 trend uses FY25 as the earliest available year, not FY24."
  - "ROE computed per fixed formula (PAT/avg Net Worth), not the AR's own ROE note, which uses closing-equity basis and has an apparent typo in the standalone FY25 cell (shows 2.48, a duplicate of the DSCR row above). FY24 ROE uses closing Net Worth only (FY23 opening not in corpus)."
  - "E2 promoter-holding change scored on a 1-year window (54.21% to 59.25%, AR FY26 p.125) because the AR carries only 31-Mar-2025 and 31-Mar-2026; no 3-year-prior figure exists in this corpus."
  - "E3 promoter pledge: no pledge disclosure found in the AR Corporate Governance Report; no quarterly shareholding pattern in corpus. Scored 0/N/A, not asserted as zero pledge."
  - "Capex/FCF isolable only for FY25 (Rs 5.30 cr) and FY26 (Rs 12.93 cr) from the AR consolidated cash flow statement (p.146); FY24 capex NOT FOUND (screener gives only a lump investing-CF total). B2/B3 scored on the 2 assessable years only."
  - "Trade Payables available only for FY25 and FY26 (AR Note 22, p.131/p.170 area); FY24 NOT FOUND (not in screener Data_Sheet, no FY24 AR in corpus). B4 WC-Days change compares FY26 to FY25, not FY26 to FY24."
  - "Inventory Days and Payable Days computed on a COGS basis (Cost of Material Consumed + Purchase of Stock-in-Trade + Changes in Inventories, AR P&L) since COGS is explicitly available; Receivable Days computed on Revenue basis (formula's only option)."
  - "PAT CAGR (34.13%, FY24-FY26 endpoints) is inflated by FY25 being a cyclical spread peak; FY26 PAT fell 19.2% YoY versus FY25 despite 30.7% revenue growth (AR FY26 p.59, p.77). Flagged for downstream stages; consistent with the company-memory 'volume vs spread' load-bearing question, not re-litigated here."
  - "D1 EBITDA basis: used AR's own disclosed consolidated EBITDA convention (PBT+Depreciation+Interest, includes Other Income), giving Net Debt/EBITDA 2.64x (D1=1). A stricter operating-EBITDA-only measure (excludes Other Income) gives 3.90x (D1=0, Block D would be 5/20 instead of 6/20). Formula set does not define an EBITDA basis; sensitivity flagged."
  - "Peer data: AKSHARCHEM-Data_Sheet.csv contains only FY2015-16 figures, stale and unusable for FY26 comparison. M2 and M9 computed using the 2 usable peers (BODALCHEM, SHREEPUSHK) only, not scored as PEER DATA NEEDED since sufficient peer data existed."
  - "No loss-to-profit swing in the 3-year window; PAT positive all 3 years (FY24 Rs 2.29 cr, FY25 Rs 5.10 cr, FY26 Rs 4.12 cr)."
  - "Basis check: screener-data figures (Sales, PAT, CFO, investing CF, Total Assets, Equity, Receivables, Inventory, Borrowings) verified line-by-line against CONSOLIDATED AR figures for FY25/FY26. FY24 basis assumed consolidated=standalone (SDPL pre-operational; no FY24 AR in corpus to verify)."
block_b_trend: "deteriorating — cumulative FCF over the only 2 assessable years is -Rs 12.40 cr (FY25 -6.10 cr, FY26 -6.30 cr), both negative on rising capex (Rs 5.30 cr to Rs 12.93 cr); FY25 CFO was -Rs 0.80 cr despite +Rs 5.10 cr PAT, the sharpest single cash-quality data point in the window"
analyst_note: "Classification lands at AVOID mainly because of the 3-year LIMITED-history downgrade rule: Core score 56/100 sits inside the AVERAGE band (40-59), and a 3-year-only record forces one tier down regardless of the underlying profile. The scorecard reads as a commodity converter mid-cycle, not a broken business: strong revenue/PAT CAGR are inflated by FY25 being a cyclical spread peak (PAT fell 19% YoY in FY26 despite 31% revenue growth); FCF was negative in both computable years on subsidiary-expansion capex; current ratio sits below 1.0x; moat tests fail on cost position (M2), scale (M5), and brand (M9) against BODALCHEM/SHREEPUSHK. ROCE, ROE-trend, and WC-day-trend metrics could only use 2 of 3 years because no source in this corpus splits FY24's balance sheet into current/non-current liabilities or carries FY24 trade payables. Per Amendment 17, none of this spot-year data should feed Section 1B or FTTCP directly; that gate sits downstream. The one unambiguously strong signal is M10 (switching costs, full marks): revenue grew every year while receivable days fell rather than rose."
```
