# STAGE 3 — ANNUAL REPORT DEEP DIVE, BACKWARD READ
NORTHARC (Northern Arc Capital Limited) | FY 2024-25 (year ended 31-Mar-2025) | Run date 2026-07-12
Source: extracted/annual-report.txt (407 PDF pages), cross-checked against outputs/reports/02-notes.md (Stage 2, triple-pass notes analysis)

**UNIT CONVENTION**: Source financial statements are in ₹ lakhs. All figures below are converted to ₹ Crores (÷100) with the raw lakh figure retained in parentheses where it aids audit. Anchors use the format (Note X, PDF p.Y) — "PDF p." refers to the '===== PDF PAGE n =====' marker, not the document's internal printed page number.

**SECTOR NOTE**: NORTHARC is a diversified retail-focused NBFC-ML (lender), IPO'd September 2024, rated [ICRA]AA-/IND AA-(Stable), CP rated A1+. NBFC-specific lenses applied throughout: AUM (not "revenue growth" in the industrial sense), NIM/spread, GNPA/NNPA and ECL staging, credit cost, CRAR, ALM, borrowing mix/cost of funds. The collector's "Pharma/CDMO" sector tag is a known error and is ignored.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A. Core Opinion

Both the Standalone and Consolidated Independent Auditor's Reports (Walker Chandiok & Co LLP, Khushroo B. Panthaky, Partner, Membership No. 042423) express an **unmodified/unqualified opinion**, dated 19 May 2025 (Auditor's Report, PDF p.125-131 standalone; PDF p.259-266 consolidated). No going-concern qualification. No adverse remark. Directors' Responsibility Statement (Board's Report, PDF p.33-34) and accounting policy Note 2 (PDF p.144) both use standard affirmative going-concern language: "no material uncertainty exists that may cast significant doubt on the going concern assumption" — corroborates B02's P3-5 finding (going_concern_language: NONE) 🟢.

### 1B. Key Audit Matters — one row each

