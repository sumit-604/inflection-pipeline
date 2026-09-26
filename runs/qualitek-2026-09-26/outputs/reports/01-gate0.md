# STAGE 1: GATE 0 SCORECARD — QUALITEK LABS LTD (QUALITEK) — Pipeline Mode
Run date: 2026-09-26

Data available: 6 years (FY21 to FY26), STANDALONE basis. Scoring adapted to 6-year history.

## BASIS NOTE (read first)
Qualitek prepared consolidated financial statements for the first time only from FY25
(results file 20260520-...txt note 10: "The Company had prepared consolidated financial
statements for the first time effective from financial year ended 31 March 2025").
Consolidated basis therefore has only 2 annual data points (FY25, FY26) — insufficient
for any CAGR, trend, or median calculation. The screener consolidated Data_Sheet.csv
(inputs/screening/screener-Data_Sheet.csv) splices standalone-era FY21/FY22 columns with
consolidated FY25/FY26 columns into one row without saying so; those FY21/FY22 screener
P&L figures also do NOT match the DRHP's own RESTATED standalone financials (e.g.
screener FY21 net profit ₹0.16 Cr vs DRHP restated standalone PAT ₹46.11 lakh — see
data_notes). This scorecard therefore builds its OWN standalone FY21-FY26 series from
primary filings (DRHP restated FY21-23, audited results FY24-26) and scores on that,
per LBF1's instruction to isolate organic (parent-only) growth from acquisition-assisted
consolidated growth. Consolidated FY26 figures (revenue ₹124.52 Cr, +77% YoY) are cited
only for context, never scored, because two points cannot support a CAGR/trend metric.

Standalone core series built (₹ lakh unless stated):

| FY | Revenue | EBITDA | PAT | ROCE (source or computed) | ROE (avg NW) |
|----|---------|--------|-----|---------------------------|--------------|
| 21 | 635.49 (DRHP p.95/117, restated) | 105.31 (DRHP p.117) | 46.11 (DRHP p.117) | 6.38% (DRHP p.117, source) | -105.39% (DRHP p.117, source) |
| 22 | 1,196.57 (DRHP p.117) | 236.18 (DRHP p.117) | 113.57 (DRHP p.117) | 9.34% (DRHP p.117, source) | 181.61% (DRHP p.117, source) |
| 23 | 1,913.66 (DRHP p.117) | 551.30 (DRHP p.117) | 296.91 (DRHP p.117) | 13.76% (DRHP p.117, source) | 50.49% (DRHP p.117, source) |
| 24 | 2,918.38 (results 29-May-2025 p.13, FY24 col) | n/a (not separately stated) | 430.73 (results p.13) | 15.41% (computed, EBIT/(TA-CL); TA 5,058.88, CL 688.41, results p.14) | 20.36% (computed, avg NW = (986.52 DRHP FY23-closing + 3,244.90 FY24-closing)/2, results p.14 + DRHP p.94) |
| 25 | 4,586.48 (results p.13/AR2026 note 34 p.185) | n/a | 528.33 (results p.13) | 10.7% (AR2026 p.78, MD&A, source, standalone) | 8.9% (AR2026 p.78 note 34-D, source, matches computed avg NW 5,911.90) |
| 26 | 6,762.45 (results 20-May-2026 p.12/AR2026 note 34 p.185) | 1,676.01 (computed: PBT 959.73 + Finance Cost 252.84 + Dep 463.44, results p.12) | 796.44 (results p.12) | 7.4% (AR2026 p.78, source, standalone) | 6.9% (AR2026 p.78, source) |

## BLOCK A: RETURN ON CAPITAL — 10/20

- A1 Median ROCE: values 6.38, 9.34, 13.76, 15.41, 10.7, 7.4 → median 10.02%
  (avg of 9.34 & 10.7). Band 10-14.9% = **3**.
