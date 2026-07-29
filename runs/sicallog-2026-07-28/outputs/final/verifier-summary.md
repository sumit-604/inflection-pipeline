# Verifier summary, full four-component, SICALLOG 2026-07-28

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate | CRITICAL | MAJOR | MINOR |
|----------|-----------|-------|-----------------|----------|-------|-------|
| A (B12a, haiku) | Numerical acceptance | 95 | 93 | 0 | 1 (cleared) | 0 |
| B (B12b, opus) | Red-flag coverage | 61 | 50 (B05-only) | 0 | 4 | 5 |
| C (B12c, opus) | Framework adherence, Gate0 + EM + valuation | 94 | 94 | 0 | 0 | 7 |
| D (B12d, sonnet) | Peer utilisation | 100 | 83 | 0 | 1 | 2 |
| Overall | min, redflag-bound | 61 | band 60-74, one-level downgrade | 0 | | |

Framework adherence is now the FULL score: B12c covers phase-1 Gate 0 (40/42) and Emerging Moat (32/34) plus the phase-3 valuation half (31/34). The valuation half is clean: Verifier C recomputed the four-pillar destination PE (RRM 8.6x governing / additive 12.4x reproduce exactly) and CONCURS with AVOID on four independent triggers (Gate0 AVOID, promoter CONCERN, upside-to-downside below 2x, Hurdle STOP). No CRITICAL anywhere; no fabrication; REWORK not triggered across phase 1 or phase 3.

## Findings, sorted CRITICAL then MAJOR then MINOR

### CRITICAL

None across any verifier.

### MAJOR

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| A | B12a, B05 Section 1B table, Rights Issue row | Claimed Rs 93.03 Cr (11:5, Rs 64/share); Verifier A read audited note (e) as "29303 lakhs" = Rs 293.03 Cr, source_fidelity:true | FLAG CLEARED, gate held. Figure correct at source: 1,45,35,790 shares x Rs 64 = Rs 93,02,90,560 = Rs 93.03 Cr = 9,303 lakh, matching the Q3 board letter's spelled-out "ninety-three crore two lakh ninety thousand five hundred sixty". The "29303 lakhs" is garbled OCR failing the filing's own share-count x price. Re-checked by orchestrator; annotated on the B12a block. Not a verdict-card or Section 1B pillar input. Rs 293 cr does NOT reach any deliverable. |
| B | B12b, B05 4D red-flag table / flags[] | D/E 4.1x to 1.6x presented as headline; total equity Rs 26,957 lakh is more than 50% NCI (Rs 13,828 lakh vs owners Rs 13,129 lakh), owners-equity leverage about 3.3x. Anchor Q4 FY26 consol B/S 673-675 | MISSED by B05; independently caught by B04 NCI overstatement finding. Carried. |
| B | B12b, B05 Section 1/3 segment mix | Mining 43 / Terminals 36 / Warehousing 21 mix used throughout; audited results report a single Ind AS 108 segment, mix is deck-only and unaudited. Anchor Q4 FY26 note (b) 401-403, Deck p.22 | MISSED by B05; independently caught by B04. Carried. |
| B | B12b, B05 Section 2 rights-issue treatment | Rights issue Rs 93 Cr for MPS plus debt/WC; promoter forwent its entire entitlement, issue funded wholly by public. Anchor Q3 letter 40-42 | MISSED by B05; carried by B01/B08. Skin-in-the-game negative not raised by B05. |
| B | B12b, B05 whole-report context | FY26 turnaround assessed; company emerged from insolvency Mar-2021, write-downs FY21-23, acquired Jan-2023, an unproven roughly 3-year-old turnaround. Anchor Deck p.7 | MISSED by B05; carried by B01/B03/B07. |
| D | B12d, B06.md Q6 verdict table + Part 4 | Claimed GDL CFS EBITDA/TEU fell to Rs 2,500-2,700 vs desired Rs 2,900-3,000; the Oct-2021 stated recovery target is Rs 2,700/2,800, and Rs 2,900-3,000 is the April/May-2021 already-achieved level | Numeric conflation of two GDL calls; immaterial to any SICALLOG verdict. Underlying pass-through-failure quote correctly sourced. |

### MINOR

