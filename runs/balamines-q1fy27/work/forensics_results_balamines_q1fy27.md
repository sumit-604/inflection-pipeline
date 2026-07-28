# A3 FORENSIC NOTES — Balaji Amines Limited (BALAMINES), Q1 FY27 — DOCTYPE: results

Source extract: `/home/user/inflection-pipeline/runs/balamines-q1fy27/work/extract_results_balamines_q1fy27.txt`
Reconciled against A2 ledger: `/home/user/inflection-pipeline/runs/balamines-q1fy27/work/ledger_results_balamines_q1fy27.md`
Ledger reconciliation: 100% (every line_item, zero_standing, note, auditor_para, entity, agenda and signature row read at its cited line before judging).
Units: Rs Lakhs (x0.01 -> Cr). First quarterly coverage for BALAMINES — no prior-quarter extract to diff.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F2 | Sec.2 L126 / Sec.3 L188, L190-191 | 126, 188, 191 | S "7,214.24" vs C "7,811.77"; NCI "318.11" (Q1FY27) vs "(147.26)" (Q1FY25) | FORWARD-SIGNAL | Sole subsidiary Balaji Speciality Chemicals swung from PAT drag to contributor YoY: consol-minus-standalone PAT gap moved from -327.24 L (-8.22% of standalone PAT) in Q1FY26 to +597.53 L (+8.28%) in Q1FY27, a ~16.5pp swing (>5pp threshold). NCI flipped from -147.26 L loss-share to +318.11 L profit-share. Subsidiary turnaround is the live growth vector; A4 to probe durability, capacity, product mix. |
| A3-02 | F12 | Sec.4 L261, L264, L245, L248 | 261, 264 | Seg. liabilities Amines "28,958.53" (Q1FY27) vs "45,364.44" (Q4FY26); Total "43,742.82" vs "59,081.80" | AMBIGUOUS | Segment liabilities fell sharply QoQ: Amines & Speciality -16,405.91 L (-36%), total -15,338.98 L (-26%). Standalone finance cost also dropped QoQ 103.77 -> 26.94 L; consol 217.58 -> 141.22 L. Ambiguous: WC unwind of a Q4 year-end build vs genuine debt paydown. Falling finance cost leans toward debt reduction. Generate concall question (borrowings movement, WC days). |
| A3-03 | F14 | Sec.6a L367-371 vs Sec.1 L57 | 370-371, 57 | Auditor cert "Date:2026.07.27 172529 +0550"; Board "concluded at 5:35 P.M." | AMBIGUOUS | Standalone limited-review report's embedded digital-signature timestamp 17:25:29 (5:25:29 PM) predates the Board Meeting's stated 5:35 P.M. conclusion by ~9.5 min. The review report on the results the Board "took note of" is timestamped before the Board formally closed. Could be clerical, could be sequencing. Consolidated cert timestamp OCR-degraded (fragment "538" only, L432) — before/after status INDETERMINABLE, not clean. A4 question / consider pulling source-PDF cert metadata. |
| A3-04 | F14 | Sec.6b L417; L372 vs L433 | 417, 372, 433 | "The Statement includes the results of the subsidiary, Balaji Speciality Chemicals Limited."; partner "MYV Ranganath" vs "MV Ranganath" | NEUTRAL-FACT | Consolidated report carries an "Other Matter" para (para 4) absent from standalone; it merely states inclusion of the subsidiary with no quantified reliance/component-auditor language (subsidiary is already inside review scope per para 1, L397-399, so the para is redundant, not a scope carve-out). Partner name renders MYV vs MV across the two reports (same membership 028031). Individually immaterial; cumulatively a governance/drafting data point. |
| A3-05 | F8 | Sec.2 L124 / Sec.3 L186 | 124, 186 | Earlier years' tax "48.51" (both standalone and consolidated, 30.06.2026) | NEUTRAL-FACT | Current-quarter "Earlier years' tax" is non-zero (48.51 L = 0.49 Cr, both statements) — mechanical FINDING per F8 rule. Prior-year tax true-up; small. Consol comparative Q1FY25 carried 159.94 L. Recurrent earlier-year adjustments suggest ongoing assessment settlements; monitor but not material to ETR (Q1FY27 ETR ~26.3% S / ~26.4% C vs 25.17% statutory — no anomaly). |
| A3-06 | F5 | Sec.6a/6b; Sec.6b L417 | 356-361, 417 | Standalone para 4 "nothing has come to our attention..."; consol para 4 "The Statement includes the results of the subsidiary..." | NEUTRAL-FACT | FIRST-OBSERVATION baseline — no prior-quarter extract available, so recorded not PASSed-by-absence. Both reports UNMODIFIED; no Going Concern, no Emphasis of Matter. Only non-standard element is the consolidated "Other Matter" para 4 (see A3-04). Baseline for future QoQ EoM/opinion diffs: opinion=unmodified, GC=none, EoM=none, one Other-Matter inclusion para on consolidated. |
| A3-07 | F15 | Sec.7 L251-252; Note 3 L301 | 301, 398, 417 | "results of subsidiary, Balaji Speciality Chemicals Limited" | NEUTRAL-FACT | FIRST-OBSERVATION entity baseline — no prior-quarter list to diff. Consolidation scope = 2 entities: Balaji Amines Limited (parent) + Balaji Speciality Chemicals Limited (sole subsidiary). No JVs, no associates, no step-down subsidiaries named. Future quarters diff against this 2-entity baseline; any add/delete/rename/relationship change = finding. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | PASS | All 13 ZERO_STANDING rows read (L119,129,130,131,132,136,181,194,195,196,197,204,247). Exceptional Items nil all periods both statements = clean earnings, no one-offs; OCI sub-lines and "items to be reclassified to P&L" nil = no cash-flow-hedge/FX-translation reserve; Other equity blank in quarter columns = standard Ind AS annual-only. No standing line anticipates an undisclosed transaction class. |
| F2 S-vs-C DECOMPOSITION | FINDING | A3-01. YoY subsidiary PAT swing ~16.5pp of standalone PAT (>5pp), loss-share to profit-share. |
| F3 SHELL-ENTITY DETECTION | PASS | Cost lines differ S vs C: materials 23,596.80 vs 24,609.25; employee 2,400.20 vs 2,582.58; depn 1,154.17 vs 1,378.24 (L110/172, 113/175, 114/176). Subsidiary carries own materials, payroll and ~224 L/qtr depreciation = real operations, not a shell. No going-concern EoM. |
| F4 UNAUDITED CONTRIBUTION | PASS | Subsidiary within review scope per consol para 1 (L397-399); no component-auditor/reliance carve-out. Subsidiary PAT contribution 597.53 L = 7.65% of consol PAT, below 10%; reviewed by same firm. Redundant Other Matter para flagged under F14 (A3-04). |
| F5 GOING CONCERN / EoM | FINDING | A3-06. First-observation baseline (no prior quarter); unmodified, no GC/EoM; non-standard consol Other Matter para recorded. |
| F6 FORWARD-COMMITMENT MINING | PASS | Notes 1-5 (L291-304) swept for lexicon. Only past-tense/descriptive language ("were considered, approved and taken on record", "are prepared in accordance with"). No "expected/will be/underway/commenc/board has approved (future)/intends to". Commitment register empty. |
| F7 HEDGE-PHRASE MINING | PASS | Notes and auditor reports swept for hedge lexicon ("no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour"). No pre-emptive hedge on revenue lumpiness or customer concentration added to notes. |
| F8 TAX FORENSICS | FINDING | A3-05. Earlier years' tax non-zero (48.51 L both statements, current qtr). ETR ~26% near statutory; deferred tax is a persistent charge (not credit) = no DTA-shield step-up risk. |
| F9 OCI FORENSICS | PASS | Remeasurement of DB plans nil in current qtr both statements (L129/194). No single-quarter swing to assess. Booked historically at year-end (Q4FY26 S (33.55), C (25.29); FY26 S (14.99), C (16.98)) — normal Q1 pattern, no assumption change this quarter. |
| F10 SHARE COUNT & DILUTION | PASS | Paid-up capital 648.02 L constant all periods, both statements (L134-135/202-203); no corporate action. Basic=Diluted EPS every period (S 22.27=22.27; C 23.13=23.13, L138-139/206-207) = no dilutive instruments outstanding. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Other equity annual-only: S 1,77,848.62 + 648.02 = 1,78,496.64 L; C 1,96,997.59 + 648.02 = 1,97,645.61 L (L136/204). Ties internally; consol excess (19,148.97 L) = subsidiary reserves + NCI. No third-party number (rating/slide) in this doc to reconcile against. |
| F12 SEGMENT FORENSICS | FINDING | A3-02. Segment liabilities fell sharply QoQ (Amines -36%, total -26%); ambiguous WC-unwind vs debt reduction; finance cost also down QoQ. |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Only 3 agenda items (L49,51,53-55): standalone results, consolidated results, took-note of review reports. No AR/AGM/record date/dividend/director appointment/capital-raising resolution (sweep L30-73). No Role-6 AR event to schedule this cycle. (Board-timing anomaly captured under F14/A3-03.) |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | A3-03 (signature timestamp predates board close) + A3-04 (redundant unquantified Other Matter para; partner name MYV vs MV). Cumulative governance data point. |
| F15 ENTITY LIST DIFFS | FINDING | A3-07. First-observation 2-entity baseline (parent + 1 subsidiary, no JV/associate); no prior list to diff. |
| F16 PRESENTATION-SPECIFIC | N.A. | Results filing; no investor presentation/deck in this document set. |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript in document set; no Notion monitoring checklist for this new-coverage ticker. |

