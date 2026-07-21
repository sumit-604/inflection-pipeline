# A5 ADVERSARY / COMPLETENESS AUDIT — SOUTHWEST — Q1 FY27 (re-audit, loop 2)

Agent A5. Fresh context: I see only the A4 review, the two A1 extracts, and the two A2 ledgers. Every number re-derived independently from the extracts (Rs Mn x0.1 to Rs Cr per A1 headers, results L8 / presentation L8); A4's and A3's cites were checked, not trusted. This is a re-audit after the A4 loop-back that grafted the order-book bear counter (F16.2 / Step 6E). That graft is verified below and the review is re-attacked fresh.

---

## AUDIT 1 — COVERAGE

Independent grep/manual re-enumeration of both extracts, diffed against the two A2 ledgers.

| Category | A2 count | My fresh count | Orphan / note | Status |
|---|---|---|---|---|
| Results: numbered notes | 0 | 0 (`^\s*[0-9]+\.\s` = 0; 4-page press release, not Reg 33) | — | PASS |
| Results: financial line items (L86-90) | 5 | 5 | — | PASS |
| Results: financial period cells (5x4) | 20 | 20 | — | PASS |
| Results: table footnote (L91 "* On Consolidated Basis") | 1 | 1 | — | PASS |
| Results: Q1 highlight bullets (L93-111) | 13 | 13 | **E8 Oil India 2D/3D seismic empanelment (L102-103) enumerated but ABSENT from A4** | **FAIL → A3** |
| Results: CMD commentary claims (L115-148) | 9 | 9 | — | PASS |
| Results: JV/coal statements (cross-ref) | 7 | 7 | — | PASS |
| Results: absent Reg-33 unit classes (K1-K15) | 15 | 15 | all carried as first-class ND in A4 0D | PASS |
| Results: letterhead/addressee/sig/about/contact | 11 | 11 | J2 phone-digit typo immaterial | PASS |
| Presentation: slides (`[page N]`) | 40 | 40 | — | PASS |
| Presentation: line items (sl33 16 + sl35 16 + sl36 42 + sl38 6) | 80 | 80 | each sub-count re-derived; sl36 42 = 22 asset + 20 eq/liab | PASS |
| Presentation: chart data points | 110 | 110 (8+8+6+11+25+6+12+32+2) | — | PASS |
| Presentation: footnotes | 7 | 7 | — | PASS |
| Presentation: ZERO_STANDING rows | 7 | 7 | OCI/CWIP/Loans/held-for-sale/NCI/CurTaxLiab reviewed (F1.1/F1.2/F9.1) | PASS |
| Presentation: DISCLOSURE_INCONSISTENCY (Ritolia sl8) | 1 | 1 | reviewed (F14.1, Q15) | PASS |

