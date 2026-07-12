# B02 — Notes to Financial Statements: PASS 2 (What Was Missed)
Company: Amagi Media Labs Limited (AMAGI) | Run date: 2026-07-12
Source: same IPO Prospectus dated January 16, 2026, `inputs/annual-report/_text/1772447113177.txt`. Re-read Note 1 through Note 54 (Annexures V/VI) plus Annexure VII (Statement of adjustments) in full against the Pass 1 output.

**UNIT NOTE (unchanged):** figures quoted in ₹ million first (document's native unit), ₹ Crore in parentheses (÷10).

This pass reports ONLY items not covered, or covered incompletely, in Pass 1. Items already rated/anchored in Pass 1 (audit trail, cloud commitment jump, transfer-pricing dispute quantum, ESOP/SAR cash-out total, zero hedging, M&A track record, Vinculum pricing existence, MSME recurrence, gratuity assumptions, receivables/customer concentration, DTA non-recognition, revenue disaggregation) are NOT repeated here even where additional detail was found in the underlying note, unless that detail materially changes the reading.

---

## NEW FINDINGS

### 1. The mechanism behind the recurring "Fair value of additional equity shares" charge: a Bonus CCPS conversion-ratio ratchet tied to valuation milestones
(Note 18B(b), p.347-348; Note 48, p.380) 🔴 Red Flag — new mechanism, not previously identified

Pass 1 flagged the recurring ~₹80 mn/period "Fair value of the additional equity shares issuable to the shareholder" charge (Note 35/48) as a puzzling recurring "one-time" item but did not identify its source. Note 18B(b) discloses that at the October 7, 2024 EGM (1st amendment to the SHA), the conversion ratios of several Bonus CCPS series were changed dramatically upward, e.g.:
- Series F CCPS: 1:1 → 36:1
- Series E CCPS (Type 4): ~1.0146:1 → 36.5252:1
- Series A2/B1/C1/C-CCPS1/D-CCPS1 Bonus CCPS: ~0.3521-0.4986:1 → 12.6763-17.9492:1
- Class D CCPS (Type 3): ~1.9444:1 → 69.99998:1

Note 48 explains: "certain shareholders of the Holding Company were entitled for additional equity shares on such conversion by diluting certain incoming investors and achievement of valuation related milestones." This is a ratchet-style anti-dilution mechanic benefiting Bonus CCPS holders (plausibly promoter/founder-linked series, given the naming convention) at the expense of other investors, and it is explicitly tied to valuation milestones — meaning the charge could recur or step up again as the company's valuation rises post-IPO if any similar unconverted instruments remain. Note 48 also links this note directly to the July 21, 2025 Vinculum Advisors LLP share purchase (Note 18A(b)) and states the additional-share fair value "is arrived based on the independent valuation performed by registered valuer" — this is new information that an independent valuer was involved in that transaction (Pass 1 flagged the absence of an evidenced fairness basis; a registered-valuer valuation did occur, though it does not resolve the ₹25/share price gap versus institutional cost bases of ₹21.45-₹172.16/share cited in Pass 1).

### 2. Promoter/promoter-group ownership jumped from 21.72% to 31.74% in H1 FY26 via the Vinculum transaction
(Note 18A(b) footnote, Note 18A(c), p.346, 350) 🟡 Watch — quantification not present in Pass 1

Note 18A(c) ("Details of shares held by promoters/promoter group") shows the combined promoter + Vinculum Advisors LLP stake rose from 7,421,724 shares (21.72%) at the start of H1 FY26 to 10,930,654 shares (31.74%) at September 30, 2025 — a ~46% relative increase in promoter-group voting control in the six months immediately preceding the IPO, driven entirely by the ₹25/share Vinculum acquisition of shares from institutional sellers (Pass 1's Finding 7). This concentration shift was not quantified in Pass 1.

### 3. ₹3,173.98 mn cash-settled SAR/ESOP liability converted to equity via "modification" accounting — a second, larger and non-cash component of the pre-IPO SBC restructuring
(Note 19, p.349; Note 43(a)(vii)/(c), p.368-370; Note 44 Level 3 roll-forward, p.371) 🔴 Red Flag — materially expands Pass 1 Finding 4

Pass 1 quantified the ~₹1,351.78 mn CASH paid out in Q1 FY26 to settle vested ESOPs/SARs. Pass 2 finds a second, larger and distinct component: at March 31, 2025 the Group carried Level-3 fair-valued cash-settled liabilities of ₹2,167.50 mn (SAR) + ₹1,991.74 mn (ESOP) = ₹4,159.24 mn (₹415.92 Cr) — nearly 82% of total equity at that date (₹5,094.52 mn). Note 44's Level-3 roll-forward shows this entire balance was extinguished by September 30, 2025 through: (i) cash paid of ₹408.23 mn (SAR) + ₹605.62 mn (ESOP) = ₹1,013.85 mn; (ii) a small residual net P&L charge (~₹28.6 mn); and (iii) "Modification of cash settled share based plan to equity settled share based plan" of ₹1,727.69 mn (SAR) + ₹1,446.29 mn (ESOP) = ₹3,173.98 mn (₹317.40 Cr) derecognized from the liability and credited directly to the "Employee stock options outstanding" equity reserve (Note 19). This ₹3,173.98 mn is a non-cash but highly dilutive equity-reserve creation, separate from and in addition to the cash payouts Pass 1 already flagged — the full pre-IPO SBC restructuring resolved roughly ₹4.5 Cr-equivalent of legacy liability (cash + equity) in a single quarter, and the equity portion should be explicitly reflected in any post-IPO fully-diluted share/equity-value bridge used in later stages.

### 4. Fragmented, hard-to-reconcile cash flow statement presentation of the SBC cash settlement
(Cash flow statement, p.324; Note 19, p.349; Note 44, p.371-372) 🟡 Watch — new observation, cash flow quality issue

Only ₹339.90 mn appears as an explicit financing-activities line in the H1 FY26 cash flow statement ("Cancellation and settlement of vested employee stock options"). But Note 44's Level-3 roll-forward shows ~₹1,013.85 mn was actually paid in cash against the SAR/ESOP liabilities in the same period (finding 3 above), and this larger amount is not separately labelled anywhere in the cash flow statement — it appears to be absorbed within the ₹(1,000.44) mn "(Decrease)/Increase in other financial liabilities" working-capital line inside OPERATING cash flow. Practical effect: H1 FY26 reported operating cash flow (₹2,005.95 mn net outflow) is depressed by what is substantially a one-time, IPO-related compensation settlement rather than ordinary working-capital movement, and an analyst relying on the face of the cash flow statement alone (without cross-referencing Notes 19, 43 and 44) would misclassify this as recurring operating cash burn. This should be explicitly adjusted for in any normalized FCF calculation at stage 11.

### 5. Fresh KMP stock option grants dated May 24, 2025 and June 20, 2025, immediately pre-IPO
(Note 37E(ii), p.355) 🟡 Watch — new item, not in Pass 1

The KMP interest-in-ESOP table discloses two new grants to key managerial personnel: 188,028 options granted May 24, 2025 (expiry May 22, 2035) and 483,000 options granted June 20, 2025 (expiry June 18, 2035) — both issued in the same window as the ESOP 2025 plan consolidation and roughly six months before the IPO. This is incremental to Pass 1's finding of rising KMP cash compensation and adds a fresh equity-dilution dimension timed to the listing.

### 6. ESOP 2025 performance-vesting milestones disclose management's own internal enterprise-valuation targets: ₹270,000 mn and ₹345,000 mn
(Note 43(c), p.368) 🟡 Watch — informational, explicitly NOT a valuation input per pipeline rules

The Amagi Employee Stock Option Plan 2025 "Performance based grants" vest 50% upon the Group achieving an enterprise valuation of Rs. 270,000 million (₹27,000 Cr) and the remaining 50% at Rs. 345,000 million (₹34,500 Cr). This is a management-set internal reference point (not a third-party valuation, not sanctioned by Section 1B v3.3) and per CLAUDE.md must NOT be used as an exit-multiple or valuation input in stage 11 — flagged here only so the pipeline is aware of it and does not inadvertently anchor to it.

### 7. India Holding Company remained loss-making even in the Group's first-ever profitable period (H1 FY26)
(Note 47, Statutory Group Information as at September 30, 2025, p.378) 🔴 Red Flag — sharpens and updates Pass 1 Finding 6/8 with H1 FY26 data

Pass 1's Finding 6 used FY25 entity-level data to show the India entity was the primary consolidated loss driver. The September 30, 2025 entity-level table (not examined in Pass 1) shows this pattern persisted into the profitable H1 FY26 period itself: Amagi Media Labs Limited (India, standalone) reported a LOSS of ₹(121.23) mn (-187.38% of consolidated Restated PAT) for H1 FY26, while 100% of the ₹64.70 mn consolidated profit was generated by foreign subsidiaries (Amagi Corporation USA +₹79.35 mn, Amagi Media Private Ltd UK +₹97.71 mn, Amagi Media Labs Pte Singapore +₹18.35 mn, Amagi Eastern Europe +₹10.22 mn, Amagi Media UK +₹5.43 mn). This materially sharpens the investment-thesis caveat: the company's first-ever profitable period is entirely a foreign-subsidiary phenomenon; the India entity has not reported a profit in any period across the full track record (FY23 through H1 FY26). This is directly relevant to (a) the ongoing India transfer-pricing dispute, where tax authorities are effectively arguing the India entity is under-compensated by the intercompany pricing, and (b) any assumption in stage 11 about future India tax-paying capacity or use of the ₹6,394.20 mn unrecognised India tax-loss shield (Pass 1, Section 10).

### 8. Consultant "Cash Bonus Plan" liability explicitly triggered by the IPO as a defined "liquidity event"
(Note 43(b)(ii), p.371-372; Note 21, p.350) 🟡 Watch — new item, forward-looking cash obligation

Certain consultants who waived vested Stock Appreciation Rights (under SAR Schemes IV, V New Hire and V Performance) in July 2025 received in exchange a "Cash Bonus Plan" award from the subsidiary companies. Payment terms: "the cash bonus would be paid to the consultant upon earlier of two years from the date of liquidity event as defined in the plan or termination of services for a reason other than cause or the tenth anniversary of the award date, whichever is earlier." The IPO itself is the "liquidity event" — this creates a defined future cash-outflow trigger within two years of listing. Only the accrued-to-date portion (₹63.14 mn, Note 21, "Liability for cash bonus plan") is on the balance sheet at September 30, 2025; the "unaccrued" tranche continues to build with service and is explicitly formula-linked to the Group's revenue growth per the plan terms, meaning the ultimate cash quantum is not yet fully determinable from the notes as disclosed.

### 9. Annexure VII confirms zero restatement adjustments across all five periods, but "Material Regroupings" (Part C) is disclosed only generically
(Annexure VII Parts A and C, p.382-383) 🟢 Clean (Part A) / 🟡 Watch (Part C, minor transparency gap)

Annexure VII Part A explicitly reconciles both restated profit/(loss) and restated total equity to the audited consolidated financial statements for every period (September 30, 2025, September 30, 2024, March 31, 2025, March 31, 2024, March 31, 2023) with "Total (B) = Nil" in every column — i.e., there were no material restatement adjustments, no accounting-policy changes, and no material reclassifications between the audited financials and the Restated Consolidated Summary Statements presented in the Prospectus for any period. This is a genuine positive accounting-quality data point (feeds `restatements_found: []`). However, Part C ("Material Regroupings") states only that "appropriate re-groupings have been made... wherever required" without disclosing whether any regroupings in fact occurred, or their nature/amount — a generic boilerplate statement, in contrast to the fully quantified Nil-adjustment disclosure in Part A. Minor disclosure-transparency gap, not a red flag.

### 10. Minor items
- **Expenses recoverable from shareholders**: ₹163.85 mn at September 30, 2025 (Note 16, p.345) — IPO-related expenses incurred by the Holding Company, recoverable from the Offer-for-Sale selling shareholders in proportion to shares offered. Routine IPO-cost-sharing mechanic, not previously noted. 🟢 Clean/informational.
- **Pre-track-record CCPS/OCPS history**: at the April 1, 2021 Ind AS transition date, CCPS/OCPS were initially classified as a financial LIABILITY at fair value of ₹5,572.29 mn (redemption feature not within the Group's control), then reclassified to equity (₹8,416.83 mn split CCPS/OCPS, plus ₹2,563.87 mn reclassified to securities premium) in August 2021 once a new funding round removed the buy-back obligation (Note 18B(a)(iii), p.347). Pre-dates the FY23-H1FY26 track record window; included here only as structural context for the preference-share mechanics already flagged elsewhere. 🟢 Informational, no action needed.

---

# PASS 2 NEW FINDINGS SUMMARY

1. 🔴 CCPS Bonus-series conversion-ratio ratchet (Oct 7, 2024 EGM), tied to valuation milestones, is the disclosed mechanism behind the recurring "fair value of additional shares" P&L charge; independent registered valuer was used for the linked Vinculum ₹25/share transaction. (Note 18B(b), Note 48)
2. 🟡 Promoter/promoter-group stake rose from 21.72% to 31.74% (a ~46% relative increase) via the Vinculum transaction in H1 FY26. (Note 18A(b), 18A(c))
3. 🔴 A second, larger, non-cash SBC restructuring component: ₹3,173.98 mn of cash-settled SAR/ESOP liability (82% of March 2025 equity) converted directly into an equity reserve via modification accounting, separate from the ~₹1,351.78 mn cash payout Pass 1 already flagged. (Note 19, Note 43, Note 44)
4. 🟡 The H1 FY26 SBC cash settlement (~₹1,013.85 mn per Note 44) is not visibly separated in the cash flow statement — only ₹339.90 mn appears in financing activities; the rest is buried in an operating working-capital line, depressing reported operating cash flow without clear one-time labelling. (Cash flow statement; Notes 19, 44)
5. 🟡 Fresh KMP option grants (188,028 and 483,000 options) dated May 24 and June 20, 2025, immediately pre-IPO. (Note 37E(ii))
6. 🟡 ESOP 2025 performance-vesting milestones disclose internal enterprise-valuation targets of ₹27,000 Cr and ₹34,500 Cr — informational only, explicitly excluded as a valuation input per CLAUDE.md. (Note 43(c))
7. 🔴 India Holding Company was loss-making (₹-121.23 mn) even during the Group's first-ever profitable period (H1 FY26); 100% of consolidated profit came from foreign subsidiaries — sharpens the transfer-pricing and India-profitability concern with H1 FY26 data not used in Pass 1. (Note 47)
8. 🟡 Consultant "Cash Bonus Plan" liability explicitly crystallizes within two years of the IPO ("liquidity event"); only the accrued portion (₹63.14 mn) is on balance sheet, unaccrued tranche is revenue-growth-linked and not yet fully quantifiable. (Note 43(b)(ii), Note 21)
9. 🟢/🟡 Annexure VII confirms zero restatement adjustments across all five periods (clean); but "Material Regroupings" (Part C) disclosure is generic/unquantified (minor transparency gap). (Annexure VII Parts A, C)
10. 🟢 Minor: ₹163.85 mn IPO-cost recoverable from selling shareholders (Note 16); pre-track-record CCPS/OCPS liability-to-equity reclassification history at Ind AS transition (Note 18B(a)(iii)) — informational context only.

**Total new findings this pass: 10** (4 rated Red Flag, 5 rated Watch, 1 mixed Clean/Watch, plus 1 minor/informational sub-item group).
