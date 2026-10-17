# A5 ADVERSARY / COMPLETENESS RE-AUDIT (CORRECTION LOOP 1): Tata Communications Limited (TATACOMM), Q2 FY27

Review under audit: runs/tatacomm-q2fy27/work/review_tatacomm_q2fy27.md, revised in correction loop 1 (887 lines, change log at rev L762-785).
Prior audit: runs/tatacomm-q2fy27/work/audit_tatacomm_q2fy27.md (loop 0, verdict INCOMPLETE, loop to A4).
Inputs: unchanged A1 fulltexts, A1 structured files and A2 ledgers; the revised A4 review. No source PDF, nothing under inputs/, no A3 file opened.
Model: claude-opus-5-5. Re-audit date 2026-10-17.

Anchors as in loop 0. "L###" = results fulltext line; "P-L###" = deck fulltext line; "rev L###" = line in the revised review.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading (revised) | Content | Status |
|---|---|---|---|
| 1. Summary narrative | rev L716 | 16 lines, one sentence per line (rev L718-733), inside the 10-20 line band | PRESENT |
| 2. Sector intelligence | rev L735 | rev L737 | PRESENT |
| 3. Business-model intelligence | rev L739 | rev L741, now with the Campaign Registry base effect and the associate yield | PRESENT |
| 4. Competition intelligence | rev L743 | rev L745 | PRESENT |
| 5. Forward map | rev L747 | Make-or-break reading plus 9 catalysts, each with a Bull and a Bear fork (rev L749-758) | PRESENT |

Gate result: PASS.

---

## 1. COVERAGE AUDIT

The A1 and A2 inputs did not change, so my loop-0 fresh enumeration still stands. I re-checked that the revised review keeps every ledger unit.

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Results notes | 18 | 18 (19 note units, reconciled as in loop 0) | none | PASS |
| Results footnotes | 28 (+3 unresolved) | 28 | none | PASS |
| Results line-item rows / cells | 356 / 1,260 | 356 (339 decimal-bearing + 17 label or dash rows) / 1,260 | none | PASS |
| ZERO_STANDING cells | 87 | 87 | none | PASS |
| Agenda items | 3 | 3 | none | PASS |
| Auditor paragraphs | 11 | 14 numbered + board-letter line; basis difference only | none | PASS |
| Entities (list / total) | 75 / 132 | 75 / 132 | none | PASS |
| ENTITY_CHANGE | 10 | 10 | none | PASS |
| Dates / forward / signatures | 71 / 32 / 4 | 71 / 32 / 4 | none | PASS |
| Structured IDs (results / deck) | 1,778 / 74 | 1,778 / 74 | none | PASS |
| Deck slides / numbers / entities / forward / dates / qualifiers | 9 / 33 / 25 / 3 / 7 / 6 | 9 / 33 / 25 / 3 / 7 / 6 | none | PASS |
| Turns | 0 | 0 | n/a | n/a |

Ledger to review:
- Notes: all 18 are still in the 0D table (rev L65-83).
- Slides: 6 are cited. Slides 2, 3 and 9 now carry an explicit "reviewed, no finding" (rev L22).
- Flags A2 raised that loop 0 found without a disposition now have one-line dispositions (rev L22): SIGNATURE_BEFORE_MEETING_END, ENTITY_CHANGE R1482, R1495, R1514, R1518, and ANONYMISED_CLIENT P-R055, P-R056.
- The Canada flag R1508 is now cited in the 1E note and in Q8 (rev L212, L616).
- No orphan rows. Nothing missing from the ledger.

Coverage verdict: PASS.

---

## 2. ARITHMETIC AUDIT

### 2A. Loop-0 mismatches

| Metric | Loop-0 finding | Revised A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| Consolidated CCC, 30-Sep-2026 | F1: -61.83 should be -55.83 | -55.83 days; change +18.26 (rev L371, L443) | -55.83 (63.32 + 3.87 - 123.02); +18.26 | L335, L338, L384, L135, L139 | RESOLVED |
| QoQ parent PAT attribution | F2: 192.08 (93%) should be 185.39 (89.6%) | Both shown: all non-parent sources 185.39 (89.6%); subsidiaries plus eliminations 192.08 (92.9%) before associates -7.60 and NCI +0.91 (rev L426-438) | Subs+elims Q1 = 129.72 - 104.45 - 4.35 = 20.92; Q2 = 335.61 - 125.86 + 3.25 = 213.00; change 192.08. Check: 21.41 + 192.08 - 7.60 + 0.91 = 206.80 | L158, L164, L166, L167, L637 | **WITHDRAWN: A5 error** (see note) |

