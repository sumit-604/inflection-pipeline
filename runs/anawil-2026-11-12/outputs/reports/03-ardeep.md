# Stage 3: Annual report deep dive, backward read (8 phases). ANAWIL (Anawil Wire and Engineering Ltd). Run 2026-11-12

Rating tags: [GREEN] clean, [YELLOW] watch, [RED] red flag. Kill switch is informational only. The pipeline continues regardless.

## 0. Basis, degradation, units, anchors

**No annual report exists.** The company listed on NSE SME on 2026-08-10 and has published no annual report (B00). This stage reads the Prospectus (business, MD&A, risk factors, objects, management, restated FY24 to FY26), the Addendum, the audited FY26 statements with FY25 and FY24 bound in (OCR), the H1 FY27 results, the CRISIL rationale, both investor presentations, the press release and the exchange filings. In every phase I name what an annual report would have supplied and is absent. Common absences: Board's Report, MD&A as filed for the year, Corporate Governance Report, Section 197(12) median-pay table, board and committee attendance, AGM notice, related-party Form AOC-2, internal-audit report, secretarial audit, cost-audit report.

**Units.** Prospectus, results, FY26 and FY25 audited statements: INR lakh. FY24 audited statements: INR thousand (B02). Presentations, press release, rating: INR Cr. I carry the unit in each anchor. "Rs X Cr (derived)" means lakh divided by 100.

**Anchors.** Page numbers are the `[page N]` markers in the .txt files. For the Prospectus the printed folio is N minus 3.
- Pros p.N = Prospectus_2026-08-06 | Add p.N = Addendum_to_RHP | AFS p.N = Audited_Financial_Statements_FY2025-26 (OCR)
- H1 p.N = H1FY27 results outcome | Pres p.N = Investor_Presentation_H1FY27 | List p.N = Investor_Presentation_Listing
- PR p.N = press release 2026-11-06 | CRISIL p.N = rating rationale | MA p.N = CARE monitoring report in 2026-11-07_NSE_Intimation
- Ann(date) p.N = exchange filing of that date | SHP30Sep = shareholding XBRL 2026-09-30 (no page markers)
- "derived" = my arithmetic on anchored numbers. "[INFERENCE]" = a reading the documents do not state.

**Accounting framework.** Accounting Standards (AS), not Ind AS, standalone only, no segment reporting (H1 p.5 notes 3 and 4). No subsidiary, associate or JV (Pros p.150; AFS p.9).

### 0.1 B00 load-bearing facts, checked first

| # | B00 fact | Result against filed documents |
|---|---|---|
| 1 | FY27 guidance Rs 450 to 500 Cr revenue, Rs 55 to 60 Cr PAT; H1 delivered Rs 153.97 Cr and Rs 14.39 Cr | VERIFIED. Guidance PR p.2, Pres p.7. H1 revenue 15,396.72 lakh and PAT 1,438.69 lakh (H1 p.4). H1 is 30.8% to 34.2% of revenue guidance and 24.0% to 26.2% of PAT guidance (derived). Order book Rs 395.58 Cr, execution "targeted by Q1FY28" (PR p.2; Pres p.21). Test of H2 in Phase 4C. |
| 2 | EBITDA margin 42.7% (FY26) to 23.4% (H1 FY27); Model 3 64.3%; tower count 107 vs 108 | MARGINS VERIFIED: FY26 6,122.99 on 14,326.69 (AFS p.17, B02 method); H1 FY27 3,608.24 on 15,396.72 (H1 p.4, derived). Model 3 64.3% PR p.2. TOWER COUNT NOT RECONCILED: 107 in the tile and 108 in the text on the same page (Pres p.7), 107 in PR p.2. EBITDA per tower Rs 32.82 lakh implies 109.9 towers (3,608.24 / 32.82, derived). 3,608.24 / 107 = 33.72 lakh; / 108 = 33.41 lakh. Unit economics reconcile to revenue mix (Phase 3C). |
| 3 | FY26 CFO prints Rs 12.5 Cr and Rs 18 Cr; short-term loans and advances Rs 50.0 Cr; name who holds them | VERIFIED: 12.5 is audited 1,246.69 lakh (AFS p.15; Pres p.28). 18 is the restated 1,843.94 lakh (Pros p.29 RF19; Pres p.25 chart). The Rs 50.0 Cr is 5,001.52 lakh, of which 3,003.57 lakh is "Advance for capital goods" (AFS p.27 Note 18). HOLDER NOT FOUND: no vendor name, ageing, order value or security anywhere in the corpus. |
| 4 | Largest customer 29%; Customer A 36.6% of order book; Karnataka 93.9%; Rs 142.56 Cr IPO money used | VERIFIED: Customer 1 29.32% (Pros p.24); Customer A 144.6 / 395.6 = 36.6% (Pres p.21, derived); Karnataka 93.87% (Pros p.23); 142.56 of 142.69 used (H1 p.6; MA p.6). Use matches the Objects (115.00 debt, 3.64 GCP, 24.05 issue cost; Pros p.73). Related-party items in Phase 2 and 5. |

## PHASE 1: AUDITOR'S REPORT AND CARO

Absent for lack of an annual report: the Board's Report that the auditor says he read (AFS p.2), the FY25 CARO annexures (named at AFS p.42 but not bound; B02), and the secretarial audit.

### 1A Core opinion
| Item | Finding | Anchor |
|---|---|---|
| Opinion | Unmodified, "true and fair view" under AS. G.B. Laddha and Co LLP, Vapi (FRN 120352W/W100033), partner Giriraj B. Laddha M.No. 108558, dated 18/06/2026, UDIN 26108558UC0PIXX5642 | AFS p.1, p.6 |
| Going concern | No material uncertainty paragraph. Boilerplate only; CARO 3(xix) "no material uncertainty ... not an assurance as to future viability" | AFS p.3, p.10-11 |
| Template residue | Opinion text still reads "profit (or Loss)*" | AFS p.1 |
| Internal financial controls | Unmodified (clause (f) and Annexure B) | AFS p.5, p.13-14 |
| Audit trail | Software "has the feature of recording audit trail (edit log)" and operated throughout | AFS p.6 |
| Dividend | None | AFS p.6 |

### 1B Key Audit Matters
| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| None reported | "Reporting of KAM as per SA 701 not applicable ... unlisted company" (AFS p.2) | n/a | [YELLOW] |

Reading: true at 18 June 2026 because listing came on 2026-08-10. FY27 will carry KAMs. The areas I would expect an auditor to pick for this book are revenue cut-off (H2 carries 71% of revenue), the capital-goods advance of 3,003.57 lakh, inventory valued "as certified by management" (AFS p.26 Note 15 heading), and the Section 115BAB tax position. No auditor judgement on any of them is on file.

### 1C Emphasis of Matter and Other Matters
None in FY26, FY25 or FY24 (AFS p.1-6, B02 section 4). H1 FY27 limited review: unmodified; H2 FY26 is stated as a balancing figure between the audited year and the reviewed H1 (H1 p.3, p.5 note 9).

### 1D CARO 2020, clause by clause (FY26, AFS p.7-11)
| Clause | Remark | Flag |
|---|---|---|
| i(a)-(e) | Records kept; verification done; **title deeds "held in the name of the Company"** (p.7). Prospectus discloses the Kutch land (Survey 112, 114/1, 114/2) was bought from a seller who lost the original deeds (FIR 11 Oct 2021) (Pros p.31) | [YELLOW] cross-document |
| ii(a) | Inventory verified "except inventory lying with third parties", "substantially confirmed"; amount NOT FOUND (p.7) | [YELLOW] |
| ii(b) | Working capital limit above Rs 5 Cr, "applicable", refers reader to Additional Information 4; the text does not say returns agree (p.8). Books exceed bank returns by 248.74 (inventory) and 302.51 (receivables) in March 2026 (AFS p.35) | [YELLOW] |
| iii | No loans or advances to Section 189 parties (p.8) | [GREEN] FY26 |
| iv, v | Sections 185 and 186 not breached; no deposits | [GREEN] |
| vi | **Cost records and cost audit "applicable ... complied"** (p.8). FY24 CARO said not applicable (AFS p.83, B02). Cost auditor and report NOT FOUND | [YELLOW] |
| vii | Regular in undisputed dues; nothing disputed (p.8-9). Prospectus lists GST, EPFO and ESIC delays, including an EPFO payment 272 days late for May 2023 (Pros p.30) and the income tax demands in Annexure Z | [YELLOW] |
| viii | No unrecorded income | [GREEN] |
| ix | No default, not wilful defaulter, loans used for purpose, no short-term funds for long-term use (p.9). Cash credit 1,193.82 outstanding against a 1,200 limit at 31 May 2026 (Pros p.74) beside capital advances held as current assets | [YELLOW] |
| x | No IPO in the year; private placement complied with Sections 42 and 62 (p.9-10). Ties to 13,80,000 shares at Rs 101 (Pros p.62-63; 1,393.80 lakh less 113.05 expenses = 1,280.75, AFS p.15) | [GREEN] |
| xi | No fraud, no Section 143(12) report, no whistle-blower complaint (p.10) | [GREEN] |
| xiii | RPTs comply with Sections 177 and 188 (p.10). See Phase 2B on Darpan | [YELLOW] |
| xiv | Internal audit "not applicable" under Section 138 limits (p.10) | [YELLOW] |
| xvii | No cash loss in FY26 or FY25 (p.10) | [GREEN] |
| xviii | No auditor resignation | [GREEN] |
| xix | No material uncertainty (p.10-11) | [GREEN] |
| xx | CSR applicable; required 17.81, spent 18.00 (AFS p.35); no unspent amount (p.11) | [GREEN] |

Adverse remarks with amounts: none in the CARO text. The yellow flags come from comparing CARO sentences with other filed pages.

### 1E Auditor continuity and fees
| Item | Finding | Anchor |
|---|---|---|
| Firm and tenure | G.B. Laddha and Co LLP signed FY24 (report 05 Sep 2024), FY25 (13 May 2025) and FY26 (18 Jun 2026). Earlier years and appointment resolution NOT FOUND (no AGM notice or AR) | Pros p.168; AFS p.6 |
| Partners | Seema Bohra (FY24), Giriraj B. Laddha (FY25, FY26) (B02; AFS p.81, p.43, p.11). Partner change noted, no finding | B02 |
| Fees | Statutory audit 4.80 / 5.00 / 1.50 lakh (FY26 / FY25 / FY24); tax audit 1.20 / 0.50 / 0.50; total "payment to auditors" 6.00 and 5.50 for FY26 and FY25 (AFS p.30; Pros p.209). 6.00 is 0.042% of revenue (derived) | AFS p.30 |
| Non-audit fees | None shown. Certification fees NOT FOUND. Same firm issued the CA certificate to the monitoring agency on 04 Nov 2026 (MA p.5) and the H1 FY27 limited review | MA p.5 |
| Audit to non-audit ratio | Cannot be computed; non-audit fee line NOT FOUND | n/a |
| Second CA firm | S.R. Goyal and Co (Jaipur, FRN 001537C) did the restatement and certified KPIs, as the statutory auditor was committed elsewhere (Pros p.25 RF8) | Pros p.25 |
| Drafting defects in the restated report | Calls G.B. Laddha the "Previous Auditor" and cites an "examination report dated September 10, 2025" for statements that include FY26 (Pros p.168). Prospectus says the Board approved the audited FY26 statements on 13 June 2026 (Pros p.237), while the audited statements and directors' signatures are dated 18 June 2026 (AFS p.15-17) | [YELLOW] |

