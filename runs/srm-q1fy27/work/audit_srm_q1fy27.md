# A5 ADVERSARY / COMPLETENESS AUDIT — SRM Contractors Limited (SRM), Q1 FY27

Fresh context. Audited only: A4 review (`review_srm_q1fy27.md`), A1 extract
(`extract_results_srm_q1fy27.txt`, 438 lines), A2 ledger (`ledger_results_srm_q1fy27.md`).
Every count re-run independently; every derived metric recomputed from raw Lakhs
(÷100 to Cr); A4/A3 cites checked, not deferred to.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF located at review lines 446-466. All four labelled parts present and carrying real content:

| Part | Heading | Line | Present / Empty | Note |
|---|---|---|---|---|
| 1 | SUMMARY NARRATIVE | 448-449 | **PRESENT** | Dense single-paragraph narrative; covers P&L-only nature, +5.05% organic, NCI gap, DTA credit, INDETERMINATE cash, HOLD. Substantive (not placeholder). |
| 2 | SECTOR INTELLIGENCE | 451-455 | **PRESENT** | EPC/J&K, WC-heavy sector structure, payer-mix trigger, Tier-3 tailwind. Provenance-tagged. |
| 3 | BUSINESS-MODEL INTELLIGENCE | 457-461 | **PRESENT** | Core contracting + MIPL gabion leg, margin/NCI/segment drift, cash multiplier. |
| 4 | COMPETITION INTELLIGENCE | 463-466 | **PRESENT** | Moat/order-book strength vs governance-quality vulnerability; peer-benchmark gap flagged (not fabricated). |

**Gate 0 result: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh enumeration diffed vs A2 ledger)

| Category | A2 count | My fresh count | Method | Orphan/Missing rows | Status |
|---|---|---|---|---|---|
| notes | 11 | 11 | Std notes 1-5 (212-230) + Consol notes 1-6 (405-428) = 5+6 | none — all 11 in Step 0D table | PASS |
| line_items | 48 | 48 | 24 std (Table 3) + 24 consol (Table 7); all in Step 1 tables 1A/1B | none | PASS |
| zero_standing | 10 | 10 | Std rows 12,16,18,19,20,21 (6) + Consol rows 12,19,20,21 (4). All shown ND/nil in Step 1 | none | PASS (see note A) |
| agenda_items | 1 | 1 | Sole item = results approval (30-42); 30-min board meeting cited Q10/Step 8.5 | none | PASS |
| auditor_paras | 12 | 13 | Std 4 substantive + Consol 9 substantive (items 2-10 of Table 5) | none — all paragraphs enumerated in ledger & covered by A4 (FF4/FF5/Q8) | PASS (see note B) |
| entities | 8 | 8 | grep `[a-h]\)` returns 7 (item c OCR-garbled "¢)" @412); re-sweep = 8; cross-checks inline list 260-264. All cited (Cons Note 2) | none | PASS |
| turns | 0 | 0 | Results filing, no transcript | n/a | PASS |
| questions | 0 | 0 | No transcript | n/a | PASS |
| slides | 0 | 0 | No deck | n/a | PASS |
| signature_blocks | 7 | 7 | CS letter, 2 std footers, 2 consol footers, 2 auditor sigs. UDIN dupe cited FF10 | none | PASS |
| reliance_table_items | 3 | 3 | Total Revenues 3,447.29 / NPAT 11.84 / TCI-Loss 11.84 (313-316); cited Q8 | none | PASS |

**Every ledger row is cited in A4 or shown as ND/nil.** No orphan rows (ledger present, A4 absent).
No rows my fresh pass found that the ledger lacks. Coverage PASS.

**Note A (minor, A2 cosmetic):** The ledger's SUMMARY-OF-FLAGS line (ledger 305) lists standalone
ZERO_STANDING as "rows 12,16,18,19,21" — omitting row 20 — which would read as 9, but the detailed
Table 3 correctly flags all six (12,16,18,19,20,21) and the COUNT TEST correctly totals 10. Content
intact; only the summary enumeration string is a typo. No coverage loss.

**Note B (minor, A2 count-total):** A2's COUNT TEST reports auditor_paras = 12 (claiming 8 consolidated
substantive paragraphs), but its own Table 5 enumerates 9 consolidated substantive paragraphs (items
2-10), which with 4 standalone = 13. The boundary is genuinely fuzzy (whether line 305 "Our conclusion
is not modified..." + its two reliance continuations count as 2 or 3). Because every paragraph is
individually enumerated in the ledger and their substance (unmodified opinion, reliance self-contradiction
FF4/FF5) is fully carried into A4, no content is missed and no finding is orphaned. Flagged to A2 to
reconcile the total; NOT gate-failing.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Lakhs)

Raw ties spot-checked: all Step 1A/1B ₹Cr conversions correct (e.g. std Q1FY27 Rev 15,031.54→150.32;
consol PBT 2,421.39→24.21; consol deferred tax −163.49→−1.63). PBT ties independently
(std TI 150.79 − TE 131.66 = 19.13 ≈ printed 19.12, rounding).

