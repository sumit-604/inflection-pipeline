# A5 ADVERSARY / COMPLETENESS AUDIT — Digitide Solutions Limited (DSSL) — Q1 FY27 (concall, Role 5)

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-07-28
**Under audit:** `runs/dssl-q1fy27/work/review_concall_dssl_q1fy27.md` (A4 Role 5)
**Re-derived from:** `extract_concall_dssl_q1fy27.txt` (ASR, DECODE KEY L14-29) + `ledger_concall_dssl_q1fy27.md` (A2)
**Method:** fresh grep/sweep over the extract; independent recompute of every derived metric; bear counters built only from transcript text. I did not defer to A4's or A3's cites; every cite below was checked at its line/turn.

---

## AUDIT 1 — COVERAGE

### 1A. Fresh enumeration vs A2 ledger

| Category | A2 count | My fresh count | Basis of my count | Orphan rows | Status |
|---|---|---|---|---|---|
| Participants | 13 | 13 | 3 mgmt + 1 moderator (PROVENANCE L34) + 1 generic operator (L38) + 8 analyst-block openers (L44, L65, L75, L105, L127, L140, L162, L173) | none | MATCH |
| Turns | 94 | 94 | Ledger's speaker-split reconciliation re-derived: 38 mgmt + 41 analyst + 15 moderator/operator = 94; internally consistent | none | MATCH |
| Questions | 27 | 27 | Distinct asks per analyst block: Adita 7 (Q1-Q7), Sanjay 2, Manish 4, Nandra 2, Siman 2, Jagdesh 5, Anukul 2, Zohir 3 = 27 | none | MATCH |
| Mgmt numbers | 34 | 34 | N1-N30 mgmt-confirmed + N31-N34 analyst-sourced (5% standalone, 9000/1800cr, 15cr/2% AI, 150cr land) | none | MATCH |
| Forward-commitments | 18 | 18 | F1-F18 at cited lines; all located | see 1B (F18) | MATCH |
| Hedges | 13 | 13 | H1-H13 at cited lines; all located | none | MATCH |

No row my fresh pass found is missing from the ledger. No return-to-A2.

### 1B. Every ledger row cited in A4 or marked reviewed-no-finding

- **Participants P1-P13:** management in A4 Step 0B; the 8 questioner firms in Step 0C and the Step 4A inventory; operator implicit. COVERED.
- **Questions Q1-Q27:** all present in A4 Step 4A inventory (Q1-Q27) with response-quality grades. COVERED.
- **Numbers N1-N34:** N1-N30 reconciled in Step 7A / used across Steps 1-8; N31 (9000/1800cr) in Q4/Step 8F#5; N32 (5% standalone) in Q1; N33 (15cr/2% AI) in Q16/8A; N34 (150cr land) in A3-F05/Step 5A. COVERED.
- **Hedges H1-H13:** H1,H2,H4,H5,H6,H7,H9,H11,H12 cited by number in Step 6C/6D; H3 (book-and-bill deferral to Q2/Q3), H8 (look-at-group), H10 (AI BU "not there yet"), H13 (headcount directional) covered by content in Steps 2/4C/5A/8F. COVERED.
- **Forward-commitments F1-F17:** each cited by number in the Step 3A register, Step 2 guidance table, Step 6B specificity list, or Step 8F. COVERED.
- **F18 (closing "acceleration of profitability/execution/value creation," turn 93/L189):** NOT line-cited anywhere in the A4 body. It does NOT appear in the Step 3A 14-item register nor the Step 6B forward-statement list. **Ruling: reviewed-no-finding, NOT an orphan.** The A4 preamble (L14) explicitly enumerates "forward-commitments F1-F18 (L238-255) ... All reviewed," which is the "explicitly marked reviewed, no finding" bar the protocol allows; and F18 carries no independent testable content (it restates F7/F15 margin-expansion and F14 measurement). Logged as the single weakest coverage point, but not verdict-flipping. No loop-back required.

**Coverage verdict: COMPLETE.** No orphan rows; no missing-from-ledger rows.

---

## AUDIT 2 — ARITHMETIC (independent recompute)

