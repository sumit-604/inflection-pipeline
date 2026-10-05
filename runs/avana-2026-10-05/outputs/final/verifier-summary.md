# AVANA: verifier summary, phase 1

Run: avana-2026-10-05. Stage 13, PHASE 1 LITE. Scope: Verifiers A, B and D in full; Verifier C on Gate 0 and Emerging Moat only (valuation half, expectation ledger and business narrative check PENDING PHASE 3). Units: figures in INR lakh unless the row says Rs Cr.

## Confidence delta (phase 1)

| Component | Value | Acceptance basis |
|---|---|---|
| Numerical acceptance (Verifier A, B12a) | 96.4 | 640 figures checked of about 1,050 material (60%); mandatory tier 32 of 32 (Gate 0 inputs; no verdict card or Section 1B pillar exists yet); 7 false positives struck |
| Red flag coverage (Verifier B, B12b) | 75 | 8 material: 3 CAUGHT + 3 PARTIALLY CAUGHT counted per verifier rule 3 = 6 of 8; strict CAUGHT only 3 of 8 = 37.5% recorded, not used; 25 independent flags found |
| Framework adherence (Verifier C, B12c) | 87.0 | 60 passed of 69 checked (Gate 0 42 of 47, EM 18 of 22); valuation 0 checked, PENDING PHASE 3 |
| Peer utilisation (Verifier D, B12d) | NOT APPLICABLE | 3 peers, under the floor of 4; 3 of 3 used substantively (2 of 3 if MARINE counts as cited only); verifier rate 100 |
| Overall | 75 | set by red flag coverage; band 75 to 89, normal |

Rework check (confidence.yaml): no CONFIRMED CRITICAL in B12a; no applicable component below 60% on a denominator of 4 or more (OR-29). No REWORK.

Orchestrator notes (confidence.yaml): Verifier B asked the orchestrator to choose between the rule 3 rate (75%) and the strict rate (37.5%); the orchestrator applied the rule 3 rate as emitted. Verifier B's two MISSED items (R6, R8) were audited against B05 and B06 only; stage 8 records promoter pay at 24.7% of PAT and the family fees, and stage 3 records the disclosure slips. Verifier C C-01 is not revised into B01 in phase 1; it carries to the dossier and stage 10.

Severity counts: CRITICAL 0. MAJOR 11 (A 5, B 5, C 1, D 0). MINOR 22 (A 7, B 6, C 6, D 3).

## CRITICAL

None. No verifier logged a CRITICAL finding.

## MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A | 03-ardeep.md Phase 3C P&L line walk (margin waterfall bullet) | Claimed travelling expenses fell 18.89 (AR p116). Source truth: 86.36 (FY25) to 65.47 (FY26) = fall of 20.89 (AR p116, Note 24). Subtraction error in lakh; not a verdict card or pillar input. Source fidelity: true. |
| 2 | A | 08-promoter.md 2C Tax and revenue (FY26 AR contingent items remark) | Claimed FY26 contingent items Rs 9.97 Cr. Source truth: FY26 total 679.22 lakh = Rs 6.79 Cr (481.42 + 196.16 + 1.64, AR p119 Note 25 item 3); Rs 9.97 Cr is the FY25 comparative. Year mislabelled; the 0.35 Cr drop beside it mixes years (RHP p33). Source fidelity: true. |
| 3 | A | B00-inputs.yaml load_bearing_facts LBF4 | Claimed H1 stub revenue Rs 36.28 Cr. Source truth: revenue from operations 3,574.71 lakh = Rs 35.75 Cr (RHP p72, p226; results re-filing p10); 3,628.32 lakh is total income including other income 53.61. Origin is the step 1 brief. Downstream stages use 3,574.71 correctly. H1 PAT 5.61 Cr matches (560.74 lakh). Source fidelity: true. |
| 4 | A | 02-notes-pass1.md section 4 Trade receivables, concentration bullet | Claimed top five 38.79% H1 FY26 vs 22.42% FY25 at "RHP p.12056". Values exist at RHP p38 and p169 to 170; page 12056 does not exist (text file line number). LBF2 is load bearing, so a missing anchor is MAJOR under rule 5. Source fidelity: true. |
| 5 | A | 09-tam.md 3C capacity cross check and B09 input_gaps | Claimed 886 vs 600 panels at AR p74; capacity figures at RHP p105. Source truth: 886 and 62,034 at AR p85; 600 / 70,000 and 1,500 / 1,75,000 at RHP p104. Values right; anchors off by one or more pages. Feeds FLAG-CAPACITY. Source fidelity: true. |
| 6 | B | B05 all sections | Claimed no governance or pay red flag; FY27 pay 341.64 listed as cost guidance. Source truth: family take 367.48 = 31.3% of FY26 PAT; FY27 pay above Sec 197 limits, self approved; 78.00 a year to promoter wives and mother; AR framing contradicts notes. R6 MISSED (AR p52, p67, p117 to 118; AGM p3; votes p5). |
| 7 | B | B05 all sections | Claimed no disclosure quality flag. Source truth: NSE results query (RES p1 to 2); Board report vs CARO on cost records and CSR; MD&A interest cover backwards; CS exit 69 days after listing; KMP pay swap. R8 MISSED. |
| 8 | B | B05 2B; block excuse_pattern | Claimed silence heavy, no external blame. Source truth: RHP p179 blames COVID-19 for KIADB non start; construction was due about Dec 2018; KIADB notice 2023; 2016 to 2025 history absent. R2 PARTIALLY CAUGHT; excuse pattern misclassified. |
| 9 | B | B05 2D; B06 Q8 | Claimed 886 vs 600 panels explainable by shift basis; capacity basis NOT FOUND. Source truth: RHP p104 "fully utilised and further capacity expansion cannot be done"; relays fell 65,840 to 62,034 (AR p85). R5 PARTIALLY CAUGHT; B06 reading OVERSTATED; relay decline and mix margin link absent. |
| 10 | B | B06 FLAG-WC-PATTERN; Part 4; cross_peer_hypothesis | Claimed AVANA WC and cash profile matches SPCL; WC drain is the live use of IPO money. Source truth: sales based inventory 97.6 days, receivables 96.7 (nearer DANISH); CFO +795.44; debt 568.51 to 76.14; IPO WC use 123.03, internal accrual 2,315.90. NOT SUPPORTED (AR p101, p43, p107; RES p4). |
| 11 | C | C-01, Gate 0 rules G-03, G-08, G-09 (01-gate0.md Block A; B01) | Stated ROCE proxy (equity + borrowings) all 7 years; median 17.79%, min 7.09%; A1 3, A2 0, Block A 10, Core 69, grand 100. Recomputed EBIT / (TA minus CL): FY23 16.65%, FY24 42.49%, FY25 46.48%, FY26 26.61% (RHP p225; results p10 to 11); FY20 to FY22 NOT FOUND; median 34.55%, min 16.65%; A1 5, A2 5, A4 5, Block A 17, Core 76, grand 108 with C-02. Classification GOOD+ unchanged. Fix: B01 revision; align B07 6C and combined_reasoning. |

## MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 12 | A | 01-gate0.md E2 line and B01 data_notes E2 | Claimed 100% promoter holding at 31 Dec 2023 (RHP p92). Source: RHP p92 is "as on December 31, 2025". 100% and the minus 26.36pp arithmetic are correct; date label wrong. Source fidelity: true. |
| 13 | A | 01-gate0.md data notes, FY25 source conflict | RHP restated CFO 676.66 and PAT 831.23 cited at RHP p290 and p32. Both at p290; PAT 831.23 at p31, not p32. Primary anchor holds. Source fidelity: true. |
| 14 | A | 01-gate0.md Block B note and B01 data_notes (WC days) | RHP projected 205 days vs computed 136.5. 136.5 is revenue basis; the RHP 205 uses COGS and purchases bases (RHP p113). Like for like 176.8 days (AR p99, p113, p115). Unlabelled basis difference; no score effect. Source fidelity: false. |
| 15 | A | 06-peers.md Q3 (DANISH IPO proceeds line) | "100% completed" quote is on May 2026 transcript page 5, not page 4. Quote exists verbatim one page later. Source fidelity: true. |
| 16 | A | 08-promoter.md 1B, 3E; B08 adverse_findings rank 5; B08 evidence | Anchors "RHP p.21283 region", "AR pp.2397 to 2417 region" do not exist (line number slips). "Our Promoters are not related to each other" is at RHP pdf p217 = printed p212. RF35 education text at pdf p53, printed p48. Facts exist; anchors wrong or off by one. Source fidelity: true. |
| 17 | A | 09-tam.md Method 3 peer table and B09 | Aartech Solonics FY25 revenue Rs 39.33 Cr ("web", no URL). RHP p119 and p122 print 3,635.22 lakh = Rs 36.35 Cr (consolidated). Feeds the peer floor only; no effect on SAM or SOM. Source fidelity: false. |
| 18 | A | 05-concall.md 1A; 07-emoat.md 4B; 08-promoter.md; 09-tam.md 5D and B09 stale_data_flags | Approximate anchors ("RHP p~36-40 region", "RHP p~170-171", "RHP line ~10682", "RHP p~190", "RHP p~14"). Order book 5,223.65 is at RHP p49 and p172; FX 88.79 at RHP line 1703. Every value checked exists. Source fidelity: false. |
| 19 | B | B05 peer_questions 2; B06 Q2 | Warranty drop 0.50% vs 3.72% treated as a peer question. Source truth: H2 FY26 accrual about 6.06 on revenue 4,811.17 (0.13%); provision 457.74 to 322.15 in H2; PBT effect 5 to 20% of H2 PBT [INFERENCE]. R4 PARTIALLY CAUGHT; under weighted (AR p124; RHP p231, p235). |
| 20 | B | B05 2A rows 4 and 6 | WC cycle and receivables marked DELIVERED. Source truth: projections that justified an 860.00 raise; IPO WC use 123.03; internal accrual 2,315.90. R10; direction right, classification generous. |
| 21 | B | B05 3D; B06 Q7 | Top five 38.79% H1 FY26 called not high vs SPCL. Source truth: top five rose from 22.42% FY25; top ten from 31.50% to 52.00% (RHP p37 to 38). R11 trend absent. |
| 22 | B | B05 2A row 7 | Exports PARTIAL at 0.55%. Source truth: AR p4 "global clientele" map with six countries vs 46.28 exports; country lists differ (AR p68). R12 branding contradiction absent. |
| 23 | B | B05 2B | "About 11 weeks before the date." Source truth: 19 Aug 2026 to 26 Oct 2026 = 68 days (9.7 weeks). Imprecision. |
| 24 | B | B05, B06 | Not mentioned: R17 NSE price query; R20 Board and Audit Committee functioning; R21 bank stock statement gaps; R24 RHP "transformers". Minor misses aggregated. |
| 25 | C | C-02, rule G-35 (01-gate0.md M8; B01) | M8 stated 0, no reach metrics. RHP p173 to 174 names 6 dealers; RHP p39 dealer revenue 3.65 to 86.16 lakh FY23 to FY25; re-derived M8 1, moat score 32, moats present 7 unchanged. No class effect. Fix: B01 revision. |
| 26 | C | C-03, rule G-47 (01-gate0.md closing block) | Report ends with an abridged YAML block missing 9 schema fields; full block only in B01-gate0.yaml. Presentational. Fix: B01 revision. |
| 27 | C | C-04, rule E-05 (07-emoat.md recount line; B07 evidence_mix) | Recount says 13 documented across 5 categories but itemises 10; evidence_mix documented 16 double adds 3 items (re-derived 13); claims at least 13, not 8. No score effect; guard outcome unchanged (2 of 22 active). Fix: B07 recount and evidence_mix. |
| 28 | C | C-05, rule E-09 (07-emoat.md Section 5 scoring table) | 15 grouped rows; rule requires all 23 rows. Presentational. Fix: B07 Section 5. |
| 29 | C | C-06, rule E-20 (07-emoat.md 2A capacity, Section 3 C2, top_moat_risks) | 3 evidence items anchored to B03 / B04 only, no source page. Weak anchor. Fix: B07 anchors. |
| 30 | C | C-07, rule E-21 (B07 catalysts_12m item 2) | Vendor registrations to valued order carries a 12 to 24 month window inside catalysts_12m. Move to the optionality register or relabel; risk of over counted catalyst proximity at Pillar 3 in phase 3. |
| 31 | D | B06 Part 3; MARINE-Data_Sheet.csv rows Sales, Raw Material Cost, Receivables, Inventory | MARINE marked SUBSTANTIVE but verdict bearing evidence is sheet only; deck citations (p16 to 17 customers, p32 new facilities) are real but light. B06 discloses this. Treat as CITED-ONLY on documents, sheet as carrier. Sheet figures spot checked and match. |
| 32 | D | MARINE deck page 31 | Q9 left UNVERIFIABLE without citing the MARINE p31 vendor qualification barrier (context only, not a lag). Verdict stands. |
| 33 | D | B06-peers.yaml line 17 | B06 peers_provided is 4 (documents) against 3 peers; count basis differs from this audit. |

