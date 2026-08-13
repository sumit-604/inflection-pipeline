# A3 FORENSIC NOTES — Amagi Media Labs Ltd (AMAGI), Q1 FY27 (results)

Doctype: results filing (Board Outcome + limited-review results S & C + 3 Reg-30 annexures).
Source extract: extract_results_amagi_q1fy27.txt (804 lines, 13 pages, Rs Millions; x0.1 = Rs Cr).
Ledger reconciled: 100% (every A2 ledger row read at its cited line in the A1 extract before judging).
Prior-quarter extract: NONE (first quarterly run; AMAGI listed ~Jan 2026). Prior-quarter diffs marked N.A. with reason.
A2 flags carried in for resolution: ZERO_STANDING (7 rows) -> F1/F8; ENTITY_COVERAGE_GAP -> F4/F15; TEXT_ANOMALY -> F14.

Applicability (per prompt doctype rule): results filing -> F1-F15 apply; F16 (presentation) and F17 (concall) N.A.
F12 N.A. (single reportable segment, no segment tables). F15 diff N.A. (no prior quarterly list).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote (short) | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F1-01 | F1 | Sec4 Current tax/Deferred tax/Total tax (219-221); Sec9 Current tax-India (476) | 219-222, 476, Note 7 @290-293/588-591 | "Total tax expense (IV) [—]" with "Profit/(loss) for the period/year ... 229.71" | FORWARD-SIGNAL | Standalone entity records **zero** total tax on positive PBT in every period; shield = unabsorbed depreciation + carried-forward losses (Note 7). Non-cash-tax status is finite; ETR normalises upward when the shield exhausts. |
| A3-F2-01 | F2 | Sec4 PAT (222) vs Sec9 PAT (480) | 222 / 480 | S PAT "229.71" vs C PAT "339.05"; prior qtr S "196.97" vs C "342.63" | AMBIGUOUS | Subsidiary net PAT contribution FELL to 109.34mn (Q1FY27) from 145.66mn (Q4FY26), -25% QoQ, a 26pp narrowing of the S-vs-C gap as % of standalone PAT (48% vs 74%). Group PAT flat (-1%) while standalone rose +16.6%. Foreign (US-heavy, ~73% rev) sub profitability softened -> A4 question. |
| A3-F4-01 | F4 | Sec7 auditor para 6+7 (391-419) | 391-419 | "total net profit after tax of Rs. 66.00 million ... reviewed by their respective independent auditors" | NEUTRAL-FACT | ~19.4% of consolidated PAT (66.00mn reviewed by other auditors, less 0.25mn truly unreviewed = 65.75mn / 339.05mn) does NOT rest on the principal statutory auditor; ~26.7% of consol revenue (1,166.33mn) likewise. Above 10% PAT threshold. Structural for a global group; no prior quarter to trend YoY. |
| A3-F4-02 | F4 | ENTITY_COVERAGE_GAP (Sec7 note) | 391-419 vs 353-372 | paras 6+7 name "five subsidiaries and a controlled trust" + "three subsidiaries" = 9 | AMBIGUOUS | Entity list (para 4) has 10 non-holding entities; other-matters paras account for review basis of only 9. One non-holding entity's review basis is unstated in the report -> A4 question (likely a directly-reviewed Indian entity, e.g. Amagi AI Pvt Ltd or Argoid Analytics Pvt Ltd, but not stated). |
| A3-F6-01 | F6 | Sec13 Annexure III rationale (694-713) | 707 | "provide greater flexibility for future equity-based capital raising and other permissible equity issuances" | FORWARD-SIGNAL | Enumerated rationale for the MOA reclassification explicitly names future equity raising. Reclassified authorised capital = 49,45,02,731 equity shares vs ~21.63 cr issued -> ~27.8 cr-share headroom. Enabling resolution foreshadows a raise/deployment. Ties tripwire 4 (dilutive/overpriced deployment of ~Rs 1,664 Cr cash) and cash-deployment optionality. |
| A3-F7-01 | F7 | Sec5/Sec10 Note 7 (290-293/588-591) | 291 / 589 | "Considering uncertainty that sufficient taxable profits will be available with the Company in the foreseeable future" | AMBIGUOUS | Pre-emptive note-level hedge: management signals doubt over near-term standalone taxable profits, hence no DTA. Reads against a rising-profit thesis; the loss/unabsorbed-depreciation position is expected to persist "in the foreseeable future" -> A4 question on the runway. |
| A3-F8-01 | F8 | Sec9 Total tax (479) vs PBT (473) | 473-479 | consol tax "65.02" on PBT "404.07"; standalone "Current tax [—]" | FORWARD-SIGNAL | Consolidated ETR ~16.1% (Q1FY27), ~15.5% (Q4), ~17.9% (FY26) vs statutory 25.17%. Gap driven entirely by the Indian holding co paying nil tax; foreign taxes 58.50mn carry the charge. Latent shield ~36.7mn this quarter ≈ **~900 bps** of ETR headroom that reverses as Indian carryforwards exhaust. FY26 carried a one-off deferred-tax CREDIT of 150.70mn (consol). |
| A3-F9-01 | F9 | Sec4/Sec9 Re-measurement DB plans (226/484) | 226 / 484, Note 6 @282-288/579-585 | "Re-measurement (losses)/gains on defined benefit plans (29.86)" | AMBIGUOUS | Single-quarter actuarial OCI loss of (29.86)mn EXCEEDS the entire prior-year FY26 net (+7.21mn) in magnitude -> assumption change (discount rate / plan assets) or Labour-Codes harmonised-wage flow-through into gratuity. Verify assumptions at the Annual Report. Signals higher employee-benefit obligation. |
| A3-F13-01 | F13 | Sec1 agenda 2,3,4 (40-82); Sec12/13/14 | 40, 48, 76, 42/50/78 | "reclassification of Authorised Share Capital ... subject to the approval of the Shareholders at the ensuing Annual General Meeting" | FORWARD-SIGNAL | Board Outcome beyond results carries: (a) capital-raising enabling MOA reclassification (see F6-01); (b) MD/CEO Baskar Subramanian re-appointed Dec-1-2026 to Nov-30-2031, promoter continuity through the thesis window; (c) first Secretarial Auditor (BMP & Co LLP, FY27-FY31); (d) "ensuing AGM" => full Annual Report drops within weeks -> **schedule Role 6 AR Deep Dive**. No dividend proposed. |
| A3-F14-01 | F14 | TEXT_ANOMALY, consol Note 7 (588-591) | 590 (also 588) | "no deferred tax assets have been recognised by the Holding Company **in its standalone financial results** as at ... June 30, 2026" | NEUTRAL-FACT | Consolidated Note 7 refers to "standalone financial results" inside the CONSOLIDATED notes block (copy-paste artifact; should read consolidated/Group). Same note carries OCR/typo "earned forward losses" (588) vs standalone "carried forward losses" (290). Individually immaterial; a drafting-quality / governance data point. |

