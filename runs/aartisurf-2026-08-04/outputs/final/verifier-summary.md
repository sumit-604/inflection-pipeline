# Verifier summary (phase 1): AARTISURF 2026-08-04

## Phase 1 confidence delta

| Component | Score | Verifier | Acceptance |
|-----------|-------|----------|------------|
| Numerical acceptance | 93.1 | A (B12a, haiku) | 93.1 |
| Red flag coverage | 86 | B (B12b, opus) | 73 strict / 86 partial credit |
| Framework adherence (Gate0 + EM only) | 97.8 | C (B12c, opus) | 98 |
| Peer utilisation | 92 | D (B12d, sonnet) | 92 |
| Overall | 86 | min of four (red flag coverage binding) | normal band 75 to 89 |

Scope note: Verifier C rows below cover the Gate 0 and Emerging Moat portion only; the valuation half is pending phase 3. No B12a finding carries `source_fidelity: true`; the sole Verifier A MAJOR was a false misread and is cleared at source. Overall 86 sits in the normal band, so no downgrade and no rework.

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| D | B06.md Part 1 Q6 table; B06-peers contradicted[2] quote_anchor; peer_coverage_map ROSSARI Jul-2026 entry | Decisive customer concentration quote ("no customer >2% of sales; top-10 at 12-13%") pinned to ROSSARI Jul-2026 Q1FY27 call p.17, where it does not appear | GATE HELD. Anchor corrected to ROSSARI May-2026 Q4FY26 call p.16, lines 571-574. Quote genuine and correctly transcribed; CONTRADICTED verdict stands. Both Verifier B and D caught it. |

### MAJOR

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| A | B01-gate0.md Block B CFO figure | FY26 CFO Rs 76.65cr (screener) vs Results "~7.60cr", flagged as a 10x discrepancy | FLAG CLEARED. False haiku lakhs to crore misread; audited cash flow statement (results 9ac5e08e line 605) shows 7,678.84 lakhs = Rs 76.79cr. B01's Rs 76.65cr is correct. `source_fidelity: false`. FY26 CFO/PAT 6.21x stands; the working capital release caveat also stands. |
| C | B07 Section 5 adjusted total / em_score 14.5 | Nine non-zero rows sum to 13.5, reported 14.5, a +1.0 misadd | Corrected to 13.5. Classification MODEST (12 to 24 band) and combined AVERAGE both unchanged; decision survives. |
| D | B06.md Part 1 Q4 net read | Galaxy K. Natarajan "4% growth" quote sourced to Aug-2025 call p.16-17; actual extraction p.12 | 4 to 5 page mislocation. Supports an UNVERIFIABLE finding, so no verdict change. |
| D | B06.md Part 1 Q1 net read | FCL supplier renegotiation quote sourced to May-2026 call p.9; actual extraction p.6 (p.9 is UAE/Middle East content) | Used for the mechanism behind FCL's one off margin jump; verdict (weighted down, no read across to Aarti) unaffected. |

### MINOR

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| A | B04-bizmodel.md Section 4C question #5 | Preference share redemption dated 20-Aug-2026; source shows 19-Aug-2026 | Date off by one day. Principal Rs 18.50cr and face value verified. Carry 19-Aug-2026. |
| B | B05 §2A row2 promise-delivery | Revenue growth marked delivered without surfacing headline PAT 1,499.00 to 1,267.83 lakhs and diluted EPS 17.71 to 14.96 (results 9ac5e08e p.11) | Optical decline driven by FY25 one times B05 itself flagged; clean basis rose. Presentational gap, not a hidden red flag. |
| B | B05 §4D red_flags | CARE 7% PBILDT negative sensitivity floor already breached on a sustained basis (FY25 5.32%, H1FY26 5.33%) not surfaced as a live further downgrade trigger (rating p.1) | Under weighted. Carried as monitorable. |
| B | B05 §2A row2 / §4A | FY26 revenue growth overstated as clean beat: cost of materials +33% (54,184.43 to 72,093.50 lakhs) outpaced revenue +30%, i.e. partly raw material passthrough not volume (results 9ac5e08e p.11) | Under weighted. B06 partially catches via "no peer describes a demand boom". Carried as monitorable. |
| B | B06 Q6 contradicted anchor | Decisive ROSSARI concentration quote cited as Jul-2026 Q1FY27 p.17; actual May-2026 transcript l.572-574 | Citation error only; CONTRADICTED verdict stands. Same item as the Verifier D CRITICAL, surfaced independently from cross-read. |
| C | B01 Block A FY26 ROCE 9.72% | Computed on average capital employed (30,723.68) not year-end (32,103.16); year-end = 9.30% | Zero sub-score and classification impact; A1/A2/A4/M3 all unchanged. |
| D | B06.md Part 1 Q3 net read | Galaxy "Premium Specialty wait-and-watch" quote at p.4; actual extraction p.3 | Off by one. Content genuine. |
| D | B06.md Part 1 Q1 net read | Galaxy "fatty oil prices increasing 6 months" at p.5; actual extraction p.4 | Off by one. Content genuine. |
| D | B06.md Part 1 Q2 peer evidence | Galaxy "fatty alcohol never been so high" at p.3; actual extraction p.4 | Off by one. Content genuine. |
| D | B06.md Part 1 Q3 peer evidence | Galaxy Feb-2026 tariff cut "major structural positive" at p.3; actual extraction p.4 | Off by one. Content genuine. |
| D | B06.md Part 1 Q3 peer evidence | ROSSARI "terry towel companies under pressure" at p.9; actual extraction p.8 | Off by one. Content genuine. |
| D | B06.md Part 1 Q1 net read | FCL Jul-2026 QoQ comparator figures (13.93% EBITDA, 29-30% gross) grouped under the p.5 citation; comparators actually on p.9 | Composite citation half correct; current quarter figures genuinely on p.5. |
| D | B06-peers.yaml peer_coverage_map FCL Dec-2025 | Labelled CITED-ONLY, but cash funded debt free capex discipline is used as direct support in the Q5 CONTRADICTED narrative | Defensible label; SUBSTANTIVE / CITED-ONLY boundary drawn slightly inconsistently against usage. |

## Counts and acceptance

- Verifier A (B12a): 58 numbers checked, 0 CRITICAL, 1 MAJOR (cleared as false), 1 MINOR. Acceptance 93.1.
- Verifier B (B12b): 11 independent red flags, 8 fully caught, 3 partially caught, 0 fully missed, 0 CRITICAL, 0 MAJOR, 4 MINOR. Acceptance 73 strict, 86 partial credit.
- Verifier C (B12c), Gate0 + EM scope: 92 rules checked, 0 CRITICAL, 1 MAJOR, 1 MINOR. Acceptance 98. Valuation half pending phase 3.
- Verifier D (B12d): 12 peers audited, 11 substantive, 1 CRITICAL (anchor, gate held), 2 MAJOR, 7 MINOR. Acceptance 92.
