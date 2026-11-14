=== FILE: verifier-summary.md ===

# Verifier summary: Kusumgar Ltd (KUSUMGAR), Phase 1, run 2026-11-12

Scope: Verifier A (numerical), Verifier B (red flags), Verifier D (peers) in full, and the Gate 0 and Emerging Moat portion of Verifier C (framework). The Verifier C valuation half is PENDING PHASE 3 (no B10 or B11 exists). Each verifier ran once (manifest verifier_runs A 1, B 1, C 1, D 1); remediation cycles 0. The Verifier A shadow run is not a verifier of record and its findings are not listed here.

## Phase 1 confidence delta

| Component | Score | Source | Basis |
|---|---|---|---|
| Numerical acceptance | 99 | B12a | 0 CRITICAL, 1 MAJOR, 4 MINOR; mandatory tier 315 of 315 checked, 0 mismatches; identity check: no CRITICAL rows, nothing struck |
| Red flag coverage | 82 | B12b | 9 of 11 MATERIAL flags had by the pipeline (5 caught, 4 partially caught); 2 MAJOR missed (F7, F11). Strict reading, CAUGHT only: 5 of 11 = 45% |
| Framework adherence | 84.3 | B12c | Gate 0 + Emerging Moat only: 43 of 51 rules pass (Gate 0 23/26, Emerging Moat 20/25); valuation half PENDING PHASE 3 |
| Peer utilisation | NOT APPLICABLE | B12d | Denominator below 4: 2 peers with transcripts (ARVIND, MAYURUNIQ), both confirmed substantive (2 of 2); GARFIBRES had zero transcripts |
| Overall | 82 | confidence.yaml | Set by redflag_coverage; band 75-89 normal |

REWORK check: Verifier A CONFIRMED CRITICAL 0; no acceptance rate below 60% on a denominator of 4 or more. REWORK not triggered.

## Acceptance rates and counts

| Verifier | Acceptance rate | CRITICAL | MAJOR | MINOR | Coverage |
|---|---|---|---|---|---|
| A, numerical (B12a) | 99 | 0 | 1 | 4 | numbers_checked 715 (mandatory 315 of 315 plus 400 sampled) of material_universe 1,415; 5 false positives struck under rule 5a |
| B, red flags (B12b) | 82 | 0 | 2 | 11 | 26 independent flags found; 11 material; 9 caught, 11 partially caught across all 26; promise delivery spot checks 5, confirmed 4, wrong 1 |
| C, framework, phase 1 scope (B12c) | 84.3 | 0 | 2 | 6 | Gate 0 26 rules (fails C-G05, C-G16, C-G25); Emerging Moat 25 rules (fails C-E03, C-E15, C-E19, C-E21, C-E23); valuation 0 rules, PENDING PHASE 3 |
| D, peers (B12d) | 100 | 0 | 0 | 3 | 2 peers audited, 2 substantive confirmed; claims all addressed; no verdict discipline fails |
| Total | | 0 | 5 | 24 | |

## Findings, sorted by severity

### CRITICAL

None. No verifier logged a CRITICAL finding.

### MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A | 08-promoter.md Section 4C CRISIL bullet and ERRATA bullet 2 | MISMATCH, source_fidelity true. Claimed "CRISIL rating 'BB- on 2026-01-21', then BB- Stable / A4+ on 2026-10-22". Source: CRISIL rationale 2026-10-22 p.2 rating history: 21-01-26 = Crisil B/Stable (Issuer Not Cooperating) long term and Crisil A4 (INC) short term; BB-/Stable and A4+ are the 2026-10-22 revision (p.1); 28-11-24 B/Stable; 20-09-23 B/Stable. The B08 YAML block is correct. Not a pillar or card input, so MAJOR. |
| 2 | B | Concall p.5; Prosp p.340, p.342, p.346, p.367 | MISSED (F7). Recurrence claim ("long-term sticky recurring business", "deeply embedded") contradicted by the prospectus: no long-term sale agreements incl. CFF; FY25 large A&D fabric order (2,045.75 INR mn) not re-ordered in FY26 (286.16); IR/ECW fabric 1,986.88 FY25 to nil FY26; new product types FY26 Nil. B05 credibility basis and Role 1 weights should treat A&D revenue as single-order lumpy, not recurring. |
| 3 | B | Q1 res p.1-2; Prosp p.261, p.263; Concall p.2 | MISSED (F11). CFO changed one month after listing and three days before the first call (Ratan Jha appointed 11 Aug 2026; prospectus CFO Kinnar Mehta, appointed 1 Jan 2025 after Naresh Patel resigned 9 Dec 2024); third CFO since Dec 2024; cessation filing NOT FOUND in corpus, PENDING LIVE VERIFICATION. |
| 4 | C | C-E15, emoat; rule: one improvement, one mechanism (B07 own control at rpt L105; CLAUDE.md) | em_score 17.5 with p.212 certificates in B2 and H3, p.210 automotive tape case in B2 and C1, p.210 parachute partner case in B2 and H2. Recomputed em_score 15.5 to 17.5; documented recount 14 on the exact p.212 duplicate alone; A4 SKU item (p.189) not recounted; Toray counted twice inside H2. Band MODEST in every allocation; UA EM >= 25 unmet in every allocation; carry em_score as range 15.5-17.5 into Pillar 3 until stage 7 assigns each item once. |
| 5 | C | C-E21, emoat; rule: 6C/6D on the INJECTED Gate 0 block (prompts/07 L202-205) | combined_assessment AVERAGE, reasoned from the pre-downgrade class. AVOID expected on the injected backward class: B07 itself rejects HIGH POTENTIAL (17.5 not 40+) and TURNAROUND (cash conversion not repaired), and MODEST gives no forward lift; the matrix text is not in prompts/07, so the orchestrator confirms whether AVOID + MODEST maps to AVERAGE. Feeds synthesis and the gate recommendation. |

### MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 6 | A | 08-promoter.md 3D Rating disclosure bullet; YAML adverse_findings item 3 | ANCHOR NOT FOUND, source_fidelity true. CRISIL non-cooperation 2026-01-21 cited at "CARE release 2026-04-02 p.4"; source is CARE release p.3 "Status of non-cooperation with previous CRA"; p.4 holds Annexure-1 and Annexure-2 only. Date is right, page is wrong. |
| 7 | A | 04-bizmodel.md 1B A&D Fabrics row; 1D WC intensity and Regulatory rows; 4A Structural row | ANCHOR NOT FOUND, source_fidelity true. "Payment follows inspection and acceptance" and "normal cycle 100 to 120 days" cited at Q2 Pres p.23; source is Investor Q&A 17 on Q2 presentation p.24. |
| 8 | A | 04-bizmodel.md anchor line under 1B | ANCHOR NOT FOUND, source_fidelity true. 66.21% of Industrial and Automotive revenue tied to exports cited at p.194; source is Prospectus p.198 (1,091.61 of 1,648.60 = 66.21%). |
| 9 | A | 07-emoat.md 1B Geography row | Period label imprecision, source_fidelity false. Sri Lanka 102.79 to 349.63 in a row timed FY24-FY26; Prospectus p.209: FY24 nil, FY25 102.79, FY26 349.63. |
| 10 | B | Concall p.6-8; Prosp p.340 | PARTIALLY CAUGHT (F3). Promise row 1 scored DELIVERED and accepts "Q1 typical" while both H1 quarters carry the 1,811.94 INR mn deferred order balance; the Q1 mix dodge is not classed as an evasion. |
| 11 | B | Prosp p.41; CARE p.2, p.4; Q1 res p.4, p.8 | PARTIALLY CAUGHT (F4). B05 3B records the US tariff release as fact; misses the 511.32 service contract and 639.57 CFF revenue in Q4 FY26, CARE turnover of 620 crore at 28 Mar 2026 (about 72 crore in the last three days, INFERENCE on basis), and the 37.3 crore 9M FY26 standalone gap. |
| 12 | B | Concall p.13; Prosp p.195; Q2 deck p.23 | PARTIALLY CAUGHT (F8). Licensed CFF systems noted but not flagged against Q&A 7 "we own the underlying ... know-how"; licence term, exclusivity and renewal NOT FOUND. |
| 13 | B | CARE p.3; Q2 res p.11-12 | PARTIALLY CAUGHT (F10). CARE maintenance capex benchmark of 10 crore a year unused (H1 FY27 44.1 crore = 4.4x); other non-current assets +308.64 INR mn not noted. |
| 14 | B | Concall p.13; Prosp p.41; Q2 res p.10-11 | SPOT CHECK WRONG (S5). "Debtors normalised" scored PARTIAL; against management's named benchmark (last couple of years of history, 26-33 days) Sep 2026 at 80.7 days is MISSED; delivery count becomes 2 delivered, 4 partial, 1 missed. |
| 15 | B | B05 2C, 4D | OVERSTATED. FY30 2,000 crore claim used as a MEDIUM red flag and over-promotion input although B05 found it NOT FOUND in corpus; keep as do-not-underwrite Step 1 item only. |
| 16 | B | Concall p.4, p.12; CARE p.2; Prosp p.123 | CALIBRATION. B05 2E calls company-authored repeats weak evidence and B06 Q1 calls the order-book refusal normal; the company posed and refused the questions itself, names a PO stage, CARE cites a healthy orderbook, the CEO said "four reported market segments" on the same call, and a KPI undertaking exists; F1 and F2 are stronger than framed; B05 HIGH rating survives. |
| 17 | B | Concall p.3; Prosp p.124, p.191 | MISSED (F13). Growth framing (FY20-FY26 revenue CAGR ~35%, PAT >70%, "7-8 times") omits FY26 revenue -11.2% and PAT -12.3%; 35% for six years is 6.05x. |
| 18 | B | Q1 deck p.4; Concall p.6; Q2 deck p.6; Q2 res p.10 | MISSED (F15). Q1 FY27 EBITDA 759 in the Q1 deck and "INR75.9 crores" on the call vs 768 in the Q2 deck; filed lines give 767.86; no restatement note. |
| 19 | B | Q2 res p.4, p.9, p.10; Q2 deck p.22 | MISSED (F22). Standalone Q2 PAT -20.8% QoQ vs consolidated -4.8%; consolidation adds 74.39 INR mn in Q2 vs 7.86 in Q1; Q&A gives consolidated only; source NOT FOUND. |
| 20 | B | CARE (announcement 2026-10-23) p.1, p.4 | MISSED (F24). CRISIL non-cooperation (press release 21 Jan 2026) vs the company's 23 Oct 2026 statement that it never mandated CRISIL; cross-reference stage 8. |
| 21 | C | C-G05, gate0; rule: ROE earliest year on closing net worth, stated (prompts/01 L32-33) | Claimed FY23 ROE NOT FOUND (no FY22 equity). Recomputed FY23 ROE 66.9% = PAT 37.22 Cr / closing equity 55.61 Cr (1.99 + 53.62, screener-data, B01 rpt L29); 4-year median ROE 61.6% vs 56.26%. A3 stays 5; no score or classification change. |
| 22 | C | C-G16, gate0; rule: M4 band ladder; 0 only for 3+ decline years (prompts/01 L109-111) | Claimed M4 = 0. Recomputed M4 = 1 on the fiscal-year reading; M4 = 3 on a TTM reading (TTM revenue 928.94 Cr vs FY25 779.0 Cr); moat score 14 or 16, grand total 73 or 75, moats present 3 (MODERATE) or 4 (STRONG). Classification unchanged: core 59 = AVERAGE; LIMITED downgrade = AVOID. |
| 23 | C | C-G25, gate0; rule: no qualitative judgments (prompts/01 L13) | analyst_note: "the pre-downgrade AVERAGE is the cleaner reading". Drop the judgment; keep the fact that AVOID = AVERAGE plus one LIMITED-history tier; the rule route for a post-IPO rebase is downstream position sizing (prompts/01 L152-154). No B01 value changes; it is the source of C-E21. |
| 24 | C | C-E03, emoat; rule: source anchor on every evidence item (prompts/07 L35-36) | At least 11 evidence items anchored only to B03 or B05 (e.g. B2 counter-evidence Customer 1 2,225.88 to 751.27 at B03 fact 2; G2 customer advances at B03 Phase 3B; F1 options at B03 Phase 2H; I1 executive pay at B03 Phase 5C). Re-anchor to prospectus or results pages, or mark as carried from B03/B05. Verifier A owns existence at source. |
| 25 | C | C-E19, emoat; rule: optionality register covers forward items scored 0 or resting only on claim/inference (prompts/07 L184-189) | 11 register rows; no A1 row. Add an A1 row: one-of-two global zero-porosity supplier and only-Indian Kevlar filament claims; converting evidence an independent manufacturer count or a customer qualification document naming sole or dual source. Monitoring coverage only; no score change. |
| 26 | C | C-E23, emoat; rule: evidence taxonomy applied to catalysts_12m (prompts/07 L29-34, L231) | Catalyst 2 (receivable days below 90, CFO above 50% of EBITDA) evidence_type DOCUMENTED; recomputed ANALYST INFERENCE: a B05-trigger threshold with no documented basis; management states a 100-120 day cycle (Q2 Q&A 17); catalyst 1 is mixed. Phase 3 checks stage 11 does not credit catalyst 2 as documented in Pillar 3. |
| 27 | D | B06 input gaps (peer transcripts) | Transcripts provided: 6 of 12 (GARFIBRES zero); input gap disclosed in B06, not a pipeline fault. |
| 28 | D | B06 Q8 (PARTIALLY VERIFIED) | B06 Q8 PARTIALLY VERIFIED rests on one peer (Mayur); permitted since no VERIFIED claimed, but flagged as single-anchor. |
| 29 | D | B06 Q5 | Sentence "where tariffs bit, supplier paid" rests on Arvind Jan p.8 only; Mayur reports no tariff impact. |

## Verifier positions recorded beside the findings

- Verifier B, credibility_grade_concur: "lower: C-. B05's C is the NO-CONCALL default, set before the contradictions it missed (no long-term agreements vs 'sticky recurring', prospectus Q4 attribution vs tariff story, post-listing CFO change); with two repeated evasions, a filed margin mislabel and the debtor benchmark miss, the evidence sits below the default".
- Verifier B, pipeline_flags_not_supported: none.
- Verifier B, coverage_basis: "material_caught counts PARTIALLY CAUGHT as had, per the schema note 'ones the pipeline already had'. Strict reading, CAUGHT only: 5 of 11 = 45%, below the 60% REWORK line; named for the operator, not applied by this verifier".
- Verifier C: recomputed_destination_pe and recomputed_decision blank (valuation PENDING PHASE 3); business_narrative rule 9 NOT IN SCOPE at phase 1; expectation ledger PENDING PHASE 3.
- Verifier D: substantive_unsupported none; unused_but_relevant none; claims_all_addressed true.
- Verifier A disposition (run log): the MAJOR CRISIL mismatch was corrected at source by the orchestrator against CRISIL rationale p.2; GATE HELD. The three MINOR anchor findings are listed for stage 10 to carry the correct anchors.
