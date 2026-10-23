import re, sys
FT = '../extracted/supremepwr-results-h1fy27-fulltext.md'
L = open(FT, encoding='utf-8').read().split('\n')   # L[i-1] is line i
pagestart = {}
for i, l in enumerate(L, 1):
    m = re.match(r'^\[page (\d+)\]$', l)
    if m:
        pagestart[int(m.group(1))] = i
pagestart[16] = len(L) + 1
def prange(p):
    return pagestart[p], pagestart[p + 1] - 1
def find(p, pat, last=True, after=None):
    a, b = prange(p)
    hits = [i for i in range(a, b + 1) if re.search(pat, L[i - 1])]
    if after:
        hits = [h for h in hits if h > after]
    if not hits:
        raise SystemExit('NOT FOUND p%d %s' % (p, pat))
    return hits[-1] if last else hits[0]

num = []; ent = []; fwd = []; dat = []; qual = []

TOK = re.compile(r'(\(?-?[\d,]+\.\d+\)?|\(?-?\d[\d,]*\)?(?=\s|$)|(?<=\s)-(?=\s|$))')
def tabrows(page, cols, ctxprefix):
    a, b = prange(page)
    # block starts after the OCR marker
    st = [i for i in range(a, b + 1) if L[i - 1].startswith('[OCR page')][0] + 1
    i = st
    section = ''
    pending = None
    while i <= b:
        line = L[i - 1]
        if line.startswith('Columns:') or not line.strip() or line.startswith('Particulars') or line.startswith('STANDALONE STATEMENT') or line.startswith('CONSOLIDATED STATEMENT') or line.startswith('(Paid up') or line.startswith('Figures of') or line.startswith('Place:') or line.startswith('Notes:') or line.startswith('(ii)'):
            i += 1; continue
        # strip trailing values
        toks = []
        rest = line.rstrip()
        while True:
            m = re.search(r'\s+(\(?-?[\d,]+\.\d+\)?|\(?-?\d[\d,]*\)?|-)$', rest)
            if m and len(toks) < len(cols):
                toks.insert(0, m.group(1)); rest = rest[:m.start()]
            else:
                break
        label = rest.strip()
        if label.startswith('(no value'):
            label = label
        if len(toks) == len(cols):
            lab = pending if (label == '' and pending) else label
            pending = None
            for c, t in zip(cols, toks):
                num.append((page, i, t, '%s, %s %s' % (lab.strip(), c, ctxprefix), t == '-'))
        elif len(toks) == 0:
            pending = label
        else:
            # partial values: label with fewer tokens, pad skip
            for c, t in zip(cols[-len(toks):], toks):
                num.append((page, i, t, '%s, %s %s' % (label, c, ctxprefix), t == '-'))
        i += 1

SA = ['H1 FY27 (HY ended 30-Sep-2026)', 'H2 FY26 (HY ended 31-Mar-2026)', 'H1 FY26 (HY ended 30-Sep-2025)', 'FY26 (year ended 31-Mar-2026)']
BS = ['as at 30-Sep-2026', 'as at 31-Mar-2026']
CF = ['H1 FY27 (HY ended 30-Sep-2026)', 'FY26 (year ended 31-Mar-2026)']
tabrows(4, SA, 'standalone P&L')
tabrows(5, BS, 'standalone balance sheet')
tabrows(7, CF, 'standalone cash flow')
tabrows(10, SA, 'consolidated P&L')
tabrows(11, BS, 'consolidated balance sheet')
tabrows(13, CF, 'consolidated cash flow')
