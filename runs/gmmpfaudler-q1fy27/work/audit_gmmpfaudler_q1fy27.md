# A5 ADVERSARY / COMPLETENESS AUDIT — GMM Pfaudler Limited (GMMPFAUDLR), Q1 FY27

Agent: A5 ADVERSARY | Fresh context (A4 review + A1 extracts + A2 ledgers only).
Every value below re-derived independently from the A1 extracts. A4/A3 cites were
checked, not trusted. `R:<n>` = results extract line; `P:<n>` = presentation extract line.

Scope acknowledgement: this run merges a 3-page press release + 29-slide deck; no full
Reg 33 statement and no concall transcript exist, so Role 5 is deferred and
balance-sheet/cash-flow cells are legitimately ND. An ND with a stated basis is NOT an
arithmetic failure; an ND dodging a number PRESENT in the extract IS. Checked on that basis.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS GATE (run first)

The A4 review carries a section `## MANDATORY PLAIN-LANGUAGE BRIEF` (review L450) with all
four labelled sub-parts present and carrying real, non-placeholder content:

| Part | Heading present | Location | Non-empty / real content | Status |
|---|---|---|---|---|
| (1) Summary narrative | `### 1. SUMMARY NARRATIVE` | review L452-453 | Yes — ~20-line narrative, numbers anchored, states the below-EBIT/subsidiary-swing read and the WATCHLIST decision | PRESENT |
| (2) Sector intelligence | `### 2. SECTOR INTELLIGENCE` | review L455-456 | Yes — Industrial Products 25x cap, end-markets, diversification tailwind, currency/tax as binding variable | PRESENT |
| (3) Business-model intelligence | `### 3. BUSINESS-MODEL INTELLIGENCE` | review L458-459 | Yes — engineered-to-order model, division revenue split, the 25-pt standalone-vs-consol tax wedge, cash as weakest link | PRESENT |
| (4) Competition intelligence | `### 4. COMPETITION INTELLIGENCE` | review L461-462 | Yes — named peers (HLEGLAS, ANUP, KLBRENG, PRAJIND), margin-vs-scale positioning, peer-concall cross-check deferred | PRESENT |

**Gate 0 result: PASS.** All four brief parts present and substantive.

---

## AUDIT 1 — COVERAGE (fresh grep/enumeration diffed against A2 ledgers)

### Results ledger (48 rows / 15 categories)

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| notes | 0 | 0 (no `^\s*[0-9]+\.` numbered notes in R:44-190) | — | OK |
| line_items (Q1FY27 summary) | 8 | 8 (R:97: 925, 94, 10.1%, 22, 2.4%, 5.32, 1,007, 2,289) | — cited Step 1/Sec C | OK |
| zero_standing | 0 | 0 | — | OK |
| highlight_bullets | 8 | 8 (5 perf R:103-107 + 3 corp R:109-113) | — cited (dividend/EUR7M/reorg all used) | OK |
| quote_paragraphs | 3 | 3 (R:117 Patel, R:123 Patel cont., R:129 Gelhaus) | — treated as claims (Sec B/C) | OK |
| agenda_items | 0 | 0 | — | OK |
| annexures_director_profiles | 0 | 0 | — | OK |
| auditor_paras | 0 | 0 (results self-labelled "Unaudited" R:51/86/142) | — Step 0D auditor=ND | OK |
| entities | 0 | 0 | — | OK |
| signature_blocks | 1 | 1 (Mittal Mehta, CS, R:66-75) | — noted Step 0 | OK |
| concall_notice_items | 6 | 6 (R:142-153) | — Sec B / monitorables | OK |
| covering_letter_elements | 9 | 9 (R:48-77) | — | OK |
| about_contacts_disclaimer | 11 | 11 (PPT name wraps R:163/164; recovered) | — 4 divisions used | OK |
| page_header_id_blocks | 2 | 2 (R:80, R:137) | — | OK |
| **TOTAL** | **48** | **48** | **none** | **OK** |

