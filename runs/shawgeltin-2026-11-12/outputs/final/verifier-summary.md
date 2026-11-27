# Narmada Gelatines Ltd (SHAWGELTIN): Phase 1 verifier summary

Run 2026-11-12. Verifiers A, B and D in full, and the Gate 0 plus Emerging Moat half of verifier C. The valuation half of C is pending Phase 3. Units: AR and results in ₹ lakh; CARE and screener in ₹ crore.

## Phase 1 confidence delta

| Component | Value | Verifier | Basis |
|---|---|---|---|
| numerical_acceptance | 99.0% | A (B12a) | 768 numbers checked; mandatory tier 348 of 348 (OR-32); material universe about 680, about 420 sampled |
| redflag_coverage | 80% | B (B12b) | material_caught 4 / material_found 5 (partial counted as caught); strict 3 of 5 = 60% |
| framework_adherence | 85.3% | C (B12c, phase 1 half) | 87 of 102 rules: Gate 0 54/59 = 91.5%, Emerging Moat 33/43 = 76.7% |
| peer_utilisation | NOT APPLICABLE | D (B12d) | 1 of 3 peers substantive (NATCAPSUQ); denominator 3 < 4. D's own acceptance rate 100% |
| overall | 80 | orchestrator (confidence.yaml) | min of applicable; set by redflag_coverage; band 75 to 89, normal |

REWORK triggers: Verifier A confirmed CRITICAL 0; any acceptance rate below 60% on a denominator of 4 or more: none. Verdict: no REWORK. Remediation cycles 0. Verifier runs A 1, B 1, C 1, D 1.

Counts: CRITICAL 0. MAJOR 10 (A 6, B 2, C 2, D 0). MINOR 25 (A 2, B 10, C 10, D 3).

## Findings, sorted by severity

### CRITICAL

None from any verifier.

### MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A | 03-ardeep.md Phase 3B balance sheet line, assets breakdown | Claimed "loans and other financial 184.88". Source: 183.88 = Loans 20.58 + Other financial assets 163.30 (AR balance sheet PDF p.49 / printed 46; Notes 7, 8 PDF p.62). Arithmetic slip of 1.00 in a derived sub-total; not a verdict card or pillar input. source_fidelity: true |
| 2 | A | 02-notes-pass1.md section 11, employee benefits bullet | Claimed -273.33. Source: -272.33 = (1,147.35 - 1,360.72) + (145.10 - 204.06) (Note 30, AR PDF p.69 / printed 66). Arithmetic slip of 1.00; inputs and totals match. source_fidelity: true |
| 3 | A | 02-notes-pass1.md section 8, Pioneer Jellice bullet | Claimed payable 83.53 is 6.8% of creditors other than MSME (758.22). Source: 83.53 / 758.22 = 11.0%; 6.8% is the share of total trade payables 1,235.40 (Note 22 PDF p.67; Note 37 PDF p.73). Wrong denominator. source_fidelity: true |
| 4 | A | 03-ardeep.md Phase 3A, CFO quality checks, first bullet | Claimed CFO about 2,267, FCF about 1,431 after removing advances 135.18 and capex payable 53.07. Source: CFO 2,267.42 ties; FCF on the same basis 1,295.71; 1,431 is reported FCF 1,483.96 less 53.07 only (cash flow AR PDF p.51 / printed 48). Sits inside a mild FLAG-CASH narrative, not a verdict input. source_fidelity: true |
| 5 | A | 02-notes-pass1.md section 2, related party table, sitting fees FY25 | Claimed 8.36. Source: Note 37 FY25 fees sum 8.40 (AR PDF p.73 / printed 70); Note 33 prints 8.66 (PDF p.69); 8.36 appears nowhere. Stray typo. source_fidelity: true |
| 6 | A | 08-promoter.md section 3D and adverse finding 6 (AGM bullet) | Claimed "1 against in one resolution". Source: 59,267 shares and 3.9197% match; 1 share against on each of 5 resolution tallies (20260819-scrutinizer.txt lines 247, 307, 357, 405, 456). Count of resolutions wrong. source_fidelity: true |
| 7 | B | B05 1C, B05 timeline_slippages, B05 2A row 7 | MISSED. Capex plan reset: CARE Apr-2025 p.2 (₹33.30 Cr over FY25-FY26 incl. 2.15 MW solar, term loan ₹18 Cr) vs CARE 06-Mar-2026 p.2 (₹33.00 Cr excl. solar, term loan ₹25 Cr, production Jan-2027); solar ₹8.89 Cr (AR p.19); term loan 798.08 to 728.65 lakh (Note 18 AR p.65); AR Note 4 (p.61) says no time delay. Source in inputs/other/, outside stage 5's dispatch: a routing gap. Carry to Halt 1 |
| 8 | B | B05 2A row 3 and 4D; B06 analyst_note reading (b) | PARTIALLY CAUGHT. CARE 06-Mar-2026 p.2 "has started importing some part of its raw material requirement"; AR p.11 import "is being utilized"; AR p.19 forex outgo shows no raw material; AR Note 43 p.77 domestic sourcing, no foreign currency exposure. FY26 cost relief cannot rest on imported bone. Separating observation: raw material line in FY27 AR forex outgo, or a rise in Note 37 purchases |
| 9 | C | F-G0-1, B01 rule G0-54 (B01-gate0.yaml L35; 01-gate0.md L77) | block_b_trend CFO/EBITDA 79% vs 92% and label "stable" not reproducible from the report's own rows (FY26 25/41 = 61%; FY25 69%); 3-yr vs 12-yr reads improving, FY25 to FY26 reads deteriorating, neither shows stable. No score change; field feeds FLAG-CASH. Restate or relabel |
| 10 | C | F-EM-1, B07 rule EM-11 (07-emoat.md L64, L99) | F2 tiered as claim with no concall or presentation source. F2 documented gives 12.0 = MODEST; F2 inference gives 11.5 = NONE. em_classification flips on the tier alone. Phase 3 re-grades to CRITICAL if the NONE/MODEST reading moves destination PE by more than 1x |

### MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 11 | A | 01-gate0.md E4 anchor | 244.64 lakh contingent liabilities is in Note 36 on printed p.69 (PDF p.72), not printed p.68. Number and note correct; re-anchor. source_fidelity: true |
| 12 | A | 06-peers.md section 2D | ACG 45-50% share cited to Q2 FY26 p.12; the 45-50% leader share is on Q2 FY26 [page 11], leader unnamed there; ACG "almost closing 50%" is Q4 FY25 [page 10]. Weak anchor, non-material. source_fidelity: true |
| 13 | B | B05 block red_flags[1], input_gaps[3], 4D row 2 | OVERSTATED clause. The company filed the CARE release with the capex paragraph on BSE itself (announcements/20260306-credit-rating.txt p.1-3). Core flag stands: AR, three results filings and AGM record carry no capex word |
| 14 | B | B05 2A row 7, 4A trigger 1 | CWIP plus commitments 1,723.03 lakh = 52% of ₹33 Cr is arithmetically correct, but Mar-2025 sum was 1,933.03 lakh (Note 4 AR p.61, Note 35 AR p.72); reading it as project progress is not supported |
| 15 | B | B05 (absent); route B08 | MISSED. MD aged 79, 2-year term to 31-May-2028, overall in charge of all operations, no successor named (Q4 FY26 filing PDF p.17; AR p.7) |
| 16 | B | B05 2E | MISSED. AGM 19-Aug-2026 held a members' question session; MD/CFO responded; content unrecorded; video-recorded and webcast on CDSL (announcements/20260819-agm-outcome.txt p.3, p.6). Request the recording at Halt 1 |
| 17 | B | B05 (absent); route B08 | MISSED. MD bonus ₹5 lakh at annual "Operating EBITDA" of ₹25 Cr plus 1% above it (AGM notice PDF p.14); metric undefined; threshold below FY26 level |
| 18 | B | B05 4C reporting accuracy | MISSED. Board's Report p.6 points to the CG Report for key risks; CG Report p.32 names none. Fifth instance of the pattern |
| 19 | B | B05 4C reporting accuracy | MISSED. Note 48 p.79: Debt-Equity 0.11 to 0.06 and DSCR 3.33 to 7.71 printed "100%" variance, no reason given. Sixth instance |
| 20 | B | B05 2D, 3A | PARTIALLY CAUGHT. MD&A silent on the group's role in procurement; Pioneer Jellice purchases 1,481.92 lakh (FY25 1,524.64), new consultancy 24.00 and lease 11.60 (Note 37 AR p.72-73); IGCL carrying 4,115.31 vs attributable net worth 2,737.02 (AOC-1 AR p.21). Channel flat year on year, cannot explain the 511 bp |
| 21 | B | B06 Q5, risks_peers_raise[0] | PARTIALLY CAUGHT. NATCAPSUQ Q2 FY26 p.11 "one larger gelatine company acquired two others"; [INFERENCE] fits NGL's own promoter group (CARE 2026 p.1). Buyer's 18-20% duty-free import access counters the consolidation |
| 22 | B | B05 3B; B06 analyst_note | MISSED, out-of-list source. CARE Apr-2025 p.2: bone prices "expected to decrease in FY26" on reduced European bone gelatine output, "with manufacturers likely to import raw materials"; synergy wording moved from procurement bargaining power (2025) to technical expertise and export access (2026 p.1). Supports the cyclical reading; not the separating observation |
| 23 | C | F-G0-2, B01 rule G0-06 (01-gate0.md L78; B01-gate0.yaml L27, L36) | Inventory 156 days labelled sales basis implies ₹91.9 Cr inventory, above FY26 total current assets ₹85.05 Cr; B07 G2 labels it on cost. B4 = 5 and M12 = 0 hold. Correct the label before stage 11 |
| 24 | C | F-G0-3, B01 rule G0-02 (01-gate0.md L57) | M3 FAT denominator 41 equals the EBITDA figure, not named as net block; FY26 gross block ₹53.2 Cr gives FAT at least 4.04x, M3 = 5 holds. Weak anchor |
| 25 | C | F-G0-4, B01 rules G0-57, G0-58 (01-gate0.md L52-68, L84-110) | No moat profile bars; report closing YAML abridged. Block file complete. Presentational |
| 26 | C | F-EM-2, B07 rule EM-12 (07-emoat.md L53, L67, L68) | Mixed-tier weight convention not uniform: per-item gives 13.1 = MODEST; weakest-link gives 10.5 = NONE. Rubric silent; operator ruling recommended |
| 27 | C | F-EM-3, B07 rule EM-20 (07-emoat.md L56, L113) | B2 scored MM but the report calls certifications existing, table stakes, copyable; at LM total 10.7 = NONE. Counterweight to F-EM-1 |
| 28 | C | F-EM-4, B07 rule EM-07 (B07-emoat.yaml L26) | capex_embedded_growth_pct 22 is the capacity cross-check, not the 2C formula output (69.1%; 36.1% on spent or contracted). Label both for stage 11 |
| 29 | C | F-EM-5, B07 rule EM-28 (07-emoat.md L71) | I2 answered for 3 of 9 scored categories; C1 not tested. I2 = 0 likely holds |
| 30 | C | F-EM-6, B07 rule EM-31 (07-emoat.md L127-134) | Optionality register omits H1 (inference only) and F2. Monitoring gap; add H1 |
| 31 | C | F-EM-7, B07 rule EM-13 (07-emoat.md L24-25, L55, L65, L66, L163) | Anchors cite stage blocks or note numbers without page. Weak anchors |
| 32 | C | F-EM-8, B07 rules EM-24, EM-36, EM-43 (07-emoat.md L120-121, L166-174, L178-191) | Scorecard groups 14 zero rows into 2; 6E map omits families D and I; closing YAML abridged. Presentational |
| 33 | D | B06 Q1; NATCAPSUQ-concall-Q2FY26-2025-11 p.11 (txt line 397) | B06 omits the "last six quarters" duration of gelatine price softening from the quoted answer |
| 34 | D | B06 risks; NATCAPSUQ Q4 FY26 p.20 (txt line 788) | 50% US tariff / HPMC slump cited to p.21; tariff text sits on p.20. Cold-shelf quote on p.21 is correct |
| 35 | D | B06 Part 3 vs Parts 4 and 5 | NITTAGELA marked UNUSED yet its screening OPM is used; label inconsistency only |

