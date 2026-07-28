# Verifier summary, phase 1, SICALLOG 2026-07-28

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate | CRITICAL | MAJOR | MINOR |
|----------|-----------|-------|-----------------|----------|-------|-------|
| A (B12a, haiku) | Numerical acceptance | 95 | 93 | 0 | 1 (cleared) | 0 |
| B (B12b, opus) | Red-flag coverage | 61 | 50 (B05-only) | 0 | 4 | 5 |
| C (B12c, opus) | Framework adherence, Gate0 + EM scope | 95 | 95 | 0 | 0 | 4 |
| D (B12d, sonnet) | Peer utilisation | 100 | 83 | 0 | 1 | 2 |
| Overall | min, redflag-bound | 61 | band 60-74, one-level downgrade | 0 | | |

Verifier C valuation half (B10/B11) is deferred to phase 3. No CRITICAL anywhere; no fabrication; REWORK not triggered.

## Findings, sorted CRITICAL then MAJOR then MINOR

### CRITICAL

None across any verifier.

### MAJOR

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| A | B05 Section 1B table, Rights Issue row | Claimed Rs 93.03 Cr (11:5, Rs 64/share); Verifier A read audited note (e) as "29303 lakhs" = Rs 293.03 Cr, source_fidelity:true | FLAG CLEARED. Figure correct at source: 1,45,35,790 shares x Rs 64 = Rs 93,02,90,560 = Rs 93.03 Cr = 9,303 lakh, matching the Q3 board letter. The "29303 lakhs" is garbled OCR failing the filing's own share-count x price. Re-checked by orchestrator. Not a verdict-card or Section 1B pillar input. |
| B | B05 4D red-flag table / flags[] | D/E 4.1x to 1.6x presented as headline; total equity Rs 26,957 lakh is greater than 50% NCI (Rs 13,828 lakh vs owners Rs 13,129 lakh), owners-equity leverage about 3.3x. Anchor Q4 FY26 consol B/S 673-675 | MISSED by B05; independently caught by B04 (NCI overstatement). Carried into gate-recommendation. |
| B | B05 Section 1/3, segment mix | Mining 43 / Terminals 36 / Warehousing 21 mix used throughout; audited results report a single Ind AS 108 segment, mix is deck-only and unaudited. Anchor Q4 FY26 note (b) 401-403, Deck p.22 | MISSED by B05; independently caught by B04. Carried. |
| B | B05 Section 2, rights-issue treatment | Rights issue Rs 93 Cr for MPS plus debt/WC; promoter forwent entire entitlement, issue funded wholly by public. Anchor Q3 letter 40-42 | MISSED by B05; carried by B01/B08. Skin-in-the-game negative not raised by B05. |
| B | B05 whole-report context | FY26 turnaround assessed; company emerged from insolvency Mar-2021, write-downs FY21-23, acquired Jan-2023, an unproven roughly 3-year-old turnaround. Anchor Deck p.7 | MISSED by B05; carried by B01/B03/B07. |
| D | B06.md Q6 verdict table + Part 4 | Claimed GDL CFS EBITDA/TEU fell to Rs 2,500-2,700 vs desired Rs 2,900-3,000; the Oct-2021 stated recovery target is Rs 2,700/2,800, and Rs 2,900-3,000 is the April/May-2021 already-achieved level | Numeric conflation of two GDL calls; immaterial to any SICALLOG verdict. Underlying pass-through-failure quote correctly sourced. |

### MINOR

| Verifier | Location | Finding |
|----------|----------|---------|
| B | B05 cash-flow not addressed | Consolidated CFO Rs 5,229 lakh is pre-interest; finance cost paid Rs 4,705 lakh in financing. Anchor Q4 consol CF 724, 732. MISSED. |
| B | B05 flag #1/#2 | Consolidated other income Rs 3,689 lakh exceeds pre-exceptional PBT Rs 150 lakh. Anchor 619, 623. PARTIALLY CAUGHT, other-income dependency not isolated. |
| B | B05 flag #2 | Q4 was an outright reported net loss: standalone Rs -1,185 lakh (190), consol owners Rs -950 lakh (632); standalone opinion text says "net loss for the year". PARTIALLY CAUGHT. |
| B | B05 2C over-promotion | Deck p.19 "Strong Capital Backing from BlackRock"; BlackRock owns 57.5% of PLIL, two levels removed from Sical. PARTIALLY CAUGHT, specific name-drop not called out. |
| B | B05 trigger table | Deleveraging via Rs 13,031 lakh asset-sale proceeds plus Rs 9,022 lakh rights issue funding Rs 27,436 lakh LT-debt repayment. Anchor 727, 730-731. PARTIALLY CAUGHT, one-time/financing nature not flagged. |
| C | B01 Block A / A4 (gate0) | ROCE trend compares precise FY26 vs proxy FY17; immaterial, score 5 robust under either basis. |
| C | B01 Block F / M12 (gate0) | WC-float band literally 15-45 to 1 vs scored 0 on data-insufficiency (2 of 10 years); immaterial to moat_class NONE either way. |
| C | B07 scorecard / H3 (emoat) | H3 multiplier 1.0x on a doc/claim-mixed row; at 0.7x total 17.1, em_class MODEST holds. |
| C | B07 scorecard / R1 (emoat) | R1 impact Moderate vs its own "no differential advantage" conclusion; at Low total 16.4, em_class MODEST holds. |
| D | B06.md Part 2B | "let go a few customers" attributed to Aug-2025 and Feb-2026; verified verbatim only in Aug-2025 (Ravi Jakhar). Citation-span imprecision, not fabrication. |
| D | B06.md Part 2C | GDL Oct-2021 discloses 17-18% / 21%+ ROCE capex targets relevant to Sical's SECL/MMLP capex-return profile, not cited. Industry-context miss, no verdict change. |

## Verifier disagreement

One disagreement logged and resolved. Verifier A (haiku) flagged the FY26 rights-issue size as a MAJOR source-fidelity MISMATCH, reading a garbled "29303 lakhs" literally. The orchestrator re-check cleared the flag: B05's Rs 93.03 Cr is correct at source by the filing's own share count times price. Disposition FLAG CLEARED. This is the standing datapoint on whether haiku catches what opus misses; here haiku surfaced a genuine source ambiguity that an arithmetic cross-check resolved in favour of the downstream figure. Full row in outputs/_working/verifier_disagreements.md.
