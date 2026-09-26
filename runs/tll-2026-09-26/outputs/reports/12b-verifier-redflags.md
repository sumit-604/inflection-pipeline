# Verifier B: Communication Red Flags. TLL (Trident Lifeline Ltd), run 2026-09-26, phase 1 (post-rework audit)

Mode: NO-CONCALL. TLL files no earnings-call transcripts. This audit reads the company's own communication instead:
- four investor decks (13-Nov-2025, 20-Jan-2026, 09-May-2026, 03-Aug-2026)
- the FY26 and FY25 annual reports
- the results filings (H1 FY26 revised, FY26 audited, Q1 FY27 reviewed)
- every Reg 30 filing in inputs/announcements, including the Sep-2026 files named by hash
- the 2022 prospectus, read for the auditor block only

Peer transcripts were spot-checked against the B06 citations. The independent read came first. Upstream reports (B02, B03, B05, B06, B08) were compared after it. The superseded/ and final/ folders were not opened.

Scope note. B05 and B08 are rework-round reports. They absorbed most of the earlier audit's list, so the high catch count below is expected. The new material this pass comes from the Reg 30 acquisition series, the Apr-2025 EGM notice, and the FY25 AR KMP section. Upstream stages had not read those three sources closely.

---

## 1. Independent red-flag list (from sources, before comparison)

Severity scale: CRITICAL (would change a decision), MAJOR (wrong or missing, decision likely survives), MINOR.

