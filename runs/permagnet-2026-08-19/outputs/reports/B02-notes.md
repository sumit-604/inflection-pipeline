# B02 — Notes to Financial Statements, PASS 3 (Pattern Pass + Consolidation)
Company: PERMAGNET (Permanent Magnets Limited) | Run date: 2026-08-19
Source: runs/permagnet-2026-08-19/work/txt/AR-FY26.txt (FY2025-26 Annual Report)
Basis: Consolidates Pass 1 (full extraction, Notes 1-35 standalone / 1-36 consolidated) and Pass 2
(what-was-missed re-read, plus primary-statement tie-outs and CARO cross-references), then adds a
targeted Pass 3 pattern re-read for contradictions, tie-out failures, deliberately vague disclosures,
restatements, subsequent events, and going-concern language.

---

## PASS 3 PATTERN RE-READ

Targeted checks performed beyond Passes 1-2:
- Searched the full document for "restat", "reclassif", "regroup", "prior period error" (all
  occurrences reviewed). Result: standard boilerplate only — "The previous year's figures have been
  regrouped, rearranged and reclassified wherever necessary to conform to the current year's
  presentation" (Note 20, standalone, p.111-112; equivalent Note 19, consolidated, ~p.155). No specific
  line items, no amounts quantified for what was reclassified — the note is generic year-on-year
  boilerplate, not a disclosed restatement. The Statement of Changes in Equity "Restated balance at the
  beginning of the reporting period" rows (standalone p.85-86, consolidated p.131-132) are template
  headers that carry Nil in the "Changes in accounting policy or prior period errors" column both years
  — confirms no actual restatement occurred. 🟢 Clean — no hidden restatement found.
- Re-checked all standalone-vs-consolidated figure pairs already flagged (PAT, ROE, current ratio,
  ROCE, gratuity discount rate, Cast Magnets revenue, capital advances, CWIP) for arithmetic
  consistency against the primary statements — all reconcile to the figures already reported in Passes
  1-2; no additional contradictions found beyond what is already catalogued.
- Confirmed the Board approved the financial statements on May 13, 2026 (Note 21, standalone, p.112) —
  no subsequent event beyond the already-flagged proposed dividend (₹2.20/share) is disclosed.
- Re-read the auditor's going-concern Emphasis of Matter and Note 3 (winding-up order) once more
  specifically for hedging or qualifying language: the EOM paragraph is unqualified in form (an
  Emphasis of Matter, not a qualification), but the explicit sentence-level linkage of "prepared on a
  Going Concern Basis on reasons mentioned in note no. 3" to a decade-old unresolved winding-up
  petition is unusual phrasing, as already flagged in Pass 1 — no material new angle found on a third
  read.

