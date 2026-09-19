# eMudhra Ltd (EMUDHRA): verifier summary, phase 1, run 2026-09-19

Current = round 2 blocks (B12b, B12c, B12d re-run on the corrected B01, B05, B06, B07). B12a ran once; no numbers it audited changed except the B01 FCF and working capital items, which B12c round 2 re-audited. Round 1 copies: B12b-r1, B12c-r1, B12d-r1.

## Confidence delta (phase 1)

| Component | Score | Source |
|---|---|---|
| Numerical acceptance | 100 | B12a: 27 of 27 material figures matched; 0 CRITICAL, 0 MAJOR |
| Red flag coverage | 71 | B12b r2: 5 of 7 material (MAJOR) caught, partials included; material found 7 |
| Framework adherence | 89.4 | B12c r2, phase 1 scope: 59 of 66 rules (Gate 0 42, EM 24); valuation half PENDING PHASE 3 |
| Peer utilisation | 91.7 | B12d r2: 11 of 12 peer quarters SUBSTANTIVE (PROTEAN Dec-2025 business update call CITED ONLY) |
| Overall | 71 | set by red flag coverage; band 60-74 |

## Acceptance rates

| Verifier | Model | Round 1 | Round 2 (current) | Counts (current) |
|---|---|---|---|---|
| A, numerical | claude-haiku-4-5 | 100 | not re-run (100 carried) | 0 CRITICAL, 0 MAJOR, 0 MINOR |
| B, red flag coverage | claude-opus-5 | 75 | 71 | 0 CRITICAL, 2 MAJOR, 7 MINOR |
| C, framework (Gate 0 + EM only) | claude-opus-5 | 82.5 | 89.4 | 0 CRITICAL, 1 MAJOR, 6 MINOR, 1 OBSERVATION |
| D, peer utilisation | claude-sonnet-5 | 83 | 83 | 0 CRITICAL, 1 MAJOR, 1 MINOR |

REWORK trigger: none. No Verifier A CRITICAL; every acceptance rate is 60 or above.

Verifier A source fidelity: 27 figures checked across B01, B03, B04, B05, all source_fidelity true, zero mismatches. No figure is struck. No downstream step disagreed with a Verifier A finding.

