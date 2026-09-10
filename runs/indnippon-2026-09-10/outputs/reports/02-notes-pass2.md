# STAGE 2 PASS 2: NOTES TO FINANCIAL STATEMENTS, WHAT WAS MISSED
Company: INDNIPPON (India Nippon Electricals Ltd) | Run date: 2026-09-10
Source: runs/indnippon-2026-09-10/extracted/annual-report__Annual_Report_2026.txt (FY2025-26 AR, both standalone and
consolidated note sets), cross-checked against runs/indnippon-2026-09-10/extracted/annual-report__Annual_Report_2025.txt
(FY2024-25 AR) for prior-year comparatives and disclosure-language changes, plus the primary statements (Balance
Sheet, P&L, Cash Flow Statement) and the front-matter (MD&A, BRSR, Independent Auditor's Report) of the FY26 AR,
which sit outside the Notes proper but were read here specifically to resolve the six open items Pass 1 flagged.
All amounts in Rs Lakhs unless converted to Rs Crores (Cr) for readability; Lakhs source figure always given.

This pass re-read Notes 1-52 (standalone and consolidated) against the Pass 1 extraction. Most notes were covered
fully in Pass 1 and are not repeated here. Six notes were covered only partially where the note interacts with a
primary statement or front-matter disclosure Pass 1 did not chase down; those six are the subject of this pass, in
the order the task set them.

---

## ITEM-BY-ITEM RESOLUTION OF PASS 1's SIX OPEN QUESTIONS

### 1. Receivables ageing deterioration: is the zero-ECL conclusion defensible?

Three genuinely new facts, not in Pass 1:

- **The zero-ECL justification paragraph in Note 48(i) is NEW disclosure text this year.** The FY26 Note 48(i)
  (standalone, p.232-233 PDF; identical consolidated) contains five sentences that do not exist anywhere in the
  FY25 AR's equivalent paragraph (Note 46(i), p.233 PDF, FY25 AR): "Trade receivables are non-interest bearing and
  are typically due within 45 to 90 days... Historically, the Company has experienced negligible defaults and
  maintains a strong collection track record... the Company applies the simplified approach for measuring expected
  credit losses (ECL)... the Company has concluded that there is no significant credit risk or increase in credit
  risk... Credit risk concentration is considered low due to a diversified customer base." I confirmed by direct
  text search that none of these phrases ("negligible defaults," "collection track record," "simplified approach
  for measuring," "concentration is considered low") appear anywhere in the FY25 AR. The FY25 paragraph stops after
  "represents the maximum exposure to credit risk" and moves straight to Other financial assets / Market risk. The
  underlying accounting POSITION did not change (Note 13 showed zero ECL allowance in FY25 too, same "Considered
  good"-only presentation, confirmed against the FY25 AR's own Note 13, p.210-211 PDF). What changed is the
  DISCLOSURE: a full explicit defence of the zero-ECL conclusion was added in the exact year the ageing table shows
  its sharpest deterioration. 🟡 Watch — this could be a routine disclosure-quality upgrade (many auditors are
  pushing clients toward more explicit ECL narrative under evolving SA 540/720 expectations) or it could be
  management pre-empting a question it anticipated. The document does not say which; flagging the coincidence in
  timing is as far as the Notes can take this.
- **The company's own default definition narrows what "152% jump" can mean.** Accounting policy 2.16(d) (p.199 PDF,
  same wording both years) states: "Default is considered to exist when the counter party fails to make the
  contractual payment within 90 days of when they fall due." The ageing table's "less than 6 months" bucket
  (Rs 4,290 Lakhs FY26) spans 1-180 days overdue, i.e., it straddles the company's own 90-day default line, and the
  Notes give no finer split. Given stated credit terms of 45-90 days (Note 13a), a receivable overdue by, say,
  30 days is not yet in default under the company's own policy even though it appears in this bucket. The Notes
  do not disclose how much of the Rs 4,290 Lakhs sits before vs after the 90-day mark, so the magnitude of the
  "in-default" population cannot be determined from this document. This tempers, but does not resolve, the
  Pass 1 red flag — it narrows the uncertainty rather than closes it.
- **Note 48(i) directly answers "who are the debtors."** "Trade receivables consist of a four to five major OEMs
  and a large number of small customers, spread across diverse industries and geographical areas" (identical
  wording both years, p.232 PDF FY26 / p.233 PDF FY25). Combined with Note 28e (2 customers = 70.66% of revenue)
  and the BRSR-named OEM list (TVS Motor, Hero MotoCorp, Bajaj Auto — see Item 7 below), the debtor concentration
  is with a small number of large, presumably investment-grade OEM counterparties, not diffuse retail exposure.
  This is consistent with, and does not contradict, a low-default-history claim, but it also means any single
  large-OEM payment-cycle change (e.g., an OEM stretching terms) would show up exactly as this ageing table shows
  it: a jump concentrated in the near-term bucket, because OEMs pay in bulk on a cycle, not in a smooth trickle.
- **A 3-year ageing view shows FY26 is the worst of three years, not a rebound from an anomalous FY25 low.**
  Pulling FY24 comparatives from the FY25 AR (Note 13c, ii, p.211 PDF): overdue-of-any-age was Rs 2,170 Lakhs /
  Rs 14,175 Lakhs total = 15.3% at FY24. FY25: Rs 1,885 Lakhs / Rs 16,965 Lakhs = 11.1%. FY26: Rs 4,613 Lakhs /
  Rs 20,646 Lakhs = 22.3%. So the trend is 15.3% (FY24) -> 11.1% (FY25) -> 22.3% (FY26): FY25 was the unusually
  clean year, and FY26 is worse than both FY24 and FY25, not merely worse than an atypically good FY25 base. This
  strengthens, not weakens, the Pass 1 concern. 🟡 Watch, sharpened.
- **The auditor's own Key Audit Matter list does NOT include receivables/ECL.** Deloitte's sole standalone KAM for
  FY26 (p.172-173 PDF; see Item 6 below) is the Lucas TVS fair valuation. No KAM was raised on trade receivables or
  ECL judgment. This is an independent (external) signal that the statutory auditor did not consider the zero-ECL
  call material enough to warrant KAM-level audit-risk disclosure, for what that is worth against an internal
  ageing-table read.

### 2. The Rs 36.81 Cr (Note 13) vs Rs 35.47 Cr (cash flow) receivables gap: found the reconciling line, not the reconciling item

The cash flow statement line is now precisely located: "Decrease / (increase) in trade receivables (3,547)"
(Standalone Statement of Cash Flows, p.185-186 PDF; identical in the Consolidated Statement of Cash Flows,
p.247-248 PDF — same Rs 3,547 Lakhs in both, confirming the deconsolidated subsidiary carried no trade receivables).
Note 13's balance sheet movement is Rs 20,646 - Rs 16,965 = Rs 3,681 Lakhs (both figures tie exactly to the Balance
Sheet line, p.183 PDF: Trade receivables Rs 20,646 / Rs 16,965 — Note 13 is not netted or adjusted anywhere else).
The residual gap is Rs 3,681 - Rs 3,547 = **Rs 134 Lakhs (Rs 1.34 Cr)**, confirmed precisely (Pass 1's "Rs 1.34 Cr"
figure was correct). I checked the candidate reconciling items and none matches:
- No bad-debt write-off or "sundry balances written off" line exists anywhere in Note 37 (Other Expenses, p.220-221
  PDF) or elsewhere in the P&L notes — searched the full text, no match.