**Note on F2 (A5 error, withdrawn).** In loop 0 I labelled "consolidated parent PAT less standalone PAT" as "subsidiaries plus eliminations". That difference also holds the share of associates (L158), which are not subsidiaries, and the NCI line (L167). On the label A4 used, A4's original 192.08 (92.9%) was correct. My 185.39 is correct only as "all non-parent sources". The revised 5C table shows both figures with their bases, the components sum to the 206.80 rise, and the conclusion (a subsidiary event, about 90%) is unchanged. The loop-0 F2 sub-item on "overseas" was valid and is fixed: the brief no longer says it, and 5C names the Indian subsidiaries (rev L436).

### 2B. Every new or changed derived number in the revised review

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| H1 Op EBITDA growth; margin change (2C) | +14.78%; +83 bps | 341.59 / 2,310.43 = 14.785%; 19.984% - 19.158% = 0.826 pp | L135-146 | PASS |
| Revenue decomposition (2D-1) | components "sum to 588.14" incl. inter-segment +38.96 | 606.52 + 75.22 - 96.63 - 35.92 + 38.96 = 588.15; Real Estate -0.01 (L237) completes 588.14 | L234-239 | ROUNDING (STYLE L1-S3) |
| Campaign Registry base effect (1E note) | Q1 FY26 122.93 / 189.38, 64.91%; Q2 FY26 -38.5% QoQ, 37.32%; Q2 FY27 +31.8% vs Q1 FY26; H1/H1 +55.75%; QoQ +10.1%; Q1 FY26 share 26.09% | same (122.93 / 471.12 = 26.09%, 471.12 = 965.96 - 494.84) | L238, L246, L247 | PASS |
| Digital bound (cross-read) | 208.10; 101.10; 51.8% of 195.09; 57.7% of 175.18; about 94 left; "halved" about 107 = about 55%; 4,378 needed, 45% above 3,016 | same ((195.09 + 107) / 0.069 = 4,378.1; 107 / 195.09 = 54.8%) | P-L138, P-L142, L1384, L243 | PASS |
| Step 4 credit-cost sentence | H1 other expenses +57.24 (+3.15%) vs revenue +10.04%; Q2 -35.42 YoY, -63.07 QoQ | same | L143, L135 | PASS (wording: STYLE L1-S1) |
| 5B Reg 52(4) rows | bad-debts ratio 1.90% to 8.57% (+6.67 pp, H1 not annualised); current ratio 0.57 to 0.36 (-0.21) | same | L938, L940 | PASS |
| Parent share of H1 write-offs | 116.73 of 161.23 = 72%; reversal 111.81 | 72.4% | L419, L825, L829 | PASS |
| 5C attribution table | 29.78 / 215.17 / +185.39; 20.92 / 213.00 / +192.08; 4.35 / (3.25) / -7.60; 4.51 / 5.42 / +0.91 | same | L158, L164, L166, L167, L637 | PASS |
| 5D WC read | cycle -55.83; lost 18.26 days, mostly payables | payables -15.67 of 18.26 | L384, L139 | PASS |
| Associate economics (5D) | TTM share 16.66; 21.4x; 139.96x; 0.71%; 5.7x H1 FCF 62.01 | same | L158, L326, L441, L458, L462 | PASS |
| Flags, Q1, Q8, Q10, Q12, brief, analyst note (restated figures) | 185.39 / 89.6%; 55.75% / 56%; 86%; about 140x; under 1% | same | as above | PASS |

All other derived metrics are unchanged from loop 0 and still tie: Op EBITDA, margins, ETR, PAT bridge, cash, net debt, S-vs-C gap, ROCE and TTM.

Arithmetic verdict: PASS. No mismatch above rounding.

---

## 3. ADVERSARIAL READ (on the revised review)

The three loop-0 grafts are in place: Campaign Registry base effect (rev L212), Digital bound (rev L310-318) and associate economics (rev L447). I re-picked the three most positive claims that remain in the revised text.

### Read 1. "On the face of the filing, the gain is operating" (rev L343); Op EBITDA +21.15%, margin +202 bps (rev L225-226)

Strongest bear counter from the extract:
- Subsidiary Op EBITDA rose 195.09 QoQ on subsidiary revenue up 89.54 (4,744.23 to 4,833.77), an incremental margin of about 218% [DERIVED from L135, L621].
- H1 margin is up only about 83 bps.
- The gross spread fell 305 bps (L135, L139).
- Digital explains about half of the jump at most (rev L310-318).
- The parent's own Reg 52(4) footnote credits its H1 margin rise to "decrease in Operating and other expenses" (L917).

