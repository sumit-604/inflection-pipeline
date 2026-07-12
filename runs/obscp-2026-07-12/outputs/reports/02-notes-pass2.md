# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (VERIFICATION / CROSS-CHECK)
Company: OBSC Perfection Limited (OBSCP) | Run date: 2026-07-12
Source: runs/obscp-2026-07-12/inputs/annual-report/Annual_Report_2025.pdf (FY2024-25 Annual Report)
Method: Independent second read of AR pages 60-77 (18 pages, via Read tool `pages "60-77"`) against every
Pass 1 claim, note anchor, and figure. Pages 78-101 (blank/truncated) and pages 3-59 (corrupted font) were
NOT re-read because they remain unrecoverable and out of scope, per Pass 1's confirmed finding — this pass
does not attempt to invent content for those ranges.

---

## 0. SCOPE NOTE ON PASS 2 TASK DEFINITION

This run's task message narrows Pass 2 from the generic "what was missed" instruction in the prompt file to
a **verification/cross-check pass**: confirm every Pass 1 note reference and figure against the readable
pages, mark ✓ verified or ✗ discrepancy (stating both values), and reconcile the five primary-statement
flags Pass 1 raised. New findings surfaced incidentally during verification (i.e., things Pass 1 marked "NOT
FOUND" that are in fact partially recoverable from the readable pages, and page-anchor errors) are reported
in Sections 2 and 3 below, consistent with the prompt's underlying "what was missed" intent.

---

## 1. LINE-BY-LINE FIGURE VERIFICATION

All primary-statement figures below were independently re-derived from the Balance Sheet (p.71), P&L
(p.72), and Cash Flow Statement (p.73), which are stated in the source **"Rs in lakhs"** (confirmed on all
three statement headers) and converted to ₹ Cr by dividing by 100, matching Pass 1's convention.

| # | Pass 1 claim | Note cited | Re-verified value (lakhs, source) | Status | Notes |
|---|---|---|---|---|---|
| 1 | Share Capital ₹24.45 Cr FY25 vs ₹17.85 Cr FY24, +37.0% | Note 3, p.71 | 2,445.24 vs 1,785.00 | ✓ | Exact match |
| 2 | Reserves & Surplus ₹79.54 Cr vs ₹12.22 Cr, +550.6% | Note 4, p.71 | 7,953.80 vs 1,222.10 | ✓ (rounding) | Precise growth = **+550.8%**, not 550.6% (7,953.80−1,222.10)/1,222.10 = 5.5082. Immaterial 0.2pp rounding drift, not a data error. |
| 3 | Long-term Borrowings ₹20.02 Cr vs ₹25.60 Cr, −21.8% | Note 5, p.71 | 2,002.39 vs 2,559.65 | ✓ | Exact match |
| 4 | Deferred Tax Liability (net) ₹0.76 Cr vs ₹1.54 Cr, −50.4% | Note 6, p.71 | 76.28 vs 153.83 | ✓ | Exact match |
| 5 | Long-term Provisions ₹0.17 Cr vs ₹0.08 Cr | Note 7, p.71 | 16.78 vs 7.76 | ✓ | Exact match |
| 6 | Short-term Borrowings ₹6.95 Cr vs ₹15.88 Cr, −56.2% | Note 8, p.71 | 694.96 vs 1,587.60 | ✓ | Exact match |
| 7 | Trade Payables ₹25.31 Cr vs ₹11.59 Cr, +118.3% | Note 9, p.71 | 2,530.87 vs 1,159.21 | ✓ | Exact match |
| 8 | Short-term Provisions ₹(0.27) Cr vs ₹0.66 Cr (negative) | Note 11, p.71 | (27.34) vs 66.48 | ✓ | Exact match; negative sign confirmed real — see §2.5 reconciliation |
| 9 | Inventories ₹26.69 Cr vs ₹14.91 Cr, +79.0% | Note 14, p.71 | 2,668.68 vs 1,490.56 | ✓ | Exact match |
| 10 | Trade Receivables ₹34.93 Cr vs ₹21.53 Cr, +62.3% | Note 15, p.71 | 3,493.44 vs 2,152.94 | ✓ | Exact match |
| 11 | Total Balance Sheet ₹158.55 Cr vs ₹86.51 Cr, +83.2% | p.71 | 15,855.08 vs 8,650.59 | ✓ | Exact match; balance sheet also internally re-footed and ties (assets = liabilities = 15,855.08 both years) |
| 12 | Income from Operations ₹142.79 Cr vs ₹115.03 Cr, +24.1% | Note 18, p.72 | 14,278.92 vs 11,503.03 | ✓ | Exact match |
| 13 | Other Income ₹2.41 Cr vs ₹1.08 Cr | Note 19, p.72 | 241.23 vs 108.38 | ✓ | Exact match |
| 14 | Consumption & Mfg Expenses +34.4% | Note 20, p.72 | 9,364.76 vs 6,966.78 | ✓ | Exact match. **Additional context**: if Purchases-Finished/Traded goods (1,843.08 vs 1,979.67) are added to form a fuller "purchase base," combined growth is only **+25.3%** (11,207.84 vs 8,946.45), which makes the +118.3% Trade Payables growth look even more disproportionate than the Note 20-only comparison implied. |
| 15 | Change in inventories ₹(6.20) Cr vs ₹(4.11) Cr | Note 21, p.72 | (620.14) vs (411.34) | ✓ | Exact match |
| 16 | Finance costs ₹3.12 Cr vs ₹2.69 Cr, +16% | Note 23, p.72 | 312.23 vs 268.88 | ✓ | Exact match |
| 17 | PBT ₹20.63 Cr | — | 2,063.49 | ✓ | Exact match |
| 18 | Provision for Tax ₹4.65 Cr | — | 465.00 | ✓ | Exact match |
| 19 | Deferred Tax Adjustment ₹(0.78) Cr credit vs ₹0.38 Cr charge | Note 6, p.72 | (77.55) vs 38.07 | ✓ | Exact match |
| 20 | Effective tax rate ≈18.8% | derived | 387.45/2,063.49 = 18.78% | ✓ | Confirmed: total tax = Provision (465.00) + Tax W/back (0) + Deferred Tax Adj (−77.55) = 387.45 lakh; PBT − total tax = 1,676.04 lakh = PAT, which ties exactly to "Transferred to Reserves" on the P&L. Full waterfall independently re-derivable and internally consistent. |
| 21 | PAT ₹16.76 Cr | "Transferred to Reserves," p.72 | 1,676.04 | ✓ | Exact match |
| 22 | Basic EPS 6.85, Diluted EPS 8.12 (FY25); Basic=Diluted=6.84 (FY24) | Note 26, p.72 | confirmed verbatim | ✓ (transcription); ✗ (arithmetic sense) | Pass 1's transcription is byte-for-byte accurate. The anomaly is **in the source document itself**, not a Pass 1 extraction error — see §2.1 reconciliation. |
| 23 | OCF ₹8.85 Cr vs PAT ₹16.76 Cr, ~52% conversion | p.73 | 884.92 / 1,676.04 = 52.79% | ✓ | Exact match — see full bridge in §2.2 |
| 24 | "[Increase]/Decrease in Current Assets" ₹(26.81) Cr vs ₹(9.57) Cr | p.73 | (2,680.74) vs (956.51) | ✓ | Exact match |
| 25 | "Increase/[Decrease] in borrowings" ₹(14.50) Cr vs +₹8.07 Cr | p.73 | (1,449.89) vs 806.76 | ✓ | Exact match |
| 26 | "Increase in Share Capital & premium" ₹57.16 Cr | p.73 | 5,715.92 | ✓ | Exact match |
| 27 | Interest income ₹0.86 Cr (within Other Income) | p.73 | 86.35 | ✓ | Exact match; implies ~₹1.55 Cr of Other Income is non-interest and remains unexplained (composition note in truncated zone) |
| 28 | EPCG FOB ₹8.09 Cr / duty exemption ₹1.35 Cr / export obligation 6x over 6 years, blocks "50%"+"60%" | Note 2.3(b), p.76 | Rs 8,08,68,765 / Rs 1,34,78,128 / "1st to 4th year (1st Block) – 50%" and "5th to 8th year (2nd Block) – 60%" | ✓ (figures); ✗ (page anchor, see §3.3); confirms wording, not OCR artifact | See §3.4 — verbatim confirmed on independent re-read; the 50%+60% (summing to 110%, and "5th to 8th year" spanning 4 years within a stated 6-year total obligation window) is now confirmed to be a genuine internal inconsistency in the AR's own drafting, not an OCR/scan artifact, since two independent extractions of the same page produced identical text. |
| 29 | CSR ₹18.04 Lakh to Swachh Paryavaran Trust | CARO para xx, p.68 | "Rs. 18.04 Lakh to Swachh Paryavaran Trust ... section (5) of section 135" | ✓ | Exact match, page confirmed |
| 30 | Auditor CARO (xix) no-going-concern-uncertainty opinion | p.68 | confirmed verbatim | ✓ | Exact match |
| 31 | Audit trail (edit log) voucher-amendment finding | Auditor's Report, p.62-63 | confirmed verbatim, spans p.62→p.63 | ✓ | Page anchor correct as originally cited |
| 32 | CFO/Director dual role (Sanjeev Verma); Lekha family board (Saksham, Ashwani) | signature blocks, pp.71-73 | confirmed on all three statements | ✓ | Exact match |

---

## 2. RECONCILIATION OF THE FIVE PRIMARY-STATEMENT FLAGS

### 2.1 Diluted EPS (8.12) > Basic EPS (6.85) — UNRESOLVED, confirmed genuine source anomaly
Re-verified verbatim on P&L p.72, Note 26: "Earnings per Equity Share of Rs 10 — Basic 6.85, Diluted 8.12"
(FY25) against "Basic 6.84, Diluted 6.84" (FY24, no dilution effect). Under AS 20 (the applicable standard,
since this company reports under the "Medium Companies" AS framework, not Ind AS — confirmed Note 2.1(a),
p.74), dilutive potential equity shares can only ever add to the weighted-average denominator, which can
only hold Diluted EPS ≤ Basic EPS, never higher, absent an anti-dilutive override (and anti-dilutive
instruments are excluded from the diluted calc by definition, which would make Diluted = Basic, not exceed
it). **This is confirmed present in the audited, signed financial statements as filed** — it is not a
Pass 1 transcription error, an OCR artifact, or resolvable from any information on the readable pages. The
weighted-average share count reconciliation that would explain it sits in the Note 26 detail, which is in
the truncated zone (note-pages 5-6 of 6, beyond AR p.77). **Status: cannot be reconciled from source. Stands
as the single highest-priority open question for management / a clean copy of the AR.**

### 2.2 OCF ₹8.85 Cr vs PAT ₹16.76 Cr (52% conversion) — FULLY RECONCILED, no missing-note dependency
Both figures and the entire bridge between them are confirmed directly from the Cash Flow Statement (p.73)
and do not depend on any truncated note:
- PBT before tax: ₹20.63 Cr
- Add back: Depreciation & amortisation ₹4.05 Cr, Interest & finance charges ₹3.12 Cr; less Profit on sale
  of assets ₹(0.04) Cr, Interest income ₹(0.86) Cr
- Operating cash flow before working capital changes: **₹26.91 Cr**
- Less: Increase in Current Assets ₹(26.81) Cr (receivables + inventory buildup, confirmed §1 rows 9-10)
- Add: Increase in Current Liabilities **₹14.39 Cr** (largely the confirmed +118.3% Trade Payables growth,
  §1 row 7) — this line partially offsets the current-asset buildup and was not separately quantified in
  Pass 1's narrative; it is the direct financing counterpart to the payables-stretching flag
- Cash generated from operations: **₹14.48 Cr**
- Less: Direct taxes paid ₹(5.64) Cr
- **Net cash from operating activities: ₹8.85 Cr**, vs PAT ₹16.76 Cr → 52.79% conversion, confirmed.
This is a mechanically complete, self-consistent reconciliation entirely from readable pages. The
qualitative *cause* of the receivables/inventory buildup (customer concentration, ageing, obsolescence)
remains unavailable (Notes 14/15 sub-schedules truncated), but the *quantum* of the cash-conversion gap is
fully evidenced, not merely asserted.

### 2.3 Trade Receivables +62.3% / Inventory +79.0% vs Revenue +24.1% — CONFIRMED, ageing detail remains lost
All three growth rates independently re-verified (§1 rows 9, 10, 12). No new resolution possible on
ageing, single-customer concentration, or ECL adequacy — Notes 14 and 15 sub-schedules remain in the
truncated zone (pp.78-101).

### 2.4 Trade Payables +118.3% vs expense-base growth — CONFIRMED, MSME/ageing detail remains lost
Confirmed (§1 row 7). Refined comparison base per §1 row 14 (Consumption+Purchases growth of +25.3% rather
than Note-20-only +34.4%) makes the payables/purchase-base growth gap even wider than Pass 1 characterised.
No MSME ageing or supplier-specific detail recoverable — Note 9 sub-schedule truncated.

### 2.5 Negative Short-term Provisions ₹(0.27) Cr — CONFIRMED as a genuine, arithmetically real negative balance
Independently re-verified the Balance Sheet subtotal arithmetic: Short-term Borrowings (694.96) + Trade
Payables (2,530.87) + Other Current Liabilities (162.10) + Short-term Provisions (−27.34) = 3,360.59, which
is the exact printed "Current Liabilities" total on p.71. This confirms the negative sign is not a
transcription or OCR artifact — it is baked into the audited balance sheet's own arithmetic (the total only
foots correctly if Short-term Provisions is treated as −27.34). **This raises the confidence that it is a
genuine reclassification/over-accrual-reversal event rather than a presentation error**, but the specific
mechanism (which provision reversed, and why) remains unavailable — Note 11 movement schedule is in the
truncated zone. Status: confirmed real, cause still unresolved, stands as a named management question.

