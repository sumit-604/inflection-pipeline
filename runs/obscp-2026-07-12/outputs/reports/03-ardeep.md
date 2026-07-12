# STAGE 3 — ANNUAL REPORT DEEP DIVE, BACKWARD READ
Company: OBSC Perfection Ltd (OBSCP) | Run date: 2026-07-12 | Model: claude-sonnet-5
Source: runs/obscp-2026-07-12/inputs/annual-report/Annual_Report_2025.pdf (FY2024-25 Annual Report, year ended 31 March 2025)

## DOCUMENT DEGRADATION NOTICE (governs every phase below)

| AR page(s) | Content | Readability | Used in this stage |
|---|---|---|---|
| 1 | Cover letter to NSE (04 Sept 2025, Regn 34 filing) | Readable | Phase 6 (front matter) |
| 2 | AR cover (image) | Readable, no substantive text | Not used |
| 3-59 | Board's Report + Annexures, MD&A, Corporate Governance Report, MGT-9/shareholding | Corrupted font — unreadable, confirmed visually | Phases 4, 5, 6 (narrative) — NOT FOUND IN DOCUMENT throughout |
| 60-70 | Independent Auditor's Report + Annexure A (CARO 2020) + Annexure B (ICFR) | Readable | Phase 1 — full |
| 71 | Balance Sheet as at 31 March 2025 | Readable | Phase 3B |
| 72 | Statement of Profit & Loss FY2024-25 | Readable | Phase 3C |
| 73 | Cash Flow Statement FY2024-25 | Readable | Phase 3A |
| 74-77 | Notes to Financial Statements — Note 1 (Corporate Information) + Note 2 (Significant Accounting Policies, sub-topics 1-5.2) | Readable | Phase 2 |
| 78-101 | BLANK/truncated — remainder of Note 2, entire numbered schedule-notes package (Note 3 through at least Note 29) | Not recoverable | All phases — NOT FOUND IN DOCUMENT where dependent |

Per operating rules, every phase below states "NOT FOUND IN DOCUMENT — AR pages [range] unreadable/truncated" where the source is unavailable, and does not estimate. Kill-switch assessments are informational only; the pipeline never halts on company quality.

---

# PHASE 1: AUDITOR'S REPORT & CARO

## 1A Core Opinion

