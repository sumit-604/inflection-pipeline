# INVESTOR PRESENTATION ANALYSIS — Vivid Electromech Limited (VIVIDEL)

Analyst: Claude Code | Model: claude-opus-4-8 | Date: 2026-09-07
Document: Updated Investor Presentation, filed with NSE 05-Sep-2026 (Reg 30). 32 PDF pages (1 cover letter + 31 deck slides). Source: `runs/vividel-2026-09-07/inputs/presentation_vividel_2026-09-05.pdf`.
Unit: figures in Rs Crore unless stated. Deck uses Rs Crore for financials, Rs Lakh for the Mechtech transaction.
Anchoring: every number carries its slide page number (p<n>) from the PDF.

## SCOPE AND GATE STATUS (read first)

- **New name.** No `companies/VIVIDEL.md` exists. No prior run on file. No SPEAR line.
- **This is a screening-stage presentation read, not a valuation.** The SPEAR GATE (CLAUDE.md) stops a new name from running shield-first. A SPEAR PASS on live web, by Claude web, must clear first. This container has no live web, so no POND/CATCH/PRICE/VERDICT and no Role 1 valuation runs here.
- **What this file delivers:** a forensic extraction of the deck, an internal-arithmetic audit, red-flag findings, the disclosure gaps, a transition-ladder read, a governance read, and the load-bearing facts a spear pass must verify first.
- **One source only.** This is a company-authored deck. Every claim is management assertion until an independent source confirms it. Filed documents beat inference; a deck is the weakest filed tier.

---

## 1. WHAT THE BUSINESS IS

- Vivid Electromech Limited. NSE Emerge (SME) symbol **VIVIDEL** (p1). Listed NSE Emerge 2026-H1 (p3).
- Maker of Low-Voltage (LV) and Medium-Voltage (MV) electrical panels and switchboards, plus automation systems (p4, p6, p5, p8). Up to 1,000 V LV; 3.3 kV to 33 kV MV.
- Incorporated 1990. In-house LV panel manufacture from 1998 (p3).
- **System integrator for global OEMs.** ABB (ArTu K licensed, system integrator for LV and MV switchboards, appointed 2019), Siemens (SIEPAN 8PU licensed), Hitachi (Hi-Rel LV drives), Lauritz Knudsen / L&T Electrical (p8, p10, p3).
- Two plants: Navi Mumbai (Unit 1, 21,500 sq ft, panel manufacture + assembly + testing + system integration) and Pune/Chinchwad (Unit 2, 12,500 sq ft, **assembly only**) (p12).
- New plant under build at Ambernath, Thane (Lodha Industrial Park). ~119,800 sq ft built-up, commercial operations expected end-October 2026 (p13).
- Archetype fit (CLAUDE.md library): **Outsourcing partner / build-to-spec component maker.** Revenue rides customer capex (data centres, metro, infra) and OEM design-wins (ArTu K, SIEPAN). ArTu K design panels alone are 64.52% of FY26 revenue (p23).

---

## 2. FINANCIAL EXTRACTION (anchored)

### 2A. Full-year P&L trajectory (Rs Cr)

| Metric | FY23 | FY24 | FY25 | FY26 | Src |
|---|---|---|---|---|---|
| Total income | 59.79 | 89.75 | 155.95 | 201.09 | p27, p25 |
| Operating revenue (with other op rev) | 59.31 | 88.91 | 155.32 | 200.14 | p19 |
| Operating revenue (ex other op rev) | 59.31 | 88.85 | 154.96 | 200.07 | p18, p20, p23 |
| EBITDA | 2.52 | 7.22 | 28.73 | 46.15 | p27 |
| EBITDA margin | 4.21% | 8.04% | 18.42% | 22.95% | p27 |
| PAT | 0.14 | 3.81 | 19.52 | 31.61 | p27 |
| PAT margin | 0.23% | 4.24% | 12.52% | 15.72% | p27 |

