# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Company: Awfis Space Solutions Limited (AWFIS) | Run: awfis-2026-09-19
Source: same as Pass 1 — runs/awfis-2026-09-19/inputs/annual-report/AR-FY26-with-AGM-notice.txt
(page-marked text of AR-FY26-with-AGM-notice.pdf). Figures in ₹ millions as filed unless noted.
Rated 🟢 Clean | 🟡 Watch | 🔴 Red Flag.

## METHOD
Two things done in this pass, per the task brief:
1. RE-VERIFIED five named Pass 1 findings against the exact AR pages cited, line by line: the Note
   33 vs CARO disputed-dues gap, the GST SCN absence, the Note 38 lease cash outflow, the Note 40
   Design & Build transfer, and the lessor-side finance-lease reclassification.
2. RE-READ the Notes end to end a second time hunting specifically for what Pass 1 skipped or only
   partially covered: sub-notes/footnotes, cross-references between notes, unflagged YoY changes,
   qualitative management-judgement language, and every note containing "significant," "material,"
   "unusual," "exceptional," "one-time," "first time," "changed," "revised," or "restated."

Only new findings are reported below (Pass 1 items are not repeated except where re-verification
changed their status).

═══════════════════════════════════════════════════════════════
## PART A — RE-VERIFICATION OF FIVE NAMED PASS 1 FINDINGS
═══════════════════════════════════════════════════════════════

1. **Note 33 vs CARO disputed-dues gap: CONFIRMED, exact.** Re-read Note 33(i) standalone (PDF
   p.112, source lines 16419-16427) word for word — zero quantified amounts, exactly as Pass 1
   quoted. Re-read the CARO Annexure clause (vii)(b) table (PDF p.86, source lines 12596-12651) —
   the six-line table (Rs216.95mn + Rs757.93mn + Rs108.50mn + Rs2.99mn + Rs8.88mn + Rs6.25mn =
   Rs1,101.50mn) matches Pass 1's transcription exactly, forum names included. 🔴 Confirmed as
   reported.
2. **GST SCN absence from the Notes: CONFIRMED**, and see Part B item 5 below for a distinct,
   additional compliance-timing finding on the SECOND notice that Pass 1 did not surface (a SEBI
   LODR disclosure delay with a formal "reason for delay" filing).
3. **Note 38 lease cash outflow: CONFIRMED, exact.** Re-read the standalone lease-liability
   roll-forward and cash-flow table (PDF p.120, source lines 17441-17491) — principal Rs2,505.11mn
   + interest Rs1,616.53mn = Rs4,121.64mn FY26 vs Rs1,169.45mn + Rs1,292.76mn = Rs2,462.21mn FY25,
   +67.4%, matches Pass 1 exactly. The consolidated Note 38 (PDF p.~198, source lines 23704-23751)
   carries the identical figures for the Holding Company (no additional subsidiary lease liability
   layered in — Awliv and Awfis Transform do not carry their own material lease books).
4. **Note 40 Design & Build transfer: CONFIRMED, exact.** Re-read PDF p.122-123 (source lines
   17723-17789) — BTA date 23-Dec-2025, consideration Rs265.91mn, timeline extension to
   31-Dec-2026 approved 26-Feb-2026, disposal-group PBT Rs158.86mn FY26 (Rs233.40mn FY25, -31.9%),
   matches Pass 1 exactly.
5. **Finance-lease reclassification (9 → 30 leases): CONFIRMED, exact.** Re-read PDF p.121 (source
   lines 17504-17548) — net investment in finance lease Rs3,583.51mn (Rs2,035.33mn FY25, +76.1%),
   footnote explicitly attributes the change to "increase in the number of leases to 30 as at 31
   March 2026 as compared to 9 leases as on 31 March 2025," matches Pass 1 exactly. Cross-checked
   against Note 9 (Other financial assets, PDF p.101, source line 15141): finance lease receivable
   split non-current Rs1,721.15mn + current Rs1,862.35mn = Rs3,583.50mn — reconciles to the rounding
   digit with Note 38's Rs3,583.51mn. 🟢 Internally consistent across two notes.

