# FORENSIC NOTES — KERNEX Microsystems (India) Ltd | Q1 FY27 | Doctype: RESULTS
Agent A3 (Forensic Notes) | Model: claude-opus-4-8 | Unit: Rs Lakhs (x0.01 = Cr)
Source extract: extract_results_kernex_q1fy27.txt (641 lines, 12 pp) | Ledger: ledger_results_kernex_q1fy27.md
Ledger reconciliation: 100% — every enumerated row read at its cited line before judging.
Doctype applicability: F1-F15 apply; F16 (presentation) and F17 (concall) = N.A.

Note on directionality: this filing is read against a Decision Status = AVOID watch-list.
Conservative bias applied; ambiguous items are surfaced as A4 questions, not resolved here.

---

## FINDINGS TABLE

| id | F# | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|----|----------------|------|----------------------|----------------|---------------------|
| A3-01 | F1 | Sec3 r16 / Sec6 r16 (ZERO_STANDING) | L203, L481 | "VI. Exceptional Items ... - / - / - / -" | FORWARD-SIGNAL | Exceptional Items line stands at zero all 4 periods while Avant-Garde (accum. losses > investment per thesis) is an unbooked impairment candidate. This is exactly where a future impairment lands; its persistent blankness is a deferred charge, not an absence of one. |
| A3-02 | F2 | Sec3 r23 vs Sec6 r23 | L213 vs L491 | consol PAT 10,984.57 vs standalone 10,957.16 | AMBIGUOUS | Consol-over-standalone PAT premium collapsed from 9.45% of standalone PAT (FY26) to 0.25% (Q1FY27), a >5pp narrowing. The entire Rs27.41L premium is ~the Rs27.56L Avant-Garde profit — a single entity reviewed by NO auditor. |
| A3-03 | F2 | Sec3 r2 / r10 | L185, L195 | rev "50,358.23" vs PY "5,592.99"; finance "1,322.77" vs "255.38" | AMBIGUOUS | Revenue Rs503.58 Cr = 9.0x YoY; ~14% of the Rs3,641 Cr order book billed in one quarter (lumpiness / percentage-completion timing). Finance cost Rs13.23 Cr = 5.2x YoY signals a large step-up in borrowings funding the WC build. |
| A3-04 | F3 | Sec3 r9/r11 vs Sec6 r9/r11 | L194 vs L472; L196 vs L474 | employee "1,393.29"/"1,393.29"; deprec "194.41"/"194.41" | CONFIRMATORY-NEGATIVE | Employee-benefit and depreciation lines are byte-identical standalone vs consolidated. The subsidiaries/JVs (TCAS, KERNEX-VRRC, VRRC-KERNEX-CE-RVR, BHEPL) carry zero workforce and zero depreciable assets = non-operating shells / pass-through vehicles. Only Avant-Garde adds real cost. |
| A3-05 | F4 | Sec5 r10 (UNREVIEWED_UNAUDITED) | L413-416 | "have not been reviewed by us and their auditors ... net profit ... Rs. 27.56 Lakhs" | FORWARD-SIGNAL | Avant-Garde figures reviewed by NO auditor (weaker than management-furnished). Its unreviewed contribution jumped from ~Rs4.68L (Q1FY26 consol-SA gap) to Rs27.56L (~6x), and it flipped a loss-making US sub to a profit — unverified, propping the consolidation. |
| A3-06 | F5 | Sec4 r4a / Sec5 r5 | L263-264, L357-363 | "ECL ... Rs334.59 lakhs ... (Previous Year: Rs 309.59 lakhs)" | FORWARD-SIGNAL | ECL provision rose Rs309.59L -> Rs334.59L (+Rs25L) on a frozen Rs422.73L receivable outstanding >3 years, while management asserts "no further provision ... at this stage." Slow-motion write-off; full provisioning of the residual Rs88L (and the Rs265.03L BG under arbitration) is the trajectory. |
| A3-07 | F6 | Sec4 r7 (Note 7) | L272-273 | "outstanding order book is Rs 3641 Crores (Including GST) ... completed to the extent of 45%" | FORWARD-SIGNAL | Order book Rs3,641 Cr is BELOW the Red threshold (Rs4,500 Cr) and ~44% under thesis (~Rs6,500 Cr). Definition is gross of GST (inflates). CLW 45% executed => ~55% future runway but off a shrunken book. Order-book breach is the headline watch-list hit. |
| A3-08 | F6 | Sec9 r6 (ENTITY_CHANGE) | L339-341 | "The Joint venture has not commenced its operations as at 30.06.2026" | FORWARD-SIGNAL | KERNEX-BHEPL JV (51%, formed 07.03.2026) is a dated commissioning commitment: agreement executed, operations pending. Future capex/funding call and a new business line (likely Moving Block). Zero revenue today; watch first-revenue quarter. |
| A3-09 | F6 | Sec4 r8 (Note 8) | L274-275 | "recognised a provision of Rs30.05 Crore towards warranty obligations on KAVACH and signalling systems" | FORWARD-SIGNAL | First large warranty provision on delivered KAVACH/signalling. As the installed base scales, warranty is a recurring drag; Rs30.05 Cr this quarter is the opening data point on field-performance liability. Sits inside "Other Expenses" (masked). |
| A3-10 | F6 | Sec1 r3/r4 (agenda iii/iv) | L59-62 | "re-appointment ... Whole Time Director for further period of three years w.e.f. 2nd September 2026" | NEUTRAL-FACT | Dated governance commitment: two Manthena-family WTDs re-appointed 02.09.2026 through 01.09.2029, i.e. across the commissioning window. Board-approved; term dates logged for the promise tracker. |
| A3-11 | F7 | Sec4 r4 (Note 4) | L261-262, L527 | "these assets are good and fully recoverable ... no further provision is considered necessary at this stage" | AMBIGUOUS | "at this stage" is a temporal hedge newly framing the >3-year receivables and Rs265.03L arbitrated BG as provision-deferred, not provision-free. Read with rising ECL (A3-06), it pre-signals further provisioning ahead. |
| A3-12 | F8 | Sec3 r21 (Note) | L210 | "(c) Deferred tax credit ... (859.17)" | FORWARD-SIGNAL | Deferred-tax CREDIT of Rs859.17L (~Rs8.59 Cr) shields Q1FY27 PAT by ~580 bps: reported ETR 25.85% vs ex-credit current-tax ETR 31.65%. Directly trips the Notion "deferred-tax-credit propping PAT again" watch. Shield is finite; ETR step-up risk once DTA/carryforward exhausts. |
| A3-13 | F13 | Sec1 r5 (agenda v) | L63-64 | "Approved the Directors report along with Management Discussion and Analysis" | FORWARD-SIGNAL | Directors' Report + MD&A + CG Report approved => FY26 Annual Report drops within weeks. Schedule Role 6 AR Deep Dive: the FY26 statutory-audit OPINION (Green if first-time unqualified / Red if qualified again or auditor exit) is the load-bearing watch-list event. |
| A3-14 | F14 | Sec1 r3 (DIN_MISMATCH) | L59 vs L88/L91 | board letter "DIN:07992925" vs Annexure "DIN: 07993925" | NEUTRAL-FACT | Same director (Badari Narayana Raju Manthena), same document, transposed DIN digit on a re-appointment resolution. Immaterial alone; a governance-hygiene data point on a board resolution. |
| A3-15 | F14 | Sec5 r5 vs Sec8 r4 / Sec4 r4a | L363 vs L592 / L264 | consol EoM "ECL ... (PY Rs.211.67 Lakhs)" vs standalone EoM/Note4 "(PY Rs.309.59 lakhs)" | AMBIGUOUS | The consolidated auditor's own EoM cites a PY ECL (Rs211.67L) that contradicts the standalone EoM AND both results' Note 4 (Rs309.59L) for the identical receivable. Which PY figure is correct changes the provision-build slope — an audit-quality inconsistency to reconcile at the AR. |
| A3-16 | F14 | Sec5 r5 / Sec8 r4 | L358, L362, L591 | EoM "attention to the Note 3" (recoverability actually in Note 4); PY receivable "Rs 422.10 Lakhs" vs Note 4 "Rs 422.73 lakhs" | NEUTRAL-FACT | Both auditor EoMs cross-reference "Note 3" while the recoverability disclosure is Note 4, and cite PY receivable Rs422.10L vs Note 4's Rs422.73L. Drafting slippage; cumulatively reinforces low report-assembly control. |
| A3-17 | F15 | Sec9 r6 (ENTITY_CHANGE) | L337, L339-341 | "Joint Operation - KERNEX-BHEPL JV" ... "formed a joint venture with ... (BHEPL) on 07.03.2026" | FORWARD-SIGNAL | New entity in consolidation scope vs prior quarters: KERNEX-BHEPL JV (Bharat Heavy Engineering Pvt Ltd, 51%). Consolidation-scope expansion with zero operations — a forward business line and a governance/funding item to track. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| F# | Check | Status | One-line basis |
|----|-------|--------|----------------|
| F1 | Zero-value standing lines | FINDING | 3 ZERO_STANDING rows read (L203, L231, L481). Exceptional Items zero all periods while an impairment candidate exists (A3-01); OCI-to-NCI zero is a de-minimis mechanical zero (NCI ~Rs0.03L), not a finding. |
| F2 | Standalone vs consolidated | FINDING | Consol-SA PAT gap swung 9.45% (FY26) -> 0.25% (Q1FY27), >5pp; premium ~= unreviewed Avant-Garde; revenue 9x / finance cost 5.2x YoY (A3-02, A3-03). |
| F3 | Shell-entity detection | FINDING | Identical employee benefits (1,393.29) and depreciation (194.41) consol vs standalone => subsidiaries/JVs are non-operating shells (A3-04). |
| F4 | Unaudited contribution ratio | FINDING | Avant-Garde reviewed by no auditor; contribution Rs27.56L, ~6x YoY jump though ~0.25% of PAT — the YoY jump and no-auditor status drive the finding (A3-05). |
| F5 | Going concern / EoM scope | FINDING | No prior-quarter extract for full verbatim diff; substantive EoM movement is ECL +Rs25L on a frozen receivable plus "at this stage" framing (A3-06). |
| F6 | Forward-commitment mining | FINDING | Order book Rs3,641 Cr/CLW 45% (A3-07); BHEPL JV pre-operational (A3-08); Rs30.05 Cr warranty provision (A3-09); WTD re-appointments dated (A3-10). |
| F7 | Hedge-phrase mining | FINDING | "no further provision ... at this stage" and "may not necessarily reflect future uncertainties ... may vary" hedge the receivables/BG (A3-11). |
| F8 | Tax forensics | FINDING | Rs859.17L deferred-tax credit shields ~580 bps; reported ETR 25.85% vs ex-credit 31.65%; trips Notion DTC watch (A3-12). Earlier-year tax adj = Nil this quarter (was Rs48.42L in Q4FY26). |
| F9 | OCI forensics | PASS | Q1FY27 OCI ~nil (only Rs(0.25)L reclass item); actuarial remeasurement booked at year-end (Q4 Rs(86.82)L) per normal practice; no swing exceeding prior year, no assumption-change signal. |
| F10 | Share count / dilution | PASS | Paid-up +0.12L (Q4->Q1) = 1,200 ESOP shares, traces cleanly to Note 5 (L266/L531); basic-diluted EPS spread nil this quarter, not widening (was 0.04 in FY26). No new dilutive instrument. |
| F11 | Reserves / net worth tie-out | PASS | Other Equity is annual-only (BLANK_QUARTERLY); FY26 consol NW Rs248.11 Cr, standalone Rs256.31 Cr; standalone > consol by Rs8.19 Cr consistent with subsidiary losses/eliminations; no third-party NW figure in filing to reconcile against. |
| F12 | Segment forensics | N.A. | Single reportable segment per Note 3 (L257-258/L522-523); no segment assets/liabilities disclosed in the interim filing — nothing to trend. |
| F13 | Board outcome beyond results | FINDING | Directors' Report + MD&A approved => FY26 AR imminent, schedule Role 6 AR Deep Dive; two WTD term dates logged (A3-13, and DIN issue A3-14). |
| F14 | Note-drafting inconsistencies | FINDING | DIN transposition (A3-14); consol EoM PY-ECL contradicts standalone EoM + Note 4 (A3-15); wrong note cross-ref + PY receivable mismatch (A3-16); OCI "A."/"A." label reuse (L216/L220); "Mr. M Sitarama Raju" (L133) vs "Sitarama Raju Manthena" (L135); "Avant-Garde"/"Avant Garde" hyphen variance. |
| F15 | Entity-list diffs | FINDING | KERNEX-BHEPL JV added to consolidation scope (formed 07.03.2026, 51%, pre-operational) (A3-17). |
| F16 | Presentation-specific | N.A. | Doctype = results; no presentation deck in scope. |
| F17 | Concall silence audit | N.A. | Doctype = results; no transcript in scope. (Notion watch items reconciled against the filing in the narrative below for A4 hand-off.) |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| CLW major order — supplies completed to 45% | 45% as at 13-08-2026; ~55% remaining | Note 7 (L272-273) / Note 6 SA (L533-534) | underway |
| KERNEX-BHEPL JV to commence operations | after 30.06.2026 (formed 07.03.2026) | Auditor Para 4 footnote (L339-341) | initiated (agreement executed) |
| Warranty obligations on KAVACH/signalling — Rs30.05 Cr provisioned | recognised this quarter (ongoing exposure) | Note 8 (L274-275) / Note 7 SA (L535-536) | has been recognised (opening) |
| Re-appointment WTD Badari Narayana Raju Manthena, 3 yrs | w.e.f. 02.09.2026 to 01.09.2029 | Agenda (iii) L59-60 / Annexure A (L91-98) | board approved |
| Re-appointment WTD Sitarama Raju Manthena, 3 yrs | w.e.f. 02.09.2026 to 01.09.2029 | Agenda (iv) L61-62 / Annexure A (L135-142) | board approved |
| Directors' Report + MD&A + CG Report approved (FY26 AR to follow) | AR filing within weeks (Aug-Sep 2026) | Agenda (v) L63-64 | approved (AR pending) |

