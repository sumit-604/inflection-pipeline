# Verifier summary (phase 1)

Scope: Verifier A (numerical), Verifier B (red flags), Verifier D (peers), and the Gate 0 plus Emerging Moat portion of Verifier C. The valuation-adherence half of Verifier C is deferred to phase 3.

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 89 | A (B12a) | 89% (47 numbers audited) |
| Red-flag coverage | 62 | B (B12b) | 62% (13 independent flags, 8 caught) |
| Framework adherence | 96 | C (B12c) | 96% (Gate 0 + EM only) |
| Peer utilisation | 100 | D (B12d) | 90% acceptance, 13/13 peers substantive |
| Overall | 62 | min | binding floor: red-flag coverage |

No CRITICAL findings across any verifier after the single permitted Verifier A re-invoke. No source-fidelity findings. No forced REWORK.

## Findings, sorted by severity

### MAJOR

| Verifier | Location anchor | Finding |
|---|---|---|
| A | 02-notes rank 1; 03-ardeep phase 2 rank 1 | FX hedge notional USD 52.86m to USD 3.73m, -92.2%: figures verified exactly at source (Note 51/45(i)(a) consol). Retained as a RISK flag on unhedged FX exposure, not a numerical error. |
| A | 03-ardeep phase 2 rank 10 | Current tax 5.7% of PBT (2,107.02 / 36,669.99 Lakh): verified exactly. Retained as a cash-tax-vs-reported-rate concern, numerically clean. |
| B | Concall_Jun_2026 (Q4 FY26) p18 | MISSED by B05: Rs 804 Cr in-quarter prepayment nets to only ~Rs 220 Cr net-debt reduction (rest was a cash-credit limit cut); softens the deleveraging thesis. This is the binding red-flag-coverage miss. |
| C | 01-gate0 line 55 / B01-gate0.yaml | Gate 0 A1 band error: median ROCE 11.96% scored 3, correct 10 to 14.9% band = 1. Block A 9 to 7, core 42 to 40, grand 46 to 44. AVERAGE holds, no flip. |
| C | 01-gate0 line 95 / B01-gate0.yaml line 20 | Gate 0 deal-breaker 1: corrected Block A = 7 (<8) triggers DB1 (max GOOD); deal_breakers list is empty. No outcome change (AVERAGE below GOOD) but DB1 should be recorded. |
| D | 06-peers Claim 7 peer evidence row | "120 million case market" quote cited as May 2026; verbatim is in GLOBUSSPR-Concall_Jan_2026 line 686. CONTRADICTED verdict still stands on three other correctly-anchored Globus quotes. |
| D | 06-peers Claim 5 peer evidence row | "OMCs reducing volume offtake... not impacted" presented as same call as the May 2026 shift; the line is in GLOBUSSPR-Concall_Jan_2026 lines 628-629, ~4 months earlier. PARTIALLY VERIFIED verdict survives on correct May 2026 and Triveni Q1 FY27 anchors. |

### MINOR

| Verifier | Location anchor | Finding |
|---|---|---|
| A | 01-gate0 Block A (line 42-43) | Gate 0 ROCE PBT FY26 = 377.21 Cr (screener): exists at its cited source (screener Data_Sheet). AR consol PBT 330.79, AR standalone 366.70; a permitted screener-vs-AR basis difference, disclosed in data_notes. Reclassified from CRITICAL to MINOR on source verification. |
| A | 01-gate0 Block A (line 44-46) | Interest FY26 = 167.18 Cr (screener): correctly transcribed; AR consol finance costs 168.33 Cr, a 1.15 Cr immaterial basis difference. |
| A | 03-ardeep phase 2 rank 5 | CISCPL JV 100%-basis profit ~Rs 9,472.81 Lakh vs Board's Report Rs 9,462.60 Lakh: 0.11% precision gap, both 100%-basis, immaterial. |
| B | Concall_Aug_2026 (Q1 FY27) p3-8 | MISSED by B05: Ennature intra-call inconsistency, revenue 90cr (+53%) vs 83cr (+65%), EBITDA +188% vs ~+100%. |
| B | Concall_Aug_2026 (Q1 FY27) p14-15 | MISSED by B05: spirits volume grew faster than revenue, reverse of the premiumisation thesis. |
| B | Concall_Feb_2026 (Q3 FY26) p11 | MISSED by B05: two-part collaboration question half-dodged, LanzaTech answered, Lululemon never addressed. |
| B | Concall_Aug_2026 (Q1 FY27) p15 | MISSED by B05: sequential-EBITDA-growth question deflected to email under repeated insistence. |
| B | B05 repeated_evasions | OVERSTATED: segment-debt deflection framed as Q3+Q4 "every time"; clear on-call deflection is Q4 only. Nov 2025 (unread by B05) answered it with a 600/800 split. |
| B | B06 contradicted[] | OVERSTATED: UP-market "contradicted" by Globus is reconcilable, IGL's 23-25 lakh is IMFL-only and its ~90 lakh IMIL figure sums to ~1.1cr, matching Globus's ~1cr. B06 did flag for operator resolution. |
| B | Concall_Jun_2026 (Q4 FY26) p15 | OBSERVATION: 98cr silver sale (cost 51cr) kept off the P&L; disclosed and explained, neutral, but a 47cr gross gap worth naming. |
| C | B07-emoat.yaml | EM 2C: capex_embedded_growth_pct = 1 vs text ~1.2%; integer truncation, immaterial. |
| C | B07-emoat.yaml | EM 6D: combined HIGH POTENTIAL on a STRENGTHENING (33) not EXPANSION (>=40) forward score; matrix has no hard cells, full reasoning given, permissible judgment. Flagged. |
| D | 06-peers Part 2E / risks_peers_raise | Supreme Court / BPCL ethanol-tender stay attributed to both Jun 2026 and Jul 2026 Triveni calls; passage exists only in TRIVENI-Concall_Aug_2026 (30-Jul). Item real, correctly anchored in that call alone. |
| D | 06-peers Part 2C capex_cycle | Balrampur PLA capex (INR 3,080 cr) attributed to Aug 2026 call; figure is in BALRAMCHIN-Concall_Jun_2026 line 114. Two facts fused under one citation. |

## Verifier disagreement note

One disagreement logged. Verifier A first pass raised a CRITICAL source-fidelity flag on the Gate 0 Block A ROCE PBT figure (377.21 Cr), reading it as a fabrication or misread against the annual report's PBT. The orchestrator ran a source re-check and re-invoked Verifier A once. The number 377.21 exists exactly in the screener Data_Sheet, which is its cited source; the gap to the AR PBT is a screener-vs-AR consolidation basis difference, a permitted source disclosed in Gate 0 data_notes. Disposition: FLAG CLEARED. The finding was reclassified CRITICAL to MINOR (re-checked by the orchestrator plus the Verifier A re-invoke). No source-fidelity finding survives, so no REWORK is forced on this axis.
