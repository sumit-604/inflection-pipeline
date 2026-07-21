# A5 ADVERSARY / COMPLETENESS AUDIT (FINAL RE-AUDIT, post-loop-2) — TATVA CHINTAN (TATVA), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | FINAL re-audit (after two fix loops)
Fresh context: A4 review + A1 extracts + A2 ledgers only. Re-derived independently; A4/A3 cites checked, not deferred to.
Prior loops, both now claimed fixed: (loop 1) subsidiary 43.1% of YoY PAT growth not carved out of "recurring"; (loop 2) parent's own non-recurring standalone Other Income +Rs 2.66 Cr not netted out of "recurring parent".
Units: Rs Cr = Rs Mn x 0.1 throughout. Source lines are filing-extract lines unless noted "deck".

---

## AUDIT 1 — COVERAGE (fresh grep/sweep vs A2 ledger, then vs A4)

Independent enumeration run over both extracts (full read-through plus targeted grep on notes, agenda, entities, signatures). Counts reproduced exactly; every ledger row is either cited in A4 or carried as reviewed-no-finding (Step 0D note table / Step 1 data tables / Step 6-8.5 mappings).

| Category | A2 count | My fresh count | Orphan rows (ledger not in A4) | Status |
|---|---|---|---|---|
| Results — numbered notes | 13 (7 consol + 6 std) | 13 (C1-C7 L359-390; S1-S6 L538-560) | none — all 13 in Step 0D table | PASS |
| Results — financial line items | 65 (38 consol + 27 std) | 65 (consol L286-344; std L484-522) | none — all in Step 1A/1B | PASS |
| Results — zero-standing items | 6 | 6 (3 NCI, 2 other-equity, 1 std stock-in-trade) | none — all noted | PASS |
| Results — board agenda items | 6 | 6 (L36,46,52,58,64,71) | none — items 1-6 (F6-a/F6-b/F13-a; Step 6D) | PASS |
| Results — annexure Sr-rows | 12 (5 director + 7 capacity) | 12 (5A L112-165; 5B L175-186) | none — director rows F13-a, capacity F6-a | PASS |
| Results — auditor paragraphs | 10 (6 consol + 4 std) | 10 (consol L199-251; std L413-444) | none — Step 0D auditor check + F4-a | PASS |
| Results — consolidation entities | 3 | 3 (L228-230: holding + 2 WOS) | none — Step 4D covers all three | PASS |
| Results — signature blocks | 5 | 5 (L91,262,397,455,569) | none — F14-a/F14-b | PASS |
| Presentation — slides | 36 | 36 (page markers, all walked) | none — "36 slides reviewed" | PASS |
| Presentation — numeric tokens | 1,427 | 1,427 (per-slide sum reconciles) | n/a (token census) | PASS |
| Presentation — reference line items | 64 (slides 6/9/10/34) | 64 (7+19+22+16) | none — Step 1/5/6 cite these | PASS |
| Presentation — footnotes | 6 | 6 (3 rounding, 2 source, 1 safe-harbor) | none | PASS |
| Presentation — zero-standing | 2 | 2 (exceptional FY23; LT-borrowings FY25 dash) | none | PASS |

Rows my fresh pass found that the ledger lacks: **none.**
Minor ledger flags not separately narrated by A4 but sitting inside already-reviewed rows (immaterial, not orphans): EXPERIENCE_YEARS_INCONSISTENCY (Patel 31 vs 30 yrs, annexure row 2), ANNEXURE_LABEL_DUPLICATE. Neither is a substantive row; no loop-back warranted.

**Coverage verdict: PASS — no orphan rows, nothing missing from ledger.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Rs-Mn lines)

Every derived metric re-derived from first principles; raw-Mn used where Cr-rounding would drift.

| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| Consol PAT YoY change | +9.33 Cr (+140.3%) | 15.98 − 6.65 = 9.33; /6.65 = 140.3% | L307 (159.81/66.51) | PASS |
| Consol revenue YoY | +42.9% | 167.06/116.86 − 1 = 42.96% | L286 | PASS |
| Consol Op EBITDA YoY | +86.3% | 322.96/173.30 − 1 = 86.4% | L300/296/295/287 | PASS |
| Op EBITDA margin Q1FY27 / Q1FY26 | 19.3% / 14.8% | 322.96/1670.55=19.33%; 173.30/1168.64=14.83% | derived | PASS |
| Op EBITDA margin YoY delta | +448 bps | 450 bps (19.33 − 14.83 = 4.50pp) | derived | PASS (immaterial ~2 bps; "Expansion" unchanged) |
| QoQ Op EBITDA margin fade | −163 bps | 20.97% → 19.33% = −164 bps | Q4 L300/296/295/287 | PASS |
| Consol ETR Q1FY27 / Q1FY26 | 24.3% / 26.9% | 5.13/21.11=24.3%; 2.45/9.10=26.9% | L306/302 | PASS |
| Core operating PBT (ex-OI) YoY | +130.7% | 18.33/7.95 − 1 = 130.6% | L302 − L287 | PASS |
| Finance cost YoY | +403.9% | 20.81/4.13 − 1 = 403.9% | L295 | PASS |
| Depreciation YoY | +17.8% | 105.66/89.71 − 1 = 17.8% | L296 | PASS |
| Exceptional item (both stmts) | 1.32 Cr | 13.18 Mn x0.1 = 1.32 | L301 / L499 | PASS |
| Std Op EBITDA margin Q1FY27 | 16.4% | (15.41+10.57+2.08−4.03)/146.70 = 16.4% | L498/495/494/485/484 | PASS |
| Std OI / PBT Q1FY27 | 28.6% | 4.03/14.09 = 28.6% | L485/500 | PASS |
| **Step 4A line-item bridge sum** | +9.33 | 14.97 −1.60 −1.67 +1.62 −1.32 −2.68 = 9.32 (≈9.33) | L300/296/295/287/301/306 | PASS (ties within rounding) |
| **4B parent standalone PAT growth** | +5.31 (56.9%) | 104.46 − 51.33 = 53.13 Mn → 5.31; /9.33 = 56.9% | L505 | PASS |
| **4B parent non-recurring OI (pre-tax)** | +2.66 (28.5%) | 40.33 − 13.69 = 26.64 Mn → 2.66; /9.33 = 28.5% | L485 | PASS |
| **4B parent core (post-tax OI strip)** | ≈+3.3 (≈36%) | 5.31 − 2.66×(1−0.259) = 5.31 − 1.97 = 3.34; /9.33 = 35.8% | L505/485, std ETR L504/500 | PASS |
| **4B subsidiary (consol − std)** | +4.02 (43.1%) | (159.81−104.46)−(66.51−51.33)=55.35−15.18=40.17 Mn → 4.02; /9.33 = 43.1% | L307 − L505 | PASS |
| **Post-tax reconciliation to 100%** | 3.3 + 2.0 + 4.02 = 9.33 | 3.34 + 1.97 + 4.02 = 9.33 (100%) | derived | PASS |
| Pre-tax basis reconciliation | core ~2.65 (~28%) + 2.66 + 4.02 = 9.33 | 5.31−2.66=2.65; 2.65+2.66+4.02 = 9.33 (100%) | derived | PASS |
| Headline-basis overlap | ~107.6%, overlap ~0.65 Cr | 3.34+2.66+4.02 = 10.02 → 0.69 (≈0.65 = tax on OI) | derived | PASS (explained, not force-summed) |
| Subsidiary PAT % of consol PAT (Q1FY27) | 34.6% | 55.35/159.81 = 34.6% | L307−L505 / L307 | PASS |
| Subsidiary share history 22.8/12.6/34.6/7.1 | as stated | 15.18/66.51=22.8; 13.0/103.21=12.6; 34.6; 29.72/420.54=7.1 | L307/L505 all periods | PASS |
| Parent PAT share Q1FY27 / Q4FY26 | 65.4% / 87.4% | 104.46/159.81=65.4%; 90.23/103.21=87.4% | L505/L307 | PASS |
| Net debt (FY26 y/e ref) | ~111.58 Cr | 50.10+1153.63−87.91 = 1115.82 Mn → 111.58 | deck L672/676/662 | PASS |

**Arithmetic verdict: PASS — no material mismatch.** The one sub-material item (448 vs recomputed ~450 bps on the YoY margin) is ~2 bps, crosses no threshold, and does not alter the "Expansion" read. The two prior fix-loop items are arithmetically confirmed present and consistent:
- **Loop-1 fix (subsidiary carve-out):** the +4.02 Cr / 43.1% subsidiary slice is explicitly removed from "recurring" — verified.
- **Loop-2 fix (parent's own non-recurring OI netted):** the +2.66 Cr parent standalone Other Income (L485) that 4A tags NON-RECURRING is the same figure 4B strips out of the parent bucket — verified; no double-count. Both clean bases (post-tax 3.34+1.97+4.02 and pre-tax 2.65+2.66+4.02) sum to exactly +9.33 Cr (100%).

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter each)