---

## NOTION WATCH-LIST RECONCILED AGAINST THE FILING (context for A4; F17 silence audit is N.A. on a results filing)

- Order book: Rs3,641 Cr incl GST (L272) — BELOW Red Rs4,500 Cr and ~44% under thesis Rs6,500 Cr. RED. Gross-of-GST definition inflates the headline. -> A3-07.
- Quarterly revenue: Rs503.58 Cr consol (L185) — EXCEEDS the >Rs500 Cr early-warning; 9x YoY, lumpy vs a shrinking book. -> A3-03.
- EBITDA margin: ~32.3% operating (PBT 14,813.71 + fin 1,322.77 + dep 194.41 - other inc 48.52, /rev 50,358.23) — top of the 28-32% Green band DESPITE a Rs30.05 Cr warranty hit; margin at/above peak. FTTCP "STAGNANT at peak" confirmed.
- Deferred-tax shield: Rs8.59 Cr credit again propping PAT this quarter. RED-adjacent. -> A3-12.
- FY26 AR auditor opinion: not in this filing but signalled imminent by agenda (v). -> A3-13, the single most important forward event.
- Subsidiary/JV impairment: Exceptional line blank (A3-01); Avant-Garde unreviewed and profit-flipped (A3-05); JVs are shells (A3-04). Impairment remains unbooked.
- Borrowings: no balance sheet, but finance cost 5.2x YoY (A3-03) implies borrowings stepped up materially — watch vs Rs250 Cr Red.
- CFO / debtor days / promoter pledge / demat-T2T: NOT DISCLOSED in this filing (no cash-flow or shareholding statement in interim results). Not computable here; carry forward for the AR and shareholding-pattern filings.