## Verifier notes carried as written

- A, coverage shortfall: stage 8 facts from SEBI documents not among A's inputs (NGL DLOF 19-Jun-2023, IGCL DPS 12-Dec-2024, IGCL post-offer ad 17-Apr-2025) were not checked: SPA date and price Rs 408.90, 39.42%, 27,95,932 shares, Rs 114.3 Cr, bulk-deal price Rs 408.8637, promoter 46.98%, combined 61.12%, brief 53.56%, shareholder tables. The AR corroborates only the 14.14% stake, 1,003,000 shares, 4,115.31 lakh cost and the 05-12-2024 date (consol Note 1, PDF p.89). Stage 9 web inputs unchecked; stage 9 arithmetic ties.
- A, struck at self-check (5): MD&A materials "increased 1.29%", EBITDA 40.88 Cr and growth rates, Annexure IV pay figures (all faithfully transcribed anomalies); OCR corrections 1,477.61, 553.99, 15.26 (reports right); M11 12.6% vs 12.54% (rounding).
- B, coverage basis: 5 material (all MAJOR) of 15 listed; 3 caught, 1 partially caught, 1 missed. Promise-delivery spot checks 5 of 5 confirmed. Credibility grade C: concur.
- C, Gate 0 boundary: core 60 is the exact floor of GOOD; E2 strict reading gives 59 = AVERAGE plus FLAG-GATE0. Operator may rule on E2.
- C, Emerging Moat band: em_score 11.7 is not stable at NONE (12.0 or 13.1 MODEST; 10.5 or 10.7 NONE by convention). Phase 3 Pillar 3 audit must carry both readings.
- D: claims all addressed; no verdict discipline fails; NATCAPSUQ 3 call rows confirmed substantive.

Verifier A disagreement set, Phase 1: none. No downstream step kept, re-derived from or cleared a figure Verifier A flagged; the synthesis files carry the corrected values only.
