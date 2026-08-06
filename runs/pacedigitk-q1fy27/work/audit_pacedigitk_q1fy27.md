# A5 ADVERSARY / COMPLETENESS AUDIT — Pace Digitek Ltd (PACEDIGITK), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Re-audit (prior verdict INCOMPLETE: three YoY % on rounded-Cr inputs + two borderline cells)
Independence: derived fresh from the A1 extracts and A2 ledgers only. All A4 cites re-checked, not deferred to.
Units: filing is Rs Millions; x0.1 = Rs Cr. Press release already Rs Cr. Deck Rs Mn.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF located at review lines 496-530. Four labelled parts checked for presence and real content:

| Part | Heading present | Location | Content | Status |
|---|---|---|---|---|
| 1. Summary narrative | yes | L498-510 | 11 lines of substantive prose (revenue, subsidiary split, core PBT, EPS, margin, missing CFO, execution, verdict) | PRESENT |
| 2. Sector intelligence | yes | L512-516 | energy-transition read-across, PSU order book, ~96% govt concentration caveat, margin mix shift, provenance-tagged | PRESENT |
| 3. Business-model intelligence | yes | L518-524 | 3-way model, 52% subsidiary-sourced, captive EPC/eliminations, capex/leverage strain, provenance-tagged | PRESENT |
| 4. Competition intelligence | yes | L526-530 | named peers, EXICOM read-across, where Pace wins/weaker, competitive risk, provenance-tagged | PRESENT |

Gate result: PASS. All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep/sweep vs A2 ledgers, then orphan check vs A4)

### 1.1 Independent re-enumeration (my fresh pass vs A2 counts)

| Category | A2 count | My fresh count | Method / evidence | Status |
|---|---|---|---|---|
| Results: notes | 15 | 15 | Standalone 1-8 (RL197,203,207,212,219,232,241,246)=8; Consolidated 1-7 (RL490,495,500,506,515,530,534)=7 | MATCH |
| Results: line items | 61 | 61 | Standalone table RL158-191=25; Consolidated RL438-486=36 | MATCH |
| Results: entities | 9 | 9 | RL317-326: 1 parent + 7 subs + 1 step-down | MATCH |
| Results: auditor paras | 13 | 13 | Standalone B 4 + Consolidated E 9 | MATCH |
| Results: signature blocks | 5 | 5 | RL65-72, RL124-134, RL250-266, RL401-412, RL540-551 | MATCH |
| Results: zero-standing | 5 | 5 | C6,C15,C23,G16,G34 | MATCH |
| PR: disclosure blocks | 36 | 36 | blank-line blocks across 4 pages | MATCH |
| PR: numbers | 56 | 56 | table 2 rows 1-56 incl. line-wrap-split "10 GWh" (#56) | MATCH |
| PR: forward signals | 7 | 7 | PR L84-86,91-92,113-115,117-119,129-135,157-158,158-159 | MATCH |
| Deck: slides | 26 | 26 | 26 [page N] markers = page_count_pdfinfo | MATCH |
| Deck: numbers | 357 | 357 | per-slide sum recomputed (14+1+1+16+18+36+75+63+0+7+3+2+0+20+32+22+0+3+7+5+13+0+4+7+2+6 = 357) | MATCH |
| Deck: line items | 59 | 59 | S7 17 + S8 12 + S15 14 + S16 16 | MATCH |
| Deck: notes | 7 | 7 | S5,S8(x3),S15,S16,S25 | MATCH |
| Deck: zero-standing | 2 | 2 | S15 MAHAGENCO, Bondada GWh dashes | MATCH |

No row my fresh pass found that the ledger lacks. No missing-from-ledger FAIL to A2.

Internal reconciliations independently re-verified: order wins 7,099+7,020+2,647 = 16,766 (matches headline); order book Energy 8,453 Cr + Telecom 2,350.3 Cr = 10,803.3 Cr (matches PR); waterfall 96,613 (31-Mar) + 16,766 incoming − 5,346 sales = 108,033 (30-Jun) closing = 10,803.3 Cr — reconciles (note: A2 ledger annotation reversed the opening/closing date labels on rows S5:L146/L148, but both values captured; not material). Slide-24 order book 113,379 mn (11,337.9 Cr) differs from 108,033 — A4 flags this as the reconciliation question.

### 1.2 Orphan-row check (ledger rows absent from A4)

- Results notes: all 15 carried into A4 Step 0D table (SA-1..8, CO-1..7). No orphan.
- Consolidation entities: 9 handled (component-auditor reliance / unreviewed-subs treated in Step 0E; 2 foreign subs flagged). No orphan.
- Deck CIN discrepancy (S26 U-prefix vs S1 L-prefix): carried into A4 flags (YAML L596). No orphan.
- Standalone Note 4 share-count transposition (3,73,35,967 vs reconciling 3,73,53,967): carried in SA-4 + FN9 + flags. No orphan.
- OI = Finance both exactly Rs28.34 Cr: carried to Q16. No orphan.
- Segment note blank (H1): carried to Q4, triggers #5/#6 unscorable. No orphan.

### 1.3 FORWARD-SIGNAL / AMBIGUOUS discharge check (every one must yield a Questions-for-Management row)

| Forward/ambiguous item | Ledger ref | Questions row |
|---|---|---|
| 2.5→5 GWh subsequent event | PR FS#1/#3/#6 | Q11 |
| C&I storage prototype under evaluation | PR FS#2 | Q12 |
| 5→10 GWh ramp + container fab on track | PR FS#4/#7 | Q8, Q11 |
| MEGMEET cooperation + Pune R&D (subsequent) | PR FS#5 | Q9 |
| FY27E/FY28E guidance | Deck S24 | Q10 |
| New 5 GWh line Q3 FY27 / machines Oct 2026 | Deck S21 | Q11 + monitorables |
| Order-book two totals + 78.1% label | Deck S24/S14 ambiguity | Q7 |
| Segment note blank | Results H1 ambiguity | Q4 |
| ETR sub-statutory + deferred-tax credit | Results ambiguity | Q13 |
| Actuarial loss Rs0.43 Cr ~92% of FY26 | Results ambiguity | Q14 |
| Foreign subs NIL/Rs0.52 Cr direction | Results ambiguity | Q15 |
| OI = Finance exact match | Results cross-doc | Q16 |

All forward-signal and ambiguous items discharged. No orphan → no FAIL to A3.

COVERAGE result: PASS. orphan_rows = []; missing_from_ledger = [].

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Millions; every derived cell)

