# A5 AUDIT: CYBERTECH Q2 FY27 (merged review), ITERATION 1 (loop 1 re-audit)

Iteration: 1. The loop-0 audit is preserved at work/audit_cybertech_q2fy27_merged_loop0.md.
Company: Cybertech Systems and Software Limited (CYBERTECH). Quarter: q2fy27. Auditor model: claude-opus-5-5.
Under audit: runs/cybertech-q2fy27/work/review_cybertech_q2fy27.md, rewritten by A4 (918 lines, YAML "loop: 1"; cited "review Lnnn").
Inputs read: the same three A1 fulltexts (results "L", press release "PR L", deck "D L"), three A1 structured files, three A2 ledgers, and the rewritten A4 review. No source PDF, nothing under inputs/, no A3 file opened. A1 and A2 inputs are unchanged since loop 0, so my loop-0 fresh counts stand. Every new or changed number in the rewrite was recomputed from the fulltext lines.

---

## LOOP-0 FINDINGS: CLOSURE CHECK

| ID | Type | Loop-0 gap | Fix found in the rewrite | Re-derivation | Status |
|---|---|---|---|---|---|
| C-1 | CONTRADICTION | Step 5B parent net cash left out the 701.16 lakh non-current treasury investment, unlike Step 5A | 5B table row restated on the 5A basis (review L484); basis note with the roll-forward (L487); restated paragraph with perimeter figures (L489); QfM 10 (L689); brief (L786); flag (L896); seed list (L583) | Parent 31-Mar-2026: 1,585.66 + 3,771.62 + 333.96 + 701.16 - 377.23 = 6,015.17 lakh = 60.15 Cr (L338, L339, L336, L329, L359). Sep-26: 1,330.59 + 538.30 + 706.92 = 2,575.81 = 25.76 Cr. Fall 34.39 Cr. Perimeter 10,944.32 to 14,216.63 lakh (109.44 to 142.17 Cr, +32.72). New figure: subsidiaries' share of current plus non-current treasury investments at March = 10,428.51 / 11,463.63 = 90.97%, so 91.0% (L154, L147, L336). All match. | CLOSED |
| F-1 | FACTUAL | Brief and Step 1D said the parent "must bill" part of the 55% client | Withdrawn. Two readings stated in Step 1D (L299), 1C scope sentence (L262), brief (L784), new QfM 27 (L706, YAML L873), flag (L901), monitorable 12 (L736) | The perimeter's 29.20 Cr = subsidiary external revenue less parent intercompany revenue. 0.55 x 7,329.57 = 4,031.26 lakh; less 2,920.29 = 1,110.97 lakh, so "about 11.1 Cr" for either reading. The text matches the algebra and labels the reading [INFERENCE, conditional]. | CLOSED |
| M-1 | MISSING | Currency counter to "revenue step looks real" (H2 FY26 FCTR) absent | Derived FCTR row (L192); 1C (L261); 2C item 3 (L362); Step 3 table (L380) and replacement diagnostic (L391); 5.5C (L524); claim 1 qualifier (L541); 6.5 (L609); Step 7 growth row (L630); QfM 5 rebuilt (L684); monitorable 5 (L729); brief summary (L758); sector (L774); flag (L899) | 866.80 - 313.14 = 553.66 lakh (+5.54 Cr); 553.66 + 192.92 = 746.58 lakh (+7.47 Cr) (L121). The closing-rate vs average-rate caveat is stated (L391, L774). Sign reading tagged [INFERENCE]. Step 3 now reads "real in rupees; its volume share is unproven" (L391). | CLOSED |

All three loop findings are closed.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Part | Present? | Where | Content check |
|---|---|---|---|
| 1. Summary narrative | present | review L750-L764 | 15 lines (inside the 10-20 line band); now carries the currency line (L758) |
| 2. Sector intelligence | present | review L768-L776 | 9 bullets, evidence-tiered |
| 3. Business-model intelligence | present | review L780-L788 | 9 bullets; F-1 readings (L784) and the parent-vs-perimeter cash split (L786) |
| 4. Competition intelligence | present | review L792-L798 | 7 bullets; peers marked PENDING LIVE VERIFICATION |
| 5. Forward map | present | review L802-L818 | 11 catalysts, each with a bull and a bear fork; every row now has a date or a check date (S-13) |

