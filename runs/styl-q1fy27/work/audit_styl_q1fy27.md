# A5 ADVERSARY / COMPLETENESS AUDIT — STYL Q1FY27

Company: Seshaasai Technologies Ltd (STYL) | Quarter: Q1FY27
Auditor: A5 ADVERSARY | Model: claude-opus-4-8
Under audit: `review_styl_q1fy27.md` (A4). Re-derived independently from A1
extracts + A2 ledgers only (no forensics files, no orchestrator commentary).
Unit: filing INR Mn, x0.1 = Rs Cr; concall already Rs Cr. On OCR pages
(7/8/11/12) both the primary and [OCR CROSS-CHECK] readings were used.

**This file now contains THREE passes.**
- **PASS 3 (BINDING)** — audit of the Role-4+Role-5 UPGRADED merged review
  (concall added). Verdict below is the operative one.
- PASS 2 — re-audit of the Role-4-only base after ARI-1/BEAR-1/COV-1 (history).
- PASS 1 — initial Role-4-only audit (history).

The closing YAML at the very bottom reflects PASS 3 and supersedes the earlier
Pass-2 YAML.

---
---

# PASS 3 — AUDIT OF THE ROLE 5 (CONCALL) UPGRADE  [BINDING]

Scope added since Pass 2: Section 5 (Role 5 concall analysis), concall forensic
findings A3-01..A3-15, re-run Sections 6 (triggers), 7 (questions), 8
(monitorables), 9 (verdict), plus the concall ledger. Role 4 Sections 1-4 were
verified in Passes 1-2 and are spot-re-confirmed unchanged. I re-ran the concall
enumeration with a fresh pass, recomputed the deceleration math from raw numbers,
and stress-tested the concall-derived claims against the extract line by line.

## AXIS 1 — COVERAGE AUDIT (fresh concall enumeration vs A2 ledger vs A4 citation)

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Concall — speaker turns | 58 | 58 | walked turn-map L21-112; body turns L10-88 minus headings | none | PASS |
| Concall — questions (incl follow-ups) | 19 | 19 | `[Q..]` markers: Q1(2)+Q2(3)+Q3(3)+Q4(3)+Q5(2)+Q6(1)+Q7(2)+Q8(3)=19 | none | PASS |
| Concall — analyst firms | 7 | 7 | Safaya/II/Nasir/Lucky/FMY325/SN Daga/Dalmus; DRJ=Dia Jen resolved to 1 | none | PASS |
| Concall — mgmt numbers | 59 | 59 | token sweep of the 15 quantified mgmt lines (L15/17/19/21/23/26/31/33/37/53/55/56/58/62/68); L26 carries 29 | none | PASS |
| Concall — participants | 13 | 13 | 6 company-side + 7 analysts (Gautam Jain silent) | none | PASS |
| Concall — forward/hedge phrases | 18 | 18 | manual sweep §5 ledger (ungated) | none | PASS |
| Results / Presentation (carried) | as Pass 1 | matches | re-confirmed no regression | none | PASS |

**Orphan-row test (every ledger row cited in A4 or reviewed-no-finding):**
- MGMT_ABSENCE (Gautam Jain silent, ledger §1) → A4 A3-09 / trigger 13 / Q29. Cited.
- REPEAT_QUESTION (3-analyst margin ask, ledger §3) → A4 A3-02 / trigger 7 / Q19. Cited.
- Q13 insurance client count 13→10 / 9→10 stated by the ANALYST from a deck slide,
  not management (ledger note on Q13) → A4 A3-07 / Q28. Cited, with the analyst-
  source caveat preserved. Correct handling.
- 59 mgmt numbers: the headline set (377/21.1%/-6.9%/157/41.7%/44.5%/58.34%/411bps/
  54.23%/94/25.1%/135bps/82/48.8%/60/16%/418bps) is cited in §1 and §5.9; the
  guidance set (8-12%, 140-160, IoT 45/35-40, payments 10-12, CFS flat/30%, SIM
  20-25%/~40%, mix 15-18%) is cited in §5.2. No quantified mgmt number left
  un-dispositioned. No orphan.