---

## 3. NEW FINDINGS SURFACED DURING VERIFICATION (Pass 1 gaps/errors corrected)

### 3.1 Related-party loan balance is PARTIALLY recoverable — Pass 1 overstated the "NOT FOUND" scope
Pass 1 stated (Section 6, Investments): *"ICDs/loans given (to whom, amount, rate, tenure): confirmed to
exist ... but amounts NOT FOUND IN DOCUMENT."* This is not fully accurate. CARO Annexure A para iii)(A)-(B)
(p.65) explicitly states the aggregate loans/advances to subsidiaries and joint ventures are disclosed
under **"Note: 13 of Loans & Advances."** The Balance Sheet (p.71) has a line item **Long-term Loans &
Advances, Note 13: ₹1.5293 Cr (152.93 lakh) as at 31 Mar 2025 vs ₹0.9999 Cr (99.99 lakh) as at 31 Mar
2024 — +52.9% YoY.** This is the readable, aggregate balance-sheet total for the related-party
current-account lending CARO describes; it is available from the primary statements even though the
sub-schedule detail (counterparty names, individual balances, interest rates, tenure) that would normally
sit inside Note 13's own text is in the truncated zone. **Correction to carry forward: related-party
lending exposure is bounded/quantified in aggregate (₹1.53 Cr, growing) even though it cannot be
decomposed by counterparty.** This is a new, material data point Pass 1 missed despite having the Balance
Sheet in hand.

