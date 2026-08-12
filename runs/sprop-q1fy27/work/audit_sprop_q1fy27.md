# A5 ADVERSARY / COMPLETENESS AUDIT — Shriram Properties Limited (SPROP), Q1 FY27
# Auditor: A5 | model claude-opus-4-8 | fresh context (A4 review + A1 extracts + A2 ledgers only)
# Re-derived independently from the extracts; A4/A3 cites checked, not trusted.
# ROUND 2 (re-audit after A4 applied the four required fixes) — see RE-AUDIT section.

Anchor key: `R-Lxxx` results extract line; `P-Lxxx` presentation extract line;
`PR-Lxxx` press-release extract line. Results filing in Rs Lakhs, converted x0.01
to Rs Cr; presentation and press release native Rs Cr. Every recompute below is
built from the raw extracted cells, not from A4's derived tables.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

The A4 review carries a `SECTION D — PLAIN-LANGUAGE BRIEF` with all four labelled
parts present and carrying real content (line numbers as of round 2):

| Brief part | Location | Present? | Content check |
|------------|----------|----------|---------------|
| (1) Summary narrative | review L714 | **present** | ~22 lines of plain prose; -7.4% recognised-revenue fall, Other Income 328% of PBT, PAT -46%, AVOID stands. Non-placeholder. |
| (2) SECTOR intelligence | review L749 | **present** | Mid-market residential; e-Khata/Bangalore approval as live sector variable; JDA/JV revenue-share headwind. Non-placeholder. |
| (3) BUSINESS-MODEL intelligence | review L768 | **present** | Asset-light Own/JDA/JV/DM; earnings from Other Income not homebuilding; SC-gap reversal. Non-placeholder. |
| (4) COMPETITION intelligence | review L792 | **present** | Positioning, where SPL wins/weaker vs peers, moat 5/60, Uttarpara land as unrealised NAV. Non-placeholder. |

**GATE 0 RESULT: PASS.** All four brief parts present and non-empty (unchanged by the round-2 fixes).

---

## AUDIT 1 — COVERAGE (independent re-enumeration, diffed against A2 ledgers)

Fresh grep/manual sweep re-run over each extract; my counts vs the A2 ledger:

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Missing from ledger | Status |
|----------|----------|----------------|------------------------------------------|---------------------|--------|
| Results — notes | 17 | 17 (6 SA numbered + S-FN1 + 7 cons numbered + C-FN1/C-FN2/A1-FN1) | none | none | PASS |
| Results — line items | 59 | 59 (24 SA + 35 cons) | none | none | PASS |
| Results — zero_standing | 7 | 7 | none | none | PASS |
| Results — agenda items | 2 | 2 | none | none | PASS |
| Results — auditor paras | 11 | 11 (5 SA + 6 cons incl. EoM + Other Matter) | none | none | PASS |
| Results — entities | 31 | 31 (26 subs + 5 JVs) | none | none | PASS |
| Results — signatures | 5 | 5 | none | none | PASS |
| Presentation — slides | 26 | 26 | none | none | PASS |
| Presentation — numeric rows | 256 | 256 | none | none | PASS |
| Presentation — footnotes | 5 (+F0) | 6 (5 marked + F0 disclaimer) | none | none | PASS |
| Press release — pages | 4 | 4 | none | none | PASS |
| Press release — narrative claims | 21 | 21 | none | none | PASS |
| Press release — numbers/metrics | 28 | 28 | none | none | PASS |
| Press release — table line items | 4 | 4 | none | none | PASS |
| Press release — forward statements | 8 | 8 | none | none | PASS |

Ledger-reconciliation preamble (review L13) intact; every flag row traceable to
an A4 citation or "reviewed" mark. No orphan rows; no row my fresh pass surfaced
is absent from the ledger.

**AUDIT 1 RESULT: PASS.** Enumeration reconciles exactly; no A2 gap, no A3 orphan.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw cells)

