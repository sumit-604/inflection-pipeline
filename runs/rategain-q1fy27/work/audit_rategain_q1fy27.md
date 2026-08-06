# A5 ADVERSARY / COMPLETENESS AUDIT — RATEGAIN Q1 FY27 (CONCALL-MERGE RE-AUDIT)

Re-audit triggered by prior INCOMPLETE verdict on the Role 5 concall merge. Prior gap:
Section I.3 (guidance diagnostic) did not surface the margin-guide-below-Q1-print bear
counter. Fresh context: audited only against the A4 review, the A1 extracts, and the A2
ledgers. All numbers re-derived independently; A4/A3 cites checked, not trusted.

Scope this pass: (i) re-verify the corrected I.3 items specifically; (ii) re-confirm the
rest of Section I from scratch; (iii) re-run the four standing audits over the merged
document with emphasis on the concall (the newly merged doctype).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS GATE (hard gate, run first)

Plain-Language Brief (Section F) — all four labelled parts present and non-empty:

| Part | Location | Present? | Content real (not placeholder)? |
|---|---|---|---|
| (1) Summary narrative | F1, review L383-384 | PRESENT | Yes — 1 full narrative para, ~18 lines, numbers-anchored |
| (2) SECTOR intelligence | F2, review L386-387 | PRESENT | Yes — TAM, demand read, FIFA/ME, structural tail/headwinds |
| (3) BUSINESS-MODEL intelligence | F3, review L389-390 | PRESENT | Yes — subscription mix, NRR/LTV:CAC, adjusted-vs-reported |
| (4) COMPETITION intelligence | F4, review L392-393 | PRESENT | Yes — moat/breadth, Distribution +3.1%, concentration |

Concall addendum (I.8, review L602-610) is additionally present. **GATE = PASS.**

---

## RE-VERIFICATION OF THE FLAGGED SECTION I.3 CORRECTION (the specific reason for re-audit)

**Item 1 — margin guide sits BELOW the Q1 print, with the step-down bear counter grafted.**
Review I.3 L514: "the raised full-year 22-23% adj-EBITDA-margin guide (call L28) sits BELOW
the 24.6% Q1 adjusted print (call L8/L34), not above it ... EMBEDS sequential margin
deceleration in the back half: implied Q2-Q4 adjusted margin ~21.1-22.5%, roughly 200-350
bps below the Q1 24.6% peak ... consistent with the FIFA World Cup one-off (+USD 2.5M) ...
reverses in Q2 (call L12/L28, FN5)."

Independent recomputation of the implied H2 step-down (my own math, from raw figures):
- Q1 adj EBITDA = 24.6% x 785.0 = 193.1 Cr (ties deck 193.4, rounding). Q1 rev 785.0.
- FY revenue guide 3,100 Cr; Q2-Q4 revenue = 3,100 - 785 = 2,315 Cr.
- At FY 22.0%: FY adj EBITDA 682.0; Q2-Q4 = 682.0 - 193.4 = 488.6; margin = 488.6/2,315 = **21.1%**.
- At FY 23.0%: FY adj EBITDA 713.0; Q2-Q4 = 713.0 - 193.4 = 519.6; margin = 519.6/2,315 = **22.4%** (~22.5%).
- Step-down vs 24.6%: 24.6 - 22.4 = 2.2 pp (~200 bps) to 24.6 - 21.1 = 3.5 pp (350 bps).

