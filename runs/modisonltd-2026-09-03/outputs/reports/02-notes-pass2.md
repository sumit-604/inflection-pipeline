# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Company: MODISON LTD | Run date: 2026-09-03 | Source: FY2025-26 Annual Report (standalone Notes 1-67 pp.145-186; AGM Notice pp.5-33; Standalone/Consolidated Cash Flow Statements pp.142/204)

Method: re-read Notes 1-67 end to end against the Pass 1 output, then followed the two specific items the orchestrator flagged for resolution this pass (Note 43 RPT table misalignment; Note 53 garbled content), and separately searched the wider document (AGM Notice, Cash Flow Statement) for material that stress-tests or independently cross-validates Pass 1's headline findings. This is standard "cross-references between notes and what they reveal" territory per the Pass 2 brief, not a departure from it: the AGM Notice and Cash Flow Statement both directly speak to numbers Pass 1 already flagged (Note 43 RPT ceiling; Note 11/12/50 working-capital deterioration).

═══════════════════════════════════════════
## A. NOTE 43 RPT TABLE — RESOLVED (item a)
═══════════════════════════════════════════

Re-read Note 43(B)/(C) (pp.174-175, both standalone and the identical consolidated copy at Note 42(B)/(C), pp.237-238) character by character. The underlying PDF-to-text extraction genuinely separates the numeric column block from the row-label block for this table (confirmed: the same scramble pattern repeats identically in the consolidated notes, so it is a structural table-extraction artifact, not a one-off error). Row-by-row reconstruction from position alone remains **not fully verifiable** from the text extract for every line. However, an **independent, cleanly-formatted, non-garbled source elsewhere in the same annual report resolves the specific question asked**:

**AGM Notice, Resolution 5 (Material RPT with Modison Copper Private Limited), Explanatory Statement, Part A(3)(1) (printed p.28, PDF page marker "PAGE 30"):**
> "Total amount of all the transactions undertaken by the listed entity... with the related party during the last financial year [FY2025-26]... Purchase / sale of goods and availing as well as rendering of services... **Rs. 5,041.74 Lakhs**" (₹50.4174 cr)

This is disclosed as **11.27% of the Company's FY26 consolidated turnover of ₹709.577 cr** (AGM Notice Part A(4)(3), printed p.28-29) — the company itself classifies this as a **material RPT under SEBI LODR Reg. 23(4)**. It is also disclosed as **48.76% of MCPL's own FY26 turnover of ₹164.0688 cr** (AGM Notice Part A(4)(5), printed p.29) — i.e. Modison Ltd is close to half of MCPL's total business, a related-party commercial-dependency fact not visible anywhere in the Note 43 table itself. 🟡 New finding — worth a management question on pricing power in that relationship (which side has leverage).

**Cross-validation of Pass 1's tentative pairing**: Note 43(B)'s "Purchase of Goods" line (₹42.29 cr) + "Sale of Goods" line (₹7.57 cr) = ₹49.86 cr, against the independently disclosed AGM total of ₹50.42 cr — a residual of only ₹0.56 cr, plausibly the "Sale of Plant & Machinery — Modison Copper Private Limited" line item visible in the same table (label present at both pp.174 and 237 of the standalone/consolidated notes, value not isolable) plus/minus minor rounding or GST treatment. **This raises confidence in Pass 1's row/label pairing from 🟡 Watch to high-confidence** — the two independently-sourced totals reconcile to within 1.1%. 🟢 (resolves Pass 1's data-quality flag on this specific figure)

