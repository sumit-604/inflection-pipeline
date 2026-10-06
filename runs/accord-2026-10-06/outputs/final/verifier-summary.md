# ACCORD verifier summary (phase 1)

Run runs/accord-2026-10-06, dated 2026-10-06. Scope: Verifier A, Verifier B, Verifier D, and the Gate 0 plus Emerging Moat half of Verifier C. The valuation half of Verifier C runs in phase 3.

## Confidence delta (outputs/blocks/confidence.yaml)

| Component | Value | Block | Basis |
|---|---|---|---|
| numerical_acceptance | 97 | B12a | 812 checked; mandatory tier 212 of 212 (OR-32) |
| redflag_coverage | 62.5 | B12b | 5 of 8 material caught in full (8 of 8 if partial catches count) |
| framework_adherence | 93.5 | B12c | 72 of 77 phase 1 rules; valuation component pending phase 3 |
| peer_utilisation | NOT APPLICABLE | B12d | 2 of 3 peers substantive; denominator 3 is below 4; reported as a count |
| overall | 62.5 | confidence.yaml | Set by redflag_coverage. Band 60 to 74: PROCEED verdicts move down one level |

REWORK triggers: none. No CONFIRMED Verifier A CRITICAL. No acceptance rate below 60% on a denominator of 4 or more (OR-29). Verifier A identity check: 0 CRITICAL rows, nothing to strike.

## Acceptance rates and counts

| Verifier | Model | Acceptance rate | Denominator | CRITICAL | MAJOR | MINOR | Other counts |
|---|---|---|---|---|---|---|---|
| A, numerical (B12a) | claude-sonnet-5-5 | 97% | 812 numbers (212 mandatory, about 600 sample) | 0 | 3 | 4 | 5 false positives struck; material universe 1,452 |
| B, concall red flags (B12b) | claude-opus-5-5 | 62.5% | 8 material flags | 0 | 4 | 8 | 23 independent flags: 12 caught, 7 partial, 4 missed (all MINOR); promise spot checks 5 of 5 confirmed |
| C, framework, phase 1 (B12c) | claude-opus-5-5 | 93.5% | 77 rules (Gate 0 50, Emerging Moat 27) | 0 | 0 | 7 | valuation and expectation ledger pending phase 3 |
| D, peer coverage (B12d) | claude-sonnet-5-5 | 100% | 3 peers | 0 | 0 | 3 | 2 substantive confirmed; 0 unsupported; all 11 peer questions addressed |

## Findings, sorted by severity

### CRITICAL

None from any verifier.

### MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A | 01-gate0.md Block D note under the D1 to D4 table | "Excluding all FDs, cash eq. is Rs 13.43 Cr" is mislabelled. Rs 13.43 Cr (1,342.70 lakh, AR p.79) includes FDs under 3 months of Rs 6.00 Cr (Note 16, AR p.90). Excluding all FDs: 2.05 + 740.65 = 742.70 lakh = Rs 7.43 Cr, below borrowings of Rs 8.83 Cr. Net debt Rs 1.40 Cr on that basis; D1 would read 4, not 5. D1 as scored uses full cash Rs 22.33 Cr and is unaffected. source_fidelity: true |
| 2 | A | 01-gate0.md Block F, M3 capital efficiency | FAT median 13.5x does not reproduce. Median of 15.3, 15.7, 11.2, 8.8 is 13.25x; from the screener Data_Sheet 13.2x; six year median 12.0x. M3 score unaffected. source_fidelity: false |
| 3 | A | 04-bizmodel.md Section 5 summary card, WC intensity line | CCC "about 151 days (calc)" does not reproduce. Report's own figures give 113 + 146 minus 136 = about 123 days (AR p.77 to 78: DSO 113.4, DIO 145.6, DPO 136.4). Rating "High" unchanged. source_fidelity: false |
| 4 | B | B05 2C, 4D | R1: FY26 called "steady growth and improved profitability" (Tr. L162 to 163). Filed: revenue minus 11.3%, PAT minus 24.2%, EBITDA margin 11.68% to 10.39%, H2 revenue minus 26.4%, H2 PAT minus 40.3% (Deck L1211 to 1225, L1243 to 1248; AR p.55 L1650 to 1668). H2 question answered with the full year gap (Tr. L194 to 197). Status: PARTIALLY CAUGHT |
| 5 | B | B05 2A P9, timeline_slippages | R5: prospectus placed IPO machinery in the existing E-11 unit with 1,424.11 sq m free against 700 sq m needed (Prospectus L5468 to 5496). Call said "for the new plant only" (Tr. L290 to 299). AR variation reason says machinery needs new built up space first (AR p.51 L1441 to 1453). Rs 700 lakh = 53.7% of the object moved; 0.00% of machinery spent (AR p.50 L1394 to 1396). Status: PARTIALLY CAUGHT |
| 6 | B | B06 Q1, Q5, 2B, PVC-SHARE-OUTLIER; B05 3C | R6: "we will not lose anything into the price variation" (Tr. L449 to 450), with only an oil availability remark (Tr. L400 to 401), weeks after Shilchar (S-M26 L318 to 320) and Danish (D-M26 L569 to 577, L599 to 600) reported oil up 100% and firm price hits. AR blames "competitive pricing" for the FY26 margin fall (AR p.82 L3114 to 3116). About Rs 19.4 Cr of filed H1 FY27 orders sit in Accord's own fixed price window (calc, mixed GST). Status: PARTIALLY CAUGHT |
| 7 | B | B05 ORDER-FILING-GAP, 4D MEDIUM; B06 Part 2E item 8, analyst_note | Pipeline flag "about Rs 17 Cr of Aditya Birla orders not filed" is contradicted. 29-Jun-26 filing Rs 19.97 Cr incl GST = Rs 16.93 Cr excl GST (calc; 20260629 L84, L94 to 107) plus 23-Sep-26 LOA Rs 20.02 Cr excl GST (20260923-d54c506f L91 to 111) = Rs 36.95 Cr against Rs 37 Cr in the H1 update (L78 to 80). Residue: the June filing did not name the end project owner. Status: NOT SUPPORTED |

### MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 8 | A | 03-ardeep.md 6E row 2 (Pros. p.123); 09-tam.md Section 1A (Pros. p.121) | "no export operations" sits at Prospectus [page 125], line 9067. Stages 4 and 7 cite p.125 correctly. Quote exists; two cited pages do not hold it. source_fidelity: true |
| 9 | A | 08-promoter.md 3C, lock in and pledge rows | 41,14,660 shares and the 3 year lock in are at Prospectus [page 70], lines 5074 to 5089, not p.85. Pledge line 5197 is on [page 71], not p.94. Values correct; Feb-2029 end date is the stage's own derivation. source_fidelity: true |
| 10 | A | 05-concall.md and 07-emoat.md transcript cites | Report mixes printed "Page N of 14" labels with [page N] markers (e.g. Tr. p3 L146 to 147 is marker p4). Every quoted figure exists at its cited line. Page label inconsistency only. source_fidelity: false |
| 11 | A | 01-gate0.md E2, E3, LBF-2, M6 anchors | Document named, page missing: 100.00% and 84.94% at Prospectus [page 68] lines 4918/4928; pledge line 5316 ([page 73]); Note 17 at AR [page 90]; R&D NIL at AR [page 55] line 2608. Weak anchor. source_fidelity: false |
| 12 | B | not in B05 or B06 | R16: 25 of 35 sets "manufactured" worth Rs 21 to 22 Cr, but FG plus WIP fell from 1,178.68 to 1,150.01 lakh at 31-Mar-26; fits only if WIP plus new stock in transit is nearly all this order [INFERENCE] (Tr. L202 to 203; AR Note 14 L4412 to 4416). Separating observation: 30-Sep-26 inventory note. Status: MISSED |
| 13 | B | not in B05 or B06 | R17: Siemens called a partner in the deck and prospectus summary and a competitor on the call; prospectus detail shows only SGB-SMIT "expressed mutual interest" (Deck L1569 to 1574; Prospectus L8524, L8994 to 8999; Tr. L346, L351). Status: MISSED |
| 14 | B | not in B05 or B06 | R21: filing hygiene. 23-May-26 filing says "Gabion Technologies India Limited has received" the orders; pre listing CIN U31500 on four post listing filings; 24-Jun-26 filing names Sunsure under a name withheld note (20260523 L7, L34 to 35; 20260611 L61; 20260624 L61, L77 to 85; 20260803 L64). Status: MISSED |
| 15 | B | B05 1A T11 | R23: 17.60 MVA inverter duty transformer called "the highest rating in the transformer industry for the renewable segment" (Tr. L123 to 125), recorded as fact; PENDING LIVE VERIFICATION. Status: MISSED |
| 16 | B | B05 3D | R18: global presence claimed (Q1 update L83; AR L1685, L2992 to 2993) against nil FX earnings FY25 to FY26 (AR L2609 to 2613) and "no export operations" (Prospectus L9065 to 9069). Status: PARTIALLY CAUGHT |
| 17 | B | B05 1C NEW row | R19: B05 dates Schneider, Lucy and PGCIL as July items; all three are in the 1-Jun-26 deck (Deck L515 to 543), Schneider and Lucy in the prospectus (L9012 to 9036). Residue: the call left them out of the spoken approvals list (Tr. L136 to 139); PGCIL scope for a 33 kV maker unverified. Status: OVERSTATED / PARTIALLY CAUGHT |
| 18 | B | B05 1A T10, 4A row 8 | R20: Moscow counterparty named three ways (Tr. L153, L537, L548); Russia sanctions in prospectus risk factors (L2988 to 2989) not addressed. Status: PARTIALLY CAUGHT |
| 19 | B | B05 4C (via B03) | R22: AR narrative claims "improvement in receivables turnover" and "comfortable debt servicing" against its own table: 4.48 to 3.22 and DSCR 0.81 (AR p.82 L3091, L3102 to 3106; p.83 L3127 to 3128). Status: PARTIALLY CAUGHT |
| 20 | C | B01 G26 E3 promoter pledge (B01 L127, L129, L135) | E3 scored 5 on 0% pledge at the prospectus date; post listing pattern NOT FOUND. Recomputed E3 0, Block E 8, core 60, grand total 75. Decision effect: none; AVERAGE via DB4 holds (F1) |
| 21 | C | B01 G48 dashboard (B01 L141 to 155) | Moat profile bars absent; moat shown as a table only. No score effect (F2) |
| 22 | C | B01 G30 M3 shown figure (B01 L145) | FAT median 13.5x; recomputed 13.25x. M3 5 stands (F3) |
| 23 | C | B01 G38 M11 proxy (B01 L153) | Proxy must be declared in data_notes; score 1 stands on every split; strict NOT FOUND reading gives 0, moat 14, grand total 79. Moats confirmed 3, MODERATE (F4) |
| 24 | C | B07 E06 C1 (B07 L134, L278) | C1 scored 1.0 with every listed C1 signal absent or NOT FOUND. Recomputed C1 0, em_score 7.0, NONE unchanged (F5) |
| 25 | C | B07 E17 I2 (B07 L204 to 209) | I2 table omits scored C1, C2, G1. I2 stays 0; no sacrifice named (F6) |
| 26 | C | B07 E21 register (B07 L279, L319) | C2 scored 1.0 and also registered. Drop the row or limit it to the unfiled FY26 and H1 FY27 tables; register never scored (F7) |
| 27 | D | B06 Part 1 Q5, Q11; D-M26 p8 L300 to 308, S-M26 p8 L318 | Q5 and Q11 VERIFIED on direction only; the Accord terms (15% advance, 3 month fixed; guidance size) are not supported. Read as direction verified |
| 28 | D | B06 Part 3 and input_gaps | Voltamp coverage is Data_Sheet only (no transcript exists); labelled UNUSED for call evidence and not credited. Handled correctly |
| 29 | D | DANISH-Concall_May_2026 L343 to 346, L482, L575, L600; SHILCTECH Aug_2026 L101, L122; May_2026 L318, L604 to 612; Apr_2025 L77, L117; Oct_2025 L251 | Verbatim spot check passed on 14 of 14 sampled quotes; some line ranges drift 1 to 4 lines. No finding on content |

