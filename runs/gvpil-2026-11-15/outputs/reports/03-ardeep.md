# Stage 3: Annual Report Deep Dive (backward read), GE Power India Ltd (GVPIL)
Run date: 2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.txt (AR26, FY2025-26, 332 pages) with Annual_Report_2025.txt (AR25) for comparison.

## Conventions
- UNIT: INR million ("INR M") as printed on the face of every statement ("All amounts in H million", AR26 p.131). Nothing is converted silently. Where the Step-1 brief uses Rs crore, I convert once and label it: 1 Rs crore = INR M 10.
- "p.N" is the "[page N]" marker in AR26. Printed folio = marker minus 3. "L N" is a line in the text file. "(calc)" is my arithmetic on anchored inputs. "(inference)" is my reading, not a filed statement. Note citations follow the AR26 standalone note numbers.
- Ratings: 🟢 clean, 🟡 watch, 🔴 red flag. Kill switches are informational only; the run continues.
- Reading order follows the protocol: auditor's report, notes (verified from stage 2), financial statements (cash flow first), MD&A and risks, governance and board, Directors' Report and front matter last. There is no Chairman's letter in this AR. The Directors' Report p.15 to 32 and the MD&A p.88 to 95 stand in for it.

---
## STEP 0: LOAD-BEARING FACTS FROM companies/GVPIL.md, CHECKED FIRST AGAINST THE AR

