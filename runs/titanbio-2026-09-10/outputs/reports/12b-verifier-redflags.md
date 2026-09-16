# STAGE 12B: VERIFIER B — COMMUNICATION RED FLAGS (NO-CONCALL MODE)
Titan Biotech Ltd (TITANBIO) | Run date 2026-09-16 | Model: claude-opus-5

**SCOPE.** This company holds no earnings calls. Per the task scope note, the 15-transcript
input is substituted by the company's own written communication record: three annual
reports (FY2024, FY2025, FY2026), four results filings (Q2 FY26, Q3 FY26, FY26 audited,
Q1 FY27) and eight Reg 30 announcements (Feb-2025 to Sep-2026). The eleven peer
transcripts are the peers' communication and are not this company's record; peer coverage
belongs to Verifier D and is not re-audited here.

**METHOD.** I read the sources first and built the list below before opening B05 or B06.
Page anchors are the extracted `=== PAGE n ===` markers, which match the PDF page numbers.
Every number below is quoted from a filing. Where I could not find a figure, I write
NOT FOUND rather than estimate.

---

## PART 1: INDEPENDENT RED-FLAG LIST (built before reading B05/B06)

Graded on the standard scale. `acceptance_rate` is computed on the CRITICAL + MAJOR
subset only (rule 6); the MINOR list is reported in full and does not depress the score.

### CRITICAL

**C1. The MD&A cash-flow table reports pre-tax operating cash as CFO, across two annual
reports, and does not reconcile to the closing cash it prints.**
AR FY2026 MD&A, PDF p.104 (printed p.102): "Cash generated from operating activities in FY
2026 was Rs. 3,896.91 Lacs." The audited standalone cash flow (30-May-2026 results, PDF
p.10) shows `Cash generation from operation 3,896.91`, then `Less: Income tax paid
(854.83)`, then `Net Cash generated/(used) - Operating Activities 3,042.08`. The MD&A
prints the pre-tax line, unlabelled, as operating cash flow — a 28.1% overstatement of
audited net CFO.
The table does not foot. MD&A "Table A" gives Operating 3,896.91, Investing (3,441.49),
Financing 34.39, Closing cash 147.77. Those three flows sum to +489.81, while cash actually
fell 365.02 (512.79 to 147.77). The Rs 854.83 lakh tax line is simply absent.
The same unlabelled basis recurs backwards: AR FY2025 MD&A (PDF p.100) gives FY24
operating activities as Rs 2,901.66 lakh; AR FY2024 MD&A (PDF p.105) gives the identical
year as Rs 2,114.63 lakh. The FY24 AR figure is the internally consistent one
(2,114.63 - 2,030.37 - 286.62 = -202.36; 486.37 - 202.36 = 284.01, matching the stated
closing cash exactly). The FY25 AR silently switched the same year to the pre-tax basis.
Two consecutive annual reports, a pillar input (cash conversion), no label, no note.
Severity CRITICAL: repeated across periods and thesis-relevant.

**C2. The "build capacity and capabilities" investing sentence is reused verbatim for
three years while the FY26 composition inverted.**
AR FY2024 p.105, AR FY2025 p.100 and AR FY2026 p.104 all carry: "Investing activities net
outflow amounting to Rs. (X) Lacs in FY 20XX includes net investment in property, plant,
equipment and intangibles to build capacity and capabilities for future business growth."
In FY24 and FY25 that was broadly true. In FY26 the audited cash flow (30-May-2026, PDF
p.10) shows `Investments in debt instruments quoted and unquoted equity instruments
(2,515.67)` against `Purchase of property, plant and equipment (740.09)` inside a total
investing outflow of (3,441.49). Rs 740.09 lakh of Rs 3,441.49 lakh, 21.5%, was PPE;
Rs 2,515.67 lakh, 73.1%, was securities. The sentence was not re-examined when the facts
changed. Severity CRITICAL: repeated language, materially false in the current year.

### MAJOR

**M1. The FY26 growth mechanism is computable from the Directors' Report and neither stage
computed it: exports supplied roughly 72% of the increment.**
Foreign exchange earned, Directors' Report §17/§16 in each AR: FY24 Rs 5,208.41 lakh
(AR FY2024 line 2920); FY25 Rs 5,295.20 lakh (AR FY2025 line 3967); FY26 Rs 8,897.37 lakh
(AR FY2026 line 4044). Against revenue of 16,582.03 / 15,645.08 / 20,619.03, the FX-earned
proxy moves from 31.4% to 33.8% to 43.2% of revenue. The FY26 revenue increment is
Rs 4,973.95 lakh; the FX-earned increment is Rs 3,602.17 lakh, or 72.4% of it. FY25 exports
were flat (+1.7%) while total revenue fell 5.7%, so the domestic proxy fell 9.0% that year
and recovered 13.3% in FY26.
Caveat stated: foreign exchange earned is not identical to export revenue (it may include
non-sales receipts and may sit on a different basis), and the freight gross-up sits inside
the revenue line. The direction and rough magnitude are nonetheless anchored and
unambiguous. Severity MAJOR: this is the answer to the question B05 itself records as
unanswered ("No explanation for the FY26 growth mechanism", B05 §2D).