**Bonus resolution while re-verifying item 3:** Pass 1 flagged an unexplained "third figure"
(Rs817.21mn and Rs303.71mn) sitting beside the FY26/FY25 columns in the standalone Note 38 P&L
table for "Variable lease payments" and "Expenses relating to leases of low-value assets and
short-term leases" (PDF p.120, source lines 17471-17477), and called it a probable
PDF-extraction/table-merge artifact rather than a genuine third disclosed figure. This pass
cross-checked the **consolidated** Note 38 table for the same two line items (PDF p.~198, source
lines 23737-23740): **822.20 / 779.70** and **328.28 / 337.30** — clean two-column figures, no
third number, and these are exactly the middle/last values from the standalone table (the ones
that reconcile arithmetically to the stated Total row). This **confirms** Pass 1's hypothesis with
high confidence: Rs817.21mn and Rs303.71mn are a text-extraction artifact of this corpus copy, not
numbers the Company actually filed. Downgraded from "flagged, unresolved" to "confirmed
non-issue," but named here because a downstream reader who saw only the standalone table could
still be misled by it.

═══════════════════════════════════════════════════════════════
## PART B — NEW FINDINGS (NOT IN PASS 1)
═══════════════════════════════════════════════════════════════

### B1. 🟡 Auditor-named exception on the statutory audit-trail (edit-log) requirement
**Note 45, standalone PDF p.124-125 (source lines 17992-18009); Independent Auditor's Report,
Rule 11(g) paragraph, PDF p.85-86 (source lines 12417-12451); identical language in the
consolidated Note (PDF p.~205, source lines 24082-24093).**

Note 45 itself reads as routine ("audit trail was enabled and operated throughout the year"), but
the Auditor's Report — a document Pass 1 read for the Key Audit Matter and CARO table but not for
this specific paragraph — names a genuine exception: for the Company's core accounting software
(maintained by a third-party service provider), the auditor states verbatim, **"we are unable to
comment on whether audit trail feature with respect to the database of the said software was
enabled and operated throughout the year,"** because the Type 2 SOC assurance report obtained on
that software did not address database-level edit logs. This is distinct from the invoicing
software, where the audit trail WAS confirmed at both application and database level. This is not
a qualified opinion and not a red flag on its own — third-party SaaS accounting platforms commonly
carry this exact limitation industry-wide — but it is a genuine, auditor-acknowledged scope gap on
a mandatory Companies Act control (the audit trail rule exists specifically to make undetected
books-of-account tampering harder to hide), and Pass 1 did not surface it at all.

### B2. 🟡 EPS / dilution (a required priority-topic item Pass 1 skipped entirely)
**Note 31 "Earnings per share," standalone PDF p.110-111 (source lines 16208-16237).**

Pass 1's extraction template explicitly asks for "basic vs diluted EPS gap and dilution sources"
(priority item 12) but Pass 1's report contains no EPS section at all. Re-read in full:

| | FY26 | FY25 | YoY |
|---|---|---|---|
| PAT, continuing + discontinued | Rs667.87mn | Rs655.61mn | +1.9% |
| Basic EPS, continuing + discontinued | Rs9.36 | Rs9.42 | -0.6% |
| Diluted EPS, continuing + discontinued | Rs9.34 | Rs9.34 | **flat, 0.0%** |
| PAT, continuing operations only | Rs509.01mn | Rs422.21mn | **+20.5%** |
| Basic EPS, continuing operations only | Rs7.13 | Rs6.07 | +17.5% |
| Weighted avg shares, basic / diluted | 71,366,771 / 71,449,035 | 69,587,749 / 70,200,438 | — |

Total diluted EPS is **flat year on year** despite standalone continuing-ops revenue growth of
+32.9% (Pass 1 Section 11). The reason: FY25 PAT was inflated by the one-off Rs251.02mn AWFIS Care
exceptional gain (Note 30, Pass 1 Section 12f) that did not recur in FY26, and FY26
discontinued-operations (Design & Build) profit fell 31.9% (Note 40, Pass 1 Section 12b). Strip
both effects out and continuing-operations PAT actually grew 20.5%. **This is an optics point, not
a deterioration** — a reader looking only at the headline PAT/EPS line would see zero growth and
miss real underlying improvement. The basic-vs-diluted gap itself is small (weighted-average
shares differ by ~82,000, ~0.1%), so ESOP dilution (Pass 1 Section 12c: 141.3% ESOP charge growth)
is not yet materially diluting per-share metrics — the flat headline is entirely a base-effect of
the lapsed one-off gain.

