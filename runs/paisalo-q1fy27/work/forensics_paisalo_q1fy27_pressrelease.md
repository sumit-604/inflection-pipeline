# A3 FORENSIC NOTES — Paisalo Digital, Q1FY27 — doctype: results (Reg-30 PRESS RELEASE subtype)

Source extract: `runs/paisalo-q1fy27/work/extract_results_paisalo_q1fy27_pressrelease.txt`
Ledger contract: `runs/paisalo-q1fy27/work/ledger_results_paisalo_q1fy27_pressrelease.md`
Ledger reconciliation: 100% — every A2 row (sections 1-10 + ABSENT-DISCLOSURES) read at its cited line before judging.
Unit convention: Rs Mn (÷10 = Rs Cr). PAT 613 Mn = Rs 61.3 Cr.

Doctype note carried from A2: this is a Regulation 30 press release, NOT the
Regulation 33 results statement. It has no P&L / balance sheet / cash flow, no
numbered notes, no auditor report, no entity list, and no board-outcome letter.
Accordingly the auditor-, notes-, and statement-dependent checks (F3, F4, F5,
F8, F9, F10, F11, F13, F15) return N.A. on this artifact — their subject matter
is physically absent, which is itself carried into the ABSENT-DISCLOSURE
reconciliation below rather than scored as PASS. F16 is used to house the two
absent hard-gate metrics because the omission of a live-tripwire disclosure is
the operative forensic question the task assigned; F17 is N.A. (no transcript —
the Aug-6-2026 concall has not yet occurred).

---

## FINDINGS TABLE

| id | check | ledger row | line | verbatim quote | classification | forward implication |
|----|-------|-----------|------|----------------|----------------|---------------------|
| FN1 | F1 | 4.3 (ZERO_STANDING) | 122 | "Total Income (Rs Mn)  2,603 … 2,609  -" | AMBIGUOUS | QoQ cell dashed though both values present (2,603 vs 2,609 = -0.2% QoQ). The dash sits inside a wider sequential-softness cluster the release frames away: PAT -15% QoQ (722→613, line 123), NIM -26 Bps QoQ (line 124), RoA 3.8%→3.6% QoQ (line 202), all dressed as "stable"/"healthy" (lines 157, 160). Sequential margin/profit compression while AUM still +10% QoQ. → A4 question on QoQ drivers. |
| FN2 | F2 / ABSENT #2 | KPI header row | 119 | "Particulars  Q1FY27  Q1FY26  YoY (%)  Q4FY26  QoQ (%)" | AMBIGUOUS | Reporting basis (standalone vs consolidated) is stated nowhere in the document. Cannot tell whether PAT Rs613 Mn and Net Worth Rs18,298 Mn are standalone or consolidated. Highest-value undisclosed item; blocks any S-vs-C decomposition. → A4 must ask basis. |
| FN3 | F6 | 7.2 (MD quote) | 248-249 | "we continue to scale our portfolio through existing and new lending verticals while deepening strategic partnerships" | FORWARD-SIGNAL | Undated commitment to new lending verticals + partnership deepening = the SBI MSME co-lending expansion track (Notion monitorable: margin-dilutive per UGRO analogue; co-lending fees <5% tripwire). → A4: which verticals, co-lending AUM & spread economics. |
| FN4 | F12 | 4.1 / 4.2 | 120-121 | "Disbursement (Rs Mn)  17,309 … +128%" vs "AUM … 67,074 … +28%" | AMBIGUOUS | Disbursement grew 4.6x faster YoY than AUM (+128% vs +28%); single-quarter disbursement is ~26% of AUM. No own-book vs co-lending / assignment split, no segment (SME/MSME/micro) breakout disclosed. Divergence implies short-tenor churn OR off-book origination not accreting to on-book AUM (margin-dilutive). → A4: disbursement mix, off-book share. |
| FN5 | F14 | 4.5 / 5.16 / 6.8 / 6.9 | 124, 165, 219 | "6.6%  6.5%  +4 Bps  6.8%  (26 Bps)" | NEUTRAL-FACT | Bps/growth deltas do not tie to displayed rounded values: NIM YoY stated +4 Bps vs displayed +10; NIM QoQ stated (26 Bps) vs displayed -20; CoB "64 bps YoY" (line 76/151) vs chart 10.7%→10.1% = 60 bps; Net Worth "grew by 15% YoY" (line 165) vs 15,746→18,298 = +16.2% (line 219). Deltas computed off unrounded figures; individually immaterial, cumulatively a data-quality flag. Verify exact figures at the Reg-33 filing. |
| FN6 | F16 / ABSENT #6 | ABSENT-DISCLOSURE #6 | 155-160 | Profitability bullets list "Total income … Net interest income … NIM … headcount … PAT … RoA at 3.6% and RoE at 13.4%" — no Cost-to-Income | FORWARD-SIGNAL | Cost-to-Income is the single cleanest pre-entry hard-gate metric (thesis needs ≤35% mgmt basis) and the live RED tripwire (Q4FY26 39.7%, FY26 36.4%). The release touts "AI-led efficiencies helped reduce headcount by 2%" (line 158) yet omits the one efficiency ratio. Selective disclosure while the ratio is a live RED leans confirmatory-negative. → A4 must extract C/I on management basis. |
| FN7 | F16 / ABSENT #7 | ABSENT-DISCLOSURE #7 | 155-156 | "Total income increased by 19% YoY to Rs 2,603 Mn" / "Net interest income increased by 16% YoY to Rs 1,447 Mn" | FORWARD-SIGNAL | Second hard-gate metric — Fees & commission income ≥Rs12 Cr/qtr — not disclosed. Only Total Income (2,603) and NII (1,447) given; the 1,156 Mn residual is all non-interest income, not isolable to fees. Co-lending fee share (<5% tripwire) uncheckable from this doc. → A4 must extract fee/commission line. |

