# Verifier summary (phases 1 and 3): AARTISURF 2026-08-04

## Confidence delta

| Component | Score | Verifier | Acceptance |
|-----------|-------|----------|------------|
| Numerical acceptance | 93.1 | A (B12a, haiku) | 93.1 |
| Red flag coverage | 86 | B (B12b, opus) | 73 strict / 86 partial credit |
| Framework adherence | 97.6 | C (B12c Gate0+EM 97.8; B12c-valuation 97.5) | 98 / 97.5 |
| Peer utilisation | 92 | D (B12d, sonnet) | 92 |
| Overall | 86 | min of four (red flag coverage binding) | normal band 75 to 89 |

Valuation framework adherence (phase 3 half): 97.5. No B12a finding carries `source_fidelity: true`; the sole Verifier A MAJOR was a false misread, cleared at source. Overall 86 sits in the normal band. No downgrade, no rework: 0 Verifier A numerical CRITICAL, 0 valuation CRITICAL, all acceptance rates above 60. Cross family FTTCP grader did not run (no Gemini/Google key), so FTTCP confidence is held one notch below 86; no CRITICAL rubric violation, the check did not execute.

Decision note: the phase 3 MAJOR (B10 TTM EPS 14.10) was corrected to 22.09 in B11 before the decision, so it is decision invariant.

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| D | B06.md Part 1 Q6; B06-peers contradicted[2] quote_anchor; peer_coverage_map ROSSARI Jul-2026 entry | Decisive customer concentration quote ("no customer >2% of sales; top-10 at 12-13%") pinned to ROSSARI Jul-2026 Q1FY27 p.17, where it does not appear | GATE HELD. Anchor corrected to ROSSARI May-2026 Q4FY26 p.16, lines 571-574. Quote genuine and correctly transcribed; CONTRADICTED verdict stands. Verifier B and D both caught it. |

### MAJOR

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| A | B01-gate0.md Block B CFO | FY26 CFO Rs 76.65cr (screener) vs Results "~7.60cr", flagged as a 10x discrepancy | FLAG CLEARED. False haiku lakhs to crore misread; audited cash flow statement (results 9ac5e08e line 605) shows 7,678.84 lakhs = Rs 76.79cr. B01's Rs 76.65cr correct. `source_fidelity: false`. CFO/PAT 6.21x and the WC release caveat both stand. |
| C (valuation, VAL-1) | B10 L79 / B10 YAML ttm_eps_rs | TTM EPS 14.10 (removed the wrong quarter, Q4FY25 11.63) driving current PE 37.1x | Correct TTM EPS 22.09 (14.99 - Q1FY26 3.62 + Q1FY27 10.72), current PE 23.68x. B11 caught and corrected before the decision. Decision invariant (HR = FV/CMP). |
| C (Gate0+EM) | B07 Section 5 adjusted total / em_score 14.5 | Nine non-zero rows sum to 13.5, reported 14.5, a +1.0 misadd | Corrected to 13.5. Classification MODEST (12 to 24) and combined AVERAGE both unchanged; decision survives. Synthesis uses 13.5. |
| D | B06.md Part 1 Q4 net read | Galaxy K. Natarajan "4% growth" quote sourced to Aug-2025 p.16-17; actual extraction p.12 | 4 to 5 page mislocation. Supports an UNVERIFIABLE finding, no verdict change. |
| D | B06.md Part 1 Q1 net read | FCL supplier renegotiation quote sourced to May-2026 p.9; actual extraction p.6 (p.9 is UAE/Middle East content) | Used for the mechanism behind FCL's one off margin jump; verdict (weighted down, no read across to Aarti) unaffected. |

### MINOR