Cannot test: whether a first-year-of-listing audit committee reviewed the auditor's independence. No AR.

### 1F Standalone vs consolidated
No subsidiaries, so no other-auditor reliance and no consolidated report (AFS p.9; Pros p.150). The only second auditor is the peer reviewer for the restatement.

### Phase 1 summary
| Test | Result |
|---|---|
| Opinion type | Unmodified, three years |
| Adverse CARO remark | None stated |
| KAM | Not reported (unlisted) |
| Cross-document conflicts | Title deed statement vs lost Kutch deeds; "regular" statutory dues vs listed delays; Board approval date 13 vs 18 June; restated report dates |

**Phase 1 verdict: [YELLOW] Watch.** Clean opinions from a small Vapi firm with a 6.00 lakh fee on Rs 143 Cr revenue and no KAMs, which leaves the judgement-heavy areas untested in the public record.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because opinions are unmodified and no fraud, default or going-concern language appears.

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Absent for lack of an annual report: the full note set as filed with an AGM, Form AOC-2, the contingent-liability and commitments notes (the audited FY26 statements carry none; AFS p.18-37), and actuarial assumptions.

### Verification of the triple-pass Top 15 (B02, section A)
| Rank | Finding | Result | Basis |
|---|---|---|---|
| 1 | 115BAB demand 367.25 lakh, 17 Jul 2026, AY 2025-26, no provision | ✓ | Pros p.240-241: demand order 17 Jul 2026 for AY 2025-26, rectification filed 22 Jul 2026, "pending for rectification order". AFS p.5 sentence "does not have any pending litigations" reproduced. Exposure 515.50: my recompute 8.008% x (534.36 + 1,487.76 + 4,450.47) = 518.3 lakh, same order; base or rate differs by 0.5%. See discrepancy 3 |
| 2 | Capital-goods advance 3,003.57 lakh | ✓ | AFS p.27 Note 18; p.16 total 29,159.89; current ratio 14,476.80 / 10,326.90 = 1.40; ex-advance 11,473.23 / 10,326.90 = 1.11 |
| 3 | CFO 1,246.69 vs restated 1,843.94; capex-neutral 2,814.94 to 3,114.75 | ✓ | AFS p.15; Pros p.29; 1,246.69 + 2,401.13 - 832.88 = 2,814.94. The 832.88 uses Note 9 capital creditors, not re-read here (carried) |
| 4 | Darpan 97.60 commission, 87.27 balance | ✓ partial | Both in the RPT table (Pros p.50-51). Notes 25 and 29 not re-read (carried) |
| 5 | H2 FY26 93.3% of PBT; bank returns | ✓ | H1 p.4: 4,152.45 / 4,450.25 = 93.3%; AFS p.35: 248.74 and 302.51 |
| 6 | Raw material 3,930.40 (14.6x) | ✓ | AFS p.26: 3,930.40 vs 269.92 = 14.56x; H1 p.8 release 1,838.24; CARO ii(a) p.7 |
| 7 | Two creditors 85.7%; MSME four versions | ✓ partial | AFS p.16: MSE 821.94 + others 3,844.38; FY25 MSE 62.48. Creditor concentration at Pros p.243 not re-read (carried) |
| 8 | No contingent, commitments, post-balance-sheet notes | ✓ | Search of AFS text finds "contingent" only in the policy (AFS p.19); "commitment" nowhere |
| 9 | Restatement moved profit | ✓ | AFS p.17 PAT 3,595.25 / 1,398.41; Pros p.231 restated 3,662.83 / 1,230.58 |
| 10 | Debt 12,824.76; post-issue 3,360.79 | ✓ with ✗ on one sub-number | Pros p.238; H1 p.7: 2,701.83 + 658.96 = 3,360.79. See discrepancy 1 |
| 11 | H1 depreciation 113.8% of FY26 | ✓ | 1,286.53 / 1,130.14 = 113.8%; CWIP 3,069.27 (H1 p.4, p.7) |
| 12 | Receivables 3,894.54, 98.6% not due, top five 78.75% | ✓ | AFS p.27: 3,841.81 / 3,894.54 = 98.65%; Pros p.24 |
| 13 | Note 38 printed errors | ✓ | AFS p.37: D/E 1.10, inventory turnover 117.56, DSCR 3.94 |
| 14 | Monitoring agency "Deviation: Yes", 0.89 Cr comingling, 2,024.30 vs 2,387 | ✓ | MA p.3, p.6-8; 14,268.96 - 12,244.66 = 2,024.30 (H1 p.8); 23.87 Cr = 2,387 lakh |
| 15 | Control history | ✓ | AFS p.8, p.10; Pros p.26-27 (ROC delays); FY24 audit-trail text carried |

**Discrepancies found**
1. Unsecured recallable loans: Pros p.34 RF37 says 516.76 lakh (4.03% of debt). B02 reports directors' loans 433.89 (AFS p.23). Difference 82.87. With the 87.27 Darpan balance the sum is 521.16, which also does not match. Unresolved.
2. B02 pass 3 says FY26 capex was funded by debt of 7,313.88 lakh. Cash flow shows long-term 5,973.82 plus short-term 1,367.30 = 7,341.12 gross (AFS p.15). Difference 27.24. Free cash flow of (8,053.92) is unaffected.
3. The 367.25 lakh demand is 2.8x the pure rate gap on AY 2025-26: 8.008% x audited FY25 PBT 1,631.76 = 130.7 lakh (119.1 on restated 1,487.76). The rest is unexplained in the corpus (interest, or other disallowances). NOT FOUND.

### 2A Accounting policy aggressiveness
| Area | Policy | Reading |
|---|---|---|
| Revenue | On delivery; net of GST, branch transfer and TCS (AFS p.19, p.28 Note 20) | TCS deducted from revenue (15.58) is presentation, small. "Others" revenue 789.93 lakh (5.5%) is scrap per Pros p.112; scrap stock at year end only 8.45 (AFS p.26) |
| Depreciation | WDV, Schedule II lives (AFS p.18) | Conventional. Restatement recomputed FY25 (+144.49) and FY24 (-142.50) (Pros p.187, B02). FY27 step-up to 1,286.53 in six months |
| Inventory | "As valued, certified and qualified by the management" (AFS p.26 heading); lower of cost and NRV (AFS p.19) | Management-certified balance of 5,068.78 with 3,930.40 raw material |
| Capitalisation incl. borrowing costs | AS 16 allowed. **MD&A states "a significant portion of the borrowing costs" for the Kutch plant "was capitalized"** (Pros p.233-234; Add p.17). Amount NOT FOUND in any note, though AS 16 calls for it | [YELLOW]: closes B02's "was it capitalised" question, not the "how much" question |
| ECL | AS framework; no matrix. Bad debts written off when irrecoverable (AFS p.19). Receivables 3,894.54 with no provision | Ageing clean (over 6 months 1.04%) |
| Leave encashment | Expensed 6.03 on cash basis (policy, B02) | Small |
| Leases | Not Ind AS 116. Registered office rented from Darpan for 36 months from 02 Feb 2024 (Pros p.30) | Expires about 01 Feb 2027 (derived) |
| Policy change | None stated (Pros p.168) | Restatement still moved FY25 PAT by -12.0% |

### 2B Related-party map (restated, Rs lakh, Pros p.50-51)
| Item | FY26 | FY25 | FY24 | Note |
|---|---|---|---|---|
| Director and KMP pay | 60.84 | n/a | n/a | 0.42% of revenue, 1.66% of restated PAT (derived) |
| Darpan interest on loan | 32.22 | 27.23 | nil | |
| Darpan guarantee commission | 97.60 | nil | nil | Booking line NOT FOUND (B02) |
| Darpan construction of assets | 127.67 | nil | nil | Contractor and guarantor and landlord and lender |
| Darpan rent paid | 0.65 | 0.65 | nil | |
| Darpan loans received / repaid | 108.50 / 576.17 | 1,018.67 / 551.00 | 1,389.52 / 1,574.57 | |
| Promoter loans taken / repaid (Nimish) | 1,442.24 / 1,039.58 | 81.50 / 380.70 | 1,208.10 / 891.81 | Balance 414.75 at Mar 2026 |
| Darpan trade payable | (87.27) | (467.67) | (132.91) | Labelled loan in AFS Note 29 (B02) |

Non-loan RPT expense in FY26: 60.84 + 32.22 + 127.67 + 97.60 + 0.65 = 319.0 lakh, 2.2% of revenue (derived). The guarantee fee to the group company (97.60) is 2.8x the pay of all four family directors combined (34.38, derived), and the five personal guarantors receive none (B02). Value-extraction signal: weak, not proven. The promoters sold 7.20 lakh shares at Rs 101 in September 2025 (Pros p.67) and 13.01 lakh in the IPO (Pros p.73). Post-IPO the CMD lent Rs 21.68 Cr at 6% (Pres p.8); date, tenor and security NOT FOUND.

### 2C Contingent liabilities
| Year | Amount | % of net worth | % of PAT | Flag |
|---|---|---|---|---|
| FY24 | 226.93 | 8.2% of 2,776.75 | 51.7% of 439.18 | >25% of PAT |
| FY25 | 226.93 | 5.7% of 4,007.59 | 18.4% of 1,230.58 | none |
| FY26 | nil restated (Pros p.28 RF17) | | | but 367.25 demand outside the table: 4.1% of net worth 8,951.16, 10.0% of PAT 3,662.83 |

All derived from Pros p.28 and Pros p.231. The audited statements carry no contingent note (AFS p.18-37). Pros p.241 says the 226.93 history ended as "disposed" with no outcome stated.

### 2D Receivables
| Metric | FY24 | FY25 | FY26 | Sep-26 |
|---|---|---|---|---|
| Trade receivables (lakh) | 382.94 | 2,516.61 | 3,894.54 | 3,985.78 |
| Days of revenue | 26 | 117 | 99 | 47 (H1, 183 days) |
| Over 6 months share | 0.74% | 1.48% | 1.04% | n/a |
| Not due share | n/a | 78.6% | 98.65% | n/a |

Sources: Pros p.29, AFS p.27, H1 p.7; CRISIL p.2 gives 99 days. Top five customers 78.75% of FY26 revenue (Pros p.24). Retention money outside receivables: 297.44 non-current plus 338.54 current = 635.98 (AFS p.26-27). Customer-wise ageing NOT FOUND.

### 2E Inventory
Raw material 3,930.40 (14.56x), WIP 1,039.64, finished goods 81.47, stores 90.29, scrap 8.45 (AFS p.26). Inventory 4.2x in a year against revenue 1.8x. CRISIL counts 226 inventory days (CRISIL p.2). No write-downs. H1 FY27 inventory fell to 3,230.54 (H1 p.7). The raw material build is 75.6% from January to March (B02 P6).

