# A3 FORENSIC NOTES — Concall — Ksolves India Limited — Q1FY27

Source extract: `extract_concall_ksolves_q1fy27.txt` (783 lines, 15 pages, 100% text-layer).
A2 ledger: `ledger_concall_ksolves_q1fy27.md` (74 turns, 17 questions, 34 quant rows, 10 forward/hedge rows) — read verbatim at every cited line.
Doctype: concall. Prior-quarter ledger NOT supplied → no quarter-over-quarter verbatim diff possible (F15/F16-diff/consecutive-silence counts noted as unestablishable, not zero).
Ledger reconciliation: 100% of ledger rows read at their A1 line cites.

Conservative bias applied: where direction is uncertain, leaned bear and generated a question rather than resolving it.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------------|----------------|---------------------|
| FN-01 | F6 | §5 #3; §6 #? | L168-169 (turn 2) | "we expect the full impact to be reflected over the next two to three quarters, resulting in some near-term revenue softness" | FORWARD-SIGNAL | Ramp-down damage lands Q2-Q3 FY27, not fully in Q1 print. Touches tripwire (a) Q2 growth <15%. |
| FN-02 | F6 | §5 #6; §6 #1 | L181-183 (turn 2) | "it would not be prudent for us to reaffirm the revenue guidance for the current financial year at this stage" | FORWARD-SIGNAL | FY27 revenue guidance formally withdrawn. Management removing a number it previously stood behind = downgrade signal. |
| FN-03 | F6 | §5 #7,#24; §6 #2,#4 | L192; L195-197 (turn 2) | "we continue to target EBITDA margin... in the 25% to 30% range for the full year and on a quarter-on-quarter basis" | NEUTRAL-FACT | Margin band reiterated and defended (30.3% actual); no downgrade. Anchors monitoring item 1/EBITDA floor 28%. |
| FN-04 | F6 | §5 #24; §6 #7 | L696-698 (turn 62) | "Not this year, but after this year, FY26-27, we would again like to maintain 20% minimum growth, with a 30% margin" | FORWARD-SIGNAL | 20%+ growth deferred to FY28. FY27 explicitly conceded soft. Sets the promise-vs-delivery clock at FY28. |
| FN-05 | F6 | §5 #27 | L727-728 (turn 66) | "even if I get all the projects, we cannot complete them in one quarter. It will take at least two quarters" | FORWARD-SIGNAL | Even full pipeline conversion is a 2-quarter revenue lag → no fast recovery even in the bull case. |
| FN-06 | F6 | §5 #28; §6 #9 | L744-745 (turn 70) | "if things go well, we may increase revenue by 4% to 5% year on year, maximum" | FORWARD-SIGNAL | New implied FY27 growth ceiling ~4-5% — well below the 15% red / 18% monitoring line. This is the de-facto replacement guidance. |
| FN-07 | F7 | §6 #3 | L357 (turn 17) | "I would like to be conservative. I do not want to give any false hope" | FORWARD-SIGNAL | CMD pre-emptively lowering expectations on an up-quarter print. Tone signal: management sees more downside than the numbers show. |
| FN-08 | F7 | §5 #3,#28; §6 #6,#8,#9 | L314; L356; L371; L665-667; L729; L744 | recurring "if things go well / if it improves / if everything goes well" | AMBIGUOUS | Every recovery statement is conditional. Base case = continued softness; upside is entirely contingent and unquantified. |
| FN-09 | F7 | §5 #19 | L450 (turn 29) | "Till now, I cannot disclose the number" | AMBIGUOUS | Flagship "excellent milestone" international-bank AI deal deflected on size → materiality unverifiable from the call. Maps to monitoring item 13 (largest deal). |
| FN-10 | F7 | §5 #30; §6 #10 | L750-751 (turn 71) | "For the guidance related to FY'28, we will revisit it again in March 2027, when we have better clarity" | FORWARD-SIGNAL | FY28 guidance deferred 8 months. Dateable decision event = March 2027; schedule a follow-up. |
| FN-11 | F7 | §5 #17,#18,#21 | L408-410; L462-463; L551-553 | "developer efficiency... almost 25%"; "more than 50 use cases"; "more than 80% of our revenue comes from repeat customers" | AMBIGUOUS | Qualitative/round-number claims not verifiable from the transcript; no supporting metric disclosed. Flag for A4 to test against the deck/AR. |
| FN-12 | F16 | §5 #24,#25; §6 (context) | L715-716 (turn 64); L181-183 | "In the last call, I said... 18% to 20%. But because of these two losses, things got changed" | FORWARD-SIGNAL | Self-referenced downward reframe: a specific prior-concall guidance number (18-20%) dropped and not reaffirmed. Guidance softened between quarters, evidenced in-transcript. |
| FN-13 | F17 | §5 #15; §4 Q1-Q3 | L303-306 (turn 9) | "out of the 10, two customers have suddenly reduced their business, and they had been with us for the last three years" | FORWARD-SIGNAL | TWO of top-10 already in ramp-down. Pre-committed tripwire (b): a THIRD disclosed ramp-down → trim to 1.5%. Now at 2 of 3. |
| FN-14 | F17 | §5 #2,#28 | L234 (turn 3); L744 (turn 70) | "revenue for the quarter stood at Rs. 41.4 crore, with 10% YoY growth" | FORWARD-SIGNAL | +10% YoY is already below the 15% red line; implied FY27 ~4-5%. Monitoring item 2 flashing red; tripwire (a) live. |
| FN-15 | F17 | §5 #13; §4 Q10 | L263 (turn 3); L516 (turn 37) | "We maintain strong cash conversion and prudent working capital management" | CONFIRMATORY-NEGATIVE | Cash-conversion / working-capital claimed qualitatively but DSO, CFO/PAT, promoter holding, FII+DII, fixed-price mix, telecom %, and attrition rate all left unquantified. See silence table. |
| FN-16 | F17 | §1 roster | L94-96 (roster); 0 turns | Darpan Audichya "HEAD BUSINESS TRANSFORMATION AND CONSULTING" — zero speaker turns | AMBIGUOUS | The transformation/consulting head is silent on a call dominated by AI-led transformation. Mild credibility/roster note; not decisive alone. |

