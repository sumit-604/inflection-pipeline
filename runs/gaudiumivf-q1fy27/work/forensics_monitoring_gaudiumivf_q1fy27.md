# A3 FORENSIC NOTES — GAUDIUMIVF Q1FY27 — DOCTYPE: MONITORING (Infomerics IPO-Proceeds Monitoring Agency Report, quarter ended June 30 2026)

Source extract: extract_monitoring_gaudiumivf_q1fy27.txt (816 lines, 24 pages)
Ledger reconciled: 39/39 fund-utilization rows + all 11 note bodies + all category counts read verbatim at cited lines. 100%.
Prior-quarter extract: NOT PROVIDED (this is the first MA report post-listing; F5/F15 verbatim diffs not possible).
Monitoring/Notion checklist for F17: NOT PROVIDED this run.

Framing note: this is a fund-utilization filing, not a P&L results statement. F2, F3, F8, F9, F10, F11 (standalone-vs-consolidated, shells, tax, OCI, dilution, net-worth) have no counterpart in a monitoring report and are marked N.A. with reason. Analytical weight is placed on the checks that DO apply to an IPO-monitoring filing: fund utilization, reclassification, evidence quality, deviations, forward commitments, delays, and governance. Several classic checks are repurposed to the monitoring context and the adaptation is stated explicitly (F4 -> evidence-verification quality; F12 -> idle-deployment as capex proxy; F16 -> reframed/reclassified object disclosure).

---

## FINDINGS TABLE

