# GATE 0 SCORECARD — Fedbank Financial Services Ltd (FEDFINA)
Run date: 2026-07-15 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 6 years (FY21 to FY26), audited/reviewed full-year statements, plus
Q1 FY27 (quarter ended June 30, 2026, unaudited/limited-review) used only for
"latest" point-in-time ratios (CRAR, PCR, GNPA/NNPA, Debt-Equity, promoter
holding) as it is the most recent disclosure available at run date. Scoring
adapted to 6-year history (Block C uses a 5-year CAGR window, FY21→FY26).

No FEDFINA-specific screener CSV existed for this run (screening/ folder holds
peer CSVs only — SBFC, MASFIN, MANAPPURAM, FIVESTAR). All figures below were
extracted directly from regulatory filings and are anchored to source and page.

**Entity type: NBFC-ND-SI (lender).** Per run instructions this scorecard is
adapted for a lender: ROCE-based tests (A1/A2/A4), Working-Capital-Days tests
(B4), Fixed-Asset-Turnover/receivable-day tests (M3/M4/M10/M12) are recorded as
N/A rather than force-scored, because Fedfina's Ind AS financial-company balance
sheet does not present a Current Liabilities / Current Assets split (the
company's own Regulation 52(4) disclosure states explicitly: "Current ratio...
[is] not applicable to the Company" — results-A p.6/results-B p.10). Where a
metric is N/A it is scored 0 per Rule 5 ("if a data point is not available,
mark N/A and score 0") — this is a data/formula-mismatch outcome, not a
judgment that the underlying business is weak on that dimension. See
data_notes below for the qualitative read.

---

## BLOCK A: RETURN ON CAPITAL (max 20) — Score: 0/20

| Test | Value | Score | Anchor |
|---|---|---|---|
| A1 Median ROCE | N/A (not in provided data) | 0 | ROCE formula (EBIT ÷ [Total Assets − Current Liabilities]) is not computable: Fedfina's Ind AS balance sheet is unclassified (no Current Liabilities line); company confirms "Current ratio... not applicable" (results-A p.6, Reg 52(4) table, note 1) |
| A2 Minimum single-year ROCE | N/A (not in provided data) | 0 | same as A1 |
| A3 Median ROE | 11.5% (median of 6 years) | 0 | see ROE table below; band <12% = 0 |
| A4 ROCE trend, latest vs earliest | N/A (not in provided data) | 0 | same as A1 |

**ROE by year** (PAT ÷ average Net Worth, company-reported):
FY21 8.08% (RHP-prospectus p.113, KPI table, "Return on Average Equity (%)") |
FY22 10.41% (RHP-prospectus p.113, same table) |
FY23 14.36% (RHP-prospectus p.113, same table) |
FY24 13.54% (annual-report.txt p.64, Directors' Report Financial Highlights, "Return on Equity (%)") |
FY25 9.37% (annual-report.txt p.64, same table) |
FY26 12.6% (investor-presentation.txt p.31, "Return on Average Total Equity", FY26 column)
Sorted: 8.08, 9.37, 10.41, 12.6, 13.54, 14.36 → median = (10.41+12.6)/2 = **11.5%**

---

## BLOCK B: CASH GENERATION QUALITY (max 20) — Score: 0/20

CFO, capex and FCF computed per year (₹ Cr) from restated/audited cash flow
statements. NBFC caveat: for a lender, "(Increase)/decrease in loans" is
classified inside CFO under Ind AS 7 — i.e. loan-book growth is booked as an
**operating cash outflow**, financed by borrowings (a financing-activity
inflow). A structurally negative CFO is therefore the normal signature of a
growing loan book, not on its own evidence of weak earnings quality — see
block_b_trend / data_notes for the genuine (non-structural) quality flags
found in the sources.

| FY | CFO (₹Cr) | Capex (₹Cr) | FCF (₹Cr) | PAT (₹Cr) | Anchor |
|---|---|---|---|---|---|
| FY21 | (371.23) | 11.15 | (382.38) | 61.68 | RHP-prospectus p.~394 (Restated Cash Flow Statement, FY21 column) |
| FY22 | (577.89) | 26.89 | (604.78) | 103.46 | RHP-prospectus, same table, FY22 column |
| FY23 | (1,474.00) | 15.10 | (1,489.10) | 180.13 | RHP-prospectus, same table, FY23 column |
| FY24 | (775.52) | 13.72 | (789.24) | 244.70 | annual-report.txt p.170 (Statement of Cash Flow FY25 AR, FY24 comparative column) |
| FY25 | (977.52) | 18.95 | (996.47) | 225.18 | annual-report.txt p.170, FY25 column |
| FY26 | (1,664.16) | 30.01 | (1,694.17) | 343.60 | results-B.txt p.8 (Statement of Cash Flow, year ended 31 Mar 2026) |
| **Cumulative** | **(5,840.32)** | **115.82** | **(5,956.14)** | **1,158.76** | sums of above, computed |

Capex = purchase of tangible (PPE) assets + purchase of intangible assets +
intangible assets under development, per year, excludes acquisitions
(none disclosed). FY26 capex uses results-B.txt p.8; FY25/FY24 use
annual-report.txt p.170; FY23/22/21 use RHP-prospectus restated cash flow
statement.

| Test | Value | Score |
|---|---|---|
| B1 Cumulative CFO ÷ Cumulative PAT | −5,840.32 ÷ 1,158.76 = **−5.04x** | 0 (<0.50) |
| B2 FCF-positive years as proportion | 0 of 6 years (0%) | 0 (<50%) |
| B3 Cumulative FCF ÷ Cumulative PAT | −5,956.14 ÷ 1,158.76 = **−5.14x** | 0 (<0.20 / negative) |
| B4 Change in WC Days, latest vs earliest | N/A (not in provided data) | 0 — "Working Capital Days" (receivable/inventory/payable days) is not a meaningful construct for a lender's balance sheet; the loan book, not trade receivables, is the core asset. Company confirms "Debtors turnover, Inventory turnover... not applicable to the Company" (results-A p.6, note 1) |

**block_b_trend: deteriorating** (feeds FLAG-CASH) — one number: direct-assignment
(DA) gain-on-sale income rose to **~50% of PBT in FY25 from ~28% in FY24**
(rating.txt p.2), i.e. a growing share of reported profit is coming from
non-recurring, non-NII, capital-relief transactions rather than accrual net
interest income actually collected in cash, at the same time credit costs
spiked to ₹216 Cr / 1.8% of average assets in FY25 (from 0.7% in FY24,
rating.txt p.2) and Provision Coverage Ratio fell from 40.0% (FY25,
annual-report.txt p.19) to 32.29% (FY26, results-B.txt p.10) even as headline
GNPA improved slightly — reserving against bad loans is thinner even as the
book scales.

---

## BLOCK C: GROWTH (max 20) — Score: 20/20

Revenue basis used = "Total Income" (Total Revenue from Operations + Other
Income) for consistency across all six years (this is the basis the FY25
Annual Report's own "Total Revenue" line uses — annual-report.txt p.64 FY25
figure ₹2,07,982 lakh ties exactly to results-B.txt p.6 "Total Income (II+III)"
FY25 ₹2,07,982 lakh).

| FY | Total Income (₹Cr) | PAT (₹Cr) | Anchor (Revenue) |
|---|---|---|---|
| FY21 | 697.57 | 61.68 | RHP-prospectus p.113, KPI table "Total Revenue" |
| FY22 | 883.64 | 103.46 | RHP-prospectus p.113, same table |
| FY23 | 1,214.68 | 180.13 | RHP-prospectus p.113, same table |
| FY24 | 1,623.00 | 244.70 | annual-report.txt p.64, Financial Highlights "Total Revenue" |
| FY25 | 2,079.82 | 225.18 | annual-report.txt p.64, same table |
| FY26 | 2,226.61 | 343.60 | results-B.txt p.6, "Total Income (II+III)" |

| Test | Value | Score |
|---|---|---|
| C1 Revenue CAGR (FY21→FY26, 5yr) | (2,226.61÷697.57)^(1/5)−1 = **26.1%** — computed | 5 (≥20%) |
| C2 PAT CAGR (FY21→FY26, 5yr) | (343.60÷61.68)^(1/5)−1 = **41.0%** — computed | 5 (≥20%) |
| C3 Positive YoY revenue years | 5 of 5 YoY comparisons positive (FY22>21, 23>22, 24>23, 25>24, 26>25) = **100%** | 5 |
| C4 PAT CAGR − Revenue CAGR | 41.0 − 26.1 = **+14.9pp** | 5 (≥+3pp) |

No loss-to-profit swing (PAT positive every year FY21–FY26); no N/M CAGR
edge cases triggered. Corroborating (not separately scored) evidence: AUM
grew from ~₹4,862 Cr (FY21, RHP-prospectus KPI table) to ₹20,153 Cr (FY26,
investor-presentation.txt p.19/31) to ₹21,136 Cr (Q1 FY27, +34.7% YoY,
investor-presentation.txt p.5) — CAGR ≈33%, consistent with the revenue
growth score.

---

## BLOCK D: BALANCE SHEET STRENGTH (max 20) — Score: 8/20

Latest point-in-time figures use Q1 FY27 (quarter ended 30 June 2026, the most
recent filing) where disclosed there; FY26 (31 March 2026, audited) figures
shown alongside for context.

| Test | Value | Score | Anchor |
|---|---|---|---|
| D1 CRAR (NBFC substitute for Net Debt/EBITDA) | **20.71%** (30 Jun 2026) | 5 (≥18%) | results-A.txt p.6, Reg 52(4) disclosure |
| D2 PCR (NBFC substitute for Interest Coverage) | **38.36%** (30 Jun 2026) | 0 (<60%) | results-A.txt p.6, Reg 52(4) disclosure; corroborated by investor-presentation.txt p.27 (Q1FY27 PCR chart, 38.4%) |
| D3 Debt ÷ Equity | Financials: default 3 applied (actual reported Debt-Equity Ratio = **4.89x**, 30 Jun 2026) | 3 (default per rubric) | results-A.txt p.6, Reg 52(4) disclosure |
| D4 Current Ratio | N/A (not in provided data) | 0 | company confirms "Current ratio... not applicable to the Company" (results-A.txt p.6, note 1) |

CRAR context: FY21 23.52% → FY22 23.04% → FY23 17.94% → FY24 23.5% (AR chart,
annual-report.txt p.18-19) → FY25 21.92% (annual-report.txt p.64) → FY26
22.40% (results-B.txt p.10) → Q1FY27 20.71% — comfortably above the RBI
minimum (15%) and the company's own NCD covenant floors (15-16%, results-A.txt
p.9), trending down modestly as the book scales.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (max 20) — Score: 10/20

| Test | Value | Score | Anchor |
|---|---|---|---|
| E1 Promoter holding (latest) | Federal Bank Ltd **60.7%** (30 Jun 2026) | 5 (≥60%) | investor-presentation.txt p.11 |
| E2 Promoter holding change, 3 years | 73.22% (30 Sep 2023, pre-IPO) → 60.7% (30 Jun 2026) = **−12.5pp** | 0 (decreased >3%) | rating.txt p.5 ("Until September 30, 2023, FBL had a 73.22% stake"); investor-presentation.txt p.11. **Caveat: this decline is entirely the Nov-2023 IPO primary/OFS dilution event, not organic post-listing selling.** Post-listing trend is flat: FBL held 60.80% at listing (rating.txt p.1) vs 60.7% now (investor-presentation.txt p.11), a −0.1pp change over ~2.6 years — analogous to a documented post-IPO rebase. |
| E3 Promoter pledge (latest) | N/A (not in provided data) | 0 | Shareholding-pattern pledge filings not included in this stage's data sources; not to be read as a positive 0%-pledge finding, only as a data gap |
| E4 Contingent liabilities ÷ Net Worth (latest) | ₹847 lakh ÷ ₹2,54,736 lakh = **0.33%** (FY25) | 5 (<5%) | annual-report.txt p.255-256, Note 53 Contingent Liabilities (FY25 figure — FY26 Annual Report/notes not yet published at run date) |

---

## BLOCK F: QUANTITATIVE MOAT SCORING (max 60) — Score: 10/60

Peer market-cap/margin comparisons were **not** part of this stage's data set
(peer CSVs/transcripts for SBFC, MASFIN, MANAPPURAM, FIVESTAR exist in the run
folder but were not injected as Gate 0 sources — "No FEDFINA screener CSV...
peer CSVs only"). Tests requiring peer data are scored 0 / "PEER DATA NEEDED"
rather than guessed.

| # | Test | Score | Basis / Anchor |
|---|---|---|---|
| M1 | Pricing Power | **5** | Proxy: operating-margin equivalent (1 − Cost-to-Income%) expanded from 38.5% (FY21, 100−61.5, annual-report.txt p.18) to 42.8% (FY26, 100−57.2, investor-presentation.txt p.31) = +4.3pp, ≥2pp, alongside revenue CAGR 26.1% (≥10%) → top tier. Proxy stated because "EBITDA margin" has no direct NBFC equivalent. |
| M2 | Cost Advantage vs peer median | 0 (PEER DATA NEEDED) | peer margin data not provided to this stage |
| M3 | Capital Efficiency (FAT × ROCE) | 0 (N/A) | Fixed Asset Turnover and ROCE are not meaningful constructs for an asset-light lender whose balance sheet is dominated by the loan book, not PP&E; ROCE denominator unavailable (see Block A) |
| M4 | Customer Stickiness | 0 (N/A) | Revenue itself never declined (positive fact, see Block C), but "receivable days stability ±10" cannot be computed — Fedfina's core asset is the loan book, not trade receivables |
| M5 | Scale & Dominance | 0 (PEER DATA NEEDED) | peer mcap/margin ranking not provided to this stage |
| M6 | Technology / R&D | 0 (N/A) | No R&D or technology-spend-as-%-of-revenue line disclosed in any source provided |
| M7 | Regulatory / License | 0 (PEER DATA NEEDED) | Fedfina is RBI-regulated (NBFC-ND-SI license required), but an exact count of listed players in the overlapping gold-loan/LAP/MSME-NBFC segment was not verifiable from the sources provided to this stage; not guessed |
| M8 | Distribution | **5** | Branch network quantified and growing every year: 359 (FY21) → 621 (FY24) → 694 (FY25) → 757 (FY26/Q1FY27) (annual-report.txt p.20-21; rating.txt p.3; investor-presentation.txt p.17). AUM/Branch (Gold Loan) grew from ₹13.0 Cr (Q1FY26) to ₹17.7 Cr (Q1FY27), investor-presentation.txt p.20; overall AUM/Branch grew FY21 ₹13.5 Cr → Q1FY24 ₹16.2 Cr (RHP-prospectus p.113 KPI table) → top tier |
| M9 | Brand | 0 (PEER DATA NEEDED) | peer gross-margin comparison not provided to this stage |
| M10 | Switching Costs | 0 (N/A) | same receivable-days limitation as M4; revenue grew every year (positive fact) but the stability leg is not computable |
| M11 | Network Effects (2-window test, 6yrs available) | 0 | Latest-3yr revenue CAGR (FY23→FY26) = (2,226.61÷1,214.68)^(1/3)−1 ≈ **22.4%** vs prior-3yr CAGR (FY21→FY24) = (1,623.00÷697.57)^(1/3)−1 ≈ **32.5%** — computed. Latest window is a *deceleration*, not acceleration, so top tier fails; "selling expense %" is not a separately disclosed NBFC line item, so the second-tier condition (rev CAGR≥20% AND selling% stable/declining) cannot be fully verified either → scored conservatively at 0 |
| M12 | Negative WC / Float | 0 (N/A) | No deposit-taking / working-capital float construct applies to an NBFC-ND-SI (non-deposit-taking by definition) |

**Moats confirmed (score ≥3): 2** (M1 Pricing Power, M8 Distribution)
**Moat classification: MODERATE** (2-3 confirmed)

```
Moat profile:
M1  [#####] 5  Pricing Power
M2  [     ] 0  Cost Advantage        (PEER DATA NEEDED)
M3  [     ] 0  Capital Efficiency    (N/A - lender balance sheet)
M4  [     ] 0  Customer Stickiness   (N/A - receivable days)
M5  [     ] 0  Scale & Dominance     (PEER DATA NEEDED)
M6  [     ] 0  Technology / R&D      (not disclosed)
M7  [     ] 0  Regulatory / License  (PEER DATA NEEDED)
M8  [#####] 5  Distribution
M9  [     ] 0  Brand                 (PEER DATA NEEDED)
M10 [     ] 0  Switching Costs       (N/A - receivable days)
M11 [     ] 0  Network Effects       (deceleration; selling% not disclosed)
M12 [     ] 0  Negative WC / Float   (N/A - non-deposit NBFC)
```

---

## SCORECARD SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 0 | 20 |
| B — Cash Generation Quality | 0 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 8 | 20 |
| E — Shareholder Alignment | 10 | 20 |
| **Core score** | **38** | **100** |
| F — Quantitative Moat | 10 | 60 |
| **Grand total** | **48** | **160** |

**Strongest block: C — Growth (20/20)** — Revenue CAGR 26.1%, PAT CAGR 41.0%,
zero revenue-decline years across 6 audited years.

**Weakest blocks: A and B (0/20 each, tied)** — driven almost entirely by
formula/data-structure mismatch (ROCE and Working-Capital-Days have no
computable NBFC equivalent in the data provided) plus one genuine data point
(median ROE 11.5%, below the 12% A3 threshold) and one structural
characteristic of a growth-stage lender (CFO/FCF negative every year because
loan disbursement is an Ind AS operating outflow, financed through financing
activities). These are NOT read as evidence the underlying lending business
destroys capital or burns cash to fund losses — Block D (CRAR 20.71%,
comfortably above regulatory and covenant minimums) and Block C confirm the
growth is being funded, not masking a cash shortfall. The genuine, non-
structural soft spots found in the sources are: PCR thinning (40.0%→32.29%,
FY25→FY26), the credit-cost spike in FY25 (0.7%→1.8% of average assets), and
the rising reliance on direct-assignment gain-on-sale income for reported
profit (~28%→~50% of PBT, FY24→FY25).

---

## DATA CONFIDENCE

6 years of full-year data (FY21-FY26) → **"5-6 lower"** band per rubric.
**Flag: may not have seen a full credit cycle** — Fedfina's listed history
(Nov 2023) and even its restated pre-IPO history (from FY21) does not span a
system-wide NBFC credit stress cycle comparable to 2018-2019 (IL&FS/DHFL); the
FY25 credit-cost spike in small-ticket LAP (rating.txt p.2-3) is the first
visible stress episode in the window provided. No classification-tier
downgrade applied (that rule triggers only at 3-4 years of history); this is
a flag only.

---

## CLASSIFICATION

```
┌─────────────────────────────────────────────┐
│  Core score:      38 / 100                   │
│  Moat class:       MODERATE (2 confirmed)    │
│  Grand total:      48 / 160                  │
│                                               │
│  CLASSIFICATION:   AVOID                     │
│  (Core <40 → AVOID, overrides moat class)    │
└─────────────────────────────────────────────┘
```

### Deal-breaker check (recorded per rules; classification is already at the
floor via Core<40, so none of these change the outcome, but they are logged
because they independently point the same direction):

1. Block A (0) < 8 → max GOOD — **triggered**, structural (NBFC ROCE N/A),
   applies across the full window FY21-FY26, not a specific bad year.
2. Block B (0) < 8 → max GOOD — **triggered**, structural (NBFC CFO
   classification), applies across the full window FY21-FY26.
3. Median ROCE <10% → max AVERAGE — **not triggered** (ROCE is N/A, not
   computed as below 10%).
4. Cumulative CFO/PAT <0.50 → max AVERAGE — **triggered** (−5.04x); see
   block_b_trend caveat above on structural vs genuine cash-quality read.
5. Pledge >15% → max AVERAGE — **not triggered / not determinable** (E3 N/A).
6. ND/EBITDA >3x AND IC <3x → AVOID — **not evaluated**, no NBFC-equivalent
   combined test defined in the rubric (D1/D2 already use CRAR/PCR
   individually).
7. Revenue declined in majority of years → max AVERAGE — **not triggered**
   (0 of 5 YoY comparisons negative).
8. PAT negative in any of last 3 years → max AVERAGE — **not triggered**
   (FY24 ₹244.70 Cr, FY25 ₹225.18 Cr, FY26 ₹343.60 Cr — all positive).
9. History <3 years → AVERAGE — **not triggered** (6 years available).

### Decision line
Mechanical Gate 0 classification is **AVOID**, driven by a growth-lender's
structural mismatch with two manufacturing-oriented blocks (A: ROCE, B:
Working-Capital-derived cash conversion) rather than by a demonstrated
capital-destruction or going-concern problem — Blocks C (growth) and D
(capitalisation) are strong to adequate, and the moat scan finds two
confirmed, evidenced moats (distribution reach, pricing/margin trend). The
genuine quality flags in the underlying documents — FY25 credit-cost spike,
declining PCR into FY26, and rising DA-income dependence for reported profit
— are real and should carry forward as flags rather than be diluted by the
AVOID label. Per pipeline rules this classification does not halt the run;
it propagates as FLAG-GATE0 (and FLAG-CASH / FLAG-ASSETQUALITY) for
downstream stages (notably Stage 11 valuation) to weigh explicitly rather
than resolve silently to a favourable read.

---

## DATA NOTES

- No loss-to-profit swing: PAT positive in all six years, FY21-FY26.
- Proxy bases used: (1) "Total Income" (Total Revenue from Operations + Other
  Income) used as the single consistent revenue basis for Block C across all
  sources (RHP, FY25 Annual Report, FY26 results) — confirmed to tie exactly
  where sources overlap (FY25: ₹2,07,982 lakh in both annual-report.txt p.64
  and results-B.txt p.6). (2) (1 − Cost-to-Income%) used as an "operating
  margin" proxy for M1 Pricing Power, since NBFCs do not report a COGS/EBITDA
  split.
- PEER DATA NEEDED items: M2, M5, M7, M9 — peer market-cap/margin/player-count
  data was not part of this stage's injected sources (peer CSVs/transcripts
  for SBFC, MASFIN, MANAPPURAM, FIVESTAR exist elsewhere in the run folder but
  were not listed as Gate 0 inputs).
- A1/A2/A4/D4 marked N/A (not a scoring judgment) because Fedfina's Ind AS
  financial-company balance sheet does not present a Current Liabilities
  line; the company's own Regulation 52(4) disclosure states this class of
  ratio ("Current ratio", "Debtors turnover", "Inventory turnover", "Debt
  service coverage ratio", "Interest service coverage ratio", "Long term debt
  to working capital ratio", "Bad debts to accounts receivable ratio",
  "Operating margin") is "not applicable to the Company" (results-A.txt p.6 /
  results-B.txt p.10, note 1).
- B4, M3, M4, M10, M12 marked N/A for the same reason (no traditional working
  capital / fixed-asset-turnover / deposit-float construct applies to a
  non-deposit-taking NBFC whose core asset is the managed loan book).
- Genuine (non-structural) quality items found in the sources, to carry
  forward: (a) direct-assignment gain-on-sale income rose to ~50% of PBT in
  FY25 from ~28% in FY24 (rating.txt p.2); (b) credit cost rose to ₹216 Cr /
  1.8% of average assets in FY25 from 0.7% in FY24, driven by small-ticket LAP
  stress (rating.txt p.2); (c) Provision Coverage Ratio fell from 40.0% (FY25,
  annual-report.txt p.19) to 32.29% (FY26, results-B.txt p.10) to 38.36%
  (Q1FY27, results-A.txt p.6); (d) PAT declined FY24→FY25 (₹244.70 Cr→
  ₹225.18 Cr) before recovering sharply in FY26 (₹343.60 Cr, +52.6%).
- Spread / Cost-to-Income / ROA / ROE figures for FY22-FY24 differ modestly
  between the FY25 Annual Report 5-year chart (two-point average basis,
  annual-report.txt p.18-19) and the Q1 FY27 investor presentation (restated
  to a quarterly-average basis per the presentation's own footnote,
  investor-presentation.txt p.24: "Yearly Yields, CoB, and Spreads restated
  from two-point average to quarterly average"). Both are anchored above
  where used; the AR chart values (FY21-FY25 ROE/ROA/GNPA/NNPA/CRAR/PCR/
  Cost-to-Income) were used for Block A/D scoring as they are the only
  audited-report-native series; the IP FY26 figures were used for the latest
  year and are internally consistent with results-B.txt's own Reg 52(4)
  disclosures.
- E2 promoter-holding-change mechanically scores 0 (>3% decrease over 3
  years), but the entire decrease (73.22%→60.80%) occurred in the November
  2023 IPO (primary issuance + offer-for-sale), not from organic post-listing
  promoter selling. Post-listing (Nov-2023 to Jun-2026) the holding is flat
  (60.80%→60.7%, −0.1pp). Flagged for downstream position-sizing judgment,
  analogous to CLAUDE.md's documented post-IPO-rebase carve-out.
- E3 promoter pledge: not found in the sources provided to this stage
  (shareholding-pattern / pledge filings were not included); scored N/A/0 per
  the "never estimate a missing number" rule — this is a data gap, not a
  finding of pledge.
- E4 uses the FY25 (31 March 2025) contingent-liabilities figure (₹847 lakh,
  annual-report.txt p.255-256, Note 53) because the FY26 Annual Report /
  notes to accounts (which would carry the FY26 contingent-liabilities note)
  had not been published as of the 2026-07-15 run date; the FY26 results
  filings (results-A, results-B) do not include the full notes-to-accounts.
- Input gaps carried forward per orchestrator: announcements (absent),
  screening-fedfina (peer-only screener, no FEDFINA-specific CSV), prospectus
  folder (absent; RHP present in annual-report/ and used as the RESTATED
  backward-year financial source for FY21-FY23 and the Q1 FY24 KPI table).