### 2F Borrowings
| Item | Finding | Anchor |
|---|---|---|
| Total | 12,824.76 at 31 Mar 2026: 11,640.44 long-term incl. current maturities, 1,184.32 cash credit | Pros p.238 |
| Lender | Bank of Baroda for all term loans and the cash credit; Cosmos Co-operative Bank 0.80 Cr (CRISIL p.4) | Pros p.74-76 |
| Term loans | 72 ballooning instalments after moratorium, 9.25% (BRLLR 8.15% + 0.25% + 0.85%); Kutch shed 2,169 and Kutch plant 4,850 (modified sanction 27 Oct 2025, drawn 20 and 21 Nov 2025); Koppal expansion 1,385 (first drawn May 2025) | Pros p.75 |
| Maturity wall | Five-year schedule and balloon amounts NOT FOUND. Current maturities 1,796.07 (B02). The wall is largely retired: 113 Cr of term and vehicle loans plus 2 Cr of working capital were repaid from the IPO (MA p.6) | MA p.6 |
| Covenants | Prior-approval covenants named; financial covenants NOT FOUND | Pros p.27 RF15 |
| Security | Hypothecation of movables, factory land and personal guarantees of promoters and Darpan | Pros p.32 RF27 |
| Rating | CRISIL BBB/Stable and A3+, upgraded 19 Aug 2026, limits Rs 135 Cr | CRISIL p.1 |
| Post-issue | 3,360.79 at 30 Sep 2026 = 0.148x equity 22,634.51 (derived). Excluding the CMD loan of 2,168 the figure is 1,192.79 or 0.053x (derived) | H1 p.7; Pres p.8 |
| ICDs given | None (AFS p.36 item 11) | |

### 2G Deferred tax
Net asset 14.46 (FY25 18.27) with no reconciliation note (AFS p.26 Note 13). Current tax 767.78 on PBT 4,450.25 is 17.25%, in line with the 17.16% concessional rate. FY25 12.7% (207.71 / 1,631.76). The audited charge also carries 83.40 earlier-year tax (AFS p.17).

### 2H Exceptional items, ESOP, post-balance-sheet
No exceptional items in three years (Pros p.231). No goodwill. No ESOP (Pros p.63). Post balance sheet: the audited statements carry no note. The Prospectus lists only board and offer approvals (Pros p.236-237), and omits the 17 Jul 2026 demand from that list (it appears in litigation instead). "Write off" of 9.81 lakh in FY26 other expenses is unexplained (AFS p.30). "Rent income" 35.00 lakh is 97% of other income, counterparty NOT FOUND (AFS p.28).

### Phase 2 reconciliation with B02
B02 scored accounting quality 5/10. I agree at 5/10. The audited and restated figures reconcile, opinions are unmodified, ageing is clean and nothing is in default. Against that: no contingent or commitments note, a 367.25 lakh tax demand and a 97.60 lakh fee that sit outside the audited notes, capitalised interest with no amount, and four versions of the Darpan record.

**Phase 2 verdict: [YELLOW] Watch**, with [RED] items on the tax regime (Pros p.240) and the Darpan trail (Pros p.50). **Cross-reference to Phase 1:** with no KAMs reported, the same four areas B02 flags are the ones the auditor did not discuss.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the flags are disclosure and classification gaps, not misstatement proven.

## PHASE 3: FINANCIAL STATEMENTS

Absent for lack of an annual report: Board's commentary on cash flow, segment data, ratio explanations other than Note 38.

### 3A Cash flow (read first). Rs lakh
| Item | FY24 restated | FY25 audited / restated | FY26 audited / restated | H1 FY27 |
|---|---|---|---|---|
| PAT | 439.18 | 1,398.41 / 1,230.58 | 3,595.25 / 3,662.83 | 1,438.69 |
| CFO | 889.33 | 978.15 / 966.31 | 1,246.69 / 1,843.94 | 2,828.40 |
| CFO / PAT | 202% | 70% / 79% | 35% / 50% | 197% |
| CFO / EBITDA | 40% | 33% (978.15 / 2,997.57) | 20% / 30% | 78% |
| Capex | 679.20 | 714.99 | 9,300.61 (AFS) / 9,305.37 (Pros) | 5,339.49 |
| Capex / depreciation | 0.60x | 0.83x | 8.23x | 4.15x |
| FCF | 210.13 | 263.16 (audited) | (8,053.92) | (2,511.09) |
| Financing inflow | (197.29) | (258.11) / (260.47) | 8,201.00 | 2,370.93 |
| Closing cash | n/a | 12.59 | 159.72 (incl. 150.00 FD) | 19.61 |

Anchors: AFS p.15, p.17, p.47; Pros p.29 RF19; H1 p.4, p.8. FY24 EBITDA 2,222.28 (Pros p.229).

Quality checks.
- **Both capex items sit inside CFO.** The loans-and-advances outflow (3,472.82) equals the Note 18 movement; the capital-advance rise is 2,401.13 (3,003.57 - 602.44, AFS p.27). The capital-creditor rise (+832.88) sits in other liabilities. Capex-neutral CFO is 2,814.94 to 3,114.75 lakh, 78% to 85% of PAT (B02, recomputed).
- **Working capital absorbed 5,241.70** in inventory and receivables, part offset by payables +3,793.27 (AFS p.15).
- **Interest.** Only 420.86 of 578.58 finance cost is added back; 157.72 stays in operating (AFS p.15, p.29).
- **One-time inflators:** none. **Payables stretch:** payables 4,666.32 equal 119 days of revenue (derived); then fell by 2,090.24 in H1 FY27 (H1 p.8).
- **Cumulative view.** FY25 to H1 FY27: CFO 5,053.24 vs PAT 6,432.35 = 78.6%; capex 15,355.09; FCF (10,301.85) (derived, audited basis). Funded by private placement 1,280.75, IPO net 12,244.66 and debt.
- **Trend:** CFO/PAT ran 202% (FY24) to 70% (FY25) to 35% (FY26), then 197% in H1 FY27 as the March stock unwound. The pattern is timing, not loss of cash, but it confirms the FLAG-CASH.

### 3B Balance sheet (Rs lakh, AFS p.16; Sep-26 H1 p.7)
| Line | Mar-25 | Mar-26 | Change | Sep-26 |
|---|---|---|---|---|
| Net worth | 4,075.16 | 8,951.16 | +119.6% | 22,634.51 |
| Long-term borrowings | 3,870.55 | 9,844.37 | 2.5x | 2,701.83 |
| Short-term borrowings | 1,613.10 | 2,980.40 | 1.8x | 658.96 |
| Trade payables | 873.06 | 4,666.32 | 5.3x | 2,576.09 |
| Other current liabilities | 866.25 | 2,120.93 | 2.4x | 2,697.25 |
| PPE + intangibles | 5,912.26 | 13,622.18 | 2.3x | 15,190.65 |
| CWIP | 124.46 | 584.80 | 4.7x | 3,069.27 |
| Inventories | 1,205.01 | 5,068.78 | 4.2x | 3,230.54 |
| Trade receivables | 2,516.61 | 3,894.54 | +54.8% | 3,985.78 |
| Short-term loans and advances | 1,528.70 | 5,001.52 | 3.3x | 5,431.40 |
| Total assets | 11,530.76 | 29,159.89 | 2.5x | 31,735.31 |

Net worth gain FY26 4,876.00 = PAT 3,595.25 + share issue 1,280.75 (derived). The H1 results show March total assets of 29,145.43, 14.46 lower because the deferred tax asset is shown as a liability there (H1 p.7).

| Ratio | FY25 | FY26 | Sep-26 | Basis |
|---|---|---|---|---|
| Debt / equity | 1.35 | 1.43 | 0.15 | Note 38 prints 1.10 (long-term only; AFS p.37) |
| Net debt / EBITDA | n/a | 2.07x | 0.46x on H1 annualised (flag: H1 is the soft half) | 12,665.05 / 6,122.99 |
| Current ratio | 1.53 | 1.40 (1.11 ex capital advances) | 2.02 | |
| Quick ratio | 1.19 | 0.91 | 1.52 | |
| EBITDA / finance cost | 5.11 | 10.58 | 6.83 | CRISIL 5.16 and 10.24 (CRISIL p.2) |
| EBIT / finance cost | 3.78 | 8.69 | 4.44 | |
| ROCE (EBIT / equity plus debt) | n/a | 23.1% | n/a | Pros p.229 prints 23.05% |
| ROE on average equity | 41.4% | 55.2% | n/a | AFS p.37 |
| Goodwill % net worth | 0 | 0 | 0 | |

**DuPont FY26 (audited, average balances):** margin 25.1% x asset turnover 0.70 x equity multiplier 3.12 = 55.2% ROE. Margin and leverage both carry it. After the IPO the multiplier is about 1.40 (Sep-26 assets 31,735.31 / equity 22,634.51), so ROE normalises to a margin-and-turnover story. The operational contribution is high in FY26 and cannot be read as run-rate (Phase 3C).

### 3C P&L line walk (audited, Rs lakh, AFS p.17)
| Line | FY26 | FY25 | YoY | % of revenue FY26 |
|---|---|---|---|---|
| Revenue | 14,326.69 | 7,858.86 | +82.3% | 100 |
| Other income | 35.98 | 80.98 | -55.6% | 0.25 |
| Materials net of inventory change | 4,168.76 | 2,014.16 | +107.0% | 29.1 |
| Employee | 411.20 | 252.56 | +62.8% | 2.9 |
| Other expenses | 3,623.75 | 2,594.12 | +39.7% | 25.3 |
| EBITDA (PBT + dep + finance - other income) | 6,122.99 | 2,998.02 | +104.2% | 42.7 |
| Depreciation | 1,130.14 | 860.64 | +31.3% | 7.9 |
| Finance cost | 578.58 | 586.60 | -1.4% | 4.0 |
| PBT | 4,450.25 | 1,631.76 | +172.7% | 31.1 |
| Tax incl. earlier-year | 854.99 | 233.35 | | 19.2% effective (14.3% FY25) |
| PAT | 3,595.25 | 1,398.41 | +157.1% | 25.1 |

- **Other income** is 0.8% of FY26 PBT and 5.0% of FY25 PBT. Under the 20% flag. FY25 had 68.38 of "rebate and discount" (AFS p.28).
- **Exceptional items:** none, three years (Pros p.231). **Tax rate:** current-tax rate 17.25% FY26, consistent with 115BAB. The 83.40 earlier-year charge is in audited PAT only; restated carries 11.69.
- **EPS** basic equals diluted at 18.78 (FY25 14.49) on 191.48 lakh weighted shares (AFS p.37).
- **H1 FY27 (H1 p.4):** revenue 15,396.72, materials 9,484.20 (61.6%), depreciation 1,286.53, finance cost 528.16, PBT 1,815.41, PAT 1,438.69, EBITDA 3,608.24 (23.4%).

