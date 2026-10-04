# KWICK verifier summary, Phase 1 (run 2026-10-04)

## Confidence delta (phase 1)

| Component | Value | Basis | Block |
|---|---|---|---|
| numerical_acceptance | 96 | 227 clean of 236 checked; material universe 410 | B12a |
| redflag_coverage | 66.7 | 10 of 15 material (CRITICAL + MAJOR) fully caught; 93.3 if 4 partials counted | B12b |
| framework_adherence | 90.6 | 58 of 64 rules: Gate 0 41, Emerging Moat 23; valuation portion PENDING PHASE 3 | B12c |
| peer_utilisation | 100 | 11 of 11 peer transcripts SUBSTANTIVE | B12d |
| overall | 66.7 | set by redflag_coverage; not_applicable: none; band 60-74 (PROCEED verdicts downgrade one level) | confidence.yaml |

Acceptance rates: Verifier A 96 (Sonnet, fresh context). Verifier B 66.7 (Opus). Verifier C 90.6 on the Gate 0 and Emerging Moat portion only (Opus). Verifier D 100 (Sonnet).
REWORK: not triggered. No CONFIRMED CRITICAL in B12a; no acceptance rate below 60% on a denominator of 4 or more (OR-29). Verifier A identity check: no CRITICAL rows, nothing struck.
Source fidelity open: 1 MAJOR (Verifier A finding 1). Values correct; anchors corrected to p.150 / p.24 / p.264 wherever the figures are used.
Severity totals: CRITICAL 0. MAJOR 9 (A 1, B 5, C 2, D 1). MINOR 22 (A 6, B 6, C 4, D 6).

## Findings, sorted by severity

### CRITICAL

None filed by any verifier.

### MAJOR

| # | Verifier | Location anchor | Note (as filed) | Source fidelity |
|---|---|---|---|---|
| 1 | A | 09-tam.md Section 2 Method 2 (kit value per vehicle) and 3B/4 citations "prospectus p.265" | Claimed: Rs 2,035.74 lakh / 95 vehicles = Rs 21.43 lakh, Mobile CSI Rs 16.41 Cr to Rs 10.57 Cr, revenue growth 115% FY25, all cited p.265. Source truth: p.265 holds none of the three. 2,035.74 is on p.150; Mobile CSI 405.09 / 1,640.66 / 1,056.76 on p.24 and p.150; 115% on p.264. ANCHOR NOT FOUND at the cited page for a load-bearing SOM input. Values correct. Re-anchor to p.150 / p.24 / p.264 | true |
| 2 | B | B05 LBF-1, 2D, 3C, input_gaps | Missed filed evidence narrowing LBF-1: kit revenue = Top Customers 2+4 (Rs 1,201.40 + 834.35 = 2,035.75 lakh vs 2,035.74), matching MH (1,204.55) and RJ (834.42) state totals; p.140 end-client pre-dispatch inspection. B05 states no separator exists in the filings. Government share re-attributed about 74.5% vs 55.22% printed. Anchor: prospectus p.160, p.159, p.150, p.140 | n/a |
| 3 | B | B05 2B, LBF-3 | Payables fall explained as voluntary for better pricing and cash discounts (p.91, p.94) and as supplier-forced with limited bargaining power (p.96, p.98); gross margin fell 4.09 points. B05 records only p.98 as external-blame. Anchor: prospectus p.91, p.94, p.96, p.98, p.257 | n/a |
| 4 | B | B05 trigger 6 kill signal, timeline_slippages, 2D | Related-party software purchase from group entity Gostocks Fintech (Rs 58.70 lakh FY25, Rs 20.00 lakh FY26) behind an in-house, 100% Made in India E-Forensics claim is not surfaced; B05 phrase "related-group vendor" is unanchored. Anchor: prospectus p.250 related-party schedule, p.151, p.213-214; Deck p.12, p.19 | n/a |
| 5 | B | B05 1B INFERENCE 3, analyst_note, notes for later stages | "Only forward revenue evidence" overstated: p.96 ties the +31.1% receivables build to projected revenue growth; Stage 11 needs three forward readings (+18-23%, about +31%, +40%) with the H1 FY27 separator. Anchor: prospectus p.96, p.95, p.90 | n/a |
| 6 | B | B06 Q3 verdict and net read, B06 input_gaps; B05 2A row 2b label | Gross margin mislabelled "on COGS"; 27.06% is on revenue (p.257). B06 conversion to 21.3% and "inside the peer resale band" are inverted: Kwick sits above ADSL hardware-only single digits and DSSL 12-18%. Mechanism verdict stands; range verdict does not. Anchor: prospectus p.257, p.24; ADSL Feb-2026 [page 13]; DSSL Jun-2026 [page 8], [page 11] | n/a |
| 7 | C | 01-gate0.md Block B (B4), Section 3 classification box; B01-gate0.yaml flags[0], blocks.B (G0-1) | B4 scored on an FY24 start (B4 = 5, Block B = 8, DB2 not triggered, uncapped GOOD+). On the FY21-FY26 window used for A4, C1-C4, M1 and M10, B4 <= 1, Block B <= 4, DB2 triggers (max GOOD); uncapped result is GOOD, not GOOD+. Final AVERAGE unchanged (DB4). Window dependence not disclosed | n/a |
| 8 | C | 07-emoat.md Section 5 row 15 (F2); B07-emoat.yaml em_score, em_classification (EM-1) | F2 adjusted with an off-rubric 0.7x "mixed" multiplier (raw 2 to 1.4). Rubric allows 1.0 / 0.7 / 0.5 by evidence type only. Documented reading: F2 2.0, total 12.2 = MODEST. Inference reading: F2 1.0, total 11.2 = NONE. Filed 11.6 NONE. The band flips on the reading. No reading reaches the EM >= 25 UA qualifier or EXPANSION; 6D AVERAGE stands | n/a |
| 9 | D | B06 Part 1 Q3; DSSL Jun-2026 p.11; ADSL Feb-2026 p.23 (F1) | Q3 verdict VERIFIED overstates; should be PARTIALLY VERIFIED. Margin-band leg has three peer anchors; the mix-compression leg rests on ADSL alone (analyst-led). DSSL management attributes its 18% to 14% fall to component cost, not mix. Zen is own IP and only sets the ceiling | n/a |

