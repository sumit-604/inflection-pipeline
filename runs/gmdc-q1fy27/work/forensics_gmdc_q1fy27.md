# A3 FORENSIC NOTES — GMDCLTD Q1 FY27 (Reg 33 Unaudited Results, Standalone + Consolidated)

Company: Gujarat Mineral Development Corporation Ltd (GMDCLTD, BSE 532181)
Quarter: Q1 FY27 (quarter ended 30 June 2026) | Doctype: results
A1 extract: `runs/gmdc-q1fy27/work/extract_results_gmdc_q1fy27.txt` (547 lines, 10 pages)
A2 ledger: `runs/gmdc-q1fy27/work/ledger_results_gmdc_q1fy27.md`
EPS correction memo read first and applied: standalone 5.13, consolidated 5.14, Basic=Diluted (no Basic-vs-Diluted finding raised for current quarter).
Ledger reconciliation: all 14 ledger tables read verbatim at cited lines; 119 line-items + 9 notes + 3 agenda + 10 auditor paras + 5 entities + 6 signatures = 100% reconciled.

Classification scheme (per orchestrator task): RED-FLAG / AMBIGUOUS / FORWARD-SIGNAL / BENIGN. AMBIGUOUS and FORWARD-SIGNAL findings are flagged for A4 to convert into management questions.

Prior-thesis note: no existing GMDC Notion page and no `companies/GMDC.md`. First-look quarterly. No prior Decision Status, entry zone, tripwires, or monitoring checklist. Checks that would reference a monitoring checklist are marked N.A. with reason "no prior thesis on file" (F17), not PASS or FINDING.
Evidence-gap note: no prior-quarter extract/ledger supplied. Where a verbatim prior-period diff is required (F5 EoM diff, F15 entity-list diff), the diff is flagged as an evidence gap, never asserted as "no change."