---

## A4 HAND-OFF — MANAGEMENT QUESTIONS (FORWARD-SIGNAL + AMBIGUOUS findings)

FORWARD-SIGNAL: A3-01, A3-05, A3-06, A3-07, A3-08, A3-09, A3-12, A3-13, A3-17
AMBIGUOUS: A3-02, A3-03, A3-11, A3-15

Priority questions for A4 to draft:
1. (A3-07) Order book Rs3,641 Cr incl GST vs prior thesis ~Rs6,500 Cr — what fell out, and what is the ex-GST net book?
2. (A3-05/A3-01) Avant-Garde flipped to a Rs27.56 Cr... Rs27.56 lakh net profit unreviewed by any auditor — basis, and why no impairment despite accumulated losses > investment?
3. (A3-12) Deferred-tax credit Rs8.59 Cr again — what reverses it and what is the normalised ETR trajectory?
4. (A3-06/A3-11) Rising ECL on frozen >3-year receivables plus "at this stage" hedge — timeline to full provision / arbitration outcome on the Rs265.03L BG?
5. (A3-09) Rs30.05 Cr warranty provision — methodology and expected run-rate as the KAVACH installed base scales.
6. (A3-08/A3-17) KERNEX-BHEPL JV — scope, capex, funding, and first-revenue timeline.
7. (A3-03) Revenue Rs503.58 Cr in one quarter vs a Rs3,641 Cr book and 5.2x finance-cost jump — recognition basis and borrowing quantum.
8. (A3-15) Reconcile the consolidated auditor EoM PY-ECL figure (Rs211.67L) against Note 4 / standalone EoM (Rs309.59L).

