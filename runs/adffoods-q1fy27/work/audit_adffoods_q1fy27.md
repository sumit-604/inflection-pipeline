# A5 ADVERSARY / COMPLETENESS AUDIT — ADF Foods Limited (ADFFOODS) — Q1 FY27 — LOOP 2 FINAL RE-AUDIT

Final re-audit after the loop-1 INCOMPLETE loop-back. Independent re-derivation from A1 extracts and A2 ledgers only. Supersedes the loop-0 and loop-1 audits. Loop 2 of a maximum 2 (final permitted loop).

Run-limitation facts (unchanged, all handled correctly): no concall transcript (Role 5 pre-positioning, master gate OPEN); no prior-quarter ledger (deck-to-deck / entity-list diffs flagged not runnable); Q1 Reg 33 files no cash-flow statement (CFO/CFO-PAT ND, cash conversion INDETERMINATE, capped at PROCEED WITH CAVEATS, missing evidence named).

---

## 1. LOOP-1 RESIDUAL GAP — NOW FULLY CLOSED

The loop-1 gap was: A4 had framed the standalone series as "the cleaner read" with "Genuine standalone growth +18.6%" and "+39 bps modest margin expansion," on a self-contradictory claim that the Rs 7.29 Cr credit only reduced the consolidated figure "via the subsidiary layer." Verified item by item:

**(1) Stale framing removed.** Grep for "cleaner read", "Genuine standalone", "via the subsidiary layer", "modest expansion" returns nothing. The self-contradictory subsidiary-layer explanation is deleted and replaced (L125, L168) with the correct mechanism.

**(2) Corrected read now stated (L125-127, L168, L217).** The credit is booked to cost of materials consumed (L481), a line identical standalone and consolidated in every period (both 42.33 Cr Q1FY27, L327) because all manufacturing is in the parent and subsidiaries are distributors carrying stock-in-trade (correctly attributed to A3-F3). It contaminates BOTH bases equally. Ex-credit:
- Consolidated operating EBITDA 22.36 vs 23.53 = −5.0%; margin ~13.4%.
- Standalone operating EBITDA 20.25 vs 22.46 = −9.8%; margin ~16.7% (−570 bps); core PBT ex-OI 16.56 vs 20.11 = −17.7%; PAT ~Rs 12.9 Cr vs 16.99.
- Both bases decline; explicitly "no clean-growth series exists this quarter on either basis."

**(3) Propagation verified across the review:**
- Step 1.3 — new anchoring note (L125-127) with both bases.
- Step 2.1 consolidated table (L145/L148/L150/L151/L152) — every affected verdict cell relabelled credit-inflated.
- Step 2.2 standalone table (L159-166) — all relabelled; revenue correctly kept clean ("revenue not credit-affected"); new standalone note (L168).
- Step 2.3 diagnostics 1/2/3 (L172-174) — both bases carried, ex-credit margins ~13.4% / ~16.7%, both contract.
- Step 3 (L185/L189) — consolidated QoQ trajectory (consolidated-only by design) reflects ex-credit 22.36 / ~13.4%; standalone not required in a consolidated step.
- Step 4 bridge (L205/L207/L210/L213) + mandatory answers (L216-217) — new dedicated standalone-contamination bullet.
- Step 6B checklist item 2 (L272) and 6C tripwire 6 (L293) — ex-credit consol ~13.4% flagged <16% for one quarter as WATCH (not fired); 6D frozen-mix trigger (L305) — "+39 bps evaporates to −570 bps ex-credit."
- Step 6A (L338) — below-red on ex-credit EBITDA margin; both bases decline.
- Section C reconciliation (L482), filing-signals (L508-514), net-thesis (L532) — all carry both bases.
- Flags (L619) and Step 8.5 Q3 (L588) — both bases.

---

