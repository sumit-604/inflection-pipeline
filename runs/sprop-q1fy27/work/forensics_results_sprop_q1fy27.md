# A3 FORENSIC NOTES — Shriram Properties Limited (SPROP), Q1 FY27 — doctype: results

Source document: `extract_results_sprop_q1fy27.txt` (526 lines, 10 pages).
Reconciliation contract: `ledger_results_sprop_q1fy27.md` (A2).
Prior-quarter extract: NONE in repo — all QoQ diffs flagged UNVERIFIED-NO-PRIOR.
Unit convention: Rs lakhs (x0.01 = Rs Cr). Doctype = results: F1-F15 apply; F16/F17 N.A.

Ledger reconciliation: 7 tables / 7 read at cited lines = 100%. Every ZERO_STANDING,
ENTITY_CHANGE, SIGNATURE_TIMING and OCR_UNCERTAIN flag from A2 read verbatim before judging.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-F2 | F2 | T2 r17 (L205) / T3 r19 (L438); T3 r14 (L431); T2 r2 (L184) | 205, 438, 431, 184 | SA "Profit/ (loss) for the period/ year ... 1,282" vs Cons "Profit for the period / year ... 1,104" | FORWARD-SIGNAL | Consolidated PAT (Rs 11.04 Cr) fell BELOW standalone (Rs 12.82 Cr) for the first time across the four periods shown — a reversal from FY26 (Cons +Rs 93.25 Cr over SA). Subsidiaries + JVs are now a net drag; standalone profit is carried by other income (Rs 48.11 Cr) exceeding operating revenue (Rs 41.50 Cr), i.e. intra-group dividends/interest. Earnings quality question for A4. |
| A3-F3 | F3 | T2 r7 (L191) / T3 r7 (L423); T2 r4 (L188) / T3 r4 (L420) | 191, 423, 188, 420 | Employee benefits SA "2,373" vs Cons "2,687"; Land cost SA "7,305" vs Cons "7,377" | NEUTRAL-FACT | Near-identical employee cost (+13%) and near-identical land cost (delta 72 lakhs) despite 5.4x consolidated revenue => the 26 SPVs are operationally hollow (staffed and land-funded via the parent), consistent with the asset-light JDA/JV model. Not shells (they carry the Rs 224 Cr consolidated revenue and inventory swings), but centralised — a structural cost-attribution fact. |
| A3-F4 | F4 | T5 para 6 (L333-341) | 333-341 | "We did not review the interim financial results of 18 subsidiaries ... total net loss after tax of = 274 lakhs ... share of net profit after tax of = 771 lakhs ... in respect of 4 joint ventures, whose interim financial results have not been reviewed by us" | AMBIGUOUS | Unreviewed 4 JVs contribute +Rs 7.71 Cr = 70% of consolidated PAT (Rs 11.04 Cr); 18 unreviewed subsidiaries carry Rs 72.66 Cr revenue and Rs 2.74 Cr net loss. The entire consolidated profit essentially rests on component-auditor numbers. Well above the 10% threshold. YoY trend UNVERIFIED-NO-PRIOR. A4 question: which entities, and why the concentration. |
| A3-F5 | F5 | T5 para 5 std (L147-152) / para 5 cons (L325-330); notes S-N5/C-N5 (L246, L495) | 147-152, 325-330, 495-500 | "we draw attention to note 5 ... a search operation carried out by the Enforcement Directorate ... There is no communication received by the Company as on date regarding any findings" | AMBIGUOUS | Emphasis-of-Matter re the Oct 2024 ED search persists ~21 months on, still "no communication ... regarding any findings." No Going Concern paragraph in either report (absence, not assumption). QoQ scope-diff impossible (UNVERIFIED-NO-PRIOR). Unresolved regulatory overhang; A4 question on ED status and any contingent exposure. |
| A3-F6 | F6 | T4 item 2 (L57-66) | 59, 64-66 | "The 5th Annual General Meeting ... will be held through video conferencing"; "The Annual Report along with the Notice of the AGM ... shall be shared with the Stock Exchanges and the Members ... within the prescribed timeline" | FORWARD-SIGNAL | Two dateable commitments: AGM convening and Annual Report + AGM Notice imminent. Full FY26 Annual Report drops within weeks — schedule Role 6 AR Deep Dive (ROCE, DTA composition, Kolkata/Uttarpara land detail). See Commitment Register. |
| A3-F8 | F8 | T2 r14/15/16 (L201-203); T3 r16/17/18 (L435-437) | 201-203, 435-437 | SA "Current tax (including taxes for earlier years) - ... Deferred tax 173"; Cons FY26 "Total tax expense/ (credit) ... (2,278)" | FORWARD-SIGNAL | (a) Standalone Q1 FY27: positive PBT Rs 14.55 Cr but NIL current tax, ETR 11.9% (all deferred) — ~1,327 bps below the 25.17% statutory rate; future ETR step-up risk as the deferred shield normalises. (b) FY26 consolidated total tax = CREDIT Rs 22.78 Cr on positive PBT Rs 78.03 Cr (ETR -29.2%), lifting PAT (Rs 100.81 Cr) above PBT — confirms the tax-flattered-PAT deal-breaker (Notion (b), ~Rs 22.9 Cr). (c) "including taxes for earlier years" line non-zero across periods; earlier-years component NOT broken out (NOT FOUND) = FINDING per F8. |
| A3-F11 | F11 | T2 r22 (L215) vs T3 r33 (L463); ledger note L154-157 | 215, 463 | SA "Other equity ... 1,42,767" vs Cons "Other equity ... 1,28,927" | AMBIGUOUS | Consolidated other equity is Rs 138.4 Cr BELOW standalone (9.7% lower) — the reverse of the usual sub-profit accretion. Candidate reconciling items: accumulated subsidiary/JV losses, negative JV net worth, and elimination of intra-group dividends that inflate standalone reserves (see F2 other-income point). No external number (rating/slide) in this filing to run the 5% third-party test. A4 question: bridge standalone-to-consolidated reserves. Supports negative-JV-income deal-breaker (c). |
| A3-F13 | F13 | T4 item 2 (L57-66) | 57-66 | "Convening of the Annual General Meeting ... The Annual Report along with the Notice of the AGM ... shall be shared ... within the prescribed timeline" | FORWARD-SIGNAL | AR/AGM approval => full Annual Report within weeks: schedule Role 6 AR Deep Dive event. NEUTRAL sub-fact: no record date, dividend, director appointment/resignation, auditor change, ESOP grant, or capital-raising enabling resolution appears anywhere in the letter (checked, confirmed absent) — no funding round or board-composition signal foreshadowed. |
| A3-F14 | F14 | T7 blocks 2-5 (L153-163, 260-269, 344-355, 511-524); T4 (L48); ledger T6 note L284-287 | 48, 158-159, 264, 349-351, 520 | Board "commenced at 06:30 P.M. and concluded at 07:20 P.M." (L48); auditor standalone report "Date: 2026.08.12 19:14:02" (L158-159); CMD "19:02:02" (L264) | AMBIGUOUS | Four of five signature timestamps predate the board's own stated conclusion time (19:20): CMD 19:02:02/19:02:24, auditor standalone 19:14:02, auditor consolidated OCR-garbled "6:1425" (plausibly 19:14:25, OCR_UNCERTAIN). Individually immaterial (clock/OCR artifacts possible), cumulatively a governance data point. Also: Annexure 1 header "List of entities included in the Statement" duplicated (L362-363, OCR). A4 question: reconcile approval-vs-signing sequence. |
| A3-F15 | F15 | T6 sub #26 + A1-FN1 (L390-391); note C-N6 (L506) | 390-391 | "26. Shrivision Upscale Spaces Private Limited (*)" / "(*) subsidiary with effect from 09 February 2026" | AMBIGUOUS | New subsidiary added w.e.f. 09 Feb 2026, now in the Q1 FY27 consolidation (26 subs total, reconciles to note C-N6). Prior-list diff UNVERIFIED-NO-PRIOR; document-internal footnote evidences the addition. Name echoes existing #13 "Shriram Upscale Spaces" — possible premium/commercial vehicle. A4 question: what project/asset does it hold and why incorporated/acquired now. |

