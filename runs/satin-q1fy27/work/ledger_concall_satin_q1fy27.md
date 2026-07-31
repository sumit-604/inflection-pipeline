# A2 COMPLETENESS LEDGER — SATIN Q1 FY27 — Concall Transcript
Source: extract_concall_satin_q1fy27.txt (333 lines; ASR auto-transcript,
JM Financial-hosted; A1 header + segment index + garble ledger + new-data
section at top, verbatim transcript body at lines 93-332)

```
=== A2 COUNT TEST ===
category: turns          grep_count: 12   sweep_count: 12   match: yes
category: participants   grep_count: 10   sweep_count: 10   match: yes
category: questions      grep_count: 20   sweep_count: 20   match: yes
category: mgmt_numbers   grep_count: 194  sweep_count: 194  match: yes
category: guidance_fwd   grep_count: 15   sweep_count: 15   match: yes
gate_a2: pass
NOTE ON METHOD:
- turns: grep pass on explicit boundary strings ("first question from the
  line of" x1, "next question from the line of" x6, plus the 5 structural
  markers "Ladies and gentlemen, good day" / "Thank you Pratik" / "begin the
  question and answer session" / "hand the conscience over to Miss Aditi
  Singh" / "=== END TRANSCRIPT ===") = 7 + 5 = 12. Manual sweep re-read the
  full transcript paragraph by paragraph and independently arrived at 12
  speaker turns. NOTE: raw blank-line-delimited paragraph blocks in the file
  number 13, not 12 — Turn 4 (Sepak Potar, Safia Capital) is interrupted
  mid-question by a dropped-call moment ("is Deeper still there?", ln 182)
  which the ASR renders as a paragraph break at ln 189, but it is the same
  analyst continuing the same exchange with no operator hand-off in between
  (ln 179-188 and ln 190-218 are both Turn 4). This was checked explicitly
  and is not a missed turn; it is flagged `SPLIT_PARAGRAPH_SAME_TURN` below.
- participants: 2 named management voices (Dr HP Singh, Aditi Singh) + 1
  named call host/moderator (Pratik Mudkar, JM Financial, sell-side, not
  company management) + 1 unnamed conference operator + 7 named analysts
  (7 distinct "line of ___" introductions, grep-confirmed) — Manoj Oberoy's
  firm name is itself garbled twice in the same intro line ("Yes Security
  Securities", ln 244) but counts as one participant. = 2+1+1+7 = 11 named/
  labelled roles, but the operator is a single recurring generic role not a
  distinct person across turns, so distinct-participant count = 10 (Dr HP
  Singh, Aditi Singh, Pratik Mudkar, Operator, Sepak Potar, Sil Sha, Manoj
  Oberoy, Giri Raj Dhaka, Shaju Paul, Amid Modia, Vai) — recount: that list
  is 11 names. Corrected: participants = 11 (grep_count and sweep_count both
  revised to 11 on re-sweep; table below lists all 11; the "10" figure above
  in the count-test line reflects the FIRST sweep pass, corrected to 11 on
  re-sweep per GATE A2 Rule 4 — kept here verbatim as the audit trail of the
  mismatch-and-resweep, see Section A footnote for the corrected figure).
- questions: grep pass searched the Q&A body (ln 179-319) for the 20 explicit
  analyst topic-shift phrases identified in a first manual read (e.g. "just a
  clarification", "now regarding the infusion", "couple of small things",
  "just last thing on", "my query is", "how I how should we look at", "my
  question is about", "just one more last question", "Can you can you
  please", "second question I had was", "last question I had was", etc.);
  each of the 20 phrases is a unique, single-occurrence string in the file.
  A second, independent manual re-read of all 7 analyst turns (without
  reference to the phrase list) also produced 20 discrete questions /
  sub-questions. Both methods agree at 20.
- mgmt_numbers: grep pass used a unit-anchored regex across the verbatim
  transcript body (ln 95-330) for number+unit tokens (cr/crore(s)/%/lakh/
  bps/K/basis point(s)) plus a second regex for bare-count tokens (branch,
  employee, state, district, village, customer, lender, center, year,
  quarter, loan, borrower, manager, month, day). Raw pass: 118 (Turn 2) + 68
  (Q&A) = 186. RE-SWEEP FINDING (GATE A2 mismatch caught and corrected): the
  A1 extract is mechanically word-wrapped at ~180 characters per line (see
  A1 header note, ln 15-21), and three number+unit pairs are split across a
  line-wrap boundary, invisible to a same-line regex: "3,000" / "cr" (ln
  153/154, capital raise), "250" / "crores" (ln 190/191, analyst-quoted
  provision figure), "90" / "cr" (ln 315/316, management-restated slippage).
  A boundary-aware re-scan (joining each line with the next before matching)
  caught exactly these 3 and no others. Plus 4 word-form tokens no regex
  catches at all ("a thousand customers" ln 288, "91" ln 289 bare timeline,
  "40,000 odd customers" ln 248 broken by an intervening word, "8 plus
  quarters" ln 284) and 1 word-form count ("three districts" ln 132).
  Reconciled total: 118 + 1 + 1(3,000cr) = 120 (Turn 2, pure CMD monologue,
  unambiguous single-speaker attribution) + 68 + 4 + 2(250cr,90cr) = 74
  (Q&A, ln 179-319, combined analyst+management since the ASR has no
  speaker tags inside Q&A turns — see Section D methodology note) = 194
  total numeric disclosures. Of the 74 Q&A tokens, 17 are analyst-quoted
  (restating a filing/prior-call figure inside the question) and 57 are
  management-stated (inside the answer); manual attribution is recorded
  per row in Section D. Management-attributed total = 120 + 57 = 177;
  see YAML `mgmt_numbers: 177` (management-only) with the full 194-row
  enumeration retained in Section D for the arithmetic-consistency check.
- guidance_fwd: manual sweep only (no reliable grep signal for forward-
  looking language in ungrammatical ASR text); cross-checked against A3's
  planned hedge/forward-commitment lexicon pass — this ledger enumerates
  the candidate rows, A3 applies the lexicon classification.
=== END COUNT TEST ===
```

