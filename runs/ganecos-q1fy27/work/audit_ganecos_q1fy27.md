# A5 ADVERSARY / COMPLETENESS AUDIT — Ganesha Ecosphere (GANECOS) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (A4 review + A1 extracts + A2 ledgers only; A3 reasoning not seen, cites re-derived).
Re-audit scope: THREE documents (Reg 33 results filing + Reg 30 board outcome + Q1 FY27 investor deck, 34 slides). Filing in Rs Lakh (x0.01 to Cr); deck already Rs Cr.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs the three A2 ledgers)

I re-swept each extract and diffed my fresh counts against each ledger's COUNT TEST, then checked every ledger category is cited in A4 or blanket-marked reviewed.

| Category | Ledger count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| **Results** notes (std 7 + consol 6 + 1 unnumbered ESOP footnote) | 14 | 14 (std notes L101-113 = 7; consol L249-260 = 6; ESOP footnote L261-264 = 1) | none | PASS — in review 0D notes table + auditor check |
| Results line items (std 31 + consol 33) | 64 | 64 (every substantive P&L row present in review Step 1 std/consol tables) | none | PASS |
| Results zero-standing (B(i)/B(ii) OCI, both statements) | 4 | 4 (std rows 24-25 L83/L86; consol rows 26-27 L231/L234; nil all periods) | none | PASS — retained, acknowledged in preamble ("4 zero-standing rows… all reviewed") |
| Results auditor paras (std 4 + consol 11) | 15 | 15 (std unnumbered prose 4; consol 1-11, incl. Other-Matter 7-10) | none | PASS — 0D auditor check + Step 4A cite paras 7-10 |
| Results consolidation entities | 6 | 6 (parent, Ecopet, Ecotech, Nepal, Trust, Recycling Chain assoc; L319-335) | none | PASS |
| Results agenda items (cover letter) | 4 | 4 (results approval + 2 enclosures + meeting-time) | none | PASS |
| **Board outcome** agenda item | 1 | 1 (SVP re-appointment L19-23) | none | PASS — governance section |
| Board outcome annexure particulars | 4 | 4 (reason, date/term, profile, relationship — L53-75) | none | PASS |
| Board outcome related-party facts | 2 | 2 (son of EVC; MD of Ganesha Ecoverse) | none | PASS — Q6/Q7, A3-F13-01/02 |
| Board outcome meeting-time / signatory / regulatory refs | 2 / 1 / 2 | 2 / 1 / 2 | none | PASS — A3-F14-03 covers signature timestamp 20:02:11 |
| **Presentation** slides | 34 | 34 ([page N] markers L15…L713; 5 OCR tags add no slides) | none | PASS — "all 34 slides reviewed" (aggregate no-finding) |
| Presentation P&L line items (14 consol + 14 std) | 28 | 28 (slide 32 L673-688; slide 33 L694-710) | none | PASS — deck-vs-filing reconciliation table |
| Presentation subsidiaries named | 3 | 3 (Ecopet, Ecotech, Overseas; slide 15) | none | PASS |
| Presentation chart clusters / footnotes / guidance | 45 / 6 / 7 | consistent with Table B/D/E | none | PASS — volume, utilisation, 5-qtr, non-GAAP, guidance all surfaced |

**Fresh-pass rows the ledgers lack:** none. My independent sweep produced no disclosure unit absent from a ledger.
**Orphan rows (ledger present, A4 absent):** none at the ledger-row level. Every enumerated category is either cited or covered by the blanket "all reviewed" for no-finding slides (safe-harbour, vision, awards, industry/EPR, growth drivers, GoRewise, ESG, dividers).

**Coverage observations (not orphans, flagged for polish — do NOT block save):**
- **OBS-1 (to A4):** Finding ID **A3-F16-04** appears in A4's "findings incorporated" list (review L21) and YAML but has no corresponding discussion anywhere in the body. I cannot adjudicate it as a true orphan because A3's forensic notes are not among my inputs (I see only extracts + ledgers). A4 should either surface A3-F16-04 explicitly or drop it from the incorporation list.
- **OBS-2 (to A4):** Deck finding **A3-F2-02** (standalone OI structural reset, CCPS conversion) is used in Step 2/4 narrative but is not in any management question's "from finding" column. It is EXPLANATORY (management already explained the driver), so a question is defensible-optional, not required. Deck tidiness **A3-F14-01(deck)** (3.53-vs-3.52; un-parenthesised tax) is folded into the disclosure-control cluster and Q14 framing rather than its own question — acceptable as an immaterial NEUTRAL/AMBIGUOUS item.

