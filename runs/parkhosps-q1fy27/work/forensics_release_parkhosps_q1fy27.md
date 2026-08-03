# FORENSIC NOTES — Park Medi World Limited (PARKHOSPS), Q1 FY27 — doctype: release (Reg 30 Media/Earnings Release)

Agent: A3 Forensic Notes | Model: claude-opus-4-8 | Date: 2026-08-03
Inputs read: A1 extract `extract_release_parkhosps_q1fy27.txt` (183 lines), A2 ledger `ledger_release_parkhosps_q1fy27.md` (10 tables). Prior-quarter extract: NONE.
Ledger reconciliation: 100% — every A2 row (Tables 1-10, all 8 gated count fields + supplementary Tables 9-10) read verbatim at its cited line in the A1 extract before judging.

Doctype applicability (per task): F6/F7 (forward + hedge mining) and F16 (reframing) apply strongly; F10/F11 apply to share/net-worth numbers present; F1/F8/F13/F14 applied; deep balance-sheet/auditor checks F2/F3/F4/F5/F9/F12/F15 are N.A.; F17 (concall silence) is N.A. Conservative (bear-leaning) bias on interpretation.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F6 | T4 b1-5, T5 b1-5, T7 rows 4-9, T6 | 60, 82-94, 100-102, 140-148 | "the company expects to commission 1,490 beds in calendar year 2026" (L102); "expected to be commissioned in November 2026" (L88-89, L93-94) | FORWARD-SIGNAL | c.46% capacity add is a dense dated commitment stack (CY2026 1,490 beds; two Nov-2026 commissionings; 4,740 beds by Mar-27, 5,740 by Mar-28). Feeds Role-5 promise-vs-delivery tracker. Rudrapur is a SUBSEQUENT_EVENT (commissioned 2 Aug 2026, post 30-Jun quarter-end); Mehar is SAME_DAY_DISCLOSURE (agreement dated release date 3 Aug 2026) — neither is in Q1FY27 numbers. |
| FND-02 | F7 | T6 (quote), T8 row 1 | 128-129, 133, 173 | "newly commissioned beds still ramping up" (L128-129); "improving utilisation at newer facilities" (L133); "subject to certain risks and uncertainties" (L173) | FORWARD-SIGNAL | Management pre-frames the 1,224 bps YoY occupancy collapse as ramp drag — a hedge that next 1-2 quarters continue to carry sub-scale utilisation from the c.46% capacity build. Signals occupancy stays depressed while new beds fill. |
| FND-03 | F8 | T2 L118 / L120, T4 b2/b3, T6 | 72-73, 118, 120, 127 | "Net Profit ... growth of 35% YoY ... margin ... expansion of 220 bps" vs "EBITDA ... growth of 20% ... expansion of 20 bps" | FORWARD-SIGNAL | NP grows 35% while EBITDA grows only 20% and EBITDA margin only +20 bps; NP margin +220 bps. Release discloses NO tax line, no ETR, no deferred-tax note — the below-EBITDA gap (per task, partly a consolidated deferred-tax benefit + FD other income on Rs 2,998mn deposits) is undisclosed and likely non-repeatable. Future ETR normalisation = NP-growth step-down risk not visible in the headline. |
| FND-04 | F10 | T2 L120 vs L122 | 120, 122 | "Net Profit 886 ... 35%" (L120) vs "EPS (INR) 2.05 ... 20%" (L122) | AMBIGUOUS | EPS grows 20% while NP grows 35%: implied shares ~432mn (886/2.05) vs ~385mn (655/1.70) YoY = c.+12% share count, consistent with a fresh-issue/IPO base change. Per-share growth is 20%, not the 35% headlined. Only one EPS line given (no basic/diluted split) so dilutive-instrument spread not computable. A4 to reconcile share count / issuance timing. |
| FND-05 | F14 | T2 vs T5/T7; SUMMARY UNIT_INCONSISTENCY | 60/102 vs 141; 83, 88, 91; 111 vs 140 | "add 1,490 beds in calendar year 2026" (L60) vs "will add 1,450 beds to our network" (L141); "INR 177 crs" (L83) amid an "INR mn" table | AMBIGUOUS | Drafting inconsistencies: (a) CY2026 add = 1,490 beds vs "About" pipeline add = 1,450 beds (40-bed gap, different scopes, not reconciled); (b) mixed units mn vs crs with no conversion shown (L83/88/91); (c) "4,290 beds as on date" (L140) vs 3,960 quarter-end (L111). Individually immaterial, cumulatively a governance/precision data point — A4 to seek a single reconciled bed roadmap. |
| FND-06 | F16 | T2 L112 vs headline T3/T4 | 57-76, 112 | "Occupancy (%) 55.6% ... 67.8% ... -1,224 bps" (L112) | FORWARD-SIGNAL | The steepest metric move in the release (occupancy down 1,224 bps YoY, 692 bps QoQ) appears only in the table — absent from the headline preview, the 5 Highlights bullets, and the MD quote, which lead with capacity +32% and revenue/EBITDA/NP growth. Selective emphasis buries the demand-density signal; low occupancy on a rising bed base pressures ARPOB/margin ahead. |
| FND-07 | F16 | T2 L118/L119/L112 QoQ col | 112, 118, 119 | "EBITDA ... 1,274 ... -1%" and "EBITDA Margin ... 27.7% ... -116 bps" QoQ (L118-119) | FORWARD-SIGNAL | QoQ, EBITDA fell 1%, EBITDA margin fell 116 bps (27.7%->26.5%), occupancy fell 692 bps (62.5%->55.6%). The narrative frames everything YoY and omits the sequential deterioration. Near-term trajectory is softening under capacity ramp; watch the monitoring-checklist EBITDA-margin <22%/2Q tripwire against this sequential slide. |

