# STAGE 2 NOTES, PASS 3 AND CONSOLIDATION: JLHL, run 2026-11-12

Source: inputs/annual-report/Annual_Report_2026.pdf (text: Annual_Report_2026.txt). Detail and anchors live in outputs/reports/02-notes-pass1.md and 02-notes-pass2.md (pass 2 section 0 corrections applied here).
UNIT RULE: INR million (Rs mn; 10 million = 1 Crore) as printed on the face of the statements, unless marked "Rs" or "%". Not converted. S = Standalone, C = Consolidated.
B00 input_gaps carried into the block. None of them touches the AR notes.

## PASS 3: PATTERN PASS

PASS 3: NO MATERIAL NEW FINDINGS

The pattern re-read (contradictions, statement mismatches, vague disclosure, restated priors, post-balance-sheet events, going concern) re-confirmed items already in passes 1 and 2. It adds no new item. The patterns, with where each sits:
- Contradictions between notes: gratuity "unfunded" vs plan assets (P1 1.11); CP "amortised cost" vs "FVTPL" (P1 6.2); "insignificant borrowings" vs Rs mn 5,085.27 floating (P1 7); stale "fixed deposits" and "bank deposits" credit text vs CP pool (P2 1.4); 961 vs 1,248 beds (P1 11.1).
- Notes vs statements: CWIP 1,286.99 vs 1,292.12 (P1 11.3); ECL P&L 12.37 vs CF 9.49 (P1 4); lease payments CF vs note (P1 11.3); S vs C pay for Dr. Ankit Thakker FY25 25.92 vs 31.91 (P1 2.1, P2 5.1).
- Deliberately thin disclosure: borrowing-cost capitalisation amount, capital commitments, BKC price, covenants, ECL matrix rates, impairment inputs, guarantee fee, loan interest rates (all NOT FOUND IN DOCUMENT).
- Restated priors: FY25 comparatives re-cut with only "regrouped" wording (P1 11.2).
- Events after balance sheet date: interim dividend Rs 1 per share declared 15-May-2026 (Rs mn 65.57); Medulla scheme pending NCLT. Stock split approved 15-May-2026 is NOT FOUND IN DOCUMENT in the AR text.
- Going concern: grep of the AR text finds only the standard basis-of-preparation line ("prepared on going concern basis under historical cost", lines 10139 and 13882) and the auditor's standard responsibility paragraphs. No stress or uncertainty language. Directors' Report: no tribunal orders impacting going concern (line 6399).