- A2 Minimum single-year ROCE: 6.38% (FY21, DRHP p.117). <8% = **0**.
- A3 Median ROE: values -105.39, 181.61, 50.49, 20.36, 8.9, 6.9 → median 14.63%
  (avg of 8.9 & 20.36). Band 12-14.9% = **2**.
- A4 ROCE trend, latest (7.4%, FY26) vs earliest (6.38%, FY21): latest ≥ earliest
  (despite a FY23-24 peak of 13.76-15.41% and a fall since) = **5**.

DATA NOTE: FY21-23 and FY25-26 ROCE use the company's/DRHP's own definition (EBIT ÷
(shareholders' equity + total borrowings), DRHP p.117 note 7 and AR2026 p.78 explanation
text "average capital employed"). FY24 has no source figure, so it was computed under
the STAGE FORMULA (EBIT ÷ (Total Assets − Current Liabilities)) — a different capital-
employed base. Mixing bases is a data quality flag, not a scoring error: the rule
instructs "if the source provides its own ROCE, use it; compute only when absent."

## BLOCK B: CASH GENERATION QUALITY — 5/20

Standalone CFO and capex (₹ lakh):

| FY | CFO | Capex (PPE+CWIP+intangibles, ex-acquisitions) | FCF |
|----|-----|------|-----|
| 21 | 135.03 (DRHP restated CF p.96) | 605.98 (DRHP p.96) | -470.95 |
| 22 | -511.94 (DRHP p.96) | 173.29 (DRHP p.96) | -685.23 |
| 23 | 717.86 (DRHP p.96) | 1,732.17 (DRHP p.96) | -1,014.31 |
| 24 | 553.51 (computed: WC-adjusted operating profit 570.83 less tax paid 17.32, results 29-May-2025 p.15; the printed CFO total line is OCR-garbled) | 999.67 (132.66+855.01+12.00, results p.15) | -446.16 |
| 25 | 801.35 (results 29-May-2025 p.15 / AR2026 confirms) | 2,050.23 (947.88+1,078.85+23.50, results p.15) | -1,248.88 |
| 26 | 715.00 (results 20-May-2026 p.16) | 3,810.74 (612.60+3,190.64+7.50, results p.16; ₹219.86 lakh goodwill outlay for the Mumbai food-lab slump sale EXCLUDED as an acquisition per the FCF formula) | -3,095.74 |

Cumulative CFO = 2,410.81 lakh. Cumulative PAT = 2,212.09 lakh (sum of the PAT column
above). Cumulative FCF = -6,961.27 lakh.

- B1 Cumulative CFO ÷ Cumulative PAT = 1.09 → ≥1.00 = **5**.
- B2 FCF-positive years: 0 of 6 = 0% → **0**.
- B3 Cumulative FCF ÷ Cumulative PAT = -3.15 → negative → **0**.
- B4 WC days change, latest vs earliest (below) → increased >15 days → **0**.

Working capital days (Receivable + Inventory − Payable, revenue basis; no COGS line
disclosed; the company carries no inventory as a testing-services business until a
₹35.63 lakh line appears FY26):

| FY | Receivable days | Inventory days | Payable days | WC days |
|----|----|----|----|----|
| 21 | 69.06 | 0 | 134.55 | -65.49 |
| 22 | 66.90 | 0 | 45.83 | 21.07 |
| 23 | 111.12 | 0 | 70.06 | 41.06 |
| 24 | 98.24 | 0 | 29.73 | 68.51 |
| 25 | 93.79 | 0 | 34.75 | 59.04 |
| 26 | 106.35 | 1.92 | 28.00 | 80.27 |

WC days moved from -65.49 (FY21) to +80.27 (FY26): a swing of +145.76 days, driven
mostly by payable days collapsing (134.55→28.00) as the company outgrew its FY21 stretched-
payables base, while receivable days stayed elevated in the 94-111 range from FY23.
This matches LBF2 (debtor days 124-150 cited at consolidated level; standalone runs
lower at ~94-111 days but the direction — lengthening — is the same).

## BLOCK C: GROWTH — 20/20

- C1 Revenue CAGR FY21→FY26 = (6,762.45/635.49)^(1/5)-1 = 60.47%. ≥20% = **5**.
- C2 PAT CAGR FY21→FY26 = (796.44/46.11)^(1/5)-1 = 76.8%. ≥20% = **5**.
- C3 Positive YoY revenue years: 5 of 5 year-over-year comparisons positive (FY22
  through FY26 all grew vs prior year) = 100% = **5**.
- C4 PAT CAGR − Revenue CAGR = 76.8 − 60.47 = +16.3pp. ≥+3pp = **5**.

This is standalone-only (parent-entity) growth — it excludes ITCPL, QTIPL, the Mumbai
food lab and LabOps Global, which sit in consolidated accounts only. It is real organic
expansion of the parent's own laboratories (funded substantially by IPO and preferential-
issue proceeds redeployed into capex, per the FY26 results utilisation table), not an
artifact of the FY25-26 acquisition spree that inflates the consolidated growth number
cited in LBF1 and company memory. Both are real, but they are different things: this
block scores the parent's own organic climb.

