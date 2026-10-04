# STAGE 2 NOTES, PASS 3 OF 3 AND CONSOLIDATION: Kwick Forensic Solutions Ltd (KWICK), run 2026-10-04

Source: final Prospectus 31-Aug-2026 (AR substitute), PDF pages. Unit: Rs lakh as printed. Indian GAAP (AS), standalone. "Computed" means my arithmetic on printed figures. Full detail sits in `02-notes-pass1.md` and `02-notes-pass2.md`; this file is the consolidated stage 2 report.

## PASS 3: PATTERN RE-READ

Method: contradictions between notes, notes against primary statements, deliberately thin disclosure, restatements, post-balance-sheet events, going concern. Pass 3 yields one reconciliation, one cluster finding and two tie-outs.

### P3-1. Pass 1 vs Pass 2 mismatch resolved: "Import of services" (Annexure V xvii, p.246)
- Pass 1 gave 643.03 / 632.14 / 507.70. Pass 2 gave 643.03 / 629.01 / 501.39. Source prints Import of Services 643.03 / 629.01 / 501.39, Freight 3.13 (FY25) and 6.31 (FY24), totals 643.03 / 632.14 / 507.70 (p.246). Both are right. The service line is the Pass 2 figure; Pass 1 used the total. Customs duty comparison in Pass 2 stands. 🟢 reconciliation, 🟡 label mismatch remains.

### P3-2. Disclosure is thin exactly where growth is made (pattern, not a defect proof)
Mandated items are given in depth: full RPT table, 3-year statutory default table with dates (RF5), 3-year ratio table, ageing, gratuity assumptions. Items that would let an investor test the growth are absent:

| Item | Status |
|---|---|
| Customer names, top 10 split government/private | NOT FOUND (top 10 anonymous, 77.64%, pp.160-161) |
| Product line by buyer type | NOT FOUND (RF3 p.24 gives lines only) |
| B2C definition | NOT FOUND (p.160) |
| Doubtful-debt/ECL rule, ageing basis | NOT FOUND (pp.229-231) |
| Contracts on percentage-of-completion, amount | NOT FOUND (policy allows two bases) |
| Software CWIP purpose, vendors, completion | NOT FOUND (p.237) |
| Commission payees (111.22), placement investors, FY25 promoter sale price | NOT FOUND |
| FY26 Q4 share of sales | NOT FOUND (FY25 was 51%, p.92) |

Reading [INFERENCE]: the document meets the form and omits the join between buyer, product and cash. This is a disclosure gap, not evidence of related-party sales. No related-party sale or receivable appears in Annexure VIII (pp.250-251). LBF-1 cannot close from the notes.

### P3-3. Revenue timing chain (cross-note)
- Policy: revenue on delivery or commissioning, or POC where installation is essential (pp.229-230). Unearned revenue 166.50 appears first in FY26 (Note I.7, p.234). FY25 Q4 was 51% of annual sales, so about 3,316 of 6,502.69 (computed). FY25 receivables under 6 months were 1,669.30 (Note I.14, p.235), about half of that Q4 amount (computed, depends on the 51%).
- [INFERENCE] Year-end receivable and debtor-day figures depend on late-quarter delivery. FY26 Q4 share is the observation that would settle it. MD&A says "business is not seasonal" (p.270), which conflicts with the 51%.

### P3-4. Tie-outs and pattern checks with no new issue
- Balance sheet total 6,053.09 foots (p.226); equity 4,140.67 ties to I.1/I.2; cash flow foots FY25/FY26 (p.228). Restatement: FY24 only, gratuity (Annexure VII p.249); FY25 and FY26 carry no adjustments. 🟢
- FY24 Annexure IX current tax 102.42 vs 97.90 in Annexure II and II.9; interest u/s 234 blank in Annexure IX vs RF5 paid amounts. Already in FLAG-CONTROLS.
- Events after balance sheet: Section VI item G, p.274: none material except as in MD&A. Going concern: NONE. The only "going concern" text in the document is the exchange eligibility table (line 19743 of the text twin), which is not a company statement.
- Auditor change: FY24 audited by Ghewarchand Rathan Kumar (05-Sep-2024), FY25/FY26 by A B C D & Co LLP (p.222, p.225). Reason NOT FOUND. Combined with thin pre-IPO controls (RF5) this is a stage 8 question.