---

## CHECKLIST SCORECARD (all 17)

| # | Check | Status | One-line basis |
|---|---|---|---|
| F1 | Zero-value standing line items | PASS | A2 `zero_standing`=0; full sweep of all 55 table cells and narrative found no nil/dash/0 line item (ledger Table 2 note, L74). |
| F2 | Standalone vs consolidated decomposition | N.A. | Release carries only a consolidated summary; no standalone column to decompose (per doctype). |
| F3 | Shell-entity detection | N.A. | No standalone cost lines (materials/employee/depreciation) disclosed to compare. |
| F4 | Unaudited contribution ratio | N.A. | No auditor report / Other Matters paragraph in this doctype (`auditor_paras`=0). Whole set is unaudited (L54, L65-66) but no component-auditor split exists to ratio. |
| F5 | Going concern / EoM scope tracking | N.A. | No auditor EoM paragraph and no prior-quarter extract to verbatim-diff. |
| F6 | Forward-commitment phrase mining | FINDING | FND-01: dense dated commitment stack ("expects to commission", "expected to be commissioned", "in the process of", "will add", "approved") — see Commitment Register. |
| F7 | Hedge phrase mining | FINDING | FND-02: "still ramping up" / "improving utilisation" pre-frame the occupancy collapse; boilerplate "subject to" at L173. |
| F8 | Tax forensics | FINDING | FND-03: NP +35% vs EBITDA +20% with NO tax/ETR/deferred-tax disclosure; gap (deferred-tax benefit + FD income) undisclosed and likely non-repeatable. |
| F9 | OCI forensics | N.A. | No OCI / actuarial disclosure in the release. |
| F10 | Share count and dilution | FINDING | FND-04: EPS +20% vs NP +35% implies ~+12% shares YoY; no basic/diluted split disclosed. |
| F11 | Reserves and net-worth tie-out | N.A. | No paid-up capital, other equity, or net-worth figure disclosed; only term debt (256mn) and FDs (2,998mn) — no equity number to tie out. |
| F12 | Segment forensics | N.A. | No segment table (single-line consolidated summary only). |
| F13 | Board outcome beyond the results | PASS | No AR/Board's-Report/MD&A approval, no AGM notice/record date, no dividend, no director-term appointment. Only operational subsidiary approval (Umkal/Park Platinum, L85) — captured under F6, not a governance/funding signal. |
| F14 | Note-drafting inconsistencies | FINDING | FND-05: 1,490 vs 1,450 bed guidance; mn/crs unit mixing (L83/88/91); 4,290 vs 3,960 bed base. |
| F15 | Entity list diffs | N.A. | No prior-quarter ledger supplied; `ENTITY_CHANGE` cross-check impossible (ledger Table 10 note, L214). |
| F16 | Dropped/reframed disclosures | FINDING | FND-06 (occupancy collapse omitted from headline/quote) and FND-07 (QoQ deterioration masked by YoY framing). No prior deck, so reframing anchored within-release. |
| F17 | Concall silence audit | N.A. | Not a transcript (`turns`=0, `questions`=0); no call to audit for silence (per doctype). |