## BLOCK D: BALANCE SHEET STRENGTH — 6/20 (standalone, FY26 latest)

- D1 Net Debt ÷ EBITDA: Net debt = Total borrowings 6,499.19 (4,875.58 LT + 1,623.61 ST,
  results p.14) − Cash & bank 213.94 (202.08+11.86) = 6,285.25. EBITDA (computed) =
  1,676.01. Ratio = 3.75x. >3x = **0**.
- D2 Interest Coverage: EBIT ÷ Interest = (PBT 959.73 + Finance Cost 252.84) ÷ 252.84 =
  4.80x. Band 3-4.9x = **2**.
- D3 Debt ÷ Equity: 6,499.19 ÷ 14,575.06 = 0.45 (matches AR2026 p.77 note J, source).
  Band 0.1-0.5 = **4**.
- D4 Current Ratio: 0.92 (AR2026 p.77/p.185 note 34-A, source, standalone). <1.0 = **0**.

Deal-breaker 6 check: ND/EBITDA >3x is TRUE (3.75x) but Interest Coverage <3x is FALSE
(4.80x): both conditions are required jointly, so the AVOID override does NOT fire.
Flagged as a near-miss: the company is levering up (D/E +36% YoY per AR2026's own
variance table) into a capex programme (FY27 plan ₹63 Cr per LBF2) faster than EBITDA
is compounding leverage cover.

## BLOCK E: SHAREHOLDER ALIGNMENT — 7/20

- E1 Promoter holding (latest, Mar-2026): 56.46% (screener shareholding aggregation,
  inputs/shareholding/screener-shareholding-pattern-2026-09-26.txt — NOT A FILING, per
  B00; the filed figure would sit in AR2026 note F, not independently re-extracted here).
  Band 50-59.9% = **4**.
- E2 Promoter holding change over ~3 years (listing, Mar-2024 73.35% → Mar-2026 56.46%,
  same source): -16.89pp. Decreased >3% = **0**.
- E3 Promoter pledge: NOT FOUND. B00 input_gaps: "shareholding/ is empty: no source is
  automated yet... closes the FII+DII UA qualifier and the promoter pledge trend." No
  filed shareholding pattern is in the corpus to confirm pledge. **N/A → score 0** per
  rule 5 (never estimate a missing number).
- E4 Contingent liabilities ÷ Net worth (standalone, FY26): the STANDALONE contingent
  liability is a corporate guarantee of ₹2,133.00 lakh given to secure ITCPL's borrowings
  (AR2026 note 30, p.185; outstanding balance ₹1,728.59 lakh). Standalone net worth =
  14,575.06 lakh. Ratio = 14.63%. Band 5-15% = **3**. (The CONSOLIDATED note 28, p.77,
  carries a larger, cross-guaranteed figure — ITCPL guaranteeing Qualitek's own borrowings
  back, ₹4,911.00 lakh, plus ₹96.69 lakh of subsidiary tax demands — not used here since
  Block E runs standalone; flagged as a data_note, not scored twice.)

