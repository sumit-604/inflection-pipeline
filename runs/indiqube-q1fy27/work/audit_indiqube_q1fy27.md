# A5 ADVERSARY / COMPLETENESS AUDIT — IndiQube Spaces Limited (INDIQUBE), Q1FY27

Auditor: A5 (Opus 4.8), fresh context. Inputs seen: A4 review, A1 extracts (5), A2 ledgers (5).
Re-derived independently; A4/A3 cites were checked, not trusted. Units: results filing +
monitoring report in Rs millions (×0.1 → ₹ Cr); press release + deck native ₹ Cr. Company is
standalone-only, single reportable segment (results Note 5, L249-250) → standalone-vs-consolidated
gap is structurally **N.A.**, not a missed metric (confirmed independently: no subsidiary /
"consolidat" / "Group" statement anywhere in the 285-line results extract).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

PLAIN-LANGUAGE BRIEF located at review lines 462-478. All four labelled parts present and carry
real, non-placeholder content:

| Part | Heading present | Lines | Non-empty / real content | Status |
|---|---|---|---|---|
| 1. Summary narrative | "### 1. SUMMARY NARRATIVE" | 464-466 | ~24-line prose narrative, numbers-anchored | PRESENT |
| 2. Sector intelligence | "### 2. SECTOR INTELLIGENCE" | 468-470 | GCC demand up-cycle, Ind AS 116 sector optics, CRISIL monitoring regime | PRESENT |
| 3. Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" | 472-474 | 3 revenue lines, unit economics, ₹1,650/sqft, VAS drift, IPO redirection | PRESENT |
| 4. Competition intelligence | "### 4. COMPETITION INTELLIGENCE" | 476-478 | Awfis/Smartworks/EFC/WeWork India, moat, supply-discipline risk, provenance line | PRESENT |

**Gate 0: PASS.** All four brief parts present and substantive.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledgers)

Fresh grep/sweep pass over each A1 extract, diffed against the A2 count tests. My counts reproduce
every A2 count exactly — **A2 enumeration is clean; nothing my fresh pass found is missing from the
ledgers** (missing_from_ledger = none).