No further material new findings beyond Passes 1 and 2 emerged from this pattern-focused re-read; the
prior two passes had already surfaced the principal contradictions (ROU depreciation method, actuarial
discount rate, share face value, "capital employed" definitions, Cash Flow PBT tie-out) through their
own note-by-note and cross-reference methods. Proceeding to consolidation.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Subsidiary's Cast Magnets revenue collapsed ≈85.5% YoY (≈₹5.37 Cr → ≈₹0.78 Cr, isolated by subtracting standalone from consolidated Note 25/26 revenue disaggregation) in the same year the subsidiary drew a ₹47.81 Cr unsecured ECB and built ≈₹15.5 Cr of capex-in-progress | Note 25 standalone p.90 vs Note 26 consolidated p.128 | 🔴 Red Flag | The subsidiary's own top line evaporated while its balance sheet expanded on borrowed money — the single most consequential fact in the notes for group risk |
| 2 | Standalone PAT +36.5% (₹20.69 Cr) vs Consolidated PAT -4.3% (₹15.07 Cr); standalone ROE 13.31% (up) vs consolidated ROE 9.57% (down); standalone Net Profit Ratio 9.18% (up) vs consolidated 6.53% (down) | Note 15/EPS/Ratios, standalone p.85-86, p.112; consolidated p.131-132, p.156 | 🔴 Red Flag | The listed entity's standalone highlights show a strengthening business while the group investors actually own shows deteriorating profitability, driven entirely by the subsidiary |
| 3 | New ₹47.81 Cr unsecured ECB at the subsidiary (5% simple interest, ≈$5m principal, 20 half-yearly instalments from 15/07/2029) drives consolidated debt-equity from 0.17x to 0.56x (+238.04%); invisible in standalone accounts | Note 16 consolidated p.131-132; Ratios Note 20 consolidated p.156 | 🔴 Red Flag | Largest single capital-structure change in the year, carrying unhedged-appearing currency/rate exposure not quantified anywhere |
| 4 | Cash Flow Statement "PBT" fails to tie to P&L "PBT" by exactly the OCI remeasurement amount (₹0.30 Cr), identically at both standalone (28.00 vs 27.70) and consolidated (22.69 vs 22.39) level | P&L p.77/p.121 vs Cash Flow p.78/p.122 | 🔴 Red Flag | A repeatable, non-rounding mechanical error in how the indirect-method Cash Flow Statement was assembled at both reporting levels — a preparation-integrity signal the Notes alone would not reveal |
| 5 | Mandatory Ind AS/Schedule III consolidated "Additional Information" table (net assets and profit/loss share attributable to parent vs. subsidiary, as % of consolidated totals) is absent from the notes | Searched Notes 1-36 consolidated, not found | 🔴 Red Flag | Standard disclosure requirement; its absence prevents investors from independently verifying the subsidiary's contribution without reconstructing it indirectly (as this analysis had to do) |
| 6 | New, unsupported "Capital Work-in-Progress" balance sheet line (₹3.37 Cr standalone, ₹8.08 Cr consolidated, FY25: Nil) carries no CWIP ageing schedule anywhere in the document | Balance Sheets p.76/p.120; searched Notes 1-35 standalone, 1-36 consolidated, not found | 🔴 Red Flag | Schedule III mandates a CWIP ageing schedule whenever CWIP is non-zero and material (5.1% of consolidated total assets); complete absence |
| 7 | Consolidated Capital Advances rose ₹1.05 Cr → ₹15.81 Cr (+1405.7%); standalone rose only to ₹4.98 Cr, implying ≈₹10.83 Cr sits at the subsidiary alone | Note 7 consolidated p.126 | 🔴 Red Flag | Combined with CWIP (row 6), ≈₹15.5 Cr of the new ECB proceeds sit as advances/work-in-progress, not yet converted into revenue-generating capacity |
| 8 | Auditor's Emphasis of Matter ties the Going Concern basis of preparation explicitly to Note 3, which describes a 2015 Bombay High Court winding-up order (₹0.13 Cr petition) under interim stay since 2015, still unresolved | Auditor's EOM standalone p.66, consolidated p.113; Note 3 standalone p.104, consolidated p.148 | 🔴 Red Flag | Unusual phrasing for an audit report; a decade-unresolved winding-up order explicitly linked to the going-concern basis warrants direct query despite the small claim amount |
| 9 | ₹22.01 Cr disputed Central Excise interest contingency ≈13-14% of net worth, unresolved since a 2013 Ministry of Finance settlement approach on a 1995-96 loan; CARO Annexure adds that it is 12% simple interest, defaulted October 2002-November 2017, with a ₹0.01 Cr discrepancy between the auditor's figure (₹1.75 Cr) and the company's Note figure (₹1.76 Cr) | Note 2(f) standalone p.103-104, consolidated p.147-148; CARO Annexure A ix(a) standalone p.72 | 🔴 Red Flag | Single largest contingent-liability item, long-dated and un-resolving, exceeding the 10% of net worth materiality threshold |
| 10 | Actuarial discount rate for gratuity/leave valuation differs between standalone (7.25%, FY26) and consolidated (6.75%, FY26) for the identical 31.03.2026 balance sheet date | Note 9A standalone p.106, consolidated p.150 | 🔴 Red Flag | Should not occur for the same economic assumption (government bond yields) unless the subsidiary uses a different actuary/basis — needs management clarification |
| 11 | No geography-wise revenue disclosure despite exports ≈47% of revenue (₹106.05-106.82 Cr FOB) across India, Europe, USA, South America, South-East Asia | Note 25/26 vs Note 14D/13D, standalone p.90, p.108; consolidated p.128, p.152 | 🔴 Red Flag | Ind AS 108 para 33 entity-wide disclosure gap; near-majority export exposure with no geographic breakdown limits risk assessment |
| 12 | Trade receivables +39.4% vs revenue +13.0%; receivable days +5.3% (standalone, 76.03 vs 72.19) to +7.9% (consolidated, 75.77 vs 70.25); corroborated by standalone current ratio deteriorating -15.87% (4.40x→3.70x) even as consolidated current ratio improves +6.44% (cash-cushioned by the ECB inflow) | Note 9 standalone p.82-83; Ratios Note 22(a)/22 standalone p.112, Note 20(a) consolidated p.156 | 🟡 Watch (feeds FLAG-CASH) | Genuine, if early-stage, working-capital deterioration at the parent, masked at group level by one-off ECB cash sitting on the balance sheet |
| 13 | ROCE declined at both levels (standalone 13.81%→11.20%, -18.93%; consolidated 13.82%→12.54%, -9.24%) despite standalone ROE rising; standalone and consolidated Ratios notes use two materially different, non-comparable "Capital employed" definitions in the same annual report | Note 22(j) standalone p.112, Note 20(j) consolidated p.156 | 🟡 Watch | Incremental capital deployed this year (debt-funded PPE/CWIP/advances) is earning a lower marginal return than the existing capital base even as leverage lifts the equity return; the definitional inconsistency also prevents like-for-like comparison |
| 14 | ₹1.47 Cr one-off gratuity Past Service Cost from the New Labour Code (plus ₹0.28 Cr leave encashment PSC) is booked as "Exceptional Items," excluding a genuine, unavoidable statutory cost from the "before exceptional items" profit metric (₹29.45 Cr standalone vs post-exceptional PBT ₹27.70 Cr) | Note 9B(iii) standalone p.106-107, consolidated p.149-150; Note 33/34 Exceptional Items standalone p.93, consolidated p.152 | 🟡 Watch | Investors relying on the pre-exceptional headline overstate recurring profitability; post-exceptional PBT is the more representative figure |
| 15 | Pervasive pattern of drafting/QC errors: standalone policy text states ROU assets depreciated on WDV basis while the actual standalone/consolidated note and figures use SLM (Note 1 p.97 vs Note 7 p.104); subsidiary share face value stated as ₹1 standalone vs ₹10 consolidated for the identical holding (Note 3 p.81 vs p.125); Exceptional Items note mislabeled "Total - Items That Will Not Be Reclassified To Profit Or Loss" (Note 33/34 p.93/p.152); standalone Note 34 duplicates note number "34:A(I)" with an inapplicable foreign-operation-translation line copied from the consolidated template (p.93); standalone Note 9 narrative states gratuity PSC as "₹1.74 Cr" against an arithmetic sum of ₹1.75 Cr (consolidated states 1.75 correctly) | Multiple, as cited | 🟡 Watch | No single instance is decision-critical, but the pattern signals weak note-preparation review discipline across both standalone and consolidated filings |