- The "Unrealized forex gain, net (118)" adjustment line in the cash flow statement (a separate line item, before
  the working-capital section) is close in magnitude but does not tie exactly, and in any case relates to all
  monetary items, not trade receivables specifically (per Note 48(ii), the unhedged FX trade receivable exposure
  alone moved by roughly Rs 1,150 Lakhs YoY in rupee terms, itself larger than the Rs 118 Lakh forex line).
- Other financial assets and other current assets notes move by amounts that already tie to their own separate
  cash flow WC lines (e.g., Note 9 Loans +31 Lakhs ties exactly to the CF "Decrease/(increase) in loans (31)" line;
  Note 17 Other current assets +878 Lakhs ties exactly to "Decrease/(Increase) in other current assets (878)").
  Nothing here absorbs the Rs 134 Lakh trade-receivables gap.
**Conclusion**: the gap is real, both source figures are now anchored precisely (Note 13 / Balance Sheet p.183 PDF
vs Cash Flow Statement p.185-186 PDF), but no note or primary-statement line in this document decomposes the
Rs 134 Lakh residual. NOT FOUND IN DOCUMENT for the specific reconciling item. This is small (0.65% of the Note 13
receivables balance) and does not change the substance of the LB1 cash-conversion read, but it should not be
described as "resolved" — it remains an open, bounded, immaterial gap.