PASS 3: material new findings are limited to P3-2 and P3-3 (cross-note patterns); no new red flag.

---
## CONSOLIDATED NOTES ANALYSIS

### First verification priorities (LBF-1 to LBF-4, as handed by the task)
| LBF | Result from notes |
|---|---|
| LBF-1 non-government customers (Rs 4,733.92 lakh FY26) | OPEN. Unnamed. 82.7% of FY26 growth (3,362.74 of 4,068.59, computed). No related-party sale or receivable disclosed; completeness untestable. Product lines not crossed to buyer type. |
| LBF-2 debtor days and ageing | Company 83/89/74 is average-balance. Year-end 144/111/79 (computed). Improved on both bases. >6 months 11.85% of gross (16.97% FY25). 130.54 stuck at 2-3 years, 20.7% provided. Operating WC days ex-cash did not improve in FY26 (72.8 to 78.4, computed). |
| LBF-3 CFO vs PAT | 762.30 vs 1,350.77 = 56.4% (FY25 54.3%, FY24 negative). Pass 1 unpaid-tax claim withdrawn (advance tax is in other current assets). Tax-neutral about 65% FY26 is inference only. |
| LBF-4 related party and group exposure | RPT ex-loans 3.63% of revenue FY26 (5.41% FY25). Promoter loans repaid, nil at FY26. Group entities are not buyers per disclosure. Software from Gostocks 78.70 over two years; guarantors outside RPT list. |

### A. Top 15 findings
| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | CFO 762.30 = 56.4% of PAT 1,350.77; 3-yr 38.8% | Annex III p.228; RF5 | 🟡 | Conversion weak; driven by working capital, not tax |
| 2 | Non-government buyers 4,733.92 unnamed; two lines give 99.97% of growth | RF10 p.29; RF3 p.24 | 🟡 | LBF-1 open |
| 3 | 130.54 at 2-3 years; 20.7% provided; no ECL rule; roll-forward anomaly 26.27 | I.14 p.235 | 🟡 | Provisioning without a rule |
| 4 | Debtor days 74 is average-basis; year-end 79; WC days ex-cash up in FY26 | p.245; pp.226-228 | 🟡 | Days story narrower than it reads |
| 5 | RPT stack 384.19 ex-loans; RPT payables 90.34 to 2.65 | Annex VIII | 🟡 | No arm's-length evidence |
| 6 | Software capitalised share 0/59.6/82.6%; CWIP 137.17 | II.8; I.9 | 🟡 | Capitalisation honesty; related-party vendor |
| 7 | Gross margin 37.3/31.2/27.1%; lease cost 160.78 to 22.48 | KPI p.257; II.3 | 🟡 | Margin held by opex leverage |
| 8 | Unearned revenue 166.50 first in FY26; advances 22.18 vs claimed 30-50% | I.7 p.234; p.92 | 🟡 | Revenue timing and collection claim |
| 9 | Statutory defaults: TDS up to 91 days, GST, EPF, ESI; advance tax short | RF5 pp.25-27 | 🟡 | Controls |
| 10 | Promoters took about 89% of Rs 20 placement; 94,918 shares transferred FY25 | I.1; RF4 | 🟡 | Stage 8 cross-check |
| 11 | Promoter-family guarantees incl. non-RPT persons; BG 592.85 = 14.3% of net worth | I.5; Annex V xiii | 🟡 | Unpriced support; above 10% line |
| 12 | ROCE is spot-year, cash 31.8% of equity; two ROE measures | Annex V; VI | 🟡 | Do not feed as durable ROCE |
| 13 | MD&A and policy contradictions cluster | pp.231, 263-270 | 🟡 | Disclosure quality |
| 14 | Zero debt, promoter loans repaid, MSME interest nil, CSR met; intra-year interest 11.95 | p.250; p.255; II.6 | 🟢 | Point-in-time clean |
| 15 | Indian GAAP; auditor change; FY24 gratuity restatement; no going concern text | pp.222-223, 249, 274 | 🟡 | Thin pre-IPO infrastructure |