| Category (doc) | A2 count | My fresh count | Match | Orphan-in-review? |
|---|---|---|---|---|
| results: numbered notes | 6 | 6 (Notes 1-6; Note 1 OCR'd "I") | yes | no |
| results: Note-4 footnotes | 4 | 4 (•, ••, #, A) | yes | no |
| results: statement line items | 29 | 29 (L166-199) | yes | no |
| results: IPO-utilisation rows | 8 | 8 (7 objects + total) | yes | no |
| results: auditor paras | 4 | 4 (L89/95/103/124) | yes | no |
| press: reconciliation rows / cells | 16 / 96 | 16 / 96 (L118-135) | yes | no |
| press: mgmt-quote numbers | 16 | 16 | yes | no |
| deck: slides / chart flags | 35 / 8 | 35 / 8 (OCR pages 2,3,4,5,7,14,24,27) | yes | no |
| deck: table line items / data points | 70 / 234 | 70 / 234 (spot-reconciled) | yes | **see D222 below** |
| monitoring: deployment rows | 65 (2 bank + 62 FD + total) | 65 | yes | no |
| monitoring: cost/progress/delay/new-objects | 10/10/2/4 | 10/10/2/4 | yes | no |
| agm: proceeding items / resolutions / persons | 14 / 3 / 7 | 14 / 3 / 7 | yes | see NAME_INCONSISTENCY |

**Material flag-class incorporation check (every A2 forensic flag → is it in A4?):**
- DEVIATION_DECLARED / NEW_OBJECT / DELAY_IN_IMPLEMENTATION / DROPPED_DESCRIPTION (monitoring): all
  incorporated (Step 0D Note 4, Step 6B #3, Step 8B, Q5-Q7, brief). ✓
- MGMT_GUIDANCE (deck D133-135: ₹52 Cr deal, 39K D&B, 3.9 Lakh Noida): incorporated (Step 6D, Q8). ✓
- DIRECTOR_ABSENT + Scrutinizer dual-role (AGM): incorporated (Step 6B #4, Q14, Q15). ✓
- ARITHMETIC_VARIANCE #1 — EBIT Ind AS 96-vs-97 (deck D108/D109): incorporated (Step 1B, NEUTRAL-FACT). ✓
- **ARITHMETIC_VARIANCE #2 — Net Impact on P&L 75-vs-74 (deck D222): NOT incorporated. ORPHAN.**
- NAME_INCONSISTENCY Meghana/Meghna (AGM Table 3): not cited — immaterial spelling variance, acceptable.
- MINOR_VARIANCE D158 (sourcing mix sums 98%): not cited — immaterial, acceptable.

**COVERAGE FINDING — ONE ORPHAN ROW.** A2 deck ledger row **D222** (page 26 / slide 25, "Net Impact
on P&L") is explicitly flagged `ARITHMETIC_VARIANCE`: "Q1FY27: 264−190=74, but slide states 75 (off
by ₹1 Cr)... flagged for A3." I re-derive independently: 116 (interest on lease liabilities, deck
L721) + 148 (ROU depreciation, deck L723) = 264 (deck L725, ties) − 190 (payment of lease
liabilities, deck L727) = **74**; the deck prints **75** (deck L729). The Q1FY26 column ties exactly
(100+113−140 = 73). A4's review surfaces the *twin* ₹1 casting variance (EBIT 96-vs-97) in Step 1B
as a NEUTRAL-FACT but is silent on this parallel, A2-enumerated variance in the very next slide's
Ind AS 116-impact table. This is an orphan ledger row absent from A4 → **FAIL, return to A3** (the
forensic-notes stage that should have carried D222 to A4 alongside D108/D109).

---

## AUDIT 2 — ARITHMETIC (recompute every derived metric from raw extract numbers)

Every metric A4 itself *computed* is correct to rounding. The task-mandated recomputes:

| Metric | A4 value | My recompute (source lines) | Status |
|---|---|---|---|
| Ind AS Op EBITDA Q1FY27 | 258.47 | −30.51+187.89+127.22−26.13 = 258.47 (results L180/176/175/168) | MATCH |
| Ind AS Op EBITDA margin Q1FY27 | 61.1% | 258.47/422.69 = 61.15% | MATCH |
| Effective tax Q1FY27 / Q4FY26 / FY26 | 21.7% / 5.2% / 21.6% | 6.63/30.51; 1.24/23.90; 29.30/135.65 | MATCH |
| Revenue YoY | +36.7% | 422.69/309.29−1 = 36.66% | MATCH |
| PAT loss narrowed YoY | 35.0% | (49.96→23.88): 12.88/36.76 = 35.0% | MATCH |
| Ind AS→IGAAP PAT bridge (Step 4B) | foots to 35 | +148+116−178−18+5 = +73 pre-tax; PBT −30+73 = 43; 43−8 = 35 (deck L281/275/282/269/268/285/286) | MATCH (within deck whole-₹ rounding; non-foots already flagged F14-1) |
| "+91%" PAT growth | flagged as +84.2% GAP | 35/19 = 84.2%; base printed 18.5 (L253) AND 19 (L286); 91% needs base ~18.3 | MATCH — A4 flagged (Q2) |
| EBIT Ind AS 96-vs-97 | flagged, correct = 97 | 449−27−24−188−113 = 97 (deck L305-317); also PBT −30 + FC 127 = 97 | MATCH — A4 flagged |
| **Net P&L impact 75-vs-74** | **NOT carried** | 116+148−190 = **74** (deck prints 75, L729); Q1FY26 = 73 ties | **SOURCE VARIANCE, un-surfaced by A4 → drives coverage FAIL above** |
| Unutilised IPO — net | ₹335.42 Cr | 3,354.22M ×0.1 = 335.42 (results L239) | MATCH |
| Unutilised IPO — gross | ₹340.6 Cr | 3,405.88M ×0.1 = 340.59 (monitoring L616/458) | MATCH (see label note) |
| Deployed this quarter | ₹38.9 Cr | 389.02M ×0.1 = 38.90 (monitoring L458) | MATCH |
| Four new IPO objects | ₹187 Cr | 520+550+160+640 = 1,870M ×0.1 = 187 (monitoring L433-448) | MATCH |
| FY27 new-centre tranche | ₹186.9 Cr | 1,868.68M ×0.1 (monitoring L482-483) | MATCH |
| FY26 underspend | ₹67.2 Cr | 2,448.73−1,776.97 = 671.76M ×0.1 = 67.18 (monitoring L649-651) | MATCH |
| Paid-up share bridge | +29.41M vs 27.43M = ~1.98M | 211.99−182.58 = 29.41M face (Re.1) vs fresh issue 27,432,636 → 1.98M gap (results L195/L221) | MATCH — A4 flagged (Q12) |
| RPA occupancy | 85.97% ≈ 86% | 6.74/7.84 (deck L410-412, glossary L766) | MATCH |

**A4-computed arithmetic: no mismatch above rounding.** arithmetic_mismatches (of A4's own figures) = none.

Two minor, non-blocking notes (recorded, not FAILs):
- **Label imprecision (Q5, review L410):** ₹340.6 Cr is described as "net IPO proceeds unutilised."
  ₹340.6 Cr is the *gross*-proceeds unutilised (3,405.88M); *net*-proceeds unutilised is ₹335.42 Cr
  (3,354.22M). Both figures are individually correct and used correctly elsewhere; only the one-word
  basis label ("net") is loose. Recommend A4 relabel to "gross." Not gate-blocking.
- The deck IGAAP column carries several additional ₹1 whole-crore casting non-foots (e.g. slide 10
  EBITDA 428−342 = 86 vs printed 87; PBT build 87−11−40+8 = 44 vs printed 43), all inside the deck's
  own rounding disclaimer (L927) and immaterial. Noted for completeness only.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims; strongest bear from same text)

| # | A4's positive claim | Strongest bear counter (same extracted text) | Survives? | Already in A4? |
|---|---|---|---|---|
| 1 | IGAAP-eq PAT ₹35 Cr, +84% YoY, positive all 3 periods; "genuinely cash-profitable" anchored by current tax ₹8.16 Cr on a book loss | The ₹35 Cr sits ONLY in a management IGAAP-eq column no auditor reviewed (SRE 2410 covered only the Ind AS statement = ₹23.88 Cr LOSS); the bridge does not foot (rev adj (6) vs +5; PAT (24) vs implied (23); +91% vs +84%; base 18.5 vs 19); and the current-tax "proof" is itself printed "Q1FY27 **Estimated**" on deck slide 25 (D214, L689), not audited | YES | YES — flags, Q1, Q2, Step 1B/4B. No new graft needed |
| 2 | VAS crossed 17% green tripwire; net cash ₹66 Cr, D/E 0.05x = strong balance sheet | VAS 17% is a One-Time artifact: One-Time VAS leapt ₹7→₹39 Cr while recurring rose only ₹27→₹33 Cr (deck L619/623/617); normalise One-Time toward ₹7 Cr and VAS share falls under the 12% RED. "Net cash ₹66 Cr" is inflated by ₹340.6 Cr unspent IPO cash parked in FDs (only ₹38.9 Cr deployed), not operating generation | YES | YES — Step 6B #6, Q9, Step 8C, brief. No new graft needed |
| 3 | Revenue +37% YoY highest ever; AUM 10.61 Mn sqft +22%; occupancy 86% GREEN; operating leverage | 3.87 Mn sqft (36% of AUM) is NOT yet client-yielding — 2.77 Mn LOI "yet to be Rent Paying" + 1.1 Mn "Rent Paying yet to be Rent Yielding" (deck L408-412); occupancy is 86% only on rent-*paying* area and "90% steady-state" is >12-month mature centers only (glossary L460); growth increasingly financed by postal-ballot-redirected IPO capital, and the ₹190 Cr cash-rent outflow / FCF drag is uncheckable (no Q1 cash flow statement) | YES | YES — Step 6B #1, Q8, Q10, Step 5 INDETERMINATE, brief. No new graft needed |

**All three bear counters survive, but each is already materially incorporated in A4's review.** No
NEW surviving bear counter requires grafting into A4. Adversarial read adds no separate FAIL.

---

## VERDICT

**INCOMPLETE.**

- Gate 0 (deliverable): PASS. Coverage enumeration vs A2: clean (no A2 miss; nothing missing from
  ledger). Arithmetic of A4's own figures: clean. Adversarial read: three bear counters survive but
  all already incorporated.
- **Sole blocking defect — one orphan ledger row.** A2 deck ledger row **D222** ("Net Impact on P&L,"
  slide 25 / page 26), enumerated and explicitly flagged `ARITHMETIC_VARIANCE` (printed 75 vs correct
  116+148−190 = 74; Q1FY26 ties at 73), is **absent from A4's review**, while its identical twin (EBIT
  Ind AS 96-vs-97) IS carried in Step 1B as a NEUTRAL-FACT. Per the coverage rule, an enumerated
  ledger row not cited in A4 and not marked "reviewed, no finding" is an orphan → FAIL.

**loop_back_to: A3** — carry the D222 Net-Impact-on-P&L 75-vs-74 casting variance into the forensic
findings so A4 can incorporate it as a NEUTRAL-FACT alongside the EBIT 96-vs-97 lapse, giving the
deck's ₹1 QC lapses symmetric treatment. This is a single, cheap, tightly-scoped fix; everything else
in the review is verified complete and arithmetically sound. Re-run A5 gate 0/coverage after the graft.

(Non-blocking, fix opportunistically: relabel Q5's ₹340.6 Cr from "net" to "gross" IPO proceeds
unutilised; net unutilised is ₹335.42 Cr.)

```yaml
stage: A5-adversary
company: "INDIQUBE"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows:
    - "deck D222 (slide 25/page 26, 'Net Impact on P&L') — ARITHMETIC_VARIANCE flag (printed 75 vs recomputed 116+148-190=74; Q1FY26 ties at 73) enumerated in A2 deck ledger but not cited in A4 review, while its twin EBIT 96-vs-97 is carried in Step 1B"
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Deck 'Net Impact on P&L' Q1FY27 (Ind AS 116 impact table, slide 25)"
    a4_value: "not carried in review"
    recomputed: "74 (116 + 148 - 190); deck prints 75"
    source_line: "deck extract L721/L723/L727/L729 (D222)"
surviving_bear_counters: []   # all 3 survive but are already incorporated in A4; none require new grafting
loop_back_to: "A3"
gap: "A2-enumerated deck row D222 (Net Impact on P&L 75-vs-74 ARITHMETIC_VARIANCE) is absent from A4's review though its identical twin (EBIT Ind AS 96-vs-97) is surfaced in Step 1B; carry D222 into A3 forensic findings so A4 can add it as a NEUTRAL-FACT for symmetric completeness. Sole blocking item; all other coverage, arithmetic, and adversarial checks pass."
```