| ID | Red flag | Anchor | Severity |
|---|---|---|---|
| R1 | FY25 standalone CFO is shown as -349.31 lakh in the Nov-2025 and Jan-2026 decks. The May-2026 deck shows +197.07 lakh for the same year, with no note. The FY26 statements add "Changes in Working Capital Facilities" inside operating cash flow. The basis change is repeated across two decks and the AR. | 20251113 deck line 676, 682; 20260120 deck line 669, 675; 20260509 deck line 644, 650 | CRITICAL |
| R2 | Total Income (10,607.05 lakh) is labelled "Revenue from Operations" in the May-2026 deck and in the FY26 Board's Report. Audited revenue from operations is 10,189.95 lakh. | 20260509 deck line 563; AR FY26 lines 1609-1614; 20260729 results line 112-114 | MAJOR |
| R3 | "The product mix has remained fairly-stable" is kept word for word while toothpaste/mouthwash/ointments fall from 36% (FY25) to 1% (FY26) and capsules rise to 30%. | 20251113 deck lines 274-286; 20260509 deck lines 273-288 | MAJOR |
| R4 | Sales, receivables, loans and Rs 2.50 Cr guarantees each to Talon Healthcare LLP and Tench Life Sciences LLP. The filings state that promoters are partners in both LLPs. The MD&A credits domestic growth to "sales reach". | 20250312-corporate-guarantee lines 17-20, 44-50, 69-75; AR FY26 Note 32 | MAJOR |
| R5 | **Mediquip stake bought from promoter-linked holders at rising prices.** TLL bought Trident Mediquip shares from its "existing shareholders" at Rs 11.32 (39,67,800 shares, completed Feb-2025), then Rs 63.00 (7,03,000 shares, Dec-2025), then Rs 95.40 (2,61,825 shares, Mar-2026, after a 1:5 bonus). Every filing names Hardik Desai, Amit Halvawala and Chetan Jariwala as members of Mediquip. The Mar-2026 Reg 30 gives the cost as "NA". Between tranches, Mediquip made private placements "to other shareholders" at prices that were not disclosed: 60.04% to 57.34% to 57.10%, then after the TLL purchase 59.77% to 59.47% to 59.17% to 58.84% to 58.67%. | AR FY26 lines 6745-6751 (Note 11 per-share prices); 20241224 lines 27-29, 66-77, 104-112; 20260101 lines 16-20, 103; 20260318 lines 17-27, 112; 20260303, 20260417, 20260424, 20260609, 20260616 filings | CRITICAL |
| R6 | **Mediquip was shrinking when bought.** It was a promoter-group company and a declining one at purchase: turnover Rs 35.08 Cr (FY22), 28.77 Cr (FY23), 20.58 Cr (FY24), 21.29 Cr (FY25). FY26 is Rs 27.31 Cr, still below FY22. The Aug-2026 deck states a Rs 70 Cr peak. | 20241224 lines 120-126; 20260616 lines 114-117 | MAJOR |
| R7 | **Promoter group co-owns the growth subsidiaries.** TLL holds 51% of TLL Parenterals, and Hardik Desai is a member of it. TLL holds 58.67% of Mediquip, and promoter-group members hold part of the rest. TLL guarantees subsidiary debt in full, for example Rs 16.53 Cr to Yes Bank for Mediquip. The "triple in 3 years" claim and the Rs 200 Cr / Rs 70 Cr peaks are stated at 100%. TLL holders own 51% and 58.67% of them. | 20241126 lines 65-75, 99-111; 20260616 line 19; 20250225-corporate-guarantee lines 17-47 | MAJOR |
| R8 | **CFO in post one year earlier than B08 says.** Ashish Anandsingh Bafna has been CFO since 17-Jul-2024, not 17-Jul-2025. The FY25 AR states "w.e.f 17.07.2024" twice. He signed the FY25 financial statements as CFO on 28-Apr-2025, next to the A Bafna & Associates audit signature. The Apr-2025 EGM notice calls him CFO. Only one line (AR FY25 line 1707) carries "2025", and it conflicts with the rest of the same AR. | AR FY25 lines 1331-1332, 3024-3025, 4600-4609, 1704-1707; 20250417-EGM-notice lines 488-492 | MAJOR |
| R9 | **Bafna holdings in TLL.** Before the issue, the CFO held 30,600 TLL shares (the "Key Managerial Personnel" row) and was allotted 24,000 warrants. Bootstrap Combinator LLP was allotted 36,000 warrants. Its ultimate beneficial owner is named "Harddik Ashish Bafna". Both are classified NON-PROMOTER. The statutory auditor is A Bafna & Associates. | 20250417-EGM-notice lines 387, 393, 611, 618, 667, 679, 747 | MAJOR |
| R10 | The 2022 prospectus names A Bafna & Associates (FRN 121901W, Membership No. 106525, audits@cabafna.in) as statutory auditor. The firm still audits TLL. | TLL-prospectus-2022 lines 4776-4785 | CRITICAL |
| R11 | The Jan-2026 deck's 9M FY26 figures do not equal H1 + Q3. The gap is 35.25 lakh, and it sits in operating expense: 9M opex 5,269.03 against 3,494.80 + 1,738.98 = 5,233.78. The audited FY26 PBT (2,497.92) less Q4 (795.07) reconciles to H1 + Q3 (1,702.85), not to the deck's 9M. Q4 FY26 D&A is 4.15 lakh against 71.23 (Q3) and 69.81 (Q1 FY27). No note is given. | 20260120 deck lines 525-565; 20251113 deck lines 561-570; 20260729 results lines 124, 129-133 | MAJOR |
| R12 | FY26 results note: consolidation method changed "from Proportionate Method to Equity Method as per AS-21", with "no material impact". | 20260507 results line 862 | MAJOR |
| R13 | AR Note 22 "Claim Income" 541.05 lakh (FY26) and 522.17 lakh (FY25) is never named in the MD&A "PBT doubled" claim. | AR FY26 line 12437 | MAJOR |
| R14 | IPO product-registration object: 51.87 lakh of 513.66 lakh used by Jun-2025, 75.81 lakh by Mar-2026. The statement says "Deviation: No". A new Rs 26.57 Cr raise followed. | 20250728-statement-of-deviation lines 54, 99; AR FY26 lines 1666-1687 | MAJOR |
| R15 | "Triple in 3 years" and the subsidiary peak figures appear only in the Aug-2026 deck. They are not in the FY26 AR outlook. | Aug-2026 deck p5, p11-15; AR FY26 outlook | MAJOR |
| R16 | The Chairman's spouse, Maniya Desai, left the board on 21-Nov-2025. The FY26 AR and the Aug-2026 deck show her as Chief Operating Officer. | AR FY26 line 993; 20260803 deck line 521 | MAJOR |
| R17 | FY26 standalone EPS is Rs 15.37 in the Board's Report and Rs 15.50 in the audited results. | AR FY26 lines 1601, 1618; 20260507 results line 347 | MINOR |
| R18 | Two award Reg 30 filings carry press releases through IR firm NeoAtlas (20-Aug and 08-Sep-2026). A group-meeting conference follows on 25-Sep. BSE sent a price-movement query on 23-Sep-2026. The company replied with boilerplate: "purely due to market conditions". | 20260820 lines 12-26, 107-119; 20260908 lines 11-30; 20260916 lines 11-26; 20260924 lines 12-29 | MINOR |
| R19 | "Lorem ipsum" placeholder text in the Aug-2026 deck. | 20260803 deck lines 263, 277, 346 | MINOR |
| R20 | The FY26 AR board table swaps DIN and title for Shravan Patel and Rupaben Jariwala. Sep-2026 filings confirm the signature-block version: Shravan Patel MD, DIN 08629141; Rupaben Jariwala WTD, DIN 08543127. | 20260817 lines 34-36; 20260916 lines 46-48 | MINOR |
| R21 | Warrant proceeds 57.5% used (1,526.57 of 2,657.34 lakh). The AR gives one line with no split by object. | AR FY26 lines 1688-1699 | MINOR |
| R22 | The promoter group took 5,98,200 of 9,99,000 warrants (59.9%). MD Shravan Patel is classified non-promoter, although he is the Chairman's partner in both LLPs. | 20250417-EGM-notice lines 372-401 | MINOR |