---

## ABSENT-DISCLOSURE RECONCILIATION (against A2 ledger ABSENT section, lines 193-222)

| A2 ABSENT # | item | A3 disposition |
|-------------|------|----------------|
| 1 | Standalone financial statements | Absent — confirmed. No P&L/BS/CF; only summary KPIs. N.A. for statement-level checks. |
| 2 | Consolidated statements / basis undisclosed | **FN2** — surfaced as AMBIGUOUS finding (basis not stated anywhere). |
| 3 | Segment reporting | Absent — feeds **FN4** (no mix/segment split despite disbursement/AUM divergence). |
| 4 | Auditor limited-review report | Absent — drives F4/F5/F14-vs-auditor = N.A.; no UDIN/opinion to test. |
| 5 | Notes to accounts | Absent — F6/F7 note-mining limited to the MD quote + disclaimer only. |
| 6 | Cost-to-Income ratio | **FN6** — hard-gate metric, FORWARD-SIGNAL, omitted while a live RED. |
| 7 | Fees & commission income | **FN7** — hard-gate metric, FORWARD-SIGNAL, omitted. |

Both hard-gate pre-entry conditions (C/I ≤35% AND fee income ≥Rs12 Cr) are
therefore UNTESTABLE from this press release. The pre-entry conditional cannot
be resolved on this artifact; A4 must route both to the Aug-6 concall / Reg-33
filing.

---

