# A5 ADVERSARY / COMPLETENESS AUDIT — ECOSMOBILITY Q1 FY27 (MERGED REVIEW)
## Target: review_full_ecosmobility_q1fy27.md (Role 4 + Role 5, results + press release + investor presentation)
## Auditor context: fresh. Re-derived independently from A1 extracts + A2 ledgers + the two verified supplements; A4's and A3's cites checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF (review §8): all four parts present and non-empty with real, provenance-labelled content.
- 8.1 Summary narrative — **PRESENT** (single dense para, ~25 lines; numbers first; carries the trigger verdict, the cash floor, the withdrawn guidance, the one-number-to-watch). Non-placeholder.
- 8.2 Sector intelligence — **PRESENT** (4 bullets; each source-tagged "this quarter's …" vs "Notion/prior-work").
- 8.3 Business-model intelligence — **PRESENT** (4 bullets; unit economics, balance-sheet model, drift signals, provenance-tagged).
- 8.4 Competition intelligence — **PRESENT** (3 bullets; where-it-wins / structurally-weaker / risk-to-watch, provenance-tagged).

Gate 0 = PASS. All four labelled parts present, all three provenance-labelled intelligence blocks carry real content.

Also confirmed present as required deliverables:
- "What the new docs add" section (§2, blocks 2a–2d) — PRESENT and complete (6-yr history, FY26 BS, KPIs, strategic/outlook).
- Role 5 credibility grade (§3, "C (Mixed)") — PRESENT.
- Role 5 claims-vs-evidence table (§3 Step 7A) — PRESENT (8 claim rows, each adjudicated CORROBORATED / UNCORROBORATED / CONTRADICTED).

---

## AUDIT 1 — COVERAGE

### 1a. Fresh enumeration vs A2 ledgers

| Category | A2 count | My fresh count | Method | Orphan/extra | Status |
|---|---|---|---|---|---|
| Deck slides (PDF pages) | 28 | 28 | `grep -c ^\[page ` | none | MATCH |
| Deck chart panels | 20 | 20 | `grep -c ^\[CHART` | none | MATCH |
| Deck balance-sheet totals (subtotals+grand) | 8 | 8 | grep on Total-rows L301–348 | none | MATCH |
| Results notes | 6 | 6 (read L192–210) | paragraph sweep | none | MATCH |
| Results P&L line-items (S+C) | 54 | 54 (23 std + 31 consol) | read L84–172 | none | MATCH |
| Results agenda items | 5 | 5 (L34–50) | read | none | MATCH |
| Results auditor paras | 10 | 10 (incl. unnumbered SEBI-circular para L333–335) | read | none | MATCH |
| Annexure-B / Annexure-C | 10 / 7 | 10 / 7 | read L371–451 | none | MATCH |
| Consolidation entities (results spine) | 0 (OCR-lost) | 0 in spine; 5 in verified supplement | supplement L106–114 | resolved by supplement, not an orphan | MATCH |
| New-docs combined units | 257 (47 PR + 210 deck) | reconciles (28 cat count-test `gate_a2: pass`) | spot-verified | none | MATCH |

The FY25 balance-sheet cross-foot (Total assets 3,414.02 vs Total equity+liab 3,414.20, a ₹0.18 Mn `02↔20` transposition) is confirmed by my own grep (L317 vs L348) and is correctly carried as A3 F14-01 BENIGN. Not an orphan.

No row appeared in my fresh pass that the ledgers lack. No ledger row is absent from the ledgers' own reconciliation. **A2 enumeration verified — no loop-back to A2.**

### 1b. A3 findings → A4 incorporation (all 23 across both forensics files)

Results forensics (11): F1-01 (§1B fn), F2-01 (§4.5), F2-02 (Step 6C / Q1,Q2 / TW1), F6-01 (Q4/Q8/§2d), F8-01 (§2b / Q11), F13-01 (§2d / Q4,Q5), F13-02 (§7 monitorable / Annexure-C), F13-03 (Q5 / monitorables), F14-01 (§2 note / Q6), F15-01 (§2c / thesis "REBUTTED" / Q3), F15-02 (§4.5 / Q7). All cited.

