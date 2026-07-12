# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 3 OF 3 (PATTERN PASS + CONSOLIDATION)
NORTHARC | Run date 2026-07-12 | Source: extracted/annual-report.txt, re-read against Pass 1 and Pass 2 outputs

**UNIT CONVENTION**: Source in ₹ lakhs; all figures converted to ₹ Crores (÷100), raw lakh figure retained in parentheses for audit.

---

## PASS 3 — PATTERN PASS (contradictions, mismatches, vague disclosure, restatements, post-BS events, going concern)

Pass 3 yields **material new findings** — not empty. Findings below are new to this pass (not repeats of Pass 1/2):

**P3-1. 🟡 Two different FY25 Net NPA ratios disclosed in the same annual report, unreconciled.** Note 68(a) "Net NPAs to net advances" states **0.39%** FY25 vs 0.09% FY24. The separate regulatory ratio-analysis disclosure (RBI Scale Based Regulation format, PDF p.~254) states Net NPA Ratio **0.43%** FY25 vs 0.09% FY24, explicitly defined there as "(gross stage 3 term loans − impairment loss allowance for stage 3 term loans) / (gross term loans − impairment allowance for stage 3 term loans)" — i.e. a term-loans-only denominator, narrower than Note 68(a)'s "net advances." The two definitions are plausibly different in scope (total net advances vs term loans only) but the document never cross-references or reconciles them, despite both being labelled simply "Net NPA(s)." This is the kind of side-by-side inconsistency the pattern pass is designed to catch: directionally identical (both ~4-5x deterioration YoY) but numerically inconsistent without explanation. (Note 68(a), PDF p.242; Ratio-analysis disclosure, PDF ~p.254) — refines/confirms the discrepancy Pass 2 flagged for verification.

**P3-2. 🟡 Gratuity accounting policy contradicts its own actuarial disclosure — confirmed on second read, present in BOTH standalone and consolidated notes identically.** Note 3k (accounting policy, both standalone p.156 and consolidated equivalent p.~within Note 3) states: "The Company/Group make[s] annual contributions to gratuity funds established as trusts." Note 40 (standalone) / equivalent consolidated note discloses **fair value of plan assets = ₹0 (Nil) in both FY24 and FY25** — i.e., the plan is actually unfunded. The identical contradictory wording appearing in both standalone and consolidated policy notes (verified at two separate locations in the document) rules out a one-off typo; it reads as boilerplate policy language that was not updated to match actual practice. Not P&L-material (DBO is provided for on the balance sheet either way), but it is a genuine internal document inconsistency and a proxy for note-maintenance rigour. (Note 3k vs Note 40, PDF p.156/222; consolidated equivalent PDF p.~within Notes 3 and equivalent gratuity note)

**P3-3. 🟡 Complaints-count mismatch between the headline complaints table and the "grounds of complaints" table, unexplained in the note.** Note 72's main table states total complaints received: 938 (FY25) / 91 (FY24) (already used in Pass 1's #3 finding). The same note's "Top five grounds of complaints" sub-table shows FY25 total tagged-by-ground complaints of **1,124** (+350% YoY) against an FY24 grounds total of **250**. Neither total reconciles to the 938/91 headline figures. The most likely explanation is that a single complaint can be tagged to multiple grounds (so the grounds table double-counts relative to unique complaints) — this is a common disclosure convention — but the note does not state this anywhere, so the reconciliation is grounded inference, not a disclosed fact. Separately confirmed: the year-captions ("For the Year ended 31 March 2025" / "31 March 2024") in the extracted text sit awkwardly relative to their data blocks — a PDF-table-reflow artifact, not a substantive error, but it makes the note harder to audit at first read than the otherwise granular RPT/borrowings notes elsewhere in the document. (Note 72, PDF p.243-244)