**CORRECTION to Pass 1's ceiling characterisation — material**: Pass 1 described the ₹80 cr figure as a "two-year Board-approved ceiling" already "more than half... used in year one." This is **not accurate on re-read**. The Resolution 5 text (AGM Notice p.5-6, explanatory statement p.27-28) states the ₹8,000 Lakhs (₹80 cr) ceiling is for **transactions the Board is seeking approval to enter into going FORWARD**, for the period "commencing from April 1, 2026 up to the conclusion of the Annual General Meeting... for financial year 2026-27" — i.e. a roughly 15-17 month FORWARD-looking ceiling for FY26-27 plus stub, split ₹65 cr purchase + ₹15 cr sale (AGM Notice Part A(4)(1)/(5), p.28-29). It does **not** retroactively cover the FY25-26 transactions already booked in Note 43; those are a separate, already-completed ₹50.42 cr actual (above). Restated correctly: **the Board is proposing a forward ceiling (₹80 cr) that is ~59% above last year's actual combined RPT value with MCPL (₹50.42 cr)** — this reads as the company proactively sizing up its sanctioned RPT headroom to accommodate expected growth in the relationship, not as a ceiling already under strain. 🟡 Watch (revised characterisation) — still worth monitoring FY27 actual utilisation against the ₹80 cr cap, but the "risk" framing in Pass 1 (ceiling half-used already) should be dropped; replace with "RPT scale with MCPL growing materially, board formally expanding sanctioned headroom."

(AGM Notice, Resolution 5 and Explanatory Statement, printed pp.5-6 and 26-31; Note 43(B)/(C) pp.174-175; Note 42(B)/(C) consolidated pp.237-238)

═══════════════════════════════════════════
## B. NOTE 53 — RESOLVED (item b)
═══════════════════════════════════════════

Re-read the extraction around printed p.183 (between Note 52 Trade Payables ageing and Note 54 CSR) line by line. **Note 53 is not a distinct MSME or provisions note.** It is the same PDF-extraction artifact as Note 43: the numeric ageing table for Note 52 (Trade Payables ageing schedule, split by (i) MSME, (ii) Others, (iii) Disputed dues-MSME, (iv) Disputed dues-Others, each across the four ageing buckets) extracted its numbers as one block (already fully captured in Pass 1 Section 8 — MSME ₹0.3296 cr FY26 ties exactly to the ₹32.96 Lakh "MSME" row here), and the bare numeral "53" precedes a **second block that is just the row/column text labels for that same Note 52 table**, re-stated ("(ii) Others," "Balance as at 31st March 2025," "(iii) Disputed dues – MSME," etc.) — no new figures.

The one substantive item physically located inside this same block (immediately after the label fragments, before Note 54 begins) is the **Labour Codes past-service-cost narrative** — already fully quantified and flagged by Pass 1 (₹0.9895 cr / 98.95 Lakhs charged to P&L, 21-Nov-2025 Labour Codes notification) but Pass 1 cited it only as "unnumbered note between 52-54." **This resolves that citation: the correct anchor is Note 53, p.183.** No new quantitative content beyond what Pass 1 already extracted. 🟢 Gap closed, no new number, one citation corrected (unnumbered → Note 53).

(Note 52/53, p.183; Note 25.1 p.161-162 for MSME cross-tie; Labour Codes narrative, Note 53, p.183)

═══════════════════════════════════════════
## C. CASH FLOW STATEMENT — MAJOR NEW CROSS-VALIDATION (stress-test of receivables/inventory finding)
═══════════════════════════════════════════

Pass 1 correctly identified the balance-sheet-side working-capital deterioration from Notes 11, 12, 50 but did not have — and this pass located — the **Standalone Cash Flow Statement (printed p.142)** and its near-identical **Consolidated counterpart (printed p.204)**. These convert Pass 1's ratio-based finding into hard, audited cash numbers and materially **raise the severity** of the existing FLAG-CASH:

| Line | FY26 (₹ cr) | FY25 (₹ cr) |
|---|---|---|
| Net Profit before tax | 96.9368 | 33.5410 |
| Operating Profit Before Working Capital Changes | 124.8373 | 44.2488 |
| Inventories (WC change, cash outflow) | **(100.9935)** | (31.3740) |
| Trade Receivables (WC change, cash outflow) | **(73.2114)** | (18.4796) |
| Total WC adjustment | (166.9379) | (52.5961) |
| Cash Generated from Operations | (42.1006) | (8.3473) |
| Direct Taxes Paid | (22.0775) | (7.7482) |
| **Net Cash From Operating Activities** | **(64.1781)** | **(16.0955)** |
| Net Increase in Borrowings (Financing) | 101.5334 | 41.0490 |
| Dividend Paid (cash) | (14.6025) | (11.3575) |

