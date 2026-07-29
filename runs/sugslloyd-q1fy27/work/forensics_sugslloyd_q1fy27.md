# A3 FORENSIC NOTES — SUGS LLOYD LIMITED (SUGSLLOYD) — Q1 FY27 (quarter ended 30 June 2026) — DOCTYPE: RESULTS

Source extract: `extract_results_sugslloyd_q1fy27.txt` (418 lines, 6 pages).
Ledger reconciled: 100% (all 70 line-items, 15 zero-standing, 14 notes, 12 auditor paras, 5 signature blocks, 2 entities, 1 agenda item read at their cited lines).
Doctype applicability: F1–F15 apply; F16 (presentation) and F17 (concall) are N.A. on a results filing. Prior-quarter ledger: none (first quarterly review for this recently listed SME). Notion monitoring checklist: none (first review) — the F17 silence audit is therefore N.A. with that reason stated; no tripwires invented.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|----------------------|
| A3-01 | F4 | Consol §5 row 26 (assoc share); §10 assoc revenue/profit; Consol auditor §9 para 6a | 261; 376-379 | "4.03 10.56 051  12:71" (share of assoc, line 261); "total revenue of Rs.521.31 ... total net profit of Rs.19.21 Lakhs" (line 376-379) | FORWARD-SIGNAL | Associate (unaudited-by-principal, other-auditor-reviewed) share of profit jumped 0.51 (Q1FY26) → 4.03 (Q1FY27), ~690% YoY. Contribution is only 0.53% of consolidated PAT (well under the 10% threshold — no level breach), but the YoY jump is a separate FINDING per F4. Associate stands alone at Rs 521.31L revenue / Rs 19.21L net profit for the quarter. A4: probe stake %, ramp drivers, and any expected stake/relationship change. |
| A3-02 | F8 | Standalone §4 row 21 / Consol §5 row 21 | 99-100; 251-252 | "(c)| Current Tax Expense Relating to Prior years ... 0.08" | NEUTRAL-FACT | "Tax relating to earlier years" non-zero (Rs 0.08L) in the FY26 audited column only; nil in all three quarters. Immaterial (Rs ~8,000) but logged per the F8 non-zero rule. No ETR distortion. |
| A3-03 | F10 | Standalone §4 rows 30, 34; Consol §5 rows 30, 34; note 5 | 109; 113; 267; 128 | "Paid-up equity share capital 2,321.40 2,321.40 1,625.00 2,321.40" (line 109); "Basic earnings ... 3.41 5:33 3.56 14.19" (line 113) | FORWARD-SIGNAL | Paid-up capital rose 1,625.00 (Q1FY26) → 2,321.40 (Q4FY26 onward), a Rs 696.40L / 69.64L-share fresh issue = the SME IPO of this recently listed scrip. Basic = diluted in every period (no dilutive instruments). Consequence: standalone EPS FELL YoY 3.56 → 3.41 (consol 3.56 → 3.43) even though standalone PAT ROSE +29.7% (578.60 → 750.26), because of the enlarged post-IPO weighted-average share base (note 5, line 128). YoY EPS comps stay distorted until the IPO anniversary laps. |
| A3-04 | F14 | Consol auditor §9 paras 6a/6b; sig blocks §3 items 2,4,5; cross-table deltas §4 rows 9,11 vs §5 rows 9,11 | 374, 401; 191-197, 409; 87 vs 230, 89 vs 234 | "6. We did not review ..." (line 374) and "6.The comparative figures ..." (line 401); standalone sig block (lines 191-197) carries no Firm Reg. No., consol block "Firm Reg. No. 108696W/W101028" (line 409) | NEUTRAL-FACT | Cumulative documentation-quality data point (each item immaterial): (a) consolidated auditor report numbers two distinct Other-Matter paras both "6." (lines 374, 401) instead of 6./7.; (b) Firm Reg. No. present in the consolidated sign-off (409) but absent from the standalone sign-off (191-197); (c) partner's personal name absent from both sign-offs (191-197, 407-414); (d) one-paisa cross-table deltas — Finance Costs Q1FY26 148.47 standalone (87) vs 148.48 consol (230), Other Expenses 1,050.91 (89) vs 1,050.90 (234) — total expenses still tie, so OCR/rounding not a real reconciliation break, logged as extraction-integrity. |
| A3-05 | F15 | Consol auditor §9 para 6a; entity list §10 row 2 | 374-377; 319-320 | "Vyna Electric Private Limited (Formerly as Levana Infra Private Limited)" | AMBIGUOUS | The sole non-parent entity (the equity-method associate) is disclosed under a new name, former name "Levana Infra Private Limited." Rename spans "Infra" → "Electric," hinting at a business repurposing; reason and effective quarter undisclosed and no prior ledger exists to date it. A4: ask what the rename reflects (change of control, line of business, or cosmetic), and whether it alters Sugs's associate exposure. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING ITEMS | PASS | All 15 zero-standing rows are standard SEBI-template placeholders (cost of materials consumed, exceptional, extraordinary, discontinued-ops trio, minority interest); "Cost of materials consumed" nil against large "Purchases of stock-in-trade" (lines 83/84) simply confirms a trading/EPC model; standalone "Share of Assoc" (105) legitimately dash while consolidated (261) is populated. No anomaly. |
| F2 STANDALONE vs CONSOLIDATED DECOMP | PASS | Revenue/expenses identical S vs C (equity-method associate, no line-by-line consol); PAT gap is entirely the associate share — 4.03/10.56/0.51/12.71 = 0.54%/0.98%/0.09%/0.44% of standalone PAT. Widest QoQ move ~0.9pp, far under the 5pp FINDING threshold. Gap decomposition clean; associate-ramp signal carried under F4. |
| F3 SHELL-ENTITY DETECTION | N.A. | No line-by-line consolidated subsidiary exists; the only non-parent entity is an equity-method associate, so identical S-vs-C cost lines are the expected artifact of equity accounting, not shell evidence. Associate is demonstrably operating (revenue Rs 521.31L, line 376). No Going Concern EoM to reconcile. |
| F4 UNAUDITED CONTRIBUTION RATIO | FINDING (A3-01) | Associate share reviewed by other auditors / furnished by Management (para 6a, line 380-384). Level = 0.53% of consol PAT (< 10%), but YoY jump 0.51 → 4.03 is a separate FINDING per F4. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No Going Concern paragraph in either report (ledger §8/§9 confirm; lines 189, 206). Other-Matter paras present but this is the first quarterly review — no prior paragraph to verbatim-diff for scope change. |
| F6 FORWARD-COMMITMENT PHRASE MINING | PASS | Notes swept for the full lexicon. Only hits are result-approval language ("Board has approved," line 45; "approved by the Board of Directors," lines 117/278) — approval of the results themselves, not a future-dated deliverable. No "expected to," "will be," "underway," "commenc," "proposes to," "intends to." Commitment register empty. |
| F7 HEDGE PHRASE MINING | PASS | No hedge lexicon in the notes. Segment note (125/287) is a factual single-segment statement, not a newly-added lumpiness/concentration hedge. Audit-reliance wording ("solely on report of other auditor," line 384) is captured under F4, not a note-level hedge. |
| F8 TAX FORENSICS | FINDING (A3-02) | ETR 26.7%/25.6%/25.6%/25.8% — all near statutory 25.17%, no shield. Deferred tax tiny (credits 1.79/2.80L recent; immaterial DTA). "Tax relating to earlier years" non-zero (0.08L, FY26 column) triggers the F8 non-zero rule. |
| F9 OCI FORENSICS | N.A. | No Other Comprehensive Income section presented; AS-basis SME filing (Ind-AS-exempt per note 4, lines 126/289). No actuarial line to trend. |
| F10 SHARE COUNT AND DILUTION | FINDING (A3-03) | Paid-up capital step-up 1,625.00 → 2,321.40 traces to the SME IPO fresh issue; basic = diluted (no overhang); EPS fell YoY while PAT rose (enlarged share base). |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | Quarterly results carry only paid-up capital (line 109/267); no Other Equity / reserves line and no balance sheet in this format; no third-party net-worth figure in context to reconcile. |
| F12 SEGMENT FORENSICS | N.A. | Single-segment company per note 3 (lines 125/287): "Company is in only one segment, hence Segment Reporting as per AS-17 is not applicable." No segment asset/liability disclosure exists. |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Single-item board meeting — only the Q1FY27 results approved (lines 42-48). Ledger §1 grep swept for AGM/dividend/director/auditor/ESOP/capital-raise and returned zero hits. Nothing beyond the results to schedule. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING (A3-04) | Duplicate "6." para numbering, asymmetric firm-reg / partner-name capture, one-paisa cross-table deltas — cumulative documentation-quality data point. |
| F15 ENTITY LIST DIFFS | FINDING (A3-05) | Associate rename "Levana Infra Private Limited" → "Vyna Electric Private Limited" disclosed in-report (lines 374-377). |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is results, not a presentation deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is results, not a concall transcript; and no Notion monitoring checklist exists (first quarterly review). No commitments/checklist items to audit for silence. |

