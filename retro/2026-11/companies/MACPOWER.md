# MACPOWER — Macpower CNC Machines Ltd
Run folders read: runs/macpower-2026-07-30 (origin/claude/macpower-pipeline-g9ouq4; folder on 259 branches)
Company file: companies/MACPOWER.md (origin/claude/macpower-pipeline-g9ouq4; 1 branch)
Q1 FY27 outcome dated 29-Jul-2026; run dated 2026-07-30 (base case built after Q4 FY26 and Q1 FY27 results). No Q2 FY27 result in any file.

## Our base case

### Forward FY27 EPS derivation (operator basis: ONE-YEAR-FORWARD; FY27 EPS not published, DERIVED)

- FY26 revenue = Rs 333.18 cr (B10). Guidance FY27 revenue growth +28-30% (B10 guidance_revenue_growth_fy27_pct) -> FY27 revenue Rs 426.5 cr (+28%) to Rs 433.1 cr (+30%).
- PAT margin band: FY26 9.72% (B10 pat_margin_pct); Q1 FY27 ~10.1% (B10 note). Use 9.5%-10.15%.
- Shares = 1.0007 crore (B10 shares_crore; the B10 shares_million:100.042 was a 10x transcription slip, corrected — EPS 33.86 on PAT Rs 33.87 cr anchors 1.0007 crore).

| Case | FY27 Revenue | PAT margin | FY27 PAT | Forward FY27 EPS |
|------|--------------|-----------|----------|------------------|
| Bear | Rs 426.5 cr (+28%) | 9.5% | Rs 40.5 cr | **Rs 40.5** |
| Base | Rs 429.8 cr (+29%) | 10.0% | Rs 43.0 cr | **Rs 43.0** |
| Bull | Rs 433.1 cr (+30%) | 10.15% | Rs 44.0 cr | **Rs 44.0** |

**Forward FY27 EPS used: Bear Rs 40.5 / Base Rs 43.0 / Bull Rs 44.0.** The deliberation preview used ~Rs 44 (my bull end). Base Rs 43.0 is the conservative midpoint of the Rs 42-44 band. FY26 (Year 0) EPS Rs 33.86 (B10).
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/11-valuation.md §SECTION 2 Forward FY27 EPS derivation L110-122

- Base EPS CAGR (FY27 onward, over the 3-year hold) = **18%** — anchored to historical 3-yr PAT CAGR 18.1% (B10); the 28-30% near-term guidance is front-loaded into FY27 and decelerates.
- Bull EPS CAGR = **24%** — grade B permits bull use; set at the SOM-implied 24.3% ceiling (B10 som_implied), guidance-supported. (Grade B -> Bull is a genuine bull, not Base+5%.)
| Revenue growth within capacity? | 28-30% is capex/land-gated (13-acre + shared 60-acre catalyst); base uses guidance | ~ (capacity-gated) |
| Margins require the unprecedented? | Base 10.0% PAT margin is near FY26 9.72% + Q1 10.1%; no heroics | Yes |
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/11-valuation.md §Three-year EPS CAGR and sanity checks L126-127,L137-138

## Management guidance and promised catalysts

  - {item: "Revenue/EBITDA/PAT growth guidance", number: "25-30%", timeframe: "FY26 and FY27", stated_in: "Q2 FY26 call"}
  - {item: "FY26 EBITDA target", number: "Rs 50 cr", timeframe: "FY26", stated_in: "Q2 FY26 call"}
  - {item: "FY27 revenue growth guidance", number: "28-30%", timeframe: "FY27", stated_in: "Q4 FY26 call"}
  - {item: "FY27 capacity utilisation target", number: "~90%", timeframe: "FY27", stated_in: "Q4 FY26 call"}
  - {item: "FY27 total capex", number: "Rs 30-40 cr", timeframe: "FY27", stated_in: "Q4 FY26 call"}
  - {item: "AMC/service/spares revenue", number: "Rs 5-6 cr/year", timeframe: "FY27", stated_in: "Q4 FY26 call"}
  - {item: "60-acre land, latest date", number: "n/a", timeframe: "3-4 months from May-2026 board (~Aug-Oct 2026)", stated_in: "Q4 FY26 call"}
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/blocks/B05-concall.yaml §B05 guidance block L23-24,L36-40

  - {item: "13-acre Metoda land capex", number: "Rs 30-35 cr", timeframe: "immediate/FY27", stated_in: "Q4 FY26 call"}
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/blocks/B05-concall.yaml §B05 guidance block L35

    - {promised_in: "Q2 FY26 call (restating a Q1 FY26 promise)", promise: "60-acre land acquired by end of December 2025", outcome: "missed", explanation: "external-blame: government approval/policy timing"}
    - {promised_in: "Q3 FY26 call", promise: "Land signing expected Feb end / March first-second week 2026", outcome: "missed", explanation: "external-blame: Gujarat local elections delaying defence-and-aeronautics land policy"}
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/blocks/B05-concall.yaml §B05 promise_delivery L51-52

