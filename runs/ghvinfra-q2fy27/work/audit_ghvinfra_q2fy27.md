# A5 ADVERSARY / COMPLETENESS AUDIT: GHV Infra Projects Limited (GHVINFRA), Q2 FY27 (RE-AUDIT, iteration 3, audit of record)

Agent: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-23 | iteration: 3 (after correction loop 2; final; no further loop follows)
Instruction file: prompts/quarterly-a5-adversary.md
Inputs read (only these):
- A4 review (loop 2): runs/ghvinfra-q2fy27/work/review_ghvinfra_q2fy27.md (867 lines)
- A1 fulltext (the spine): runs/ghvinfra-q2fy27/extracted/ghvinfra-results-q2fy27-fulltext.md (843 lines)
- A1 structured: runs/ghvinfra-q2fy27/extracted/ghvinfra-results-q2fy27-structured.md (R001-R821)
- A2 ledger: runs/ghvinfra-q2fy27/work/ledger_results_ghvinfra_q2fy27.md (253 rows)
- A5 iteration-2 audit (gap list): runs/ghvinfra-q2fy27/work/audit_ghvinfra_q2fy27_iter2.md
Not opened: the source PDF and everything under inputs/. A3 reasoning was not read. Every figure below was re-derived from the fulltext.
Anchors: "l###" = fulltext line. "review l###" = A4 review line (loop 2 file). Units: Rs Lakhs (L) as filed; Rs Cr = L x 0.01.
Scope (orchestrator, bounded): verify the five iteration-2 items at their sites, re-run the brief gate, carry the coverage count forward, and run the adversarial read on loop-2 new claims only.

---

## ITERATION-2 GAP CLOSURE (iteration-2 findings vs loop 2 review)

| Iter-2 ID | Type | Gap | Status | Evidence in loop 2 review (recomputed against the fulltext) |
|---|---|---|---|---|
| F-A | FACTUAL | "C keeps 0.50 Cr of investments" | CLOSED | review l414: "C keeps 0.50 L (Rs 0.005 Cr) of investments (l678)". l678 prints 0.50 L both dates. Elimination 1,189.90 - 0.50 = 1,189.40 L = 11.89 Cr (l374, l678) |
| F-B | FACTUAL | 0.99% yield "cap [derived]" and "non-interest-bearing [derived]" | CLOSED | review l412: the cap holds "only if the full amount stayed out all half"; maturity dates and Mar-26 gross balance NOT FOUND; l444 named a net flow; the 22.40 Cr bank placements (l443, 2,240.20 L) named; conclusion tagged [INFERENCE]. Q33 (review l639): "[INFERENCE; maturity dates NOT FOUND]". Ratio 58.39 / 5,918.44 = 0.987% (l427, l444) |
| F-C | FACTUAL | "remaining 90.54 Cr at most" (inverted bound) | CLOSED | review l406: 90.54 Cr if all 59.18 Cr sat in the line; larger, up to the full 149.72 Cr, if less did; tagged [INFERENCE]. 16,043.59 - 1,071.11 = 14,972.48 L; less 5,918.44 = 9,054.04 L (l375, l444). Header l15 wording differs (STYLE ST-A) |
| M-A | MISSING | 37.61 Cr "ceiling" lacked the booked-balance scope | CLOSED | Every reader-facing "ceiling" now reads "booked-balance ceiling" with claims and performance guarantees NOT FOUND, outside it: review l87 (0D S5), l398 (5-S row), l414 (Step 5), l538 (6D), l555 (6.5), l589 (8B d), l609 (Q3), l610 (Q4), l638 (Q32), l676 (Step 9 Key Notes), l687 (Flag 1), l770 (forward map), YAML l806, l807, l852. Grep of "ceiling" finds no unqualified site. Anchors l485-487 verified verbatim |
| M-B | MISSING | Warrant timing from R302 unread; deadline and forfeiture absent | CLOSED on the inference, dates and forfeiture; one new defect in a support sentence (F-D) | review l72-73 (0C), l75 (readings), l540 (6D), l618 (Q12), l658 (M4), l676 (Key Notes), l697 (Flag 11), l766 (forward map, dated, forfeiture leg added), YAML l815, l841, l861. R302 = 3,850.00 L (structured l310; fulltext l448 H1 FY26 column) |
| ST1 | STYLE | Name the DTA residual in the bridge | CLOSED | review l414: 10.32 L C-over-S DTA (244.63 - 234.31, l376, l680) |
| ST2 | STYLE | "(2.14)" not a recovery | CLOSED | review l398 in-cell |
| ST3 | STYLE | 29.10 Cr net basis | CLOSED | review l87, l415: 29.10 net of trade payables only; 28.31 net of all 12.21 Cr |
| ST4 | STYLE | 25.39 Cr covers both subsidiaries | CLOSED | review l87, l398, l414: "exposure to the two subsidiaries (FZ-LLC holds Erisha)" |
| ST5 | STYLE | Undated forward-map rows to the end | CLOSED | review l763-771: dated rows run Now, 22-Jan, 14-Feb, 31-Mar, 30-May, 14-Aug, 22-Aug; "undated" and "NOT FOUND" last |

