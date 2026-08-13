# A5 ADVERSARY / COMPLETENESS AUDIT — Kirloskar Electric Company Limited (KECL) — Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8
**Under audit:** `review_kecl_q1fy27.md` (A4) | **Diffed against:** `ledger_results_kecl_q1fy27.md` (A2) | **Re-derived from:** `extract_results_kecl_q1fy27.txt` (A1)
**Fresh context:** A4 review + A1 extract + A2 ledger only. All counts re-run independently; all metrics recomputed from raw Lakhs figures. A3 reasoning not seen.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF is present as the mandatory final section (review l.390-406). All four labelled parts present and carrying real, non-placeholder content:

| Brief part | Located | Non-empty / real content | Status |
|---|---|---|---|
| (1) Summary narrative | review l.392-394 | Yes — ~15-line narrative, [FILING]/[ANALYSIS] tagged, covers revenue fall, operating loss, solvency, monetization, dilution, verdict | PRESENT |
| (2) SECTOR intelligence | review l.396-398 | Yes — segments, order intake, EXTERNAL-GENERAL sector tailwinds, cyclicality, labelled | PRESENT |
| (3) BUSINESS-MODEL intelligence | review l.400-402 | Yes — unit economics, operating leverage ~Rs120-130 Cr breakeven, balance-sheet-repair story, Kirsons shell, model-drift watch | PRESENT |
| (4) COMPETITION intelligence | review l.404-406 | Yes — larger better-capitalized peers, capital-fragility disadvantage, niche traction, derisking risk, labelled | PRESENT |

**Gate result: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/manual sweep of the A1 extract (original lines 1-878 + verbatim re-extraction 881-1301). My counts vs A2:

| Category | A2 count | My fresh count | Basis (lines) | Orphan / missing rows | Status |
|---|---|---|---|---|---|
| Numbered notes | 14 | 14 | Notes 1-14, l.253-400 (no gaps, no unnumbered footnotes) | none | MATCH |
| P&L line items | 28 | 28 | l.96-134: 21 value/dash rows + 7 OCI/TCI/equity rows | none | MATCH |
| Segment line items | 32 | 32 | verbatim l.908-986: 6 rev + 8 results + 6 assets + 6 liab + 6 cap-employed | none | MATCH |
| Board agenda items | 3 | 3 | l.43-54 | none | MATCH |
| Auditor paras standalone | 10 | 10 | l.433-565 (paras 1-7 incl. 5a bullet, 6a, 6b + signature) | none | MATCH |
| Auditor paras consolidated | 12 | 12 | l.590-768 (paras 1-8 incl. 33(8) addendum, 4a, 5a, 5b, 6 Other Matters, 7 conclusion + signature) | none | MATCH |
| Annexure-2 rows | 3 | 3 | l.781-790 | none | MATCH |
| Annexure-3 blocks | 9 | 9 | l.807-870 | none | MATCH |
| Named entities | 7 (+2 unnamed) | 7 (+2 unnamed) | Kirsons BV, Kelbuzz, SKG Terra, SLPKG, Luxquisite, Kaytee Switchgear, Kirloskar Power Equipments | none | MATCH |
| Signature blocks | 4 | 4 | Bhat l.58-68; V.Kirloskar l.408-410; Patwardhan x2 l.553/757 | none | MATCH |

**Fresh-pass diff:** no category differs from the ledger. **No row my pass found that the ledger lacks** (nothing loops to A2).

**Ledger-row → A4 reconciliation (orphan check):** every A2 row is either cited in A4 or covered by A4's explicit blanket "all reviewed" statements (review l.13-26). Notes 1-14 individually tabled (0D, l.50-63). Segment rows cited in Step 5 proxies (l.251-252) and S-vs-C (l.277). Auditor paras characterized in 0D (l.65-69). Entities/agenda/annexures cited across Steps 0-8.5 and monitorables. **No orphan rows** (nothing loops to A3).

