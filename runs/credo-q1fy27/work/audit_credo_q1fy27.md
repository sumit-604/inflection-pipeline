# A5 ADVERSARY / COMPLETENESS AUDIT — Credo Brands Marketing Ltd (CREDO / NSE:MUFTI) — Q1 FY27

Auditor: A5 (Opus 4.8). Fresh context: A4 review + A1 extracts + A2 ledgers only. All
figures below independently re-derived from the raw extracts; A4/A3 cites checked, not
trusted. Unit rule applied: results filing is Millions ×0.1 → Rs Cr; presentation and
media release are Crores ×1.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The PLAIN-LANGUAGE BRIEF (A4 lines 374-386) carries all four labelled parts, each with
real, non-placeholder content:

| Part | Heading present | Location | Content check | Status |
|---|---|---|---|---|
| 1. Summary narrative | yes | L376-377 | Dense multi-clause narrative: revenue +4.4%, EBITDA -14%, PAT -64%, marketing driver, tax tell, WC, net cash, basis mismatch, WATCHLIST framing, PWC cap. Substantive. | PRESENT |
| 2. Sector intelligence | yes | L379-380 | Men's mid-premium-to-premium casual wear; discretionary softness; Labour Codes as cross-sector cost input; named provenance + disclosure gap. | PRESENT |
| 3. Business-model intelligence | yes | L382-383 | Asset-light design-led outsourced model; channel mix; unit economics; deliberate WC-risk retention; three model-drift items. | PRESENT |
| 4. Competition intelligence | yes | L385-386 | Wins/weaknesses framed; peer-benchmark gap named; cleanest competitive tell. | PRESENT |

GATE 0 = PASS. All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep re-enumeration diffed against each A2 ledger)

Independent grep pass (my own):
- Results extract numbered notes 1-8 confirmed (note 1 leading digit OCR-dropped, anchor "were reviewed by the Audit Committee" at L203; notes 2-8 at L206/210/213/216/225/228/230). Count = 8.
- Presentation `^\[page ` = 38. Media `^\[page ` = 4. Confirmed.
- Presentation "On Consolidated Basis" = 3 (slides 35/36/37) → BASIS_MISMATCH footnotes FN-16/17/18. Confirmed.
- Presentation borrowings `0.0` at L861 and L873 (2 zero cells) → ZERO_STANDING ZS-01/02. Confirmed.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — numbered notes | 8 | 8 | none — all 8 in A4 Step 0D table (L44-53) | PASS |
| Results — P&L line items | 34 | 34 | none — reproduced in A4 Step 1 (L68-94) | PASS |
| Results — ZERO_STANDING | 4 | 4 (Exceptional, Current tax Q1FY27 blank, Excess-provision, Other Equity) | none — all 4 cited (A4 L82/84/85/91, L96) | PASS |
| Results — auditor paras | 9 | 9 (P1-P4 present, P5-P7 absent, P8 entity, P9 sig/UDIN) | none — A4 L55 cites clean para 4 + confirms P5-P7 absent + entity | PASS |
| Results — entities | 1 | 1 (standalone-only, Note 7) | none — A4 L52, S-vs-C section | PASS |
| Results cover-letter — agenda items | 10 | 10 (A1 present = results approval; A2-A10 NOT DISCLOSED) | A1 covered (Step 0 approval); A2-A10 not itemised in A4 preamble — see NOTE below | PASS (see note) |
| Board-outcome (AGM) — agenda items | 13 | 13 (6 present / 7 ZERO_STANDING) | none — AGM/dividend/AR/directors/auditor/scrutinizer/ESOP/capital-raising all surfaced (A4 Q15-Q17, Monitorables 1-3) | PASS |
| Presentation — slides / slide-numbers | 38 / 38 | 38 / 38 | none | PASS |
| Presentation — numbers (line items) | 863 | 863 (spot-reconciled: P&L slide 9, historicals 35-37, WC/return slide 31) | none material | PASS |
| Presentation — footnotes | 18 | 18 (incl. 3 BASIS_MISMATCH, MGMT_ESTIMATE MBO, TTM/as-of) | none — BASIS_MISMATCH + MGMT_ESTIMATE both surfaced (A4 S-vs-C, Q7) | PASS |
| Presentation — ZERO_STANDING | 4 | 4 (Borrowings NC, Borrowings C, Current-tax-liab dash, Exceptional) | none — net-cash/zero-debt + Exceptional cited (A4 L214, L237) | PASS |
| Media — 78 rows (10 sub-categories) | 78 | 78 (4 pages / 6 P&L / 15 op / 1 quote / 11 quote-nums / 4 fwd / 10 bullets / 3 tiles / 5 fn / 19 admin) | none — Outerwear (1%) FF-09→Q8, store net-2 FF-11→Q9, WC 176 FF-08, D2C FF-03 all surfaced | PASS |