Material items: 16 (3 CRITICAL: R1, R5, R10; 13 MAJOR). Minor items: 6.

---

## 2. Comparison against the pipeline

| ID | Status | Where caught / note |
|---|---|---|
| R1 | CAUGHT | B02 #1, B03 LBF1/3A, B05 item 2 (FLAG-CASHFLOW) |
| R2 | CAUGHT | B05 item 3 |
| R3 | CAUGHT | B05 item 9 |
| R4 | CAUGHT | B08 3A (15.4% standalone, receivables +232%), B03 LBF3, B02 #2 |
| R5 | PARTIALLY CAUGHT | B02 #4 found the tranche dates and the goodwill jump. It classed the item as a missing-note accounting gap. It also says "no purchase-consideration ... disclosure exists", but Note 11 prints every per-share price. No stage names the sellers, the price step-up, the "NA" cost filing, or the interleaved private placements. Classed wrongly and weighted too low. |
| R6 | MISSED | B03 6A/6B/8 calls Mediquip "executing to a meaningful scale" and "a genuine partial confirmation" of LBF3. No stage read the pre-acquisition turnover history. |
| R7 | MISSED | B02 #15 notes the Parenterals term loan. No stage flags that promoter-group members own the minority stakes, or what that means for the subsidiary peak claims. |
| R8 | PARTIALLY CAUGHT | B08 caught the name link and graded it RED FLAG. It dates the CFO start to 17-Jul-2025 from the single conflicting AR line, so it understates the overlap. In fact he was CFO for the full FY25 audit year. |
| R9 | MISSED | B08 3E says no filing discloses a relationship. It did not read the EGM notice allottee tables. |
| R10 | CAUGHT | B08 3E, REWORK item 1 |
| R11 | CAUGHT | B05 item 5. Refinement: the gap sits in opex, and the deck understates 9M profit rather than flattering it. The Q4 D&A anomaly is the part that matters: it lifts Q4 FY26 PBT, the exit-rate quarter. |
| R12 | CAUGHT | B05 item 6 |
| R13 | CAUGHT | B02 #14, B03 LBF2, B05 item 7 |
| R14 | CAUGHT | B05 1B/2A/4A |
| R15 | CAUGHT | B03 4C, B05 1C/4D |
| R16 | CAUGHT | B08 REWORK item 10 |
| R17 | MISSED | B02 pass 1 cites 15.37 without testing it against the results |
| R18 | PARTIALLY CAUGHT | B03 5E mentions the BSE query from company memory. It does not name the award and press-release cadence around the query. |
| R19 | CAUGHT | B05 4D FLAG-PROCESS |
| R20 | CAUGHT | B08 1A |
| R21 | CAUGHT | B02 #9, B08 3B |
| R22 | MISSED | B08 3C says the dilution was "absorbed by the market/other allottees". The filing shows the promoter group took 59.9% of the warrants. |

### Pipeline flags I did not raise independently, assessed

| Pipeline flag | Assessment | Basis |
|---|---|---|
| B03 LBF4 / 5D: "true FY25 promoter 65.22%, -2.37pp; FY25 comparative is a stale copy" | **NOT SUPPORTED** (number) | The FY25 AR prints 72,49,400 shares = 63.04% (AR FY25 lines 5095-5096), and the Apr-2025 EGM notice matches (line 715). The FY26 AR table headed "as on 31st March, 2025" (AR FY26 line 10551) carries FY26 data under a stale heading. The true move is 63.04% to 62.85%. The defect is real. The derived dilution figure is wrong and feeds LBF4 and the Phase 8 monitorable. |
| B05 item 8: registration-by-region vs export-by-region "test fails" | OVERSTATED | By the company's own claim, registrations take 1.5-3 years to turn into revenue. The FY26 export mix therefore cannot falsify "registrations are the clearest indicator of future revenue". The observation that would separate the two readings is Africa export revenue in FY27-FY28. The flag belongs on a watch list, not in the credibility grade. |
| B06 Q1: SENORES 90-94 days as a "second, independent" receivable-days anchor | OVERSTATED | The CFO said "net versus capital cycle is around 90 days, 94 days" (SENORES Jan-2026 line 1315). That is a net working-capital cycle, a different basis from TLL's 208 debtor days. The CONTRADICTED verdict still holds on the CAPLIPOINT 117-136 day band alone. |
| B06 Q2: INNOVACAP 65-70% utilisation ceiling after 4-5 years | SUPPORTED (with caveat) | Verbatim at INNOVACAP Nov-2025 lines 710-716. The quote covers CDMO capacity at Jammu, not injectables alone. It is a fair cross-check, but not a like-for-like injectable benchmark. |
| B05 items 2, 3, 5, 6, 7, 9 | SUPPORTED | Spot-read at source: rows R1, R2, R11, R12, R13 and R3 above |
| B08 items 1, 10 | SUPPORTED | R10 and R16 above; B08 item 1 is refined by R8 and R9 |

