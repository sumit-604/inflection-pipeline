# PROCEED WITH FLAGS

TAAL Tech Ltd (TAALTECH) | Run: runs/taaltech-2026-09-10 | Run date: 2026-09-10
Phase 1 (evidence) only. Stages 10 and 11 did not run.

**Scope of this verdict.** This is the go / no go on the evidence record alone.
It says the phase 1 record is good enough to carry into Halt 1 and FTTCP
deliberation, with the flags below travelling with it. It is not a valuation
verdict, not a decision, and not a price. There is no fair value, no destination
PE, no Hurdle Ratio, no entry range and no BUY / WATCHLIST / AVOID in this run.

**Verdict rule applied: rule 3.** FLAG-PROMOTER is active with verdict CONCERN
and FLAG-CASH is active, which lands the verdict at PROCEED WITH FLAGS.

**Transition posture: not set in phase 1.** The decision matrix needs three state
variables. Two are readable now: the proof gate has NOT fired (the three quarter
acceleration is filed but its cause is unexplained in every document management
wrote), and the ugliness classification is unresolved (the cash fall is
INDETERMINATE between artifact of climb and structural feature). The third, the
recognition gap, resolves at stage 11, which did not run. No posture is
assignable without it.

---

## How the verdict was reached

**Rule 1, REWORK: does not fire.** Verifier A returned zero CRITICAL findings on
127 checked numbers. The lowest verifier acceptance rate is 64 (Verifier B),
above the 60 floor. Overall confidence is 64, above the 60 floor.
`rework_triggered: false` in every verifier block.

**Source fidelity gate: clear.** One Verifier A finding carries
`source_fidelity: true`. It is the FY2026 Other Income figure, Rs19.40cr from
screener against Rs19.03cr in audited Consolidated Note 25 (AR p.143). The
audited figure governs. It was already flagged by the pipeline at stage 2 and no
verdict input in this run rests on the screener figure. Disposition and carrier
by carrier detail are in verifier-disagreement-log.md.

**Rule 2, INSUFFICIENT EVIDENCE: considered, does not fire.** Two stages carry
status: partial (see the named line below). Neither stage 2 nor stage 3 was
skipped, and Gate 0 ran on populated screening data plus three results filings.
The decision relevant record, the FY2025-26 annual report, three results filings,
the 27 May 2026 corrigendum and eleven peer transcripts, is intact and was
verified at 96.9% numerical acceptance. The gaps are external lookups that Claude
web closes at Halt 1, not holes in the filed record. Per rule 2's own wording,
partial gaps that leave the decision relevant record intact cap at PROCEED WITH
CAVEATS rather than trigger this rule.

**Rule 3, PROCEED WITH FLAGS: fires.** FLAG-PROMOTER active (verdict CONCERN, no
deal breakers) and FLAG-CASH active.

**The INDETERMINATE cash cap.** The cash determination below is INDETERMINATE,
which caps the verdict at PROCEED WITH CAVEATS. That cap is a ceiling on
optimism, not a floor. PROCEED WITH FLAGS already sits one level below the cap,
so the cap binds nothing here. A flag never softens a verdict.

**Rule 4, the confidence band.** Overall confidence is 64, inside the 60 to 74
band, which downgrades a PROCEED one level. Rule 3 already landed the verdict two
levels below PROCEED. Applying a further downgrade would produce REWORK, which
the confidence block explicitly rules out (`rework_triggered: false`, no Verifier
A CRITICAL, no acceptance rate below 60). PROCEED WITH FLAGS holds.

---

## FLAG-PROMOTER

**Status: ACTIVE. Verdict: CONCERN. Deal breakers: NONE. Stage status: PARTIAL.**

**Top two findings**

