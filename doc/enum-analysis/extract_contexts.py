#!/usr/bin/env python3
"""Mine the OpenCL spec sources for enum-token usage contexts.

Produces enum-contexts.json: for every CL_ token, every distinct spec
context (file, heading chain, table label) where it is listed as a valid
value. This is the review substrate for adding group= attributions.
"""

import json
import os
import re
from collections import defaultdict

BASE = "/home/videau-ai/OpenCL-Docs"
SPEC_SOURCES = [
    "api/opencl_runtime_layer.asciidoc",
    "api/opencl_platform_layer.asciidoc",
]
EXT_SOURCES = []
for f in sorted(os.listdir(os.path.join(BASE, "api"))):
    if re.match(r"cl_(khr|ext)_[a-z0-9_]+\.asciidoc$", f):
        EXT_SOURCES.append("api/" + f)

TOKEN_RE = re.compile(r"\b(CL_[A-Z0-9_]+)\b")
FUNC_RE = re.compile(r"\b(cl[A-Z][A-Za-z0-9_]+)\b")


def tokenize_file(path):
    """Return occurrences: {token, line, heading, table_label, file}."""
    lines = open(path, encoding="utf-8").read().split("\n")
    heading_stack = {}
    table_label = None
    in_table = False
    pending_label = None
    rel = os.path.relpath(path, BASE)
    out = []
    for idx, line in enumerate(lines):
        h = re.match(r"^(==+)\s+(.*)", line)
        if h:
            level = len(h.group(1))
            heading_stack[level] = h.group(2).strip()
            for lev in [k for k in heading_stack if k > level]:
                del heading_stack[lev]
        stripped = line.strip()
        if re.match(r"^\.[^\s=]", line):
            pending_label = line[1:].strip()
        if stripped == "|====":
            in_table = True
            table_label = pending_label
        elif re.match(r"^====\|?$", stripped) and in_table:
            in_table = False
            table_label = None
        for tok in TOKEN_RE.findall(line):
            heading = " > ".join(heading_stack[k] for k in sorted(heading_stack))
            out.append({
                "file": rel,
                "line": idx + 1,
                "token": tok,
                "heading": heading,
                "table_label": table_label,
            })
    return out


def main():
    per_token = defaultdict(list)
    for rel in SPEC_SOURCES + EXT_SOURCES:
        for occ in tokenize_file(os.path.join(BASE, rel)):
            per_token[occ["token"]].append(occ)

    summary = {}
    for tok, occs in per_token.items():
        seen, distinct = set(), []
        for o in occs:
            key = (o["file"], o["heading"], o["table_label"])
            if key in seen:
                continue
            seen.add(key)
            blob = "{} {}".format(o["heading"], o["table_label"] or "")
            o = dict(o)
            o["functions_in_context"] = sorted(set(FUNC_RE.findall(blob)))
            distinct.append(o)
        fset = set()
        for d in distinct:
            fset.update(d["functions_in_context"])
        summary[tok] = {
            "occurrences": len(occs),
            "distinct_contexts": distinct,
            "functions": sorted(fset),
        }

    dest = os.path.join(BASE, "doc/enum-analysis/enum-contexts.json")
    with open(dest, "w") as fh:
        json.dump(summary, fh, indent=1)
    multi = [t for t, v in summary.items() if len(v["functions"]) > 1]
    nofunc = [t for t, v in summary.items() if not v["functions"]]
    print("wrote", dest)
    print("total tokens:", len(summary))
    print("tokens with >1 function in their spec contexts:", len(multi))
    for t in multi[:30]:
        print("  ", t, "->", summary[t]["functions"])
    print("tokens with NO function in context:", len(nofunc))


if __name__ == "__main__":
    main()
