# GATE 0 SCORECARD — KRONOX (Kronox Lab Sciences Ltd)
Run date: 2026-08-30 | Model: claude-sonnet-5 | Mode: pipeline (no human loop)

Data available: 4 years (FY23 to FY26). Scoring adapted to 4-year history.
No KRONOX screener CSV in this run. Built entirely from: AR FY26 financial
statements and Financial Snapshot table (annual-report txt), FY26 audited
Q4+full-year results filing (results 4c8de5ae txt), and Q1 FY27 results
filing (results 03380acb txt, used only for spear-fact cross-check, not
scored — quarterly data is outside the annual scorecard).

## SOURCE NOTE ON YEAR MAPPING
The AR's "Financial Snapshot" table (AR p.11) is a genuine columnar table,
header-ordered FY26/FY25/FY24/FY23, and is reliable for every row in it
(margins, ROCE%, ROE%, FAT, Cash Conversion Cycle, Net Worth, Current
Ratio, CFO/CFI/CFF, EPS). The "Revenue Growth" bar chart on AR p.10 is
NOT in this table; its four values (10,121.9 / 9,557.7 / 8,986.2 /
10,019.3, all Rs lakh) came back from PDF text extraction in scrambled,
non-year-ordered form (typical of chart-derived OCR). Year assignment was
inferred by elimination: FY26 and FY25 values were cross-confirmed exactly
against the audited results filing (Revenue from Operations FY26 =
10,122.0, FY25 = 10,018.4, results FY26 p.2) and against operator company
memory (FY24 = Rs 89.86 cr = 8,986.2). That leaves 9,557.7 as FY23 by
elimination — moderate confidence, flagged in data_notes.

## PAT BY YEAR
FY26 = Rs 2,766.0 lakh, FY25 = Rs 2,545.7 lakh — both exact, audited
(results FY26 p.2, Statement of Profit and Loss).
FY24 = Rs 2,155.7 lakh, FY23 = Rs 1,595.5 lakh — computed as reported EPS
(AR p.11: FY24 = 5.81, FY23 = 4.30) × 371.04 lakh shares outstanding
(constant across the AR's disclosed periods, AR p.104 Note 12
Reconciliation of Shares Outstanding). Moderate confidence: FY23/FY24
audited P&L statements are not held in this corpus (no AR FY24/FY25).

---

## BLOCK A: RETURN ON CAPITAL (max 20)
Source: AR p.11 Financial Snapshot, company's own ROCE%/ROE%, used directly
per rule (source provides its own ROCE).

| Metric | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| ROCE % (AR p.11) | 49.46% | 43.15% | 38.03% | 32.22% |
| ROE % computed (PAT ÷ avg Net Worth; FY23 uses closing, opening N/A) | 35.65% | 38.83% | 32.55% | 26.83% |

Net worth (closing, AR p.11): FY23=4,475.08, FY24=6,630.50, FY25=9,010.50,
FY26=11,612.71 (Rs lakh).

- A1 Median ROCE = 40.59% (median of 32.22/38.03/43.15/49.46) → ≥25% → **5**
- A2 Minimum single-year ROCE = 32.22% (FY26) → ≥15% → **5**
- A3 Median ROE = 34.10% (median of computed 26.83/32.55/35.65/38.83) → ≥20% → **5**
- A4 ROCE trend, latest (32.22%) vs earliest (49.46%): decline of 17.24pp → >5pp decline → **0**

**Block A = 15/20.** ROCE and ROE remain elite in absolute terms but have
declined every single year of the available window — a real trend, not
noise (A4 note).

---

## BLOCK B: CASH GENERATION QUALITY (max 20)
CFO (AR p.11, Financial Snapshot): FY23=1,966.50, FY24=1,741.51,
FY25=3,069.67, FY26=2,389.22 (Rs lakh).
Cumulative CFO (FY23-FY26) = 9,166.90 lakh.
Cumulative PAT (FY23-FY26) = 9,062.90 lakh (see PAT-by-year note above).

- B1 Cumulative CFO ÷ Cumulative PAT = 9,166.90 / 9,062.90 = 1.011 → ≥1.00 → **5**

