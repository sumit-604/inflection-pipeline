# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)

**Company:** Aequs Limited (AEQUS) | **Run date:** 2026-09-05 | **AR:** FY2025-26 (year ended 31-Mar-2026)
**Basis:** All ₹ amounts in the AR notes are in INR MILLIONS. This report converts to **₹ Crores** (Mn ÷ 10), original Mn kept alongside where useful for cross-checking. Page numbers are the PDF page from the `=== PAGE n of 361 ===` markers.

**Method.** Re-read Consolidated Notes 1–41 (PDF pp.233–302) and Standalone Notes 1–36 (PDF pp.149–216) a second time, this time reading every sub-note, footnote, cross-reference and adjoining risk-management/fair-value/related-party table in full (several of which Pass 1 summarised at headline level only), plus the two Independent Auditor's Reports and their CARO Annexure A (Standalone PDF pp.149–159, Consolidated PDF pp.219–226), which Note 40 in the Notes proper does NOT actually cross-reference (see correction below). Only genuinely new findings are reported below; items Pass 1 already covered fully are not repeated.

Pass 1 specifically flagged four items for this pass: (i) the FX-exposure-by-currency table at Note 28(C) — now transcribed in full below; (ii) the Note 15(C) vs Note 29 net-debt inconsistency — now diagnosed more precisely below; (iii) the new non-current contract asset of ₹11.14 Cr (Note 12) — re-checked, no further disclosure exists beyond the balance-sheet line itself, remains NOT FOUND IN DOCUMENT for its nature; (iv) the CARO/audit-trail cross-reference at "Note 40(vi)" — this citation was wrong; corrected below.

---

## CORRECTION TO A PASS 1 ANCHOR

