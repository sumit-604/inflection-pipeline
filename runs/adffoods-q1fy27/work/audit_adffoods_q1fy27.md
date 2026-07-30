# A5 ADVERSARY / COMPLETENESS AUDIT — ADF Foods Limited (ADFFOODS) — Q1 FY27 — LOOP 1 RE-AUDIT

Re-audit of the A4 review after the loop-0 INCOMPLETE loop-back. Independent re-derivation from A1 extracts and A2 ledgers only. This supersedes the loop-0 audit. Loop 1 of a maximum 2.

Run-limitation facts (unchanged, all handled correctly by A4): no concall transcript (Role 5 pre-positioning, master gate OPEN); no prior-quarter ledger (deck-to-deck / entity-list diffs flagged not runnable); Q1 Reg 33 files no cash-flow statement (CFO/CFO-PAT ND, cash conversion INDETERMINATE — cap at PROCEED WITH CAVEATS respected, missing evidence named).

---

## 1. VERIFICATION OF THE THREE LOOP-0 GRAFTS

### PRIMARY graft (consolidated ex-credit EBITDA) — CORRECT
The consolidated correction is grafted thoroughly and propagated everywhere required. Verified:
- Step 2.3 diagnostics 2/3/6 (L169-173): reported +26% now framed as "ENTIRELY a Note-6 one-off"; ex-credit consolidated operating EBITDA "29.65 − 7.29 = 22.36 Cr vs 23.53 Cr prior — a ~5.0% DECLINE"; ex-credit margin ~13.4%; reported PAT flat-to-down.
- Step 3 table + one-off row (L185/L189): "22.36 Cr, a ~5.0% DECLINE"; margin ~13.4% below the 16% break line.
- Step 4 bridge (L197-212): every component re-annotated (EBITDA +6.12 = entirely the credit; ex-credit EBIT ~(2.85); PBT ~(4.91); PAT ex-credit ~(3.3) DECLINE).
- Step 6A (L333), Step 6B, R5 Step 7 (L477): reconciliation now CONTRADICTED on the driver.
- Section C #1 (L508), verdict prose (L525), net-thesis line (L527 "WEAKENED on quality... underlying operating EBITDA declined ~5% YoY"), flags PRIMARY (L611).
- No residual "growth is REAL" / "NOT treasury-flattered" consolidated language survives (grep clean).
Arithmetic re-checked: 29.65 − 7.29 = 22.36; (22.36−23.53)/23.53 = −4.97% ≈ −5.0%; 22.36/167.29 = 13.37% ≈ 13.4%; core PBT ex-OI ex-credit 22.39 − 7.29 = 15.10; post-tax strip 7.29×(1−0.26) ≈ 5.4, PAT ~11.9 vs 15.24. All tie. PASS.

### SECONDARY graft (subsidiary-drag narrowing) — CORRECT
- Section C read (L505): 10.28%→5.44% now labelled "one-off flattered, not clean structural narrowing"; Note-6 refund received by an overseas WOS lands in consolidated PAT and mechanically shrinks the gap; auditor para 7 unreviewed subs still Rs (1.16) Cr loss (L264-275).
- Step 6A row (L255) → AMBER (one-off flattered); Step 6B checklist item 6 (L271) → AMBER; tripwire 9 narrowing "not clean"; monitorable relabelled "ex-tariff-refund" (L550/L606); Step 8.5 Q5 reworded (L585); YAML sc-gap note (L578) and flag (L618). PASS.

### MINOR fix (Q4FY26 consolidated deferred+earlier-tax) — CORRECT
Step 1.2 cell now (0.88) (L102) with derivation at L107 (Total 10.56 − Current 11.44 = (0.88); L361/L342). Matches my recompute (1,056.06 − 1,143.87 = −87.81 L). PASS.

---

## 2. NEW MATERIAL ERROR INTRODUCED BY THE PRIMARY GRAFT — the STANDALONE series

In grafting the consolidated correction, A4 added a NEW claim that the standalone series is clean. This claim is contradicted by the extract and partially resurrects the very "growth is genuine" narrative the loop-back removed — relocated from consolidated to standalone.

**A4's new text:**
- Step 2.2 table (L160): Core Operating PBT (ex-OI) standalone +18.6% verdict = **"Genuine standalone growth."**
- Step 2.2 note (L164): "the refund credit reduces the CONSOLIDATED figure via the subsidiary layer. **The standalone series is therefore the cleaner read of underlying operations this quarter**, and even it shows PAT growth of only +7.6%."
- Step 2.2 table (L151/L169) standalone Op EBITDA margin **+39 bps to 22.77% = "Modest expansion,"** presented without any ex-credit adjustment.