**Half-year test of the margin base (new, derived; B02 P7 extended).** Towers by half: H1 FY26 62 (Pres p.18); H2 FY26 = 210 - 62 = 148. H2 FY26 is a balancing figure between the audited year and the reviewed H1 (H1 p.3, p.5).

| Half | Revenue | Towers | Revenue per tower (lakh) | EBITDA per tower (lakh) | Band from unit economics |
|---|---|---|---|---|---|
| H1 FY26 | 4,137.16 | 62 | 66.7 | 16.4 | Model 1 and 2 band 1,695 to 2,005 lakh total; actual 1,014.13, 40% below the floor |
| H2 FY26 | 10,189.54 | 148 | 68.8 | 34.5 | Top of band 4,714 lakh total; actual 5,108.87, 8% above the ceiling |
| FY26 | 14,326.69 | 210 | 68.2 | 29.2 | Mid-case 6,184; actual 6,122.99, within 1% |
| H1 FY27 | 15,396.72 | 107 | 143.9 | 33.7 | Mix-implied range 30.0 to 42.8 Cr; actual 36.08 Cr |

Band method: Model 1 revenue Rs 50 to 60 lakh and EBITDA Rs 25 to 30 lakh per tower, Model 2 Rs 1.0 to 1.1 Cr and Rs 35 to 40 lakh, Model 3 Rs 3.0 to 3.5 Cr and Rs 40 to 50 lakh (Pres p.15; List p.16). FY26 carried only four Model 3 towers (Pros p.232); the half is not disclosed, so I place all four in H2. Solving the towers per model from revenue per tower (Model 1 at 55 lakh, Model 2 at 105 lakh, Model 3 at 325 lakh) gives about 19 Model 2 towers in H2 FY26 and 14 in H1 FY26 (derived). For H1 FY27 the revenue split of 64.3%, 21.2% and 10.8% (PR p.2) implies about 28 to 33 Model 3, 54 to 65 Model 1 and 15 to 17 Model 2 towers, which sums to the 107 reported (derived).

Reading. Revenue per tower barely moved between the two FY26 halves (66.7 to 68.8 lakh), so a mix shift cannot explain EBITDA per tower more than doubling (16.4 to 34.5). The full year lands on the company's own unit economics, but the half-year split does not. [INFERENCE] The FY26 half-year margin gap is a cost-recognition or timing effect, not mix. B02 offered mix (A) and timing (B); this test favours (B) for FY26. Caveats: towers produced are not towers delivered, and revenue is booked on delivery. Mix is the right explanation for FY27 H1 (64.3% Model 3, EBITDA inside the mix-implied band). The one observation that settles it: revenue and cost by model for each half-year, and the H1 FY26 cost detail. Both NOT FOUND. H2 FY26 EBITDA margin of 50.1% is also above the top of the company's own Model 1 band (44 to 50%, Pres p.15), which a blend that includes Model 2 and 3 towers cannot exceed.

### Phase 3 summary
| Test | Result |
|---|---|
| CFO/PAT | 35% to 85% in FY26 depending on classification; 197% in H1 FY27 |
| Capex vs depreciation | 8.2x FY26: growth capex after two years below depreciation |
| Leverage | 1.43x at Mar-26, 0.15x at Sep-26 |
| Earnings base | FY26 margin is not run-rate; half-year split is a plug |

**Phase 3 verdict: [YELLOW] Watch.** FLAG-CASH carries forward: conversion in FY26 was not clean, but H1 FY27 shows the stock and payables unwinding and the leverage reset is real. **Cross-reference to Phases 1 to 2:** the working-capital build and the capital advance are the items the auditor did not name as KAMs.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because cash flow is explainable and leverage has fallen.

## PHASE 4: RISK FACTORS AND MD&A

Absent for lack of an annual report: a year-end MD&A with forward discussion, outlook and risk section written by the Board. The Prospectus MD&A (Pros p.228-238) covers FY24 to FY26 only. Management's forward voice lives in the press release, the presentations and the 05 Oct 2026 investor-conference note.

### 4A Disclosed risks, real vs boilerplate (Pros p.22-38; 78 numbered risks)
| # | Risk | Page | Assessment |
|---|---|---|---|
| 1 | Limited history; promoters lack prior wind experience | 22 | Real. Towers began 2023 |
| 3 | Seasonality, with H2 at 70.5%, 80.2%, 71.1% of revenue | 23 | Real, quantified |
| 4 | Karnataka 93.87% | 23 | Real |
| 5 | Top five customers 78.75%, no long-term contracts | 23-24 | Real |
| 6 | Vendor uses the Koppal plant address for GST | 24 | Real, odd |
| 7 | Top 10 suppliers 90.11% of purchases; Gujarat, Karnataka, Maharashtra 97.76% | 24-25 | Real. Steel price pass-through not discussed |
| 8 | Restatement certified by a non-statutory auditor | 25 | Real |
| 9 | Under-utilisation; Kutch 8.04% of tonnage | 25 | Real |
| 10 | Order book 35,981.72 lakh from 6 customers can be cancelled | 25-26 | Real |
| 12 | Litigation: 4.00 civil and 367.25 tax | 26 | Real |
| 13 | ROC form errors and delays | 26-27 | Real |
| 14, 15, 23 | Debt, covenants, Bank of Baroda dependence | 27, 31 | Real |
| 17 | Contingent liabilities: 226.93 FY25, nil FY26 | 28 | Understates: omits the 367.25 demand |
| 18, 19 | Working capital, negative cash flows | 29 | Real, but uses restated CFO and says nothing on the capital advance |
| 20 | Tax, GST and EPFO delays | 29-30 | Real, detailed |
| 21 | Registered office rented from Darpan; unregistered documents; Kutch deeds lost | 30-31 | Real |
| 27 | Personal guarantees by promoters and Darpan | 32 | Real |
| 37 | Unsecured loans recallable: 516.76 | 34 | Real, but number differs (Phase 2) |
| 47 | "Proposed fund requirement for our working capital ... from the IPO" | 36 | **Template residue.** Objects are debt repayment and GCP (Pros p.73) |
| 31, 40, 55 to 78 | No listed peer, SME liquidity, dividend, market and macro | various | Boilerplate |

### 4B Missing risks (evidence and likely reason)
| Missing risk | Evidence | Likely reason |
|---|---|---|
| Loss of the Section 115BAB rate as a stand-alone risk with PAT effect | Demand 367.25 lakh (Pros p.240-241); 8.0 point rate gap; the 17 Jul 2026 demand came after the 20 Jun restatement but before the 6 Aug Prospectus | Late event; shown under litigation only |
| Margin dilution from the shift to Model 3 | Model 3 had 4 towers in FY26 (Pros p.232); EBITDA margin 23.4% in H1 FY27 (H1 p.4). The listing deck, four days after the Prospectus, already says margin is "a revenue mix effect" (List p.16) | Management framed it as a metric choice. A KPI of EBITDA margin 42.64% is described as an indicator of operating performance (Pros p.229) |
| Kutch approvals and ramp-up | "client approval and certification processes currently ongoing" (Ann 2026-10-05 p.3); "trial runs underway" (PR p.3); Gujarat revenue 3.23 Cr in H1 FY27 (Pres p.23) against 8.78 Cr for FY26, all from March (Pros p.23, Add p.17). Pros RF16 lists only a shop licence and a trademark as pending (Pros p.28) | Prospectus says operations "commenced" (Pros p.111) |
| 3,003.57 lakh to unnamed capital-goods vendors | AFS p.27 | The Prospectus labels it "Advance to Vendors" (B02) |
| GST credit accumulation. [INFERENCE] | Output on towers is billed at 5% (Order 2026-09-10 p.1: 140.68 incl. vs 133.98 excl. = 5.0%). The input rate for steel (18%, outside the corpus) is NOT FOUND IN DOCUMENT and must be verified. "Balance with revenue authority" rose from 827.37 to 1,878.59 (AFS p.27). GST deducted from FY26 sales was 16.2% of net revenue (AFS p.28) | Not discussed; becomes sharper as Model 3 rises |
| Customer concentration inside the order book | March 2026: Customer D 29.9%, A 20.2% (Pros p.114, derived). Oct 2026: A 36.6% (Pres p.21) | Customer letters are relabelled between documents, so continuity cannot be tested |
| Capex funding after the IPO | Objects fund only debt (Pros p.73); H1 FY27 capex 5,339.49 vs CFO 2,828.40 and cash 19.61; CMD loan Rs 21.68 Cr (Pres p.8) | Not in Prospectus because no capex object |
| Registered-office lease from Darpan lapses about 01 Feb 2027 | Pros p.30 | Minor |
| Order book valued inconsistently | The Rs 58.3 Cr order of 29 Oct 2026 is GST-inclusive (Ann 2026-10-29 p.1) but is counted at 58.3 in the order book (Pres p.21), while the 133.98 order is ex-GST. At 5% GST the ex-GST value is 55.55, so the book is overstated by about 2.78 Cr (0.7%, derived) | Presentation error |
| FY26 AGM and annual report | A FY26 AGM was due by 30 Sep 2026 (Companies Act Section 96, outside the corpus). No notice or annual report is in the corpus and none on the NSE API (B00). Whether it was held or extended: NOT FOUND | Needs a check |

### 4C MD&A deep dive
**Industry claims.** India wind installed 58.52 GW at 31 Aug 2026, record 6.05 GW added in FY26, 28 GW under implementation, 100 GW target by 2030, 156 GW by 2036 (Pres p.10). The Prospectus uses Dec 2024 data, 48,163 MW (Pros p.115). Stage 9 tests these externally. Domestic turbine manufacturing capacity of about 24 GW (Pres p.10) is the only ceiling named; no tower-market size is stated.

**Growth and margin explanations (Pros p.232-234).**
- FY26 revenue growth credited to Koppal Bay-4, pending orders carried forward, and a new third model of which "four towers" were supplied (Pros p.232). Bay-4 lifted Koppal capacity from 300 to 420 towers (Add p.17). Koppal output rose from 135 to 194 towers (Add p.17); Kutch made 16 towers and Rs 877.73 lakh.
- Margin gain credited to cost absorption and "a significant portion of the borrowing costs" capitalised under AS 16 (Pros p.233-234). The capitalised amount is not given.
- **Utilisation basis.** 48.17% for FY26 equals 210 towers / 436, and 436 = 420 + 16 (derived). So FY26 utilisation is measured on year-end Koppal capacity plus the one month of Kutch, even though Bay-4 came during the year. On the 300-tower base, Koppal ran at 64.7% (194 / 300, derived). Tonnage utilisation is lower: 41.74% (Pros p.25).
- Tonnes per tower: 61,357.70 / 194 = 316 t at Koppal and 4,822.20 / 16 = 301 t at Kutch (derived). The 29 Oct 2026 order is for 474 t towers (EN-182, 5 MW; Ann 2026-10-29 p.2). **Installed tonnage is 207,000 t (147,000 + 60,000, Pros p.25); at 474 t per tower it supports about 437 towers, not 612 (derived). The 612-tower capacity depends on tower weight.** That is a point for the capacity model in stage 10.
- No external blame or credit-taking beyond "increase in business operations". The MD&A says no known trends or uncertainties beyond risk factors (Pros p.236). A drafting break: the sentence at Pros p.232 ends "the significant increase in the Company's revenue during the year was primarily." and stops.