- **Minor observation (not a FAIL):** the seven OCI/TCI/Other-Equity rows (l.118,119,121,122,123,124,126) are omitted from A4's Step-1 line-item table and covered only via the blanket "all 28 reviewed" statement. Substantively fine — these are ZERO_STANDING in every quarter column and populated only in the FY26 annual column, and the two that matter (Revaluation gain on land (366); Remeasurements 79) feed A4's revaluation-reserve / net-worth thread (0D Note-5, Q1 for management). Recorded as reviewed-no-finding, not an orphan.

**COVERAGE RESULT: PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs, x0.01 → Rs Cr)

Headline YoY table and PAT bridge re-derived from scratch off l.96-134. Standalone unless noted.

### 2A. Step-1 / derived-metric re-run
| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Revenue Q1FY27 | 103.85 | 10,385 x0.01 = 103.85 | l.96 | OK |
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | (0.37) | −5.95+1.01+5.25−0.68 = −0.37 | l.108/105/104/97 | OK |
| Op EBITDA Q1FY26 | 6.91 | 0.45+1.07+6.35−0.96 = 6.91 | l.108/105/104/97 | OK |
| Op EBITDA margin Q1FY27 | (0.36)% | −0.37/103.85 = −0.356% | — | OK |
| Op EBITDA margin Q1FY26 | 5.23% | 6.91/132.24 = 5.225% | — | OK |
| Reported EBITDA FY26 | 38.57 | 8.75+4.34+25.48 = 38.57 | l.110/105/104 | OK |
| Op EBITDA FY26 ex-exceptional | 35.60 | 16.84+4.34+25.48−11.06 = 35.60 | l.108/105/104/97 | OK |
| Core PBT ex-OI Q1FY27 | (6.63) | −5.95−0.68 = −6.63 | l.110/97 | OK |
| FY26 core PBT ex-OI ex-exc | 5.78 | 16.84−11.06 = 5.78 | l.108/97 | OK |
| Effective tax rate FY26 | 3.4% | 0.30/8.75 = 3.43% | l.112/110 | OK |
| PAT margin Q1FY27 | (5.77)% | −5.99/103.85 = −5.77% | l.115/96 | OK |

### 2B. YoY table re-run
| Metric | A4 | My recompute | Status |
|---|---|---|---|
| Revenue YoY | −21.5% | (103.85−132.24)/132.24 = −21.47% | OK |
| Op EBITDA margin | −559 bps | −0.356% − 5.225% = −5.58pp | OK |
| Depreciation YoY | −5.6% | (1.01−1.07)/1.07 = −5.6% | OK |
| Finance cost YoY | −17.3% | (5.25−6.35)/6.35 = −17.32% | OK |
| Other income YoY | −29.2% | (0.68−0.96)/0.96 = −29.17% | OK |
| Core PBT ex-OI move | −Rs6.12 Cr | −6.63 − (−0.51) = −6.12 | OK |

### 2C. PAT bridge re-run (Q1FY26 0.45 → Q1FY27 −5.99, total −6.44)
| Component | A4 | My recompute | Status |
|---|---|---|---|
| Gross profit change (net-materials) | −4.98 | GP Q1FY27 103.85−(80.83−9.12)=32.14; Q1FY26 132.24−(96.71−1.59)=37.12; Δ=−4.98 | OK |
| Employee+Other exp change | −2.30 | (19.52+12.99)−(18.44+11.77)=+2.30 cost = −2.30 | OK |
| = Op EBITDA change | −7.28 | −4.98−2.30 = −7.28 (ties −0.37 vs 6.91) | OK |
| Depreciation change | +0.06 | 1.07−1.01 = 0.06 | OK |
| Finance cost change | +1.10 | 6.35−5.25 = 1.10 | OK |
| Other income change | −0.28 | 0.68−0.96 = −0.28 | OK |
| = Reported PBT change | −6.40 | −7.28+0.06+1.10−0.28 = −6.40 (ties −5.95 vs 0.45) | OK |
| Tax change | −0.04 | 0 → 0.04 charge = −0.04 | OK |
| = PAT change | −6.44 | −6.40−0.04 = −6.44 (ties −5.99 vs 0.45) | OK |

