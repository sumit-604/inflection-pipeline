# STAGE 2 NOTES, PASS 3 AND CONSOLIDATION: SOUTHWEST, FY26 (year ended 31 Mar 2026)

Run date 2026-11-09. Source: inputs/annual-report/Annual_Report_2026.txt (20th AR). Model: claude-sonnet-5-5.
Unit: INR Lakhs on the face of the document (S p.127, C p.169). Nothing converted. Anchors: "S" standalone, "C" consolidated, page = "[page N]" marker in the .txt. "(derived)" = my arithmetic on anchored figures. "[INFERENCE]" = reading beyond the printed number.
Pass 1 detail: outputs/reports/02-notes-pass1.md. Pass 2 detail: outputs/reports/02-notes-pass2.md (its line 7 "P2-17" read as "P2-10", per the task).
Input gaps carried from B00: shareholding/ empty; screener P&L/Quarters/BS/CF sheets empty (Data_Sheet populated); no results or rating PDFs; Q2 FY27 concall not held at run date (freshness FAIL); Q3 FY26 transcript absent; announcements cover Nov 2025 to Nov 2026 only; research/ empty. None of these blocks a notes read. The AR text has two extraction gaps (S Note 41 body, S Note 46 segment table); the verifier should open the PDF for both.

## PASS 3: PATTERN PASS (contradictions, mismatches, vagueness, restatements, post-balance-sheet events, going concern)

### P3-1. Going concern language: one subsidiary, rescued by an unquantified parent letter (RED for opacity)
- Consolidated auditor's report, "Material Uncertainty Related to Going Concern" (C p.159): SWR "accumulated losses amounting to INR 314.88 Lakhs ... fully eroded the net worth ... current liabilities exceeded its current assets by INR 266.40 Lakhs ... material uncertainty that may cast significant doubt ... results prepared on a going concern basis as the Company has letter of financial support from Holding Company."
- The parent's own auditor paragraph (CARO clause xix, S) finds no material uncertainty for the parent (S, CARO xix, line-level text near p.141 of the standalone auditor's report; page marker not resolved in my read).
- The letter appears in no note: not in Note 42 contingencies (C pp.185-186), not in the RPT note (S p.148), not in Note 63 on s.186. Amount, term, and whether it is a comfort letter or a binding guarantee: NOT FOUND IN DOCUMENT.
- Board's report going-concern section (line-level p.52-53 area) states no material event affecting the company's going concern status. It says nothing on the SWR paragraph. [INFERENCE] The parent funds SWR in substance: 410.34 interest-free loan (Pass 2 P2-1) plus an open-ended letter.

### P3-2. Post-balance-sheet event sits in the Board's report, not in the notes (YELLOW)
- Board's report (p.41-42): on 10 Jul 2026 the Board allotted 28,21,411 equity shares on conversion of all warrants, against balance consideration of Rs 279,742,900 (= 2,797.43 Lakhs, derived; ties to Pass 1 balance due 2,797.43).
- The notes carry no events-after-balance-sheet disclosure (S and C: NOT FOUND IN DOCUMENT). Note 19 S (p.134) still shows the warrants as outstanding with the 18-month window.
- This confirms, inside the AR itself, the announcement-based finding in Pass 2 P2-10. Net effect for the notes: FY26 diluted EPS 10.09 (Note 40 S p.139) is the last pre-conversion print; post-allotment share count 3,26,51,422 (announcements, Pass 2).
- Contradiction inside the AR: Note 18(a) S FY25 column still shows promoter holdings 42.36% and 24.80% (S p.132) against 39.62% and 23.20% in Note 18(e) (S p.133) (Pass 2 P2-10).