Materiality bar: a counter "survives" only if (a) supported by the extract AND (b) it materially changes the review's conclusion or an unflagged number AND (c) it is not already disclosed-and-flagged in the review.

**Positive claim 1 — "Strong operating quarter: revenue +43%, operating margin +448 bps YoY, PAT +140% — not a group-treasury artefact." (YoY verdict, L172)**
Strongest bear counter: the +448 bps "expansion" is off an unusually weak Q1FY26 base (14.8%); sequentially the operating margin FADED 21.0% → 19.3% (−163 bps) and now sits below the FY27 20-22% guide, so the trajectory is deteriorating, not expanding. Supported (Q4 L300/296/295/287). **Does NOT survive** — already disclosed and flagged in Step 3 (margin-fade diagnostic), monitor #4 (AMBER), question #4, verdict flag #5.

**Positive claim 2 — "Group headline is operational, not treasury-manufactured (consolidated OI only Rs 2.78 Cr)." (YoY diag #3/#6, L167/170)**
Strongest bear counter: consolidated OI (2.78) is LOWER than standalone OI (4.03), implying the two WOS carry ~−1.25 Cr OI on consolidation; the parent's own PAT is treasury-flattered (OI = 28.6% of standalone PBT) even though the group aggregate is not. Supported (L485 vs L287). **Does NOT survive** — this is exactly the loop-2 fix: the review carves the +2.66 Cr parent OI as non-recurring (28.5% of growth) in Step 4B/4C, flag #2, flag #7, and question #5.

**Positive claim 3 — "Monitor #7 GREEN: standalone PBT Rs 14.09 Cr (>Rs 10 Cr) and parent PAT share 65.4% (>50%), both thresholds met." (Step 6B, L305)**
Strongest bear counter: standalone PBT Rs 14.09 Cr embeds Rs 4.03 Cr one-off OI, so recurring standalone PBT is ~Rs 10.06 Cr — barely at threshold; parent PAT share is falling QoQ 87.4% → 65.4%; and only ~36% of the growth is durable parent core. "GREEN" overstates durability. Supported (L485/L500/L505). **Does NOT survive** — the monitor #7 row itself reads "GREEN (both thresholds met; watch direction + OI quality)" and notes "Rs 4.03 Cr of it is one-off OI; QoQ deteriorating from 87.4%"; reinforced by flags #2/#3.

Additional adversarial probes tested and dismissed (already covered): subsidiary transfer-price durability (flagged UNRESOLVED, top management question); nil standalone current tax flatter (flag #2, question #6); Rs 31.52 Cr inventory build supporting current-quarter gross margin (noted Step 3 + Step 5; the INDETERMINATE cash-conversion cap already gates exactly this WC risk); unexplained Rs 1.32 Cr exceptional (question #5). One angle runs in the company's favour (parent core 3.34 is stated net of the non-recurring Rs 1.32 Cr exceptional drag, i.e. conservatively understated) — not a bear survivor.

**Step 4 internal-consistency judgment:** 4A (line-item bridge) and 4B (entity + recurrence split) are now internally consistent. Both tie to +Rs 9.33 Cr; 4A tags the same +2.66 Cr Other Income non-recurring that 4B strips; the subsidiary +4.02 Cr is carved out of "recurring"; the only >100% figure (the ~107.6% headline) is explicitly explained as the pre-tax-OI-over-post-tax-PAT overlap (~Rs 0.65 Cr = tax on the OI), and both clean bases sum to exactly 100%. The two prior gaps are closed.

**No bear counter survives the materiality bar. Every strongest counter is already stated and flagged in the review — that is COMPLETE, not INCOMPLETE.**

---

## VERDICT

**COMPLETE.** Coverage reconciles (no orphan rows, nothing missing from ledger). Arithmetic recomputes with no material mismatch; the Step 4 three-way split and its post-tax reconciliation to +Rs 9.33 Cr are confirmed exact, and both prior fix-loop items (subsidiary carve-out; parent non-recurring Other Income net-out) are verifiably present and consistent. Adversarial read produces no surviving bear counter — every strongest counter is already disclosed and prominently flagged. No loop-back required. Proceed to Notion save.

```yaml
stage: A5-adversary
company: "TATVA"
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