| Verifier | Location | Finding |
|----------|----------|---------|
| B | B12b, B05 cash-flow not addressed | Consolidated CFO Rs 5,229 lakh is pre-interest; finance cost paid Rs 4,705 lakh in financing. Anchor Q4 consol CF 724, 732. MISSED. |
| B | B12b, B05 flag #1/#2 | Consolidated other income Rs 3,689 lakh exceeds pre-exceptional PBT Rs 150 lakh. Anchor 619, 623. PARTIALLY CAUGHT, other-income dependency not isolated. |
| B | B12b, B05 flag #2 | Q4 was an outright reported net loss: standalone Rs -1,185 lakh (190), consol owners Rs -950 lakh (632); standalone opinion text says "net loss for the year". PARTIALLY CAUGHT. |
| B | B12b, B05 2C over-promotion | Deck p.19 "Strong Capital Backing from BlackRock"; BlackRock owns 57.5% of PLIL, two levels removed from Sical. PARTIALLY CAUGHT, specific name-drop not called out. |
| B | B12b, B05 trigger table | Deleveraging via Rs 13,031 lakh asset-sale proceeds plus Rs 9,022 lakh rights issue funding Rs 27,436 lakh LT-debt repayment. Anchor 727, 730-731. PARTIALLY CAUGHT, one-time/financing nature not flagged. |
| C | B12c, B01 Block A / A4 (gate0) | ROCE trend compares precise FY26 (17.42%) vs proxy FY17 (6.95%); not like-for-like. Score 5 robust under either basis, no block-total impact. |
| C | B12c, B01 Block F / M12 (gate0) | WC-float band literally 15-45 to 1 vs scored 0 on data-insufficiency (2 of 10 years); a score of 1 still below the moat-present bar, moat_class NONE either way. |
| C | B12c, B07 scorecard / H3 (emoat) | H3 evidence-type multiplier 1.0x on a doc/claim-mixed row; at 0.7x total 17.1, em_class MODEST holds. |
| C | B12c, B07 scorecard / R1 (emoat) | R1 impact Moderate (adj 3.0) vs its own "fully shared/non-exclusive" conclusion; at Low (2.0) total 16.4, em_class MODEST holds. |
| C | B12c, B11 3.3 tertiary peer cross-check (valuation) | B11 extracted peer EV/EBITDA from screener Data_Sheets that B10 marked NOT FOUND, to anchor the 10% tertiary SOTP slice multiples. Transparently flagged stale/illustrative; does not touch exit PE or any Section 1B pillar. |
| C | B12c, B11 Hurdle Ratio 1B/4H (valuation) | HR run on one-year-forward owners'-clean construct (current forward PE about 107x) rather than current trailing PE, because clean current EPS is negative/NM. Disclosed, internally consistent; STOP robust (would need about 190% EPS CAGR to clear 1.953). HR 0.27 RRM / 0.39 additive / 0.30 capped-bull. |
| C | B12c, B11 0/1B sector cap (valuation) | "Logistics (WC-heavy/project cargo) 20x" cap is operator-assigned in the FTTCP deliberation; Amendment 8 has no explicit Logistics row (nearest Mining 20x). Non-binding, both tracks far below 20x, zero impact. |
| D | B12d, B06.md Part 2B | "let go a few customers" attributed to Aug-2025 and Feb-2026; verified verbatim only in Aug-2025 (Ravi Jakhar). Citation-span imprecision, not fabrication. |
| D | B12d, B06.md Part 2C | GDL Oct-2021 discloses 17-18% / 21%+ ROCE capex targets relevant to Sical's SECL/MMLP capex-return profile, not cited. Industry-context miss, no verdict change. |

## Phase-3 valuation-adherence audit (B12c valuation half)

Verifier C re-derived the full valuation. Rules checked 34, passed 31, 0 CRITICAL, 0 MAJOR, 3 MINOR (all above). Recomputed destination PE reproduces exactly: 12.85 to 12.9 x 0.65 = 8.4, +4 +0 = 12.4x additive; 12.4 x 0.70 = 8.6x RRM. Recomputed decision CONCURS: AVOID (on valuation), position None, Tier A, four independent AVOID triggers. Confirmed no exit PE originates outside Section 1B; Pillar 1 normalization route correctly NONE; single-credit rule respected (ROCE recovery credited only in Pillar 1, Strategic Premium ROCE route barred). No source-fidelity finding on the valuation half.

## Verifier disagreements

Two rows this run, both on the FY26 rights-issue size, both resolved in favour of the downstream figure of Rs 93.03 cr. Row 1 (phase 1): Verifier A read a garbled "29303 lakhs" literally as Rs 293.03 cr; orchestrator re-check cleared the flag by the filing's own share count times price. Row 2 (phase 3): the devil's-advocate maker read the raw B12a block, did not see the phase-1 overturn, and inverted it, propagating Rs 293 cr in its management_trust dimension; gate held, figure corrected to Rs 93.03 cr, the devil's conclusion unaffected because the deleveraging was funded by the rights issue plus asset sales rather than operations at either figure. Full rows in outputs/final/verifier-disagreement-log.md. This is the standing datapoint on whether haiku catches what opus misses; here haiku surfaced a genuine source ambiguity that an arithmetic cross-check resolved against the flagged reading.