## BLOCK F: QUANTITATIVE MOAT SCORING — 12/60, 3 present, MODERATE

- M1 Pricing Power: EBITDA margin 16.57% (FY21) → 24.79% (FY26), +8.22pp, AND revenue
  CAGR 60.47% ≥10% → **5**.
- M2 Cost Advantage vs peer median: PEER DATA NEEDED. Peer screener sheets
  (VIMTALABS/METROPOLIS/KRSNAA Profit & Loss, Balance Sheet, Cash Flow, Quarters) came
  back EMPTY per B00 collector warning; only qualitative peer concall transcripts exist.
  → **0, PEER DATA NEEDED**.
- M3 Capital Efficiency: FAT = Revenue ÷ Net fixed assets (PPE+CWIP+intangibles) =
  6,762.45 ÷ 9,423.50 = 0.72x. Not >1x. → **0**.
- M4 Customer Stickiness: zero revenue-decline years (all 6 years grew), but receivable
  days ranged 66.90-111.12 (a 44-day spread, not stable ±10). Full marks require both
  conditions; only the no-decline half holds. Scored on the "no decline" strength, one
  tier down from top → **3**.
- M5 Scale & Dominance: PEER DATA NEEDED (no listed pure-play TIC peer of scale exists
  per B00; Vimta/Metropolis/Krsnaa are structural comps in different sub-segments, no
  mcap/margin ranking data provided) → **0, PEER DATA NEEDED**.
- M6 Technology / R&D: no R&D spend disclosed anywhere in the corpus read for this stage
  → **0**.
- M7 Regulatory / License: NABL-accredited, regulated testing business, but no confirmed
  count of listed players in the specific TIC segment (no TIC pure-play peer exists per
  B00). Standalone EBITDA margin swung 16.57%→28.81%(FY23)→24.79%(FY26), a >10pp range,
  well outside the ±3pp or ±5pp stability bands. → **1**.
- M8 Distribution: lab network visibly growing (Bhubaneswar 2nd-lab NABL accreditation
  Oct-2025, ITCPL, Mumbai food-testing slump sale, LabOps Global) AND revenue CAGR
  60.47% ≥15%, but revenue-per-lab is not separately quantified → **3**.
- M9 Brand: PEER DATA NEEDED (no peer gross-margin data; a GM proxy could be built from
  Revenue − Cost of Materials but there is no peer figure to compare it against) → **0,
  PEER DATA NEEDED**.
