# A5 ADVERSARY AUDIT: HFCL Q2 FY27, ROLE 5 LOOP 2 FINAL RE-AUDIT (concall 19-Oct-2026)

Model: claude-opus-5-5. Audit date: 2026-10-20. Fresh context.
Prior audit: runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_role5_loop1.md (INCOMPLETE: NF1 FACTUAL, NM1 MISSING; NS1-NS6 STYLE).
Scope (task message): this run checks closure only. (1) It confirms NF1 and NM1 are closed at every site the loop-1 audit named. (2) It re-runs the deliverable-completeness gate. (3) It checks only the loop-2 changed text for new FACTUAL / MISSING / CONTRADICTION errors. It does not run a new adversarial pass on unchanged text.
Inputs read: the A4 review (Role 5 loop-2 change log RV-L2118-2128; every changed site listed below; brief RV-L1916-1975; YAML RV-L2016-2017, RV-L2060, RV-L2070-2071, RV-L2081); concall fulltext C-L166-177, C-L248-281, C-L710-715, C-L764-773; concall ledger (count test L15-16, section 12 L723-738); A4 block blocks/a4-role5.yaml (alignment grep only); the loop-1 joined part file (grep only, a regression check). Not read: any source file, anything under inputs/, any A3 file.
Anchors: C-L### = concall fulltext line. RV-L### = review_hfcl_q2fy27.md line (current numbering; loop-1 sites have shifted by +1 to +2 lines). M## = A2 MISSING_FROM_STRUCTURED row.
Source caveat: the source is a machine transcript and speakers are inferred. Filed numbers win on any conflict.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate, run first)

DELIVERABLE-COMPLETENESS: PASS. Brief (6), RV-L1916-1975:
- (1) Summary narrative: PRESENT (RV-L1920-1930). Five paragraphs, about 340 words, inside the 200-400 band. This part was not changed in loop 2.
- (2) Sector intelligence: PRESENT (RV-L1932-1940). The defence paragraph RV-L1940 changed in loop 2 (NM1).
- (3) Business-model intelligence: PRESENT (RV-L1942-1950).
- (4) Competition intelligence: PRESENT (RV-L1952-1960). The strengths paragraph RV-L1958 changed in loop 2 (NF1).
- (5) Forward map: PRESENT (RV-L1962-1975). It has a make-or-break reading and 10 dated catalysts, each with a bull fork and a bear fork. Unchanged.

---

## 1. PRIOR-FINDING CLOSURE

### NF1 (FACTUAL): hyperscaler 39.90% must read as the ceiling of the export-orders reading

Source check: C-L170-172: "out of 18,500 crore large portion would be from hyperscalers ... I do not have the exact number but yeah maybe 70 percent ... of the export orders". So 0.70 x export share of book (57%, P-L314 via Role 4) = 39.90% is a ceiling on that reading.

| Site named in loop-1 audit | Current line | Loop-2 text (abridged) | Status |
|---|---|---|---|
| 8A trigger 1 | RV-L1665 | "up to 39.90% of the total book if the 70% applies only to export orders (a ceiling; the share may be lower), or 44.81% if it applies to the whole Rs18,500 Cr" | CLOSED |
| 9B net impact | RV-L1788 | "hyperscalers are up to 39.90% of the book if the 70% applies only to export orders (a ceiling; the share may be lower), or 44.81% if it applies to the whole Rs18,500 Cr" | CLOSED |
| 9B Key Notes line (Notion save) | RV-L1790 | "Hyperscalers ~70% of export orders (up to 39.90% of book on that base, may be lower; 44.81% only if the 70% covers the whole Rs18,500 Cr)" | CLOSED |
| Brief part 4 | RV-L1958 | "On that base, hyperscalers are at most 39.90% of the total book, and may be less (computed). Only if the 70% applies to the whole Rs18,500 Cr do they reach 44.81% (computed)." | CLOSED |
| YAML flag | RV-L2070 | "up to 39.90% if the 70% applies only to export orders ... (a ceiling, the share may be lower); 44.81% only if it applies to the whole Rs18,500 Cr" | CLOSED |
| YAML analyst_note | RV-L2081 | "hyperscalers are at most 39.90% of the book on that base, and may be less; 44.81% assumes the whole book" | CLOSED |

Residual check: a grep of "39.90" and "44.81" over the whole review finds no remaining "39.90%-44.81%" floor-style range. 5A (RV-L1512) and 8D (RV-L1714) are unchanged and were already correct ("caps", "cap"). YAML hyperscaler_share_of_book (RV-L2016) is also unchanged and correct. MQ57 (RV-L1814) reads "39.90% vs 44.81% ... depends on the base", which is a comparison, not a floor. A4's block (blocks/a4-role5.yaml L35, L89) matches the review. Arithmetic unchanged: 0.70 x 0.57 = 0.3990; 12,950 / 28,900 = 44.81%.
Regression check: "I do not have the exact number" appears at 4 sites in both the loop-1 joined file and the current review (RV-L1369, RV-L1395, RV-L1512, RV-L1585). Loop 2 dropped none.

NF1: CLOSED.

