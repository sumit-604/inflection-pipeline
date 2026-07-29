# A3 FORENSIC NOTES — MTAR Technologies Limited (MTAR), Q1 FY27, RESULTS filing

Source extract: /home/user/inflection-pipeline/runs/mtar-q1fy27/work/extract_results_mtar_q1fy27.txt (585 lines, 9 pages)
Ledger: /home/user/inflection-pipeline/runs/mtar-q1fy27/work/ledger_results_mtar_q1fy27.md
Unit convention: INR millions (x0.1 to Cr). VERIFIED cell values used per A1 text-layer verification note (extract lines 15-72); the six decimal-glyph cells cited at their VERIFIED value.
Ledger reconciliation: 100% — every A2 row (11 notes, 68 line_items, 8 zero_standing, 7 agenda_items, 26 auditor_paras, 3 entities, 2 annexure_profiles, 4 signature_blocks) read at its A1 line before judging.
Doctype scope: results filing — F1-F15 apply; F16 (presentation) and F17 (concall) N.A. First quarterly run for MTAR; no prior baseline, so F5 diff and F15 diff are N.A. (current-quarter content still assessed in full).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F6-a | F6 | §6 note[3] / §7 note 4 | 365 (standalone) / 437 (consol) | "has filed the scheme for the merger of its wholly owned subsidiaries, Gee Pee Aerospace ... into the Holding company with the National Company Law Tribunal" | FORWARD-SIGNAL | Prospective collapse of 3 entities to 1; NCLT sanction pending, undated. Consolidation scope will change on effectiveness. Feeds Role 5 promise/delivery + FTTCP timeline. A4 question. |
| F8-a | F8 | §4 L342 / §5 L413 | 342 (standalone) / 413 (consol) | "Adjustment of tax relating to earlier periods ... (8.26)" | NEUTRAL-FACT | Non-zero prior-period tax credit of Rs 8.26M booked in Q4 FY26 / FY26 column (nil in both Jun-26 and Jun-25). Mandated FINDING per F8 rule. One-time; inflated FY26 PAT base by 8.26M, does not recur into Q1 FY27. |
| F13-a | F13 | §2 agenda items 3-7 | 113-120 | "Notice of the Annual General Meeting (AGM), the Directors' Report ... the BRSR, the MD&A, and the Corporate Governance Report for the Financial Year ended 31.03.2026" | FORWARD-SIGNAL | Full FY26 Annual Report drops within weeks of AGM (28 Sep 2026) -> schedule Role 6 AR Deep Dive. AGM VC-mode 28 Sep 2026. Two promoter-family directors re-appointed (retiring by rotation), w.e.f. ensuing AGM. A4 question. |
| F14-a | F14 | §9 block 15 / §11 #4 | 687 (consol) vs 535 (standalone) | "Membership No.: 4777" (consol) vs "Membership No.: 504777" (standalone) | NEUTRAL-FACT | Same partner/firm/day, membership number differs. Standalone UDIN "2650477 1 DMUF RT 3484" (L537) embeds "50477", consistent with 504777; consol "4777" is almost certainly a dropped leading "50" glyph (same artifact class as pages 5-6). Low governance weight; confirm at source PDF. |
| F14-b | F14 | §9 UDIN_MISSING flag / §11 #4 | 537 (present, standalone) vs consol sig block 679-692 (absent) | standalone: "UDIN: 2650477 1 DMUF RT 3484"; consolidated block carries NO UDIN line | AMBIGUOUS | Consolidated review report shows no UDIN anywhere in its signature block. Either a genuine UDIN omission on the consolidated report (UDIN is ICAI-mandatory — a compliance/governance data point) or an extraction line-drop. Cannot resolve from text layer. Conservative: A4 question — verify against the BSE/NSE-filed source PDF. |
| F14-c | F14 | §4 L338 / §5 L409 | 338 (standalone) vs 409 (consol) | standalone: "Statutory impact of new Labour Codes"; consol: "Statutory impact of new Labour Code" | NEUTRAL-FACT | Line-label singular/plural mismatch across the two statements for the same exceptional item. Individually immaterial note-drafting inconsistency; logged per F14 (cumulative governance data point). |

