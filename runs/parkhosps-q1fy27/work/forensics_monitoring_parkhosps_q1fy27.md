# A3 FORENSIC NOTES — Park Medi World Limited (PARKHOSPS)
Doctype: monitoring (SEBI Reg 32(6) CRISIL Monitoring Agency Report on IPO proceeds utilization) | Quarter: Q1 FY27 (quarter ended June 30, 2026)
Source extract: /home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/extract_monitoring_parkhosps_q1fy27.txt (13 pages, 677 lines)
Ledger reconciled: 12/12 tables, all rows read at cited lines = 100%
Unit convention: Rs Millions (x0.1 -> Rs Crores). Prior-quarter extract: NONE (first monitoring report; deviation is cumulative-to-date, stands alone).

Doctype mapping applied (per task): F1 ZERO_STANDING -> unutilised/nil IPO objects; F6 forward-commitment -> stated deployment timelines / "expected by" dates per object; F7 hedge -> CRISIL caveats/scope carve-outs; F13 board-outcome -> N.A.; the delay/deviation table (Section 4(iv), Table 9) is the core finding. All balance-sheet / statement / concall checks that have no substrate in this document are marked N.A. with a one-line basis.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F1-01 | F1 | T6.3 / T8.1-8.3 | 413, 549-555 | "No proceeds utilized during the reported quarter" (413); deployment table Earnings/ROI "-" (549-555) | FORWARD-SIGNAL | Object 3 (medical equipment) dormant this quarter; Rs 648.32mn (64.83 Cr) IPO cash parked in Axis (72.32mn) + ICICI (576.00mn) monitoring accounts with zero disclosed earnings/yield. 4 of 5 objects showed Nil movement in Q1 FY27. Idle-capital drag until deployment; watch pace next quarter. |
| A3-F1-02 | F1 | T6.4 / T10.1 | 422, 601 | "Proceeds fully utilized as at the quarter ended March 31, 2026" (422); "Not applicable" (601) | AMBIGUOUS | Object 4, Rs 2,453.18mn (245.32 Cr) "unidentified inorganic acquisitions and general corporate purposes", reported FULLY UTILIZED by Mar-26, yet no acquisition target is named anywhere and Section 5 GCP-utilization detail is "Not applicable." How was 245 Cr of *unidentified* acquisition + GCP money deployed with no object-level breakdown? Transparency gap on capital allocation. -> A4 question. |
| A3-F6-01 | F6 | T9.1 / Note 2 | 580-592 | "there is a delay in the implementation schedule. The delay is primarily attributable to deferment in finalisation of equipment procurement, including commercial negotiations and alignment of delivery timelines. The Company intends to utilise the unspent proceeds in the subsequent period." | AMBIGUOUS | CORE FINDING. Object 3: FY26 schedule Rs 229.59mn (22.96 Cr) vs actual Rs 36.08mn (3.61 Cr) to date = ~84% shortfall vs FY26 milestone; Rs 238.51mn (23.85 Cr) of the Rs 274.59mn object still unutilised. Stated reason reads as procurement/timing delay, NOT a cost revision ("No revision" throughout T5) and NOT a named re-prioritisation. Conservative read: cannot rule out that Panchkula / Ambala (Blue Heavens) / Jaipur (Ratangiri) hospital commissioning is slipping, which would make this a demand/roadmap signal, not just procurement lag. -> A4 question. |
| A3-F6-02 | F6 | T6.2 / T7.2 | 400-406, 470-478 | "Proceeds utilized towards construction of a new hospital building in Rohtak. The utilization as in line with the prospectus" (403); "intends to deploy the amount of Net Proceeds allocated towards the construction of New Hospital by our Subsidiary, Park Medicity (NCR)" (474-477) | FORWARD-SIGNAL | Only active object this quarter: Rs 28.66mn deployed, Rs 195.19mn of Rs 605.00mn cumulative (32%), Rs 409.81mn (40.98 Cr) still to deploy into the Rohtak build. Live bed-roadmap object. NOTE for A4: the IPO-funded hospital is Rohtak (Park Medicity NCR); this is DISTINCT from the Notion monitorable Narela/Febris and Kanpur roadmap items, which are not IPO objects. Map Rohtak deployment pace to bed adds. |
| A3-F7-01 | F7 | T2.4 / T2.6 | 148-149, 159-163 | "The MA does not perform an audit and undertakes no independent verification of any information/ certifications/ statements it receives" (148-149); "These sections have not been reviewed by the MA, and the MA takes no responsibility for such comments of the issuer's Management/Board" (162-163) | CONFIRMATORY-NEGATIVE | The entire monitoring opinion rests on the Agiwal & Assocaites statutory-auditor certificate (dated Aug 1, 2026) plus a management undertaking; CRISIL performs no independent verification. Every "Comments of the Board of Directors" cell (incl. the "No Comments"/"Refer note 2" against the object-3 delay) is issuer-populated and MA-unreviewed. Assurance value is limited; treat the utilisation figures as management-certified, not independently audited. |
| A3-F14-01 | F14 | T1.5 / T2.7 / T12.6 | 168-170, 302 | "no UDIN disclosed anywhere" (ref T2.7, line 168-170); "M/s Agiwal & Assocaites, Chartered Accountants" (302) | NEUTRAL-FACT | Governance/drafting data points, individually immaterial: (i) MISSING_UDIN — no UDIN on the CRISIL signature block or referenced statutory-auditor certificate anywhere in 677 lines (NOT FOUND, not estimated); (ii) NO_TIMESTAMP — CRISIL cover letter (p3) and MA report (p4) carry no digital-signature timestamp, unlike the company letter (signed 2026.08.03 17:11:35); (iii) auditor firm name mis-spelled "Assocaites" (for "Associates") repeated 6x (302/359/439/536/568/601). Cumulative housekeeping/governance note. |