### Derived metrics — all PASS (representative recompute)

| Metric | A4 value | My recompute (raw) | Source line | Status |
|---|---|---|---|---|
| Std Op EBITDA Q1FY27 (PBT+D+FC−OI) | 32.82 | 1912.46+1001.99+414.29−47.10 = 3281.64 →32.82 | 178/173/172/164 | PASS |
| Std Op EBITDA margin Q1FY27 | 21.83% | 3281.64/15031.54 | 163 | PASS |
| Std ETR Q1FY27 | 33.68% | (481.33+162.67)/1912.46 = 33.68% | 183/184/178 | PASS |
| Std ETR Q1FY26 | 29.26% | 540.09/1846.05 | — | PASS |
| Std PAT margin Q1FY27 | 10.60% | 1593.80/15031.54 | 186/163 | PASS |
| Consol Op EBITDA Q1FY27 | 38.15 | 2421.39+1029.05+457.06−92.30 = 3815.20 →38.15 | 372/367/366/358 | PASS |
| Consol ETR Q1FY27 | 18.84% | (619.63−163.49)/2421.39 = 456.14/2421.39 | 377/378/372 | PASS |
| Consol ETR vs statutory | 633 bps below 25.17% | 25.17−18.84 = 6.33pp | 259 (review) | PASS |
| Std Rev YoY | +5.05% | 7.23/143.09 | 163 | PASS |
| Std Op EBITDA YoY | +59.51% | (3281.64−2057.29)/2057.29 | — | PASS |
| Std core-PBT-ex-OI YoY | +10.59% | 178.59/1686.77 | — | PASS |
| Std PAT YoY | +22.04% | 287.84/1305.96 | 186 | PASS |
| Consol Rev YoY | +37.83% | 5386.54/14239.66 | 357 | PASS |
| Consol PAT YoY (pre-NCI) | +54.63% | 696.44/1274.81 | 380 | PASS |
| Consol EPS YoY | +54.50% | 3.03/5.56 | 390 | PASS |
| S-vs-C PAT gap Q1FY27 | 23.68% | (1971.25−1593.80)/1593.80 | 380/186 | PASS |
| S-vs-C PAT gap Q4FY26 | 60.54% | 2036.54/3363.84 | — | PASS |
| S-vs-C PAT gap Q1FY26 | −2.39% | −31.15/1305.96 | — | PASS |
| S-vs-C PAT gap FY26 | 29.72% | 2543.89/8557.91 | — | PASS |
| MIPL residual profit | ₹365.6 lakh | 377.45(S-vs-C PAT) − 11.84(reviewed subs) = 365.61 | 380/186/314 | PASS |
| MIPL implied margin | ~31.8% | 365.61/(4594.66−3447.29 rev residual) = 365.61/1147.37 | 357/313 | PASS |
| Reviewed-subs margin | 0.34% | 11.84/3447.29 | 314/313 | PASS |
| Reviewed-subs % of consol rev | 17.6% | 3447.29/19626.20 = 17.56% | 313/357 | PASS |
| Consol tax tie-out gap | ~₹6 lakh | TI−TE = 2427.39 vs printed PBT 2421.39 (OCR artefact) | 360/370/372 | PASS (correctly flagged immaterial) |

### FAIL — Standalone PAT bridge (Step 4A), review lines 227-240

The bridge END-POINTS are correct: subtotal to Op EBITDA +12.25 ties, and final PAT change +2.88
ties (13.06→15.94). But the **internal decomposition does not foot**, and one cell contradicts its
own stated formula:

- Row "Gross profit change **(Rev − COGS − Direct Exp)**" is entered as **+18.35**. That formula on
  the printed numbers gives **+14.22** (Q1FY27 150.32−92.68−12.57 = 45.07; Q1FY26 143.09−101.49−10.75
  = 30.85; Δ +14.22). A4's own footnote (line 240) concedes "Δ +14.22 at the GP line" then labels
  +18.35 as "materials-intensity swing net of direct-cost step-up" — a figure I cannot reconstruct
  from any combination of the printed lines. **Mismatch of 4.13 Cr between the cell value and its own formula.**
- Row "Other expenses change" is entered as **−0.22** (a drag). For the column to foot to the
  correct subtotal +12.25 with GP +14.22 and Employee −2.11/−2.12, other-expenses must be a
  **+0.14/+0.15 benefit** (Q1FY27 other-exp balances to ~2.25 vs Q1FY26 2.39 — A4 itself flags the
  printed "2614" as OCR-garbled, line 70/82). The **sign is wrong.**
- As printed, the three components sum to 18.35 − 2.12 − 0.22 = **16.01**, which does not equal the
  stated subtotal **+12.25**. A reader cannot reconcile the table.

This is an above-rounding arithmetic error in a metric the protocol names explicitly (the PAT bridge).
**Loop back to A4.** Fix: set the GP line to +14.22 (matching its formula) and the other-expenses
line to a ~+0.14 benefit, so the column foots to the (correct) +12.25 Op EBITDA subtotal.