- M10 Switching Costs: revenue grew every year (0 decline years — better than the "all
  but 1 year" tier) but receivable days ROSE 37.29 days (69.06→106.35) over the period,
  exceeding the ≤10-day threshold for either the top or second tier. Because there were
  also no decline years, the "2+ decline years" middle tier does not apply either →
  no listed tier fits → **0**.
- M11 Network Effects (6-year window, meets the ≥6-year threshold): latest 3-year
  revenue CAGR (FY23→FY26) = 52.4% vs prior 3-year-equivalent CAGR (FY21→FY23, 2-year
  span) = 73.5%. Latest is LOWER than prior, so the growth-accelerating condition fails.
  Selling/distribution expense is not separately broken out in the standalone P&L (only
  "Other Expenses" lumps selling, admin and other costs together) so the selling-%
  qualifier cannot be checked without guessing → **0, data gap noted, not guessed**.
- M12 Negative WC / Float: WC days negative in only 1 of 6 years (FY21); majority
  positive, and the three most recent years (FY24 68.51, FY25 59.04, FY26 80.27) all
  exceed the 45-day ceiling for even the lowest positive tier → **0**.

Moat classification: 3 tests present (M1, M4, M8) = **MODERATE**.

## DATA CONFIDENCE

6 years (FY21-FY26), standalone. Band 5-6 = lower confidence. FLAG: "may not have seen
full cycle" — Qualitek listed 29-Jan-2024 (BSE new-listing notice) and every year of the
built series sits inside a rising-rate-of-change capex and acquisition programme; no
downcycle or flat-revenue year has been observed for this entity.

## DEAL-BREAKER CHECK

1. Block A <8? Block A = 10. No.
2. **Block B <8? Block B = 5. TRIGGERED → max GOOD.**
3. Median ROCE <10%? Median = 10.02%. No (marginal — 0.02pp above the line).
4. Cumulative CFO/PAT <0.50? Ratio = 1.09. No.
5. Pledge >15%? NOT FOUND — cannot confirm or deny; carried as an open gap, not a
   triggered deal-breaker (never estimate a missing number into a trigger).
6. ND/EBITDA >3x (3.75x, true) AND IC <3x (4.80x, false)? Joint condition not met. No.
7. Revenue declined in a majority of years? No — 0 of 6 years declined.
8. PAT negative in any of the last 3 years (FY24-26)? No — all positive.
9. History <3 years? No — 6 years.

Only deal-breaker #2 fires. It caps classification at GOOD, but the classification
matrix outcome below (AVERAGE) already sits below that cap, so the cap is recorded but
non-binding.

## CLASSIFICATION

Core score = A(10) + B(5) + C(20) + D(6) + E(7) = **48/100**.
Moat score = **12/60**, 3 present, **MODERATE**.
Grand total = 48 + 12 = **60/160**.

Matrix: Core 40-59 → **AVERAGE**, regardless of moat tier.

## STRONGEST / WEAKEST BLOCK

Strongest: **Block C (Growth), 20/20** — standalone (organic, parent-only) revenue
CAGR 60.47% and PAT CAGR 76.8% FY21-FY26, zero decline years, PAT compounding faster
than revenue.

Weakest: **Block B (Cash Generation), 5/20** — every year FCF-negative (6 of 6), FCF
cumulatively -69.6 Cr against cumulative PAT of +22.1 Cr, working capital days swinging
+145.76 days over the period as payables normalised from an unsustainably stretched
FY21 base while receivables stayed elevated. This is the deal-breaker driver.

## BLOCK B TREND

**Deteriorating.** The one number that shows it: WC days moved from -65.49 (FY21) to
+80.27 (FY26), and FCF worsened every single year in absolute terms as the capex
programme (funded by IPO and preferential-issue proceeds) accelerated (FY26 capex
₹38.1 Cr standalone vs FY21 ₹6.1 Cr). This feeds FLAG-CASH.

## FLAGS

- **FLAG-GATE0**: classification AVERAGE. Historical depressor is Block B (cash
  conversion), not Block A or C — the underlying operating growth and profitability
  are both strong (Block C 20/20, EBITDA margin expansion). The depressor is a
  capex-funded capacity ramp outrunning operating cash flow, which the pipeline should
  read as a GROWTH-INDUCED cash-conversion pattern (per LBF2's own framing) pending the
  claw-back check on receivables ageing and the government/PPP customer share that LBF2
  calls for — this stage has no receivables-ageing schedule to confirm or refute that
  classification.
- **FLAG-CASH**: see Block B trend above — deteriorating, driven by WC days and FCF,
  not by profitability.

## DATA NOTES

- Screener FY21/FY22 standalone P&L figures (net profit ₹0.16 Cr / ₹0.42 Cr) do not
  match the DRHP's own RESTATED standalone financials (PAT ₹46.11 lakh / ₹113.57 lakh)
  for the same years. The DRHP restated figures were used throughout this scorecard as
  the audited, restatement-adjusted source; the screener CSV figures were not used for
  FY21-23 P&L or balance sheet inputs. Flagged for the downstream verifier.
- FY24 CFO (₹553.51 lakh) is reconstructed from the components printed in the FY25
  results filing's cash-flow statement (operating-profit-before-WC-changes-adjusted row
  570.83 less tax paid 17.32); the printed FY24 total-CFO figure itself is OCR-garbled
  in the extraction ("5533;") and was not used directly.
- ROCE basis is not uniform across the 6-year series: FY21-23 and FY25-26 use the
  company's own EBIT/(equity+borrowings) definition (source-anchored, per formula rule);
  FY24 alone is computed under the stage's EBIT/(TA-CL) formula because no source figure
  exists for FY24. This affects A1/A2/A4 marginally; the qualitative read (ROCE rising
  FY21-24, falling FY25-26) is not affected.
- E4 used the STANDALONE contingent-liability note only (₹2,133.00 lakh corporate
  guarantee to ITCPL). The CONSOLIDATED note carries a larger, partly cross-guaranteed
  figure (ITCPL guaranteeing Qualitek back for ₹4,911.00 lakh, plus ₹96.69 lakh of
  subsidiary tax demands) that was not scored, to avoid double-counting the same
  intercompany debt from both directions.
- M2, M5, M6, M9 scored 0 / PEER DATA NEEDED: the collector's peer screener sheets
  (VIMTALABS, METROPOLIS, KRSNAA — Profit & Loss, Balance Sheet, Cash Flow, Quarters)
  came back empty (B00 collector warning); only qualitative peer earnings-call
  transcripts are in the corpus, which cannot support the quantitative peer-median tests
  these moat items require.
- No promoter pledge figure exists in the corpus (shareholding/ folder empty per B00);
  E3 scored 0 as N/A, not as a confirmed >15% pledge. This is an open evidence gap, not
  a finding.
- No credit rating exists in the corpus or (per B00) on BSE filings; Block D used only
  company-reported ratios, no rating-based cross-check was possible.

## ANALYST NOTE

Qualitek's standalone (parent-only) numbers show a genuinely strong organic operating
story: 60% revenue CAGR, EBITDA margin up 8pp, zero decline years, all funded so far by
IPO and preferential-issue capital rather than debt-fuelled overreach (D/E still 0.45).
The scorecard's AVERAGE result and its one deal-breaker both trace to the SAME root
cause: the company is spending capital (mostly capex, some acquisitions consolidated
separately) faster than its standalone entity generates cash, which is a normal pattern
for a recently-listed SME funding a capacity ramp, but it is indistinguishable at this
stage from a company that cannot self-fund its own growth. LBF2 already flags this exact
question (GROWTH-INDUCED vs STRUCTURAL) and this stage cannot resolve it: the missing
piece is receivables ageing and the government/PPP customer share, neither of which is
in the corpus read here. Block A's ROCE picture (rising FY21→FY24 to 15.41%, then
falling to 7.4% by FY26) is worth carrying forward too: it could mean capital deployed
into FY25-26 capex/acquisitions has not yet turned productive (a J-curve read, favourable
if temporary) or that returns are structurally diluting as the base grows (unfavourable
if durable). Six years of data, all inside a single rising-investment regime since a
Jan-2024 listing, cannot distinguish the two; that is exactly the "may not have seen
full cycle" flag this stage is required to raise.

