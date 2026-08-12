# A3 FORENSIC NOTES — Sharika Enterprises Limited (SHARIKA), Q1FY27 — doctype: results

Source A1 extract: `extract_results_sharika_q1fy27.txt` (v2, 597 lines, unit Lakhs).
A2 ledger: `ledger_results_sharika_q1fy27.md` (61 line items + 20 notes + 28 auditor paras + 24 signature blocks + 4 entities). **Ledger rows read at cited line = 100% reconciled.** No prior-quarter extract available (`NO_PRIOR_LEDGER`); prior facts diffed from the supplied Notion memory only, flagged where it limits a verbatim diff.

Doctype rule: on a results filing F1-F15 apply, F16/F17 are normally N.A. **F17 is run and marked FINDING here on the explicit direction in the task message** (silence audit against the Notion monitoring checklist + verbatim diff of the auditor qualification paragraphs). F16 stays N.A. (no presentation deck in scope).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| F1-a | F1 | §8 r12 / §9 r15 (Exceptional Items, ZERO_STANDING) | 263 (SA), 520 (CA) | "Exceptional Items … - " | FORWARD-SIGNAL | The Exceptional Items line stands empty in every period — it is the exact template home for the impairment the auditor says has NOT been taken (Spintech carrying value 579.69 vs accumulated losses 514.68, EOM line 228) and for the un-computed ECL on receivables. An empty exceptional line next to three "no provision made" qualifications is where a future write-down lands. |
| F2-a | F2 | §8 r18 vs §9 r21 (PAT) | 274 (SA 22.86), 527 (CA 29.86) | "Profit / (Loss) after tax … 22.86" ; "Profit I (Loss) after tax … 29.86" | AMBIGUOUS | Consol-minus-standalone PAT gap flipped sign: Q1FY26 -66.93, FY26 -119.64 (subsidiaries a drag) → Q4FY26 +24.01, Q1FY27 +7.00 (subsidiaries additive). A >5pp-of-standalone-PAT swing. Consol PAT now EXCEEDS parent PAT while NCI is a loss (-4.75). Genuine subsidiary turnaround or a consolidation/elimination artifact? Needs an A4 question. |
| F3-a | F3 | §9 r7/r9 vs §8 r6/r8 (Employee, Depreciation) | 511 vs 257; 513 vs 259 | "Employee benefit expenses … 173.79" (CA) vs "145,05" (SA) | FORWARD-SIGNAL | Subsidiaries are NOT identical-cost shells, but they carry +28.74 employee cost and +6.29 depreciation while adding only +0.24 revenue (CA 2,220.07 vs SA 2,219.83, line 504 vs 251). Cost and assets, ~zero external revenue = pre-revenue / dormant-operational build (Spintech SCADA vehicle). Future funding or impairment need. Yet consol profit is HIGHER than parent — driven by a consol-only inventory credit (34.14, line 510) and lower other expenses; flag with F2-a. |
| F5-a | F5 | §3 r13 (EOM Spintech) vs §4 r13 (EOM Note 7 only) | 224-230 (SA), 456-477 (CA) | "Our opinion is not modified in respect of the aforesaid matters." (SA 232) | AMBIGUOUS | EoM scope is asymmetric: standalone EOM carries BOTH Note 7 (sequential settlement) and Note 6 (Spintech no-impairment); consolidated EOM carries ONLY Note 7. Defensible (Spintech losses already inside consol numbers) but must be confirmed. No prior-quarter extract to verbatim-diff the paragraph — `NO_PRIOR_LEDGER`. The Spintech non-impairment rests on a soft forward justification (see F6-a). |
| F6-a | F6 | §5 r6 / §6 r6 (Note 6) | 317-318 (SA), 576-577 (CA) | "supported by a Preliminary Agreement with Brazil's SPIN Engenharia … and Identified projects under negotatlon" | FORWARD-SIGNAL | Sole documented forward commitment in the notes. The entire Spintech no-impairment argument (514.68 accumulated loss un-provided) hangs on an unquantified, undated "Preliminary Agreement" + "projects under negotiation." Dateable: track for conversion to an order/revenue. Feeds Role 5 promise-vs-delivery. |
| F7-a | F7 | §5 r9 / §6 r9 (Note 9) | 331 (SA), 587 (CA) | "including those related to MSME and Interest etc. If any payable In this respect are currently not ascertainable" | AMBIGUOUS | Pre-emptive hedge: MSME dues and MSMED-Act interest declared "not ascertainable." Notion flags MSME payables jumped 16x to 4.68 Cr FY26 with interest unascertained; the note continues that opacity. An unquantified statutory interest liability that can crystallise. A4 question: quantify MSME payable + interest. |
| F8-a | F8 | §8 r14/r15 (Current/Deferred tax) | 266 (current "-"), 267 (deferred 9.02) | "Current tax … -" ; "Deferred tax … 9.02" | AMBIGUOUS | Nil current tax even in a positive-PBT quarter (PBT 31.88); ETR 28.3% is 100% deferred. FY26 ran persistent deferred-tax CREDITS (-249.08, line 267) that recognised a DTA (Notion Rs 2.95 Cr) during losses; this quarter deferred tax turns to EXPENSE (+9.02) — the DTA is now reversing. DTA recoverability depends on sustained profit the loss history (FY24-26 CFO negative) does not support. "Taxation pertaining to earlier years" is nil (line 268) — that sub-test PASSes. |
| F10-a | F10 | §8 r23/r25-26 (Paid-up, EPS) | 286 (2,165.00), 292-293 (EPS 0.05) | "Paid-up equity share capita … 2,165.00" ; Basic/Diluted "0.05 / 0.05" | FORWARD-SIGNAL | Paid-up unchanged all periods; basic = diluted (no spread) = no dilutive instrument reflected. But per Notion the 17 Jul 2026 EGM approved up to **1,51,49,079 equity shares (non-promoter) + 38,38,102 warrants** — ~44% potential dilution on the 4.33 Cr share base (2,165.00 lakh / Rs 5). This 12 Aug filing does not disclose the issue at all and diluted EPS ignores the approved warrants. Large near-term dilution not yet in the count; Reg 30 (allottee/price) incoming. |
| F11-a | F11 | §8 r24 / §9 r33 (Other Equity) | 288 (SA -217.33), 552 (CA -835.99) | "Other Eequlty Excluding Revaluation Reserves … (217.33)" ; "… (835.99)" | CONFIRMATORY-NEGATIVE | Other Equity negative on both statements (SA -217.33 lakh, CA -835.99 lakh = -8.36 Cr), confirming Notion. Disclosed only in the FY-ended column (`PARTIAL_DISCLOSURE`, blank in all 3 quarter columns) so QoQ net-worth erosion is invisible in the interim filing. Consol reserves have consumed 39% of paid-up. No third-party (rating/slide) number available to tie-out against. |
| F13-a | F13 | §1 (agenda) + §2a (sign-off timing) | 73-75, 80 | "The meeting commenced at 04:30 P.M. and concluded at 10:00 P.M." | AMBIGUOUS | Single-item board meeting (results approval only) ran 5.5 hours; CS signed 22:14, 14 min after close. No AGM notice, no AR approval, no dividend, and — critically — **no capital-raising enabling resolution or preferential-issue pricing/allottee**, despite the 17 Jul EGM having approved the issue 25 days earlier. Disproportionate duration + no capital-raise progression = unresolved substance; watch the next Reg 30. |
| F14-a | F14 | §3 r13 vs §5 r6 (Spintech loss figure); §5 r10 (entity name) | 228 vs 316; 336/588 | auditor: "accumulated losses of Rs. 514.68 lakhs" (228) vs Note 6: "accumulated losses of ~514.63 lakhs" (316) | CONFIRMATORY-NEGATIVE | Company's own Note 6 and the auditor's qualified-opinion paragraph state DIFFERENT Spintech accumulated-loss figures (514.63 vs 514.68 lakh) for the identical fact at the identical date; both independently OCR-confirmed, unharmonized in the source (`SOURCE_DOCUMENT_INCONSISTENCY`). Plus entity-name inconsistency "Electtromeccanica"/"Electromeccanica" (336/588). Amounts immaterial; cumulatively a control-weakness / governance data point consistent with the qualifications and CFO revolving door. |
| F15-a | F15 | §7 (entity list) + §5/§6 r10 (Note 10) | 388-392; 336 (SA), 588 (CA) | "the investment of the Company in its joint venture has been eroded due to accumulated losses" | AMBIGUOUS | Consolidation scope: Holding + 3 subsidiaries (Spintech, Smartec, Contronics). JV Electromeccanica India Pvt Ltd EXCLUDED, investment eroded to nil (Note 10), not on the entity list. Smartec and Contronics appear nowhere else in the filing. Cannot verbatim-diff the entity list vs prior quarter (`NO_PRIOR_LEDGER`) — cannot confirm whether the JV exclusion is new this quarter. A4: source prior entity list; confirm no residual carrying value / contingent exposure on Electromeccanica. |
| F17-a | F17 | Notion monitorables vs filing | see silence table | 331, 186/435, 162-163 | CONFIRMATORY-NEGATIVE (forward element on pref-issue) | Silence audit vs the 6 re-entry signals + tripwires: filing is conspicuously silent on the preferential issue (allottee/price), on cash flow (CFO undisclosed — no interim CFS), on the MSME payable amount, and on any new/second ADMS order. Auditor qualification NOT removed — verbatim carried forward from FY26 on all 3 counts. Detail below. |