New-docs forensics (12): F1-01 (§2d / Q12), F6-01 (§2d), F7-01 (Role 5 §6 / Q10), F8-01 (§2b / Q11), F13-01 (§2d), F14-01 (§2 "no number games; ties exactly" — benign, addressed at the level A3 assigned), F16-01 (§2d / Q10 / Role 5 Step 2), F16-02 (Role 5 Step 7A / Q1), F16-03 (§2c / Q9), F16-04 (§2c / Q9), F16-05 (§2c / thesis / monitorables), F16-06 (§2c / thesis / Q3). All cited.

Every one of the 23 findings is cited or reviewed in A4. **No orphaned forensic finding — no loop-back to A3.**

### 1c. Management-question coverage of FORWARD-SIGNAL / AMBIGUOUS findings (A4 §6 contract test)

A4 §6 states verbatim: "Every A3 FORWARD-SIGNAL and AMBIGUOUS finding (both forensics files) generates at least one row." I mapped every FS/AMBIGUOUS finding to A4's 12-question table:

- Results FS: F2-02→Q1/Q2 ✓ · F6-01→Q4/Q8 ✓ · F13-01→Q4/Q5 ✓ · F13-03→Q5 ✓ · F15-01→Q3 ✓
- Results AMBIGUOUS: F14-01→Q6 ✓ · F15-02→Q7 ✓
- New-docs FS: F6-01 ✓ · F7-01→Q10 ✓ · F13-01→Q5 ✓ · F16-01→Q10 ✓ · F16-03→Q9 ✓
- New-docs AMBIGUOUS: F1-01→Q7/Q12 ✓ · F8-01→Q11 ✓ · F16-02→Q1 ✓ · F16-04→Q9 ✓ · **F16-05 → NO QUESTION ROW ✗**

**GAP FOUND.** F16-05 (long-standing >5yr customer revenue share drifting 61%→55%→51% across FY25/FY26/Q1FY27; classified AMBIGUOUS in new-docs forensics) is the one FORWARD-SIGNAL/AMBIGUOUS finding with **no management-question row**, despite A4's own §6 universal contract. Q9 does not cover it — Q9 is scoped to revenue-per-trip and the ETS/CCR service-line mix (F16-03/F16-04), a distinct signal from customer-tenure concentration. F16-05 IS otherwise reviewed (narrative §2c, thesis reconciliation, monitorables/catalyst list), so it is not an orphan for citation purposes — but A4's stated "every … generates at least one row" claim is falsified, and a live quality-softening signal reaches management-channel with no question attached.

This is an A4 deliverable defect (additive fix), not an A2/A3 defect.

---

