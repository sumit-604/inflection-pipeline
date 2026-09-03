# Verifier Summary (Phase 1): VILAS, run vilas-2026-09-03

Phase-1 scope. Verifiers A (numerical), B (red-flag coverage), D (peer accuracy), and the Gate 0 plus Emerging Moat half of C. Verifier C's valuation-adherence half is deferred to phase 3.

## Phase-1 confidence delta

| Axis | Score | Acceptance basis |
|---|---|---|
| Numerical acceptance (A) | 96.6% effective (raw 89.7%) | 2 MAJOR source-fidelity flags cleared at source; 1 MINOR rounding remains |
| Red-flag coverage (B) | 73% | 16 caught + 2 partial of 22 independently found |
| Framework adherence (C, phase-1) | 100% | Gate 0 + Emerging Moat; 4 MINOR imprecisions, no rule misapplied |
| Peer utilisation (coverage) | 92% | 11 of 12 peers used substantively |
| Peer accuracy (D) | 75% | 3 MAJOR attribution errors in B06 |
| Overall | 73% | Min of the axes; red-flag coverage binds. Band 60-74 |

Verifier A note on source fidelity: Verifier A raised two MAJOR source-fidelity flags (FY26 current ratio, FY26 payable days). Both were re-checked against the same FY26 audited results sidecar and CLEARED; the pipeline report figures verify exactly at the source, and the two flags are Verifier A arithmetic slips. See verifier-disagreement-log.md. Neither forces REWORK. Effective numerical acceptance is 96.6% (28 of 29 clean).

Verifier A ran lean on Haiku. The full-corpus first attempt failed prompt-too-long on Haiku's window; the re-run audited the financial source-fidelity core against the screener dataset and the FY26 sidecar. Qualitative-number fidelity is covered by Verifiers B and D.

## Findings, sorted by severity

No CRITICAL finding stands across any verifier.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A (num) | 01-gate0.md Block D (D4 Current Ratio) | Claimed CA Rs 287.51 Cr / CR 3.83x vs Verifier A's Rs 297.51 Cr / 3.97x. CLEARED at source: report is correct; Verifier A over-added current assets by Rs 10 Cr. See disagreement log. |
| A (num) | 02-notes.md Block B4 (WC Days) | Claimed FY26 payable days 22.25 vs Verifier A's ~50 (COGS basis). CLEARED at source: Gate 0 fixed formula is revenue-basis on Rs 28.08 Cr payables = 22.25 days; report is correct. Verifier A itself flagged this unconfirmed. See disagreement log. |
| B (redflag) | B05 vs Concall May-2026 p.3, p.14-15 | MISSED: HV-bushing entity is 25% Vilas / 75% promoter, using Vilas customers, a group building, and the Yash Highvoltage founder as CEO; possible future merger at unstated terms. Promoter-favorable structure. |
| B (redflag) | B05 vs Concall May-2026 p.10-11 | MISSED: management's own admission that 14% EBITDA is a 1-in-3-4-year event; normal is 10 to 11% EBITDA and 7 to 8% PAT. Recalibrates the normalised earnings base. |
| B (redflag) | B05 vs Concall May-2026 p.23 | MISSED: other income ~15 to 20% of profitability (treasury/FD income) flatters PAT margin; IPO funds ~95% utilised. Not flagged as earnings-quality risk. |
| B (redflag) | B05 vs Concall Nov-2025 p.7-8 and May-2026 p.21 | PARTIALLY CAUGHT: a 2-quarter pattern of deflecting customer-weakness signals (Voltamp/Shilchar) with a firm-price-order narrative was framed only as a forward verification question, not as a deflection pattern. |
| D (peer) | B06 peer_coverage_map, PITTIENG H1 FY26 (May-2026) row | File marked UNUSED on a false "no extractable text" claim; file is fully readable and holds a fourth, earlier confirmation of the West Asia/war input-cost shock used for Q7. |
| D (peer) | B06 Q7 table, PITTIENG Aug-2026 row | Quote on LPG/war cost shock presented as an Akshay Pitti (management) statement; in the transcript it is spoken by analyst Mohit Jain as a question premise. |
| D (peer) | B06 risks_peers_raise, 544310/Yash Jan-2025 row | The 2-4 year bushing qualification-cycle quote attributed to the Jan-2025 call is actually from the Jun-2025 call (Lakshminarayanan K G exchange). |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| A (num) | 01-gate0.md Block D (Interest Coverage) | Claimed 25.4x vs recomputed 25.33x; EBIT rounding 53.77 vs 53.78. Immaterial. |
| A (num) | Multiple Block A-D ratios | All 26 other verified figures matched exactly or within rounding tolerance. |
| A (num) | 02-notes.md findings | B03's 15 major FY25 AR re-derivations confirmed sound against screener and sidecar; no contradictions. |
| B (redflag) | B05 vs Concall May-2025 p.16, May-2026 p.20 | PARTIALLY CAUGHT: nanocrystalline full-capacity potential collapsed Rs 150 Cr to Rs 25-27 Cr; only the near-term Rs 50 to 18-20 Cr cut was weighted. |
| B (redflag) | Concall May-2025 p.14, p.4 vs May-2026 p.5 | MISSED: Rs 10 Cr capex/CWIP reconciliation gap and FY25 EBITDA basis drift (14.8% reported to 12.68% Ind-AS restated). |
| B (redflag) | Concall May-2025 p.18-19, May-2026 p.3-4 | MISSED: amorphous-core demand challenged by a sector-expert investor; "64% growth precisely in line with target" spin on a missed 24,000 MT goal. |
| C (framework) | 01-gate0.md Block A / basis note | ROCE FY20-23 on Net Worth + Borrowings, a data-forced substitution for Total Assets minus Current Liabilities; disclosed, no A-block score change. |
| C (framework) | 01-gate0.md Block B / data_notes | FCF capex FY20-24 proxied by total Cash from Investing rather than PPE+intangibles; disclosed, feeds only an already deal-breakered Block B. |
| C (framework) | 01-gate0.md Block B B4 | WC-days change computed FY24 vs FY26, not FY20 vs FY26 (Trade Payables not broken out FY20-23); disclosed, direction and score 0 unaffected. |
| C (framework) | 07-emoat.md Section 3 recount vs B07 evidence_mix | Recount reports 5 documented items while evidence_mix.documented=12; different scopes, not reconciled; cosmetic, no score impact. |
| D (peer) | B06 industry_cross_read.demand / Q4 | "demand continues to significantly exceed global supply" described as Oct-2025/May-2026 repeatedly; exact sentence confirmed only in May-2026. |
| D (peer) | B06 Q7 table, Yash citation | "a forex hit already showing in finance costs (Keyur Shah)" is a reasonable paraphrase, not a direct quotation. |

## Verifier counts

- Verifier A (B12a): 29 numbers checked; 0 CRITICAL, 2 MAJOR (both cleared), 27 MINOR; raw acceptance 89.7%, effective 96.6%.
- Verifier B (B12b): 22 independent flags found, 16 caught, 2 partial; 0 CRITICAL, 4 MAJOR, 3 MINOR; acceptance 73%. Credibility grade C concurred.
- Verifier C (B12c), phase-1: 32 rules checked (20 Gate 0 + 12 Emerging Moat); 0 CRITICAL, 0 MAJOR, 4 MINOR; acceptance 100%. Valuation-adherence half deferred to phase 3.
- Verifier D (B12d): 12 peers audited, 9 confirmed substantive; 0 CRITICAL, 3 MAJOR, 2 MINOR; acceptance 75%.