---

## F17 SILENCE AUDIT — Notion monitorables vs this filing (verbatim-diffed where possible)

**Auditor qualification paragraph diff vs FY26 (signal 1 / tripwire):** DID NOT FIRE. All three FY26 qualification counts persist verbatim, each closing with "Our Report for the quarter and year ended March 31, 2026 was also qualified in respect of this matter" (lines 162-163, 181-182, 193-194 SA; 417-418, 430-431, 442-443 CA):
- (a) inventory Rs 149.25 lakh, no obsolescence provision (Note 8, line 153-163) — FY26 amount ~1.46 Cr, now 1.49 Cr, still unprovided.
- (b) advances Rs 210.66 lakh, >3 yrs, no recoverability provision (Note 9, line 171-182) — FY26 ~2.45 Cr → 2.11 Cr, still unprovided.
- (c) trade receivables Rs 4,862.30 lakh (SA) / 5,273.38 lakh (CA), no ECL under Ind AS 109 (line 184-194 / 433-443) — FY26 54.18 Cr → 48.62 Cr SA / 52.73 Cr CA. Still >3yr, litigated, un-provided.

| # | Monitorable (Notion) | Filing status | Consecutive-quarter silence | Read |
|---|----------------------|---------------|------------------------------|------|
| 1 | Audit qualification REMOVED FY27 | NOT removed; all 3 counts carried forward verbatim (l.162-163) | addressed (confirmed non-fire) | CONFIRMATORY-NEGATIVE |
| 2 | Equity raise / strategic stake at ≥CMP | **SILENT** — preferential issue (EGM 17 Jul) not mentioned; no allottee, no price, no use-of-proceeds, no board resolution | 1 (first post-EGM quarter) | FORWARD-SIGNAL (Reg 30 pending; F10-a, F13-a) |
| 3 | First CLEAN operating quarter: op profit +ve AND CFO > Rs 0.5 Cr | Operating profit POSITIVE (PBT 31.88 SA / 40.97 CA); **CFO SILENT** — no interim cash-flow statement | CFO silent 1 (interim) | half-fired / AMBIGUOUS |
| 4 | Receivables 54.18 Cr → ≤35 Cr with disclosed collection | Addressed but DID NOT FIRE: 48.62 Cr SA / 52.73 Cr CA, still >3yr, no ECL, no collection disclosed | addressed | CONFIRMATORY-NEGATIVE |
| 5 | MSME payables back to ~0.30 Cr | **SILENT on amount** — Note 9 says MSME + interest "currently not ascertainable" (l.331) | opaque, continuing | CONFIRMATORY-NEGATIVE |
| 6 | 2nd/3rd software/ADMS order beyond East India Udyog / UPCL | **SILENT** — no order book, no ADMS/SCADA progress, no UPCL delivery update; only Spintech "projects under negotiation" (l.317) | 1 | CONFIRMATORY-NEGATIVE |
| T | Note 7 sequential settlement (supplier float) | CONTINUES — Note 7 present (l.321/579), EOM'd both statements | ongoing | CONFIRMATORY-NEGATIVE |
| T | CFO negative 3 yrs | Not disclosed (no interim CFS) | silent | CONFIRMATORY-NEGATIVE |
| T | MD Rajinder Kaul on Audit Committee (independence) | Kaul signs as MD (l.340/593); committee composition not disclosed | silent | CONFIRMATORY-NEGATIVE |
| T | Copper / fixed-price margin resilience | No pass-through / margin commentary; SA PBT margin 1.4% | silent | CONFIRMATORY-NEGATIVE |

