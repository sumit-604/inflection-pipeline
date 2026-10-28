# A5 ADVERSARY / COMPLETENESS AUDIT: Knack Packaging Limited (KNACK) | Q2 FY27 | CORRECTION LOOP 1 RE-AUDIT

Stage: A5 | Model: claude-opus-5-5 | Re-audit date: 29-Oct-2026 | Loop: 1 of 1 (the one permitted cycle)
Inputs read: rewritten A4 review (review_knack_q2fy27.md, 1,058 lines); loop-0 review (review_knack_q2fy27_loop0.md) for the diff; patched concall ledger (ledger_concall_knack_q2fy27.md); the same A1 fulltexts, structured files and results/deck ledgers as loop 0. No source PDF was opened. Nothing under inputs/ was read. A3 reasoning was not read.
Loop-0 audit: audit_knack_q2fy27_loop0.md (8 loop findings A5-01 to A5-08; 4 STYLE notes).

Anchor key: "rev L###" = rewritten review line. "r0 L###" = loop-0 review line. "res / deck / cc L###" = A1 fulltext lines. "led-cc L##" = patched concall ledger line.

Diff method: I checked that the loop-0 file matches the text I audited at loop 0 (r0 L384, L631, L690, L798, L867, L945-948 match). Then I read the rewritten review in full, line against line, and grepped both files for every changed term ("treasury", "very small portion", "8.6/kg", "minimum", "approximate", "other current assets", "1.82").

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

Plain-language brief (rev L913-959): (1) summary narrative PRESENT, rev L917-918, about 243 words (loop 0 about 217; one sentence added for A5-02); (2) sector PRESENT, rev L920-925; (3) business model PRESENT, rev L927-932; (4) competition PRESENT, rev L934-937; (5) forward map PRESENT, rev L939-946, 6 dated catalysts, each with a bull and a bear fork. Gate: PASS.

---

## 1. CLOSURE TEST: LOOP-0 FINDINGS

| ID | Type | Target | Loop-0 gap | Loop-1 evidence | Status |
|---|---|---|---|---|---|
| A5-01 | CONTRADICTION | A4 | "Very small portion" (cc L486-487, Mexico JV passage) used as India margin evidence at r0 L384, L690, L798, L867, L946 | Re-attributed at all five places: rev L390 (6D), L697 (5A), L805 (8A), L874 (Section C), L953 (FY27E PAT basis). India partial-recovery reading now rests on cc L478-480 and cc L547-559. The phrase now appears only in JV context: rev L393, L638, L697, L808. Conflict log row 12 (rev L41). Verified against cc L481-492 | CLOSED |
| A5-02 | FACTUAL | A4 | All Q2 other income called treasury; interest at most Rs 5.45/kg (res L631) | "Treasury" survives only in the conflict-log row that records the fix (rev L42). Relabelled at rev L89, L94, L213, L217, L243, L258, L262, L278, L401, L446, L453, L476, L581, L670, L880, L918, L930, L945, L949. 3.57 Cr (36.8%) and Rs 5.45/kg recomputed below. The 70.8% bridge share (rev L286) is unchanged, as it should be | CLOSED |
| A5-03 | MISSING | A4 | Contract "approximate" (deck L219) vs ASR "minimum" (cc L406-412); HIGH confidence for a floor | rev L568: "~Rs 150 Cr/yr approximate (deck p16 L219, FILED)"; confidence "HIGH for existence, size order and Dec-2028 end; LOW for a value floor". Also rev L377 (deck L240-241 "no material dependency" added), L633, L750, L779, L809, L936 | CLOSED |
| A5-04 | MISSING | A4 | 55.73 Cr receivables outflow = 40.48 Cr trade + about 15.03 Cr other current assets; 7A CONFIRMED overstated | rev L314 (new split paragraph), L318 (WC verdict and missing evidence), L452 (Q8), L677, L698, L775 (7A now PARTIALLY CONFIRMED), L932 | CLOSED |
| A5-05 | MISSING | A4 | Forward base and Reading 1 inherit the Q1 FY27 31.61 Cr build credit (res L532) | rev L957 (caveat under the forward table; size NOT FOUND); YAML flag rev L1051 | CLOSED |
| A5-06 | MISSING | A4 | CON other non-current assets 1.82 Cr below SA (res L237, L580) not used for Question 3 | rev L196 (two readings and the separating observation), L312, L447 (Q3, with bull and bear answers keyed to the two readings), L873, L900 (monitorable 14), YAML flag rev L1043 | CLOSED |
| A5-07 | MISSING | A2 | Question ledger lacked cc L164-166 (T05) and cc L501-511 (T11); A4 4A lacked the T05 row | led-cc L41 now 28 questions; T05-Q5 added (led-cc L47), T11-Q5 added (led-cc L67); ledger YAML "questions: 28" (led-cc L1047). Review 4A adds T05-Q5 (rev L621); grade count 28 rows (rev L646) | CLOSED |
| A5-08 | FACTUAL | A2 | T09-Q2 coded 3%/9,927; T10-Q3 coded NUMBER 69-72k | led-cc L56: "13% YoY volume growth, cc L363"; 9,927 moved to T05-Q5. led-cc L62: "DEFLECTED (reply cc L462 is about Mexico capacity)". Review agrees (rev L30, L630, L636) | CLOSED |