**Fresh-pass rows the ledger lacks:** none. My enumeration reproduces the A2
concall ledger exactly (three-way agreement A1 header / A2 grep / my sweep).

Coverage verdict (Pass 3): **complete — no orphan row, no ledger gap.** But see
Axis 3: one A4 *interpretation* mis-uses a row the A2 presentation ledger DID
capture (company-wide vs segment top-10) — a review-correctness defect, not a
coverage/enumeration gap.

## AXIS 2 — ARITHMETIC AUDIT

### 2A. Headline / derived / bridge / ETR / S-vs-C — all re-confirmed
Re-ran every Section 1/2c/3 figure from the OCR-cross-check raw numbers. All tie
out (selected):
- Revenue YoY 65.60/310.87 = **+21.1%**; QoQ -27.71/404.18 = **-6.9%**. ✓
- Reported EBITDA Q1FY27 = PBT 81.79 + D 10.78 + Fin 1.84 = **94.41**; margin
  94.41/376.47 = **25.08%**. ✓  Operating EBITDA 94.41 − OI 7.10 = **87.31**;
  margin **23.19%** (+22 bps YoY, -611 bps QoQ). ✓
- Gross profit Q1FY27 = 3,764.70 − (2,283.14+8.32−95.05) = 1,568.29 Mn =
  **156.83 Cr**; GM **41.66%**. Q4FY26 = **189.65** (ARI-1 fix holds); Q1FY26 =
  **138.40**. GM -286 bps YoY / -527 bps QoQ. ✓
- ETR 21.50/81.79 = **26.29%** (vs 33.0% Q1FY26, 26.81% Q4FY26). ✓
- PAT bridge closes to **+23.50** (components sum 23.46, rounding noted by A4). ✓
- C−S PAT gap -1.41 Cr; pre-NCI 60.284 − 61.745 = -1.461; subsidiaries net
  -0.138 (loss 2.15 Mn + profit 0.77 Mn) ⇒ **~Rs 1.32 Cr consolidation
  adjustment** (A4 "~Rs 1.3 Cr"). ✓
- Concall internal checks: COMC 2,196.41/3,764.70 = **58.34%**; FY26 avg
  7,815.43/14,411.35 = **54.23%**; diff **+411 bps**. ✓  Payments 1,582/3,764.70
  = 42.0% and +5.6% YoY (≈+5%); IoT 674/3,764.70 = 17.9% (≈18%) and +144.2%
  (≈+145%); CFS 1,488 = 39.5% (≈40%) and +12.9% (≈+13%). ✓  Net cash 3,690 Mn =
  **369 Cr**; unutilised IPO 1,700.8 Mn = **170.1 Cr**; capex-earmark unutilised
  1,360.92 Mn = **136.1 Cr**; deployed this qtr 244.0 Mn = **24.4 Cr**. ✓

### 2B. THE concall deceleration math (task-mandated independent re-derivation)
FY26 base 1,441.14. Guide +8/+12% → FY27 **1,556.43 / 1,614.08 Cr** (A4 "1,556-
1,614" ✓). Less Q1FY27 376.47 → remaining 9M **1,179.96 / 1,237.61 Cr** (A4
"1,179-1,237" ✓). FY26 9M = 1,441.14 − 310.87 = **1,130.27 Cr** (A4 "1,130" ✓).
Remaining-9M YoY = **+4.40% to +9.50%** (A4 "+4.3% to +9.5%"; my +4.40% vs A4
+4.3% is the Q1=377-rounded vs 376.47 choice, ~0.1 pp, within rounding).
**CONFIRMED: an 8-12% full-year guide off the Rs 1,441 Cr base, net of the Rs 377
Cr Q1, does imply only ~+4-10% YoY for the remaining nine months** vs the +21.1%
Q1 print — the lead A3-01 deceleration finding foots.

