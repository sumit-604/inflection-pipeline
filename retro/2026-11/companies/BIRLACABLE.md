# BIRLACABLE — Birla Cable Limited
Run folders read: runs/birlacable-2026-08-20 (origin/claude/birlacable-pipeline-4rln8o)
Company file: NONE

## Our base case
```
L102: | Year | Revenue ₹ Cr | YoY | Basis |
L103: |---|---|---|---|
L104: | FY22 | NOT FOUND | NOT FOUND | No source in run folder |
L105: | FY23 | 792.20 | NOT FOUND | ACTUAL, screener data sheet, consolidated |
L106: | FY24 | 685.50 | −13.5% | ACTUAL, screener data sheet |
L107: | FY25 | 661.65 | −3.5% | ACTUAL, screener data sheet |
L108: | FY26 | 771.11 | +16.5% | ACTUAL, FY26 audited results 22-May-2026, p.2, ₹77,111.40 lakh |
L109: | FY27E | 924 | +19.8% | EXPECTED, illustrative |
L115: Quarterly, all ACTUAL: Q1 FY26 ₹176.44 Cr, Q2 ₹176.07 Cr, Q3 ₹204.51 Cr, Q4 ₹214.10 Cr, Q1 FY27 ₹266.64 Cr. Year on year for those quarters: plus 6.3%, minus 3.1%, plus 29.6%, plus 37.0%, plus 51.1%. Q1 FY27 is anchored to the 2 August 2026 filing, p.2, ₹26,663.67 lakh against ₹17,643.76 lakh.
L116: 
L117: How the expected columns are built, so nobody mistakes them for facts. FY27E takes the Q1 actual of ₹266.64 Cr and grows the FY26 figures for the other three quarters at 10.5%, the market growth rate from B09. From FY28 the line steps down to 2.9% a year, which is the ceiling B09 computes from the company's realistic share with no capacity expansion in flight. The emerging moat classification is NONE, and under the fade rule that means growth falls to industry rate immediately rather than holding. The capacity ceiling then binds below the industry rate, because CARE puts structured cable utilisation near 94% and capex is running at 12% of depreciation. Module B1 fails FY28 onward on that ground: the growth cannot be produced without capex the company is not spending.
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/final/fttcp-draft.md §TRANSITION 1 — REVENUE L102-117

```
L126: |---|---|---|---|
L127: | FY22 | NOT FOUND | NOT FOUND | No source in run folder |
L128: | FY23 | 63.16 | 7.97% | ACTUAL, derived from screener, reconciles to reported PBT ₹43.97 Cr |
L129: | FY24 | 40.46 | 5.90% | ACTUAL, reconciles to reported PBT ₹29.79 Cr |
L130: | FY25 | 32.69 | 4.94% | ACTUAL, reconciles to reported PBT ₹6.68 Cr |
L131: | FY26 | 46.97 | 6.09% | ACTUAL, reconciles to reported PBT ₹22.63 Cr |
L132: | FY27E | 86.9 | 9.41% | EXPECTED, illustrative |
L138: Quarterly operating margin, all ACTUAL: Q1 FY26 4.44%, Q2 4.12%, Q3 5.32%, Q4 9.46%, Q1 FY27 17.24%. Raw material cost was 74.3% of revenue in Q1 FY27 against 82.3% for FY26.
L139: 
L140: This name is flagged cyclical, so scenario margins come from the cycle and not from a trailing average. From the audited annual prints: peak 7.97% in FY23, trough 4.94% in FY25, full cycle average 6.23%. FY27E holds the Q1 actual and applies the full cycle average to the remaining three quarters. FY28 onward uses the full cycle average throughout. The rule deliberately refuses to let one quarter reset the cycle, and that is the whole reason the expected line drops back after FY27.
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/final/fttcp-draft.md §TRANSITION 2 — MARGIN L126-140