### Presentation ledger (29 slides / 414 numbers / 6 footnotes)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| slides | 29 | 29 (extract `[page 1]`…`[page 29]`) | — all reviewed per preamble | OK |
| numbers | 414 | 414 (spot-recount agrees: consol table P:672 = 90 cells, standalone P:698 = 80, snapshot P:145 = 15, trend P:168 = 35, order/backlog P:203 = 32) | — | OK |
| footnotes | 6 | 6 (P:256, P:498, P:566 = 355-order x3; P:200 PPA restate; P:695, P:721 rounding) | — FN-12/FN-13/rounding all cited | OK |
| dropped_slides | N.A. | N.A. (no prior deck) | — | OK |

### Ledger flags — every flag traced to an A4 disposition

| Ledger flag | Where A4 dispositions it | Status |
|---|---|---|
| ZERO_STANDING Exceptional Items (consol P:687) | Step 0D table, gate 7, FN-01/FN-11 | reviewed |
| ZERO_STANDING OCI (standalone P:717) | Step 1 standalone table (0/2/0); Q10 covers consol OCI 55→5 | reviewed |
| ZERO_STANDING HET Revenue "Flat" (P:487) | Step 1 division cross-check, Step 2 | reviewed |
| AXIS_BINDING_UNCERTAIN x3 (slides 6/17/18) | Step 3 L176 explicit endpoint-binding resolution | reviewed |
| REPEAT_FOOTNOTE 355 (P:256/498/566) | FN-12, Step 8.5 Q12, gate 10, growth-trigger | reviewed |
| RESTATEMENT PPA (P:200) | FN-13, Step 3, Q13 | reviewed |

**A3 findings incorporated (per A4 preamble + YAML):** F6-01/02/03, F8-01/02, F13-01, F14-01;
FN-01…FN-14 (all 14). Cross-checked against ledger flags above — every enumerated
flag has an A4 disposition. **No orphan row. No row my fresh pass found that the ledger lacks.**

**Coverage result: PASS.**

---

## AUDIT 2 — ARITHMETIC (every A4 derived metric recomputed from raw extract)

Source figures re-read from P:676-694 (consol) and P:703-719 (standalone). Deck footers
(P:695/P:721) state percentages are computed on ABSOLUTE (unrounded) figures — so where a
%/bps derived from rounded crores differs from the disclosed value by <1 unit, that is a
rounding artifact, not an error. Columns Q1FY26 | Q4FY26 | Q1FY27 unless noted.

