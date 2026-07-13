# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Company: C.E. Info Systems Ltd (MAPMYINDIA) | Run date: 2026-07-13
Source: inputs/_text/annual-report__Annual_Report_2023.txt (FY2024-25 Annual Report, FY25 vs FY24;
see Pass 1's provenance flag — file mislabeled, actual content is the 30th AR, year ended 31.03.2025)

Basis: full re-read of Notes 1–52 (standalone and consolidated) against the Pass 1 output supplied.
Only new findings, or findings that materially refine a Pass 1 item, are reported below. Units
converted to ₹ Crore (÷100 from source ₹ lakh) throughout; lakh figures retained in-line for audit
trail on first use.

---

## 1. ACCOUNTING POLICIES / PP&E — NEW: quantified, unlabelled write-off

- **IoT devices on rent — management wrote off ₹5.70 Cr of gross carrying value this year**, stated
  plainly in the note: *"During the year management has decided to write off the rental devices
  which were not in active use and life of the devices had expired"* (Note 3(b), standalone p.129,
  consolidated p.184 — identical ₹570 lakh gross / ₹481-482 lakh accumulated-depreciation
  scrap-out figure in both books, confirming this specific write-off event sits entirely at the
  **parent** level, not at Gtropy). The associated P&L line **"Loss on scrapping-out IoT devices on
  rent"** is new this year: ₹0.89 Cr standalone / ₹0.88 Cr consolidated vs **nil** in FY24 (Note 24
  standalone p.141-142, Note 23 consolidated p.196-197). 🟡 Watch — this is a real, quantified,
  one-time charge sitting inside "Other expenses" with no separate exceptional-item label,
  reinforcing (and now quantifying) Pass 1's Section 12 observation that the company has no
  exceptional-items line despite having genuinely one-time items.