---

## CHECKLIST SCORECARD (all 17, one status each — GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 | FINDING | 7 ZERO_STANDING rows resolved: all are tax / OCI-tax lines. Standalone Total tax nil (219-221) on positive PBT every period; consol Current tax-India nil (476). Anticipated tax charge suppressed by Note-7 carryforwards -> forward ETR risk (A3-F1-01). |
| F2 | FINDING | S-vs-C PAT gap narrowed 26pp QoQ (subs 109.34mn vs 145.66mn; -25%) while group PAT flat and standalone +16.6% (222 vs 480). >5pp of standalone PAT -> A3-F2-01. No JV/associate, no NCI (owners = group). |
| F3 | PASS | Not shells: S vs C cost lines diverge sharply (Emp benefits 1,000.50 vs 2,063.53 @211/467; Dep 37.00 vs 58.86 @213/469; stock-in-trade lines exist only in consol @465-466). Subs are operational. 3 unreviewed subs are dormant (rev Nil, loss 0.25mn @413) not shells of the group; no going-concern EoM to reconcile. |
| F4 | FINDING | ~19.4% of consol PAT / ~26.7% of consol revenue rest on non-principal-auditor numbers (para 6+7, 391-419) — above 10% (A3-F4-01). ENTITY_COVERAGE_GAP: 1 of 10 non-holding entities' review basis unstated (A3-F4-02). No prior quarter to trend. |
| F5 | PASS | Both auditor reports checked: NO Emphasis of Matter, NO Going Concern paragraph; conclusions unmodified (158-163 standalone; 382-389/421-423 consolidated). Nothing to scope-track. Prior-quarter EoM diff N.A. (no prior extract) but moot — no EoM exists. |
| F6 | FINDING | Forward-commitment lexicon hits mined: "future equity-based capital raising" (707, A3-F6-01); "will be re-appointed ... effective December 1, 2026" (622); "shall be substituted" (727); "will evaluate the impact" Labour Codes (287/584); "completed its IPO" (264/560); liquidation "approved" (279/576). See Commitment Register. |
| F7 | FINDING | Note-level hedges: Note 7 "uncertainty that sufficient taxable profits will be available ... in the foreseeable future" (291/589, A3-F7-01); Note 6 "will evaluate the impact of any further clarifications" on employee-benefit obligations (287/584). Pre-emptive cover on tax runway and future gratuity cost. |
| F8 | FINDING | Consol ETR ~16% vs statutory 25.17%; Indian holdco pays nil tax, foreign taxes 58.50mn carry the charge; ~900 bps latent shield; FY26 one-off deferred-tax credit 150.70mn (473-479, A3-F8-01). No "earlier years" tax adjustment line disclosed. |
| F9 | FINDING | Q1FY27 actuarial OCI loss (29.86)mn > full FY26 net (+7.21)mn in magnitude -> assumption/Labour-Codes change (226/484, A3-F9-01); verify assumptions at AR. |
| F10 | PASS | Paid-up steady 1,081.70mn (216.34mn shares @Rs5) across Q4FY26/Q1FY27; jump from 170.81mn (Q1FY26) traces cleanly to IPO fresh issue + CCPS conversions (Notes 3,4). Basic=Diluted EPS in Q1FY27 (1.01 standalone / 1.49 consol) — no dilution overhang; spread NARROWED post-IPO, no new dilutive instrument. (Consol FY26 EPS OCR-garbled per A2; not material to dilution call.) |
| F11 | PASS | Net worth ties: standalone 1,081.70 + 15,223.16 = 16,304.86mn (Rs 1,630 Cr); consol 1,081.70 + 16,486.39 = 17,568.09mn (Rs 1,757 Cr) (232/234, 509/511). Consol>standalone by 1,263mn (foreign-sub reserves + FCTR). Order-consistent with ~Rs 1,664 Cr cash context; no third-party rating number in-document to gap-test. |
| F12 | N.A. | Single reportable segment per Note 8 (295/593); no segment asset/liability/revenue tables disclosed to trend. |
| F13 | FINDING | Board Outcome beyond results carries 3 non-results resolutions: capital-raising enabling MOA reclassification, MD re-appointment (Dec-2026 to Nov-2031), first Secretarial Auditor; "ensuing AGM" => AR imminent -> Role 6 AR Deep Dive (A3-F13-01). |
| F14 | FINDING | TEXT_ANOMALY resolved: consol Note 7 says "standalone financial results" inside consolidated notes (590); "earned forward" typo (588). Drafting-quality data point (A3-F14-01). Note-vs-letter consistent otherwise (both "limited review", not audit). |
| F15 | N.A. | No prior quarterly extract on file — no consolidation-list diff possible. Baseline established: 11 entities (1 holding + 5 subs + 4 step-down + 1 trust, 353-372). Forthcoming change to capture next quarter: Argoid Analytics Pvt Ltd under liquidation since Nov 17, 2025 (Note 5, 279/576) -> expected deletion. |
| F16 | N.A. | Results filing; no investor presentation / deck in this doctype. |
| F17 | N.A. | Results filing; no concall transcript. Silence audit deferred to the concall doctype run. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Note / annexure / agenda ref | Status word |
|---|---|---|---|
| IPO of 4,95,46,221 equity shares completed; listed BSE/NSE | Jan 21, 2026 | Note 3 (264-268 / 560-564) | completed |
| CCPS-to-equity conversions (Series D1 + all outstanding 12,430,901 CCPS -> 159,300,958 shares) | Nov 21, 2025 | Note 4 (271-277 / 567-573) | completed |
| Argoid Analytics Pvt Ltd liquidation approved by its Board | approved Nov 17, 2025 (in process) | Note 5 (279-280 / 576-577) | underway |
| Evaluate Labour-Codes impact on gratuity / compensated absences | "the period in which they become applicable" (future) | Note 6 (287-288 / 584-585) | underway / monitoring |
| MD & CEO Baskar Subramanian re-appointment effective | Dec 1, 2026 – Nov 30, 2031 | Agenda 2 (40) / Annexure II (622-626) | recommended, subject to AGM |
| MOA Clause V reclassification substituted (single-class capital) | upon AGM approval; enables "future equity-based capital raising" | Agenda 3 (48) / Annexure III (727, 707) | approved / proposed, subject to AGM |
| BMP & Co LLP appointed Secretarial Auditors | FY2026-27 to FY2030-31 (5-yr first term) | Agenda 4 (76) / Annexure IV (763-768) | approved, subject to AGM |
| Full Annual Report / AGM (dividend & special resolutions) | "ensuing" AGM (weeks) | Agenda 2/3/4 (42, 50, 78) | scheduled -> Role 6 AR Deep Dive |