---

## CHECKLIST SCORECARD

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 | FINDING | Empty Exceptional Items line (263/520) is the template home for the un-taken Spintech impairment / un-computed ECL. |
| F2 | FINDING | Consol-vs-standalone PAT gap flipped sign and swung >5pp of standalone PAT (Q1FY26 -66.93 → Q1FY27 +7.00). |
| F3 | FINDING | Subsidiaries carry employee/depreciation cost (+28.74/+6.29) with ~zero incremental revenue (+0.24) = pre-revenue build, not pure shells. |
| F4 | PASS | No Other Matters / component-auditor paragraph; all 3 subsidiaries reviewed by R D V; JV excluded at nil → 0% unaudited PAT. |
| F5 | FINDING | EoM scope asymmetric (Spintech EOM standalone-only); Spintech non-impairment rests on soft forward justification; no prior extract to verbatim-diff. |
| F6 | FINDING | Note 6 "Preliminary Agreement with … SPIN Engenharia … projects under negotiation" — sole forward commitment, underpins no-impairment. |
| F7 | FINDING | Note 9 hedge: MSME dues + interest "currently not ascertainable" (331/587) — unquantified statutory liability. |
| F8 | FINDING | Nil current tax in a profit quarter; FY26 persistent DTA credits (-249.08) now reversing to expense (+9.02); DTA recoverability risk. |
| F9 | PASS | Actuarial re-measurement 0.48 net; single-quarter swing does not exceed full prior year (1.95). No assumption-change signal. |
| F10 | FINDING | Paid-up unchanged, basic = diluted, but ~44% approved preferential dilution (1.51 Cr shares + 38.38 lakh warrants) undisclosed here. |
| F11 | FINDING | Negative Other Equity (SA -217.33 / CA -835.99), disclosed FY-column only; QoQ net-worth erosion invisible. |
| F12 | N.A. | Single reportable segment (Note 5, l.309/570); no segment asset/liability disclosure in interim results to trend. |
| F13 | FINDING | 5.5-hr single-item board meeting; no capital-raise / AGM / AR resolution despite pending preferential issue. |
| F14 | FINDING | 514.63 (Note 6) vs 514.68 (auditor EOM) lakh discrepancy + "Electtromeccanica"/"Electromeccanica" name inconsistency. |
| F15 | FINDING | JV Electromeccanica excluded (eroded to nil); cannot diff entity list vs prior quarter (NO_PRIOR_LEDGER). |
| F16 | N.A. | No presentation deck in scope (results filing). |
| F17 | FINDING | Silence audit: silent on preferential-issue terms, CFO, MSME amount, new orders; qualification NOT removed (verbatim carried forward). |