1. Rs10cr unsecured loan to Vishkul Enterprises Private Limited, the holding
   company that owns 50.74% of TAAL Tech, granted in FY26. Form AOC-2 (Annexure
   E, AR p.56) returns "NA" for every field in both parts. CARO Annexure A clause
   3(iii)(a) (AR p.60) discloses the loan as granted during the year; clause
   3(iii)(d), four lines later, states no loan was given during the year. No
   contractual rate, tenure, security, purpose or board approval date appears
   anywhere in 164 pages. Note 37(B) (AR p.98) books Rs98.55 lakh of interest on
   it, a derived rate near 9.85%, while Note 37(C) states related party balances
   are interest free except for borrowings. CARO 3(iii)(c) asserts principal
   repayments are regular as per stipulation on a loan whose opening balance was
   nil and whose full Rs1,000.00 lakh was still outstanding at year end. No
   Regulation 30 disclosure or shareholder approval was found.
   (B08 adverse_findings 1-3; B02 top_findings 3 and 9; B12b G4, G7)

2. Narayan Vithal Karbhase was appointed to TAAL Tech's audit committee with
   effect from 4 August 2025 (AR p.39), the committee whose stated functions
   include approval of related party transactions, and he is a director of
   Vishkul Enterprises Private Limited, the borrower (AGM notice p.27, item 2).
   He is also a director of Asscher Enterprises Limited, which Note 37(A) names
   as an entity under common control. No document in the corpus discloses the
   conflict, records a Section 184 interest declaration, or records a recusal.
   (B03 flags FLAG-PROMOTER-PRELIM; B08 adverse_findings 4; B12b G6, CRITICAL)

**Third finding carried, because it is the largest single gap.** Who controls
Vishkul Enterprises Private Limited could not be established. Directors,
shareholders, financials and other holdings are all NOT FOUND after ten or more
search and fetch attempts (MCA, Zauba, Tofler and InstaFinancials all blocked or
tool errored). (B08 adverse_findings 6)

**One unadopted item, listed so the operator can check it live.** A single web
search summary referenced a SEBI "warning letter" dated 23 April 2026. It could
not be corroborated against any primary source and the underlying BSE PDFs
returned 403. NOT ADOPTED as a finding. Possible tool artifact. (B08
adverse_findings 5)

**Transition evidence: FOUND.**

- Two credentialed independent directors added: Anil Kumar Sahu (May 2025) and
  Muralidhar Chitteti Reddy (August 2026). (B08 transition_evidence 1)
- Auditor continuity through a documented casual vacancy firm merger process, not
  a resignation. Both the predecessor and successor opinions are unmodified.
  (B08 transition_evidence 2)
- Dividend payout ratio rose from about 17% of profit in FY25 to about 38% in
  FY26. (B08 transition_evidence 3)
- NCLT approved 2025 merger of TAAL Tech India Pvt Ltd into the listed parent,
  plus the CMD five year term formalised in August 2025. Structural
  simplification of the core operating business. (B08 transition_evidence 4)
- Zero promoter pledge, holding stable at 50.74% for Vishkul and 50.80% for the
  promoter group, 1:5 stock split with record date 22 September 2026. Pledge is
  aggregator corroborated across screener.in, tijorifinance.com and
  marketsmojo.com, not primary verified (403 on the SEBI shareholding pattern
  fetch). (B08 transition_evidence 5, pledge_pct_latest 0)

**Counterweight the verifier added, not yet in the promoter verdict.** Verifier B
raised a second CRITICAL: Muralidhar Chitteti Reddy is proposed as an independent
director with a Section 149(6) declaration (AGM notice p.6 and p.22), while Note
37(B) of the audited standalone statements (p.98) records sitting fees paid to
him as a Non Whole Time Director of Rs0.80 lakh in FY26 and Rs1.26 lakh in FY25,
attributed by the governance report to TAAL Tech India Pvt Ltd, amalgamated into
the company with appointed date 1 April 2023. The explanatory statement discloses
none of it. This item post dates the promoter stage and is unresolved. (B12b G8,
CRITICAL)

---

## FLAG-CASH

**Status: ACTIVE. Determination: INDETERMINATE.**

**The evidence, both directions.**

