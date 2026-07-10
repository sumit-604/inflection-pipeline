# Verifier summary (phase 1)

## Confidence delta and acceptance rates

| Component | Score | Source | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 93 | B12a (verifier A) | 93 |
| Redflag coverage | 67 | B12b (verifier B) | 67 |
| Framework adherence | 99 (Gate 0 + Emerging Moat; valuation half PENDING phase 3) | B12c (verifier C) | 99 |
| Peer utilisation | 83 | B12d (verifier D) | 100 |
| Overall | 67 (min) | confidence.yaml | |

Note: verifier C covers the Gate 0 (46 rules) and Emerging Moat (40 rules) portion only; the valuation adherence component (B10/B11) is deferred to phase 3. Verifier D acceptance rate is 100 on substantive claim discipline; the 83 peer utilisation figure is substantive_confirmed 10 over peers_provided 12.

## Findings, sorted CRITICAL then MAJOR then MINOR

### CRITICAL

None across all four verifiers.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A | B08 Promoter, Section 2C | IT tax demand of Rs 133.75 cr block period group demand (May 2026) is ANCHOR NOT FOUND against a primary CBDT order; reported as company disclosed via trade press only. Requires AR or tax disclosure verification in a future run. |
| B | B05 4D#6 / trigger #1 | European CDMO contract is FIXED PRICE to December 2032 (Q3 p10, Q4 p11); six year input cost exposure on the number one growth pillar amid acknowledged Middle East crude and solvent inflation (Q4 pp6-7) was not surfaced as a risk, only single customer concentration was. |
| B | B05 red flags / cash conversion | FY26 OCF of Rs 1,181 cr is majorly attributable to the assigned European contract advance (Q4 p4); ex advance FCF was Rs 90 cr in Q2. The cash quality caveat was not elevated to a red flag and was handed off to stage 11/13. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| A | B09 TAM, Method 3 | FY24 CDMO revenue of Rs 3,255 cr is estimated from the FY25 ratio applied to FY24 total (WebSearch, not primary verified); report correctly flags it as an estimate, arithmetic sound. |
| A | B08 Promoter, Section 1C | Claim that Sanjeev and Sandeep both discontinued education after 12th grade is UNANCHORED, media profiles only; biographical, no financial impact. |
| A | B06 Peers, PPLPHARMA | PPLPHARMA transcript is mislabeled and contains Piramal Finance (NBFC), not Piramal Pharma; report correctly identifies and marks UNUSED, Claim 2 verified via Cohance plus Innovacap instead. |
| B | B05 (absent) | Working capital days rose 91 to 105 with advance payments to creditors during the wartime build (Q4 p4), volunteered but not captured. |
| B | B05 3B | Q3 lists and live introduces two Managing Directors, Sanjeev and Sandeep Jain (p1/p2); B05 downgrades to listing anomaly, understating governance salience for a promoter family company. |
| B | B05 (absent) | FY27 top line guidance refused (Q4 Deeya p13) after a Q3 promise to better guide on next year (p9). |
| B | B05 2A promise table | Plant 2 EU GMP labeled a roughly one month slip; under a fiscal Q4 reading, January 2026 approval is on time, a slightly harsh classification. |
| C | B07 Section 2C / YAML capex_embedded_growth_pct | Not computable value emitted as numeric 0 in YAML; correctly NOT FOUND in narrative and input_gaps, but the structured field loses the not computable state. No score or classification impact. |
| D | B06 Part 1, Claim 1; Cohance Q2 FY26 | The minus 8% / +14% figure (Himanshu Agarwal, Q2 FY26 p6) is total consolidated company revenue, not a Pharma CDMO segment specific figure; the Q3 (minus 27% / +7%) and Q4 (early single digit) anchors for the same claim ARE segment specific and accurate, so the conclusion survives; only the Q2 anchor's segment label is imprecise. |

## Counts

- Verifier A: 0 CRITICAL, 1 MAJOR, 3 MINOR (45 numbers checked, 93 acceptance).
- Verifier B: 0 CRITICAL, 2 MAJOR, 4 MINOR (12 independent flags found, 8 caught, 3 partially caught, 1 missed; 67 acceptance). Credibility grade concur: C.
- Verifier C: 0 CRITICAL, 0 MAJOR, 1 MINOR (Gate 0 + Emerging Moat, 86 rules checked, 99 acceptance; valuation deferred).
- Verifier D: 0 CRITICAL, 0 MAJOR, 1 MINOR (12 peers audited, 10 substantive confirmed, 100 discipline).