Period columns throughout: Q1 FY27 (30/06/2026, Unaudited) | Q4 FY26 (31/03/2026, Audited quarter) | Q1 FY26 (30/06/2025, Unaudited) | FY26 (31/03/2026, Audited year).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F1 | TABLE 5 row 6 / TABLE 6 row 6 | 184 (std) / 304 (cons) | "GST Compensatory Cess Exp ... –" (nil Q1FY27 vs 79.03 in Q1FY26, 130.75 FY26) | FORWARD-SIGNAL | An ~79 cr/quarter cost line has gone to nil YoY. Structural cost/margin change; confirm it is permanent removal of the coal/lignite compensatory cess and whether it drops to margin or is revenue-offset. |
| A3-02 | F2 | TABLE 14 + TABLE 6 rows 4-12 | 305, 309 (cons) vs 185, 189 (std) | consolidated Other Expenses "212.81" (Q4) / "564.18" (FY26) vs standalone "182.47" / "530.75" | AMBIGUOUS | S-vs-C PAT gap swung from -12.25% of standalone PAT (Q4FY26: 194.09 vs 221.18) to +0.26% (Q1FY27: +0.42). >5pp swing. Prior-period consolidated operating lines diverge from standalone (~+33 cr Other Expenses FY26) which pure equity-method JV/associate consolidation cannot produce; divergence vanishes this quarter. Ask what was line-consolidated in FY26 (subsidiary? eliminations? Q4 true-up) that is absent now. |
| A3-03 | F6 | TABLE 1 items 2,3 / TABLE 2 note 2 | 55-56, 73, 267-268 | "We will submit further details in due course on execution of MOU"; "the Company shall receive 1 equity share ... of GSPL Transmission Limited (GTL) for every 3 shares held in GEL" | FORWARD-SIGNAL | Three dateable commitments: GNFC MoU execution, IREL MoU execution, and pending GTL demerger share entitlement. Feed Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. |
| A3-04 | F7 | TABLE 1 items 2,3 | 53-54, 72 | "to jointly evaluate opportunities across the coal-to-chemicals value chain"; "to explore collaboration opportunities in the Rare Earth Elements (REE) sector" | AMBIGUOUS | Both MoUs framed with hedge verbs ("evaluate", "explore") plus "further details in due course" — non-binding, early-stage optionality, not committed capex. Ask for scope, capex envelope, timeline, and JV/ownership structure. |
| A3-05 | F8 | TABLE 5 rows 16-18 | 197 (std) | "Short/ (excess) provision of earlier years ... 0.07" (Q1FY27); "(47.02)" (Q4FY26) | AMBIGUOUS | Earlier-year tax adjustment non-zero this quarter (0.07, immaterial), but Q4FY26 carried a 47.02 cr earlier-year credit that flattered Q4 (ETR 15.5%). Q1FY27 standalone ETR ~28.3% runs above statutory 25.17%. Ask for the normalized/guided tax rate. |
| A3-06 | F9 | TABLE 5 row 22 / TABLE 6 row 23 | 204 (std) / 328 (cons) | "Income tax relating to these items ... (21.79)" | AMBIGUOUS | Tax on OCI items of (21.79) cr exceeds the pre-tax OCI gain itself (FVTOCI 12.75 + remeasurement 2.56 = 15.31), flipping OCI net to (6.48); ~10x the full FY26 OCI-tax of (1.99) and reverses the +1.85 credit booked in Q1FY26. Single-quarter OCI swing exceeds full prior year = likely valuation/assumption change, probably tax on the FVTOCI equity revaluation tied to the GSPC->GEL swap (Note 2). Verify assumptions at Annual Report. |
| A3-07 | F12 | TABLE 9 rows 7,10,15 | 235, 244 (std) | Segment Results Power "(6.00)"; Segment Assets Mining "4,095.65" (vs 2,930.20 Q1FY26) | FORWARD-SIGNAL | Power segment swung to an operating loss of (6.00) in Q1FY27 from +10.59 in Q1FY26 and lost (79.61) across FY26 — a persistent value drag on ~1,224 cr of Power assets. Mining segment assets grew ~+40% YoY (2,930 -> 4,096) = capex build in the profit engine; trend the accretion rate as a capex proxy. Ask what is driving Power losses and Mining asset build. |
| A3-08 | F13 | TABLE 1 items 2,3 | 53-55, 72 | "coal-to-chemicals value chain using gasification technologies, including Underground Coal Gasification (UCG)"; "Rare Earth Elements (REE) sector" | FORWARD-SIGNAL | Board approved two strategic-diversification MoUs beyond the results: GNFC coal-to-chemicals / UCG and IREL REE. New optionality register entries and catalyst events pending MoU execution; schedule tracking. No AR/AGM/director-term item present in this filing. |
| A3-09 | F14 | TABLE 11 | 386 vs 455; 388 vs 457; 387 vs 456; 417 | "Swamim Gujarat Flourspar" (note) vs "Swarnim Gujarat Fluorspar" (auditor); "Industries" vs "Industrial"; "Infrastructure" vs "Infra"; title "CONSOLIDTED" | BENIGN | Entity-name and title inconsistencies across tables (some OCR artifact, "Industries/Industrial" a substantive drafting variance). Individually immaterial, cumulatively a low-grade drafting/governance data point. No action beyond noting. |
| A3-10 | F15 | TABLE 2 note 2 / TABLE 3 note 4 | 261-268 (std) / 397-402 (cons) | "the Company's investment in Gujarat State Petroleum Corporation Limited (GSPC) stood extinguished ... received 10 equity shares ... of Gujarat Energy Limited (GEL) for every 305 shares held in GSPC" | BENIGN | Investment-entity relationship change: GSPC extinguished via Composite Scheme, replaced by GEL shares (received 12 May 2026) and a pending GTL entitlement. Non-cash; links to the F9 OCI-tax anomaly (FVTOCI portfolio recomposition). Separately, the 5 consolidated JV/associate entities cannot be diffed against a prior quarter — no prior ledger supplied = evidence gap. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING LINES | FINDING | 3 ZERO_STANDING classes read (GST Cess, Exceptional Items, Reserves). Exceptional line anticipates one-offs (FY26 522.65, GSPC-related); Reserves blank per interim convention (benign). GST Compensatory Cess nil vs 79.03 Q1FY26 = A3-01 forward signal. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | Q1FY27 gap +0.42 (0.26%) = pure JV equity share; but S-vs-C PAT gap swung >5pp from -12.25% (Q4FY26) and prior-period consolidated operating lines diverge from standalone. A3-02. |
| F3 SHELL-ENTITY DETECTION | PASS | Q1FY27 consolidated cost lines identical to standalone (5.78/86.70/42.27/6.61/33.33/436.78/144.07) because all 5 consolidated entities are equity-method JV/associates, not line-consolidated subsidiaries; no Going Concern EoM to reconcile. |
| F4 UNAUDITED CONTRIBUTION RATIO | PASS | Para 6 (line 471-480): Rs 0.42 cr JV/associate share, unaudited/management-certified = 0.26% of consolidated PAT (163.43); below 10% threshold; "not material to the Group" (line 480). Prior periods (0.33)/(0.10)/(0.71) all immaterial, no YoY jump of concern. |
| F5 GOING CONCERN / EoM SCOPE | PASS | No Emphasis of Matter or Going Concern paragraph in either review report; consolidated conclusion unmodified (line 482), standalone clean (line 529-536). Prior-quarter verbatim EoM diff not runnable = evidence gap (noted, not asserted). |
| F6 FORWARD-COMMITMENT MINING | FINDING | "will submit further details ... on execution of MOU" (55-56, 73), "shall receive ... GTL" (267-268), "board ... approved" (51, 70). Three dateable commitments = A3-03. See Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | "evaluate" (53), "explore" (72) + "in due course" hedges frame both MoUs as non-binding optionality = A3-04. |
| F8 TAX FORENSICS | FINDING | Earlier-year adjustment non-zero (0.07, line 197); Q4FY26 47.02 cr earlier-year credit non-recurring; Q1FY27 standalone ETR ~28.3% > statutory 25.17% = A3-05. |
| F9 OCI FORENSICS | FINDING | OCI tax (21.79) exceeds pre-tax OCI (15.31), single-quarter swing exceeds full FY26 OCI-tax (1.99); likely FVTOCI revaluation tied to GSPC->GEL = A3-06. |
| F10 SHARE COUNT AND DILUTION | PASS | Paid-up equity constant 63.60 cr all periods (line 208/333); no corporate action to share count; Basic=Diluted after correction memo (no dilutive instruments). EPS 5.13 x 31.80 cr shares = 163.1 cr ties to PAT 163.01. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Net worth ties internally: paid-up 63.60 + reserves 7,004.97 (std) / 7,009.14 (cons) at FY26 (line 209/334); consolidated exceeds standalone by 4.17 cr (cumulative JV/associate equity pickup). No third-party benchmark available (first-look) so no gap detectable. Interim quarter reserve columns blank per convention. |
| F12 SEGMENT FORENSICS | FINDING | Power segment operating loss (6.00) vs +10.59 Q1FY26 and (79.61) FY26; Mining assets +40% YoY (2,930->4,096) = capex build = A3-07. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Two board-approved strategic MoUs beyond results: GNFC coal-to-chemicals/UCG (48-56), IREL REE (68-73) = A3-08. No AR/AGM/director-term item in filing. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Entity-name variances across note vs auditor tables ("Swamim/Swarnim", "Flourspar/Fluorspar", "Industries/Industrial", "Infra"), title typo "CONSOLIDTED" = A3-09. Note-vs-letter "audit/limited review" wording is consistent (no mismatch). |
| F15 ENTITY LIST DIFFS | FINDING | GSPC investment extinguished -> GEL received / GTL receivable (261-268/397-402) = investment-entity relationship change (A3-10); 5 JV/associate entities cannot be diffed vs prior quarter = evidence gap. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results, not a presentation deck (per applicability rule). |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results, not a concall transcript; and no prior Notion thesis / monitoring checklist on file (first-look). Nothing to silence-audit. |

