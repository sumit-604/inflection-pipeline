# A5 ADVERSARY / COMPLETENESS AUDIT — NephroPlus (Nephrocare Health Services Ltd) — Q1 FY27 — v2 (MERGED review, concall + AGM)

Auditor: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 12 Aug 2026
Review under audit: `runs/nephroplus-q1fy27/work/review_nephroplus_q1fy27_v2.md`
Method: fresh context. I re-derived every figure from the A1 extracts and re-ran the enumeration against the A2 ledgers. I did not defer to A4's or A3's cites; each was re-checked at its cited source line/turn.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The Mandatory Plain-Language Brief (Section 19) carries all four labelled parts, each present and non-empty with real content:

| Part | Heading | Present | Content check |
|---|---|---|---|
| 1 | 19.1 SUMMARY NARRATIVE | present | ~20-line narrative; numbers-anchored; covers growth, non-GAAP framing, Saudi, guidance, AGM, verdict, INDETERMINATE cap |
| 2 | 19.2 SECTOR INTELLIGENCE | present | dialysis annuity economics, penetration, organized-share shift, reimbursement dependence, lumpy pricing; provenance-tagged |
| 3 | 19.3 BUSINESS-MODEL INTELLIGENCE | present | asset-light BOO model, four cost levers, geographic margin structure India vs intl, fixed-capacity vs same-store |
| 4 | 19.4 COMPETITION INTELLIGENCE | present | scale/focus moat, PH #2, UZ sole private, Fresenius/DaVita, Saudi binary-tender JV with Tibbiyah |

**Gate: PASS.** All four parts present.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers, then ledger→review reflection)

### 1a. Fresh count diff vs ledgers

| Category | A2 count | My fresh count | Orphan/extra rows | Status |
|---|---|---|---|---|
| Concall participants | 17 | 17 (4 mgmt + Operator + IIFL host + 11 analysts) | none | MATCH |
| Concall turns | 103 | 103 (opening 3 + moderator/host + Q&A to turn 103 closing, l.124) | none | MATCH |
| Concall questions | 36 | 36 (34 question-bearing turns; Sedar l.26 bundles 3) | none | MATCH |
| Concall mgmt-number rows | 81 (34 turns) | reconciles (spot-checked l.10/12/18/22/40/49/71/106) | none | MATCH |
| Concall forward/hedge rows | 18 | reconciles (guidance 15-20%, 12-18m cadence, 3 refusals, RPT caveat) | none | MATCH |
| AGM resolutions | 6 | 6 (L131-152) | none | MATCH |
| AGM directors present | 8 | 8 (L61-72) | none | MATCH |
| AGM in attendance | 7 | 7 (L76-87) | none | MATCH |
| AGM quorum | 1 (74 members) | 1 (L92) | none | MATCH |
| AGM procedural/other | 20 | reconciles (RESULT_PENDING L166-167, recusal L123-127, clean audit L120-121) | none | MATCH |
| Results notes | 21 | carried from A5 v1 COMPLETE; spot-checked geography L699-702, IPO L717-727 | none | MATCH |

No orphan rows (ledger rows absent from review) and no rows my fresh pass found that a ledger lacks.

### 1b. Ledger row → review reflection (designed-silence + forward-signal → question)

**Concall designed-silence items — each generates ≥1 management question:**
- Saudi loss/revenue run-rate (refused, l.62; F17.3) → **Q14** (+ retained Q1). CONFIRMED.
- Country splits (refused, l.117; F17.1) → **Q7** retained (platform-only); monitoring items 15-17 marked designed-silence. CONFIRMED.
- Same-store (refused, l.117/119) → **Q17** + Exchange 3. CONFIRMED.
- Captive/hospital renewal (never raised, F17.2) → **Q21**. CONFIRMED.

**AGM promoter-economics items — each generates ≥1 management question:**
- Promote Incentive Arrangement (Res 6, Agreement 25-Jul-2025, L149-152) → **Q22** (+ Ordinary-vs-Special anomaly F-11). CONFIRMED.
- ESOP Scheme 2026 (Res 3-4, L140-144, incl. "holding company") → **Q23**. CONFIRMED.
- MD remuneration clarificatory amendment (Res 5, L145-148) → **Q24**; vote tallies → **Q25**. CONFIRMED.

**Other concall forward/ambiguous findings → questions:** F1.1(dep one-off)→Q19; F6.1/F6.8(guidance)→Q17; F6.5/F7.5(Saudi timeline)→Q15; F6.7(contract mfg)→Q20; F8.1(ETR)→Q18; F14.1(120/125 bps)→Q16; F16.1(non-GAAP)→Q14/Q3(retained). All present.

