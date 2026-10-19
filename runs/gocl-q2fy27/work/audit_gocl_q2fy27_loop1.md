# A5 ADVERSARY AUDIT, LOOP 1 RE-AUDIT: GOCL Corporation Limited (GOCL), Q2 FY27

Agent: A5 adversary, model claude-opus-5-5. Run date 2026-10-20.
Under audit: runs/gocl-q2fy27/work/review_gocl_q2fy27.md (revised, 903 lines; Loop 1 change log at RL884-RL902).
Prior audit: runs/gocl-q2fy27/work/audit_gocl_q2fy27.md (Loop 0, INCOMPLETE on F1 FACTUAL, M1 MISSING, M2 MISSING).
Inputs read:
- A1 fulltext runs/gocl-q2fy27/extracted/gocl-results-q2fy27-fulltext.md (1,078 lines). The image transcription at L832-L1078 governs pages 4-7 and 12-14. Text-layer lines read: L1-L60, L140-L181, L425-L504, L770-L827.
- A1 structured runs/gocl-q2fy27/extracted/gocl-results-q2fy27-structured.md (last row R2233 confirmed).
- A2 ledger runs/gocl-q2fy27/work/ledger_results_gocl_q2fy27.md (count-test block L3-L18 confirmed unchanged).
I opened no source PDF and nothing under inputs/.
Anchor key: "L###" = fulltext line. "RL###" = line in the revised review. "R####" = structured row. Sums are in Rs lakhs unless marked Cr.

Scope (task message): (1) confirm F1, M1 and M2 are closed; (2) re-run the deliverable-completeness gate; (3) check new or changed text for new FACTUAL, MISSING or CONTRADICTION errors, arithmetic included. No new full adversarial pass on unchanged text. Coverage and the adversarial read are re-run on the Loop 1 delta.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT

DELIVERABLE-COMPLETENESS: narrative PRESENT (RL736-RL751; 14 lines, inside the 10-20 band) | sector PRESENT (RL753-RL759) | business-model PRESENT (RL761-RL769) | competition PRESENT (RL771-RL776) | forward map PRESENT (RL778-RL792; 11 catalysts, four hard-dated: 24-Nov-2026 11:00 IST, by 14-Feb-2027, by 30-May-2027, about Aug-Sep 2027; two "before 24-Nov-2026"; every catalyst carries a bull fork and a bear fork). Gate: PASS.

---

## LOOP 0 FINDING CLOSURE

| Loop 0 item | Type | Required fix | Where A4 made it | Verified against | Status |
|---|---|---|---|---|---|
| F1 | FACTUAL | Drop EMS assets +34.5% as capex evidence; state Rs 0.76 Cr capitalised; re-tag "new capacity came into use" as inference | RL266 (filed facts: CWIP 76.01 capitalised, L894; capex 272.63, L950; PPE +160.11, L893; EMS total segment assets +546.80 in Q2 after -233.94 in Q1, net +312.86, L882; "[INFERENCE: if the capitalised items are EMS equipment ...]"); RL280 row relabelled "total, incl. working capital"; RL283; RL405; RL600; brief RL741 ("Whether new EMS capacity came into use is not stated"); RL767; flag RL868 ("capacity not stated in filing"). The +34.5% figure no longer appears. RED grade rests on CWIP-to-nil plus group revenue -4.2% QoQ (L833). | L833, L866, L874, L882, L893, L894, L950 | CLOSED |
| M1 | MISSING | Graft net new lending against interest received; replace "interest is cash-backed"; extend missing evidence (2) and Q1 | RL330, RL353, RL356, 5-III RL363-RL386 (with H1 FY26 comparatives, HGHL net lending, singular label, bull and bear readings, separating observation), RL403, RL409-RL410, RL472, RL496, RL553, RL568, RL593, RL622, RL658, RL673, brief RL746 and RL764, verdict RL726-RL727, flag RL866, YAML RL821. The phrase "cash-backed" no longer appears. | L907, L940, L957-L959, L1012, L1043, L1061-L1063 | CLOSED |
| M2 | MISSING | State HNPCL purchase multiple NOT DETERMINABLE; name missing inputs and source document; mark BVPS step-up untested; extend Q2 | 6D RL513 (re-graded "ON TRACK on process only; economics untested"), RL495, RL539, RL554-RL555, RL575, Q2 RL594, RL621, RL624, monitorable 2 RL653, brief RL750 and RL783, bull fork RL785 "(untested from the filing)", flag RL871, YAML RL822 and RL848. | L44-L56 (Board "reviewed and took note of the Notice ... together with the Explanatory Statement", L49-L52; meeting 24-Nov-2026, L54-L56), L479-L484 (no swap ratio, no share count, no HNPCL financials; "no effect of the scheme has been given", L484), L481-L482 (30-Jul NCLT "while not according approval"; NCLAT set aside 25-Sep), L775, L1020 | CLOSED |
| S6 to S12 | STYLE | Optional fixes | Change log RL893-RL899 | Spot-checked below | Applied; S1 to S5 stay upstream (A1/A2), no loop |

