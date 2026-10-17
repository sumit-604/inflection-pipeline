# A5 ADVERSARY AUDIT: KARNIKA | h1fy27 | Loop 1 re-audit

Agent: A5 adversary, claude-opus-5-5. Run date 2026-10-17.
Review under audit: runs/karnika-h1fy27/work/review_karnika_h1fy27.md (A4, Correction Loop 1 amended in place, 1,274 lines).
Inputs read: A1 fulltexts and structured files (results, concall, presentation), A2 ledgers (three), A4 review. No source PDF and nothing under inputs/ was opened. A3 reasoning and the prior audit were not read. Every figure below was re-derived from the A1 fulltext at the cited line.

Anchor key: `res Lnnn` = results fulltext line; `cc Lnnn` = concall fulltext line; `ppt lnnn` = presentation fulltext line; `rev Lnnn` = line in the A4 review. Money in Rs lakhs unless marked Cr.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading in review | Content | Status |
|---|---|---|---|
| 1 Summary narrative | "## 1. SUMMARY NARRATIVE" (rev L1112) | 16 numbered lines (rev L1114-L1129), inside the 10-20 line band | present |
| 2 Sector intelligence | "## 2. SECTOR INTELLIGENCE" (rev L1131) | 6 bullets: market size and CAGR, fragmentation, cotton cycle, seasonality, trade credit, ND list | present |
| 3 Business-model intelligence | "## 3. BUSINESS-MODEL INTELLIGENCE" (rev L1140) | 7 bullets: channel, margin, capital, Kidcity, deal economics, drift, ND list | present |
| 4 Competition intelligence | "## 4. COMPETITION INTELLIGENCE" (rev L1150) | 5 bullets: claimed edge, named peers, buying-house power, retail entry, switching risk | present |
| 5 Forward map | "## 5. FORWARD MAP" (rev L1158) | make-or-break reading plus 8 dated catalysts, each with a bull fork and a bear fork | present |

Gate: PASS. All five parts present and non-empty.

---

## 1. COVERAGE AUDIT

Fresh pass method: regex and line sweep over each A1 FULLTEXT, then diff against the A2 ledger and the A1 structured IDs.

| Doc | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| results | notes (numbered 1-6, 11-13 printed twice; 2 unnumbered comparatives) | 20 | 20 (res L290-L349, L584-L648) | none | PASS |
| results | line items (6 tables) | 210 | 210 (BS 29, P&L 26, CF 44, consol BS 32, consol P&L 35, consol CF 44) | none | PASS |
| results | agenda items | 1 | 1 (res L44-L50) | none | PASS |
| results | auditor paragraphs | 8 | 8 (res L90-L115, L369-L394) | none | PASS |
| results | group entities | 4 | 4 (parent, Kidcity, Elementa Lifespaces, RDB Elementa) | none | PASS |
| results | structured IDs referenced | 780 | 780 (R001 res L137 to R780 res L673; ledger ID accountability) | none | PASS |
| concall | speaker turns | 167 | 167 (speaker-label regex; 9 further label-like hits are cover lines L24-L78) | none | PASS |
| concall | analyst questions | 67 | 67 (77 analyst turns less 8 sign-offs T37, T64, T89, T113, T117, T134, T140, T163 and 2 audibility checks T13, T67) | none | PASS |
| concall | participants | 8 | 8 | none | PASS |
| concall | management numbers | 105 | **106** | none | **FAIL (A2)**: cc L378 "There are basically two growth drivers for us" (CFO, T24) is in neither the structured file nor the ledger. Same class as R040 "three" models (cc L264), R042 "four" models (cc L270) and M004 "two methods of billing" (cc L901) |
| concall | forward statements (management) | 47 | **54 core; 57 incl. secondary** | none | **FAIL (A2)**: absent from FORWARD rows R158-R204 and from the ledger: cc L156-160 ("Our objective is to combine these capabilities to expand market access"), L196-199 ("Our priority will be to execute consistently, convert growth into earnings"), L228-230 ("Our focus remains on managing costs ... to support sustainable and profitable growth"), L521-524 ("our margins will grow much higher"), L684-685 ("some ... will be on the airports, majority will be in the high-street ... malls"), L704-707 ("we will also have this live online and we will be available in all the high-end malls"), L1094-1095 ("Hopefully, we will achieve next milestones"). Secondary: L531, L869-870, L1051-1053. A2's forward count test re-counted A1 tags against A1 tags, so it could not catch these |
| concall | hedge phrases (A4 Step 6C) | protocol list 6; other 11 | 6 and 11, line for line (cc L137, L196; L437, L471; L411, L1095; "I think" L346, L437, L490, L491, L712; "maybe" L471, L547, L565, L571; L403; L698) | none | PASS |
| concall | structured IDs referenced | 246 | 246 | none | PASS |
| presentation | slides (pages) | 32 | 32 (page markers ppt l17-l599) | none | PASS |
| presentation | slide numbers | 445 | 445 (slide sum: 1+12+1+3+19+8+20+28+112+8+6+3+1+1+8+4+22+4+68+116) | none | PASS |
| presentation | structured IDs referenced | 553 | 553 | none | PASS |