Growth claims (all verified in Section 3): Total income CAGR 49.8%, EBITDA CAGR 163.7%, PAT CAGR 512.1% (FY23-FY26) (p27). FY26 YoY: income +28.95%, EBITDA +60.66%, PAT +61.93% (p25).

### 2B. Half-year split, FY26 (Rs Cr)

| Metric | H2 FY25 | H1 FY26 | H2 FY26 | Src |
|---|---|---|---|---|
| Total income | 101.60 | 70.89 | 130.20 | p26 |
| EBITDA | 20.74 (20.41%) | 13.82 (19.49%) | 32.34 (24.84%) | p26 |
| PAT | 15.64 (15.39%) | 9.44 (13.32%) | 22.16 (17.02%) | p26 |

H1 FY25 implied = 155.95 - 101.60 = **54.35**. So H2 is ~65% of both FY25 and FY26 income. **The business is H2-loaded** (project execution skews to the second half). Any single-half read overstates or understates the run-rate.

### 2C. Revenue mix, FY26

- **By end-market** (p20): Data Centre & Technology **49.95%** (99.94), Industrial Mfg & Machinery 21.30% (42.62), Infra/Construction incl Metro 19.89% (39.79), Solar & Renewable 8.53% (17.07), Other 0.33%.
- **By product** (p23): LV panels **79.84%** (159.74; of which ArTu K design 64.52%, non-ArTu K 15.32%), MV panel 15.07% (30.15), traded goods 4.09%, services 0.99%.
- **By geography** (p18): Maharashtra **91.65%** (183.37), then Gujarat 2.05%, Karnataka 1.40%, others each <1%.

### 2D. Operating scale

- Customers: 77 (FY23) -> 110 (FY24) -> 109 (FY25) -> **113 (FY26)** (p19). Revenue per customer 0.77 -> 0.81 -> 1.42 -> **1.77 Cr** (p19).
- Domestic vs international (Rs Cr): FY23 58.90 / 0.42; FY24 86.37 / 2.48; FY25 152.72 / 2.24; **FY26 197.56 / 2.51** (p19).
- Capacity utilisation FY26: Navi Mumbai **94.36%** (5,048 of 5,350 verticals), Pune **70.00%** (1,505 of 2,150) (p17, p12).
- Executable order book **Rs 205 Cr** at 31-Aug-2026; execution cycle 2-9 months; 72% from existing customers, 28% new; 4 of top 10 customers 3+ years (p22).
- Data centre: 70% of DC revenue from hyperscale; avg project Rs 20-25 Cr; delivery 8 weeks to 9 months; named clients Adani Connex, STT Global Data Centres, CtrlS, NTT Data (p21).

---

## 3. INTERNAL ARITHMETIC AUDIT

Every growth and margin claim in the deck was recomputed from the deck's own figures.

| Claim (slide) | Recompute | Verdict |
|---|---|---|
| Income +28.95% YoY FY26 (p25) | 201.09/155.95 = +28.95% | PASS |
| Income CAGR 49.8% (p27) | (201.09/59.79)^(1/3)-1 = +49.8% | PASS |
| EBITDA +60.66% YoY (p25/p27) | 46.15/28.73 = +60.64% | PASS (rounding) |
| EBITDA margin 22.95% / 18.42% (p27) | 46.15/201.09 = 22.95%; 28.73/155.95 = 18.42% | PASS |
| EBITDA margin +453 bps (p27) | 22.95% - 18.42% = 453 bps | PASS |
| PAT +61.93% YoY (p25/p27) | 31.61/19.52 = +61.93% | PASS |
| PAT margin 15.72% / 12.52% (p27) | 31.61/201.09; 19.52/155.95 | PASS |
| EBITDA CAGR 163.7% (p27) | (46.15/2.52)^(1/3)-1 = +163.4% | PASS (rounding) |
| PAT CAGR 512.1% (p27) | (31.61/0.14)^(1/3)-1 ~= +509% | PASS in form, see F-2 |
| H2 FY26 income +28.16% (p26) | 130.20/101.60 = +28.15% | PASS |
| H2 EBITDA margin +443 bps (p26) | 24.84% - 20.41% = 443 bps | PASS |
| H2 PAT +41.7% YoY (p26) | 22.16/15.64 = +41.7% | PASS |
| H1+H2 FY26 income = FY26 | 70.89 + 130.20 = 201.09 | PASS |
| H1+H2 FY26 EBITDA = FY26 | 13.82 + 32.34 = 46.16 ~= 46.15 | PASS |
| H1+H2 FY26 PAT = FY26 | 9.44 + 22.16 = 31.60 ~= 31.61 | PASS |
| Rev/customer FY26 1.77 (p19) | 200.14/113 = 1.77 | PASS |
| Order book sums to 205 (p22) | Industry 98+32+75=205; Product 132+30+43=205 | PASS |
| Capacity util Navi Mumbai 94.36% (p17) | 5,048/5,350 = 94.36% | PASS |
| New capacity to 22,500 verticals (p17) | 7,150 LV + 350 MV + 15,000 new = 22,500 | PASS |