### 3.2 Litigation note reference (Note 29) — page anchor corrected
Pass 1 cited: *"Independent Auditor's Report (p.61, clause (g)(i))... Refer Note No. 29."* Re-verified
location: this clause is on **AR p.63** (Auditor's Report internal "Page 4 of 11"), not p.61. p.61 is the
"Management's responsibility" section, which does not contain this reference. **✗ discrepancy — corrected
anchor: p.63, not p.61.**

### 3.3 EPCG capital goods note (Note 2.3(b)) — page anchor corrected
Pass 1 cited the entire EPCG paragraph, including the FOB value (₹8.09 Cr) and duty exemption (₹1.35 Cr)
figures, as "(Note 2.3(b), p.76)." Re-verified: the FOB value and duty exemption sentence is the **last
sentence on p.75** (end of Note 2.3(b), opening clause); only the export-obligation continuation (6x duty
saved, 6-year block structure, Authorization date 26-12-2024) is on p.76. **✗ discrepancy — FOB/duty figures
anchor to p.75, not p.76; export-obligation detail correctly anchors to p.76.** Both pages should be cited:
"Note 2.3(b), pp.75-76."

### 3.4 Statutory dues overdue (Note 10 reference) — page anchor corrected
Pass 1 cited: *"CARO Annexure A, para vii(b), p.67... except those stated in the Note No. 10 on Accounts."*
Re-verified location: CARO para vii)(a)-(b) is on **AR p.66** (internal "Page 7 of 11"), not p.67.
**✗ discrepancy — corrected anchor: p.66, not p.67.** New context recoverable: the Balance Sheet's "Other
Current Liabilities" line (Note 10, p.71) — the same note number CARO points to — totals ₹1.62 Cr FY25 vs
₹1.09 Cr FY24 (+48.8% YoY). Whatever the overdue-statutory-dues amount is, it is bounded above by this ₹1.62
Cr aggregate balance (which also includes other unrelated current-liability items); the specific overdue
quantum within it remains unrecoverable (Note 10 sub-schedule truncated).

