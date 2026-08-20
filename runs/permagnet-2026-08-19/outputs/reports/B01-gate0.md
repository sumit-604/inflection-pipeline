# GATE 0 SCORECARD — Permanent Magnets Limited (PERMAGNET)
Run date: 2026-08-19 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 5 years (FY22 to FY26) for the revenue / PAT / margin / ROCE / ROE /
equity / debt-equity / working-capital-days trend, sourced from the Annual Report's own
5-year KPI infographic (standalone basis only, AR-FY26 p.12). Full audited financial
statements (balance sheet, P&L, cash flow with note-level detail) are available for only
**2 years** (FY25 and FY26, standalone and consolidated) — no PERMAGNET screener CSV was
provided this run and no earlier annual reports were supplied, so FY22-FY24 balance
sheet/cash-flow line items do not exist in the provided documents. Scoring is adapted
block by block: Blocks A, C and the moat tests use the 5-year (FY22-FY26) window;
Block B (cash generation) is computed on the 2-year (FY25-FY26) window only, below the
pipeline's stated 3-year minimum — flagged as a data limitation, not a company signal.
Consolidated figures are used for the latest-year Block D (balance sheet strength) per
orchestrator guidance ("group view"); standalone figures are used wherever the AR's own
multi-year series is standalone-only, with basis stated on every line.

Input gaps carried from the orchestrator: no PERMAGNET screener; no announcements folder;
no shareholding filing (promoter pledge % and 3-year promoter-holding trend not available);
NO-CONCALL MODE; the manifest's sector_cap_row ("Agri processing") is a known collector
defect and is not used anywhere below; no peer/competitor financial data was provided this
run (10 of 12 moat tests need it — see Block F).

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — standalone, FY22-FY26, AR's own figures (AR-FY26 p.12)

| Year | ROCE % | ROE % |
|---|---|---|
| FY22 | 31 | 23 |
| FY23 | 36 | 27 |
| FY24 | 22 | 17 |
| FY25 | 14 | 10 |
| FY26 | 16 | 13 |

Cross-check: FY26 ROCE recomputed independently = EBIT 32.56 (PBIDT 45.19 − Depreciation
12.63, AR-FY26 p.34) ÷ Capital Employed 197.56 (Total Assets 238.35 − Current Liabilities
40.79, AR-FY26 p.76) = 16.48%, matching the AR's own 16% — AR figure used per the ROCE
formula-override rule.

- **A1 Median ROCE**: sorted [14,16,22,31,36], median = 22% → band 20-24.9% → **score 4**
- **A2 Minimum single-year ROCE**: 14% (FY25) → band 12-14.9% → **score 3**
- **A3 Median ROE**: sorted [10,13,17,23,27], median = 17% → band 15-19.9% → **score 4**
- **A4 ROCE trend, latest vs earliest**: FY26 16% vs FY22 31% = decline of 15pp → band
  decline >5pp → **score 0**

**Block A total: 11/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — consolidated, FY25-FY26 only (2 yrs)

Only 2 years of audited cash-flow-statement detail exist in the provided documents
(AR-FY26 p.122-123, cross-checked against RESULTS-Q4FY26 p.10, identical figures).

| ₹ Cr | FY25 (Consol) | FY26 (Consol) |
|---|---|---|
| CFO | 39.15 | 17.59 |
| PAT (continuing ops) | 15.75 | 14.77 |
| Capex (Additions to FA + CWIP + Capital advances for PPE) | 29.08 | 43.34 |
| FCF (CFO − Capex) | +10.07 | −25.75 |

Capex definition: Additions to Fixed Assets (Net) + Capital Work-in-Progress + Capital
Advances for PPE, from the consolidated CF investing section (AR-FY26 p.122); this
reconciles almost exactly to "Net cash used in investing activities" both years (off by
only the ₹0.01-0.02cr Sale of Fixed Assets line), confirming no other investing items are
present.

- **B1 Cumulative CFO ÷ Cumulative PAT**: (39.15+17.59) / (15.75+14.77) = 56.74/30.52 =
  1.86 → band ≥1.00 → **score 5**