**M2. The two-year revenue CAGR is 11.5%, not 31.8%, and the FY26 MD&A never says the base
year was a decline year.**
16,582.03 (FY24, AR FY2024 p.104) to 20,619.03 (FY26) is 11.5% p.a. FY25 fell 5.7% and fell
on every quality ratio the company itself publishes: Operating Profit Margin 20.67 to
16.02, Net Profit Margin 14.47 to 11.68, Return on Net Worth 18.42 to 12.59 (AR FY2025
p.100 ratio table). The FY26 MD&A's revenue paragraph is one sentence and mentions none of
this. Severity MAJOR.

**M3. The FY26 MD&A restates FY25 ROE at 10.70% using the wrong denominator, flattering the
improvement.**
AR FY2026 MD&A p.105 ratio table: "Return on equity (%) 17.32% (FY26) 10.70% (FY25)".
AR FY2025 MD&A p.100: "Return on Net Worth 12.59 (FY25)". 1,827.11 / 14,513.36 (FY25
closing equity) = 12.59%. 1,827.11 / 17,084.15 (**FY26** closing equity) = 10.70%. The FY26
report computed the prior year's return on the current year's equity base. The published
improvement reads +6.62pp; on a consistent closing-equity basis it is +3.47pp. Severity
MAJOR: ROE improvement is the headline quality metric of a transition thesis.

**M4. AR FY2025 blanks the "Change %" column for all eight ratios — in the one year every
ratio deteriorated.**
AR FY2025 p.100: every row reads "- %" or "-%". AR FY2024 p.106 populates the column for
all eight rows; AR FY2026 p.105 populates it for all eleven. The blanking is confined to
the year the numbers went the wrong way. Severity MAJOR.

**M5. FY24 revenue restated between annual reports without a note.**
AR FY2024 p.104: "revenue increasing from Rs. 14,594.24 Lakhs to Rs. 16,582.03 Lakhs."
AR FY2025 p.98: "revenue reduced ... from rs. 16407.21 Lakhs to rs. 15645.08 Lakhs."
Rs 174.82 lakh difference for the same year, no restatement note. Severity MAJOR.

**M6. The freight gross-up into revenue is never quantified and comparatives were not
restated.**
Note carried in every FY26 results filing (Q2 note 6, Q3 note 6, FY26 audited note 7, Q1
FY27 note 5): "Freight amount has been added in revenue from operations for the purpose of
calculation of sales including GST in current year. Freight also added in total in other
expenses to neutralise the impact of its addition in revenue in current year." The rupee
amount is never given, the FY25 comparative (15,645.08) is unchanged from its original
audited figure, and the policy is absent from all three annual reports. Reported FY26
growth of 31.8% is therefore not like-for-like by an undisclosed amount. Severity MAJOR.

**M7. FY26 capital allocation moved Rs 25.16 crore into a portfolio the company itself
reports earning 3.64%.**
Securities purchases Rs 2,515.67 lakh versus capex Rs 740.09 lakh (30-May-2026, PDF p.10).
Non-current investments rose 2,449.99 to 4,965.67 lakh standalone, close to the net PPE
figure of 5,133.97. Cash fell 512.79 to 147.77. The company's own ratio table (AR FY2026
p.105) reports "Return on investment (in %) 3.64% (FY26) 7.04% (FY25)" against "Return on
capital employed (%) 24.09%". Capital moved from a 24% business into a 3.6% portfolio, on
management's own numbers. Severity MAJOR.

**M8. Titan Media Limited: voting rights raised to 48.44%, disclosed in five lines.**
Reg 30, 28-Feb-2025: "the Company's voting right in Investee Company stands increased to
48.44% (from 32.29% at the time of our investment in February 2024)." No consideration, no
valuation, no rationale, no strategic fit statement. A media company held just under the
consolidation line by a biological-products manufacturer. Contrast the disclosure standard:
the NGenious Solutions arbitration, a claim of Rs 10,62,410, received a full Annexure-A with
seven fields on 24-Jul-2025. The auditor states the associates are "not material to the
Group" (30-May-2026, PDF p.14) while they contribute Rs 243.80 lakh, 8.2% of consolidated
PAT, and lift consolidated EPS to 7.24 from standalone 6.64. Severity MAJOR.

