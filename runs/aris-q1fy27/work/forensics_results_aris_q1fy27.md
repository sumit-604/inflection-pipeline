# A3 FORENSIC NOTES — Arisinfra Solutions Limited (ARIS) — Q1 FY27 — DOCTYPE: results

Source: `extract_results_aris_q1fy27.txt` (610 lines, 10 pages, unit = Rs Millions; x0.1 -> Rs Cr).
Ledger reconciled: 100% (all 8 A2 categories read row-by-row at cited lines; 16 notes + 77 line items + 1 zero_standing + 1 agenda + 13 auditor paras + 8 entities + 5 signatures + 4 annexures).
Prior-quarter extract: none (first quarterly run) — all QoQ verbatim diffs (F5 EoM, F15 entity list) are baseline-only this cycle; noted where a check depends on a prior-quarter compare.
Auditor: MSKC & Associates LLP — this is MSKC's FIRST review engagement (predecessor auditor did Q1FY26 and FY26; PwC resigned May 2026 per Notion). Conclusion UNMODIFIED, no EoM, no Going Concern paragraph, both statements.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F1 | 2B row 13 (zero_standing) | 493-495 | "Share of net loss of investments accounted for using the equity method ... (0.00)" | NEUTRAL-FACT | Template line exists solely for one equity-accounted associate, Vishwa Hitay Foundation, whose share is nil and "not material to the Group" (para 7, l.419). A for-profit consolidating a "Foundation" as associate warrants an RPT/routing check at the AR; watch if it ever turns material. |
| A3-02 | F2 | 2A r1/r19 vs 2B r1/r21 | 180/206/475/510 | S rev "1,287.26" vs C rev "2,908.09"; S PAT "74.60" vs C PAT "200.31" | FORWARD-SIGNAL | Subsidiary share of group PAT swung from 45% of standalone PAT (Q4FY26) to 168% (Q1FY27), a >120pp move (threshold 5pp). Subsidiaries (PAT 127.28mn) now out-earn the listed parent (74.60mn); standalone revenue fell 38% QoQ (2,073.57 -> 1,287.26) while consolidated fell only 15%. The economic engine sits in the seven unlisted subsidiaries, all reviewed by OTHER auditors — see A3-03. |
| A3-03 | F4 | 5B para 6 + para 7 | 387-396 / 412-419 | "We did not review the interim financial statements of seven subsidiaries ... total net profit after tax of Rs. 127.28 Million" | FORWARD-SIGNAL | 63.5% of consolidated PAT (127.28/200.31) and 55.7% of consolidated revenue (1,620.83/2,908.09) rest on component-auditor work MSKC did not review; +1 associate wholly management-certified. Level is 6x the 10% finding threshold. YoY trend of the unaudited % is N.A. (first MSKC engagement, no comparable prior disclosure). Concentration is acute given the governance CONCERN backdrop (PwC resigned, CFO churn). |
| A3-04 | F6 | Note 6 (both) | 251-252 | "The Company is in the process of filing of the Application with the Hon'ble NCLT" | FORWARD-SIGNAL | AUSPL (ArisUnitern RE Solutions) amalgamation into listed ASL is a live, dateable catalyst: NOCs already received (BSE 17-Jul-2026, NSE 20-Jul-2026), NCLT filing underway (context deadline 20-Jan-2027), appointed date 1-Apr-2026. See COMMITMENT REGISTER. |
| A3-05 | F7 | 2A r6 / 2B r6 (loss allowance) | 187 / 482 | Loss allowance on trade receivables Q1FY27 " - " (nil) vs Q4FY26 "44.62" (C) / "23.95" (S) | FORWARD-SIGNAL | ZERO expected-credit-loss charge booked this quarter, both statements, against a receivable book that absorbed 44.62mn (C) of provisions last quarter and 50.04mn across FY26, with debtor days at 140 (Notion master metric, Red >160). Nil provisioning while receivables are the pre-committed break test signals catch-up-provision risk next quarter. Also hedge phrase "subject to the necessary statutory and regulatory approvals" (note 6, l.247-248) around the scheme. |
| A3-06 | F8 | 2A r16 / 2B r18 + deferred-tax rows | 202 / 506 | "Short/(excess) provision of tax in earlier years ... 17.12" (S, Q4FY26); "17.29" (C, Q4FY26) | AMBIGUOUS | Prior-year tax true-up of 17.12mn (S) / 17.29mn (C) sits in the Q4FY26 comparative column (current quarter nil). Consolidated deferred tax is a persistent CREDIT every period shown ((2.55)/(30.07)/(22.34)/(3.03)) = ~96bps ETR shield this quarter from DTA/carry-forward utilisation = future ETR step-up risk once exhausted. ETRs otherwise normal (C 24.9%, S 23.5% vs 25.17%). |
| A3-07 | F9 | 2A r20 / 2B r22 | 210 / 514 | "Remeasurements of defined benefit plans (2.07)" (S) / "(2.56)" (C) | AMBIGUOUS | Single-quarter actuarial OCI loss (S 2.07mn / C 2.56mn) exceeds the entire prior full-year remeasurement (S 0.95mn / C 0.84mn) — mechanical F9 trigger for a discount-rate/plan-assets assumption change. Absolute amounts tiny; verify actuarial assumptions at the Annual Report. |
| A3-08 | F10 | 2A r24 / 2B r35 + EPS rows | 216/222 / 536/542 | Paid-up "163.52" (Q4FY26) -> "163.59" (Q1FY27); diluted EPS "0.91" = basic "0.91" | AMBIGUOUS | Paid-up equity rose +0.07mn QoQ (~35,000 shares at Rs 2 FV) with NO corporate action explained in this filing; the separately-disclosed ESOP grant of 1,633 options (Notion) cannot account for it. Basic-vs-diluted spread collapsed to nil this quarter (was 0.03 S / 0.05 C in FY26) — dilutive instruments turned non-dilutive on lower quarterly EPS. Trace the share-count change to an allotment. |
| A3-09 | F12 | Note 3 (both) vs entity list | 232-233 / 558-559 / 372,571 | "The Company operates only in one business segment i.e. Trading of Construction Materials" | AMBIGUOUS | Single reportable segment declared, yet the consolidation list carries ArisUnitern RE Solutions (real estate) and Arisinfra Realty Private Limited — businesses not obviously "Trading of Construction Materials." Possible segment aggregation; no segment asset/liability disclosure to trace equity-funded builds. A4 question on segment definition. |
| A3-10 | F14 | Cat 6 entity list vs Note 6 | 372 vs 571 | "Arsinfra Reality Private Limited" (auditor report) vs "Arisinfra Realty Private Limited" (note 6) | CONFIRMATORY-NEGATIVE | Entity name mis-spelled/inconsistent across the same filing (also "ArisUnitern RE Solutions" l.363 vs "Arisunitern Re Solutions" l.245). Individually immaterial; cumulatively a drafting-control data point consistent with the standing governance CONCERN and a first-time auditor. |
| A3-11 | F15 | Cat 6 row 4 + Note 6 | 365-366 | "Lionheart Trading Private Limited (Formerly known as 'Arisinfra Trading Private Limited')" | FORWARD-SIGNAL | In-document entity CHANGES visible even without a prior ledger: (a) subsidiary renamed Arisinfra Trading -> Lionheart Trading; (b) ArisUnitern RE Solutions is a subsidiary pending absorption into ASL (appointed date 1-Apr-2026 already inside the Q1FY27 consolidation window; scheme not yet effective). Entity list will shrink post-NCLT. This 8-entity list is the baseline for future diffs. |

