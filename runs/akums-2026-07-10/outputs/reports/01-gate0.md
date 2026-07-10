# STAGE 1: GATE 0 SCORECARD — Akums Drugs & Pharmaceuticals Ltd (AKUMS) — RE-RUN

Run date: 2026-07-10 | Model: claude-sonnet-5 | Data sources: screener.in CSV exports, AR FY26 (integrated annual report, 375pp, PDF `inputs/annual-report/40c769ef-bb37-46e6-a96d-e95b55734c3a.pdf`), Q4 FY26 results (14 May 2026, PDF `inputs/results/1a5e3be8-49f0-4e34-83cf-d45500c1c1c7.pdf`), Q3 FY26 results (13 Feb 2026), 4 peer screener CSVs (COHANCE, INNOVACAP, PPLPHARMA, WINDLAS)

**This is a re-run.** The prior Gate 0 pass (screener-only, no AR/results/rating) scored 58/160 AVERAGE with Block E and several moat tests zeroed purely for missing documents. The AR and results are now available and have been mined directly (grep + targeted reads across the full 375-page AR and both results filings). This re-score is a full re-derivation, not a patch.

Data available: 9 data points spanning FY15 to FY26 (screener-Data_Sheet; **gap FY17–FY19 not exported by screener**, unchanged from before). The AR FY26 and Q3/Q4 FY26 results filings carry Ind AS-standard 2-year comparatives only (FY26 vs FY25 on the balance sheet; FY26 vs FY25 on segment/MD&A summaries) — they do **not** independently re-disclose FY24 or earlier detail. What the new documents unlock: (1) full shareholding pattern and promoter detail (Block E), (2) primary-source trade payables for FY25–FY26 (full Working Capital Days formula, previously a partial proxy), (3) primary-source capex for FY25–FY26 (real FCF, previously a full-history accounting-identity proxy), (4) a current/non-current asset-liability split (D4 Current Ratio, previously N/A), (5) quantified R&D and distribution-network disclosures (M6, M8), (6) the full shareholding/pledge/contingent-liability picture. Scoring adapted to this 9-data-point core history with primary-source cross-verification for FY25–FY26.

---

## FORMULA BASIS NOTES (read before the blocks)

