"""
Stamps the CSS and JS links with a content hash.

GitHub Pages serves assets with a ten-minute cache lifetime, so after a deploy
returning visitors keep the previous stylesheet and the page renders with a
layout that no longer matches the markup. Appending a hash of the file contents
changes the URL whenever the file changes, which makes every deploy take effect
immediately and lets unchanged files stay cached.

Run after editing anything in assets/, before committing.
"""

import glob
import hashlib
import io
import os
import re

SITE = os.path.dirname(os.path.abspath(__file__))
TRACKED = ("assets/tl.css", "assets/tl.js")

stamps = {}
for rel in TRACKED:
    p = os.path.join(SITE, rel.replace("/", os.sep))
    stamps[rel] = hashlib.sha1(open(p, "rb").read()).hexdigest()[:8]
    print(f"  {rel:<16} {stamps[rel]}")

changed = 0
for page in glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True):
    s = io.open(page, encoding="utf-8").read()
    original = s
    for rel, h in stamps.items():
        name = rel.split("/")[-1]
        # matches href="assets/tl.css", href="../assets/tl.css", with or without
        # an existing ?v= stamp
        s = re.sub(r'((?:\.\./)?assets/' + re.escape(name) + r')(\?v=[0-9a-f]+)?"',
                   rf'\1?v={h}"', s)
    if s != original:
        io.open(page, "w", encoding="utf-8", newline="").write(s)
        changed += 1
        print(f"  stamped {os.path.relpath(page, SITE)}")

print(f"\n{changed} page(s) updated")

for page in sorted(glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True)):
    for m in re.finditer(r'(?:href|src)="((?:\.\./)?assets/tl\.(?:css|js)[^"]*)"',
                         io.open(page, encoding="utf-8").read()):
        print(f"  {os.path.relpath(page, SITE):<40} {m.group(1)}")
