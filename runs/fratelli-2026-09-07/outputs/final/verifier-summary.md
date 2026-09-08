# VERIFIER SUMMARY — FRATELLI, run fratelli-2026-09-07 (phase 1)

Written 2026-09-08. Covers verifiers A, B, D in full, and the Gate 0 plus Emerging Moat portion of verifier C. Stages 10 and 11 did not run, so the valuation half of verifier C is not audited and is not summarised here.

## CONFIDENCE DELTA (revision 2)

| Component | Verifier | Block | Acceptance | Floor | Status |
|---|---|---|---|---|---|
| Numerical acceptance | A | B12a run 2 | 87% | 60% | pass |
| Red flag coverage | B | B12b run 2 | 31% | 60% | FAIL |
| Framework adherence | C | B12c | 82% | 60% | pass, Gate 0 + Emerging Moat scope only |
| Peer utilisation | D | B12d run 2 | 67% | 60% | pass |
| Citation acceptance | D | B12d run 2 | 50% | 60% | FAIL |
| **Overall** | minimum | confidence.yaml rev 2 | **31** | 60 | **FORCED REWORK** |

Revision 1 recorded an overall of 39 and is in git history at commit 9ddb6e0. Movement: red flag coverage 39 to 31; peer utilisation 100 to 67; numerical acceptance and framework adherence unchanged, since verifiers A and C were not re-run against the reran stages.

Finding counts by verifier: A 0 CRITICAL / 7 MAJOR / 1 MINOR. B 2 CRITICAL / 15 MAJOR / 8 MINOR. C 0 CRITICAL / 1 MAJOR / 9 MINOR. D 0 CRITICAL / 8 MAJOR / 3 MINOR.

## HOW MANY TIMES EACH VERIFIER RAN

**Verifier A ran twice, and re-decided its own two CRITICALs.** Run 1 raised two CRITICAL findings on Gate 0's FY24 and FY25 revenue figures. The orchestrator neither cleared nor downgraded them. It re-invoked verifier A once, per the standing LESSONS.md remedy, to re-decide on source with a widened coverage brief. Run 2 opened screener-Data_Sheet.csv and both annual reports, found both figures present in the source the report named and labelled as screener data rather than presented as audited consolidated, and reclassified both to MAJOR itself. Verifier A remains the deciding authority on both. Both movements are logged in outputs/final/verifier-disagreement-log.md, which is maintained separately from this file.

**Verifiers B and D each ran twice, once before and once after the stage 5 and stage 6 reruns.** Neither rerun stage was shown the earlier audit's substantive findings, so both re-measures stay independent. Verifier B's second pass found 29 flags where the first found 38; the two passes are not the same list, so only the coverage ratio is comparable, not the counts. Verifier D's run 1 audit is archived in git history.

**Verifier C ran once.** Neither Gate 0 nor the Emerging Moat scan was reran, so no re-measure was needed.

## VERIFIER B (RED FLAGS, B12b run 2) — 2 CRITICAL, 15 MAJOR, 8 MINOR, acceptance 31%

29 flags found independently. 9 caught, 10 partly caught.

