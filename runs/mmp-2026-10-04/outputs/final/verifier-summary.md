# MMP Industries Ltd (NSE: MMP): verifier summary, phase 1

Run 2026-10-05, folder runs/mmp-2026-10-04. Verifiers A, B, D and the Gate 0 plus Emerging Moat half of C. Verifier C's valuation half runs in phase 3.

## Confidence delta (phase 1)

| Component | Value | Source | Note |
|---|---|---|---|
| numerical_acceptance | 96 | B12a run 1 (96%, 730 checked, mandatory 175 of 175); B12a run 2 (96.6%, 411 checked, mandatory 187 of 187) | lower of the two carried |
| redflag_coverage | 67 | B12b | 6 of 9 material fully caught (strict); 100 with partials credited |
| framework_adherence | 95.6 | B12c run 2 (86 of 90 rules) | Gate 0 and EM half only; run 1 was 83.7 |
| peer_utilisation | 100 | B12d | 8 of 8 peer transcripts used substantively; ARFIN none collected |
| overall | 67 | min of the four | set by redflag_coverage; band 60 to 74 |

Not applicable: none. REWORK check: no CONFIRMED Verifier A CRITICAL; no acceptance rate below 60% on a denominator of 4 or more (OR-29).

## Acceptance rates

| Verifier | Run | Rate | Denominator | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| A (numbers, source fidelity) | run 1 | 96 | 730 checked; about 1,100 material universe; mandatory 175 of 175 | 0 | 7 | 9 |
| A | run 2 (Gate 0 tier and stage 7 run 2 sample) | 96.6 | 411 checked; mandatory 187 of 187; sample 224 of about 260 | 0 | 1 | 4 |
| B (red flags, independent read) | single | 67 | 9 material of 27 listed | 0 | 2 | 16 |
| C (Gate 0 + EM) | run 1 | 83.7 | 86 rules (50 Gate 0, 36 EM) | 1 | 4 | 4 |
| C (Gate 0 + EM) | run 2 | 95.6 | 90 rules (54 Gate 0, 36 EM) | 0 | 3 | 3 |
| D (peer utilisation) | single | 100 | 3 peers, 8 transcripts | 0 | 0 | 4 |

False positives struck by Verifier A: 6 in run 1, 3 in run 2.

## Remediation cycle

Trigger. Verifier C run 1 F1 (CRITICAL) and Verifier A run 1 row 7 (MAJOR, source fidelity) hit the same item. Gate 0 E4 used standalone contingent liabilities (Note 47, 7,133.72 L) over consolidated net worth and stated that no consolidated note existed. AR26 [page 241] Note 51 gives 445.72 L. Gate 0 read core 39, AVOID.

Cycle 1 of 1. Stage 1 re-ran with AR25 and the three peer Data_Sheets. Stage 7 re-derived 6C to 6E. Verifier A re-audited the mandatory tier, and Verifier C re-audited its phase 1 half. Result: core 54, AVERAGE; combined class AVOID to AVERAGE. No second cycle ran (cap on remediation cycles). Open MAJORs go to Halt 1.

### Run 1: Verifier A (B12a-run1), sorted by severity, with dispositions