---------------------------------------------------------------------
## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Borrowing-cost capitalisation, pre-operative cost and Dombivli depreciation start are unquantified. Parent term-loan interest expensed is Rs mn 15.15 on a loan that rose 750.00 to 2,610.32. Dombivli capitalised Rs mn 3,881.3. Expensed interest equals about 0.9 month at the full balance [INFERENCE]. | S Note 31 p.167; S Note 1.1 p.156; Policy C.4 pp.145-146 | 🔴 | The profit squeeze (D&A +305.57, finance cost +219.57, C, Rs mn) cannot be split into expensed and capitalised cost. FY27 carries a full-year charge. |
| 2 | No capital-commitment disclosure. Capital advances Rs mn 1,169.36 (S) vs 3.69. Three projects named (Pune 500, Mira Road 300, BKC 400 beds). BKC price and schedule absent. | S Note 37B p.171; S Note 4 p.158; S Note 1 A p.144 | 🔴 | Remaining capex and funding need cannot be sized from the notes. |
| 3 | FY25 comparatives re-cut with no restatement note: C revenue +408.57 (+3.2%), PBT +29.75, PAT +2.54, total assets +308.61; about Rs mn 3,980 moved from cash into current investments. | S Note 37R p.182; C Note 36R p.235 | 🔴 | Growth reads +15.2% on the AR26 base and +18.9% on the AR25 base. Base choice drives every trend. |
| 4 | HMIS billing software lacks database-level audit trail; backup logs missing for another system; management calls controls effective. | S Note 37Q p.182; Auditor paras 19.2, 19.6, 20.8 pp.129-132 | 🔴 | HMIS is the revenue source system. |
| 5 | Receivables: gross +72.3% vs revenue +15.2%. Unbilled Rs mn 191.07 (24% of gross). Net days 12.1 to 18.4. ECL equals the credit-impaired bucket only; good balances carry no allowance. Impaired under 6 months 5.2x. KAM. | C Note 7 p.212; S Note 7 pp.159-160 | 🟡 | Cash conversion signal; feeds FLAG-CASH. |
| 6 | Debt Rs mn 5,085.27 (C), all floating at Repo + 200 bps. 92.5% repays after year 3. Covenants not disclosed. Net cash only Rs mn 353.45 if CP counts (vs 2,763.67). | C Note 14 p.215; C Note 36H p.229; C Note 35 p.222 | 🟡 | Funding of the build and the finance-cost run-rate. |
| 7 | 89.3% of group liquid assets (Rs mn 4,857.04) is one issuer's commercial paper (JM Financial Services). Credit-risk text says bank deposits. | C Note 6 p.211; C Note 35 p.221 | 🟡 | Concentration in the liquidity buffer; negative carry vs Repo + 200 bps debt [INFERENCE]. |
| 8 | JHPPL: loss Rs mn 34.29 (FY25 +88.01). Parent cost 939.00 vs net assets 242.60. No impairment inputs. Loan 293.37 with no stated rate. Guarantee 2,500 not in the contingent table, described as given in FY26 for a loan outstanding at March 2025. | C Note 36D p.226; S Note 2 p.158; S Note 37B p.172 | 🟡 | Parent exposure to the subsidiary is about 3,700 (cost, loan, guarantee, derived 939.00 + 293.37 + 2,500 = 3,732.37). |
| 9 | Cost lines: doctor fees 24.27% of revenue (23.44%); inventory days 48.7 (37.8); patient food +106%, insurance +115%, rates +61% (S); other income 16.3% of PBT; pre-other-income profit -4.0%. | C Notes 29, 5, 25; S Note 33 p.168 | 🟡 | Quality of the earnings under the squeeze. |
| 10 | Leasehold-land ROU addition Rs mn 221.41 with no lease liability (upfront payment); payee and plot NOT FOUND. | S Notes 1.2, 37J | 🟡 | Possible BKC or other site payment; unlinked. |
| 11 | Payables +38.3%; MSME dues +188% (or +209% on ageing base); Rs mn 69.90 MSME past due with nil MSMED interest; capital creditors reclassified out of payables. | C Notes 20, 36E pp.216, 228 | 🟡 | Working-capital stretch plus compliance exposure. |
| 12 | Subsidiary revenue +24.7% vs parent +13.0%; S FY25 profit carried Rs mn 47.16 pharmacy-partnership contribution that eliminates on consolidation. | S Note 25 p.166; C Note 24 p.218 | 🟡 | Standalone trend is not a clean read of the core. |
| 13 | Promoter pay S +25.0% (Ankit Thakker S 39.00 vs 25.92); S vs C disagree on his FY25 pay and on lease income lines; Anshul Sethi in no related-party list; RPTs 1.15% of revenue. | C Note 36K p.232; S Note 37K p.179 | 🟡 | Control quality of RPT disclosure. |
| 14 | Joint auditors from FY26; audit fee +80% (S). One partnership firm's loss Rs mn 2.62 on unaudited accounts. | S Note 33 p.168; Auditor para 17 | 🟡 | Auditor change plus control finding in one year. |
| 15 | Gratuity assets shown gross; Labour Codes exceptional Rs mn 48.87 (C) vs gratuity past service cost 37.52, gap 11.35 unreconciled; leave-encashment liability NOT FOUND. | S Note 37A p.171; S Note 37C; S Note 4 p.158 | 🟡 | Presentation; one-time item not fully traced. |

