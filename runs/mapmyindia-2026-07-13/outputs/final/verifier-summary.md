# Verifier Summary (Phase 1)

## Confidence delta and acceptance rates

| Component | Verifier | Score | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | A (B12a) | 90 | 90% (28/31 numeric claims clean; 0 CRITICAL) |
| Redflag coverage | B (B12b) | 60 | 60% (12/20 verifier flags fully caught upstream; 0 CRITICAL) BINDING |
| Framework adherence (Gate 0 + Emerging Moat only) | C (B12c) | 100 | 100% (58/58 rule checks pass; valuation half deferred to phase 3) |
| Peer utilisation | D (B12d) | 100 | 100% peers used; cite-anchor accuracy 78% |
| OVERALL | min | 60 | redflag-bound; 60 to 74 band, no forced REWORK |

No verifier returned a CRITICAL finding. No acceptance rate fell below 60. Verifier C's valuation-adherence audit is deferred to phase 3 (B10/B11 not yet produced).

## Findings, sorted by severity

### CRITICAL
None across all four verifiers.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A | B01 Block B, FY26 capex line | FY26 capex claimed Rs42.40 Cr (cited to results FY26 p.9) but audited consolidated cash flow shows Rs49.38 Cr; recomputes FY26 FCF to Rs43.95 Cr from Rs50.93 Cr. |
| A | B02 Finding 7, RPO conversion sub-claim | "13% actual vs 15% guided vs 20% guided forward" not found anywhere in the AR on full-text search; unanchored to any provided source (unbilled-revenue and POC-mix figures in the same finding verify exactly). |
| B | B05 vs Q4 FY26 p.10-11 (Gautam Rathi / Rohan Verma) | Missed: core C&E/API business stuck at ~Rs80 to Rs85 Cr for three to four years, down from Rs100 to Rs120 Cr, masked by IoT and government growth; management did not dispute it. Thesis-relevant. |
| B | B05 vs Q4 FY26 p.3 (Rakesh Verma) | Recorded 5-year CAGR (revenue 24% / EBITDA 19% / PAT 11%) but did not flag PAT compounding at under half of revenue as a profitability-compression signal. |
| B | B05 vs Q4 FY26 p.6 (Rakesh Verma) | Did not flag cash balance flat to down (Rs676 Cr to Rs639 Cr to ~Rs600 Cr) against a "generated a lot of cash" claim; receivables absorbed the generation. |
| D | B06 Part 2B (Labour Code cross-read) | Newgen wage-revision quote cited to the Q2 FY26 (Oct 2025) call p.10; quote is actually in the Jan 2026 (Q3 FY26) transcript p.10. Wrong call. |
| D | B06 Part 2E (competitive-entry risk) | Newgen platform-competitor quote (Salesforce/ServiceNow/Mendix/OutSystems) cited to Q2 FY26 p.16; actually in the Jul 2025 (Q1 FY26) transcript near p.21. Wrong call and page. |
| D | B06 Part 1 Q3 (AI-readiness claim) | The report's own "single strongest independent confirmation" quote (Newgen Jan 2026) cited to p.5-6; actual location p.11, a 5 to 6 page miss on the most load-bearing anchor. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| B | B05 2C consistency vs Q4 FY26 p.8-9 (Gautam Rathi) | Under-weighted the quarter-versus-full-year framing reversal an analyst directly challenged after years of "look at full year" coaching. |
| B | B05 2C over-promotion vs Q3 FY26 p.8 (Rakesh Verma) | Noted Mappls metrics as promotional but not the internal implausibility: 100M MAU claim exceeds 45M cumulative downloads. |
| B | B05 vs Aug 2025 p.3-4 (Rakesh / Rohan Verma) | Caught Zepto silence but not the revenue-quality angle of a Rs25 Cr equity investment into a customer that then adopts MMI APIs. |
| B | B05 vs Q3 FY26 p.2 (Rakesh Verma) | Did not flag the "no Labour Code liability" claim as a peer outlier (peers took Rs18 to Rs35 Cr hits); B06 covered it at pipeline level. |
| D | B06 Part 1 Q1 (Newgen Jul 2025) | "Public sector momentum slightly lesser" cited p.4, actual p.7 (3 off); "addressable market has closed" cited p.16, actual p.17 (1 off). |
| D | B06 Part 1 Q5 (Newgen Jul 2025) | "top 20, we don't lose anything" churn quote cited p.16, actual p.18 (2 off). |
| D | B06 Part 1 Q4 (Newgen DSO data) | DSO/receivables citations cited p.4, both actually p.5 (1 off each); underlying figures (123/125 days, Rs504/Rs530 Cr) accurate. |
| C | B01 Block A / M3 | ROCE via proxy Capital Employed (Equity + Borrowings), not the fixed EBIT/(TA-CL) formula; permitted under grounding rule 5, disclosed, ~1% cross-check. No score impact. |
| C | B01 Block B B2/B3/B4 + M12 | Computed on the FY24-26 3-year subset (payables/capex NOT FOUND pre-FY24); B2=5 on a 3-year window is generous but disclosed. No classification impact. |
| C | B01 E2 | 3-year promoter-change rule applied on a 1-year proxy (-1.26pp), flagged; score 1 unchanged. |
| C | B01 M3 | ROCE 20.92% includes ~11% other income; ex-OI M3 would step 5 to 3 (moat 22 to 20) but stays present; 5 moats, STRONG, GOOD+ all unchanged. Flagged in-report. |
| C | B07 6D | EXCELLENT+ combined placement not mechanically checkable versus an enumerated matrix in the stage prompt; verified for internal logic only. |
| C | B07 E1/A4 | Scored 1.0x though evidence_type mixed documented/spoken; documented anchors dominate, defensible. |

## Spot checks and coverage notes

- Verifier B promise-delivery spot checks: 5 checked, 5 confirmed, 0 wrong. Credibility grade C concurred, biased to C-minus.
- Verifier D peer utilisation: 9/9 provided peer transcripts substantively used with verbatim content; anchor imprecision concentrated in Newgen cites does not indicate non-use.
- Verifier A coverage: verdict-card figures (classification GOOD+, market cap Rs6,488 Cr, CMP Rs1,185) verified exactly; Gate 0 Blocks A to E inputs verified.
- Verifier C: valuation-adherence checks (0 rules) pending phase 3; concurs GOOD+ (Gate 0) and EXCELLENT+ (combined) on the gate0 + emerging-moat scope.