### B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Recognition policy itself unremarkable (Ind AS 115, cumulative catch-up, "insignificant" transition impact); but no contract asset/liability disclosure, no unsatisfied performance obligations, no geography split despite ~47% export revenue, and the subsidiary's Cast Magnets revenue collapse is entirely unexplained in the notes |
| Expense capitalisation honesty | 5 | New CWIP (₹8.08 Cr consolidated) and Capital Advances (+1406% consolidated) appear with zero explanatory notes; ₹1.47 Cr genuine recurring-type statutory cost reclassified as "Exceptional," flattering the pre-exceptional profit metric |
| Provisioning adequacy | 5 | Gratuity/leave actuarial assumptions reasonable in isolation but the standalone/consolidated discount-rate mismatch (7.25% vs 6.75%) for the same date undermines confidence; ECL allowance of 0.36% of gross receivables newly recognised with no ECL matrix disclosed to test adequacy |
| RPT fairness | 7 | No non-arm's-length signals; KMP remuneration modest in absolute terms (₹2.53 Cr, 1.1% of revenue) though MD remuneration grew faster (68.6%) than PAT (34.5%); personal guarantees of MD relatives securing company debt are disclosed, not hidden; "maximum balance outstanding" for the subsidiary loan appears to equal the closing balance rather than a true intra-year peak (Note 13 standalone p.107) |
| Disclosure transparency | 3 | Missing: Schedule III consolidated Additional Information table, CWIP ageing schedule, geography-wise revenue, ECL matrix, effective-vs-statutory tax rate reconciliation, FX sensitivity table, capitalisation threshold, impairment discount/growth-rate assumptions, incremental borrowing rate for leases — a long list of standard Ind AS/Schedule III disclosures absent across notes that are otherwise reasonably detailed elsewhere |
| Consistency with prior years | 4 | Cash Flow Statement PBT tie-out fails identically at both reporting levels; standalone-vs-consolidated figures diverge on profitability, liquidity, and ROCE trend direction in the same period; two incompatible "Capital employed" definitions used within the same annual report; multiple copy-paste/drafting errors between standalone and consolidated templates |
| **OVERALL** | **4** | Weighted down from the component average by the severity concentration in disclosure transparency and consistency (9 of the top 15 findings are Red Flag rated), and by the subsidiary's revenue-collapse-cum-debt-draw pattern, which is the most investor-relevant fact in the notes |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Subsidiary (Quantum Magnetics) revenue collapse alongside large unsecured ECB draw and unconverted capex-in-progress | High | Subsidiary standalone financials (if disclosed separately), consolidated Cast Magnets revenue line each quarter, CWIP-to-commissioned-asset conversion, ECB covenant/repayment status ahead of the July 2029 first instalment | Next 1-3 quarters for early signs; repayment moratorium means a cash-flow shock is not imminent, but a further revenue miss would be an early warning |
| Consolidated leverage step-change (debt-equity 0.17x to 0.56x) not visible in standalone accounts | High | Consolidated Ratios note each period; ECB interest/FX cost as it flows through consolidated P&L; whether the debt funds revenue-generating capacity or remains idle capex-in-progress | Ongoing; interest cost visible from FY27 onward, principal repayment risk from FY30 |
| Cash Flow Statement preparation error (PBT tie-out failure) | Medium | Whether corrected in FY27 filing; whether it recurs elsewhere in the statement | Next annual report |
| Missing Schedule III/CWIP/geography disclosures | Medium | Whether these are added in the FY27 annual report following auditor/regulator query | Next annual report cycle |
| ₹22.01 Cr disputed Central Excise interest contingency, unresolved for over a decade | Medium | Ministry of Finance settlement status; any change in "no liability expected" assessment | Indeterminate; long-pending, could resolve or escalate at any point |
| Going-concern language tied to unresolved 2015 winding-up order | Low-Medium (amount immaterial, phrasing unusual) | Resolution of the Bombay HC petition; whether future audit reports retain or drop the EOM linkage | Indeterminate |
| Standalone working-capital deterioration (receivables, current ratio) masked at group level by one-off ECB cash | Medium | Standalone receivable days and current ratio next 2-3 quarters once the ECB cash is deployed | Next 2-4 quarters |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. The subsidiary's Cast Magnets revenue collapsed ≈85.5% YoY (≈₹5.37 Cr to ≈₹0.78 Cr) in the same year it drew a ₹47.81 Cr unsecured ECB and built ≈₹15.5 Cr of capex-in-progress and capital advances — what caused the revenue collapse, and what is the utilisation plan, expected commissioning date, and underwritten return for this capex program?
2. The Cash Flow Statement's opening "Profit before tax" figure does not tie to the P&L "Profit before tax" line by exactly the ₹0.30 Cr other-comprehensive-income remeasurement amount, identically at both standalone (₹28.00 Cr vs ₹27.70 Cr) and consolidated (₹22.69 Cr vs ₹22.39 Cr) level — is this a preparation error, and will it be corrected in the next filing?
3. Why does the actuarial discount rate used to value gratuity and leave encashment differ between the standalone (7.25%) and consolidated (6.75%) financial statements for the identical 31 March 2026 balance sheet date?
4. What is the current status of the 2015 Bombay High Court winding-up petition that the auditor explicitly cites as the basis for the going-concern assumption, and of the ₹22.01 Cr disputed Central Excise interest liability that has remained unresolved since a 2013 approach to the Ministry of Finance?
5. Why are the Schedule III mandatory consolidated "Additional Information" table (net assets and profit/loss share by entity) and the Capital Work-in-Progress ageing schedule (₹8.08 Cr consolidated, first year of appearance) absent from the FY26 notes, and when will they be included?

