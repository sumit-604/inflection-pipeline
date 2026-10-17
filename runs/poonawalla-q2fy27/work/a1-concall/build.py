import collections
rows=[l.rstrip('\n').split('|') for l in open('work/a1-concall/rows.txt',encoding='utf-8') if l.strip()]
c=collections.Counter(r[0] for r in rows)
out=[f"R{i:03d} | page {r[1]} | line {r[2]} | {r[0]} | {r[3]} | {r[4]}" for i,r in enumerate(rows,1)]
n=len(rows)
hdr=f"""=== A1 STRUCTURED EXTRACTION ===
source: Poonawalla_Q2FY27_Concall_Transcript.pdf (concall, Q2 FY27)
fulltext: runs/poonawalla-q2fy27/extracted/poonawalla-concall-q2fy27-fulltext.md (line numbers refer to that file; page = PDF page marker)
row_id_range: R001-R{n:03d}
counts: NUMBER {c['NUMBER']} | ENTITY {c['ENTITY']} | FORWARD {c['FORWARD']} | DATE {c['DATE']} | QUALIFIER {c['QUALIFIER']}
note: transcript running page Page N of 18 = PDF page N+1. No ZERO_STANDING values present. Rows grouped by type, page order within type.
format: R### | page N | line L | TYPE | verbatim value | short context

"""
open('extracted/poonawalla-concall-q2fy27-structured.md','w',encoding='utf-8').write(hdr+'\n'.join(out)+'\n')
y=f"""stage: A1-extractor
company: "POONAWALLA"
quarter: "q2fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
page_count: 19
formfeed_count: 19
line_count: 1093
unit_convention: "Crores"
conversion_factor_to_cr: "x1"
text_layer_present: true
extraction_mode: text-only
render_candidates: []
rendered_pages: []
page_coverage_pct: 100
detected_quarter: "Q2 FY27"
fulltext_path: "runs/poonawalla-q2fy27/extracted/poonawalla-concall-q2fy27-fulltext.md"
structured_path: "runs/poonawalla-q2fy27/extracted/poonawalla-concall-q2fy27-structured.md"
structured_counts:
  number: {c['NUMBER']}
  entity: {c['ENTITY']}
  forward: {c['FORWARD']}
  date: {c['DATE']}
  qualifier: {c['QUALIFIER']}
structured_id_range: "R001-R{n:03d}"
gate_a1: pass
gap_note: ""
"""
open('work/blocks/a1-concall.yaml','w').write(y); print(y)
