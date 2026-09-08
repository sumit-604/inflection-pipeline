# VERIFIER SUMMARY — FRATELLI, run 2026-09-07, PHASE 1

## Confidence delta and acceptance rates

| Component | Score | Verifier | Model | Counts |
|---|---|---|---|---|
| Numerical acceptance | 87 | A (B12a, run 2) | claude-haiku-4-5 | 61 numbers audited. 0 CRITICAL, 7 MAJOR, 1 MINOR |
| Red flag coverage | 39 | B (B12b) | claude-opus-4-8 | 38 flags found independently. 15 caught, 7 partially caught. 2 CRITICAL, 15 MAJOR, 6 MINOR |
| Framework adherence | 82 | C (B12c) | claude-opus-4-8 | 47 of 57 rule checks passed. 0 CRITICAL, 1 MAJOR, 9 MINOR |
| Peer utilisation | 100 | D (B12d) | claude-sonnet-5 | 12 of 12 peers used substantively. Citation acceptance separately 60%: 12 of 20 spot checked citations correct. 0 CRITICAL, 6 MAJOR, 2 MINOR |
| **Overall** | **39** | orchestrator | | Minimum of the four. Band: FORCED REWORK |

Framework adherence scope: PARTIAL. Gate 0 (B01) 26 of 28 = 93%; Emerging Moat (B07) 21 of 29 = 72%. The valuation audit is PENDING PHASE 3, since B10 and B11 do not exist.

Verifier A ran twice. Run 1 raised two CRITICAL findings, on the Gate 0 FY24 and FY25 revenue figures. The orchestrator neither cleared nor downgraded them. It re-invoked Verifier A once, per the LESSONS.md remedy, with a widened coverage brief. Run 2 opened screener-Data_Sheet.csv and both annual reports, found both figures present in the source the report named and labelled as screener data rather than presented as audited consolidated, and Verifier A itself reclassified both to MAJOR. Verifier A remains the deciding authority on both. All three movements, the two reclassifications and the warrant forfeiture correction, are already recorded at outputs/final/verifier-disagreement-log.md.

---

## VERIFIER A — numerical (B12a, run 2)

61 numbers audited across all 11 reports. Priority: revenue 12, balance sheet 14, cash flow 8, working capital 10, share and warrant 6, segment expense 5, peer figures 6. No fabricated figure found; all MAJOR findings are anchored to source PDFs.

| Severity | Location | Claimed | Source truth | Note | source_fidelity |
|---|---|---|---|---|---|
| MAJOR | 01-gate0.md, p.35, LOAD-BEARING FACT 1 | FY2025 revenue Rs 276.25 cr (screener data) | Screener CSV row 11 confirms 276.25 cr; AR FY26 consolidated P&L shows 30,209.66 lakh = Rs 302.10 cr | Figure exists in screener and is labelled screener data, not presented as audited consolidated. Screener FY25 is 9.3% below AR consolidated, a Rs 25.85 cr gap, causing base mixing in downstream working capital calculations. Not fabrication; basis mismatch | false |
| MAJOR | 01-gate0.md, p.96, Block A ROCE | FY2024 revenue Rs 421.35 cr (screener data) | Screener CSV row 11 confirms 421.35 cr; AR FY25 consolidated P&L shows 45,107.48 lakh = Rs 451.07 cr | Screener FY24 is 7.1% below AR consolidated, a Rs 29.72 cr gap. Not fabrication; basis discrepancy | false |
| MAJOR | 02-notes-pass1.md, p.598 | 39.5% of the 5,57,650 warrants allotted Aug-2024 lapsed | AR FY26 p.51-52 and p.56 show 3,63,150 of 5,57,650 = 65.1%; confirmed by 08-promoter.md line 338 and 05-concall.md line 136 | 39.5% of 557,650 is about 220,272, not 363,150. Material numerical error. ALREADY SUPERSEDED UPSTREAM: pass 2 corrected it on source; the consolidated B02 block, B05 and B08 all carry 65.1%. Error confined to the pass 1 working artifact | **true** |
| MAJOR | 01-gate0.md, p.99-100, B4 WC Days table | FY2025 payable days 29.6 (screener revenue basis) | AR consolidated: 2,241.37 lakh over 30,209.66 lakh x 365 = 27.07 days (AR FY26 p.144 Note 19) | Base mixing: screener FY25 revenue with AR consolidated payables. Difference 2.5 days | false |
| MAJOR | 01-gate0.md, p.99, B4 WC Days table | FY2025 inventory days 109.0 (screener revenue basis) | AR consolidated: 8,250.19 lakh over 30,209.66 lakh x 365 = 99.73 days (AR FY26 p.144 Note 9) | Base mixing: screener FY25 revenue with AR consolidated inventory. Difference 9.3 days | false |
| MAJOR | 01-gate0.md, p.99, B4 WC Days table | FY2024 inventory days 80.2 (screener revenue basis) | AR consolidated: 9,255.37 lakh over 45,107.48 lakh x 365 = 74.9 days (AR FY25 p.143 Note 9 comparative) | Base mixing: screener FY24 revenue with AR consolidated inventory. Difference 5.3 days | false |
| MINOR | 01-gate0.md, p.96, Block A ROCE table | FY2026 equity Rs 135.96 cr (screener data) | Screener 43.47 + 92.49 = 135.96 cr; AR FY26 consolidated 13,596.36 lakh = 135.96 cr, matched | Verified. Screener and AR reconcile when the business is wine only | false |
| MINOR | 01-gate0.md, p.50, Contingent liabilities | Rs 37.88 cr (AR FY26, Note 39) | AR FY26 p.150 Note 39 consolidated contingencies 3,787.90 lakh = Rs 37.88 cr, matched | Verified clean | false |

