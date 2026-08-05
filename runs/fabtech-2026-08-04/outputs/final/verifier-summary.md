# Verifier Summary — Fabtech Technologies Ltd (FABTECH) | Run 2026-08-04

## Confidence delta and acceptance rates

| Component | Score | Acceptance basis |
|---|---|---|
| numerical_acceptance (B12a) | 93 | strict numerical accuracy 14/15; headline acceptance_rate 53 counts interpretation/disclosure catches; 0 source-fidelity mismatches |
| redflag_coverage (B12b) | 68 | 13/19 fully caught, 2 partial; acceptance_rate 68; graded strong; no CRITICAL |
| framework_adherence (B12c) | 96 | Gate0+EM 97 (46/46 gate0 pass, 2 EM MINOR), valuation 96 (45 rules, 4 MINOR) |
| peer_utilisation (B12d) | 83 | acceptance_rate 92; 10 of 12 provided peers used substantively |
| overall | 68 | minimum of the four, redflag bound; band 60-74 |

REWORK not triggered: no B12a CRITICAL is a fabricated or materially misread stage figure; 0 source-fidelity mismatches; no acceptance rate below the 60 percent hard floor on its correct denominator; overall 68 is in the one level downgrade band, not the forced REWORK band below 60.

## Findings sorted by severity

### CRITICAL

| Verifier | Location | Finding |
|---|---|---|
| B12a | B01-gate0 / B03-ardeep Phase 2; AR consol p.149 vs p.174 | FY26 consolidated trade receivables Rs 241.52 Cr on the balance sheet vs Rs 204.34 Cr in Note 13, a Rs 37.18 Cr (18.2%) unreconciled gap on the auditor's sole KAM. Source-internal inconsistency within the AR; stage correctly reported both figures. source_fidelity true, is_mismatch false. Live monitorable. |
| B12a | B02-notes #2 / B03-ardeep Phase 1B; AR consol p.139-140, Note 13(a) p.174 | Auditor KAM: trade receivables >365 days overdue Rs 58.9 Cr (Rs 5,887.55 Lakh consol / Rs 5,854.04 Lakh standalone), 27.4% of gross receivables. Number matches exactly; the finding is management non-address across three concalls, not a numerical error. source_fidelity true, is_mismatch false. |

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| B12a | B02-notes #1 / B03 Phase 2; Note 5 AR std p.115, Note 47 p.133-134 | Rs 19.71 Cr freehold land acquired from related party Fabtech Technologies International Pvt Ltd, in Note 5 but absent from the RPT note. Figure correct; issue is disclosure incompleteness, not a numerical error. |
| B12a | B02-notes #4 / B03 Phase 2; Note 13(b) std p.118, consol p.174 | ECL provision matrix rate curves changed YoY with no disclosed rationale. Numbers stated correctly; MAJOR is the absence of Ind AS 109 rationale. |
| B12a | B02-notes #5 / B03 Phase 2; Note 37 std p.124, Note 39 consol p.182 | Provision for doubtful debts jumped standalone nil to Rs 530.21 Lakh, consolidated Rs 7.74 Lakh to Rs 544.54 Lakh, in the IPO year. Figures verified exactly. |
| B12a | B05-concall; Q4 FY26 call | FY26 revenue guidance Rs 380-400 Cr vs delivered Rs 431.33 Cr total income: revenue-vs-total-income basis ambiguity. On operating revenue Rs 410.77 Cr the actual sits above the upper end; without verbatim Q3 text the basis cannot be independently confirmed. |
| B12b | B05 red_flags / Section 2D omission; Apr call Karan p17 | Non-operating other income ~Rs 21 Cr (~12 Cr forex + ~7 Cr IPO-FD interest) is ~55% of FY26 reported PAT Rs 38.36 Cr; earnings-quality dependence never flagged. Carried into synthesis. |
| B12b | B05 triggers #1 / red_flags omission; Feb p6, Apr p10, Aug p3 | Hot-lead pipeline figure definitionally unstable ($455M Feb, $200M Apr, Rs 3,800 Cr Aug within a new Rs 9,300 Cr funnel) against flat ~Rs 900-926 Cr order book; not flagged. |
| B12b | B05 red_flag #3 / repeated_evasions under-weighted; Feb p11, p18 | Revenue-timing discretion: management holds/releases shipments to time revenue, an earnings-smoothing lever, framed by B05 only as quarter lumpiness. |
| B12d | 06-peers.md Part 5 (Cross-Peer Hypothesis) | B06 claim that "Anup shifted away from 100% fixed-price terms" is FABRICATED, contradicted by Anup's own Feb 2026 and May 2026 transcripts. Does not affect the six formal Q1-Q6 claim verdicts. MUST NOT carry into synthesis. Removed. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| B12a | B02-notes #7; Note 35 std p.124 | Finance costs +122.8% YoY, lease interest +753%. Verified exactly; composition finding. |
| B12a | B02-notes #15; Note 47 std p.133 | Trademark licence fee to related party ceased FY26 after Rs 23.22 Lakh; corporate guarantee expenses Rs 42.76 Lakh first appear. Verified; pattern concern. |
| B12a | B01-gate0 | ROCE 29.32% to 11.25% and ROE 24.43% to 12.94% FY23 to FY26, attributed to post-IPO cash rebase. Verified; interpretation mechanically correct (denominator inflation). |
| B12b | B05/B11 handoff interpretation gap; Nov p12, Apr p5/p7, Aug p3 | "Asset-light/not capital-intensive" claim contradicts Rs 24 Cr+ subsidiary deployment, IPO-funded M&A and persistent negative operating cash flow; contradiction not surfaced. |
| B12b | B05 scope, Nov-2025 excluded; Nov p3, p4, p11, p14-15 | Q2 FY26 call excluded by the 3-quarter contract; strongest guidance-refusal baseline, 22-vs-62-countries in-call contradiction and factual sloppiness uncaught; corroborates the existing HIGH guidance flag. |
| B12b | B05 triggers #4 / Section 3D interpretation gap | Project-cycle and ticket-size figures wobble across calls; B05 treats ticket size as a validated positive trigger without flagging the inconsistency. |
| B12c | B07 Section 5 scorecard + 4C | E1 (4.0) and R1 (3.0) both scored off the same SACE/Vision 2030 development, ~36% of the 19.2 total; permitted and disclosed, MODEST unchanged. |
| B12c | B07 Section 5 scorecard | B1 (+1.0) and F2 (+0.7) carry the LL=1 negative-signal floor rather than 0; conservative direction, MODEST unchanged. |
| B12c | B11 Section 4A/4E | Entry computed off operative 13x rather than the conservative RRM track; superseded by documented operator override, RRM floor Rs 50.3 retained; no decision impact. |
| B12c | B14 YAML position_size | position_size "Small" is the hypothetical in-zone ceiling while action is None at CMP; prose explicit; no decision impact. |
| B12d | 06-peers.md Part 2 (2A) | Ion Exchange ~Rs 9,011 Cr bid pipeline prose-cited to Feb 2026/Q3 FY26 call but the quote is in the Nov 2025/Q2 FY26 call; the yaml coverage_map attributes it correctly, so only the prose citation is quarter-mislabeled. |

## Verifier B12b spot checks

Promise-delivery spot checks: 5 checked, 5 confirmed, 0 wrong. Credibility grade C concurred; the added earnings-quality, pipeline-volatility and revenue-timing findings reinforce C, do not move it.
