# Verifier summary, phase 1: Walchandnagar Industries (WALCHANNAG), run 2026-11-12

Scope: Verifier A (numerical), Verifier B (red flags), Verifier C (Gate 0 and Emerging Moat half only; valuation half pending phase 3) and Verifier D (peers). Each verifier ran once (manifest verifier_runs A 1, B 1, C 1, D 1). Remediation cycles: 0. Verifier A shadow: not run (one run slot claimed by runs/kusumgar-2026-11-12; switch not touched).

## Confidence delta, phase 1

| Component | Score | Denominator / basis |
|---|---|---|
| Numerical acceptance (A) | 97 | about 450 numbers checked; mandatory tier 26 of 26 (Gate 0 inputs only; no verdict card or Section 1B output exists in phase 1) |
| Red flag coverage (B) | 82.4 | 14 of 17 material items caught or partially caught; strict caught only 11 of 17 = 64.7% |
| Framework adherence (C) | 91.7 | 77 of 84 rules (Gate 0 44/48, Emerging Moat 33/36); valuation component PENDING phase 3 |
| Peer utilisation (D) | 100 | 12 substantive of 12 provided |
| Overall | 82.4 | set by red flag coverage; band 75 to 89, normal; REWORK not triggered (no CONFIRMED Verifier A CRITICAL; no acceptance rate below 60% on a denominator of 4 or more, OR-29) |

## Acceptance rates and counts

| Verifier | Model | Acceptance | CRITICAL | MAJOR | MINOR | Notes |
|---|---|---|---|---|---|---|
| A, numerical (B12a) | claude-sonnet-5-5 | 97 | 0 | 4 | 4 | 6 false positives struck; material universe 620; mandatory 26 of 26 |
| B, red flags (B12b) | claude-opus-5-5 | 82.4 | 0 | 8 | 7 | 32 independent flags; 15 caught, 7 partially caught; promise spot checks 5, confirmed 4, wrong 1 |
| C, framework, phase 1 half (B12c) | claude-opus-5-5 | 91.7 | 0 | 0 | 7 | valuation rules 0 checked (PENDING phase 3); expectation ledger and narrative checks PENDING, template defaults |
| D, peers (B12d) | claude-sonnet-5-5 | 100 | 0 | 0 | 3 | 12 audited, 12 substantive confirmed; no unsupported, no unused but relevant |

## CRITICAL findings

None. Verifiers A, B, C and D each report critical_count 0.

## MAJOR findings