### 2C. ARI-3 (NEW) — segment-blend weighted-growth figure does not foot
A4 §5.2 (review L370-373): "Payments +10-12% (42% of mix) + CFS ~flat (40%) + IoT
+45% (18%) blends to roughly **+5% to +10% weighted** — i.e. the segment guides
themselves imply **~8-12%**."
Recompute with A4's own weights/rates: 0.42×(10..12) + 0.40×0 + 0.18×45 =
(4.2..5.04) + 0 + 8.1 = **+12.3% to +13.1%**. The stated "+5% to +10%" is wrong by
~3-8 pp (above rounding), and the "~8-12%" restatement understates it — the true
blend sits **at/just above the top of the 8-12% headline band**. Direction of the
error is FAVOURABLE to A4's own thesis (a blend of ~12-13% vs an 8-12% headline
makes the guide look *even more* conservative/below the +21.1% run-rate), so no
conclusion flips — but the arithmetic as printed is a mismatch. **Loop A4.**
Materiality: LOW (narrative reconciliation; headline deceleration math in 2B is
independently correct and unaffected).

## AXIS 3 — ADVERSARIAL READ (three most-positive claims + strongest bear from the same text)

1. **Revenue +21.1% YoY, trigger 1 FIRED FAVOURABLY.** Bear from same text:
   -6.9% QoQ; laps a "relatively subdued Q1FY26 base" (deck L508); the full-year
   8-12% guide implies the remaining 9M decelerates to +4-10% (2B). **Counter
   already carried** by A4 (A3-01 §5.3, X1). Does not survive as new.
2. **IoT +145% YoY, trigger 3 FIRED FAVOURABLY / IoT>Rs55Cr MET.** Bear: mgmt
   itself calls +145% a weak-base artifact (L68), guides only +45% FY27 with mix
   flat 15-18%, and IoT is NOT a statutory segment (unaudited, F12-01). **Counter
   already carried** by A4 (A3-03, trigger 3 "unaudited"). Does not survive as new.
3. **Net cash Rs 369 Cr / "well capitalized."** Bear: no Balance Sheet or Cash
   Flow filed (unaudited, deck/concall only); ~Rs 170 Cr is unutilised IPO not
   operating cash; mgmt confirms a deliberate cash-CONSUMING chip-inventory build
   (L82). **Counter already carried** by A4 (COV-1, A3-13, cash conversion
   INDETERMINATE). Does not survive as new.

No NEW surviving bear counter to graft. HOWEVER the adversarial axis also tests
*overstated* claims, and one A4 negative claim is unsupported:

**ADV-3 (NEW) — the "56% vs 73% top-10 concentration" contradiction is a FALSE
FLAG, resolvable from the extract.** A4 §5.9 (review L566-568) calls it "the one
material narrative-vs-source conflict," lists it as a Flag (L956), and raises
Q23 (L721). But the deck itself reconciles it:
- Concall top-10 = **56%** (L26); results press release top-10 = **56%** (results
  L131); deck slide 22 company-wide "Revenue from Top 10 Customers Q1FY27 =
  **56.0%**" (presentation L683); deck slide 16 client-concentration Top-10 =
  **56%** (presentation L489). All four AGREE.
- The **73%** is on deck slide 12, the **Payment Solutions segment** slide
  ("Top 10 customers contributed 73% of the revenue for Q1 FY27," presentation
  L325) — i.e. a *segment-level* top-10, exactly as slide 13 gives CFS-segment
  top-10 = 77.16% (L362).
So there is no company-level contradiction: 56% (company-wide) vs 73% (Payment
Solutions segment). The A2 presentation ledger captured **both** rows (slide 12 =
73% payments; slide 22 = 56.0% company-wide), so this is NOT an A2 enumeration
gap — it is an A4 interpretation error that elevated a segment/company scope
difference to a "material conflict," a standing flag, and a management question.
**Loop A4** (origin A3-06). Materiality: LOW-MODERATE — it inflates the "adverse
cluster widened" narrative (§6) and creates a spurious management ask (Q23); it
does not change the PROCEED WITH FLAGS verdict, but it should not propagate to
Notion as written.