Consolidated operating cash flow was Rs1,874.29 lakh in FY26 against Rs4,102.40
lakh in FY25, a 54% fall while profit rose 16% (Q4FY26 results p.17). Cash flow
over profit fell from 0.84x to 0.33x. Unbilled revenue, the contract asset, went
from Rs4.64cr to Rs13.75cr, up 196%, and from 10.4% to 24.1% of the exit
quarter's revenue (consolidated Note 14, AR p.137). Trade receivables rose 34.8%
to Rs52.04cr (Note 10). Full year revenue grew 6.6%. Receivables plus unbilled
rose 55.7% on that 6.6%. Working capital days moved 77 to 120. (B01, B02, B03,
B04 all carry FLAG-CASH on this evidence)

Peer evidence runs the other way at all three peers, in the same window. Onward
Technologies improved days sales outstanding from 73 to 70. Cyient converted free
cash flow to profit at 163% in Q4 FY26 and 80.5% in Q1 FY27, narrating "sustained
focus on working capital efficiency and collections discipline" both times. Tata
Elxsi's only working capital event was a Chapter 11 customer provision, which is
a credit event, not a billing cycle event. No peer describes a lengthening
billing cycle. (B06 FLAG-WC-GAP; B06 contradicted 2)

Two facts push back toward growth. The receivables ageing is clean: the tail
older than six months is 2.0% of gross against 1.5% a year earlier, so nothing in
the book looks uncollectible. And the balance sheet date sits one month after a
quarter in which revenue jumped 24.6% sequentially to Rs57.04cr. A quarter end
that is 24.6% larger than the one before it mechanically inflates the contract
asset measured on that date.

One fact makes the group picture worse than the parent picture. Standalone
operating cash flow of Rs2,885.27 lakh is held up by a Rs1,396.81 lakh increase
in the payable to the company's own US subsidiary, from Rs603.70 lakh to
Rs2,000.51 lakh, or 50 days to 154 days of intra group payables (Note 37(B),
p.98). That eliminates on consolidation, which is exactly why consolidated
operating cash flow is Rs1,874.29 lakh. Note 41(d) then presents the standalone
cash flow as the consolidated one. A reader who trusts Note 41 computes 0.51x
instead of the true 0.33x. (B12b F5; B02 top_findings 6)

**Why INDETERMINATE and not GROWTH-INDUCED.** Growth induced requires the working
capital build to scale with the growth that caused it. Over FY26 as a whole it
did not: working capital grew about eight times faster than sales. The peer
evidence removes the "normal ER&D growth phase pattern" reading, because three
peers growing in the same window moved the other way.

**Why INDETERMINATE and not STRUCTURAL.** Structural requires evidence the
billing cycle itself broke. The ageing does not show it, the company carries zero
debt and a 9.49x current ratio, and the exit quarter step gives a mechanical
explanation for a large part of the March 2026 contract asset. There is no
rating agency working capital commentary to quote: the annual report states the
company was not required to obtain a credit rating in FY2025-26 because fund
based and non fund based facilities were NIL (AR extract, lines 3270-3271). That
verbatim source, normally the tiebreaker on this flag, does not exist for this
company.

**Missing evidence, named.** The determination cannot be closed without these
three items and no other item substitutes for them.

1. A contract asset (unbilled revenue) rollforward or ageing schedule. Neither
   the standalone nor the consolidated note set carries one, so opening balance,
   additions, billings and reversals cannot be separated. (B03 flags FLAG-CASH)
   Where to obtain: the next annual report Note 14, or a direct company request.
2. The H1 FY27 cash flow statement. Indian quarterly filings carry a cash flow
   only at half year and full year, so the first post acceleration cash read
   lands with the H1 FY27 results, due around November 2026. Where to obtain: BSE
   scrip code 539956.
3. Any management statement on the billing cycle. None exists. No earnings calls,
   no investor presentation, and the MD&A does not mention cash flow at all.
   Where to obtain: a written shareholder question at the next AGM, or the first
   earnings call if the company ever holds one.

**The observation that resolves it.** Unbilled revenue as a share of that
quarter's revenue in the H1 FY27 balance sheet, November 2026. It was 24.1% at
March 2026 and 10.4% a year earlier. Below 15% with revenue holding above Rs60cr
a quarter resolves the flag to GROWTH-INDUCED. At or above 24% with revenue flat
or falling resolves it to STRUCTURAL. Cash flow over profit above 0.7x in the
same statement confirms the first reading; below 0.5x for a second consecutive
period confirms the second.

