#!/usr/bin/env python3
"""One-time converter: workshop-guide LaTeX -> Markdown pages for Zensical/MkDocs.

Usage: python3 convert_tex.py source.tex output_docs_dir
Math is emitted as \\( ... \\) (inline) and \\[ ... \\] (display) for MathJax.
"""
import re
import sys
import pathlib

SRC = pathlib.Path(sys.argv[1]).read_text()
OUT = pathlib.Path(sys.argv[2])


# ---------------------------------------------------------------- helpers
def match_brace(s, i):
    """s[i] == '{'. Return (content, index after the closing brace)."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError('unbalanced braces: ' + s[i:i + 60])


def read_arg(s, i):
    while i < len(s) and s[i] in ' \t':
        i += 1
    if i >= len(s) or s[i] != '{':
        raise ValueError('expected { at: ' + s[max(0, i - 20):i + 30])
    return match_brace(s, i)


def skip_empty_group(s, j):
    return j + 2 if s[j:j + 2] == '{}' else j


ARGC = {'cu': 1, 'cb': 1, 'cx': 1, 'up': 1, 'ensuremath': 1, 'sci': 2, 'fr': 2,
        'x': 0, 'dv': 0}
MU_UNITS = {'uCi': 'µCi', 'uSv': 'µSv', 'uL': 'µL'}


def macro_extent(s, i):
    m = re.match(r'\\([A-Za-z]+)', s[i:])
    name = m.group(1)
    j = i + m.end()
    for _ in range(ARGC[name]):
        _, j = read_arg(s, j)
    if ARGC[name] == 0:
        j = skip_empty_group(s, j)
    return name, j


def esc_tex_text(t):
    for a, b in (('%', r'\%'), ('&', r'\&'), ('#', r'\#'), ('_', r'\_')):
        t = t.replace(a, b)
    return t


# ---------------------------------------------------------------- math mode
def conv_math(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c != '\\':
            out.append(c)
            i += 1
            continue
        m = re.match(r'\\([A-Za-z]+)', s[i:])
        if not m:
            out.append(s[i:i + 2])
            i += 2
            continue
        name = m.group(1)
        j = i + m.end()
        if name in ('cu', 'cb', 'cx'):
            arg, j = read_arg(s, j)
            cmd = {'cu': 'cancel', 'cb': 'bcancel', 'cx': 'xcancel'}[name]
            out.append('\\%s{%s}' % (cmd, textmath(arg)))
        elif name == 'sci':
            a, j = read_arg(s, j)
            b, j = read_arg(s, j)
            out.append('%s\\times 10^{%s}' % (conv_math(a), conv_math(b)))
        elif name == 'x':
            j = skip_empty_group(s, j)
            out.append('\\times ')
        elif name == 'dv':
            j = skip_empty_group(s, j)
            out.append('\\div ')
        elif name in MU_UNITS:
            j = skip_empty_group(s, j)
            out.append('\\text{%s}' % MU_UNITS[name])
        elif name == 'up':
            a, j = read_arg(s, j)
            out.append('^{%s}' % conv_math(a))
        elif name == 'ensuremath':
            a, j = read_arg(s, j)
            out.append(conv_math(a))
        elif name == 'fr':
            a, j = read_arg(s, j)
            b, j = read_arg(s, j)
            out.append('\\dfrac{%s}{%s}' % (textmath(a), textmath(b)))
        elif name == 'text':
            a, j = read_arg(s, j)
            out.append(textmath(a))
        else:
            out.append(s[i:j])
        i = j
    return ''.join(out)


def textmath(s):
    """Turn a text-mode fragment (possibly containing math macros) into a math expression."""
    s = s.replace('\\ensuremath{\\mu}', 'µ')
    out, run = [], []

    def flush():
        t = ''.join(run)
        run.clear()
        if t:
            out.append('\\ ' if t.strip() == '' else '\\text{%s}' % esc_tex_text(t))

    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+)', s[i:])
            if m and m.group(1) in ARGC:
                flush()
                name, j = macro_extent(s, i)
                out.append(conv_math(s[i:j]))
                i = j
                continue
            if m and m.group(1) in MU_UNITS:
                run.append(MU_UNITS[m.group(1)])
                i += m.end()
                i = skip_empty_group(s, i)
                continue
            if s[i:i + 2] == '\\ ':
                run.append(' ')
                i += 2
                continue
            run.append(s[i:i + 2])
            i += 2
            continue
        if c == '$':
            j = s.index('$', i + 1)
            flush()
            out.append(conv_math(s[i + 1:j]).strip())
            i = j + 1
            continue
        run.append(c)
        i += 1
    flush()
    return ''.join(out)


# ---------------------------------------------------------------- text mode
def esc_plain(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('*', '\\*').replace('_', '\\_'))


def inline_math(inner):
    return '\\(%s\\)' % conv_math(inner).strip()


DROP = {'boldmath', 'footnotesize', 'itshape', 'large', 'bfseries', 'small',
        'noindent', 'raggedright', 'arraybackslash', 'selectfont', 'centering'}


def conv_text(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '$':
            j = s.index('$', i + 1)
            out.append(inline_math(s[i + 1:j]))
            i = j + 1
        elif c == '\\':
            m = re.match(r'\\([A-Za-z]+)', s[i:])
            if not m:
                nxt = s[i + 1:i + 2]
                if nxt in (';', ',', ' ', '!'):
                    out.append(' ')
                elif nxt in '%$&_#{}':
                    out.append(esc_plain(nxt))
                else:
                    out.append(esc_plain(nxt))
                i += 2
                continue
            name = m.group(1)
            j = i + m.end()
            if name == 'textbf':
                a, j = read_arg(s, j)
                out.append('**%s**' % conv_text(a).strip())
            elif name == 'underline':
                a, j = read_arg(s, j)
                out.append('<u>%s</u>' % conv_text(a))
            elif name == 'fbox':
                a, j = read_arg(s, j)
                out.append('<span class="boxed">%s</span>' % conv_text(a))
            elif name == 'ans':
                a, j = read_arg(s, j)
                out.append('**Answer:** <span class="answer">%s</span>' % conv_text(a))
            elif name == 'why':
                a, j = read_arg(s, j)
                out.append('*Why: %s*' % conv_text(a).strip())
            elif name in ('fr', 'sci', 'cu', 'cb', 'cx'):
                name, j = macro_extent(s, i)
                out.append('\\(%s\\)' % conv_math(s[i:j]))
            elif name == 'x':
                j = skip_empty_group(s, j)
                out.append('×')
            elif name == 'dv':
                j = skip_empty_group(s, j)
                out.append('÷')
            elif name == 'up':
                a, j = read_arg(s, j)
                out.append('<sup>%s</sup>' % conv_text(a))
            elif name in MU_UNITS:
                j = skip_empty_group(s, j)
                out.append(MU_UNITS[name])
            elif name == 'ensuremath':
                a, j = read_arg(s, j)
                a_ = a.strip()
                if a_ == '\\mu':
                    out.append('µ')
                elif a_ == '-':
                    out.append('−')
                elif a_ == '\\surd':
                    out.append('√')
                else:
                    out.append('\\(%s\\)' % conv_math(a))
            elif name == 'textasciicircum':
                j = skip_empty_group(s, j)
                out.append('^')
            elif name == 'texttt':
                a, j = read_arg(s, j)
                out.append(conv_text(a.replace('\\string^', '^')))
            elif name == 'textbackslash':
                j = skip_empty_group(s, j)
                out.append('\\\\')
            elif name == 'ldots':
                j = skip_empty_group(s, j)
                out.append('…')
            elif name in ('quad', 'qquad'):
                out.append('&emsp;')
            elif name == 'color':
                _, j = read_arg(s, j)
            elif name in ('label',):
                _, j = read_arg(s, j)
            elif name in DROP:
                pass
            else:
                raise ValueError('Unhandled text macro \\%s in: %s' % (name, s[:80]))
            i = j
        elif s.startswith('``', i):
            out.append('“')
            i += 2
        elif s.startswith("''", i):
            out.append('”')
            i += 2
        elif c == '[':
            m = re.match(r'\[([^\[\]$]{1,14})\]', s[i:])
            if m and re.fullmatch(r'[A-Za-z0-9\\{}^]+', m.group(1)):
                out.append('<kbd>%s</kbd>' % conv_text(m.group(1)))
                i += m.end()
            else:
                out.append('\\[')
                i += 1
        elif c == '~':
            out.append('&nbsp;')
            i += 1
        elif c in '{}':
            i += 1  # stray grouping braces
        else:
            out.append(esc_plain(c))
            i += 1
    return ''.join(out)


# ---------------------------------------------------------------- paragraphs
def clean_line(s):
    s = re.sub(r'\\vspace\{[^}]*\}', '', s)
    s = re.sub(r'\\nopagebreak\[\d\]', '', s)
    return s


def split_paras(line):
    parts = re.split(r'\\par(?![A-Za-z])', clean_line(line))
    return [p.strip() for p in parts if p.strip()]


def display(math):
    return '\\[\n%s\n\\]' % math


def render_para(p):
    p = p.strip()
    if not p:
        return None
    if p.startswith('{\\footnotesize\\color{mutedgrey}'):
        inner = p[len('{\\footnotesize\\color{mutedgrey}'):].rstrip()
        assert inner.endswith('}')
        return '<small>%s</small>' % conv_text(inner[:-1].strip())
    m = re.fullmatch(r'\$([^$]+)\$', p)
    if m:
        return display(conv_math(m.group(1)).strip())
    if re.match(r'(\d+ HVL: )?\\fr\{', p):
        pm = re.search(r'\.\s+(?=[A-Z][a-z])', p)
        if pm:
            math, rest = p[:pm.start()], p[pm.end():]
            return display(textmath(math)) + '\n\n' + conv_text(rest)
        return display(textmath(p))
    t = conv_text(p)
    return re.sub(r'^(\d+)\.', r'\1\\.', t)


def render_paras(lines):
    res = []
    for ln in lines:
        for p in split_paras(ln):
            r = render_para(p)
            if r:
                res.append(r)
    return res


def indent(md, n=4):
    pad = ' ' * n
    return '\n'.join((pad + l) if l.strip() else '' for l in md.split('\n'))


def admonition(kind, title, paras, collapsible=False):
    head = ('??? ' if collapsible else '!!! ') + '%s "%s"' % (kind, title)
    return head + '\n\n' + indent('\n\n'.join(paras))


# ---------------------------------------------------------------- answers
def parse_keys(text):
    keys = {}
    for ln in text.split('\n'):
        ln = ln.strip()
        if ln.startswith('\\key{'):
            lab, j = read_arg(ln, 4)
            body, j = read_arg(ln, j)
            keys[lab.strip()] = body.strip()
    return keys


def answer_paras(body):
    am = body.find('\\ans{')
    pre, ans = body[:am], None
    if am >= 0:
        ans, j = read_arg(body, am + 4)
        post = body[j:].strip()
    pre = re.sub(r'(\\quad|\s)+$', '', pre.strip())
    paras = []
    if re.search(r'Method 1:', pre):
        pieces = re.split(r'\s*(?=Method \d:)', pre)
        items = ['- ' + conv_text(p.strip()) for p in pieces if p.strip()]
        paras.append('\n'.join(items))
    elif pre:
        # split a trailing explanatory sentence off a math line when needed
        for p in re.split(r',\s*\\quad\s*', pre) if re.fullmatch(r'(\$[^$]+\$,?\s*(\\quad)?\s*)+', pre + ' ') else [pre]:
            r = render_para(p)
            if r:
                paras.append(r)
    if ans is not None:
        paras.append('**Answer:** <span class="answer">%s</span>' % conv_text(ans))
    return paras


# ---------------------------------------------------------------- tables
def convert_table(block_lines):
    text = ' '.join(l.strip() for l in block_lines)
    m = re.search(r'\\begin\{tabularx\}', text)
    _, j = read_arg(text, m.end())      # table width
    spec, j = read_arg(text, j)         # column spec
    body = text[j:text.rindex('\\end{tabularx}')]
    body = re.sub(r'\\(toprule|midrule|bottomrule)', '', body)
    rows = re.split(r'\\\\(?:\[[^\]]*\])?', body)
    rows = [r.strip() for r in rows if r.strip()]
    cells = [[c.strip() for c in re.split(r'(?<!\\)&', r)] for r in rows]
    return cells, spec


def render_table(cells, spec):
    ncol = len(cells[0])
    first_bold = '\\bfseries' in (spec.split('p{')[0] if spec else '')
    lines = []

    def cell(c, bold=False):
        t = conv_text(c).replace('|', '&#124;')
        if bold and t and not t.startswith('**'):
            t = '**%s**' % t
        return t

    head = cells[0]
    lines.append('| ' + ' | '.join(cell(c) for c in head) + ' |')
    lines.append('|' + '|'.join([' --- '] * ncol) + '|')
    for r in cells[1:]:
        r = r + [''] * (ncol - len(r))
        lines.append('| ' + ' | '.join(cell(c, bold=(k == 0 and first_bold)) for k, c in enumerate(r)) + ' |')
    return '\n'.join(lines)


LADDER = """| **G** | ↔ | **M** | ↔ | **k** | ↔ | **(base)** | ↔ | **m** | ↔ | **µ** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| giga | | mega | | kilo | | Ci, Bq, Gy | | milli | | micro |"""


# ---------------------------------------------------------------- main parse
body = SRC[SRC.index('\\begin{document}') + len('\\begin{document}'):SRC.index('\\end{document}')]
lines = body.split('\n')

# answer key lives in the last section
ans_start = next(k for k, l in enumerate(lines) if l.strip().startswith('\\section*{Answers'))
KEYS = parse_keys('\n'.join(lines[ans_start:]))
lines = lines[:ans_start]

pages = []          # dicts: label, title, blocks
cur = {'label': 'preface', 'title': '', 'blocks': []}
pages.append(cur)
used_keys = set()

i, n = 0, len(lines)
while i < n:
    s = lines[i].strip()
    i += 1
    if not s or s.startswith('%'):
        continue
    if s == '\\clearpage' or s.startswith('\\vspace') or s.startswith('\\needspace'):
        continue
    if s.startswith('{\\renewcommand{\\arraystretch}'):
        continue
    if s.startswith('{\\fontsize') or s.startswith('{\\large'):
        continue

    m = re.match(r'\\section\*\{(.*)\}\\label\{(\w+)\}$', s)
    if m:
        cur = {'label': m.group(2), 'title': conv_text(m.group(1)), 'blocks': []}
        pages.append(cur)
        continue

    m = re.match(r'\\subsection\*\{(.*)\}$', s)
    if m:
        cur['blocks'].append('## ' + conv_text(m.group(1)))
        if m.group(1).strip() == 'Try these':
            cur['blocks'].append('*Work each problem on paper with the setup-line method, '
                                 'then click **Show answer** to check your work.*')
        continue

    if s.startswith('\\begin{callout}'):
        buf = []
        while not lines[i].strip().startswith('\\end{callout}'):
            buf.append(lines[i])
            i += 1
        i += 1
        paras = render_paras(buf)
        title_m = re.fullmatch(r'\*\*(.*)\*\*', paras[0])
        title = title_m.group(1) if title_m else 'Note'
        rest = paras[1:] if title_m else paras
        kind = 'info'
        if title.startswith('Memorize'):
            kind = 'warning'
        elif title.startswith(('Three calculator', 'Order of')):
            kind = 'tip'
        cur['blocks'].append(admonition(kind, title, rest))
        continue

    if s.startswith('\\begin{ex}'):
        j = len('\\begin{ex}')
        label, j = read_arg(s, j)
        question, j = read_arg(s, j)
        buf = []
        while not lines[i].strip().startswith('\\end{ex}'):
            buf.append(lines[i])
            i += 1
        i += 1
        qpara = '**%s**' % conv_text(question).strip()
        if any('\\workspace' in b for b in buf):
            body_md = [qpara]
            ans = answer_paras(KEYS[label.strip()])
            used_keys.add(label.strip())
            body_md.append(admonition('success', 'Show answer', ans, collapsible=True))
            cur['blocks'].append(admonition('question', label, body_md))
        else:
            paras = render_paras(buf)
            cur['blocks'].append(admonition('example', label, [qpara] + paras))
        continue

    if s.startswith('\\begin{itemize}') or s.startswith('\\begin{enumerate}'):
        ordered = 'enumerate' in s
        items = []
        while not lines[i].strip().startswith('\\end{'):
            l = lines[i].strip()
            if l.startswith('\\item'):
                items.append(l[len('\\item'):].strip())
            i += 1
        i += 1
        out = []
        for k, it in enumerate(items, 1):
            out.append(('%d. ' % k if ordered else '- ') + conv_text(it))
        cur['blocks'].append('\n'.join(out))
        continue

    if s == '\\[':
        buf = []
        while lines[i].strip() != '\\]':
            buf.append(lines[i].strip())
            i += 1
        i += 1
        cur['blocks'].append(display(conv_math(' '.join(buf)).strip()))
        continue

    if s.startswith('\\begin{align*}'):
        buf = []
        while not lines[i].strip().startswith('\\end{align*}'):
            buf.append(lines[i].strip())
            i += 1
        i += 1
        inner = '\n'.join(buf)
        cur['blocks'].append(display('\\begin{aligned}\n%s\n\\end{aligned}' % conv_math(inner)))
        continue

    if s.startswith('\\begin{center}'):
        while not lines[i].strip().startswith('\\end{center}'):
            i += 1
        i += 1
        cur['blocks'].append(LADDER)
        continue

    if s.startswith('\\begin{tabularx}'):
        buf = [s]
        while '\\end{tabularx}' not in lines[i]:
            buf.append(lines[i])
            i += 1
        buf.append(lines[i])
        i += 1
        if cur['label'] == 'preface':
            continue
        cells, spec = convert_table(buf)
        cur['blocks'].append(render_table(cells, spec))
        continue

    # plain paragraph line(s)
    for p in split_paras(s):
        r = render_para(p)
        if r:
            cur['blocks'].append(r)

# ---------------------------------------------------------------- write
FILES = {
    'start': ('start-here', 'Start Here: The Setup-Line Method'),
    'constants': ('constants', None),
    'calc': ('calculator-check', None),
    'words': ('reading-word-problems', None),
    'top1': ('topic-01-dimensional-analysis', None),
    'top2': ('topic-02-scientific-notation', None),
    'top3': ('topic-03-metric-prefixes', None),
    'top4': ('topic-04-activity-units', None),
    'top5': ('topic-05-dose-units', None),
    'top6': ('topic-06-concentration-volume', None),
    'top7': ('topic-07-weight-bmi', None),
    'top8': ('topic-08-dose-rate-time', None),
    'top9': ('topic-09-inverse-square-law', None),
    'top10': ('topic-10-shielding', None),
    'top11': ('topic-11-radioactive-decay', None),
    'final': ('final-checks', None),
}
OUT.mkdir(parents=True, exist_ok=True)
index = []
for pg in pages:
    if pg['label'] == 'preface':
        pre = '\n\n'.join(pg['blocks'])
        (OUT / '_preface_callout.md').write_text(pre + '\n')
        continue
    fname, _ = FILES[pg['label']]
    md = '# %s\n\n' % pg['title'] + '\n\n'.join(pg['blocks']) + '\n'
    (OUT / (fname + '.md')).write_text(md)
    index.append((fname, pg['title']))

missing = set(KEYS) - used_keys
assert not missing, 'answers not attached: %s' % missing
print('pages:', len(index), ' answers attached:', len(used_keys))
for f, t in index:
    print(' ', f, '|', t)
