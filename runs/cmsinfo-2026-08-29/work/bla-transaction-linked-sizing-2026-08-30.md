# CMSINFO — Sizing the Transaction-Linked Brown Label ATM Book
Corpus-only extraction. Run: cmsinfo-2026-08-29. Date: 2026-08-30.

Read methods used throughout: "page-marked text" = the `[[PAGE N / M]]`-anchored .txt files in work/txt/; "rasterized" = pdftoppm render of the named PDF page, read as an image. ar_FY23.txt, ar_FY24.txt and ar_FY25.txt carry NO page markers in the extracted text (confirmed by grep before use) — anchors for those three files are PDF page numbers found by paging `pdftotext -layout` through the source PDF and, where load-bearing, verified by rasterizing that PDF page.

---

## TASK 1 — DIRECT DISCLOSURE SEARCH

Searched all four ARs, four concalls, both results filings, both presentation files and the ICRA rationale for: (a) BLA revenue in rupees or as a share, (b) fixed vs transaction-linked pricing split, (c) proportion of contracts fixed-price, (d) BLA machine count.

### (a) Brown Label ATM revenue, in rupees or as a share

**FY25 AR (Annual Report 2024-25), PDF page 9 (printed page 12-13), rasterized** — "REVENUES (%) BY BUSINESS SEGMENT" donut chart, two rings (FY22 outer, FY25 inner), legend: ATM Cash / Retail Cash / CIT / Managed Solutions / Txn-linked BLA / Automation / RMS & Software.
- FY22 ring: ATM Cash 39%, Retail Cash 16%, CIT 12%, Managed Solutions 13%, **Txn-linked BLA 10%**, Automation 7%, RMS & Software 4%.
- FY25 ring: ATM Cash 33%, Retail Cash 16%, CIT 11%, Managed Solutions 15%, **Txn-linked BLA 8%**, Automation 10%, RMS & Software 7%.

This is a direct, named, quantified disclosure: **"Txn-linked BLA" = 10% of consolidated revenue in FY22, declining to 8% in FY25.**

**FY25 AR, PDF page 42 (printed page 78), page-marked text, verified by rasterizing the same page** — Risk section, "Industry and Macro Risks":
> "Selective bidding and participation in the transaction-linked BLA business (the only business with a direct linkage to transaction activity at ATMs), with the contribution further capped at 10% of revenue, compared to 15% earlier"

Two independent things stated here: (i) transaction-linked BLA is explicitly named as CMS's *only* revenue stream with direct transaction-volume linkage (Cash Logistics is explicitly stated elsewhere on the same page as NOT directly impacted by currency volume — see quote under Task 1(b) below); (ii) its contribution is capped at 10% of revenue, down from 15% earlier (an earlier, unnamed year).

**FY24 AR, line 3434 (page-marked text has no page numbers; PDF page not separately verified)** — same risk-register boilerplate, one year earlier:
> "Selective bidding and participation in BLA business (only business with a direct linkage to transaction activity at ATM)."
No percentage given in FY24 AR. The "capped at 10%, down from 15% earlier" quantification first appears in the FY25 AR.

**FY26 AR (Annual_Report_2023.txt, actually the FY26 AR — see run-folder note)**: the equivalent risk paragraph and the "REVENUES BY BUSINESS SEGMENT" donut chart were **searched for and NOT FOUND** anywhere in the FY26 AR text or in a direct PDF text search of Annual_Report_FY26.pdf. CMS appears to have dropped this specific disclosure in the FY26 AR, replacing the old 7-way segment mix with the new 3-platform reporting (ATM Management Solutions / Retail Solutions & Currency Logistics / Technology & Payment Solutions). **NOT DISCLOSED in FY26 AR.**

**Third-party file work/txt/presentation/91190-0df0d62357e045f2aa207869eddbaf82.txt, page 1 (page-marked), line 28** (this file is a broker "Stock Idea Note," not a CMS-authored investor presentation, despite living in the presentation/ folder — flagged for the record, but it is inside the permitted corpus so it is used):
> "As of FY25, the company's total revenue was broken down as follows: ATM Cash accounted for 33%, Retail for 16%, Managed Solutions for 15%, DCV for 11%, Automation for 10%, Txn BLA for 8%, and RMS+SW for 7%."
This numerically reproduces the FY25 AR pie chart exactly (33/16/11/15/8/10/7), which corroborates that the 8% figure was read correctly off the rasterized chart. It is not an independent data point — it is a restatement of the same AR chart.

**Q1 FY27 concall (Aug 2026), page 10/18, direct Q&A** (full quote and derivation under Task 2 below):
> "No, this is the 12% of our revenue, which is from what we call the brown label estate, the transaction-linked ATM revenues." — Anush Raghavan, CBO.

This is the single most explicit rupee-share disclosure in the corpus, and it is current (Q1 FY27, quarter ended 30-Jun-2026): **transaction-linked BLA = 12% of CMS's revenue**, per management's own words.

