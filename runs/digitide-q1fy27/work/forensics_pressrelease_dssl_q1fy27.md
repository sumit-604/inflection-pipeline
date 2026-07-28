# A3 FORENSIC NOTES — Digitide Solutions Limited (DSSL) — Q1 FY27 — Doctype: results (earnings PRESS RELEASE)

Source extract: `runs/dssl-q1fy27/work/extract_pressrelease_dssl_q1fy27.txt` (311 lines, 4 pages, 100% coverage)
Ledger reconciled: `runs/dssl-q1fy27/work/ledger_pressrelease_dssl_q1fy27.md` — 148/148 enumerated disclosure units read at cited lines = 100%.

DOCTYPE CAVEAT: The document is the earnings press release only. It carries NO financial statements, NO numbered notes, NO auditor report, NO board-outcome letter, NO consolidation entity list. The pure-filing checks (F1, F3, F4, F5, F8, F9, F10, F11, F13, F14, F15) are therefore N.A. with the standing basis "press release carries no statements/notes/auditor report/board letter." The document-content checks (F2 partial, F6, F7, F12 partial, F16, F17) are run in full below. First quarterly run: no prior-quarter extract; in-document Q1FY26 / Q4FY26 comparative columns used for all trend work.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|---------------------|
| FN-01 | F2 | KH-3, FQ-1, B-2 | 84, 248-249 | "Consolidated revenue for Q1 FY27 stood at ₹775 Cr" / "Reported PAT turned posiƟve at ₹2.9 Cr" | AMBIGUOUS | Revenue labelled "Consolidated" but PAT ₹2.9 Cr carries no standalone comparator and no owners-vs-NCI split. S-vs-C gap and attributable-vs-total PAT cannot be computed from this document. A4 must reconcile ₹2.9 Cr against the Reg 33 filing (is ₹2.9 Cr total-comprehensive, PAT-after-NCI, or owners-of-parent?). |
| FN-02 | F6 | I-1, I-2, Q-1, Q-2 | 221-222, 225, 245-246, 254, 256-257 | "12+ acƟve discussions underway" / "we enter Q2 focused on converting high-probability pipeline" / "pursuing disciplined, value-accreƟve M&A" / "retain the ﬂexibility to invest in ... selective inorganic opportunities" | FORWARD-SIGNAL | Management has planted four dateable/near-dateable commitments: (a) AI-Lab engagement model extension across "12+" clients, (b) Q2 FY27 pipeline conversion at "stronger pricing discipline", (c) active M&A intent, (d) capital-deployment framework ("four priorities ... will guide how we allocate capital"). These become the Role 5 promise-vs-delivery baseline and FTTCP catalyst timeline. |
| FN-03 | F7 | I-2, Q-2 | 225, 256-257 | "12+ acƟve discussions underway" / "We continue to retain the ﬂexibility to invest ... and selective inorganic opportunities" | AMBIGUOUS | "Discussions" = pipeline not yet closed; "retain the flexibility" is non-committal cover on capital deployment and M&A. Neither confirms conversion. Direction uncertain -> A4 question on close-rate of the "12+" and on capital-allocation guardrails. |
| FN-04 | F12 | Table 5 (BPM/T&D/Total), Table 6 EBITDA | 116, 125, 134, 158 | BPM "-2.4%" QoQ, T&D "-4.7%" QoQ, Total "-3.1%" QoQ; EBITDA "-12.5%" QoQ | FORWARD-SIGNAL | Every revenue segment declined sequentially (BPM -2.4%, T&D -4.7%, Total -3.1%) while the headline foregrounds YoY. Core BPM (69.4% of revenue) is flat YoY at -0.2% — the entire YoY growth engine is T&D + International. EBITDA fell -12.5% QoQ vs revenue -3.1% QoQ = ~4x operating deleverage. No segment assets/liabilities disclosed (that half of F12 is N.A.), but the revenue-momentum and deleverage signal is live. |
| FN-05 | F16 | Table 6 Reported PAT row | 166-171 | Reported PAT QoQ cell = "Turned Positive" (vs Q4FY26 "-5.0", Q1FY27 "2.9") | CONFIRMATORY-NEGATIVE | SUPPRESSED_METRIC: a text label substitutes for the numeric QoQ, and no absolute ₹ swing (-5.0 -> +2.9 = +7.9 Cr) is stated anywhere in narrative. The reframing masks that PAT is ₹2.9 Cr on ₹775.1 Cr revenue = 0.4% net margin, and PAT is down -69.7% YoY (line 171). "Improved earnings quality" (line 85) framing over a 0.4% margin. |
| FN-06 | F16 | B-3 vs Table 6 EBITDA | 86-88, 158 | Bullet: "EBITDA of ₹76.9 Cr declined QoQ" — omits table's "-12.5%" | CONFIRMATORY-NEGATIVE | SELECTIVE_DISCLOSURE: bullet B-3 states direction only, dropping the -12.5% QoQ magnitude that IS printed in the table (line 158), whereas B-1/B-4/B-5 all state their % explicitly. Asymmetric disclosure — the one deteriorating headline metric is the one shown without its number. Cause given ("minimum wage revisions across states") is a margin-structural driver to test for persistence. |
| FN-07 | F16 | KH-5, Table 6 EBITDA/EBITDA% | 87, 154-165 | "EBITDA of ₹76.9 Cr" / "EBITDA % 9.9%" | NEUTRAL-FACT | NON_GAAP_MEASURE: EBITDA, EBITDA% and Reported PAT% are presented with no reconciliation to Reported PAT and no definition anywhere in the document. Standard for a press release but A4 must anchor EBITDA definition (does it net the "minimum wage" / any one-offs?) against the Reg 33 filing before using the 9.9% margin. |
| FN-08 | F16 | KH-12/13/14, IN-2/3/5/6-8, CQ-3 | 94, 96, 225, 228-232, 242 | "TCV bookings ₹205 Cr" / "26 key logo wins" / "5.7 Mn AI interacƟons" / "NPS by 15%" / "25–30% improvement in code generaƟon" / "12+ acƟve discussions" / "over 300 clients" / "16,000+ hires" | AMBIGUOUS | UNDEFINED_KPI cluster: none of these operating KPIs carries a definition, baseline, or footnote (TCV contract-duration/deal criteria; "key logo" threshold; what counts as one "AI interaction"; NPS baseline and pp-vs-% basis; code-gen baseline; "active discussion"; exact client count; gross-vs-net hires). Unverifiable and non-comparable QoQ. Each is an A4 management question to lock a definition before it enters any trend. |
| FN-09 | F16 | KH-8/11, CQ-2, FQ-4/5/7/8, A-6 | 42-43, 90, 92, 239, 250-251 | "31% of total revenue" (table 30.6%) / "38% of total revenue" (table 38.1%) / "₹775 crores" (table 775.1) / "₹237 Cr" (237.4) / "₹296 Cr" (295.6) | NEUTRAL-FACT | ROUNDING_VARIANCE between narrative/quotes and tables. Individually immaterial; direction is mixed (T&D 30.6->31 rounds up, Intl 38.1->38 rounds down). Logged as a cumulative drafting-discipline data point, not a red flag. |
| FN-10 | F17 | Table 6 EBITDA% row | 160-163 | "EBITDA % ... 11.2% ... 11.0% ... 9.9%" (Q1FY26/Q4FY26/Q1FY27) | FORWARD-SIGNAL | BINDING TRIPWIRE READ: Q1 FY27 EBITDA margin printed at 9.9% — below the 11% floor and one quarter into the two-quarter FLAG-CASH falsifier test. If Q2 FY27 also prints near 9% (<11%), the Q4 FY26 compression is confirmed STRUCTURAL (DaaS/CBaaS annuity pivot diluting unit economics), not a transient AI-hardware blip. Press release is SILENT on all five monitorables (unit economics IRR/ROCE/GM; ~₹90cr PPE/capex gap; receivables ageing; CFO/PAT 0.529x; governance) — expected for a press release, but the CFO quote had the opening to address margin/economics and gave qualitative "quality of revenue over volume" (line 249) instead. Q1 FY27 = first quarter of the silence tracker; concall transcript pending. |