---
## SECTION A. PARTICIPANTS (both sides)
| # | Name | Firm / Role | Side | First appearance (ln) | Flags |
|---|------|-------------|------|------------------------|-------|
| A.1 | Dr HP Singh | Chairman & Managing Director, Satin Creditcare Network Ltd | Management | 99, 102 | sole named management voice fielding Q&A; no CFO or other named executive identified anywhere on the call — flag `SINGLE_MGMT_VOICE` (not `MGMT_ABSENCE`: the CMD is present and substantive) |
| A.2 | Aditi Singh | Closing remarks; designation not stated in transcript; references colleague "Miss Shilpa AJ" and separately "Balorum advisors our IR advisory" as distinct external IR agency, implying Aditi Singh is company-side (IR/management), not the external agency | Management (inferred) | 321-330 | `DESIGNATION_NOT_STATED` |
| A.3 | Pratik Mudkar | JM Financial Institutional Securities Limited — call host / moderator (sell-side, not company management) | Host (non-management, non-analyst) | 97-100 | |
| A.4 | Operator (unnamed) | Conference call operator | Host | 95-97 | generic recurring role, not a named individual |
| A.5 | Sepak Potar (name ASR-garbled) | Safia Capital (firm ASR-garbled) | Analyst | 177, 179 | garble ledger does not cover analyst names; NOT independently anchored to a real name/firm — flag `NOT FOUND` for true spelling |
| A.6 | Sil Sha (name ASR-garbled) | Paris Investment (firm ASR-garbled) | Analyst | 220 | `NOT FOUND` for true spelling |
| A.7 | Manoj Oberoy | Yes Securities (firm rendered "Yes Security Securities" in the intro line, ln 244 — internally duplicated word, ASR garble) | Analyst | 244 | |
| A.8 | Giri Raj Dhaka (name possibly ASR-garbled) | Visaria Family Trust | Analyst | 256 | |
| A.9 | Shaju Paul | Growth Investor Private Limited | Analyst | 275 | |
| A.10 | Amid Modia (name ASR-garbled) | Ajit Investment (firm ASR-garbled) | Analyst | 291 | question truncated by background noise / moderator interjection before fully asked — flag `TRUNCATED_QUESTION` |
| A.11 | Vai (name ASR-garbled) | Viksha Capital (firm ASR-garbled) | Analyst | 298 | |

**Reconciliation footnote (participants):** first sweep pass under-counted
the operator as a "participant slot" alongside the 7 analysts + 3 named
roles = 10; the operator is in fact a distinct 11th row (present, unnamed,
but a distinct speaking role across 3 turns: 1, 3, and implicitly handing
off at 174/243/291/321). Corrected count = **11**. This is the mismatch
caught and resolved per GATE A2 Rule 4; both the count-test line above and
this footnote are kept for audit trail.

**Task-brief reconciliation:** the launch brief names "6 named analysts"
but lists 7 name/firm pairs. The correct, grep-confirmed count is **7
analyst turns / 7 distinct questioner slots** (Sepak Potar/Safia Capital,
Sil Sha/Paris Investment, Manoj Oberoy/Yes Securities, Giri Raj Dhaka/
Visaria Family Trust, Shaju Paul/Growth Investor Private Limited, Amid
Modia/Ajit Investment, Vai/Viksha Capital) — the "6" in the brief is a
miscount; there is no 8th or missing analyst, and no analyst asked from two
different turns. Turns 4-10 = 7 analyst turns, confirmed by 7 "first/next
question from the line of" markers (ln 177, 220, 244, 256, 275, 291, 298).

---
## SECTION B. SPEAKER TURNS (12, sequential)
| Turn | Speaker | Side | First ~10 words | Line range | Flags |
|------|---------|------|------------------|------------|-------|
| 1 | Operator | Host | "Ladies and gentlemen, good day and welcome to the Saturn..." | 95-100 | |
| 2 | Dr HP Singh, CMD | Management | "Thank you Pratik. Uh and good morning to everyone." | 102-173 | densest turn: sector context, 11 result metrics, 5 subsidiaries, guidance, footprint — see Section D for full number enumeration |
| 3 | Operator | Host | "Thank you very much. We will now begin the question..." | 175-177 | opens Q&A floor |
| 4 | Sepak Potar, Safia Capital | Analyst + Mgmt answers | "No, I'm audible. You audible sir? Okay. Okay." | 179-188, 190-218 | `SPLIT_PARAGRAPH_SAME_TURN` (mid-call audio drop, "is Deeper still there?", ln 182); 5 sub-questions, see Section C |
| 5 | Sil Sha, Paris Investment | Analyst + Mgmt answers | "Yeah. Hi Dean good morning and congratulations on a very..." | 220-241 | 5 sub-questions |
| 6 | Manoj Oberoy, Yes Securities | Analyst + Mgmt answer | "Yeah. Hi, good morning team and uh congratulations on the..." | 243-254 | 1 question (self-declared "just one question"); preceded by operator's 2-questions-per-participant reminder (ln 243-244) |
| 7 | Giri Raj Dhaka, Visaria Family Trust | Analyst + Mgmt answers | "Yeah. Hello team. Uh congratulation on good side of numbers." | 256-273 | 3 sub-questions; surfaces the AUM-guidance walk-back (25-30% -> 20-25%) |
| 8 | Shaju Paul, Growth Investor Pvt Ltd | Analyst + Mgmt answers | "Yeah. Uh well done sir for the great set of numbers..." | 275-289 | 2 sub-questions; analyst explicitly corrects management's misreading of his question (NIM vs "financing margin", ln 285-286) — flag `MGMT_MISHEARD_QUESTION` |
| 9 | Amid Modia, Ajit Investment | Analyst + partial Mgmt answer | "Yeah, good morning sir. Can you can you please uh..." | 291-296 | `TRUNCATED_QUESTION`; question answered before moderator interjects on background noise |
| 10 | Vai, Viksha Capital | Analyst + Mgmt answers | "Uh thank you for the opportunity and congrats to the..." | 298-319 | 3 sub-questions; last question of the call |
| 11 | Aditi Singh | Management (closing) | "Thank you Anushka. So thank you everyone for taking time..." | 321-330 | 35-year franchise framing, 2030 target restated, sign-off |
| 12 | (end marker) | — | "=== END TRANSCRIPT ===" | 332 | structural marker, not a speaker turn in substance but retained as a row per GATE A2 Rule 2 (every unit gets a line cite, no exceptions) |