**Tension across sources, not resolved by the corpus**: FY25 AR chart shows the "Txn-linked BLA" share falling 10%→8% (FY22→FY25) alongside explicit strategic guidance capping it and shrinking it. The Q1 FY27 concall states 12%, i.e. HIGHER than the FY25 figure. Two explanations are visible in the corpus but neither is confirmed as the reason: (i) the FSS acquisition (closing H1 FY27) is separately disclosed as bringing in "some contracts... which would have a transaction exposure" (May-2026 concall, page 14/20 — quoted under Task 1(b)); (ii) "brown label estate, transaction-linked ATM revenues" as used in Aug-2026 may be a broader population than the narrowly-labelled "Txn-linked BLA" pie slice in the FY25 AR chart (which sits in a 7-way split alongside a separate "Managed Solutions" slice; the AR does not define the boundary between the two). The corpus does not disclose which explanation, if either, is correct. **This is flagged, not resolved.**

### (b) Split of revenue between transaction-linked and fixed-fee pricing, however worded

This is extensively and explicitly discussed across the FY26 AR MD&A and three of the four concalls (Nov-2025, Feb-2026, May-2026 — the Aug-2026 call's version is under Task 2).

**FY26 AR (Annual_Report_2023.txt), page 51/147, page-marked text**, MD&A "3.1 What Happened":
> "Since Brown Label ATM contracts are volume-linked, revenues were hit directly."

Same page, "3.2 What Company Did":
> "1. Focusing on Fixed Fee Contracts and wallet share expansion in Private Banks. The Company stopped bidding for contracts linked to transaction volumes and only competed for fixed-price service Contracts. This meant lower short-term revenue but much better quality and certainty of future revenue."

**FY26 AR, PDF page 5 (printed page 04-05), rasterized (text extraction of this multi-column shareholder letter is column-scrambled; rasterization used to confirm accurate reading)** — Rajiv Kaul's shareholder letter:
> "The capex profile is shifting. Through the years following listing, much of our capex went into the cash logistics infrastructure and the BLA ATM business. FY26's ₹352 Cr capex spend was predominantly HAWKAI and managed services, now on fixed-price contracts."
> "...fixed-fee managed services contracts that insulate revenue from transaction-volume swings. These do not eliminate the risk, but they reduce its amplitude." (Risks We Are Watching section, same page)
> "...the mix shift toward fixed-fee contracts and T&PS revenue, combined with operating leverage on a larger revenue base, will continue to rebuild profitability through FY27." (The Year Ahead section, same page)

**May-2026 concall (Q4 FY26 results), page 4/20**, Rajiv Kaul:
> "Given the overall weakness in the MSP segment, we were able to drive a more sensible commercial model of fixed price contracts. Historically, the industry has not been to get off the transaction fee model and I feel, at this stage, for all practical purposes, the transaction fee model is dead in the ATM business. We in fact ourselves won a contract for Rs.700 Crores at a reasonably high transaction fee of Rs.19 per transaction, but we still chose to stick to our principle of not doing any transaction fee model deals. And we did not want to take the risk, even though this could have meant Rs.75 Crores annual revenue to start with at reasonable margins the first few years."

Same call, page 5-6/20:
> "In Q4, we signed our contract deal with FSS for the managed services business... It also helps us influence and shift those contracts from a transaction fee model historically to fixed fee models when those contracts expire."

Same call, page 6-7/20 (FY26 order book):
> "We end FY2026 with a solid order book, not only from size, which is Rs.2,000 Crores, but even if we say so, it is high quality wins. None of these deals is linked to any transaction fee linked contract. All of them are fixed fee models."

Same call, page 8-9/20, Anush Raghavan (interchange as the benchmark transaction price, quoted in full under Task 3):
> "The last RFP that a one bank did, this came at close to Rs.25, which is in any case not an economical price for the bank given interchange is at Rs.19."

Same call, page 12/20, definitional statement of what "BLA model" means:
> "...both private and public sector banks expanded ATM growth rapidly mostly on the back of independent ATM deployers, or what we call the BLA model, executing this on a transaction basis, simply because there was a significant arbitrage to be earned between interchange fee, which is what one bank settled with the other, versus the cost of running an ATM network."

Same call, page 14-15/20, on the FSS acquisition (Divyansh Gupta Q&A):
> "...yes, there would be some contracts of this which would have a transaction exposure. However... in contracts like this, which have already had two, three, four years of transaction history and aging, it is a lot easier to understand how those ATMs are performing..." — Anush Raghavan.
> "The transaction linked business, which is there, I think the very good question, has thankfully been contracted mostly to what I would say a high quality base at reasonable price points. There may have been some impact in the last one year to that base of business..." — Rajiv Kaul.

**Feb-2026 concall, page 3/19**, Rajiv Kaul:
> "FY '24 and '25 saw an increase in competitive intensity, and we sat out on most transaction BLA RFPs where the pricing was pretty low."

Same call, page 4/19:
> "In the ATM business, our focus has been on higher value and yield and more fixed price contracts."

**Nov-2025 concall, page 4/21**, order-win commentary:
> "Order wins for the quarter are at INR500 crores, most of which are fixed price contracts in nature and from leading private sector banks."

**Nov-2025 concall, page 17/21**, CFO Pankaj Khandelwal, on capital work-in-progress:
> "Yes. Couple of projects we have already given like UPI, etcetera, like branch UPI or some of the other fixed price BLA, etcetera. These projects are part of that."

This confirms explicitly that BLA contracts exist in BOTH pricing forms — "fixed price BLA" is named as its own category, distinct from transaction-linked BLA.

**Summary for (b)**: the corpus is unusually rich and consistent on this point. CMS runs BLA (and other managed-services/ATM contracts) under two pricing models — legacy transaction-fee (interchange-linked, currently benchmarked around Rs 19/transaction) and fixed-fee/fixed-price. Management states repeatedly, across FY26 AR and three concalls, that new contract wins since roughly FY25 are effectively all fixed-fee, and that the transaction-fee model is being deliberately run down ("for all practical purposes... dead in the ATM business" — May-2026). The remaining transaction-linked book is the legacy BLA estate, concentrated (per the Aug-2026 call, Task 2) in Tier 2/3 geographies.

### (c) Proportion of contracts that are fixed-price

No single clean percentage-of-contracts figure is disclosed anywhere in the corpus (as distinct from percentage-of-REVENUE, which is covered under (a)). The closest quantified statements:
- FY25 AR: transaction-linked BLA "capped at 10% of revenue, compared to 15% earlier" (a revenue-share cap, not a contract-count share).
- May-2026 concall: "None of these deals [FY26's Rs 2,000 Cr order book] is linked to any transaction fee linked contract. All of them are fixed fee models" — i.e., 100% of the FY26 NEW order book is fixed-fee, but this says nothing about the stock of existing/live contracts.
**NOT DISCLOSED** as a stock-of-contracts percentage; only the revenue-share figures above and the "all new wins are fixed-fee" flow statement exist.

### (d) BLA machine count, standalone or combined

**FY23 AR (ar_FY23.txt, no page marker; Board's Report section)**:
> "the total ATMs under BLA and Managed Services expanded from 12,000 ATMs in FY22 to 18,000 in FY23 led by large wins in Managed Services (Asset Light ATM Management) with Public sector and Private sector Banks."
This is a COMBINED BLA + Managed Services count, not standalone BLA. **Standalone BLA machine count: NOT DISCLOSED** anywhere in the corpus searched (FY23/24/25/26 ARs, all four concalls, both results filings, both presentation files, ICRA rationale). The FY26 AR's PPE useful-life notes (Note 4, both standalone p.80 and consolidated p.112 equivalents) give depreciation categories "Plant and machinery for Brown Label ATMs (BLA)" (10-year life) vs. general plant and machinery (7-year life), and "Furniture, fixtures and fittings for BLA" (7-year) vs. other (10-year) — these confirm BLA sites are accounted for as a distinct asset class but carry no unit counts or rupee gross-block figures broken out separately from total PPE.

---

## TASK 2 — THE Q1 FY27 DERIVATION

All quotes below are from work/txt/concalls/Concall_Aug_2026_Transcript.txt (Q1 FY27 results call, held 11-Aug-2026, covering the quarter ended 30-Jun-2026), page-marked text.

**(a) Total revenue impact — page 3/18, Rajiv Kaul, opening remarks:**
> "The first thing we set out to do this year was to grow our services revenue run rate from INR609 crores in Q4 to INR650 crores. In Q1, we came in at INR625 crores. This is some modest growth on Q4, but is INR25 crores short of what we aimed for. And the shortfall is entirely down to the worst cash supply squeeze this industry has seen in the last decade.
> Banks supplied about 70% of currency what the industry indented for on a daily basis. This is a risk we had called out in our May call, and this INR25 crores revenue loss has an operating deleverage impact on the P&L."

Confirmed again by CFO Pankaj Khandelwal, page 5/18:
> "Total revenue for the quarter was INR635 crores, with services revenue at all-time high at INR625 crores, up 9.3% on a year-on-year basis and 2.6% on a quarter-on-quarter basis. Rajiv and Anush have called out the currency supply impacting services revenue by INR25 crores, out of which INR18 crores in the BLA business and INR7 crores in the Cash Logistics segment."

**(b) BLA-specific impact — page 4/18, Anush Raghavan, Chief Business Officer:**
> "The constraint imposed around currency supply affected distribution, and it was concentrated in Tier 2 and Tier 3 locations, where our transaction BLA estate is. Now this has a direct impact on the operating deleverage for us on 12% of our revenue base.
> On per transaction contracts, an ATM which is not filled does not earn and there is no way to offset the operating costs. Across our own estate, ATMs that stayed well supplied saw transactions flat year-on-year. Those which saw currency supply lower at about 70% saw transactions fall by 27%. So in effect, there is almost a near one-to-one correlation between currency supply and the impact on transaction at these ATMs.
> This, in effect, has lowered our revenues by INR18 crores in the BLA business and impact to us on the cash logistics side from the work that we do for other MSPs is about INR7 crores."

**(c) Stated transaction decline at under-supplied ATMs**: "27%" (above quote), directly. This is materially confirmed and refined by the Q1 FY27 investor presentation (work/txt/presentation/Investor_Presentation_1.txt, page 5/24, chart "CMS Txn. BLA estate (YoY Transaction Impact)"), which gives three tiers, not two:
- Well supplied (≥90% fill): -1.1%
- Partly supplied (70-90% fill): -6.7%
- Under-supplied (<70% fill): **-27.2%**

**(d) Stated behaviour at well-supplied ATMs**: "flat year-on-year" per the concall quote above; the presentation's more precise figure is -1.1% (essentially flat, slightly negative).

**(e) Proportion of CMS's ATMs that were under-supplied**: **NOT DISCLOSED** as a machine-count or ATM-count percentage. The corpus gives only currency-fulfilment-RATE percentages (e.g. "about 70% of currency what the industry indented for," worsening to "as much as only 70%... in April, May," recovering to "80%, 85%" by the time of the call — page 8/18, Anush Raghavan responding to Praveen Kumar), and qualitative geographic concentration ("concentrated in Tier 2 and Tier 3 locations, where our transaction BLA estate is" — page 4/18). No statement gives the count or share of ATMs, as opposed to currency volume, that fell into the under-supplied bucket.

**(f) Period covered**: the Rs 25 Cr / Rs 18 Cr figures are for the FULL Q1 FY27 quarter (April-June 2026), per Pankaj Khandelwal's figures above, which are explicitly tied to "the quarter." Within the quarter, the disruption is described as front-loaded and easing: "somewhere around the May, June — or April, May of Q1, the impact was as much as only 70% of the money that we were indenting... That situation has improved. It has gone up from 70% closer to 80%, 85% now [as of the Aug-2026 call, i.e. into Q2]" (page 8/18, Anush Raghavan). So: full Q1 FY27 quarter, worst in April-May, partial recovery visible by June/into Q2.

### Direct disclosure — not merely inference

Before doing the arithmetic, note that the corpus contains a DIRECT management statement of the answer this task set out to derive. In the Q&A (page 10/18):
> **Umang Shah:** "Understood. And one clarification on your comments. You had mentioned that this shortage has affected 12% of your revenue base. Are you referring to the ATM logistics? Can you say 12% of the revenue base?"
> **Anush Raghavan:** "No, this is the 12% of our revenue, which is from what we call the brown label estate, the transaction-linked ATM revenues."

This is a direct, unambiguous, management-confirmed figure: **the transaction-linked BLA estate = 12% of CMS's total revenue**, as of the Q1 FY27 call. This is not an inference — it is the company's own answer to almost exactly this question, put to them by an analyst on the same call.

### INFERENCE — arithmetic cross-check against the 12% figure

Labelled INFERENCE. Arithmetic, shown in full:
- Revenue lost to the transaction decline at under-supplied ATMs = Rs 18 Cr (disclosed, quarterly, Q1 FY27).
- Stated transaction decline at those ATMs = 27% (disclosed).
- **Assumption 1**: the Rs 18 Cr loss is attributable to the 27% transaction decline at the under-supplied subset of the transaction-linked BLA estate (supported: Anush's passage explicitly links the 27% decline and the Rs 18 Cr figure in the same breath, and Pankaj's figure explicitly labels it "in the BLA business").
- **Assumption 2**: the 27% decline applies uniformly across the affected (under-supplied) subset, and that subset's revenue, absent the decline, is what we are solving for. This treats the Rs 18 Cr as 27% of the affected subset's steady-state quarterly revenue: 18 = 0.27 × affected_quarterly_revenue.
  - affected_quarterly_revenue = 18 / 0.27 = **Rs 66.7 Cr** (quarterly, for the affected/under-supplied subset only).
  - Annualised (×4): **≈ Rs 266.7 Cr**.
  - Against FY26 consolidated revenue of Rs 2,487.18 Cr (Note 19, FY26 AR, page 112/147, page-marked text, consolidated "Revenue from operations 24,871.82" H million = Rs 2,487.18 Cr): 266.7 / 2,487.18 = **≈ 10.7%**, i.e. ~11%.

**This ~11% is a FLOOR on the transaction-linked BLA book, not its total** — it captures only the affected (under-supplied) subset, by construction of the arithmetic. It excludes: (i) any transaction-linked BLA ATMs that stayed well-supplied and kept transacting near-normally (these still count as part of the transaction-linked book but are invisible to this calculation because they didn't generate a revenue shortfall); (ii) the "partly supplied" tier, which the investor presentation shows also lost 6.7% of transactions (a real but smaller loss, not captured in the pure 18cr/27% two-point calculation used here).

**Assumptions the transcript does NOT fully support, flagged**: the 27% figure is described as the transaction decline "at these ATMs" (the under-supplied tier), and the Rs 18 Cr as the BLA-business revenue impact overall — the transcript does not explicitly state that 100% of the Rs 18 Cr sits within the under-supplied tier specifically (vs. some spillover from the partly-supplied 6.7%-decline tier, per the presentation chart). Treating Rs 18 Cr as purely a function of the 27%-decline tier is therefore a simplification; if part of the Rs 18 Cr in fact came from the partly-supplied tier (which has a much larger revenue base and a smaller % decline), the true "affected subset" quarterly revenue implied would be different from Rs 66.7 Cr. This is flagged, not resolved, by the corpus.

**Reconciliation**: the inference-derived floor (~11% of FY26 revenue) sits close to, and slightly below, the directly-disclosed 12% figure. This is a sensible relationship — the 12% figure covers the WHOLE transaction-linked BLA estate (Tier 2/3, "where our transaction BLA estate is"), while the ~11% inference floor covers only the portion of that estate that was actually under-supplied and lost revenue this quarter. The two numbers corroborate rather than contradict each other.

**Bottom line for Task 2**: the transaction-linked BLA book is **directly disclosed at 12% of CMS's total revenue** (Q1 FY27 concall, page 10/18, management confirmation). The independent arithmetic derivation from the Rs 18 Cr / 27% figures produces a floor of **~11% of FY26 revenue**, consistent with and slightly below the direct figure, as expected given the floor only covers the affected subset.

---

## TASK 3 — THE Nov-2025 BLA PASSAGES

All quotes from work/txt/concalls/Concall_Nov_2025_Transcript.txt, page-marked text.

**(a) The 4,500-ATM BLA tender passage — page 4/21, Anush Raghavan:**
> "This gives us visibility of getting to 74,000 to 75,000 ATMs in our cash business by March of this fiscal year. Another major BLA tender for 4,500 ATMs, which are mostly an expansion and not replacement was bid at prices which are very close to interchange levels. This is a clear sign of improving pricing discipline in the ecosystem. At CMS, we are also targeting a 6% improvement in pricing and realizations in our ATM cash business by March."

**(b) Kaul declining BLA projects on return grounds — page 12/21, Rajiv Kaul, in response to a question on segment-level return profiles:**
> "As a principle, we don't normally invest in any project or business unless we are able to see a minimum IRR of 18% or 20% of the business. and ROE in the 18%, 20% range or ROCE in the 20% plus range... We also look at the project should fend for itself. And if you think of it in the last 1 year, we had opportunities for, let's say, having higher growth because in some of the ATMS, which companies won, they could not deploy certain banks came to companies like us to come and take up the project to deployment, and we evaluated it. We had the opportunity to get that business and growth, but we didn't think it will be sustainable in a 3- to 5-year period. And therefore, we didn't take that up. So we sacrifice and we let go of growth, but we weren't confident of the return on the project, let's say, specifically for the BLA segment. So I think, for us, each project has to meet a threshold has to have a margin of safety."

**(c) BLA pricing structure statements, this call or later** — page 17/21, CFO Pankaj Khandelwal, on capital work-in-progress:
> "Yes. Couple of projects we have already given like UPI, etcetera, like branch UPI or some of the other fixed price BLA, etcetera. These projects are part of that."
(This confirms, as of Nov-2025, "fixed price BLA" as a distinct named category alongside transaction-linked BLA — same finding as Task 1(b).)

### INFERENCE — does "interchange levels" imply transaction-priced?

Labelled INFERENCE. Interchange fee is, by construction, a PER-TRANSACTION settlement mechanism between banks (the fee one bank pays another/an ATM deployer per transaction routed through its network). The corpus independently confirms this usage repeatedly and consistently: "given interchange is at Rs.19" (May-2026 concall, per-transaction price benchmark), "the max you can really get at interchange today" (same call, in the context of a transaction-fee-model contract CMS declined), and "a significant arbitrage to be earned between interchange fee... versus the cost of running an ATM network" describing the historical (pre-fixed-fee) BLA operating model (same call, page 12/20). Given this consistent usage across the corpus, a tender "bid at prices very close to interchange levels" most plausibly describes a PER-TRANSACTION pricing structure benchmarked against the interchange rate — because "interchange levels" is not a unit of currency or a fixed monthly sum, it is inherently a per-transaction rate. **This supports, but does not conclusively prove**, that the 4,500-ATM tender referenced in the Nov-2025 call was transaction-priced; the corpus does not contain an explicit statement "the 4,500-ATM tender was a transaction-fee contract."

---

## TASK 4 — CROSS-CHECK AGAINST THE LESSOR NOTE

FY26 AR Note 29 "Group as lessor," page-marked text page 127/147, **verified by rasterizing PDF page 127** (image matches the extracted text exactly; no column-collapse found on this page).

Full note text:
> "**Group as lessor**
> The Group has entered into lease arrangement for its ATM management and Remote monitoring service business. These leases have terms ranging between five and seven years. Future minimum rentals receivable under non-cancellable operating leases are, as follows: [table: Within one year 2,119.82 / After one year but not more than five years 4,906.02 / More than five years 1,100.47 / Total 8,126.31 — all H million, March 31, 2026 column]
> During the year, the Group has recognized H 1,753.12 million (March 31, 2025 - H 1,264.10 million) as income in relation to the above arrangements. These are reported under sale of services (refer note 19).
> The following are the details of the Plant and Machinery (ATM and Remote Monitoring Equipments) given on lease: Gross block value as at 3,127.92 [March 2026] / 2,434.70 [March 2025]; Net block value as at 2,303.94 / 1,690.24; Depreciation for the year 309.27 / 275.73."

**(a) Does the AR anywhere state whether this lease income is fixed or transaction-linked?** **NOT DISCLOSED explicitly.** The note does not use the words "fixed," "variable," "transaction-linked," "usage-based," or any equivalent to characterise the nature of the Rs 1,753.12 million.

**(b) Is the Rs 1,753.12 million the FIXED-fee portion of the owned-machine book, with transaction-linked BLA sitting outside it, or does it include both?** **NOT DISCLOSED explicitly** which of these is correct. However, an INFERENCE, clearly labelled: under Ind AS 116, a lessor's disclosure of "future minimum rentals receivable under non-cancellable operating leases," presented as a fixed schedule by time bucket (within 1 year / 1-5 years / more than 5 years), is the standard treatment for FIXED (non-contingent) lease payments. Variable/contingent lease payments that depend on usage (e.g. transaction volume) are a separately-required disclosure category under Ind AS 116 (as "variable lease payments not included in the measurement of minimum lease payments") and are NOT present anywhere in this note or elsewhere in the FY26 AR's lease disclosures. The absence of any variable/contingent-rent disclosure, combined with the presence of a clean minimum-rentals schedule, is consistent with — but does not conclusively prove — the Rs 1,753.12 million being entirely fixed-rental income. Two further ambiguities the AR does not resolve: (i) whether "ATM management and Remote monitoring service business" (the note's own description of what is leased) is coextensive with "Brown Label ATMs" at all, or is a distinct/broader leasing arrangement (e.g. hardware leased to banks who then operate it themselves, rather than CMS-operated BLA machines); (ii) whether this lessor arrangement sits inside or outside the Managed Services segment's revenue that also carries the transaction-linked BLA book.

**(c) If not stated, NOT DISCLOSED, no inference forced beyond the above** — the above paragraph is explicitly labelled as an accounting-standard-structure inference, not a corpus statement, and is not represented as settling the question. Given the ambiguity in (b) about what exactly is being leased, this report does NOT assert that Rs 1,753.12 million = 7.0% of revenue is "the fixed owned-machine book" as a bound on the problem from the other side — the two conditions the task set for making that statement (a) or (b) affirmatively supporting it are not met by the corpus.

---

## TASK 5 — THE EBIT-VS-EBITDA DIVERGENCE (pinned)

**Identifying the Q1 FY27 filing**: work/txt/results/e21eec72-688c-4d1b-8735-d95491b67fc3.txt is the correct file — its cover letter (page 1/12) is dated August 10, 2026 and states "Un-Audited Financial Results (Standalone and Consolidated) for the quarter ended June 30, 2026." (The other file, 05f75e67...txt, is dated May 14, 2026 and covers the quarter/year ended March 31, 2026 — FY26 audited full-year/Q4 results, not Q1 FY27.)

### Filed consolidated figures, Q1 FY27 (quarter ended 30-Jun-2026), all H million, page 10/12

| Line | Q1 FY27 (Jun-26) | Q4 FY26 (Mar-26) | Q1 FY26 (Jun-25) | FY26 (year) |
|---|---|---|---|---|
| Revenue from operations | 6,346.97 | 6,329.34 | 6,274.05 | 24,871.82 |
| Other income | 151.14 | 97.66 | 163.55 | 456.60 |
| Total Income | 6,498.11 | 6,427.01 | 6,437.60 | 25,328.42 |
| Finance costs | 62.11 | 63.19 | 41.22 | 194.79 |
| Depreciation & amortization | **727.64** | 593.24 | 445.23 | 2,076.39 |
| Total Expenses | 5,448.25 | 5,373.81 | 5,181.65 | 21,181.94 |
| PBT (before exceptional items) | 1,049.86 | 1,053.20 | 1,255.95 | 4,146.48 |
| Tax expense | 213.02 | 281.23 | 320.16 | 1,020.12 |
| PAT | 836.84 | 790.60 | 935.79 | 3,033.92 |

Segment note, page 11/12, consolidated:

| Segment | Q1 FY27 Revenue | Q1 FY27 Result | Q1 FY26 Revenue | Q1 FY26 Result |
|---|---|---|---|---|
| Cash Management services | 4,026.87 | 815.41 | 4,170.35 | 998.23 |
| Managed services | 2,865.86 | 279.99 | 2,440.15 | 329.10 |
| Card services | 185.18 | 34.58 | 137.54 | 33.23 |
| Total Segment Results | | 1,129.98 | | 1,360.56 |
| Less: Unallocated corporate expenses | | 169.13 | | 226.94 |
| **Profit before other income, finance costs and tax** | | **960.85** | | 1,133.62 |

Media release (Annexure I, page 2/12) — the company's own headline non-GAAP disclosure:
> "EBITDA ₹173 Cr, EBITDA Margin 27.2% (+190bps YoY, +170bps QoQ)... PAT ₹84 Cr."
> "Segmental — Cash Logistics: Revenue ₹403 Cr, EBIT ₹81 Cr (YoY -18%, QoQ +3%). Managed Services & Technology Solutions* (Revenue ₹305 Cr, EBIT ₹32 Cr, YoY -13%, QoQ -24%). *Including Card Services. Segment EBIT reflects the flow-through of lower BLA transaction revenue and a higher depreciation charge."

Investor presentation (Investor_Presentation_1.txt, page 9/24) shows the same split with explicit margins: "MS" (Managed Services & Technology Solutions, incl. Card) EBIT% = **10.3%** in Q1 FY27, vs **14.1%** in both Q1 FY26 and Q4 FY26, footnoted "*MS EBIT impacted due to flow through impact of dip in BLA revenues to margin."

### Arithmetic — reconciling the 10.3% figure to the filed segment table

"Managed Services & Technology Solutions" in the media release/presentation = statutory "Managed services" segment + "Card services" segment combined (explicitly stated: "*Including Card Services").

- Q1 FY27: Revenue = 2,865.86 + 185.18 = 3,051.04 mn (₹305.10 Cr). Result = 279.99 + 34.58 = 314.57 mn (₹31.46 Cr).
  - Margin = 314.57 / 3,051.04 = **10.31%** — matches the concall/presentation's "10.3%" to two decimal places.
- Q1 FY26 (year-ago): Revenue = 2,440.15 + 137.54 = 2,577.69 mn (₹257.77 Cr). Result = 329.10 + 33.23 = 362.33 mn (₹36.23 Cr).
  - Margin = 362.33 / 2,577.69 = **14.06%** — matches the "14.1% a year ago" figure.

**This exactly reconciles.** The 10.3% (Q1 FY27) and 14.1% (Q1 FY26) figures the concall's CFO quotes as "EBIT" and "Managed Services EBIT" are the "Managed services" + "Card services" statutory segments combined, margin computed on that combined segment's own revenue — confirmed independently from the filed regulatory segment note, the media release, and the investor presentation, all three of which agree to the decimal.

### Arithmetic — the whole-company EBIT margin (a different, broader number)

Two ways to compute company-wide (all-segment) EBIT from the filed P&L, both distinct from the 10.3%/14.1% figures above because they include the much more profitable Cash Management/Cash Logistics segment:

1. **Operating EBIT (excludes other income)** = "Profit before other income, Finance costs and tax" per the segment note = 960.85 mn on Revenue from operations of 6,346.97 mn = **15.14%**.
2. **Total EBIT (includes other income)** = PBT + Finance costs = 1,049.86 + 62.11 = 1,111.97 mn, on Revenue from operations = **17.52%** (or 17.11% on Total Income including other income in the base).

The media release's own Segmental table sums to a similar figure independently: Cash Logistics EBIT ₹81 Cr + Managed Services & Tech EBIT ₹32 Cr = ₹113 Cr total company EBIT (excl. unallocated-corporate-expense presentation nuance and other income), on ₹635 Cr total revenue = **17.8%**, consistent with the "Total EBIT" calc above within rounding.

### Verdict — is 10.3% or ~15% correct, or both wrong?

**Both figures are correct, but they measure different populations, and the corpus fully supports this once the segment scope is made explicit — neither figure is wrong.**

- **10.3%** is the ACTUAL Q1 FY27 EBIT margin of the "Managed Services & Technology Solutions" segment (statutory Managed services + Card services combined) — the segment that houses the transaction-linked BLA book. This figure IS the correct, filed-figure-reconciled reading of what the concall's CFO called "the EBIT for Q1" and "EBIT margin" in the passage the verifier flagged — provided the reader understands it as a segment metric, not a whole-company metric. It compresses from 14.1% (Q1 FY26) because of the Rs 18 Cr BLA transaction-revenue shortfall landing almost entirely inside this segment, on top of a segment-specific depreciation step-up (FY26 capex of ₹352 Cr, mostly HAWKAI/managed-services related, vs. the ₹200 Cr historical run-rate — FY26 AR page 5, CFO commentary Aug-2026 call page 6/18).
- **~15%** (from the secondary source's D&A-based reconstruction, and also close to management's own stated counterfactual — "if not for the INR18 crores revenue impact, the EBIT would have been 15%," Aug-2026 call page 5/18) is close to the correct WHOLE-COMPANY operating EBIT margin computed directly from the filed segment note: **15.14%**. This is a materially different, and much larger, population than the Managed Services segment alone — it includes the Cash Logistics segment, which ran at a much higher ~20.1% EBIT margin (₹81 Cr / ₹403 Cr) in the same quarter and dilutes the blended company-wide figure upward relative to Managed Services alone.
- The secondary source's D&A figure of "~Rs 73 crore" is itself accurate — the filed consolidated D&A for Q1 FY27 is Rs 727.64 million (₹72.76 Cr), matching almost exactly. Where the secondary source appears to go wrong (this report cannot confirm the secondary source's own working, since the research PDFs were not opened) is in applying that whole-company D&A figure to reconstruct a whole-company EBIT margin, and then treating that as if it contradicted the 10.3% figure — when the 10.3% figure was never a whole-company number in the first place. There is no contradiction once the segment scope is made explicit; the discrepancy is a scope confusion, not a factual error in either figure.

**Load-bearing conclusion for the proof gate**: the 10.3%→14.1% EBIT compression is real, filed, and correctly scoped to the segment carrying the transaction-linked BLA book (Managed Services & Technology Solutions). It should NOT be read as a whole-company EBIT margin collapse — the whole-company operating EBIT margin for Q1 FY27 was a materially healthier ~15.1% (or ~17.5% including other income), still down from the comparable whole-company margin a year ago (this report did not separately reconcile a whole-company Q1 FY26 EBIT margin from the FY26-period segment note beyond what is shown in the table above; that full reconciliation is available from the same segment-note format for Q1 FY26 for further work if needed: Q1 FY26 Total Segment Results 1,360.56 mn less Unallocated corporate expenses 226.94 mn = 1,133.62 mn, on Revenue 6,274.05 mn = 18.07% operating EBIT margin whole-company — i.e. the whole-company operating EBIT margin fell from ~18.1% to ~15.1% YoY, a real but much smaller compression than the segment-level 14.1%→10.3% move).

---

## VERIFICATION QUESTION

### Files quoted, with date/period and read method

| File | Date/period | Read method |
|---|---|---|
| work/txt/annual-report/Annual_Report_2023.txt (= FY26 AR, "Annual Report 2025-26") | FY26 (year ended 31-Mar-2026) | Page-marked text; pages 5, 51, 80/112 (equivalent), 127 verified/checked by rasterizing the corresponding pages of inputs/annual-report/Annual_Report_FY26.pdf |
| work/txt/ar_FY25.txt | FY25 AR ("Annual Report 2024-25") | Page-marked text NOT present in this file (confirmed absent by grep); PDF page numbers located via `pdftotext -layout` page-by-page search of inputs/annual-report/Annual_Report_FY25.pdf; PDF pages 9 and 42 (load-bearing figures) verified by rasterizing |
| work/txt/ar_FY24.txt | FY24 AR | Page-marked text NOT present (confirmed absent); cited by content/section only, PDF page not separately verified (not load-bearing to the sizing conclusion) |
| work/txt/ar_FY23.txt | FY23 AR | Page-marked text NOT present (confirmed absent); cited by content/section only (Board's Report), PDF page not separately verified |
| work/txt/concalls/Concall_Aug_2026_Transcript.txt | Q1 FY27 call, 11-Aug-2026 | Page-marked text |
| work/txt/concalls/Concall_May_2026_Transcript.txt | Q4/FY26 results call, 15-May-2026 | Page-marked text |
| work/txt/concalls/Concall_Feb_2026_Transcript.txt | Q3 FY26 call, 13-Feb-2026 | Page-marked text |
| work/txt/concalls/Concall_Nov_2025_Transcript.txt | Q2 FY26 call, 06-Nov-2025 | Page-marked text |
| work/txt/results/e21eec72-688c-4d1b-8735-d95491b67fc3.txt | Q1 FY27 results filing, quarter ended 30-Jun-2026, filed 10-Aug-2026 | Page-marked text |
| work/txt/presentation/Investor_Presentation_1.txt | Q1 FY27 investor presentation (accompanies Aug-2026 call) | Page-marked text |
| work/txt/presentation/91190-0df0d62357e045f2aa207869eddbaf82.txt | Third-party broker note referencing FY25 data | Page-marked text (flagged as non-CMS-authored; used only to corroborate the FY25 AR chart, not as an independent source) |
| work/txt/rating/142128.txt | ICRA rating rationale | Page-marked text (not load-bearing; only high-level segment splits found, no BLA-specific figures) |

Not quoted / not needed: work/txt/results/05f75e67-7f39-4b02-b881-c6635b448b71.txt (confirmed to be the FY26/Q4 filing, not Q1 FY27, and set aside once identified).

### Confirmation on excluded files

**inputs/research/rpt1.pdf, "rpt 2.pdf" and "rpt 3.pdf" were NOT opened, read, or used at any point in this task.** No content from them appears anywhere above.

### Final answer

**YES — the transaction-linked BLA book can be sized from the corpus, and it does not require the excluded research reports or the "<10%" forum estimate.**

- **Tier 1 (direct, current, management-confirmed)**: **12% of CMS's total revenue** — explicit statement by CBO Anush Raghavan in direct response to an analyst's question on the Q1 FY27 (Aug-2026) call: "this is the 12% of our revenue, which is from what we call the brown label estate, the transaction-linked ATM revenues."
- **Tier 1 (direct, historical, from filed ARs)**: **8% of revenue in FY25, 10% in FY22** (FY25 AR pie chart), and separately, **"capped at 10% of revenue, compared to 15% earlier"** (FY25 AR risk-register text) — both explicit, both from audited/board-approved Annual Report disclosures, not estimates.
- **Tier 2 (arithmetic floor, cross-validating Tier 1)**: **≈11% of FY26 revenue**, derived from the disclosed Rs 18 Cr BLA revenue impact and 27% transaction decline, clearly labelled as a floor on the affected subset only, not the full book — and consistent with, not contradicting, the 12% direct figure.

The three independent figures (8-10% historical AR disclosure, ~11% arithmetic floor, 12% current direct disclosure) triangulate tightly around a range that has moved from roughly 8-10% (FY22-FY25) to roughly 11-12% (Q1 FY27) of consolidated revenue. The upward movement across that window is real in the corpus but its cause (FSS acquisition transaction-exposed contracts vs. a scope difference in how "transaction-linked BLA" is defined between the AR chart and the concall) is flagged, not resolved.
