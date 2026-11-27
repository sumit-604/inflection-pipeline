# RKFORGE: Verifier summary (phase 1, run 2026-11-12)

## PHASE 1 CONFIDENCE DELTA

| Component | Value | Source | Basis |
|---|---|---|---|
| Numerical acceptance | 98 | B12a | 585 numbers checked; mandatory tier 174 of 174; sample tier about 411 of about 650 (63%); 7 false positives struck |
| Red flag coverage | 100 | B12b | 13 of 13 material flags caught (8 caught, 5 partly caught); strict count without partials 8 of 13 = 62% |
| Framework adherence | 77.1 | B12c | phase 1 scope, Gate 0 26 rules + Emerging Moat 22 rules: 37 of 48 passed; valuation half PENDING PHASE 3 |
| Peer utilisation | 100 | B12d | 12 of 12 peer transcripts substantive |
| Overall | 77.1 | confidence.yaml | min of components; set by framework adherence; band 75 to 89 normal |

Acceptance rates: A 98, B 100, C 77.1, D 100. REWORK triggers: Verifier A confirmed CRITICAL false; acceptance below 60% on a denominator of 4 or more false. Remediation cycles used 0. Verifier runs A 1, B 1, C 1, D 1. Verifier A shadow: skipped (claimed by another session).

Severity counts: A 0 CRITICAL / 0 MAJOR / 12 MINOR (1 source fidelity row); B 0 / 5 / 11; C 0 / 1 / 10 (plus 8 notes, not counted); D 0 / 0 / 2.

Verifier A identity check: 0 CRITICAL rows, 0 struck.

Source fidelity open: B12a finding 4. The stage 8 report cites AR26 p.8 for Directors' Report disclosure j (14 June 2025 fact finding report date; 22,052.43 / 5,022.26 INR lakh). Verifier A places it at AR26 p.15. The number exists in the source; downstream use is at the p.15 anchor only.

Verifier disagreements: none. No downstream step kept the p.8 anchor, leaned on it in a re-derivation, or cleared the flag. The gate recommendation and the narrative use the figure only at AR26 p.15. No verifier-disagreement-log.md is written for this run.

## CRITICAL

None from any verifier.

## MAJOR

| # | Verifier | ID | Location anchor | Finding |
|---|---|---|---|---|
| 1 | B | B-01 | B05, B06; Oct LK p10; Oct Aditya Kumar Q p10 | Bill discounting sub-claims not supported: 'outside gross debt', 'hides', Rs 173 Cr all bill discounting, receivable add-back |
| 2 | B | B-02 | B05; May LK p16 | ECL Rs 42 Cr 'headroom... will help us in future' on a receivable called 'totally receivable' filed as neutral prudence; earnings-quality flag not raised |
| 3 | B | B-03 | B05; Jan NJ p7; May NJ p7; Jul NJ p13; Oct MG p7 | Cold and aluminium forging utilisation target slip (80-85% -> 75-80% -> >70% Q3 -> >50%; 'full in 8-10 months' -> >50%) not identified; 4A priority 1 confirm signal stale |
| 4 | B | B-04 | B05; Oct NJ p12, Oct p18-19; May NJ p10 | Oct retreat on Rs 8,000 Cr FY29 target read as analyst error; phantom 'May guidance' not flagged; YAML still carries FY29 target and 22-25% CAGR as live |
| 5 | B | B-05 | B05; May Ayush Goyal Q / LK p9; Jan NJ p11 | FY27 order-book revenue bucket cut Rs 2,200 Cr to Rs 1,550 Cr rated explained and low; CFO answer non-responsive; forward-basis input |
| 6 | C | G07 | B01 l.11, l.27, l.88; rule P01 l.27-31, l.13 | EBIT strips other income. As written EBIT = PBT + finance cost: FY24 ROCE 14.4%, FY25 7.7%, median >= 10.2%; A1 0 -> 1, Block A 5 -> 6, core 40 -> 41, grand total 47 -> 48, DB3 not fired; D2 0 -> 1 if FY26 other income >= 24.64 Cr. Classification AVOID unchanged (DB6, DB1). Fix: stage 1 re-scores A1, A2, A4, M3, D2 on PBT + finance cost, or operator defines EBIT in prompt 01 |

## MINOR