---

## 3. Promise-delivery spot checks (B05 Section 2A)

| # | B05 row | Earlier document has the promise? | Later document shows the outcome? | Result |
|---|---|---|---|---|
| 1 | H1 FY26 deck: "grow at both standalone and consolidated levels" | Yes, 20251113 deck lines 597-600 | FY26 standalone revenue from operations 10,189.95 lakh (20260729 results line 112) against FY25 total revenue 7,094.00 lakh (20251113 deck line 617). Delivered directionally. | Confirmed |
| 2 | Q3 FY26 deck outlook, and 9M PBT does not reconcile | Yes, 20260120 deck line 589 | 9M PBT 1,667.60 against H1 1,110.46 + Q3 592.39 = 1,702.85. The audited FY less Q4 gives 1,702.85. | Confirmed |
| 3 | Statement of Deviation: registration capital underdelivered | Allocation 513.66 lakh (20250728 line 99) | 51.87 lakh used by Jun-2025; 75.81 lakh by Mar-2026 (AR FY26 line 1679) | Confirmed |
| 4 | Board's Report "revenue from operations 10607.05 Lacs" | AR FY26 lines 1610-1612 | Results: revenue 10,189.95 plus other income 417.10 = total 10,607.05 | Confirmed |

Checked 4, confirmed 4, wrong 0.

---

## 4. Credibility grade

**Concur with D.** One B05 input is overstated: the registration-region item. Removing it does not lift the grade. The items this pass adds all point the same way:
- Mediquip was bought from promoter-linked holders at rising prices, with one cost filed as "NA".
- The CFO's holdings and warrants, and his relative's LLP allotment, appear in the EGM notice and in no later disclosure.
- The CFO start date is wrong in one AR line.

---

## 5. What the operator should carry to Halt 1

1. **Mediquip related-party pricing (R5).** The most evidenced reading is that TLL paid promoter-linked sellers Rs 11.32, then Rs 63.00, then Rs 95.40 per share within about 13 months. Over that time Mediquip turnover moved from Rs 21.29 Cr to Rs 27.31 Cr. The other reading is that arm's-length third parties sold the later tranches and the placements were priced at or above TLL's price. One observation separates the two: the seller list and the placement price for each tranche. That comes from Mediquip's MGT-7 / PAS-3, or a company answer. NOT FOUND in the corpus.
2. **Auditor independence (R8, R9, R10).** The question is no longer only whether he is the same person. The CFO held TLL shares and warrants in Apr-2025, and a relative-named LLP holds warrants. The one observation that separates the readings is the date he left A Bafna & Associates, if he ever did. That date is NOT FOUND.
3. **Subsidiary economics (R6, R7).** Read the "triple" claim and the peak figures at TLL's ownership share, not at 100%. Treat Mediquip as a recovery toward its FY22 level, not as a new-build ramp.

---

