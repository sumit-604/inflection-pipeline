# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Company: Akums Drugs & Pharmaceuticals Ltd (AKUMS) | Run date: 2026-07-10
Source: Integrated Annual Report FY2025-26 (AR PDF: `annual-report/40c769ef-bb37-46e6-a96d-e95b55734c3a.pdf`); extracted text with page markers used for anchoring; page numbers below are AR PDF page numbers, re-verified against the "===== PAGE N =====" markers for every citation in this pass.
Input consumed: `runs/akums-2026-07-10/outputs/reports/02-notes-pass1.md`

METHOD: Re-read the Notes to Financial Statements (Standalone Notes 1-56, Consolidated Notes 1-53) end to end a second time, cross-checking every line against the Pass 1 report. Where Pass 1 covered a note fully, it is not repeated. This pass surfaces (a) genuinely new items Pass 1 did not extract, (b) quantification/cross-note synthesis that materially escalates or refines a Pass 1 finding, and (c) two page-anchor corrections. Special attention paid, per instruction, to sub-notes/footnotes, cross-references between notes, unflagged YoY changes, "significant/material/unusual/exceptional/non-recurring/first time/changed" language, subsidiary/JV notes, and financial-instruments/fair-value-hierarchy/risk-management notes.

---

## NEW FINDINGS

### 1. Quality-of-earnings: reported PBT growth is largely a non-operating/treasury artefact (NEW — cross-note synthesis, not in Pass 1)

