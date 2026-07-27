# A3 FORENSIC NOTES — AEROFLEX INDUSTRIES LTD | Q1 FY27 | doctype: RESULTS

Source extract: `runs/aeroflex-q1fy27/work/extract_results_aeroflex_q1fy27.txt`
Ledger: `runs/aeroflex-q1fy27/work/ledger_results_aeroflex_q1fy27.md`
Ledger reconciliation: 100% (all 15 notes, 81 line-items, 20 zero-standing, 2 agenda, 10 auditor-paras, 2 entities read at cited lines).
Classification taxonomy (per prompt): FORWARD-SIGNAL / AMBIGUOUS / CONFIRMATORY-NEGATIVE / NEUTRAL-FACT. (RED-FLAG maps to CONFIRMATORY-NEGATIVE.)

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-F1 | F1 | Set C line 133 (ZERO_STANDING) | 133 | "Exceptional items / Diminution in value of Investment ... - - - -" | FORWARD-SIGNAL | The only *named* zero-standing line is an investment-impairment slot. The sole investment (Hyd-Air, loss-making, assets Rs 3,825.35 L) is exactly what it anticipates. A future write-down would land here; watch. |
| A3-F2 | F2 | Set A line 75 (C PAT) vs Set C line 138 (SA PAT) | 75, 138 | consol "1,879.31" vs standalone "1,905.89" | AMBIGUOUS | Standalone PAT now EXCEEDS consolidated by 26.58 L (sub drag). Gap direction reversed vs FY26 (consol was +24.48 ABOVE standalone). Subsidiary is a volatile Q1/Q4 drag; re-entered loss. A4 question: is Hyd-Air structurally seasonal-loss or deteriorating? |
| A3-F6 | F6 | Note 3, lines 93/146; D&A line 66; Finance line 65; Reg32 line 188 | 93, 66, 65, 188 | "has increased the production capacity of its liquid cooling SFN skid assemblies from 6,000 pieces per annum to 9,000 pieces per annum" | FORWARD-SIGNAL | Capacity uplift COMPLETED (3rd of the ramp to 15,000 by ~Mar-27). Confirmed by D&A +32% (592.79->784.41) and finance cost +98% (17.77->35.26 = new debt for capex). Rs 10.38 Cr GCP funds still undeployed = further firepower. |
| A3-F8 | F8 | Tax lines 72/73 (C), 135/136 (SA), 74/137 earlier-yr | 72, 73, 74 | current tax "715.68" / deferred "(5.59)" / earlier-yr FY26 "25.38" | FORWARD-SIGNAL | ETR stepped up to 27.4% (Q4FY26 21.9%), now ABOVE statutory 25.17%. Deferred-tax credit shrank 28.11->5.59 YoY (shield ~22 bps and fading = future ETR normalization/step-up). Sub loss creates NO DTA (consol deferred = SA deferred = 5.59). FY26 earlier-year true-up 25.38/36.38. |
| A3-F9 | F9 | OCI lines 81 (C), 140 (SA), 98 (Set B) | 81, 140 | Other Comprehensive Income "- - - -" | AMBIGUOUS | OCI is zero in ALL four periods INCLUDING FY26 audited, despite employee-benefit expense of 1,394.23 L (gratuity/leave). No actuarial remeasurement recognized even annually. Verify OCI/actuarial treatment at Annual Report; possible P&L-lumping or non-disclosure. |
| A3-F13 | F13 | Agenda Item 2, lines 27/151-156 | 27, 151 | "Appointment of M/s. Kailash Chand Jain & Co., Chartered Accountants ... as Tax Auditor ... for the Financial Year 2026-27" | AMBIGUOUS | A separately-empaneled tax auditor (RBI/C&AG/SFIO panel) appointed alongside thin-fee statutory auditor Shweta Jain & Co — bandwidth-additive OR a scope split; "Reason of Change" framing implies a change. Note: AGM Notice + Annual Report (which carry the Italica FY27 RPT cap — Notion's cleanest governance metric) are NOT in this filing = still pending. Schedule Role 6 AR deep-dive when it drops. |
| A3-F14 | F14 | Sig block line 158; Set C line 133 vs Set A line 70 | 158, 133 | "Ruthu John Parampogi" (l.158) vs "Ruthu Parampogi" (ll.33,169,189,198) | NEUTRAL-FACT | CS name variant + standalone exceptional line labelled "Diminution in value of Investment" while consolidated line is bare "Exceptional items". Individually immaterial; cumulatively a drafting/governance data point. Confirm CS identity. |

(F3, F4, F5, F7, F10, F11 = PASS; F12, F16, F17 = N.A. — see scorecard.)

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | FINDING | Standalone impairment line "Diminution in value of Investment" (l.133) stands at zero while sole investment Hyd-Air is loss-making (assets 3,825.35 L). NCI zero (l.80) confirms Hyd-Air 100%-owned = full 26.58 loss to owners. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | SA PAT (1,905.89) EXCEEDS C PAT (1,879.31) by 26.58 L; gap direction reversed from FY26 (consol +24.48 above SA). Sub is volatile Q1/Q4 drag. |
| F3 SHELL-ENTITY DETECTION | PASS | Hyd-Air has distinct cost lines (materials C 8,422.70 vs SA 8,015.44 = +407.26; employee +63.81; D&A +56.48; revenue 765.66, l.50) — a real operating entity, not a shell. No going-concern EoM. |
| F4 UNAUDITED CONTRIBUTION | PASS | Component not reviewed by principal auditor = Hyd-Air: 1.4% of consol PAT, 5.3% of revenue (l.49-50) — both below 10% threshold. Note: principal relied "solely on the reports of the other auditors" (l.51); ties to Notion auditor-bandwidth watch. Trend N/A (no prior ledger). |
| F5 GOING CONCERN / EoM | PASS | Both LRRs UNMODIFIED, no Emphasis of Matter, no going-concern language (ll.52, 116). No prior-quarter extract supplied, so no verbatim diff; nothing to track this filing. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Capacity 6,000->9,000 skids "has increased" = COMPLETED milestone (ll.93/146); capex confirmed by D&A +32% and finance cost +98%; Rs 10.38 Cr GCP funds undeployed (l.188). See commitment register. |
| F7 HEDGE-PHRASE MINING | PASS | No F7 lexicon hits in notes; no newly-added hedge on revenue lumpiness or customer concentration. Notable ABSENCE: no hedge language accompanies the single-customer liquid-cooling capacity note. |
| F8 TAX FORENSICS | FINDING | ETR 27.4% Q1FY27 (>25.17% statutory), up from 21.9% Q4FY26; deferred credit fading 28.11->5.59 (~22 bps, shrinking shield); sub loss yields no DTA; FY26 earlier-year tax 25.38/36.38 (ll.74/137). |
| F9 OCI FORENSICS | FINDING | OCI = zero every period incl FY26 audited (ll.81,140,98) despite growing gratuity-bearing workforce. No swing to measure, but zero-annual actuarial OCI is itself an AR-verify question. |
| F10 SHARE COUNT / DILUTION | PASS | Paid-up 2,586.41->2,646.62 (+60.21 L / Rs2 FV = 3.01M shares) traces cleanly to preferential issue allotted 03-Feb-26 (Reg32 l.175-176, ~Rs 183/sh). Basic = Diluted in all periods (ll.85-86,144-145) = no dilutive overhang. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Net worth (FY26): consol 44,727.35 L, standalone 44,653.61 L; consol-SA other-equity diff 73.74 L = expected consolidation adjustment. No third-party number in filing to reconcile; Q1 other-equity not disclosed (standard). No >5% gap. |
| F12 SEGMENT FORENSICS | N.A. | Single segment, "segment-wise reporting not applicable" (Note 5, ll.100/146). |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Only extra resolution = tax-auditor appointment (Item 2, l.27). No AR/AGM/dividend/director change (confirmed absent, ledger l.172). Italica FY27 RPT cap (AGM Notice) still pending. |
| F14 NOTE-DRAFTING INCONSISTENCIES | FINDING | CS name variant "Ruthu John Parampogi" vs "Ruthu Parampogi" (l.158); exceptional-line label differs SA vs consol (l.133 vs l.70). Low severity, governance data point. |
| F15 ENTITY-LIST DIFFS | PASS | Single subsidiary Hyd-Air Engineering Pvt Ltd (l.44), unchanged within-filing. No prior-quarter ledger supplied (ledger l.3/209) so cross-quarter diff not performable; A4 to verify no entity change vs company memory. |
| F16 DROPPED/REFRAMED (presentation) | N.A. | Doctype = results, not a presentation. |
| F17 SILENCE AUDIT (concall) | N.A. | Doctype = results, not a transcript. Silences on GST/ROCE/Italica addressed in tripwire section below (results filings do not carry MD&A). |

Blank checks: none. GATE A3 = PASS (17/17 marked).

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|------------|--------------|-----|-------------|
| SFN liquid-cooling skid capacity raised 6,000 -> 9,000 pcs/annum | effective this quarter (Notion: 01-Jul-26); target 15,000 by ~Mar-27 | Note 3, lines 93 / 146 | completed ("has increased") |
| Board approved appointment of Kailash Chand Jain & Co as Tax Auditor for FY26-27 | July 27, 2026; term FY2026-27 | Item 2, lines 27 / 154 | completed / approved |
| General Corporate Purpose funds Rs 12.02 Cr allocated; only Rs 1.64 Cr (13.6%) deployed; Rs 10.38 Cr to be utilised | open (allotment 03-Feb-26) | Reg32, lines 188 / 196 | underway / pending deployment |

---

## TRIPWIRE TEST — mapping findings to Notion pre-committed triggers

- **(a) ROCE < 18% thesis-broken trigger [FY26 20.40%, borderline].** No ROCE in a results filing (F17 silence expected). Directional read from this quarter is FAVOURABLE, not adverse: consol EBITDA margin 23.04% (Q1FY26 18.35%, +469 bps) hits the 23% FY27 guide; revenue +72.4% YoY outpaced other expenses +66.6% and employee +53.8% (positive operating leverage). PAT +162% YoY. This *supports* ROCE holding above 18% near-term. Tripwire NOT fired. A4: still a "red silence" — no explicit ROCE disclosure.
- **(b) Capex-absorption / CFO-PAT gap.** CONFIRMED ACTIVE via A3-F6: D&A +32% (784.41 L) and finance cost +98% (35.26 L, new debt) evidence the capex cycle; Rs 10.38 Cr preferential proceeds still undeployed. No cash-flow statement in this filing to test CFO/PAT directly. Watch the capex-absorption tripwire; not fired.
- **(c) Single unnamed US tech customer, INDIA-ONLY exclusivity.** Note 3 capacity build (A3-F6) is for exactly this liquid-cooling line, yet the notes carry NO concentration/lumpiness hedge (F7 absence). Demand-side visibility untested here; Q2 unit disclosure (~Oct-26) remains the confirmation test.
- **(d) Italica Global FZC RPT / auditor bandwidth.** Italica FY27 RPT cap lives in the AGM Notice, which is NOT in this filing (A3-F13) = still pending. Auditor bandwidth: principal auditor relied SOLELY on other auditors for the loss-making sub (F4, l.51); Item 2 splits tax audit to a larger empaneled firm (A3-F13) — bandwidth-additive but worth an A4 question.
- **(e) Contingent liabilities (IT Rs 41.76 Cr; GST Rs 8.56 Cr).** Not disclosed in a results filing (no notes to accounts here). Zero-standing exceptional/impairment lines (F1) carry no provision. Silence expected; verify at AR.
- **(f) Auditor fee/bandwidth (Shweta Jain Rs 3 L).** Two clean UNMODIFIED LRRs, same partner (CA Ravi Jain), two correct UDINs (F5/F14). No qualification. Reliance-on-other-auditors for Hyd-Air noted.
- **(g) Promoter caution history.** No new governance event in this filing beyond the tax-auditor appointment (A3-F13) and CS name variant (A3-F14).

**Three "red silences" status:** GST exposure — silent (expected, no notes-to-accounts in results). US M&A pillar — silent. ROCE trajectory — silent, but Q1 operating metrics point favourable. All three remain concall/AR items for A4/Role 5.

**Net:** No pre-committed tripwire fired. Two forward-signals lean constructive (F6 capacity-completed, margin expansion) and one leans cautionary (F8 ETR step-up = a few-hundred-bps PAT headwind ahead). F2/F9/F13 are the AMBIGUOUS items for A4 to convert into management questions.

---

```yaml
stage: A3-forensics
company: "AEROFLEX"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/aeroflex-q1fy27/work/forensics_results_aeroflex_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1", check: "F1", line: "133", classification: "FORWARD-SIGNAL", implication: "Named investment-impairment line at zero while sole investment (Hyd-Air) loss-making; future write-down candidate"}
  - {id: "A3-F2", check: "F2", line: "75/138", classification: "AMBIGUOUS", implication: "Standalone PAT exceeds consolidated by 26.58L; S-vs-C gap direction reversed vs FY26; subsidiary re-entered loss"}
  - {id: "A3-F6", check: "F6", line: "93", classification: "FORWARD-SIGNAL", implication: "Capacity 6000->9000 completed; D&A +32%, finance cost +98% confirm capex cycle; Rs 10.38 Cr GCP funds undeployed"}
  - {id: "A3-F8", check: "F8", line: "72/73", classification: "FORWARD-SIGNAL", implication: "ETR stepped to 27.4% (>statutory); deferred shield fading 28.11->5.59; sub loss yields no DTA; PAT headwind ahead"}
  - {id: "A3-F9", check: "F9", line: "81/140", classification: "AMBIGUOUS", implication: "Zero OCI every period incl FY26 audited despite gratuity workforce; verify actuarial treatment at Annual Report"}
  - {id: "A3-F13", check: "F13", line: "27", classification: "AMBIGUOUS", implication: "Tax-auditor appointment (scope split / bandwidth); AGM Notice with Italica FY27 RPT cap still pending; schedule AR deep-dive"}
  - {id: "A3-F14", check: "F14", line: "158", classification: "NEUTRAL-FACT", implication: "CS name variant + differing exceptional-line labels SA vs consol; confirm CS identity"}
forward_signals: ["A3-F1", "A3-F6", "A3-F8"]
ambiguous: ["A3-F2", "A3-F9", "A3-F13"]
commitments:
  - {commitment: "SFN skid capacity 6000->9000 pcs/annum (target 15000 by ~Mar-27)", implied_date: "2026-07-01", ref: "Note 3, lines 93/146", status_word: "completed"}
  - {commitment: "Board approved Kailash Chand Jain & Co as Tax Auditor FY26-27", implied_date: "2026-07-27", ref: "Item 2, lines 27/154", status_word: "completed"}
  - {commitment: "General Corporate Purpose Rs 12.02 Cr allocated, Rs 10.38 Cr still to deploy", implied_date: "open", ref: "Reg32, lines 188/196", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