Coverage verdict: **PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakh cells; x0.01 to Cr)

I recomputed every derived metric, margin, YoY, QoQ, the PAT bridge, the S-to-C gap ladder, and every deck-vs-filing reconciliation line from the source cells. Representative checks (all remaining metrics reconciled identically):

| Metric | A4 value | My recompute (from raw) | Source line | Status |
|---|---|---|---|---|
| Std Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 23.79 | 18.4553+6.8533+1.9990−3.5168 = 23.79 | L70/65/64/55 | ✓ |
| Std Op EBITDA margin Q1FY27 | 9.07% | 23.79/262.30 = 9.07% | — | ✓ |
| Std ETR Q1FY26 | 25.5% | 2.6161/10.2790 = 25.45% → 25.5% | L72-73/70 | ✓ (rounds up) |
| Consol Op EBITDA Q1FY27 (V+D+Fin−OI) | 59.78 | 37.1802+17.3425+8.8726−3.6198 = 59.78 | L216/210-211/209/201 | ✓ |
| Consol Op EBITDA margin Q1FY27 | 14.11% | 59.78/423.67 = 14.11% | — | ✓ ties deck 14.1% |
| Consol ETR Q1FY27 | 21.7% | (5.0773+2.9826)/37.0947 = 21.73% | L220-221/218 | ✓ below statutory 25.17% |
| Consol PAT margin FY26 | 2.58% | 38.2135/1481.6629 = 2.58% | — | ✓ |
| Std revenue YoY | +18.4% | 262.30/221.47−1 = 18.44% | L54 | ✓ |
| Consol revenue YoY | +25.7% | 423.67/337.12−1 = 25.67% | L199 | ✓ |
| Consol PAT YoY | +170.0% | 29.0348/10.7536−1 = 170.0% | L222 | ✓ |
| Std core PBT (ex-OI) YoY | +608.4% | 14.9385/2.1089−1 = 608.4% | L70,55 | ✓ |
| Std finance cost YoY | +51.8% | 1.9990/1.3165−1 = 51.84% | L64 | ✓ |
| Std PAT QoQ | −16.2% | 13.75/16.41−1 = −16.2% | L74-75 | ✓ |
| Consol PAT QoQ | +25% (deck bullet) | 29.03/23.21−1 = 25.1% | L222 / s12 L304 | ✓ |
| **Consol PAT bridge** total | +18.27 (ties +18.28) | +22.77 PBT change then −4.50 tax = +18.27 | Step 4 | ✓ ties |
| — Op EBITDA change term | +23.46 | precise 59.7755−36.3145 = 23.461 | — | ✓ (rounded endpoints give 23.47; within tolerance) |
| — Tax change term | −4.50 | (5.08+2.98)−(2.59+0.97)=8.06−3.56 = 4.50 | L220-221 | ✓ |
| **Std PAT bridge** total | +6.09 | 14.49−0.98−0.68−4.65−2.09 = +6.09 | Step 4 | ✓ |
| — Std tax change term | −2.09 | 4.7058−2.6161 = 2.0897 | L72-73 | ✓ |
| **S-to-C gap Q1FY27** | +15.29 (+111%) | 29.0348−13.7495 = 15.285; 15.29/13.75 = 111.2% | Step 4A | ✓ |
| S-to-C gap Q3FY26 (deck) | −16.4 (−103%) | −0.5−15.9 = −16.4; /15.9 = −103% | s10 L245,264 | ✓ |
| Four FY26 quarterly gaps sum | −9.6 (ties FY26 −9.62) | +3.09−3.1−16.4+6.80 = −9.61 | Step 4A | ✓ |
| **Deck non-GAAP Cash Profits** consol Q1FY27 | 46.4 = PAT+dep | 29.03+17.34 = 46.37 → 46.4 | s6 | ✓ reconciles, correctly flagged non-GAAP |
| **Component-auditor PAT share** | ~50.6% | (15.04−0.27−0.09)/29.03 = 50.6% | paras 7/8/10 | ✓ (subs+Nepal+assoc) |

