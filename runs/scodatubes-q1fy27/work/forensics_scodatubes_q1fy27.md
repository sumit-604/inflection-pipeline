# A3 FORENSIC NOTES — Scoda Tubes Limited (SCODATUBES), Q1 FY27, Doctype: results (RE-RUN vs CORRECTED A1 extract + CORRECTED A2 ledger)

Agent: A3 Forensic Notes | Model: claude-opus-4-8 | Conservative bias
Extract: `/home/user/inflection-pipeline/runs/scodatubes-q1fy27/work/extract_results_scodatubes_q1fy27.txt` (289 lines; body 1-204 unchanged, A1 corrections + footing proof 205-289)
Ledger: `/home/user/inflection-pipeline/runs/scodatubes-q1fy27/work/ledger_results_scodatubes_q1fy27.md`
Prior-quarter extract: NONE (first quarterly run) — EoM/entity/dropped-slide diffs not performable this cycle.
Units: Rs Millions as filed; Rs Cr = Millions x 0.1.

Reconciliation: 100%. Every A2 ledger unit read verbatim at its A1 line before judging — 25 line items (lines 81-112), 7 notes (115-127), 3 zero-standing (93/97/111), 1 agenda item (38-39), 4 auditor paras (158-185), 1 entity (123-124), 3 signatory blocks (51-53/141-143/188-197). All four columns foot 20/20 on the corrected grid (extract lines 257-289).

RE-RUN CONTEXT: The prior pass ran on the PDF's embedded (Adobe Paper Capture) text layer, which carried a systematic "7 rendered as 1" digit substitution across the three comparative columns. Prior F14 caught it. A1 has re-extracted at 400 DPI OCR reconciled to arithmetic footing and corrected the digits in place. This checklist runs on the CORRECTED numbers. The correction materially changes the headline read (see F14-2).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F8-1 | F8 | L96 Current tax; L98 Deferred tax; L94 PBT | 96, 98, 94 | "Current tax ... 6.25" / "Deferred tax liability / (asset) ... 11.22" | FORWARD-SIGNAL | Q1FY27 current cash tax is only 8.9% of PBT (6.25/69.97) vs 25.17% statutory; total ETR 25.0% is normal only because a deferred-tax LIABILITY charge of 11.22 (16.0% of PBT, ~1,624 bps) carries it. DTL build = accelerated tax depreciation on the new welded plant. Timing shield, not a rate cut: reverses to higher cash tax / ETR step-up as the DTL unwinds. Current-tax share of PBT collapsed from 20.4% (Q1FY26) / 27.5% (Q4FY26) / 22.1% (FY26) to 8.9%. |
| F9-1 | F9 | L102 OCI remeasurement | 102 | "Re-measu rements of t he defined benefit s plans ... 1.71" | AMBIGUOUS | Single-quarter OCI remeasurement 1.71 EXCEEDS the full prior year FY26 of 1.18, on a sign-flipping series (Q1FY26 +1.47, Q4FY26 (1.47), Q1FY27 +1.71). Per F9 rule, a single quarter exceeding the full prior year = actuarial assumption change (discount rate / plan-asset return / salary escalation). Absolute size immaterial (Rs0.17 Cr) but signals an assumption reset to verify at the Annual Report. |
| F10-1 | F10 | L110/L112 EPS; L106 Paid-up; L99 PAT | 110, 106, 99 | "Basic / Dil uted from Continuing Opera tion (in Rs.) ... 1.44" | AMBIGUOUS | EPS comparatives do NOT reconcile to corrected PAT / paid-up shares. Paid-up flat Rs599.09M (=59.909M shares) at all four period-ends. Only Q1FY27 ties (52.50/59.909 = 0.88). Q1FY26 filed EPS 1.44 implies ~49.2M weighted shares (70.83/1.44), ~18% below the 59.9M the flat paid-up line implies; FY26 6.79 implies ~57.2M. Points to a FY25/FY26 capital action (dilution) or an unrestated EPS base. As filed, EPS fell 1.44 -> 0.88 = -38.9% YoY, WORSE than PAT -25.9%, i.e. per-share earnings hit is amplified by a larger share base. Unreconstructable from this bare filing. |
| F14-1 | F14 | whole comparative grid | 205-289 | "systematic '7 rendered as 1' digit substitution across the Q1FY27, Q4FY26 and Q1FY26 comparative columns ... flagged by A3 finding F14" | CONFIRMATORY-NEGATIVE | DATA-INTEGRITY CATCH (the value of this pipeline). Source PDF's embedded text layer corrupted 7->1 across the three comparative columns. Prior A3 F14 footing tests caught it. A1 re-extracted via 400 DPI tesseract OCR reconciled to the five footing identities; corrected digits written in place (e.g., Q1FY26 PAT 10.83 -> 70.83, line 99; Q1FY26 raw-material 142.49 -> 742.49, line 85; FY26 Total Expenses 4,164.89 -> 4,764.89, line 91). All 4 columns now foot 20/20 (lines 257-289). Record preserved so the miss shows as caught, not erased. |
| F14-2 | F14 | L81 Revenue; L94 PBT; L99 PAT; L89 Depn; L88 Finance | 81, 94, 99, 89, 88 | "Profit / (l oss) for t he perfod ... 52.50 ... 70.83" | FORWARD-SIGNAL | Consequence of the F14-1 correction: the corrected base FLIPS the headline. On the corrupt base (Q1FY26 PAT 10.83) Q1FY27 PAT 52.50 read as ~+385% growth; corrected it is Rs5.25 Cr vs Rs7.08 Cr = PAT -25.9% YoY, PBT -24.6% (69.97 vs 92.75), while revenue ROSE +27.6% (1,243.45 vs 974.17). Negative operating leverage driven below EBITDA: depreciation +162.8% (41.31 vs 15.72) and finance costs +27.0% (64.81 vs 51.04) = the debt-funded new-capacity (welded plant) fixed-cost signature hitting the P&L BEFORE the revenue/margin ramp. Gross material margin actually improved (net material 68.0% of rev vs 70.8%); the entire PAT decline sits in depreciation + finance. |
| F14-3 | F14 | Note 1 | 115 | "for the quarter and year ended June 30, 2026 have been reviewed" | CONFIRMATORY-NEGATIVE | Note-drafting slip: "quarter AND year ended June 30, 2026" — this is a quarter-ended interim filing; the audited year ended is March 31, 2026 (per the table header and Note 6). Copy-paste from an annual template. Individually immaterial; with the OCR-uncertain MD name (line 51 "Jagrutkushar Rameshbhai", possibly "Jagrutkumar", unconfirmed), the garbled Chairman raw OCR (line 141) and the uncaptured auditor partner name (lines 188-197), a cumulative governance/data-capture data point. |