Result: 8 of 8 closed.

---

## 2. COVERAGE AUDIT (re-run on the patched ledger)

| Doc | Category | A2 count (loop 1) | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Concall | Questions | 28 (led-cc L41-71) | 28 (cc L133-578; same pass as loop 0) | none | PASS |
| Concall | Response-type totals | number 12; hedged/qualitative/partial/deflected 11; confirmed 3; declined 1; none 1 = 28 (led-cc L71) | 12 / 11 / 3 / 1 / 1 = 28, recounted row by row from led-cc L43-70 | none | PASS |
| Concall | REPEAT_QUESTION | 12 (led-cc L71, L1030) | 12 flagged rows (led-cc L47, L50, L52, L53, L55, L56, L58, L62, L64, L65, L68, L69) | none | PASS |
| Concall | Turns / IDs / line-0 | 16 / 934 / 0 | 16 / 934 / 0 (unchanged files) | none | PASS |
| Results | All categories | unchanged from loop 0 (notes 18+3, line items 198, ZERO_STANDING 41, agenda 3, auditor paras 12, entities 2, forward 10, IDs 921) | unchanged; ledger file not modified | none | PASS |
| Deck | All categories | unchanged from loop 0 (slides 36, ZERO_STANDING 15, M01-M06, IDs 798) | unchanged; ledger file not modified | none | PASS |

Orphan-row test: the preamble still marks every ID reviewed (rev L19-23), and the T05-Q5 and T11-Q5 rows now appear in 4A (rev L621, L641). Orphan rows: none. Missing from ledger: none. Units missing from the structured file: the seven known units (results M1; deck M01-M06), carried, A1 patch still open from A2 (unchanged from loop 0).

---

## 3. DRIFT AUDIT (rewritten review vs loop-0 review)

