# Verifier summary: Azad Engineering Ltd (AZAD), run 2026-11-15, Phase 1

Scope: Verifier A (numerical), Verifier B (red flags), Verifier C (framework; Gate 0 and Emerging Moat portion only, valuation pending Phase 3), Verifier D (peers). Each verifier ran once (verifier_runs A 1, B 1, C 1, D 1). Remediation cycles 0. The Verifier A shadow did not run in this session. Units in the rows are as the verifiers wrote them: filings and annual reports in INR million, screener and CARE in INR crore.

## Confidence delta (Phase 1)

| Component | Score | Source | Basis |
|---|---|---|---|
| Numerical acceptance | 99.3 | B12a | 400 numbers checked; mandatory tier 78 of 78; 0 CRITICAL, 1 MAJOR, 2 MINOR |
| Red flag coverage | 75.0 | B12b | 9 of 12 MATERIAL flags fully caught upstream; 91.7% counting partial catches |
| Framework adherence | 90.4 | B12c | Phase 1 portion only: Gate 0 and Emerging Moat, 85 of 94 rules; valuation adherence PENDING PHASE 3 |
| Peer utilisation | 78.0 | B12d | 7 of 9 peer transcripts handled correctly; 8 of 9 substantive use confirmed |
| Overall | 75.0 | confidence.yaml | Set by red flag coverage; band 75 to 89, normal, note specifics |

REWORK check: 0 confirmed Verifier A CRITICAL; no acceptance rate below 60% on a denominator of 4 or more (denominators 400, 12, 94, 9); REWORK false.

## Acceptance rates and counts

| Verifier | Acceptance rate | Denominator | CRITICAL | MAJOR | MINOR | Other |
|---|---|---|---|---|---|---|
| A, numerical (B12a) | 99.3 | 400 numbers checked (universe about 900); mandatory 78 of 78 | 0 | 1 | 2 | 3 false positives struck under rule 5b |
| B, red flags (B12b) | 75.0 | 12 material of 36 independent flags; 9 fully caught, 2 partly caught, 1 missed | 0 | 3 | 16 | Promise delivery spot checks: 5 checked, 3 confirmed, 2 wrong |
| C, framework (B12c) | 90.4 | 94 rules (Gate 0 57, Emerging Moat 37); valuation 0 checked | 0 | 1 | 8 | Valuation and expectation ledger PENDING PHASE 3 |
| D, peers (B12d) | 78 | 9 peers audited; 8 substantive confirmed | 0 | 2 | 2 | 1 INFO row; claims_all_addressed true |
| Total | | | 0 | 7 | 28 | |

## Source fidelity findings (Verifier A, non overridable)

| Severity | Location | Claimed | Source truth | Disposition in these files |
|---|---|---|---|---|
| MAJOR | 02-notes.md Top 15 rank 9 and yaml top_findings rank 9 (Note 34, PDF pp.244 to 245, consolidated notes) | 104.04 | 104.07, consolidated Note 34 USD sensitivity (AR2026 p.245, text line 12680); 104.04 is the standalone figure (text line 9061) | Corrected figure used: ₹104.07 Mn (about ₹10.4 Cr). 03-ardeep.md already carries 104.07. Not a verdict card, Section 1B or Gate 0 input. |
| MINOR | 02-notes.md P3-1 and the B02 FLAG-CASH text: standalone operating cash flow (1,232.63) vs 628.85 cited to "[page 156] cash flow area" | AR2026 [page 156] | Values correct; they sit on AR2026 PDF page 123 (standalone cash flow statement); page 156 is standalone Note 17, trade payables | Corrected anchor used: [page 123]. |

Verifier disagreement log: none (outputs/final/verifier-disagreement-log.md). No downstream step holds a position against either finding.

Anchor key for the B and D rows: Q1 = AZAD_Q1FY27_concall_transcript_2026-08-14.pdf; Q2 = AZAD_Q2FY27_concall_transcript_2026-11-14.pdf; Q4 = AZAD_Q4FY26_concall_transcript_2026-05-22.pdf; MT-Q2 = MTARTECH_Concall_Transcript_2026-11-06.pdf; UN-Q2 = UNIMECH_Concall_Transcript_2026-10-31.pdf; PT-23 = PTCIL_Concall_Transcript_2023-06-09.pdf.

## CRITICAL

None. No verifier logged a CRITICAL finding.

## MAJOR (7)