## Current findings (round 2), sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| B | B05 2B, 2D, 4C governance row | MISSED 3i non-disclosure: allegations known since Jan-2024, silent on the Q3 FY26 call held 03-Feb-2026 (complaint filing date); "proactive" framing wrong. Anchor: 3i special call [page 6]; Reg 30 04-Feb-2026 [page 1] |
| B | B05 1C, 4A trigger 1 | MISSED: Q1 FY27 26.2% EBITDA margin partly lifted by lower low margin token sales per management; guide ~25%; affects margin bridge evidence. Anchor: Q1 FY27 VS [page 20], [page 10] |
| C | B01 Block B / B4 (+ operating rules 5, 6); F1 | B4 scored on FY25 as "earliest" while A4 uses FY19; rule 5 requires N/A and 0 for the missing FY19 payables; Block B 7, deal breaker 2, GOOD not GOOD+ (core 69). Filed: B4 5, Block B 12, core 74, GOOD+. Routes to the operator ruling B01 already raised |
| D | 06-peers.md Q6 verdict text, Part 2A, Part 3 peer coverage map row, YAML flags entry (4 locations) | NEWGEN Q4FY26 (May-2026) "serious impact last quarter" Middle East quote cited at p.8; quote confirmed present, but after the [page 9] marker (line 382). Anchor off by one page on the report's single strongest independent corroboration; finding unaffected once the page is corrected |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| B | B05 1C bolt-on acquisition | Q3 stance misread as "live consideration"; transcript says "not evaluating any acquisition... may not be required". Anchor: Q3 FY26 VS [page 11] |
| B | B05 2A row 5, 4D | UAE promise OVERSTATED as missed: Q3 promise was DC commissioning, Q4 reports DC operating; QTSP licence first timed in Q1. Anchor: Q3 [page 9]-[page 10]; Q4 [page 4]; Q1 [page 8] |
| B | B06 2B, flags, pricing_inputs | NOT SUPPORTED attribution of the stock in trade item to the Jul-2026 call; B05/B06 contradict; hardware inflation read across withdrawn on an unsound premise. Anchor: Q1 FY27 [page 10]; Q3 FY26 [page 12]-[page 13] |
| B | B05 1B | Guidance drift not recorded: Enterprise 25-30% to 20-25%; Trust 20% to 15-20%. Anchor: Q4 [page 9]; Q1 [page 14], [page 21] |
| B | B05 3C | "Full numbers given" overstated; AI Cyber Forge revenue untracked. Anchor: Q3 FY26 [page 6] |
| B | B05 2A row 7 | Attribution of organic shortfall to Trust decline not stated explicitly by management. Anchor: Q1 FY27 [page 12] |
| B | B05 2D, B06 2A | NEWGEN ME/EMEA collections slowdown and DSO pressure not connected to eMudhra's receivables silence. Anchor: NEWGEN May-2026 [page 4], [page 11] |
| C | B01 M6 tier bands; F2 | M6 scored 0 on a "consistently" test that binds only the 5 point tier; FY26 product development 601.00 Mn = 8.57% of revenue meets the 3 point tier text; possible 3 (F 20, grand 94, moats 5, still STRONG); no classification effect. The 814.21 Mn label on the 8.6% is wrong (814.21 = 11.6%) |
| C | B01 ROCE formula (EBIT/(TA-CL)); F3 | ROCE computed on a substitute basis (Equity+Reserves+Borrowings, FY26 14.51%); prompt formula gives FY26 12.92% (1,055.63 Cr CE), FY25 14.08% (AR p.216); A1 3, A2 3, A4 0 unchanged |
| C | B01 YAML block_b_trend; F4 | Not in the schema enum; use improving / stable / deteriorating with one number |
| C | B07 evidence_mix; F5 | Claim 10 and inference 6 counts not itemised in the report; unverifiable |
| C | B07 C2 score vs evidence tier; F6 | C2 credited at documented tier (HL 2 x 1.0 = 2.0) on customer additions while the concentration test is unconfirmed; inference tier 0.5x = 1.0; em_score 21.1 (filed 22.1); band MODEST unchanged |
| C | B07 H2 strength label; F7 | H2 labelled Strong at raw HM 3; Moderate (same raw as A4, E1, H1) |
| D | 06-peers.md Part 2 and Part 2D text, cited "(p.9, 2D)" | QUICKHEAL Q1FY26 (Aug-2025) tier one BFSI DPDP quote is a two part splice: "we have won large BFSI deal in this quarter" on p.5 (line 191), "It's a tier one insurance Company" on p.9 (line 388); split not disclosed; underlying finding sound |

### OBSERVATION

| Verifier | Location | Finding |
|---|---|---|
| C | prompts/07 Section 6D; O1 | Section 6D names an 8 label combined matrix that no rule source defines; prompt defect, not a stage fail. Operator to supply the lookup table |

Verifier B, pipeline flag not supported (round 2): B06 2B correction/flags say "eMudhra's own Jul-2026 call attributes the stock in trade item to DSC token partner stocking and a FIPS 140-3 transition"; the Q1 FY27 transcript never mentions stock in trade; contradicts B05 2A row 6 ("never revisited").

Verifier B, promise delivery spot checks (round 2): 6 checked, 5 confirmed, 1 wrong. Credibility grade: concur, C (Mixed).

Verifier C, recomputed values (round 2): Gate 0 GOOD (filed GOOD+); em_score 21.1 MODEST (filed 22.1 MODEST); combined assessment GOOD (filed GOOD+). Valuation and expectation ledger PENDING PHASE 3.

## Closed in correction round (round 1 findings the corrections closed)

