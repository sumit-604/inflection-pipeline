# ASTRAMICRO (Astra Microwave Products Ltd): verifier summary, Phase 1, run 2026-11-15

## Phase 1 confidence delta

| Component | Value | Source | Basis |
|---|---|---|---|
| numerical_acceptance | 97.3 | B12a | 692 numbers checked; mandatory 234 of 234 |
| redflag_coverage | 91.7 | B12b | material 12, caught 11 (7 caught + 4 partially caught); caught only 7/12 = 58.3, reported by the verifier, not applied |
| framework_adherence (phase 1 portion) | 87.0 | B12c | Gate 0 + Emerging Moat: 40 of 46 rules |
| framework_adherence (valuation component) | PENDING PHASE 3 | B12c | Verifier C audit of B10, B11 not run; expectation ledger and recomputed destination PE pending |
| peer_utilisation | NOT APPLICABLE | B12d | denominator below 4: 2 of 2 peers used substantively (8 of 8 transcripts); PARAS has no transcripts and was not scored |
| overall | 87.0 | confidence.yaml | set by framework_adherence phase 1 portion; band 75 to 89 |

Acceptance rates: A 97.3 | B 91.7 | C phase 1 87.0 | D 100 (on 2 peers, reported as a count, not used in overall).
REWORK test: Verifier A confirmed CRITICAL 0; no rate below 60 on a denominator of 4 or more; rework false.
Verifier A identity check: B12a carries 0 CRITICAL rows, so no row needed the claimed against source_truth identity test. Verifier A struck 5 false positives before reporting.
Verifier runs this Phase 1: A 1, B 1, C 1, D 1 (manifest). Remediation cycles: 0.

Counts by verifier:

| Verifier | Scope | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|
| A (numerical, B12a) | all stage reports; 692 numbers | 0 | 1 | 6 |
| B (red flags, B12b) | concall and peer stages | 0 | 4 | 10 |
| C (framework, B12c, phase 1 portion) | Gate 0 (21 rules) and Emerging Moat (25 rules) | 0 | 1 | 5 |
| D (peers, B12d) | 2 peers, 9 peer questions | 0 | 0 | 0 |

## CRITICAL

None. No verifier logged a CRITICAL finding.

## MAJOR

| # | Verifier | ID / status | Location anchor | Note (as the verifier wrote it) |
|---|---|---|---|---|
| 1 | A | source_fidelity: false | 04-bizmodel.md, "Findings on the four first-verification priorities" item 3 (HAL order value reconciliation) | Claimed: deck Rs 1,878.8 Cr x 1.18 = Rs 2,216.98 Cr, "the two differ by about 1.2%" against AR Rs 2,205.23 Cr incl. taxes. Source truth: AR p.28 prints Rs 2,205.23 Cr (text lines 1868-1872 and 1925); both inputs are right; recomputed gap 2,216.98 vs 2,205.23 = 11.75 = 0.53%; equivalently 2,205.23 / 1.18 = 1,868.8 vs deck 1,878.8 = 0.54%. Arithmetic slip on two correctly anchored inputs; the true gap is close to rounding, which weakens the "not reconciled" framing carried into FLAG-CONC and the analyst note. No verdict-card or Section 1B input affected. |
| 2 | B | MISSED | B05 (no entry); Q3 FY26 call (13 Feb 2026), Atim Kabra, PDF p.7; also p.6 ("seem scary high") | Management's own admission that part of reported inventory is legacy stock accumulated over about three decades, not tied to current production, with obsolescence risk, is absent; it changes how the H1 FY27 inventory build (B05 FLAG-CASH) reads. |
| 3 | B | PARTIALLY CAUGHT | B05 1B, guidance YAML "Order intake over 3-4 years", 3D; Q3 FY26 Atim p.8; Q1 FY27 Atim p.7, SGR p.3 | Order-book goalpost redefinition missed: Feb "new order booking over 4 years" became "over 5 years" with the full current book (pre-commitment Rs 2,156 Cr backlog, tax-inclusive Uttam, an expected QRSAM portion) counted "in the bag"; B05 caught the GST part only and treats the two commitments as like for like. |
| 4 | B | PARTIALLY CAUGHT | B05 FLAG-DISCLOSURE, 2D; Q1 FY27 Atim p.6 | 18-month senior churn volunteered on the Q1 FY27 call (new CTO, HR, quality, purchase, R&D domain and sales heads; "replacements for folks who have moved on") missed; MD exit caught. |
| 5 | B | PARTIALLY CAUGHT | B05 trigger 7, 1C, FLAG-NUMBERS; Q1 FY27 mgmt p.19; Q4 FY26 mgmt p.12, MVR p.5 | Turnover multiples sit on a combined base that includes the space-weather segment being demerged while the order build is "mostly defense"; management gave both readings in one answer; not flagged. |
| 6 | C | C-P1-01 (rule E08, prompts/07 l.171-172) | 07-emoat.md l.417, l.418, l.431, l.438 (stage 07) | Claimed A3 0, A4 0, G2 0; em_score 16.5. Recomputed A3 1.0 (A3-1 DOC automation), A4 0.7 (A4-2 CLAIM modular), G2 1.0 (G2-1 DOC WC days 459 to 374); em_score 19.2, range 18.7-19.2. Band MODEST unchanged; active_categories unchanged; B2+H2 downside case 13.2 not 10.5, so the analyst_note fragility statement fails; gap to STRENGTHENING 5.8 not 8.5. Stage 07 not re-run. |