---

## VERIFIER B — red flags (B12b)

Independent re-read of the same five company transcripts and twelve peer transcripts. 38 red flags found independently; 15 caught upstream, 7 partially caught, giving coverage of 39%. Promise delivery spot checks: 6 checked, 6 confirmed, 0 wrong. Credibility grade concurred at D. pipeline_flags_not_supported: none.

### B1. Flags the pipeline missed

| Severity | Item | Anchor |
|---|---|---|
| CRITICAL | Repeated evasion, 2 or more quarters: Shotgun unit economics and monthly run rate refused in Q1FY26 ("I will not be commenting on that as of now") and deferred in Q3FY26 ("happy to share once the financial year has ended"); Q4FY26 gave Rs 18 cr against Rs 20 cr promised, still no run rate or per case economics | Concall_Q1FY26_Aug2025_Transcript.pdf p.9; Concall_Q3FY26_Feb2026_Transcript.pdf p.11; Concall_Q4FY26_Jun2026_Transcript.pdf p.8 |
| CRITICAL | Repeated evasion, 2 or more quarters: cost structure refused as sensitive in Q1FY26 (margin bridge) and in Q4FY26 (breakdown of Rs 85 to 86 cr other expenses, 47% of FY26 revenue) | Concall_Q1FY26_Aug2025_Transcript.pdf p.9; Concall_Q4FY26_Jun2026_Transcript.pdf p.15 |
| MAJOR | Peer contradiction: Sula says Maharashtra wine duty did not change by a single rupee and that Sula hit an all time high share there, against Fratelli's spirits excise attribution for its 16% Q1FY26 decline | SULA-Concall_Aug_2026_Transcript.pdf p.10; SULA-Concall_Nov_2025_Transcript.pdf p.15 vs Concall_Q1FY26_Aug2025_Transcript.pdf p.5 |
| MAJOR | Peer contradiction: Sula says the entire wine category degrew in Karnataka in H2 FY26 and Q1 FY27, against Fratelli's H2 "market conditions began to normalize" narrative | SULA-Concall_Aug_2026_Transcript.pdf p.10-11 vs Concall_Q4FY26_Jun2026_Transcript.pdf p.3 |
| MAJOR | Peer contradiction: Sula holds pricing on wines above Rs 1,200 because of EU FTA duty cuts; Fratelli claims exposure begins only above Rs 2,000 and is 7% of revenue | SULA-Concall_May_2026_Transcript.pdf p.10 vs Concall_Q4FY26_Jun2026_Transcript.pdf p.7 |
| MAJOR | Dodged question: analyst asks about super premium (Rs 1,050 to 2,000) migration to European wines; the answer covers the above Rs 2,000 segment and pivots to a 55% share claim | Concall_Q3FY26_Feb2026_Transcript.pdf p.15 |
| MAJOR | FTA position stated three incompatible ways and a confident forecast falsified in one quarter: "wine has not been covered" (Q4FY25), "no concession for wine, no further concessions beyond Australia" (Q2FY26), then duties to 20 to 30% (Q3FY26), presented as routine news rather than a corrected forecast | Concall_Q4FY25_Jun2025_Transcript.pdf p.10; Concall_Q2FY26_Nov2025_Transcript.pdf p.3 and p.8; Concall_Q3FY26_Feb2026_Transcript.pdf p.4 |
| MAJOR | Auditor Emphasis of Matter and going concern basis at the parent, plus derecognition of the DTA with Rs 361.12 lakh charged back to P&L, never mentioned on the Q4FY26 call held three days after the filing; falsifies the CFO's Q4FY25 deferred tax answer | Results_Q4FY26_and_FY26_2026-05-30.pdf p.4, p.11, p.13 vs Concall_Q4FY26_Jun2026_Transcript.pdf |
| MAJOR | Q3FY26 guidance of "roughly 7% revenue growth with a far better Q4" was issued with six weeks left in the year and implied Q4 of about Rs 48 cr; audited Q4FY26 was Rs 35.30 cr, a 25% miss | Concall_Q3FY26_Feb2026_Transcript.pdf p.14 vs Results_Q4FY26_and_FY26_2026-05-30.pdf p.16 |
| MAJOR | Operating leverage breakeven threshold moved from "around INR210 crores, INR215 crores" to "around INR240 crores" in two quarters with no explanation; management's own FY24 revenue was Rs 215 cr | Concall_Q2FY26_Nov2025_Transcript.pdf p.9 vs Concall_Q4FY26_Jun2026_Transcript.pdf p.12 |
| MAJOR | Premium segment decline stated at four different values: minus 10% and minus 13 to 14% on the same Q3FY26 call, then minus 16% and minus 15% on the same Q4FY26 call | Concall_Q3FY26_Feb2026_Transcript.pdf p.8 and p.15; Concall_Q4FY26_Jun2026_Transcript.pdf p.4 and p.12 |
| MAJOR | Luxury metrics oscillate: share 50 to 55 to 50 percent, contribution 6 to 13 to 7 percent, growth 18% Q2, 20% 9M, 15% FY implying near zero Q4 luxury growth sold as strength; claims do not close against the managing director's own Rs 50 cr sizing of the above Rs 2,000 category | Concall_Q1FY26 p.4; Q2FY26 p.3 and p.14; Q3FY26 p.12; Q4FY26 p.4 and p.8 |
| MAJOR | TiLT stagnation admitted only in Q2FY26 ("they have not yet grown in any remarkable fashion") after three calls of growth framing; the TiLT share question answered circularly with a distribution footprint; Q4FY26 returns to a 90% market share claim | Concall_Q2FY26_Nov2025_Transcript.pdf p.7 vs Concall_Q4FY25_Jun2025_Transcript.pdf p.6 and Concall_Q4FY26_Jun2026_Transcript.pdf p.13 |
| MAJOR | RTD realisation per case fell about 10%, Rs 2,000 in H1 to Rs 1,800 for the full year, while states expanded from 11 to 18; Rs 18 cr delivered against Rs 20 cr promised. B05 calls the Shotgun record "the one genuinely clean positive" | Concall_Q2FY26_Nov2025_Transcript.pdf p.16 vs Concall_Q4FY26_Jun2026_Transcript.pdf p.3 and p.8 |
| MAJOR | WIPS subsidy: the CFO affirmed an "INR8 crores to INR12 crores" range he never gave, having said Rs 8 cr; the subsidy exceeds claimed FY26 EBITDA; the WIPS receivable is never disclosed while Sula discloses Rs 88 cr quarterly; the Mar-2028 scheme expiry is never framed as a risk | Concall_Q1FY26_Aug2025_Transcript.pdf p.8; Concall_Q2FY26_Nov2025_Transcript.pdf p.9; SULA-Concall_Aug_2026_Transcript.pdf p.8 |
| MINOR | Composite: Sula's asset light partner built hospitality model contradicts the managing director's "revalidate your assumptions" correction of an analyst; the promoter family RPT postal ballot is never mentioned; exports reversed from "not enough to matter, frankly" to a 5% of revenue FY27 driver; solar 50 to 45 percent; touch points static at 25,000 for a year then plus 20%; Q4FY25 volume "almost same" then "about 10%"; two deadlines for the same 15 state target on one call; "the ongoing war" cited once and never explained | SULA-Concall_Aug_2026 p.11 vs Concall_Q1FY26 p.14-15; Results_Q4FY26 p.2; Concall_Q3FY26 p.8 vs Q4FY26 p.4 |

