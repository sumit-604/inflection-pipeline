Verifier summary, phase 1

Confidence delta (phase 1): numerical_acceptance 85, redflag_coverage 100, framework_adherence 93 (Gate 0 plus Emerging Moat; valuation pending phase 3), peer_utilisation 100, overall 85, band normal (75-89).

Acceptance rates: Verifier A 85%, Verifier B (v2) 86%, Verifier C 93%, Verifier D 100%.

Process note. Verifier B run1 caught a systematic under-read in B05 v1: the stated 20-25% guidance was missed, a false CFO-present premise was carried, and the transcript was wrongly treated as scanned. Stage 5 was re-run. Verifier B run2 re-audited the corrected B05 v2 and returned redflag_coverage 100%, acceptance 86%, credibility C. GATE HELD, corrected at source and re-verified. The B05-run1 and B12b-run1 artifacts are archived and superseded.

Verifier-A source-fidelity disagreement log for this run: none. No Verifier A source-fidelity flag was cleared or overridden downstream.

No CRITICAL findings from any verifier (critical_count 0 across A, B, C, D).

MAJOR findings.

| Verifier | Location | Note |
|---|---|---|
| A (numerical) | B01 Block B / Block A ROCE FY26 | FY26 capex NOT FOUND; FY26 results filing image-only, not text-extractable; Block B reduced to FY23-FY25. source_fidelity true. Does not change AVOID. |
| A (numerical) | B01 Block E E4, p.52 | FY26 contingent liabilities NOT FOUND; FY25 Rs 357.82 lakhs used (Annexure AB p.189); staleness on a KPI up 325% two years. source_fidelity true. No verdict change. |
| A (numerical) | B03 Phase 3 p.145; B04 3D | FY24 effective tax rate 37.97% from an unexplained Rs 79.88L deferred-tax swing; numeric cause documented, strategic reason not in RHP extracts; earnings-normalisation adjustment. |
| A (numerical) | B05 p.101/p.128 | H1 FY26 revenue Rs 42.70 cr verified to the lakh; FY26 full-year margin sustenance unconfirmed (FY26 filing image-only). Conservative handling. |
| A (numerical) | B05 1C/2A; B07 1A; B08 5C | Jul-2026 Reg 30 order wins ~Rs 67.85 cr ex-GST across four zones and CFO resignation 28-Jul-2026 are operator-supplied provenance, not checked against original BSE Reg 30 PDFs; BSE-portal verification recommended. |
| C (framework) | B01.md end-of-file | Mandated stage: B01-gate0 YAML block absent from the report artifact; captured separately in outputs/blocks/. Storage-convention artifact, no score affected. |
| C (framework) | B07.md end-of-file | Mandated stage: B07-emoat YAML block absent from the report artifact; captured separately in outputs/blocks/. Storage-convention artifact, no score affected. |
| D (peers) | B06 Part 2B, plastics RM paragraph | Anchor mismatch on the ~45% virgin polypropylene decline; Q3 p.4 supports only 30-35%, the 45% sits at GRP Q2 p.3, never cited for this claim; underlying fact real but mis-cited across quarters. |
| D (peers) | B06 verified block Q6 | VERIFIED rests on a single peer (GRP Ltd, 5 anchors across 4 quarters); Rule 4 requires >=2 independent peers, so this should be PARTIALLY VERIFIED. Mitigated by peer-set scarcity, not resolved. |

MINOR findings.

| Verifier | Location | Note |
|---|---|---|
| A (numerical) | B03 Phase 3 p.125 | Two RHP FY25 RoNW figures, Annexure X 36.22% (closing) vs Summary/MD&A 44.23% (average), unreconciled; disclosure inconsistency, not a numeric error. |
| A (numerical) | B01 Block C p.193; B04 3B p.249 | EBITDA margin fell 20.17% (FY25) to 16.21% (FY26); FY26 half from image-only PDF, unverified. |
| A (numerical) | B02 F15 p.137; B03 p.145 | Gratuity actuarial gain Rs 19.46L exact and anchored (Annexure AD p.191); ~Rs 21L PAT-inflation estimate appropriately marked. |
| B (red-flags) | B05 red flag #9 (rated LOW-MEDIUM) | Margin quality-of-earnings under-weighted: EBITDA +61.3%, margin 17.99%->26.63%, PAT +103.53% on only +8.47% revenue with no mechanical driver stated; warrants a HIGH/MAJOR QoE flag, not a guidance-consistency footnote. |
| B (red-flags) | B05 3A/3B/3D | Core-segment pricing/quality erosion captured only as competitive intel, not double-booked as a direct margin risk to the 55%-of-revenue railway-pad core. |
| B (red-flags) | B05 (not noted) | Maiden-call analyst roster entirely retail / small-broker / individual investors, no institutional participation; a modest disclosure-scrutiny signal absent upstream. |
| C (framework) | B01 Block F, M10 | Switching costs scored 1 vs strict-ladder 0; 1pt too generous, immaterial to moat count, class, and classification. |
| C (framework) | B07 Section 3, recount line | Completionist recount stated 22 documented items; itemisation sums to 16; guard conclusion of 5 active categories unaffected. |
| D (peers) | B06 industry_cross_read.demand | GRP Q3 p.2 India-EU FTA as a demand driver not incorporated; context item, does not affect any of the six B05 verdicts. |

Verifier coverage counts. Verifier A: 88 figures checked, 0 CRITICAL, 5 MAJOR, 4 MINOR. Verifier B (v2): 14 independent flags, 12 caught, 2 partially caught, 0 missed, 0 CRITICAL, 0 MAJOR, 3 MINOR. Verifier C: 46 Gate 0 rules plus 14 Emerging Moat rules checked, 0 CRITICAL, 2 MAJOR, 2 MINOR; valuation scope pending phase 3. Verifier D: 3 peers audited, 1 substantive confirmed, peer_utilisation 100%, peer-set completeness 33% (1 of 3 named peers had a transcript).
