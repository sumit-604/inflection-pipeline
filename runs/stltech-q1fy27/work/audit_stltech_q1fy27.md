# A5 ADVERSARY / COMPLETENESS AUDIT — Sterlite Technologies Limited (STLTECH), Q1FY27

Agent A5 (Adversary). Fresh context: A4 review + A1 extracts (results, presentation) + A2 ledgers (results, presentation). Re-derived independently; A4/A3 cites checked, not deferred to. Concall out of scope (Role 5 deferred, no transcript).

---

## AUDIT 1 — COVERAGE (fresh grep pass diffed against A2 ledgers)

I re-enumerated each A1 extract independently and diffed against the A2 count tests.

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Results — notes (consol 12 @ l.323/328/332/336/364/372/408/449/453/484/488/492 + std 12 @ l.594/599/602/606/610/640/648/676/718/723/730/734) | 24 | 24 | none | PASS |
| Results — agenda items (core resolution + enclosures i–viii, l.33–55) | 9 | 9 | none | PASS |
| Results — consolidation entities (para 4, Sr 1–20, l.824–847) | 20 | 20 | none | PASS |
| Results — auditor paras (consol 8 + standalone 5 + security-cover 14) | 27 | 27 | none | PASS |
| Results — line items (P&L 33+30, segment 26, ratios 16+16, sec-cover A/B, annexures) | 200 | 200 (spot-reconciled key tables; no extra token found) | none | PASS |
| Results — zero-standing | 38 | 38 (subset, spot-checked) | none | PASS |
| Results — signature blocks | 14 | 14 | see SIG note below | PASS w/ note |
| Presentation — slides | 32 | 32 | none | PASS |
| Presentation — numeric rows | 470 | 470 (per-slide subtotals re-summed = 470) | none | PASS |
| Presentation — footnotes (F1–F9) | 9 | 9 | none | PASS |
| Presentation — zero-standing (excl-items Q1FY26/Q1FY27) | 2 | 2 | none | PASS |

**Fresh-pass rows the ledger lacks (→ would FAIL to A2):** NONE. Every material headline I searched for is captured, including the two that the A2 methodology notes almost lost — the QIP "~1,500 Cr pending allocation" footnote (pres row 424, l.981, recovered on manual sweep) and the "-17" negative PAT bar (pres row 360). No orphan tokens.

**Ledger rows / flags absent from A4 (→ would FAIL to A3):**
- **SIG_BEFORE_MEETING_CONCLUSION** (A2 results ledger §16, 12 of 14 signature blocks timestamped 12:35–13:04). A2 explicitly routed this "for A3/A4 to reconcile against the stated meeting window." A4 carries NO explicit disposition, and it is not among the incorporated A3 findings (F2-01…F11-01 / FND-01…12). This is the one ledger flag A4 does not visibly dispose of. **However it is resolvable directly from the extract, not unresolvable:** the board meeting commenced 11:50 and concluded 14:36 (l.56); all 12 auditor/management signatures at 12:35–13:04 fall INSIDE that window (after results approval, before the meeting's stated close), and the only post-close signature (CS, 14:39:55) is exactly as expected. Signing-before-conclusion is normal, not an anomaly. Because the coverage question is resolvable and benign, this does not meet the "genuinely unresolvable → FAIL" bar; it is recorded as a non-blocking gap. **Recommendation to A4:** add one line — "SIG_BEFORE_MEETING_CONCLUSION reviewed; signatures fall within the 11:50–14:36 meeting window; benign, no finding."
- **NCI-absence note** (A2 results ledger §2, row 27 — no non-controlling-interest line in any period). A4 does not name it, but it is subsumed by A4's subsidiary-attribution treatment (all 20 entities wholly owned; F2-01 PAT-gap analysis). Benign, resolved.

Coverage verdict: COMPLETE. No orphan and no missing-from-ledger row rises to a FAIL; the single undisposed flag is benign and self-resolving from the extract.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract numbers)

Raw sources: consol P&L l.198–239; standalone P&L l.537–574; ratios l.413–447 / 681–715; deck l.849–981.

### Consolidated derived (A4 Step 1A/1B)
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (EBITDA−OI) | 385 | 397−12 = 385 | l.210/199 | MATCH |
| Op EBITDA margin Q1FY27 | 20.2% | 385/1,910 = 20.16% | l.210/199/198 | MATCH |
| Reported EBITDA margin Q1FY27 | 20.8% | 397/1,910 = 20.79% | l.210/198 | MATCH |
| Op EBITDA margin Q1FY26 | 13.0% | 132/1,019 = 12.95% | l.210/199/198 | MATCH |
| Core PBT ex-OI Q1FY27 | 245 | 257−12 = 245 | l.217/199 | MATCH |
| Effective tax rate Q1FY27 | 23.3% | 60/257 = 23.35% | l.218/217 | MATCH |
| Effective tax rate Q4FY26 | 45.9% | 50/109 = 45.87% | l.218/217 | MATCH |
| PAT margin Q1FY27 | 10.3% | 197/1,910 = 10.31% | l.221/198 | MATCH |