| Severity | Location anchor | Note |
|---|---|---|
| CRITICAL | B05 4D / red_flags / credibility_basis / analyst_note | EBITDA-SIGN-FLIP is the report's headline flag, drives the D grade, three promise delivery rows and an explicit downstream instruction to treat every call EBITDA/PBT/PAT figure as unverified. It rests on a basis mismatch B05 itself created. Decision changing if carried into synthesis as written. Rule 5 sets NOT SUPPORTED at MAJOR; graded CRITICAL here on decision impact. A judgment call on basis, not an existence of a number call; any verifier A source fidelity verdict on these figures stands untouched. |
| CRITICAL | B05 + B06, both absent | MISSED repeated peer contradiction on discounting across four consecutive SULA calls, compounded by Fratelli self contradiction between Q3FY26 and Q4FY26. Anchors: Concall_Q4FY26_Jun2026_Transcript.pdf p.14 vs Concall_Q3FY26_Feb2026_Transcript.pdf p.8 vs SULA-Concall_Nov_2025 p.15, SULA-Concall_Feb_2026 p.14, SULA-Concall_May_2026 p.10, SULA-Concall_Aug_2026 p.4 and p.6. Bears on whether the 79% gross margin and the operating leverage story survive the trade spend needed to hold shelf. Rule 5: a missed repeated evasion or contradiction spanning 2+ quarters is CRITICAL. |
| MAJOR | B05 Section 2A prose + promise_delivery row 7 | Q3FY26 PBT/PAT "opposite sign" claim NOT SUPPORTED. Subsidiary PBT +Rs11.79 lakh vs claim of roughly Rs0.1cr. |
| MAJOR | B05 promise_delivery row 6 | Q3FY26 EBITDA "~14x overstated" NOT SUPPORTED. Subsidiary EBITDA Rs5.42cr / 8.5% vs claim Rs5.5cr / 8.6%. |
| MAJOR | B05 promise_delivery tally | delivered 3 / partial 1 / missed 10 is wrong in composition; corrected to about delivered 5 / partial 1 / missed 7 before adding four untracked unkept promises. Consequential on the basis mismatch. |
| MAJOR | missed — Concall_Q2FY26_Nov2025 p.3 vs SULA-Concall_Feb_2026 p.7; Fratelli association claim Concall_Q3FY26_Feb2026 p.15 | Q2FY26 FTA assurance that the government would concede nothing beyond Australia, against the peer's statement that the industry was summoned by the Commerce Ministry a year earlier and told duties would fall significantly; Fratelli claims a seat at that table. |
| MAJOR | missed — Concall_Q4FY25_Jun2025 p.10 vs Results_Q4FY26_and_FY26_2026-05-30 p.11 | CFO's Q4FY25 deferred tax guidance (25% ETR, DTA to reverse against profit) falsified by the FY26 write off of the entire DTA for want of future taxable profit, Rs361.12 lakh charged to P&L; never revisited on any call. |
| MAJOR | missed — Concall_Q3FY26_Feb2026 p.5 vs Results_Q4FY26_and_FY26_2026-05-30 p.8 | Holdco receivable promise "the same will be recovered within FY26" not delivered; Rs46.72 lakh still on the balance sheet at 31-Mar-2026. B05 credits the write off half as a positive but does not test the delivery half. |
| MAJOR | missed — Concall_Q4FY25_Jun2025 p.11 and p.20 vs Concall_Q3FY26_Feb2026 p.7 and p.9 vs Concall_Q4FY26_Jun2026 p.11 | A&P reduction promised in FY25 (100bps down, 5-6% destination by 2028-30) never delivered; still 8% a year later and destination quietly raised to 7-8%, with Shotgun spend above 10%. |
| MAJOR | missed — Concall_Q4FY26_Jun2026 p.8; 6% share at Concall_Q2FY26_Nov2025 p.3 | RTD market size, case count, share and revenue figures mutually incompatible within one answer: 10% share by cases, 3.6% by value, 6% claimed elsewhere, and Rs5,000/case market vs Rs1,800/case own realisation. |
| MAJOR | missed — Concall_Q1FY26_Aug2025 p.14-15 vs SULA-Concall_Nov_2025 p.8 and SULA-Concall_Aug_2026 p.11 | Management's only specific factual claim about the competitor's hospitality model is wrong; it told an accurate analyst to "revalidate some of your assumptions". |
| MAJOR | missed — Concall_Q2FY26_Nov2025 p.12 (Smith Gala) | "Your audio is not clear" used twice to sidestep the only balance sheet strength question asked across five calls; B05 instead scores Defensiveness 3/5 as willing to engage tough questions. |
| MAJOR | missed — Results_Q4FY26_and_FY26_2026-05-30 p.2, board item 4 | Related party postal ballot approved the same day as the FY26 results, sponsorship of Mr. Keshav Sekhri's higher education, never mentioned on the call three days later; B05's silence check catches five other items from the same filing package. |
| MAJOR | B05 1D silence check — FY26 consolidated balance sheet p.17 | PARTIAL: working capital never discussed on any call; receivables Rs105.1cr (about 212 days) and inventory Rs95.1cr against Rs181.29cr revenue are absent from the silence check. The peer quantifies these every quarter. |
| MAJOR | B05 2A / 4C — Concall_Q4FY25 p.14, Concall_Q2FY26 p.8, FY26 consolidated balance sheet p.17 | PARTIAL: debt rising Rs100cr to Rs120cr against "not intending to take any more substantial debt" is scored as a credibility positive. |
| MAJOR | B06 Q5 / B05 3A — Concall_Q4FY26 p.13 vs SULA-Concall_Nov_2025 p.10 | PARTIAL: Fratelli's "more than 90% market share in the Wine-in-a-Can segment" is never tested against Sula's direct counter claim to leadership on the same question. |
| MAJOR | B05 1B / 1C — Concall_Q3FY26 p.8/p.14 vs Concall_Q4FY26 p.10/p.12 | PARTIAL: FY27 10-12% EBITDA guidance silently dropped at Q4FY26 and replaced by a Rs240cr net net breakeven framing implying materially less; the analyst's 20% target is neither confirmed nor corrected. |
| MINOR | missed — Concall_Q2FY26_Nov2025 p.4 vs p.5 | "Our business has turned EBITDA positive in Q2" when Q2FY25 was already positive (Rs1.47cr vs Rs1.32cr prior year); B05 scores this promise DELIVERED without the qualifier. |
| MINOR | B05 Section 2A / headline — Concall_Q4FY26 p.3 vs p.5 | PARTIAL: Q4FY26 opening conflates the FY EBITDA figure with the Q4 sentence preceding it. |
| MINOR | B06 2B — SULA-Concall_Feb_2026 p.14 vs Concall_Q3FY26 p.4 | PARTIAL: harvest contradiction anchored to SULA Aug 2026 price data rather than the tighter SULA 9-Feb-2026 crop assessment one week before Fratelli's claim; Fratelli's own Q4FY26 p.9 "higher cost" admission unused. |
| MINOR | B06 Q1 — Concall_Q1FY26 p.7 | SUPPORTED but OVERSTATED as to precision: 7.5-9.5% share rests on a TAM with no in corpus third party source; management's own in transcript Rs1,000cr denominator gives 18% and needs no external TAM. |
| MINOR | B05 1C — Concall_Q3FY26 p.3/p.7/p.15; Concall_Q4FY26 p.3/p.4/p.12 | PARTIAL: segment and denominator drift only half caught. |
| MINOR | B05 + B06 WIPS treatment — Concall_Q1FY26 p.8 vs Concall_Q2FY26 p.9 | PARTIAL: neither catches management ratifying an Rs8-12cr figure an analyst put to it after saying Rs8cr the prior quarter. |
| MINOR | B05 + B06 input_gaps | PARTIAL: Q1FY27 transcript non publication filed as a corpus gap rather than a management conduct signal, in the quarter the 30% guidance first went against management. Five prior transcripts were filed on schedule; all three peers published Q1FY27. |
| MINOR | B05 Section 2A prose | Promise delivery counts internally muddled against the YAML tally. Presentational. |
| MINOR | B05 anchors | Mixes PDF page numbers with the transcripts' printed footer numbers, one page low, in at least four places; B06 uses PDF pages. B06 has one drift of its own: SULA Aug 2026 table grape quote cited p.8, PDF p.9. Source fidelity is verifier A's call; noted so the convention clash is not read as fabrication. |

