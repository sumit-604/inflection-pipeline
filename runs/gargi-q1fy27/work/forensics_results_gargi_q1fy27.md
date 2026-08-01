# A3 FORENSIC NOTES — GARGI Q1 FY27 (Doctype: RESULTS)

Company: PNGS Gargi Fashion Jewellery Ltd (GARGI, BSE 543709)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Doctype: results filing (Reg 33 Unaudited Standalone Financial Results)
Source extract: /home/user/inflection-pipeline/runs/gargi-q1fy27/work/extract_results_gargi_q1fy27.txt
Ledger: /home/user/inflection-pipeline/runs/gargi-q1fy27/work/ledger_results_gargi_q1fy27.md
Units: Lakhs (x0.01 to Rs Cr). Statutory tax rate reference: 25.17%.
Line-number convention: the extract's OWN embedded per-line numbers (1-275), matching the A2 ledger.

Ledger reconciliation: 100%. Every A2 ledger row (9 notes, 28 line items, 3 zero_standing, 1 agenda item, 4 auditor paras, 0 entities, 4 signatory blocks) was read verbatim at its cited line before judging. No unread row.

Doctype applicability: F1-F15 apply to a results filing; F16 (presentation-specific) and F17 (concall-specific) are N.A. by protocol.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F1 | §3b row 12 (ZERO_STANDING) | 141 | "Exceptional Item ... 15.18" (blank Q1FY27/Q4FY26/Q1FY26; only FY26 annual populated) | NEUTRAL-FACT | Exceptional-item template line stands empty this quarter (no one-off distortion to Q1FY27 PBT). It was used once in FY26 for Rs 15.18 lakhs; the reduction from PBT-before-exceptional 4,252.78 to PBT 4,237.60 is that item. Watch for reuse; none this quarter. |
| A3-02 | F6 | §4 Company Outlook 2) | 254 | "our expansion guidance continues as planned" | FORWARD-SIGNAL | Management affirms the pan-India expansion guidance for FY27 despite the demand caveat in the same note. Dateable commitment for the Role 5 promise-vs-delivery tracker. |
| A3-03 | F6 | §4 Company Outlook 1) | 248-249 | "company has started spending on PAN India marketing ... company has utilised Rs 640.20 lakhs out of preferential issue proceeds" | FORWARD-SIGNAL | Preferential-issue proceeds deployment is underway; Rs 640.20 lakhs utilised as of 30 Jun 2026 against marketing/pan-India expansion. Track burn rate and remaining balance next quarter. |
| A3-04 | F7 | §4 Company Outlook 2) | 251-253 | "clear signs of a slowdown in spending and lifestyle consumption among the middle class. As a result, our earlier estimates are likely to be affected" | AMBIGUOUS | NEW pre-emptive hedge inside the notes about middle-class demand softening. This is management telling you next quarter looks soft. Directly tensions with the same note's "guidance continues as planned" (A3-02). The contradiction is the standout item for A4 to convert into a management question. |
| A3-05 | F8 | §3b row 16 (ZERO_STANDING) | 148 | "Previous Period 's tax ... 8.34" (blank Q1FY27 & Q1FY26; populated Q4FY26 and FY26) | NEUTRAL-FACT | "Tax adjustments relating to earlier years" non-zero in the comparative columns (Rs 8.34 lakhs, booked in Q4FY26/FY26). Nil this quarter. Q1FY27 ETR 25.59% (173.63/678.59) sits at statutory; no shield distortion this quarter. |
| A3-06 | F10 | §3b rows 25/23/24 + §4 Company Outlook 1) | 168 | paid-up capital "1,035.78" (Q1FY26) rising to "1,047.03"; per note "issued 90,000 equity shares to the promoters and 22,500 equity shares to the non-promoters on a preferential basis at a price of ₹970 per share" (L244-245) | NEUTRAL-FACT | Share count rose +1,12,500 shares YoY, traced cleanly to the FY26 preferential allotment (90,000 promoter + 22,500 non-promoter at Rs 970). Basic EPS = Diluted EPS in every period (no spread, no live dilutive instrument). Note: this is a promoter PURCHASE (opposite of a sale), relevant to monitoring items 10/12. |
| A3-07 | F14 | §3 page-3 statement header | 107 | "Wadgaon Khurd, Nanded, Punc, Maharashtra• 411041" | NEUTRAL-FACT | Registered-office address on the financial-statement page inserts "Nanded" (a different district) whereas the cover letter (L42) and notes footer (L234) read "Wadgaon Khurd, Pune". Likely OCR/copy-paste artifact but an entity-address drafting inconsistency across tables; cumulative governance data point, individually immaterial. |

FINDINGs total: 6 (A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07 = 7 rows across 6 flagged checks; F6 carries two rows A3-02/A3-03). Distinct FINDING checks = 6 (F1, F6, F7, F8, F10, F14).

