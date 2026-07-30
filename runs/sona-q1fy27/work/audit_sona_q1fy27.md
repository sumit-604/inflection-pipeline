# A5 ADVERSARY / COMPLETENESS AUDIT — Sona BLW Precision Forgings (SONACOMS) — Q1 FY27
Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-30
Scope: FULL re-audit of the UPDATED merged review (Role 4 results + Role 5 concall). Fresh context; independent re-derivation from A1 extracts and A2 ledgers; A4/A3 cites checked, not trusted. Focus per launch: NEW Role 5 (Section B), updated Section C, updated Step 8.5, monitorables / promise-vs-delivery register. Section A (Role 4) spot-checked for drift only (it previously passed A5 COMPLETE).

Review under audit: `runs/sona-q1fy27/work/review_sona_q1fy27.md`

---

## AUDIT 1 — COVERAGE

### 1A. Fresh enumeration vs A2 concall ledger

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Speaker turns | 104 | **104** | Name-anchored grep `^(Vivek Vikram Singh\|Vikram Verma\|Sat Mohan Gupta\|Praveen Rao\|Rohit Nanda\|Pratik Sachan\|Kapil Singh\|Pramod Kumar\|Nitin Arora\|Jay Kale\|Sonal Gupta\|Moderator):` = 104 exactly. Broad grep = 108 (3 cover-letter artifacts `Date:` L16, `Subject:` L26, `Disclaimer:` L1262 correctly excluded by the ledger). | none | PASS |
| Independently-asked questions | 24 (25 rows, Q17 folded) | **24** | Sweep of analyst question-turns (7,13,18,20,24,29,33,35,40,42,44,49,51,53,58,60,62→folded,64,68,70,72,76,80,82,89). Q17 (turn 62) is a same-cluster clarification of Q16 — correctly not double-counted. | none | PASS |
| Management-stated numbers | 44 | **44** | N1-N44 (ledger Table 4) traced to cited transcript lines; all present. | none material (see 1C) | PASS |
| Entities (participants) | 14 | **14** | 12 speaking + Amit Mishra (0 turns, roll-call L90-91) + Ankit Agarwal (0 turns, L91). Cross-foots to 104 turns. | none | PASS |
| Forward/hedge statements | 15 | **15** | F1-F15 (ledger Table 5) verified at cited turns. | none | PASS |

**No row my fresh pass found is missing from the ledger. No return-to-A2.**

### 1B. Every concall A3 forensic finding incorporated (C-A3-F01..F19)

All 19 traced to a specific citation in the review body:

| Finding | Incorporated at |
|---|---|
| F01 Q2 recovery promise | Step 6A(A); Step 1 claim 17; 8.5b C1; Sec C; YAML |
| F02 robotics SOPs 1/1/1 | Step 4A Q21; 5A; 8.5b C2; Sec C |
| F03 10X ambition | Step 1 claim 10; 8.5b C8 |
| F04 JV2 SOP dodged twice | Step 2; 4A Q2/Q16; 8F N2; Sec C |
| F05 DENSO terms silent | 4C Ex1; 5B; 7A#6; 8.5 Q1; Sec C |
| F06 JV1/JV2 label inconsistency | Step 1 claim 11; 8F N5 |
| F07 forex-in-revenue silent | 4C Ex2; 5B; 7A#2; 8F N8; Sec C |
| F08 Novelic KAM silent | Step 1 claim 7; 5B; 7A#5; 8F N14; Sec C |
| F09 ROCE no number/path | Step 1 claim 25; Step 2; 5B; 7A#3; 8F N9 |
| F10 capex/CFO silent | Sec A Step 5; 5B; 7A#4; 8F N10; Sec C |
| F11 order-book haircut | Step 2; 4C Ex3; 7A#7/#9; 8F N11 |
| F12 reconciliation unresolved | Step 2; 4C Ex3; 8F N11 |
| F13 debtor-days silent | Sec A Step 5; 5B; 7A#12 |
| F14 railway P&L / Head 0 turns | 0B; 5B; 7A#11; 8A; 8F N12 |
| F15 refuses EV inflection | 4A Q7; 7A#8; 8F N6 |
| F16 robotics ramp "don't know" | Step 2; 4A Q25; 8A; 8F N7 |
| F17 margin may worsen | Step 1 diag; 4C Ex2; 6A(A); Sec C; YAML |
| F18 customer concentration % | 4A; 5B; 7A#10; 8F N13 |
| F19 governance not raised | 8.5 Q10; 5B; 7A#14; Sec C |

