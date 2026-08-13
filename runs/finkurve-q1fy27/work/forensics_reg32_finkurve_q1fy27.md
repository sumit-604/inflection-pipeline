# A3 FORENSIC NOTES — Finkurve Financial Services Ltd (Arvog) — Q1 FY27
Doctype: results — Regulation 32(1) use-of-proceeds declaration + Annexure 1 (preferential issue of equity shares and share warrants, private placement). Filename token: reg32.
Ticker: FINKURVE | Quarter: Q1 FY27 (quarter ended June 30, 2026)
A1 extract: runs/finkurve-q1fy27/work/extract_reg32_finkurve_q1fy27.txt
A2 ledger: runs/finkurve-q1fy27/work/ledger_reg32_finkurve_q1fy27.md
Ledger reconciliation: 41/41 disclosure units read at their cited A1 lines (100%).

## SCOPE NOTE
This is a two-page SEBI Reg 32(1) deviation declaration, not a financial-statement filing, concall, or presentation. There are no financial statements, no standalone/consolidated split, no auditor Other-Matters paragraph, no segment tables, no consolidation-entity list, no OCI/tax notes, and no transcript. F2-F5, F8, F9, F11-F13, F15-F17 are therefore N.A. and marked so explicitly. Signal in this document lives in exactly three places, per the A2 flags: (1) TOTAL_RAISED vs Funds Utilised gap, (2) the inline warrant-subscription note, (3) the DEVIATION_DECLARATION = "No" attestation. All three are worked below.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F6-1 | F6 forward-commitment phrase mining | Table 4 fn1 / Table 3 row 5 (Funds Utilised inline note) | 84-86 (span 79-86) | "share warrants subscription amount yet to be received" | FORWARD-SIGNAL | Rs 30 Cr is an expected-but-unrealised FY27 cash inflow contingent on warrant holders paying the 75% exercise call. It is a dateable management commitment (warrant exercise window falls in FY27). Directly maps to the Notion monitorable "Rs 40 Cr warrant cash expected FY27." If warrants lapse unexercised, the Rs 30 Cr never arrives and the associated onward-lending growth does not fund. Track receipt each quarter. |
| F10-1 | F10 share count and dilution | Table 2 row 2 (Mode of Fund Raising) + Table 3 rows 3/5 | 51-52; 77, 84-86 | "Preferential Issue of Equity Shares and Share Warrant" / "75% of the share warrants subscription amount yet to be received" | FORWARD-SIGNAL | Outstanding share warrants are a live dilutive instrument with exercise still pending on 75% of subscription. The document's own arithmetic (Rs 30 Cr = 75%) implies total warrant subscription = Rs 40 Cr, corroborating the Notion Rs 40 Cr FY27 figure; Rs 10 Cr (25% application money) already in. Warrant exercise PRICE is NOT disclosed in this document, so the Notion tripwire "dilutive equity raise below Rs 40" is NOT testable here — A4 must source the warrant issue price and exercise deadline from the original preferential-issue postal ballot / offer document. |
| F14-1 | F14 note drafting inconsistencies | Table 2 row 4 (Amount Raised) vs Table 3 row 5 (Funds Utilised); Table 2 row 14 | 54 vs 77/84-86; 67 | "Amount Raised Rs. 141.50 Crore" vs "111.50 ... yet to be received" | AMBIGUOUS | The headline "Amount Raised Rs. 141.50 Crore" counts Rs 30 Cr of warrant money not yet received; cash actually realised = Rs 111.50 Cr, which exactly equals Funds Utilised — i.e. 100% of received proceeds deployed, zero idle capital-raise cash (disciplined deployment into the stated object). But the label "raised" overstates realised proceeds by ~Rs 30 Cr (~21%). Secondary quirk: line 67 "Not Applicable" heads a table that is nonetheless populated with utilisation data (standard SEBI-form artefact, immaterial). A4 question: confirm the Rs 141.50 Cr split across fully-paid equity, 25% warrant application money received, and the Rs 30 Cr (75%) exercise money still receivable; confirm warrant exercise deadline. |

---

## INTERNAL-CONSISTENCY WORKING (task-directed: warrant shortfall + deployment)

