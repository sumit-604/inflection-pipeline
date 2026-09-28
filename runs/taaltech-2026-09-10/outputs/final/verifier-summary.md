# VERIFIER SUMMARY — TAAL Tech Ltd (TAALTECH)

Run: runs/taaltech-2026-09-10 | Run date: 2026-09-10 | Phase 1 (evidence) only.

All four phase 1 verifiers' findings in one document, sorted CRITICAL first, then
MAJOR, then MINOR. No commentary beyond what the verifiers wrote.

---

## CONFIDENCE DELTA, PHASE 1

| Component | Score | Verifier | Basis |
|---|---|---|---|
| Numerical acceptance | 96.9 | A (B12a, invocation 2) | 127 numeric claims checked, 123 clean |
| Red flag coverage | 64 | B (B12b) | (10 caught + 3 partial at half credit) / 18 in scope flags; strict caught only 56 |
| Framework adherence | 88 | C (B12c) | 86 of 98 phase 1 rule checks passed (gate0 46/51, emoat 40/47); F11 excluded as a rule file gap |
| Peer utilisation | 81.8 | D (B12d) | 9 of 11 transcripts mined substantively |
| **Overall** | **64** | | Minimum of the four. Band 60 to 74. |

## ACCEPTANCE RATES AND COUNTS

| Verifier | Model | Status | Acceptance | CRITICAL | MAJOR | MINOR | Rework triggered |
|---|---|---|---|---|---|---|---|
| A — numerical accuracy | claude-haiku-4-5 | complete (invocation 2) | 96.9 | 0 | 0 | 3 | false |
| B — red flags / adversarial | claude-opus-4-8 | complete | 64 | 2 | 16 | 4 | false |
| C — framework adherence | claude-opus-4-8 | complete (phase 1 scope) | 88 | 0 | 1 | 12 | false |
| D — peer utilisation | claude-sonnet-5 | complete | 82 | 0 | 2 | 3 | false |

**Verifier A, invocation note.** The first invocation resolved relative paths
against the wrong checkout of this repository, found only one stale file, and
returned seven CRITICAL "ANCHOR NOT FOUND" findings with acceptance_rate 0. Every
one was a path failure, not a source fidelity failure. Per the standing Verifier A
rule the stage was re-invoked once with absolute paths. Invocation 2 supersedes
invocation 1 and is the block of record. The event is logged in
verifier-disagreement-log.md.

**Verifier C, valuation half: PENDING PHASE 3.** B10 and B11 do not exist for this
run. No Section 1B layer, Master Prompt Role 1 or FTTCP file was read. Verifier C
rules 4, 6, 7, 9, 11 and 12 were not evaluated. The expectation ledger and the
business understanding narrative are both recorded PENDING PHASE 3 in the same
block. Absence is not a REWORK trigger in phase 1.

**REWORK check.** Verifier A CRITICAL count 0. Lowest acceptance rate 64
(Verifier B), floor 60. No REWORK.

---

## CRITICAL (2)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| C1 | B | Routed to B08 governance. AGM notice p.27 item 2; AR p.39 | Narayan Vithal Karbhase is a director of Vishkul Enterprises Private Limited, the holding company that borrowed Rs1,000 lakh from TAAL Tech in FY26, and was appointed to TAAL Tech's Audit Committee with effect from 4 August 2025, the committee whose stated functions include approval of related party transactions. No document discloses the conflict or records a recusal. |
| C2 | B | Routed to B08 governance. AGM notice p.6, p.22; Note 37(B) p.98; p.40; Note 47 p.104 | Muralidhar Chitteti Reddy is proposed as an INDEPENDENT director with a Section 149(6) declaration, while Note 37(B) of the audited standalone statements records sitting fees paid to him as a Non Whole Time Director of Rs0.80 lakh in FY26 and Rs1.26 lakh in FY25, attributed by the governance report to TAAL Tech India Pvt Ltd, amalgamated into the company with appointed date 1 April 2023. The explanatory statement discloses none of it. |

---

## MAJOR (19)

### Verifier B — missed by stage 5 or stage 6 (5)

