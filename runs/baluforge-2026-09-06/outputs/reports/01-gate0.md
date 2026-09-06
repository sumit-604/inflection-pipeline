# GATE 0 QUANTITATIVE SCORECARD — Balu Forge Industries Ltd (BALUFORGE)
Run date: 2026-09-06 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 6 years (FY2021 to FY2026). Scoring adapted to 6-year history.

Data sources: screener.in Data_Sheet.csv (screener-data; the Profit_Loss/
Balance_Sheet/Cash_Flow/Quarters/Customization CSVs in the same export were
blank templates and contributed nothing), Annual Report FY2025 (216 pp) and
Annual Report FY2024 (232 pp), and 3 peer screener Data_Sheet.csv files
(HAPPYFORGE, MMFL, RKFORGE — supplied "for context only," used for the 3
moat tests that explicitly require peer data: M2, M5, M9). No results
filings, rating report, shareholding-pattern filing, or concalls are in the
corpus, per B00. FY2026 figures in screener-data are unaudited full-year
aggregates; no FY2026 Annual Report exists yet, so FY2026 cannot be
independently verified against audited statements.

## BASIS NOTES (apply throughout; read before the numbers below)
1. **Change in Inventory sign.** Screener's Data_Sheet reports "Change in
   Inventory" such that it must be SUBTRACTED from Raw Material + Power&Fuel
   + Other Mfr + Employee + S&A + Other Expenses to reconcile to reported
   PBT. Verified by back-solving PBT across all 6 years (screener-data);
   matches to the rupee. Total Expenses = RM+P&F+OtherMfr+Emp+S&A+OtherExp
   − ΔInventory.
2. **EBIT** = PBT + Interest expense throughout (Depreciation already
   deducted in arriving at PBT; Other Income is included, as no clean
   operating-only split is available).
3. **EBITDA (for D1 leverage ratio only)** = EBIT + Depreciation (includes
   Other Income). A SEPARATE "Operating EBITDA" (excludes Other Income,
   standard operating-margin basis: Sales − Total Expenses per note 1) is
   used for M1/M2/M9 peer-comparable margin tests. Two different
   constructs, each labelled where used.
4. **Capital Employed (ROCE denominator).** FY2023–FY2025: Total Assets −
   Total Current Liabilities, taken directly off the AR consolidated balance
   sheet (exact figures, anchored). FY2021, FY2022, FY2026: no AR balance
   sheet is in the corpus (no AR for FY21/22; FY2026 AR not yet published),
   so Capital Employed = Net Worth + Total Borrowings (screener-data), a
   DIFFERENT and less precise basis that does not net out working-capital
   current liabilities. This basis switch is flagged where it affects trend
   scoring (A4).
5. **Capex proxy.** Screener-data does not isolate capex from total
   investing cash flow. AR confirms "(Increase)/decrease PPE (net)" ≈ "Net
   cash used in investing activities" for FY2023–FY2025 (Investments line
   ≤ ₹20.12 lakh, immaterial). FCF for FY2021, FY2022, FY2026 uses total
   Cash from Investing Activity as the capex proxy, unverified against an
   AR for those 3 years.
6. **Trade Payables** is not a line item in screener Data_Sheet. FY2023–
   FY2025 payables are sourced from AR consolidated balance-sheet notes.
   FY2021, FY2022, FY2026 WC Days cannot be computed (no payables data);
   B4 and M12 use the FY2023–FY2025 window only (3 years, not 6).

---

## BLOCK A: RETURN ON CAPITAL (max 20)

| FY | EBIT (₹cr) | Capital Employed (₹cr) | Basis | ROCE |
|---|---|---|---|---|
| 2021 | 16.35 (PBT 9.74+Int 6.61, screener-data) | 103.52 (NW 77.52+Borrow 26.0, screener-data) | proxy | 15.79% |
| 2022 | 44.32 (39.09+5.23, screener-data) | 206.02 (158.62+47.4, screener-data) | proxy | 21.51% |
| 2023 | 61.09 (50.56+10.53, screener-data; matches AR2024 p.177 consol PBT 5,056.53+FC 1,053.16 lakh) | 210.16 (AR2024 p.176 consol: TA 37,075.70 − CL 16,059.56 lakh) | AR-precise | 29.07% |
| 2024 | 127.31 (113.67+13.64, screener-data) | 578.73 (AR2025 p.160 consol: TA 71,246.06 − CL 13,372.55 lakh) | AR-precise | 22.00% |
| 2025 | 264.90 (253.94+10.96, screener-data; matches AR2025 p.161 consol PBT 25,394.26+FC 1,095.70 lakh) | 1,070.46 (AR2025 p.160 consol: TA 1,25,219.02 − CL 18,172.60 lakh) | AR-precise | 24.75% |
| 2026 | 322.49 (306.04+16.45, screener-data) | 1,746.39 (1,594.52+151.87, screener-data) | proxy | 18.47% |