**Segment.** Single segment, B2B only (Pros p.112, p.236). Product split FY26: towers 13,518.76 (94.36%), boiler and paper parts 18.00, others 789.93 (scrap, Pros p.112).

**Guidance table with credibility check**

| Claim | Number | Timeframe | Check against history and arithmetic | Credibility |
|---|---|---|---|---|
| FY27 revenue | Rs 450 to 500 Cr (PR p.2) | FY27 | H1 was 153.97. H2 needs 296 to 346 Cr. History: H2 share 70.5%, 80.2%, 71.1% (Pros p.23), so guidance implies H2 at 66% to 69%, a smaller seasonal lift than any past year (H2/H1 of 1.9x to 2.2x vs 2.4x FY24, 4.1x FY25, 2.5x FY26; derived). Towers needed at H1 realisation (1.44 Cr per tower): 206 to 240 in H2, against 148 in H2 FY26 (+39% to +62%) and nameplate of 306 per half (derived) | MEDIUM. Seasonal arithmetic supports it; delivery of towers is the test |
| FY27 PAT | Rs 55 to 60 Cr | FY27 | H2 needs 40.6 to 45.6 Cr. If H2 EBITDA margin equals H1 (23.4%), depreciation 12.87, finance cost 5.28, tax 20.75% (H1 rates), PAT is 40.7 to 49.9 Cr in H2, so FY27 is 55.1 to 64.3 Cr (derived). Margin is not the stretch; revenue is. Order-book mix at slide-15 mid-points gives about 27.7% EBITDA, above H1 (derived) | MEDIUM |
| Order book execution | Rs 395.58 Cr, 320 towers, by end Q1 FY28 (PR p.2; Pres p.21) | to Jun 2027 | March book was due by 31 Mar 2027 (Pros p.114); partly replaced by new orders. Implied inflow Apr to Oct 2026 at least 395.58 + 153.97 - 359.82 = 189.73 Cr (derived). Largest order 38 towers, Rs 133.98 Cr, "Q4 FY27" (Order 2026-09-10 p.2); LOI had been Rs 120 Cr (List p.8) | MEDIUM |
| Kutch | 16 towers a month, 192 a year (Pres p.18); "nearing completion, trial runs underway" (PR p.3) | no date | Operations "commenced March 2026" (Pros p.111). Client approvals ongoing at 05 Oct 2026. Completion date NOT FOUND | LOW to MEDIUM |
| EBITDA per tower rises as mix shifts | 32.82 lakh in H1 FY27 vs 29.2 in FY26 | ongoing | Mix-implied range holds (3C). Tower base for 32.82 unreconciled | MEDIUM |
| In-house kits at Koppal | internals plant "started" (List p.9); "nearing completion" (PR p.3) | no date | Capital outlay NOT FOUND | MEDIUM |
| External: operating margin about 40% | CRISIL p.1 | medium term | Already off at first print: H1 FY27 23.4% | LOW (rating-agency assumption) |
| External: gearing below 0.05x at Mar 2027; cash accrual Rs 80 Cr a year | CRISIL p.1-2 | Mar 2027 | Sep-26 gearing 0.148x incl. CMD loan; H1 cash PAT 27.3 Cr (Pres p.9) | LOW to MEDIUM |
| Use of IPO money | 115.00 debt, 3.64 GCP, 24.05 issue cost (Pros p.73) | FY27 | Delivered in 53 days: 115.00, 3.69, 23.87 (H1 p.6). Credible on delivery | HIGH |

No earlier guidance exists, so historical forecast accuracy is NOT FOUND.

### 4D Tone and credibility ratings (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3 | Per-model unit economics, tower counts, order book by customer disclosed. Capital advance vendors, Kutch capex, capitalised interest, contingent notes absent |
| Consistency | 2 | Tower count 107 / 108 / 110; CFO 12.5 / 18; order book mixes GST-inclusive and exclusive; 24 Oct 2026 filing says no ongoing tax disputes (Ann 2026-10-24 p.3) while the 367.25 demand was pending as of 6 Aug (Pros p.241); CS resignation reason given three ways (Ann 2026-10-31 letter p.1, intimation p.1, Annexure I p.3) |
| Specificity | 4 | Dated orders, tower counts, ranges per tower |
| Accountability | 2 | No discussion of the FY25 restatement (-12.0% PAT), of H1 FY26 weakness, or of missed items. Framing moved from EBITDA margin (Pros p.229) to EBITDA per tower within four days (List p.16) |
| Capital allocation sense | 3 | Spending all IPO money on debt cut interest. Then the CMD funds capex at 6% while Rs 30 Cr sits in vendor advances |

### Phase 4 summary and contradictions with Phases 1 to 3
- The Prospectus MD&A says capitalised interest helped the margin; the audited notes give no capitalised amount (Phase 2A).
- MD&A explains margin by cost absorption; Phase 3 shows the half-year margin gap is not mix.
- Risk factor 17 shows nil contingent liability; the litigation section shows 367.25 (Pros p.28 vs p.240).

**Phase 4 verdict: [YELLOW] Watch.** **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the omissions are of disclosure, not of fact, and the numbers reconcile.

## PHASE 5: CORPORATE GOVERNANCE AND BOARD

Absent for lack of an annual report: meeting attendance, committee meeting counts, the Section 197(12) disclosures, the Corporate Governance Report (exempt as an SME, Ann 2026-10-24 p.2), and the Board's Report. Attendance is NOT FOUND for every director.

### 5A Board (Pros p.145-148; changes p.151)
| Director | Role | Age | Since | Notes |
|---|---|---|---|---|
| Nimish K. R. Vashi | Promoter, Chairman and MD | 55 | 01 Feb 2025 | Secondary Certificate; 20 years as director of Darpan, where he still sits. Held 45.5 lakh shares from Jan 2022 and bought 50 lakh from Darpan in Nov 2023 at Rs 19 (Pros p.66-67), yet joined the board only in Feb 2025 |
| Ayush N. Vashi | Promoter, WTD | 25 | Incorporation | B.Com 2023; handles compliance, legal, inventory. Sits on the Audit Committee |
| Bhavin N. Desai | Promoter, NED | 46 | Incorporation | Director of Darpan; signs the accounts |
| Bijal N. Vashi | Promoter, NED | 52 | 01 Feb 2025 | Director of Ayush Rebar Coating Pvt Ltd; became promoter 19 Jun 2025 |
| Digant H. Bhagat | Independent | 30 | 20 Jun 2025 | Consultancy, 5 years |
| Nirav J. Desai | Independent | 45 | 20 Jun 2025 | Construction and hospitality |

Flags. Independents are 2 of 6 (33%); the Listing Regulations board rules do not bind an SME (Ann 2026-10-24 p.2). No independent is over 10 years. No director holds more than 8 seats. Promoter-group cross-board seats: Nimish and Bhavin are on Darpan, the guarantor, lender, landlord and contractor. Two earlier independents (Tayal, Bhurat) were appointed 01 Apr 2025 and resigned 19 Jun 2025 with no reason given (Pros p.151). No director has listed-company experience (Pros p.36 RF50).

### 5B Committees (Pros p.152-154)
Audit: Nirav Desai (chair), Digant Bhagat, Ayush Vashi, formed 20 Jun 2025. A 25-year-old executive director sits on the committee that reviews executive actions. Majority independent, so compliant. NRC: Bhagat (chair), N. Desai, Bhavin Desai. Stakeholder and CSR committees exist (Pros p.155-156). Internal audit: none, "not applicable" (AFS p.10). Whistle-blower complaints: none (AFS p.10).

### 5C Compensation (Pros p.50, p.149)
| KMP | FY26 Rs lakh | Note |
|---|---|---|
| Nimish Vashi (CMD) | 16.94 | Limit 40.00 a year; "15 lakh excluding sitting fees" (Pros p.149) |
| Ayush Vashi (WTD) | 14.04 | Limit 40.00; 12 lakh excluding sitting fees |
| Bijal Vashi, Bhavin Desai | 1.70 each | NED fees |
| Digant Bhagat, Nirav Desai | 1.50 each | |
| CFO Chiragkumar Patel | 9.93 | In role from 28 Mar 2025 |
| CS Sakshi Vijay | 10.18 | From 01 May 2025; resigned 31 Oct 2026 |
| Senior management D. Maiti | 2.75 | From 01 Jun 2025 |
| Total | 60.84 | 1.66% of restated PAT (derived) |

Promoter-family payroll 34.38 lakh. CEO to median multiple: NOT FOUND. A rough proxy: employee cost ex-directors 373.70 / 95 full-time staff = 3.93 lakh each, so the CMD at 15 lakh is about 3.8x (derived; excludes 767 contract workers paid through labour charges). Sitting fees: 1.50 lakh for an independent at a cap of Rs 10,000 a meeting implies about 15 meetings in 9 months, count NOT FOUND (Pros p.149). No ESOP (Pros p.63).

### 5D Shareholding
| Date | Promoters | Other | Source |
|---|---|---|---|
| 25 Apr 2025 (post-bonus) | Nimish alone 1,81,44,924 of 1,83,35,000 = 98.96% (derived) | | Pros p.66-67 |
| Pre-IPO (6 Aug 2026) | 1,76,14,943 = 89.35% | | Pros p.67 |
| 30 Sep 2026 | 1,63,14,162 = 65.26%, all locked in, no pledge | AIF 25,02,000 = 10.01% (5,96,000 locked); NBFC 56,000; DII total 10.23%; FII 1.73% (Pres p.29) | SHP30Sep |

Promoter selling: 7,20,000 shares at Rs 101 in Sept 2025 to 20 buyers, Rs 7.27 Cr (Pros p.67-68), then 13,00,800 shares in the IPO OFS at Rs 270, Rs 35.12 Cr (Pros p.73). Total Rs 42.39 Cr (derived). The drop from 89.35% to 65.26% is 18.9 points of fresh-issue dilution plus 5.2 points of OFS (derived). Pledge: none (SHP30Sep; Pros p.67). Average promoter cost Rs 7.65 a share (Pros p.68). Promoter selling against a growth narrative: **flagged, decision stays human**. It is IPO-structure selling, not a pattern of ongoing sales. Full promoter verdict comes from B08.

### 5E Governance red-flag checklist
| Item | Finding |
|---|---|
| Whistle-blower complaints | None (AFS p.10) |
| SEBI or exchange actions | None disclosed (Pros p.240-242) |
| RPT committee | Audit Committee approves (Pros p.152) |
| Auditor fee ratio | Cannot compute |
| CSR | Compliant, 18.00 vs 17.81 (AFS p.35) |
| Section 143(12) | None |
| Material subsidiary | None |
| Filing discipline | ROC delays in 2021-22 to 2025-26 (Pros p.27); GST and EPFO delays (Pros p.30) |
| KMP churn | CS resigned 31 Oct 2026 after 18 months; reason stated three ways; replacement from 01 Nov 2026 (Ann 2026-10-31) |
| Disclosure integrity | "No ongoing tax litigations" on 24 Oct 2026 vs 367.25 demand (see 4D) |
| Criminal matter | MS STP Ltd case against Darpan since 2015, amount unascertainable (Pros p.241-242) |
| Name and CIN | Addendum cover prints CIN U72300UP2015PLC070649, different from the company's (B00) |