Blank checks: none. **GATE A3: pass** (all 17 statuses assigned).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Spintech carrying value recovery via "Preliminary Agreement with Brazil's SPIN Engenharia" for smart-grid automation + "identified projects under negotiation" (justifies non-impairment of 514.68 lakh accumulated loss) | none stated (ongoing) | Note 6, l.317-318 (SA) / 576-577 (CA) | under negotiation (in-process) |
| Sequential settlement arrangement with vendors continues; receivables under it pledged in bank stock statements | ongoing | Note 7, l.321-324 (SA) / 579-581 (CA) | underway (continuing) |

No "expected by / will be / shall be completed / board has approved / commenc" hits carrying a hard date were present in the notes; the notes are commitment-thin, which is itself consistent with the F17 silence pattern.

---

```yaml
stage: A3-forensics
company: "SHARIKA"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sharika-q1fy27/work/forensics_sharika_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F1-a", check: "F1", line: "263/520", classification: "FORWARD-SIGNAL", implication: "Empty Exceptional Items line is the template home for the un-taken Spintech impairment / un-computed ECL"}
  - {id: "F2-a", check: "F2", line: "274/527", classification: "AMBIGUOUS", implication: "Consol-vs-standalone PAT gap flipped sign and swung >5pp; consol PAT now exceeds parent while NCI loses"}
  - {id: "F3-a", check: "F3", line: "511/257", classification: "FORWARD-SIGNAL", implication: "Subsidiaries carry cost + assets but ~zero revenue = pre-revenue build; future funding/impairment"}
  - {id: "F5-a", check: "F5", line: "224-230/456-477", classification: "AMBIGUOUS", implication: "EoM scope asymmetric; Spintech non-impairment on soft justification; no prior extract to diff"}
  - {id: "F6-a", check: "F6", line: "317-318", classification: "FORWARD-SIGNAL", implication: "SPIN Engenharia Preliminary Agreement + projects under negotiation underpin no-impairment; track conversion"}
  - {id: "F7-a", check: "F7", line: "331/587", classification: "AMBIGUOUS", implication: "MSME dues + interest declared not ascertainable; unquantified statutory liability that can crystallise"}
  - {id: "F8-a", check: "F8", line: "266-267", classification: "AMBIGUOUS", implication: "Nil current tax in profit quarter; DTA recognised in losses now reversing; recoverability risk / ETR step-up"}
  - {id: "F10-a", check: "F10", line: "286/292-293", classification: "FORWARD-SIGNAL", implication: "~44% approved preferential dilution (1.51 Cr shares + 38.38 lakh warrants) undisclosed; Reg 30 incoming"}
  - {id: "F11-a", check: "F11", line: "288/552", classification: "CONFIRMATORY-NEGATIVE", implication: "Negative Other Equity disclosed FY-column only; QoQ net-worth erosion invisible in interim filing"}
  - {id: "F13-a", check: "F13", line: "80", classification: "AMBIGUOUS", implication: "5.5-hr single-item meeting, no capital-raise resolution despite pending preferential issue; watch next Reg 30"}
  - {id: "F14-a", check: "F14", line: "228/316", classification: "CONFIRMATORY-NEGATIVE", implication: "514.63 vs 514.68 lakh Spintech loss inconsistency + entity-name garble = control-weakness data point"}
  - {id: "F15-a", check: "F15", line: "336/588", classification: "AMBIGUOUS", implication: "JV Electromeccanica excluded (eroded to nil); cannot diff entity list vs prior quarter"}
  - {id: "F17-a", check: "F17", line: "331/186/162-163", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on pref-issue terms, CFO, MSME amount, new orders; qualification not removed (verbatim carried forward)"}
forward_signals: ["F1-a", "F3-a", "F6-a", "F10-a"]
ambiguous: ["F2-a", "F5-a", "F7-a", "F8-a", "F13-a", "F15-a"]
commitments:
  - {commitment: "Spintech carrying-value recovery via Preliminary Agreement with Brazil's SPIN Engenharia + identified projects under negotiation", implied_date: "none stated (ongoing)", ref: "Note 6 l.317-318 SA / 576-577 CA", status_word: "under negotiation"}
  - {commitment: "Sequential settlement arrangement with vendors; receivables pledged in bank stock statements", implied_date: "ongoing", ref: "Note 7 l.321-324 SA / 579-581 CA", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