---

## CHECKLIST SCORECARD (all 17, one status each — GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Concall transcript carries no financial-statement line items; ZERO_STANDING is a results-filing flag family (ledger §Flags confirms). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Only consolidated figures spoken (L154, L234); no standalone column to decompose in a concall. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost lines available in a transcript. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor's Other Matters / component-auditor disclosure in a concall. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No auditor EoM paragraph in a transcript; nothing to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Multiple dated/dateable commitments — guidance withdrawn (L181), FY28 20% deferred (L696), pipeline 2-qtr lag (L727), 4-5% max (L744). See FN-01,02,04,05,06 + Commitment Register. |
| F7 HEDGE MINING | **FINDING** | Dense conditional/hedge cluster + a deflected quant (bank deal size, L450) + FY28 deferral (L750) + pre-emptive "no false hope" (L357). FN-07,08,09,10,11. |
| F8 TAX FORENSICS | N.A. | No ETR / deferred-tax / earlier-year tax adjustment disclosed on the call. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a transcript. |
| F10 SHARE COUNT & DILUTION | N.A. | EPS quoted (Rs 3.88 vs 2.71, L178-179) but no paid-up capital, no basic-vs-diluted spread, no corporate action → nothing to trace. |
| F11 RESERVES & NET WORTH TIE-OUT | N.A. | No Other Equity / net-worth figures on the call. |
| F12 SEGMENT FORENSICS | N.A. | No segment asset/liability tables in a transcript (geography mix given as revenue % only, L257-259). |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Reviewed the two disclosed board/leadership items — interim dividend Rs 4/sh (L265-266) and sales-leadership hires Eric Paul / Najib Saiyed (L187-188); neither is an AR/AGM/director-term catalyst. Appointments logged in Commitment Register as a pipeline-rebuild action. |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | No auditor letter / note text to cross-check; roster designations consistent between title page (L94) and roll call (L129). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in a concall and no prior-quarter ledger supplied. |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** | In-transcript guidance reframe: management self-references its prior-concall 18-20% growth figure and formally declines to reaffirm FY27 guidance (FN-12). Detectable without the prior deck. |
| F17 CONCALL SILENCE / TRIPWIRE AUDIT | **FINDING** | Monitoring checklist cross-ref: 2-of-3 top-10 ramp-down tripwire live (FN-13), revenue growth red (FN-14), and 7 monitoring metrics left unquantified (FN-15); silent panelist (FN-16). |