**Phase 5 verdict: [YELLOW] Watch.** Board is promoter-controlled, young and inexperienced for a listed company. Offsets: no pledge, full lock-in, no SEBI action, no default. FLAG-PROMOTER-PRELIM is set for selling, not pledge.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because no integrity breach is shown, but the 24 Oct tax statement should be put to management.

## PHASE 6: LETTER AND FRONT MATTER (substitutes)

No chairman's letter or annual report exists. Substitutes read last, with Phases 1 to 5 in mind: the CMD commentary (Pres p.6; PR p.3), Prospectus overview and strategy (Pros p.111-116, p.228-229), listing-day deck, and the 05 Oct 2026 investor-conference note.

### 6A Narrative vs reality
| Claim | Source | Test | Mark |
|---|---|---|---|
| H1 FY27 revenue surpassed all of FY26 | Pres p.7 | 153.97 vs 143.27 Cr (H1 p.4; AFS p.17) | ✅ |
| "Maintaining healthy EBITDA margins of 23.4%" | Pres p.7 | Margin fell from 42.7%; not maintained | ❌ as framed; number ✅ |
| Higher integrated supply gives higher EBITDA per tower | Pres p.6 | 32.82 vs 29.2 lakh; tower base unreconciled | ✅ with caveat |
| Kutch "commenced operations March 2026" | Pros p.111; Pres p.18 | Approvals and trial runs ongoing (Ann 2026-10-05 p.3; PR p.3); Gujarat revenue 3.23 Cr in six months | ❌ partial |
| IPO money "utilised for the purposes for which they were raised" | H1 p.5-6 | Matches objects; 0.89 Cr comingled in the CC account; MA ticks "Deviation: Yes" yet text shows only 0.13 Cr unutilised (MA p.3, p.6-8) | ✅ with caveat |
| No ongoing tax litigation (24 Oct 2026) | Ann p.3 | Demand 367.25 pending (Pros p.241) | ❌ |
| Debt-light by Mar 2027 (CRISIL: below 0.05x) | CRISIL p.1 | 0.148x at Sep-26 | ❌ today |

### 6B Strategic priorities
Four stated: ramp Kutch to 192 towers a year, lift value per tower through Model 2 and 3, execute the order book, build in-house internals (Pres p.11). Specific, with numbers. Capital allocated: term loans sanctioned in FY26 for Kutch and Koppal of 8,404 lakh (Pros p.75) and, after the IPO, CFO plus a Rs 21.68 Cr CMD loan. Execution evidence: 107 towers in H1 FY27 against 62; Kutch contribution small.

### 6C Metrics showcased vs missing
Showcased: revenue growth, EBITDA per tower, cash PAT, order book, ROE, ROCE. Missing: CFO to PAT (chart shows 18 Cr, table 12.5), working-capital days (CRISIL: 292 gross current asset days), revenue by model per half-year, Kutch utilisation, capex plan, capital-advance detail, tax-rate sensitivity, net debt.

### 6D Tone and priority drift
Prospectus (6 Aug): EBITDA margin 42.64% as "an indicator of operational profitability" (Pros p.229). Listing deck (10 Aug): "business health should be measured through EBITDA per tower rather than only EBITDA margin" (List p.16). The 05 Oct note and H1 deck repeat it. The reframe came before any margin fell in a reported period, which means management expected the mix to shift.

### 6E Quiet Abandonment Check
| # | Opening claim | Where it should show | Class | Materiality |
|---|---|---|---|---|
| 1 | "We commenced operations at our new manufacturing facility in Kutch, Gujarat, in March 2026 ... additional capacity of 16 windmill towers per month" (Pros p.111, p.115) | H1 FY27 operations: "approvals and production ramp-up underway", "trial runs underway", client approval ongoing (Pres p.18; PR p.3; Ann 2026-10-05 p.3); Gujarat 3.23 Cr in six months vs 8.78 Cr in March | (c) hedged retreat | Thesis-changing: Kutch is 192 of 612 towers (31%) |
| 2 | EBITDA margin as the performance KPI (Pros p.229) | Replaced by EBITDA per tower (List p.16; PR p.2) | (c) hedged retreat | Medium: changes how H1 FY27 reads |
| 3 | Tax demand of 367.25 lakh disclosed as pending, rectification awaited (Pros p.241) | 24 Oct 2026 governance filing Part E: "no ongoing tax litigations or disputes" (Ann 2026-10-24 p.3) | (a) implicit retraction | Medium: governance and disclosure |
| 4 | "Time and cost overrun: none" (Pros p.144) | Kutch "nearing completion" eight months after "commenced" (PR p.3) | (c) hedged retreat | Medium, unquantified |
| 5 | Objects: IPO "working capital requirements" (Pros p.36 RF47) | Objects list only debt and GCP (Pros p.73) | (b) silent drop | Low: template residue |

The boiler accessories and weldmesh business was dropped but with acknowledgement (Pros p.234), so it is not a quiet abandonment.

**Phase 6 verdict: [YELLOW] Watch.** Number claims largely hold; framing claims drift. **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the drift is of framing and timing.

## PHASE 7: MULTI-STRATEGY SIGNALS

| Strategy | Result | Top three reasons |
|---|---|---|
| Value + Quality | WATCHLIST | (1) ROE 55% and ROCE 23% in FY26 but on a partly plugged half-year margin; (2) accounting quality 5/10, CFO/PAT 35% to 85%; (3) market cap Rs 1,000 Cr at CMP Rs 400 (Pres p.29) is 27.8x FY26 audited PAT and 16.7x to 18.2x guided FY27 PAT (derived) |
| **GARP** | WATCHLIST | (1) Growth evidenced: revenue CAGR FY24 to FY26 62.8% and restated PAT 188.8%, order book Rs 395.6 Cr covering 114% to 134% of H2 revenue need (derived). (2) The transition: pure conversion to Model 2 and 3 raises EBITDA per tower by 1.6x (25 to 30 lakh to 40 to 50 lakh) while revenue per tower rises about 6x, so margin falls and capital per tower rises. [INFERENCE] returns on incremental capital fall unless working capital stays at the Sep-26 level (47 receivable days, 38 stock days on H1 revenue, derived). The observation that separates "pre-buy then run-off" from "structurally higher capital": the March 2027 balance sheet. (3) Tax-regime risk is binary: 9.7% less PAT per rupee of PBT at 25.168% |
| **Turnaround** | FAIL | Not a turnaround. FY24 profit was low (PAT 8.1%) but positive and CFO positive every year. The "transition" is mix and scale, not recovery from distress. The ugly optic (margin 42.7% to 23.4%) is largely an artifact of the mix climb in H1 FY27, but the FY26 base margin is itself in doubt (Phase 3C), so the proof gate cannot be assessed here |
| Capex-led growth | WATCHLIST (best fit) | Capex 8.2x depreciation in FY26 and 4.2x in H1; capacity 300 to 612 towers; funded by an IPO-cleaned balance sheet. Proof is utilisation and Kutch approval, both NOT FOUND |
| Cash flow compounder | FAIL today | FCF (8,053.92) FY26 and (2,511.09) H1 FY27 |
| Contrarian | FAIL | Newly listed, no negative-sentiment evidence in corpus |
| Insider confidence | WATCHLIST | Promoters sold Rs 42.39 Cr; but 65.26% is locked in and the CMD lent Rs 21.68 Cr after listing |
| Guidance divergence | WATCHLIST | Guidance implies a smaller H2 lift than any past year; towers needed are 39% to 62% above H2 FY26 |

**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because no strategy row fails on integrity.

## PHASE 8: FINAL VERDICT DASHBOARD

**Snapshot.** Tubular wind-tower maker, Koppal and Kutch, 612-tower nameplate. FY26 revenue Rs 143.27 Cr, EBITDA 6,122.99 lakh (42.7%), audited PAT Rs 35.95 Cr. H1 FY27 revenue Rs 153.97 Cr, EBITDA 23.4%, PAT Rs 14.39 Cr. Order book Rs 395.58 Cr. Market cap Rs 1,000 Cr (Pres p.29).

| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | [YELLOW] |
| 2 Notes | [YELLOW] with [RED] on tax and Darpan |
| 3 Financials | [YELLOW] |
| 4 Risks and MD&A | [YELLOW] |
| 5 Governance | [YELLOW] |
| 6 Front matter | [YELLOW] |
| 7 Best fit | Capex-led growth, WATCHLIST |

**Quality score: 5.0 / 10.**
| Component (25% each) | Score | Basis |
|---|---|---|
| Governance | 4 | Young promoter-controlled board; 24 Oct filing conflict; ROC and EPFO lapses; KMP churn. Offsets: no pledge, lock-in, no SEBI action |
| Accounting quality | 5 | B02 5/10; no capitalised-interest amount; four Darpan versions |
| Balance sheet | 6 | Gearing 0.15x at Sep-26; large capital advances and heavy working capital; CMD loan |
| Earnings quality | 5 | Half-year margin plug; CFO 35% to 85%; tax rate at risk; real volume growth |

**Top 3 strengths.** (1) Volume and revenue growth are filed and audited: 114, 135, 210 towers; revenue 54.1 to 143.3 Cr; H1 FY27 107 towers (Pres p.18). (2) Balance sheet reset: 115 Cr of IPO money repaid debt in 53 days, gearing 1.43x to 0.15x (H1 p.6-7). (3) Per-model unit economics reconcile to H1 FY27 EBITDA (Phase 3C).

**Top 3 red flags.** (1) Section 115BAB demand 367.25 lakh unprovided, outside the audited notes, and denied as a "tax litigation" in the 24 Oct filing (Pros p.241; Ann p.3). (2) 3,003.57 lakh of capital-goods advances with no named vendor, plus 97.60 lakh Darpan fee and a four-version Darpan record (AFS p.27; Pros p.50). (3) FY26 margin base and half-year split are not run-rate; FY27 depends on H2 delivering 296 to 346 Cr from 206 to 240 towers (PR p.2; derived).

**Monitorables.**
| Metric | Threshold | Where | Why |
|---|---|---|---|
| H2 FY27 revenue | At least Rs 296 Cr for the floor; Rs 346 Cr for the top | FY27 results, about May 2027 | Guidance floor 450 |
| Towers produced in H2 FY27 | At least 206 at H1 realisation; 240 to 280 at order-book realisation | Results and presentation | Capacity test |
| H2 FY27 EBITDA margin | About 20% (on Rs 346 Cr, PAT 55) to 25.5% (on Rs 296 Cr, PAT 60); 23.4% is the H1 level | Results | Needed for PAT 55 to 60 (derived) |
| Revenue and cost by model per half-year | Provided at all | Presentation, call transcript | Settles mix vs timing |
| Section 115BAB rectification order | Granted vs denied | NSE Reg 30 filing | 9.7% of PAT per rupee PBT |
| Capital-goods advance conversion | Fall below 3,003.57 lakh; CWIP and PPE rise | Half-year balance sheet note | 10.3% of assets |
| Kutch approval and Gujarat revenue | Above 8.78 Cr per half | Presentation | 31% of nameplate |
| Receivable and inventory days | Receivables under 60 days; stock under 90 days of revenue at 31 Mar 2027 | Balance sheet | Tests run-off vs structural |
| CMD loan terms | Date, tenor, security disclosed; repaid | Reg 30, notes | Funding of capex |
| FY26 annual report and AGM | Filed | NSE | Board's report is absent |
| H1 FY27 call transcript | Filed | NSE | NO-CONCALL MODE closure |

