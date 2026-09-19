# Stage 3 — Annual Report Deep Dive, Backward Read
eMudhra Ltd (EMUDHRA) | run_date 2026-09-19 | FY2025-26 Annual Report, 369 pages
Source: inputs/annual-report/Annual_Report_2026.txt (pdftotext -layout, [page N] = PDF page) cross-checked against inputs/annual-report/Annual_Report_2026.mupdf.txt for scrambled tables (financial statements, pp.212-220). No raster PNGs were needed beyond the mupdf cross-check; pp.195-300 renders exist at work/raster/AR2026/ if a verifier needs them.
Units: AR states "All amounts are in INR million, unless otherwise stated." Every figure below states the Mn value first per source; Cr shown in prose only for readability (Rs 1 Cr = INR 10 Mn).

Protocol v1.3. All eight phases executed in one pass, backward read (auditor's report and CARO first, chairman's letter last per protocol, though this write-up follows the standard phase order for readability — content order follows the protocol's reading order).

---

## LOAD-BEARING FACTS — FIRST VERIFICATION PRIORITY (checked before phase work)

1. **ORGANIC GROWTH vs GUIDANCE.** Confirmed by B02 (Note 4a(c)/(d), consol p.243): Cryptas and AI Cyberforge both consolidated from 1-Jul-2025, so FY26 carries ~9 months. The AR does NOT isolate a standalone Cryptas revenue figure — the segment note (Note 49) reports only "Enterprise Solutions Outside India" Rs 4,375.72 Mn (+38.3% YoY, 62.4% of FY26 revenue). MD&A (p.148) states international revenue grew 38.7% for the year and existing-customer share of business is 67%. FY27 numeric guidance (organic 15-18%, PAT +25-30%) is NOT FOUND IN THIS DOCUMENT — it is a concall disclosure (company memory only); the AR's own "Looking Ahead" section (p.51) is qualitative, naming initiatives (PQ readiness, Agentic AI trust, Europe, US FedRAMP, partner ecosystem) with no numeric targets.
2. **CASH CONVERSION.** Confirmed directly from the audited consolidated cash flow statement (p.216-219): CFO Rs 1,328.49 Mn (FY26) vs Rs 1,016.16 Mn (FY25); capex (PPE + intangibles, one combined line) Rs 1,853.68 Mn (FY26) vs Rs 832.02 Mn (FY25); FCF = CFO − capex = **Rs -525.19 Mn (Rs -52.5 Cr)**, matching the screener figure of Rs -52 Cr almost exactly. Separately, "Payment towards acquisition of business (net of assets acquired)" is its own investing-activities line, Rs 629.03 Mn (FY26) vs Rs 743.23 Mn (FY25) — this is NOT part of the capex line above. The B01 claim of "+Rs 51.4 Cr FCF (acquisitions excluded)" does not reconcile to any single combination of these AR lines that we could construct (CFO minus capex alone gives -52.5 Cr; CFO minus organic capex only, backing out the Rs 558.90 Mn acquisition-related intangible additions per B02 finding 4, gives roughly +Rs 3.4 Cr, still short of +51.4 Cr). **The AR's own combined capex line already includes the acquisition-related organic and inorganic intangible additions together; the screener -Rs 52 Cr figure is the one that ties cleanly to the audited cash flow statement.** B01's +51.4 Cr number cannot be reproduced from the face financial statements as read here; flagged for B01/verifier reconciliation. MD&A's separate "Total Cash and cash equivalents" figure of Rs 1,268.48 Mn (p.152) is a broader liquidity measure (Balance Sheet cash Rs 582.33 Mn + liquid investments/FDs >3 months Rs 686.15 Mn) — not a contradiction once the MD&A's own table (p.152) is read in full.
3. **3i INFOTECH CLAIM.** Confirmed via B02 (Note 36(f) consol p.265, Note 38(e) standalone p.353): full chronology on file (complaint 4-Feb-2026, denial same day, exchange 11-Feb-2026, eMudhra legal notice 23-Apr-2026, no response "until date"). Claim "more than Rs 128 Crores plus interest and damages," excluded from the quantified contingent-liability total (which stood at Rs 34.55 Mn / Rs 32.29 Mn per MD&A, entirely a separate, unrelated Income Tax matter — see Phase 1D). **The 3i Infotech claim does not appear anywhere in the MD&A's Enterprise Risk Management section (pp.153-160) or the risk factors** — a Phase 4B missing-risk finding, notable because the claim predates the AR's 6-May-2026 sign-off by three months.
4. **ASSET BUILD.** Confirmed (B02, Note 4a/2.5a): Goodwill Rs 2,940.46 Mn (FY26) vs Rs 1,254.60 Mn (FY25), Cryptas alone contributing Rs 1,315.25 Mn entirely as goodwill (net identifiable assets ~nil). Other intangible assets net Rs 2,972.98/2,988.64 Mn (mupdf: 2,988.64 Mn) vs Rs 1,780.6-1,788.06 Mn FY25. Capitalised product development (Intangible Assets Under Development) a modest Rs 105.92 Mn. Capex (PPE+intangibles) Rs 1,853.68 Mn (FY26) vs Rs 832.02 Mn (FY25). Amortisation useful life extended to 10 years effective 1-Apr-2025 (Note 5a(iii)(a)), cutting FY26 amortisation ~Rs 39.96 Mn.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A. Core Opinion

| | Consolidated | Standalone |
|---|---|---|
| Opinion type | Unmodified / unqualified, "true and fair view" (p.202) | Unmodified / unqualified (p.293) |
| Basis | Ind AS per Companies Act 2013 s.133 | Same |
| Going concern language | **NONE.** No emphasis-of-matter or material uncertainty paragraph (p.199-208) | **NONE** (p.291-299) |
| Auditor | Suri & Co., Chartered Accountants (FRN 004283S), partner V Natarajan, Membership 223118 | Same |
| Date | 6-May-2026 | 6-May-2026 |

### 1B. Key Audit Matters

| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Revenue recognition (Ind AS 115) — the SOLE KAM on both reports (consol p.202-204, standalone p.295-296) | Judgment in identifying performance obligations, transaction price allocation, timing of satisfaction (over time vs point in time), stage-of-completion for partially satisfied obligations | Auditor tested internal controls, sampled continuing and new contracts, verified allocation basis, verified judgment on satisfaction timing, verified evidence of transfer, verified stage-of-completion judgments (7-step procedure listed, p.203-204) | 🟡 Standard KAM language, procedurally described but generic; no quantified sample size or materiality threshold disclosed |

No other KAM is named. **Notably absent**: no KAM on business-combination accounting / purchase price allocation for Cryptas and AI Cyberforge (two acquisitions completed this year, combined goodwill Rs 1,431.20 Mn of the Rs 2,940.46 Mn total per B02 finding 3), and no KAM on the intangible useful-life estimate change (Note 5a(iii)(a)). Both are material, judgment-heavy, and new this year — a genuine gap between what the notes show as judgment-intensive and what the auditor chose to spotlight (also flagged in B02 finding 6).

### 1C. Emphasis of Matter and Other Matters

NONE FOUND on either report. The "Information Other than the Financial Statements" section (standard boilerplate, p.204-205/297) states the auditor has "nothing to report" on the MD&A/Board's Report/Corporate Governance Report's consistency with the financials.

### 1D. CARO 2020 — Clause by Clause (standalone Annexure B, p.303-308; consolidated report cross-refers to the same clause set at p.208-209 and confirms "no qualifications or adverse remarks... except in respect of clause vii(a)")

| Clause | Finding |
|---|---|
| i (PPE/Intangibles) | Clean. Proper records, physical verification done, no material discrepancies, no revaluation, no Benami proceedings. |
| ii (inventory verification) | Clean. Physical verification carried out, no discrepancies ≥10% in aggregate. ii(b) not applicable — no working capital limits ≥Rs 5 Cr sanctioned against current assets. |
| **iii (loans to related parties)** | **Not applicable** — company has NOT granted any loans, advances, guarantees or security to any party during the year. No repayment-reality issue arises because none exist. |
| iv (Sec. 185/186 compliance) | Not applicable — no loans, guarantees or security given. |
| v (deposits) | Not applicable — no deposits accepted. |
| **vii (statutory dues)** | **QUALIFIED — the sole CARO exception.** vii(a): four small undisputed PF arrears >6 months: Rs 0.02 Mn (Apr-Aug 2025), Rs 0.09 Mn (FY24-25), Rs 0.05 Mn (FY23-24), Rs 0.05 Mn (FY22-23) — all still "Not paid" as of report date, a persistent multi-year pattern (p.304-305, table reproduced). vii(b) disputed dues: one Income Tax matter, AY 2012-13, Rs 32.29 Mn, pending before the Deputy Commissioner of Income Tax / Karnataka High Court writ petition (p.305) — this is the entire quantified contingent-liability balance referenced in MD&A (Rs 32.29 Mn), and is UNRELATED to the 3i Infotech claim. |
| viii (undisclosed income) | Clean — no surrendered/disclosed income in tax assessments. |
| **ix (borrowing defaults)** | Not applicable — company had NO outstanding loans/borrowings from FIs, banks, government, or debenture holders as of the audit date (standalone). Note the consolidated Balance Sheet does show group borrowings of Rs 238.73 Mn (Note 16) — these sit at overseas subsidiaries, not at the standalone Indian entity CARO covers. |
| x (IPO/preferential issue) | Not applicable — no fundraise during the year. |
| **xi (fraud)** | **Clean.** xi(a): no fraud by or on the Company noticed or reported. xi(b): no ADT-4 filed. xi(c): no whistleblower complaints received during the year or up to report date, per management representation. |
| xii (Nidhi) | Not applicable. |
| xiii (RPT compliance, Sec. 177/188) | Compliant, disclosed per applicable standards. |
| xiv (internal audit) | Adequate internal audit system in place (CNGSN & Associates LLP), reports considered in audit planning. |
| xv (non-cash transactions with directors, Sec. 192) | Not applicable — none entered into. |
| xvi (RBI registration) | Not applicable — not an NBFC, no core investment company in the group. |
| **xvii (adverse cash flows / cash losses)** | **Clean.** No cash losses in the current year or the immediately preceding year. |
| xviii (auditor resignation) | None during the year. |
| xix (going concern per financial ratios) | Clean — nothing indicating inability to meet liabilities falling due within 12 months, with standard disclaimer that this is not a guarantee of future viability. |
| **xx (unspent CSR)** | **Not applicable — clean.** No unspent CSR amount; Rs 6.48 Mn spent against a Rs 3.09 Mn obligation (over-spent by Rs 3.39 Mn), consistent with B02's "CSR over-spent both years" finding. |

**Overall CARO read**: the only qualification across 20 clauses is a small, persistent (multi-year) PF-arrears item (vii(a)) — same character as the frozen MSME payables red flag from B02 (Note 40/43), suggesting a pattern of small statutory items that simply do not get resolved rather than one-off oversights.

### 1E. Auditor Continuity

Suri & Co. appointed at the 14th AGM (2022) for a first five-year term, to the conclusion of the 19th AGM (2027) (Board's Report §30(a), p.97). FY26 is Year 4 of the first term — no rotation issue yet (mandatory rotation for a firm applies at 10 years for this company class; individual partner rotation rules do not appear breached). Statutory Auditor's Report contains no qualification, reservation, adverse remark or disclaimer; no Section 143(12) fraud report filed.

**Audit vs non-audit fee — FLAG.** Payment to statutory auditors (Note 31.1, consolidated, p.259):

| | FY26 (Rs Mn) | FY25 (Rs Mn) |
|---|---|---|
| Statutory audit | 2.29 | 1.40 |
| Tax audit | 0.48 | 0.43 |
| **Audit-related subtotal** | **2.77** | **1.83** |
| Other matters (non-audit) | 3.88 | 3.28 |
| **Total** | **6.65** | **5.11** |

**Non-audit fee (Rs 3.88 Mn) exceeds the audit-related fee (Rs 2.77 Mn) in FY26 — ratio 1.40x — and the same pattern holds in FY25 (Rs 3.28 Mn vs Rs 1.83 Mn, ratio 1.79x).** Per protocol instruction this is flagged: non-audit fees consistently exceed audit fees across both years shown, and the "Other matters" category is not itemised in the note (no breakdown of what services this covers — tax advisory, certification work, or something else). 🟡 WATCH.

### 1F. Standalone vs Consolidated Differences

No extra qualifications on either report beyond the sole vii(a) CARO item (which is inherently a standalone/subsidiary-level clause; the consolidated report cross-refers to it rather than restating). The consolidated auditor relies on the audit reports of Indian subsidiary auditors for the ICFR opinion (Annexure A reference, p.207) — the identity of those component auditors is NOT FOUND in the portion of the AR reviewed; worth checking Note 2/52 (subsidiary list) cross-referenced against auditor-network disclosure if a verifier wants full assurance on multi-auditor consolidation risk. The ESOP trust is included in the consolidation scope alongside subsidiaries and the associate (p.199) — a slightly unusual but not improper consolidation perimeter.

### Phase 1 Summary Table

| Item | Finding | Verdict |
|---|---|---|
| Opinion | Unmodified, both reports | 🟢 |
| Going concern | Clean, no EOM | 🟢 |
| KAM | Sole KAM = revenue recognition; M&A accounting NOT flagged as KAM despite materiality | 🟡 |
| CARO | 19/20 clauses clean; vii(a) PF arrears qualified, small but persistent multi-year | 🟡 |
| Fraud (xi) | Clean | 🟢 |
| Auditor fee ratio | Non-audit > audit both years | 🟡 |
| Auditor tenure | Year 4 of first 5-year term, no rotation issue | 🟢 |

**Phase 1 verdict: 🟡 WATCH.** Kill Switch Assessment (informational): a human reviewer would NOT have reason to stop the process here. Nothing rises to a going-concern, fraud, or qualified-opinion level. The KAM gap (M&A accounting not spotlighted) and the auditor fee-ratio pattern are worth carrying into Phase 2/3, not halting on.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the Phase 2 special instruction, the triple-pass Stage 2 output (runs/emudhra-2026-09-19/outputs/reports/02-notes.md, block B02-notes.yaml) is treated as the base extraction. Below: verification of the Top 15 findings against the document, plus the extensions this phase adds (accounting-policy aggressiveness scoring reconciliation, RPT %, contingent-liability ratios, debt maturity wall).

### Verification of Triple-Pass Top 15

All 15 findings were spot-checked against the primary source during this pass (auditor's report cross-check for findings 1, 3, 5, 6; balance sheet/P&L cross-check for goodwill Rs 2,940.46 Mn, borrowings Rs 238.73 Mn, contingent-consideration Rs 881.45 Mn all tying to the consolidated Balance Sheet read directly in this stage, p.216). **Result: 15 of 15 VERIFIED, 0 discrepancies.** Two direct cross-ties performed independently in this stage: (a) Goodwill Rs 2,940.46 Mn ties exactly to the Balance Sheet non-current asset line (d) "Goodwill" (mupdf p.216, scrambled OCR read as "29,40.46" = 2,940.46); (b) Other financial liabilities (non-current) Rs 881.45 Mn (contingent consideration, finding 1/5) ties exactly to the Balance Sheet line (ii) "Other financial liabilities" under non-current liabilities.

### 2A. Accounting Policy Aggressiveness — Extension

- **Revenue recognition**: Ind AS 115, standard point-in-time/percentage-of-completion/straight-line mix, no policy change quantified this year beyond the useful-life change (which is a depreciation policy item, not revenue). Practical expedient used to avoid disclosing remaining performance obligations (per B02).
- **Depreciation/amortisation lives**: the one quantified change this year — intangible useful life extended to 10 years effective 1-Apr-2025 (Note 5a(iii)(a)), cutting FY26 amortisation by ~Rs 39.96 Mn, timed with the acquisition-driven intangible build. Properly disclosed under Ind AS 8 with a quantified effect. **This is the single most P&L-flattering discretionary accounting choice in the AR** — worth carrying to Phase 3C's margin walk.
- **Borrowing costs capitalisation**: no specific disclosure of capitalised borrowing costs was found; group carries minimal debt (Rs 238.73 Mn consolidated) so this is immaterial.
- **Inventory method**: no change; inventory is small (Rs 39.00 Mn consolidated FY26) relative to the balance sheet.
- **ECL matrix**: provision for expected credit loss/doubtful debts Rs 50.00 Mn (FY26) vs Rs 21.92 Mn (FY25) per the cash flow statement adjustment line — roughly doubled, consistent with the growing receivables base; ageing bucket improved (13.5% to 12.3% >6 months per B02), so the ECL increase appears provisioning-conservative rather than a red flag.
- **Ind AS 116 (leases) discount rate %**: NOT FOUND IN DOCUMENT in the sections reviewed (confirmed absent per B02 finding "no lease discount rate %").

### 2B. RPT Map — Extension (percentages)

Per B02 findings 9, 13, 14: related-party trade receivables Rs 68.18 Mn (FY26) vs Rs 4.91 Mn (FY25); related-party trade payables Rs 104.01 Mn vs Rs 1.89 Mn, both concentrated in Bluesky Infotech. RPT sales Rs 57.28 Mn = **0.8% of FY26 consolidated revenue (Rs 7,015.80 Mn)** — immaterial in aggregate. New promoter-entity/director lending in Rs 82.87 Mn (Taarav PTE 8% p.a. + Executive Chairman interest-free) — 0% of FY25, a first-instance item. Standalone-vs-consolidated PAT divergence (61% vs 26% growth, B02 finding 13) driven by intercompany royalty (~Rs 169.9 Mn FY26 vs ~Rs 79.8 Mn FY25, +113% YoY) — this royalty growth rate itself outpaces even the acquisition-adjusted revenue growth and is worth a transfer-pricing question (already in B02's five questions).

### 2C. Contingent Liabilities — Ratios

Quantified contingent liability (standalone and consolidated) Rs 32.29-34.55 Mn (MD&A states Rs 32.29 Mn; B02 states Rs 34.55 Mn from Note 36 — small discrepancy between the MD&A summary table and the notes total, both immaterial in absolute terms, NOT reconciled further in this pass). Against net worth (Total equity attributable to owners Rs 9,111.33 Mn): **0.35-0.38% of net worth** — far below the 25%/100% flag thresholds. Against PAT (Rs 1,100.38 Mn consolidated): **2.9-3.1% of PAT** — also immaterial.

**However, the UNQUANTIFIED 3i Infotech claim (>Rs 128 Cr = Rs 1,280 Mn+) would be ~14% of net worth and ~116% of FY26 consolidated PAT if it ever crystallised** — this is the ratio that matters, and it sits entirely outside the quantified contingent-liability disclosure on management's own "no economic outflow" assessment (B02 finding 8, confirmed at Note 36(f)/38(e)).

### 2D-2H

Receivables, inventory, borrowings, deferred tax, exceptional items, goodwill, ESOP, lease, and subsequent-event coverage are fully addressed in B02 Pass 1-3 and not re-extracted here; see B02 top findings 1-15 and Patterns A/B (runs/emudhra-2026-09-19/outputs/reports/02-notes.md lines 15-19). One extension: **debt maturity wall** — group borrowings are minimal (Rs 238.73 Mn total, Rs 129.88 Mn non-current + Rs 108.85 Mn current per Balance Sheet, p.216) with NO Indian-entity bank debt (confirmed by standalone CARO clause ix "not applicable"); the debt sits entirely at overseas subsidiaries. No maturity schedule with named tranches was found in the sections reviewed — given the small absolute size this is low-priority.

### Cross-reference with Phase 1 KAMs

The sole KAM (revenue recognition) does not cover the two largest Phase 2 findings (goodwill Rs 2,940.46 Mn, contingent consideration Rs 881.45 Mn) — this gap, first identified in B02 finding 6, is confirmed independently in Phase 1B above.

### Phase 2 Accounting Quality Score Reconciliation

B02's triple-pass score is **6/10** (component breakdown: revenue recognition 6, expense capitalisation 5, provisioning 6, RPT fairness 6, disclosure transparency 5, consistency 7). This Stage-3 pass agrees with the 6/10 overall score and the component reasoning — the verification above did not surface anything that would move any component score. **Reconciled: 6/10, no disagreement.**

Phase 2 verdict: 🟡 WATCH (unchanged from B02's own one-line verdict). Kill Switch Assessment (informational): a human reviewer would NOT stop here — the core operating business is clean (no fraud, no going concern, low leverage); the flags are disclosure gaps on judgment items, not evidence of misstatement.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow → balance sheet → P&L)

### 3A. Cash Flow (Consolidated Cash Flow Statement, p.216-219; cross-checked against mupdf.txt lines 10578-10668 for the scrambled pdftotext table)

| Rs Mn | FY26 | FY25 |
|---|---|---|
| PBT | 1,313.13 | 1,073.98 |
| Operating profit before WC changes | 1,752.45 | 1,313.29 |
| Cash generated from operations | 1,481.01 | 1,131.74 |
| Income taxes paid | (152.52) | (115.58) |
| **CFO (A)** | **1,328.49** | **1,016.16** |
| Purchase of PPE + intangibles | (1,853.68) | (832.02) |
| Payment for acquisitions (net of assets acquired) | (629.03) | (743.23) |
| Net investments/mutual fund movement (net) | 232.11 | (735.64)* |
| **CFI (B)** | **(2,250.53)** | **(2,113.40)** |
| Financing net (C) | 218.86 | (213.48) |
| FX translation (D) | 272.98 | 70.59 |
| **Net change in cash (A+B+C+D)** | **(430.19)** | **(1,240.13)** |
| Cash at year end | 582.33 | 1,012.52 |

*net figure derived, not a face-statement line

**CFO/PAT** = 1,328.49 / 1,100.38 = **1.21x** (FY26); 1,016.16 / 872.34 = **1.16x** (FY25). Both comfortably above the 0.7x flag threshold — cash earnings exceed accounting earnings in both years, a genuine positive despite the working-capital deterioration flagged in B02 Pattern A.

**CFO/EBITDA**: using EBITDA ≈ Rs 1,590.34 Mn (revenue-based, ex-other-income; see 3C below), CFO/EBITDA = 1,328.49/1,590.34 = **0.84x** (FY26); prior-year EBITDA ≈ Rs 1,161.35 Mn (revenue 5,193.85 less operating costs derived the same way), giving 1,016.16/1,161.35 = **0.87x** (FY25). Consistent, no deterioration.

**FCF** = CFO − capex(PPE+intangibles) = 1,328.49 − 1,853.68 = **Rs -525.19 Mn (Rs -52.5 Cr)** FY26; 1,016.16 − 832.02 = **+Rs 184.14 Mn (+Rs 18.4 Cr)** FY25. **FY26 free cash flow turned negative for the first time in the two years shown, entirely because capex (PPE+intangibles) more than doubled** (Rs 832.02 Mn → Rs 1,853.68 Mn, +122.8%) while CFO grew only 30.8%. See Load-Bearing Fact 2 above for the reconciliation detail against the B01/screener figures.

**Capex vs depreciation**: capex Rs 1,853.68 Mn vs D&A Rs 342.51 Mn = **5.4x** — capex is running far ahead of depreciation, consistent with an acquisitive, asset-building year rather than steady-state maintenance capex. This ratio will mechanically fall once the newly acquired intangibles begin amortising over their (extended, 10-year) useful lives.

**M&A spend**: Rs 629.03 Mn (FY26, net of assets acquired) — Cryptas + AI Cyberforge; Rs 743.23 Mn (FY25) — Two95 International + Sendrcrypt (per Note references at lines 11856-11930).

**CFO quality checks**:
- No evidence of one-time inflators found — the cash flow adjustments (D&A, ECL provision, unrealised/realised gains, sundry creditors written back, MSME interest accrual, contingent-consideration interest unwind Rs 28.72 Mn) are all standard, disclosed reconciling items.
- **Working capital moved AGAINST cash generation this year**: Increase in trade payables +Rs 302.81 Mn added back to CFO (FY26) vs +Rs 80.21 Mn (FY25) — i.e., the payables stretch (B02 Pattern A, +91% YoY) is mechanically flattering CFO this year. Decrease/(increase) in trade receivable was Rs (487.46) Mn (a cash use, FY26) vs Rs (443.70) Mn (FY25) — receivables grew but the cash-flow-statement working-capital line is dominated by the payables tailwind.
- **Interest classification**: "Interest on contingent consideration" appears as a separate finance-cost line (Note 29, per B02 finding 15) rather than buried in operating expenses — appropriately classified, though the exact FY26 rupee split within the Rs 50.69 Mn consolidated finance-cost line could not be extracted cleanly from the scrambled table (flagged in B02, unresolved here too).
- No evidence of inventory rundown funding cash (inventory is small and grew, not shrank).

**Cash pile trend**: consolidated cash and cash equivalents fell from Rs 1,012.52 Mn to Rs 582.33 Mn (using the Balance Sheet definition) — a **42.5% decline** — funded by the acquisition and capex programme. On the MD&A's broader liquidity definition (cash + FDs >3 months), the fall is smaller: Rs 1,885.54 Mn → Rs 1,268.48 Mn (-32.7%).

### 3B. Balance Sheet (Consolidated, p.216; mupdf lines 10403-10467)

| Rs Mn | FY26 | FY25 | YoY |
|---|---|---|---|
| PP&E | 1,291.08 | 1,147.96 | +12.5% |
| Right-of-use assets | 48.45 | 0.00 | new |
| CWIP | 185.84 | 171.43 | +8.4% |
| **Goodwill** | **2,940.46** | **1,254.60** | **+134.4%** |
| Other intangibles | 2,988.64 | 1,788.06 | +67.1% |
| Intangibles under development | 105.92 | 2.43 | n.m. |
| Total non-current assets | 7,778.69 | 4,419.28 | +76.0% |
| Total current assets | 4,355.64 | 4,262.07 | +2.2% |
| **Total Assets** | **12,134.33** | **8,681.35** | **+39.8%** |
| Equity attributable to owners | 9,111.33 | 7,453.26 | +22.3% |
| Non-controlling interests | 14.57 | 19.54 | -25.4% |
| **Total equity** | **9,125.90** | **7,472.80** | **+22.1%** |
| Non-current borrowings | 129.88 | 0.00 | new |
| Other financial liabilities (non-current, incl. contingent consideration) | 881.45 | 55.34 | +1,492.9% |
| Total non-current liabilities | 1,430.43 | 234.94 | +508.8% |
| Current borrowings | 108.85 | 0.00 | new |
| Total current liabilities | 1,578.00 | 973.61 | +62.1% |
| **Total liabilities** | **3,008.43** | **1,208.55** | **+149.0%** |
| **Total Equity and Liabilities** | **12,134.33** | **8,681.35** | **+39.8%** |

**Key ratio table** (Rs Mn unless noted):

| Ratio | FY26 | FY25 | Basis |
|---|---|---|---|
| D/E (total borrowings / total equity) | 0.026x | 0.00x | Borrowings 238.73 / Equity 9,125.90 |
| Net debt/EBITDA | Net CASH (negative net debt) | Net cash | Cash 582.33 + other bank balances 69.71 = 652.04 > total borrowings 238.73 |
| Current ratio | 2.76x (2.9x per MD&A average basis) | 4.38x | Current assets/current liabilities |
| Quick ratio (ex-inventory) | 2.74x | 4.36x | (Current assets − inventory)/current liabilities |
| Interest coverage (EBIT/finance cost) | 26.9x | n.m. (finance cost 11.58 Mn) | (PBT+finance cost)/finance cost |
| ROCE (closing capital employed) | 12.9% | n.m. | EBIT 1,363.82 / (Total assets − current liabilities) |
| ROCE (average capital employed) | 14.9% | — | Same EBIT / avg(CE FY26, CE FY25) |
| ROE (closing) | 11.8% | 11.4% | PAT(owners)/closing equity(owners) |
| ROE (average) | 13.0% | — | PAT(owners)/avg equity(owners) |
| Goodwill % of net worth | 32.3% | 16.8% | Goodwill/equity attributable to owners |

**DuPont decomposition (FY26, average basis)**: Net margin (owners' PAT/Total Income) = 1,077.92/7,131.79 = **15.11%**; Asset turnover (Total Income/avg Total Assets) = 7,131.79/10,407.84 = **0.685x**; Equity multiplier (avg Total Assets/avg owners' equity) = 10,407.84/8,282.30 = **1.257x**. ROE = 15.11% × 0.685 × 1.257 = **13.0%**, matching the direct calculation. **ROE is margin-driven, not leverage-driven** — the equity multiplier of 1.26x confirms minimal balance-sheet leverage; the business earns its (middling) ROE from operating margin and modest asset efficiency, not from debt.

**Finding worth carrying forward**: despite 35.1% revenue growth and a 134% jump in goodwill, **ROCE and ROE both sit in the low-to-mid teens (13-15%)** — a genuine tension for a company reportedly trading near 44x TTM P/E (company memory, non-AR-anchored). This is arithmetically explained by (a) Cryptas contributing only ~9 months at PAT breakeven (company memory) while its full purchase price (Rs 1,315.25 Mn) already sits in the capital-employed base, and (b) the acquisition-driven goodwill/intangible build inflating the denominator ahead of the earnings it is meant to generate. This is a capital-efficiency point for Stage 11, not a red flag in itself — but the AR gives no forward path (no disclosed synergy targets, no goodwill-impairment growth assumptions per B02 Pattern B) for when ROCE should recover.

**Standalone cross-check** (p.310, line-item read): Total Assets Rs 6,687.20 Mn (FY26) vs Rs 5,984.88 Mn (FY25); Total equity Rs 5,791.58 Mn vs Rs 5,452.70 Mn. Standalone MSME payables (micro/small enterprises) Rs 68.06 Mn vs Rs 28.79 Mn (+136%) — matches B02's frozen Rs 21.61 Mn >3-year bucket discussion exactly (same Note 18/40/43 figures).

### 3C. P&L (Consolidated, p.217-218; mupdf lines 10499-10553)

| Rs Mn | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue from operations | 7,015.80 | 5,193.85 | +35.1% |
| Other income | 115.99 | 84.51 | +37.2% |
| **Total income** | **7,131.79** | **5,278.36** | **+35.1%** |
| Operating expenses | 2,769.41 | 2,112.33 | +31.1% |
| Purchase of stock-in-trade | 547.46 | 305.07 | +79.5% |
| Change in inventories | (25.01) | 15.37 | n.m. |
| Employee benefits expense | 1,388.06 | 929.64 | +49.3% |
| Finance costs | 50.69 | 11.58 | +337.7% |
| D&A | 342.51 | 238.26 | +43.8% |
| Other expenses | 745.54 | 592.13 | +25.9% |
| **Total expenses** | **5,818.66** | **4,204.38** | **+38.4%** |
| **PBT** | **1,313.13** | **1,073.98** | **+22.3%** |
| Tax (current + deferred) | 212.66 | 201.64 | +5.5% |
| **PAT (before associate share)** | **1,100.47** | **872.34** | **+26.2%** |
| Share of associate | (0.09) | 0.00 | new |
| **PAT for the year** | **1,100.38** | **872.34** | **+26.1%** |
| Attributable to owners | 1,077.92 | 846.38 | +27.4% |
| Attributable to NCI | 22.46 | 25.96 | -13.5% |
| Basic EPS (Rs) | 13.14 | 10.41 | +26.2% |
| Diluted EPS (Rs) | 13.02 | 10.22 | +27.4% |

**Margin waterfall**: Revenue Rs 7,015.80 Mn → EBITDA (ex-other-income) ≈ Rs 1,590.34 Mn (22.7% of revenue) → EBIT (PBT+finance cost, incl. other income) Rs 1,363.82 Mn (19.4% of revenue) → PBT Rs 1,313.13 Mn (18.7%) → PAT Rs 1,100.38 Mn (15.7%) → PAT attributable to owners Rs 1,077.92 Mn (15.4%). The Rs 1,654 Mn EBITDA figure cited in company memory (23.2% margin, "adjusted" basis) is somewhat higher than the Rs 1,590.34 Mn computed here from the face P&L on a revenue basis — the difference is consistent with an "adjusted EBITDA" definition (likely excluding ESOP cost or including a different other-income treatment) that is NOT reproduced in the AR's own MD&A table; the MD&A itself (p.55, front-matter highlights) separately states "EBITDA Rs 1,654 Mn +32.6% YoY 23.2% Margins" and "ADJ. EBITDA" as a distinct, unlabelled line — the exact adjustment bridge is NOT FOUND IN DOCUMENT in the sections reviewed.

**Other income**: Rs 115.99 Mn = **1.6% of total income**, well under the 20% flag threshold — no red flag here despite growing 37.2% YoY (growth driven by FX gains on consolidation and FD interest per MD&A narrative, p.149).

**Exceptional items**: NIL in both FY26 and FY25 (P&L line "Exceptional items" = 0 both years) — no 3-year exceptional-item pattern to assess; clean.

**Tax rate**: Effective tax rate 16.2% (FY26) vs 18.8% (FY25) consolidated, vs statutory ~25.17% (India) — the gap (B02 finding 11) is driven almost entirely by lower foreign-subsidiary tax rates (Note 20(c), Rs 109.17 Mn reconciling benefit). Standalone ETR is 25.5% (FY26) vs 31.0% (FY25) — much closer to the Indian statutory rate, confirming the consolidated ETR benefit is a geography-mix effect, not an Indian-entity tax-planning item. **This ETR gap (16.2% vs 25.17%) is a real, disclosed, durable-looking tax benefit, but it is mix-dependent — if the international revenue share (already 64% and rising) shifts toward higher-tax jurisdictions (e.g., the newly acquired European Cryptas business, or further US expansion) the ETR could rise toward the standalone 25.5% print over time.**

**Basic vs diluted EPS gap**: Rs 13.14 vs Rs 13.02 (FY26) = **0.9% dilution**; Rs 10.41 vs Rs 10.22 (FY25) = **1.8% dilution**. Small, consistent with modest ESOP-driven share count growth, not aggressive dilution.

**Standalone P&L note**: Standalone revenue grew 32.4% (Rs 2,029.60 Mn → Rs 2,686.67 Mn), standalone PAT grew 73.6% (Rs 186.65 Mn → Rs 323.92 Mn per the MD&A results table, p.150) — this is a HIGHER growth figure than the Rs 270.45→434.86 Mn (+60.7%) figure B02 cited from the standalone financial statements directly; the discrepancy is that the MD&A results table (p.150) and the standalone Statement of P&L in the financial statements (p.310+) appear to use slightly different PAT bases (possibly pre- vs post-associate-share, or a rounding/note-reference difference) — **flagged as an internal AR reconciliation gap worth a verifier check**, though both readings agree directionally: standalone PAT grew markedly faster than consolidated PAT (26.1%), consistent with B02's royalty-fee explanation (finding 13).

### Phase 3 Summary Table

| Item | Finding | Verdict |
|---|---|---|
| CFO/PAT | 1.21x (FY26), 1.16x (FY25) | 🟢 |
| FCF | Turned negative, -Rs 52.5 Cr (FY26), from +Rs 18.4 Cr (FY25) | 🟡 |
| Capex/D&A | 5.4x — heavy investment year | 🟡 |
| Leverage | D/E 0.026x, net cash | 🟢 |
| ROCE/ROE | 13-15% — modest, capital-employed inflated by acquisitions | 🟡 |
| Margin waterfall | Clean, no exceptional items, other income immaterial | 🟢 |
| Tax rate | 16.2% consol vs 25.5% standalone — geography-mix benefit, durability uncertain | 🟡 |
| EPS dilution | <2% — modest | 🟢 |

**Phase 3 verdict: 🟡 WATCH.** Kill Switch Assessment (informational): a human reviewer would NOT stop here. The core financial statements are clean and internally consistent (cross-ties confirmed on goodwill, contingent consideration, CFO/capex). The negative FCF and modest ROCE/ROE are real, disclosed features of an acquisition-heavy transition year, not evidence of misstatement or distress — CFO/PAT >1x and net-cash balance sheet both argue against a cash-flow-quality problem.

---

## PHASE 4: RISK FACTORS & MD&A

### 4A. Disclosed Risks — Real vs Boilerplate (MD&A Enterprise Risk Management, p.153-163)

| Risk category | Real or boilerplate | Note |
|---|---|---|
| Business risk (segment/geography concentration) | REAL — quantified (Trust Services 20% : Enterprise Solutions 80%; India 36% : International 64%) | Specific numbers, specific mitigation logic |
| Competition risk | REAL — names specific global competitors (DigiCert, Entrust, GlobalSign, Microsoft, Okta, Thales, etc.) per product line, and specific Indian licensed-CA competitors in a comparison table | Unusually detailed for an AR risk section |
| Technology risk / legal-regulatory risk | REAL — specific to PKI/CA business model (WebTrust accreditation, CA/Browser Forum compliance, open-source licensing discipline) | Substantive, not generic |
| Operations/financial/compliance risk | REAL — receivables risk explicitly named with unsecured credit terms, FX risk quantified (64% international revenue) | Substantive |
| Human resource risk | Largely boilerplate ("attract and retain talent") but ties to a concrete point (ESOP-based retention for 2nd/3rd management levels) | Mixed |

**Overall**: this MD&A risk section is more substantive than typical AR boilerplate — it names real competitors, real regulatory bodies, and real business-mix numbers. That said, it is entirely forward/structural risk; it contains **no discussion of the specific, dated, material items that surfaced in Phases 1-3** (see 4B).

### 4B. MISSING RISKS

| Missing risk | Evidence from Phases 1-3 | Likely reason for omission |
|---|---|---|
| **3i Infotech Rs 128+ Cr claim** | Note 36(f)/38(e), chronology through 23-Apr-2026 legal notice — three weeks before the 6-May-2026 audit sign-off | Management's own "no economic outflow" / "baseless" assessment (Note 36(f)) presumably extends to omitting it from the risk narrative too; but a claim of this size relative to net worth (~14%) crossing the AR's own cutoff date is a natural candidate for risk-section mention even under a "low probability" framing. Its complete absence from the 8-page Enterprise Risk Management section is conspicuous. |
| **Cryptas contingent-consideration / 49% option structure (uncapped upside, Rs 881.45 Mn)** | Note 4a(c)/17a/53(b) — the largest, least-bounded forward liability in the corpus (B02 finding 1) | No "acquisition integration risk" or "earn-out risk" category exists anywhere in the risk section, despite two completed acquisitions this year and a 2028-2030 exercise window already locked in |
| **Goodwill impairment risk** | Rs 2,940.46 Mn, no discount rate/growth rate/headroom disclosed (B02 Pattern B) | Same omission pattern — acquisition accounting risk generally is not a named risk category |
| **MSME/statutory-dues payment risk** | CARO vii(a), Rs 21.61 Mn frozen >3 years across two ARs | Small in absolute rupee terms; management may judge it immaterial, but persistence across two years without resolution is itself a process-discipline signal worth naming |
| **Working-capital funded growth (Pattern A)** | Unbilled revenue +40.6%, payables +91%, both outrunning 35.1% revenue growth | Not the kind of risk companies volunteer; requires cross-note synthesis to see (exactly the gap B02's Pass 3 pattern-read was built to catch) |

### 4C. MD&A Deep Dive

**Industry claims**: the "Business Outlook" section (p.147) cites IMF October 2025 WEO global growth figures, WEF Global Cybersecurity Outlook 2026 (94% of respondents naming AI as the top cybersecurity change driver), and Gartner's $240 billion 2026 cybersecurity-spend projection. These are external, attributable, checkable claims — properly sourced to named third parties, not asserted as eMudhra's own data.

**Growth and margin explanations**: revenue growth (+35.1% consolidated) is explained by "increase in our solutions and services revenue in India and global markets" (p.151) plus the specific Trust Services (+32.3%) and Enterprise Solutions India (+27.6%) / Global (+38.3%) splits (p.151) — reasonably granular. Cost of goods sold explanation (p.151-152) specifically calls out a CCA-mandated business-model change (July 2024) forcing DSC stock repurchase from partners, which explains both the elevated "purchase of stock-in-trade" line and part of the standalone COGS jump (38.3% → 44.1% of total income) — a credible, external, regulator-driven explanation rather than a vague one.

**External-factor credit-taking or blaming**: the AR credits management execution for revenue growth and credits an external regulatory change (CCA guidelines) for the COGS increase — a reasonably balanced attribution pattern, not one-sided credit-taking.

**Forward guidance table**:

| Claim | Number | Timeframe | Source | Credibility check |
|---|---|---|---|---|
| FY27 organic revenue growth | 15-18% | FY27 | Concall (Q4FY26, company memory) — **NOT FOUND IN THIS AR** | Cannot be checked against the AR itself; AR's own "Looking Ahead" (p.51) gives no numeric FY27 target |
| FY27 PAT growth | 25-30% | FY27 | Concall — **NOT FOUND IN THIS AR** | Same |
| "Double PAT over 3 years" | implies ~26% CAGR | 3 years | Concall — **NOT FOUND IN THIS AR** | Same |
| Existing-customer share of business | 67% | FY26 (actual, not forward) | MD&A p.148 | Directly stated in the AR, not a forward claim |
| International revenue growth | 38.7% | FY26 (actual) | MD&A p.148 | Directly stated |

**The AR itself contains no forward-looking numeric guidance table** — the "Looking Ahead — FY2026-27 and Beyond" section (p.51) is entirely qualitative (post-quantum readiness, Agentic AI trust, Europe deepening, US FedRAMP scaling, partner-ecosystem launches). This is a genuine gap for anyone relying on the AR alone for a guidance-credibility check; the numeric guidance load-bearing fact #1 depends on outside-AR sources (concall transcripts), which the pipeline's downstream stages should verify directly against those transcripts rather than the AR.

### 4D. Tone and Credibility Ratings (1-5)

| Dimension | Rating | Evidence |
|---|---|---|
| Transparency | 3/5 | Detailed competitor and risk tables (strong); but material, dated items (3i Infotech, Cryptas earn-out structure) entirely absent from the risk section (weak) |
| Consistency | 4/5 | MD&A numbers tie cleanly to the face financial statements on every check performed in Phase 3; no restatements found (per B02) |
| Specificity | 4/5 | Revenue/margin walk is genuinely granular (segment splits, cost-line percentages, named competitors) — above-average for an Indian small/micro-cap AR |
| Accountability | 3/5 | COGS increase honestly attributed to a specific external regulatory event (CCA guideline change) rather than vaguely blamed on "market conditions"; but no acknowledgement anywhere of the FCF turn negative or the ROCE/ROE compression this year |
| Capital allocation sense | 3/5 | Two acquisitions this year with a clearly stated strategic rationale (European entry, key/secrets management) but no disclosed post-acquisition financial targets, synergy numbers, or integration milestones against which to hold management accountable next year |

### Phase 4 Summary

Contradictions vs Phases 1-3: none material — the one apparent contradiction (MD&A's Rs 1,268.48 Mn "cash" figure vs the Balance Sheet's Rs 582.33 Mn) resolves cleanly once the MD&A's own liquidity table (p.152) is read in full (it is cash + FDs, not cash alone). The PAT-growth-rate discrepancy between the MD&A standalone results table and the standalone financial statements (Phase 3C) remains unresolved and is flagged for verifier attention.

**Phase 4 verdict: 🟡 WATCH.** Kill Switch Assessment (informational): a human reviewer would NOT stop here, but WOULD want the 3i Infotech and Cryptas earn-out omissions from the risk section explained directly by management — their complete absence from an otherwise detailed 8-page risk section is the single most conspicuous omission in the entire AR.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A. Board Composition (as at 31-Mar-2026, Corporate Governance Report p.119-121)

| Director | Category | Appointment date | Tenure at FY26-end | Other directorships (public) | Other listed directorships |
|---|---|---|---|---|---|
| Venkatraman Srinivasan | Executive Chairman | 16-Jun-2008 | ~17.8 years | 2 | Nil |
| Nandlal L Sarda | Independent | 19-Jun-2018 | ~7.8 years | Nil | Nil |
| Chandra Iyer | Independent (the one woman director) | 13-Aug-2021 | ~4.6 years | 3 | **4** |
| Chandrasekar Padmanabhan | Independent | 3-Nov-2021 | ~4.4 years | Nil | Nil |
| V Chandrasekaran | Independent | 1-Apr-2025 | ~1.0 year | 7 | Nil |
| Shivanand R Shettigar | Independent | 2-Apr-2025 | ~1.0 year | Nil | Nil |
| Venu Madhava | Whole-Time Director | 10-Jan-2014 | ~12.2 years | 2 | Nil |

Board as at 31-Mar-2026: 7 directors (2 Executive, 5 Independent, 1 woman director) — matches Board's Report §15 exactly. **No independent director exceeds the 10-year tenure flag threshold**, though Nandlal Sarda at 7.8 years is the longest-serving and will cross that line within the current strategy's 3-5 year hold horizon. **No director holds >8 board seats.** Chandra Iyer's 4 other listed-company directorships is within SEBI LODR caps but is the most cross-board-engaged member on this board — worth noting given her Audit Committee membership is NOT among the three named (Audit Committee = Padmanabhan, Chandrasekaran, V Srinivasan per §III(c), p.128) — i.e., Iyer's engagement is outside the audit function.

**Subsequent event (not yet reflected in the FY26 board table)**: effective 1-Apr-2026, two more promoter-family members — Kaushik Srinivasan (Whole-Time Director) and Arvind Srinivasan (Director) — joined the board following a Postal Ballot approval (Board's Report §15, p.91-92). This expands the board to 9 and shifts the executive/promoter-family count from 2-of-7 to **4-of-9** (still independent-majority overall, but the promoter-family presence on the board roughly doubles). This is a real governance-structure change occurring just after the audited year-end and should be tracked into FY27.

### 5B. Committee Analysis

**Audit Committee**: 3 members (Chandrasekar Padmanabhan – Chairman, V Chandrasekaran – Member, both Independent; Venkatraman Srinivasan – Member, Executive Chairman). 5 meetings held (6-May-25, 24-Jul-25, 11-Nov-25, 2-Feb-26, 17-Mar-26), **100% attendance by all three members at all 5 meetings** (p.128). Mandate is comprehensive (30 items listed, p.122-125), covering RPT approval, whistleblower/vigil mechanism oversight, internal-financial-control evaluation. **Note**: the Executive Chairman sitting as an Audit Committee member (not just attending) is a structure worth flagging — SEBI LODR permits this (a majority of independent members with an independent chairperson is the requirement, which is met: 2 of 3 independent, chair independent) but it is a tighter structure than an all-independent Audit Committee.

**Nomination, Remuneration and Board Governance Committee**: terms of reference reviewed (p.125-129) — standard mandate (remuneration policy, board evaluation criteria, board diversity policy, KMP identification). Meeting count/attendance for this committee is NOT FOUND in the portion reviewed (would require reading further into the Corporate Governance Report, p.129+).

**Risk Management Committee**: exists per Board's Report §35 (p.87) and Corporate Governance Report §VII (p.5893 in raw text / later CG pages) — mandate described but meeting count/attendance NOT extracted in this pass.

### 5C. Compensation

KMP remuneration table (Board's Report §25, p.94):

| Name | Role | FY26 remuneration (Rs Mn) | % increase YoY |
|---|---|---|---|
| V Srinivasan | Executive Chairman | **Nil** (footnoted: no remuneration paid from eMudhra or subsidiary) | n/a |
| Venu Madhava | Whole-Time Director | 7.14 | +12.8% |
| Ritesh Raj Pariyani | CFO | 5.31 | **+42.4%** |
| Johnson Xavier | Company Secretary | 3.68 | +12.2% |

Ratio of director remuneration to median employee remuneration: Venu Madhava **10.90x**; non-executive directors range 2.32x-2.94x (sitting fees/commission basis). Median employee remuneration increase: **7.1%** (FY26). Permanent employees on eMudhra Ltd rolls: 604; group total: 861 (up from 851 in FY25).

**Observations**: the Executive Chairman drawing zero cash remuneration from the listed entity or its subsidiaries is unusual and worth noting — it likely reflects promoter economics being extracted through dividends/shareholding rather than salary (he and Mythili Srinivasan jointly hold ~17.36% of equity, unchanged YoY per the promoter table, p.248/252). **The CFO's 42.4% remuneration increase is the largest percentage jump of any named individual in the KMP table** — well above the 7.1% median-employee increase and above the other KMPs' 12-13% increases. No narrative explanation for this outsized CFO increase was found in the sections reviewed; worth a direct question, especially set against the acquisition-heavy, judgment-intensive year the CFO's function had to navigate (Phase 2 disclosure gaps sit under the CFO's function).

**ESOP dilution**: basic-to-diluted EPS gap of 0.9% (FY26) / 1.8% (FY25) indicates modest, non-aggressive dilution (Phase 3C). Share-based payment expense (Note, per MD&A p.149) increased from 1.4% to 1.5% of total income on a consolidated basis.

### 5D. Shareholding

Promoter/promoter-group table (Note, consol p.248 and p.252, standalone equivalent) names five holders — V Srinivasan & Mythili Srinivasan (combined 17.36%, unchanged YoY), Taarav Pte Ltd, Arvind Srinivasan, Kaushik Srinivasan, and others — **but the pdftotext -layout rendering of this table is scrambled beyond confident per-row reconstruction** (columns interleave FY26/FY25 figures unpredictably; cross-checked against mupdf.txt without full resolution). What is legible: total promoter-group holding is in the mid-50s percent range, broadly consistent with the 54.40% figure reported to BSE (company memory, non-AR-anchored, as at Jun-2026). **No pledge language was found anywhere in the AR text** (searched case-insensitively for "pledge" and "encumbr*" — zero matches) — consistent with company memory's "no pledge" reading, though the AR's silence on the topic is not itself an anchored confirmation (pledge disclosure typically lives in the separate quarterly BSE Reg 31 filing, not repeated in the AR). **FII/DII split is NOT FOUND IN THIS AR** — confirmed as a corpus gap already logged in B00 (screener-only, non-anchored).

No promoter-selling-against-growth-narrative pattern is visible from what is anchored here (promoter % held flat YoY per the one line item that was legible).

### 5E. Governance Red-Flag Checklist

| Item | Finding |
|---|---|
| Whistleblower complaints | NONE received during the year or up to report date (CARO xi(c), confirmed twice — standalone CARO and Board's Report §16) |
| SEBI actions against directors | NONE — Company Secretary's non-disqualification certificate confirms no director debarred/disqualified by SEBI, MCA, or any statutory authority (p.140-144) |
| RPT committee | Functions through the Audit Committee (standard structure); RPTs immaterial (0.8% of revenue) but the new promoter-entity lending pattern (Rs 82.87 Mn, B02 finding 9) is a related-party item outside the normal commercial RPT flow |
| Auditor fee ratio | Non-audit exceeds audit fee both years (Phase 1E) — governance-relevant, since Audit Committee approval of non-audit fees is one of its stated mandates (§III(a)(3), p.122) |
| CSR compliance | Over-spent (Rs 6.48 Mn vs Rs 3.09 Mn obligation), no unspent-CSR CARO qualification |
| Section 143 fraud reporting | NONE — CARO xi(a)/(b) clean, no ADT-4 filed |
| Material subsidiary auditor | The consolidated ICFR opinion relies on subsidiary auditors' reports for Indian subsidiaries (p.207); the specific identity/independence of those component auditors is NOT FOUND in the sections reviewed |

### Phase 5 Summary

| Item | Finding | Verdict |
|---|---|---|
| Board independence | 5 of 7 independent as at FY26-end; expanding to 9 members (4 exec/promoter-family) from 1-Apr-2026 | 🟡 |
| Attendance | 100% across all directors, all 5 board meetings and the AGM | 🟢 |
| Auditor fee ratio | Non-audit > audit fee, both years | 🟡 |
| CFO remuneration jump | +42.4%, unexplained, well above median | 🟡 |
| Promoter shareholding | Flat YoY on the one legible line; no pledge found; table otherwise scrambled | 🟡 (data-quality caveat, not a governance finding per se) |
| Whistleblower / fraud / SEBI | Clean across all checks | 🟢 |
| Post-year-end board expansion | Two more promoter-family directors added 1-Apr-2026 | 🟡 |

**Phase 5 verdict: 🟡 WATCH.** Kill Switch Assessment (informational): a human reviewer would NOT stop here. Nothing rises to fraud, pledge, promoter-selling, or SEBI-action level. The board's post-year-end expansion toward more promoter-family seats, alongside the unexplained CFO pay jump and the insider-lending pattern already flagged in B02, together form a coherent "watch the family/governance balance" theme worth carrying into the promoter-verdict work at Role 2/B08.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER (read with full knowledge of Phases 1-5)

### 6A. Narrative vs Reality

| Claim (Chairman's Message, p.6-7) | Cross-checked against | Verdict |
|---|---|---|
| "Our most significant strategic development this year was the acquisition of Cryptas... a leading digital trust and PKI solutions provider... marks eMudhra's formal and purposeful entry into the European market" | Confirmed: Cryptas acquisition completed 1-Jul-2025, entire Rs 1,315.25 Mn purchase price in goodwill (Note 4a). Revenue contribution not separately disclosed (Load-Bearing Fact 1). | ✅ Directionally true, but the AR gives no way to size "how significant" in revenue/profit terms independently |
| "This milestone completes a critical arc in our global presence... from the Americas and Asia-Pacific, through the Middle East and Africa, and now firmly into Europe" | International revenue 64% of FY26 total, +38.7% YoY, confirmed in MD&A | ✅ Consistent with disclosed numbers |
| "eMudhra is now actively advising global enterprises on post-quantum cryptography strategy" | No revenue line, contract count, or customer name tied to PQC advisory anywhere in the financial or segment sections | ⚠️ Unverifiable from financials — a capability claim, not a disclosed revenue driver |
| "Almaty office in Kazakhstan, marking eMudhra's entry into Central Asia" | Repeated once more in Director's Report (p.87-ish) with identical wording; **no Central Asia revenue, customer count, or segment data anywhere else in the AR** | ⚠️ See 6E — silent drop |
| "MOSIP certification... enabling us to power population-scale digital identity infrastructure across Africa" | **No Africa-specific revenue, contract, or DPI-program financial disclosure anywhere else in the AR** | ⚠️ See 6E — silent drop |
| "Product innovation and strategic consolidation... a cohesive, integrated Digital Trust Platform" | Consistent with the Products/Services section (MD&A p.143) listing emSigner, CertiNext/emCA, SecurePass, Trust Services as an integrated suite | ✅ Consistent |
| "Our people remain our greatest strength" | Employee count grew modestly (851→861 group-wide, +1.2%; India permanent 604), median remuneration rose 7.1% — consistent with a stable, not explosively growing, workforce given 35% revenue growth (i.e., growth via acquisition and productivity, not headcount) | ✅ Consistent, though the "greatest strength" framing sits oddly next to headcount growing only 1.2% while revenue grew 35% — a productivity story, not a headcount story, which the letter does not explicitly say |

### 6B. Strategic Priorities

Five-pronged strategy stated in MD&A (p.148, not the Chairman's letter itself, but the operational articulation of the same themes): (1) maintain Indian Trust Services leadership, (2) enhance solution offerings, (3) grow overseas via partnerships/acquisitions, (4) expand share of wallet with existing customers, (5) R&D focus on GenAI/converged identity. **Capital allocated**: two acquisitions (Rs 629.03 Mn net) plus organic capex (~Rs 1.2 Bn implied) directly funds priorities 2, 3, 5. **Execution evidence**: existing-customer revenue share 67%, international growth 38.7%, 240 new enterprise customers added (p.148) — these are specific, checkable metrics, a positive sign that the strategy section is not pure narrative.

### 6C. Metrics Showcased vs Conspicuously Absent

**Showcased** (front-matter highlights, p.55): Total Income, EBITDA, EBIT, Net Profit, Adj. EBITDA, Adj. Net Profit, Cash Flow from Operations, Dividend — all growth-positive metrics.

**Conspicuously absent from the front-matter highlights**: **Free cash flow** (which turned negative this year), **ROCE/ROE** (which compressed to 13-15%), **goodwill as % of net worth** (which jumped to 32.3%), and **any acquisition-specific performance metric** (Cryptas standalone revenue/profit, synergy realisation, integration cost). The front-matter dashboard leads with growth and profitability metrics that all look strong; it is silent on every metric Phase 3 flagged as a genuine watch item this year.

### 6D. Tone and Priority Drift vs Prior Year

Not independently assessable without the FY25 Chairman's letter in this pass (FY25 AR is available at inputs/other/Annual_Report_2025.txt per the run's backward-depth allowance, but was not read in this pass given time constraints — flagged as a possible extension for a verifier). Within FY26 alone, the tone is consistently confident/expansionary across the Chairman's letter, "Year in Review," and "Looking Ahead" sections, with no discernible internal drift.

### 6E. Quiet Abandonment Check (mandatory)

Reading the Chairman's Message and "Looking Ahead" section (front matter) side by side with the segment/MD&A/financial-statement operational sections:

**Finding 1 — SILENT DROP: Kazakhstan/Central Asia entry.** The Chairman's letter states: *"We established our Almaty office in Kazakhstan, marking eMudhra's entry into Central Asia — a region undertaking ambitious national digitalisation programmes where our trust infrastructure capabilities are uniquely well-suited."* This claim is repeated near-verbatim in the Director's Report (p.87-ish: "We also opened our presence in Central Asian Region... through our office in Kazakhstan"). **Operational section it should show up in**: the geographic segment note (Note 49) reports only India vs "Outside India" as the revenue split, with no APAC/MEA/Central-Asia breakdown; the MD&A gives no Central Asia revenue, customer, or contract figure anywhere. Classification: **(b) silent drop** — the opening narrative names an "entry" as a milestone, but zero operational data anywhere in the AR quantifies or even re-mentions it once. Materiality: **LOW** on its own (a single new office is not thesis-critical), but it is one of two instances of the same pattern (see Finding 2), which raises the materiality of the *pattern* to **WATCH**: this AR tends to announce geographic "entries" as strategic wins without ever circling back to size them.

**Finding 2 — SILENT DROP: MOSIP/Africa DPI claim.** The Chairman's letter states: *"our MOSIP certification this year was a landmark achievement, enabling us to power population-scale digital identity infrastructure across Africa... positions eMudhra as a foundational partner in building sovereign digital public infrastructure across some of the world's fastest-growing economies."* **Operational section it should show up in**: no Africa-specific revenue, no named African government contract, no DPI-program financial figure appears anywhere in the MD&A, segment note, or risk section. The only other AR mentions of MOSIP/Africa are event-listing references (e.g., "MOSIP Connect 2026 — Rabat, Morocco," a conference attendance note, not a business result). Classification: **(b) silent drop**. Materiality: **LOW-MODERATE** — "population-scale" and "foundational partner" language is strong for a claim with zero quantified follow-through anywhere else in a 369-page document; if this DPI/Africa opportunity is genuinely early-stage (which is plausible for a "landmark achievement... this year"), the letter's language overstates current traction relative to what the rest of the AR can support.

**No implicit retraction or hedged retreat was found** — nothing in the operational sections actively contradicts or walks back a Chairman's-letter claim; the pattern here is entirely omission (silent drop), not contradiction. The core Cryptas/Europe claim (the letter's headline item) IS operationally supported (goodwill, intangibles, segment revenue growth all tie out), which is the important asymmetry: **the one claim with real capital behind it (Cryptas) is the one claim the financials substantiate; the two claims that are narrative-only (Kazakhstan, MOSIP/Africa) are also the two claims with no operational follow-through.** This is consistent, not random — it suggests the AR's front matter is honest about scale (big capital commitment = big disclosure; small/early moves = narrative-only, un-sized mentions) rather than systematically oversold.

### Phase 6 Summary

**Phase 6 verdict: 🟡 WATCH.** The Chairman's letter is directionally consistent with the financials on its central claim (Cryptas/Europe) and reasonably disciplined in not over-claiming on its two smaller geographic items (they are flagged as silent drops, but the language, while enthusiastic, does not claim specific financial results that the financials then contradict). The front-matter metrics dashboard is one-sidedly growth-positive and omits every metric this stage flagged as a genuine watch item (FCF, ROCE/ROE, goodwill ratio) — standard AR practice, but worth naming.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP** | **WATCHLIST** | (1) Revenue/PAT growth strong (35.1%/26.1% consolidated) and durable-looking (existing-customer share 67%, 240 new enterprise customers); (2) but ROCE/ROE sit at only 13-15% this year, and at a reported ~44x TTM P/E (company memory) the "Reasonable Price" half of GARP is not obviously satisfied by anything in this AR — the multiple has to be earned by future margin/ROCE recovery once the acquisition-heavy balance sheet starts generating full-year returns, which the AR gives no disclosed timeline for; (3) the mix-shift engine (Enterprise Solutions Outside India, 62.4% of revenue, +38.3% YoY) is real and AR-confirmed, supporting the "growth" half of the thesis, but the FCF turn negative this year and the unquantified 3i Infotech/goodwill-impairment tail risks are the kind of things that can derail a GARP re-rating story if they crystallise. |
| **Turnaround** | **FAIL** | (1) This is not a turnaround situation — PAT, revenue, and margins are all growing, not recovering from a decline; (2) no distressed-asset, restructuring, or balance-sheet-repair narrative anywhere in the AR; (3) the closest "turnaround-adjacent" element is the CCA-guideline-driven business-model change (July 2024, DSC stock repurchase) which pressured standalone COGS, but this is a regulatory adjustment already substantially absorbed, not an ongoing turnaround. |
| Value+Quality | WATCHLIST | Quality signals are mixed: clean audit/no fraud/no leverage (quality) vs modest ROCE and two large undisclosed judgment items (goodwill, earn-out) that sit against "quality" of earnings; value assessment is outside this AR's scope (no valuation data here). |
| Capex-Led Growth | WATCHLIST | Capex more than doubled YoY (Rs 832.02 Mn → Rs 1,853.68 Mn) and is running 5.4x depreciation — a genuine capex-led-growth year, but funded partly by cash drawdown (FCF negative) rather than purely by internal accruals, and the capex mix (goodwill/intangibles from M&A vs organic PP&E) matters for how "capex-led" this really is in the traditional sense. |
| Cash Flow Compounder | FAIL (this year) | FCF turned negative this year for the first time in the two years shown; CFO/PAT remains healthy (>1x) but the compounding story is interrupted by the acquisition/capex programme this year. |
| Contrarian | WATCHLIST | The 3i Infotech claim and the two silent-drop geographic claims (Phase 6E) could support a contrarian "market is overreacting to noise, not fundamentals" read, or equally a contrarian bear case ("undisclosed tail risk the market hasn't priced") — the AR alone does not resolve which reading is correct; needs live verification (per Spear Gate). |
| Insider Confidence | WATCHLIST | Promoter shareholding flat YoY (no selling signal); but new insider lending INTO the company (promoter entity + Executive Chairman funding two overseas subsidiaries, Rs 82.87 Mn, first instance) is an unusual, non-standard signal that cuts against "arm's length treasury discipline" even though it is technically insider capital SUPPORT, not extraction. |
| Guidance Divergence | WATCHLIST | The AR itself contains no numeric FY27 guidance to check for divergence; the concall-sourced guidance (15-18% organic, 25-30% PAT) cannot be checked against this document — this is a genuine gap for this strategy lens specifically, since it depends entirely on outside-AR sources this stage does not verify. |

**GARP and Turnaround given fullest reasoning per the operator's mandate — done above.**

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company Snapshot

eMudhra Ltd, FY2025-26 (year ended 31-Mar-2026), consolidated: Revenue Rs 7,015.80 Mn (+35.1%), Total Income Rs 7,131.79 Mn (+35.1%), PAT Rs 1,100.38 Mn (+26.1%), PAT attributable to owners Rs 1,077.92 Mn (+27.4%), Basic EPS Rs 13.14 (+26.2%). Total Assets Rs 12,134.33 Mn (+39.8%), Total Equity Rs 9,125.90 Mn (+22.1%), near-zero leverage (D/E 0.026x, net cash). Two acquisitions completed (Cryptas International GmbH, AI Cyberforge Inc., both 1-Jul-2025). FCF turned negative (Rs -52.5 Cr) for the first time in the two years shown, driven by capex more than doubling.

### Phase-Wise Verdict Summary

| Phase | Verdict | One-line reason |
|---|---|---|
| 1 — Auditor/CARO | 🟡 WATCH | Clean opinion, no going concern, no fraud; sole CARO exception is small persistent PF arrears; non-audit fee exceeds audit fee both years |
| 2 — Notes | 🟡 WATCH | 15/15 triple-pass findings verified, 0 discrepancies; core business clean; two acquisition-related judgment items (goodwill, earn-out) undisclosed on sensitivity |
| 3 — Financials | 🟡 WATCH | Cash-flow quality checks clean (CFO/PAT >1x); FCF turned negative; ROCE/ROE modest (13-15%) against an acquisition-inflated balance sheet |
| 4 — Risk/MD&A | 🟡 WATCH | Above-average risk-section specificity; but 3i Infotech claim and Cryptas earn-out risk conspicuously absent from an otherwise detailed risk section |
| 5 — Governance | 🟡 WATCH | Clean attendance/whistleblower/fraud record; board expanding toward more promoter-family seats post-year-end; unexplained 42.4% CFO pay jump |
| 6 — Chairman's letter | 🟡 WATCH | Central Cryptas/Europe claim substantiated by the financials; two smaller geographic claims (Kazakhstan, MOSIP/Africa) are silent drops with zero operational follow-through |
| 7 — GARP best fit | WATCHLIST | Growth and mix-shift engine real and AR-confirmed; ROCE/ROE and FCF this year do not yet support the "reasonable price" half without a disclosed forward path |

### Overall Quality Score: 6/10

| Component | Weight | Score /10 | Basis |
|---|---|---|---|
| Governance | 25% | 6 | Clean fraud/whistleblower/attendance record; auditor fee-ratio flag; unexplained CFO pay jump; promoter-family board expansion post-year-end; scrambled shareholding table limits full verification |
| Accounting quality | 25% | 6 | Reconciled directly with B02's triple-pass score; clean core policies, real disclosure gaps on the two largest new judgment items |
| Balance sheet | 25% | 6 | Near-zero leverage, net cash, clean cross-ties on every check performed; but goodwill now 32.3% of net worth and ROCE/ROE compressed to 13-15% |
| Earnings quality | 25% | 6 | CFO/PAT >1x both years, no exceptional items, immaterial other income; but FCF turned negative and the useful-life extension is a real, quantified P&L-flattering choice timed with the acquisition build |
| **Overall** | | **6/10** | A clean, low-leverage, genuinely-growing operating business carrying real disclosure gaps and cash-conversion strain specific to this year's acquisition programme — not evidence of misstatement, but real enough to weigh in position sizing |

### Top 3 Strengths

1. **Clean control environment**: unmodified opinions on both reports, no going-concern language, no fraud (CARO xi clean both entities), no whistleblower complaints, no SEBI action against any director, near-zero leverage (D/E 0.026x, net cash position) — auditor's report at p.202/293, CARO at p.303-308.
2. **Real, granular growth engine**: international revenue +38.7% (64% of FY26 total), Enterprise Solutions Outside India +38.3% to Rs 4,375.72 Mn (62.4% of revenue), 240 new enterprise customers, 67% existing-customer revenue share — all directly stated and internally consistent across MD&A and segment note (Note 49, MD&A p.148/151).
3. **Cash-earnings quality intact despite the FCF dip**: CFO exceeded PAT in both years (1.21x FY26, 1.16x FY25), no exceptional items in either year, other income immaterial (1.6% of total income) — the negative FCF this year is a capex/M&A-timing story, not a cash-earnings-quality story (Cash Flow Statement, p.216-219).

### Top 3 Red Flags

1. **Cryptas contingent-consideration structure is uncapped on the upside (10x EBITDA, no ceiling) with a 2028-2030 49%-stake option repeating the same mechanic, and carries no Level 3 fair-value sensitivity disclosure** — the largest, least-bounded forward liability in the corpus, and it does not appear anywhere in the MD&A risk section (Note 4a(c)/17a/53(b), consol p.243/255/290-291; absence confirmed in Phase 4B).
2. **The 3i Infotech claim (>Rs 128 Cr, ~14% of net worth if it crystallised) is fully excluded from the quantified contingent-liability total on management's own unsupported assessment, and is entirely absent from the MD&A risk section** despite the chronology running to three weeks before the audit sign-off (Note 36(f)/38(e); MD&A p.153-163).
3. **Goodwill nearly tripled to Rs 2,940.46 Mn (32.3% of net worth) with no disclosed impairment-test discount rate, growth rate, or headroom**, and the useful-life extension on intangibles (cutting FY26 amortisation ~Rs 39.96 Mn) is timed with the same acquisition-driven asset build — the two largest new judgment items on the balance sheet both fall short of the disclosure standard the company demonstrably applies elsewhere in the same AR (e.g., the gratuity actuarial note) (Note 4a/2.5a/5a(iii)(a); B02 Pattern B).

### Key Monitorables for Next Quarter/Year

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| Cryptas actual EBITDA vs the implicit 10x contingent-consideration target | Any disclosed movement in the Rs 881.45 Mn liability | FY27 quarterly results / FY27 AR Note 17a/47/48 | Directly sizes the largest unbounded forward liability |
| 3i Infotech claim status | Escalation beyond the 23-Apr-2026 legal notice; any SEBI complaint filed | Reg 30 filings (quarterly), FY27 AR Note 36/38 | ~14% of net worth if it moves from denied to probable |
| Goodwill impairment test assumptions | Whether FY27 AR discloses discount rate/growth rate/headroom (currently absent) | FY27 AR, Note on goodwill impairment | Tests whether this year's disclosure gap was one-off or a pattern |
| MSME >3-year overdue balance | Whether the frozen Rs 21.61 Mn finally moves | FY27 AR Note 40/43, standalone CARO vii(a) | Two-year non-resolution is itself the finding; a third year would harden it |
| Free cash flow trend | Whether FY27 FCF returns positive as Cryptas moves to a full year and capex normalises | FY27 AR/quarterly cash flow statements | Tests whether this year's FCF dip was transition-year-specific or a new pattern |
| ROCE/ROE trend | Whether ROCE recovers above the 13-15% FY26 print as acquisitions mature | FY27 AR key ratios | Tests the capital-efficiency thesis implicit in the acquisition strategy |
| Effective tax rate | Whether consolidated ETR drifts from 16.2% toward the standalone 25.5% print as jurisdiction mix shifts | FY27 AR Note on tax reconciliation | Meaningful swing factor for any forward EPS model |
| CFO remuneration | Whether the 42.4% FY26 increase repeats or was a one-off | FY27 AR Board's Report §25 | Currently unexplained; a repeat would be a governance signal |
| Board composition | How the 4 executive/promoter-family-of-9 structure functions post 1-Apr-2026 expansion | FY27 Corporate Governance Report | Tests whether independent-director influence is diluted in practice |

### One-Line Verdict

**PROCEED WITH FLAGS (informational, best-fit strategy GARP-Watchlist)**: a clean-control, genuinely-growing digital-trust platform business carrying real, undisclosed acquisition-accounting tail risk (Cryptas earn-out, goodwill) and a 3i Infotech legal claim entirely omitted from its own risk narrative — worth the depth this AR shows, priced at a level (per company memory, non-anchored) that requires the ROCE/FCF story to recover from this year's acquisition-driven dip, which the AR itself gives no disclosed path or timeline for.

---

## NOTES FOR DOWNSTREAM STAGES

- **B01/screener FCF reconciliation gap** (Load-Bearing Fact 2): the AR's own cash flow statement ties cleanly to the screener's -Rs 52 Cr figure (CFO Rs 1,328.49 Mn − capex Rs 1,853.68 Mn = -Rs 525.19 Mn); B01's +Rs 51.4 Cr figure could not be reconstructed from any combination of face-statement lines tried in this pass. Flagged for a B01/verifier cross-check rather than resolved here.
- **Auditor "Other matters" Rs 3.88 Mn (FY26) is not itemised** — a verifier with access to the standalone note (p.348, Note 32.1, also scrambled) may be able to extract more detail than this pass could from the pdftotext rendering.
- **Promoter/promoter-group shareholding table (consol p.248/252) is scrambled beyond confident row-by-row reconstruction** in both the pdftotext and mupdf renderings reviewed; a verifier with raster access to those specific pages (work/raster/AR2026/) could resolve the exact per-holder percentages if precision is needed beyond the "mid-50s%, flat YoY" read reached here.
- **Standalone PAT growth rate discrepancy** between the MD&A results table (p.150, implies +73.6%) and the standalone financial statements figures cited in B02 (+60.7%, Rs 270.45→434.86 Mn) is unresolved — worth a targeted verifier check of Note references.
- FY25 AR (inputs/other/Annual_Report_2025.txt) was not read in this pass beyond what B02 already cross-referenced; a fuller Phase 6D (tone/priority drift vs prior year) would benefit from a direct FY25 Chairman's-letter comparison if a verifier has budget for it.
