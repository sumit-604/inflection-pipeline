# Verifier summary (phase 3 final)

## Confidence delta and acceptance rates

| Component | Score | Source | Acceptance / basis |
|---|---|---|---|
| Numerical acceptance | 97.7 | B12a (verifier A, haiku) | 43 figures audited against full source set (AR FY26, Q3/Q4 results, ICRA); 0 CRITICAL |
| Redflag coverage | 67 | B12b (verifier B, opus) | 8 of 12 independent flags caught; 2 MAJOR, 4 MINOR, 1 missed |
| Framework adherence | 97 | B12c (verifier C, opus) | 106 of 109 rules passed across both halves (Gate 0 46, Emerging Moat 39/40, valuation 21/23) |
| Peer utilisation | 83 | B12d (verifier D, sonnet) | 10 of 12 peers substantively used; discipline 100 |
| Overall | 67 | confidence.yaml | minimum of the four |

Overall 67 sits in the 60 to 74 band and downgrades the gate verdict one level. No CRITICAL across any verifier, no acceptance below 60, so REWORK is not forced. Verifier C now covers both halves (Gate 0 plus Emerging Moat, and the valuation half B10/B11); the phase 1 valuation deferral is closed. Verifier B remains the weakest component and drives the overall.

## Findings, sorted CRITICAL then MAJOR then MINOR

### CRITICAL

None across all four verifiers.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A | B01 Gate 0 deal-breaker analysis | Rs 133.75 cr IT block period tax demand is NOT FOUND in AR or results; AR states "no demands raised as of reporting date." Appropriately identified as NOT FOUND by B01 and not scored into the verdict; originates from B08 web sources, contradicted by the primary AR. |
| B | B05 4D#6 / trigger #1 | European CDMO contract is FIXED PRICE to December 2032 (Q3 p10, Q4 p11); six year input cost exposure on the number one growth pillar amid acknowledged Middle East crude and solvent inflation (Q4 pp6-7) was not surfaced as a risk, only single customer concentration was. |
| B | B05 red flags / cash conversion | FY26 OCF of Rs 1,181 cr is "majorly attributable to the European contract that was assigned" (Q4 p4); ex advance FCF was Rs 90 cr in Q2. The cash quality caveat was not elevated to a red flag or FY26 view and was handed to stage 11/13. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| A | 02-notes.md anchor precision | AR page citations rendered as "p.20150" are text file line numbers, not PDF pages; 100% of numerical figures verify exact when cross referenced to page markers. Extraction labelling artefact. |
| B | B05 (absent) | Working capital days rose 91 to 105 with advance payments to creditors during the "wartime" build (Q4 p4), volunteered but not captured. |
| B | B05 3B | Q3 lists and live introduces two Managing Directors, Sanjeev and Sandeep Jain (p1/p2); B05 downgrades to listing anomaly, understating governance salience for a promoter family company. |
| B | B05 (absent) | FY27 top line guidance refused (Q4 Deeya p13) after a Q3 promise to "better guide on next year" (p9). |
| B | B05 2A promise table | Plant 2 EU GMP labeled a roughly one month slip; under a fiscal Q4 reading, January 2026 approval is on time, a slightly harsh classification. |
| C | B11 pillar_detail.roce_recovery_route | "pillar1-midpoint" mislabels a STAGNANT current ROCE route; no recovery credited (Strategic +0x); no numeric impact, destination PE unchanged. |
| C | B10/B11 Pillar 3 | "3c Duration Premium" is not in the committed Section 1B v3.4 file (framework has 3a+3b only; 3c lives on an unmerged branch); scored +0x so combined +1x and destination PE are correct; extra framework structure flagged with a latent +6x cap bypass risk if 3c later pays. |
| C | B07 Section 2C | capex_embedded_growth_pct emitted as numeric 0 in the pre AR run; corrected to 20.6% on re-run, no score impact. |
| D | B06 Part 1, Claim 1; Cohance Q2 FY26 | The minus 8% / +14% figure (Himanshu Agarwal, Q2 FY26 p6) is total consolidated company revenue, not a Pharma CDMO segment specific figure; the Q3 (minus 27% / +7%) and Q4 (early single digit) anchors for the same claim ARE segment specific and accurate, so the conclusion survives; only the Q2 anchor's segment label is imprecise. |

## Counts

- Verifier A: 0 CRITICAL, 1 MAJOR, 1 MINOR (43 numbers checked, 97.7 acceptance).
- Verifier B: 0 CRITICAL, 2 MAJOR, 4 MINOR (12 independent flags found, 8 caught, 3 partially caught, 1 missed; 67 acceptance). Credibility grade concur: C.
- Verifier C: 0 CRITICAL, 0 MAJOR, 3 MINOR (both halves, 109 rules checked, 97 acceptance).
- Verifier D: 0 CRITICAL, 0 MAJOR, 1 MINOR (12 peers audited, 10 substantive confirmed, 100 discipline).