Pass 1 covered the tax-rate spike (its Finding #3) but did not connect Notes 26/27/30/33/46 to test what actually drove PBT growth. Doing so materially changes the read:

- **Segment note bridge** (Note 46, Consolidated, p.360-361): "Profit before exceptional items and tax" was **₹4,021.25M FY26 vs ₹3,285.56M FY25 (+22.4%, +₹735.69M)** — much stronger than the headline reported PBT growth of only **+10.7% (₹3,821.01M vs ₹3,452.53M, +₹368.48M)**. The gap is because FY26 carries a ₹200.24M exceptional *charge* while FY25 carried a ₹166.97M exceptional *income* (Note 33) — two years with offsetting one-offs, both already known individually to Pass 1 but their combined distorting effect on YoY PBT comparability was not quantified.
- **Other income** (Note 27, Consolidated, p.331) jumped **₹766.03M YoY (₹521.22M → ₹1,287.25M, +47%)**, driven almost entirely by "interest income on term deposits" **+₹833.34M (₹237.78M → ₹1,071.12M)** — i.e., treasury interest earned on IPO-proceeds cash sitting in bank deposits (cross-refers to Pass 1's Note 47 observation that net cash swung to -₹1,607.64 Cr due to IPO proceeds). This is non-operating income.
- **Finance costs** (Note 30, Consolidated, p.332) jumped **₹594.73M YoY (₹346.00M → ₹940.73M)**, but not from higher debt — real borrowing-cost lines actually *fell* (interest on borrowings ₹239.71M → ₹36.04M, -₹203.67M, consistent with the group's near-zero debt). The entire increase is explained by a brand-new line, **"Interest on contract liability" ₹776.06M FY26 vs nil FY25** (Note 30) — the imputed financing-component charge tied to the unnamed advance-from-customer deal (see Finding #2 below and Pass 1 Finding #2).
- **Net effect**: these two "other" line movements together contributed **≈₹171.30M** of net favourable swing to PBT (+766.03 other income, -594.73 finance costs), i.e. roughly **46% of the reported ₹368.48M PBT growth**, leaving only **≈₹197.18M (54%)** attributable to core operating (EBIT-level) improvement. Reported PBT growth therefore overstates organic operating momentum: a large share is treasury interest on cash that will taper as capex deploys it, netted against a new non-cash accounting construct tied to a single undisclosed customer arrangement.

🔴 Red Flag — new, high-importance finding not identified in Pass 1. Directly relevant to normalising FY26 earnings for valuation purposes.

### 2. Total contract-liability from the unnamed advance-from-customer deal is larger than Pass 1's headline number, and its current portion signals an imminent revenue-recognition catch-up (ESCALATES Pass 1 Finding #2)

Note 42(C) (Consolidated, p.348-349) shows the "Advance from customers" contract liability in *both* its non-current and current columns:

| | Non-current | Current | **Total** |
|---|---|---|---|
| FY26 | 8,408.06 | 1,915.01 | **10,323.07** (₹1,032.31 Cr) |
| FY25 | 0.00 | 230.96 | **230.96** (₹23.10 Cr) |

Pass 1 anchored only the ₹840.81 Cr non-current figure. The **true total balance-sheet exposure is ₹1,032.31 Cr, ≈23.7% of FY26 revenue** (₹4,359.02 Cr), and the **current portion alone grew +729% YoY** (₹23.10 Cr → ₹191.50 Cr), meaning a materially larger tranche of this liability is now due to convert to recognised revenue within the next 12 months than the balance-sheet mix implied a year ago. Counterparty and contract nature remain unnamed anywhere in the notes reviewed (Note 42(C), p.349: "long-term agreements entered by the group that includes a significant upfront consideration"). 🔴 Red Flag — escalation of Pass 1 #2, not a repeat.

### 3. Segment note corroborates the deal sits inside CDMO and quantifies the scale of the balance-sheet shift (NEW)

Note 46 (Consolidated, p.361), segment assets/liabilities table: **CDMO segment liabilities more than doubled, ₹7,280.97M → ₹18,177.11M (+149.6%) YoY**, while CDMO segment assets grew a much more modest +13.1% (₹27,016.32M → ₹30,544.04M). This is the segment-level fingerprint that locates Finding #2's ₹1,032.31 Cr advance-from-customer liability inside the CDMO segment specifically (consistent with Pass 1's inference, now quantified for the first time). The same table shows **un-allocated corporate assets jumped ₹7,990.29M → ₹18,716.42M (+134.2%)**, consistent with IPO cash sitting centrally rather than in any operating segment. 🟡 Watch — new corroborating quantification.

### 4. Note 49 "Intra group eliminations" contributed a large, unexplained swing to consolidated profit (NEW)

The Note 49 net-assets/profit-share table (Consolidated, p.364-365) has a line, "Intra group eliminations," that is not a subsidiary but a consolidation mechanic. It shows:

| | FY26 | FY25 |
|---|---|---|
| Net assets | (4,684.71) / -14.06% | (5,385.01) / -17.58% |
| Share in profit/(loss) | **+700.58 / +27.32%** | +53.90 / +1.57% |

The profit contribution from this eliminations line **jumped ~13x YoY (₹53.90M → ₹700.58M)** and is the **second-largest positive contributor to consolidated PAT after the parent's own 43.54% share** — larger than any single subsidiary's contribution (Pure & Cure 25.80%, Malik 11.08%, etc.). Nothing in the notes reviewed explains its composition (typical drivers would be unrealised-profit elimination on inter-company inventory/ICD interest/fair-value adjustments, but none is named here). 🟡 Watch — new quality-of-consolidated-earnings item; candidate for a management question given its size relative to total profit.

### 5. Note 49 quantifies the read-through of the Akumentis exceptional-item mismatch into consolidated profit, and corrects two Pass 1 page anchors

Note 49's per-entity table shows Akumentis Healthcare Limited's **share of consolidated profit collapsed from ₹602.19M (17.52% of consol PAT) FY25 to ₹129.99M (5.07%) FY26 — a ₹472.20M / -78.4% decline**. This is directionally and materially consistent with Akumentis's own standalone "Exceptional item" charge of ₹630.48M disclosed in Note 34B (Consolidated, p.336-337; NCI/subsidiary P&L: revenue ₹4,463.04M, PBT ₹406.44M after the ₹630.48M exceptional charge, tax ₹264.39M, profit ₹142.05M, of which ₹129.96M attributable to equity holders). **This confirms the item DOES flow into consolidated results (via equity pickup), even though it does not appear as a separate line in the Group's own Note 33 Exceptional Items** (total ₹200.24M) — resolving part of the ambiguity Pass 1 flagged in its Finding #4, though the note set still does not explain *why* the ₹630.48M Akumentis charge is excluded from the Group's own exceptional-items line rather than being added to it (the two treatments are inconsistent in presentation even if the profit effect is captured).

**Anchor correction**: Pass 1 cited this content as "Note 34A, Consolidated, pp.361-362" and "Note 34B, Consolidated, pp.362-363." Re-verified against the extracted page markers: **Note 34A (subsidiary ownership/entity list) is actually on p.335, and Note 34B (NCI summarised financials, incl. the ₹630.48M Akumentis exceptional item) is on p.336-337.** Note 49 (net assets/profit-share table) is correctly anchored at p.364-365 in Pass 1. 🟡 Watch + anchor correction.

### 6. Blanket asset pledge is far larger in scope than Pass 1's "inventory pledged" line, and includes IPO cash (NEW)

Pass 1 (Section 5, Inventory) noted only that "inventory pledged as security... ₹754.84 Cr." Note 40 (Consolidated, "Assets pledged as security," p.342-343) shows the true scope is much wider:

| | FY26 (₹M) | FY25 (₹M) |
|---|---|---|
| Inventories | 7,548.35 | 6,174.01 |
| Other current assets | 2,461.87 | 1,574.10 |
| Cash and cash equivalents | 2,045.65 | 457.65 |
| Other bank balances | 12,943.30 | 1,724.50 |
| Other financial assets | 442.28 | 441.34 |
| Trade receivables | 7,965.64 | 7,702.96 |
| PP&E | 8,121.80 | 9,825.07 |
| CWIP | 457.92 | 169.04 |
| **Total assets pledged** | **41,986.81 (₹4,198.68 Cr)** | 28,068.67 (₹2,806.87 Cr), **+49.6% YoY** |

This is pledged against a sanctioned working-capital/term-loan facility of only **₹5,910.00M (FY25: ₹12,092.00M)** of which just **₹1,183.06M was actually utilised** (Note 40.2) — pledged assets are **~7.1x the sanctioned facility and ~35.5x the drawn amount**. Notably, **₹1,494.90 Cr of cash and bank balances (including IPO-proceeds term deposits) is pledged** even though the Group is structurally net-cash. This is most likely standard blanket-hypothecation practice across a multi-entity working-capital banking arrangement rather than a genuine credit-quality red flag, but the scale (nearly the entire balance sheet, including surplus IPO cash, pledged against a shrinking, lightly-drawn facility) had no prior visibility in Pass 1 and is worth a direct question to management on collateral flexibility / whether release of the pledge on surplus cash is achievable. Ties to the "Financing arrangements (un-utilised)" table (Note, Consolidated, p.356): undrawn working-capital facility fell ₹9,277.19M → ₹4,726.94M and the undrawn term-loan facility of ₹1,362.00M (FY25) is now nil, i.e. banks/company right-sized total sanctioned lines materially post-IPO. 🟡 Watch — new.

### 7. Procurement fraud disclosure: statutory escalation and remediation detail not captured in Pass 1 (REFINES Pass 1 Finding #5)

Pass 1 flagged the ₹9.54M consolidated fraud (Note 52(c)) only as a qualitative control-environment red flag. Cross-reading the standalone note and the Board's Report reveals materially more context:

- **Standalone quantum is ₹4.49M** (Note 55(d), Standalone, p.281) vs **₹9.54M at consolidated level** — meaning roughly ₹5.05M of the fraud originates in subsidiary-books-only transactions, not captured in the parent's own books.
- The perpetrators are specified: **"employees of subsidiary companies"** operating fraudulently through the **Head Office** procurement function for IT assets/services, via "fictitious and inflated procurement transactions through certain vendor entities" (Note 55(d)).
- **Remediation already taken and disclosed**: disciplinary action against the individuals involved, blacklisting and blocking of the concerned vendors, an **insurance claim filed for recovery of the loss**, and strengthening of internal controls over IT procurement (Note 55(d)).
- **Statutory escalation**: this is not merely a notes-level disclosure — the Board's Report (p.76) confirms the Statutory Auditors formally reported this incident to the Audit Committee under the **second proviso to Section 143(12) of the Companies Act** (the formal fraud-reporting mechanism, which also triggers CARO clause (xi)(a) disclosure) — a materially more serious statutory characterisation than an internal note alone would suggest, even though the ₹4.49-9.54M quantum itself remains immaterial to Group scale.

🔴 Red Flag (qualitative) — refines and strengthens Pass 1 #5 with statutory-escalation and remediation context; does not change the immateriality of the rupee amount but changes the governance-severity read.

### 8. Tax search block-assessment: Company has already self-assessed and filed a "no undisclosed income" position (REFINES Pass 1 Finding #8)

Note 55(c) (Standalone, p.280) adds detail Pass 1 did not have: following the January 2025 Section 132 search (block period 1 April 2018 to 12 March 2025, per the standalone note — Pass 1 approximated this as "FY2018-19 to FY2024-25"), **the Company assessed that no undisclosed income is required to be reported and has already filed the requisite block-period returns during FY26** taking that position, ahead of the post-year-end show-cause notice Pass 1 flagged. This is a proactive, already-filed management position (not merely awaiting outcome), which somewhat tempers — without eliminating — the open-ended tail-risk characterisation in Pass 1's Finding #8. The SCN response has also already been submitted (Note 55(c)). 🟡 Watch, minor refinement, rating unchanged (risk remains unquantified and unresolved).

### 9. Investment property carries meaningful unrecognised value (NEW, minor, positive)

Note 3 (Standalone, "Investment property," p.236-237): net carrying value (cost model) ₹181.13M FY26 vs an independent registered valuer's fair value of **₹352.70M** — a **₹171.57M unrecognised gain**, categorised as Level 2 in the fair-value hierarchy. Rental income ₹19.36M FY26 (down from ₹21.36M FY25). Immaterial to overall balance sheet scale but a small hidden-asset-value item not previously noted. 🟢 Clean/minor positive, new.

### 10. Capital work-in-progress ageing shows a growing tail of multi-year buildings-in-progress (NEW, minor)

Note 2b (Consolidated CWIP, p.317-318) ageing schedule: buildings aged **2-3 years (₹256.65M) + >3 years (₹176.90M) = ₹433.55M, 57.8% of the ₹750.13M total buildings-in-CWIP balance**. The >3-year bucket alone grew **5.3x YoY** (₹33.24M → ₹176.90M). The note explicitly states "there are no such project... whose completion is overdue or has exceeded its cost compared to its original plan," so this is not flagged by management as a problem, and likely reflects long-gestation greenfield capacity expansion consistent with Pass 1's capex/inventory-build observations (Pass 1 Finding #7). Included here as new granularity supporting, not contradicting, that existing Watch item. 🟡 Watch, minor.

### 11. ECL reconciliation shows a materially higher write-off/reversal rate this year (NEW granularity, supports existing Pass 1 rating)

Note 43(c)(ii) (Consolidated, p.354-355), "Reconciliation of loss provision — Trade receivables": FY26 shows **₹293.01M gross provision created less ₹150.97M reversed/utilised** (net +₹142.04M) vs FY25's **₹291.77M created less only ₹21.85M reversed** (net +₹269.92M... reconciling to the 492.47 opening... note the FY25 closing of 492.47 vs FY26 closing 634.51 matches Pass 1's figures). The **reversal/utilisation rate rose from ~7.5% of FY25's created provision to ~51.5% in FY26** — i.e., materially more receivables were actually written off or recovered against the allowance this year, alongside the heavier new provisioning Pass 1 already flagged (Finding #6). This is corroborating detail; it does not change Pass 1's 🟡 Watch rating but adds the "how" behind the "what."

### 12. Minor inter-note tax figure inconsistency (NEW, flagged for Pass 3 pattern check)

Note 46's segment reconciliation (Consolidated, p.361) shows **"Tax expenses ₹1,257.04M"** for FY26, while Note 44(a) DTA reconciliation (as cited in Pass 1, p.423) shows total tax of **₹1,260.94M** for the same P&L line — a **₹3.90M variance between two notes purporting to reconcile to the same reported tax expense**. Immaterial in size (0.3% of the line) but a genuine note-to-note numerical inconsistency, flagged here for the Pass 3 "numbers that do not match between notes" pattern check rather than rated independently.

---

# PASS 2 NEW FINDINGS SUMMARY

1. **PBT growth quality**: ~46% of FY26's reported ₹368.48M PBT growth is a net artefact of treasury interest on IPO cash (+₹766.03M other income, mostly term-deposit interest) netted against a new non-cash imputed "interest on contract liability" (+₹594.73M finance costs) — core operating improvement is closer to ₹197.18M than the headline suggests; normalising for both years' offsetting exceptional items, underlying PBT growth was actually stronger (+22.4%) than the headline PBT growth (+10.7%). (Notes 26/27/30/33/44/46, Consolidated) — 🔴 new.
2. Total advance-from-customer contract liability (current + non-current) is **₹1,032.31 Cr (23.7% of revenue)**, not the ₹840.81 Cr Pass 1 cited; current portion alone +729% YoY. (Note 42(C), p.348-349) — 🔴 escalates Pass 1 #2.
3. CDMO segment liabilities +149.6% YoY (vs assets +13.1%) locates the deal in CDMO; un-allocated corporate assets +134.2% shows IPO cash sitting centrally. (Note 46, p.361) — 🟡 new.
4. Note 49 "Intra group eliminations" added ₹700.58M (27.3% of consol PAT) to profit, up ~13x from ₹53.90M FY25, with no explanatory note anywhere. (Note 49, p.364-365) — 🟡 new.
5. Akumentis's consolidated profit-share collapsed ₹602.19M → ₹129.99M (-78.4%), consistent with (and now quantifying) its ₹630.48M standalone exceptional charge flowing into consolidated results despite not appearing in the Group's own Note 33; two Pass 1 page-anchor errors corrected (34A → p.335, 34B → p.336-337, not pp.361-363). (Note 49 p.364-365; Note 34B p.336-337) — 🟡 refines Pass 1 #4 + anchor fix.
6. Total assets pledged as security is ₹4,198.68 Cr (+49.6% YoY), ~7.1x the sanctioned facility and ~35.5x the drawn amount, including ₹1,494.90 Cr of cash/bank balances (IPO cash) — far broader than Pass 1's inventory-only citation. (Note 40, p.342-343) — 🟡 new.
7. Procurement fraud was formally reported by auditors under Section 143(12) to the Audit Committee (Board's Report p.76); standalone quantum ₹4.49M vs consolidated ₹9.54M; remediation (disciplinary action, vendor blacklisting, insurance claim filed) now disclosed. (Note 55(d), Standalone, p.281) — 🔴 refines Pass 1 #5.
8. Company has already self-assessed and filed a "no undisclosed income" position for the Section 158BC block-assessment period, ahead of the post-year-end SCN. (Note 55(c), Standalone, p.280) — 🟡 refines Pass 1 #8.
9. Investment property carries a ₹171.57M unrecognised fair-value gain (Level 2). (Note 3, Standalone, p.236-237) — 🟢 new, minor.
10. Buildings-in-CWIP aged 2+ years now 57.8% of the buildings CWIP balance; >3yr bucket up 5.3x YoY, though no project is management-flagged as overdue/over-budget. (Note 2b, Consolidated, p.317-318) — 🟡 new, minor, supports Pass 1 #7.
11. ECL write-off/reversal rate rose sharply (~7.5% to ~51.5% of created provision), adding the "how" behind Pass 1's ECL Watch item. (Note 43(c)(ii), p.354-355) — supports Pass 1 #6, no rating change.
12. ₹3.90M inconsistency between Note 46 and Note 44(a) tax-expense figures — immaterial, flagged for Pass 3 cross-note pattern check.

END OF PASS 2.