- **Counter-finding, same note: the Gtropy-level IoT-devices-on-rent fleet is expanding fast, not
  shrinking.** Consolidated gross carrying value rose ₹19.13 Cr → ₹26.14 Cr (+36.6%) even after
  absorbing the ₹5.70 Cr write-off (i.e. gross additions were ₹12.71 Cr vs ₹7.75 Cr PY, +64%); net
  carrying value rose ₹10.70 Cr → ₹16.87 Cr (+57.7%); depreciation charge on this asset class rose
  ₹3.12 Cr → ₹5.65 Cr (+81%) (Note 3(b) consolidated, p.184-185). 🟡 Watch/nuance — this materially
  qualifies Pass 1's Finding #3 (inventory build-up / "hardware demand softness"): **falling "Sale
  of Hardware" revenue (-18.4%) is occurring at the same time as a rapidly growing IoT-devices-
  *on-rent* asset base**, consistent with a genuine business-model shift from outright hardware sale
  to a device-as-a-service/rental model (which would also help explain the +30.8% growth in "Map
  data & services," which includes MaaS). This is a plausible alternative (or additional) explanation
  to pure demand weakness and belongs in the questions-for-management list, not just the earlier
  "inventory build-up = weak hardware demand" framing.
- **Investment property (the Jasola/DLF Tower A property later sold post year-end) ran at a small
  loss before indirect expenses in FY25** — rent/reimbursement collected fell ₹0.38 Cr → ₹0.07 Cr
  while direct operating expenses rose ₹0.04 Cr → ₹0.14 Cr, flipping a ₹0.20 Cr FY24 profit into a
  ₹(0.07) Cr FY25 loss before depreciation (Note 3(c), standalone p.129-130). 🟢 Minor/neutral —
  consistent with the property standing vacant ahead of its post-year-end sale (already known from
  Pass 1 Section 12); explains the disposal decision.

---

## 2. RELATED PARTY TRANSACTIONS — NEW: two related parties missing from Pass 1's table, one with
   an identified promoter-group/director link, both growing 4-18x

- **Two "Entities having common director" — ClarityX Analytics Pvt Ltd and Zenithra Tech Pvt Ltd —
  are entirely absent from Pass 1's RPT table**, despite being formally listed as a related-party
  category in Note 31A standalone (p.147) / Note 30a consolidated (p.203) and carrying material,
  fast-growing transaction values:

  | Party | Nature | FY25 (₹Cr) | FY24 (₹Cr) | YoY % |
  |---|---|---|---|---|
  | ClarityX Analytics Pvt Ltd | Technical & Business Support Services | 2.40 | 0.45 | **+433%** |
  | ClarityX Analytics Pvt Ltd | Sub-let charges | 0.01 | 0.00 | new |
  | Zenithra Tech Pvt Ltd | Purchase of Goods | 1.14 | 0.06 | **+1,800%** |
  | Zenithra Tech Pvt Ltd | Technical & Business Support Services | 2.57 | 0.32 | **+703%** |
  | Zenithra Tech Pvt Ltd | Sub-let charges | 0.01 | 0.00 | new |

  (Note 31B standalone p.148-149; identical figures in Note 30b consolidated p.203-204.) Combined:
  ₹6.13 Cr (FY25) vs ₹0.83 Cr (FY24), **+638%**. Outstanding balance: Zenithra Trade Payable ₹0.26
  Cr, new this year, nil PY (Note 31C standalone p.149).
- **Identity of the common director, cross-referenced from a different section of the document**
  (Regulation 36(3)/AGM-notice director disclosures, not the Notes themselves, but directly
  clarifying a Note 31 entry): **Ms. Rakhi Prasad — who is simultaneously a Non-Executive Director
  of MapmyIndia and a member of its Promoter & Promoter Group (both listed in Note 31A) — holds an
  "Other Directorship" in ClarityX Analytics Private Limited** (director bio table, printed p.226;
  DIN 07621845 matches her Note 31A entry). Zenithra's common director is not separately named
  anywhere in the document — **NOT FOUND IN DOCUMENT**. 🔴 Red Flag — this is a governance-relevant
  fact Pass 1 missed entirely: a promoter-group-affiliated director sits on the board of one of the
  two counterparties receiving a combined ₹6.13 Cr in FY25 (vs ₹0.83 Cr FY24), with no
  arm's-length benchmarking disclosed beyond the standard boilerplate assertion.
- **Corporate-governance-report cross-reference (Regulation 23 material-RPT disclosure, printed
  p.57-58) shows the Board pre-approved ClarityX and Zenithra "Business Agreements" for Technical &
  Business Support Services up to ₹12 Crore *each*, and Zenithra's Purchase-of-Goods agreement also
  up to ₹12 Crore, both approved 13-May-2024.** Actual FY25 utilisation (₹2.40-2.57 Cr per line) is
  roughly 20% of each ceiling — meaning there is large disclosed headroom for these two
  common-director entities to become materially larger counterparties next year without a fresh
  shareholder approval event. 🔴 Red Flag — combine with the +433-1,800% YoY growth above; this
  belongs at the top of the questions-for-management list.
- **A related party appears in the consolidated transactions table with no category assigned and no
  standalone-level mirror:** "Chirag Associates Private Limited — Sale of service — ₹0.15 Cr (FY24
  only, nil FY25)" (Note 30b consolidated, p.204) is not listed in the "related parties with whom
  transactions have taken place" category table above it, nor does it appear anywhere in the
  standalone RPT note. 🟡 Watch (minor) — a small disclosure-consistency gap, likely a Gtropy-level
  relationship not properly categorised, but not independently explained in the notes.
- **Additional RPT lines not extracted in Pass 1** (Note 31B standalone p.148-149 / Note 30b
  consolidated p.203-204): Mappls DT "Technical expenses" fell from ₹2.57 Cr to **nil**; Mappls DT
  "Map data service" rose ₹0.27 Cr → ₹0.86 Cr (+218.5%); Indrones Solutions "Technical expenses"
  fell ₹0.67 Cr → ₹0.06 Cr (-91%); Gtropy "Sale of service" ₹5.33 Cr vs ₹5.28 Cr (flat); Gtropy
  "Sub let charges" ₹0.48 Cr flat both years. None individually large, but they were not in Pass 1's
  table at all and round out the RPT picture.
- **Payments to promoter-group individuals under "Professional charges" — a category Pass 1 did not
  extract:** Rakhi Prasad ₹0.27 Cr (FY25) vs ₹0.34 Cr (FY24), -20.6%; Vineet Jaipuriar (relative of
  director & promoter, per Reg. 36(3) disclosure p.57) ₹0.11 Cr flat both years (Note 31B standalone
  p.149). 🟡 Watch (minor) — small amounts, but Rakhi Prasad now draws **three separate RPT income
  streams** in the same year: Non-Executive Director sitting fees + commission, *and* promoter-group
  "Professional charges," *and* (via ClarityX) an indirect commercial relationship as described
  above. The layering itself is a disclosure-clarity point worth a management question, independent
  of arm's-length adequacy.