Survives? Yes. Graft needed? No. The review already carries it: cost-led growth (rev L262), unexplained cost credits (rev L286), the about-half bound with "neither covers the whole jump alone" (rev L318), the one-quarter caveat (rev L285) and the Q3 21.0% / 19.5% test (rev L592-595). The 218% incremental margin and L917 are optional sharpenings.

### Read 2. Cash conversion "Direction: improving" (rev L449; CFO +63.87%, pre-tax cash +21.48%)

Strongest bear counter from the extract:
- On a pre-tax basis, cash conversion of Op EBITDA moved only from 59.16% to 62.61%, about +3.4 pp (1,366.85 / 2,310.43 to 1,660.49 / 2,652.02) [DERIVED, L439, Step 1B]. 51.8% of the CFO gain is lower tax paid (315.42 of 609.06, L440).
- WC drag grew by 150.15 (L431-438).
- FCF after lease and interest stayed negative at (584.30), while 498.78 of dividend and 356.10 of associate investment went out (L458, L462, L478-480).

Survives? Yes, but it is already in the review: tax share (rev L360), WC "More drag" (rev L367), negative FCF after lease and interest (rev L366), and the INDETERMINATE classification with tax refunds as missing evidence item 1 (rev L449). Pre-tax cash growth (+21.48%) still beats Op EBITDA growth (+14.78%), so the "improving" direction holds on a pre-tax basis too. No graft.

### Read 3. Digital portfolio breakeven path as a candidate trigger (rev L529; forward map rev L754)

Strongest bear counter from the extract:
- The series skips FY26 and every FY26 quarter (P-L137-151).
- "Digital margin" has no definition (L1366, R1768).
- There is no breakeven date (P-L132).
- The FY25 point is a full-year rupee figure set beside a quarter (P-L147 vs P-L138).
- The perimeter moves both ways (L463, L1246, L1251, L1253-1254).

Survives? Yes, but it is already in the review: P-A3-01 to P-A3-04 in the cross-read (rev L299-302), the bound and perimeter bullets (rev L310-316), and Q2, Q3 and Q27 (rev L610-611, L640). No graft.

### Read 4. Mandatory acquisition-economics probe

- **Associate stake buy, 356.10.** The multiple is now stated in the review (rev L447): about 21.4x the TTM group share of associate profit (16.66) for the H1 cash call, and about 140x for the 2,331.73 carrying value, a 0.71% yield. The review gives the bear reading ("capital-hungry stake earning under 1% on book") and carries it into flag 13, the Step 7 overlay and the brief. Probe SATISFIED.
- **Kaleyra, Inc. transfer.** FMV is USD 92.625m (L1505-1507). Target PAT is NOT FOUND, so the multiple cannot be computed. The deal is intra-group and the review holds the standalone carrying-value question (Q15, rev L628). SATISFIED.
- **FY26 acquisition of a subsidiary, 136.96 (L463).** Target PAT is NOT FOUND. The review carries the amount as a Digital perimeter fact (rev L316, Q27 rev L640). SATISFIED.

No new surviving bear counter needs a graft.

---

## LOOP-0 FINDING DISPOSITION

| Loop-0 item | Type | Disposition in revised review | Status |
|---|---|---|---|
| F1 CCC | FACTUAL | Corrected (rev L371, L443) | RESOLVED |
| F2 attribution 93% | FACTUAL | A5 error on label basis; A4's 192.08 was correct for "subsidiaries plus eliminations". Revised text shows both bases correctly | WITHDRAWN |
| F2 "overseas" | FACTUAL | Dropped from the brief; Indian subsidiaries named (rev L436, L725) | RESOLVED |
| F3 H1 other expenses | FACTUAL | Corrected (rev L343) | RESOLVED (wording residual, STYLE L1-S1) |
| M1 Campaign Registry base | MISSING | Grafted (rev L212, L477, L530, L561-562, L616, L704, L741) | RESOLVED |
| M2 Digital bound | MISSING | Grafted (rev L310-318); "likeliest" removed (rev L883) | RESOLVED |
| M3 Associate multiple | MISSING | Grafted (rev L447, L567, L625, L705, L741) | RESOLVED |
| M4 Reg 52(4) bad-debt qualifier | MISSING | Grafted (rev L83, L400-404, L623, L697, L702) | RESOLVED |
| S1, S2, S3, S4, S5, S9, S12, S13 | STYLE | Applied | RESOLVED |
| S6, S7, S8, S10, S11 | STYLE | A1/A2 items, not A4; carried for the record | OPEN (no loop) |

