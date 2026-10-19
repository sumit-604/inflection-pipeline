# A5 AUDIT, LOOP 2 FINAL RE-AUDIT (closure only): Kross Limited (KROSS), Q2 FY27

Agent: A5 adversary / completeness auditor | model claude-opus-5-5 | date 2026-10-20
Instruction file: prompts/quarterly-a5-adversary.md
Prior audits: runs/kross-q2fy27/work/audit_kross_q2fy27.md (loop 0, INCOMPLETE); runs/kross-q2fy27/work/audit_kross_q2fy27_loop1.md (loop 1, INCOMPLETE on C1 only)

Scope (from the task message): (1) confirm C1 is closed and agrees with 6A and 6B #1; (2) confirm the deliverable-completeness gate still passes; (3) check only the loop-2 changed text for new FACTUAL / MISSING / CONTRADICTION errors. No new adversarial pass on unchanged text. Concall sections read "pending Role 5 addendum" by design (REV L4, L785); not failed.

Inputs read (and only these):
- A4 review: runs/kross-q2fy27/work/review_kross_q2fy27.md (now one file, L1-L825; Loop 2 change log L818-L824)
- A1 fulltexts: extracted/kross-results-q2fy27-fulltext.md (RES), extracted/kross-pressrelease-q2fy27-fulltext.md (PR), extracted/kross-presentation-q2fy27-fulltext.md (PPT)
- A1 structured: the three *-structured.md files (RES R001-R372, PR R001-R135, PPT R001-R665)
- A2 ledgers: work/ledger_results_kross_q2fy27.md, work/ledger_pressrelease_kross_q2fy27.md, work/ledger_presentation_kross_q2fy27.md

Not read: the source PDFs, anything under inputs/, A3 forensic notes, orchestrator commentary, blocks/a4.yaml. No source access was needed. No pipeline error to report. Pipeline note: a file extracted/kross-concall-q2fy27-fulltext.md now exists (seen in a page-marker grep). It is outside this Role 4 audit's inputs and was not opened. The Role 5 addendum can be scheduled against it.

Anchor key: RES / PR / PPT Lnnn = fulltext line. REV Lnnn = line in the single-file A4 review under audit. Review lines moved up by one against the loop-1 audit (old L699 is now L698-L699; old L617 is now L616). Units: RES in Rs Mn (Rs Cr = Mn x 0.1).

---

## A. C1 CLOSURE CHECK

Loop-1 finding C1 (CONTRADICTION): the single "By 30-May-2027" forward-map row mixed trigger 1, the H2 seasonality test and the Bear case. It labelled a Base-to-Bull revenue outcome and an AMBER margin as "the bear case becomes the working case".

Revised text (REV L698-L699), two rows:
- Test 1 (L698). Bull: "Operating margin ex-other income at or above 14% AND like-for-like debtor days lower than the prior half: trigger 1 fires". Bear: "Either leg fails: trigger 1 stays unfired; the Bear case applies only if operating margin is at or below ~12.5%".
- Test 2 (L699). Bull: "H2 revenue at or above Rs 461-482 Cr: the seasonal reading holds". Bear: "H2 revenue below Rs 461 Cr: the plateau reading holds, still Base to Bull down to Rs 410.57 Cr; the Bear case applies only below Rs 370.57 Cr".

| C1 element (loop-1 audit) | Required | Revised text | Cross-check | Status |
|---|---|---|---|---|
| 1. Revenue threshold vs 6A | H2 at or above 410.57 Cr is Base or better; Bear only below 370.57 Cr | L699: Base to Bull down to 410.57; Bear only below 370.57 | 6A L362: H2 needed 370.57 / 410.57 / 460.57. Recomputed in Section 2. | CLOSED |
| 2. Margin threshold vs 6B #1 | Bear case only at margin at or below ~12.5% | L698: "the Bear case applies only if operating margin is at or below ~12.5%" | 6B #1 L387: red "at or below ~12.5% (bear becomes working case)"; green "above ~14%"; 12.5-14% is AMBER | CLOSED |
| 3. Trigger 1 definition | Two legs only, no revenue leg | L698: "(two legs only)", margin ex-OI at or above 14% AND like-for-like debtor days lower | 0A L56 (two legs); 6B #1-#2 L387-L388; ex-OI basis governs L399; 8A-W L474 (Q4 tests both legs) | CLOSED |
| 4. Purpose of the 461-482 Cr test | Separates seasonal vs plateau reading; not a Bear line | L699: bull = seasonal reading holds; bear = plateau reading holds | Step 2 diag 1 L171-L173; Step 3 L217-L219; brief L651; 8A-W L474; M6 L555; YAML monitorable L754 | CLOSED |