## PASS-3 DISCREPANCY LIST

| ID | A4 claim | My recomputation / finding | Line cite | Loop | Materiality |
|---|---|---|---|---|---|
| ARI-3 | Segment guides "blend to roughly +5% to +10% weighted … imply ~8-12%" | 0.42×(10-12)+0.40×0+0.18×45 = **+12.3% to +13.1%** (at/above top of band); "+5-10%" is off by ~3-8 pp | review L370-373; concall L53/55/56 + mix L17/19/21 | A4 | LOW (conclusion unaffected / reinforced) |
| ADV-3 | Top-10 "56% (concall) vs deck ~73%" = "the one material narrative-vs-source conflict" (flag + Q23) | No conflict: 56% is company-wide (deck slide 22 L683, slide 16 L489, PR L131, concall L26); 73% is the **Payment Solutions segment** top-10 (deck slide 12 L325); deck reconciles it | review L566-568/L721/L956; presentation L325/L489/L683; results L131; concall L26 | A4 (origin A3-06) | LOW-MOD |

Confirmed-sound (no action): deceleration math (2B, +4.4-9.5% ✓), COMC/GM bridge,
ETR, PAT bridge, C−S gap, all trigger reconciliations, IoT/Payments/CFS mix and
YoY, cash/IPO figures, the ARI-1/BEAR-1/COV-1 fixes from Pass 2.

## PASS-3 GATE VERDICT

**INCOMPLETE — loop to A4.** Two bounded review-correctness defects in the Role 5
material must be fixed before Notion save:
1. **ARI-3** — correct the §5.2 segment-blend from "+5% to +10% weighted / ~8-12%"
   to the recomputed **~+12-13%** (which, note, strengthens rather than weakens the
   "guide is conservative/below the +21.1% run-rate" reading).
2. **ADV-3** — retire/down-rank the "56% vs 73%" *material contradiction*: the deck
   resolves it as company-wide top-10 (56%, slide 22/16, matching concall/PR) vs
   Payment-Solutions-segment top-10 (73%, slide 12). Restate as a benign
   scope/label note; the standing Flag and management question Q23 should be
   retired or re-scoped to "confirm segment-vs-company basis," not carried as an
   open contradiction.

Everything else in the concall upgrade is sound: coverage reproduces the A2
concall enumeration exactly (no orphan, no gap); the lead A3-01 deceleration math
foots to +4-10% 9M YoY; the trigger scorecard, cash-conversion INDETERMINATE cap,
PROCEED WITH FLAGS verdict and HELD Decision Status are all supported. These are
narrow A4 corrections, not a re-run.

---
---

# PASS 2 — RE-AUDIT (after A4 applied ARI-1, BEAR-1, COV-1) — Role-4-only base [HISTORY]

Scope: confirm each of the three bounded fixes landed correctly and accurately;
confirm nothing else in the review changed; confirm no new arithmetic or
coverage error was introduced by the edits.

## Fix-by-fix confirmation

**ARI-1 — CONFIRMED.** Section 2c (review L141) now reads Gross profit
`138.40 | 189.65 | 156.83 | ND`; the 190.66 slip is gone. Footnote L153-156
shows the working (Rev 404.18 − net materials 214.53 = 189.65 Cr) and the
independent deck cross-cite (slide 15 = 1,897 Mn = 189.7 Cr, presentation
extract L445), and states Q4FY26 gross margin 46.9% is unchanged. My independent
recompute: 404.176 − 214.524 = **189.652 → 189.65 Cr**; 189.65 / 404.18 =
46.92% → 46.9%. Both correct. (The intermediate net-materials shown as 214.53
vs the precise 214.52 is a 0.01 display-rounding of the subtrahend; it does not
change the stated 189.65 result — immaterial.)