### B. ACCOUNTING QUALITY SCORE: 6 / 10

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Accrual for undischarged inpatients; HMIS audit-trail gap; unbilled 191.07 newly shown; no payer-class split |
| Expense capitalisation honesty | 4 | Capitalised interest, pre-operative cost and commitments not quantified in a year that capitalised 3,881.3 |
| Provisioning adequacy | 5 | ECL on impaired bucket only; no overlay amount; no litigation provision (contingents only 0.32% of net worth) |
| RPT fairness | 7 | RPTs 1.15% of revenue; CARO and Sec 177/188 clean; S vs C inconsistencies and the guarantee wording |
| Disclosure transparency | 4 | Re-cut priors with "regrouped" only; many NOT FOUND items; stale boilerplate in risk notes |
| Consistency with prior years | 5 | Policies unchanged, but comparatives re-cut and FY25 ageing format changed |
| OVERALL | 6 | No fraud, default or policy change; weaknesses are disclosure gaps and control findings |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Full-year Dombivli depreciation and interest after capitalisation stops | High | Capitalised-interest amount; FY27 quarterly D&A and finance cost | FY27 quarters, already running |
| Undisclosed capital commitments and BKC payment schedule | High | Commitments note in next filing; capital advances | FY27 to FY28 |
| Floating debt Rs mn 5,085.27, 92.5% after year 3, covenants unseen | Medium | Repo moves; covenant disclosure; DSCR 36.58 (C) | FY27 onward |
| CP concentration in one issuer (89.3% of liquidity) | Medium | Issuer rating; maturity; yield | Any quarter |
| Receivables and unbilled build; ECL on impaired only | Medium | Ageing next half; impaired under 6 months; unbilled | Next 2 to 4 quarters |
| Revenue-system control gap (HMIS) | Medium | Audit-trail fix; next auditor report | FY27 audit |
| JHPPL exposure (~3,732 derived) with loss and no impairment inputs | Medium | JHPPL results; guarantee release test (Debt/EBITDA below 3.5x) | FY27 to FY28 |
| Comparative re-cut hides trend | Medium | Management reconciliation of AR25 to AR26 base | Next results |
| MSME interest not provided | Low | MSMED interest line | FY27 audit |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. How much borrowing cost, and how much pre-operative expense, did you capitalise into Dombivli in FY26 and FY25, at what rate, and from what date did Dombivli depreciation start?
2. What are the capital commitments at 31-Mar-2026 for Pune, Mira Road and BKC, what was paid to MMRDA, and what do the Rs mn 1,169.36 capital advances and the Rs mn 221.41 leasehold addition relate to?
3. Why were FY25 comparatives re-cut (revenue +408.57, about 3,980 from cash to investments), and can you reconcile the AR25 and AR26 figures line by line?
4. Why does the ECL allowance equal the credit-impaired bucket only, what overlay did the auditor's KAM refer to, and what drove unbilled revenue of Rs mn 191.07 and impaired receivables under 6 months to 5.2x?
5. What are the HDFC loan covenants and instalment schedule for both loans, why was the Rs mn 2,500 JHPPL guarantee described as given in FY26 for a loan outstanding in March 2025, and what is the rate and yield on the commercial paper held against it?

### E. NOTES-BASED RED FLAGS

- Earnings management: none proven. Exposure sits in capitalised interest (inferred, unquantified) and the unquantified Dombivli start date. A rise of Rs mn 131.46 in gain on sale of investments plus Rs mn 245.15 interest income carries other income to 16.3% of PBT; pre-other-income profit fell 4.0%.
- Aggressive accounting: ECL on impaired bucket only; gratuity assets grossed up; guarantee not in the contingent table.
- Undisclosed risk indicators: capital commitments, covenants, BKC price, guarantee fee, loan interest rates, impairment inputs.
- Control: HMIS audit-trail gap in the billing system, with unmodified IFC opinion.
- Comparability: FY25 re-cut; payables and ageing formats changed.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices. Key concern: the build year's capitalised interest, pre-operative cost and capital commitments are not quantified, so the profit squeeze cannot be split, and FY25 comparatives were re-cut without a restatement note. Key strength: no policy change, no covenant default, no going concern language, contingent liabilities 0.32% of net worth, RPTs 1.15% of revenue. Overall accounting quality: 6/10.