Emerging Moat score, side by side: stage 16.5; Verifier C recomputed 19.2. Band MODEST under both.

## MINOR

| # | Verifier | ID / status | Location anchor | Note (as the verifier wrote it) |
|---|---|---|---|---|
| 1 | A | source_fidelity: true | 05-concall.md, anchors for the Q1 FY27 call (Concall_Aug_2026) and Q4 FY26 call (Concall_Jun_2026) in the priority table, 1A, 2A and the YAML (guidance, promise_delivery) | Each value is in the transcript one page later on the PDF marker: 1,350 at PDF p.4 (line 128); 182, 836, 360 at PDF p.4 (lines 148-152); Uttam Phase 1 at PDF p.10 (lines 383-384); 1,870 at PDF p.7 (line 246); "delay from our side" at PDF p.18 (line 702); 1,057 at PDF p.19 (line 745); Q4 call 1,157 / 530 / 2,141 / 490 at PDF p.5 (lines 189-209); Q3 call advances at PDF p.12 (lines 502-505), "offensive" at PDF p.11 (line 471). About nine anchors use the printed footer page; the Phase 1 anchor p.11 matches neither convention. Every value itself is correct. |
| 2 | A | source_fidelity: true | 04-bizmodel.md (Findings item 3, "PR p.1") and 07-emoat.md (P1 inflow line, 4D exports, E2-2, 1C, "PR p.1") | "Orders received during the quarter stood at Rs. 2,036 crores" and H1 FY27 exports 5.7% are on PDF p.2 of 2026-11-12_Q2FY27_press_release (lines 56-59); PDF p.1 is the cover letter. Values correct. |
| 3 | A | source_fidelity: true | 07-emoat.md, 1A row 9 and D1-1 ("AR p.22") | "first satellite targeting 2027-28" occurs once in Annual_Report_2026.txt, line 1678, PDF p.25. AR p.22 carries the 40 GHz MMIC text. Wrong page, correct text. |
| 4 | A | source_fidelity: true | 09-tam.md, Section 3 Method 2 bottom-up ("deck PDF p.7") | Uttam AAAU Rs 1,878.8 Cr ex-tax is on Investor_Presentation_1 PDF p.6 (line 187). PDF p.7 is the revenue break-up. Page slip; value correct. |
| 5 | A | source_fidelity: true | 03-ardeep.md (triple-pass row 14, B02 CORRECTIONS item 2, YAML note_ref "Note 46 p.265") and 02-notes.md (P3-2 "Note 14, p.236") | Note 46 text (lines 17273-17282) is on PDF p.264; p.265 holds Note 47 only. The 7.15% to 9.80% sentence (line 15701) is on PDF p.237. Values (77,837; 28,486; 7.15%; 9.80%) correct; derived 49,351 remaining shares right. |
| 6 | A | source_fidelity: true | 03-ardeep.md, Phase 3C EBITDA BASIS MISMATCH ("pp.31, 35") | Rs 343 Cr is at PDF p.34 (line 2407); the 266 / 343 and 25.47 / 29.70 table is at PDF p.35 (lines 2423, 2460). PDF p.31 holds the segment order book table. Values correct; the basis finding recomputes exactly. |
| 7 | B | WEIGHTING | B05 4D "Defensiveness and not quarterly stance" LOW | Execution-delay and deflection pattern spans three calls, the Q1 FY27 deferred-revenue quantum went unanswered, and SGR "modest" vs MVR "robust operational execution" (Q1 FY27 p.3-4) is unrecorded; MEDIUM fits. |
| 8 | B | SPOT CHECK WRONG | B05 2A row 5 and promise_delivery row "Man-portable SDR" | Marked delivered, but no later call reports bid opening, L1 or award; "SDR programs" in Q4 FY26 orders (MVR p.5) do not identify the tender and SDR wins already existed in Q3 FY26 (MVR p.5); correct status OPEN; delivered tally 4. |
| 9 | B | OVERSTATED | B06 P6, FLAG-PEER-CAPEX, Part 4 | CONTRADICTED rests on peers' own capex scale-up (DP Q1 FY27 p.16; APOLLO Q2 FY27 p.7), which does not test Astra's stated need (Q4 FY26 mgmt p.11); B06's own caveats say so; should not lead synthesis as a contradiction. |
| 10 | B | MISCLASSIFIED | B06 P9 | DP remark "Astra is a DcPP partner for MCA variant, not the Su30 variant" (DP Q1 FY27 p.18) scored as partial support; on the Su-30 radar sub-claim it is a hedged contradiction of Atim's "Tier 1" (Q1 FY27 p.7); B06 2D and FLAG-PEER-COMPETE carry it correctly. |
| 11 | B | ANCHOR FORMAT | B05 throughout | About 9 of 20 spot-checked B05 page anchors cite the transcript footer page, one below the PDF page; one is one high (Uttam phase plan "Q1 p.11" is p.10); referred to Verifier A, not a source-fidelity ruling. |
| 12 | B | MISSED | B05 guidance "Funding"; Q3 FY26 mgmt PDF p.11 and Atim p.7; Q1 FY27 mgmt PDF p.15 | Equity stance gained an "accretive nonorganic opportunities" carve-out: "we won't be raising any equity capital" became "Till we have accretive nonorganic opportunities, we will not dilute for working capital". |
| 13 | B | MISSED | B05 3D; Q3 FY26 SGR PDF p.3; Q4 FY26 MVR PDF p.5; Q1 FY27 SGR p.3 and MVR p.4 | Q4 FY26 order-book roll-forward gap of about Rs 125 Cr [calc: 2,226 + 530 - 490 = 2,266 vs 2,141 reported]; Q1 FY27 reconciles within Rs 12 Cr. |
| 14 | B | MISSED | B05 1A space/met row; Q3 FY26 mgmt PDF p.17; Q1 FY27 mgmt PDF p.13 | Mission Mausam ordering timeline pulled forward without a stated cause: "at least a couple of years to finalize" became "more orders in the current financial year". |
| 15 | B | PARTIALLY CAUGHT | B05 2A row 3; Q4 FY26 MVR p.5; Q1 FY27 MVR p.4 | Rs 300 Cr PNC promised "in next couple of months" is not tracked; Q1 FY27 inflow was Rs 185 Cr. |
| 16 | B | PARTIALLY CAUGHT | B05 1C exports; Q4 FY26 mgmt p.10, p.18; Q1 FY27 mgmt p.12 | Export gross margin told as 40% and 45% to two analysts; history reframed as "so-called exports, which was not really exports". |
| 17 | C | C-P1-02 (rule E17, prompts/07 l.140-148) | 07-emoat.md l.340 (stage 07) | I2 answered collectively; relationships called execution leads. Recomputed I2 0 unchanged; no specific sacrifice named. Decision impact none; reasoning gap on the institutional-relationship direction. |
| 18 | C | C-P1-03 (rule E18, prompts/07 l.39-40) | 07-emoat.md l.239, l.245-250, l.301 (stage 07) | D1, E2, H1 headed NO EVIDENCE FOUND while tabling D1-1, E2-1, E2-2, H1-1. Recomputed 0 each unchanged; no tabled item matches a listed indicator; H1-1 credited in R1. Label only. |
| 19 | C | C-P1-04 (rule E21, prompts/07 l.60-62) | B07-emoat.yaml l.40 (stage 07) | capex_embedded_growth_pct 19.9 on the literal total-capex reading; 9.4 plant-only (24 x 4.51 = 108 Cr), the report's own capacity figure (07-emoat.md l.132). No EM score impact; block should carry both figures with the basis. |
| 20 | C | C-P1-05 (rule E22, prompts/07 l.184-185, l.194) | 07-emoat.md l.458-470; B07-emoat.yaml l.42-51 (stage 07) | 13 report rows, 10 block rows: block missing GaN next-generation radar and A4 platform cadence; A2 and I1 merged; R1 (2.1, claim-only) and B1 (1.5, inference multiplier) have no row. No score impact; two report rows would not reach the synthesis monitoring checklist. |
| 21 | C | C-P1-06 (rule G14, prompts/01 l.19-25) | 01-gate0.md l.58, l.111 (stage 01) | B2-B4 NOT FOUND on a 2-year window; M6 3 on a 2-year window. Reading 1, per-metric 3-year floor: M6 0, moat_score 12, moats_confirmed 2, grand_total 65. Reading 2, no floor: Block B 8, core 61, DB2 off. AVERAGE and MODERATE under both readings. |