### 3. Note 28 export-figure inconsistency (Rs 33.63 Cr vs Rs 33.25 Cr): this is not a FY26 transcription error, it is an uncorrected carry-forward from the FY25 AR itself

New finding: the FY25 AR's OWN current-year Note 27 (Revenue from Operations, the FY25 AR's note number for what
becomes Note 28 in the FY26 AR — the note numbering shifted by one between the two ARs) already shows the identical
inconsistency for FY25 as its own current year: "Export sales 3,363" (product-line, p.218 PDF FY25 AR) vs "Rest of
the world 3,325" (geography, same note, p.218 PDF FY25 AR) — the same Rs 38 Lakh gap, not a number that changed
when FY25 became a comparative in the FY26 AR. Checking one year further back, the FY25 AR's own FY24 comparative
ties exactly both ways: Export sales Rs 3,578 Lakhs = Rest of the world Rs 3,578 Lakhs (FY25 AR, p.218 PDF, "3,578"
appears identically in both lines). So the inconsistency is specific to the FY25 fiscal year's own figures, was
never corrected across two successive annual reports, and both the FY25 AR and FY26 AR carry it forward unchanged
as a comparative. This rules out a Pass 2 hypothesis that it might be a mechanical carry-forward/transcription slip
introduced only in the FY26 AR; it is a genuine, persistent, two-report-old reconciliation gap between how the
company's product-type ledger and its geography ledger each classify the same FY25 export transactions.
**Which line to build the growth figure on**: use "Rest of the world" (geography) — Rs 8,727 / Rs 3,325 Lakhs =
+162.5% — because it is the figure disclosed independently in two places within Note 28 itself (28a Disaggregation
and 28d Geographical information, both p.217-218 PDF) and has not moved between the FY25 AR and the FY26 AR's
comparative column, whereas "Export sales" is a single product-type sub-line with no independent cross-check. The
difference to the alternative reading (+159.4% on "Export sales") does not change the qualitative story (~160%
export growth either way).

### 4. Technical knowhow Rs 4.77 Cr: earnings effect quantified, and it explains the YoY amortization decline the run had not connected