Scorecard tally: PASS 5 (F3, F4, F5, F10, F11) | FINDING 10 (F1, F2, F6, F7, F8, F9, F12, F13, F14, F15) | N.A. 2 (F16, F17). No blanks. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Execute MoU with GNFC (coal-to-chemicals value chain, gasification incl. UCG); submit further details on execution | "in due course" (undated) | Board Outcome item 2, lines 48-56 | initiated (board-approved, execution pending) |
| Execute MoU with IREL(India) Ltd (Rare Earth Elements collaboration); submit further details on execution | "in due course" (undated) | Board Outcome item 3, lines 68-73 | initiated (board-approved, execution pending) |
| Receipt of GTL shares: 1 equity share (Rs 10) of GSPL Transmission Ltd per 3 GEL shares, on demerger of gas transmission undertaking | on completion of GTL demerger (undated) | Note 2 (std) line 267-268 / Note 4 (cons) line 400-402 | underway (pending demerger) |
| Receipt of GEL shares: 10 equity shares (Rs 2) of Gujarat Energy Ltd per 305 GSPC shares, Record Date 12 May 2026 | 12 May 2026 | Note 2 line 264-265 / Note 4 line 399 | completed |

---

## FOR A4 — QUESTIONS TO GENERATE (AMBIGUOUS + FORWARD-SIGNAL findings)