| # | Verifier | ID | Location anchor | Finding |
|---|---|---|---|---|
| 7 | A | 1 | 01-gate0.md E3; 08-promoter.md pledge table | Pledge as % of equity: 12,300,000 / 18,55,70,017 (XBRL NumberOfFullyPaidUpEquityShares) = 6.63%; 18,59,40,989 is fully diluted (6.62%); Gate 0's 6.7% matches neither base. Basis mislabelled (08) and unstated (Gate 0). DB5 unaffected. source_fidelity false |
| 8 | A | 2 | 02-notes.md LB fact 3 and top_findings rank 11 | Promoter holding 31 Mar 2026 shown as 43.32% without 'computed' label; 43.33% printed (AR26 p.66 CG table; Note 16(l) pp.117-118). 0.01 pp. source_fidelity false |
| 9 | A | 3 | 01-gate0.md Block F M6 | R&D 995.69 lakh is the STANDALONE total (AR26 p.135 Note 38); 0.27% of standalone, 0.23% of consolidated revenue. Basis not labelled; score unchanged. source_fidelity false |
| 10 | A | 4 | 08-promoter.md Section 3E close-out line | Disclosure j ('14 June, 2025'; 22,052.43 / 5,022.26 lakh) is at AR26 p.15, not p.8 (p.8 holds the warrant utilisation table). Number exists; page 7 off. Anchor correction clears it. source_fidelity TRUE |
| 11 | A | 5 | 08-promoter.md 3E and 6C | AR25 Note 47 and Note 48 values sit at AR25 p.161, cited p.160. All values MATCH; page off by one. source_fidelity false |
| 12 | A | 6 | 04-bizmodel.md 1B, 2A, 2E | Price adjustment mechanism (Note 41(iii)) and 50 bp = 870.15 lakh PBT are at AR26 p.147, cited p.146. Values MATCH. source_fidelity false |
| 13 | A | 7 | 05-concall.md Oct 2026 call cites (LK p3, LK p4, MG p4-5); 07-emoat.md | Cited page equals printed footer page (PDF page minus 1) for 28.7%/30.7%, 126 Cr, 18.23%, 95 Cr, 673/447/272; other Oct cites use PDF pages. Values MATCH; mixed convention. source_fidelity false |
| 14 | A | 8 | 02-notes.md C3/rank 4; 03-ardeep.md 1D/2.0/flags; 02-notes-pass1.md 4.7/7.4 | Note 18.3 and 18.4 at marker p.124 (printed p.122) under a declared marker convention; CARO ii(b) at marker p.81, cited p.80. Values MATCH. source_fidelity false |
| 15 | A | 9 | 09-tam.md 1A, 2, 4A/4B, signal table; 04-bizmodel.md IP refs | Wheel demand text at AR26 p.43 (cited p.41); IP slide numbers drift between printed and PDF numbering. Values MATCH. source_fidelity false |
| 16 | A | 10 | 09-tam.md Section 2 Method 1 table | Persistence 72,886 / Expert Market 55,658 / IMARC 33,793 recompute to 72,884 / 55,657 / 33,792. 1-2 Cr; no TAM carried changes. source_fidelity false |
| 17 | A | 11 | 02-notes-pass1.md 10.2 | 83.8% is 18,737.28 / FY25 PBT 22,356.91, attached to the PAT denominator; correct share 46.6% printed in the same line. Not carried downstream. source_fidelity false |
| 18 | A | 12 | 03-ardeep.md 4C Mexico row | 'loss (1,447.73)' is Mexico PBT (AOC-1, AR26 p.17); PAT loss is 1,014.67, used elsewhere. Basis differs. source_fidelity false |
| 19 | B | B-06 | B05; Jan NJ p13-15; May NJ p14; Jul NJ p9, p11; Oct NJ p11, p13 | Four-call margin timeline evasion absent from 4D table and YAML red_flags; Oct casting dilution remark not tied to bear margin |
| 20 | B | B-07 | B05; Jan NJ p13; Jul Bharat Shah Q p22 | Promise row 16 origin wrong; no Rs 8,000 Cr promise in the Jan call |
| 21 | B | B-08 | B05; Jul LK p5; Oct LK p4 | Promise row 7 scored DELIVERED on H1 only; full-year outcome not observable |
| 22 | B | B-09 | B05; May p16, p9, p19; Jul p12, p13; Oct p5, p12, p25 | Mixed anchor convention: many May/Jul/Oct anchors cite printed page, one below PDF page; not a source-fidelity finding |
| 23 | B | B-10 | B05, B06; Jul NJ p27; Jan LK p12; HAPPYFORGE Aug 2026 Garg p7 | Currency pass-on claim marked needs check but never tested against peers or the Jan FX loss remark |
| 24 | B | B-11 | B06; BHARATFORG Nov 2026 Dixit p3; HAPPYFORGE Aug 2026 Garg p3 | Q4 verdict VERIFIED for a claim worded 'without customer recovery' while peers show lagged or partial recovery; RKFL part is divergent |
| 25 | B | B-12 | B05; May NJ p6; Jul NJ p8 | Missed wheel approval-sequence contradiction |
| 26 | B | B-13 | B05; Jan NJ p6, p8, p19; May NJ p11; Oct p17, LK p18 | Missed wheel capacity drift and Jan exclusion of wheel sales from projections; consolidation at 51% asserted from an analyst figure |
| 27 | B | B-14 | B05; Jan LK p12 | Missed Q3 FY26 rejection-driven gross margin hit |
| 28 | B | B-15 | B05; Jan NJ p15; Jul NJ p7 | Wheel '40,000 -> 80,000' inconsistency overstated |
| 29 | B | B-16 | B05; Jul p13; B06 Q5 | 36-point gross-to-EBITDA gap overstated as a level flag; peer-normal per B06 Q5 |
| 30 | C | G06 | B01 l.11; P01 l.29 | ROCE denominator proxy Equity + Reserves + Borrowings for all 10 years, not Total Assets less Current Liabilities, though FY25-FY26 formula inputs were read (AR2026 p.164). Recomputed NOT DETERMINABLE from B01; no effect on classification |
| 31 | C | G03 | B01 l.38; P01 l.15-18 | FY24 trade payables 1,016.63 Cr, the B4 earliest endpoint, anchored without a page |
| 32 | C | G17 | B01 l.80; P01 l.132 | M11 1-band (growth >15% but selling % rising) not tested; FY17 selling share NOT FOUND; moat score 7 or 8; count 2 and MODERATE unchanged |
| 33 | C | G23 | B01y l.25; P01 l.153-154 | DB1 driving years not stated; drivers FY20 (A2 4.72%) and FY17, FY20, FY21, FY25, FY26 (A1) |
| 34 | C | E04 | B07 l.66-70, l.37-43, l.91, l.93, l.162; P07 l.29-30 | Taxonomy tag missing on descriptive items; deck history tagged documented in B2/E2 but claim in H3; no score change |
| 35 | C | E07 | B07 l.194; B07y l.22; P07 l.44-46, l.157-159 | Count line '1 of 22' should read 0 of 22 plus R1 Moderate; recount mixes units (row basis 14, item basis 17); claim count 11 not 10; evidence_mix wrong; guard result unchanged |
| 36 | C | E10 | B07 l.230-249; P07 l.172-173 | No mixed-tier multiplier rule stated; recomputed range 8.7 to 11.7, NONE in every reading |
| 37 | C | E17 | B07 l.111, l.125 | Railway share 4.6% to 7.5% backs both B2 and the C2 non-auto rise; worst case total 7.6, NONE unchanged |
| 38 | C | E19 | B07 l.265; B07y l.32-41; P07 l.194-195 | Register row 'Cold forging and casting approvals as lock-in' missing from optionality_register (9 of 10 rows); watch item lost to synthesis |
| 39 | C | E22 | B07 l.340-345; B07y l.12; P07 l.214 | Report YAML and block file differ; block carries anchor errata the report body does not correct |
| 40 | D | 1 | B06 Q4 verdict; BF Aug-26 p3, Happy Aug-26 p8, MMFL Aug-26 p13 | Q4 verdict VERIFIED rests on a reworded claim; cost-borne has 3 peer anchors, no-recovery is contradicted by Happy and BF; PARTIALLY VERIFIED would fit the claim as written |
| 41 | D | 2 | B06 Q9; BF Aug-26 lines 280-282, 469-505 | BF defence approval discussion is not an aerospace forging approval timeline; UNVERIFIABLE stands; industry context only |