**All 19 incorporated. No orphan forensic. No return-to-A3.**

### 1C. Non-blocking coverage observations (not FAILs)
- Two pure-color numbers — N30/N31 (lines-of-code 2m/>1m/5m) and N40 (Denso-vs-Sona brand ~100:1) — are folded as NEUTRAL-FACT into the Q1 AI-discussion / competitive-color narrative rather than separately cited. Compliant with the review's stated NEUTRAL-FACT folding rule (preamble L26). Reviewed-no-finding, acceptable.
- The ledger's "entities" category is participant-scoped (14). External entities named on the call (DENSO, Nomura, Morgan Stanley, S&P Global, Boston Dynamics, Hyundai, Bosch, Maebara-san) are not separately enumerated, but the thesis-material ones (DENSO throughout; Nomura as host firm) are substantively handled. Internally consistent scope; not an orphan.
- Prior orphan **PR-FD4** (stale "April 30, 2026" press-release dateline) is now grafted into Step 8.5 Q10 "From findings" and Section C — confirmed closed.

**Coverage verdict: PASS.**

---

## AUDIT 2 — ARITHMETIC

### 2A. Role 4 (Section A) figures — re-derived independently; confirm UNCHANGED (no drift)

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q1FY27 | 302.60 | 240.94 + 76.88 + 10.48 − 25.70 = **302.60** | C481/478/477/471 | ✓ |
| Op EBITDA margin Q1FY27 | 23.26% | 302.60 / 1301.20 = **23.26%** | C469 | ✓ |
| Op EBITDA YoY | +49.40% | 302.60 / 202.55 − 1 = **+49.4%** | — | ✓ |
| Net-forex swing YoY | +12.18 | 9.17 − (−3.01) = **+12.18** | C470 | ✓ |
| Core PBT ex-OI YoY | +65.28% | 215.24 / 130.22 − 1 = **+65.3%** | C481/471 | ✓ |
| Core PBT ex-OI **ex-forex** YoY | +54.67% | 206.08 / 133.24 − 1 = **+54.67%** (~+55%) | — | ✓ |
| S-vs-C PAT gap Q1FY27 | +18.90% | (220.11 − 178.51)/220.11 = **18.90%** | SA202/C490 | ✓ |
| Standalone ETR Q1FY27 | 20.14% | 55.52 / 275.62 = **20.14%** | SA200/194 | ✓ |
| Consolidated ETR Q1FY27 | 25.91% | 62.43 / 240.94 = **25.91%** | C488/483 | ✓ |
| Owners PAT YoY | +44.71% | 180.47 / 124.71 − 1 = **+44.7%** | C506 | ✓ |

Section A re-derives cleanly. **No drift; the preserved Role-4 block is arithmetically intact.**

### 2B. NEW concall-derived numbers — re-checked against filing/deck

| Metric | Call / A4 handling | My recompute | Source | Status |
|---|---|---|---|---|
| EBITDA "303 cr, +49%" | ties to Op EBITDA 302.60 | 302.60 ≈ 303; 23.1% = 302.60/1310.37 = **23.09%** | l.572 | ✓ CONFIRMED |
| PAT "181 cr, +45%" | owners 180.47→181 | 180.47/124.71 = **+44.7%**; A4 correctly notes owners basis (total PAT 178.51) | l.577/C506 | ✓ |
| PAT margin "13.6%" | management basis | 178.51/1310.37 = **13.62%**; A4 does not restate as its own metric | l.577 | ✓ consistent |
| Revenue "12,310 crore" | flagged units artifact | 12,310/1,310 ≈ 9.4x artifact; +54% ties to incl-forex 1,310.37/850.90 = **+54.0%** (ex-forex +52.4%) | l.564/C469-470 | ✓ correctly flagged (C-A3-F07) |
| BEV "436 cr, +107%" | — | 436/2.07 ≈ 210 prior → "more than doubled" | l.565 | ✓ |
| Order book 24,000 Cr, EV 64% | — | 24,000 × 0.64 = 15,360 ≈ deck 15,400 | l.499 | ✓ |
| Robotics book 800 Cr = 3% | — | 800/24,000 = 3.33% → "3%" | l.499-501 | ✓ |
| Robotics +600 → 800 Cr | — | implies 200 Cr prior book; consistent | l.360-364 | ✓ |
| Consumption 32x / 8-yr life | A4 flags UNRECONCILED | 1,300 × 32 = 41,600 ≠ 24,000 book — A4 labels "direction not reconciliation" (C-A3-F11/F12); not adopted as A4's own metric | l.1195-1197 | ✓ correctly flagged, not an A4 error |

