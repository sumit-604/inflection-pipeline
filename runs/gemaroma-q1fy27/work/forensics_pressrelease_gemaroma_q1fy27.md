# A3 FORENSIC NOTES — GEMAROMA (Gem Aromatics Limited) — Q1FY27 — doctype: presentation (press release, narrative prose)

Source extract: `runs/gemaroma-q1fy27/work/extract_pressrelease_gemaroma_q1fy27.txt` (238 lines, 5 pages)
Ledger reconciled: `runs/gemaroma-q1fy27/work/ledger_pressrelease_gemaroma_q1fy27.md` — 82 disclosure units, 100% read at cited lines.
Prior quarter: NONE (first-time coverage). Notion monitoring checklist: NONE.

This is a Reg-30 press release, not a Reg-33 financial-statement filing. There is no auditor report, no tax line, no OCI, no balance sheet, no segment table, no consolidation entity list, no Board Outcome agenda. Those checks are marked N.A. with a one-line basis, never blank. The document carries two summary tables (standalone + consolidated), a five-bullet narrative, one attributed MD quote, 13 forward-looking statements, and a new-entity announcement — the live surface for F2, F6, F7, F10, F13, F14, F15, F16.

---

## HEADLINE FORENSIC (F2 — the story of this document)

The standalone and consolidated columns tell opposite stories in the SAME quarter. Standalone PAT is +11.0% YoY (Rs 7.3 Cr, line 78). Consolidated PAT swings to a Rs −7.9 Cr loss from +Rs 8.0 Cr a year ago (line 97, −198.6%). The entire gap is the wholly-owned subsidiary layer (Krystal Ingredients / the newly commissioned Dahej facility). Decomposition below. The narrative prose (page 3) and the MD quote (page 4) discuss only standalone-consistent positives ("YoY growth in revenue") and never name the consolidated loss — that framing gap is itself a finding (F16).

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|---------------------|
| F2-1 | F2 | C4, C6, C9 vs S4, S6, S9 | 93 / 97 / 102 | "PAT  -7.9  8.0  -198.6%" (line 97) | FORWARD-SIGNAL | Subsidiary (Krystal/Dahej) swung from +Rs1.5 Cr PAT contribution (Q1FY26) to −Rs15.2 Cr drag (Q1FY27); gap = −208% of standalone PAT vs +23% a year ago (231pp swing, >>5pp gate). Whole consolidated thesis now rides on the Q3–Q4FY27 Krystal revenue ramp absorbing Dahej fixed cost. |
| F6-1 | F6 | FL1–FL8, R6 | 117-148, 133 | "revenue contribution is expected to commence towards the end of Q2FY27, with a more meaningful contribution from Q3FY27" (line 142-143) | FORWARD-SIGNAL | Nine dated, falsifiable milestones (Cooling Agents Q3FY27; Safranal end-Q2/Q3FY27; Phenol trial end-Q2, commercial Q3, revenue Q4FY27; Brazil WOS). Feeds Role 5 promise-vs-delivery tracker. See Commitment Register. |
| F7-1 | F7 | FL7 | 146-147 | "Commercial production is targeted during Q3FY27, subject to completion of the required approvals and quality processes" | AMBIGUOUS | Pre-emptive hedge attached to the single most loaded milestone quarter (Q3FY27, where all three Krystal lines are guided to contribute). "subject to" gives cover for slippage; A4 to ask what "required approvals" are outstanding and the gating date. |
| F10-1 | F10 | S8, C8 vs S6, C6 | 82 / 101 | "EPS (Rs)  1.4  1.4        2.3" (line 82; YoY%/QoQ% cells blank) | NEUTRAL-FACT | Implied standalone share count (PAT/EPS) rises ~4.64 Cr (Q1FY26) → ~5.21 Cr (Q1FY27) = denominator change, consistent with a recent IPO (BSE 544491 is a fresh listing). Explains the blank growth cells; no basic-vs-diluted split disclosed. Fresh IPO capital likely funding Dahej capex — A4 to confirm listing date and net proceeds. |
| F13-1 | F13 | R6 | 133 | "The Company has approved the incorporation of a Wholly Owned Subsidiary in Brazil" | FORWARD-SIGNAL | Board-level corporate action beyond the results: new foreign subsidiary = capital deployment + entity to track at next filing. Schedule an entity-diff at Q2FY27. |
| F14-1 | F14 | R6 vs FL12 | 133 vs 168 | "has approved the incorporation" (133) vs "the proposed Brazil subsidiary" (168) | AMBIGUOUS | Same entity described as "approved" (done) in the bullet and merely "proposed" (pending) in the MD quote. Status inconsistency: is incorporation board-approved-and-executing or still proposed? A4 question. |
| F14-2 | F14 | N9 vs cover-letter footer | 211 vs 53-54 | "operates three manufacturing facilities across Uttar Pradesh, Gujarat, and Daman & Diu" (211) | NEUTRAL-FACT | Cover-letter footer lists only two facilities — Facility 1 Silvassa (Dadra & Nagar Haveli) and Facility 2 Budaun, UP (lines 53-54). The Gujarat/Dahej facility (the ~Rs265 Cr capex site) and the third-facility geography are absent from the footer, and "Daman & Diu" ≠ "Dadra & Nagar Haveli" (Silvassa). Immaterial alone; a governance data point on drafting rigour. |
| F15-1 | F15 | R6 | 133 | "a Wholly Owned Subsidiary in Brazil to distribute essential oils, aromatic chemicals and specialty chemicals" | FORWARD-SIGNAL | NEW_ENTITY_ANNOUNCED. No prior ledger to diff (first coverage), but the document itself announces a new consolidation-scope entity. Establishes the baseline: at Q2FY27 confirm incorporation, capitalisation, and whether it consolidates. |
| F16-1 | F16 | narrative bullets vs C5/C6/C7 | 113, 122, 126 vs 95-99 | "Q1FY27 revenue from operations recorded YoY growth, reflecting an improvement in underlying business activity" (line 113) | FORWARD-SIGNAL | Selective framing: the five narrative bullets and the MD quote foreground standalone-style revenue growth and "gradual improvement," and never acknowledge that consolidated EBITDA fell −77.7% (line 93), consolidated EBITDA margin fell −1361 bps to 3.3% (line 95), or that consolidated PAT margin is −1708 bps at −8.0% (line 99). A4 to force management to address the consolidated loss on the 14-Aug call. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis |
|-------|--------|-------|
| F1 — Zero-value standing line items | N.A. | No Reg-33 statement template exists in a press release; the two `ZERO_STANDING` flags (S8, C8) are blank EPS YoY%/QoQ% growth cells, not nil transaction-class lines. Substance handled at F10-1 (denominator change) and F14 (drafting). |
| F2 — Standalone vs consolidated decomposition | **FINDING** | F2-1. Subsidiary PAT contribution swung +Rs1.5 Cr → −Rs15.2 Cr YoY (−208% of standalone PAT); EBITDA gap +4.4 → −5.2 Cr. Far exceeds the 5pp gate. |
| F3 — Shell-entity detection | N.A. | Press release gives no cost-line breakdown (no Cost of Materials / Employee Benefits / Depreciation split by S vs C) to run the identical-cost test. Note: the subsidiary is demonstrably operational (Rs~265 Cr Dahej capex, real losses), i.e. the opposite of a shell. |
| F4 — Unaudited contribution ratio | N.A. | No auditor report / Other Matters paragraph in a press release; results are wholly unaudited. |
| F5 — Going concern / EoM scope | N.A. | No auditor report, no EoM, and no prior quarter to verbatim-diff (first-time coverage). |
| F6 — Forward-commitment phrase mining | **FINDING** | F6-1. Nine dated management commitments (see Commitment Register). |
| F7 — Hedge phrase mining | **FINDING** | F7-1. "subject to completion of the required approvals and quality processes" hedging the Q3FY27 phenol commercial-production date. |
| F8 — Tax forensics | N.A. | No PBT and no tax expense line disclosed (PAT only); ETR uncomputable. |
| F9 — OCI forensics | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 — Share count and dilution | **FINDING** | F10-1. Implied share count ~4.64 → ~5.21 Cr (denominator change / recent IPO); blank EPS growth cells; no basic-vs-diluted split. |
| F11 — Reserves and net worth tie-out | N.A. | No balance sheet, reserves, or net-worth figure disclosed. |
| F12 — Segment forensics | N.A. | No segment tables (assets/liabilities/revenue) in a press release. |
| F13 — Board outcome beyond results | **FINDING** | F13-1. Board approved incorporation of a Brazil WOS. |
| F14 — Note drafting inconsistencies | **FINDING** | F14-1 ("approved" vs "proposed" Brazil status) and F14-2 (2-facility footer vs 3-facility About; Gujarat/Dahej absent; Daman&Diu vs Dadra&Nagar Haveli). |
| F15 — Entity list diffs | **FINDING** | F15-1. New entity (Brazil WOS) announced; sets baseline for Q2FY27 diff. |
| F16 — Dropped / reframed disclosures | **FINDING** | F16-1. Selective narrative framing — consolidated EBITDA/PAT collapse unmentioned in prose. (Cross-deck diff proper is not runnable: first coverage, no prior deck.) |
| F17 — Concall silence audit | N.A. | This is the press release, not a transcript; the earnings call is scheduled 14-Aug-2026 (line 179) and not yet held. The F6 Commitment Register becomes the silence-audit checklist for that call and the next quarter. |