### B2. Findings against pipeline blocks

| Severity | Location | Finding | Anchor |
|---|---|---|---|
| MAJOR | B05 red_flags, LOW row | FY26 EBITDA claim misclassified as a minor reconciliation variance within plausible rounding or other income range. Claimed plus Rs 1.06 cr against audited consolidated minus Rs 4.56 cr including other income, minus Rs 7.78 cr excluding it; the gap is five times the claimed figure and reconciles only by excluding a Rs 5.21 cr holdco segment loss and adding Rs 3.22 cr other income, neither disclosed. Consolidated EBITDA deteriorated from minus Rs 1.82 cr in FY25. The same call carries a sign contradiction, plus Rs 1.06 cr against minus Rs 3.7 cr for Q4, not addressed. Should be HIGH under B05's own basis flag logic | Concall_Q4FY26_Jun2026_Transcript.pdf p.3, p.5, p.6, p.12; Results_Q4FY26_and_FY26_2026-05-30.pdf p.16; Results_Q1FY27_2026-08-11.pdf p.9 |
| MAJOR | B06 unverifiable / partially_verified | Market share claim filed as unverifiable when it is internally falsifiable: management's own Rs 1,000 cr domestic market against Rs 181 cr revenue gives 18%, not the 31 to 33% claimed across four calls; Sula alone is about Rs 600 cr. The basis, value against volume and MRP against net, is never stated | Concall_Q1FY26 p.7; Concall_Q3FY26 p.12 and p.14; SULA-Concall_Aug_2026_Transcript.pdf p.8; SULA-Concall_Nov_2025_Transcript.pdf p.13 |
| MAJOR | B06 risks_peers_raise | Competitor discounting logged as an unnamed risk rather than a peer contradiction of an affirmative claim: Fratelli asserts flat, disciplined discounts showing brand love four weeks after Sula predicted industry casualties, having itself conceded in Q3FY26 that trade promotions run higher than wished. Belongs in contradicted | SULA Nov-2025 p.15, Feb-2026 p.14, May-2026 p.10 vs Concall_Q3FY26 p.8 and Concall_Q4FY26 p.14 |
| MAJOR | B05 red_flags / B06 risks_peers_raise | Balance sheet deterioration carried only on the DSO leg: FY26 current borrowings rose Rs 71.62 cr to Rs 89.60 cr, inventory up 15% on flat revenue, cash Rs 0.08 cr, equity minus Rs 20.4 cr, finance cost Rs 13.26 cr against claimed EBITDA of Rs 1.06 cr, and zero debt disclosure on either H2 FY26 call | Results_Q4FY26_and_FY26_2026-05-30.pdf p.16-17; Concall_Q2FY26 p.8 |
| MINOR | B05 guidance table | FY27 EBITDA margin guidance of 10 to 12% listed, but its silent disappearance from the very next call is not flagged; Q1FY27 actual is 0.7% excluding other income | Concall_Q3FY26 p.9 and p.14; Concall_Q4FY26 p.10; Results_Q1FY27_2026-08-11.pdf p.7 |
| MINOR | B05 repeated_evasions | Equity fundraise recorded as an evasion "mooted by project deferral" rather than a stated plan withdrawn without acknowledgement, after an earlier "we are adequately funded" claim | Concall_Q1FY26 p.17; Concall_Q2FY26 p.8 and p.16; Concall_Q4FY26 p.15 |
| MINOR | B05 trigger 2 | FY27 30% guidance flagged low conviction but the bridge arithmetic not performed: plus Rs 55 cr needed, RTD doubling supplies Rs 18 cr, residual Rs 37 cr must come from a bottled business that declined 15 to 16% in FY26 | Concall_Q4FY26_Jun2026_Transcript.pdf p.7, p.8, p.12 |
| MINOR | B05 promise_delivery | Counters of delivered 1, partial 3, missed 8 do not tie to the six rows presented. Presentational only; the table is directionally sound on all six spot checks | (no anchor recorded) |

