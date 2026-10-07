#!/usr/bin/env python3
"""Manual-check discovery: for every unassigned cl.xml token, dump the spec
context in which it appears so a human (or its agent) can decide the group.

Output: spec-check.md — one block per token with raw spec lines.
"""
import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))

data = json.load(open(os.path.join(HERE, "attribution-final.json")))
un = sorted(t for t, r in data.items() if not r["groups"])

specs = []
for sub in ("api", "env", "extensions"):
    d = os.path.join(BASE, sub)
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.endswith(".asciidoc") and "template" not in f:
                specs.append(os.path.join(d, f))

out = []
for tok in un:
    hits = []
    for f in specs:
        lines = open(f, encoding="utf-8").read().split("\n")
        n = len(lines)
        for i, l in enumerate(lines):
            if not re.search(r"\b" + tok + r"(?:_anchor)?\b", l):
                continue
            # context window
            a = max(0, i - 3)
            b = min(n, i + 4)
            ctx = []
            for j in range(a, b):
                s = lines[j].strip()
                s = re.sub(r"include::\{generated\}.*", "[version-note]", s)
                ctx.append((">> " if j == i else "   ") + s[:150])
            hits.append((f.replace(BASE + "/", ""), ctx))
    out.append((tok, data[tok]["container"], data[tok]["value"], hits))

# order: by container then name
out.sort(key=lambda x: (x[1] or "", x[0]))
lines = ["# SPEC DISCOVERY — unassigned cl.xml tokens (manual check)", ""]
lines.append("%d tokens.  Mark each as: assign `group=...` / confirm ungrouped." % len(out))
lines.append("")
for tok, cont, val, hits in out:
    lines.append("## `%s`  (container: `%s`, value: %s)" % (tok, cont, val))
    if not hits:
        lines.append("- NO SPEC MENTIONS in api/, env/, extensions/")
    for f, ctx in hits[:6]:
        lines.append("- `%s`:" % f)
        lines.extend("  " + c for c in ctx)
    lines.append("")
open(os.path.join(HERE, "spec-check.md"), "w").write("\n".join(lines))
print("wrote spec-check.md with", len(out), "tokens")
nohits = [t for t, _, _, h in out if not h]
print("tokens with zero spec hits:", len(nohits))
for t in nohits:
    print("   ", t)