### 3.5 RPT note-number-illegible finding — page anchor corrected
Pass 1 cited: *"CARO Annexure A, para xiii, p.68 ... reported in Note No. ___."* Re-verified location: CARO
para (xiii) is on **AR p.67** (internal "Page 8 of 11"), not p.68. **✗ discrepancy — corrected anchor: p.67,
not p.68.** The blank/illegible note number is independently reconfirmed on this second read — the source
literally prints "Note No.    to the financial statements" with the number omitted; this is not a Pass 1 or
OCR failure, the source document itself has the blank.

### 3.6 "Loans to subsidiaries/JVs" (CARO para iii) — page range narrowed
Pass 1 cited "pp.65-66" for CARO para iii (a-f), covering the Note 13 loans disclosure. Re-verified: all of
para iii)(a) through iii)(f), including both "Note: 13 of Loans & Advances" references, sits entirely on
**AR p.65** (internal "Page 6 of 11"); it does not extend onto p.66. **Minor discrepancy — narrow to p.65
only.** (Items ix(a)-(d) — the no-default/no-wilful-defaulter/term-loan-purpose findings Pass 1 anchored to
"p.67" — are also corrected: these are on **p.66**, not p.67; items ix(e)-(f) are the ones on p.67.)

### 3.7 Note-numbering label imprecision (immaterial)
Pass 1 labelled the "Basis of preparation" policy sub-section as "Note 2.1(a)-(b), p.74." The source
document's own internal numbering actually reads "**1** Basis of preparation of Financial Statements: a) ...
b) ... c) ..." (an un-parented "1," not "2.1") on p.74, with "**2.1** Method of accounting" beginning
separately on p.75. Page and content are both correct in Pass 1; only the note-numbering label is
imprecise. Immaterial, noted for completeness only.

