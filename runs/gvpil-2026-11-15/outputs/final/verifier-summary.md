# GVPIL verifier summary, PHASE 1 (run 2026-11-15)

## Confidence delta (phase 1)

| Component | Value | Basis | Source |
|---|---|---|---|
| numerical_acceptance | 98 | 429 numbers checked; mandatory tier 139 of 139 (Gate 0 scorecard, OR-32); about 290 of 431 sample numbers checked | B12a |
| redflag_coverage | 86 | 14 material flags, 12 caught (9 caught, 3 partially caught), 2 missed; strict caught only 64 | B12b |
| framework_adherence | 89.3 | Gate 0 (45 rules) and Emerging Moat (30 rules): 67 of 75 passed | B12c |
| peer_utilisation | 83.3 | 10 of 12 peer transcripts used substantively | B12d |
| overall | 83.3 | min of applicable components; overall_set_by peer_utilisation; not_applicable none | confidence.yaml |

Band: 75 to 89, normal, note specifics (overall_set_by peer_utilisation).

Acceptance rates as each verifier reported them: A 98; B 86; C 89.3 (phase 1 scope); D 100 (no MAJOR or CRITICAL finding; the peer_utilisation component is computed separately as 10 of 12).

Verifier C's valuation half is PENDING PHASE 3. Its valuation adherence audit (B10, B11), the expectation ledger checks, the business understanding narrative check and the recomputed destination PE and decision were not run in phase 1, because stages 10 and 11 do not exist yet. Their fields in B12c are null or blank, and null means not evaluated, not a finding.

Verifier A identity check (orchestrator): no CRITICAL rows in B12a, so nothing was tested and nothing was struck. Verifier A itself struck 4 draft rows under its rule 5b (contingent growth 5.6% reproduces; CFO and equity consolidated against standalone, labelled; ICRA upgrade dated 2 Mar and 3 Mar, each in its own source; BHEL reversal "about Rs 116 Cr" faithfully transcribed).

Verifier runs: A 1, B 1, C 1, D 1. Remediation cycles: 0. Verifier A shadow: not run in this session (operator batch instruction).

## CRITICAL

None. Verifier A 0, Verifier B 0, Verifier C 0, Verifier D 0.

## MAJOR (9)

| # | Verifier | Location anchor | Note (verifier's words, condensed) |
|---|---|---|---|
| 1 | A (source fidelity) | 08-promoter.md Section 3A, "Purchases from group: materials INR M 697.6 FY26" | Copy error. Source truth INR M 699.1 = 71.1 + 182.6 + 106.1 + 68.7 + 41.6 + 96.5 + 55.2 + 53.9 + 23.4 (AR26 Note 36 p.181, L 12421-12441). Context figure, not a pillar input. Corrected by orchestrator erratum. |
| 2 | A (source fidelity) | 03-ardeep.md Phase 3B balance sheet table, "Other financial and other assets", FY26 cell | Cell prints 1,432.7; source truth 1,601.4 = 58.5 + 268.9 + 1,007.1 + 155.6 + 111.3 (AR26 standalone p.131, L 8908-8938). The note under the table already gives 1,601.4. Corrected by orchestrator erratum. |
| 3 | A (source fidelity) | 04-bizmodel.md Section 3B must-track table, "Material cost % of revenue" row | 67.6% is gross of the (100.6) WIP change (2,103.8 / 3,112.3, Results Q2 FY27 p.3); the 60.2% and 67.3% bases are net. Net Q2 FY27 is 64.4%, so the 67% red flag is not tripped. Unlabelled basis difference, UNANCHORED. Corrected by orchestrator erratum. |
| 4 | A | 09-tam.md Section 2 Method 2 (bottom up) | "Rs 1.1 Cr per MW a year" is out by 100x: Rs 2,500 Cr / 224,150 MW = about Rs 1.1 lakh per MW a year. Derived figure; the report says not to read it as a unit rate. source_fidelity false. Erratum appended. |
| 5 | B (MISSED) | B05 2A row "INR 300-320 cr per quarter"; 3C | Opposite CFO answers on whether the BHEL ECL reversal sits in cost (Q3) or in revenue (Q4); B05 treats Q4 INR 316 cr as clean delivery. Anchor: Q3 FY26 p.9-10; Q4 FY26 p.16. |
| 6 | B (MISSED) | B05 2D, 3C | Three party BHEL settlement with promoter offshore entities, group side undisclosed when asked; INR 17 cr receivable gap (calc); related party load-bearing fact. Anchor: Q2 FY26 p.9, p.14. |
| 7 | B (PARTIALLY CAUGHT) | B05 Fact 1 table; flag FACT1_PARTLY_CONFIRMED | MD "close to 2 years" visibility (Q3, Q4), 3-4 year upgrade cycle and FY27 +/-5% guide contradict 85-90% if it applies to the whole INR 1,628 cr book (INR 1,384-1,465 cr from backlog alone, calc); B05 does not use the contradiction. Anchor: Q3 FY26 p.4, p.10, p.11, p.19; Q4 FY26 p.4, p.8. |
| 8 | C (F-G10, gate0) | B01 l.44, Block B2 FCF-positive proportion | Stated 3/6 determinable years = 50% = 2; rule scores NOT FOUND as 0 on the 10 year window (P01 l.19-22, l.64): 3/10 = 30% = 0; Block B 0, core 31, grand total 42. Decision impact none; AVOID and deal-breaker 2 hold. |
| 9 | C (F-E17, emoat) | B07 l.125, l.127, l.343, rows G1 and G2 | FY26 receivable release credited twice (G1 cash 2.0, G2 receivable days 1.0), against the one improvement, one mechanism rule. G2 to 0, EM 11.6 to 10.6. Decision impact none; NONE holds; gap to the 12 band widens from 0.4 to 1.4; Shoaiba upside case still MODEST at 12.6. |