**M9. Selling and distribution rose 3% on revenue up 31.8%, with promotion and advertising
cut — and the prior year did the exact opposite.**
AR FY2026 p.103: "Selling and distribution expenses increased marginally by approximately
3% to Rs. 1,152.78 lakh ... primarily attributable to a 36.88% rise in Cartage & Freight
Outward expenses, partly offset by lower expenditure on business promotion, travelling,
advertisement and commission." S&D fell from 7.15% to 5.59% of revenue. AR FY2025 p.98:
"selling and distribution expenses increased by 27.74% primarily because of the increase in
Business Promotion" — in a year revenue fell 5.7%. Promotion up into a falling top line,
promotion cut into a 32% rise. No annual report reconciles the two. Severity MAJOR: it goes
directly to whether the FY26 demand was won or arrived.

**M10. The employee-cost sentence states the opposite of its own table.**
AR FY2026 p.103: "As a percentage of revenue, employee benefits expenses increased to
15.70% in FY26 from 16.86% in FY25." That is a decrease. The sentence is the AR FY2024
(p.105) and AR FY2025 (p.99) template carried forward unchanged, including the closing
clause "taking into account cost optimization and pyramid rebalancing measures" — staffing-
pyramid language from IT services, retained for three years in a fermentation business. In
FY24 and FY25 the ratio genuinely rose and the sentence was true; in FY26 nobody checked.
Severity MAJOR.

**M11. The headcount series does not reconcile across three annual reports.**
AR FY2024 p.105: 449 permanent employees, "+13.38%". AR FY2025 p.100: 424 employees,
"Total Headcount was increased by 7.07% during the year" — a fall of 25 against the prior
AR, and +7.07% implies a base of 396. AR FY2026 p.104: 527 employees, "+15.09%" — which
implies a base of 458, not 424 (527/424 is +24.3%). Headcount is the only scale or capacity
proxy the company discloses anywhere. Severity MAJOR.

**M12. Q4 FY26 fell hard sequentially and no filing says a word about it.**
Q4 FY26 revenue is Rs 4,883.35 lakh (20,619.03 less 9M 15,735.68), against Q3's 5,650.57 —
down 13.6% QoQ. PAT 655.57 against 786.82, down 16.7%. The Q4 effective tax rate is 36.2%
(372.60 on 1,028.17) against 25.5% in Q3, including a deferred tax charge of 70.38 after
9M deferred tax of just 13.61. The year's best quarter to its weakest, inside the year, with
no commentary in the results filing or the annual report. Severity MAJOR.

### MINOR

| # | Item | Anchor |
|---|---|---|
| m1 | FY26 consolidated results note says statutory auditors "carried out a Limited Review of the aforesaid results" for annual **audited** results, contradicting the audit opinion on PDF p.11 | 30-May-2026, PDF p.15 and p.16 notes |
| m2 | Prior-year ratio values restated between ARs without note: Inventory Turnover FY24 2.40 then 2.29; Current Ratio FY24 3.77 then 3.71; Debt-equity FY24 0.07 then 0.06; Current Ratio FY25 4.46 then 4.48 | AR FY2024 p.106 vs AR FY2025 p.100 vs AR FY2026 p.105 |
| m3 | FY26 ratio table prints two different change percentages, 19.46% and 0.36%, for the identical Inventory Turnover pair 2.21 vs 1.85 | AR FY2026 p.105 |
| m4 | FY25 finance-cost paragraph explains FY25 by reference to "the year ended March 31, 2023" | AR FY2025 p.98 |
| m5 | FY24 tax expense given as Rs 789.48 lakh, then as Rs 778.86 lakh; the stated FY25 decrease of 181.85 does not match either pair | AR FY2024 p.104 vs AR FY2025 p.98 |
| m6 | FY25 R&D restated: Rs 18.39 lakh in AR FY2025, Rs 17,63,024.68 (17.63 lakh) as the FY26 AR's prior-year column | AR FY2026 line 4805 |
| m7 | R&D is 0.13% of turnover in FY26 (0.11% FY25) against a product-development claim repeated three years | AR FY2026 line 4807 |
| m8 | Prior-year audited balance-sheet components restated between filings under boilerplate "regrouped/reclassified": inventories at 31-Mar-25 given as 5,072.29 then 5,082.06; other current assets 386.73 then 424.04. Total assets unchanged at 16,643.79. OCR caution on scanned tables | Q2 FY26 PDF p.6 vs 30-May-2026 PDF p.9 |
| m9 | Three FY26 ratios moved more than 25% (current ratio -26.79%, debt-equity +50%, trade payables turnover -32.37%) with no MD&A explanation, only a cross-reference to Note 45; AR FY2024 explained its single >25% mover in the MD&A itself | AR FY2026 p.105 vs AR FY2024 p.106 |
| m10 | First-ever expected-credit-loss provision on receivables, Rs 36.26 lakh, nil in FY25, no commentary anywhere | 30-May-2026, PDF p.10 |
| m11 | Split (1:5, approved 29-Nov-2025, effective 20-Feb-2026), bonus (1:4, 03-Sep-2026) and authorised-capital increase inside ten months, with no investor presentation, press release or call at any point | Reg 30 filings 29-Nov-2025 and 03-Sep-2026 |
| m12 | The FY26 MD&A opens with roughly three pages of IMF/World Bank macro text (Middle East war, defence-spending booms, post-war recovery economics) against roughly one page of company-specific discussion | AR FY2026 pp.95-97 vs pp.103-105 |
| m13 | Four Singla family members hold executive board seats (two Managing Directors, two Whole Time Directors), all re-appointed or given raises at the same AGM | Reg 30, 27-Sep-2025 |
| m14 | Receivables built to Rs 2,963.55 lakh at 30-Sep-25 (53.6 days annualised) then fell to Rs 2,282.86 lakh at year end (40 days) | Q2 FY26 PDF p.6; 30-May-2026 PDF p.9 |
| m15 | Board meetings approving results ran 34 to 42 minutes | 30-May-2026 p.2; 11-11-2025 p.1; 12-02-2026 p.1; 13-08-2026 p.1 |