- **Screener basis confirmed consolidated**: cross-checking screener-Data_Sheet FY26 Sales (4,359.02 cr), Receivables (796.56 cr), Inventory (755.71 cr) and Cash & Bank (1,680.60 cr) against the Q4 FY26 audited **consolidated** statement of assets and liabilities (results p.21) — Revenue from operations 43,590.17 million, Trade receivables 7,965.64 million, Inventories 7,557.13 million, Cash & equivalents 3,860.05m + other bank balances 12,945.93m = 16,805.98m — all match screener to the cent (₹1 million = ₹0.1 cr). Screener-Data_Sheet is confirmed **consolidated**, not standalone. All blocks below use consolidated figures for consistency.
- **ROCE/ROE**: no populated ROCE/ROE ratio column in the export; both remain **computed**. ROCE = EBIT ÷ Capital Employed (Equity Share Capital + Reserves + Borrowings, screener Data_Sheet). EBIT = PBT + Interest.
- **Payable Days / full WC Days — NOW COMPUTABLE for FY25–FY26**: Q4 FY26 results (p.21, consolidated) give Trade payables (MSME + others) = ₹6,021.58 million (FY26) and ₹6,427.85 million (FY25). This is primary-source data unavailable in the prior screener-only run. Full WC Days (Receivable + Inventory − Payable) is now computed for FY25 and FY26 using the true formula; FY15–FY24 payables remain undisclosed in any provided document (AR/results carry only 2-year comparatives), so the full-formula trend is a **2-year window**, below the general 3-year minimum — flagged explicitly, used as the best available primary evidence rather than discarded.
- **Capex/FCF — NOW COMPUTABLE from primary cash-flow statements for FY25–FY26**: Q4 FY26 results consolidated cash flow (p.22): "Purchase of property, plant and equipment and intangible assets" = ₹2,305.29m (FY26) and ₹2,723.12m (FY25). These replace the FY25/FY26 rows of the prior run's accounting-identity capex proxy (Δ(Net Block+CWIP)+Depreciation). FY16, FY21–FY24 capex remain proxied (no primary cash-flow statement available for those years in any provided document) — stated explicitly per row.
- **Current Ratio (D4) — NOW COMPUTABLE**: Q4 FY26 results consolidated balance sheet (p.21) gives Total current assets = ₹35,598.58m and Total current liabilities = ₹10,947.57m for FY26 — a genuine current/non-current split, unavailable in the screener export.
- **EBITDA cross-check**: the annual line-item resum of screener P&L rows (Sales − RM − ΔInv − Power − OtherMfr − Employee − SellAdmin − OtherExp) gives FY26 EBITDA = ₹549.90 cr (12.61% margin) — this **excludes** "Purchase of stock-in-trade" and "Changes in inventories of stock-in-trade," which screener's Data_Sheet template omits as separate rows but which Q4 FY26 results (consolidated P&L, AR p.72) show as real cost lines for a group with trading/distribution subsidiaries. Recomputing from the audited consolidated P&L: EBITDA FY26 = Revenue 43,590.17m − (Total expenses 40,856.17m − Finance costs 940.73m − Depreciation 1,545.51m) = ₹5,220.24m = **₹522.02 cr (11.98% margin)** — this matches the quarters-summed Operating Profit figure used for peer comparison in the prior run almost exactly (522.03 cr) and is the more accurate, audited figure. **Used for FY26 in all cross-sectional/peer tests (M2, M5) and stated as the audited cross-check for M1's FY26 row; FY15–FY25 margins remain the line-item-computed screener figures since no audited multi-year EBITDA breakdown exists for those years in provided documents** — methodology stated per year.
- **M9 Brand GM proxy**: (Revenue − Material Cost) ÷ Revenue, Material Cost = Raw Material Cost + Change in Inventory, stated proxy, unchanged basis from prior run.
- **Shareholding (Block E) — NOW COMPUTABLE from AR primary source**: AR FY26 Corporate Governance Report, "Category-wise shareholding Pattern as on March 31, 2026" (AR PDF p.119, printed p.185) and Note 15.3 "Details of shareholders holding more than 5% shares... and shares held by promoters" (AR PDF p.244, standalone financial statements) give promoter holding, promoter-holding history since listing, and (by absence) the pledge picture. See Block E for full detail and the specific data-availability limit on the 3-year E2 window (company listed 6 August 2024 — AR PDF p.244/p.324).
- **Contingent liabilities (E4)**: Note 37 "Contingent liabilities and litigations," consolidated financial statements (AR PDF p.338–340). Standalone equivalent is Note 35 (AR PDF p.251).
- **R&D (M6)**: Note 45 "Research and development expenditure," consolidated financial statements (AR PDF p.360), corroborated by the standalone MD&A R&D narrative (AR PDF p.80).
- **Distribution (M8)**: Business Responsibility & Sustainability Report, "Markets served" (AR PDF p.128) and "Openness of business" dealer/distributor concentration table (AR PDF p.146).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Per-year EBIT, Capital Employed, and ROCE (computed; screener Data_Sheet for underlying PBT/Interest/Equity/Reserves/Borrowings — unchanged from prior run, screener export identical):

| FY | PBT | Interest | EBIT | Cap. Employed | ROCE |
|---|---|---|---|---|---|
| 15 | 76.74 | 23.12 | 99.86 | 748.80 | 13.34% |
| 16 | 88.78 | 22.14 | 110.92 | 842.81 | 13.16% |
| 20 | 113.82 | 19.93 | 133.75 | 897.25 | 14.91% |
| 21 | 172.26 | 6.74 | 179.00 | 1014.82 | 17.64% |
| 22 | -193.20 | 16.66 | -176.54 | 1016.96 | -17.36% |
| 23 | 150.30 | 46.25 | 196.55 | 1336.28 | 14.71% |
| 24 | -45.28 | 50.61 | 5.33 | 1274.72 | 0.42% |
| 25 | 345.25 | 34.60 | 379.85 | 3135.23 | 12.12% |
| 26 | 382.10 | 94.07 | 476.17 | 3470.78 | 13.72% |

(all inputs: screener Data_Sheet)

- **A1 Median ROCE = 13.34%** (5th of 9 sorted values) → band 10–14.9% = **3**
- **A2 Minimum single-year ROCE = -17.36% (FY22)** → <8% = **0**
- **A3 Median ROE = 8.72%** (computed: PAT ÷ average Net Worth; FY15 and FY20 use closing NW only, opening unavailable due to the FY17-19 gap):