```yaml
stage: B01-gate0
company: "QUALITEK"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
input_gaps:
  - "No filed shareholding pattern in the corpus (shareholding/ empty per B00): promoter pledge (E3) and the FII+DII split are both unconfirmed. E3 scored 0 as N/A, not as a >15% pledge finding."
  - "Peer screener financial sheets (VIMTALABS, METROPOLIS, KRSNAA: Profit & Loss, Balance Sheet, Cash Flow, Quarters) came back empty per B00 collector warning; M2, M5, M6, M9 scored 0 / PEER DATA NEEDED, not a finding of no moat."
  - "No credit rating in the corpus or on BSE filings per B00; Block D has no rating cross-check."
  - "Final prospectus (RHP) absent; DRHP restated FY21-23 financials used, unconfirmed against any later restatement."
  - "Consolidated basis has only 2 annual data points (FY25, FY26); no consolidated CAGR/trend is computable. This stage scores standalone FY21-FY26 (6 years) instead, per LBF1."
flags:
  - {type: FLAG-GATE0, reason: "Classification AVERAGE. Depressor is Block B (cash conversion, cumulative FCF/PAT -3.15x, 0 of 6 years FCF-positive), not Block A or C (growth 20/20, EBITDA margin +8pp). Likely GROWTH-INDUCED (capex ramp, IPO/pref-issue funded) per LBF2's own framing, but unconfirmed without receivables ageing and PPP/government customer share, neither in this stage's corpus."}
  - {type: FLAG-CASH, reason: "Deteriorating. WC days moved -65.49 (FY21) to +80.27 (FY26), a +145.76 day swing; FCF worsened every year in absolute terms (-470.95 lakh FY21 to -3,095.74 lakh FY26) as standalone capex accelerated 6.3x over the period."}
  - {type: FLAG-DATA-CONFIDENCE, reason: "6 years of history (FY21-FY26), all inside a single post-IPO (listed Jan-2024) rising-investment regime. No downcycle or flat year observed. 'May not have seen full cycle.'"}
data_years: 6
fy_range: "FY21 to FY26"
blocks: {A: 10, B: 5, C: 20, D: 6, E: 7}
core_score: 48
moat_score: 12
grand_total: 60
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 (actual 5) -> max GOOD. Non-binding: matrix outcome AVERAGE already sits below the GOOD cap."
history_downgrade: false
data_notes:
  - "Screener FY21/FY22 standalone P&L (net profit Rs 0.16 Cr / Rs 0.42 Cr) conflicts with DRHP restated standalone PAT (Rs 46.11 lakh / Rs 113.57 lakh) for the same years. DRHP restated figures used throughout; screener FY21-23 P&L/BS not used."
  - "FY24 CFO (Rs 553.51 lakh) reconstructed from FY25 results filing cash-flow components (operating profit before WC changes 570.83 less tax paid 17.32); the printed FY24 CFO total is OCR-garbled in the extraction and was not used directly."
  - "ROCE basis not uniform across the series: FY21-23 and FY25-26 use the company's/DRHP's own EBIT/(equity+borrowings) definition (source-anchored); FY24 alone computed under the stage's EBIT/(Total Assets-Current Liabilities) formula, no source figure existed. Qualitative trend (rise to FY24, fall since) unaffected."
  - "E4 used the standalone-only contingent liability (Rs 2,133.00 lakh corporate guarantee to ITCPL); the consolidated note's larger, partly cross-guaranteed figure (Rs 4,911.00 lakh reverse guarantee plus Rs 96.69 lakh subsidiary tax demands) was not double-counted."
  - "PEER DATA NEEDED: M2 (cost advantage), M5 (scale/dominance), M6 (tech/R&D), M9 (brand) all scored 0 because peer screener P&L/BS/CF/Quarters sheets were empty per B00; only qualitative peer concall transcripts exist in the corpus."
block_b_trend: "deteriorating - WC days -65.49 (FY21) to +80.27 (FY26), a +145.76 day swing; FCF negative and worsening every year, 0 of 6 years FCF-positive"
analyst_note: "Standalone (parent-only, organic) growth is strong: 60% revenue CAGR, EBITDA margin +8pp, zero decline years, D/E still 0.45. The AVERAGE classification and its one deal-breaker both trace to one cause: capex (IPO/pref-issue funded) outrunning standalone cash generation, the exact GROWTH-INDUCED-vs-STRUCTURAL question LBF2 already raises and this stage cannot resolve (no receivables ageing or PPP/government customer share in this corpus). ROCE rose FY21-FY24 (6.4% to 15.4%) then fell to 7.4% by FY26: could be a J-curve on FY25-26 capital deployed, or durable dilution as the base grows. Six years, all inside one post-listing investment ramp since Jan-2024, cannot distinguish the two - hence the full-cycle flag."
```