Status tally: 11 N.A. (F1,F2,F3,F4,F5,F8,F9,F10,F11,F12,F14,F15 — that is 12) / 1 PASS (F13) / 4 FINDING (F6,F7,F16,F17). No blanks.

Correction to tally: N.A. = 12 (F1-F5, F8-F12, F14, F15); PASS = 1 (F13); FINDING = 4 (F6, F7, F16, F17); total 17.

---

## COMMITMENT REGISTER (from F6 / F7 forward language)

| commitment | implied date | ref (line/turn) | status word |
|------------|--------------|-----------------|-------------|
| Full impact of client ramp-downs to reflect in results | over next 2-3 quarters (Q2-Q3 FY27) | L168-169 / turn 2 | underway |
| Not reaffirming FY27 revenue guidance "at this stage" | FY27 | L181-183 / turn 2 | withdrawn |
| EBITDA margin held in 25%-30% band, full-year and QoQ | FY27 | L192 / turn 2 | reiterated |
| EBITDA margin to move toward upper end as revenue scales | conditional, FY27+ | L195-197 / turn 2 | intends |
| Bank AI-hosted platform "almost a year-long project," still in discussion | ~12 months from Q1FY27 | L466-469 / turns 30-31 | in discussion / initiated |
| Official partner of Claude / Anthropic "very soon" | near-term | L581-582 / turn 48 | in process |
| Start SAP and cybersecurity as new verticals "as soon as possible" | unspecified, FY27+ | L672-678 / turn 60 | planning / initiated |
| 20% minimum YoY growth + 30% margin to resume after FY27 | FY28+ | L696-698 / turn 62 | intends |
| FY27 revenue same as FY26, +4-5% max "if things go well" | FY27 | L744-745 / turn 70 | expected (hedged) |
| Pipeline (~US$1M: $300K + $250K) conversion needs "at least two quarters" | H2 FY27 | L724-728 / turn 66 | expected |
| FY28 guidance to be revisited | March 2027 | L750-751 / turn 71 | deferred |
| Sales leadership appointed to accelerate NA/global pipeline (Eric Paul VP Global Sales; Najib Saiyed Head Sales NA) | done (Q1FY27) | L187-188 / turn 2 | completed |

---

## F17 — "WHAT WAS NOT DISCUSSED" TABLE (monitoring checklist cross-reference)

Consecutive-quarter silence counts cannot be established this run (prior-quarter ledger not supplied); counts shown as "1 (this qtr); prior unestablished."