---

## VERDICT

**COMPLETE.** No FACTUAL, MISSING or CONTRADICTION finding remains. Only STYLE notes are logged. The review may proceed to the Notion payload gate. The protocol verdict stays PROCEED WITH FLAGS and cash conversion stays INDETERMINATE-WITH-DIRECTION.

---

## STYLE NOTES (logged, no re-run)

- L1-S1. Step 4 (rev L343) says "So other cost lines absorbed most of the credit swing". On H1 numbers, other expenses excluding the credit swing fell 53.55 (57.24 - 110.79). That is about half (48%) of the 110.79 swing, and the filing does not say which P&L line holds credit costs. Write "about half". This wording traces to my loop-0 audit text.
- L1-S2. The brief (rev L725) says "Subsidiaries, with eliminations, supplied about 90%". Step 5C gives 92.9% for subsidiaries plus eliminations and 89.6% for all non-parent sources. Use the 5C label "non-parent sources" with "about 90%", or say "about 93%".
- L1-S3. Diagnostic 1 (rev L261): the named components sum to 588.15. Add Real Estate -0.01 (L237) to reach 588.14.
- L1-S4. The brief (rev L741) says "the 114% quarterly jump". That reads as QoQ. Say "the 114% rise on the year-ago quarter".
- L1-S5. The preamble (rev L22) lists R1514 (Mgage SA de CV) as "context only", but the Digital bound (rev L316) and Q27 use it as a perimeter fact. Drop R1514 from the no-finding list.
- L1-S6. Loop-0 S6, S7, S8, S10 and S11 are A1/A2 items and stay open for the record: A2 count-test bases, the p16/L776 label, repeat column qualifiers not emitted as rows, the P-R026 value, and the slide 4 verbatim title.

---

```yaml
stage: A5-adversary
company: "TATACOMM"
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
    - "L1-S1 Step 4 rev L343 'absorbed most of the credit swing': ex-credit other expenses fell 53.55 of 110.79 (about half, 48%); credit-cost P&L line not disclosed (wording from A5 loop-0 text)"
    - "L1-S2 Brief rev L725 labels 'about 90%' as subsidiaries with eliminations; 5C gives 92.9% subsidiaries plus eliminations, 89.6% all non-parent sources"
    - "L1-S3 Diagnostic 1 rev L261 named components sum to 588.15; add Real Estate -0.01 (L237)"
    - "L1-S4 Brief rev L741 '114% quarterly jump' reads as QoQ; say 'on the year-ago quarter'"
    - "L1-S5 Preamble rev L22 lists R1514 (Mgage) as context only while rev L316 and Q27 use it as a Digital perimeter fact"
    - "L1-S6 Loop-0 A1/A2 style items S6, S7, S8, S10, S11 remain open (not A4)"
loop_back_to: ""
gap: ""
style_notes:
  - "L1-S1 'most' should read 'about half' (53.55 of 110.79)"
  - "L1-S2 align brief attribution label with 5C"
  - "L1-S3 add Real Estate -0.01 to the revenue decomposition"
  - "L1-S4 '114% quarterly jump' to 'rise on the year-ago quarter'"
  - "L1-S5 drop R1514 from the no-finding disposition list"
  - "L1-S6 A1/A2 items S6, S7, S8, S10, S11 carried, no loop"
analyst_note: "Loop 1 re-audit is COMPLETE. Every loop-0 FACTUAL and MISSING item is resolved in the revised review, checked against the A1 fulltext lines. One loop-0 finding was an A5 error: F2. My 185.39 (89.6%) was consolidated parent PAT less standalone PAT, which also holds the associate swing (-7.60) and NCI (+0.91). A4's original 192.08 (92.9%) was correct for its label, subsidiaries plus eliminations. The revised 5C shows both bases, the parts sum to the 206.80 rise, and the conclusion is unchanged. The Step 4 phrase 'absorbed most of the credit swing' also traces to my loop-0 wording; on H1 numbers it is about half, logged as STYLE. Coverage is unchanged and clean. Every new derived number ties; one 0.01 Real Estate omission is rounding-level. Re-reading the three most positive remaining claims (operating gain, cash direction, Digital breakeven path) finds counters that survive but are already in the review. The acquisition probe is satisfied. A1/A2 style notes S6, S7, S8, S10, S11 carry with no loop."
```