Ledger-row disposition in A4: the preamble marks all 20 notes, 167 turns and 32 slides reviewed and states "No unreviewed row" (rev L34). Every A2-flagged results row and cc R240 carries a one-line disposition (rev L49-L55). All 69 A3 IDs are listed (rev L36, L1187). All 67 questions appear in the Q&A inventory (rev L763-L829). No orphan row. A2-flagged presentation rows carry no one-line disposition (STYLE S1).

Coverage result: **FAIL, loop to A2** for the two concall categories above (findings M1, M2).

---

## 2. ARITHMETIC AUDIT

Every derived figure was recomputed from raw lakhs. Rounding tolerance is the last printed digit.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Standalone Q2 FY27 op EBITDA, margin | 15.16 Cr, 18.53% | 1,516.12; 18.528% | res L189, L190, L197, L198, L201 | PASS |
| Standalone Q2 FY26 op EBITDA, margin | 14.45 Cr, 20.72% | 1,444.62; 20.718% | same lines, col 3 | PASS |
| Standalone Q1 FY27 / H1 FY27 / H1 FY26 / FY26 op margin | 17.28 / 18.00 / 18.86 / 15.57% | 17.279 / 18.000 / 18.864 / 15.573 | res L189-L201 | PASS |
| Standalone reported EBITDA, core PBT, OI/PBT (all 6 columns) | per 1-S table | all tie (e.g. FY26 43.61, 27.91, 23.72%) | res L189-L201 | PASS |
| Standalone ETR Q2 FY26 / Q1 / Q2 / H1 FY26 / H1 FY27 / FY26 | 26.41 / 29.27 / 26.35 / 26.26 / 27.56 / 27.09% | 26.411 / 29.269 / 26.346 / 26.264 / 27.558 / 27.094 | res L201-L205 | PASS |
| Standalone gross margin Q2 FY26 / Q1 FY27 / Q2 FY27 / H1 FY26 / H1 FY27 / FY26 | 38.54 / 37.48 / 38.64 / 41.99 / 38.15 / 36.37% | 38.536 / 37.479 / 38.640 / 41.991 / 38.150 / 36.370 | res L193-L195 | PASS |
| Q1 FY26 gross margin (derived H1 minus Q2) | 49.23% | 49.230% (COGS 1,689.93 on 3,328.59) | res L189, L193-L195 | PASS |
| Q2 material-plus-conversion spread | 21.89% vs 23.56%, -167 bps | 21.886% vs 23.556% | res L193-L195, L199 | PASS |
| Standalone Q2 YoY: revenue / op EBITDA / core PBT / PBT / PAT | +17.4 / +4.9 / +7.4 / +15.1 / +15.2% | +17.36 / +4.95 / +7.41 / +15.11 / +15.21% | res L189-L206 | PASS |
| Standalone H1 YoY: revenue / op EBITDA / core PBT / PAT | +37.5 / +31.2 / +40.8 / +45.8% | +37.46 / +31.17 / +40.85 / +45.77% | res L189-L206 | PASS |
| Share-adjusted EPS (PAT / 619.975 lakh) | 1.51 / 1.19 / 1.74 / 2.01 / 2.93 / 4.30 | 1.514 / 1.186 / 1.745 / 2.011 / 2.931 / 4.303 | res L206, L214 | PASS |
| Implied weighted shares from reported EPS | 285.4 / 205.3 / 416.2 lakh | 285.37 / 205.34 / 416.18 | res L217 | PASS |
| PAT bridge Q2 (sum of components) | +1.43 Cr; shares 175.6 / -125.5 / 16.7 / -1.1 / 69.3 / -35.7 / 0.7% | components sum to 142.80 lakh; shares tie | res L189-L206 | PASS |
| PAT bridge H1 | +5.70 Cr; shares 127.6 / -21.4 / 7.2 / 0.3 / 29.7 / -37.6 / -5.7% | 570.43 lakh; shares tie | res L189-L206 | PASS |
| OI share of Q2 PBT gain; PAT if OI reverts | 51%; 10.09 Cr, +7.4% | 51.3% (98.98 / 192.76); 1,008.78, +7.45% | res L190, L201 | PASS |
| Consolidated op EBITDA margin Q1 / Q2 / H1 / FY26 | 17.23 / 18.79 / 18.15 / 14.99% | 17.231 / 18.791 / 18.151 / 14.993 | res L469-L481 | PASS |
| Consolidated ETR, gross margin, PAT margin (4 columns) | per 1-C table | all tie | res L469-L488 | PASS |
| H2 FY26 group revenue / op margin / core PBT | 145.47 Cr / 12.25% / 14.32 Cr | 14,546.60 / 12.251% / 1,431.58 | res L469-L481, L189-L201 | PASS |
| Kidcity implied (C minus S) H1 revenue / op EBITDA / PAT / PAT margin | 38.36 / 7.18 / 5.30 Cr / 13.8% | 3,836.44 / 717.73 / 530.42 / 13.83% | res L469, L486; L189, L206 | PASS |
| NCI tie-out, H1 and FY26 | 530.40 vs 530.42; 170.92 vs 170.93 | same | res L499, L486, L206 | PASS |
| Q1 FY27 NCI = 25% of Kidcity Q1 tax | 0.15 Cr | 25% x (364.15 - 304.23) = 14.98 | res L483-L484, L203-L204, L499 | PASS |
| Kidcity consideration, route A / route B | 367.42 / 367.43 lakh | 2,552.91 - 2,169.96 - 15.53 = 367.42; (160.53 - 42.73) / 0.25 x 0.75 + 14.03 = 367.43 | res L140, L420, L487, L439, L499, L418 | PASS |
| Price / TTM PAT; / first half annualised; / book | 0.70x; 1.43x; 1.04x | 489.89 / 701.35 = 0.699; 489.89 / 341.86 = 1.433; 367.42 / 353.40 = 1.040 | as above | PASS |
| Mar-26 FVOCI omission (investments / DTA / Other Equity) | +251.03 / -57.43 / +193.59 | 2,359.43 + 251.03 - 367.42 = 2,243.04; 85.16 - 57.43 + 0.69 = 28.42; 3,635.61 - 3,442.02 = 193.59; 3,442.02 + 2,219.80 = 5,661.82 | res L140, L420, L142, L422, L437, L507, L504 | PASS |
| 5-K Kidcity receivables / inventory / borrowings / cash | >=35.40 / >=3.96 / 4.61 / 0.04 Cr | 3,540.14 / 395.72 / 460.66 / 4.11 | res L427, L147, L425, L145, L444, L449, L163, L168, L428, L148 | PASS |
| Standalone CFO/PAT, FCF, WC change | -0.27x; (1.79); (23.85) | -0.269; -179.07; -2,385.42 | res L259, L206, L264, L255 | PASS |
| Standalone receivable / inventory / payable days, CCC | 109.7 to 141.7; 129.5 to 121.0; 41.9 to 64.0; 197.3 to 198.7 | 109.70 to 141.65; 129.54 to 121.00; 41.90 to 63.99; 197.34 to 198.66 | res L145-L147, L170-L171, L189, L193-L195 | PASS |
| Consolidated CCC as computed / scope-matched | 182.2 to 159.5 / 151.9 to 159.5 | 182.23 to 159.47 / 151.90 (110.00 + 100.67 - 58.77) | res L425, L427, L451-L452, L469-L475 | PASS |
| Net debt and ND/E (standalone, consolidated, corrected) | 70.40 to 78.61; 75.23 to 83.17; 0.74 / 0.63 / 0.75 / 0.77 / 0.62x | 7,039.64 to 7,860.78; 7,523.47 to 8,317.33; ratios tie | res L148, L163, L168, L159; L428, L444, L449, L440 | PASS |
| FY26 consolidated ROCE / ex-OI / on corrected equity | 25.2 / 20.3 / 25.5% | 25.23 / 20.28 / 25.52% | res L481, L477, L470, L440, L444, L449 | PASS |
| H1-annualised ROCE incl. / ex OI on avg CE 196.28 | 35.7 / 32.8% | 35.71 / 32.84% | res L481, L477, L470 | PASS |
| SC PAT gap FY26 / Q1 / Q2 / H1; parent vs standalone H1 | 6.4 / 24.3 / 32.5 / 29.2%; +21.0% | 6.41 / 24.29 / 32.53 / 29.19%; +21.04% | res L486, L206, L498 | PASS |
| Elementa annualised loss, 40% and 100% | 0.82 Cr; 2.05 Cr | 82.15; 205.4 lakh (15.53 x 365 / 69) | res L348, L487 | PASS |
| Implied H2 FY27 needs (standalone; group) | 127.53-138.74 Cr; 143.05-155.48 Cr | same | res L189 | PASS |
| Component-guide CAGR to FY28 | 42.3-48.8% | 42.27-48.84% | cc L189, L403-L412, L821 | PASS |
| Q&A grade tally | A22 B28 C14 D2 n/a1 = 67 | counted row by row: same | rev L763-L829 | PASS |
| **Share of H1 consolidated OI from interest, MF gain and PPE gain (Step 6.5, rev L539)** | **92%** | **89.1%** (250.63 / 281.44). 92% is the standalone share (250.63 / 272.53) | res L470, L532, L533, L537; L190 | **FAIL (F1)** |
| **Concall specificity ratio (Step 6B, rev L924)** | **24/47 = 0.51, "above 0.5"** | **24/49 = 0.49** with the two Forward Soft statements A4's own Step 1 types (cc L198-199, L228-230; rev L697, L703). About 24/54 = 0.44 on the fresh-pass set | cc L196-L199, L228-L230 | **FAIL (C1)** |