- **A1 Median ROCE** = 21.76% (sorted: 15.79/18.47/21.51/22.00/24.75/29.07,
  median of middle two) → band 20–24.9 → **score 4**
- **A2 Minimum single-year ROCE** = 15.79% (FY2021) → ≥15% → **score 5**
- **A3 Median ROE** = 23.38% (ROE by year: FY21 9.83% [closing NW only, no
  FY2020 opening NW in corpus, stated per rule]; FY22 25.27%; FY23 21.85%;
  FY24 24.91%; FY25 25.39%; FY26 19.56%; PAT and Net Worth all
  screener-data) → ≥20% → **score 5**
- **A4 ROCE trend, latest vs earliest** = 18.47% (FY26) vs 15.79% (FY21):
  latest ≥ earliest → **score 5**. Caveat: both endpoints use the proxy
  Capital Employed basis (note 4 above), so this is an internally
  consistent comparison but not on the AR-precise basis used for FY23-25.

**Block A total = 19/20**

## BLOCK B: CASH GENERATION QUALITY (max 20)

| FY | CFO (₹cr) | PAT (₹cr) | Capex proxy (₹cr) | FCF (₹cr) |
|---|---|---|---|---|
| 2021 | 17.33 | 7.62 | 3.23 | 14.10 |
| 2022 | -57.74 | 29.84 | 7.67 | -65.41 |
| 2023 | 26.16 | 38.91 | 21.25 | 4.91 |
| 2024 | -31.73 | 93.49 | 134.11 | -165.84 |
| 2025 | 148.24 | 203.86 | 416.63 | -268.39 |
| 2026 | 31.70 | 258.89 | 353.96 | -322.26 |

(all screener-data; CFO/Investing FY2024 and FY2025 verified exact against
AR2025 p.163 consolidated cash flow statement: CFO ₹(3,173.16) lakh FY24 and
₹14,824.16 lakh FY25, Net cash used in investing ₹(13,411.31) lakh FY24 and
₹(41,662.54) lakh FY25)

- Cumulative CFO = ₹133.96cr; Cumulative PAT = ₹632.61cr
- **B1 Cumulative CFO ÷ Cumulative PAT** = 0.21 → <0.50 → **score 0**
- Cumulative FCF = −₹802.89cr
- **B2 FCF-positive years** = 2 of 6 (FY21, FY23) = 33% → <50% → **score 0**
- **B3 Cumulative FCF ÷ Cumulative PAT** = −1.27 → negative → **score 0**
- **B4 Change in WC Days, latest vs earliest** (FY2023–FY2025 window only;
  no Trade Payables data for FY21/22/26, see basis note 6):
  - FY2023: RecvDays 235.28 + InvDays 38.91 − PayDays 73.18 = **201.01**
    days (Payables ₹65.50cr = AR2024 p.176 consol, 37.45+6,512.92 lakh)
  - FY2024: RecvDays 142.49 + InvDays 58.32 − PayDays 52.53 = **148.28**
    days (Payables ₹80.58cr = AR2025 p.160 consol, 52.65+8,005.28 lakh)
  - FY2025: RecvDays 129.36 + InvDays 38.76 − PayDays 46.64 = **121.48**
    days (Payables ₹118.01cr = AR2025 p.160 consol, 50.02+11,751.00 lakh)
  - Change: 121.48 − 201.01 = **−79.5 days** (decreased) → decreased >5 days
    → **score 5**

**Block B total = 5/20 — WEAKEST BLOCK.** Deal-breaker #2 (Block B<8) and
deal-breaker #4 (cumulative CFO/PAT<0.50) both fire; see CLASSIFICATION.

## BLOCK C: GROWTH (max 20)

- Revenue CAGR FY21→FY26 (5yr): (1,107.37/142.09)^(1/5)−1 = **50.79%**
  (screener-data) → ≥20% → **C1 score 5**
- PAT CAGR FY21→FY26 (5yr): (258.89/7.62)^(1/5)−1 = **102.42%**
  (screener-data) → ≥20% → **C2 score 5**
- Positive YoY revenue years: 5 of 5 transitions positive (FY22 through
  FY26 all grew vs prior year, screener-data) = 100% → **C3 score 5**
