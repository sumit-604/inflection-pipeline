# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 3 OF 3 (PATTERN PASS + CONSOLIDATION)
Company: SHAREINDIA (Share India Securities Limited) | Run date: 2026-09-19
Source: inputs/annual-report/SHAREINDIA-AR-FY26.txt (FY26 AR, page markers cited)
Method: a third read of the same Notes (standalone 1-64, pp.140-221; consol
1-68, pp.251-335), this time hunting PATTERNS instead of reading sequentially:
contradictions between notes, numbers that do not tie to each other,
disclosure depth that varies without reason, unquantified prior-year
regrouping, subsequent events, and going-concern language. Cross-checked
against Pass 1 (outputs/reports/02-notes-pass1.md) and Pass 2
(outputs/reports/02-notes-pass2.md); only genuinely new pattern findings are
reported below, then the three passes are consolidated.
Units as printed: ` in Lakhs. Cr equivalents in parentheses (÷100), arithmetic
shown inline, never a silent conversion.

═══════════════════════════════════════════════════════════════════
PASS 3 — PATTERN FINDINGS
═══════════════════════════════════════════════════════════════════

## 1. 🟡 CONTRADICTION: Note 62 ("no significant events") sits beside a
   same-day Board decision disclosed only in the debt note (Note 17e
   standalone p.171; Note 18e consol p.271-272; Note 62 standalone p.221;
   Note 66 consol p.334)

Note 62 (standalone) and Note 66 (consol) both state, verbatim, "there
were no significant events after the end of the reporting period which
require any adjustment or disclosure." Both notes are dated to the same
Board approval: "the financial statements were approved for issue by the
Board of Directors on May 19, 2026" (accounting policy 2.1(b), p.140
standalone; p.238 consol). Note 17e/18e discloses, as a fact already known
to the Board by that same date, that the Board had itself resolved on
19-May-2026 to pursue EARLY REDEMPTION of the ₹9,990 lakh First-Issue NCD
after NCD holders/the Debenture Trustee would not approve the proposed
end-use change. A Board resolution to accelerate repayment of a listed
debt instrument, taken on the very date the accounts were approved, is
placed inside the borrowings note as background to the instrument's terms,
never surfaced as an "event" in Note 62/66. This is not a timing gap (both
notes share the 19-May-2026 date) — it is a placement and completeness
question: the company judged the same fact "explain in the debt note" but
not "significant" for the events-after-reporting-date note, even though it
is the origin of the NCD holders' meeting that was later adjourned
(Aug-Sep 2026, per company memory, outside this AR).

## 2. 🟢 Standalone total income ties out exactly across the revenue notes,
   no plug (Notes 27, 28, 29, 30, 31, 32, cross-checked against Note 48a,
   pp.176-177, 191-192, 194)

Interest income (Note 27) ` 21,826.59 lakhs + Dividend income (Note 28)
` 1,966.21 lakhs + Fees and commission (Note 29) ` 13,197.33 lakhs + Net
gain on fair value changes (Note 30) ` 72,005.77 lakhs + Sale of products
(Note 31) ` 13,731.45 lakhs + Other income (Note 32) ` 1,952.17 lakhs =
` 1,24,679.52 lakhs, which matches Note 48a's disclosed Total Income
(` 1,24,679.52 lakhs, p.194) to the rupee. No unexplained plug or residual
line exists between the individual revenue notes and the aggregate
disclosed elsewhere — a positive internal-consistency finding worth
naming explicitly, since Pass 1/2 cited these notes individually but never
tied them out against each other.

## 3. 🟡 DISCLOSURE-DEPTH CONTRAST: highly granular where routine, generic
   where a live compliance number would matter (Note 52 pp.194-207 vs
   Note 55 p.212; Note 64 p.221 / Note 68 consol p.331)

Note 52 (related party disclosures) names 14 subsidiaries, 17 KMPs, ~38
relatives, and ~65 controlled/influenced entities, with a full
transaction table down to individual round-trip loans. By contrast, Note
55 (Capital management) states only that the Company "is required to
maintain a minimum net worth as prescribed by SEBI (Stock brokers and
sub-brokers) Regulations, 1992" and asserts compliance, with NO quantum
disclosed (NOT FOUND, already flagged Pass 1). Note 64 (standalone) and
Note 68 (consol) — the prior-year regrouping note — likewise gives a
generic "does not affect overall financial position" statement with no
rupee amount for any reclassification, even though other notes in the
same document (e.g. Note 3's FD reclassification between cash and
bank-balance buckets) DO quantify similar reclassifications precisely.
The pattern: disclosure granularity is inconsistent across notes of
comparable Ind AS materiality, and the two thinnest notes (55, 64/68)
happen to be the ones that would let a reader test a live regulatory
minimum and a prior-year adjustment respectively.

## 4. 🟢 No restatement or prior-year adjustment found anywhere in the notes
   (document-wide check)

A full-document search for "restate"/"restated" returns zero matches
anywhere in the AR. The only prior-year adjustment language at all is the
generic, unquantified regrouping statement in Note 64/68 (see finding #3).
No note discloses a correction of a prior-period error under Ind AS 8, and
no note shows a comparative figure that differs from what was reported in
the FY25 AR's own comparatives as far as this pass could test internally.
This is a clean finding, stated for completeness rather than as a concern.

## 5. 🟢 Going-concern language is standard boilerplate, unqualified, both
   years and both entities (Note 2.1(c) standalone p.140; Note 2.1
   consol p.238)

Standalone: "The financial statements have been prepared on going concern
basis... Management is satisfied that the Company shall be able to
continue its business for the foreseeable future and no material
uncertainty exists that may cast significant doubt on the going concern
assumption" (p.140). Consol carries identical language for "the Group"
(p.238). No emphasis-of-matter, no material-uncertainty paragraph, and no
qualifying language anywhere else in the notes. This is worth stating
explicitly because the run's LBF4 (Sep-2026 rating downgrade, adjourned
NCD meeting) post-dates this AR by four months; the notes, as filed, give
no going-concern signal at all — consistent with LBF4 being outside this
document's window, not evidence the AR understated a known risk.

PASS 3 vs NO-FINDINGS GUARD: this pass produced five genuine pattern-level
findings (one contradiction, one clean tie-out, one disclosure-depth
contrast, one restatement-absence confirmation, one going-concern
confirmation) — it is not an empty pass.

═══════════════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Segment note reports "Share broking/trading" as ONE undifferentiated segment (₹1,387.84 Cr revenue, ₹533.90 Cr EBIT FY26); notes structurally cannot answer LBF1 prop-vs-client split. Net gain on fair value changes = 58.3% of consol total income, >5x fee income. | Note 45 consol p.289-290; Note 43 standalone p.183 (defers entirely) | 🔴 | Central to the run's transition thesis; management's "60% client by volume" claim is unreconcilable to this revenue mix from filed evidence |
| 2 | Parent's share of consolidated profit ROSE from 75.28% (FY25) to 92.03% (FY26) — group earnings concentration in the standalone entity increased, opposite of a subsidiary-led diversification narrative | Note 62 consol pp.327-330 | 🔴 | Directly undercuts any bull case resting on subsidiaries (NBFC, algo-tech, insurance, wealth) diversifying earnings away from parent's prop/broking book |
| 3 | Share India Algoplus (100%-owned) PAT fell 64.7% YoY (₹67.61 Cr to ₹23.83 Cr); Share India Securities (IFSC) swung from ₹3.97 Cr profit to ₹4.18 Cr loss. No narrative explanation given (Schedule III is numbers-only by design) | Note 61/62 consol pp.325-330 | 🔴 | Two of the group's operating subsidiaries deteriorated sharply in the same year the parent's own EPS rose; feeds Q&A item and Rank 2 finding |
| 4 | NCD funding-stress origin: ₹99.90 Cr First-Issue NCD needed an end-use change NCD holders/Trustee would not approve; Board (19-May-2026) pivoted to proposing early redemption instead. A separate ₹30.85 Cr subsidiary NCD matures 1-Oct-2026 | Note 17e standalone p.171; Note 18e/18c consol pp.271-272 | 🔴 | Pre-dates and plausibly explains the Sep-2026 adjourned NCD holders' meeting in company memory (LBF4); two distinct NCD events cluster around Sep-Oct 2026 |
| 5 | The Company's OWN footnote states reported DSCR/ISCR "exclude the impact of proposed early redemption of NCDs" — i.e. the headline ratio is computed on the pre-acceleration schedule, not the economically live one | Note 58a standalone p.218; Note 63a consol p.328 | 🔴 | Company-disclosed qualifier proving FY26 reported debt-service coverage is a floor, not the true near-term position, once the Board's own redemption plan executes |
| 6 | Contingent liabilities (bank guarantees, almost entirely exchange margin) grew 48.3% YoY consol to ₹3,232.72 Cr, far outpacing revenue growth (~1-2% consol); FDs pledged as collateral grew 42.7% to ₹1,526.88 Cr | Note 44/44a consol p.288; Note 42/42a standalone p.186 | 🔴 | Guarantee corpus scaling with trading-book/derivatives exposure, not reported income; standard for a clearing member but the growth-rate gap is the item to track |
| 7 | DSCR/ISCR and two further ratios deteriorated: DSCR 4.79x→3.25x standalone (2.74x consol); long-term debt/working capital up 4.7x standalone, 2.2x consol; debtor turnover down 29.8% standalone, 34.2% consol | Note 58a standalone p.218; Note 63a consol p.328 | 🟡 | Funding structure and receivables efficiency both worsened in FY26, before the Sep-2026 rating action; feeds FLAG-CASH |
| 8 | Trade receivables from related parties and director-linked firms jumped from near-zero to ₹8.26 Cr and ₹7.89 Cr respectively, a >100x increase, unexplained in the note | Note 7 standalone p.156 | 🟡 | Genuine new finding not in company memory; a concrete Q&A item |
| 9 | LBF2's promoter-pledge question has NO note-level home at all (pledge status is not an Ind AS notes item); separately, a NEW ₹50.04 Cr FY26 company borrowing is secured against "lien on shares of promoter, directors and relatives" | Note 18 standalone p.171-172 | 🟡 | Related but distinct fact from the BSE-SHP-level promoter share pledge (LBF2); both now put promoter shareholdings behind company or third-party credit |
| 10 | Consolidated deferred tax swung from a ₹4.97 Cr net liability to a ₹1.48 Cr net asset, most plausibly originating in lower-profit Algoplus; DTA realisability not independently testable from the notes | Note 13/42 consol pp.261, 282-285 | 🟡 | Ind AS 12 realisability question sits directly on top of the Rank 3 subsidiary profit collapse |
| 11 | Parent is exiting a Master Trust Limited FVOCI stake (-93.5%, gains never pass through P&L) while a subsidiary independently holds a Master Trust FVPL position that absorbed a 55.6% mark-to-market decline without trimming | Note 10/10A/10B standalone pp.159-160, consol pp.258-260 | 🟡 | Single-name concentration and risk-discipline question underneath the group's still-positive aggregate trading gains; also an earnings-quality point (FVOCI exits never hit PAT) |
| 12 | A new Level 3 (illiquid/model-valued) slice appears inside "Securities for trade" this year: ₹33.03 Cr, 13.6% of the book, versus 0% Level 3 in FY25 | Note 53 standalone pp.207-208 | 🟡 | "Held for trading" is meant to be the most liquid book on the balance sheet; some of it is not, in fact, exchange-quoted |
| 13 | Note 62 ("no significant events") sits beside a same-day (19-May-2026) Board resolution on NCD early redemption disclosed only inside the debt note, never surfaced as an "event" | Note 62/66 vs Note 17e/18e | 🟡 | Pattern-pass finding: a placement/completeness question on the company's own subsequent-events note, not a fabricated timing gap |
| 14 | Auditor change confirmed via a payment to the "erstwhile auditor" (₹1.50 lakhs, FY25); predecessor not named, reason not disclosed. Separately, related-party revenue lines collapsed unexplained: brokerage from Idhyah Futures -99.2% (₹280.99 lakhs to ₹2.26 lakhs); rent to Aggarwal Enterprises +133.0% | Note 39 standalone p.183; Note 52 pp.205-206 | 🟡 | Three unexplained swings in adjacent disclosure families; none individually alarming, together a pattern of thin narrative around related-party and governance changes |
| 15 | NBFC segment (Fincap) revenue -2.4%, EBIT -5.7% even as its loan book grew and impairment allowance rose 58.9%; segment liabilities fell 37.3%. The segment currently shrinking, not diversifying, the group's earnings base | Note 45 consol pp.286-287, cross-ref Note 9 consol p.257 | 🟢/🟡 | Sharpens Rank 2: none of the subsidiary businesses (NBFC, Algoplus, IFSC) is currently the profit-diversification engine a "subsidiary-led transition" narrative would need on FY26's numbers |

## B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Ind AS 115 (fee income) vs Ind AS 109 (proprietary trading, "as and when trade is executed") correctly separated (Note 2.13, p.147-148); FY26 fair-value gain is 95%+ realised-trade profit, not unrealised marks (Note 30) — a genuine quality-of-earnings positive |
| Expense capitalisation honesty | 8 | Depreciation useful lives within Schedule II norms, no extension (Note 2, p.142); ESOP compensation properly expensed through P&L (Note 37, 46); no evidence of opex capitalised as an asset |
| Provisioning adequacy | 4 | Standalone MTF impairment allowance is NIL both years under an unchanged "always Stage 1" assumption (Note 9, Note 54 p.211), not spot-tested in the notes against the group NBFC's 4.30% GNPA (MD&A, not notes); consol loan-loss allowance IS rising faster than the book (+58.9% vs +35.4%), so the group is not blind to credit risk, but the parent MTF policy is the weakest link |
| RPT fairness | 6 | Disclosure format (SEBI LODR Reg 53(F)) is complete and compliant, but several material swings (Idhyah Futures brokerage -99.2%, Aggarwal Enterprises rent +133.0%, trade receivables from related parties >100x) carry no qualitative explanation |
| Disclosure transparency | 5 | Segment note is a structural non-disclosure of the run's central question (prop vs client); Schedule III AOC-1 gives subsidiary swings as numbers only, no narrative; Capital management note omits the SEBI net-worth quantum; set against genuinely strong disclosure elsewhere (fair value hierarchy, financial risk management, employee benefits, leases) |
| Consistency with prior years | 7 | Accounting policies unchanged YoY, no first-time-adoption surprises; only inconsistency is the generic, unquantified prior-year regrouping statement (Note 64/68) |
| **OVERALL** | **6** | Clean at the line-item level (no classic earnings-management red flags: no goodwill-impairment gaming, no revenue manipulation detected, realised-gain quality is good), but pulled down by the MTF "always Stage 1" assumption and the structural opacity on prop-vs-client and subsidiary narrative disclosures |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Prop-trading dependence the segment note cannot disaggregate | High | Any future segment/note redesign; management Q&A on prop vs client split | Ongoing; resolved only outside this AR |
| NCD early redemption / refinancing execution | High | NCD holders' meeting outcome, Debenture Trustee approval, actual redemption date, the separate subsidiary NCD maturing 1-Oct-2026 | Imminent — Q2/Q3 FY27 |
| DSCR/ISCR understate near-term coverage (company's own exclusion) | High | Pro-forma DSCR once early redemption executes; covenant headroom | Next 1-2 quarters |
| Guarantee corpus (48.3% YoY) outpacing revenue | Medium | Guarantee-to-net-worth ratio; exchange margin calls in a volatile market | Ongoing; spikes with market volatility |
| Subsidiary profit collapse undiversifying the parent (Algoplus, IFSC) | Medium | Subsidiary quarterly disclosures; FY27 AOC-1 | Already occurred FY26; recurrence risk FY27 |
| MTF "always Stage 1" ECL assumption vs group NBFC GNPA 4.30% | Medium | Any future Stage 2/3 reclassification of the MTF book | Triggered by a market downturn / client margin-call defaults |
| Promoter/company assets increasingly pledged as collateral (FDs, property, and now a company loan secured on promoter/director/relative shares) | Medium | Any enforcement action, top-up demand, or covenant breach | Triggered by a guarantee call or loan-covenant event |
| Unexplained RPT and receivable swings (Idhyah Futures, Aggarwal Enterprises, related-party receivables) | Low-Medium | Management clarification; next AR/quarterly RPT note | Next disclosure cycle |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. What is the FY24-FY26 and Q1 FY27 split of revenue and profit between proprietary trading and client-driven business (brokerage, MTF interest, fees), given the segment note reports "share broking/trading" as one line and proprietary fair-value gains are 57.8% (standalone) / 58.3% (consol) of total income?
2. What is the current status of the ₹99.90 Cr First-Issue NCD early redemption the Board approved on 19-May-2026, why did NCD holders/the Trustee not approve the original end-use change, and what pro-forma DSCR results once the redemption is included (the reported ratio explicitly excludes it)?
3. What drove Share India Algoplus's 64.7% PAT decline and Share India Securities (IFSC)'s swing from a ₹3.97 Cr profit to a ₹4.18 Cr loss in FY26, and are these expected to reverse or persist into FY27?
4. What explains the >100x jump in trade receivables from related parties and director-linked firms (₹6.12 lakhs to ₹826.37 lakhs), the 133.0% jump in rent paid to Aggarwal Enterprises, and the 99.2% collapse in brokerage income from Idhyah Futures?
5. Why does the standalone MTF book carry a NIL impairment allowance and remain classified entirely as Stage 1 across both years, given the group NBFC subsidiary's GNPA of 4.30% (per MD&A); and what is the actual quantum of the SEBI-prescribed minimum net worth the Company must maintain (Note 55 confirms the requirement exists but not the number)?

## E. NOTES-BASED RED FLAGS

- Structural non-disclosure of the prop-vs-client revenue split (a segment-design choice, not an Ind AS violation, but the run's central transparency gap).
- The Company's own footnote excludes a known, Board-approved future cash outflow (NCD early redemption) from its headline DSCR/ISCR ratios.
- An unchanged, aggressive "always Stage 1" ECL assumption on the MTF book across two years of rapid book growth (+69.8% YoY), untested in the notes against the group's own NBFC GNPA.
- Parent profit concentration rose to 92.03% of the consolidated total, the opposite direction from any subsidiary-diversification narrative the bull case might need.
- No classic earnings-management indicators found: no goodwill-impairment gaming, no revenue-recognition manipulation, no opex capitalised as an asset, no unusual one-off/exceptional-item pattern across years. The auditor change (Note 39) is flagged for its lack of a stated reason, not as evidence of impropriety.

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate, structurally opaque accounting practices. Key
concern: prop-trading dependence and NCD refinancing stress the company's
own ratios do not fully capture. Key strength: internally consistent
revenue tie-outs and conservative, largely realised-gain revenue
recognition. Overall accounting quality: 6/10.

═══════════════════════════════════════════════════════════════════

```yaml
stage: B02-notes
company: "SHAREINDIA"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
input_gaps: []
flags:
  - {type: FLAG-CASH, reason: "Debtor turnover fell 29.8% standalone / 34.2% consol, DSCR fell 4.79x-3.25x standalone (4.62x-2.74x consol), long-term debt/working capital rose 4.7x standalone (2.2x consol), and the company's own footnote (Note 58a/63a) excludes the Board-approved NCD early redemption from the reported DSCR (Note 17e/18e). Balance-sheet growth (MTF book +69.8% YoY) was funded by new debt/NCDs (net financing inflow Rs 215.05 Cr, Note 57), not retained cash."}
accounting_quality: 6        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Segment note reports share broking/trading as ONE undifferentiated segment; proprietary fair-value gains are 58.3% of consol total income, >5x fee income; notes structurally cannot answer the prop-vs-client (LBF1) question.", note_ref: "Note 45 consol p.289-290; Note 43 standalone p.183", rating: "RED", why: "Central to the run's transition thesis; management's 60% client-by-volume claim is unreconcilable to this revenue mix"}
  - {rank: 2, finding: "Parent's share of consolidated profit rose from 75.28% (FY25) to 92.03% (FY26): group earnings concentration increased, opposite of a subsidiary-led diversification narrative.", note_ref: "Note 62 consol pp.327-330", rating: "RED", why: "Undercuts any bull case resting on subsidiaries diversifying earnings away from the parent's prop/broking book"}
  - {rank: 3, finding: "Share India Algoplus PAT fell 64.7% YoY (Rs 67.61 Cr to Rs 23.83 Cr); Share India Securities (IFSC) swung from Rs 3.97 Cr profit to Rs 4.18 Cr loss; no narrative explanation given (Schedule III numbers-only).", note_ref: "Note 61/62 consol pp.325-330", rating: "RED", why: "Two operating subsidiaries deteriorated sharply the same year parent EPS rose; feeds the profit-concentration finding"}
  - {rank: 4, finding: "NCD end-use change refused by holders/Trustee; Board pivoted to proposing early redemption of the Rs 99.90 Cr First-Issue NCD on 19-May-2026. A separate Rs 30.85 Cr subsidiary NCD matures 1-Oct-2026.", note_ref: "Note 17e standalone p.171; Note 18e/18c consol pp.271-272", rating: "RED", why: "Plausible origin of the Sep-2026 adjourned NCD holders' meeting (LBF4); two distinct NCD events cluster around Sep-Oct 2026"}
  - {rank: 5, finding: "Company's own footnote states reported DSCR/ISCR exclude the impact of the proposed NCD early redemption.", note_ref: "Note 58a standalone p.218; Note 63a consol p.328", rating: "RED", why: "Proves FY26 reported debt-service coverage is a floor, not the true near-term position, once the Board's own redemption plan executes"}
  - {rank: 6, finding: "Contingent liabilities (bank guarantees, mostly exchange margin) grew 48.3% YoY consol to Rs 3,232.72 Cr, far outpacing revenue growth (~1-2% consol); pledged FDs grew 42.7% to Rs 1,526.88 Cr.", note_ref: "Note 44/44a consol p.288; Note 42/42a standalone p.186", rating: "RED", why: "Guarantee corpus scaling with trading-book/derivatives exposure, not reported income"}
  - {rank: 7, finding: "DSCR/ISCR and two further ratios deteriorated: long-term debt/working capital up 4.7x standalone/2.2x consol; debtor turnover down 29.8% standalone/34.2% consol.", note_ref: "Note 58a standalone p.218; Note 63a consol p.328", rating: "YELLOW", why: "Funding structure and receivables efficiency both worsened in FY26, before the Sep-2026 rating action; feeds FLAG-CASH"}
  - {rank: 8, finding: "Trade receivables from related parties and director-linked firms jumped from near-zero to Rs 8.26 Cr and Rs 7.89 Cr respectively, a >100x increase, unexplained.", note_ref: "Note 7 standalone p.156", rating: "YELLOW", why: "Genuine new finding not in company memory; a concrete Q&A item"}
  - {rank: 9, finding: "No note-level home exists for the promoter share-pledge question; separately a new Rs 50.04 Cr FY26 company borrowing is secured against lien on shares of promoter, directors and relatives.", note_ref: "Note 18 standalone p.171-172", rating: "YELLOW", why: "Related but distinct from the BSE-SHP-level promoter pledge (LBF2); both put promoter shareholdings behind credit"}
  - {rank: 10, finding: "Consol deferred tax swung from a Rs 4.97 Cr net liability to a Rs 1.48 Cr net asset, plausibly originating in lower-profit Algoplus; DTA realisability not testable from the notes.", note_ref: "Note 13/42 consol pp.261, 282-285", rating: "YELLOW", why: "Ind AS 12 realisability question sits directly on the subsidiary profit collapse (finding 3)"}
  - {rank: 11, finding: "Parent exiting a Master Trust Limited FVOCI stake (-93.5%, never through P&L) while a subsidiary's FVPL position in the same stock absorbed a 55.6% mark-to-market decline without trimming.", note_ref: "Note 10/10A/10B standalone pp.159-160, consol pp.258-260", rating: "YELLOW", why: "Single-name concentration/risk-discipline question underneath the group's positive aggregate trading gains"}
  - {rank: 12, finding: "A new Level 3 (illiquid/model-valued) slice appears inside Securities for trade this year: Rs 33.03 Cr, 13.6% of the book, versus 0% Level 3 in FY25.", note_ref: "Note 53 standalone pp.207-208", rating: "YELLOW", why: "Held-for-trading book is meant to be the most liquid on the balance sheet; some of it is not exchange-quoted"}
  - {rank: 13, finding: "Events-after-reporting-date note (no significant events) sits beside a same-day 19-May-2026 Board resolution on NCD early redemption disclosed only inside the debt note.", note_ref: "Note 62/66 vs Note 17e/18e", rating: "YELLOW", why: "Placement/completeness question on the company's own subsequent-events note (Pass 3 pattern finding)"}
  - {rank: 14, finding: "Auditor change confirmed via payment to an erstwhile auditor, predecessor unnamed and reason not disclosed; related-party brokerage from Idhyah Futures collapsed 99.2%; rent to Aggarwal Enterprises rose 133.0%.", note_ref: "Note 39 standalone p.183; Note 52 pp.205-206", rating: "YELLOW", why: "A pattern of thin narrative around related-party and governance changes, none individually alarming"}
  - {rank: 15, finding: "NBFC segment (Fincap) revenue -2.4%, EBIT -5.7% even as its loan book grew and impairment allowance rose 58.9%; not currently a profit-diversification engine.", note_ref: "Note 45 consol pp.286-287, cross-ref Note 9 consol p.257", rating: "GREEN/YELLOW", why: "Sharpens finding 2: none of the subsidiary businesses is currently diversifying group earnings on FY26's numbers"}
red_flags:
  - "Structural non-disclosure of prop-vs-client revenue split in the segment note (Note 45 consol p.289-290; Note 43 standalone p.183)"
  - "Company's own footnote excludes the Board-approved NCD early redemption from reported DSCR/ISCR (Note 58a p.218; Note 63a p.328)"
  - "Unchanged, aggressive always-Stage-1 ECL assumption on the MTF book across two years of 69.8% book growth, untested against group NBFC GNPA of 4.30% (Note 9 p.157-158; Note 54 p.211)"
  - "Parent profit concentration rose to 92.03% of consolidated total, opposite of a subsidiary-diversification narrative (Note 62 consol pp.327-330)"
  - "No classic earnings-management indicators found: no goodwill-impairment gaming, no revenue-recognition manipulation, no opex capitalisation detected"
questions_for_mgmt:
  - "What is the FY24-FY26 and Q1 FY27 split of revenue and profit between proprietary trading and client-driven business, given the segment note reports share broking/trading as one line and proprietary fair-value gains are 57.8-58.3% of total income?"
  - "What is the current status of the Rs 99.90 Cr NCD early redemption approved 19-May-2026, why did holders/Trustee not approve the original end-use change, and what is the pro-forma DSCR including this redemption?"
  - "What drove Algoplus's 64.7% PAT decline and IFSC's swing from a Rs 3.97 Cr profit to a Rs 4.18 Cr loss in FY26, and will these reverse in FY27?"
  - "What explains the >100x jump in related-party/director-linked trade receivables, the 133.0% jump in rent to Aggarwal Enterprises, and the 99.2% collapse in Idhyah Futures brokerage?"
  - "Why does the MTF book carry a NIL impairment allowance and remain always-Stage-1 across both years given the group NBFC's 4.30% GNPA, and what is the actual quantum of the SEBI-prescribed minimum net worth the Company must maintain (Note 55 confirms the requirement but not the number)?"
receivables_trend: "deteriorating - trade receivables ageing bucket itself stayed clean (98.7-98.9% under 6 months both years, Note 7 standalone p.156), but debtor turnover fell 29.8% standalone (5.87x to 4.12x) and 34.2% consol (7.13x to 4.69x) per the Schedule III ratio note (Note 58a p.218; Note 63a p.328), and trade receivables from related parties/director-linked firms rose from near-zero to Rs 8.26 Cr and Rs 7.89 Cr respectively (Note 7 p.156), unexplained"
restatements_found:
  - "No restatement or prior-period-error correction found anywhere in the AR (document-wide check, zero matches for restate/restated). Only prior-year adjustment language is a generic, unquantified regrouping statement: 'previous year figures have been regrouped/reclassified... does not affect overall financial position', with no rupee amount disclosed (Note 64 standalone p.221; Note 68 consol p.331)"
going_concern_language: "NONE - standard unqualified going-concern basis stated both years and both entities: 'Management is satisfied that the Company [Group] shall be able to continue its business for the foreseeable future and no material uncertainty exists' (Note 2.1(c) standalone p.140; Note 2.1 consol p.238). No emphasis-of-matter or material-uncertainty paragraph found anywhere in the notes."
analyst_note: "The single most load-bearing item across all three passes is not any one red flag but a chain: the segment note cannot show prop-vs-client (finding 1), the parent's share of group profit rose to 92% while two subsidiaries deteriorated (findings 2-3), and the company's own DSCR footnote admits its headline ratio excludes a redemption it has already resolved to make (finding 5). Read together, FY26 is a year where the parent's prop-trading book carried the group, funded by new debt, while the diversification subsidiaries the transition thesis needs (NBFC, Algoplus) went the wrong way. None of this is accounting manipulation; it is a business-model and disclosure-design finding for Role 1/6 to weigh, not a notes-level fraud signal."
```