---

## 3. ADVERSARIAL READ

### Claim 1 (most positive). Kidcity was bought cheaply (1-K2, rev L210-L239; Brief part 3, rev L1146; Brief line 10, rev L1123)
A4: about Rs 3.67 Cr for 75%. That is about 0.70x Kidcity TTM PAT and 1.04x deal-date book. Karnika's 75% share of TTM PAT (Rs 5.26 Cr) exceeds the price.

**Mandatory multiple, stated.** About Rs 3.67 Cr consideration / (75% x target TTM PAT Rs 7.01 Cr = Rs 5.26 Cr) = **about 0.70x earnings**. On the first post-deal half annualised (H2 FY26 PAT Rs 1.71 Cr x 2), the multiple is 1.43x. On book it is 1.04x. Pre-deal earnings: ND. The TTM year holds the festive Q2 FY27 peak and the post-integration margin (7.1% to 13.8%), so it is a peak-shaped year, not a representative one.

**Strongest bear counter, from the extract: the earnings that make the price look cheap did not turn into cash.**
- Kidcity H1 FY27 operating cash flow is consolidated CFO minus standalone CFO: (440.63) - (487.90) = **+47.27 lakh, Rs 0.47 Cr** (res L553, L259). Intra-group flows net to zero across the two entities, so this difference is Kidcity's own CFO whether or not the group eliminates intra-group items.
- Kidcity H1 PAT is 530.42 lakh (res L486 minus L206). **CFO/PAT = 0.09x** [derived].
- Kidcity's receivable build in the CF statement absorbed 1,485.42 lakh (res L542 minus L248). Its working capital took 501.37 lakh in total (res L549 minus L255), and its tax paid was 178.00 lakh (res L552 minus L258).
- Kidcity's whole H1 operating cost is staff 48.91 lakh (res L476 minus L196) plus other expenses 59.14 lakh (res L479 minus L199) = 108.05 lakh, **2.8% of revenue** [derived]. That is a business described on the call as running 85-plus SIS counters, one EBO, one kiosk, a website and aggregation (cc L163-L165, L262-L270, L844, L1019). Two readings fit: Kidcity is a wholesale book, or group costs sit in Karnika and flatter Kidcity's margin [INFERENCE].
- Survives: YES. A4's 1-K2 lists debt and receivables but no cash-conversion test for Kidcity. The 0.70x prices one peak-shaped accrual year that converted 9% to cash. **Graft into A4 (MISSING, M3).** Separating observation: Kidcity FY27 CFO and Karnika's sales to Kidcity (Q15).