- Rs 30 Cr stated as "75% of the share warrants subscription amount" ⇒ total warrant subscription = 30 / 0.75 = Rs 40.00 Cr. This ties exactly to the Notion monitorable (Rs 40 Cr warrant cash FY27). Internally consistent.
- Cash received to date = Amount Raised 141.50 − unreceived warrant money 30.00 = Rs 111.50 Cr. Funds Utilised = Rs 111.50 Cr. Received equals utilised ⇒ zero un-deployed cash; full deployment into "onward lending and investment and repayment of borrowing." Deployment matches the stated object.
- Implied structure: ~Rs 101.50 Cr equity + Rs 10 Cr warrant application money (25%) = Rs 111.50 Cr received and deployed; Rs 30 Cr warrant exercise money (75%) still receivable.
- DEVIATION_DECLARATION = "No" is defensible: unreceived warrant call money is an inflow-timing item, not a utilisation deviation. The "No" is NOT contradicted by the Rs 30 Cr gap. No false-attestation finding raised.
- Net: numbers reconcile; the shortfall's stated cause is internally consistent. The only live risk is contingency of the Rs 30 Cr inflow (warrant exercise), captured as F6-1 / F10-1.

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | Basis |
|-------|--------|-------|
| F1 zero-value standing line items | PASS | 10 ZERO_STANDING cells (Table 2 rows 9-14; Table 3 rows 2,4,6,7) are the standard SEBI deviation-form fields, dash/"NA"/"Not Applicable" because Deviation = "No"; no hidden transaction class concealed. AC-comments field (line 65) blank is consistent with the letter's "reviewed and noted, no adverse comment." |
| F2 standalone vs consolidated | N.A. | No financial statements; no S/C decomposition in a Reg 32 declaration. |
| F3 shell-entity detection | N.A. | No cost lines, no subsidiary financials. |
| F4 unaudited contribution ratio | N.A. | No auditor Other-Matters paragraph; CRISIL named as monitoring agency only. |
| F5 going concern / EoM scope | N.A. | No auditor report / EoM in this doctype. |
| F6 forward-commitment phrase mining | FINDING | Hit: "yet to be received" (line 84-86) = future FY27 warrant inflow. See F6-1. |
| F7 hedge phrase mining | PASS | Declaration + Annexure prose scanned for the hedge lexicon ("subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", etc.); no hits. "no material deviation" (line 22) is an attestation, not a pre-emptive hedge. |
| F8 tax forensics | N.A. | No P&L, no tax lines, no ETR computable. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure. |
| F10 share count and dilution | FINDING | Preferential issue includes share warrants; 75% of subscription unexercised = live dilution + Rs 40 Cr corroboration; exercise price undisclosed. See F10-1. |
| F11 reserves / net worth tie-out | N.A. | No balance sheet; warrant money would be a reconciling item but no net-worth figure is present to tie to. |
| F12 segment forensics | N.A. | No segment tables. |
| F13 board outcome beyond results | N.A. | Only an Audit Committee review of this declaration (line 25-26); no AR/Board's Report approval, no AGM notice/record date, no director appointment. No catalyst event to schedule. |
| F14 note drafting inconsistencies | FINDING | "Amount Raised Rs. 141.50 Crore" (line 54) vs realised/utilised Rs 111.50 Cr; plus "Not Applicable" (line 67) over a populated table. See F14-1. |
| F15 entity list diffs | N.A. | No consolidation entity list; single filing entity only. |
| F16 presentation dropped/reframed disclosures | N.A. | Not a presentation deck. |
| F17 concall silence audit | N.A. | Not a concall; no transcript. Note for A4: the Notion tripwire "dilutive raise below Rs 40" is not testable from this document (warrant price absent) — carry forward, do not resolve. |

Scorecard tally: PASS 2 (F1, F7) | FINDING 3 (F6, F10, F14) | N.A. 12 (F2, F3, F4, F5, F8, F9, F11, F12, F13, F15, F16, F17). Total 17, no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note / ref | status word |
|------------|--------------|------------|-------------|
| Rs 30 Cr (75% of the ~Rs 40 Cr share-warrant subscription) to be received | FY27 (warrant exercise window; declaration filed 13 Aug 2026 for quarter ended 30 Jun 2026) | Annexure 1 objects-table Funds Utilised inline note, A1 lines 84-86 | awaited / pending (not yet received) |

---

## HANDOFF TO A4
- Convert F6-1 and F10-1 (FORWARD-SIGNAL) and F14-1 (AMBIGUOUS) into management / monitoring questions.
- Priority A4 questions: (1) warrant exercise price and deadline (needed to test the Notion "below Rs 40" tripwire, untestable here); (2) confirm the Rs 141.50 Cr split (equity vs 25% warrant application vs 75% exercise receivable); (3) monitor quarterly receipt of the Rs 30 Cr warrant inflow against the FY27 Rs 40 Cr thesis assumption.
- Confirmatory positive to carry: received proceeds (Rs 111.50 Cr) fully deployed to the stated object with zero idle cash; deployment discipline is clean this quarter and the "No deviation" attestation is defensible.

```yaml
stage: A3-forensics
company: "finkurve"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/finkurve-q1fy27/work/forensics_reg32_finkurve_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
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
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F6-1", check: "F6", line: "84-86", classification: "FORWARD-SIGNAL", implication: "Rs 30 Cr (75% of a ~Rs 40 Cr warrant subscription) is an unrealised FY27 inflow contingent on warrant exercise; maps to Notion Rs 40 Cr FY27 monitorable; track receipt quarterly."}
  - {id: "F10-1", check: "F10", line: "51-52", classification: "FORWARD-SIGNAL", implication: "Share warrants are a live dilutive instrument, 75% unexercised; arithmetic implies Rs 40 Cr total subscription (corroborates Notion); exercise price undisclosed so 'below Rs 40' tripwire not testable here."}
  - {id: "F14-1", check: "F14", line: "54", classification: "AMBIGUOUS", implication: "'Amount Raised Rs 141.50 Cr' includes Rs 30 Cr not yet received; realised cash Rs 111.50 Cr equals Funds Utilised (zero idle, disciplined); label overstates proceeds ~21%; confirm equity/warrant split and exercise deadline."}
forward_signals: ["F6-1", "F10-1"]
ambiguous: ["F14-1"]
commitments:
  - {commitment: "Rs 30 Cr (75% of ~Rs 40 Cr share-warrant subscription) to be received", implied_date: "FY27", ref: "A1 lines 84-86 (Annexure 1 Funds Utilised inline note)", status_word: "awaited"}
gate_a3: pass
blank_checks: []
```