### Load-bearing facts status
1. Dombivli ramp: capitalised Rs mn 3,881.3 (S Note 1.1 p.156). Start and depreciation dates NOT FOUND IN DOCUMENT. Three filed signals fit a late-in-year start [INFERENCE].
2. Profit squeeze: D&A 876.40 vs 570.83; finance cost 326.63 vs 107.06 (C, Rs mn). Capitalised amount NOT FOUND IN DOCUMENT.
3. Capex funding: gross debt C Rs mn 5,085.27 (brief's Rs 584 Cr reads as debt plus leases, 5,842.40 Rs mn). Capital commitments, BKC price NOT FOUND IN DOCUMENT. Group FCF (2,341.37) in FY26 (derived).
4. Occupancy and ARPOB: no definitions in the notes; AR pp.20 and 46 only (61.20% vs 65.30%; Rs 67,700 vs Rs 60,600).

```yaml
stage: B02-notes
company: "JLHL"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "collector warning: shareholding/ was empty; REPAIRED at /step1 with NSE XBRL pattern for 30-Sep-2026 (one quarter, no pledge trend series). No effect on notes."
  - "screener export sheets came out empty (formulas without cached values); only the four Data_Sheet CSVs are populated. No effect on notes."
  - "results PDFs and rating PDF absent at collection; REPAIRED at /step1 (three results filings, two ICRA rationales). Results text layers partly garbled; use page images. No effect on notes."
  - "research: EMPTY; other: EMPTY. No broker notes. No effect on anchored evidence."
  - "prospectus: RHP 30-Aug-2023 present; final Prospectus 11-Sep-2023 not in corpus."
  - "announcements: collector fetched ~5 weeks from BSE; /step1 added nine NSE filings; set is a selection, not the complete 12-month record."
  - "two scanned announcements (Secretarial_Compliance_Report_FY26, newspaper Q2 results publication); no tesseract; neither is anchored evidence."
  - "annual-report: FY26 (237 pages, primary) and FY25 (106 pages, baseline) held. AR text complete in the notes range."
  - "Verifier A shadow switch not flipped by this run (claimed by another session)."
  - "NOTES-SPECIFIC NOT FOUND IN DOCUMENT: Dombivli commissioning and depreciation start dates; capitalised borrowing cost and pre-operative cost; capital commitments; BKC land price and payments; covenants; ECL matrix rates and overlay; impairment inputs; lease discount rate; interest rate on JHPPL and Medulla loans; guarantee fee; stock split in AR text; fair value hierarchy table; MAT credit and unrecognised DTA."
flags:
  - {type: FLAG-CASH, reason: "Gross receivables +72.3% (C Rs mn 792.22 vs 459.67) against revenue +15.2%; net days 12.1 to 18.4; unbilled Rs mn 191.07 newly shown; credit-impaired under 6 months 7.02 vs 1.36 (C Note 7 p.212). Allowance equals impaired bucket only."}
  - {type: FLAG-COMPARATIVES, reason: "FY25 comparatives re-cut in AR26 with only 'regrouped' wording: C revenue 13,024.02 vs 12,615.45 as filed in AR25 (Rs mn); about Rs mn 3,980 moved from cash to current investments (S Note 37R p.182; C Note 36R p.235)."}
  - {type: FLAG-CAPEX-DISCLOSURE, reason: "Capital commitments, capitalised borrowing cost and BKC land payments not disclosed in any note while capital advances reached Rs mn 1,169.36 (S) and Dombivli capitalised Rs mn 3,881.3."}
  - {type: FLAG-CONTROL, reason: "HMIS billing software without database-level audit trail; backup logs missing for another system (Auditor paras 19.2, 19.6, 20.8 pp.129-132; S Note 37Q p.182)."}
  - {type: FLAG-LIQUIDITY-CONCENTRATION, reason: "Rs mn 4,857.04 commercial paper of one issuer (JM Financial Services) is 89.3% of group liquid assets (C Note 6 p.211), against floating debt Rs mn 5,085.27."}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: true
top_findings:
  - {rank: 1, finding: "Borrowing-cost capitalisation, pre-operative cost and Dombivli depreciation start unquantified; parent term-loan interest expensed Rs mn 15.15 on debt 750.00 to 2,610.32; Dombivli capitalised Rs mn 3,881.3", note_ref: "S Note 31 p.167; S Note 1.1 p.156; Policy C.4 pp.145-146", rating: "RED", why: "Profit squeeze (C D&A +305.57, finance cost +219.57, Rs mn) cannot be split into expensed and capitalised cost; FY27 carries full-year charges"}
  - {rank: 2, finding: "No capital-commitment disclosure; capital advances S Rs mn 1,169.36 vs 3.69; Pune, Mira Road, BKC named; BKC price absent", note_ref: "S Note 37B p.171; S Note 4 p.158; S Note 1 A p.144", rating: "RED", why: "Remaining capex and funding need cannot be sized from the notes"}
  - {rank: 3, finding: "FY25 comparatives re-cut without restatement note: C revenue 13,024.02 vs 12,615.45 as filed (Rs mn); about Rs mn 3,980 cash to current investments", note_ref: "S Note 37R p.182; C Note 36R p.235", rating: "RED", why: "Growth is 15.2% on AR26 base and 18.9% on AR25 base; base choice drives trends"}
  - {rank: 4, finding: "HMIS billing software lacks database-level audit trail; management says controls effective", note_ref: "S Note 37Q p.182; Auditor paras 19.2, 19.6, 20.8", rating: "RED", why: "HMIS is the revenue source system"}
  - {rank: 5, finding: "Receivables gross +72.3% vs revenue +15.2%; unbilled Rs mn 191.07; ECL equals impaired bucket only (C 36.83)", note_ref: "C Note 7 p.212; S Note 7 pp.159-160", rating: "YELLOW", why: "Cash-conversion deterioration; no allowance on good balances"}
  - {rank: 6, finding: "Group debt Rs mn 5,085.27 all floating Repo + 200 bps; 92.5% repays after year 3; covenants not disclosed; net cash Rs mn 353.45 if CP counts vs 2,763.67", note_ref: "C Note 14 p.215; C Note 36H p.229; C Note 35 p.222", rating: "YELLOW", why: "Funding of the build and finance-cost run-rate"}
  - {rank: 7, finding: "89.3% of liquid assets (Rs mn 4,857.04) is one issuer's commercial paper; credit-risk text says bank deposits", note_ref: "C Note 6 p.211; C Note 35 p.221", rating: "YELLOW", why: "Concentration in the liquidity buffer"}
  - {rank: 8, finding: "JHPPL loss Rs mn 34.29; cost 939.00 vs net assets 242.60; loan 293.37 no rate; Rs mn 2,500 guarantee outside contingent table, described as given in FY26 for loan outstanding March 2025", note_ref: "C Note 36D p.226; S Note 2 p.158; S Note 37B p.172", rating: "YELLOW", why: "Parent exposure about Rs mn 3,732 derived (939.00 + 293.37 + 2,500)"}
  - {rank: 9, finding: "Doctor fees 24.27% of revenue (23.44%); inventory days 48.7 (37.8); patient food +106%, insurance +115% (S); other income 16.3% of PBT; pre-other-income profit -4.0%", note_ref: "C Notes 29, 5, 25; S Note 33 p.168", rating: "YELLOW", why: "Earnings quality under the squeeze"}
  - {rank: 10, finding: "Leasehold-land ROU addition Rs mn 221.41 carries no lease liability; payee and plot NOT FOUND", note_ref: "S Notes 1.2, 37J", rating: "YELLOW", why: "Upfront payment unlinked to any named site"}
  - {rank: 11, finding: "Payables +38.3%; MSME dues +188% (+209% on ageing base); Rs mn 69.90 MSME past due, nil MSMED interest", note_ref: "C Notes 20, 36E pp.216, 228", rating: "YELLOW", why: "Working-capital stretch and compliance exposure"}
  - {rank: 12, finding: "Subsidiary revenue +24.7% vs parent +13.0%; S FY25 carried Rs mn 47.16 partnership profit that eliminates in C", note_ref: "S Note 25 p.166; C Note 24 p.218", rating: "YELLOW", why: "Standalone trend is not a clean read of the core"}
  - {rank: 13, finding: "Promoter pay S +25.0%; S vs C disagree on Dr. Ankit Thakker FY25 pay (25.92 vs 31.91) and lease income; Anshul Sethi in no RPT list; RPTs 1.15% of revenue", note_ref: "C Note 36K p.232; S Note 37K p.179", rating: "YELLOW", why: "RPT disclosure control quality"}
  - {rank: 14, finding: "Joint auditors from FY26; audit fee +80% (S); one firm's loss Rs mn 2.62 on unaudited accounts", note_ref: "S Note 33 p.168; Auditor para 17", rating: "YELLOW", why: "Auditor change and control finding in one year"}
  - {rank: 15, finding: "Labour Codes exceptional Rs mn 48.87 (C) vs gratuity past service cost 37.52, gap 11.35 unreconciled; gratuity assets grossed up; leave-encashment liability NOT FOUND", note_ref: "S Note 37A p.171; S Note 37C; S Note 4 p.158", rating: "YELLOW", why: "One-time item not fully traced; presentation"}
red_flags:
  - "Capitalised borrowing cost, pre-operative cost and Dombivli depreciation start unquantified (S Note 31 p.167; Policy C.4)"
  - "No capital-commitment figure; BKC land price absent (S Note 37B p.171)"
  - "FY25 comparatives re-cut without restatement note (S Note 37R p.182)"
  - "HMIS billing audit-trail gap (S Note 37Q p.182; Auditor paras 19.2, 19.6, 20.8)"
questions_for_mgmt:
  - "How much borrowing cost and pre-operative expense did you capitalise into Dombivli in FY26 and FY25, at what rate, and from what date did Dombivli depreciation start?"
  - "What are the capital commitments at 31-Mar-2026 for Pune, Mira Road and BKC, what was paid to MMRDA, and what do Rs mn 1,169.36 of capital advances and the Rs mn 221.41 leasehold addition relate to?"
  - "Why were FY25 comparatives re-cut (C revenue +408.57; about Rs mn 3,980 from cash to investments), and can you reconcile AR25 to AR26 line by line?"
  - "Why does the ECL allowance equal the credit-impaired bucket only, what overlay did the KAM refer to, and what drove unbilled Rs mn 191.07 and the 5.2x rise in impaired receivables under 6 months?"
  - "What are the HDFC covenants and instalment schedules, why was the Rs mn 2,500 JHPPL guarantee described as given in FY26 for a loan outstanding in March 2025, and what is the CP yield against floating debt?"
receivables_trend: "deteriorating. C gross Rs mn 792.22 vs 459.67 (+72.3%) vs revenue +15.2%; net 755.39 vs 432.33; unbilled 191.07 (nil shown FY25); over 6 months 53.92 (6.8% of gross) vs 47.90 (10.4%); credit-impaired under 6 months 7.02 vs 1.36; ECL 4.65% of gross vs 5.95%; net days on year-end balance 18.4 vs 12.1 (C Note 7 p.212; Note 36L p.233)"
restatements_found:
  - "FY25 consolidated comparatives in AR26 differ from AR25 as filed (Rs mn): revenue 13,024.02 vs 12,615.45; purchases of consumables 2,581.70 vs 2,329.19; PBT 2,606.76 vs 2,577.01; profit 1,937.54 vs 1,935.00; total assets 19,357.50 vs 19,048.89. Disclosure is only 'regrouped wherever applicable' (S Note 37R p.182; C Note 36R p.235; Annual_Report_2025.pdf p.85)"
  - "FY25 standalone: cash and cash equivalents 845.39 vs 3,674.10 as filed; current investments 5,122.59 vs 1,142.68; trade payables 541.75 vs 821.56 (capital creditors 279.81 moved to other financial liabilities); professional fees 2,461.49 vs 2,523.95 (Annual_Report_2025.pdf p.63)"
  - "FY25 consolidated provisions re-split: non-current 112.21 and current 20.23 vs AR25 49.69 and 153.67 (Rs mn)"
going_concern_language: "NONE. Only the standard basis line 'prepared on going concern basis under historical cost' (S Note 1 B(ii) p.144; C Note 1 B(ii) p.196); CARO xix reports no material uncertainty on liabilities due within a year (pp.135-136)."
analyst_note: "The notes never state how much interest was capitalised into Dombivli. Pass 2 triangulated it: parent term-loan interest expensed was Rs mn 15.15, about 0.9 month at the full Rs mn 2,610.32 balance at 7.61% (the rate implied by the JHPPL loan). Rest was probably capitalised [INFERENCE, not filed]. Buildings depreciation rose Rs mn 4.94 against a 34.66 full-year equivalent, so FY26 carries a stub of depreciation and interest. Stage 10 should treat FY26 D&A and finance cost as a partial-year base. Growth base matters: AR26 re-cut gives 15.2%, AR25 filed gives 18.9%. Brief's Rs 584 Cr debt equals borrowings 5,085.27 plus leases 757.13 (Rs mn), not borrowings alone. All figures Rs mn."
```