```
L150: | Year | PAT ₹ Cr | CFO ₹ Cr | CFO/PAT | Debtor days | Net debt ₹ Cr | Basis |
L151: |---|---|---|---|---|---|---|
L152: | FY22 | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | No source |
L153: | FY23 | 32.94 | −7.84 | −0.24x | 99.7 | 123.83 | ACTUAL |
L154: | FY24 | 22.14 | 15.82 | 0.71x | 113.7 | 161.88 | ACTUAL |
L155: | FY25 | 4.89 | 112.26 | 22.96x | 92.2 | 95.74 | ACTUAL |
L156: | FY26 | 16.90 | −20.71 | −1.23x | 96.1 | 128.94 | ACTUAL |
L157: | FY27E | 48.9 | 10 to 20 | 0.2x to 0.4x | 95 to 105 | 140 to 155 | EXPECTED, illustrative |
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/final/fttcp-draft.md §TRANSITION 3 — CASH CONVERSION L150-157 (PAT column)

## Management guidance and promised catalysts
```
L15: guidance:
L16:   - {item: "Dividend, FY26", number: "Rs 1.25/share (12.5%; ~Rs 375 lakh payout, 22.23% of standalone PAT)", timeframe: "recommended 22 May 2026, payable within 30 days of AGM (AGM held 3 Aug 2026)", stated_in: "AR Directors' Report, Dividend section; FY26R note 1"}
L17:   - {item: "Global OFC demand growth (industry data cited by management)", number: "+6.8% YoY, 136.70M FKM; global production +7.2% YoY", timeframe: "Q1 CY2026", stated_in: "AR Directors' Report, General & Corporate Matters"}
L18:   - {item: "India OFC demand growth (industry data cited by management)", number: "+9.9% YoY, 4.7M F-km", timeframe: "Q1 CY2026", stated_in: "AR Directors' Report, General & Corporate Matters"}
L19:   - {item: "OFC demand 'poised to strengthen'", number: "no company-specific number; qualitative only", timeframe: "FY 2026-27", stated_in: "AR MD&A, Industry Structure and Developments"}
L20:   - {item: "Amalgamation into VTL completion", number: "~10-12 months from 21 Mar 2026 board approval", timeframe: "expected ~Jan-Mar 2027", stated_in: "CARE rating rationale, 1 Apr 2026"}
L26:     - {promised_in: "AR MD&A/Directors' Report (board 22 May 2026)", promise: "OFC demand revival since late Mar 2026, poised to strengthen in FY27", outcome: "Q1 FY27 revenue +51.1%, PBT +2132%, net profit +2182% YoY, but no OFC-vs-copper segment split disclosed in Q1R", explanation: "Aggregate direction/magnitude validated; specific OFC-led mechanism unconfirmed"}
L27:     - {promised_in: "CARE rating rationale (1 Apr 2026), reporting management view", promise: "Management expects OFC demand revival from FY27", outcome: "Same Q1 FY27 aggregate delivery as above", explanation: "Directionally borne out, same segment-mix caveat"}
L28:     - {promised_in: "AR Directors' Report/FY26R (22 May 2026)", promise: "Dividend Rs 1.25/share for FY26, payable within 30 days of AGM", outcome: "AGM held on schedule 3 Aug 2026; payment window not yet closed as of run date", explanation: "Not yet assessable, excluded from tally"}
L29:     - {promised_in: "CARE rating rationale (1 Apr 2026)", promise: "Amalgamation into VTL completes in ~10-12 months from 21 Mar 2026", outcome: "As of 2 Aug 2026, still 'applications filed, awaiting NSE/BSE no-objection letters', identical to 22 May 2026 language", explanation: "Too early to grade; ~5 of 10-12 months elapsed"}
L33: credibility_basis: "AR (board 22 May 2026) forward view of OFC demand revival into FY27 was validated by Q1 FY27 results (filed 2 Aug 2026): revenue +51% YoY, PBT ~22x YoY; single-cycle evidence, segment-level OFC-vs-copper mix undisclosed so mechanism is unconfirmed; no quantified company guidance exists beyond dividend (not yet due); no-concall-mode caps grade below A regardless."
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/blocks/B05-concall.yaml §guidance/promise_delivery L15-33

```
L254: | 2 | Q2 FY27 EBITDA margin | Above 12% with raw material below 78% of revenue | 0 to 3m | Confirms the margin step change; margin moves toward FIRING and the whole card is rebuilt |
L255: | 3 | Q2 FY27 EBITDA margin, downside | Below 8% | 0 to 3m | Margin falls to STAGNANT; composite drops to +1 |
L256: | 4 | Q2 FY27 revenue | Above ₹250 Cr | 0 to 3m | Confirms revenue STARTING; below ₹200 Cr moves it back to DECLINING |
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/final/fttcp-draft.md §STEP 5 — MONITORING TRIGGERS L254-256

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
```
L108: | FY26 | 771.11 | +16.5% | ACTUAL, FY26 audited results 22-May-2026, p.2, ₹77,111.40 lakh |
L109: | FY27E | 924 | +19.8% | EXPECTED, illustrative |
L115: Quarterly, all ACTUAL: Q1 FY26 ₹176.44 Cr, Q2 ₹176.07 Cr, Q3 ₹204.51 Cr, Q4 ₹214.10 Cr, Q1 FY27 ₹266.64 Cr. Year on year for those quarters: plus 6.3%, minus 3.1%, plus 29.6%, plus 37.0%, plus 51.1%. Q1 FY27 is anchored to the 2 August 2026 filing, p.2, ₹26,663.67 lakh against ₹17,643.76 lakh.
L131: | FY26 | 46.97 | 6.09% | ACTUAL, reconciles to reported PBT ₹22.63 Cr |
L132: | FY27E | 86.9 | 9.41% | EXPECTED, illustrative |
L138: Quarterly operating margin, all ACTUAL: Q1 FY26 4.44%, Q2 4.12%, Q3 5.32%, Q4 9.46%, Q1 FY27 17.24%. Raw material cost was 74.3% of revenue in Q1 FY27 against 82.3% for FY26.
L156: | FY26 | 16.90 | −20.71 | −1.23x | 96.1 | 128.94 | ACTUAL |
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/final/fttcp-draft.md §TRANSITION 1-3 L108-156

