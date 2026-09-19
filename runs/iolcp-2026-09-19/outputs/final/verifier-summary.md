# IOLCP: verifier summary (Phase 1 lite, run 2026-09-19)

## Phase 1 confidence delta

| Component | Value | Verifier | Basis |
|---|---|---|---|
| numerical_acceptance | 100 | A (B12a) | 21 of 21 sampled figures clean; material universe 47 |
| redflag_coverage | 77 | B (B12b) | 10 of 13 material flags caught or partly caught; strict full catch reading 31 (4 of 13) |
| framework_adherence | 73.2 | C (B12c) | phase 1 portion: 41 of 56 rules (Gate 0 28 of 32, Emerging Moat 13 of 24) |
| peer_utilisation | 100 | D (B12d) | 12 of 12 peer transcripts substantive |
| overall | 73.2 | | overall_set_by: framework_adherence (B12c Gate 0 plus Emerging Moat half) |

Band: 60 to 74, PROCEED verdicts downgrade one level; set by framework_adherence. Pending: framework_adherence valuation half (B10/B11), phase 3. REWORK gate: Verifier A CRITICAL 0; no acceptance rate below 60 on the 77 reading; result "no REWORK trigger". Under the strict 31 reading, redflag_coverage falls below 60 and forces REWORK; operator ruling at Halt 1.

## Acceptance rates and counts

| Verifier | Scope | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| A numerical (haiku) | 21 of 47 material figures | 100 | 0 | 0 | 0 |
| B red flags (opus) | 24 independent flags; 13 material | 77 (strict 31) | 1 | 9 | 9 |
| C framework (opus), Gate 0 + Emerging Moat only | 56 rules | 73.2 | 1 | 4 | 8 |
| D peers (sonnet) | 12 peer transcripts | 100 | 0 | 0 | 0 |

