# Verifier summary

## Confidence delta and acceptance rates

| Component | Score | Verifier |
|---|---|---|
| Numerical acceptance | 89 | A (B12a), haiku, 47 numbers checked, reinvoked once |
| Red flag coverage | 62 | B (B12b), opus |
| Framework adherence | 78 | C phase 1 Gate0+EM 96 (B12c-verifier-framework), C phase 3 valuation 78 (B12c-phase3); binding 78 |
| Peer utilisation | 100 | D (B12d), sonnet, 13 of 13 substantive |
| Overall | 62 | min of four; red flag coverage bound; band 60 to 74, one level downgrade |

Rework triggers present: none. No Verifier A source fidelity CRITICAL. No acceptance rate below 60. The one phase 3 CRITICAL was framework tier (Amendment 19 FV path over-roll), not source fidelity, acceptance 78% at or above 60, and it was corrected in a single targeted stage 11 re-run; the operator approved destination PEs and the AVOID decision were unchanged by the correction.

## Findings, CRITICAL first

### CRITICAL

- C phase 3 | 11-valuation.md Section 4 Amdt 19; B11 fv_cagr_pct/return_source_class | End-Year-3 FV rolled 4 steps not 3; corrected SOTP end-Y3 about 948.7, FV CAGR about 8.5% giving DISCOUNT-CLOSER, not 11.5% HYBRID. CORRECTED in stage 11 re-run. AVOID and entry zone survive; fails the hurdle either way.

### MAJOR

- A | 02-notes.md rank 1; 03-ardeep.md phase 2 rank 1 | FX hedge notional USD 52.86mn FY25 to USD 3.73mn FY26, minus 92.2%; figures verified exactly, retained as a RISK flag not a numerical error. source_fidelity: false.
- A | 03-ardeep.md phase 2 rank 10 | Current tax 5.7% of PBT (2,107.02 / 36,669.99 Lakh); calculation verified exactly, retained as a cash tax versus reported rate concern. source_fidelity: false.
- B | B05 red_flags / guidance, Concall_Jun_2026 p18 | MISSED: Rs 804 Cr prepaid nets to only about Rs 220 Cr net debt reduction; rest was a cash credit limit cut; softens the deleveraging thesis, never flagged.
- C phase 3 | 11-valuation.md Entity B Track 1 | 16.6x carried versus 16.0x at stated r=15.0%; Amdt 4.4 RRM and conservative track governs. STOP/AVOID unchanged.
- C phase 3 | 11-valuation.md Section 4D/4E | Tier A justified as FII+DII<3% contradicts B10 ua_qualifiers (at or above 3%); Tier A correct only via the HIGH POTENTIAL limb; divisor and zone unaffected, basis wording wrong.
- C phase 3 | 11-valuation.md Entity A Pillar 3 | 3b +0.5x growth premium awarded without citing the FTTCP B2 YES/NO flag while Entity A ROCE 13% is below required return 15.25%; if B2=NO, 3b zeros, additive raw 14.5x to 14.0x, within 1x.
- C phase 3 | 11-valuation.md Entity A Pillar 1 | ROCE 13% exceeds the 2 year evidenced range (about 9 to 12%), not reconciled to the 17.1 method; operator approved 14.5x limits decision impact.
- C phase 3 | 14-thesis.md Section 7 | Both Role 2 AVOID triggers fire (Gate 0 AVERAGE; Hurdle STOP); mechanical verdict AVOID, report emits WATCHLIST on operator DEEP WATCH disposition; no buy action identical, label does not follow the written rule; surfaced for human ruling.
- C phase 3 | 11-valuation.md Section 2 + FV path | Single forward column per entity, not Year-1-4 committed rows; FV path rolls a flat CAGR with no fade step down (Amdt 18.0/14).
- C phase 1 | 01-gate0.md line 55; B01-gate0.yaml | Gate 0 A1 median ROCE 11.96% scored 3; correct 10-14.9% band = 1; Block A 9 to 7, core 42 to 40, grand 46 to 44; still AVERAGE, no flip.
- C phase 1 | 01-gate0.md line 95; B01-gate0.yaml line 20 | Deal breaker 1 fires at corrected Block A=7 (<8); deal_breakers list empty; no outcome change but DB1 should be recorded.
- D | 06-peers.md Claim 7 peer evidence row | "120 million case market" quote cited as May 2026; verbatim quote is in GLOBUSSPR-Concall_Jan_2026 line 686; CONTRADICTED verdict still stands on three correctly anchored Globus quotes.
- D | 06-peers.md Claim 5 peer evidence row | "OMCs reducing volume offtake... not impacted" presented as same call as the May 2026 shift; the line is in GLOBUSSPR-Concall_Jan_2026 lines 628-629, about four months earlier; PARTIALLY VERIFIED verdict survives on independently correct anchors.

