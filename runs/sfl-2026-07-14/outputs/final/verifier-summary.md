# Phase 1 verifier summary — SFL

## Confidence delta and acceptance rates

| Verifier | Scope | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| A (B12a) | Numerical, 52 figures | 98.1% | 0 | 0 | 1 |
| B (B12b) | Redflag coverage, 10 flags | 90% | 0 | 0 | 3 |
| C (B12c) | Framework adherence, Gate 0 + EM only (valuation deferred to phase 3) | 97% | 0 | 1 | 1 |
| D (B12d) | Peer utilisation, 4 peers / 23 citations | 91% | 0 | 1 | 2 |
| Overall | | 90 (high confidence) | 0 | 2 | 7 |

Both MAJOR findings are decision-neutral: the Gate 0 AVOID, EM STRENGTHENING (27/80), combined TURNAROUND, and the underlying peer claim (verified in the correct quarter) are all unchanged. REWORK not triggered.

## Findings, sorted by severity

### MAJOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 1 | C (B12c) | B01 YAML history_downgrade + CLASSIFICATION section | history_downgrade:true contradicts the report's own text (ten-year full confidence, no history-length downgrade applies); the framework ties history_downgrade to the 3-4yr LIMITED tier-downgrade rule, which does not fire at ten years. Misstates a structured handoff field; the transition signal is already carried by FLAG-GATE0. Does not flip AVOID. |
| 2 | D (B12d) | B06 Part 1 Claim 3 and Part 3 peer coverage map, CENTURYPLY Nov-2025 (Q2 FY26) row | The quote "we need to stop looking at cycles... capturing the unorganized to organized... irrespective of the real estate cycle" (Nikita Bansal) is cited as Nov-2025 but is not present there; it is found in the Aug-2025 (Q1 FY26) transcript, lines 450-459, correctly attributed. Wrong-call citation; the Nov-2025 SUBSTANTIVE tag still stands on other correctly-cited material. |

### MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 3 | A (B12a) | B02, Section A, Finding #1 (Consolidated Revenue Growth FY22) | Claimed FY22 consolidated revenue growth of 22.4%; actual is 20.57%. MINOR because it is an internal AR variance acknowledged in B03 (Chairman's 23%, MD&A 22.4%/20.6%, screener base 20.6%); the pipeline cited one of the AR's own stated variants, not a calculation error. Anchor: Annual_Report_2023.txt line 4442. |
| 4 | B (B12b) | B05 vs Q4 FY26 call, Amit Gupta, p.5-6 | H2 PAT concentration under-weighted: Rs 144 Cr of Rs 161 Cr FY26 PAT fell in H2 and management guides annualising the greater than Rs 70 Cr/quarter H2 run-rate, which is simultaneously lifted by the depreciation-policy change, the Furlenco Q4 step-up and favourable RM-inventory timing. Components each flagged by B05 but not tied together as a run-rate-quality caveat (partially caught). |
| 5 | B (B12b) | B05 1C/dropped_triggers vs Q2 p.11 and Q3 p.18 | COCO/Home Comfort "narrative inconsistency" flag slightly overstated: both Q2 and Q3 state 24 stores running and profitable and describe an evolving format; the change is emphasis, not a factual contradiction. |
| 6 | B (B12b) | B05 2D/4D vs Q3 p.9 and Q4 p.7,12 | Depreciation flag attributes the full ~Rs 35-40 Cr FY27 D&A reduction to the useful-life change, but the ~Rs 180 Cr baseline blends Kurlon intangible amortisation that rolls off independently; pure policy-change effect may be smaller. Direction valid; exact magnitude to be reconciled. |
| 7 | C (B12c) | B01 methodology / Block A | ROCE computed as EBIT/(Net Worth + Borrowings) against the framework's fixed EBIT/(Total Assets - Current Liabilities) under a "do not substitute" header. Disclosed, consistent across years and peers, decision-neutral, forced by the CSV lacking a current/non-current split. |
| 8 | D (B12d) | B06 Part 1, Claim 3 (organised-share progression quote) | Quote "4%,4.5% -> 8%,8.5%" from CENTURYPLY Feb-2026 (Q3 FY26) attributed to Keshav Bhajanka; the actual speaker is Nikita Bansal (lines 367-379). Quote content and quarter correct; speaker name only wrong. |

## Verifier C Gate 0 + EM detail

- Gate 0: 38 rules checked, 1 MAJOR (history_downgrade semantics), 1 MINOR (ROCE formula substitution). Recomputed decision concurs: Gate 0 AVOID.
- Emerging Moat: 29 rules checked, 0 fails. EM 27/80 STRENGTHENING and combined TURNAROUND both concur.
- Valuation adherence (B10/B11 checks): pending phase 3, 0 rules checked in phase 1.

## Cross-verifier spot checks

- B12b promise-delivery spot checks: 5 checked, 5 confirmed, 0 wrong; credibility grade B concurred, with H2-loaded PAT framing arguing against a higher grade.
- B12d peer utilisation: 3 of 4 entities used substantively (WAKEFIT, CENTURYPLY, GREENLAM); NILKAMAL correctly UNUSED (no transcript); all 9 provided transcript-instances used (100% of transcripts provided).