Re-reading Note 6A's full roll-forward (p.202-203 PDF) rather than only the closing figures: Technical knowhow
gross additions of Rs 477 Lakhs were booked in FY25 (year ended 31-Mar-2025, "Additions" row), and the SAME Rs 477
Lakhs appears in the "Charge for the year" row for FY25 — an exact match, confirming a 100% first-year write-off.
Net block is Rs 0 in every one of Note 6A's closing columns for this asset from FY25 onward. This is a FY25 P&L
event (confirmed by the roll-forward dates), so it does NOT depress FY26 earnings. What Pass 1 did not connect: this
single Rs 477 Lakh charge is the primary driver of Note 36's YoY amortization decline. Note 36 (Depreciation and
Amortization Expenses, p.219-220 PDF) shows "Amortization of intangible assets" falling from Rs 531 Lakhs (FY25) to
Rs 42 Lakhs (FY26), a Rs 489 Lakh (92%) drop — and the technical-knowhow line alone accounts for Rs 477 Lakhs of
that Rs 489 Lakh decline (the remaining Rs 12 Lakh comes from smaller movements in software/SAP/license
amortization). Practically: any FY25-to-FY26 D&A trend comparison, or any 2-year average D&A run-rate used for
normalization, should exclude this one-off FY25 spike, or it will understate FY26's "amortization decline" as
operating leverage when it is in fact a base-year anomaly unwinding. No note anywhere explains WHY a 5-year-life
asset (per stated policy 2.5, p.191-192 PDF) got a 100% first-year charge; this remains an unexplained
policy-vs-practice gap, as Pass 1 found, now with the earnings mechanics fully quantified.

### 5. Receivables turnover ratio vs ageing table contradiction: mechanically explained, not necessarily exonerated

Note 51 (p.233-234 PDF) defines Trade Receivables Turnover Ratio as "Net credit sales (net of sales returns) /
Average accounts receivable" — an AVERAGE-balance, full-year metric. Recomputing: FY26 average trade receivables =
(16,965 + 20,646)/2 = Rs 18,805.5 Lakhs; Net Sales Rs 1,05,292 Lakhs (Note 28); 1,05,292 / 18,805.5 = 5.60, close to
the disclosed 5.7 (small difference likely from the company using a slightly different average-receivables base,
e.g., including/excluding retained taxes). The ratio improved slightly because full-year average receivables grew
by 20.8% while net sales grew faster (roughly 26.5% headline revenue growth), so the AVERAGE-based ratio looks
stable-to-better even as the YEAR-END SNAPSHOT (the ageing table) looks materially worse. Both are arithmetically
correct; they simply measure different things — a full-year average smooths out a late-year (or year-end)
concentration of overdue amounts that the point-in-time ageing table captures directly. For cash-conversion and
going-forward liquidity purposes, the point-in-time ageing table is the more relevant of the two, since it is what
actually sits on the balance sheet on the cut-off date. This resolves the apparent "contradiction" as a
measurement-basis effect rather than a data error, but does not diminish the substance of the ageing deterioration
itself (see Item 1 above).

### 6. Lucas TVS 8x EV/EBITDA multiple: three new facts materially update the Pass 1 read

- **The multiple has moved before — it is not permanently frozen.** The FY25 AR's own Note 47(g) equivalent
  (p.232 PDF, FY25 AR) states: "EV/EBITDA Multiple at 8x (Previous Year - EV/EBITDA Multiple at 9x)." So the
  multiple was 9x at FY24, was cut to 8x for FY25 (an 11.1% reduction), and has been held at 8x for FY25 and FY26
  (the "unchanged" window Pass 1 correctly identified is 2 years, not the full history). Management has
  demonstrably exercised judgment to move this input before, and moved it DOWN, which weakens (without eliminating)
  a "management is holding the multiple artificially high" reading.
- **Value has risen in every one of the last three years regardless of multiple direction, meaning the EBITDA/net
  debt bridge input, not the multiple, has driven all the gains.** Lucas TVS fair value: Rs 19,037 Lakhs (FY24) ->
  Rs 22,468 Lakhs (FY25, +18.0%, DESPITE the multiple being cut 9x to 8x that same year — this level of value growth
  against a falling multiple implies the underlying EBITDA/bridge input rose by roughly a third that year) ->
  Rs 26,412 Lakhs (FY26, +17.6%, multiple flat at 8x). Cumulative 3-year growth: +38.7%, while the multiple itself
  FELL over the same window. All three years of gains are therefore attributable entirely to the unobservable
  EBITDA/net-debt-bridge input, never to multiple expansion. This is a genuine mitigant on the "is management
  inflating this holding via a stale multiple" question — the multiple, if anything, has been a drag, not a lever.
  It does NOT resolve the deeper problem: neither Lucas TVS's EBITDA, its net debt/cash position, nor India
  Nippon's percentage ownership of Lucas TVS's total share capital is disclosed anywhere in this document (Note 8A
  gives only "97,351 shares, face value Rs 100" with no total-shares-outstanding denominator). The entire economic
  driver of a holding worth 32.2% of net worth is external to what this document can verify.
