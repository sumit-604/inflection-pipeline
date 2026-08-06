# A3 FORENSIC NOTES — RPTECH (Rashi Peripherals Ltd) — Q1 FY27

Doctype (as filed): results. Actual content: proposed Joint Venture press release
+ BSE/NSE cover letter (Reg 30 strategic disclosure), filed alongside Q1 FY27
results, dated 4 Aug 2026. Source extract: `extract_pressrelease_jv_rptech_q1fy27.txt`
(5 pages, 212 body lines). Ledger: `ledger_pressrelease_jv_rptech_q1fy27.md`.

Reconciliation: every A2 ledger section was read at its cited line in the A1
extract before judging (entities 13; governance 6; capital-commitment 0/NOT FOUND;
scope 1 + segments 8; key-highlights 4; conditions-precedent 0/NOT FOUND; timeline
10; forward-commitment phrases 12; quotes 3; monetary 3; identifiers 3; signature 1;
boilerplate 4; background facts 6). ledger_reconciled_pct = 100.

Doctype note on applicability: although the cover header labels this "results", the
document carries NO financial statements, NO auditor's report, NO balance sheet, P&L,
segment, tax, OCI, share-count or reserves data. The balance-sheet / audit family of
checks (F2, F3, F4, F5, F8, F9, F10, F11, F12) is therefore N.A. by absence of the
underlying content, not by doctype rule. The applicable forensic surface is the
disclosure/entity/forward-commitment family (F1, F6, F7, F13, F14, F15). F16
(presentation) and F17 (concall) are N.A. per doctype.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1-1 | F1 | §3 (capital commitment, ZERO_STANDING) + §6 (conditions precedent, ZERO_STANDING) | 94 (anchor); absence spans doc | "will subsequently acquire a 26% equity stake in the subsidiary" — with NO consideration, valuation or condition precedent stated anywhere | AMBIGUOUS | A cross-border 26% equity sale disclosed with zero price, zero valuation basis and zero conditions precedent (CCI / definitive agreement / shareholder or board approval). Either the deal is small enough to be immaterial, or material terms are withheld from a Reg 30 release. Cash consideration (if any) is the direct read on whether the carve-out RELIEVES the live working-capital concern or is a nominal internal transfer. Lean bear; convert to management question. |
| F6-1 | F6 | §7 (timeline 10) + §8 (forward-commitment phrases 12) + §5 bullet 3 | 91, 94, 95, 97, 107, 112 | "the JV scheduled to officially commence operations in October 2026"; "50+ new local engineering hires over 2 years" | FORWARD-SIGNAL | Six dated/dateable management commitments with a hard first milestone: JV live Oct 2026 (~2 months out). This becomes the Role 5 promise-vs-delivery baseline — confirm at Q2/Q3 FY27 that the WOS transfer completed, Restar's 26% closed, and the hiring ramp began. Feeds the FTTCP catalyst timeline against the Notion "semiconductor/strategic-JV scaling" Medium catalyst. |
| F7-1 | F7 | §8 (phrase mining) + §13 boilerplate row 1 (Safe Harbor) | 27, 31, 88 | "Press Release on proposed Joint Venture" (cover) vs "has entered into a joint venture ('JV') with Restar Corporation" (body) | AMBIGUOUS | Status contradiction: cover letter and title say "proposed"; body asserts a completed "has entered into". With zero conditions precedent (§6) the reader cannot tell whether a binding definitive agreement exists or this is an in-principle / MoU stage. Hedge-by-omission. The standard Safe Harbor (L174-184) is boilerplate NEUTRAL-FACT; the material hedge is this proposed-vs-executed ambiguity. Convert to management question. |
| F14-1 | F14 | §1 rows 1.3–1.5 (ENTITY_CHANGE) + §2 rows 1–3 | 27/88, 94, 103, 161 | "acquire a 26% equity stake in the subsidiary" (L94) vs "26% with Restar Corporation" of "74% shareholding with RP tech" (L103); only naming instance "Rashi Restar Semiconductor Solutions" (L161) | AMBIGUOUS | Cumulative drafting/naming inconsistency: (a) "subsidiary" (L94) vs "the JV" (L103) — is Restar buying 26% of the Bengaluru WOS or of a distinct JV vehicle?; (b) JV entity named only once ("Rashi Restar Semiconductor Solutions", L161), relationship to the unnamed Bengaluru WOS unstated; (c) against the Notion filing batch the same reorg is described as a slump sale of the "Embedded Business" to "Rashi Semiconductor Solutions Pvt Ltd / Pte" — a different entity name than the press release's "Rashi Restar Semiconductor Solutions". Individually immaterial, cumulatively a governance/drafting data point. Convert to a structure-clarification question. |
| F15-1 | F15 | FLAGS SUMMARY — 4× ENTITY_CHANGE (§1 rows 1.2, 1.3, 1.4, 1.5) | 88, 91-93, 161 | "transfer its semiconductor business division into a wholly owned subsidiary headquartered in Bengaluru and step-down subsidiary headquartered in Singapore" | FORWARD-SIGNAL | Consolidation-list change incoming: two new entities created (Bengaluru WOS, Singapore step-down) and a relationship change — the semiconductor division moves from 100% owned to a 74%-owned JV, introducing a 26% minority interest at Oct 2026. Consolidated financials from Q3 FY27 will carry new MI lines and a de-consolidation adjustment on the transferred division. Track the new entities and MI in future S-vs-C decomposition (F2/F15 next quarter). |