Gate result: PASS.

---

## 1. COVERAGE AUDIT

The A1 fulltexts, A1 structured files and A2 ledgers are unchanged since loop 0, so the loop-0 fresh counts stand.

| Document | Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | notes | 7 | 7 (L430-L436) | none | PASS |
| Results | line items | 191 | 191 | none | PASS |
| Results | embedded numbers | 42 | 42 (+4 admin identifiers with no row, S-1) | none | PASS |
| Results | agenda items / auditor paragraphs | 1 / 7 | 1 / 7 | none | PASS |
| Results | entities / forward / dates / qualifiers | 46 / 3 / 51 / 46 | 46 / 3 / 51 / 46 | none | PASS |
| Results | structured IDs | 739 | 739 | 0 | PASS |
| Press release | pages / line items / cells / notes | 4 / 14 / 55 / 1 | 4 / 14 / 55 / 1 | none | PASS |
| Press release | structured IDs | 141 | 141 | 0 | PASS |
| Deck | slides / slide numbers / p15 lines | 16 / 205 / 22 | 16 / 205 / 22 | none | PASS |
| Deck | qualifiers / forward / dates / entities | 18 / 1 / 24 / 78 | 18 / 1 / 24 / 78 | none | PASS |
| Deck | structured IDs | 326 | 326 | 0 | PASS |

Ledger rows vs A4: the preamble still marks all 739, 141 and 326 IDs reviewed (review L60-L67). It now lists the uncited results line groups by line as "reviewed, no finding" (L66, S-4). Every A2 flag still maps to an A4 treatment, as tabled at loop 0. The deck's repeated OCI caption (D L331, R284) is now named in the flags (L907, S-5).

Coverage result: orphan_rows = [], missing_from_ledger = []. PASS.

---

## 2. ARITHMETIC AUDIT

The loop-0 PASS rows are unchanged in the rewrite: Op EBITDA, margins, ETR, S-C gap, PAT bridges, CFO ratios, consolidated net cash, buyback core multiples and the equity gap. I spot-checked them against the text at review L198-L205, L239-L245, L253-L258, L406-L432 and L451-L463. New or changed figures:

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Parent net cash Mar-26 / Sep-26 / change | 60.15 / 25.76 / -34.39 Cr (L484) | 6,015.17 / 2,575.81 / -3,439.36 lakh | L329, L336, L338, L339, L359 | PASS |
| SA current-investment roll-forward | 706.92 (L487) | 333.96 + 701.16 + 30.00 - 376.89 + 18.69 = 706.92 | L336, L390, L391, L406, L407 | PASS |
| Perimeter net cash | 109.44 to 142.17 Cr, +32.72 (L489) | 16,959.49 - 6,015.17 = 10,944.32; 16,792.44 - 2,575.81 = 14,216.63 lakh | L147-L178 less parent | PASS |
| Subsidiary share of treasury investments, current + non-current, Mar-26 | 91.0% (L489) | 10,428.51 / 11,463.63 = 90.97% | L154, L147, L336 | PASS |
| H2 FY26 FCTR; Sep-25 to Sep-26 FCTR | +5.54 Cr; +7.47 Cr (L192) | 553.66; 746.58 lakh | L121 | PASS |
| Top-client gap | about 11.1 Cr (L299) | 4,031.26 - 2,920.29 = 1,110.97 lakh | L100, L286; D L254 | PASS |
| QoQ incremental Op EBITDA margin | 48.9% (L362) | 236.98 / 484.84 = 48.88% | L100-L110 | PASS |
| Delivery cost QoQ | +4.7% (L362) | 5,718.20 / 5,459.58 = +4.74% | L104-L105 | PASS |
| Government share of QoQ increment and band | 71.5%; about 57%-86% (L283) | 346.52 / 484.84 = 71.47%; band 275.65-417.38 lakh = 56.9%-86.1% | D L247, L100 | PASS |
| Industry share sums | 100% / 101% / 101% (L267) | 73+9+7+11 = 100; 72+11+9+9 = 101; 68+15+8+10 = 101 | D L247 | PASS |
| SA delivery cost and YoY (claim 3) | 35.14 Cr, +8.8% (L543) | 3,514.27 / 3,228.83 = +8.84% | L290, L291 | PASS |
| OI fall QoQ | 3.45 Cr (L544, L694) | 818.55 - 473.23 = 345.32 lakh | L101 | PASS |
| Direct taxes paid / PBT | 17.5% H1 FY27; 18.8% H1 FY26 (L439) | 422.00 / 2,415.95 = 17.47%; 417.29 / 2,223.34 = 18.77% | L221, L201 | PASS |
| Buyback ex-cash multiple, Q1 FY27 run-rate | Rs 4.40; about 27.7x (L127) | 442.98 x 4 x 0.7512 / 3,02,80,600 = Rs 4.40; 121.76 / 4.40 = 27.7x | L101, L110, L112-L114, L124 | PASS |
| Standalone liability tie (S-11) | 1,492.92 vs 275.09; gap 1,217.83 vs 1,215.22 (L471) | same | L354, L362-L366, L397 | PASS |