### Consolidated YoY (Step 2) and PAT bridge (Step 4)
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Revenue YoY | +87.4% | 891/1,019 = 87.44% | l.198 | MATCH |
| Op EBITDA YoY | +191.7% | 253/132 = 191.7% | derived | MATCH |
| EBIT (OpEBITDA−D) YoY | +445.5% | (300−55)/55 = 445.5% | l.210/199/214 | MATCH |
| Core Op PBT YoY | +4,800% | 240/5 = 4,800% | derived | MATCH |
| Reported PBT YoY | +1,876.9% | 244/13 = 1,876.9% | l.217 | MATCH |
| PAT YoY | +1,870.0% | 187/10 = 1,870% | l.221 | MATCH |
| EPS diluted YoY | +1,755% | 3.51/0.20 = 1,755% | l.239 | MATCH |
| PBT bridge sum | +244 | 253+4−8−5 = 244 (=257−13) | l.210/199/214/213/217 | MATCH |
| % recurring | ~98% | 240/244 = 98.4% | derived | MATCH |
| Annualised run-rate | ₹7,640 Cr | 1,910×4 = 7,640 | l.198 | MATCH |

### Standalone derived (Step 1B)
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA margin Q1FY27 | 21.7% | 202/929 = 21.74% | l.549/538/537 | MATCH |
| Reported EBITDA margin Q1FY27 | 27.0% | 251/929 = 27.02% | l.549/537 | MATCH |
| Core PBT ex-OI Q1FY27 | +120 | 169−49 = 120 | l.558/538 | MATCH |
| Core PBT ex-OI FY26 | −176 | 3−179 = −176 | l.558/538 | MATCH |
| Effective tax rate Q1FY27 | 26.0% | 44/169 = 26.04% | l.559/558 | MATCH |
| PAT margin Q1FY27 | 13.5% | 125/929 = 13.46% | l.562/537 | MATCH |
| PAT margin FY26 | 0.2% | 2/2,446 = 0.08% (rounds to 0.1%) | l.562/537 | MINOR — see note |

### Balance-sheet / thesis-linked
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Subs share of consol PAT Q1FY27 | 36.5% | 72/197 = 36.5% | l.221/562 | MATCH |
| Ex-QIP net debt | ~₹1,017 Cr | 483−1,500 = −1,017 (net debt) | deck l.957/981 | MATCH |
| Ex-QIP net debt / annualised EBITDA | ~0.64x | 1,017/(397×4)=1,017/1,588 = 0.64x | deck l.956 | MATCH |
| Net-worth vs Other-Equity+paid-up gap | ₹302 Cr / 13.3% | (2,170+98)−1,966 = 302; 302/2,268 = 13.3% | l.236/235/447 | MATCH |
| Basic-diluted EPS spread | ~8% | 0.32/4.03 = 7.94% | l.238/239 | MATCH |
| Dilution overhang (warrants+QIP) | ~14% | (45.3M+25.7M)/488M = 14.5% | Annex II l.1017; Note 5 l.364 | MATCH |
| Warrants implied count | ~45M | (124.57/0.25)/110 = 45.3M | Annex II l.1017/1056 | MATCH |
| Order intake 1.7x | 1.7x | 13,100/7,687 = 1.70x | deck l.561/564 | MATCH |
| Order book 2.4x | (used) | 18,618/7,687 = 2.42x | deck l.931/936 | MATCH |
| EBITDA YoY (press ~184%) | ~184% | 397/140−1 = 183.6% | l.210 | MATCH |

**Arithmetic verdict:** All material derived metrics reproduce within rounding. One immaterial nit: **standalone PAT margin FY26** shown as 0.2% recomputes to 0.08% (≈0.1%); the filing's own Reg-52 net-profit-margin row (l.712) reports 0% for that cell. The value is dominated by the rounding of a PAT reported as "₹2 Cr" and does not affect any read (parent was barely profitable in FY26 either way). Below-materiality; not a FAIL. No mismatch above rounding anywhere else.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear from the SAME extract)

