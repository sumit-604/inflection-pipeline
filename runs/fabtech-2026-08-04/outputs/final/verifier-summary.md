# Verifier summary — Phase 1

Scope: Verifier A (numerical), Verifier B (red flag coverage), Verifier D (peers), and the Gate 0 plus Emerging Moat portion of Verifier C (framework). Valuation framework audit is PENDING PHASE 3.

## Phase 1 confidence delta

| Component | Score | Verifier |
|---|---|---|
| numerical_acceptance | 93 | A (strict numerical accuracy 14/15; headline acceptance_rate 53 counts interpretation and disclosure catches, not numerical errors; 0 source-fidelity mismatches; REWORK gate not triggered) |
| redflag_coverage | 68 | B (13/19 fully caught, 2 partial; graded strong; no CRITICAL) |
| framework_adherence | 97 | C (Gate 0 46/46 rules pass; Emerging Moat 2 MINOR; valuation PENDING PHASE 3) |
| peer_utilisation | 83 | D (10 of 12 provided peers used substantively; acceptance_rate 92) |
| overall | 68 | minimum of the four available components |

## Findings, sorted by severity

| # | Severity | Verifier | Location anchor | Finding |
|---|---|---|---|---|
| 1 | CRITICAL | A | B01 / B03 Phase 2; AR consol p.149 vs p.174 | FY26 consolidated trade receivables Rs 241.52 Cr on balance sheet vs Rs 204.34 Cr in Note 13; Rs 37.18 Cr (18.2%) unreconciled on the auditor's sole KAM. Source internal inconsistency within the AR, correctly reported by the stages; not a fabrication or misread. |
| 2 | CRITICAL | A | B02 finding #2 / B03 Phase 1B; AR consol p.139-140 | Auditor KAM: receivables overdue >365 days Rs 58.9 Cr (27.4% of gross receivables). Number matches source exactly; the finding is management non address across three concalls, not a numerical error. |
| 3 | MAJOR | A | B02 finding #1 / B03 Phase 2; AR p.115 vs p.133-134 | Rs 19.71 Cr freehold land acquired from related party (agreement 2024-11-06) disclosed in Note 5 but absent from the Note 47 RPT table. Figure correct; issue is disclosure incompleteness. |
| 4 | MAJOR | A | B02 finding #4; Note 13(b) AR p.118 and consol p.174 | ECL provision matrix rate curves changed materially YoY with no disclosed rationale. Figures stated correctly; the catch is the missing Ind AS 109 explanation. |
| 5 | MAJOR | A | B02 finding #5; Note 37 standalone p.124, Note 39 consol p.182 | Provision for doubtful debts jumped to Rs 530.21 Lakh standalone / Rs 544.54 Lakh consol in FY26 from nil / Rs 7.74 Lakh. Verified exactly; material earnings quality jump in the IPO year. |
| 6 | MAJOR | A | B05; Q4 FY26 call | FY26 revenue guidance Rs 380-400 Cr vs delivery stated as total income Rs 431.33 Cr; on operating revenue basis Rs 410.77 Cr sits above the upper end. Unit/basis ambiguity, not confirmable without verbatim Q3 text. |
| 7 | MAJOR | B | B05 red_flags / Section 2D omission; Apr-2026 call p.17, p.3 | Other income ~Rs 21 Cr (~12 Cr forex + ~7 Cr IPO FD interest) is ~55% of FY26 reported PAT Rs 38.36 Cr; earnings quality dependence not flagged upstream. |
| 8 | MAJOR | B | B05 triggers #1 / red_flags omission; Feb p.6, Apr p.10, Aug p.3 | Hot lead pipeline figure unstable and re-labelled: ~$455M -> ~$200M -> ~Rs 3,800 Cr within a new Rs 9,300 Cr funnel, against flat ~Rs 900-926 Cr order book; not flagged. |
| 9 | MAJOR | B | B05 red_flag #3 / repeated_evasions under-weighted; Feb p.11, p.18 | Revenue timing discretion (holds/releases shipments to time revenue) is an earnings smoothing lever, framed by B05 only as quarter lumpiness. |
| 10 | MAJOR | D | 06-peers.md Part 5 | FABRICATED claim that Anup shifted away from 100% fixed price terms; contradicted by Anup's own Feb-2026 and May-2026 transcripts. Must not carry forward. The six formal claim verdicts (Q1-Q6) are unaffected and valid. |
| 11 | MEDIUM | A | B05 / B01 | FY26 EBITDA Rs 55.56 Cr vs B01 computed ~Rs 55.96 Cr (Rs 40 Lakh rounding variance, <0.1%); YoY growth rate leans on the RHP prior year figure. |
| 12 | MEDIUM | A | B05 | FY27 growth guidance 30-40% -> ~25% -> 20-25% across three calls, all cited verbatim; the finding is the recalibration pattern, not a numerical error. |
| 13 | MEDIUM | A | B09 | Management TAM claim $30bn + $70bn/10yr accurately cited from transcript but unattributed and untriangulated; B09 diagnoses TAM/SAM conflation. No downstream valuation impact. |
| 14 | MINOR | A | B02 finding #7; Note 35 standalone p.124 | Finance costs +122.8% YoY, lease interest +753%; verified exactly. Composition finding. |
| 15 | MINOR | A | B02 finding #15; Note 47 standalone p.133 | Trademark fee to related party ceased FY26; new corporate guarantee expenses Rs 42.76 Lakh first appear FY26; verified exactly. Pattern concern. |
| 16 | MINOR | A | B01 | ROCE 29.32% -> 11.25%, ROE 24.43% -> 12.94%; interpretation as post IPO cash denominator rebase mechanically correct, not a deterioration in EBIT/profit. |
| 17 | MINOR | B | B05 / B11 handoff; Nov p.12, Apr p.5/p.7, Aug p.3 | Asset light narrative contradicts Rs 24 Cr+ subsidiary deployment, IPO funded M&A and admitted persistent negative operating cash flow; contradiction not surfaced. |
| 18 | MINOR | B | B05 scope; Nov-2025 p.3, p.4, p.11, p.14-15 | Q2 FY26 call excluded by the 3 quarter contract; strongest guidance refusal baseline, 22 vs 62 countries in-call contradiction and factual sloppiness uncaught; corroborates the HIGH guidance flag. |
| 19 | MINOR | B | B05 triggers #4 / Section 3D | Project cycle and ticket size figures wobble across calls; ticket size treated as a validated positive trigger without flagging the inconsistency. |
| 20 | MINOR | C | B07 Section 5 scorecard + 4C | E1 (4.0) and R1 (3.0) both score off the same SACE / Vision 2030 development, ~36% of the 19.2 total; permitted and disclosed, MODEST unchanged. |
| 21 | MINOR | C | B07 Section 5 scorecard | B1 (+1.0) and F2 (+0.7) are negative signal categories carrying the LL=1 floor rather than 0; conservative direction, MODEST unchanged if removed. |
| 22 | MINOR | D | 06-peers.md Part 2A | Ion Exchange ~Rs 9,011 Cr bid pipeline cited in prose as Feb-2026/Q3 FY26; actual quote is Nov-2025/Q2 FY26. Underlying coverage map is correct; only the prose citation is quarter mislabeled. |

Severity roll up: 2 CRITICAL (both A, both source internal / concall silence, correctly surfaced), 10 MAJOR, 8 MINOR, plus 3 MEDIUM from A. No CRITICAL is a fabricated or misread stage figure; no source-fidelity mismatch; REWORK gate not triggered.