| FY27 revenue growth guidance | 28-30% | FY27 | Q4 FY26 call (p.4, 9, 20) |
| FY27 capacity utilisation target | ~90% | FY27 | Q4 FY26 call (p.9) |
| FY27 total capex | ₹30-40 cr | FY27 | Q4 FY26 call (p.21) |
| AMC/service/spares revenue | ₹5-6 cr/year | FY27 | Q4 FY26 call (p.12) |
| 60-acre land — latest date | n/a | "one or two months" / "3-4 months" from May-2026 board (i.e. ~Aug-Oct 2026) | Q4 FY26 call (p.22-23) |
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/05-concall.md §Guidance table L49-53

- **60-acre govt land**: WEAKENING / repeated timeline slippage. Promised "December end" (Q2 FY26 call, itself already a restatement of a Q1 FY26 promise) → pushed to "March 2026" (Q3 FY26 call) → still unsigned as of Q4 FY26 call, now vaguely "3-4 months." Flagged directly by analyst Hiren Modi in the Q4 FY26 call, who noted the plan was first announced in March 2024. **Timeline slippage, three-plus quarters running.**
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/05-concall.md §Trigger notes L59

- 60-acre govt land: token paid, signing withheld to benefit from new Gujarat policy (effective land cost ~25% of guideline vs 50%); intended for 10,000-machine greenfield (5,000 yr1 scaling to 10,000; 3-4x revenue potential).
- Legally registered leasehold ~13 acres (9 usable + 4 green zone), 30-year lease, nominal rate.
- Purpose: debottleneck, component production/backward integration, future capacity, world-class assembly.
- ~Rs 50 cr capex (building/infra, P&M, utilities); funded via internal accruals and/or debt; completion target 12 months; consultant Taknik (Ahmedabad).
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/operator-context-2026-07-30.md §Operator context (non-anchored) L34,L40-42

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)

| **Revenue (Latest FY)** | Rs 333.18 cr | (FY26 results Q4/FY26, P&L Statement, p.3; year-ended column) |
| **EBITDA (Latest FY)** | Rs 53.90 cr | (B09-tam.yaml, cross-verified from 16.2% margin x 333.18 cr revenue) |
| **EBITDA Margin** | 16.2% | (B05 concall, B09 tam; Q4 FY26 shows flat 16.2% vs Q1 FY27; deliberation confirms stagnant margin at 16.2%) |
| **PAT (Latest FY)** | Rs 33.87 cr | (FY26 results P&L, "Profit for the period" row, year-ended 31-Mar-2026 column, p.3) |
| **PAT (TTM including Q1 FY27)** | Rs 43.45 cr approx. | (FY26 PAT 33.87 cr + Q1 FY27 PAT 9.58 cr, less Q1 FY25 PAT 4.55 cr ≈ 38.9 cr; operator-supplied screener trailing PAT from "Stock P/E 38.1" interpretation) |
| **PAT Margin (FY26)** | 9.72% | (FY26 results P&L, 33.87 / 333.18 calculation; consistent with B03 note of 9.72% vs disclosed 12.00% margin discrepancy) |
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/10-valinputs.md §LATEST FINANCIALS TABLE L28-33

- Order book 31 Mar 2026 ~Rs 406 cr (+23% YoY). Domestic bids submitted ~Rs 652.5 cr; under evaluation ~Rs 376 cr; total ~Rs 1,028 cr. NEXA ~40% of pending order book.
- Q1 FY27 revenue Rs 95.24 cr, +56.1% YoY. EBITDA Rs 15.43 cr, +94.8% YoY, margin 16.2%. PAT Rs 9.58 cr, +110.3% YoY, PAT margin 10.1%. "Highest ever Q1".
- Order book 30 Jun 2026 ~Rs 456 cr. NEXA ~40% of pending order book (higher base). Domestic bids submitted ~Rs 739 cr; under evaluation ~Rs 304 cr; total ~Rs 1,043 cr.
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/operator-context-2026-07-30.md §Operator context Q4 FY26 and Q1 FY27 (non-anchored) L28,L46-47