---

## 1. COVERAGE AUDIT

Method for Loop 1: the A1 and A2 artifacts did not change between Loop 0 and Loop 1. I confirmed this three ways. (a) The ledger count-test block (ledger L3-L18) still reads 2,233 IDs, 16 notes, 32 qualifiers, 796 cells, 231 line items, 31 ZERO_STANDING cells, 949 superseded, 4 agenda items, 12 auditor paragraphs, 26 entities, 20 forward statements, gate pass. (b) The structured file still ends at R2233 (structured L2252). (c) The fulltext header still reads line_count 1,078 (L6). The Loop 0 fresh grep pass (audit_gocl_q2fy27.md, section 1) therefore stands. I then re-ran the orphan check against the revised review, because a revision can delete citations.

| Category | A2 count | Fresh count (Loop 0 pass, inputs unchanged) | Orphan rows | Status |
|---|---|---|---|---|
| Numbered notes (C1-C8, S1-S8) | 16 | 16 | 0 | PASS. All 16 still in the Step 0D table (RL58-RL73). |
| Unnumbered footnotes / qualifiers | 32 | 32 | 0 | PASS |
| Financial line items | 231 | 232 | 0 | DIFF 1, unchanged: L956 "Repayment of loans from Companies", label only, no value in either period (L930, L956). Loop 0 STYLE S1, no loop. The revised preamble now names it (RL19). |
| Image NUMBER cells | 796 | 796 | 0 | PASS |
| ZERO_STANDING line items / cells | 21 / 31 | 21 / 31 | 0 | PASS |
| Superseded OCR rows | 949 | 949 | 0 | PASS |
| Board agenda items | 4 | 4 (L40, L44, L49, L54) | 0 | PASS. Cited at RL3, RL62, RL480, RL513, RL554, RL653-RL655. |
| Auditor paragraphs | 12 | 12 | 0 | PASS. Conclusions RL83 (L121-L128, L540-L544); EoM RL74, RL473; Other Matter RL75, RL197. |
| Entities | 26 | 26 | 0 | PASS |
| Forward / pending statements | 20 | 25 (20 plus five units tagged otherwise; Loop 0 S2) | 0 | PASS. All five still reviewed: L434-L435 at RL663; L449-L450 at RL516, RL613, RL662; L563-L567 at RL473; L793 at RL71; L801-L802 at RL72, RL476. |
| Turns / questions / slides | 0 | 0 | 0 | N/A (results filing only, RL6) |
| Structured row IDs | 2,233 | R001-R2233 | 0 | PASS |

A3 findings: all 33 still listed in the preamble (RL21), the YAML (RL808) and the disposition table (RL683-RL717). Grep of the revised review for the agenda and auditor anchors (L36-L42, L40, L44, L49-L52, L54-L56, L121-L128, L540-L544, L143-L155, L159-L180, L556-L568) returns 31 hits.
Orphan rows: none. Missing from ledger: L956 only (STYLE, carried).

---

## 2. ARITHMETIC AUDIT (new and changed text)

Step 1 to Step 4 tables passed in Loop 0 and the Loop 1 change log names no change to them beyond the S7 rounding fixes. I re-checked those fixes and spot-checked unchanged cells I relied on below.