## Verifier C framework gaps (as the verifier wrote them; operator ruling needed)

1. prompts/01: per-metric minimum window undefined (C-P1-06).
2. prompts/07: Strong/Moderate/Weak/None cut-offs undefined; stage used its own (07-emoat.md l.11).
3. prompts/07: combined-matrix mapping absent (labels only, l.204-205); 6D not re-derivable in phase-1 scope.
4. prompts/07: "active" in the completionist guard undefined (non-zero vs Strong/Moderate).
5. prompts/07: multiplier rule for mixed-class evidence undefined.
6. prompts/07 2C: "historical" FAT (latest vs mean) and treatment of intangibles under development undefined.

## Verifier D

No findings. Peers audited 2; substantive confirmed 2; no unsupported substantive claim; no unused but relevant transcript; all claims addressed; no verdict discipline fails. The five B06 ERRATA anchors were re-checked and are right.

## Verifier B coverage notes (as the verifier wrote them)

Independent flags found 24: caught 12, partially caught 8, missed 4. Promise delivery spot checks 5: confirmed 4, wrong 1. Credibility grade concur: "lower: B is defensible on hard numbers, but delivered is 4 not 5 (B05 2A row 5 MP-SDR unevidenced) and the grade omits the order-book goalpost redefinition, the volunteered inventory-obsolescence admission and the 18-month senior churn; reads B-minus, with B05's own C trigger (H2 FY27 revenue near Rs 913 Cr, FY27 year-end CFO) unchanged". Main transcripts read in full (3 of 3); 8 peer transcripts keyword searched and hit sections read; PARAS absent.

## Verifier A coverage note (summary of B12a coverage_note)

Mandatory tier: no B10, B11 or verdict card exists in Phase 1. The tier was (a) every sourced Gate 0 scorecard input (177), (b) the Section 1B sector cap row inputs in 04-bizmodel (20), and (c) 37 other pillar or priority inputs: 234 of 234 checked. Sample tier: about 950 material numbers, 458 checked (about 48 percent), by materiality. Not checked against a PDF: web sourced figures in 08-promoter and 09-tam (outside the corpus, a coverage shortfall, not UNANCHORED); the 09-tam arithmetic on those inputs was recomputed and holds. Pass level files 02-notes-pass1 and 02-notes-pass2 were not audited. Errata appended to the reports were applied before checking.

## Valuation component

PENDING PHASE 3. Verifier C's audit of B10 and B11, the expectation ledger rules 13 and 14, the recomputed destination PE and the recomputed decision have not run. The business narrative rule 9 check is pending the finalize verifier pass.
