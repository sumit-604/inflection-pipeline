# A5 ADVERSARY / COMPLETENESS AUDIT — RPTECH Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-08-04
**Target:** `review_rptech_q1fy27.md` (A4) | **Verdict:** INCOMPLETE (loop back to A4)

Fresh-context re-derivation. Every extract number below was re-read from the A1
files and every metric recomputed independently of A4's and A3's cites. Unit
conversion applied throughout: source INR Mn x0.1 = Rs Cr.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The MANDATORY PLAIN-LANGUAGE BRIEF (review line 392) is present with all four
labelled, non-empty parts carrying real content:

| Part | Heading | Line | Present / Empty |
|---|---|---|---|
| 1 | SUMMARY NARRATIVE | 395-396 | PRESENT (one dense paragraph, numbers-first, symmetric bull/bear, provenance-tagged) |
| 2 | SECTOR INTELLIGENCE | 398-399 | PRESENT (ICT-distribution economics, margin structure, WC-as-risk) |
| 3 | BUSINESS-MODEL INTELLIGENCE | 401-402 | PRESENT (spread/velocity, ROCE, model drift into services + semis, tax-tailwind end) |
| 4 | COMPETITION INTELLIGENCE | 404-405 | PRESENT (scale/reach edge, top-3 brands, Redington/Ingram peers, Restar optionality) |

**Gate result: PASS.** Deliverable is complete; no hard INCOMPLETE on this axis.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers)

Independent recount. Slide/page markers re-grepped; results notes, entities, and
line items re-read directly from the extract; press-release and JV categories
re-read against their full extracts (JV anchors independently grepped, lines
93-164).

| Category (doc) | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Presentation — slides/pages | 23 | 23 | `grep -c "^\[page N\]"` = 23 | none | MATCH |
| Presentation — gated rows total | 265 | 265 (41+86+86+11+11+1+5+23-… reconciled to summary) | ledger cross-foot | none material | MATCH |
| Results — pages | 30 | 30 | `grep -c "^\[page N\]"` = 30 | — | MATCH |
| Results — numbered notes | 13 | 13 | direct read: Standalone 1-6 (L393-437) + Consolidated 1-7 (L722-788) | none | MATCH |
| Results — line items | 72 | 72 | re-read standalone 24 + consol 31 + note-tables 17 | none | MATCH |
| Results — consolidation entities | 5 | 5 | direct read L504-511 | none | MATCH |
| Results — auditor paras | 15 | 15 | 5 standalone (L223-325) + 10 consol (L461-626) | none | MATCH |
| Results — board-agenda items | 12 | 12 | direct read L42-157 | none | MATCH |
| Results — annexure rows | 57 | 57 | Annexure II 10 + III 16 + IV 31 | none | MATCH |
| Results — signatures / footnotes / zero-standing | 10 / 20 / 40 | 10 / 20 / 40 | ledger sweep, spot-verified | none | MATCH |
| PR (results) — KPI/quotes/hedges/segment/actions | 25/2/13/12/5 | same | full re-read of 185-line extract | none | MATCH |
| JV — entities/commitments/dates/gov/segments/quotes | 13/12/10/6/8/3 | same | ledger + anchor grep (26%, Oct-2026, 74%, 50+, US$4bn, $150bn all confirmed) | none | MATCH |
| JV — consideration / conditions-precedent | 0 / 0 (NOT FOUND) | 0 / 0 | grep "consideration|Fair Market|SPA" in JV extract = no match | none | MATCH (correctly logged NOT FOUND) |

**Fresh pass found no row the ledgers lack. No missing_from_ledger (A2) failures.**

**Orphan check (ledger row present, absent from A4).** Every substantive flagged
row is addressed in A4:
- ENTITY_CHANGE (3 new subs) -> Step 0D Notes S6/C7, Step 6D, Q15. Cited.
- UNAUDITED_BY_PRINCIPAL + MANAGEMENT_FURNISHED (Singapore branch, 1 foreign sub,
  3 shells) -> Step 0D auditor opinion, Step 5 S-vs-C gap, Q10. Cited.
- ZERO_STANDING exceptional-item line -> Step 0D, Q6. Cited.
- CASH_CONVERSION_THESIS_METRIC / CFO AMBIGUOUS_LAYOUT -> Step 5 CFO discrepancy,
  Q2. Cited.
