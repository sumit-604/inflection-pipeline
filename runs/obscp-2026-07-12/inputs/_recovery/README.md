# Annual report recovery (2026-07-12)

`inputs/annual-report/Annual_Report_2025.pdf` as delivered by collect_to_repo v3 was
truncated mid-stream: no xref table, no trailer, no %%EOF, and object 2 (the shared
/Resources dictionary that maps every page's /TPLn Form XObject) was in the lost tail.

Recovery performed by the pipeline session:
- Truncated the file at the last complete `endobj`, dropping one incomplete stream object.
- Reconstructed object 2 by reading each page's `/TPLn Do` content operator and pairing
  TPL1..TPL101 with the 101 Form XObjects in document order (verified 1:1).
- Synthesized a /Catalog pointing at the /Pages tree (object 1).
- Null-stubbed 88 referenced-but-missing objects (the truncated tail, objects ~575-662).
- Rebuilt the xref table + trailer + startxref + %%EOF.

Result: pages 1-77 render with full content and are used by all AR-reading stages.
Pages 78-101 are blank (their page images / resources were never delivered); these hold
the detailed numbered notes-to-accounts schedules. The original truncated file is kept
here as `Annual_Report_2025.ORIGINAL_corrupt.pdf` for audit.