Note: F5, F3, F11, F13 checked and clean (see scorecard). QoQ diffs (F5 EoM, F15 entity list) are baseline-only; F16/F17 N.A. for a results filing with no concall.

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1  | FINDING | Sole zero_standing line (equity-method associate share, l.493-495) exists for one immaterial "Foundation" associate; documented (A3-01). |
| F2  | FINDING | S-vs-C PAT gap widened from 45% to 168% of standalone PAT QoQ, >120pp (threshold 5pp); subsidiaries out-earn the parent (A3-02). |
| F3  | PASS | No shells: C cost lines materially exceed S (Employee 120.21 vs 41.98 l.483/188; Purchases 2,403.91 vs 1,154.85 l.480/185); subsidiaries have real operations; no Going Concern flag. |
| F4  | FINDING | 63.5% of consolidated PAT and 55.7% of revenue unreviewed by MSKC (para 6-7, l.387-419); 6x the 10% threshold (A3-03). |
| F5  | PASS | No EoM and no Going Concern paragraph in either review report (5A#5 l.130-136, 5B#8 l.424-430); nothing to track; QoQ diff N.A. (first run). |
| F6  | FINDING | Forward commitments mined in note 6 / note 7 (NCLT filing underway, scheme effectiveness, IPO balance) — see register (A3-04). |
| F7  | FINDING | Nil ECL charge this quarter vs 44.62mn last quarter against a 140-day debtor book = pre-emptive forward signal; scheme "subject to ... approvals" hedge present (A3-05). |
| F8  | FINDING | Earlier-year tax true-up 17.12/17.29mn in Q4FY26 comparatives (l.202/506); persistent consolidated deferred-tax credits (~96bps shield) (A3-06). |
| F9  | FINDING | Q1FY27 actuarial OCI loss (S 2.07 / C 2.56mn) exceeds full FY26 (S 0.95 / C 0.84mn) = assumption-change trigger (A3-07). |
| F10 | FINDING | Paid-up +0.07mn QoQ unexplained by any corporate action in filing; basic=diluted EPS spread collapsed to nil (A3-08). |
| F11 | PASS | Other Equity annual-only (FY26 S 7,000.95 / C 7,227.96, l.218/538); net worth ties (S 7,164.47mn); no third-party number (ICRA rating rejected, no rationale figure) to reconcile; no gap. |
| F12 | FINDING | Single segment "Trading of Construction Materials" (note 3) despite realty/RE-Solutions subsidiaries in consolidation list (A3-09). |
| F13 | PASS | Board Outcome carries only results approval (37-min meeting 16:00-16:37, l.34-35); no AR/AGM/record-date/dividend/director/capital-raise resolution (A2 grep = zero hits). ESOP grant of 1,633 options was disclosed SEPARATELY today, not in this filing. |
| F14 | FINDING | Entity-name inconsistencies within the filing ("Arsinfra Reality" l.372 vs "Arisinfra Realty" l.571) (A3-10). |
| F15 | FINDING | In-document rename (Lionheart, formerly Arisinfra Trading, l.365-366) + pending AUSPL amalgamation change relationship; baseline set (A3-11). QoQ diff N.A. (first run). |
| F16 | N.A. | Presentation-specific check; this is a results filing. |
| F17 | N.A. | Concall-specific silence audit; no concall this run. |

No blanks. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| File the Scheme of Amalgamation Application with the Hon'ble NCLT (AUSPL into ASL) | near-term; context deadline 20-Jan-2027 | note 6, l.251-252 ("in the process of filing") | underway |
| Scheme becomes effective upon filing of NCLT order with Registrar of Companies | post-NCLT approval | note 6, l.250-251 ("will be effective upon filing") | pending |
| NOCs from BSE (17-Jul-2026) and NSE (20-Jul-2026) for the Scheme | achieved | note 6, l.249-250 ("has received the No Objection Certificates") | completed |
| Remaining unutilised IPO share-issue-expense balance (Rs 5.86mn) to be applied | unspecified future | note 7, l.275 ("the remaining shall be used in future") | initiated |

---

## MONITORING CROSS-CHECK (Notion checklist vs this filing)

1. Debtor days (MASTER, 140 latest, Red >160): NOT disclosed in this results filing (no balance sheet). This quarter is the pre-committed master test but the metric is not derivable from the P&L alone — flag for A4 to source from balance sheet / concall.
2. >6-month receivable bucket (Red >Rs 100 Cr): NOT disclosed. See A3-05 — nil ECL this quarter is the read-through signal.
3. CM capacity utilisation: N.A. (trading company, single segment).
4. Operating EBITDA margin (Green >9.5%): Consolidated Q1FY27 ~10.5% (rev 2,908.09 less purchases/inventory/employee/other-exp) = above green; standalone ~5.9% = weak. Margin quality sits in subsidiaries (A3-02). Not a break.
5. DAAS/Services revenue share: NOT disclosed (single reportable segment, note 3) — see A3-09.
6. Free cash flow: NOT computable (no cash-flow statement in this filing).
7. Equity dilution: Paid-up +0.07mn QoQ unexplained (A3-08); ESOP 1,633 options disclosed separately today; no QIP/discounted raise in this filing.
8. Auditor stability: MSKC clean UNMODIFIED conclusion, no EoM, no qualification, no specific-customer provision, no receivable-recoverability comment = GREEN on this filing's face. BUT it is MSKC's first engagement, 63.5% of PAT rests on unreviewed component auditors (A3-03), and nil group ECL was booked (A3-05) — the "clean" opinion covers numbers MSKC largely did not review.

---

```yaml
stage: A3-forensics
company: "ARIS"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/aris-q1fy27/work/forensics_results_aris_q1fy27.md"
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
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "493-495", classification: "NEUTRAL-FACT", implication: "Equity-method line exists only for immaterial associate Vishwa Hitay Foundation; RPT/routing check at AR"}
  - {id: "A3-02", check: "F2", line: "180/206/475/510", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap 45%->168% of standalone PAT QoQ; subsidiaries out-earn listed parent"}
  - {id: "A3-03", check: "F4", line: "387-396", classification: "FORWARD-SIGNAL", implication: "63.5% of consolidated PAT and 55.7% of revenue unreviewed by MSKC; 6x threshold; governance-CONCERN backdrop"}
  - {id: "A3-04", check: "F6", line: "251-252", classification: "FORWARD-SIGNAL", implication: "AUSPL amalgamation live catalyst; NCLT filing underway, NOCs received, deadline 20-Jan-2027"}
  - {id: "A3-05", check: "F7", line: "187/482", classification: "FORWARD-SIGNAL", implication: "Nil ECL charge this quarter vs 44.62mn prior against 140-day debtor book; provision catch-up risk next quarter"}
  - {id: "A3-06", check: "F8", line: "202/506", classification: "AMBIGUOUS", implication: "Prior-year tax true-up 17.12/17.29mn in Q4FY26 comparatives; persistent consolidated DT credits ~96bps shield = future ETR step-up"}
  - {id: "A3-07", check: "F9", line: "210/514", classification: "AMBIGUOUS", implication: "Q1 actuarial OCI loss exceeds full FY26; verify discount-rate/plan-asset assumptions at AR"}
  - {id: "A3-08", check: "F10", line: "216/536", classification: "AMBIGUOUS", implication: "Paid-up +0.07mn (~35k shares) unexplained by any corporate action in filing; diluted spread collapsed to nil"}
  - {id: "A3-09", check: "F12", line: "232-233", classification: "AMBIGUOUS", implication: "Single segment declared despite realty/RE-Solutions subsidiaries; possible aggregation; A4 question"}
  - {id: "A3-10", check: "F14", line: "372", classification: "CONFIRMATORY-NEGATIVE", implication: "Entity-name inconsistencies within filing; drafting-control data point under governance CONCERN + first-time auditor"}
  - {id: "A3-11", check: "F15", line: "365-366", classification: "FORWARD-SIGNAL", implication: "In-doc rename (Lionheart ex-Arisinfra Trading) + pending AUSPL absorption; entity list will shrink post-NCLT; baseline set"}
forward_signals: ["A3-02", "A3-03", "A3-04", "A3-05", "A3-11"]
ambiguous: ["A3-06", "A3-07", "A3-08", "A3-09"]
commitments:
  - {commitment: "File Scheme of Amalgamation Application with NCLT (AUSPL into ASL)", implied_date: "20-Jan-2027 (context)", ref: "note 6, l.251-252", status_word: "underway"}
  - {commitment: "Scheme effective upon filing of NCLT order with RoC", implied_date: "post-NCLT approval", ref: "note 6, l.250-251", status_word: "pending"}
  - {commitment: "NOCs from BSE and NSE for the Scheme", implied_date: "2026-07-17 / 2026-07-20", ref: "note 6, l.249-250", status_word: "completed"}
  - {commitment: "Remaining unutilised IPO share-issue-expense balance Rs 5.86mn to be applied", implied_date: "unspecified future", ref: "note 7, l.275", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