### NM1 (MISSING): MD's C-L278-279 confidence line beside "aspiration" / "possibly"; remove "not a target"

Source check: C-L251-253 "next year we look at least 2000 crores, in expiration, if you take it in three years time frame to 5000 crores". C-L278-279 "So overall it should not be difficult for us to reach the 2000 crores figure and a 5000 crores figure." C-L769-770 "we have to do 2,000 crores and possibly 5,000 crores in next two years". C-L713 (analyst) "your aspirations".

| Site named in loop-1 audit | Current line | Loop-2 text (abridged) | Status |
|---|---|---|---|
| 9A #22 (register, Q3 FY27 scoring input) | RV-L1768 | A4 classification ASPIRATION [INFERENCE from C-L252, C-L713, C-L770]; three framings quoted with C-L252-253, C-L278-279, C-L770; "the scorer weighs all three framings"; source_ref adds C-L278-279 | CLOSED |
| 6D | RV-L1604 | Aspiration ("in expiration", C-L252) and "possibly" (C-L770), analyst "your aspirations" (C-L713), and "Between those two framings ... 'it should not be difficult ...' (C-L278-279)" | CLOSED |
| Step 2 defence row | RV-L1291 | Three framings quoted; "[INFERENCE: A4 classification ... weighed against the MD's 'should not be difficult', C-L278-279]" | CLOSED |
| 5A defence row | RV-L1507 | Three framings quoted; "A4 reads Rs5,000 Cr as an aspiration ... [INFERENCE], though the MD also said it 'should not be difficult' to reach (C-L278-279)" | CLOSED |
| N18 | RV-L1896 | "A4 classification: ASPIRATION ... [INFERENCE]; MD framings: C-L252; C-L278-279; C-L770"; source C-L252-253, C-L278-279, C-L770 | CLOSED |
| YAML defence_5000 | RV-L2017 | A4 classification INFERENCE; C-L278-279 quoted in full | CLOSED |
| YAML monitorable, flag, analyst_note (added by A4 beyond the named list) | RV-L2060, RV-L2071, RV-L2081 | Each carries C-L278-279 or "should not be difficult" | CLOSED |
| Brief part 2 ("not a target" attribution) | RV-L1940 | "The MD framed about Rs5,000 Cr in three ways ... First he called it an aspiration ('in expiration') over three years. Then he said it 'should not be difficult' to reach. Later he said 'possibly' within two years. We read it as an aspiration, not a commitment (INFERENCE)." | CLOSED |

Residual check: a grep for "not a target" over the review finds it only in the change log (RV-L2125). The order first / then / later matches C-L252, C-L278, C-L770. The horizon "2 or 3 years (FY29 or FY30)" follows from a 19-Oct-2026 call plus 2 years (Oct-2028, FY29) or 3 years (Oct-2029, FY30). A4's block (L36, L79, L90) matches the review.

NM1: CLOSED.

---

## 2. COVERAGE AUDIT (concall; loop 2 changed A4 text only)

A1 and A2 did not re-run in loop 2. The ledger count test still reads missing_from_structured 14, gate_a2 pass (ledger L15-16). Section 12 holds M01-M14 (ledger L725-738), the same list the loop-1 audit verified at line.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Fulltext / structured | unchanged since loop 1 (A1 not re-run) | loop-1 fresh pass stands (193 digit lines, 132 number-word lines; no material unit missing) | n.a. | PASS |
| MISSING_FROM_STRUCTURED | 14 | 14 (ledger L725-738) | 0 | PASS |
| Ledger rows total | 629 | 629 (615 structured IDs + 14 M rows; unchanged) | 0 | PASS |
| M rows cited in the A4 Role 5 addendum after the loop-2 rewrite | 14 | 14. M01 RV-L1400; M02 RV-L1578, RV-L1667, RV-L1764, RV-L1883; M03 RV-L1483, RV-L1486, RV-L1515; M04 RV-L1578, RV-L1779; M05 RV-L1428; M06 RV-L1431; M07 RV-L1431, RV-L1578, RV-L1752; M08 RV-L1441, RV-L1476; M09 RV-L1443, RV-L1475, RV-L1478, RV-L1866; M10 RV-L1443, RV-L1478; M11 RV-L1449; M12 RV-L1406; M13 RV-L1433; M14 RV-L1440 | 0 | PASS |

Orphan rows: none. Missing from ledger: none.

---

## 3. ARITHMETIC AUDIT (loop-2 changed text)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Hyperscaler ceiling, export-orders reading | up to 39.90% of book | 0.70 x 0.57 = 0.3990 | C-L171-172; P-L314 via RV-L152 | PASS |
| Hyperscaler, whole-book reading | 44.81% | 0.70 x 18,500 = 12,950; / 28,900 = 44.81% | C-L170-172 | PASS |
| Defence horizon | FY29 or FY30 | 19-Oct-2026 + 2 years = FY29; + 3 years = FY30 | C-L252-253, C-L770 | PASS |

Loop 2 introduced no new numbers. Arithmetic mismatches above rounding: none.

---

## 4. CHANGED-TEXT CHECK (new FACTUAL / MISSING / CONTRADICTION)