---

## VERIFIER C — framework adherence (B12c), Gate 0 and Emerging Moat scope only

57 rule checks: 28 on Gate 0, 29 on Emerging Moat. The valuation section is PENDING PHASE 3, rules_checked 0, because B10 and B11 do not exist. The business understanding narrative check is likewise not audited, since stage 13 had not executed when the verifier ran; the verifier records that as pending, not as a fail. Categories 21 and 22 are both present in B07 and both correctly scored 0 against their two leg and named sacrifice tests, so the stage 7 rework condition does not fire. Gate 0 AVOID and the B07 MODEST and AVOID reads survive every recomputation.

| Severity | Location | Claimed | Rule | Note and recomputation |
|---|---|---|---|---|
| MAJOR | B07 Section 3 B2 / Section 5 row B2 | Likelihood Medium-High x Impact Medium, raw 3, adjusted 3.0 | Section 5 matrix defines only High, Medium, Low per axis; HM or MH = 3, MM = 2 | Undefined likelihood level. One point swing lands em_score on the 12.0 MODEST or NONE boundary where the label depends on an unstated rounding convention. Recomputed em_score 11.7 against 12.7. No decision moves: EM stays far below the 25 threshold and combined_assessment stays AVOID |
| MINOR | B01 Block F, M8 | M8 = 0 | M8 ladder: "mentioned unquantified = 1", "none or purely digital = 0", no else clause | The 31,000 touchpoint network is quantified and growing, so both band conditions are false. Gap resolved downward. M8 = 1 gives moat_score 1 of 60; moats_confirmed still 0, class still NONE, AVOID unchanged. Disclosed and flagged by the stage, hence MINOR |
| MINOR | B01-gate0.yaml data_notes | data_notes omits both proxy bases | Field comment: data_notes carries proxy bases used | The FY17 to FY21 "Other Liabilities" proxy for current liabilities in capital employed, and the sales rather than COGS basis for working capital days, appear in the report body only. Downstream stages read the block |
| MINOR | B07 Section 5 row H2 | Blended spoken and registry tier weighted 0.7x | Evidence quality multiplier: documented 1.0x, spoken 0.7x, registry 0.5x, plus rule 4 skepticism | The load bearing item is the Singhal and PI Industries relationship, which the report itself puts at media and registry tier. At 0.5x, H2 = 0.5 and the total is 12.5, rounding to 13. Classification unchanged |
| MINOR | B07 Section 3 guard line and YAML completionist_recount | 14 documented items across 6 categories | Completionist guard recount line | A4 5 + B1 3 + B2 2 + C2 1 + F1 1 + H3 1 = 13 across 6. The 14th item, A2 R&D = NIL anti evidence, sits in a seventh category. Recomputed 13 of 6, or 14 of 7 |
| MINOR | B07 Section 2C vs B01 Block F M3 | FAT 2.22x (B07) against 1.88x (B01), same company, same year | 2C uses historical fixed asset turnover | Net PP&E 81.56 against net block 96.41. Which figure is correct is a source question referred to Verifier A. On the B01 basis, capex_embedded_growth_pct is 8, not 10. Feeds valuation |
| MINOR | B07-emoat.yaml catalysts_12m | Hospitality venture decision point, window CY27-28 | catalysts_12m covers the next 12 months; feeds Pillar 3 catalyst proximity | 15 to 28 months from the 2026-09-07 run date. The report's own 6A timeline places it in the 12 to 24 month bucket, so block and narrative disagree. Recomputed 4 compliant catalysts, not 5 |
| MINOR | B07-emoat.yaml evidence_mix | documented: 15 | Block payload internal consistency with the stated documented item recount of 14 | Populations may legitimately differ but are never stated; 15 against 14 reads as one population miscounted |
| MINOR | B07 Section 6E peer cross check | SULA Q1FY27 deck read | Stage consumes AR plus 3 main concalls plus investor presentation plus B01 | The stage itself names the file as outside its injected inputs. Disclosed in input_gaps, marked supplementary, changed no score: E1 stayed 0 and hospitality stayed in the register. The output was a flag, not a number |
| MINOR | B07 6D and YAML combined_reasoning | "seven of eight deal breakers fired" | Accurate restatement of the Gate 0 deal breaker framework, which lists nine | Seven fired, deal breaker 5 (pledge) unevaluable NOT FOUND, deal breaker 9 (history under 3 years) did not fire. Wrong denominator in both report and block. Recomputed 7 of 9 |

