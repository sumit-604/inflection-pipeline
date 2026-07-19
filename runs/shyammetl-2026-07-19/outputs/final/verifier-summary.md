# Verifier summary (phase 1)

Confidence delta (overall 69, band 60 to 74, PROCEED family downgrades one level, not forced REWORK):

| Component | Verifier | Score / acceptance |
|---|---|---|
| Numerical acceptance | A (B12a, haiku) | 77% (24 clean of 31 distinct numbers) |
| Red flag coverage | B (B12b, opus) | 69% (11 of 16 independent flags caught) |
| Framework adherence (Gate 0 + EM) | C (B12c, opus) | 96% ((90 rules - 4 fails) / 90) |
| Peer utilisation | D (B12d, sonnet) | 75% (3 of 4 peers substantive) |

Source fidelity gate: HELD. One CRITICAL Verifier A mismatch (CARO count 11 to 10) corrected at source with an auditable per entity anchor; non verdict card red flag count, so no REWORK escalation. Zero fabrications. All Gate 0 verdict card and Section 1B pillar inputs verified clean. Valuation framework adherence pending phase 3 (B10/B11 not built this run).

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Note |
|---|---|---|
| A | B02 CARO clause 3(xvii) count; AR PDF p.233 (printed p.260) | Claimed 11 of 13 group entities cash loss qualified; true 10 of 13 per auditable per entity list. Corrected at source; conclusion (systemic group wide cash losses, ~77%) unchanged. source_fidelity. |

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| A | B02 standalone related party trade receivables; AR Note 42 standalone | 729.52cr / 78.1% corrected to 726.53cr / 77.77% (immaterial 2.99cr / 0.33pp). Corrected. source_fidelity. |
| A | B04 FY26 raw material / cost of materials ratio; audited Q4 FY26 P&L p.10 | ~72% (Inv. Pres. deck bundling) corrected to 73.68% (13,680.15cr / 18,552.21cr, audited). Audited authoritative. source_fidelity. |
| A | B02/B03 SSPL entity share in consol profit (Note 47); AR PDF p.298-302 | 722.34 to 417.15cr (70.20% to 45.88%) not legible in verifier text/image extraction; sourced by two sonnet passes and stage 3 independently. Rendering limit, not fabrication; re-read phase 3. source_fidelity. |
| B | B05 vs Q4 FY26 transcript (margin/earnings quality); Ashish Kejriwal / Deepak Agarwal p12, Brij Bhushan p13 | MISSED red flag: Q4 headline 14.4% margin partly rests on favourable cost inventory build (days 99 to 123) and an unexplained ~Rs 5,100 price rise versus ~Rs 2,600 EBITDA/tonne gap; bears on Trigger 3 durability and the delivered margin promise. |
| D | B06 Part 2E, risks peers raise (iron ore import dependency) | Misattribution: the seven year high iron ore import quote, verbatim including "highlighting robust consumption trend", is GPIL Q4 FY26 p.5, not SARDAEN Q3 FY26 (read in full, quote absent). Fact real, wrong peer; GPIL role inverted from primary to implicit secondary. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 timeline_slippages (stainless) | PARTIALLY CAUGHT: stainless slippage captured but Q3 firmness (~FY27) understated, making the slip to March 2029 sharper than portrayed; intra Q2 26/27 vs 27/28 contradiction not noted. |
| B | B05 guidance (HR mill capacity) | PARTIALLY CAUGHT: HR/SMS fixed at 1.6 MTPA; transcript wobbles across 0.8 / 1.6 / 2.0 MT without reconciliation. |
| B | B05 vs Q3 FY26 transcript (aluminium) | MISSED: Trigger 1 aluminium realization down QoQ despite rising international prices; analyst flagged mix deterioration met with a soft answer. |
| B | B05 defensiveness, Q3+Q4 transcripts | MISSED: CMD terminated Q&A early on two consecutive calls (Q3 p16, Q4 p17). |
| C | B01 Block A / Formula Notes (GA-1) | ROCE computed from proxy capital employed (Equity+Reserves+Borrowings) instead of framework TA minus CL for FY18-24 where CL split absent; documented, cross checked within 1.9 to 3.1% of audited; no band or score change. |
| C | B01 Block F M10/M12 (GA-2 advisory) | FY26 trade receivables 904.59 identical to FY26 cash 904.59; possible transcription collision, routed to Verifier A number existence domain; M10 scoring logic holds. |
| C | B07 Section 5 scorecard, H1/R1 (EM-1) | Blended 0.85x evidence multiplier applied; taxonomy specifies only 1.0/0.7/0.5. Non directional, immaterial; STRENGTHENING unaffected. |
| C | B07 Section 3 vs Section 5, A4/C1/F1 (EM-2) | Summary classifies evidence documented but scorecard applies 0.5x inference multiplier; conservative (understates), no classification change. |
| C | B07 Section 3 count statement (EM-3) | Active category count stated inconsistently (headline 8 of 21, reconciliation 5+4=9, YAML 10); correct count 10; presentational, em_score 30 unaffected. |
| D | B06 GPIL Q1 FY26 citations (Q1 and Q2 evidence) | Quote verbatim and accurate; page claimed p.5, actual p.4 of 21 (off by one, two instances). |
| D | B06 GPIL Q3 FY26 citations (Q1 and Q2 evidence) | Quote verbatim and accurate; page claimed p.4, actual p.5 of 19 (off by one, two instances). |
| D | B06 GALLANTT Q4 FY26 citation (Q6 evidence) | Claimed p.6 and p.9; actual p.7 and p.9 (p.6 has no capex figure); one of two anchors off by one. |
| D | B06 SARDAEN Q3 FY26 citation (Q2 evidence) | Content accurate; claimed p.3, passage spans p.3 into p.4 of 12; anchor covers only first half. |
| D | B06 SARDAEN Q4 FY25 citation (Q2 evidence) | Content accurate and locatable at p.5 of 20; page anchor omitted entirely. |