**Second acquisition in the filing (probe also applied).** Elementa Lifespaces: Rs 2.00 Cr for 40% at face value (res L343-L348). Implied 100% equity Rs 5.00 Cr. Target earnings: loss. Group share (15.53) lakh in 69 days, about Rs (0.82) Cr a year for the 40% and Rs (2.05) Cr at 100% [derived]. Multiple: negative. Business and related-party status: ND. A4 already carries this bear reading (Q6, Step 6.5). No new graft. RDB Elementa: Rs 5.20 lakh for 26%, not allotted, earnings ND (res L337-L342). Immaterial.

### Claim 2. Kidcity delivered its margin guide (6A-M rev L502; Step 3 delivery table rev L754; 7A rev L965)
A4: H1 implied PAT margin 13.8% against the 10-13% guide (cc L418), "Delivered or above" and "CONFIRMED on the reported split".
- Bear counter 1, transfer prices and NCI leakage: already grafted in Loop 1 (rev L502, L754, L965). Survives; no new action.
- Bear counter 2, from the extract: the margin is not cash. CFO/PAT 0.09x and opex 2.8% of revenue (Claim 1 above). The 6A-M, Step 3 and 7A rows grade delivery on accrual margin alone. Survives. **Same graft as M3:** add the CFO/PAT line to those three rows.