### Verifier B: upstream flags ruled NOT SUPPORTED

This section is a finding against the analysis, not against the company, and is shown here in full because a pipeline flag that does not survive audit must not travel downstream unmarked.

1. **B05 red_flag "EBITDA/PBT/PAT sign-flip against filed results in 3-4 of last 4 checked periods" (HIGH) and YAML flag EBITDA-SIGN-FLIP: OVERSTATED.** Applies a consolidated recomputation to figures management reports on the wine subsidiary basis that B05's own UNDISCLOSED-BASIS-CHANGE flag identified. On the subsidiary basis, Q3FY26 subsidiary PBT is +Rs11.79 lakh vs a claim of "roughly INR0.1 crores" (exact match); Q3FY26 subsidiary EBITDA Rs5.42cr / 8.5% vs a claim of Rs5.5cr / 8.6% (match); FY26 subsidiary EBITDA approximately +Rs0.65cr, positive, vs a claim of +Rs1.06cr; Q4FY26 subsidiary EBITDA -Rs3.97cr vs Aditya's stated -Rs3.7cr (match). The sole reconciling item is the holdco's one off Rs512.82 lakh write off that B05 elsewhere credits management for disclosing proactively. Derivation validated by exact additivity: consolidated FY26 net loss Rs2,491.19 lakh minus subsidiary Rs1,583.47 lakh = Rs907.72 lakh vs parent standalone Rs907.64 lakh.
2. **B05 sub-claim "Q3 FY26 PBT/PAT... the single starkest reconciliation failure in the entire five-call sample... OPPOSITE SIGN on both PBT and PAT": NOT SUPPORTED.** Subsidiary PBT +Rs0.12cr against a claim of roughly Rs0.1cr.
3. **B05 sub-claim "Q3 FY26 EBITDA claim overstates the recomputed figure by ~14x": NOT SUPPORTED.** Subsidiary basis recompute is Rs5.42cr against a claim of Rs5.5cr.
4. **B05 promise_delivery rows 7, 8 and 9 (all scored missed / opposite sign) and the resulting tally delivered 3 / partial 1 / missed 10: OVERSTATED,** consequential on the above. Corrected tally is approximately delivered 5 / partial 1 / missed 7 before adding the four untracked unkept promises this audit found: Shotgun run rate disclosure, deferred tax, holdco receivable, A&P.
5. **B05 2C tone score "Defensiveness 3/5 - generally calm and willing to engage tough questions": NOT SUPPORTED as written;** omits the Q2FY26 p.12 audio deflection of the only balance sheet strength question in the sample.

