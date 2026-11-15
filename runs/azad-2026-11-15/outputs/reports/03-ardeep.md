# Stage 3, Annual Report Deep Dive, Backward Read (pipeline mode)
Company: AZAD (Azad Engineering Ltd). Run date: 2026-11-15. Model: claude-sonnet-5-5.

## Conventions
- Source key. AR26 = Annual_Report_2026.pdf (FY2025-26). AR25 = Annual_Report_2025.pdf (FY2024-25, comparison only). PRO = AZAD_Prospectus_2023-12-23.pdf. "[p.N]" is the PDF page marker; the printed folio is the PDF page minus 3.
- Unit. INR million (Rs Mn), as printed on the face of each statement. Nothing is converted. "[calc]" is arithmetic on printed figures. "[INFERENCE]" is my reading, not filed text. Order book figures are printed in Rs Mn and Rs Cr in different places; the unit is named each time.
- Reading order. Backward: auditor's reports and CARO, notes, statements (cash flow first), MD&A and risk text, corporate governance, then the Chairman's letter and front matter last.
- Phase verdicts use text labels GREEN / YELLOW / RED. Every kill switch is informational. The run continues after each one.
- Scope note. The AR was read directly for this stage. The B02 report was used as the starting list, and every item in it that I relied on was checked against the page.

## Load-bearing facts, checked first

| # | Fact | What the AR shows | Status |
|---|---|---|---|
| 1 | July falsifier: OCF sign, working-capital days vs 344, any factoring | Consolidated OCF (1,189.66) Rs Mn vs 536.67 (AR26 [p.193]). Standalone (1,232.63) vs 628.85 (AR26 [p.123]). The AR does print working-capital days: 244 at FY26 year end vs 202 a year earlier, Chairman's letter (AR26 [p.7]); the definition is NOT FOUND IN DOCUMENT. B02 said the AR prints none; that is wrong and is corrected here. The July 344 is on a basis the AR does not state, so 244 and 344 are not comparable. Revenue-basis calc gives 336.3 vs 265.6 (matches B01). Text search of the whole AR for factoring, discounting, bills discounted, recourse: no hit that relates to receivables. H1 FY27 OCF (436.24) Rs Mn comes from B01 (Q2 FY27 results p.11); I did not re-read it. | FALSIFIER DIRECTION SUPPORTED by the AR. Nothing in the AR shows factoring propping the number. The AR also cannot confirm clean conversion. |
| 2 | Growth guidance over 25% vs delivered; capacity ramp | AR25 Board's Report (AR25 [p.40]): "we are targeting revenue growth of ~30%" for FY26. AR26 Outlook (AR26 [p.36]): "Management has consistently guided towards sustained revenue growth in excess of 25% per annum". Delivered: consolidated +31.84%, standalone +30.35% (AR26 [p.38]). Ramp: Chairman (AR26 [p.8]) says utilisation climbs through FY 2026-27 and "towards full utilisation in FY 2027-28"; MD&A (AR26 [p.31]) says the dedicated facilities "are expected to progress toward stable operating levels over the coming year, with peak utilisation anticipated over a longer horizon". Hedged retreat, see 6E. A "Q4 FY27 ramp" statement is NOT FOUND IN DOCUMENT. | Revenue guidance delivered. Ramp timing softer in the MD&A than in the letter. |
| 3 | Customer concentration | Top customer 1,123.97 Rs Mn = 18.64% of 6,029.75 [calc] (AR26 [p.242]), up from 648.81 = 14.19% (AR26 [p.242]). Two customers at or above 10% of revenue (AR26 [p.237]) vs one in FY25. Top-5: 1,123.97 + 1,711.10 = 2,835.07 = 47.02% [calc]; FY25 comparable 2,352.65 = 51.44% [calc] (AR25 [p.238]). B02's 41.3% is not anchored, see Phase 2. Tripwires 20% and 65%: top-1 is 1.36 points under 20%; top-5 is far under 65%. | Both pass. Top-1 rising and near. |
| 4 | QIP deployment, capex commissioning | QIP 7,000.00 Rs Mn: capex object 3,686.65 of 5,250.00 used; GCP 1,562.10 fully used; issue expenses 153.98 of 187.90; unutilised 1,597.27 (AR26 [p.74]; Note 40 AR26 [p.249]). Auditor: idle funds 1,600.06 (CARO x(b), AR26 [p.117]). **New:** on 2026-02-13 the Board extended the timeline for the objects from 2026-03-31 to 2027-03-31 (AR26 [p.74]). Gross PPE additions 3,961.55 (AR26 [p.214]); CWIP 2,566.82 vs 797.80; capital advances 1,237.18 (AR26 [p.219]); commitments 1,182.77 (AR26 [p.233]). Phase 1 build-out "roughly 70% to 80% complete" (AR26 [p.7]). | Money parked in deposits, not diverted. Capex use is behind the original deadline. Commissioning is not yet visible in cash. |

## Corrections to B02 found in this stage (carry to downstream stages)
1. The AR prints company working-capital days (244 vs 202, AR26 [p.7]). B02 input_gaps and Fact 1 say it does not.
2. Standalone cash flow is on AR26 [p.123] (financing on [p.124]). B02 P3-1 cites "[page 156]". That page is wrong.
3. The 76.6% plant share of gross PPE is Note 3(a), AR26 [p.214]. B02 attributes it to Note 6.
4. B02 Top-15 #11 and P3-2 rest on Note 44. Note 44 conflicts with Form AOC-1; see Phase 2, "Note 44 vs AOC-1".
5. B02 says "management growth guidance NOT FOUND in the notes". The AR does carry it (AR26 [p.36]); it sits in the MD&A, not the notes.
6. The 41.3% top-5 figure is an equal-split assumption. Do not use it.

---

# PHASE 1: AUDITOR'S REPORT AND CARO

## 1A Core opinion
| Item | Finding | Anchor |
|---|---|---|
| Opinion type | Unmodified, standalone and consolidated. "give a true and fair view in conformity with the Indian Accounting Standards" | AR26 [p.109], [p.183] |
| Basis | SAs under section 143(10); independence confirmed | AR26 [p.109] |
| Going concern | No material uncertainty paragraph. Only the standard responsibility text. CARO xix: "nothing has come to our attention, which causes us to believe that any material uncertainty exists as on the date of the audit report that Company is not capable of meeting its liabilities existing at the date of balance sheet as and when they fall due within a period of one year" | AR26 [p.111], [p.118] |
| Books and audit trail | Not a modified opinion, but a reservation is recorded: "proper books of account ... except for the matters stated in the paragraph 2(h)(vi)" (audit trail not enabled at database level). Paragraph 2(g) uses the word "reservation" | AR26 [p.111] |
| Report date | 2026-05-15 (both). Partner Ananthakrishnan Govindan, Membership 205226 | AR26 [p.112], [p.187] |