**P3-4. 🟢 No quantified prior-year restatement found; only generic regrouping boilerplate.** Note 87 (standalone, PDF ~p.252) and Note 53 (consolidated) both state: "Previous year figures have been regrouped/rearranged, wherever considered necessary, to conform to the classification/disclosure of the current year." No specific line item, amount, or note is identified as restated or reclassified with a quantified prior-year impact anywhere in the document. This is standard IPO-adjacent boilerplate, not evidence of a restatement. **restatements_found: none identified.**

**P3-5. 🟢 Going concern: no material uncertainty anywhere in the document.** Standard affirmative language appears identically at four locations — Directors' Responsibility Statement, standalone accounting policies (Note 2, PDF p.144: "prepared on a going concern basis... Management is satisfied... no material uncertainty exists"), consolidated accounting policies (same wording), and both Independent Auditor's Reports (standalone and consolidated) confirm no going-concern qualification or Key Audit Matter. No going-concern-adjacent stress language (e.g., "significant doubt," "material uncertainty") appears anywhere in the notes. **going_concern_language: NONE.**

**P3-6. No new post-balance-sheet events beyond the two already flagged in Pass 1/2** (RBI FLDG/ECL directive dated 16-May-2025, already absorbed in FY25 numbers; Finreach stake sale from 24.55% to 11.16% ceasing associate status, Note 84). A full re-scan of the "Events after the reporting period" note and the Auditor's Report "Other Matter"/"Emphasis of Matter" sections found no third event.

**P3-7. Cross-check: contingent liability for subsidiary guarantees remains genuinely NOT FOUND (confirmed on this pass).** Note 38b's caption ("Financial guarantee issued to third parties," PDF p.220) is present but the table content covers only the third-party financial-guarantee book already quantified in Pass 1 (₹1.69 Cr FY25 vs ₹64.42 Cr FY24); no separate line for guarantees issued specifically on behalf of subsidiaries/associates was found on a targeted re-read. Treated as NOT FOUND IN DOCUMENT, not as a red flag — the Company's subsidiaries (NAIM, Pragati, etc.) do not appear to carry parent guarantees per the disclosed table.