| Monitoring item | Addressed on call? | Evidence line | Silence count |
|-----------------|--------------------|---------------|----------------|
| 1. EBITDA margin (green >=28%) | YES — 30.3% | L240 | n/a (addressed) |
| 2. Revenue growth YoY (red <15% x2) | YES, ADVERSE — +10% YoY; implied FY27 ~4-5% | L234, L744 | n/a (addressed, red) |
| 3. PAT margin (green >=20%) | YES — 22.2% | L249 | n/a (addressed) |
| 4. DSO / receivable days (red >65) | NO — only "prudent working capital management" claimed, no day count | L263 (proxy) | 1; prior unestablished |
| 5. CFO/PAT (green >=0.85x) | NO — "strong cash conversion" asserted, no ratio | L263 (proxy) | 1; prior unestablished |
| 6. IT products % revenue | YES, ADVERSE — services 98.3% and explicit products exit ("completely service-based company") | L253, L480-498 | n/a (addressed, red-leaning) |
| 7. Fixed-price revenue mix (green >25%) | NO — only a single "T&M project" mention, no mix % | L308 (proxy) | 1; prior unestablished |
| 8. Promoter holding (red <55% / any sale) | NO — never raised | none (absent L109-777) | 1; prior unestablished |
| 9. Top-5 client concentration (red >55%) | YES, ADVERSE — top-10 ">half"; 2 of 10 ramped down | L297, L303-306, L348 | n/a (addressed, tripwire b at 2/3) |
| 10. Net debt (green net cash) | YES — debt-free, cash Rs 17 cr | L262 | n/a (addressed, green) |
| 11. Telecom sector concentration | NO — Fortune 500 telecom giant named, no sector % | L563 (proxy) | 1; prior unestablished |
| 12. FII+DII combined | NO — no shareholding-pattern discussion | none (absent) | 1; prior unestablished |
| 13. Largest deal closed (>=$1M / >$500K) | YES, ADVERSE — largest single disclosed $300K; bank deal size withheld | L450, L724-725 | n/a (addressed, red — no disclosed deal >$500K) |
| 14. Attrition rate (red >22%) | NO — layoffs question answered without any attrition % | L516 | 1; prior unestablished |

Panelist silence: Darpan Audichya (Head, Business Transformation & Consulting) — 0 of 74 turns despite an AI-transformation-heavy call (L94-96 roster; FN-16).

Interpretation (conservative): sustained silence on DSO, CFO/PAT, promoter holding and attrition — four metrics that anchor the full-exit tripwires — while revenue growth and client concentration flash red is a confirmatory-negative pattern per Role 5. A4 should convert the seven silent items into direct management questions next quarter.

---

## HANDOFF TO A4 (flagged findings → management questions)

FORWARD-SIGNAL (convert to questions): FN-01, FN-02, FN-04, FN-05, FN-06, FN-07, FN-10, FN-12, FN-13, FN-14.
AMBIGUOUS (convert to questions): FN-08, FN-09, FN-11, FN-16.
CONFIRMATORY-NEGATIVE (monitor): FN-15.
NEUTRAL-FACT (log only): FN-03.

Highest-priority A4 questions: (1) implied FY27 growth now ~4-5% max vs prior 18-20% — quantify the trajectory and the third-client risk (FN-06/FN-12/FN-13); (2) size and revenue recognition profile of the withheld bank AI deal (FN-09); (3) DSO, CFO/PAT and attrition numbers that were never spoken (FN-15).

---