Promise delivery spot checks: 6 checked, 4 confirmed, 2 wrong.

Credibility grade: **concur with D, different basis.** The D is well earned on guidance discipline, repeated evasion, undisclosed filed items and peer contradicted claims. It is NOT earned on the EBITDA sign flip B05 leads with, which does not survive a like for like subsidiary basis check.

## VERIFIER D (PEER CROSS READ, B12d run 2) — 0 CRITICAL, 8 MAJOR, 3 MINOR, citation acceptance 50%, peer utilisation 67%

12 peers audited, 8 substantively confirmed.

| Severity | Location anchor | Claimed vs source truth |
|---|---|---|
| MAJOR | B06 Part 2B narrative + GRAPE-COST-SILENCE flag (report and YAML) | Claimed: ~350-400bps FY26 gross margin impact cited to SULA-Investor_Presentation_Q1FY27_2026-08-06.txt p.10-11. Source truth: the figure is genuine but sits in SULA-Concall_May_2026_Transcript.txt p.8, a different document entirely. Wrong transcript citation on a load bearing flag figure. |
| MAJOR | B06 Part 2B narrative + GRAPE-COST-SILENCE flag | Claimed: "Rs15-16/kg" and "Rs35/kg" cited to SULA-Concall_Aug_2026_Transcript.txt p.8 as part of a compound quote. Source truth: both fragments are on p.9; only the "more than doubling" fragment is genuinely on p.8. Compound claim, one citation, mixed page components. |
| MAJOR | B06 Part 1 Question 2 evidence table | Claimed: Sula WIPS receivable Rs85cr (Dec-25) cited to SULA-Concall_Feb_2026_Transcript.txt p.9. Source truth: p.11. Two pages off. |
| MAJOR | B06 peer coverage map, SULA Q2 FY26 row | Claimed: WIPS accrual and payout detail cited p.10-11. Source truth: SULA-Concall_Nov_2025_Transcript.txt p.9. Wrong page. |
| MAJOR | B06 Part 2C narrative + coverage map, SDBL Q3 FY26 row | Claimed: Rs570cr Phase 1 quote cited SDBL-Concall_Feb_2026_Transcript.txt p.4. Source truth: p.3. Wrong page. |
| MAJOR | B06 Part 2A/2E narrative + coverage map, SDBL Q1 FY27 row | Claimed: Madhya Pradesh disruption quote cited SDBL-Concall_Aug_2026_Transcript.txt p.4. Source truth: p.3. Wrong page. |
| MAJOR | B06 coverage map, SDBL Q4 FY26 row | Claimed: SUBSTANTIVE, "UP greenfield brewery commissioning and capacity detail". Source truth: no page or quote anchor given anywhere in the report body for this specific quarter. Content genuine but unanchored. Rule 2 violation. |
| MAJOR | B06 Part 3 peer presentation summary | Claimed: peer presentations used substantively throughout, SDBL two presentations CITED-ONLY. Source truth: TI-Investor_Presentation_Q1FY27_2026-07-27.txt is never mentioned anywhere, in any category. Its p.12 states "Customs: Reduction in custom under India-UK FTA from 150% to 75% for scotch import" with "Cost savings will result in 250-400 bps in margin expansion", directly relevant to Question 6 and more precise than the 60-100bps figure B06 used. Rule 3 violation, unused but relevant. |
| MINOR | B06 Part 1 Question 3 net read | Claimed: market leader EBITDA benchmark understated by 5-15 points. Source truth: re-derived range is 0.9 to 15.3 points depending on comparator quarter. Verdict unaffected, range imprecise. |
| MINOR | B06 flags YAML, MARKET-SHARE-ARITHMETIC-CONTRADICTED | Claimed: implies 7.5-9.5% share. Source truth: re-derived range is 7.81%-9.46%. Low end rounded down beyond the actual figure; immaterial. |
| MINOR | B06 Part 2C narrative | Claimed: Sula's CFO did not dispute the 12% ROE framing, attributing it instead to harvest seasonality of tanks and barrels, same page. Source truth: the harvest seasonality explanation (SULA-Concall_Nov_2025_Transcript.txt p.12-13) answered an earlier asset turnover question; the CFO's direct response to the 12% ROE follow up cited a base year comparability issue and a forward 17-18% ROE target (p.13). Same speaker, same exchange, two explanations conflated as one response. |