### Claim 3. "The business grows" on a like-for-like basis (Step 2 rev L247-L249; note U row rev L101; Brief lines 2 and 15, rev L1115, L1128; Section C rev L1067, L1070; flag rev L1254)
A4: consolidated YoY is not comparable, so standalone is the like-for-like base. Standalone revenue rose +17.4% in Q2 and +37.5% in H1, and PAT rose +45.8% in H1.

**Strongest bear counter, from the extract: standalone revenue includes Karnika's sales to its own new subsidiary.**
- Kidcity joined the group on 04-Oct-2025 (res L318). That is after both base periods (Q2 FY26 and H1 FY26).
- The CFO ties Karnika's growth to Kidcity: "Karnika is also doing pretty good because 60% of the goods what we are selling via Kidcity, these are the production will be held by the Karnika only. So, Karnika's production itself will grow up." (cc L425-L427).
- Kidcity's purchases of stock-in-trade (C minus S) were 1,337.35 lakh in Q2 (res L474 1,917.77 minus L194 580.42) and 2,668.10 lakh in H1 (3,500.69 minus 832.59). Kidcity consumes no raw material (consolidated COMC equals standalone, res L473 vs L193).
- Illustrative sizing [INFERENCE]. Assume 60% of those purchases came from Karnika and Karnika sold nothing to Kidcity in the base periods. Then Karnika's sales to Kidcity are about Rs 8.0 Cr in Q2 and Rs 16.0 Cr in H1. Standalone third-party revenue then grew about **+5.9% in Q2** (73.81 vs 69.73) and **+21.9% in H1** (125.60 vs 103.01), against the +17.4% and +37.5% A4 labels like-for-like.
- A4's own 1-K2 says the margin step-up "came after Karnika began making 60% of Kidcity's goods" (rev L231). By that reading the intra-group supply is new since the base period. The like-for-like label never carries this qualifier.
- A4's only link between intra-group sales and standalone growth inverts the mechanism: "If intercompany sales are not eliminated, standalone growth is overstated" (rev L864). Standalone revenue includes these sales whether or not the group eliminates them on consolidation. Non-elimination overstates consolidated revenue and the 52.3% / 74.7% headline (FACTUAL, F3).
- Survives: YES. The magnitude is ND until Q15 is answered, but the direction is extract-supported. **Graft into A4 (MISSING, M4)**: qualify every "like-for-like" use of standalone YoY. Separating observation: Karnika's Q2 and H1 sales to Kidcity, and any sales to Kidcity before the deal (Q15).

---

## 4. OTHER FINDINGS (factual audit of bear claims, same bar as bull claims)

**F2 (FACTUAL, A4). "Continue with this debt level" is labelled contradicted. The extract does not support that label.**
- The analyst asked about future expansion: "if we do so much expansion, what will happen to the debt? Will you maintain the same debt or take more?" (cc L977-L978). The CFO answered: "we do not want to grow the debt too much. We want to continue with this debt level" (cc L981).
- The statement is forward intent from the Sep-26 level. It was made on 13-Oct-2026, after the H1 rise.
- A4 labels it "Contradicted in the half" (rev L503), "Contradicted in the period it describes" (rev L752) and CONTRADICTED (rev L968). Its own 6A-M row names the guide "Debt held at current level" (rev L503).
- The H1 net debt rise of Rs 8.21 Cr (res L148, L163, L168) precedes the statement. It is an undisclosed fact on the call, not a contradiction.
- Fix: relabel the item as "forward intent, not testable yet; H1 rise of Rs 8.21 Cr undisclosed on the call; test against FY27 net debt vs Rs 78.61 Cr standalone". Cut the same-quarter contradiction count from four to three in 6E (rev L947), the Concall Verdict block (rev L1054), 8E (rev L1036), Step 5 (rev L446), Section C (rev L1069) and the flag (rev L1263). The other three items stand: retained-earnings funding (cc L990-L991), operating-leverage mechanism (cc L221) and Kidcity "no debtors" (cc L828-L831).

