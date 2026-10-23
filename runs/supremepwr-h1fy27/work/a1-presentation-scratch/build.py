import subprocess,datetime
pdf='inputs/SupremePower_H1FY27_Presentation.pdf'
t=open('work/a1-presentation-scratch/raw.txt',encoding='utf-8',errors='replace').read().split('\f')[:41]
annex={4,5,31,33,34,35,36,37,38,40}
body=[]
for i,x in enumerate(t):
    p=i+1
    body.append('[page %d]'%p)
    ls=[l.rstrip() for l in x.strip('\n').split('\n')]
    ls=[l for l in ls if l.strip()] 
    body+=ls
    if p==2: body.append('[no text layer on this page; title slide image, skipped: no data]')
    if p in annex:
        r=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'-raw',pdf,'-'],capture_output=True,text=True,encoding='utf-8',errors='replace').stdout
        body.append('[page %d RAW-ORDER SUPPLEMENT (pdftotext -raw, same page; reading-order text of same layer)]'%p)
        body+=[l.rstrip() for l in r.split('\n') if l.strip()]
nb=len(body)
hdr=f"""=== A1 EXTRACTION HEADER ===
source_filename: SupremePower_H1FY27_Presentation.pdf
doctype: presentation
page_count_pdfinfo: 41
formfeed_count: 41
line_count: LINECOUNT
unit_convention: Crores (slide footers "All Figures In Cr", "In Cr"; page 1 cover letter and page 3 disclaimer carry no figures)
conversion_factor_to_cr: x1 (share price/EPS/BVPS in Rs; capacities in MVA; margins in %)
text_layer_present: yes
extraction_mode: text-only
render_candidates: [page 2: zero characters, title slide photo "Transforming Capacity Into Growth"; skipped: no data]
rendered_pages: [page 2 rendered at 50 dpi for inspection only, no OCR, no data present (title/cover picture); no other page rendered]
page_coverage: 100%
detected_quarter: H1 FY27 (half year ended 30-Sep-2026)
extraction_date: 2026-10-23
note_page_numbering: page N = PDF page N. Slide number printed on slide = PDF page minus 1 (page 1 is NSE cover letter).
note_layout: pages 4,5,31,33,34,35,36,37,38,40 are tables/charts where -layout interleaves columns; a RAW-ORDER SUPPLEMENT (pdftotext -raw, same text layer) follows the layout text on those pages. Footnote glyph for Rs symbol is dropped by the PDF font (appears as blank or "()").
=== END HEADER ===
"""
hl=hdr.count('\n')
hdr=hdr.replace('LINECOUNT',str(nb+hl))
open('extracted/supremepwr-presentation-h1fy27-fulltext.md','w',encoding='utf-8').write(hdr+'\n'.join(body)+'\n')
print(nb+hl)