No findings on F2, F3, F4, F5, F8, F9, F10, F11, F12, F13, F16, F17 (see scorecard).

---

## CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING ITEMS | FINDING | Two ZERO_STANDING ledger rows — consideration (§3) and conditions precedent (§6) — both absent for a cross-border 26% stake sale; template items conspicuously missing (F1-1). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Press release carries no standalone/consolidated financial statements; no Revenue/EBITDA/PAT to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines (materials/employee/depreciation) disclosed; the two new subsidiaries are pre-operational vehicles with no financials to test. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor report / Other Matters paragraph in this document. |
| F5 GOING CONCERN / EoM | N.A. | No auditor Emphasis-of-Matter or going-concern language present; no prior-quarter EoM to verbatim-diff for this doctype. |
| F6 FORWARD-COMMITMENT MINING | FINDING | 12 forward-commitment phrases enumerated; six dated/dateable commitments incl. Oct 2026 JV commencement and 50+ hires over 2 years (F6-1). |
| F7 HEDGE PHRASE MINING | FINDING | "proposed" (L27/31) vs "has entered into" (L88) status contradiction plus zero conditions precedent = hedge-by-omission; Safe Harbor itself boilerplate (F7-1). |
| F8 TAX FORENSICS | N.A. | No ETR, deferred-tax or earlier-year tax adjustment figures in the document. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial data disclosed. |
| F10 SHARE COUNT & DILUTION | N.A. | No paid-up capital or basic/diluted EPS; the 26% is a subsidiary-level MI, not parent-share dilution, and no numbers are given. |
| F11 RESERVES & NET WORTH | N.A. | No balance sheet / Other Equity / net-worth figures to tie out. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities/revenue tables; the semiconductor carve-out is captured qualitatively under F15. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | No AR/Board's-Report/MD&A approval, AGM notice, record date or director-appointment term dates in this standalone press release; the separate slump-sale board approval (Notion batch) is out of scope for this document. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | "subsidiary" vs "the JV" (L94/L103); single unlinked entity name (L161); "Rashi Restar Semiconductor Solutions" vs Notion-batch "Rashi Semiconductor Solutions Pvt Ltd/Pte" and "semiconductor business division" vs "Embedded Business" (F14-1). |
| F15 ENTITY LIST DIFFS | FINDING | 4× ENTITY_CHANGE: two new subsidiaries (Bengaluru WOS, Singapore step-down), new counterparty Restar, JV brand name; relationship change 100%→74% with new 26% MI (F15-1). |
| F16 PRESENTATION-SPECIFIC | N.A. | Not an investor presentation; no charts/baselines/order-book definitions. |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a transcript; no concall to cross-reference F6 commitments/Notion checklist against. |