**Coverage status: PASS.** Every ledger row across all five documents is reflected or explicitly dispositioned; every designed-silence and forward-signal finding converts to at least one question.

**Minor coverage observations (non-gating):** three A2-flagged transcription artifacts are not explicitly reconciled in the review body but their substantive metrics are correctly used: (i) RPT prior-year comparator "₹253" (l.12) is an obvious typo for ~₹2,503 — review correctly uses RPT ₹2,733 / +9.2%; (ii) network cities "370" (l.8) vs "357" (l.10) — review uses 357; (iii) "addition of 50 clinics" (garbled l.28) vs 26 added — review uses 26. None affect a monitored metric; advisory only.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract lines; Role 4 metrics + concall cross-checks)

### 2a. Derived metrics (CONSOLIDATED), recomputed from R L582-627

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| Op EBITDA ex-OI Q1FY27 | 63.88 | 44.60+24.54+2.21−7.46 = 63.89 (PBT-before-JV basis) | MATCH (rounding) |
| Op EBITDA margin Q1FY27 | 22.7% | 63.88/281.75 = 22.67% | MATCH |
| Op EBITDA ex-OI Q1FY26 | 47.56 | 28.52+19.52+6.10−6.58 = 47.56 | MATCH |
| Op EBITDA YoY | +34.3% | 63.88/47.56−1 = 34.31% | MATCH |
| Op EBITDA margin YoY | +180 bps | 22.67−20.88 = 1.79pp | MATCH |
| Core PBT ex-OI (after JV) Q1FY27 | 33.57 | 41.03−7.46 = 33.57 | MATCH |
| Core PBT ex-OI YoY | +53.0% | 33.57/21.94−1 = 53.0% | MATCH |
| Reported PBT YoY | +43.9% | 41.03/28.52−1 = 43.86% | MATCH |
| ETR Q1FY27 | 22.1% | 9.06/41.03 = 22.08% | MATCH |
| ETR Q1FY26 | 16.9% | 4.82/28.52 = 16.90% | MATCH |
| ETR Q4FY26 | 8.6% | 2.85/33.22 = 8.58% | MATCH |
| OI/PBT Q1FY27 | 18.2% | 7.46/41.03 = 18.18% | MATCH |
| PAT margin Q1FY27 | 11.3% | 31.97/281.75 = 11.35% | MATCH |
| Reported PAT YoY | +34.9% | 31.97/23.70−1 = 34.89% | MATCH |
| Revenue YoY | +23.7% | 281.75/227.78−1 = 23.69% | MATCH |
| EPS basic YoY | +13.1% | 3.19/2.82−1 = 13.12% | MATCH |
| FY26 Op EBITDA | 226.96 | 100.57+90.67+60.24−24.51 = 226.97 | MATCH (rounding) |

### 2b. Derived metrics (STANDALONE), recomputed from R L262-299

| Metric | A4 value | My recompute | Status |
|---|---|---|---|
| Op EBITDA ex-OI Q1FY27 | 24.15 | 16.69+13.09+0.49−6.12 = 24.15 | MATCH |
| Op EBITDA margin Q1FY27 | 14.2% | 24.15/170.38 = 14.17% | MATCH |
| Revenue YoY | +14.5% | 170.38/148.83−1 = 14.48% | MATCH |
| Core PBT ex-OI YoY | +169% | 10.57/3.93−1 = 168.96% | MATCH |
| PAT YoY | +150.6% | 12.56/5.01−1 = 150.70% | MATCH (0.1pp rounding) |
| ETR Q1FY27 | 24.7% | 4.13/16.69 = 24.75% | MATCH |

### 2c. Concall cross-checks (task-specified)