Verifier D note carried in full: "The arithmetic-based CONTRADICTED verdicts were re-derived independently and HELD. The market share calculation re-derives to 7.81-9.46% against the stage's stated 7.5-9.5%, and the EBITDA benchmark gap to 0.9-15.3 points against the stated 5-15. Both are MINOR imprecision, not verdict failures. The substance of the rerun stands; the citation layer does not."

Two of the anchor findings were independently spot checked by the orchestrator against the page markers and both confirmed: the grape price fragment is on p.9 of SULA-Concall_Aug_2026_Transcript, and the 350-400bps figure is in SULA-Concall_May_2026_Transcript, not the Q1FY27 presentation. There is no page numbering convention mismatch in stage 6; the citations are wrong.

## VERIFIER A (NUMERICAL, B12a run 2) — 0 CRITICAL, 7 MAJOR, 1 MINOR, acceptance 87%

61 numerical claims audited across all 11 reports. Priority given to revenue (12), balance sheet (14), cash flow (8), working capital (10), share and warrant (6), segment expense (5) and peer figures (6).

| Severity | Location anchor | Claimed vs source truth | source_fidelity |
|---|---|---|---|
| MAJOR | 02-notes-pass1.md, p.598 | Claimed: 39.5% of the 5,57,650 warrants allotted Aug-2024 lapsed. Source truth: AR FY26 p.51-52 and p.56 show 3,63,150 of 5,57,650 forfeited = 65.1%; confirmed by 08-promoter.md line 338 and 05-concall.md line 136. 39.5% of 557,650 is about 220,272, not 363,150. Material numerical error. ALREADY SUPERSEDED UPSTREAM: stage 2 pass 2 corrected it on source and the consolidated B02 block carries 65.1%, as do B05 and B08. The error is confined to the pass 1 working artifact. | true |
| MAJOR | 01-gate0.md, p.35, LOAD-BEARING FACT 1 | Claimed: FY2025 revenue Rs 276.25 cr (screener data). Source truth: screener CSV row 11 confirmed 276.25 cr; AR FY26 consolidated P&L shows 30,209.66 lakhs (302.10 cr). Figure exists and is labelled screener data, not presented as audited consolidated, but is 9.3% below AR consolidated, a Rs 25.85 cr gap, causing base mixing in downstream WC calculations. Not fabrication; basis mismatch. | false |
| MAJOR | 01-gate0.md, p.96, Block A ROCE | Claimed: FY2024 revenue Rs 421.35 cr (screener data). Source truth: screener CSV row 11 confirmed 421.35 cr; AR FY25 consolidated P&L shows 45,107.48 lakhs (451.07 cr). 7.1% below, a Rs 29.72 cr gap. Not fabrication; discrepancy in basis. | false |
| MAJOR | 01-gate0.md, p.99-100, B4 WC Days table | Claimed: FY2025 payable days 29.6 on the screener revenue basis. Source truth: on AR consolidated, 2,241.37 lakh / 30,209.66 lakh x 365 = 27.07 days (AR FY26 p.144 Note 19). Base mixing, difference 2.5 days. | false |
| MAJOR | 01-gate0.md, p.99, B4 WC Days table | Claimed: FY2025 inventory days 109.0 on the screener revenue basis. Source truth: on AR consolidated, 8,250.19 lakh / 30,209.66 lakh x 365 = 99.73 days (AR FY26 p.144 Note 9). Base mixing, difference 9.3 days. | false |
| MAJOR | 01-gate0.md, p.99, B4 WC Days table | Claimed: FY2024 inventory days 80.2 on the screener revenue basis. Source truth: on AR consolidated, 9,255.37 lakh / 45,107.48 lakh x 365 = 74.9 days (AR FY25 p.143 Note 9 comparative). Base mixing, difference 5.3 days. | false |
| MINOR | 01-gate0.md, p.96, Block A ROCE table | Claimed: FY2026 equity Rs 135.96 cr (screener data). Source truth: screener 43.47 + 92.49 = 135.96 cr; AR FY26 consolidated 13,596.36 lakhs = 135.96 cr. Matched. Verified. Shows screener and AR reconcile when the business is wine only. | false |
| MINOR | 01-gate0.md, p.50, Contingent Liabilities | Claimed: Rs 37.88 cr (AR FY26, Note 39). Source truth: AR FY26 p.150 Note 39 consolidated contingencies 3,787.90 lakhs = 37.88 cr. Matched. Verified clean. | false |

