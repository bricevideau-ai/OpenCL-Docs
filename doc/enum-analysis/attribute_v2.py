#!/usr/bin/env python3
"""DEFINITIVE spec-derived `group` attribution for every <enum> in cl.xml.

Group vocabulary (OpenGL gl.xml convention — groups are C value-set names,
comma-separated when a token belongs to several):

  * value-set types  : cl_device_type, cl_mem_flags, cl_semaphore_type_khr ...
  * param-name types : cl_platform_info, cl_device_info, cl_kernel_info,
                       cl_event_info, cl_command_type ...
  * ErrorCode        : for the ErrorCodes.* registry block (GL convention)

Every assignment carries spec evidence from at least one of:
  A. a spec table/line whose C type cell or label names the value set
  B. a spec table/sentence/define-list that lists the token under a
     Get-function F  (cl.xml's command signature names F's `param_name`
     C type — this is the keystone for splitting cl.xml's mega-container
     `cl_device_info` into spec-declared param-name families)
  C. the declared named value-set container in cl.xml (C typedef names)
  D. ErrorCodes container + GL `ErrorCode` precedent

cl_device_info in cl.xml is a mega-container: the SPLIT into
cl_platform_info / cl_kernel_info / cl_event_info / cl_kernel_exec_info /
cl_command_type / ... comes from the spec (per Get-function tables and
cl.xml's unused-range reservation comments), and each family's C type is
declared in that Get-function's signature.

Tokens with no evidence are left WITHOUT a group attribute (GL precedent:
gl.xml itself leaves ~12k of 15k enums ungrouped).
"""

import json
import os
import re
import xml.etree.ElementTree as ET
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))

TOKEN_RE = re.compile(r"\b(CL_[A-Z0-9_]+)\b")
TYPE_MACRO_RE = re.compile(r"\{(cl_[a-zA-Z0-9_]+)_TYPE\}")
EXT_PARAM_RE = re.compile(
    r"_param_name_\s*(?:parameter|argument)?[^*\n]*\*\s*(cl[A-Za-z0-9_]+)", re.I)
EXT_PARAM_RE2 = re.compile(r"_param_name_\s+parameter\s+to\s+\*?(cl[A-Za-z0-9_]+)")
TYPDEF_RE = re.compile(r"typedef\s+cl_\w+\s+(cl_[a-z0-9_]+)\s*;")
DEFINE_RE = re.compile(r"#define\s+(CL_[A-Z0-9_]+)")
SKIP_TYPES = {"cl_uint", "cl_char", "cl_int", "cl_long", "cl_short", "cl_byte",
              "cl_bitfield", "size_t"}


def registry():
    tree = ET.parse(os.path.join(BASE, "xml/cl.xml"))
    root = tree.getroot()
    containers = {}
    for enums in root.findall("enums"):
        c = enums.get("name", "")
        for e in enums.iter("enum"):
            n = e.get("name")
            if n:
                containers[n] = (c, e.get("value"))
    names = set(containers)

    vsets = set()
    for enums in root.findall("enums"):
        c = enums.get("name", "")
        if c.lower().startswith("cl_"):
            vsets.add(c)
    typedefs = set()
    for t in root.findall("types/type"):
        name_el = t.find("name")
        if name_el is not None and name_el.text:
            typedefs.add((name_el.text or "").split()[-1].strip())
        nm = (t.get("name") or "").strip()
        if nm.lower().startswith("cl_") and nm not in SKIP_TYPES:
            typedefs.add(nm)
    typedefs.discard("")

    fn_paramtype = {}
    for cmd in root.findall("commands/command"):
        p = cmd.find("proto/name")
        if p is None:
            continue
        fn = p.text.strip()
        for pp in cmd.findall("param"):
            nm, ty = pp.find("name"), pp.find("type")
            if nm is not None and ty is not None and (nm.text or "").strip() == "param_name":
                fn_paramtype[fn] = (ty.text or "").strip()
    return names, containers, vsets, typedefs, fn_paramtype


def spec_files():
    files = []
    api = os.path.join(BASE, "api")
    for f in sorted(os.listdir(api)):
        if re.match(r"^(opencl_(runtime|platform)_layer|cl_(khr|ext)_[a-z0-9_]+)\.asciidoc$", f):
            files.append(os.path.join(api, f))
    ext = os.path.join(BASE, "extensions")
    if os.path.isdir(ext):
        for f in sorted(os.listdir(ext)):
            if f.endswith(".asciidoc") and "template" not in f:
                files.append(os.path.join(ext, f))
    return files