### MINOR

| # | Verifier | Location anchor | Note (as filed) | Source fidelity |
|---|---|---|---|---|
| 10 | A | 01-gate0.md LBF-2 bullet 3 | Claimed the prospectus does not state that debtor days use average receivables. p.245 (txt L15281) prints "Trade receivables Turnover Ratio (Average Receivables days) = 365 / (Net Revenue / Average Trade receivables)". The p.91 table carries no "average" wording. All numbers correct; only the statement about the filing is wrong | true |
| 11 | A | 08-promoter.md 3D item 1 (deck PBT) | Deck PBT 1,921.45 is on [page 20], not p.19. Value correct | true |
| 12 | A | 08-promoter.md 3D timeline; 05-concall.md LBF-4 | "No UPSI was shared" is in the 30-Sep outcome announcement (20260930-b0992b12 line 31), and "Wednesday, 30th" in the 24-Sep intimation (20260924-9a7d0634 line 28), not in the deck. No number involved | true |
| 13 | A | 02-notes.md Section B provisioning row; 02-notes-pass1.md ageing table and revenue details | Gross receivables FY26 printed 2,320.01 (L14653), not 2,320.02; Mobile CSI FY24 printed 405.09 (p.24, L1429), not 405.08. 0.01 lakh. Stage 03 correct | true |
| 14 | A | 06-peers.md Q1, Q7, Q8 page anchors | ADSL 10% threshold is on [page 23], not 24; DSSL PPE Rs 8 Cr to 68 Cr and net debt Rs 68 Cr on [page 5], not 4; "Rs 36-odd crore ECL" is in the May-2026 (Q4 FY26) transcript [page 13], not Q3 [page 16]. Values exist; no verdict moves | true |
| 15 | A | 08-promoter.md 3A finding 2 | 7,998.16 labelled "purchases" is the P&L Cost of Materials Consumed (p.227); Note II.3 Purchases is 7,446.06. Basis unlabelled against stage 03; immaterial | false |
| 16 | B | B05 2A row 5, promise_delivery row 6 | Caveat that repayment came from cash held is not supported: FY26 cash rose 1,206.79 to 1,316.32 lakh; CFO 762.30 covered investing 273.17 and financing 379.60. Verdict DELIVERED stands. Anchor: prospectus p.268; Deck p.20 | n/a |
| 17 | B | B05 LBF-2 | FY24 83 days is testable: opening receivables 180.79 lakh from p.93; average basis gives 83.1, so 3 of 3 years reproduce. Anchor: prospectus p.93, p.91 | n/a |
| 18 | B | B05 2A row 2a | Domestic sourcing scored DELIVERED in form only; channel-partner awards and foreign-OEM range suggest imported goods bought from Indian entities [INFERENCE]; separator Top Supplier 1 identity. Anchor: prospectus p.146-149, p.153, p.161 | n/a |
| 19 | B | B05 overall | Six minor items missed (R16 to R20, R23): KMP pay, Jan-2026 plan attribution, pre-listing share transfers, RF15 heading, deck tenure and partnership claims, mid-FY25 dealer-shift date. Anchor: prospectus p.266-267, p.265, p.34, p.33, p.27, p.140; Deck p.5-6 | n/a |
| 20 | B | B06 Part 1 Q4 and Part 4 vs flags | Peer Q4 range stated as 26-34% in text and 26-33% in the flag | n/a |
| 21 | B | B05 FLAG-CHANNEL-OMISSION | "Explained only in business strategy p.150" is imprecise; p.140 also describes the channel and dates it from mid-FY25. Anchor: prospectus p.140 | n/a |
| 22 | C | 01-gate0.md lines 116-147 (G0-2) | Embedded YAML in the report has pointer strings and trailing prose. Block file B01-gate0.yaml is authoritative and complete; presentational | n/a |
| 23 | C | 07-emoat.md Section 3 recount line; B07 evidence_mix (EM-2) | evidence_mix {documented 12} uses an unstated counting rule; tagged documented rows exceed 12. Undercounting is the conservative direction | n/a |
| 24 | C | 07-emoat.md 2C; B07 capex_embedded_growth_pct (EM-3) | Filed 0; the 2C arithmetic as written gives 42.5% (Rs 1.37 Cr CWIP x 32.77x). Override reasoned and disclosed; stage 11 must read the analyst_note | n/a |
| 25 | C | B07 catalysts_12m items 3 and 4 (EM-4) | Two items sit outside 12 months (state DNA and cyber awards 6-18m; E-Forensics CWIP 12-24m). Stage 11 should read the window field, not list membership | n/a |
| 26 | D | B06 Part 1 Q8; ADSL May-2026 p.12 (F2) | Q8 VERIFIED covers the disclosure-practice half only; GeM wording and timing after award rest on one peer or on silence; timing not caveated | n/a |
| 27 | D | ADSL-Feb-2026 lines 867, 940; ADSL-May-2026 line 516; ZENTEC-Jul-2026 lines 482, 563; DSSL-Jun-2026 line 57 (F3) | Page anchors off by one: ADSL Q3 Supreme Court p.22 (p.21); ADSL Q3 10% threshold p.24 (p.23); ADSL Q4 Western Railway p.14 (p.13); Zen Q1 FY27 state police p.14 (p.13); Zen Q1 FY27 "no simulator tenders" p.16 (p.15); DSSL Q4 PPE and net debt p.4 (p.5). Quotes and figures exist | n/a |
| 28 | D | DSSL-Feb-2026 p.6 lines 215-222; DSSL-Jun-2026 line 57 (F4) | DSSL net debt Rs 68 Cr cited to Q3 p.6; the Feb-2026 call has no net debt figure; it is in the Jun-2026 call (p.5) | n/a |
| 29 | D | DSSL-Feb-2026 p.13; DSSL-Jun-2026 p.10 (F5) | "Milestone payment vs upfront billing" is in DSSL Q4 (Jun-2026 p.10), not Q3. Row stays SUBSTANTIVE | n/a |
| 30 | D | ZENTEC-Jul-2026 p.4 lines 119-125 (F6) | Zen WC 196 to 257 days attributed to cash holdings; transcript says supplier advances and inventory. B06 inference stated as fact | n/a |
| 31 | D | ZENTEC-Jul-2026 line 482; full-text search of 11 files (F7) | "Both sell to police" for ADSL and Zen: "police" appears once in all 11 transcripts. Q5 net read calls silence both "no evidence" and "informative". Verdict UNVERIFIABLE correct and not upgraded | n/a |

