# Verifier summary (phase 3, final)

## Confidence delta and acceptance rates

| Component | Score | Acceptance | Note |
|---|---|---|---|
| Numerical acceptance (A, B12a) | 97.1 | 97.1 | 34 numbers checked, 0 CRITICAL, 1 MAJOR source-fidelity gate |
| Red flag coverage (B, B12b) | 71 | 71 | 17 flags, 12 caught + 3 partial, 2 missed |
| Framework adherence (C, B12c) | 89 | 89 (Gate0+EM) / 92 (valuation) | Conservative min 89; both halves re-derived clean, valuation and decision concur |
| Peer utilisation (D, B12d) | 75 | 75 | 9 of 12 peers substantive; 4 MAJOR fixes, 0 fabrication |
| Overall | 71 | | Band 60 to 74; red flag coverage binds; PROCEED-family verdicts downgrade one level |

Rework not triggered: no Verifier A CRITICAL (0 critical, acceptance 97.1), no verifier acceptance rate below 60 (minimum 71).

Phase-3 valuation adherence: COMPLETE. 38 rules checked, 0 CRITICAL, 0 MAJOR, 3 MINOR, acceptance 92, ACCEPTED. Destination PE (Track 1 16.8x governing, Track 2 24.0x) and decision (WATCHLIST leaning AVOID, no position) concur; no MINOR alters PE, Hurdle, or decision.

## Source-fidelity gate (one MAJOR, non-overridable)

Verifier A overturned stage 7's "DBX Holdings and GreenLeaf NOT FOUND in AR Note 8." Consolidated Note 8, p.112, Section B lists both unquoted equity instruments: DBX Rs 166.11 L and GreenLeaf TDG Rs 35.88 L. Disposition: GATE HELD, figure corrected at source. Stage 3's figures stand; stage 7's NOT FOUND removed. Carried to the verifier disagreement log.

## Findings, sorted by severity

### CRITICAL

None across all four verifiers, either phase.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A | Stage 7 (07-emoat.md) Section 1B, lines 62-71 | "DBX Holdings and GreenLeaf NOT FOUND in AR Note 8" contradicted by Consolidated Note 8 p.112: both listed (DBX Rs 166.11 L, GreenLeaf Rs 35.88 L). Stage 3 correct. Source-fidelity, non-overridable. |
| A | Stage 7 (07-emoat.md) Section 1B, line 69 | "GreenLeaf NOT FOUND anywhere in the AR" contradicted by Consolidated Note 8 p.112: GreenLeaf TDG Ltd, 320 shares at GBP 1, Rs 35.88 L. Source-fidelity, non-overridable. |
| B | B05 promise-delivery tracker (2A/4D) | July 2023 crypto derivative platform "three months away from launch" promise omitted from the tracker and never confirmed launched; flagship silently replaced by an intelligent document processing platform in Nov 2023. Anchor: Jul p.4 vs Nov pp.9-10. |
| D | B06 Part 1 Q4 / Part 4 | INFOBEAN blockchain exit quote characterized as unprompted in prepared remarks; it is Avinash Sethi's direct answer to analyst Mohit's blockchain question. Inflates the strongest single corroborating point. |
| D | B06 Part 1 Q1 | "InfoBeans confirms elsewhere (Nov 2025 call)" the doubling-every-3-years framing; that phrase is analyst Rupesh's own question framing, not management confirmation. |
| D | B06 Part 3 coverage map / 06-peers.yaml | KSOLVES Q2FY26 (Oct 2025) rated CITED-ONLY with Q6 IPO-vintage contribution credited to Jul 2025; the decisive "21st result after launching the IPO" quote is in the Oct 2025 transcript p.7. Should be SUBSTANTIVE. |
| D | B06 Part 3 closing paragraph | "10 of 12 peer transcripts SUBSTANTIVE" contradicted by the same paragraph and the coverage map, which show 3 CITED-ONLY, i.e. 9 SUBSTANTIVE. Headline coverage statistic arithmetically wrong. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| A | Stage 1 (01-gate0.md) Block E, line 217 | Promoter 72.07% (31 Mar 2025) verified exact against AR Note 1D p.76; data 17 months stale, gap already flagged. |
| B | B05 2C/2D | Headcount flat ~305 (Jul) to 301 (Nov) against the 500-people FY26 target; growth counter-signal not noted. Anchor: Jul pp.3,6 vs Nov pp.5,6. |
| B | B05 2C Consistency | Analyst margin-direction dispute (33 to 29%) vs management (25 to 34%) left unreconciled. Anchor: Nov p.3. |
| B | B05 3B | "Massive improvement" demand claim asserted while halving FY24 guidance; tension not drawn. Anchor: Nov pp.5,12. |
| B | B05 3C | Equity-for-services plus subsidized rates on high-mortality early-stage clients under-weighted as a revenue-quality risk. Anchor: Jul p.7; Nov p.8. |
| C (phase 1) | B01 Block C / C1 | 19.97% revenue CAGR at the >=20% band edge; scored 5 by rounding, decision-neutral, inconsistent with M11 treatment of the same number. Strict recompute: Block C 19, core 87, GOOD+ unchanged. |
| C (phase 1) | B01 Block F / M12 | Latest-year basis for the negative-WC band (43.59 days); majority read across 4 years gives 0. Moat score 19 vs 18, STRONG and classification unaffected. |
| C (phase 1) | B07 Section 3 recount | Stated recount tally "13 items across 7 categories" while 8 categories enumerated (A2, A4, B2, C2, F1, F2, G1, G2). Cosmetic; guard purpose met, score not over-credited. |
| C (phase 3) | 11-valuation UA F2 + B10 ua_qualifiers.gate0_or_em | Gate0-OR-EM qualifier stated FAIL on EM 10<25; actually MET because Gate 0 88>=60 satisfies the OR leg. UA NOT APPLIED still correct on other grounds (stale FII+DII leg, operator R2 Kacholia falsification). No PE impact. |
| C (phase 3) | 11-valuation RRM + deliberation r-build | "One unaudited subsidiary" cited under both governance +1.5 and complexity +0.5; each stands on independent sufficient triggers, no material double-charge; r=16.0% holds. Home the fact to one adjustment for a clean single-credit trail. |
| C (phase 3) | 14-thesis Section 7 verdict box | Amdt 4.3 first-line "Tier: A | Hurdle: 25%" not printed verbatim (tier derived and used correctly). Presentational; synthesis verdict card prints it verbatim. |
| D | B06 Part 1 Q2 | KSOLVES debtors under 60 days quote placed in Q&A; it is in prepared remarks p.8 of 25. Cosmetic location error. |

## Decision-rule audit (Role 2, phase 3, B12c)

- Promoter override printed: PASS. BUY gate respected: PASS. AVOID map overridden to PROCEED: PASS. Position size Small ceiling / no position now: PASS. Promoter cap binds size: PASS.
- Tier line verbatim: MINOR (now corrected at synthesis).
- Decision-matrix cell: Verifier read RESEARCH-WATCH on (proof, gap); the signed STRUCTURAL-FEATURE ugliness (09b B5) makes the correct cell VALUE-TRAP RISK per the devil (B15). Synthesis carries the more bearish read.

## Scope notes

- Verifier B concurs with the B05 credibility grade D. Promise-delivery spot checks: 5 of 5 confirmed.
- Verifier D corrected peer utilisation to 9 of 12 (0.75) from B06's stated 10 of 12; the "10/12" is the arithmetic error found above.
- Verifier C phase-3 valuation pass: destination PE and decision concur, valuation ACCEPTED, no rework.