Line references are to the A1 extract. Quotes reproduce OCR spacing/artifacts verbatim.

---

## CHECKLIST SCORECARD (all 17; every check marked)

| # | Check | Status | One-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | PASS | 3 ZERO_STANDING rows all blank in all 4 periods and all standard SEBI template placeholders: Exceptional items (L93, anticipates one-off gains/impairment/restructuring), Earlier year taxes (L97, anticipates prior-year tax true-ups — blank confirms F8 has no earlier-year adjustment), EPS Discontinued Operations (L111, anticipates discontinued ops). No anomaly. |
| F2 | Standalone vs consolidated decomposition | N.A. | Standalone-only filing; Note 5 (L123): "does not have any subsidiary, joint venture or associate company as on June 30, 2026." No consolidated statement exists — no S-vs-C gap to decompose. |
| F3 | Shell-entity detection | N.A. | No subsidiaries (Note 5, L123). No consolidated cost lines to compare. |
| F4 | Unaudited contribution ratio | N.A. | No JV/associate/component auditors; auditor report carries no Other Matters paragraph (A2 sec 4, lines 179-185). Zero PAT rests on unreviewed numbers. |
| F5 | Going concern / EoM scope tracking | PASS | Auditor expressed unmodified conclusion (L179-185); no Emphasis of Matter and no Going Concern paragraph present. No prior quarter to verbatim-diff (first run). |
| F6 | Forward-commitment phrase mining | PASS | Full lexicon sweep of the 7 notes (L115-127) and board letter (L34-45): no hits ("expected to", "will be", "underway", "commenc", "shall be completed", "board has approved [capex]", "intends to" all absent). Bare Reg 33 filing — Commitment Register empty. |
| F7 | Hedge phrase mining | PASS | No hedge lexicon hits in notes. Only Note 7 (L127) "regrouped / restated, wherever considered necessary" — standard regrouping boilerplate, not a newly-added hedge about revenue lumpiness or customer concentration. |
| F8 | Tax forensics | FINDING | F8-1: current cash tax only 8.9% of PBT; ~1,624 bps deferred-tax timing shield from DTL build on new-plant accelerated depreciation; future ETR step-up risk. Earlier-year taxes nil (L97) — clean on that leg. |
| F9 | OCI forensics | FINDING | F9-1: Q1FY27 remeasurement 1.71 (L102) exceeds full FY26 1.18 on a sign-flipping series = assumption change; verify actuarial assumptions at AR. |
| F10 | Share count and dilution | FINDING | F10-1: paid-up flat Rs599.09M / Basic=Diluted (no spread), but filed EPS comparatives do not reconcile to corrected PAT / share count (only Q1FY27 ties); EPS -38.9% YoY as filed exceeds PAT -25.9%. Points to an unreconstructable FY25/FY26 capital action or unrestated EPS base. |
| F11 | Reserves and net worth tie-out | PASS | Other Equity 3,304.00 (FY26 audited, L107) + paid-up 599.09 (L106) = net worth Rs3,903.09M (Rs390.31 Cr) at 31 Mar 2026; internally consistent. No third-party figure (rating/slide) in this bare filing to reconcile against; Q1FY27 balance sheet not in scope of a Reg 33 interim. Paid-up consistency question cross-refs F10-1. |
| F12 | Segment forensics | N.A. | Single segment; Note 4 (L122): "dealing in manufacturing of stainless-steel (SS) pipes and tubes only. Hence, segment reporting ... is not applicable." No segment assets/liabilities table exists. Welded-vs-seamless split and utilisation therefore UNDISCLOSED -> monitorable (re-engagement trigger 8), logged in ND register below. |
| F13 | Board outcome beyond the results | PASS | Sole agenda item = approval of the Q1 unaudited results + LRR (L38-39). Sweep of L34-46 found no AR/AGM/record-date/dividend/director appointment or resignation/auditor change/ESOP/capital-raising enabling resolution. Nothing schedules a Role-6 AR event or funding round from this letter. |
| F14 | Note drafting / extraction integrity | FINDING | F14-1 extraction digit-corruption caught + corrected (comparatives now foot 20/20, L205-289); F14-2 corrected base flips the headline read to PAT -25.9% YoY (forward signal); F14-3 Note 1 "quarter and year ended June 30, 2026" drafting slip + signatory capture gaps. |
| F15 | Entity list diffs | N.A. | Single standalone entity (Note 5, L123); no prior-quarter entity list (first run). No additions/deletions/renames/relationship changes performable. |
| F16 | Presentation-specific (dropped/reframed disclosures) | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 | Concall-specific (silence audit) | N.A. | Doctype is a results filing, not a concall transcript. (Silence on the deteriorating metrics is instead captured as the ND register / management questions below, and half-yearly concall cadence remains a Notion-flagged concern.) |