---

## FLAG-GATE0

**Status: ACTIVE. Gate 0 grand total 81 of 160. Classification GOOD. Moat class
MODERATE, 2 moats confirmed of 12. Deal breakers: none.**

Block scores: A 15, B 14, C 12, D 20, E 9. Core score 70 of 100, moat score 11 of
60. (B01)

**Why the backward score sits where it does.**

The 20 of 20 in Block D is real and unarguable. Net cash of Rs26.87cr, no
borrowings, interest coverage above 100x, current ratio 5.26x on the audited
Q4 FY26 balance sheet.

The score depends on a base year. Blocks C1, C2 and C4 and moat sub test M1
anchor to FY2017, when profit was Rs3.81cr on a thin post demerger capital base.
That gives a nine year profit growth rate of 35.0% and a growth spread of
+26.15pp. Measure FY2022 to FY2026 instead and revenue growth is about 11% and
profit growth 15% to 16%, with a spread near +4.3pp. Both are arithmetically
correct. The second window is the decision relevant one. (B01 flags FLAG-GATE0)

The pre FY2022 rows carry an unresolved business mix question. TAAL Enterprises
received both the air charter business and TAAL Tech India in the October 2014
demerger from Taneja Aerospace. No pre FY2022 annual report is in this corpus, so
the run cannot say when charter revenue dropped out of the consolidated series.
FY2017 to FY2021 rows therefore carry a comparability flag that the annual report
in hand cannot settle: it presents only FY25 and FY26. (B01 input_gaps; B03
input_gaps)

Block B is the deteriorating one. Cumulative ten year cash flow over profit is
0.884x, which passes. The one year direction is 0.84x to 0.33x, which is the
FLAG-CASH finding above.

**Verifier C recomputation, carried here.** Verifier C found `history_downgrade`
set true against a rule whose only trigger is a three or four year history;
TAALTECH has ten. The classification correctly stayed GOOD, so the boolean and
the classification contradict each other and a machine consumer could apply an
unauthorised one tier drop. The corrected value is `history_downgrade: false`.
The comparability concern belongs in flags and data notes, where it already sits.
Verifier C also recomputed four MINOR Gate 0 defects (ROCE denominator, the FCF
positive year proportion, one FY2026 FCF cell, and moat sub test M11) and
confirmed the classification is GOOD under every one of them. (B12c F5, F1-F4)

---

## Every other active flag