FORWARD-SIGNAL: A3-02, A3-03. AMBIGUOUS: A3-04. (These three feed A4 management questions.)

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING LINES | FINDING (L141) | 3 ZERO_STANDING rows read: L141 Exceptional Item (template one-off line, FY26 used Rs 15.18, blank this q — A3-01), L148 Previous Period tax (see F8), L169 Other equity (pure quarterly-column convention, benign). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No consolidated track exists in this filing; title, cover letter (L18), auditor report (L50-54) all standalone-only. No S-vs-C gap to compute. Confirmed no hidden consol reference across all 275 lines. |
| F3 SHELL-ENTITY DETECTION | N.A. | No consolidated cost lines to compare; standalone-only, no subsidiaries/JVs named anywhere. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Auditor report has NO Other Matters paragraph (§2) and no JV/associate/component-auditor carve-out; nothing rests on un-reviewed numbers. |
| F5 GOING CONCERN / EoM SCOPE | PASS | Auditor report carries no Emphasis of Matter, no Other Matters, no Going Concern language (§2, swept L45-104). Clean unmodified conclusion (L78-85). Nothing to track. |
| F6 FORWARD-COMMITMENT PHRASE MINING | FINDING (L254, L248) | Lexicon hits: "continues as planned" (L254, expansion guidance affirmed — A3-02); "has started spending"/proceeds utilised (L248-249 — A3-03); "will be available" (L213, boilerplate website posting, non-catalyst). |
| F7 HEDGE PHRASE MINING | FINDING (L251-253) | New note-level hedge on demand: "clear signs of a slowdown... earlier estimates are likely to be affected" (A3-04). Pre-emptive legal/expectation cover, tensions with F6 guidance affirmation. |
| F8 TAX FORENSICS | FINDING (L148) | ETR near statutory every period (Q1FY27 25.59%, Q1FY26 25.57%, FY26 26.07%, Q4FY26 29.71% inc. prior-period tax). Deferred-tax credits persistent but tiny (Q1FY27 credit 6.28, ~0.9pp shield). "Previous Period's tax" non-zero (L148, Rs 8.34) triggers the F8 rule (A3-05). |
| F9 OCI FORENSICS | PASS | Re-measurement of defined-benefit plans: Q1FY27 +0.74, Q4FY26 +1.31, Q1FY26 (0.62), FY26 (0.33); net-of-tax OCI Q1FY27 0.55. Mechanical "swing > full prior year" would trip, but magnitudes are sub-lakh actuarial noise (Rs 55k-74k), gain-direction, no discount-rate/plan-asset assumption-change signal. Not a finding. |
| F10 SHARE COUNT AND DILUTION | FINDING (L168) | Paid-up 1,035.78 -> 1,047.03 (+1,12,500 shares YoY) traced to FY26 preferential issue at Rs 970 (L244-245). Basic EPS = Diluted EPS all periods, no spread, no live dilutive overhang (A3-06). |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | FY26 net worth = Other Equity 13,143.35 + Paid-up 1,047.03 = Rs 14,190.38 lakhs. Other equity blank in all quarterly columns (convention); no third-party figure (rating/slide) in this filing to reconcile against, so no gap detectable — nothing to flag. |
| F12 SEGMENT FORENSICS | N.A. | Single reportable segment per Note 5 (L216-219): "operates in one segment i.e., Trading in fashion/costume jewellery..."; no segment asset/liability tables exist to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Cover letter (L18) discloses results approval only (AGENDA_SINGLE_ITEM); swept for AR/AGM/dividend/director/auditor/ESOP/record-date/capital-raise (§1) — none. No forward board event (AR drop, AGM notice, enabling resolution) to schedule. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING (L107) | Registered-office address inserts "Nanded" on the statement page (L107) vs "Wadgaon Khurd, Pune" elsewhere (L42, L234) — A3-07. Note text vs auditor letter otherwise consistent (both "limited review", Note 1 L196 says "reviewed by Audit Committee and approved by Board"). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation/entity list in this filing (entities = 0) and no prior-quarter list supplied; nothing to diff. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is a results filing, not a presentation deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a results filing, not a concall transcript. (Notion monitoring reconciliation folded into forward implications below, since the operator requested it.) |

GATE A3: every F1-F17 carries a status; every FINDING cites a line. PASS.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Pan-India expansion guidance affirmed ("continues as planned") | FY27 (ongoing) | Company Outlook 2), L254 | underway (affirmed) |
| Deployment of preferential-issue proceeds into pan-India marketing; Rs 640.20 lakhs utilised of proceeds | as of 30 Jun 2026, continuing | Company Outlook 1), L246-249 | underway |
| Results to be posted on BSE and company website | on filing (routine) | Main Note 4, L213 | completed/boilerplate |

---

## NOTION MONITORING CHECKLIST RECONCILIATION (operator watch list vs this filing)

Recorded because the operator pre-committed this watch list; not a formal F-check. Reported for A4.