- FORWARD-SIGNAL: A3-01 (GST cess removal — structural margin?), A3-03 (three commitments to track), A3-07 (Power segment losses / Mining capex build), A3-08 (GNFC + IREL MoUs — new optionality).
- AMBIGUOUS: A3-02 (S-vs-C operating-line divergence in prior periods — what was consolidated in FY26?), A3-04 (MoU scope/capex/timeline — how binding?), A3-05 (normalized tax rate above statutory), A3-06 (OCI tax anomaly / FVTOCI revaluation).
- BENIGN (no A4 question): A3-09 (drafting inconsistencies), A3-10 (GSPC/GEL/GTL non-cash swap; entity-diff evidence gap).

```yaml
stage: A3-forensics
company: "GMDCLTD"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gmdc-q1fy27/work/forensics_gmdc_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "184", classification: "FORWARD-SIGNAL", implication: "GST Compensatory Cess ~79 cr/qtr cost gone to nil YoY; structural margin change to confirm"}
  - {id: "A3-02", check: "F2", line: "309", classification: "AMBIGUOUS", implication: "S-vs-C PAT gap swung >5pp; prior-period consolidated operating lines diverge from standalone, unexplained by equity-method-only consolidation"}
  - {id: "A3-03", check: "F6", line: "55", classification: "FORWARD-SIGNAL", implication: "Three dateable commitments (GNFC MoU, IREL MoU, GTL shares) for promise-vs-delivery tracker"}
  - {id: "A3-04", check: "F7", line: "53", classification: "AMBIGUOUS", implication: "MoUs hedged as evaluate/explore, non-binding optionality; scope/capex/timeline unknown"}
  - {id: "A3-05", check: "F8", line: "197", classification: "AMBIGUOUS", implication: "Earlier-year tax adjustment non-zero; Q4 47.02 cr credit non-recurring; Q1FY27 ETR ~28.3% above statutory 25.17%"}
  - {id: "A3-06", check: "F9", line: "204", classification: "AMBIGUOUS", implication: "OCI tax (21.79) exceeds pre-tax OCI gain and full FY26 OCI-tax; likely FVTOCI revaluation tied to GSPC->GEL swap"}
  - {id: "A3-07", check: "F12", line: "235", classification: "FORWARD-SIGNAL", implication: "Power segment loss-making (6.00) vs +10.59 YoY and (79.61) FY26; Mining assets +40% YoY capex build"}
  - {id: "A3-08", check: "F13", line: "53", classification: "FORWARD-SIGNAL", implication: "Two board-approved strategic MoUs (coal-to-chemicals/UCG; REE) = new optionality and catalyst events"}
  - {id: "A3-09", check: "F14", line: "386", classification: "BENIGN", implication: "Entity-name and title drafting inconsistencies; cumulative low-grade governance data point"}
  - {id: "A3-10", check: "F15", line: "261", classification: "BENIGN", implication: "GSPC->GEL/GTL non-cash investment restructuring; prior-quarter entity-list diff not runnable (evidence gap)"}
forward_signals: ["A3-01", "A3-03", "A3-07", "A3-08"]
ambiguous: ["A3-02", "A3-04", "A3-05", "A3-06"]
commitments:
  - {commitment: "Execute MoU with GNFC (coal-to-chemicals / gasification incl. UCG)", implied_date: "in due course", ref: "lines 48-56", status_word: "initiated"}
  - {commitment: "Execute MoU with IREL(India) Ltd (Rare Earth Elements)", implied_date: "in due course", ref: "lines 68-73", status_word: "initiated"}
  - {commitment: "Receive GTL shares on gas-transmission demerger (1 per 3 GEL)", implied_date: "on GTL demerger completion", ref: "lines 267-268 / 400-402", status_word: "underway"}
  - {commitment: "Receive GEL shares (10 per 305 GSPC), Record Date 12 May 2026", implied_date: "2026-05-12", ref: "lines 264-265 / 399", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