The MAJOR count here is 7 rows against 6 lines in the table above plus the warrant row, per B12a's own major_count of 7 over the eight listed findings. FY26 figures reconcile cleanly between screener and AR, so the base mixing issue is specific to FY24 and FY25 screener data.

## VERIFIER C (FRAMEWORK ADHERENCE, B12c) — 0 CRITICAL, 1 MAJOR, 9 MINOR, acceptance 82%

SCOPE: Gate 0 (B01) and Emerging Moat (B07) only. Gate 0 26 of 28 checks = 93%. Emerging Moat 21 of 29 = 72%. The valuation audit (B10/B11), the business understanding narrative audit, the Halt 1 dossier, downstream candidates and method plurality are NOT covered and are deferred to phase 3. Valuation framework documents were not loaded.

| Severity | Location anchor | Claimed vs rule, and recomputation |
|---|---|---|
| MAJOR | B07 Section 3 B2 / Section 5 row B2 | Claimed: likelihood Medium-High x impact Medium, raw 3, adjusted 3.0. Rule: the Section 5 matrix defines only H/M/L per axis; HM or MH = 3, MM = 2. "Medium-High" is not a defined level. Recomputed em_score 11.7 vs 12.7, landing on the 12.0 MODEST/NONE boundary where the label depends on an unstated rounding convention. No decision moves: EM stays far below the EM>=25 UA qualifier and combined_assessment stays AVOID. |
| MINOR | B01 Block F, M8 | Claimed: M8 = 0. Rule: the M8 ladder offers "mentioned unquantified = 1" and "none or purely digital = 0" with no else clause. The 31,000 point network is quantified and growing, so both band conditions are false and the gap was resolved downward. Recomputed M8 = 1, moat_score 1/60; moats_confirmed still 0, class still NONE, AVOID unchanged. Disclosed and flagged by the stage, hence MINOR. |
| MINOR | B01-gate0.yaml data_notes | Claimed: data_notes omits both proxy bases. Rule: data_notes carries proxy bases used. The FY17-21 "Other Liabilities" proxy for Current Liabilities in capital employed, and the Sales rather than COGS basis for WC days, appear in the report body only. Downstream stages read the block. |
| MINOR | B07 Section 5 row H2 | Claimed: blended spoken/registry tier weighted 0.7x. Rule: documented 1.0x, spoken 0.7x, registry 0.5x. The load bearing item is the Singhal/PI relationship, which the report itself puts at media and registry tier. At 0.5x, H2 = 0.5 and the total is 12.5, rounding to 13. Classification unchanged. |
| MINOR | B07 Section 3 guard line and YAML completionist_recount | Claimed: 14 documented items across 6 categories. A4 5 + B1 3 + B2 2 + C2 1 + F1 1 + H3 1 = 13 across 6; the 14th item (A2 R&D = NIL anti evidence) sits in a seventh category. Recomputed 13/6 or 14/7. |
| MINOR | B07 Section 2C vs B01 Block F M3 | Claimed: fixed asset turnover 2.22x (B07) vs 1.88x (B01), same company, same year. Net PP&E 81.56 vs net block 96.41, unreconciled across stages. Which base is correct is referred to verifier A. On the B01 basis capex_embedded_growth_pct is 8, not 10. Feeds valuation. |
| MINOR | B07-emoat.yaml catalysts_12m | Claimed: hospitality venture decision point, window CY27-28. Rule: catalysts_12m covers the next 12 months and feeds Pillar 3 catalyst proximity. CY27-28 is 15 to 28 months from the 2026-09-07 run date, and the report's own 6A timeline places it in the 12-24m bucket. Recomputed 4 compliant catalysts, not 5. |
| MINOR | B07-emoat.yaml evidence_mix | Claimed: documented 15, against a stated recount of 14. Populations may legitimately differ but are never stated; 15 vs 14 reads as one population miscounted. |
| MINOR | B07 Section 6E peer cross check | Claimed: SULA Q1FY27 deck read. Rule: the stage consumes AR + 3 main concalls + investor presentation + B01. The stage itself names the file as outside its injected inputs. Disclosed in input_gaps, marked supplementary, changed no score; the output was a flag, not a number. |
| MINOR | B07 6D and YAML combined_reasoning | Claimed: "seven of eight deal-breakers fired". Rule: Gate 0 lists nine deal breakers. Seven fired, deal breaker 5 (pledge) unevaluable NOT FOUND, deal breaker 9 (history under 3y) did not fire. Wrong denominator in both report and block. Recomputed 7 of 9. |

Verifier C note carried in full: no CRITICAL and no REWORK trigger fires from this verifier; acceptance sits well above the 60% floor. Categories 21 and 22 are both present in B07 and both correctly scored 0 against their two leg and named sacrifice tests, so the stage 7 REWORK condition does not fire. Gate 0 AVOID and B07 MODEST/AVOID survive every recomputation run.