Unmodified (clean) opinion. Auditor: P. K. Chand & Co., Chartered Accountants, Noida (Firm Regn. No. 512371C). Engagement partner: Prashant Kumar Chand (M.No. 091046). Report dated 16 May 2025. UDIN: 25091046BMONEY2913 (Auditor's Report p.60).

Opinion text: "the aforesaid financial statements... [g]ives true and fair view in the conformity with the recognition and measurement principles laid down in the applicable accounting standards... of the net profit and other financial information for the half year and year ended 31st March, 2025" (Auditor's Report p.60). Note the report is framed for "Half Year and Year ended 31st March, 2025" per Regulation 33 SEBI LODR — standard combined half-year/full-year listing-regulation format.

Basis for opinion: standard SA-143(10) language, no qualification (Auditor's Report p.60).

Going-concern language: NONE beyond the standard CARO clause (xix) 12-month liquidity opinion (see 1D below). No explicit management going-concern disclosure or auditor emphasis-of-matter on going concern found on any readable page (Auditor's Report pp.60-61; Note 2, pp.74-77).

## 1B Key Audit Matters

| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| N/A — none reported | Auditor states explicitly: "Reporting of key audit matters as per SA 701, Key Audit Matters are not applicable to the Company as it is an unlisted company" (Auditor's Report p.60) | N/A | 🟡 |

**Cross-reference flag**: the audit report (dated 16 May 2025) treats OBSCP as unlisted and therefore exempts it from SA 701 KAM reporting. The cover letter to NSE (p.1, dated 04 September 2025) shows the company had by then listed and was circulating its 9th AGM notice and this same FY25 AR to shareholders under scrip symbol OBSCP. This means the audit itself was performed and dated before listing, so no revenue-recognition, impairment, provisioning, or fair-value KAM analysis exists anywhere in this document for FY25 — a structural gap for a first-listing-year AR, not a document-degradation artifact. Should the FY26 audit (post-listing, full year) also omit KAMs, that would be a listing-status/compliance question worth raising with the auditor.

## 1C Emphasis of Matter and Other Matters

NONE found. No Emphasis of Matter paragraph and no separate Other Matters paragraph appear in the readable Auditor's Report (pp.60-63). The only "Other Matters" content present is the s.143(3)(g) sub-clauses on litigation disclosure (Note 29), long-term contracts/derivatives, and IEPF transfers (Auditor's Report p.63) — routine, not adverse.

## 1D CARO 2020 Clause-by-Clause

| Clause | Subject | Finding | Amount | Anchor |
|---|---|---|---|---|
| i(a)-(e) | PPE/intangibles records, physical verification, title deeds, no revaluation, no benami proceedings | Clean — no material discrepancies on physical verification; all title deeds held in company's name (other than lessee-held leased properties); no revaluation; no benami proceedings | — | CARO Annexure A p.64 |
| ii(a) | Inventory verification | Clean — physical verification by rotation during the year, frequency and procedures "reasonable and adequate," discrepancies noticed "were not material and dealt with in the accounts" | Not quantified | CARO Annexure A p.64 |
| ii(b) | Working capital limits >Rs 5 Cr, quarterly returns to banks | Quarterly returns "prima facie in agreement" with books; auditor separately notes unit-rate valuation basis furnished to banks (rough-and-ready) varies from the weighted-average/actual-cost basis used in the financial statements, "though the variation is nominal" | Not quantified | CARO Annexure A pp.64-65 |
| iii(a)-(f) | Loans/advances/guarantees to subsidiaries, JVs | Loans confined to subsidiaries and JV companies (running current account, monthly interest, rates opined "not prima facie prejudicial"); parties repaying principal as stipulated and regular on interest; no overdue amount >90 days; no loans renewed/extended to settle overdues of existing loans; no funds taken by company for subsidiaries' obligations; no loans raised on pledge of securities held in subsidiaries/JV/associates | Aggregate balance per Note 13: Rs 1.53 Cr FY25 vs Rs 1.00 Cr FY24 (+52.9% YoY) | CARO Annexure A pp.65, 67; Balance Sheet p.71 (Note 13) |
| iv | Loans/investments u/s 185, 186 | Not attracted — no loans/guarantees/investments of the type covered | — | CARO Annexure A pp.65-66 |
| v | Public deposits u/s 73-76 | None accepted | — | CARO Annexure A p.66 |
| vi | Cost records u/s 148(1) | Not required to be maintained | — | CARO Annexure A p.66 |
| vii(a) | Statutory dues — regularity | EPF/ESI deposited regularly, "generally deposited... normally within due dates"; Income Tax, Customs Duty, GST, Cess "generally deposited... within due dates" — note the hedging language ("generally," "normally") is the auditor's own phrasing, not a quantified exception | Not quantified | CARO Annexure A p.66 |
| vii(b) | Statutory dues overdue >6 months | Exception stated: "except those stated in the Note No. 10 on Accounts" | Bounded above by Note 10 "Other Current Liabilities" aggregate: Rs 1.62 Cr FY25 vs Rs 1.09 Cr FY24 (+48.8% YoY); specific overdue quantum within that aggregate NOT FOUND IN DOCUMENT — AR pp.78-101 truncated (Note 10 detail) | CARO Annexure A p.66; Balance Sheet p.71 |
| viii | Undisclosed income surrendered in tax assessments | None | — | CARO Annexure A p.66 |
| ix(a) | Borrowing defaults | No default to any financial institution, bank, Government, or debenture holders (test-check basis) | — | CARO Annexure A p.66 |
| ix(b) | Wilful defaulter | Not declared a wilful defaulter | — | CARO Annexure A p.66 |
| ix(c) | Term-loan utilisation | Applied for the purpose obtained | — | CARO Annexure A p.66 |
| ix(d) | Short-term funds diverted to long-term use | None | — | CARO Annexure A p.66 |
| ix(e) | Funds raised for subsidiaries' obligations | None | — | CARO Annexure A p.67 |
| ix(f) | Loans raised on pledge of securities held in subsidiaries/JV/associates | None | — | CARO Annexure A p.67 |
| x(a) | IPO/FPO proceeds raised during the year | None raised via IPO/FPO/debt instruments during FY25 — clause not attracted | — | CARO Annexure A p.67 |
| x(b) | Preferential allotment / private placement | None during the year — ss.42/62 not attracted | — | CARO Annexure A p.67 |
| xi(a) | Fraud by/on the company | None noticed or reported | — | CARO Annexure A p.67 — hard clean, no red flag |
| xi(b) | ADT-4 report u/s 143(12) | None filed | — | CARO Annexure A p.67 |
| xi(c) | Whistle-blower complaints (received by auditor) | None received during the year | — | CARO Annexure A p.67 |
| xii | Nidhi Company | Not applicable | — | CARO Annexure A p.67 |
| xiii | RPT compliance (s.177 Audit Committee; s.188/AS 18 RPT disclosure) | Section 177 Audit Committee: "not applicable" because "the company [is] not being a listed company" (as of the 16 May 2025 report date); RPT compliance with s.188/AS 18 stated as "reported in Note No. ___ to the financial statements" — **the note number itself is left blank in the source document** | Not quantified; note cross-reference itself is illegible/blank in the recovered copy | CARO Annexure A p.67 |
| xiv | Internal audit | System commensurate with size and nature; internal audit reports considered for the period under audit | — | CARO Annexure A p.67 |
| xv | Non-cash transactions with directors (s.192) | None | — | CARO Annexure A p.68 |
| xvi | RBI registration u/s 45-IA | Not required | — | CARO Annexure A p.68 |
| xvii | Cash losses | None incurred in FY25 or the immediately preceding FY | — | CARO Annexure A p.68 — clean |
| xviii | Statutory auditor resignation | None during the year | — | CARO Annexure A p.68 |
| xix | Going-concern / 12-month liquidity | No material uncertainty; company "capable of meeting its liabilities... within a period of one year from the balance sheet date, subject to the fact there is no major financial, health or political turmoil" — standard boilerplate qualifier | — | CARO Annexure A p.68 |
| xx | CSR (unspent amount, s.135(5)/(6)) | Company "paid Rs. 18.04 Lakh to Swachh Paryavaran Trust to spend the amount for Corporate Social Responsibility in terms of section (5) of section 135" — no unspent-amount adverse remark | Rs 18.04 Lakh; mandated 2%-of-average-net-profit base amount NOT FOUND IN DOCUMENT so compliance percentage cannot be independently verified | CARO Annexure A p.68 |
| xxi | Branch/consolidated remarks | No branch/unit auditors; "these are not consolidated financial statements" — explicit statement | — | CARO Annexure A p.68 |
| Para 4 | Overall CARO adverse/qualified remarks | "Since there are no material un-favourable or qualified remarks in the foregoing CARO report, no further comments are necessary" | — | CARO Annexure A p.68 |

**No adverse or qualified CARO remarks overall.** The one open item requiring a named management/auditor follow-up is the blank RPT note-number cross-reference at clause xiii — an internal document gap, not an adverse finding.

## 1E Auditor Continuity

Firm: P. K. Chand & Co. (Firm Regn. No. 512371C), Noida. Engagement partner Prashant Kumar Chand (M.No. 091046). Report dated 16 May 2025 (Auditor's Report p.60, p.63; ICFR opinion p.70).

- Tenure / rotation year: NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable (auditor tenure/appointment history normally disclosed in the Board's Report/AGM notice, not in the Auditor's Report itself).
- Audit vs non-audit fees, and the ratio: NOT FOUND IN DOCUMENT — fee break-up normally sits in the Notes schedule (Other Expenses detail, Note 25) or Corporate Governance Report, both unrecoverable (pp.78-101 truncated; pp.3-59 unreadable). Cannot assess the "non-audit exceeds audit" flag.
- CARO xviii confirms "no resignation of the statutory auditors during the year" — implies at least continuity through FY25, but does not establish original appointment date or first-year-of-tenure status.

## 1F Standalone vs Consolidated

The financial statements presented are **standalone only** — the Balance Sheet, P&L and Cash Flow Statement carry no "Consolidated" designation (Balance Sheet p.71; P&L p.72; Cash Flow Statement p.73), and CARO Annexure A clause xxi states explicitly: "these are not consolidated financial statements" (CARO Annexure A p.68).

This is notable because CARO clause iii and Note 13 both confirm the company has subsidiaries and joint-venture relationships with running loan accounts (CARO Annexure A p.65; Balance Sheet Note 13, p.71). Under s.129(3) of the Companies Act 2013, a company with subsidiaries is ordinarily required to prepare consolidated financial statements unless a specific exemption applies. No exemption basis is stated anywhere in the readable document. **NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable / pp.78-101 truncated** for whether an exemption was claimed, whether the subsidiaries are immaterial/dormant, or whether CFS exists in a section not recovered. This is flagged as an open compliance question, not asserted as a violation.

No auditor's-report differences from a consolidated version exist to compare (none prepared/presented). No reliance on other auditors' work is mentioned (no branch auditors per clause xxi).

## Phase 1 Summary

| Item | Verdict |
|---|---|
| Audit opinion | Clean/unmodified |
| ICFR opinion (Annexure B) | Unmodified, "adequate and operating effectively" (Annexure B p.70) |
| CARO adverse/qualified remarks | None |
| KAMs | None reported — unlisted-company exemption at report date |
| Audit-trail (edit-log) finding | Voucher amendments found on test check, auditor accepts "staff not well versed... reasonable cause," no P&L/BS impact asserted (Auditor's Report pp.62-63) |
| RPT note cross-reference | Blank/illegible in source (CARO xiii, p.67) |
| Consolidated FS | Not prepared; s.129(3) applicability unresolved from readable pages |
| Auditor continuity/fees | NOT FOUND IN DOCUMENT |

**Phase 1 Verdict: 🟡 Watch.** The audit opinion itself is clean with no adverse CARO remarks, but three items keep this from a flat green: (1) the audit-trail voucher-edit finding is a real, disclosed control-integrity issue even if characterised as low-severity by the auditor; (2) the blank RPT note-number cross-reference is a document-quality gap internal to the audited filing itself; (3) the absence of consolidated financial statements despite confirmed subsidiary/JV relationships is an open compliance question that cannot be resolved from this copy.

**Kill Switch Assessment (informational only)**: Based on Phase 1 alone, a human reviewer would *not* have reason to stop, because the audit opinion is clean, ICFR is unmodified, and there is no fraud, default, or qualified CARO remark. The audit-trail and CFS-exemption items warrant a named follow-up question but do not rise to a halt-worthy signal on their own. Continuing to Phase 2.

---

# PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the Phase 2 special instruction, the triple-pass consolidated analysis (runs/obscp-2026-07-12/outputs/reports/02-notes.md) is used as the base. Each of its Top-15 findings is independently re-verified below against the primary financial statements (Balance Sheet p.71, P&L p.72, Cash Flow Statement p.73) and Notes 1-2 (pp.74-77), which this stage re-read directly rather than relying solely on the triple-pass extraction.

## Triple-Pass Top-15 Verification

| Rank | Triple-pass finding | Verification | Status |
|---|---|---|---|
| 1 | Notes 3-29 entirely missing (pp.78-101) | Confirmed — pp.78-101 render blank/truncated on direct re-read; Note 2 ends at sub-note 5.2 on p.77, an internally-numbered 4-of-6-page document | ✓ verified |
| 2 | Diluted EPS Rs 8.12 > Basic EPS Rs 6.85, FY25; FY24 Basic=Diluted=Rs 6.84 | Confirmed byte-for-byte on direct re-read of P&L p.72, Note 26: "Earnings per Equity Share of Rs 10 — Basic 6.85 / Diluted 8.12" (FY25) vs "6.84 / 6.84" (FY24) | ✓ verified |
| 3 | OCF Rs 8.85 Cr vs PAT Rs 16.76 Cr (~52.8% conversion); bridge: OCF before WC Rs 26.91 Cr, current-asset increase Rs (26.81) Cr, current-liability increase Rs 14.39 Cr, taxes paid Rs (5.64) Cr | Confirmed exactly on direct re-read of Cash Flow Statement p.73: Operating cashflow before WC changes Rs 2,690.66 lakh; [Increase]/Decrease in Current Assets Rs (2,680.74) lakh; Increase/[Decrease] in Current Liabilities Rs 1,438.56 lakh; Direct taxes paid Rs (563.56) lakh; Net cash from Operating activities Rs 884.92 lakh | ✓ verified |
| 4 | Trade Payables +118.3% YoY (Rs 25.31 Cr vs Rs 11.59 Cr) | Confirmed on Balance Sheet p.71: Note 9 Trade Payables Rs 2,530.87 lakh FY25 vs Rs 1,159.21 lakh FY24 = +118.3% | ✓ verified |
| 5 | Short-term Provisions negative Rs (0.27) Cr FY25 vs Rs 0.66 Cr FY24 | Confirmed exactly on Balance Sheet p.71: Note 11 Short-term Provisions Rs (27.34) lakh FY25 vs Rs 66.48 lakh FY24; Current Liabilities subtotal Rs 3,360.59 lakh only foots with the negative figure included | ✓ verified |
| 6 | RPT loans to subsidiaries/JVs: Note 13 Rs 1.53 Cr FY25 vs Rs 1.00 Cr FY24 (+52.9%) | Confirmed on Balance Sheet p.71: Long-term Loans & Advances Rs 152.93 lakh FY25 vs Rs 99.99 lakh FY24 | ✓ verified |
| 7 | EPCG: FOB Rs 8.09 Cr, duty exemption Rs 1.35 Cr, obligation = 6x duty over 6 years from 26-12-2024; blocks 50% (yrs 1-4) + 60% (yrs 5-8) = 110% | Confirmed verbatim on direct re-read of Note 2.3(b), pp.75-76: FOB Rs 8,08,68,765 (US$ 9,63,870.85), duty exemption Rs 1,34,78,128, export obligation Rs 8,08,68,785 (6x duty saved) within 6 years, "1st to 4th year (1st Block) — 50%" and "5th to 8th year (2nd Block) — 60%", Authorization date 26-12-2024. The block-year range genuinely extends beyond the stated 6-year window and the percentages genuinely sum to 110% — confirmed as a real drafting defect, not an OCR artifact | ✓ verified |
| 8 | Auditor found voucher edits under audit-trail feature, attributed to staff unfamiliarity, "reasonable cause," no P&L/BS impact | Confirmed verbatim on Auditor's Report pp.62-63 | ✓ verified |
| 9 | Effective tax rate ~18.8% FY25 (Rs 4.65 Cr provision + Rs (0.78) Cr deferred credit = Rs 3.87 Cr on PBT Rs 20.63 Cr) | Confirmed on P&L p.72: Provision for Tax Rs 465.00 lakh, Deferred Tax Adjustment Rs (77.55) lakh, total tax Rs 387.45 lakh on PBT Rs 2,063.49 lakh = 18.77% | ✓ verified |
| 10 | Private-to-Public conversion; Share Capital +37.0%, Reserves +550.8%, Rs 57.16 Cr fresh capital, Balance Sheet +83.2% | Confirmed on Note 1 p.74 (conversion effective 28 June 2024 per fresh Certificate of Incorporation, ROC approval SRN AA7899496 dated 19 June 2024) and Balance Sheet p.71: Share Capital Rs 2,445.24 lakh vs Rs 1,785.00 lakh (+37.0%); Reserves Rs 7,953.80 lakh vs Rs 1,222.10 lakh (+550.8%); Total Rs 15,855.08 lakh vs Rs 8,650.59 lakh (+83.2%); Cash Flow Statement p.73: Increase in Share Capital & premium Rs 5,715.92 lakh | ✓ verified |
| 11 | Deleveraging: LT Borrowings -21.8%, ST Borrowings -56.2%, net Rs (14.50) Cr outflow, funded by equity not OCF | Confirmed on Balance Sheet p.71 (LT Borrowings Rs 2,002.39 lakh vs Rs 2,559.65 lakh = -21.8%; ST Borrowings Rs 694.96 lakh vs Rs 1,587.60 lakh = -56.2%) and Cash Flow Statement p.73 (Increase/[Decrease] in borrowings Rs (1,449.89) lakh) | ✓ verified |
| 12 | Finance costs +16% despite falling borrowings | Confirmed on P&L p.72: Finance costs Rs 312.23 lakh vs Rs 268.88 lakh = +16.1% | ✓ verified |
| 13 | Other Income more than doubled (Rs 1.08 Cr to Rs 2.41 Cr); only Rs 0.86 Cr confirmed interest income | Confirmed on P&L p.72: Other Income Rs 241.23 lakh vs Rs 108.38 lakh (+122.6%); Cash Flow Statement p.73: Interest income Rs 86.35 lakh — leaves ~Rs 1.55 Cr of Other Income composition unexplained | ✓ verified |
| 14 | Note 3 "no investments" vs CARO confirms subsidiary/JV group | Confirmed on direct re-read: Note 2, sub-note 3, p.76: "The Company has no investments at present" vs CARO Annexure A paras iii (p.65) and prior clause references to subsidiaries/JVs | ✓ verified |
| 15 | Statutory dues overdue >6m per CARO vii(b); RPT note number blank in CARO xiii | Confirmed on CARO Annexure A p.66 (vii(b): "except those stated in the Note No. 10 on Accounts") and p.67 (xiii: "...reported in Note No.    to the financial statements" — number field genuinely blank in the source) | ✓ verified |

**Result: 15 of 15 verified, 0 discrepancies.** Direct re-read of the primary statements (Balance Sheet, P&L, Cash Flow) and Notes 1-2 fully corroborates the triple-pass extraction to the rupee/lakh in every case checked.

## Phase 2 Extensions (per special instruction)

**2A. Accounting policy aggressiveness**

| Area | Finding | Assessment | Anchor |
|---|---|---|---|
| Basis of preparation / framework | Financial statements prepared under **Indian GAAP (Accounting Standards under the Companies Act), not Ind AS** — "in a manner to comply with the material requirements... to Medium Companies as per general instructions with respect of Accounting Standards prescribed" | Material framework finding: this is a "Medium Company" AS-based filing, not Ind AS. Explains the absence of Ind AS 116 (leases), Ind AS 109 (ECL), and Ind AS fair-value disclosures anywhere in the document — they are simply not applicable frameworks for FY25. This has downstream implications: post-listing, SEBI LODR / Companies Act thresholds may require Ind AS transition in a future year; FY26 comparability should be checked for a first-time-adoption note | Note 2.1(a), p.74 |
| Revenue recognition | "Accounts relating to the Manufacturing and trading activities are accounted as income on Mercantile/Accrual basis, in accordance to Accounting Standard AS 9" — a single generic sentence, no detail on point of recognition, contract terms, variable consideration, or warranty accrual | Thin/generic but not overtly aggressive; cannot assess conservatism further — NOT FOUND IN DOCUMENT for revenue disaggregation (Note 18 schedule, pp.78-101 truncated) | Note 2.1(a), p.74 |
| Depreciation | Schedule II useful lives; SLM for Plant & Machinery/electrical installations, WDV for all other assets; no revaluation; 5% residual value; land never depreciated | Standard, not aggressive | Note 2, sub-note 5(v)-(vi), p.77 |
| Inventory valuation, method change | Raw materials: lower of cost (weighted average) or market; Finished goods: lower of estimated cost of production or NRV; WIP: cost of RM + average conversion cost restricted to work done; Other items: lower of cost (FIFO) or market. No stated change in method this year (consistent with Pass 3's "no restatements" finding) | Standard, multiple methods across categories (weighted-average/FIFO mix) but consistently applied; not flagged as aggressive | Note 2, sub-note 4, p.76 |
| Capitalisation incl. borrowing costs | PP&E capitalised at cost inclusive of incidentals and borrowing costs up to date of use; borrowing costs allocated during construction period; input-tax credits reduced from cost of acquisition | Standard AS 16-consistent treatment, not aggressive | Note 2, sub-note 5(i), (ii), (xi), pp.76-77 |
| Impairment assumptions | Generic: "Present realizable market values... reviewed with their corresponding book values, to consider if there exists any indication of an impairment... In case of a permanent impairment... it is dealt in accounts as per Accounting Standards" — no CGU definitions, discount rates, or growth assumptions disclosed | NOT ASSESSABLE beyond generic policy language — specific impairment-testing detail (if any) would sit in the missing Note 12 schedule | Note 2, sub-note 5(iii), p.76 |
| ECL matrix | NOT FOUND IN DOCUMENT — AR pp.78-101 truncated (receivables Note 15). Also note: since the company reports under AS (not Ind AS 109), an Ind AS-style ECL matrix may not exist at all; AS-based provisioning would instead use a provision-for-doubtful-debts approach, detail of which is equally unrecoverable | — | — |
| Ind AS 116 (lease) rate | NOT APPLICABLE — company is on AS, not Ind AS, for FY25. Short-term leases are expensed directly (yearly lease premium charged to P&L; non-refundable/adjustable premium amortised) with no ROU asset/lease-liability recognition on the Balance Sheet | Note 2, sub-note 5(vii), p.77 | |
| Policy changes quantified this year | None found | Consistent with triple-pass Pass 3 conclusion (no item-level restatements) | Note 2.1(b), p.74 |

**2B. RPT map**

| Item | Value | % of Revenue (Rs 142.79 Cr) | Anchor |
|---|---|---|---|
| Long-term Loans & Advances to subsidiaries/JVs (aggregate) | Rs 1.53 Cr FY25 (Rs 1.00 Cr FY24, +52.9%) | 1.07% | Balance Sheet Note 13, p.71 |
| RPT compliance disclosure (s.188/AS 18) note reference | Blank/illegible — cannot locate the specific RPT note | N/A | CARO Annexure A xiii, p.67 |
| Counterparty names, individual amounts, rates, tenure, remuneration/rent/royalty to promoters | NOT FOUND IN DOCUMENT — AR pp.78-101 truncated | — | — |

Value-extraction signals: none quantifiable from readable pages. The only RPT data point is the aggregate loan balance to subsidiaries/JVs, which CARO characterises as "not prima facie prejudicial" with regular interest/principal repayment and no overdue >90 days (CARO Annexure A p.65). No promoter remuneration, rent, or royalty RPT visible anywhere in the readable document (KMP compensation itself sits in the unreadable Corporate Governance Report, pp.3-59).

**2C. Contingent liabilities**

| Item | Value | % of Net Worth (Rs 103.99 Cr) | % of PAT (Rs 16.76 Cr) | Flag threshold (>25% NW / >100% PAT) |
|---|---|---|---|---|
| EPCG export obligation (customs duty clawback exposure if unfulfilled) | Rs 8.09 Cr | 7.8% | 48.3% | Below both thresholds |
| Formal contingent liabilities table (Note 29 — litigation, guarantees, disputed claims) | NOT FOUND IN DOCUMENT — AR pp.78-101 truncated | — | — | Cannot rule out additional undisclosed items pushing past threshold |

The only quantifiable contingent exposure recoverable from this document (the EPCG export obligation) falls below both the 25%-of-net-worth and 100%-of-PAT flag thresholds. However, the complete Note 29 contingent-liabilities/litigation schedule is unavailable, so this is a lower bound, not a total.

**2D. Receivables**

| Metric | FY25 | FY24 | Change |
|---|---|---|---|
| Trade Receivables | Rs 34.93 Cr | Rs 21.53 Cr | +62.3% |
| Revenue (Income from Operations) | Rs 142.79 Cr | Rs 115.03 Cr | +24.1% |
| Days Sales Outstanding (Receivables/Revenue × 365) | 89.3 days | 68.3 days | +21.0 days |

Ageing schedule, >6-month share, single-customer concentration, and unbilled revenue: NOT FOUND IN DOCUMENT — AR pp.78-101 truncated (Note 15). DSO computed independently in this stage from the primary Balance Sheet and P&L (a metric not present in the triple-pass output) confirms the receivables-stretch pattern with a specific magnitude: 21 additional days of sales tied up in receivables.

**2E. Inventory**

| Metric | FY25 | FY24 | Change |
|---|---|---|---|
| Inventories (Balance Sheet) | Rs 26.69 Cr | Rs 14.91 Cr | +79.0% |
| Revenue growth (comparator) | +24.1% | — | — |
| Inventory days (Inventory / COGS proxy × 365; COGS proxy = Consumption & Mfg Expenses + Purchases + Change in Inventories) | 92.0 days | 63.7 days | +28.3 days |

No write-downs disclosed anywhere in the readable Note 2 valuation policy (sub-note 4, p.76) or on the P&L face. FG vs revenue growth mismatch (change-in-inventories line moved from Rs (4.11) Cr FY24 to Rs (6.20) Cr FY25, i.e., a larger build) is consistent with the overall inventory stretch. Category-level breakdown (raw material vs WIP vs finished goods) NOT FOUND IN DOCUMENT.

**2F. Borrowings**

| Item | Finding | Anchor |
|---|---|---|
| Maturity wall (instrument-level, due dates) | NOT FOUND IN DOCUMENT — AR pp.78-101 truncated (Notes 5, 8 schedule detail) | — |
| Covenants near breach | NOT FOUND IN DOCUMENT | — |
| Pledge (of subsidiary/JV/associate securities to raise loans) | None — CARO ix(f) confirms no loans raised on pledge of such securities | CARO Annexure A p.67 |
| Pledge (promoter's own shares) | NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable (shareholding pattern) | — |
| ICDs / loans given (to subsidiaries/JVs) | Rs 1.53 Cr FY25 running current account, CARO confirms not prejudicial, no overdue >90 days | CARO Annexure A p.65; Note 13, p.71 |

**2G. Deferred tax reconciliation**

| Item | FY25 | FY24 |
|---|---|---|
| Deferred Tax Liability (Net), Balance Sheet | Rs 76.28 lakh | Rs 153.83 lakh |
| Deferred Tax Adjustment, P&L | Rs (77.55) lakh (credit) | Rs 38.07 lakh (charge) |

The net DTL balance and the P&L movement are visible on the face of the primary statements, but the qualitative reconciling items (timing differences by category — depreciation, provisions, MAT credit) that would explain both the sub-statutory effective tax rate (18.8%, see Phase 2 verification #9) and the FY25 net credit are NOT FOUND IN DOCUMENT — AR pp.78-101 truncated (Note 6 schedule).

**2H. Exceptional items, goodwill, ESOP, leases, post-balance-sheet events**

| Item | Finding |
|---|---|
| Exceptional items pattern | None visible — no separate exceptional-item line on the P&L face in either FY25 or FY24; clean |
| Goodwill assumptions | No goodwill line anywhere on the Balance Sheet — not applicable (consistent with Note 3's "no investments" declaration and no disclosed acquisitions) |
| ESOP dilution | NOT FOUND IN DOCUMENT — no ESOP note visible; cannot be confirmed as the explanation for the Diluted EPS > Basic EPS anomaly (see Phase 3C) |
| Lease obligations | No ROU asset / lease liability line on the Balance Sheet, consistent with AS-based (not Ind AS 116) treatment — short-term leases expensed directly (Note 2, sub-note 5(vii), p.77) |
| Post-balance-sheet events | NOT FOUND IN DOCUMENT — AR pp.78-101 truncated; confirmed unreachable per triple-pass Pass 3 |

## Phase 2 Cross-Reference with Phase 1 KAMs

No KAMs exist to cross-reference (Phase 1B — none reported, unlisted-company exemption). The closest analogue is the auditor's audit-trail voucher-edit finding (Phase 1, Auditor's Report pp.62-63), which sits adjacent to — but is distinct from — the Note-level findings above (EPS anomaly, negative provisions). All three are independent, unresolved evidence-integrity/accounting-quality items that compound rather than explain one another.

## Reconciliation with Triple-Pass Accounting Quality Score

The triple-pass (B02) scored accounting quality at **3/10**, driven by the disclosure-transparency gap (Notes 3-29 missing) plus the unresolved EPS anomaly and negative-provisions anomaly. This stage's independent re-verification of all 15 findings against the primary statements produces zero discrepancies and surfaces one additional structural point (AS-vs-Ind-AS framework) that reinforces rather than changes the disclosure-transparency conclusion. **This stage's Phase 2 accounting-quality verdict agrees with the triple-pass 3/10 — no disagreement to explain.**

## Phase 2 Summary

**Verdict: 🔴 Red Flag.** Two source-confirmed, unresolved accounting-quality anomalies (Diluted EPS > Basic EPS; negative short-term provisions) sit inside the audited, signed primary statements themselves — not merely a consequence of the missing notes package — combined with a near-total loss of the supporting schedule notes (Notes 3-29) that would normally allow these anomalies, the RPT exposure, and the contingent liabilities to be independently assessed.

**Kill Switch Assessment (informational only)**: Based on Phases 1-2, a human reviewer *would* have reason to pause and seek a clean copy of this AR or direct management clarification before finalising any valuation or quality conclusion, specifically on the EPS reconciliation and the negative provisions movement — both are genuine, arithmetically confirmed anomalies in audited numbers, not document artifacts. Per pipeline rules this is informational only; continuing to Phase 3.

---

# PHASE 3: FINANCIAL STATEMENTS

## 3A Cash Flow (read first)

| Metric | FY25 | FY24 |
|---|---|---|
| CFO (Net cash from Operating activities) | Rs 8.85 Cr | Rs 5.00 Cr |
| PAT | Rs 16.76 Cr | Rs 12.21 Cr |
| **CFO/PAT** | **52.8%** | **40.9%** |
| EBITDA (PBT + Finance costs + Depreciation) | Rs 27.81 Cr | Rs 21.84 Cr |
| **CFO/EBITDA** | **31.8%** | **22.9%** |
| Capex (Purchase of Fixed Assets) | Rs 33.27 Cr | Rs 10.53 Cr |
| FCF (CFO − Capex) | Rs (24.42) Cr | Rs (5.53) Cr |
| Capex / Depreciation | 8.2x | 3.9x |
| M&A spend | None (no investing outflow line for acquisitions; Note 3 confirms "no investments at present") | — |
| Net financing flows | +Rs 39.54 Cr (equity raise dominant) | +Rs 5.38 Cr |
| Cash & equivalents, closing | Rs 16.60 Cr | Rs 0.58 Cr |

Anchors: Cash Flow Statement p.73; PBT/Finance costs/Depreciation from P&L p.72; both flagged consistently by CFO/PAT <0.7 in both years (rule threshold).

**CFO quality checks:**

1. **One-time inflators**: none identified — OCF before working-capital changes (Rs 26.91 Cr) tracks EBITDA reasonably (Rs 27.81 Cr including Other Income), no evidence of a one-time non-operating credit inflating OCF.
2. **Interest classification choice — a genuine, previously unflagged quality issue**: the Cash Flow Statement adds back "Interest & Finance charges-paid Rs 312.23 lakh" as a non-cash adjustment within Operating Activities (to arrive at operating cashflow before working-capital changes), then separately shows "Interest & Finance charges-paid Rs (312.23) lakh" as an outflow within **Financing** Activities (Cash Flow Statement p.73). This means interest paid is classified as a financing outflow, not an operating outflow — a permitted alternative under AS 3 but one that inflates reported CFO relative to the more common practice of treating interest paid as operating. **If interest paid were instead classified as operating (as is common practice among peers), FY25 CFO would fall to Rs 5.73 Cr (Rs 8.85 Cr − Rs 3.12 Cr) and CFO/PAT would fall further to ~34.2%.** This is a material presentation choice that a reader relying on the headline CFO figure alone would miss.
3. **Unsustainable payable stretching**: confirmed and quantified — Trade Payables +118.3% YoY against combined purchase-base growth of only ~25-34% (Consumption & Mfg Expenses +34.4%, Purchases -6.9%); payables days rose from 49.6 to 87.3 (+37.7 days). This is financing roughly half of the receivables/inventory buildup (see Phase 2 #3-4).
4. **Inventory rundown**: opposite pattern — inventory *built up* (+79.0% YoY, +28.3 inventory days), not run down; this is a cash *use*, not a cash-conversion inflator, and is itself part of the weak-conversion story.

**Cash pile trend**: cash rose from Rs 0.58 Cr to Rs 16.60 Cr (28.4x), driven almost entirely by the Rs 57.16 Cr equity/premium infusion rather than operations; net of the Rs 33.27 Cr capex outflow and the Rs 14.50 Cr net debt paydown, Rs 16.02 Cr of the raise remains as a cash cushion at year-end.

## 3B Balance Sheet

**Asset and liability walk (Rs Cr)**

| Line | FY25 | FY24 | YoY |
|---|---|---|---|
| Share Capital | 24.45 | 17.85 | +37.0% |
| Reserves & Surplus | 79.54 | 12.22 | +550.8% |
| **Shareholders' Funds** | **103.99** | **30.07** | **+245.8%** |
| Long-term Borrowings | 20.02 | 25.60 | -21.8% |
| Deferred Tax Liability (Net) | 0.76 | 1.54 | -50.4% |
| Long-term Provisions | 0.17 | 0.08 | +116.2% |
| **Non-Current Liabilities** | **20.95** | **27.21** | **-23.0%** |
| Short-term Borrowings | 6.95 | 15.88 | -56.2% |
| Trade Payables | 25.31 | 11.59 | +118.3% |
| Other Current Liabilities | 1.62 | 1.09 | +48.8% |
| Short-term Provisions | (0.27) | 0.66 | anomalous — see Phase 2 #5 |
| **Current Liabilities** | **33.61** | **29.22** | **+15.0%** |
| **Total Equity & Liabilities** | **158.55** | **86.51** | **+83.2%** |
| PP&E | 69.90 | 40.83 | +71.2% |
| Capital WIP | 2.33 | 2.18 | +6.9% |
| Long-term Loans & Advances | 1.53 | 1.00 | +52.9% |
| **Non-Current Assets** | **73.76** | **43.01** | **+71.5%** |
| Inventories | 26.69 | 14.91 | +79.0% |
| Trade Receivables | 34.93 | 21.53 | +62.3% |
| Cash & Equivalents | 16.60 | 0.58 | +2760.1% |
| Short-term Loans & Advances | 6.57 | 5.48 | +19.9% |
| **Current Assets** | **84.79** | **42.50** | **+99.5%** |
| **Total Assets** | **158.55** | **86.51** | **+83.2%** |

Balance sheet foots correctly both years (Total Equity & Liabilities = Total Assets); the negative Short-term Provisions figure is required for the Current Liabilities subtotal to reconcile (confirmed anomaly, not a footing error).

**Key ratio table**

| Ratio | FY25 | FY24 |
|---|---|---|
| D/E (Total Debt / Equity) | 0.26x | 1.38x |
| Net Debt / EBITDA | 0.37x | 1.87x |
| Current Ratio | 2.52x | 1.45x |
| Quick Ratio | 1.73x | 0.94x |
| Interest Coverage (EBIT/Interest) | 7.61x | 7.11x |
| ROCE (EBIT / Closing Capital Employed) | 19.0% | — |
| ROCE (EBIT / Average Capital Employed) | 26.1% | — |
| ROE (PAT / Closing Equity) | 16.1% | — |
| ROE (PAT / Average Equity) | 25.0% | — |
| Goodwill % of Net Worth | 0% (no goodwill line) | 0% |

Anchors: Balance Sheet p.71; P&L p.72 (EBIT = PBT + Finance costs). ROE/ROCE shown on both closing- and average-equity bases because the ~Rs 57 Cr equity raise occurred mid-year (28 June 2024, Note 1 p.74), materially distorting a single-basis calculation; the true run-rate likely sits between the two.

**DuPont decomposition (FY25, closing basis)**: ROE 16.1% = Net Margin 11.74% (PAT/Revenue) × Asset Turnover 0.90x (Revenue/Total Assets) × Equity Multiplier 1.52x (Total Assets/Equity). **ROE is margin-driven, not leverage-driven** — the equity multiplier of 1.52x is low (consistent with the FY25 deleveraging and equity infusion), so the improvement in ROE this year reflects operating profitability and capital-structure delevering, not increased financial leverage. This is a clean signal on the balance-sheet side.

## 3C P&L

**Line walk (Rs Cr), FY25 vs FY24**

| Line | FY25 | FY24 | YoY |
|---|---|---|---|
| Income from Operations | 142.79 | 115.03 | +24.1% |
| Other Income | 2.41 | 1.08 | +122.6% |
| Total Income | 145.20 | 116.11 | +25.1% |
| Consumption & Mfg Expenses | 93.65 | 69.67 | +34.4% |
| Purchases — Finished/Traded goods | 18.43 | 19.80 | -6.9% |
| Change in inventories (FG/WIP/Stock-in-trade) | (6.20) | (4.11) | larger build |
| Employee Benefits Expenses | 5.71 | 4.28 | +33.5% |
| Finance Costs | 3.12 | 2.69 | +16.1% |
| Depreciation & Amortization | 4.05 | 2.73 | +48.6% |
| Other Expenses | 5.81 | 4.64 | +25.1% |
| Total Expenditure | 124.57 | 99.68 | +25.0% |
| PBT | 20.63 | 16.43 | +25.6% |
| Total Tax | 3.87 | 4.22 | -8.3% |
| **PAT (Transferred to Reserves)** | **16.76** | **12.21** | **+37.3%** |

**Other Income composition and % of PBT**: Rs 2.41 Cr, or **11.7% of PBT** — below the >20% flag threshold, but only Rs 0.86 Cr (36% of the total) is confirmed as interest income (Cash Flow Statement p.73); the remaining ~Rs 1.55 Cr composition is unexplained (Phase 2 #13). Growth of +122.6% YoY, well ahead of revenue growth, means this line's contribution to PAT growth is disproportionate and its recurring-vs-one-time character cannot be verified.

**Margin waterfall**: EBITDA-margin-ex-Other-Income was **17.8% FY25 vs 18.0% FY24** — essentially flat to slightly down, despite Consumption & Mfg Expenses growing 34.4% against 24.1% revenue growth, i.e., core operating margin faced mild compression that is masked at the PAT level by (a) the surge in Other Income and (b) the sub-statutory effective tax rate. PAT growth of +37.3% materially outpaces revenue growth of +24.1% and even PBT growth of +25.6%, with the wedge between PBT growth and PAT growth attributable to the falling effective tax rate (22.9% FY24 → 18.8% FY25, unreconciled — Phase 2 #9/2G).

**Exceptional items 3-year pattern**: none visible in either year presented (no exceptional-item line on the P&L face); prior years beyond FY24 NOT FOUND IN DOCUMENT (only two years of primary statements presented).

**Tax rate consistency**: FY24 effective rate ≈ 22.9% (Rs 4.22 Cr / Rs 16.43 Cr — using total tax including the Rs (0.20) lakh earlier-year write-back and Rs 38.07 lakh deferred charge), FY25 ≈ 18.8% — a genuine ~4.1pp drop, unreconciled from readable pages (deferred tax reconciliation, Note 6, truncated).

**Basic vs Diluted EPS gap**: FY25 Diluted (Rs 8.12) *exceeds* Basic (Rs 6.85) by Rs 1.27 — the reverse of the normal direction and arithmetically anomalous under AS 20 (dilutive instruments should only ever reduce or leave unchanged, never increase, EPS). FY24 shows no dilution (Basic = Diluted = Rs 6.84), so this is a FY25-specific, unexplained item. **Confirmed independently in this stage via direct primary-statement read — this is the single highest-priority open item in the entire AR deep dive** (P&L p.72, Note 26).

## Phase 3 Cross-Reference with Phases 1-2

- The CFO/PAT weakness (Phase 3A) is the same underlying working-capital pattern already surfaced via the notes cross-check in Phase 2 (#3-4) — fully consistent, no contradiction, and now quantified with an additional dimension (the interest-paid financing-classification effect) not previously surfaced by the triple-pass.
- The EPS anomaly (Phase 3C) is identical to Phase 2 finding #2 — independently reconfirmed at the primary-statement level, removing any possibility this is an OCR/extraction artifact from the triple-pass; it is present in the signed, audited P&L itself.
- The negative Short-term Provisions balance (Phase 2 #5) is confirmed again here via the Balance Sheet cross-footing exercise (Phase 3B) — same conclusion, independently reached.
- No new contradictions found between Phase 3 and Phases 1-2.

## Phase 3 Summary

**Verdict: 🔴 Red Flag.** Weak and worsening cash conversion (CFO/PAT 52.8%, or ~34.2% if interest paid is reclassified as operating), the confirmed EPS anomaly, the confirmed negative-provisions anomaly, receivables/inventory/payables all stretching well beyond revenue growth, and an unreconciled ~4pp drop in effective tax rate together outweigh the genuinely clean balance-sheet-strength signals (low leverage, strong liquidity ratios, margin-driven not leverage-driven ROE).

**Kill Switch Assessment (informational only)**: Based on Phases 1-3, a human reviewer *would* have reason to pause before proceeding to valuation, specifically to obtain (a) the EPS reconciliation, (b) the receivables ageing/customer-concentration detail, and (c) confirmation of the interest-paid cash-flow classification's effect on sustainable operating cash generation. Per pipeline rules this is informational only; continuing to Phase 4.

---

# PHASE 4: RISK FACTORS & MD&A

## 4A Disclosed Risks

**NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable (corrupted font).** The Risk Factors section and MD&A, wherever they sit within the Board's Report, are entirely inaccessible. No risk-factor text of any kind could be read or verified.

## 4B Missing Risks (risks evidenced by Phases 1-3 that a complete risk section would need to address)

Whether the actual (unreadable) risk-factor section discloses these cannot be verified either way — this list documents what the *evidence* from Phases 1-3 indicates should be addressed, not a confirmed omission.

| Risk (evidenced) | Evidence anchor |
|---|---|
| Working-capital/cash-conversion risk: receivables +62.3%, inventory +79.0%, payables +118.3% YoY vs 24.1% revenue growth; CFO/PAT 52.8% (or ~34.2% on an interest-paid-as-operating basis) | Balance Sheet p.71; Cash Flow Statement p.73 |
| EPS computation / accounting-quality risk: Diluted EPS exceeds Basic EPS, AS 20-anomalous | P&L p.72, Note 26 |
| Negative short-term provisions balance, unexplained | Balance Sheet p.71, Note 11 |
| EPCG export-obligation clawback risk (Rs 8.09 Cr customs duty exposure; drafting inconsistency in the fulfilment-block schedule itself) | Note 2.3(b), pp.75-76 |
| Related-party/subsidiary lending concentration combined with absence of consolidated financial statements | CARO Annexure A p.65, p.68; Note 13, p.71 |
| Interest-paid financing-classification choice masking the true run-rate of operating cash generation | Cash Flow Statement p.73 |
| Single-family board concentration (Managing Director and a Director share the "Lekha" surname) | Balance Sheet/P&L signature blocks, p.71-72 (partial evidence only — full promoter/shareholding analysis NOT FOUND, AR pp.3-59 unreadable) |

## 4C MD&A Deep Dive

NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable. Industry claims, growth/margin explanations, external-factor attribution patterns, forward guidance, and segment analysis are entirely inaccessible. The only substantive business-description text available in the entire document is Note 1 (Corporate Information, p.74): the company manufactures "components made of steel and other metals, primarily for the automotive industry," operating two factories in Chakan (Pune suburbs, Maharashtra), one factory in Mapedu, Sriperumbudur, Tamil Nadu (began production FY24), and a third unit under construction in Pune suburbs during FY24 that began production during FY25. This is factual corporate information, not MD&A narrative, and carries no forward guidance or credibility claims to test.

**Guidance table**: empty — no forward guidance of any kind is recoverable from this document.

## 4D Tone and Credibility Ratings

NOT ASSESSABLE — no narrative text (Chairman's letter, MD&A, Board's Report) is readable anywhere in this document (AR pp.3-59 unreadable; p.1 is a procedural NSE filing letter, not narrative). Transparency, consistency, specificity, accountability, and capital-allocation-sense ratings cannot be produced without a text base to rate.

## Phase 4 Summary

**Verdict: NOT ASSESSABLE — AR pp.3-59 unreadable.** No contradiction check against Phases 1-3 is possible because there is no Phase 4 narrative text to compare.

**Kill Switch Assessment (informational only)**: Based on Phases 1-4, a human reviewer would note that the complete absence of MD&A/risk-factor text is itself a document-completeness problem requiring a clean AR copy before any qualitative management-credibility judgment can be formed — this is a mechanical evidence gap, not a company-quality signal, and does not by itself change the trajectory from Phases 1-3. Continuing to Phase 5.

---

# PHASE 5: CORPORATE GOVERNANCE & BOARD

## 5A Board Composition

NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable (Corporate Governance Report). Tenure, other directorships, attendance percentages, and independence status of any board member cannot be determined.

**Partial evidence only** — from the Balance Sheet/P&L signature blocks (p.71, p.72) and the NSE cover letter (p.1), the following individuals and roles are confirmed:

| Name | Role | DIN/ACS |
|---|---|---|
| Saksham Lekha | Managing Director | DIN 07389575 |
| Ashwani Lekha | Director | DIN 07389860 |
| Sanjeev Verma | CFO / Director | DIN 00296825 |
| Mudit Johri | Company Secretary | ACS 67471 |
| Asha Narang | Director (signatory to NSE filing letter) | DIN 00296714 |

The shared surname "Lekha" for the Managing Director and one Director is consistent with promoter-family board representation but is not, on its own, evidence of a governance problem; full board size, independent-director count, and cross-board memberships are NOT FOUND IN DOCUMENT.

## 5B Committee Analysis

NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable. The only committee-related fact available is negative: CARO Annexure A clause xiii states Section 177 Audit Committee requirements are "not applicable" because the company was "not being a listed company" as of the 16 May 2025 report date (CARO Annexure A p.67) — consistent with Phase 1B's KAM-exemption finding. Post-listing (by September 2025 per the cover letter), an Audit Committee should be mandatory for FY26; whether one now exists is unverifiable from this document.

## 5C Compensation

NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable and pp.78-101 truncated. No KMP compensation table, comp-as-%-of-PAT, CEO-to-median multiple, promoter-family payroll figures, or ESOP dilution detail is recoverable.

## 5D Shareholding

NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable (MGT-9/shareholding pattern). Promoter %, YoY change, pledge status, and FII/DII trends cannot be determined. **No evidence of promoter pledge or promoter selling was found because the source data is entirely absent — this is a gap, not a clean bill of health, and should not be read as either a positive or negative signal.**

## 5E Governance Red-Flag Checklist

| Item | Finding | Anchor |
|---|---|---|
| Whistleblower complaints | None received by the auditor during the year | CARO Annexure A xi(c), p.67 |
| SEBI actions | NOT FOUND IN DOCUMENT | — |
| RPT committee / Audit Committee | Not applicable at report date (unlisted); status post-listing unverifiable | CARO Annexure A xiii, p.67 |
| Auditor fee ratio (non-audit vs audit) | NOT FOUND IN DOCUMENT | — |
| CSR compliance | Rs 18.04 Lakh paid to Swachh Paryavaran Trust per s.135(5); no unspent-amount adverse remark; mandated base amount (2% of average net profits) not independently verifiable | CARO Annexure A xx, p.68 |
| Section 143(12) fraud reporting | None — no fraud noticed/reported; no ADT-4 filed | CARO Annexure A xi(a)-(b), p.67 |
| Material subsidiary auditor / consolidation | No consolidated financial statements prepared despite confirmed subsidiary/JV relationships; s.129(3) exemption basis not stated | CARO Annexure A xxi, p.68; Note 13, p.71 |

## Phase 5 Summary

**Verdict: NOT ASSESSABLE — AR pp.3-59 unreadable**, with the CARO-derived negative-assurance items (no fraud, no whistleblower complaints, CSR paid, ICFR effective per Phase 1) as the only positive governance signals available, and the CFS/subsidiary question as the only negative signal recoverable from this stage's own evidence base.

**Kill Switch Assessment (informational only)**: Based on Phases 1-5, a human reviewer would flag the complete absence of board/committee/compensation/shareholding data as a material evidence gap for any governance-driven investment decision, but this is a document-completeness issue, not an adverse governance finding on its own. Continuing to Phase 6.

---

# PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

## 6A Narrative vs Reality

NOT FOUND IN DOCUMENT — no Chairman's letter is present or accessible. Page 1 is a procedural cover letter to NSE announcing the 9th AGM notice and e-Voting cut-off date, signed by Asha Narang (Director), dated 04 September 2025 — administrative correspondence, not a shareholder narrative. Any actual Chairman's/MD's letter would sit within the unreadable pp.3-59 range (Board's Report front matter). No prominent claims exist to cross-reference against Phases 1-5 financial reality.

## 6B Strategic Priorities

NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable. The only strategy-adjacent fact recoverable anywhere in the document is factual, from Note 1 (p.74): a third manufacturing unit (Pune suburbs) began construction in FY24 and began production in FY25, alongside continuing operations at two existing Chakan units and the Tamil Nadu unit that started production in FY24. This is confirmed capital deployment (capex of Rs 33.27 Cr in FY25, Phase 3A) consistent with an active capacity-expansion strategy, but no qualitative strategic-priority statement or capital-allocation rationale is available to assess specificity or execution evidence beyond the capex figure itself.

## 6C Metrics Showcased vs Conspicuously Absent

NOT ASSESSABLE — no front-matter/Chairman's-letter text exists to compare against.

## 6D Tone and Priority Drift vs Prior Year

NOT ASSESSABLE — no prior-year Chairman's letter or this year's letter is available for comparison.

## Phase 6 Summary

**Verdict: NOT ASSESSABLE — AR pp.3-59 unreadable; no Chairman's letter recoverable in this document.** The only confirmed front-matter fact is the private-to-public conversion and NSE listing context (cover letter p.1; Note 1, p.74), which is consistent with, and corroborated by, the capital-raise and deleveraging findings in Phases 2-3.

---

# PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP** | **WATCHLIST** | (1) Revenue +24.1%, PAT +37.3%, PBT +25.6% — genuine growth at a reasonable-looking multiple set-up (small/micro-cap, recent listing) is the core thesis fit; (2) but earnings quality is compromised by the unresolved EPS anomaly, weak/questionable cash conversion (52.8%, ~34.2% adjusted), and a falling, unreconciled effective tax rate inflating PAT growth beyond PBT growth; (3) capex-led margin base (Rs 33.27 Cr FY25, 8.2x depreciation) has not yet proven out in ROCE terms on a closing basis (19.0%; 26.1% on an average-capital-employed basis inflated by the mid-year equity raise) — GARP quality gate requires the EPS and cash-conversion questions resolved before this converts to a clean PASS |
| **Turnaround** | **WATCHLIST** | (1) Clear deleveraging signal: D/E fell from 1.38x to 0.26x, Net Debt/EBITDA from 1.87x to 0.37x, funded by a Rs 57.16 Cr equity raise tied to the private-to-public conversion (28 June 2024) — a genuine balance-sheet reset; (2) DuPont shows ROE is margin-driven not leverage-driven (equity multiplier only 1.52x), a clean signal that the improvement is not manufactured through gearing; (3) however, the turnaround is not yet cash-flow-confirmed — OCF/PAT of 52.8% (or ~34.2% adjusted) means the earnings improvement has not yet translated into commensurate cash generation, and the working-capital stretch (receivables/inventory outpacing revenue) is the opposite of what a clean turnaround typically shows in year one |
| Value+Quality | FAIL | Accounting-quality score 3/10 (this stage, reconciled with triple-pass); unresolved EPS and provisions anomalies fail the "quality" leg outright regardless of any value case |
| Capex-Led Growth | WATCHLIST | Capex/Depreciation of 8.2x and a third-unit ramp-up (Note 1, p.74) fit the pattern, but ROCE and revenue-per-unit-of-capex have not yet been demonstrated over multiple years — only one year of aggressive capex visible in this document |
| Cash Flow Compounder | FAIL | CFO/PAT of 52.8% (52.8% best case, ~34.2% on an interest-paid-as-operating basis) is well below the profile this strategy requires; FCF is deeply negative (Rs (24.42) Cr) in the expansion year |
| Contrarian | NOT ASSESSABLE | Requires sentiment/valuation context not available from this AR-only stage |
| Insider Confidence | NOT ASSESSABLE | Promoter shareholding/pledge/buying-selling data entirely NOT FOUND IN DOCUMENT (AR pp.3-59 unreadable) |
| Guidance Divergence | NOT ASSESSABLE | No forward guidance recoverable (Phase 4C) to test against delivery |

---

# PHASE 8: FINAL VERDICT DASHBOARD

## Company Snapshot

OBSC Perfection Ltd (OBSCP), CIN U27100DL2017PLC314606, incorporated 17 March 2017, manufactures steel and other-metal components primarily for the automotive industry. Converted from private to public limited company effective 28 June 2024; listed on NSE (scrip symbol OBSCP) by September 2025 per the cover letter accompanying this FY25 AR. Three manufacturing units: two at Chakan (Pune suburbs, Maharashtra), one at Mapedu, Sriperumbudur, Tamil Nadu (production started FY24), and a third Pune-suburb unit (construction started FY24, production started FY25). FY25 revenue Rs 142.79 Cr (+24.1% YoY), PAT Rs 16.76 Cr (+37.3% YoY).

## Phase-Wise Verdict Summary

| Phase | Verdict |
|---|---|
| 1. Auditor's Report & CARO | 🟡 Watch |
| 2. Notes to Financial Statements | 🔴 Red Flag |
| 3. Financial Statements | 🔴 Red Flag |
| 4. Risk Factors & MD&A | NOT ASSESSABLE — AR pp.3-59 unreadable |
| 5. Corporate Governance & Board | NOT ASSESSABLE — AR pp.3-59 unreadable |
| 6. Chairman's Letter & Front Matter | NOT ASSESSABLE — no letter recoverable |
| 7. Best-fit strategy | GARP / Turnaround, both WATCHLIST |

## Overall Quality Score: 4/10

| Component | Weight | Score /10 | Basis |
|---|---|---|---|
| Governance | 25% | 3 | Clean CARO negative-assurance items (no fraud, no whistleblower complaints, ICFR effective) but total absence of board/committee/compensation/shareholding evidence, plus the unresolved CFS-with-subsidiaries question |
| Accounting quality | 25% | 3 | Reconciled with triple-pass 3/10 — unresolved EPS anomaly, unresolved negative-provisions anomaly, entire Notes 3-29 schedule package missing, AS-not-Ind-AS framework confirmed |
| Balance sheet | 25% | 6 | Genuinely strong: D/E 0.26x, current ratio 2.52x, quick ratio 1.73x, interest coverage 7.6x, ROE margin-driven not leverage-driven; offset by the negative-provisions anomaly and unresolved CFS question |
| Earnings quality | 25% | 3 | CFO/PAT 52.8% (or ~34.2% adjusted for interest-paid classification), EPS anomaly, unreconciled effective-tax-rate drop, unexplained Other Income surge, mild core-margin compression masked at the PAT line |
| **Overall** | | **4 (rounded from 3.75)** | |

## Top 3 Strengths

1. **Balance-sheet reset is genuine and well-evidenced**: D/E fell from 1.38x to 0.26x, Net Debt/EBITDA from 1.87x to 0.37x, current ratio from 1.45x to 2.52x, funded by a Rs 57.16 Cr equity raise tied to the private-to-public conversion — fully cross-verified across the Balance Sheet, Cash Flow Statement, and Note 1 (Balance Sheet p.71; Cash Flow Statement p.73; Note 1, p.74).
2. **No adverse CARO remarks, no fraud, no default**: clean CARO 2020 across all 21 clauses, unmodified ICFR opinion, no willful-defaulter designation, no cash losses in either presented year (CARO Annexure A pp.64-68; Annexure B p.70).
3. **ROE is margin-driven, not leverage-driven**: DuPont decomposition shows equity multiplier of only 1.52x FY25, meaning the profitability improvement reflects genuine operating performance rather than financial engineering (Balance Sheet p.71; P&L p.72).

## Top 3 Red Flags

1. **Diluted EPS (Rs 8.12) exceeds Basic EPS (Rs 6.85), FY2025** — arithmetically anomalous under AS 20, confirmed genuine and unexplained across three independent verification passes (triple-pass Notes stage + this stage's independent primary-statement re-read), unresolved, and the reconciling detail (Note 26 weighted-average share count) sits in a truncated section of the source document (P&L p.72, Note 26).
2. **Weak and possibly overstated cash conversion**: CFO/PAT of 52.8% falls to ~34.2% if interest paid is reclassified from Financing to Operating Activities (a presentation choice this document makes but many peers do not); receivables (+62.3%), inventory (+79.0%), and payables (+118.3%) are all stretching materially faster than the 24.1% revenue growth (Cash Flow Statement p.73; Balance Sheet p.71).
3. **Negative Short-term Provisions balance** (Rs (0.27) Cr FY25 vs Rs 0.66 Cr FY24), confirmed arithmetically real via balance-sheet cross-footing, with no movement schedule available to explain the swing (Balance Sheet p.71, Note 11).

## Key Monitorables for Next Quarter/Year

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| EPS reconciliation (Basic vs Diluted) | Any restatement, correction, or weighted-average share disclosure in FY26 filings or a clean FY25 AR copy | FY26 AR Note 26 (or a re-sourced clean FY25 AR) | Resolves the highest-priority open accounting-quality item in this deep dive |
| Trade Receivables DSO | Continued rise above 89.3 days (FY25) signals deteriorating collectability | FY26 Balance Sheet / receivables ageing note | Direct cash-conversion and quality-of-earnings driver |
| Trade Payables days / MSME ageing | Any Section-16-interest disclosure or overdue amount beyond stipulated terms | FY26 Note 9 / MSME note | Payables stretch is currently financing roughly half the working-capital buildup — a reversal would create a liquidity squeeze |
| Short-term Provisions balance | Return to a positive, explained balance | FY26 Balance Sheet / Note 11 movement schedule | Confirms whether the FY25 anomaly was a one-off reclassification or a recurring issue |
| CFO/PAT and interest-paid cash-flow classification | Sustained CFO/PAT below 0.7x on either classification basis | FY26 Cash Flow Statement | Direct earnings-quality read; also test whether the financing-classification choice persists |
| Ind AS transition status | Any first-time-adoption note or confirmation of continued AS-basis reporting | FY26 AR Note 1/2 | Post-listing, Ind AS applicability should be confirmed; affects comparability of all ratios computed here |
| EPCG export obligation progress | Actual exports vs the Rs 8.09 Cr obligation at each block review (1st block: years 1-4 from 26-12-2024) | FY26-29 AR contingent liability note / DGFT correspondence | Duty-plus-penalty clawback risk if the obligation (as clarified) is not met |
| Consolidated financial statements | Whether CFS appears in FY26 given confirmed subsidiary/JV relationships | FY26 AR | Resolves the open s.129(3) compliance question raised in Phase 1F |

## One-Line Verdict

Clean audit and a genuine balance-sheet reset are undercut by an unresolved EPS anomaly and weak cash conversion; best-fit strategy: GARP/Turnaround, both WATCHLIST pending resolution.

---

```yaml
stage: B03-ardeep
company: "OBSCP"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps:
  - "AR pp.3-59: corrupted/garbled font encoding, unreadable even visually (Board's Report, MD&A, Corporate Governance Report, MGT-9/shareholding pattern) — Phases 4, 5, 6 narrative content NOT FOUND IN DOCUMENT throughout"
  - "AR pp.78-101: blank/truncated in source PDF — remainder of Note 2 policy topics plus the entire numbered schedule-notes package (Note 3 through at least Note 29: RPT detail, contingent liabilities/litigation, receivables ageing, inventory category detail, subsidiaries/investments detail, borrowings instrument table, payables MSME ageing, provisions movement, deferred tax reconciliation detail, revenue disaggregation, EPS weighted-average reconciliation, CSR base-amount computation, capital commitments, segment reporting) — all marked NOT FOUND IN DOCUMENT, none estimated"
  - "RPT note number itself is blank/illegible in the source document (CARO Annexure A para xiii, p.67) — not recoverable even with a complete PDF unless a clean copy is sourced"
  - "Auditor tenure/rotation year and audit-vs-non-audit fee ratio: NOT FOUND IN DOCUMENT — normally in Board's Report/Corporate Governance Report (pp.3-59 unreadable) or Notes schedule (pp.78-101 truncated)"
  - "Consolidated financial statements: not prepared despite confirmed subsidiary/JV relationships (CARO iii, xxi); s.129(3) exemption basis NOT FOUND IN DOCUMENT"
  - "Promoter shareholding %, pledge status, FII/DII trends, KMP compensation, board tenure/attendance: NOT FOUND IN DOCUMENT — AR pp.3-59 unreadable"
flags:
  - {type: FLAG-CASH, reason: "OCF Rs 8.85 Cr vs PAT Rs 16.76 Cr (52.8% conversion), falling further to ~34.2% if interest paid is reclassified from Financing to Operating Activities per the cash flow statement's own presentation choice; Trade Receivables +62.3% YoY (DSO 89.3 vs 68.3 days) and Inventory +79.0% YoY (92.0 vs 63.7 days) vs 24.1% revenue growth; Trade Payables +118.3% YoY (87.3 vs 49.6 days) partially funding the buildup; ageing/ECL detail unrecoverable (Notes 14/15 truncated) — caps at PROCEED WITH CAVEATS"}
  - {type: FLAG-ACCOUNTING-QUALITY, reason: "Diluted EPS (Rs 8.12) exceeds Basic EPS (Rs 6.85) FY2025, independently reconfirmed via direct primary-statement re-read in this stage (P&L p.72, Note 26); arithmetically anomalous under AS 20; weighted-average share reconciliation unrecoverable"}
  - {type: FLAG-ACCOUNTING-QUALITY, reason: "Short-term Provisions balance is negative Rs (0.27) Cr FY25 vs positive Rs 0.66 Cr FY24, independently reconfirmed via balance-sheet cross-footing in this stage; cause unrecoverable (Note 11 movement schedule truncated)"}
  - {type: FLAG-CFO-QUALITY, reason: "Interest paid Rs 3.12 Cr classified as a Financing outflow rather than Operating outflow in the Cash Flow Statement (p.73) — a permitted but non-standard presentation choice that inflates reported CFO; reclassifying to Operating drops CFO/PAT from 52.8% to ~34.2%"}
phase_verdicts: {p1: "Watch", p2: "Red Flag", p3: "Red Flag", p4: "NOT ASSESSABLE - AR pp.3-59 unreadable", p5: "NOT ASSESSABLE - AR pp.3-59 unreadable", p6: "NOT ASSESSABLE - no Chairman's letter recoverable", p7_best_fit: "GARP/Turnaround - both WATCHLIST"}
overall_quality: 4            # /10 (governance 3, accounting 3, balance sheet 6, earnings 3; average 3.75 rounded to 4)
quality_components: {governance: 3, accounting: 3, balance_sheet: 6, earnings: 3}
kill_switch_notes:
  - "Phase 1: would not stop - clean opinion, unmodified ICFR, no fraud/default/qualified CARO remark; audit-trail and CFS-exemption items warrant follow-up but not a halt"
  - "Phase 2: would pause - EPS reconciliation and negative-provisions movement are genuine, arithmetically confirmed anomalies in audited numbers requiring a clean AR copy or management clarification before finalising valuation/quality conclusions"
  - "Phase 3: would pause - EPS reconciliation, receivables ageing/concentration, and interest-paid cash-flow classification effect on sustainable operating cash generation should be obtained before proceeding to valuation"
  - "Phase 4: complete absence of MD&A/risk-factor text is a document-completeness problem, not a company-quality signal, requiring a clean AR copy before qualitative management-credibility judgment"
  - "Phase 5: complete absence of board/committee/compensation/shareholding data is a material evidence gap for governance-driven decisions, not an adverse finding on its own"
triple_pass_verification:
  verified: 15                # of 15
  discrepancies: []
missing_risks:
  - {risk: "Working-capital/cash-conversion risk: receivables +62.3%, inventory +79.0%, payables +118.3% YoY vs 24.1% revenue growth; CFO/PAT 52.8% (~34.2% adjusted)", evidence: "Balance Sheet p.71; Cash Flow Statement p.73"}
  - {risk: "EPS computation/accounting-quality risk: Diluted EPS exceeds Basic EPS, AS 20-anomalous", evidence: "P&L p.72, Note 26"}
  - {risk: "Negative short-term provisions balance, unexplained", evidence: "Balance Sheet p.71, Note 11"}
  - {risk: "EPCG export-obligation clawback risk (Rs 8.09 Cr customs duty exposure; drafting inconsistency in the fulfilment-block schedule)", evidence: "Note 2.3(b), pp.75-76"}
  - {risk: "Related-party/subsidiary lending concentration combined with absence of consolidated financial statements", evidence: "CARO Annexure A p.65, p.68; Note 13, p.71"}
  - {risk: "Interest-paid financing-classification choice masking the true run-rate of operating cash generation", evidence: "Cash Flow Statement p.73"}
  - {risk: "Single-family board concentration (Managing Director and a Director share the Lekha surname)", evidence: "Balance Sheet/P&L signature blocks, p.71-72 - partial evidence only"}
guidance_table: []            # No forward guidance recoverable - AR pp.3-59 unreadable (MD&A/Board's Report)
monitorables:
  - {metric: "EPS reconciliation (Basic vs Diluted)", threshold: "Any restatement/correction or weighted-average share disclosure", where: "FY26 AR Note 26 or a re-sourced clean FY25 AR", why: "Resolves the highest-priority open accounting-quality item"}
  - {metric: "Trade Receivables DSO", threshold: "Continued rise above 89.3 days (FY25)", where: "FY26 Balance Sheet / receivables ageing note", why: "Direct cash-conversion and quality-of-earnings driver"}
  - {metric: "Trade Payables days / MSME ageing", threshold: "Section-16-interest disclosure or overdue beyond stipulated terms", where: "FY26 Note 9 / MSME note", why: "Payables stretch currently finances roughly half the WC buildup; reversal risk"}
  - {metric: "Short-term Provisions balance", threshold: "Return to positive, explained balance", where: "FY26 Balance Sheet / Note 11", why: "Confirms whether FY25 anomaly was one-off or recurring"}
  - {metric: "CFO/PAT and interest-paid classification", threshold: "Sustained CFO/PAT below 0.7x on either classification basis", where: "FY26 Cash Flow Statement", why: "Direct earnings-quality read"}
  - {metric: "Ind AS transition status", threshold: "First-time-adoption note or confirmation of continued AS-basis reporting", where: "FY26 AR Note 1/2", why: "Post-listing Ind AS applicability affects comparability of all ratios"}
  - {metric: "EPCG export obligation progress", threshold: "Actual exports vs Rs 8.09 Cr obligation at each block review", where: "FY26-29 AR contingent liability note / DGFT correspondence", why: "Duty-plus-penalty clawback risk if unmet"}
  - {metric: "Consolidated financial statements", threshold: "CFS appears in FY26 given confirmed subsidiary/JV relationships", where: "FY26 AR", why: "Resolves open s.129(3) compliance question"}
strengths_top3:
  - "Balance-sheet reset genuine and fully cross-verified: D/E 1.38x to 0.26x, Net Debt/EBITDA 1.87x to 0.37x, current ratio 1.45x to 2.52x, funded by Rs 57.16 Cr equity raise tied to private-to-public conversion"
  - "No adverse CARO remarks across all 21 clauses, unmodified ICFR opinion, no fraud, no default, no cash losses either year"
  - "ROE is margin-driven not leverage-driven per DuPont decomposition (equity multiplier only 1.52x FY25)"
red_flags_top3:
  - "Diluted EPS (Rs 8.12) exceeds Basic EPS (Rs 6.85) FY2025, AS 20-anomalous, confirmed genuine across three independent verification passes, unresolved"
  - "Cash conversion weak and possibly overstated: CFO/PAT 52.8% falls to ~34.2% if interest paid reclassified from Financing to Operating; receivables/inventory/payables all stretching far faster than revenue"
  - "Negative Short-term Provisions balance Rs (0.27) Cr FY25, confirmed arithmetically real via balance-sheet cross-footing, mechanism unexplained"
best_fit_strategy: "GARP / Turnaround (both WATCHLIST, not yet PASS)"
one_line_verdict: "Clean audit and genuine balance-sheet reset undercut by unresolved EPS anomaly and weak cash conversion."
```
