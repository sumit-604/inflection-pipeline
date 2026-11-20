# Stage context (TDPOWERSYS, run 2026-11-15)

Carried in every STAGE task message. Never given to verifiers.

Company: TD Power Systems Ltd (TDPOWERSYS), BSE 533553, NSE TDPOWERSYS. Run date: 2026-11-15.
Run folder (RUN): C:\Users\sumit\repos\inflection-pipeline\.claude\worktrees\step1-tdpower-4df019\runs\tdpowersys-2026-11-15
Repo root (ROOT): C:\Users\sumit\repos\inflection-pipeline\.claude\worktrees\step1-tdpower-4df019

UNITS: All figures in ₹ Cr unless the source says otherwise; the source unit is on the face of the document, not in the filename. On this corpus the results filings and the annual report print in Rs LAKH; the screener Data_Sheet and the manifest are in Rs crore. Carry the unit in every anchor. Do not convert silently.

READ ROUTE: every PDF has a page-marked text file beside it (same name, .txt, one "[page N]" marker per page). Read the .txt and cite the PDF name and page. Open the PDF itself only if the .txt is unclear at that page. Large files: read in chunks with offset and limit, or Grep first.

B00 block (inventory, input_gaps, freshness pairs): RUN\outputs\blocks\B00-inputs.yaml. Copy its input_gaps list into your block's input_gaps field.

COMPANY MEMORY (weigh it; never cite it as evidence; every number you report comes from this run's filings):
- ROOT\companies\TDPOWERSYS.md
- RUN\step1-business-brief.md

FIRST VERIFICATION PRIORITY (load-bearing facts). Before your own work, check the ones your stage's documents can settle, and state what you found with anchors:
1. Guidance vs delivery: FY27 revenue guidance Rs 2,400 cr+ -> Rs 2,600 cr (Q1 FY27 call) -> Rs 2,900-3,000 cr (Q2 FY27 presentation); H1 FY27 delivered Rs 1,481.5 cr; FY28 Rs 3,200 cr said to be capacity, not guidance.
2. Customer concentration: FY26 consolidated Customer A 23.17%, Customer B 10.74% of revenue; standalone three customers above 10% (AR segment note).
3. Cash conversion: CFO/PAT 23% FY25, 54% FY26; debtor days 146 FY26; H1 FY27 receivables Rs 742.1 cr -> Rs 952.9 cr; other current liabilities Rs 190.3 cr -> Rs 430.3 cr (nature unconfirmed).
4. Governance: promoter holding 26.51%; SAST Reg 29(1) filing 14 Nov 2026; FY26 subsidiary transactions Rs 256.3 cr (Europe GmbH) and Rs 167.1 cr (USA Inc).

Known corpus facts: the Q2 FY27 concall transcript is absent (call 13 Nov 2026, not yet filed). Corporate actions in the last 12 months include a share sub-division and a QIP or preferential allotment (see inputs/announcements). Per-share figures across periods may sit on different share bases, so state the basis.

OUTPUT RULES: write the full report to the report path and the YAML block alone to the block path BEFORE replying; reply with the block. NOT FOUND is the only valid fill for a missing number. You cannot edit a report after writing it, so check it before you finish.
