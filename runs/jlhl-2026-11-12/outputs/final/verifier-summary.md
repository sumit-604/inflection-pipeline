# JLHL verifier summary, phase 1 (run 2026-11-12)

## Confidence delta (phase 1, computed by the orchestrator)

| Component | Score | Verifier | Basis |
|---|---|---|---|
| numerical_acceptance | 97 | A (B12a) | 470 numbers checked of about 1,900 material cells; mandatory tier 32 of 32 (OR-32); 0 CRITICAL, 4 MAJOR, 1 MINOR; 4 false positives struck |
| redflag_coverage | 85 | B (B12b) | 13 material found (CRITICAL + MAJOR), 11 caught (7 in full, 4 partial); full-catch-only 7/13 = 53.8%, shown for transparency, not scored |
| framework_adherence | 94.4 | C (B12c) | phase 1 scope only: 68 of 72 rules (Gate 0 46/48, Emerging Moat 22/24) |
| framework_adherence_valuation | PENDING PHASE 3 | C (B12c) | stages 10 and 11 not run; B10/B11 audit, expectation ledger and narrative rules deferred |
| peer_utilisation | 100 | D (B12d) | 12 substantive confirmed of 12 peer transcripts provided |
| overall | 85 | | min of applicable; set by redflag_coverage; band 75-89 normal, note specifics; not_applicable: none |

Acceptance rates: A 97, B 85, C 94.4 (phase 1), D 100. REWORK triggers: Verifier A confirmed CRITICAL false; acceptance below 60% false. Remediation cycles: 0. Verifier runs: A 1, B 1, C 1, D 1.

Verifier C covers Gate 0 and the Emerging Moat scan only. Its valuation half (B10, B11, destination PE, expectation ledger, business understanding narrative rule) is PENDING PHASE 3.

Verifier A identity check: no CRITICAL rows in B12a, so no row to test. No finding struck by the orchestrator. Verifier A shadow: not run by this session (claimed by runs/kusumgar-2026-11-12).

## CRITICAL

None. No verifier logged a CRITICAL finding.

## MAJOR