- **B2 FCF-positive years as proportion**: 1 of 2 years positive (FY25 only) = 50% →
  band 50-74% → **score 2**
- **B3 Cumulative FCF ÷ Cumulative PAT**: (10.07−25.75)/30.52 = −15.68/30.52 = −0.51 →
  negative → **score 0**
- **B4 Change in WC Days, latest vs earliest**: computed on the **standalone 5-year**
  window instead (AR-FY26 p.12, cross-checked by formula recomputation for FY25/FY26,
  which matched the AR figures exactly): FY22 = 136 days, FY26 = 132 days → decreased 4
  days → band ±5 days → **score 3**. (Basis note: B1-B3 use the 2-yr consolidated window;
  B4 uses the 5-yr standalone window because that is the only multi-year WC-days series
  available — flagged for transparency.)

**Block B total: 10/20**

Block B trend: **deteriorating**. Consolidated FCF swung from +₹10.07cr (FY25) to
−₹25.75cr (FY26) as capex more than doubled to ₹43.34cr against CFO of only ₹17.59cr —
driven by the Quantum Magnetics subsidiary's capacity build-out (see data notes).
Standalone-only FCF stayed positive both years (FY25 +8.70, FY26 +3.63), so this is a
group-level, subsidiary-driven swing, not a parent-business cash-quality deterioration.

---

## BLOCK C: GROWTH (Max 20) — standalone, FY22-FY26

| ₹ Cr (Total Income, proxy — see note) | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|
| Total Income | 133 | 188 | 206 | 204 | 232 |
| PAT (chart, ≈Total Comprehensive Income) | 19 | 30 | 23 | 15 | 21 |

Source: AR-FY26 p.12 (KPI infographic, "Note: Standalone Figures"). Proxy basis note:
"Revenue" for FY22-FY24 is not separately available as "Revenue from Operations" in the
provided documents (only Total Income, which includes Other Income of ~2-3% of the
total); Revenue from Operations is known precisely only for FY25 (₹199.54cr) and FY26
(₹225.46cr) from the audited P&L (AR-FY26 p.77). Total Income is used as the CAGR proxy
for the full 5-year window; distortion from Other Income is judged immaterial to banding.
PAT figures are the AR chart's own rounded values, which reconcile to Total Comprehensive
Income (₹20.69cr/₹15.16cr for FY26/FY25) rather than "Profit for the period" pre-OCI
(₹20.39cr/₹15.17cr); the OCI difference (≤₹0.30cr) does not change any band.

- **C1 Revenue CAGR**: (232/133)^(1/4) − 1 = 14.94% → band 10-14.9% → **score 3**
  (AR's own headline rounds this to "15%" CAGR; precise recomputation from the year
  points is 14.94%, just under the 15% band boundary — scored on the precise figure.)
- **C2 PAT CAGR**: (21/19)^(1/4) − 1 = 2.54% → band <5% → **score 0**
- **C3 Positive YoY revenue years**: FY23, FY24, FY26 positive; FY25 negative (206→204)
  = 3 of 4 transitions = 75% → band 75-99% → **score 3**
- **C4 PAT CAGR − Revenue CAGR**: 2.54% − 14.94% = −12.4pp → band <−8pp → **score 0**

**Block C total: 6/20**

Deal-breaker check #7 (revenue declined in majority of years): only 1 of 4 years
declined (25%), not majority — **not triggered**. Deal-breaker check #8 (PAT negative in
any of last 3 years): PAT positive every year FY24-FY26 — **not triggered**.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — consolidated, latest year (FY26)

Source: Consolidated Balance Sheet, AR-FY26 p.120-121; Financial Highlights table,
AR-FY26 p.34 (PBIDT/EBITDA, Interest); RESULTS-Q4FY26 p.9 (cross-check, identical).