Blank checks: none. GATE A3 = PASS (17/17 marked exactly one of PASS/FINDING/N.A.).

Scorecard tally: PASS x2 (F1, F13); FINDING x6 (F6, F7, F8, F10, F14, F16); N.A. x9 (F2, F3, F4, F5, F9, F11, F12, F15, F17). Total 17.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (line) | status word |
|---|---|---|---|
| Panchkula 350-bed greenfield hospital commissioned | 10 Apr 2026 (in-quarter) | L81 | completed |
| Agra 360-bed facility commissioned | Feb 2026 | L100 | completed |
| Rudrapur (The Medicity) acquisition, INR 177 crs, definitive agreement signed | signed 25 May 2026; commissioned 2 Aug 2026 (post quarter-end SUBSEQUENT_EVENT) | L82-84 | completed |
| Mehar Hospital, Zirakpur acquisition, INR 107 crs, "150+" beds, definitive agreement | signed 3 Aug 2026 (SAME_DAY_DISCLOSURE); commission Nov 2026 | L90-94 | initiated |
| Park Platinum 100-bed expansion at Palam Vihar (Umkal Health Care) | subsidiary approved 30 Jun 2026; commission Nov 2026 | L85-89 | underway |
| Febris 200-bed hospital, Narela (Delhi) | "upcoming commissioning", CY2026 | L101 | underway |
| Commission 1,490 beds in CY2026 (c.46% capacity add over 3,250) | by Dec 2026 | L60 / L102 / L132 | underway |
| Integrate 5 additional hospitals + expand 2 units, add 1,450 beds | "in the process of", staged to FY27/FY28 | L140-141 | underway |
| Total capacity to reach 4,740 beds | by March 2027 | L148 | expected |
| Total capacity to reach 5,740 beds | by March 2028 | L148 | expected |

Per-bed price note (monitoring-checklist trigger, acquisition >Rs 1.0 Cr/bed): Mehar = Rs 107 crs / "150+" beds -> <=Rs 0.71 Cr/bed IF beds are exactly 150, but capacity is stated open-ended ("150+", L92) so exact per-bed price is NOT cleanly disclosed. Rudrapur = Rs 177 crs with no bed count disclosed -> per-bed not computable. A4/A5: per-bed price is indeterminate on the face of the release; trigger cannot be evaluated precisely. Flagged, not resolved.

---

## HANDOFF TO A4 (questions to generate)
- FORWARD-SIGNAL: FND-01, FND-02, FND-03, FND-06, FND-07
- AMBIGUOUS: FND-04, FND-05
- Priority questions implied: (1) quantify the deferred-tax/other-income component of the EBITDA-to-NP gap and its repeatability (FND-03); (2) reconcile share count and issuance so per-share vs absolute NP growth is clear (FND-04); (3) disclose exact Mehar/Rudrapur bed counts to evaluate the Rs 1.0 Cr/bed acquisition tripwire (FND-01); (4) occupancy trajectory and expected trough given the ramp (FND-02/FND-06/FND-07); (5) single reconciled bed roadmap (1,490 vs 1,450; 3,960 vs 4,290) (FND-05).

