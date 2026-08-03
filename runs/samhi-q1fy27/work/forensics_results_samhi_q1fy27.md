# A3 FORENSIC NOTES — SAMHI Hotels Limited (SAMHI) — Q1 FY27 (quarter ended 30 June 2026) — DOCTYPE: RESULTS

Inputs read verbatim: A1 extract `extract_results_samhi_q1fy27.txt` (14 pages; pages 8/9/13/14 OCR-substituted) and A2 ledger `ledger_results_samhi_q1fy27.md`.
Ledger reconciliation: 100% of A2 rows read at their cited lines (Sections 1A/1B notes, 2A/2B/2C line items, 3 PAT-gap, 4 agenda, 5A/5B annexures, 6A/6B auditor paras, 7 entities, 8 signatures, 9 zero-standing, 10 flags).
Monitoring checklist: EMPTY (new company, no companies/SAMHI.md, no Notion page). No tripwires fabricated.
Unit note: source is INR million; Rs Crore = million x 0.1.

**Reconciliation exception surfaced (load-bearing):** A2 Section 3 asserts standalone Q1 FY27 PAT ~Rs 247 cr (2,467.85 mn). Reading the cited rows, the standalone Q1 FY27 cells at lines 459/461/467/473 are all OCR-garbled, and **2,467.85 belongs to the Q4 FY26 (31 March 2026) column**, not the current quarter. The unambiguous standalone Q1 FY27 basic EPS = 0.05 (line 487; corroborated line 499) implies standalone Q1 FY27 PAT ≈ 0.05 x 222.13 mn shares ≈ 11 mn ≈ **Rs 1.1 cr**, corroborated by standalone TCI 12.43 mn (line 481). The A2 "standalone 10x consolidated" framing is therefore an OCR column-shift artifact; the true relationship is inverted (standalone << consolidated). Carried into F2.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / cite | short verbatim quote | classification | forward implication |
|----|-------|----------------|-------------|----------------------|----------------|---------------------|
| A3-F2a | F2 | Sec 3 PAT-gap; 2A row 12 / 2B rows 12,15a | L473 (std), L487 (std EPS), L743/L758 (consol) | "Profit for the period/year (10+11) PA 2,467.85 458,88 3,843.37" / "Basic (INR) 0,05" | AMBIGUOUS | A2's Rs 247 cr standalone PAT is a Q4 FY26 column mis-read; true standalone Q1 FY27 PAT ~Rs 1.1 cr (EPS 0.05) is FAR BELOW consolidated ~Rs 24.93 cr — normal holdco. A4 to confirm quantum + current-qtr standalone exceptional from clean PDF. |
| A3-F2b | F2 | Sec 2C composition flag | L529-533 (std), L820-824 (consol); L473 vs L749 | "Profit on sale of investment ... 974.93" (std) vs "Reversal of impairment in value of property, plant and equipment ... 268.93" (consol) | AMBIGUOUS | S-vs-C PAT relationship flips period to period (Q1 FY26 std 458.88 > consol 192.16; Q1 FY27 std ~12 < consol 249.27) driven by standalone investment-level exceptionals that eliminate on consolidation. Current-qtr standalone exceptional cell garbled — verify it is genuinely near-nil. |
| A3-F4 | F4 | 6A para 5; 6B para 5 | L399-400 (std), L633-635 (consol) | "the Company's share in the net loss of Rs. 7.38 million ... in respect of a partnership firm, whose interim financial information has not been reviewed" | FORWARD-SIGNAL | Unreviewed partnership-firm loss Rs 7.38 mn = ~60% of standalone Q1 FY27 PAT (~12 mn). Consolidated: 3 unreviewed subs, net loss Rs 17.14 mn = ~6.9% of consol PAT 249.27 (below 10% but a loss). No prior-period trend (new co). Partnership = RARE India (newly consolidated). A4: quality/quantum of unreviewed loss-making entities. |
| A3-F6 | F6 | Sec 4 items 3-5; notes 7/8 | L263-264, L102-104, L540, L833-834, L68-88 | "Indicative time period for completion of the acquisition; By 30* August,2026"; "The remaining 15% interest is proposed to be acquired subsequently"; "the purchase price allocation ('PPA'), is currently in progress" | FORWARD-SIGNAL | Dated/dateable commitments feed Role 5 promise-vs-delivery + FTTCP catalyst timeline. See Commitment Register. |
| A3-F7 | F7 | Sec 4 item 3 narrative (L220 cross-ref) | L80-88 | "prepared to operate in an increasingly volatile geo-political environment"; "The timing and terms for such infusion is dependent on prevailing market conditions" | AMBIGUOUS | Fundraise rationale embeds macro/geo-political + market-condition hedges. Pre-emptive framing that a Rs 750 cr raise may be opportunistic/conditional. A4: is dilution imminent or contingent? |
| A3-F8 | F8 | 2A rows 9a-9c; 2B rows 9a-9c | L463-465 (std), L739-741 (consol) | std "Current tax / Deferred tax" nil all four periods; consol "Deferred tax 78.06 3,302.39 38.67 2,995.45" | FORWARD-SIGNAL | Standalone tax = nil across ALL four periods incl Q4 FY26 (PBT 2,467.85) and FY26 (PBT 3,897.88) — exceptional gains treated as exempt/capital, zero deferred tax. Consolidated Q4 FY26 shows ~Rs 330 cr deferred-tax credit (total tax (3,300.81)) = DTA recognition / carryforward = future ETR step-up risk. Q1 FY27 consol ETR ~22.3% (73.06/327.33). |
| A3-F10 | F10 | 2A row 15,17a-b; Sec 4 items 2-3 | L482, L487-488, L60-76 | "Paid up equity share capital ... 222,13 222.13 221.21 222.13"; "increase in Authorized Share Capital ... from INR 25,00,00,000 ... to INR 29,00,00,000" | FORWARD-SIGNAL | Paid-up rose 221.21->222.13 mn (Jun25->Mar26, +0.92 mn shares, likely ESOP). Persistent basic>diluted spread = live dilutive instruments. Authorized capital lifted 25->29 cr shares SPECIFICALLY to enable Rs 750 cr raise (equity/warrants/CCD/CCPS) = material forward dilution. |
| A3-F13a | F13 | Sec 4 item 4 | L102-104 | "Approved to hold the 16 (Sixteenth) Annual General Meeting ... on Monday, 31 ... August 2026 & ... the Board's Report for the financial year 2025-26" | FORWARD-SIGNAL | Board's Report FY25-26 approved => full Annual Report drops within weeks. Schedule Role 6 AR Deep Dive event (~late Aug 2026). |
| A3-F13b | F13 | Sec 4 items 2-3 | L60-88 | "enabling resolution for raising of funds for an aggregate amount not exceeding INR 750,00,00,000" | FORWARD-SIGNAL | Capital-raising enabling resolution + authorized-capital headroom = funding round foreshadowed; QIP/preferential/private placement on the table, timing market-dependent. |
| A3-F13c | F13 | Sec 4 item 5; Annexure B | L106-121, L263-264, L302-319 | "Approved the acquisition of ... 100% ... of Itmenaan Lodges Private Limited ... for an aggregate cash consideration of INR 12,00,00,000" | FORWARD-SIGNAL | New M&A: Rs 12 cr (up to Rs 25 cr incl capex) boutique-luxury hotel in RARE India portfolio; completion by 30 Aug 2026; enters consol scope next quarter. Target income declining (FY24 88.99 lakh -> FY26 69.76 lakh) on tiny base. |
| A3-F14 | F14 | 1A note heading | L513 | "Notes to the Statement of unaudited standalone financial results for the quarter and year ended 31 March 2026" | NEUTRAL-FACT | Standalone notes heading mis-dated "quarter and year ended 31 March 2026" on a 30 June 2026 filing (consolidated heading L802 is correct). Stale copy-paste; individually immaterial governance data point. |
| A3-F15 | F15 | Sec 7 entities 16-18 | L698-700 | "SAMHI Skyline Private Limited (from 16 January 2026)"; "RARE India (from 22 April 2026)"; "(formerly known as ACIC Advisory Private Limited)" | FORWARD-SIGNAL | Two consolidation-scope additions (SAMHI Skyline; RARE India partnership, 55% control, PPA provisional, 15% still to acquire, unreviewed/loss-making) + one rename (ACIC Advisory -> SAMHI Hospitality Ventures). No prior ledger for cross-quarter diff; flagged on document's own effective dates. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis |
|-------|--------|-------|
| F1 ZERO-VALUE STANDING | PASS | All 12 zero-standing rows read at L463-465,470,478,746,185-209,259-261. Tax-discontinued/OCI-tax + Annexure "Not Applicable" rows are standard template/format lines. The one live oddity — standalone current/deferred/total tax nil across ALL periods incl profitable ones — is escalated to F8, not double-counted here. |
| F2 STD vs CONSOL DECOMP | **FINDING** | A3-F2a/b. A2's Rs 247 cr standalone PAT is a Q4 FY26 column mis-read; standalone Q1 FY27 PAT ~Rs 1.1 cr (EPS 0.05, L487) << consolidated Rs 24.93 cr (L743); gap direction inverted and swings >5pp across periods on standalone investment-level exceptionals. |
| F3 SHELL-ENTITY | PASS | Consol cost lines (materials 211.75, employee 502.07, D&A 308.83) >> standalone (12.20/124.10/34.20) at L724-732 vs L448-456 => subsidiaries operate; not shells. Three unreviewed subs (rev Rs 1.91 mn, L634) are near-dormant but no Going Concern EoM to reconcile; routed to F4/F15. |
| F4 UNAUDITED CONTRIBUTION | **FINDING** | A3-F4. Standalone unreviewed partnership-firm loss Rs 7.38 mn ~= 60% of standalone PAT; consol 3 unreviewed subs net loss Rs 17.14 mn ~= 6.9% of consol PAT. No prior trend (new co). |
| F5 GOING CONCERN / EoM | PASS | Both auditor conclusions unmodified/clean (L378-383 std, L625-631 consol); no Going Concern or Emphasis-of-Matter paragraph in either report. New-company coverage, no prior quarter to verbatim-diff. Nothing to flag. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | A3-F6. Lexicon hits: "proposed to be acquired" (L540), "is currently in progress" (L833), completion "By 30 August 2026" (L263), AGM "31 August 2026" (L102), "will be in consultation" (L88), multiple "board has approved" (items 2/3/5). See Commitment Register. |
| F7 HEDGE MINING | **FINDING** | A3-F7. "increasingly volatile geo-political environment" (L80), "dependent on prevailing market conditions" (L86), pervasive "subject to ... approval of the shareholders" (L65,75). Macro/market hedges wrapped around the fundraise rationale. |
| F8 TAX FORENSICS | **FINDING** | A3-F8. Standalone tax nil all periods vs 25.17% statutory despite large book profits; consol Q4 FY26 ~Rs 330 cr deferred-tax credit = DTA recognition => future ETR step-up. "tax adjustments relating to earlier years": none found. |
| F9 OCI FORENSICS | PASS | Re-measurement DBO tiny: consol Q1 FY27 (0.47) vs full FY26 (3.22) at L752 — single-quarter swing does NOT exceed prior year; no assumption-change signal. Standalone amounts <=0.25 (L477). |
| F10 SHARE COUNT / DILUTION | **FINDING** | A3-F10. Paid-up 221.21->222.13 mn corporate action (L482); persistent basic>diluted spread (L487-488) = live instruments; authorized capital 25->29 cr shares to enable Rs 750 cr raise = forward dilution. |
| F11 RESERVES / NET WORTH | PASS | Other equity + paid-up ties internally: standalone 32,275.07+222.13 (L483/482); consol 21,599.67+222.13 (L770/769). Standalone net worth exceeds consol by ~Rs 1,068 cr (impairment-reversal of investment in subs vs eliminated on consol) — reconciles to subsidiary accumulated losses. No third-party anchor (rating/slide) in a results-only filing to trigger the >5% test. |
| F12 SEGMENT FORENSICS | PASS | Single reportable segment "developing and running of hotels" per Note 4 (L522 std, L813 consol); no segment asset/liability lines disclosed to trend. Nothing to flag. |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | A3-F13a/b/c. Four items beyond results: authorized-capital increase (item 2), Rs 750 cr fundraise enabling resolution (item 3), AGM 31 Aug 2026 + Board's Report FY25-26 => AR imminent (item 4), Itmenaan Lodges M&A (item 5). |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | A3-F14. Standalone notes heading mis-dated "quarter and year ended 31 March 2026" (L513) on a 30 June 2026 filing; consol heading correct (L802). Notes "Limited Review" matches auditor letter (no note/letter mismatch). |
| F15 ENTITY LIST DIFFS | **FINDING** | A3-F15. SAMHI Skyline (from 16 Jan 2026) + RARE India (from 22 Apr 2026) additions; ACIC Advisory -> SAMHI Hospitality Ventures rename (L698-700). Clean Max Nile 49% held but explicitly NOT an associate/not consolidated (L541/835). |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results filing; no investor presentation in scope. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results filing; no transcript in scope. Monitoring checklist empty (new company). |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Complete acquisition of 100% Itmenaan Lodges Pvt Ltd (Rs 12 cr, up to Rs 25 cr incl capex) | By 30 Aug 2026 | Annexure B row 6, L263-264 | initiated (board-approved; SPA to be executed) |
| Acquire remaining 15% interest in RARE India | "subsequently" (no fixed date) | Std Note 8 L540 / Consol Note 7 L831 | underway (55% control taken 22 Apr 2026) |
| Finalize RARE India purchase price allocation (Ind AS 103) | Provisional now; within 12 months (~by 22 Apr 2027) | Consol Note 7 L833-834 | in progress |
| Hold 16th AGM; put fundraise + authorized-capital resolutions to shareholders | 31 Aug 2026 | Board letter item 4 L102-103 | approved / scheduled |
| Publish Board's Report FY2025-26 (=> full Annual Report) | Weeks (approved 03 Aug 2026) | Board letter item 4 L104 | approved (AR publication pending) |
| Raise up to Rs 750 cr (equity/warrants/CCD/CCPS) for capex + acquisitions | Market-dependent; post-AGM approval | Board letter item 3 L68-88 | initiated (enabling resolution) |
| Increase authorized capital 25 cr -> 29 cr shares | Post-AGM shareholder approval | Board letter item 2 L60-66 | board-approved, shareholder-pending |

---

## NOTES FOR A4 (questions to generate)

- **A3-F2 (AMBIGUOUS):** Reconcile from the clean source PDF — confirm standalone Q1 FY27 PAT (~Rs 1.1 cr per EPS 0.05) and whether the current-quarter standalone exceptional-items line is genuinely near-nil (Q1 FY26 profit-on-sale-of-investment 974.93 and Q4 FY26 impairment-reversal 2,508/3,250.87 sat in prior columns). A2 Section 3's Rs 247 cr standalone figure should be corrected in downstream memory.
- **A3-F7 (AMBIGUOUS):** Is the Rs 750 cr raise imminent or opportunistic? "Dependent on prevailing market conditions" + "geo-political environment" hedging suggests optionality, but authorized-capital headroom is being created now.
- **Forward-signal cluster:** RARE India (unreviewed, loss-making, PPA provisional, 15% residual) + Itmenaan Lodges + Clean Max Nile solar + Duet Hyderabad CCPS = active inorganic-build phase funded by the pending Rs 750 cr raise. Dilution vs growth trade-off is the central A4 question.
