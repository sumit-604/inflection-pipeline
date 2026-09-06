# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 OF 3
CEIGALL (Ceigall India Ltd) | Run date 2026-09-06
Source: Annual Report FY2026 (`runs/ceigall-2026-09-06/work/text/annual-report__Annual_Report_2026.txt`,
extracted from `inputs/annual-report/Annual_Report_2026.pdf`)

═══════════════════════════════════════════════════════════
## CRITICAL MECHANICAL FAILURE — SOURCE DOCUMENT UNREADABLE
═══════════════════════════════════════════════════════════

Before extraction, the full text file was checked page by page. The result:

- The file carries 151 `[[PAGE n]]` markers (matches the source PDF page count
  per the manifest note).
- Pages 2 through 151 (150 of 151 pages) contain ZERO extracted characters.
  Every page marker is followed by a blank line. This includes the entire
  Notes to Financial Statements section, wherever in the document it sits.
- Page 1 is the only page with any extracted content, and that content is
  not decodable: it renders as strings of modifier-letter and Coptic/Greek-
  range Unicode code points (e.g. "ǣͲ͵ǡʹͲʹ͸"), consistent with a PDF whose
  text layer uses a custom subset font without a working ToUnicode CMap.
  Loose visual pattern-matching suggests page 1 is an AGM-notice-style cover
  (references to e-voting, a meeting date, Companies Act 2013 section
  citations, Ind AS wording), but this is a GUESS from glyph shape density,
  not a grounded reading, and is not reported as a finding. It is also not
  part of the Notes to Financial Statements in any case.
- I attempted to read the source PDF directly (bypassing the pre-extracted
  text) via image rendering. This failed: the PDF-to-image renderer
  (`pdftoppm`, part of poppler-utils) is not installed in this environment,
  so the PDF cannot be read as images either.

CONCLUSION: I have NO usable text for this document. This is a mechanical
corpus failure (extraction/encoding), not a company-quality finding, per
CLAUDE.md's distinction between the two. It is isolated to this one file:
I spot-checked another pre-extracted file from the same run
(`concalls__Concall_Nov_2025_Transcript.txt`) and it reads as clean, normal
English text from line 1. So the problem is specific to
`Annual_Report_2026.pdf`'s extraction, not a systemic corpus-wide encoding
break.

Because every one of Stage 2's twelve extraction categories, and all of the
archetype-specific items named in the task brief, live inside the Notes to
Financial Statements, and because those pages returned no text, EVERY item
below is "NOT FOUND IN DOCUMENT" for the single reason stated once here. I
am not inferring, estimating, or filling any of these from outside
knowledge of the company or its peers, per the grounding rule.

Recommended remediation (for the orchestrator/operator, not actioned here):
re-run the PDF-to-text extraction with an OCR pass (e.g. Tesseract over
rendered page images), or source a clean re-export of the Annual Report PDF,
since the current extraction is unusable for pages 2-151. Any other stage
that depends on this same text file (stage 1 and stages 3-9, per the
document-reading DISPATCH list) will hit the identical wall and should be
told so before they run, to avoid each one independently rediscovering this.

═══════════════════════════════════════════════════════════
## PASS 1 EXTRACTION BY CATEGORY
═══════════════════════════════════════════════════════════

1. ACCOUNTING POLICIES & CHANGES — NOT FOUND IN DOCUMENT (Notes section
   unreadable, see failure above). No policy-change text, no depreciation
   useful-life table, no capitalisation threshold, no impairment
   assumptions, no ECL matrix, no Ind AS 116 ROU/lease numbers, no
   first-time-adoption disclosure could be read.
2. RELATED PARTY TRANSACTIONS — NOT FOUND IN DOCUMENT. No RPT table, no
   promoter-entity loans, no royalty/fee/rent items, no new-related-party
   disclosure could be read.
3. CONTINGENT LIABILITIES — NOT FOUND IN DOCUMENT. No contingent-liability
   table, no bank-guarantee or performance-security figures, no tax-dispute
   composition could be read.
4. TRADE RECEIVABLES — NOT FOUND IN DOCUMENT. No ageing schedule, no
   >6-month proportion, no single-customer concentration, no ECL-on-
   receivables adequacy could be read.
5. INVENTORY — NOT FOUND IN DOCUMENT. (Note: for an EPC/HAM contractor,
   inventory is typically a minor balance sheet line relative to contract
   assets/WIP; this expectation is NOT a substitute finding, since the
   actual note text was not read.)
6. INVESTMENTS (SUBSIDIARIES/JVS/HAM SPVs) — NOT FOUND IN DOCUMENT. No
   ownership percentages, no carrying values, no impairment test, no ICD/
   loan-to-SPV table, no consolidation-method statement could be read. This
   is the single most consequential gap for this archetype: whether HAM
   SPVs are equity-accounted or consolidated, and the size of any
   intra-group receivable or guarantee, cannot be established from this
   document in its current form.
