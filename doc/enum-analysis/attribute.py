#!/usr/bin/env python3
"""Attribute every OpenCL enum token to spec contexts (function + parameter
type) by analyzing the .asciidoc spec sources.

Emit attribution.json: token -> [
  {"file", "section", "label", "functions", "param_type"}
]
where:
  - functions: cl* names mentioned in the section heading / table label
  - param_type: the C type name from the table's value column
    (e.g. cl_mem_flags from `{cl_mem_flags_TYPE}`) if detectable

This is ground truth for which 'group' (parameter type) each token belongs to.
"""

import json
import os
import re
from collections import defaultdict

BASE = "/home/videau-ai/OpenCL-Docs"
SPECS = [
    "api/opencl_runtime_layer.asciidoc",
    "api/opencl_platform_layer.asciidoc",
]
EXT = []
for f in sorted(os.listdir(os.path.join(BASE, "api"))):
    if re.match(r"cl_(khr|ext)_[a-z0-9_]+\.asciidoc$", f):
        EXT.append("api/" + f)

FUNC_RE = re.compile(r"\b(cl[A-Z][A-Za-z0-9_]+)\b")
TOKEN_RE = re.compile(r"\b(CL_[A-Z0-9_]+)\b")
TYPE_RE = re.compile(r"\{(cl_[a-z0-9_]+)_TYPE\}")
LABEL_RE = re.compile(r"^[.]\s*(.+)$")
# 'list of ... values ...' labels
LISTY_RE = re.compile(r"list of .*(values|properties|modes|types|flags)", re.I)


def analyze(rel):
    path = os.path.join(BASE, rel)
    lines = open(path, encoding="utf-8").read().split("\n")

    # Track heading stack, tables, labels, parameter types in scope
    entries = defaultdict(list)  # token -> list of contexts
    heading_stack = {}
    in_table = False
    table_lines = []            # lines of current table
    table_label = None
    pending_label = None

    def flush_table():
        nonlocal table_lines, table_label, in_table
        if not in_table:
            return
        blob = "\n".join(table_lines)
        tokens = sorted(set(TOKEN_RE.findall(blob)))
        types = sorted(set(TYPE_RE.findall(blob)))
        funcs = sorted(set(FUNC_RE.findall(table_label + " " + " ".join(heading_stack.values()))))
        # The list-table convention: the label says what kind of values
        for tok in tokens:
            entries[tok].append({
                "file": rel,
                "label": table_label,
                "heading": list(heading_stack.values()),
                "functions": funcs,
                "value_types": types,
            })
        table_lines, table_label, in_table = [], None, False

    for line in lines:
        h = re.match(r"^(==+)\s+(.*)", line)
        if h:
            level = len(h.group(1))
            heading_stack[level] = h.group(2).strip()
            for lev in [k for k in heading_stack if k > level]:
                del heading_stack[lev]
            flush_table()
            continue
        if re.match(r"^[.][^\s=]", line):
            pending_label = line[1:].strip()
            continue
        if line.strip() == "|====":
            flush_table()
            in_table = True
            table_label = pending_label
            continue
        if re.match(r"^====\|?$", line.strip()) and in_table:
            flush_table()
            continue
        if in_table:
            table_lines.append(line)
    flush_table()
    return entries


def main():
    # token -> set of context keys -> first context
    all_entries = defaultdict(dict)
    for rel in SPECS + EXT:
        data = analyze(rel)
        for tok, ctxs in data.items():
            for c in ctxs:
                key = (c["label"], tuple(c["value_types"]), tuple(sorted(c["functions"])))
                if key not in all_entries[tok]:
                    all_entries[tok][key] = c

    out = {}
    for tok, ctxmap in all_entries.items():
        merged = []
        for c in ctxmap.values():
            merged.append({
                "label": c["label"],
                "value_types": c["value_types"],
                "functions": sorted(c["functions"]),
                "heading": c["heading"],
            })
        merged.sort(key=lambda m: (m["label"] or "", tuple(m["value_types"])))
        out[tok] = merged

    dest = os.path.join(BASE, "doc/enum-analysis/attribution.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1)

    print("tokens with spec contexts:", len(out))
    multi = {t: v for t, v in out.items() if len({tuple(m["value_types"]) for m in v}) > 1}
    print("tokens with >1 distinct value-type context:", len(multi))
    for t in list(multi)[:30]:
        ts = set()
        for m in out[t]:
            for x in m["value_types"]:
                ts.add(x)
        print("  ", t, sorted(ts))


if __name__ == "__main__":
    main()