### P3-3. Management's ratio commentary contradicts the figures it explains (RED for disclosure quality)
All S p.154 (Note 51) unless stated.
- Trade payables: commentary says "Better cash flows due to better margins have led to reduction in Trade Payables". Payables rose to 2,387.27 from 1,823.80 (+30.9%, derived; Note 26 S p.136). Cash flow shows payables +563.48 (S p.115). Turnover fell 9.79 to 7.33, which is a longer payment cycle (Pass 1 Section 8). Only MSME payables fell (462.34 to 186.21); "Others" rose 1,361.46 to 2,201.06 (derived +61.7%).
- Receivables: MD&A (p.62) says the debtor ratio shows "Stable collections profile across our public sector and corporate client base". Note 51 shows receivable turnover 2.55 vs 2.74 (-7.20%); billed receivables +101% (Pass 1 Section 4).
- ROCE: Note 51 commentary says profits rose "without corresponding increase in capital employed". Net PPE +46.9%, borrowings +24.9%, equity +17.9% (Pass 2 P2-16, derived).
- Basis drift between sections: MD&A ROCE 23.00% vs 16.00% prior (p.62); Chairman's letter "16% to 23%" (p.6); Note 51 S ROCE 22.06% vs 11.94% (S p.154). MD&A ROE 16.21% (p.62) vs Note 51 ROE 16.46% (S p.154). MD&A net profit margin 13.58% (p.62) vs Note 51 12.68% (S p.154). 13.58% fits consolidated PAT 3,302.70 / revenue 24,302.17 (derived); 12.68% fits standalone 3,080.05 / 24,292.95 (derived). The MD&A does not say it switched to the consolidated basis. The prior-year ROCE differs (16% vs 11.94%) with no bridge.
- MD&A interest coverage 5.90 (PY 3.28) and "Gross Margin 29% vs 23%" (p.62-63) have no matching line in Note 51. Basis: NOT FOUND IN DOCUMENT.

### P3-4. Borrowing notes contradict each other on rate type (YELLOW, Pass 1 Finding 6 sharpened)
- Note 20 S (p.134) and Note 25 S (p.135) say term loans carry rates fixed at drawdown (8.00-9.75%). Term loans (non-current 1,599.44 + current maturities 2,024.84) = 3,624.28 (Note 20 S p.134; derived sum).
- Note 49 S (p.152-153): fixed-rate borrowings only 1,132.21 (PY 1,184.23); floating 6,729.13 (PY 5,107.16). If all term loans were fixed, fixed borrowings would be at least 3,624.28 (derived). The gap of 2,492.07 (derived) is the amount that cannot be fixed under Note 20 and floating under Note 49 at once.
- The interest-rate sensitivity (33.65 for 50 bp) uses the floating figure (S p.153). Consolidated fixed/floating (1,132.71 / 6,729.13; C p.198) differs from standalone by 0.50, which equals the consolidated related-party loan (Note 26 C p.181) (derived).
- Implied interest 10.99% on average debt (Pass 1) against the stated 8.00-9.75%. All three disclosures cannot be right together.

### P3-5. Cash-flow line vs balance-sheet movement (YELLOW, derived)
- Cash flow "(Increase) in trade receivables (4,456.25)" (S p.115; line text at AR text line 6247). Gross receivable movement per Note 12 S (p.131) is 11,832.46 less 7,534.67 = 4,297.79 (derived). Difference 158.46 (derived). The cash-flow line may bundle other receivable heads; the bridge is NOT FOUND IN DOCUMENT.
- PY cash flow line (1,950.76) against PY gross movement: FY24 receivable base NOT FOUND IN DOCUMENT in these notes, so not tested.

### P3-6. Remuneration table prior-year mismatch and a driver revealed (YELLOW)
- Consolidated RPT table prints remuneration 420.49 (PY 263.13) (C p.194, AR text line 12072). Compensation table short-term benefits 420.49 (PY 236.13) (S p.149). The PY digits are transposed (263.13 vs 236.13); 236.13 + sitting fee 6.58 = 242.71, which ties to the standalone total (Pass 1 Section 2c).
- Board's report (p.51) gives the cause of the rise: "sales commission availed by CMD and JMD during the year which was although part of their remuneration yet was not being availed in yester years due to cash flow constraints". The note does not disclose the commission basis or any approved ceiling. The auditor confirms Section 197 / Schedule V compliance (C p.163; Pass 2 P2-18).
- [INFERENCE] The promoters held back pay in a cash-constrained year (FY25) and took it in FY26 when profit rose, while FY26 CFO fell to 1,233.87 (Cash flow S p.115). The confirming observation is the commission formula in the shareholder approval, which is not in the notes.

### P3-7. Samit JV: net assets and loss share do not reconcile (YELLOW, extends Pass 2 P2-4)
- Net assets 39.99 (PY) to (13.51) (FY26) = fall of 53.50 (derived). Reported loss is 17.71 (Note 51 C p.201). The other 35.79 fall (derived) has no disclosed cause (distribution, capital reduction, or other).
- Equity-method policy (C p.171, text near line 10281-10285): further losses stop at the investment unless the group has obligations or made payments on the JV's behalf. Group carrying is positive at 10.70 against 80% of net assets of (10.81) (derived). Either the group has made payments for the JV (a related-party loan not shown) or the carrying is overstated by 21.51 (derived). Which: NOT FOUND IN DOCUMENT.