Capex (Purchase of PPE, cash flow statement) is only available for FY25
(Rs 310.4 lakh) and FY26 (Rs 330.7 lakh) — AR p.103/104 cash flow
statement and results FY26 p.4 (consistent between both sources). FY23/FY24
capex is NOT FOUND (no AR FY24/FY25 held in this corpus). B2/B3 are
therefore scored on the 2-year window where FCF is computable, stated
explicitly.

FCF FY25 = 3,069.67 − 310.4 = 2,759.27 lakh. FCF FY26 = 2,389.22 − 330.7 =
2,058.52 lakh. Both positive.

- B2 FCF-positive years as proportion (of the 2 years computable: FY25, FY26) = 2/2 = 100% → **5** (flag: only 2 of 4 years testable)
- B3 Cumulative FCF (FY25+FY26 = 4,817.79) ÷ Cumulative PAT (same 2 years: 2,545.7+2,766.0 = 5,311.7) = 0.907 → ≥0.60 → **5** (window matched to FCF availability, not the full 4-year PAT)
- B4 Change in WC Days (AR p.11 "Cash Conversion Cycle", used as WC-days proxy: Receivable + Inventory − Payable days): FY23=74, FY24=96, FY25=77, FY26=83. Latest (83) vs earliest (74): increased 9 days → increased 5-15 days → **1**

**Block B = 16/20.**

Block B trend: **deteriorating** in the latest year — CFO ÷ PAT fell from
1.21x (FY25: 3,069.67/2,545.7) to 0.86x (FY26: 2,389.22/2,766.0), and WC
days rose from 77 to 83 over the same year.

---

## BLOCK C: GROWTH (max 20)
Revenue (Rs lakh): FY23=9,557.7 (AR p.10 chart, inferred — see source
note), FY24=8,986.2 (AR p.10 chart, matches company memory), FY25=10,018.4
(results FY26 p.2, exact), FY26=10,122.0 (results FY26 p.2, exact).

- C1 Revenue CAGR (FY23→FY26, 3yr) = (10,122.0/9,557.7)^(1/3)−1 = 1.93% → <5% → **0**
- C2 PAT CAGR (FY23→FY26, 3yr) = (2,766.0/1,595.5)^(1/3)−1 = 20.15% → ≥20% → **5**
- C3 Positive YoY revenue years: FY23→24 declined (9,557.7→8,986.2), FY24→25 grew, FY25→26 grew = 2 of 3 = 66.7% → 50-74% band → **1**
- C4 PAT CAGR minus Revenue CAGR = 20.15% − 1.93% = +18.2pp → ≥+3pp → **5**

**Block C = 11/20.** Margin-led, not volume-led: EBITDA margin nearly
doubled (22.72%→33.86%, AR p.11) while revenue barely moved. Consistent
with the transition thesis (owner-caused growth stall, not an economic
ceiling).

Deal-breaker #7 check (revenue declined in majority of years): only 1 of 3
YoY transitions declined (FY23→24) — not a majority. Not triggered.
Deal-breaker #8 check (PAT negative in any of last 3 years): PAT positive
and rising every year. Not triggered.

---

## BLOCK D: BALANCE SHEET STRENGTH (max 20)
Balance sheet figures (Rs lakh, FY26/FY25) from results FY26 p.3 (Statement
of Assets and Liabilities) and AR notes (cross-matching).

Total borrowings FY26 = 100.4 (non-current) + 60.3 (current) = 160.7.
FY25 = 0 (debt-free). Cash & equivalents FY26 = 274.6. FDs: current
(<12mo) 4,599.5 (AR p.103, Note 10) + non-current (>12mo) 1,854.0 (AR
p.104, Note 5) = 6,453.5 lakh ≈ Rs 64.54 cr, matching company memory's
"~Rs 64.5 cr FDs" (the specific "Rs 52.70 lakh lien-marked" sub-detail was
NOT FOUND anywhere in this AR extraction — flagged, not a contradiction,
just unlocated).

Net debt FY26 = 160.7 − 274.6 − 6,453.5 = −6,567.4 lakh (net cash).
EBIT (PBT + Finance Cost, results FY26 p.2) = 3,730.3 + 11.4 = 3,741.7
lakh. Finance Cost FY26 = 11.4 lakh.
Equity FY26 = 11,612.7 lakh (AR p.11 / results p.3).
Contingent liabilities: NIL, both FY26 and FY25 (AR p.109, Note 31).