Blank checks: none. GATE A3: pass (every check carries exactly one status).

---

## COMMITMENT REGISTER (from F6)

None. No forward-dated management commitment appears in the notes or board-outcome letter. The only lexicon hits ("Board has approved," line 45; "approved by the Board of Directors ... meetings held on July 29, 2026," lines 117/278) are approvals of the results being filed, not promises of a future deliverable, so no dateable commitment enters the Role 5 promise-vs-delivery tracker this quarter.

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| (none) | — | — | — |

---

## NOTES FOR A4 (question generation)

- FORWARD-SIGNAL A3-01 (F4): associate ramp — stake %, revenue/profit drivers, expected relationship change.
- FORWARD-SIGNAL A3-03 (F10): flag the IPO-driven EPS-comp distortion as an analytical adjustment; not necessarily a management question, but YoY EPS should be read against the enlarged weighted-average base until the IPO anniversary laps.
- AMBIGUOUS A3-05 (F15): associate rename Levana Infra → Vyna Electric — ask what the rename reflects and whether it changes Sugs's exposure.
- Extraction-integrity caveats (do not assert false precision): OCR comma/colon-for-period at lines 80, 113, 219, 261, 270; one-paisa cross-table deltas at 87 vs 230 and 89 vs 234; standalone sign-off missing name/designation and firm-reg (lines 132-134, 191-197).