GATE A3: PASS — 17/17 checks marked, zero blanks. F1-F15 applied (F2/F3/F4/F12/F15 structurally N.A. with basis stated), F16/F17 N.A. per doctype.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| (none) | — | — | — |

No forward-commitment phrases present. This is a bare Reg 33 interim: no capex/commissioning/approval/tender language in the notes or board letter to date-track. Every catalyst on the Notion checklist (welded commercial production, BHEL/NTPC tender, RINA + Bureau Veritas marine approvals, first marine PO) is UNADDRESSED in this filing and rolls forward as a silence item.

---

## ND (NON-DISCLOSURE) REGISTER / MONITORABLES — unverifiable from this filing

This bare Reg 33 interim carries no balance sheet, no cash flow statement, and no segment table. The following Notion tripwires / re-engagement triggers CANNOT be tested and each becomes an A4 management question / carry-forward monitorable. Conservative bias: unverifiable ≠ resolved.

| Monitorable | Notion ref | Why unverifiable here | Forward read |
|-------------|-----------|-----------------------|--------------|
| Inventory days (>180 tripwire; <170 by Q2, <150 by Q4 target) | Trigger 2; thesis-break | No balance sheet in a Reg 33 interim. But Changes in inventories (L86) = (156.14) vs (52.47) Q1FY26 = a +198% YoY inventory BUILD, far outpacing revenue +27.6% -> working-capital absorption continuing off the FY26 217-day base. | Bear-leaning; likely CFO drag. Verify inventory days at H1 / AR. |
| H1 CFO positive AND cumulative FY22-FY27 CFO/PAT >0.30x | Trigger 1; THESIS BROKEN IF <0.30x | No cash flow statement filed. Prior concern H1 FY26 CFO -Rs51 Cr unaddressed. | Thesis-break test open; the inventory build (L86) points the wrong way. |
| Receivables growth <= revenue growth (2 consecutive q) | Trigger 7 | No balance sheet. | Untestable; monitor at H1. |
| Welded / seamless utilisation; welded commercial revenue >Rs30 Cr Q3/Q4 | Triggers 4, 8 | Note 4 single-segment aggregation (L122) suppresses the split. | The depreciation +162.8% (L89) confirms the welded plant is capitalised and depreciating; revenue contribution not separable. |
| Customer concentration (top customer <20%, Note 36) | Trigger 3; prior 26.7% single-customer FY25 | Interim filing carries no Note 36. | Hidden-concentration concern unresolved. |
| Marine approvals (RINA + Bureau Veritas) + first marine PO | Trigger 6 (imminent Jun-Sep 2026) | No operational disclosure in a bare filing. | Silence; ask on concall. |
| BHEL/NTPC tender (volumes >Rs75 Cr) | Trigger 5; THESIS BROKEN IF lost/<Rs75 Cr | No disclosure. | Silence; ask. |
| FY27 EBITDA margin sustained >=14% all quarters | Trigger 9 | Computable: Q1FY27 operating EBITDA (ex other income) Rs159.79M / rev = 12.85%, vs 14.57% Q1FY26 (-172 bps); including other income 14.16% vs 16.37%. | On either basis, margin compressed YoY; trigger 9 already at risk in Q1. |

