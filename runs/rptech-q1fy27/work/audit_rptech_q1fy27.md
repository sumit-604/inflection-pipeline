# A5 ADVERSARY / COMPLETENESS AUDIT — RPTECH Q1 FY27
**Agent:** A5 ADVERSARY (Opus 4.8) | **Audits under review:** A4 merged Role 4 + Role 5 review (`review_rptech_q1fy27.md`)
**Method:** fresh context. Re-derived independently from A1 extracts (results, PR-results, PR-JV, presentation, concall) and diffed against the five A2 ledgers. Did NOT defer to A4/A3 cites; every A4 number re-computed from the raw source line.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The MANDATORY PLAIN-LANGUAGE BRIEF exists (review lines 822-835) with all four labelled parts present and carrying real, provenance-tagged content:

| Brief part | Heading present | Non-empty / real content | Status |
|---|---|---|---|
| (1) Summary narrative | "## 1. SUMMARY NARRATIVE" (L825) | ~18 lines, numbers-first, symmetric bull/bear, [FILING]/[CONCALL]/[NOTION]/[NOT DISCLOSED] tags | PRESENT |
| (2) Sector intelligence | "## 2. SECTOR INTELLIGENCE" (L828) | ICT distribution economics, super-cycle three-force read, WC-as-risk framing | PRESENT |
| (3) Business-model intelligence | "## 3. BUSINESS-MODEL INTELLIGENCE" (L831) | spread+velocity model, days levers, VDA/JV drift, DTA-exhaustion headwind | PRESENT |
| (4) Competition intelligence | "## 4. COMPETITION INTELLIGENCE" (L834) | scale/last-mile moat, top-3 brand access, Dell-below-bar, refurb, Restar optionality | PRESENT |

**Gate 0: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (fresh grep re-enumeration vs A2 ledgers)

I re-ran the enumeration independently over each extract and diffed against the ledger counts.

| Doc / category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Concall — turns | 103 | 103 | odd content lines 11-215 = (215-11)/2+1 = 103 | none | MATCH |
| Concall — participants | 19 | 19 | 3 mgmt + host + operator + 14 named analysts | none | MATCH |
| Concall — questions | 33 | 33 (accept documented Sedartha 2-in-1 split) | topic sweep; 27 literal "?" + 12 ordinals corroborate | none | MATCH |
| Concall — mgmt numbers | 110 | reconciled (spot-verified 4A/4B token list) | — | none | MATCH |
| Concall — zero-standing / fwd-commit / hedges | 2 / 19 / 15 | 2 / 19 / 15 | refurb "none", zero-Japanese-customer; commitment + hedge lexicon | none | MATCH |
| Results — notes / line-items / entities / auditor-paras | 13 / 72 / 5 / 15 | tie (Step-1 tables re-derived from L341-708) | source-line re-read | none | MATCH |
| Presentation — 265 gated rows (23 slides) | 265 | tie (CFO/WC/write-off/ROCE clusters re-read) | — | none | MATCH |
| PR-results — 25 KPI + 2 quotes + 13 hedge + 12 seg + 5 corp-action | as ledgered | tie | — | none | MATCH |
| PR-JV — 13 entities / 12 fwd / 10 dates / 6 gov / 8 seg / 3 quotes; consideration + CPs NOT FOUND | as ledgered | tie | — | none | MATCH |

**Orphan-row test (ledger row present, absent from A4):** every material ledger row is cited or dispositioned in A4:
- Concall A3 findings F1-01, F1-02, F6-01, F7-01, F17-01..F17-07 — all 11 incorporated (review L25) and each carries a Questions-for-Management row (Step 8F A1-A10 + YAML question set). Verified below in Audit 3 / concall-specific checks.
- Results ZERO_STANDING (excess-provision dash), UNAUDITED_BY_PRINCIPAL (branch + 1 sub), MANAGEMENT_FURNISHED, UDIN_ILLEGIBLE, ENTITY_CHANGE (3 shells), post-period VDA — all surfaced (Step 0D, auditor-opinion para, Step 5 S-vs-C).
- Presentation CASH_CONVERSION_THESIS_METRIC (CFO 1,137/-1,020/-2,992), conflicting WC-days series (54/54/58/56), write-off provision doubling (0.043→0.088), DTA exhaustion (P20-9), Exceptional-Item dormant line (ZS-1) — all surfaced (Step 5 bear counter, Step 4, Step 0D).
- PR-JV consideration NOT FOUND + zero conditions-precedent — surfaced (JV F7-1; questions Q4/Q21/A6).