**Independent list: 29 items. Material (CRITICAL + MAJOR): 14.**

---

## PART 2: COMPARISON AGAINST B05 AND B06

### 2A. My material items against the pipeline

| # | Item | Verdict | Note |
|---|---|---|---|
| C1 | MD&A cash table reports pre-tax CFO, does not reconcile | **MISSED** | B05 quotes the investing line from this same table (Rs 34.41cr) and does not test the operating line above it. Neither B05 nor B06 mentions Rs 3,042.08. |
| C2 | "Build capacity" sentence vs FY26 composition | **CAUGHT** | B05 red flag 1 (HIGH), §1C, §2A row 3, §2E; B06 §2C. Strongest item in both reports. Magnitude is wrong (see 2B, F-P5). |
| M1 | Exports supplied ~72% of the FY26 increment; FX-earned series in every Directors' Report | **MISSED** | B05 §2D records the growth mechanism as unexplained and §3D asserts no geography signal exists after FY24. The Directors' Report gives an annual export proxy in all three years. |
| M2 | Two-year CAGR 11.5%, FY25 a decline year on every published ratio | **PARTIALLY CAUGHT** | B05 §2A row 5 and trigger 1 name the FY25 fall and the FY26 rebound, and the kill-signal is right. Neither report sets the two-year rate or cites the FY25 ratio-table deterioration. |
| M3 | FY25 ROE restated to 10.70% on the FY26 equity base | **MISSED** | Not mentioned in either report. |
| M4 | AR FY2025 blanks the Change % column in the down year | **MISSED** | Not mentioned in either report. |
| M5 | FY24 revenue 16,582.03 then 16,407.21 | **CAUGHT** | B05 red flag 5 (MEDIUM), with the employee-cost ratio restatement alongside it. Correctly anchored. |
| M6 | Freight gross-up unquantified, comparatives not restated | **CAUGHT** | B05 §2D and flag; B06 Claim 3 (UNVERIFIABLE, correctly reasoned). |
| M7 | Rs 25.16cr into a portfolio returning 3.64% on the company's own table | **PARTIALLY CAUGHT** | The portfolio is caught and made trigger 3. The company's own "Return on investment 3.64% vs 7.04%" line — the hardest single piece of evidence that the allocation destroys value — is not cited in either report. |
| M8 | Titan Media voting to 48.44%; disclosure asymmetry vs a Rs 10.62 lakh arbitration | **PARTIALLY CAUGHT** | B05 §2D and trigger 4 flag the associates as a reconciliation gap and B05 row 7 covers the arbitration. Neither report cites the 28-Feb-2025 Reg 30, the 48.44%/32.29% escalation, or the asymmetry between the two disclosures. |
| M9 | S&D +3% on revenue +32% with promotion cut; FY25 the inverse | **MISSED** | B05 treats the marketing claim qualitatively (§2A row 5) and never reaches the FY26 S&D numbers on AR FY2026 p.103. |
| M10 | "increased to 15.70% from 16.86%" — it fell | **PARTIALLY CAUGHT** | B05 caught the FY24 ratio restatement (14.30 vs 14.45) in the same paragraph but not the directional error in the FY26 sentence. |
| M11 | Headcount series does not reconcile across three ARs | **MISSED** | Not mentioned in either report. |
| M12 | Q4 FY26 down 13.6% QoQ, PAT down 16.7%, tax rate 36.2% | **MISSED** | Neither report examines within-year quarterly shape. |

Material found 14. Caught 3, partially caught 4, missed 7. Counting partials as "the
pipeline already had it": material_caught = 7 of 14 = **50%**.