## NOTES (Verifier C, not counted as fails)

| ID | Location anchor | Note |
|---|---|---|
| N1 | P01 l.77-86, l.89; B01 l.51-55, l.93, l.97 | 'Latest' in Block D undefined. On a latest reported period reading, TTM EBITDA 838.62 Cr, D2 2.04x = 1; D1 > 3x only if Sep-26 net debt > 2,515.86 Cr vs 2,285.87 Cr FY26; Sep-26 net debt NOT FOUND in verifier inputs; if DB6 off, classification AVERAGE. Operator ruling needed |
| N2 | P01 l.93; B01 l.62 | Pledge basis not named in the rule; on total equity basis E3 = 1 and DB5 does not fire; classification unchanged (DB6) |
| N3 | B01 l.42; P01 l.35 | B4 = 5 is fragile; with the 399.78 Cr non-recourse add-back, WC days rise 24 days and B4 would be 0; already flagged |
| N4 | B01 l.79; P01 l.126-127 | M10 = 3 stands on either receivable days reading |
| N5 | B07 l.23; P07 l.50-51 | B07 1A row 8 status 'DROPPED' sits outside the six-status list; no score effect |
| N6 | B07 l.304-307; P07 l.203-204 | Combined matrix not stated in P07; 6D checked for internal consistency only |
| N7 | B01 l.75; P01 l.114-116 | M6 'PEER DATA NEEDED' label is cosmetic; R&D 0.2% fails every band |
| N8 | prompts/12-verifiers-pipeline.md l.379 | Instruction-file defect: the business_understanding_narrative line was replaced with instruction text; operator should restore it in prompt 12 |