| # | Verifier | ID | Location anchor | Note (as the verifier wrote it) | Source fidelity |
|---|---|---|---|---|---|
| 1 | A | A-1 | 01-gate0.md, Block C caution line (tax rate) | Claimed FY26 tax rate 25.7% (66.25 / 260.44). Source: 66.25 / 260.44 = 25.44% (screener-Data_Sheet FY26 Tax 66.25, PBT 260.44; AR26 p.192 C: 662.49 / 2,604.36 = 25.44%). 25.7% is the FY25 rate (66.93 / 260.68 = 25.68%). FY25 rate printed against the FY26 inputs. Not a scored input; the FY24 9.6% comparison is correct (18.80 / 195.42). | true (MISMATCH) |
| 2 | A | A-2 | 01-gate0.md, Block B capex FY21 to FY23 (2,415.89 / 917.32 / 772.44 Mn) | Claimed RHP restated cash flow p.76. Values are exact but sit on RHP PDF p.77 (printed folio 70, "Purchase of fixed assets"). PDF p.76 is the Restated Statement of Profit and Loss. ANCHOR NOT FOUND at the cited page; one page off. Feeds B2, B3 (mandatory tier). Value correct, anchor wrong. | true (ANCHOR NOT FOUND) |
| 3 | A | A-3 | 01-gate0.md, Block B capex FY24 (852.95 Mn) | Claimed AR 2025 consolidated cash flow, printed p.167. 852.95 is on Annual_Report_2025.pdf PDF p.86, printed folio 166. ANCHOR NOT FOUND at printed p.167; one folio off. Value correct. Feeds B2, B3 (mandatory tier). | true (ANCHOR NOT FOUND) |
| 4 | A | A-4 | 09-tam.md, Method 1, Method 5, Section 4A (RHP bed density, MMR and Kalyan-Dombivli inputs, global median, ARPOB CAGR, per-capita spend) | Values exist but not on the cited PDF pages. MMR figures (33.0 beds/10,000, 20.96 M, 69,000 beds): PDF p.184 and p.185; Kalyan-Dombivli (10/10,000, 1,500 beds): PDF p.185 (cited p.178, which holds personnel data). Global median 29 beds: PDF p.147 and p.176 (cited p.172). ARPOB CAGR 10.7%: PDF p.181 (cited p.174). US$56.6: PDF p.145 (cited p.138). Mixed printed-folio and PDF-page convention with no label. Bed-density inputs drive the Method 5 conclusion. Values correct, anchors unreliable. | true (ANCHOR NOT FOUND) |
| 5 | B | F1 | MISSED. May26 PDF p.4 Ankit Thakker l.133-136; Oct26 PDF p.3 opening l.108-116; Feb26 PDF p.4 l.156-164 | Pune South land was leased, contradicting May "we pretty much own all the real estate"; Rs 150 Cr purchase (Rs 100 Cr new cash) announced Oct; landowner not named; B05 grades it "Strengthening". | n/a |
| 6 | B | F2 | MISSED. Aug26 PDF p.4 Dhvani Shah / Ankit Thakker l.136-147 | Q2 FY26 unbilled-revenue accounting policy change gave a one-time revenue bump; size not given; inflates FY26 growth base; absent from B05 and B06. | n/a |
| 7 | B | F3 | NOT_SUPPORTED. Aug26 p.6 l.215-219; Oct26 p.7 l.282-289 | B05 lists Dombivli breakeven wording as a timeline slippage ("end of year 2 to 1.5-2 years, hard to predict"). Analyst states guidance as "1.5 to 2 years", CEO "the guidance still holds"; Oct repeats 1.5-2 years and defers an upward revision. No slip; sign reversed. | n/a |
| 8 | B | F4 | SPOT_CHECK_WRONG. May26 (no hit); Aug26 p.7 l.259-261 | B05 2A row 8 seasonality "promise" from May does not exist in May or Feb; counted as delivered. Aug "Q1 and Q3, as I said earlier, are relatively weaker" has no antecedent. | n/a |
| 9 | B | F5 | PARTIALLY_CAUGHT. Oct26 p.4-6 l.169-184, l.246-255; p.9-10 l.365-388 | Dombivli Q2 swing (Rs 9.5 Cr to Rs 0.2 Cr) read as Strengthening; derived contribution about doubles vs 17-40% occupancy rise at lower ARPOB; four analysts pressed; cost-timing reading not named. | n/a |
| 10 | C | C-01 | Gate 0, rule G26 E2 (prompts/01 L91-92, L19-22); B01 L101 | E2 scored 3 on an 18-month window, Mar-2025 to Sep-2026; B01 itself calls the 3-year point NOT FOUND. Recomputed E2 = 0; Block E 13; core 68; grand total 91. Decision effect none: Core 60-79 + STRONG = GOOD+, capped to GOOD by deal-breaker 2. Confirming observation: promoter group % in the 30-Sep-2023 shareholding pattern; 39.91-41.91% restores E2 = 3 and core 71. | n/a |
| 11 | C | C-02 | Emerging Moat, rule E17 2C (prompts/07 L59-62); B07 L92-94, L376 | capex_embedded_growth_pct 177 on 2,129 Cr counts Pune South, Mira Road, BKC, Thane. Recomputed 62: Pune South 750 Cr x 1.245 = 933.8 Cr on FY26 1,499.8 Cr; range 50-64; bed-day cross-check 48. 177 is the announced pipeline. Risk that stage 11 or 13 reads 177 as embedded capacity growth. Confirming observation: construction start at Mira Road, BKC or Thane adds that project to the 2C count. | n/a |

## MINOR