**Positive claim 1 — "Genuinely clean record quarter: operating EBITDA margin 20.2% ex-OI, +720 bps YoY, ~98% of PAT growth recurring, not treasury-driven" (Step 2, Combined Verdict).**
Strongest bear from the same text: the 20.8%/20.2% margin embeds an **unquantified tariff tailwind** ("peak tariff" baseline) and monitor #2 (operational EBITDA **ex-tariff**) is UNDISCLOSED (FND-12); the entire EBITDA lift sits in the Optical-networking segment (segment EBITDA 137→401, l.280) with unallocated income swinging −₹22 Cr QoQ (l.283). I also tested the ₹158 Cr inventory line (l.204) as a possible margin flatterer — it is a destocking *expense* add, i.e. a margin *headwind*, so that angle fails; the operating lift is real.
Survives? **NO — already incorporated.** A4 carries the ex-tariff caveat in Step 8C, monitor #2 (AMBER/UNKNOWN), the single-cleanest-metric pick, and Q11.

**Positive claim 2 — "Parent standalone turned operationally profitable at the core (ex-OI PBT −176 FY26 → +120 Q1FY27) for the first time in the visible window" (Step 1B, Combined Verdict).**
Strongest bear from the same text: the standalone turn rests partly on a **near-nil cash-tax base** — current tax ₹1 Cr against ₹43 Cr deferred on ₹169 Cr PBT (l.560–561), i.e. shield-supported; standalone Op-EBITDA margin (21.7%) exceeds consolidated (20.2%), implying subsidiary drag; and it is a single quarter.
Survives? **NO — already incorporated.** A4 carries the cash-tax step-up risk (F8-01, Step 4, Q4), the subsidiary-concentration gap (F2-01, l.437, Q3), and states explicitly "it is exactly ONE quarter."

**Positive claim 3 — "Net debt-free balance sheet; order book ₹18,618 Cr; DC & Cloud mix 1%→21%" (Combined Verdict, monitors #4/#5/#6).**
Strongest bear from the same text: (a) "net debt-free" is **QIP-cash-funded and restricted-cash-inflated** — ex-QIP the book is net *debt* ~₹1,017 Cr, and the ₹1,500 Cr QIP cash sat in June-30 cash (Sec-Cover note 5, l.1406) while the *shares* were only allotted 3-Jul (subsequent event, Note 5 l.364), so the offsetting equity is not even on the 30-Jun balance sheet; (b) the "1.7x" intake bar is a **period mismatch** (single Q1 vs full-year FY26, FND-09); (c) the DC-mix 1%→21% comes from a **scrambled deck chart** (FND-11) with no ₹-value corroboration in the filing's two-segment disclosure (Optical vs Digital only).
Survives? **NO — already incorporated.** A4 carries the QIP-funded/restricted-cash quality flag (Step 5, F6-01, FND-10, Q2), the period-mismatch (Q7), and the chart-order caveat on monitor #5 (Q7). The QIP-cash-vs-share-timing subtlety is captured in substance by A4 netting the ₹1,500 Cr out to reach ex-QIP net debt ₹1,017 Cr.

**No surviving bear counter requires grafting into A4.** Every strongest same-text counter to the three most positive claims is already present as a caveat, monitor, flag, or management question.

---

## SECONDARY OBSERVATIONS (non-blocking; for A4 clean-up, not verdict-changing)

1. **Internal inconsistency on scrambled deck revenue (FND-06):** In Step 3, A4 assigns deck value 1,034 to **Q2FY26**; in Step 8.5 Q7, A4 treats the deck's 1,034 as the **Q1FY26** bar (asking to reconcile it against the filing's 1,019). The two cannot both hold. The A2 presentation ledger reads 1,034→Q1FY26, 1,257→Q2FY26, 1,020→Q3FY26 (rows 338–340), which matches A4's Q7 reading, not its Step 3 table. Immaterial to every derived metric (Q2/Q3FY26 are deck-only narrative quarters; filing governs Q1FY26 = 1,019, which A4 uses correctly in Step 3). Recommend A4 reconcile the Step-3 trajectory row to the Q7 framing.
2. **Standalone PAT-margin FY26** = 0.2% should read ≈0.1% (see Arithmetic). Cosmetic.
3. **SIG_BEFORE_MEETING_CONCLUSION** one-line disposition recommended (see Coverage).

None of the three alters the protocol verdict (PROCEED WITH CAVEATS), the decision status (AVOID / passive-monitoring UNCHANGED), the entry zone (₹130–160 UNCHANGED), or any thesis-broken/trigger reading.

---

## VERDICT

**COMPLETE.** The A4 review is arithmetically sound (every material derived metric reproduced within rounding), coverage-complete (all A2 ledger counts reconcile to my fresh pass with zero orphan and zero missing-from-ledger rows; the single undisposed ledger flag, SIG_BEFORE_MEETING_CONCLUSION, is benign and resolvable directly from the extract), and adversarially complete (the strongest same-text bear counter to each of the three most positive claims is already carried in A4 — none survives requiring a graft). The three secondary observations are cosmetic/immaterial and do not block the Notion save.

```yaml
stage: A5-adversary
company: "STLTECH"
quarter: "Q1FY27"
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