**BEAR-1 — CONFIRMED.** Section 3 (review L192-198) now states "Q1FY27 PAT margin
of 16.0% is BELOW the FY26 full-year 16.7%" that management itself cites
(presentation extract L529-532), and ties it to the derived FY26 PAT margin
16.65% in Section 2c. A new Questions-for-Management **row 17** (L333) asks
whether FY27 PAT margin will exceed 16.7%. The question count is reconciled to
"all 17" (L343) and the closing YAML carries 17 QfM entries. The counter is also
surfaced in the Flag list (L382-383, L478). Text support verified: 16.03% <
16.65% (FY26 derived) and < 16.7% (management benchmark, L532).

**COV-1 — CONFIRMED.** Section 3 (review L204-219) is corrected: net cash is
"NOT ND" — the deck discloses cash & cash equivalents ~Rs 3,690 Mn (~Rs 369 Cr)
at 30-Jun-2026 incl ~Rs 1,700 Mn unutilised IPO (presentation extract L950-951;
A2 presentation ledger Table 4 narrative) — while the **cash-CONVERSION quality
remains explicitly INDETERMINATE** (no CFO / CFO-PAT / receivable / inventory /
payable days without the Cash Flow Statement). The verdict block, monitorables,
and QfM row 11 are updated consistently. Load-bearing conclusion (cash conversion
INDETERMINATE) preserved.

## No-regression confirmation (Role-4-only base)

| Item | Expected | Status |
|---|---|---|
| Protocol verdict | PROCEED WITH FLAGS | UNCHANGED |
| Cash-conversion cap | INDETERMINATE, subsumed by FLAGS | UNCHANGED |
| Decision Status | HELD 4% at Rs 287 (Notion ts 2026-06-16) | UNCHANGED |
| Position branch | 8A | UNCHANGED |
| Headline scorecard (§1) | as Pass-1-verified | UNCHANGED |
| PAT bridge (§3 table) | +23.50 (23.46 rounding) | UNCHANGED |
| A3 findings table (§4) | 20 findings | UNCHANGED |

## Pass-2 GATE VERDICT (superseded by Pass 3)

**COMPLETE** for the Role-4-only base. All three bounded fixes landed correctly.
This verdict governed only the pre-concall review; the concall upgrade is
re-audited in Pass 3 above, which is now binding.

---
---

# PASS 1 — INITIAL AUDIT (verdict INCOMPLETE — Role-4-only base) [HISTORY]

## AXIS 1 — COVERAGE AUDIT (fresh enumeration vs A2 ledger vs A4 citation)

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — numbered notes | 12 (6C+6S) | 12 | notes-section sweep L571/577/611/616/620/625 + L967/973/1005/1010/1015/1020 | none | PASS |
| Results — statement line items | 60 (32C+28S) | 60 | full sweep L385-500 / L813-905; NCI rows OCR-variant "Controlhng" confirmed | none | PASS |
| Results — auditor paragraphs | 10 (6C+4S) | 10 | C paras 1-6 (L270-349), S paras 1-4 (L718-774) | none | PASS |
| Results — board-agenda items | 5 | 5 | covering letter L52-63; no AGM/dividend/director/auditor/ESOP item | none | PASS |
| Results — consolidation entities | 2 | 2 | Rite Infotech (L304), Atoll Solutions (L305) | none | PASS |
| Results — zero-standing rows | 3 | 3 | C-OCI equity (L453), S-Exceptional (L847), S-OCI equity (L875) | none | PASS |
| Results — signature blocks | 5 | 5 | CS (L68), MD x2 (L629/1024), Auditor x2 (L351/777) | none | PASS |
| Results — Note-2 IPO sub-rows | 20 | 20 | 5 objects x 2 tables x 2 columns | none | PASS |
| Presentation — slides | 32 | 32 | `^\[page N\]` markers | none | PASS |
| Presentation — slide-6 claims | 12 | 12 | L153-188 | none | PASS |
| Presentation — slides 17/18 P&L | 20 | 20 | L503-533 / L543-574 | none | PASS |
| Presentation — slide-31 IPO objects | 4 (+Total) | 4+1 | L930-948 | see COV-1 | PASS w/ note |