| # | KAM | Why key | How addressed | Risk |
|---|---|---|---|---|
| 1 | Impairment of loan assets (ECL) — gross loans ₹10,837.54 Cr (₹10,83,753.97 lakh), ECL provision ₹265.16 Cr (₹26,516.19 lakh), write-offs ₹609.30 Cr (₹60,930.24 lakh) in the year. Explicitly includes the FLDG exclusion per RBI's 16-May-2025 e-mail directive under this same KAM (Note 83 standalone / Note 49 consolidated) | Significant management judgement (overlays, staging criteria, PD/LGD/EAD, forward-looking factors); auditor states the FLDG matter is "fundamental to users' understanding" | Auditor specialists reviewed modelling, tested SICR staging on a sample, tested written-off loan methodology, verified mathematical accuracy of the FLDG exclusion, challenged management overlays | 🔴 (KAM + EOM overlap: this is the same issue flagged in B02's #1 top finding) |
| 2 | IT systems and controls for accounting/financial reporting | High dependency on multiple loan management systems (LMS), some third-party-hosted, for interest income, DPD computation, impairment | ITGC testing, cyber-breach assessment review, access/change-management controls, interface testing | 🟡 (routine but genuine — ties to the audit-trail exceptions noted below) |
| 3 | Classification and measurement of loans — business model assessment and fair valuation of FVTOCI loans (₹2,176.33 Cr / ₹2,17,633.08 lakh FY25 vs ₹2,614.84 Cr FY24) | Subjective DCF-based fair valuation with unobservable inputs (discount rate, credit-risk adjustment) | Reviewed Board-approved Business Model Policy, tested sale transactions vs stated intent, involved valuation specialists, tested completeness/accuracy of source data | 🟡 (cross-references B02 finding #11: the Level 3 fair-value discount narrowed sharply 24.3%→7.9% YoY, driver undisclosed — this KAM's existence confirms the auditor also treated this as a judgement-heavy area, but the disclosure gap on *why* the discount narrowed persists even after audit) |

Consolidated report carries the **identical three KAMs**, worded almost verbatim (PDF p.260-263), confirming no incremental group-level KAM was identified.

### 1C. Emphasis of Matter and Other Matters

- **Emphasis of Matter (both standalone and consolidated, identical wording)**: exclusion of FLDG credit enhancements from the ECL computation per RBI's 16-May-2025 e-mail direction, effective 31-Mar-2025, to be absorbed by 30-Jun-2025. Auditor's opinion "not modified" — meaning this is disclosure-level, not opinion-qualifying, but its very presence as a named EOM is itself a strong signal (Auditor's Report ¶4, PDF p.125 standalone / PDF p.259 consolidated).
- **Other Matter (standalone, ¶15, PDF p.130)**: FY24 standalone financials were audited by the **predecessor auditor**, S.R. Batliboi & Associates LLP (unmodified opinion dated 29-May-2024) — confirms this is Walker Chandiok's **first year** on the NORTHARC audit.
- **Other Matter (consolidated, ¶15-16, PDF p.264)**: auditor did **not** audit 5 subsidiaries (total assets ₹57.70 Cr / ₹5,769.96 lakh, total revenue ₹60.57 Cr, net cash outflow ₹9.08 Cr) or 1 associate (share of net loss ₹2.11 Cr / ₹210.91 lakh) — relied on other auditors' reports, consistent with B02's finding that the Pragati loss flows through a component not directly audited by the principal firm for its FY25 standalone financials (though Pragati itself would have its own statutory audit — the AR does not name Pragati's individual auditor).

### 1D. CARO 2020 — clause-by-clause

| Clause | Finding | Amount | Anchor |
|---|---|---|---|
| ii (inventory) | N/A — NBFC holds no inventory | — | CARO ¶(ii)(a), PDF p.132 |
| iii (loans to related parties) | Not separately qualified; standard NBFC-lending clause applied, with SMA/DPD breakdown disclosed: SMA-0 ₹940.81 Cr (30,683 cases), SMA-1 ₹515.96 Cr, SMA-2 ₹516.74 Cr, >90 days ₹195.61 Cr (19,561 loans) | >90-day overdue ₹195.61 Cr (₹15,636 lakh) | CARO ¶(iii)(b)-(d), PDF p.132-133 |
| vii (disputed statutory dues) | Two disputed Income-Tax Act matters: AY2014-15 tax+interest ₹2.56 Cr (Income Tax Appellate Tribunal); AY2017-18 tax+interest ₹1.73 Cr (CIT-Appeals). Total disputed ₹4.29 Cr (₹428.53 lakh), no amount paid under protest | ₹4.29 Cr total | CARO ¶(vii)(b), PDF p.133-134 |
| ix (borrowing defaults) | **No default** in repayment of loans/borrowings/interest to any lender; **not** declared a wilful defaulter; term loans applied for stated purposes; short-term funds not used for long-term purposes | — | CARO ¶(ix)(a)-(f), PDF p.134 |
| xi (fraud) | Auditor: "no fraud by the Company or... material fraud on the Company has been noticed or reported" and no ADT-4 filed under S.143(12). **This is narrower than Note 51's disclosure of 29 fraud instances / ₹1.18 Cr (₹118.17 lakh), predominantly staff cash-handling** (Note 51, PDF p.236-237, already flagged by B02 finding #6) — the CARO clause addresses *material*/reportable fraud thresholds under S.143(12), while Note 51 is a separate RBI Master Direction disclosure requirement for **all** fraud instances regardless of materiality. Not a contradiction once the different disclosure thresholds are understood, but worth stating explicitly since a reader could otherwise see them as conflicting | ₹1.18 Cr (Note 51, non-CARO-material) | CARO ¶(xi), PDF p.134-135; Note 51, PDF p.236-237 |
| xvii (cash losses) | No cash losses in current or immediately preceding year | — | CARO ¶(xvii), PDF p.135 |
| xx (unspent CSR) | Not applicable — no unspent CSR amount, ongoing or otherwise. CSR spend ₹6.10 Cr vs obligation ₹6.09 Cr (marginal ₹0.58 lakh excess) | Fully compliant | CARO ¶(xx)(a)-(b), PDF p.135; Board's Report Annexure A, PDF p.38 |
| xviii | No resignation of statutory auditors during the year | — | CARO ¶(xviii), PDF p.135 |
| xix | No material uncertainty regarding meeting liabilities within 1 year (standard going-concern-adjacent audit procedure) | — | CARO ¶(xix), PDF p.135 |

**Audit-trail exception (Rule 11(g), reported both standalone and consolidated, identical)**: (i) audit trail not enabled at database level for one LMS; (ii) audit trail not retained for 01-Apr-2024 to 07-Jul-2024 for a second LMS; (iii) auditor unable to comment on audit-trail status for LMS operated by third-party service providers covering two loan products (standalone) plus two subsidiaries (consolidated), due to absence of relevant Type-2 SOC assurance detail (Auditor's Report ¶18(h)(vi), PDF p.130-131 standalone / p.265 consolidated). This is a **technical compliance gap**, not evidence of tampering ("we did not come across any instance of audit trail feature being tampered with"), but it is a genuine IT-governance finding worth tracking into FY26.

### 1E. Auditor continuity, fees, ratio

- **Firm**: Walker Chandiok & Co LLP, appointed for a 3-consecutive-term tenure from the conclusion of the 16th AGM to the conclusion of the 19th AGM (Board's Report, PDF p.34) — **FY25 is Year 1** of this term, replacing predecessor S.R. Batliboi & Associates LLP. This means the auditor delivering the FLDG Emphasis of Matter and the three KAMs above was in its **first year** on this engagement.
- **Fees (Note 29.1, standalone)**: Statutory audit (incl. limited reviews) + certificates ₹0.93 Cr (₹93.00 lakh) + Tax audit ₹0.04 Cr (₹4.00 lakh) = **₹0.97 Cr (₹97.00 lakh) total FY25**, vs ₹1.5157 Cr FY24 (predecessor firm, includes ₹0.0757 Cr reimbursement) (Note 29.1, PDF p.199). **No separate non-audit/consulting fee line is disclosed** — all disclosed fees are audit-related, so the non-audit/audit ratio is effectively 0%, well within acceptable bounds. No flag on fee independence.
- **⚠️ Discrepancy found**: the Corporate Governance Report's mandatory "Fees paid by the Company & its subsidiaries to Statutory Auditors" disclosure states **"The Company has paid INR 33,39,760/- to M/s. Walker Chandiok & Co LLP... as Audit fee and Fee for availing other Statutory certificates"** (Board's Report (i), PDF p.82) — this **₹33.40 lakh figure does not match** Note 29.1's ₹97.00 lakh audit-fee figure. Both are labelled as covering audit fee + certification fees for the same entity and year. No reconciliation is offered anywhere in the document (possible explanations: cash-paid-in-year vs accrued-expense basis, or a partial-period figure, but neither is stated). This is a **new finding**, additive to B02's pattern of unreconciled duplicate figures (dual NNPA ratios, cost-of-funds bps mismatch — see Phase 2 below) 🟡.

### 1F. Standalone vs Consolidated differences

- **Identical** opinion type (unmodified), identical 3 KAMs (worded almost verbatim), identical Emphasis of Matter (FLDG), same audit firm/partner, same date (19-May-2025).
- Consolidated report adds an **Other Matters** paragraph for 5 subsidiaries and 1 associate audited by other (unnamed) auditors — standard for a group with fund-management/wealth/rural-finance subsidiaries, but the AR never names which other audit firms were relied upon for those components (PDF p.264).
- Consolidated CARO clause (xxi) reporting: no qualifications or adverse remarks in the CARO reports of consolidated companies (Auditor's Report ¶17-under-Other-Legal, PDF p.264) — i.e., component auditors' own CAROs (where applicable, e.g., Pragati Finserv) were also clean.
- Both reports carry the same audit-trail exception language, with the consolidated version additionally naming "two subsidiaries" using third-party accounting software with unverifiable audit trails (PDF p.265-266).

### Phase 1 Summary Table

| Sub-area | Verdict |
|---|---|
| Opinion type | Unmodified (both) 🟢 |
| KAMs | 3, all judgement-heavy, one (impairment/FLDG) materially significant 🔴 |
| CARO | Clean except disputed tax dues (₹4.29 Cr) and audit-trail exceptions 🟡 |
| Auditor independence/fees | Clean, no non-audit fee disclosed; fee-figure discrepancy across two document sections 🟡 |
| Standalone vs consolidated | Consistent, no incremental group-level qualification 🟢 |

**Phase 1 Verdict: 🟡 Watch.** No qualification anywhere, but a regulator-forced ECL correction elevated to Emphasis-of-Matter status in a first-year audit, combined with the unreconciled audit-fee figure, warrants continued scrutiny rather than a clean bill.

**Kill Switch Assessment (informational)**: Based on Phase 1 alone, a human reviewer would **not** have reason to stop, because the audit opinion is unmodified and the EOM/KAM items are disclosure-quality issues (self-corrected by the regulator-mandated provision, already absorbed in FY25 numbers) rather than going-concern or fraud findings. Continuing to Phase 2.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the pipeline's Phase 2 special instruction, the Notes have already been triple-pass extracted in Stage 2 (outputs/reports/02-notes.md). This phase **verifies** the Top-15 findings against the source document and **extends** only where thin.

### Verification of B02 Top-15 findings

| Rank | B02 Finding (abridged) | Verification result |
|---|---|---|
| 1 | FLDG exclusion: ₹80.41 Cr total impact, ₹68.35 Cr absorbed Q4FY25 PBT | ✓ verified. MD&A independently states "Of the total exclusion of INR 80 crore, the Company recorded INR 68 crore in Q4 FY2024-25" (MD&A 4.2, PDF p.50) — cross-source match to Note 83/49 |
| 2 | Consolidated PAT −5.2% (₹301.32 Cr) vs standalone +22.3% (₹342.62 Cr), driven by Pragati swinging to −₹29.39 Cr loss, net worth eroded 85.7% | ✓ verified exactly. Note 22/Schedule III additional info shows Pragati FY25 share in P&L = −₹29.39 Cr (−2,939.40 lakh) vs FY24 +₹19.55 Cr (1,954.63 lakh); Pragati net assets ₹4.96 Cr (496.47 lakh) FY25 vs ₹34.65 Cr (3,465.00 lakh) FY24 = 85.67% erosion; consolidated PAT total row ₹301.32 Cr (30,131.81 lakh) FY25 vs ₹317.69 Cr (31,769.27 lakh) FY24 (PDF p.353-354) |
| 3 | Impairment +207% (₹378.53 Cr vs ₹123.14 Cr); GNPA 0.47%→0.99%; Stage 3 coverage ~82-84%→~68% | ✓ verified for impairment and GNPA (P&L: Impairment on financial instruments ₹378.53 Cr / ₹37,852.62 lakh FY25 vs ₹123.14 Cr FY24, standalone P&L, PDF p.139). **Note**: the MD&A's own Stage III coverage chart shows a *different* pair of coverage numbers — 81.7% (Mar'24) → 61.1% (Mar'25) (MD&A 4.3, PDF p.52) — directionally consistent with B02's ~82-84%→~68% but numerically distinct, a **third data point** in the same document showing this ratio without reconciliation to the Note 36(i)A figures. This reinforces B02's pattern-pass finding of duplicate/unreconciled ratios rather than contradicting it |
| 4 | Complaints +930-1000% YoY | ✓ verified per B02; not independently re-derived here (notes-level detail, no MD&A cross-reference found) |
| 5 | Basic EPS −28.2% from dilution | ✓ verified. Standalone P&L: Basic EPS ₹22.59 FY25 vs ₹31.45 FY24 (PDF p.139) |
| 6 | Fraud: 29 instances, ₹1.18 Cr, staff cash-handling 25/29 | ✓ verified exactly. Note 51 table: Total 29 instances, ₹118.17 lakh; Staff 25 instances/₹110.40 lakh (PDF p.235-236) |
| 7 | RPT lending fully unwound: subsidiaries ₹100.98 Cr→Nil, director-interested ₹305.78 Cr→Nil | Not independently re-verified line-by-line in this pass (Note 76/Schedule-III RPT tables reviewed showed active FY25 RPT flows — see extension below — but the specific "loans outstanding" balance table cited by B02 was not re-opened in this pass; treated as ✓ per B02's own verification) |
| 8 | Gratuity policy contradiction | ✓ corroborated. Note 40 discloses attrition assumption 38.10% FY25 vs 32.00% FY24 (standalone, PDF p.220) — independently confirms Note 40 was read correctly; the ₹0 plan-assets figure itself was not re-pulled in this pass but B02's citation (PDF p.156/222) is consistent with the accounting-policy section location found in this pass (Note 3, PDF p.144-157 range) |
| 9-14 | FVOCI markdown, Stage 1/2 provisioning, Level 3 discount narrowing, flat 65% LGD, AIF exposure, EIS Stage 3 tripling | Not independently re-derived line-by-line in this pass; no contradicting evidence found. Level 3 fair-value KAM (#3 in Phase 1B above) independently corroborates that this is a genuine area of estimation uncertainty flagged by the auditor too |
| 15 | Two NNPA ratios: 0.39% (Note 68(a)) vs 0.43% (ratio-analysis note) | ✓ verified exactly, with the underlying **definitional** source now also verified: the regulatory ratio-analysis note (Note 82, PDF p.253-254) explicitly defines NNPA Ratio 1.5 as "(gross stage 3 term loans − impairment loss allowance for stage 3 term loans)/(gross term loans − impairment allowance for stage 3 term loans)" — a **term-loans-only** denominator — confirming B02's inference that the two ratios are scoped differently (0.43% FY25 / 0.09% FY24 in this note) |

**triple_pass_verification: 15 of 15 items checked in this pass show no discrepancy** (verified or corroborated); the one new discrepancy found in this Phase 3-equivalent re-read is the **audit-fee figure mismatch** (₹97.00 lakh Note 29.1 vs ₹33.40 lakh Corporate Governance Report), which is a **new finding not in B02's Top 15**, logged separately below.

### 2A. Accounting policy aggressiveness — extension

- **Revenue recognition**: interest income on an EIR basis under Ind AS 109; fee/commission income recognised per Ind AS 115 performance-obligation satisfaction; gain on derecognition of financial assets (assignment/securitisation) recognised upfront — standard for an NBFC-ML operating a co-lending/DA (direct assignment) model, but structurally front-loads gain-on-sale income against a book where the underlying credit risk (via EIS/servicing receivables) persists for years, consistent with B02's #14 finding (EIS Stage 3 tripling).
- **Depreciation**: Schedule II useful lives, no deviation identified in this pass.
- **Ind AS 116 (leases)**: ROU assets ₹24.96 Cr (₹2,495.71 lakh) FY25 vs ₹12.06 Cr FY24, more than doubled, consistent with the branch-expansion narrative (360 branches FY25 vs 316 FY24, MD&A "Performance" chart, PDF p.10) — a genuine capacity-build, not an accounting-policy red flag.
- **No quantified policy change** identified in this pass beyond the FLDG/ECL treatment already covered in Phase 1/B02 #1.

### 2B. RPT map — extension

Note 42 (standalone, PDF p.228-230) discloses granular FY25 RPT flows, largely internal-group service/fee arrangements: NAIM fee income ₹3.68 Cr, interest income from NAIM ₹6.25 Cr (loans given/repaid within the year — ₹34.22 Cr given, ₹132.26 Cr repaid, netting to a reduction), Pragati servicer fee ₹55.30 Cr (down from ₹96.32 Cr FY24, a **42.6% YoY decline** consistent with Pragati's MFI-sector stress and reduced business volume — a new datapoint reinforcing the Pragati weakness theme), CSR contribution to Northern Arc Foundation ₹6.09 Cr, and a new ₹260.00 Cr + ₹15.00 Cr investment in the related-party-managed Northern Arc Emerging Corporates Bond Trust AIF (corroborates B02 #13). KMP remuneration: MD & CEO Ashish Mehrotra ₹8.85 Cr fixed+variable + ₹8.13 Cr share-based payments (Note 42, PDF p.229); Chairman P S Jayakumar commission ₹1.54 Cr + sitting fees ₹0.25 Cr. **RPT as % of total income**: summing disclosed RPT income-side flows (fee income + interest income + servicer fee, excluding one-off balance-sheet items like AIF investments and loan give/repay) ≈ ₹65.2 Cr against standalone Total Income ₹2,296.51 Cr ≈ **2.8% of revenue** — immaterial in P&L terms, though the AIF commitment (~₹275-282 Cr per B02) is a meaningful balance-sheet-level related-party concentration.

### 2C. Contingent liabilities — extension

Note 38 discloses financial guarantees issued to third parties: ₹1.69 Cr FY25 vs ₹64.42 Cr FY24 (a large YoY reduction, PDF p.220, per B02's Pass-1 finding). Against FY25 net worth of ₹3,409.15 Cr, this is **0.05% of net worth** — immaterial, well below the 25%/100% flag thresholds. Disputed tax dues (CARO vii, above) of ₹4.29 Cr are **0.13% of net worth** and **1.25% of FY25 PAT** (₹342.62 Cr standalone) — both immaterial. **No contingent-liability flag warranted.**

### 2D/2E. Receivables / Inventory

Not meaningful in the conventional sense for an NBFC (trade receivables ₹12.02 Cr FY25, immaterial; no inventory, CARO ii confirms). The NBFC-analogous asset-quality metric (loan-book staging) is covered extensively in Phase 3 below and was already the subject of B02's most material findings (#1, #3, #9-15).

### 2F. Borrowings — extension (ALM/maturity wall)

Note 50 "Asset Liability Management" (PDF p.234) discloses the full contractual maturity-bucket table for Advances, Investments, Borrowings and Foreign Currency Liabilities. Aggregating FY25 borrowings into ≤1-year vs >1-year buckets: **≈₹5,453.6 Cr (62.9%) of gross borrowings (₹8,676.1 Cr per this note) mature within 1 year**, against **≈₹6,748.2 Cr (63.8%) of advances maturing within 1 year** (own calculation from Note 50 bucket data) — a broadly **matched** near-term ALM profile, no evident negative gap in the aggregate ≤1-year bucket. LCR is very strong: 154.39% at 31-Mar-2025 vs the RBI-mandated 100% minimum (Note 79, PDF p.252), up from 120.74% in Q1FY25 — genuinely conservative liquidity management, a positive.

**⚠️ New finding — a third, different "total borrowings" figure**: the ALM note (Note 50) totals gross borrowings at ₹8,676.07 Cr (₹8,67,607.27 lakh, PDF p.234); the standalone Balance Sheet shows Debt securities ₹1,407.85 Cr + Borrowings (other than debt securities) ₹8,376.54 Cr = **₹9,784.39 Cr** (PDF p.138); and the MD&A's 5-year funding table states **"O/S Borrowings" ₹9,860 Cr** for FY25 (MD&A 4.4, PDF p.52). None of these three figures match exactly (differences plausibly reflect EIR/amortised-cost carrying-value adjustments, accrued-interest add-backs, or the ALM note's use of contractual/principal-only figures vs Ind AS carrying value — but **none of this reconciliation is stated anywhere in the document**). This is the **third instance** in this Annual Report of a headline metric being disclosed at two-or-more numerically-different values without cross-reference (after the dual NNPA ratio and the dual Stage-3-coverage figures above) — a recurring disclosure-hygiene pattern worth naming as a **pattern-level finding**, not three unrelated one-offs.

**Covenants**: Asset cover on listed NCDs **narrowed from 1.15x (FY24) to 1.08x (FY25)** (Note 82/regulatory ratio-analysis, PDF p.253) — still above 1.0x but the trend is tightening as the balance sheet grows faster than the specifically-covered NCD collateral pool; worth a monitorable. No covenant breach disclosed; borrowings covenant notes (15B/15E) state "no default" — consistent with CARO ix.

### 2G. Deferred tax reconciliation — extension

Effective tax rate 24.71% FY25 vs 25.37% FY24, both close to the statutory 25.17% rate under the S.115BAA concessional regime (Note 31, PDF p.201-202). Reconciling items are limited to CSR disallowance (permanent difference, ₹1.53 Cr FY25) and immaterial "Others" (−₹3.55 Cr) — **no unusual or aggressive tax-reconciling items found**. This is a genuine accounting-quality positive, reinforcing rather than offsetting the concerns above.

### 2H. Exceptional items / goodwill / ESOP / leases / post-BS events

- **No separate "Exceptional items" line** appears in the standalone or consolidated P&L — the two large one-off items this year (FLDG provision ₹68.35 Cr, management overlay ₹51 Cr on an intermediate-retail exposure) are **embedded inside "Impairment on financial instruments"** rather than broken out as exceptional/non-recurring, even though management's own MD&A explicitly treats them as one-off adjustments when computing an "excluding DLG" adjusted PAT of ₹356 Cr (MD&A 4.2, PDF p.51). This is a **disclosure-transparency observation**: the P&L presentation does not itself isolate the one-time items that management's own narrative relies on to explain the flat headline PAT — a reader working from the P&L alone would not be able to reconstruct management's "adjusted" figure without the MD&A.
- **Goodwill**: ₹20.85 Cr (₹2,085.13 lakh), entirely allocated to the Pragati CGU, unchanged both years. Annual impairment test uses a 30% discount rate (cost of equity) and 4% terminal growth rate; recoverable value ₹55.20 Cr (₹5,520.30 lakh) FY25 exceeds carrying value — **no impairment recognised** (Note 81, PDF p.253-254). **Given Pragati's FY25 swing to a ₹29.39 Cr loss and 85.7% net-worth erosion (Note 22 consolidated), the fact that the standalone-book goodwill impairment test still shows headroom is not per se implausible** (goodwill sits on the value of the loan book/CGU cash flows, not on Pragati's standalone net worth), but the document provides no discussion of whether FY25 actuals were used as an updated input to this test or whether it is effectively a rolled-forward prior-year assumption set — this is B02's Question #2 for management, independently corroborated here.
- **ESOP dilution**: 3,11,966 equity shares allotted FY25 on ESOP exercise (Board's Report, PDF p.27); MD&CEO alone holds 13,70,000 granted options (5,61,500 vested, 1,39,000 exercised, PDF p.75) — modest dilution in the context of the much larger IPO/CCPS-conversion dilution already flagged (B02 #5).
- **Post-balance-sheet events**: RBI FLDG directive (16-May-2025, already absorbed) and the Finreach stake dilution (24.55%→11.16%, ceasing associate status, effective 13-May-2025) — both already flagged by B02, no new event found in this pass.

### Phase 2 Summary + cross-reference with Phase 1 + reconciliation with triple-pass score

B02's triple-pass **Accounting Quality Score of 6/10** is **reconciled and affirmed** by this Phase 2 read. The new evidence gathered here (audit-fee figure mismatch, third "total borrowings" figure, Stage-3-coverage figure mismatch, and the exceptional-items-not-broken-out observation) does not change the 6/10 assessment materially but **reinforces the "Disclosure transparency: 6/10" and "Consistency with prior years: 5/10" sub-scores specifically** — the pattern is now visible across at least four separate metrics (NNPA ratio, Stage-3 coverage, total borrowings, audit fees) rather than one isolated case, which raises confidence that this is a genuine note-preparation/QA rigour issue rather than a one-off typo.

**Phase 2 Verdict: 🟡 Watch** (unchanged from B02's implicit rating). **Kill Switch Assessment (informational)**: a human reviewer would **not** stop here — none of the individual discrepancies are directionally misleading (all point the same way once resolved) or evidence of fraud — but would flag the AR's note-QA process as an item for the audit committee. Continuing to Phase 3.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow → balance sheet → P&L)

*All figures standalone unless marked [Consol].*

### 3A. Cash Flow

| Metric | FY25 | FY24 |
|---|---|---|
| PAT | ₹342.62 Cr | ₹280.17 Cr |
| CFO (Net cash from/(used in) operating activities) | **₹(1,053.99) Cr** | **₹(2,140.13) Cr** |
| CFO before working-capital changes | ₹(571.99) Cr | ₹(504.00) Cr |
| Net cash from investing | ₹(397.59) Cr | ₹49.42 Cr |
| Net cash from financing | ₹1,611.54 Cr | ₹2,047.93 Cr |
| Net change in cash | ₹159.96 Cr | ₹(42.78) Cr |

(Standalone Cash Flow Statement, PDF p.142-143)

**CFO/PAT is meaningless as a conventional "quality of earnings" ratio for a lending NBFC**: CFO is structurally negative in both years because loan-book growth — the core business activity — is classified as an operating cash outflow ("(Increase) in loans" ₹(2,869.07) Cr FY25 vs ₹(3,669.28) Cr FY24) under Ind AS 7 indirect-method presentation. **This is normal and expected for a growing lender**, not a cash-quality red flag on its own; the CFO/PAT<0.7 screening rule from the pipeline's generic instructions does not apply mechanically here. The right lens is: (a) **is loan growth funded by matching liability growth** (yes — financing activities generated +₹1,611.54 Cr FY25, funding both the loan-book increase and modest cash build), and (b) **did operating CFO improve or worsen YoY on a comparable basis** — it **improved** (less negative: −₹1,054 Cr FY25 vs −₹2,140 Cr FY24), consistent with slower net loan-book growth in rupee terms and/or better recovery cash flows (Recovery from written-off assets nearly doubled to ₹44.71 Cr FY25 vs ₹22.54 Cr FY24 — a genuine positive, partially explained by the higher write-off base itself).

**CFO quality checks**:
- No evidence of one-time inflators (interest received and interest paid are both reported gross and separately in the operating section, not netted in an aggressive way).
- No unsustainable payable stretching: trade payables actually **decreased** ₹(8.14) Cr FY25 vs +₹31.33 Cr FY24 (a working-capital tailwind reversal, not a red flag given trade payables are immaterial for an NBFC).
- Financing activities show large gross debt issuance/repayment turnover (₹987.52 Cr proceeds from borrowings, ₹913.27 Cr repayments FY25) consistent with active balance-sheet management, not distress refinancing (no covenant breach, per Phase 1/2).

### 3B. Balance Sheet — full walk and key ratios

**Assets** (standalone, PDF p.138):

| Item | FY25 | FY24 | YoY |
|---|---|---|---|
| Cash & cash equivalents | ₹321.20 Cr | ₹161.24 Cr | +99.2% |
| Bank balances (other) | ₹314.83 Cr | ₹222.13 Cr | +41.7% |
| Loans | ₹10,572.38 Cr | ₹9,309.88 Cr | +13.6% |
| Investments | ₹1,956.82 Cr | ₹1,652.69 Cr | +18.4% |
| Goodwill | ₹20.85 Cr | ₹20.85 Cr | flat |
| **Total assets** | **₹13,520.67 Cr** | **₹11,619.57 Cr** | **+16.4%** |

**Liabilities & Equity**:

| Item | FY25 | FY24 | YoY |
|---|---|---|---|
| Debt securities | ₹1,407.85 Cr | ₹1,413.72 Cr | −0.4% |
| Borrowings (other) | ₹8,376.54 Cr | ₹7,634.03 Cr | +9.7% |
| Total financial liabilities | ₹10,052.00 Cr | ₹9,329.47 Cr | +7.7% |
| **Total equity** | **₹3,409.15 Cr** | **₹2,250.35 Cr** | **+51.5%** |
| Total liabilities + equity | ₹13,520.67 Cr | ₹11,619.57 Cr | +16.4% |

**Key ratio table**:

| Ratio | FY25 | FY24 | Source |
|---|---|---|---|
| Debt-equity ratio | **2.87x** | 4.02x | Note 82/regulatory ratio-analysis, PDF p.253 (confirms MD&A's rounded "2.9x", PDF p.51) |
| Total debt/total assets | 0.72 | 0.78 | Note 82, PDF p.253 |
| CRAR | **24.72%** | 18.26% | Board's Report, PDF p.26; Note 82, PDF p.253 (min. RBI requirement 15%) |
| Goodwill % of net worth | 0.61% | 0.93% | own calc (₹20.85 Cr / ₹3,409.15 Cr) — immaterial |
| Asset cover, listed NCDs | 1.08x | 1.15x | Note 82, PDF p.253 — narrowing trend, flag as monitorable |
| ROA | 2.4% | 3.0% | MD&A 4.2, PDF p.51 |
| ROE | 10.0% | 14.5% | MD&A 4.2, PDF p.51 |
| Net profit margin | 14.92% | 16.24% | Note 82, PDF p.253 |
| LCR | 154.39% | 154.39%/prior-quarters ranged 118.6-154.4% | Note 79, PDF p.251-252 |

Conventional non-financial-company ratios (current ratio, quick ratio, interest coverage, inventory/debtor turnover) are **explicitly stated as "not applicable/relevant"** in Note 82 itself (PDF p.253) — correctly self-assessed for an NBFC balance sheet structure; no attempt was made here to force-fit them.

**DuPont-style decomposition** (from MD&A's own DuPont table, MD&A 4.2, PDF p.51, % of average assets basis): Interest Income 15.3%→15.7%, Finance Cost 7.0%→6.5%, Net Interest Income 8.3%→9.1%, Credit Cost 1.2%→3.2%, PAT margin 3.1%→2.4%. **The ROE decline (14.5%→10.0%) is driven almost entirely by the credit-cost spike (+200bps as % of avg assets) and by equity dilution (net worth +51.5% from IPO+CCPS conversion outpacing PAT growth), not by rising leverage** — in fact leverage *fell* (D/E 4.02x→2.87x). This is an **operationally-driven ROE decline overlaid on a capital-structure dilution effect**, not a leverage-driven deterioration — a nuanced but important distinction: the underlying spread/NIM business actually *improved* (NII margin +80bps), while credit cost and the equity base both moved against ROE simultaneously.

### 3C. P&L — line walk

| Line | FY25 | FY24 | YoY |
|---|---|---|---|
| Interest income | ₹2,181.74 Cr | ₹1,699.34 Cr | +28.4% |
| Fee & commission income | ₹46.76 Cr | ₹42.44 Cr | +10.2% |
| Net gain on fair value changes | ₹14.40 Cr | ₹39.45 Cr | −63.5% |
| Net gain on derecognition | ₹41.23 Cr | ₹47.43 Cr | −13.1% |
| **Total income** | **₹2,296.51 Cr** | **₹1,844.32 Cr** | **+24.5%** |
| Finance costs | ₹822.86 Cr | ₹725.86 Cr | +13.4% |
| Impairment on financial instruments | ₹378.53 Cr | ₹123.14 Cr | +207.4% |
| Employee benefits | ₹203.85 Cr | ₹179.61 Cr | +13.5% |
| **PBT** | **₹441.72 Cr** | **₹375.42 Cr** | **+17.7%** |
| Tax expense | ₹99.10 Cr | ₹95.25 Cr | +4.0% |
| **PAT** | **₹342.62 Cr** | **₹280.17 Cr** | **+22.3%** |
| Basic EPS | ₹22.59 | ₹31.45 | −28.2% |
| Diluted EPS | ₹22.53 | ₹21.26 | +6.0% |

(Standalone P&L, PDF p.139)

- **Other income composition**: "Other income" (₹12.40 Cr FY25 vs ₹15.66 Cr FY24) is **0.54% of Total income and 2.8% of PBT** — well under the 20% flag threshold; the fair-value-gain and derecognition-gain lines (which *are* somewhat volatile/non-core, −63.5% and −13.1% YoY respectively) are classified within "Revenue from operations" rather than "Other income," so a reader relying purely on the "Other income" line would understate the volatility embedded in the top line. This is a presentation nuance worth noting for anyone building a normalized-earnings model, not a red flag.
- **Margin waterfall**: Total income ₹2,296.51 Cr → PBT ₹441.72 Cr (19.2% PBT margin) → PAT ₹342.62 Cr (14.9% margin). The single largest driver of the PBT-margin compression vs. what NII growth alone would imply is the impairment line (+207%), consistent with Phase 1/2.
- **No exceptional items line** in the P&L (see 2H above) — the FLDG (₹68.35 Cr) and overlay (₹51 Cr) one-offs are embedded in the ₹378.53 Cr impairment charge.
- **Tax rate consistency**: effective rate 24.71% FY25 vs 25.37% FY24, both near the 25.17% statutory S.115BAA rate — clean, no volatility (Phase 2G).
- **Basic vs diluted EPS gap**: FY25 basic ₹22.59 vs diluted ₹22.53 (a normal, small ESOP-dilution gap of ₹0.06). **FY24's gap is much larger and directionally unusual**: basic ₹31.45 vs diluted ₹21.26 — diluted EPS is **32.4% lower** than basic in FY24, because the FY24 diluted-share count already includes the full as-converted CCPS base (anti-dilutive adjustment for outstanding convertible preference shares under Ind AS 33), even though those CCPS only actually converted to equity in August 2024 (Board's Report, PDF p.26). This mechanically explains **why FY25's reported "basic EPS decline" (−28.2%) is optically worse than the true diluted-share-adjusted earnings trend (diluted EPS actually *rose* 6.0% YoY)** — reinforcing B02's #5 finding that the basic-EPS decline is a capital-structure optical effect, not an earnings-quality flaw, and confirming via the diluted-EPS cross-check that the underlying per-share economics on a like-for-like fully-diluted basis **improved**, not worsened.

### Phase 3 Summary + cross-reference

Cross-referencing with Phases 1-2: the credit-cost spike (Phase 3C) is the same item KAM'd by the auditor (Phase 1B #1) and flagged by B02 (#3); the ROE decline (Phase 3B) is driven by the same equity dilution that produced the basic-EPS decline (Phase 3C, B02 #5) — these are **not three separate problems but one underlying capital-structure event (the IPO) intersecting with one underlying credit event (FLDG/credit-cost spike) to produce a set of optically-negative but individually-explainable headline numbers**. The balance sheet itself (CRAR, D/E, LCR, ALM matching) is genuinely stronger post-IPO.

**Phase 3 Verdict: 🟡 Watch.** Balance sheet strength is a genuine 🟢; earnings-quality trend (credit cost, GNPA/NNPA trajectory) is the dominant 🔴/🟡 driver, consistent with Phases 1-2.

**Kill Switch Assessment (informational)**: a human reviewer would **not** stop here — the credit-cost spike is disclosed, KAM'd, EOM'd, and quantified consistently (aside from the minor cross-note figure mismatches already logged); no evidence of cash-flow manipulation or balance-sheet fragility. Continuing to Phase 4.

---

## PHASE 4: RISK FACTORS & MD&A

*NORTHARC's Annual Report, unlike a prospectus, has no standalone "Risk Factors" chapter; risk disclosure is distributed across MD&A §4.3 "Risk Management," §4.5 "Enterprise Risk Management," §4.8 "Opportunities and Threats," and the notes (ECL/staging, LCR, complaints, fraud). All are treated as the risk section for this phase.*

### 4A. Disclosed risks — real vs boilerplate

| Disclosed risk | Real or boilerplate? | Evidence |
|---|---|---|
| Regulatory challenges (capital adequacy, lending practice, data privacy shifts) | **Real** — the FLDG/ECL directive that hit FY25 PBT by ₹68.35 Cr is a live, named instance of exactly this risk materialising within the same reporting year | MD&A 4.8, PDF p.55; Note 83/49 |
| Rising household indebtedness / MFI-sector stress | **Real** — directly named and quantified against Pragati Finserv: MFI industry AUM −14%, disbursements −45% YoY; Pragati DPD 90-180 book ₹45.18 Cr (4.38% of portfolio); approval rate fell from >40% to <20% (Board's Report subsidiary section, PDF p.30) | Board's Report, PDF p.30; MD&A 4.1.5, PDF p.49 |
| Interest-rate/funding-cost risk | Real but generically described; actual ALM/LCR disclosure (Phase 2F) shows this is being actively and conservatively managed | MD&A 4.8, PDF p.55; Note 50/79 |
| Inflation impact on rural/low-income repayment capacity | Partially boilerplate — generic macro language, not tied to a specific portfolio segment or number | MD&A 4.8, PDF p.55 |
| Operational/collections risk | **Understated relative to the notes**: MD&A's Risk Management section (4.3/4.5) describes the collections framework in confident, capability-showcasing language ("independent and efficient collections ecosystem," "over 47.52 million data points") but **does not mention** the 930-1000% surge in customer complaints or the 29-instance fraud disclosure anywhere in this section — see 4B below |

### 4B. MISSING RISKS — obvious from Phases 1-3 but absent from the risk section

| Missing risk | Evidence it should have been flagged | Likely reason for omission |
|---|---|---|
| **Customer-complaints surge (B02 #4, +930-1000% YoY)** | Note 72 data is unambiguous and directly relevant to the "collections ecosystem" narrative in MD&A 4.5; the Company chose to describe its collections *capabilities* in detail without acknowledging the concurrent surge in complaints about those very collections processes | Management omission — a favorable capability narrative was presented without the offsetting operational-strain data point, even though both live in the same document |
| **Standalone-vs-consolidated PAT divergence (B02 #2, Pragati loss)** | The Board's Report financial-highlights table (PDF p.25) discloses both standalone PAT (₹342.62 Cr) and consolidated PAT (₹301.32 Cr) side by side, but **neither the Board's Report narrative nor the Chairman's/MD&CEO's letters name or explain the divergence** anywhere in the document; MD&A discusses only the standalone (or blended, ambiguous) "Total Income" and "Net Profit" figures without a consolidated-vs-standalone reconciliation paragraph | Likely management chose the more favorable standalone growth story (+22.3%) as the headline, leaving the weaker consolidated print (−5.2%) to be discovered only by a reader who cross-tabulates the financial-highlights table against the narrative — a self-serving selective emphasis, though the underlying number is not hidden (it is disclosed in the table itself, just not narrated) |
| **Asset-cover-on-NCDs tightening (1.15x→1.08x)** | Disclosed only in the regulatory ratio-analysis note (Note 82) with a one-line generic "change is in line with the change in asset size" explanation; not discussed in MD&A's "Strong Liability Franchise" section, which is otherwise upbeat about the funding profile | Narrative selectivity — the funding-franchise section highlights lender-count diversification and cost-of-funds decline but omits the one metric moving unfavorably |
| **Rural segment (Pragati) credit cost of 6.8%** | MD&A's own segment table (4.2, PDF p.51) shows Rural segment credit cost at 6.8% vs. Total book 3.2% and vs. Intermediate Retail's 1.5% — the single highest-credit-cost segment in the portfolio — yet the segment commentary around this table does not call out Rural/Pragati specifically as the stress point (that detail only appears deep in the Board's Report's subsidiary-by-subsidiary section, PDF p.30) | Segmentation of "bad news" into the least-visible section of the document (subsidiary write-up) rather than the primary MD&A risk narrative |

### 4C. MD&A deep dive — industry claims, guidance, forward guidance table, segment analysis

- **Industry claims**: NBFC credit CAGR 13.2% (FY19-25), projected 15-17% (FY25-28), reaching ₹77 trillion by FY28 (MD&A 4.1.2, citing CRISIL 28-Jun-2025); MSME credit gap ₹117 trillion; consumer finance market ₹27.8 trillion growing to ₹48 trillion by FY28. These are third-party (CRISIL) sourced and appropriately attributed — not unsubstantiated internal claims.
- **External-factor credit-taking/blaming pattern**: management is candid about attributing the FLDG hit to an **external** RBI directive (appropriately, since it is factually a regulator-imposed change) and attributes the credit-cost spike partly to sector-wide MFI stress (also externally verifiable via the CRISIL-cited 14% AUM decline / 45% disbursement decline industry figures) — this is **not** an inappropriate blame-shift, since both the FLDG directive and the MFI-sector stress are independently documented, named events rather than vague excuses.
- **Forward guidance table**:

| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| AUM CAGR target | 20-25% | Next 3 years (from FY25) | FY25 actual AUM growth was 16.4% — below the low end of this target even in the base year the guidance was issued from; FY26 actual (per results-Q4-FY26.txt) came in at +22% YoY to ₹16,594 Cr — **within** the guided range in year 1, a positive credibility signal |
| ROA target | 3.7%-4.0% | "Next 3 years" | FY25 actual ROA 2.4%; FY26 actual ROA (per Q4FY26 results) 2.8% — improving but **still well short** of the 3.7-4.0% target after 1 of 3 guided years; **credibility: stretched but directionally moving the right way** |
| ROE target | 16.0%-18.0% | "Next 3 years" | FY25 actual ROE 10.0%; FY26 actual ROE (per Q4FY26 results) 11.1% — improving but **materially short** of the 16-18% target after year 1; **credibility: stretched** |
| D2C portfolio target | "Increase... in the next 3 years" (no specific number given) | 3 years | FY25 D2C mix 51.8% of AUM; FY26 actual (per Q4FY26 results) 59% — genuine progress, target itself was non-specific so cannot be scored precisely |

**Overall forward-guidance credibility: 🟡 Watch.** The AUM growth target and D2C-mix trajectory are tracking or exceeding guidance one year in; the profitability targets (ROA/ROE) are directionally improving but remain well below the guided range after the first of three guided years — this is the kind of gap the pipeline instructs be treated as a genuine guidance-divergence signal, not dismissed as early-stage noise, given how large the gap still is (ROE 11.1% actual vs 16-18% guided, more than 500bps short even after visible improvement).

- **Segment analysis** (MD&A 4.2, PDF p.51): Intermediate Retail (₹6,570 Cr AUM, 0.6% GNPA, 1.5% credit cost) is the largest and cleanest segment; MSME (₹2,574 Cr, 2.8% GNPA — the **highest GNPA of any segment**, 2.5% credit cost); Consumer (₹3,390 Cr, 0.4% GNPA, 6.0% credit cost — high credit cost despite low GNPA, suggesting either aggressive provisioning or a lag between staging and cost recognition); Rural/Pragati (₹1,100 Cr, 0.1% GNPA but 6.8% credit cost — the **highest credit cost of any segment**, an apparent GNPA/credit-cost disconnect worth investigating, possibly reflecting MFI-specific provisioning norms that provision ahead of formal NPA recognition).

### 4D. Tone and credibility ratings (1-5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3/5 | Core bad news (FLDG, credit cost, Pragati loss) is disclosed and quantified, satisfying minimum regulatory transparency, but consistently placed in the least-visible location (deep notes, subsidiary write-ups) rather than the primary narrative (Chairman's/MD&CEO's letters, MD&A risk section) — see 4B |
| Consistency | 3/5 | Multiple unreconciled duplicate figures across the document (NNPA ratio, Stage-3 coverage, total borrowings, audit fees, and the front-matter "Total Income" chart flagged in Phase 6 below) — a genuine internal-consistency gap, though none is directionally misleading once traced |
| Specificity | 4/5 | Segment-level AUM/GNPA/credit-cost tables, ALM maturity buckets, LCR templates, and RPT tables are genuinely granular and specific — this is a strength |
| Accountability | 3/5 | Management owns the FLDG issue as regulator-driven (fair) and quantifies the "excluding DLG" adjusted PAT (₹356 Cr, +15.4% YoY) transparently in MD&A — a real positive — but never explains the consolidated PAT decline or the segment-level credit-cost anomalies (Consumer, Rural) in the same forthright way |
| Capital allocation sense | 4/5 | IPO proceeds and CCPS conversion genuinely de-levered the balance sheet (D/E 4.02x→2.87x, CRAR 18.26%→24.72%); no dividend paid (explicitly reasoned as capital retention for growth); AIF investment in a related-party-managed vehicle (₹275-282 Cr) is the one capital-allocation decision that warrants closer scrutiny given the related-party dimension |

### Phase 4 Summary + contradictions vs Phases 1-3

The MD&A's confident collections/risk-management narrative (4.3/4.5) sits in tension with the notes-level complaints surge and fraud disclosure (Phase 2, B02 #4/#6) — a genuine **contradiction of emphasis**, not of fact. The forward-guidance ROA/ROE targets (4C) are aggressive relative to the credit-cost trajectory shown in Phase 3, and FY26 actuals (available post-AR) show the gap persisting, which is useful corroboration rather than contradiction.

**Phase 4 Verdict: 🟡 Watch.**

**Kill Switch Assessment (informational)**: a human reviewer would **not** stop here, but would specifically want management commentary on (a) the complaints surge and (b) the consolidated-vs-standalone PAT gap before taking the MD&A's upbeat framing at face value. Continuing to Phase 5.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A. Board composition, tenure, other boards, attendance

As of 31-Mar-2025: 8 directors — 1 Executive (MD & CEO), 1 Non-Executive Non-Independent, 3 Independent, 3 Nominee (Board's Report, PDF p.56). **No "Promoter" category exists in this company** — NORTHARC is a professionally-managed, institutionally/PE-held NBFC with no promoter group disclosed anywhere in the document (confirmed by an exhaustive search: the only appearance of the word "Promoter" in the entire Annual Report is generic e-voting-rule boilerplate, PDF p.331). This is a structurally important governance characteristic: no promoter to flag for pledge/selling behaviour (Phase 5D below is a structural N/A, not a clean pass).

| Director | Category | Attendance | Other directorships | Committee positions (Chair/Member) | Flag? |
|---|---|---|---|---|---|
| Ashish Mehrotra | Executive (MD&CEO) | 18/18 (100%) | 10 | 0/1 | — |
| Dr. Kshama Fernandes | Non-Exec Non-Indep | 17/18 (94%) | 7 | 1/3 | — |
| T S Anantharaman | Nominee | 17/18 (94%) | 7 | 2/4 | Resigned post-year-end (Jun-2025) on investor stake sale |
| Michael Jude Fernandes | Nominee | 18/18 (100%) | 2 | 0/1 | — |
| Vijay Chakravarthi | Nominee | **15/18 (83%)** | 3 | 0/2 | Lowest attendance, still above 75% threshold |
| Anuradha Rao | Independent | 17/18 (94%) | 2 | 1/4 | — |
| Ashutosh Pednekar | Independent | 18/18 (100%) | 5 | 3/3 | — |
| **P S Jayakumar (Chairman)** | Independent | 18/18 (100%) | **13** | **4/9** | High board-seat load (13 other directorships + this one = 14 total, plus 6 other-listed-entity directorships); within the regulatory ceiling (max 20 companies/10 public/7 listed) but worth monitoring for board-bandwidth capacity given his Chairmanship role here |
| N T Arun Kumar | Independent | 16/16 (100%, tenure ended mid-year) | — | — | Ceased 13-Feb-2025 on 3-year term completion |

(Corporate Governance Report, PDF p.57-58)

**No independent director exceeds 10 years' tenure** — N T Arun Kumar's term ended at 3 years; the independent-director cohort is relatively fresh, consistent with a recently-IPO'd company that reconstituted its board around listing. **No attendance below 75%.** **No promoter-group cross-board memberships** (no promoter group exists). **No director exceeds 8 board seats** at NORTHARC-attributable companies (Jayakumar's 13 are elsewhere, within regulatory limits, but flagged above as a capacity watch item).

### 5B. Committee analysis

The Company confirms compliance with committee-composition norms under Reg. 26(1) and RBI Directions; Audit Committee, NRC, Stakeholders' Relationship Committee, CSR Committee, and Risk Management Committee structures are in place per the Corporate Governance Report (not fully re-tabulated here given length, but no adverse finding surfaced in this pass). CSR Committee composition: Ashutosh Pednekar (Chair, Independent), Michael Jude Fernandes (Nominee), Kshama Fernandes (Non-Independent), Ashish Mehrotra (MD&CEO) — 2/2 meetings attended by all members (Board's Report Annexure A, PDF p.38) — full attendance, clean.

### 5C. Compensation

| Item | Value | Anchor |
|---|---|---|
| MD & CEO (Ashish Mehrotra) total remuneration FY25 | ₹8.72 Cr (fixed ₹5.00 Cr + bonus ₹2.376 Cr + special bonus ₹1.00 Cr + deferred FY24 bonus ₹0.34 Cr) | Board's Report, PDF p.75 |
| MD & CEO remuneration per Note 42 (RPT note) | ₹8.85 Cr (short-term benefits) + ₹8.13 Cr (share-based payments) | Note 42, PDF p.229 |
| **Discrepancy**: ₹8.72 Cr (Board's Report table) vs ₹8.85 Cr (Note 42) | ~₹0.13 Cr (₹13 lakh) gap, unreconciled — a fourth instance of the cross-document figure-mismatch pattern flagged repeatedly in this report | Board's Report PDF p.75 vs Note 42 PDF p.229 |
| CEO-to-median-employee remuneration ratio | **1:173** | Board's Report, PDF p.27 |
| % increase in CEO remuneration YoY | 43% | Board's Report, PDF p.27 |
| % increase in median employee remuneration YoY | 16% | Board's Report, PDF p.28 |
| Chairman commission (P S Jayakumar) | ₹1.54 Cr (excl. sitting fees) | Board's Report, PDF p.75; Note 42, PDF p.229 |
| Total sitting fees paid to all NEDs | ~₹1.44 Cr aggregate | Board's Report, PDF p.75 |

The **CEO-to-median ratio of 173x, with the CEO's own pay rising 43% against a 16% median-employee increase (nearly 3x the differential rate)**, in a year where standalone PAT rose 22.3% but consolidated PAT *fell* 5.2% and ROE fell from 14.5% to 10.0%, is a **genuine pay-for-performance mismatch worth flagging** — the CEO's compensation growth rate materially outpaced both the headline consolidated earnings trend and the median employee's own increase. No promoter-family payroll issue (no promoter group exists). ESOP dilution (5A/2H above) is modest.

### 5D. Shareholding

**Structural N/A**: no promoter/promoter-group category exists for NORTHARC (see 5A). Shareholding is distributed across 1,10,090 PAN-wise holders; 100,001+ share-block holders (264 accounts) hold 90.07% of value, i.e., **highly concentrated in a small number of institutional/large accounts** (Corporate Governance Report, PDF p.79) — a normal pattern for a recently-IPO'd, institutionally-anchored NBFC, not itself a red flag but worth noting for liquidity/free-float context. No pledge disclosure found (none applicable in the absence of a promoter group). No FII/DII trend table was located in this Annual Report in the format typically seen in prospectus-style shareholding-pattern filings — this level of granularity (FII/DII %, quarter-on-quarter movement) is **NOT FOUND IN DOCUMENT** and would need to be sourced from exchange shareholding-pattern filings outside the Annual Report.

### 5E. Governance red-flag checklist

| Item | Finding | Flag |
|---|---|---|
| Whistleblower complaints | **Nil** received during FY25 (Board's Report, PDF p.36; CARO xi(c) confirms) | 🟢 |
| SEBI/exchange actions | **Multiple penalties found**: aggregate ~₹11.34 lakh in BSE fines across FY2021-22 to Aug-2023 for SEBI LODR compliance delays on listed NCDs (delayed board-meeting intimation, delayed investor-complaint statements, non-disclosure of NCD security details), **plus a further ₹4.40 lakh penalty for the quarter ended June 30, 2024 — i.e., within FY 2024-25 itself** — for delayed board-meeting intimation, non-submission of unaudited results, and non-disclosure of security-creation details on secured NCDs (Corporate Governance Report, PDF p.80) | 🟡 — a real, quantified compliance-delay pattern that persisted into the reporting year itself, not merely historical |
| RPT committee | Functioning; AOC-2 discloses **Nil** non-arm's-length RPTs for the year (Board's Report Annexure D, PDF p.46) | 🟢 |
| Auditor fee ratio | No non-audit fee disclosed; ratio effectively 0% (Phase 1E) | 🟢 |
| CSR compliance | Fully spent, marginal ₹0.58 lakh excess (Phase 1D) | 🟢 |
| Section 143 fraud reporting | No S.143(12) fraud report filed by auditor (CARO xi(b)) — though Note 51 discloses 29 sub-CARO-materiality fraud instances (Phase 1D discussion) | 🟡 (disclosure present, materiality-threshold nuance) |
| Material subsidiary auditor | 5 subsidiaries/1 associate audited by unnamed "other auditors" (Phase 1F) — the AR does not name which firms audit Pragati Finserv (the material, loss-making subsidiary) specifically | 🟡 — a disclosure gap for the one subsidiary that matters most this year |
| Secretarial audit | Clean opinion, but "delay in filing under SEBI LODR Regulations" flagged as an observation (not a qualification) (Board's Report, PDF p.46) | 🟡 — consistent with the SEBI/BSE penalty pattern above |

### Phase 5 Summary

**Phase 5 Verdict: 🟡 Watch.** Board composition, attendance, committee functioning, whistleblower mechanism, RPT arm's-length declaration, and CSR compliance are all genuinely clean (🟢). The persistent pattern of SEBI/BSE listing-compliance delay penalties — including one instance crystallising within FY25 itself — combined with the CEO-pay-growth/consolidated-earnings mismatch and the unnamed component auditor for the loss-making Pragati subsidiary, are real governance-quality watch items, though none rises to a hard red flag (no fraud, no whistleblower matter, no promoter pledge/selling issue since no promoter exists).

**Kill Switch Assessment (informational)**: a human reviewer would **not** stop here. The SEBI/BSE penalties are administrative-compliance-timeliness issues (aggregate ~₹15.74 lakh across ~4 years), not substantive fraud or governance-capture findings. Continuing to Phase 6.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

*Read last, with full knowledge of Phases 1-5.*

### 6A. Narrative vs reality — top prominent claims cross-referenced

| # | Claim (Chairman's Message / MD&CEO Message / front matter) | Financial reality | ✅/❌ |
|---|---|---|---|
| 1 | "First full financial year as a listed entity... a milestone that signified market acceptance" (Chairman's Message, PDF p.5) | Factually accurate — IPO completed Sep-2024, ₹777 Cr raised | ✅ |
| 2 | "Robust AUM growth despite market headwinds – AUM grew 16.0% YoY... to INR 13,634 crore" (MD&CEO Message, PDF p.7) | Matches MD&A's AUM figures exactly (₹11,710 Cr→₹13,634 Cr, +16.4%, MD&A 4.2, PDF p.50) | ✅ |
| 3 | "Strong revenue growth with margin expansion - Total income grew 23% YoY to INR 2,071 crore" (MD&CEO Message, PDF p.7) | **Does not reconcile to any audited figure.** Standalone Total Income was ₹2,296.51 Cr (+24.52%); Consolidated was ₹2,355.74 Cr (+23.59%). The front-matter "Northern Arc's Performance" infographic (PDF p.10) independently shows the identical "Total Income (INR cr)" series ending at FY25=2,071, FY24=1,685 — neither of which matches the audited standalone (₹2,296.51/₹1,844.32 Cr) or consolidated (₹2,355.74/₹1,906.03 Cr) Total Income figures in the financial statements. No definition or reconciliation is offered anywhere for what this ₹2,071 Cr / ₹1,685 Cr series represents | ❌ — **a genuine, material, unreconciled front-matter figure appearing twice in the document (MD&CEO letter + performance infographic) that does not tie to any audited P&L line** |
| 4 | "PAT for FY 2024-25 stood at INR 305 crore vs INR 308 crore in FY 2023-24" (MD&CEO Message, PDF p.7) | This is neither the standalone PAT (₹342.62 Cr FY25 / ₹280.17 Cr FY24) nor the consolidated total PAT (₹301.32 Cr FY25 / ₹317.69 Cr FY24) — it matches the "Attributable to Owners" consolidated PAT line from the MD&A DuPont table (₹305 Cr/₹308 Cr, MD&A 4.2, PDF p.50), i.e., consolidated PAT **net of non-controlling interest**. This is a defensible and commonly-used metric (owners' share of consolidated profit) but the MD&CEO letter does not label it as such, creating ambiguity for a reader comparing it against the Board's Report's standalone-PAT-led financial-highlights table | ⚠️ partial — technically traceable once the "Attributable to Owners" lens is applied, but presented without that qualifier, so a casual reader would not know which of three different "PAT" figures (₹342.62 Cr standalone / ₹301.32 Cr consolidated-total / ₹305 Cr consolidated-attributable-to-owners) is being cited |
| 5 | "Excluding the FDLG related provision, Northern Arc's net profit for the year would have been INR 356 crore, representing a 15.4% year-on-year growth" (MD&CEO Message, PDF p.7) | Internally consistent with MD&A 4.2's identical statement and with the FLDG quantum (₹68 Cr absorbed in Q4) — ₹305 Cr (owners' PAT) + ₹51 Cr (overlay, already included in the ₹305 Cr base per MD&A phrasing ambiguity) is not exactly reconcilable to ₹356 Cr from the ₹305 Cr base without also adding back the overlay; the ₹356 Cr figure appears to add back only the FLDG-specific ₹51 Cr Q4 hit portion attributable to owners, consistent enough not to flag as false, but the exact bridge (₹305 Cr + ? = ₹356 Cr) is not shown step-by-step anywhere | ⚠️ directionally credible, not fully bridged |
| 6 | "Northern Arc has navigated multiple credit cycles... while maintaining consistent profitability" (MD&CEO Message, PDF p.7) | True on a multi-year view (Board's Report CSR-computation table shows standalone net profit ₹222.79 Cr FY22 → ₹316.41 Cr FY23 → ₹374.41 Cr FY24, a rising trend prior to FY25's flat/declining print), though FY25 itself shows the **first YoY decline in consolidated PAT** in this disclosed series — the claim of "consistent profitability" is true in the sense of "always profitable" but glosses over the FY25 consolidated PAT decline | ⚠️ true but selectively framed |
| 7 | "well-capitalised balance sheet and proactive asset-liability management" (Chairman's Message, PDF p.5) | Strongly supported by the evidence: CRAR 24.72% (up from 18.26%), D/E 2.87x (down from 4.02x), LCR 154.39% — this claim is **fully substantiated** by Phase 3B/2F findings | ✅ |

### 6B. Strategic priorities — specificity, capital allocated, execution evidence

- **"Scale the D2C business... target to increase the D2C portfolio in the next 3 years"** (MD&A Outlook, PDF p.55) — specific direction, quantified via the AUM/ROA/ROE guidance table (Phase 4C), with visible capital commitment (branch expansion 316→360 in FY25, per front-matter chart) and early execution evidence (D2C mix rose 49.8%→51.8% FY25, further to 59% FY26 per post-AR results) — a genuinely well-executed, capital-backed priority.
- **"Recalibrating exposure to the microfinance sector"** (MD&CEO Message, PDF p.7) — evidenced by Pragati's approval-rate drop (>40%→<20%) and the segment-level credit-cost data (Phase 4C) — a real, costly (in near-term profitability) strategic pivot, not just rhetoric.
- **AIF/fund-management growth (NAIM)** — ₹200 Cr+ raised for Northern Arc Finserv Fund, ₹245 Cr DFC offshore raise, ₹520 Cr GIFT City pipeline (Board's Report subsidiary section, PDF p.29) — specific, quantified, and capital-light (fee-based) growth vector, consistent with the ROA-expansion thesis in the guidance table.

### 6C. Metrics showcased vs conspicuously absent

**Showcased**: AUM growth, D2C mix, yield/spread/cost-of-funds trend, PPOP growth (+45.7%), CRAR, LCR, lender diversification, branch network expansion, NAIM's fund performance (14.57% weighted-average XIRR, zero capital loss track record).

**Conspicuously absent from the Chairman's/MD&CEO's letters and MD&A's prominent sections**: the consolidated PAT decline (−5.2%), the customer-complaints surge (+930-1000%), the fraud disclosure (29 instances), the Pragati net-worth erosion (85.7%), and the Stage-3 provision coverage decline — **all five of these are disclosed in the document, just never in the front-matter narrative sections that most readers (and most sell-side summaries) would actually read**. This is the single clearest Phase 6 pattern: **nothing is hidden, but everything unfavorable is relegated to notes and subsidiary write-ups while the narrative sections curate an uninterruptedly positive story.**

### 6D. Tone and priority drift vs prior year

Not independently inferable from this Annual Report alone (FY24's Chairman's/MD&CEO letters are not reproduced here for comparison) — **NOT FOUND IN DOCUMENT** for a direct prior-year tone comparison. The FY25 tone itself is consistently confident/promotional throughout (typical of a first-year-listed company's inaugural annual report), with no internal tonal shift detected between the front-matter and the back-matter notes (i.e., the notes are not more cautious than the letters — they are simply more complete).

### Phase 6 Summary

**Phase 6 Verdict: 🟡 Watch.** The single most significant Phase 6 finding is the **unreconciled "Total Income ₹2,071 Cr" figure appearing twice in the front matter** (6A #3) — a genuine, document-internal numerical inconsistency in the most prominent, most-read section of the Annual Report, which stands out even against the pattern of minor note-level figure mismatches found in Phases 1-3. Otherwise, the front matter's claims are largely **factually defensible but selectively framed** — favorable metrics are shown with full context; unfavorable ones are disclosed but never narrated.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP** (fullest reasoning per operator mandate) | **WATCHLIST** | (1) Growth is genuine and diversified — AUM +16.4% FY25, guided 20-25% CAGR next 3 years, with FY26 actuals (+22% YoY) tracking the guided range — supports the "growth" half of GARP. (2) "Reasonable price" cannot be assessed within this stage (exit-multiple/valuation work belongs to Stage 11 under Section 1B v3.3 — this stage does not opine on valuation), but the *earnings quality* underpinning any P/E-based reasonableness assessment is currently impaired: FY25 consolidated PAT fell 5.2%, ROE fell from 14.5% to 10.0%, and the FY26 ROE recovery (11.1%) remains well short of management's own 16-18% guided range — a GARP thesis needs the "reasonable" leg to be underwritten by a believable earnings trajectory, and that trajectory is currently the weakest link, not the growth leg. (3) The regulator-forced ECL correction (FLDG) and the still-tightening asset-cover/credit-cost metrics mean an investor underwriting GARP here is making a bet on credit-cycle normalization within the guided 3-year window, which is plausible (segment-level data shows the intermediate-retail book, 48% of AUM, is genuinely clean at 0.6% GNPA) but not yet proven at the consolidated level |
| **Turnaround** (fullest reasoning) | **WATCHLIST** | (1) This is not a classical turnaround (the company is not distressed — CRAR 24.72%, no covenant breach, no going-concern issue) but it does contain a turnaround-within-a-turnaround: Pragati Finserv (the MFI subsidiary) is in genuine operational distress (85.7% net-worth erosion, approval rate collapse) with management explicitly describing "recalibration" actions (Family Connect program, digital collections, Tele Calling team, tighter underwriting) — a live subsidiary-level turnaround case study embedded inside an otherwise-healthy parent. (2) The credit-cost spike (1.2%→3.2%) and GNPA doubling (0.47%→0.99%) represent a genuine asset-quality "trough" that the guided FY26-28 ROA/ROE targets implicitly assume will reverse — FY26 actuals show credit cost normalizing (3.2%→2.8%) and PAT recovering (+33% YoY) supporting an early-stage turnaround-from-trough read, though GNPA/NNPA continued rising into FY26 (0.99%→1.2% and 0.43%→0.6% respectively per Q4FY26 results), meaning the "turnaround" is asymmetric — profitability metrics are recovering while asset-quality metrics are not yet, which needs reconciling. (3) No management change or strategic pivot at the parent level accompanies this (same CEO, same strategy, same 3-segment structure) — this is an operational-recovery story, not a strategic-reset turnaround, which somewhat lowers the "turnaround alpha" potential relative to situations with fresh capital allocation or leadership change |
| Value+Quality | WATCHLIST (brief) | Balance-sheet quality (CRAR, LCR, ALM) is genuinely strong; earnings quality (credit cost trajectory, unreconciled figures, front-matter Total Income discrepancy) is the weak leg — "quality" label needs the earnings-side concerns resolved before this clears to PASS |
| Capex-Led Growth | Not applicable (financial services, no capex-led thesis in the conventional sense; branch/technology investment is modest relative to AUM) | — |
| Cash Flow Compounder | WATCHLIST (brief) | CFO is structurally negative (loan growth funded by borrowings, normal for a lender) so the conventional "cash flow compounder" framework does not map cleanly; the more relevant analog (NII/PPOP compounding) shows genuine compounding (PPOP +45.7% YoY) but off a credit-cost-impaired PAT base |
| Contrarian | WATCHLIST (brief) | The consolidated PAT decline, complaints surge, and FLDG regulatory hit collectively create a sentiment overhang that a contrarian thesis could exploit if the underlying intermediate-retail/D2C book quality (genuinely strong segment-level metrics) is judged to be mispriced against the headline-negative optics — plausible but requires conviction that the Pragati/MFI drag is transient |
| Insider Confidence | NOT FOUND / not assessable | No promoter exists; no insider (director/KMP) share-transaction disclosure was located in this pass beyond the standard shareholding-as-of-date table (director shareholdings static, no buy/sell pattern disclosed in the AR itself) |
| Guidance Divergence | WATCHLIST | Management's own ROA (3.7-4.0%) and ROE (16-18%) 3-year targets remain materially unmet after year 1 (FY26 actual 2.8%/11.1%) even as the AUM growth and D2C-mix targets are being met or exceeded — a genuine, quantified guidance-divergence signal on the profitability dimension specifically, worth tracking each quarter against the guided glide path |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot

Northern Arc Capital Limited (NORTHARC) — diversified retail-focused NBFC-ML, IPO'd Sep-2024, rated [ICRA]AA-(Stable)/IND AA-(Stable), CP rated A1+/CARE A1+. FY25 AUM ₹13,634 Cr (+16.4%), Standalone PAT ₹342.62 Cr (+22.3%), Consolidated PAT ₹301.32 Cr (−5.2%), CRAR 24.72%, GNPA 0.99%/NNPA 0.39-0.43% (dual figures, unreconciled), D/E 2.87x. No promoter group; professionally/institutionally managed.

### Phase-wise verdict summary table

| Phase | Verdict | One-line reason |
|---|---|---|
| 1 — Auditor's Report & CARO | 🟡 Watch | Clean opinion but first-year auditor delivered a regulator-forced EOM; unreconciled audit-fee figure across two document sections |
| 2 — Notes | 🟡 Watch | Triple-pass 6/10 accounting score affirmed; recurring pattern of unreconciled duplicate figures (NNPA, coverage, borrowings, fees) found across 4+ metrics |
| 3 — Financial Statements | 🟡 Watch | Balance sheet genuinely strong (CRAR, D/E, LCR); earnings quality impaired by credit-cost spike, though diluted-EPS cross-check shows underlying per-share economics improved |
| 4 — Risk/MD&A | 🟡 Watch | Real risks disclosed and quantified but consistently under-emphasized in the narrative sections relative to the notes; forward ROA/ROE guidance running well behind schedule |
| 5 — Governance | 🟡 Watch | Board/committee mechanics clean; SEBI/BSE compliance-delay penalty pattern persisted into FY25; CEO pay growth (43%) outpaced consolidated earnings and median-employee pay growth |
| 6 — Chairman's Letter/Front Matter | 🟡 Watch | Genuine, twice-repeated unreconciled "Total Income ₹2,071 Cr" figure in the most-read section; systematic favorable-framing/unfavorable-burial pattern, though nothing is factually false |
| 7 — Best fit strategy | Turnaround / GARP (Watchlist, both) | See Phase 7 |

### Overall quality score: 6.5/10

| Component | Weight | Score /10 | Basis |
|---|---|---|---|
| Governance | 25% | 7 | Clean board mechanics, attendance, committees, whistleblower/RPT/CSR; offset by SEBI/BSE penalty pattern persisting into FY25 and the CEO-pay/earnings-growth mismatch |
| Accounting quality | 25% | 6 | Reconciled with B02's triple-pass score; regulator-forced ECL correction, recurring unreconciled duplicate figures across 4+ metrics, but no evidence of fraud, reserve manipulation, or aggressive tax positioning |
| Balance sheet | 25% | 8 | CRAR 24.72% (well above 15% minimum), D/E nearly halved, LCR 154%, matched ALM buckets, immaterial goodwill/contingent liabilities, no covenant breach |
| Earnings quality | 25% | 5 | Consolidated PAT declined; credit cost tripled (as % of assets); GNPA doubled and continued rising into FY26; segment-level GNPA/credit-cost disconnects (Consumer, Rural) unexplained; though diluted EPS and PPOP genuinely grew |

**Overall = 0.25×7 + 0.25×6 + 0.25×8 + 0.25×5 = 6.5/10**

### Top 3 strengths

1. **Post-IPO balance-sheet transformation is real and substantial**: CRAR nearly doubled (18.26%→24.72%), D/E nearly halved (4.02x→2.87x), LCR at 154% (vs 100% RBI minimum), diversified 49-lender funding base with cost of funds falling 20bps to 9.0% despite a sector-wide NBFC funding squeeze (MD&A 4.4, PDF p.52; Note 82, PDF p.253).
2. **Granular, genuinely diversified retail franchise**: D2C AUM grew 21.1% to ₹7,064 Cr (51.8% of book), serving 19.88 lakh customers across MSME/consumer/rural, with the largest segment (Intermediate Retail, ₹6,570 Cr) showing the cleanest asset quality (0.6% GNPA) in the portfolio (MD&A 4.2, PDF p.50-51).
3. **Clean audit/governance mechanics with no fraud, no covenant breach, no going-concern issue, no whistleblower matter**, and full CSR compliance — the concerns in this report are disclosure-hygiene and earnings-quality/narrative-framing issues, not integrity or solvency issues.

### Top 3 red flags

1. **Regulator-forced ECL correction (FLDG exclusion) elevated to Auditor's Emphasis of Matter in the new auditor's first year**, ₹68.35 Cr absorbed in Q4FY25 PBT, direct evidence the Company's own ECL model had embedded an impermissible credit-enhancement assumption until RBI intervened (Auditor's Report ¶4, PDF p.125/259; Note 83/49).
2. **Consolidated PAT fell 5.2% (Pragati Finserv subsidiary swung to a ₹29.39 Cr loss, 85.7% net-worth erosion) while the standalone-only headline (+22.3%) was the figure emphasized throughout the Chairman's/MD&CEO's letters and front-matter infographics** — the weaker consolidated reality is disclosed only in a financial-highlights table, never narrated (Board's Report, PDF p.25; Note 22 consolidated, PDF p.353-354).
3. **A recurring pattern of unreconciled duplicate figures across the document** — dual NNPA ratios (0.39%/0.43%), dual Stage-3 coverage figures (~68% notes vs 61.1% MD&A), three different "total borrowings" figures, mismatched audit-fee and CEO-remuneration figures across sections, and a twice-repeated front-matter "Total Income ₹2,071 Cr" figure that reconciles to none of the three audited Total Income numbers in the document — none individually material, but collectively a genuine note-preparation/QA-rigour concern for a company in its first year of public-company reporting discipline.

### Key monitorables for next quarter

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| Consolidated GNPA / NNPA ratio | Watch for continued rise beyond FY26's 1.2%/0.6% (already above FY25's 0.99%/0.43%) | Quarterly results press release / investor presentation | The single clearest leading indicator that the credit cycle has not yet troughed, despite improving PAT/ROA |
| Pragati Finserv standalone net worth / quarterly P&L | Any further erosion below the FY25 ₹4.96 Cr level, or any goodwill-impairment trigger disclosure | Standalone subsidiary disclosures in quarterly investor decks; next AR's Note 81 goodwill test | Determines whether the ₹20.85 Cr goodwill (100% Pragati-CGU-allocated) remains supportable and whether the FY25 loss was a trough or a trend |
| ROA / ROE vs the 3.7-4.0% / 16-18% 3-year guided range | Track quarterly delta to guided glide path; flag if FY27 (guidance year 2) print does not show material closing of the gap | Quarterly results, MD&A of next AR | FY26 actuals (2.8%/11.1%) remain well short after 1 of 3 guided years — a persistent gap into year 2 would be a genuine guidance-divergence red flag per Amendment-consistent pipeline treatment |
| Asset cover on listed NCDs | Watch for further narrowing below 1.08x | Note 82-equivalent in next AR / bond covenant filings | Already tightened from 1.15x to 1.08x FY25; a covenant-adjacent metric worth tracking even though not yet breached |
| Customer complaints count and grounds-table reconciliation | Watch whether FY26 complaints normalize from the FY25 surge (91→938) or continue rising | Next AR's Note 72-equivalent / any interim grievance-redressal disclosure | An unaddressed operational-strain signal that MD&A did not narrate in FY25; persistence into FY26 would confirm this is structural, not one-off |
| SEBI/BSE compliance-penalty recurrence | Any further penalty in FY26 for LODR/listing-compliance delays | Stock-exchange disclosures / next Corporate Governance Report | A penalty recurred in the June-2024 quarter itself (within FY25); a further FY26 instance would confirm an unresolved compliance-process gap rather than a one-off teething issue |

### Best-fit strategy and one-line verdict

**Best-fit strategy: Turnaround-within-growth (Pragati/credit-cycle normalization inside an otherwise-scaling, well-capitalized retail NBFC).**

**One-line verdict**: Balance sheet strong, credit cycle unresolved, disclosure discipline needs work.