| Verifier | R1 severity | Location | Round 1 finding | Closed by |
|---|---|---|---|---|
| C | CRITICAL | B01 Block B / B4, deal breakers, classification | B4 scored N/A on a false premise; payables clean at AR p.216 and Note 18 p.255 | B01 Correction 2: B4 = 5 (WC days 81.12 to 69.21), Block B 12. The window question stays open as the round 2 MAJOR (F1) |
| C | MAJOR | B01 Block A / A2 | Mixed computed and AR disclosed ROCE series; minimum on the 15% edge | A2 = 3 on one computed series (min 14.41%, FY24); Block A 10 |
| C | MAJOR | B07 Section 3/5 E1 | First mover attribute on unanchored inference, scored at max | E1 HH to MH; em_score 23.1 to 22.1; band MODEST unchanged |
| C | MAJOR | B07 Section 2C | Capex embedded growth on a mismatched FAT basis (22.6%) | Rebased to run consistent FAT 0.97x: 4.0%; range 4.0-22.6% named |
| C | MINOR | B01 D1 | FY25 cash column used for FY26 | FY26 cash Rs 65.20 Cr; net cash Rs 36.42 Cr; score unchanged |
| C | MINOR | B01 D4 | Standalone current ratio used | Consolidated 2.76x (AR p.216); score unchanged |
| C | MINOR | B01 M1/M2/M5 | Change in Inventory sign reversed in EBITDA | FY26 EBITDA Rs 159.12 Cr, 22.68%; scores unchanged |
| C | MINOR | B01 M12 | N/A label on false premise | 69.21 days, score 0 |
| C | MINOR | B07 R1 / 4C | Narrative says tempered, score is max | Narrative and score reconciled; R1 stays HH = 4 |
| C | MINOR | B07 evidence_mix / Section 3 count | Documented count 24 unreconciled with 19 item recount | Documented reconciled to 19 (claim and inference itemisation still open as round 2 F5) |
| C | MINOR | B07 Section 1C | Estimated Services FY27 growth filled | Removed; marked NOT FOUND |
| B | MAJOR | B05 3C/1C/4A | MISSED Cryptas profitability narrative drift and B.V. loss | Added to B05 flags and red flags; credibility B to C |
| B | MAJOR | B05 and all reports | MISSED promoter link to the 3i Infotech stake | Added to B05 as the Capital MXT connection (Q1 FY27 p.23-24); PENDING LIVE VERIFICATION |
| B | MAJOR | B05 4E/4C | UNDER-WEIGHTED 3i matter | Re-rated Low to MEDIUM |
| B | MAJOR | B05 4E | UNDER-WEIGHTED the ~15% ROE "we can maintain" admission | Re-rated Low to MEDIUM |
| B | MAJOR | B05 4E/2D | NOT SUPPORTED: SEBI complaint status said never addressed | Retracted (addressed May-2026 call p.7) |
| B | MAJOR | B06 Q8 / Part 4 / flags | NOT SUPPORTED: H-1B CONTRADICTED verdict; misanchored quote | Q8 moved to UNVERIFIABLE; quote re-anchored to NEWGEN Jan-2026 p.16 |
| B | MINOR | B05 2A row 7 | Q3 FY26 organic 11-12% omitted | Context added to row 7 (Trust attribution point stays open as a round 2 MINOR) |
| B | MINOR | B05 2A row 5 / 1C | Q4 not silent; UAE DC stated operating | DC operating recorded; licence named as the pending item (outcome label stays open as a round 2 MINOR) |
| B | MINOR | B05 2E | OVERSTATED repeated deflection | repeated_evasions now empty |
| B | MINOR | B06 2B | OVERSTATED hardware inflation hypothesis | Withdrawn (its replacement attribution is the round 2 NOT SUPPORTED item) |
| B | MINOR | B05 2A row 2 | MISSED Trust beat quality (tokens, partner stocking) | Pulled forward demand caveat added |
| B | MINOR | B05 | MISSED eSign volume drift, 4 lakh to 3 lakh per day | Added as a minor flag |
| B | MINOR | B06 | MISSED QUICKHEAL DPDP lead vs PrivaTrust | Added to B06 risks and flags |
| B | MINOR | B06 2D/Q7 | MISSED PROTEAN eSign Pro direct competition | Added; "structurally distinct" withdrawn |
| B | MINOR | B06 Q5 | MISSED NEWGEN margin partial contradiction of the chairman's peer margin claim | Added with scope caveat |
| B | MINOR | B05 2A row 3 | MISSED adjusted EBITDA framing and Q4 margin dip | Row 3 moved delivered to partial (Q4 FY26 22.4%) |
| D | MAJOR | B06 Q8 verdict / Part 4 / YAML | NEWGEN H-1B quote cited Q4FY26 p.10; true source Q3FY26 (Jan-2026) p.16 | Re-anchored |
| D | MAJOR | B06 Q6 verdict / Part 2A | PROTEAN war quote cited Q1FY27 p.11; true source Q4FY26 (May-2026) p.13 | Re-anchored |
| D | MAJOR | B06 Q5 verdict | PROTEAN 18.7% vs 10% comparison cited p.4; sits on p.11 | Split anchor p.5 and p.11 |

Round 1 findings not recorded as closed: B MINOR "B05 1C bolt-on acquisition raised in Q1 FY27 (KS [page 19])" (round 2 raises a related Q3 stance misread); B MINOR "B05 3B R&D capitalisation not tied to EBITDA or peer R&D in the concall read" (carried in the notes and business model stages); B MINOR "IAM not taken to the US (May-2026 KS [page 11])" (no matching correction found in B05).