**Deck-vs-filing reconciliation re-derived from cells (verified A4 did NOT let a deck non-GAAP or different-basis figure override a filed number):**
- Deck consol "Cost of materials/traded" 303.52 = filing COGS 297.57 + purchases 5.95 = 303.52 ✓
- Deck consol "Other exp (incl assoc loss)" 71.55 = P&F 34.44 + Other 37.02 + assoc 0.09 = 71.55 ✓
- Deck consol Tax 8.06 = 5.08+2.98 ✓; Std Tax 4.71 = 5.08−0.37 ✓
- Deck consol OCI 1.00 = 0.0153+1.157−0.177 = 0.995 ✓; TCI 30.03 = 29.03+1.00 ✓
- Deck EBITDA 59.8 is the **operating** figure (excl OI), matches derived 59.78 — not a dressed-up number ✓
- Non-GAAP **EBITDA/Ton** (11.6→14.9) and **Cash Profits** (46.4) are explicitly quarantined as non-GAAP, not in the filing, read "with the falling-volume denominator." They do **not** override any GAAP line. ✓

Arithmetic verdict: **PASS.** Every derived metric ties within rounding (<=0.01 Cr / <=0.1 pp). No mismatch above rounding.

Minor methodology note (not a mismatch): A4's "Reported EBITDA" uses PBT-after-associate while "Operating EBITDA" uses PBT-before-associate (line V). The associate term is 0.03-0.09 Cr; immaterial and each series is internally consistent.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to the three most positive claims, from the same text)

**Claim 1 — "Consol PAT +170% YoY; ~100% of the rise is recurring core ops; high P&L quality."**
Bear counter from the same extract: the deck states consolidated **sales volume fell 11.2%** and standalone **13.4%** (s12 L298-299) while production rose 3.8% — the whole top-line gain is realisation/price/mix on a shrinking base; 50.6% of consol PAT rests on component-auditor-reviewed / management-certified entities (paras 7/8/10); the base is volatile (Q3 FY26 consol PAT −0.5 Cr, s10 L245); consol current tax equals standalone current tax, so subs paid ~nil current tax on a loss-carryforward shield (ETR 21.7% < statutory 25.17%) that will step up.
**Survives?** NO. A4 already incorporates every strand — the volume decline (Step 2 diag 1, flag), selective framing (A3-F16-02), Q3 volatility (Step 3/4A), the 50.6% component-auditor share (0D AMBER), the ETR step-up (Step 4, Q3). Nothing to graft.

**Claim 2 — "Pre-registered S-to-C PAT gap swung to +15.29 Cr (+111%); pre-condition (i) met."**
Bear counter: the subsidiary block swung from a −16.4 Cr gap (Q3 FY26) to +15.3 Cr in two quarters — a recently-turned, volatile base; the +15.04 Cr is component-auditor-reviewed, not principal; it coincides with falling volume (price/mix, not utilisation — Warangal still 72%); durability unproven.
**Survives?** NO. A4 states exactly this in Step 4A ("durability the central open question — needs one more clean quarter + FY26 AR") and caps pre-condition (i) as met-on-number-not-durable.

**Claim 3 — "Op EBITDA margin +334 bps YoY (consol) / +487 bps (std) — margin expansion."**
Bear counter: EBITDA/Ton (non-GAAP) is flattered by the falling-volume denominator; the margin gain may be a transient polymer-price/mix effect that reverses if volume recovers only at lower realisation; standalone OI structural reset (9.86→3.52, CCPS conversion) permanently lowers standalone PAT.
**Survives?** NO. A4 flags the denominator effect (A3-F16-02, Step 2 diag 2), makes sustainability the central management question (Q12/Q14), and treats the OI reset as structural (Step 2 diag 3, Step 4).

**Surviving bear counters requiring graft into A4: none.** The review is already symmetric — each positive is paired with its filing-supported bear.

---

## SPECIFIC RE-AUDIT CHECKLIST (task items a–g)

