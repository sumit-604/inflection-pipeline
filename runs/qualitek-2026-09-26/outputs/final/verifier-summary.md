# Qualitek Labs Ltd (QUALITEK): verifier summary (Phase 1)

_Phase 1 verifiers only: A (numerical, B12a), B (red flag coverage, B12b), D (peer utilisation, B12d), and the Gate 0 plus Emerging Moat half of C (framework, B12c). Verifier C's valuation half (B10/B11) runs in phase 3. Verification cycle 2 of a one cycle correction cap. Findings sorted CRITICAL, then MAJOR, then MINOR._

## Phase 1 confidence delta

| Component | Verifier | Score | Acceptance basis |
|---|---|---|---|
| Numerical acceptance | A (B12a) | 100 | 45 of 45 checked figures clean, material universe 54 (83% coverage); cycle 1 48 of 48 |
| Red flag coverage | B (B12b) | 67 | 12 material items: 5 caught, 6 partially caught, 1 missed; declared rule CAUGHT = 1, PARTIAL = 0.5 gives 8/12; caught only 42%, partials as caught 92% |
| Framework adherence | C (B12c) | 90.3 | 56 of 62 rules passed: Gate 0 39 of 40, Emerging Moat 17 of 22; valuation half pending phase 3 |
| Peer utilisation | D (B12d) | 100 | 12 of 12 transcripts substantive, 0 unsupported, 0 verdict discipline fails |
| **Overall** | | **67** | Set by red flag coverage. Band 60 to 74. No CRITICAL anywhere; no acceptance rate below 60 on the number of record. REWORK not triggered; sensitivity ruling in gate-recommendation.md. |

## Findings by severity

### CRITICAL

None across all four verifiers, in either cycle.

### MAJOR (13)

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | B | B05 (all sections); announcements/20260829-71a8605c item 5; announcements/20260907-d2d6e19d | MISSED: managerial remuneration cap 28% to 35% of net profits proposed 29-Aug-2026, withdrawn 07-Sep-2026 with no reason. |
| 2 | B | B05 1C, 2D, 4D; presentation/20260520 p.2 l.97-103; AR2026 p.70 l.3236; AR2026 p.139 note (iv) l.6904-6906; results/20260520 note 6 | PARTIALLY CAUGHT: MD&A and AR call standalone growth organic, but standalone includes the Mumbai lab bought by slump sale w.e.f. 01-Sep-2025 for Rs 882.00 lakh. Mumbai revenue contribution NOT FOUND. B05 flags only the absence of an organic split, not the affirmative mislabel. |
| 3 | B | B05 2A row "2X Revenue" and 1C; presentation/20250530 p.9; presentation/20251114 p.2 l.66-67; presentation/20241114 p.8; presentation/20260520 p.2 l.75-79 | SPOT CHECK WRONG (magnitude): 2X is about 2.03x on the company's combined FY24 base of Rs 61.4 Cr, met not exceeded, not 4.27x, and includes Mumbai (and claimed Bengaluru). The company switches bases between halves; like for like FY26 growth on the FY25 walk through Rs 85.0 Cr is about 46.5%. |
| 4 | B | B05 2B excuse_pattern, 4D; AR2025 p.19 l.730-732; presentation/20260521 p.11; presentation/20250530 p.4 l.65 | PARTIALLY CAUGHT, misclassified: FY25 AR chairman calls FY25 results "well aligned" with targets while revenue missed Rs 90 Cr and PAT margin fell 15% to 11%, EBITDA margin 28% to 23%. Affirmative reframing, not silence. |
| 5 | B | B05 1A, 1C, 4A priority 2, 4D; presentation/20260520 p.3 l.135; AR2026 l.6858-6906, l.10075-10083; results/20260520 notes 5-8 | PARTIALLY CAUGHT: Bengaluru USFDA lab acquisition has no Reg 30 intimation and no entry in the audited acquisition notes, yet the FY26 MD&A says borrowings funded "the Mumbai and Bengaluru acquisitions". Price, date, seller, acquiring entity NOT FOUND. |
| 6 | B | B05 1A (QTIPL row), 2D; announcements/20240726-28ac1529 p.8-10; AR2026 p.140 note (iii) l.6894-6900; EGM notice 24-Sep-2026 l.701 | PARTIALLY CAUGHT: QTIPL bought for Rs 500 lakh cash from a promoter common group; software firm with FY24 turnover Rs 41.29 lakh, loss Rs 73.80 lakh; FY26 revenue Rs 37.63 lakh, loss Rs 24.94 lakh. Never discussed in MD&A, deck or AR. Only visible precursor to the new cybersecurity acquisition object. |
| 7 | B | B05 2D, 4D (net debt row); announcements/20251220-cccc69b5; announcements/20260603-77c97589; announcements/20250705-f894fb96; AR2026 p.83 l.3610; presentation/20260520 p.3 l.137-141 | PARTIALLY CAUGHT: financing never narrated against the "net debt/EBITDA ~3.0x will compress" claim: Rs 65 Cr secured NCD (share pledge, promoter guarantees, DSRA; no later outcome), HDFC Rs 91.31 Cr facilities 03-Jun-2026, Jul-2025 HDFC Rs 60 Cr and Kotak Rs 35.07 Cr. B05 caught only the Sep-2026 GCP raise. |
| 8 | C | 01-gate0.md Block A, A1 (line 35-36); prompts/01-gate-0-pipeline.md line 55 | Median ROCE 10.02% scored 3; the 10 to 14.9 band scores 1. Block A 8, core 46, grand 58. Classification AVERAGE unchanged. Deal breaker 1 sits exactly at its line (8, fires below 8). |
| 9 | C | 07-emoat.md A1 (line 72, 174) | Moat attribute (scarcity) is inference scored at the documented multiplier; 2.0 to 1.0. |
| 10 | C | 07-emoat.md E1 (line 95, 185) | First mover attribute is inference scored at the documented multiplier; 2.0 to 1.0. |
| 11 | C | 07-emoat.md H2 (line 111, 192); prompts/07-emerging-moat-pipeline.md line 30-33 | Deck only partner list with no contracts scored as documented; taxonomy says claim 0.7; 3.0 to 2.1. |
| 12 | C | 07-emoat.md Section 3 recount (line 149); B07 evidence_mix | Recount counts the USFDA lab three times and the 2018 PPP arrangement probably twice. MODEST survives at 12.5 but falls to NONE (11.5) if E1 is struck as duplicative. One improvement, one mechanism. |
| 13 | C | 07-emoat.md 2C (line 54-60); B07 capex_embedded_growth_pct 88; 01-gate0.md M3 line 151-152 | Uses announced, not under execution, capex and a single year consolidated net PPE turnover. B01's 0.72x FAT gives about 36%. A single basis value is NOT DETERMINABLE. Downstream should not consume 88. |

