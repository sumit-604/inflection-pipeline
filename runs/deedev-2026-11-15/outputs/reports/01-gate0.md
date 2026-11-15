# STAGE 1 GATE 0 SCORECARD: DEE Development Engineers Ltd (DEEDEV), run 2026-11-15

Data available: 7 years (FY20 to FY26). Scoring adapted to 7-year history (data confidence: moderate, 7-9 band; no downgrade).

Units: screener-data is INR Cr (consolidated; FY26 CFO 19.55 = AR/results INR lacs 1,954.85, so the sheet is consolidated). Results and AR are INR lacs, the prospectus is INR million. Each anchor carries its unit. Page anchors for the prospectus use the section name, because I did not page-resolve the .txt.

## 0. Load-bearing facts reachable at this stage (checked first)

| LBF | What I found at the page |
|---|---|
| 2 Cash conversion | CONFIRMED. H1 FY27 net cash used in operating activities (679.09) INR lacs = -Rs 6.79 Cr; PBT 4,991.76 INR lacs = Rs 49.92 Cr (results Q2 FY27 p.7, consolidated cash-flow). H1 FY26 comparable was +327.34 INR lacs. FY26 consolidated CFO 1,954.85 INR lacs = Rs 19.55 Cr on PBT 9,624.89 INR lacs (results Q4 FY26 p.17); FY25 CFO (11,845.73) INR lacs (results Q4 FY26 p.17). Screener CFO series ties to both years. |
| 2 Operating cycle | Not reproduced on the same basis. On a revenue basis (this prompt's formula) FY26 is inventory 184 + receivable 123 - payable 31 = 275 days (computed below). The brief's 261 days (inventory 227, debtors 100, creditors 66) uses a COGS/other basis; I did not reach its source. The direction agrees (cycle far above the 190-200 day target). |
| 1 Guidance vs delivery | PARTLY CONFIRMED. Sales Q1 FY27 294.46 and Q2 FY27 292.99 (screener-data, Quarters; INR Cr), so H1 = 587.45 and Q2 is below Q1. Rs 1,500 Cr less 587.45 = 912.55, which is +55.3% over H1. The Rs 1,500 Cr guidance itself and the Rs 25 Cr deferral are transcript statements, not in my inputs: NOT VERIFIED here. |
| 3 Contingency | AR consolidated Note 30B lists claims and obligations (below, used in E4). The Abohar Rs 13.85 Cr refund and the MPPL carrying value are not in Note 30B as a line; I did not trace them at this stage (a text search for "13.85" and "1,385" found nothing in the AR text). NOT VERIFIED here; left to stages 3 and 5. |
| 4 Concentration | Outside this stage's inputs. |

## 1. Extracted base series (INR Cr, screener-data, Data_Sheet)

| Item | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| Sales | 722.51 | 495.22 | 460.92 | 595.50 | 788.76 | 827.36 | 1142.00 |
| PBT | 27.14 | 8.83 | 13.29 | 20.37 | 35.51 | 55.35 | 96.25 |
| Interest | 42.58 | 29.78 | 28.10 | 34.35 | 46.69 | 45.02 | 60.74 |
| Net profit | 13.37 | 14.21 | 8.20 | 12.97 | 26.21 | 43.63 | 77.17 |
| Net worth (cap + reserves) | 437.89 | 454.32 | 411.98 | 423.65 | 451.12 | 800.57 | 890.38 |
| Borrowings | 313.21 | 257.16 | 290.39 | 363.76 | 460.46 | 511.89 | 771.19 |
| CFO | 71.30 | 95.54 | 67.15 | 13.94 | 102.92 | -118.46 | 19.55 |

All rows: (screener-data, Profit & Loss / Balance Sheet / Cash Flow blocks). EBITDA = Sales - RM +/- inventory change - power - other mfr - employee - selling - other expenses, which equals the screener operating profit (FY26 195.84; FY20 87.03). Computed, screener-data.

## 2. BLOCK A: Return on capital (max 20)

Screener's Data_Sheet carries no ROCE row, so ROCE is computed. Method: EBIT = PBT + Interest (includes other income); capital employed = Equity + Reserves + Borrowings (= Total assets less Other Liabilities, the only current-liability proxy the Data_Sheet carries; it keeps short-term borrowings inside capital employed). State: computed, proxy basis.

| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| EBIT | 69.72 | 38.61 | 41.39 | 54.72 | 82.20 | 100.37 | 156.99 |
| Cap. employed | 751.10 | 711.48 | 702.37 | 787.41 | 911.58 | 1312.46 | 1661.57 |
| ROCE % | 9.28 | 5.43 | 5.89 | 6.95 | 9.02 | 7.65 | 9.45 |
| ROE % | 3.05* | 3.19 | 1.89 | 3.10 | 5.99 | 6.97 | 9.13 |

*FY20 ROE on closing net worth (no opening available). ROE = PAT / average net worth, computed from screener-data.

Sensitivity on the strict prompt formula (TA - current liabilities), only where current liabilities are in the inputs: FY26 = 156.99 / (1,923.73 - 869.24) = 14.9% (results Q4 FY26 p.16: total assets 1,92,372.72 and current liabilities 86,924.44 INR lacs); FY25 = 100.37 / (1,593.50 - 687.20) = 11.1% (same page, 1,59,349.91 and 68,720.35 INR lacs). The strict formula counts about Rs 553 Cr of short-term borrowings as funding, not capital employed, which lifts ROCE. The other five years cannot be computed on that basis from the inputs.

| Line | Value | Score |
|---|---|---|
| A1 Median ROCE | 7.65% (median of 7) | 0 |
| A2 Min single-year ROCE | 5.43% (FY21) | 0 |
| A3 Median ROE | 3.19% | 0 |
| A4 ROCE trend, latest vs earliest | 9.45% vs 9.28%, latest >= earliest | 5 |
| **Block A** | | **5 / 20** |

A4 note: the earliest year FY20 (9.28%) is itself low. The A4 score of 5 shows no decline, not a high level.

## 3. BLOCK B: Cash generation quality (max 20)

Capex (purchase of PPE, CWIP and intangibles, acquisitions excluded):
- FY21 16.86, FY22 26.32, FY23 58.65: prospectus restated cash flow, INR million 168.63 / 263.17 / 586.45 (Prospectus, restated cash-flow statement).
- FY25 163.96 = 16,334.04 + 62.27 INR lacs; FY26 189.54 = 18,367.88 + 585.94 INR lacs (results Q4 FY26 p.17, consolidated).
- FY20 and FY24: capex NOT FOUND in the inputs (the prospectus gives only the 9M to Dec 2023 figure). Not estimated.

| Year | CFO | Capex | FCF |
|---|---|---|---|
| FY21 | 95.54 | 16.86 | +78.68 |
| FY22 | 67.15 | 26.32 | +40.83 |
| FY23 | 13.94 | 58.65 | -44.71 |
| FY25 | -118.46 | 163.96 | -282.42 |
| FY26 | 19.55 | 189.54 | -169.99 |

| Line | Value | Score |
|---|---|---|
| B1 Cum CFO / cum PAT | 251.94 / 195.76 = 1.29 (7 years, screener-data) | 5 |
| B2 FCF-positive years | 2 of 5 evaluable = 40% (FY20, FY24 NOT FOUND) | 0 |
| B3 Cum FCF / cum PAT | -377.61 / 156.18 (same 5 years) = negative | 0 |
| B4 WC days change | FY21 225.0 to FY26 275.2 = +50.2 days | 0 |
| **Block B** | | **5 / 20** |

B1 is a 7-year cumulative and is carried by FY20 to FY22 (CFO 233.99 on PAT 35.78). FY25 plus FY26 together: CFO -98.91 on PAT 120.80. The 5 hides a break after IPO.

B2 sensitivity: with the two NOT FOUND years counted as positive, 4 of 7 = 57%, which would score 2. Counted as negative, 2 of 7 scores 0. I score only evaluable years.

B4 working-capital days (revenue basis: receivable, inventory and payable all on revenue; the COGS basis is not used):
- FY21: receivable 146.3 (198.46), inventory 135.8 (184.26), payable 57.1 (77.49 = INR million 774.88 from the Prospectus restated balance sheet) = 225.0.
- FY26: receivable 122.5 (383.34), inventory 184.1 (576.02), payable 31.4 (98.37 = 404.28 + 9,432.67 INR lacs, results Q4 FY26 p.16) = 275.2.
- FY20 payables NOT FOUND, so FY21 is the earliest year. FY26 payables exclude the Rs 65.78 Cr trade credits from banks (INR lacs 6,577.63); including them would lower FY26 to about 254 days, still +29 days, same score.

## 4. BLOCK C: Growth (max 20)

| Line | Value | Score |
|---|---|---|
| C1 Revenue CAGR FY20 to FY26 (6 yrs) | (1142.00 / 722.51)^(1/6) - 1 = 7.9% | 1 |
| C2 PAT CAGR | (77.17 / 13.37)^(1/6) - 1 = 33.9% | 5 |
| C3 Positive YoY revenue years | 4 of 6 = 66.7% (FY21, FY22 fell) | 1 |
| C4 PAT CAGR minus revenue CAGR | +26.0pp | 5 |
| **Block C** | | **12 / 20** |

All from screener-data. The FY20 base year is the pre-IPO high of revenue; FY23 to FY26 revenue CAGR is 24.2% (595.50 to 1142.00, screener-data). The prompt fixes the window at full history, so I score that; the split matters downstream.

## 5. BLOCK D: Balance sheet strength (max 20)

| Line | Value | Score |
|---|---|---|
| D1 Net debt / EBITDA (FY26) | (771.19 - 84.37) / 195.84 = 3.51x | 0 |
| D2 Interest coverage (FY26) | 156.99 / 60.74 = 2.58x (2.34x if other income is stripped from EBIT) | 1 |
| D3 Debt / Equity (FY26) | 771.19 / 890.38 = 0.87 | 3 |
| D4 Current ratio (FY26) | 1,16,038.61 / 86,924.44 = 1.33 (INR lacs; results Q4 FY26 p.16) | 2 |
| **Block D** | | **6 / 20** |

Borrowings 771.19 (screener-data) reconciles to results Q4 FY26 p.16: 13,348.78 + 55,345.20 + 6,577.63 trade credits + 1,313.10 + 534.27 lease INR lacs = 77,118.98. Cash 84.37 = cash 3,926.82 + other bank balances 4,509.77 INR lacs. Excluding trade credits and leases from debt gives net debt 602.57 and 3.08x: still above 3x. The latest annual balance sheet is the scoring basis; the 30 Sep 2026 balance sheet (results Q2 FY27) was not re-scored here.

## 6. BLOCK E: Shareholder alignment (max 20)

| Line | Value | Score |
|---|---|---|
| E1 Promoter holding | 65.13% (shareholding-30Sep2026, promoter and group 49,004,787 shares) | 5 |
| E2 Promoter change over 3 years | Pre-Offer 97.24% + 2.76% = 100.00% (Prospectus, capital-structure table); post-Offer 68.05% + 2.12% = 70.17%; now 65.13%. Down 34.87pp vs pre-Offer, 5.04pp vs post-Offer | 0 |
| E3 Promoter pledge | 0%: encumbered-under-pledge flag false (shareholding-30Sep2026) | 5 |
| E4 Contingent liabilities / net worth | 22,970.21 / 89,043.69 INR lacs = 25.8% (AR Note 30B, PDF p.331-332; equity from results Q4 FY26 p.16) | 1 |
| **Block E** | | **11 / 20** |

E2 note: both baselines give a decline over 3pp, so the score is 0 either way. The drop comes from IPO dilution and the Offer for Sale, not open-market selling. The score does not read intent.

E4 build: income-tax demand 350.62 + excise/GST demand 622.54 + custom duty liability on unfulfilled exports 1,759.76 + export obligation on duty-free imports 20,237.29 INR lacs. The export obligation is 88% of the total and is an obligation the Company expects to fulfil (Note 30B, point c). Ex-obligation, the figure is 2,732.92 / 89,043.69 = 3.1%, which would score 5. I score the full listed total (a stricter, literal read). Also listed and not summed: corporate guarantees for subsidiary loans 668.89 INR lacs (AR Note 30C), a customs demand of 815.09 plus penalty 305.00 INR lacs (Note 30B(e), paid 7.5% under protest), and others. The scorecard score moves Block E between 11 and 15.

## 7. BLOCK F: Quantitative moat (max 60)

Peer set: the three auto-selected sheets (ANUP, ISGEC, RATNAMANI; FY26; peer-Data_Sheet). EBITDA margin by the same formula: DEEDEV 17.15%, ANUP 21.48%, ISGEC 8.59%, RATNAMANI 16.86%; peer median 16.86%. Gross-margin proxy = (Sales - RM +/- inventory change) / Sales: DEEDEV 58.05%, ANUP 52.17%, ISGEC 45.36%, RATNAMANI 40.36%; peer median 45.36%. Market cap (peer sheets, INR Cr): DEEDEV 3,973.32; ANUP 3,455.43; ISGEC 7,248.17; RATNAMANI 17,431.88.

| Test | Evidence | Score |
|---|---|---|
| M1 Pricing power | EBITDA margin 12.05% (FY20) to 17.15% (FY26) = +5.1pp, but revenue CAGR 7.9% < 10% | 0 |
| M2 Cost advantage | 17.15% vs peer median 16.86% = +0.3pp (within +/-2pp) | 1 |
| M3 Capital efficiency | FAT 1,142.00 / 653.78 = 1.75x; ROCE 9.45% (proxy) fails > 12%. On the strict ROCE of 14.9% the score would be 1 | 0 |
| M4 Customer stickiness | 2 revenue-decline years (FY21, FY22), CAGR positive | 1 |
| M5 Scale and dominance | Mcap rank 3 of 4 in the supplied set; margin rank 2 of 4. Provisional: the supplied set is not the full segment | 3 |
| M6 Technology / R&D | R&D spend NOT FOUND (AR text names no R&D expense line); PEER DATA NEEDED not the issue, the company's own figure is | 0 |
| M7 Regulatory / license | Core piping and fabrication are unregulated; only the biomass power segment (INR lacs 5,546.64 of 1,14,199.92 revenue, AR Note 31) is regulated | 0 |
| M8 Distribution | No outlet network; a project and OEM seller | 0 |
| M9 Brand | GM proxy +12.7pp over peer median, but revenue CAGR 7.9% < 8% | 1 |
| M10 Switching costs | Growth in 4 of 6 years; 2 decline years | 1 |
| M11 Network effects | 7 years available. FY23 to FY26 revenue CAGR 24.2% > FY20 to FY23 -6.2% (722.51 to 595.50); selling and admin % of sales 9.29% (FY23) to 6.91% (FY26) = declining | 5 |
| M12 Negative WC / float | WC days 225 to 275, never negative | 0 |
| **Block F** | | **12 / 60** |

Moats present (score >= 3): M5 and M11 = 2, MODERATE.

Flags on the moat score:
- M11 is an arithmetic artefact. DEE is a build-to-spec manufacturer with no network. The test credits the post-FY23 growth acceleration over a COVID-hit, loss-making base. Without it the count is 1 (THIN). Scored as the prompt specifies, because no qualitative judgment is allowed at this stage.
- M5 rests on three auto-selected peers.
- M2 and M9 use those same three peers. The peer set is small.

## 8. Dashboard

```
A Return on capital      5 / 20  #####..............
B Cash generation        5 / 20  #####..............
C Growth                12 / 20  ############........
D Balance sheet          6 / 20  ######..............
E Alignment             11 / 20  ###########.........
CORE                    39 / 100
MOAT (F)                12 / 60   MODERATE (2 present: M5, M11)
GRAND TOTAL             51 / 160
```

Classification box: Core 39 (< 40) = **AVOID**. The deal-breaker grid also fires AVOID on its own (override 6).

Deal-breakers triggered:
- Override 6 (ND/EBITDA > 3x AND interest cover < 3x): 3.51x and 2.58x, FY26. AVOID.
- Override 3 (median ROCE < 10%): 7.65% (all seven years under 10%). Max AVERAGE.
- Override 1 (Block A < 8): 5. Max GOOD.
- Override 2 (Block B < 8): 5. Max GOOD.
- Not triggered: 4 (CFO/PAT 1.29), 5 (0% pledge), 7 (revenue fell in 2 of 6 years), 8 (PAT positive FY24 to FY26), 9 (7 years).

Which years drive it: the leverage trip is FY26 alone. Borrowings rose 511.89 to 771.19 (+259 Cr, +51%) while FY26 funded Rs 189.54 Cr of capex and a working-capital build (receivable +135 Cr, results Q4 FY26 p.16). The low ROCE years are mostly pre-IPO FY20 to FY24 (each below 10%); FY25 and FY26 keep ROCE under 10% on the proxy because capital employed grew 44% and 27%.

Sensitivities on the AVOID call: E4 at 5 (ex-export-obligation) lifts Core to 43 (AVERAGE band), but override 6 still holds AVOID. A strict-formula ROCE would lift A1/A2 for FY25 to FY26 only. Neither shifts override 6, which rests on FY26 debt, EBITDA and interest.

Strongest block: C Growth (12 of 20). Weakest blocks: A and B (5 of 20 each).

Decision line: Gate 0 verdict AVOID on the mechanical scorecard. Per CLAUDE.md, quality never halts a run: this flows on as FLAG-GATE0, and downstream sizing and the operator decide. Block B trend is deteriorating (FY25 plus FY26 CFO -98.91 Cr on PAT 120.80 Cr; H1 FY27 CFO -6.79 Cr on PBT 49.92 Cr).

## 9. Input gaps and NOT FOUND list
- Screener Profit & Loss, Balance Sheet, Cash Flow, Quarters sheets empty; Data_Sheet used.
- Capex FY20 and FY24; payables FY20 and FY24; current liabilities FY20 to FY24 for strict ROCE: NOT FOUND.
- R&D spend: NOT FOUND.
- Q2 FY27 concall absent (call 17 Nov 2026): the guidance statements are unverified here.
- Screener "Adjusted Equity Shares" and PRICE rows partly blank; not used.
- Prospectus restated figures (FY21 to FY23) are INR million; they were cross-checked to screener CFO and receivables for the same years and tie.

---
ORCHESTRATOR ERRATUM (2026-11-15; Verifier A finding, B12a row 6, not a source-fidelity row)
- Section 1 note: EBITDA 195.84 is computed from the Data_Sheet annual expense rows. It does not "equal the screener operating profit": the Data_Sheet has no annual operating-profit row, and the four FY26 quarterly operating profits sum to 191.21. On 191.21, D1 reads 3.59x and still scores 0. Override 6 is unchanged.

```yaml
stage: B01-gate0
company: "DEEDEV"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "screener P&L/BS/CF/Quarters sheets empty; Data_Sheet populated and used"
  - "Q2 FY27 concall transcript absent (call 17 Nov 2026; CORPUS GAPPED-FRESHNESS)"
  - "Q2 FY27 investor presentation absent (none filed)"
  - "research folder empty"
  - "shareholding is XBRL text, not a PDF"
  - "capex FY20 and FY24, payables FY20 and FY24, current liabilities FY20-FY24: NOT FOUND"
  - "R&D spend: NOT FOUND"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID (core 39; override 6: ND/EBITDA 3.51x and interest cover 2.58x, FY26). Depressors: all seven years ROCE under 10% on proxy basis (median 7.65%); FY26 debt-funded capex 189.54 Cr and working-capital build; pre-IPO FY20-FY24 low-return base."}
  - {type: FLAG-CASH, reason: "Block B trend deteriorating: FY25+FY26 CFO -98.91 Cr on PAT 120.80 Cr; H1 FY27 CFO -6.79 Cr on PBT 49.92 Cr (results Q2 FY27 p.7). Cum CFO/PAT 1.29 is carried by FY20-FY22."}
data_years: 7
fy_range: "FY20 to FY26"
blocks: {A: 5, B: 5, C: 12, D: 6, E: 11}
core_score: 39
moat_score: 12
grand_total: 51
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "6: ND/EBITDA 3.51x AND interest cover 2.58x, FY26 (AVOID)"
  - "3: median ROCE 7.65% < 10% (all years FY20-FY26 under 10%, proxy basis) (max AVERAGE)"
  - "1: Block A 5 < 8 (max GOOD)"
  - "2: Block B 5 < 8 (max GOOD)"
history_downgrade: false
data_notes:
  - "ROCE computed (screener Data_Sheet has no ROCE row): EBIT=PBT+interest; capital employed=equity+reserves+borrowings (TA less Other Liabilities proxy). Strict TA-CL ROCE: FY26 14.9%, FY25 11.1%; other years not computable."
  - "ROE FY20 on closing net worth (no opening)."
  - "FCF evaluated on 5 years (FY21-23, FY25-26); FY20 and FY24 capex NOT FOUND, not estimated. FY21-23 capex from prospectus INR million; FY25-26 from results Q4 FY26 p.17 INR lacs."
  - "WC days on revenue basis; earliest year FY21 (FY20 payables NOT FOUND): 225.0 to 275.2 days."
  - "E4 scored on full Note 30B listed total 25.8% (incl. export obligation 20,237.29 INR lacs); ex-obligation 3.1% would score 5 (Block E 15, core 43). Override 6 still holds AVOID."
  - "M11 scores 5 by arithmetic (FY23-26 CAGR 24.2% vs FY20-23 -6.2%; selling % 9.29 to 6.91) but is an artefact: no network economics. Without it moats=1 THIN."
  - "M5 provisional on three auto-selected peers (mcap rank 3 of 4, margin rank 2 of 4); full segment peer list PEER DATA NEEDED."
  - "M6 R&D NOT FOUND scored 0. M9 GM proxy=(Sales-RM+/-inventory change)/Sales: 58.05% vs peer median 45.36%."
  - "Revenue CAGR FY20-26 7.9%; FY23-26 24.2%. Window fixed at full history per prompt."
  - "LBF1: H1 FY27 sales 587.45 Cr, H2 needs 912.55 (+55.3%) for 1,500 Cr; guidance and deferral statements unverified (concall absent). LBF2: H1 FY27 CFO -6.79 Cr on PBT 49.92 Cr CONFIRMED (results Q2 FY27 p.7). LBF3 Abohar 13.85 Cr not found in AR text search; not verified here."
  - "Pre-IPO promoter holding 100.00% (Prospectus pre-Offer) vs 65.13% now (shareholding-30Sep2026); drop is IPO dilution and OFS."
block_b_trend: "deteriorating: FY25+FY26 CFO -98.91 Cr on PAT 120.80 Cr; H1 FY27 CFO -6.79 Cr on PBT 49.92 Cr"
analyst_note: "AVOID rests on FY26 leverage (borrowings +259 Cr to fund capex and working capital), not on loss-making history: PAT grew from 13.37 to 77.17 Cr. Every ROCE year is under 10% on the proxy basis; strict TA-CL basis gives 14.9% for FY26 because 553 Cr of short-term borrowing sits in current liabilities. Cash conversion has broken since IPO (CFO/PAT 1.29 cumulative hides FY25-26). The call is mechanical; the flags carry forward to sizing."
```