---

## VERIFIER D — peer utilisation and citations (B12d)

12 peers audited, 12 confirmed substantive, giving peer utilisation of 100%. No substantive claim unsupported, no unused but relevant peer material found on independent re-search, all five B05 peer questions received a verdict, no verdict discipline failures. Citation acceptance is a separate number: 12 of 20 individual citations spot checked against source page markers were correct, so 60%, exactly at the floor and not below it. No fabricated quotes; every mismatch is a wrong page or wrong transcript anchor on real quoted material.

| Severity | Location | Claimed anchor | Actual anchor | Note |
|---|---|---|---|---|
| MAJOR | Claim 3, the "350 to 400 basis points" gross margin figure | SULA-Concall_May_2026_Transcript.pdf p.5-6 | PDF page 8 | The single most material quantified figure behind the CONTRADICTED grape cost verdict sits outside the cited range; the composite quote splices p.6 text with a p.8 number |
| MAJOR | Bonus / EU FTA, the "+20% by Feb-2026" Euro appreciation figure | Folded into the SULA-Concall_May_2026_Transcript.pdf p.10 citation | SULA-Concall_Feb_2026_Transcript.pdf, PDF page 7 | Real figure, credited to the wrong transcript entirely and left uncited at its true source |
| MAJOR | Part 2E, the "casualties among the industry" risk quote | SULA-Concall_Feb_2026_Transcript.pdf p.13 | SULA-Concall_May_2026_Transcript.pdf, PDF page 10 | Wrong transcript, not just wrong page. A keyword search finds exactly one hit for "casualties" across all 12 peer transcripts, in the May-2026 call |
| MAJOR | Claim 5 / Part 2C, the SDBL UP brewery composite quote (Rs 570 cr total, Rs 300 cr invested, 3 to 4 years to peak) | SDBL-Concall_Aug_2026_Transcript.pdf p.7, a single citation for a compound claim | Rs 570 cr is in SDBL-Concall_Feb_2026_Transcript.pdf, uncited; Rs 300 cr invested is Aug-2026 PDF p.4; "3 to 4 years to peak" is Aug-2026 PDF p.11 | A compound quote assembles two different quarterly calls under one wrong page citation; the headline Rs 570 cr figure's true source transcript is never named |
| MAJOR | Claim 1, the Keshav Garg "60% market share" analyst quote | SULA-Concall_Nov_2025_Transcript.pdf p.11 | PDF page 13 | Off by two pages |
| MAJOR | Part 2B, the SDBL barley and glass cost inflation quote | SDBL-Concall_Feb_2026_Transcript.pdf p.7 | PDF page 9 | Off by two pages |
| MINOR | Claim 1, the Sula presentation "above 50% share in domestic premium wines" | SULA-Investor_Presentation_Q4FY26 p.13 / Q1FY27 p.13 | PDF page 12 in both decks | Off by one page in both presentations; the quote itself is accurate |
| MINOR | Bonus / EU FTA, "a further +5%" Euro appreciation | SULA-Concall_May_2026_Transcript.pdf p.10 | PDF page 11 | Off by one page |

---

Disagreement log: outputs/final/verifier-disagreement-log.md, three rows, already written.