## AUDIT 2 — ARITHMETIC (re-derived from raw deck balance sheet + KPIs + filing; ₹ Mn unless noted)

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Liquid assets (gross) | ₹1,376.79 Mn / ₹137.68 Cr | 241.88+69.86+1,060.79+4.26 = 1,376.79 | deck L308,309,306,297 | MATCH |
| Borrowings (total) | ₹0.11 Cr (1.07 Mn) | current 1.07 + non-current nil = 1.07 | deck L338,331 | MATCH |
| Net cash ex-lease | ~₹137.6 Cr | 1,376.79 − 1.07 = 1,375.72 Mn = 137.57 Cr | derived | MATCH (~137.6) |
| Debtor days (FY26 basis) | ~48 | 365×1,070.21/8,081.58 = 48.34 | deck L308(recv), L132(rev) | MATCH |
| Fresh provisions FY26 vs FY25 | +₹1.98 Cr (<₹3 Cr) | (73.19+21.17) − (55.54+19.03) = 94.36 − 74.57 = 19.79 Mn = 1.98 Cr | deck L333,342 | MATCH |
| Revenue-per-trip change | ~−8% | (1.167/1.27) − 1 = −8.1%; 2,113.72/1.48 = ₹1,428 vs 1,811.19/(1.48/1.27) = ₹1,554 | PR L128,141 | MATCH |
| 6-yr EBITDA margin series | 15.2/12.3/16.5/16.2/14.1/11.6% | EBITDA÷rev: 157/1038=15.1; 181/1473=12.3; 697/4227=16.5; 900/5544=16.2; 924/6540=14.1; 939/8082=11.6 | deck L371–372 | MATCH |
| 6-yr ROCE series | 9.1/19.1/40.9/42.9/35.78/29.4% | company-printed (not independently derivable w/o capital employed); reproduced exactly | deck L380 | MATCH (faithful reproduction) |
| Consol EBITDA excl OI Q1FY27 | ₹21.848 Cr (218.48 Mn) | 2,113.72 − (1,587.29+0+0+237.63+70.32) = 218.48 (deck bar 218.47, rounding) | filing L132–142 | MATCH |
| Consol EBITDA margin Q1FY27 | 10.34% | 218.48/2,113.72 = 10.34% | derived | MATCH |
| Consol PAT margin Q1FY27 | 6.88% (÷rev) / 6.76% (÷total income, deck) | 145.50/2,113.72 = 6.88%; 145.50/2,151.20 = 6.76% | filing L160,132,134 | MATCH (both denominators correct, labelled) |
| Reported EBITDA margin Q1FY27 | 12.11% ÷rev / 11.90% ÷total income | (191.64+61.55+2.77)=255.96; ÷2,113.72=12.11%; ÷2,151.20=11.90% | filing L144,141,140 | MATCH |
| Reported EBITDA margin Q4FY26 | 13.43% / 13.20% | (196.53+79.43+1.75)=277.71; ÷2,067.60=13.43%; ÷2,103.78=13.20% | supp L51; filing | MATCH — confirms Q4FY26 resets any 3-Q sub-12% run |
| Core PBT ex-OI YoY (consol) | −2.39% | (191.64−37.48)/(186.68−28.75) − 1 = 154.16/157.93 − 1 = −2.39% | filing L132,133 | MATCH |
| Consol ETR YoY | 28.82% → 24.08% | 53.81/186.68=28.82%; 46.14/191.64=24.08% | filing L146–148,144 | MATCH |
| PAT bridge YoY | +1.263 Cr = −0.007−0.325−0.045+0.873+0.767 | pretax legs sum to PBT Δ +0.496 Cr; tax leg residual +0.767; total +1.263 (=145.50−132.87) | filing | MATCH (internally consistent) |
| Three-doc tie (EBITDA/margin/PAT) | ties across filing, PR, deck | Q1FY27 218.47/10.34%/145.50/6.76% identical PR L113–117, deck p9 L264/L270, filing 218.48 (rounding) | all three | MATCH |

**No arithmetic mismatch above rounding.** The only inter-document numeric disagreements (PR EBITDA Q1FY26 219.18 vs deck 218.55; PR PAT-margin Q4FY26 7.48% vs deck 7.22%; total-income YoY 16.91% vs 16.92%; FY25 BS cross-foot ₹0.18 Mn; deck-p8 PAT bar +10.28% vs +9.50%) are all confined to comparative-period / rounded-bar cells, none touches a current-quarter figure, and all are correctly adjudicated BENIGN by A3 (F14-01 both files). A4's arithmetic re-derivations are sound. **No loop-back to A4 on arithmetic.**

---

## AUDIT 3 — ADVERSARIAL READ

Task-directed adversarial checks (1)–(6):

**(1) Is the Role 5 grade C (Mixed) defensible? — YES, defensible; neither overstated nor understated.**
Bear case for a harsher D: two forward/quality claims ("disciplined profitable growth", "improving operating efficiency") are contradicted by the company's own 6-yr chart, and three load-bearing guidance items (13–15% EBITDA, 8.5–10% PAT, FY28 ₹1,000–1,200 Cr) were dropped from writing. Bull case for a softer B: disclosure is genuinely thorough (full FY26 BS, 6-yr history, openly disclosed realisation drop, every current-quarter figure ties, no number-hiding), and promoter voice is candid. C sits exactly between: trust the disclosed numbers, discount the forward margin narrative 30–50%. The counter that it should be D does NOT survive — there is no evidentiary evasion or number-hiding; the gap is framing optimism, correctly labelled "narrative-ahead-of-numbers, drifting EVASIVE on margin, NOT Overpromiser." A4 correctly held durable Management Grade at B and Promoter Verdict TRUSTWORTHY pending a scored trailing-4 concall record (conservative, not over-reactive to one no-transcript quarter). SOUND.