## MINOR (25)

| # | Verifier | Location anchor | Note (verifier's words, condensed) |
|---|---|---|---|
| 10 | A | 02-notes.md Sections 3.6, A rank 2, FLAG-EARNINGS, top_findings rank 2; 03-ardeep.md rank 2 row | 55.3% should be 55.2%: (1,320.0 + 433.5) / 3,174.4 = 55.24%. Rounding of rounded parts. Erratum appended. |
| 11 | A | 09-tam.md Section 3B "Second reading on 4,000" | CAGR 7.8% should be 7.7%: (918 / 734)^(1/3) - 1 = 7.74%. Rounding. Erratum appended. |
| 12 | A | 08-promoter.md Section 0 row 1 and flags; 02-notes.md 3.0.1 and Top-15 rank 7 | FY25 royalty gap 382.4 is right on the AR25 original basis (514.5 less 132.1); against the re-presented 121.5 the gap is 393.0. Unlabelled basis difference. Erratum appended to 08. |
| 13 | A | 09-tam.md Section 4A Drivers row "Utilisation" | PLF 65.2%, 66-68% forecast and demand growth 0.8% attributed to ICRA are not in inputs/rating/ICRA_Rationale_2026-03-03.txt; no ICRA URL in Sources. UNANCHORED. Not material to the 4% proxy. Erratum appended. |
| 14 | B (PARTIALLY CAUGHT) | B05 3C item 5; 2A row "Core double-digit" | Q3 revenue +22% credited to core; 68% of the increase was one-off settlement revenue (calc); MD said core revenue +4%. Anchor: Q3 FY26 p.4, p.5, p.9. |
| 15 | B (PARTIALLY CAUGHT) | B05 1C export row; trigger 5 | Parent set India only perimeter recorded, not flagged or tied to Shoaiba. Anchor: Q4 FY26 p.10; Q3 FY26 p.14. |
| 16 | B (MISSED) | B05 2D | No timeline for about INR 640 cr non-BHEL receivables (calc); peer ISGEC FGD retentions slipped. Anchor: Q2 FY26 p.15; ISGEC Feb 2026 p.11-12; ISGEC 29 May 2026 p.9-10. |
| 17 | B (MISSED) | B05 2C | Q2 FY26 gross margin fall (22% vs 42%, analyst) reframed by CFO to 33% on a different cost base. Anchor: Q2 FY26 p.7. |
| 18 | B (MISSED) | B05 1A, 2A | Same call figure clashes: core intake 18% vs 45%; core revenue 12% vs 14%; country count ("7 countries" followed by eight names; "13-odd" vs "13 other"). Anchor: Q2 FY26 p.4, p.5, p.7, p.12; Q4 FY26 p.4, p.6, p.10. |
| 19 | B (MISSED) | B05 3B | FGD category sizes and notification dates inconsistent across calls (Category C about 70 GW vs more than 200 GW; notification July, 11 July, 11 June 2025). Anchor: Q2 FY26 p.3-4; Q3 FY26 p.10; Q4 FY26 p.11-12. |
| 20 | B (MISSED) | B05 2A row "10% plus FY26" | Q4 one-off list omits INR 25 cr Jaypee gain; no bridge to 11% (up to 2.0 points if included, calc). Anchor: Q3 FY26 p.5, p.13; Q4 FY26 p.6. |
| 21 | B (MISSED) | B05 trigger 4 | Possible transfer of Durgapur post appointed date costs (over INR 50 cr for 9M) is a signalled future one-off credit. Anchor: Q3 FY26 p.19. |
| 22 | B (PARTIALLY CAUGHT) | B05 guidance block; trigger 3; timeline_slippages | FY27 revenue guide given two ways (+/-5% and 5-8%) and JSW access "declining" vs "reserved" resolved silently. Anchor: Q3 FY26 p.11, p.16, p.18; Q4 FY26 p.15. |
| 23 | B (PARTIALLY CAUGHT) | B06 Q3, Q4, 2E | Power Mech IPP R&M and ISGEC retention slippage not tied back to GVPIL statements. Anchor: POWERMECH Aug 2026 p.14; GVPIL Q3 FY26 p.20; ISGEC 29 May 2026 p.9-10. |
| 24 | B (OVERSTATED) | B06 cross_peer_hypothesis | ISGEC does not supply utility power plants; its services division serves its own industrial boiler base. Anchor: ISGEC Feb 2026 p.12; ISGEC Aug 2026 p.16. |
| 25 | B (OVERSTATED) | B05 2D first bullet | "New build is loss-making" given as the likely reason for the segment margin refusal, unlabelled and not in the transcript. Anchor: Q2 FY26 p.12; Q3 FY26 p.15. |
| 26 | B (OVERSTATED) | B06 Part 4; Q7 net read | Power Mech standalone margin rise is Apr-Jun 2026, not the Jul-Sep quarter of GVPIL's fall; only ISGEC covers the same period. Anchor: POWERMECH Aug 2026 p.3; ISGEC Nov 2026 p.4. |
| 27 | C (F-G03, gate0) | B01 l.17, ROCE formula | Proxy capital employed (equity + reserves + borrowings) used all years against a fixed formula (P01 l.27-31). Formal TA-CL for FY25/FY26 leaves A1 1, A2 0, A4 5; strict NOT FOUND reading gives Block A 0, core 27. AVOID under both readings. |
| 28 | C (F-G36, gate0) | B01 l.81, M11 | Two window test not performed (P01 l.129-133). Outcome 0, or 5 if FY20 revenue exceeded 2,540.5 Cr (calc) and selling % declined; a 5 makes 3 moats (still MODERATE), moat score 16. |
| 29 | C (F-G42, gate0) | B01 l.89, deal-breaker 4 | Not recorded; cumulative CFO/PAT -1.92 is below 0.50 and fires max AVERAGE (P01 l.156-157). Does not bind; DB8 sets the same cap and the class is AVOID. |
| 30 | C (F-E03, emoat) | B07 l.87, l.91, l.135 (A2, A4 NPI, H3); l.119, l.125, l.127 (G1, G2, F1) | Three evidence items without page or note; four anchored to upstream blocks instead of a source (P07 l.35-36). Anchor format fix only; existence of numbers is Verifier A's. |
| 31 | C (F-E16, emoat) | B07 l.141, I2 | I2 question answered for A4, C1, G1 only; A1, E1, F2, G2, R1 unanswered (P07 l.140-142). I2 most likely stays 0. |
| 32 | C (F-E20, emoat) | B07 block l.38; flag CAPEX_GROWTH_NOT_MEANINGFUL l.73 | capex_embedded_growth_pct holds 0, not the 2C result 73.0 (P07 l.233). No effect on EM score; field-only readers see 0. |
| 33 | D | B06 peer coverage map, POWERMECH Nov 2025 | O&M margin 15-16% (lines 747, 819) not used as an extra Q1 anchor; same peer, verdict unchanged. |
| 34 | D | B06 peer coverage map, BHEL May 2023 | Ukai R&M cited as "p.4, p.7 region"; page imprecise. |