### 2D. Cross-checks
- Material cost ratio: Q1FY27 (80.83−9.12)/103.85 = 69.05% ≈ press 69.1%; Q1FY26 (96.71−1.59)/132.24 = 71.93% ≈ press 71.9% (l.826). OK.
- Gross margin 30.9%/28.1% and +281 bps: 32.14/103.85=30.95%; 37.12/132.24=28.07%. OK (see Audit 3, claim 3 — arithmetically correct but analytically incomplete).
- Press ties: Rev Rs103.9 Cr = 10,385 (l.96); PBT (Rs5.95 Cr) = (595) (l.110); finance Rs5.25 Cr = 525 (l.104). OK.
- Segment proxies: Unallocated cap-employed Q1FY27 (19,505)=−195.05 vs Mar-26 (14,894)=−148.94, Δ −46.11 (l.985); Others assets 8,893=88.93, liab 927=9.27, rev 624=6.24, cap-emp 7,966=79.66 (l.941/954/911/965); consol total cap-emp 12,594=125.94 vs std 12,646=126.46, gap 0.52 (l.986). OK.
- S-vs-C PAT gaps: Q1FY26 0.45−0.42=0.03; Q4 −0.62−(−0.63)=0.01; FY26 8.45−8.38=0.07. OK.

**ARITHMETIC RESULT: PASS — zero mismatches above rounding.** Every derived metric, the full YoY table, and the PAT bridge reproduce exactly.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims → strongest bear counter from the SAME extract)

### Positive claim 1 — "Record Q1 order book Rs184 Cr (+28% YoY, book-to-bill 1.79x); underlying demand firm" (review l.196, 366, 386, 461; source l.813)
**Bear counter (from extract):** the Rs184 Cr sits only in the management press release (Annexure 3, l.813), never in the financial statements; A4's own Q9 concedes the firm-vs-framework split is unknown. The 1.79x book-to-bill is mechanically flattered by the −21.5% billing collapse (shrunk denominator), and A4's own competition read (l.404-406) says a solvency overhang may push customers to stronger-balance-sheet peers, i.e. orders may not convert.
**Survives?** NO (already incorporated). A4 already labels the figure a press claim, flags firm-vs-framework in Q9, and explicitly states orders "do not offset the solvency flags" (l.386). The one incremental nuance (ratio inflated by denominator) is minor. No new graft required.

### Positive claim 2 — Finance costs −17.3% YoY = "genuine, recurring positive (deleveraging); JLF term loans repaid" (review l.158, 174, 223; source Note 5 l.284, press l.828)
**Bear counter (from extract):** the deleveraging characterization is not established by the extract. The press attributes the finance-cost fall to "improved working capital utilisation" (l.828), NOT debt paydown. A4's own segment proxy shows the net corporate-borrowing line WORSENING QoQ from (14,894) to (19,505) = −Rs46 Cr (l.985), and the auditor flags "certain overdue payments to creditors" (l.1046) — consistent with lower cost coming from stretching non-interest-bearing payable float rather than genuine net-debt reduction. Note 5 confirms only that JLF-*restructured* term loans were repaid, not that total net borrowing fell.
**Survives?** YES. Supported by l.828, l.985, l.1046 and unaddressed by A4, which calls it a "genuine, recurring positive" without reconciling against its own worsening borrowing proxy. Must be grafted as a caveat: the finance-cost decline is not confirmed deleveraging; it may reflect working-capital/payable stretch, and the net-borrowing proxy deteriorated QoQ.

