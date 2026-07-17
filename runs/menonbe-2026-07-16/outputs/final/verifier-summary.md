# Verifier summary (phase 3 complete) — MENON BEARINGS (MENONBE)

Run date 2026-07-16. Phase 3 adds verifier C's valuation-adherence audit (B10 / B11 / B14, extended to Role 2 decision rules and sizing) on top of the phase 1 verifiers. Phase 1 Gate 0 and Emerging Moat halves of verifier C are carried forward unchanged.

## Confidence delta and acceptance rates

| Component | Verifier | Score | Acceptance | Findings |
|---|---|---|---|---|
| Numerical acceptance | A (B12a) | 91.5 | 91.5% | 0 CRITICAL, 0 MAJOR, 4 MINOR |
| Red flag coverage | B (B12b), binding | 75 | 75% | 0 CRITICAL, 1 MAJOR, 4 MINOR |
| Framework adherence | C (B12c) | 94 | gate0+emoat 99%, valuation 94% (96% combined over 126 rules) | 0 CRITICAL, 1 MAJOR, 10 MINOR |
| Peer utilisation | D (B12d) | 100 | 100% | 0 CRITICAL, 0 MAJOR, 5 MINOR |
| OVERALL | min | 75 | | Band 75 to 89 normal; no verdict downgrade; REWORK not triggered |

Overall 75 = min(91.5, 75, 94, 100). Binding component is red flag coverage. No CRITICAL findings anywhere. REWORK is not triggered: no numerical finding is CRITICAL and every acceptance rate is at or above 60%. Totals across all four verifiers: 0 CRITICAL, 3 MAJOR, 23 MINOR.