- DTA exhausted (P20-9) -> Step 4, Q8. Cited.
- Inventory write-off provision doubled (P18-11/12, 0.043%->0.088%) -> Q19. Cited.
- WC/debtor/creditor days -> Step 5. Cited.

One minor, non-failing observation (reviewed, no finding): balance-sheet row
P20-33/34 (Trade Payables MSME grew 3 -> 568 Mn FY23-FY26, ~189x) is not
explicitly named in A4. It is a historical annual BS row the ledger itself left
to interpretation; it is subsumed in A4's WC/net-debt narrative (supplier-credit
financing) and is directionally consistent, so it is treated as reviewed-no-finding,
not an orphan.

**Coverage result: PASS.** Counts reconcile; no orphans; no missing-from-ledger.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted Mn, x0.1 to Cr)

Every extraction tie-out (all four periods, standalone and consolidated) matches
A4's Step 1 tables exactly — Revenue, OI, purchases, changes-in-inventory,
expenses, PBT, tax, PAT, owners/NCI split, and EPS all confirmed at their cited
lines. Derived metrics recomputed:

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA consol Q1FY27 (PBT+D+Fin-OI) | 155.28 | 138.96+6.29+27.42-17.39 = 155.28 | 655/656/661/644 | OK |
| Op EBITDA standalone Q1FY27 | 146.23 | 130.15+6.19+27.22-17.33 = 146.23 | 349/350/354/342 | OK (ties deck 1,462 Mn) |
| Op EBITDA margin consol Q1FY27 | 3.04% | 155.28/5101.85 = 3.043% | — | OK |
| Op EBITDA margin YoY chg | -24 bps | 3.043% - 3.283% = -24 bps | — | OK |
| **Reported EBITDA consol Q4FY26 (PBT+D+Fin)** | **138.69** | **113.63+6.13+28.93 = 148.69** | **661/656/655 (Mn 1,136.32/61.27/289.26)** | **MISMATCH (-10.00 Cr)** |
| Reported EBITDA consol Q1FY27 | 172.67 | 138.96+6.29+27.42 = 172.67 | — | OK |
| Reported EBITDA consol Q1FY26 | 111.41 | 80.27+4.21+26.93 = 111.41 | — | OK |
| Reported EBITDA consol FY26 | 499.28 | 371.27+21.52+106.49 = 499.28 | — | OK |
| Core PBT ex-OI consol Q1FY27 | 121.57 | 138.96-17.39 = 121.57 | — | OK |
| Effective tax rate consol Q1FY27 | 24.76% | 34.40/138.96 = 24.76% | 670/661 | OK |
| ETR YoY step-up | +163 bps | 24.76% - 23.13% = 163 bps | — | OK |
| Revenue YoY consol | +61.9% | 5101.85/3152.14-1 = 61.85% | 643 | OK |
| Op EBITDA YoY consol | +50.0% | 155.28/103.50-1 = 50.03% | — | OK |
| Core PBT ex-OI YoY consol | +68.0% | 121.57/72.36-1 = 68.0% | — | OK |
| PAT YoY consol | +69.5% | 104.57/61.70-1 = 69.5% | 672 | OK |
| Diluted EPS YoY consol | +64.0% | 15.25/9.30-1 = 63.98% | 708 | OK |
| Standalone Rev / PAT / EPS YoY | +58.3 / +65.1 / +61.4% | 58.3% / 65.14% / 61.4% | 341/362/381 | OK |
| PAT bridge sum | +42.86/87 | 64.0-12.2-2.08-0.49+9.48-13.57-2.26 = +42.88 | — | OK (ties within rounding) |
| S-vs-C PAT gap Q1FY26 | +4.9% | (61.70-58.83)/58.83 = 4.88% | 362/672 | OK |
| S-vs-C PAT gap Q4FY26 | +14.2% | (86.84-76.02)/76.02 = 14.23% | — | OK |
| S-vs-C PAT gap Q1FY27 | +7.6% | (104.57-97.15)/97.15 = 7.64% | — | OK |
| Inventory build ~5x (standalone) | ~5x | 651.45/124.88 = 5.22x | 347 | OK |
| Singapore sub PAT / uplift | ~99% | 7.40 of 7.42 Cr | 564-565 | OK |
| Non-principal-reviewed PAT | Rs7.32 Cr / 7.0% | 0.117+7.399-0.193 = 7.32; /104.57 = 7.0% | 282/564/600 | OK |
| FY26 CFO deck | Rs113.7 Cr | 1,137 Mn x0.1 = 113.7 | PPT L733 | OK (Rs514 Notion is memory, correctly LOGGED unreconciled) |