**COVERAGE NOTE (non-fatal discrepancy, named for A4):** A4's ledger-reconciliation
preamble (L11-16) enumerates the results filing as "8 notes / 34 line-items / 9 auditor
paras / 1 entity" but OMITS the results ledger's own `agenda_items: 10` category (the
results-approval cover letter, ledger_results section 2). Substantively this is harmless:
row A1 (approval of the unaudited results) is covered in A4 Step 0 preamble and Note 1;
rows A2-A10 are NOT-DISCLOSED Reg-30 checklist nulls that are fully duplicated and
reconciled by the separate board-outcome (AGM) ledger's 13-item checklist, which A4 does
address (Q15-Q17, Monitorables 1-3). No substantive disclosure is orphaned, so this is
recorded as a preamble-labelling omission, not a coverage FAIL. Recommend A4 add one line
acknowledging the results-cover-letter agenda category for a clean reconciliation.

No row surfaced by my fresh pass is missing from the ledgers (missing_from_ledger = none).
GATE 1 = PASS.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extracted numbers)

Raw check first: all 34 filing line items convert cleanly Millions ×0.1 → Rs Cr and match
A4's Step 1 table to the cent (Revenue 1,252.69M→125.27; PAT 22.85M→2.29; PBT 31.43M→3.14;
Total tax 8.58M→0.86; Depreciation 192.36M→19.24; Other Income 20.95M→2.10). Cross-basis
tie-out to deck (125.3 / 26.6 / 2.3) holds. No conversion error.