### 2.1 Table 1A/1B unit conversions (spot of all lines) — all tie (x0.1)
Standalone RL158-191 and Consolidated RL438-486: every A4 Cr figure equals raw Mn x0.1 within rounding. Verified line by line (Revenue, OI, expenses, PBT, tax, PAT, PAT-to-owners, NCI, EPS). No exception.

### 2.2 Table 1C derived metrics

| Metric | A4 | Recomputed (raw) | Status |
|---|---|---|---|
| Op EBITDA SA Q1FY26 (PBT+D+Fin−OI) | 72.96 | 68.92+1.09+8.87−5.92 = 72.96 | OK |
| Op EBITDA SA Q1FY27 | 49.43 | 57.24+3.19+7.89−18.89 = 49.43 | OK |
| Op EBITDA CO Q1FY26 | 80.05 | 73.88+2.09+9.72−5.64 = 80.05 | OK |
| Op EBITDA CO Q1FY27 | 86.07 | 81.63+4.44+28.34−28.34 = 86.07 | OK |
| Op EBITDA CO FY26 | 455.24 | 429.53+12.00+59.82−46.11 = 455.24 | OK |
| Op EBITDA margin CO Q1FY27 | 15.50% | 86.07/555.36 = 15.50% | OK |
| Op EBITDA margin CO Q1FY26 | 21.81% | 80.05/367.08 = 21.81% | OK |
| Core PBT CO Q1FY27 | 53.29 | 81.63−28.34 = 53.29 | OK |
| OI/PBT CO Q1FY27 | 34.7% | 28.34/81.63 = 34.7% | OK |
| ETR CO Q1FY27 | 23.4% | 19.12/81.63 = 23.42% | OK |
| ETR CO FY26 | 28.5% | 122.27/429.53 = 28.47% | OK |
| PAT margin CO Q1FY27 | 11.3% | 62.51/555.36 = 11.26% | OK |
All 35 cells of 1C recomputed; every one ties within rounding.

### 2.3 Step 2A Consolidated YoY — including the three PRIOR-GAP cells