| Verifier | Location | Finding | Disposition |
|----------|----------|---------|-------------|
| A | B04-bizmodel.md Section 4C question #5 | Preference share redemption dated 20-Aug-2026; source shows 19-Aug-2026 | Date off by one day. Principal Rs 18.50cr and face value verified. Carry 19-Aug-2026. |
| B | B05 §2A row2 promise-delivery | Revenue growth marked delivered without surfacing headline PAT 1,499.00 to 1,267.83 lakhs and diluted EPS 17.71 to 14.96 (results 9ac5e08e p.11) | Optical decline driven by FY25 one times B05 itself flagged; clean basis rose. Presentational gap. |
| B | B05 §4D red_flags | CARE 7% PBILDT negative sensitivity floor already breached on a sustained basis (FY25 5.32%, H1FY26 5.33%) not surfaced as a live trigger (rating p.1) | Under weighted. Carried as monitorable. |
| B | B05 §2A row2 / §4A | FY26 growth overstated as clean beat: cost of materials +33% (54,184.43 to 72,093.50 lakhs) outpaced revenue +30%, i.e. partly raw material passthrough not volume (results 9ac5e08e p.11) | Under weighted. B06 partially catches. Carried as monitorable. |
| B | B06 Q6 contradicted anchor | ROSSARI concentration quote cited as Jul-2026 p.17; actual May-2026 l.572-574 | Same item as the Verifier D CRITICAL, surfaced independently. Verdict stands. |
| C (valuation, VAL-2) | B10/B11 vs fttcp-deliberation | CFO/PAT stated 0.90x/6.05x vs 0.77x/6.21x | Volatile band either way; Verifier A domain; cash multiplier 1.00x invariant. |
| C (valuation, VAL-3) | B11 4F | Upside/downside 0.09x | Base upside -5.8% is itself negative; already fails 2x. Cosmetic sign context. |
| C (valuation, VAL-4) | B14 decision-trace | Gate0 AVERAGE default WATCHLIST described as superseded by STOP | Gate0 AVERAGE is a direct AVOID trigger (Master L809); net AVOID over-determined; presentational. |
| C (Gate0+EM) | B01 Block A FY26 ROCE 9.72% | Computed on average capital employed (30,723.68) not year-end (32,103.16); year-end = 9.30% | Zero sub-score and classification impact; A1/A2/A4/M3 unchanged. |
| D | B06.md Part 1 Q3 net read | Galaxy "Premium Specialty wait-and-watch" at p.4; actual p.3 | Off by one. Content genuine. |
| D | B06.md Part 1 Q1 net read | Galaxy "fatty oil prices increasing 6 months" at p.5; actual p.4 | Off by one. Content genuine. |
| D | B06.md Part 1 Q2 peer evidence | Galaxy "fatty alcohol never been so high" at p.3; actual p.4 | Off by one. Content genuine. |
| D | B06.md Part 1 Q3 peer evidence | Galaxy Feb-2026 tariff cut "major structural positive" at p.3; actual p.4 | Off by one. Content genuine. |
| D | B06.md Part 1 Q3 peer evidence | ROSSARI "terry towel companies under pressure" at p.9; actual p.8 | Off by one. Content genuine. |
| D | B06.md Part 1 Q1 net read | FCL Jul-2026 QoQ comparators (13.93% EBITDA, 29-30% gross) grouped under the p.5 citation; comparators on p.9 | Composite citation half correct; current quarter figures genuinely on p.5. |
| D | B06-peers.yaml peer_coverage_map FCL Dec-2025 | Labelled CITED-ONLY, but content used as direct support in the Q5 CONTRADICTED narrative | Defensible label; SUBSTANTIVE / CITED-ONLY boundary drawn slightly inconsistently. |

## Counts and acceptance

- Verifier A (B12a): 58 numbers checked, 0 CRITICAL, 1 MAJOR (cleared as false), 1 MINOR. Acceptance 93.1.
- Verifier B (B12b): 11 independent red flags, 8 fully caught, 3 partially caught, 0 fully missed, 0 CRITICAL, 0 MAJOR, 4 MINOR. Acceptance 73 strict, 86 partial credit.
- Verifier C (B12c) Gate0 + EM: 92 rules, 0 CRITICAL, 1 MAJOR, 1 MINOR. Acceptance 98.
- Verifier C (B12c-valuation) phase 3: 40 valuation rules, 0 CRITICAL, 1 MAJOR (VAL-1, corrected in B11), 3 MINOR. Acceptance 97.5. Destination PE 12.2x and decision AVOID both concur.
- Verifier D (B12d): 12 peers audited, 11 substantive, 1 CRITICAL (anchor, gate held), 2 MAJOR, 7 MINOR. Acceptance 92.