---

## CHECKLIST SCORECARD (all 17 — exactly one status each)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING | PASS | All 8 ZERO_STANDING rows (L338, L342, L347, L348 standalone; L409, L413, L418, L419 consol) checked. Current Q1 FY27 (Jun-26) nil on every one; values sit only in Mar-26/FY26 comparatives. Labour-code exceptional (37.67M) and OCI (3.61) explained by notes 5/6 (L368-369, L440-441); tax-adjustment and OCI are standard template lines carried as comparatives. No standing profit-on-sale / impairment / discontinued-ops line lurking. |
| F2 S vs C DECOMPOSITION | PASS | Revenue gap ~0 all periods (identical Jun-26 3,607.21; Jun-25 1,565.84). PAT gap consol-below-standalone: Jun-26 2.77 (0.55% of standalone PAT), Jun-25 4.16 (3.7%), FY26 12.94 (1.36%). Max YoY change 3.15pp < 5pp threshold. Subs drag narrowing. Auditor-stated subs net loss 7.22M vs 2.77 PAT gap reconciles through intra-group eliminations (other-expense elimination ~11.68M offsetting higher subs employee/dep cost). |
| F3 SHELL-ENTITY | PASS | Cost lines S vs C (Jun-26): materials 2,042.72 vs 2,043.19 (near-identical, +0.47); finance cost 158.47 vs 158.47 (IDENTICAL — subs carry zero debt); employee 457.71 vs 465.20 (+7.49); dep 94.76 vs 96.92 (+2.16). Subs have revenue (Rs 16.79M, L641) and employees — small operating entities, not pure shells. No Going Concern EoM present anywhere, so no shell/going-concern mismatch to reconcile. |
| F4 UNAUDITED CONTRIBUTION | PASS | Auditor Other-Matters-type disclosure (L640-646): two subsidiaries not reviewed by principal auditor S.R. Batliboi — revenue Rs 16.79M (0.47% of consol revenue), net loss Rs 7.22M (1.44% of consol PAT 502.27M). Below 10% threshold. Reports management-furnished, principal auditor relies "solely on the report of such auditors" (L671) — standard caveat noted. No prior period to trend (first run). |
| F5 GOING CONCERN / EoM | N.A. | Diff check has no prior-quarter baseline (first run). Current-quarter paragraphs assessed in full: standalone conclusion UNMODIFIED, no EoM/no Going Concern (L512-524); consolidated conclusion UNMODIFIED, no formal EoM heading, no Going Concern (L620-634). Only Other-Matters-type subsidiary reliance disclosure present (L637-678). Nothing to diff, nothing adverse. |
| F6 FORWARD-COMMITMENT | FINDING | NCLT merger scheme filed (F6-a, L365/L437); plus dated/dateable commitments in the commitment register: AGM 28 Sep 2026 (L117), director re-appointments "subject to the approval of shareholders" w.e.f. ensuing AGM (L216-227), FY26 AR/BRSR/MD&A/CG release (L113-116), scrutinizer appointment (L119). Merger flagged FORWARD-SIGNAL for A4. |
| F7 HEDGE PHRASE | PASS | Only "subject to" hits are procedural — director re-appointment "subject to the approval of shareholders/members" (L218, L226), "subject to the requirements of Regulation 33", "subjected to limited review" (L364, L436). No pre-emptive risk hedge on revenue lumpiness or customer concentration newly added in notes. |
| F8 TAX FORENSICS | FINDING | ETR clean vs 25.17% statutory: standalone Jun-26 25.33% (171.36/676.40), Jun-25 26.11%, FY26 25.10%; consol Jun-26 25.48%. Deferred tax is a persistent CHARGE (19.97/20.36 Jun-26), not a credit — no DTA shield risk. FINDING is the mandated one: "Adjustment of tax relating to earlier periods" non-zero (8.26) in Mar-26/FY26 (F8-a). |
| F9 OCI FORENSICS | PASS | OCI nil in Q1 FY27 (Jun-26) and Jun-25 both statements; the (3.61) loss sits only in Mar-26 quarter = FY26 full year — standard year-end actuarial remeasurement, not a mid-year assumption change or a single-quarter swing exceeding the prior year. Verify discount-rate/plan-asset assumptions at the FY26 AR (drops in weeks). |
| F10 SHARE COUNT / DILUTION | PASS | Paid-up capital 307.59M flat across all four periods, both statements (L350/L421) — no corporate action. Basic EPS = Diluted EPS every period (16.42=16.42 standalone; 16.33=16.33 consol Jun-26; 3.65=3.65; 30.99/30.57) — zero spread, no dilutive instruments outstanding. |
| F11 RESERVES / NET WORTH | PASS | Net worth: standalone 7,949.23 + 307.59 = 8,256.82M (Rs 825.68 Cr); consol 7,918.28 + 307.59 = 8,225.87M (Rs 822.59 Cr). Other-equity populated only in year-end column (blank in quarters) — standard quarterly treatment. No third-party number (rating rationale/slide) in this filing to reconcile against. Consol reserves 30.95M below standalone = accumulated subs losses/adjustments (neutral). |
| F12 SEGMENT FORENSICS | PASS | Single business segment per Ind AS 108 (note 4 standalone L367 / note 5 consol L439). No segment asset/liability schedule in the quarterly statement — nothing to trend. Checked; not anomalous. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | 7 agenda items. Item 5: full FY26 AR/Directors' Report/BRSR/MD&A/CG approved -> Role 6 AR Deep Dive within weeks. Item 6: AGM 28 Sep 2026 (VC). Items 3-4: re-appointment of Rohith Loka Reddy (DIN 06464331) and Anushman Reddy (DIN 08104131), both retiring by rotation, both promoter-family related parties (to MD P. Srinivas Reddy and WTD Praveen Kumar Reddy respectively, L259-263). No independent director non-renewal. Item 7: scrutinizer. FORWARD-SIGNAL (F13-a). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Membership No. 504777 (standalone L535) vs 4777 (consol L687), same partner/day (F14-a — likely glyph drop; UDIN L537 embeds "50477", corroborating 504777). Consolidated UDIN absent entirely (F14-b — AMBIGUOUS). Labour "Codes" (L338) vs "Code" (L409) label variance (F14-c). Cumulative governance data point. |
| F15 ENTITY LIST DIFFS | N.A. | No prior-quarter extract for a diff (first run). Current list assessed in full: 3 entities — MTAR (holding) + Gee Pee Aerospace and Defence Pvt Ltd (WOS) + Magnatar Aero Systems Pvt Ltd (WOS). Internally consistent between consolidated note 1 (L429-430) and auditor entity list (L616-619). Both WOS under pending NCLT merger (prospective structure change captured under F6-a). |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a results filing, not a concall transcript. |