**Qualifier the orchestrator should weigh.** The misses cluster in one place: the MD&A's
own numeric tables (C1, M3, M4, M10, M11) and the Directors' Report annexures (M1). B05's
audit of MD&A *prose* — repetition, dropped disclosures, hedged market-share language,
undelivered claims, excuse patterns — is strong and I confirmed every prose finding I
tested. The gap is a table-reading gap, not an analytical failure. A targeted re-read of
the three MD&A ratio tables, the three cash-flow "Table A" blocks and the three
Directors' Report FX-earnings paragraphs would close most of it.

### 2B. Pipeline flags I did not find independently

| # | Pipeline flag | Assessment | Basis |
|---|---|---|---|
| F-P1 | Health-supplement claim repeated three years, never named (B05 MEDIUM) | **SUPPORTED** | Spot-checked. AR FY2024 line 2807 and AR FY2025 line 3830 are verbatim identical: "The Company is developing product for health supplement." AR FY2026 lines 3837-3840 expand the wording and still name nothing. |
| F-P2 | Cautionary statement claims consolidated basis while quoting standalone figures (B05 MEDIUM) | **SUPPORTED but OVERSTATED** | The sentence is real and is identical boilerplate in all three ARs (FY24 p.106, FY25 p.100, FY26 p.105). But the MD&A heads its own table "Standalone Statement of Cash Flows", the ratio table carries both bases in separate columns, and standalone and consolidated revenue are the same number (20,619.03). Consequence for a reader is near zero. Should sit at LOW, not MEDIUM. |
| F-P3 | No follow-up on the NGenious arbitration (B05 LOW) | **SUPPORTED** | Confirmed against the announcement set through 05-Sep-2026. Correctly graded LOW and correctly excluded from the grade. |
| F-P4 | "The only customer/geography signal across three years is the FY24-only split" (B05 §3D) | **NOT SUPPORTED as written** | Foreign exchange earned is disclosed in the Directors' Report in every year: FY24 Rs 5,208.41 lakh, FY25 Rs 5,295.20 lakh, FY26 Rs 8,897.37 lakh, plus the matching Annexure-2 restatement. An annual export proxy exists in all three years. The narrower flag — that the domestic/overseas *percentage split* was dropped from the MD&A after FY24 — stands and is correct. MAJOR, because this is the disclosure that answers B05's own open question about the FY26 growth mechanism. |
| F-P5 | "77% of the outflow" / consolidated outflow "Rs 32.55cr" / "(3,254.59)" (B05 flag 1, §1C, §2A row 3; repeated in B06 §2C and Claim 6) | **NOT SUPPORTED on the magnitude** | The consolidated cash flow in the cited filing (30-May-2026, PDF p.18) reads `Net Cash Generated/ (Used) - Investing Activities (3,441.49)` — identical to standalone, not (3,254.59). I could not locate Rs 3,254.59 lakh anywhere in that filing. The correct share is 2,515.67 / 3,441.49 = **73.1%**, not 77%. The flag itself stands; the number propagated into B06 twice. MAJOR. |
| F-P6 | "Rs 80.33cr exports FY26", "39%-of-revenue export book", "49% FY26 export growth" (B06 §2B, §2E, Claim 4, Part 4) | **NOT FOUND in the sources I read** | The FY26 Directors' Report §16 and Annexure-2 state foreign exchange earned of Rs 8,897.37 lakh — 43.2% of revenue, and +68.0% against FY24's 5,208.41. I could not find Rs 80.33 crore, 39%, or 49% in the annual report sections I read. These may sit in a financial-statement note on FOB export sales that I did not open. Referred to Verifier A as a source-fidelity question, not resolved here. MAJOR: the 49% figure is load-bearing in B06's Claim 4 net read and Part 4. |
| F-P7 | "~28.06% like-for-like ex freight" (B05 §2D, trigger 1) | **MINOR — unanchorable precision** | No company filing quantifies the freight amount. The figure is a Stage 2 derivation and B05 does attribute it, but it is carried in the trigger table to two decimal places as if measured. |
| F-P8 | B06 Claim 1 and Claim 6 verdicts of CONTRADICTED | **NOT RE-TESTED** | The peer transcripts are the peers' record, not this company's, and peer coverage is Verifier D's mandate. B06's construction is symmetric and its verdicts are stated with quote anchors; I record no view. |

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS

Five checks. Rule 4 asks whether the earlier document actually contains the promise and the
later document actually shows the outcome.