Load-bearing recomputes all tie (Core Operating EBITDA −4.84 / +22.42; margin
−1150 bps; PBT-after-JV −34.8%; PAT −46.4%; ETR 22.5%; PAT bridge sums to −9.55;
deck-basis EBITDA row; standalone table; unit conversions; 70% PAT; net debt
+32.5% vs Mar'25; true FCF −34). Full detail in round 1.

The two round-1 mismatches are re-checked against the corrected review below in
the RE-AUDIT section; both now match my independent derivation.

**AUDIT 2 RESULT (round 2): PASS.** No mismatch above rounding remains.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims + strongest bear counter)

- **Positive claim 1 — finance-cost "relief".** Bear counter: fall is entirely the
  non-cash unwinding line 1.5→0 (P-L320); cash interest ROSE 20.8→21.2 (P-L319) on
  gross debt up 610→651 (P-L420). Round-1 SURVIVED → required grafting.
- **Positive claim 2 — "net debt flat QoQ (438→432)".** Bear counter: flat only via
  cash build funded by Rs 106 Cr fresh loan drawals (P-L382); gross debt +41 QoQ.
  Round-1 SURVIVED → required grafting.
- **Positive claim 3 — "equity rolls cleanly +11 = Q1 PAT".** Bear counter: that PAT
  is entirely non-cash Other Income/fair-value (328% of PBT). Already incorporated
  by A4's earnings-quality thesis → no separate graft needed.

**AUDIT 3 RESULT (round 2): both surviving counters now grafted (see RE-AUDIT). PASS.**

---

## RE-AUDIT (round 2) — verification of A4's four applied fixes

| # | Required fix | Corrected review reads | My independent derivation | Verdict |
|---|--------------|------------------------|---------------------------|---------|
| 1 | Step 5 gross debt = +41 vs Mar'26 (610→651); +5 only vs Mar'25 | L350: "**+41 QoQ vs Mar'26 (610→651)** … the +5 is only vs the older Mar'25 base of 646"; echoed L377 | 651 − 610 = +41; 651 − 646 = +5 (Mar'25) | **FIXED** |
| 2 | Table 1.3 FY26 Reported EBITDA = 174.29 (not 174.65) | L169: "…| 46.45 | 91.36 | 38.05 | **174.29** |" | 78.03 + 10.05 + 86.21 = 174.29 (cross-check 176.88 − 2.59 JV = 174.29) | **FIXED** |
| 3 | Finance-cost characterisation: fall is non-cash (royalty-unwind cessation) while cash interest rose 20.8→21.2 on gross debt 610→651 | L211: "**NON-CASH relief only:** fall is entirely the royalty-unwind line 1.5→0 (P-L320); CASH interest ROSE 20.8→21.2 (P-L319) on gross debt up 610→651. No deleveraging" | P-L319 20.8→21.2 (+0.4); P-L320 1.5→0; P-L420 610→651 | **GRAFTED** |
| 4 | Step 5 net-debt answer: flat net debt is debt-funded (cash build via ~Rs 106 Cr drawals; gross debt +41 QoQ) | L374-380: "**only optically flat QoQ (438→432)** … **debt-funded liquidity, not deleveraging.** Cash rose 172→219 (+47) funded by ~Rs 106 Cr of fresh loan drawals (P-L382), while **gross external debt rose +41 QoQ (610→651)**" | Cash 219−172 = +47; drawals P-L382 = 106; gross debt +41 | **GRAFTED** |

Both round-1 arithmetic mismatches are corrected to my recomputed values, and both
surviving bear counters are now written into the review body (not merely into the
question list). Coverage and the four-part brief remain present and unchanged. No
residual gap.

---

## VERDICT

**COMPLETE.** All four audits pass on the corrected review:
- Audit 0 (deliverable gate): PASS — four brief parts present and non-empty.
- Audit 1 (coverage): PASS — enumeration reconciles; no orphan rows, no ledger gap.
- Audit 2 (arithmetic): PASS — the two round-1 mismatches now read 174.29 and
  +41 vs Mar'26, matching my independent derivation; no mismatch above rounding remains.
- Audit 3 (adversarial): PASS — both surviving bear counters (finance-relief is
  non-cash / cash interest and gross debt rose; net-debt-flat is debt-funded) are
  grafted into the review body.

No loop-back required. The review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "SPROP"
quarter: "Q1 FY27"
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
