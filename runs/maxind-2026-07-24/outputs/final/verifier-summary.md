# VERIFIER SUMMARY (PHASE 1) — MAX INDIA LTD (MAXIND)

Run date: 2026-07-24 | Stage: B13-synthesis | Model: claude-opus-4-8
Phase 1 verifiers: A (B12a, numerical), B (B12b, redflag), C (B12c, Gate0 + Emerging Moat scope), D (B12d, peer). Verifier C's valuation scope and phase 3 verifiers are not in this run.

## PHASE-1 CONFIDENCE DELTA AND ACCEPTANCE RATES

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| numerical_acceptance | 98 | A (B12a, haiku) | 98% (0 CRIT, 0 MAJ, 1 MIN; no source fidelity flags) |
| redflag_coverage | 70 | B (B12b, opus) | 70% fully caught (14/20), 90% at least partial |
| framework_adherence | 100 | C (B12c, opus) | 100% Gate0 + Emerging Moat scope; valuation PENDING PHASE 3 |
| peer_utilisation | 75 | B06 coverage map | 3 of 4 peers substantive |
| **overall** | **70** | | min = 70, redflag bound, band 60-74 |

Separate REWORK-rule input (not in the delta min): Verifier D (B12d) accuracy acceptance_rate 50% (2 MAJOR, 3 MINOR). Adjudicated NOT REWORK in the gate recommendation: both MAJORs are localized attribution/sourcing errors confined to the directional peer stage B06, substance survives, provenance corrected, confidence downgraded.

## FINDINGS (sorted CRITICAL, then MAJOR, then MINOR)

### CRITICAL
None across all four phase 1 verifiers.

### MAJOR

| Verifier | Location anchor | Note |
|---|---|---|
| D (B12d) | B06 Part 1 Q2 / Part 4 | GPT Healthcare "24 to 36 months to break even" slippage quote attributed to the Feb-2026 (Q3) call but found verbatim only in the May-2026 (Q4) call; the actual Feb-2026 call reaffirmed the original timeline. Misdates the report's key cross read by one quarter. |
| D (B12d) | B06 Part 2E / risks_peers_raise | Insurance empanelment lag (12 to 15+ months) attributed jointly to GPTHEALTH and KRSNAA; all four KRSNAA transcripts show zero mentions. Only GPTHEALTH supports it. Risk invented for KRSNAA. |
| B (B12b) | B05 1B guidance table / 1C / 4C consistency row | Care home maturity curve characterized as reaffirmed/stable when it quietly lengthened Q1 to Q4 (4 and 8 quarters to 4-6 and 8-10 quarters); missed drift on the core Assisted Care assumption. Anchor: Q1 Aug-25 p10 vs Q4 May-26 p13-16. |

### MINOR

| Verifier | Location anchor | Note |
|---|---|---|
| A (B12a) | B02 p.19 Top Finding #3; corrected B03 p.1B | B02 called the standalone auditor's report a SOLE KAM; it lists TWO (impairment of investments in subsidiaries, plus RPT evaluation). B03 corrected the count in phase 1B; substantive finding intact, only cardinality misstated. source_fidelity: false. |
| C (B12c) | B01 Block F M8 Distribution | Conservative group level read scored 1; a segment level read could support 3; no decision impact (Core 22 stays AVOID). |
| C (B12c) | B07 YAML capex_embedded_growth_pct | Body states NOT FOUND per the no estimation rule; YAML renders 0 (representational only). |
| B (B12b) | B05 4D flag 7 / 3D | Repeat customer flag conflates Q3 "65,000 unique customers" with Q4 "44,000 repeat"; correct comparable is Q2 50,000 repeat to Q4 44,000 repeat. Flag direction valid, anchor imprecise. |
| B (B12b) | B05 2A row 10 / 4A | Q4 loss improvement (27.8 to 6.8 Cr) presented as clean delivery; lumpy DM fee timing (Rs26 Cr E360 fee accrued FY26) that management warns may reverse to EBITDA loss in FY27, plus treasury basis shift, under weighted. |
| B (B12b) | B05 trigger-1 / Section 4A | Management's Q4 admission that Noida Phase 1 is "into red" (loss making) not surfaced; value case rests on unapproved Phase 2. |
| B (B12b) | B05 guidance table (care home EBITDA margin) | Steady state care home EBITDA margin quoted as both 18-20% and 16-18% within the same Q4 call; only the cross quarter restatement was captured. |
| B (B12b) | B05 (no location) / 2C consistency | "No debt at all" (Q1) versus "net debt of Rs105cr repaid" (Q2) never reconciled; likely SPV land dues but unexamined. |
| D (B12d) | B06 Part 1 Q4 and Q2 (MAXESTATES citations) | MAXESTATES Q4 FY26 call (Sector 105 GDV doubling, about 29% realization increase) labeled "May-2026" when the transcript cadence is Jun-2026; content accurate, month label wrong, recurs twice. |
| D (B12d) | B06 Part 2A (demand cross read) | Claims ASHIANA and MAXESTATES use "nearly identical language" on "West Asia conflict"; the exact phrase is only in MAXESTATES. Ashiana references "geopolitical situations"/"the war" but not the phrase. Directional point survives. |
| D (B12d) | B06 Part 1 Q5 / KRSNAA coverage | Krsnaa's own disclosed "20-25% CAGR" company growth figure (May-2026 call) not mentioned as an available (if weak) industry context point alongside Ashiana's CAGR citations. |

## VERIFIER NOTES

- Verifier A (B12a) verified 50+ material numbers across consolidated revenue (6 years), PAT (3 years), balance sheet items, subsidiary AOC-1 results and operating metrics, against the audited FY25 AR, FY26 audited results and the Q4 FY26 concall. Screener FY20 to FY23 marked as unaudited throughout; operator relayed non anchored figures excluded from verification scope.
- Verifier B (B12b) spot checked 5 promise delivery items, 5 of 5 confirmed; concurs with credibility grade C.
- Verifier C (B12c) recomputed Gate 0 (Core 22, Grand 24, AVOID) and Emerging Moat (em_score 27, STRENGTHENING, combined TURNAROUND) clean, 45 + 30 rules checked, 0 fails; valuation scope pending phase 3.
- Verifier D (B12d) audited 4 peers, confirmed 2 substantive claims, 0 substantive unsupported; the accuracy defects are provenance level, not substance level.