- **C4** PAT CAGR − Revenue CAGR = 102.42% − 50.79% = **+51.6pp** → ≥+3pp →
  **score 5**

**Block C total = 20/20 — STRONGEST BLOCK (perfect score).**

## BLOCK D: BALANCE SHEET STRENGTH (max 20)

- **D1 Net Debt ÷ EBITDA (latest, FY2026)**: Net Debt = Borrowings 151.87 −
  Cash&Bank 89.0 = ₹62.87cr (screener-data); EBITDA = EBIT 322.49 + Dep 9.96
  = ₹332.45cr (per basis note 3) → 0.189x → 0–1.0x → **score 4**
- **D2 Interest Coverage EBIT÷Interest (latest, FY2026)**: 322.49/16.45 =
  **19.60x** (screener-data) → ≥10x → **score 5**
- **D3 Debt÷Equity (latest, FY2026)**: 151.87/1,594.52 = **0.095x**
  (screener-data) → <0.1 → **score 5**
- **D4 Current Ratio**: screener Data_Sheet does not split current from
  non-current assets/liabilities for FY2026 (no FY2026 AR exists to supply
  the split) → marked N/A for FY2026. Latest year with a full split is
  FY2025 (AR2025 p.160 consolidated: Total Current Assets 56,768.07 ÷ Total
  Current Liabilities 18,172.60 lakh = **3.12x**) → ≥2.0 → **score 5**.
  Period mismatch flagged: D1–D3 = FY2026 basis, D4 = FY2025 basis.

**Block D total = 19/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (max 20)

- **E1 Promoter holding (latest available)** = **55.25%** as on 31 March
  2025 (AR2025 p.60, Corporate Governance shareholding pattern; no
  post-March-2025 shareholding filing exists in the corpus, 18 months stale
  vs run date) → 50–59.9% → **score 4**
- **E2 Promoter holding change** (FY2023 65.40% → FY2025 55.25%, AR2024
  p.149 / AR2025 p.60/p.132 equity notes; earliest data point available is
  FY2023, so this is a 2-year-elapsed / 3-snapshot window, not a full
  3-year-elapsed window — no FY2022 promoter % in corpus) = **−10.15pp** →
  decreased >3% → **score 0**. Note: AR2025 p.132 states the decline is
  driven by new shares issued to non-promoter investors (dilutive
  capital raise funding the capex program), not promoter share sales;
  promoters' absolute share count rose. Scored mechanically per rule
  regardless.
- **E3 Promoter pledge (latest)**: not disclosed in either AR text extract
  and no shareholding-pattern filing is in the corpus → **N/A (not in
  provided data)** → **score 0**
- **E4 Contingent liabilities ÷ Net Worth (latest)**: AR2025 p.148,
  standalone Note 46 "Contingent Liabilities and Legal Cases" shows Bank
  guarantee = Nil for both FY2025 and FY2024; no other contingent-liability
  line item is disclosed (Capital Commitments of ₹2,569.23 lakh FY2025 /
  ₹5,499.92 lakh FY2024 are commitments, not contingent liabilities, and are
  excluded per Ind AS classification) → ratio ≈ **0%** (standalone basis) →
  <5% → **score 5**

**Block E total = 9/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (max 60)

Peer set used for M2/M5/M9 (PEER DATA provided, "context only" per
orchestrator — only 3 named peers, not the full listed forging segment;
flagged as PEER DATA LIMITED, not "PEER DATA NEEDED," since some data
exists): Happy Forgings (HAPPYFORGE), MM Forgings (MMFL), Ramkrishna
Forgings (RKFORGE), all peer screener-data, FY2025.

Operating EBITDA margin (Sales − Total Expenses per basis note 1, excludes
Other Income), FY2025:
- BALUFORGE: 27.19% (923.62 sales, 672.51 expenses; PBT-reconciled)
- HAPPYFORGE: 28.87% | MMFL: 19.41% | RKFORGE: 13.90% → peer median 19.41%

Gross-margin proxy (Revenue − Material Cost consumed) ÷ Revenue, FY2025:
- BALUFORGE: 34.75% | HAPPYFORGE: 58.00% | MMFL: 56.60% | RKFORGE: 50.44%
  → peer median 56.60%

Market cap (screener-data): HAPPYFORGE ₹21,126.68cr > RKFORGE ₹12,767.39cr
> BALUFORGE ₹6,969.11cr > MMFL ₹3,042.22cr.