| id | check | ledger row ref | line(s) | verbatim quote | classification | forward implication |
|----|-------|----------------|---------|----------------|----------------|---------------------|
| FND-1 | F4 (adapted: unverified-evidence ratio) | §8 Note No.1 (EVIDENCE_GAP) | 475-477 | "relied upon management representations and supporting quotations for payments aggregating to ₹ 0.30 Crore (29.14% of ₹ 1.03 Crore of capex utilisation reviewed during the quarter) where tax invoices were pending receipt" | AMBIGUOUS | Nearly a third of the quarter's already-tiny capex is substantiated only by vendor quotations (Luxen Interior & Décor LLP, Shinelife Meditec LLP), not tax invoices. MA "may review such invoices during subsequent monitoring periods." A4 question: are these payments genuine deployed capex or advances that could reverse? Track invoice receipt next quarter. |
| FND-2 | F6 (forward-commitment mining) | §11 delay table + Board note | 617-624, 696-699 | "The expenditure originally proposed to be incurred during FY 2025-26 is now proposed to be incurred during FY 2026-27." / "Cost to be Incurred FY27 26.31 ... No. of Centres FY27 10" | FORWARD-SIGNAL | A dated, sized management promise: Rs 26.31 Cr and 10 new IVF centres in FY27. Against Rs 1.03 Cr actually deployed in Q1FY27, this is a steep back-loaded ramp. Feeds the Role 5 promise-vs-delivery tracker; the FY27 number is the metric to hold management to at each subsequent MA report. |
| FND-3 | F7 (hedge-phrase mining) | §8 Note No.2 / §12 restated para | 500-501 | "any further expenditure towards the Lucknow Hospital shall be funded from GCP proceeds, to the extent available and permissible, and/or from the Company's internal accruals" | FORWARD-SIGNAL | Pre-emptive hedge. GCP object is Rs 12.28 Cr total, of which Rs 5.76 Cr (Lucknow) + Rs 0.42 Cr TDS + Rs 0.06 Cr is already consumed and the head is capped at 25% of gross proceeds. The "and/or internal accruals" clause signals GCP headroom for Lucknow is nearly exhausted and future hospital spend will draw on operating cash. |
| FND-4 | F12 (adapted: idle deployment as capex proxy) | §8 row1 + §10 deployment table | 412, 568-589, 596-597 | "50.00 50.00 - 1.03 1.03 48.97" (capex object, 98% unspent) / FDs "27.00 ... 7.20%" / "includes accrued interest of ₹ 0.14 crore on fixed deposits" | CONFIRMATORY-NEGATIVE | CONFIRMS the same-quarter RESULTS filing: the New-IVF-Centres object is 98% unspent (Rs 48.97 Cr idle) and unutilised proceeds (Rs 55.97 Cr) sit in HDFC FDs of ~Rs 55.5 Cr at 7.20-7.27%. The Rs 0.14 Cr accrued FD interest here is the visible tip of the Rs 1.02 Cr FD interest the results filing flagged as flattering PBT. Growth capex is not being deployed; the "earnings" are treasury yield on unspent IPO cash. |
| FND-5 | F13 (board outcome beyond the numbers) | §11 Board note + §8 Note No.2 | 480-484, 636-647, 696-699 | "The Board of Directors ... at its meeting held on 28 May 2026, took note of the delay in utilisation of a portion of the IPO proceeds" / "The Board of Directors ... approved the establishment of Gaudium Women Hospital at Lucknow ... 30 years with a 15-year lock-in" | FORWARD-SIGNAL | Two governance events: (1) formal Board acknowledgement (28 May 2026) of the FY25-26 -> FY26-27 deferment of both the capex and the repayment objects; (2) Board approval of a 30-year Lucknow hospital lease (15-yr lock-in, 10% of monthly net revenue + Rs 3.00 Cr refundable deposit). Both foreshadow the FY27 deployment story and a new long-dated fixed obligation. Candidate Role 6 event: watch the FY26 Annual Report / Board's Report for the deferment and lease disclosure. |
| FND-6 | F14 (note-drafting inconsistencies) | §12 DUPLICATE_NOTE + date fields | 723-732 vs 495-504; 497/724 vs 194, 618 | "an amount of Rs. 5.76 crore incurred towards the Lucknow Hospital has been funded from the GCP proceeds ..." (Section 5 repeats Note No.2 verbatim) / "Prospectus dated February 25, 2026" | NEUTRAL-FACT | Section 5 restates the entire Note No.2 Lucknow paragraph word-for-word (no new information). Separately the report cites a "Prospectus dated February 25, 2026" while the issue period is Feb 20-24 2026 and listing is Feb 27 2026, and borrowings are "as at September 30, 2025" on a restated basis. Individually immaterial; cumulatively a drafting-care governance data point on a report whose entire value is verification rigour. |
| FND-7 | F16 (adapted: reframed / reclassified object disclosure) | §8 Note No.2 + §12 row1 (RECLASSIFICATION) | 125, 486-504, 708-711 | "(a) Deviation from the objects: Nil" / "the expenditure has not been classified under the earmarked capex object for establishment of IVF centres" / "Advance Payment for setting up ... 'Gaudium Women Hospital, Lucknow' 5.76" | AMBIGUOUS | Substance-over-form. Rs 5.76 Cr of real, growth healthcare capex (a new hospital) is routed through the General Corporate Purpose object, not the dedicated New-IVF-Centres capex object, while the report simultaneously certifies zero deviation. This REFINES the results-filing "98% capex object unspent" picture: growth capital IS being deployed, just off the earmarked line and into a facility that is a hospital rather than an IVF centre. A4 question: is a 30-year hospital lease a legitimate GCP use or an object-level reallocation presented as GCP to preserve the "Nil deviation" statement? Note GCP now carries a build the offer document never named. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing line items | PASS | ZERO_STANDING template lines (deviation "Nil" x2 line 125/127; Section 3 "Not Applicable"/"No" rows; cost-table revised-cost dashes; beginning-of-quarter nils) are the standard clean monitoring template. Beginning-of-quarter utilisation = 0 for both capex and repayment (line 412/427) confirms all deployment occurred within this quarter; nothing anomalous in the zero pattern itself. |
| F2 Standalone vs consolidated decomposition | N.A. | A monitoring report carries no standalone/consolidated financial statements; only a passing "restated consolidated" borrowings figure (line 531). No gap to compute. |
| F3 Shell-entity detection | N.A. | No entity-level cost lines (materials/employee/depreciation) to compare; no subsidiary decomposition in scope. |
| F4 Unaudited / unverified contribution ratio | FINDING | Adapted to evidence quality: Rs 0.30 Cr = 29.14% of the quarter's Rs 1.03 Cr capex verified on vendor quotations only, tax invoices pending (lines 475-477). See FND-1. |
| F5 Going concern / EoM scope tracking | N.A. | No going-concern or Emphasis-of-Matter paragraph in an MA report; and no prior-quarter extract supplied for a verbatim diff (first MA report post-Feb-2026 listing). |
| F6 Forward-commitment phrase mining | FINDING | Multiple dated/sized commitments: FY25-26->FY26-27 deferment, FY27 Rs 26.31 Cr / 10 centres, "ensures to utilise ... within the stipulated timeline." See FND-2 and Commitment Register. |
| F7 Hedge-phrase mining | FINDING | New pre-emptive funding hedge on Lucknow: "to the extent available and permissible, and/or ... internal accruals" (line 501). See FND-3. |
| F8 Tax forensics | N.A. | No ETR, deferred-tax, or P&L tax line. (TDS Rs 0.42 Cr in the GCP breakdown, line 712, is withholding on payments, not an effective-tax-rate datapoint.) |
| F9 OCI forensics | N.A. | No statement of other comprehensive income / actuarial lines in a monitoring report. |
| F10 Share count and dilution | N.A. | Share/issue structure stated once (1,13,92,500 fresh shares @ Rs 79, line 218-222); no EPS, no period-over-period paid-up capital movement, no dilutive-instrument table to analyse. |
| F11 Reserves and net-worth tie-out | N.A. | No balance sheet / other-equity disclosure; only third-party figure is Sep-30-2025 borrowings Rs 22.51 Cr (line 531), not a net-worth reconciliation. |
| F12 Segment forensics | FINDING | Adapted: the New-IVF-Centres object is the "pre-commissioning build" analog — 98% unspent (Rs 48.97 Cr, line 412), unutilised cash parked in FDs at 7.2% generating Rs 0.14 Cr accrued interest. Confirms results-filing idle-cash/FD-interest story. See FND-4. |
| F13 Board outcome beyond the results | FINDING | Board 28 May 2026 noted the deferment (lines 696-699) and approved the 30-year Lucknow hospital lease (lines 480-484). See FND-5. |
| F14 Note-drafting inconsistencies | FINDING | Section 5 (723-732) verbatim duplicates Note No.2 (495-504); minor date/entity inconsistencies (Prospectus "Feb 25 2026" vs issue Feb 20-24). See FND-6. |
| F15 Entity-list diffs | N.A. | No consolidation entity list; no prior-quarter MA report available for an additions/deletions/rename diff. |
| F16 Dropped / reframed disclosures | FINDING | Adapted to monitoring: Rs 5.76 Cr Lucknow growth capex reclassified through the GCP object rather than the earmarked New-IVF-Centres capex object, under a "Deviation: Nil" certification. See FND-7. |
| F17 Concall silence audit | N.A. | No concall transcript and no Notion monitoring checklist supplied for this document/run; no commitment-vs-silence cross-reference possible. |