---

## CHECKLIST SCORECARD (all 17 — no blanks)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINES | N.A. | Press release carries no statements/notes; ledger `zero_standing: 0`, no template nil/dash line exists. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | FN-01: PAT ₹2.9 Cr labelling ambiguous (no standalone comparator, no owners-vs-NCI split); A4 to reconcile vs Reg 33. |
| F3 SHELL-ENTITY DETECTION | N.A. | Press release carries no standalone/consolidated cost lines to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Press release carries no auditor report / Other Matters paragraph. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | Press release carries no auditor report; also no prior-quarter EoM to diff. |
| F6 FORWARD-COMMITMENT PHRASE MINING | FINDING | FN-02: "underway" / "will guide" / Q2 pipeline / M&A intent — four dateable commitments (see Commitment Register). |
| F7 HEDGE PHRASE MINING | FINDING | FN-03: "active discussions" (unclosed pipeline) and "retain the flexibility" (non-committal M&A/capital cover). |
| F8 TAX FORENSICS | N.A. | Press release carries no tax line / P&L / ETR. |
| F9 OCI FORENSICS | N.A. | Press release carries no OCI / actuarial disclosure. |
| F10 SHARE COUNT & DILUTION | N.A. | Press release carries no paid-up capital / EPS / instrument disclosure. |
| F11 RESERVES & NET WORTH TIE-OUT | N.A. | Press release carries no balance sheet / other equity. |
| F12 SEGMENT FORENSICS | FINDING | FN-04: all segments down QoQ (BPM -2.4%, T&D -4.7%), EBITDA -12.5% QoQ = ~4x deleverage; segment assets/liabs not disclosed (that half N.A.). |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Press release carries no board-outcome letter / agenda / director term dates. |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | Press release carries no notes/auditor letter; cross-table rounding inconsistencies are adjudicated under F16 (FN-09). |
| F15 ENTITY LIST DIFFS | N.A. | Press release discloses no consolidation entity list; no prior quarter to diff. |
| F16 DROPPED/REFRAMED DISCLOSURES | FINDING | FN-05 (PAT QoQ "Turned Positive" suppressed), FN-06 (EBITDA -12.5% QoQ omitted from bullet), FN-07 (NON_GAAP no recon), FN-08 (UNDEFINED_KPI cluster), FN-09 (rounding variance). |
| F17 SILENCE AUDIT | FINDING | FN-10: EBITDA margin 9.9% triggers/approaches the 11% binding tripwire (Q1 of the 2-quarter test); press release silent on all five monitorables; concall transcript pending. |