My recompute reproduces A4's "~21.1-22.5%, roughly 200-350 bps below" **exactly**. Cites
L28 (guide, ledger #23) vs L8 (#4)/L34 (#31) 24.6% print all verify in the extract. FIFA
reversal cite L12/L28 verifies (extract src L12: "$2.5 million ... don't expect ... repeat
at the same scale in Q2"; src L28: "expect this to normalize marginally going into Q2").
**Item 1 SATISFIED.**

**Item 2 — magnitude footnoted as +50 bps/bound, not the management-claimed ~100 bps, with
GARBLED_FIGURE note.** Review I.3 footnote † L516: "the raise is +50 bps per bound
(21.5-22.5% -> 22-23%) and +50 bps at the midpoint (22.0% -> 22.5%), NOT the '~100 bps / 1
percentage point' management asserted (call L28, #23). ... ledger_concall #23 is flagged
GARBLED_FIGURE, the source rendering '22 to 23 12%' / '21 12 to 22 1/2%'. The correct
magnitude is +50 bps."

Independent check: lower bound 21.5 -> 22.0 = +50 bps; upper bound 22.5 -> 23.0 = +50 bps;
midpoint 22.0 -> 22.5 = +50 bps. Management's "~100 bps/1 pp" is arithmetically wrong;
the extract src L28 verbatim garble ("22 to 23 12%", "21 12 to 22 1/2%", "roughly 100 basis
points or 1% 1 percentage point") matches; ledger #23 carries GARBLED_FIGURE (ledger L174).
**Item 2 SATISFIED.**

**Item 3 — nothing else changed; rest of Section I re-confirmed from scratch:**

| Element | Where | Independent finding |
|---|---|---|
| Thesis reconciliation — no trigger fired | I.7 L582-588 | T1-T5 all **NOT FIRED**; T3/T4 moved favourably, base reset up. Re-checked against call evidence — correct. |
| Decision Status held WATCHLIST | I.7 L578/L598; YAML L633-634 | **WATCHLIST**, entry Rs390-490, dest PE 19x/24x, UNCHANGED by call. Correct — no pre-committed trigger fired. |
| Cash-conversion INDETERMINATE cap retained | I.3 L511; I.7 L598; YAML L632 | INDETERMINATE cap **held**; 78.8% FCF-conv reasserted on call (src L36) with no cash-flow statement/bridge. Correct per house rule. |
| Answer-to-question scorecard | I.4 L522-542 | Present; 17 questions statused; tally **1 ANSWERED / 3 PARTIAL / 13 DODGED = 17**. Sums correctly; A3's 1/4/12 discrepancy noted and resolved to the itemised count. Correct. |
| All call numbers tie to cited lines | I.1/I.2/I.3/I.6 | Re-derived below (Arithmetic Audit) — every headline reconciles. |

All three re-audit items pass. **The prior gap is closed and no regression introduced.**

---

## AUDIT 1 — COVERAGE (fresh grep pass over the concall extract, diffed vs A2 ledger)

Fresh enumeration (my own ripgrep pass on `extract_concall_rategain_q1fy27.txt`):

| Category | A2 ledger | My fresh count | Method / reconciliation | Status |
|---|---|---|---|---|
| Participants | 8 | 8 | Moderator/BKN, CEO, CFO Ankit, Nitin, Prayer, Deepak, Ash Par, unnamed investor | MATCH |
| Turns | 31 | 31 | 3 section-header turns (OPENING src L4, CFO src L32, CLOSING src L124) + 14 Q + 14 A. "QUESTION AND ANSWER SESSION" = pure divider, not a turn. | MATCH |
| `[Management answer]` markers | 14 (answers) | 15 raw -> 14 | 15th is the line-21 header false positive; A2 excludes it explicitly | MATCH |
| `[Q#` markers | 14 (questions) | 15 raw -> 14 | 15th is the same line-21 header false positive; A2 excludes it | MATCH |
| Mgmt numbers | 59 | 59 (spot-verified) | #1-#44 opening/CFO; #45-#59 Q&A; each spot row located at its cited src line | MATCH |
| Forward/hedge phrases | 14 (8 FC + 6 H) | 14 | FC1-FC8, H1-H6 each located at cited src line | MATCH |

Orphan-row test (ledger row present, absent from A4): I.0 preamble (review L403) blanket-
states "All 31 turns / 14 questions / 59 numbers / 14 forward-hedge rows reviewed," and the
review's I.1/I.2/I.3/I.4/I.5/I.6 physically cite the thesis-load-bearing rows (#1-#44, #47,
#49, #50, #55, #56, #58, #59; FC1-FC8; H1-H6). Operational-only rows not individually
narrated (#12/#13/#19/#51/#52/#54/#57, e.g. the Rs 141 Cr new-contract figure #51 and the
"almost a dozen" #56) are covered by the blanket "reviewed" and are correctly treated as
non-thesis-load-bearing colour (management itself flagged #51's contract-win metric as
"under-represented", extract src L86) — **no thesis-material orphan**. No FAIL.

Missing-from-ledger test (my fresh pass found a row the ledger lacks): none. My counts
equal the ledger in every category. No FAIL.

**COVERAGE = PASS. loop_back(A2)=none, loop_back(A3)=none.**

---

## AUDIT 2 — ARITHMETIC (every derived Section-I / reconciliation metric recomputed from raw)

| Metric | A4 value | My recompute | Raw source | Status |
|---|---|---|---|---|
| Revenue YoY | +187.6% | 785.0/272.9 - 1 = +187.65% | deck L740; CEO "188%" rounding (src L8) | MATCH |
| Sequential QoQ | +9.7% | 785.0/715.5 - 1 = +9.71% | deck L740 (src L34) | MATCH |
| Annualised run-rate | 3,140 Cr | 785.0 x 4 = 3,140.0 | src L8 (#2) | MATCH |
| FY27 rev guide implied YoY | +70% | 3,100/1,823.6 - 1 = +70.0% | FY26 consol rev deck L740 (guide src L28) | MATCH |
| Adj EBITDA margin | 24.6% | 193.4/785.0 = 24.64% | deck L751/L752 (src L8/L34) | MATCH |
| Reported EBITDA margin | 21.9% | 171.5/785.0 = 21.85% | deck L748/L749 (src L34) | MATCH |
| Adj EBITDA YoY | +289.3% | 193.4/49.7 - 1 = +289.1% | deck L751; CFO "89.3%" = dropped-"2" garble of 289.3% | MATCH (garble correctly resolved) |
| Adj PAT YoY | +148.8% | 116.8/46.9 - 1 = +149.0% (base rounding) | deck L766 (src L34) | MATCH |
| Reported PAT margin | 12.1% | 94.9/785.0 = 12.09% | deck L764/L765 (src L34) | MATCH |
| Adj PAT margin | 14.9% | 116.8/785.0 = 14.88% | deck L766/L767 (src L34) | MATCH |
| Deferred consid. annualised | ~80-90 Cr/yr | 21.9 x 4 = 87.6 Cr (in band) | deck L750 (src L8/L34) | MATCH |
| Debt repaid % | 38% | 47.5/125 = 38.0%; outstanding 125-47.5 = 77.5M | loan L44; src L8/L36 | MATCH |
| FCF conversion | 78.8% | 135.2/171.5 = 78.83% | deck L335/L664 (src L36) | MATCH (non-GAAP; unbridged — caps cash conv) |
| Net debt | 615.4 Cr | 871.0 - 255.6 = 615.4 | deck L336/L333/L784+L796 (src L36) | MATCH |
| Margin-guide raise magnitude | +50 bps/bound | 21.5->22.0=+50; 22.5->23.0=+50; mid 22.0->22.5=+50 | src L28 (#23) — mgmt "~100bps" wrong | MATCH (A4 correction is right) |
| Implied Q2-Q4 adj margin | ~21.1-22.5% | 21.1% (FY22%) to 22.4% (FY23%) | 3,100 & 785 & 193.4 | MATCH |
| Step-down vs Q1 peak | ~200-350 bps | 24.6-22.4=220bps to 24.6-21.1=350bps | above | MATCH |
| FIFA/ME net swing & margin | ~$1M net / $600-700k | 2.5-1.5=$1.0M net; 70% x 1.0 = $0.70M | src L12/L71/L74 (#47/#48/#49) | MATCH |
| Scorecard tally | 1/3/13 = 17 | 1+3+13 = 17; Section-D has Q1-Q17 | I.4 vs Section D | MATCH |
| Std vs consol PAT gap Q1FY27 | 4.4% / 95.6% | 4.21/94.91 = 4.44%; gap 90.70/94.91 = 95.56% | res L209/L515 | MATCH |

No mismatch above rounding on any recomputed metric. The single internal call discrepancy
(CEO 289% vs CFO 89.3% adj-EBITDA growth) resolves to the deck's 289.3% and is correctly
labelled a transcription garble, not a filing contradiction. **ARITHMETIC = PASS.
loop_back(A4)=none.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter each)

**Claim 1 (I.7/I.6): "First-ever organic-growth disclosure — combined 17.5%, MK 18.2% —
resolves the inorganic-vs-organic bull/bear split and clears trigger T1."**
Strongest bear counter from the same text: both figures are management-only, appear in NO
audited statement/deck/PR, and management **explicitly refused** clean ex-Sojern attribution
("very difficult to attribute how much would be attribute alone", extract src L80/L98), so
"combined-entity organic" is an unauditable construct volunteered only after the attribution
refusal. **Survives** — but ALREADY grafted (review L491-492, L499, flag L701, I.2 verdict
"UNVERIFIABLE — NEW DISCLOSURE"). No new graft required.

**Claim 2 (I.3): "Dual guidance RAISE (revenue to Rs 3,100 Cr upper end; adj margin to
22-23%) is a confidence posture."**
Strongest bear counter from the same text: (a) the 22-23% FY guide sits BELOW the 24.6% Q1
print, embedding a 200-350 bps H2 step-down consistent with the self-flagged FIFA reversal
(src L28/L12); (b) the revenue "raise" only moves to the upper end of an UNCHANGED 3,100
ceiling — the ceiling was not lifted; (c) the margin raise is +50 bps/bound, not the
mgmt-claimed ~100 bps (GARBLED_FIGURE). **Survives** — this was the prior audit's gap and is
now fully grafted (review L507, L514-516, flags L702). No new graft required.

**Claim 3 (I.3/I.7): "Real deleveraging — 38% of acquisition debt repaid; net-debt-free by
FY28."**
Strongest bear counter from the same text: a same-day board-approved **USD 65M new corporate
guarantee** is NEVER mentioned on the call (silence, Q7 DODGED), and management flagged M&A
"will be an event in 2027" (src L110) — a re-levering path in direct tension with the
net-debt-free claim. **Survives** — already grafted (review L510, L566, L574, L600, flags
L706/L714). No new graft required.

All three strongest bear counters are already present in the A4 review; **no surviving
counter is missing.** loop_back(A4)=none.

---

## VERDICT

**COMPLETE.** The prior INCOMPLETE gap (Section I.3 guidance diagnostic) is closed: the
22-23% FY27 adj-margin guide is now correctly stated as sitting BELOW the 24.6% Q1 print
with the implied ~21.1-22.5% / 200-350 bps H2 step-down bear counter grafted (Item 1), and
the +50 bps/bound magnitude is footnoted against the garbled management "~100 bps" claim
with the GARBLED_FIGURE note (Item 2). The rest of Section I is independently re-confirmed
sound (Item 3): no thesis-broken trigger fired, Decision Status held WATCHLIST, the
cash-conversion INDETERMINATE cap is retained, the answer-to-question scorecard is complete
and internally consistent (1/3/13 = 17), and every call number ties to its cited line under
fresh recomputation. Deliverable gate PASS, coverage PASS, arithmetic PASS, adversarial read
PASS. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "RATEGAIN"
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
surviving_bear_counters: []   # all three strongest counters already grafted into A4
loop_back_to: ""
gap: ""
```