| # | Verifier | Location | Finding | Source fidelity |
|---|---|---|---|---|
| 1 | A | 01-gate0.md Block A, line "AR cross-check on Total Assets less Current Liabilities" | Claimed FY24 1.76%, FY25 -8.64%, FY26 5.75%. On the cited anchors with EBIT (PBT + finance cost) over TA less CL: FY24 748 / 43,872 = 1.71%; FY25 -4,214 / 48,555 = -8.68%; FY26 2,377 / 44,033 = 5.40% (AR 2025 p.67-68; AR 2026 p.67-68, INR Lakhs). Scored series is the screener ROCE, which reproduces; scores unchanged. Not a verdict card or Section 1B input, so MAJOR not CRITICAL. | true |
| 2 | A | 02-notes-pass1.md section 12 and top 10 rank 7; 02-notes-pass2.md B3 item 14; 02-notes-pass3.md top 15 rank 10; B02 yaml top_findings rank 10 | ESOP outstanding claimed 3,98,388 = 0.59%. Note 20 tranche rows (AR 2026 PDF p.101-108): 1,04,076 + 1,61,812 + 1,20,000 + 1,12,500 = 4,98,388 = 0.73% of 6,78,42,060. 03-ardeep.md rank 10 catches it; the 02 reports and the B02 block still carry 3,98,388. | true |
| 3 | A | 05-concall.md load bearing fact 3, section 2D row "Other income share of EBITDA", yaml FLAG-OTHER-INCOME, analyst_note | Claimed 34% to 68% of EBITDA each quarter. Q3 FY26 306 / 1,836 = 16.7% (Q3 FY26 PR, filing 20260129-e605cd17 p.2); Q4 FY26 67.8%; Q1 FY27 48.7%; Q2 FY27 34.4%. Range is 17% to 68%. | true |
| 4 | A | 04-bizmodel.md evidence table rows "FY25 revenue share" and "FY24 revenue share", yaml input_gaps/flags; 07-emoat.md section 0 facts 1d, 1b, 1B "Product" row | DNA share 30% (FY24) to 39% (FY25) and FY25 order inflow Rs 248.50 Cr cited AR 2025 PDF p.30. Both sit on AR 2025 PDF p.29 (text lines 3439 and 3491). The 52% order book share, capex 84/38.49/45.51 Cr and Aerospace Rs 42 Cr are correctly on p.30. Clearance: re anchor to PDF p.29. | true |
| 5 | B | B05 2D/4D (absent) | Planned preferential allotment by FY2027 missed; disclosed only via Acuite (Acuite 7 Aug 2026 p.3). | n/a |
| 6 | B | B05 (absent) | Issue proceeds reallocation of Rs 21 Cr filed as "No deviation" for five quarters (Reg 32 statement 2 Nov 2026 p.2-3; ICRA MA 3 Nov 2026 p.3, p.5). | n/a |
| 7 | B | B05 1B/2A (absent) | NAL Rs 400 Cr in 6 to 7 months opportunity (May 2025) unfulfilled; belongs in the guidance table and promise tally as MISSED (Presentation p.39). | n/a |
| 8 | B | B05 2A row 3; 4D | Q1 FY27 "structural" PAT 118 includes 334 profit on sale of asset held for sale; ex gain PBT -216 (derived); row 3 should be PARTIAL (Results 11 Aug 2026 p.3; results 2 Nov 2026 p.4-5). | n/a |
| 9 | B | B05 2B/4D | FY26 turnaround about 76% base effect from FY25 TNEB provision 5,431 of 7,110; 1,545 FY26 TNEB cost absorbed by provision; raise to red flag with the bull reading (ex provision operating swing about +3,137) beside it (AR 2026 Note 26 PDF p.112; Acuite p.3). | n/a |
| 10 | B | B05 3A | States no competitor is named in the presentation; presentation p.9, p.17, p.30 name competitors and claim "Nuclear: 1 of 4"; credibility check was possible and fails on MTAR (Presentation p.9, p.17, p.30; MTAR 13 May 2026 call lines 743-746). | n/a |
| 11 | B | B06 Q2 net read; FLAG-INCUMBENT; Part 4 contradicted: 0 | OVERSTATED: MTAR is a first time End Shield/Calandria bidder, not the incumbent; correct read is a peer contradiction of WIL's scarcity claim (count 1 contradiction) (MTAR 13 May 2026 lines 743-746; MTAR 30 Jul 2026 line 679; Presentation p.9, p.20). | n/a |
| 12 | B | B05 4C credibility_grade | Would grade D not C; Role 1 4D weights shift 35/45/20 to 45/40/15 (B12b Parts 3-4). Re scored trailing window: delivered 2, partial 3, missed 6. | n/a |

## MINOR findings