## VERIFIER B: PIPELINE FLAGS ASSESSED NOT SUPPORTED OR OVERSTATED

| Pipeline flag | Assessment | Anchor |
|---|---|---|
| B05 4D HIGH, 4B, YAML flags: bill discounting 'outside gross debt' and 'hides' | NOT SUPPORTED. Oct LK p10 nets bill discounting from the Rs 2,173 Cr gross figure, so it sits inside gross. The netting itself is supported | Oct LK p10 |
| B05 2D: whole Rs 173 Cr gap labelled bill discounting | OVERSTATED. Analyst frames the net figure as 'net of cash and bill discounting'; bill discounting amount NOT FOUND on calls | Oct Aditya Kumar Q p10 |
| B06 Q10, YAML flags: receivable days 68.5 to 83.4 with Rs 173 Cr added back | NOT SUPPORTED. Bills inside gross borrowings imply receivables not derecognised, so the add-back double counts | Oct LK p10 |
| B05 2B: Oct 'never guided Rs 8,000 Cr from wheel project' called a fair correction of an analyst misreading | NOT SUPPORTED. The analyst asked about total revenue and NJ interrupted | Oct p18 |
| B05 2C, 4D: wheel volume '40,000 -> 80,000' inconsistency | OVERSTATED. 80,000 is the total confirmed order, 40,000 the FY27 obligation | Jan NJ p15; Jul NJ p7 |
| B05 4D MEDIUM: 36-point gross-to-EBITDA gap as a level flag | OVERSTATED. B06 Q5 shows the level is peer-normal; the QoQ divergence (Jul p13) is the supported signal | Jul p13; B06 Q5 |

Verifier B promise-delivery spot checks: 5 checked, 4 confirmed, 1 wrong (row 16 origin). Credibility grade: concur C.

Verifier B missed items (all MINOR, carried as B-12, B-13, B-14 above): wheel approval sequence contradiction (Jan NJ p15; May NJ p6; Jul NJ p8; Oct NJ p18); wheel capacity and revenue framing drift (Jan NJ p6, p8, p19; May NJ p11; Oct LK p18); Q3 FY26 gross margin hit of about 1% from higher rejections (Jan LK p12).

## VERIFIER A COVERAGE NOTE

Mandatory tier 174 of 174 checked (Gate 0 scorecard; no verdict card or Section 1B input exists in phase 1; screener cells 135 + filing, NSE and XBRL figures 39). Sample tier about 650 material numbers (estimate), about 411 checked (63%), in materiality order. Not checked: web-sourced figures with no corpus source (stage 8 EGM vote counts, media items, pledge history; stage 9 FX rate, AIFI, third-party market sizes, Bharat Forge segment, ACMA, China share, INR move); the investor presentation slide 8 image (arithmetic recomputed from text layer); results PDFs and most announcements not cited by any report. Page rule: right note with marker page off by 1 to 2 is MINOR weak anchor; more than 2 is ANCHOR NOT FOUND (one row, source_fidelity true).