```yaml
stage: A3-forensics
company: "SUGSLLOYD"
quarter: "Q1 FY27 (quarter ended 30 June 2026)"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sugslloyd-q1fy27/work/forensics_sugslloyd_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: PASS
  F3: N.A.
  F4: FINDING
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F4", line: "261;376-379", classification: "FORWARD-SIGNAL", implication: "Associate (other-auditor-reviewed) share of profit up 0.51->4.03 YoY (~690%); 0.53% of consol PAT, under 10% level but YoY jump = finding; probe stake and ramp drivers"}
  - {id: "A3-02", check: "F8", line: "99-100;251-252", classification: "NEUTRAL-FACT", implication: "Tax relating to earlier years non-zero (Rs 0.08L) in FY26 column only; immaterial, logged per rule"}
  - {id: "A3-03", check: "F10", line: "109;113;267", classification: "FORWARD-SIGNAL", implication: "SME IPO fresh issue 1625.00->2321.40 paid-up; basic=diluted; EPS fell YoY 3.56->3.41 while PAT +29.7%, comps distorted until IPO anniversary laps"}
  - {id: "A3-04", check: "F14", line: "374;401;191-197;409", classification: "NEUTRAL-FACT", implication: "Duplicate 6. para numbering, firm-reg present consol/absent standalone, no partner name, one-paisa cross-table deltas; cumulative documentation-quality signal"}
  - {id: "A3-05", check: "F15", line: "374-377;319-320", classification: "AMBIGUOUS", implication: "Associate renamed Levana Infra Private Limited -> Vyna Electric Private Limited; Infra->Electric hints at repurposing; reason/effective date undisclosed"}
forward_signals: ["A3-01", "A3-03"]
ambiguous: ["A3-05"]
commitments: []
gate_a3: pass
blank_checks: []
```