---

## 5. FINDINGS REGISTER

| ID | Type | Loop to | Finding |
|---|---|---|---|
| M1 | MISSING | A2 | Concall management number cc L378 "two growth drivers" (CFO, T24) is absent from the structured file and the ledger. Append it as M006 |
| M2 | MISSING | A2 | Concall forward statements are absent from FORWARD rows R158-R204 and the ledger: cc L156-160, L196-199, L228-230, L521-524, L684-685, L704-707, L1094-1095 (secondary L531, L869-870, L1051-1053). Append them as MISSING_FROM_STRUCTURED. Replace the circular forward count test (A1 tags vs A1 tags) with a fulltext sweep |
| C1 | CONTRADICTION | A4 | Step 6B specificity uses A1's 47 FORWARD rows. That set omits cc L198-199 and L228-230, which A4's own Step 1 types as Forward Soft (claims 19, 25). Corrected: 24/49 = 0.49 on A4's typing, about 0.44 on the M2 set. Both sit below the 0.5 line A4 cites. Restate 6B (rev L924), 6E (rev L946-L947), the Concall Verdict block (rev L1056) and the OVERPROMISER lean, and cite the M2 rows |
| F1 | FACTUAL | A4 | Step 6.5 (rev L539) gives "OI 2.81 Cr H1 consolidated, 92% from interest, MF gains and a PPE gain". The consolidated share is 89.1% (250.63 / 281.44). 92% is the standalone share |
| F2 | FACTUAL | A4 | "Continue with this debt level" (cc L981) is labelled contradicted. It is forward intent from the Sep-26 level, made after the H1 rise. Relabel it and cut the same-quarter contradictions from four to three (section 4) |
| F3 | FACTUAL | A4 | Exchange 3 (rev L864) says non-elimination overstates standalone growth. The mechanism is inverted: standalone includes intra-group sales regardless, and non-elimination overstates consolidated revenue |
| M3 | MISSING | A4 | Surviving bear counter, Claims 1 and 2: Kidcity H1 CFO +Rs 0.47 Cr on PAT Rs 5.30 Cr (0.09x), and opex 2.8% of revenue. Graft into 1-K2 quality markers and bear reading, 6A-M, the Step 3 delivery table, 7A and Brief part 3 |
| M4 | MISSING | A4 | Surviving bear counter, Claim 3: standalone "like-for-like" YoY includes Karnika's sales to Kidcity, which joined after both base periods (res L318; cc L425-L427; res L474, L194). Qualify it in Step 2, the note U row, 2-S/2-H, 6A-M (Karnika 20-25% row), the Brief (lines 2 and 15), Section C and the flags. Add the illustrative sizing (about +6% Q2, +22% H1 ex intra-group, [INFERENCE]) |

---

## VERDICT

**INCOMPLETE.** The review fails on FACTUAL (F1-F3), MISSING (M1-M4) and CONTRADICTION (C1) findings.
- Failing agents, in pipeline order: **A2** first (M1, M2: append rows to the concall ledger), then **A4** (C1, F1, F2, F3, M3, M4).
- **A3:** no new forensic work is expected. The new ledger rows restate content A4 already reads (Step 1 claims 8, 19, 25; Q&A rows 8, 19, 32, 34). A4 must cite them or mark them "reviewed, no finding".
- No finding moves the protocol verdict (PROCEED WITH FLAGS) or the cash class (INDETERMINATE-WITH-DIRECTION).
- Loop 1 fixes verified: the 1-K2 price routes, the FVOCI three-line tie, the scope-matched CCC, the 5-K balances, the "maybe" count of 4, the q36 inventory row and the timeline column reading all hold.

## STYLE NOTES (logged, no loop)