All five iteration-2 items are closed at their named sites. A new defect sits inside the M-B text (F-D). It came from my own iteration-2 narrative (3C), which A4 carried into 0C. A5 owns it as much as A4.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS: PASS. All five labelled brief parts are present and carry real content.

| Brief part | Heading (review line) | Status | Content check |
|---|---|---|---|
| 1. Summary narrative | "### 1. SUMMARY NARRATIVE" (review l706) | present | 20 lines (review l708-727), inside the 10-20 band. "Up to" and the INFERENCE tag on the Erisha link stand (l718) |
| 2. Sector intelligence | "### 2. SECTOR INTELLIGENCE" (review l729) | present | 5 bullets; the West Asia quote ties to l483-484; gaps stated NOT FOUND |
| 3. Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" (review l737) | present | 9 bullets; 0.69 Cr construction cost (l744) and non-trade liabilities (l745) stand |
| 4. Competition intelligence | "### 4. COMPETITION INTELLIGENCE" (review l749) | present | 5 bullets; peer set NOT FOUND stated |
| 5. Forward map | "### 5. FORWARD MAP" (review l757) | present | Make-or-break line plus 9 catalysts. Every row has a bull fork and a bear fork. 7 rows dated and in order; the warrant row is dated 31-Mar-2027 [INFERENCE] with the forfeiture leg |

Gate result: no part missing or empty. The gate does not fail.

---

## 1. COVERAGE AUDIT

### 1A. Enumeration (carried forward from iteration 2)

