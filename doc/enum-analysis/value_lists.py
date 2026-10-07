#!/usr/bin/env python3
"""Row-level spec attribution for OpenCL enum tokens.

Walks the .asciidoc spec sources and collects, for each CL_* token,
the contexts in which the spec lists it as a valid value:
  - tables: row whose first data cell is {TOKEN}; the row's other cells
    give the associated C type (via {type_TYPE} macros) and the table
    label names the parameter kind.
  - inline lists: bullet/indent lists following 'can be one of the
    following values' / 'combination of the following values'.

For each context we capture:
  - function: the enclosing refpage (cl* name) if any
  - section: nearest heading chain
  - label: table label text
  - types: C types found in the same row/section
  - kind: 'table' | 'inline'

These contexts are the *evidence* for the group attribution:
a token's group is the set of named value-sets (C types) whose valid
lists contain it, verified against the spec sources.
"""

import json
import os
import re
from collections import defaultdict

BASE = "/home/videau-ai/OpenCL-Docs"
CORE_DEPS = [os.path.join(BASE, "out/core/spec/api/opencl_runtime_layer.asciidoc")]
SOURCES = [
    "api/opencl_runtime_layer.asciidoc",
    "api/opencl_platform_layer.asciidoc",
]
EXT = []
for f in sorted(os.listdir(os.path.join(BASE, "api"))):
    if re.match(r"cl_(khr|ext)_[a-z0-9_]+\.asciidoc$", f):
        EXT.append("api/" + f)

TOKEN_RE = re.compile(r"\{?CL_[A-Z0-9_]+\}?")
TOKEN_NAME_RE = re.compile(r"CL_[A-Z0-9]+")
TYPE_MACRO_RE = re.compile(r"\{(cl_[a-z0-9_]+)_TYPE\}")
REFPAGE_RE = re.compile(r"\[open,refpage='(cl[A-Za-z0-9]+)'")
HEADING_RE = re.compile(r"^(={1,6})\s+(.*)")
LABEL_RE = re.compile(r"^\.(?!\d)\S.*$")
INLINE_LIST_RE = re.compile(r"(one of the following values|combination of the following values|supported values|list of)")


def load_registry_enum_names():
    import xml.etree.ElementTree as ET
    tree = ET.parse(os.path.join(BASE, "xml/cl.xml"))
    names = set()
    for e in tree.getroot().iter("enum"):
        if e.get("name"):
            names.add(e.get("name"))
    return names


REG_ENUMS = None