Stale-copy sweep: a grep of the review for "461", "working case", "Bear case applies", "370.57", "410.57" and "460.57" finds no other copy of the old row (hits at REV L173, L219, L362, L387, L474, L555, L651, L698, L699, L754, L800, L822; all consistent). The A4 YAML (L701-L790) carries no forward-map entries.

C1: CLOSED.

Loop-1 STYLE S-L4 (Key Notes "+4.1%" label): applied at REV L616 ("H1 +4.1% vs H2 FY26; Q2 +16.7% vs H2 FY26 avg qtr"). Figures recomputed in Section 2. CLOSED.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASSES.

| Part | Heading in review | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" REV L634 | 17 lines (REV L635-L651), inside the 10-20 line band; bull and bear readings plus two separating observations (L649-L651). Unchanged in loop 2. | present |
| 2. Sector intelligence | "### 2. Sector intelligence" REV L653 | 7 lines (REV L654-L660). Unchanged. | present |
| 3. Business-model intelligence | "### 3. Business-model intelligence" REV L662 | 13 lines (REV L663-L675). Unchanged. | present |
| 4. Competition intelligence | "### 4. Competition intelligence" REV L677 | 7 lines (REV L678-L684). Unchanged. | present |
| 5. Forward map | "### 5. Forward map (next ~10-11 months)" REV L686 | Make-or-break line (L687) plus 9 catalyst rows (L691-L699), each with a dated or ND date, a bull fork and a bear fork. The loop-2 split adds one row; no fork is empty. | present |

---

## 1. COVERAGE AUDIT (light re-run; A1 inputs and ledgers unchanged since loop 1)

Method. (a) Fresh grep count of structured row IDs per document. (b) Fresh grep count of R/M rows in each ledger, read against the ledger headers. (c) Fresh grep of page and slide markers in the three fulltexts. (d) Loop-2 changed text checked for any removed citation.

