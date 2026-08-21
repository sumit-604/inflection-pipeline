# B02 — Notes to Financial Statements, PASS 2 (What Was Missed)
Company: PERMAGNET (Permanent Magnets Limited) | Run date: 2026-08-19
Source: runs/permagnet-2026-08-19/work/txt/AR-FY26.txt (FY2025-26 Annual Report, 157 pages)
Method: full second read of Notes 1-35 standalone (pp.79-112) and Notes 1-36 consolidated (pp.124-156)
against the Pass 1 output, plus tie-outs to the primary statements (Balance Sheet, P&L, Cash Flow,
pp.76-79 standalone / pp.120-123 consolidated) and cross-references into the CARO annexures (pp.70-72
standalone, p.117 consolidated) where a Note explicitly points there. All figures ₹ Crores unless stated.
Rating: 🟢 Clean | 🟡 Watch | 🔴 Red Flag. Only NEW findings not already in Pass 1 are reported below.

---

## 1. PRIMARY-STATEMENT TIE-OUT FAILURES (missed entirely in Pass 1, which only read the Notes)

- **Cash Flow Statement "Profit before tax" does not tie to the P&L "Profit before tax" line, at both
  standalone and consolidated level, by an identical amount that equals the OCI remeasurement gain.**
  Standalone P&L (p.77): "VII Profit/(loss) before tax (V-VI)" = **27.70**. Standalone Cash Flow Statement
  (p.78): "Profit before tax and extraordinary items (PBT)" = **28.00**. Unreconciled gap = 0.30, which
  exactly equals the OCI line "Items that will not be reclassified to profit or loss" (Remeasurement of
  defined benefit plans) = 0.30 (P&L item XIV(A)(i), p.77; Note 34, p.93). The same pattern repeats at
  consolidated level: consolidated P&L PBT (p.121) = **22.39**; consolidated Cash Flow PBT (p.122) =
  **22.69**; gap = 0.30, again equal to the consolidated OCI remeasurement figure (p.121, Note 35, p.152).
  🔴 Red Flag — this is not a rounding artefact (it repeats identically, to the paisa, at both reporting
  levels); it indicates the Cash Flow Statement's opening "PBT" line has been built by adding an
  other-comprehensive-income item (which by definition sits outside the P&L and should never enter an
  indirect-method cash flow reconciliation) to the actual P&L PBT. A mechanical, systemic error in how
  the Cash Flow Statement was assembled, present in both standalone and consolidated statements — a
  disclosure/preparation-quality signal the Notes alone would never reveal.
- **PPE and finance-cost depreciation/amortisation figures DO tie out cleanly** between the Cash Flow
  Statement and Notes 31/30 (standalone) and 32/31 (consolidated) — checked as part of this exercise
  and confirmed correct (8.22+0.05=8.27 dep&amort; 1.40+1.72=3.12 finance costs, standalone; similarly
  consolidated). 🟢 Clean — noted only because Pass 1 never attempted this tie-out at all; the fact that
  most lines reconcile makes the PBT gap above more notable, not less.
- **Capital Advances (Note 7) movement ties exactly to the Cash Flow Statement's "Capital Advances for
  PPE" investing outflow**: standalone Capital Advances rose 1.05→4.98 (+3.93), and the Cash Flow
  Statement shows "Capital Advances for PPE (3.93)" (p.78-79). 🟢 Clean cross-check, confirms both
  figures are internally consistent (Note 7, p.82; Cash Flow, p.79).

## 2. CAPITAL WORK-IN-PROGRESS — NEW BALANCE SHEET LINE WITH NO SUPPORTING NOTE (missed in Pass 1)

