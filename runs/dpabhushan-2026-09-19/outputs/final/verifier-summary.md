# DPABHUSHAN: verifier summary, phase 1

Run 2026-09-19. Run folder: runs/dpabhushan-2026-09-19. Verifier C covers the Gate 0 (B01) and Emerging Moat (B07) half only; its valuation half is pending phase 3.

## Confidence delta (phase 1, from outputs/blocks/confidence.yaml)

| Component | Score | Verifier | Basis |
|---|---|---|---|
| numerical_acceptance | 100 | A (B12a, claude-haiku-4-5) | 32 of 32 material Gate 0 scorecard figures clean |
| redflag_coverage | 79 | B (B12b, claude-opus-5) | 11 of 14 material flags had by the pipeline (7 caught + 4 partially caught); strict caught-only 7 of 14 = 50%, recorded, not the number of record |
| framework_adherence | 86.7 | C (B12c, claude-opus-5) | 52 of 60 Gate 0 + EM rules passed; valuation half pending phase 3 |
| peer_utilisation | 92 | D (B12d, claude-sonnet-5) | 11 of 12 substantive coverage points clean |
| overall | 79 | orchestrator | overall_set_by: redflag_coverage; band 75-89 normal |

Acceptance rates: A 100 | B 79 | C 86.7 | D 92. Counts: CRITICAL 0 | MAJOR 12 (A 0, B 8, C 3, D 1) | MINOR 18 (A 0, B 9, C 8, D 1). No REWORK trigger.

Coverage notes as the verifiers wrote them:
- A: "32 material scorecard figures checked (100% of Block A/B/C/D/E scorecard inputs, intermediates, outputs + grand total + classification)." Stage-report figures outside the scorecard (B02-B09) were not sampled (confidence.yaml).
- B: "Company transcripts 4 of 4 read in full; peer transcripts 3 of 12 in full, 9 of 12 by topic search." The annual reports were not read by Verifier B.
- C: "Gate 0 (B01) and Emerging Moat (B07) only; valuation audit pending phase 3."
- D: 3 peers audited, 12 substantive coverage points confirmed.

## CRITICAL