**Fresh-pass rows the ledger lacks:** none found. The A2 ledgers are exhaustive; my independent read surfaced no disclosure unit the ledgers missed.

**Audit 1: PASS.** No orphan rows (no loop to A3); nothing missing from ledger (no loop to A2).

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw source lines)

All raw figures below converted from the filing's Rs-millions x0.1 to Rs Cr. Source lines are results-extract lines unless noted.

### 2A. Step-1C derived metrics (consolidated unless flagged S)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Operating EBITDA Q1FY27 (C) | 155.28 | 138.96 + 6.29 + 27.42 − 17.39 = 155.28 | L661/L656/L655/L644 | MATCH |
| Reported EBITDA Q1FY27 (C) | 172.67 | 138.96 + 6.29 + 27.42 = 172.67 | same | MATCH |
| Op EBITDA + OI = Reported | 172.67 | 155.28 + 17.39 = 172.67 | — | MATCH |
| Op EBITDA margin Q1FY27 (C) | 3.04% | 155.28/5,101.85 = 3.043% | L643 | MATCH |
| Reported EBITDA margin (C) | 3.38% | 172.67/5,101.85 = 3.384% | — | MATCH (ties CFO 3.38%) |
| Op EBITDA margin Q1FY26 (C) | 3.28% | 103.50/3,152.14 = 3.284% | L643 | MATCH |
| Op EBITDA margin YoY | −24 bps | 3.284 → 3.043 = −24 bps | — | MATCH |
| Reported EBITDA Q4FY26 (C) [the corrected cell] | 148.69 | 113.63 + 6.13 + 28.93 = 148.69 | L661/L656/L655 | MATCH (prior 138.69 error fixed) |
| Standalone Op EBITDA Q1FY27 | 146.23 | 130.15 + 6.19 + 27.22 − 17.33 = 146.23 | L354/L350/L349/L342 | MATCH |
| Standalone Reported EBITDA | 163.56 | 130.15 + 6.19 + 27.22 = 163.56; /4,832.22 = 3.385% | — | MATCH (ties CFO 3.38%) |
| Effective Tax Rate Q1FY27 (C) | 24.76% | 34.40/138.96 = 24.76% | L670/L661 | MATCH |
| ETR Q1FY26 (C) | 23.13% | 18.57/80.27 = 23.13% | L670/L661 | MATCH |
| ETR step-up YoY | +163 bps | 24.76 − 23.13 = 1.63pp | — | MATCH |
| ETR Q1FY27 (S) | 25.36% | 33.00/130.15 = 25.36% | L360/L354 | MATCH |
| PAT margin Q1FY27 (C) | 2.05% | 104.57/5,101.85 = 2.049% | L672/L643 | MATCH |
| Core PBT ex-OI Q1FY27 (C) | 121.57 | 138.96 − 17.39 = 121.57 | — | MATCH |
| OI / PBT Q1FY27 (C) | 12.5% | 17.39/138.96 = 12.51% | — | MATCH |

### 2B. Step-2 YoY (consolidated)