Scorecard: FINDING x8 (F2, F6, F7, F10, F13, F14, F15, F16); N.A. x9 (F1, F3, F4, F5, F8, F9, F11, F12, F17); PASS x0. No blanks — GATE A3 pass.

---

## F2 DECOMPOSITION DETAIL (subsidiary + elimination layer = Consolidated − Standalone)

| Metric | Q1FY26 gap | Q4FY26 gap | Q1FY27 gap | Read |
|--------|-----------|-----------|-----------|------|
| Revenue (Rs Cr) | +11.2 | −1.8 | +15.9 | Subsidiary top line growing; the Q4FY26 negative gap implies eliminations > sub revenue that quarter. |
| EBITDA (Rs Cr) | +4.4 | +0.6 | −5.2 | Subsidiary flipped from EBITDA-accretive to a −Rs5.2 Cr operating drag. |
| PAT (Rs Cr) | +1.5 | −10.9 | −15.2 | Subsidiary swung +Rs1.5 Cr → −Rs15.2 Cr. |
| PAT gap as % of standalone PAT | +23% | −92% | −208% | 231pp deterioration YoY. |

Depreciation back-out (Cash PAT − PAT): standalone ≈ Rs1.6 Cr (8.9 − 7.3); consolidated ≈ Rs9.2 Cr (1.3 − (−7.9)); subsidiary depreciation ≈ Rs7.6 Cr. This matches the narrative "higher depreciation of Rs. 9.1 Cr, following the capitalization of a significant portion of the ~Rs. 265 Cr capex incurred for the Dahej facility" (lines 128-129). Interpretation for A4: the consolidated loss is overwhelmingly front-loaded fixed cost (Dahej depreciation + start-up operating cost) on a pre-scale revenue base. The bull case is that the Q3–Q4FY27 Krystal ramp (F6-1 milestones) absorbs it; the bear case is that a −Rs15 Cr quarterly subsidiary drag compounds if the dated milestones slip (F7-1 hedge). This is the single most important number in the document and the narrative prose never states it (F16-1).

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Ref | Status word |
|---|-----------|-------------|-----|-------------|
| 1 | Krystal Cooling Agents (GEM Cool 03/05/23) revenue contribution; audits done, initial orders secured | Q3FY27 | line 138-141 (FL4) | underway (orders secured) |
| 2 | Krystal Safranal revenue contribution commences | end Q2FY27 | line 142-143 (FL5) | underway (in customer approvals) |
| 3 | Krystal Safranal "more meaningful contribution" | Q3FY27 | line 143-144 (FL5) | underway |
| 4 | Krystal Phenol Derivatives trial production commences | end Q2FY27 | line 145 (FL6) | initiated (not started) |
| 5 | Krystal Phenol Derivatives commercial production ("subject to approvals") | Q3FY27 | line 146-147 (FL7) | initiated (hedged) |
| 6 | Krystal Phenol Derivatives meaningful revenue contribution | Q4FY27 | line 147-148 (FL8) | initiated |
| 7 | Newer product verticals revenue "to build progressively" | undated / progressive | line 117-119 (FL1) | underway |
| 8 | "gradual improvement in margins" from product mix + operating leverage | undated | line 123-125 (FL2/FL3) | initiated |
| 9 | Brazil Wholly Owned Subsidiary incorporation (LatAm distribution) | undated (board-approved, not incorporated) | line 133 (R6) / restated 168 (FL12) | approved / initiated |