**Verdict: the deck's internal financial arithmetic is clean.** No manufactured percentages, no broken sub-totals. This raises trust in the numbers as presented. It does not verify them against audited accounts, which the deck does not contain.

---

## 4. RED-FLAG FINDINGS (anchored)

**F-1 (AMBER) — "Diversified / pan-India" narrative contradicts rising concentration.**
The deck repeats "diversified" and "pan-India" (p9, p18, p20, p29). The data shows concentration **increasing**. Maharashtra revenue share: FY23 54.5% -> FY24 51.2% -> FY25 85.9% -> **FY26 91.65%** (p18). End-market: Data Centre grew to **49.95%** of FY26 revenue (p20). The business is getting less diversified, not more. The claim and the data point opposite ways.

**F-2 (AMBER) — Headline CAGRs sit on a near-zero base.**
PAT CAGR "512.1%" and EBITDA CAGR "163.7%" (p27) are arithmetically correct but start from FY23 PAT of **Rs 0.14 Cr** and EBITDA of **Rs 2.52 Cr** (p27). A base near zero makes any CAGR look extreme. The economically honest read is the margin walk: EBITDA 4.21% -> 22.95%, PAT 0.23% -> 15.72% over three years. That is the real story; the CAGR headline inflates it.

**F-3 (AMBER) — Margin expansion is unexplained and coincides with the data-centre ramp.**
EBITDA margin rose from 4.21% (FY23) to 22.95% (FY26); +453 bps in FY26 alone (p27). Over the same window data-centre revenue climbed to half the book (p20). The deck attributes the gain to "operating leverage" (p27) but gives no gross-margin bridge, no mix effect, no price-vs-cost split. A 19-point EBITDA margin move in three years is large for a panel builder and needs a mechanism. If the margin is data-centre-mix-driven, it is exposed to that one cycle.

**F-4 (AMBER) — "Increasing contribution from international markets" is false on the deck's own figures.**
Key takeaway p19 claims rising international contribution. International revenue: FY24 2.48 -> FY25 2.24 -> FY26 2.51 Cr (p19). It is flat in rupees and **falling as a share** (2.8% of FY24 revenue to 1.25% of FY26). The claim contradicts the chart on the same slide.

**F-5 (AMBER) — Related-party acquisition of Mechtech Infrasolutions.**
Vivid raised its stake in Mechtech Infrasolutions from 1% to 99% for **Rs 99 Lakhs cash** (p14). The sellers are the promoters: pre-transaction Sameer Attavar and Meeta Attavar held the entity; post-transaction Sameer holds the residual 1% (p14). This is a promoter-to-company transfer. Absolute size is tiny (~Rs 1 Cr implied for 100%; Mechtech FY26 turnover ~Rs 2.01 Cr provisional, p14), so it is not material to value. It is material to governance: the arm's-length basis, valuation method, and audit-committee/independent approval are undisclosed and must be confirmed.

