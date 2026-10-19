# A5 ADVERSARY / COMPLETENESS AUDIT, LOOP 1 RE-AUDIT: Tatva Chintan Pharma Chem Limited (TATVA), Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-20 | Loop 1 re-audit of the revised A4 review
Prior audit: runs/tatva-q2fy27/work/audit_tatva_q2fy27.md (INCOMPLETE: F1 FACTUAL, C1 CONTRADICTION, M1-M3 MISSING, S1-S7 STYLE).
Scope, set by the orchestrator: (1) confirm each prior item is closed; (2) re-run the deliverable-completeness gate; (3) check new or changed text for new FACTUAL, MISSING or CONTRADICTION errors, including the arithmetic (parent margin, SDA shares, FX-gain bounds). There is no new full adversarial pass on unchanged text.
Read: revised A4 review (839 lines, including the Loop 1 change log at REV L821-L838), A1 results fulltext (RES L140-L169, L198-L247, L260-L323, L440-L469), A1 presentation fulltext (PPT L155-L164, L600-L629, L1100-L1111), structured row counts, and the A2 ledger gate lines.
Not read: source PDFs, anything under inputs/, A3 forensics files, orchestrator commentary.

Anchors. REV L### = runs/tatva-q2fy27/work/review_tatva_q2fy27.md (revised). RES / PPT L### = A1 fulltext line. The filing is in Rs Mn, and Rs Cr = Mn x 0.1. Every recomputation starts from the Mn cell.

---

## PART A: PRIOR FINDINGS, CLOSURE CHECK