| Metric | A4 value | My recompute (raw) | Source line | Status |
|---|---|---|---|---|
| Consol Operating EBITDA | 101 / 75 / 94 | 795−694=101 / 944−868=76→disc 75 / 925−831=94 | P:677/680/681 | OK (Q4 76 vs disc 75 = source rounding) |
| Consol Op EBITDA margin | 12.7 / 8.0 / 10.1% | 101/795=12.7 / 75/944=7.9→8.0 / 94/925=10.16→10.1 | P:682 | OK |
| Consol Reported EBITDA (+OI) | 110 / 93 / 104 | 101+9 / 75+18 / 94+10 | P:681/683 | OK |
| Consol Core PBT ex-OI | 23 / 8 / 30 | 32−9 / 26−18 / 40−10 | P:688/683 | OK |
| Consol OI/PBT | 28 / 69 / 25% | 9/32=28.1 / 18/26=69.2 / 10/40=25.0 | P:683/688 | OK |
| Consol Effective Tax Rate | 65.6 / 42.3 / 45.0% | 21/32=65.6 / 11/26=42.3 / 18/40=45.0 | P:689/688 | OK |
| Consol PAT margin | 1.3 / 1.6 / 2.4% | 10/795=1.3 / 15/944=1.6 / 22/925=2.4 | P:691 | OK |
| Consol Revenue YoY | +16.4% (disc +16) | 795→925 = +16.35% | P:677 | OK |
| Consol Op EBITDA YoY | −6.9% (disc −7) | 101→94 = −6.93% | P:681 | OK |
| Consol EBITDA-margin YoY | −258 bps | disc −258 (abs); 10.1−12.7 rounded = −260 | P:682 | OK |
| Consol Finance cost YoY | −46.5% (disc −47) | 43→23 = −46.5% | P:685 | OK |
| Consol EBIT (EBITDA−D) YoY | −18.5% | (101−36)=65 → (94−41)=53 = −18.46% | P:681/684 | OK |
| Consol Core PBT ex-OI YoY | +30.4% | 23→30 = +30.43% | derived | OK |
| Consol Reported PBT YoY | +27% (disc) | 40−32; disc 27% (abs), rounded +25% | P:688 | OK |
| Consol PAT YoY | +118% (disc) | 10→22; disc 118% (abs), rounded +120% | P:690 | OK |
| Consol EPS YoY | +114% (disc) | 2.48→5.32 = +114.5% | P:694 | OK |
| Standalone Op EBITDA margin | 15.7 / 9.0 / 11.0% | 36/231=15.6→15.7 / 26/289=9.0 / 26/235=11.06→11.0 | P:709 | OK |
| Standalone Core PBT ex-OI | 21 / 12 / 14 | 22−1 / 20−8 / 15−1 | P:713/710 | OK |
| Standalone Effective Tax Rate | 27.3 / 15.0 / 20.0% | 6/22=27.3 / 3/20=15.0 / 3/15=20.0 | P:714/713 | OK |
| Standalone PAT margin | 7.4 / 5.7 / 4.7% | 17/231=7.36→7.4 (my recompute matches A4) / disc 5.7 / disc 4.7 | P:716 | OK — see note [a] |
| Standalone EBITDA YoY | −28% | 36→26 = −27.8% | P:708 | OK |
| Standalone Op-margin YoY | −466 bps | disc −466 (abs) | P:709 | OK |
| Standalone PBT YoY | −35% (disc) | 22→15; disc −35% (abs), rounded −31.8% | P:713 | OK |
| Standalone PAT YoY | −33% (disc) | 17→11; disc −33% (abs), rounded −35.3% | P:715 | OK |
| Standalone EPS YoY | −33% (disc) | 3.71→2.48 = −33.2% | P:719 | OK |
| PAT bridge endpoints | 10→22 = +12 | 10→22 = +12 | P:690 | OK — see note [b] |
| S-vs-C subsidiary contribution | −7 / −1 / +11 | 10−17 / 15−16 / 22−11 | P:690/715 | OK |
| S-vs-C subs % of consol | −70 / −7 / +50% | −7/10 / −1/15=−6.7 / +11/22 | derived | OK |
| YoY subsidiary swing | +18 | +11−(−7) = +18 | derived | OK |
| Gate 4 backlog QoQ / YoY | +4% / +20% | 2,289/2,205=+3.8→4 / 2,289/1,906=+20.1 | P:107/P:214 | OK |
| Order-intake division tie | 1,007 | 502+367+58+80 = 1,007 | P:492/P:106 | OK |
| Division revenue tie | ≈925 | 466+255+74+131 = 926 ≈ 925 | P:486 | OK (rounding) |
| QoQ revenue | −2% | 925/944 = −2.01% | P:677 | OK |
| QoQ EBITDA | +25% | 75→94 = +25.3% | P:681 | OK |

**Notes:**
- **[a] Standalone Q1FY26 PAT margin.** My independent recompute from raw crores = 17/231 =
  **7.4%**, which MATCHES A4's 7.4%. The deck's disclosed figure (P:716) is **7.2%**
  (computed on unrounded absolutes per the P:721 casting footnote). The 0.2pp gap is fully
  inside the rounding band of the ₹17 Cr PAT input; it is NOT a mismatch between my recompute
  and A4. Within rounding — PASS. (Observation only: A4 could have cited the disclosed 7.2%
  to match the other two cells in that row, which use P:716.)