## 1B Key audit matters
| KAM | Why key | How addressed | Risk |
|---|---|---|---|
| Revenue recognition, cut-off (only KAM, both reports) | Point-in-time recognition; risk that control has not transferred and obligations are unfulfilled at the date | Seven procedures, including controls testing, contract review, shipping documents, customer balance confirmations, near-year-end evidence, analytics and journal entry testing (AR26 [p.109] to [p.110]; consolidated [p.183] to [p.184]) | YELLOW. Q4 revenue was 1,573.9 Rs Mn, 26.1% of the year [calc] (AR26 [p.13]). The policy carries bill-and-hold style criteria (customer's explicit request, identified goods, no ability to use) (AR26 [p.200]). |

No KAM on inventory (+73.9%), receivable provisioning, CWIP 2,566.82, or the level 3 put/call liability 171.50. The auditor did not judge them key. [INFERENCE] The ECL matrix and inventory write-down are not disclosed, so this reduces what the reader can test.

## 1C Emphasis of matter and other matters
None in either report. The "other information" paragraph says the Chairman's statement and the BRSR were "expected to be made available to us after that date" (AR26 [p.110], [p.184]). The front matter is therefore unaudited and was finished after the audit report date. It contains events dated 2026-07-22 (AR26 [p.7], [p.10], [p.22]).

## 1D CARO 2020, clause by clause (standalone, AR26 [p.114] to [p.118])
| Clause | Remark | Amount (Rs Mn) | Colour |
|---|---|---|---|
| i(c) title deeds | Land not in Company's name. Mangampet 75.17 and Tunkibollaram 259.02, both allotted by TSIIC. Mangampet title "currently under dispute before the Hon'ble Court of Telangana". Separate remark: deeds of 271.88 pledged with banks, originals not with the Company | 75.17; 259.02; 271.88 | YELLOW |
| ii inventory | Physically verified; discrepancies under 10% per class; bank quarterly returns agree with books | NA | GREEN |
| iii loans | Loans to subsidiaries: granted 7.53, outstanding 196.41; nothing overdue over 90 days; no loans to promoters or related parties | 196.41 | GREEN |
| vii(a) statutory dues | "slight delay in a few cases"; provident fund pending over six months | 1.00 | YELLOW (small) |
| vii(b) disputed dues | Income tax 19.67 (paid 2.00); customs 218.57 (FY20 to FY26, Customs Adjudicating Authority); customs 2.37 (FY15, Commissioner Appeals); GST 2.13 (paid 0.20) | 242.74 total | YELLOW |
| ix(a) to (c), (e), (f) | No default; not wilful defaulter; term loans applied to purpose | NA | GREEN |
| ix(d) short-term funds | "no funds raised on short-term basis have been utilised for long-term purposes" | NA | YELLOW. **Contradiction** with Phase 3: working-capital loans rose 488.15 to 1,193.27 (+144.4%) (AR26 [p.226]) while capex cash was 5,724.80 and OCF was (1,189.66). The notes cannot prove or disprove it. |
| x(b) private placement | Funds used for purpose except idle funds 1,600.06 in bank deposits; maximum idle during the year 6,430.00; 1,599.99 in fixed deposits and 0.07 in the monitoring account | 1,600.06 | YELLOW |
| xi fraud | No fraud; no ADT-4; no whistle-blower complaints | NA | GREEN |
| xiii, xiv | Related party compliance; internal audit commensurate | NA | GREEN |
| xvii cash losses | Standalone: none | NA | GREEN |
| xx CSR | No unspent amount. CSR 14.01 spent vs 14.01 required (2% of average net profit 700.50) (AR26 [p.51] to [p.52]) | 14.01 | GREEN |

Consolidated report adds the sub-level CARO listing (AR26 [p.187]): Holding i(c), vii(a), vii(b), x(b); **Azad VTC: vii(a) and xvii; Azad Prime: vii(a) and xvii.** Clause xvii means cash losses in both the current and the preceding year. This conflicts with Form AOC-1 for Azad VTC (profit), see Phase 2.

## 1E Auditor continuity
| Item | Finding | Anchor |
|---|---|---|
| Firm | M S K A & Associates LLP (LLP from 2026-01-13), FRN 105047W/W101187 | AR26 [p.43] |
| Appointment | 39th AGM, 2022-12-29, to hold office till the 44th AGM. About 3.4 years in office at the report date [calc]. First five-year term ends at the 44th AGM (date not stated) | AR26 [p.43] |
| Fees, standalone (Rs Mn) | Statutory audit 3.90 (3.90); limited review 1.20 (1.10); certification 0.30 (nil); out of pocket 0.14 (0.20); total 5.54 (5.20) | AR26 [p.161] |
| Fees, consolidated (Rs Mn) | 5.70 (5.82) | AR26 [p.232] |
| Non-audit ratio | Certification 0.30 of 5.54 = 5.4% [calc]. Not above audit fee | AR26 [p.161] |
| Fee level | Statutory audit fee 3.90 = 0.066% of standalone revenue 5,903.75 [calc]. Flat for two years while revenue rose 30.3% and total assets 18.4% [calc]. [INFERENCE] Thin fee for the scale; no evidence of impairment of independence | AR26 [p.121], [p.122] |

## 1F Standalone vs consolidated
- Extra remark: "in the absence of sufficient appropriate audit evidence in respect of two subsidiary companies, we are unable to comment whether back-up of the books of account ... have been kept in servers physically located in India on a daily basis" (AR26 [p.185]).
- Subsidiary audit trail: not enabled at application level from 2025-04-01 to 2025-04-13 and not enabled at database level for the whole year (AR26 [p.187]); Note 41(n) says the auditor could not assess whether it operated (AR26 [p.250]).
- Same firm audits the subsidiaries ("CARO reports issued by us"). No reliance on other auditors.
- Directors' Report calls both reports unmodified and "self-explanatory" (AR26 [p.43]). That describes the opinion, not the reservations above.

**Phase 1 summary.** One KAM, unmodified opinion, clean fraud and whistle-blower answers, adequate internal financial controls (AR26 [p.119]). Weak points: audit trail, title deeds, subsidiary CARO remarks, ix(d) against the cash picture.
**Phase 1 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because no modification, no going concern language and no fraud report exist. The run continues.

---

# PHASE 2: NOTES TO FINANCIAL STATEMENTS

## Triple-pass verification (B02 Top 15 against the page)
Result: **9 verified clean, 6 verified with a correction.** No finding was wrong in direction.

| Rank | B02 value | AR check (Rs Mn unless stated) | Result |
|---|---|---|---|
| 1 | OCF (1,189.66) vs 536.67; WC drain 3,034.45; standalone (1,232.63) | Same (AR26 [p.193]; standalone [p.123]). Drain = 2,332.96 + 701.49 = 3,034.45 [calc] | VERIFIED. Page fix: standalone is [p.123] |
| 2 | Inventory 3,291.13 vs 1,893.01 (+73.9%); days 199/151, 189/178, 52/64; cycle 336 vs 266 | Same (Notes 7, 8, 15, AR26 [p.219], [p.220], [p.227]). Days recomputed on revenue 6,029.75 and 4,573.54: 199.2, 188.7, 51.6; 336.3 | VERIFIED |
| 3 | Government balances 1,102.51 vs 554.83; 66.7 vs 44.3 days; 74.4% of other-asset build | Same (Note 10, AR26 [p.222]). 547.68 / 736.45 = 74.4% [calc] | VERIFIED |
| 4 | Top-1 18.6%; top-5 41.3% to 47.0% | Top-1 18.64% verified. 47.0% reproducible. **41.3% reproduces only as top-1 plus 4/5 of 1,711.10 (2,492.9 / 6,029.75), an equal-split assumption.** The FY25 comparative proves the row is "next customers": 2,352.65 less 648.81 = 1,703.84 (AR26 [p.242]; AR25 [p.238]). B01's 28.4% reading is impossible: two customers at 10% or more need at least 602.98 each, so top-2 alone is at least 1,726.95, above 1,711.10 [calc] | CORRECTED. Use 47.0% |
| 5 | QIP 7,000.00; 3,686.65 of 5,250.00; GCP 1,562.10; unspent 1,597.27 (auditor 1,600.06); CWIP 2,566.82 (3.2x); commitments 1,182.77 | Same (AR26 [p.74], [p.249], [p.117], [p.217], [p.233]). 3.22x [calc]. Gap 1,600.06 less 1,597.27 = 2.79; the footnote says interest on the deposits stays in the monitoring account or deposits (AR26 [p.74]), which may explain it [INFERENCE] | VERIFIED. New: deadline extended |
| 6 | Debt 4,566.39 vs 2,435.82; net debt 2,720.48 vs net cash 4,534.45; 76.7% floating; interest cover 5.6x vs 7.2x | Same (Notes 13, 14, 35, AR26 [p.225], [p.226], [p.245]). Floating 3,501.19 / 4,566.39 = 76.7% (AR26 [p.243]). Cover = 1,724.71 / 308.19 = 5.60 and 1,318.24 / 183.89 = 7.17 [calc] | VERIFIED |
| 7 | Plant life 15 vs 7.5 years; plant 76.6% of gross PPE; 20.20 interest on capital advances | Policy table (AR26 [p.205]) prints 15 and 7.5. 76.6% = 6,885.05 / 8,991.30, **Note 3(a) [p.214]**, not Note 6. 20.20 is Note 6 (AR26 [p.219]). The policy says lives rest on "technical evaluation"; the report itself is not disclosed. Schedule II column of 7.5 years is as printed and not verified against the Act: PENDING LIVE VERIFICATION. If general plant and machinery in Schedule II is 15 years, the "double the statutory life" flag falls away. Total borrowing cost capitalised 92.04 = 35.51 (CWIP) + 36.33 (PPE) + 20.20 (advances) [calc], ties to Note 25 footnote (AR26 [p.231]); 92.04 / (308.19 + 92.04) = 23.0% [calc] | CORRECTED (note ref; aggression claim unproven) |
| 8 | Over-one-year bucket 159.77 vs 64.94; cover 56.3% vs 111.1%; charge 17.78 vs 35.76 | Buckets and cover verified (Note 8, AR26 [p.221]). **Charge is 17.78 in Note 8 and Note 34 ([p.221], [p.242]) but 17.87 in Note 27 and the cash flow ([p.232], [p.193]).** 72.15 + 17.78 = 89.93 ties to the 17.78 | CORRECTED (0.09 unexplained) |
| 9 | Other income 456.54 = 24.4% of PBT; FX 214.01 (unrealised 158.16); core PBT +24.9%; 5% rupee move costs 104.04 | 24.4% verified (AR26 [p.192]). FX 214.01 (AR26 [p.229]); 158.16 (AR26 [p.193]). Core PBT 1,416.52 vs 1,134.35 = +24.9% [calc]. **USD line is 104.07** (AR26 [p.245]), and the EUR line is (14.39) the other way, because euro borrowings of 900.28 exceed euro receivables 618.85. Net 89.68 [calc] | CORRECTED (104.04 to 104.07; add EUR offset) |
| 10 | Customs 220.94 vs 75.11; total 293.33 (1.9% of equity) | Same (Note 28, AR26 [p.232]). 218.57 + 2.37 = 220.94 ties to CARO vii(b). 293.33 / 15,288.36 = 1.92% [calc] | VERIFIED |
| 11 | Prime liability 171.50; VTC loss (41.97) 4.8x; NCI (0.62) vs 118.0 implied; adjustment +42.10 | Liability verified: 225.63 floor less 54.13 advance = 171.50 [calc] (Note 42, AR26 [p.250] to [p.251]). **VTC loss and +42.10 are from Note 44 and conflict with AOC-1, see below** | CORRECTED |
| 12 | Payables 63.0% overdue; MSME overdue 90.96 of 181.12; interest 0.66 unchanged | 537.57 / 852.74 = 63.0% [calc] (AR26 [p.227]). MSME 181.12 less 90.16 not due = 90.96. Note 32: payments beyond the appointed day nil, interest due 0.66 both years (AR26 [p.237]) | VERIFIED |
| 13 | Audit trail | Same (Note 41(n), AR26 [p.250]; auditor [p.112], [p.186] to [p.187]) | VERIFIED |
| 14 | Promoter 59.35% to 54.88%; 28,85,267 shares; rent 98.9%; Atlas sales 17.19 (+667%) | 3,83,30,255 less 3,54,44,988 = 28,85,267 [calc] (AR26 [p.223]). Rent: 1.56 + 1.56 + 13.06 = 16.18 of 16.36 short-term rent = 98.9% [calc] (AR26 [p.217], [p.235]). Atlas 17.19 vs 2.24 = +667% [calc] | VERIFIED |
| 15 | Debtors 164 vs 158 days; creditors 164 vs 209; inventory turnover 0.22 "not reproducible" | Days verified (Note 45, AR26 [p.181] to [p.182]). **0.22 does reproduce**: (1,282.43 less 712.00 = 570.43) / average inventory 2,575.6 = 0.2215 [calc], standalone. The numerator leaves out conversion cost, so the ratio cannot give inventory days. Conclusion "do not use" stands | CORRECTED |

Anchor check on the B02 appendix: P3-2 is resolved below. P3-7 stands: no going concern uncertainty. The consolidated policy line is Note 2.1(i), AR26 [p.196]; the Board's statement is AR26 [p.40].

## Note 44 vs AOC-1: the unexplained +42.10 is explained, and the VTC loss is not reliable
| Source | Azad VTC PAT | Azad Prime PAT | Sum | Parent |
|---|---|---|---|---|
| Form AOC-1, Board's Report (AR26 [p.47]) | +16.68 (PBT 20.87) | (2.69) | +13.99 (PBT sum +18.18) | n/a |
| Note 44 (AR26 [p.251]) | (41.97) | +13.89 | (28.08) | 1,363.71 |
| Standalone PAT (AR26 [p.122]) | n/a | n/a | n/a | 1,321.61 |

Ties that favour AOC-1 [calc]:
1. Consolidated PBT 1,873.06 less standalone 1,854.85 = 18.21, vs AOC-1 PBT sum 18.18.
2. Standalone PAT 1,321.61 + 13.99 = 1,335.60 vs consolidated 1,335.63.
3. NCI share of profit 6.86 (AR26 [p.192]) = 49% of 13.99 = 6.86. Note 44 sum (28.08) would give a negative NCI share.
4. Equity bridge: standalone total equity 15,519.78 less investment in subsidiaries 0.20 less AOC-1 subsidiary equity 5.20 (0.20 + 12.15 and 0.20 less 17.75 = 12.35 and (17.55)) less derivative reserve 225.63 = 15,288.75 vs reported 15,288.36. Gap 0.39 (AR26 [p.121], [p.191], [p.195]).

So the +42.10 in Note 44 is a reallocation between the parent and subsidiary columns. Note 44's parent column is 42.10 above the standalone PAT and its subsidiary columns are 42.07 below AOC-1. The consolidated total is unchanged. [INFERENCE]

**Still unresolved.** CARO xvii (AR26 [p.187]) says both subsidiaries had cash losses in both years. That fits Note 44 for VTC and fits AOC-1 for Prime, and fits neither for the other entity. The Chairman says "both subsidiaries ... reached EBITDA breakeven" (AR26 [p.7]); subsidiary EBITDA is NOT FOUND IN DOCUMENT. Subsidiary turnover is 104.30 + 83.07 = 187.37, 3.1% of consolidated revenue [calc]. The money at stake is small. The control signal is that three parts of one report disagree.

## 2A Accounting policy aggressiveness
| Policy | What the AR says | View |
|---|---|---|
| Revenue | Point in time on delivery, single obligation per order; services (job work) recognised when goods are sent after completion; bill-and-hold criteria listed (AR26 [p.200]). Services 1,193.62 vs 695.17 (+71.7%) (AR26 [p.229]) | Conventional. Amount on bill-and-hold NOT FOUND IN DOCUMENT |
| Depreciation | Straight line; plant and machinery 15 years vs "Schedule II" 7.5 (AR26 [p.205]) | Unproven; see rank 7 |
| Inventory | Weighted average; obsolescence provision "management's estimate"; scrap at net realisable value (AR26 [p.206]). Write-down amount NOT FOUND IN DOCUMENT | Opaque |
| Capitalisation | Borrowing cost capitalised 92.04 (23.0% of total); includes 20.20 on capital advances (AR26 [p.219], [p.231]) | Aggressive end of normal |
| ECL | Provision matrix by days past due; rates NOT FOUND IN DOCUMENT (AR26 [p.242]). Allowance 89.93 = 2.80% of gross 3,206.54 [calc] | Opaque |
| Leases | Incremental borrowing rate used; the rate is NOT FOUND IN DOCUMENT. Implied: interest 16.50 / opening liability 197.83 = 8.3% [calc] (AR26 [p.208], [p.216]) | Normal |
| Policy changes | None quantified | GREEN |
Assessment: moderate. I agree with B02's 6/10 (see reconciliation at the end of this phase).

## 2B Related-party map (consolidated, AR26 [p.233] to [p.235])
| Counterparty | FY26 (Rs Mn) | FY25 | Note |
|---|---|---|---|
| KMP pay: Rakesh 48.00, Jyoti 12.00, Malpani 7.20, Murali 16.71, CFO 5.55, CS 2.56 and 1.03 | 93.05 | n/a | 1.54% of revenue [calc] |
| Relatives' pay: Kartik 5.75, Satwik 0.92 | 6.67 | 5.35 | Two sons of the promoter |
| Sitting fees 5.56 and reimbursement 2.10 | 7.66 | 2.09 | Governance report shows fees 4.36 and reimbursement 2.11; fees differ by 1.20 (AR26 [p.66]) |
| Atlas Fasteners: sales 17.19, PPE purchase 5.31, job work 0.59 | 23.09 | 3.35 | Sales +667% |
| Atlas Fasteners receivable 23.98 (3.90) and supplier advance 10.80 | 34.78 | 16.30 | Receivable is 509 days of its FY26 sales [calc]; group is 189 |
| Rent: Agrima Logipark 13.06, Swastik 1.56, Rouland 1.56 | 16.18 | 15.16 | All promoter-linked |
| Security deposits: Swastik 4.96, Rouland 4.96, Forgen 2.00 | 11.92 | 11.92 | Interest income 0.20 each |
| Loans to subsidiaries (parent) | 196.41 | 188.88 | CARO iii; plus guarantee 50.59 (AR26 [p.115], [p.232]) |
Entity transactions ex-pay 40.38 = 0.67% of revenue [calc]. Total pay-type items 107.38 = 1.78% [calc]. No loan to promoter entities (CARO iii(f); AR26 [p.74]). BRSR (AR26 [p.92]) prints related-party sales 0.33% (FY25 4.95%) and purchases 3.34% (0%); Note 31 shows FY25 related sales of 2.24 = 0.05% of revenue, so the 4.95% is not reproducible. Value-extraction signal: none large. The Atlas receivable is the one to watch.

## 2C Contingent liabilities (AR26 [p.232])
| Item | FY26 | FY25 |
|---|---|---|
| Direct tax | 19.67 | 19.67 |
| GST | 2.13 | 13.20 |
| Customs duty (export obligation discharge pending) | 220.94 | 75.11 |
| Guarantee for subsidiary | 50.59 | 52.45 |
| Total | 293.33 | 160.43 |
293.33 is 1.92% of equity 15,288.36 and 21.96% of consolidated PAT 1,335.63 [calc]. Customs alone is 1.45% of equity and 16.5% of PAT [calc]. Neither the 25% of net worth flag nor the 100% of PAT flag is hit. History: the same notice family sat at 71.83 in FY21 and FY22, 86.24 in FY23 and 63.04 at 2023-09-30 (PRO [p.317]), waiting for norms to be fixed; it is now 220.94 and still unprovided. Capital commitments 1,182.77 vs 523.34 (AR26 [p.233]).

## 2D Receivables (AR26 [p.220] to [p.221])
Gross 3,206.54 vs 2,306.95 (+39.0%); not due 2,219.30 (69.2% vs 49.6%); under 6 months 704.94; 6 to 12 months 122.53; 1 to 2 years 130.20; 2 to 3 years 12.93; over 3 years 16.64. Over 6 months 282.30 = 8.8% (7.8%). Allowance 89.93. Terms "30 to 180 days". No unbilled dues. Foreign currency receivables 2,293.38 + 618.85 = 2,912.23 = 93.4% of net trade receivables (AR26 [p.244]) [calc]. Concentration: two customers at or above 10%. The ageing table lists every bucket as "considered good" while the note face calls the full 89.93 "credit impaired". Wording defect, not a number defect. Days: 188.7 vs 178.4 on revenue [calc].

## 2E Inventory (AR26 [p.219])
| Class | FY26 (Rs Mn) | FY25 | Growth |
|---|---|---|---|
| Raw material | 1,188.05 | 626.91 | +89.5% |
| Work in progress | 1,531.74 | 967.53 | +58.3% |
| Finished goods | 107.23 | 42.75 | +150.8% |
| Scrap inventory | 199.13 | 104.32 | +90.9% |
| Stores and spares | 264.98 | 151.50 | +74.9% |
| Total | 3,291.13 | 1,893.01 | +73.9% |
Revenue grew 31.8%. Days 199 vs 151 [calc]. **New:** scrap inventory 199.13 is 3.6 times FY26 scrap sales of 55.54 (AR26 [p.229]) [calc], while scrap sales fell 44.3% (99.64 to 55.54). The scrap build also credits the P&L through the change in inventories: scrap rose 94.81 (AR26 [p.230]). The NRV basis for scrap is not disclosed. Write-down amount NOT FOUND IN DOCUMENT.

## 2F Borrowings (AR26 [p.225] to [p.226], [p.243])
| Item | FY26 (Rs Mn) | FY25 |
|---|---|---|
| Term loans, banks | 2,738.27 | 1,672.30 |
| Term loans, financial institutions | 562.69 | 236.53 |
| Vehicle loans | 72.16 | 38.84 |
| Current maturities | 563.65 | 239.02 |
| Working capital loans (on demand) | 1,193.27 | 488.15 |
| Total debt | 4,566.39 | 2,435.82 |
| Floating / fixed | 3,501.19 / 1,065.20 | 1,398.02 / 1,037.80 |
Rates 6.3% to 14.05%. Maturity table puts all 2,809.47 of long-term debt in "1-5 years" and nothing beyond five years (AR26 [p.243]), although one equipment loan has 72 monthly instalments (AR26 [p.225]). [INFERENCE] The bucket is likely coarse. No year-wise schedule exists. Current maturities next year: 563.65, +136% on 239.02. Foreign currency borrowings: euro 900.28 and USD 107.16 (22.1% of debt) [calc]. Covenants exist; terms NOT FOUND IN DOCUMENT; "no breaches" (AR26 [p.245]). A 1% rate move is 35.01 on pre-tax profit. Pledge of promoter shares: NOT FOUND IN DOCUMENT in the AR. Inter-corporate loans given: to subsidiaries only, 196.41.

## 2G Deferred tax (AR26 [p.228], [p.246] to [p.247])
Deferred tax liability 492.02 vs 274.38. Plant and machinery timing difference 541.25 vs 325.81 explains the rise: 215.44 of the 217.71 charge. Deferred tax is 40.5% of the 537.43 tax charge [calc]. Effective rate 28.69% vs statutory 29.12% [calc]. Cash tax paid 488.17 exceeded the current tax charge 323.68 because the FY25 payable of 178.64 was settled. No MAT credit left.

## 2H Exceptional items, goodwill, ESOP, leases, events
- Exceptional items: nil in both years (AR26 [p.38]). No goodwill or intangibles on the balance sheet (AR26 [p.191]; CARO i(a)(B), AR26 [p.114]).
- ESOP: scheme approved 2025-01-28 for 11,82,259 options (1.83% of 6,45,81,743 shares [calc]); none granted to 2026-03-31 (AR26 [p.48]). Post year end, 80,000 options at Rs 1,050 granted 2026-05-12 (Note 39, AR26 [p.249]). QIP price was Rs 1,280 (AR26 [p.249]).
- Leases: right-of-use 161.13, liability 176.84 (AR26 [p.216]).
- Events after the balance sheet date: the options only. The Board's report says no material change till 2026-05-15 (AR26 [p.46]).
- Labour codes: no material impact expected (Note 45, AR26 [p.252]).

**Phase 2 summary and cross-reference.** The notes tie out on borrowings, capex, leases, gratuity, QIP use and the borrowing cost capitalised. Cross-reference to Phase 1: the one KAM (revenue cut-off) fits the Q4-heavy year; the CARO ix(d) wording is hard to square with the funding mix; CARO vii(b) customs 218.57 + 2.37 ties to Note 28.
**Reconciliation with B02 accounting score 6/10:** agree. Strengths: no restatement of any headline line, clean RPT, QIP trail, borrowing costs tie. Weak points: silence on ECL rates, hedges, covenants, write-downs, the government balance; one note (44) that disagrees with AOC-1; the unexplained scrap build.
**Phase 2 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the issues are disclosure gaps and one inconsistency of about 42 Rs Mn that nets to zero in the consolidated total.

---

# PHASE 3: FINANCIAL STATEMENTS (cash flow first)

## 3A Cash flow (consolidated, Rs Mn; AR26 [p.193] to [p.194])
| Line | FY26 | FY25 |
|---|---|---|
| Operating profit before working capital changes | 2,332.96 | 1,686.64 |
| Change in working capital | (3,034.45) | (974.82) [calc] |
| of which receivables | (736.91) | (555.78) |
| of which inventories | (1,398.12) | (563.38) |
| of which other assets | (739.76) | (252.18) |
| of which payables | 61.05 | 302.44 |
| of which other financial liabilities | (230.00) | 163.48 |
| Cash from operations | (701.49) | 711.82 |
| Tax paid | (488.17) | (175.15) |
| **CFO** | **(1,189.66)** | **536.67** |
| CFO / PAT | (0.89) [calc] | 0.62 |
| CFO / EBITDA (ex other income) | (0.53) [calc] | 0.33 |
| Capex (PPE, CWIP, capital advances) | (5,724.80) | (2,932.52) |
| **FCF (CFO less capex)** | **(6,914.46)** [calc] | **(2,395.85)** [calc] |
| Capex / depreciation | 10.8x | 9.9x |
| Deposits matured (net) | 4,795.34 | (6,229.70) |
| Long-term borrowings raised / repaid | 1,542.43 / (116.98) | 1,677.81 / (97.74) |
| Short-term borrowings, net | 705.12 | 484.15 |
| Equity raised | nil | 7,000.20 |
| Finance costs paid | (351.61) | (153.57) |
| Cash and bank (cash 245.92 + bank 1,599.99) | 1,845.91 | 6,970.27 |
| M&A spend | none | advance toward investments (19.11) |

Where the money came from: FD maturities 4,795.34 plus net borrowing 2,130.57 [calc] funded CFO (1,189.66), capex 5,724.80 and finance costs. Net cash 4,534.45 became net debt 2,720.48, a swing of 7,254.93 [calc] (AR26 [p.245]).

**CFO quality checks.**
- Interest classification flatters CFO. Interest paid (351.61) and lease interest (16.50) sit in financing; interest received 215.24 sits in investing. CFO is before both.
- No one-time inflator: the 14.00 liability write-back and 158.16 unrealised FX gain are removed from CFO.
- Payables are not being stretched. Payables rose only 61.05 and payable days fell (calc 64 to 52); BRSR shows 166 vs 255 days and the company ratio table shows 164 vs 209 on a purchases basis (AR26 [p.91], [p.182]). Three bases, one direction.
- Inventory build is the largest drag (1,398.12); other assets (739.76) include the government balance.
- Issue costs may sit inside CFO. QIB expense payable fell 136.03 to 3.00 and IPO expense payable 44.78 to nil (AR26 [p.228]), against a 22.42 credit to securities premium (AR26 [p.195]). Cash paid is about 155.39 to 177.81 [calc, INFERENCE]. Adding it back leaves CFO at (1,034.27) to (1,011.85). Still negative.
- Six-year view: OCF +47.73 (FY21), +209.39 (FY22), (102.09) (FY23) (PRO [p.359]); (69) (FY24) (AR25 [p.21]); +536.67 (FY25); (1,189.66) (FY26). The sum is about (567) Rs Mn [calc], matching B01's cumulative (56.75) Rs Cr. Cash conversion has not been clean in any growth phase.
**FLAG-CASH: raised.**

## 3B Balance sheet (consolidated, AR26 [p.191])
| Line (Rs Mn) | FY26 | FY25 | Change |
|---|---|---|---|
| PPE + ROU + CWIP | 10,360.26 | 5,158.11 | +100.9% |
| Of which CWIP | 2,566.82 | 797.80 | +221.7% |
| Capital advances (other non-current) | 1,237.18 | 1,108.04 | +11.7% |
| Inventories | 3,291.13 | 1,893.01 | +73.9% |
| Trade receivables | 3,116.61 | 2,234.80 | +39.5% |
| Cash and bank | 1,845.91 | 6,970.27 | (73.5%) |
| Other current assets | 1,576.73 | 840.28 | +87.6% |
| Total assets | 22,000.42 | 18,606.98 | +18.2% |
| Equity | 15,288.36 | 13,930.26 | +9.7% |
| Borrowings (total) | 4,566.39 | 2,435.82 | +87.5% |
| Trade payables | 852.74 | 801.08 | +6.4% |
| Deferred tax liability | 492.02 | 274.38 | +79.3% |

| Ratio | FY26 | FY25 | Note |
|---|---|---|---|
| Debt / equity | 0.30 | 0.17 | calc; company standalone 0.29 vs 0.17 (AR26 [p.32]) |
| Net debt / EBITDA | 1.21x | net cash | 2,720.48 / 2,253.13 [calc] |
| Current ratio | 3.27 | 5.20 [calc] | company standalone 3.29 vs 5.30 |
| Quick ratio | 2.18 | n/a | (9,892.99 less 3,291.13) / 3,026.71 [calc] |
| Interest cover (ex other income) | 5.60x | 7.17x | on capitalised-adjusted interest 4.31x [calc] |
| ROCE (company) | 10.7% | 8.7% | AR26 [p.32]; adjusted ROCE 15.3% vs 20.7% (AR26 [p.14], AR25 [p.21]) |
| ROE | 9.1% | n/a | PAT 1,335.63 / average equity 14,609.31 [calc] |
| Goodwill / net worth | nil | nil | no goodwill |

**DuPont (FY26) [calc].** Net margin 22.15% x asset turnover 0.30 x leverage 1.39 = 9.1%. ROE is operational: high margin and low turnover, not leverage. The low turnover comes from 3,804.00 of CWIP plus capital advances and 3,291.13 of inventory that are not yet earning.

## 3C P&L (consolidated, AR26 [p.192])
| Line (Rs Mn) | FY26 | FY25 | YoY | % of revenue FY26 / FY25 |
|---|---|---|---|---|
| Revenue | 6,029.75 | 4,573.54 | +31.8% | |
| Materials consumed | 1,304.73 | 1,049.86 | +24.3% | 21.6 / 23.0 |
| Change in inventories | (723.50) | (413.08) | | |
| Employee cost | 1,355.23 | 928.66 | +45.9% | 22.5 / 20.3 |
| Other expenses | 1,840.16 | 1,395.02 | +31.9% | 30.5 / 30.5 |
| EBITDA (ex other income) | 2,253.13 | 1,613.08 | +39.7% | 37.4 / 35.3 |
| Depreciation | 528.42 | 294.84 | +79.2% | 8.8 / 6.4 |
| EBIT (ex other income) | 1,724.71 | 1,318.24 | +30.8% | 28.6 / 28.8 |
| Other income | 456.54 | 105.91 | +331% | |
| Finance cost | 308.19 | 183.89 | +67.6% | |
| PBT | 1,873.06 | 1,240.26 | +51.0% | |
| Tax | 537.43 | 374.92 | +43.3% | 28.7% / 30.2% of PBT |
| PAT | 1,335.63 | 865.34 | +54.3% | 22.2 / 18.9 |
| EPS, basic = diluted (Rs) | 20.57 | 14.66 | +40.3% | |

- **Operating leverage test.** EBITDA margin rose 2.1 points, but depreciation took 2.4 points, so EBIT margin is flat (28.6% vs 28.8%) [calc]. The MD&A credit to "operating leverage" (AR26 [p.30]) holds at EBITDA only.
- **Other income.** 456.54 = 24.4% of PBT. Composition: FX gain 214.01 (46.9%), fixed deposit interest 225.77, other interest 2.72, write-back 14.00 (AR26 [p.229]). Other income supplied 350.63 of the 632.80 PBT increase (55.4%) [calc]. The Chairman states this openly (AR26 [p.6]).
- **EBITDA margin appears on three bases.** 37.4% consolidated (AR26 [p.18], [p.30]); 36.9% standalone "reported" (AR26 [p.15], [p.18], [p.32]); 37.2% in the KPI chart (AR26 [p.14]). FY25: 35.5%, 36.3%. I rebuilt only the consolidated one (37.37%). The others are NOT reconciled in the AR.
- Exceptional items: none, three-year pattern clean. Basic equals diluted because no option was outstanding. EPS growth (40.3%) trails PAT growth (54.3%) because the QIP raised weighted shares from 5.95 crore to 6.46 crore (AR26 [p.236]).

**Cross-reference.** Phase 1 CARO ix(d) (no short-term funds for long-term use) sits against working-capital loans +705.12 net and capex 5,724.80. Phase 2 inventory build (+1,398.12) is the same number as the cash flow drag. The 1.4% of equity that customs represents is small beside the 6,914.46 FCF gap.

**Phase 3 summary.** Profit is real and growing. Cash is not following. Capex is 10.8x depreciation, cash and bank fell by 5,124.36 [calc], and debt rose 2,130.57. The balance sheet is still sound (net debt 1.2x EBITDA; CARE A Stable, AR26 [p.73]).
**Phase 3 verdict: RED.**
**Kill switch (informational):** Based on phases so far, a human reviewer would have reason to pause and read the cash conversion evidence before any price work, because CFO is (1,189.66) Rs Mn on +31.8% revenue and FCF is (6,914.46) Rs Mn [calc]. Under the pipeline rule the run continues.

---

# PHASE 4: RISK FACTORS AND MD&A

## 4A Disclosed risks, real vs boilerplate
There is no separate risk factors section. Risk text sits in the MD&A strategic table (AR26 [p.33], [p.34]), the Outlook paragraph (AR26 [p.36]) and the BRSR material issues table (AR26 [p.86]).
| Disclosed risk | Source | Real or boilerplate |
|---|---|---|
| Qualification dependency; withdrawal by a major OEM "could not be substituted" | AR26 [p.34] | Real |
| Segment concentration: energy and oil and gas 81.5%, "concentrated among three OEMs" | AR26 [p.33] | Real |
| Working capital intensity "governs the conversion of reported profit into operating cash" | AR26 [p.33] | Real, but no number attached |
| Capital maturation lag; returns reflect the gap until FY 2026-27 | AR26 [p.33] | Real |
| Free cash flow "expected to develop only gradually" | AR26 [p.36] | Real |
| Raw material pass-through with a ±5% band absorbed by the Company | AR26 [p.34] | Real |
| Trade policy; technology progression; talent | AR26 [p.33], [p.34] | Mostly boilerplate |
| BRSR items: energy, safety, waste | AR26 [p.86] | Boilerplate |

## 4B Missing risks (evidence from Phases 1 to 3, absent from the risk text)
| Missing risk | Evidence | Likely reason for omission |
|---|---|---|
| Land title and litigation at the core campus | Tunkibollaram land 259.02 Rs Mn held on allotment; title transfer conditional on full project implementation and 50% utilisation; the agreement is "valid for a period of 3 years" from 2021-09-23, and any extension is NOT FOUND (AR26 [p.215]). Mangampet land 75.17 in CWIP under Writ Petition 18735 of 2024 (AR26 [p.218]); CARO i(c) (AR26 [p.114]). Not in Note 28 | Treated as legal, not business, risk |
| Operating cash flow and net debt swing | OCF (1,189.66) never appears in the MD&A; net cash 4,534.45 to net debt 2,720.48 is never narrated (MD&A only says debt-equity rose on new loans, AR26 [p.32]) | The Chairman states working-capital days instead (AR26 [p.7]) |
| Foreign exchange | Net long USD 21.96 Mn (24.18 less 1.09 less 1.13); 5% = 104.07 Rs Mn pre-tax; FX gain 214.01 in other income (AR26 [p.244] to [p.245], [p.229]). Hedging only "if it is beneficial and/or favourable" (AR26 [p.72]). The MD&A "Threats" list has no currency item | Natural hedge belief |
| Realisability of government balance | 1,102.51, doubled, composition NOT FOUND (AR26 [p.222]) | Seen as routine |
| Customs duty and export obligation | 220.94 vs 75.11; discharge certificates pending (AR26 [p.233]) | Seen as technical |
| Control environment | Audit trail gaps at parent and both subsidiaries (AR26 [p.250]); no anti-corruption policy yet, "in the process of formulating" (AR26 [p.91]) | Compliance, not business |
| Senior attrition | CS resigned 2025-11-28; EGM operations resigned 2025-11-08; EGM projects 2025-10-10; Business Head aero engines died 2026-02-14 (AR26 [p.68] to [p.69]) | Generic "talent" line used |
| Promoter dependence and stake sale | Promoter holds 54.88%, sold 28,85,267 shares in FY26 (AR26 [p.223]); PRO lists dependence on the promoter as a risk (PRO [p.263] onward) | Not repeated in AR |
| Subsidiary data conflict | AOC-1 vs Note 44 vs CARO xvii | Clerical |
| QIP deadline extension | 2026-03-31 to 2027-03-31 (AR26 [p.74]) | Compliance item |

## 4C MD&A deep dive
**Industry claims.** All demand claims are positive and unsourced in numbers: gas turbine order books "run ahead of installed production capacity", several-year airframe backlogs, LNG train build-out (AR26 [p.29] to [p.30]). No market size or share figure is printed in the AR26 MD&A. The only share datum is "AZAD's share of these customers' spend remains in the region of 1% to 1.50%" (AR26 [p.11]).
**External factors.** The MD&A credits demand and OEM supply constraints for growth, and credits capacity commissioning and operating leverage for margin. It blames nothing external for the cash drag; it calls working capital "structural to the business rather than a function of the year's activity" (AR26 [p.32]). That is a framing choice. The AR25 said the opposite: initiatives would deliver benefits "from FY26" (AR25 [p.21]).
**Segment view (standalone, AR26 [p.31]).**
| Segment (Rs Mn) | FY26 | FY25 | Growth | Share of revenue |
|---|---|---|---|---|
| Energy and Oil & Gas | 4,811.3 | 3,586.3 | +34.2% | 81.5% (79% in FY25, AR25 [p.21]) |
| Aerospace and Defence | 1,012.6 | 807.4 | +25.4% (FY25: +84.1%) | 17.2% (17.9%) |
| Others (scrap, incentives) | 79.9 | 135.6 | n/a | |
Diversification went backward in FY26. Oil and gas revenue was "under H100 million" (AR26 [p.23]). Order book at 2026-03-31 is about 65,000 Rs Mn (about 6,500 Rs Cr), 10.8x consolidated revenue [calc]: energy about 37,000, aerospace and defence about 18,500, oil and gas about 9,500 (AR26 [p.19], [p.21], [p.23]). AR25 order book was 6,080 Rs Cr (AR25 [p.11]). Implied new orders in FY26 are about 1,023 Rs Cr [calc: 6,500 less 6,080 plus 603 revenue], on a management estimate that is "not audited" (AR26 [p.18]).

**Guidance table**
| Claim | Number | Timeframe | Delivered / evidence | Credibility |
|---|---|---|---|---|
| Revenue growth target (AR25 [p.40]) | ~30% | FY26 | +31.8% consolidated, +30.3% standalone (AR26 [p.38]) | High |
| Revenue growth guide (AR26 [p.36]) | >25% per annum | multi-year | FY26 above it; H1 FY27 not tested here | Medium-High |
| Working capital benefits (AR25 [p.21]) | "from FY26" | FY26 | Days 244 vs 202; revenue basis 336 vs 266 (AR26 [p.7]) | Low |
| Positive OCF "driven by better collections" (AR25 [p.21]) | +629 standalone | FY25 | FY26 (1,232.63) standalone | Low |
| Energy share falls to 55 to 60% (AR26 [p.36]) | 55% to 60% | 4 to 5 years | FY26 share rose to 81.5% | Not testable yet; direction wrong |
| Dedicated facilities (AR25 [p.21]; AR26 [p.16]) | more sheds in FY26 | FY26 | GE Vernova 2025-04-29 and Siemens Energy 2025-09-18 opened | High |
| Rolls-Royce first shipments (AR26 [p.22]) | before end FY27 | FY27 | Contract signed 2024-01; still in qualification | Medium |
| Full utilisation (AR26 [p.8]) | FY 2027-28 | FY28 | MD&A: "peak utilisation anticipated over a longer horizon" (AR26 [p.31]) | Medium-Low |
| QIP objects (AR26 [p.74]) | by 2026-03-31 | FY26 | Extended to 2027-03-31; 1,563.35 of capex object unspent | Low-Medium |
| ROCE to strengthen as facilities ramp (AR25 [p.21]) | rise | FY26 | Reported 8.7% to 10.7%; adjusted 20.7% to 15.3% (AR26 [p.14]) | Mixed |

## 4D Tone and credibility (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3 | Candid on working-capital days and other income (AR26 [p.6], [p.7]). Silent on OCF, net debt swing, land title, customer names. Front matter is unaudited |
| Consistency | 3 | EBITDA margin on three bases; exports "93%" vs 91.1% outside India in Note 31 (5,495.70 / 6,029.75, AR26 [p.237]) [calc]; "dedicated" capacity vs the footprint table (6E) |
| Specificity | 4 | Order book by segment, facility dates, contract values, areas in sq m |
| Accountability | 3 | Owns the working-capital number; does not mention the AR25 promise it missed |
| Capital allocation sense | 3 | Capex tied to contracts; CWIP 3.2x; GCP 1,562.10 use undisclosed; QIP deadline extended |
Mean 3.2.

**Contradictions vs Phases 1 to 3.** MD&A "gradual normalisation" vs Chairman "principal operational task of FY 2026-27". MD&A explains current ratio fall as "utilisation of QIP proceeds towards capital expenditure" (AR26 [p.32]); true for 4,900 of FD maturities, but debt also rose 2,130.57. MD&A inventory turnover note blames "capacity additions" while the ratio excludes conversion cost.

**Phase 4 summary.** Better than average candour on working capital; the risk text still omits the cash flow, land title and currency items that Phases 1 to 3 surfaced.
**Phase 4 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the omissions are of emphasis and the main weakness is disclosed in words if not in numbers.

---

# PHASE 5: GOVERNANCE AND BOARD

## 5A Board (AR26 [p.60] to [p.61])
| Director | Role | Joined | Other directorships | Board attendance | Flag |
|---|---|---|---|---|---|
| Rakesh Chopdar | Executive Chairman and CEO, promoter | 2003-08-14 | 5 | 9 of 11 (82%) | Combined chair and CEO |
| Jyoti Chopdar | Whole-time Director, promoter spouse | 2014-07-01 | 8 | **2 of 11 (18%)** | Below 75%; at the 8-seat limit |
| Murali Krishna Bhupatiraju | Managing Director | 2025-01-03 | 0 | **7 of 11 (64%)** | Below 75%; CSR committee 0 of 2 |
| Vishnu Malpani | Whole-time Director | 2023-09-13 | 0 | 11 of 11 | 99,103 shares |
| Madhusree Vemuru | Independent | 2023-09-12 | 0 | 10 of 11 (91%) | Audit chair |
| Subba Rao Ambati | Independent | 2023-09-24 | 1 | 11 of 11 | |
| Michael Joseph Booth | Independent | 2023-09-12 | 0 | 11 of 11 | Over 75; continuation by special resolution 2025-09-30 (AR26 [p.69]) |
| Deepak Kabra | Independent | 2025-01-03 | 2 | 10 of 11 (91%) | |
Independents: 4 of 8 (50%); none over 10 years; longest tenure 2.5 years. Eleven board meetings; maximum gap under 120 days. Promoter-group cross-board memberships: Rakesh 5 and Jyoti 8 other seats are in non-listed entities ("-" in the listed column).
Housekeeping defects: Jyoti's DIN is 03132157 in the report (AR26 [p.41], [p.60]) and 03132757 in the AGM notice (AR26 [p.254]); the Risk Committee table names both Vemuru and Booth as chair (AR26 [p.67]).

## 5B Committees
Audit Committee: Vemuru (chair), Booth, Kabra, Malpani; five meetings; Vemuru 4 of 5 (AR26 [p.63]). NRC: four independents, six meetings, all present. Stakeholders' Relationship: Ambati chair with three executives; one meeting. Risk Management: four independents, two meetings (2025-05-23, 2025-12-18). CSR: Rakesh chair, Booth, Murali, Malpani; two meetings. All Board recommendations accepted. One executive sits on the Audit Committee; the committee has an independent majority. Related party approvals sit with the Audit Committee (AR26 [p.63]).

## 5C Compensation (AR26 [p.57], [p.66]; Rs Mn)
| Person | FY26 | Multiple of median (0.3) |
|---|---|---|
| Rakesh Chopdar | 48.00 (flat) | 166.34x |
| Murali Krishna Bhupatiraju | 16.71 (9.99) | 57.91x |
| Jyoti Chopdar | 12.00 | 41.58x |
| Vishnu Malpani | 7.20 | 24.96x |
| Four executive directors | 83.91 | 6.35% of standalone PAT 1,321.61 [calc] |
| Promoter family payroll (Rakesh, Jyoti, Kartik, Satwik) | 66.67 | 5.04% of PAT [calc] |
No performance-linked pay was paid (AR26 [p.66]). Proposed: Rakesh at Rs 528 lakh a year (52.8 Rs Mn, +10%) from 2026-04-01, then a five-year term from 2026-09-13 (AR26 [p.253] to [p.254]). Median remuneration flat at 0.3 while aggregate non-managerial pay rose 47.52% (AR26 [p.57]). Permanent employees 2,168 (AR26 [p.57]) vs "more than 2,500" workforce (AR26 [p.35]). ESOP: 1.83% pool; 80,000 granted after year end (0.12% of shares).

## 5D Shareholding
| Category | 2024-03-31 | 2025-03-31 | 2026-03-31 |
|---|---|---|---|
| Promoter (Rakesh) | 64.84% | 59.35% | 54.88% |
| Promoter group | n/a | 0.97% | 0.96% |
| Promoter plus group | n/a | 60.32% | 55.84% |
| Foreign portfolio | n/a | 14.23% | 14.75% |
| Mutual funds | n/a | 7.07% | 10.19% |
Anchors: AR26 [p.223], [p.71]; AR25 [p.80]. The FY25 fall (64.84% to 59.35%) is dilution: shares held stayed 3,83,30,255 while the QIP added 54,68,750 shares. **The FY26 fall is a sale:** 28,85,267 shares, 7.53% of his holding, 4.47 points of equity [calc]. Consideration, buyers and pledge status are NOT FOUND IN DOCUMENT. FII plus DII (mutual funds 10.19%, insurance 0.74%, AIF 0.33%, foreign portfolio 14.75%) = 26.01% [calc]. Top public holder: ICICI Prudential Flexicap 4.94% (AR26 [p.72]). The governance report prints resident individuals as 5.48% when 94,58,699 shares are 14.65% [calc]; a typing defect.
**FLAG-PROMOTER-PRELIM: raised** (selling against a growth narrative; no pledge evidence in the AR). Full promoter verdict belongs to B08.

## 5E Governance red-flag checklist
| Check | Result | Anchor |
|---|---|---|
| Whistle-blower complaints | None (management representation) | AR26 [p.117] |
| SEBI actions | None disclosed; secretarial audit clean | AR26 [p.55] |
| Regulatory penalty | GST orders: penalties Rs 10,38,280 and Rs 1,10,582 (about 1.15 Rs Mn [calc]); no appeal yet | AR26 [p.90] |
| RPT committee | Audit Committee approves RPTs | AR26 [p.63] |
| Auditor fee ratio | Non-audit 5.4% | AR26 [p.161] |
| CSR | Compliant, 14.01 spent | AR26 [p.51] to [p.52] |
| Section 143(12) fraud | None | AR26 [p.117] |
| Material subsidiary | None; same auditor | AR26 [p.38] |
| Anti-bribery policy | None yet; "in the process of formulating" | AR26 [p.91] |
| Controls | Audit trail gaps | AR26 [p.250] |
| Key person changes | Four senior exits in FY26 | AR26 [p.68] to [p.69] |
| Share pledge | NOT FOUND IN DOCUMENT | |

**Phase 5 summary.** Clean paper trail, executive-heavy board, thin independent tenure, two executive directors below 75% attendance, a promoter seller, and no anti-bribery policy.
**Phase 5 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because nothing shows misconduct. The promoter sale needs the shareholding file (B08) before any view on intent.

---

# PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

## 6A Narrative vs reality
| # | Claim (anchor) | What the financials show | Result |
|---|---|---|---|
| 1 | "posted record revenue and profit" (AR26 [p.6]) | Revenue 6,029.75, PAT 1,335.63; both highest | PASS |
| 2 | "our capacity is now largely in place" (AR26 [p.8]); "roughly 70% to 80% complete" (AR26 [p.7]) | CWIP 2,566.82 + capital advances 1,237.18 = 3,804.00; commitments 1,182.77; Phase 2 about 67,000 sq m not started in any statement | PASS for Phase 1 at 70% to 80%; FAIL if read as the whole programme |
| 3 | Operating leverage (AR26 [p.30], [p.8]) | EBITDA margin +2.1 points; EBIT margin 28.6% vs 28.8% | FAIL at EBIT |
| 4 | "Our cash conversion cycle is the slowest-moving number in the Company, and I will not present it as anything else" (AR26 [p.7]) | Days 244 vs 202; OCF (1,189.66) | PASS (direction candid; OCF not quoted) |
| 5 | Capex "funded substantially through our QIP proceeds" (AR26 [p.6]) | QIP capex use 3,686.65 vs two-year capex 8,657.32 = 42.6% [calc]; debt rose 2,130.57 in FY26 | FAIL ("substantially" overstated) |
| 6 | "both subsidiaries ... reached EBITDA breakeven" (AR26 [p.7]) | Not verifiable; three sources disagree on subsidiary profit | NOT VERIFIABLE |
| 7 | Exports "~93% of revenue" (AR26 [p.9]); order book "~11x" (AR26 [p.9]) | Outside India 91.1% of consolidated revenue [calc]; order book 10.8x [calc] | FAIL (export basis NOT FOUND); PASS (order book) |

## 6B Strategic priorities
Priorities named: convert qualifications into production, ramp four plants, commission the rest, normalise working capital, deepen OEM ties (AR26 [p.8]). Specific enough: yes (dates, areas, contract values). Capital allocated: Phase 1 largely funded; Phase 2 (about 67,000 sq m) has no amount (NOT FOUND). Execution evidence: two dedicated facilities opened in FY26; GTRE engine delivered 2026-07-22, "not reflected in our management revenue guidance" (AR26 [p.22]).

## 6C Metrics showcased vs absent
Showcased: record numbers, order book 11x, 1,700 qualified parts, awards, aerospace crossing 1,000 Rs Mn, wallet share 1% to 1.5%.
Conspicuously absent from the front matter: operating cash flow and free cash flow; net debt swing; reported vs adjusted ROCE fall (adjusted 20.7% to 15.3% appears only in a chart, AR26 [p.14]); top-1 customer 18.6% and the second customer above 10%; receivable ageing; the government balance; the promoter stake sale; subsidiary profit.

## 6D Tone and priority drift vs prior year
AR25 headline: "A Year of Consolidation and Forward Momentum", net cash 6,959 Rs Mn, "Operating cash flows turned positive" (AR25 [p.11], [p.21]). AR26 headline: "FY 2026-27: The Year of Conversion" (AR26 [p.8]). The emphasis moves from balance sheet strength to execution and working capital. The AR26 tone is more candid on cash conversion than AR25 was optimistic. It does not mention the net debt turn.

## 6E Quiet abandonment check
| # | Opening claim (quote) | Where it should show | Class | Materiality |
|---|---|---|---|---|
| 1 | "our capacity is now largely in place" (Chairman, AR26 [p.8]) | Footprint table (AR26 [p.12]) shows Phase 2 of about 67,000 sq m, 36.8% of the 182,000 sq m end state [calc], with no status, date or cost anywhere | (b) silent drop of Phase 2; (c) hedged retreat on "largely" | Material: capital intensity and FCF timing |
| 2 | MD&A: footprint "dedicated to specific OEM programmes" (AR26 [p.32]) | Same footprint table: existing base ~20,000 "fungible", Phase 2 ~67,000 "Fungible capacity"; 87,000 of 182,000 sq m = 47.8% not dedicated [calc] | (a) implicit retraction | Moderate: the switching-cost story covers about 52% of the area |
| 3 | "Normalising it is the principal operational task of FY 2026-27, and a fair measure to hold us to" (AR26 [p.7]) | MD&A: "structural to the business rather than a function of the year's activity" and "gradual normalisation" (AR26 [p.32]); Outlook: requirements "likely to remain structurally elevated for a sustained period" (AR26 [p.36]) | (c) hedged retreat | Material: this is the July falsifier |
| 4 | AR25: "benefits expected to accrue from FY26"; OCF "driven by profitability and better collections" (AR25 [p.21]) | AR26 cash flow and Note 7, 8 show the reverse; AR26 never refers back to the promise | (a) implicit retraction across years | Material |
| 5 | "both subsidiaries ... reached EBITDA breakeven" (AR26 [p.7]) | No subsidiary EBITDA anywhere; AOC-1, Note 44 and CARO xvii disagree | (b) silent drop of support | Low: subsidiaries are 3.1% of revenue |

**Phase 6 summary.** The letter is more candid than most. Where it claims strength (dedicated capacity, operating leverage, QIP funding), the numbers in the same AR do not fully support it.
**Phase 6 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the discrepancies are of degree and each is disclosed somewhere in the AR.

---

# PHASE 7: MULTI-STRATEGY SIGNALS

| Strategy | Call | Top reasons |
|---|---|---|
| Value + Quality | FAIL | ROCE 10.7%; CFO (1,189.66); adjusted ROCE fell to 15.3% (AR26 [p.14]). Quality of earnings: other income 24.4% of PBT |
| **GARP** | **WATCHLIST** | 1. Growth is real: revenue +31.8%, PAT +54.3%, EPS +40.3%, order book 10.8x revenue. 2. Price is not tested here (stage 11 owns valuation); context only: trailing EPS Rs 20.57 (AR26 [p.192]) vs the collector CMP Rs 2,456.0 (B00) is 119x [calc]. 3. The G rests on conversion that is not yet in cash: FCF (6,914.46), inventory +73.9%, government balance 2x. Reasonable-price test cannot pass until cash follows |
| **Turnaround** | **FAIL (not applicable)** | Not a turnaround. Margins already high (37.4% EBITDA). The transition is capacity conversion, not repair. The only repair item is working capital |
| Capex-Led Growth | WATCHLIST (best fit) | Capex 5,724.80 = 10.8x depreciation; CWIP 3.2x; contracts tied to named OEMs; but commissioning is not yet proven in revenue or cash, and the QIP deadline moved |
| Cash Flow Compounder | FAIL | CFO negative in FY26; cumulative six-year CFO about (567) Rs Mn |
| Contrarian | FAIL | No sign the name is out of favour: FII + DII 26.01%, ICICI Prudential Flexicap 4.94% |
| Insider Confidence | FAIL | Promoter sold 4.47 points; ESOP first grant 80,000 options; no insider buying evidence in the AR |
| Guidance Divergence | WATCHLIST | Revenue guidance delivered; working-capital and cash guidance diverged |

GARP detail. Reasons to keep it on the list: demand backlog is large and contracted (MHI 13,870 Rs Mn over five years, GE Steam Power about USD 53.5 Mn, AR26 [p.16]); EBITDA margin 37.4%; leverage is low (1.21x). Reasons it is not a PASS: the three AR numbers that matter for conversion (OCF, working-capital days, government balance) all moved the wrong way in the same year; the AR gives no quantified path for them; and the one repeatable cash promise (AR25) was missed.
Turnaround detail. The pipeline's turnaround lens would need a broken business to repair. The AR shows an operating business with a stressed cash cycle, so the call is "not applicable" rather than a negative judgment.

---

# PHASE 8: FINAL VERDICT DASHBOARD

## Snapshot
Azad Engineering Ltd. Precision airfoils and critical components for energy turbines, aerospace and defence, oil and gas. Consolidated FY26: revenue 6,029.75 Rs Mn (+31.8%), EBITDA ex other income 2,253.13 (37.4%), PAT 1,335.63 (+54.3%), CFO (1,189.66), FCF (6,914.46) [calc], net debt 2,720.48, equity 15,288.36. Order book about 65,000 Rs Mn. Exports about 91% to 93%. Promoter 54.88%.

## Phase verdicts
| Phase | Verdict | One-line reason |
|---|---|---|
| 1 Auditor and CARO | YELLOW | Unmodified; audit trail reservation; CARO remarks at parent and subsidiaries |
| 2 Notes | YELLOW | 9 of 15 clean, 6 corrected; Note 44 vs AOC-1 conflict |
| 3 Financials | RED | CFO (1,189.66); FCF (6,914.46); net cash to net debt |
| 4 MD&A | YELLOW | Candid on working capital; omits cash flow, land title, FX |
| 5 Governance | YELLOW | Promoter sale; attendance; no anti-bribery policy |
| 6 Front matter | YELLOW | Three claims fail the numbers test; five withdrawals |
| 7 Strategy | Best fit: Capex-Led Growth, WATCHLIST | |

## Quality score /10 (four components at 25% each)
| Component | Score | Basis |
|---|---|---|
| Governance | 5.5 | Clean CARO fraud and whistle-blower answers, adequate IFC, RPT small; offset by promoter sale, executive-heavy board with short independent tenure, two directors below 75% attendance, audit trail and anti-bribery gaps |
| Accounting quality | 6.0 | Agree with B02; policies ordinary, silence on ECL, hedges, write-downs; Note 44 conflict |
| Balance sheet | 6.0 | Net debt 1.21x EBITDA, current ratio 3.27, CARE A Stable; but net cash became net debt in one year, 76.7% floating, interest cover 5.6x |
| Earnings quality | 4.5 | CFO/PAT (0.89); other income 24.4% of PBT; EBIT margin flat; unrealised FX gain 158.16; ROCE 10.7% |
| **Overall** | **5.5 / 10** | |

## Top 3 strengths
1. Contracted demand and growth delivered: revenue +31.8%, guidance of about 30% met, order book about 65,000 Rs Mn or 10.8x revenue (AR26 [p.38], [p.15]).
2. Clean statutory record: unmodified opinion, no going concern language, no related-party loans, CSR fully spent, adequate IFC (AR26 [p.109], [p.118], [p.119]).
3. Balance sheet capacity: equity 15,288.36 Rs Mn, net debt 1.21x EBITDA, CARE A Stable (AR26 [p.191], [p.73]).

## Top 3 red flags
1. Cash conversion: CFO (1,189.66), FCF (6,914.46) [calc], working-capital days 244 vs 202, inventory +73.9%, government balance 1,102.51 (AR26 [p.193], [p.7], [p.219], [p.222]).
2. Earnings quality and returns: other income 24.4% of PBT, EBIT margin flat, ROCE 10.7%, adjusted ROCE 15.3% vs 20.7% (AR26 [p.192], [p.14]).
3. Disclosure and ownership integrity: Note 44 vs AOC-1 vs CARO xvii; promoter sold 28,85,267 shares; core-campus land held on allotment and Mangampet land under a High Court writ (AR26 [p.251], [p.47], [p.223], [p.215], [p.218]).

## Key monitorables
| Metric | Threshold | Where | Why |
|---|---|---|---|
| Consolidated OCF | Positive for FY27; H1 FY27 was (436.24) Rs Mn per B01 | Q3 and Q4 FY27 cash flow statements; AR27 | July falsifier |
| Company working-capital days | Below 202 (FY25) then toward management target; same definition each time | Concall and AR27 letter | 244 vs 202; definition NOT FOUND, so ask for it |
| Inventory growth vs revenue growth | Inventory growth below revenue growth | Balance sheet, Note 7 | +73.9% vs +31.8% |
| Government balance | Below 1,102.51 and composition disclosed | Note 10 | Doubled, 66.7 days of revenue |
| Top customer share | Under 20%; top-5 under 65% | Note 34 | 18.64%; 47.02% |
| QIP capex object | 1,563.35 spent by 2027-03-31 | Monitoring agency reports; Note 40 | Deadline was extended once |
| CWIP transfers | CWIP 2,566.82 falls as plant is capitalised | Note 4; Q results | Commissioning proof |
| Receivables over 1 year and allowance cover | Cover at or above 100% (now 56.3%) | Note 8 | Old bucket 2.46x |
| Promoter holding and pledge | No further sale; pledge nil | Shareholding pattern | 59.35% to 54.88% |
| Net debt and interest cover | Cover at or above 5.6x; floating share not rising | Notes 13, 14, 34 | Leverage with negative OCF |
| Subsidiary profit | One agreed figure in AOC-1 and Note 44 | Next AR | 42 Rs Mn conflict |
| Other income share of PBT | Falling from 24.4% | Note 22 | Quality of growth |

## One-line verdict
Revenue and orders are strong and cash conversion is not: best fit is Capex-Led Growth on WATCHLIST until operating cash flow turns positive and the cash numbers are reconciled.

```yaml
stage: B03-ardeep
company: "AZAD"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "QIP placement document (2025) not collected; Note 40 and the Corporate Governance Report (AR26 [page 74]) read against the AR only (carried from B00 and B02)."
  - "Five screener formula sheets absent; research/ empty (carried from B00). No effect on anchored AR evidence."
  - "Definition of the company working-capital days figure (244 at FY26, 202 at FY25, Chairman letter AR26 [page 7]) NOT FOUND IN DOCUMENT. The July tripwire 344 has no stated basis in the AR, so the two are not comparable. B02 said the AR prints no working-capital days; corrected here."
  - "Promoter pledge status and the consideration for the 28,85,267 shares the promoter sold in FY26: NOT FOUND IN DOCUMENT. Belongs to the shareholding file and B08."
  - "Composition and age of balance with government authorities 1,102.51 Rs Mn: NOT FOUND IN DOCUMENT."
  - "ECL provision matrix rates, inventory write-down amount, hedge contracts, covenant terms, lease incremental borrowing rate: NOT FOUND IN DOCUMENT."
  - "Use of the 1,562.10 Rs Mn general corporate purposes bucket of the QIP; any extension of the Tuniki Bollaram land agreement (3-year validity from 2021-09-23); names of the two customers at or above 10% of revenue: NOT FOUND IN DOCUMENT."
  - "Reconciliation of Azad VTC and Azad Prime profit between AOC-1 (AR26 [page 47]), Note 44 (AR26 [page 251]) and CARO xvii (AR26 [page 187]): NOT FOUND IN DOCUMENT."
  - "Schedule II useful life for plant and machinery is printed as 7.5 years in the AR policy table (AR26 [page 205]); not verified against the Act in this container. PENDING LIVE VERIFICATION."
flags:
  - {type: FLAG-CASH, reason: "Consolidated OCF (1,189.66) Rs Mn vs 536.67 on revenue +31.8% (AR26 [page 193]); standalone (1,232.63) vs 628.85 (AR26 [page 123]). FCF (6,914.46) Rs Mn calc. Inventory +73.9%, receivables +39.5%, government balance 1,102.51 vs 554.83. Company working-capital days 244 vs 202 (AR26 [page 7]). No factoring, discounting or recourse wording in the AR. CFO is stated before interest paid 351.61 and before interest received 215.24. Adding back possible QIP issue costs of 155.39 to 177.81 still leaves CFO negative."}
  - {type: FLAG-PROMOTER-PRELIM, reason: "Promoter Rakesh Chopdar 59.35% to 54.88%: 3,83,30,255 to 3,54,44,988 shares, 28,85,267 sold in FY26 (Note 11(v), AR26 [page 223]); 64.84% at 2024-03-31. Promoter plus group 60.32% to 55.84% (AR26 [page 71]; AR25 [page 80]). Pledge and sale consideration NOT FOUND IN DOCUMENT. Full promoter verdict from B08."}
phase_verdicts: {p1: "YELLOW: unmodified opinion; one KAM (revenue cut-off); books reservation for audit trail; CARO i(c), vii(a), vii(b), x(b) at parent and vii(a), xvii at both subsidiaries; no going concern language", p2: "YELLOW: B02 6/10 confirmed; 9 of 15 top findings clean, 6 corrected; Note 44 conflicts with AOC-1", p3: "RED: CFO (1,189.66) Rs Mn; FCF (6,914.46) calc; net cash 4,534.45 to net debt 2,720.48; ROCE 10.7%", p4: "YELLOW: candid on working capital and other income; MD&A omits CFO, land title, FX and the net debt swing; EBITDA margin on three bases", p5: "YELLOW: promoter sold 4.47 points; two executive directors under 75% attendance; anti-bribery policy not yet formulated; clean fraud and whistle-blower answers", p6: "YELLOW: three claims fail the numbers test (dedicated capacity, operating leverage at EBIT, QIP-funded capex); five withdrawals or hedged retreats", p7_best_fit: "Capex-Led Growth: WATCHLIST"}
overall_quality: 5.5
quality_components: {governance: 5.5, accounting: 6.0, balance_sheet: 6.0, earnings: 4.5}
kill_switch_notes:
  - "P2 informational: Note 44 subsidiary split disagrees with AOC-1 and CARO xvii; about 42 Rs Mn reallocation that nets to zero in the consolidated total. A reviewer would not stop."
  - "P3 informational: a reviewer would have reason to pause on cash conversion before price work, because CFO is (1,189.66) Rs Mn and FCF (6,914.46) Rs Mn calc on +31.8% revenue. The run continues."
  - "P5 informational: promoter sold 28,85,267 shares in FY26; pledge unknown. A reviewer would not stop, but B08 must resolve it."
triple_pass_verification:
  verified: 9
  discrepancies:
    - {finding_rank: 4, triple_pass_value: "top-5 41.3% to 47.0%", ar_value: "47.0% reproduces (1,123.97 + 1,711.10 = 2,835.07 on 6,029.75 Rs Mn). 41.3% reproduces only as top-1 plus 4/5 of 1,711.10, an equal-split assumption. B01 reading of 28.4% is excluded because two customers at 10% or more need at least 1,726.95", note_ref: "Note 34 AR26 [page 242]; Note 31(c) [page 237]; AR25 [page 238]"}
    - {finding_rank: 7, triple_pass_value: "76.6% plant share cited to Note 6; no technical evaluation disclosed; 15 vs 7.5 years flagged as double statutory", ar_value: "76.6% is Note 3(a) (6,885.05 of 8,991.30 Rs Mn); policy says lives rest on technical evaluation, report not disclosed; Schedule II 7.5 column unverified, PENDING LIVE VERIFICATION", note_ref: "AR26 [page 214]; [page 205]; Note 6 [page 219]"}
    - {finding_rank: 8, triple_pass_value: "credit loss charge 17.78", ar_value: "17.78 in Notes 8 and 34; 17.87 in Note 27 and the cash flow statement", note_ref: "AR26 [page 221]; [page 242]; [page 232]; [page 193]"}
    - {finding_rank: 9, triple_pass_value: "5% rupee move costs 104.04", ar_value: "104.07 on the USD line; EUR line (14.39) offsets; net 89.68 calc", note_ref: "Note 34 AR26 [page 245]"}
    - {finding_rank: 11, triple_pass_value: "VTC loss (41.97), Prime +13.89, consolidation adjustment +42.10", ar_value: "AOC-1 prints VTC PAT +16.68 and Prime (2.69); NCI profit 6.86 = 49% of 13.99; PBT and equity bridges tie to AOC-1; Note 44 is a reallocation of about 42 between parent and subsidiary columns", note_ref: "AR26 [page 47]; Note 44 [page 251]; [page 192]; [page 187]"}
    - {finding_rank: 15, triple_pass_value: "inventory turnover 0.22 not reproducible", ar_value: "0.2215 reproduces as (1,282.43 less 712.00) over average inventory 2,575.6 standalone; numerator omits conversion cost so it cannot give inventory days", note_ref: "Note 45 AR26 [page 181]; MD&A [page 32]; standalone P&L [page 122]"}
missing_risks:
  - "Land title at the core campus: Tunkibollaram land 259.02 Rs Mn on allotment with conditional title and a 3-year agreement from 2021-09-23 (AR26 [page 215]); Mangampet land 75.17 in CWIP under Writ Petition 18735 of 2024 (AR26 [page 218]); CARO i(c) (AR26 [page 114]). Absent from MD&A risk text (AR26 [page 33], [page 34], [page 36])."
  - "Operating cash flow (1,189.66) Rs Mn and the swing from net cash 4,534.45 to net debt 2,720.48 never stated in the MD&A (AR26 [page 32], [page 36], [page 245])."
  - "Foreign exchange: net long USD 21.96 Mn open, 5% = 104.07 Rs Mn pre-tax, FX gain 214.01 in other income, hedging only if beneficial (AR26 [page 245], [page 229], [page 72]); no currency item in MD&A threats (AR26 [page 34])."
  - "Government balance 1,102.51 Rs Mn doubled with composition not disclosed (AR26 [page 222])."
  - "Customs and export obligation demand 220.94 vs 75.11 Rs Mn, same issue open since FY21 (AR26 [page 233]; PRO [page 317])."
  - "Control environment: audit trail gaps at parent and both subsidiaries (AR26 [page 250]); no anti-corruption policy yet (AR26 [page 91])."
  - "Senior attrition: Company Secretary, two EGMs and the aero engines business head left in FY26 (AR26 [page 68], [page 69])."
  - "Promoter stake sale of 28,85,267 shares with pledge unknown (AR26 [page 223])."
  - "QIP objects deadline extended from 2026-03-31 to 2027-03-31 with 1,563.35 Rs Mn of the capex object unspent (AR26 [page 74])."
guidance_table:
  - {claim: "Revenue growth target for FY26 (AR25 [page 40])", number: "~30%", timeframe: "FY26", credibility: "High: delivered +31.8% consolidated, +30.3% standalone (AR26 [page 38])"}
  - {claim: "Sustained revenue growth (AR26 [page 36])", number: "above 25% per annum", timeframe: "multi-year", credibility: "Medium-High: FY26 above it; later periods not tested here"}
  - {claim: "Working capital efficiency benefits (AR25 [page 21])", number: "from FY26", timeframe: "FY26", credibility: "Low: days 244 vs 202 (AR26 [page 7]); revenue basis 336 vs 266"}
  - {claim: "Positive OCF from better collections (AR25 [page 21])", number: "629 Rs Mn standalone FY25", timeframe: "FY25 onward", credibility: "Low: FY26 standalone OCF (1,232.63) Rs Mn"}
  - {claim: "Energy share to 55% to 60% of revenue (AR26 [page 36])", number: "55% to 60%", timeframe: "4 to 5 years", credibility: "Not testable; FY26 share rose to 81.5% from 79%"}
  - {claim: "Full utilisation of dedicated plants (AR26 [page 8])", number: "full utilisation", timeframe: "FY 2027-28", credibility: "Medium-Low: MD&A says peak utilisation over a longer horizon (AR26 [page 31])"}
  - {claim: "Rolls-Royce first shipments (AR26 [page 22])", number: "before end of FY27", timeframe: "FY27", credibility: "Medium: contract January 2024, still in qualification"}
  - {claim: "QIP objects completed (AR26 [page 74])", number: "5,250.00 Rs Mn capex object by 2026-03-31", timeframe: "FY26", credibility: "Low-Medium: 3,686.65 used; deadline moved to 2027-03-31"}
  - {claim: "Return ratios to strengthen as facilities ramp (AR25 [page 21])", number: "ROCE up", timeframe: "FY26", credibility: "Mixed: reported 8.7% to 10.7%; adjusted 20.7% to 15.3% (AR26 [page 14])"}
monitorables:
  - {metric: "Consolidated operating cash flow", threshold: "Positive for FY27; H1 FY27 was (436.24) Rs Mn per B01", where: "Q3 and Q4 FY27 cash flow statements; AR27", why: "July falsifier; FY26 was (1,189.66) Rs Mn"}
  - {metric: "Company working-capital days", threshold: "Below 202 (FY25 level), same definition each print; definition requested", where: "Concall and AR27 Chairman letter", why: "244 vs 202; definition NOT FOUND"}
  - {metric: "Inventory growth vs revenue growth", threshold: "Inventory growth below revenue growth", where: "Balance sheet and Note 7", why: "+73.9% vs +31.8%"}
  - {metric: "Balance with government authorities", threshold: "Below 1,102.51 Rs Mn with composition disclosed", where: "Note 10", why: "Doubled; 66.7 days of revenue"}
  - {metric: "Top customer and top-5 share of revenue", threshold: "Top-1 under 20%; top-5 under 65%", where: "Note 34 customer lines", why: "18.64% and 47.02% now; top-1 up 4.45 points"}
  - {metric: "QIP capex object spent", threshold: "1,563.35 Rs Mn spent by 2027-03-31", where: "Monitoring agency reports; Note 40", why: "Deadline already extended once"}
  - {metric: "CWIP and capitalisation", threshold: "CWIP 2,566.82 Rs Mn falls as plant is capitalised", where: "Note 4; quarterly results", why: "Commissioning proof"}
  - {metric: "Receivables over one year and allowance cover", threshold: "Cover at or above 100% (now 56.3%)", where: "Note 8", why: "Old bucket 159.77 vs 64.94 Rs Mn"}
  - {metric: "Promoter holding and pledge", threshold: "No further sale; pledge nil", where: "Quarterly shareholding pattern", why: "59.35% to 54.88%"}
  - {metric: "Net debt and interest cover", threshold: "Cover at or above 5.6x; floating share not above 76.7%", where: "Notes 13, 14, 34", why: "Leverage with negative OCF"}
  - {metric: "Subsidiary profit", threshold: "One agreed figure in AOC-1 and Note 44", where: "Next AR", why: "About 42 Rs Mn conflict"}
  - {metric: "Other income share of PBT", threshold: "Below 24.4%", where: "Note 22", why: "FX and treasury income carry profit growth"}
ar_new_downstream_entities:
  - {name: "Safran Aircraft Engines", where_in_ar: "AR26 [page 7], [page 16], [page 22]; MOU for critical rotating airfoils for strategic defence platforms", entity_type: "aero engine OEM, customer prospect (first named in AR26 vs AR25)"}
  - {name: "Pratt & Whitney Canada", where_in_ar: "AR26 [page 16], [page 22]; Master Terms Agreement and Purchase Agreement, December 2025", entity_type: "aero engine OEM, customer contract"}
  - {name: "GE Steam Power GmbH (GE Vernova Power, Switzerland)", where_in_ar: "AR26 [page 16]; long-term supply agreement about USD 53.5 million", entity_type: "customer contract counterparty"}
  - {name: "Nuovo Pignone S.r.l. (Baker Hughes company)", where_in_ar: "AR26 [page 16]; amended strategic supply agreement through 2030", entity_type: "customer contract counterparty"}
  - {name: "Arabelle Solutions (EDF group)", where_in_ar: "AR26 [page 7], [page 20], [page 31]; nuclear turbine airfoil qualification", entity_type: "customer, qualification"}
  - {name: "Hindustan Aeronautics, Mahindra Aerospace, Tata Advanced Systems", where_in_ar: "AR26 [page 22]; domestic aerospace and defence customers", entity_type: "domestic customers named for the first time"}
strengths_top3:
  - "Contracted demand and growth delivered: revenue +31.8%, ~30% target met, order book about 65,000 Rs Mn or 10.8x revenue (AR26 [page 38], [page 15])."
  - "Clean statutory record: unmodified opinion, no going concern language, no related-party loans, CSR fully spent, adequate IFC (AR26 [page 109], [page 118], [page 119])."
  - "Balance sheet capacity: equity 15,288.36 Rs Mn, net debt 1.21x EBITDA calc, CARE A Stable (AR26 [page 191], [page 73])."
red_flags_top3:
  - "Cash conversion: CFO (1,189.66) Rs Mn, FCF (6,914.46) calc, working-capital days 244 vs 202, inventory +73.9%, government balance 1,102.51 (AR26 [page 193], [page 7], [page 219], [page 222])."
  - "Earnings quality and returns: other income 24.4% of PBT, EBIT margin flat at 28.6%, ROCE 10.7%, adjusted ROCE 15.3% vs 20.7% (AR26 [page 192], [page 14])."
  - "Disclosure and ownership integrity: Note 44 vs AOC-1 vs CARO xvii; promoter sold 28,85,267 shares; core-campus land on allotment and Mangampet land under a High Court writ (AR26 [page 251], [page 47], [page 223], [page 215], [page 218])."
best_fit_strategy: "Capex-Led Growth (WATCHLIST)"
one_line_verdict: "Revenue and orders are strong and cash conversion is not: Capex-Led Growth on WATCHLIST until operating cash flow turns positive and the subsidiary and cash numbers are reconciled."
analyst_note: "Three things a later stage cannot rebuild from the fields. First, the AR does print company working-capital days: 244 (FY26) vs 202 (FY25), Chairman letter AR26 [page 7]; B02 said it did not. The July 344 is on another basis, so the tripwire cannot be tested from the AR. Second, AOC-1 (AR26 [page 47]) ties to the consolidated statements (PBT +18.18 vs +18.21, PAT sum 13.99, NCI profit 6.86 = 49% of 13.99, equity bridge within 0.39 Rs Mn); Note 44 does not. Treat the VTC loss of 41.97 in B02 as unreliable. CARO xvii on both subsidiaries still conflicts with AOC-1. Third, top-5 concentration is 47.0% calc; B02's 41.3% is an equal-split assumption. Cash facts stand: CFO (1,189.66), FCF (6,914.46) calc, no factoring wording. Promoter sold 28,85,267 shares in FY26; pledge and price NOT FOUND."
```


---
ERRATA / ANCHOR CAVEATS (appended by the orchestrator 2026-11-15 from the stage's own hand-back; the stage has no edit tool):
1. The delivered growth anchor "AR26 [page 38]" covers the standalone 30.35% only; the consolidated 31.84% is on [page 39].
2. Phase 5E material-subsidiary statement: [page 39], not [p.38].
3. Industry claims cited as AR26 [p.29] to [p.30] run from [page 28].
4. The oil-and-gas "under ... 100 million" quote is on [p.19]; [p.23] carries different wording.
5. The Prospectus promoter-dependence risk is cited as PRO [p.263] onward; the risk factor is on printed page 28 and its PDF page was not located.
6. KPI chart values (adjusted ROCE 15.3% versus 20.7%; EBITDA margins 37.2% and 36.3%) come from a garbled extraction line on AR26 [page 14]. FY25 adjusted ROCE 20.7% is confirmed by AR25 [page 21]; the FY26 figures need a visual check on the PDF.
7. The Schedule II useful life for plant and machinery (7.5 years as printed in the AR) is not verified against the Act: PENDING LIVE VERIFICATION. The "15 vs 7.5" flag is unproven.
8. The "first named in AR26" entity list rests on a text search of AR25 only; the Prospectus was not checked for those names.
9. The report uses the text labels GREEN, YELLOW and RED.