Cross-check on the "no deviation" headline: Section (a)/(b) at lines 141/143 state "(a) Deviation from the objects: Not applicable" and "(b) Range of Deviation: Not applicable." This is technically consistent with a Section 4(iv) delay because the money still flows to the *same* objects (no change of use, "No revision" throughout) — the deviation is purely deployment-pace, not re-prioritisation. Recorded here so A4 does not mistake the "Not applicable" headline for an absence of the object-3 shortfall.

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING (mapped: unutilised/nil IPO objects) | FINDING | Object 3 nil this quarter + Rs 648.32mn parked zero-yield (A3-F1-01); object 4 Rs 2,453.18mn "fully utilized" with no named use + GCP detail "N.A." (A3-F1-02). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Monitoring report carries no S-vs-C financial statements to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost-line financials for subsidiaries (Park Medicity NCR / Blue Heavens / Ratangiri) to compare; nothing to test. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters / PAT figures; no % of PAT to compute (limited-assurance point captured under F7). |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No going-concern/EoM paragraph; first monitoring report so no prior-quarter verbatim to diff. |
| F6 FORWARD-COMMITMENT (mapped: deployment timelines/"expected by") | FINDING | Object-3 delay/deviation with "intends to utilise the unspent proceeds in the subsequent period" (A3-F6-01, core); Rohtak deployment underway (A3-F6-02). See Commitment Register. |
| F7 HEDGE (mapped: CRISIL caveats/scope carve-outs) | FINDING | IMPORTANT_SCOPE_CARVEOUT quoted (A3-F7-01): MA does no audit/independent verification; Board-comment columns MA-unreviewed. |
| F8 TAX FORENSICS | N.A. | No tax expense, ETR, or deferred-tax lines in a monitoring report. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosures present. |
| F10 SHARE COUNT AND DILUTION | N.A. | No share count or EPS. OFS category noted (Rs 12.67mn, line 558) but no per-share/dilution data to test. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No Other Equity / paid-up / net-worth figures in document. |
| F12 SEGMENT FORENSICS | N.A. | No segment asset/liability tables; object-level utilisation covered under F1/F6. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Per doctype mapping. Report only "placed before and considered by the Board... August 03, 2026" (39-40); no AR/AGM/record-date/director-term event. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | MISSING_UDIN + NO_TIMESTAMP + auditor-name mis-spelling "Assocaites" (A3-F14-01). |
| F15 ENTITY LIST DIFFS | N.A. | No prior-quarter extract; first monitoring report, no consolidation-list diff possible. |
| F16 PRESENTATION DROPPED/REFRAMED | N.A. | Not a presentation deck; no prior deck to diff baselines/guidance against. |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a transcript; no F6-vs-transcript silence set to audit. |

Blank checks: none. GATE A3: PASS (17/17 marked, exactly one status each).

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Note/line ref | Status word |
|---|---|---|---|---|
| C1 | Repayment/prepayment of Company + Subsidiary borrowings, Rs 3,800.00mn — "intends to utilise the entire amount earmarked for this object during... Fiscal 2026" | Fiscal 2026 (met) | T7.1 / 456-467; T6.1 / 390-396 | completed ("Proceeds fully utilized as at the quarter ended March 31, 2026", 393) |
| C2 | Rohtak New Hospital debt-investment into Park Medicity (NCR), Rs 605.00mn — "intends to deploy the amount of Net Proceeds allocated towards the construction of New Hospital" | ongoing (no fixed date in doc) | T7.2 / 470-478; T6.2 / 400-406 | underway (Rs 195.19mn of 605.00mn = 32%; Rs 28.66mn this quarter; Rs 409.81mn remaining) |
| C3 | Medical equipment for Panchkula (Rs 184.59mn, Company) + Ambala/Jaipur (Rs 90.00mn, Blue Heavens/Ratangiri), Rs 274.59mn — "intends to utilise an estimated amount of Rs. 274.59 million... towards purchase of such new medical equipment" | Offer Doc: FY26 (MISSED) -> "the unspent proceeds in the subsequent period" / next fiscal year | T7.3 / 482-498; T9.1+Note 2 / 580-592 | initiated (Rs 36.08mn of 274.59mn = 13%; Rs 238.51mn unutilised; ~84% short of FY26 schedule) |
| C4 | Unidentified inorganic acquisitions + GCP, Rs 2,453.18mn — "proposes to deploy the balance Net Proceeds aggregating to Rs. 2,453.18 million towards unidentified inorganic acquisitions and general corporate purposes" | Mar-26 (reported met) | T7.4 / 507-531; T6.4 / 419-425 | completed-per-report ("Proceeds fully utilized as at the quarter ended March 31, 2026", 422) — but no target named; see A3-F1-02 |
| C5 (contingency) | Prospectus fallback — "In the event that the estimated utilization of the Net Proceeds in a scheduled fiscal year is not completely met... the same shall be utilised in the next fiscal year" | next fiscal year | 594-596 | underway (invoked for object 3) |