| Metric | A4 value (RL) | Recomputed | Source line | Status |
|---|---|---|---|---|
| EMS segment assets, Q2 rise / Q1 fall / H1 net | +5.47 / -2.34 / +3.13 (+17.2%) Cr (RL266) | 2,130.52 - 1,583.72 = 546.80; 1,583.72 - 1,817.66 = (233.94); 312.86, +17.21% | L882 | PASS |
| PPE net rise; CWIP capitalised; H1 capex | +1.60; 0.76; 2.73 Cr (RL266, RL337-RL338, RL405) | 1,901.77 - 1,741.66 = 160.11; 76.01 to nil; 272.63 | L893, L894, L950 | PASS |
| EMS income QoQ; EMS loss; EMS income YoY | -6.9%; (110.94) to (213.66), "nearly doubled"; +307% (RL266, RL283) | 244.19 / 262.33 - 1 = -6.92%; 1.93x; 244.19 / 59.97 - 1 = +307.19% | L866, L874 | PASS |
| EMS segment asset row (relabelled) | 8.40 / 15.84 / 21.31 / 8.40 / 21.31 / 18.18 (RL280) | 839.58 / 1,583.72 / 2,130.52 / 839.58 / 2,130.52 / 1,817.66 lakhs | L882 | PASS |
| Interest received, consolidated; change; share of income | 99.47 to 110.17; +10.70; 99.96% (RL330) | 9,946.62 to 11,017.17; 1,070.55 = 10.71 Cr; 99.964% | L959, L940 | PASS (last digit: 10.70 is the difference of rounded values; STYLE L1-S2) |
| Net new lending, consolidated; share of interest received; net cash recovered | 88.16; 80.0%; 22.01 (RL330, RL376-RL378, RL403, RL764) | 1,56,115.79 - 1,47,300.00 = 8,815.79; 80.02%; 11,017.17 - 8,815.79 = 2,201.38. Ties to loan balance rise 3,07,099.16 - 2,98,283.36 = 8,815.80 (L907). | L957-L959, L907 | PASS |
| Standalone interest income / received; ratio | 97.48 / 97.66; 100.2% (RL353) | 9,747.91 / 9,766.00; 100.19% | L1043, L1063 | PASS |
| Standalone net new lending; share of interest; net cash recovered | 68.00; 69.6%; 29.66 (RL353, RL380-RL381, RL472, RL553) | 1,54,100.00 - 1,47,300.00 = 6,800.00; 69.63%; 2,966.00. Ties to L1012 rise 2,34,990.00 - 2,28,190.00 = 6,800.00. | L1061-L1063, L1012 | PASS |
| "Other Company" given / realised | (1,432.75) / 349.70 H1 FY26; (1,541.00) / 1,473.00 H1 FY27 (RL356) | 1,43,275.00 / 34,970.00; 1,54,100.00 / 1,47,300.00 | L1061-L1062 | PASS |
| H1 FY26 comparatives, 5-III | cons 178.58, 179.5%, (79.11); standalone 1,083.05, 1,846.1%, (1,024.38); received 90.9% (RL375-RL381) | 17,857.95; 179.54%; (7,911.33); 1,08,305.00; 1,846.11%; (1,02,438.32); 9,946.62 / 10,948.17 = 90.85% | L940, L957-L959, L1061-L1063 | PASS |
| HGHL net new lending H1 FY27; realised | 20.16 (2,015.79); nil (RL382) | 1,56,115.79 - 1,54,100.00 = 2,015.79; L958 = L1062 = 1,47,300.00. Ties to HGHL loan rise by subtraction 72,109.16 - 70,093.36 = 2,015.80. | L907, L957-L958, L1012, L1061-L1062 | PASS |
| Yield and churn | 8.42%; 7.28%; 66.5% (RL372-RL374) | 9,747.91 / 2,31,590.00 x 2 = 8.418%; 11,021.19 / 3,02,691.26 x 2 = 7.282%; 1,54,100.00 / 2,31,590.00 = 66.54% | L907, L940, L1012, L1043, L1061 | PASS |
| HNPCL guarantee as share of standalone equity | 52.4% (RL513, RL555) | 1,09,610 / 2,09,074.08 = 52.43% | L775, L1020 | PASS (see STYLE L1-S1 on the "at least" wording) |
| Unplaced FX loss outside standalone | 7.55; 7.46; 0.09 Cr (RL197, RL617) | 746.24 + 8.82 = 755.06; 746.24; 8.82 lakhs | L941, L1044 | PASS |
| Q1 FY26 realty income (land-gain quarter) | 2,123.55 lakhs; 21.24 Cr (RL244, RL256) | 2,240.64 - 117.09 = 2,123.55 | L867 | PASS |
| H1 OI like-for-like | -11.0%; +2.9% to +3.8%; interest 90.7% (RL244) | -11.05%; 12,149.48 / 11,802.89 = +2.94%; / 11,702.89 = +3.82%; 90.71% | L834, L445, L800, L940 | PASS |
| Borrowings repaid inside finance cost paid | 61.52 + 2.41 = 63.93 (RL399) | 63.93 | L919, L942, L963 | PASS |
| S7 fixes | revenue YoY +85.0%; inventory-days change -194.1; Mar-26 payable days 8,281.9; Mar-26 CCC -7,984.4; Q1 FY27 revenue 4.29 (RL207, RL224, RL239, RL334-RL336, RL263) | 84.95%; 260.25 - 66.17 = 194.08; 3,064.54 / 135.06 x 365 = 8,281.93; 37.31 + 260.25 - 8,281.93 = -7,984.37; 428.51 | L833, L836-L837, L901, L904, L921 | PASS |
| Revenue QoQ; H2 FY26 run-rate | -4.2%; "about Rs 2 Cr a quarter" (RL263) | 410.63 / 428.51 - 1 = -4.17%; (976.31 - 561.20) / 2 = 207.56 | L833 | PASS |
| Standalone net cash change | +162.78 (RL360) | 21,509.52 - 5,232.47 = 16,277.05 = 162.77 Cr | L1010-L1011 | PASS (last digit, STYLE L1-S2) |
| Standalone FCF change | +46.67 (RL355) | 2,149.67 + 2,516.65 = 4,666.32 = 46.66 Cr | L1052-L1053 | PASS (last digit, STYLE L1-S2) |
| Liquidity after dividend; advance share of cash; tax bridge | 68.73; 51.4%; 26.37 - 9.09 - 0.43 = 16.85 (RL395-RL399) | 21,745.13 - 14,871.75 = 6,873.38; 11,168.42 / 21,745.13 = 51.36%; 2,637.06 - 908.83 - 42.90 = 1,685.33 vs 1,685.34 | L494, L846, L851, L905-L906, L925, L948, L953 | PASS |
| BVPS; change; P/B | 619.46; -2.3%; 0.57x (RL539, RL558) | 3,07,079.33 / 495.725 = 619.46; vs 3,14,293.85 / 495.725 = 634.01, -2.29%; 354 / 619.46 = 0.571 | L860, L915 | PASS |
| Continuing PAT QoQ | -19.4% (RL551) | 3,535.88 / 4,385.20 - 1 = -19.37% | L849 | PASS |
| Unreviewed shares (re-check) | 17.1 / 18.8 / 11.6 / 14.3 / 26.2% (RL197) | 17.10 / 18.81 / 11.56 / 14.27 / 26.19% | L160-L162, L853, L859, L912 | PASS |