| Flag | Stage | What it says | Anchor |
|---|---|---|---|
| FLAG-MARGIN-SOURCE | B04 | Genuine EBIT margin, other income excluded, is about 27.8% against roughly 13% at Onward Technologies on Rs544cr revenue and 12% at Cyient on Rs7,268cr. No offshore mix, pricing, utilisation or overhead disclosure in the annual report explains the spread. Called at stage 4 the single most important unresolved question in the run. **Status now: PARTLY RESOLVED, see the section below.** | AR p.37, p.90; B04 flags |
| FLAG-CONCENTRATION | B04 | Top customer at 24.05% of FY26 revenue and rising, in a business whose only confirmed moat is client relationship tenure. Data note: the prior year comparator is filed as 20.55% in B04 and 21.00% in B07; the run carries both and did not reconcile them. | Note 42, AR p.102 / p.157 |
| FLAG-DISCLOSURE | B04 | No investor presentation, no earnings calls, no utilisation, attrition or pricing metric anywhere. The MD&A itself states AI's impact on the sector is unassessed. Limits how far KPI tracking and pricing power classification can go on filed evidence. | AR p.37; B00 declared_not_gaps |
| FLAG-SILENCE | B05 | The three quarter revenue acceleration, Rs45.79cr to Rs57.04cr to Rs64.81cr, is unaddressed in every document management authored in this corpus. The only candidate sentence, "won multiple strategic accounts", is unquantified, unnamed and undated. | AR MD&A p.37; B05 flags |
| FLAG-FILING-CONTROL | B05 | The 26 May 2026 results filing carried two numerical errors inside audited financial statements. The investments current / non current swap drew a corrigendum on 27 May 2026. The Note 41 "Summarised Consolidated" table, which overstates profit before tax by 57%, profit after tax by 77.6% and operating cash flow by 54%, was never corrected. | AR Note 41 p.155-156; corrigendum extract; B12b D20 |
| FLAG-DEMAND-GAP | B06 | No peer transcript in the January to June 2026 window describes a sector wide ER&D demand step up. Tata Elxsi grew 0.9% to 1.3% quarter on quarter constant currency; Cyient's digital engineering unit shrank 2.4% then 0.5%. One narrow exception: Cyient's aerospace linked Transportation and Mobility cluster grew 13.2% to 14.8% year on year constant currency. | TATAELXSI Q4 FY26 p.2; CYIENT Q4 FY26 p.5 |
| FLAG-WC-GAP | B06 | Every peer working capital disclosure in this window points stable, improving or explicitly explained, the opposite direction to TAAL Tech. Removes the most charitable reading of the cash fall. | ONWARDTEC Q2/Q3 FY26 (DSO 73 to 70); CYIENT Q4 FY26 p.7 |
| FLAG-MARGIN-UNEXPLAINED | B07 | None of the 22 emerging moat categories supplies a documented moat based mechanism for the margin. The one partially evidenced explanation, lean overhead at 10.1% of revenue with R&D at 0.19%, is not a competitive advantage and is scale fragile. An unexplained margin is not a moat. | B07 flags; AR p.49 |
| FLAG-CONCENTRATION-DUAL-READ | B07 | The rising top customer share is the sole basis for the one Moderate category (C1) and simultaneously the top named risk to it. The annual report gives no evidence to separate broad wallet share deepening from a single program ramp. | Note 42, AR p.102 |
| FLAG-ZERO-CAPEX | B07 | Standalone property plant and equipment and right of use assets both fell year on year while revenue grew 7.1%. No capex programme exists anywhere in the annual report, so embedded growth arithmetic returns 0%. | B07 capex_embedded_growth_pct |
| FLAG-RPT | B01 | The FY2026 Rs10cr loan went to Vishkul Enterprises Pvt Ltd at a 9.85% effective rate. The actual holding company is Vishkul, not Taneja Aerospace, which shows only a trivial FY26 transaction. Rolled into FLAG-PROMOTER above. | Note 36(B) p.151; Note 13 p.85 |
| FLAG-SEARCH-FAILURE | B09 | WebSearch was unavailable on 20 of 20 calls. Total market and served market are both floors built from peer aggregation and analog proxies, not top down industry data. True figures are almost certainly larger. | B09 searches_skipped |
| FLAG-SOM-BASIS | B09 | The served share base uses the Q1 FY27 annualised run rate of about Rs259cr as the fresh evidence start, per the Amendment 26 basis hierarchy. That is one quarter of evidence, and the cause of the jump is unresolved. Confirming observation: Q2 and Q3 FY27 sustaining Rs64cr to Rs65cr or more per quarter. | B09 flags |
| FLAG-SAM-SHARE-TENSION | B09 | The served share gain implied is +10.6pp over three years and +16.6pp over five, above the normal 1-2pp and aggressive 3-5pp bands. Most likely an undersized served market denominator built from two analog peers under search failure, not an aggressive claim. Named so a later stage does not misread a measurement artifact. | B09 flags |
| FLAG-AI-UNRESOLVED | B09 | Management states it has not assessed AI's impact on the ER&D sector. Both the bearish reading (billable hour compression) and the bullish reading (demand expansion, safety critical work slower to substitute) are evidenced. No data this run calls a direction. Position size carries this, not the growth number. | AR MD&A p.37; B06 verified 3 |

---

## The margin question, restated with the verifier's finding

FLAG-MARGIN-SOURCE was raised at stage 4 as the single most important unresolved
question in the run. Verifier B reached the disclosure that answers a large part
of it, and neither stage 5 nor stage 6 got there.