| # | Verifier | Location anchor | Finding as written | Fix or recompute as written |
|---|---|---|---|---|
| 1 | A | 02-notes.md Top 15 rank 9 and yaml top_findings rank 9 (Note 34, PDF pp.244 to 245) | MISMATCH on basis: standalone value 104.04 cited as the consolidated note's figure 104.07 (AR2026 p.245). 0.03 apart; no verdict input depends on it. source_fidelity: true | 03-ardeep.md rank 9 row already corrects to 104.07 |
| 2 | B | Q2 [page 15] to [page 16]; Q2 Malpani [page 8] | MISSED: refused count of customers still in delta qualification, the gate on the B05 priority 1 trigger | Name as Halt 1 open question; separating observation is delta qualifications cleared by the Q3 FY27 call |
| 3 | B | Q1 Jajoo [page 10]; Chopdar [page 15]; Malpani [page 15]; Bagmar [page 16] | PARTIALLY CAUGHT: FX answers contradict in one call (CFO below EBITDA; Chopdar few percent; Malpani 5 to 6% revenue help); D1 "25% plus DELIVERED" carries no currency adjustment; [INFERENCE] H1 constant currency growth about 23 to 24% | Carry two readings into Role 1; separating observation is a constant currency or USD revenue figure; rupee rates NOT FOUND |
| 4 | B | Q1 [page 5], [page 9], [page 14]; Q2 [page 10], [page 17] to [page 18] | PARTIALLY CAUGHT: revenue ramp date moved on all three calls and the plant state reversed (Aug "full throttle" vs Nov "spindles just started ... not seeing revenue today"); RF3 holds it as one slip at Medium; B06 calls it mild | Raise RF3 to High; cite the reversal; change D4 to PARTIAL |
| 5 | C | 07-emoat.md S3 row F2 (l.94); F2 evidence (l.126 to 129); S5 (l.157). Rule 3 / 07 Section 5 matrix | F2 recorded documented, Weak, Mixed; scored 0. Matrix gives 0 only for no evidence; the stage's own Weak documented row R1 scores 2 | F2 = 1.0; em_score 13.0, MODEST unchanged; the C1 Low edge case becomes 12.0 MODEST, not 11 NONE. The other reading needs F2 labelled None in S3 |
| 6 | D | MT-Q2 [page 10], [page 11] | Q1 and Part 5 present MTAR 260 to 50 days as the cash fix and omit MTAR's own statement that 50 days is not sustainable (100 by year end, 150 long term). This bears directly on Azad's 160 to 180 and 200 day targets | Not stated by the verifier |
| 7 | D | PT-23 [page 10], [page 31] | FLAG-NO-GAS-TURBINE-PEER and "Gas turbine: silent" overstate. PTCIL names industrial gas turbines as an evolving market and says their approvals are much shorter than aerospace. No growth rate is given, so the no growth rate point stands | Not stated by the verifier |

## MINOR (28)

