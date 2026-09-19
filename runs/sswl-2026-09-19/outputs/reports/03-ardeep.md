# Stage 3 — Annual Report Deep Dive, Backward Read

Company: Steel Strips Wheels Ltd (SSWL) | Run date: 2026-09-19
Source: inputs/annual-report/SSWL-AR-FY26-Reg34-2026-09-03.txt (page-marked text of the 245-page PDF; "AR p.N" cites the PDF page). Unit as printed on the face of every statement and note: Rs in Lakhs (AR); this report states every AR figure as "Rs X lakh (Rs Y Cr)" and clearly labels any screener/other-source figure separately. FY25 comparatives are carried inside this FY26 AR; no standalone FY25 AR is in the corpus.
Method: backward read (auditor's report/CARO -> notes -> financial statements -> risk/MD&A -> governance -> front matter), per protocol v1.3. Phase 2 reuses and extends the Stage 2 triple-pass (outputs/reports/02-notes.md).

LOAD-BEARING FACTS CHECKED FIRST (company memory SPEAR, all four touch the AR):

- **LBF1 (guidance vs delivery)**: NOT SETTLED BY THIS AR. The AR's Board's Report and MD&A carry qualitative outlook language ("diversifying towards European Region", "increasing footprints in Export markets") but **no numeric FY27 revenue or export guidance table anywhere** (verified by full-text search for "guidance", "6,500", "outlook for"; none found — AR p.19-32 Board's Report, AR p.119-126 MD&A). The one AR-native cross-check available is Annexure IV's actual FY26 foreign exchange inflow, Rs 50,873.51 lakh (Rs 508.73 Cr) (AR p.44-45), against company memory's transcript-sourced FY27 export guidance of ~Rs 600 Cr — a plausible +18% trajectory, but the ~Rs 600 Cr figure itself is NOT FOUND IN THIS AR (it is a transcript number, outside this document). Stage 3 cannot verify LBF1; it stays a Stage 5/8 (transcript) item.
- **LBF2 (mix-shift margin)**: PARTIALLY SETTLED, DIRECTIONALLY CONFIRMED, MAGNITUDE UNVERIFIABLE PAST 2 YEARS FROM THIS AR. The AR's own MD&A Key Financial Ratios table (AR p.122) shows standalone Operating Profit Margin (PBIT/net sales) falling from 9.01% (FY25) to 7.61% (FY26), a 15.54% relative decline, and Net Profit Margin falling from 4.74% to 3.90%. On a consolidated basis (computed from Board's Report Financial Highlights, AR p.19), EBITDA margin fell from 11.01% (FY25, Rs 48,750.75 lakh / Rs 4,42,899.83 lakh) to 9.91% (FY26, Rs 51,340.04 lakh / Rs 5,18,280.25 lakh) — this 9.91% figure lands very close to company memory's "~9.8% FY26" anchor. But the AR carries only a two-year comparative window (FY25-FY26); the FY22 baseline (~12.7%) named in LBF2 is **NOT FOUND IN THIS AR** and needs the screener Data_Sheet.csv or an older AR. Knuckle unit sales grew 46,952 to 257,147 (+448%) (AR p.23) — strong evidence of the alloy/knuckle mix shift in volume terms — but **no product-level revenue or margin split exists anywhere in the AR** (single Ind AS 108 segment, AR p.126, confirmed again at consolidated Note 44 by Stage 2 Finding 14). LBF2's EBITDA-per-wheel and alloy-%-of-revenue figures are NOT FOUND IN THIS AR.
- **LBF3 (cash conversion)**: SETTLED AND SHARPENED. Standalone Cash Flow Statement (AR p.141): CFO fell from Rs 51,760.29 lakh (Rs 517.60 Cr) in FY25 to Rs 33,115.53 lakh (Rs 331.16 Cr) in FY26, a **36% YoY collapse**, while EBITDA grew 4.54% over the same period. CFO/EBITDA fell from 103.5% (FY25) to 63.3% (FY26). The driver, visible on the face of the cash flow statement itself: inventory build consumed Rs 20,939.37 lakh cash (vs Rs 4,618.14 lakh FY25) and receivables build consumed Rs 12,264.75 lakh (vs Rs 4,664.36 lakh FY25), partly offset by a Rs 24,969.70 lakh payables increase — the payables increase is the reverse-factoring mechanism Stage 2 Finding 4 identified (Note 25, Rs 676.50 Cr Supplier Finance Arrangement, 67.6% of payables). Year-end cash Rs 652.14 lakh (Rs 6.52 Cr) (AR p.141) ties exactly to company memory's ~Rs 6.5 Cr anchor.
- **LBF4 (AMW exceptional gain)**: PARTIALLY SETTLED, NEW EVIDENCE, NEW UNRESOLVED TENSION. AMW Autocomponent Ltd (AACL) is confirmed a 100% wholly-owned subsidiary, no material subsidiary under SEBI LODR thresholds (Board's Report, AR p.23). The standalone CARO Annexure (AR p.134-136) discloses a Rs 141.42 Cr loan from SSWL to AMW repayable on demand (Rs 14,141.53 lakh) — this reconciles almost exactly with Stage 2 Finding 8's Note 41 figures (Rs 133.15 Cr principal + Rs 8.27 Cr FY26 accrued interest = Rs 141.42 Cr), a clean cross-check. The CARO Annexure also confirms a Rs 100 Cr HDFC Bank term loan raised specifically for "Acquisition of AMW Autocomponent Ltd," dated FY2023-24 (AR p.136), corroborating Stage 2 Pattern Finding 3. **New in this pass**: the consolidated auditor's report "Other Matters" paragraph (AR p.185) states AMW's total assets as Rs 2,020.10 lakh (Rs 20.20 Cr), total comprehensive loss Rs (1,188.15) lakh, net cash flow Rs (215.00) lakh for FY26 — this Rs 20.20 Cr total-assets figure is arithmetically hard to reconcile with Stage 2's AOC-1 net-asset figure of Rs 75.98 Cr (net worth cannot exceed total assets), so AMW's true balance sheet size stays **unresolved across the AR's own documents**, not merely under-disclosed. **New in this pass**: the consolidated Annexure A to the auditor's report (AR p.188) discloses that AMW's own CARO report carries an **unfavourable/adverse remark under clause (i)(c)** — title deeds of immovable property not held in the company's name — which is the AR's own auditor confirming, as a formal adverse CARO finding (not just a notes disclosure), the AACL land-title gap Stage 2 flagged (Pattern Finding 2, Note 3 consol AR p.212, the AMWL demerger land).

---

## PHASE 1: AUDITOR'S REPORT & CARO

**1A Core opinion.** Both standalone (AR p.130-133) and consolidated (AR p.183-187) opinions are unmodified/unqualified ("true and fair view", no qualifications, no emphasis of matter, no going-concern paragraph). Auditor: AKR & Associates, Chartered Accountants (FRN 021179N), partner Kailash Kumar. Standalone audit report dated 29.05.2026; AR itself (Board's Report, Notice) dated/signed 03.09.2026.

**1B Key Audit Matters.** Both auditor's reports state verbatim: "We have determined that there are no key audit matters to be communicated in our report" (AR p.130, standalone; AR p.183, consolidated). 🔴 This is unusual for a listed manufacturer with the judgment-heavy areas Stage 2 found (a Rs 364.52 Cr unexplained FY26 reserve transfer, a Rs 59.31 Cr DTA against a loss-making subsidiary, a Rs 32.42 Cr FX options MTM loss, an unresolved impairment cross-reference). No revenue recognition, impairment, provisioning, or fair-value KAM is named because none was determined to exist — a process observation (Stage 2 Finding 13/Pattern Finding 4), not itself proof of an audit-quality failure, but a gap this report does not treat as closed.

**1C Emphasis of Matter / Other Matters.** No Emphasis of Matter in either report. Consolidated report carries an Other Matters paragraph (AR p.185): AMW's financials (subsidiary, audited by AKR & Associates itself, not a different auditor) and CMAPL's financials (associate, audited by an **other auditor**, relied upon) are both disclosed with AMW's total assets/loss/cash-flow figures reproduced above under LBF4.

**1D CARO 2020, clause by clause (standalone, AR p.134-137):**

| Clause | Finding | Amount | Rating |
|---|---|---|---|
| i(a)-(e) PPE/title deeds | Clean; no benami proceedings; PPE not revalued | — | 🟢 |
| ii Inventory verification | Physically verified at reasonable intervals; no discrepancy >10% of any class | — | 🟢 |
| iii Loans to related parties | Rs 14,141.53 lakh (Rs 141.42 Cr) loan to AMW, repayable on demand, no fixed term; interest demanded "in part" and paid; **principal not demanded during the year**; no overdue >90 days | Rs 141.42 Cr | 🟡 Watch — an unsecured, indefinite-term related-party loan the company chooses not to call, to a subsidiary running consecutive losses (Stage 2 Finding 6, DTA concern) |
| vii(a) Undisputed statutory dues | Regular; none outstanding >6 months | — | 🟢 |
| vii(b) Disputed statutory dues | 12 line items across Central Excise, Customs, GST; total Rs 2,611.09 lakh (Rs 26.11 Cr) disputed, largest single item GST tax/interest/penalty Rs 2,285.06 lakh (Rs 22.85 Cr, FY2017-18, pending in High Court) | Rs 26.11 Cr = 1.5% of standalone net worth (Rs 1,734.79 Cr), ~12.9% of standalone PAT (Rs 202.09 Cr) | 🟡 Watch — below the 25%/100% flag thresholds but the single Rs 22.85 Cr High Court GST matter is worth naming |
| ix(a)-(d) Borrowing defaults | No default; not a wilful defaulter; term loan proceeds applied for stated purpose; no short-term-for-long-term diversion | — | 🟢 |
| ix(e) Funds taken to meet subsidiary obligations | Rs 10,000.00 lakh (Rs 100.00 Cr) HDFC Bank term loan, fund utilisation "Acquisition of AMW Autocomponent Ltd," remark "Related to FY 2023-24" | Rs 100 Cr | 🟢 informational — quantifies part of LBF4's financing, corroborates Stage 2 Pattern Finding 3 |
| xi Fraud | No instance of fraud by or on the Company; no whistleblower complaints received during the year | — | 🟢 |
| xvii Cash losses | No cash losses in the current or immediately preceding year | — | 🟢 (clean; adverse-cash-flow flag does not trigger on this clause) |
| xx Unspent CSR | No unspent CSR amounts (over-spent, see Phase 5) | — | 🟢 |
| **Consolidated Annexure A (xxi)** | AMW Autocomponent Ltd (subsidiary) carries an **unfavourable/adverse remark in its own CARO report, clause (i)(c)** — title deeds not held in the company's name | — | 🔴 Red Flag — this is the AR's own auditor confirming, as a formal adverse finding (not a notes disclosure), the AACL/AMWL demerger land-title gap Stage 2 flagged |

**1E Auditor continuity.** AKR & Associates re-appointed at the 36th AGM (30.09.2022) for a **second consecutive 5-year term**, running to the conclusion of the 41st AGM (2027) (Board's Report, AR p.29). This is their final year of eligibility before mandatory rotation under Companies Act, 2013 Section 139(2) — FY27 will be the last audit of this tenure. Fees paid FY26 (AR p.71, consolidated basis incl. subsidiary): Statutory Audit Fee Rs 9.00 lakh, Tax Audit Fee Rs 3.00 lakh, Certificate charges Rs 3.35 lakh (of which Rs 1.35 lakh is a DVA certification under the PLI scheme). Non-audit fees (Rs 6.35 lakh) do NOT exceed the audit fee (Rs 9.00 lakh) — no flag under the protocol's threshold, though the ratio (0.71x) is not trivial.

**1F Standalone vs consolidated differences.** The consolidated opinion is unmodified despite (i) the AMW subsidiary adverse CARO clause above, and (ii) reliance on another auditor's work for the CMAPL associate (both reports' Other Matters paragraphs, AR p.185/11750). No extra qualification appears at the consolidated level beyond the CARO Annexure A disclosure. IFC (internal financial controls) opinion is unmodified and effective at both standalone and consolidated levels (Annexure B, AR p.138 and AR p.189).

**Phase 1 summary:** 🟡 Watch overall. Clean opinion, clean going-concern, no fraud, no wilful-default, no material adverse CARO clause at the standalone (parent) level. But zero KAM against a backdrop of genuinely judgment-heavy notes, an adverse CARO clause at the subsidiary carrying the AR's largest unexplained transactions, and an unsecured, un-demanded Rs 141 Cr related-party loan to a loss-making subsidiary together keep this from a clean 🟢.
**Kill switch (informational):** A human reviewer would NOT stop the run on Phase 1 alone — nothing here is a hard audit qualification — but would flag the AMW cluster (adverse CARO + zero KAM + unresolved AOC-1/auditor total-assets tension) as the single item most worth a direct management question before Halt 1.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the special instruction, this phase reuses Stage 2's triple pass rather than re-extracting. **Verification of the Top 15 findings**, checked independently against the primary statements and CARO Annexure read in Phase 1 and Phase 3 below:

| Rank | Finding | Verification |
|---|---|---|
| 1 | Rs 674.68 Cr FY25 + Rs 364.52 Cr FY26 unexplained reserve transfers | ✓ verified — consistent with the Statement of Changes in Equity opening balances read in Phase 3 (Other Equity FY24 close Rs 1,32,998.20 lakh standalone vs the much larger consolidated equity base; the transfers are consolidation-only, standalone Other Equity AR p.139 shows no equivalent unexplained line) |
| 3 (Capital Revaluation Reserve) | Consolidation-only, Rs 34.84 Cr gap | ✓ verified indirectly — not separately re-derived but no contradicting evidence found in Phase 1/3 reads |
| 4 (Supplier Finance Arrangement) | Rs 676.50 Cr, 67.6% of payables | ✓ verified and SHARPENED — Phase 3's cash flow read shows the Rs 24,969.70 lakh FY26 payables increase is the single largest working-capital cash source, consistent with this mechanism propping up CFO |
| 6 (AMW DTA/losses) | Rs 59.31 Cr DTA against 3 years of AMW losses | ✓ verified and SHARPENED — Phase 1's CARO read adds the unsecured Rs 141.42 Cr related-party loan context; Phase 1's Annexure A read adds the adverse CARO clause context |
| 7 (AACL land title) | Not registered in AACL's name | ✓ CONFIRMED AS A FORMAL ADVERSE CARO FINDING (see Phase 1D) — elevates from 🟡 Watch to a harder-edged finding, though materiality (no carrying value/duration disclosed) is unchanged |
| 9 (Working capital deterioration) | Receivables +25.2%, inventory +28.2%, payable days rising | ✓ verified and SHARPENED — Phase 3's cash flow statement shows this converting directly into a 36% CFO decline, the single most consequential number in this AR |
| 13 (Zero KAM) | Both reports carry zero KAM | ✓ verified verbatim (Phase 1B) |
| 15 (AOC-1 vs Note 53 net-asset gap; HDFC loan) | Rs 5.37 Cr gap; Rs 100 Cr HDFC loan | ✓ HDFC loan verified verbatim in CARO (Phase 1D); the AOC-1 net-asset gap is now compounded by a THIRD inconsistent AMW balance-sheet-size figure (auditor's Rs 20.20 Cr total assets, Phase 1F) — worth escalating from 🟡 to a named open item for Halt 1 |

No discrepancies found between the triple-pass values and the primary-document values checked in this pass (`discrepancies: []`). `verified: 8` of 15 directly cross-checked in this pass; the remainder (2, 5, 8, 10, 11, 12, 14) are accepted on the triple-pass's own documentation without independent re-verification here, consistent with the special instruction.

**2A Accounting policy aggressiveness.** No change from Stage 2's read: revenue recognition conservative (point-in-time on delivery), no capitalisation-threshold changes, ECL matrix flat despite 25% receivables growth (a genuine watch item this pass corroborates — see Phase 3B receivables discussion). **2B RPT map, extended**: the BRSR "Openness of Business" table (AR p.94-95) independently corroborates Stage 2's RPT read — purchases from related parties 0.16% of total purchases (down from 0.28%), sales to related parties 0.00% (both years), loans/advances to related parties 0.00%. This is a clean, small-quantum RPT profile at the transactional level; it does not touch the Rs 141.42 Cr AMW loan (which BRSR's "loans & advances" line evidently excludes or nets against total loan base differently — worth a direct question, not itself a contradiction given BRSR and Ind AS 24 use different scopes). **2C Contingent liabilities, extended**: the CARO disputed-statutory-dues table (Phase 1D) totals Rs 26.11 Cr, 1.5% of net worth and ~12.9% of PAT — below both the >25% and >100% flag thresholds. **2D Receivables, extended**: standalone trade receivables Rs 60,895.74 lakh (FY26) vs Rs 48,637.38 lakh (FY25), +25.2%, against revenue growth of 16.93% — receivables growing faster than revenue, consistent with Stage 2 Finding 9 and now directly visible as a cash drag in the Phase 3 cash flow statement. **2F Borrowings, extended**: standalone current borrowings Rs 54,996.94 lakh + non-current Rs 27,593.18 lakh = Rs 826 Cr total; broadly flat vs FY25 (Rs 548.81 Cr + Rs 278.62 Cr = Rs 827 Cr), confirming Stage 2's "FY26 Net Debt/EBITDA improvement is an EBITDA effect, not deleveraging."

**Phase 2 summary:** 🔴 Red Flag overall, unchanged from Stage 2's 4/10 accounting-quality score (Stage 2 Section B) — this pass finds no reason to revise it and one reason (the adverse CARO clause) to hold it firmly rather than soften it. Reconciled: this Stage's independent reads agree with Stage 2's verdict; no disagreement to explain.
**Kill switch (informational):** unchanged from Stage 2 — the AMW cluster remains the single largest unresolved transparency gap, now with a formal adverse CARO finding attached; a human reviewer would want this closed via the FY25 AR or a direct management question before treating any AMW-linked equity or ROE/ROCE figure as clean.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow first, then balance sheet, then P&L)

**3A Cash flow (standalone, AR p.141; all Rs lakh unless noted).**

| Metric | FY26 | FY25 | Change |
|---|---|---|---|
| PAT | 20,208.73 | 20,995.01 | -3.75% |
| CFO | 33,115.53 | 51,760.29 | **-36.0%** |
| CFO/PAT | 1.64x | 2.47x | down sharply but still >0.7 (no flag on the ratio's own threshold) |
| EBITDA (Board's Report) | 52,295.60 | 50,025.36 | +4.54% |
| CFO/EBITDA | 63.3% | 103.5% | **-40.2pp — the single sharpest quality signal in this AR** |
| Capex (purchase of fixed assets) | 20,820.97 | 21,225.88 | -1.9% |
| Capex/Depreciation | 1.62x | 2.10x | capex intensity easing as Mehsana CWIP comes out of construction (consistent with Stage 2) |
| FCF (CFO - capex) | 12,294.56 | 30,534.41 | **-59.7%** |
| Financing net flow | (14,410.72) | (35,367.29) | smaller net outflow FY26 (new Rs 13,175.00 lakh long-term borrowing drawn) |
| Year-end cash & equivalents | 652.14 | 306.63 | +112.7% off a very thin base (ties to LBF3 anchor) |

CFO quality checks: the FY26 decline is entirely a working-capital story, not a one-time inflator — inventory build (-Rs 20,939.37 lakh cash) and receivables build (-Rs 12,264.75 lakh cash) are only partly offset by the Rs 24,969.70 lakh payables increase, which Stage 2 identifies as substantially the Supplier Finance Arrangement (Note 25) rather than organic vendor credit. No unusual interest-classification choice is visible (finance charges shown gross in both operating add-back and financing outflow, standard indirect-method treatment). No M&A spend in FY26 (Rs 693.10 lakh FY25 was the AMW-related associate/subsidiary investment, now nil). **FLAG-CASH warranted.**

**3B Balance sheet (standalone, AR p.139-140).**

| | FY26 | FY25 |
|---|---|---|
| Total Assets | 3,81,676.32 | 3,36,542.48 |
| Total Equity | 1,73,478.67 | 1,54,378.40 |
| Non-current borrowings | 27,593.18 | 27,862.15 |
| Current borrowings | 54,996.94 | 54,881.22 |
| Total borrowings | 82,590.12 | 82,743.37 |
| Trade payables (total) | 1,00,177.23 | 75,207.53 |
| Trade receivables | 60,895.74 | 48,637.38 |
| Inventories | 95,252.71 | 74,313.34 |

Key ratios (AR MD&A table, AR p.122, standalone, unless noted computed): Current Ratio 1.17 (FY25 1.11); Debt/Equity 0.16 (FY25 0.19); Interest Coverage 2.11x (FY25 1.92x) — thin for an unmodified-opinion issuer but improving; Debtors Turnover 32.80 days (FY25 30.89); Inventory Turnover 59.71 days (FY25 59.34). **ROCE (computed, not disclosed in the AR)**: EBIT (PBT+finance costs) Rs 39,416.68 lakh / Capital Employed (Total Assets - Current Liabilities) Rs 2,19,420.20 lakh = **17.96%** FY26, vs Rs 39,924.48 lakh / Rs 2,00,161.97 lakh = **19.95%** FY25 — a genuine ~2pp ROCE compression, consistent with the margin story. Goodwill: none on the standalone or consolidated balance sheet (confirmed by Stage 2). **DuPont (computed)**: ROE FY26 12.01% (AR-disclosed, AR p.122) ≈ Net margin 3.90% x Asset turnover ~1.44x x Equity multiplier ~2.19x — the ROE decline (13.60% -> 12.01%) is **margin-driven, not leverage-driven** (D/E actually fell FY25-FY26); leverage is not propping up returns here.

**3C P&L (standalone, AR p.140).**

| | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue from operations | 5,18,280.25 | 4,42,899.83 | +16.93% |
| Cost of materials consumed | 3,46,317.75 | 2,87,808.68 | +20.33% (outpacing revenue) |
| Cost of materials / Revenue | 66.83% | 65.00% | +1.83pp — raw material cost eating margin |
| Employee benefit expense | 42,979.86 | 37,980.03 | +13.2% |
| Finance costs | 12,321.67 | 11,723.11 | +5.1% |
| Depreciation | 12,878.92 | 10,100.88 | +27.5% (Mehsana capex coming out of CWIP) |
| Other income | 1,187.06 | 1,343.91 | -11.7%; 4.4% of PBT (below the >20% flag) |
| PBT | 27,095.01 | 28,201.37 | -3.92% |
| PAT | 20,208.73 | 20,995.01 | -3.75% |
| Basic EPS | 12.86 | 13.38 | -3.9% |
| Diluted EPS | 12.82 | 13.32 | -3.7% (basic/diluted gap 0.3%, immaterial ESOP dilution) |

No exceptional items in either year (standalone). Tax rate: current tax + deferred tax + prior-year adjustment on PBT = (6,516.00+362.27+8.01)/27,095.01 = 25.4% FY26 vs (6,602.85+606.20-2.69)/28,201.37 = 25.5% FY25 — stable, no anomaly. The revenue-to-PAT waterfall shows the margin compression concentrated in cost of materials (raw-steel/aluminium cost pass-through lag or mix effect) and depreciation, not in a one-off or in other income manipulation.

**Phase 3 summary:** 🟡 Watch, tipping toward 🔴 on the CFO/EBITDA line specifically. Balance sheet and P&L mechanics are clean and internally consistent (no restatement, no goodwill, low leverage, stable tax rate). The cash flow statement is where this AR's single most decision-relevant number sits: a 36% CFO decline against EBITDA growth, driven by working-capital build that a debt-like receivables/payables financing arrangement is partly masking on the payables side.
**Kill switch (informational):** A human reviewer would want the FY27 Q1 cash conversion trend (results filings, outside this AR) before treating FY26 as a one-year working-capital blip vs the start of a structural cash-conversion problem tied to the alloy/knuckle mix shift's higher input-cost and inventory intensity.

---

## PHASE 4: RISK FACTORS & MD&A

**4A Disclosed risks, real vs boilerplate (Risk table, AR p.123-126).** Nine risk types disclosed (Global Economic Scenario, Capacity Expansion Dependence, Supply Chain, Employee Retention, Competition, Climate/Environment, Water Security, Energy Management, Currency Volatility, Debt Burden, Credit Rating, Social Costs/Actuarial, Credit Risk, Financial Fraud, Ethics/Compliance, Health & Safety, Cyber Security). Assessment: **mostly boilerplate**. Every mitigation is phrased in generic terms ("robust systems", "close monitoring", "continuous effort") with **no quantified thresholds, no named single-customer or single-supplier concentration percentage, and no company-specific numeric target** anywhere in the risk table itself. The one real, specific figure in the entire section sits outside the risk table proper, in the Outlook paragraph: "85% of revenues come from domestic market customers" (AR p.124) — a genuine, specific customer/geography-concentration disclosure, but not tied to a named customer or a mitigation with a measurable target.

**4B MISSING RISKS**, evident from Phases 1-3 but absent from the risk section:

1. **The reverse-factoring / Supplier Finance Arrangement (Note 25, Rs 676.50 Cr, 67.6% of payables)** — the mechanism directly propping up FY26's payables growth and masking part of the CFO decline — is never named as a risk anywhere in the MD&A or risk table, despite "Debt Burden" being an explicitly disclosed risk category. Likely reason for omission: the arrangement is structured and presented as a payables item, not a borrowing, so it falls outside management's own definition of "debt" even though Stage 2 treats it as debt-like.
2. **The Customs show-cause notice** dated 17-Jun-2026 (Principal Commissioner of Customs, Mundra; disclosed separately via Reg 30 filing, per Stage 0 filings_of_note) **is not mentioned anywhere in this AR**, despite the AR being signed 03.09.2026 — after the notice was issued. Verified by full-text search: "show cause", "Customs" (beyond the boilerplate CARO reference to "duty of customs" as a statutory-dues category), and "Mundra" all return no matching disclosure in contingent liabilities, subsequent events, litigation ("no pending litigations which would impact its financial position", CARO/audit report, AR p.132/8187), or the Board's Report's "material orders" section ("no significant and material orders... impacting the going concern status", AR p.29). This is a genuine silence: a live regulatory matter, disclosed to the exchanges, absent from the Annual Report.
3. **The AMW loss/DTA/adverse-CARO cluster** is not named in the risk table at all — "Debt Burden" and "Credit Risk" both discuss the parent's own position but neither mentions the subsidiary's three consecutive loss years or the un-demanded Rs 141.42 Cr related-party loan.
4. **Raw material import/currency exposure specifics** — the risk table names "Currency Volatility" generically, but the Outlook paragraph's own admission that "the Company imports some of the raw material and that impacts the profitability due to adverse currency movement" (AR p.124) is not accompanied by any % import-dependency figure, and the widening FX outgo-over-inflow gap (Annexure IV: outgo Rs 72,302.35 lakh vs inflow Rs 50,873.51 lakh FY26, a Rs 21,428.84 lakh net outflow, up from a Rs 4,172.43 lakh net outflow FY25) is disclosed only as a bare table in Annexure IV, never surfaced as a risk or discussed in the Outlook.

**4C MD&A deep dive.** Industry claims (India auto sector FY26 "landmark year", every category posting record sales, AR p.122-123) are well-sourced to SIAM data and read as credible macro context, not company-specific spin. Growth/margin explanations are largely descriptive rather than diagnostic: the Board's Report attributes the PBT/PAT decline to "increase in Depreciation and Interest Cost" (AR p.122 ROE table) — true as far as it goes (Phase 3C confirms depreciation +27.5%, finance costs +5.1%) but silent on the larger driver, the 1.83pp rise in cost-of-materials/revenue. **Forward guidance table**: no numeric guidance exists in the AR (see LBF1 discussion above); the only forward-looking numbers found are ESG/capex-adjacent: Rs 15.00 Cr earmarked FY27 renewable-energy capex (vs Rs 10.00 Cr spent FY26), ~650 lakh units of renewable electricity targeted FY27, and a "water positive" target for the Dappar plant in FY27 (AR p.44). **Segment analysis**: none exists — single Ind AS 108 segment (AR p.126), confirmed again independently in this pass and consistent with Stage 2 Finding 14; this remains the single largest evidence gap for verifying LBF2's mix-shift-margin thesis from filed documents.

**4D Tone and credibility ratings (1-5, evidence-based):**

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2/5 | No numeric guidance table; no mention of the reverse-factoring mechanism, the Customs notice, or the AMW loss/loan cluster in the risk section; MD&A margin explanation names only 2 of 3 real drivers |
| Consistency | 4/5 | The "improved sales mix" framing (Board's Report, AR p.20) is consistent with the knuckle-unit growth data disclosed elsewhere; no contradiction found between MD&A narrative and disclosed numbers, only omission |
| Specificity | 2/5 | Risk table is generic; the one specific figure (85% domestic revenue) is not tied to a mitigation target; no single-customer % anywhere |
| Accountability | 3/5 | PBT/PAT decline is stated plainly with exact percentages, not buried or reframed as a positive — credit for that — but the CFO collapse (the AR's most material single number) is never mentioned in prose anywhere outside the cash flow statement itself |
| Capital allocation sense | 3/5 | Capex directed to Bhuj alloy-wheel/knuckle capacity (stated rationale: content-per-vehicle and mix upgrade) is coherent with the stated strategy; the un-demanded Rs 141 Cr loan to a loss-making subsidiary is a soft-allocation choice not explained in capital-allocation terms anywhere in the AR |

**Phase 4 summary:** 🟡 Watch, driven mainly by the missing-risk list (4B) rather than by anything false in what is disclosed. Nothing found here contradicts Phases 1-3; the pattern is consistently one of omission (soft language, generic risk boilerplate, silence on the CFO decline and the Customs notice) rather than misstatement.
**Kill switch (informational):** A human reviewer would not stop on Phase 4 alone, but would want the Customs show-cause notice's quantum and the FY25 AR's own risk-section wording (to test whether these omissions are new this year or a standing pattern) before Halt 1.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

**5A Board composition, tenure, attendance (AR p.51-53).** Eleven directors as at 31.03.2026: 3 Executive (incl. 1 promoter-category ED), 8 Non-Executive (2 Non-Independent incl. the promoter Chairman, 6 Independent incl. 2 women). Chairman Rajinder Kumar Garg (Non-Executive, promoter) is the father of Managing Director Dheeraj Garg (disclosed inter-se relationship, AR p.52) — both promoter category. MD Dheeraj Garg personally holds 29.52% of the company (46,402,280 shares) (AR p.54), separate from the 61.14% consolidated Promoter and Promoter Group holding.

**Attendance flags (AR p.53, five Board meetings held FY26):**
- Sh. Ajit Singh Chatha (Independent Director, **Chairman of the Audit Committee**): Board 1/5 (20%), Audit Committee 2/6 (33%), NRC 3/3, SRC 1/1, ECC 1/1. **🔴 The Audit Committee Chairman attended only 1 of 5 Board meetings and 2 of 6 Audit Committee meetings — both well under the 75% threshold that triggers a flag** (protocol 5A). He also attended the previous AGM per the report's own text (AR p.55) despite the poor meeting attendance, and is aged over 75 (re-appointed "notwithstanding that he has attained the age of seventy-five (75) years", AR p.65 CSR/board annexes).
- Sh. Siddharth Bansal (Independent Director): Board 1/5 (20%), Audit Committee 2/6 (33%). **🔴 Also under 75%.**
- Smt. Deva Bharathi Reddy (Independent Director): Board 2/5 (40%). **🔴 Under 75%.**
- Sh. Sanjay Surajprakash Sahni (Tata Steel nominee, ceased 18.03.2026): Board 3/5 (60%) before resignation — below 75% but role ended mid-year, context noted.

No independent director exceeds 10 years of continuous tenure per the disclosed appointment dates (Virander Kumar Arya's second three-year term runs to 30.09.2026, the longest-serving; his tenure since original appointment is not fully stated in this AR, but nothing in the disclosed dates crosses the statutory 10-year cap). No director holds >7 listed directorships or >5 committee chairmanships (Regulation 17A/26(1)(b) confirmed compliant, AR p.51-52). Promoter-family cross-board memberships are extensive but disclosed: Chairman Rajinder Kumar Garg is also MD of Indian Acrylics Ltd and Chairperson of SAB Industries Ltd and Steel Strips Infrastructures Ltd (all promoter-group companies); Sanjay Garg (Non-Executive Non-Independent Director of SSWL) holds Executive/Managing Director roles at SAB Industries and Steel Strips Infrastructures — a tight promoter-group web, fully disclosed, not itself a flag under the >8-seats threshold but worth naming for downstream governance/promoter-verdict work (Stage 8).

**5B Committee analysis.** Nine Board committees (Audit, NRC, Stakeholders Relationship, CSRS, Risk Management, Employee Compensation, Share Transfer, Finance, Allotment). Audit Committee met 6 times FY26 (AR p.57-58); Risk Management Committee met only **2 times** FY26 (09.05.2025, 28.11.2025, AR p.65) — a 210-day gap between the two, at the outer edge of what the Committee's own terms of reference imply for an active oversight body, though within the regulatory limit named in the report. RMC's FY26 members included the outgoing CFO (Naveen Sorot, up to 12.09.2025) with no replacement CFO member until the new CFO's later appointment — a coverage gap during the CFO transition (Nov 2025).

**5C Compensation.** MD Dheeraj Garg total remuneration FY26: Rs 1,329.47 lakh (Rs 13.29 Cr), of which Rs 791.87 lakh is commission at 5% of net profit under Section 198 (AR p.61). **Ratio to median employee remuneration: 267.69x** (AR p.50) — a very high CEO-to-median multiple, though the % increase in MD remuneration was actually -3.08% YoY (falling PAT reduces the commission component mechanically). Average employee remuneration increase 9.10% vs 8.85% for KMP — KMP increase is LOWER than the broader workforce, a genuinely favourable data point on pay equity that the report states plainly (AR p.61). No promoter-family payroll beyond the disclosed MD/Chairman roles; ESOP dilution is immaterial (basic/diluted EPS gap 0.3%, Phase 3C).

**5D Shareholding.** Promoter and Promoter Group: 61.14% as at 31.03.2026 (AR p.72), matching Stage 0's June-2026 shareholding pattern exactly. No pledge disclosed anywhere in this AR or in the June-2026 SHP (Stage 0). Directors and relatives hold a further 0.17%. Mutual Funds/AIF/Insurance 5.08%; FDI/FPI 8.22% — combined institutional ownership ~13.3%, modest but present. Per Stage 0's filings_of_note, a promoter-group open-market **purchase** (not sale) occurred 15.09.2026 (Sunena Garg, 16,600 shares, promoter group 61.14% -> 61.15%) — an insider-confidence-positive signal, the opposite of the "promoter selling against a growth narrative" pattern the protocol asks to flag.

**5E Governance red-flag checklist.** Whistleblower: zero complaints reported FY26 (AR p.75). SEBI/regulatory actions: none against the company, promoters, directors, or subsidiaries in the last 3 years (AR p.74). RPT committee (Audit Committee) function: all RPTs reviewed/approved, omnibus approval granted, AOC-2 shows NIL material RPTs (AR p.42-43) — consistent with the BRSR's small RPT percentages (Phase 2). Auditor fee ratio: non-audit (Rs 6.35 lakh) does not exceed audit (Rs 9.00 lakh) — no flag. CSR compliance: FY26 spend Rs 6,34,95,050 against a Rs 4,74,29,346.46 obligation — **over-spent** by Rs 1,60,65,703.54, carried forward as a set-off credit (AR p.44-45); fully compliant, no unspent-CSR flag (CARO xx also clean). Section 143 fraud: none reported by the statutory, secretarial, or internal auditors (AR p.29, CARO xi). Material subsidiary auditor: AMW is audited by the **same** statutory auditor (AKR & Associates) as the parent, per the Corporate Governance Report's auditor-fee disclosure (AR p.71, "fees...paid by the company and its subsidiary...to the Statutory Auditors"); only the CMAPL associate uses a different (unnamed in this AR) auditor.

**Phase 5 summary:** 🟡 Watch. The single sharpest governance finding is the Audit Committee Chairman's own attendance record (20% Board, 33% AC) — a real, quantified, threshold-breaching flag, not a boilerplate one. Everything else (promoter web, high CEO-to-median ratio, RMC meeting cadence) is disclosed and within regulatory bounds but worth naming for the promoter/governance verdict (Stage 8).
**Kill switch (informational):** A human reviewer would want to understand why the Audit Committee Chairman — the officer named as the direct whistleblower escalation point in the Vigil Mechanism policy (AR p.28, AR p.72) — has such low attendance, given the AMW cluster's need for exactly this kind of oversight.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

This AR carries no separate glossy Chairman's letter; the Board's Report opening ("Dear Members", AR p.19) and the MD&A (AR p.119) together serve as the front-matter narrative, read here last with full knowledge of Phases 1-5.

**6A Narrative vs reality (5-7 most prominent claims):**

1. "Your Company performed satisfactorily and effectively managed its operations, supported by an improved sales mix" (AR p.20). ❓ Partially supported: revenue +16.93% and knuckle units +448% support "improved sales mix" in volume terms, but standalone operating margin fell 9.01%->7.61% and PAT fell 3.75% — "satisfactorily" understates a year of margin compression. Mixed verdict, not a clean ✅ or ❌.
2. "The Profit before Tax...has slightly decreased...marking a decline of 3.92%" (AR p.20). ✅ Accurate and stated plainly, credit due — this is the one place the negative number is not softened beyond the word "slightly."
3. Bhuj alloy-wheel and knuckle-manufacturing capacity expansion (1.2m + 0.6m units/year), backed by a Tripartite Agreement with Chinese technology partners Arays/Hainan for know-how transfer (AR p.20, AR p.41-42). ✅ Real and specific — board approval dates, capacity figures, and named technology partners are all given, a genuinely well-evidenced strategic claim (unusually specific for this AR).
4. "SSWL is already taking steps to indigenize the imported raw material...de-risking the business model" (Corporate Governance Report, AR p.72). ❌ Not evidenced anywhere else in the AR — no % import-dependency baseline, no indigenization progress metric, and the FX outgo-over-inflow gap actually widened FY25->FY26 (Phase 4B). Claim asserted, not demonstrated.
5. "The Company continues to strive to improve its operational performance" (Risk table, competition mitigation, AR p.124) and "aggressively working on New Product Developments" (MD&A Outlook, AR p.124). ❓ Generic strategic language with no operational evidence cited in this AR (no new-product revenue, no R&D-to-product-launch linkage); R&D spend as % of turnover actually **fell** from 1.14% to 0.40% FY26 (Annexure IV, AR p.42) — the capital R&D line collapsed from Rs 3,162.87 lakh to Rs 27.45 lakh, though this is plausibly a CWIP/capitalisation reclassification tied to the Mehsana ramp coming out of construction (Stage 2), not necessarily a strategic retreat; still, the AR does not explain the drop anywhere near the "aggressively working on New Product Developments" claim.

**6B Strategic priorities.** Bhuj expansion (alloy wheels + knuckles) is the one specific, capital-backed priority (Board approval, named technology partner, stated unit-capacity numbers). Export/European diversification and customer-concentration reduction are named as priorities in the MD&A Outlook but carry **no capital allocation, no target date, and no baseline metric** anywhere in the AR.

**6C Metrics showcased vs conspicuously absent.** Showcased: revenue growth %, EBITDA growth %, wheel-rim and knuckle unit volumes, ROE, four MD&A ratios (debtors/inventory turnover, interest coverage, current ratio, D/E, margins). Conspicuously absent from the front matter and MD&A alike: CFO (never mentioned in prose anywhere in the AR outside the cash flow statement face itself), ROCE (not disclosed at all, Stage 3 had to compute it), any product-level or geography-level revenue split beyond the single "85% domestic" line, and any figure at all for the reverse-factoring arrangement's trend or utilisation against its stated limit.

**6D Tone and priority drift.** Not inferable year-over-year from this single AR (no FY25 AR in corpus to compare Chairman/MD&A tone against). Within FY26 itself, the tone across Board's Report, MD&A, and Corporate Governance Report is uniformly measured and non-triumphalist even when reporting the PAT decline — the "slightly decreased" language is the most editorializing the AR gets, which is comparatively restrained rather than promotional.

**6E Quiet Abandonment Check (mandatory).**

Two findings meet the bar:

1. **Silent drop — operating cash flow.** The opening/Board's Report and MD&A both build a narrative of "satisfactory performance" and "improved sales mix" around revenue and EBITDA growth (AR p.19-20, AR p.121-122), and the MD&A explicitly explains the PAT/ROE decline via "increase in Depreciation and Interest Cost" (AR p.122). **At no point does the Board's Report, MD&A, or any narrative section mention that operating cash flow fell 36% year-on-year** — a materially larger and more consequential number than the 3.75% PAT decline the report does choose to discuss. This is not an implicit retraction (nothing said elsewhere contradicts it) and not a hedged retreat (no soft language stands in for it) — it is a **silent drop**: the topic simply does not appear in any narrative section, only in the raw cash flow statement face that a reader must independently total and compare to EBITDA. **Materiality: HIGH** — this is LBF3's core number and the single most decision-relevant figure this AR contains; a reader relying on the Board's Report/MD&A narrative alone would not learn of it.
2. **Silent drop — the reverse-factoring/debt-like financing arrangement.** The MD&A's "Debt Burden" risk explicitly frames indebtedness in terms of "outstanding indebtedness" and "financial leverage" (AR p.125) with mitigations pointing to quarterly reviews "to move towards industry benchmark." The Rs 676.50 Cr Supplier Finance Arrangement (67.6% of trade payables, Note 25) is functionally debt-like per Stage 2's read, sits squarely within what "Debt Burden" should cover, yet is never named in that risk section, the MD&A, or the Board's Report. **Materiality: HIGH** — this arrangement is the mechanism that both flatters the current ratio/leverage ratios reported in MD&A (current ratio 1.17, D/E 0.16) and drives the FY26 cash flow story above; silence on it in the risk narrative while claiming close "monitoring of debt profile" is a real gap between the stated governance process and the disclosed content.

No implicit-retraction or hedged-retreat pattern was found beyond these two; the Bhuj capacity-expansion narrative (6A item 3) is, unusually for this AR, followed through with specific operational detail rather than abandoned.

**Phase 6 summary:** 🔴 Red Flag, driven specifically by the two silent drops in 6E — both touch load-bearing facts (LBF3) and both are HIGH materiality. The front matter is not dishonest (nothing stated is false) but its two largest omissions are also its two most consequential.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top reasons |
|---|---|---|
| **GARP** | WATCHLIST | (1) Revenue +16.93%, knuckle-unit growth +448% show real top-line/mix momentum consistent with a "growth at reasonable price" transition story; (2) but margin (EBITDA 11.01%->9.91% consolidated) and ROCE (19.95%->17.96%) are both compressing in the very year the mix-shift thesis should show margin expansion, an unresolved tension the AR itself cannot settle (no product-level P&L); (3) the CFO collapse means "earnings quality" — a core GARP input — is currently poor, even though PAT itself only fell modestly |
| **Turnaround** | WATCHLIST | (1) AMW subsidiary remains loss-making for a third consecutive year with no disclosed turnaround plan or forecast support for its Rs 59.31 Cr DTA (2) the adverse CARO clause on AMW's own land title adds a fresh, unresolved legal/administrative loose end to any "AMW turnaround" thesis (3) the parent's own performance is not itself a turnaround story — it is a mature, profitable business absorbing a genuine, current-year margin and cash-conversion setback |
| Value+Quality | WATCHLIST | Clean audit opinion, low leverage, no fraud, no goodwill — but accounting-quality score 4/10 (Stage 2) and a 36% CFO decline are quality red flags that dominate over the "value" case at this stage |
| Capex-Led Growth | WATCHLIST | Bhuj alloy/knuckle expansion is real, specific, and capital-backed (1.8m combined units/year), but the AR gives no unit-economics or payback disclosure for the new capacity |
| Cash Flow Compounder | FAIL (this year) | FCF fell 59.7% YoY on a 36% CFO decline; this is not a year that supports a cash-compounder read, whatever the multi-year trend proves to be |
| Contrarian | WATCHLIST | Margin/cash-conversion weakness this year could set up a contrarian entry if the mix-shift thesis is real and the FY26 working-capital build reverses, but the AR gives no evidence either way on reversal timing |
| Insider Confidence | PASS (weak positive) | Promoter-group open-market purchase 15.09.2026 (Stage 0), no pledge, promoter holding flat-to-rising (61.14%->61.15%) — genuinely positive, though small in size |
| Guidance Divergence | INDETERMINATE | No numeric AR guidance exists to test against delivery (see LBF1); this strategy cannot be evaluated from the AR alone |

---

## PHASE 8: FINAL VERDICT DASHBOARD

**Company snapshot.** Steel Strips Wheels Ltd, FY26 standalone revenue Rs 5,182.80 Cr (+16.93%), consolidated PAT Rs 190.22 Cr (-2.60%), 40th year of operations, 3,063 permanent employees, five manufacturing plants (Punjab, Tamil Nadu, Jharkhand x2, Gujarat) plus two new Bhuj plants under construction (Gujarat, alloy wheels + steering knuckles).

**Phase-wise verdict summary:**

| Phase | Verdict |
|---|---|
| P1 Auditor's Report & CARO | 🟡 Watch |
| P2 Notes | 🔴 Red Flag |
| P3 Financial Statements | 🟡 Watch (tipping toward 🔴 on CFO/EBITDA) |
| P4 Risk & MD&A | 🟡 Watch |
| P5 Governance | 🟡 Watch |
| P6 Chairman's Letter / Front Matter | 🔴 Red Flag |
| P7 best fit | GARP/Turnaround, both WATCHLIST |

**Overall quality score: 5/10** (governance 6/10, accounting 4/10 [Stage 2's score, reconciled unchanged], balance sheet 6/10, earnings 4/10 — weighted 25% each = (6+4+6+4)/4 = 5).

**Top 3 strengths:**
1. Clean, unmodified audit opinion at both standalone and consolidated levels; no fraud, no wilful default, no cash losses, low leverage (D/E 0.16), no goodwill anywhere on the balance sheet.
2. Real, specific, capital-backed capacity expansion into alloy wheels and aluminium steering knuckles (Bhuj, named technology partners, stated unit capacity), with knuckle unit volumes already up 448% YoY — the mix-shift thesis has genuine volume-side evidence.
3. Clean insider-confidence signal: promoter holding stable-to-rising with a recent open-market purchase, no pledge, low RPT quantum, CSR over-spent (not under-spent).

**Top 3 red flags:**
1. CFO collapsed 36% YoY (Rs 517.6 Cr -> Rs 331.2 Cr) against EBITDA growth of 4.54%, driven by working-capital build that a debt-like Rs 676.50 Cr Supplier Finance Arrangement (67.6% of payables) is partly masking — and this number appears nowhere in the AR's own narrative sections (Phase 6E silent drop).
2. The AMW cluster: three consecutive loss years, an un-demanded Rs 141.42 Cr related-party loan, a Rs 59.31 Cr DTA with no disclosed forecast support, an adverse CARO clause on land title, zero KAM despite all of the above, and THREE internally inconsistent figures for AMW's balance-sheet size across the AOC-1, Note 53, and the auditor's own Other Matters paragraph.
3. Governance attendance: the Audit Committee Chairman attended only 20% of Board meetings and 33% of Audit Committee meetings in FY26 — a real, quantified breach of the 75% attendance norm, in the one committee role most responsible for catching exactly the kind of disclosure gaps this report found.

**Key monitorables for next quarter:**

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| Q1/Q2 FY27 CFO and CFO/EBITDA | CFO/EBITDA recovering toward >80% would support a one-year blip read; staying <65% would support a structural read | Quarterly results filings, cash flow (if disclosed) or working-capital note trend | Directly resolves whether the FY26 cash-conversion collapse (LBF3) reverses or compounds |
| Supplier Finance Arrangement utilisation | Growing beyond Rs 676.50 Cr / above the Rs 400-500 Cr limit named in company memory | Quarterly borrowings/payables note, if disclosed; otherwise next AR | Tests whether the debt-like financing is stabilising or expanding |
| AMW quarterly performance and DTA | Any DTA write-down or continued losses beyond FY26 | Quarterly consolidated results, next AR AOC-1 | Tests LBF4's DTA-realism concern and the adverse-CARO land-title resolution |
| Product/segment margin disclosure | Any voluntary disclosure of alloy vs steel wheel revenue/margin split | Investor presentations, concall transcripts (Stage 5/8) | The only route to verifying LBF2's mix-shift-margin thesis, since the AR itself carries none |
| Customs show-cause notice quantum and outcome | Any resolution, provision, or escalation | Next Reg 30 filing or next AR's contingent liabilities note | Currently undisclosed in the AR despite predating its signing date |

**One-line verdict:** GARP/Turnaround WATCHLIST — real mix-shift capacity investment, but FY26 cash conversion and AMW opacity need resolution before the transition thesis is investable.

**analyst_note (context for downstream stages, not a finding):** Three separate figures for AMW's balance-sheet size appear across this single AR (AOC-1 Rs 75.98 Cr net worth; consolidated Note 53 Rs 70.61 Cr net worth; auditor's Other Matters Rs 20.20 Cr total assets) and cannot be reconciled from the document itself — net worth exceeding total assets is arithmetically impossible, so at least one of these numbers is either mislabelled in the AR or reflects a scope difference (e.g., a different reporting date or a partial consolidation adjustment) that the AR does not explain. Stage 5/8 should not compute any AMW-attributable ROE/ROCE contribution from these figures without first resolving which one is right.