- D1 Net Debt ÷ EBITDA (latest) = net cash → **5**
- D2 Interest Coverage EBIT ÷ Interest (latest) = 3,741.7 / 11.4 = 328x → ≥10x → **5**
- D3 Debt ÷ Equity (latest) = 160.7 / 11,612.7 = 0.014 → <0.1 → **5**
- D4 Current Ratio (latest, AR p.11) = 7.60 → ≥2.0 → **5**

**Block D = 20/20.** Fortress balance sheet, confirms company memory
(debt-free, ~Rs64.5cr FDs).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (max 20)
Promoter shareholding (AR p.104, Note 12(b)): Pritesh Ramani 21.40%,
Jogindersingh Jaswal 26.39%, Ketan Ramani 26.39% = 74.18% total, IDENTICAL
in FY25 and FY26 ("Change during the Year" column shows "-" for all three,
both years).

- E1 Promoter holding (latest) = 74.18% → ≥60% → **5**
- E2 Promoter holding change over 3 years: NOT COMPUTABLE as specified — no
  prospectus and no FY23/FY24 shareholding pattern held in this corpus
  (input gap). Only the FY25→FY26 window is in the AR (unchanged, 0%
  change). Scored on the available 1-year window: ±1% band → **3** (flag:
  the true 3-year window spans the Jun-2024 IPO, an OFS event that by
  definition moved promoter % — not visible in this corpus)
- E3 Promoter pledge (latest): NOT FOUND anywhere in AR FY26 (pledge % is
  disclosed in the SEBI shareholding pattern filing, not held in this
  corpus — input gap). Scored **0** per no-estimate rule; this is a data
  gap, not evidence of actual pledge.
- E4 Contingent Liabilities ÷ Net Worth (latest) = 0 / 11,612.7 = 0% → <5% → **5**

**Block E = 13/20.**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (max 60)

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | 0 | EBITDA margin expanded +11.14pp (22.72%→33.86%, AR p.11) but revenue CAGR only ~1.9%, below the ≥10% threshold both top tiers require. Scored 0 per literal test despite the margin trajectory. |
| M2 | Cost Advantage vs peer | 0 | PEER DATA NEEDED — no peer set in this run |
| M3 | Capital Efficiency | 5 | FAT FY26 = 3.52x (AR p.11) >3x AND ROCE FY26 = 32.22% >20% |
| M4 | Customer Stickiness | 3 | 1 revenue-decline year (FY23→24), fully recovered by FY25 (10,018.4 > 9,557.7); receivable days stable (72/72/76, company memory cross-checked against AR p.106 ageing note) |
| M5 | Scale & Dominance | 0 | PEER DATA NEEDED — no mcap/peer margin comparison available |
| M6 | Technology / R&D | 0 | AR p.3 states R&D expenses incurred but does not disclose R&D/Revenue %; NOT quantified |
| M7 | Regulatory / License | 0 | No listed-player count or regulatory scarcity disclosed; segment (specialty fine chemicals) presented as unregulated/open |
| M8 | Distribution | 0 | No distribution network/reach quantified — B2B industrial chemical manufacturer |
| M9 | Brand | 0 | PEER DATA NEEDED — no peer gross margin for comparison |
| M10 | Switching Costs | 3 | Growth in all but 1 year, receivable days rose only 4 days (72 FY24 → 76 FY26) — stable |
| M11 | Network Effects | 0 | Only 4 years available (<6 needed for two-window test); scored conservatively — overall revenue CAGR is weak (~1.9%), stated per rule |
| M12 | Negative WC / Float | 0 | WC days (CCC proxy) 74/96/77/83, all >45 days consistently |

**Moat score = 11/60. Moats "present" (≥3): M3, M4, M10 = 3 confirmed.**
**Moat classification: 2-3 present = MODERATE.**

Four of twelve tests (M2, M5, M9, and effectively M6) are capped at 0 for
lack of peer data, not genuine absence of moat — flagged for the
downstream verifier; a peer-data pass could move this materially.

---

## CLASSIFICATION