Silence-audit seed for the 14-Aug-2026 call: any of commitments 1–9 not addressed = a "What Was NOT Discussed" row at Q2FY27, with F7-1's hedge (Q3FY27 phenol "subject to approvals") the highest-priority probe.

---

## RECONCILIATION NOTE

All 82 ledger units read at their cited extract lines: financial rows S1–S9 (lines 71-83) and C1–C9 (lines 88-102); narrative N1–N21 (lines 128-213); MD quote Q1–Q5 (lines 157-173); forward statements FL1–FL13 (lines 117-173); regulatory R1–R8 (lines 12-237); earnings-call E1–E12 (lines 179-193); pages P1–P5. Ledger flags absorbed: `ZERO_STANDING` S8/C8 → F1/F10; `APPROX_VALUE` N2 (~Rs265 Cr) → F2 detail; `NEW_ENTITY_ANNOUNCED` R6 → F13/F15; `MISSING_VALUE` E12 (Diamond Pass Link blank) noted, administrative, no forensic weight; the A2-surfaced S/C PAT divergence → F2-1. ledger_reconciled_pct = 100.

---

```yaml
stage: A3-forensics
company: "GEMAROMA"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gemaroma-q1fy27/work/forensics_pressrelease_gemaroma_q1fy27.md"
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
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F2-1", check: "F2", line: "97", classification: "FORWARD-SIGNAL", implication: "Subsidiary (Krystal/Dahej) swung +Rs1.5Cr to -Rs15.2Cr PAT drag YoY (-208% of standalone PAT); consolidated thesis rides on Q3-Q4FY27 ramp absorbing Dahej fixed cost"}
  - {id: "F6-1", check: "F6", line: "117-148", classification: "FORWARD-SIGNAL", implication: "Nine dated Krystal/Brazil milestones (end-Q2FY27 to Q4FY27) seed the promise-vs-delivery tracker"}
  - {id: "F7-1", check: "F7", line: "146-147", classification: "AMBIGUOUS", implication: "'subject to completion of required approvals' hedges the Q3FY27 phenol commercial-production date, the most loaded milestone quarter"}
  - {id: "F10-1", check: "F10", line: "82", classification: "NEUTRAL-FACT", implication: "Implied share count ~4.64Cr to ~5.21Cr (recent IPO); blank EPS growth cells; no basic-vs-diluted split; confirm listing date and net proceeds"}
  - {id: "F13-1", check: "F13", line: "133", classification: "FORWARD-SIGNAL", implication: "Board approved Brazil WOS incorporation = capital deployment + new entity to track at Q2FY27"}
  - {id: "F14-1", check: "F14", line: "133", classification: "AMBIGUOUS", implication: "Brazil described 'approved' (bullet 133) vs 'proposed' (MD quote 168) - status inconsistency"}
  - {id: "F14-2", check: "F14", line: "211", classification: "NEUTRAL-FACT", implication: "About claims 3 facilities (UP/Gujarat/Daman&Diu) but footer lists only 2 (Silvassa, Budaun); Gujarat/Dahej absent; geography mismatch - drafting-rigour data point"}
  - {id: "F15-1", check: "F15", line: "133", classification: "FORWARD-SIGNAL", implication: "New consolidation-scope entity (Brazil WOS); baseline for Q2FY27 entity diff"}
  - {id: "F16-1", check: "F16", line: "113", classification: "FORWARD-SIGNAL", implication: "Narrative and MD quote foreground revenue growth and 'gradual improvement' while never naming the consolidated -77.7% EBITDA / -Rs7.9Cr PAT loss; force management to address on the call"}
forward_signals: ["F2-1", "F6-1", "F13-1", "F15-1", "F16-1"]
ambiguous: ["F7-1", "F14-1"]
commitments:
  - {commitment: "Krystal Cooling Agents revenue contribution (audits done, initial orders secured)", implied_date: "Q3FY27", ref: "line 138-141 (FL4)", status_word: "underway"}
  - {commitment: "Krystal Safranal revenue contribution commences", implied_date: "end Q2FY27", ref: "line 142-143 (FL5)", status_word: "underway"}
  - {commitment: "Krystal Safranal meaningful contribution", implied_date: "Q3FY27", ref: "line 143-144 (FL5)", status_word: "underway"}
  - {commitment: "Krystal Phenol Derivatives trial production commences", implied_date: "end Q2FY27", ref: "line 145 (FL6)", status_word: "initiated"}
  - {commitment: "Krystal Phenol Derivatives commercial production (subject to approvals)", implied_date: "Q3FY27", ref: "line 146-147 (FL7)", status_word: "initiated"}
  - {commitment: "Krystal Phenol Derivatives meaningful revenue contribution", implied_date: "Q4FY27", ref: "line 147-148 (FL8)", status_word: "initiated"}
  - {commitment: "Newer product verticals revenue to build progressively", implied_date: "progressive/undated", ref: "line 117-119 (FL1)", status_word: "underway"}
  - {commitment: "Gradual margin improvement from product mix + operating leverage", implied_date: "undated", ref: "line 123-125 (FL2/FL3)", status_word: "initiated"}
  - {commitment: "Brazil Wholly Owned Subsidiary incorporation (LatAm distribution)", implied_date: "undated (board-approved, not incorporated)", ref: "line 133 (R6)/168 (FL12)", status_word: "approved"}
gate_a3: pass
blank_checks: []
```