| Financial-guidance delivery | Strong — FY26 growth, EBITDA target, and order-book target all met or exceeded; Q1 FY27 results (₹95.24 cr revenue, +56.1% YoY, per inputs/results outcome PDF) run well ahead of the 28-30% FY27 guidance given in the Q4 FY26 call |
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/05-concall.md §Financial-guidance delivery L194

## Management's stated reasons

| 7 | Q3 FY26 call | Land signing expected "Feb end / March first, second week" 2026 | ❌ Missed | External-blame: Gujarat local elections delaying corporation/district administration and the new defence-and-aeronautics policy (Q4 FY26 call, p.5, 22-23) |
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/05-concall.md §Promise table L81

- **60-acre govt land**: WEAKENING / repeated timeline slippage. Promised "December end" (Q2 FY26 call, itself already a restatement of a Q1 FY26 promise) → pushed to "March 2026" (Q3 FY26 call) → still unsigned as of Q4 FY26 call, now vaguely "3-4 months." Flagged directly by analyst Hiren Modi in the Q4 FY26 call, who noted the plan was first announced in March 2024. **Timeline slippage, three-plus quarters running.**
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/05-concall.md §Land slippage L59

## Risk flags raised before the result, and any overruling
Run dated 2026-07-30, after the Q4 FY26 and Q1 FY27 results. Flags raised in the run:

  - "60-acre govt land repeatedly slipped (Dec-2025 -> Mar-2026 -> undated as of Jun-2026 call); JV and 25% EBITDA margin story both gated on it"
  - "Market share stated as 4.5% (Q2/Q3 FY26 calls) vs 1%/2% (Q4 FY26 call) not explicitly reconciled"
  - "Machine unit volumes withheld every quarter"
  - "First-time finished-goods inventory (~80 machines) booked as cost without matching revenue, tied to customer subsidy/loan documentation lags"
quarters_analysed: ["Q2 FY26", "Q3 FY26", "Q4 FY26"]
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/blocks/B05-concall.yaml §B05 flags L8-12

- **PAT +33%** is booked while CFO/PAT sits at 0.41x and the business consumed net cash, stretched MSME suppliers 81.4%, and liquidated its entire investment book to stay funded (B02 #2, #6, #9).
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/15-devil.md §15-devil L53

## Verdicts and dates

## DECISION STATUS AND ENTRY ZONE
- As of 2026-07-30: AVOID (on valuation). Evidence gate PROCEED WITH CAVEATS; FTTCP transition composite +2/8 DEEP WATCH leaning AVOID; devil's advocate SURVIVES (AVOID over-determined).
- Entry zone Rs 440 to 550 (additive 25.0x forward EPS Rs 43), MoS Rs 440. RRM-default zone is deeper at ~Rs 291 to 364.
Source: origin/claude/macpower-pipeline-g9ouq4:companies/MACPOWER.md §DECISION STATUS AND ENTRY ZONE L8-10

AVOID on valuation at CMP Rs 1,481.
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/final/fttcp-recommendation.md §Valuation decision L9

PROCEED WITH CAVEATS
The cap to PROCEED WITH CAVEATS comes from FLAG-CASH resolving INDETERMINATE. Selection rule 3 applied: FLAG-CASH is active, and an INDETERMINATE cash determination caps the verdict at PROCEED WITH CAVEATS rather than PROCEED WITH FLAGS, with the missing evidence named below. FLAG-GATE0 is active but does not cap. FLAG-PROMOTER is not triggered.
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/final/gate-recommendation.md §Gate disposition L1,L5

| **Listed ≥12 months (as of run date 2026-07-30)** | YES | Listed on NSE SME Emerge 2018; migrated main board Aug-2020 (B08 p.12-13, board's report notes; >6 years as of run date) |
Source: origin/claude/macpower-pipeline-g9ouq4:runs/macpower-2026-07-30/outputs/reports/10-valinputs.md §Listing status L178

## Lessons archive mentions
NOT FOUND (no MACPOWER or Macpower line in LESSONS_ARCHIVE.md or LESSONS_ARCHIVE_offmain_lines.md)
