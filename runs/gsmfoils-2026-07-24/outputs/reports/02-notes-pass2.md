# GSM FOILS LIMITED — STAGE 2 NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Run: gsmfoils-2026-07-24 | Source: Annual Report FY25 (year ended 31-Mar-2025), regenerated pdftotext -layout
extract (114pp), re-read against Pass 1 (pypdf extract, 113pp) note by note from Note 1 to the last note.

## RE-EXTRACTION METHODOLOGY NOTE (read before the findings)
The regenerated extract preserves page markers (`===== PAGE N =====`, 114 pages total). Pages 1-65 and 85-98
(Directors' Report, MD&A, Secretarial Audit Report, CEO/CFO certification, Balance Sheet, P&L, Notes 2.1-6.2)
now render as clean, directly readable text — no cipher. However, three large blocks (Note 1's fuller
duplicate at pp.99-111 covering accounting policies, "Other Disclosures"/Related Party section, Foreign
Currency section, Schedule III Ratio Disclosure, and Additional Regulatory Information; plus the entire
Independent Auditor's Report and CARO Annexure A/IFC Annexure B at pp.66-84) are STILL rendered in the same
substitution font Pass 1 identified, decodable via a consistent **+29 ASCII shift on letters** (verified: e.g.
"5HJLVWUDWLRQ'HWDLOV" decodes letter-by-letter, +29 each, to "Registration Details"; "6$1-,<$0(7$/&25325$7,21"
decodes to "SANJIYA METAL CORPORATION"). This Pass 2 manually decoded these blocks directly (no shell/OCR tool
available in this environment) rather than relying on a second automated extraction pass.

**Critical confirmation, not a Pass 1 error**: within this ciphered font, every table/sentence that should
contain a NUMBER still has a genuinely BLANK cell where the digit should be — confirmed by manually inspecting
raw line content (not just visual rendering) at the Related-Party Remuneration table, the Related-Party Director
Loan table, the Foreign Exchange Earnings/Outgo narrative, the Expenditure-in-Foreign-Currency table, and the
Schedule III Ratio Disclosure table (all at pp.104-106 of the printed report / lines 5109-5242 of this extract).
Numerals are ALSO blank inside CARO Annexure A's own prose even where the same fact is independently stated in
clean, non-ciphered text elsewhere in the document (e.g. CARO's "Company was sanctioned an amount of ₹[blank]
crore from DBS Bank" and "fresh issue of [blank] equity shares... at a fixed issue price of ₹[blank] per
share... aggregating to ₹[blank] crores", printed-report pp.68-69/extract lines 3284-3293, 3359-3369 — the IPO
share count/price/aggregate ARE independently confirmed elsewhere via Directors' Report clean text: 34,40,000
shares at ₹32.00, ₹11.01 Cr aggregate). This proves the digit loss is a genuine, systemic property of this one
embedded font across the WHOLE ciphered block, not something specific to the RPT/forex/ratio content, and not
fixable by re-running a different text-extraction library — only visual/OCR inspection of the source PDF pages
(pp.104-109 of the printed report) can recover these specific numbers. This finding narrows, rather than
resolves, Pass 1's extraction-quality caveat.

═══════════════════════════════════════════════════════════
NEW FINDINGS (not covered, or covered incompletely, in Pass 1)
═══════════════════════════════════════════════════════════

## 1. 🔴 Cash Flow Statement / Statement of Changes in Equity: escalated from "possible extraction failure" to
"likely absent from the filed document" — NEW EVIDENCE AND NEW ANCHOR
Pass 1 flagged the missing CFS/SOCE as its #2 finding but left open whether this was a mechanical extraction
failure. Pass 2 adds three pieces of evidence that shift the balance toward a genuine filing-completeness gap:
- Every OTHER ciphered financial table in the document (RPT remuneration, RPT director loans, forex
  earnings/outgo, expenditure-in-foreign-currency, Schedule III ratios) still shows its full table SKELETON —
  headers, row labels, section titles all decode cleanly; only the digit cells are blank. A full-text search
  (both plain and the same +29-cipher encoding) for "Operating Activities", "Investing Activities", "Financing
  Activities", or "Statement of Changes in Equity" returns ZERO hits anywhere in the 114-page document — not
  even a bare, digit-less table skeleton. If these statements existed as pages in the source PDF, the same
  partial-extraction pattern seen everywhere else should have surfaced at least their structure.
- NEW ANCHOR: Independent Auditor's Report, Section 143(3) reporting clause (iii), p.66 of report (decoded):
  "The Balance Sheet, the Statement of Profit and Loss, the Statement of Changes in Equity, and the Cash Flow
  Statement dealt with by this Report are in agreement with the books of account" — a second, more specific
  auditor attestation beyond the opinion-paragraph citation Pass 1 already found.
- Cross-checked against the CEO/CFO Certification (clean text, p.62 of report, already partly cited by Pass 1):
  "We have reviewed financial statements and the cash flow statement of GSM FOILS LIMITED for the year ended
  March 31, 2025..." — a THIRD independent signer (MD + CFO) attesting to a document that cannot be located.
Net: three separate certifying parties (statutory auditor's opinion paragraph, statutory auditor's clause-(iii)
compliance statement, and the CEO/CFO Reg 17(8) certificate) all attest to a Cash Flow Statement and Statement
of Changes in Equity that do not appear anywhere — not even as a blank-digit skeleton — in the filed Annual
Report text. Recommend escalating this as a priority item to verify directly against the NSE-filed PDF via the
exchange portal before Stage 11 relies on any cash-conversion metric, and flagging it to Keerti as a possible
filing-completeness issue independent of this pipeline's extraction tooling. 🔴 Red Flag (upgraded confidence).

## 2. 🔴 Contingent Liabilities note: genuinely absent from the filing — NEW FINDING, brief point 3 not
addressed at all in Pass 1
Pass 1's note-by-note walk never produced a dedicated Contingent Liabilities entry (extraction brief point 3).
Pass 2 confirms why: the accounting-POLICY definition of "Contingent liabilities" appears twice (duplicated,
consistent with Note 1 appearing in two places) — p.100/104 of report (decoded) — but in BOTH instances the
policy paragraph is followed immediately by the "Cash and cash equivalents" policy paragraph, with no
intervening actual disclosure, table, or even a "NIL" statement of contingent liabilities (contrast with Notes
5.6/5.7/5.8 — Exceptional/Extraordinary/Prior Period items — which DO explicitly show "0.00" both years). Under
Schedule III, a contingent liabilities note (even if NIL) is a mandatory line item; none is present here in any
form, ciphered or clear. Combined with CARO Annexure A's statement that "the Company does not have any pending
litigations which would impact its financial position" (already noted by Pass 1), the balance of evidence
suggests there are genuinely no contingent liabilities to disclose — but the absence of the mandatory
disclosure note itself (as opposed to its content) is a disclosure-completeness gap worth naming explicitly.
🟡 Watch (governance/disclosure-completeness, not a valuation flag).

## 3. 🟡 Capital Commitments: no disclosure found anywhere — NEW FINDING, brief point 12 gap
A full-text search for "Commitment" (plain and ciphered) returns zero hits anywhere in the 114-page document.
Given the PPE additions of ₹1.52 Cr in FY25 (Note 3.3) were funded by IPO proceeds and are apparently complete
(no CWIP balance, Note 3.5 = nil both years), a nil capital-commitments position is plausible and consistent
with the rest of the filing, but — as with Contingent Liabilities above — the ABSENCE of even a "NIL" capital
commitments note is a disclosure-completeness gap rather than a confirmed nil disclosure. 🟡 Watch.

## 4. 🟡 Related party "SANJIYA METAL CORPORATION": name and relationship now definitively confirmed; the
transaction VALUE remains genuinely unrecoverable — refines, does not resolve, Pass 1 finding #4
The full Related Party list decodes cleanly at p.104/107 of report (Note "Other Disclosures", Related Party
disclosure): Sagar Bhanushali (Key Managerial Personnel), Mohansingh Parmar (Key Managerial Personnel), Mahesh
V. Mehta / Vijay V. Pandya / Swati D. Mirani (Non-Executive Independent Directors), **SANJIYA METAL
CORPORATION (KMP is Proprietor)** — spelling now confirmed with certainty (resolves Pass 1's
"Sanjiya/Sanjaya" ambiguity) — and Pratik Makwana (Company Secretary). However, per the methodology note above,
the "Related Party Transactions" sub-section immediately below this list (Details of Remuneration of Executive
Directors; Details of Loan from Directors and relatives) shows fully-formed table headers and row labels
(Sagar Bhanushali, Mohansingh Parmar, Pratik Makwana for remuneration; Sagar Bhanushali, Mohansingh Parmar for
director loans) with every single numeric cell blank — confirmed by direct line inspection, not merely visual
scan. Sanjiya Metal Corporation does not appear as a row in either of these two specific tables (which cover
only KMP remuneration and KMP/relative loans), meaning its transaction NATURE and VALUE, if disclosed at all,
would have to sit in a general "Related Party Transactions" table this extract does not surface distinctly
from the party list itself — still NOT FOUND IN DOCUMENT. Given the company name and GSM Foils' aluminium input
base, this remains the single most important unresolved governance/RPT item and should be visually verified
against the source PDF (pp.104-105 of report) before it is dismissed as immaterial.

## 5. 🟡 Note 2.9 (Short-Term Borrowings) correction: Pass 1 mislabeled which bank held the FY24 balance —
the company switched its working-capital banker from Bank of India to DBS Bank during FY25
The structured, clean-text Note 2.9 table (p.85 of report, extract lines 4134-4153) reads:
"BOI CC: FY25 = 0.00, FY24 = ₹424.46 lakh (₹4.2446 Cr)" and "DBS BANK WORKING CAPITAL: FY25 = ₹1,334.45 lakh
(₹13.3445 Cr), FY24 = blank/nil." Pass 1's Note 2.9 discussion wrote "FY24 composition: Bank of India CC ~nil /
DBS ₹4.24 Cr" — this reverses the two banks. The correct reading is that Bank of India held the entire FY24 CC
balance (₹4.24 Cr) and DBS did not exist as a facility until FY25, when it replaced BOI entirely (BOI FY25 =
nil) and grew to ₹13.34 Cr. This is a genuine banker switch during the IPO year (from Bank of India to DBS
Bank India Limited) that Pass 1 did not call out as such — consistent with the MD&A's own description of DBS
as the company's current working-capital banker (p.52/55 of report, clean text: "the Company... banks with DBS
Bank India Limited for its working capital needs and enjoys concessional interest rates"). Does not change any
of Pass 1's aggregate short-term-borrowings-growth conclusion (+295% YoY to ₹17.82 Cr remains correct), only
the bank-level attribution within it. 🟡 Watch (correction, not a new risk).

## 6. 🟢 Segment reporting (AS-17): explicitly stated not applicable — fills brief point 11 gap Pass 1 did not
address
MD&A, p.53/56 of report (clean text): "The Company has identified its business segment as Primary Reportable
Segment. There are no other Primary Reportable Segment and the Company's Operations fall under a single
segment 'Aluminium Foils'. Hence, Segment reporting is not applicable as per Accounting Standard (AS)-17 —
Segment Reporting." Pass 1's note-by-note walk never addressed segment reporting at all (extraction brief
point 11 explicitly asks for this). This is a clean, standard disclosure for a genuinely single-product-line
manufacturer and is not a red flag on its own, but should be recorded as the answer to that open brief item
rather than left silent. 🟢 Clean.

## 7. 🟢 AOC-2 (Form No. AOC-2) — re-confirmed, not new, but with a corrected anchor
The Greek/Coptic-numeral-glyph AOC-2 table Pass 1 decoded (₹47.00 lakh / ₹43.00 lakh / ₹5.40 lakh, all
"Remuneration", all approved 23-Apr-2024) is present at extract p.48 (printed report p.45, "Annexure-I"), not
p.45 of the extract as Pass 1's anchor implied — the extract's own internal page numbering runs several pages
ahead of the printed report's page footer at this point in the document (front-matter/TOC pages). The FIGURES
themselves are unchanged and independently re-confirmed by this pass: Row 1 = ₹47,00,000, Row 2 = ₹43,00,000,
Row 3 = ₹5,40,000, all dated 23-04-2024, Board-approved. The recipient NAMES for all three rows are still not
recoverable (the "Mr./Ms. [Name]" text preceding "Remuneration" in each row does not survive extraction in
this font either) — Pass 1's inference that rows 1 and 2 are Sagar Bhanushali and Mohansingh Parmar (summing
exactly to the ₹90.00 lakh Note 5.2 KMP total) still stands and is not contradicted by anything new here. This
is a pagination correction only, not a new figure.