---

## CHECKLIST SCORECARD (all 17; exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 | PASS | All 7 ZERO_STANDING rows explained: current-tax dash (L201, routed to F8), paid-up/other-equity interim blanks (L214-215, L462-463 = SEBI annual-only format), NCI dashes/"(0)" (L449/454/459 = negligible or rounding minority per C-FN2). No "exceptional items", "profit on sale of subsidiary/investments", or "discontinued operations" line exists in the template — no hidden transaction class anticipated. |
| F2 | FINDING | Consolidated PAT (1,104) fell below standalone (1,282) in Q1 FY27, reversing FY26's +9,325-lakh gap; standalone carried by other income > operating revenue (A3-F2). |
| F3 | FINDING | Near-identical employee benefits (2,373 vs 2,687) and land cost (7,305 vs 7,377) against 5.4x consolidated revenue = operationally hollow SPVs, parent-centralised (A3-F3). |
| F4 | FINDING | 70% of consolidated PAT (771 of 1,104 lakhs) rests on 4 unreviewed JVs; 18 unreviewed subsidiaries; >10% threshold breached (A3-F4). |
| F5 | FINDING | ED-search Emphasis-of-Matter persists (note 5, both reports), no findings communicated ~21 months on; no Going Concern para; QoQ diff UNVERIFIED-NO-PRIOR (A3-F5). |
| F6 | FINDING | Two dateable commitments mined — AGM "will be held", AR/Notice "shall be shared ... within the prescribed timeline" (A3-F6, Commitment Register). |
| F7 | PASS | No note newly adds a hedge about revenue lumpiness or customer concentration. The only forward-looking cover is the note-5 "as on date ... no ... communication regarding the findings" ED carve-out, tracked under F5 to avoid double-count. |
| F8 | FINDING | Standalone Q1 nil current tax on positive PBT (ETR 11.9%, ~1,327 bps shield); FY26 consolidated tax CREDIT Rs 22.78 Cr flatters PAT above PBT; "taxes for earlier years" line non-zero (A3-F8). |
| F9 | PASS | OCI is defined-benefit remeasurement only; Q1 FY27 swing (SA -11 / Cons -16) does not exceed the full prior-year figure (SA -43 / Cons -69). No assumption-change signal. |
| F10 | PASS | Paid-up capital 17,065 lakhs unchanged (annual column only; interim blank per format); Basic = Diluted EPS (SA 0.75/0.75, Cons 0.65/0.65), zero spread; no dilutive instrument or capital action on the board agenda. |
| F11 | FINDING | Consolidated other equity (1,28,927) is Rs 138.4 Cr below standalone (1,42,767) — reverse of normal sub-profit accretion; reconciling bridge sought (A3-F11). |
| F12 | PASS | Single reportable segment (note 4, L243/L492), single geography; no segmental asset/liability table disclosed to trend. Transparency limitation noted (no residential/commercial/Uttarpara-land split) but disclosure is Ind AS 108-standard; nothing flagged. |
| F13 | FINDING | AGM convening + AR forthcoming => Role 6 AR Deep Dive to be scheduled; no dividend/director/capital-raise resolution present (A3-F13). |
| F14 | FINDING | Four of five signatures timestamp before the board's stated 19:20 conclusion; Annexure header duplicated — cumulative governance data point (A3-F14). |
| F15 | FINDING | Shrivision Upscale Spaces added as subsidiary w.e.f. 09 Feb 2026 (A3-F15); prior-list diff UNVERIFIED-NO-PRIOR. |
| F16 | N.A. | Presentation-specific (dropped/reframed disclosures) — document is a results filing, no deck. |
| F17 | N.A. | Concall-specific silence audit — no transcript in this document. Notion checklist items (Kolkata land plan, FY27 sales/margin conditions, ROCE) carried forward to the concall/results-Q&A silence audit when a transcript is filed. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| 5th AGM (post-IPO) to be held via VC/OAVM per MCA/SEBI circulars | FY27, date TBD | L59 (agenda item 2) | intends / announced |
| Annual Report + AGM Notice to be shared with exchanges and members | "within the prescribed timeline" (weeks) | L64-66 (agenda item 2) | underway / forthcoming |