**Why it is wrong (extract, L327 + Note 6 L481):**
"Cost of material consumed" is **identical for standalone and consolidated in every one of the four periods** — Q1FY27 4,232.79 / Q4FY26 5,244.13 / Q1FY26 4,509.97 / FY26 18,827.06 L. It is a parent-only line: subsidiaries are distributors and carry their cost in "Purchases of Stock-in-Trade," which is NOT identical (standalone 440.62 vs consolidated 1,528.38 L, Q1FY27). Note 6 states the Rs 7.29 Cr refund was "recognized as a reduction of **cost of materials consumed** in the Statement of Profit and Loss." Because that line originates entirely in the parent and is identical S and C, the 7.29 Cr credit sits in the parent's standalone P&L and contaminates the standalone series **equally** — it does not, and structurally cannot, reduce a consolidated-only figure "via the subsidiary layer" (subsidiaries contribute zero to cost-of-materials-consumed, so there is nothing at the subsidiary layer for it to reduce). A4's own premise ("all manufacturing is in the parent") defeats its conclusion.

**Corrected standalone ex-credit arithmetic (my recompute):**
- Standalone Op EBITDA ex-OI reported = 24.56 + 3.29 + 0.40 − 0.71 = 27.54. Ex-credit = 27.54 − 7.29 = **20.25 vs Q1FY26 22.46 = −9.8% DECLINE** (not +22.6% / +39 bps expansion).
- Standalone Op EBITDA margin ex-credit = 20.25/120.94 = **16.7% vs 22.38% prior = a ~570 bps CONTRACTION** (A4's "+39 bps modest expansion" is a credit artefact).
- Standalone core PBT ex-OI ex-credit = 23.85 − 7.29 = **16.56 vs 20.11 = −17.7% DECLINE** (A4's "Genuine standalone growth +18.6%" is wrong).
- Standalone PAT ex-credit ≈ 18.28 − 7.29×(1−0.256) = 18.28 − 5.42 = **~12.86 vs 16.99 = DECLINE** (A4's "+7.6% / even it shows PAT growth of only +7.6%" is credit-inflated).

The standalone series is therefore NOT the cleaner read; it is contaminated by the same Rs 7.29 Cr credit and, ex-credit, also declined across EBITDA, PBT and PAT. This is material: it means underlying operations declined YoY at BOTH the standalone and consolidated level, and A4's review currently asserts the opposite for standalone.

---

## 3. ARITHMETIC AUDIT (material items re-run this loop)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Consol Op EBITDA ex-credit YoY | 22.36 vs 23.53 = ~5.0% decline | 29.65−7.29=22.36; −4.97% | L338/335/334/324/481 | PASS (graft correct) |
| Consol ex-credit margin | ~13.4% | 22.36/167.29 = 13.37% | derived | PASS |
| Q4FY26 consol deferred+earlier tax | (0.88) | 1,056.06−1,143.87 = −87.81 L | L361/342 | PASS (fixed) |
| Standalone Op EBITDA ex-OI YoY | +22.6% / +39 bps "modest expansion" | reported ok, but **ex-credit 20.25 vs 22.46 = −9.8%, margin 16.7% vs 22.38% = −570 bps** | L327/338/335/334/324 | **FAIL — standalone presented as clean/expanding; it is equally credit-contaminated** |
| Standalone core PBT ex-OI YoY | +18.6% "Genuine standalone growth" | **ex-credit 16.56 vs 20.11 = −17.7% decline** | L327/338/324/481 | **FAIL — "genuine growth" contradicted by extract** |
| Standalone PAT YoY | +7.6% ("even it shows growth of only +7.6%") | **ex-credit ~12.86 vs 16.99 = decline** | L327/363/481 | **FAIL — credit-inflated, not a clean +7.6%** |

Coverage: unchanged from loop 0 — all ledger rows addressed, all FWD/AMB findings mapped to questions, no orphan or missing rows. No new coverage gap.

Cash-conversion / protocol-verdict handling: unchanged and correct (INDETERMINATE, capped, evidence named).

---

## 4. VERDICT

**INCOMPLETE.** Loop back to **A4** (this is loop 1; one loop remains).

The three loop-0 grafts (primary consolidated ex-credit, secondary subsidiary-drag, minor deferred-tax cell) are all correctly incorporated. However, the primary graft introduced a NEW material error: it frames the STANDALONE series as "the cleaner read" with "Genuine standalone growth (+18.6%)" and standalone margin "+39 bps modest expansion." The extract contradicts this. "Cost of materials consumed" is identical standalone and consolidated in all four periods (L327) — a parent-only line — so the Rs 7.29 Cr Note-6 credit booked to that line (L481) contaminates the standalone series equally. Ex-credit, standalone operating EBITDA is 20.25 vs 22.46 (~−9.8%), standalone margin 16.7% vs 22.38% (~−570 bps), standalone core PBT ex-OI 16.56 vs 20.11 (~−17.7%), and standalone PAT ~12.86 vs 16.99 — all DECLINES. A4 must remove the "standalone is the cleaner read / genuine standalone growth / modest margin expansion" framing (L160, L164, L151/L169), apply the same ex-credit treatment it correctly applied to the consolidated series, and state that underlying operations declined YoY at BOTH standalone and consolidated once the Rs 7.29 Cr credit is stripped. A4's L164 explanation ("the refund credit reduces the CONSOLIDATED figure via the subsidiary layer") must be deleted or reconciled: it is self-contradictory given A4's own premise that all cost-of-materials-consumed sits in the parent.

```yaml
stage: A5-adversary
company: "ADFFOODS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
loop: 1
coverage:
  orphan_rows: []
  missing_from_ledger: []
grafts_verified:
  primary_consolidated_ex_credit: CORRECT
  secondary_subsidiary_drag: CORRECT
  minor_q4fy26_deferred_tax_0.88: CORRECT
arithmetic_mismatches:
  - {metric: "Standalone operating EBITDA ex-Note6-credit (Step 2.2 table/note L151/L160/L164/L169)", a4_value: "+22.6% / +39 bps 'modest expansion' / standalone is 'the cleaner read'", recomputed: "ex-credit 20.25 vs 22.46 = -9.8% decline; margin 16.7% vs 22.38% = -570 bps contraction", source_line: "extract L327 (S COGS = C COGS identical all periods), L481 (7.29 credit), L338/335/334/324"}
  - {metric: "Standalone core PBT ex-OI YoY (Step 2.2 L160)", a4_value: "+18.6% 'Genuine standalone growth'", recomputed: "ex-credit 16.56 vs 20.11 = -17.7% decline", source_line: "extract L327/L338/L324/L481"}
  - {metric: "Standalone PAT YoY (Step 2.2 note L164)", a4_value: "+7.6% ('even it shows PAT growth of only +7.6%')", recomputed: "ex-credit ~12.86 vs 16.99 = decline", source_line: "extract L327/L363/L481"}
surviving_bear_counters:
  - {claim: "Standalone series is the cleaner read of underlying operations; genuine standalone growth +18.6% / +39 bps margin expansion", counter: "Cost of materials consumed is identical standalone and consolidated in all four periods (L327), a parent-only line, so the Rs 7.29 Cr Note-6 credit (L481) contaminates standalone equally; ex-credit standalone operating EBITDA -9.8%, margin -570 bps, core PBT -17.7%, PAT declined. Underlying operations declined YoY at BOTH levels", source_line: "review L160/L164/L151/L169; extract L327/L481"}
loop_back_to: "A4"
gap: "NEW error introduced by the graft: A4 frames the standalone series as 'the cleaner read' with 'Genuine standalone growth +18.6%' and '+39 bps modest margin expansion' (L160/L164/L151/L169). Extract contradicts this: 'cost of materials consumed' is identical standalone and consolidated in every period (L327, parent-only line), so the Rs 7.29 Cr Note-6 credit (L481) contaminates standalone equally. Ex-credit standalone operating EBITDA is 20.25 vs 22.46 (-9.8%), margin 16.7% vs 22.38% (-570 bps), core PBT ex-OI 16.56 vs 20.11 (-17.7%), PAT ~12.86 vs 16.99 - all declines. Apply the same ex-credit treatment to the standalone series; remove the 'standalone is cleaner / genuine growth / modest expansion' language; delete or reconcile the self-contradictory L164 'reduces the CONSOLIDATED figure via the subsidiary layer' explanation. The primary, secondary and minor grafts are otherwise correct."
```