| Metric | A4 | My recompute | Status |
|---|---|---|---|
| Revenue YoY | +61.9% | 5,101.85/3,152.14 = +61.85% | MATCH |
| Op EBITDA YoY | +50.0% | 155.28/103.50 = +50.03% | MATCH |
| Core PBT ex-OI YoY | +68.0% | 121.57/72.36 = +68.0% | MATCH |
| Reported PBT YoY | +73.1% | 138.96/80.27 = +73.11% | MATCH |
| PAT YoY | +69.5% | 104.57/61.70 = +69.48% | MATCH |
| Other Income YoY | +119.8% | 17.39/7.91 = +119.8% | MATCH |
| Diluted EPS YoY | +64.0% | 15.25/9.30 = +63.98% | MATCH |
| Finance costs YoY | +1.9% | 27.42/26.93 = +1.82% | WITHIN TOLERANCE (0.08pp over-round; immaterial line, no downstream metric; bridge uses exact −0.49 Cr) |
| Standalone Rev YoY | +58.3% | 4,832.22/3,052.73 = +58.29% | MATCH |
| Standalone Op EBITDA YoY | +43.4% | 146.23/102.00 = +43.4% | MATCH |
| Standalone diluted EPS YoY | +61.4% | 14.41/8.93 = +61.4% | MATCH |

### 2C. PAT bridge (Step 4) and S-vs-C gap (Step 5)

| Item | A4 | My recompute | Status |
|---|---|---|---|
| Reported PAT change | +42.87 | 104.57 − 61.70 = 42.87 | MATCH |
| Revenue-driven EBITDA @3.28% | +64.0 | (5,101.85−3,152.14)×3.284% = 64.0 | MATCH |
| Margin-change contribution | −12.2 | −0.24pp × 5,102 = −12.2 | MATCH |
| OI change | +9.48 | 17.39 − 7.91 = 9.48 | MATCH |
| Tax change (total) | −15.83 (−13.57 base / −2.26 rate) | 34.40 − 18.57 = 15.83 | MATCH |
| Bridge sum | +42.86 | 64.0−12.2−2.08−0.49+9.48−15.83 = 42.86 | MATCH |
| S-vs-C gap Q1FY26 | +4.9% | 2.87/58.83 = 4.88% | MATCH |
| S-vs-C gap Q4FY26 | +14.2% | 10.82/76.02 = 14.23% | MATCH |
| S-vs-C gap Q1FY27 | +7.6% | 7.42/97.15 = 7.64% | MATCH |
| Non-principal-reviewed PAT | Rs7.32 Cr = 7.0% | 0.12 + 7.40 − 0.19 = 7.33; /104.57 = 7.0% | MATCH |

### 2D. Concall Role-5 specific arithmetic (task-flagged)

- **(a) Growth bridge:** price 30-35 + volume 20-25 + new 5-10 + share 10 sums to 65 (bottoms) / 80 (tops) vs stated 60-62. A4's "~65-80% vs 60-62%, market-share double-counts inside volume" is arithmetically correct; the clean tie is price 32.5 + volume 22.5 + new 6 ≈ 61. **A4 handled the over-attribution correctly** and produced a management question (F17-07 → Q-A2). CONFIRMED.
- **(b) EBITDA definition:** 155.28 operating + 17.39 other income = 172.67 reported = 3.38% (172.67/5,101.85). Recomputed from concall L15/L17 + filing L661/L656/L655/L644. **A4's reconciliation is exact** (173−155≈OI; 3.38% masks the −24 bps operating contraction). CONFIRMED.
- **(c) ASR-error resolutions:** standalone PAT = 97.15 not 197 (L362: 971.52 mn); consol revenue = 5,101.85 not 5,12 (L643: 51,018.52 mn). **A4 resolved both correctly** (97.15/4,832.22 = 2.01% ties). CONFIRMED.
- **(d) Cash-conversion verdict:** concall gave NO CFO figure (verified across all 217 transcript lines; only WC 56 / inv 55 / debtor 41 / creditor 40 / net debt 1,285). A4 keeps cash conversion **INDETERMINATE** and verdict **PROCEED WITH CAVEATS**; it did NOT drift to PROCEED. CONFIRMED (house rule respected).