**The disclosure.** AOC-1 (AR p.162) gives TAAL Technologies Inc, USA turnover of
Rs5,350.15 lakh and profit after tax of Rs303.90 lakh, a net margin of 5.68%.
Note 37(B) (AR p.98) shows the parent received services from that subsidiary
worth Rs4,734.48 lakh. That is 88.5% of the subsidiary's entire turnover and it
matches the parent's standalone "Cost of technical services" line exactly. The
Indian parent earns 28.3% net margin on Rs19,010.10 lakh. Consolidation
eliminates Rs4,878.76 lakh of intra group billing, 25.7% of standalone revenue.
(B12b D7, MAJOR, MISSED by both stage 5 and stage 6)

**What it settles.** It settles the shape of the business. The onshore arm is a
thin billing conduit earning a low risk service provider return, not a delivery
organisation. Delivery sits offshore in Bangalore at Indian cost, and the
contracts, the customer risk and therefore the residual profit are booked in
India. That is a mechanism, filed and arithmetically checkable, where the run
previously had none. It also settles how the consolidated margin should be read
against peers: the 27.84% group operating margin already carries the US arm's
5.68% inside it, so consolidation is not inflating the group figure. Peers with
large onshore delivery organisations carry a far heavier onshore cost base in
their own consolidated margins. TAAL Tech barely carries one.

**What it leaves open, in order of weight.**

1. Whether the 28.3% Indian margin survives a US challenge. A customer facing
   onshore arm on a 5.68% margin is the classic invitation to a transfer pricing
   adjustment. No transfer pricing study and no advance pricing agreement is
   disclosed anywhere in the annual report. An adjustment moves profit out of
   India and cuts the group's after tax margin. The two readings are that the
   contracts, IP and risk genuinely sit in India so the profit does, or that the
   structure is thin. The observation that separates them is the transfer pricing
   study or an APA, and it is disclosed nowhere.
2. The residual gap against Onward Technologies. Onward is also offshore heavy at
   similar scale and earns about 13%. Offshore mix narrows the spread against
   Cyient and Tata Elxsi. It does not close the gap against Onward, and no bill
   rate, utilisation or per account margin figure exists in the corpus to test it.
3. It says nothing about the revenue acceleration. Different question, still open.
4. Verifier B also weakened the peer side of the margin comparison. On the same
   transcript page stage 6 quoted, the Tata Elxsi CFO says the company is "making
   constant effort to go back to our original margin band, which is about 27% to
   28%". That is a band previously held, not one never reached. The claim that
   27.8% is "genuinely anomalous against the best comparable evidence" is
   withdrawn from this synthesis on that basis. (B12b pipeline_flags_not_supported
   1, OVERSTATED, MAJOR)

---

## Confidence delta, phase 1

| Component | Score | Source |
|---|---|---|
| Numerical acceptance | 96.9 | B12a invocation 2. 127 numeric claims checked, 123 clean, 3 MINOR, zero CRITICAL. |
| Red flag coverage | 64 | B12b. (10 caught + 3 partial at half credit) / 18 in scope flags. Strict caught only figure is 56. |
| Framework adherence | 88 | B12c, phase 1 portion only. 86 of 98 Gate 0 and Emerging Moat rule checks passed. |
| Peer utilisation | 81.8 | B12d. 9 of 11 transcripts mined substantively. |
| **Overall** | **64** | The minimum of the four. |

**Overall 64 places this run in the 60 to 74 band, which downgrades a PROCEED one
level.** The band is not a REWORK trigger: REWORK requires a Verifier A CRITICAL
or an acceptance rate below 60, and neither exists here.

**The weakest component is red flag coverage at 64, and it sets the overall.**
Verifier B independently found 34 red flags, 18 of them inside the stage 5 and
stage 6 scope. Those stages caught 10 outright and 3 in part and missed 5, all
MAJOR: the mark to market gain at 21.2% of profit whose increase is 84% of the
profit increase, the US subsidiary transfer pricing structure, the Rs938.46 lakh
contingent tax at 16.5% of profit, the Rs371.05 lakh customer claim reversal, and
R&D at 0.20% of revenue with technology absorption "NA". Verifier B's own two
CRITICAL findings are both governance items it routed to stage 8, which had
already reached CONCERN on overlapping evidence.