| Check | A4 treatment | My verification (source) | Status |
|---|---|---|---|
| Reported vs adjusted EBITDA | Op EBITDA 63.88 reported; Adj 65.1 (ex-ESOP, ex-Saudi) | l.12 states Adj EBITDA 65.1 vs 49.8, +31%; filing op EBITDA 63.89 | MATCH |
| Reported vs adjusted PAT | Reported 31.97/+34.9%; Adj 37/+41.7% | l.12 states Adj PAT 37 vs 26, +41.7%; filing PAT 31.97 | MATCH; reported +34.9% NEVER spoken (confirmed vs full transcript) |
| +120 vs +125 bps | Rohit +120 (l.10), Prashant +125 (l.27); filed adj 23.1 vs 21.9 = +120 | l.10 "120 basis point... 23.1%"; l.27 "125 basis point" | MATCH — inconsistency correctly surfaced (F14.1) |
| AR days 121→101 | improved 20 days YoY | l.22 verbatim "121 days to 101 days... 20-day improvement" | MATCH |
| ETR ~20% | spoken ~20% proxy; filed 22.1%; Uzbekistan 0% conditional on healthcare >90% | l.49 verbatim | MATCH |
| RPT growth | RPT ₹2,733 +9.2%; ~11% CAGR | l.12 (+9.2%), l.40 (~11% CAGR) | MATCH (₹253 comparator is a transcription typo, non-material) |
| Revenue/guest/treatment | +23.7% / guests +13% to 38,262 / treatments +13.3% to 10.3 lakh | l.10 and l.12 | MATCH |
| Intl revenue mix 44.9% | 44.9% (R L699-702), concall ~45% | (906.29+321.34+36.12)/2,817.54 = 44.85% | MATCH |
| Subsidiary share of PAT 60.7% | 60.7% (Q1FY27) | (31.97−12.56)/31.97 = 60.7%; Q4 64.1%; Q1FY26 78.9% | MATCH |
| IPO unutilised | ₹117.67 Cr; clinic-capex ₹116.34 of ₹129.11 Cr | R L724-727: 1,176.70M / 1,163.38M of 1,291.06M ×0.1 | MATCH |

**Every derived metric in every analytical table reconciles to a cited raw line/turn.** No arithmetic error in any financial table.

### 2d. ONE arithmetic error found — outside the financial tables, in the AGM section

**Section C3 (Governance-positive signals), "Full board present" bullet, and the same claim in Step 0D lineage:** the review describes the 8-director board as **"2 promoter/exec-adjacent, 4 nominee, 4 independent."** That tally sums to **10**, and it misstates the composition.

Re-derived from the primary evidence (AGM extract L61-72):
- 1 executive/promoter: Vikram Vuppala (CMD) — **A4 says 2**
- 3 nominee: Gaurav Sharma, Vishal Vijay Gupta, Sunil Kumar Thakur — **A4 says 4**
- 4 independent: Hemant Sultania, Om Prakash Manchanda, Annette Kumlien, Ajay Bakshi — A4 says 4 (correct)
- Total = **8** — A4's breakdown sums to 10

(Kamal D Shah, the only other promoter-side figure, is **"In attendance" (L78), not a director** — so there is no second promoter/exec director.) This is a mismatch above rounding against a cited primary source, and by the audit's own FAIL taxonomy an "arithmetic error" loops back to A4. The headline fact ("all 8 directors present") and every governance conclusion (proper recusal, independent chairing Res 5-6, clean audit) are correct and unaffected, but the erroneous sub-tally must be corrected before save.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear from the same text; does a NEW counter survive?)

**Claim 1 — "Operating-led clean quarter: revenue +23.7%, operating EBITDA +34.3%, margin +180 bps."**
Strongest bear from same text: part of the QoQ/YoY margin gain is a self-declared **one-time depreciation benefit** (RFID + near-zero machine adds, l.58, "of course it's a one-time benefit"); the RPT tailwind embeds **non-repeatable lumpy pricing** (PH +55-60%, CGHS +35%, l.40/56) that management says "one should not expect... to continue forever"; and management guides **15-20%** below the 23.7% delivered (l.12 vs l.10). **Already grafted** into the review (F1.1, F7.3, F6.8; Steps 2/3/4, Q17/Q19). No new surviving counter.

**Claim 2 — "KSA growth trigger resolved favourably; license delivered."**
Strongest bear from same text: the tender is **binary across four clusters** — "if you don't win, you pack the bags and leave" (l.81); loss run-rate and revenue **refused under ~5x questioning** (l.62/80); timeline given three irreconcilable ways (l.10/60/62). **Already grafted** (Step 6D "ON TRACK but BINARY", Exchange 1, F17.3/F6.5, Q14/Q15). No new surviving counter.

**Claim 3 — "No tripwire fired; promoter TRUSTWORTHY; clean audit."**
Strongest bear from same text: three **undisclosed** promoter-economics/dilution items approved same-week (Promote Incentive Arrangement Res 6, ESOP 2026 Res 3-4 incl. a "holding company" above the listco, MD remuneration amendment Res 5; AGM L140-152); the entire profitability headline was **non-GAAP** (reported PAT +34.9% never spoken, F16.1); country economics/same-store **withheld by design** (l.117). **Already grafted** (Section C, monitoring item 14, tripwire 6 watch, F16.1, F17.1, Q22-Q25). No new surviving counter.