| Document | Category | A2 count | Fresh count (A5) | Orphan rows | Status |
|---|---|---|---|---|---|
| RES | all structured IDs | 372 (ledger L2) | 372 (grep ^R### in structured) | none | PASS |
| RES | pages | 7 | 10 page markers = 7 [page N] + 3 image-transcription headers (pp 4, 6, 7) | none | PASS |
| RES | ledger rows | 372 IDs, grouped (ledger L2, L4-L13) | 172 ledger lines carry the 372 IDs (several IDs per line, e.g. ledger L21); header counts unchanged from loop 1 | none | PASS |
| PR | all structured IDs | 135 (ledger L3, L14) | 135 | none | PASS |
| PR | pages | 2 | 3 markers = 2 pages + 1 image-transcription header | none | PASS |
| PPT | all structured IDs | 665 (ledger L10, L15) | 665 | none | PASS |
| PPT | slides | 38 | 38 | none | PASS |
| PPT | ledger rows incl. M001 | 665 + 21 superseded-ID rows + M001 | 687 R/M rows (grep), same as loop 1 | none | PASS |
| PPT | missing_from_structured | 1 (M001, ledger L11, L20) | 1 | none | PASS |
| All | ledger rows cited in A4 or marked reviewed | 1,173 (REV L22) | 372 + 135 + 665 + 1 = 1,173 | none | PASS |
| All | loop-2 changed text | n/a | The old forward-map row cited no row ID. The Key Notes and YAML edits removed no citation. | none | PASS |

Coverage result: no orphan row, nothing missing from the ledger. Unchanged from loop 1.

---

## 2. ARITHMETIC AUDIT (loop-2 changed text only)

Each figure in the changed rows recomputed in Rs Mn from RES L412-L515 (image transcriptions govern). Tolerance: last displayed digit.

| Metric (review line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Seasonal band, H1 FY27 x 1.10-1.15 (L699) | Rs 461-482 Cr | 4,194.31 x 1.10 = 4,613.74 Mn; x 1.15 = 4,823.46 Mn (461.37-482.35 Cr) | RES L412 | PASS |
| H2 floor for Base (L699) | Rs 410.57 Cr | 8,300 - 4,194.31 = 4,105.69 Mn | RES L412; 6A L362 | PASS |
| H2 line for Bear (L699) | Rs 370.57 Cr | 7,900 - 4,194.31 = 3,705.69 Mn | RES L412; 6A L362 | PASS |
| "Base to Bull" upper edge vs the 461 split (L699) | below 461 = Base to Bull | Bull H2 = 8,800 - 4,194.31 = 4,605.69 Mn (460.57 Cr). H2 of 460.57-461.37 Cr is FY27 880.0-880.8 Cr, a hair above Bull. 0.8 Cr; rounding. | RES L412 | PASS (rounding) |
| Margin lines (L698) | 14%; ~12.5% | Thresholds, not computed. Match 0A L56, 6B #1 L387, 8B L480. | REV L56, L387 | PASS |
| Key Notes rev YoY (L616) | +79.6% | 2,350.92 / 1,309.20 = 1.7957 | RES L412 | PASS |
| Key Notes H1 vs H2 FY26 (L616) | +4.1% | H2 FY26 = 6,732.01 - 2,702.75 = 4,029.26; 4,194.31 / 4,029.26 = 1.0410 | RES L412 | PASS |
| Key Notes Q2 vs H2 FY26 avg qtr (L616) | +16.7% | 2,350.92 / 2,014.63 = 1.1669 | RES L412 | PASS |
| Key Notes op margin (L616) | 13.02% | 2,350.92 - 1,339.24 + 20.46 - 107.22 - 618.92 = 306.00; 306.00 / 2,350.92 = 13.016% | RES L412, L415-L417, L420 | PASS |
| Key Notes GM change (L616) | -232 bps | Q2 FY27 1 - 1,318.78 / 2,350.92 = 43.904%; Q2 FY26 1 - 704.01 / 1,309.20 = 46.226%; -232.2 bps | RES L412, L415-L416 | PASS |
| Key Notes H1 CFO/PAT (L616) | 14% | 47.28 / 331.63 = 14.26% | RES L496, L427 | PASS |
| Key Notes net debt (L616) | 88.9 Cr | 779.38 + 391.98 - 63.19 - 195.08 - 23.97 = 889.12 Mn | RES L447-L450, L458, L463 | PASS |

Arithmetic result: no mismatch above rounding.

---

## 3. ADVERSARIAL READ (loop scope: changed text only)

No new full pass on unchanged text (task scope). The changed text adds no new positive claim. One phrase leans positive: the L699 bear fork says H2 below Rs 461 Cr is "still Base to Bull down to Rs 410.57 Cr".
- Strongest counter from the extract: that grade is on revenue only. On the ex-unexplained-OI basis, H1 PAT is 32.10 Cr, between Bear (28.0) and Base (32.5) pro-rata (REV L374; RES L413, L427, L480, L483).
- Does it survive as a gap? No. The counter already sits in A4 at 6A reading 2 (L373-L379), 8A-W (L471), flag 10 (L626) and the YAML flags (L777). The row is a revenue test by its own label ("test 2: H2 FY27 revenue"). No graft needed.

Mandatory acquisition-economics probe: DOES NOT FIRE. The A1 inputs are unchanged. "Investment in shares" is nil in both halves (RES L503). The probe result from loop 1 stands.

Prior surviving counters A, B and C stay grafted (REV L171-L178, L217-L219, L373-L379); the loop-2 edits did not touch them.

---

## E. NEW FINDINGS ON CHANGED TEXT

No new FACTUAL, MISSING or CONTRADICTION finding.

Three STYLE notes (logged, no loop):
- S-L7 (carried from loop 1, now wider). The header still describes two part files. REV L3 says "change log at the end of part 2". REV L8 says "this file is part 1 ... The orchestrator concatenates part 1 then part 2". REV L34 says "Loop 1 change log at the end of part 2". The YAML review_path (L789) and the Loop 2 change log (L824) now say the review is one file. No number, fact or verdict changes. Fix at save: rewrite L3, L8 and L34 to describe one file.
- S-L8 (new). L698 and L699 each say "the Bear case applies only ...". Each "only" is scoped to its own test. A reader who takes the two rows together can read them as two exclusive conditions. 6B #1 and 6A give two routes to the Bear case: margin at or below ~12.5%, or H2 revenue below Rs 370.57 Cr. Fix: add "on this test" to each bear fork.
- S-L9 (new). The L699 bear fork leaves the H2 band Rs 370.57-410.57 Cr unlabelled. 6A (L362) puts that band between Bear and Base (FY27 Rs 790-830 Cr). The row already says Bear applies only below Rs 370.57 Cr, so no outcome is mislabelled. Fix: add "between Bear and Base from Rs 370.57 to 410.57 Cr".

Carried from loop 1, in unchanged text, still open, no loop: S-L1 (p15 Unit-V order), S-L2 (p24 "will double casting capacity" cite), S-L3 (REV L30 "R416-R438" vs R416-R435 cited), S-L5 (Q3 bear fork at REV L696 needs "with revenue below Q2"), S-L6 (REV L670 describes the 124-day cash cycle as including other current assets). S-L4 is closed.

---

## FINDINGS REGISTER (tagged)

| ID | Type | Finding | Line evidence | Loop |
|---|---|---|---|---|
| C1 (loop 1) | CONTRADICTION | Closed: rows split; thresholds match 6A and 6B #1 | REV L698-L699 vs L362, L387, L56, L173 | closed |
| S-L4 (loop 1) | STYLE | Closed: Key Notes "+4.1%" now labelled H1 | REV L616 | closed |
| S-L7 | STYLE | Header (L3, L8, L34) says two part files; YAML L789 and change log L824 say one file | REV L3, L8, L34, L789, L824 | none |
| S-L8 | STYLE | Two "the Bear case applies only" phrases can read as exclusive; add "on this test" | REV L698, L699; L387; L362 | none |
| S-L9 | STYLE | H2 band 370.57-410.57 Cr unlabelled; 6A grades it between Bear and Base | REV L699; L362 | none |

---

## VERDICT

VERDICT: COMPLETE.
- C1 is closed. The two forward-map rows keep trigger 1, the seasonal test and the Bear case apart. They agree with 6A (L362), 6B #1 (L387), Step 2 (L171-L173) and 8A-W (L474).
- The plain-language brief gate passes (all five parts present and non-empty).
- Coverage reconciles at 1,173 ledger rows, with no orphans and nothing missing from the ledger.
- Every figure in the changed text recomputes within rounding.
- Only STYLE findings remain (S-L7, S-L8, S-L9, plus open loop-1 STYLE items in unchanged text). They are logged and do not loop. loop_back_to is blank. The review may proceed to the Notion payload gate.

---

## STYLE NOTES (logged; no re-run)

- S-L7. Header L3, L8 and L34 still describe a part-1 / part-2 split; the YAML (L789) and the Loop 2 change log (L824) say one file. Rewrite the three header lines at save.
- S-L8. Add "on this test" to "the Bear case applies only" in L698 and L699, so the two routes to Bear (margin at or below ~12.5%; H2 below Rs 370.57 Cr) do not read as exclusive.
- S-L9. Label the H2 band Rs 370.57-410.57 Cr in L699 as "between Bear and Base" (6A L362).
- Carried open from loop 1 (unchanged text): S-L1, S-L2, S-L3, S-L5, S-L6.

---

```yaml
stage: A5-adversary
company: "KROSS"
quarter: "Q2 FY27"
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
    - "S-L7 (carried, wider): review header L3, L8, L34 still describe part 1 / part 2 files; YAML review_path L789 and Loop 2 change log L824 say one file. No number, fact or verdict changes."
    - "S-L8: forward-map L698 and L699 each say 'the Bear case applies only ...'; each 'only' is scoped to its test, but together they can read as exclusive. The two routes are margin at or below ~12.5% (6B #1, L387) and H2 revenue below Rs 370.57 Cr (6A, L362). Add 'on this test'."
    - "S-L9: L699 bear fork leaves H2 Rs 370.57-410.57 Cr unlabelled; 6A (L362) grades it between Bear and Base (FY27 Rs 790-830 Cr). No outcome is mislabelled."
    - "Carried open from loop 1, unchanged text: S-L1, S-L2, S-L3, S-L5, S-L6. S-L4 closed at L616."
loop_back_to: ""
gap: ""
style_notes:
  - "S-L7: rewrite review L3, L8, L34 to describe one file."
  - "S-L8: add 'on this test' to the two 'Bear case applies only' bear forks (L698, L699)."
  - "S-L9: label H2 Rs 370.57-410.57 Cr as between Bear and Base in L699."
  - "Loop-1 S-L1, S-L2, S-L3, S-L5, S-L6 remain open in unchanged text; optional at save."
analyst_note: "Loop 2 closes C1. The 30-May-2027 row is now two rows. Test 1 is trigger 1 on its two legs (margin ex-OI at or above 14%; like-for-like debtor days lower), with the Bear case only at margin at or below ~12.5%, as in 6B #1. Test 2 is H2 FY27 revenue against Rs 461-482 Cr (H1 x 1.10-1.15), seasonal vs plateau, with Base to Bull down to Rs 410.57 Cr and Bear only below Rs 370.57 Cr, as in 6A. All thresholds recompute from RES L412. The Key Notes relabel ties (+79.6%, +4.1%, +16.7%, 13.02%, -232 bps, 14%, 88.9 Cr). A grep finds no stale copy of the old row. Coverage is unchanged at 1,173 rows. Only STYLE remains. Pipeline note, not a finding: extracted/kross-concall-q2fy27-fulltext.md now exists. A5 did not read it. The Role 5 addendum can be scheduled against it."
```