- The standalone Balance Sheet (p.76) and consolidated Balance Sheet (p.120) both carry a new line item,
  **"Capital Work-in-Progress"**, standalone **₹3.37 Cr** (FY25: Nil) and consolidated **₹8.08 Cr** (FY25:
  Nil) — implying the subsidiary alone holds ₹4.71 Cr of CWIP. Searched the entire document (Notes 1-35
  standalone, 1-36 consolidated) and confirmed there is **no CWIP ageing schedule or supporting note
  anywhere** — the Balance Sheet line itself carries no Note Number reference (blank in the "Note No."
  column, p.76 and p.120). 🔴 Red Flag — Schedule III (Division II, as amended) mandates a CWIP ageing
  schedule (amount and duration, analogous to the intangible-assets-under-development schedule) whenever
  CWIP is non-zero; this is completely absent despite CWIP appearing for the first time and being
  material at the consolidated level (₹8.08 Cr = 5.1% of consolidated total assets). Cross-references to
  Section 7 below (the subsidiary's ECB-funded capex program) and to Pass 1's flagged Note 2(c) capital
  commitment reconciliation question.

## 3. RELATED PARTY DISCLOSURE — NAMED PARTIES WITH ZERO DISCLOSED ACTIVITY, AND A DISCLOSURE-QUALITY GAP

- Note 8's related-party list (both standalone p.105 and consolidated p.149) names three "Enterprises in
  which key managerial personnel and/or their relatives are able to exercise significant influence":
  **Pregna International Limited, Megh Exim LLP, and NYMPH Properties Private Limited**. The transaction
  table immediately below shows **zero transactions with Pregna International Limited or Megh Exim LLP
  in either year** — they appear only in the entity list, never in the transactions table. 🟡 Watch — this
  may simply mean no transactions occurred (permissible), but Ind AS 24 requires disclosure of the
  relationship even absent transactions, which is met; what is missing is any statement confirming "no
  transactions during the year" for completeness, leaving the reader unable to distinguish "no
  transactions" from "an incomplete extraction." NYMPH Properties Private Limited is separately disclosed
  as holding 1.86% of promoter-group shares (Note 14.3, p.85/p.129) but likewise shows no RPT-table
  transactions with the company.
- **Note 13 (standalone p.107) / equivalent listing-regulation disclosure — "Maximum balance outstanding
  during the year" for the subsidiary loan equals the closing balance in both years** (FY26: 2.73/2.73;
  FY25: 6.17/6.17), even though the RPT table (Note 8, p.105) shows the subsidiary loan opened at 6.16-
  6.17, received a further ₹2.97 Cr disbursement, and had ₹7.01 Cr repaid during FY26 — arithmetic that
  implies the true intra-year peak balance should exceed both the opening and closing figures (e.g., if
  the 2.97 Cr disbursement occurred before the 7.01 Cr repayment, the peak would be materially above 6.17).
  🟡 Watch — the "maximum balance outstanding during the year" figure appears to have been populated as a
  copy of the closing balance rather than a true intra-year maximum, a SEBI LODR Regulation 34(3)
  disclosure-quality point Pass 1 did not test.

## 4. PROMOTER SHAREHOLDING MOVEMENTS (Note 14.3, standalone p.84-85, consolidated p.128-129) — not examined in Pass 1

- **Both co-promoters increased personal shareholding meaningfully during the year**: Sharad Jaiprakash
  Taparia (MD) 15.58%→16.11% (+0.53pp); Mukul Taparia (Director) 15.86%→16.29% (+0.43pp); Jaiprakash
  Hanumanbux Taparia 7.05%→7.20% (+0.15pp); Yamini Taparia 0.91%→1.00% (+0.09pp). 🟢 Clean/positive —
  insider accumulation by the two largest promoter shareholders during a year of strong standalone
  profit growth is a supportive signal, not previously surfaced.
- **ICICI Bank Ltd, listed under "Promoter Group" shareholding, held 31,290 shares (0.36%) at FY25 and
  fell to zero (0.00%) at FY26** (Note 14.3, same pages) — a full exit of what was presumably
  pledge-related promoter-group bank holding. 🟡 Watch — not explained in the notes; worth a factual
  question (was this a pledge release/sale, and to whom).