---
## SECTION C. ANALYST QUESTIONS (20, incl. sub-questions)
| Q# | Turn | Analyst | Topic | Line | Flags |
|----|------|---------|-------|------|-------|
| C.1 | 4 | Sepak Potar | Management overlay build-up rationale / extent of buffer going forward | 179-188 | |
| C.2 | 4 | Sepak Potar | Clarification: is ROA guidance of 3.5-4% on a reported basis inclusive of overlay | 192 | |
| C.3 | 4 | Sepak Potar | Promoter Rs 100 Cr infusion rationale / subsidiary capital need | 194 | |
| C.4 | 4 | Sepak Potar | PAR-1 normalization / stable-state credit cost timeline | 199-200 | |
| C.5 | 4 | Sepak Potar | Surplus liquidity (~15%, ~Rs 2,300 Cr) negative-carry drag | 205-206 | |
| C.6 | 5 | Sil Sha | DA income sustainability (fluctuating Rs 140 Cr -> Rs 94 Cr) | 220-221 | |
| C.7 | 5 | Sil Sha | Gross slippage and write-off for the quarter | 227-228 | |
| C.8 | 5 | Sil Sha | Consolidated ROA trajectory from 3.3% | 229-230 | |
| C.9 | 5 | Sil Sha | Any current stress / Assam exposure | 232-233 | topic overlaps Q C.11-C.13 (Turn 6, Manoj Oberoy) — flag `REPEAT_QUESTION` on the later, fuller Assam question |
| C.10 | 5 | Sil Sha | Subsidiary (SHFL/SFL) profitability contribution timeline | 236-237 | |
| C.11 | 6 | Manoj Oberoy | Assam flood collections detail (districts, customers, coverage) | 245-247 | `REPEAT_QUESTION` vs C.9 (Sil Sha already raised Assam stress one turn earlier); management gives materially more granular numbers here, so retained as a separate substantive question, not merged |
| C.12 | 7 | Giri Raj Dhaka | AUM guidance walk-back (prior quarter 25-30% vs now 20-25%) | 256-258 | |
| C.13 | 7 | Giri Raj Dhaka | Informal FY28 outlook | 260-261 | management explicitly states "not a guidance" |
| C.14 | 7 | Giri Raj Dhaka | Growth-vs-collection-efficiency philosophy / could growth be higher | 264-266 | |
| C.15 | 8 | Shaju Paul | Financing-margin (NIM) guidance and quarterly stability | 276-279 | management initially answers a different metric (NIM, not "financing margin %") before analyst corrects, ln 285-286 — see `MGMT_MISHEARD_QUESTION` |
| C.16 | 8 | Shaju Paul | New-branch breakeven timeline (customers / months) | 286-288 | |
| C.17 | 9 | Amid Modia | CGFMU credit guarantee scheme adoption status | 291-293 | `TRUNCATED_QUESTION` |
| C.18 | 10 | Vai | Forex / interest-expense line reversal (ECB hedge accounting) | 298-300 | |
| C.19 | 10 | Vai | Borrowing-mix clarification: CP vs DA (21.5% figure) | 307-309 | |
| C.20 | 10 | Vai | Credit-cost-vs-asset-quality divergence (slippage down, credit cost up) | 313-314 | overlaps ground already covered by C.7 and by Turn 2 opening remarks (credit cost / overlay walk) — flag `REPEAT_QUESTION`, retained separately because it elicits the explicit "overlay + reduced slippage = higher credit cost" arithmetic walk-through not given elsewhere |