Verifier disagreement log: none. Verifier A logged zero findings, so no downstream step conflicted with a source fidelity finding.

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Note |
|---|---|---|
| B | B05 2E / repeated_evasions | MISSED repeated evasion (Feb, May, Aug): R&D / new product pipeline never answered. Anchor: Feb p.12-14; May p.11; Aug p.7, p.11, p.12 |
| C | EM-1: 07-emoat.md Section 5 rows B2, E2, F1, G1; B07 em_score, em_classification, combined_assessment | L x I matrix misapplied, LM scored 2 (rule says 1). em_score 26.3 to 23.4 (23.1 on maker A2 multiplier); STRENGTHENING to MODEST; crosses below the EM 25 UA qualifier; 6D GOOD+ loses its basis. Action: REWORK stage 7 Section 5 and 6D recommended (not forced; stage 7 not rerun in phase 1) |

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 3C row 3 | NOT SUPPORTED: inventory gain exchange read as consistent denial; transcript shows admission reversing the May denial; Q4 15.2% beat partly valuation driven. Anchor: May p.4 (Abhay); Aug p.7 (Abhay); Aug p.9 (Mahajan) |
| B | B05 3B bullet 4; peer_questions Q3 | NOT SUPPORTED: analyst's spread figures and ibuprofen "neutralised" remark attributed to IOL management as an acetyls claim. Anchor: May p.7 (Sachin Kasera); Sep p.7 (Abhay); Aug p.4 (Mahajan) |
| B | B06 Q3, FLAG-SPREAD, Part 4 | NOT SUPPORTED: second contradiction rests on a claim IOL never made; LXCHEM Aug call dated 30-Jul-2026, not after IOL's call. Contradicted count should be 1, not 2. Anchor: LXCHEM-Concall_Aug_2026 p.7; Sep p.7 |
| B | B05 2A row 6 / promise_delivery | Greenfield MISSED is wrong in direction: 4-6/6-8 quarter window not elapsed; "not in this FY" agrees with it; the 3-4 month approvals sub-promise was substantially met. Should be OPEN / NOT YET DUE. Anchor: May p.4, p.11; Aug p.11; Sep p.8 |
| B | B05 2B/2C/3B | MISSED: contradictory spread answers to two analysts on the May call; peer backs the higher spread version. Anchor: May p.7, p.9; LXCHEM-Concall_May_2026 p.7 |
| B | B05 1C / 4A trigger 2 | MISSED: paracetamol price concession for volume, peer corroborated (pharma EBIT 10.5% to 9.7%, "focusing mainly on volume"). Anchor: Feb p.9; GRANULES-Concall_Jan_2026 p.12 |
| B | B05 1C / 4D | PARTIALLY CAUGHT: CDMO formulations denied in Feb, "proof-of-concept" answer in Aug, EU-GMP plant with ~30% funding incurred disclosed in Sep. Anchor: Feb p.7; Aug p.12; Sep p.2-3 |
| B | B05 3C row 2 / 3B | PARTIALLY CAUGHT: ibuprofen "no pressure" denials vs May admission of a new peer entrant, alongside 50% capacity add with unquantified customer backing. Anchor: Feb p.4, p.13; May p.6, p.8; Sep p.10 |
| B | B05 1B / guidance YAML / 2C | PARTIALLY CAUGHT: FY28 15-20% / 15-17% entered without the same breath "we cannot predict for 28"; May FY27 numbers vary 15%+/-2 to 16-18% to mid-teen; Consistency 4/5 overstated. Anchor: May p.5, p.6, p.15; Aug p.9 |
| C | EM-2: 07-emoat.md C1 vs H2 | C1 scored HH x 1.0 = 4.0 on Anchor Customer relationships that H2 grades as management claim ("contracts being finalized"); 0.7 reading gives 2.8. Action: state one tier for the Anchor Customer evidence |
| C | EM-3: 07-emoat.md A1 and R1/4A-4C | Same EDQM/MFDS/NMPA filing extension credited in A1 (3.0) and R1 (2.0); one improvement, two mechanisms. Action: separate R1 evidence or drop the overlap |
| C | EM-4: 07-emoat.md 2C; B07 capex_embedded_growth_pct | 142.6 includes the undated ₹1,200-1,400 Cr greenfield, not capex under execution; dated ₹495 Cr tranche gives 39.3. Action: restate the field; keep 142.6 as a labelled ceiling note |
| C | G0-1: 01-gate0.md Block B B2/B3 | FCF built on AR p.24 capex chart for FY22-FY24, a substituted basis the fixed formula forbids; CFS basis B2 = 2 (FY25-FY26, 1 of 2 positive) or 0 if N/A, maker 0; classification GOOD unchanged. Action: restate on CFS basis or source FY22-FY24 CFS |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 2E row 1 | PARTIALLY CAUGHT: Aug margin drivers contradict across Khanna, Abhay, Mahajan. Anchor: Aug p.5, p.7, p.8, p.9 |
| B | B05 1B / guidance YAML | PARTIALLY CAUGHT: ibuprofen asset turn walked to 1.5-1.75x, "not the firm number"; B05 records 1.75-2.0x. Anchor: Sep p.3, p.12 |
| B | B05 Supplementary | MISSED: "neutralised" vs "margin expansion, yes" within Sep call. Anchor: Sep p.7, p.13 |
| B | B05 2A row 5 | PARTIALLY CAUGHT: minoxidil end-Dec target slip omitted. Anchor: Feb p.7-8 |
| B | B05 2A row 4 | PARTIALLY CAUGHT: FY26 capex ₹160 Cr vs ₹130-135 Cr guide labelled DELIVERED. Anchor: Feb p.7; May p.3 |
| B | B05 3D | MISSED: non-ibu export share drift (15-17% to 20% to 21-20%; regulated split given in Feb, "not having exact bifurcation" in Aug). Anchor: Feb p.6; May p.11; Aug p.6 |
| B | B05 2B | MISSED: pass-through statements conflict (Aug: prices tied up with big customers; Sep: "in every contract, we have a clause of price adjustment"). Anchor: Aug p.9-10; Sep p.10 |
| B | B05 1B / Supplementary | PARTIALLY CAUGHT: ROCE "more about 15%" transcribed as ">15%". Anchor: Sep p.10 (Mahajan) |
| B | B05 1A | MISSED: Triacetin commissioning timing ("recent commissioning" 22-May vs "started production... after May"). Anchor: May p.3; Aug p.13 |
| C | G0-2: 01-gate0.md B4 | B4 3 on FY25 to FY26; same score; 1 year window, deal-breaker 2 fragile (Block B sits exactly at the line of 8). Action: carry fragility note |
| C | G0-3: 01-gate0.md E2 | E2 5 scored on a 21 month window (Sep-2024 to Jun-2026), not 3 years; score unchanged. Action: none |
| C | G0-4: 01-gate0.md deal-breaker text, analyst_note | Qualitative framing (ibuprofen supercycle, company memory LBF3) in a numbers only stage; A1 median (15.03%, FY18) spans the peak years. Action: trim |
| C | EM-5: 07-emoat.md Section 5 A2 | A2 stated DOCUMENTED tier but multiplied 0.7; rule gives 1.0 (+0.3). Action: fix |
| C | EM-6: 07-emoat.md Section 3 recount; B07 evidence_mix | Completionist recount says 28 documented items; listed breakdown sums to 18; evidence_mix.documented 28 unreconciled; guard outcome unchanged. Action: reconcile |
| C | EM-7: 07-emoat.md G1, G2, 1C | Several anchors point to upstream blocks (B03, B04, B05) instead of primary documents. Action: anchor to primary documents |
| C | EM-8: 07-emoat.md 6C | 6C omits existing moat count (moats_confirmed 0, moat_class NONE). Action: add |
| C | EM-9: 07-emoat.md end | 07-emoat.md does not end with the fenced YAML block; block exists only in blocks/B07-emoat.yaml. Action: append block |

## Verifier B side records

- Promise delivery spot checks: 5 checked, 4 confirmed, 1 wrong.
- Credibility grade concurrence: "lower: B/C boundary. Delivery supports B, but the May-denied / Aug-admitted inventory gain, contradictory margin and spread answers across analysts, the CDMO 'proof-of-concept' reply 4 weeks before an EU-GMP plant, and a 3-quarter pipeline non-answer cut Consistency and Transparency to 3/5 at most; operator ruling needed at Halt 1 since 4D weights key off the grade."

## Verifier C recomputed values (used downstream)

| Field | Maker | Recomputed |
|---|---|---|
| em_score | 26.3 | 23.4 |
| em_classification | STRENGTHENING | MODEST |
| UA EM 25 qualifier | passes | fails at recomputed score |
| capex_embedded_growth_pct | 142.6 | 39.3 |
| Gate 0 B2 | 0 | 2 (CFS FY25-FY26) or 0 (N/A); classification GOOD unchanged |

Valuation audit, expectation ledger and business understanding narrative checks: PENDING PHASE 3 / NOT IN SCOPE.
