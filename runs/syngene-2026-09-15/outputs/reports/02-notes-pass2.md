# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 (WHAT WAS MISSED)
Company: Syngene International Ltd (SYNGENE) | Run date: 2026-09-15
Source: Annual_Report_2026.pdf (page numbers = PDF page in the "===== PAGE n =====" markers).
Comparator: Annual_Report_2025.txt, cited only where used. All amounts in INR Million unless
converted to Rs Cr for readability. Tagged [STANDALONE] / [CONSOLIDATED].

This pass re-reads the notes end to end against Pass 1's coverage, resolves the three
carry-forward items Pass 1 flagged for verification, and reports genuinely new findings only.
Items Pass 1 already covered fully are not repeated.

---

## RESOLUTION OF THE THREE PASS 1 CARRY-FORWARD ITEMS

### 1. Syngene Scientific Solutions (SSS) Rs 315,000/share dividend — CONFIRMED AS PRINTED, RESOLUTION STILL NOT POSSIBLE FROM THIS DOCUMENT
Re-read verbatim at consolidated Note 45(c), p.375: "On 28 April 2026, the Board of Directors of
Syngene Scientific Solutions Limited recommended a final dividend of Rs. 3,15,000 per equity
share of Rs. 10/- each." (Indian digit-grouping "3,15,000" = 315,000 in international grouping —
this is not an OCR/comma-placement artefact; the pipeline's own extraction is faithful to the
source text.) Cross-checked against SSS's disclosed share count of 84,000,000 equity shares of
Rs 10 each (standalone Note 5, p.246, unchanged FY26 vs FY25) and SSS's FY26 profit before tax
of Rs 287mn on total income of Rs 4,255mn (Board's Report subsidiary review, p.65-66, quoting
SSSL's own management commentary). A dividend of Rs 315,000/share on 84,000,000 shares implies
an aggregate payout of approximately Rs 26,46,00,00,00,000 (~Rs 26.46 lakh crore) — roughly 56x
Syngene's own FY26 consolidated revenue (Rs 37,387mn) and off by several orders of magnitude
against SSS's own Rs 287mn PBT. 🔴 No other figure anywhere in the AR (cash flow statement,
dividend distributed line, subsequent-events register) corroborates a payout of this scale. This
reads as an as-filed error in the AR itself (most likely a decimal/digit-grouping slip in
drafting, e.g., an intended Rs 3.15 or Rs 31.50 per share), not resolvable from the document —
carried forward as a management/verification question, not assumed to be a real economic event.

### 2. Bayview pre-operating cost Rs 787mn standalone vs Rs 785mn consolidated — RESOLVED, IMMATERIAL
Both note sets state the identical underlying USD figure: "additional pre-operating cost of
Rs. 787 million (USD 8.4 million)" (standalone Note 42, p.288-289) vs "Rs. 785 million (USD 8.4
million)" (consolidated Note 43, p.374). The Rs 2mn (0.25%) gap is a rupee-translation rounding
difference — the standalone entry translates the intercompany-funded US cost at the parent's own
transaction/average rate, while the consolidated entry reflects Syngene USA Inc.'s own USD books
translated at the Group's consolidation rate for the period. 🟢 Immaterial, not a data-quality
concern; both anchor to the same USD 8.4mn.

### 3. Consolidated cash-flow-hedge OCI net of tax — RESOLVED
Consolidated OCI note (p.365, series continuing the table referenced in Pass 1): "Effective
portion of gains/(losses) on hedging instrument in cash flow hedges (3,082) (146)" pre-tax,
"Income tax effect 766 44", giving **net-of-tax Rs -2,316mn FY26 vs Rs -102mn FY25**
(consolidated) — a ~22.7x deterioration, comparable in scale to but a distinct figure from the
standalone Rs -2,275mn net-of-tax loss already reported in Pass 1. The consolidated OCI table
also separately shows "Exchange difference on translation of foreign operations 403 (64)" FY26
vs FY25 — a genuinely new, non-hedge OCI line that helps explain other findings below.

---

## PASS 2 NEW FINDINGS

### A. 🔴 Derivative fair-value position flipped from a large net ASSET to a large net LIABILITY — a second, independent note confirming the scale of the hedge deterioration
Note 28 "Financial instruments: Fair value and risk management" [STANDALONE, p.270-271] shows,
within the SAME table that carries both years' figures:
- 31-Mar-2025: derivative assets (non-current Rs 1,705mn + current Rs 516mn) = Rs 2,221mn vs
  derivative liabilities (non-current Rs 17mn + current Rs 49mn) = Rs 66mn → **net derivative
  ASSET of ~Rs 2,155mn**.
- 31-Mar-2026: derivative assets (non-current Rs 317mn + current Rs 69mn) = Rs 386mn vs
  derivative liabilities (non-current Rs 488mn + current Rs 1,089mn) = Rs 1,577mn → **net
  derivative LIABILITY of ~Rs 1,191mn**.