Debt is defined as Borrowings (current + non-current) **plus** Lease Liabilities
(current + non-current), consistent with the company's own "Total Debt to Equity" KPI
methodology — verified by recomputing the standalone FY26 figure: (19.03+3.47+11.05+3.87)
/ 164.97 = 0.227 ≈ 0.23x, exactly matching the AR's own chart value (AR-FY26 p.12).

- Total debt (consol, FY26) = 66.84 (NC borrowings) + 3.47 (current borrowings) + 12.63
  (NC lease) + 5.05 (current lease) = **87.99**
- Cash & Cash Equivalents (consol, FY26) = **28.11**. Net debt nets only this line, not
  the separately classified "Other Bank Balances" (₹23.20cr current + ₹0.29cr non-current
  = ₹23.49cr, likely FDs with >3-month maturity); if those were netted too, net debt would
  be ₹36.39cr and ND/EBITDA ~0.85x (band score 4 instead of 3) — basis stated for
  downstream re-check.
- Net debt = 87.99 − 28.11 = **59.88**
- EBITDA (PBIDT & EO items, consol FY26) = **42.76** (AR-FY26 p.34)
- EBIT = 42.76 − 14.52 (depreciation) = **28.24**
- Interest (Finance costs, consol FY26) = **4.10**
- Equity (consol FY26) = **157.39**
- Current Assets / Current Liabilities (consol FY26) = 172.83 / 42.60 = **4.06x**