| Sev | SF | Location | Note (verifier) | Disposition |
|---|---|---|---|---|
| MAJOR | yes | 04-bizmodel.md 1D table, row "Regulatory moat or burden" | Anti-dumping duty carried as Rs 619-873 per MT; source is US$619-$873/MT (Q1 FY27 deck [page 25]). Currency unit trap. | Corrected in place by the orchestrator to US$619-873 per MT (run-log 2026-10-05) |
| MAJOR | yes | 05-concall.md Section 3C table row 2 | Analyst quoted as "Rs 150 Cr capex and Rs 18 Cr interest"; May-26 call [page 15] states INR 13 Cr finance cost on INR 180 Cr gross borrowing, capex INR 30 + 15 + 90 Cr, CFO INR 53 Cr. | Corrected in place by the orchestrator to the call [page 15] figures |
| MAJOR | yes | 09-tam.md 5E output card | "25.6x P/E" unanchored and material; no source in the run reproduces it; screener Data_Sheet gives 36.8x on FY26 PAT and about 22.8x on trailing PAT. | Removed by the orchestrator; stage 11 owns the multiple |
| MAJOR | yes | B01-gate0.yaml data_notes (E4); 01-gate0.md Block E, E4 | Standalone numerator over consolidated denominator; consolidated Note 51 exists at AR26 [page 241], 445.72 L, 1.3%. | Fixed by stage 1 run 2: E4 on Note 51, 1.29%, score 5 |
| MAJOR | no | 05-concall.md Section 1B, "Reading the FY27 pair against Q1 (derived)" | +16.8% to +20.8% should be +18.1% to +24.5% from the report's own inputs. | OPEN; report not corrected; synthesis does not carry the printed figure |
| MAJOR | no | 09-tam.md 5E output card | EBITDA CAGR 12.9% recomputes to 13.8%. | Corrected in place by the orchestrator to 13.8% |
| MAJOR | no | 09-tam.md 1B and B09 FLAG-MGMT-CLAIM-NOT-A-TAM | Deck endpoints imply 8.9%, not 8.1%; finding survives with a larger gap. | OPEN; report and block still read 8.1%; synthesis does not carry it |
| MINOR | yes | 03-ardeep.md Phase 2 triple pass table, rank 11 | Gratuity DBO 611.39 / 349.40 is on AR26 [page 146], not p.147. | Left for the dossier to cite at the correct marker |
| MINOR | yes | 05-concall.md 2A row 9, 2D row 1; B05 FLAG-INSURANCE | 76 Mn exceptional is on Q4 PR [page 6], not p.3. | Left for the dossier to cite at the correct marker |
| MINOR | yes | 05-concall.md 1B, 2C, 3C, 3D; B05 yaml (May-26 call anchors) | Adani Renewables on [page 14]; conductor and wire rod per tonne on [page 13]; powder and foil on [page 20]. | Left for the dossier to cite at the correct marker |
| MINOR | yes | 07-emoat.md B1 table and 2D | Wire rod 10,000-12,000 per tonne on call [page 13]; one third export target on [page 23]. | Not fixed in stage 7 run 2; re-flagged in run 2 |
| MINOR | yes | 07-emoat.md Q1 FY27 PR anchors (1A, 1B, 3, 4A, catalysts) | Mixed anchor convention; insulator ramp and approvals on [page 5], lidding foil on [page 4], Star forging on [page 6-7]. | Not fixed in stage 7 run 2; re-flagged in run 2 |
| MINOR | yes | 09-tam.md 2, 3A, 4C (call anchors, MD&A pages) | Rs 150-9,000 and Deccan/Olectra on call [page 11]; 220 kV focus on [page 17]; MD&A markers 49-55. | Left for the dossier to cite at the correct marker |
| MINOR | no | 05-concall.md 1B/3C; B05 peer_questions; 06-peers.md Q8 | "About Rs 150 Cr" capex has no source; stages give 137-145, 143-155 and about 150. | OPEN; synthesis does not carry it |
| MINOR | no | 05-concall.md 2B; B05 input_gaps and analyst_note | 20-25% FY27 figure is printed in the Q4 FY26 deck [page 9]; "known only from the call" is wrong. | OPEN; synthesis cites the deck |
| MINOR | no | 09-tam.md FLAG-INSULATOR-PEAK-ABOVE-SHARE-RULE vs body | Flag says 7.0-7.2%; body and arithmetic give 7.0-7.5%. | OPEN; synthesis uses 7.0-7.5% |

### Run 1: Verifier C (B12c-run1), sorted by severity, with dispositions