**One-line verdict.** Capex-led volume growth with real order cover, but a margin base and tax rate that are not yet settled, so the best fit is Capex-led growth on WATCHLIST with position size carrying the caution.

## STAGE 5 MAP: DATED FORWARD STATEMENTS AND PAGES TO READ (NO-CONCALL MODE)

| Topic | Statement | Anchor |
|---|---|---|
| Guidance | FY27 revenue Rs 450 to 500 Cr, PAT Rs 55 to 60 Cr | PR p.2-3; Pres p.7 |
| Order book | Rs 395.58 Cr, 320 towers, 8 customers, LOIs Rs 44.05 Cr, execution by end Q1 FY28 | PR p.2-3; Pres p.7, p.21 |
| March order book | 35,981.72 lakh, 379 towers, completion dates 30 Sep 2026 to 31 Mar 2027 | Pros p.114; List p.8 |
| Large orders | 38 towers Rs 133.98 Cr, Q4 FY27; 10 towers Rs 58.32 Cr incl. GST, Q1 FY28 | Order 2026-09-10 p.2; Order 2026-10-29 p.2 |
| LOI history | LOI Rs 120 Cr for 38 towers (Q1 FY27) | List p.2, p.8; CRISIL p.1 |
| Kutch | 16 towers a month, 192 a year; "approvals and ramp-up underway"; "trial runs underway"; client approval ongoing | Pres p.18; PR p.3; Ann 2026-10-05 p.3; Pros p.111, p.115 |
| In-house internals | "Koppal Internals Plant Started"; kit manufacturing "strengthens backward integration" | List p.9; Pres p.6, p.11; Pros p.115 |
| Seasonality | 70% to 80% of revenue in H2 | Pres p.22; Pros p.23 |
| Margin framing | EBITDA per tower rises as mix moves; percentage margin moderates | Ann 2026-10-05 p.2; PR p.3; List p.16 |
| Unit economics | Three models with revenue, EBITDA per tower and margin ranges | Pres p.15; List p.16 |
| Objects of the offer | 115.00 Cr repay debt, 3.64 Cr GCP, 24.05 Cr issue cost, all in FY27; utilisation report | Pros p.73-74; H1 p.5-6; MA p.6-8 |
| Capacity | Koppal 420 a year (from 300), Kutch 192, total 612; utilisation 38%, 45%, 48% | Pres p.18; Add p.17; Pros p.111, p.124 |
| MD&A pages | Overview and KPI | Pros p.228-229 |
| | Results table | Pros p.230-231 |
| | Revenue and Kutch narrative | Pros p.232 |
| | Cost, finance cost, borrowing-cost capitalisation | Pros p.233-234 |
| | Material developments | Pros p.236-237 |
| | Capitalisation statement | Pros p.238 |
| Working capital | Risk factor, KPI and CRISIL view (292 gross current asset days) | Pros p.29; CRISIL p.2 |
| KPI pages | EBITDA, RoNW, RoCE | Pros p.229, p.113 |
| Promoter loan | CMD loan Rs 21.68 Cr at 6% | Pres p.8 |
| Rating | BBB/Stable; margin about 40%; cash accrual Rs 80 Cr; gearing below 0.05x | CRISIL p.1-2 |
| Tax | Rectification pending, no date | Pros p.240-241 |
| Governance | CS change; SME exemption | Ann 2026-10-31 p.1-3; Ann 2026-10-24 p.2-3 |

## SOURCES NOT FOUND (carried)
Annual report, Board's Report, MD&A for the year, Corporate Governance Report, attendance, AGM notice, call transcript (call held 09 Nov 2026, B00), vendor list for the capital advance, revenue by model per half-year, customer-wise ageing, capitalised borrowing cost amount, capital commitments, warranty provision, lien on FDs, five-year repayment schedule, covenant tests, outcome of the 226.93 lakh demands, CMD loan date and tenor, Kutch completion date.