| # | Verifier | Location | Finding | Source fidelity |
|---|---|---|---|---|
| 13 | A | 04-bizmodel.md section 1D row "How delivered" | Plant list cited at AR p.205. AR 2026 has 147 PDF pages; the plant list is at text line 205. A text line number was written as a page number. Content is in the source. | true |
| 14 | A | 04-bizmodel.md section 4A row "Structural, Customer insolvency risk" | CIRP against JUD Cements dated 22 Oct 2026. NCLT Guwahati admission order is dated 12 Oct 2026; company learned 21 Oct 2026; Reg 30 filing dated 22 Oct 2026 (announcements/20261022-ca285396, p.1). Filing date presented as admission date with no label. | false |
| 15 | A | 08-promoter.md sections 1B, 3A, 3B | Revenue about Rs 296 Cr / 29,600 Lakhs sourced to company memory. Revenue from operations FY26 is 27,519 Lakhs (275.19 Cr); 29,626 Lakhs is Total Revenue including other income 2,107 (AR 2026 PDF p.68). Company memory is not an anchor. Not material to the verdict. | false |
| 16 | A | 07-emoat.md section 2A capex table, rows "Gear Hobbing Machine" and "Rapid-1250 Hofler CNC Gear Grinding Machine" | Status "Capitalised FY26" at 13.80 Cr and 8.26 Cr (AR 2026 p.50). p.50 gives only Capital Investment of 1,380 and 826 Lakhs; Note 4 (PDF p.87) carries Gear Hobbing Machine 1,622 and Hofler 27 Lakhs still in CWIP at 31 Mar 2026. Anchor gap on a status. | false |
| 17 | B | B05 4D MEDIUM / 2D JUD Cements | OVERSTATED: exposure is sized in the filing (1,657 value, 1,565 impaired, 92 carrying) (Reg 30 22 Oct 2026 p.1-2). | n/a |
| 18 | B | B05 conventions; input_gaps | H1 FY27 CFO left NOT READ; text layer reconciles to CFO (592), cash 859, other financial assets +4,408 (Results 2 Nov 2026 p.4-5). | n/a |
| 19 | B | B05 FLAG-OTHER-INCOME | "34% to 68% each quarter" misses Q3 FY26 at 17%; range 17% to 68% (Q3 FY26 PR p.2). | n/a |
| 20 | B | B05 2A row 8 | Past tense claim scored as a promise; inflates missed tally by one (Q2 FY26 PR p.2). | n/a |
| 21 | B | B05 2A accuracy bullets | 68 Aicitta link is filed fact not inference; "PAT after exceptional" bullet overstated for Q3; Q3 FY26 PR YTD EBITDA 2,250 vs 2,114 from its own quarters unlisted (Results 20 May 2026 Note 6; Q3 FY26 PR p.2). | n/a |
| 22 | B | B05 (absent) | Minor items missed: R15, R21, R23, R25, R26, R27, R32 (B12b Part 1; listed below). | n/a |
| 23 | B | B05 2D/4D | Minor items under weighted: R6 MD&A self contradiction, R19 lockout omitted from MD&A, R24 no call since May 2019 in corpus, R28 Q1-Q2 FY27 tone shift (B12b Part 1). | n/a |
| 24 | C | B01 Block A; B01-gate0.yaml data_notes ROCE line | Rule: ROCE = EBIT / (TA - CL), fixed. Stage used proxy EBIT / (Equity + Reserves + Borrowings). Fixed formula bound gives median 9.39% (A1 0), FY25 -8.64% (A2 0), FY17 <= 4.35% < FY26 5.75% (A4 5); Block A 5 unchanged. Method deviation, disclosed; no score effect. | n/a |
| 25 | C | B01 Block B, B4; B01-gate0.yaml data_notes B4 line | B4 0 (FY17 payables NOT FOUND). Available window reading: B4 1, Block B 1, core 11; strict window reading: B4 0 as scored. Three treatments of one FY17-FY23 data gap; classification AVOID unchanged. | n/a |
| 26 | C | B01 Block F, M6; data_notes PEER DATA NEEDED line | M6 tier labels inverted and R&D/Rev input not stated; tier 1 is peer dependent and fails on R&D 0.00% (B07 A2, AR 2026 p.51); score 0. Presentational. | n/a |
| 27 | C | B01 report fenced YAML block | Pointer stubs; deal breakers without years. B01-gate0.yaml holds the full block. | n/a |
| 28 | C | B07 Section 0 row 4c | "About 18 months tenure at most" left in the body after the erratum declared it unsourced; strike; CFO hire date NOT FOUND. No score effect. | n/a |
| 29 | C | B07 Section 3 recount line; B07-emoat.yaml evidence_mix | Stated documented 8, claim 9, inference 3; about 15 claim tags in Sections 3-4 (A1 3, A3 2, B2 1, F2 2, H2 1, R1 6); inference tags in Sections 0-2 exceed 3. Basis unstated; stated mix reads more documented than the report. | n/a |
| 30 | C | B07 Section 5 two readings; FLAG-EM and analyst_note | Reading B 14.2 MODEST "needs a double credit of A1 and B2 plus a credit on F2". Without double credit 12.1; legal tiers and no double credit 9.7 (range 9.0-10.3), NONE. Adopted 5.2 NONE stands; flag understates what Reading B needs. | n/a |
| 31 | D | B06 Part 4 / YAML unverifiable list | Part 4 says "Unverifiable as whole: 0" but YAML lists Q8 state utility overruns as unverifiable while Part 1 gives Q8 PARTIALLY VERIFIED on central PSU retention; labelling inconsistent, not an upgrade from silence. | n/a |
| 32 | D | B06 FLAG-INCUMBENT (MTAR Aug 2026 txt l.679) | MTAR 60-70% nuclear share line sits after an inaudible marker and reads as a rhetorical tag; B06 attributes it to Srinivas Reddy and flags the marker, but FLAG-INCUMBENT leans on it. | n/a |
| 33 | D | B06 Q6 VERIFIED | "Late delivery" rests on peer date slips (benchmark), not WIL evidence; wording could say benchmark verified. | n/a |