| # | B05 row | Earlier document contains the promise? | Later document shows the outcome? | Verdict |
|---|---|---|---|---|
| 1 | Row 1: FY24 dividend Rs 2.00/share delivered | YES — AR FY2024 notice item 2: "RESOLVED THAT final dividend of Rs. 2.00 per equity share be and is hereby approved" (line 56) | YES — AR FY2025 Directors' Report §10: "For the financial year 2023-24, your Company has paid a final dividend of Rs. 2/- per equity share aggregating to Rs. 165.27 Lakh" (lines 3840-3841) | **CONFIRMED** |
| 2 | Row 4: health supplement promised FY24, undelivered | YES — AR FY2024 §8 FUTURE PLANS, line 2807, verbatim; AR FY2025 §8, line 3830, identical | YES — AR FY2026 §8, lines 3837-3840, expanded wording, no product, no date, no revenue line | **CONFIRMED** |
| 3 | Row 6: share split promised 29-Nov-2025, delivered | YES — Reg 30 29-Nov-2025: rationale "To enhance the liquidity of Company's equity shares and to encourage participation of retail investors by making equity shares of the Company more affordable" (lines 89-91) | YES — 30-May-2026 audited results note 8: sub-division effective 20-Feb-2026, 82,63,700 shares of Rs 10 to 4,13,18,500 shares of Rs 2 | **CONFIRMED** |
| 4 | Row 3: investing outflow builds capacity | YES — AR FY2024 p.105 and AR FY2025 p.100 carry the sentence verbatim | PARTLY — the direction of the contradiction is right and confirmed, but the stated magnitude is wrong: B05 says 77% of a consolidated (3,254.59); the filing shows (3,441.49) and the share is 73.1% | **DIRECTION CONFIRMED, MAGNITUDE WRONG** |
| 5 | §1C row: domestic/export split given in FY24, dropped thereafter | YES — AR FY2024 MD&A p.102: "revenue from Domestic Operation has increased by 7.80 % and revenue from Overseas Operation has increased by 27.81%" | YES for the MD&A split — AR FY2025 p.97 and AR FY2026 p.100 carry only "The Company has only one segment". NO for the wider claim that no geography signal survives: FX earned is disclosed in all three Directors' Reports | **CONFIRMED on the split, OVERSTATED on the generalisation** |

Checked 5, confirmed 3, wrong 2 (rows 4 and 5, both partial: correct direction, wrong
magnitude or over-generalised scope).

---

## PART 4: CREDIBILITY GRADE

B05 grades management communication **C** and states it cannot rise to B without documented
delivery evidence. **I concur, and nothing in my independent list argues for a higher
grade.** Everything I found that B05 missed points the same way: an MD&A cash table that
does not reconcile to its own closing cash, a prior-year ROE computed on the wrong equity
base, a Change-% column blanked in the one year the ratios fell, a headcount series that
contradicts itself across three reports, and an employee-cost sentence that states the
opposite of the table beneath it. Against that, the one genuinely constructive fact I found
— that exports supplied roughly 72% of the FY26 increment and the Directors' Report has
disclosed the proxy every year — is a point *for* the disclosure record, and it is the
reason I stop short of arguing for a grade below C. The company does disclose more than B05
credits it with; what it discloses is disorganised, unreconciled and never explained.

---

## PART 5: WHAT I DID NOT DO

- I did not re-audit the eleven peer transcripts. They are the peers' record; Verifier D
  owns peer coverage and B06's verdict discipline.
- I did not verify the financial-statement notes (Note 45, the AOC-1, the related-party
  note). B06's Rs 80.33cr export figure may sit in a note I did not open; I report it as
  NOT FOUND in the sections I read and refer it to Verifier A rather than calling it wrong.
- Scanned-table OCR is a real risk in the results filings. Where a finding rests on a
  scanned cell (m8 in particular) I have said so. Every CRITICAL and MAJOR item above rests
  either on machine-readable AR text or on a figure I cross-footed against another figure
  in the same filing.

