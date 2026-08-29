# Entero Healthcare Solutions — Verifier Summary (Phase 1)

Phase 1 covers Verifier A (numerical), Verifier B (red flags), Verifier D (peers), and the Gate 0 and Emerging Moat portion of Verifier C (framework). The valuation portion of Verifier C is deferred to Phase 3.

## Phase 1 confidence delta

| Component | Score | Note |
|---|---|---|
| Numerical acceptance (B12a) | 89 | 0 CRITICAL; no verdict-card or pillar mismatch |
| Red-flag coverage (B12b) | 85 | 11 of 13 flags caught, 1 partial, 1 MAJOR missed |
| Framework adherence (B12c) | 98 | Gate 0 and Emerging Moat only; valuation PENDING PHASE 3 |
| Peer utilisation (B12d) | 92 | 11 of 12 peers substantive |
| **Overall** | **85** | min of the four; normal band |

## Acceptance rates

| Verifier | Scope | Acceptance rate | CRITICAL / MAJOR / MINOR |
|---|---|---|---|
| A (B12a, numerical) | 85 numbers checked | 89 | 0 / 4 / 0 |
| B (B12b, red flags) | 13 independent flags | 85 | 0 / 2 / 2 |
| C (B12c, framework, Gate 0 + EM) | 63 rules checked | 98 | 0 / 0 / 1 |
| D (B12d, peers) | 12 peers audited | 83 | 0 / 2 / 3 |

No CRITICAL across any verifier. No acceptance rate below 60. REWORK not triggered.

## Findings, sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location anchor | Note |
|---|---|---|
| A | B02 Finding 6 | Source-fidelity: "adjusted" net debt-to-equity 0.02x to 0.23x; adjustment methodology not traced to a note (consolidated D/E reads 0.09x to 0.31x). |
| A | B02 Finding 8 | Source-fidelity: CEO remuneration Rs43.74M to Rs94.50M (+116%); Note 52 p.235 exists, CEO line and +116% build not re-verified in abbreviated read. |
| A | B02 Finding 1 | Source-fidelity: net worth denominator Rs17,090.35M not found as a single line, appears computed from equity components; goodwill numerator Rs7,490.90M verified. |
| A | B02 Finding 12 | Source-fidelity: prior CFO name not in corpus; turnover asserted, pre-period name unanchored. |
| B | B05 2D/2E and red-flag table | MISSED the Q1 FY27 quarterly debt and OCF disclosure refusal (Q1 call p.14); part of a three-quarter granularity-opacity pattern. |
| B | B05 red flag 7 (net worth / put option) | PARTIALLY CAUGHT: minority buyout call options are a committed forward cash claim on thin OCF (Q1 p.3, 6-7, 11); accounting caught, cash-claim implication under-weighted. |
| D | B06 Part 1, Q5 evidence | "LIT is a better gross margin product" attributed to management (RPTECH May-2026), but it is the analyst's question premise; weakens the corroboration basis of the Q5 PARTIALLY VERIFIED grade. |
| D | B06 Part 3 coverage map, RPTECH Nov-2025 row | Labelled CITED-ONLY "no new decisive evidence," but Part 1 Q1 cites the same call for the "10-12% market" finding; internal inconsistency that understates the evidence. |

### MINOR

| Verifier | Location anchor | Note |
|---|---|---|
| B | B05 red flag 1 / 2D | Reach-metric label shifted "retail pharmacies" to "retail customers" Q4 to Q1; the relabel deepens rather than explains the contraction. |
| B | B05 1B item 7 / 4A#6 | Rising leverage framed only as an upside trigger, not a risk; about Rs 200 Cr fresh acquisition debt, IPO funds exhausted (Q1 p.7). |
| C | B07 Section 5 scoring table, rows B3/D2/D1 | Documented-labelled rows multiplied by 0.7 not the fixed 1.0; conservative deviation, no classification or UA-qualifier impact (18.8 vs strict <=20.7, both MODEST). |
| D | B06 Part 1, Q5 evidence | "close to 6% gross margins... PAT higher" presented as one continuous management response (REDINGTON Feb-2026); "6% gross margins" is analyst premise, only the PAT clause is management's. |
| D | B06 Part 3 / Q1 cross-reference | MEDPLUS SSSG "10.5% (Feb-2026 call)" not found verbatim; only an analyst paraphrase ("10% plus SSSG") appears; direction confirmed elsewhere in the same call. |
| D | B06 Part 2E | RPTECH "quantifies... the expected revenue hit" from Micron end-of-life overstates precision; the response is qualitative only, no number given. |

Verifier C Gate 0 scope: 38 rules checked, 0 fails.

## Source-confirm items for Halt 1

The four Verifier A MAJOR findings are all source-fidelity items. None sits on a verdict-card or Section 1B pillar input; none forces REWORK. Each is a source-confirm task for Halt 1, not a fabrication. Per the source-fidelity gate, none of these figures may enter a downstream computation as valid until re-anchored against the source.

1. B02 Finding 6 — confirm the "adjusted" net debt-to-equity basis against a note or footnote.
2. B02 Finding 8 — confirm the CEO remuneration line and the +116% build against the full Note 52.
3. B02 Finding 1 — confirm the Rs17,090.35M net worth aggregation used in the 43.8% goodwill ratio.
4. B02 Finding 12 — confirm the prior CFO name from a filing.