- (1) Comparable rev growth: same-store/comparable NOT disclosed in this filing. Reported Revenue-from-operations +10.64% YoY (3,021.62 vs 2,731.10, L124); Total-income +12.56% (L127). Both BELOW the 20% RED line and far below the operator's 30% binary threshold. Prior context cited +11.61%; consistent order of magnitude. Binary test FAILS on the growth leg from this document.
- (2) EBITDA margin: operating EBITDA (Rev-from-ops less purchases, inventory change, employee, other expenses) ≈ 597.04 / 3,021.62 = 19.76%; including other income ≈ 25.98%. Below the 22% RED line on the stricter (ex-other-income) definition. Definition call is A4's; flagged.
- (3) PAT margin: PAT 504.96 / Rev-from-ops 3,021.62 = 16.71% (15.73% on total income). Below 18% RED, ABOVE the 15% thesis-broken floor. Down from Q1FY26 19.46%. Deteriorating but not thesis-broken on this leg.
- (4) CFO/PAT (MOST CRITICAL / binary): NOT COMPUTABLE from this document — a Reg 33 quarterly results filing carries no cash-flow statement. The "August binary test" on CFO/PAT cannot be resolved here. Note the inventory build (Changes in inventories (709.57), L131 = ~Rs 7.1 Cr working-capital absorption in the quarter) is a directional cash drag to watch. A4 must source CFO elsewhere.
- (5) Store adds: Note 7 (L224-226) = 36 SIS with PNGS, 54 other-entity SIS, 48 EBO (incl. Kiosk). No prior-quarter figure supplied, so adds not computable from this filing alone.
- (8) Receivable days: no balance-sheet in this filing; not computable.
- (10) RPT / royalty language: Note 7 (L224) confirms the ongoing "Shop in Shop (SIS) stores with P. N. Gadgil & Sons Limited" relationship; NO new charge structure, NO brand-royalty language anywhere (swept). Confirmatory-negative: the thesis-broken RPT-restructuring trigger is NOT tripped this quarter.
- (12) Promoter pledge: none disclosed. The only promoter action is the FY26 preferential PURCHASE of 90,000 shares (A3-06) — opposite of a sale; no >5% open-market sale, no pledge. Trigger NOT tripped.
- (13) CS stability: signatory is Hiranyamai Chaitanya Deshpande, CS & Compliance Officer (L31-32); no CS change disclosed. 12-month change history not assessable from this single filing.

Binary-test summary for A4: growth leg FAILS (<30%), PAT-margin leg marginally holds (>=15%), CFO/PAT leg UNRESOLVABLE from this document, non-EBO stabilisation NOT confirmable here. The demand-softening hedge (A3-04) is the forward tell.

Auditor note for A4/A5: UDIN and partner name are OCR-illegible in the extract (§2, L87-99, flag UDIN_ILLEGIBLE). Recommend sourcing the original BSE PDF for a clean UDIN read, since UDIN verifiability is a compliance-relevant fact — not a finding against the filing, an extract limitation.

---

```yaml
stage: A3-forensics
company: "GARGI"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gargi-q1fy27/work/forensics_results_gargi_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "141", classification: "NEUTRAL-FACT", implication: "Exceptional-item template line blank this quarter; used once in FY26 (Rs 15.18 lakhs). No one-off distortion to Q1FY27 PBT."}
  - {id: "A3-02", check: "F6", line: "254", classification: "FORWARD-SIGNAL", implication: "Pan-India expansion guidance affirmed for FY27 despite same-note demand caveat; dateable commitment for promise-vs-delivery tracker."}
  - {id: "A3-03", check: "F6", line: "248", classification: "FORWARD-SIGNAL", implication: "Preferential-issue proceeds deployment underway; Rs 640.20 lakhs utilised as of 30 Jun 2026. Track burn and remaining balance."}
  - {id: "A3-04", check: "F7", line: "251", classification: "AMBIGUOUS", implication: "New note-level hedge on middle-class demand slowdown ('earlier estimates likely to be affected') tensions with 'guidance continues as planned'; standout A4 management question."}
  - {id: "A3-05", check: "F8", line: "148", classification: "NEUTRAL-FACT", implication: "Prior-period tax adjustment non-zero in comparatives (Rs 8.34 lakhs, Q4FY26/FY26); nil this quarter. Q1FY27 ETR 25.59% at statutory, no shield distortion."}
  - {id: "A3-06", check: "F10", line: "168", classification: "NEUTRAL-FACT", implication: "Paid-up capital +1,12,500 shares YoY traced to FY26 preferential issue at Rs 970 (promoter purchase). Basic=Diluted EPS, no dilutive overhang."}
  - {id: "A3-07", check: "F14", line: "107", classification: "NEUTRAL-FACT", implication: "Registered-office address inserts 'Nanded' on statement page vs 'Pune' elsewhere; entity-address drafting inconsistency, cumulative governance data point."}
forward_signals: ["A3-02", "A3-03"]
ambiguous: ["A3-04"]
commitments:
  - {commitment: "Pan-India expansion guidance affirmed ('continues as planned')", implied_date: "FY27 ongoing", ref: "L254 Company Outlook 2)", status_word: "underway"}
  - {commitment: "Deployment of preferential-issue proceeds into pan-India marketing (Rs 640.20 lakhs utilised)", implied_date: "as of 2026-06-30, continuing", ref: "L246-249 Company Outlook 1)", status_word: "underway"}
  - {commitment: "Results posted on BSE and company website", implied_date: "on filing", ref: "L213 Main Note 4", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