**(2) "Asset-light-drift REBUTTED" vs MITIGATED-PENDING? — the label overstates; MITIGATED-PENDING is the more precise word.**
The evidence is only the group-level 5% owned / 95% vendor mix; the Ecos Fleet Management WOS's own gross block / capex is NOT disclosed. The 5/95 group ratio disproves a *material whole-model* drift, but a subsidiary could accumulate owned vehicles while the group ratio stays low against a large vendor base — so the specific F15-01 concern (the WOS gross block) is mitigated, not closed. **Verdict: this counter SURVIVES on the letter of the label** — but it is already SUBSTANTIVELY INCORPORATED in A4: the §5 thesis table and every flag append "WOS gross block still unshown → residual question," Q3 keeps the WOS gross-block question live, and the monitorables list carries "rebutted by 5/95 mix, not closed." Because the qualifying evidence, the open question, and the monitorable are all already present, the analytical content is complete; the fix is a one-word header softening (REBUTTED → MITIGATED-PENDING) for internal consistency with A4's own body. Recommended amendment, not a gate failure.

**(3) Was the thesis-break trigger carried forward UNCHANGED, without silent re-firing OR silent softening? — YES, correctly.**
A4 (Step 6C, §5, YAML) states MEASURE-CONDITIONAL / NOT FIRED, carried forward, not re-opened. It does NOT silently soften: margins are flagged prominently as "genuinely soft," actuals BELOW BEAR (10.34% op margin, 6.88% PAT), weight shifted toward Poor. It does NOT silently re-fire: on the LITERAL pre-committed measure (consolidated reported EBITDA margin sub-12% ×3 consecutive), my recompute confirms Q4FY26 = 13.43% ÷rev / 13.20% ÷total income, which unambiguously breaks any 3-quarter run; Q1FY27 is a single borderline quarter (12.11% ÷rev above 12%; 11.90% ÷total income below). Importantly, A4 did NOT defer to A3 results F2-02, which had asserted the sub-12% clock "FIRES" on the Notion operating basis — A4 re-derived on the literal reported measure and named the measure/denominator ambiguity for Keerti rather than adopting A3's firing. That is the correct independent handling. SOUND.

**(4) Are the tripwire RESOLUTIONS correctly scoped to the FY26 balance-sheet basis? — YES.**
Debtor days use FY26 receivables 1,070.21 / FY26 rev 8,081.58; provisions are FY26 vs FY25 year-end; net cash is FY26 year-end (with the PR ₹155.8 Cr as-on-30-Jun-26 quoted separately, not conflated). A4 repeatedly states "All on an FY26 year-end basis; the Q1 quarterly ageing is still undisclosed" (§2b, TW table). Not misrepresented as Q1FY27 quarterly data. SOUND.

**(5) Is cash conversion still correctly INDETERMINATE, not silently resolved by the balance-sheet cash? — YES.**
Step 5, §2b, Tripwire 6 and the YAML all hold CFO/PAT INDETERMINATE ("no cash-flow statement in filing OR deck; does not resolve silently to PROCEED; resolves at FY26 AR / Q2"). The balance-sheet cash floor is used only for the leverage/net-cash tripwire, never to infer cash conversion; the working-capital build (receivables +₹24.3 Cr, payables +₹16.4 Cr) is noted as unresolvable to a ratio. This honours the CLAUDE.md NEVER rule. Minor observation for the orchestrator: A4's protocol_verdict is "PROCEED WITH FLAGS" while CLAUDE.md says INDETERMINATE cash conversion "caps at PROCEED WITH CAVEATS"; the anti-silent-resolution intent is satisfied (cash conversion is explicitly named and flagged, verdict is not clean PROCEED), but Keerti/orchestrator should confirm PROCEED-WITH-FLAGS is treated as at-least-as-qualified as PROCEED-WITH-CAVEATS. Not an A5 gate item; noted.

**(6) Any A3 forward-signal/ambiguous finding without a management question? — YES: F16-05.** See Audit 1c. This is the single actionable defect. (All other 16 FS/AMBIGUOUS findings map to at least one question row.)

### The three most-positive A4 claims, strongest bear counter, survival

1. **"Balance-sheet floor confirmed — net cash ₹137.6 Cr, clean."** Bear counter (from the same extract): the figure is FY26 year-end; with no cash-flow statement and a visible working-capital build (receivables +₹24.3 Cr, payables +₹16.4 Cr), the "clean cash" can coexist with weak cash conversion, and the ₹155.8 Cr June figure is gross cash+investments, not net of a growing payables cycle. **Survives — but already incorporated** (A4 keeps cash conversion INDETERMINATE and names the WC build). No graft required.