Hedge language noted for A4 (F7-adjacent, not a separate finding): object-4 acquisition narrative "The actual acquisition will depend on number of factors, including the timing, nature, geographical and strategical location, size of acquisitions..." (515-518) — standard optionality hedge on the inorganic-growth object.

---

## HANDOFF TO A4 (flagged findings)
- FORWARD-SIGNAL: A3-F1-01 (idle Rs 648.32mn / dormant objects), A3-F6-02 (Rohtak deployment pace vs bed roadmap).
- AMBIGUOUS -> convert to management questions: A3-F1-02 (how were Rs 2,453.18mn of unidentified-acquisition/GCP proceeds deployed with no named target and GCP detail "N.A."?), A3-F6-01 (is the equipment deferral pure procurement timing, or does it signal slippage in Panchkula/Ambala/Jaipur hospital commissioning?).
- Capital-allocation read for the thesis war-chest line: idle IPO proceeds Rs 648.32mn (64.83 Cr) confirm the undeployed-cash component; no cost revision or object change supports the "capex discipline" credit, but the object-3 pace and unnamed object-4 deployment are the two execution watch-items.

---

```yaml
stage: A3-forensics
company: "PARKHOSPS"
quarter: "Q1 FY27"
doctype: "monitoring"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/forensics_monitoring_parkhosps_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1-01", check: "F1", line: "413,549-555", classification: "FORWARD-SIGNAL", implication: "Object 3 nil this quarter; Rs 648.32mn IPO cash parked zero-yield in Axis+ICICI; 4 of 5 objects dormant in Q1 FY27"}
  - {id: "A3-F1-02", check: "F1", line: "422,601", classification: "AMBIGUOUS", implication: "Rs 2,453.18mn unidentified-acquisition/GCP object reported fully utilized by Mar-26 with no target named and Section 5 GCP detail 'Not applicable' — deployment transparency gap"}
  - {id: "A3-F6-01", check: "F6", line: "580-592", classification: "AMBIGUOUS", implication: "Object 3 medical equipment ~84% short of FY26 schedule (Rs 36.08mn vs Rs 229.59mn); reason stated as procurement deferment; cannot rule out Panchkula/Ambala/Jaipur commissioning slippage"}
  - {id: "A3-F6-02", check: "F6", line: "400-406,470-478", classification: "FORWARD-SIGNAL", implication: "Rohtak (Park Medicity NCR) only active object; Rs 195.19mn of 605.00mn deployed (32%), Rs 409.81mn remaining; bed-roadmap-relevant but distinct from Narela/Febris/Kanpur"}
  - {id: "A3-F7-01", check: "F7", line: "148-149,159-163", classification: "CONFIRMATORY-NEGATIVE", implication: "MA performs no audit/independent verification; opinion rests on Agiwal & Assocaites certificate + management undertaking; Board-comment cells MA-unreviewed — assurance value limited"}
  - {id: "A3-F14-01", check: "F14", line: "168-170,302", classification: "NEUTRAL-FACT", implication: "MISSING_UDIN + NO_TIMESTAMP on CRISIL signature vs timestamped company letter + auditor name mis-spelled 'Assocaites' 6x — cumulative governance/drafting data point"}
forward_signals: ["A3-F1-01", "A3-F6-02"]
ambiguous: ["A3-F1-02", "A3-F6-01"]
commitments:
  - {commitment: "Repayment/prepayment of Company+Subsidiary borrowings Rs 3,800.00mn", implied_date: "Fiscal 2026", ref: "L456-467/L393", status_word: "completed"}
  - {commitment: "Rohtak New Hospital debt-investment into Park Medicity NCR, Rs 605.00mn", implied_date: "ongoing (no fixed date)", ref: "L470-478/L400-406", status_word: "underway"}
  - {commitment: "Medical equipment Panchkula+Ambala+Jaipur, Rs 274.59mn", implied_date: "FY26 missed -> subsequent/next fiscal", ref: "L482-498/L580-592", status_word: "initiated"}
  - {commitment: "Unidentified inorganic acquisitions + GCP, Rs 2,453.18mn", implied_date: "Mar-26 (reported met)", ref: "L507-531/L419-425", status_word: "completed"}
  - {commitment: "Prospectus contingency: unmet fiscal-year utilisation carries to next fiscal year", implied_date: "next fiscal year", ref: "L594-596", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