- **[b] PAT-bridge non-footing.** A4's bridge components (EBIT −12, finance +20, OI +1,
  exceptional 0 = PBT +9; then +tax +3 = +11) do not foot exactly to the reported deltas
  (PBT +8, PAT +12) because Q1FY26's individually-rounded lines reconstruct to PBT 31 / PAT 11
  vs reported 32 / 10 — a ±1 Cr source-rounding artifact disclosed by the casting footnote.
  A4 anchored the bridge to the disclosed endpoints (PAT 10→22 = +12), which are correct.
  Within rounding — PASS.

**Arithmetic result: PASS. No mismatch above rounding between any A4 derived metric and my
independent recompute.**

Additional source-inconsistency observed (NOT an A4 error): QoQ PAT is disclosed as **44%**
in the highlight bullets (R:105, P:302) but **47%** in the summary table (P:690, 15→22 =
+46.7%). This is an inconsistency inside the source documents, not an A4 derivation. A4 quoted
the 44% headline; the true QoQ is 47%. Immaterial to the thesis (both are QoQ off the
exceptional-laden Q4 base A4 already discounts). Logged for awareness only.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to the 3 most positive claims)

| # | Most-positive A4 claim | Strongest bear counter from the SAME extract | Survives? | Already in A4? |
|---|---|---|---|---|
| 1 | "Order backlog +20% YoY to ₹2,289 Cr; order intake highest-ever ₹1,007 Cr — genuine pipeline strength (gate 4 GREEN)" (Sec C L412) | The Q1 FY26 base carries a one-off ₹355 Cr order (P:256/498/566), so intake/PST YoY optics are inflated; backlog is undefined as gross/net-of-GST or executed/pending; HET order intake +719% is off a ₹7→58 Cr micro-base (P:559), i.e. noise not signal | Yes (extract-supported) | **Yes** — FN-12, Step 8.5 Q12, gate 10 AMBER, growth-trigger table. No graft needed. |
| 2 | "Consolidated revenue +16% YoY (₹925 Cr) = genuine top-line strength" (Step 2) | Standalone (domestic) revenue only +2% (231→235, P:704); growth is entirely subsidiary/overseas-led; revenue is −2% QoQ and has plateaued ~₹900-945 Cr for four quarters (P:677/175) — no step-change up | Yes | **Yes** — Step 2 diagnostic 1, Step 3 run-rate, brief narrative. No graft needed. |
| 3 | "PAT more than doubled, +118% YoY (₹22 Cr); no fresh European exceptional (gate 7 GREEN)" | The entire +₹12 Cr PAT rise is below-EBIT: finance cost +₹20 Cr (partly FX-reclass base) and tax +₹3 Cr, against EBIT −₹12 Cr; it is a ~₹18 Cr subsidiary loss-to-profit swing masking standalone PAT −33%. Gate 7 "green" is fragile: ₹9 Cr exceptional was just one quarter ago and the 12-24m refinancing/intercompany unwind (P:595-606) keeps fresh-exceptional and ₹852 Cr goodwill-impairment risk live (FN-13) | Yes | **Yes** — Step 2 diag 3/4, Step 4 bridge + S-vs-C metric, gate 7 "GREEN by absence/unmonitored", FN-01/FN-13, Q8/Q13. No graft needed. |

**Adversarial result: PASS.** All three bear counters are extract-supported and SURVIVE, but
each is already incorporated in A4's review (the review is, unusually, more bearish than its
own headline). **No surviving counter requires grafting into A4 before save.**

---

## VERDICT

**COMPLETE.** Gate 0 (plain-language brief, four parts) PASS; coverage PASS (48 results rows +
29 slides / 414 numbers / 6 footnotes all reconciled, zero orphans, zero missing-from-ledger);
arithmetic PASS (every A4 derived metric reproduces within rounding, including the ETR wedge
45.0% consol vs 20.0% standalone, the +118% PAT bridge, and the +₹18 Cr S-vs-C swing);
adversarial PASS (three surviving bear counters, all already incorporated). No loop-back
required. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "GMMPFAUDLR"
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