**F-6 (MINOR) — Ownership arithmetic in the Mechtech table does not foot.**
Pre-transaction partnership is stated as "Vivid 1% + Sameer 50% + Meeta 50%" = **101%** (p14). A deck slip, but in the one related-party slide it should foot. Confirm the true pre-transaction cap table.

**F-7 (AMBER) — Two revenue definitions run side by side without reconciliation.**
Operating revenue prints as **200.14** (p19) and **200.07** (p18, p20, p23), FY25 as **155.32** vs **154.96**, FY24 as **88.91** vs **88.85**. The gap is "other operating revenue" per the p18/p23 footnotes, but the deck never reconciles the two series on one page, and revenue-per-customer (p19) silently uses the higher series. Small amounts; still, one revenue number per period is the discipline.

**F-8 (AMBER) — Thin independent oversight for the risk profile.**
Board is five people (p31): promoter CMD (Sameer Attavar), promoter spouse as Whole-Time Director (Meeta Attavar), and three outsiders. The non-executive director (Hardik Shah) and one independent (Kiran Shetty) come from fashion and experiential-marketing backgrounds. The only finance-literate independent (Pratik Kabra, CA) was appointed 19-Sep-2025 and is described as having "more than 3 years" experience (p31). For a company running half its revenue through lumpy hyperscale data-centre projects, the independent bench is thin on industrial, engineering, and audit depth.

**F-9 (AMBER) — Single-half and single-year skew.**
H2 is ~65% of the year (Section 2B). FY26 growth also benefits from the data-centre ramp inside one year. A buyer reading annualised margins off H2 FY26 (24.84% EBITDA) would overstate the durable rate.

---

## 5. WHAT THE DECK DOES NOT DISCLOSE (the gaps that matter)

A panel builder that runs large project orders lives or dies on cash conversion and the balance sheet. None of it is here.

- **No balance sheet.** No debt, no net worth, no cash.
- **No working capital.** No receivables, no inventory, no payables, no cash-conversion cycle. For a project business with Rs 20-25 Cr data-centre orders and 2-9 month cycles, this is the single most important missing block. **Cash conversion is INDETERMINATE.** Per CLAUDE.md this caps any downstream verdict at PROCEED WITH CAVEATS at best, with the missing evidence named.
- **No cash flow statement.** Cannot test whether the PAT is collected.
- **No ROCE / ROE.** The deck sells a margin-and-returns story (p27 title "profitability and returns") but prints no return ratio.
- **No gross margin** and no cost bridge to explain the 19-point EBITDA-margin climb (F-3).
- **No shareholding pattern, no promoter holding, no pledge disclosure.**
- **No segment or customer profitability**, no customer-concentration percentages (only "4 of top 10 are 3+ years", p22).
- **No order-book ageing** or conversion-to-revenue history.
- **No capex figure or funding plan** for the ~119,800 sq ft Ambernath plant (p13), and no stated funding source.

---

## 6. TRANSITION-ALPHA READ (quality ladder)

This is a candidate transition, not a proven one.

