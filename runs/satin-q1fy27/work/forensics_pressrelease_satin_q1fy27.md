# A3 FORENSIC NOTES — SATIN Q1 FY27 — doctype: PRESS RELEASE (presentation)

Source extract: `extract_pressrelease_satin_q1fy27.txt` (6 pages, 304 lines, unit Crores)
Ledger reconciled: 112/112 disclosure units read verbatim at cited lines — 100%.
Prior-quarter extract: NOT supplied — F15 prior-period entity diff and F16 dropped-metric diff could not be run against a prior deck (noted as gap, not silently skipped).

Nature of document: company-authored promotional narrative (press release). No auditor letter, no Board Outcome, no numbered notes, no P&L/BS schedules, no segment tables, no tax/OCI lines. Balance-sheet-schedule checks (F3, F8, F9, F11, F12) and audit/governance checks (F4, F5, F13) are N.A. by doctype and are marked so explicitly below.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|--------------------|
| A3-F1-01 | F1 | §20.1/20.6/20.7/20.8/20.11, 9.1, 9.6 | 161-162, 169, 129 | "On-book Gross Non-Performing Assets (GNPA) stood at 2.18% (₹219 Crores)" (161-162); "Recovery against write-offs ₹8 Crores during Q1FY27" (169) | AMBIGUOUS | NNPA, GROSS write-off amount, cost of funds, cost-to-income, consolidated credit cost all ABSENT despite being standard MFI disclosures. GNPA fell 3.74%→2.18% YoY but only recoveries (₹8 Cr) are shown, not gross write-offs — cannot tell if the improvement is organic or write-off/ARC-driven (thesis tripwire #2: FY26 write-offs ~₹437 Cr). A4 question. |
| A3-F1-02 | F1 | §20.10, 5.1, 9.1-9.2 | 97, 161-164 | "On-book" GNPA ₹219 Cr; "on-book portfolio" 2.51% (163-164); standalone AUM "13,312" (97) | AMBIGUOUS | Repeated "on-book" qualifier + implied on-book book ~₹10,040 Cr (219/2.18%; 252/2.51%) vs standalone AUM ₹13,312 Cr ⇒ ~₹3,270 Cr (~25% of AUM) sits OFF-BOOK (DA/securitised/assigned), unquantified. Bears on ROA quality and thesis tripwire #8 (Q4FY26 DA ₹1,256 Cr). A4 question. |
| A3-F2-01 | F2 | 3.5, 5.5 | 76, 112 | Consol PAT "123 ... 162 ... -24.3%" (76); standalone PAT "120 ... 137 ... -12.2%" (112) | AMBIGUOUS | Consol−standalone PAT gap collapsed QoQ: Q4FY26 ₹25 Cr (18.2% of standalone PAT) → Q1FY27 ₹3 Cr (2.5%), a ~15.7pp swing (>5pp F2 threshold). Subsidiary/consolidation contribution to group PAT fell sharply QoQ; direction and cause not narrated. A4 question. |
| A3-F2-02 | F2 | 10.4, 11.5, 3.5, 5.5 | 179, 189, 76, 112 | SHFL "PAT ... ₹1.5 Crores" (179); SFL "PAT ... ₹4.9 Crores" (189) | FORWARD-SIGNAL | Disclosed subsidiary PATs (1.5 + 4.9 = ₹6.4 Cr) EXCEED the ₹3 Cr consol uplift over standalone ⇒ ~₹3.4 Cr of undisclosed drag = STL + SGAL investment losses and/or minority interest. STL (line 12.1) and SGAL (13.7) disclose zero financials. Ongoing build-out burn in the non-lending arms; future funding/dilution signal. |
| A3-F6-01 | F6 | 6.6, 12.2, 6.3, 13.1, 12.3 | 132, 197, 127-128, 212, 198, 200 | "Promoters will infuse ₹100 Crores Equity Share Capital" (132); "commercial go-live targeted for September 2026" (197); "guidance provided for FY27: 3-3.5%" (127-128) | FORWARD-SIGNAL | Six dated/dateable management commitments (see Commitment Register). Promise-vs-delivery tracking rows for Role 5 / FTTCP catalyst timeline. |
| A3-F10-01 | F10 | 6.6 | 132 | "Promoters will infuse ₹100 Crores Equity Share Capital at ~17% premium to minimum issue price as per SEBI Regulations" | FORWARD-SIGNAL | Dilutive capital action pending (matches thesis warrant ~₹100.1 Cr). Paid-up capital, share count, basic-vs-diluted EPS all ABSENT in this doc, so dilution magnitude unquantifiable here — A4 to size against share count. |
| A3-F14-01 | F14 | 3.F/5.F, 9.3, 14.2 | 81, 116, 165, 235 | "created as an extra buffer" (81); "maintained a ₹36 crore management overlay" (165); "increased our management overlay to ₹36 crore" (235) | AMBIGUOUS | Same ₹36 Cr overlay framed three ways — "created" / "maintained" / "increased ... to". Cannot tell if it is a NEW charge booked this quarter (a one-time hit depressing Q1 PAT) or a standing balance. Material to interpreting the −24.3% QoQ PAT. A4 question. |
| A3-F16-01 | F16 | 2.1, 2.2, 3.5, 3.2, 3.4 | 55-56, 76, 68, 73 | "Consolidated PAT of ₹123 Crores ... 172% up YoY" / "20th profitable quarter in a row" (55-56) | AMBIGUOUS | Selective framing: headline foregrounds +172% YoY off a DEPRESSED base (Q1FY26 PAT ₹45 Cr; chairman: industry "emerging from a difficult two-year period", 231), while QoQ declines sit only in the table, unnarrated — PAT −24.3% (76), Disbursement −20.9% (68), PPOP −7.9% (73). QoQ operating softness disclosed but buried. A4 question. |
| A3-F16-02 | F16 | 3.F/5.F, 3.6-3.7, 5.6-5.7, 6.3 | 81, 116, 78-80, 113-115, 126-128 | "*ROA and ROE exclude management overlay of ₹36 Crores created as an extra buffer" (81, 116) | AMBIGUOUS | Non-GAAP presentation choice. Reported PAT ₹123 Cr is struck AFTER the overlay (credit cost 3.06% incl. overlay vs 1.97% ex, 126-128), but ROA/ROE ADD IT BACK ⇒ the presented consol ROA 4.0% / ROE 20.4% are the flattered figures. Direction: excluding the overlay INFLATES returns (est. consol ROE incl. overlay ~17% vs 20.4% reported; ~+300bps). A4 to request GAAP ROA/ROE incl. overlay against thesis ROE gate (green ≥15%). |

---

## CHECKLIST SCORECARD (all 17; one status each — GATE A3)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | FINDING | 11 standard MFI disclosures absent (§20): NNPA, gross write-offs, PAR 30/60/90, Tier I/II, absolute net worth, cost of funds, cost-to-income, segment AUM split, off-book AUM, consolidated credit cost, dividend — see A3-F1-01/02. |
| F2 STANDALONE vs CONSOL | FINDING | Consol−standalone PAT gap 18.2%→2.5% of standalone QoQ (>5pp); disclosed sub PATs (6.4) exceed 3 Cr uplift — A3-F2-01/02. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost-line decomposition in a press release; cannot compare Cost of Materials / Employee Benefits / Depreciation. (STL discloses no financials — captured under F1/F2.) |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor "Other Matters" paragraph in a press release. |
| F5 GOING CONCERN / EoM | N.A. | No auditor Emphasis-of-Matter / going-concern paragraph in a press release. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Six dated/dateable commitments (will infuse / targeted for Sept 2026 / underway / in progress / FY27 guidance / launched) — Commitment Register + A3-F6-01. |
| F7 HEDGE PHRASE MINING | PASS | Only the boilerplate forward-looking-statements disclaimer (272-282: "not guarantees of future performance ... risks and uncertainties"). No note-level hedge newly added on revenue lumpiness or customer concentration; no prior deck to diff. |
| F8 TAX FORENSICS | N.A. | No tax line, ETR, or deferred-tax disclosure in a press release. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 SHARE COUNT / DILUTION | FINDING | ₹100 Cr promoter equity infusion pending (line 132); paid-up/share count/EPS absent so magnitude unquantifiable — A3-F10-01. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No Paid-up / Other-Equity breakdown; absolute net worth absent (F1); only BVPS ₹270 consol (142) and D/E 3.15x (148) — no reconcilable third-party figure to tie out. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities tables; product-wise AUM split absent (§20.9, captured under F1). |
| F13 BOARD OUTCOME | N.A. | No Board's Report / AGM notice / record date / director-appointment terms in a press release. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | ₹36 Cr overlay framed "created" vs "maintained" vs "increased ... to" across lines 81/165/235 — A3-F14-01. |
| F15 ENTITY LIST DIFFS | N.A. | No prior-quarter extract supplied to diff the consolidation list; four subs named (SHFL, SFL, STL, SGAL) — SGAL newly incorporated Aug 2025 (265) but no prior quarter to confirm a change. |
| F16 PRESENTATION-SPECIFIC (dropped/reframed) | FINDING | Selective YoY-vs-QoQ framing off a depressed base (A3-F16-01) + non-GAAP ROA/ROE excluding overlay (A3-F16-02). |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a press release, not a concall transcript; no transcript to cross-reference. Monitoring-checklist silence folded into F1 (see "Silence vs Monitoring Checklist" below). |

GATE A3: PASS — all 17 marked, no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (line) | status word |
|-----------|-------------|-----------|-------------|
| Promoters to infuse ₹100 Cr equity share capital at ~17% premium (SEBI process) | near-term FY27 | 132 | will infuse (announced / pending) |
| STL Core Banking Solution commercial go-live | September 2026 | 196-197 | targeted (dev completed, customer UAT entered) |
| STL LMS/LOS portfolio expansion for NBFCs | undated | 198 | underway |
| QTrino Labs FIPS certification | undated | 200 | in progress |
| FY27 credit cost 3.0-3.5% (guidance) | FY27 full year | 127-128 | on track (Q1 at 3.06% incl. overlay) |
| SGAL Category II AIF Scheme 1, target corpus ₹200 Cr; LP onboarding | undated | 212, 225 | launched / onboarding (underway) |
| SGAL-SBI co-invest MoU | signed Q1FY27 | 218 | signed (MoU, non-binding) |
| Kerala market entry (South India build-out) | June 2026 | 134 | completed/initiated |

---

## SILENCE vs MONITORING CHECKLIST (weigh, not evidence — folded into F1; noted for A4)

Notion tripwires NOT addressed in this press release: gross write-offs / ARC-DA quality of the GNPA fall (#2 — only ₹8 Cr recovery shown, line 169); Direct Assignment volume and its P&L contribution (#8 — off-book ~₹3,270 Cr implied but unquantified); promoter personal guarantees trajectory (#7); Stage 2 assets % (#6 — only Stage 3 coverage 84.66% given, line 167); SFL GNPA level (#5 — SFL AUM +133.67% and PAT ₹4.9 Cr given, asset quality not, lines 184-189); INR-USD hedge FV swings (#9 — 13% overseas borrowing, line 149-150, no hedge/FV note). These are silences to carry into A4/A5, consistent with A3-F1-01/02.

## CROSS-CHECKS RUN (internal consistency — no finding where consistent)
- PCR: provisions 252 / GNPA 219 = 115.07% ✓ (matches line 168).
- On-book book size: 219/2.18% ≈ 10,046 Cr; 252/2.51% ≈ 10,040 Cr — mutually consistent.
- States & UTs: table 32 (line 86) = About "27 states, 5 union territories" (255-256) ✓.
- Borrowing mix 70+13+11+6 = 100% ✓ (149-150).
- Implied NNPA (not disclosed): 219 × (1−0.8466) ≈ ₹33.6 Cr, ~0.33% — derivable, omitted (feeds A3-F1-01).

```yaml
stage: A3-forensics
company: "SATIN"
quarter: "Q1FY27"
doctype: "press release (presentation)"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/satin-q1fy27/work/forensics_pressrelease_satin_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-F1-01", check: "F1", line: "161-162,169,129", classification: "AMBIGUOUS", implication: "NNPA/gross write-offs/cost of funds/cost-to-income/consol credit cost absent; GNPA fall unverifiable as organic vs write-off/ARC driven"}
  - {id: "A3-F1-02", check: "F1", line: "97,161-164", classification: "AMBIGUOUS", implication: "~Rs 3,270 Cr (~25% of AUM) off-book/securitised implied but unquantified; ROA quality / DA tripwire"}
  - {id: "A3-F2-01", check: "F2", line: "76,112", classification: "AMBIGUOUS", implication: "consol-standalone PAT gap 18.2%->2.5% of standalone QoQ; subsidiary contribution to group PAT collapsed, uncaused"}
  - {id: "A3-F2-02", check: "F2", line: "179,189,76,112", classification: "FORWARD-SIGNAL", implication: "sub PATs 6.4 Cr exceed 3 Cr consol uplift => ~3.4 Cr undisclosed STL/SGAL burn + minority; future funding/dilution"}
  - {id: "A3-F6-01", check: "F6", line: "132,197,127-128,212,198,200", classification: "FORWARD-SIGNAL", implication: "six dated management commitments for Role 5 promise-vs-delivery / FTTCP catalyst timeline"}
  - {id: "A3-F10-01", check: "F10", line: "132", classification: "FORWARD-SIGNAL", implication: "Rs 100 Cr promoter equity infusion pending (warrant); dilution magnitude unquantifiable, share count absent"}
  - {id: "A3-F14-01", check: "F14", line: "81,165,235", classification: "AMBIGUOUS", implication: "Rs 36 Cr overlay 'created' vs 'maintained' vs 'increased to'; new charge vs standing balance ambiguous, drives QoQ PAT read"}
  - {id: "A3-F16-01", check: "F16", line: "55-56,76,68,73", classification: "AMBIGUOUS", implication: "+172% YoY headline off depressed base masks QoQ declines PAT -24.3%, disb -20.9%, PPOP -7.9%"}
  - {id: "A3-F16-02", check: "F16", line: "81,116,126-128", classification: "AMBIGUOUS", implication: "ROA/ROE exclude Rs 36 Cr overlay = non-GAAP; inflates returns ~300bps (est consol ROE ~17% incl overlay vs 20.4%)"}
forward_signals: ["A3-F2-02", "A3-F6-01", "A3-F10-01"]
ambiguous: ["A3-F1-01", "A3-F1-02", "A3-F2-01", "A3-F14-01", "A3-F16-01", "A3-F16-02"]
commitments:
  - {commitment: "Promoters to infuse Rs 100 Cr equity at ~17% premium", implied_date: "near-term FY27", ref: "line 132", status_word: "will infuse"}
  - {commitment: "STL Core Banking commercial go-live", implied_date: "Sept 2026", ref: "line 196-197", status_word: "targeted"}
  - {commitment: "STL LMS/LOS expansion for NBFCs", implied_date: "undated", ref: "line 198", status_word: "underway"}
  - {commitment: "QTrino Labs FIPS certification", implied_date: "undated", ref: "line 200", status_word: "in progress"}
  - {commitment: "FY27 credit cost 3.0-3.5% guidance", implied_date: "FY27", ref: "line 127-128", status_word: "on-track"}
  - {commitment: "SGAL Cat II AIF Scheme 1 corpus Rs 200 Cr; LP onboarding", implied_date: "undated", ref: "line 212,225", status_word: "launched"}
  - {commitment: "SGAL-SBI co-invest MoU", implied_date: "Q1FY27", ref: "line 218", status_word: "signed"}
  - {commitment: "Kerala market entry / South India build-out", implied_date: "June 2026", ref: "line 134", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