- S1. Several A2-flagged presentation rows have no one-line disposition: MAPPING_UNRESOLVED R018-R036 (S8 product mix), SERIES_UNRESOLVED R055-R064, YEAR_BY_X_POSITION R205-R209, LOGOS_NOT_IN_TEXT R458, FOOTNOTE_PAIRED R546-R547 and PERIOD_NOT_STATED R548. The results and concall A2-flagged rows each got one (rev L49-L55). Add one line each.
- S2. 1-K2 (rev L231) says the margin step-up "came after Karnika began making 60% of Kidcity's goods". The transcript gives no start date (cc L425-L426). Tag the line [INFERENCE].
- S3. Q21 (rev L610) says airport economics "moved from loss to profit in three turns". The CFO said "break-even at the maximum" (cc L547-L548), then "might get profitability" (cc L565), then "profitable" at 15 pieces a day (cc L572). Write "from break-even at best to profitable".
- S4. Q23, F1 and P5 (rev L612, L1044, L520) set Kidcity H2 thresholds on management's rounded H1 Rs 40 Cr. On the filed C minus S Rs 38.36 Cr, the FY27 low end needs H2 Rs 41.64 Cr (Rs 6.94 Cr a month). State the basis.
- S5. Q2 (rev L591) sets "Receivables +63.1%" (Sep-26 vs Mar-26 balance) against "revenue +37.5%" (H1 YoY). These are two bases. Name both.

---