## Verifier B missed items, as listed

| Severity | Item | Anchor |
|---|---|---|
| MAJOR | R10 planned preferential allotment by FY2027 disclosed only to Acuite; absent from every WIL PR, MD&A and Reg 30 filing | Acuite rating 7 Aug 2026 p.3 |
| MAJOR | R11 Rs 21 Cr moved from capex object (105 to 84 Cr) to working capital (50 to 67 Cr) and loan repayment (41 to 45 Cr) by Board resolution 17 Oct 2024, filed as "No deviation" for five quarters; ICRA says utilisation differs from offer document | Reg 32 statement 2 Nov 2026 p.2-3; ICRA MA report 3 Nov 2026 p.3, p.5 |
| MAJOR | R16 NAL wind tunnel "~Rs 400 crores in next 6-7 months" (May 2025) unfulfilled, never updated | Presentation 3 May 2025 p.39; no order filing Nov 2025 to Nov 2026 |
| MINOR | R15 FY24 DNA share 26.5% (presentation) vs 30% (AR2025) | Presentation p.4; AR2025 MD&A line 3439 |
| MINOR | R21 Aicitta project exit unexplained; "No financial impact" vs 68 Lakhs exceptional gain; ICD arranged for Aicitta | Reg 30 5 Mar 2026; Reg 30 28 Aug 2026; results 20 May 2026 Note 6 |
| MINOR | R23 headline EBITDA basis moved from before FX (AR2025) to incl. 390 Lakhs FX gain (FY26) | AR2025 MD&A lines 3511-3516; AR2026 Directors' Report s.1 PDF p.21 |
| MINOR | R25 two exchange price surveillance queries answered with SHANTI Bill narrative | BSE clarifications 22 Dec 2025, 24 Apr 2026 |
| MINOR | R26 "long term Debt Free" aim vs 2,579 Lakhs new LT borrowings H1 FY27 | Reg 30 29-30 Jan 2026 p.2; results 2 Nov 2026 p.4-5 |
| MINOR | R27 VSSC order: free issue material, no tooling cost paid | Reg 30 20 Aug 2026 p.2 |
| MINOR | R32 NSE/BSE fines for ICDR Reg 162 breach on May 2025 warrant conversion | AR2026 Corporate Governance Report lines 3172-3175 |

Verifier B pipeline flags not supported: none. Credibility grade concurrence: "lower: D, not C".

## Verifier A coverage, as stated

Mandatory tier (OR-32): 26 of 26 checked (20 scored Gate 0 core inputs, 5 numeric moat test inputs, the AR ROCE cross-check line); 25 matched, 1 mismatch (finding 1). Verdict card and Section 1B pillar inputs will exist only after stages 11 and 13 and need their own Verifier A pass. Sample tier: about 424 of 620 material figures checked. Not checkable from Verifier A's inputs: web sourced figures in 09-tam.md and 08-promoter.md (outside the corpus). Struck as false positives: 6 rows, none a genuine fidelity finding.

## Verifier disagreement log

none. No downstream step in this phase 1 synthesis kept, re derived from, or cleared a figure Verifier A flagged. Findings 1 to 4 and 13 are carried at their corrected values in gate-recommendation.md.