Arithmetic mismatches above rounding: none. Three last-digit differences, each from subtracting already-rounded values, are logged as STYLE L1-S2.

---

## 3. ADVERSARIAL READ (Loop 1 delta)

Loop 0 claim status after the grafts:
- Claim 1, "Interest is cash-backed": the bear counter is now grafted (M1 closed). The review states gross receipt (99.96%) and net re-lending (80.0% group, 69.6% standalone) side by side, names the bull and bear readings, and names the separating observation (borrower-level grants and realisations, Q1).
- Claim 2, the Kukatpally advance "points to continued appetite" (RL756, now tagged [INFERENCE]): the counter survives and was already carried in Loop 0 (RL511, RL597, RL613, RL787). No change needed.
- Claim 3, "debt-free": the in-sentence qualifier is now present at RL406, RL768 and RL773 (S8 applied). Carried.

New positive claim introduced by the graft: 5-III bull reading, "Rs 1,473.00 Cr of principal came back in H1 (L1062), so the borrower can repay at scale" (RL386).
- Strongest bear counter from the extract: repayment at that scale appears in one half only. In H1 FY26 the "Other Company" line realised 349.70 Cr against 1,432.75 Cr lent (L1061-L1062). In H1 FY27, grants (1,541.00) still exceeded realisations (1,473.00). A book that turns over 66.5% of its average balance in six months (RL374) can show large realisations with no fall in exposure.
- Survives: YES, but A4 already carries every element in the same table (H1 FY26 column at RL379-RL381, churn at RL374) and in the bear reading at RL386. No graft needed.