### Positive claim 3 — Gross margin / material cost improved to 69.1% from 71.9% (+281 bps), "raw material discipline… problem is billing volume, not input cost" (review l.209, 221, 394; source l.826)
**Bear counter (from extract):** the margin "improvement" is materially inflated by an inventory build, not procurement discipline. Change in inventories swung to (912) in Q1FY27 from (159) in Q1FY26 (l.101) — a Rs9.12 Cr finished-goods/WIP accumulation that, on the net-materials basis A4 uses, mechanically lowers cost-of-sales as a % of revenue. Strip the build and Q1FY27 materials-consumed alone is 80.83/103.85 = 77.8% of revenue (gross margin ~22%), well BELOW the year-ago 71.9%/28.1%. Building Rs9.12 Cr of inventory into a −21.5% revenue quarter is the WC red flag A4 itself notes at l.256 — the very same item flattering the headline margin. So "input-cost discipline" overstates a low-quality, inventory-capitalization-driven number.
**Survives?** YES. Supported directly by l.101 and unaddressed as a caveat — A4 asserts the opposite ("problem is billing volume, not input cost," l.394) and never links the margin gain to the inventory build it flags elsewhere. Must be grafted: the gross-margin improvement is partly an inventory-build artifact (net-materials basis); on a materials-consumed basis gross margin deteriorated, and the build is itself a WC-stress signal.

---

## VERDICT

**INCOMPLETE.**

- Deliverable-completeness: PASS (all four brief parts present).
- Coverage: PASS (fresh enumeration matches A2 on all 10 categories; no orphan rows, nothing missing from ledger).
- Arithmetic: PASS (headline YoY table and PAT bridge reproduce exactly; zero mismatches above rounding).
- Adversarial read: **TWO surviving bear counters** (finance-cost "deleveraging" and gross-margin "input-cost discipline") are supported by the same extract and are not addressed in A4. Per the protocol, a surviving counter must be grafted into the review before save.

**loop_back_to: A4.**
**Gap:** graft two surviving bear counters before save — (1) the −17.3% finance-cost decline is not confirmed deleveraging; the press attributes it to working-capital utilisation (l.828) while the net-borrowing proxy worsened Rs46 Cr QoQ (l.985) amid overdue creditors (l.1046); (2) the 69.1%-from-71.9% / +281 bps gross-margin improvement is partly an inventory-build artifact — change in inventories (912) vs (159) YoY (l.101); on a materials-consumed basis gross margin deteriorated (~22% vs 28.1%), and the build is itself the WC-stress signal A4 flags at l.256. No A2 or A3 loop-back required; enumeration and forensic coverage are clean.

```yaml
stage: A5-adversary
company: "KECL"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Finance costs -17.3% YoY = genuine recurring deleveraging positive (review l.158,174,223)"
    counter: "Not confirmed deleveraging: press attributes the fall to working-capital utilisation not debt paydown; net corporate-borrowing proxy worsened Rs46 Cr QoQ (14,894)->(19,505); overdue creditors flagged. May be payable-stretch, not net-debt reduction."
    source_line: "extract l.828, l.985, l.1046; review l.223,251"
  - claim: "Gross margin improved to 69.1% from 71.9% / +281 bps = raw-material discipline; problem is billing volume not input cost (review l.209,221,394)"
    counter: "Partly an inventory-build artifact: change in inventories (912) vs (159) YoY inflates the net-materials margin; on materials-consumed basis gross margin fell to ~22% from 28.1%. The Rs9.12 Cr build into a -21.5% revenue quarter is the WC red flag A4 itself flags (l.256)."
    source_line: "extract l.101; review l.209,221,256,394"
loop_back_to: "A4"
gap: "Graft two surviving bear counters into the review before save: (1) finance-cost decline is not confirmed deleveraging (press attributes to WC utilisation l.828; net-borrowing proxy worsened Rs46 Cr QoQ l.985; overdue creditors l.1046); (2) gross-margin improvement is partly an inventory-build artifact (change in inventories (912) vs (159) YoY, l.101; materials-consumed basis margin deteriorated ~22% vs 28.1%; build is a WC-stress signal). Coverage and arithmetic pass; no A2/A3 loop-back."
```
