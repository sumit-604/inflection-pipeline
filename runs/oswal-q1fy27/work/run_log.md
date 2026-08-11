# Run Log — OSWAL Q1 FY27 Quarterly Review

## 0. Setup and Prechecks

**a. Arguments.** TICKER = `OSWAL` (Oswal Pumps Ltd; user wrote "Uswal/Oswal
pumps", matched to Notion COMPANIES MASTER ticker `OSWAL`). `--docs`: none
supplied as files; the user pasted ONE document inline — the Q1 FY27 earnings
concall transcript (Hindi/Hinglish ASR). "all transcripts" requested; only the
Q1 FY27 concall was provided, so this run covers that single document. No
results filing (Reg 33) and no investor presentation were supplied.

**b. Protocol-file check.** PRESENT:
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md  ✅ (governs this run — concall)
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md   ✅ (present; not exercised — no results filing this run)
- frameworks/Master_Project_Prompt_v3.3.md               ✅
No protocol reconstructed from memory. No STOP.

**c. Toolchain precheck.** pdftotext / pdfinfo / pdftoppm / tesseract =
MISSING. Install attempted (apt-get poppler-utils tesseract-ocr) — FAILED
(no package access in this environment). **Not a halt for this run:** the sole
input is a TEXT transcript, not a PDF. Per the Atlanta Electricals precedent
(runs/atlantaelec-q1fy27/inputs/concall_*.txt was a text file extracted without
PDF tooling), A1 line-numbers the text directly. The PDF toolchain would only
be required if a PDF results filing or presentation were in scope — neither is.
If a PDF is added later, extraction halts until poppler/tesseract are available.

**d. Document-class detection.** One document. Speaker-turn structure
(Moderator / "Ladies and gentlemen" / analyst-firm attributions / Q&A) →
classified **concall**. Recorded.

**e. Run folder.** `runs/oswal-q1fy27/` created with `inputs/` and `work/`.
Transcript saved verbatim (ASR errors preserved, not corrected) to
`inputs/concall_oswal_q1fy27.txt`. Quarter detected from content header
("Q1 FY27", quarter ended 26/30 June 2026) → `q1fy27`.

**f. Company memory + Notion.** No `companies/OSWAL.md` local file. Notion page
fetched LIVE (2026-08-11) — page id 345bb2b9-d3ab-8092-9806-c2ec690686c6,
COMPANIES MASTER. Key state passed inline to A3 and A4 (subagents do not call
Notion). See NOTION MEMORY PACKET below.

---

## NOTION MEMORY PACKET (passed inline to A3 and A4)

**Decision Status:** WATCHLIST. **Position Size:** Small (2-3% max) until
governance clears. **Promoter Verdict:** CONCERN. **Sector:** Manufacturing
(Solar Water Pumping Systems, B2G). **Gate 0:** GOOD, 114/160. **EM:** 32,
MOAT STRENGTHENING. **Destination PE:** 16-20x. **Cash multiplier:** 0.65x
(structural WC drag). **One-line thesis:** buy < ₹435 MoS; EPS ₹47 (FY25) →
₹150 (FY28E) on PM-KUSUM + capacity + backward integration; base range
₹990-2,400; ~32.6% expected CAGR.

**PRE-COMMITTED BINARY ENTRY GATES (this quarter is the first H1 FY27 data point):**
1. FY27 **H1 CFO/PAT ≥ +0.10x** — operational entry gate (evaluated at Q1/H1 FY27).
2. **Permanent CFO successor named by 19-Aug-26** — governance entry gate.
   (CFO Subodh Kumar resigned effective 20-Jun-26; NO successor named as of 5-Jul-26.)

**HARD ENTRY STOP (DROP from watchlist entirely) if ALL of:**
H1 FY27 CFO/PAT still negative **AND** DSO > 210 days **AND** (successor CFO
not named OR from promoter family) **AND** segment-level RESCO/solar-EPC ROCE
not disclosed. (Strengthened 14-Jun-26 after 63 MW Bihar RESCO award.)

**COMMITTED Q1 FY27 CONCALL QUESTIONS (from Notion, must be checked as answered/unanswered):**
1. Total HAM/RESCO capital-allocation envelope FY27-FY28 + segment-level ROCE commitment.
2. Doon Infrapower 40% SPV partner — commercial rationale + any promoter linkage (RPT test).
3. HAM annuity 15-25yr cash cycle reconciled against existing PM-KUSUM WC drag; CFO/PAT trajectory to FY28.

**QUARTERLY MONITORING CHECKLIST (12 items):**
1. CFO/PAT (most important) — green: positive & >40%; red: negative 3rd year.
2. PM-KUSUM order book — green: >₹1,500 Cr; red: <₹800 Cr.
3. Governance / SEBI communication — red: any SEBI notice/inquiry.
4. Auditor stability — green: same auditor 2 yrs (Singhi & Co. yr 2 at FY26); red: another change.
5. Revenue growth — green: >25% YoY; red: <15%.
6. New state approvals — green: 3+ new states/yr; red: only existing states.
7. AIIB/funding-cycle normalisation (DSO) — green: DSO <150 days; red: DSO >200 days.
8. Oswal Solar HAM/EPC capital deployment — green: <10% of consol capex; red: >20% w/o ROCE disclosure.
9. Segment-level ROCE for solar EPC arm — green: disclosed & ≥18%; red: not disclosed OR <12%.
10. Doon Infrapower partner profile — red: family/promoter linkage emerges.
11. RRECL 33 MW empanelment bidding outcomes — red: silence in concall.
12. New HAM SPV announcements — red: multiple SPVs in 12 months → strategy drift.

**PRIOR-QUARTER CONTEXT (FY26 / Q4 FY26, from Notion):**
- FY26 (consol): Revenue +44% to ₹2,064 Cr; PAT +34% to ₹376 Cr; Op EBITDA margin 29.4%→24.9% (-394 bps); DSO 199 days (worsened 39 days); CFO/PAT -0.20x (3rd consecutive negative year).
- Maharashtra concentration 54.9%; scheme concentration in Magel Tyala (MSEDCL). Direct PM-KUSUM revenue declined 44% FY26 — all growth from Magel Tyala.
- Residential (PM Surya Ghar) 1.8%→15.5% of mix.
- Walso Solar now 51% subsidiary (RPT; Goela 4.3% retained). Backward integration (module + BOS + structures).
- Governance flags (5 in 9 months): undisclosed pre-IPO share transfer; 3 auditors in 3 years; Doon Infrapower opacity; Walso RPT; CFO exit.
- 04-Jul-26: MSEDCL additional 10,000-pump order ₹235.92 Cr (Magel Tyala, not RPT).
- 14-Jun-26: 63 MW Bihar RESCO LOAs (₹247 Cr install + ₹257 Cr 10-yr annuity = ₹504 Cr). RESCO = 10-yr cash recovery; Bihar DISCOM slow-pay.
- IPO listed 20-Jun-2025; ₹890 Cr fresh issue; ₹571 Cr IPO-proceeds capex deployment in flight.

---

## Gate log
- GATE A1 (concall): PASS — 100% line coverage, 150 lines, conversion x1 (Rs Cr). 2026-08-11.
- GATE A2 (concall): PASS — 145/145 turns, 9/9 Q-rounds, 53/53 number universe (30 mgmt-spoken), 28 consolidated sub-Qs, 14 AMBIGUOUS_ASR rows. 2026-08-11.
- GATE A3 (concall): PASS — all 17 checks marked (F1,F6,F7,F13,F16,F17 = FINDING; rest N.A. per concall doctype), 100% ledger reconciled, 11 findings (3 forward-signal, 6 ambiguous). 2026-08-11.
- GATE A5: pending