**Adversarial status: PASS.** All strong bear counters constructible from the extracts are already incorporated in the review. No un-incorporated surviving counter to graft.

---

## SPECIFIC CONFIRMATIONS REQUESTED

- **Non-GAAP reframing surfaced:** YES — reported PAT +34.9% / reported EBITDA ₹63.88 Cr flagged as NEVER spoken (F16.1; Steps 1c, 2, R5-6E, verdict, narrative). Verified against full 103-turn transcript: management verbalised only Adj EBITDA 65.1 / Adj PAT 37 / +41.7%.
- **Cash-conversion INDETERMINATE cap NOT relaxed by AR-days:** CONFIRMED — Step 5 explicitly holds INDETERMINATE, item 8 GREEN on AR days but "does not lift the cash-conversion classification"; verdict capped at PROCEED WITH CAVEATS; missing evidence named (no Q1 CFO, no Q1 BS, capex not isolable, net cash not refreshed).
- **No exit PE / valuation introduced:** CONFIRMED — Step 7 states "destination PE and fair values are not recomputed"; entry zone ₹345-423 and CMP ₹644 are carried Notion memory, not new multiples. No round-number default. Complies with the Section 1B / never-invent-exit-PE rule.
- **Standalone AND consolidated both treated:** CONFIRMED — Steps 1a/1b, 2/2b; S-vs-C margin gap (14.2% vs 22.7%) analysed (F2).
- **Doctype-mismatch provenance handled without fabrication:** CONFIRMED — the uploaded `concall_nephroplus_q1fy27.pdf` is in fact the 17th AGM Reg 30 filing (A1 content_mismatch_note; AGM ledger DOCTYPE_MISMATCH / F-10); the actual transcript was supplied separately as `concall_transcript_nephroplus_q1fy27.txt`. The review treats the PDF as an AGM/Board-Outcome document (Section 0, Section C) and sources all Role 5 content to the transcript. Spot-checked C-cites (l.8/10/12/22/40/49/58/62/71/81/106/117) all resolve to the transcript. No concall content fabricated.

---

## VERDICT

**INCOMPLETE.**

**Failing agent: A4.**

**Exact gap:** Section C3 (and the "Full board present" governance note) misstates the 8-director AGM board as "2 promoter/exec-adjacent, 4 nominee, 4 independent" — a tally that sums to 10 and contradicts the primary evidence (AGM extract L61-72). The correct composition is **1 executive/promoter (Vikram Vuppala), 3 nominee (Sharma, Gupta, Thakur), 4 independent (Sultania, Manchanda, Kumlien, Bakshi) = 8**. This is an arithmetic/factual error above rounding and must be corrected before Notion save. All other checks pass: deliverable-completeness gate PASS; coverage PASS (no orphan/missing rows; all designed-silence + forward-signal findings converted to questions); every derived financial-table metric and every concall cross-check reconciles; adversarial read finds no un-incorporated surviving bear counter; non-GAAP framing surfaced; INDETERMINATE cap intact; no exit PE introduced; standalone and consolidated both treated; doctype provenance correctly handled with no fabricated concall content.

Advisory (non-gating, recommend A4 fold into the same correction pass): explicitly note the three A2-flagged transcription artifacts (RPT "₹253" typo; cities 370 vs 357; "50 clinics" garble) as transcription inconsistencies, and tighten the F4 label "44.9% of revenue arising in subsidiaries" to "international geographies" (the 44.85% is the geographic mix from R L699-702; the standalone-vs-consolidated revenue gap is 39.5%).

```yaml
stage: A5-adversary
company: "NEPHROPLUS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "AGM board composition (Section C3 'Full board present')"
    a4_value: "2 promoter/exec-adjacent + 4 nominee + 4 independent (= 10)"
    recomputed: "1 executive/promoter (Vikram Vuppala) + 3 nominee (Sharma, Gupta, Thakur) + 4 independent (Sultania, Manchanda, Kumlien, Bakshi) = 8"
    source_line: "AGM extract L61-72"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Section C3 misstates the 8-director AGM board as '2 promoter/exec-adjacent, 4 nominee, 4 independent' (sums to 10); correct composition per AGM L61-72 is 1 executive/promoter + 3 nominee + 4 independent = 8. Arithmetic/factual error above rounding; correct before Notion save. All other audits (deliverable, coverage, financial-table arithmetic, concall cross-checks, adversarial, non-GAAP surfacing, INDETERMINATE cap, no-exit-PE, standalone+consolidated, doctype provenance) PASS."
```