**No row my fresh pass found is missing from either ledger → no FAIL to A2.** (A2's results-ledger reconciliation prose is internally loose — it says Category G is "not added again" yet the stated total 70 only closes if the 7 G cross-refs are counted; 48 primary + 15 K = 63, +7 G = 70. This is A2 bookkeeping cosmetics only; every distinct disclosure unit is enumerated and no content is missed. Noted, not failed.)

**Ledger-row → A4 disposition spot-check** (every flagged row must be cited in A4 or reviewed-no-finding):
- `TITLE_LABEL_MISMATCH` "Q on Q" vs "Y on Y" → A4 F14-01, Step 3, Q14. Cited.
- F2 standalone "on similar lines" → A4 First-Class Metric, Q4. Cited.
- Slide 6 Rs 307 cr HZL vs slide 32 Rs 3,070 Mn Rajasthan → A4 F16.2 / Step 6E. Cited (A4 correctly overrides the ledger's "do not conflate" note).
- Ritolia caption/body → A4 F14.1, Q15. Cited.
- Slide 37 DATA_GAP (no Q1 net-worth/D-E/ROE-ROCE) → A4 F16.1, Q12. Cited.
- OCI swing / Current Tax Liability / held-for-sale → A4 F9.1 / F1.2 / F1.1. Cited.

**Orphan row (ledger present, A4 absent) → FAIL to A3:**
- **Results E8 / presentation slide-32 bullet:** *"Company empaneled by Oil India Limited for providing 2D/3D Seismic Data Acquisition Services across OIL's onshore"* (results L102-103; pres L1011-1012). A distinct forward growth catalyst — a new-scope empanelment with a marquee PSU client — enumerated by A2 (E8) and the slide-32 operational bullets. A4 carries it nowhere: not in the growth-trigger table (6D), not in the monitorables/catalyst list, not in Questions 1-17, not in Section C. A4's own rule (Step 8.5: "every A3 FORWARD-SIGNAL … maps to >= 1 row"; monitorables "seeded by A3 commitment registers F6") means the omission traces to a missing A3 commitment-register entry. A3 must add the empanelment as a forward-signal / monitorable; A4 then carries it.

**Secondary coverage observation (recommend A3 flag; not the binding fail):** snapshot slide 3 (L94-95) labels **"23% ROCE"**, whereas slide 37 (L1170-1175) pairs FY26 as ROE 23% / ROCE 16%. A4 correctly used the conservative ROCE = 16% in Step 7 and held the pillar, so no valuation harm — but the same-metric label contradiction (snapshot mislabels ROE as ROCE) is the same class A3 flagged for Ritolia and is currently unlogged. Low materiality; recommend A3 add a one-line flag.

**Coverage verdict: FAIL — one orphan (E8, Oil India empanelment) → A3.**

---

## AUDIT 2 — ARITHMETIC

Every derived cell in A4's tables recomputed from raw extract numbers (slide 33 L1031-1063; slide 35 L1074-1106; slide 36 L1112-1142; slide 38 L1199-1210). All load-bearing cells shown; all others reconcile to rounding.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Total Income Q1FY27 (Rev+OI) | 62.1 | 61.7+0.4 = 62.1 | L1033,L1041 | OK |
| Op EBITDA (Rev−TotExp) Q1FY27 | 14.9 | 61.7−46.8 = 14.9 | L1033/35 | OK |
| Op EBITDA margin Q1FY27 | 24.15% | 149/617 = 24.15% | L1037/33 | OK |
| Op EBITDA margin Q1FY26 | 14.43% | 58/402 = 14.43% | L1035/33 | OK |
| Reported EBITDA Q1FY27 (PBT+D+Fin) | 16.6 | 11.9+3.0+1.7 = 16.6 | L1051,43,45 | OK |
| Core Op PBT ex-OI Q1FY27 | 11.5 | 11.9−0.4 = 11.5 | L1051,41 | OK |
| Core Op PBT ex-OI ex-JV Q1FY27 | 10.2 | 10.6−0.4 = 10.2 | L1047,41 | OK |
| Effective tax rate Q1FY27 (Tax/PBT) | 21.8% | 26/119 = 21.85% | L1053/51 | OK |
| ETR pre-JV Q1FY27 (Tax/PBSJV) | 24.5% | 26/106 = 24.53% | L1053/47 | OK |
| Revenue YoY | +53.5% | (617−402)/402 = 53.48% | L1033 | OK |
| Op EBITDA YoY | +156.9% | (149−58)/58 = 156.9% | L1037 | OK |
| Op EBITDA margin bps YoY | +972 | 2415−1443 = 972 | L1039 | OK |
| Depreciation YoY | +42.9% | (30−21)/21 = 42.86% | L1043 | OK |
| Finance cost YoY | −15.0% | (17−20)/20 = −15.0% | L1045 | OK |
| Operating EBIT YoY | +221.6% | (11.9−3.7)/3.7 = 221.6% | der. L1037,43 | OK |
| Core Op PBT ex-OI YoY | +475% | (11.5−2.0)/2.0 = 475% | der. | OK |
| Core Op PBT ex-OI ex-JV YoY | +500% | (10.2−1.7)/1.7 = 500% | der. | OK |
| Reported PBT YoY | +283.9% | (119−31)/31 = 283.9% | L1051 | OK |
| PAT YoY | +287.5% | (93−24)/24 = 287.5% | L1055 | OK |
| PAT margin bps YoY | +910 | 1507−597 = 910 | L1057 | OK |
| EPS YoY | +287.3% | (3.06−0.79)/0.79 = 287.3% | L1063 | OK |
| PAT bridge: Op EBITDA delta | +9.1 | 14.9−5.8 = 9.1 | L1037 | OK |
| PAT bridge: = PBT change | +8.8 | 9.1−0.9+0.3−0.7+1.0 = 8.8; also 11.9−3.1 | L1051 | OK |
| PAT bridge: = reported PAT change | +6.9 | 8.8−1.9 = 6.9; also 9.3−2.4 | L1055 | OK |
| JV share of consolidated PAT | 14.0% | 13/93 = 13.98% | L1049/55 | OK |
| Receivable days FY25 (TR/Rev x365) | 154.5 | 763/1803 x365 = 154.5 | L1132/76 | OK |
| Receivable days FY26 | 175.0 | 1166/2430 x365 = 175.1 | L1132/76 | OK |
| Inventory days FY26 (Inv/TotExp) | 100.6 | 509/1847 x365 = 100.6 | L1129/78 | OK |
| Payable days FY26 (TP/TotExp) | 45.9 | 232/1847 x365 = 45.9 | L1133/78 | OK |
| Cash conversion cycle FY26 | ~230 | 175.0+100.6−45.9 = 229.7 | der. | OK |
| Capex FY26 (PPE+CWIP) | 92.2 | 918+4 = 922 Mn | L1114-15 | OK |
| Cash & equiv FY25→FY26 | 19.4→1.3 (−93%) | 194→13 Mn, −93.3% | L1134 | OK |
| Gross borrowings FY26 (LT+ST) | 78.6 | 160+626 = 786 Mn | L1120/31 | OK |
| Net debt FY26 (gross−cash&equiv) | 77.3 | 78.6−1.3 = 77.3 | der. | OK |
| Order book net QoQ add | +180.1 Cr (+31.0%) | (7613−5812)/10 = 180.1; /581.2 = 31.0% | L546 | OK |
| ROCE base (0.5xROCE+7.5) | 15.5x | 0.5x16+7.5 = 15.5 | L1170 (sl.37 ROCE 16%) | OK |

Standalone-vs-consolidated PAT gap: A4 records ND (both docs consolidated-only, results K5) — confirmed unrecoverable from today's extracts, correctly ND not fabricated; JV-share-of-PAT (14.0%) kept distinct from the S-vs-C gap. Correct handling.

**Arithmetic verdict: PASS — zero mismatches above rounding.** The PAT bridge closes exactly both ways (+6.9 Cr). Note (not a FAIL; no A4 table affected): the press-release body claim "PAT … more than 3.90 fold" (results L97) is a mild company overstatement (93/24 = 3.875x); A4 correctly used +287.5% throughout and did not import the 3.90 figure.

---

## AUDIT 3 — ADVERSARIAL READ

Three most positive claims in A4, each attacked from the same extracted text.

**Positive claim 1 — "PAT +287.5% is genuinely operating-led, NOT treasury/one-off; ~100%+ recurring" (Step 2 D4, Step 4; bridge labels Share of JV "+1.0 Recurring").**
Strongest bear counter from the extract: the equity-accounted **Share of Profit from JVs leapt 3 → 13 Mn YoY (+333%)** (L1049), and Q1 FY27's 13 Mn is **~93% of the ENTIRE FY26 full-year JV profit of 14 Mn** (L1092) — one quarter nearly equals a full prior year. It is now **14.0% of consolidated PAT** (1.3/9.3 Cr), sits below the operating line, and the JV audit status is ND (F8.1/Q16). Labeling a +333% single-line spike "Recurring" (Step-4 bridge) is unproven; the pattern (one quarter ~ one prior year) is the fingerprint of a lump / catch-up / revaluation in the Oman JV. Normalise the JV to its FY26 quarterly run-rate (~3.5 Mn) and Q1 PAT falls ~10% (9.3 → ~8.4 Cr) and the 15.07% PAT margin softens.
**SURVIVES.** Extract-supported (L1049 vs L1092 vs L1055). A4 flags the JV concentration (14%) and audit status but nowhere notes the magnitude anomaly (Q1 JV ~ full FY26 JV, +333% YoY) and nowhere challenges the bridge's "Recurring" label at the PAT level. Must be grafted into A4. **→ FAIL to A4.**

**Positive claim 2 — "Operating EBITDA margin +972 bps to 24.15%, genuine and holding FY26's 23.99%" (Step 2).**
Bear counter: the deck discloses only an **aggregated "Total Expenses"** line — no materials/employee/other split (ND, results K9-K13) — while the CMD cites "substantial increase in input cost" (L123) and Intangibles-under-development rose 143 → 193 Mn (L1119). The margin jump cannot be decomposed into operating leverage vs classification/capitalisation.
**DOES NOT SURVIVE.** The move also holds at the full-FY26 level (23.99%, L1082) and recurs annually FY24→FY26; the capitalised intangibles are coal-GR / Oman project costs, not services COGS, so they cannot mechanically inflate the services margin. A4 already flags the cost-line ND and the intangibles build (F12.1 / Q17). No graft.

**Positive claim 3 — "Coal first-production target FY27-28 is EARLIER than the house FY29 tripwire; no thesis-broken trigger fired" (Step 6C/6D).**
Bear counter: FY27-28 is a management aspiration and the **GR has not even been submitted** ("being finalised for early submission," L682); the earlier date is promise, not delivery.
**DOES NOT SURVIVE as new.** A4 already logs the binary GR-slip risk, AMBER-tracks it, and dedicates Question 6 to reaffirm/deny the target. Already incorporated.

**Verification of the previously-grafted order-book counter (re-audit focus):** the F16.2 double-count / Step 6E graft is **properly and completely incorporated** — it appears in 6B (item 8), 6C, 6D, 6E, Step 7 (Growth-Visibility premium explicitly NOT credited), Step 8 gate 2, Section C, Caveat 4, the flags block, and Questions 2 & 8. Re-attacked fresh: the arithmetic (net QoQ add 180.1 Cr < the single 307 Cr order; L546) and the identity claim (3,070 Mn Rajasthan order = the FY25 HZL 307 Cr award: same value, same "single largest" descriptor, same HZL-subsidiary customer, same Rajasthan location; L151-155 vs L1003-1004) are both extract-supported. This graft holds. No further action on the order-book counter.

---

## VERDICT

**INCOMPLETE.**

Two binding gaps:
1. **Coverage orphan → A3.** Oil India 2D/3D seismic empanelment (results E8 L102-103; pres slide-32 bullet L1011-1012) is enumerated by A2 but reviewed nowhere in A4 — a forward growth catalyst dropped from the commitment register, monitorables, and questions. A3 must add it; A4 then carries it.
2. **Surviving bear counter → A4.** The equity-accounted JV profit share is anomalously large this quarter (Q1 FY27 13 Mn ~ full FY26 14 Mn; +333% YoY; 14% of PAT; audit status ND). A4's "Recurring" bridge label and its "~100%+ recurring/operating PAT" framing must be qualified with this extract-supported non-recurrence risk before save.

**Re-entry point: A3** (earliest gate; the orphan originates in the A3 commitment register and cascades to A4). On the A4 re-run, graft the surviving JV-recurrence counter. Secondary (non-binding): A3 should also log the snapshot "23% ROCE" vs slide-37 "16% ROCE" label inconsistency — A4's number is already the conservative 16%.

Arithmetic audit fully passes; the previously-grafted order-book counter is verified correctly incorporated.

```yaml
stage: A5-adversary
company: "SOUTHWEST"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows:
    - "Results E8 / pres slide-32 bullet: Oil India 2D/3D Seismic empanelment (results L102-103; pres L1011-1012) — forward catalyst enumerated by A2, reviewed nowhere in A4 (no growth-trigger, monitorable, or question)"
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "PAT +287.5% is operating-led / ~100%+ recurring; Share of JV labelled 'Recurring' in the PAT bridge (Step 2, Step 4)"
    counter: "Equity-accounted JV profit share jumped 3->13 Mn YoY (+333%); Q1 FY27 (13 Mn) ~= the entire FY26 JV profit (14 Mn) and = 14% of consolidated PAT; JV audit status ND. One-quarter-~-one-prior-year is the fingerprint of a lump/catch-up, so the 'Recurring' label is unproven; normalising the JV run-rate cuts Q1 PAT ~10% (9.3->~8.4 Cr) and softens the 15.07% PAT margin"
    source_line: "presentation L1049 (JV 13 vs 3), L1092 (FY26 JV 14), L1055 (PAT 93)"
loop_back_to: "A3"
gap: "A3: add the Oil India 2D/3D seismic empanelment (E8, results L102-103 / slide-32 L1011) as a forward-signal to the commitment register and monitorables (also recommend logging the snapshot '23% ROCE' vs slide-37 'ROCE 16%' label inconsistency). A4 (on re-run): graft the surviving JV-recurrence bear counter — qualify the 'Recurring' JV bridge label and the '~100%+ recurring PAT' claim with the +333% YoY / Q1~=full-FY26 JV-lump risk (L1049/L1092/L1055). The previously-grafted order-book counter (F16.2/Step 6E) is verified correctly incorporated; no action there."
```