Tally: PASS 9 (F1,F3,F4,F6,F7,F9,F10,F11,F13) | FINDING 6 (F2,F5,F8,F12,F14,F15) | N.A. 2 (F16,F17) = 17. No blanks. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

None. Notes 1-5 contain no dated or dateable management commitment (no capex, commissioning, approval-pending, or status-change language). Nothing to feed the Role 5 promise-vs-delivery tracker or FTTCP catalyst timeline from this filing.

---

## NOTES FOR A4 (question generation)

- FORWARD-SIGNAL A3-01 (F2): Subsidiary Balaji Speciality Chemicals turnaround — quantify what drove the ~16.5pp YoY PAT-share swing (volume, price, product mix, one-off), and whether it is sustainable into the commissioning/ramp window.
- AMBIGUOUS A3-02 (F12): Segment liabilities down 153.39 Cr QoQ with finance cost down — ask management: gross/net borrowings movement, working-capital days, and whether Q4FY26 was a year-end WC peak.
- AMBIGUOUS A3-03 (F14): Auditor standalone-review digital signature timestamped ~10 min before the Board concluded; consolidated cert timestamp illegible — a governance-hygiene question, and consider pulling the source-PDF certificate metadata before relying on the sequencing conclusion.

---

```yaml
stage: A3-forensics
company: "BALAMINES"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/balamines-q1fy27/work/forensics_results_balamines_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: FINDING
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F2", line: "126,188,191", classification: "FORWARD-SIGNAL", implication: "Sole subsidiary swung loss-share to profit-share YoY; consol-minus-standalone PAT gap moved -8.22% to +8.28% of standalone PAT (~16.5pp, >5pp); NCI -147.26L to +318.11L"}
  - {id: "A3-02", check: "F12", line: "261,264", classification: "AMBIGUOUS", implication: "Segment liabilities fell QoQ Amines -36% / total -26% (-153.39 Cr) with finance cost also down; WC unwind vs debt paydown - concall question"}
  - {id: "A3-03", check: "F14", line: "370-371,57", classification: "AMBIGUOUS", implication: "Standalone auditor digital-signature timestamp 17:25:29 predates Board close 5:35 P.M. by ~9.5 min; consolidated cert OCR-degraded (538 fragment) = indeterminable"}
  - {id: "A3-04", check: "F14", line: "417,372,433", classification: "NEUTRAL-FACT", implication: "Redundant unquantified consol Other Matter para 4 (subsidiary already in review scope per para 1); partner name MYV vs MV across reports"}
  - {id: "A3-05", check: "F8", line: "124,186", classification: "NEUTRAL-FACT", implication: "Earlier years' tax non-zero 48.51L both statements current qtr; ETR ~26% near statutory; deferred tax a charge not credit"}
  - {id: "A3-06", check: "F5", line: "356-361,417", classification: "NEUTRAL-FACT", implication: "First-observation baseline: unmodified opinion, no GC/EoM; non-standard consol Other Matter para recorded for future QoQ diff"}
  - {id: "A3-07", check: "F15", line: "301,398,417", classification: "NEUTRAL-FACT", implication: "First-observation entity baseline: parent + 1 subsidiary (Balaji Speciality Chemicals), no JV/associate; no prior list to diff"}
forward_signals: ["A3-01"]
ambiguous: ["A3-02", "A3-03"]
commitments: []
gate_a3: pass
blank_checks: []
```