Blank checks: none. GATE A3: PASS (all 17 marked exactly one status).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/line ref | status word |
|------------|--------------|---------------|-------------|
| Transfer semiconductor business division into Bengaluru WOS + Singapore step-down subsidiary | before Oct 2026 commencement | L91-93 | proposed ("will transfer") |
| Restar acquires 26% equity stake in the subsidiary | "subsequently" / by Oct 2026 | L94 | proposed ("will…acquire") |
| JV officially commences operations | October 2026 | L95 | scheduled |
| 50+ new local engineering hires | over 2 years (no start anchor — NOT FOUND) | L112 | committed (headcount + horizon) |
| JV to focus on advanced Image Sensing Solutions (Industrial + Automotive) | no date | L97 | proposed ("will focus") |
| JV to leverage network across 5 major-city locations | no date | L107 | proposed ("will leverage") |

---

## A4 HANDOFF — findings flagged for conversion into management questions

FORWARD-SIGNAL: F6-1, F15-1
AMBIGUOUS: F1-1, F7-1, F14-1

Suggested question seeds (A4 to finalise):
1. (F1-1) What consideration does Restar pay for the 26% stake, on what valuation, and
   does that cash enter the semiconductor entity — i.e. does it relieve the live
   working-capital concern (Notion Pillar 2 / VDA WC flag) or is it a nominal transfer?
2. (F1-1/F7-1) Is a binding definitive agreement executed, or is this an in-principle /
   MoU stage? What conditions precedent (CCI, definitive agreement, board/shareholder
   approvals) gate the October 2026 commencement, given none are disclosed?
3. (F14-1/F15-1) Confirm the entity map: is "Rashi Restar Semiconductor Solutions" the
   Bengaluru WOS, and how does it reconcile with the slump-sale entity "Rashi
   Semiconductor Solutions Pvt Ltd/Pte" named in the same filing batch? Is Restar's 26%
   at the Bengaluru WOS or a separate JV vehicle?
4. (F15-1) From which quarter will consolidated financials carry the 26% minority interest
   and the de-consolidation of the transferred semiconductor division?
5. (F6-1) Post-commencement, on what run-rate does the JV reach the Notion ₹100 Cr+
   semiconductor revenue threshold (Medium catalyst), and is the 50+ hire ramp on plan?

---

```yaml
stage: A3-forensics
company: "rptech"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rptech-q1fy27/work/forensics_jv_rptech_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-1", check: "F1", line: "94", classification: "AMBIGUOUS", implication: "26% stake disclosed with zero consideration/valuation and zero conditions precedent; cash terms are the read on whether the carve-out relieves the working-capital concern"}
  - {id: "F6-1", check: "F6", line: "95", classification: "FORWARD-SIGNAL", implication: "Six dated commitments; hard first milestone JV live Oct 2026 plus 50+ hires over 2 yrs; Role 5 promise-vs-delivery baseline"}
  - {id: "F7-1", check: "F7", line: "88", classification: "AMBIGUOUS", implication: "'proposed' (L27/31) vs 'has entered into' (L88) with no conditions precedent = binding-vs-MoU status unclear"}
  - {id: "F14-1", check: "F14", line: "103", classification: "AMBIGUOUS", implication: "'subsidiary' vs 'JV', single unlinked entity name L161, and name mismatch vs filing-batch 'Rashi Semiconductor Solutions Pvt Ltd/Pte'"}
  - {id: "F15-1", check: "F15", line: "91", classification: "FORWARD-SIGNAL", implication: "Two new entities + relationship change 100%->74%; new 26% minority interest and de-consolidation land in future consolidated financials"}
forward_signals: ["F6-1", "F15-1"]
ambiguous: ["F1-1", "F7-1", "F14-1"]
commitments:
  - {commitment: "Transfer semiconductor business division into Bengaluru WOS + Singapore step-down subsidiary", implied_date: "before Oct 2026", ref: "L91-93", status_word: "proposed"}
  - {commitment: "Restar acquires 26% equity stake in the subsidiary", implied_date: "by Oct 2026", ref: "L94", status_word: "proposed"}
  - {commitment: "JV officially commences operations", implied_date: "October 2026", ref: "L95", status_word: "scheduled"}
  - {commitment: "50+ new local engineering hires", implied_date: "over 2 years (no start anchor)", ref: "L112", status_word: "committed"}
  - {commitment: "JV to focus on advanced Image Sensing Solutions", implied_date: "NOT FOUND", ref: "L97", status_word: "proposed"}
  - {commitment: "JV to leverage network across 5 major-city locations", implied_date: "NOT FOUND", ref: "L107", status_word: "proposed"}
gate_a3: pass
blank_checks: []
```