Pass 1 stated the audit-trail (edit-log) gap and CARO adverse remarks were "cross-referenced at Note 40(vi)" in the Notes to Financial Statements. On a full re-read, **Note 40(vi) of the Notes proper is the boilerplate "no funds advanced to intermediaries / no funds received from funding parties" disclosure** (Consol. Note 40(vi)(a)-(b), PDF p.301) — it has nothing to do with the audit trail. The audit-trail language and the CARO clause table sit **only** in the Independent Auditor's Reports themselves, not in a Notes cross-reference:
- Audit trail (Rule 11(g)): Standalone Auditor's Report PDF p.153; Consolidated Auditor's Report PDF p.223.
- The auditors' Section 143(3)(b) opinion on "proper books of account" is **explicitly qualified "except for"** the Rule 11(g) audit-trail matter, in both reports (Standalone PDF p.152, para 2A(b); Consolidated PDF p.222, same para) — this is a formal exception in the statutory audit opinion, not merely disclosure boilerplate as Pass 1's phrasing implied. 🔴 Red Flag (elevated from Pass 1's 🟡 framing).
- CARO Annexure A clause (xxi) (Consolidated, PDF p.222) lists adverse/unfavourable CARO remarks by **entity and specific clause number** — see new finding below; Pass 1 only had this as one aggregate sentence.

---

## NEW FINDINGS BY NOTE

### Note 15(B) — Quarterly stock-statement vs. books reconciliation (Consol., PDF p.267)

Pass 1 cited only the year-end Axis Bank gap ("up to ₹59.0 Cr"). The full quarterly table shows the gap is not a snapshot — it **widens every single quarter of FY26** with Axis Bank:

| Quarter | Trade receivables: books − reported (₹ Cr) | Trade payables: books − reported (₹ Cr) |
|---|---|---|
| Jun-25 | +29.95 | +13.71 |
| Sep-25 | +36.21 | +22.13 |
| Dec-25 | +54.71 | +34.27 |
| Mar-26 | +59.01 | +32.30 |

Reason given (footnote b): "Inter-company balances and receivables more than 120 days are not included in the stock statement." The monotonic widening means the pool of aged/intercompany receivables excluded from the bank's collateral base is **itself growing every quarter**, not a one-off timing gap. This independently corroborates Pass 1's Finding 5 (DSO 62→78.5 days, ECL coverage 1.91%→0.73%) from a completely different note (a lender-reporting note, not the ageing/ECL note) — two unrelated disclosures point at the same underlying deterioration. 🔴 Red Flag (upgraded from Pass 1's 🟡 Watch on this specific note).

### Note 15(C) / Note 27 / Note 28(C)(ii) / Note 29 — the net-debt reconciliation problem is not isolated to one pair of notes

Sharper diagnosis of Pass 1's Finding 8: the same formula — (lease liabilities + NCDs + non-current borrowings + current borrowings) minus (cash and cash equivalents + other bank balances) — reproduces **both** Note 15(C)'s and Note 29's FY25 net-debt figure (₹705.26 Cr) exactly, but only Note 15(C)'s FY26 figure (₹344.28 Cr), not Note 29's (₹250.05 Cr). This proves the FY26 gap is an isolated computational error in Note 29, not a differently-defined "net debt" applied consistently — it disappears completely at FY25 under the identical formula.

A **second, independent** unreconciled total-debt figure exists in the same Note 28: the interest-rate-risk sub-note (Note 28(C)(ii), PDF p.282) states "Total borrowings" of ₹657.58 Cr (6,575.75 Mn) FY26 and ₹785.05 Cr (7,850.47 Mn) FY25. The FY25 figure ties exactly to Note 27's borrowings (₹437.06 Cr) plus Note 5's lease liabilities (₹347.99 Cr) = ₹785.05 Cr. The FY26 figure does **not** tie to the equivalent sum (₹403.58 Cr + ₹297.35 Cr = ₹700.93 Cr; gap ₹43.35 Cr). Three separate sub-notes inside Note 28/29 now show an unreconciled FY26 debt aggregate while FY25 reconciles cleanly across all of them — a recurring FY26-specific pattern across the financial-risk-management notes, not a single typo. 🟡 Watch, flagged for verification alongside Pass 1's Finding 8; carry forward to Pass 3 pattern check.

### Note 28(C)(i) — Foreign currency exposure table (now transcribed; flagged pending in Pass 1)

FY26 net exposure by currency (Financial assets less financial liabilities, ₹ Cr):
- **USD**: assets 274.00, liabilities 150.84 → **net long ~123.16 Cr** (receivables-heavy).
- **EUR**: assets 3.72, liabilities 53.86 → **net short ~50.14 Cr**, driven almost entirely by EUR lease liabilities (48.78 Cr) — this is the France operation's lease book, largely unhedged.
- GBP, HKD, CHF: small net short positions (≤1.1 Cr each); JPY nil FY26.

Sensitivity table: a 5% INR move against USD swings P&L by **±4.365 Cr** FY26 (up from ±2.331 Cr FY25 — the USD sensitivity **nearly doubled** YoY as USD receivables grew), while the same move against EUR swings P&L by **∓1.777 Cr** FY26 (down from ∓2.967 Cr FY25). Because the net USD position is long and the net EUR position is short, INR depreciation is a P&L tailwind on the USD leg and a headwind on the EUR leg simultaneously — the two do not offset since they are different currency pairs. Currency-driven earnings volatility is increasingly USD-sized and growing, worth flagging for stage 11's FX sensitivity work. 🟡 Watch.

### Note 19 (Other income) and Note 24 (Finance costs) — a material non-operating FX swing Pass 1 did not surface

- **Note 19, Other income (Consol., PDF p.275)**: "Exchange difference (other than on borrowings)" = **₹42.63 Cr FY26 vs ₹5.23 Cr FY25 (+715%)** — roughly **65% of total other income** (₹65.38 Cr) FY26 came from this one line.
- **Note 24, Finance costs (Consol., PDF p.276)**: "Exchange differences (on borrowings)" = **₹19.66 Cr FY26 vs ₹5.74 Cr FY25** — an FX **loss** sitting inside finance costs, opposite sign to the Note 19 gain.
- Net FX effect across the two lines: **+₹22.97 Cr to FY26 P&L**, split across two different line items that an analyst summing "operating" lines could easily miss netting together. This is a real, non-recurring cushion to the reported consolidated loss (-₹113.25 Cr) — without it, the loss trajectory looks meaningfully worse YoY. 🟡 Watch (earnings-quality item).
- Separately, total finance costs rose 56.8% YoY (₹92.35 Cr from ₹58.90 Cr) despite net debt roughly halving on IPO proceeds — explained by the IPO landing only in Dec-2025 (an 8-month stub of pre-IPO leverage), new high-cost NBFC/NCD financing added mid-year, and the FX loss above. Also, reported finance costs are **net of ₹15.92 Cr of capitalised interest** (Note 4A, capitalisation-of-expenditure table) — true gross finance cost incurred in FY26 was **≈₹108.27 Cr**, not the ₹92.35 Cr headline figure.

### Note 36 — Segment note: full PBT-level bridge (Pass 1 stopped at EBITDA)

| | Aerospace FY26 | Aerospace FY25 | Consumer FY26 | Consumer FY25 |
|---|---|---|---|---|
| Finance costs (₹ Cr) | 58.25 | 38.78 (+50.2%) | **55.06** | 23.87 (**+130.7%**) |
| Segment PBT (₹ Cr) | **173.98** | 71.17 (**+144.5%**) | **(217.92)** | (145.85) (**+49.4%**) |

Consumer segment finance costs (₹55.06 Cr) are now **almost as large as Aerospace's** (₹58.25 Cr) despite Consumer generating only 17.6% of segment external revenue (₹184.06 Cr of ₹1,046.38+184.06 Cr) — a disproportionate debt-service burden landing on the loss-making segment, consistent with the high-cost NBFC financing (Oxyzo/Vivriti) Pass 1 flagged at Note 15(A), now quantified at the P&L level. The Consumer segment's **full pretax loss** (-₹217.92 Cr, +49.4% YoY) is materially worse than the EBITDA-level view alone (-₹78.27 Cr, Pass 1 Finding 2) once depreciation, finance costs, exceptional items and JV losses are added — Consumer segment lost roughly **119% of its own revenue** before tax in FY26. Conversely Aerospace segment PBT **more than doubled** (+144.5%), stronger confirmation of the transition thesis than the EBITDA view alone. 🔴 Red Flag (Consumer) / 🟢 Clean (Aerospace), both new quantifications.

Also new: "Unallocated corporate expense net of unallocated income" (costs sitting outside both segments) rose to **₹24.24 Cr FY26 from ₹12.98 Cr FY25 (+86.9%)** — plausibly reflects new listed-company overhead (two new independent directors appointed in FY26, board/compliance costs) not attributable to either segment. Minor, but a real new post-listing cost layer.

### Note 37 — Interest in other entities (subsidiary/JV detail Pass 1 summarised only partially)

**Subsidiary table (PDF pp.293–294)**: of 19 listed group entities, **seven are liquidated, struck off, inactive or formally "discontinued"**: Aequs Home Appliances Pvt Ltd (liquidated Jun-2025), Aequs Material Management Pvt Ltd (liquidated Jun-2024), Koppal Toys Tooling COE Pvt Ltd (liquidated Nov-2024), Aequs Force Technology Co Ltd, Hong Kong (liquidated Aug-2024), Aequs Rajas Extrusion Pvt Ltd ("inactive company"), Aequs Oil & Gas LLC and Aequs Toys Hong Kong Pvt Ltd (both "discontinued operations", Note 39 confirms both are "in the process of liquidating"). This is concentrated in Consumer/US/Hong Kong entities and confirms, at the **legal-entity level** (not just the standalone investment-impairment level Pass 1 already flagged at Finding 6), that the earlier toys/oil-and-gas international expansion is being wound down, not merely written down on paper. 🟡 Watch.

**JV summarised P&L (Note 37(c)/(iii), PDF pp.296–297)**: SQuAD JV profit **nearly tripled** to ₹28.89 Cr FY26 from ₹10.39 Cr FY25 (+178%) — this is real operating improvement, corroborating (not just asserting) the "improved performance" management cited when reversing the ₹23.44 Cr SQuAD impairment (Pass 1, Section 6). ACPL JV (holding the transferred Consumer Durables business) shows finance cost of ₹8.25 Cr against revenue of only ₹39.69 Cr (~20.8% of revenue) — the high-cost-debt pattern flagged for Consumer subsidiaries reaches into the JV structure too. New JV Ajna Aerospace & Defence posted a loss of ₹0.99 Cr in its first (under one month) stub period since inception (6-Mar-2026) — too small to matter financially but a data point worth tracking.

**Note 39 Discontinued operations (PDF p.299–300)**: confirms formally that AOGLLC and ATHPL are "in the process of liquidating" both years — sizes are immaterial (~₹0.01–0.08 Cr) but this is the formal Ind AS 105 classification Pass 1 did not separately extract.

### Note 34 — Related Party Disclosures: fuller transaction table changes the RPT-as-%-of-revenue conclusion

Pass 1 estimated aggregate RPT expense flows at "low single-digit %" of revenue using three line items. The full transaction table (PDF pp.286–287) adds several large flows Pass 1 did not tally: API (JV) services received ₹44.13 Cr FY26 (+36.4% YoY, from ₹32.36 Cr), ASEZ services received ₹32.84 Cr, HDGCPL services received ₹17.67 Cr, SQuAD (JV) purchase of goods and consumables **₹16.29 Cr FY26 vs ₹4.25 Cr FY25 (+283%)**, QGEPL services received ₹2.76 Cr, MFRE Taris LLC services received ₹1.54 Cr (new counterparty). Summing these purchase/service-received flows gives **≈₹115 Cr, or ~9.4% of consolidated revenue (₹1,230.44 Cr)** — materially higher than Pass 1's "not material in aggregate" read. The Group's operating dependency on related-party suppliers (chiefly its own JVs and promoter-linked landlord/service entities) is more significant than first assessed. 🟡 Watch (upgrades Pass 1's conclusion on this specific point).

Also new: **Aequs Foundation** is added as a related party (associate) with effect from **27-Mar-2026** — four days before year-end, an unusually late-in-year addition (small, ₹0.01 Cr investment, but worth noting for completeness). Technical point: **AMIPL and Aequs Inc, Cayman Islands formally ceased to be "holding company"/"ultimate holding company" from 10-Dec-2025** (IPO date) for Ind AS classification purposes, yet the 13% p.a. related-party loan from AMIPL and the flat ₹1 Cr/yr branding fee continue at unchanged commercial terms post-IPO, with AMIPL still the largest single shareholder per company memory (43.35%). Also, within the KMP remuneration table, **Co-founder & Managing Director Rajeev Kaul's pay declined slightly** (₹1.797 Cr FY26 from ₹1.836 Cr FY25, −2.1%) in the same year Executive Chairman Melligeri's rose +111% — a notable divergence between the company's two named founders' pay trajectories, worth a management question alongside Pass 1's Finding 7.

### Note 35 — Income tax: a second large reconciling item, and a compositional shift in unrecognised losses

Pass 1's Finding highlighted the "no DTA recognised" reconciling item (₹44.39 Cr FY26). The full reconciliation table (PDF pp.289–290) shows a **second, comparably large positive reconciling item**: "Tax impact due to differential tax rates applicable to subsidiaries" = **₹21.56 Cr FY26 vs ₹12.12 Cr FY25 (+78%)**. Together these two items (₹65.95 Cr combined) are the dominant reasons the Group posts a tax **charge** of ₹41.76 Cr on a **pre-tax loss** of ₹71.54 Cr, rather than a tax benefit — both point at the same structural issue (loss-making entities and higher-tax jurisdictions can't be pooled for group tax relief), now with the differential-rate driver quantified for the first time.

Also new: the tax-loss-carryforward table shows a **compositional shift**, not pure growth. The "expiring" bucket actually **fell** to ₹158.57 Cr FY26 from ₹304.12 Cr FY25, while the "never expire" bucket **more than doubled** to ₹542.65 Cr (Pass 1 already had this figure). Total unrecognised losses still grew overall (+25.5%, ₹701.22 Cr from ₹558.66 Cr), but the mix is shifting hard toward permanently-unrecognised losses — a nuance that changes the read from "losses growing" to "losses growing AND becoming structurally harder to ever monetise." 🟡 Watch.

### Note 4A — Capitalisation of expenditure (capex quality detail, not just the CWIP→PP&E transfer amount)

Costs capitalised into CWIP **fell** to ₹89.85 Cr FY26 from ₹105.88 Cr FY25 (−15.1%) even as a record ₹412.19 Cr moved from CWIP to PP&E (Pass 1 Finding 10) — consistent with Pass 1's read that the big capacity build is largely behind the company. Within this falling total, "cost of materials consumed" capitalised **jumped to ₹35.86 Cr from ₹7.45 Cr (+381%)** while capitalised employee cost and finance cost both fell — the tail end of the build looks materials/equipment-heavy (late-stage fit-out) rather than labour/interest-heavy (early-stage construction), a texture Pass 1 did not have. Minor, but useful for stage 11's capex-normalisation work.

### Note 38 — Additional Schedule III consolidation disclosure (entity-level net-asset and P&L contribution table; not reviewed at all in Pass 1)

This table (PDF pp.297–299) shows each consolidated entity's % share of consolidated net assets and consolidated profit/loss. Two points stand out:
- The **Parent standalone entity's own net assets (₹1,844.26 Cr) equal 124.00% of the consolidated total (₹1,487.36 Cr, pre-elimination sub-total)** — implying the subsidiaries are, in aggregate, net-negative before consolidation eliminations (a large negative "effect of intercompany and consolidation adjustments" of −₹1,654.39 Cr closes the gap). This is consistent with, but a sharper way of stating, Pass 1's standalone-impairment finding (Finding 6).
- **ACPPL (Consumer) alone contributed a loss of ₹145.75 Cr to the consolidated profit/loss line, equal to 130.75% of the whole Group's consolidated attributable loss (₹111.48 Cr)** — i.e., this single Consumer entity lost more than the entire Group lost on a net basis, with profits elsewhere in the structure (chiefly the Parent and the Aerospace subsidiaries) offsetting the rest. This is the clearest single-entity quantification yet of where the consolidated loss concentrates. 🔴 Red Flag.

### Note 33 (Consol.) — Business combination detail: a small nuance on the lease-liability trend

The full asset/liability transfer table (ACPPL → ACPL, effective 1-Oct-2024, PDF p.284) shows ₹18.32 Cr of right-of-use assets and ₹18.32 Cr of lease liabilities were deconsolidated along with the Consumer Durable Goods business unit. This means part of the FY25 base-year lease-liability level already reflects a deconsolidation, not repayment — a minor but real nuance for anyone modelling the FY25→FY26 lease-liability decline (₹347.99 Cr → ₹297.35 Cr, Pass 1 Section 1) as pure debt paydown.

### Standalone Note 33 — Financial ratios: full table (Pass 1 extracted only the ROCE line)

| Ratio | FY26 | FY25 | Variance | Company's stated reason |
|---|---|---|---|---|
| Current ratio (x) | 2.85 | 1.97 | +44.7% | IPO funds received |
| Debt-equity ratio (x) | 0.02 | 0.06 | −66.7% | Equity up, debt down |
| Debt service coverage (x) | 2.06 | 0.76 | +171.1% | PBT up, debt service down |
| Return on equity (%) | 3.59% | −7.84% | +145.7% | PAT up |
| Inventory turnover (x) | 1.33 | 1.05 | +26.7% | COGS up |
| Trade receivables turnover (x) | 5.90 | 6.38 | −7.5% | (below 25% threshold, no reason required) |
| Trade payables turnover (x) | 4.19 | 4.01 | +4.5% | (below threshold) |
| Net capital turnover (x) | 0.88 | 1.34 | −34.3% | Working capital up faster than revenue |
| **Net profit ratio (%)** | **40.21%** | **−80.31%** | +150.1% | PAT up |
| ROCE (%) | 3.41% | −6.81% | +150.1% | EBIT up |
| Return on investment (%) | 36.08% | 1.38% | **+2,519.4%** | Investment income up, average investment down |

Two of these numbers need context Pass 1 did not have:
- **A 40.21% standalone "net profit ratio" is not an operating margin and should not be read as one.** Back-solving from standalone PAT (₹49.80 Cr, per the EPS note) and this ratio implies standalone "Sales (revenue from operations)" of only **≈₹123.85 Cr** — a small fraction of the Group's ₹1,230 Cr consolidated revenue, because the Parent entity's own invoiced sales are a fraction of what its subsidiaries generate. The 40.21% margin is therefore dominated by non-operating income (investment income, guarantee fees, interest from subsidiaries), not manufacturing profitability, and would materially mislead any screen that reads it as a comparable operating margin. 🟡 Watch — a disclosure-interpretation risk, not an accounting-quality defect per se.
- **Return on investment of 36.08% (from 1.38%, +2,519% variance)** is explained only as "increase in income from investment while there is decrease in average total investment" — almost certainly connected to the same-year AABV loan-to-equity conversion and simultaneous impairment reversal Pass 1 flagged at Finding 6 (Note 6(iv), Standalone p.180), which would mechanically depress the average-investment denominator and could inflate the numerator. Likely a one-off, not sustainable investment-income growth. 🟡 Watch.
- **Trade receivables turnover at the standalone level deteriorated only mildly** (5.90 vs 6.38, DSO roughly 57→62 days) compared with the much sharper consolidated deterioration Pass 1 flagged (62→78.5 days, Finding 5). This indicates the receivables buildup is concentrated in the **subsidiaries** (most plausibly the direct-export Aerospace units billing end customers), not the Parent — useful context for FLAG-CASH scoping.

---

## PASS 2 NEW FINDINGS SUMMARY

1. **CARO Annexure A (Consolidated, PDF p.222)** lists entity-and-clause-specific adverse remarks not captured in Pass 1's one-line summary: Parent + ASMIPL — clause ii(b) (quarterly stock statements do not agree with books, corroborating the Note 15(B) finding above) and clauses iii(c)–iii(f) (irregular terms/repayment on loans and advances given, i.e. the intercompany lending Pass 1 flagged at Finding 6); ACPPL, AEPPL, AFCPPL — clause xvii, **auditor-confirmed CASH losses** (not just book losses); AFCPPL and Aequs Toys — clause ii(a), physical inventory count discrepancies not properly dealt with; AFCPPL — clause ix(d), short-term funds used for long-term purposes; new JV Ajna — clauses vii(a) (irregular statutory dues) and xiv (inadequate internal audit). Three JVs (SQuAD, API, ACPL) and the new associate (Aequs Foundation) had **no CARO report issued** by their auditors as of the principal auditor's sign-off date (26-May-2026) — an open compliance gap. Both auditor's reports (Standalone p.152, Consolidated p.222) formally qualify the "proper books of account" opinion "except for" the Rule 11(g) audit-trail matter — a stronger characterisation than Pass 1's framing. 🔴 Red Flag.
2. **Note 15(B) stock-statement gap widens every quarter of FY26 with Axis Bank** (receivables gap ₹29.95 Cr Jun-25 → ₹59.01 Cr Mar-26), not a single snapshot as Pass 1's framing suggested — independently corroborates the receivables/DSO deterioration from a lender-reporting angle. 🔴 Red Flag.
3. **Consumer segment's full pretax loss is ₹217.92 Cr FY26 (+49.4% YoY)**, not the ₹78.27 Cr EBITDA-level loss Pass 1 cited — Consumer segment finance costs alone (₹55.06 Cr, +130.7% YoY) are now nearly as large as Aerospace's (₹58.25 Cr) despite generating a sixth of the revenue. Aerospace segment PBT more than doubled to ₹173.98 Cr. 🔴 Red Flag (Consumer) / 🟢 Clean (Aerospace).
4. **A material, largely non-operating net FX gain of ~₹22.97 Cr cushioned FY26 earnings**, split across Other Income (+₹42.63 Cr FX gain) and Finance Costs (−₹19.66 Cr FX loss) — an earnings-quality item Pass 1 did not surface.
5. **A second unreconciled "total borrowings" figure (₹657.58 Cr FY26) inside Note 28's interest-rate-risk table** does not tie to Note 27/Note 15's figures, while the identical FY25 figures tie exactly — the net-debt reconciliation problem (Pass 1 Finding 8) recurs across three sub-notes within Note 28/29, not one isolated pair.
6. **Full FX-exposure table transcribed**: net EUR short position (~₹50 Cr, mostly France lease liabilities) against a net USD long position (~₹123 Cr); USD sensitivity to a 5% INR move nearly doubled YoY (±₹2.33 Cr → ±₹4.37 Cr).
7. **Seven of nineteen consolidated entities are liquidated, struck off, inactive or discontinued** (Note 37), confirming the Consumer/international wind-down at the legal-entity level, not just via the standalone investment write-downs Pass 1 already flagged.
8. **RPT purchase/service flows total ~₹115 Cr (~9.4% of consolidated revenue)** once the full Note 34 transaction table is tallied (API, ASEZ, HDGCPL, SQuAD, QGEPL, MFRE Taris), materially higher than Pass 1's "not material in aggregate" read; SQuAD purchases from the Group +283% YoY.
9. **ACPPL alone contributed a loss equal to 130.75% of the Group's entire consolidated attributable loss** (Note 38) — the sharpest single-entity quantification of loss concentration found in the Notes.
10. **Standalone "net profit ratio" of 40.21%" is a holding-company artefact, not an operating margin** — standalone revenue from operations is only ≈₹123.85 Cr; the ROI ratio's 2,519% jump likely reflects the one-off AABV loan-to-equity/impairment wash already flagged at Pass 1 Finding 6.
11. Second tax reconciling item found: **differential tax rates across subsidiaries added ₹21.56 Cr to tax expense (+78% YoY)**, alongside the ₹44.39 Cr "no DTA recognised" item Pass 1 already had; tax-loss composition is shifting toward permanently-unrecognised losses, not just growing.
12. Minor items: Co-founder/MD Rajeev Kaul's pay fell 2.1% while the Executive Chairman's rose 111%; unallocated corporate costs rose 86.9% to ₹24.24 Cr (post-listing overhead); capitalised-cost mix within CWIP shifted toward materials (+381%) as employee/finance-cost capitalisation fell; reported finance costs are net of ₹15.92 Cr capitalised interest (true gross ≈₹108.27 Cr); new associate Aequs Foundation added four days before year-end; ₹18.32 Cr of ROU assets/lease liabilities were deconsolidated with the Consumer Durables transfer, partly explaining the base-year lease-liability decline.