Mismatches above rounding: none.

---

## 3. ADVERSARIAL READ (re-run on the rewritten review)

### Claim 1. Core PBT ex-OI nearly doubled; Op EBITDA margin +318 bps (review L336, L752-L753)
Strongest bear counter: one quarter old; 48.9% QoQ incremental margin; all QoQ gain outside the parent; subsidiary margin 2.4% and 2.5% before; Government about 72% of the increment; currency across both bases (L121).
Survives: yes, and fully incorporated (L362, L391, L757-L758, L898-L899). No graft.

### Claim 2. Cash conversion favourable; 1.56x headline, 1.20x-1.23x matched; "the 12.15 Cr liability was kept out of CFO" (review L500, L669)
Bear counter: the H2 reversal of a liability-led release. It survives and is already incorporated (L496, L500, L814).
Second counter, tested against the new claim: the "kept out of CFO" reading rests on the standalone tie (1,217.83 vs 1,215.22 lakh, L354-L397). The consolidated gap is 1,041.38 lakh, which is not an exact tie (L173, L181-L185 vs L218). But the consolidated CF liability line (1,112.60) is about 10.4 Cr below the balance-sheet rise (2,153.98). It could not hold the full 12.15 Cr without an offsetting reclassification of the same size. The counter fails, and the reading stands as an inference. 5A tags it [INFERENCE] (L471). 5C, the verdict basis, the flag and the A4 analyst note state it untagged (L500, L669, L897, L915). STYLE S-14.

### Claim 3. "Number integrity is high"; release and deck tie to the filing except one deck cell (review L558)
Bear counter: the deck is also internally inconsistent where no filing tie is possible. Its industry shares sum to 101% in Q1 FY27 and Q2 FY27 (D L247), and its Q2 FY26 TCI does not foot on its own lines (D L330, D L332).
Survives: yes, as a qualifier. Both facts are already in the review (L108, L267), so no graft. The L558 document-control list and flag L907 do not name the 101% sum. STYLE S-16.

### Mandatory acquisition-economics probe
No external acquisition is described (L223-L231, L145, L73-L76, L431).
Buyback: ~Rs 14.98 Cr / 8,50,000 shares = Rs 176.24 a share.
- vs FY26 EPS: ~18.0x.
- Ex net cash vs FY26 core EPS: ~34.9x.
- Ex net cash vs Q1 FY27 run-rate: ~27.7x.
- Ex net cash vs Q2 FY27 run-rate: ~18.1x.
FY26 is shown to be a trough year against the run-rate (L127). The "not cheap on trailing; fair only if the Q2 run-rate holds" reading is carried (L128).
The 41.13 Cr injection is not a purchase: no ownership change, and 32.64 Cr went to treasury investments (L489).
Probe complete; no graft.

---

## FINDINGS (tagged)