### E. NOTES-BASED RED FLAGS

- Subsidiary revenue collapse concurrent with large unsecured debt draw and unconverted capex — pattern consistent with capital being deployed faster than the underlying business can absorb it; not itself evidence of earnings management, but warrants close monitoring for potential related-party or intercompany dynamics not visible in the notes.
- Systemic Cash Flow Statement PBT tie-out failure at both reporting levels — a genuine preparation-quality defect, not merely a rounding artefact.
- Missing mandatory disclosures (Schedule III Additional Information, CWIP ageing schedule, geography revenue split, ECL matrix, tax rate reconciliation, FX sensitivity) — a completeness gap pattern rather than an aggressive-accounting pattern; no evidence found of deliberately misleading disclosure, but the volume of absences is itself a transparency concern.
- Actuarial discount-rate inconsistency and "Capital employed" definitional inconsistency between standalone and consolidated notes of the same report — internal-consistency failures that limit reliability of derived ratios.
- One-off statutory cost (gratuity Past Service Cost) classified as "Exceptional," which is defensible given its non-recurring regulatory trigger but does inflate the pre-exceptional profit metric that management highlights.
- No evidence of revenue-recognition manipulation, channel stuffing (finished goods inventory actually declined), reserve-bypass accounting, or MSME payment abuse was found in the notes.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate-to-concerning accounting practices, weighted down by disclosure gaps and a Cash Flow Statement tie-out failure rather than by evidence of deliberate earnings management. Key concern: the subsidiary's Cast Magnets revenue collapsed roughly 85.5% in the same year it drew a ₹47.81 Cr unsecured ECB and built roughly ₹15.5 Cr of unconverted capex, dragging consolidated profitability and leverage in a direction the standalone highlights alone would never reveal. Key strength: no evidence of revenue-recognition aggressiveness, channel stuffing, reserve-bypass accounting, or MSME payment abuse; RPTs are modest and CSR/dividend/share-capital items are fully clean. Overall accounting quality: 4/10.