Counts by verifier: A 4 MAJOR, 4 MINOR; B 3 MAJOR, 13 MINOR; C 2 MAJOR, 6 MINOR; D 0 MAJOR, 2 MINOR. Verifier B's coverage basis reads: 34 independent flags listed, 14 material, 9 caught, 3 partially caught, 2 missed; GVPIL transcripts read in full, peers by targeted search; B05 and B06 were opened before the transcripts (anchoring risk disclosed). Verifier B concurs with credibility grade B (6 of 6 promise delivery spot checks confirmed) and found no pipeline flag unsupported. Verifier D found every peer claim addressed, no substantive use unsupported and no verdict discipline fail.

## Verifier observations (not findings, not counted)

- Verifier C O-01: the Gate 0 moat class MODERATE rests on FY26 spot ROCE 48.4% in M3. On the window median reading (11.5%), M3 is 0, 1 moat, THIN, moat score 6.
- Verifier C O-13 (forward note for phase 3): catalysts_12m marks pending events as documented (Shoaiba contract signature, Q3 FY27 margin outcome). The phase 3 check should confirm that Pillar 3 reads these as documented triggers, not documented outcomes.
- Verifier C O-02 to O-12: basis and format observations (D2 and D4 bases, M8 basis line, loss to profit note, C1 likelihood, F2 against 6D, evidence_mix count, H2 rationale, 6D matrix, FY17 to FY19 borrowings blanks, Section 3 format). Full list in outputs/reports/12c-verifier-framework.md Section 4.
- Verifier A coverage: web sourced figures in 09-tam.md (CEA 224.15 GW, 228,560 MW, CREA 44 GW, IMARC USD 1,043.6M, BHEL Rs 75,000 Cr) and 08-promoter.md (SEC USD 200M, vote percentages, 10 Dec 2025 NSE filing) were not checked, because no corpus PDF holds them. Eight of twelve peer transcripts were sampled by keyword, not read in full.

## Verifier disagreement set

none.

No downstream step's conclusion conflicted with a Verifier A source fidelity finding in this phase. The three source fidelity rows (INR M 697.6 to 699.1; 1,432.7 to 1,601.4; 67.6% to 64.4% net of WIP) were corrected by orchestrator errata at their source anchors before synthesis, and no flagged value was carried into any phase 1 file. Verifier C's phase 1 scope (Gate 0 and Emerging Moat) relied on none of the three figures. No source re-check cleared any Verifier A flag.