| # | Verifier | Location anchor | Finding as written | Fix or recompute as written |
|---|---|---|---|---|
| 1 | A | 02-notes.md P3-1 (and B02 flag text) | ANCHOR NOT FOUND: standalone OCF (1,232.63) vs 628.85 cited to [page 156]; the number exists at AR2026 p.123. source_fidelity: true | Stage errata and 03-ardeep.md correction 2 already give p.123 |
| 2 | A | 03-ardeep.md Phase 1B, KAM row: "Q4 revenue was 1,573.9 Rs Mn, 26.1% of the year [calc] (AR26 [p.13])" | UNANCHORED basis: an unlabelled basis quarter is divided by a consolidated year; filed Q4 FY26 consolidated revenue is 1,615.39 Mn (Q4 FY26 results p.10), 26.8% of 6,029.75; the 41.5 Mn gap is not named. source_fidelity: false | Not material to any verdict input |
| 3 | B | Q2 [page 12] to [page 13] | MISSED: other operating income question unanswered; CFO confused it with other income; taken offline | Read the results line; upgrade if material |
| 4 | B | Q4 [page 7]; Q2 [page 7] | MISSED: inventory and receivable ageing bases changed between May and Nov (96% of inventory under 1 year, then 72% of ageable inventory under six months and 69% of regular receivables not yet due; terms undefined) | Add to FLAG-MARGIN-WIP watch |
| 5 | B | MT-Q2 [page 19]; UN-Q2 [page 7], [page 10] | MISSED: peer order book framing contrast (MTAR 12 to 18 months executable; Unimech firm POs vs Rs 589 Cr forecast based LTAs) not used against Azad's unsplit Rs 6,500 Cr | Context for RF5 in the A26.1 basis hierarchy |
| 6 | B | Q2 [page 7] | MISSED: call capex funding bridge does not close as spoken (Rs 139.3 Cr vs Rs 80.8 Cr QIP plus Rs 28.6 Cr named, Rs 109.4 Cr) | Note only; cash flow statement governs |
| 7 | B | Q2 [page 11]; Q2 [page 9] | PARTIALLY CAUGHT: Chopdar "we started the bill discounting" vs Malpani "in reserve" in the same call | Add to RF2 |
| 8 | B | Q4 [page 10]; Q1 [page 13]; Q2 [page 12] | OVERSTATED: Rolls-Royce "slipped three times"; one missed date, H2 window still open | Correct optionality tracker and 4A kill wording |
| 9 | B | Q4 [page 8]; Q1 [page 14]; Q1 [page 5] | OVERSTATED: M7 guidance revisit counted MISSED though hedged and conditional | Reclassify PENDING |
| 10 | B | Q1 [page 5]; Q2 [page 3], [page 10], [page 11], [page 18] | Spot check WRONG: D4 DELIVERED; later call Q&A supports PARTIAL with full closure PENDING | Correct to PARTIAL; tally 5/6/7 |
| 11 | B | MT-Q2 [page 4]; MT-Q2 [page 8] | OVERSTATED: B06 cites MTAR 15 month Phase 3 slip; same transcript also says June of next year (June 2027) | Note both readings |
| 12 | B | UN-Q2 [page 6] to [page 7]; Q4 [page 15] | PARTIALLY CAUGHT: Unimech Saudi JV on schedule while Azad deferred its Saudi plant | Reweight M8 toward bandwidth choice |
| 13 | B | Q4 [page 18] | PARTIALLY CAUGHT: capitalised development cost answer rated satisfactory but was partial | Check FY25 AR policy and intangible/CWIP note |
| 14 | B | Q2 [page 7]; MT-Q2 [page 11]; UN-Q2 [page 12] | PARTIALLY CAUGHT: asset turn contrast uncomputed for Azad (about 1.1x calc vs peers 2 to 3x) | Stage 11 uses filed gross block |
| 15 | B | Q2 [page 4] | B05 quote anchors at Q2 [page 3] belong at Q2 [page 4] (PAT "speak plainly", H1 consolidated) | Correct anchor |
| 16 | B | Q2 [page 5], [page 11]; Q1 [page 14] | PARTIALLY CAUGHT: ARR Rs 1,300 Cr scope and Rs 1,800 to 1,900 Cr full potential framing unreconciled | Halt 1 open question |
| 17 | B | Q4 [page 7]; Q1 [page 6] | PARTIALLY CAUGHT: FY26 other income Rs 46 Cr (FX plus treasury) in the FY26 PAT base | Stage 11 builds entry earnings ex other income (A18) |
| 18 | B | UN-Q2 [page 7] | PARTIALLY CAUGHT: Dheya small turbojet progress not read against ATGG positioning | Context for ATGG optionality slice |
| 19 | C | 07-emoat.md A1 (l.105 to 109); B2 (l.112 to 115); C1 (l.118). Single credit rule | MHI LTCPA (ANN 2026-03-26) credited in A1 and B2; no separation stated; A1 certificates are a B2 rubric item | A1 3.0 if distinct mechanisms are stated; 2.0 if the MHI filing is held in B2 only; em_score 11.0 to 12.0. B2/C1 overlap has no score effect |
| 20 | C | 07-emoat.md B2 (l.113); 1A Safran (l.26); 1A Arabelle and Landing gear (l.29 to 30). 07 op rule 2 evidence taxonomy | Q2 concall statement tagged documented; MOU tagged documented; two rows untagged | No score change; B2 stays documented on four filed agreements; Safran scores 0 |
| 21 | C | 07-emoat.md S5 (l.157). 07 Section 5 full scoring table | 17 rows collapsed into one line; the collapsed line hides F2, the one zero row with documented evidence | n/a |
| 22 | C | 07-emoat.md 2A (l.51 to 58). 07 Section 2A table columns | % over current column absent | Write NOT FOUND where no base exists |
| 23 | C | 07-emoat.md I2 (l.133). 07 Family I, I2 | One collective answer for the company; separate answers for A1, B2 and C1 are absent | I2 = 0 unchanged |
| 24 | C | 07-emoat.md register (l.165 to 177); B07-emoat.yaml optionality_register | Report names 10 current items carried in the block; block carries 8; four column table absent from report | Add Baker Hughes oil and gas revenue line and OEM advance (USD 4.5 Mn) to the register |
| 25 | C | 01-gate0.md Block F M7 (l.78). 01 op rule 5 grounded claims | "unregulated" asserted with no basis or anchor; B07 S4A records CEMILAC/DGAQA status NOT FOUND | M7 = 0 unchanged |
| 26 | C | 01-gate0.md Block F M11 (l.82); B01 data_notes. 01 M11 two window test | 6 years only, two window test called impossible, fallback used; rule threshold is 6 years or more, and 6 meets it | M11 = 3 unchanged: FY23 to FY26 revenue CAGR 33.8% is below FY21 to FY24 40.6% (or FY21 to FY23 43.2%), so tier 5 fails and tier 3 holds |
| 27 | D | PT-23 [page 19], [page 20] | PTCIL EBITDA margin trend (26% to 29% FY22 to FY23) and working capital/ROE remark not used in Q6 or Q1 (stale 2023 source) | Not stated by the verifier |
| 28 | D | B06 Part 1 Q12, Q13 | Q12 and Q13 verdict grade is generous: Q12 PARTIALLY VERIFIED although no peer quotes a wallet share figure; Q13 PARTIALLY VERIFIED although the 5 to 6% revenue lift is not tested | Not stated by the verifier |