(Standalone Cash Flow Statement, p.142; Consolidated Cash Flow Statement, p.204 — the two are within ₹0.01-0.1 cr of each other throughout, confirming Pass 1's note that consolidated ≈ standalone)

🔴 **New Red Flag, materially strengthens FLAG-CASH**: Operating cash flow was **negative in BOTH years** and got **~4x more negative** in FY26 (-₹64.18 cr vs -₹16.10 cr) even as PBT nearly tripled (₹96.94 cr vs ₹33.54 cr) and EPS grew from ₹7.61 to ₹22.36. The entire ₹124.84 cr of operating profit generated before working-capital changes was consumed, and then some, by the ₹166.94 cr swing into working capital (inventory alone absorbed ₹100.99 cr of cash, receivables ₹73.21 cr) — this is the cash-flow-statement confirmation of exactly the balance-sheet pattern Pass 1 flagged from Notes 11/12/50, but expressed in absolute cash terms it is far starker than a set of ratios conveys. The shortfall was funded almost entirely by **₹101.53 cr of net new borrowings** — which reconciles closely to Note 24's total-borrowings increase of ₹101.71 cr (₹174.47 cr FY26 less ₹72.76 cr FY25) — directly corroborating Spear F2 with a second, independent primary-statement source, not just the Notes.

🔴 **New finding**: the Company paid a **cash dividend of ₹14.60 cr in FY26** (Note 55: ₹5.50/share declared) in the same year operating cash flow was **negative ₹64.18 cr** — the dividend was, in substance, debt-funded, not free-cash-flow-funded. This did not appear in Pass 1 because Note 55 discloses only the per-share/declared amounts, not the cash-paid figure or its funding source; only the Cash Flow Statement makes the funding relationship visible. 🔴 Feeds FLAG-CASH; a governance/capital-allocation question worth raising directly with management (why maintain/raise the payout ratio into a year of negative operating cash flow and 139.8% debt growth).

🟢 **Minor reconciling item, no concern**: CFS shows a "Loss due to Fire" non-cash addback of ₹10.2104 cr, ₹0.4242 cr less than Note 39's total fire loss of ₹10.6346 cr. The ₹0.4242 cr gap ties exactly to the GST-reversal component of the fire loss (Note 39/fire narrative, p.166/186), which is evidently treated as a cash/tax item elsewhere in the CFS reconciliation rather than added back as non-cash. This is a clean, fully explainable tie-out — a positive data-quality signal, not a flag.

(Standalone Cash Flow Statement, p.142; Consolidated Cash Flow Statement, p.204; cross-checked against Note 24 p.161-162, Note 41 p.166, Note 39 p.166, Note 55 p.166 & 183-184)

═══════════════════════════════════════════
## D. STRESS-TEST OF THE THREE SPEAR FACTS — RESULT: ALL THREE HOLD, TWO NOW DOUBLY CORROBORATED
═══════════════════════════════════════════

- **Borrowings (Note 24/41, Spear F2)**: HOLDS, now cross-validated by the Cash Flow Statement's Net Increase in Borrowings of ₹101.53 cr (Financing Activities, p.142/204), which reconciles to within 0.2% of Note 24's stated ₹101.71 cr increase. No contradiction found anywhere else in the document (Directors' Report, Auditor's Report, Additional Regulatory Information p.186 all consistent).
- **Hedging (Note 39/45, Spear F3)**: HOLDS. Re-read Note 45 in full (p.179-180, both standalone and consolidated copies) — no additional silver/tungsten commodity-derivative quantum found anywhere else in the document (Directors' Report/MD&A section was searched for "hedg", "silver", "commodity" and returned nothing beyond the Note 42(A) qualitative language and Note 45's FX-only forward table already captured in Pass 1). The disclosure-granularity gap Pass 1 flagged (commodity hedging described qualitatively, not quantified separately from FX) stands as identified; no new information closes it.
- **Vapi fire (Note 39/32/67, Spear F4)**: HOLDS and is now triple-corroborated. Pass 1 had already matched Note 39 (Exceptional Items), the fire narrative (p.186) and Note 32 (Other Income, ₹1.70 cr insurance) to the exact Lakh. This pass adds a fourth, independent tie: the Cash Flow Statement's non-cash addback of ₹10.21 cr (Loss due to Fire), which reconciles to Note 39's ₹10.63 cr total once the GST-reversal component is set aside (see Section C above). No contradiction found in the Directors' Report or Auditor's Report (both are silent on the fire beyond the notes; no separate MD&A commentary on the fire's operational impact was found in the searched text — a mild disclosure-breadth observation, not a red flag, since the notes-level disclosure is itself thorough and quantified).

No going-concern language was found anywhere in the wider document either (Directors' Report, Auditor's Reports, CARO annexures) — Pass 1's "NONE" finding stands, even against the newly-found negative operating cash flow, which is a genuine tension worth naming: **a company can show two consecutive years of negative operating cash flow, a >139% YoY borrowings increase and a debt-funded dividend, all inside a clean unqualified audit opinion with no going-concern paragraph** — this is not itself a red flag on the audit (negative operating cash flow alone does not typically trigger going-concern language when liquidity/covenant headroom exists and is undisclosed as breached), but it is the single most important thing for FTTCP and cash-conversion analysis downstream to carry forward with the numbers, not just the direction.

═══════════════════════════════════════════
## E. OTHER RE-READ, NO MATERIAL NEW FINDINGS
═══════════════════════════════════════════

Re-read Notes 1-10, 13-23, 26-38, 40, 41, 44, 46-52, 54-67 in full against Pass 1. No further new findings of investor significance. Specifically checked and confirmed NOTHING NEW on: accounting policy notes (Note 2, all sub-parts), deferred tax reconciliation (Note 23), contingent liabilities (Note 30), provisions/actuarial assumptions (Note 44), segment note (Note 47), fair value hierarchy (Note 49), CSR (Note 54 — now correctly renumbered from Pass 1's "p.183" citation, confirmed at p.184), immovable properties not in company's name (Note 56), and the Additional Regulatory Information block (pp.186, unnumbered 57-66) — all match Pass 1's extraction and ratings with no contradiction. AOC-1 Part B (Associates/JVs) was checked again: confirms Pass 1's finding that the Company has no associates or JVs; Part B of AOC-1 is present in the Directors' Report annexures but is blank/not applicable, consistent with Note 43(A)'s related-party list showing only one subsidiary at year-end (Modison HV) after Modison Solartech's divestiture. 🟢

═══════════════════════════════════════════
## PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════

1. 🔴 **Net Cash From Operating Activities was negative in both years and worsened ~4x in FY26** (-₹64.18 cr vs -₹16.10 cr), funded by ₹101.53 cr of net new borrowings — the Cash Flow Statement (p.142/204), not found by Pass 1, converts the balance-sheet WC finding into hard cash numbers and is the single biggest addition this pass. Feeds FLAG-CASH, materially raises its severity.
2. 🔴 **₹14.60 cr cash dividend paid in FY26 despite -₹64.18 cr operating cash flow** — effectively debt-funded. New finding, not visible from Note 55 alone.
3. 🟡 **Note 43 RPT ceiling correction**: the ₹80 cr MCPL ceiling is a FORWARD ~15-month ceiling for FY26-27 (not a two-year retrospective aggregate); actual FY25-26 RPT with MCPL was ₹50.42 cr (cleanly disclosed in AGM Notice, not the garbled Note 43 table), = 11.27% of company turnover and 48.76% of MCPL's own turnover. Corrects Pass 1's framing; also raises confidence in Pass 1's Note 43 row-pairing to high.
4. 🟢 **Note 53 resolved**: it is Note 52's (Trade Payables ageing) row-label continuation plus the Labour Codes narrative's correct citation (not a distinct MSME/provisions note as speculated). No new figures; one citation corrected.
5. 🟢 **Fire-loss cash flow tie-out**: CFS addback of ₹10.21 cr reconciles exactly to Note 39's ₹10.63 cr once the ₹0.42 cr GST-reversal component is excluded — positive data-quality signal.
6. All three Spear facts (borrowings, hedging, fire) re-confirmed on re-read; borrowings and fire now additionally cross-validated against the Cash Flow Statement, a fourth/independent primary-statement source not used in Pass 1.

No contradictions to Pass 1's Top 10 findings were found. No restatements found (confirmed on re-read). No going-concern language found anywhere in the wider document (confirmed on re-read), despite the newly-quantified negative operating cash flow — flagged as a tension for FTTCP to carry forward, not as an audit red flag.