Status tally: PASS 1 (F1) · FINDING 7 (F4, F6, F7, F12, F13, F14, F16) · N.A. 9 (F2, F3, F5, F8, F9, F10, F11, F15, F17). No blanks. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| # | commitment | implied date | ref (line) | status word |
|---|------------|--------------|------------|-------------|
| 1 | Capex originally for FY25-26 "now proposed to be incurred during FY 2026-27" | FY2026-27 | 696-699 | deferred / underway ("Ongoing", line 617) |
| 2 | Deploy Rs 26.31 Cr and open 10 new IVF centres in FY27 (then Rs 21.05 Cr/8 in FY28, Rs 2.63 Cr/1 in FY29) | FY27 / FY28 / FY29 | 622-624 | proposed |
| 3 | "The Company ensures to utilise the IPO proceeds within the stipulated timeline" | within stipulated (upto FY29) | 617-621 | committed |
| 4 | Repayment object completion | Upto FY27 | 669 | ongoing |
| 5 | GCP object completion | Upto FY27 | 676 | ongoing |
| 6 | Further Lucknow spend "shall be funded from GCP proceeds ... and/or from the Company's internal accruals" | ongoing | 500-501 | undertaken |
| 7 | Lucknow: "will place a refundable security deposit of ₹3.00 crore" and pay "10% of the monthly net revenue" over 30-yr lease (15-yr lock-in) | 30-yr lease from Board approval (28 May 2026) | 481-484 | board-approved |

---

## CROSS-DOCUMENT RECONCILIATION FLAGS (for A4)

