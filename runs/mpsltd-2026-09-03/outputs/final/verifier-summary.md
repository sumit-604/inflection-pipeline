# MPS Limited (MPSLTD) — Verifier Summary (PHASE 1)

Phase-1 verifiers: A (B12a numerical), B (B12b red-flags), D (B12d peers), and the Gate 0 plus Emerging Moat portion of C (B12c). Verifier C's valuation audit is deferred to phase 3.

## Phase-1 confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 87.5 | A (B12a) | 87.5 |
| Red-flag coverage | 87 | B (B12b) | 53 fully-caught / 87 at-least-partial |
| Framework adherence | 96 | C (B12c, phase-1 scope) | 96 |
| Peer utilisation | 100 | D (B12d) | 75 (findings) / 100 (peer-entity) |
| Overall | 87.5 | min | band 75-89 NORMAL |

No verifier found a fabricated figure. Verifier A's block self-encodes critical_count:1, but the orchestrator records that item as a source-fidelity ANCHOR NOT FOUND on an operator SPEAR figure, not a fabricated or misread stage number; it is presented below at MAJOR.

## Findings, sorted by severity

### MAJOR

| Verifier | Location anchor | Finding |
|---|---|---|
| A (B12a) | B05 Section 1C / SPEAR gate | AJE revenue pruning ~USD 18m to 12m: NOT FOUND in any concall transcript. Trend (growth ex-AJE) verified; magnitude unanchored. source_fidelity:true, non-overridable. Corpus substitute: AJE LLC standalone FY26 revenue ~INR 10,097.28 lacs (~USD 12m), Directors' Report p.38-39. |
| A (B12a) | B01 Gate 0 Block D | FY26 consolidated borrowings 60.63 cr (screener) diverge Rs 24.38 cr from the audited BS 36.25 cr. Stage 10/11 must use the audited figure. |
| B (B12b) | B05 2A / 4D | Record FY26 EPS 102.11 treated as clean; a +INR 7.64 cr positive exceptional not flagged. Ex-exceptional EPS ~97-98, below the Rs 100 milestone. Anchor: Q4 FY26 call p.2-3. Binds Role 1 entry-EPS basis. |
| B (B12b) | B05 2E repeated-question tracker | Claimed no repeated evasion beyond Unbound revenue; forex and organic-adjusted growth were deflected in Q4 (Gunit Singh) and Q1 (Nachiket Kale). |
| B (B12b) | B05 2A row "EPS >100 delivered" | Scored delivered without caveat; FY26 EPS 102.11 sits below the Q2 FY26 TTM of 104, and H2 FY26 earnings declined. |
| D (B12d) | B06 Part 3, ECLERX Q2 FY26 row | Consolidation-of-suppliers quote and hedge/MTM disclosure sourced to ECLERX Oct-2025; both are verbatim in the Jan-2026 (Q3 FY26) call instead. Date/quarter transposition, no verdict change. |
| D (B12d) | B06 Part 2A cross-read | eClerx H1 FY26 "+20 percent YoY" is the INR growth rate; USD growth was +17 percent. Basis confusion in the "stays strong" framing. |
| D (B12d) | B06 Part 1 Claim 2 / INDGN Q1 FY27 row | "GenAI equalizes access to technology..." sourced to INDGN 31-Jul-2026; verbatim in the 30-Apr-2026 (Q4 FY26) call. Two quotes from two calls blended under one date. |
| D (B12d) | B06 Part 1 Claim 4 / INDGN Q1 FY27 row | "Agency, RO, and CRO spend is consolidating into specialized technology-led partners..." sourced to INDGN 31-Jul-2026; verbatim in the 30-Apr-2026 call. Same transposition; the +39.7 percent demand print in the cell is correctly dated. |
| D (B12d) | B06 Part 3, NIITMTS Q4 FY26 and Q1 FY27 rows | Labelled "signs of stabilization" and "continued recovery"; both transcripts disclose a named, quantified client-budget pullback in Tech/Telecom and Management Consulting that persisted across both quarters. Claim-relevant material left unused; fold into the Corporate Learning cross-read. |

### MINOR

| Verifier | Location anchor | Finding |
|---|---|---|
| A (B12a) | B05 Section 1C | Vision 2027 mix 40:40:20 (Feb-2026) versus 55:35:10 (Q4 FY26 / Q1 FY27). Both figures traceable; revision not explicitly flagged by management. |
| A (B12a) | B07 Section 1A | Five AI products moved to production in FY26; no itemized R&D spend disclosed (charged to P&L, BRSR R&D Nil). Product launches documented; cost basis opaque. |
| B (B12b) | B05 4D dividend flag | Dividend withholding disclosed transparently, but contradicts the Feb acquisition-call promise that distribution continues "for the foreseeable future"; cross-call reversal not connected. |
| B (B12b) | B05 1C / trigger table | Unbound called "high-margin" in Q3 versus disclosed 14 to 19 percent; characterization gap not flagged. |
| B (B12b) | B05 4D / 2D turnover flag | COO Sreenivas T.V. introduced as new hire in Q3, absent from the Q4 panel one quarter later. |
| B (B12b) | B05 Unbound acquisition coverage | Unbound founder Bill Detmer moved to advisor at close; key-person risk for a domain-authority asset. Anchor: Unbound acquisition call p.12, p.14. |
| D (B12d) | B06 Part 3, DATAMATICS Q2 FY26 row | Labelled CITED-ONLY; the 20.5 percent YoY figure from this call is the load-bearing data point in the Part 2A deceleration argument. Content and citation accurate; categorization understates use. |
| C (B12c) | B01 report file (end) | Mandated terminal YAML block absent from the report file; the block reached B07 at hand-off. Completeness gap, not a scoring error. Valid B01 block held in outputs/blocks/01-gate0.yaml. |
| C (B12c) | B01 Block A / ROCE table | ROCE computed as Net Worth + Borrowings instead of Total Assets - Current Liabilities; disclosed data-gap substitution. Every score sits far inside band; no score flips. |
| C (B12c) | B07 Section 3 summary | Prose states 8 active categories; nine distinct categories (C1, C2, D1, A4, F1, F2, G1, H1, H2) are enumerated and carried in the YAML. Count mislabelled; no threshold effect (both below the 12+ guard). |

## Verifier disagreement seed (source-fidelity)

One point where a source-fidelity finding met a downstream position. Verifier A verdict: AJE 18m to 12m ANCHOR NOT FOUND (B12a, source_fidelity:true), versus the SPEAR-supplied figure carried into the run. Disposition: GATE HELD — figure corrected at source. The magnitude does not enter any verdict statement; the AR-anchored substitute (AJE LLC ~USD 12m, Directors' Report p.38-39) is carried instead.