The orchestrator states that the fulltext, structured file and ledger are byte-identical to iteration 2, with no edit in git history. I carried the iteration-2 fresh count forward and did not re-sweep every statement line. I ran these spot checks to confirm the files match the iteration-2 baseline:
- Structured: grep "^R### |" = 821 IDs (iteration 2: 821).
- Ledger: grep of row IDs (L###, A##-G##) = 253 (iteration 2: 253).
- Fulltext: 843 lines (last content l842, iteration 2: 843).
- Anchor values unchanged: l353 (R163-R168), l448 (R301 6,666.67; R302 3,850.00), l678 (0.50 / 0.50), l714 (76,587.87).

| Category | A2 count | A5 count (iter-2 fresh pass, carried) | Orphan rows | Status |
|---|---|---|---|---|
| Notes, standalone | 8 | 8 | none | MATCH |
| Notes, consolidated | 11 | 11 | none | MATCH |
| Footnotes (EPS asterisk) | 2 | 2 | none | MATCH |
| Line items, all six statements | 196 | 196 | none | MATCH |
| Zero-standing cells | 41 | 41 | none | MATCH |
| Board agenda items | 4 | 4 | none | MATCH |
| Annexures | 3 | 3 | none | MATCH |
| Auditor paragraphs | 11 | 11 | none | MATCH |
| Consolidation entities (excl. parent) | 4 | 4 | none | MATCH |
| Turns / questions / slides | 0 | 0 | n/a | MATCH |
| Structured IDs | 821 | 821 (re-counted this run) | none | MATCH |
| Ledger rows | 253 | 253 (re-counted this run) | none | MATCH |

missing_from_ledger = [].

### 1B. Ledger rows vs A4 review (orphan test, loop-2 delta)

- The iteration-2 "unread cell" is closed. Ledger L085 (R301-R302, l448) now has its H1 FY26 cell R302 read at review l72.
- Loop-2 text cites l353 (L023, R163-R169), l356-357, l375, l410, l427, l443, l444, l448 (L085), l475, l485-487, l678, l714. Each of these rows was already cited, so loop 2 creates no orphan row.
- The nine base-run orphans (L030, L134, L080, L158, L082, L055, L056, L074, L075) keep their reads at review l392-398 and l412-415.

Coverage verdict: PASS. orphan_rows = [].

---

## 2. ARITHMETIC AUDIT (every figure at the loop-2 fix sites)

"PASS" = matches within rounding (0.01 Cr, 0.01 pp). Figures outside the fix sites passed in iterations 1 and 2, and their inputs have not changed.

| Metric | A4 value (review line) | Recomputed (from Lakhs) | Source line | Status |
|---|---|---|---|---|
| C investments | 0.50 L, Rs 0.005 Cr (l414) | 0.50 L | l678 | PASS |
| Investments eliminated on consolidation | 11.89 (l414) | 1,189.90 - 0.50 = 1,189.40 L | l374, l678 | PASS |
| S-over-C current OFA | 13.50 (l414) | 45,214.27 - 43,864.36 = 1,349.91 L | l384, l688 | PASS |
| Funded parent exposure | up to 25.39 (l87, l398, l414) | 1,189.40 + 1,349.91 = 2,539.31 L | as above | PASS |
| Consolidation bridge with DTA | 97,226.59 L (l414) | 95,680.05 + 4,075.53 - 1,189.40 - 1,349.91 + 10.32 = 97,226.59 L; DTA 244.63 - 234.31 = 10.32 L | l388, l572, l376, l680, l692 | PASS (exact) |
| Subsidiaries' booked external liabilities | 12.21 (l414) | 76,587.87 - 75,366.48 = 1,221.39 L | l410, l714 | PASS |
| Booked-balance ceiling | 37.61 (l414 and sites) | 2,539.31 + 1,221.39 = 3,760.70 L | as above | PASS |
| Ceiling as % of S net worth | 18.51% (l414, l638) | 3,760.70 / 20,313.57 = 18.513% | l393 | PASS |
| Funded as % of S net worth | 12.50% (l414, l687) | 2,539.31 / 20,313.57 = 12.501% | l393 | PASS |
| Group figure gross; net of trade payables; net of all booked liabilities | 40.52; 29.10; 28.31 (l87, l415) | (27,830.33 - 26,749.99) + (15,189.67 - 12,218.10) = 4,051.91 L; less 1,141.87 = 2,910.04 L; less 1,221.39 = 2,830.52 L | l381, l386, l685, l690, l404, l708 | PASS |
| Deposit yield ratio | 0.99% (l412, l639) | 58.39 / 5,918.44 = 0.987% | l427, l444 | PASS; premise now stated |
| Bank placements in H1 | 22.40 (l412) | 2,240.20 L | l443 | PASS |
| Non-current OFA fall; reclassification candidate | 149.72; 90.54 if all deposits sat there (l406) | 16,043.59 - 1,071.11 = 14,972.48 L; less 5,918.44 = 9,054.04 L | l375, l444 | PASS; bound now conditional |
| Total warrants | 38,50,000 (l72) | 16,66,667 + 21,83,333 = 38,50,000 | l475; FN13 arithmetic | PASS |
| H1 FY26 upfront vs R302 | 25% x 38,50,000 x Rs 400 = 38.50 Cr (l72) | 38,50,000 x 400 = Rs 154.00 Cr; x 25% = Rs 38.50 Cr = 3,850.00 L; R302 = 3,850.00 | l448 (structured l310) | PASS (exact to the paisa) |
| Forfeiture on lapse | about 21.83 (l73, l658, l697, l766) | 21,83,333 x 400 x 25% = Rs 21,83,33,300 = 2,183.33 L | l475 | PASS |
| Pending tranche consistency | 87.33 total; 65.50 due (l71, l766) | 1,09,16,665 x 80 = 8,733.33 L; 21.83 + 65.50 = 87.33 | l475 | PASS (ties both ways) |
| Pending deadline | by 31-Mar-2027 at the latest (l73 and sites) | Latest H1 FY26 allotment 30-Sep-2025 + 18 months = 30-Mar-2027; 31-Mar-2027 is a valid outer bound | l448; ICDR tenure (regulatory frame, not in filing) | PASS as an outer bound (see STYLE ST-B on the window) |
| Paid-up capital "did not move in that window" | stated as fact, cited l353 (l72; YAML l787 "paid-up capital flat (l353)") | l353 (R163-R168) prints closing capital only: 30-Sep-2025, 31-Mar-2026, 30-Jun-2026, 30-Sep-2026. There is no 31-Mar-2025 opening, so H1 FY26 movement cannot be computed. l358 dates the bonus only to "the previous year ended March 31, 2026"; a bonus inside H1 FY26 would have moved capital in that window | l353, l358; structured l171-176 | FAIL (FACTUAL F-D, unsupported premise) |

Arithmetic verdict: every loop-2 figure recomputes within rounding, and the consolidation bridge ties exactly. One support sentence states a fact that its cited line cannot show (F-D).

---

## 3. ADVERSARIAL READ (loop-2 new claims only)

### N1. "Booked-balance ceiling 37.61 Cr; claims and performance guarantees NOT FOUND, outside it" (review l87, l414 and sites)

Bear counter tested. The 37.61 Cr comes from S-minus-C differences (l374 vs l678, l384 vs l688, l410 vs l714). That method sees only balances with and through the subsidiaries. A direct parent balance tied to Erisha would sit in S and C alike, so the method cannot see it. Review l414 says "The 37.61 Cr bounds booked balances only", which a reader can take as all booked balances.
Survives? Not as a FACTUAL or MISSING item. Every site scopes the figure as "exposure to the two subsidiaries". The extract shows no direct parent balance with Rana Exim: the contract party is FZ-LLC (l482). Q4 (review l610) and Q32 (l638) already ask for the parent's total Erisha-linked exposure. The qualifier is also direction-neutral. A claim by GHV is upside, and Q3 (l609) keeps both forks. Logged as STYLE ST-D.

### N2. "Pending warrants convert or lapse by 31-Mar-2027 at the latest [INFERENCE]" (review l73 and sites)

Bear counter tested on two points.
- (a) The support sentence. Review l72 reads: "Paid-up capital did not move in that window (l353), so the 38.50 Cr was not a share issue." l353 has no 31-Mar-2025 opening (arithmetic table), so it cannot show this. My own iteration-2 text (3C) wrote "did not move between Sep-25 and Jun-26 (l353)". That was a non-sequitur, because the 38.50 Cr was received before Sep-25. A4 carried it into 0C. Survives? YES, as FACTUAL F-D. The conclusion keeps its INFERENCE tier on other evidence. The 3,850.00 L is an exact 25% of 38,50,000 warrants at Rs 400. Q2 FY26 diluted EPS of Rs 1.52 sits below basic EPS of Rs 1.56 (l356-357). So a dilutive instrument was outstanding in Jul-Sep 2025. The warrants are the only dilutive instrument the filing names (l475). Only the sentence needs to change.
- (b) The window. On the same premise (allotment in H1 FY26, from 1-Apr-2025), the 18-month tenure ends between 1-Oct-2026 and 31-Mar-2027. The warrants were still pending at 30-Sep-2026 (l475). The review gives only the outer bound, and the forward-map row sits after 14-Feb-2027. A weak lead in the extract points to the later part of the window. The H1 FY26 basic-diluted spread (2.21 vs 2.19, 0.9%) is about a third of the Q2 FY26 spread (1.56 vs 1.52, 2.6%) (l356-357). With 2-decimal rounding the ranges are 0.46-1.37% and 1.97-3.30%, so they do not overlap. That points to warrants outstanding for only part of H1, so allotment in Q2 FY26 and a deadline in Jan-Mar 2027 [weak INFERENCE]. Treasury-stock price effects could also cause the gap. Survives? Only as a precision note. The stated bound is correct and labelled "at the latest", and the row placement matches the leaning evidence. Logged as STYLE ST-B.

### N3. "On lapse about 21.83 Cr upfront is forfeited to the company, with no dilution [INFERENCE]" (review l73, l658, l697, l766)

Bear counter tested. The forfeiture brings in no new cash. The 21.83 Cr was received in H1 FY26 (l448) and is already in the balance sheet. On lapse, the company does not receive the 65.50 Cr still due. A reader of Flag 11 (l697) or M4 (l658) could still read "forfeited to the company" as a gain.
Survives? Only as wording. The forward-map bear fork (l766) already says "the funding gap stays". No site claims new cash. The arithmetic ties (21.83 + 65.50 = 87.33). The forfeiture rule is tagged INFERENCE, regulatory frame. Logged as STYLE ST-C.

### Mandatory acquisition-economics probe (re-run)

Loop 2 adds no acquisition text. The iteration-2 probes stand, and I re-checked both:
- Subsidiary infusion: 2.05 Cr (l442) went in against a 4.83 Cr H1 subsidiary loss (l573) on Nil revenue (l572). The earnings multiple is negative, and no earnings case exists. This is carried as Q29 (review l635).
- Promoter stake purchase: Rs 80 / TTM S EPS Rs 6.9587 = 11.50x, against a market P/E of 239 / 6.9587 = 34.35x (l347, l475; CMP from Notion). This is carried in 0C (review l69-71). The two readings stay open, and the separating observation is the H1 FY26 market and floor price (review l75).

---

## FINDINGS REGISTER (tagged)

| ID | Type | Agent | Gap (exact) | Exact fix | Anchors |
|---|---|---|---|---|---|
| F-D | FACTUAL | A4 (text site; A5-originated in iter-2 3C) | review l72 says "Paid-up capital did not move in that window (l353), so the 38.50 Cr was not a share issue." l353 (R163-R168) prints closing capital only, with no 31-Mar-2025 opening. It cannot show H1 FY26 capital was flat. The FY26 bonus (l358, dated only to FY26) may have moved capital in that half. YAML l787 repeats "paid-up capital flat (l353)" | At review l72, replace that sentence with: "Line 353 prints closing capital only (no 31-Mar-2025 opening), so it cannot show whether capital moved in H1 FY26. Corroboration: Q2 FY26 diluted EPS Rs 1.52 sits below basic Rs 1.56 (l356-357), so a dilutive instrument was outstanding in Jul-Sep 2025; the warrants are the only one the filing names (l475) [INFERENCE]." Change the l72 anchor cell to "l448, l356-357, l475". In YAML l787, replace "paid-up capital flat (l353)" with "Q2 FY26 diluted EPS below basic (l356-357)" | review l72, l787; l353, l356-358, l448, l475; structured l171-176, l310 |
| ST-A to ST-D | STYLE | none | See STYLE NOTES | as listed | as listed |

No MISSING finding. No CONTRADICTION finding. Loop-2 text agrees with itself at every warrant and ceiling site: 0C, 6D, Q12, M4, Key Notes, Flag 11, forward map and YAML carry the same date, figures and tiers.

---

## VERDICT

VERDICT: INCOMPLETE.

- Failing agent: A4 (text site). Gap: F-D [FACTUAL]. The one-sentence premise at review l72 (and YAML l787) cites l353 for a fact that l353 cannot show. The exact replacement text is in the register.
- Iteration cap: this is iteration 3, the audit of record, and no further loop follows. F-D goes to the orchestrator and the operator as an open item. It is a text swap with exact wording and needs no re-derivation.
- Not affected: the deliverable gate passes, coverage passes, and all five iteration-2 items are closed. Every loop-2 figure recomputes. F-D moves no number. It does not change the allotment inference tier (INFERENCE), the 31-Mar-2027 outer bound, the protocol verdict (PROCEED WITH FLAGS), the cash classification (INDETERMINATE-WITH-DIRECTION) or the AVOID framing. The Step 9 Key Notes text (review l676) does not contain the F-D sentence. The full-review page append (l677) does.

---

## STYLE NOTES (logged; no loop)

- ST-A. Header review l15 says the candidate is "at least 90.54 Cr and up to 149.72 Cr". The body (l406) states it conditionally, and other settlements inside l432 could lower it. Align the header to the body: "90.54 Cr if all 59.18 Cr sat in that line, up to 149.72 Cr otherwise".
- ST-B. Warrant deadline window. On the same H1 FY26 premise, the tenure ends between 1-Oct-2026 and 31-Mar-2027. A weak diluted-EPS lead (l356-357) leans to Jan-Mar 2027. Suggested date cell at l73, l658, l766 and YAML l841: "1-Oct-2026 to 31-Mar-2027 [INFERENCE]; diluted EPS leans to Jan-Mar 2027; watch BSE allotment or lapse intimations".
- ST-C. Forfeiture is not new cash. At l73, l658, l697 and YAML l841, l861, add "(already received in H1 FY26, l448; no new cash)".
- ST-D. At review l414, "bounds booked balances only" should read "bounds booked balances with and through the subsidiaries only". A direct parent balance tied to Erisha, if any, sits in S and C alike and the S-minus-C method cannot see it. The extract identifies none. Q4 and Q32 already ask.
- Carried: base S5 rounding-level differences, no action.

---

```yaml
stage: A5-adversary
company: "GHVINFRA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
iteration: 3
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
  basis: "iteration-2 fresh count carried forward (inputs byte-identical per orchestrator); spot checks this run: 821 structured IDs, 253 ledger rows, 843 fulltext lines, anchors l353/l448/l678/l714 unchanged"
iteration2_gaps_closed: [F-A, F-B, F-C, M-A, M-B, ST1, ST2, ST3, ST4, ST5]
arithmetic_mismatches:
  - metric: "Paid-up capital 'did not move' in H1 FY26 (support for warrant allotment inference)"
    a4_value: "Paid-up capital did not move in that window (l353), so the 38.50 Cr was not a share issue (review l72; YAML l787)"
    recomputed: "not derivable: l353 (R163-R168) prints closing capital at 30-Sep-2025, 31-Mar-2026, 30-Jun-2026, 30-Sep-2026 only; no 31-Mar-2025 opening; FY26 bonus (l358) undated within FY26"
    source_line: "fulltext l353, l358; structured l171-176"
surviving_bear_counters:
  - claim: "Warrant allotment in H1 FY26 supported by flat paid-up capital (l353)"
    counter: "l353 has no opening H1 FY26 value and cannot show capital was flat; the inference survives on the exact 25% match (3,850.00 L = 25% x 38,50,000 x Rs 400, l448) and Q2 FY26 diluted EPS 1.52 below basic 1.56 (l356-357)"
    source_line: "fulltext l353, l356-358, l448, l475; review l72, l787"
    type: FACTUAL
  - claim: "Pending warrants convert or lapse by 31-Mar-2027 at the latest"
    counter: "outer bound is correct; on the same premise the window is 1-Oct-2026 to 31-Mar-2027; weak diluted-EPS lead leans to Jan-Mar 2027"
    source_line: "fulltext l356-357, l448, l475; review l73, l658, l766, l841"
    type: STYLE
  - claim: "About 21.83 Cr forfeited to the company on lapse"
    counter: "not new cash; received in H1 FY26 (l448); lapse forgoes 65.50 Cr still due; bear fork already says the funding gap stays"
    source_line: "fulltext l448, l475; review l73, l658, l697, l766"
    type: STYLE
  - claim: "37.61 Cr bounds booked balances only"
    counter: "S-minus-C method sees only balances with and through the subsidiaries; direct parent Erisha balances, if any, are invisible to it; none identifiable in the extract; Q4 and Q32 ask"
    source_line: "fulltext l374, l384, l410, l482, l678, l688, l714; review l414, l610, l638"
    type: STYLE
findings_by_type:
  factual:
    - "F-D (A4 text site; A5-originated in iter-2 3C): review l72 'Paid-up capital did not move in that window (l353), so the 38.50 Cr was not a share issue' and YAML l787 'paid-up capital flat (l353)'; l353 prints closing capital only, no 31-Mar-2025 opening; replace with the l356-357 diluted-EPS corroboration (exact text in audit register)"
  missing: []
  contradiction: []
  style:
    - "ST-A: header l15 'at least 90.54 Cr' vs conditional body l406; align"
    - "ST-B: warrant deadline window 1-Oct-2026 to 31-Mar-2027 on the same premise; diluted EPS leans Jan-Mar 2027 (l356-357)"
    - "ST-C: forfeiture is not new cash; add 'already received in H1 FY26, l448'"
    - "ST-D: l414 'booked balances only' -> 'booked balances with and through the subsidiaries only'"
loop_back_to: "A4"
gap: "A4 (iteration cap reached, audit of record; route as operator open item): F-D [FACTUAL] at review l72 replace 'Paid-up capital did not move in that window (l353), so the 38.50 Cr was not a share issue.' with 'Line 353 prints closing capital only (no 31-Mar-2025 opening), so it cannot show whether capital moved in H1 FY26. Corroboration: Q2 FY26 diluted EPS Rs 1.52 sits below basic Rs 1.56 (l356-357), so a dilutive instrument was outstanding in Jul-Sep 2025; the warrants are the only one the filing names (l475) [INFERENCE].'; anchor cell to 'l448, l356-357, l475'; YAML l787 'paid-up capital flat (l353)' to 'Q2 FY26 diluted EPS below basic (l356-357)'. No number, verdict, cash classification or AVOID framing moves."
style_notes:
  - "ST-A: align header l15 reclassification wording to the conditional body l406"
  - "ST-B: date the warrant row as a window, 1-Oct-2026 to 31-Mar-2027 [INFERENCE], diluted EPS leaning Jan-Mar 2027"
  - "ST-C: forfeiture of 21.83 Cr brings no new cash (received H1 FY26, l448)"
  - "ST-D: scope 'booked balances' to balances with and through the subsidiaries"
analyst_note: "Loop 2 closed all five iteration-2 items and all five style notes at every named site. Every loop-2 figure recomputes from the fulltext, and the consolidation bridge ties to the paisa. The coverage count is carried forward. The inputs are unchanged, and the spot checks hold. One FACTUAL item remains, and it started in my iteration-2 text. That text said paid-up capital did not move. A4 carried it into 0C as support for the warrant allotment inference. Line 353 prints closing capital only. It has no 31-Mar-2025 opening, so it cannot show H1 FY26 was flat. The inference survives on two other facts. The 38.50 Cr is exactly 25% of 38.5 lakh warrants at Rs 400. Q2 FY26 diluted EPS sits below basic. The fix is a one-sentence swap. It moves no number, verdict, cash classification or AVOID framing. One weak lead is not grafted. The H1 FY26 diluted spread is about a third of the Q2 FY26 spread, which leans to a Q2 FY26 allotment and a Jan-Mar 2027 deadline. EPS rounding limits that lead. This is the audit of record. The operator decides whether to apply the swap before the Notion save."
```