## Verifier notes carried as written

- Verifier A, struck under rule 5b (5): 16.69 vs 16.685 lakh per MVA (rounding); GM Operations tenure 70 vs 69 days (counting convention); Rs 265.3 vs 265.4 Cr (rounding); Shilchar FY25 inventory days 54 vs 54.5 (rounding); stage 8 CFO exit "35 days" vs "41 days" (different reference dates, both stated).
- Verifier A, not checkable from supplied sources: web figures in 09-tam (CRISIL Rs 33,000 Cr, MarketsandMarkets, IMARC, Ken Research, MNRE GW, Waaree 1,275 MVA order, TARIL Rs 2,395 Cr, 48.6% DT share; arithmetic recomputed and reproduces) and in 08-promoter (chittorgarh close and anchor list, aggregator holdings, indiamart). Results PDF pp3 to 19 (image only) cited by no report.
- Verifier B, credibility grade: "lower: D. B05 keeps the unfiled Rs 1,600 Cr NHEV LOI claim out of the grade and misses the FY26 'improved profitability' misstatement and the IPO-variation reason that contradicts the prospectus; delivered items are facts the company controls. C stands only if H1 FY27 results reconcile with the pass-through and deferral claims."
- Verifier B, method limit: one company transcript, so no cross quarter evasion test ran and no CRITICAL can arise under that rule.
- Verifier C: recomputed_decision concurs on phase 1 scope: Gate 0 AVERAGE, Emerging Moat NONE, combined AVERAGE.

## Verifier disagreements

None this run. No downstream step relied on, cleared or argued around a Verifier A source fidelity finding (finding 1, Block D ex FD cash label; finding 8, export quote page cite; finding 9, lock in and pledge page cites). The synthesis carries the corrected Rs 7.43 Cr figure. See verifier-disagreement-log.md.