- Swing: from +Rs 2,155mn to -Rs 1,191mn is a **~Rs 3,346mn net deterioration** in the fair value
  of the Company's hedge book within the year — a magnitude consistent with, and independently
  corroborating from a balance-sheet note rather than the P&L/OCI note, the Rs -3,027mn pre-tax
  cash-flow-hedge OCI loss Pass 1 already flagged as the single most significant finding.
- [CONSOLIDATED, p.339 series] Same pattern: derivative assets non-current fell from Rs 1,706mn
  (FY25) to Rs 317mn (FY26); derivative liabilities rose from Rs 18mn+56mn=Rs 74mn (FY25) to
  Rs 488mn+1,145mn=Rs 1,633mn (FY26).
- This means the hedge book entered FY26 sitting on a large UNREALISED GAIN (favourable to the
  Company — the rupee had weakened less than the forward rates locked in, or forward points
  moved in Syngene's favour) and flipped to a large unrealised LOSS within the year. This is a
  forward-earnings risk item, not a one-off: unrealised losses reclassify into the P&L over the
  life of the underlying hedged transactions (the Q1FY27 EBITDA hit per company memory is a first
  tranche of this reclassification).

### B. 🟡 Apparent unit mislabel in the FX forward/option notional-contract table — second documentation-quality gap in the standalone notes
Note 28 [STANDALONE, p.273 sensitivity/derivatives section] discloses "outstanding foreign
exchange forward and option contracts" under the note's blanket header "All amounts are in
Indian Rupees Million... unless otherwise stated": FY26 forward contracts to sell USD, total
Rs 393mn; FY25 total Rs 512mn; European-style options Rs 167mn FY26 / Rs 217mn FY25.
[CONSOLIDATED equivalent, p.339 series]: Rs 404mn/Rs 527mn forwards, Rs 170mn/Rs 222mn options.
These notional totals (aggregate ~Rs 560mn-750mn) are implausibly small set against: (i) the
Rs 3,027-3,082mn pre-tax fair-value swing on this same hedge book in the same year (Finding A
above and Pass 1's Note 30(b) finding); (ii) the Company's own USA-derived services revenue of
Rs 21,157mn (~USD 238mn at FY26 average rates) that the forwards exist to hedge. A notional book
of USD 393-560 million (i.e., the SAME digits read as USD Mn rather than Rs Mn) would sit at
roughly 1.7-2.3x annual USD revenue spread over a multi-year forecast horizon (the table's own
"1-2 years," "2-5 years" buckets), which is internally consistent with a company hedging several
years of forecast USD sales — and with the derivative fair-value swing's magnitude. This reads as
a probable USD-vs-Rs-Mn labelling error carried through both the standalone and consolidated
versions of the same table (an inherited template error, not independently made twice) — a
second instance, alongside the Note 1.2(e)/Note 43 cross-reference slip already flagged in Pass 1
Finding 10, of the standalone notes not being fully proofed before filing. Flagged for management
verification, not restated as fact.

### C. 🟡 Syngene USA Inc. loss: Board's Report narrative figure does not tie to the audited consolidation note
Board's Report subsidiary review (p.65): "In FY26, [Syngene USA Inc.] revenue stood at USD 12.25
million, with a loss of USD 1.4 million" — at the FY26 average/closing USD rate (Rs 88.71-93.48
per Note 28 sensitivity table), this loss translates to roughly Rs 124-131mn. The AUDITED
consolidated Schedule III "Additional information" note [CONSOLIDATED Note 33(b), p.368] instead
attributes only **Rs 77mn** of consolidated loss to Syngene USA Inc. — a gap of roughly Rs 47-54mn
(38-42%) between the narrative disclosure and the note that is not reconciled anywhere in the AR.
Plausible explanations (intercompany elimination of the Rs 1,033mn business-support-services fee
Syngene USA earns from the parent per Note 26 RPT table, or an average-vs-closing FX rate
difference) are not stated by the Company. Not a red flag on its own, but a disclosure
inconsistency worth a management question given LBF3's focus on Syngene USA/Bayview
profitability.

### D. 🟢 Syngene USA Inc.'s net assets rose despite the loss — explained by FX translation, not fresh equity, clean finding
Note 33(b) [CONSOLIDATED, p.368] shows Syngene USA Inc.'s net assets rising from Rs 4,415mn (FY25)
to Rs 4,708mn (FY26, +Rs 293mn) despite the Rs 77mn loss recognised in the same table, and despite
standalone Note 5 showing the Company's investment in Syngene USA Inc. UNCHANGED at Rs 4,339mn
(at cost) in both years — i.e., no fresh equity was injected by the parent this year. The
increase is explained by the newly-identified consolidated OCI line "Exchange difference on
translation of foreign operations Rs 403mn FY26 (vs Rs -64mn FY25)" (Note 30(b) consolidated,
p.365) — the rupee's depreciation against the dollar over the year (Rs 84.63 → Rs 88.71 per USD,
Note 28 sensitivity table, ~4.8%) inflates the INR-translated value of Syngene USA's USD-
denominated net assets. This is a genuinely clarifying finding: Bayview-related capital
deployment this year was NOT underwritten by a fresh parent equity infusion (the USD 50mn
original investment, per the Corporate Governance report p.[?], already funded the FY25
acquisition); FY26 additions sat inside Syngene USA's own balance sheet, funded by its own
capital base plus translation gain, not new parent cash.