## 5. ACCOUNTING POLICIES / DRAFTING QC — additional instances beyond Pass 1's list

- **Standalone Note 34 duplicates the note number "34: A (I)"** for two unrelated disclosures: first for
  "Remeasurements of the defined benefit plans" (0.30 / (0.01)), then again, under the identical heading
  "34: A (I) Items That Will Not Be Reclassified To Profit Or Loss," for "Exchange differences in
  translating the financial statements of a foreign operation" (Nil / Nil) (p.93). The second instance is
  conceptually inapplicable to a standalone-only filer with no consolidated foreign operations of its
  own — it reads as boilerplate copied from the consolidated note template (which correctly carries the
  equivalent item at Note 35, p.152) without adaptation. 🟡 Watch — same drafting-QC pattern Pass 1 flagged
  elsewhere (Section 12 of Pass 1), a further data point for that pattern rather than a new standalone
  issue.
- **Standalone Note 9 narrative states the gratuity Past Service Cost is "₹1.74 Crores"** (p.106), but the
  arithmetic sum of the two components (Gratuity PSC 1.47 + Leave Encashment PSC 0.28) = **1.75**, and the
  **consolidated Note 9 narrative correctly states "₹1.75 Crores"** (p.149) for the same combined figure.
  🟡 Watch — confirms the ₹0.01 Cr discrepancy Pass 1 flagged as ambiguous ("1.74/1.75") is specifically a
  standalone-note typo; the consolidated note and the Exceptional Items note total (1.75, both standalone
  Note 33 and consolidated Note 34) are internally consistent with each other, only the standalone Note 9
  narrative sentence is wrong.
- **Two different, inconsistent definitions of "Capital employed" are used for the Return on Capital
  Employed ratio between the standalone and consolidated Ratios notes**, in the same annual report:
  standalone Note 22(j) (p.112) defines Capital employed = "Net worth + Deferred tax liabilities";
  consolidated Note 20(j) (p.156) defines it as "Total Assets - Current Liabilities other than interest
  bearing liabilities" — two materially different formulas that cannot be compared to each other or used
  to sanity-check one another. 🟡 Watch — a genuine methodology-consistency gap within a single document
  that Pass 1 did not test since it never compared the standalone and consolidated Ratios notes side by
  side.

## 6. RATIOS NOTE — items Pass 1 extracted only partially

- **Standalone Current Ratio deteriorated 4.40x→3.70x (-15.87%)** (Note 22(a), p.112) while the
  **consolidated Current Ratio IMPROVED 3.81x→4.06x (+6.44%)** (Note 20(a), p.156) — liquidity trends move
  in opposite directions between standalone and consolidated, a further, previously unflagged facet of
  the standalone-vs-consolidated divergence Pass 1's KEY FINDING already identified for profitability. 🟡
  Watch — corroborates the deteriorating standalone working-capital signal (receivables +39.4%, Section 4
  of Pass 1) with an independent ratio, while showing the consolidated entity's liquidity was actually
  cushioned (by the large ECB cash inflow sitting on the balance sheet at year end).
- **Return on Capital Employed (ROCE) fell at both levels despite standalone profit growth**: standalone
  11.20% (FY26) vs 13.81% (FY25), -18.93% (Note 22(j), p.112); consolidated 12.54% vs 13.82%, -9.24% (Note
  20(j), p.156). 🟡 Watch — not discussed anywhere in Pass 1; a declining ROCE alongside a rising ROE
  (standalone 13.31% vs 10.89%, +22.20%, already flagged by Pass 1) is an internally consistent but
  noteworthy pattern: it means the incremental capital deployed this year (debt-funded PPE/CWIP/capital
  advances) is earning a lower marginal return than the existing capital base, even as leverage
  amplifies the equity-holder return. Worth a management question on incremental project returns for the
  new capex program.
- **Debt Service Coverage Ratio declined modestly, standalone 3.66x→3.45x (-5.82%)** (Note 22(c), p.112);
  not discussed by Pass 1; below the 25%-variance disclosure threshold but directionally consistent with
  rising leverage.