```yaml
stage: B12b
company: "TITANBIO"
run_date: "2026-09-16"
model: claude-opus-5
status: complete
independent_flags_found: 29
caught: 3
partially_caught: 4
missed:
  - {severity: "CRITICAL", item: "MD&A cash-flow Table A reports pre-tax operating cash (Rs 3,896.91 lakh) as CFO against audited net CFO of Rs 3,042.08 lakh, omits the Rs 854.83 lakh tax line, and does not reconcile to the closing cash it prints; same unlabelled basis switch recurs for FY24 between AR FY2024 (2,114.63) and AR FY2025 (2,901.66)", anchor: "AR FY2026 MD&A PDF p.104; 30-May-2026 results standalone cash flow PDF p.10; AR FY2024 p.105; AR FY2025 p.100"}
  - {severity: "MAJOR", item: "Exports supplied roughly 72% of the FY26 revenue increment; foreign exchange earned is disclosed in every Directors' Report (FY24 Rs 5,208.41 lakh, FY25 Rs 5,295.20 lakh, FY26 Rs 8,897.37 lakh), moving from 31.4% to 43.2% of revenue", anchor: "AR FY2024 line 2920; AR FY2025 line 3967; AR FY2026 line 4044"}
  - {severity: "MAJOR", item: "FY26 MD&A restates FY25 ROE at 10.70% by dividing FY25 PAT of 1,827.11 by FY26 closing equity of 17,084.15; AR FY2025 reported the same year as Return on Net Worth 12.59%", anchor: "AR FY2026 MD&A p.105 vs AR FY2025 MD&A p.100"}
  - {severity: "MAJOR", item: "AR FY2025 blanks the Change % column for all eight ratios in the one year every ratio deteriorated; AR FY2024 and AR FY2026 populate it", anchor: "AR FY2025 p.100 vs AR FY2024 p.106 and AR FY2026 p.105"}
  - {severity: "MAJOR", item: "Selling and distribution rose 3% to Rs 1,152.78 lakh on revenue up 31.8%, with business promotion, travelling, advertisement and commission cut; FY25 did the inverse (+27.74% on revenue down 5.7%, driven by business promotion). No AR reconciles the two", anchor: "AR FY2026 MD&A p.103; AR FY2025 MD&A p.98"}
  - {severity: "MAJOR", item: "Headcount series does not reconcile across three ARs: 449 (FY24), 424 (FY25, claimed +7.07%, implying base 396), 527 (FY26, claimed +15.09%, implying base 458). Headcount is the only scale proxy disclosed", anchor: "AR FY2024 p.105; AR FY2025 p.100; AR FY2026 p.104"}
  - {severity: "MAJOR", item: "Q4 FY26 revenue fell 13.6% QoQ to Rs 4,883.35 lakh and PAT 16.7% to 655.57, with the Q4 effective tax rate at 36.2% against 25.5% in Q3; no commentary in any filing", anchor: "30-May-2026 results PDF p.7 vs 12-Feb-2026 results PDF p.4"}
pipeline_flags_not_supported:
  - {flag: "B05 Section 3D: 'the only customer/geography signal across three years is the FY24-only split'", severity: "MAJOR", truth: "Foreign exchange earned is disclosed in all three Directors' Reports (5,208.41 / 5,295.20 / 8,897.37 lakh), giving an annual export proxy. The narrower claim that the MD&A percentage split was dropped after FY24 is correct and stands"}
  - {flag: "B05 flag 1 and Sections 1C/2A row 3: consolidated FY26 investing outflow 'Rs 32.55cr / (3,254.59)' and '77% of the outflow'; repeated in B06 Section 2C and Claim 6", severity: "MAJOR", truth: "The cited filing shows consolidated Net Cash Used - Investing Activities (3,441.49), identical to standalone; Rs 3,254.59 lakh does not appear. Correct share is 2,515.67/3,441.49 = 73.1%. The flag itself stands"}
  - {flag: "B06: 'Rs 80.33cr exports FY26', '39%-of-revenue export book', '49% FY26 export growth'", severity: "MAJOR", truth: "NOT FOUND in the AR sections read. AR FY2026 Directors' Report §16 and Annexure-2 give foreign exchange earned Rs 8,897.37 lakh = 43.2% of revenue, +68.0% vs FY24. May sit in an unopened FOB export note; referred to Verifier A"}
  - {flag: "B05 flag 3: cautionary statement claims consolidated basis while quoting standalone figures, graded MEDIUM", severity: "MINOR", truth: "SUPPORTED but OVERSTATED. Identical boilerplate in all three ARs; the MD&A labels its own cash table 'Standalone', the ratio table carries both bases in separate columns, and standalone and consolidated revenue are the same number. Belongs at LOW"}
promise_delivery_spot_checks: {checked: 5, confirmed: 3, wrong: 2}
credibility_grade_concur: "concur — grade C is right; every item B05 missed points the same way, and the one constructive finding (exports drove ~72% of the FY26 increment, disclosed annually in the Directors' Report) is the reason I do not argue for lower"
findings:
  - {severity: "CRITICAL", location: "B05 Section 2A / Section 2D — MD&A cash-flow table not audited", claimed: "MD&A investing line quoted (Rs 34.41cr) with the operating line above it untested", source_truth: "AR FY2026 MD&A p.104 states CFO of Rs 3,896.91 lakh against audited net CFO of Rs 3,042.08 lakh; the table omits Rs 854.83 lakh tax paid and does not reconcile to its own closing cash of 147.77. Same unlabelled basis switch in AR FY2025 for FY24 (2,901.66 vs AR FY2024's 2,114.63)", note: "Repeated across two annual reports; cash conversion is a Section 1B pillar input"}
  - {severity: "MAJOR", location: "B05 Section 2D and Section 3D — FY26 growth mechanism recorded as unexplained", claimed: "'No explanation for the FY26 growth mechanism'; 'the only customer/geography signal across three years is the FY24-only split'", source_truth: "Directors' Report FX earned 5,208.41 / 5,295.20 / 8,897.37 lakh implies exports supplied ~72% of the FY26 increment and rose from 31.4% to 43.2% of revenue", note: "The disclosure that answers B05's own open question was available in all three annual reports"}
  - {severity: "MAJOR", location: "B05 red-flag table / B06 Section 2C and Claim 6 — consolidated investing outflow", claimed: "Rs 32.55cr consolidated outflow, (3,254.59), 77% into the FVTPL portfolio", source_truth: "30-May-2026 consolidated cash flow PDF p.18: (3,441.49). Correct share 73.1%", note: "Underlying flag stands; wrong denominator propagated from B05 into B06 twice"}
  - {severity: "MAJOR", location: "B06 Section 2B / Section 2E / Claim 4 / Part 4 — export figures", claimed: "Rs 80.33cr exports FY26, 39% of revenue, 49% FY26 export growth", source_truth: "NOT FOUND in the AR sections read; Directors' Report §16 gives Rs 8,897.37 lakh, 43.2% of revenue, +68.0% vs FY24", note: "The 49% figure is load-bearing in Claim 4's net read; referred to Verifier A"}
  - {severity: "MAJOR", location: "B05 — FY25 ROE restatement not caught", claimed: "not mentioned", source_truth: "AR FY2026 p.105 gives FY25 ROE 10.70% (= 1,827.11/17,084.15, the FY26 equity base); AR FY2025 p.100 gives 12.59%", note: "Inflates the published FY25-to-FY26 ROE improvement from +3.47pp to +6.62pp"}
  - {severity: "MAJOR", location: "B05 — AR FY2025 blanked ratio Change column not caught", claimed: "not mentioned", source_truth: "AR FY2025 p.100: all eight rows read '- %'; AR FY2024 p.106 and AR FY2026 p.105 populate the column", note: "Blanking confined to the year every ratio deteriorated"}
  - {severity: "MAJOR", location: "B05 Section 2A row 5 — marketing claim tested qualitatively only", claimed: "'the marketing claim cannot be verified as cause of either the fall or the rise'", source_truth: "AR FY2026 p.103: S&D +3% on revenue +31.8% with promotion, travel, advertisement and commission cut; AR FY2025 p.98: S&D +27.74% on revenue -5.7% driven by business promotion", note: "The numbers to test the claim are in the MD&A prose B05 quotes from"}
  - {severity: "MAJOR", location: "B05 — headcount series not tested", claimed: "not mentioned", source_truth: "449 (FY24), 424 with claimed +7.07% (FY25), 527 with claimed +15.09% (FY26); the FY25 and FY26 claims imply bases of 396 and 458", note: "Only scale proxy the company discloses"}
  - {severity: "MAJOR", location: "B05 / B06 — within-year quarterly shape not examined", claimed: "not mentioned", source_truth: "Q4 FY26 revenue Rs 4,883.35 lakh, -13.6% QoQ; PAT 655.57, -16.7% QoQ; Q4 effective tax rate 36.2% vs 25.5% in Q3", note: "No commentary in any filing; relevant to whether the FY26 exit rate supports the FY27 base"}
  - {severity: "MINOR", location: "B05 flag 3 — cautionary-statement basis mislabel graded MEDIUM", claimed: "MEDIUM", source_truth: "Identical boilerplate across all three ARs; MD&A labels its own tables by basis; standalone and consolidated revenue are the same number", note: "Over-called by one severity band; belongs at LOW"}
  - {severity: "MINOR", location: "B05 Section 2D / trigger 1 — like-for-like growth figure", claimed: "'~28.06% like-for-like ex freight'", source_truth: "No company filing quantifies the freight amount; the figure is a Stage 2 derivation", note: "Attributed by B05, but carried to two decimals in the trigger table as if measured"}
  - {severity: "MINOR", location: "B05 trigger 3 / Section 2D — FVTPL portfolio return not cited", claimed: "portfolio flagged; purpose and return profile described as undisclosed", source_truth: "AR FY2026 p.105 ratio table: 'Return on investment (in %) 3.64% (FY26) 7.04% (FY25)' against ROCE 24.09%", note: "The company does disclose the portfolio return; it is the strongest evidence on the allocation and neither report cites it"}
  - {severity: "MINOR", location: "B05 Section 2D / trigger 4 — Titan Media stake escalation not cited", claimed: "associates flagged as a reconciliation gap", source_truth: "Reg 30 28-Feb-2025: voting rights in Titan Media Limited raised to 48.44% from 32.29%, disclosed in five lines with no consideration, valuation or rationale, against a full Annexure-A for a Rs 10.62 lakh arbitration", note: "Disclosure asymmetry is a communication finding and sits in this stage's scope"}
critical_count: 1
major_count: 8
minor_count: 4
material_found: 14
material_caught: 7
acceptance_rate: 50
coverage_basis: "14 material (2 CRITICAL + 12 MAJOR) of 29 listed; 3 fully caught, 4 partially caught, 7 missed; partials counted as caught for the rate. Misses cluster in the MD&A numeric tables and Directors' Report annexures, not in the MD&A prose, where B05's audit is strong and every finding I spot-tested held."
```