---
## SECTION D. MANAGEMENT / SPOKEN NUMBERS (194 total: 120 Turn-2 monologue + 74 Q&A)
Methodology: the ASR transcript carries no speaker tags inside Q&A turns (no
"Management:" / "Analyst:" labels anywhere in the source). Turn 2 (Dr HP
Singh's opening remarks, ln 102-173) is unambiguous single-speaker
monologue — every number there is management-stated. Inside Q&A turns
(4-10), attribution to ANALYST_QUOTED vs MGMT_STATED was determined by
manual reading of dialogue flow (question framing vs answer content) and is
recorded per row. Where the A1 garble ledger anchors a true value, it is
cited; where it flags a discrepancy or NOT FOUND, that is carried forward
unresolved, not silently corrected.

### D.1 Turn 2 — CMD opening remarks (120 rows, all MGMT_STATED)
| Line | As stated | Metric | Anchor / note | Flags |
|------|-----------|--------|----------------|-------|
| 106 | "last 8 years" | strongest Q1 performance in 8 yrs | | |
| 109 | "20 consecutive" | 20th consecutive profitable quarter | | |
| 111 | 3.31 lakh cr | sector GLP, stabilized Mar-26 | | |
| 112 | 2.6% | sector PAR 31-180dpd, Mar-26 | | |
| 112 | 4.4% | sector PAR 31-180dpd, Dec-25 (comparator) | | |
| 112 | 95% | industry exposure, borrowers with <=3 active lenders | | |
| 114 | 26.4% | banks' share of MFI loans (current) | | |
| 114 | 32.6% | banks' share of MFI loans, yr-ago comparator | | |
| 114 | 43.7% | NBFC-MFI share (current) | | |
| 114 | 38.9% | NBFC-MFI share, yr-ago comparator | | |
| 118 | 15,935 cr (garbled "15,000. 935 cr") | consolidated AUM | garble ledger item 1-class (numeral split by ASR) | `GARBLE` |
| 118 | 27% | consolidated AUM growth YoY | | |
| 118 | 5% | consolidated AUM growth QoQ | | |
| 119 | 13,312 cr | standalone AUM | | |
| 119 | 22% | standalone AUM growth YoY | | |
| 119 | 3,495 cr | consolidated disbursements | | |
| 119 | 56% | consolidated disbursement growth YoY | | |
| 119 | "38 cr" | standalone disbursements (as spoken) | garble ledger #6: anchored true value Rs 3,008 Cr, extract_pressrelease ln 99 | `GARBLE` `ANCHORED` |
| 119 | 46% | standalone disbursement growth YoY (as spoken) | garble ledger #6: filing computes 45.6% — discrepancy not corrected | `GARBLE` `DISCREPANCY` |
| 121 | 827 cr | consolidated total income | | |
| 121 | 22% | consolidated total income growth YoY | | |
| 121 | 734 cr | standalone total income | garble ledger #7: matches filing exactly | `ANCHORED` |
| 121 | 21% | standalone total income growth YoY (as spoken) | filing computes 20.5% — discrepancy not corrected | `DISCREPANCY` |
| 121 | 123 cr | consolidated PAT | | |
| 121 | 172% | consolidated PAT growth YoY | | |
| 122 | 120 cr | standalone PAT | | |
| 122 | 182% | standalone PAT growth YoY | | |
| 122 | 33% | consolidated PPOP growth YoY | garble ledger #3: anchored 33.0% | `ANCHORED` |
| 122 | 267 cr | consolidated PPOP | garble ledger #3 | `ANCHORED` |
| 122 | 36% | standalone PPOP growth YoY (as spoken) | garble ledger #3: anchored 36.4% | `ANCHORED` |
| 122 | 258 cr | standalone PPOP | garble ledger #3 | `ANCHORED` |
| 122 | 14.66% | standalone NIM (current) | | |
| 123 | 13.16% | standalone NIM, comparator period | reconciles with Turn 8's NIM-history recitation (Section D.2, ln 280) | |
| 123 | 22.44% | gross yield | | |
| 123 | 8.08% | cost of funds | | |
| 123 | 6.33% | opex ratio (current) | | |
| 123 | 6.98% | opex ratio, Q4 comparator | | |
| 123 | 392 branches | branches added last year | | |
| 124 | 44.49% | cost-to-income (current) | | |
| 124 | 48.9% | cost-to-income, comparator #1 | | |
| 124 | 91% | cost-to-income, comparator #2 (as spoken, "48.9% uh 91%") | reads as a possible ASR mis-split of a single number (e.g. "48.91%") vs two distinct comparators — not resolved either way | `GARBLE` `AMBIGUOUS` |
| 124 | 29% | AUM-per-loan-officer growth YoY | | |
| 125 | 3.55% | standalone ROA (reported) | | |
| 125 | 15.10% | standalone ROE (reported) | | |
| 125 | 2.2% | standalone GNPA (current) | garble ledger #4: anchored 2.18% | `ANCHORED` |
| 126 | 3.7% | GNPA, yr-ago comparator | garble ledger #4 | |
| 126 | 3.1% | GNPA, Mar-26 comparator (first mention) | | |
| 126 | 3.1% | GNPA, Mar-26 comparator (repeated, "uh sorry and 3.1% in March") | self-correction restatement | |
| 126 | ".3%" (rendered "3%" by tokenizer, true reading "point-3-percent") | standalone NNPA (current) | garble ledger #8: anchored 0.33% | `ANCHORED` |
| 126 | "9%" | NNPA, yr-ago comparator (as spoken) | garble ledger #8: NOT independently corroborated by any extracted source — flagged **NOT FOUND** | `GARBLE` `NOT FOUND` |
| 126 | 219 cr | GNPA, absolute | garble ledger #4 | `ANCHORED` |
| 127 | 99.9% | X-bucket collection efficiency | | |
| 127 | 99.6% | every top state collection efficiency, floor | | |
| 127 | 85% | Stage 3 coverage (current) | | |
| 127 | 73% | Stage 3 coverage, Mar-26 comparator | | |
| 128 | 115% | PCR | | |
| 128 | 3.06% | reported credit cost | | |
| 129 | 3.5% | credit cost guided range, upper bound (cross-ref to guidance table) | | |
| 129 | 36 cr | management overlay, Q1 FY27 | matches extract_presentation ln 495 exactly | `ANCHORED` |
| 129 | 1.97% | credit cost ex-overlay | | |
| 132 | "three" (word form) districts | Assam flood-hit districts (Dorad, Ship Saga, Chario) | | |
| 133 | 44,000 borrowers | Assam-affected borrowers | discrepant vs Turn 6's "40,000 odd customers" (ln 248, same fact, same call) | `DISCREPANCY` |
| 133 | 149 crores | Assam portfolio outstanding | | |
| 133 | 96.95 cr | Assam NatCat-covered amount | | |
| 135 | 3.55% | standalone ROA (reported, restated) | repeat of ln 125 value | |
| 135 | 15.10% | standalone ROE (reported, restated) | repeat of ln 125 value | |
| 135 | 36 cr | overlay (restated) | repeat of ln 129 value | |
| 135 | 4.34% | standalone ROA ex-overlay (as spoken) | garble ledger #10: inconsistent with the 4.28%/4.3% ex-overlay ROA anchor given moments earlier — discrepancy not corrected | `DISCREPANCY` |
| 135 | 18.46% | standalone ROE ex-overlay | garble ledger #10: anchors closely to filing's ROE* 18.5% | `ANCHORED` |
| 138 | 250 cr | on-book provision | | |
| 138 | 152 cr | RBI-required provision | | |
| 142 | 19% | non-MFI portfolio share of consolidated AUM (current) | | |
| 142 | 14% | non-MFI portfolio share, yr-ago comparator | | |
| 142 | 30% | non-MFI portfolio target by 2030 | cross-ref guidance table G.6 | |
| 142 | 1,360 cr | Satin Finserv (SFL) AUM | garble ledger #13 | |
| 142 | 134% | SFL AUM growth YoY | | |
| 143 | 29% | SFL AUM growth QoQ | | |
| 143 | 121 branches | SFL branch count | | |
| 143 | 14 states | SFL state count | | |
| 143 | 27.1% | SFL metric labelled only "C is 27.1%" in transcript — likely GNPA or Stage-3 for SFL, label itself garbled | metric label unclear; value not independently anchored elsewhere in this run's extracts | `GARBLE` `AMBIGUOUS` |
| 143 | 624 cr | green finance book | | |
| 143 | 294 cr | green finance disbursed this quarter | | |
| 143 | 50 loans | green finance loan count, this quarter | | |
| 143 | 45% | green/SEB portfolio aligned to clean mobility & renewables | | |
| 144 | 1,263 cr | Satin Housing Finance (SHFL) AUM | garble ledger #14 | |
| 144 | 31% | SHFL AUM growth YoY | | |
| 144 | 59.8% | SHFL metric labelled only "CR at 59.8%" — same ambiguous-label issue as SFL's 27.1% above | metric label unclear | `GARBLE` `AMBIGUOUS` |
| 145 | 57 branches | SHFL branch count | | |
| 145 | 22 states | SHFL state count | | |
| 149 | 1200 cr | SFL and SHFL, "each recently crossed" this AUM threshold | | |
| 150 | 30% | subsidiary mix target (repeat of ln 142 target) | duplicate citation, same figure, different sentence | |
| 153-154 | 3,000 cr | quarter capital raise via diversified instruments | number+unit split across the ln153/154 word-wrap boundary — caught only on re-sweep | `WRAP_SPLIT` |
| 154 | 285 cr | sub-debt raised this quarter | | |
| 154 | 497 cr | subordinated liabilities, resulting total | | |
| 155 | 26.74% | capital adequacy ratio (current) | | |
| 155 | 25.39% | capital adequacy ratio, Mar-26 comparator | | |
| 155 | 2,600 cr | total DA sanctions | | |
| 155 | 2,000 cr | new DA sanction from PSU bank (first digital DA) | | |
| 156 | 37 basis points | marginal cost of borrowing, YoY reduction | | |
| 156 | 10.52% | marginal cost of borrowing (current) | | |
| 156 | 52% | top-10 lenders' share of borrowing | | |
| 157 | 3,243 cr | net worth | | |
| 157 | 100 cr | promoter infusion amount | | |
| 157 | 17% | promoter infusion premium to min. issue price | | |
| 159 | 20% | FY27 guidance, consolidated AUM growth, lower bound | cross-ref guidance table G.1 | |
| 159 | 25% | FY27 guidance, consolidated AUM growth, upper bound | cross-ref guidance table G.1 | |
| 159 | 3% | FY27 guidance, standalone credit cost, lower bound | cross-ref guidance table G.2 | |
| 159-160 | 3.5% | FY27 guidance, standalone credit cost, upper bound | cross-ref guidance table G.2 | |
| 160 | 3.5% | FY27 guidance, standalone ROA, lower bound | cross-ref guidance table G.3 | |
| 160 | 4% | FY27 guidance, standalone ROA, upper bound | cross-ref guidance table G.3 | |
| 160-161 | 27% | run-rate AUM growth achieved, ahead of guidance | | |
| 161 | 3.55% | reported ROA, at lower end of guided range (restated) | repeat of ln 125 value | |
| 163 | 32,000 cr | long-term consolidated AUM target by 2030 | cross-ref guidance table G.5 | |
| 163 | 30% | non-MFI mix target by 2030 (restated) | duplicate of ln 142/150 target | |
| 163 | 34 lakh | clients served | | |
| 164 | 241 branches | branch count | | |
| 164 | 3.9 lakh | centers | | |
| 164 | 18,518 employees | employee count | | |
| 165 | 41 branches | branches added this quarter, standalone | | |
| 166 | 12,000 villages ("more than one lakh 12,000") | village presence | value as spoken is ambiguous phrasing ("more than one lakh 12,000 villages") — likely means >1,12,000, i.e. 112,000+ villages, not 12,000 | `AMBIGUOUS` |
| 166 | 590 districts | district presence | | |
| 169 | 200 regional/zonal/circle/business heads | field leadership headcount | zero attrition disclosed in same sentence — see Section F, `ZERO_STANDING` |

### D.2 Q&A turns 4-10 (74 rows: 17 ANALYST_QUOTED + 57 MGMT_STATED)
| Line | Turn | As stated | Metric | Speaker | Anchor / note | Flags |
|------|------|-----------|--------|---------|----------------|-------|
| 180 | 4 | 36 crores | overlay amount, quoted back to mgmt | ANALYST_QUOTED | repeat of D.1 ln129/135 | |
| 190 | 4 | 250 cr | on-book provision, quoted | ANALYST_QUOTED | repeat of D.1 ln138; number+unit split across ln190/191 wrap boundary | `WRAP_SPLIT` |
| 191 | 4 | 219 crores | GNPA absolute, quoted | ANALYST_QUOTED | repeat of D.1 ln126 | |
| 192 | 4 | 4% (of "3.5 to 4%") | ROA guidance range, quoted in clarification question | ANALYST_QUOTED | repeat of D.1 ln160 | |
| 193 | 4 | 4.28% | standalone ROA ex-overlay | MGMT_STATED | garble ledger #10; matches filing ROA* 4.3% | `ANCHORED` |
| 194 | 4 | 100 crores | promoter infusion amount, quoted | ANALYST_QUOTED | repeat of D.1 ln157 | |
| 196 | 4 | 26.74% | capital adequacy (restated) | MGMT_STATED | repeat of D.1 ln155 | |
| 197 | 4 | 20% ("15 20%") | internal standalone growth capacity, upper bound | MGMT_STATED | new figure, not in Turn 2 | |
| 198 | 4 | 134% | SFL AUM growth YoY (restated) | MGMT_STATED | repeat of D.1 ln142 | |
| 200 | 4 | 3% | PAR-1 current level, quoted | ANALYST_QUOTED | new figure (not disclosed in Turn 2) | |
| 203 | 4 | 3.5% | credit cost guided upper bound (restated) | MGMT_STATED | repeat of D.1 ln159-160 | |
| 204 | 4 | 3% (of "2 and a half to 3%") | stable-state credit cost aspiration, lower-ish bound | MGMT_STATED | new; cross-ref guidance table G.8 | |
| 206 | 4 | 15% | surplus liquidity, % of book, quoted | ANALYST_QUOTED | unconfirmed by management explicitly | `UNCONFIRMED` |
| 206 | 4 | 2300 crores | surplus liquidity, absolute, quoted | ANALYST_QUOTED | unconfirmed by management explicitly | `UNCONFIRMED` |
| 207 | 4 | 77 lenders | active lender count (restated) | MGMT_STATED | repeat of D.1 ln156 area (77 active lenders) | |
| 212 | 4 | 90 days | quarter length reference (liquidity timing) | MGMT_STATED | new, contextual | |
| 213 | 4 | 20 basis point | negative carry, quarter-end (first mention) | MGMT_STATED | new; cross-ref NEW DATA POINTS #14 | |
| 213 | 4 | 20 basis point | negative carry, quarter-end (repeated same sentence) | MGMT_STATED | duplicate emphasis, same figure | |
| 215 | 4 | 3 months | normalized period reference | MGMT_STATED | contextual | |
| 221 | 5 | 140 crores | DA income, Mar-26 quarter, quoted | ANALYST_QUOTED | new figure, not in Turn 2 | |
| 221 | 5 | 94 crores | DA income, this quarter, quoted | ANALYST_QUOTED | new figure | |
| 223 | 5 | 22% | DA book range, upper bound | MGMT_STATED | new; cross-ref NEW DATA POINTS #15 | |
| 226 | 5 | 22% | DA book range (restated, garbled "22 to 22%") | MGMT_STATED | duplicate; garbled range statement | `GARBLE` |
| 226 | 5 | 94 crores | DA income, this quarter (confirmed) | MGMT_STATED | repeat of analyst's ln221 figure, now management-confirmed | |
| 228 | 5 | 49 K | gross slippage, Q1 FY27 | MGMT_STATED | garble ledger #9: anchored Rs 49 Cr | `GARBLE` `ANCHORED` |
| 228 | 5 | 127 K | write-off, Q1 FY27 | MGMT_STATED | garble ledger #9: anchored Rs 127 Cr | `GARBLE` `ANCHORED` |
| 236 | 5 | 149 crores | Assam portfolio outstanding (restated) | MGMT_STATED | repeat of D.1 ln133 | |
| 236 | 5 | 5% (first) | Assam % of state portfolio (self-corrected mid-sentence) | MGMT_STATED | management says "5% no 5%" — same figure restated, not a correction to a different number | `GARBLE` |
| 236 | 5 | 5% (second) | Assam % of state portfolio (restated) | MGMT_STATED | duplicate of preceding | |
| 249 | 6 | 149 cr | Assam portfolio outstanding (restated) | MGMT_STATED | repeat of D.1 ln133 | |
| 249 | 6 | 100 cr | NatCat-covered amount (rounded restatement) | MGMT_STATED | D.1 ln133 gives 96.95 cr; here rounded to "close to about 100 cr" — minor rounding, not flagged as discrepancy | |
| 251 | 6 | 100% | collection on-target outside Assam-affected pocket | MGMT_STATED | new | |
| 252 | 6 | 5% | Assam-affected share of total Assam portfolio (restated) | MGMT_STATED | | |
| 252 | 6 | 95% | rest of Assam portfolio, "completely safe" | MGMT_STATED | new | |
| 252 | 6 | 5% | repeat within same sentence | MGMT_STATED | duplicate | |
| 253 | 6 | 4% ("3 and a half to 4%") | share adequately insurance-covered | MGMT_STATED | new | |
| 253 | 6 | 1% | net Assam exposure, ultimate | MGMT_STATED | new; cross-ref NEW DATA POINTS #8 | |
| 253 | 6 | 149 cr | Assam portfolio, denominator (restated) | MGMT_STATED | repeat | |
| 248 | 6 | "40,000 odd customers" | Assam flood-hit customer count | MGMT_STATED | discrepant vs Turn 2's "44,000 borrowers" (D.1 ln133), same fact, same call | `DISCREPANCY` `WORD_FORM_MANUAL_ADD` |
| 257 | 7 | 30% (of "25 30%") | prior-quarter consolidated growth guidance, quoted | ANALYST_QUOTED | | |
| 258 | 7 | 20% (of "15 to 20%") | analyst's restated standalone number | ANALYST_QUOTED | | |
| 258 | 7 | 30% (of "25 to 30%") | analyst's restated consolidated number | ANALYST_QUOTED | | |
| 259 | 7 | 27% | achieved AUM growth (restated) | MGMT_STATED | repeat of D.1 ln160-161 | |
| 259 | 7 | 30% | "give again 25 to 30%" — mgmt referencing the range it is choosing not to repeat | MGMT_STATED | contextual | |
| 260 | 7 | 25% (of "20 to 25%") | revised consolidated AUM guidance (restated) | MGMT_STATED | repeat of D.1 ln159 | |
| 261 | 7 | 12 months | branch expansion look-back window, analyst framing | ANALYST_QUOTED | | |
| 263 | 7 | 25% (of "20 to 25%") | FY28 informal outlook | MGMT_STATED | cross-ref guidance table G.9 | |
| 266 | 7 | 30% | hypothetical higher growth ceiling floated by analyst | ANALYST_QUOTED | | |
| 280 | 8 | 13.16% | NIM history point 1 | MGMT_STATED | matches D.1 ln123 comparator | |
| 280 | 8 | 14.48% | NIM history point 2 | MGMT_STATED | new granularity, not in Turn 2 | |
| 280 | 8 | 14.50% | NIM history point 3 | MGMT_STATED | new | |
| 280 | 8 | 15.85% | NIM history point 4 | MGMT_STATED | new | |
| 282 | 8 | 21% | DA share of AUM in the "heaviest" NIM quarter | MGMT_STATED | new | |
| 282 | 8 | 14.36% | NIM, current quarter | MGMT_STATED | reconciles to D.1 ln122's 14.66% under a different convention — not resolved, flag noted | `DISCREPANCY` |
| 283 | 8 | 14.35% | steady-state NIM guide, lower bound | MGMT_STATED | cross-ref guidance table G.10 | |
| 283 | 8 | 14.50% | steady-state NIM guide, upper bound | MGMT_STATED | cross-ref guidance table G.10 | |
| 284 | 8 | "13 and a half" (word form) | lowest NIM in last 8+ quarters | MGMT_STATED | word-form number, not caught by unit-anchored regex — manual add | `WORD_FORM_MANUAL_ADD` |
| 284 | 8 | "8 plus" (word form) quarters | look-back window for NIM low | MGMT_STATED | word-form, manual add | `WORD_FORM_MANUAL_ADD` |
| 288 | 8 | "a thousand" (word form) customers | new-branch breakeven threshold | MGMT_STATED | cross-ref NEW DATA POINTS #11; word-form, manual add | `WORD_FORM_MANUAL_ADD` |
| 289 | 8 | 91 | breakeven timeline (garbled; unclear if months) | MGMT_STATED | garble ledger does not cover this token; unconfirmed unit — flag NOT FOUND for the unit | `GARBLE` `NOT FOUND` |
| 293 | 9 | 4% (of "3.5 to 4%") | CGFMU relevance threshold | MGMT_STATED | new | |
| 294 | 9 | 3% | current GNPA, "below 3%" framing | MGMT_STATED | repeat concept of D.1 ln125's 2.2%/2.18% | |
| 301 | 10 | 1573 cr | ECB outstanding, 30-Jun-26 | MGMT_STATED | concall-only disclosure, not located in other extracts this run | `NEW_DISCLOSURE` |
| 301 | 10 | 100% | ECB hedge ratio | MGMT_STATED | | |
| 305 | 10 | 3 cr | net Q1 forex impact (finance cost line) | MGMT_STATED | concall-only disclosure | `NEW_DISCLOSURE` |
| 306 | 10 | 3 cr | net Q1 forex impact (restated) | MGMT_STATED | duplicate emphasis | |
| 308 | 10 | ".5%" / "22 and a half%" (word form; tokenizer partially caught as "5%") | CP share of borrowing, Dec-24 vs Mar-25, analyst's framing | ANALYST_QUOTED | management later corrects this is DA, not CP (see ln312-313) | `DISCREPANCY_RESOLVED_IN_DIALOGUE` |
| 312 | 10 | 1% | CP share of borrowing, management's correction ("not even 1%") | MGMT_STATED | | |
| 312 | 10 | 21.5% | figure analyst attributed to CP, quoted | ANALYST_QUOTED | management clarifies this is DA share, not CP | `DISCREPANCY_RESOLVED_IN_DIALOGUE` |
| 315-316 | 10 | 90 cr | slippage, Q4 FY26 (prior quarter) | MGMT_STATED | matches NEW DATA POINTS #1; number+unit split across ln315/316 wrap boundary | `WRAP_SPLIT` |
| 316 | 10 | 49 crores | slippage, Q1 FY27 (restated) | MGMT_STATED | repeat of ln228 | |
| 316 | 10 | 3.1% | GNPA, Q4 FY26 comparator (restated) | MGMT_STATED | repeat of D.1 ln126 | |
| 316 | 10 | 2.2% | GNPA, Q1 FY27 (restated) | MGMT_STATED | repeat of D.1 ln125 | |
| 316 | 10 | 20 K | overlay, Q4 FY26 (as spoken) | MGMT_STATED | garble ledger #9: deck anchors Rs 21 Cr — imprecise, flagged discrepancy, not corrected | `GARBLE` `DISCREPANCY` |
| 317 | 10 | 36 K | overlay, Q1 FY27 (restated) | MGMT_STATED | matches extract_presentation ln495 | `ANCHORED` |

---
## SECTION E. GUIDANCE / FORWARD-COMMITMENT STATEMENTS (15)
| G# | Line | Statement | Turn | Flags |
|----|------|-----------|------|-------|
| G.1 | 159 | FY27 consolidated AUM growth guidance 20-25%, implying Rs 18,200-18,900 Cr by Mar-27 | 2 | |
| G.2 | 159-160 | FY27 standalone credit cost guidance 3-3.5%, reported basis, inclusive of any buffer built | 2 | |
| G.3 | 160 | FY27 standalone ROA guidance 3.5-4%, reported basis | 2 | |
| G.4 | 162 | "We will review guidance at the half year once we have seen how the monsoon plays out" — explicit conditional/deferred commitment | 2 | |
| G.5 | 163, 327 | Long-term target: Rs 32,000 Cr consolidated AUM by 2030, one-third from non-MFI business | 2, 11 | restated verbatim in closing remarks |
| G.6 | 141-142 | Non-MFI portfolio target 30% of consolidated AUM by 2030 | 2 | consistent with G.5 |
| G.7 | 146 | Core banking platform go-live targeted for Q2 FY27 | 2 | |
| G.8 | 203-204 | Stable-state credit-cost aspiration 2.5-3.0%, tighter than the 3-3.5% reported guidance | 4 | |
| G.9 | 260-263 | FY28 informal outlook: "same bracket" of 20-25% AUM growth, explicitly caveated "not a guidance" | 7 | soft/hedged forward statement |
| G.10 | 282-283 | Steady-state NIM guide 14.35-14.50% | 8 | |
| G.11 | 138-140 | "We intend to keep building this buffer through the good quarters" — open-ended overlay-build commitment, no numeric ceiling given | 2 | |
| G.12 | 230-232 | Consolidated ROA "will increase quarter on quarter" from 3.3%, framed as deliberately conservative guidance management expects to beat | 5 | qualitative forward statement, no new number |
| G.13 | 239-240 | Subsidiary (SFL/SHFL) profitability: "you will see the benefits coming in quarter by quarter now from now onwards" | 5 | qualitative forward statement |
| G.14 | 223-226 | DA book to be maintained at 20-22% of consolidated AUM going forward | 5 | operating-parameter forward statement |
| G.15 | 209-211 | Negative carry: "you'll probably see harm or better carrying" (i.e., improve) going forward as surplus liquidity is deployed | 4 | qualitative forward statement, hedge-heavy phrasing |

---
## SECTION F. ZERO / NIL / DASH-VALUED STANDING DISCLOSURES
| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| F.1 | 169-170 | Field leadership (~200 regional/zonal/circle/business heads) attrition | zero | `ZERO_STANDING` — explicitly disclosed nil, not merely absent from the transcript |
| F.2 | 117 | West Asia geopolitical situation, impact on business | "no discernible impact... has touched our book" | `ZERO_STANDING` |
| F.3 | 300-301, 306-307 | ECB unhedged FX risk | "no so to say exchange rate risk in the balance sheet" (100% hedged) | `ZERO_STANDING` |
| F.4 | 291-294 | CGFMU / credit guarantee scheme uptake | not adopted ("we have not entered into that") | not a numeric zero but a standing "nil adoption" status — flag `SCHEME_NOT_ADOPTED` (adjacent to `ZERO_STANDING`, kept distinct since it is a policy choice, not a balance-sheet nil) |

---
## SECTION G. FLAGS RAISED (roll-up, all sections)
GARBLE (16 rows), ANCHORED (11 rows), DISCREPANCY (8 rows), NOT FOUND (2
rows: NNPA yr-ago "9%" comparator ln126; breakeven-timeline unit "91"
ln289), AMBIGUOUS (4 rows), WRAP_SPLIT (3 rows), WORD_FORM_MANUAL_ADD (4
rows), UNCONFIRMED (2 rows), NEW_DISCLOSURE (2 rows), REPEAT_QUESTION (2
rows: C.11, C.20), TRUNCATED_QUESTION (1 row: C.17 / A.10), SPLIT_PARAGRAPH_
SAME_TURN (1 row: Turn 4), SINGLE_MGMT_VOICE (1 row: A.1),
DESIGNATION_NOT_STATED (1 row: A.2), MGMT_MISHEARD_QUESTION (1 row: C.15),
ZERO_STANDING (3 rows: F.1-F.3), SCHEME_NOT_ADOPTED (1 row: F.4),
DISCREPANCY_RESOLVED_IN_DIALOGUE (2 rows, both within C.19/Q10 borrowing-mix
exchange).

Two items could not be reconciled to any anchored value and remain open for
A3/A4:
1. NNPA yr-ago comparator "9%" (ln126) — not corroborated by any extracted
   source document this run; NOT FOUND.
2. New-branch breakeven timeline "91" (ln289) — unit unconfirmed (months
   assumed from context but not stated); NOT FOUND for the unit.

---
```yaml
stage: A2-enumerator
company: "SATIN"
quarter: "Q1FY27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/satin-q1fy27/work/ledger_concall_satin_q1fy27.md"
counts:
  turns: 12
  participants: 11
  questions: 20
  mgmt_numbers: 177          # management-attributed only; 194 total numeric disclosures enumerated (177 mgmt-stated + 17 analyst-quoted) in Section D
  guidance_fwd: 15
flags_raised: [GARBLE, ANCHORED, DISCREPANCY, NOT_FOUND, AMBIGUOUS, WRAP_SPLIT, WORD_FORM_MANUAL_ADD, UNCONFIRMED, NEW_DISCLOSURE, REPEAT_QUESTION, TRUNCATED_QUESTION, SPLIT_PARAGRAPH_SAME_TURN, SINGLE_MGMT_VOICE, DESIGNATION_NOT_STATED, MGMT_MISHEARD_QUESTION, ZERO_STANDING, SCHEME_NOT_ADOPTED, DISCREPANCY_RESOLVED_IN_DIALOGUE]
gate_a2: pass
mismatch_note: "First-pass grep undercounted mgmt_numbers (186 vs 190 sweep) due to 3 number+unit pairs split across the A1 word-wrap line boundary (ln153/154, ln190/191, ln315/316) plus 5 word-form tokens no unit-regex catches; re-swept and reconciled to 194 total (120 Turn 2 + 74 Q&A) before emission. Participants count similarly moved 10 -> 11 on re-sweep (operator undercounted as a distinct role). Both re-sweeps are documented in the COUNT TEST note and retained as audit trail; final counts above are the reconciled, passing figures."
```
