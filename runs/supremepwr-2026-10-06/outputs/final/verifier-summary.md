# SUPREMEPWR verifier summary (phase 1)

Run runs/supremepwr-2026-10-06, dated 2026-10-06. Scope: Verifier A, Verifier B, Verifier D, and the Gate 0 plus Emerging Moat half of Verifier C. The valuation half of Verifier C runs in phase 3.

## Confidence delta (outputs/blocks/confidence.yaml)

| Component | Value | Block | Basis |
|---|---|---|---|
| numerical_acceptance | 97.5 | B12a | 640 checked; mandatory tier 103 of 103 (OR-32) |
| redflag_coverage | 76 | B12b | 13 of 17 material caught in full (88 at half credit for 4 partials, 100 at full credit) |
| framework_adherence | 94.9 | B12c | 74 of 78 phase 1 rules (Gate 0 45 of 48, Emerging Moat 29 of 30); valuation component pending phase 3 |
| peer_utilisation | NOT APPLICABLE | B12d | 2 of 3 peers substantive; Indotech has no transcripts; denominator 3 is below 4; reported as a count |
| overall | 76 | confidence.yaml | Set by redflag_coverage. Band 75 to 89: normal, note specifics |

REWORK triggers: none. No CONFIRMED Verifier A CRITICAL. No acceptance rate below 60% on a denominator of 4 or more (OR-29). Verifier A identity check: 0 CRITICAL rows, nothing to strike.

## Acceptance rates and counts

| Verifier | Model | Acceptance rate | Denominator | CRITICAL | MAJOR | MINOR | Other counts |
|---|---|---|---|---|---|---|---|
| A, numerical (B12a) | claude-sonnet-5-5 | 97.5% | 640 numbers (103 mandatory, about 510 sample, 28 supporting recomputations) | 0 | 2 | 11 | 7 rows struck by own rule 5b self check; material universe about 1,600 |
| B, concall red flags (B12b) | claude-opus-5-5 | 76% | 17 material items (1 CRITICAL, 16 MAJOR) | 0 | 4 | 12 | 30 independent flags: 22 caught, 8 partial, 0 missed; promise spot checks 5 of 5 confirmed; grade C concurred |
| C, framework, phase 1 (B12c) | claude-opus-5-5 | 94.9% | 78 rules (Gate 0 48, Emerging Moat 30) | 0 | 0 | 4 | valuation, expectation ledger and narrative checks pending phase 3 |
| D, peer coverage (B12d) | claude-sonnet-5-5 | 100% | 3 peers | 0 | 0 | 5 | 2 substantive confirmed; 0 unsupported; all claims addressed; 0 verdict discipline fails |

## Findings, sorted by severity

### CRITICAL

None from any verifier. Verifier B's one CRITICAL independent item (B-01, the FY27 guide walkback with a denial) was CAUGHT by the concall stage and is not a finding against the pipeline.

### MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A | 01-gate0.md Block E, E4 (and B01 yaml data_notes) | Claimed: contingent liabilities nil FY26 and FY25 (AR p.91, Note 30), 0% of net worth; basis not stated. Source: consolidated Note 30.1A AR p.91, guarantees nil; standalone Note 30.1A AR p.71, corporate guarantee for Danya 1,470.00 lakh = 13.0% of standalone net worth 11,293.81. Basis (consolidated vs standalone) unlabelled in Gate 0. UNANCHORED basis on a mandatory Gate 0 input scoring 5 of 5. Nil is correct on the cited consolidated page. source_fidelity: true |
| 2 | A | 03-ardeep.md Phase 4D, Capital allocation sense row | Claimed: borrowing limit asked 5x gross debt. Source: AGM Items 7 and 8 (AR p.33), Rs 500 Cr limit; gross debt Rs 45.73 Cr standalone (Notes 6, 9) or Rs 50.0 Cr consolidated; 500/45.73 = 10.9x; 500/49.97 = 10.0x. Contradicts the same report's own 10x in its block. Derived figure, no verdict card use. source_fidelity: true |
| 3 | B | B05 trigger 4; B06 2B (F1, PARTIALLY CAUGHT B-13) | Q1 FY27 gross margin 23.80% to 28.82%: inventory gain question unanswered; March pre buy of oil and copper disclosed in June; PVC passes rises and falls. B05 trigger 4 takes Q1 gross margin as the level to hold; B06 reads the oil spike one way. Two readings: PVC run rate vs one time pre buy gain. Separating observation: Q2 FY27 gross margin. Stage 11 should not anchor the margin bridge on Q1 until Q2 prints. Anchors: AUG p.5 (Garvit Goyal, CMD); JUN p.9, p.11 (CMD); SHIL-MAY26 p.8 (Alay Shah); DAN-MAY26 p.15 (Shivam Talwar) |
| 4 | B | B05 1B guidance row; dropped_triggers (F2, PARTIALLY CAUGHT B-02) | FY28 revenue guide walked down 400 to 500 Cr (Feb) to about 375 to 400 (Jun) to about 300 to 390 (Aug, DERIVED); B05 files the Feb figure as "order booking, ambiguous" and a dropped trigger. Feb p.12 follow up ties 450 to 500 Cr by FY28 to working capital and equity: it is revenue. Anchors: FEB p.11 to 12 (Paras Chheda, CMD); JUN p.5; AUG p.9, p.17 |
| 5 | B | B05 FLAG-SCHEDULE-DRIFT and repeated_evasions row 8 (F3, OVERSTATED pipeline flag) | 412 vs 377 Cr is a time basis comparison; about 41 Cr executed in the 78 days between closes most of the step; "flat book despite Q1 wins" double counts April to May wins already inside 588.17 Cr. The 377 to "almost 350" step and the 377 vs 250 to 300 guide gap stand. Order coverage held while the revenue guide fell; the cut points at execution capacity, not order flow. Anchors: JUN p.4, p.7; AUG p.3, p.7, p.15 |
| 6 | B | B05 FLAG-CAPACITY-INCONSISTENT derived range and analyst_note (F4, OVERSTATED pipeline derivation) | FY27 cross check 225 to 275 Cr uses the contradicted Unit 1 potential and steers stage 11 off the top of the guide; demonstrated output reading about 282 to 327 Cr (DERIVED). State both readings; Q2 FY27 revenue and any split by unit separate them. Anchors: FEB p.7, p.15; JUN p.4, p.8; AUG p.11 |

### MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 7 | A | 07-emoat.md G1 table (D27 cross ref) | 12.47 lakh x Rs 169 = Rs 21.08 Cr claimed; AR Note 30.2 p.71: 2,107.43 lakh = Rs 21.07 Cr. Rounding; 08-promoter.md has 21.07. source_fidelity: true |
| 8 | A | 03-ardeep.md 1B observation 2 | Note 12 cited on p.66; it is on [page 67], AR L6391 to 6398. Page off by one; figures right. source_fidelity: true |
| 9 | A | 03-ardeep.md Key monitorables (Danya gross trade) | Rs 15.54 Cr to 13-Aug cited at AR p.29; it is at AR L2472 on [page 28]. Page off by one; figure right. source_fidelity: true |
| 10 | A | 08-promoter.md 4B | Headcount 112 incl. contract cited at AR p.44; it is L4038 on [page 43]. Page off by one; figure right; 03 cites p.43. source_fidelity: true |
| 11 | A | 09-tam.md Method 4 | "AR p.18 says CRGO is 60 to 90% imported": AR MD&A L1398 to 1401 (p.17) says domestic output met around 10 to 12% of demand; GTRI shortfall close to 30%; no 60 to 90% anywhere in the AR. ANCHOR NOT FOUND, non material; Method 4 was not run. source_fidelity: true |
| 12 | A | 02-notes-pass1.md A(b); 03 LB3; 05 sec 2D; 07 D16 | Borrowings 18.74 to 49.98 Cr attributed to AR lakh figures or AR MD&A; AR consolidated BS p.81: 1,874.56 and 4,997.30 lakh = 18.75 and 49.97 Cr; AR MD&A p.19: Rs 50.0 Cr; 18.74 and 49.98 are the Pres-Q1 s.37 sums. 0.01 Cr rounding and basis; Gate 0 states the gap; 04 anchors to the presentation correctly. source_fidelity: true |
| 13 | A | 01-gate0.md load bearing fact 4; B01 yaml; 03 LB4 | Attributable Q1 FY27 +10.1% on 490.08 vs 445.37 lakh claimed; 490.08/445.37 = +10.04%; Pres-Q1 s.6 prints 10.04%. Rounding; 10.1% comes from the rounded Cr values. source_fidelity: true |
| 14 | A | 03-ardeep.md 3C-6 | Danya tax 36.6% of PBT claimed; AR p.43: (135.53 + 0.76)/371.30 = 36.71%. 0.1 point; pass 2 N6 has 36.7%. source_fidelity: true |
| 15 | A | 03-ardeep.md 2A and monitorables; 04 3D; 05 trigger 1 | Gross block depreciation run rate 1.26 Cr a quarter claimed; the report's own Note 13 / Schedule II components sum to 497 lakh a year = 1.24 Cr a quarter (1.56 Cr with CWIP add on). 1.26 reproduces neither basis; gap to Q1 0.80 is 0.44 Cr, not 0.46. source_fidelity: true |
| 16 | A | 09-tam.md 3B | Management peak 550 to 650 Cr = +4.7 to +6.1pp share vs FY29 SAM claimed; 650/6,819 = 9.53% less 3.37% = +6.16pp (6.2). Rounding on web derived SAM; arithmetic only. source_fidelity: true |
| 17 | A | 06-peers.md: Danish H2 FY26 PV p.8 and myth p.12; Shilchar Q4 FY26 PV clause p.15 and oil p.7 | Danish May-2026 PV text under [page 9]; myth under [page 13]; Shilchar May-2026 PV clause under [page 16]; oil +100% under [page 8]. Mixed marker and printed page convention. Quotes verbatim and present. source_fidelity: true |
| 18 | B | B05 trigger 5; JUN and AUG opening remarks (F5, PARTIALLY CAUGHT B-11) | Scripted margin claims (Jun: offset by high voltage mix; Aug: greater operating leverage) contradicted in the same calls' Q&A; not flagged. B05 trigger 5 (conviction L) already holds the right margin read; do not quote the opening remarks as margin evidence. Anchors: JUN p.4, p.6, p.11; AUG p.3, p.4, p.8, p.15 |
| 19 | B | B05 FLAG-QUALIFICATION-GAP; red_flags MEDIUM (F6, PARTIALLY CAUGHT B-15) | CMD describes the book as "25 MVA to 60-70 MVA" while 20 MVA orders sit in it; not flagged as a management overstatement. B05 reaches the substance from filings. Anchors: JUN p.9; FEB p.4; AUG p.6 |
| 20 | B | not in B05 (F7, PARTIALLY CAUGHT B-20) | "No credit" policy vs 60 to 75 day credit in one answer; 210 vs 110 day baseline in one call. Anchors: FEB p.12, p.13, p.15 |
| 21 | B | B05 red_flags LOW (F8, PARTIALLY CAUGHT B-23) | 112 MVA "330 kV" order above the 220 kV plant rating; 330 kV not a standard Indian class. Needs a filed check. Anchors: JUN p.9, p.10, p.12 |
| 22 | B | not in B05 (F9, PARTIALLY CAUGHT B-25) | June to August tone shift (exceptional, flawless, impressive to moderation, measured, cautiously, commit less) not called out. Anchors: JUN p.3 to 4; AUG p.3, p.4, p.7, p.16 |
| 23 | B | B05 (one instance noted) (F10, PARTIALLY CAUGHT B-28) | Wrong analyst figures left standing in all three calls (9M 118.45 vs 111.38; H2 EBITDA 14.6% vs 17.8% DERIVED; employee cost 4x); B05 notes only the 4x instance. Anchors: FEB p.3, p.14; JUN p.4, p.11; AUG p.7 |
| 24 | B | B05 Section 3D (F11, NOT SUPPORTED pipeline observation) | "3.03 Cr gap unexplained" (588.17 vs 585.14): different as of dates explain it (27-May and 2-Jun); six days at about 0.53 Cr a day is about 3.2 Cr. Anchors: JUN p.4, p.7, p.10 |
| 25 | B | B05 Section 2C (F12, NOT SUPPORTED pipeline evidence) | "Four times in Q1": one instance in the Aug call; five such replies across all three calls. Feeds only the Defensiveness score, which holds. Anchor: AUG p.5 |
| 26 | B | B06 Q1b CONTRADICTED (F13, OVERSTATED pipeline verdict) | B06 Q1b contradicts a lead time claim SPEL never made; SPEL's own lead times (about 4 weeks DT, 6 to 8 weeks at 25 MVA, 3 to 4 months at 50 to 100 MVA) match the peers. Synthesis should not count it against SPEL. Anchors: JUN p.13 to 14; AUG p.12 |
| 27 | B | B05 Section 3A (F14, OVERSTATED pipeline rating) | "No symptom" of competitive pressure rated Low on an input cost dip; an input cost dip is not price competition; use the forward capacity race as the basis. Anchors: FEB p.6; SHIL-AUG26 p.10 |
| 28 | B | B05 promise table (F15) | Padded row (government below 50%), premature row (Kannur 3 to 4 months), hedged intent tabled as a promise (land), positive delivery omitted (order book 311 to 588.17 Cr vs 70 to 160 Cr implied conversion, DERIVED). Tally becomes 3/3/3 plus one untabled positive; grade unchanged. Anchors: FEB p.9, p.11, p.16; JUN p.4, p.8; AUG p.4, p.6 |
| 29 | B | B05 and B06 anchors (F16, anchor drift, note for Verifiers A and D) | Some anchors use the printed page instead of the file marker; all quotes exist, page off by one. B05: 500 to 550 at H2 p.3 is p.4; players less at Q1 p.12 is p.11; 160 MVA at H2 p.8 is p.9. B06: DAN-MAY26 PVC p.8 is p.9; SHIL-MAY26 PV clause p.15 is p.16; SHIL-AUG26 entry margin p.6 is p.7; DAN-MAY26 product type p.12 is p.13 |
| 30 | C | B01 G0-33, M6 (01-gate0.md L109; B01-gate0.yaml L37) (F1) | M6 marked PEER DATA NEEDED; tiers 5 and 3 need no peer data. Binding gap is R&D spend (B07 reads R&D Nil, AR Annexure V). M6 = 0 unchanged; no effect on Block F (15), moats confirmed (4) or GOOD. Fix: relabel M6 "R&D Nil, 0% of revenue" |
| 31 | C | B01 G0-45, FLAG-GATE0 (B01-gate0.yaml L13, L22, L23) (F2) | FLAG-GATE0 raised on classification GOOD; trigger is AVERAGE or below, or a deal breaker override. Trigger not met; fragility text already in data_notes and analyst_note. Presentational; B07 carried the flag. Fix: drop the flag and keep the fragility note, or operator rules that "fragile to AVERAGE" fires FLAG-GATE0 |
| 32 | C | B01 G0-46, report YAML (01-gate0.md L134 to 150) (F3) | Report YAML carries 14 of 21 template keys and is followed by a pointer line; block file B01-gate0.yaml complete and values match. No data effect. Fix: paste the full block as the report's last element |
| 33 | C | B07 EM-21, I2 (07-emoat.md L347) (F4) | I2 answered for the 220 kV moat only; B2 (Moderate) not addressed. Maker's own B2 reading gives "nothing must be destroyed". I2 = 0 and total 8.3 unchanged; band NONE |
| 34 | D | B06 Q1a | Q1a VERIFIED overstated: peers state 3 to 7 years; the 10 year end rests on one passing line (Oct-2025 p.9) |
| 35 | D | B06 Q1b | Q1b CONTRADICTED rests on IDT niche lead times of 10 to 22 weeks; Shilchar Apr-2025 supports a 1.5 to 2 year industry norm; comparability caveat present |
| 36 | D | B06 Q10; 531201-Concall_Aug_2026_Transcript line 122 (Alay Shah) | Shilchar state utility avoidance ("will not do business with any state utility companies") not used in Q10, relevant to SPEL's 30.10% government share |
| 37 | D | B06 comparability note; 531201-Concall_May_2026 line 262; Aug_2026 line 110 | Shilchar export share cited at 50% (Oct-2025) while later calls say about 30% of FY26 revenue (context only) |
| 38 | D | B06 citations (Danish May-2026 p.8, p.12; Shilchar May-2026 PV p.15) | Page anchors off by one in several citations; all findable on the adjacent page |

