# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 OF 3 (WHAT WAS MISSED)
Company: SYSTANGO (Systango Technologies Limited) | Run date: 2026-08-29 | Model: claude-sonnet-5

Full second read of the Notes, Note 1 to the last note, both note sets (Standalone Notes 1-22,
p.76-94; Consolidated Notes 1-22, p.104-118), against the Pass 1 report at
`outputs/reports/02-notes-pass1.md`. Reporting NEW items only; anything Pass 1 already covered
is not repeated. All amounts Rs. Lakhs unless stated. Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag.

---

## PASS 2 NEW FINDINGS SUMMARY

### [1] Standalone operating cash flow DECLINED even as profit rose 43% — new cash-basis evidence for the receivables red flag
**Standalone Cash Flow Statement [p.74]:** Net Cash generated from Operating Activities fell to
**₹807.49L (FY25) from ₹822.35L (FY24)** — a decline — while Profit Before Tax rose **+39.7%**
(₹2,831.95L vs ₹2,027.12L) and PAT rose **+42.9%**. The reconciliation shows why: the "Net change
in Trade Receivables" working-capital line was an outflow of **(691.77)** in FY25 versus (464.53)
in FY24 — a worse cash drag, not a better one, even as "Operating Profit before Working Capital
Changes" rose 31.8% (₹2,222.83L vs ₹1,686.18L). 🔴 **RED FLAG** — this is the hard cash-flow-statement
evidence Pass 1's receivables/turnover-ratio finding implied but did not itself cite. The company's
own P&L profit growth is not converting to standalone operating cash at anywhere near the same rate.

### [2] Consolidated operating cash flow grew in line with profit — the cash problem is concentrated in the PARENT, not the Group
**Consolidated Cash Flow Statement [p.106]:** Net Cash from Operating Activities rose to
**₹1,238.40L (FY25) from ₹869.07L (FY24), +42.5%** — tracking consolidated PAT growth of +40.2%
(₹2,373.10L vs ₹1,692.64L) closely. This is a **material divergence from the standalone picture**
(finding [1] above, where OCF fell despite profit +43%). Corroborating evidence: the Consolidated
Trade Receivable Turnover Ratio fell only -22.07% (5.12x FY25 vs 6.58x FY24, Note 22(f) consolidated,
p.118) versus the Standalone Trade Receivable Turnover Ratio's -37.32% decline (Note 22(f)
standalone, p.93, already flagged by Pass 1). 🟡 **WATCH** — the cash-conversion deterioration Pass
1 flagged sits mainly at the parent/standalone entity, not the Group. This lines up with the RPT
billing-entity reshuffle Pass 1 already found (Systango LLC USA sales -91%, Systango INC USA sales
appearing from zero at ₹1,157.81L with a ₹353.46L year-end receivable) — worth a direct question on
whether the parent's own cash conversion is being drained by unbilled/uncollected intercompany
trade with the newly-billing US entity.

### [2b] Note 8, Non-Current Investments — STANDALONE figure independently confirmed, and it differs from the consolidated figure Pass 1 cited
Pass 1 flagged standalone Note 8 as an unconfirmed coverage gap and reported only the
**consolidated** Note 8 total (₹115.91L FY24 → ₹1,325.25L FY25, 11.4x, confirmed here again at
consolidated p.112). This pass directly confirms the **standalone** Note 8 [p.80]: Total
**₹1,424.64L (FY25) vs ₹350.53L (FY24), a +306% / 4.07x increase** — a different number and a
different growth multiple from the consolidated figure. The gap is explained by consolidation
eliminations: the standalone total includes ₹268.73L invested in wholly-owned subsidiaries
(Isystango UK, Systango INC USA — eliminated on consolidation) and ₹32.64L in the Systango
Account Aggregator LLP (also eliminated), while the consolidated total separately includes
₹35.88L in GreenLeaf TDG Ltd UK, an investment evidently held at subsidiary level and invisible in
the standalone note. 🟡 **WATCH** — resolves Pass 1's stated coverage gap; the parent entity's own
(pre-elimination) treasury/investment book is larger than the headline consolidated number implies.
Standalone Note 8 + Note 11 (current investments, ₹4,602.37L, unchanged from Pass 1) together put
total standalone investments at **~₹60.3 Cr**, against a company with ₹61.3 Cr standalone revenue.