```yaml
stage: B12b
company: "TLL"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 22
caught: 14
partially_caught: 3
missed:
  - {severity: "MAJOR", item: "R6 Mediquip turnover fell from Rs 35.08 Cr FY22 to 20.58 Cr FY24 before acquisition from promoter-linked holders; FY26 27.31 Cr still below FY22 vs Rs 70 Cr deck peak", anchor: "20241224-acquisition.txt lines 120-126; 20260616-acquisition.txt lines 114-117"}
  - {severity: "MAJOR", item: "R7 Promoter-group co-ownership of Parenterals (51% TLL) and Mediquip (58.67% TLL); TLL guarantees subsidiary debt in full; peaks stated at 100%", anchor: "20241126-acquisition.txt lines 65-75, 99-111; 20260616-acquisition.txt line 19; 20250225-corporate-guarantee.txt lines 17-47"}
  - {severity: "MAJOR", item: "R9 CFO held 30,600 shares and took 24,000 warrants; Bootstrap Combinator LLP (UBO 'Harddik Ashish Bafna') took 36,000 warrants; statutory auditor is A Bafna & Associates", anchor: "20250417-EGM-notice.txt lines 387, 393, 611, 618, 667, 679, 747"}
  - {severity: "MINOR", item: "R17 Standalone FY26 EPS 15.37 in Board's Report vs 15.50 in audited results", anchor: "Annual_Report_2026.txt lines 1601, 1618; 20260507-FY26-H2-results.txt line 347"}
  - {severity: "MINOR", item: "R22 Promoter group took 59.9% of the 9,99,000 warrants; B08 says dilution absorbed by market", anchor: "20250417-EGM-notice.txt lines 372-401"}
pipeline_flags_not_supported:
  - "B03 LBF4: true FY25 promoter 65.22% and -2.37pp fall. FY25 AR prints 72,49,400 = 63.04% (Annual_Report_2025.txt lines 5095-5096); defect is a stale heading at Annual_Report_2026.txt line 10551"
promise_delivery_spot_checks: {checked: 4, confirmed: 4, wrong: 0}
credibility_grade_concur: "concur at D. New related-party pricing and Bafna holdings items support D; the overstated region item does not lift it"
findings:
  - {severity: "CRITICAL", location: "B02 finding 4; B08 3A", issue: "R5 PARTIALLY CAUGHT. Mediquip shares bought from existing (promoter-linked) holders at Rs 11.32, 63.00, 95.40; Mar-2026 cost filed NA; placements to other shareholders at undisclosed prices", anchor: "Annual_Report_2026.txt lines 6745-6751; 20260318-acquisition.txt lines 17-27, 112"}
  - {severity: "MAJOR", location: "B08 1A, 3E", issue: "R8 PARTIALLY CAUGHT. CFO since 17-Jul-2024 not 2025; signed FY25 accounts audited by A Bafna & Associates", anchor: "Annual_Report_2025.txt lines 1331-1332, 3024-3025, 4600-4609"}
  - {severity: "MAJOR", location: "B08 3E", issue: "R9 MISSED. Bafna share and warrant holdings", anchor: "20250417-EGM-notice.txt lines 393, 611, 618, 679, 747"}
  - {severity: "MAJOR", location: "B03 6A, 8", issue: "R6 MISSED. Mediquip pre-acquisition decline", anchor: "20241224-acquisition.txt lines 120-126"}
  - {severity: "MAJOR", location: "B05 1B, 4A", issue: "R7 MISSED. Promoter co-ownership of subsidiaries", anchor: "20241126-acquisition.txt lines 65-75"}
  - {severity: "MAJOR", location: "B03 LBF4, 5D", issue: "NOT SUPPORTED. 65.22% FY25 promoter figure contradicted by filed 63.04%", anchor: "Annual_Report_2025.txt lines 5095-5096"}
  - {severity: "MINOR", location: "B05 item 8", issue: "OVERSTATED. Registration-region test cannot falsify a lead indicator", anchor: "B05 lines 125-143"}
  - {severity: "MINOR", location: "B06 Q1", issue: "OVERSTATED. SENORES 90-94 days is a net WC cycle, not receivable days", anchor: "SENORES-Concall_Jan_2026_Transcript.txt line 1315"}
  - {severity: "MINOR", location: "B02 pass1", issue: "R17 MISSED. EPS 15.37 vs 15.50", anchor: "20260507-FY26-H2-results.txt line 347"}
  - {severity: "MINOR", location: "B08 3C", issue: "R22 MISSED. Promoters took 59.9% of warrants", anchor: "20250417-EGM-notice.txt lines 372-401"}
  - {severity: "MINOR", location: "B03 5E", issue: "R18 PARTIALLY CAUGHT. Award PR cadence around BSE price query", anchor: "20260924-96a42ab8 lines 12-29"}
critical_count: 3
major_count: 13
minor_count: 6
material_found: 16
material_caught: 13
acceptance_rate: 81
acceptance_rate_full_catch_only: 69
coverage_basis: "22 independent items: 16 material (3 CRITICAL, 13 MAJOR), 6 MINOR. All 22: 14 caught, 3 partial, 5 missed. Material: 11 caught, 2 partial, 3 missed. 13/16 = 81% with partial as caught; 11/16 = 69% full catches only. Pipeline flags: 1 NOT SUPPORTED, 4 OVERSTATED or partly wrong"
```