- **D1 Net Debt ÷ EBITDA**: 59.88/42.76 = 1.40x → band 1-2x → **score 3**
  (standalone-only equivalent, for context: 25.63/45.19 = 0.57x, band 0-1x, score 4 — the
  gap is entirely the subsidiary's FY26 debt-funded capex)
- **D2 Interest Coverage**: 28.24/4.10 = 6.89x → band 5-9.9x → **score 4**
- **D3 Debt ÷ Equity**: 87.99/157.39 = 0.56x → band 0.5-1.0x → **score 3**
  (standalone-only: 0.23x, band 0.1-0.5x, score 4 — AR's own chart figure)
- **D4 Current Ratio**: 4.06x → band ≥2.0x → **score 5**

**Block D total: 15/20**

Deal-breaker check #6 (ND/EBITDA >3x AND IC <3x → AVOID): ND/EBITDA 1.40x, IC 6.89x —
**not triggered**.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Source: Shareholding Pattern as on 31.03.2026, AR-FY26 p.60 and p.84-85 (promoter-level
detail with FY25 comparative). No shareholding filing was provided this run, so only a
1-year comparison (Mar-2025 to Mar-2026) exists in the provided documents; the formula's
3-year window (E2) is genuinely not available.

- **E1 Promoter holding (latest, 31.03.2026)**: 4,987,875 shares / 8,598,453 = 58.01% →
  band 50-59.9% → **score 4**
- **E2 Promoter holding change over 3 years**: **N/A (not in provided data)** — only a
  1-year comparison exists. For context (not scored): summing the individual promoter/
  promoter-group lines, aggregate holding is essentially flat, ~58.00% (Mar-2025) to
  ~58.01% (Mar-2026), i.e. +0.01pp over 1 year — this does not satisfy the 3-year window
  the formula requires, so scored per the "never estimate" rule → **score 0**
- **E3 Promoter pledge (latest)**: **N/A (not in provided data)** — no pledge disclosure
  found anywhere in the AR excerpts provided (checked shareholding pattern tables,
  Corporate Governance references, CARO report); the one CARO "pledge" hit concerns loans
  raised against pledge of subsidiary securities (not applicable / nil), not promoter
  share pledge specifically → **score 0**
- **E4 Contingent liabilities ÷ Net Worth (standalone, FY26)**: Contingent liabilities
  (AR-FY26 p.103-104, Note I.2): Unutilized LCs 5.13 + Bank Guarantee 0.16 + Labour cases
  0.08 + Excise duty demand & penalty 0.32+0.32 + Central Excise loan interest dispute
  22.01 + Corporate guarantee for subsidiary EPCG 0.83 = **28.85** (Capital Commitment of
  4.13 excluded as a commitment, not a contingent liability; including it gives 32.98,
  same band). Net Worth (standalone FY26) = 164.97. Ratio = 28.85/164.97 = 17.49% → band
  15-30% → **score 1**

**Block E total: 5/20**

Note: the ₹22.01cr Central Excise loan interest item is a legacy 1995-96 dispute,
unchanged for years; management does not expect an actual cash outflow (AR-FY26 p.35,
Director's Report explanation), but it is disclosed every year and is material relative
to net worth, which is why it drives E4 into the 15-30% band.

Deal-breaker check #5 (pledge >15% → max AVERAGE): pledge is N/A, not confirmed >15% —
**not triggered** (absence of evidence is not evidence of a breach).

---

## CORE SCORE

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 11 | 20 |
| B — Cash Generation Quality | 10 | 20 |
| C — Growth | 6 | 20 |
| D — Balance Sheet Strength | 15 | 20 |
| E — Shareholder Alignment | 5 | 20 |
| **Core Total** | **47** | **100** |

Strongest block: **D (Balance Sheet Strength, 15/20, 75%)**. Weakest block: **E
(Shareholder Alignment, 5/20, 25%)** — driven almost entirely by data gaps (E2, E3 both
N/A) rather than adverse findings; the one scored-and-adverse line is E1 (58.01%, below
the 60% top band).

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Basis: standalone 5-year series (AR-FY26 p.12) unless noted. 10 of 12 tests need peer
(competitor/mcap/margin) data not provided this run — scored 0 and marked "PEER DATA
NEEDED" per the pipeline rule (never guess peer figures).

- **M1 Pricing Power**: EBITDA margin (Operating Profit Margin) FY22 21% → FY26 17%,
  declined 4pp; Revenue CAGR 14.94% (≥10%) → band "margin declined 2-5pp despite
  growth" → **score 1**
- **M2 Cost Advantage vs peer median**: PEER DATA NEEDED → **score 0**
- **M3 Capital Efficiency**: FAT (Revenue ÷ Net Fixed Assets incl. ROU+CWIP+Intangibles)
  = 225.46/75.69 = 2.98x; ROCE FY26 = 16% → band "FAT>2x AND ROCE>15%" → **score 3**
- **M4 Customer Stickiness**: 1 decline year (FY24→FY25), fully recovered by FY26
  (232 > prior peak 206) → band "max 1 decline year, fully recovered" → **score 3**.
  (5-band criterion "receivable days stable ±10" not independently verifiable — FY22-FY24
  receivable-day detail, as opposed to aggregate WC days, is not in the provided
  documents — scored conservatively on the verifiable criterion only.)
- **M5 Scale & Dominance**: PEER DATA NEEDED (mcap/segment ranking) → **score 0**
- **M6 Technology/R&D**: R&D/Revenue FY26 = 0.65% (₹1.46cr total R&D spend / ₹225.46cr
  revenue, AR-FY26 p.49) — below the ≥1% floor for even the lowest band → **score 0**
- **M7 Regulatory/License**: single reportable business segment (Engineering & Current
  Sensing, AR-FY26 p.104), no evidence of a licensing regime restricting entrant count →
  treated as unregulated → **score 0**
- **M8 Distribution**: no dealer/distributor network or quantified reach disclosed;
  business is direct-to-OEM (automobiles, electricity meters) → **score 0**
- **M9 Brand**: PEER DATA NEEDED (peer median gross margin) → **score 0**
- **M10 Switching Costs**: same growth pattern as M4 (all-but-1-year growth) → band
  "growth all but 1 year AND stable" → **score 3** (same receivable-days-stability
  caveat as M4)
- **M11 Network Effects**: only 5 years available, formula needs ≥6 for a clean
  two-window test — scored conservatively. Approximated windows: latest 3yr (FY23→FY26)
  CAGR ≈7.3%, prior 3yr (FY22→FY25) CAGR ≈15.3% — momentum is decelerating, not
  accelerating, and overall Revenue CAGR (14.94%) is below the ≥20% threshold for the
  next band either way → **score 0**
- **M12 Negative WC/Float**: WC days positive and >45 in every year (122-150 range,
  FY22-FY26) → band >45 → **score 0**

**Moat score total: 1+0+3+3+0+0+0+0+0+3+0+0 = 10/60**

Moat profile (bars, ●=present ≥3, ○=absent):
```
M1  ○ (1)   M2  ○ PEER DATA NEEDED   M3  ● (3)   M4  ● (3)
M5  ○ PEER DATA NEEDED   M6  ○ (0)   M7  ○ (0)   M8  ○ (0)
M9  ○ PEER DATA NEEDED   M10 ● (3)   M11 ○ (0)   M12 ○ (0)
```

Moats confirmed (score ≥3): 3 (M3 Capital Efficiency, M4 Customer Stickiness,
M10 Switching Costs) → **Moat classification: MODERATE** (2-3 present)

---

## CLASSIFICATION

Data confidence: 5 years of trend data (FY22-FY26) → band "5-6 lower" → flag: **may not
have seen a full cycle** (the FY22-FY23 peak includes what MDA text elsewhere describes
as a post-COVID recovery / alloys-furnace-ramp period; FY24-FY25 look more like a
normalization). This is a confidence flag only — it does not meet the 3-4yr LIMITED
threshold, so **no history_downgrade** is applied.

Grand total = Core (47) + Moat (10) = **57/160**

Classification matrix: Core 47 falls in the 40-59 band → **AVERAGE** (moat tier does not
change the outcome at this Core band per the matrix).

Deal-breaker overrides checked:
1. Block A <8 → not triggered (11)
2. Block B <8 → not triggered (10)
3. Median ROCE <10% → not triggered (22%)
4. Cumulative CFO/PAT <0.50 → not triggered (1.86x)
5. Pledge >15% → not triggered (N/A, no evidence)
6. ND/EBITDA >3x AND IC <3x → not triggered (1.40x / 6.89x)
7. Revenue declined in majority of years → not triggered (1 of 4)
8. PAT negative in any of last 3 years → not triggered
9. History <3 years → not triggered (5 years)

**No deal-breakers triggered. Classification stands at AVERAGE from the Core-score
matrix alone.**

---

## DECISION LINE

PERMAGNET scores **AVERAGE (Core 47/100, Moat MODERATE 10/60, Grand Total 57/160)** on a
5-year standalone trend window with only 2 years of full audited financial-statement
detail available in the provided documents. The score is depressed as much by disclosure
gaps as by fundamentals: Block E lost 10 of its 20 points to N/A fields (3-year promoter
change, pledge %) that a shareholding filing would likely resolve, and 10 of 12 moat
tests are blocked entirely by missing peer data. The one clear fundamental depressor is
Block C (Growth, 6/20): a decelerating PAT trend (CAGR 2.5% vs revenue CAGR 14.9%,
C4 = −12.4pp) and a FY22-23 ROCE/ROE peak that has not been re-approached (A4 = 0). The
FY26 consolidated cash-flow deterioration (Block B trend) is a subsidiary-driven
(Quantum Magnetics) capex-and-debt event, not a parent-business cash-quality signal —
standalone FCF stayed positive both years. This is flagged for downstream stages, not
halted; per pipeline rules there is no STOP verdict at Gate 0.

---
```yaml
stage: B01-gate0
company: "PERMAGNET"
run_date: "2026-08-19"
model: claude-sonnet-5
status: complete
input_gaps:
  - "no PERMAGNET screener CSV this run; all financials extracted directly from AR-FY26 / RESULTS-Q4FY26 / RESULTS-Q1FY27"
  - "no announcements folder provided"
  - "NO-CONCALL MODE"
  - "no shareholding filing: E2 (3-yr promoter change) and E3 (pledge %) not in provided documents, scored N/A/0"
  - "no peer/competitor financial data provided: 10 of 12 moat tests (M2,M5,M6,M7,M8,M9,M11 partially, M9) blocked, scored 0 PEER DATA NEEDED where applicable"
  - "full audited BS/CF line-item detail available for only 2 years (FY25-FY26); FY22-FY24 only available via the AR's own 5-yr KPI-chart aggregates (standalone)"
  - "sector_cap_row in manifest ('Agri processing') is a known collect_to_repo defect, not used anywhere in this scorecard"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE (Core 47/100). Historical depressors: A4 ROCE decline latest-vs-earliest (31%->16%, -15pp, score 0); C2/C4 PAT CAGR 2.5% vs Revenue CAGR 14.9% (score 0 both); Block E lost 10/20 pts to genuine data gaps (E2, E3 both N/A, not adverse findings); Block B computed on only a 2-yr consolidated window and shows FY26 FCF swinging to -25.75cr, driven by the pre-revenue Quantum Magnetics subsidiary's debt-funded capex ramp (assets 46.58cr, FY26 net loss 5.62cr, RESULTS-Q4FY26 p.18) rather than the parent business, which stayed FCF-positive standalone both years."
data_years: 5
fy_range: "FY22 to FY26"
blocks: {A: 11, B: 10, C: 6, D: 15, E: 5}
core_score: 47
moat_score: 10
grand_total: 57
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers: []
history_downgrade: false
data_notes:
  - "C1/C2 CAGR computed on Total Income (proxy for Revenue, includes ~2-3% Other Income) for FY22-FY24 since Revenue-from-Operations by year is not in the provided documents outside FY25/FY26; AR-FY26 p.12."
  - "PAT chart values (FY22-FY24) reconcile to Total Comprehensive Income basis, not pre-OCI 'Profit for the period'; difference immaterial to banding (<=0.30cr)."
  - "Block D debt figure includes lease liabilities, matching the company's own 'Total Debt to Equity' KPI methodology (verified by recomputation)."
  - "Net debt nets only Cash & Cash Equivalents, not 'Other Bank Balances' (~23.49cr consol.); if netted, ND/EBITDA would be ~0.85x (D1 score 4) instead of 1.40x (score 3) -- basis stated for downstream re-check."
  - "Block B (B1-B3) computed on CONSOLIDATED FY25-FY26 only (2 yrs, below the 3-yr minimum); B4 uses the STANDALONE 5-yr WC-days series instead since that is the only multi-year series available -- basis mismatch flagged."
  - "M4/M10 5-point 'stability' sub-criteria not independently verifiable (FY22-FY24 receivable-day-only detail not provided); scored on the verifiable growth-year-count criterion."
  - "E2: available 1-yr promoter-holding comparison (not the required 3-yr) shows the group essentially flat, ~58.00% to ~58.01%; not scored per 'never estimate', shown for context only."
loss_to_profit_swings: []
block_b_trend: "deteriorating -- consolidated FCF swung from +10.07cr (FY25) to -25.75cr (FY26) as capex more than doubled to 43.34cr against CFO of only 17.59cr, driven by the Quantum Magnetics subsidiary buildout; standalone-only FCF stayed positive both years (+8.70 FY25, +3.63 FY26)."
analyst_note: "The low Core/Moat scores read worse than the underlying parent business: Block E lost half its points to genuine disclosure gaps (no shareholding filing this run), and 10 of 12 moat tests are peer-data-blocked, not fundamentally failed. The one real fundamental depressor is growth quality -- PAT has decoupled from revenue (CAGR 2.5% vs 14.9%) and ROCE/ROE have not re-approached their FY22-23 peak, which itself may reflect a post-recovery/one-off alloys-furnace-ramp base rather than a sustainable run-rate (5-yr window flagged as possibly not a full cycle). The FY26 consolidated cash and leverage deterioration is entirely attributable to the pre-revenue Quantum Magnetics subsidiary (46.58cr assets, 0.78cr revenue, 5.62cr loss) funded by 61.48cr of new consolidated long-term borrowing -- the standalone parent stayed FCF-positive and under 0.25x D/E throughout. Downstream stages should treat the subsidiary capex/loss trajectory as a distinct, separately trackable risk factor from the core engineering/current-sensing business."
```