- **The Lucas TVS fair valuation is the auditor's SOLE Key Audit Matter for FY26.** Deloitte Haskins & Sells's
  Independent Auditor's Report (standalone, p.172-173 PDF; consolidated equivalent carries the identical KAM) names
  exactly one Key Audit Matter: "Fair Valuation of Investments," specifically this Rs 26,412 Lakh unquoted equity
  holding. The auditor's response procedures explicitly include "engaging our fair valuation expert to test the
  appropriateness of the Management's underlying assumptions" and "a look back analysis to ascertain whether the
  input data and assumptions considered by the Management in the past is within a reasonable range when compared to
  the actual results." No other KAM is listed — nothing on receivables, nothing on inventory, nothing on revenue
  recognition. This independently corroborates that this valuation, not the ageing-table question, is the single
  highest-judgment area in these accounts by the statutory auditor's own assessment, and confirms an external
  valuation expert (not disclosed by name) has already tested this input as part of the FY26 audit — a fact
  investors weighing the "is 8x supportable" question should know exists, even though the expert's conclusion
  itself is not reproduced in the Notes.

### 7. TVS Motor / two-customer concentration vs Note 42 related-party perimeter: resolved via BRSR and front-matter, and the Ind AS 24 line looks correctly drawn

- **The MD&A/BRSR names the major customers outright, something Note 28e (anonymised per Ind AS 108) does not do.**
  BRSR Question 19(c) (standalone, p.129 PDF): "Our major customers - TVS Motor Company Limited, Hero MotoCorp
  Limited and Bajaj Auto Limited." This is a direct, dated (FY26), signed disclosure sitting outside the Notes. It
  names THREE large OEMs, not one; Note 28e's two ">10%" customers are therefore drawn from this group of three
  (or possibly include an OEM outside this named group — the Notes and BRSR together do not say which two of the
  three, or whether it is even two of these three, individually cross 10%). Hero MotoCorp and Bajaj Auto are
  independently listed, non-TVS-group companies with no ownership or control link to India Nippon's promoter chain
  (Lucas Indian Service / SB TVS Industrial Ventures). This materially updates Pass 1's framing, which speculated
  the dominant counterparty was "almost certainly including TVS Motor Company" given the TVS lineage — the evidence
  now shows the customer base is explicitly a THREE-OEM group spanning both TVS-affiliated and entirely unrelated
  promoter families, which is the more standard "few large 2W-OEM customers" pattern for an Indian ignition-systems
  auto ancillary, not a TVS-group-internal concentration. The Ind AS 24 perimeter in Note 42 (excluding TVS Motor,
  Hero MotoCorp, and Bajaj Auto, none of which are under common control or significant influence with India
  Nippon's promoter group) reads as correctly drawn on these facts, not under-drawn.
- **India Nippon's own "Our Journey" history section (p.15 PDF) independently corroborates a long-standing,
  multi-OEM (not TVS-exclusive) customer base**: "Commencement of production and supply to TVS-Suzuki (now TVS
  Motor Company), Bajaj Auto, and Hero Motors" from the company's earliest years, later adding "Birla Yamaha,"
  "Hero MotoCorp," "Honda Siel Power Products," "India Yamaha Motor," "Mahindra Two-Wheelers," and an export
  relationship with "Kokusan Denki Co. Limited, Japan." A current-year award ("Outstanding Commitment to
  Sustainability Award — TVS Motor Company," p.[~50] PDF, and a Founder's Day 2026 appearance by Hero MotoCorp's
  COO, p.41 PDF) confirms both TVS Motor and Hero MotoCorp remain live, active relationships today, not merely
  historical ones.