---

## NOTES FOR A4 (flagged findings -> management questions)

FORWARD-SIGNAL findings: A3-F1-01, A3-F6-01, A3-F8-01, A3-F13-01.
AMBIGUOUS findings (lean-bear, convert to questions): A3-F2-01, A3-F4-02, A3-F7-01, A3-F9-01.

Cross-links to the monitoring checklist:
- Tripwire 1 (cash resolver): this is Q1 FY27, one quarter before the resolver window; cash flow statement not in this results filing (half-yearly). Leading indicator captured: no OCF disclosed. Receivables-vs-revenue growth not testable from this doc (no balance sheet). Capture at H1.
- Tripwire 4 (dilutive/overpriced deployment of ~Rs 1,664 Cr cash): A3-F6-01 / A3-F13-01 — the MOA reclassification explicitly enables future equity raising; the ~27.8 cr-share authorised headroom is the mechanism to watch.
- Tripwire 5 (Rule 11(g) audit-trail): limited-review reports carry NO Rule 11(g) / audit-trail language (limited review, not audit — CARO/Rule 11 apply at the annual audit). Not testable this filing; re-test at the FY27 audit report.
- Optionality register: no NEWSPULSE / marketplace / cloud-modernization revenue lines disclosed (single-segment reporting, Note 8) — no convert signal fired this quarter.