| # | Location anchor | Finding |
|---|---|---|
| M1 | B05 silence record. AR Note 25 Other income; Q4FY26 p.17 cash flow; Q4FY26 p.14 P&L | Rs1,204.05 lakh unrealised mark to market gain is 21.2% of consolidated PAT and its Rs649.52 lakh increase is 84% of the entire consolidated PBT increase; the MD&A never mentions it. The single largest earnings quality omission from the silence record. |
| M2 | B05 silence record / B06 margin benchmark. AR AOC-1 p.162; Note 37(B) p.98; Q4FY26 p.14 | The margin pools in India because the US subsidiary bills the parent Rs4,734.48 lakh, 88.5% of its own turnover, at a 5.68% net margin while the parent earns 28.3%. Rs4,878.76 lakh of intra group billing eliminates on consolidation. No transfer pricing risk is named anywhere. B06 calls the margin mechanism the single most important open item for this run without reaching the disclosure that explains most of it. |
| M3 | B05 silence record. AR Note 36 p.97; CARO clause vii(b) p.61 | Rs938.46 lakh contingent income tax liability, 16.5% of consolidated PAT, at CIT(Appeals) for AY2016-17 and AY2020-21, absent from both the MD&A and the Board's Report. |
| M4 | B05. Q3FY26 results p.4 notes 2-3; AR Notes 48-49 p.104 | Rs371.05 lakh customer claim provision reversed into profit and netted against a Rs333.02 lakh labour code charge to a single Rs38.03 lakh exceptional item; the underlying customer claim is disclosed nowhere else, in a year receivables rose 34.7%. |
| M5 | B05 silence record. AR Annexure A p.49 versus MD&A p.37 | R&D recurring expenditure Rs37.55 lakh, 0.20% of revenue, and "efforts made towards technology absorption: NA", for a company whose MD&A opens by calling itself an ER&D company providing high value engineering support. |

### Verifier B — pipeline flags not supported (2)

| # | Location anchor | Finding |
|---|---|---|
| M6 | B06 margin benchmark. TATAELXSI Apr 2026 transcript line 352 | OVERSTATED. B06 omits the Tata Elxsi CFO's statement, on the same transcript page as the quote used, that 27% to 28% is the company's original margin band it is working to return to. A band previously held, not one never reached. This materially weakens B06's conclusion that TAAL Tech's 27.8% margin is anomalous, and that conclusion feeds the valuation stage. The omission runs one way, against the company. |
| M7 | B06 Part 1 Q4, Part 4, analyst note | OVERSTATED. B06 concludes TAAL Tech's 24.05% single customer concentration is modest by comparing it to Onward's 87% to 88% top 25 aggregate. Not a comparable benchmark; Onward's single largest customer share is not disclosed in any of its four transcripts. The reframe is hedged once then repeated flatly twice. |

### Verifier B — out of scope, routed to other stages (9)

| # | Routed to | Location anchor | Finding |
|---|---|---|---|
| M8 | B02 | AR Note 37(B) p.98; Q4FY26 p.8; Note 41(d) | Standalone CFO of Rs2,885.27 lakh is held up by a Rs1,396.81 lakh increase in the payable to the company's own US subsidiary (Rs603.70 lakh to Rs2,000.51 lakh, 50 days to 154 days). It eliminates on consolidation; this is why consolidated CFO is Rs1,874.29 lakh. Note 41(d) then presents the standalone cash flow as the consolidated one. |
| M9 | B02 | Q4FY26 p.14; note 3 p.15 | Q4 FY26 consolidated effective tax rate 16.3% against 26.3% in Q4 FY25, inside the quarter that note 3 states is a balancing figure. No note explains it. |
| M10 | B03 | AR p.57 and consolidated audit report; Q3 FY26 limited review reports | TLB & Co was appointed statutory auditor on 10 February 2026 to fill a casual vacancy and signed both Q3 FY26 limited review reports dated the same day. Both FY26 audit reports then declare there are no key audit matters to communicate. Member approval of the casual vacancy appointment is not evidenced anywhere and the secretarial audit does not list the auditor change among the year's events. |
| M11 | B03 | AR AOC-1 p.162; audit report; Q3 FY26 review report | 28.4% of consolidated FY26 revenue (Rs5,611.58 lakh) is audited solely by other auditors; TAAL Tech UK's statements are unaudited and management furnished; in Q3 FY26 the auditor declared entities carrying 30.7% of consolidated quarterly revenue not material to the group on management prepared unaudited results. |
| M12 | B08 | AR p.47; Q4FY26 note 7 p.15; audit reports p.4 and p.13 | The Regulation 17(8) MD/CFO certificate is dated 19 May 2026, seven days before the audit committee and board approved the FY26 accounts on 26 May 2026 and before both audit reports of the same date. |
| M13 | B02 / B08 | CARO 3(iii)(c); AR Note 37(B) and 37(C) p.98 | CARO 3(iii)(c) asserts principal repayments are regular as per stipulation on a loan whose opening balance was nil and whose full Rs1,000.00 lakh remained outstanding at year end. Note 37(C) states related party balances are interest free except for borrowings while Note 37(B) books Rs98.55 lakh of interest on that loan. |
| M14 | B08 | AR governance report; Taneja Aerospace board records | Three of the four independent directors also sit as independent directors of Taneja Aerospace and Aviation Limited, where Salil Taneja is Promoter-NED; two were appointed there on 8 August 2025, four days after taking committee chairs at TAAL Tech. |
| M15 | B08 | AR p.40 governance remuneration table; Note 37 footnote p.98 | The corporate governance remuneration table shows a Rs164.00 lakh commission to the Managing Director; the Note 37 footnote states the Company has not paid any commission to managerial personnel, and the policy paragraph on the same page names only salary, perquisites and allowances. |
| M16 | B05 severity extension | AR Note 41 p.155-156 | Extension to the Note 41 finding B05 caught: PAT in the Summarised Consolidated table is overstated 77.6% (Rs10,071.52 lakh against Rs5,671.50 lakh), the summarised consolidated balance sheet is the standalone one, and Note 41(a) lists the parent as its own subsidiary. |