### B3. 🟡 Top-10 customer receivable concentration jumped sharply
**Note 36(b)(II), standalone PDF p.116 (source line 16921-16922).**

"As at 31 March 2026, the top 10 accounts receivables accounted for **61.66%** (31 March 2025:
**42.74%**) of all the receivables outstanding." Pass 1's Section 4 (Trade Receivables) reported
"no single customer >10%" from the segment note but did not carry this top-10 concentration
statistic from Note 36, which is materially different information: concentration among the top 10
accounts has risen by roughly 19 percentage points in one year. Part of this is arithmetic
(concentration ratios naturally rise on a shrunken post-carve-out base — gross receivables fell
from Rs1,277.20mn to Rs510.99mn per Pass 1 Section 4), but a jump of this size is still worth
naming directly against Pass 1's "broadly stable to modestly improving" receivables read — the
ageing mix improved while the concentration mix worsened, and both are true at once.

### B4. 🟡 The numeric ECL loss-rate matrix EXISTS — correcting a Pass 1 "NOT FOUND"
**Note 36(b)(II) ageing/ECL-rate table, standalone PDF p.116 (source lines 16923-16985).**

Pass 1's input_gaps explicitly stated "No numeric ECL loss-rate-by-ageing-bucket matrix disclosed
(Note 8 ageing table gives balances only, not the applied provision rate per bucket)." This is
**incorrect as stated** — the rate-by-bucket matrix exists, just in **Note 36** (the financial
instruments / credit-risk note), not Note 8 (the trade-receivables note where Pass 1 looked for
it):

| Bucket | FY26 ECL rate | FY25 ECL rate |
|---|---|---|
| Unbilled / current not due | 17.32% | 0.00% |
| 0-90 days | 1.19% | 0.95% |
| 90-180 days | 0.00% | 10.77% |
| 180-360 days | 37.09% | 5.40% |
| 1-2 years | 23.56% | 3.60% |
| 2-3 years | 100.00% | 54.13% |
| >3 years | 100.00% | 100.00% |

Two things worth naming beyond the correction itself: (a) the unbilled/"current not due" bucket —
normally the lowest-risk bucket — carries a new 17.32% ECL rate in FY26 versus 0.00% in FY25, a
genuine change in loss expectation on what should be the safest receivables; (b) the pattern is
non-monotonic and swings hard year to year (90-180 days falls from 10.77% to 0.00% while 180-360
days rises from 5.40% to 37.09%), which reads more like case-by-case specific provisioning dressed
in a bucket table than a stable statistical loss-rate model. Worth a direct management question on
ECL methodology consistency.

### B5. 🟡 Second GST Show Cause Notice: a distinct SEBI LODR disclosure-delay finding
**Cross-checked against the three announcement filings in the corpus** (not in the AR Notes; Pass
1 already flagged the notices' absence from Note 33 and the events notes — this is additional,
separate information about the disclosure of the second notice itself, not about the AR).

- First SCN: received 20-May-2026, **disclosed to exchanges 21-May-2026** — one-day turnaround,
  clean.
- Second SCN: dated 23-May-2026, **received by the Company 25-May-2026** (per the 02-Jun and
  04-Jun filings), but **not disclosed to exchanges until 02-Jun-2026** — an 8-day gap. The Company
  then filed a **third announcement on 04-Jun-2026 specifically to state the "reason for delay"**
  under SEBI LODR Schedule III, citing the time needed to review the notice and identify "a
  material calculation error in the demand amount" before disclosing.

This is a genuine, separate compliance-timing point from Pass 1's "absent from the Notes" flag:
the second notice was received the same day the FY26 accounts were board-approved (25-May-2026)
AND its market disclosure itself ran late enough to require a formal delay explanation. Neither
the delay nor the reason-for-delay filing is mentioned anywhere in the AR Notes (consistent with
Pass 1's broader finding that neither SCN appears in the statutory financial-statement notes at
all).