```yaml
stage: A3-forensics
company: "PARKHOSPS"
quarter: "Q1 FY27"
doctype: "release"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/forensics_release_parkhosps_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-01", check: "F6", line: "60,82-94,100-102,140-148", classification: "FORWARD-SIGNAL", implication: "Dense dated commitment stack: 1,490 beds CY2026, two Nov-2026 commissionings, 4,740 by Mar-27 / 5,740 by Mar-28; Rudrapur post-quarter subsequent event, Mehar same-day disclosure."}
  - {id: "FND-02", check: "F7", line: "128-129,133,173", classification: "FORWARD-SIGNAL", implication: "'Still ramping up' / 'improving utilisation' pre-frame occupancy collapse; signals continued sub-scale utilisation next 1-2 quarters."}
  - {id: "FND-03", check: "F8", line: "72-73,118,120,127", classification: "FORWARD-SIGNAL", implication: "NP +35% vs EBITDA +20% with no tax/ETR/deferred-tax disclosure; below-EBITDA boost likely non-repeatable, ETR normalisation risk to NP growth."}
  - {id: "FND-04", check: "F10", line: "120,122", classification: "AMBIGUOUS", implication: "EPS +20% vs NP +35% implies ~+12% shares YoY (issuance/IPO base); per-share growth is 20%, not 35%; no basic/diluted split."}
  - {id: "FND-05", check: "F14", line: "60,141,83,88,91,111,140", classification: "AMBIGUOUS", implication: "1,490 vs 1,450 bed guidance, mn/crs unit mixing, 4,290 vs 3,960 bed base; needs one reconciled roadmap."}
  - {id: "FND-06", check: "F16", line: "112", classification: "FORWARD-SIGNAL", implication: "Occupancy -1,224 bps YoY buried in table, absent from headline/quote; low occupancy on rising bed base pressures ARPOB/margin."}
  - {id: "FND-07", check: "F16", line: "112,118,119", classification: "FORWARD-SIGNAL", implication: "QoQ EBITDA -1%, margin -116 bps, occupancy -692 bps masked by YoY-only framing; sequential softening vs 22%/2Q tripwire."}
forward_signals: ["FND-01", "FND-02", "FND-03", "FND-06", "FND-07"]
ambiguous: ["FND-04", "FND-05"]
commitments:
  - {commitment: "Panchkula 350-bed greenfield commissioned", implied_date: "2026-04-10", ref: "L81", status_word: "completed"}
  - {commitment: "Agra 360-bed facility commissioned", implied_date: "2026-02", ref: "L100", status_word: "completed"}
  - {commitment: "Rudrapur (Medicity) acquisition INR 177 crs, agreement signed", implied_date: "2026-05-25 signed / 2026-08-02 commissioned", ref: "L82-84", status_word: "completed"}
  - {commitment: "Mehar Hospital Zirakpur acquisition INR 107 crs, 150+ beds", implied_date: "2026-08-03 signed / 2026-11 commission", ref: "L90-94", status_word: "initiated"}
  - {commitment: "Park Platinum 100-bed expansion (Umkal/Palam Vihar)", implied_date: "2026-06-30 approved / 2026-11 commission", ref: "L85-89", status_word: "underway"}
  - {commitment: "Febris 200-bed hospital, Narela commissioning", implied_date: "CY2026", ref: "L101", status_word: "underway"}
  - {commitment: "Commission 1,490 beds CY2026 (c.46% add)", implied_date: "2026-12", ref: "L60/L102/L132", status_word: "underway"}
  - {commitment: "Integrate 5 hospitals + 2 unit expansions, add 1,450 beds", implied_date: "FY27-FY28", ref: "L140-141", status_word: "underway"}
  - {commitment: "Total capacity 4,740 beds", implied_date: "2027-03", ref: "L148", status_word: "expected"}
  - {commitment: "Total capacity 5,740 beds", implied_date: "2028-03", ref: "L148", status_word: "expected"}
gate_a3: pass
blank_checks: []
```