---

## FORWARD-SIGNAL NARRATIVE

The corrected grid rewrites the quarter. On the corrupt embedded-text base (Q1FY26 PAT 10.83), Q1FY27 PAT of 52.50 would have printed as roughly +385% YoY — a false blowout. Corrected, Q1FY27 PAT is Rs5.25 Cr against Rs7.08 Cr a year ago: PAT DOWN 25.9%, PBT down 24.6%, and EPS down 38.9% (1.44 -> 0.88 as filed), even as revenue grew 27.6% to Rs124.35 Cr. This is the core forward signal, and it only exists because the pipeline's footing tests caught the digit corruption (F14). Preserving the catch on the record is the point.

The decline is textbook debt-funded pre-ramp negative operating leverage. Gross material economics did not deteriorate — net-of-inventory material cost improved to 68.0% of revenue from 70.8%. The entire earnings hit sits below EBITDA: depreciation jumped 162.8% (Rs4.13 Cr vs Rs1.57 Cr) as the new welded plant was capitalised and began depreciating, and finance costs rose 27.0% (Rs6.48 Cr vs Rs5.10 Cr) on the debt that funded it. Fixed costs of new capacity are in the P&L; the revenue and margin ramp that is meant to absorb them is not yet. Operating EBITDA margin compressed ~172 bps YoY to 12.85%, putting the Notion 14%-all-quarters trigger at risk in the very first quarter.

Two second-order signals compound the read. Tax (F8): current cash tax is only 8.9% of PBT; a Rs1.12 Cr deferred-tax liability charge (16% of PBT, ~1,624 bps) is doing the work to keep the headline ETR near-statutory. That is an accelerated-depreciation timing shield tied to the same new plant — flattering after-tax profit now and reversing to higher cash tax later. Dilution (F10): the filed EPS comparatives do not reconcile to PAT over the flat Rs599.09M paid-up base (only Q1FY27 ties), implying a FY25/FY26 share-count increase that is not reconstructable from this bare filing; per-share earnings fell harder than PAT. OCI (F9) flags a defined-benefit assumption change (a single quarter, 1.71, exceeding the full prior year, 1.18) to verify at the AR.