None. (Verifier B's independent list carried one CRITICAL item, R1, the four-call inventory-gain evasion. It was PARTIALLY CAUGHT by the pipeline and enters the consolidated findings as MAJOR F1.)

## MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | B (F1, R1) | B05 1A / 2C; Q2 FY26 call Nov p8; Q3 FY26 Jan p6, p8; Q4 FY26 May p6, p9; Q1 FY27 Jul p14, p18-p19 | PARTIALLY CAUGHT. Repeated evasion on inventory-gain share across four calls, recorded by B05 as transparency. Add to repeated_evasions; drop "High specificity". |
| 2 | B (F2, R2) | Q1 FY27 call, Manish Laddha, Jul p5, p14, p19 | MISSED. Q1 FY27 EBITDA 11.01% exceeds the CFO-stated normal gross margin of 10-11%; the stated split (10-15% inventory gain, majority making charges) cannot produce it. |
| 3 | B (F3, R3) | B06 Claim 6; Jul p4, p15; SENCO Aug-2026 p14; KALYANKJIL Aug-2026 p10, p14 | PARTIALLY CAUGHT. Customs-duty inventory windfall never mentioned; SENCO Rs 12-15 Cr and KALYANKJIL ~Rs 40 Cr quantified theirs. |
| 4 | B (F4, R5) | B05 1B; Q4 FY26 call, Vikas Kataria, May p7, p9, p12, p17 | MISSED. FY27/FY28 rupee guide Rs 4,800/5,500 Cr implies +17.9%/+14.6%, not the stated 20-25%; 25-30% also stated in the same call. |
| 5 | B (F5, R6) | B05 2A; Q3 FY26 call Jan p8, p9 | PARTIALLY CAUGHT. 10-15% growth told to one analyst, 25-30% "minimum" to the next, same call. |
| 6 | B (F6, R11) | B05 1C, 4A #2; Jan p7; May p6; Jul p6, p12 | PARTIALLY CAUGHT. Diamond revenue decline contradicts the mix explanation management gives for margin. |
| 7 | B (F7, R14) | B06 2C; Q1 FY27 call, Manish Laddha, Jul p7; KALYANKJIL Aug-2026 p8 | MISSED. FOCO pilot: company bears all expenses, franchisee receives the gold gain, counterparty unnamed; reverse of the KALYANKJIL model, yet B06 2C says it matches peers. |
| 8 | B (F8) | B05 4D #1 / FLAG-HEDGING-CONTRADICTION; B06 Claim 5 and Part 5; Nov p8; Jan p12, p14; May p5 | OVERSTATED pipeline flag. B05's first HIGH flag likely misreads a GML/leased-gold position as unhedged; transcripts show GML adoption began in FY26. Re-read AR Note 33.2.2(D) before synthesis. See disagreement D1. |
| 9 | C (F-G1) | B01 Block F, M11; screener-Data_Sheet.csv rows 11, 14-18 | M11 scored 3 on a rising selling % with FY26 missing; recomputed 1 (or 0 strict N/A). Moats present 6 -> 5, moat class FORTRESS -> STRONG. Classification AVERAGE unchanged. |
| 10 | C (F-E1) | B07 Section 3 H1; Section 4B row 1, 4C (R1) | Hallmarking formalisation credited twice (H1 2.0 + R1 3.0). One credit only; EM total 7.7. Class NONE unchanged. |
| 11 | C (F-E2) | B07 Section 2C | capex_embedded_growth_pct 23 rests on estimated capex (Jodhpur by analogy; unsited guided stores). Recomputed NOT FOUND at site level, or 4.2-5.0% on the Dahod bracket basis. |
| 12 | D | B06 Claim 4 / Part 5 Cross-Peer Hypothesis; KALYANKJIL-20260210-734a40ea-8d9f-420f-b381-e3f39c0f06e3.txt lines 710-720 | KALYANKJIL "we do not take any margin benefit... We are fully protected" attributed to the Nov-2025 call; the quote is in the Feb-2026 (Q3 FY26) transcript. Real quote, wrong quarter; the substantive point survives. |

## MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 13 | B (F9, R4b) | Q4 FY26 call May p6, p8, p12; Q2 FY26 Nov p12 | MISSED. CFO calls 6-6.5% EBITDA "consistently maintained" against FY26 7.61% and a 7-8% prior guide; promoter promises yearly margin gains in the same call. |
| 14 | B (F10, R7b) | Q4 FY26 call, Manish Laddha, May p15 | MISSED. QIP dilution of 5-8% cannot take the promoter from 75% to 65-68%. |
| 15 | B (F11, R12) | Q1 FY27 call, Manish Laddha, Jul p14; Q4 FY26 May p11 | MISSED. FY26 volume question dodged with industry framing instead of the company's -20% figure. |
| 16 | B (F12, R17) | Nov p12; May p4, p16; Jul p5 | MISSED. E-commerce told as already live (May) and as launched in Q1 FY27 (Jul); Rs 25-30 Cr profit on 3-5% of revenue implies a 9-18% channel margin. |
| 17 | B (F13, R18) | Q4 FY26 May p13-p14; Q1 FY27 Jul p16 | MISSED. Inventory days: Dhar Rs 100-125 Cr vs Rs 40-60 Cr per-store norm in the same answer; 4.7-5.0x turns called best in industry after a ~100-day close. |
| 18 | B (F14, R19) | Jan p11-p12; May p13; Jul p8 | MISSED. Store payback quoted on capex only (6-9 months) while inventory of Rs 40-60 Cr per store is excluded. |
| 19 | B (F15) | B05 2A promise-delivery row; Jan p15; Jul p5 | WRONG SPOT CHECK. B05 marks "4-6 stores around Diwali" as missed; the promise is Diwali 2026, not yet due. Should read "open, at risk". |
| 20 | B (F16) | B05 4D #6; Jul p5, p6 | OVERSTATED. SSSG flag, Q1 FY27 half: 52% SSSG vs 58% total growth is consistent. Q3 FY26 half stands. |
| 21 | B (F17) | B05 3C and 2A; May p15 | ATTRIBUTION. B05 names Kanishk Gupta on the guidance-cut question (Abhi Bilala only asked); 2A says no explanation was given (one was). |
| 22 | C (F-G2) | B01 Block F, M9; SENCO/PNGJL/KALYANKJIL-Data_Sheet.csv rows 11-13 | M9 marked PEER DATA NEEDED when the peer GM proxy was computable: peer median 19.79 (B01 set) / 13.16 (current set) vs DPABHUSHAN 10.28. Score 0 unchanged. |
| 23 | C (F-G3) | B01 Block F, M2/M5 | Stale peer set (MOTISONS). On SENCO/PNGJL/KALYANKJIL the EBITDA median is 7.62; M2 = 1 (was 0); M5 = 1 unchanged. |
| 24 | C (F-G4) | B01 data confidence tier | "10+ yrs full" defensible; ratio blocks run on FY24-FY26 only; a LIMITED tier would not change the final AVERAGE. |
| 25 | C (F-G5) | B01 Block E, E2 | E2 scored on a 1-year filed window (-0.23pp); 3-year screener window -0.11pp; score 3 either way. |
| 26 | C (F-E3) | B07 Section 5, adjusted total | D2 0.7 rounded up to 1; correct sum 9.7 (7.7 after F-E1). |
| 27 | C (F-E4) | B07 Section 3 / YAML completionist_recount | Completionist recount (7 DOC) does not reconcile with evidence_mix (documented 10). |
| 28 | C (F-E5) | B07 Section 6C, 6E | Core printed "69/?" (should be 69/100); FORTRESS label (should be STRONG); MOTISONS named (should be SENCO/PNGJL/KALYANKJIL). |
| 29 | C (F-E6) | B07 Section 5 D2 row; optionality register | Digital revenue claim sits in the register and also drives D2 0.7. Operator ruling needed; if register-only, D2 = 0 and total 7.0. |
| 30 | D | B06 Claim 5 | SENCO hedging "down from a historical 80-90%": the Feb-2026 transcript gives 80% for the last 2-3 years; 85-90% is a stated forward target. Direction and rough magnitude correct. |

Verifier A: 0 findings. One observation, not a finding: "One weak anchor noted (M3 FAT 54.5x does not reconcile to AR Net Block; report itself acknowledges metric unreliability; conclusion unaffected)" (B01 Block F, M3; B12a coverage_note).

Verifier B promise-delivery spot checks: 6 checked, 5 confirmed, 1 wrong (row 19). Credibility grade: B05 C; Verifier B "lower: C to D boundary".

Verifier C recomputed values (no decision change): Gate 0 core 69, moat score 22 (current peer set) / 21 (B01 set), moats 5, class STRONG, classification AVERAGE. EM 7.7, class NONE, capex_embedded_growth_pct NOT FOUND (4-5 on the Dahod bracket basis).

## Verifier disagreement set

Verifier A source-fidelity disagreement log: none. Verifier A raised no finding, so no downstream step conflicts with one.

Disagreements between verifiers and pipeline stages (open unless marked):

| ID | Point | Verifier position | Pipeline position | Status |
|---|---|---|---|---|
| D1 | FY26 AR Note 33.2.2(D): 42 kg unfixed gold (10 kg Gold Metal Loan + 32 kg Gold on Lease) at 31-Mar-2026, nil at 31-Mar-2025 | B (F8): OVERSTATED. GML adoption began in FY26 per the calls (Jan p14, May p5). "In a jeweller's book, unfixed gold loans are gold-denominated liabilities that offset inventory price risk. Reading 'unfixed' as 'unhedged' may invert the note." Verifier B did not read the AR. | B02 rank 4 (RED), B03 (verified, Phase 2), B04 (Section 2A, 3B) read it as a new unfixed/unhedged exposure contradicting the natural-hedge framing; B05 ranks it HIGH #1 (FLAG-HEDGING-CONTRADICTION); B06 grades the hedging claim contradicted. | OPEN for Halt 1 re-read. Recorded, not resolved (confidence.yaml). |
| D2 | FOCO structure vs peers | B (F7): reverse of the KALYANKJIL model | B06 2C: "matching DPABHUSHAN's own pivot toward FOCO" | Verifier position carried into the gate recommendation. |
| D3 | Credibility grade | B: C to D boundary | B05: C | Both carried. |
| D4 | Moat class and EM score | C: STRONG (5 present); EM 7.7; capex growth NOT FOUND | B01: FORTRESS (6 present); B07: EM 10, capex growth 23% | Verifier values carried; classifications unchanged. |
| D5 | KALYANKJIL "fully protected" quote date | D: Feb-2026 transcript | B06: Nov-2025 | Anchor corrected to Feb-2026; substance unchanged. |

D1 source text, retrieved at synthesis for the Halt 1 re-read (quote only; no ruling):
- FY26 AR Note 33.2.2(D), PDF p.101 left half (printed p.196): "To mitigate this risk, the Company enters into Gold Metal Loan (GML) arrangements and Gold on Lease agreements with bullion banks. Under these schemes, the price of gold is fixed at the time of sale or within a contractually permitted window, effectively creating a natural hedge against market fluctuations." Then, under the heading "Unhedged/Unfixed Exposure": "As of the reporting date, the details of unfixed gold liabilities that are exposed to price risk are as follows", with "Gold Metal Loan 10.00 Kgs" and "Gold on Lease 32.00 Kgs" at 31-Mar-2026 and "-" at 31-Mar-2025.
- FY26 AR accounting policy "Embedded Derivative", PDF p.86 right half: "The Company enters into purchase gold contract, in which the amount payable is not fixed based on gold price on the date of purchase, but instead is affected by changes in gold prices in future. Such transactions are entered into to protect against the risk of gold price movement in the purchased gold. Accordingly, such unfixed payables (gold Loan, gold on lease) are considered to have an embedded derivative."
- The note's own heading supports the pipeline's label. The note body describes the 42 kg as liabilities. The policy text states such payables exist "to protect against the risk of gold price movement". Both readings have a textual basis. The operator rules at Halt 1.
