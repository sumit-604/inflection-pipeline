# A5 ADVERSARY / COMPLETENESS AUDIT — GHVINFRA Q1 FY27
# Model: Opus 4.8 | Fresh context: A4 review + A1 extract + A2 ledger only.
# Re-derived independently; A4/A3 cites checked, not deferred to.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF exists at review L560-658. All four labelled parts
present and carrying real content (not placeholders):

| Brief part | Heading location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | L562-589 ("## 1. SUMMARY NARRATIVE") | PRESENT | ~24 lines of plain prose; numbers + thesis + verdict. Non-empty. |
| (2) SECTOR intelligence | L591-613 ("## 2. SECTOR INTELLIGENCE") | PRESENT | 4 bullets, provenance-tagged (Notion vs filing). Non-empty. |
| (3) BUSINESS-MODEL intelligence | L615-637 ("## 3. BUSINESS-MODEL INTELLIGENCE") | PRESENT | 4 bullets, unit economics + model-drift. Non-empty. |
| (4) COMPETITION intelligence | L639-658 ("## 4. COMPETITION INTELLIGENCE") | PRESENT | 3 bullets, peer contrast + competitive risk. Non-empty. |

Gate 0: **PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep pass diffed against A2 ledger)

Independent re-enumeration of the 182-line A1 extract. Non-disclosure artifacts
(header L1-13, page markers L15/70/124, logo/tagline repeats) excluded, matching
A2 method note.

| Category | A2 count | My fresh count | Basis (my grep/read) | Orphan rows | Status |
|---|---|---|---|---|---|
| line_items (P&L table) | 5 | 5 | L94-98 (Rev/EBITDA/EBITDA%/PAT/PAT%) | none | MATCH |
| narrative_financial_metrics | 2 | 2 | PBT L86-87/110-111; Diluted EPS L112 | none | MATCH |
| headline_bullets | 3 | 3 | L84-85, L86-87, L88-91 | none | MATCH |
| narrative_paragraphs | 12 | 12 | F1-F12 (L78, 80-82, 99-106, 108-112, 114-122, 131-132, 147-151, 153-154, 156-160, 162, 164-165, 179-182) | none | MATCH |
| director_appointments | 3 | 3 | L134-145 (Aggarwal/Tawade/Dasgupta) | none | MATCH |
| business_verticals | 6 | 6 | L167-177 (6 colon-labelled) | none | MATCH |
| letter_metadata | 11 | 11 | A1-A11 (L17-20…66-68) | none | MATCH |
| signature_block | 2 | 2 | L51-56, L58-59 | none | MATCH |
| absence_flags | 15 | 15 | I1-I15 | none | MATCH |
| zero_standing | 0 | 0 | no nil/dash rows in table | n/a | MATCH |
| notes | 0 | 0 | no numbered notes (doctype) | n/a | MATCH |
| agenda_items | 0 | 0 | no Board Outcome letter | n/a | MATCH |
| auditor_paras | 0 | 0 | "Auditor"/"Limited Review" 0 hits | n/a | MATCH |
| entities | 0 | 0 | no subsidiary/consolidation list | n/a | MATCH |
| **TOTAL positive-count** | **59** | **59** | 11+2+5+2+3+12+3+6+15 | none | MATCH |

**Ledger-vs-A4 orphan check.** A4's reconciliation preamble (L14-27) accounts for
all 59 rows and asserts "All 59 ledger rows reviewed." Spot-verified that each
category surfaces in the review body: P&L 5 rows (Step 1, L128-148); PBT/EPS
(Step 1); bullets (Step 2); paragraphs incl. MD quote L114-122 (sector/business
model); directors L131-145 (Step 6B/6D, QFM Q5); verticals L167-177
(sector/business/competition); letter metadata date-discrepancy + name-change
(QFM Q6, governance-hygiene); signature block CS Daksh Mewada L58-59 (Step 6B
watchlist #4); absence flags I1-I15 collectively acknowledged (L40-45, L536) and
individually cited I1/I2/I4/I5/I7/I8/I10/I13/I14/I15.
Absence flags I3, I6, I9, I11, I12 are covered by the blanket "I1-I15 reviewed,
confirmed-absent" statement plus content coverage (notes Step 0D; segment L604;
DIN/dates QFM Q5). I9 (board-meeting start/end time) is covered only collectively,
which is acceptable for a confirmed-absent unit — not an orphan.

**Rows my fresh pass found that the ledger lacks:** none.
**Orphan rows (ledger present, A4 absent):** none.

Coverage: **PASS.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from A1 raw lines)

