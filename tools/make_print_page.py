#!/usr/bin/env python3
"""Builds docs/print-full-guide.md: every guide page joined into one long page,
so students can print the whole guide to a single PDF.

The page order comes from the `nav:` list in mkdocs.yml, so you never have to
edit this file when you add or reorder pages. The GitHub workflow runs this
script automatically before every build.
"""
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
docs = root / "docs"
out = docs / "print-full-guide.md"

pages = []
for line in (root / "mkdocs.yml").read_text().splitlines():
    m = re.match(r'\s+-\s+.*?:\s*([\w\-/]+\.md)\s*$', line)
    if m and m.group(1) not in ("index.md", "print-full-guide.md"):
        pages.append(m.group(1))

header = """# Print the Full Guide

<div class="no-print" markdown>

!!! tip "How to save the whole guide as a PDF"

    1. Click **Print / Save as PDF** (top right), or press **Ctrl+P** (Windows) or **Cmd+P** (Mac).
    2. Choose **Save as PDF** as the destination.
    3. Turn on **Background graphics** so the colored boxes print.

    All answers open automatically in the printout. Scroll down to see the full guide.

</div>
"""

parts = [header]
for name in pages:
    text = (docs / name).read_text().strip()
    parts.append(text)

out.write_text("\n\n".join(parts) + "\n")
print("Wrote", out.relative_to(root), "from", len(pages), "pages")