### Verifier C (1)

| # | Location anchor | Finding |
|---|---|---|
| M17 | B01-gate0.yaml history_downgrade / 01-gate0.md CLASSIFICATION | history_downgrade set true on a business mix comparability concern; the field's only rule trigger is a 3 to 4 year history and TAALTECH has 10. Classification correctly stayed GOOD, so the boolean contradicts the classification and risks an unauthorised downstream one tier drop. Recomputed: history_downgrade: false; the comparability concern belongs in flags[] and data_notes, where it already also sits. |

### Verifier D (2)

| # | Location anchor | Finding |
|---|---|---|
| M18 | B06 Q6 and Part 5 cross peer hypothesis. CYIENT TAO Digital call PAGE 4; CYIENT Q1 FY27 call PAGE 5 | B06 states Cyient's TAO Digital deal reframes the ER&D TAM to "$2-3 trillion", citing the TAO Digital call p.3-4 and the Cyient Q1 FY27 call p.5. Neither transcript supports the range: the TAO Digital call states an estimated "$2 trillion market" (a single figure, not a range) and the Q1 FY27 call implies roughly $1.6 trillion to $2.0 trillion ("20 times" an $80bn to $100bn base). No source states $3 trillion at either end. |
| M19 | B06 THE MARGIN BENCHMARK section. ONWARDTEC Q2 FY26 (Oct 2025 transcript) PAGE 10 | B06 attributes the analyst quote "our peers, I believe, are somewhere around in the range of 20%" to the ONWARDTEC Q3 FY26 call (Jan 2026 transcript) p.11. The quote does not appear anywhere in that transcript. It is genuinely said in the ONWARDTEC Q2 FY26 call (Oct 2025 transcript), PAGE 10. Wrong quarter misattribution of a real and material quote. |

---

## MINOR (22)

### Verifier A (3)

| # | Location anchor | Finding | source_fidelity |
|---|---|---|---|
| m1 | 01-gate0.md / 02-notes-pass1.md (LBF-1) | Claimed Other Income Rs19.40cr (FY2026). Source truth: audited Consolidated Note 25 Rs19.0272cr (Rs1,902.72 lakh); screener figure Rs19.4cr. Discrepancy Rs0.37cr or 1.9%. Screener basis undefined; the audited source is authoritative. 02-notes-pass1 already flags this delta. Does not alter any verdict conclusion. | true |
| m2 | 06-peers.md (multiple tables) | Peer revenue and margin figures (for example Tata Elxsi 3.2% QoQ Q3 FY26) cited from peer concalls; peer transcripts are Verifier D's scope, not this audit's extraction set. All peer figures correctly attributed to concall sources. Coverage gap by design. No reporting error. | false |
| m3 | 01-gate0.md Block F (moat sub test M6) | R&D expense Rs37.55 lakh (Rs0.376cr) FY2026, claimed source AR p.49 Conservation of Energy annexure; not independently re-derived in this audit. Immaterial in quantum (0.19% of revenue) and consistent with the Companies Act mandatory note. | false |

