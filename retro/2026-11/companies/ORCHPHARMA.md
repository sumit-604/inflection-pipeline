# ORCHPHARMA — Orchid Pharma Ltd
Run folders read: runs/orchpharma-2026-09-06 (origin/claude/orchpharma-2026-09-06-runs-bx6lcr)
Company file: companies/ORCHPHARMA.md (origin/main)

## Our base case
NOT FOUND. "Stages 10 and 11 did not run, no valuation exists, and no investment call is made or implied"
Source: origin/claude/orchpharma-2026-09-06-runs-bx6lcr:runs/orchpharma-2026-09-06/outputs/final/gate-recommendation.md L7
"No entry zone set. No valuation has run." Source: origin/main:companies/ORCHPHARMA.md §DECISION STATUS
Tracker thresholds only (not a base): "| 1 | Q2 FY27 revenue | above Rs 290 cr | Nov-2026 | holds revenue at STARTING; below it, revenue drops to STAGNANT |"
Source: outputs/final/fttcp-draft.md L281
Signed model: "Fixed cost about Rs 350 cr a year; breakeven about Rs 260 cr revenue a quarter; each extra Rs 100 cr revenue adds about Rs 33 cr EBITDA [INFERENCE from FILED]."
Source: origin/main:companies/ORCHPHARMA.md §SIGNED MENTAL MODEL DECLARATION

## Management guidance and promised catalysts
  - {item: "Base-business FY27 EBITDA margin ~12%", number: "analyst-proposed, management assented", timeframe: "FY27", stated_in: "Q4 FY26 call, PDF p.8"}
  - {item: "FY27 revenue growth target 10-15%", number: "management-volunteered in response to an open question", timeframe: "FY27", stated_in: "Q4 FY26 call, PDF p.10"}
  - {item: "7-ACA commissioning", number: "Q1 CY2027 (~March 2027)", timeframe: "target", stated_in: "Q4 FY26 call, PDF p.4"}
  - {item: "7-ACA mechanical completion", number: "September 2026", timeframe: "target, checkpoint dropped from later disclosure", stated_in: "Q3 FY26 call, PDF p.3"}
  - {item: "Cefiderocol production readiness", number: "December 2026", timeframe: "target", stated_in: "Q3 FY26 call, PDF p.8"}
  - {item: "Enmetazobactam US deal", number: "within 12 months", timeframe: "~Nov 2026", stated_in: "Q2 FY26 call, PDF p.9"}
  - {item: "Cefiderocol India commercial launch (revised)", number: "Q3 of FY28 (~Oct-Dec 2027)", timeframe: "target", stated_in: "Q1 FY27 call, PDF p.14"}
Source: runs/orchpharma-2026-09-06/outputs/blocks/05-concall.yaml guidance L36-56
    - {promised_in: "Q3 FY26 call", promise: "Base-business FY27 EBITDA margin ~10%", outcome: "partial", explanation: "Revised up to ~12% via an analyst-proposed figure the following quarter; Q1 FY27 actual ~8.2%, below both targets; management declined to reaffirm a number when asked directly"}
Source: 05-concall.yaml L70
"Exblifep US licence: target expired 30-Sep-2026 [MGMT, May call]." Source: origin/main:companies/ORCHPHARMA.md §ACTIVE TRIPWIRES

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
  - {item: "Q4 FY26 revenue / EBITDA (standalone)", number: "Rs238cr, ~flat YoY; EBITDA Rs42.3cr", timeframe: "reported", stated_in: "Q4 FY26 call, PDF p.3"}
  - {item: "FY26 full-year revenue / EBITDA (standalone)", number: "Rs811cr vs Rs922cr; EBITDA Rs101cr vs Rs155cr", timeframe: "reported", stated_in: "Q4 FY26 call, PDF p.3"}
  - {item: "FY26 revenue (restated combined)", number: "Rs1,233cr vs Rs1,398cr FY25; gross margin ~32% vs ~36%; opex ~Rs353cr both years", ...}
  - {item: "Q1 FY27 revenue / margin / EBITDA (combined)", number: "Rs304cr vs Rs263cr (+15% YoY); GM 33% vs 30%; EBITDA Rs25cr vs Rs10cr", timeframe: "reported", stated_in: "Q1 FY27 call, PDF p.4"}
Source: 05-concall.yaml L43-44, L51-52
| Net profit ratio | 2.81% | 10.20% | (72%) | lower profits |  Source: outputs/reports/fy26-ar-extraction.md L309
"Q1 FY27 actual quarterly EBITDA margin ~8.2% (Rs25cr / Rs304cr)" Source: outputs/reports/05-concall.md L167
Q2 FY27: NOT FOUND

## Management's stated reasons
"management calls the market 'cutthroat'" (Q1 FY27 revenue context) Source: outputs/final/fttcp-draft.md L28
NOT FOUND for the ~8.2% margin ("management declined to reaffirm a number when asked directly", 05-concall.yaml L70)

## Risk flags raised before the result, and any overruling
NOT FOUND before the Q1 FY27 result (Aug-2026 call); the run is dated 2026-09-06.
Flags in this run after the result: "Q1 FY27 sequential revenue reconstructed as a ~13-17% decline even as the only figure presented was +15% YoY off a trough comparator" (05-concall.yaml L104)
Tripwires set at Halt 1 2026-09-28: "Gross margin below 31% for two quarters in a row." "Falsifier: material cost at or above 63.5% four quarters after COD."
Source: origin/main:companies/ORCHPHARMA.md §ACTIVE TRIPWIRES
Rulings: "2026-09-28: Halt 1 decision changed from SHALLOW WATCH to PROCEED (operator...)"; promoter items "ruled STRUCTURE concerns, not integrity findings"
Source: origin/main:companies/ORCHPHARMA.md §OPERATOR RULINGS

## Verdicts and dates
"## VERDICT: REWORK" (Verifier B red flag coverage 39%, below 60%) Source: outputs/final/gate-recommendation.md L5, L9
"Spear: OVERRIDE 2026-09-06 (operator)" Source: companies/ORCHPHARMA.md §SPEAR
"Halt 1 decision: PROCEED (2026-09-28, operator). Supersedes SHALLOW WATCH of the same day." Source: companies/ORCHPHARMA.md §HALT 1 GATE
"1. Core cephalosporin API ... CONVERTER (spread business, price taker)." Source: companies/ORCHPHARMA.md §SIGNED MENTAL MODEL DECLARATION

## Lessons archive mentions
"[2026-09-06] ORCHPHARMA phase 1 (first workup ...). Gate cleared by operator spear OVERRIDE ... Six things broke or dragged. (1) CORPUS OCR CORRUPTION" Source: LESSONS_ARCHIVE.md L647-652
ORCHPHARMA 2026-09-06 phase 1 items, all OPEN: LESSONS_ARCHIVE.md L1013-1023; REWORK remediation-cycle question L1111