### B6. 🟡 Large, unexplained cost-line growth inside Note 29 (Other expenses)
**Standalone PDF p.109-110 (source lines 16158-16185); identical figures in the consolidated Other
expenses note.**

Re-reading Note 29 line by line (as the pass-2 rules direct — "large movements you did not comment
on") surfaced several YoY moves Pass 1 did not carry, the largest by far being:

- **Infra and allied service expenses: Rs483.26mn FY26 vs Rs110.48mn FY25, +337.4%** — nearly
  quadrupled, with **no narrative explanation anywhere in the Notes** for what drove it (searched
  the full document; the phrase appears only in the two Other Expenses tables, standalone and
  consolidated, with no accompanying footnote).
- Security and housekeeping charges: Rs879.38mn vs Rs464.01mn, **+89.5%** (nearly doubled).
- Common area maintenance: Rs874.47mn vs Rs574.95mn, +52.1%.
- Repair and maintenance: Rs191.53mn vs Rs120.67mn, +58.7%.
- Advertisement and sales promotion: Rs55.40mn vs Rs33.55mn, +65.1%.

**Total Other expenses grew Rs3,994.57mn → Rs5,624.13mn, +40.8% YoY** — faster than standalone
continuing-ops revenue growth of +32.9% (Pass 1 Section 11) and faster even than the already-
flagged +67.4% lease cash-outflow growth's revenue comparator. This is a second, independent
margin-quality data point beyond the lease-cost story Pass 1 already centred: opex outside of
leases is also growing ahead of revenue, and the single largest driver (Infra and allied service
expenses) is disclosed with a number but zero explanation.

### B7. 🟡 New/enlarged doubtful-debt provisions in Note 29 that do not obviously reconcile to Note 36
**Standalone PDF p.109-110 (source lines 16181-16182), cross-checked against Note 36's ECL
roll-forward (PDF p.117, source lines 17027-17040).**

Within the same Note 29 Other Expenses table:
- **Provision for doubtful debts: Rs27.05mn FY26 (Nil FY25) — a first-time occurrence.**
- **Provision for doubtful advances and deposits: Rs41.42mn FY26 (Rs0.63mn FY25) — up ~66x.**

Combined, these are **Rs68.47mn of new P&L bad-debt-type charges in FY26 versus Rs0.63mn in FY25**.
This does not cleanly map to the Note 36 trade-receivables ECL roll-forward, which separately shows
"Provision made/(provisions written back), net" of **Rs57.44mn** for trade receivables and
**Rs12.62mn** for security deposits in FY26 (Pass 1 Section 4 cited the former). The two sets of
numbers (Rs27.05mn "doubtful debts" in Note 29 vs Rs57.44mn "provision made" in Note 36 for the
same trade-receivables pool) are not the same figure, and the Notes do not bridge them explicitly.
This may simply reflect different presentation conventions (net of write-backs, or a split between
"specific" doubtful-debt provisions and the Ind AS 109 ECL model), but it is not resolvable from
the Notes alone and is worth a direct management question: what exactly does the Rs27.05mn Note 29
line represent relative to the Rs57.44mn Note 36 ECL movement, and does the Rs41.42mn "doubtful
advances and deposits" line double-count any of the Rs12.62mn security-deposit ECL provision also
shown in Note 36?

### B8. 🟡 OCR/text-extraction digit-drop in the Consolidated Segment Information note (Note 31)
**Consolidated PDF p.152 (source lines 22371, 22505), cross-checked against the note's own later
reconciliation table (PDF p.153, source line 22552).**

Two totals in the segment table's FY25 comparative column are garbled in this corpus copy:
- "Total Income" FY25 reads **Rs2,075.35mn**, but the four segment columns for FY25 sum to
  Rs9,160.38 + Rs2,782.58 + Rs132.39 + Rs0 = **Rs12,075.35mn** — the extracted figure is missing a
  leading "1".
- "Total assets" FY25 reads **Rs5,069.84mn**, but the same note's own reconciliation table two
  pages later explicitly states "Total assets 29,101.89 / **25,069.85**" for FY26/FY25 — the
  extracted figure in the first table is missing a leading "2".

This is **not a company disclosure error** — it is a text-extraction defect specific to this
corpus copy, confirmed by the fact that the correct number appears elsewhere in the same note. It
is named here only so that no downstream stage building the FY27 valuation model off this corpus
accidentally cites Rs2,075.35mn or Rs5,069.84mn as real FY25 consolidated totals.

### B9. 🟢 Widening unallocated (corporate) segment loss
**Consolidated Note 31, PDF p.152 (source lines 22402, 22410, 22533).**

The "Unallocated" segment column (fixed deposits, tax balances, borrowings, corporate overhead)
shows profit/(loss) before tax of **Rs(323.74)mn FY26 vs Rs(232.47)mn FY25, +39.3% wider loss**.
Within it, unallocated employee benefit expense rose Rs237.89mn → Rs267.72mn (+12.5%), and
standalone "Payment to auditor" (statutory audit fee) rose Rs7.45mn → Rs8.95mn (+20.1%, all fee,
no non-audit services disclosed separately — Note 29(i), PDF p.109). A minor item on its own scale
but consistent with the broader Note 29 opex-growing-ahead-of-revenue pattern in B6.

### B10. 🟢 Growing TDS-recoverable balance — texture on the 0% effective tax rate finding
**Note 10, standalone PDF p.101 (source lines 15168-15174).**

Non-current tax assets (tax deducted at source recoverable) grew **Rs534.48mn → Rs926.71mn,
+73.4% YoY**. Read alongside Pass 1's Section 10 finding (0% effective tax rate both years), this
is a real cash-conversion texture point: as a zero-cash-tax company, AWFIS still has tax deducted
at source on rental income (a standard Indian statutory withholding), and the recoverable pool is
growing faster than revenue — capital effectively held by the tax authorities pending refund or
future set-off, not available for operating use in the interim.

### B11. 🟢 Minor gap-fill: New Labour Codes (a genuine "first time" item Pass 1's Section 1 missed)
**Note 44, standalone PDF p.124 (source lines 17985-17991).**

The Government of India's four consolidated Labour Codes became effective 21-Nov-2025. The Company
states the impact on its own employees "is not material" for FY26 and will evaluate further
guidance prospectively. Routine, immaterial, no action needed — named only because it is literally
a "first time"/"changed" item under the pass-2 keyword hunt list and Pass 1's accounting-policy
section (which specifically covers "first-time standard adoptions") did not mention it.

═══════════════════════════════════════════════════════════════
## UPDATED RECEIVABLES TREND (supersedes Pass 1's statement, does not contradict it)
═══════════════════════════════════════════════════════════════
Pass 1's read ("broadly stable to modestly improving on ageing mix, structurally distorted by the
Design & Build carve-out") stands, but must now be read together with two new facts from this
pass: (a) top-10 customer concentration rose from 42.74% to 61.66% (B3), and (b) the previously
zero-risk "unbilled/current not due" bucket now carries a 17.32% ECL rate versus 0.00% prior year
(B4). Net effect: the receivables book is smaller, its ageing mix looks better, but it is now more
concentrated in fewer customer relationships and carries a new loss expectation on a bucket that
carried none before. "Improving" is an incomplete read on its own; "smaller, more concentrated,
and with a new pocket of expected loss" is the fuller one.

═══════════════════════════════════════════════════════════════
## PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════
Eleven new findings (B1-B11) plus one confirmed resolution of a Pass 1 open question (the Note 38
"third figure" is a text-extraction artifact, not a real disclosure gap) and one correction to a
Pass 1 input_gap (the ECL rate-by-bucket matrix exists, in Note 36 not Note 8). Ranked by investor
importance: B2 (EPS flat-headline optics) and B1 (audit-trail exception) are the most consequential
because they touch, respectively, how a reader should read the headline growth number and the
statutory control environment; B3/B4 (receivables concentration and ECL-rate volatility) and B5
(GST SCN disclosure delay) are the next tier; B6/B7 (opex growth and doubtful-debt provisions) round
out the operating-quality picture; B8/B9/B10/B11 are minor or purely corpus-hygiene items.