| Sev | ID | Location | Note (verifier) | Disposition |
|---|---|---|---|---|
| CRITICAL | F1 | B01 Block E, E4 | Standalone Note 47 7,133.72 L over consolidated NW = 20.6%, score 1; consolidated Note 51 (AR26 [page 241]) 445.72 L = 1.29%, score 5; core 39 to 43; AVOID to AVERAGE under every reading. | Fixed by stage 1 run 2 (E4 = 5) |
| MAJOR | F2 | B01 Block B (B2, B3, B4) | FY24 capex and payables are in AR25 [page 154], [page 156]; FY24 to FY26 meets the rule 6 minimum; Block B 5 to 14 or 10. | Fixed by stage 1 run 2 (Block B 14) |
| MAJOR | F3 | B01 ROCE formula (G03) | Equity plus reserves plus borrowings proxy replaced the fixed EBIT/(TA-CL); fixed formula FY24 to FY26 14.74 / 16.31 / 12.91%; Block A 4 to 9 or 2. MINOR consequence on M3 (G31). | Fixed by stage 1 run 2 (fixed formula, Block A 9); proxy admissibility left as an open ruling |
| MAJOR | F4 | B01 E2 (G26) | 3 year start point NOT FOUND; rule 5 gives 0, not 3. | Fixed by stage 1 run 2 (E2 = 0) |
| MAJOR | F5 | B01 M2, M5, M9 (G30, G33, G37) | Three peer Data_Sheets exist; M2 1, M5 3, M9 3; moats 0 to 2; NONE to MODERATE. | Fixed by stage 1 run 2 (moat 12/60, MODERATE) |
| MINOR | F6 | B01 C1-C4, M3, M11 lines | Lines lack inline anchors. | Not re-raised in run 2 |
| MINOR | F7 | 01-gate0.md end | Report ends with a 6 key stub, not the full block. | Not re-raised in run 2 |
| MINOR | F8 | B07 G1, G2, B2, 1A; E1 | Evidence anchored to upstream blocks; E1 location unanchored. | Fixed in stage 7 run 2; residual re-raised as run 2 F6 |
| MINOR | F9 | B07 I2 test | I2 omits E2 and H2; I2 = 0 survives. | Fixed in stage 7 run 2 (all three Moderate moats tested; I2 stays 0) |

### Run 2: Verifier A (B12a-run2), sorted by severity

| Sev | SF | Location | Note (verifier) | Disposition |
|---|---|---|---|---|
| MAJOR | yes | 01-gate0.md Block E, E4 line; B01 yaml data_notes E4 | "Capital commitments 7,621.61 L" is the A+B total; AR26 p.241 Note 52: capital 5,642.27 L, other 1,979.34 L, total 7,621.61 L. Not an E4 score input. | Corrected in place by the orchestrator (label and value) |
| MINOR | yes | 07-emoat.md Family H, H2 table row 3 and I2 table H2 row | Toyo 74% cited to AR26 p.31, p.54; AR26 p.54 states only MMP's 26%; 74.0% is at Q1 FY27 deck p.11 and p.22. | OPEN; anchor only, figure exists in the deck |
| MINOR | yes | 07-emoat.md Family B, B1 note | Wire rod 10,000-12,000 per tonne cited to call p.20; it is on [page 13]. | OPEN; anchor only |
| MINOR | yes | 07-emoat.md and B07 yaml page anchors | Q1 FY27 PR lidding foil p.4, approvals and ramp p.5, solar p.6; call one third exports [page 23]; AR26 7.00% preference p.118; deck cash flow table p.30. | OPEN; synthesis cites corrected markers where used |
| MINOR | no | 01-gate0.md LBF1, LBF4, alternative reading; 07-emoat.md G1 | Rounding from rounded intermediates: 134 bps not 135; 12.52 Cr not 12.53; 12.83% not 12.85%; 18,452.45 L not 18,452.46 L. No score change. | OPEN; synthesis uses 12.52 Cr and about 1.3 points |

### Run 2: Verifier C (B12c run 2), sorted by severity

| Sev | ID | Location | Note (verifier) | Disposition |
|---|---|---|---|---|
| MAJOR | F1 | B01 Block B (B2, B3); data_notes capex line; block_b_trend; core_score | Capex should include CWIP increase and capital advances (AR25 p.156; AR26 p.173); FCF 0.43 / 4.76 / -2.50 Cr; B 10; core 50; AVERAGE. | OPEN; carried to Halt 1 |
| MAJOR | F2 | B01 Block F M9; moat_score; moat_class; grand_total | GM proxy net of change in inventory (same basis as B01 EBITDA): MMP 22.00%, median 18.44%, gap 3.56 points; M9 1; THIN; moat 10; grand 64; AVERAGE. | OPEN; carried to Halt 1 |
| MAJOR | F5 | B07 2C, capex_embedded_growth_pct, FLAG-CAPEX-FUNDING, 6E | Solar is claim only; documented capex under execution is wire rod 20-25 Cr; 7.8-9.7%, midpoint 8.7%; keep 20.4 as upper bound. | OPEN; carried to Halt 1 |
| MINOR | F3 | B01 LBF3, Block A, FLAG-GATE0 reason | Ex exceptional FY26 EBIT 63.14 Cr, ROCE 15.26%; 2.35 of the 3.40 point fall is the one time loss; add the sensitivity, do not rescore. | OPEN; synthesis shows the sensitivity |
| MINOR | F4 | B01 LBF4, Block B caveat, open ruling table | Ex short term borrowing reading: Block B 7, deal breaker 2 trips (max GOOD, not binding), core 47; add to the open ruling table. | OPEN; synthesis shows the reading |
| MINOR | F6 | B07 2A solar row, F2 table, 6D, G1, 2A MEPL funding, C1 | Five items anchored to upstream records or unpaged notes; give source page or NOT FOUND. | OPEN; no score effect |