| Metric (A4 assertion) | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Revenue tie | 775, +5.3% YoY, -3.1% QoQ = filing 775.07 | ties exactly | L42 (N1/N4) | PASS |
| Op EBITDA / margin | 76.9cr, 9.9% = 76.89/9.92% | 76.89 / 775.07 = 9.92% | L42 (N2/N7) | PASS |
| PAT | 2.9cr spoken = 2.93 consol total incl NCI | ties; owners -1.89 / standalone -10.58 flagged | L42 (N17) | PASS |
| T&D | +20.3% / ~237 / 31% (filing +20.5% / 237.36 / 30.6%) | 237.36/775.07 = 30.6%; 20.3 vs 20.5 = 0.2pp | L42 (N5) | PASS (rounding; filing governs) |
| International | +10.2% / ~296 / 38% | 296/775.07 = 38.2% | L42 (N6) | PASS |
| D&A split | 55 = ~36 lease RoU + ~19 owned (filing 55.18) | 36 + 19 = 55 | L42 (N12) | PASS |
| Finance / lease interest | 15 incl ~11 lease; non-lease ~4/qtr | 15 - 11 = 4 | L42 (N15) | PASS |
| EBIT QoQ | 22 "up ~1cr" from 21 (filing 21.71 vs 21.48) | rounds 22/21 OK; **true delta +0.23cr** | L42 (N14) | PASS-with-note (see 2A) |
| DSO | 82, +7 QoQ (vs 75), -9 YoY (vs 91) | 82-75=+7; 91-82=9 | L42 (N21) | PASS |
| Sequential EBITDA bridge | -11 = Q4 87.89 - Q1 76.89 | 87.89 - 76.89 = 11.00 | L42 (N8) | PASS |
| Bridge decomposition | -9.9 one-off + -1 operational; +~10 wage inside operational | -9.9 + -1 ≈ -11; wage +10 nets to -1 → ~+9 hidden offset | L42 (N9/N10/N11) | PASS |
| A3-F09 un-itemized offset | ~9cr | Q1 ex-wage 76.89+10 = 86.9; norm Q4 87.89-9.9 = 78.0; 86.9-78.0 = **8.9 ≈ +9** | Step 7B | PASS |
| 200bps FY27 exit | 9.9% + 2.0 = ~11.9% | 9.9 + 2.0 = 11.9 | Step 7B (A3-F02) | PASS |
| Lease outflow vs annualised EBITDA | 175-180 vs 307.6 (76.89x4) = ~57-59% | 175/307.56 = 56.9%; 180/307.56 = **58.5%** | Step 7C | PASS (upper 59 vs 58.5, rounding) |
| Lease outflow vs FY26 EBITDA | vs 343.17 = ~51-52% | 175/343.17 = 51.0%; 180/343.17 = 52.5% | Step 7C | PASS |
| Non-lease interest / residual | +~16/yr; ~191-196 committed; ~115-150 left | 4x4=16; 175+16=191 / 180+16=196; 307.56-196=111.6 / 343.17-191=152 | Step 7C | PASS (lower 111.6 vs stated 115, rounding) |
| Wage annualised | ~40cr/yr drag | 10 x 4 = 40 | Step 7B | PASS |

**No mismatch above rounding. Zero arithmetic FAILs.**

### 2A. Two rounding notes (not FAILs; A4 already labels both "(rounding)")
1. **EBIT "up 1cr" is a rounding-inflated framing.** Filing EBIT 21.71 (Q1) vs 21.48 (Q4) → **true QoQ delta +0.23cr, i.e. essentially flat.** The spoken "+1cr" is the artifact of rounding each figure to a whole crore (22 vs 21). Each spoken figure still ties to filing within rounding, and A4 flags "(rounding)," so it is not a FAIL — but the honest read is "EBIT flat QoQ," not "+1cr." Already implied by A4's parenthetical; no graft required.
2. **T&D +20.3% (spoken) vs +20.5% (filing)** and 31% vs 30.6% mix — 0.2pp / 0.4pp, immaterial; filing governs per protocol. Not a FAIL.

