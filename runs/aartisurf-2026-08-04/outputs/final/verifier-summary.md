# Verifier summary (phase 1)

Confidence delta: numerical 96.6, red flag coverage 79, framework adherence 100 (Gate 0 + Emerging Moat; valuation half pending phase 3), peer utilisation 91.7, overall 79. Band normal (75-89): note specifics, no verdict downgrade, no forced REWORK.

Acceptance rates: Verifier A 96.6, Verifier B 79, Verifier C 100 (Gate 0 + Emerging Moat scope), Verifier D 92. No acceptance rate below 60. Verifier A found 0 CRITICAL source fidelity issues; the SOURCE FIDELITY gate held clean. There are no verifier disagreements of the Verifier A source fidelity kind: no downstream step leaned on, cleared, or carried a number Verifier A flagged.

Verifier D re-invocation: the first D run reported a CRITICAL "transcripts missing" finding, which was a mechanical look up error (it grepped binary PDFs). The 12 transcripts exist and are readable, confirmed by directory listing and by Stage 6, Verifier A, and Verifier B reading them. The corrected run read all 12 in full and is the record below.

## CRITICAL

None across all four verifiers.

## MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A | Stage 3 (03-ardeep.md Phase 3C), effective tax rate | Claimed ~2.2% current tax rate (current only) vs full effective 5.58% including deferred; basis interpretation, source data correctly used, not a MISMATCH |
| A | Stage 3 (03-ardeep.md Phase 2), payables | Claimed payables +305.9%, payable days 28.3 to 80.1; verified +305.87%, days 28.28 to 80.06; matches within rounding |
| A | Stage 2 (02-notes.md), notes | Claimed receivable days FY20 20.1; recomputed 20.07; immaterial rounding |

All three Verifier A MAJORs are immaterial rounding or basis interpretation; no verdict input impaired. AVOID classification, FLAG-CASH, and NO-EMERGING-MOAT conclusions all rest on verified pillars.

## MINOR

| Verifier | Location | Finding |
|---|---|---|
| B | B05 2C / 4D, deck slide 7 | MISSED over promotion: slide titled "Rating Upgrade" while both CARE ratings shown "Reaffirmed" (Inv. Pres. slide 7). This is the one flag that caps red flag coverage at 79 |
| B | B05 2B | OVERSTATED: "complete absence of any acknowledgement that a decline occurred"; deck discloses declines numerically, what is absent is causal narrative (Inv. Pres. slides 6-7) |
| B | B05 4C credibility_basis | PARTIALLY CAUGHT: delivery benchmarked to FY24; FY21 AR baseline (RoNW 25.14%) implies a larger multi year return collapse to ~6.6% ROE (AR p.11; deck slide 7) |
| B | B06 Q3 / 2E | MISATTRIBUTED: Rs5 Cr phenol figure is in the ROSSARI Jul 2026 call re Q4, not the Apr/May call; substance correct (ROSSARI-Concall_Jul_2026 p.13) |
| B | B06 Q5 | INR480 Cr not independently locatable in GALAXYSURF Nov 2025 (CWIP ~INR260 Cr confirmed); ROSSARI Q4 call actually dated 28 Apr 2026 |
| B | B06 Q1 / 2B | PARTIALLY CAUGHT: reformulation away from oleochemical surfactants surfaced as a Galaxy margin story, not linked as an AARTISURF specific volume risk (GALAXYSURF-Concall_Nov_2025 pp.3-9) |
| C | B01 Block A / ROCE formula | ROCE capital employed uses Net Worth + Total Borrowings proxy, not Total Assets minus Current Liabilities (screener balance sheet empty); disclosed, non decision changing; median 8.36% and min 5.92% sit far below thresholds |
| C | B07 Section 2C / capex_embedded_growth_pct | 11.1% computed on FY2020-21 revenue base, not current FY26 where it would be ~6%; disclosed and caveated; phase 3 valuation must confirm the base before any live catalyst credit |
| D | B06 Q5, GALAXYSURF Nov 2025 row | INR480 Cr capex attributed to Nov 2025 call; figure is from the May 2026 call; Nov 2025 supports the adjacent ~INR260 Cr CWIP; does not change the Q5 finding |
| D | B06 Q1, FCL Jul 2026 row | 13.93% framed as a Q1 FY26 YoY figure; it is "the last quarter" QoQ vs Q4 FY26; number correct, period basis QoQ; does not change the Q1 read |
| D | B06 Q5, ROSSARI Jan 2026 row | Rs192 Cr plan attributed to the Jan 2026 call; the figure is stated in Oct 2025 and referenced in May 2026, not restated in Jan 2026; the "still in force" inference is correct; does not change the Q5 finding |

## Counts

- Verifier A (B12a): 0 CRITICAL, 3 MAJOR, 0 MINOR; 87 numbers checked; acceptance 96.6.
- Verifier B (B12b): 0 CRITICAL, 0 MAJOR, 6 MINOR; 14 independent flags found, 11 caught, 2 partial, 1 missed; acceptance 79.
- Verifier C (B12c), Gate 0 + Emerging Moat scope: 0 CRITICAL, 0 MAJOR, 2 MINOR; 46 + 27 rules checked, 0 fails; acceptance 100. Valuation adherence pending phase 3.
- Verifier D (B12d): 0 CRITICAL, 0 MAJOR, 3 MINOR; 12 transcripts audited, 11 substantive confirmed; acceptance 92.