```yaml
stage: A3-forensics
company: "AMAGI"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/amagi-q1fy27/work/forensics_amagi_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1-01", check: "F1", line: "219-222,476,290-293", classification: "FORWARD-SIGNAL", implication: "Standalone zero total tax on positive PBT; carryforward shield finite, ETR normalises upward on exhaustion"}
  - {id: "A3-F2-01", check: "F2", line: "222,480", classification: "AMBIGUOUS", implication: "Subsidiary PAT contribution -25% QoQ (109.34 vs 145.66); foreign/US sub profitability softened while group PAT flat"}
  - {id: "A3-F4-01", check: "F4", line: "391-419", classification: "NEUTRAL-FACT", implication: "~19.4% of consol PAT / ~27% revenue not from principal auditor; above 10% threshold; structural for global group"}
  - {id: "A3-F4-02", check: "F4", line: "391-419,353-372", classification: "AMBIGUOUS", implication: "ENTITY_COVERAGE_GAP: 1 of 10 non-holding entities' review basis unstated in the report"}
  - {id: "A3-F6-01", check: "F6", line: "707", classification: "FORWARD-SIGNAL", implication: "MOA reclassification explicitly enables future equity-based capital raising; ~27.8 cr-share authorised headroom"}
  - {id: "A3-F7-01", check: "F7", line: "291,589", classification: "AMBIGUOUS", implication: "Note-level hedge: uncertainty over sufficient standalone taxable profits in foreseeable future; loss position expected to persist"}
  - {id: "A3-F8-01", check: "F8", line: "473-479", classification: "FORWARD-SIGNAL", implication: "Consol ETR ~16% vs 25.17% statutory; ~900 bps latent shield from Indian nil-tax; reverses as carryforwards exhaust"}
  - {id: "A3-F9-01", check: "F9", line: "226,484", classification: "AMBIGUOUS", implication: "Q1FY27 actuarial OCI loss (29.86) exceeds full FY26 (7.21); assumption/Labour-Codes change; verify at AR"}
  - {id: "A3-F13-01", check: "F13", line: "40,48,76", classification: "FORWARD-SIGNAL", implication: "Capital-raising enabling MOA reclassification + MD re-appointment through window + ensuing AGM triggers Role 6 AR Deep Dive"}
  - {id: "A3-F14-01", check: "F14", line: "590,588", classification: "NEUTRAL-FACT", implication: "Consol Note 7 copy-paste says 'standalone financial results' in consolidated notes; drafting-quality governance data point"}
forward_signals: ["A3-F1-01", "A3-F6-01", "A3-F8-01", "A3-F13-01"]
ambiguous: ["A3-F2-01", "A3-F4-02", "A3-F7-01", "A3-F9-01"]
commitments:
  - {commitment: "IPO completed, listed BSE/NSE", implied_date: "2026-01-21", ref: "Note 3 L264/560", status_word: "completed"}
  - {commitment: "CCPS-to-equity conversions", implied_date: "2025-11-21", ref: "Note 4 L271-277/567-573", status_word: "completed"}
  - {commitment: "Argoid Analytics Pvt Ltd liquidation", implied_date: "2025-11-17 (in process)", ref: "Note 5 L279/576", status_word: "underway"}
  - {commitment: "Evaluate Labour-Codes impact on employee-benefit obligations", implied_date: "when applicable (future)", ref: "Note 6 L287/584", status_word: "underway"}
  - {commitment: "MD & CEO re-appointment effective", implied_date: "2026-12-01 to 2031-11-30", ref: "Annexure II L622-626", status_word: "recommended"}
  - {commitment: "MOA Clause V reclassification enabling future equity raising", implied_date: "upon AGM approval", ref: "Annexure III L707/727", status_word: "proposes to"}
  - {commitment: "BMP & Co LLP Secretarial Auditors appointment", implied_date: "FY2026-27 to FY2030-31", ref: "Annexure IV L763-768", status_word: "approved"}
  - {commitment: "Full Annual Report / ensuing AGM", implied_date: "weeks", ref: "Agenda 2/3/4 L42/50/78", status_word: "is underway"}
gate_a3: pass
blank_checks: []
```