- **Management's own MD&A/BRSR Risk Factors table names customer concentration as a named risk, and its stated
  mitigation narrative sits in tension with the Note 28e data.** The Customer Risk row (standalone, p.126 PDF)
  reads: "High dependence on a limited number of key customers can create vulnerabilities if these relationships
  change... The Company has also progressively reduced its dependency on key customers over the years, thereby
  strengthening business diversification and enhancing revenue stability." Against this, Note 28e shows the
  two-customer concentration eased only 3.2 percentage points in relative terms (73.82% FY25 -> 70.66% FY26,
  matching Pass 1's finding) while growing 21.1% in absolute rupees (Rs 623.65 Cr -> Rs 754.91 Cr). A
  "progressively reduced dependency" framing sits awkwardly against a concentration ratio that remains above 70% of
  total revenue and is still growing in absolute terms; the word "progressively" implies a multi-year trend the
  two data points disclosed in this AR (FY25, FY26) cannot themselves establish either way. 🟡 Watch — a
  narrative-versus-data tension worth a direct management question, not proof of misstatement (the claim may be
  true over a longer, undisclosed history the Notes do not cover).

---

## OTHER NOTES RE-READ, NO MATERIAL NEW FINDING
Notes 3 (Non-current investments classification), 4 (PPE — title-deed confirmation is standard/clean), 5 (CWIP
ageing), 7 (ROU assets), 9-11 (Loans, other financial assets, other non-current assets), 15-17 (other current
financial/non-financial assets), 18-27 (share capital, reserves, lease liabilities, DTL, trade payables, other
financial/current liabilities, provisions, current tax) were re-read in full against Pass 1's coverage; all match
Pass 1's extraction with no new note-level finding. Note 43 (Earnings per share detail beyond the headline figures
already in Note 44), Note 46 (CSR detail), Note 49 (Additional regulatory information / CARO cross-references), and
Note 50 (Loans and advances in nature of loans, Regulation 34(3)) were also re-read; all Nil / not-applicable lines
confirmed, nothing further to extract.

---

## PASS 2 NEW FINDINGS SUMMARY

