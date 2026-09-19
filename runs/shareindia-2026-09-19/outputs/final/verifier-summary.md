# SHAREINDIA: verifier summary (Phase 1, run 2026-09-19)

## Confidence delta (phase 1)

| Component | Value | Source | Basis |
|---|---|---|---|
| numerical_acceptance | 100 | B12a | 80 material figures checked; 0 MISMATCH, 0 ANCHOR NOT FOUND, 0 UNANCHORED |
| redflag_coverage | 50 | B12b | material_found 10, material_caught 5 (3 caught + 2 partial); 30 on full catches only |
| framework_adherence | 84.7 | B12c | 61 passed / 72 checked (Gate 0 47 + EM 25); valuation portion PENDING PHASE 3 |
| peer_utilisation | 91.7 | B12d | 11 substantive / 12 peer transcripts provided |
| overall | 50 | min of applicable | overall_set_by: redflag_coverage; not_applicable: none |
| band | < 60 | orchestrator Section 5 | forced REWORK |

Acceptance rates as reported by each verifier: A 100 | B 50 | C 84.7 | D 92 (block acceptance_rate; peer_utilisation 91.7 is the orchestrator's 11/12).

Orchestrator note (confidence.yaml): B12b coverage_basis text says "1 CRITICAL, 9 MAJOR" and "30% on full catches only", while critical_count is 0 and major_count 7. The acceptance_rate field (50) is used as reported. On the full catch reading (30) the band is the same.

Verifier A identity check: no CRITICAL rows in B12a (findings: []); nothing to strike. Source fidelity findings: none.

Counts: CRITICAL 0 | MAJOR 10 (B 7, C 2, D 1) | MINOR 29 (B 15, C 8, D 6) | A 0.

## CRITICAL

None. (B12a 0, B12b 0, B12c 0, B12d 0)

## MAJOR

| # | Verifier | Location anchor | Source anchor | Note |
|---|---|---|---|---|
| 1 | B | B05 1C/2A/4A | Q3 [page 10] L455-469; Q4 [page 8] L270-272, [page 12] L424-425; Q1 [page 5] L193-198 | MTF trigger scored on track / no slippage; target restated each quarter, book +3% in 6 months |
| 2 | B | B05 1B/2A | Q4 [page 16] L589-593, [page 17] L605-607; Q1 [page 10] L408-409 | Q4 profit mix target misrecorded (55/45 profit, not 60/40); flat ~52% prop profit share not flagged |
| 3 | B | B05 absent | Q4 [page 4] L152-154; Q1 [page 3] L114-117, [page 10-11] L417-422 | Fair value contribution to Q4 weakness and Q1 record consol PAT not identified |
| 4 | B | B06 Q3 | SMCGLOBAL-2026-07-31 [page 7] L271-272; CHOICEIN-2026-02-11 [page 6] L233-236; ANGELONE-2026-01-21 [page 17] L707-708 | False peer silence on MTF; peer MTF outgrowth missed |
| 5 | B | B06 Q5 | Q4 [page 7-8] L259-260; Q1 [page 13] L511; SMCGLOBAL-2026-02-09 [page 6] L218-222; SMCGLOBAL-2026-07-31 [page 10] L352-355 | SMC algo platform contradicts Share India algo uniqueness claim; not tested |
| 6 | B | B06 2C | Q4 [page 8] L287-290; Q1 [page 7] L287-289; CHOICEIN-2026-02-11 [page 6] L224-236; CHOICEIN-2026-08-17 L487-498; ANGELONE-2026-01-21 [page 12] L544-546, [page 17] L727 | Tier 3 "no supply / vacuum" claim not set against Choice/Angel evidence (partially caught) |
| 7 | B | B05 1C/2A/2B | Q3 [page 5] L237-245, [page 6] L272-276, [page 8] L366-369; Q4 [page 6-7] L222-238, [page 9] L312-313, [page 11] L389-401; Q1 [page 5] L202-208, [page 6-7] L255-260 | Five for five slip pattern on Q3 FY26 milestones not stated (partially caught) |
| 8 | C (G-1) | 01-gate0.md L236-242; B01 moats_confirmed/moat_class | prompts/01-gate-0-pipeline.md L109-111 | M4 scored 3 on "fully recovered" band though FY26 revenue is 99.1% of FY24 peak; band gaps resolved upward here but downward for M8/M9. Recomputed: M4 1; alone flips FORTRESS to STRONG |
| 9 | C (G-2) | 01-gate0.md L284-286; B01 data_notes line 31 | prompts/01-gate-0-pipeline.md L27, L33-38, L19-21 | M12 uses screener Working Capital Days, which is not Rec+Inv-Pay (FY16 debtor days 91, screener WC days 29); inventory/payable days blank except FY25. Recomputed: M12 0; with G-1 moats_confirmed 4, moat_class STRONG, moat_score 15 (with G-4) |
| 10 | D | B06 Part 2B (industry_cross_read.pricing_inputs) | SMCGLOBAL-2026-05-08 p.11, lines 342-350 | Claimed p.2 proactive "opening remarks"; actually a Q&A answer (Himanshu Gupta) to a narrower analyst question. Quote verbatim accurate; anchor and characterisation wrong, overstating how voluntarily SMC disclosed the RBI driven funding parallel. Does not touch any Part 1 verdict |

## MINOR

| # | Verifier | Location anchor | Source anchor | Note |
|---|---|---|---|---|
| 11 | B | B05 1A | Q3 [page 5] L237-242; Q4 [page 6] L222-228; Q1 [page 6-7] L255-260 | Wealth distribution slip not flagged |
| 12 | B | B05 1C | Q4 [page 14] L519-521, [page 20] L722-723, [page 21-22] L771-779; Q1 [page 4] L147-149 | RBI tone shift not read; 25-30% misstatement (transcript ~20%) |
| 13 | B | B05 1B/2A | Q1 [page 11] L438-458 | Enshrine acquisition not flagged (turnover vs price, capital into own use property) |
| 14 | B | B05 absent | Q3 [page 8] L398-399; [page 9] L402-409 | Insurance speaker contradiction missed |
| 15 | B | B05 absent | Q4 [page 4] L139-148 | Impossible Q4 opening numbers missed (Q4 rev 383 vs FY 395; EPS 17.6) |
| 16 | B | B05 absent | Q3 [page 5] L213-221 | Retail client stagnation missed |
| 17 | B | B05 absent / B06 2E | Q3 [page 7] L305-331; Q4 [page 18] L655-665 | NBFC NIM/NPA missed; B06 2E overstated |
| 18 | B | B05 1A | Q4 [page 7] L246-248; Q1 [page 6] L221-226 | Share India Cred run rate not checked |
| 19 | B | B05 1C | Q4 [page 7] L229-235; Q1 [page 5] L202-204 | PMS metric broadening and launch quarter inconsistency missed |
| 20 | B | B05 1B | Q3 [page 4] L152-153; Q4 [page 10] L353-356 | Margin guidance restatement missed (43/24 to 38/22) |
| 21 | B | B05 1B | Q4 [page 19] L670-697; Q1 [page 7] L282-285 | Branch economics called first time quantified; Q4 already quantified |
| 22 | B | B05 absent | Q4 [page 11-12] L402-425 | MTF spread question deflection missed |
| 23 | B | B05 3D | Q3 [page 5] L222-224; Q4 [page 8-9] L294-298; Q1 [page 5] L213 | Institutional active vs empanelment counts merged |
| 24 | B | B05 2C/3B | Q4 [page 17] L605-607; inputs/other Q2FY26 [page 13] L526, L535 | Quarter/topic attribution errors (52%/49%; media hype) |
| 25 | B | B06 Part 5/2A | ANGELONE-2026-04-22 [page 12] L535-572 | "Stagnate" misattributed to Angel One CFO |
| 26 | C (G-3) | 01-gate0.md L75-80 | prompts/01-gate-0-pipeline.md L27, L33-38, L67-68 | B4 uses the same substituted WC Days; report also misstates debtor days as blank FY16-FY24. Strict: B4 0, Block B 2, core 41, still AVERAGE; receivable only reading keeps 5 |
| 27 | C (G-4) | 01-gate0.md L250-253 | prompts/01-gate-0-pipeline.md L19-21, L117-119 | M7 player count taken from general market knowledge, not provided data. M7 0; no moat count effect |
| 28 | C (G-5) | B01-gate0.yaml line 39 | internal consistency | analyst_note says six moat tests score 0; five do (M5, M6, M8, M9, M11) |
| 29 | C (E-1) | 07-emoat.md L151, L208 | prompts/07-emerging-moat-pipeline.md L172-173 | H1 scored 1.0x while the beneficiary link is inference/NOT FOUND. Recomputed 0.5 |
| 30 | C (E-2) | 07-emoat.md L128, L212 | prompts/07-emerging-moat-pipeline.md L172-173 | I2 sacrifice is the scanner's inference, scored at claim tier. Recomputed 0.5; total 8.9, band unchanged |
| 31 | C (E-3) | B07-emoat.yaml line 30 | CLAUDE.md NEVER: NOT FOUND is the only valid fill | capex_embedded_growth_pct carries 0 for a not computable figure. Recomputed NOT FOUND |
| 32 | C (E-4) | 07-emoat.md L224-237; B07 optionality_register | prompts/07-emerging-moat-pipeline.md L183-196 | Register omits claim only rows C1, D1 and claim items Silverleaf HFT, Cred Rs 500 Cr target, third party country expansion. Add 5 rows |
| 33 | C (E-5) | B07-emoat.yaml line 17 | prompts/07-emerging-moat-pipeline.md L224 | em_score rounded to 10; adjusted total is 9.6 (verifier 8.9) |
| 34 | D | B06 Part 1 Q1 evidence | SMCGLOBAL-2026-02-09 | Claimed p.4; p.6 by the file's "Page N of 8" footer. Quote verbatim accurate; anchor drift only |
| 35 | D | B06 Part 1 Q2 evidence | ANGELONE-2026-04-22 | Claimed p.6; p.7 by the "Page N of 21" footer. Quote verbatim accurate; anchor drift only |
| 36 | D | B06 Part 1 Q3 evidence | ANGELONE-2026-01-21 | Claimed p.17-18; roughly p.16 by one convention; two page marking conventions disagree by about one page. Source extraction ambiguity, not a clear pipeline error |
| 37 | D | B06 Part 2E (restricted basket quote) | ANGELONE-2026-07-21 | Claimed p.19-20; p.24 by the "Page N of 25" footer. Largest single anchor drift (~4-5 pages); quote exact and correctly attributed |
| 38 | D | B06 Part 2C (800 branch quote) | CHOICEIN-2026-08-17 | Claimed p.13; p.12 by bracket page markers. Companion "210-350 branches" quote correctly on p.13 |
| 39 | D | B06 Part 2 (SMCGLOBAL Q2 FY26, CITED-ONLY) | SMCGLOBAL-2025-11-07 lines 313-314 | Call also discloses NBFC GNPA 3.6% / NNPA 2.5%, not reused in Part 2E. Industry context miss; the Part 2E point is already made via other quarters, not claim critical |

## Verifier B: pipeline claims not supported

| Verifier | Location anchor | Verdict | Note |
|---|---|---|---|
| B | B06 Q3 | NOT SUPPORTED | "no MTF product line disclosed by either [SMC, Choice]" is false (SMCGLOBAL-2026-07-31 [page 7] L271-272; CHOICEIN-2026-02-11 [page 6] L233-236) |
| B | B06 Part 5 | NOT SUPPORTED | "stagnate" is the analyst's word, rebutted by the CEO (ANGELONE-2026-04-22 [page 12] L535-572) |
| B | B05 3B | NOT SUPPORTED as attributed | "media hype" quote is Q2 FY26 context, on weekly expiries (inputs/other Q2FY26 [page 13] L526, L535) |
| B | B05 1C | OVERSTATED | RBI impact "25-30%"; transcript ~20% (Q4 [page 20] L722-723) |
| B | B06 2E | OVERSTATED | Share India lending "never discussed in asset quality terms"; Q3 NBFC NPA Q&A (Q3 [page 7] L322-331) |

## Verifier B: promise delivery spot checks and credibility

Spot checks: 5 checked, 4 confirmed, 1 wrong. The wrong row is the MTF Rs 900-1,000 Cr two year target, scored "Delivered (on track)" by B05; verifier reading "Off track; target restated" (Q3 [page 10] L455-457; book 457 -> 424 -> 470).

Credibility grade: "concur - C holds, but B05's 'Good' operational-delivery sub-rating is overstated: MTF is off its glide path and all five dated Q3 FY26 new-initiative milestones slipped" (B12b credibility_grade_concur).

## Verifier C: scope and recompute

Scope: phase 1 (Gate 0 B01 + Emerging Moat B07); valuation audit, expectation ledger and business understanding narrative pending phase 3 / stage 13, not audited. Recomputed decision: concur, Gate 0 AVERAGE, EM NONE, combined AVERAGE all survive.

## Verifier D: coverage

Peers audited 12; substantive confirmed 11; substantive unsupported none; claims all addressed true; verdict discipline fails none. Unused but relevant: SMCGLOBAL Q2 FY26 (2025-11-07) NBFC GNPA 3.6% / NNPA 2.5% (lines 313-314).