All spoken figures on the task's checklist (775, 76.9/9.9%, 2.93, T&D +20.3%/237, Intl +10.2%/296, D&A 55=36+19, finance 15/11, EBIT 22 vs 21, DSO 82/+7/-9, lease 175-180 as % of EBITDA, the ~11cr bridge = 9.9 one-off + 1 operational + 10 wage, and the A3-F09 ~9cr offset) reconcile. No garbled figure required DECODE-KEY rescue to a different value; all spoken numbers match the filing baseline directly.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear per positive claim, from the transcript)

**Claim A — "Candid quality-over-volume reset is credible" (Step 6D/6E candour markers).**
Bear counter (from transcript): The reset reframes the scorecard to the one metric not yet printed (future margin) at the exact moment the company misses on every hard metric — revenue -3.1% QoQ, "continuously deteriorating quarter on quarter... 5th quarter" (Manish, L80), TCV "crashed" (Sanjay, L67), margin 9.9%. Owning the miss is costless when management simultaneously withholds the Q2 margin (H12/L179), defers the replacement revenue % (Q26/L179), and refuses to quantify the parent cost-housing (L97) — every number that would let the market hold the new frame to account. "Actions have already started" (F1/L42) is unquantified. On a first CEO call there is zero delivery track record behind the credibility claim.
**Survives?** NO — already incorporated. A4 Step 6E gives the symmetric EVASIVE-vs-CREDIBLE verdict citing "withdrawn guide, unfunded ambition, walked-back land, silence"; Step 3B and A3-F04 flag the withdrawal; Step 4A grades the guidance cluster C. No new graft.

**Claim B — "200bps FY27 margin expansion, reaffirmed / credible-conditional."**
Bear counter: The 200bps rides on (i) a ~9cr/qtr offset management asserted but did not itemize (A3-F09), against (ii) a wage step-up that is a PERMANENT, regulated ~40cr/yr cost — minimum-wage revisions "from at least 1st of April" (L101), structural not one-off — where the offsetting repricing is only in "active discussions" (F5/F11, L42/L101), i.e. not signed. If the offset was a one-off true-up and repricing is not agreed, FY27 margin can fall, not rise 200bps. Management gave no Q2 checkpoint.
**Survives?** NO — already incorporated. A4 Step 7B states it verbatim: "200bps guide is credible-conditional-on-an-unproven-offset ... over-committed if the offset is one-off," and Step 8F#1/#2 raise the itemization and Q2-checkpoint questions. No new graft.

**Claim C — "All numbers reconcile / no concall-vs-filing contradiction."**
Bear counter: Arithmetically true, but the headline profitability claim is materially misleading as spoken. "Returned to profit... 2.9cr" is 100% NCI — owners of the parent LOST 1.89cr and standalone parent LOST 10.58cr; and management's own AI narrative ("improving productivity, expanding margins," L42) directly contradicts the printed 9.9% margin contraction + 10cr employee-cost rise this quarter.
**Survives?** NO — already incorporated. A4 Step 7A logs PAT as "CONFIRMED but incomplete" (owners loss named); the flag block states "framing technically true, materially incomplete"; Step 1 diagnostic 4 and Exchange 3 flag the AI-productivity-vs-margin contradiction. No new graft.

**Adversarial result: three counters constructed, zero survive as new material — each is already present in A4's review. No loop-back to A4 for an unincorporated counter.**

---

## VERDICT

**COMPLETE.**

- Coverage: all 13/94/27/34/18/13 ledger rows re-enumerated independently and matched; every row cited in A4 or (F18 alone) covered by the explicit preamble reviewed-no-finding blanket. No orphan, no missing-from-ledger.
- Arithmetic: every derived metric recomputed from raw numbers; all tie within rounding. Two rounding notes surfaced (EBIT "+1cr" is truly +0.23cr/flat; T&D 20.3 vs 20.5) — both already labelled "(rounding)" by A4; neither a FAIL.
- Adversarial: the three most management-favourable claims each have a real bear counter, but all three are already grafted into A4. Nothing survives requiring incorporation.

Only COMPLETE proceeds to Notion save. This review may proceed.

```yaml
stage: A5-adversary
company: "DSSL"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