Note: both are freshly announced (not carried from a prior status word; no prior extract to confirm a status transition — UNVERIFIED-NO-PRIOR). The AR forthcoming is the actionable catalyst — feeds F13 (Role 6 AR Deep Dive) and the FTTCP catalyst timeline.

---

## CROSS-CHECK NOTES (for A4)
- The reviewed vs unreviewed JV split implies the single directly-reviewed JV is the large loss-maker: consolidated JV share (net) = (385) lakhs (L431) while the 4 unreviewed JVs contributed +771 lakhs (L336-337), i.e. the reviewed JV(s) ~ (1,156) lakhs loss. Inference, flagged for A4 confirmation, not asserted.
- Standalone other income (4,811 lakhs, L184) exceeding standalone operating revenue (4,150 lakhs, L183) is the mechanical driver behind both F2 (PAT reversal) and F11 (standalone reserves above consolidated): intra-group dividends/interest inflate the parent, wash out on consolidation.
- FY26 consolidated deferred tax credit (1,687 lakhs, L436) + current tax credit (591 lakhs, L435) = (2,278) lakhs total credit reconciles to the Notion deal-breaker (b) "~Rs 22.9 Cr deferred-tax-asset credit."

```yaml
stage: A3-forensics
company: "SPROP"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sprop-q1fy27/work/forensics_results_sprop_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F2", check: "F2", line: "205/438/431/184", classification: "FORWARD-SIGNAL", implication: "Consolidated PAT fell below standalone for first time; subs+JVs a net drag, standalone carried by intra-group other income"}
  - {id: "A3-F3", check: "F3", line: "191/423/188/420", classification: "NEUTRAL-FACT", implication: "Near-identical employee and land cost vs 5.4x consolidated revenue = operationally hollow parent-centralised SPVs (asset-light model)"}
  - {id: "A3-F4", check: "F4", line: "333-341", classification: "AMBIGUOUS", implication: "70% of consolidated PAT rests on 4 unreviewed JVs; 18 unreviewed subsidiaries; above 10% threshold"}
  - {id: "A3-F5", check: "F5", line: "147-152/325-330", classification: "AMBIGUOUS", implication: "ED-search Emphasis-of-Matter persists ~21 months, no findings communicated; unresolved regulatory overhang; QoQ diff UNVERIFIED-NO-PRIOR"}
  - {id: "A3-F6", check: "F6", line: "59/64-66", classification: "FORWARD-SIGNAL", implication: "AGM and Annual Report imminent within prescribed timeline; schedule Role 6 AR Deep Dive"}
  - {id: "A3-F8", check: "F8", line: "201-203/435-437", classification: "FORWARD-SIGNAL", implication: "Standalone nil current tax (ETR 11.9%, ~1327bps shield); FY26 consolidated Rs 22.78 Cr tax credit flatters PAT above PBT; earlier-years tax not broken out"}
  - {id: "A3-F11", check: "F11", line: "215/463", classification: "AMBIGUOUS", implication: "Consolidated other equity Rs 138.4 Cr below standalone; reverse of sub-profit accretion; bridge sought; supports negative-JV-income deal-breaker"}
  - {id: "A3-F13", check: "F13", line: "57-66", classification: "FORWARD-SIGNAL", implication: "AR/AGM approval => full Annual Report within weeks (Role 6 event); no dividend/director/capital-raise resolution present"}
  - {id: "A3-F14", check: "F14", line: "48/158-159/264/349-351/520", classification: "AMBIGUOUS", implication: "Four of five signatures timestamp before board's stated 19:20 conclusion; header duplication; cumulative governance data point"}
  - {id: "A3-F15", check: "F15", line: "390-391", classification: "AMBIGUOUS", implication: "New subsidiary Shrivision Upscale Spaces added w.e.f. 09 Feb 2026; purpose/asset to identify; prior-list diff UNVERIFIED-NO-PRIOR"}
forward_signals: ["A3-F2", "A3-F6", "A3-F8", "A3-F13"]
ambiguous: ["A3-F4", "A3-F5", "A3-F11", "A3-F14", "A3-F15"]
commitments:
  - {commitment: "5th AGM (post-IPO) to be held via VC/OAVM", implied_date: "FY27 TBD", ref: "L59 agenda item 2", status_word: "announced"}
  - {commitment: "Annual Report + AGM Notice to be shared with exchanges and members", implied_date: "within prescribed timeline (weeks)", ref: "L64-66 agenda item 2", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