### [3] IPO net-proceeds utilization: only 44.7% deployed more than two years after listing
**Note 21C.1 "Initial Public Offer" [standalone, p.87]:** Net IPO proceeds were ₹3,083.53L (Gross
₹3,481.92L less actual issue expenses of ₹398.39L — which itself ran **17.6% over the ₹338.79L
originally projected**). Against this, **"Amount utilized till 31-03-2025" = ₹1,378.38L, i.e. only
44.7% of net proceeds**, more than two years after the March-2023 NSE Emerge listing. No
category-wise object-of-issue utilization breakdown is given in this note (NOT FOUND: use-of-funds
schedule by stated object). 🟡 **WATCH** — this is a material, previously unreported anchor that
directly explains where the money in Pass 1's flagged investment/treasury build-up (Note 8 + Note
11, ~₹60 Cr standalone) came from: roughly ₹17 Cr of unutilized net IPO proceeds are sitting inside
that portfolio rather than being deployed into the operating business, more than two years after
the float. No consolidated equivalent of this utilization table exists (consistent with the
disclosure-gap Pass 1 already flagged for the consolidated policy notes).

### [4] Related-party PAYABLES collapsed 99% in the same year "Creditors for Expenses" collapsed 88% — an unexplained link Pass 1 did not draw (new note: Note 5)
**Note 21C.8.B.viii(c), standalone [p.91]:** Payables to related parties at FY24 year-end were
Isystango Ltd UK ₹29.65L + Systango LLC USA ₹2.97L + Systango Account Aggregator Services Pvt
Ltd ₹0.28L = **₹32.90L**, falling to essentially nil by FY25 (₹0.36L, all director sitting-fee
payables: NV Agro ₹0.90L, Narender Kabra ₹0.18L, Vikas Jain ₹0.18L — NV Agro is not a subsidiary
so the true intercompany payable is ₹0.36L). Separately, and **not covered by Pass 1 at all**,
**Note 5, "Other Current Liabilities" [standalone, p.78]** shows "Creditors for Expenses" falling
from **₹61.55L (FY24) to ₹7.15L (FY25), an 88% decline**. The ₹32.90L intercompany-payable collapse
is large enough relative to the ₹54.40L drop in Creditors for Expenses to plausibly explain most of
it, but neither note cross-references the other, and Note 4 (Trade Payables) remains NIL throughout
— so the notes as disclosed do not let a reader trace where the FY24 intercompany payable actually
sat or confirm the read. 🟡 **WATCH** — a new, genuine cross-note reconciliation gap (Note 4 vs
Note 5 vs Note 21C.8), reinforcing rather than repeating Pass 1's Note 4 (NIL trade payables)
anomaly with a fact pattern Pass 1 did not have.