MANDATORY ACQUISITION-ECONOMICS PROBE (HNPCL Scheme of Merger by Absorption; L44-L47, L479-L484, L782-L787).
- Multiple: consideration ND / HNPCL PAT ND = NOT DETERMINABLE from the extract. A4 now states this at RL513 and RL554, names the missing inputs (swap ratio, shares to be issued, HNPCL PAT, net worth, debt) and the source (Notice and Explanatory Statement, L49-L52), and marks the BVPS step-up untested.
- Quality markers on file: leverage only. ROCE, cash and customer tenure are ND.
- The bear reading is grafted. One wording point remains on the leverage marker (STYLE L1-S1 below).

---

## FINDINGS (tagged)

FACTUAL: none new.
MISSING: none new.
CONTRADICTION: none new.

STYLE (logged, no loop):
- L1-S1 (A4; wording originated in A5's Loop 0 audit). 6D (RL513) reads "guaranteed HNPCL borrowings of at least Rs 1,096.10 Cr (L775) [INFERENCE: a guarantee does not exceed the borrowing it backs]". The premise is not general. The guarantee was "given in earlier year" (L775) on borrowings "availed" from banks and FIs. Outstanding borrowings can amortise below a guarantee amount, so the guarantee is a ceiling on GOCL's exposure, not a floor on HNPCL's debt. Suggested fix: "GOCL guarantees Rs 1,096.10 Cr of HNPCL bank and FI borrowings (L775), 52.4% of standalone equity (L1020); HNPCL's outstanding debt is not disclosed." The same cell already says debt is not disclosed. The 52.4% exposure figure, the 6D grade, the flags and the verdict do not change. I logged it as STYLE because the claim carries an explicit [INFERENCE] tag with its premise shown. The operator may overrule to FACTUAL.
- L1-S2 (A4). Last-digit differences from subtracting rounded values: RL330 interest received change +10.70 (exact 10.71); RL360 standalone net cash change +162.78 (exact 162.77); RL355 standalone FCF change +46.67 (exact 46.66). No conclusion is affected.
- L1-S3 (A4). Change log RL902 says "every Step 1 to Step 4 figure [is] unchanged". The change log's own S7 and F1 rows (RL890, RL894) changed Step 2 revenue YoY (84.9% to 85.0%), Step 3 Q1 FY27 revenue wording, and removed the Step 3 +34.5% figure. This is a process note only; the review body is correct.
- L1-S4 (A4, informational for the orchestrator). The review file no longer ends with its YAML block; the change log follows it (RL884-RL902). The change log holds no fenced block, so a last-fenced-block parser still finds the A4 YAML (RL796-RL882).
- L1-S5 (A4, optional; unchanged text). Brief RL743 lists "three causes" of the YoY profit rise and omits the exceptional FX gain (+Rs 3.46 Cr, 13.1% of the change; RL302, L844).
- L1-S6 (A4, optional). Brief RL756 "GOCL has sold 157.21 of 264.50 Kukatpally acres to one buyer [FILED Q2]". Note 3 (L442-L446) places the sales inside the Squarespace MoU but does not state that every acre went to Squarespace. Drop "to one buyer" or tag it as read in context.
- Carried from Loop 0, upstream, no loop: S1 (A2, L956 label not in ledger; still 231 line items), S2 (A1, forward tagging; R1239 "ceased"), S3 (A1, SEBI/ICAI boilerplate), S4 (A2, auditor-paragraph mapping and RESTATED usage), S5 (A1, R1606/R2073 reserves column).

---

## VERDICT

VERDICT: COMPLETE.
- F1, M1 and M2 are closed. Each graft ties to the extract line by line (section 2).
- Deliverable-completeness gate: PASS.
- Coverage: no orphan rows; the one ledger diff (L956, label only) stays STYLE.
- Arithmetic: no mismatch above rounding.
- Adversarial delta: the one new positive claim (RL386) has its bear counter already carried in the same table.
- Only STYLE findings remain (L1-S1 to L1-S6, plus Loop 0 S1 to S5 upstream). They are logged and do not loop. The review may proceed to the operator-approved Notion save.

---

```yaml
stage: A5-adversary
company: "GOCL"
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
  missing_from_ledger:
    - "L956 consolidated CF 'Repayment of loans from Companies': label only, no value either period (A1 header L930); carried from Loop 0 as STYLE S1, no loop."
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "L1-S1 (A4; wording from A5 Loop 0): 6D RL513 'guaranteed HNPCL borrowings of at least Rs 1,096.10 Cr [INFERENCE: a guarantee does not exceed the borrowing it backs]'; premise not general, guarantee given in earlier year can exceed amortised outstanding debt; restate as GOCL guarantee Rs 1,096.10 Cr (L775), 52.4% of standalone equity (L1020), HNPCL debt not disclosed. No number, grade or verdict changes; operator may overrule to FACTUAL."
    - "L1-S2 (A4): last-digit differences from rounded subtraction: RL330 +10.70 vs 10.71; RL360 +162.78 vs 162.77; RL355 +46.67 vs 46.66."
    - "L1-S3 (A4): change log RL902 'every Step 1 to Step 4 figure unchanged' conflicts with its own S7/F1 rows (Step 2 revenue YoY, Step 3 Q1 revenue, Step 3 +34.5% removed)."
    - "L1-S4 (A4, info): review file ends with the change log, not the YAML; A4 YAML is still the last fenced block (RL796-RL882)."
    - "L1-S5 (A4, optional): brief RL743 'three causes' omits exceptional FX +Rs 3.46 Cr (13.1% of YoY PAT change, RL302, L844)."
    - "L1-S6 (A4, optional): brief RL756 'to one buyer' not stated in Note 3 (L442-L446)."
loop_back_to: ""
gap: ""
style_notes:
  - "L1-S1 HNPCL debt floor inference wording in 6D (A4; from A5 Loop 0)"
  - "L1-S2 last-digit rounded differences RL330, RL355, RL360 (A4)"
  - "L1-S3 change log 'Step 1-4 unchanged' line vs its own S7/F1 rows (A4)"
  - "L1-S4 change log follows YAML block (A4, info)"
  - "L1-S5 brief 'three causes' omits exceptional FX (A4, optional)"
  - "L1-S6 brief 'to one buyer' provenance (A4, optional)"
  - "Loop 0 S1-S5 upstream (A1/A2) carried, no loop"
analyst_note: "Loop 1 closes all three Loop 0 loop items. F1: the RED capex grade now rests on the CWIP-to-nil test, the review states Rs 0.76 Cr capitalised, and EMS segment assets carry a total-assets label. M1: net new lending against interest received sits in 5-III with H1 FY26 comparatives, and every downstream line uses the gross-versus-net wording. Both net-lending figures tie to the balance-sheet loan movement (L907, L1012). M2: 6D states the HNPCL multiple is not determinable and names the missing inputs and the Explanatory Statement (L49-L52). No new FACTUAL, MISSING or CONTRADICTION finding. One STYLE note needs the operator's eye. The 'at least Rs 1,096.10 Cr' HNPCL debt floor assumes a guarantee never exceeds the borrowing it backs. That is not general: debt can amortise below a guarantee given in an earlier year. The wording came from A5's own Loop 0 audit. It changes no number, grade or verdict, so I logged it as STYLE; the operator may overrule. Coverage carries forward because the A1 and A2 artifacts are unchanged."
```