## INFO (1)

| Verifier | Location anchor | Note as written |
|---|---|---|
| D | MT-Q3 p6; MT-Q4 p13; MT-Q1 p7; MT-Q2 p13; UN-ACQ p10, p16; UN-Q4 p7; UN-Q1 p7; UN-Q2 p9, p13, p17; PT-23 p10, p20 | Spot checked anchors all found. Only Q11 is VERIFIED, and it has two independent peers (MTAR debt, Unimech equity). No upgrade from silence found. All 14 peer_questions received a verdict. |

## Other verifier records, as written

Verifier A:
- Mandatory tier (OR-32): every Gate 0 scorecard input, 78 of 78, ties to screener-Data_Sheet.csv, AR2026 pp.123/191/193/232/242, AR2025, Prospectus pp.71/73/92, Q2 FY27 results pp.6/10/11, Q4 FY26 results p.13 and the shareholding XBRL. No verdict card or Section 1B pillar inputs exist in stages 1 to 9, so none were in scope.
- Rule 5b rows struck (3): FY26 EBITDA 225.32 vs four quarter sum 225.31 (rounding); H1 revenue 3,635.4 vs 3,635.34 (formatting); the 37.4% "FY21-25" standalone CAGR label (faithfully transcribed deck anomaly; the computed FY21 to FY26 37.4% is right).
- Not checked (named): most of 02-notes-pass1 beyond line 60 and 02-notes-pass2; 03 board and compensation tables beyond samples; 06 peer figures beyond about a dozen; 07 narrative items; 08 MEDIA items (block sale price Rs 1,623.78, 48 lakh share block); 09 live web figures (GE Vernova 122 GW, Siemens Energy, Howmet, MHI, Baker Hughes, USD 93.70). These sit outside the PDF corpus.

Verifier B:
- Credibility grade: concur, C holds. D4 and M7 corrections give 5 delivered / 6 partial / 7 missed, and the unweighted items (Aug "full throttle" vs Nov "spindles just started", three way FX answer, refused delta qualification count) all point the same way.
- Pipeline flags not supported: none.
- Coverage basis: 12 material (1 CRITICAL, 11 MAJOR) of 36 listed; read in full: 3 Azad calls, MTAR Q2 FY27, Unimech Q2 FY27; other 7 peer files read by keyword passages only.

Verifier C:
- Scope: Phase 1 only. Gate 0 (B01) and Emerging Moat (B07) audited. Valuation rules 4 to 7 and 9 to 15 not run; expectation ledger rules 13 and 14 not checked (null is not a fail). Rule 9 (Business Understanding Narrative) not in Phase 1 scope.
- Recomputed destination PE and decision: not applicable in Phase 1.

Verifier D:
- Unused but relevant: MTAR says 50 days is not sustainable, year end target about 100 days, long term goal 150 days over 2 to 3 years, with a GST refund of Rs 70 to 80 Cr a year as part of the lever (MT-Q2 [page 10], [page 11]); PTCIL names industrial gas turbines as a "very big area that's evolving" with certification "much, much shorter" than aerospace (PT-23 [page 10], [page 31]); PTCIL EBITDA margin 26% to 29% FY22 to FY23 and an analyst remark that working capital need is very high and ROE is below 10% (PT-23 [page 19], [page 20]).
- Substantive use unsupported: none. Claims all addressed: true.