- CONFIRMS (results filing "98% capex object unspent, Rs 48.97 Cr idle"): line 412 shows exactly Rs 48.97 Cr unutilised on the New-IVF-Centres object. FND-4.
- CONFIRMS (results filing "Rs 1.02 Cr FD interest flattering PBT"): lines 568-589 show ~Rs 55.5 Cr in HDFC FDs at 7.20-7.27%; line 596 shows Rs 0.14 Cr accrued FD interest on unutilised proceeds. Same idle-cash-on-treasury-yield mechanism. FND-4.
- REFINES ("is real growth capex being deployed?"): YES but off the earmarked line — Rs 5.76 Cr Lucknow hospital via GCP (lines 495-504, 708). So the "98% unspent capex object" overstates how little growth capital is moving; it just is not moving through the IVF-centre object. FND-7.
- DEVIATION STATUS: report certifies "Deviation from the objects: Nil" (line 125) and auditor remark "No deviations" (line 311), yet FND-7 shows an object-level substance question A4 must resolve. Flagged AMBIGUOUS, not asserted as a deviation.
- FORWARD COMMITMENT on deployment timeline: FY27 Rs 26.31 Cr / 10 centres (FND-2) is the hard number to hold management to.

---

```yaml
stage: A3-forensics
company: "GAUDIUMIVF"
quarter: "q1fy27"
doctype: "monitoring"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gaudiumivf-q1fy27/work/forensics_monitoring_gaudiumivf_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: FINDING
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-1", check: "F4", line: "475-477", classification: "AMBIGUOUS", implication: "29.14% of quarter capex on vendor quotations not tax invoices; track invoice receipt next quarter"}
  - {id: "FND-2", check: "F6", line: "617-624,696-699", classification: "FORWARD-SIGNAL", implication: "FY27 promise of Rs 26.31 Cr and 10 new centres vs Rs 1.03 Cr deployed; back-loaded ramp to hold management to"}
  - {id: "FND-3", check: "F7", line: "500-501", classification: "FORWARD-SIGNAL", implication: "GCP headroom for Lucknow near-exhausted; future hospital spend shifts to internal accruals"}
  - {id: "FND-4", check: "F12", line: "412,568-589,596-597", classification: "CONFIRMATORY-NEGATIVE", implication: "Confirms results-filing idle capex object (Rs 48.97 Cr) and FD interest on unspent IPO cash flattering PBT"}
  - {id: "FND-5", check: "F13", line: "480-484,636-647,696-699", classification: "FORWARD-SIGNAL", implication: "Board formalised FY25-26->FY26-27 deferment and approved 30-yr Lucknow lease; FY26 AR deep-dive candidate"}
  - {id: "FND-6", check: "F14", line: "723-732", classification: "NEUTRAL-FACT", implication: "Section 5 verbatim duplicates Note 2; minor date inconsistencies; drafting-care governance data point"}
  - {id: "FND-7", check: "F16", line: "125,486-504,708-711", classification: "AMBIGUOUS", implication: "Rs 5.76 Cr hospital capex routed via GCP under a Nil-deviation certification; object-level reallocation question for A4"}
forward_signals: ["FND-2", "FND-3", "FND-5"]
ambiguous: ["FND-1", "FND-7"]
commitments:
  - {commitment: "Capex deferred from FY25-26 to FY26-27", implied_date: "FY2026-27", ref: "696-699", status_word: "deferred"}
  - {commitment: "Deploy Rs 26.31 Cr / 10 new IVF centres in FY27 (21.05Cr/8 FY28, 2.63Cr/1 FY29)", implied_date: "FY27-FY29", ref: "622-624", status_word: "proposed"}
  - {commitment: "Utilise IPO proceeds within stipulated timeline", implied_date: "upto FY29", ref: "617-621", status_word: "committed"}
  - {commitment: "Repayment object completion", implied_date: "upto FY27", ref: "669", status_word: "ongoing"}
  - {commitment: "GCP object completion", implied_date: "upto FY27", ref: "676", status_word: "ongoing"}
  - {commitment: "Further Lucknow spend funded from GCP and/or internal accruals", implied_date: "ongoing", ref: "500-501", status_word: "undertaken"}
  - {commitment: "Lucknow Rs 3.00 Cr refundable deposit + 10% net-revenue share, 30-yr lease/15-yr lock-in", implied_date: "from 28-May-2026", ref: "481-484", status_word: "board-approved"}
gate_a3: pass
blank_checks: []
```