*(By contrast, the CONSOLIDATED bridge 4B foots within the acknowledged ~₹6 lakh OCR tax artefact —
GP +25.10, Employee −5.93, Other −1.37, Dep −7.81, FC −3.26, OI −0.67, Tax +0.90, JV −0.01, tie-out
+0.06 → +6.96. PASS.)*

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, bear counter from same extract)

**Claim 1 — "Standalone operating EBITDA margin expanded +746 bps to 21.83%" (review 149, 179).**
Bear counter: the lift is driven by COGS collapsing to 61.7% of revenue (92.68/150.32) from 70.9%
(101.49/143.09) in a single quarter with **no explanatory note** anywhere in the notes blocks (lines
210-232, 403-429), while D&A tripled (239.40→1001.99) and finance costs tripled (131.12→414.29). A
margin lifted by revenue-recognition timing on work-in-progress would surface as rising contract-asset
days — the exact metric the P&L-only filing omits (statement ends at EPS, line 196). **Counter SURVIVES
on the extract — but A4 already incorporates it** (Step 2 diag 2, line 179; business-model brief line
458). No new graft required.

**Claim 2 — "MIPL consolidation accretive; consol PAT +54.6%, EPS 8.59" (review 172, 343).**
Bear counter: consol PAT 1,971.25 and EPS 8.59 carry **no NCI line** (statement lines 372-391 contain
no minority-interest row) despite MIPL being 51%-owned, so ~49% of MIPL profit is not stripped and
owner EPS is overstated; and a deferred-tax **credit** of −163.49 (line 378) flatters consol PAT, cutting
ETR to 18.84%. **Counter SURVIVES — but A4 already incorporates it fully** (FF3/FF7, Step 1B line 111,
Q1/Q3). No new graft required.

**Claim 3 — "Audit clean on both statements; exit trigger #1 did not fire; watchlist item 1 GREEN"
(review 46, 316, 330).** Bear counter: the consolidated "clean" conclusion explicitly rests on a
reliance paragraph (lines 307-323) covering ₹3,447.29 lakh — 17.6% of consolidated revenue — on
"unaudited/unreviewed" component information "certified by the Board," described inconsistently by the
auditor; plus an identical UDIN on both reports (139, 339). So "clean" overstates the assurance actually
obtained. **Counter SURVIVES — but A4 already incorporates it** (FF4/FF5/FF10, Q8/Q9, competition brief
line 465). No new graft required.

**Adversarial result:** all three strongest bear counters are supported by the extract, and all three
are already present in A4's review. **No unincorporated surviving bear counter.** This dimension passes.

---

## VERDICT

**INCOMPLETE.**

- Gate 0 (deliverable): PASS — all four brief parts present.
- Coverage: PASS — no orphan rows, no ledger-missing rows (two cosmetic A2 count-total notes, non-gating).
- Adversarial: PASS — three surviving bear counters, all already incorporated.
- **Arithmetic: FAIL.** Standalone PAT bridge (Step 4A, review lines 227-240) does not foot: the
  "Gross profit change (Rev−COGS−Direct Exp)" cell reads +18.35 where its own formula yields +14.22
  (4.13 Cr mismatch), the "Other expenses change" sign is inverted (−0.22 shown vs ~+0.14 benefit
  required), and the three components sum to 16.01 rather than the stated +12.25 subtotal.

**loop_back_to: A4.** **gap:** Standalone PAT bridge (Step 4A) internal decomposition is arithmetically
inconsistent — restate the Gross-profit line to +14.22 (per its stated formula) and the Other-expenses
line to a ~+0.14 Cr benefit so the column foots to the correct +12.25 Op EBITDA subtotal; endpoints
(+12.25 subtotal, +2.88 PAT) are already correct and unchanged.

```yaml
stage: A5-adversary
company: "SRM"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Standalone PAT bridge (Step 4A) — Gross profit change line"
    a4_value: "+18.35"
    recomputed: "+14.22 (Rev-COGS-Direct: 45.07 - 30.85)"
    source_line: "review 229/240; extract 163/169/170"
  - metric: "Standalone PAT bridge (Step 4A) — Other expenses change line (sign)"
    a4_value: "-0.22 (drag)"
    recomputed: "+0.14 benefit (Q1FY27 other-exp balances ~2.25 vs Q1FY26 2.39)"
    source_line: "review 231; extract 174"
  - metric: "Standalone PAT bridge (Step 4A) — components vs subtotal (foot test)"
    a4_value: "18.35 - 2.12 - 0.22 = 16.01 shown as subtotal +12.25"
    recomputed: "14.22 - 2.11 + 0.14 = 12.25"
    source_line: "review 229-232"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Standalone PAT bridge (Step 4A) does not foot: Gross-profit line +18.35 contradicts its own formula (=+14.22), Other-expenses sign inverted (-0.22 vs ~+0.14 benefit), components sum to 16.01 not the stated +12.25 subtotal. Endpoints (+12.25, +2.88) correct; restate the two lines so the column foots."
```