Raw inputs (A1): Rev 218.59/80.46 (L94); EBITDA 28.05/8.35 (L95); PAT 11.25/4.72
(L97); PBT 15.53/6.32 (L86-87,110-111); Diluted EPS 1.48 (L112).

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Revenue YoY % | +171.67% | (218.59-80.46)/80.46 = 171.68% | L94 | MATCH (0.01pp rounding; A4 uses printed) |
| EBITDA YoY % | +235.93% | 19.70/8.35 = 235.93% | L95 | MATCH |
| EBITDA margin Δ | +245 bps | 12.83-10.38 = 2.45pp | L96 | MATCH |
| PAT YoY % | +138.35% | 6.53/4.72 = 138.35% | L97 | MATCH |
| PAT margin Δ | -71 bps | 5.15-5.86 = -0.71pp | L98 | MATCH |
| PBT YoY % | +145.73% | 9.21/6.32 = 145.73% | L86,111 | MATCH |
| EBITDA→PBT gap Rs (FY26) | 2.03 | 8.35-6.32 = 2.03 | L95,111 | MATCH |
| EBITDA→PBT gap Rs (FY27) | 12.52 | 28.05-15.53 = 12.52 | L95,86 | MATCH |
| Gap % of rev (FY26) | 2.52% | 2.03/80.46 = 2.52% | derived | MATCH |
| Gap % of rev (FY27) | 5.73% | 12.52/218.59 = 5.73% | derived | MATCH |
| Gap Δ | +321 bps | 5.73-2.52 = 3.21pp | derived | MATCH |
| PBT margin (FY26) | 7.85% | 6.32/80.46 = 7.85% | derived | MATCH |
| PBT margin (FY27) | 7.10% | 15.53/218.59 = 7.10% | derived | MATCH |
| Implied ETR (FY26) | 25.32% | (6.32-4.72)/6.32 = 25.32% | derived | MATCH |
| Implied ETR (FY27) | 27.56% | (15.53-11.25)/15.53 = 27.56% | derived | MATCH |
| ETR Δ | +2.24pp | 27.56-25.32 = 2.24pp | derived | MATCH |
| PAT margin (FY26) recompute | 5.87% | 4.72/80.46 = 5.87% | L98 | MATCH (A4 flags 0.01pp vs printed 5.86%) |
| PAT margin (FY27) | 5.15% | 11.25/218.59 = 5.15% | L97,94 | MATCH |
| Implied diluted share count | ~7.6 Cr | 11.25/1.48 = 7.60 Cr | L97,112 | MATCH (A4 flags unverifiable) |
| PAT YoY Rs change | +6.53 | 11.25-4.72 = 6.53 | L97 | MATCH |
| PBT YoY Rs change | +9.21 | 15.53-6.32 = 9.21 | L86,111 | MATCH |
| EBITDA→PBT charge growth Rs | +10.49 | 12.52-2.03 = 10.49 | derived | MATCH |

Operating EBITDA / core-PBT / cash metrics: A4 correctly returns **ND** (Other
Income, Depreciation, Finance Cost, CFO all undisclosed) rather than estimating —
compliant with CLAUDE.md "never estimate a missing number."

Arithmetic: **PASS. No mismatch above rounding.**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, bear counter from same text)

**Claim 1 — Revenue +171.67% YoY to Rs 218.59 Cr (headline L80-85).**
Strongest bear from the same extract: the base is a Rs 80.46 Cr quarter on a
sub-3-year, reverse-merger vehicle (formerly Sindu Valley, L20); the filing
discloses **no order book / customer mix** (A2 I14), so the growth cannot be shown
to be arm's-length rather than parent-fed. **Counter survives? No — already grafted:**
Step 2 diagnostic 1 (L204-209), growth-trigger table (L372), competition brief
(L652-658). No new incorporation required.

**Claim 2 — Reported EBITDA margin expanded +245 bps to 12.83% (L96, L108-109).**
Strongest bear: this is REPORTED EBITDA which may embed Other Income; Operating
EBITDA (ex-OI) is ND because Other Income / Depreciation / Finance Cost are all
undisclosed, so the "margin expansion" is unverifiable and un-cleanable.
**Counter survives? No — already grafted:** Step 2 diagnostics 2 and 6 (L212-214,
L239-242), Step 1 note (L172-176). No new incorporation required.

**Claim 3 — PAT surged +138.35% / "more than doubled" to Rs 11.25 Cr (L84, L103).**
Strongest bear: PAT **margin CONTRACTED -71 bps** (5.86%→5.15%, L98) because
below-EBITDA charges rose +321 bps of revenue and implied ETR rose to 27.56%
(above the 25.17% statutory reference); the depreciation-vs-finance-cost split is
withheld, so a leverage-funded read cannot be excluded (corroborates the FY25 CFO
-Rs 55.63 Cr AVOID driver). **Counter survives? No — already grafted:** Step 2
diagnostic 4 (L220-230), Step 4 bridge (L260-290), Combined Verdict (L511-516),
summary narrative (L569-576). No new incorporation required.

Additional positive claims checked (governance: 3 new Independent Directors L131;
RAHSTA award L153-154): bear counters (no DINs/dates, Dasgupta lender-independence
caveat, AGM ratification pending; award self-reported/non-catalyst) are already
incorporated at Step 6B/6D, QFM Q5, and the monitorables list.

**Surviving bear counters requiring graft into A4: NONE.**

---

## VERDICT

**COMPLETE.** Gate 0 passes (all four brief parts present, non-empty). Coverage:
fresh enumeration reproduces all 59 A2 positive-count rows exactly; zero orphan
rows, zero rows missing from the ledger. Arithmetic: all 22 derived metrics
recompute within rounding; no discrepancy. Adversarial read: the three (plus two)
most-positive claims each already carry their strongest same-text bear counter in
A4; nothing survives un-incorporated. No loop-back required.

```yaml
stage: A5-adversary
company: "GHVINFRA"
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