| # | New finding | Anchor | Rating | Relates to |
|---|---|---|---|---|
| 1 | Note 48(i)'s explicit zero-ECL justification paragraph (typical 45-90 day terms; "historically negligible defaults... strong collection track record"; simplified ECL approach; "concentration is considered low") is entirely NEW text in the FY26 AR, absent from the FY25 AR's equivalent Note 46(i) paragraph, added in the exact year the ageing table deteriorated most | Note 48(i), p.232-233 PDF FY26 vs Note 46(i), p.233 PDF FY25 AR | 🟡 Watch | Item 1 |
| 2 | Company's own default definition ("90 days of when they fall due," policy 2.16(d)) means the ageing table's "less than 6 months" bucket straddles the pre-default/in-default line with no further split disclosed, so the 152% jump cannot be decomposed into defaulted vs not-yet-defaulted amounts | Policy 2.16(d), p.199 PDF | 🟡 Watch | Item 1 |
| 3 | 3-year ageing trend (pulled from FY25 AR's FY24 comparative): overdue share 15.3% (FY24) -> 11.1% (FY25) -> 22.3% (FY26) — FY26 is the worst of three years shown, not a rebound from an anomalous FY25 low | Note 13c, p.211 PDF FY25 AR vs p.208-209 PDF FY26 AR | 🟡 Watch, sharpens Pass 1 | Item 1 |
| 4 | Deloitte's sole standalone Key Audit Matter for FY26 is the Lucas TVS fair valuation; no KAM was raised on receivables/ECL, an independent external signal the auditor did not treat the ageing question as the top judgment risk | Independent Auditor's Report, KAM section, p.172-173 PDF | 🟢 Clean (context) | Items 1 & 6 |
| 5 | The Rs 134 Lakh (Rs 1.34 Cr) gap between Note 13's balance-sheet receivables movement (Rs 3,681 Lakhs) and the Cash Flow Statement's working-capital line (Rs 3,547 Lakhs) is now precisely bounded (both source figures anchored) but remains formally unreconciled: no bad-debt write-off, no forex line, and no other-asset reclass in the document accounts for it | Note 13 / Balance Sheet p.183 PDF vs Cash Flow Statement p.185-186 PDF (standalone) | 🟡 Watch | Item 2 |
| 6 | The Rs 38 Lakh Export-sales-vs-Rest-of-world gap is NOT a FY26 transcription artifact: the FY25 AR's own current-year Note 27 shows the identical Rs 38 Lakh gap for FY25's own figures, uncorrected across two successive ARs; FY24 figures tied exactly both ways in the FY25 AR | Note 27, p.218 PDF FY25 AR vs Note 28, p.217-218 PDF FY26 AR | 🟡 Watch | Item 3 |
| 7 | Technical-knowhow full write-off (Rs 477 Lakhs, FY25) is the primary driver of Note 36's YoY amortization decline (Rs 531 Lakhs FY25 to Rs 42 Lakhs FY26, a Rs 489 Lakh / 92% drop) — a base-effect that should be excluded from any FY25-to-FY26 D&A trend read | Note 6A / Note 36, p.202-203 & p.219-220 PDF | 🟡 Watch | Item 4 |
| 8 | Receivables turnover ratio (average-balance basis) vs ageing table (point-in-time basis) is a measurement-basis effect, not a data contradiction: average receivables grew 20.8% while net sales grew faster, improving the ratio even as the year-end snapshot worsened | Note 51, p.233-234 PDF | 🟢 Clean (methodology), issue itself remains 🟡 | Item 5 |
| 9 | Lucas TVS EV/EBITDA multiple was 9x at FY24, cut to 8x for FY25 (an actual downward revision, not a frozen input), held flat at 8x for FY25-FY26; fair value rose in all three years (+18.0% FY25 despite the multiple cut, +17.6% FY26 on a flat multiple) — all 3 years of gains are attributable entirely to the undisclosed EBITDA/net-debt bridge input, never to multiple expansion | Note 47(g), p.228-229 PDF FY26 vs equivalent, p.232 PDF FY25 AR | 🟡 Watch, materially updates Pass 1 | Item 6 |
| 10 | Neither Lucas TVS's EBITDA, its net debt/cash bridge, nor India Nippon's % ownership of Lucas TVS's total share capital is disclosed anywhere in this document — the entire economic driver of a 32.2%-of-net-worth holding is external to what this AR can verify | Note 8A, p.204-205 PDF | 🔴 Red Flag (disclosure gap, not misstatement) | Item 6 |
| 11 | BRSR Q19(c) names the major customers directly: "TVS Motor Company Limited, Hero MotoCorp Limited and Bajaj Auto Limited" — a three-OEM group spanning both TVS-affiliated and wholly independent promoter families, materially updating Pass 1's speculation that the dominant counterparty was "almost certainly" TVS-affiliated alone | BRSR Q19c, p.129 PDF | 🟢 Clean (resolves Item 7's open question) | Item 7 |
| 12 | Management's own MD&A/BRSR Risk Factors table claims the Company has "progressively reduced its dependency on key customers over the years," in tension with Note 28e showing the two-customer concentration still above 70% of revenue and growing 21.1% in absolute rupees YoY (percentage share eased only 3.2pp) | MD&A Risk Factors, Customer Risk row, p.126 PDF, vs Note 28e, p.217-218 PDF | 🟡 Watch | Item 7 |

END OF PASS 2.
