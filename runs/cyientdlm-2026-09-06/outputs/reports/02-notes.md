# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: CYIENTDLM | Run date: 2026-09-06
Source: AR FY2025-26 (Annual_Report_2026.pdf, 174 pages); AR FY2024-25 (Annual_Report_2025.pdf,
287 pages) used for two-year persistence and restatement checks only.

## PASS 3: PATTERN RE-READ

Method: instead of note-by-note, searched the full document text for contradiction, restatement,
and going-concern signal patterns, and checked three specific claims from Pass 1/Pass 2 against the
source directly.

- Restatement check: searched the entire AR text for "regroup", "reclassif", "restat". Every hit in
  the financial-statement text (lines ~13554, 15465, 15696, 17613-17620, 18265, 19838, 19987) is
  either standard OCI-recycling accounting-policy boilerplate ("items that will not be reclassified
  subsequently to profit or loss") or a standard Ind AS 8/new-standard-adoption disclaimer ("an
  entity cannot restate comparative information" re: Ind AS 21 exchangeability amendments, p. line
  14676/18993 — prospective-only, immaterial, confirmed "no material impact"). The only actual
  restatements found anywhere in the document are BRSR/sustainability water-footprint and RBI
  location-classification restatements (lines 9528, 9800), which sit in the ESG section, out of
  scope for financial notes. CONFIRMS Pass 2: no restatement of any financial-statement figure.
- Going-concern check: searched for "going concern" and "material uncertainty" across the document.
  All hits (lines 12768-12820, standalone auditor's report; 17181-17236, consolidated auditor's
  report) are the standard SA 700/SA 570 auditor-responsibility paragraph describing what the
  auditor would do IF a material uncertainty existed. No conclusion of a material uncertainty, no
  emphasis-of-matter paragraph, no management going-concern note anywhere. CONFIRMS Pass 1: NONE.
- Cross-check of the standalone-vs-consolidated Note-35 numbering collision: standalone Note 35
  (Ratio Analysis, p.136-137) and consolidated Note 35 (Schedule III entity-wise net assets/profit,
  p.171) are two different disclosures that happen to share a note number because standalone and
  consolidated statements number independently. Both passes anchored this correctly; flagged here
  only so a downstream stage does not conflate the two under one "Note 35" citation.