## CHECKLIST SCORECARD

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | FINDING | Total Income QoQ dash (line 122) masks -0.2% QoQ inside a PAT/NIM/RoA sequential-softness cluster (FN1). |
| F2 STANDALONE vs CONSOL | FINDING | Reporting basis undisclosed anywhere; no S-vs-C gap computable (FN2, ABSENT #2). |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone/consolidated cost lines and no entity list in a press release. |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor report / Other Matters attached; nothing to ratio. |
| F5 GOING CONCERN / EoM | N.A. | No auditor EoM/going-concern paragraph; no prior-quarter extract for verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | MD quote "new lending verticals … deepening strategic partnerships" (line 248-249) + Aug-6 concall commitment (FN3). |
| F7 HEDGE PHRASE MINING | PASS | Only the standard forward-looking-statement disclaimer (lines 281-290); no note-level hedge on lumpiness/concentration newly added. |
| F8 TAX FORENSICS | N.A. | No PBT/tax line; PAT-only disclosure — ETR uncomputable. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial line disclosed. |
| F10 SHARE COUNT / DILUTION | N.A. | No paid-up capital or basic/diluted EPS disclosed. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | Net Worth 18,298 Mn given (line 165/219) but no paid-up + other-equity components to reconcile; NW growth-rate inconsistency captured under F14. |
| F12 SEGMENT FORENSICS | FINDING | No segment/mix or own-book-vs-co-lending split despite disbursement +128% vs AUM +28% divergence (FN4). |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | No AR/AGM/dividend/director/capital-raise items; only a concall notice (housed in F6). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | bps/growth deltas inconsistent with displayed rounded values (NIM, CoB, Net Worth) — FN5. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list present; no prior list to diff. |
| F16 DROPPED / ABSENT DISCLOSURES | FINDING | Two hard-gate metrics — Cost-to-Income (FN6) and Fee/commission income (FN7) — absent; live-tripwire omission is the primary assigned forensic item. |
| F17 CONCALL SILENCE AUDIT | N.A. | Concall is Aug 6, 2026 — no transcript yet; press-release-level silence already logged via FN6/FN7 for the Aug-6 audit. |

Scorecard completeness: 17/17 marked, zero blanks — GATE A3 = pass.

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | ref (line) | status word |
|-----------|--------------|------------|-------------|
| Host Q1FY27 earnings conference call | Aug 6, 2026, 4:00 PM IST | 258, 260 | initiated (scheduled) |
| Scale portfolio through existing + new lending verticals, deepen strategic partnerships | undated (ongoing) | 248-249 | underway ("As we continue to scale") |

---

## FORWARD-SIGNAL / AMBIGUOUS ROUTING TO A4

FORWARD-SIGNAL (feed A4 management questions): FN3 (new verticals / co-lending economics), FN6 (Cost-to-Income on mgmt basis), FN7 (fee & commission income line).
AMBIGUOUS (A4 to resolve, bear-leaning): FN1 (QoQ profit/margin softness drivers), FN2 (standalone vs consolidated basis), FN4 (disbursement-vs-AUM mix / off-book share).
NEUTRAL-FACT: FN5 (delta/rounding data-quality).

Highest-value items for A4, per task: FN6 (Cost-to-Income absent — cleanest pre-entry metric, live RED), FN7 (fee income absent — second hard gate), FN2 (undisclosed standalone/consolidated basis).

---

```yaml
stage: A3-forensics
company: "paisalo"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/paisalo-q1fy27/work/forensics_paisalo_q1fy27_pressrelease.md"
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
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN1", check: "F1", line: "122", classification: "AMBIGUOUS", implication: "Total Income QoQ dashed (2,603 vs 2,609) masks -0.2% QoQ inside a PAT -15% / NIM -26bps / RoA -20bps QoQ softness cluster framed as stable/healthy"}
  - {id: "FN2", check: "F2", line: "119", classification: "AMBIGUOUS", implication: "Standalone-vs-consolidated basis undisclosed anywhere; PAT/Net Worth basis unknown"}
  - {id: "FN3", check: "F6", line: "248-249", classification: "FORWARD-SIGNAL", implication: "New lending verticals + deepening partnerships = SBI co-lending expansion (margin-dilutive monitorable)"}
  - {id: "FN4", check: "F12", line: "120-121", classification: "AMBIGUOUS", implication: "Disbursement +128% vs AUM +28% with no own-book/co-lending split = off-book origination or short-tenor churn"}
  - {id: "FN5", check: "F14", line: "124", classification: "NEUTRAL-FACT", implication: "NIM/CoB/Net-Worth bps and growth deltas inconsistent with displayed rounded values; data-quality flag"}
  - {id: "FN6", check: "F16", line: "155-160", classification: "FORWARD-SIGNAL", implication: "Cost-to-Income (hard-gate, live RED tripwire) omitted while efficiency is touted; untestable pre-entry condition"}
  - {id: "FN7", check: "F16", line: "155-156", classification: "FORWARD-SIGNAL", implication: "Fees & commission income (hard-gate >=Rs12 Cr) not disclosed; co-lending fee-share tripwire uncheckable"}
forward_signals: ["FN3", "FN6", "FN7"]
ambiguous: ["FN1", "FN2", "FN4"]
commitments:
  - {commitment: "Host Q1FY27 earnings conference call", implied_date: "2026-08-06 16:00 IST", ref: "line 258,260", status_word: "initiated"}
  - {commitment: "Scale portfolio via existing + new lending verticals, deepen strategic partnerships", implied_date: "undated", ref: "line 248-249", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