Structural confirmations: No Balance Sheet / no Cash Flow in the results filing
(grep for `Balance Sheet|Cash Flow|Assets|Liabilities` returns only the
press-release phrase "strengthen cash flows" L187, not a statement header).
Standalone carries 4 fewer rows than Consolidated (2 NCI + duplicate "7."),
expected. Every A2 flag traced to an A4 disposition (no orphan forensic).

**COV-1 (initial):** A4 stated net debt/net cash "all ND," but slide 31 (L950-951,
in A2 ledger Table 4) discloses cash ~Rs 3,690 Mn. Required A4 correction. LOW.

## AXIS 2 — ARITHMETIC AUDIT

All headline, extraction, derived, PAT-bridge, ETR, margin, and standalone-vs-
consolidated figures recomputed from OCR-cross-check readings and CONFIRMED,
with a single exception:

**ARI-1 (initial):** Gross profit Q4FY26 = 190.66 (A4) vs 189.65 (recomputed;
404.18 − 214.52; deck 1,897 Mn = 189.7 Cr, L445). +1.01 Cr digit slip,
non-load-bearing (GM% 46.9% correct), but above rounding → A4 correction.

## AXIS 3 — ADVERSARIAL READ

- Positive claim 1 (Revenue +21.1% FIRED FAVOURABLY): bear counter (subdued
  Q1FY26 base / flat-to-declining 3yr) already carried by A4 (X1/F16a/Q14).
- Positive claim 2 (EBITDA +28% / margin +135 bps): bear counter (other-income-
  driven, operating +22 bps) already fully made by A4.
- Positive claim 3 (PAT +63.8% / margin 16.0%): bear counter — 16.0% BELOW FY26
  16.7% (management's own benchmark, deck L529-532) — NOT stated by A4.
  **SURVIVES (BEAR-1)**, grafted in Pass 2.

## PASS-1 GATE VERDICT

INCOMPLETE — loop to A4 for ARI-1 / BEAR-1 / COV-1. Coverage otherwise complete;
arithmetic otherwise sound. (Superseded by Pass 2 = COMPLETE for the base, then
by Pass 3 = INCOMPLETE for the concall upgrade.)

---

```yaml
stage: A5-adversary
company: "STYL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE               # COMPLETE | INCOMPLETE
coverage:
  orphan_rows: []                 # concall/results/presentation enumeration reproduced exactly; no orphan
  missing_from_ledger: []         # fresh pass found nothing the A2 ledgers lack
arithmetic_mismatches:
  - {metric: "segment-blend weighted revenue growth (§5.2)", a4_value: "+5% to +10% (\"imply ~8-12%\")", recomputed: "+12.3% to +13.1% (0.42x(10-12)+0.40x0+0.18x45)", source_line: "review L370-373; concall L17/19/21/53/55"}
surviving_bear_counters: []       # the 3 most-positive claims' counters are already incorporated (A3-01/A3-03/COV-1+A3-13)
loop_back_to: "A4"
gap: "Two Role-5 review-correctness defects for A4 before save: (ARI-3) the §5.2 segment-blend arithmetic '+5% to +10% weighted / ~8-12%' does not foot to A4's own weights/rates — recompute to ~+12-13% (error is thesis-favourable, no conclusion flips); (ADV-3) the '56% vs 73% top-10 concentration' called 'the one material narrative-vs-source conflict' (flag + Q23) is a FALSE conflict resolvable from the deck — 56% is company-wide (deck slide 22 L683 / slide 16 L489, matching press release L131 and concall L26) while 73% is the Payment Solutions SEGMENT top-10 (deck slide 12 L325, cf CFS-segment 77.16% slide 13 L362); origin A3-06. Retire/re-scope the flag and Q23. Deceleration math (A3-01, +4-10% 9M YoY), trigger scorecard, INDETERMINATE cash cap, PROCEED WITH FLAGS verdict and HELD status all independently confirmed."
```