```yaml
stage: B03-ardeep
company: "ANAWIL"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "ANNUAL REPORT ABSENT (HIGH, carried from B00): no annual report exists (listed 2026-08-10). Backward history built from the Prospectus (business, MD&A, risk factors, objects, management, restated FY24 to FY26), the Addendum and the audited FY26 statements with FY25 and FY24 bound in. No Board's Report, annual MD&A, Corporate Governance Report, attendance, Section 197(12) table, AGM notice or internal audit report."
  - "AFS text is OCR (rapidocr, 103 pages); figures that matter were checked against the Prospectus or the H1 comparative. FY24 statements are in INR thousand; others INR lakh. FY25 CARO annexures not bound."
  - "CONCALL TRANSCRIPT ABSENT (NO-CONCALL MODE): H1 FY27 call held 2026-11-09, transcript not yet filed. Forward statements come from the press release, presentations, orders, the 05 Oct 2026 investor-conference note and the CRISIL rationale."
  - "NOT FOUND: vendors, order values, ageing and security for the 3003.57 lakh capital-goods advances; amount of borrowing cost capitalised; booking line of the 97.60 lakh Darpan fee; revenue and cost by contract model per half-year; customer-wise receivables; third-party inventory; capital commitments; Kutch completion date; CMD loan date, tenor and security."
  - "NOT FOUND: board and committee attendance, median employee pay, auditor non-audit fees, FY26 AGM date, outcome of the 226.93 lakh tax demands, basis of the 367.25 lakh demand beyond the Prospectus text, tower count behind the Rs 32.82 lakh EBITDA per tower."
  - "Screener P&L, Quarters, Balance Sheet, Cash Flow sheets absent (carried from B00); research folder empty (no broker notes)."
flags:
  - {type: FLAG-CASH, reason: "FY26 audited CFO 1246.69 lakh is 34.7% of PAT 3595.25; restated 1843.94 is 50.3%; capex-neutral 2814.94 to 3114.75 (78% to 85%). CFO/PAT ran 202% FY24, 70% FY25, 35% FY26, then 197% in H1 FY27 as March stock unwound. Working capital absorbed 5241.70 lakh in FY26. AFS p.15, p.27; H1 p.8; Pros p.29."}
  - {type: FLAG-PROMOTER-PRELIM, reason: "No pledge (SHP30Sep; Pros p.67). Promoter selling: 7.20 lakh shares at Rs 101 in Sept 2025 (Rs 7.27 Cr) and 13.01 lakh shares in the IPO OFS at Rs 270 (Rs 35.12 Cr); promoter stake 89.35% to 65.26%, of which 18.9 points is fresh-issue dilution and 5.2 points OFS. CMD lent Rs 21.68 Cr at 6% after listing (Pres p.8). Full verdict from B08. Pros p.67-68, p.73."}
  - {type: FLAG-TAX-REGIME, reason: "Section 115BAB demand 367.25 lakh dated 17 Jul 2026, AY 2025-26, rectification pending (Pros p.240-241); 2.8x the 8.008 point rate gap on AY 2025-26 PBT (130.7 lakh, derived); unprovided and absent from audited notes (AFS p.5); Ann 2026-10-24 p.3 states no ongoing tax litigation."}
  - {type: FLAG-MARGIN-BASE, reason: "FY26 half-year EBITDA per tower is 16.4 lakh (H1) and 34.5 lakh (H2) on near-equal revenue per tower (66.7 and 68.8 lakh); H1 is 40% below and H2 8% above the band from company unit economics, full year within 1%. Mix does not explain it; timing or cost recognition does [INFERENCE]. H2 FY26 margin 50.1% exceeds the top of the Model 1 band. H1 p.4; Pres p.15, p.18."}
  - {type: FLAG-DISCLOSURE, reason: "Tower count 107/108/110 for H1 FY27; CFO 12.5 vs 18 Cr; order book mixes GST-inclusive 58.3 Cr and ex-GST values; 516.76 vs 433.89 unsecured loans; Board approval date 13 vs 18 June 2026; Kutch 'commenced' vs trial runs. Pres p.7, p.21, p.25, p.28; Pros p.34, p.237; PR p.3."}
phase_verdicts: {p1: "YELLOW Watch: unmodified opinions, no KAMs, cross-document conflicts on title deeds and dues", p2: "YELLOW Watch with RED items on 115BAB tax and Darpan trail; accounting quality 5/10", p3: "YELLOW Watch: FLAG-CASH carries; leverage reset real; FY26 half-year margin split not mix", p4: "YELLOW Watch: Prospectus MD&A only; missing risks on tax, Kutch approvals, margin dilution; guidance credibility MEDIUM", p5: "YELLOW Watch: promoter-controlled young board, 24 Oct tax statement conflict, no pledge", p6: "YELLOW Watch: framing drift EBITDA margin to EBITDA per tower; five quiet-abandonment items", p7_best_fit: "Capex-led growth WATCHLIST; GARP WATCHLIST; Turnaround FAIL"}
overall_quality: 5
quality_components: {governance: 4, accounting: 5, balance_sheet: 6, earnings: 5}
kill_switch_notes:
  - "P1: Based on phases so far, a human reviewer would not have reason to stop, because opinions are unmodified and no fraud, default or going-concern language appears."
  - "P2: would not have reason to stop; flags are disclosure and classification gaps (tax demand, Darpan fee, no contingent note), not proven misstatement."
  - "P3: would not have reason to stop; cash flow is explainable by the March stock build and leverage has fallen to 0.15x."
  - "P4: would not have reason to stop; omissions are of disclosure, numbers reconcile."
  - "P5: would not have reason to stop; no integrity breach shown, but the 24 Oct 2026 'no tax litigation' statement should be put to management."
  - "P6: would not have reason to stop; drift is of framing and timing."
triple_pass_verification:
  verified: 13
  discrepancies:
    - {finding_rank: 10, triple_pass_value: "unsecured recallable loans: directors 433.89 lakh (AFS p.23 per B02)", ar_value: "516.76 lakh (Pros p.34 RF37); with Darpan 87.27 the sum is 521.16", note_ref: "Pros p.34; AFS p.23; difference 82.87 unresolved"}
    - {finding_rank: 3, triple_pass_value: "FY26 capex funded by debt 7313.88 lakh", ar_value: "7341.12 lakh gross (5973.82 + 1367.30); difference 27.24; FCF (8053.92) unchanged", note_ref: "AFS p.15"}
    - {finding_rank: 1, triple_pass_value: "extra tax exposure FY24 to FY26 if 115BAB denied: 515.50 lakh", ar_value: "518.3 lakh on 8.008% x restated PBT 6472.59; and the 367.25 demand is 2.8x the 130.7 lakh rate gap on AY 2025-26 PBT", note_ref: "Pros p.240-241, p.231"}
missing_risks:
  - {risk: "Loss of Section 115BAB rate as a stand-alone risk with PAT effect", evidence: "Demand 367.25 lakh; rate gap 8.008 points; contingent-liability table shows nil FY26", anchor: "Pros p.28, p.240-241"}
  - {risk: "Margin dilution from the shift to Model 3", evidence: "Model 3 was 4 towers in FY26 and 64.3% of H1 FY27 revenue; EBITDA margin 42.7% to 23.4%; reframing to EBITDA per tower on listing day", anchor: "Pros p.232; PR p.2; List p.16"}
  - {risk: "Kutch approvals and ramp-up", evidence: "client approval ongoing, trial runs underway, Gujarat revenue 3.23 Cr in H1 FY27 vs 8.78 Cr for FY26 (all March)", anchor: "Ann 2026-10-05 p.3; PR p.3; Pres p.23"}
  - {risk: "Rs 30.0 Cr of advances to unnamed capital-goods vendors", evidence: "3003.57 lakh, 98% of short-term advances, 10.3% of assets", anchor: "AFS p.27, p.16"}
  - {risk: "GST credit accumulation as the mix moves to 5% billed Model 3 [INFERENCE, input rate outside corpus]", evidence: "output billed at 5% (140.68 vs 133.98); balance with revenue authority 827.37 to 1878.59", anchor: "Order 2026-09-10 p.1; AFS p.27"}
  - {risk: "Tower weight lowers effective capacity", evidence: "installed 207,000 t; 316 t per tower at Koppal; latest order 474 t per tower gives about 437 towers vs 612", anchor: "Pros p.25; Add p.17; Ann 2026-10-29 p.2"}
  - {risk: "Capex funding after the IPO", evidence: "objects fund only debt; H1 capex 5339.49 vs CFO 2828.40; CMD loan Rs 21.68 Cr at 6%", anchor: "Pros p.73; H1 p.8; Pres p.8"}
  - {risk: "Order book counts a GST-inclusive order at face (overstated about 2.78 Cr)", evidence: "58.32 Cr incl. GST counted as 58.3 in book", anchor: "Ann 2026-10-29 p.1; Pres p.21"}
  - {risk: "FY26 AGM and annual report not evidenced", evidence: "no notice or report in corpus or NSE API; due by 30 Sep 2026 (legal rule outside corpus)", anchor: "B00 input_gaps"}
guidance_table:
  - {claim: "FY27 revenue", number: "Rs 450 to 500 Cr", timeframe: "FY27", credibility: "MEDIUM: H2 needs 296 to 346 Cr; implied H2/H1 1.9x to 2.2x vs 2.4x FY24, 4.1x FY25, 2.5x FY26; towers needed 206 to 240 vs 148 in H2 FY26 (PR p.2; Pros p.23)"}
  - {claim: "FY27 PAT", number: "Rs 55 to 60 Cr", timeframe: "FY27", credibility: "MEDIUM: holding the H1 margin of 23.4% gives 55.1 to 64.3 Cr on the revenue range; revenue is the stretch, not margin (PR p.2; H1 p.4)"}
  - {claim: "Order book execution", number: "Rs 395.58 Cr, 320 towers, plus LOIs Rs 44.05 Cr", timeframe: "by end Q1 FY28", credibility: "MEDIUM: March book was due by 31 Mar 2027; implied inflow at least 189.73 Cr since March (PR p.2; Pros p.114)"}
  - {claim: "Large order 38 towers", number: "Rs 133.98 Cr ex GST", timeframe: "Q4 FY27", credibility: "MEDIUM: LOI had been Rs 120 Cr (Order 2026-09-10 p.2; List p.8)"}
  - {claim: "Kutch ramp", number: "192 towers a year, 16 a month", timeframe: "no date; 'nearing completion'", credibility: "LOW to MEDIUM: client approval ongoing at 05 Oct 2026 (Pres p.18; PR p.3; Ann 2026-10-05 p.3)"}
  - {claim: "EBITDA per tower rises as mix shifts", number: "Rs 32.82 lakh H1 FY27 vs 29.2 FY26", timeframe: "ongoing", credibility: "MEDIUM: mix-implied EBITDA range 30.0 to 42.8 Cr holds; tower base unreconciled (PR p.3; Pres p.15)"}
  - {claim: "Operating margin about 40% (CRISIL)", number: "40%", timeframe: "medium term", credibility: "LOW: H1 FY27 23.4% (CRISIL p.1; H1 p.4)"}
  - {claim: "Gearing below 0.05x and cash accrual Rs 80 Cr a year (CRISIL)", number: "0.05x; 80 Cr", timeframe: "Mar 2027", credibility: "LOW to MEDIUM: Sep-26 gearing 0.148x incl. CMD loan, 0.053x excl.; H1 cash PAT 27.3 Cr (CRISIL p.1-2; H1 p.7; Pres p.9)"}
  - {claim: "IPO money used as per objects", number: "115.00 + 3.69 + 23.87 = 142.56 Cr", timeframe: "by 30 Sep 2026", credibility: "HIGH: delivered in 53 days (H1 p.6; MA p.6-8)"}
monitorables:
  - {metric: "H2 FY27 revenue", threshold: "at least Rs 296 Cr (floor) to Rs 346 Cr (top)", where: "FY27 results, about May 2027", why: "decides the Rs 450 Cr guidance floor"}
  - {metric: "H2 FY27 towers produced", threshold: "at least 206 at H1 realisation of 1.44 Cr; 240 to 280 at order-book realisation of 1.236 Cr", where: "results and presentation", why: "capacity and execution test vs 148 in H2 FY26"}
  - {metric: "H2 FY27 EBITDA margin", threshold: "about 20% (on Rs 346 Cr, PAT 55) to 25.5% (on Rs 296 Cr, PAT 60); H1 level 23.4%", where: "results", why: "needed for PAT Rs 55 to 60 Cr (derived)"}
  - {metric: "Revenue and cost by model for each half-year", threshold: "disclosed", where: "presentation or call transcript", why: "separates mix from timing for FY26 and FY27 margin base"}
  - {metric: "Section 115BAB rectification order", threshold: "granted vs denied", where: "NSE Reg 30 filing", why: "9.7% less PAT per rupee of PBT if denied"}
  - {metric: "Capital-goods advance and CWIP", threshold: "advance below 3003.57 lakh as CWIP and PPE rise; vendors named", where: "half-year balance sheet and note", why: "10.3% of assets paid before delivery"}
  - {metric: "Kutch approval and Gujarat revenue", threshold: "Gujarat revenue above 8.78 Cr per half", where: "presentation geography slide", why: "Kutch is 31% of nameplate"}
  - {metric: "Receivable and inventory days at 31 Mar 2027", threshold: "receivables under 60 days, stock under 90 days of revenue", where: "FY27 balance sheet", why: "tests pre-buy run-off vs structurally higher capital per tower"}
  - {metric: "CMD loan terms and repayment", threshold: "date, tenor and security disclosed", where: "Reg 30 filing and notes", why: "capex is funded by it after the IPO"}
  - {metric: "FY26 annual report and AGM", threshold: "published", where: "NSE", why: "Board's Report and governance data are absent"}
ar_new_downstream_entities:
  - name: "SANY (WTG OEM; Sany WTG towers)"
    where_in_ar: "Pros p.114 order book; Pres p.21"
    entity_type: "customer OEM (named by product description; legal customer letters anonymised)"
  - name: "Envision (WTG OEM; Envision WTG towers, EN-156 3.3MW and EN-182 5MW)"
    where_in_ar: "Pros p.114; Pres p.21; Order 2026-09-10 p.2; Order 2026-10-29 p.2"
    entity_type: "customer OEM / end project (FDRE wind project, Andhra Pradesh)"
  - name: "Darpan Infrastructure Private Limited"
    where_in_ar: "Pros p.50-51 RPT; Pros p.30 registered office; Pros p.241-242 criminal case MS STP Ltd"
    entity_type: "promoter group company: guarantor, lender, contractor, landlord, former holding company"
  - name: "India-Ahead Venture Fund"
    where_in_ar: "Pros p.62-63 private placement of 7,00,000 shares at Rs 101"
    entity_type: "pre-IPO investor"
  - name: "Mukul Mahavir Agrawal"
    where_in_ar: "Pros p.62 private placement of 6,80,000 shares at Rs 101"
    entity_type: "pre-IPO investor"
  - name: "Bank of Baroda; The Cosmos Co-operative Bank Ltd"
    where_in_ar: "Pros p.74-76; CRISIL p.4"
    entity_type: "lenders"
strengths_top3:
  - "Volume and revenue growth are filed and audited: 114, 135, 210 towers; revenue Rs 54.1 to 143.3 Cr; H1 FY27 107 towers and Rs 153.97 Cr (Pros p.111; Pres p.18; H1 p.4)"
  - "Balance sheet reset: Rs 115 Cr of IPO money repaid debt in 53 days; debt to equity 1.43x to 0.15x (H1 p.6-7; MA p.6)"
  - "Per-model unit economics reconcile: H1 FY27 EBITDA 36.08 Cr sits inside the 30.0 to 42.8 Cr range implied by slide-15 economics and the 64.3/21.2/10.8 mix (Pres p.15; PR p.2)"
red_flags_top3:
  - "Section 115BAB demand 367.25 lakh unprovided, outside audited notes, 2.8x the pure rate gap, and denied as tax litigation in the 24 Oct 2026 governance filing (Pros p.241; Ann 2026-10-24 p.3)"
  - "3003.57 lakh of capital-goods advances to unnamed vendors, 97.60 lakh Darpan fee with no P&L line, and four versions of the Darpan record (AFS p.27; Pros p.50)"
  - "FY26 margin base and half-year split are not run-rate; FY27 guidance needs 206 to 240 towers in H2 against 148 in H2 FY26 (PR p.2; H1 p.4; derived)"
best_fit_strategy: "Capex-led growth (WATCHLIST); GARP WATCHLIST; Turnaround FAIL"
one_line_verdict: "Capex-led volume growth with real order cover, but an unsettled margin base and tax rate; WATCHLIST with position size carrying the caution."
analyst_note: "No annual report exists, so this stage read the Prospectus MD&A and audited statements. Three results a later stage cannot rebuild from the fields above. One: FY26 revenue per tower was flat across halves (66.7 and 68.8 lakh) while EBITDA per tower went 16.4 to 34.5 lakh, so the 50.1% H2 margin is a timing or cost-recognition plug, not mix; B02's reading B is favoured for FY26, mix is right for H1 FY27. Two: FY26 utilisation of 48.17% is 210/(420+16), measured on year-end capacity. Installed tonnage of 207,000 t supports about 437 towers at the 474 t weight of the latest order, not 612. Three: guidance needs H2 at 66 to 69% of the year, a smaller seasonal lift than any past year, so revenue (towers) is the stretch and margin is not. Conservatism belongs in position size."
```