### P3-8. Deliberately thin disclosure, ranked by what is withheld (pattern list)
Compare the detail on gratuity (a 4-page note) with these single-line or absent items:
1. The 1,100.00 loan (PY 950.00) to an unnamed KMP-influenced enterprise: borrower, rate, tenor, purpose.
2. The SWR support letter.
3. E&E policy and impairment trigger for 1,930.58.
4. Names of the three customers holding 72.27% of revenue.
5. Sub-contractor identity behind 8,109.98 (+219%).
6. "Sundry assets written off" 197.79 (4.5x) and "Bad debt written off 119.32" in FY25 group.
7. Contingent liability probability, with the GST 397.59 demand new.
8. Covenant terms, while Note 49c (S p.153) confirms covenants exist.
9. Events after the balance sheet date.
Full register of absences: Pass 1 closing register.

### P3-9. Restatements and reclassifications (none quantified)
- "Previous year figures have been re-grouped/re-classified wherever necessary" (Note 66 S p.157; C Note 65, AR text line 12718). No amounts and no line items named.
- Tests I could run for hidden regrouping: FY25 receivable ageing 7,534.67 and net 7,433.89 (Note 12 S p.131) tie to the face of the balance sheet comparatives as printed; Note 39 S ECL 87.18 ties to the allowance movement (Pass 1). FY25 inventory opening 4,342.36 and closing 4,624.04 tie to Note 33 S. I found no number that fails a tie because of regrouping.
- Mismatches that look like uncorrected errors, not restatements: 42.36%/24.80% FY25 shareholding in Note 18(a); consolidated Note 20 equity total 17,079.98 vs 14,079.98; OMR FY25 asset 0.41 vs 1.16 million against one INR value 91.09; lease undiscounted total equal to carrying amount; sensitivity table year labels (Pass 2 P2-16).
- Result: restatements_found stays empty; the mismatch list goes to the verifier as hygiene items.