Score: 6 FINDING (F2, F6, F7, F12, F16, F17); 11 N.A.; 0 PASS; 0 blank. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (line) | status word |
|-----------|--------------|-----------|-------------|
| Extend the AI Innovation Lab "scalable engagement model" across the client base ("12+ active discussions") | ongoing / near-term | 224-225 | underway |
| Convert "high-probability pipeline with stronger pricing discipline" | Q2 FY27 | 254-255 | initiated |
| Pursue "disciplined, value-accreƟve M&A" / "selective inorganic opportunities" | undated intent | 221-222, 256-257 | initiated |
| "Four priorities" framework to "guide how we allocate capital and measure progress" | undated (new framework this quarter) | 245-246 | initiated |
| Grow Tech & Digital, International and AI-led revenue mix | undated, ongoing | 250-251, 255 | underway |

---

## NOTES FOR A4 (question generation)
FORWARD-SIGNAL and AMBIGUOUS findings flagged for conversion into management questions: FN-01, FN-02, FN-03, FN-04, FN-08, FN-10. Priority: FN-10 (margin tripwire, quarter 1 of 2) and FN-01 (PAT consolidation/attribution reconciliation vs Reg 33 filing).

---

```yaml
stage: A3-forensics
company: "DSSL"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/dssl-q1fy27/work/forensics_pressrelease_dssl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "FN-01", check: "F2", line: "84, 248-249", classification: "AMBIGUOUS", implication: "PAT Rs2.9cr consolidation/attribution ambiguous; A4 reconcile vs Reg 33 (total vs after-NCI vs owners-of-parent)"}
  - {id: "FN-02", check: "F6", line: "221-222, 225, 245-246, 254, 256-257", classification: "FORWARD-SIGNAL", implication: "Four dateable commitments (AI-Lab extension, Q2 pipeline, M&A, capital framework) = Role 5 promise-tracker baseline"}
  - {id: "FN-03", check: "F7", line: "225, 256-257", classification: "AMBIGUOUS", implication: "Pipeline unclosed ('discussions') and non-committal M&A/capital cover ('retain the flexibility')"}
  - {id: "FN-04", check: "F12", line: "116, 125, 134, 158", classification: "FORWARD-SIGNAL", implication: "All segments down QoQ; BPM flat YoY; EBITDA -12.5% QoQ vs revenue -3.1% = ~4x operating deleverage"}
  - {id: "FN-05", check: "F16", line: "166-171", classification: "CONFIRMATORY-NEGATIVE", implication: "PAT QoQ suppressed as 'Turned Positive'; 0.4% net margin, -69.7% YoY masked"}
  - {id: "FN-06", check: "F16", line: "86-88, 158", classification: "CONFIRMATORY-NEGATIVE", implication: "EBITDA -12.5% QoQ magnitude omitted from bullet while other bullets state their %; asymmetric disclosure"}
  - {id: "FN-07", check: "F16", line: "154-165", classification: "NEUTRAL-FACT", implication: "EBITDA/EBITDA%/PAT% non-GAAP, no reconciliation/definition; anchor vs Reg 33 before use"}
  - {id: "FN-08", check: "F16", line: "94, 96, 225, 228-232, 242", classification: "AMBIGUOUS", implication: "TCV/logos/AI-interactions/NPS/ARISE/300-clients/16000-hires all undefined; not comparable QoQ; lock definitions"}
  - {id: "FN-09", check: "F16", line: "42-43, 90, 92, 239, 250-251", classification: "NEUTRAL-FACT", implication: "Cross-table rounding variance; cumulative drafting-discipline data point only"}
  - {id: "FN-10", check: "F17", line: "160-163", classification: "FORWARD-SIGNAL", implication: "EBITDA margin 9.9% <11% floor = quarter 1 of 2-quarter FLAG-CASH structural-compression falsifier; silent on all five monitorables"}
forward_signals: ["FN-02", "FN-04", "FN-10"]
ambiguous: ["FN-01", "FN-03", "FN-08"]
commitments:
  - {commitment: "Extend AI Innovation Lab engagement model across client base (12+ discussions)", implied_date: "near-term", ref: "224-225", status_word: "underway"}
  - {commitment: "Convert high-probability pipeline with stronger pricing discipline", implied_date: "Q2 FY27", ref: "254-255", status_word: "initiated"}
  - {commitment: "Pursue disciplined value-accretive M&A / selective inorganic opportunities", implied_date: "undated", ref: "221-222, 256-257", status_word: "initiated"}
  - {commitment: "Four-priorities framework to guide capital allocation", implied_date: "undated", ref: "245-246", status_word: "initiated"}
  - {commitment: "Grow Tech & Digital, International and AI-led revenue mix", implied_date: "ongoing", ref: "250-251, 255", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