---

## 4. ITEMS CONFIRMED AS GENUINELY NOT RECOVERABLE (no change from Pass 1)

Re-verification did not surface any additional recoverable content for: full RPT table (party/nature/
amounts), contingent liabilities table (Note 29 itself), receivables/inventory ageing (Notes 14/15),
borrowings instrument table (Notes 5/8 detail), trade payables MSME ageing (Note 9 detail), provisions
movement/actuarial assumptions (Notes 7/11 detail), deferred tax reconciliation (Note 6 detail), revenue
disaggregation (Note 18 detail), EPS weighted-average reconciliation (Note 26 detail), CSR required-vs-actual
computation, capital commitments, segment reporting, or financial instruments/fair value disclosures. All
remain "NOT FOUND IN DOCUMENT — AR pages 78-101 truncated," consistent with Pass 1.

---

## 5. SOURCE PAGE MAP — CORRECTED

| AR page | Content | Internal Auditor's-Report pagination |
|---|---|---|
| 60 | Auditor's Report — Opinion | Page 1 of 11 |
| 61 | Management's responsibility | Page 2 of 11 |
| 62 | Auditor's responsibilities (b-e); audit trail para begins | Page 3 of 11 |
| 63 | Audit trail para concludes; Section 143(3) items incl. **Note 29 litigation reference**; signed | Page 4 of 11 |
| 64 | Annexure A: i)a) – ii)a) | Page 5 of 11 |
| 65 | Annexure A: ii)b) – iv) — **incl. both Note 13 loans-to-subsidiaries references (iii)(A)/(B))** | Page 6 of 11 |
| 66 | Annexure A: v) – ix)(d) — **incl. statutory dues Note 10 reference (vii)(b))** | Page 7 of 11 |
| 67 | Annexure A: ix)(e) – xiii) — **incl. blank/illegible RPT note-number reference (xiii)** | Page 8 of 11 |
| 68 | Annexure A: xiv) – 4) — **incl. going-concern (xix) and CSR (xx)**; signed | Page 9 of 11 |
| 69-70 | Annexure B (ICFR) | Page 10-11 of 11 |
| 71 | Balance Sheet | — |
| 72 | Statement of Profit & Loss — **incl. EPS anomaly (Note 26)** | — |
| 73 | Cash Flow Statement | — |
| 74 | Notes p.1/6: Note 1 (Corporate Info); Note 2, "1 Basis of preparation" (a-c) | — |
| 75 | Notes p.2/6: Note 2.1 (Method of accounting, a-i); Note 2.2 (Provisions); Note 2.3(a); **Note 2.3(b) opens — FOB/duty exemption figures here** | — |
| 76 | Notes p.3/6: **Note 2.3(b) concludes — export obligation detail**; Note 3 (Investments — "no investments at present"); Note 4 (Inventory valuation policy) | — |
| 77 | Notes p.4/6: Note 5 (PP&E/Depreciation policy, i-xi); Note 5.2 (Amortisation) | — |
| 78-101 | Blank / truncated — Notes p.5-6/6 (rest of Note 2) + entire Notes 3-29 schedule package | Not recoverable |