═══════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════
Five genuinely new items surfaced on this pass: (1) materially strengthened evidence — including a second,
more specific auditor attestation clause and cross-confirmation from the CEO/CFO certificate — that the Cash
Flow Statement and Statement of Changes in Equity are likely absent from the filed document rather than merely
lost in extraction, which should be escalated as a priority verification item ahead of Stage 11; (2) the
Contingent Liabilities note is completely absent in any form (policy definition only, no disclosure/table, not
even a "NIL"), a gap the extraction brief's point 3 asks for and Pass 1 never addressed; (3) Capital
Commitments disclosure is likewise entirely absent; (4) the related party "SANJIYA METAL CORPORATION"'s name
and KMP-proprietor relationship are now confirmed with certainty, but its transaction value remains genuinely
unrecoverable from text and does not appear in either of the two RPT sub-tables this extract does surface
(remuneration, director loans) — it must sit in a separate general RPT table not distinctly extracted here;
(5) a correction to Pass 1's Note 2.9 bank attribution, revealing an unremarked FY25 banker switch from Bank
of India to DBS Bank. One re-confirmation (AOC-2 figures, with a pagination correction) and one gap-fill
(segment reporting, AS-17 not applicable) round out this pass. The RPT rupee amounts, forex earnings/outgo,
and Schedule III ratio table that this pass was specifically tasked with recovering remain genuinely
unrecoverable from the text layer even in this regenerated, layout-preserving extraction — confirmed via
direct line-by-line inspection rather than visual scan — and require OCR or manual visual inspection of the
source PDF (pp.104-109 of the printed report) to resolve, not a different text-extraction tool.