- **From / To.** The margin walk (EBITDA 4.21% -> 22.95%; PAT 0.23% -> 15.72%) reads as a climb from **R1/R2 (commodity or cost-advantaged converter)** toward **R3 (value-added / spec'd supplier)**. The spec-in comes from OEM licences: ArTu K design panels are 64.52% of revenue (p23), which carry ABB approval and switching cost. That is the R3 mechanism (partial pricing power from spec-in and stickiness).
- **The re-rating engine question is unanswered here.** A rung climb is only alpha if it is real and unpriced. Whether the margin gain is durable spec-in economics (R3) or a temporary data-centre-cycle mix bump (still R2 with a good year) is exactly what the deck does not let you decide (F-3). The ArTu K share is the bull; the data-centre concentration is the doubt.
- **Rung-jump base rate.** CLAUDE.md: one rung per 2-3 years, a multi-rung leap is itself a red flag. A jump from 4% to 23% EBITDA in three years is fast. Treat it as a claim to prove, not a fact to bank.
- **Proof gate.** Not testable from a deck. The proof would be: margins hold through a soft data-centre quarter, receivables convert to cash, and non-data-centre lines carry their own weight. None is shown.

Provisional matrix placement (to be resolved only after the signed Mental Model and Stage 11, never from a deck): **RESEARCH / WATCH** territory. The climb is narrated and the numbers are internally clean, but the proof gate has not fired and cash conversion is unknown. This is not yet a trade.

---

## 7. LOAD-BEARING FACTS FOR THE SPEAR PASS (priority verification targets)

If the operator runs Vivid, these are the facts a Claude-web spear pass must land first. They are the load-bearing beams; if any fails, the thesis changes shape.

1. **Cash conversion.** Receivables days, CFO vs EBITDA, and CFO vs PAT for FY24-FY26. Does the reported PAT collect? (Fills the Section-5 gap; governs the caveat cap.)
2. **Balance sheet and debt.** Net debt, net worth, and how the Ambernath plant (~119,800 sq ft, ops end-Oct-2026, p13) is funded. Debt-funded capex changes the risk.
3. **Durability of the margin climb.** Independent gross-margin or segment-margin evidence that the EBITDA move to 22.95% is spec-in economics, not a one-cycle data-centre mix bump (F-3).
4. **Data-centre concentration risk.** Confirm the 49.95% / 70%-hyperscale figures (p20, p21) and the named-client exposure; test order-book conversion. This is the single largest revenue dependency.
5. **Promoter holding, pledge, and the Mechtech RPT** approval basis and valuation (F-5, F-6).
6. **ROCE / ROE** actuals, since the deck sells returns but shows none.

---

## 8. SCREENING VERDICT

- **This is a screening note, not a pipeline verdict.** The five-verdict set (PROCEED / PROCEED WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT EVIDENCE) applies to a signed-model pipeline run, which has not happened and cannot happen shield-first.
- **On the deck alone:** the numbers are internally consistent and the margin trajectory is genuinely striking. Against that sit five substantive flags (narrative-vs-data on diversification and international, unexplained margin, related-party deal, thin oversight) and a complete absence of balance-sheet and cash-conversion data.
- **Nothing halts.** No mechanical failure. Flags propagate; the decision stays with the operator (CLAUDE.md).
- **Next step per the gate:** if Vivid is worth pursuing, run a **SPEAR PASS on Claude web first** (POND, CATCH, PRICE, VERDICT against CMP), carrying the six load-bearing facts in Section 7 as the first verification priority. Only a SPEAR HIT or an explicit operator override opens the heavy pipeline. Until then, no `companies/VIVIDEL.md` Spear line exists, so `/run-pipeline` and `/fttcp` must not run this name.

---

## 9. NARRATIVE (STE)

Vivid builds electrical panels. It assembles designs licensed from ABB, Siemens, and Hitachi. Three years ago it barely made a profit. Last year it kept 23 paise of EBITDA on every rupee. That climb is real and the deck's own maths holds.

Two facts sit under the climb. Half of last year's sales went to data centres. Most of that went to a few hyperscale customers. The margin rose as those orders rose. The deck does not prove the margin will hold when that cycle cools.

The deck also says the business is spreading out. The numbers say the opposite. Maharashtra was 92 percent of sales last year, up from 55 percent three years ago. Export sales are flat and shrinking as a share. The story and the data disagree.

The deck shows profit. It shows no balance sheet and no cash. For a business that ships large project orders on 2 to 9 month terms, the cash question is the whole question. We cannot answer it from here.

This is a name to watch, not to buy. The next move is a spear pass on live web. Verify the cash first.

---

*Prepared by Claude Code from the filed deck only. No live web. No corpus beyond this document. One source; treat every figure as management assertion until an independent read confirms it.*
