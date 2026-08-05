# Verifier summary (phase 1)

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance |
|---|---|---|---|
| Numerical acceptance | 100 | A (B12a) | 100% (35/35 numbers) |
| Redflag coverage | 62 (binding) | B (B12b) | 62% |
| Framework adherence | 91 | C (B12c), Gate 0 + Emerging Moat | 91% (42/46 rules) |
| Peer utilisation | 93 | D (B12d) | 87% |
| Overall | 62 | min of four; band 60-74 | REWORK floor (<60) not breached |

Verifier A: 0 CRITICAL, 0 MAJOR, 0 MINOR. 35 numbers checked, all MATCHES; Verdict-card and Section 1B inputs 100% verified. No source fidelity findings, no REWORK trigger.

Verifier C scope here is the Gate 0 and Emerging Moat portion only; the valuation half (B10/B11) is deferred to phase 3.

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Note |
|---|---|---|
| C | B07 Section 5 (report lines 391-396) | Non framework +1.5 per category corroboration bump inflates em_score 9.1 to 15, flipping classification NONE to MODEST; fabricated scoring step with no framework basis. Corrected: em_score 9.1, classification NONE. |

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 2E / repeated_evasions (Aug-2025 p.6-7; Nov-2025 p.11-12) | The peer lag / is the model broken question was deflected in Q1 (Viraj Mehta) and Q2 (Mathur Rathi); B05 recorded repeated_evasions as empty because it excluded the Aug-2025 Q1 call. |
| B | B05 3A / competitive intelligence (Aug-2025 p.8, p.10) | In the same Q1 call management volunteered competitor price drops and Bangalore/South pricing pressure, contradicting the "unchanged competitive intensity" claim treated as a credibility positive. |
| C | B01 Block E / E4 (report line 131) | Contingent liability to net worth 26.17% sits in the 15-30 band (score 1); B01 assigned 3. Block E 2/20 not 4/20, Core 19 not 21. Classification AVOID unchanged. |
| C | B07 Section 6D (report lines 472-479) | combined_assessment TURNAROUND contradicts the 6D taxonomy; with the corrected NONE forward score the label is AVOID / not a transition setup. |
| D | Claim 6 capex/payback, Speciality breakeven | Nov-2025 Speciality call states breakeven of 6 to 9 months, not 3 to 6; the Nov figure was misattributed, understating disclosed breakeven variability. |
| D | Part 2E, Middle East / geopolitical cost pressure | The "pressure on suppliers with the geopolitical situation" quote is cited to Westlife Q1 FY27 (Jul-2026) but is from Westlife Q4 FY26 (May-2026); wrong quarter on a timeline sensitive claim. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 1B / 4D (Aug-2025 p.4) | Gross margin 67-68% band was also guided in Q1 FY26 (~68% annual); the span is four calls, not three, strengthening the reiterated but missed flag. |
| B | B05 2B / 2C accountability (Aug-2025 p.14 vs May-2026 p.7) | Q1 stated corporate cost "should not go beyond 5-6%"; the 7.1% resets the baseline above management's own historical normal, so the FY27 6.5% target is a partial return, not pure leverage upside. |
| C | B07 Section 5 scorecard (rows A4/D2/E1/H1) | Evidence multipliers 0.85 and 0.6 lie outside the framework's discrete {1.0, 0.7, 0.5} set; outcome remains below 12 under any strict reading. |
| C | B01 Block F / M12 (report line 179) | Negative working capital band on a 2 year straddling sample scored 3; a stricter reading gives 1, which would flip moat_class THIN to NONE. AVOID unchanged. |
| C | B01 Block B / B2 (report line 77) | FCF positive proportion scored 100% to 5 on a 2 of 10 year computable sample; applied as written and disclosed. Note only. |
| D | RBA Q3 FY26 wage code citation | INR 2.3 Cr wage code one off cited at p.6; content located at approximately p.8. Quote real, page imprecise. |
| D | Sapphire Q1 FY27 aggregator benign citation | "haven't heard about any heightened competition on these two aggregators" cited at p.7; content at approximately p.9. Quote real, page imprecise. |
| D | Westlife Q2 FY26 GST and Q1 FY27 first positive SSSG citations | GST 80-100bps quote at approximately p.6-7 not p.3; "first positive SSSG" at approximately p.3 not p.7; page references appear transposed. Quotes real. |
| D | Part 2E, wage code / minimum wage risk for Westlife | Minimum wage impact confirmed present (Westlife Q1 FY27, Jul-2026) but B06 gives no anchor for the specific sentence; unanchored but independently verifiable. |