---

## 4. TRADE RECEIVABLES / ECL — NEW: the deterioration Pass 1 flagged (Red Flag #2) is concentrated
   almost entirely at subsidiary level, not the parent

This is a material refinement of Pass 1's #1-ranked-by-magnitude Red Flag, not a contradiction of it.

- **Standalone-only ECL and bad-debt provisioning data (Note 8 standalone p.133-134; Note 30
  "Financial risk management" standalone p.146; Note 24 standalone p.141):**
  - Standalone gross trade receivables ₹105.33 Cr (FY25) vs ₹96.28 Cr (FY24); standalone ECL
    allowance ₹2.58 Cr vs ₹2.05 Cr, **+25.9%** — a fraction of the consolidated +117% Pass 1 flagged.
  - Standalone "Provision for doubtful debts" P&L charge (Note 24) **fell** ₹1.32 Cr → ₹0.86 Cr
    (**-34.8%**) even as revenue grew. This is the opposite direction of the consolidated figure.
  - Standalone >6-months-overdue as % of gross receivables: 3.8% (FY24) → 5.4% (FY25), a real but
    modest deterioration — smaller in absolute ageing terms than the ECL-charge math implies, and
    much smaller than the consolidated ECL-balance swing.
- **Arithmetic implication (derived, not stated in the document):** subtracting standalone from
  consolidated figures, the *subsidiary-level* (effectively Gtropy) ECL P&L addition rose from
  roughly ₹0.56 Cr (FY24: ₹1.88 Cr consol − ₹1.32 Cr standalone) to roughly ₹3.28 Cr (FY25: ₹4.14 Cr
  consol − ₹0.86 Cr standalone) — an implied **+486%** increase, entirely offsetting a genuine
  **decline** in the parent's own receivables-quality metric. 🔴 Red Flag, refined — the credit-risk
  deterioration Pass 1 flagged is real at the Group level but should be labelled a **Gtropy/hardware-
  subsidiary phenomenon**, not a core-business (map data/SaaS) receivables problem. This materially
  changes how an investor should weight the flag against the core thesis.
- **Separately, both books show actual cash write-offs of receivables *declining* even as the
  forward-looking ECL provision balance rises:** standalone "Bad debts written off" ₹0.76 Cr → ₹0.33
  Cr; consolidated ₹1.77 Cr → ₹0.99 Cr (Note 24 standalone p.141, Note 23 consolidated p.196-197).
  🟡 Watch/nuance — the deterioration Pass 1 flagged is in the *estimated* provision, not yet in
  realised losses; could reflect either prudent forward-looking provisioning or a genuine ageing
  build-up not yet crystallised. Worth a management question on what is driving the Gtropy-specific
  provision build (customer names, sector concentration, ageing detail below the aggregate bucket).
- **Level 3 (unobservable-input) fair-value assets grew faster at the standalone level than the
  consolidated figure Pass 1 cited:** standalone Level 3 investments ₹10.32 Cr (FY24) → ₹23.64 Cr
  (FY25), **+129%** (Note 30 standalone, p.144-146) vs the consolidated +54.7% (₹17.22 Cr → ₹26.64
  Cr) Pass 1 reported. 🟡 Watch — reinforces Pass 1's earnings-quality concern on the FVTPL book,
  with a sharper standalone-level growth rate than the consolidated number alone would suggest.
- **No Level 3 valuation-technique or unobservable-input sensitivity disclosure exists anywhere in
  the Financial Instruments note (Note 30 standalone p.144-146, Note 29 consolidated p.199-201)** —
  only the fair-value hierarchy classification is given, with no DCF/comparable-multiple methodology
  or sensitivity table for the ₹26.64 Cr (consolidated) Level 3 book. **NOT FOUND IN DOCUMENT.**
  🟡 Watch — a genuine disclosure gap distinct from (and additional to) the concentration-risk point
  Pass 1 already made; an investor cannot assess how the ₹27.02 Cr "Gain on investments (net)"
  (Note 20 consolidated) was actually derived.

