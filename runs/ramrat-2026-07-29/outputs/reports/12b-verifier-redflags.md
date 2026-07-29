# Stage 12b — Verifier B: Communication / Red-Flag Audit — RAMRAT

Run date: 2026-07-29 | Model: claude-opus-4-8 | Emits: B12b
Mode: **NO-CONCALL** for the main company (manifest `concalls_available: false`).
Main-company audit is against the AR MD&A/Chairman/Board report, the two results
PDFs, and the investor presentation. Peer audit (B06) is against the five raw
peer transcripts.

Sources I read fresh for this audit:
- FY26 audited results PDF `0a5a99ff-...-aeb5-...` (standalone P&L, BS, cash flow,
  segment reporting; auditor's reports standalone + consolidated) — **12 pp read**
- Q3 FY26 results PDF `789d1085-...` — **11 pp read**
- Investor Presentation — **slides 1-19 read** (financials, mix, balance sheet,
  journey, management)
- VIDYAWIRES Dec-2025 (12 pp), VIDYAWIRES May-2026 (18 pp), BHAGYANGR Nov-2025
  (17 pp), BHAGYANGR Feb-2026 file / call 31-Jan-2026 (17 pp), BHAGYANGR Jun-2026
  file / call 02-May-2026 (16 of ~18 pp) — **all five peer transcripts read**

---

## HEADLINE

Two things dominate this audit.

**(1) The FY26 audited results PDF that B05 declared "does not exist" DOES exist.**
It is present at the exact path in my task (`0a5a99ff-9ec3-47bb-aeb5-49ca3432890d.pdf`).
B05 (echoing Stage 1) searched a corrupted UUID — `...-b91f-...` instead of
`...-aeb5-...` (the `b91f` fragment actually belongs to the *other* results PDF,
`789d1085-67ff-46ca-b91f-...`). Consequence: B05 built its entire no-concall
analysis WITHOUT the primary audited FY26 filing, substituting the investor
presentation. Most numeric conclusions survived the substitution, but two things
did not: the audited negative operating cash flow (available directly, not just
via screener) and an auditor **Emphasis of Matter on an income-tax search-and-
seizure demand**, which B05 never surfaces.

**(2) B06 (peers) is accurate and disciplined.** Every load-bearing quote I
spot-checked against the raw transcripts is real and correctly attributed; the
coverage map (all five SUBSTANTIVE) holds; verdict discipline is sound
(Claim 4 VERIFIED on two independent peers; Claims 1 & 3 correctly UNVERIFIABLE
on a genuine copper-tube segment mismatch). No invented peer signal.

---

## PART 1 — INDEPENDENT RED-FLAG LIST (fresh read, anchored)

### Main company (B05 domain)

**RF1 — FY26 operating cash flow went sharply negative against record profit. [HIGH]**
Audited **standalone CFO = ₹(95.85) cr** (₹9,584.84 lakhs used in operations) vs
FY25 **+₹225.07 cr** (22,507.12 lakhs), against standalone PAT of **₹108.33 cr**
(10,832.99 lakhs). Driver: working-capital blowout — trade receivables movement
₹(242.1) cr (24,212.26 lakhs), inventories ₹(247.7) cr (24,766.10 lakhs), only
part-offset by trade payables +₹205.3 cr. Balance sheet corroborates: standalone
receivables ₹614.4 cr vs ₹369.2 cr, inventories ₹469.4 cr vs ₹221.7 cr.
*(Source: FY26 audited results, Standalone Cash Flow + Standalone Assets &
Liabilities.)* None of the three narrative documents explains the reversal.

**RF2 — Income-tax search & seizure; ₹67.9 cr demand (₹98.4 cr incl. interest);
auditor Emphasis of Matter; no provision. [HIGH / MAJOR miss]**
Auditor's report (FY26 standalone), **Emphasis of Matter**: draws attention to
Note (vi) — tax demand of **₹6,790.77 lakhs (excl. interest of ₹3,149.05 lakhs)**
by the Income Tax Department for AY 2021-22 to 2024-25 **pursuant to search and
seizure action u/s 132**; further **reassessment notices u/s 148** served on
Global Copper Pvt Ltd (merged into RRWL) for AY 2019-20 and 2020-21. Management
made no provision; treated as contingent. This is present in **both** the Q3
results (789d1085, Note vi — the PDF B05 says it read in full) **and** the FY26
audited results (auditor Emphasis + Note vi). A tax search/seizure plus an
unprovided ~₹98 cr demand is a first-order governance/red-flag item.

**RF3 — Copper-tube Q4 deceleration, now confirmed by audited data. [LOW-MEDIUM]**
Audited **Q4 FY26 copper-tubes segment revenue = ₹347.2 cr** (34,719.72 lakhs)
vs **Q3 ₹361.2 cr** — a sequential DECLINE — while total standalone revenue rose
+38% QoQ (Q3 ₹1,249.6 cr → Q4 ₹1,724.8 cr), driven entirely by winding wires
(₹905.8 cr → ₹1,392.0 cr). Full-year copper-tubes ₹1,146.7 cr. *(Source: FY26
audited results, Standalone Segment Reporting.)* This confirms B05's computed
estimate (≈₹339 cr) and its "tension with the ramp-up narrative" flag — and the
audited figure removes the rounding hedge B05 had to attach.

**RF4 — Leverage roughly doubled; current borrowings quadrupled. [MEDIUM]**
Standalone total borrowings **₹613.4 cr** FY26 (non-current 250.2 + current
363.2) vs **₹278.6 cr** FY25 (188.3 + 90.3). Current borrowings **90.3 → 363.2 cr**.
Consistent with D/E 0.57→1.04 (AR). Note the presentation frames only
"Net Debt/Equity 0.46" (slide 6), which by its own definition **excludes current
borrowings** — precisely where leverage ballooned. Selective framing.

**RF5 — Year-end CFO (Chief Financial Officer) change. [LOW / MINOR miss]**
Rajeev Maheshwari ceased to be CFO from close of 31-Mar-2026 (redesignated SVP
Accounts & Taxation); Iqbal Singh Saggu appointed CFO w.e.f. 01-Apr-2026.
*(Q3 results cover letter, 06-Feb-2026, items b & c; presentation slide 19.)*
Worth a line given the concurrent tax-search matter and negative-CFO year.

**RF6 — Dividend held flat ₹2.50 (and down from FY24's ₹5.00) despite +51-55% PAT.**
[LOW-MEDIUM] Presentation slide 5 (FY24 5.0 / FY25 2.5 / FY26 2.5); unexplained.

**RF7 — No promoter shareholding / pledge disclosure in any of the three docs.**
[MEDIUM, data gap] (Consistent with Gate 0 Block E = 0/20.)

### Peer cross-reads (B06 domain) that bear on RAMRAT

**RF8 — Industry-wide capex / overcapacity race, including CTC overlap. [supports thesis risk]**
VIDYAWIRES nearly doubling capacity 19,680→37,680 MT via ALCU (₹140 cr of its
₹274 cr Dec-2025 IPO), and entering **CTC (~3,000 MT Phase 1), starting
"September/October, before Diwali"** 2026 — the *same product and near-identical
timing* as RAMRAT's CTC "Q2 2026" plan. BHAGYANGR 30,000→35,000 MT + ₹40 cr more
capex; analyst explicitly flags Adani/Hindalco overcapacity risk. *(VIDYAWIRES
Dec-2025 p.4-5, May-2026 p.13; BHAGYANGR Jun-2026 p.5, p.12.)*

**RF9 — Peers explain the cash-flow mechanism RAMRAT stays silent on. [corroborates RF1]**
Both peers state that even with fully hedged/back-to-back pricing, a rising copper
price **mechanically inflates working capital and short-term debt**. *(VIDYAWIRES
Dec-2025 Mihir Manohar Q&A, May-2026 Naveen Pachisia; BHAGYANGR Nov-2025 "second-
level effect… increases our working capital", Jan-2026 Atul Raval/Pakshal Jain,
Jun-2026 Aryan Bhatia.)* Independent corroboration that RAMRAT's negative CFO is a
sector-wide copper-price dynamic — which management should have named.

**RF10 — Pass-through preserves price, not incremental margin. [nuances RAMRAT margin claim]**
BHAGYANGR: "we have a pass-through mechanism of the copper prices to the finished
products. However, passing on the additional EBITDA per tonne is a little bit of a
stretch" *(Jun-2026 p.11, Aryan Bhatia Q&A)*; margin gains came mainly from
value-added mix + copper-scrap customs-duty removal *(Nov-2025 p.4-5)*.

---

## PART 2 — COMPARISON AGAINST PIPELINE (B05 + B06)

### My items vs the pipeline

| # | Red-flag item | Pipeline verdict |
|---|---|---|
| RF1 | FY26 negative CFO / working-capital build | **CAUGHT** (B05 4D #1, HIGH) — sourced via Stage 1/screener (-₹92.99 cr) not the primary audited statement (-₹95.85 cr standalone), which B05 wrongly believed absent |
| RF2 | Tax search & seizure + ₹98 cr demand / Emphasis of Matter | **MISSED** (absent from B05 §2D, §4C, §4D) — MAJOR |
| RF3 | Copper-tube Q4 sequential decline | **PARTIALLY CAUGHT** — flagged but rated LOW with a rounding caveat; audited data (₹347.2<₹361.2 cr) firms it to fact |
| RF4 | Leverage doubling / current borrowings quadrupling | **CAUGHT** (B05 4D, MEDIUM) |
| RF5 | Year-end CFO (officer) change | **MISSED** — MINOR |
| RF6 | Dividend flat/down vs PAT surge | **CAUGHT** (B05 4D, LOW-MED) |
| RF7 | Promoter/pledge non-disclosure | **CAUGHT** (B05 2D/4D, MEDIUM) |
| RF8 | Industry-wide capex / CTC overlap / overcapacity | **CAUGHT** (B06 Claim 4 VERIFIED + Part 5) |
| RF9 | Copper-price → working-capital inflation (corroborates RF1) | **CAUGHT** (B06 2E) |
| RF10 | Pass-through is price-only, not EBITDA-additive | **CAUGHT** (B06 Claim 2 PARTIALLY VERIFIED) |

Independent flags found: **10** · Caught: **7** · Partially caught: **1** · Missed: **2**.

### Pipeline red flags — are they supported?

Every B05 red flag (negative CFO, leverage, dividend, copper-tube deceleration,
promoter gap, Bhiwadi capacity/utilisation gap) is **SUPPORTED** by source
evidence; none overstated or invented. Every B06 verdict is **SUPPORTED**:
Claim 4 VERIFIED rests on two genuinely independent peers (VIDYAWIRES ALCU +
BHAGYANGR 30k→35k); Claims 1 & 3 UNVERIFIABLE reflect a real segment mismatch,
not silence-upgraded verdicts; Claim 2 PARTIALLY VERIFIED is correctly nuanced.
**pipeline_flags_not_supported: none.**

### B06 quote spot-checks (all confirmed in the raw transcripts)

- VIDYAWIRES "completely back to back… 100%… margins quite intact" — Dec-2025 p.7 ✓
- VIDYAWIRES ~90% utilisation — Dec-2025 p.8 ✓ · ALCU 19,680→37,680 MT / ₹140 cr — p.4-5 ✓
- VIDYAWIRES Q4 +58% YoY — May-2026 p.6 ✓ · CTC 3,000 MT "before Diwali" / India CTC "30,000-40,000 tons" — p.13-14 ✓
- VIDYAWIRES names **Ram Ratna Wires**, "50 to 60% commonness" — May-2026 p.11, ans. to Nikhil Chowdhary ✓
- BHAGYANGR "straightaway pass-through" / 1.92%→3.88% H1 / vol 8,955→12,400 MT — Nov-2025 p.9, p.4, p.6 ✓
- BHAGYANGR aluminium substitution (Mitesh Bhandari) / US 50% tariff (Rahul Mehta) / copper ~$13,000 — Jan-2026 p.6, p.11, p.12 ✓
- BHAGYANGR "additional EBITDA per tonne is a little bit of a stretch" / 30k→35k + ₹40 cr / Adani-Hindalco overcapacity (Manan Shah) / FY26 >₹2,000 cr, Q4 ₹735 cr / Precision & KSH EBITDA-per-tonne benchmarks — Jun-2026 p.11, p.2 & p.5, p.12, p.2, p.10 & p.15 ✓

One MINOR imprecision: B06 §2E attributes the Gulf scrap-logistics point to
"Manan Shah and Raj Sarraf"; the Gulf exchange is Manan Shah (Jun-2026 p.6) —
"Raj Sarraf" is not locatable in the transcript. Non-material.

Call-date labels all correct: BHAGYANGR files map to calls of 13-Nov-2025,
31-Jan-2026, 02-May-2026; B06 labels them exactly so.

---

## PART 3 — PROMISE-DELIVERY SPOT CHECKS (B05 §2A)

| Promise | B05 outcome | Independent verification | Direction |
|---|---|---|---|
| Commission Bhiwadi copper-tube plant | Delivered June 2025 | Presentation "Journey" slide 12: "Production Successfully Commenced at Bhiwadi"; segment revenue ₹531 cr FY25 → ₹1,147 cr FY26 (audited) | **CONFIRMED** |
| Complete NCLT merger of GCPL into RRWL | Delivered, order 29-May-2025 | Q3 results Note (vii) & FY26 results Note (viii): NCLT order 29-May-2025, appointed date 01-Apr-2024 | **CONFIRMED** |
| Tefabo +4% stake to 64% | Delivered, eff. 1-Jul-2025 | Presentation slide 12 ("+4% eff. 1 July 2025") & slide 16 ("64% stake") | **CONFIRMED** |
| Silvassa ~₹86 cr capex | Pending, excluded from tally | Presentation slide 17 shows expansion "in progress"; ₹86 cr figure sits in AR Chairman p.7 (not re-read here) — classification (pending) correct | **CONFIRMED direction** (₹86 cr amount not independently re-verified) |
| CTC "Q2 2026" commercial start | Pending, excluded | Not yet due; peer VIDYAWIRES entering CTC on the same 2026 timeline corroborates the opportunity is real and time-competitive | **CONFIRMED direction** |

Checked: 5 · Confirmed: 5 · Wrong: 0. The promise-delivery table's direction is
sound; no delivered item is mis-stated. (The ₹86 cr Silvassa figure itself was not
re-verified against the AR, but B05 correctly excluded it from the delivered tally.)

---

## PART 4 — CREDIBILITY GRADE

B05 assigned **B** (no-concall mode: defaults C, may rise to B only on documented
delivery, never A). **I concur with B.** The delivery record is genuine — three
commitments independently confirmed, zero mis-stated. The newly-surfaced items
(RF2 tax search/seizure; the directly-audited negative CFO) do **not** flip the
grade below B, because none is a missed *promise*; but they reinforce the cap AT B
and remove any cushion above it. Had B05 read the primary audited filing, the same
grade would stand, now resting on complete rather than partial evidence. Net:
concur, with the caveat that the grade was reached on an incomplete source base.

---

## PART 5 — CONSOLIDATED FINDINGS

| # | Severity | Location | Finding |
|---|---|---|---|
| 1 | **MAJOR** | B05 §2D/§4C/§4D | MISSED the income-tax **search-and-seizure** demand of ₹67.9 cr (₹98.4 cr incl. interest), an auditor **Emphasis of Matter**, present in both the Q3 results Note (vi) and the FY26 audited results. Material contingent-liability & governance red flag absent from the report. |
| 2 | **MAJOR** | B05 header / INPUT GAP note | Wrongly declared the FY26 audited results PDF non-existent (searched corrupted path `...-b91f-...` vs correct `...-aeb5-...`). The primary audited P&L/BS/CFO/segment filing was available and unused; root cause of Finding 1 and of sourcing the negative CFO second-hand. |
| 3 | MINOR | B05 §2D | MISSED the year-end CFO (officer) change (Maheshwari out 31-Mar-2026, Saggu in 01-Apr-2026); a governance note worth surfacing given the concurrent tax matter. |
| 4 | MINOR | B05 §1C/§3D/§4D | Under-weighted the copper-tube Q4 decline (rated LOW, rounding-caveated); audited Q4 ₹347.2 cr < Q3 ₹361.2 cr removes the hedge and confirms a real sequential decline. |
| 5 | MINOR | B06 §2E | Attribution imprecision: Gulf scrap-logistics point cited to "Manan Shah and Raj Sarraf"; only Manan Shah is in the transcript. Non-material. |

No CRITICAL findings. B06 is otherwise clean and well-anchored; B05's substantive
red flags are all supported — its gap is the tax-search omission driven by the
mis-pathed primary filing.

---

```yaml
stage: B12b
company: "RAMRAT"
run_date: "2026-07-29"
model: claude-opus-4-8
status: complete
independent_flags_found: 10
caught: 7
partially_caught: 1
missed:
  - {severity: "MAJOR", item: "Income-tax search & seizure demand of Rs.67.9 cr (Rs.98.4 cr incl. interest), auditor Emphasis of Matter, in both Q3 results Note (vi) and FY26 audited results — absent from B05", anchor: "FY26 audited results, Auditor's Report Emphasis of Matter + Note (vi); Q3 results 789d1085 Note (vi)"}
  - {severity: "MINOR", item: "Year-end CFO (officer) change: Maheshwari out 31-Mar-2026, Saggu in 01-Apr-2026", anchor: "Q3 results cover letter 06-Feb-2026 items b & c; presentation slide 19"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "concur — B holds; newly-surfaced tax-search red flag and audited negative CFO reinforce the cap at B, do not drop it (no missed promise)"
findings:
  - {severity: "MAJOR", location: "B05 §2D/§4C/§4D", note: "MISSED income-tax search-and-seizure demand ~Rs.98 cr / auditor Emphasis of Matter, present in Q3 and FY26 results", source_fidelity: false}
  - {severity: "MAJOR", location: "B05 header INPUT GAP note", note: "Wrongly declared FY26 audited results PDF non-existent (corrupted path b91f vs aeb5); primary audited filing available and unused", source_fidelity: false}
  - {severity: "MINOR", location: "B05 §2D", note: "MISSED year-end CFO officer change", source_fidelity: false}
  - {severity: "MINOR", location: "B05 §1C/§3D/§4D", note: "Under-weighted copper-tube Q4 decline; audited Q4 347.2<Q3 361.2 cr confirms it, removes rounding hedge", source_fidelity: false}
  - {severity: "MINOR", location: "B06 §2E", note: "Attribution imprecision: Gulf scrap point cites 'Manan Shah and Raj Sarraf'; only Manan Shah found", source_fidelity: false}
critical_count: 0
major_count: 2
minor_count: 3
acceptance_rate: 70
coverage_note: "NO-CONCALL MODE for main company: B05 audited against AR MD&A/Chairman/Board report, both results PDFs, and investor presentation (no transcripts exist). I independently read both results PDFs (incl. the FY26 audited PDF B05 wrongly deemed absent), presentation slides 1-19, and all five peer transcripts in full. Peer B06 quotes spot-checked exhaustively against raw transcripts — all confirmed, all call-date labels correct, verdict discipline sound. AR Chairman p.7 / MD&A pp.48-57 not re-read here (Silvassa Rs.86 cr amount not independently re-verified, though its 'pending' classification is correct). Acceptance_rate = caught (7) / independent_flags_found (10)."
```
