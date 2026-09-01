# VINYAS — Verifier Summary (Phase 1)
Run date: 2026-09-01 | Phase 1 verifiers: A (numerical), B (red flag), D (peer), and the Gate 0 + emerging moat scope of C. Valuation adherence (rest of C) is pending phase 3.

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate |
|---|---|---|---|
| A (B12a) | Numerical acceptance | 98 | 98 |
| B (B12b) | Red flag coverage | 94 | 82 |
| C (B12c) | Framework adherence, Gate 0 + emerging moat | 90 | 90 |
| D (B12d) | Peer utilisation | 83 | 75 |
| Overall | min of four | 83 | normal band (75 to 89) |

No CRITICAL findings across any verifier. One MAJOR source-fidelity finding (A) and three MAJOR peer coverage findings (D). Valuation framework adherence pending phase 3.

## Findings sorted by severity

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| A | 01-gate0.md Block D1 (Net Debt); repeated 03-ardeep.md Phase 3B | Cash and bank Rs 18.45 Cr overstated about 13x. Source truth Rs 1.39 Cr (consolidated Note 8.2). Corrected Net Debt about Rs 128.66 Cr vs reported Rs 111.61 Cr. source_fidelity: true; do not carry Rs 18.45 Cr into any valuation computation. |
| D | 06-peers.md Claim 5 (SYRMA) | SYRMA PCB plant capex reported as "~Rs 400cr total across all phases"; transcript shows Rs 400cr is phase 1 alone (phase 2 flagged, phase 3 unquantified). Understates true cost about half, narrowing not eliminating the capex intensity gap Claim 5 rests on. |
| D | 06-peers.md coverage map (CYIENTDLM, Claim 4) | Credits CyientDLM SUBSTANTIVE for Claim 4 with "$0.5bn order pipeline confirmed"; Claim 4 text never cites CyientDLM and the Jul 2026 transcript shows management DISPUTING $0.5bn as too low, not confirming. SUBSTANTIVE tag without a findable accurate citation. |
| D | 06-peers.md Claim 4 (ASTRAMICRO) | ASTRAMICRO Rs 8,000-10,000cr is Astra's own program by program order intake guidance, not independent sector sizing. B06 discounts the similar KAYNES figure on this basis but not ASTRAMICRO's, then leans on it as strongest support for VINYAS's pipeline. Inconsistent evidentiary standard within one claim. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 4C | Missed within call PAT contradiction (Jun'25 MD line Rs 19.4 Cr vs CFO Rs 15.3 Cr, EPS 15.43); the "matches to the rupee" claim is overstated. |
| B | B05 1B/4D | Low promoter holding about 30% (no plan to increase) recorded as fact, not surfaced as a governance red flag for a micro cap. |
| B | B05 1B/1C | Rs 150 Cr raise not framed as a reversal of Jun'25 "capex done / working capital sufficient / no need" statements. |
| B | B06 Claim 5 | Treats "Rs 500-600 Cr per SMT line" as capex; transcript states it as revenue per line (capex about Rs 30 Cr). Magnitude leg of the CONTRADICTED verdict overstated; the 2-3 month timeline leg holds. |
| C | 01-gate0.md Block F M11 (Network Effects) | Top band requires selling expense % declining; FY26 selling expense merged into Other Expenses, so top band rests on FY20 to FY25 only. Immaterial: AVERAGE fixed by core 58 and deal breaker 4. |
| C | 01-gate0.md end | Report file lacks the mandated closing fenced YAML block; values present in prose and consumed downstream. VOID: B01-gate0.yaml stored as a separate run artifact. |
| C | 07-emoat.md I2 | I2 scored 1.0 on inference only with sacrifice "not proven-implausible"; above 0 defensible, kept out of top band. Immaterial: MODEST holds at 21.1 without the I family. Flagged for operator I1/I2 checkpoint. |
| C | 07-emoat.md end | Report file lacks mandated closing YAML block; content complete in prose. VOID: B07-emoat.yaml stored separately. |
| D | 06-peers.md Claim 7 (DATAPATTNS) | "~Rs 1,700cr single-vendor GeM order" conflates a negotiated but unbooked total with a distinct unquantified L1 single vendor GeM mention; transcript never states they are the same order. |
| D | 06-peers.md Claim 6 verdict | VERIFIED headline rests on only 2 of 5 named peers actually disclosing a concentration figure (other 3 not asked); caveat stated in prose but clean VERIFIED framing overstates the hit rate. |

## Verifier notes carried

- A: 47 material numeric claims verified against the FY26 consolidated AR (P&L, CFS, Balance Sheet, all 41 notes). Revenue, PAT, OCF, receivables ageing, inventory build, borrowings, leverage, ROCE/ROE all exact to source. 46 of 47 clean; one MAJOR flag on the cash position.
- B: 17 independent red flags found, 14 caught, 2 partially caught, 1 missed (the MINOR within call PAT contradiction). Promise delivery spot checks 5 of 5 confirmed. Concurs with credibility grade C.
- C: Phase 1 scope is Gate 0 and emerging moat only; 14 + 15 rules checked, 4 MINOR fails, all immaterial to the AVERAGE and MODEST classifications. Valuation adherence pending phase 3.
- D: 12 peers audited, 10 substantive, peer utilisation 83, all claims addressed, no verdict discipline fails. The three MAJOR findings weaken B06 Claim 4 (pipeline) and Claim 5 (capex).

## Source-fidelity disposition

The single source-fidelity finding (A, MAJOR, Rs 18.45 Cr cash overstated about 13x) was corrected against source in the gate recommendation: true cash Rs 1.39 Cr, corrected Net Debt about Rs 128.66 Cr. The flagged figure is not carried into any verdict card or table. GATE HELD by correction; no downstream step retained the flagged number as valid; no REWORK forced.