---

## 10. DEFERRED TAX — NEW: mechanical detail behind the ₹5.17 Cr prior-period catch-up, plus a
    standalone-vs-consolidated rate gap

- **Deferred tax component roll-forward shows exactly which line absorbed the ₹5.17 Cr prior-period
  correction Pass 1 flagged as Red Flag #1** (Note 27 standalone p.143-144; Note 26 consolidated
  p.197-198): DTA "Unrealized gain on fair valuation of investments" fell from ₹3.67 Cr (opening) to
  ₹0.36 Cr (closing), a ₹3.31 Cr P&L reversal, while a new DTL "Unrealized loss on fair valuation of
  investments" grew from ₹0.55 Cr to ₹5.27-5.28 Cr, a ₹4.73 Cr P&L charge — net effect consistent
  with (and explaining the mechanics of) the ₹5.17 Cr catch-up figure already flagged. 🟡 Watch,
  supporting detail only — useful for anyone verifying the Red Flag #1 number, not a new flag itself.
- **Standalone effective tax rate is 27.31% (FY25) vs 22.40% (FY24)** against the same 25.17%
  statutory rate (Note 27 standalone p.143) — Pass 1 only reported the consolidated figures (28.24%
  vs 23.27%). The standalone "Others" reconciliation line swung ₹3.88 Cr charge (FY25) vs ₹(5.28) Cr
  credit (FY24), an even larger undecomposed swing than the consolidated one Pass 1 flagged. 🟡 Watch
  — same underlying issue as Red Flag #1, now confirmed present (and slightly larger in ₹ terms) at
  standalone level too.
- **Subsidiary-level DTA lines, not previously extracted:** "Gtropy's figures" DTA rose ₹1.27 Cr →
  ₹2.67 Cr (+110%); "Others-Vidteq" (Mappls DT) DTA fell ₹1.44 Cr → ₹0.29 Cr (-80%) (Note 26
  consolidated, p.197). 🟢 Minor — low materiality, included for completeness.
- **Basic/diluted EPS is genuinely different between the two books, quantifying the "consolidation
  is dilutive" finding Pass 1 already made qualitatively (Finding #6):** standalone Basic EPS ₹27.56
  vs Diluted ₹27.28 (FY25); consolidated Basic ₹27.05 vs Diluted ₹26.77 (Note 29 standalone p.143,
  Note 28 consolidated p.199). **Consolidation costs the investor ₹0.51/share on both a basic and
  diluted basis (~1.9% of standalone EPS)** — a concrete, quantified version of Pass 1's
  consolidation-contribution-table finding. 🟡 Watch, sharpened.

---

## 11. REVENUE DETAILS — NEW: standalone POC exposure is higher than the consolidated figure cited

- **Standalone fixed-price/POC revenue is 62.6% of standalone revenue in FY25 (₹240.31 Cr of
  ₹383.87 Cr) vs 50.6% in FY24 (₹159.57 Cr of ₹315.61 Cr)** (Note 18 standalone, p.139) — a bigger
  jump, and a higher absolute share, than the consolidated 56.1%/41.8% figures Pass 1 cited. 🟡 Watch
  — the estimation-heavy revenue-recognition method the auditor flagged as its sole Key Audit Matter
  is actually *more* concentrated in the parent entity than the consolidated blend suggests.
- Standalone contract assets (unbilled revenue) ₹20.24 Cr (FY25) vs ₹10.61 Cr (FY24), **+90.8%**
  (Note 18 standalone p.139-140) — same direction, slightly different magnitude, as the consolidated
  +115% Pass 1 reported; both books confirm the trend independently.

---

## 12. OTHER CRITICAL NOTES — NEW items

- **Promoter/Co-Founder & Managing Director Rakesh Kumar Verma's equity shareholding fell by
  5,00,000 shares during FY25** (2,31,63,080 → 2,26,63,080 shares; 42.84% → 41.64%), while
  co-founder Rashmi Verma's absolute share count was **unchanged** (51,53,589 both years) — meaning
  the reduction is a genuine share-count decrease, not merely ESOP-driven percentage dilution.
  Total promoter & promoter-group holding fell from 52.37% to 51.11% (-1.26pp) (Note 12 standalone,
  "Promoter Shareholding" sub-table, p.135-137). **No explanation of the nature of this reduction
  (open-market sale, inter-se transfer, gift, or otherwise) is given anywhere in the notes, and no
  share-pledge disclosure exists anywhere in the document — NOT FOUND IN DOCUMENT.** 🔴 Red Flag —
  a material, unexplained promoter/MD share-count reduction is exactly the kind of fact Pass 1's
  note-by-note pass should have caught in the Equity Share Capital note; it belongs on the
  questions-for-management list and in the FLAG register.