## 2. ARITHMETIC AUDIT (material items, independently recomputed this loop)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Consol Op EBITDA ex-credit | 22.36 vs 23.53 = −5.0% | 29.65−7.29=22.36; −4.97% | L338/335/334/324/481 | PASS |
| Consol ex-credit margin | ~13.4% (contraction ~−430 bps) | 22.36/167.29=13.37%; 17.71→13.37 = −434 bps | derived | PASS |
| Standalone Op EBITDA ex-credit | 20.25 vs 22.46 = −9.8% | 27.54−7.29=20.25; −9.84% | L338/335/334/324/481 | PASS |
| Standalone ex-credit margin | ~16.7% (−570 bps) | 20.25/120.94=16.74%; 22.38→16.74 = −564 bps | derived | PASS |
| Standalone core PBT ex-OI ex-credit | 16.56 vs 20.11 = −17.7% | 23.85−7.29=16.56; −17.65% | L338/324/481 | PASS |
| Standalone PAT ex-credit | ~Rs 12.9 Cr vs 16.99 | 18.28−7.29×(1−0.256)=12.86 | L363/481 | PASS |
| Consol PAT ex-credit | ~Rs 11.9 Cr vs 15.24 | 17.29−7.29×(1−0.264)=11.92 | L363/481 | PASS |
| Bridge ex-credit: EBIT / PBT / PAT change | (2.85) / (4.91) / ~(3.3) | 4.44−7.29=−2.85; 2.38−7.29=−4.91; 11.9−15.24=−3.3 | Step 4 | PASS |
| Consol EBIT operating ex-credit | 15.79 vs 18.64 = decline | 23.08−7.29=15.79 | L338/335/324/481 | PASS |
| Consol reported PBT ex-credit | ~16.20 vs 21.11 = decline | 23.49−7.29=16.20 | L338/481 | PASS |
| Q4FY26 consol deferred+earlier tax (minor) | (0.88) | 1,056.06−1,143.87=−87.81 L | L361/342 (review L107) | PASS (preserved) |

Every corrected figure ties to my independent recompute within rounding. No new arithmetic error was introduced by the second graft.

**Internal consistency check.** Revenue is correctly the sole line held clean of the credit (L159/L172). The ex-credit consol margin (~13.4%) < 16% break line is treated as a one-quarter WATCH, not a fired tripwire — a defensible, non-overstated reading of tripwire 6 ("<16% two consecutive quarters"). The reported-vs-ex-credit distinction is applied consistently across both bases everywhere. A3-F3 is now substantively cited (L125/L168), incidentally closing the loop-0 roster-only observation for that finding. No internal contradiction remains.

**Coverage.** Unchanged: all ledger rows addressed, every A3 FORWARD-SIGNAL / AMBIGUOUS finding maps to a Step 8.5 question, no orphan rows, no missing-from-ledger rows.

**Cash-conversion / protocol verdict.** Unchanged and correct: INDETERMINATE, cap at PROCEED WITH CAVEATS respected, missing evidence (H1 FY27 cash-flow at Q2) named. The strengthened flags do not fire a tripwire; PROCEED WITH FLAGS remains internally coherent and if anything better supported.

---

## 3. VERDICT

**COMPLETE.**

The loop-1 residual gap is fully closed: the "standalone is the cleaner read / genuine standalone growth / modest margin expansion" framing and the self-contradictory "via the subsidiary layer" explanation are removed; the corrected read (Rs 7.29 Cr credit in cost of materials consumed, identical S=C at 42.33 Cr per L327/L481, contaminating BOTH bases; ex-credit consolidated −5.0% / ~13.4% margin and standalone −9.8% / ~16.7% margin, both declining, no clean-growth series) is stated and propagated to Steps 1.3, 2, 3, 4, 6, Section C, reconciliation, net-thesis, verdict prose, flags, and monitorables. All material arithmetic ties on independent recompute; no new error was introduced; the review is internally consistent. Coverage and cash-conversion handling remain correct. This review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "ADFFOODS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
loop: 2
coverage:
  orphan_rows: []
  missing_from_ledger: []
grafts_verified:
  loop0_primary_consolidated_ex_credit: CORRECT
  loop0_secondary_subsidiary_drag: CORRECT
  loop0_minor_q4fy26_deferred_tax_0.88: CORRECT
  loop1_standalone_contamination: CORRECT
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