### MINOR (16)

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | B | B05 (absent); B06 2E bullet 2; announcements/20250329-bff730c8; announcements/20260209-7b6ff1b4; announcements/20260730-44102f7e | PARTIALLY CAUGHT: three company secretary exits in 16 months; the Jul-2026 exit reason differs within one filing. B06 notes the count; B05 omits it. |
| 2 | B | B05; announcements/20250829-7bef86ef; announcements/20260211-c303ae33 | MISSED: Reg 30 timeliness lapses. LabOps 74% bought 23-May-2025, intimated 29-Aug-2025; CS resignation letter 21-Nov-2025 disclosed 09-Feb-2026, drew a BSE observation. |
| 3 | B | B05 2A / grade reasoning; presentation/20251114 p.2 l.83-84; presentation/20260520 p.2 l.111 | PARTIALLY CAUGHT positive: H1 FY26 MD&A promised better operating leverage from H2 FY26; EBITDA margin went 20.7% H1 to 25.7% H2. Not recorded as delivered; the symmetric bar requires it. |
| 4 | B | B05 2C Over promotion; presentation/20250530 p.9; AR2025 p.15 l.787-788 | OVERSTATED: "Rs 125 Cr commitment does not exist"; 2X on the combined FY24 base of Rs 61.4 Cr implies about Rs 122.8 Cr. |
| 5 | B | B05 1B (PAT 14-15% row); AR2026 l.707 [page 23], l.757, l.760 [page 24] | Anchor slip: line 757 sits on PDF page 23 (printed p.18), not p.24. |
| 6 | B | B06 Q1, Part 4; KRSNAA Nov-2025 l.304; May-2026 l.379, l.495-500, l.1103 | OVERSTATED: Krsnaa "124-155 days across four consecutive quarters"; day counts in 2 of 4 calls; 124 not found. |
| 7 | B | B06 Q6; METROPOLIS Sep-2026 l.617-624; May-2026 l.310, l.441 | Metropolis 24.4% (reported) and 25.9% (organic) are the same year, not an FY26 move; organic expansion about 140bps. Missed contrast: Metropolis separates organic from acquired margin; Qualitek never does. |
| 8 | B | B06 Q4, 2D; VIMTALABS Jul-2026 l.1198-1221; Feb-2026 l.865-895 | Vimta 4.5% is said of the "electronics industry"; same passage gives 8-11% for testing markets. Vimta "filled a gap" in Hyderabad defence EMI/EMC and says customers will not ship from Pune: an incumbency read that B06 frames as mild support. |
| 9 | C | 01-gate0.md E2 | Window labelled "~3 years" is Mar-2024 to Mar-2026, 2 years. Score 0 unaffected. |
| 10 | C | 01-gate0.md M11 | Prior window is FY21 to FY23 (2 years), not 3. Fallback also scores 0. Score unaffected. |
| 11 | C | 01-gate0.md FY24 CFO (line 59) | Base row called "WC adjusted operating profit" in the report and "before WC changes" in the data note. If pre WC, it is not CFO. B1 holds at 5 unless true FY24 CFO is below Rs 354.79 lakh. Referred to Verifier A. |
| 12 | C | 01-gate0.md A3 | ROE formula has no use source exception; FY21-23 prospectus ROE taken as source, FY24 computed. Mixed basis; 2 points at stake. |
| 13 | C | 01-gate0.md M1 | FY26 EBITDA computed from PBT (includes other income); FY21 from the prospectus line. M1 5 survives unless the gap exceeds about 6pp. |
| 14 | C | 01-gate0.md Block D / analyst_note vs 07-emoat.md G1 | B01 scores standalone D/E 0.45 and reads it as low leverage; B07 cites consolidated 1.25. On 1.25, D3 scores 1 (core 43, still AVERAGE). Carry the basis gap; do not read 0.45 as group leverage. |
| 15 | C | 07-emoat.md line 80 (B2) | Stray non English token in prose; "renewable" contract claim is inference, not in the cited Reg 30 terms. |
| 16 | D | B06 Part 2E, attrition bullet; VIMTALABS-Concall_May_2026_Transcript.txt l.222 | A second, later Vimta attrition mention makes the same point and is not cited. Reinforcement miss, no verdict change. source_fidelity: false. |