- **Standalone Financial Ratios note (Note 43, p.156-157) triggered FIVE separate >25%-variance
  explanations that Pass 1 did not extract** (Pass 1 only discussed the consolidated note's single
  triggered explanation, Inventory Turnover):

  | Ratio | FY25 | FY24 | Variance | Company's explanation |
  |---|---|---|---|---|
  | Current ratio | 6.96x | 4.85x | +44% | "increase in short term investment and Fixed Deposit" |
  | Trade Payables turnover | 10.14x | 6.55x | +55% | "increase in expenses as compared to trade payable" |
  | Inventory turnover | 145.64x | 44.67x | +226% | "purchases mainly from subsidiary...doesn't hold more physical inventory" |
  | Debt-Equity ratio | 0.28% | 1.12% | -75% | "lease liability has decreased" |
  | Debt service coverage | 302.45x | 135.33x | +123% | "EBIT has increased" |

  🟡 Watch — the explanations are directionally reasonable but thin (same "circular" quality Pass 1
  already flagged for the consolidated note); more importantly, **standalone Debt-Equity of just
  0.28% vs consolidated 3.77%** is a clean, quantified confirmation that essentially all Group
  leverage sits at Gtropy (ties directly to Section 7/Borrowings in Pass 1).
- **Net profit ratio and Return on Equity both declined at both standalone and consolidated levels,
  a genuine "quality of growth" signal Pass 1 did not surface at all** (below the 25% disclosure
  trigger, so the company itself offers no explanation, but the pattern is consistent and real):
  Standalone Net Profit Ratio 38.60% → 34.44% (-11%); Consolidated 32.18% → 28.62% (-11%).
  Standalone ROE 23.08% → 20.75% (-10%); Consolidated 22.36% → 20.34% (-9%). Standalone/consolidated
  Return on Capital Employed (ex-cash) both -10%. (Note 43 standalone p.156, consolidated p.213.)
  🟡 Watch — profit is growing in absolute terms, but capital-efficiency ratios are compressing
  across the board as the balance sheet carries a growing bond/FD investment portfolio (₹290+ Cr
  standalone, Note 30 standalone p.146) rather than the whole capital base compounding within the
  operating business. Worth a direct question to management on capital-deployment intent for the
  investment book (buyback candidate vs. further venture-style deployment per Section 6 of Pass 1).
- **ESOP Black-Scholes assumptions, not extracted in Pass 1:** risk-free rate 7.27%-7.33%, dividend
  yield 0.13%, volatility 38.74% (Note 33 standalone p.151-152 / Note 32 consolidated). Options were
  exercised twice during the year at market prices of ₹2,182 and ₹1,641 against the legacy exercise
  price of ₹12.15 — implying very large embedded value per option (~₹1,629-₹2,170), i.e. the tiny
  remaining ESOP pool (~1% of shares, per Pass 1) is deeply in the money. 🟢 Low materiality, included
  for completeness only.
- **CSR activity concentration narrowed this year:** FY25 CSR spend (₹2.77 Cr) went entirely to a
  single activity, "Road Safety Awareness Programs," versus three distinct activities in FY24 (Har
  Ghar Tiranga campaign, Road Safety, Education & research) (Note 39/40 consolidated, p.211-212).
  🟢 Minor observation, immaterial financially.
- **Maturity-of-financial-liabilities table (Note 30 standalone p.146) shows standalone total
  contractual financial liabilities nearly halved: ₹37.35 Cr (FY24) → ₹19.16 Cr (FY25)**, driven by
  the trade-payables and lease-liability declines Pass 1 already noted elsewhere. 🟢 Clean/positive —
  a concrete, quantified confirmation of a shrinking near-term liability profile at the parent level.