```
L306:    investments ₹51.20 Cr book. OCI never enters EPS — Q1 FY27 OCI was ₹40.70 Cr
L378: The spread is the whole problem. Q1 FY27 alone contributed ₹10.23 of earnings per share, against ₹5.62 for the entire prior year. Choose trailing and the stock looks like it must de-rate from 50.7x to 7.7x, which is catastrophic. Choose forward and it is already trading below the destination multiple, which reads as cheap. Both are computed from the same audited and filed numbers.
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/final/fttcp-draft.md §HANDOFF TO VALUATION / P/E BASE CARD L306, L378
(No Q2 FY27 result in the files.)

## Management's stated reasons
NOT FOUND. No concalls held (manifest concalls_available false).
```
L33: credibility_basis: "AR (board 22 May 2026) forward view of OFC demand revival into FY27 was validated by Q1 FY27 results (filed 2 Aug 2026): revenue +51% YoY, PBT ~22x YoY; single-cycle evidence, segment-level OFC-vs-copper mix undisclosed so mechanism is unconfirmed; no quantified company guidance exists beyond dividend (not yet due); no-concall-mode caps grade below A regardless."
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/blocks/B05-concall.yaml credibility_basis L33

## Risk flags raised before the result, and any overruling
NOT FOUND. First file is dated 2026-08-20, after the 22-May-2026 and 2-Aug-2026 filings. No shortfall recorded for Q4 FY26 or Q1 FY27.

## Verdicts and dates
```
L1: REWORK
L2: 
L3: # Gate recommendation, phase 1
L4: 
L5: Company: Birla Cable Ltd (BIRLACABLE). Run date: 2026-08-20. Scope: phase 1 evidence only. Valuation runs in phase 3, so this file carries no decision, no entry zone and no exit multiple.
L6: 
L7: ## What this verdict judges
L8: 
L9: REWORK judges this run's analysis. It does not judge the company. The evidence stages produced a usable record on the balance sheet, the merger and the promoter. Two evidence stages did not audit what they were given, and the red flag verifier found the gap large enough that the run cannot be closed on their output.
L10: 
L11: Two binding inputs force the verdict under selection rule 1:
L12: 
L13: - Overall confidence is 15.4, below the 60 floor.
L14: - Verifier B's acceptance rate is 15%, below the 60% floor.
L15: 
L16: Either one alone forces REWORK. Company quality does not enter this test.
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/outputs/final/gate-recommendation.md L1-16

```
L1: company: Birla Cable Ltd
L2: ticker: BIRLACABLE
L3: cmp: 285.0
L4: market_cap_cr: 854.0
L5: run_date: 2026-08-20
L6: run_type: full
```
Source: origin/claude/birlacable-pipeline-4rln8o:runs/birlacable-2026-08-20/manifest.yaml L1-6

## Lessons archive mentions
```
L10: ===== LINES NOT ON MAIN, from origin/claude/birlacable-pipeline-4rln8o (+0 more branches) =====
L11: ## 2026-08-20 — BIRLACABLE (phase 1, /run-pipeline)
L12: - Verdict REWORK on verifier evidence: Verifier B found 26 independent red flags, stages 5/6 caught 4 (coverage 15.4%). Root cause per verifier: NO-CONCALL MODE stage 5 mined the AR/results narratives for statements but never audited the audited cash flow statement or balance sheet behind them; stage 6 read 12 peer transcripts for confirmation of BCL claims, not for complications (missed HFCL MD's price-top call, STL's refusal to corroborate pricing, the germanium/preform input squeeze, HFCL's direct fund-disbursement answer). Two B06 attribution errors (STL order-intake quote spliced into HFCL bullet; analyst words quoted as management) caught by both B and D.
L13: - 5 of 11 stage invocations returned the YAML block in the final response but omitted it from the written report; orchestrator extracted from response and appended to the report each time. No retry needed.
L14: - Known collector defects recurred exactly as catalogued: sector_cap_row wrong ("Specialty chemicals" for a telecom cable maker), screener P&L/BS/CF/Quarters CSVs label-only (Data_Sheet populated). Recorded in B00.
L15: - PDF tooling broken at session start exactly as catalogued (cffi backend); fixed with pip force-reinstall cffi, pre-extracted all 17 PDFs to page-marked .txt; no stage hit the render wall.
L16: - Stage-0 empty-folder pause delivered; operator answered "proceed with gaps" (announcements/shareholding/prospectus/research/presentation empty).
```
Source: origin/claude/birlacable-pipeline-4rln8o:LESSONS_ARCHIVE.md §2026-08-20 — BIRLACABLE (phase 1, /run-pipeline) L10-16 of LESSONS_ARCHIVE_offmain_lines.md (export)