PASS 3: NO MATERIAL NEW FINDINGS beyond the three confirmations above (which strengthen, not add
to, Pass 1/Pass 2's existing "no restatement" / "no going concern" conclusions). Proceeding to the
required consolidation.

═══════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Entity-wise Schedule III table shows 100% of consolidated PAT growth (+7.65%, Rs680.76mn→Rs732.82mn) is manufactured at the US-subsidiary level (Cyient DLM Inc. swung from a Rs84.69mn loss to a Rs246.69mn profit, +Rs331.38mn); the Indian parent's own standalone PAT FELL 26.6% (Rs766.98mn→Rs563.24mn) | Note 35 CONSOLIDATED, p.171 | 🔴 Red Flag | Proves, with the company's own numbers, that the headline consolidated growth story is a mix-shift artifact, not operating improvement; the actual India EMS business is shrinking on both revenue and profit |
| 2 | India-geography revenue collapse: consolidated -83.2% (Rs7,256.92mn→Rs1,218.90mn), standalone -84.4%; standalone total revenue -29.9% vs consolidated -17.0%, cushioned entirely by the newly acquired US-based Altek subsidiary | Note 20/34 CONSOLIDATED p.162/171; Note 33 STANDALONE p.135 | 🔴 Red Flag | The core India EMS operation, the entity investors are actually valuing the transition thesis on, has contracted sharply; consolidation optics hide this |
| 3 | Changes-in-inventory P&L line: consolidated swing of Rs538.33mn favourable ((325.79) FY26 build vs 212.54 FY25 drawdown) — the single LARGEST profit-flattering item this year, larger than the Altek fair-value gain and ESOP reversal combined | Note 23 CONSOLIDATED p.163-164; STANDALONE p.128-129 | 🔴 Red Flag | Reported PBT is flattered by unsold production sitting in the warehouse; if this inventory does not sell through, it converts to future write-downs or cash-tied-up losses rather than profit already booked |
| 4 | Rs195.75mn non-cash, non-operating fair-value gain on the Altek contingent-consideration (earn-out) liability, unlabelled as exceptional, drove reported PBT (Rs931.61mn, roughly flat YoY); PBT ex-gain fell ~19.8% YoY, in line with revenue. Altek's own full-year FY26 profit (Rs31.32mn) is LOWER than its part-year FY25 profit (Rs39.70mn, ~6 months) — annualised run-rate implies >50% profit decline | Note 21 p.161-162; Note 33.1.4 p.170; Note 35 p.171 (all CONSOLIDATED) | 🔴 Red Flag | The earn-out gain is booked as income precisely because Altek is missing its acquisition-case targets; the gain and the miss are the same event viewed from two notes |
| 5 | Inventory +13.3% consolidated (Rs5,712.73mn→Rs6,473.32mn; finished goods +52.0%), +11.8% standalone-only, while revenue fell 17-30%; trade payable days stretched ~84→~127 days; unbilled payables +125.6% (Rs288.05mn→Rs650.06mn); Rs368.47mn of IPO capex proceeds reallocated to working capital 23-Mar-2026, 8 days before year-end | Note 9 CONSOLIDATED p.155, STANDALONE p.116; Note 17 p.161-162; Note 12(h) p.158-159 | 🔴 Red Flag | Working-capital strain (inventory build + payable stretch + IPO-fund reallocation) directly corroborates Gate 0's cumulative FY2023-26 CFO of -Rs25.07cr against PAT of +Rs234.29cr |
| 6 | New, material related-party subcontracting flow to ultimate parent Cyient Limited: Rs537.56mn (from Rs NIL FY25), payable balance up 257% to Rs442.12mn; no arm's-length benchmarking disclosed beyond boilerplate language | Note 30 CONSOLIDATED/STANDALONE p.164-166/132-134 | 🔴 Red Flag | Appeared from zero to ~4.3% of consolidated revenue in one year, paid up to the listed parent, coincident with the India revenue collapse; pricing basis unverifiable from the notes |
| 7 | Debt Service Coverage Ratio fell below 1.0x: 1.67x→0.62x (-62.9%), per the company's own mandatory Schedule III ratio disclosure | Note 35 STANDALONE p.136-137 | 🔴 Red Flag | Earnings available for debt service did not cover interest, lease, and principal obligations this year; management's stated reasons (deleveraging + "reduction in operations") do not separate voluntary overpayment from genuine earnings weakness |
| 8 | Unhedged FX exposure grew ~15x: 5% sensitivity impact on PBT Rs4.87mn (FY25)→Rs73.38mn (FY26); "no material outstanding [forward] contracts" as export mix (NAM+EMEA) rose to ~86.5% of consolidated revenue from ~50.4% | Note 33.2 CONSOLIDATED p.171 | 🔴 Red Flag | A new, quantifiable, currently uncovered risk that grew materially larger exactly as the revenue mix shifted export-heavy |
| 9 | Customer concentration remains extreme: top customers (each ≥10%) = 55.71% consolidated / 70.54% standalone of revenue (improved from 69.21%/78.19% prior year) | Note 20/33, both statements | 🔴 Red Flag | Structural, persistent concentration risk; a single customer loss would be material at either entity level |
| 10 | Standalone employee benefits expense FELL 18.8% (Rs1,294.20mn→Rs1,051.60mn) despite absorbing a one-time Rs17.27mn Labour Code catch-up charge, while CONSOLIDATED employee cost ROSE 21.8% (driven entirely by a full year of Altek headcount vs the acquisition's Oct-2024 mid-year entry) | Note 24 STANDALONE p.129, CONSOLIDATED p.164 | 🟡 Watch | A second, independent metric beyond revenue (Finding 2) showing the consolidated income statement masks a shrinking India operation behind the newly consolidated US subsidiary |
| 11 | Permanent, P&L-bypassing FVTOCI loss on the Stuam Technologies (unquoted equity) investment: cumulative Rs792.88mn destroyed over two years (84.5% of original Rs662.12mn value); the irrevocable FVTOCI election means this loss will NEVER pass through the income statement | Note 6/13(f)/33.1.4 CONSOLIDATED p.154/160/169-170 | 🟡 Watch | Legitimate accounting election, not a violation, but a genuine, permanent value destruction invisible to a P&L-only reading of the accounts |
| 12 | Two of three Key Audit Matters (inventory obsolescence, investment valuation) are UNCHANGED for a second consecutive year vs AR FY2024-25, near-identical wording | Independent Auditor's Report, standalone, AR FY2025-26 p.104-106; cross-checked AR FY2024-25 | 🟡 Watch | Upgrades both items from "this year's disclosure is thin" to "a structural, recurring judgement risk area the company has not resolved or shrunk over two annual cycles" |
| 13 | Share-based payment expense reversed to a Rs28.92mn CREDIT (from a Rs62.16mn charge in FY25) due to mass ESOP/RSU forfeitures tied to the CEO (Jul-2025) and CFO (Oct-2025) transitions | Note 24 CONSOLIDATED p.163 | 🟡 Watch | Mechanically correct under Ind AS 102, but another item flattering reported profit in a declining-revenue year; combines with Findings 3 and 4 to compound the profit-quality question |
| 14 | Total cash and bank balances fell 56.3% (Rs2,877.82mn→Rs1,258.00mn) as IPO proceeds were fully utilised; against this, unutilised bank credit limits stayed essentially stable and substantial (Rs4,412.80mn→Rs4,172.60mn) | Note 33.2 CONSOLIDATED, Liquidity risk, p.169 | 🟡 Watch (mixed) | The cash cushion carried into FY26 is now largely spent (on debt repayment and, per Finding 5, working capital); the stable credit-line cushion is a genuine, quantified mitigant that should sit alongside the Gate 0 cash-conversion deal-breaker, not resolve it |
| 15 | No "events after the reporting period" note found anywhere, despite a ~3-week gap to board approval (21-Apr-2026), a CEO change (Jul-2025), a CFO change (Oct-2025), and a Citibank loan amendment dated 23-Mar-2026 (8 days before year-end, unexplained rationale) all sitting close to or within the reporting period | Note 1 CONSOLIDATED/STANDALONE p.146/111 | 🟡 Watch | A disclosure-completeness gap for a company with unusual within-period events that a reader would expect a subsequent-events note to address |

## B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | Standard point-in-time/POC/practical-expedient policies (Note 2.14, CONSOLIDATED p.148-149), immaterial variable-consideration and discount adjustments (Note 20.3); the collapse is a business-performance fact, not a recognition-policy aggression |
| Expense capitalisation honesty | 7 | Useful lives at or shorter than Schedule II (Note 2.7, p.147), no lengthening found; no explicit capitalisation threshold disclosed (NOT FOUND) is a minor gap, not evidence of aggression |
| Provisioning adequacy | 6 | ECL matrix (Note 10) and gratuity funding (Note 29) reasonable and improving; inventory obsolescence provision (Note 9) tracks the inventory build roughly in proportion but the item is a two-year-running Key Audit Matter (Finding 12) that has not shrunk; CARO GST dispute (Rs2.08mn) not surfaced in Note 28's "NIL" contingent-liabilities statement is a minor completeness gap |
| RPT fairness | 5 | New Rs537.56mn subcontracting flow to the parent with no arm's-length benchmarking beyond boilerplate (Finding 6); KMP cash compensation rose 18.4% in a year of declining standalone revenue and ROE/ROCE; against this, the parent term loan was fully repaid and the parent's guarantee to bankers was released (both reduce related-party dependency) |
| Disclosure transparency | 4 | Three separate items (Altek FV gain Rs195.75mn, inventory-build P&L credit Rs538.33mn, ESOP reversal Rs28.92mn credit vs Rs62.16mn charge) prop up reported PBT/PAT and none is labelled "exceptional" or non-recurring; the standalone ratio note (Note 35) reuses one generic reason across six deteriorating ratios and applies its own >20% variance-flagging threshold inconsistently (ROCE fell 23.2% with "NA" coded); lease discount rate (Note 3B) and capitalisation threshold are not numerically disclosed; no events-after-reporting-period note (Finding 15) |
| Consistency with prior years | 7 | No restatements found anywhere in the financial notes (Pass 3 confirmed); useful lives, ECL matrix, and accounting policies unchanged; two Key Audit Matters persisting unchanged for a second year is a consistency finding in itself, coded as a watch item rather than a penalty here since it reflects an unresolved judgement area, not a policy inconsistency |
| **OVERALL** | **4** | Not a simple average: no violation, no restatement, no going-concern qualification, and no covenant breach were found, but the top-ranked findings (Rank 1-6 above) show a headline consolidated growth number entirely constructed from segment mix and three unlabelled non-recurring items, sitting on top of a genuine India-core revenue and profit contraction and a working-capital deterioration that independently corroborates Gate 0's cash-conversion deal-breaker. The profit-quality gap is the dominant fact for an investor, and the overall score is weighted to reflect that |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Quality-of-earnings: reported PBT propped by non-recurring items (Rs195.75mn Altek FV gain + Rs538.33mn inventory-build credit + ~Rs91mn ESOP-reversal swing) exceeding the entire YoY PBT change | HIGH | Note 21 fair-value gain direction each quarter, Note 23 inventory drawdown, ESOP forfeiture trend | FY27, if inventory does not sell through or the earn-out liability is remeasured up |
| India core business contraction masked by the Altek acquisition (standalone revenue -29.9%, standalone PAT -26.6%, geography -84.4%) | HIGH | Standalone-only segment and geography figures each quarter, not just consolidated headlines | Already crystallized; watch for further deterioration or stabilisation |
| Working-capital deterioration / cash conversion (independently corroborates the Gate 0 deal-breaker: cumulative FY2023-26 CFO -Rs25.07cr vs PAT +Rs234.29cr) | HIGH | CFO vs PAT, NWC days (48/79/127/145 FY23-26), inventory and payable days, IPO-fund utilisation | Active now; FY27 Q1-Q2 will show if the Mar-2026 reallocation resolves or repeats |
| Altek underperforming its acquisition-case earn-out targets (FY26 full-year profit Rs31.32mn below FY25's ~6-month profit of Rs39.70mn) | MEDIUM-HIGH | Note 35 entity-level PAT each year, direction of future earn-out remeasurements (Note 21/33.1.4) | Visible at each annual report; next earn-out true-up |
| Debt Service Coverage Ratio below 1.0x (0.62x) | MEDIUM | DSCR trend, Citibank quarterly instalment schedule (raised from USD0.51mn to USD0.75mn per the 23-Mar-2026 amendment) | Each quarterly debt-service date through FY27-29 |
| Unhedged FX exposure (~15x sensitivity increase) against an export mix now ~86.5% of revenue | MEDIUM-HIGH | Whether forward contracts are initiated; INR/USD volatility | Any material currency move before hedging is put in place |
| Customer concentration (55.71% consolidated / 70.54% standalone in top customers) | MEDIUM-HIGH, structural | Top-customer % each year, any single-customer program loss | Ongoing; crystallizes on any customer loss |
| Related-party subcontracting to parent with no benchmarking (Rs537.56mn, +257% payable) | MEDIUM | Note 30 RPT amounts and payable balance to Cyient Limited | Ongoing; watch for further growth or a pricing-policy disclosure |
| Recurring, unresolved Key Audit Matters (inventory obsolescence, investment valuation) for a second straight year | MEDIUM | Provision-to-inventory ratio, Stuam Technologies fair value | Each year-end audit cycle |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. What specifically caused standalone India-geography revenue to fall 84.4%, and what is the business rationale and pricing basis for the new Rs537.56mn subcontracting arrangement with parent Cyient Limited — is India-based design or manufacturing work being re-routed through the parent?
2. Given Altek Electronics' full-year FY26 profit (Rs31.32mn) is below its part-year FY25 profit (Rs39.70mn, ~6 months), what is management's revised view of Altek meeting its original acquisition-case earn-out targets, and should investors expect further downward remeasurement of the contingent-consideration liability (i.e., further fair-value gains booked to Other Income)?
3. What is management's plan and timeline to sell through the built-up finished-goods (+52%) and raw-material inventory that generated the Rs538.33mn (consolidated) favourable swing in the changes-in-inventory P&L line this year, and what happens to that swing if the underlying demand weakness is not temporary?
4. Why did the Debt Service Coverage Ratio fall below 1.0x (0.62x), and why was the Citibank term loan amended eight days before year-end (23-Mar-2026) to simultaneously reduce the margin (1.76% to 1.5%) and accelerate the quarterly instalment (USD0.51mn to USD0.75mn) — was this a covenant-related renegotiation rather than a routine refinancing?
5. Why is there no "events after the reporting period" note despite a CEO transition (Jul-2025), a CFO transition (Oct-2025), and the Citibank loan amendment (23-Mar-2026) all sitting close to or within the reporting period, and can management confirm no other subsequent event through the 21-Apr-2026 approval date requires disclosure?

## E. NOTES-BASED RED FLAGS

- India standalone revenue collapse (-29.9%; geography -84.4%) masked at the consolidated level (-17.0%) by the newly acquired Altek subsidiary.
- Consolidated PAT growth (+7.65%) is entirely attributable to the US-subsidiary structure; the Indian parent's own standalone PAT fell 26.6% (Note 35 CONSOLIDATED, p.171).
- Reported PBT is propped by three unlabelled, non-recurring items: Rs195.75mn Altek earn-out fair-value gain, Rs538.33mn inventory-build P&L credit, and a ~Rs91mn ESOP-reversal swing — combined larger than the entire YoY PBT movement.
- Altek Electronics' full-year FY26 profit (Rs31.32mn) is lower than its part-year FY25 profit (Rs39.70mn), evidencing a miss against the acquisition-case earn-out targets that the FY26 fair-value gain implicitly concedes.
- Inventory +13.3% consolidated (finished goods +52.0%) while revenue fell 17-30%; trade payable days stretched ~84 to ~127; unbilled payables +125.6%.
- New related-party subcontracting flow to the ultimate parent, Rs537.56mn from Rs NIL, with no arm's-length benchmarking disclosed beyond boilerplate language.
- Debt Service Coverage Ratio fell below 1.0x (1.67x to 0.62x).
- Unhedged FX exposure grew ~15x with "no material outstanding forward contracts" as the export mix rose to ~86.5% of revenue.
- Extreme, persistent customer concentration (55.71% consolidated / 70.54% standalone in top customers).
- No events-after-reporting-period note despite a leadership transition and a late (8-days-before-year-end) loan amendment.
- Minor: a Rs2.08mn GST dispute disclosed in the CARO annexure (p.107) is not surfaced in Note 28's "NIL" contingent-liabilities statement — a completeness gap, immaterial in size (~0.02% of consolidated net worth).

## F. ONE-LINE NOTES VERDICT

The notes reveal concerning accounting practices. Key concern: the headline consolidated profit growth is manufactured entirely by a US-subsidiary mix shift and three unlabelled non-recurring items, while the India core business and its cash conversion deteriorate underneath. Key strength: no restatements, no going-concern qualification, no covenant breach, and genuine deleveraging with a stable unused credit-line cushion. Overall accounting quality: 4/10.

═══════════════════════════════════════════════════════════