- **Note 51 "Other Statutory Information" (standalone, p.159) — a full block of MCA-mandated
  negative-assurance disclosures Pass 1 did not mention at all:** no Benami property, no undisclosed
  income, no crypto-currency trading, no struck-off-company transactions, no layering-of-companies
  breach, no scheme of arrangement, no charge-registration lapses, funds not routed through
  intermediary "ultimate beneficiary" structures (both given and taken), audit-trail feature
  confirmed enabled and untampered (Note 50). 🟢 Clean — reviewed in full; no new items, included for
  completeness of the note-by-note pass.

---

## PASS 2 NEW FINDINGS SUMMARY

Highest-priority new/refining findings from this pass, in order of investor importance:

1. **🔴 Two related parties (ClarityX Analytics, Zenithra Tech — "entities having common director")
   missing entirely from Pass 1's RPT table; combined transactions grew +638% YoY (₹0.83 Cr → ₹6.13
   Cr); one is traceable to Non-Executive Director/Promoter-group member Rakhi Prasad; Board-approved
   ceilings of ₹12 Cr each leave large room for further growth** (Note 31A/B standalone p.147-149,
   Note 30a/b consolidated p.203-204; director-bio cross-reference p.226).
2. **🔴 Promoter/MD Rakesh Kumar Verma's shareholding fell by 5,00,000 shares (-1.2pp) during FY25,
   unexplained in the notes, no pledge disclosure found** (Note 12 standalone p.135-137).
3. **🔴/🟡 Refinement of Pass 1 Red Flag #2: receivables/ECL deterioration is concentrated almost
   entirely at subsidiary (Gtropy) level — standalone ECL provisioning actually *declined* -34.8%
   while consolidated rose +120%; implied subsidiary-level addition rose ~+486%** (Note 8/24/30
   standalone p.133-134, 141, 144-146; Note 8/23/29 consolidated as in Pass 1).
4. **🟡 IoT-devices-on-rent write-off (₹5.70 Cr gross, new "Loss on scrapping-out" P&L line ₹0.89 Cr
   standalone) sits alongside a rapidly *expanding* Gtropy IoT-rental fleet (+57.7% net carrying
   value) — nuances the "hardware demand weakness" framing toward a possible business-model shift to
   device-as-a-service** (Note 3(b) standalone p.129, consolidated p.184; Note 24/23 Other Expenses).
5. **🟡 Standalone Financial Ratios note triggered five >25%-variance explanations Pass 1 did not
   extract, and net-profit-ratio/ROE/ROCE all declined at both standalone and consolidated levels
   (sub-threshold, unexplained by the company) — a genuine capital-efficiency compression signal
   Pass 1 missed entirely** (Note 43 standalone p.156-157, consolidated p.213-214).
6. **🟡 Deferred-tax mechanics behind the already-flagged ₹5.17 Cr prior-period catch-up now traced
   to specific DTA/DTL line movements; standalone effective tax rate (27.31% vs 22.40%) and "Others"
   swing also confirmed, not just the consolidated figures Pass 1 cited** (Note 27 standalone
   p.143-144, Note 26 consolidated p.197-198).
7. **🟡 No Level 3 fair-value valuation-technique/sensitivity disclosure found anywhere in the
   Financial Instruments notes, despite a ₹26.64 Cr Level 3 book and ₹27.02 Cr "Gain on investments"
   — a disclosure gap distinct from the concentration-risk point already made** (Note 30 standalone
   p.144-146, Note 29 consolidated p.199-201).
8. **🟡 Standalone POC/fixed-price revenue share (62.6%) is higher than the consolidated figure Pass
   1 cited (56.1%)** — the estimation-heavy revenue base is more concentrated in the parent than the
   consolidated blend implies (Note 18 standalone p.139).
9. Minor/low-materiality items for completeness: unlisted "Chirag Associates" RPT line (Note 30b
   consolidated p.204); quantified EPS cost of consolidation (₹0.51/share); ESOP Black-Scholes
   assumptions; CSR activity-count narrowing; halved standalone financial-liability maturity profile;
   Note 51 "Other Statutory Information" block reviewed clean.

```yaml
stage: B02-notes-pass2
company: "MAPMYINDIA"
run_date: "2026-07-13"
model: claude-sonnet-5
status: complete
pass_2_empty: false
new_findings_count: 9
highest_new_severity: red_flag
```