I read every loop-2 changed site against the fulltext lines.
- Quotes: each quotation of C-L252-253, C-L278-279 and C-L769-770 is verbatim, or a marked ellipsis of the verbatim text. "[aspiration]" is a bracketed gloss of the ASR "in expiration", and the classification is tagged INFERENCE everywhere it appears.
- Attribution: no changed site attributes words the MD did not say. "We read it as an aspiration, not a commitment (INFERENCE)" is A4's own call, labelled as such.
- Consistency: the changed sites agree with each other, with the unchanged 5A / 8D / YAML hyperscaler fields, and with A4's block. No ruling, verdict field or number changed. Tripwire #4 FIRED (silence limb) with the AVOID proposal; trigger #6 NOT FIRED with an imminent test; PROCEED WITH FLAGS; INDETERMINATE-WITH-DIRECTION.
- New FACTUAL: none. New MISSING: none. New CONTRADICTION: none.

Adversarial read: the task scope excludes a new pass on unchanged text. The three positive claims stay bounded as verified in loop 1 (RV-L1788). No surviving bear counter is open.

---

## 5. FINDINGS BY TYPE

FACTUAL
- none (NF1 closed).

MISSING
- none (NM1 closed).

CONTRADICTION
- none.

STYLE (logged only, no loop)
- NS1-NS6: carried from the loop-1 audit. Per the loop-2 change log (RV-L2120), A4 did not apply them. They stay logged for the next run.
- NS7: unchanged shorthand. Several sites still call the Rs5,000 Cr figure an "aspiration" and cite only C-L252 / C-L770, not C-L278-279: 0D RV-L1224; T018 RV-L1398; 3B RV-L1557; 7C RV-L1650; 8A #5 RV-L1669; 8D RV-L1714 ("as an aspiration only"); MQ46 RV-L1803. None of these was an NM1 site. The register, scoring line, brief and YAML carry all three framings. Optional: tag these "(A4 classification)" and drop "only" at 8D.
- NS8: unchanged range format. 8D RV-L1714 and YAML hyperscaler_share_of_book RV-L2016 (block L35) still write "39.90% (lower reading, cap) to 44.81% (upper reading)". They are labelled "cap", so the loop-1 audit judged them correct. Optional: use the "up to 39.90% ... ; 44.81% only if ..." wording of the NF1 sites, for one form throughout.

---

## 6. VERDICT

VERDICT: COMPLETE. Only STYLE findings remain. loop_back_to "".
- NF1 is CLOSED at all six named sites. NM1 is CLOSED at all seven named sites and at three extra YAML sites. The "not a target" attribution is removed.
- The deliverable-completeness gate passes; all five brief parts are present.
- Coverage passes: 629 ledger rows, M01-M14 each cited, no orphan rows.
- No arithmetic mismatches.
- Loop 2 introduced no new FACTUAL, MISSING or CONTRADICTION error.
- Rulings unchanged: tripwire #4 FIRED (silence limb) with the AVOID proposal, which the operator decides; trigger #6 NOT FIRED with an imminent test.

---

```yaml
stage: A5-adversary
company: "HFCL"
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
    - "NS1-NS6 carried from loop-1 audit, not applied by A4 (RV-L2120); logged for next run"
    - "NS7 unchanged shorthand 'aspiration' citing only C-L252/C-L770 at 0D RV-L1224, T018 RV-L1398, 3B RV-L1557, 7C RV-L1650, 8A #5 RV-L1669, 8D RV-L1714 ('only'), MQ46 RV-L1803; register, brief and YAML carry all three framings incl. C-L278-279; optional '(A4 classification)' tag"
    - "NS8 unchanged range format '39.90% (lower reading, cap) to 44.81%' at 8D RV-L1714 and YAML RV-L2016 (block L35); labelled cap so correct; optional harmonise to the NF1 'up to 39.90% ...; 44.81% only if ...' wording"
loop_back_to: ""
gap: ""
style_notes:
  - "NS1-NS6 carried (anchors; Reading B 'only'; capacity flag wording; mix-shift cites; A1 enumeration rule; A3 file lacks M01-M14)"
  - "NS7 residual 'aspiration' shorthand without C-L278-279 at unchanged sites"
  - "NS8 residual 'cap to' range format at 8D and YAML hyperscaler_share_of_book"
analyst_note: "Loop 2 closes both open items. NF1: all six named sites now say hyperscalers are up to 39.90% of the book on the export-orders reading (C-L171-172), a ceiling that may be lower. 44.81% applies only if the 70% covers the whole Rs18,500 Cr. No floor-style range remains, and the Notion Key Notes line is fixed. NM1: the MD's 'should not be difficult ... a 5000 crores figure' (C-L278-279) now sits beside 'in expiration' (C-L252-253) and 'possibly' (C-L770) at all named sites and three extra YAML fields. The aspiration reading is labelled as A4's INFERENCE, and 'not a target' is gone from brief part 2. All quotes match the fulltext. A4's block matches the review. No number, ruling or verdict field changed. Coverage holds at 629 rows with M01-M14 cited. The brief gate passes. Two optional STYLE harmonisations are logged on unchanged text."
```