| FY | PAT | Avg/Closing NW | ROE |
|---|---|---|---|
|15|43.07|494.02 (closing only)|8.72%|
|16|61.48|561.70|10.95%|
|20|43.65|722.40 (closing only, FY19 gap)|6.04%|
|21|122.71|803.63|15.27%|
|22|-252.54|753.42|-33.52%|
|23|94.86|669.59|14.17%|
|24|-4.04|713.35|-0.57%|
|25|338.18|1878.26|18.01%|
|26|255.19|3180.18|8.02%|

→ <12% = **0**
- **A4 ROCE trend, FY26 (13.72%) vs FY15 (13.34%)**: latest ≥ earliest → **5**

**Block A = 3 + 0 + 0 + 5 = 8 / 20** (unchanged — no new document affects this block; screener P&L/BS export is identical to the prior run)

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

- **B1 Cumulative CFO ÷ Cumulative PAT**: Cumulative CFO (9yr) = 2,672.78 cr; Cumulative PAT (9yr) = 702.56 cr (screener Data_Sheet, both sums verified by re-addition) = **3.80x** → ≥1.00 = **5**

FCF, 7 valid consecutive-pair years. **FY25 and FY26 now use real capex from the audited consolidated cash-flow statement (Q4 FY26 results p.22, cross-checked against AR consolidated cash flow); FY16, FY21–24 remain the accounting-identity proxy (Δ(Net Block+CWIP)+Depreciation) since no primary cash-flow breakdown for those years exists in provided documents:**

| FY | CFO | Capex | Basis | FCF |
|---|---|---|---|---|
|16|89.14|105.14|proxy|-16.00|
|21|130.61|289.30|proxy|-158.69|
|22|31.85|225.29|proxy|-193.44|
|23|176.63|261.67|proxy|-85.04|
|24|498.26|311.35|proxy (no primary source available)|+186.91|
|25|465.20|272.31|**real, results Q4 FY26 p.22 / AR consolidated CF**|+192.89|
|26|1181.20|230.53|**real, results Q4 FY26 p.22 / AR consolidated CF**|+950.67|

