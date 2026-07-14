# Verifier summary — SFL (final, all five passes)

## Confidence delta and acceptance rates

| Verifier | Scope | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| A (B12a) | Numerical, 52 figures | 98.1% | 0 | 0 | 1 |
| B (B12b) | Redflag coverage, 10 flags | 90% | 0 | 0 | 3 |
| C gate0+emoat (B12c) | Framework adherence, 67 rules | 97% | 0 | 1 | 1 |
| C valuation (B12c-valuation) | Valuation-adherence B10/B11 + Role 2, 47 rules | 94% | 0 | 0 | 3 |
| D (B12d) | Peer utilisation, 4 peers / 23 citations | 91% | 0 | 1 | 2 |
| Overall | | 90 (high confidence) | 0 | 2 | 10 |

Confidence delta: numerical 98, redflag 90, framework 96 (Gate0+EM 97 merged with valuation 94), peer 100, overall 90. All five passes returned 0 CRITICAL. Both MAJOR findings are decision-neutral. Verifier C valuation concurs with destination PE 17.8x additive / 16.7x RRM and the AVOID-on-valuation / Hurdle STOP decision; no recompute required. REWORK not triggered.

## Findings, sorted by severity

### MAJOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 1 | C gate0+emoat (B12c) | B01 YAML history_downgrade + CLASSIFICATION section | history_downgrade:true contradicts the report's own text (ten-year full confidence, no history-length downgrade applies); the framework ties history_downgrade to the 3-4yr LIMITED tier-downgrade rule, which does not fire at ten years. Misstates a structured handoff field; the transition signal is already carried by FLAG-GATE0. Does not flip AVOID. |
| 2 | D (B12d) | B06 Part 1 Claim 3 and Part 3 peer coverage map, CENTURYPLY Nov-2025 (Q2 FY26) row | The quote "we need to stop looking at cycles... capturing the unorganized to organized... irrespective of the real estate cycle" (Nikita Bansal) is cited as Nov-2025 but is not present there; it is found in the Aug-2025 (Q1 FY26) transcript, lines 450-459, correctly attributed. Wrong-call citation; the Nov-2025 SUBSTANTIVE tag still stands on other correctly-cited material (Punjab flood spike, Sanjay Agarwal organised-share exchange). |

### MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 3 | A (B12a) | B02 Section A Finding #1 (FY22 consolidated revenue growth) | Claimed FY22 consolidated revenue growth of 22.4%; actual 20.57%. MINOR: an internal AR variance acknowledged in B03 (Chairman's 23%, MD&A 22.4%/20.6%, screener base 20.6%); pipeline cited one of the AR's own stated variants, not a calculation error. Anchor: Annual_Report_2023.txt line 4442. |
| 4 | B (B12b) | B05 vs Q4 FY26 call, Amit Gupta p.5-6 | H2 PAT concentration under-weighted: Rs 144 Cr of Rs 161 Cr FY26 PAT fell in H2 and management guides annualising the greater than Rs 70 Cr/quarter H2 run-rate, which is simultaneously lifted by the depreciation-policy change, the Furlenco Q4 step-up and favourable RM-inventory timing. Components each flagged by B05 but not tied together as one run-rate-quality caveat (partially caught). |
| 5 | B (B12b) | B05 1C/dropped_triggers vs Q2 p.11 and Q3 p.18 | COCO/Home Comfort "narrative inconsistency" flag slightly overstated: both Q2 and Q3 state 24 stores running and profitable and describe an evolving format; the change is emphasis, not a factual contradiction. |
| 6 | B (B12b) | B05 2D/4D vs Q3 p.9 and Q4 p.7,12 | Depreciation flag attributes the full ~Rs 35-40 Cr FY27 D&A reduction to the useful-life change, but the ~Rs 180 Cr baseline blends Kurlon intangible amortisation that rolls off independently; pure policy-change effect may be smaller. Direction valid; exact magnitude to be reconciled. |
| 7 | C gate0+emoat (B12c) | B01 methodology / Block A | ROCE computed as EBIT/(Net Worth + Borrowings) against the framework's fixed EBIT/(Total Assets - Current Liabilities) under a "do not substitute" header. Disclosed, consistent across years and peers, decision-neutral, forced by the CSV lacking a current/non-current split. |
| 8 | C valuation (B12c-valuation) | B11 Pillar 1 / B10 roce_cash_basis | Current-ROCE input uses operating/tangible Cash ROCE 13.0% not reported 6.7%; deliberation-authorised and disclosed; less-conservative direction but decision-neutral (reported basis gives an even harder STOP). |
| 9 | C valuation (B12c-valuation) | B11 RRM Track 1 | RRM applied to the full raw destination PE (17.8x) read as "Fundamental Base PE"; the Master spine leaves the term undefined; interpretation defensible and decision-neutral (6.2% divergence, both tracks STOP). |
| 10 | C valuation (B12c-valuation) | B11 Section 3 basis interaction | Pillar 1 multiple built on operating ROCE while PE x EPS uses reported EPS; handled conservatively via reported-ladder PPA convergence and a cash-basis robustness pass that still returns STOP; no double-count. |
| 11 | D (B12d) | B06 Part 1 Claim 3 (organised-share progression quote) | Quote "4%,4.5% -> 8%,8.5%" from CENTURYPLY Feb-2026 (Q3 FY26) attributed to Keshav Bhajanka; the actual speaker is Nikita Bansal (lines 367-379). Quote content and quarter correct; speaker name only wrong. |

## Verifier C — gate0 + emerging moat detail

- Gate 0: 38 rules checked, 1 MAJOR (history_downgrade semantics), 1 MINOR (ROCE formula substitution). Recomputed decision concurs: Gate 0 AVOID.
- Emerging Moat: 29 rules checked, 0 fails. EM 27/80 STRENGTHENING and combined TURNAROUND both concur.
- Combined 65 of 67 rules passed; acceptance 97%.

## Verifier C — valuation-adherence detail

- 47 rules checked, 0 fails, 3 MINOR passed-with-note; acceptance 94%.
- Framework adherence HIGH: Pillars 1 to 3, single-credit, UA ordering (Amendment 3), Building-materials 22x sector cap (genuine Master row, manifest "Agri processing" 20x correctly overridden), both RRM tracks (Amendment 4.4 percentage-point reading), Hurdle Ratio plus Tier A (Amendment 2/4.3), and Role 2 hardest-verdict-wins plus Small/Tier-A sizing all applied as written. Amendment 4.5 correctly NOT applied (permanent goodwill re-basing, documented unwind catalyst absent).
- Concurs: destination PE 17.8x additive / 16.7x RRM; AVOID-on-valuation, Hurdle STOP. No recompute required.

## Cross-verifier spot checks

- B12b promise-delivery spot checks: 5 checked, 5 confirmed, 0 wrong; credibility grade B concurred, H2-loaded PAT framing arguing against a higher grade.
- B12b: 10 independent flags found, 9 caught, 1 partially caught, 0 missed; 0 pipeline flags unsupported.
- B12d peer utilisation: 3 of 4 entities used substantively (WAKEFIT, CENTURYPLY, GREENLAM); NILKAMAL correctly UNUSED (no transcript); all 9 provided transcript-instances used (100% of transcripts provided); 21 of 23 sampled citations verified clean.