```yaml
stage: A5-adversary
company: "KARNIKA"
quarter: "h1fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger:
    - "concall mgmt_numbers: cc L378 'two growth drivers' (CFO, T24); append as M006 (same class as R040, R042, M004)"
    - "concall forward statements absent from FORWARD rows R158-R204: cc L156-160, L196-199, L228-230, L521-524, L684-685, L704-707, L1094-1095; secondary L531, L869-870, L1051-1053; append as MISSING_FROM_STRUCTURED"
arithmetic_mismatches:
  - {metric: "Share of H1 consolidated OI from interest, MF gain, PPE gain (Step 6.5, rev L539)", a4_value: "92%", recomputed: "89.1% (250.63 / 281.44 lakh); 92% is the standalone share (250.63 / 272.53)", source_line: "res L470, L532, L533, L537, L190"}
  - {metric: "Concall specificity ratio (Step 6B, rev L924)", a4_value: "24/47 = 0.51 (above 0.5)", recomputed: "24/49 = 0.49 with A4's own Forward Soft claims 19 and 25; about 24/54 = 0.44 on the fresh-pass set", source_line: "cc L196-199, L228-230; rev L697, L703"}
surviving_bear_counters:
  - {claim: "Kidcity bought cheaply: ~Rs 3.67 Cr for 75% = ~0.70x TTM PAT Rs 7.01 Cr, 1.04x book (1-K2)", counter: "Kidcity H1 CFO +Rs 0.47 Cr (consol (440.63) minus standalone (487.90) lakh) on PAT Rs 5.30 Cr = 0.09x; receivable build 14.85 Cr; opex 2.8% of revenue; the 0.70x prices a peak-shaped accrual year", source_line: "res L553, L259, L486, L206, L542, L248, L476, L196, L479, L199", type: MISSING}
  - {claim: "Kidcity delivered its 10-13% PAT margin guide at 13.8% (6A-M, Step 3, 7A)", counter: "transfer-price and NCI reading already grafted; add the same cash test (CFO/PAT 0.09x) to the three delivery rows", source_line: "cc L418; res L553, L259", type: MISSING}
  - {claim: "The business grows like-for-like: standalone Q2 +17.4%, H1 +37.5% (Step 2, Brief, Section C)", counter: "standalone includes sales to Kidcity, acquired 04-Oct-2025 after both base periods; CFO ties Karnika growth to making 60% of Kidcity goods; Kidcity purchases Rs 13.37 Cr Q2, Rs 26.68 Cr H1; illustrative ex-intra growth ~+6% Q2, ~+22% H1 [INFERENCE]", source_line: "res L318, L474, L194; cc L425-427, L395-396", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): Step 6.5 OI share 92% is the standalone basis; consolidated is 89.1% (res L470, L532, L533, L537)"
    - "F2 (A4): 'continue with this debt level' (cc L981) is forward intent from the Sep-26 level, made after the H1 rise; relabel from CONTRADICTED and cut same-quarter contradictions from four to three (rev L446, L503, L752, L947, L968, L1036, L1054, L1069, L1263)"
    - "F3 (A4): rev L864 says non-elimination overstates standalone growth; mechanism inverted, since standalone includes intra-group sales regardless and non-elimination overstates consolidated revenue"
  missing:
    - "M1 (A2): cc L378 'two growth drivers' absent from structured file and ledger"
    - "M2 (A2): seven core plus three secondary management forward statements absent from FORWARD rows and ledger (cc L156-160, L196-199, L228-230, L521-524, L684-685, L704-707, L1094-1095; L531, L869-870, L1051-1053)"
    - "M3 (A4): Kidcity cash test absent from 1-K2 and the margin-delivery rows: CFO +Rs 0.47 Cr on PAT Rs 5.30 Cr (0.09x), opex 2.8% of revenue"
    - "M4 (A4): standalone like-for-like YoY carries no intra-group qualifier (Kidcity joined after both base periods; cc L425-427)"
  contradiction:
    - "C1 (A4): Step 6B specificity denominator omits cc L198-199 and L228-230, which A4 Step 1 types Forward Soft; ratio 0.51 becomes 0.49 (below the 0.5 A4 cites in 6E), ~0.44 on the fresh-pass set"
  style:
    - "S1: A2-flagged presentation rows (R018-R036, R055-R064, R205-R209, R458, R546-R548) lack one-line dispositions"
    - "S2: 1-K2 (rev L231) asserts when Karnika began supplying Kidcity; the transcript gives no date; tag [INFERENCE]"
    - "S3: Q21 'from loss to profit' should read 'from break-even at best to profitable' (cc L547-548, L565, L572)"
    - "S4: Q23, F1, P5 Kidcity H2 thresholds use mgmt's Rs 40 Cr H1; on filed Rs 38.36 Cr the low end needs H2 Rs 41.64 Cr; state basis"
    - "S5: Q2 'receivables +63.1% vs revenue +37.5%' mixes balance change and H1 YoY; name both bases"
loop_back_to: "A2"
gap: "A2: append concall ledger rows M006 (cc L378 'two growth drivers') and forward statements cc L156-160, L196-199, L228-230, L521-524, L684-685, L704-707, L1094-1095 (+ L531, L869-870, L1051-1053) as MISSING_FROM_STRUCTURED. A3: no new forensic work expected. Then A4: (C1) restate specificity on the completed denominator (0.49 on A4's own typing) in 6B, 6E, Concall Verdict block and OVERPROMISER lean, citing the new rows; (F1) Step 6.5 OI share 92% to 89% consolidated; (F2) relabel 'continue with this debt level' as untested forward intent with an undisclosed H1 rise and cut contradictions four to three; (F3) fix rev L864 mechanism; (M3) graft Kidcity H1 CFO +0.47 Cr vs PAT 5.30 Cr (0.09x) and opex 2.8% into 1-K2, 6A-M, Step 3, 7A, Brief part 3; (M4) qualify every standalone like-for-like YoY with intra-group sales to Kidcity (res L318, L474, L194; cc L425-427) plus illustrative sizing [INFERENCE]."
style_notes:
  - "S1: add one-line dispositions for A2-flagged presentation rows R018-R036, R055-R064, R205-R209, R458, R546-R548"
  - "S2: tag the 1-K2 'came after Karnika began making 60%' line [INFERENCE]"
  - "S3: Q21 wording, break-even at best to profitable, not loss to profit"
  - "S4: Q23, F1, P5 thresholds: state mgmt Rs 40 Cr vs filed Rs 38.36 Cr basis"
  - "S5: Q2 receivables vs revenue growth: name the two bases"
analyst_note: "Loop 1 fixes hold. I recomputed every derived figure from raw lakhs and all tie, except two: the Step 6.5 OI share (92% is the standalone basis; consolidated is 89%) and the specificity ratio. The ratio sits on A1's 47 forward rows. The fulltext holds at least seven more management forward statements, two of which A4 itself types Forward Soft, so the ratio falls below 0.5. Two bear counters survive and are not in the review. Kidcity's H1 cash flow (consolidated minus standalone CFO, exact regardless of eliminations) is +Rs 0.47 Cr on PAT Rs 5.30 Cr, so the 0.70x multiple prices accrual earnings. Standalone 'like-for-like' growth includes sales to Kidcity, which joined after both base periods; the CFO ties Karnika's growth to that supply, and A4's L864 inverts the mechanism. One bear claim overreaches: 'continue with this debt level' is forward intent stated after the H1 rise, so it is undisclosed, not contradicted. No finding moves PROCEED WITH FLAGS. The A2 fix is an append only."
```