No A4 arithmetic error found. Every derived figure recomputes within rounding; the two internally-inconsistent management numbers (the "12,310" units artifact; the 32x consumption that does not tie to the book) are correctly flagged BY A4 as management artifacts, not propagated as A4 conclusions.

**Arithmetic verdict: PASS. No mismatch above rounding.**

---

## AUDIT 3 — ADVERSARIAL READ (strongest same-transcript bear counter to each most-positive concall claim)

**Claim 1 — "Cost-recovery measures will become progressively more visible from Q2 onwards" (l.455-456) → margin recovery is coming.**
- Strongest same-transcript counter: management simultaneously pre-warns pass-through lag "may continue to create some pressure on margin" (l.419-421); costs "always lag inflation... come a little later" (l.418-419); and the mix drag is not one-off — traction motors (the "lowest margin" category) "grew quite rapidly" (l.457-460) and remain the 2nd-fastest-growing product (l.1173). 23.1% may not be the trough.
- Survives? **YES as a signal — already GRAFTED** (Step 1 diagnostic "central credibility fault-line"; 4C Exchange 2; 6A(A); 8F N1; Section C; C-A3-F17 vs C-A3-F01). No further graft required.

**Claim 2 — "Best quarter from an operational cash-flow perspective" + "significant reduction in debtor days" (l.596-598).**
- Strongest same-transcript counter: both are fully unquantified; Q1 carries no cash-flow statement / balance sheet (Reg 33), so there is no CFO and no debtor-days figure behind them. A superlative resting on an undisclosed number.
- Survives? **YES — already GRAFTED** (Sec A Step 5 update; 5A; 7A row; Section C; YAML: INDETERMINATE cash cap NOT lifted; C-A3-F10/F13). No further graft required.

**Claim 3 — Robotics + DENSO optionality ("Sona Comstar 2.0", build another 10X, robotics SOPs 1/1/1, DENSO "killer combo").**
- Strongest same-transcript counter: the DENSO deal requires slump-selling the existing 100% in-house EV-motors subsidiary (partial divestment of a core EV asset) with EVERY financial term silent on the call; JV2 revenue timeline dodged twice on confidentiality (l.707-711, l.1068-1070); robotics revenue-conversion timeline conceded unknown ("I don't think I know", l.1209); robotics is 3% of the order book; in JV1 (high-voltage) Sona cedes majority/management to DENSO by design.
- Survives? **YES — already GRAFTED** (4C Exchange 1; 8A trigger "NEW/AMBIGUOUS"; 5B RED silences; Section C; 8F N2/N3/N7; C-A3-F04/F05/F16). No further graft required.

### 3A. Additional bear signal tested (secondary, not among the three named positives)
Positive framing "we are not constrained by demand... we have enough and more capacity" (l.816-826). Same-transcript counter: Vivek concedes "we are able to sell **less than we ideally would have**" due to **other players'** supply-chain bottlenecks (l.833-835) — a throughput/realisation risk on the revenue line, only lightly reflected (Step 2 "capacity ahead of markets", LOW confidence). This counters a secondary "healthy demand / best-ever revenue" claim, not one of the three thesis-load-bearing positives, and the review already frames revenue as real-but-FX-flattered-and-part-inorganic. **Non-blocking optional enhancement** (A4 could add one clause to Step 2 / Section C noting sales were capped by third-party supply-chain bottlenecks). Not required for COMPLETE.

**Adversarial verdict: no surviving un-grafted bear counter to any of the three most-positive concall claims. PASS.**

---

## VERDICT

**COMPLETE.**

- Coverage: 104 turns / 24 questions / 44 numbers / 14 entities / 15 fwd-hedge all reconcile to my fresh pass; all 19 concall forensics (C-A3-F01..F19) incorporated; prior PR-FD4 orphan confirmed closed. No return-to-A2, no return-to-A3.
- Arithmetic: Section A re-derives with no drift; all NEW concall-derived figures recompute within rounding; the two internally-inconsistent management numbers are correctly flagged by A4 rather than propagated. No return-to-A4.
- Adversarial: bear counters to all three named most-positive concall claims (Q2 margin recovery, best-ever cash flow, robotics/DENSO optionality) are already grafted into Sections B and C. One minor secondary counter (sales capped by third-party supply-chain bottlenecks, l.833-835) is a non-blocking optional enhancement.

Only COMPLETE proceeds to Notion save. This review may proceed.

```yaml
stage: A5-adversary
company: "SONACOMS"
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