def mine(evidence, names, vsets, typedefs, fn_paramtype):
    for path in spec_files():
        rel = os.path.relpath(path, BASE)
        lines = open(path, encoding="utf-8").read().split("\n")
        n = len(lines)
        i = 0
        label = None
        refpage = None
        while i < n:
            line = lines[i]
            stripped = line.strip()

            if re.match(r"^={1,6}\s+\S", line):
                label = re.sub(r"^={1,6}\s+", "", line).strip()
                i += 1
                continue

            m = re.search(r"refpage='(cl[A-Za-z0-9_]+)'", line)
            if m:
                refpage = m.group(1)
            elif stripped.startswith("[open,"):
                refpage = None

            if stripped == "|====":
                i += 1
                rows = []
                row = None
                while i < n:
                    raw = lines[i]
                    t = raw.strip()
                    if set(t) <= {"=", "|"} and len(t) >= 5:
                        i += 1
                        break
                    if raw.startswith("|"):
                        if row is not None:
                            rows.append(row)
                        row = [c.strip() for c in raw[1:].split("|")]
                    elif re.match(r"^\s+\|", raw) and row is not None:
                        row.append(raw.lstrip()[1:].strip())
                    elif row is not None and t:
                        row[-1] = (row[-1] + " " + t).strip()
                    i += 1
                if row is not None:
                    rows.append(row)

                fams = set()
                lab_types = set(TYPE_MACRO_RE.findall(label or ""))
                lab_types.update(re.findall(r"`(cl_[a-z0-9_]+)`", label or ""))
                for tname in ["".join(p) for p in lab_types]:
                    if tname in (vsets | typedefs) and tname not in SKIP_TYPES:
                        fams.add(tname)
                if refpage in fn_paramtype and fn_paramtype[refpage]:
                    fams.add(fn_paramtype[refpage])

                for row in rows:
                    toks = set(t for c in row for t in TOKEN_RE.findall(c)) & names
                    if not toks:
                        continue
                    vtype = None
                    for c in row:
                        tm = [t for t in TYPE_MACRO_RE.findall(c) if t not in SKIP_TYPES]
                        if tm:
                            vtype = tm[0]
                            break
                    for fname in toks:
                        if vtype:
                            evidence[fname].add((rel, vtype, "value-type cell"))
                        for fam in fams:
                            evidence[fname].add((rel, fam, "function-family"))
                label = None
                continue

            # extension "sentence + define list" and typedef+define
            dm = DEFINE_RE.match(stripped)
            if dm and dm.group(1) in names:
                nm = dm.group(1)
                # scan the 14 lines above for defining context
                ctx = "\n".join(lines[max(0, i - 14):i + 1])
                s2 = EXT_PARAM_RE.search(ctx) or EXT_PARAM_RE2.search(ctx)
                if s2:
                    fn = s2.group(1)
                    if fn in fn_paramtype and fn_paramtype[fn]:
                        evidence[nm].add((rel, fn_paramtype[fn], "ext sentence+define"))
                td = TYPDEF_RE.search(ctx)
                if td and td.group(1) in (vsets | typedefs):
                    evidence[nm].add((rel, td.group(1), "ext typedef+define"))
            i += 1


def attribute(names, containers, vsets, typedefs, evidence):
    MEGA = "cl_device_info"
    out = {}
    for tok in sorted(names):
        container, val = containers[tok]
        ev = evidence.get(tok, set())
        groups = set()
        conf = set()
        notes = []

        if container.startswith("ErrorCodes"):
            groups.add("ErrorCode")
            conf.add("declared")
            notes.append("cl.xml ErrorCodes container; GL precedent group=ErrorCode")

        if container.lower().startswith("cl_") and container != MEGA:
            groups.add(container)
            corroborated = any(g == container for (_, g, _) in ev)
            if corroborated:
                conf.add("high")
                notes.append("cl.xml container %s corroborated by spec" % container)
            else:
                conf.add("declared")
                notes.append("cl.xml value-set container %s" % container)

        spec_fams = set(g for (_, g, _) in ev)
        for fam in sorted(spec_fams):
            if fam not in SKIP_TYPES and (fam in (vsets | typedefs) or fam.endswith("_info")):
                # mega-container split: spec-named family replaces bare container
                if container == MEGA and fam != MEGA:
                    groups = {fam}
                    notes.append("spec family %s (cl_device_info mega-container split)" % fam)
                    conf.add("high")
                    continue
                if fam == MEGA and container == MEGA:
                    continue
                groups.add(fam)
                notes.append("spec evidence: %s" % fam)
                conf.add("high")

        out[tok] = {
            "container": container,
            "value": val,
            "groups": sorted(groups),
            "confidence": sorted(conf),
            "evidence": notes,
            "files": sorted(set(f for (f, _, _) in ev)),
        }
    return out


def main():
    names, containers, vsets, typedefs, fn_paramtype = registry()
    evidence = defaultdict(set)
    mine(evidence, names, vsets, typedefs, fn_paramtype)
    out = attribute(names, containers, vsets, typedefs, evidence)

    with open(os.path.join(HERE, "attribution-v2.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)

    unassigned = [t for t, r in out.items() if not r["groups"]]
    multi = {t: r for t, r in out.items() if len(r["groups"]) > 1}
    high = sum(1 for r in out.values() if "high" in r["confidence"])
    decl = sum(1 for r in out.values() if "declared" in r["confidence"] and "high" not in r["confidence"])
    print("total:", len(out))
    print("assigned:", len(out) - len(unassigned), " unassigned:", len(unassigned))
    print("multi-group:", len(multi))
    print("high:", high, " declared-only:", decl)
    print("\n--- multi-group members ---")
    for t in sorted(multi):
        print("  %-45s %s" % (t, multi[t]["groups"]))
    print("\n--- unassigned sample (by container) ---")
    from collections import Counter
    cc = Counter(out[t]["container"] for t in unassigned)
    for c, k in cc.most_common(12):
        ex = [t for t in unassigned if out[t]["container"] == c][:4]
        print("  %-45s %3d e.g. %s" % (c, k, ex))


if __name__ == "__main__":
    main()