| Metric | A4 | Recomputed from raw Mn | Deck tie | Status |
|---|---|---|---|---|
| Revenue | +51.3% | 5,553.64/3,670.79−1 = 51.29% | S7 51.3% | OK |
| Op EBITDA | +7.5% | 86.07/80.05−1 = 7.52% | S7 7.5% | OK |
| Op EBITDA margin | −631 bps | 15.50−21.81 = −6.31pp | — | OK |
| **Depreciation (FIXED)** | **+112.6%** | **44.37/20.87−1 = 112.55%** | S7:L229 112.6% | **OK — fix correct (was 112.4% on rounded Cr)** |
| **Finance costs (FIXED)** | **+191.5%** | **283.41/97.23−1 = 191.48%** | S7:L232 191.5% | **OK — fix correct (was 191.6%)** |
| **Other income (FIXED)** | **+402.9%** | **283.41/56.36−1 = 402.86%** | S7:L233 402.9% | **OK — fix correct (was 402.5%)** |
| EBIT (operating) | +4.7% | 81.63/77.96−1 = 4.71% | S7 4.7% | OK |
| Core operating PBT | −21.9% | 53.29/68.24−1 = −21.91% | — | OK |
| Reported PBT | +10.5% | 81.63/73.88−1 = 10.49% | S7 10.5% | OK |
| PAT | +14.3% | 62.51/54.70−1 = 14.28% | S7 14.3% | OK |
| PAT to owners | +13.2% | 61.32/54.15−1 = 13.24% | — | OK |
| EPS | −6.3% | 2.84/3.03−1 = −6.27% | — | OK |

### 2.4 Step 2B Standalone YoY — including the two BORDERLINE cells

| Metric | A4 | Recomputed from raw Mn | Deck tie | Status |
|---|---|---|---|---|
| Revenue | −22.2% | 2,642.40/3,396.65−1 = −22.21% | S8 (22.2)% | OK |
| **Op EBITDA (borderline)** | **−32.2%** | **494.39/729.61−1 = −32.24%** (Q1FY27 = 572.43+31.94+78.93−188.91 = 494.39; Q1FY26 = 689.21+10.87+88.72−59.19 = 729.61) | S8:L256 (32.2)% | **OK — raw-Mn derivation correct** |
| Op EBITDA margin | −277 bps | 18.71−21.48 = −2.77pp | — | OK |
| **Depreciation (borderline)** | **+193.8%** | **31.94/10.87−1 = 193.83%** | S8:L258 prints 193.7% (deck rounding); A4 correctly uses its own 193.8% and notes the deck value | **OK — independently recomputed, deck variance flagged** |
| Finance costs | −11.0% | 78.93/88.72−1 = −11.04% | S8 (11.0)% | OK |
| Other income | +219.1% | 188.91/59.19−1 = 219.16% | S8 nm | OK |
| Core operating PBT | −39.1% | 38.35/63.00−1 = −39.13% | — | OK |
| Reported PBT | −16.9% | 57.24/68.92−1 = −16.95% | S8 (16.9)% | OK |
| PAT | −16.7% | 42.51/51.04−1 = −16.71% | S8 (16.7)% | OK |
| EPS | −31.1% | 1.97/2.86−1 = −31.12% | — | OK |

Prior-gap verdict: the three consolidated cells (D&A, Finance, OI) and the two standalone borderline cells (Op EBITDA, D&A) are all now re-derived from raw Millions, tie to the deck, and are correct. The rounded-Cr contamination is eliminated. Fix VERIFIED.

### 2.5 Step 2C / Step 4 / Step 6 spot recomputations