### E. 🟡 Standalone-vs-consolidated CWIP divergence quantifies the scale of non-standalone (Bayview) capital for the first time
[STANDALONE, Note 3(a), p.242-243]: total Capital work-in-progress fell sharply from Rs 8,754mn
(FY25) to Rs 5,360mn (FY26), a 38.8% decline — a large domestic capitalisation event (a big chunk
of standalone CWIP moved into commissioned, depreciating PP&E this year; standalone PP&E rose
Rs 19,941mn → Rs 22,440mn over the same period). This corroborates Pass 1's already-flagged 71.7%
drop in standalone capital commitments (Note 31(ii)) with a matching balance-sheet-side move.
[CONSOLIDATED, Note 3(a), p.324]: total CWIP fell much less, from Rs 12,614mn to Rs 10,404mn, a
17.5% decline — because Bayview-related CWIP inside Syngene USA Inc. kept GROWING (the Rs 785mn
additional pre-operating cost, Finding resolved above). Netting standalone from consolidated CWIP
gives a new, note-derived estimate: **non-standalone (predominantly Syngene USA/Bayview) CWIP =
Rs 10,404mn - Rs 5,360mn = ~Rs 5,044mn at 31-Mar-2026** — a figure not stated anywhere directly
in the AR but derivable by subtraction across the two note sets, and now roughly AS LARGE AS the
entirety of the Company's own standalone CWIP book. This sharpens LBF3: the scale of
non-revenue-generating US capital sunk is larger, relative to the domestic capex programme, than
either note set shows in isolation.

### F. 🟢 Single operating segment (Ind AS 108) is the structural reason no CGU-level impairment disclosure exists for Bayview/Unit 3
[STANDALONE Note 32, p.278 / CONSOLIDATED Note 33, p.365]: "The Company/Group is engaged in a
single operating segment of providing contract research and manufacturing services. Accordingly,
there are no additional disclosures to be provided [under] Ind AS 108." This is new context (not
noted explicitly in Pass 1) for the Pass 1 impairment-disclosure-gap finding: because Syngene
reports as one segment, Ind AS 108 imposes no obligation to show segment- or CGU-level financial
data that would let an investor test Bayview or Unit 3 Bengaluru in isolation. The absence is
therefore a structural feature of single-segment CRDMO reporting, not a unique omission by
Syngene — though it does not reduce the substantive gap (no quantified impairment test exists for
either asset regardless of the reason).

### G. 🟢 No prior-period restatement or reclassification found on the pattern re-read
Explicit search across both note sets for "restated," "reclassified," and "regroup" turns up only
routine OCI/financial-instrument classification language (items "reclassified subsequently to
profit or loss," standard Ind AS 109/119 boilerplate) and the standard business-combination
accounting policy sentence on retrospective restatement (which is policy text, not an actual
restatement event this year). No comparative-period number in the primary statements or notes
carries a "restated" flag. Confirms and closes out this line of the pattern-pass early.

---

## PASS 2 NEW FINDINGS SUMMARY

Seven new items beyond Pass 1, plus resolution of all three carried-forward verification items:
1. 🔴 Derivative fair-value swing from +Rs 2,155mn net asset (FY25) to -Rs 1,191mn net liability
   (FY26), standalone (Note 28) — corroborates Pass 1's hedge-loss finding from a second note.
2. 🟡 Probable USD-vs-Rs-Mn unit mislabel in the FX forward/option notional table (Note 28),
   both standalone and consolidated — second proofing-quality gap alongside Pass 1's Note 43
   cross-reference error.
3. 🟡 Syngene USA Inc. FY26 loss: Board's Report says USD 1.4mn (~Rs 124-131mn); audited
   Note 33(b) attributes Rs 77mn — an unreconciled ~40% gap.
4. 🟢 Syngene USA Inc.'s net assets rose Rs 293mn on FX translation gain (Rs 403mn consolidated
   OCI line), not fresh parent equity — clarifies Bayview funding source for FY26.
5. 🟡 Standalone CWIP fell 38.8% (large domestic capitalisation) vs consolidated CWIP fell only
   17.5% (Bayview kept growing) — implies ~Rs 5,044mn of non-standalone CWIP at FY26-end, now
   comparable in size to the entire standalone CWIP book.
6. 🟢 Single-segment (Ind AS 108) reporting structurally explains, though does not excuse, the
   absence of CGU-level impairment disclosure for Bayview/Unit 3.
7. 🟢 No restatement or reclassification of prior-period figures found anywhere in either note
   set on targeted re-read.

Carry-forward resolutions: SSS Rs 315,000/share dividend confirmed as printed and numerically
implausible against SSS's own share count and profit — unresolved from the document, a
verification item for management, not an extraction error. Bayview pre-operating cost Rs 787mn
vs Rs 785mn resolved as an immaterial FX-translation rounding difference. Consolidated cash-flow-
hedge net-of-tax OCI loss resolved at Rs -2,316mn FY26 vs Rs -102mn FY25.