### Verifier B (4)

| # | Location anchor | Finding |
|---|---|---|
| m4 | B05 (PARTIALLY CAUGHT). AR Note 42 p.102 / p.157 | Beyond the copy paste B05 found, the major customers note's own table sums to Rs6,470.22 lakh against a stated Rs5,734.36 lakh, asserts both customers exceed 10% while showing Customer-2 at 9.98%, and the consolidated version applies standalone based percentages. |
| m5 | B05 silence record (PARTIALLY CAUGHT). AR Note 7 | The Rs14,432.21 lakh securities book, Rs10,733.83 lakh of it debentures and 56.6% of standalone assets, has no silence record row; B05 cites its size only as corrigendum context. |
| m6 | B05 / B06 (PARTIALLY CAUGHT). AR p.37 Key Financial Ratios; Q4FY26 p.14 | Neither report flags that the MD&A's "Operating Profit Margin 37.66% rising from 36.00%" is PBT over revenue including Rs1,902.72 lakh of other income, while the actual operating margin FELL from 28.34% to 27.84%. |
| m7 | Routed to B03 / B08 | Ten further anchored internal contradictions: auditor firm registration 106505S versus 016505S; "quarter ended December 30, 2024" and "six months" inside a nine month review; secretarial audit promising observations and listing none; one practising company secretary holding four roles; AOC-1 versus audit report on UK subsidiary assets; two current ratios moving in opposite directions; "Dividend Payment date: Not Applicable" against Rs2,025.62 lakh paid; a "Chairman & Whole Time Director" signature; a CSR annexure naming no project with spend equal to obligation to the rupee and zero committee meetings; AGM Item 9 described as both Ordinary and Special resolution. |

### Verifier C (12)

| # | Location anchor | Finding | Recomputed |
|---|---|---|---|
| m8 | 01-gate0.md Block A preamble | ROCE denominator taken as Total Assets minus Other Liabilities instead of the mandated Total Assets minus Current Liabilities, under a formula heading that says do not substitute. | FY2026 22.62% versus 22.54% reported; A1/A2 hold with wide margin; no block score change demonstrable |
| m9 | 01-gate0.md Block B, B2 | FCF positive proportion computed over 8 computable years (100%) rather than the 10 available years; FY2017 and FY2021 excluded from the denominator. Operating rule 5 scores unavailable data 0. | 8/10 = 80% gives B2 = 4; Block B 13; core 69; grand total 80; classification unchanged GOOD |
| m10 | 01-gate0.md FCF table, FY2026 row | FY2026 FCF shown as 18.62; 18.74 minus 0.13 = 18.61. | cumulative FCF 181.15; B3 = 0.7053; no band change |
| m11 | 01-gate0.md Block F, M11 | M11 = 5 rests on a 0.44pp gap (7.45% versus 7.01%) whose FY2020 and FY2023 revenue endpoints are never shown, so the test cannot be re-derived. The selling expense leg substituted a 3 year average comparison for the rule's "declining". | if M11 = 0: moat_score 6, moats_confirmed 1, moat_class THIN; classification still GOOD |
| m12 | 07-emoat.md Section 3 completionist recount / B07 evidence_mix | States 5 documented items but enumerates 4; the fifth exists only by counting the same actuarial attrition assumption twice (standalone p.94 and consolidated p.146). | documented = 4; guard threshold is 12, no consequence |
| m13 | 07-emoat.md Family G, G1 | G1 scored 0 citing an injected run constraint present in neither rule file, though debt free status and internally funded capex are on the category's own list. | even a raw 2 x 1.0 gives em_score 6; band NONE holds against the 12 threshold |
| m14 | 07-emoat.md optionality register rows 3 and 5 | Window column reads "unclear, no signal currently" on two of seven rows. Two watch items enter the monitoring checklist with no review date. | (none stated) |
| m15 | 07-emoat.md optionality register rows 4 and 6 | H3 and F1 rows registered although both categories scored 1.0 on documented evidence. No double credit occurs, since register items are never scored. | (none stated) |
| m16 | B07-emoat.yaml catalysts_12m entries 3 and 5 | evidence_type "documented if it appears" is a conditional, not a tier. This field feeds Pillar 3 catalyst proximity downstream. | (none stated) |
| m17 | B07-emoat.yaml evidence_mix | inference: 4 is never enumerated in the report, so the count is untraceable. No scoring consequence: no inference item was scored, so the 0.5x multiplier is nowhere in play. | (none stated) |
| m18 | B07-emoat.yaml analyst_note | "22 of 23 rows return NO EVIDENCE FOUND or the reverse" contradicts the body and the recount line, which both give 20 of 23. Cosmetic. | 20 of 23 |
| m19 | prompts/07-emerging-moat-pipeline.md section 6D | FRAMEWORK GAP, not a stage defect: the standard matrix for combined classification names its eight output labels but defines no cells mapping backward class against forward class to a label. The stage's GOOD plus NONE giving GOOD is reasoned but not independently re-derivable. Excluded from the acceptance denominator. FOR OPERATOR: framework amendment candidate. | (none stated) |