**No contradiction found** between the borrowings covenant notes (15B/15E, "no default," "not a wilful defaulter") and the ratings/liquidity notes (Note 62, 79) — internally consistent.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | RBI-directed FLDG exclusion from ECL model: ₹80.41 Cr total impact, ₹68.35 Cr already absorbed in Q4FY25 PBT; flagged as Auditor's Emphasis of Matter | Note 83 standalone / 49 consolidated, p.261/380 | 🔴 | Regulator-forced correction proves the Company's own ECL model had been over-crediting FLDG recoveries; direct evidence of prior ECL-model aggressiveness |
| 2 | Consolidated Group PAT fell 5.2% YoY (₹301.32 Cr vs ₹317.69 Cr) while standalone PAT rose +22.3%, driven by Pragati Finserv swinging from +₹19.55 Cr profit to −₹29.39 Cr loss (net worth eroded 85.7%) | Note 22, consolidated, p.353 | 🔴 | Standalone-only PAT reading materially overstates true Group earnings momentum; also undermines the Pragati CGU goodwill test (Note 81) which was not shown to be re-run against this loss |
| 3 | Impairment on financial instruments (P&L) up 207% YoY (₹378.53 Cr vs ₹123.14 Cr); GNPA ratio doubled 0.47%→0.99%; provision coverage on Stage 3 fell ~82-84%→~68% | Notes 27, 36(i), 68-69, p.199-230 | 🔴 | Largest single P&L swing item in the notes; core credit-quality deterioration |
| 4 | Customer complaints up ~930-1000% YoY (91→938 headline; grounds-table total 250→1,124) vs ~15% loan book growth; complaints pending year-end 1→129 | Note 72, p.243-244 | 🔴 | Magnitude mismatch vs book growth signals operational/collections strain not addressed in MD&A |
| 5 | Basic EPS fell 28.2% (₹31.45→₹22.59) despite PAT +22.3%, entirely from IPO + CCPS-conversion dilution (weighted avg shares +70.3%) | Note 32, p.217 | 🔴 (flag) | Visible optical negative on any trailing-EPS screen; one-time capital-structure effect, not an earnings-quality flaw |
| 6 | Fraud disclosure: 29 instances, ₹1.18 Cr, predominantly staff cash-handling (25 of 29, ₹1.10 Cr) — no prior-year comparative given | Note 51, p.236-237 | 🟡 | Third independent data point (with complaints and attrition) reinforcing an operational-control-strain theme |
| 7 | Related-party lending fully unwound in one year: loans to subsidiaries ₹100.98 Cr→Nil; loans to director-interested firms ₹305.78 Cr→Nil, no counterparty named for the latter | Note 76, p.248 | 🟡 | Large, unexplained pre-IPO-adjacent related-party lending base eliminated with no disclosed rationale |
| 8 | Gratuity accounting policy ("Company makes annual contributions to gratuity funds established as trusts") contradicts actual disclosure of ₹0 plan assets both years, in both standalone and consolidated notes | Note 3k vs Note 40, p.156/222 | 🟡 | Internal document inconsistency; proxy for note-maintenance rigour, not P&L-material |
| 9 | FVOCI loan book fair-value markdown: OCI reserve fell ₹21.76 Cr (₹37.38→₹15.62 Cr); Level 3 "gains through OCI" swung −₹28.51 Cr vs +₹19.39 Cr prior year | Note 20(g), 35, p.209-210 | 🟡 | Consistent with rising credit stress in the FVOCI-classified loan segment |
| 10 | Stage 1 provision +199% YoY (coverage 0.58%→1.53%) and Stage 2 provision +281% YoY (coverage 9.36%→18.19%) — provisioning build broader than Stage 3 alone | Note 36(i)A, p.215-216 | 🟡 | Partial mitigant to the flat-LGD concern (#12): shows genuine conservatism build across the performing book |
| 11 | Level 3 fair value of the amortised-cost loan book: discount to carrying value narrowed sharply from 24.3% (FY24) to 7.9% (FY25); driver (discount-rate change vs credit re-rating) not disclosed | Note 35(A), p.209-210 | 🟡 | Large, undisclosed swing in an unobservable-input DCF valuation; question for management |
| 12 | ECL LGD is a flat 65% "Basel II FIRB-recommended" assumption, not empirically modelled, applied across a diversified secured/unsecured book | Note 36(i)A, p.228 | 🟡 | Simplifying convention whose conservatism cannot be independently verified from disclosure alone |
| 13 | New ₹267.31 Cr related-party-managed AIF exposure from zero (Northern Arc Emerging Corporates Bond Trust, managed by subsidiary NAIM), plus a further ₹15.00 Cr AIF application money pending allotment | Notes 8, 42, 43, 53, 9; p.168, 169, 231-232, 238 | 🟡 | Concentration + related-party-manager risk combined; total related-party AIF commitment may approach ₹282 Cr |
| 14 | EIS (Excess Interest Spread) receivable Stage 3 balance more than tripled (₹0.53 Cr→₹1.71 Cr, +219%) even as the aggregate EIS balance stayed flat | Note 9.1, p.169 | 🟡 | Growing share of previously upfront-booked gain-on-assignment income sits against now-delinquent pools — leading indicator for future EIS writedowns |
| 15 | Two different FY25 Net NPA ratios disclosed in the same annual report without cross-reference: 0.39% (Note 68(a), net-advances basis) vs 0.43% (regulatory ratio disclosure, term-loans-only basis) | Note 68(a) vs ratio-analysis note, p.242/~254 | 🟡 | Directionally consistent but numerically unreconciled; disclosure-clarity issue found only on pattern re-read |

### B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Upfront gain-on-assignment/EIS recognition is a structurally aggressive pattern for NBFC assignment volumes; Stage 3 EIS tripling is an early writedown signal (findings #14, Pass 1 revenue section) |
| Expense capitalisation honesty | 8 | Depreciation lives at statutory Schedule II norms with no deviation; ROU/lease accounting properly disclosed under Ind AS 116; no evidence of aggressive capitalisation |
| Provisioning adequacy | 6 | Mixed: Stage 1/2 coverage genuinely built up (finding #10, a positive), but a flat non-empirical 65% LGD (#12) and a regulator-forced FLDG/ECL correction (#1) both cut against conservatism claims |
| RPT fairness | 6 | Full RPT table disclosed and self-declared "arm's length" (not independently tested); large, unexplained director-interested-party lending base (₹305.78 Cr) eliminated with no counterparty named (#7) |
| Disclosure transparency | 6 | Extremely granular in places (148 individual loan tranches, full ageing/covenant tables) but several large unexplained swings (Level 3 fair-value discount narrowing, other-receivables spike, dual NNPA ratios) and one internally contradictory note (gratuity policy vs disclosure) |
| Consistency with prior years | 5 | Standalone-vs-consolidated PAT divergence (Pragati loss) not called out or reconciled by the Company anywhere in the standalone notes; Pragati CGU goodwill test (30% discount rate) not shown to be re-run against the FY25 loss/net-worth erosion as a triggering event |
| **OVERALL** | **6** | Financially sound, granular funding/borrowings disclosure and a genuinely de-levered balance sheet, but a regulator-forced ECL correction, an unreconciled standalone/consolidated earnings divergence, and several unexplained note-level swings keep this out of "clean" territory |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Credit-quality deterioration (GNPA 0.47%→0.99%, NNPA ~5x, impairment charge +207%) | High | Quarterly GNPA/NNPA trend, Stage 3 coverage ratio, write-off run-rate | Already crystallising in FY25; watch FY26 Q1-Q2 for trend continuation |
| Pragati Finserv subsidiary loss (−₹29.39 Cr, 85.7% net worth erosion) and its impact on the Pragati CGU goodwill headroom (₹20.85 Cr carrying value) | Medium-High | Pragati standalone results each quarter; any goodwill impairment trigger disclosure | Next annual impairment test (FY26) or interim trigger if losses continue |
| Operational/collections strain (complaints +930-1000%, fraud ₹1.18 Cr staff-driven, attrition assumption 38.1%) | Medium | Complaints trend, ombudsman referrals, fraud instance count next year | Ongoing; a governance/franchise risk rather than a single-quarter event |
| Regulatory ECL-model risk (FLDG exclusion precedent) | Medium | Any further RBI directives on ECL methodology; residual ₹12.06 Cr FLDG roll-off in Q1FY26 | Already partly resolved; residual amount confirms in Q1FY26 |
| Floating-rate funding exposure (~71% of liabilities variable-rate) combined with heavy bank-term-loan concentration (69.03% of total liability) | Medium | Rate-reset sensitivity (100bp = ₹69.59 Cr impact), funding-source diversification | Any rate-cycle upswing or bank-funding-line tightening |
| Real estate sector exposure growth (+84.7% YoY vs ~15% book growth) | Low-Medium | Sector-wise NPA emergence in residential/commercial real estate book | Medium-term (12-24 months), sector-cycle dependent |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Please name the specific counterparty(ies) behind the ₹305.78 Cr "loans and advances to firms/companies in which directors are interested" that was fully eliminated in FY25 (Note 76) — what was the commercial rationale for lending of this scale to director-interested entities, and was this pre-IPO cleanup?
2. Given Pragati Finserv's swing to a ₹29.39 Cr consolidated loss and 85.7% net-worth erosion in FY25 (Note 22, consolidated), was the Pragati CGU goodwill impairment test (Note 81, 30% discount rate / 4% terminal growth, headroom ₹34.35 Cr) re-run using FY25 actuals as a triggering event, and if not, why not?
3. What is driving the ~930-1000% surge in customer complaints and the 38.1% staff-attrition assumption in the FY25 gratuity valuation — is this linked to the "Staff Interaction/Collection related" complaints category specifically, and what remediation, if any, is underway?
4. Note 3k states the Company "makes annual contributions to gratuity funds established as trusts," yet Note 40 shows ₹0 fair value of plan assets in both FY24 and FY25. Please reconcile: is the plan actually funded via trust, or does the accounting-policy text need correction?
5. What is driving the Level 3 fair-value discount on the amortised-cost loan book narrowing from 24.3% (FY24) to 7.9% (FY25) — a discount-rate/cost-of-funds assumption change, or a credit-quality re-rating — and separately, can management reconcile the two different FY25 Net NPA ratios disclosed (0.39% in Note 68(a) vs 0.43% in the regulatory ratio-analysis note)?

### E. NOTES-BASED RED FLAGS

- **Regulator-forced ECL correction** (FLDG exclusion, ₹68.35 Cr Q4FY25 hit, Auditor's Emphasis of Matter) — direct evidence the Company's own ECL model had embedded an impermissible credit-enhancement assumption until RBI intervened.
- **Standalone-consolidated earnings divergence not flagged by the Company**: +22.3% standalone PAT growth vs −5.2% consolidated PAT, driven by an unremarked-upon Pragati Finserv loss swing; the goodwill test for that same subsidiary shows no evidence of having been revisited against the FY25 loss.
- **Operational-strain triangulation across three independent notes** (complaints +930-1000%, fraud 29 instances/₹1.18 Cr staff-driven, attrition assumption 38.1%) with no corresponding qualitative management discussion found in the notes themselves.
- **Internal document inconsistency**: gratuity accounting policy text contradicts the actual (unfunded) plan-asset disclosure, identically in both standalone and consolidated notes.
- **Two unreconciled Net NPA ratios** in the same annual report (0.39% vs 0.43%), found only on the pattern re-read — a disclosure-clarity, not a numerical-error, flag.
- **Aggressive revenue-recognition structure typical of the NBFC assignment model** (upfront gain-on-sale) with an early deterioration signal (EIS Stage 3 balance tripling) that has not yet flowed through to a writedown.

No evidence found of: outright earnings management via reserve manipulation, off-book related-party diversions, covenant breaches, MSME non-compliance, or going-concern doubt.

### F. ONE-LINE NOTES VERDICT

The notes reveal **moderate** accounting practices. Key concern: a regulator-forced ECL correction (FLDG exclusion) combined with an unremarked standalone-vs-consolidated PAT divergence driven by the Pragati Finserv subsidiary's swing to loss. Key strength: exceptionally granular, internally consistent borrowings/funding disclosure (148 loan tranches, no covenant breaches, de-levering balance sheet) and a genuine broadening of ECL coverage on the performing book. Overall accounting quality: 6/10.

---

```yaml
stage: B02-notes
company: "NORTHARC"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps: []
flags:
  - {type: FLAG-CASH, reason: "Loan-book asset quality (the NBFC analog to receivables/working-capital) deteriorated sharply in FY25: GNPA ratio doubled 0.47%->0.99%, Net NPA ratio ~4-5x'd (0.09%->0.39-0.43%, two unreconciled figures in the document), impairment P&L charge +207% YoY (Rs378.53 Cr vs Rs123.14 Cr), Stage 3 provision coverage fell from ~82-84% to ~68%, and this required a regulator-forced (RBI) exclusion of FLDG credit enhancements from the ECL model, Rs68.35 Cr already absorbed in Q4FY25 PBT (Note 83/49, Auditor's Emphasis of Matter)."}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "RBI-directed FLDG exclusion from ECL model: Rs80.41 Cr total impact, Rs68.35 Cr absorbed in Q4FY25 PBT; flagged as Auditor's Emphasis of Matter", note_ref: "Note 83 standalone / Note 49 consolidated, p.261/380", rating: "red flag", why: "Regulator-forced correction is direct evidence of prior ECL-model aggressiveness"}
  - {rank: 2, finding: "Consolidated Group PAT fell 5.2% YoY (Rs301.32 Cr vs Rs317.69 Cr) while standalone PAT rose +22.3%, driven by Pragati Finserv swinging from +Rs19.55 Cr profit to -Rs29.39 Cr loss, net worth eroded 85.7%", note_ref: "Note 22 consolidated, p.353", rating: "red flag", why: "Standalone-only PAT reading materially overstates true Group earnings momentum; Pragati CGU goodwill test not shown re-run against this loss"}
  - {rank: 3, finding: "Impairment on financial instruments (P&L) up 207% YoY (Rs378.53 Cr vs Rs123.14 Cr); GNPA ratio doubled 0.47%->0.99%; Stage 3 provision coverage fell ~82-84%->~68%", note_ref: "Notes 27, 36(i), 68-69, p.199-230", rating: "red flag", why: "Largest single P&L swing item in the notes; core credit-quality deterioration"}
  - {rank: 4, finding: "Customer complaints up ~930-1000% YoY (91->938 headline; grounds-table 250->1,124) vs ~15% loan book growth; complaints pending year-end 1->129", note_ref: "Note 72, p.243-244", rating: "red flag", why: "Magnitude mismatch vs book growth signals operational/collections strain unaddressed in MD&A"}
  - {rank: 5, finding: "Basic EPS fell 28.2% (Rs31.45->Rs22.59) despite PAT +22.3%, entirely from IPO + CCPS-conversion dilution (weighted avg shares +70.3%)", note_ref: "Note 32, p.217", rating: "red flag (investor-facing optical, not earnings-quality)", why: "Visible optical negative on trailing-EPS screens; one-time capital-structure effect"}
  - {rank: 6, finding: "Fraud disclosure: 29 instances, Rs1.18 Cr, predominantly staff cash-handling (25 of 29, Rs1.10 Cr), no prior-year comparative given", note_ref: "Note 51, p.236-237", rating: "watch", why: "Third independent data point reinforcing an operational-control-strain theme alongside complaints and attrition"}
  - {rank: 7, finding: "Related-party lending fully unwound in one year: loans to subsidiaries Rs100.98 Cr->Nil; loans to director-interested firms Rs305.78 Cr->Nil, no counterparty named", note_ref: "Note 76, p.248", rating: "watch", why: "Large, unexplained pre-IPO-adjacent related-party lending base eliminated with no disclosed rationale"}
  - {rank: 8, finding: "Gratuity accounting policy states annual contributions to trust-funded plans; actual disclosure shows Rs0 plan assets both years, in both standalone and consolidated notes", note_ref: "Note 3k vs Note 40, p.156/222", rating: "watch", why: "Internal document inconsistency; proxy for note-maintenance rigour"}
  - {rank: 9, finding: "FVOCI loan book fair-value markdown: OCI reserve fell Rs21.76 Cr (Rs37.38->Rs15.62 Cr); Level 3 gains-through-OCI swung -Rs28.51 Cr vs +Rs19.39 Cr prior year", note_ref: "Note 20(g), 35, p.209-210", rating: "watch", why: "Consistent with rising credit stress in the FVOCI-classified loan segment"}
  - {rank: 10, finding: "Stage 1 provision +199% YoY (coverage 0.58%->1.53%) and Stage 2 provision +281% YoY (coverage 9.36%->18.19%) - broader provisioning build than Stage 3 alone", note_ref: "Note 36(i)A, p.215-216", rating: "watch (mitigant)", why: "Partial offset to the flat-LGD concern; shows genuine conservatism build across the performing book"}
  - {rank: 11, finding: "Level 3 fair value discount on the amortised-cost loan book narrowed sharply from 24.3% (FY24) to 7.9% (FY25); driver not disclosed", note_ref: "Note 35(A), p.209-210", rating: "watch", why: "Large, undisclosed swing in an unobservable-input DCF valuation"}
  - {rank: 12, finding: "ECL LGD is a flat 65% Basel II FIRB-recommended assumption, not empirically modelled, across a diversified secured/unsecured book", note_ref: "Note 36(i)A, p.228", rating: "watch", why: "Simplifying convention whose conservatism cannot be independently verified from disclosure"}
  - {rank: 13, finding: "New Rs267.31 Cr related-party-managed AIF exposure from zero, plus a further Rs15.00 Cr AIF application money pending allotment", note_ref: "Notes 8, 42, 43, 53, 9; p.168-169, 231-232, 238", rating: "watch", why: "Concentration plus related-party-manager risk combined"}
  - {rank: 14, finding: "EIS (Excess Interest Spread) receivable Stage 3 balance more than tripled (Rs0.53 Cr->Rs1.71 Cr, +219%) even as the aggregate EIS balance stayed flat", note_ref: "Note 9.1, p.169", rating: "watch", why: "Growing share of upfront-booked gain-on-assignment income sits against now-delinquent pools"}
  - {rank: 15, finding: "Two different FY25 Net NPA ratios disclosed without cross-reference: 0.39% (Note 68(a), net-advances basis) vs 0.43% (regulatory ratio note, term-loans-only basis)", note_ref: "Note 68(a) vs ratio-analysis note, p.242/~254", rating: "watch", why: "Directionally consistent but numerically unreconciled; found only on pattern re-read"}
red_flags:
  - "Regulator-forced ECL correction (FLDG exclusion), Auditor's Emphasis of Matter, Rs68.35 Cr Q4FY25 PBT hit"
  - "Standalone-consolidated PAT divergence (+22.3% vs -5.2%) not flagged by the Company; Pragati CGU goodwill test not shown re-run against the FY25 subsidiary loss"
  - "Operational-strain triangulation across complaints (+930-1000%), fraud (Rs1.18 Cr staff-driven), and attrition assumption (38.1%), with no corresponding management discussion found in the notes"
  - "Gratuity accounting policy text contradicts the actual unfunded plan-asset disclosure, identically in standalone and consolidated notes"
  - "Two unreconciled Net NPA ratios (0.39% vs 0.43%) in the same annual report"
questions_for_mgmt:
  - "Name the counterparty(ies) behind the Rs305.78 Cr loans to director-interested firms eliminated in FY25 (Note 76) and the commercial rationale."
  - "Was the Pragati CGU goodwill impairment test (Note 81) re-run using FY25 actuals given the subsidiary's Rs29.39 Cr consolidated loss and 85.7% net-worth erosion?"
  - "What is driving the ~930-1000% complaints surge and the 38.1% attrition assumption, and is it linked to the Staff Interaction/Collection-related complaints category?"
  - "Reconcile Note 3k's gratuity-trust-funding policy language against Note 40's Rs0 plan-assets disclosure in both years."
  - "What drove the Level 3 loan-book fair-value discount to narrow from 24.3% to 7.9% YoY, and can the two different FY25 Net NPA ratios (0.39% vs 0.43%) be reconciled?"
receivables_trend: "Not a meaningful metric in its trade-receivables form for an NBFC (trade receivables actually improved Rs14.38 Cr->Rs12.02 Cr, immaterial). The analogous asset-quality metric, loan-book credit quality, is DETERIORATING: GNPA ratio 0.47%->0.99%, Net NPA ratio 0.09%->0.39-0.43% (two figures disclosed, unreconciled), gross Stage 3 NPA Rs52.03 Cr->Rs127.83 Cr, net NPA rupee amount Rs9.61 Cr->Rs49.18 Cr (+412%), impairment P&L charge Rs123.14 Cr->Rs378.53 Cr (+207%), Stage 3 provision coverage ~82-84%->~68% (Notes 27, 36(i)A, 68-69, p.199-230, 241-242)."
restatements_found: []
going_concern_language: "NONE. Standard affirmative language only, identical across standalone and consolidated accounting policies (Note 2/equivalent): \"prepared on a going concern basis... Management is satisfied that the Company/Group shall be able to continue its business for the foreseeable future and no material uncertainty exists that may cast significant doubt on the going concern assumption\" (PDF p.144 standalone / p.~20507 consolidated). No going-concern qualification or Key Audit Matter in either Auditor's Report."
```