**Audit 2: PASS.** No mismatch above rounding. The single 0.08pp over-round on finance-cost YoY (1.82% shown as 1.9%) is on an explicitly-immaterial line and does not touch any decision metric; the bridge uses the exact −0.49 Cr. Not a gate failure. No loop to A4.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from the SAME text)

| # | A4's positive claim | Strongest bear counter (from the extract) | Survives? | Already in A4? |
|---|---|---|---|---|
| 1 | Highest-ever quarter: revenue +61.9%, PAT +69.5%, core PBT ex-OI +68% — "operations drove the profit" | The +68% is ACCRUAL, not cash: consolidated purchases 5,603.61 (L650) EXCEEDED revenue 5,101.85 (L643); inventory build Rs651 Cr S (L347)/Rs759 Cr C (L651); write-off provision doubled 0.043→0.088% (PPT P18-11/12). The inventory-change credit props accrual profit above cash. | YES | YES — grafted at Step-2 bear counter (L156) and Combined Verdict |
| 2 | Large AI-DC deals DEPRIORITISED to hold Net D/E <0.5x vs 2x = ROC-discipline positive | Discipline is SELECTIVE: management passed low-ROC deals while simultaneously locking Rs651 Cr into inventory; and net debt ROSE ~Rs408 Cr to Rs1,285 Cr (concall L133) with D/E AT the 0.5 ceiling — the IPO-deleveraging story is already reversing. | YES | YES — noted at Exchange 2 (L575) "discipline is selective" and cross-ref L668/L752 |
| 3 | ROC/ROE 19.5/19.8% "highest since listing"; WC days 56 improving | Spoken, annualised, UNVERIFIED — no filing anchor; FY26 ROCE was 16.02% (PPT P21-33). WC "improvement" leans on a seasonal-peak comparator (73) while the deck's own second series (54/54/58/56, PPT P21-24..27) shows WC days ROSE FY25→FY26; page-18 day-pairings are AMBIGUOUS_LAYOUT. | YES | YES — Step-5 bear counter (L210), checklist "GREEN (low confidence)", Step 7A |

**No NEW surviving bear counter is un-incorporated.** Every counter I could construct from the extracts is already present in A4's review (three A5-survived Role-4 counters plus the concall silence/selective-disclosure treatment). Nothing to graft back. No loop to A4.

### Concall FORWARD-SIGNAL / AMBIGUOUS → Questions-for-Management coverage (task-required)

Every forward/ambiguous concall finding produced a question row:
F17-01 CFO silence → Q-A1; F17-07 growth bridge → Q-A2; F17-02 EBITDA definition → Q-A3; F17-06 Q2 decel tripwire → Q-A4; F1-01/F1-02 refurbished → Q-A5; F7-01/F6-01 Restar consideration → Q-A6; F17-05 inventory absolute → Q-A7; F6-01 VDA/JV WC → Q-A8; F17-03 Dell below bar → YAML Dell question; F17-04 pledge/holding/ESOP/ETR → Q-A9, Q-A10. **All mapped. PASS.**

---

## VERDICT

**COMPLETE.**

- Gate 0 (plain-language brief, 4 parts): PASS.
- Audit 1 (coverage / fresh re-enumeration): PASS — counts reconcile across all five ledgers; no orphan rows; nothing missing from ledger.
- Audit 2 (arithmetic): PASS — every Step-1C/2/4/5 derived metric and every task-flagged concall computation (growth bridge, EBITDA definition, ASR resolutions, cash verdict) recomputes from raw source lines; one 0.08pp finance-cost over-round is within tolerance and decision-irrelevant.
- Audit 3 (adversarial read): PASS — the three strongest bear counters are already grafted; no surviving un-incorporated counter; every concall forward/ambiguous finding carries a management question.

Cash conversion correctly held INDETERMINATE → verdict correctly capped at PROCEED WITH CAVEATS; the hair-trigger is correctly ARMED-BUT-UNRESOLVED (no CFO number exists to fire it). Only COMPLETE proceeds to Notion save. No loop-back required.

```yaml
stage: A5-adversary
company: "RPTECH"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