FACTUAL: none. MISSING: none. CONTRADICTION: none.
Leftover pre-fix text: a grep for "53.14", "27.38", "must bill", "weak explanation", "looks real", "cash tax", "35.15" and "3.46 Cr QoQ" hits only the change logs (L19-L23), the "replacing" sentence (L391) and the basis note that records the base error (L487). No stale figure survives in live text.

### STYLE NOTES (logged; no re-run)
- S-1, S-2, S-3 (carried from loop 0; A1/A2 capture, no A4 change needed): admin identifiers without rows (L62, L96, L252, L282; PR L26, PR L30); the L33 subject-line date has no own row; blank-value rows R121, R122, R394, R395 contradict the A1 header convention.
- S-14 (new): "kept out of CFO" is tagged [INFERENCE] at L471 but stated untagged at L500, L669, L897 and L915. Carry the tag.
- S-15 (new): S-7 is only partly applied. The band (about 57%-86%) sits in Step 1D (L283), but the brief still says "about 72%" with no band (L756).
- S-16 (new): name the deck's 101% industry-share sum (L267) in the document-control list (L558) and flag L907.

---

## VERDICT

COMPLETE (iteration 1).
C-1, F-1 and M-1 are closed. The rewrite, including the S-4 to S-13 changes, adds no FACTUAL, MISSING or CONTRADICTION finding. Audits 0-3 pass. Three new STYLE notes (S-14 to S-16) are logged, with no loop. The review may proceed to the Notion save step. The protocol verdict (PROCEED WITH FLAGS) and the cash class (INDETERMINATE-WITH-DIRECTION) are unchanged.

```yaml
stage: A5-adversary
company: "CYBERTECH"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Core PBT ex-OI nearly doubled; Op EBITDA margin +318 bps (review L336, L752)", counter: "one quarter old; 48.9% QoQ incremental margin; gain outside the parent; FCTR +5.54 Cr H2 FY26, +7.47 Cr Sep-25 to Sep-26; already incorporated at L362, L391, L757-L758", source_line: "results L100-L110, L121", type: "STYLE"}
  - {claim: "Number integrity is high (review L558)", counter: "deck industry shares sum to 101% in Q1 and Q2 FY27 and deck Q2 FY26 TCI does not foot; both already in the review (L108, L267); not named in the L558 document-control list", source_line: "D L247, D L330, D L332", type: "STYLE"}
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style: ["S-1", "S-2", "S-3", "S-14", "S-15", "S-16"]
loop_back_to: ""
gap: ""
style_notes:
  - "S-1 (carried) admin identifiers without rows (L62, L96, L252, L282; PR L26, L30); A1/A2 capture, no A4 change"
  - "S-2 (carried) L33 subject-line date has no own row (restates R673)"
  - "S-3 (carried) blank-value rows R121, R122, R394, R395 contradict A1 header convention"
  - "S-14 'kept out of CFO' tagged [INFERENCE] at review L471 but untagged at L500, L669, L897, L915"
  - "S-15 S-7 partly applied: band 57-86% in Step 1D L283, brief L756 still 'about 72%' without band"
  - "S-16 name the deck's 101% industry-share sum (L267) in the document-control list L558 and flag L907"
analyst_note: "Iteration 1 re-audit of the A4 loop-1 rewrite. C-1 closed: parent net cash restated on the 5A basis (60.15 Cr March, 25.76 Cr September, fall 34.39 Cr); the roll-forward and perimeter figures recompute exactly, and the new 91.0% current-plus-non-current share is right (10,428.51 / 11,463.63). F-1 closed: two readings on who bills the 55% client, consistent with perimeter revenue being net of intercompany; QfM 27 added. M-1 closed: H2 FY26 FCTR +553.66 lakh and +746.58 lakh over the year carried through Step 3, 2C, 1C, the brief, the sector line, QfM 5 and the flags, with the closing-rate caveat. Leftover-text grep found only change-log references. All new figures (48.9%, 71.5% with band, 17.5% taxes paid, 27.7x buyback, liability tie) recompute. Three STYLE notes only: the CFO-exclusion inference is untagged in four places, the brief's 72% lacks its band, and the 101% share sum is missing from the document-control list. Inputs unchanged since loop 0, so loop-0 coverage counts stand."
```