---

# PASS 2 NEW FINDINGS SUMMARY

**New findings not covered (or mis-anchored) in Pass 1:**

1. **Related-party loan balance IS partially recoverable** — Long-term Loans & Advances, Note 13, p.71:
   ₹1.53 Cr FY25 vs ₹1.00 Cr FY24 (+52.9% YoY), the aggregate balance-sheet total for the subsidiary/JV
   current-account lending CARO describes. Pass 1 marked this "amounts NOT FOUND IN DOCUMENT," which
   overstated the gap — the aggregate is available, only the counterparty-level breakdown is truncated. 🟡
2. **Five page-anchor corrections**: litigation Note 29 reference is p.63 (not p.61); statutory dues Note 10
   reference is p.66 (not p.67); RPT blank-note-number reference is p.67 (not p.68); CARO para iii
   (loans to subsidiaries) is p.65 only (not p.65-66); ix(a)-(d) no-default findings are p.66 (not p.67).
   EPCG FOB/duty figures anchor to p.75, not p.76 (only the export-obligation continuation is p.76). None of
   these change the substance of any finding; all change only the page citation.
3. **Full OCF-to-PAT bridge is completely reconstructable from readable pages alone** (§2.2) — this was not
   previously laid out as a full waterfall in Pass 1; it shows the ₹14.39 Cr increase in current liabilities
   (payables-driven) partially offsetting the ₹26.81 Cr current-asset buildup, which is new explanatory
   detail, not a new number.
4. **Negative Short-term Provisions balance is confirmed arithmetically genuine**, not a transcription
   artifact — the current-liabilities subtotal (₹33.61 Cr) only foots correctly with Short-term Provisions
   entered as −₹0.27 Cr. Raises confidence this is a real reclassification/reversal event rather than a
   presentation error, though the specific cause remains unrecoverable. 🟡
5. **EPCG export-obligation block wording (50%+60%, "5th to 8th year" within a 6-year total) is now
   confirmed verbatim across two independent extractions of the same page** — no longer characterised as a
   possible OCR artifact; it is a genuine internal drafting inconsistency in the AR itself. 🟡
6. **Diluted EPS > Basic EPS anomaly stands exactly as Pass 1 reported it** — confirmed byte-for-byte
   accurate transcription, confirmed unexplainable from any readable page, confirmed as an anomaly in the
   filed financial statements themselves rather than an extraction error. No new resolution. 🔴

**All five primary-statement flags Pass 1 raised are reconciled in §2 above**: three (receivables +62%,
inventory +79%, payables +118%) are simple confirmations with no new resolution possible; one (OCF vs PAT)
is now fully bridged from readable pages with no missing-note dependency; one (negative short-term
provisions) is upgraded from "unusual, unexplained" to "arithmetically confirmed real, mechanism still
unexplained." The Diluted EPS anomaly remains fully unresolved and is the single highest-priority open
item carried into Pass 3.