**Valuation framework adherence: PENDING PHASE 3.** Verifier C's stage 10 and
stage 11 audit does not run in phase 1 and its absence is not a REWORK trigger.

---

## Contradicted claims, peer stage

These are the run's priority monitoring items. Each was tested against eleven
peer transcripts and failed.

1. **"TAAL Tech's 24.6% then 13.6% sequential revenue jump reflects a sector wide
   ER&D demand step up." CONTRADICTED.** Tata Elxsi grew 0.9% to 1.3% quarter on
   quarter in constant currency; Cyient's digital engineering unit shrank 2.4%
   then 0.5%. Anchors: TATAELXSI Q4 FY26 call p.2 ("0.9% quarter-on-quarter");
   CYIENT Q4 FY26 call p.5 ("a degrowth of 2.4% quarter-over-quarter"). The
   acceleration is company specific, and still unexplained.

2. **"TAAL Tech's unbilled revenue tripling and cash conversion collapse reflect a
   normal ER&D growth phase billing cycle pattern." CONTRADICTED.** Onward
   Technologies improved days sales outstanding from 73 to 70; Cyient converted
   free cash flow to profit at 163% with explicit collections discipline.
   Anchors: ONWARDTEC Q2/Q3 FY26 calls; CYIENT Q4 FY26 call p.7 ("163%...
   sustained focus on working capital efficiency and collections discipline").

**One claim was verified in the company's favour and carries equal weight.** AI
has not yet materially compressed core ER&D services pricing, scope or headcount
in this window; the effect is concentrated in adjacent software coding, IT and
BPO work. Confirmed across all three peers with seven anchors. (B06 verified 3)

**Two peer stage conclusions were withdrawn by verifiers.** The Tata Elxsi margin
band omission and the single customer concentration benchmark are both recorded
as OVERSTATED, and the wrong quarter attribution of the "peers around 20%" quote
is recorded as a MAJOR quote fidelity failure. All three sit in
verifier-disagreement-log.md with their dispositions.

---

## Monitorables and triggers

Eight items, deduplicated from the annual report stage, the business model stage,
the emerging moat catalysts and the first deterioration signals.

1. **Unbilled revenue as a share of the quarter's revenue.** H1 FY27 results,
   around November 2026, "Other current financial assets" note. It was 24.1% at
   March 2026 against 10.4% a year earlier. Below 15% says the build was the
   growth step. At or above 24% with flat revenue says the billing cycle broke.
   This is the single item that resolves FLAG-CASH.

2. **Operating cash flow over profit after tax.** Same H1 FY27 statement. FY26 was
   0.33x, FY25 was 0.84x. Above 0.7x clears the flag. Below 0.5x for a second
   consecutive period makes it structural. Read the consolidated statement only,
   never Note 41's "Summarised Consolidated" table.

3. **Quarterly revenue run rate.** Q2 FY27 (November 2026) and Q3 FY27 (February
   2027) results. Q1 FY27 was Rs64.81cr. Sustained above Rs60cr for two more
   quarters confirms the acceleration is structural. A fall back into the Rs44cr
   to Rs49cr band held from March 2024 to September 2025 kills it. This tests the
   whole transition thesis.

4. **Top customer revenue share.** Next annual report, Note 42, around August
   2027. It was 24.05% in FY26 against roughly 21% in FY25. Above 28% to 30%
   turns the one credited moat, client tenure, into a dependency instead.

5. **The Vishkul loan balance and its terms.** Next quarterly related party filing
   and the next annual report Note 36 / 37. Rs10cr was outstanding at March 2026
   with no disclosed rate, tenure or security. Any growth beyond Rs10cr, or a
   first disclosure of terms and a board approval date, tests whether this year's
   approval trail was a one off or a practice.

6. **Any transfer pricing study, advance pricing agreement or US tax assessment.**
   Next annual report notes, or a Regulation 30 filing. None exists today. This is
   the one document that decides whether the 28.3% Indian parent margin survives.

7. **Genuine operating margin and employee cost.** Every quarterly result. Revenue
   minus total expenses over revenue was 27.84% in FY26 against 28.34% in FY25.
   Track employee benefits expense as a share of revenue beside it; a sharp
   unexplained move in either direction is the first sign the margin mechanism has
   changed. Ignore the company's own "Operating Profit Margin" ratio; it is profit
   before tax over revenue.

8. **Treasury book credit events.** Rs143.89cr, of which 85.5% (Rs122.96cr) is
   unquoted Level 3 paper concentrated in subordinated NBFC and fintech
   debentures and alternative credit funds. Watch news flow for any downgrade,
   default or redemption gate among the named holdings, and the impairment line in
   the next annual report Note 7. A mark to market gain of Rs1,204.05 lakh was
   21.2% of FY26 profit; the same book can run the other way.

---

## Falsification line

**Q2 FY27, around November 2026: consolidated revenue back below Rs57cr with
unbilled revenue still above 20% of that quarter's revenue.** That single print
kills both legs at once. It ends the acceleration and it removes the growth step
explanation for the contract asset build, leaving the structural reading of the
cash fall as the only one standing. The half year filing carries both figures, so
one document settles it.

---

## Stage status: B08 and B09 are both PARTIAL, and why it matters to the reader

**The named line.** The promoter stage (B08) and the market sizing stage (B09)
both closed with `status: partial`. WebSearch failed on roughly 75% to 80% of
promoter stage calls and on 20 of 20 market sizing calls. Neither partial status
feeds any of the four confidence components, so the 64 overall does not price
them in.

**What it means for the reader.** Two different things.

On the promoter side, the findings that drive the CONCERN verdict are all primary
source, read out of the annual report: the AOC-2 blank, the CARO self
contradiction, the missing board approval date, and the Karbhase directorship at
the borrower. Those stand at full confidence and do not depend on any search.
What the failure cost is the surrounding picture: who controls Vishkul
Enterprises, whether a Regulation 30 disclosure exists, whether Karbhase recused,
whether any proxy advisory has written on the name, and the 2015 demerger and
2025 merger swap ratio history. The identity of Vishkul's controllers is the
single largest open item in the run and should be closed with authenticated MCA
access or Claude web before this name goes past Halt 1.

On the market sizing side, the failure is more basic. There is no top down
industry figure in this run at all. The Rs23,678cr to Rs23,875cr total market and
the Rs1,100cr served market are floors built by adding up listed peers, and the
run says so. Treat the runway class GOOD and the 5.6x headroom as a floor
statement, not a measurement. The load bearing figure, the implied revenue growth
of 13.9% to 16.6%, is built bottom up from TAAL Tech's own filed headcount of 521
and revenue per engineer of Rs36.5 lakh, so it does not depend on the failed
searches.

---

## Publish check

📤 **PUBLISH CANDIDATE**

**The observation.** Inside TAAL Tech's audited consolidated financial statements
for FY2025-26, Note 41 presents a table headed "Summarised Consolidated"
statements. It is the standalone accounts with one expense line deleted. It
overstates profit before tax by 57%, profit after tax by 77.6% (Rs10,071.52 lakh
shown against Rs5,671.50 lakh actual) and operating cash flow by 54%. Note 41(a)
lists the parent as its own subsidiary. A reader who trusts that table computes
cash conversion of 0.51x instead of the true 0.33x, which reverses the single
most important finding about the company. The company filed a corrigendum the
next day for a smaller error in the same filing, an investments classification
swap, and never corrected this one.

**Why it is worth publishing.** It is a clean, checkable, single document
demonstration of why a reader must go to the audited consolidated statements and
not to a summary table, even a summary table sitting inside audited statements.
Everything needed to verify it is in one public annual report with page numbers.
No opinion required.

**Schedule slot type.** Forensic teardown of one note. Not a company call, not a
recommendation. The company is not named as a buy or sell anywhere in the post.

Post not drafted here.