7. BORROWINGS — NOT FOUND IN DOCUMENT. No instrument table, no rate/
   maturity/security detail, no covenant language, no fixed-vs-floating
   split, no repayment schedule, no related-party borrowing could be read.
   The borrowing profile against HAM equity commitments (an archetype
   priority item per the task brief) is therefore entirely unresolved.
8. TRADE PAYABLES — NOT FOUND IN DOCUMENT. No ageing schedule, no MSME
   >45-day disclosure, no MSME interest accrual could be read.
9. PROVISIONS — NOT FOUND IN DOCUMENT. No warranty movement, no employee
   benefit funded status or actuarial assumptions, no litigation provision
   detail could be read.
10. DEFERRED TAX — NOT FOUND IN DOCUMENT. No effective-vs-statutory rate
    reconciliation, no MAT credit position, no DTA realism discussion could
    be read.
11. REVENUE DETAILS — NOT FOUND IN DOCUMENT. No segment/product/geography
    disaggregation, no contract asset/contract liability note, no
    unsatisfied-performance-obligation disclosure, no top-customer
    concentration could be read. Contract revenue recognition method
    (percentage-of-completion basis, input vs output method, and any change
    in method) is an archetype priority item and is entirely unresolved.
12. OTHER CRITICAL NOTES — NOT FOUND IN DOCUMENT. No exceptional-item
    detail, no capital-commitment figure, no segment report, no basic/
    diluted EPS reconciliation, no post-balance-sheet event, no CSR
    required-vs-actual, no ESOP or share-capital-change note, no
    direct-to-reserves entry could be read.

═══════════════════════════════════════════════════════════
## ARCHETYPE-SPECIFIC PRIORITY ITEMS (order-book/HAM EPC, per task brief)
═══════════════════════════════════════════════════════════

All NOT FOUND IN DOCUMENT, for the single reason given above:
- Contract revenue recognition policy and any change in method.
- Expected-credit-loss policy on contract assets, unbilled revenue, and
  retention money; the ageing and provisioning behind each.
- HAM SPV accounting treatment: equity-accounted vs consolidated; intra-
  group receivable balances; parent guarantees given to or on behalf of
  SPVs; any SPV-level default or covenant stress disclosed.
- Mobilisation advance balances, movement, and any adjustment/recovery
  terms.
- Related-party construction contracts with the promoter group: whether
  any exist, their value, and their terms relative to third-party
  contracts.
- Bank guarantees and performance-security contingent liabilities: total
  quantum and composition.
- Borrowing profile measured against HAM equity commitments (undrawn
  commitment, timing, and funding source).

═══════════════════════════════════════════════════════════
## COMPOUNDING CONTEXT FROM STAGE 0 (B00)
═══════════════════════════════════════════════════════════

- The corpus already carries HIGH-priority gaps on prospectus, results,
  rating, and shareholding (company listed August 2024; DRHP/RHP absent).
  None of those gaps are inside Stage 2's scope, but they compound the
  present failure: there is no alternate filed document in this corpus that
  could substitute for the Notes (e.g. no results filing with a condensed
  notes annexure, no rating rationale with a balance-sheet summary).
- Only one Annual Report exists in the corpus, so even a working extraction
  would have limited any multi-year notes trend (receivables ageing,
  borrowings, RPTs) to the comparative column printed inside the FY2026
  statements themselves, per the Stage 0 freshness note. With the current
  extraction failure, even that single-year comparative check is
  unavailable.

═══════════════════════════════════════════════════════════
## PASS 1 SUMMARY — TOP FINDINGS
═══════════════════════════════════════════════════════════

Only one finding is possible from this pass. All twelve extraction
categories and all seven archetype-priority items return NOT FOUND IN
DOCUMENT for the identical underlying cause, so listing them separately in
a ranked top-10 table would manufacture the appearance of ten findings out
of one root cause. That would violate the grounding rule against inventing
significance. The honest Pass 1 result is:

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Notes to Financial Statements text is unreadable: 150 of 151 pages extracted blank, the 1 page with content is not decodable, and direct PDF image rendering also failed (pdftoppm not installed). Isolated to this one file; other corpus documents extract cleanly. | N/A (whole Notes section, Annual Report FY2026, pp.2-151) | MECHANICAL FAILURE (not a company quality flag) | Blocks all 12 Stage 2 categories and all 7 archetype-priority items for this order-book/HAM name, including the two items CLAUDE.md and the task brief mark as most load-bearing for this archetype: HAM SPV consolidation/guarantee exposure and the ECL policy on contract assets/unbilled revenue/retention. Any other document-reading stage drawing on this same extracted text file (stage 1, stages 3-9) will hit the same wall. Needs corpus remediation (OCR re-extraction or a clean re-sourced PDF) before this stage can produce evidence. |

No other findings are reported. Pass 2 and Pass 3, if run against this same
extracted text file without remediation, will reach the identical result:
nothing to add, because there is nothing to read.
