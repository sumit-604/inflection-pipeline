#!/usr/bin/env python3
"""Convert GitHub-flavored markdown (headings, paragraphs, pipe tables, code
fences) into Notion-flavored Markdown for insert_content. Pipe tables become
<table header-row="true"> blocks; cell text has < > | escaped. Closing fenced
YAML blocks are dropped (pipeline plumbing, not review prose)."""
import re, sys

def esc_cell(s):
    s = s.strip()
    # unescape any pre-existing backslash-pipes from source, then escape angle brackets
    s = s.replace('\\|', '|')
    s = s.replace('<', '\\<').replace('>', '\\>')
    return s

def split_row(line):
    line = line.strip()
    if line.startswith('|'): line = line[1:]
    if line.endswith('|'): line = line[:-1]
    # split on unescaped pipes
    cells = re.split(r'(?<!\\)\|', line)
    return [esc_cell(c) for c in cells]

def is_sep(line):
    return bool(re.match(r'^\s*\|?[\s:—-]*-{2,}[\s:|—-]*\|?\s*$', line)) and '-' in line

def convert(text):
    lines = text.split('\n')
    out = []
    i = 0
    n = len(lines)
    in_code = False
    while i < n:
        line = lines[i]
        # code fence handling: drop yaml plumbing fences, keep others as code
        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            # collect fence body
            j = i + 1
            body = []
            while j < n and not lines[j].strip().startswith('```'):
                body.append(lines[j]); j += 1
            if lang == 'yaml':
                # drop pipeline YAML entirely
                i = j + 1
                continue
            out.append('```' + lang)
            out.extend(body)
            out.append('```')
            i = j + 1
            continue
        # table detection: current line has pipe, next line is separator
        if '|' in line and i + 1 < n and is_sep(lines[i+1]):
            header = split_row(line)
            i += 2
            rows = []
            while i < n and '|' in lines[i] and lines[i].strip():
                if is_sep(lines[i]):
                    i += 1; continue
                rows.append(split_row(lines[i]))
                i += 1
            out.append('<table fit-page-width="true" header-row="true">')
            def emit(cells):
                out.append('<tr>')
                for c in cells:
                    out.append('<td>' + c + '</td>')
                out.append('</tr>')
            emit(header)
            for r in rows:
                # pad/truncate to header width
                while len(r) < len(header): r.append('')
                r = r[:len(header)]
                emit(r)
            out.append('</table>')
            continue
        out.append(line)
        i += 1
    return '\n'.join(out)

if __name__ == '__main__':
    src = sys.argv[1]
    with open(src) as f:
        print(convert(f.read()))
