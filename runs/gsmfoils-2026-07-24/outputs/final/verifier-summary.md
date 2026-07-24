# Verifier summary (phase 1)

## Confidence delta and acceptance rates

| Verifier | Scope | Acceptance | CRITICAL | MAJOR | MINOR |
| --- | --- | --- | --- | --- | --- |
| A (B12a) | Numerical, 91 numbers checked | 100% | 0 | 0 | 0 |
| B (B12b) | Red flag coverage, 18 independent flags | 72% | 0 | 1 | 3 |
| C (B12c) | Framework, Gate 0 + Emerging Moat (phase 1) | 96% | 0 | 0 | 2 |
| D (B12d) | Peer utilisation, 12 transcripts | 92% | 0 | 1 | 2 |

Overall phase 1 confidence 72 (min of the four, redflag bound). Band 60 to 74. Valuation framework adherence deferred to phase 3. REWORK not triggered: Verifier A source fidelity clean, no acceptance below 60.

Two MAJORs, both carried, neither flips a verdict:
- B12b MAJOR, earnings quality: the historical 7 to 11.5 percent EBITDA margin build is partly cyclical aluminium inventory gain that reverses on a downcycle; B05 treated aluminium only as a Q4 compression excuse, never as an earnings quality flag on the margin the valuation extrapolates. Carry to phase 3.
- B12d MAJOR, source fidelity of a peer quote: B06 Claim 2a spliced a fabricated CGRAPHICS Mar 2026 quote fragment not present in any CGRAPHICS transcript; the PARTIALLY VERIFIED verdict holds on the real quotes, but the fabricated fragment must be struck from B06.

## All findings sorted by severity

| Severity | Verifier | Location | Note |
| --- | --- | --- | --- |
| MAJOR | B | B05 Sec 2B / 4D red_flags | Earnings quality flag missing: margin expansion partly cyclical inventory gain on aluminium, reverses on downcycle, not flagged. Anchor: Nov 2025 call p8/p10; Apr 2026 call p11. |
| MAJOR | D | 06-peers.md Claim 2a, CGRAPHICS Mar 2026 citation | Fabricated quote fragment ("first or the second of each month... based on the Hindalco letters") not present in any CGRAPHICS transcript, spliced beside a real quote from the same speaker/call; must be struck. Does not flip Claim 2a PARTIALLY VERIFIED. |
| MINOR | B | B05 Sec 2B/3C/4D | Employee cost YoY near halving (Rs 10.8 Cr to Rs 6.9 Cr) rated Low-Medium; margin flattering "directors' salary not taken" thread under weighted. Anchor: Apr 2026 Subhanu Bangal p6. |
| MINOR | B | B05 Sec 1B/2C consistency | Within call diverging figures to different analysts (Feb 2026: Ahmedabad Rs 10-12 vs Rs 12-15 Cr; Vasai Rs 25-28 vs Rs 28-30 Cr; Ahmedabad full Rs 25-27 vs Rs 28-30 Cr) not surfaced. Anchor: Feb 2026 p4/p6/p10/p12. |
| MINOR | B | B05 Sec 3D | 2x capacity add with zero order visibility / no contracts noted structurally but not weighted as a demand risk. Anchor: Apr 2026 Atharva Kulkarni p12. |
| MINOR | C | B01 Block A / A1 | Median ROCE on 2 clean years excludes bounded FY26; conservative low bound inclusion gives A1=4 not 5, Block A 19 not 20, Core 57. No decision impact, still AVERAGE then AVOID. |
| MINOR | C | B07 Section 6D combined_reasoning | AVOID floor attributed to mechanical cash/data failures when the substantive cap is AVERAGE and AVOID comes from the LIMITED history downgrade; outcome unaffected, forward em_score 4.8 (NONE) blocks any transition class. |
| MINOR | D | 06-peers.md Claim 3, CGRAPHICS May 2026 citation | Cited passage gives the ~8,000-9,000 ton figure but no competitor name ("I Get") present in the transcript at that point. Does not change Claim 3 UNVERIFIABLE. |
| MINOR | D | 06-peers.md Claim 1, CGRAPHICS Nov/Dec 2025 citation | Rs 1,000 Cr Wahren guidance is real but first appears in the May 2026 call, not Nov/Dec 2025; single citation covers two figures from two quarters without disambiguation. Both figures genuinely peer sourced. |

Verifier A: 91 numbers traced to primary sources (screener CSV, AR extracts, AR images, concall confirmations); zero mismatches, zero anchoring gaps, zero unit or basis errors.