## Verifier notes as filed

Verifier A. Numbers checked 236 of a material universe of 410 (58%); 227 clean; 9 defects in 7 findings. False positives struck before filing: 3 (stage 04 "deck slide N" labels; cash-tax figures behind a withdrawn inference; "33 or 34 payroll staff", a faithful copy of a source anomaly). Not verified: web-sourced items in 08 and 09, and items tagged PENDING LIVE VERIFICATION. "No CRITICAL: no verdict-card or Section 1B pillar input differs from source."

Verifier B. Independent list 29 items (0 CRITICAL, 15 MAJOR, 14 MINOR). Against the pipeline: 15 caught, 7 partially caught, 7 missed. Material 15: 10 caught, 4 partial, 1 missed. Promise-delivery spot checks: 6 checked, 6 confirmed, 0 wrong. Pipeline flags not supported: none. Credibility grade: "concur: C is the no-concall default and nothing documents delivery strong enough for B; evidence sits at the low end of C." Not read: risk factors p.36-50.

Verifier C. Scope: PHASE 1 ONLY (Gate 0 and Emerging Moat). Valuation audit, expectation ledger and rule 9 PENDING PHASE 3. Gate 0 final classification AVERAGE concurs. Rubric notes for the operator: (1) Gate 0 M11 says the two-window test "needs >= 6 years", but two non-overlapping 3-year windows need 7 annual points; (2) Gate 0 M10 has no band for exactly 1 decline year with unstable receivable days.

Verifier D. Peers audited 11; substantive confirmed 11; unsupported none; unused but relevant none; all claims addressed. Verdict discipline fails: 1 (Q3).