Everything that would let us weigh the ramp against the fixed-cost drag — cash flow, inventory days, welded utilisation and revenue, customer concentration, order-book progress — is absent from this Reg 33 interim. Conservative call: the quarter confirms the fixed-cost hit landing ahead of the volume; the offsetting evidence is unverifiable and must be pulled as management questions. Nothing here re-rates the AVOID stance.

## MANAGEMENT QUESTIONS FOR A4 (FORWARD-SIGNAL + AMBIGUOUS findings + ND monitorables)

1. (F14-2 / F8-1) Depreciation rose 162.8% and finance costs 27.0% YoY while PAT fell 25.9%. What is the commissioned welded-plant gross block now depreciating, the full-quarter run-rate depreciation and interest once fully ramped, and the welded revenue and utilisation expected to absorb them by Q3/Q4 FY27?
2. (F8-1) Current tax is 8.9% of PBT this quarter with a Rs1.12 Cr deferred-tax charge. What is the DTL balance and its expected reversal profile — i.e., when does cash-tax ETR normalise toward 25%?
3. (F10-1) Filed EPS comparatives do not reconcile to PAT over the flat Rs599.09M paid-up: Q1FY26 EPS 1.44 implies ~49.2M weighted shares vs 59.9M today. What FY25/FY26 capital action explains this, and are prior-period EPS restated per Ind AS 33?
4. (F9-1) The Q1 defined-benefit remeasurement (1.71) exceeds all of FY26 (1.18). Which actuarial assumption changed (discount rate, salary escalation, plan-asset return)?
5. (ND) H1 FY27 CFO and cumulative FY22-FY27 CFO/PAT — is the >0.30x thesis-break line intact given the Rs15.6 Cr inventory build this quarter?
6. (ND) Inventory days at Q1 FY27 vs the 217-day FY26 base and the <170 by Q2 target?
7. (ND) Welded commercial-production revenue and welded/seamless utilisation; BHEL/NTPC tender status and volume; RINA + Bureau Veritas marine approvals and first marine PO; top-customer concentration (still >26.7%?).

---

```yaml
stage: A3-forensics
company: "SCODATUBES"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/scodatubes-q1fy27/work/forensics_scodatubes_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F8-1", check: "F8", line: "96,98,94", classification: "FORWARD-SIGNAL", implication: "Current cash tax 8.9% of PBT; ~1,624 bps deferred-tax timing shield (DTL build on new-plant accelerated depreciation); future ETR step-up risk"}
  - {id: "F9-1", check: "F9", line: "102", classification: "AMBIGUOUS", implication: "Q1FY27 OCI remeasurement 1.71 exceeds full FY26 1.18 on sign-flipping series = actuarial assumption change; verify at AR"}
  - {id: "F10-1", check: "F10", line: "110,106,99", classification: "AMBIGUOUS", implication: "EPS comparatives do not reconcile to corrected PAT over flat Rs599.09M paid-up (only Q1FY27 ties); implies FY25/FY26 capital action; EPS -38.9% YoY as filed exceeds PAT -25.9%"}
  - {id: "F14-1", check: "F14", line: "205-289", classification: "CONFIRMATORY-NEGATIVE", implication: "Embedded-text-layer 7->1 digit corruption across 3 comparative columns, caught by prior F14, corrected via 400 DPI OCR + footing; comparatives now foot 20/20; miss recorded as caught"}
  - {id: "F14-2", check: "F14", line: "81,94,99,89,88", classification: "FORWARD-SIGNAL", implication: "Corrected base flips headline: PAT -25.9% YoY (5.25 vs 7.08 Cr), PBT -24.6%, on revenue +27.6%; debt-funded new-capacity fixed-cost signature (depreciation +162.8%, finance +27.0%) landing before the revenue/margin ramp"}
  - {id: "F14-3", check: "F14", line: "115", classification: "CONFIRMATORY-NEGATIVE", implication: "Note 1 drafting slip 'quarter and year ended June 30, 2026' (template carry-over) plus signatory capture gaps; cumulative governance/data-quality data point"}
forward_signals: ["F8-1", "F14-2"]
ambiguous: ["F9-1", "F10-1"]
commitments: []
gate_a3: pass
blank_checks: []
```
