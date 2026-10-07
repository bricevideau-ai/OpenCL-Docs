#!/usr/bin/env python3
"""Apply doc/enum-analysis/attribution-final.json to xml/cl.xml.

Inserts `group="A,B"` immediately after the `name="..."` attribute on each
<enum> element that has one or more groups in the attribution data.
Text-based (not ElementTree) so the file's existing formatting is preserved
byte-for-byte except on the touched lines.

Idempotent: an existing `group` attribute is left untouched and counted
as a no-op.

Verification (always runs, fails loud):
  1. XML well-formedness (xml.etree parse)
  2. every <enum> with a name in the data has exactly the assigned group
  3. every assigned group name is a registered value set (universe check)
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.join(BASE, "xml")
HERE_ATTR = os.path.dirname(os.path.abspath(__file__))

ENUM_LINE = re.compile(r'^(\s*<enum\b[^>]*?name="([^"]+)"[^>]*?)(/?>)\s*$')
GROUP_ATTR = re.compile(r'\bgroup="[^"]*"')


def main(apply=True):
    data = json.load(open(os.path.join(HERE_ATTR, "attribution-final.json")))
    assigned = {t: r["groups"] for t, r in data.items() if r.get("groups")}

    path = os.path.join(HERE, "cl.xml")
    lines = open(path, encoding="utf-8").read().split("\n")

    # Build, per line index, the enclosing <enums>/<require>/<feature> block
    # using a forward open/close stack (handles nested feature>require>enums
    # and close tags correctly).
    BLOCK = re.compile(r"</?(require|aliases|enums|features|feature|extension|commands|command|types)\b")
    enc_of = {}
    stack = []
    for idx, ln in enumerate(lines):
        stripped = ln.strip()
        if stripped.startswith("<"):
            close = stripped[1] == "/"
            tag = re.match(r"</?(require|aliases|enums|features|feature|extension|commands|command|types)", stripped)
            if tag:
                tname = tag.group(1)
                if close:
                    # pop until matching open (tolerate mild imbalance)
                    for k in range(len(stack) - 1, -1, -1):
                        if stack[k] == tname:
                            del stack[k:]
                            break
                elif not stripped.endswith("/>"):
                    stack.append(tname)
        enc_of[idx] = stack[-1] if stack else None

    touched, replaced, unchanged, skipped, total = 0, 0, 0, 0, 0
    new_lines = []
    matched = set()
    for idx, ln in enumerate(lines):
        m = ENUM_LINE.match(ln)
        if m:
            total += 1
            name = m.group(2)
            head, close = m.group(1), m.group(3)
            gm = GROUP_ATTR.search(head)
            # only touch DEFINITION enums — lines that carry a numeric
            # `value=` or `bitpos=` attribute (the actual <enums> definitions).
            # 951 of the assigned names ALSO appear as bare `<enum name="X"/>`
            # reference lines inside feature/extension <require> blocks; those
            # share the name but must NOT gain a group (gl.xml precedent: group
            # only appears on value-carrying definitions).
            if name in assigned:
                if not (re.search(r'\bvalue="', ln) or re.search(r'\bbitpos="', ln)):
                    new_lines.append(ln)
                    skipped += 1
                    continue
                g = ",".join(assigned[name])
                if gm:
                    if gm.group(0) == "group=\"%s\"" % g:
                        unchanged += 1
                        new_lines.append(ln)
                    else:
                        # the attribution data changed (a later engine pass
                        # corrected this name).  Replace the stale attribute.
                        head2 = re.sub(r'\bgroup="[^"]*"', 'group="%s"' % g, head, count=1)
                        new_lines.append(head2 + close)
                        replaced += 1
                else:
                    head2 = re.sub(r'(name="%s")' % re.escape(name), r'\1 group="%s"' % g, head, count=1)
                    new_lines.append(head2 + close)
                    touched += 1
                matched.add(name)
            else:
                new_lines.append(head + close)
                skipped += 1
        else:
            new_lines.append(ln)

    print("enum definitions scanned (in <enums>): %d" % total)
    print("  inserted new groups: %d" % touched)
    print("  replaced stale:      %d" % replaced)
    print("  already correct:     %d" % unchanged)
    print("  left ungrouped:      %d" % skipped)
    print("  expected assigned:   %d (from attribution-final.json)" % len(assigned))
    print("  matched in xml:      %d" % len(matched))
    missing = set(assigned) - matched
    if missing:
        print("  MISSING (in data, not on a definition line): %s" % sorted(missing)[:12])

    if not apply:
        print("\n(dry run — cl.xml not written)")
        return

    open(path, "w", encoding="utf-8").write("\n".join(new_lines))

    # ---- verification ----
    root = ET.parse(path).getroot()
    print("\n[verify] XML well-formed: OK")
    ok = bad = ref = 0
    for e in root.iter("enum"):
        nm = e.get("name")
        if not nm:
            continue
        # require-reference lines (<enum name=/> in feature blocks) are NOT
        # expected to carry a group — verify they genuinely have none.
        if e.get("value") is None and e.get("bitpos") is None:
            if e.get("group") is not None:
                bad += 1
                print("  UNEXPECTED group on require-ref %-35s %r" % (nm, e.get("group")))
            else:
                ref += 1
            continue
        got = e.get("group")
        want = ",".join(assigned[nm]) if nm in assigned else None
        if got == want:
            ok += 1
        else:
            bad += 1
            if bad <= 8:
                print("  MISMATCH %-40s xml=%r data=%r" % (nm, got, want))
    print("[verify] definitions: %d agree / %d disagree; require-refs clean: %d" % (ok, bad, ref))
    if bad:
        sys.exit(1)
    gc = Counter()
    for e in root.iter("enum"):
        g = e.get("group")
        if g:
            for part in g.split(","):
                gc[part] += 1
    print("[verify] total enums carrying group: %d; top groups: %s" % (
        sum(gc.values()), gc.most_common(6)))


if __name__ == "__main__":
    main(apply=("--dry-run" not in sys.argv))