| Check | A4 | Recomputed | Status |
|---|---|---|---|
| Q1 as % of FY27E midpoint | 16.8% | 555.36/3,300 = 16.83% | OK |
| CoGS jump CO | +846% | 375.32/39.66−1 = 846.3% | OK |
| Implied Q2-Q4 avg | ~915 | (3,300−555.36)/3 = 914.9 | OK |
| Revenue QoQ | −49.4% | 555.36/1,096.78−1 = −49.36% | OK |
| PAT QoQ | −41.0% | 62.51/105.92−1 = −40.98% | OK |
| PAT bridge: rev@prior margin | +41.07 | 188.28×21.81% = 41.07 | OK |
| PAT bridge: margin drag | −35.04 | ≈−6.31pp×555.36 = −35.0 | OK (rounding) |
| PAT bridge: PBT change | +7.75 | 81.63−73.88 = 7.75 | OK |
| PAT bridge: reported PAT change | +7.81 | 62.51−54.70 = 7.81 | OK |
| OI-reverted PAT | ~45.1 | (81.63−22.70)×(1−0.2342) = 45.13 | OK |
| Core PBT ex-OI change | −14.95 | 53.29−68.24 = −14.95 | OK |
| TTM op EBIT (#19) | ~446.9 | (455.24−80.05+86.07)−(12.00−2.09+4.44) = 461.26−14.35 = 446.91 | OK |
| Energy segment implied (#6) | ~441.5 | 79.5%×555.36 = 441.5 | OK |
| Subsidiary-sourced share | ~52% / 7.5% | (555.36−264.24)/555.36 = 52.4%; (367.08−339.67)/367.08 = 7.5% | OK |
| Inter-co eliminations share | 49% | 250.9/515.1 = 48.7% | OK |
| SC-gap PAT% Q1FY27 | 47.0 | (62.51−42.51)/42.51 = 47.05% | OK |
| SC-gap PAT% Q4FY26 | 160.8 | (105.92−40.62)/40.62 = 160.8% | OK |
| SC-gap PAT% FY26 | 24.7 | (307.26−246.48)/246.48 = 24.66% | OK |
| SC-gap PAT% Q1FY26 | 7.2 | (54.70−51.04)/51.04 = 7.17% | OK |

ARITHMETIC result: PASS. No mismatch above rounding anywhere. arithmetic_mismatches = [].

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear from same text)

**Claim 1 (verdict C): "Consolidated revenue +51.3% is real and order-backed" — strong top-line.**
Bear from same extract: the growth is 100% subsidiary/Energy; the parent contracted −22.2% (RL158); consolidated core operating PBT fell −21.9% and standalone −39.1%; Op EBITDA margin −631 bps; CoGS +846% (RL442) as low-margin BESS manufacturing displaced EPC (RL443 −57%). The +14.3% PAT is Other Income (+22.70 Cr), not operations.
Survives? Already fully incorporated (Step 2A/2C, Step 4, verdict flags, brief). No graft required.

**Claim 2 (trigger #3 GREEN): "5 GWh BESS capacity reached ~Aug 2026" — execution delivered.**
Bear from same extract: the 2.5→5 GWh event is SUBSEQUENT to the quarter (PR L84-86, L113-115), not in Q1; it is installed capacity, not utilised (no utilisation figure); the container fab is only "ready for commissioning" (S21:L601-603, not producing); the genuinely-new 5 GWh line's machines arrive Oct 2026, operational only Q3 FY27 (S21:L610-614). "5 GWh reached" overstates in-period delivery.
Survives? Already incorporated (trigger #3 note ~1 month late; trigger #4 unscorable; Q11 on date + utilisation; growth-trigger "partial slip"). No graft required.

**Claim 3 (growth-visibility premium held): "Order book Rs10,803.3 Cr executable, strong revenue visibility."**
Bear from same extract: the deck carries a DIFFERENT total on S24 (Rs11,337.9 Cr) vs the PR/S5/S10 Rs10,803.3 Cr; the figure is "as of Aug 05" not June 30 (PR L83, L99); the only new Q1 order booked from a private/non-government counterparty is zero — the sole new order is a PSU (BSNL Rs264 Cr, PR L106); NEC XON/MEGMEET/3 MoUs are partnerships, not booked orders; the slide-14 split carries an unexplained 78.1% label alongside the reconciling 84.2%/15.8%.
Survives? Already incorporated (Q7 reconciliation, Q9 conversion, growth-trigger "DELAYED/unproven", flags on PSU concentration). No graft required.

ADVERSARIAL result: no surviving un-incorporated bear counter. surviving_bear_counters = [].

---

## VERDICT

- Deliverable gate: PASS (all four brief parts present).
- Coverage: PASS (all 14 categories reconcile; no orphan rows; every forward-signal/ambiguous item discharged to a Questions row).
- Arithmetic: PASS (all derived cells re-derived from raw Millions tie within rounding; the three prior-gap YoY cells and two borderline cells are correctly re-derived and match the deck).
- Adversarial: PASS (three strongest bear counters all already incorporated; none needs grafting).
- Cash-conversion INDETERMINATE handling: correct — capped at PROCEED WITH CAVEATS with missing evidence named (Q1 CFO, receivables, inventory level, net debt, segment note); did not silently resolve to PROCEED (CLAUDE.md rule honoured).
- Monitoring-trigger scoring: verified — 2 GREEN (#3, #13), 0 RED, 18 UNSCORABLE; no balance-sheet-dependent trigger scored off absent data; TTM EBIT #19 informational value recomputed (446.9) matches.

**VERDICT: COMPLETE.** Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "pacedigitk"
quarter: "q1fy27"
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