| Metric | A4 value | My recompute | Source line (raw) | Status |
|---|---|---|---|---|
| Operating EBITDA Q1FY27 (PBT+D+Fin−OI) | 26.57 | 3.14+19.24+6.29−2.10 = 26.57 | filing L153/150/149/142 | MATCH |
| Operating EBITDA Q1FY26 | 31.05 | 8.24+18.23+6.20−1.62 = 31.05 | filing | MATCH |
| Operating EBITDA Q4FY26 | 41.51 | 20.61+18.78+6.34−4.22 = 41.51 | filing | MATCH |
| Operating EBITDA FY26 (on PBT-pre-exc 65.20) | 154.19 | 65.20+74.37+25.47−10.85 = 154.19 (ties deck 154.2) | filing/deck L839 | MATCH |
| Op EBITDA Margin Q1FY27 | 21.21% | 26.57/125.27 = 21.21% | — | MATCH |
| Op EBITDA Margin Q1FY26 | 25.89% | 31.05/119.94 = 25.89% | — | MATCH |
| Core PBT ex-OI Q1FY27 | 1.04 | 3.14−2.10 = 1.04 | filing | MATCH |
| Core PBT ex-OI Q1FY26 | 6.62 | 8.24−1.62 = 6.62 | filing | MATCH |
| Other Income / PBT Q1FY27 | 66.9% | 2.10/3.14 = 66.9% | filing | MATCH |
| Effective Tax Rate Q1FY27 | 27.3% | 0.858/3.143 = 27.30% | filing L161/155 | MATCH |
| ETR Q1FY26 | 23.5% | 1.932/8.235 = 23.5% | filing | MATCH (rounding) |
| ETR vs statutory spread | +213 bps vs 25.17% | 27.30−25.17 = 2.13pp = 213 bps | — | MATCH |
| PAT Margin Q1FY27 | 1.83% | 2.29/125.27 = 1.83% | filing | MATCH |
| Revenue YoY | +4.44% | (125.27−119.94)/119.94 = +4.44% | filing | MATCH |
| Op EBITDA YoY | −14.43% | −4.48/31.05 = −14.43% | filing | MATCH |
| Op EBITDA margin YoY | −468 bps | 21.21−25.89 = −4.68pp | — | MATCH |
| EBIT operating (ex-OI) YoY | −42.8% | (7.33−12.82)/12.82 = −42.8% | filing | MATCH |
| Core PBT ex-OI YoY | −84.3% | (1.04−6.62)/6.62 = −84.3% | filing | MATCH |
| Reported PBT YoY | −61.9% | (3.14−8.24)/8.24 = −61.9% | filing | MATCH |
| PAT YoY | −63.7% | (2.29−6.30)/6.30 = −63.65% | filing | MATCH |
| EPS YoY | −63.9% | (0.35−0.97)/0.97 = −63.9% | filing L177 | MATCH |
| Gross Profit Q1FY27 | 77.18 (77.2) | 125.27−(5.17+61.87−18.95) = 77.18 | filing L141/145/146/147 | MATCH (deck 77.2) |
| Gross Margin Q1FY27 | 61.61% | 77.18/125.27 = 61.61% | — | MATCH |
| Employee cost YoY | +12.4% | (9.43−8.39)/8.39 = +12.4% | filing L148 | MATCH |
| Other Expenses YoY | +19.8% | (41.18−34.37)/34.37 = +19.8% | filing L151 | MATCH |
| Marketing delta | +5.3 (10.7 vs 5.4) | 10.7−5.4 = 5.3; 10.7/125.27 = 8.5% | deck L242-243 | MATCH |
| PAT bridge close | −4.03 ≈ −4.01 | GP+3.38 −emp1.04 −oth6.81 +OI0.48 −dep1.01 −fin0.09 +tax1.07 = −4.02 | filing | MATCH (rounding, A4 flags it) |
| CFO/PAT FY26 (annual, deck) | 2.79x | 132.4/47.42 = 2.79x | deck L908/848 | MATCH |
| CFO YoY (deck) | −16.7% | (132.4−159.0)/159.0 = −16.7% | deck L908 | MATCH |
| Net cash ex-lease Mar-26 | ~72.6 | 52.4+20.2 = 72.6, borrowings 0.0/0.0 | deck L878/880/861/873 | MATCH |
| Net debt incl leases Mar-26 | ~155.6 | 228.2−72.6; leases 46.2+182.0 = 228.2 | deck L863/875 | MATCH |
| Deck EBIT −34% | −34% | (9.5−14.4)/14.4 = −34.0% | deck L246 | MATCH |
| Q2+Q3 FY26 combined (derived) | 309.86 | 592.10−119.94−162.30 = 309.86 | filing | MATCH |

Every derived metric recomputes within rounding. **Zero arithmetic mismatches.** The
one FY26-column ratio worth noting (Other Income/PBT = 17.0%) uses reported PBT 63.80
(10.85/63.80 = 17.0%), internally consistent with A4's stated formula; not a mismatch.
Media-release rounding (revenue "+5%" vs +4.4%; margin "−460 bps" vs −468 bps; GM "10 bps"
vs +8 bps) is a source overstatement, correctly flagged by A4, not an A4 error.
GATE 2 = PASS.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to A4's three most positive claims)

A4 is already a bear-heavy review, so its genuinely POSITIVE assertions are few. The three
most positive, each stress-tested from the same extracted text:

**Positive claim 1 (A4 L214/221, brief L377): "genuinely deleveraged balance sheet — zero
interest-bearing debt and ~Rs 73 Cr net cash ex-leases," called "a genuine positive."**
Bear counter (same extract): the Rs 72.6 Cr net-cash figure is a **Mar-26** balance-sheet
value (deck slide 36); no Jun-26 balance sheet was filed (Reg 33, Q1), so the "positive" is
one quarter stale and pre-dates the marketing-heavy Q1FY27. On a lease-inclusive basis
(lease liabilities 46.2 + 182.0 = 228.2, L863/875) the entity is net **debt ~Rs 155.6 Cr**,
not net cash; and trade receivables 236.3 + inventories 110.4 (L872/876) tie up working
capital many times the cash cushion, with debtor days rising 66→147.
Survives? **Already incorporated** — A4 states the lease-inclusive net debt (155.6), the
Jun-26 ND caveat, and the structural WC drag. Does NOT need grafting; the one refinement is
that the plain-brief sentence "genuine positive" should carry the Mar-26-staleness tag A4
uses elsewhere. Minor, non-blocking.

**Positive claim 2 (A4 L55, Step 0D): "auditor UNMODIFIED / CLEAN... audit surface is quiet."**
Bear counter (same extract, auditor para 3, L86-93): the conclusion is a **limited review
under SRE 2410**, which the auditor itself states "is substantially less in scope than an
audit... and consequently does not enable us to obtain assurance that we would become aware
of all significant matters." Para 4 is negative assurance ("nothing has come to our
attention"), not a clean audit opinion. Combined with Note 3 (Q4FY26 = unreviewed balancing
figures) and the unexplained deferred-tax charge with blank current tax, "quiet audit
surface" slightly overstates the comfort.
Survives? **Partially** — A4 does label it a "limited review" and flags Q4-balancing and the
tax sign-flip, but does not foreground the negative-assurance limitation. This is boilerplate
that every limited review carries and is not thesis-changing; recommended one-line graft
("negative assurance, limited-review scope"), non-blocking.

**Positive claim 3 (A4 L187, Step 4): "Nothing one-off is flattering or masking the number —
it is a clean operating-deleverage quarter."**
Bear counter (same extract): reported PAT of Rs 2.29 Cr is in fact cushioned versus the true
operating run-rate by two below-the-line items A4 itself quantifies — a **+Rs 1.07 Cr YoY tax
tailwind** (tax 1.93→0.86 despite a HIGHER 27.3% ETR, driven entirely by a non-cash deferred
CHARGE with blank current tax) and **+Rs 0.48 Cr Other Income** now funding 66.9% of PBT.
Strip both and core PBT is Rs 1.04 Cr (−84.3%); on cash-tax normalisation PAT would be lower.
So the −63.7% headline UNDERSTATES the operating deterioration.
Survives? **Already incorporated in substance** — A4 states the OI cushion, the tax tailwind,
and core PBT −84.3% prominently (L135-136, L182, L188) and flags them. A4's L187 sentence is
specifically about *one-off* items (there is no one-time gain), which is defensible; the
cushioning by OI/tax is recurring-ish, not a one-off, and is fully disclosed. No new bear
content is missing. Non-blocking; recommend A4 soften L187 wording so it does not read as
contradicting its own core-vs-reported analysis.

**Result:** no surviving bear counter introduces material bear content ABSENT from A4. All
three are either already incorporated (1, 3) or reduce to non-thesis-changing boilerplate (2).
Two light wording grafts recommended (brief net-cash staleness tag; L187 softening) but none
rises to a completeness FAIL that blocks save.

---

## VERDICT

**COMPLETE.**

- GATE 0 (deliverable): PASS — all four plain-language-brief parts present and substantive.
- GATE 1 (coverage): PASS — every ledger row across all four ledgers is cited or reviewed;
  one non-fatal preamble-labelling omission named (results-cover-letter `agenda_items:10`
  category absent from A4's reconciliation preamble though A1 is covered and A2-A10 are null
  duplicates of the reconciled board-outcome checklist). No substantive orphan.
- GATE 2 (arithmetic): PASS — every derived metric recomputes within rounding from the raw
  Millions×0.1 filing and Crores×1 deck/media; zero mismatches; PAT −63% / EBITDA −14% /
  revenue +4.4% walk and the Rs-Crore conversions are internally consistent; ETR 27.3% vs
  25.17% statutory spread (+213 bps) confirmed.
- GATE 3 (adversarial): PASS — no surviving bear counter adds material bear content missing
  from A4; two optional light wording grafts recommended, non-blocking.

Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "CREDO"
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
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