Run 2 open rulings raised (Verifier C): rule 6 scope, ROCE proxy admissibility, confidence tier basis. Carried to Halt 1, not ruled here.

## Verifier B (B12b), sorted by severity

Credibility grade: concur, C holds. Promise and delivery spot checks: 6 checked, 5 confirmed, 1 wrong.

| Sev | Location | Note (verifier) |
|---|---|---|
| MAJOR | B05 2A, 4D | Foil conversion utilisation flat 45-50% (Jul 2022) to about 45% (May 2026) not paired; four year stall missing from tracker and red flags (C22 [page 13], [page 6]; C26 [page 16], [page 21]) |
| MAJOR | B05 2A, FLAG-FUNDING | 2022 pledges of 5x asset turn, about 27% gross margin in two years and FCF positive in FY24 absent from tracker (FY24 GM 22.3%, FY26 20.5%; CFO plus CFI FY26 -1.6 Cr derived); June 2026 ECLGS working capital approval not recorded (C22 [page 10], [page 15]; DECK-MAY [page 28], [page 30]; BM-JUN) |
| MINOR | B05 2C, 3C, red_flags | Inventory gain scored as transparency; PR commentary omits it; 2022 hedging pledge untracked (PR-Q4 [page 3]; PR-Q1 [page 3]; C22 [page 12]) |
| MINOR | B05 input_gaps, analyst_note | Q4 FY26 deck marked NOT FOUND but is in inputs/presentation and states about 20-25%; "appeared only in a footnote" is wrong (DECK-MAY [page 9]; DECK-AUG [page 9]) |
| MINOR | B05 2C | CFO did not restate 20-25% on the call; the line is an asterisked post call insertion worded "reiterates" (C26 [page 20]) |
| MINOR | B05 repeated_evasions | Overstated for 2022: CFO gave GM about 27% and 5x asset turn; 2026 refusal beside same call segment percentages not drawn (C22 [page 10]; C26) |
| MINOR | B05 red flag MEDIUM approvals | Overstated: "several boards" backed by PR-Q3 and PR-Q1; real contradiction is the only named approval (33 kV or below) sitting in the band the MD calls non focus (PR-Q3 [page 4]; PR-Q1 [page 5]) |
| MINOR | B05 2A row 8 | Two part AR25 MEPL promise half scored DELIVERED; full capacity by end FY26 missed; should be PARTIAL (tally 6/3/9) (AR25 [page 18]; PR-Q4 [page 2]) |
| MINOR | B05 2B Positive | Fire quantification credited without testing AR25 "all customer demands fulfilled" or deck 40-50 vs 45-50 (AR25; DECK-MAY) |
| MINOR | B05 1B, guidance | "Maiden" dividend recorded as FACT; dividends paid FY25 and FY26 (AR26; AR25) |
| MINOR | B05 1B, T6, capex sum | Wire rod capex stale at INR 13-15 Cr vs INR 20-25 Cr in Aug deck; SPV switch unflagged (DECK-AUG [page 9]; AR26) |
| MINOR | B05 1B powders | "Largely volume" recorded without MD value mix statement or capacity ceiling (C26) |
| MINOR | B05 2E | 2022 email deferrals and "do not have that data" not logged (C22) |
| MINOR | B05 3C | Analyst misquoted as Rs 18 Cr interest and Rs 150 Cr capex; call says INR 13 Cr finance cost on INR 180 Cr gross borrowing, capex 30+15+90 (C26 [page 15]) |
| MINOR | B05 3B | Pass through tone shift not compared with 2022 7-10 day settlement (C22 [page 17]; C26 [page 18]) |
| MINOR | B05 1C, 4D | Aug deck copy forward of Q4 exceptional bullet and header, and PR-Q3 insulator unit slip, missing from disclosure control evidence (DECK-AUG; PR-Q3; PR-Q4) |
| MINOR | B05 dropped_triggers | Security printing foil still targeted in Aug deck footnote; "dropped" is PR only (DECK-AUG) |
| MINOR | B05 2E note | 2022 "first earnings call" was said by the CMD, not only a participant (C22 [page 3]) |