| # | Brief lead (Step-1, unverified) | What AR26 settles | Anchor | Status |
|---|---|---|---|---|
| 1a | Core services backlog Rs 1,218 cr (= INR M 12,180, calc) at Mar 2026 | NOT FOUND IN DOCUMENT. The AR gives only total remaining performance obligation (RPO) INR M 16,278 (Mar-26) against INR M 26,623 (Mar-25), down 38.9% (calc). No core services split. If the INR M 12,180 is right it is 74.8% of RPO (calc, inference). Do not confuse it with INR M 1,218.6 in Note 34 (PF trust "liabilities assumed/(settled)"). That is a different item and a coincidence of digits. | Note 27 p.166 (L 11651); Note 34 p.173 (L 12035); chart p.13 | Not settled by AR; total RPO verified |
| 1b | FY27 guidance: 85-90% execution of core backlog, 11% normalised EBITDA margin | NOT FOUND IN DOCUMENT. The AR has no numeric FY27 guidance of any kind. Forward text is qualitative only ("healthy order backlog", "improving margins", "continued growth in core services", "measured approach to FGD equipment supply (EP) rather than full EPC"). | Directors' Report p.18 (L 617-641); MD&A p.91-92 | Guidance table in Phase 4 |
| 1c | Q1 FY27 margin 14.5%, Q2 FY27 9.8% | Out of AR scope (AR is dated 18 July 2026 and covers FY26). The Q1 and Q2 FY27 filings are not in this stage's input. | cover letter p.1 | Cannot test here |
| 2a | Royalty and trademark fee Rs 13.21 cr FY25; FY26 NOT FOUND | RESOLVED. Rs 13.21 cr = INR M 132.1 = the FY25 royalty line as first printed in AR25 (AR25 Note 33, L 12643). AR26 re-presents FY25 at INR M 121.5. FY26 P&L line is INR M 125.7. The related-party table shows INR M 435.7 for FY26 (305.1 + 110.1 + 20.5). Stage 2 said the brief figure "ties to neither"; it ties to the AR25 original. | Note 33 p.168 (L 11755); Note 36 p.180 (L 12383-12393); AR25 L 12643 | Verified; gap INR M 310.0 stays open |
| 2b | Gas sale Rs 43.86 cr and hydro sale Re 1 to GE Vernova entities | VERIFIED. Gas Power business sold for INR M 438.6 (= Rs 43.86 cr) to GE Renewable Energy Technologies Pvt Ltd; Hydro business sold for INR 1 to GE Vernova Hydro Power India Pvt Ltd. Both closed in FY25 (30 Sep 2024; 31 Mar 2025). Hydro net liability INR M 2,978.9, fair value negative INR M 609.0, gain INR M 2,369.9 booked to FY25 P&L, difference to capital reserve INR M 609.0. | Note 47(i),(ii) p.194 (L 13189-13220); Note 36 p.180 (L 12375-12377); equity statement p.135 | Verified; closed FY25 events |
| 2c | INR M 4,500.0 inter-corporate loan and its Notice resolution | VERIFIED and sharpened. See Phase 2 and Phase 5E. Loan is to LM Wind Power Blades (India) Pvt Ltd (cash-pool header), repayable on demand, 5.49% to 6.35%. Notes and CARO call it UNSECURED. The Notice (dated 19 June 2026) says it is "secured through Parent Corporate Guarantee from GE Vernova Inc." and asks members to approve a new INR M 10,000 guarantee "to the Company". AGM Items 8 (s.186 cap INR M 4,500 to INR M 10,000, special resolution), 9 (LM Wind MRPT: borrow 3,000, lend 10,000) and 10 (GE Vernova Inc: bank guarantee 16,000, cash-pool guarantee 10,000, shared services 250). | Balance sheet p.131; Note 16 p.158 (L 11267, 11289-11296); Note 36 p.181 (L 12471); CARO iii(a) p.128 (L 8616-8625); Notice p.290-293, p.317, p.320-321 | Verified |
| 2d | Durgapur demerger share swap to JSW Energy | VERIFIED. Ratio 10 JSW shares of INR 10 for every 139 GVPIL shares, per valuation report and fairness opinion; appointed date 1 July 2025; held for sale from 18 Sep 2025; completion expected within 12 months of year end. JSW gives shares to GVPIL holders. GVPIL receives no cash (inference from the text). Durgapur net liabilities INR M 548.7 leave with it. Value of the JSW shares to be received: NOT FOUND IN DOCUMENT. | Directors' Report p.28 (L 1445-1456); Note 47(iii) p.194 (L 13221-13228); Note 47(v) p.195 (L 13286) | Verified; consideration value NOT FOUND |
| 3 | One-offs in FY26 profit (provision write-backs, FGD settlements, 27.0% vs 11% margin) | VERIFIED in the notes. ECL reversal INR M (1,016.6) inside Other expenses; liabilities written back INR M 240.9; insurance claim INR M 184.2; JPVL FGD settlement INR M 250 received (project costs to 30 Sep 2025 charged, collection recognised as revenue; net effect NOT STATED); BHEL settlement cash INR M 3,430.6 against INR M 3,400 agreed. Reported "margin 27.0%" = PBITDA INR M 3,740.8 / total income INR M 13,839.1 (calc). On revenue it is 29.5% (calc). Core margin ex all other income and ex the ECL reversal is 12.4% (calc, matches stage 2). | Note 28 p.167; Note 33 p.168; Note 53-54 p.202; Directors' Report p.16 | Verified |
| 4 | Two customers 34.8% FY25; FY26? CFO INR M 469 cr vs PAT 253 cr; net cash Rs 880 cr | Top two customers 38.6% of FY26 revenue (34.8% FY25). Names NOT DISCLOSED. CFO INR M 4,692.5 (= Rs 469.25 cr, calc), PAT INR M 2,363.6 (= Rs 236.4 cr; the brief's 253 cr does not tie to total PAT; continuing PAT is INR M 3,061.0). Net cash: cash INR M 4,244.6 + bank INR M 58.5 + ICD INR M 4,500.0 - fund-based draw INR M 330.0 = INR M 8,473.1 (= Rs 847.3 cr, calc). The brief's Rs 880 cr (INR M 8,800) matches cash + ICD with no debt deducted (INR M 8,803.1, calc). CFO is a working-capital release (receivables +5,136.0 less customer advances and billing in excess down). | Note 35 p.176 (L 12199); cash flow p.133; balance sheet p.131; Notice p.320 | Verified |

---
## PHASE 1: AUDITOR'S REPORT AND CARO

**1A Core opinion.** Unmodified opinion on standalone statements (p.122, L 8017-8027) and on consolidated statements (p.206, L 13924-13935). Basis: Standards on Auditing; independence stated. Internal financial controls: unmodified opinion that controls are adequate and operating effectively (Annexure A p.127, L 8516-8527). Going concern: no "material uncertainty" paragraph. The only going-concern text is CARO clause (xix): "nothing has come to our attention, which causes us to believe that any material uncertainty exists" for liabilities falling due within one year, with the standard disclaimer "this is not an assurance as to the future viability" (p.130, L 8830-8848). Directors' Responsibility Statement confirms going-concern basis (p.27, L 1327). Audit trail: unmodified (p.125, L 8379-8391); Note 57 p.203 says the employee-database software audit trail is not covered by an independent SOC report (L 13807-13810).

**1B Key Audit Matters (one, standalone and consolidated)**

| # | Subject | Why key | How addressed | Risk | Anchor |
|---|---|---|---|---|---|
| 1 | Revenue recognition, over-time contracts, total estimated cost and cost to complete | Management judgement on cost to complete drives percentage of completion; over-time revenue is INR M 7,640.3 = 60.2% of revenue (calc; FY25 INR M 6,215.2 = 59.4%) | Tested controls over cost estimate review; re-performed percentage-of-completion; compared estimated and actual cost; read "Project Management Review" for contracts with margin change | 🟡 | p.122-123 (L 8057-8110); Note 29 and 35 |

Observations (mine, not the auditor's):
- The KAM text is word-for-word the same as AR25 (AR25 L 9361-9411). Two business carve-outs, a Durgapur held-for-sale reclassification, a INR M 1,320.0 swing in the loss allowance and a INR M 4,500.0 related-party loan changed the year. The KAM set did not change.
- No KAM covers the INR M 1,016.6 receivable-allowance reversal (Note 33, Note 53). It is the single largest P&L swing and sits inside operating profit. No KAM covers the INR M 4,500.0 loan, the held-for-sale and discontinued presentation of Durgapur (INR M 344.0 assets, INR M 892.7 liabilities), or the common-control carve-out gains of FY25.
- Revenue from prior-period estimate changes: +INR M 70.3 in FY26 against INR M (501.0) in FY25 (Note 27 p.162). The swing of INR M 571.3 (calc) is the cost-to-complete judgement that the KAM covers. It is 0.6% of FY26 revenue (calc) and 4.8% of FY25 revenue (calc).

**1C Emphasis of Matter and Other Matters.** NONE in either report. "Other information" paragraph says nothing to report (p.123, L 8111-8133).

**1D CARO 2020, clause by clause (Annexure B p.128-130)**

| Clause | Finding | Amount (INR M) | Risk | Anchor |
|---|---|---|---|---|
| i(c) title deeds | Freehold land at Shahabad and building, gross INR M 108.7, still in the name of ACC Vickers Babcock / Alstom Projects India since 1 Aug 1974; reason: "Refer Note 3" | 108.7 | 🟡 minor | p.128 (L 8578-8585) |
| ii(a) inventory | Verified at reasonable intervals; no discrepancy of 10% or more | n/a | 🟢 | p.128 (L 8594-8609) |
| ii(b) working capital facility | Auditor says the Company "has not been sanctioned any working capital facility from banks or financial institutions" at any time in the year. The Notice says sanctioned facilities at 31 Mar 2026 were INR M 15,150 of which INR M 610 fund-based and INR M 14,540 non-fund-based, with INR M 330 fund-based drawn, and that facilities are availed "by charging inter alia Company's current assets". Direct conflict between two filed documents. | 610 sanctioned fund-based vs "none" | 🟡 | p.128 (L 8610-8615); Notice p.320 (L 21555-21571) |
| iii(a)-(f) loans | Unsecured loan to a fellow subsidiary, granted in year and outstanding INR M 4,500.0; payable on demand; terms "not prejudicial"; no demand for repayment made; 100% of loans granted are to related parties | 4,500.0 | 🟡 | p.128-129 (L 8616-8691) |
| iv s.185/186 | Complied; no guarantee given | n/a | 🟢 | p.129 (L 8692-8698) |
| vi cost records | Maintained; not examined in detail | n/a | 🟢 | p.129 |
| vii(a) undisputed dues | No arrears over six months | n/a | 🟢 | p.129 (L 8730-8735) |
| vii(b) disputed dues | Table by statute and forum (see below). Gross INR M 8,022.1, net of deposits INR M 7,658.3 (calc). | 8,022.1 | 🔴 reconciliation gap | p.129 (L 8646-8683) |
| viii, ix | No unrecorded income; no default; no wilful default; no short-term funds used long-term | n/a | 🟢 | p.130 |
| xi | No fraud noticed or reported; no ADT-4 filed; whistle-blower complaints considered | n/a | 🟢 | p.130 (L 8786-8797) |
| xiii | s.177 and s.188 complied | n/a | 🟢 | p.130 |
| xvii cash losses | None in FY26; INR M 824.15 in FY25 | 824.15 | 🟢 improving | p.130 (L 8823-8827) |
| xix | No material uncertainty (see 1A) | n/a | 🟡 standard disclaimer | p.130 |
| xx CSR | Average net loss in three prior years, so no statutory CSR; voluntary spend INR M 0.8 | 0.8 | 🟢 | p.130; Note 37 p.184 |

**Disputed-dues table (CARO vii(b)) against Note 39 contingent liabilities (new finding; stage 2 did not run this tie)**

| Head | CARO vii(b) gross (INR M, calc from p.129) | CARO net of deposit | Note 39 (p.185) |
|---|---|---|---|
| Sales tax (CST/LST/VAT) | 3,620.5 (54.7 + 381.8 + 44.0 + 2,599.4 + 538.6 + 2.0) | 3,476.0 | 2,036.7 |
| GST | 808.2 (99.1 + 59.1 + 466.3 + 173.0 + 10.7) | 797.0 | 132.6 |
| Income tax | 3,281.6 (48.2 + 147.4 + 299.9 + 2,786.1) | 3,096.5 | 1,105.8 |
| Central excise | 293.4 (195.5 + 97.9) | 270.4 | not a separate head |
| DGFT duty drawback | 18.4 | 18.4 | not a separate head |
| "Amounts not acknowledged as debts" | none | none | 1,300.8 |
| TOTAL | 8,022.1 | 7,658.3 | 4,575.9 |

- The CARO table exceeds Note 39 by INR M 3,446.2 (calc), or 75.3%. Sales tax alone in the CARO table (INR M 3,620.5) is 77.8% above the Note 39 sales tax head (INR M 2,036.7). The single CARO line "Tribunal, 2011-12 to 2017-18, sales tax INR M 2,599.4" is larger than the whole Note 39 sales tax head.
- Two readings. Reading A: Note 39 shows contingent amounts net of amounts already provided in "provision for contingencies/others" INR M 1,901.3 (Note 26 p.165), and the "Alstom Transport recoverable" (Note 50). The difference INR M 3,446.2 is larger than that whole provision (INR M 1,901.3), so reading A leaves a residual gap that is not explained. Reading B: the two tables use different bases (demand incl. interest and penalty versus principal). The filing does not say. Observation that separates them: a reconciliation line in Note 39 or the Note 50 and Note 26 narrative in AR27, or a management answer.
- Scale (calc): CARO gross INR M 8,022.1 = 147.5% of total equity INR M 5,437.7 and 339.4% of FY26 PAT INR M 2,363.6. Note 39 INR M 4,575.9 = 84.2% of equity (stage 2) and 193.6% of PAT (calc). Both clear the 25% (net worth) and 100% (PAT) flags.
- Stage 2 rank 9 stands but understates the exposure the auditor itself lists.

**1E Auditor continuity**

| Item | Finding | Anchor |
|---|---|---|
| Firm and partner | Deloitte Haskins & Sells (FRN 015125N); partner Vikas Khurana (membership 503760) | p.125 (L 8397-8406) |
| Tenure | First five-year term from the 29th AGM (2021) to the 34th AGM (14 Aug 2026); re-appointment for a second term to the 39th AGM (2031) is Notice Item 4 | Directors' Report p.26 (L 1227-1244); Notice p.289-290 |
| Rotation | Not due. Second term of the firm; partner rotation date NOT FOUND IN DOCUMENT | |
| Audit fee | INR M 10.5 FY26 (INR M 13.2 FY25); includes INR M 4.0 of "overruns", so the underlying fee is INR M 6.5 (calc). Tax audit 1.3 (1.9); limited reviews 4.4 (6.3); other services 0.3 (0.3); out-of-pocket 1.0 (0.8) | Note 33 p.168 (L 11760-11770, L 11806) |
| Total fees incl. network firms | INR M 18.31 FY26 against INR M 24.4 FY25; fall attributed to "change in scope post Hydro/Gas Business carveout" | CG Report p.116-117 (L 7701-7770) |
| Non-audit to audit ratio | "Other services" INR M 0.3 against audit INR M 10.5 = 2.9% (calc). Even with limited reviews and tax audit counted as non-audit, INR M 6.0 (calc) vs INR M 10.5 = 57%, so non-audit does not exceed audit. Network-firm non-audit NOT SEPARATED. | Note 33 p.168 |
| FY27 proposed audit fee | INR M 11.70 excluding taxes | Notice L 20774 |
| Cost auditor | Yogesh Gupta & Associates, INR M 0.3 (INR 300,000) for FY27 | Directors' Report p.26 |
| Internal auditor | Ernst & Young LLP; reports to Audit Committee | p.6; CG Report p.116 |

**1F Standalone vs consolidated.** One subsidiary (GE Power Boilers Services Ltd, 100%; income INR M 1.6; accumulated losses INR M 3.1; its statements are on a basis other than going concern, Directors' Report p.27 L 1342-1356) and one 50% joint venture (NGSL, equity method, GVPIL share of profit INR M 161.7; investment INR M 72.0). Same auditor for the group; consolidated report carries the same single KAM and no extra qualification (p.206-207). No other-auditor reliance stated for NGSL beyond the standard text. Consolidated and standalone differ mainly by the JV profit share.

**Phase 1 verdict: 🟡 Watch.** Clean unmodified opinion and clean CARO on fraud, defaults and statutory dues. Three items hold it at Watch: the CARO disputed-dues table (INR M 8,022.1) does not reconcile to Note 39 (INR M 4,575.9); CARO ii(b) contradicts the Notice on bank sanctions; the single KAM did not change while the year's risk did.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop on the auditor's report alone, because the opinion is unmodified and CARO reports no fraud, default or arrears. The disputed-dues reconciliation is a question for management.

---
## PHASE 2: NOTES TO FINANCIAL STATEMENTS (verify, extend, summarise)

### Verification of the stage 2 Top 15 against the AR

| Rank | Finding | AR check (number, anchor) | Mark |
|---|---|---|---|
| 1 | ICD INR M 4,500.0; 21.4% of assets; 106% of cash; absent from Notes 42/43; Notice says PCG secures it | 4,500.0 (p.131, L 8931); total assets 20,995.6 gives 21.43% (calc); cash 4,244.6 gives 106.0% (calc); Notice L 21301 and L 19881 present. NEW: CARO iii(a) and Note 16 header say UNSECURED; Notice Item 10 says GEV "proposes to provide" the INR M 10,000 guarantee (L 21757-21762) | ✓ verified (reading sharpened below) |
| 2 | PBT before exceptional 3,399.0; reversal 1,016.6; write-backs 240.9; insurance 184.2; group income 851.9; step-up share 55.3% | 3,399.0 (p.132); 1,016.6 (L 11758); 240.9 and 184.2 (L 11720, 11724). Group income re-built: 106.0 + 156.7 + 78.7 + 188.6 + 30.6 + 72.5 = 633.1, plus ICD interest 199.8, plus JV 19.0 = 851.9 (Note 36 p.180-181). Step-up 3,399.0 - 224.6 = 3,174.4; ECL swing 1,320.0 + other income 433.5 = 1,753.5, which is 55.2% (calc) | ✓ verified; ✗ minor: 55.2% not 55.3% (1,753.5 / 3,174.4 = 55.24%) |
| 3 | CFO 4,692.5 is a working-capital release; receivables +5,136.0 | 4,692.5 and 5,136.0 (p.133, L 9146, 9156). Other current liabilities line (2,158.3) (L 9152); stage 2's 2,106.6 is advances (677.9 vs 1,764.0, down 1,086.1) plus billing in excess (3,399.9 vs 4,420.4, down 1,020.5) (Note 25 p.164) | ✓ verified |
| 4 | RPO 16,278 / 26,623 / 15,870 | 16,278 and 26,623 (Note 27 p.166, L 11651); Mar-24 15,870 (AR25 L 12521). Derived additions 2,347.7 = 16,278 - 26,623 + 12,692.7 (calc) | ✓ verified |
| 5 | Durgapur cost 548.0 outside continuing; 247.0 internal billing | 548.0 loss before exceptional (p.132, L 9058); Note 47(vi) ties to P&L; not re-read line by line here | ✓ verified |
| 6 | Parent guarantee 7,977.6 used; peak 20,432; debt 330.0; net cash 8,473.1 | 7,977.6 (Note 36 p.182, L 12522-12524); 20,432 and 7,648 + 330 = 7,978 (Notice p.320-322, L 21569-21571, 21581); 4,244.6 + 58.5 + 4,500.0 - 330.0 = 8,473.1 (calc) | ✓ verified |
| 7 | Royalty P&L 125.7 vs table 435.7; gap 310.0 | 125.7 (L 11755); 305.1 + 110.1 + 20.5 = 435.7 (L 12385-12391) | ✓ verified |
| 8 | Note 26 "slump sale" deductions repeat FY25; 322.7 > 280.3; warranty -34.0% | 185.0 and 137.7 in both columns (L 11572, 11604); 579.9 / 879.1 = -34.0% (calc). Durgapur provisions 172.8 + 107.5 = 280.3 (L 13292, 13319) | ✓ verified |
| 9 | Contingent liabilities 4,575.9; 84.2% of net worth; sales tax 37.5% | 2,036.7 + 132.6 + 1,105.8 + 1,300.8 = 4,575.9 (L 12724-12734); /5,437.7 = 84.2% (calc). The AR's own 5-year chart prints net worth INR M 4,829 (p.13), which equals equity less capital reserve INR M 609.0 (5,437.7 - 609.0 = 4,828.7, calc); on that base it is 94.8% | ✓ verified (base difference noted) |
| 10 | Top two customers 38.6%; NGSL 1,111.6 (8.8%); receivable 703.0; advances 833.0 | 38.6% (L 12199); 1,111.6 / 12,692.7 = 8.8% (calc); 703.0 and 833.0 (L 12598-12602); advance line 677.9 (L 11578) | ✓ verified |
| 11 | Hydro Re 1; gain 2,369.9; Durgapur net liabilities 548.7 | L 13209, 13218; L 13286 | ✓ verified |
| 12 | Inventory +69.9%; revenue +21.2%; payables overdue 65.9% to 41.3%; FX payables 535.9 | 1,495.7 / 880.5 = +69.9% (calc); 12,692.7 / 10,471.0 = +21.2% (calc); not-due payables 3,244.3 of 5,529.5 gives 41.3% overdue; FY25 1,783.4 of 5,232.3 gives 65.9% (Note 23 p.163, L 11501, 11517); 535.9 (L 11520) | ✓ verified |
| 13 | Unrecognised DTA 1,806.8 netted (note shows 1,983.6); ETR 2.5% | 1,983.6 vs total DTA 1,895.2 (L 11092, 11128); ETR 61.7 / 2,425.3 = 2.5% (calc) | ✓ verified |
| 14 | Labour Codes 425.7 (275.7 + 150.0); gratuity past service 320.7 | 425.7 (L 13247); exceptional lines (275.7) and (150.0) (p.132, L 9047, 9059). Past service 320.7 not re-read | ✓ verified (320.7 carried) |
| 15 | Other expenses ex-ECL +26.3%; misc 299.3 vs 20.7; legal 234.8 vs 77.3; two KMP posts open | (616.2 + 1,016.6) = 1,632.8 vs (1,596.2 - 303.4) = 1,292.8 = +26.3% (calc); L 11772, 11802; CFO resignation 13 May 2026, CS resignation 2 Apr 2026 (p.25, L 1054-1057, 1122-1123) | ✓ verified |

Result: 15 of 15 verified. One rounding point (rank 2: 55.2%, not 55.3%). One base note (rank 9). No number or note reference is wrong.

### Where the AR sharpens stage 2

1. **The existing ICD was unsecured at the balance sheet date.** Note 16 headline reads "(Unsecured considered good unless otherwise stated)" (p.158, L 11267). CARO iii(a) says the Company "has granted unsecured loans" (p.128, L 8616). The Notice says the loan "is secured through Parent Corporate Guarantee" (p.317, L 21301, 21416-21422) and that GEV "proposes to provide a guarantee up to the maximum amount of INR M 10,000" (p.323, L 21757-21762). Reading the audited documents together, the PCG for the INR M 4,500.0 was not in place at 31 Mar 2026 (inference). It is proposed for the period after the 14 Aug 2026 AGM. Stage 2 left "coverage unconfirmed"; the audited documents answer it. Counterparty facts from the Notice: LM Wind FY25 turnover INR M 25,488.7, PAT INR M 2,917.1, net worth INR M 9,366.2; the INR M 4,500.0 is 48.0% of that net worth and the INR M 10,000 ceiling is 106.8% (calc, p.314). GEV rated BBB (S&P) and BBB+ (Fitch) (p.318). The Notice says LM Wind's own credit rating "is not available".
2. **Approval chain of the cap.** The Directors' Report (p.30, L 1557-1562) says the INR M 4,500 s.186 limit came from a postal ballot of 29 March 2025. The Notice (p.320, L 21587-21589) says it came from the 33rd AGM on 14 August 2025. Secretarial Audit (p.35, L 2030-2044) lists a separate 4 May 2025 postal ballot with MRPT approvals for LM Wind of INR M 600 and INR M 10,500 and for GE Vernova Inc. INR M 40,000, with no purposes printed. The loan sits exactly at the s.186 cap. Date of approval: two filed dates disagree. 🟡.
3. **Cash flow FY25 comparatives were re-presented.** AR25 printed FY25 CFO INR M 3,196.5, investing INR M 539.9, financing INR M (658.4) (AR25 L 10330, 10339, 10353). AR26 prints FY25 CFO INR M 3,790.4, investing INR M 563.1, financing INR M (1,275.5) (p.133-134). CFO moved up INR M 593.9 (calc). The cause is a new financing line "Movement in owner's investment (pursuant to Scheme)" INR M (617.1) FY25 and INR M (349.5) FY26 that carries the Durgapur cash drain outside CFO. FY26 CFO is therefore continuing-business CFO; Durgapur-inclusive CFO is INR M 4,343.0 (4,692.5 - 349.5, calc). 🟡.
4. **MD&A ratios do not agree with Note 44.** MD&A p.93 prints Return on Net Worth 0.69 (FY25 0.20); Note 44 p.192 prints Return on Equity 0.73 (FY25 0.13), which my calc matches (3,061.0 / average equity 4,188.8 = 0.731). MD&A also labels "Net Profit Margin (%) 0.24" and "Return on Net Worth (%) 0.69" with fractions, not percentages. The "Operating Profit Margin 26.33%" reproduces only as (PBT after exceptional 3,123.3 + finance cost 219.0) / revenue 12,692.7 (calc). 🟡 minor: unit labelling and a ratio basis that differ by page.
5. **Remuneration.** MD pay rose from INR M 30.9 to INR M 48.4 (+56.6%, calc) with RSU/ESOP exercise included (Note 36 p.182, L 12509-12513); Annexure D shows fixed pay +8.4% (p.38).

### 2A Accounting policy aggressiveness (extend)

| Item | Finding | Anchor | Rating |
|---|---|---|---|
| Revenue recognition | Percentage of completion on cost-to-cost for over-time contracts (60.2% of revenue). Net contract liability INR M 3,056.5 (billing in excess 3,399.9 less contract assets 343.4): customers fund the work. Prior-period estimate effect +INR M 70.3 | Note 27 p.166 | 🟡 |
| Depreciation lives | Not re-read here beyond stage 2 (plant up to 50 years on a INR M 93.8 net block per stage 2). Depreciation INR M 122.8, of which right-of-use INR M 100.9 (Note 22) so owned-asset depreciation is INR M 21.9 | Note 32 p.168; Note 22 p.162 | 🟢 low base |
| Capitalisation | Capex INR M 21.3 against depreciation INR M 122.8 = 0.17x (calc). No borrowing-cost capitalisation seen | p.133 | 🟢 |
| ECL matrix | Allowance 7.7% of gross receivables at the bottom of the stated 7.3% to 13.1% band (stage 2); INR M 1,016.6 reversal booked under Other expenses on BHEL cash INR M 3,430.6 (Note 53 p.202) | Note 53 | 🟡 |
| Policy change | None stated. CEO/CFO certificate: "no significant changes in the accounting policies" (p.118). Note 2.20 common-control policy lets the Company choose P&L or equity for the gain on group transfers (used in FY25) | p.118; Note 47(ii) | 🟡 |
| Ind AS 116 | Incremental borrowing rate 9% both years; lease liability INR M 175.9 | Note 22 p.162 | 🟢 |
| Discontinued presentation | FY25 re-presented for Durgapur: INR M 604.8 of cost moved out of continuing result (stage 2); depreciation on Durgapur stopped from 18 Sep 2025 | Note 47(iii) p.194 | 🟡 |

### 2B Related-party map (percentages are my calc on Note 36, p.180-183)

| Group | FY26 INR M | % of revenue (12,692.7) or other base | Note |
|---|---|---|---|
| Revenue from fellow subsidiaries (sum of lines) | 376.8 | 3.0% | Largest: GE Power Systems India 74.2, GE Steam Power Inc 72.9, Powerstatic 59.2 |
| Revenue from NGSL (50% JV) | 1,111.6 | 8.8% (FY25 265.1; 4.2x) | Receivable 703.0; advances held 833.0 |
| Revenue from subsidiary | 0.4 | 0.0% | |
| Total related-party revenue | 1,488.8 | 11.7% | |
| Other income from group (6 fellow subsidiaries + ICD interest + NGSL) | 851.9 | 74.3% of other income; 25.1% of PBT before exceptional | |
| Royalty and trademark (table) | 435.7 | 3.4% of revenue; P&L line 125.7 (1.0%) | Gap 310.0 unplaced |
| Material purchases, fellow subsidiaries | 699.1 | 9.0% of cost of materials (calc: 699.1 / 7,765.2) | Nexus Controls 182.6, GE Power GmbH 106.1, GE Steam Power Switzerland 96.5 |
| Material purchases and services from NGSL | 406.1 (225.0 + 181.1) | 5.2% of cost of materials | |
| Service purchases, fellow subsidiaries | 241.0 | | Powerstatic 239.7 |
| ACC-Babcock Staff Provident Fund | 169.4 | | Related party (employee trust) |
| ICD given to LM Wind | 4,500.0 | 21.4% of total assets | Interest income 199.8 |
| Gratuity paid to GE Vernova Hydro (business combination) | 226.2 | | Trade payable to it 23.8 (FY25 226.2) |
| Guarantee received from GE Vernova Inc (labelled "issued") | 7,977.6 (FY25 28,100.0) | 49.9% of INR M 16,000 sought | Peak 20,432 |

Value-extraction signals: royalty outflow to group of INR M 435.7 is 18.4% of FY26 PAT (calc: 435.7 / 2,363.6). The cash pool places surplus cash with the group's treasury at 5.49% to 6.35% against a 90-day bank deposit rate of 5.25% to 5.50% the Notice quotes (p.315, L 21303-21305), a pick-up of about 0 to 1.1 percentage points for unsecured group credit (calc). The Hydro business left for INR 1; FY25 gain and capital reserve followed from policy choice. Promoter dividend: 46,102,083 shares x INR 7 = INR M 322.7 (calc), 68.6% of the INR M 470.6 recommended. No loan to promoter family or to a firm in which a director is interested (CG Report p.117, L 7790-7792).

### 2C Contingent liabilities (done in 1D)
Note 39 INR M 4,575.9 = 84.2% of equity, 193.6% of PAT. CARO gross INR M 8,022.1 = 147.5% of equity, 339.4% of PAT. Both clear the 25% and 100% flags. No forum or stage in Note 39. The Company states "no provision is considered necessary" because it "believes that it has good cases" (p.185, L 12736-12738), while Note 26 carries INR M 1,901.3 for "probable claims" from disputes with authorities. A claim cannot be both "good case, no provision" and "probable". 🟡.

### 2D to 2H (stage 2 stands; additions only)
- **2D Receivables.** Gross INR M 8,260.5 less allowance INR M 635.9 = net INR M 7,624.6 (ties, balance sheet p.131). FY25 gross 13,489.2 less 1,759.7 = 11,729.5 (ties, L 11248-11250). Net days 219 (calc: 7,624.6 / 12,692.7 x 365) against 409 FY25. Concentration: top two customers 38.6%. NGSL receivable INR M 703.0 = 9.2% of net receivables (calc). Unbilled: contract assets INR M 343.4.
- **2E Inventory.** INR M 1,495.7 (+69.9%) on revenue +21.2%. Days about 71 against 46 (calc, stage 2). Raw materials consumed INR M 5,237.2 against INR M 3,373.5 (+55.3%, calc) while project materials fell INR M 3,674.8 to INR M 2,528.0 (-31.2%, calc): the mix moved from project execution to parts and services supply. No write-down line found.
- **2F Borrowings and maturity wall.** No term debt. Fund-based draw INR M 330.0 sits inside Durgapur held-for-sale liabilities (p.195, L 13301) and equals the INR M 330 "utilised" in the Notice (L 21570). Contractual maturities (Note 43 p.190): trade payables INR M 5,529.5 (INR M 4,795.3 within one year), leases INR M 175.9 (INR M 123.4 within one year), amount held in trust INR M 1,607.0 all within one year; total non-derivative INR M 7,315.2. Covenant: bank documents require GE Vernova to keep majority ownership for the life of the facilities; the ICRA rating "draws strength on GEV's global rating" (Notice p.324, L 21793-21796). ICRA upgraded the long-term rating from BBB to BBB+ (Stable) on 2 Mar 2026 (CG Report p.115, L 7643-7647). Pledge: deposits INR M 55.5 pledged against bank guarantees (Note 15). ICDs given: INR M 4,500.0.
- **2G Deferred tax.** Total DTA INR M 1,895.2, unrecognised INR M 1,983.6 (Note 9, L 11092, 11128). Effective tax rate 2.5% (calc). Brought-forward loss expiry schedule: NOT FOUND IN DOCUMENT.
- **2H Exceptional, goodwill, ESOP, leases, post balance sheet.** Exceptional items by year: FY24 none in continuing (AR25); FY25 gain INR M 2,953.3 on carve-outs (discontinued); FY26 INR M (275.7) continuing and INR M (150.0) discontinued for Labour Codes. Goodwill: nil (intangibles nil, p.131). ESOP/RSU: parent-company plans only; 3,901 options and 451 RSUs outstanding (Note 49, L 13690, 13712), no new GVPIL shares, so dilution nil; share count unchanged at 67,227,471 (Note 19). Post balance sheet: dividend of INR 7 per share, INR M 470.6 (Note 61); scheme observations from BSE and NSE on 1 Apr 2026; CFO and CS exits.

**Phase 2 reconciliation with stage 2 score (6/10):** I agree with 6/10 and a Watch verdict. Stage 2 cited the contingent disclosure as vague. The CARO table now shows the disclosure gap is INR M 3,446.2 wide. That would lower provisioning adequacy from 5 to 4 on its own; I hold the overall at 6 because the gap may be a basis difference (reading B). If management confirms reading A (unprovided), the score falls to 5.
**Cross-reference with Phase 1 KAM:** the single KAM covers cost to complete. The notes' larger accounting risks (ECL reversal, ICD, held-for-sale, contingencies) have no KAM.
**Phase 2 verdict: 🟡 Watch.**
**Kill switch (informational):** a human reviewer would not have reason to stop here, because no impairment, covenant, default or going-concern signal exists. The unsecured INR M 4,500.0 group loan and the CARO reconciliation gap are open questions, not stop signals.

---
## PHASE 3: FINANCIAL STATEMENTS (cash flow, balance sheet, P&L)

### 3A Cash flow (p.133-134; INR M)

| Line | FY26 | FY25 (as re-presented in AR26) | FY25 (as printed in AR25) | FY24 (AR25) |
|---|---|---|---|---|
| Profit before tax, continuing | 3,123.3 | 224.6 | (380.2) | (1,423.7) |
| Operating profit before working capital | 2,509.2 | 661.8 | 63.5 | (800.2) |
| Trade receivables decrease | 5,136.0 | 542.5 | 542.5 | 3,728.0 |
| Other current liabilities | (2,158.3) | 1,543.1 | 1,543.1 | 55.6 |
| Trade payables | 189.1 | 724.9 | 716.6 | (516.0) |
| Inventories | (625.9) | (119.3) | (119.2) | 18.9 |
| CFO | 4,692.5 | 3,790.4 | 3,196.5 | 1,824.0 |
| Capex | (21.3) | (30.3) | (53.5) | (23.2) |
| Loan to related parties | (4,500.0) | nil | nil | nil |
| Financing: lease repayment | (122.8) | (139.0) | (139.0) | (153.2) |
| Financing: owner's investment (Scheme) | (349.5) | (617.1) | not a line | not a line |
| Net change in cash | (138.6) | 3,078.0 | 3,078.0 | (469.5) |
| Closing cash and equivalents | 4,244.6 | 4,383.2 | 4,383.2 | 1,305.2 |

CFO quality tests:
- CFO / PAT = 4,692.5 / 2,363.6 = 1.99 (calc); CFO / continuing PAT = 1.53 (calc). Not below 0.7. The ratio is high because PAT is partly non-cash in timing: the INR M 1,016.6 reversal is a profit with cash behind it (BHEL INR M 3,430.6), but the cash came from old receivables.
- CFO / EBITDA = 4,692.5 / 3,740.8 = 1.25 (calc). On EBITDA before other income (INR M 2,594.4, calc) it is 1.81.
- One-time inflators: receivables release INR M 5,136.0 (109.5% of CFO, calc) offset by customer advances and billing in excess (Note 25: payments in advance 677.9 vs 1,764.0; billing in excess 3,399.9 vs 4,420.4, a fall of INR M 2,106.6, calc). FY25 receivables inflow was only INR M 542.5, so the FY26 release is not a trend. Receivables fell 35.0% (7,624.6 / 11,729.5 - 1, calc). With gross receivables now INR M 8,260.5 against revenue INR M 12,692.7, a repeat release of this size is not available.
- Working-capital reversal in FY27: inventory build (outflow INR M 625.9) has started; customer advances fall; the overdue share of payables fell from 65.9% to 41.3%, which means supplier float was repaid.
- Interest classification: interest received INR M 172.6 is in investing; interest paid is nil in FY26 although finance cost is INR M 219.0 (P&L) and INR M 186.6 is added back. The unpaid portion includes interest on the INR M 1,607.0 held in trust (INR M 53.7) and interest on uncertain tax positions (INR M 113.4 "others", Note 31 p.168). Cash interest will be a FY27 cost if settled.
- **Where the cash went.** INR M 4,500.0 of INR M 4,692.5 CFO (95.9%, calc) went to a group treasury as an unsecured demand deposit. Dividend INR M 470.6 is still to be paid. Durgapur drain INR M 349.5 sits in financing. FCF = CFO 4,692.5 - capex 21.3 = INR M 4,671.2; after leases (122.8) and Durgapur funding (349.5) INR M 4,198.9 (calc). Cash balance still fell INR M 138.6.
- Trust liability: cash and bank INR M 4,303.1 stands against INR M 1,607.0 held in trust (Supreme Court pending since 2016, stage 2) and customer-funded contract liabilities INR M 3,399.9 plus advances INR M 677.9. Net cash after the trust amount: INR M 8,473.1 - 1,607.0 = INR M 6,866.1 (calc).
- **FLAG-CASH raised**: CFO is real cash but one-time in source, flows 95.9% to a related-party deposit, and FY25 comparatives were re-presented upward by INR M 593.9.

### 3B Balance sheet (p.131; INR M)

| Asset side | 31 Mar 2026 | 31 Mar 2025 | Liability and equity side | 31 Mar 2026 | 31 Mar 2025 |
|---|---|---|---|---|---|
| PPE | 246.6 | 354.6 | Equity share capital | 672.3 | 672.3 |
| CWIP | 31.9 | 43.7 | Other equity | 4,765.4 | 2,267.5 |
| ROU assets | 155.4 | 272.1 | Lease liabilities (NC + C) | 175.9 | 288.3 |
| Investment in JV | 72.0 | 72.0 | NC provisions | 238.8 | 619.1 |
| Tax assets | 679.4 | 493.5 | Trade payables | 5,529.5 | 5,232.3 |
| Inventories | 1,495.7 | 880.5 | Other financial liabilities (incl. trust 1,607.0) | 1,609.8 | 1,557.0 |
| Trade receivables | 7,624.6 | 11,729.5 | Other current liabilities | 4,193.3 | 6,351.6 |
| Cash and equivalents | 4,244.6 | 4,383.2 | Current provisions | 2,917.9 | 2,765.6 |
| Loans (ICD) | 4,500.0 | nil | Current tax liabilities | nil | 141.5 |
| Other financial and other assets | 1,432.7 (58.5 + 268.9 + 1,007.1 + 155.6 + 111.3 + 31.3, see note) | 1,666.1 | HFS liabilities | 892.7 | nil |
| HFS assets | 344.0 | nil | | | |
| Total | 20,995.6 | 19,895.2 | Total | 20,995.6 | 19,895.2 |

Note on the "other assets" row: it groups bank balances other than cash (58.5), other current financial assets (268.9), other current assets (1,007.1), other non-current financial assets (155.6) and other non-current assets (111.3) = 1,601.4 (calc) for FY26 and 37.4 + 34.7 + 1,153.1 + 149.4 + 291.5 = 1,666.1 for FY25. The FY26 figure in the cell above should read 1,601.4; the parenthetical list carries an extra 31.3 that is not a balance sheet line. Totals tie: 246.6 + 31.9 + 155.4 + 72.0 + 679.4 + 1,495.7 + 7,624.6 + 4,244.6 + 4,500.0 + 1,601.4 + 344.0 = 20,995.6 (calc).

Key ratios (calc unless marked):

| Ratio | Value | Anchor or method |
|---|---|---|
| Debt/equity | nil (MD&A); the INR M 330.0 bank draw is in HFS liabilities; Notice shows 0.55x after a INR M 3,000 cash-pool borrowing | MD&A p.93; Notice p.319 (L 21525-21528) |
| Net debt/EBITDA | net cash; not meaningful | |
| Current ratio | 1.34 (19,199.4 / 14,362.5) | MD&A p.93; Note 44 p.192 |
| Quick ratio | 1.23 ((19,199.4 - 1,495.7) / 14,362.5) | calc |
| Interest coverage | 15.26 (MD&A basis); 16.5x on (PBT pre-exceptional + finance) / finance | p.93; calc |
| ROE (continuing PAT / average equity) | 73.1% (Note 44 prints 0.73); on total PAT 56.4% | Note 44 p.192; calc |
| ROCE (continuing EBIT 3,342.3 / (total assets - current liabilities incl. HFS) 5,740.4) | 58.2% | calc; not meaningful because customer advances fund the asset base |
| Goodwill / net worth | 0% | p.131 |
| Equity rebuilt | INR M 573.5 (1 Apr 2024) to 2,939.8 to 5,437.7 | p.135; stage 2 |

DuPont (calc, average balances): net margin 18.6% (2,363.6 / 12,692.7) x asset turnover 0.621 (12,692.7 / 20,445.4) x leverage 4.88 (20,445.4 / 4,188.8) = 56.4%. ROE is leverage-driven by liabilities that are not debt: trade payables INR M 5,529.5, customer-funded contract liabilities INR M 4,077.8, provisions INR M 2,917.9 and the INR M 1,607.0 trust. It is not operational in the sense of margin alone, and it is not borrowed. The "equity" is thin against a large non-interest-bearing float, which is why ROE and ROCE look extreme.

Balance sheet read: no debt of substance, goodwill nil, cash of INR M 4,244.6 plus INR M 4,500.0 group deposit, and a current ratio of 1.34. Against that, float liabilities (payables plus contract liabilities) are INR M 9,607.3 (calc), larger than cash plus ICD INR M 8,744.6 (4,244.6 + 4,500.0, calc). The balance sheet is liquid only if the group deposit is recalled on demand and customers do not call the work. Recall right: "Pool participants have full liquidity rights and can withdraw cash lent ... at any time without any penalty" (Notice p.317, L 21403-21404).

### 3C P&L (p.132; continuing operations; INR M)

| Line | FY26 | FY25 | YoY | % of revenue FY26 (FY25) |
|---|---|---|---|---|
| Revenue | 12,692.7 | 10,471.0 | +21.2% | 100 |
| Other income | 1,146.4 | 712.9 | +60.8% | 9.0 (6.8) |
| Cost of materials and erection (net of WIP change) | 7,643.0 | 7,042.8 | +8.5% | 60.2 (67.3) |
| Employee benefits | 1,839.1 | 1,934.9 | -5.0% | 14.5 (18.5) |
| Other expenses | 616.2 | 1,596.2 | -61.4% | 4.9 (15.2) |
| Other expenses ex ECL line | 1,632.8 | 1,292.8 | +26.3% | 12.9 (12.3) |
| Finance costs | 219.0 | 247.2 | -11.4% | 1.7 (2.4) |
| Depreciation | 122.8 | 138.2 | -11.1% | 1.0 (1.3) |
| PBT before exceptional | 3,399.0 | 224.6 | +1,413% | 26.8 (2.1) |
| Exceptional (Labour Codes) | (275.7) | nil | | 2.2 |
| Tax | 62.3 | nil | | 2.0% of PBT |
| Net profit, continuing | 3,061.0 | 224.6 | | 24.1 |
| Discontinued, after tax | (697.4) | 1,693.5 | | |
| Net profit | 2,363.6 | 1,918.1 | +23.2% | 18.6 |
| EPS (basic = diluted, INR) | 35.16 (continuing 45.53) | 28.54 (continuing 3.34) | | |

Margin waterfall (calc, FY26, % of revenue): revenue 100 -> after net materials 39.8 -> after employee cost 25.3 -> after other expenses ex reversal 12.4 (core EBITDA INR M 1,577.8) -> add reversal 8.0 -> EBITDA before other income 20.4 -> add other income 9.0 -> PBITDA 29.5 -> less depreciation and finance 2.7 -> PBT before exceptional 26.8 -> exceptional 2.2 -> PBT 24.6 -> tax 0.5 -> continuing PAT 24.1 -> discontinued 5.5 -> PAT 18.6.

- Other income is 33.7% of PBT before exceptional (1,146.4 / 3,399.0, calc), above the 20% flag. With the reversal it is 63.6% (2,163.0 / 3,399.0, calc). Without both, PBT before exceptional is INR M 1,236.0 (calc), 9.7% of revenue.
- Exceptional items: INR M 2,953.3 gain (FY25), INR M (425.7) charge (FY26). Two years running. Each year carries a structural item (carve-out, then Labour Codes) that is labelled non-recurring.
- Tax: current tax INR M 62.3 on PBT INR M 3,123.3 = 2.0%; total 2.5% on INR M 2,425.3. Low because brought-forward losses shield profit (unrecognised DTA INR M 1,983.6 or INR M 1,806.8 netted). Cash tax rises when the pool is spent. Expiry schedule NOT FOUND.
- EPS: basic equals diluted at INR 35.16; no dilutive instruments of GVPIL.
- Revenue base: FY24 INR M 10,386.7, FY25 INR M 10,471.0, FY26 INR M 12,692.7 (AR25 p.168; AR26 p.132). Two-year CAGR 10.5% (calc), +0.8% then +21.2%. FY26 growth is the first real step.
- Revenue mix (Note 35): construction contracts INR M 7,640.3 (+22.9%), products INR M 4,911.7 (+18.9%), services INR M 109.5 (-2.0%) (calc from p.176). Exports INR M 349.5 = 2.75% (calc; BRSR p.49 prints 2.75%).
- Raw materials and components consumed jumped 55.3% to INR M 5,237.2 while project materials fell 31.2%: FY26 revenue is parts and equipment supply plus services, less erection.

**Phase 3 verdict: 🟡 Watch.** Cash is real and the balance sheet carries no debt. Earnings quality is the issue: 55.2% of the profit step-up is a reversal and other income, 25.1% of PBT is group-sourced, CFO is a one-time receivable release, and 95.9% of it moved to a group deposit.
**Kill switch (informational):** a human reviewer would not have reason to stop here. A reviewer would stop to ask whether FY27 can repeat the margin without the reversal and without the cash release.

---
## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (what the AR says)
There is no separate "Risk Factors" section. Risk text sits in the Directors' Report (p.30, L 1598-1628, ERM framework with a Risk Management Committee that met twice) and the MD&A (p.92, "Risks and Threats", L 5738-5768).

| Disclosed risk | Real or boilerplate | Anchor |
|---|---|---|
| Delays in customer decisions, tender finalisation, ordering cycles, site readiness, especially retrofit and environmental compliance | Real but unquantified. Matches the RPO fall and the Board's own DTA reasoning "delay in order backlog execution ... lower order intake than expected" (Note 9 p.155) | MD&A p.92 |
| FGD timelines and working-capital cycles | Real. Settlement with JPVL (INR M 250) and BHEL (INR M 3,400) show it | MD&A p.92; Note 53-54 |
| Grid, supply chain, input cost, competition, policy | Boilerplate | MD&A p.92 |
| Skilled manpower and talent retention | Mixed. BRSR prints permanent-employee turnover 71.11% (FY25 28.05%) while MD&A prints attrition 8.7% "an improvement" | MD&A p.94; BRSR p.51 |
| FX, commodity | Real but small: unhedged exposure with a 10% sensitivity of about INR M 23.9 (USD) and INR M 7.7 (EUR) after tax (Note 43 p.192); CG Report p.115 says "no exposure ... to commodity" | Note 43; CG p.115 |
| Board's view: "none of the above-mentioned risks threaten the existence of your Company" | Boilerplate | p.30 (L 1627-1628) |

### 4B Missing risks (obvious from Phases 1-3, absent from the risk text)

| # | Missing risk | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Credit and liquidity exposure to a group treasury: unsecured INR M 4,500.0 demand deposit = 21.4% of assets, 106% of cash | Note 16 p.158; CARO iii(a) p.128; balance sheet p.131 | Treated as treasury routine under the group cash pool; the Notice (not the MD&A) discloses it |
| 2 | Single-guarantor dependence: banks require GEV to keep majority ownership; INR M 16,000 of guarantees needed; ICRA rating "draws strength" from GEV | Notice p.320-324 | Seen as support, not risk. The July 2024 communication "Ending Plan to Exit ... and De-Promoterise" (p.28, L 1407-1417) shows the exit option existed |
| 3 | Order-book contraction: RPO -38.9% to INR M 16,278; derived FY26 additions INR M 2,347.7 (calc) | Note 27 p.166 | MD&A says "healthy order backlog" (p.18) |
| 4 | Customer concentration: two customers 38.6% | Note 35 p.176 | Names NOT DISCLOSED; likely public-sector buyers (inference) |
| 5 | Durgapur demerger execution and the post-demerger cost of INR M 247.0 internal supply; consideration paid in JSW shares | Note 47(iii), (vi); Directors' Report p.28 | MD&A p.88-95 never mentions the Scheme or JSW. The word "Durgapur" appears there only in the HR section (p.93) |
| 6 | One-off earnings: reversal INR M 1,016.6, write-backs INR M 240.9, insurance INR M 184.2, JPVL INR M 250 | Notes 28, 33, 53, 54 | MD&A never explains the profit jump |
| 7 | Disputed taxes: CARO gross INR M 8,022.1 vs Note 39 INR M 4,575.9 | p.129; p.185 | No narrative anywhere |
| 8 | KMP continuity: CFO/WTD and company secretary resigned (13 May 2026, 2 Apr 2026); new CFO Rahul Rojal and CS Vipul Sharma from 19 June 2026 | p.25; p.6 | Handled as routine in board changes |
| 9 | Working-capital reversal: inventory +69.9%, customer advances down | Balance sheet; Note 25 | MD&A attributes debtor turnover only to "decrease in average trade receivable" (p.93) |
| 10 | Amount held in trust INR M 1,607.0 (Supreme Court pending since 2016) | Note 24 p.163; Note 43 p.190 | Not described in MD&A |
| 11 | Labour Codes and PF-trust exemption surrender (open-ended) | Note 47(iv) p.195; Note 34 | Described as non-recurring |

### 4C MD&A deep dive

- **Industry claims.** Electricity demand growth 6.4% a year for India to 2030 (IEA, cited), thermal fleet ageing, renovation and FGD regulatory clarity (p.89-91). Sourced to IEA, OECD, PIB. No GVPIL market share, no addressable market size, no pricing data. The 524 GW installed base and 38,745 MW thermal under construction (p.90) are sector facts, not company claims.
- **Growth and margin explanations.** None for the company. The MD&A "Key Financial Ratios" table (p.93) gives only variance reasons in one line each, such as "increase in profit before tax and interest expense from continuing operations". No discussion of the INR M 3,174.4 profit step-up, the reversal, the other income or exceptional items.
- **Credit-taking and blaming.** The year is credited to focus: "reinforced our strategic focus on high-margin, cash-accretive opportunities with shorter cash conversion cycles" (p.18). External blame is for risk only (customer delays, FGD timelines). The BHEL and JPVL settlements are reported as events (p.22), not as profit drivers.
- **Segment analysis.** Single segment "Power Generation equipment and related services" (Note 35 p.176). Business lines are named (Boilers, Services, Mills, Automation and Control, Air Quality Control, p.5) without revenue or margin. Revenue split by accounting basis only.
- **Order disclosure.** One order quantified in the whole AR: INR M 430 from NTPC for generator parts at Talcher (p.18, p.91) = 2.6% of RPO (calc). Others named without value (Monnet Power 500 MW stator repair; Adani Kawai IP inner casing; RattanIndia LP blades; Adani Mundra study; RRUVNL Kalisindh ESP refurbishment, p.18-19).
- **JV order book (50% NGSL).** Order book INR M 21,828 and inflow INR M 6,182 for FY26 (p.27) against INR M 23,032 and INR M 15,344 in AR25 (AR25 L 1480): book -5.2%, inflow -59.7% (calc). NGSL revenue INR M 7,663 (p.27) against INR M 7,225.3 (AR25 L 16950), +6.1% (calc).

**Forward guidance table**

| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| "healthy order backlog" (p.18) | RPO INR M 16,278 = 1.28x FY26 revenue (calc) | Mar-26 | LOW to MEDIUM: -38.9% YoY; derived additions INR M 2,347.7; 1.28x cover is adequate for services, but the fall is steep |
| "improving margins" (p.18) | No number. Core margin 12.4% (calc) vs 1.9% FY25 on the same basis (calc: 10,471.0 - 7,042.8 - 1,934.9 - 1,292.8 = 200.5) | FY26 | MEDIUM: direction true on cost lines (materials 67.3% to 60.2%; employees 18.5% to 14.5%), but the 27.0% headline is not run-rate |
| "continued growth in core services, selective upgrade participation, measured FGD EP rather than full EPC" (p.18) | None | FY27 onward | NOT TESTABLE from AR; brief's 85-90% / 11% guidance NOT FOUND IN DOCUMENT |
| "approximately 50% growth in the other OEM market segment" (p.18) | 50%, base not given | FY26 | UNVERIFIABLE; total product sales +18.9% (calc) |
| Durgapur scheme complete "within twelve months from the end of the reporting period" (Note 47(iii)) | by 31 Mar 2027 | 12 months | MEDIUM: approvals from shareholders, creditors, NCLT Mumbai pending (p.28) |
| Parent guarantees needed up to INR M 16,000 (Notice p.320) | 16,000 | AGM to AGM, max 15 months | Based on "existing order book, project pipeline" (inference: management expects peak bid support above current INR M 7,978 usage) |
| Cash-pool lending up to INR M 10,000 (Notice p.292) | 10,000 against INR M 4,500.0 today | to 35th AGM | Signals management expects to lend 2.2x the present balance (calc) |
| Dividend INR 7 per share (p.16) | 470.6 | FY26 final | Firm; 19.9% of PAT, 10.0% of CFO (calc) |

Note on the "improving margins" row: FY25 core EBITDA on the 12.4% basis (all other income out, ECL line out) is INR M 200.5, or 1.9% of revenue (calc). Stage 2 gives FY25 at 4.5% on its 16.1% basis (cost recoveries and rent kept). The two stage 2 bases stand. FY25 comparability also depends on the Durgapur re-presentation (INR M 604.8 of cost moved out of continuing).

### 4D Tone and credibility (1 low to 5 high)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | MD&A silent on demerger, ICD, one-offs, customer names, order inflow; Notice discloses the ICD guarantee, LM Wind financials and the PCG peak INR M 20,432 that the Notes do not |
| Consistency | 2 | Attrition 8.7% (p.94) vs turnover 71.11% (p.51); RoNW 0.69 vs ROE 0.73 (p.93 vs p.192); "no guarantee provided" (p.30) vs "Corporate Guarantee issued" INR M 7,977.6 (p.182); ICD limit approval dated 29 Mar 2025 postal ballot (p.30) vs 14 Aug 2025 AGM (p.320); CARO ii(b) vs Notice |
| Specificity | 2 | Technical project milestones are specific (Directors' Report p.15-19). Financial outlook is not |
| Accountability | 3 | Names risks, but no admission of the order-book fall or of dependence on group support |
| Capital allocation sense | 3 | Dividend resumed, no debt, cash lent to a creditworthy affiliate at a thin pick-up; Durgapur exit is rational for a services pivot (inference). Cash placed unsecured with the group treasury is not an operating use of capital |

**Contradictions vs Phases 1-3.** (1) "Healthy order backlog" vs RPO -38.9%. (2) "Shorter cash conversion cycles" vs inventory +69.9% and a one-time receivable release. (3) "Margin improving": direction fine; the reported figure is overstated by one-offs. (4) MD&A ratios vs Note 44. (5) Attrition vs BRSR.
**Phase 4 verdict: 🔴 Red Flag on disclosure quality only.** The accounting is not rated red. The MD&A omits every item that moves value, and at least three of its numbers disagree with other pages of the same report.
**Kill switch (informational):** a human reviewer would not have reason to stop, because the omissions are filled by the Notice and the notes. A reviewer would not rely on the MD&A.

---
## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board composition (31 Mar 2026; CG Report p.97-101)

| Director | Role | Since | Board attendance | Other directorships (listed) | Flags |
|---|---|---|---|---|---|
| Craig Martin Richards | Chairman, NED non-independent (GE Vernova Hydro Asia GM) | 14 Aug 2025 (Chairman 15 Aug 2025) | 5 of 6 (83%) | Nil | Promoter-group executive as Chairman; liable to retire by rotation |
| Puneet Bhatla | Managing Director | 1 Sep 2024 | 11 of 11 | Nil | Leads GE Steam Power India growth areas; 36 years' experience |
| Aashish Ghai | WTD and CFO | 22 Jul 2024 | 11 of 11 | Nil | Resigned effective 13 May 2026 |
| Shukla Wassan | Independent | 29 Nov 2021 | 11 of 11 | 2 other (India Glycols, Kwality Wall's) | Second term proposed (Notice Item 6); 4.4 years |
| Ashok Kumar Barat | Independent, Audit Chair | 1 Jun 2024 | 11 of 11 | 9 other directorships; 6 listed (Everest, Bata, Huhtamaki, Alembic, Aarti, Eveready) | 10 total seats with GVPIL; above the 8-seat flag; 8 committee memberships |
| Neeraj Kumar Nanda | Independent | 16 May 2025 | 10 of 10 | Nil | Power-sector experience (ABB, Alstom, BHEL, KEC) |
| Shrikar Thakur | WTD, additional director from 1 Jul 2026 (Notice Item 7) | 1 Jul 2026 | n/a | | Appointment needs member vote |

- Independents are 3 of 6 (50%). No independent exceeds 10 years. No attendance below 75%. Mahesh Palashikar attended 5 of 5 before retiring on 14 Aug 2025.
- Promoter-group cross-board: the Chairman is a GE Vernova executive; the Managing Director's career is inside GE/Alstom; Craig Richards also sits on the Audit Committee, NRC and Risk Committee (p.11, p.102, p.104, p.108). The Audit Committee has 3 independent members and the Chairman. Related-party approvals therefore rest on the 3 independents.
- Board met 11 times; Audit Committee 10; NRC 8; SRC 2; RMC 2; Strategy and Innovation 4 (CG p.98-109).
- The Board dissolved the Sustainability Committee and the Inclusion & Diversity Committee on 11 Feb 2026 and moved their matters to the Board and the NRC (p.25, L 1151-1167; CG p.109-110). CSR Committee was dissolved on 7 Nov 2024 (p.108).

### 5B Committees
Audit (Barat chair, Wassan, Nanda, Richards; all attendance 100%), NRC (Wassan chair; 8 meetings), SRC (Wassan chair, Bhatla, Ghai; 11 investor complaints received, 11 resolved), RMC (Richards chair; the Chief Risk Officer is an invitee). RMC met twice, on 16 Apr 2025 and 12 Nov 2025, 210 days apart (calc). The CG text says the 120-day gap rule was met "except in case of Risk Management Committee meeting" (p.99, L 6302-6303). I do not test the RMC gap against the Listing Regulations here. Two meetings a year is a low frequency for a company with this risk profile. 🟡 minor.

### 5C Compensation (CG p.105-106; Note 36 p.182; Annexure D p.38-39)

| Person | FY26 INR M | FY25 INR M | Ratio to median | Note |
|---|---|---|---|---|
| Puneet Bhatla, MD | 48.40 (salary 5.32, allowances 6.49, bonus 7.31, perquisites 26.85, retirals 2.43) | 30.90 | 20.59x | Includes RSU/ESOP exercise (+56.6%, calc); fixed pay +8.4%; 2.0% of PAT (calc) |
| Aashish Ghai, WTD and CFO | 10.06 | 5.80 | 4.28x | Resigned |
| Kamna Tiwari, CS | 5.4 | 5.3 | n/a | Resigned 2 Apr 2026 |
| Independent directors (3) | 4.44 / 4.50 / 4.07 (fees plus commission INR M 2.00 each) | 3.92 / 2.99 / nil | 1.89x to 1.91x | Commission +51.5% (Annexure D); shareholder approval for loss years (23 Jul 2024) |
| Chairman | nil | nil | n/a | Not entitled to compensation (CG p.116) |

Median employee remuneration +5.4%; average non-managerial increase 5.90%; 571 permanent employees (Annexure D p.39; BRSR p.50: 479 employees + 92 workers = 571 ✓). Workers other than permanent: 2,137 (BRSR p.50); the business leans on contract labour (inference). KMP pay total (MD, CFO, CS) INR M 63.9 = 2.7% of PAT (calc). ESOP: parent plans; no dilution. Promoter-family payroll: none (the promoter is a corporate group).

### 5D Shareholding (CG p.114; Directors' Report p.28)

| Holder | % | Shares |
|---|---|---|
| Promoter (GE Steam Power International BV) | 68.58 | 46,102,083 |
| Mutual funds | 0.15 | 101,461 |
| Insurance | 0.32 | 216,797 |
| FIIs | 1.25 | 843,602 |
| Resident individuals | 24.11 | 16,207,437 |
| Others | 5.59 | balance |

- Promoter holding unchanged at 68.58% (46,102,083 shares) for FY25 and FY26 with "no change up to the date of this report" (p.28, L 1401-1403). Ultimate holding changed from General Electric to GE Vernova Inc. on 2 Apr 2024. On 25 Jul 2024 the promoter withdrew its plan to exit and de-promoterise (p.28).
- **Pledge: NOT FOUND IN DOCUMENT.** The shareholding table has no pledge or encumbrance column. The Notes show deposits of INR M 55.5 pledged to banks, nothing on promoter shares.
- Institutional ownership is 2.1% (calc: 0.15 + 0.03 + 0.32 + 1.25 + 0.39 government + 0.01 foreign bodies corporate, rounded). Low institutional ownership is not a risk under house rules; it is noted.
- Promoter not selling. Dividend INR 7 per share pays the promoter INR M 322.7 (calc). The cash-pool ICD and the INR M 10,000 lending ceiling place company liquidity with a promoter-group entity.

### 5E Governance red-flag checklist

| Check | Finding | Anchor |
|---|---|---|
| Whistle-blower | 19 Code of Conduct policy concerns raised and closed; about 39% confirmed (about 7, calc); nature NOT DISCLOSED | Directors' Report p.29 (L 1522-1524) |
| SEBI or exchange actions | None in last three years | CG p.116 (L 7727-7730) |
| RPT committee | RPTs go to the Audit Committee; omnibus approval; MRPT approved by non-related members. FY26 MRPT approvals by postal ballot 4 May 2025: Powerstatic 1,478; GE Vernova Hydro 1,500; GE Renewable 1,500; LM Wind 600 and 10,500; GE Vernova Inc 40,000; NGSL 1,742 | Secretarial Audit p.35 |
| Auditor fee ratio | Non-audit below audit (1E) | Note 33 |
| CSR compliance | Not applicable (average net loss); voluntary INR M 0.8 | Note 37 |
| Section 143(12) fraud | None | p.27 (L 1304-1308); CARO xi |
| Material subsidiary auditor | No material subsidiary | CG p.116 |
| Disclosure | Directors' Report says "Your Company has not provided any guarantee" (p.30) while Note 36 labels INR M 7,977.6 "Corporate Guarantee issued"; direction is received per the Notice | p.30; p.182; Notice p.320 |
| Secretarial auditor | Changed to VKC & Associates (peer reviewed) from Hemant Singh & Associates; no qualifications | p.26-27; p.35 |
| IEPF | Delay of about two weeks in FY25 due to MCA portal outage (INR M 0.91) | Note 55 p.202 |
| Preference share capital | Authorised INR M 4,050 of preference capital unused | Note 19 p.159 |
| Interested-party loans | None to firms in which directors are interested | CG p.117 |

**Phase 5 verdict: 🟡 Watch.** Clean certificates, 50% independent board, full attendance for the independents and no regulatory penalties. Watch items: a promoter-group Chairman on the Audit Committee that approves the group cash pool, an independent Audit Chair with nine other boards, CFO and CS exits within six weeks of each other, the "not provided any guarantee" wording, and the limit approval-date disagreement. No promoter pledge or selling pattern found; pledge detail itself is absent.
**Kill switch (informational):** a human reviewer would not have reason to stop; governance flags are procedural.

---
## PHASE 6: DIRECTORS' REPORT AND FRONT MATTER (read last)

There is no Chairman's letter in AR26. The front matter is a cover notice (p.1), a cover theme "The Energy of Change" (p.2), the board and committee pages (p.6-12), five-year charts (p.13), events (p.14), then the Directors' Report (p.15 onward). The "Way Forward" (p.22) is the nearest thing to a strategy statement.

### 6A Narrative vs reality (5-7 claims)

| # | Claim (anchor) | What the financials show | Mark |
|---|---|---|---|
| 1 | "strategic focus on high-margin, cash-accretive opportunities with shorter cash conversion cycles" (p.18) | CFO INR M 4,692.5; receivable days 219 vs 409. But the cash is a one-off BHEL and receivable release and inventory is +69.9% | ✅ with caveat |
| 2 | "improving margins" (p.18) | Core margin 12.4% vs 1.9% last year (calc); reported 27.0% includes INR M 1,016.6 reversal | ✅ direction, ❌ magnitude |
| 3 | "healthy order backlog" (p.18) | RPO INR M 16,278, -38.9%; derived additions INR M 2,347.7 | ❌ |
| 4 | "secured a series of significant orders" (p.18) | One order quantified, INR M 430 (2.6% of RPO) | ❌ unquantified |
| 5 | "final settlement agreement ... with BHEL ... significant release of cash and bank guarantees" (p.22) | BHEL paid INR M 3,430.6 (Note 53); ECL reversal INR M 1,016.6 | ✅ |
| 6 | "approximately 50% growth in the other OEM market segment" (p.18) | No base disclosed; product sales +18.9% | ❌ unverifiable |
| 7 | Durgapur "transformation ... into a multiproduct manufacturing facility" (MD&A p.93) and "Durgapur Factory: cryogenic and pressure vessels, first order in the cryogenic segment" (p.21) | The Board approved the demerger of Durgapur to JSW on 18 Sep 2025 and held it for sale (p.28; Note 47(iii)) | ❌ contradicted (see 6E) |

### 6B Strategic priorities
Stated: core services and upgrades; installed-base engagement; selective emission-control work; parts exports; asset-light models; "measured approach to FGD equipment supply (EP) rather than full EPC" (p.18, p.22). Capital allocated: dividend INR M 470.6; capex INR M 21.3; the QPPL Leave and License and Contract Manufacturing Agreements for "a dedicated facility to support the Company's repairs business" (p.28, L 1480-1488), no value stated. Execution evidence: seven FGD operational acceptance certificates; BHEL and JPVL settlements; PG tests at NTPC North Karanpura and Gadarwara (p.22). Specificity: strategy is specific in direction, silent on targets.

### 6C Metrics showcased vs absent
Showcased: safety, Lean/Kaizen intensity "up 137%", engagement index, project milestones, MW and emission reductions. Absent: order inflow, core services share of revenue, backlog split, margin targets, customer names, cash conversion target, JSW share value, explanation of the profit step-up, return on the INR M 4,500.0 deployed.

### 6D Tone and priority drift vs AR25
AR25 listed named FGD projects by site with status (AR25 L 693-744) and an NGSL order book INR M 23,032 and inflow INR M 15,344 (L 1480). AR26 drops the FGD project table and moves to "core services, upgrades, asset-light". The tone shifted from project execution to services. AR26 adds two items not in AR25: the JSW demerger and the QPPL repairs facility.

### 6E Quiet Abandonment Check (mandatory)

| # | Opening claim (quote, anchor) | Where operations speak | Class | Materiality |
|---|---|---|---|---|
| 1 | "As part of the transformation of Durgapur manufacturing into a multiproduct manufacturing facility, various people initiatives ... non-coal products and services jobs" (MD&A p.93, L 5878-5884); Directors' Report p.21 shows a first cryogenic vessel order; BRSR p.47 cites the plant as 93% green zone | Note 47(iii) p.194 and Directors' Report p.28: Durgapur is being demerged to JSW, classified held for sale and discontinued; the MD&A and Way Forward never mention the Scheme | (a) implicit retraction | Material. The Durgapur business is the source of INR M 548.0 cost and INR M 247.0 internal billing. The thesis for the continuing company changes if supply from Durgapur is lost or repriced |
| 2 | "a measured approach to FGD equipment supply (EP) rather than full EPC undertakings" (p.18) and "FGD ... opportunity for equipment supply, retrofit execution, project management, commissioning" (MD&A p.92, L 5788-5791) | Notes show the legacy EPC FGD book closing out through settlements and a loss-order provision of INR M 223.8; RPO fell 38.9%; no new FGD order is quantified. The MD&A refers back to the FY25 report for the FGD market size (p.92) | (c) hedged retreat | Moderate. Scope of FGD revenue in the continuing business is not stated |
| 3 | "Strategic focus on ... asset-light models" with a new "dedicated facility to support the Company's repairs business" with QPPL (p.28) | Capex INR M 21.3; no capital stated for the repairs facility; QPPL does not appear in the notes or the related-party list | (b) silent drop | Low to moderate. A new facility with no cost, size or timeline |
| 4 | Sustainability and inclusion framed as strategic committees in the CG preamble ("non-mandatory committees which focus on strategy, innovation, sustainability, gender inclusion", p.97) | The Board dissolved the Sustainability and I&D Committees on 11 Feb 2026 (p.25) | (a) implicit retraction | Low (framework noise), but the CG preamble still describes them as existing |
| 5 | "Attrition ... 8.7% ... an improvement over the previous year" (p.94) | BRSR turnover for permanent employees 71.11% vs 28.05% (p.51) | (a) implicit retraction | Moderate. If 71.11% is carve-out related, say so; the AR does not |

---
## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top reasons |
|---|---|---|
| Value + Quality | WATCHLIST | (1) No price in the AR, so valuation NOT FOUND here; (2) ROE 73.1% and no debt, but built on one-offs and a large float; (3) core margin 12.4% is decent for services |
| GARP | WATCHLIST | See below |
| Turnaround | WATCHLIST leaning PASS | See below |
| Capex-led growth | FAIL | Capex INR M 21.3 = 0.17x depreciation; asset-light by design; no capacity programme |
| Cash flow compounder | FAIL on this evidence | CFO INR M 4,692.5 is a one-time release; FY25 CFO INR M 3,790.4 restated; FY24 CFO only 1,824.0; 95.9% went to a group deposit |
| Contrarian | WATCHLIST | Orders fall and a messy FY26 optic, but price and sentiment NOT FOUND IN DOCUMENT |
| Insider confidence | WATCHLIST | Promoter holds 68.58%, unchanged; exit plan withdrawn in July 2024 (p.28); no purchases; promoter-group treasury holds INR M 4,500.0 of company cash; MD pay includes RSU/ESOP of the parent |
| Guidance divergence | NOT TESTABLE from AR | No numeric guidance in the AR; the brief's 85-90% / 11% (unverified) and Q1/Q2 FY27 margins 14.5% / 9.8% sit outside this document. Test where the Q1/Q2 FY27 filings are read |

**GARP (full reasoning).**
- Growth: revenue +21.2% in FY26 but +0.8% in FY25 and a two-year CAGR of 10.5% (calc). RPO is 1.28x revenue and falling. Forward revenue visibility rests on RPO INR M 16,278 plus a core services run-rate that the AR does not break out.
- Earnings base for P/E: a clean FY26 earnings base must exclude the reversal (INR M 1,016.6), write-backs (240.9), insurance (184.2), group income that is not operating (ICD interest 199.8) and the JPVL settlement net effect (NOT STATED). Core EBITDA INR M 1,577.8 (calc) less depreciation 122.8 and finance cost 219.0 gives core PBT of about INR M 1,236.0 (calc), against reported INR M 3,399.0. That is 36.4% of reported (calc). The Durgapur cost shift may flatter this by up to INR M 247.0 (internal billing; stage 2).
- Quality of growth: gross margin rose 6.9 points (materials 67.3% to 60.2%) and employee cost fell 4 points (18.5% to 14.5%), both real and consistent with a shift to services and parts. Revenue growth is parts supply (raw material consumed +55.3%), so "services" means supply of spares, not high-margin labour only.
- Balance sheet optionality: INR M 8,473.1 net cash with the ICD; INR M 3,973.1 without. Roughly INR M 6,866.1 after the trust amount. Market capitalisation NOT FOUND IN DOCUMENT, so the share of price backed by cash cannot be set here.
- GARP fit: PASS on balance sheet, WATCHLIST on growth and on the earnings base. PEG cannot be computed from the AR.

**Turnaround (full reasoning).**
- Evidence of a turnaround: continuing loss before tax INR M (1,423.7) in FY24 to INR M (380.2) as printed in AR25 (INR M 224.6 as re-presented) to INR M 3,399.0 before exceptional items in FY26. Cash losses ended: CARO xvii INR M 824.15 in FY25, none in FY26. Equity rebuilt from INR M 573.5 to INR M 5,437.7. Two loss-making businesses sold and a third (Durgapur) on the way out. Bank debt cleared: INR M 3,100 repaid in FY24 (AR25 cash flow), nil debt of substance now.
- What is not proven: whether core earnings hold without one-offs. The turnaround so far is half portfolio surgery (carve-out gains INR M 2,953.3 in FY25), half release of old receivable allowances (INR M 1,016.6). Operating cost-line gains are real (materials and employee ratios). The order book is the open question.
- What would prove it: H1 FY27 results with core margin at or above 11% (the brief's stated normalised level; unverified) and RPO at or above INR M 16,278 with positive book-to-bill. Neither can be tested in the AR.
- Fit: the best-fit lens for the evidence in this AR.

---
## PHASE 8: FINAL VERDICT DASHBOARD

**Company snapshot.** GE Power India Ltd (NSE: GVPIL, BSE 532309), 68.58% held by GE Steam Power International BV (GE Vernova Inc. ultimate). FY26 revenue INR M 12,692.7 (+21.2%), PBT before exceptional INR M 3,399.0, PAT INR M 2,363.6, EPS INR 35.16, CFO INR M 4,692.5, equity INR M 5,437.7, RPO INR M 16,278, 571 permanent employees, ICRA BBB+ Stable. Business: services and parts for thermal power plants (boilers, turbines, generators, mills, automation, air quality control) with a legacy FGD book. Single segment. Durgapur plant being demerged to JSW Energy.

| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | 🟡 |
| 2 Notes | 🟡 |
| 3 Financial statements | 🟡 |
| 4 Risk and MD&A | 🔴 (disclosure quality) |
| 5 Governance | 🟡 |
| 6 Directors' Report and front matter | 🟡 (one quiet abandonment is material) |
| 7 Best-fit strategy | Turnaround |

**Overall quality score: 5.8 / 10** (four components at 25% each).

| Component | Score /10 | Basis |
|---|---|---|
| Governance | 6 | Clean certificates and 50% independents; promoter-group Chairman on the committee that approves the group cash pool; CFO and CS exits; wording gaps |
| Accounting quality | 6 | Stage 2 score reconciled; CARO vs Note 39 gap and Note 26 label defect hold it; no proven misstatement |
| Balance sheet | 7 | No debt, current ratio 1.34, INR M 8,473.1 net cash; offset by unsecured INR M 4,500.0 group deposit, parent-guarantee dependence and a INR M 9,607.3 float |
| Earnings quality | 4 | 55.2% of profit step-up is reversal plus other income; 25.1% of PBT is group-sourced; CFO one-time and 95.9% lent out |

**Top 3 strengths**
1. Debt-free balance sheet with INR M 4,244.6 cash, current ratio 1.34, cash losses ended (Balance sheet p.131; CARO xvii).
2. Real cost-line gains: materials 67.3% to 60.2% of revenue; employee cost 18.5% to 14.5% (calc from p.132); revenue +21.2%.
3. BHEL and JPVL disputes closed with cash (INR M 3,430.6 and INR M 250) and bank guarantees released (Note 53-54; p.22); ICRA upgrade to BBB+ (CG p.115).

**Top 3 red flags**
1. Profit quality: INR M 1,016.6 reversal, INR M 240.9 write-backs, INR M 851.9 group-sourced income; core margin 12.4% against reported 27.0% (Notes 28, 33, 36, 53).
2. Group dependence: unsecured INR M 4,500.0 demand deposit with a group treasury (106% of cash), guarantee for it only proposed; INR M 16,000 of bank guarantees from one parent whose majority ownership banks require (Note 16; CARO iii; Notice p.317-324).
3. Order book: RPO -38.9% to INR M 16,278, derived additions INR M 2,347.7, and an MD&A that calls it "healthy" and never mentions the Durgapur demerger (Note 27; p.18; p.88-95).

**Key monitorables (next quarter)**

| Metric | Threshold | Where | Why |
|---|---|---|---|
| Core EBITDA margin excluding other income and any allowance reversal | At or above 11% (brief's normalised level, unverified) | Q3 FY27 results, P&L and notes on exceptional/other items | Tests whether FY26 12.4% is run-rate |
| RPO and order inflow | RPO at or above INR M 16,278; inflow at or above revenue | Investor presentation, concall; AR27 Note 27 | Revenue visibility after a 38.9% fall |
| AGM 14 Aug 2026 votes on Items 8, 9, 10 and the PCG in place | Items passed; PCG covers 100% of ICD balance; balance at or below cap | Stock exchange voting results; Q3 FY27 notes | Closes the unsecured-loan gap. Voting outcome NOT FOUND in this corpus |
| ICD balance and classification | Balance at or below INR M 4,500.0; shown in the financial-instrument and credit-risk notes | Q2/Q3 FY27 balance sheet and loan note | Single largest non-operating asset |
| CFO excluding group-deposit movements | CFO at or above PAT; inventory days at or below 71; receivable days at or below 219 | Half-year cash flow | One-time release not repeated |
| Durgapur scheme | NCLT sanction; supply agreement and price; cost of materials trend | Exchange filings; scheme documents | Post-demerger cost of INR M 247.0 supply |
| Note 26 provision roll-forward | Warranty "slump sale" label explained; warranty provision by head | Half-year notes | Possible release up to INR M 299.2 |
| Disputed taxes | CARO vii(b) total reconciled to Note 39 | AR27 | INR M 3,446.2 gap |
| KMP and attrition | Permanent CFO and CS in seat; one attrition figure | Corporate governance filing; BRSR | Continuity after exits |
| Top two customers | At or below 38.6% | AR27 Note 35 | Concentration |

**One-line verdict.** Best fit: Turnaround. A cash-rich parent-captive thermal services business whose FY26 margin and cash are flattered by one-offs and a group deposit, and whose order book has shrunk.

---
## New findings not in stage 2 (summary for downstream stages)
1. CARO vii(b) disputed dues INR M 8,022.1 gross vs Note 39 INR M 4,575.9 (gap INR M 3,446.2).
2. CARO ii(b) says no working capital facility sanctioned; the Notice says INR M 610 fund-based sanctioned and INR M 330 drawn.
3. Existing INR M 4,500.0 ICD is unsecured per Note 16 and CARO iii(a); the guarantee is proposed in Notice Item 10.
4. FY25 CFO re-presented from INR M 3,196.5 to INR M 3,790.4; Durgapur drain INR M 349.5 now in financing.
5. Brief's royalty Rs 13.21 cr = INR M 132.1 = AR25 original FY25 line.
6. MD&A attrition 8.7% vs BRSR turnover 71.11%; MD&A RoNW 0.69 vs Note 44 ROE 0.73.
7. MD&A and Way Forward omit the JSW demerger and describe Durgapur as being transformed.
8. QPPL repairs facility (Leave and License, contract manufacturing) appears only in the Directors' Report.
9. Approval date of the INR M 4,500 s.186 limit differs: postal ballot 29 Mar 2025 (p.30) vs 33rd AGM 14 Aug 2025 (p.320).
10. NGSL FY26 inflow INR M 6,182 vs INR M 15,344 FY25 (-59.7%).
11. AR chart net worth INR M 4,829 excludes capital reserve INR M 609.0.
12. Risk Management Committee met only twice (16 Apr 2025, 12 Nov 2025; 210 days apart, calc).
13. Secretarial Audit (p.35) lists MRPT approvals of 4 May 2025 (GE Vernova Inc INR M 40,000; LM Wind INR M 600 and INR M 10,500) with no purposes; the s.186 loan limit and the Reg 23 approval are separate.

```yaml
stage: B03-ardeep
company: "GVPIL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "concalls: no Q1 FY27 or Q2 FY27 earnings-call transcript"
  - "shareholding: screener-derived table only; filed pattern and pledge detail absent (AR26 CG p.114 has no pledge column; pledge NOT FOUND IN DOCUMENT)"
  - "screening: only Data_Sheet CSVs populated"
  - "research: none; prospectus not expected (long-listed)"
  - "notes: FY24 comparatives from AR25 as first reported; not like-for-like with continuing FY25/FY26"
  - "notes: continuing-basis FY25 related-party table NOT FOUND (Note 36 FY25 column not re-presented)"
  - "notes: contingent liability stage/forum, customer names, Durgapur demerger consideration value, MAT credit, loss expiry schedule NOT FOUND IN DOCUMENT"
  - "notes: royalty booking location for INR M 310.0 gap NOT STATED; P&L effect of Note 26 slump-sale deductions NOT STATED; post-demerger Durgapur supply price NOT FOUND"
  - "ar: no numeric FY27 guidance, no core services backlog split, no order inflow in AR26; brief's 85-90% / 11% guidance NOT FOUND IN DOCUMENT"
  - "ar: outcome of AGM 14 Aug 2026 votes on Items 8, 9, 10 not in corpus"
  - "ar: reconciliation of CARO vii(b) INR M 8,022.1 to Note 39 INR M 4,575.9 NOT STATED"
flags:
  - {type: FLAG-CASH, reason: "FY26 CFO INR M 4,692.5 is a one-time receivable release (+5,136.0) with customer advances and billing in excess down 2,106.6; 95.9% (4,500.0) moved to an unsecured group deposit; FY25 CFO re-presented upward by INR M 593.9 (3,196.5 to 3,790.4) with Durgapur drain INR M 349.5 now in financing"}
  - {type: FLAG-PROMOTER-PRELIM, reason: "No pledge or selling pattern found (promoter 68.58% unchanged; pledge detail NOT FOUND IN DOCUMENT). Preliminary note only: INR M 4,500.0 unsecured demand deposit with promoter-group cash-pool header; ceiling to rise to INR M 10,000; bank lines depend on GEV majority ownership; promoter exit plan withdrawn 25 Jul 2024. Full promoter verdict from B08"}
  - {type: FLAG-EARNINGS, reason: "ECL reversal 1,016.6 plus other income increase 433.5 = 55.2% of the 3,174.4 profit step-up; group-sourced other income 851.9 = 25.1% of PBT before exceptional; core margin 12.4% vs reported 27.0%"}
  - {type: FLAG-ORDERS, reason: "RPO INR M 16,278 vs 26,623 (-38.9%); derived FY26 additions INR M 2,347.7; AR calls it healthy; NGSL inflow 6,182 vs 15,344 (-59.7%)"}
  - {type: FLAG-CARO-RECON, reason: "CARO vii(b) disputed dues gross INR M 8,022.1 (net of deposits 7,658.3) vs Note 39 contingent liabilities INR M 4,575.9; gap INR M 3,446.2 unreconciled; CARO ii(b) says no working capital facility sanctioned vs Notice INR M 610 fund-based sanctioned"}
  - {type: FLAG-DISCLOSURE, reason: "MD&A omits JSW demerger, ICD, profit step-up and customer names; MD&A attrition 8.7% vs BRSR turnover 71.11%; MD&A RoNW 0.69 vs Note 44 ROE 0.73; Directors' Report says no guarantee provided vs Note 36 'Corporate Guarantee issued' 7,977.6"}
phase_verdicts: {p1: "YELLOW", p2: "YELLOW", p3: "YELLOW", p4: "RED (disclosure quality only)", p5: "YELLOW", p6: "YELLOW", p7_best_fit: "Turnaround"}
overall_quality: 5.8
quality_components: {governance: 6, accounting: 6, balance_sheet: 7, earnings: 4}
kill_switch_notes:
  - "p1: informational only. Reviewer would not stop: unmodified opinion, CARO clean on fraud/default/arrears. Open: CARO vii(b) INR M 8,022.1 vs Note 39 INR M 4,575.9; CARO ii(b) vs Notice; single unchanged KAM"
  - "p2: informational only. No impairment/covenant/default signal. Open: unsecured INR M 4,500.0 group loan; Note 26 slump-sale label; contingent-liability gap"
  - "p3: informational only. Reviewer would ask whether FY27 can repeat margin and cash without the INR M 1,016.6 reversal and the INR M 5,136.0 receivable release"
  - "p4: informational only. Omissions are filled by the Notice and notes; do not rely on the MD&A"
  - "p5: informational only. Procedural governance flags; no pledge or selling pattern found"
triple_pass_verification:
  verified: 15
  discrepancies:
    - {finding_rank: 2, triple_pass_value: "55.3% of profit step-up", ar_value: "55.2% (1,753.5 / 3,174.4 = 55.24%, calc)", note_ref: "Notes 28, 33; P&L p.132; rounding only"}
    - {finding_rank: 9, triple_pass_value: "84.2% of net worth (equity 5,437.7)", ar_value: "94.8% on the AR 5-year-chart net worth INR M 4,829 (equity less capital reserve 609.0); base difference, not an error", note_ref: "Note 39 p.185; chart p.13"}
missing_risks:
  - {risk: "Unsecured INR M 4,500.0 demand deposit with group cash-pool header (21.4% of assets, 106% of cash)", evidence: "Note 16 p.158; CARO iii(a) p.128; balance sheet p.131"}
  - {risk: "Single-guarantor dependence; banks require GEV majority ownership; INR M 16,000 guarantees needed", evidence: "Notice p.320, p.324"}
  - {risk: "Order-book contraction RPO -38.9%", evidence: "Note 27 p.166"}
  - {risk: "Customer concentration, top two 38.6%", evidence: "Note 35 p.176"}
  - {risk: "Durgapur demerger execution and post-demerger cost of INR M 247.0 internal supply; MD&A silent", evidence: "Note 47(iii), (vi) p.194-198; Directors' Report p.28"}
  - {risk: "One-off earnings (reversal 1,016.6; write-backs 240.9; insurance 184.2; JPVL 250)", evidence: "Notes 28, 33, 53, 54 p.167-168, p.202"}
  - {risk: "Disputed taxes CARO INR M 8,022.1 vs Note 39 INR M 4,575.9", evidence: "CARO p.129; Note 39 p.185"}
  - {risk: "KMP continuity: CFO/WTD and CS resigned", evidence: "Directors' Report p.25"}
  - {risk: "Working-capital reversal: inventory +69.9%, customer advances down", evidence: "Balance sheet p.131; Note 25 p.164"}
  - {risk: "Amount held in trust INR M 1,607.0, Supreme Court pending", evidence: "Note 24 p.163; Note 43 p.190"}
guidance_table:
  - {claim: "healthy order backlog", number: "RPO INR M 16,278 (1.28x revenue, calc)", timeframe: "Mar-26", credibility: "LOW-MEDIUM: -38.9% YoY"}
  - {claim: "improving margins", number: "none stated; core 12.4% (calc) vs 1.9% FY25 same basis; reported 27.0%", timeframe: "FY26", credibility: "MEDIUM: direction true, magnitude overstated by one-offs"}
  - {claim: "continued growth in core services; measured FGD EP not EPC", number: "none", timeframe: "FY27 onward", credibility: "NOT TESTABLE; brief's 85-90% execution and 11% margin NOT FOUND IN DOCUMENT"}
  - {claim: "approximately 50% growth in other OEM market segment", number: "50%, base not given", timeframe: "FY26", credibility: "UNVERIFIABLE; product sales +18.9% (calc)"}
  - {claim: "Durgapur scheme completes within 12 months of year end", number: "by 31 Mar 2027", timeframe: "12 months", credibility: "MEDIUM: shareholder, creditor, NCLT approvals pending"}
  - {claim: "Parent guarantees needed up to INR M 16,000", number: "16,000 vs 7,977.6 used", timeframe: "to 35th AGM", credibility: "MEDIUM: peak FY26 20,432"}
  - {claim: "cash-pool lending up to INR M 10,000", number: "10,000 vs 4,500.0 today", timeframe: "to 35th AGM", credibility: "signals 2.2x lending intent (calc)"}
monitorables:
  - {metric: "Core EBITDA margin ex other income and ex allowance reversal", threshold: ">=11% (brief level, unverified)", where: "Q3 FY27 results and notes", why: "tests whether FY26 12.4% is run-rate"}
  - {metric: "RPO and order inflow", threshold: "RPO >= INR M 16,278; inflow >= revenue", where: "investor presentation, concall, AR27 Note 27", why: "revenue visibility after -38.9%"}
  - {metric: "AGM Items 8, 9, 10 outcome and PCG covering ICD", threshold: "passed; PCG 100% of balance", where: "exchange voting results; Q3 FY27 notes", why: "closes unsecured-loan gap; outcome NOT FOUND in corpus"}
  - {metric: "ICD balance and note treatment", threshold: "<= INR M 4,500.0 and included in financial-instrument/credit-risk notes", where: "half-year balance sheet and notes", why: "largest non-operating asset"}
  - {metric: "CFO excluding group-deposit movements; inventory days; receivable days", threshold: "CFO >= PAT; inventory days <= 71; receivable days <= 219", where: "half-year cash flow", why: "one-time release not repeated"}
  - {metric: "Durgapur scheme: NCLT sanction, supply price, cost of materials", threshold: "sanction by 31 Mar 2027; supply cost disclosed", where: "exchange filings", why: "post-demerger cost of INR M 247.0 supply"}
  - {metric: "Warranty provision by head; slump-sale label", threshold: "explained; no release above INR M 299.2", where: "half-year notes", why: "Note 26 label defect"}
  - {metric: "CARO vii(b) vs Note 39 reconciliation", threshold: "gap explained", where: "AR27", why: "INR M 3,446.2 gap"}
  - {metric: "Permanent CFO and CS; one attrition figure", threshold: "in seat; 8.7% vs 71.11% reconciled", where: "CG filing; BRSR", why: "continuity"}
  - {metric: "Top two customers share", threshold: "<= 38.6%", where: "AR27 Note 35", why: "concentration"}
ar_new_downstream_entities:
  - {name: "JSW Energy Limited", where_in_ar: "Directors' Report p.28; Note 47(iii) p.194", entity_type: "demerger counterparty (receives Durgapur; issues shares 10 for 139)"}
  - {name: "Quality Profiles Private Limited (QPPL)", where_in_ar: "Directors' Report p.28 (L 1480-1488)", entity_type: "repairs-facility partner (Leave and License; Contract Manufacturing Agreement)"}
  - {name: "GE Vernova (Switzerland) GmbH", where_in_ar: "Note 36 p.180", entity_type: "RPT counterparty: other income INR M 188.6 (FY25 nil)"}
  - {name: "Monnet Power", where_in_ar: "Directors' Report p.18, MD&A p.91", entity_type: "named customer: 500 MW generator stator repair, value not stated"}
  - {name: "Adani Kawai (Shanghai Electric SEC 660 MW turbine IP inner casing)", where_in_ar: "Directors' Report p.19", entity_type: "named first-time customer order, value not stated"}
  - {name: "RattanIndia Power", where_in_ar: "Directors' Report p.19", entity_type: "named first-time customer: LP last-stage blades 270 MW, value not stated"}
  - {name: "RRUVNL Kalisindh", where_in_ar: "Directors' Report p.19, p.21", entity_type: "named customer: ESP refurbishment and stator rewind, value not stated"}
strengths_top3:
  - "Debt-free balance sheet: cash INR M 4,244.6, current ratio 1.34, cash losses ended (p.131; CARO xvii)"
  - "Cost-line gains: materials 67.3% to 60.2% and employee cost 18.5% to 14.5% of revenue; revenue +21.2% (p.132)"
  - "BHEL (INR M 3,430.6) and JPVL (INR M 250) disputes closed with cash; ICRA upgrade to BBB+ (Notes 53-54; CG p.115)"
red_flags_top3:
  - "Profit quality: reversal 1,016.6, write-backs 240.9, group income 851.9; core margin 12.4% vs reported 27.0%"
  - "Group dependence: unsecured INR M 4,500.0 deposit with promoter-group treasury (106% of cash), guarantee only proposed; INR M 16,000 bank guarantees from one parent"
  - "Order book RPO -38.9% to INR M 16,278 while MD&A says healthy and omits the Durgapur demerger"
best_fit_strategy: "Turnaround"
one_line_verdict: "Turnaround: cash-rich parent-captive thermal services business; FY26 margin and cash flattered by one-offs and a group deposit; order book shrunk 38.9%."
analyst_note: "Three AR-only results stage 2 could not reach. (1) The INR M 4,500.0 ICD was unsecured at 31 Mar 2026 per Note 16 header and CARO iii(a); the Notice's 'secured by PCG' reads as the proposed INR M 10,000 guarantee (Item 10), so coverage starts after the 14 Aug 2026 AGM vote (outcome not in corpus). (2) CARO vii(b) lists INR M 8,022.1 of disputed dues against Note 39's INR M 4,575.9; the gap (3,446.2) is larger than the whole contingency provision (1,901.3). (3) FY25 CFO was re-presented up INR M 593.9 when Durgapur funding moved to financing, so FY26 CFO is continuing-only. Brief's Rs 13.21 cr royalty = INR M 132.1 = AR25 original line. Brief's 85-90% / 11% FY27 guidance and the Rs 1,218 cr core backlog are NOT in the AR; INR M 1,218.6 in Note 34 is an unrelated PF-trust item."
```


---
ORCHESTRATOR ERRATUM (2026-11-15, appended; the stage agent cannot edit its own report): in section 3B the FY26 "other assets" row prints a wrong cell value. The stage reports the correct figure as INR M 1,601.4, with totals tying to INR M 20,995.6. Read the correcting note beneath that table.