## Verifier B: further record (as written by the verifier)

Missed items (12): R6 promoter family take (MAJOR); R8 disclosure control weakness pattern (MAJOR); R13 MD&A interest cover 0.05x vs 0.07x vs derived 19.4x and 14.5x (AR p74; AR p127); R14 cost records, Board report vs CARO (AR p51; AR p94); R15 CSR nil spent, committee never met, 12.78 to PM CARES, CARO says no unspent amount (AR p46, p57 to 59, p96, p124); R16 NSE email 17 Jun 2026, four defects in the FY26 results filing (RES p1 to 2); R17 NSE surveillance price movement query 10 Apr 2026; R18 CS resigned 69 days after listing (AR p63); R19 CFO and CS pay figures swapped between Board report and notes (AR p52; AR p117; RES p18); R20 10 of 23 Board meetings at 57% attendance, Audit Committee met 3 times, none after 23 Dec 2025 (AR p45 to 46); R21 bank statement receivables above books by 2.15% to 7.77% each FY26 quarter (AR p125); R24 RHP order book described as "transformers and relay panels" (RHP p49). All MINOR except R6 and R8.

Pipeline flags not supported (1): B06 FLAG-WC-PATTERN (row 10 above).

Promise delivery spot checks: 5 checked, 5 confirmed, 0 wrong.

Credibility grade concurrence: lower by one notch. RHP blames COVID for a KIADB delay whose first deadline passed about 15 months before COVID (RHP p179), and the AR contradicts its own numbers (margin "no significant change", interest cover, pay "marginally", cost records and CSR vs CARO). Hold C at its floor if no lower grade exists.

## Verifier A: coverage (as written by the verifier)

Mandatory tier 32 of 32: the Gate 0 scorecard inputs (A1 to A4, B1 to B4, C1 to C4, D1 to D4, E1 to E4, M1 to M12), each re-derived from source cells; all 32 tie. No verdict card and no Section 1B pillar section existed (stages 10, 11 and 13 not yet run), so those sub tiers held zero figures. Sample tier 640 of about 1,050 material figures (60%). About 45 figures were not checkable from the inputs: stage 9 web market sizes, stage 8 media figures, MARINE deck financial slides (images). AR pp99 to 127 are image transcriptions; the verifier settled damaged digits by tie outs and did not reopen page images.

## Verifier C: phase 1 scope note

Gate 0: 47 rules checked, 5 fails (G-03 MAJOR, G-08 and G-09 consequential, G-35 and G-47 MINOR). Emerging Moat: 22 rules checked, 4 fails (E-05, E-09, E-20, E-21, all MINOR). Valuation: 0 rules checked, PENDING PHASE 3. Expectation ledger: PENDING PHASE 3. Business narrative check: NOT IN PHASE 1 SCOPE. Recomputed classification: GOOD+ concurs.

## Verifier D: scope note

3 peers audited (DANISH two transcripts, SPCL deck and sheet, MARINE sheet and deck); 3 substantive confirmed; 0 unsupported; 9 of 9 peer questions carry a verdict (0 verified, 7 partial, 2 unverifiable); no verdict discipline fails. Unused but relevant: MARINE deck p31 vendor qualification barrier for Navy and Coast Guard (MARINE-Investor-Presentation-2025-10-11.txt page 31).

## Verifier disagreement log

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| none | | | | | | |

No downstream step's conclusion conflicted with a Verifier A source fidelity finding in phase 1. Verifier C's ROCE recompute rests on RHP p225 and results re-filing p10 to 11, which Verifier A did not flag. No source re-check has cleared any Verifier A finding: all 12 B12a findings stand UNCLEARED. Stage 13 used Verifier A's source truth wherever a flagged figure appears in its three files: H1 FY26 revenue Rs 35.75 Cr (not Rs 36.28 Cr), FY26 contingent items Rs 6.79 Cr (the Rs 9.97 Cr figure is not used), capacity figures anchored to AR p85 and RHP p104, top five concentration anchored to RHP p38 and p169 to 170. These are applications of the gate, not disagreements, so they take no row.