- Core score = A(15) + B(16) + C(11) + D(20) + E(13) = **75/100**
- Moat score = **11/60**, class = **MODERATE**, 3 moats confirmed
- Classification matrix: Core 60-79 + (moat class not STRONG/FORTRESS) → **GOOD**
- Data confidence: 4 years of history (FY23-FY26) → **3-4 LIMITED band → downgrade classification one tier**
- **GOOD → AVERAGE** (history_downgrade = true)
- Grand total = 75 + 11 = **86**

Deal-breaker overrides checked: none triggered (Block A=15 not <8; Block
B=16 not <8; median ROCE 40.59% not <10%; cumulative CFO/PAT 1.011 not
<0.50; pledge unknown, not confirmed >15%; net debt is net cash, D1/D2
deal-breaker N/A; revenue declined in only 1 of 3 years, not a majority;
PAT never negative; history is 4 years, ≥3).

**Final classification: AVERAGE** (driven by the LIMITED-history downgrade
from an underlying GOOD; the underlying fundamentals — Blocks A, D
especially — are far stronger than the label suggests).

Strongest block: **D (Balance Sheet Strength), 20/20** — debt-free in
substance, ~Rs 64.5 cr in FDs, zero contingent liabilities.
Weakest block: **C (Growth), 11/20** — revenue CAGR near zero, though
PAT CAGR is strong on margin expansion alone.

---

## SPEAR LOAD-BEARING FACTS — VERIFICATION STATUS

1. **IPO 100% OFS (~Rs 130cr to 3 promoters)**: NOT VERIFIABLE in this
   corpus. AR FY26 does not discuss the FY25 IPO structure; no FY25 AR or
   prospectus held (input gap). AR p.87 CARO clause only confirms the
   company raised no IPO money DURING FY26 (the year after listing),
   which is consistent with, but does not prove, a pure-OFS IPO in FY25.
2. **Promoter remuneration % of PAT**: CONFIRMED for FY25 and FY26. AR
   p.112, Note 34 (Related Party Disclosures — Remuneration paid to
   Directors): Director Remuneration total FY25 = Rs 180.0 lakh, FY26 =
   Rs 396.0 lakh (Rs 60.0 lakh and Rs 132.0 lakh per promoter
   respectively, 3 promoters). Against PAT (results FY26 p.2): FY25 =
   180.0/2,545.7 = **7.07%** (exact match to spear fact); FY26 =
   396.0/2,766.0 = **14.32%** (exact match to spear fact). FY21-FY24
   portion of the claim (40.08/30.09/30.69/17.45%) is NOT VERIFIABLE in
   this corpus (no earlier AR/prospectus held).
3. **Dahej Unit IV: approvals obtained, construction not started**:
   CONFIRMED. AR p.18, Chairman's Letter: "we have already obtained all
   the required permission... Due to unforeseen circumstances the work at
   Unit IV, Dahej could not be started. Now shortly the work will be
   started..."
4. **Revenue Rs 89.86/100.19/101.22 cr FY24/25/26, ROCE 36-44%, net margin
   ~26%, debt-free, ~Rs 64.5cr FDs**: CONFIRMED, with minor precision
   notes. Revenue matches (FY24=8,986.2, FY25=10,018.4, FY26=10,122.0
   lakh). ROCE range in memory (36-44%) is slightly narrower than the
   actual 4-year range found (32.22%-49.46%, AR p.11) — the FY26 figure
   (32.22%) and FY23 figure (49.46%) both sit outside the memory's stated
   band; flagged, not a contradiction of substance. Net margin ~26%
   matches FY26 (25.99%). Debt-free is true in substance (net cash, minor
   vehicle loans of Rs 1.6 cr only in FY26). FDs ~Rs 64.5 cr confirmed
   (computed Rs 64.54 cr).

## ADDITIONAL CROSS-CHECK (not a spear fact, flagged for reconciliation)
Company memory states "Q1 FY27 PAT +16.24%." Source data (Q1 FY27 filing
p.3) shows Q1 FY27 PAT = Rs 730.3 lakh vs Q1 FY26 PAT = Rs 527.3 lakh =
**+38.5%** growth, not +16.24%. Revenue growth over the same period was
+13.4% (Rs 2,830.5 lakh vs Rs 2,496.7 lakh). This quarterly figure is not
used in the annual Gate 0 scoring but the discrepancy is flagged for
downstream reconciliation.

---