### Further items Verifier B listed as MISSED (MINOR, verification only)

| Verifier | Location anchor | Note |
|---|---|---|
| B | presentation/20260521 p.7-8; presentation/20260520 p.2 l.61; AR2026 p.139 note (i); announcements/20250705-f894fb96 p.1 l.24 | Consolidation start date misstated: deck and MD&A say consolidation from H1 FY26, audited ITCPL subsidiary w.e.f. 11-Sep-2024; Jul-2025 Reg 30 still calls ITCPL an associate/group company. |
| B | presentation/20260520 p.2 l.93; presentation/20260521 p.24 | "Asset light economics" claim against FY26 capex Rs 51.3 Cr (about 41% of revenue) and Rs 63 Cr FY27 plan. |
| B | announcements/20240726-28ac1529 p.8 item f; results/20260520 note 5; presentation/20241114 p.2 | ITCPL acquisition promised complete by 30-Sep-2024; swap leg completed 10-Sep-2025, about 11 months late. |
| B | announcements/20250829-7bef86ef p.1 l.109-110, Annexure C item b | LabOps shares bought from Mr. Kishan Chand Grover; promoter WTD is Mr. Kamal Grover; filing says not a related party; relationship NOT FOUND. |
| B | results/20260520 note 9; AR2025 p.21 l.817; presentation/20260520 p.3 l.183 | Single geographic segment "Within India" against the claimed domestic/international balance and the 30% overseas by FY31 target. |
| B | VIMTALABS-Concall_Jul_2026 l.1198-1200 | B06 does not use Vimta's 8-11% testing market growth statement from the same passage as the 4.5% figure. |

### Verifier A (source fidelity)

0 findings in cycle 2 (45 of 45 figures, 54 material, all sources re-read, no ANCHOR NOT FOUND, no UNANCHORED). 0 findings in cycle 1 (48 of 48). Source fidelity gate clear.

## Correction history, cycle 1 to cycle 2

| Verifier | Cycle 1 | Action | Cycle 2 |
|---|---|---|---|
| A | 48 of 48 clean, 0 findings | re-run fresh | 45 of 45 clean, 0 findings |
| B | 43% (7 material: 3 caught, 1 partial, 3 missed; 6 MAJOR, 12 MINOR). REWORK trigger. | stages 5 and 6 reworked from source; B re-run fresh | 67% (12 material: 5 caught, 6 partial, 1 missed; 7 MAJOR, 8 MINOR) |
| C | Gate 0 + EM audit | not re-run: its scope (B01, B07) did not change | 90.3 carried (6 MAJOR, 7 MINOR) |
| D | 100% substantive; 3 MAJOR, 2 MINOR, 1 verdict discipline fail | re-run fresh | 100%; 0 MAJOR, 1 MINOR, 0 verdict discipline fails |

What the cycle 1 findings changed:

- FY25 revenue miss corrected from about 22% to about 5.6% like for like; the Rs 90 Cr projection sat on a pro forma basis that the FY25 deck walks to Rs 85.0 Cr.
- The 30% EBITDA ambition corrected from "stated twice, diluted to 25-27%" to "stated once, redated, then dropped".
- Two missed MAJORs added to stage 5: three FY31/FY32 targets dropped between the May-2026 MD&A and the Sep-2026 AR (earlier misattributed to the AR), and the Sep-2026 raise with Rs 22 Cr for unidentified acquisitions including cybersecurity, Hyderabad unnamed.
- USFDA lab contradiction re-anchored to MD&A 20-May-2026 against deck 21-May-2026.
- Stage 6: Vimta electronics, EMI/EMC and defence overlap added (cycle 1 said no peer operates in the segment); debtor days verdict cut from VERIFIED to PARTIALLY VERIFIED (one peer); Krsnaa 150 day quote moved to the Nov-2025 call; Metropolis acquisition multiple quote moved to the 05-Aug-2026 call; Vimta CAGR corrected to 7.5% to 9%; attrition and geopolitical "total absence" claims withdrawn.
- Cycle 2 Verifier B concurred with credibility grade C in both cycles.

## Verifier disagreement log

none. Verifier A logged no finding in either cycle, so no downstream step leaned on a flagged number, kept a flagged figure, or cleared a flag by re-check. No verifier-disagreement-log.md was written.