- **(a) Ties to all three ledgers, no orphan/unreviewed unit, zero-standing retained** — PASS. 14 notes / 64+28 line items / 15 auditor paras / 6 entities / 5 board-outcome categories / 34 slides all reconcile; 4 zero-standing OCI rows retained and acknowledged.
- **(b) Deck reconciliation arithmetically correct; no deck non-GAAP or different-basis figure silently overrode the filed number** — PASS. Every combined deck line re-derived to the filed cells; EBITDA/Ton and Cash Profits explicitly quarantined as non-GAAP.
- **(c) Volume −11.2% consol / −13.4% std YoY and Q3 FY26 consol PAT −0.5 Cr are supported by deck line cites (not invented)** — PASS. Volume figures are management's own bullet text s12 L298-299; Q3 −0.5 is the printed PAT bar s10 L245. Both are direct extract cites, not chart-order inferences.
- **(d) Every deck AMBIGUOUS/FORWARD-SIGNAL finding maps to >=1 management question** — PASS with two benign notes (OBS-2): A3-F7-01→Q12, A3-F15-01→Q13, A3-F16-02→Q14, A3-F16-03/A3-F6-01deck→Q15, A3-F6-01deck→Q16, A3-F16-01→Q2, A3-F8-01→Q3, A3-F10-01→Q5. A3-F2-02 (explanatory) and A3-F14-01deck (immaterial tidiness) reasonably folded into narrative/cluster.
- **(e) Net debt not computable; cash conversion INDETERMINATE (deck did not close)** — PASS. No balance sheet in any of the three docs; Step 5 leaves net debt ND and cash conversion INDETERMINATE, caps off a clean PROCEED, names the missing evidence (H1 cash flow + AR balance sheet). Tripwire 3 RED.
- **(f) No NOT FOUND value estimated** — PASS with one traceability flag (OBS-3, below). ND used consistently for EPS share-adjusted, CFO, capex, net debt, ROCE.
- **(g) Decision Status unchanged; no committed trigger** — PASS. WATCHLIST retained (Step 0A/8/verdict/YAML); no committed thesis-broken or growth trigger exists, so none fired; A4 flags, human decides.

**OBS-3 (to A4, pre-save polish, NOT a completeness failure):** the "FY26 combined loss ~Rs 11.20 Cr" for Ecopet+Ecotech (Q1 management question + Step 4A) is **not derivable from any of the three extracts** and carries no source label, unlike A4's other carried-in figures which are tagged "(Notion)". Its direction is corroborated by the filed FY26 S-to-C gap of −9.62 Cr (subs were net-negative contributors), so it is not a fabricated current-period value and does not touch any derived metric, gate, or the verdict. A4 should append the source tag (Notion / prior AR / prior component-auditor figure) or restate as "prior-year loss (per baseline)." Because it is a prior-period directional comparison and not a filled current-statement number, it does not rise to a never-estimate violation that blocks save — it is a labelling fix.

---

## VERDICT

**COMPLETE.** All three audits pass. Coverage reconciles to all three ledgers with no orphan or missing-from-ledger rows; every derived metric, margin, YoY/QoQ, PAT bridge, S-to-C ladder, and deck-vs-filing reconciliation recomputes from the raw Lakh cells within rounding; no bear counter survives unincorporated (A4 is already symmetric); net debt correctly ND and cash conversion INDETERMINATE; no NOT FOUND estimated in the current statements; Decision Status unchanged at WATCHLIST with no committed trigger. Three non-blocking polish notes (OBS-1 A3-F16-04 label, OBS-2 optional question mapping, OBS-3 source-tag the ~Rs 11.20 Cr prior-year figure) are recommended for A4 before save but do not affect completeness or the verdict. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "GANECOS"
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
notes_non_blocking:
  - "OBS-1 (A4): finding A3-F16-04 listed as incorporated but not surfaced in body; label or drop (A3 notes not in A5 inputs, cannot adjudicate as true orphan)."
  - "OBS-2 (A4): A3-F2-02 (explanatory) and A3-F14-01-deck (immaterial tidiness) folded into narrative/cluster rather than own question; acceptable."
  - "OBS-3 (A4): 'FY26 combined loss ~Rs 11.20 Cr' (Ecopet+Ecotech) not in any of the three extracts and unlabelled; direction corroborated by filed FY26 S-to-C gap -9.62 Cr; append source tag before save. Non-blocking (prior-period comparison, not a filled current value; no metric/gate/verdict impact)."
```