### MINOR

- A | 01-gate0.md Block A ROCE line 42-43 | PBT FY26 377.21 Cr (screener) with AR consolidated BS; basis/consolidation difference, permitted source, disclosed; reclassified CRITICAL to MINOR on orchestrator source verification. source_fidelity: false.
- A | 01-gate0.md Block A line 44-46 | Interest FY26 167.18 Cr (screener) versus AR consol finance costs 168.33 Cr; immaterial basis difference.
- A | 03-ardeep.md phase 2 rank 5 | CISCPL JV 100% basis profit about Rs 9,472.81 Lakh derived versus Board's Report Rs 9,462.60 Lakh; 0.11% precision gap, immaterial.
- B | B05 red_flags, Concall_Aug_2026 p3-8 | MISSED: Ennature intra-call revenue and EBITDA inconsistency (90 vs 83 Cr; +188% vs about +100%).
- B | B05 red_flags, Concall_Aug_2026 p14-15 | MISSED: spirits volume outgrew revenue, contradicting the premiumization thesis.
- B | B05 red_flags, Concall_Feb_2026 p11 | MISSED: Lululemon collaboration question left unanswered while LanzaTech was addressed.
- B | B05 red_flags, Concall_Aug_2026 p15 | MISSED: sequential EBITDA question deflected to email under analyst insistence.
- B | B05 repeated_evasions | OVERSTATED: segment debt deflection framed as Q3+Q4 every time; clear on-call deflection is Q4 only; Nov 2025 (unread by B05) answered it with a 600/800 split.
- B | B06 contradicted[] | OVERSTATED: UP market contradiction is reconcilable; IGL's 23-25 lakh is IMFL only and its own about 90 lakh IMIL figure sums to about 1.1 Cr, matching Globus's about 1 Cr.
- B | Concall_Jun_2026 p15 | OBSERVATION: 98 Cr silver sale (cost 51 Cr) kept off the P&L; disclosed and explained, neutral, a 47 Cr gross gap worth naming.
- C phase 3 | 11-valuation.md Section 4B | Entity B hurdle uses additive 19.5x versus governing RRM 16.6x; verdict STOP unchanged.
- C phase 3 | 11-valuation.md Entity A Track 1 | RRM arithmetic 11.5x versus 11.06x at r=15.25%; non governing.
- C phase 3 | 11-valuation.md Entity A divergence | Governing track additive 14.5x over RRM 11.5x via operator override; legitimate, flagged.
- C phase 1 | B07-emoat.yaml | capex_embedded_growth_pct=1 versus text about 1.2%; integer truncation, immaterial.
- C phase 1 | B07-emoat.yaml | Combined HIGH POTENTIAL on a STRENGTHENING (33) not EXPANSION (at or above 40) forward score; permissible judgment, flagged.
- D | 06-peers.md Part 2E | Supreme Court/BPCL ethanol tender stay attributed to both Jun and Jul 2026 Triveni calls; passage exists only in the 30-Jul call; item real, correctly anchored in that call.
- D | 06-peers.md Part 2C | Balrampur PLA capex INR 3,080 Cr attributed to the Aug 2026 call; figure is in the Jun 2026 call; two facts from two calls fused under one citation.

## Verifier counts

- A (B12a): 0 CRITICAL, 2 MAJOR, 5 MINOR; acceptance 89; source fidelity findings 0.
- B (B12b): 0 CRITICAL, 1 MAJOR, 7 MINOR; acceptance 62; 8 of 13 independent flags caught.
- C phase 1 (B12c-verifier-framework): 0 CRITICAL, 2 MAJOR, 2 MINOR; acceptance 96.
- C phase 3 (B12c-phase3-valuation): 1 CRITICAL (corrected), 6 MAJOR, 3 MINOR; valuation adherence 78.
- D (B12d): 0 CRITICAL, 2 MAJOR, 2 MINOR; acceptance 90; peer utilisation 100.