### B. Accounting quality score: 5 of 10
| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 5 | Two bases allowed; POC amount absent; unearned revenue new; Q4 51% |
| Expense capitalisation honesty | 5 | Software CWIP 137.17 unamortised; capitalised share 82.6% |
| Provisioning adequacy | 4 | No ECL rule; 20.7% vs 100% inconsistency; provision 31.94 on 2,320.02 gross |
| RPT fairness | 5 | Full listing, small share of revenue; no arm's-length evidence; guarantors outside list |
| Disclosure transparency | 4 | Thin on customers, buyer type, POC; MD&A contradictions |
| Consistency with prior years | 6 | Policies stable; FY24 gratuity restated once; auditor change |
| OVERALL | 5 | Unchanged from Pass 1 and 2 |

### C. Key risks from notes
| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Cash conversion stays near 55% while revenue grows 60%+ | High | CFO/PAT, WC share of incremental revenue (21.3%) | FY27 results; WC need FY27 4,442.00 vs 3,587.14 |
| Non-government buyer concentration or identity risk | High | Named customer disclosure, receivable split | First annual report |
| Stuck receivables (130.54 aged 2-3 years) | Medium | 2-3 year bucket, provision rule | FY27 ageing |
| Margin: gross margin falling, lease cost fall not explained | Medium | Gross margin, rental revenue vs lease cost | H1 FY27 |
| Q4 loading of sales and delivery-based recognition | Medium | Q4 share, unearned revenue | Each year-end |
| Control gaps (TDS, GST, EPF delays) | Low-Medium | Statutory defaults as a listed company | Next audit |
| Software CWIP impairment or amortisation start (about 35.6 a year) | Low | Commissioning | FY27 |

### D. Five questions for management
1. Name the top 10 FY26 customers split government/private, say which private buyers resell to government, and cross-tab product line and receivable bucket by buyer type.
2. What is the ageing basis and provisioning rule, and why is the 2-3 year bucket of 130.54 provided 20.7%?
3. What equipment carried FY26 rentals after machine lease cost fell to 22.48, and why did gross margin fall to 27.1%?
4. What is the software under development (137.17), who built it, when does it commission, and why did the capitalised share reach 82.6%?
5. Who bought the Rs 20 and Rs 569 placements, at what price did promoters transfer 94,918 shares in FY25, and what is behind unearned revenue 166.50 and the 30-50% advance claim?

### E. Notes-based red flags
None at red level. Earnings management indicators checked: capitalisation of software (watch), provisioning inconsistency (watch), margin by opex leverage (watch), revenue timing (watch). No restated FY25/FY26, no going concern language, no qualification. Flags raised: FLAG-CASH, FLAG-CUSTOMER-ID, FLAG-RPT, FLAG-RECEIVABLE-QUALITY, FLAG-CONTROLS, FLAG-MARGIN-QUALITY.

### F. One-line notes verdict
The notes reveal moderate accounting practices. Key concern: the buyers behind 82.7% of FY26 growth are unnamed, and profit converts to cash at 56%. Key strength: zero debt at FY26, promoter loans repaid, full related-party listing with no related-party sale or receivable. Overall accounting quality: 5/10.

```yaml
stage: B02-notes
company: "KWICK"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: complete
accounting_quality: 5
pass_2_empty: false
pass_3_empty: false
note: "Full block, including top_findings, flags, questions_for_mgmt, receivables_trend, restatements_found and going_concern_language, is in outputs/blocks/B02-notes.yaml"
```