## Verifier notes carried as written

- Verifier A, struck under rule 5b (7): net debt 40.23 vs 40.22 (labelled AR basis); EBITDA 32.82 vs 32.83 (labelled basis difference); Gate 0 profit +9.6% (correct on the lakh anchor); ROCE FY24 28.14% vs 28.16% (correct on stated inputs); payables FY25 3,464.86 (AR prints it); net worth FY26 112.9 vs 118.21 (source to source conflict, logged); Q1 FY26 PBT 6.16 vs 6.15 (labelled Data_Sheet basis).
- Verifier A, coverage: "No number in the verdict-bearing chain (Gate 0 inputs, load-bearing facts 3 and 4, Danya structure figures, order book, guidance figures, CFO/capex/debt) is wrong against its source." Mandatory tier is the Gate 0 scorecard inputs because no stage 13 verdict card and no stage 11 Section 1B exist in phase 1.
- Verifier A, not checkable from the corpus (arithmetic checked, inputs not): web inputs in 09-tam.md (CRISIL market size, Mordor shares, RBI rate, CEA MVA, NEP GVA, RDSS, peer capacity, TARIL and Voltamp revenue) and in 08-promoter.md (IPO subscription, pre IPO holding, FY26 Danya limit). Caution: 2,342 appears in B09 both as the NEP 2032 GVA endpoint and as Voltamp's order book; verify the NEP endpoint before stage 11 uses 8.2%.
- Verifier A, source conflicts recorded (no report cites the conflicting figure): FY25 CFO 37.69 (AR, screener) vs 39.36 (Pres-Q1 s.36); FY26 net worth 112.9 (AR p.12) vs 118.21 (Pres-Q1 s.37, screener); reserves 87.9 vs 93.22; Q1 FY27 EBITDA 8.89 (presentation) vs operating profit 8.81 (Data_Sheet); Pres-Q1 s.10 shows A3 and 21,357+ units against AR A3+ and 20,800+.
- Verifier B, credibility grade: "concur (C): every revenue guide landed at or below its floor and FY27 was cut twice with a denial, offset by a held PAT band and order intake that beat the Feb conversion range; after removing one padded and one premature row the tally is 3/3/3, still C." Added observation: Q2 FY27 gross margin against Q1's 28.82% separates a PVC run rate from a one time pre buy gain.
- Verifier B, promise spot checks: 5 checked, 5 confirmed, 0 wrong. Caveats: the Kannur 3 to 4 month row is better labelled NOT YET DUE; the government below 50% row tests nothing.
- Verifier C, framework defects noted for the operator (not fixed on a run branch): prompts/12 L379 carries an edit instruction instead of a field; prompts/12 names no input for B09/09b in rules 6, 9, 10 (run log).
- Verifier D, unused but relevant: Shilchar will not do business with state utilities (Aug-2026 line 122); Shilchar export mix about 30% in later calls vs 50% cited.

## Verifier disagreements

None this run. No downstream step relied on, cleared or argued around a Verifier A source fidelity finding. The synthesis carries both bases for the E4 contingent liability input (finding 1: consolidated nil at AR p.91; standalone Rs 14.70 Cr Danya guarantee at AR p.71), the corrected 10x borrowing limit (finding 2), and the corrected minor figures (Rs 21.07 Cr, 10.04%, Rs 1.24 Cr a quarter, Rs 18.75 Cr and Rs 49.97 Cr on the AR basis). Disposition for each: GATE HELD, figure corrected at source with the correct anchor shown. In phase 1 lite mode this section stands in for verifier-disagreement-log.md; the content of that file would read "none".
