# Verifier A shadow comparison: tdpowersys 2026-11-15

Built mechanically from outputs/blocks/B12a.yaml (Sonnet 5.5, verifier of record) and shadow/verifier-a-haiku.yaml (Haiku 5.5, shadow). The shadow findings count for nothing. No source page was re-checked for this table and no judgment is made on which verifier is right.

- Sonnet findings: 8 (critical 0, major 1, minor 7). Numbers checked 582; mandatory 277 of 277; acceptance 98.6%.
- Haiku findings: 4 (critical 0, major 1, minor 3). Numbers checked 243; mandatory 146 of 146; acceptance 98.4%.
- Rows marked "?" in a found column: 0. No finding matched on location or on claimed value across the two verifiers.

Matching rule: two findings are the same finding when location and claimed value match. Input column: the shadow row's tier (mandatory = Y, sample = N); a finding located in the stage 1 Gate 0 report is Y; otherwise "?".

| finding | Sonnet found (Y/N) | Haiku found (Y/N) | verdict-card / Section 1B / Gate 0 input (Y/N) |
|---|---|---|---|
| 04-bizmodel.md s1B row 5 and s2B Alstom row; 05-concall.md s3D Customers bullet. Claimed: Alstom long-term agreement dated 2020 (Pres. slide 5). Sonnet severity MAJOR. | Y | N | ? |
| 05-concall.md s1B rows and s2A row 23. Claimed: INR22 billion, INR500 million, INR40 billion and above, "month of August" at Q1C p.3. Sonnet severity MINOR. | Y | N | ? |
| 05-concall.md s0A item 1 and s1B Capacity row. Claimed: Q4C p.13, capacity to address INR32 billion for FY28. Sonnet severity MINOR. | Y | N | ? |
| 05-concall.md s3A first row and s3D Customers bullet. Claimed: Siemens 2012 licence and Alstom agreement in presentation p.4. Sonnet severity MINOR. | Y | N | ? |
| 07-emoat.md s0 item 1. Claimed: Q1C p.5, "it is not written in stone". Sonnet severity MINOR. | Y | N | ? |
| 09-tam.md s1B. Claimed: p.6, no market-share number (B04 cites p.9). Sonnet severity MINOR. | Y | N | ? |
| 04-bizmodel.md s2A competition row and s2B BRUSH row. Claimed: BRUSH Group, CG Newage, Kirloskar Electric at Pres. slide 15, 17. Sonnet severity MINOR. | Y | N | ? |
| 04-bizmodel.md s0 item 4, s4A, s4C; 05-concall.md s0A item 4; 07-emoat.md s0 item 4. Claimed: promoter holding 26.5% at 30 Sep 2026 (Pres. slide 36). Sonnet severity MINOR. | Y | N | ? |
| 02-notes.md section 3 item 7 and P3-02 sensitivity; section D question 1; section A rank 2; orchestrator appendix. Claimed: capital creditor build 1,596.63 lakh (inference that it sits in CFO). Haiku severity MAJOR, tier sample. | N | Y | N |
| 01-gate0.md section 1 ROCE table (FY26 interest), section 4 D2, section 0 item 1. Claimed: FY26 interest 7.60 Rs cr (screener Interest row); EBIT 333.72; interest cover 43.9x. Haiku severity MINOR, tier mandatory. | N | Y | Y |
| 04-bizmodel.md section 0 row 3 and section 1 cash conversion. Claimed: H1 FY27 receivables rose Rs 209.7 Cr (20,965.02 lakh). Haiku severity MINOR, tier sample. | N | Y | N |
| 04-bizmodel.md section 0 row 1. Claimed: Q2 FY27 revenue Rs 841.4 Cr. Haiku severity MINOR, tier sample. | N | Y | N |