2. **"Asset-light-drift REBUTTED (5/95 mix)."** Bear counter: WOS gross block undisclosed; group ratio can mask sub-level owned-fleet accumulation → status should be MITIGATED-PENDING. **Survives on the label — substantively incorporated** (residual question + monitorable + "not closed" already in body). Recommended one-word softening; not gate-failing.

3. **"Volume-growth leg INTACT (revenue +16.7%, trips +27%)."** Bear counter: growth arrives at −8% realisation, flat absolute EBITDA, and *diluting customer stickiness* (>5yr revenue share 61→55→51%); "intact volume" masks deteriorating unit economics. **Survives.** The profitless-growth and realisation legs are fully incorporated; the *stickiness-drift* leg (F16-05) is narratively incorporated BUT lacks its management-question row (Audit 1c) — this is the concrete unincorporated edge that must be closed by A4.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

**Exact gap:** New-docs forensic **F16-05** — long-standing (>5yr) customer revenue-share drift 61%→55%→51% (FY25/FY26/Q1FY27), classified AMBIGUOUS by A3 — is the one FORWARD-SIGNAL/AMBIGUOUS finding with **no row in A4's §6 management-questions table**, contradicting A4's own §6 contract that "Every A3 FORWARD-SIGNAL and AMBIGUOUS finding … generates at least one row." The finding is otherwise reviewed (§2c, §5 thesis, monitorables), so the remediation is additive and narrow: add one management-question row, e.g. — *"The >5yr-customer revenue share fell 61%→55%→51% over FY25/FY26/Q1FY27 while the absolute ₹Mn base kept rising. Is this legacy-client attrition or faster dilution by newer, lower-yield clients, and does it signal retention/pricing pressure that compounds the realisation decline?"* (from F16-05, Category C/E). No re-derivation and no other section is affected.

Secondary (non-gating) recommendations for the same A4 pass, safe to fold in: (i) soften the §5/flag header word "REBUTTED" to "MITIGATED-PENDING" on the asset-light-drift row to match A4's own "WOS gross block still unshown / not closed" body language; (ii) orchestrator to confirm "PROCEED WITH FLAGS" satisfies the INDETERMINATE-cash-conversion "caps at PROCEED WITH CAVEATS" rule.

All other gates PASS: plain-language brief complete (4/4), coverage of all 23 forensic findings and all A2 ledger rows verified with an independent grep pass (no orphans, nothing missing from ledger), and every derived metric re-derived from raw numbers with zero mismatch above rounding.

```yaml
stage: A5-adversary
company: "ECOSMOBILITY"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Asset-light-drift REBUTTED via 5% owned / 95% vendor mix", counter: "Only the group-level mix is shown; the Ecos Fleet Management WOS gross block/capex is undisclosed, so a sub could accumulate owned fleet while the group ratio stays low — status should read MITIGATED-PENDING, not REBUTTED. Substantively already incorporated (residual question + monitorable); recommend one-word header softening.", source_line: "deck p20 L601 (5/95 mix); WOS gross block NOT FOUND; review §5 / flags / Q3"}
  - {claim: "Volume-growth leg INTACT (revenue +16.7%, trips +27%)", counter: "Growth arrives at -8% realisation, flat absolute EBITDA, and diluting >5yr-customer stickiness (61->55->51%); the stickiness-drift leg (F16-05) is narratively present but has no management-question row.", source_line: "PR L128/L141/L155-156; deck p25 L709-710"}
loop_back_to: "A4"
gap: "New-docs forensic F16-05 (long-standing >5yr customer revenue-share drift 61%->55%->51%, AMBIGUOUS) has no row in A4's Section 6 management-questions table, breaking A4's own stated contract that every FORWARD-SIGNAL/AMBIGUOUS finding generates at least one question row. Finding is otherwise reviewed (Section 2c, thesis, monitorables); fix is additive — add one F16-05 management-question row. Secondary non-gating: soften asset-light 'REBUTTED' header to 'MITIGATED-PENDING' to match body; confirm PROCEED-WITH-FLAGS honours the INDETERMINATE-cash-conversion PROCEED-WITH-CAVEATS cap."
```