| # | Test | Result | Score |
|---|---|---|---|
| M1 | Pricing Power | Operating margin 8.61%(FY21)→27.05%(FY26), +18.4pp expansion, AND revenue CAGR 50.8%≥10% | **5** |
| M2 | Cost Advantage vs peer median | 27.19% vs 19.41% peer median = +7.78pp above | **5** |
| M3 | Capital Efficiency (latest, FY26) | FAT=Rev/NetBlock=1,107.37/546.58=2.03x, ROCE=18.47%: FAT>2x AND ROCE>15% (see caveat below) | **3** |
| M4 | Customer Stickiness | 0 revenue-decline years, BUT receivable days NOT stable ±10 (156→235→142→129→140 across FY21-26) | **3** |
| M5 | Scale & Dominance | BALUFORGE 3rd of 4 by mcap (top-3), margin 2nd of 4 (top-2) — PEER DATA LIMITED to 3 named peers | **3** |
| M6 | Technology / R&D | AR describes an R&D centre qualitatively; no R&D/Revenue % disclosed anywhere in corpus | **0**, N/A |
| M7 | Regulatory / License | Unregulated segment (forging/components, no licence/quota constraint identified) | **0** |
| M8 | Distribution | B2B component manufacturer; no distribution-reach metric disclosed | **0** |
| M9 | Brand | GM proxy 34.75% vs peer median 56.60%: at/below peer median | **0** |
| M10 | Switching Costs | Revenue grew every year AND receivable days fell ~15.8 days over the period (well within "rose ≤10 days") | **5** |
| M11 | Network Effects (6yr window, qualifies for two-window test) | Latest 3yr CAGR (FY23→26) 50.2% < prior 3yr CAGR (FY21→24) 58.0% (deceleration, fails top tier); overall 5yr CAGR 50.8%≥20% AND selling-exp % of revenue declining (10.19%→5.01%, FY21→FY25; FY26 S&A blank in screener-data, excluded from this trend) | **3** |
| M12 | Negative WC / Float | WC Days FY23-25 window: 201/148/121 days, all >45 | **0** |

Moat score = 5+5+3+3+3+0+0+0+0+5+3+0 = **27/60**

Moats "present" (score ≥3): M1, M2, M3, M4, M5, M10, M11 = **7 tests**

**Moat classification: 7 present ≥ 6 → FORTRESS**

Moat profile bars:
```
M1  Pricing Power      █████ 5
M2  Cost Advantage     █████ 5
M3  Capital Efficiency ███   3
M4  Cust. Stickiness   ███   3
M5  Scale & Dominance  ███   3
M6  Tech/R&D                 0
M7  Regulatory               0
M8  Distribution             0
M9  Brand                    0
M10 Switching Costs    █████ 5
M11 Network Effects    ███   3
M12 Neg. WC/Float            0
```

---

## CLASSIFICATION

- Core score (A+B+C+D) = 19+5+20+19 = **63/80** (band: 60–79)
- Moat class = FORTRESS
- Matrix lookup (Core 60-79 + FORTRESS) → GOOD+ **before deal-breaker
  overrides**

Deal-breaker check:
1. Block A<8? No (19). Not triggered.
2. **Block B<8? YES (5). → caps max GOOD.**
3. Median ROCE<10%? No (21.76%). Not triggered.
4. **Cumulative CFO/PAT<0.50? YES (0.21). → caps max AVERAGE.**
5. Pledge>15%? Unknown (N/A, not in provided data). Not triggered (cannot
   confirm).
6. ND/EBITDA>3x AND IC<3x? No (0.19x and 19.60x). Not triggered.
7. Revenue declined majority of years? No (0 of 5 transitions). Not
   triggered.
8. PAT negative in any of last 3 years? No (all positive). Not triggered.
9. History<3 years? No (6 years). Not triggered.