PASS 3 outcome: not empty. Nine pattern findings (P3-1 to P3-9); P3-1, P3-3 and P3-4 change the consolidation.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Cash conversion weak under rig capex. Gross receivables 11,832.46 vs 7,534.67 (+57.0%) on revenue +35.6%; billed receivables 9,218.67 vs 4,576.59 (+101%); customer advances 342.23 to nil; cash and equivalents 88.81 vs 1,824.50; CFO 1,233.87 vs PAT 3,080.05; capex 4,254.36 plus E&E 499.77. | Note 12 S p.131; Note 30 S p.136; Cash flow S p.115 | RED | Load-bearing fact 4. Profit is not turning into cash; working-capital lines +740.76 and margin-money FD release funded the gap (P2-7, P2-9). Feeds FLAG-CASH. |
| 2 | Three customers = 72.27% of revenue (PY 48.00%), names withheld; credit-risk text rates concentration "low" because customers are PSUs. | Note 46 S p.146; Note 49 S p.150 | RED | Load-bearing fact 2. Concentration rose 24 points in a year in a business whose receivables are stretching. |
| 3 | SWR: net assets (264.94), auditor going-concern emphasis (C p.159), unquantified parent support letter, interest-free loan 410.34 (61.41% of all loans), investment 42.38, 632.01 drilling bought from it, no ECL or impairment. Group removes only 66.53 of cost on consolidation (inference: pass-through markup about 10.5%). | Note 52 S p.154; Note 7 S p.129; C p.159; Note 48 S p.148 | RED | Hidden obligation of unknown size sits on the parent; related-party purchase may carry a markup the notes do not explain. |
| 4 | Management commentary contradicts figures: payables "reduction" vs +30.9% rise; "stable collections" vs turnover down; ROCE "without increase in capital employed" vs net PPE +46.9%; MD&A ratios on a different basis from Note 51. | Note 51 S p.154; MD&A p.62 | RED (disclosure quality) | Narrative guidance is not reliable against the notes; it matters for the load-bearing "guidance against delivery" test. |
| 5 | Round-trip loans to an unnamed KMP-influenced enterprise: 1,100.00 out and back inside FY26 (PY 950.00), 15.62 interest (PY 3.30). | Note 48 S p.147-148 | RED (opacity) | Same shape two years running; no balance at year end, yet borrower, rate and tenor are withheld. |
| 6 | E&E asset 1,930.58 (Jharkhand block): no E&E policy, no impairment test, 757.73 older than three years, nil-revenue segment, "PL cum ML underway" in the note vs "completed" in the Board's report. | Note 5 S p.129; Note 1 S p.116; Note 47 C p.192 | RED (policy gap) / YELLOW | Load-bearing fact 3. 9.5% of standalone equity (derived) with no stated test. |
| 7 | Borrowing disclosure conflict: term loans "fixed" (3,624.28) vs total fixed borrowings 1,132.21; implied interest 10.99% vs stated 8.00-9.75%. Net debt nets off 1,042.52 margin-money FDs against its own definition (gearing 38.4% on stated definition vs 33.23%). | Note 20 S p.134; Note 49 S p.152-153; Note 37 S p.138 | YELLOW | Cost of debt and leverage cannot be pinned from the notes; matters for any interest or net-debt input downstream. |
| 8 | Receivable quality: allowance 187.95 covers only the over-one-year tail (189.34); 173.13 over three years frozen from last year; "all debtors good and realizable within the current financial year" contradicted by that tail; 115.69 of old balances left ageing unexplained. | Note 12 S p.131; Note 49 S p.150 | YELLOW | Matrix leaves almost nothing against 11,643.12 of newer balances. |
| 9 | Contingent liabilities 2,812.69 = 13.8% of net assets (bank guarantees 2,250.07 = 11.1%); new GST demand 397.59 (FY2021-22, appellate); no probability stated. Margin-money cover of guarantees fell 98.9% to 61.2%. | Note 42 C p.185-186; Notes 9, 14 S | YELLOW | Guarantee base grows while banks hold less cash against it. |
| 10 | Related-party and promoter-linked capital: 288.00 for 1.56% of Alara Resources Ltd (KMP-influenced; fair value 274.76); 39.92 into 17.5% Al Hadeetha; Omani JV loan 257.86 (+183%); total related-party financial exposure 855.35 (4.2% of equity). Alara LLC carrying exceeds 35% of net assets by 86.28; JV profit non-cash to date; 146.90 JV profit share unaudited. | Note 48 S p.148; Note 7 S p.129-130; Note 8 S p.130; Auditor C p.161 | YELLOW | Promoter-adjacent capital deployment with thin terms and non-cash earnings in group profit (4.4% of PAT). |
| 11 | Cost mix: sub-contract and technical fees 8,109.98 (+219%) now 33.4% of revenue; coal trading (4,533.92 revenue, thin margin) stopped; services revenue +82.2%. Depreciation rose only 150.50 on 3,900.25 plant additions (part year). | Note 35 S p.137; Note 47 C p.192; Note 2 S p.127 | YELLOW | Load-bearing fact 1. Growth came with outsourced execution; FY27 depreciation step-up is not disclosed. |
| 12 | Promoter remuneration +75.2% to 425.29 driven by CMD/JMD sales commission not taken in prior years; PY table digits transposed (263.13 vs 236.13). | Note 48 S p.148-149; C p.194; Board's report p.51 | YELLOW | 10.3% of standalone PBT (derived); commission basis not disclosed. |
| 13 | Warrants: 2,797.43 inflow arrived 10 Jul 2026 after year end, with no subsequent-event note; dilution 9.46%; promoter-group open-market disposals Jun to Sep 2026 per announcements (not in notes). | Note 19 S p.134; Board's report p.41-42 | YELLOW | The identified equity funding for the capex arrived after the balance sheet date; promoter selling alongside conversion is outside the notes. |
| 14 | Inventory of spares and diesel 5,093.93 = 139% of annual consumption (about 508 days) with no ageing or NRV note; "sundry assets written off" 197.79 (4.5x) unexplained. | Note 11 S p.130; Note 39 S p.138 | YELLOW | Possible hidden write-down risk; the write-off nature is withheld. |
| 15 | Samit JV: 80% holding treated as JV; carrying 10.70 positive against net assets (13.51); unexplained 35.79 fall in net assets beyond the 17.71 loss; revenue equals parent's spend 45.41. | Note 51 C p.201; Note 7 C p.176 | YELLOW (minor in rupees) | Equity-method policy breach or an undisclosed payment on the JV's behalf. |

