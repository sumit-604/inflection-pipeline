
## Confidence delta and acceptance rates
| Component | Verifier | Acceptance rate |
|---|---|---|
| Numerical acceptance | A (B12a) | 84 |
| Redflag coverage | B (B12b) | 71 |
| Framework adherence | C (B12c) | 98 |
| Peer utilisation | D (B12d) | N/A (skipped) |
| Overall | | 71 |

Band 60 to 74. REWORK gate triggered (B12a critical_count 2).

## Findings, CRITICAL first

CRITICAL
| Verifier | Location | Note |
|---|---|---|
| A | B10 p.113-126 | TAM 102.0 / SAM 73.4 / SOM 1.32 / SOM 1.62 Rs Cr should be Rs 10,200 / 7,340 / 132 / 162 Cr; 100x unit error; B09 5E confirms source; B11 corrected before valuation logic; FLAG-DATA on B10. |
| A | B10 p.15 | shares_outstanding_cr 11.4463 should be 1.14463 Cr (114.46 lakh); 10x unit error; B11 flagged FLAG-DATA and corrected for per share math; no verdict impact. |

MAJOR
| Verifier | Location | Note |
|---|---|---|
| A | B10 p.113 | market_cap_cr 169.0 versus reconciled 139.6 Cr (CMP 122 x 1.1446 Cr shares); per share valuation runs off CMP/EPS; secondary impact only. |
| A | B07 p.107 | Export revenue FY25 Rs 6,716.52 L (+38.35%) versus Notice Annexure Rs 2,616.05 L (minus 31.28%); unreconciled internal AR contradiction; B07 carries caveat. |
| B | B05 Section 4D / 2C-2D | No red flag on Directors' Report clean audit framing versus auditor Rule 11(g) / 143(3)(b) reservation; central disclosure integrity miss. |
| B | B05 Section 4C | CARO (ix)(a) technical interest default (Rs 1.11 L Nov 2024) not surfaced; contradicts "Strong" balance sheet characterisation. |
| B | B05 Section 4C / 4D | Remuneration above 11% of net profits (Section 197(16)) and buried remuneration disclosures not flagged; Rimika RPT raise. |
| B | B05 Section 1A trigger 1 / 3B | 38% export growth accepted at face value; same AR (General Info section 4) reports exports down 31.28%; unreconciled. |
| C | B11 Pillar 2 / Four-Pillar Summary | Cash multiplier 0.80x applied though cumulative CFO/PAT 2.80x and CFO positive every year; as written band 1.00x; recompute QAB 11.1x, Track1 7.8x, Hurdle still STOP, decision still AVOID; decision impact none. |

MINOR
| Verifier | Location | Note |
|---|---|---|
| A | B10 p.61 | ROCE Latest FY26 marked NOT FOUND but exists in B01 (7.74%, from 6.34/81.88); B11 conservatively used 7.2% low bound; appropriate. |
| A | B10 p.196 | 3 year Revenue CAGR NOT FOUND; FY24 full year not in input set; B11 anchored base 5% below SOM ceiling 9.0%; no verdict impact. |
| A | B10 p.196 | 3 year PAT CAGR NOT FOUND; same data gap; B11 derived PAT bottom up; no verdict impact. |
| B | B05 Section 3D / 4D | Customer concentration anchored to Note 45(d) p.24; figure correct, true location AR p.90; anchor imprecision only. |
| C | B11 Pillar 1 / FTTCP integration | FTTCP ROCE forward verdict (DECLINING) self derived in stage, not injected from discrete FTTCP artifact; rule consistent and most conservative; procedural gap only; no numeric change. |

Verifier D (B12d): SKIPPED. Stage 6 skipped (no peer concalls); no B06 coverage map to audit; acceptance_rate N/A, excluded from the confidence delta minimum, not scored 0.