### 3A. Changes outside [LOOP1] markers
| rev line | Loop-0 text (r0 line) | Loop-1 text | Loop item behind it | Number or verdict moved? | Tag |
|---|---|---|---|---|---|
| L94 | "stripping treasury income" (r0 L92) | "stripping other income" | A5-02 relabel | No | STYLE (unmarked) |
| L262 | "Q2 FY27 other income carries IPO treasury income" (r0 L258) | "Q2 FY27 other income rose with IPO cash parked in FDs" | A5-02 | No | STYLE (unmarked) |
| L918 | "About 71% of that rise came from interest on unspent IPO money and a one-time tax credit" (r0 L911) | "About 71% of that rise came from higher other income and a one-time tax credit" | A5-02 (adjacent sentences are marked) | No (71% unchanged) | STYLE (unmarked) |
| L447, L452 (bull/bear cells) | Q3 and Q8 bull/bear answers (r0 L441, L446) | Answers rewritten to key off the two readings (Q3) and the other-current-assets split (Q8) | A5-06, A5-04 (marker sits in the same row's question cell) | No | none (same row is marked) |
| L963-1057 (A4 YAML block) | r0 L953-1046 | Questions 2, 3, 7, 8, 9, monitorable 14, flags 2, 4, 5, 9, 10, new FY28 flag, analyst_note | A5-02 to A5-06; conflict count 11 to 13 matches the 13 log rows (rev L28-42) | No verdict, no forward figure, no metric moved | STYLE (YAML not marked) |

### 3B. Numbers, verdicts and table cells
- Protocol verdict: PROCEED WITH FLAGS at rev L880 and r0 L873. Unchanged. Cash conversion INDETERMINATE-WITH-DIRECTION (rev L322, r0 L316). Unchanged. Position branch 8A-W, proposed RESEARCH / WATCH. Unchanged.
- Step 1A/1B/1C tables (rev L108-192 vs r0 L106-190): every cell identical.
- Step 2A/2B (rev L205-235 vs r0 L201-231): every number identical; only the OI and PAT verdict words changed (marked).
- Step 3, Step 4, Step 5 tables: every number identical; marked text only.
- Forward table (rev L952-955 vs r0 L945-948): all twelve figures identical (1,146.7 / 1,208.9 / 1,097.1; 112.1 / 131.2 / 103.7; 1,244.5 / 1,310.0 / 1,080.0; 122.3 / 166.8 / 81.8). Only the FY27E PAT basis text changed (marked, A5-01).
- Errata declared in the header (rev L3), all marked: rev L87 equity 414.15 to 414.14; rev L287 core PAT per share -14.9% to -14.7%; rev L770 GM YoY -651 to -652 bps. All three match my loop-0 recomputation (S-01).
- No number, verdict or table cell changed without a loop item behind it. New drift findings: 0 non-STYLE.

### 3C. Arithmetic of new or changed figures
| Metric (new in loop 1) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Q2 non-interest OI floor | at least 3.57 Cr (36.8%) | 97.04 - 61.33 = 35.71m; 35.71/97.04 = 36.8% | res L527, L631 | PASS |
| Q2 interest per kg cap | at most Rs 5.45/kg | 61.33m / 11,252 MT = 5.45 | res L631; cc L138 | PASS |
| Q2 OI per kg | about Rs 8.6/kg | 97.04m / 11,252 MT = 8.62 | res L527 | PASS |
| Receivables split | 40.48 + about 15.03 of 55.73 | 404.78m (res L584 delta); 150.27m (res L589 delta); 557.33m (res L641) | res L584, L589, L641 | PASS |
| Other NCA gap | 49.33 vs 51.15 = 1.82; both 40.25 at Mar-26 | 493.33m vs 511.54m = 18.21m; 402.53m both | res L237, L580 | PASS |
| Equity increase (erratum) | 414.14 | 7,223.24 - 3,081.85 = 4,141.39m | res L596 | PASS |
| Core PAT per share YoY (erratum) | -14.7% | 1.3745 / 1.6114 = -14.70% | rev L287 | PASS |
| GM YoY (erratum) | -652 bps | 34.638% - 41.154% = -651.6 bps | res L526-532 | PASS |
| 4A grade count | A 6, B 13, C 6, D 2, n/a 1 = 28 | A: T05-Q1, T05-Q5, T09-Q1, T09-Q2, T09-Q3, T12-Q3 = 6; others unchanged | rev L617-644 | PASS |

Arithmetic mismatches above rounding: 0.

---

## 4. ADVERSARIAL READ (loop 1)
The three loop-0 bear counters are grafted: P1 at rev L568 and L750; P2 at rev L314, L318 and L775; P3 at rev L957. The [LOOP1] text adds no new positive claim. The new Q3 and Q8 bull answers (rev L447, L452) are framed as answers to test, not as claims. The acquisition-economics probe result stands from loop 0: JV stake Rs 4.40 Cr for 50% (res L305), earnings negative, multiple not meaningful; cumulative loss share 7.00 Cr = 1.59x consideration; the bear reading is in the review (rev L447, L461, L1043).

---

## 5. NEW FINDINGS (loop 1)

FACTUAL: none. MISSING: none. CONTRADICTION: none.

STYLE (logged, no loop):
- S-05 (A4). Unmarked loop edits at rev L94, L262, L918 (the "About 71%" sentence) and in the A4 YAML block (rev L963-1057). Each has an A5-02, A5-03 or A5-06 item behind it, and none moves a number or verdict. Mark them [LOOP1] for audit trail.
- S-06 (A4). rev L949 says the non-interest part is "at least 3.57 Cr per quarter". That floor holds for Q2 and for the H2 assumption held at the Q2 composition. It does not hold for every quarter: Q1 FY27 total OI was 2.31 Cr (res L527), and H1 non-interest OI was 5.88 Cr in total (120.15m - 61.33m, res L527, L631). Write "at the Q2 composition".
- S-07 (A2). led-cc L64 still codes T11-Q2 as "HEDGED (very small portion recovered)". The response type HEDGED is correct on cc L478-480. The cue quotes the Mexico-passage phrase that the review now attributes to the JV (rev L638). No number, no review fact and no verdict depends on the cue, so this is STYLE. Align the cue with rev L638. Same file: the repeat pointers run backwards. T05-Q5 points to T09-Q2 (led-cc L47), and T09-Q2 points to T05-Q1 (led-cc L56); the YoY pair is T05-Q5 and T09-Q2.

STYLE carried from loop 0 (still open, no loop):
- S-01 partial. rev L235 SA period-end EPS YoY +3.43% (unrounded +3.55%). The other three items are fixed.
- S-02. rev L391 and rev L806 "utilisation % declined" (management declined to state it; cc L214-215, L189-191).
- S-03. rev L924 "FY26 H2 revenue was 16.9% above H1 (FILED)" is derived; tag INFERENCE.
- S-04. rev L121 anchor "L538/L541"; values are L538 only.

---

## VERDICT

VERDICT: COMPLETE.
- All eight loop-0 findings are closed (Section 1).
- The coverage re-run passes on the patched ledger: 28 questions, no orphan rows, nothing missing (Section 2).
- No drift: no number, verdict or table cell changed without a loop item behind it (Section 3).
- Arithmetic: 0 mismatches above rounding.
- Open items are STYLE only (S-01 partial, S-02 to S-07). Per the STYLE rule they are logged and never re-run. The review may proceed to the operator-approved Notion save.

---

```yaml
stage: A5-adversary
company: "KNACK"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - {id: "S-05", target: "A4", gap: "Unmarked loop edits at rev L94, L262, L918 and the A4 YAML block; each backed by A5-02/A5-03/A5-06; no number or verdict moved; mark [LOOP1]"}
    - {id: "S-06", target: "A4", gap: "rev L949 'at least 3.57 Cr per quarter' holds only at the Q2 composition; Q1 FY27 total OI 2.31 Cr (res L527); H1 non-interest OI 5.88 Cr (res L527, L631)"}
    - {id: "S-07", target: "A2", gap: "led-cc L64 T11-Q2 cue 'very small portion recovered' quotes the Mexico-passage phrase; HEDGED stands on cc L478-480; align with rev L638; repeat pointers at led-cc L47, L56 run backwards"}
    - {id: "S-01", target: "A4", gap: "Partial: rev L235 SA period-end EPS YoY +3.43% (unrounded +3.55%) still open; three other items fixed"}
    - {id: "S-02", target: "A4", gap: "rev L391, L806 'utilisation % declined' ambiguous; write 'not stated'"}
    - {id: "S-03", target: "A4", gap: "rev L924 derived H2/H1 ratio tagged FILED; tag INFERENCE"}
    - {id: "S-04", target: "A4", gap: "rev L121 anchor L538/L541; use L538"}
loop_back_to: ""
gap: ""
style_notes:
  - "S-05 unmarked loop edits rev L94, L262, L918, A4 YAML; no number or verdict moved"
  - "S-06 rev L949 3.57 Cr floor holds at Q2 composition only"
  - "S-07 led-cc L64 T11-Q2 cue still quotes the Mexico phrase; led-cc L47, L56 repeat pointers backwards"
  - "S-01 partial rev L235 +3.43% (unrounded +3.55%)"
  - "S-02 rev L391, L806 'declined' ambiguous"
  - "S-03 rev L924 derived ratio tagged FILED"
  - "S-04 rev L121 anchor L538/L541"
analyst_note: "Loop 1 closes A5-01 to A5-08: 8 of 8. Drift test: the loop-0 file matches what I audited, and a full line-by-line read found no number, table cell or verdict changed without a loop item behind it. All twelve forward-table figures, every Step 1-5 table cell and PROCEED WITH FLAGS are unchanged. The three declared errata match my loop-0 recomputation. New loop-1 figures (3.57 Cr, Rs 5.45/kg, 40.48 + 15.03, 1.82 Cr, grade count 28) all recompute. One judgement call: the patched ledger still codes T11-Q2 with the Mexico-passage phrase (led-cc L64). I tagged it STYLE, not CONTRADICTION. The response type HEDGED is correct on cc L478-480, the review attributes the phrase correctly, and no number, review fact or verdict depends on the cue. Remaining items are STYLE only and are not re-run."
```