### B. ACCOUNTING QUALITY SCORE: 6 / 10

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Ind AS 115 on monthly performance; 2,613.79 unbilled inside receivables; KAM on stage-of-completion not matched by the policy note (Note 1(c) S p.117; C p.159-160). No contract-asset reconciliation. |
| Expense capitalisation honesty | 5 | E&E 1,930.58 carried with no policy and no impairment test; borrowing-cost capitalisation NOT FOUND; finance cost fully expensed (Note 37 S p.138). Depreciation lives not disclosed. |
| Provisioning adequacy | 5 | ECL matches the over-one-year tail only (Note 12 S p.131); no provision on 410.34 SWR loan; no contingent probability. Gratuity assumptions low (2.00% salary, 2.68% attrition; Note 45 S p.142-145) but sensitivity disclosed. |
| RPT fairness | 5 | Round-trip loan opacity, interest-free SWR loan, unquantified support letter, Alara Resources Ltd share purchase. Offset: no promoter loans outstanding, no loans repaid late, s.197 compliant. |
| Disclosure transparency | 5 | Many stale labels and contradictions (P3-3, P3-4, Pass 2 P2-16); no subsequent-events note; extraction gaps are mine, not the company's. Offset: ageing tables, sensitivity tables and JV summaries are detailed and mostly tie. |
| Consistency with prior years | 7 | Policies unchanged; ageing, gratuity, PPE and tax tables tie arithmetically (Pass 2 Section C); no quantified restatement. Offset: retirement-age assumption change unexplained. |
| OVERALL | 6 | Numbers mostly foot and no going concern doubt at the parent. The weakness is what is withheld and the commentary that contradicts the numbers. No sign of aggressive revenue or capitalisation beyond E&E. |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Receivable build-up and cash conversion | High | Billed receivables, over-6-month bucket (270.11), customer advances, CFO vs PAT in H1 FY27 results | Next two quarters; Q2 FY27 results filed 6 Nov 2026 |
| Customer concentration at 72.27% with PSU payment cycles | High | Names and shares of top three; any LOA delays; ageing by customer | FY27 H2 collections |
| SWR support letter and related-party flows | Medium-High | Letter amount; loan 410.34; drilling purchases 632.01; SWR cost split | Any FY27 SWR loss or parent funding top-up |
| E&E 1,930.58 impairment | Medium | PL cum ML milestones, reserves report, funding plan, lease grant date | FY27-FY28 on lease outcome |
| Margin-money release reversal | Medium | FD balance 1,390.57, bank margin terms, guarantee growth | FY27 on any guarantee renewal |
| Rate-type disclosure (floating 6,729.13) | Medium | Rate cut/hike effect 33.65 per 50 bp; reconcile fixed vs floating | Each rate-policy move |
| GST 397.59 and tax contingencies | Medium | Appellate outcomes; amounts paid under protest | 12-24 months |
| Warrant conversion dilution and promoter selling | Medium | Shareholding patterns; Reg 29 filings; pledge status | Already occurred Jun-Sep 2026 |
| Promoter-linked capital (ARL shares, Al Hadeetha, Omani loans) | Medium | Rights-issue follow-on (announced Jul-Aug 2026), loan terms, JV dividends | FY27 |
| Plant depreciation step-up from FY26 additions | Medium-Low | Put-to-use dates; FY27 depreciation | FY27 P&L |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Who are the three customers that make up 72.27% of FY26 revenue, what share does each hold, and what was the overdue amount from each at 31 Mar 2026?
2. What is the amount, term and enforceability of the financial support letter to South West Resources, and why is the 410.34 loan to it interest-free and not tested for impairment?
3. Who borrowed the 1,100.00 in FY26 (and 950.00 in FY25), at what rate and tenor, and what was the purpose of a loan repaid within the year?
4. Where does the E&E asset of 1,930.58 stand against the PL cum ML process, what impairment test applies, and who funds the remaining capex?
5. Which of the three borrowing disclosures is correct: term loans fixed (3,624.28), fixed borrowings 1,132.21, or implied interest cost of 10.99% on average debt?

### E. NOTES-BASED RED FLAGS

- Earnings management: no direct evidence. Watch items: unbilled revenue 2,613.79 (22.1% of receivables); ECL sized to the old tail; "sundry assets written off" 197.79 (4.5x); other income 358.66 included an unrealised FX gain 39.34 (Cash flow S p.115).
- Aggressive accounting: E&E 1,930.58 with no policy or impairment test; interest-free SWR loan at cost with no fair-value discount (Ind AS 109); positive Samit carrying against negative net assets.
- Undisclosed risk indicators: SWR support letter amount; borrower of 1,100.00 loan; covenant terms; contingent probabilities; events after balance sheet date; customer names.
- Disclosure reliability: MD&A and Note 51 commentary contradicts the figures (P3-3); fixed/floating split conflicts with Note 20 (P3-4).
- Going concern: parent none; subsidiary SWR flagged by its auditor (P3-1). The verdict-card flag belongs to the SWR dependency, not the parent.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices. Key concern: receivables and cash conversion under rig capex, with 72.27% revenue concentration and an unquantified parent support letter to a going-concern-flagged subsidiary. Key strength: arithmetic ties across PPE, receivables, tax, gratuity and segment notes, and no parent-level going-concern doubt or quantified restatement. Overall accounting quality: 6/10.