| # | Verifier | ID | Location anchor | Note (as the verifier wrote it) | Source fidelity |
|---|---|---|---|---|---|
| 12 | A | A-5 | 01-gate0.md, Block E, E2 | Claimed "RHP p.~240 shows promoters at 40.69% pre-offer". 40.69% (23,677,415 shares) is at RHP PDF p.260; p.239 to p.240 hold director profiles. Approximate anchor with a tilde, wrong page. Context figure only; the E2 score rests on 40.91% to 40.91% (AR25 p.50, XBRL). | true (ANCHOR NOT FOUND) |
| 13 | B | F6 | INTERNAL_INCONSISTENCY. B05 2A | B05 counts not-yet-due rows 6, 9, 10 against its own due-only rule; recount 4/2/0. | n/a |
| 14 | B | F7 | OVERSTATED. Aug26 p.6 l.219; Oct26 p.7 l.282-289 | Breakeven-guidance revision listed as a repeated evasion; answers were direct. | n/a |
| 15 | B | F8 | OVERSTATED. May26 p.7 l.259-261 | "Q4 FY26 drag Rs 9.4 Cr": call does not say loss or revenue. | n/a |
| 16 | B | F9 | OVERSTATED. B06 Q8 | B06 Q8 "KIMS shows the opposite" on Q2 medical-mix ARPOB; KIMS group ARPOB not a clean test. | n/a |
| 17 | B | F10 | PARTIALLY_CAUGHT. May26 p.6 l.224-230 | BKC "back of the envelope" funding with no red-flag row. | n/a |
| 18 | B | F11 | PARTIALLY_CAUGHT. KIMS Feb26 p.7 l.266-268; Oct26 p.9 l.342-344 | B06 "contradicted: 0" despite KIMS NABH line contradicting the JLHL CEO; B05 calls empanelment drift Unchanged. | n/a |
| 19 | B | F12 | PARTIALLY_CAUGHT. May26 p.7 l.274-277; Feb26 p.8 l.296-299 | Biennial renewal step behind FY26 ARPOB not carried to FY27; defensiveness 2 is light. | n/a |
| 20 | B | F13 | MISSED. Feb26 PDF p.9 l.333-336; Aug26 PDF p.9 l.360-361 | CGHS stance shift: Feb "you will not see any impact on that at all" to Aug "with the revised pricing, we could consider it"; B05 calls it unchanged. | n/a |
| 21 | B | F14 | MISSED. Feb26 PDF p.8 l.306-308; KIMS May26 PDF p.9 l.333-341; MEDANTA Feb26 PDF p.16 l.601-609 | Peer contrast not drawn: KIMS cites FY26 industry insurer standoff and GIC common-empanelment confusion; MEDANTA "could have been faster"; JLHL said no unusual payer friction. | n/a |
| 22 | B | F15 | OVERSTATED. Aug26 p.8 l.318; p.9 l.355 | "exact" debt refused "every call" / "Aug and Oct"; only Aug. | n/a |
| 23 | B | F16 | ANCHOR_IMPRECISION. B05 2A, 1B, 1C | Several B05 May/Aug/Oct cites one page low (printed vs PDF page); route to Verifier A. | n/a |
| 24 | C | C-03 | Gate 0, rule G03 ROCE fixed formula (prompts/01 L27-31); B01 L18, L29 | EBIT / (TA - other liabilities) used for FY20-FY26; CL split exists in RHP p.75, AR 2025, AR 2026 p.191. NOT RECOMPUTABLE from B01 inputs for FY21-FY25; FY26 fixed basis 13.82%, same band. A1 median FY22 15.35% is 0.35pp over the 15% boundary; worst case A1 3 -> 1, core -2 (66 with C-01), GOOD unchanged. Confirming observation: FY22 TA - CL from the RHP restated balance sheet at or below 807.1 Cr keeps A1 = 3. | n/a |
| 25 | C | C-04 | Emerging Moat, rule E10 (prompts/07 L172-174; prompts/12 L241-244); B07 L205 | B1 at 0.7 on the claimed benefit; E1 and R1 at 1.0 on the documented fact; total 13.6. Recomputed B1 at 1.0 on the fact basis: 13.9, MODEST. Advantage basis gives 11.1 (10.5 with B2 at 0.7), NONE, which changes the Pillar 3 EM input. Operator ruling needed; prompt gap at prompts/07 L172-174. | n/a |
| 26 | D | D-1 | B06 2B and yaml industry_cross_read.pricing_inputs | Insurers-push-price-down attributed to KIMS and MEDANTA; MEDANTA Q3 FY26 p.7 does not say it; KIMS Q3 FY26 p.7 alone supports it; erratum appended to report but yaml uncorrected. | n/a |
| 27 | D | D-2 | B06 Part 5 | KIMS Q2 FY27 Rs 13.2 Cr call-option gain cited p.14; text is on p.15. | n/a |
| 28 | D | D-3 | B06 Q4 and Q7 verdicts | VERIFIED labels lenient: Q4 peer range 5-23 months with one expectation not outcome; Q7 land vs no-land split NOT FOUND at all peers; gaps disclosed in-row, no upgrade from silence. | n/a |