## 7. CAPEX / BORROWING DETAIL — granularity Pass 1 did not extract

- **Effective interest rates on every standalone/consolidated term loan facility are fully disclosed** and
  were not extracted by Pass 1 beyond "floating (RBLR/EBLR-linked)": Central Bank of India term loan
  9.45% (RBLR+0.90%+0.30%); SBI TL-1 and TL-2 both 10.90% (EBLR+1.75%); SBI TL-3 10.40% (EBLR+0.50%); four
  car loans 8.40-8.50% fixed; SBI working-capital facility EBLR+0.70% = 9.1%; Central Bank of India
  working-capital facility RBLR+0.45% = 9.80% (Note 16, standalone p.87, consolidated p.131; Note
  19.1/19.2 standalone p.88, Note 20.1/20.2 consolidated p.133). 🟢 Clean, useful for cost-of-debt modelling
  in later stages, but not itself a flag.
- **PPE capex acceleration is sharper than Pass 1's summary conveyed**: standalone Plant & Machinery
  additions rose ₹8.21 Cr (FY25) → ₹17.77 Cr (FY26), +116.4%; ROU/lease asset additions rose ₹5.13 Cr →
  ₹10.19 Cr, +98.6% (Note 2 PPE schedule, p.80). 🟡 Watch — this is a materially larger acceleration than
  the headline capital-commitment figures (Section 3/12 of Pass 1) suggested standalone alone; combined
  with the new CWIP and capital advances findings above (Sections 2 and this section), FY26 marks a
  clear capex step-change at the parent level too, not only at the ECB-funded subsidiary.
