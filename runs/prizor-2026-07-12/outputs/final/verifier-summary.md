# Verifier Summary (Phase 3, full)

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance | Note |
|---|---|---|---|---|
| Numerical acceptance | 97.87 | A (B12a) | 97.87 | 0 critical, 0 major, 1 minor of 47 numbers |
| Red flag coverage | 62 | B (B12b) | 62 | 8 of 13 flags caught, 3 partial; stage 5 degraded no concall |
| Framework adherence | 100 | C (B12c) | 100 | Gate 0 (48), EM (24), valuation (34), 106 rules, 0 fails |
| Peer utilisation | 75 | D (B12d) | 100 | 3 of 4 peers substantive; D-Link had no transcript |
| OVERALL | 62 | min of four | 62 | band 60 to 74, one level downgrade, no forced rework |

Rework gate: verifier A critical count 0; minimum verifier acceptance 62 at or
above the 60 floor; overall 62 not below 60. Forced rework: false. Framework
adherence rose 94 to 100 once the phase 3 valuation adherence audit (34 rules,
0 fails) merged with the gate 0 and emerging moat checks; overall stays bound
by red flag coverage (62).

## Findings sorted by severity

### CRITICAL

None across all four verifiers.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B (B12b) | Stage 5 Sec 2A/4D omission; Inv.Pres. slide26/p27 | Rs 10.0 Cr long term loans and advances newly on FY26 balance sheet, purpose undisclosed, while borrowing Rs 31.82 Cr short term; material capital allocation or possible related party flag missed |
| B (B12b) | Stage 5 2D / flag #2 under-weight; Inv.Pres. slide32/p33 | Three year broken cash conversion; FY26 OCF plus Rs 0.29 Cr against PAT Rs 20.76 Cr, about 1.4% conversion, not surfaced (FY24 minus 1.82, FY25 minus 14.10) |
| B (B12b) | Stage 5 flag #6 misframe; Inv.Pres. slide23/p24 | AR affirmatively declares a single reportable segment while the deck reports two; audited versus unaudited contradiction should be MAJOR, was logged MEDIUM |
| D (B12d) | 06-peers.md Part 1, Q7 row | Wrong speaker and quarter: quote is Vivek Patel in the OSEL Nov 2025 call, not Mahesh Attal May 2025; genuine sourcing defect, does not change the Q7 verdict |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A (B12a) | B01 Gate 0, Block A EBIT presentation; AR p.72 | Screener finance cost 1.42 Cr does not match AR 1.2402 Cr; gate 0 EBIT calc (14.910 Cr) correctly used AR values; screener data quality issue, not a calc error |
| B (B12b) | Stage 5 omission; Inv.Pres. slide25/p26 vs slide30/p31 | FY25 cost split self contradicts across two deck slides (2,201.3/4,532.8 vs 6,282.9/552.7); totals reconcile, EBITDA unaffected |
| B (B12b) | Stage 5 flag #7 framing; Inv.Pres. slide26/p27 | Receivables build noted but H2 FY26 = 72% of full year revenue (10,592.7 vs 4,201.4), receivables 15.74 to 38.63 Cr; back ending / channel loading angle not drawn |
| B (B12b) | Stage 5 4C / flag #8 add-on | CFO is the promoter WTD, spouse of the CMD; segregation of duties concentration not called out |
| C (B12c) | B01 Block F / M7; prompts/01 lines 118-120 | Regulatory/license scored 0 as unregulated; a BIS mandatory certification regime exists, at most M7 = 1; no moat count or classification impact |
| C (B12c) | B01 Block F / M8; prompts/01 lines 121-123 | Distribution scored 0 (no network in AR); stage 7 documented an 11,000 plus dealer network from the presentation; differing input set, not a rule error; no moat count impact |
| C (B12c) | B01 Blocks A/B; prompts/01 line 31 | ROCE computed from AR rather than taken from source per formula preference; justified by empty screener CSV templates; provenance matter |
| C (B12c) | B07 Section 2C / capex_embedded_growth_pct; Sec1B Amdt 4.1 | Headline 116% is capacity based, not the prescribed FAT turnover method (~237%); both clear the 15% Pillar 3a qualifier, zero destination PE impact |
| C (B12c) | B07 Section 5 / R1; prompts/07 lines 128-132 | R1 rated HH despite the maker's own Moderate durability finding; HM would drop total to 12.6, still MODEST; within tolerance |
| C (B12c) | B14-thesis zone_reachability (14-thesis.md vs B14 YAML); Master v3.3 Role 2 / Amdt 4.3-4.4 | md says lowest tested listed price NOT FOUND; yaml says ~25% below the only reference Rs 105.25; cross-artifact anchor inconsistency; MARKET-UNLIKELY / DEEP WATCH classification correct either way; no decision impact |
| D (B12d) | 06-peers.md Part 2E | OSEL cash flow reclassification confirmed in the Jun 2026 transcript; the NSE compliance query framing is unanchored |
| D (B12d) | 06-peers.md Part 1, Q1 row | Single continuous Chinese players out quote is a compound of Prateek Chaudhary's question and Aditya Khemka's answer; faithful in substance, two speaker composition not flagged |
| D (B12d) | 06-peers.md scope note vs body | Call date labels (Jun vs May) reconcilable but never reconciled; cache filenames follow SEBI filing date, body labels follow actual call date |
| D (B12d) | 06-peers.md Part 1, Q5 cell | Sahasra EBITDA guidance 28 to 32% confirmed in the Nov 2024 call; figure accurate, granular call date anchor missing |
| D (B12d) | 06-peers.md Part 1, Q6 row | OSEL JNPT SEZ land; transcript uses JNPA; same entity, name variant, immaterial |

## Coverage notes

Verifier A (numerical, 47 figures): verified against AR FY2024-25, Screener
Data_Sheet.csv, and the FY26 investor presentation; verdict card numbers for
the AVERAGE classification (core 63, moat 19, deal breakers #4 and #9) all
clean; acceptance 97.87.

Verifier B (red flags, no-concall mode): stage 5 ran degraded from AR and deck
with no transcripts; all three major misses were surfaced from FY26
presentation data and reinforce the cash and governance read, none contradict
a pipeline finding; no pipeline flag found unsupported; credibility grade C
concurred; acceptance / coverage 62.

Verifier C (framework, phase 1 and 3 merged): Gate 0 (48 rules), Emerging Moat
(24 rules), and Valuation (34 rules) checked, 106 passed of 106; both
destination PE tracks, the Hurdle STOP, the two-tier assignment, UA ordering,
sector cap 25x, and the Role 2 AVOID / position None / DEEP WATCH chain
independently recomputed and tie exactly to the valuation and thesis blocks;
concurs AVOID; acceptance 100.

Verifier D (peers, 4 audited): central Q5 margin contradiction (Prizor 21 to
23% EBITDA / 14% PAT versus CP Plus 8.7 to 18.0% EBITDA / 4.4 to 11.9% PAT
plus 14 to 15% new normal) exactly anchored and verified clean; CP Plus
market share trajectory, Sahasra DDR shortage, and capex cycle figures all
accurate; peer coverage classification (3 substantive, 1 unused for D-Link)
correct; verdict discipline clean; acceptance 100, utilisation 75.