```yaml
stage: A3-forensics
company: "KERNEX"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/kernex-q1fy27/work/forensics_kernex_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L203/L481", classification: "FORWARD-SIGNAL", implication: "Exceptional Items zero all periods = unbooked Avant-Garde impairment lands here"}
  - {id: "A3-02", check: "F2", line: "L213/L491", classification: "AMBIGUOUS", implication: "Consol-SA PAT gap 9.45%->0.25% (>5pp); premium ~= unreviewed Avant-Garde"}
  - {id: "A3-03", check: "F2", line: "L185/L195", classification: "AMBIGUOUS", implication: "Revenue 9x YoY, ~14% of book billed in a quarter; finance cost 5.2x = borrowing step-up"}
  - {id: "A3-04", check: "F3", line: "L194/L196", classification: "CONFIRMATORY-NEGATIVE", implication: "Identical employee/deprec = subsidiaries and JVs are non-operating shells"}
  - {id: "A3-05", check: "F4", line: "L413-416", classification: "FORWARD-SIGNAL", implication: "Avant-Garde reviewed by no auditor; Rs27.56L profit, ~6x YoY jump, loss-to-profit flip"}
  - {id: "A3-06", check: "F5", line: "L263-264/L357-363", classification: "FORWARD-SIGNAL", implication: "ECL +Rs25L on frozen Rs422.73L receivable = slow-motion write-off"}
  - {id: "A3-07", check: "F6", line: "L272-273", classification: "FORWARD-SIGNAL", implication: "Order book Rs3,641 Cr incl GST below Red Rs4,500 Cr and ~44% under thesis"}
  - {id: "A3-08", check: "F6", line: "L339-341", classification: "FORWARD-SIGNAL", implication: "BHEPL JV pre-operational: future capex/funding, new business line"}
  - {id: "A3-09", check: "F6", line: "L274-275", classification: "FORWARD-SIGNAL", implication: "Rs30.05 Cr KAVACH warranty provision = recurring field-performance drag"}
  - {id: "A3-10", check: "F6", line: "L59-62", classification: "NEUTRAL-FACT", implication: "Two WTD term dates 02.09.2026-01.09.2029 logged for promise tracker"}
  - {id: "A3-11", check: "F7", line: "L261-262/L527", classification: "AMBIGUOUS", implication: "'at this stage' temporal hedge pre-signals further provisioning"}
  - {id: "A3-12", check: "F8", line: "L210", classification: "FORWARD-SIGNAL", implication: "Rs859.17L deferred-tax credit shields ~580bps; ETR 25.85% vs ex-credit 31.65%"}
  - {id: "A3-13", check: "F13", line: "L63-64", classification: "FORWARD-SIGNAL", implication: "Directors Report+MD&A approved => FY26 AR imminent; schedule Role 6 AR Deep Dive"}
  - {id: "A3-14", check: "F14", line: "L59/L91", classification: "NEUTRAL-FACT", implication: "DIN transposition 07992925 vs 07993925 on re-appointment resolution"}
  - {id: "A3-15", check: "F14", line: "L363/L592", classification: "AMBIGUOUS", implication: "Consol EoM PY-ECL Rs211.67L contradicts standalone EoM+Note4 Rs309.59L"}
  - {id: "A3-16", check: "F14", line: "L358/L362", classification: "NEUTRAL-FACT", implication: "EoM cites wrong note (3 vs 4) and PY receivable Rs422.10L vs Note4 Rs422.73L"}
  - {id: "A3-17", check: "F15", line: "L337/L339-341", classification: "FORWARD-SIGNAL", implication: "KERNEX-BHEPL JV added to consolidation scope, pre-operational"}
forward_signals: ["A3-01","A3-05","A3-06","A3-07","A3-08","A3-09","A3-12","A3-13","A3-17"]
ambiguous: ["A3-02","A3-03","A3-11","A3-15"]
commitments:
  - {commitment: "CLW major order supplies completed to 45%", implied_date: "45% at 13-08-2026; ~55% remaining", ref: "Note 7 L272-273", status_word: "underway"}
  - {commitment: "KERNEX-BHEPL JV to commence operations", implied_date: "after 30.06.2026", ref: "Auditor Para 4 L339-341", status_word: "initiated"}
  - {commitment: "KAVACH/signalling warranty provision Rs30.05 Cr", implied_date: "recognised Q1FY27, ongoing", ref: "Note 8 L274-275", status_word: "recognised"}
  - {commitment: "WTD re-appointment Badari Narayana Raju Manthena 3 yrs", implied_date: "02.09.2026-01.09.2029", ref: "Agenda iii L59-60 / Annexure A L91-98", status_word: "approved"}
  - {commitment: "WTD re-appointment Sitarama Raju Manthena 3 yrs", implied_date: "02.09.2026-01.09.2029", ref: "Agenda iv L61-62 / Annexure A L135-142", status_word: "approved"}
  - {commitment: "Directors Report + MD&A approved, FY26 AR to follow", implied_date: "AR within weeks (Aug-Sep 2026)", ref: "Agenda v L63-64", status_word: "approved"}
gate_a3: pass
blank_checks: []
```