- **Consolidated Capital Advances (Note 7, p.126) rose ₹1.05 Cr → ₹15.81 Cr (+1405.7%)**, versus
  standalone Capital Advances of ₹4.98 Cr — implying the subsidiary alone is carrying **≈₹10.83 Cr** of
  capital advances at year end, a very large sum relative to the subsidiary's overall balance sheet size.
  🔴 Red Flag (refines/quantifies Pass 1's Section 3 note that "worth reconciling against MD&A capex
  narrative") — combined with the subsidiary's CWIP of ₹4.71 Cr (Section 2 above), roughly ₹15.5 Cr of the
  new ₹47.81 Cr ECB proceeds are sitting as advances/work-in-progress rather than commissioned assets,
  meaning a meaningful share of the new debt has not yet converted into revenue-generating capacity.

## 8. SUBSIDIARY REVENUE COLLAPSE, ISOLATED VIA PRODUCT-LINE DISAGGREGATION (missed entirely in Pass 1)

- Standalone revenue disaggregation (Note 25, p.90) shows Cast Magnets & Magnetic Assembly at ₹47.21 Cr
  (FY26) / ₹30.86 Cr (FY25). Consolidated revenue disaggregation (Note 26, p.128) shows the SAME line at
  ₹47.99 Cr (FY26) / ₹36.23 Cr (FY25) — a **higher** consolidated figure in both years, meaning the
  subsidiary's Cast Magnets contribution can be isolated by subtraction: **FY25 subsidiary Cast Magnets
  revenue ≈ ₹5.37 Cr; FY26 subsidiary Cast Magnets revenue ≈ ₹0.78 Cr — an ≈85.5% YoY collapse**. All
  other revenue lines (Engineering & Current Sensing, Export Benefits net of a trivial 0.14 Cr, Sale of
  Residue) are identical between standalone and consolidated, confirming the subsidiary's entire revenue
  base is the Cast Magnets line and that this line, not the group total, is where the divergence lives.
  🔴 Red Flag — this is a materially significant finding Pass 1 missed by not cross-tabulating the
  standalone and consolidated revenue notes: the subsidiary's own revenue essentially evaporated in FY26
  at precisely the moment it drew down a ₹47.81 Cr unsecured ECB and built ≈₹15.5 Cr of capex-in-progress
  (Section 7 above). This sharpens Pass 1's Top Finding #1 (standalone-vs-consolidated PAT divergence)
  considerably: the subsidiary is not merely diluting group profitability through higher costs on stable
  revenue — its own top line contracted sharply while its balance sheet expanded on borrowed money. This
  belongs among the most important findings of the whole exercise and should be elevated in the Pass 3
  consolidation.

## 9. CARO ANNEXURE CROSS-REFERENCE — auditor detail that sharpens an existing Pass 1 Red Flag

Note: this material sits in the Auditor's Report annexures (Annexure A, standalone pp.70-72; consolidated
Annexure A, p.117), not in the Notes themselves, so it is flagged here only because the **consolidated
Auditor's Report explicitly cross-references it**: "we report that their adverse remarks in paragraphs no.
iii (a), vii (b) & ix (a) their CARO report on the standalone financial statements" (Consolidated Annexure
A, p.117). Reading those three paragraphs in the standalone Annexure A (pp.70-72):
- **CARO ix(a) (p.72) quantifies the interest default already flagged by Pass 1 (Note 16.2/Note 2(f)) with
  detail absent from the Notes themselves**: "ICICI — Interest on Central excise Loan — ₹1.75 Cr — Due
  Between October 2002 to November 2017 — Not yet paid," with a footnote "It is simple interest @12% per
  annum provided by the company till the last repayment of the loan." Neither the 12% rate nor the
  October 2002-November 2017 default window appears anywhere in Note 2(f) or Note 16.2. 🔴 Red Flag (sharpens
  Pass 1 Top Finding #5) — also note a ₹0.01 Cr discrepancy between the auditor's stated default amount
  (₹1.75 Cr) and the company's own Note 16.2/Note 2(f) figure (₹1.76 Cr) for the same balance.
- CARO vii(b) (p.71) is the CESTAT excise duty dispute already in Note 2(e) (₹0.63 Cr) — no new
  information, confirms the Note.
- CARO iii(a)/iii(f) (p.70-71) is the subsidiary loan already covered by Pass 1's RPT section — the
  auditor separately confirms the loan "is repayable on demand," a term not explicitly stated in Note 8's
  RPT table itself. 🟡 Watch — a loan repayable on demand that has nonetheless been outstanding across
  multiple years with partial repayments/redisbursements (Section 3 above) is a soft-governance point
  worth a question.

## 10. OTHER EXPENSE LINE ITEMS NOT EXAMINED IN PASS 1

- **Bank Charges rose sharply**: standalone ₹0.04 Cr (FY25) → ₹0.31 Cr (FY26), +675%; consolidated ₹0.05
  Cr → ₹0.34 Cr, +580% (Note 32 standalone p.92, Note 33 consolidated p.136-137). 🟡 Watch — unexplained in
  the notes; plausibly linked to the new ECB/term-loan activity but not stated; worth a question.
- **New "Brokerage" expense line, ₹0.11 Cr (FY26), Nil (FY25)**, both standalone and consolidated (same
  pages) — first appearance, no explanation given. 🟡 Watch — plausibly linked to the land/property
  additions in the PPE schedule (Freehold Land +₹0.30 Cr, Building +₹0.89 Cr, Section 7 above) but not
  confirmed in the notes; worth a question for management.

---

## PASS 2 NEW FINDINGS SUMMARY (new items only, ranked by investor importance)

1. **Subsidiary's Cast Magnets revenue collapsed ≈85.5% YoY (≈₹5.37 Cr → ≈₹0.78 Cr)**, isolated by
   subtracting standalone from consolidated revenue disaggregation, at the same time the subsidiary drew
   a ₹47.81 Cr unsecured ECB and built ≈₹15.5 Cr of capex-in-progress. (Note 25 standalone p.90 vs Note 26
   consolidated p.128). 🔴 Red Flag — the single most significant Pass 2 finding; materially sharpens Pass
   1's Top Finding #1.
2. **Capital Work-in-Progress is a new, unsupported Balance Sheet line** (₹3.37 Cr standalone, ₹8.08 Cr
   consolidated) with no CWIP ageing schedule anywhere in the document — a Schedule III mandatory
   disclosure gap. (Balance Sheets, p.76 and p.120; searched entire Notes, not found). 🔴 Red Flag.
3. **Cash Flow Statement "PBT" fails to tie to P&L "PBT" by exactly the OCI remeasurement amount (₹0.30
   Cr), at both standalone and consolidated level** — a systemic, repeatable Cash Flow Statement
   preparation error. (P&L p.77/p.121 vs Cash Flow p.78/p.122). 🔴 Red Flag.
4. **Consolidated Capital Advances rose ₹1.05 Cr → ₹15.81 Cr (+1406%)**, implying ≈₹10.83 Cr sits at the
   subsidiary alone — a large share of new ECB proceeds not yet converted into productive assets. (Note 7
   consolidated, p.126). 🔴 Red Flag.
5. **CARO Annexure cross-reference adds quantified detail to the Central Excise interest default**: 12%
   simple interest, default window October 2002-November 2017, auditor's figure ₹1.75 Cr vs company's
   ₹1.76 Cr. (CARO Annexure A ix(a), standalone p.72, cross-referenced by consolidated Auditor's Report
   Annexure A, p.117). 🔴 Red Flag — sharpens Pass 1 Top Finding #5.
6. **Two inconsistent "Capital employed" definitions used for ROCE** in the standalone vs. consolidated
   Ratios notes of the same annual report, plus ROCE declining at both levels (-18.93% standalone, -9.24%
   consolidated) despite rising standalone ROE. (Note 22(j) standalone p.112, Note 20(j) consolidated
   p.156). 🟡 Watch.
7. **Standalone current ratio deteriorating (-15.87%) while consolidated current ratio improving
   (+6.44%)** — liquidity trends diverge between the two reporting levels, corroborating the receivables
   deterioration Pass 1 already flagged. (Note 22(a) standalone p.112, Note 20(a) consolidated p.156). 🟡
   Watch.
8. **Related parties Pregna International Limited and Megh Exim LLP are named but show zero transactions**
   in the RPT table both years; separately, "maximum balance outstanding during the year" for the
   subsidiary loan appears to equal the closing balance rather than a true intra-year peak. (Note 8
   standalone/consolidated p.105/p.149; Note 13 standalone p.107). 🟡 Watch.
9. **Both co-promoters increased personal shareholding meaningfully during the year** (Sharad Taparia
   +0.53pp to 16.11%, Mukul Taparia +0.43pp to 16.29%); ICICI Bank Ltd's promoter-group holding fell to
   zero from 0.36%. (Note 14.3, standalone p.84-85, consolidated p.128-129). 🟢/🟡 mixed — insider
   accumulation is a positive signal; the ICICI Bank exit is unexplained.
10. **Unexplained new/spiking expense lines**: Bank Charges +675% standalone (₹0.04→₹0.31 Cr); new
    Brokerage line ₹0.11 Cr (Nil prior year), both standalone and consolidated. (Note 32 standalone p.92,
    Note 33 consolidated p.136-137). 🟡 Watch.
11. **Standalone Note 9's gratuity Past Service Cost narrative states "₹1.74 Crores" against an arithmetic
    sum of "₹1.75 Crores"** (which the consolidated equivalent note states correctly) — confirms Pass 1's
    flagged "1.74/1.75" ambiguity is a standalone-only typo. (Note 9 standalone p.106, consolidated
    p.149). 🟡 Watch.
12. **Standalone Note 34 duplicates note number "34: A(I)"** for an inapplicable "foreign operation
    translation" boilerplate line, evidence of copy-paste from the consolidated template. (Note 34,
    standalone p.93). 🟡 Watch — further data point for Pass 1's drafting-QC pattern (Pass 1 Top Finding
    #10), not a standalone new theme.