---

```yaml
stage: B02-notes
company: "PERMAGNET"
run_date: "2026-08-19"
model: claude-sonnet-5
status: complete
input_gaps: []
flags:
  - {type: FLAG-CASH, reason: "Standalone trade receivables +39.4% vs revenue +13.0%; receivable days +5.3% (standalone) to +7.9% (consolidated); standalone current ratio deteriorating -15.87% even as consolidated liquidity is temporarily cushioned by one-off ECB cash (Note 9 standalone p.82-83; Ratios Note 22 standalone p.112, Note 20 consolidated p.156)"}
accounting_quality: 4        # /10
pass_2_empty: false
pass_3_empty: true
top_findings:                # max 15
  - {rank: 1, finding: "Subsidiary's Cast Magnets revenue collapsed ~85.5% YoY (~Rs.5.37 Cr to ~Rs.0.78 Cr) same year subsidiary drew Rs.47.81 Cr unsecured ECB and built ~Rs.15.5 Cr capex-in-progress", note_ref: "Note 25 standalone p.90 vs Note 26 consolidated p.128", rating: "Red Flag", why: "Subsidiary top line evaporated while its balance sheet expanded on borrowed money; most consequential group-risk fact in the notes"}
  - {rank: 2, finding: "Standalone PAT +36.5% (Rs.20.69 Cr) vs Consolidated PAT -4.3% (Rs.15.07 Cr); standalone ROE 13.31% up vs consolidated ROE 9.57% down", note_ref: "Note 15/EPS/Ratios standalone p.85-86, p.112; consolidated p.131-132, p.156", rating: "Red Flag", why: "Listed entity's standalone highlights mask deteriorating group profitability driven entirely by the subsidiary"}
  - {rank: 3, finding: "New Rs.47.81 Cr unsecured ECB at subsidiary (5% simple interest, ~$5m) drives consolidated debt-equity from 0.17x to 0.56x (+238.04%); invisible in standalone accounts", note_ref: "Note 16 consolidated p.131-132; Ratios Note 20 consolidated p.156", rating: "Red Flag", why: "Largest single capital-structure change in the year with unquantified currency/rate exposure"}
  - {rank: 4, finding: "Cash Flow Statement PBT fails to tie to P&L PBT by exactly the Rs.0.30 Cr OCI remeasurement amount, identically at standalone and consolidated level", note_ref: "P&L p.77/p.121 vs Cash Flow p.78/p.122", rating: "Red Flag", why: "Repeatable, non-rounding mechanical error in Cash Flow Statement preparation at both reporting levels"}
  - {rank: 5, finding: "Mandatory Schedule III consolidated Additional Information table (net assets/profit share by entity) is absent from the notes", note_ref: "Searched Notes 1-36 consolidated, not found", rating: "Red Flag", why: "Standard disclosure requirement; absence prevents independent verification of subsidiary's contribution to consolidated totals"}
  - {rank: 6, finding: "New unsupported Capital Work-in-Progress balance sheet line (Rs.3.37 Cr standalone, Rs.8.08 Cr consolidated, FY25 Nil) with no CWIP ageing schedule anywhere in the document", note_ref: "Balance Sheets p.76/p.120; searched Notes, not found", rating: "Red Flag", why: "Schedule III mandates a CWIP ageing schedule when material (5.1% of consolidated total assets); wholly absent"}
  - {rank: 7, finding: "Consolidated Capital Advances rose Rs.1.05 Cr to Rs.15.81 Cr (+1405.7%), implying ~Rs.10.83 Cr sits at the subsidiary alone", note_ref: "Note 7 consolidated p.126", rating: "Red Flag", why: "Combined with CWIP, ~Rs.15.5 Cr of new ECB proceeds not yet converted into revenue-generating capacity"}
  - {rank: 8, finding: "Auditor's Emphasis of Matter ties going concern basis explicitly to Note 3, a 2015 Bombay HC winding-up order (Rs.0.13 Cr claim) under interim stay since 2015, still unresolved", note_ref: "Auditor's EOM standalone p.66, consolidated p.113; Note 3 standalone p.104, consolidated p.148", rating: "Red Flag", why: "Unusual audit-report phrasing linking going concern to a decade-unresolved winding-up order"}
  - {rank: 9, finding: "Rs.22.01 Cr disputed Central Excise interest contingency ~13-14% of net worth, unresolved since 2013; CARO adds 12% simple interest, default window Oct 2002-Nov 2017, auditor figure Rs.1.75 Cr vs company figure Rs.1.76 Cr", note_ref: "Note 2(f) standalone p.103-104, consolidated p.147-148; CARO Annexure A ix(a) standalone p.72", rating: "Red Flag", why: "Single largest contingent liability item, exceeds 10% of net worth materiality threshold, long unresolved"}
  - {rank: 10, finding: "Actuarial discount rate for gratuity/leave differs: standalone 7.25% vs consolidated 6.75% for the identical FY26 balance sheet date", note_ref: "Note 9A standalone p.106, consolidated p.150", rating: "Red Flag", why: "Should not differ for the same economic assumption unless a different valuation basis is used; needs clarification"}
  - {rank: 11, finding: "No geography-wise revenue disclosure despite exports ~47% of revenue (Rs.106.05-106.82 Cr FOB) across multiple continents", note_ref: "Note 25/26 vs Note 14D/13D standalone p.90, p.108; consolidated p.128, p.152", rating: "Red Flag", why: "Ind AS 108 entity-wide disclosure gap given near-majority export exposure"}
  - {rank: 12, finding: "Trade receivables +39.4% vs revenue +13.0%; receivable days +5.3% standalone to +7.9% consolidated; standalone current ratio deteriorating -15.87% even as consolidated ratio improves +6.44% on one-off ECB cash", note_ref: "Note 9 standalone p.82-83; Ratios Note 22(a) standalone p.112, Note 20(a) consolidated p.156", rating: "Watch", why: "Genuine early-stage working-capital deterioration masked at group level by ECB cash; feeds FLAG-CASH"}
  - {rank: 13, finding: "ROCE declined at both levels (standalone -18.93%, consolidated -9.24%) despite rising standalone ROE; standalone and consolidated Ratios notes use two incompatible Capital Employed definitions", note_ref: "Note 22(j) standalone p.112, Note 20(j) consolidated p.156", rating: "Watch", why: "Incremental capital is earning a lower marginal return than the existing base; definitional inconsistency blocks comparability"}
  - {rank: 14, finding: "Rs.1.47 Cr one-off gratuity Past Service Cost (New Labour Code) booked as Exceptional Item, excluding a genuine unavoidable statutory cost from the before-exceptional profit metric", note_ref: "Note 9B(iii) standalone p.106-107; Note 33/34 standalone p.93, consolidated p.152", rating: "Watch", why: "Pre-exceptional headline overstates recurring profitability versus post-exceptional PBT of Rs.27.70 Cr"}
  - {rank: 15, finding: "Pattern of drafting/QC errors: ROU depreciation stated WDV in policy text vs SLM in actual note/figures; subsidiary share face value Rs.1 standalone vs Rs.10 consolidated; mislabeled Exceptional Items heading; duplicated note number 34:A(I) with inapplicable copied line; standalone gratuity PSC stated Rs.1.74 Cr vs arithmetic Rs.1.75 Cr", note_ref: "Note 1 p.97 vs Note 7 p.104; Note 3 p.81 vs p.125; Note 33/34 p.93/p.152", rating: "Watch", why: "No single instance decision-critical, but the pattern signals weak note-preparation review discipline"}
red_flags:
  - "Subsidiary Cast Magnets revenue collapse ~85.5% YoY concurrent with Rs.47.81 Cr unsecured ECB draw and unconverted capex (Note 25 standalone p.90 vs Note 26 consolidated p.128)"
  - "Standalone-vs-consolidated PAT/ROE divergence: parent business improving, group deteriorating (Note 15/Ratios, p.85-86/112 standalone, p.131-132/156 consolidated)"
  - "New Rs.47.81 Cr unsecured ECB pushes consolidated debt-equity up 238%, invisible in standalone accounts (Note 16 consolidated p.131-132)"
  - "Cash Flow Statement PBT tie-out failure of Rs.0.30 Cr at both standalone and consolidated level (P&L p.77/p.121 vs Cash Flow p.78/p.122)"
  - "Missing Schedule III consolidated Additional Information table (searched, not found)"
  - "New Capital Work-in-Progress balance sheet line with no ageing schedule anywhere (Balance Sheets p.76/p.120)"
  - "Consolidated Capital Advances +1406%, ~Rs.10.83 Cr unconverted at subsidiary (Note 7 consolidated p.126)"
  - "Going concern language explicitly tied to unresolved 2015 winding-up order (Auditor's EOM p.66/p.113; Note 3 p.104/p.148)"
  - "Rs.22.01 Cr disputed Central Excise interest contingency, ~13-14% of net worth, unresolved over a decade (Note 2(f) standalone p.103-104, consolidated p.147-148)"
  - "Actuarial discount rate mismatch: standalone 7.25% vs consolidated 6.75% for identical FY26 date (Note 9A p.106/p.150)"
  - "No geography-wise revenue disclosure despite ~47% export revenue (Note 25/26 vs Note 14D/13D)"
questions_for_mgmt:
  - "What caused the subsidiary's Cast Magnets revenue to collapse ~85.5% YoY in the same year it drew a Rs.47.81 Cr unsecured ECB and built ~Rs.15.5 Cr of capex-in-progress/capital advances, and what is the utilisation and commissioning timeline?"
  - "Why does the Cash Flow Statement's PBT not tie to the P&L PBT by exactly the Rs.0.30 Cr OCI remeasurement amount at both standalone and consolidated level, and will this be corrected?"
  - "Why does the actuarial discount rate for gratuity/leave differ between standalone (7.25%) and consolidated (6.75%) for the identical 31 March 2026 balance sheet date?"
  - "What is the current status of the 2015 Bombay High Court winding-up petition cited by the auditor as the going-concern basis, and of the Rs.22.01 Cr disputed Central Excise interest liability unresolved since 2013?"
  - "Why are the Schedule III consolidated Additional Information table and the CWIP ageing schedule absent from the FY26 notes, and when will they be added?"
receivables_trend: "deteriorating: standalone trade receivables +39.4% (Rs.39.24 Cr to Rs.54.68 Cr net) vs revenue +13.0%; receivable days +5.3% standalone (72.19 to 76.03) and +7.9% consolidated (70.25 to 75.77); ageing quality itself remains high (99.3% under 6 months) but the growth-rate and days trend are both adverse for a second consecutive comparison point (Note 9 standalone p.82-83; Ratios Note 22 standalone p.112, Note 20 consolidated p.156)"
restatements_found: []
going_concern_language: "Auditor's Emphasis of Matter (standalone p.66, consolidated p.113): \"The financial statements of the company [Group] have been prepared on a Going Concern Basis on reasons mentioned in note no. 3 of notes of accounts.\" Note 3 (standalone p.104, consolidated p.148) describes a 2015 Bombay High Court winding-up order on a Rs.0.13 Cr petition, under interim stay since 2015, unresolved."
analyst_note: "The two most important facts in these notes sit in different places and only connect when standalone and consolidated notes are read side by side: the subsidiary's core revenue line effectively disappeared (Cast Magnets ~85.5% down) in the exact year it drew Rs.47.81 Cr of new unsecured debt and built Rs.15.5 Cr of unconverted capex. Neither the standalone accounts (which look clean and improving) nor any single consolidated note states this outright; it required subtracting standalone from consolidated revenue and capex disaggregation across two different notes. Downstream valuation/synthesis stages should treat the standalone-only profitability picture as materially incomplete and weight the consolidated, subsidiary-inclusive numbers as the operative reality for risk purposes. The Cash Flow Statement PBT tie-out failure, while mechanical, corroborates a broader note-preparation quality concern that recurs across both standalone and consolidated filings."
```