### FAIL — one arithmetic mismatch (loop back to A4)

**Step 1C, Reported EBITDA row, Q4 FY26 (Consolidated) cell = 138.69.**
Correct value = **148.69 Cr**. Recompute: PBT 113.63 + D&A 6.13 + Finance 28.93 =
148.69 (source Mn 1,136.32 / 61.27 / 289.26 at L661/656/655). A4's own Operating
EBITDA for the same cell (132.64) plus Other Income (16.05) also equals 148.69,
confirming the printed 138.69 is a transposition error of exactly 10.00 Cr. Above
rounding -> FAIL. Non-load-bearing (the cell is not used downstream), but the
mechanical rule admits no discretion: the cell must be corrected by A4 before save.

Minor characterization note (not a mismatch, no fix required): Step 2 attributes
the full 5.5pp diluted-EPS-vs-PAT gap to "YoY dilution"; ~1.9pp of it is actually
the NCI wedge (owners' PAT grew 67.6% vs total PAT 69.5%), the rest dilution.
Numbers are all disclosed and correct; only the attribution is loose.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter per top-3 positive claim)

### Claim 1 (Step 2 / brief): "Growth is REAL, not a treasury trick — core operating PBT ex-OI grew +68% YoY."
**Bear counter (same extract):** The +68% core PBT sits on top of a Rs651 Cr
standalone / Rs759 Cr consolidated inventory build in which **purchases (consol
5,603.61 Cr) exceed revenue (5,101.85 Cr) by ~Rs500 Cr** (L650 vs L643). The
changes-in-inventory credit of Rs758.97 Cr (L651) is the very line holding
reported gross profit up while stock is pre-loaded. The profit is real on accrual,
but "real" is not "cash" and not "durable": the deck's own **Provision for
Inventory Write-off % has DOUBLED, 0.043% -> 0.088%** (PPT P18-11/12), signalling
rising impairment risk on exactly the stock that manufactured the accrual profit.
**Survives.** A4 discusses the inventory build and weak-CFO signal but never links
the doubled write-off provision to the "growth is REAL" claim as a quality caveat.
**Graft required.**

### Claim 2 (Step 5 / brief): "Working-capital days improved — WC days 73->56, debtor 41, cash cycle better by 17 days — GREEN."
**Bear counter (same extract):** The 17-day improvement compares Q1 FY26 (73, a
seasonal peak) to Q1 FY27 (56). The **same deck carries a second, conflicting
WC-days series (page 21: FY24/FY25/FY26/Q1 = 54/54/58/56, PPT P21-24..27)** on
which WC days actually **ROSE FY25->FY26 (54 -> 58)** and Q1 sits at 56, i.e. near
the top of the multi-year band, not a clean structural improvement. Worse, the
page-18 Inventory/Debtor/Creditor cluster is flagged **AMBIGUOUS_LAYOUT** by A2
(metric-to-value pairing uncertain: inventory 55-or-53, debtor 53-or-55), so the
"41 debtor days" and "55 inventory days" A4 quotes as GREEN are not confidently
assignable from the source. **Survives.** A4 uses 73->56 uncritically and does not
surface the conflicting annual series or the AMBIGUOUS_LAYOUT caveat.
**Graft required.**

### Claim 3 (Steps 6A/8 / brief): "On every disclosed metric the quarter lands at/above base; share-count correction (6.64 Cr vs 9 Cr) raises intrinsic per-share value and the Hurdle Ratio — likely favourable."
**Bear counter (same extract):** "At/above base" is true only on the disclosed
growth cherries; the single BINDING metric (CFO) is undisclosed, six of twelve
checklist items are UNKNOWN, ROCE (a green/red gate) is AMBER with no Q1 number,
and the entire consolidated PAT premium is one Singapore subsidiary reviewed by an
"other auditor" whose report was "furnished by Management" (L561-593) — the least
independently verified rupee in the file. On the share-count point specifically,
A4 presents only the favourable side: EPS is disclosed directly so nothing changes
in reported terms; the diluted/basic spread has just OPENED (in-the-money ESOPs,
5,06,081 allotted 4-Aug plus an undisclosed residual option pool, Q12), so the
correction also flags **forward dilution**, and with the net DTA exhausted and ETR
+163 bps the lower share count must carry EPS growth against a rising tax drag.
**Partially survives.** Most of the cash/ROCE/subsidiary caveats are already in
A4 (it caps at PROCEED WITH CAVEATS); the only un-incorporated fragment is that
the share-count correction cuts both ways (forward dilution + tax drag), which A4
frames one-directionally as "likely favourable." **Graft the two-sided framing.**

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**. Two gaps, both A4-owned:

1. **Arithmetic FAIL** — Step 1C Reported EBITDA, Q4 FY26 consolidated cell reads
   138.69; correct is 148.69 (PBT 113.63 + D 6.13 + FinCost 28.93). Fix the cell.
2. **Surviving bear counters not incorporated** — (a) doubled inventory
   write-off provision (0.043%->0.088%) as a quality caveat on the "+68% core PBT
   is REAL" claim; (b) the conflicting page-21 WC-days series (54/54/58/56, WC days
   rose FY25->FY26) plus AMBIGUOUS_LAYOUT on debtor/inventory pairing, qualifying
   the "days improved / GREEN" claim; (c) the share-count correction is two-sided
   (forward ESOP dilution + exhausted DTA / rising ETR), not one-directionally
   favourable. Graft these into A4 before Notion save.

Deliverable gate PASS. Coverage PASS. Arithmetic and adversarial audits FAIL as
above. Only COMPLETE proceeds to save; this run does not.

```yaml
stage: A5-adversary
company: "RPTECH"
quarter: "Q1FY27"
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
  - metric: "Reported EBITDA (PBT+D+FinCost), Consolidated Q4 FY26"
    a4_value: 138.69
    recomputed: 148.69
    source_line: "results L661 PBT 1,136.32 + L656 D&A 61.27 + L655 Finance 289.26 (Mn x0.1); ties to A4 Op EBITDA 132.64 + OI 16.05"
surviving_bear_counters:
  - claim: "Growth is REAL — core operating PBT ex-OI +68% YoY (Step 2 diagnostic 3)"
    counter: "Same-period inventory build Rs651 Cr(S)/Rs759 Cr(C) with purchases (5,603.61) exceeding revenue (5,101.85) means the changes-in-inventory credit props the accrual profit; deck's own inventory write-off provision DOUBLED 0.043%->0.088%, flagging impairment risk on the pre-loaded stock. 'Real' is accrual, not cash or durable."
    source_line: "results L650/L643/L651; presentation P18-11/P18-12"
  - claim: "Working-capital days improved 73->56, GREEN (Step 5 / checklist #2)"
    counter: "Deck carries a second conflicting WC-days series (page 21: FY24/FY25/FY26/Q1 = 54/54/58/56) on which WC days ROSE FY25->FY26; the 73->56 story leans on a seasonal-peak comparator, and the page-18 inventory/debtor/creditor pairings are A2-flagged AMBIGUOUS_LAYOUT (inventory 55-or-53, debtor 53-or-55)."
    source_line: "presentation P21-24..27 (L734-735); P18-1..6 AMBIGUOUS_LAYOUT (L595-598)"
  - claim: "Share-count correction 6.64 Cr vs Notion 9 Cr raises intrinsic per-share value / Hurdle Ratio, 'likely favourable' (Step 7 / 0C)"
    counter: "Two-sided: EPS is disclosed directly so nothing changes in reported terms; the diluted/basic spread just opened (in-the-money ESOPs, 5,06,081 allotted plus undisclosed residual pool) flagging forward dilution, and with net DTA exhausted and ETR +163bps the lower count must carry EPS growth against a rising tax drag. A4 frames it one-directionally."
    source_line: "results L142-147, L380-381 vs L707-708; presentation P20-9 (DTA nil FY26)"
loop_back_to: "A4"
gap: "(1) Fix Step 1C Reported EBITDA Q4 FY26 cell 138.69 -> 148.69. (2) Graft three surviving bear counters (doubled inventory write-off provision vs the 'growth is REAL' claim; conflicting page-21 WC-days series 54/54/58/56 plus AMBIGUOUS_LAYOUT vs the 'days improved/GREEN' claim; two-sided read of the share-count correction) before Notion save."
```