| Prior ID | Type | Required fix | Where A4 now carries it (REV line) | Check | Status |
|---|---|---|---|---|---|
| F1 | FACTUAL | CWIP +Rs 19.48 Cr restated as the 31-Mar to 30-Sep change, project split ND, and no Dahej-III attribution | L231 (diag 5 now attributes ST debt to "working capital and capex", not CWIP to Dahej-III); L285 ("CWIP Rs 42.83 Cr at 30-Sep, RES L203, project split ND"); L306; L314 ("CWIP build; project split ND"); L347 (exact correction text); L410, L441, L491 ("CWIP +Rs 19.48 Cr in H1 (project split ND)"); L582 and L758 (Q11 asks for the Dahej-III share) | A grep for "Dahej-III build", "groundbreaking" and "since the 20-Jul" finds no attribution left. The two remaining "groundbreak" hits are the guidance label (L441) and a memory-tagged milestone (L491). Neither ties CWIP to the project. RES L203: 428.27 vs 233.48 Mn = +194.79 Mn | CLOSED |
| C1 | CONTRADICTION | Guidance tally matches the 17 row statuses | L453 | Recount of L435-L451: delivered 1 (#7); ahead 1 (#1); behind 2 (#2, #3); far 1 (#14); near 1 (#15); consistent or on track 3 (#8, #10, #16); window open 1 (#11); not updated 1 (#4); unverifiable 1 (#5); not testable 5 (#6, #9, #12, #13, #17). Sum 17. Tally text matches | CLOSED |
| M1 | MISSING | FX-location counter beside the "core profit is real" and "95% core" claims | L209 (Step 2 verdict cell); L229 (diag 3); L233 (counter with bull reading, bear reading and separating observation); L283 (upper-bound qualifier); L503; L579 (Q8 asks the FX line); L626 (M15); L666 (brief narrative); L718 (forward map); L755, L783, L801 (YAML) | Arithmetic recomputed in Part C (rows 8-13) | CLOSED |
| M2 | MISSING | Parent-level counter beside "operating leverage offset the input-cost hit" | L227 (claim now scoped "At group level"); L228 (counter, two readings, separating observation M12, Q5, Q7); L689 (brief line; "Operating leverage is real" removed, and a grep finds no match); L800 (YAML flag) | Arithmetic recomputed in Part C (rows 1-7) | CLOSED |
| M3 | MISSING | SDA one-quarter and MGMT-attribution qualifier; monitorable; forward-map row | L408 (6B #3 "GREEN on revenue; new-customer leg ND; one quarter"); L486 (counter); L490 (trigger "FIRED on revenue (one quarter, MGMT attribution); durability unproven"); L514; L585 (Q14); L636 (M25); L644; L680 (brief sector line); L697; L716 (forward-map row with both forks); L761, L793, L802 (YAML) | Arithmetic recomputed in Part C (rows 14-21) | CLOSED |
| S1 | STYLE | "no cause named" | L643, L674 | Matches NTC L39-40 wording intent | CLOSED |
| S2 | STYLE | "Working capital, mainly stock and customer dues, absorbed 99%" | L668 | | CLOSED |
| S3 | STYLE | Call-script reading tagged [INFERENCE] | L86, L555 | | CLOSED |
| S4 | STYLE | LABEL_ANOMALY (R1005, R1040) disposed by name | L22 "Reviewed, no finding" | | CLOSED |
| S5 | STYLE | One-file self-description | L6, L816 | | CLOSED |
| S6 | STYLE | FY26 Rs 4.00 Cr investment named as ND | L315 | RES L207 40.00 / 40.00 Mn; RES L295 (40.00) FY26; 40.00 / 8,146.51 = 0.491% | CLOSED |
| S7 | STYLE | A2 presentation count test should grep the fulltext | A2-side; A4 cannot fix it (L836) | Carried as a note for A2's next run | OPEN (A2, next run; no loop) |

All five loop-triggering items (F1, C1, M1, M2, M3) are closed.

---

## AUDIT 0: DELIVERABLE-COMPLETENESS (hard gate, re-run)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (REV L664-L676, six paragraphs, about 310 words, within 200-400) | sector PRESENT (REV L678-L684) | business model PRESENT (REV L686-L692) | competition PRESENT (REV L694-L699) | forward map PRESENT (REV L701-L719: make-or-break reading plus 13 catalysts, each with a bull fork and a bear fork; 11 dated; 2 undated because no date exists: the call reschedule, NTC L39-40, and operator rulings 50/51).

Gate result: PASS. All five parts carry real content. The new M25 row (L716) is dated (by 14-Feb-2027) and carries both forks.

---

## AUDIT 1: COVERAGE (re-confirmation)

The ledgers and extracts are the loop-0 inputs. I re-ran the count spine with my own grep to confirm that nothing moved.

| Doc | Category | A2 count | A5 fresh count (method) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | structured row IDs | 1,090 (ledger L12, L15) | 1,090 (grep "^R\d+ \|" on the structured file) | 0 | PASS |
| Results | pages | 14 | 14 ("[page N]" in the fulltext) | 0 | PASS |
| Results | line items, notes, ZERO_STANDING, agenda, auditor paras, entities | 241 / 13 / 69 / 1 / 10 / 3 | unchanged from loop 0 (audit_tatva_q2fy27.md rows 25-31); extracts unchanged (ID and page counts identical) | 0 | PASS |
| Presentation | structured row IDs | 738 (ledger L16) | 738 (grep) | 0 | PASS |
| Presentation | slides | 42 | 42 ("[page N]") | 0 | PASS |
| Notice | structured row IDs | 28 (ledger L10) | 28 (grep) | 0 | PASS |
| Notice | pages | 1 | 1 | 0 | PASS |
| All | ledger rows absent from A4 | n/a | 0. REV L16 still declares all 1,856 IDs reviewed (1,090 + 738 + 28 = 1,856, matching my grep). The 13 notes are at REV L57-L65. The LABEL_ANOMALY flag, the only A2 flag left without a named disposition at loop 0, is now disposed at REV L22 | 0 | PASS |

Coverage result: PASS. Orphan rows: none. Rows my pass found that the ledgers lack: none.

---

## AUDIT 2: ARITHMETIC (new and changed text only)

Tolerance is plus or minus 1 in the last printed digit. Loop-0 rows 1-72 are unchanged; the change log confirms no table number moved (REV L838).

| # | Metric (REV line) | A4 value | Recomputed (Mn inputs) | Source line | Status |
|---|---|---|---|---|---|
| 1 | Parent materials / revenue, Q2 FY26 to Q2 FY27 (L228) | 44.59% to 52.69%, +810 bps | (619.87 - 103.22) / 1,158.63 = 44.591%; (1,140.51 - 47.30) / 2,074.84 = 52.689%; +809.7 bps | RES L447, L451, L452, L453 | PASS |
| 2 | Parent employee cost / revenue change (L228) | -411 bps | 149.47 / 1,158.63 = 12.901%; 182.30 / 2,074.84 = 8.786%; -411.4 bps | RES L447, L454 | PASS |
| 3 | Parent other expenses / revenue change (L228) | -82 bps | 281.42 / 1,158.63 = 24.289%; 487.00 / 2,074.84 = 23.472%; -81.7 bps | RES L447, L457 | PASS |
| 4 | Parent op EBITDA margin change (L228) | -317 bps | 18.219% to 15.053% = -316.6 bps (cross-check: (204.37 + 107.92 + 27.09 - 27.05) / 2,074.84 = 15.053%) | RES L447-L459 | PASS |
| 5 | Parent cost leverage (L800) | -493 bps | 411.4 + 81.7 = 493.1 bps | RES L454, L457 | PASS |
| 6 | Subsidiary PAT gap, H2 FY26 (L228) | Rs 0.48 Cr | (420.54 - 390.82) - (165.68 - 140.74) = 29.72 - 24.94 = 4.78 Mn | RES L164, L466 | PASS |
| 7 | Brief: group staff and other each fell about 1.6 points QoQ; factory materials +8.1 points YoY (L689) | 1.6 / 1.6 / 8.1 | employee 10.018% to 8.388% = -1.630 pp; other 25.580% to 23.997% = -1.583 pp; parent materials +8.097 pp | RES L145, L152, L155; row 1 | PASS |
| 8 | H1 unrealised FX gain (L233, L666) | Rs 3.91 Cr | 39.06 Mn (gain) | RES L268 | PASS |
| 9 | FX gain share of H1 core PBT (L233, L801) | 8.3% of Rs 46.84 Cr | 513.69 - 45.34 = 468.35 Mn; 39.06 / 468.35 = 8.34% | RES L146, L157, L268 | PASS |
| 10 | H1 FY26 unrealised FX loss (L233) | Rs 0.43 Cr | 4.26 Mn (loss) | RES L268 | PASS |
| 11 | FX swing (L233) | up to Rs 4.33 Cr | 39.06 + 4.26 = 43.32 Mn | RES L268 | PASS |
| 12 | H1 core-PBT increase (L233) | Rs 26.23 Cr | 468.35 - (227.64 - 21.63) = 468.35 - 206.01 = 262.34 Mn | RES L146, L157 | PASS |
| 13 | Swing share of the increase; "one-sixth" (L233, L801) | 16.5% | 43.32 / 262.34 = 16.51% (one-sixth = 16.67%) | RES L146, L157, L268 | PASS |
| 14 | H1 SDA revenue and share (L408, L486) | Rs 154.6 Cr; 40% | 1,546 Mn (PPT L614); "40% of Revenue" under H1FY27 (PPT L623); 1,546 / 3,843.75 = 40.22% | PPT L614, L623; RES L145 | PASS |
| 15 | FY26 SDA quarterly average (L486) | Rs 51.1 Cr | 2,045 / 4 = 511.25 Mn | PPT L614 | PASS |
| 16 | Q2 SDA from filed share only (L486) | about Rs 97-99 Cr | 44.5-45.5% x 2,173.20 = 967.1-988.8 Mn | PPT L1106; RES L145 | PASS |
| 17 | Q1 SDA from filed values only (L486) | about Rs 56-58 Cr | 1,546 - 988.8 to 1,546 - 967.1 = 557.2-578.9 Mn | PPT L614, L1106 | PASS |
| 18 | Q1 SDA share (L486, L490, L585, L680, L802) | about 34% | 557.2-578.9 / 1,670.55 = 33.4-34.7% (6D memory value 57.8: 34.6%) | RES L145 | PASS |
| 19 | SDA H1 vs FY26 (L490) | 76% | 1,546 / 2,045 = 75.6% | PPT L614 | PASS |
| 20 | 6B #3 derived Q2 / Q1 SDA (L408) | about Rs 97 / about Rs 57 Cr | 6D table (L478): 96.8 / 57.8. 96.8 rounds to 97; 57.8 rounds to 58, not 57 | REV L478 | PASS on substance (57 lies inside the filed-only range of row 17); wording logged as STYLE L2 |
| 21 | M25 and forward-map thresholds (L636, L716) | about Rs 97 Cr; share 45%; fall-back toward Rs 55-60 Cr | rows 16-17 | PPT L614, L1106 | PASS |
| 22 | CWIP, PPE (L285, L314, L347) | 23.35 to 42.83, +19.48; PPE -15.22 | 233.48 to 428.27 Mn, +194.79; 5,741.83 - 5,589.61 = 152.22 Mn | RES L201, L203 | PASS |
| 23 | ST borrowings rise (L231) | +Rs 50.17 Cr | 1,655.30 - 1,153.63 = 501.67 Mn (cash-flow net proceeds 501.27 Mn, L317, used at REV L323; the two lines are cited separately) | RES L240, L317 | PASS |
| 24 | H1 capex (L347) | Rs 30.85 Cr | 308.45 Mn | RES L291 | PASS |
| 25 | Investment share of equity (L315) | 0.49% | 40.00 / 8,146.51 = 0.491% | RES L207, L230, L295 | PASS |
| 26 | Guidance tally (L453) | 17 items, 10 buckets | see Part A, C1 | REV L435-L451 | PASS |

Arithmetic result: no mismatch above rounding in any new or changed cell.

---

## AUDIT 3: ADVERSARIAL READ (scoped to new and changed text)

Scope. The three loop-0 claims (core profit real; operating leverage offset; SDA FIRED/GREEN) now carry their counters. I checked each graft for adequacy and checked whether the revision added any new positive claim.

1. "Core profit is real" (L229, L666). The counter is grafted at L233 and L283, and in the brief. It has both readings, the H1 bounds, and a separating observation (L233; Q8 L579; M15 L626; forward map L718). Adequate. One precision point is logged as STYLE L1: "upper bound" (L283) holds on the H1 evidence, but the Q2 FX split is ND for both Q2 FY27 and Q2 FY26. Strictly, the Q2 share is conditional, not bounded. The bear direction on H1 data supports the conservative wording, and no number or conclusion changes. This wording came from the loop-0 A5 correction text.
2. "Operating leverage offset the input-cost hit" (L227). The claim is now scoped "At group level". The parent counter is grafted at L228 with two readings and a separating observation (M12, Q5, Q7). The brief line "Operating leverage is real" is gone; L689 now states the factory result. Adequate.
3. "SDA FIRED / GREEN" (L408, L490). Both statuses are qualified. The counter is at L486. M25 (L636), the forward-map row (L716), Q14 (L585) and the brief sector line (L680) are present. Adequate.

New positive claims introduced by the revision: none. The new "Bull reading" sentences (L228, L233) are each paired with a bear reading and a separating observation.

Mandatory acquisition-economics probe: unchanged from loop 0. No business acquisition or stake buy appears in Q2 or H1 FY27 (RES L295: nil in the 30.09.2026 column). The FY26 Rs 4.00 Cr non-current investment (RES L207, L295) has no named investee or earnings, so price / target PAT is not computable. A4 now names it as ND (L315). The revision makes no "cheap, accretive acquisition" claim.

Surviving bear counters needing a graft: none.

---

## FINDINGS REGISTER (loop 1)

| ID | Type | Finding | Lines | Loop |
|---|---|---|---|---|
| L1 | STYLE | "This share is an upper bound" (95% core share of the Q2 YoY PAT change). The bound holds on the H1 evidence (H1 net FX gain 39.06 Mn vs H1 FY26 net loss 4.26 Mn), but the Q2 FY27 and Q2 FY26 FX splits are ND. Suggested wording: "an upper bound on the H1 evidence; the Q2 split is ND". This traces to A5's own loop-0 correction text. No number or conclusion changes | REV L283; RES L268 | none |
| L2 | STYLE | 6B #3 says "Q1 about Rs 57 Cr", but the 6D derived Q1 value is 57.8 (rounds to 58). The value still lies in the filed-only range of Rs 55.7-57.9 Cr. Write "about Rs 58 Cr" or "about Rs 56-58 Cr" (as at L486) | REV L408, L478, L486 | none |
| L3 | STYLE | Provenance tag. The brief's key (L662) tags deck values MGMT, not FILED. L680 says "[INFERENCE from FILED deck values]" and L486 says "From filed figures alone". Both rest on PPT L614, L623 and L1106. Write "[INFERENCE from MGMT deck values]". L486 wording traces to A5 loop-0 text | REV L486, L662, L680 | none |
| L4 | STYLE | The diag 6 separating observation (L233) names only the FY27 annual report and Q8. M15 (L626) already names the FY26 AR as the check "now". Add the FY26 AR FX-presentation note as the earliest check in L233, so the two cells agree on timing | REV L233, L626 | none |
| S7 | STYLE (carried) | A2's presentation count test takes its grep side from A1 header totals (LED-P L17). A2 should grep the fulltext in the next run | LED-P L17 | none (A2, next run) |

No FACTUAL, MISSING or CONTRADICTION finding.

---

## VERDICT

**COMPLETE.** All five loop-triggering findings from loop 0 (F1, C1, M1, M2, M3) are closed, and S1-S6 are applied. The deliverable gate passes: all five brief parts are present, and the forward map has 13 rows with bull and bear forks. Coverage is clean: 1,856 structured IDs, no orphan rows and nothing missing from the ledgers. Every new or changed number recomputes within rounding, including the parent bridge (+810 / -411 / -82 / -317 bps), the SDA derivations (Q2 Rs 96.7-98.9 Cr, Q1 Rs 55.7-57.9 Cr, Q1 share 33.4-34.7%) and the FX bounds (8.34%, 16.51%). Four new STYLE notes are logged with no re-run. The review may proceed to the Notion save gate.

---

## STYLE NOTES (logged; no re-run)

- L1. REV L283: write "an upper bound on the H1 evidence; the Q2 split is ND" (RES L268).
- L2. REV L408: "Q1 about Rs 57 Cr" should read "about Rs 58 Cr" (6D 57.8) or "about Rs 56-58 Cr".
- L3. REV L680 and L486: deck values are MGMT under the review's own key (L662), not FILED.
- L4. REV L233: name the FY26 AR FX-presentation note as the earliest separating check, as M15 (L626) does.
- S7 (carried). A2 should grep the presentation fulltext for its count test (LED-P L17).

---

```yaml
stage: A5-adversary
company: "TATVA"
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
    - "L1: REV L283 '95% core share is an upper bound' holds on H1 evidence (H1 FX gain 39.06 Mn vs H1 FY26 loss 4.26 Mn, RES L268); Q2 FX split ND, so for the Q2 change the share is conditional. Reword; no number changes."
    - "L2: REV L408 'Q1 about Rs 57 Cr' vs 6D derived 57.8 (L478), which rounds to 58; within filed-only range Rs 55.7-57.9 Cr."
    - "L3: REV L680 '[INFERENCE from FILED deck values]' and L486 'From filed figures alone' mis-tag deck values; the review key (L662) tags the deck MGMT."
    - "L4: REV L233 separating observation names only the FY27 AR and Q8; M15 (L626) names the FY26 AR as the check now. Align."
    - "S7 (carried from loop 0): A2 presentation count test grep side is A1 header totals (LED-P L17); A2 to grep the fulltext next run."
loop_back_to: ""
gap: ""
style_notes:
  - "L1: write 'an upper bound on the H1 evidence; the Q2 split is ND' (REV L283; RES L268)."
  - "L2: 'Q1 about Rs 58 Cr' or 'about Rs 56-58 Cr' (REV L408; 6D L478)."
  - "L3: tag deck-derived SDA inference MGMT, not FILED (REV L486, L680; key L662)."
  - "L4: name the FY26 AR FX-presentation note as the earliest separating check in diag 6 (REV L233; M15 L626)."
  - "S7: A2 should grep the presentation fulltext for its count test (LED-P L17)."
analyst_note: "Loop 1 closes every loop-0 trigger. F1: CWIP is now an H1 change with project split ND at all nine sites, and no Dahej-III attribution survives a grep. C1: the tally matches the 17 row statuses. M1-M3 are grafted beside each bull claim with both readings and a separating observation; M25 and its forward-map row exist. New arithmetic recomputes from Mn cells. Parent bridge: materials +809.7 bps, employee -411.4, other -81.7, margin -316.6 bps. SDA from filed deck values only: Q2 Rs 96.7-98.9 Cr, Q1 Rs 55.7-57.9 Cr (33.4-34.7% share). FX bounds: 8.34% of H1 core PBT; the swing is 16.51% of the H1 core-PBT increase. Coverage spine unchanged at 1,856 IDs. The four new STYLE notes are wording precision; two (L1, L3) trace to A5's own loop-0 correction text, so they are logged rather than looped."
```