Two deal-breakers fire (#2 and #4); the tighter cap governs.

**FINAL CLASSIFICATION: AVERAGE** (capped down from matrix-implied GOOD+ by
deal-breaker #4, cumulative CFO/PAT = 0.21, itself reinforced by
deal-breaker #2, Block B = 5/20)

Data confidence: 6 years of P&L/CFO history → 5–6 band → **"may not have
seen full cycle"** flag (no automatic tier downgrade at this band; that
only applies at 3-4 years). Separately, the ROCE/WC-days/payables/current-
ratio precision is uneven across the 6 years (AR-precise for FY23-25 only,
screener-proxy for FY21/22/26; see basis notes), and the two most recent
data points (FY2026 full year, per the concall decks and screener
aggregation) postdate the newest Annual Report in the corpus (FY2025),
consistent with the B00 CORPUS GAPPED-FRESHNESS verdict.

Strongest block: **C (Growth), 20/20, perfect score.**
Weakest block: **B (Cash Generation Quality), 5/20**, driven by two
negative-CFO years (FY22 −57.74, FY24 −31.73) despite profit growth in
both, and by capex (proxy) outrunning CFO in 4 of 6 years.

**Grand total (A+B+C+D+E+F) = 19+5+20+19+9+27 = 99** (of 160 max)

## DECISION LINE

Balu Forge screens AVERAGE, not because the business is growing slowly (it
is not: 50.8% revenue CAGR, 102.4% PAT CAGR, FORTRESS-tier moat count) but
because cash has not followed profit. Cumulative CFO is only 21% of
cumulative PAT over FY21-26, and free cash flow was negative in 4 of the
last 5 years as a large capex program ran ahead of operating cash
generation. The deal-breaker rule caps the classification at AVERAGE
regardless of the growth and moat scores. FLAG-GATE0 is raised.

---

## BLOCK B TREND (most recent-year signal, feeds FLAG-CASH downstream)

**Deteriorating.** CFO/PAT cash-conversion ratio was 72.7% in FY2025
(148.24/203.86, screener-data) — the best year in the series — but
collapsed to 12.2% in FY2026 (31.70/258.89, screener-data) even as PAT grew
27%. Receivable days (Revenue basis, no payables data for FY26) rose from
129.36 (FY25) to 140.14 (FY26), and inventory days rose from 38.76 to
47.90, both moving the wrong way in the one year for which there is no AR
to independently verify the screener aggregate.

## DATA NOTES

1. Change-in-Inventory sign convention (see basis note 1) verified against
   PBT for all 6 years, screener-data.
2. ROCE basis differs by year: AR-precise Capital Employed for FY23-25 vs
   proxy (Net Worth + Total Borrowings) for FY21/22/26 — no AR exists for
   the latter years in this corpus (see basis note 4).
3. Trade Payables (for WC Days, B4, M12) sourced from AR only; not
   available for FY21/22/26 (see basis note 6). B4 and M12 use the FY23-25
   window, not the full 6-year history used elsewhere.
4. Capex proxy = total Cash from Investing Activity for FY21/22/26 (no AR
   to isolate the PPE-purchase line for those years); confirmed near-exact
   for FY23-25 against AR (Investments line ≤₹20.12 lakh).
5. S&A (Selling and admin) is blank in screener-data for FY2026; M11's
   selling-expense-ratio trend is computed through FY2025 only.
6. E1/E2 promoter holding figures are all "as at 31 March 2025" or earlier
   (AR2025 p.60, p.132; AR2024 p.77, p.149); no shareholding-pattern filing
   newer than March 2025 is in the corpus, consistent with B00's declared
   input gap.
7. E2's mechanical score (0) reflects a dilutive equity/warrant raise to
   non-promoter investors that funded the capex program (AR2025 p.132),
   not promoter share sales; promoters' absolute share count increased over
   the period. Flagged as an interpretive caveat; scored per the rule
   regardless.
8. E3 promoter pledge: no pledge disclosure located in either AR text
   extract; marked N/A, scored 0.
9. E4 contingent liabilities computed on a standalone basis (AR2025 p.148,
   Note 46); a separately-stated consolidated contingent-liabilities note
   was not located in the extract. Numerator is 0 either way.
10. D4 Current Ratio uses FY2025 (AR2025 p.160, 3.12x) rather than FY2026,
    because screener-data does not split current/non-current assets or
    liabilities and no FY2026 AR exists. D1-D3 use the true latest year
    (FY2026, screener-data). Period mismatch flagged.
11. M5/M2/M9 peer comparisons use only 3 named peers (Happy Forgings, MM
    Forgings, Ramkrishna Forgings), supplied "for context only"; broader
    segment confirmation not attempted. Labelled PEER DATA LIMITED rather
    than PEER DATA NEEDED since partial peer data does exist.
12. M6 Technology/R&D: R&D spend as % of revenue is not disclosed anywhere
    in the corpus (only qualitative R&D-centre description); scored 0,
    N/A.
13. M9 Brand: gross-margin proxy places BALUFORGE well below the 3-peer
    median (34.75% vs 56.60%), likely reflecting a more material-intensive
    product mix (e.g., crankshaft/forging content) rather than a direct
    read on brand pricing power; flagged as an interpretive caveat for
    downstream stages, not a correction to the mechanical score.
14. No loss-to-profit swing occurred in the FY21-26 window (PAT was
    positive in every year); the swing rule is not triggered.