### [5] Legal & Professional Charges: subsidiaries are spending far more than the parent, and the gap widened sharply
Cross-note comparison (not performed in Pass 1): **Standalone** Note 20 Other Expenses, Legal &
Professional Charges [p.84-85, already in Pass 1's other-expenses read] = ₹44.89L (FY25) /
₹30.27L (FY24). **Consolidated** Note 21 Other Expenses, Legal & Professional Charges [p.116] =
**₹156.74L (FY25) / ₹81.34L (FY24)**. The gap — legal/professional spend booked at subsidiary
level, invisible in the standalone accounts — is **₹111.85L in FY25** (up from ₹51.07L in FY24,
more than doubling), i.e. subsidiaries now spend roughly 3.5x the parent's own legal/professional
budget. No note explains this spend (litigation? cross-border structuring? the Systango LLC USA
liquidation? the DBX Holdings relationship?). 🟡 **WATCH** — new finding, a plausible additional
angle on the DBX Holdings / US-entity-restructuring questions Pass 1 already flagged for management.

### [6] Consolidated-only "Commission Expenses" line is numerically identical to CSR spend — worth a direct duplication check
**Note 21 Other Expenses, Consolidated [p.116]:** a new line, "Commission Expenses" = **₹29.29L
(FY25) / NIL (FY24)**, sits in the Administrative Expenses section. In the same note's "Others"
section, "Contribution towards CSR" = **₹29.29L (FY25) / ₹19.92L (FY24)** — the exact same FY25
figure. This line does not exist in the standalone Other Expenses note at all (NOT FOUND
standalone). 🟡 **WATCH**, minor but concrete — worth a direct management/auditor query to confirm
this is a genuine distinct subsidiary-level cost and not a copy/duplication artifact in the
consolidated schedule (the amount is immaterial to profit either way, ~0.4% of consolidated PBT).

### [7] Additional standalone/consolidated profitability ratios not extracted in Pass 1 (context, not a flag)
Note 22(xiv) [standalone, p.93-94] / Note 22(xiv) [consolidated, p.117-118] disclose, beyond the
Return-on-Investment ratio Pass 1 already cited: Return on Equity 26.10% (FY25) vs 23.44% (FY24)
standalone [26.26% vs 24.17% consolidated]; Return on Capital Employed 28.24% vs 26.28% standalone
[28.51% vs 26.91% consolidated]; Net Profit Ratio 37.83% vs 30.83% standalone (+22.71%) [35.34% vs
29.92% consolidated (+18.13%)]; Current Ratio 10.79x vs 10.30x standalone [9.24x vs 10.48x
consolidated, -11.83%]; Net Capital Turnover Ratio 0.76x vs 0.77x standalone [0.81x vs 0.79x
consolidated]. 🟢 informational — all margin/return ratios rose YoY, consistent with the reported
profit growth; included for completeness since Pass 1 did not extract the full ratio table.

### [8] Directors' remuneration, individual split (minor, new detail)
**Note 21C.8.B.ii, standalone [p.90]:** Nilesh Rathi ₹90.07L (FY25) / ₹68.98L (FY24), +30.6%;
Vinita Rathi ₹89.65L (FY25) / ₹67.96L (FY24), +31.9% — aggregating to the ₹179.72L / ₹136.94L
total Pass 1 already reported. Both promoter-directors received near-identical percentage
increases. 🟢 informational, no new concern raised.

### [9] Auditors' remuneration split (minor, new detail)
**Note 21C.9.B, standalone [p.91] / equivalent consolidated:** Audit Fees ₹1.50L, Tax Audit Fees
₹0.25L, Other Services NIL — unchanged both years, totalling the ₹1.75L Pass 1 already had.
🟢 clean, no non-audit-fee dependency signal.

---

## COVERAGE CONFIRMATION

This pass re-read, page by page: Standalone Notes 1-22 in full (p.76-94, including the Balance
Sheet/P&L/Cash Flow face statements at p.73-77 that sit ahead of Note 1) and Consolidated Notes
1-22 in full (p.104-118, including face statements p.104-107). Two of Pass 1's stated coverage
gaps for standalone Notes 6, 7, and 8 (previously "not independently confirmed, consolidated proxy
used") are now directly resolved: Note 6 (Short-Term Provisions) and Note 7 (PPE/Intangibles) match
the consolidated proxy Pass 1 used almost exactly (Note 6 Employee Benefits provision ₹255.14L /
₹258.67L identical at both levels, confirming that anomaly sits 100% at the parent), while Note 8
(Non-Current Investments) does NOT match and is corrected above at finding [2b].

No further material items were found beyond those listed above; CARO annexure clauses, the audit-
trail non-compliance finding, and the standalone/consolidated Note 22 disclosure-gap finding are
Pass 1 items and are not repeated here except where a new angle (note-numbering mismatch under
finding context, cash-flow divergence) added information Pass 1 did not have.

---

## PASS 2 NEW FINDINGS SUMMARY (short form)

1. Standalone operating cash flow fell (₹807.49L to ₹822.35L direction reversed, i.e. declined
   YoY) despite PAT +42.9% — Cash Flow Statement, p.74. 🔴
2. Consolidated operating cash flow rose in line with profit (+42.5% vs PAT +40.2%) — the cash
   conversion problem is standalone/parent-specific, not Group-wide — Cash Flow Statement, p.106. 🟡
3. Standalone Note 8 non-current investments independently confirmed at ₹1,424.64L (FY25) vs
   ₹350.53L (FY24), a different figure/multiple (4.07x) than the consolidated number Pass 1 cited
   (11.4x) — Note 8, p.80 vs p.112. 🟡
4. IPO net proceeds only 44.7% utilized (₹1,378.38L of ₹3,083.53L) more than two years post-listing
   — Note 21C.1, p.87. 🟡
5. Related-party payables collapsed 99% (₹32.90L to ₹0.36L) the same year Creditors for Expenses
   (Note 5, not covered in Pass 1) fell 88% (₹61.55L to ₹7.15L) — p.78, p.91. 🟡
6. Subsidiary-level Legal & Professional Charges (₹156.74L) now run 3.5x the parent's own
   (₹44.89L), gap more than doubled YoY — Note 20 p.84-85 vs Note 21 p.116. 🟡
7. Consolidated-only "Commission Expenses" line exactly matches CSR spend (₹29.29L both) — Note 21,
   p.116, worth a duplication check. 🟡
8. Full standalone/consolidated ratio tables (ROE, ROCE, Net Profit Ratio, Current Ratio, Net
   Capital Turnover) extracted for completeness — Note 22(xiv), p.93-94/p.117-118. 🟢
9. Individual director remuneration split and auditor fee split extracted for completeness —
   Note 21C.8.B / 21C.9.B, p.90-91. 🟢