## Findings, sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| C (B12c, phase 3) | B14 Section 7 decision-rule trace (Gate 0 leg) | Verdict WATCHLIST overrides Master Role 2 rule L809 (Gate 0 AVERAGE/AVOID triggers AVOID) and cites a non-existent "Gate 0 below GOOD defaults to WATCHLIST" rule. Defensible under the pipeline flag-not-gate convention plus the documented FLAG-GATE0 backward artifact plus Role 1 consistency; action-neutral at CMP because the verdict already reads AVOID-on-valuation at Rs 190. MAJOR not CRITICAL because the actionable outcome (no buy at CMP; act only in Rs 132-148) is unchanged and the destination PE and Hurdle verdict are untouched. Operator to adjudicate the label; recommended fix names L809 explicitly and records the Gate0-AVOID override on backward-artifact grounds. |
| B (B12b) | B05 trigger 2 / promise 8 / section 1C | Cash conversion and ex-works promise under weighted. The Q3 FY26 "180 to 30 day" pledge was already contradicted by Q4 FY26: debtors still beyond 180 days, high interest re labelled one-off, large DDP customers refusing conversion. B05 framed ex-works as on track and treated rising receivables (Rs 90.77 Cr vs Rs 60.63 Cr) as a forward kill signal only. Thesis relevant per the cash conversion rule; consolidated into a realised red flag downstream. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A (B12a) | B04 Section 3D | Alkop per unit realisation Rs 7.5 lakh/MT (Investor Presentation slide 33) versus Rs 2.0 to 2.2 lakh/MT (concall Jan-2026 p.24). Both company sourced from different contexts; B04 already flags the inconsistency. Not a report error. |
| A (B12a) | B01 Block B item 2 (cross reference) | PAT growth stated 64.4% in B02 finding 2 is a basis error; correct value 61.9% (3262.93/2015.73), already found and corrected by B03 phase 2. No current report carries the wrong figure. |
| A (B12a) | B07 Section 1C | Alkop Rs 95 Cr by FY27 from a Rs 40 Cr base (Investor Presentation slide 33); the Rs 40 Cr base does not reconcile with FY25 and FY26 actuals of Rs 65.94 Cr and Rs 72.18 Cr disclosed two slides earlier. B07 correctly flags this as a company presentation defect, not a report error. |
| A (B12a) | B01 p.51, M6 R&D | R&D at 0.56% of turnover (AR p.54) is a standalone Menon Bearings disclosure, not consolidated. Correct figure and sourcing; specificity note only. |
| B (B12b) | B05 promise 5 (brakes) | Brakes Rs 100 Cr FY27 target collapse to a Rs 10 Cr two year pipeline not surfaced as its own flag; bundled into the dynamometer miss, magnitude under highlighted. |
| B (B12b) | B05 Section 1A / guidance table (Alkop parts) | Alkop development parts count drift (63 / 53 / 51 / 60) noted only as a 51 to 63 range, not flagged as an inconsistency. |
| B (B12b) | B05 dropped_triggers (Canada) | B05 says Canada had no mention in Q3 or Q4; Q4 p.16 references a planned Canada visit. No deal closure, so substance holds; minor imprecision. |
| B (B12b) | Q4/FY26 call p.13-14 (not in B05) | Alkop capacity muddle: 1,450 tons capacity stated versus operating at 1,500 tonne in the same exchange. Immaterial, missed by the pipeline. |
| C (B12c, phase 3) | B10 Pillar 1 (line 211) | Illustrative Pillar 1 formula (1+ROCE-CoE)×target ROCE approx 22.4x is arithmetically incoherent; tagged illustrative, B11 re-derived correctly via Amendment 5. No downstream impact. |
| C (B12c, phase 3) | B10 bull-cap illustration (line 297) | B10 caps bull off the 5yr base (16.2%); the Hurdle needs the 3yr base. Tagged illustrative; B11 correctly used 3yr 19%+5=24%. No impact. |
| C (B12c, phase 3) | B11 Section 1C Hurdle EPS window | Growth compounds off FY26 6.82 while current PE uses TTM 7.83 (same reported basis, different start point); conservative, understates the Hurdle; SFL basis-consistency met; label looseness only. |
| C (B12c, phase 3) | B14 Section 7 tier call | Tier B bar rationale over-elaborated (FLAG-CASH plus promoter CAUTION plus credibility C); the primary mechanical reason is FII+DII 0.24% below 3% making Tier A the default. Conclusion correct. |
| C (B12c, phase 1) | B01 Block F M10 (Switching Costs) | Scored 1 against strict band 0. Moat total 16 to 15 possible; moat count (3), MODERATE class, grand total band and AVOID classification all unchanged. |
| C (B12c, phase 1) | B01 Block E E2 | Promoter change window about 2.75 years versus the 3 year spec, a data limitation already flagged; band unaffected. |
| C (B12c, phase 1) | B01 Block F M9 | Gross margin to revenue CAGR of plus 4.05pp falls between bands; a score of 1 is defensible; no impact. |
| C (B12c, phase 1) | B07 F2 | B05 promise delivery record absent to B07; a self service concall substitute was flagged. F2 scored 0, no scoring impact. |
| C (B12c, phase 1) | B07 Section 5 | Scale ceiling about 84 versus the prompt roughly 0 to 80; cosmetic, absolute bands unaffected. |
| D (B12d) | B06 Claim 8, NRBBEARING Q2 FY26 citation | Customer concentration quote cited as p.7 of 20; actual internal page is p.8 of 20. Quote text and speaker exact. |
| D (B12d) | B06 Claim 2, HARSHA Q3 FY26 citation | The "3 months, 4 months total lag" quote cited as p.12 of 16; actual page is p.11 of 16. Quote text exact. |
| D (B12d) | B06 Claim 1, HARSHA Q4/FY26 citation | Composite quote cited as p.12-13 of 18; the "manufacturing is moving to India" half is on p.11, and p.12 has no quoted material. Second half correctly on p.13. |
| D (B12d) | B06 Part 2E, EV strategy reversal item | "a complete U-turn" presented in quotation marks as a PRECAM quote; no such phrase exists in the transcripts. Actual wording is a paraphrase equivalent from Karan Shah, Mar-2026 call. |
| D (B12d) | B06 Part 2 / Claim 6 net read | States peers show complete silence on railway terminology; HARSHA does use railway as an unrelated industrial end demand segment. Substantively immaterial to the UNVERIFIABLE verdict, which stands. |

## Verifier C phase 3 recomputation

Destination PE re-derives exactly: Track 2 additive 25.0x (22.4×0.85=19.0, +1.0 override=20.0, ×1.25 UA=25.0=cap), Track 1 RRM 22.4x (0.94 RRM, UA, cap). Hurdle base 1.73 FAIL, bull 1.96 PASS, CONDITIONAL. Entry Rs 132 to 148, MoS Rs 118. Both operator overrides labeled and arithmetically reconciled. The only open item is the Role 2 verdict LABEL (WATCHLIST under pipeline convention vs AVOID under a literal reading of L809); the actionable outcome (no buy at CMP; buy only in Rs 132-148) is the same under both. Phase 3 rules checked: valuation (B10/B11) 40, Role 2 (B14) 12, combined 52, 50 clean, 1 MAJOR, 1 counted MINOR, 3 immaterial MINOR notes.

## Verifier notes carried

- Verifier B promise delivery spot checks: 5 checked, 5 confirmed, 0 wrong. Credibility grade C concurred. Its independent red flag list carried one CRITICAL-grade item, the multi quarter dynamometer evasion, which the pipeline caught and correctly elevated, so it is not a coverage finding.
- Verifier A: all Gate 0 verdict card figures (classification AVOID, core 54, moat 16, blocks A to E) verified clean. Four ANCHOR NOT FOUND items are source document data availability gaps, not errors.
- Verifier D: 11 of 11 peer transcripts used substantively; no pipeline peer claim unsupported.