Verifier B also records 5 promise-delivery spot checks: 4 confirmed, 1 wrong (F4). Its credibility read: "concur at B, low end: zero hard misses holds, but a due-only recount is 4 delivered / 2 partial / 0 missed (row 8 has no source promise; rows 6, 9, 10 not due), and the Pune leased-land contradiction belongs in the basis."

Verifier D: peers audited 12; substantive confirmed 12; substantive unsupported none; unused but relevant none; claims all addressed; verdict discipline fails none.

## Stage figure against verifier figure

| Item | Stage figure | Verifier figure | Governs |
|---|---|---|---|
| Gate 0 FY26 tax rate | 25.7% (01-gate0.md Block C) | 25.44% (screener Data_Sheet; AR26 p.192) | Verifier A (source fidelity, non-overridable) |
| Capex FY21 to FY23 anchor | RHP p.76 | RHP PDF p.77 (printed folio 70); values unchanged | Verifier A |
| Capex FY24 anchor | AR 2025 printed p.167 | Annual_Report_2025.pdf PDF p.86 (printed folio 166); value unchanged | Verifier A |
| TAM bed density and RHP inputs anchors | RHP p.178, p.172, p.174, p.138 | RHP PDF p.184-185, p.147 and p.176, p.181, p.145; values unchanged | Verifier A |
| Promoter pre-offer 40.69% anchor | RHP p.~240 | RHP PDF p.260 | Verifier A |
| Gate 0 E2 / core / grand | E2 3; core 71; grand 94 | E2 0; core 68; grand 91; GOOD unchanged | Verifier C (framework rule) |
| Capex embedded growth | 177% (announced pipeline, 2,129 Rs Cr) | 62% (Pune South 750 Rs Cr under execution) | Verifier C (rule counts capex under execution only) |
| Emerging Moat score | 13.6 MODEST | 13.9 MODEST (fact basis) or 11.1 NONE (advantage basis) | Open: operator ruling needed (C-04) |
| Promise delivery | 6 delivered / 4 partial / 0 missed | 4 / 2 / 0 on promises already due | Verifier B (transcript lines) |
| Dombivli breakeven wording | timeline slippage | no slip; guidance held at 1.5-2 years | Verifier B (transcript lines) |
| B05 2A row 8 seasonality promise | delivered | no source promise exists | Verifier B (transcript lines) |
| B06 insurer price pressure attribution | KIMS and MEDANTA | KIMS alone | Verifier D (transcript page) |

## Verifier disagreement log

none

No downstream step relied on, kept, or cleared a figure Verifier A flagged. Verifier C's Gate 0 and Emerging Moat re-derivations did not use the 25.7% tax rate, and the misanchored values it touched are correct values. Synthesis carries 25.44% and the corrected anchors. No source re-check cleared any Verifier A flag.

## Open items (from confidence.yaml)

1. B12a: five source-fidelity findings (one wrong value: Gate 0 FY26 tax rate 25.7% printed, source 25.44%; four anchor-page errors in 01-gate0.md and 09-tam.md). Not corrected in the stage reports; no remediation cycle was run because REWORK did not fire. Each must be corrected at source before any phase-3 use.
2. B12b F1 (MAJOR, missed upstream): Pune South land was leased, against the May statement on owning the real estate; Rs 150 Cr purchase; landowner not named.
3. B12b F2 (MAJOR, missed upstream): Q2 FY26 unbilled-revenue accounting policy change, one-time revenue bump, unsized.
4. B12b F3, F4, F5 (MAJOR): B05 breakeven "slippage" not supported; B05 2A row 8 has no source promise; Dombivli Q2 swing second reading (cost timing) not named. Due-only promise recount 4 delivered / 2 partial / 0 missed.
5. B12c C-01 (MAJOR): Gate 0 E2 scored 3 on an 18-month window; rule scores 0; core 68 not 71; classification GOOD unchanged. C-02 (MAJOR): B07 capex_embedded_growth_pct 177 counts projects not under execution; recompute 62. C-04: evidence-multiplier basis needs an operator ruling (13.9 MODEST vs 11.1 NONE).
6. B12d: three MINOR; B06 block pricing_inputs line still attributes insurer price pressure to MEDANTA (KIMS alone supports it).
7. Verifier A shadow not run by this session (claimed by runs/kusumgar-2026-11-12).
8. From confidence.yaml rework_triggers note: Verifier B's full-catch-only rate of 7/13 = 53.8% is carried to Halt 1 for the operator; the scored rate is 85.