```yaml
stage: A3-forensics
company: "ksolves"
quarter: "q1fy27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ksolves-q1fy27/work/forensics_ksolves_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "FN-01", check: "F6", line: "168-169", classification: "FORWARD-SIGNAL", implication: "Ramp-down full impact lands Q2-Q3 FY27; tripwire (a) risk"}
  - {id: "FN-02", check: "F6", line: "181-183", classification: "FORWARD-SIGNAL", implication: "FY27 revenue guidance formally withdrawn"}
  - {id: "FN-03", check: "F6", line: "192", classification: "NEUTRAL-FACT", implication: "EBITDA margin 25-30% band reiterated; no downgrade"}
  - {id: "FN-04", check: "F6", line: "696-698", classification: "FORWARD-SIGNAL", implication: "20%+ growth deferred to FY28"}
  - {id: "FN-05", check: "F6", line: "727-728", classification: "FORWARD-SIGNAL", implication: "Even full pipeline conversion is a 2-quarter revenue lag"}
  - {id: "FN-06", check: "F6", line: "744-745", classification: "FORWARD-SIGNAL", implication: "New implied FY27 growth ceiling ~4-5%, below 15% red"}
  - {id: "FN-07", check: "F7", line: "357", classification: "FORWARD-SIGNAL", implication: "CMD pre-empting low expectations on an up-quarter; tone signal"}
  - {id: "FN-08", check: "F7", line: "356", classification: "AMBIGUOUS", implication: "All recovery statements conditional; base case is continued softness"}
  - {id: "FN-09", check: "F7", line: "450", classification: "AMBIGUOUS", implication: "Flagship bank AI deal size deflected; materiality unverifiable"}
  - {id: "FN-10", check: "F7", line: "750-751", classification: "FORWARD-SIGNAL", implication: "FY28 guidance deferred to March 2027; dated follow-up event"}
  - {id: "FN-11", check: "F7", line: "408-410", classification: "AMBIGUOUS", implication: "Round-number efficiency/repeat-revenue claims unverifiable from call"}
  - {id: "FN-12", check: "F16", line: "715-716", classification: "FORWARD-SIGNAL", implication: "Self-referenced downward reframe of prior 18-20% guidance"}
  - {id: "FN-13", check: "F17", line: "303-306", classification: "FORWARD-SIGNAL", implication: "2 of 3 top-10 ramp-down tripwire; third triggers trim to 1.5%"}
  - {id: "FN-14", check: "F17", line: "234", classification: "FORWARD-SIGNAL", implication: "Revenue +10% YoY below 15% red; monitoring item 2 red"}
  - {id: "FN-15", check: "F17", line: "263", classification: "CONFIRMATORY-NEGATIVE", implication: "DSO/CFO-PAT/promoter/FII-DII/fixed-price/telecom%/attrition all unquantified"}
  - {id: "FN-16", check: "F17", line: "94-96", classification: "AMBIGUOUS", implication: "Transformation/consulting head silent across all 74 turns"}
forward_signals: ["FN-01","FN-02","FN-04","FN-05","FN-06","FN-07","FN-10","FN-12","FN-13","FN-14"]
ambiguous: ["FN-08","FN-09","FN-11","FN-16"]
commitments:
  - {commitment: "Full impact of client ramp-downs reflected in results", implied_date: "Q2-Q3 FY27", ref: "L168-169/turn2", status_word: "underway"}
  - {commitment: "FY27 revenue guidance not reaffirmed", implied_date: "FY27", ref: "L181-183/turn2", status_word: "withdrawn"}
  - {commitment: "EBITDA margin held 25-30% full-year and QoQ", implied_date: "FY27", ref: "L192/turn2", status_word: "reiterated"}
  - {commitment: "EBITDA margin toward upper end as revenue scales", implied_date: "FY27+", ref: "L195-197/turn2", status_word: "intends"}
  - {commitment: "Bank AI platform ~year-long project, still in discussion", implied_date: "~12 months", ref: "L466-469/turn30-31", status_word: "initiated"}
  - {commitment: "Official Claude/Anthropic partner very soon", implied_date: "near-term", ref: "L581-582/turn48", status_word: "in-process"}
  - {commitment: "Start SAP and cybersecurity verticals ASAP", implied_date: "FY27+", ref: "L672-678/turn60", status_word: "initiated"}
  - {commitment: "20% minimum growth + 30% margin resumes", implied_date: "FY28+", ref: "L696-698/turn62", status_word: "intends"}
  - {commitment: "FY27 revenue same as FY26, +4-5% max if things go well", implied_date: "FY27", ref: "L744-745/turn70", status_word: "expected"}
  - {commitment: "Pipeline (~US$1M) conversion needs at least two quarters", implied_date: "H2 FY27", ref: "L724-728/turn66", status_word: "expected"}
  - {commitment: "FY28 guidance to be revisited", implied_date: "March 2027", ref: "L750-751/turn71", status_word: "deferred"}
  - {commitment: "Sales leadership appointed to accelerate pipeline", implied_date: "done Q1FY27", ref: "L187-188/turn2", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