### Verifier D (3)

| # | Location anchor | Finding |
|---|---|---|
| m20 | Multiple B06 citations: TATAELXSI Apr 2026 and Jan 2026, CYIENT Apr 2026 | B06 mixes the extraction's PAGE marker numbering with the transcripts' internal printed "Page X of Y" numbering inconsistently within the same report, producing citations off by one and occasionally two pages. Every quote's content is genuine and present in the named file. |
| m21 | B06 Q1 sector demand section, TATAELXSI Q1 FY27 quote. Jul 2026 transcript PAGE 5 and PAGE 11 | B06 places "soft" in quotation marks as a direct Tata Elxsi quote describing Germany. The word does not appear in the Jul 2026 transcript; management says "softness in Germany" twice. Substance accurate, quotation mark precision is not. |
| m22 | B06 Part 3 coverage map, CYIENT-Concall_Jun_2026_2 row. PAGE 4 | The UNUSED classification is justified on content, but the file contains an AI and data centre power demand market sizing passage that would have reinforced B06's own cross peer hypothesis about AI infrastructure adjacent demand clustering. |

---

## VERIFIER D SUPPORTING RECORD

| Item | Value |
|---|---|
| Peers audited | 11 |
| Substantive confirmed | 9 |
| Substantive unsupported | none |
| Claims all addressed | true |
| Questions worked | 6 of 6; 0 restated only |
| Verdict discipline fails | none. Two or more independent anchors on every VERIFIED verdict; no upgrade from silence anywhere in the report. |
| Unused but relevant | CYIENT-Concall_Jun_2026_Transcript_2 (Semiconductor Strategic Financing, 26-May-2026), PAGE 4: AI and data centre power demand share rising from 2% (2025) to 8% (2030), framing the entire fundraise around AI infrastructure capex. |

## VERIFIER B SUPPORTING RECORD

| Item | Value |
|---|---|
| Independent flags found | 34 (18 in scope for B05/B06, 16 routed to B02/B03/B08) |
| Caught | 10 |
| Partially caught | 3 |
| Missed | 5 |
| Promise delivery spot checks | 3 checked, 3 confirmed, 0 wrong |
| Peer quote spot checks | 14 checked, 13 confirmed, 1 overstated |
| Credibility grade | Concur. C is right. With no calls, no presentation and zero numeric guidance anywhere in 164 pages plus three results filings, independently re-searched and confirmed, C is the correct no concall floor and B05's reasoning is sound. If the two CRITICAL governance items are confirmed, the question moves from communication opacity to disclosure integrity, which is stage 8's grade to set, not stage 5's. |

## VERIFIER C SUPPORTING RECORD

| Item | Value |
|---|---|
| Gate 0 rules checked | 51 (46 passed) |
| Emerging Moat rules checked | 47 (40 passed) |
| Valuation rules checked | 0. PENDING PHASE 3. |
| Expectation ledger | PENDING PHASE 3. Stage 11 artifact, not in phase 1 scope. |
| Business understanding narrative | Recorded PENDING PHASE 3 at verifier time. Stage 13 artifact, produced in this synthesis. |
| Stage 7 categories 21 and 22 | present: true; cat21_score 0; cat22_score 0; both legs rule applied; rework false |
| Recomputed decision | Concur: Gate 0 GOOD and Emerging Moat NONE hold under every recomputation above. |