def parse_file(path):
    global REG_ENUMS
    if REG_ENUMS is None:
        REG_ENUMS = load_registry_enum_names()
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    rel = os.path.relpath(path, BASE)

    entries = defaultdict(list)  # token -> list of context dicts

    heading_stack = {}
    refpage = None
    refpage_depth = 0  # how deep inside the refpage block
    cur_label = None
    in_table = False
    table_rows = []
    table_label_at_start = None

    def record_table(rows):
        label = table_label_at_start or cur_label
        if not rows:
            return
        # type names in the label, e.g. `cl_command_queue_property` or {cl_uint_TYPE}
        label_types = set(re.findall(r"`(cl_[a-z0-9_]+)`", label or ""))
        label_types |= set(TYPE_MACRO_RE.findall(label or ""))
        for row in rows:
            cells = row
            if not cells:
                continue
            first = cells[0].strip()
            rowtext = " | ".join(cells)
            # A row contributes tokens in two ways:
            #  (a) the row's first cell is itself a token  -> row token
            #  (b) the row's description cell lists bitfield-member tokens
            #      ("can be set to a combination of the following values")
            #      -> member tokens
            # In both cases the row's value-set is the C type shown in its
            # type cell ({type_TYPE}) or in the table label.
            m = re.match(r"^\{?(CL_[A-Z0-9_]+?)(_anchor)?\}?$", first)
            row_token = m.group(1) if m else None
            rowtypes = set(TYPE_MACRO_RE.findall(rowtext)) | label_types
            desc_tokens = set()
            if rowtypes:
                # Only harvest member tokens from description cells that
                # explicitly enumerate valid values; otherwise cells merely
                # cross-referencing sibling params would produce spurious
                # attribution.
                for c in cells[1:]:
                    if re.search(r"combination of|one of the following|following values|bit.?field|bit field|bit.?mask|bit mask|property value|list of supported|List of supported", c, re.I):
                        for name in re.findall(r"\b(CL_[A-Z0-9_]+)\b", c):
                            if name in REG_ENUMS and name not in ("CL_TRUE", "CL_FALSE"):
                                desc_tokens.add(name)
            targets = set()
            if row_token:
                targets.add(row_token)
            targets |= desc_tokens
            for tok in sorted(targets):
                entries[tok].append({
                    "file": rel,
                    "kind": "table",
                    "label": label,
                    "row": rowtext[:200],
                    "types": sorted(rowtypes),
                    "functions": [refpage] if refpage else [],
                    "heading": list(heading_stack.values()),
                })

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        h = HEADING_RE.match(line)
        if h:
            level = len(h.group(1))
            heading_stack[level] = h.group(2).strip()
            for lev in [k for k in heading_stack if k > level]:
                del heading_stack[lev]
            in_table = False
            i += 1
            continue

        rm = REFPAGE_RE.search(line)
        if rm and "refpage=" in line and not in_table:
            # refpages open with [open,refpage='x'...] and close with another
            # [open, ...] or a section end; in these specs refpages are
            # delimited by -- ... -- blocks. Track via the block.
            refpage = rm.group(1)
            i += 1
            continue
        # A new refpage block starts; if we see any '[open,' without refpage,
        # that ends the previous refpage's value-list context but keep heading.
        if stripped.startswith("[open,"):
            refpage = None
            i += 1
            continue

        if LABEL_RE.match(line) and not in_table:
            cur_label = line[1:].strip()
            i += 1
            continue

        if stripped == "|====" and not in_table:
            in_table = True
            table_label_at_start = cur_label
            rows = []
            i += 1
            row = None
            # AsciiDoc grid table:
            #   - a '|' at column 0 starts a NEW ROW (cell 1)
            #   - an indented '| ...' is the NEXT CELL of the current row
            #   - any other line (blank, include, text) is a continuation of
            #     the current cell
            # The closing delimiter is a line of only '=' and a single '|'.
            while i < n:
                raw = lines[i]
                t = raw.strip()
                if set(t) <= {"=", "|"} and len(t) >= 5:
                    i += 1  # consume the closing delimiter
                    break
                if raw.startswith("|"):
                    if row is not None:
                        rows.append(row)
                    row = [c.strip() for c in raw[1:].split("|")]
                elif re.match(r"^\s+\|", raw) and row is not None:
                    cell = raw.lstrip()[1:].strip()
                    if cell or row[-1] != "":
                        row.append(cell)
                elif row is not None:
                    row[-1] = (row[-1] + " " + t).strip()
                i += 1
            if row is not None:
                rows.append(row)
            record_table(rows)
            in_table = False
            table_label_at_start = None
            cur_label = None
            continue

        # inline lists: line contains INLINE_LIST_RE marker; the following
        # bullet/indent lines with CL_* tokens belong to this list
        if INLINE_LIST_RE.search(line):
            list_types = TYPE_MACRO_RE.findall(line)
            # scan following lines for {CL_X} entries
            j = i + 1
            collected = []
            while j < n:
                t = lines[j].strip()
                if not t or t.startswith("--") or HEADING_RE.match(lines[j]) \
                        or t.startswith("[") or t.startswith("ifdef") \
                        or t.startswith("endif") or t.startswith("include"):
                    if t and not t.startswith("include") and not t.startswith("ifdef") \
                            and not t.startswith("endif") and t:
                        break
                    j += 1
                    continue
                toks = re.findall(r"\bCL_[A-Z0-9_]+\b", t)
                if toks:
                    collected.extend(toks)
                    j += 1
                elif t.startswith("- ") or t.startswith("* "):
                    j += 1
                else:
                    break
            if collected:
                for tok in sorted(set(collected)):
                    ctx = {
                        "file": rel,
                        "kind": "inline",
                        "label": None,
                        "row": line[:200],
                        "types": list_types,
                        "functions": [refpage] if refpage else [],
                        "heading": list(heading_stack.values()),
                    }
                    entries[tok].append(ctx)
            i = j
            continue

        i += 1
    return entries


def next_line_empty(idx):
    return False


def main():
    all_entries = defaultdict(dict)
    for rel in SOURCES + EXT:
        data = parse_file(os.path.join(BASE, rel))
        for tok, ctxs in data.items():
            for c in ctxs:
                key = (c["label"], c["kind"], tuple(c["types"]), tuple(c["functions"]))
                if key not in all_entries[tok]:
                    all_entries[tok][key] = c

    merged = {t: sorted(v.values(), key=lambda c: (c["file"], c["label"] or ""))
              for t, v in all_entries.items()}
    dest = os.path.join(BASE, "doc/enum-analysis/value-lists.json")
    with open(dest, "w") as fh:
        json.dump(merged, fh, indent=1)

    # stats
    withtypes = {t: v for t, v in merged.items()
                 if any(c["types"] for c in v)}
    print("tokens:", len(merged), " with type signal:", len(withtypes))
    # tokens with multiple distinct types across contexts
    multi = {}
    for t, v in merged.items():
        ts = set()
        for c in v:
            ts.update(c["types"])
        if len(ts) > 1:
            multi[t] = sorted(ts)
    print("tokens with >1 type signal:", len(multi))
    for t, ts in list(multi.items())[:25]:
        print("  ", t, ts)


if __name__ == "__main__":
    main()