Items the pipeline missed (all MINOR, listed by Verifier B):

| Sev | Item | Anchor |
|---|---|---|
| MINOR | Fire messaging: AR25 says all customer demands were fulfilled during the suspension; FY26 messaging claims INR 45-50 Cr revenue loss and INR 11-12 Cr PAT effect; deck shows 40-50 and 45-50 ranges | AR25; PR-Q4 [page 3]; DECK-MAY |
| MINOR | CFO says FY27 powder and foil growth is largely volume; MD says value added grades within same capacity; powder 80%, rolling 80-85%, no capex for 2 years | C26 [page 16], [page 18] |
| MINOR | Wire rod capex INR 13-15 Cr restated as INR 20-25 Cr in Aug 2026 deck; SPV moved from MMP Alutech to MMP Cables | DECK-AUG [page 9]; AR25; AR26 |
| MINOR | "Maiden" dividend label false; dividends paid INR 381.04 L (FY25) and INR 508.05 L (FY26) | AR26; AR25; AGM |
| MINOR | Jul 2022 call deferred four questions to email and answered the top 3 pharma ramp with "I do not have that data" | C22 [page 10-11], [page 14], [page 16], [page 18] |

Pipeline flags not supported by Verifier B: none.

## Verifier D (B12d), sorted by severity

Peers audited 3 (APARINDS 4 calls, MAANALU 4 calls, ARFIN none). Substantive confirmed 2; all 8 call rows confirmed. Claims addressed 8 of 8. Verdict discipline fails: none.

| Sev | Location | Note (verifier) |
|---|---|---|
| MINOR | B06 Q6 | B06 says MAANALU lists no Europe growth; MAANALU Nov-25 opening remarks say it is adding customers and growing in Europe; scoped verdict unchanged (MAANALU Nov-25 transcript lines 199-200) |
| MINOR | B06 Part 1 Q6 | CONTRADICTED rests on non powder peers; quotes are real; UNVERIFIABLE on powder demand with a flagged contradiction on route conditions is the tighter reading (MAANALU Jun-26 line 291, Aug-26 line 271; APARINDS Jun-26 lines 577-578) |
| MINOR | B06 Q7 | PARTIALLY VERIFIED rests on peers saying metal is hedged and on an oil, not metal, inventory effect; UNVERIFIABLE with contrast flag is tighter (MAANALU Nov-25 line 368, Feb-26 line 389, Aug-26 lines 300-304; APARINDS Nov-25 line 485) |
| MINOR | B06 Part 1 Q5 | PARTIALLY VERIFIED is direction only; no utility or PGCIL duration from any peer; B06 states this itself; acceptable |

Unused but relevant peer items (Verifier D):

| Peer | Item | Anchor |
|---|---|---|
| MAANALU | Nov-25 call: adding customers and growing in UK, Israel, Europe, Australia (qualitative, no numbers) | MAANALU Nov-25 transcript lines 199-200 |
| MAANALU | Europe and US require declaration of aluminium origin; Indian smelting origin preferred by export customers | MAANALU Jun-26 transcript lines 533-545, printed p.13 |
| APARINDS | Private rival with carbon score conductor reported close to PGCIL approval; PGCIL past performance barrier | APARINDS Jun-26 transcript lines 739-745, printed p.16 |

## Standing CRITICAL count after remediation

CRITICAL: 0 across A run 2, B, C run 2 and D. The single CRITICAL of the run (C run 1 F1) is fixed at source.