---

```yaml
stage: B02-notes
company: "SOUTHWEST"
run_date: "2026-11-09"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "shareholding/ is empty: no source is automated yet. Push the latest quarterly shareholding pattern by hand; it closes the FII+DII UA qualifier and the promoter pledge trend."
  - "screener export sheets came out EMPTY (formulas with no cached values), so no CSV was written for them: screener, ASIANENE, DEEPINDS, JINDRILL Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization. Open Financials.xlsx once in Excel or LibreOffice, save it, then run --push-again."
  - "no results PDFs yet (screener has none): add later on github or locally + --push-again"
  - "no rating PDF yet: add later the same way"
  - "HIGH (freshness): inputs/concalls/ has no Q2 FY27 transcript. The call is scheduled for 11 Nov 2026 at 16:00 IST, after this run."
  - "shareholding/ is empty: COLLECTOR gap, not evidence. FII+DII UA qualifier and pledge trend stay open."
  - "Screener export: Data_Sheet is populated for main and peers; Profit & Loss, Quarters, Balance Sheet and Cash Flow CSVs are ABSENT. Stages use Data_Sheet and filings."
  - "results/ and rating/ were cured by /step1: three BSE results filings and the CRISIL rationale of 10 Jul 2026 (text capture; no PDF)."
  - "Q3 FY26 concall transcript (Feb 2026) is not in the corpus."
  - "annual-report/ holds FY26 and FY25; FY26 governs; FY25 is prior-year comparison only."
  - "announcements/ cover Nov 2025 to Nov 2026; pre-Nov 2025 filings are not held."
  - "inputs/announcements/20261107-eaf4e423-6c28-4f7f-b374-694a12c96ee9.txt: newspaper-advert pages garbled; not material."
  - "inputs/announcements/20260929-ae2f036b-6e7c-4543-a22d-9a2188e91ab7.txt: AGM voting results; 15 of 32 pages carry text."
  - "research/ is empty: no broker notes supplied."
  - "EMPTY-FOLDER CONFIRMATION suppressed by /step1 AUTONOMY CONTRACT. Standing default taken: proceed with the gaps."
  - "Stage 2 text extraction gaps: standalone Note 41 (contingent liabilities) body and Note 46 segment table are missing from the .txt; consolidated Notes 42 and 47 used instead; verifier to open the PDF."
flags:
  - {type: FLAG-CASH, reason: "Gross trade receivables 11,832.46 vs 7,534.67 INR Lakhs (+57.0%) on revenue +35.6%; billed receivables 9,218.67 vs 4,576.59 (+101%); customer advances 342.23 to nil; cash and equivalents 88.81 vs 1,824.50; CFO 1,233.87 vs PAT 3,080.05 (Note 12 S p.131; Note 30 S p.136; Cash flow S p.115)."}
  - {type: FLAG-GOING-CONCERN-SUBSIDIARY, reason: "Consolidated auditor reports material uncertainty on South West Resources (accumulated losses 314.88, net assets (264.94)); going-concern basis rests on an unquantified parent letter of support (C p.159; Note 52 C p.202)."}
  - {type: FLAG-RPT-OPACITY, reason: "1,100.00 loan (PY 950.00) to an unnamed KMP-influenced enterprise repaid within the year; borrower, rate and tenor not disclosed (Note 48 S p.147-148)."}
  - {type: FLAG-CONCENTRATION, reason: "Three customers = 72.27% of revenue (PY 48.00%), names not disclosed (Note 46 S p.146)."}
  - {type: FLAG-DISCLOSURE-CONFLICT, reason: "Management ratio commentary and fixed/floating borrowing split contradict the figures and Note 20 (Note 51 S p.154; Note 49 S p.152; Note 20 S p.134)."}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Cash conversion weak under rig capex: gross receivables +57.0% vs revenue +35.6%, billed receivables +101%, customer advances 342.23 to nil, cash 88.81 vs 1,824.50, CFO 1,233.87 vs PAT 3,080.05 (INR Lakhs)", note_ref: "Note 12 S p.131; Note 30 S p.136; Cash flow S p.115", rating: "RED", why: "Profit not converting to cash; capex funded by working-capital lines and margin-money release"}
  - {rank: 2, finding: "Three customers = 72.27% of revenue (PY 48.00%), names withheld; credit-risk text calls concentration low because customers are PSUs", note_ref: "Note 46 S p.146; Note 49 S p.150", rating: "RED", why: "Concentration up 24 points while receivables stretch"}
  - {rank: 3, finding: "SWR: net assets (264.94), auditor going-concern emphasis, unquantified parent support letter, interest-free loan 410.34 (61.41% of loans), no ECL or impairment; consolidation removes only 66.53 of cost against 632.01 bought (inference)", note_ref: "Note 52 S p.154; Note 7 S p.129; Auditor C p.159; Note 48 S p.148", rating: "RED", why: "Obligation of unknown size sits on the parent; related-party purchase markup unexplained"}
  - {rank: 4, finding: "Management commentary contradicts figures: payables 'reduction' vs +30.9%; 'stable collections' vs turnover down; ROCE 'without increase in capital employed' vs net PPE +46.9%; MD&A ratios on a different basis", note_ref: "Note 51 S p.154; MD&A p.62", rating: "RED", why: "Narrative is unreliable against the notes; bears on guidance-against-delivery test"}
  - {rank: 5, finding: "Round-trip loan 1,100.00 (PY 950.00) to unnamed KMP-influenced enterprise, interest 15.62 (PY 3.30)", note_ref: "Note 48 S p.147-148", rating: "RED", why: "Same shape two years; borrower, rate and tenor withheld"}
  - {rank: 6, finding: "E&E asset 1,930.58 with no policy, no impairment test, 757.73 older than three years, nil-revenue segment; PL cum ML 'underway' in note vs exploration 'completed' in Board's report", note_ref: "Note 5 S p.129; Note 1 S p.116; Note 47 C p.192", rating: "RED", why: "Jharkhand coal block load-bearing fact; 9.5% of standalone equity with no stated test"}
  - {rank: 7, finding: "Borrowing conflict: term loans fixed 3,624.28 vs total fixed borrowings 1,132.21; implied interest 10.99% vs stated 8.00-9.75%; net debt nets margin-money FDs (gearing 38.4% on stated definition vs 33.23%)", note_ref: "Note 20 S p.134; Note 49 S p.152-153; Note 37 S p.138", rating: "YELLOW", why: "Cost of debt and leverage cannot be pinned from the notes"}
  - {rank: 8, finding: "ECL allowance 187.95 covers only the over-one-year tail 189.34; 173.13 over three years frozen; 'all debtors good and realizable within the year' contradicted", note_ref: "Note 12 S p.131; Note 49 S p.150", rating: "YELLOW", why: "Almost no allowance against 11,643.12 of newer receivables"}
  - {rank: 9, finding: "Contingent liabilities 2,812.69 = 13.8% of net assets; new GST demand 397.59; margin-money cover of guarantees fell 98.9% to 61.2%", note_ref: "Note 42 C p.185-186; Notes 9, 14 S", rating: "YELLOW", why: "Guarantee base grows while banks hold less cash against it"}
  - {rank: 10, finding: "Promoter-linked capital: 288.00 for 1.56% of Alara Resources Ltd, 39.92 into Al Hadeetha, Omani JV loan 257.86 (+183%); related-party financial exposure 855.35 (4.2% of equity); JV profit non-cash, 146.90 unaudited", note_ref: "Note 48 S p.148; Note 7 S p.129-130; Note 8 S p.130; Auditor C p.161", rating: "YELLOW", why: "Thin terms; non-cash JV earnings are 4.4% of group PAT"}
  - {rank: 11, finding: "Sub-contract and technical fees 8,109.98 (+219%) = 33.4% of revenue; coal trading ended; depreciation +150.50 on 3,900.25 plant additions (part year)", note_ref: "Note 35 S p.137; Note 47 C p.192; Note 2 S p.127", rating: "YELLOW", why: "Growth bought with outsourced execution; FY27 depreciation step-up undisclosed"}
  - {rank: 12, finding: "Promoter remuneration +75.2% to 425.29 from CMD/JMD sales commission not taken in prior years; PY digits transposed in consolidated table", note_ref: "Note 48 S p.148-149; C p.194; Board's report p.51", rating: "YELLOW", why: "10.3% of standalone PBT; commission basis not disclosed"}
  - {rank: 13, finding: "Warrant balance 2,797.43 received and 28,21,411 shares allotted 10 Jul 2026, after year end, with no subsequent-events note; dilution 9.46%", note_ref: "Note 19 S p.134; Board's report p.41-42", rating: "YELLOW", why: "Funding for capex arrived post balance sheet; promoter disposals Jun-Sep 2026 are outside the notes"}
  - {rank: 14, finding: "Inventory 5,093.93 = 139% of annual consumption with no ageing or NRV note; sundry assets written off 197.79 (PY 43.86) unexplained", note_ref: "Note 11 S p.130; Note 39 S p.138", rating: "YELLOW", why: "Possible hidden write-down; write-off nature withheld"}
  - {rank: 15, finding: "Samit JV carrying 10.70 positive vs net assets (13.51); 35.79 fall in net assets beyond the 17.71 loss unexplained", note_ref: "Note 51 C p.201; Note 7 C p.176", rating: "YELLOW", why: "Equity-method loss-cap policy not followed or an undisclosed payment for the JV"}
red_flags:
  - "Receivables and cash conversion deterioration under rig capex (Note 12 S p.131; Cash flow S p.115)"
  - "Customer concentration 72.27% (PY 48.00%), names withheld (Note 46 S p.146)"
  - "SWR going-concern emphasis with unquantified parent support letter (C p.159)"
  - "Round-trip loan 1,100.00 to unnamed KMP-influenced enterprise (Note 48 S p.147-148)"
  - "E&E 1,930.58 with no policy or impairment test (Note 5 S p.129)"
  - "Management ratio commentary contradicts the figures (Note 51 S p.154)"
questions_for_mgmt:
  - "Who are the three customers making up 72.27% of FY26 revenue, what share does each hold, and what was overdue from each at 31 Mar 2026?"
  - "What is the amount, term and enforceability of the financial support letter to South West Resources, and why is the 410.34 loan interest-free and untested for impairment?"
  - "Who borrowed the 1,100.00 in FY26 (and 950.00 in FY25), at what rate and tenor, and why was it repaid within the year?"
  - "Where does the E&E asset of 1,930.58 stand against the PL cum ML process, what impairment test applies, and who funds the remaining capex?"
  - "Which borrowing disclosure is correct: term loans fixed (3,624.28), fixed borrowings 1,132.21, or implied interest of 10.99% on average debt?"
receivables_trend: "deteriorating: gross 11,832.46 vs 7,534.67 INR Lakhs (+57.0%) vs revenue +35.6%; billed 9,218.67 vs 4,576.59 (+101%); not due 71.4% vs 56.3%; unbilled 22.1% vs 39.3%; overdue under 6m 496.12 vs 25.42; over 6m 270.11 (2.28%) vs 309.72 (4.11%); over 3 years 173.13 frozen; allowance 187.95 (1.59%) vs 100.78 (1.34%); derived days 177.8 vs 153.5; company turnover 2.55 vs 2.74 (Note 12 S p.131; Note 51 S p.154)"
restatements_found: []
going_concern_language: "Subsidiary only: 'South West Resources Private Limited ... accumulated losses amounting to INR 314.88 Lakhs ... fully eroded the net worth ... current liabilities exceeded its current assets by INR 266.40 Lakhs ... material uncertainty that may cast significant doubt ... prepared on a going concern basis as the Company has letter of financial support from Holding Company' (Consolidated auditor's report, C p.159). Parent: NONE (CARO xix, no material uncertainty)."
analyst_note: "Scored 6, not lower, because the numbers foot (PPE, ageing, tax, gratuity, segments tie) and the parent has no going-concern doubt. The score falls on what is withheld and on commentary that contradicts the notes. Rank 3 (SWR) is the item a later stage cannot rebuild: the support letter is open-ended, the loan is interest-free, and the consolidation arithmetic suggests a pass-through markup (inference, confirmable only from SWR's own cost split). Rank 1 and rank 2 compound: receivables are stretching while three customers carry 72.27% of revenue, and margin-money cover of guarantees fell to 61.2%. The warrant money (2,797.43) arrived 10 Jul 2026, so FY27 leverage looks better than the FY26 balance sheet. Pass 2 found the 56.91 'other receivables' are all related-party balances. S Note 41 and Note 46 bodies are missing from the .txt; verifier should open the PDF. Parent auditor page for CARO xix not resolved."
```