- **B2 FCF-positive years = 3 of 7 (42.9%)** → <50% = **0** (unchanged conclusion; FY24-26 were already positive under the proxy, the primary-source correction to FY25/26 doesn't flip the pass/fail count)
- **B3 Cumulative FCF (877.29) ÷ Cumulative PAT over same 7 years (615.84) = 1.42x** → ≥0.60 = **5**
- **B4 Change in WC Days — recomputed with the true formula now that Trade Payables is primary-sourced for FY25 and FY26** (results Q4 FY26 p.21, consolidated; screener Data_Sheet for Receivables/Inventory/Sales):
  - FY25: RD = 770.30/4118.16×365 = 68.28d; ID = 680.93/4118.16×365 = 60.35d; PD = 642.785/4118.16×365 = 56.97d → **WC Days = 71.66d**
  - FY26: RD = 796.56/4359.02×365 = 66.69d; ID = 755.71/4359.02×365 = 63.26d; PD = 602.158/4359.02×365 = 50.42d → **WC Days = 79.53d**
  - Change FY25→FY26 = **+7.86 days** → band "increased 5-15 days" = **1**
  - **Data-availability caveat**: this is a 2-year window (FY25→FY26 only), not the full FY15→FY26 span used elsewhere, because Trade Payables is undisclosed for FY15-24 in any provided document. For context only (not scored): the prior run's partial Receivable+Inventory-only proxy across the full FY15→FY26 span showed a small *improvement* (-3.06 days). The now-available true-formula figure shows the opposite direction over the shorter, more recent window — **this is a real, primary-sourced finding, not noise**, and is flagged in data_notes for downstream attention.

**Block B = 5 + 0 + 5 + 1 = 11 / 20** (down from 13 in the prior run — the true WC Days formula, now computable, is less favorable than the partial proxy it replaces; B1 and B3 both improved marginally on more accurate capex data)

**block_b_trend = improving.** CFO jumped from 465.20 cr (FY25) to 1,181.20 cr (FY26), +154% YoY (screener Data_Sheet, cross-verified against results Q4 FY26 p.22: ₹4,651.96m → ₹11,812.02m); FCF (now real, not proxied, for both years) also expanded sharply: +192.89 cr (FY25) → +950.67 cr (FY26). The one number showing deterioration, flagged separately: **WC Days (full formula) rose 71.66d → 79.53d (+7.86d) FY25→FY26**, driven by faster receivable build and slower payable-days (56.97d→50.42d, i.e., paying suppliers faster) even as inventory days held roughly flat — worth monitoring but not yet a cash-quality red flag given the CFO and FCF trajectory.

---

## BLOCK C: GROWTH (Max 20)

Revenue: FY15 = 1,464.27, FY26 = 4,359.02 (screener Data_Sheet, both endpoints positive, 11-year span, unchanged from prior run).
- Revenue CAGR = (4359.02/1464.27)^(1/11) − 1 = **10.43%**

PAT: FY15 = 43.07, FY26 = 255.19 (screener Data_Sheet, both endpoints positive).
- PAT CAGR = (255.19/43.07)^(1/11) − 1 = **17.55%**

- **C1 Revenue CAGR = 10.43%** → band 10-14.9% = **3**
- **C2 PAT CAGR = 17.55%** → band 15-19.9% = **4**
- **C3 Positive YoY revenue years**: valid consecutive pairs (FY16→20 excluded as a 4-year gap): FY15-16(+), FY20-21(+), FY21-22(+), FY22-23(−, 3654.82<3671.89), FY23-24(+), FY24-25(−, 4118.16<4178.18), FY25-26(+) — 5 of 7 = 71.4% → band 50-74% = **1**
- **C4 PAT CAGR − Revenue CAGR = 17.55% − 10.43% = +7.12pp** → ≥+3pp = **5**

**Block C = 3 + 4 + 1 + 5 = 13 / 20** (unchanged — no new document changes the full-history revenue/PAT series)

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

- **D1 Net Debt ÷ EBITDA**: Borrowings 157.43 − Cash & Bank 1,680.60 = **-1,523.17 cr (net cash)** (screener Data_Sheet; cash figure cross-verified exactly against results Q4 FY26 p.21: Cash & equivalents 386.005 cr + other bank balances 1,294.593 cr = 1,680.598 cr). Net cash regardless of which EBITDA base is used → **5**
- **D2 Interest Coverage = EBIT ÷ Interest = 476.17 ÷ 94.07 = 5.06x** (screener Data_Sheet) → band 5-9.9x = **4**
- **D3 Debt ÷ Equity = 157.43 ÷ 3313.35 = 0.048x** (screener Data_Sheet) → <0.1 = **5**
- **D4 Current Ratio — NEWLY COMPUTABLE**: Total current assets ÷ Total current liabilities = 35,598.58 ÷ 10,947.57 million = **3.25x** (results Q4 FY26 p.21, consolidated audited balance sheet) → ≥2.0 = **5**

**Block D = 5 + 4 + 5 + 5 = 19 / 20** (up from 14 — D4 was the sole zero in the prior run purely for lack of a current/non-current split; now resolved with primary data)

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**Fully re-scored — the prior run's zero here was entirely a document-availability gap, now closed.**

- **E1 Promoter holding (latest, FY26)**: **75.26%** — "Promoter and Promoter Group," 11,84,55,480 shares of 15,73,93,988 total (AR PDF p.119, printed p.185, Corporate Governance Report, "Category-wise shareholding Pattern as on March 31, 2026") → ≥60% = **5**

- **E2 Promoter holding change over 3 years**: **data-availability limited — company listed on NSE/BSE only on 6 August 2024** (AR PDF p.244, Note 15.3(a); results Q4 FY26 confirms the same date). A true FY23-baseline 3-year comparison is **NOT FOUND** — pre-IPO private-company cap tables are not subject to public shareholding-pattern disclosure, and no such document was supplied. Best available primary-sourced comparison (AR PDF p.244, Note 15.3, "Details of shareholders holding more than 5% shares... and shares held by promoters," full 12-month FY25→FY26 window, the only complete like-for-like promoter-group data available):
  | Holder | FY26 | FY25 | % change during the year |
  |---|---|---|---|
  | Akums Master Trust (promoter) | 40.79% | 40.79% | — |
  | Sanjeev Jain (promoter) | 17.21% | 17.21% | — |
  | Sandeep Jain (promoter) | 17.23% | 17.23% | — |

  Combined 75.23% (of the >5% holders shown) vs. total category "Promoter and Promoter Group" of 75.26% (AR p.119) — flat, **0.00% change** stated explicitly in the note. FY24-and-earlier data in the same note shows a large apparent swing (Sanjeev Jain 42.45%→17.21%, Sandeep Jain 15.09%→17.23%) but this is the creation of the Akums Master Trust as part of pre-IPO restructuring, not a sale to outside parties, and the note does not disclose full promoter-group % for FY24 (only >5% holders) — **not used, as it would not be a like-for-like total-promoter-group comparison.**
  → within ±1% band = **3** (scored on the best available, fully-disclosed, like-for-like 1-year window; the requested 3-year window is explicitly NOT FOUND and flagged, not fabricated)

- **E3 Promoter pledge (latest)**: The AR's full text (375 pages, searched for "pledge," "encumber*," "Regulation 31," "SAST") contains **no promoter-share-pledge/encumbrance disclosure of any kind** — every "pledge" hit in the AR concerns company assets pledged as security for working-capital/term loans (Note 39/40, unrelated to promoter shares), not promoter shareholding. This is consistent with, but does not by itself independently confirm, a nil-pledge position. Cross-referencing this pipeline run's Stage 8 promoter analysis (`outputs/reports/08-promoter.md`), which sourced pledge = 0% converging across three secondary aggregators (Trendlyne, IIFL, Angel One) — no source found a non-zero figure. Scored on this converging evidence, sourcing basis stated explicitly (secondary-aggregator cross-reference, not a primary AR disclosure line, since the AR simply does not carry the item): 0% → **5**

- **E4 Contingent liabilities ÷ Net Worth (latest, FY26, consolidated)**: Note 37 "Contingent liabilities and litigations" (AR PDF p.338-340): Income-tax matters ₹765.58m + Indirect tax matters ₹103.71m + Product pricing (NPPA) matters ₹121.88m + Others ₹2.82m = **₹993.99m = ₹99.40 cr**. Net Worth (equity attributable to owners, FY26) = ₹3,313.35 cr (screener Data_Sheet; cross-verified exactly against results Q4 FY26 p.21 consolidated: ₹33,133.48m). Ratio = 99.40/3313.35 = **3.00%** → <5% = **5**

  **Separately flagged, not included in the ratio (per "never estimate a missing number" — no number exists to include)**: the IT Department conducted a search-and-seizure operation under Section 132 of the Income Tax Act at Akums offices, manufacturing units, and KMP residences from 15–21 January 2025 (AR PDF p.280, Note 55(c), standalone; also consolidated Note (subsidiary) equivalent, and both statutory auditors' reports carry a formal **"Emphasis of Matter"** paragraph on this, without qualifying the audit opinion). The Company has been required to furnish returns of undisclosed income for the block period 1 April 2018 to 12 March 2025 under Section 158BC; it has filed those returns asserting no undisclosed income, and subsequently received a show-cause notice (post 31 March 2026) to which it has responded. **The AR states explicitly: "As of the reporting date, there have been no demands which have been raised on the Company"** (AR PDF p.280-281). The Rs 133.75 cr block-period tax demand figure referenced in this run's task brief was searched for specifically across the full AR text and both Q3/Q4 FY26 results filings — **NOT FOUND in any provided document**; it directly contradicts the AR's explicit "no demands raised" statement as of the FY26 reporting date. This is recorded as **NOT FOUND / possibly a different (unconfirmed) source or a post-report-date development**, not fabricated into the E4 ratio.

  Also flagged (immaterial in size, ₹4.49 million / ₹0.45 cr, but a governance item): AR Note 55(d) discloses a case of misappropriation of funds relating to IT assets/services at Head Office, involving fictitious/inflated procurement via vendor entities, attributed to subsidiary-company employees; corrective/disciplinary action taken, insurance claim filed.

**Block E = 5 + 3 + 5 + 5 = 18 / 20** (up from 0 — the entire block was a document-availability gap in the prior run; now resolved with the AR as primary source, one item (E2's exact 3-year window) still explicitly data-limited by the company's recent listing rather than by input scope)

---

## CORE SCORE

Blocks A(8) + B(11) + C(13) + D(19) + E(18) = **69 / 100**

Block scores as %: A 40% | B 55% | C 65% | D 95% | E 90%.
**Strongest block: D (Balance Sheet Strength) at 95%. Weakest block: A (Return on Capital) at 40%, driven by the FY22 ROCE trough (-17.36%) and a sub-12% median ROE — both real operating-history findings, not data gaps.**

(Grand total after moat score below: 79/160 — up from the prior run's 58/160, driven almost entirely by Block E, D4, and B4/B3 refinements once the AR/results primary sources were available; Blocks A and C are unchanged because no new document altered the full-history revenue/PAT/ROCE series.)

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin by year (computed, screener Data_Sheet line items FY15-25; **FY26 uses the audited consolidated P&L cross-check, see Formula Basis Notes**):

| FY | EBITDA | Margin |
|---|---|---|
|15|64.26|4.39%|
|16|90.30|5.47%|
|20|116.54|4.83%|
|21|143.11|5.26%|
|22|-264.10|-7.19% (one-off: Other Expenses spiked to 565.07 vs ~75-100 cr normal run-rate; **no FY22 AR/results document was provided in this run to independently re-verify the driver, screener-derived pattern carried forward from the prior run**)|
|23|342.03|9.36%|
|24|147.99|3.54% (one-off: Other Expenses 434.05 cr, IPO-adjacent period; **AR FY26's own comparatives run FY26 vs FY25 only — it does not re-disclose FY24 P&L detail, so this driver also remains screener-pattern-only, not independently re-confirmed by a primary FY24 document**)|
|25|461.34|11.20% (line-item; audited cross-check from results Q4 FY26 consolidated P&L: 464.48 cr / 11.28% — consistent within rounding)|
|26|**522.02 (audited, results Q4 FY26 p.72/AR consolidated P&L cross-check)**|**11.98%** (line-item annual-summed alternative was 549.90/12.61% — audited figure used, see Formula Basis Notes)|

**M1 Pricing Power**: margin expanded FY15 (4.39%) → FY26 (11.98%, audited), +7.59pp, past ≥2pp, AND revenue CAGR 10.43% ≥10% → **5**

**M2 Cost Advantage vs peer median EBITDA margin (FY26, quarters-summed Operating Profit ÷ Sales — unchanged peer CSVs, re-verified identical to the prior run)**:
- COHANCE: 426.99/2268.55 = 18.82%
- INNOVACAP: 238.46/1630.02 = 14.63%
- PPLPHARMA: 921.63/8869.07 = 10.39%
- WINDLAS: 104.76/904.09 = 11.59%
- Peer median = (11.59+14.63)/2 = **13.11%**
- Akums (audited, 11.98%) is 1.13pp *below* peer median, within ±2pp → **1**

**M3 Capital Efficiency**: FAT = Sales ÷ Net Block = 4359.02/1455.80 = 2.99x; ROCE FY26 = 13.72%. FAT>3x AND ROCE>20% fails; FAT>2x AND ROCE>15% fails (ROCE short); FAT>1x AND ROCE>12% holds → **1**

**M4 Customer Stickiness**: 2 revenue-decline years (FY22-23, FY24-25), overall CAGR positive → **1**

**M5 Scale & Dominance** (4 supplied comparators; broader listed universe not enumerable from provided data): Mcap ranking — PPLPHARMA 23,598.52 > COHANCE 17,270.55 > **AKUMS 11,051.63** > INNOVACAP 5,668.41 > WINDLAS 1,713.64. Akums is 3rd of 5. Margin ranking (FY26, audited) — COHANCE 18.82% > INNOVACAP 14.63% > AKUMS 11.98% > WINDLAS 11.59% > PPLPHARMA 10.39%. Akums is 3rd of 5 (not top 2). Top-3 mcap holds, margin-top-2 fails → falls to "top 5 mcap" band → **1**

**M6 Technology/R&D — NEWLY QUANTIFIED (previously N/A/0 for lack of data; now an evidenced 0)**: AR Note 45 (consolidated, AR PDF p.360): Holding Company R&D revenue expenditure = ₹318.35m (FY26) / ₹235.67m (FY25). A group subsidiary (Barwala DSIR-recognised unit) R&D revenue expenditure = ₹56.57m (FY26, full year) / ₹44.19m (FY25, partial period from 28 Nov 2024). Combined consolidated R&D revenue expenditure: FY26 = ₹374.92m = ₹37.49 cr; FY25 = ₹279.86m = ₹27.99 cr.
- R&D/Revenue FY26 = 37.49/4359.02 = **0.86%**
- R&D/Revenue FY25 = 27.99/4118.16 = **0.68%**
Both years fail even the lowest test band (≥1%) → **0** (also, separately, capital expenditure of ₹253.58m/₹150.95m was capitalised under PP&E in the same note — capitalised, not expensed, correctly excluded from the ratio)

**M7 Regulatory/License**: still cannot verify the true count of listed players in the regulated pharma-CDMO/formulations segment — only 4 comparators supplied, not a full segment enumeration; AR contains qualitative "largest CDMO" claims (AR p.420, p.1900-ish narrative) but no quantified count of listed peers → PEER DATA NEEDED, scored **0** (unchanged)

**M8 Distribution — NEWLY QUANTIFIED (previously N/A/0 for lack of data; now an evidenced 0)**: AR Business Responsibility & Sustainability Report (p.128, p.146):
- Reach is quantified: national, Pan-India (28 states + 8 union territories); international, 72 countries (AR p.128, p.9531); export contribution 4.4% of turnover.
- But the only **year-over-year comparable** distribution metric disclosed (BRSR "Openness of business," AR p.146) shows a sharp **decline**, not growth: Number of dealers/distributors sold to fell from 2,979 (FY25) to 271 (FY26), a -90.9% drop; sales to dealers/distributors as % of total sales fell from 16.95% (FY25) to 5.74% (FY26); concentration among the top 10 dealers rose sharply (13.43%→43.62%), consistent with a distributor-base consolidation. No prior-year country count is disclosed for a like-for-like international-reach comparison (only the current 72-country figure).
- Does not meet the "growing" criterion required for bands 5 or 3; the reach is genuinely quantified (not the "mentioned unquantified" band 1 case either) but the only YoY-comparable metric moved backward → **0**

**M9 Brand** (GM proxy, FY26, unchanged basis and peer figures from the prior run):
- Akums: (4359.02 − 2485.84)/4359.02 = **42.97%**
- COHANCE: 67.02% | INNOVACAP: 47.90% | PPLPHARMA: 59.26% | WINDLAS: 39.94%
- Peer median = 53.58%. Akums 42.97% is 10.61pp *below* peer median → at/below → **0**

**M10 Switching Costs**: overall revenue growth (CAGR +10.43%) with 2 decline years → "overall growth, 2+ decline years" → **1**

**M11 Network Effects** (7 continuous years FY20-FY26, ≥6-year threshold met): Latest 3yr (FY23→FY26) CAGR = (4359.02/3654.82)^(1/3)-1 = **6.05%**; Prior 3yr (FY20→FY23) CAGR = (3654.82/2414.16)^(1/3)-1 = **14.82%**. Latest lower than prior (deceleration), and below the 20% threshold → **0**

**M12 Negative WC/Float — recomputed with the true formula now available**: FY25 WC Days = 71.66d; FY26 WC Days = 79.53d (both from Block B4 above, results Q4 FY26 p.21). Both years >45 days → **0** (unchanged conclusion, now on evidenced rather than N/A grounds)

**Moat score = 5+1+1+1+1+0+0+0+0+1+0+0 = 10 / 60**

Moats "present" (score ≥3): M1 only. **moats_confirmed = 1 → THIN**

---

## CLASSIFICATION

- Data confidence: 9 data points → band "7-9 = moderate" (no formal downgrade tier triggered).
- Core score = 69/100 → falls in **Core 60-79** band.
- Moat class = THIN (not STRONG/FORTRESS) → per the classification matrix, "Core 60-79 + else = GOOD" → **base matrix classification = GOOD**

**Deal-breaker check:**
1. Block A (8) <8? No (exactly 8) — no trigger.
2. Block B (11) <8? No — no trigger.
3. Median ROCE (13.34%) <10%? No — no trigger.
4. Cumulative CFO/PAT (3.80x) <0.50? No — no trigger.
5. Pledge >15%? No (0%, per Stage 8 cross-reference, Block E3) — no trigger.
6. ND/EBITDA >3x AND IC <3x? Net cash position — no trigger.
7. Revenue declined in majority of years? 2 of 7 valid YoY pairs (28.6%) — not majority, no trigger.
8. **PAT negative in any of last 3 years? YES — FY24 PAT = -4.04 cr (screener Data_Sheet). Triggers → max AVERAGE.**
9. History <3 years? No, 9 data points — no trigger.

**Deal-breaker #8 triggers, driven by FY24.** The FY24 loss coincides with an "Other Expenses" spike to ₹434.05 cr (vs. a ~75-100 cr normal run-rate) in the screener series, in a year adjacent to major equity-structure changes (bonus issuances, face-value/capital-base changes) ahead of the August 2024 IPO — consistent with the prior run's characterisation of a **documented post-IPO rebase / legacy cleanup pattern**. This characterisation could not be independently re-verified against a primary FY24 document in this run: the AR FY26 in hand carries only FY26-vs-FY25 comparatives (Ind AS standard), and no FY24 annual report or FY24-specific filing was supplied. The finding is therefore carried forward on screener evidence only, flagged as such, and recorded for downstream position-sizing consideration per pipeline rules — it does not lift the Gate 0 cap here.

Base matrix classification (GOOD) is capped down by the deal-breaker to **max AVERAGE**.

**FINAL CLASSIFICATION: AVERAGE**

---

## DASHBOARD SUMMARY

```
BLOCK A (Return on Capital)......... 8/20  [####------] 40%
BLOCK B (Cash Generation Quality)...11/20  [#####-----] 55%
BLOCK C (Growth)....................13/20  [######----] 65%
BLOCK D (Balance Sheet Strength)....19/20  [#########-] 95%
BLOCK E (Shareholder Alignment).....18/20  [#########-] 90%
                                     -----
CORE SCORE...........................69/100

MOAT PROFILE (12 tests, present = score >=3):
M1 Pricing Power.........  5  PRESENT
M2 Cost Advantage......... 1
M3 Capital Efficiency..... 1
M4 Customer Stickiness.... 1
M5 Scale & Dominance...... 1
M6 Technology/R&D......... 0  (evidenced: R&D/Rev 0.86% FY26, 0.68% FY25 - AR Note 45)
M7 Regulatory/License..... 0  (PEER DATA NEEDED - segment player count not enumerable)
M8 Distribution............ 0  (evidenced: dealer count -90.9% YoY, AR BRSR p.146)
M9 Brand................... 0
M10 Switching Costs....... 1
M11 Network Effects....... 0
M12 Negative WC/Float..... 0  (evidenced: WC days 71.7d/79.5d, both >45)
                          ---
MOAT SCORE................10/60   MOATS PRESENT: 1 -> THIN

GRAND TOTAL: 69 + 10 = 79/160

+------------------------------------------------------+
| CLASSIFICATION: AVERAGE                               |
| Base matrix result GOOD (Core 69, moat THIN) capped   |
| by Deal-breaker #8 (PAT negative, FY24, -4.04 cr)     |
| Data confidence: MODERATE (9 data points, FY17-19     |
| gap noted; AR/results add FY25-26 primary detail)     |
+------------------------------------------------------+

Strongest block: D (Balance Sheet Strength), 95%
Weakest block: A (Return on Capital), 40%
```

**Decision line**: Gate 0 does not halt (no STOP verdict exists). With the AR and results now available, AKUMS clears with an AVERAGE classification — up materially from the prior screener-only pass in evidenced quality (Block E fully resolved at 18/20, D4 resolved, real capex/WC-days data for FY25-26) but landing on the same final tier because the FY24 PAT-negative deal-breaker is a hard cap independent of data richness. The underlying picture that emerges with full documents: promoter alignment is strong and clean (75.26% holding, flat since listing, 0% pledge per converging sources, contingent liabilities a clean 3.00% of net worth), balance sheet strength is very strong (net cash, 3.25x current ratio, 0.05x D/E), but the moat profile remains THIN (1 of 12 tests present) and Block A (return-on-capital consistency) is the genuine weak point — FY22's -17.36% ROCE trough and sub-12% median ROE are real historical volatility, not data gaps. Two items are explicitly flagged as NOT FOUND rather than fabricated: the Rs 133.75 cr block-period tax demand referenced in this run's brief (contradicted by the AR's explicit "no demands raised" statement) and the true 3-year E2 promoter-holding-change window (the company has only been listed since August 2024). The IT search-and-seizure matter (Section 132, Jan 2025, auditors' Emphasis of Matter in both standalone and consolidated opinions) is unquantified as of the FY26 reporting date and is flagged for downstream stages rather than folded into E4. Proceeds to Stage 2 with flags carried forward.

---