GATE A3: PASS — all 17 checks carry exactly one status; every FINDING cites a line and a verbatim quote.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/item ref | status word |
|---|---|---|---|
| Merger of WOS Gee Pee Aerospace and Defence Pvt Ltd and Magnatar Aero Systems Pvt Ltd into the Holding company | Pending NCLT sanction (undated) | note 3 standalone (L365) / note 4 consol (L437) | filed / underway |
| Annual General Meeting for FY 2025-26 (video conference) | 28 September 2026 | agenda item 6 (L117) | scheduled |
| Re-appointment of Rohith Loka Reddy (DIN 06464331) and Anushman Reddy (DIN 08104131), retiring by rotation | w.e.f. ensuing AGM (28 Sep 2026), subject to shareholder approval | agenda items 3-4 (L109-112) / Annexure A (L216-227) | proposed / subject to approval |
| Release of FY26 Annual Report + Directors' Report + BRSR + MD&A + Corporate Governance Report | Ahead of AGM, i.e. within weeks | agenda item 5 (L113-116) | approved / pending release |
| Appointment of S.S. Reddy & Associates as e-voting scrutinizers | For ensuing AGM (28 Sep 2026) | agenda item 7 (L119) | appointed |

---

## NOTES FOR A4 (interpretation handoff)
- FORWARD-SIGNALS to convert into management questions: F6-a (NCLT merger — timeline, effective date, accounting/tax impact of collapsing the two WOS into the holding), F13-a (FY26 AR drop -> Role 6 AR Deep Dive; confirm the AR carries the order-book, segment and WC detail the Notion monitoring checklist tracks — Bloom hot-box, Kaiga nuclear PO, Weatherford commissioning, EBITDA ~23% sustain, WC <200 days).
- AMBIGUOUS to resolve at source: F14-b (consolidated review report UDIN absence — genuine omission vs extraction artifact; verify against BSE/NSE-filed PDF).
- Notion monitoring checklist items (Bloom volumes, Kaiga/civil-nuclear inflows, Weatherford commissioning, EBITDA margin sustain, WC days) are NOT addressable from a bare results filing — no segment split (single-segment), no order book, no balance sheet detail. These carry to the FY26 AR (weeks away) and the concall, not resolvable here. Not scored as F17 (N.A. for a results doctype) but flagged for A4/Role 5 continuity.
- Conservative lean applied: F8-a and F14-a logged as mandated/NEUTRAL findings without over-interpretation; F14-b escalated to AMBIGUOUS rather than dismissed as artifact.
```yaml
stage: A3-forensics
company: "MTAR"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/mtar-q1fy27/work/forensics_mtar_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: PASS
  F3: PASS
  F4: PASS
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F6-a", check: "F6", line: "365 / 437", classification: "FORWARD-SIGNAL", implication: "NCLT merger of two WOS into holding filed, pending sanction; consolidation scope will change"}
  - {id: "F8-a", check: "F8", line: "342 / 413", classification: "NEUTRAL-FACT", implication: "Prior-period tax credit (8.26) in Q4FY26/FY26; one-time, non-recurring into Q1FY27"}
  - {id: "F13-a", check: "F13", line: "113-120", classification: "FORWARD-SIGNAL", implication: "FY26 AR drops within weeks -> Role 6 AR Deep Dive; AGM 28 Sep 2026; two promoter-family directors re-appointed"}
  - {id: "F14-a", check: "F14", line: "535 / 687", classification: "NEUTRAL-FACT", implication: "Membership No. 504777 vs 4777 same partner/day; likely dropped-glyph, confirm at source"}
  - {id: "F14-b", check: "F14", line: "537 / 679-692", classification: "AMBIGUOUS", implication: "UDIN absent on consolidated review report vs present on standalone; genuine omission vs extraction artifact — verify at source PDF"}
  - {id: "F14-c", check: "F14", line: "338 / 409", classification: "NEUTRAL-FACT", implication: "Labour 'Codes' vs 'Code' line-label variance across statements; immaterial drafting inconsistency"}
forward_signals: ["F6-a", "F13-a"]
ambiguous: ["F14-b"]
commitments:
  - {commitment: "Merger of WOS Gee Pee Aerospace and Magnatar Aero Systems into Holding company", implied_date: "pending NCLT sanction (undated)", ref: "note 3 L365 / note 4 L437", status_word: "filed/underway"}
  - {commitment: "AGM for FY2025-26 (video conference)", implied_date: "2026-09-28", ref: "agenda item 6 L117", status_word: "scheduled"}
  - {commitment: "Re-appointment of directors Rohith Loka Reddy and Anushman Reddy (retiring by rotation)", implied_date: "w.e.f. ensuing AGM 2026-09-28, subject to shareholder approval", ref: "agenda items 3-4 L109-112 / Annexure A L216-227", status_word: "proposed"}
  - {commitment: "Release of FY26 Annual Report / Directors' Report / BRSR / MD&A / CG Report", implied_date: "within weeks (ahead of 2026-09-28 AGM)", ref: "agenda item 5 L113-116", status_word: "approved/pending-release"}
  - {commitment: "Appointment of S.S. Reddy & Associates as e-voting scrutinizers", implied_date: "for ensuing AGM 2026-09-28", ref: "agenda item 7 L119", status_word: "appointed"}
gate_a3: pass
blank_checks: []
```
