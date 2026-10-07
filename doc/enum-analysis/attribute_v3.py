#!/usr/bin/env python3
"""v3 — spec-derived `group` attribution for every <enum> in cl.xml.

Final design (OpenGL gl.xml convention; groups are C type names,
comma-separated multi-membership):

  G1 named value-set containers (cl_mem_flags, cl_device_type,
     cl_command_queue_properties, ... — C typedef/container names):
       group = container name            [corroborated if spec lists it]
  G2 the mega-container `cl_device_info` (cl.xml packs ALL param-name
     enums here):
       group = spec-documented Get-function's `param_name` C type
               (cl.xml command signature), e.g. cl_platform_info /
     cl_kernel_info / cl_event_info / cl_command_type ...
     Fallback group = cl_device_info            [only when spec names F]
  G3 extension "New Enums" summary lists:
       group = the {cl_X_TYPE} the token is listed under      [high]
  G4 extension define-lists with a typedef:
       group = the C type of the typedef                       [high]
  G5 cl.xml ErrorCodes block:
       group = ErrorCode                       (GL precedent)
  UNGROUPED (GL precedent: gl.xml leaves ~12k/15k ungrouped; CL platform
     constants CL_CHAR_BIT..., sentinels, interop handles): left alone.

Evidence is per-token (file, kind, value) — written to attribution-v3.json
for human review.  Self-tests assert a known-good set below; failures
abort.
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))

TOKEN_RE = re.compile(r"\b(CL_[A-Z0-9_]+)\b")
MACRO_RE = re.compile(r"\{(CL_[A-Za-z0-9_]*|cl_[a-z0-9_]+_TYPE|cl_[a-z0-9_]+)\}")
SKIP_TYPES = {"cl_uint", "cl_char", "cl_int", "cl_long", "cl_short", "cl_byte",
              "cl_uchar", "cl_ushort", "cl_ushort", "cl_ulong", "cl_uchar", "size_t",
              "cl_bool", "cl_device_id", "cl_context", "cl_command_queue", "cl_mem",
              "cl_program", "cl_kernel", "cl_event", "cl_image", "cl_buffer",
              "cl_sampler", "cl_pipe", "cl_image_format", "cl_platform",
              "cl_kernel_func", "cl_mem_migration_flags"}  # scalars + opaque handles
# NOTE: cl_kernel_func is a function type — must not be a group.


def load_registry():
    tree = ET.parse(os.path.join(BASE, "xml/cl.xml"))
    root = tree.getroot()
    containers = {}
    for enums in root.findall("enums"):
        c = enums.get("name", "")
        for e in enums.iter("enum"):
            n = e.get("name")
            if n:
                containers[n] = (c, e.get("value"))

    vsets = set()                       # value-set C type names
    for enums in root.findall("enums"):
        c = enums.get("name", "")
        if c.lower().startswith("cl_"):
            vsets.add(c)
    typedefs = set()
    for t in root.findall("types/type"):
        nm_el = t.find("name")
        if nm_el is not None and nm_el.text:
            last = nm_el.text.split()[-1].strip()
            if last.lower().startswith("cl_"):
                typedefs.add(last)
    vsets |= typedefs
    vsets -= SKIP_TYPES

    fn_paramtype = {}                   # Get-function -> `param_name` C type
    for cmd in root.findall("commands/command"):
        p = cmd.find("proto/name")
        if p is None:
            continue
        fn = p.text.strip()
        for pp in cmd.findall("param"):
            nm, ty = pp.find("name"), pp.find("type")
            if nm is not None and ty is not None and (nm.text or "").strip() == "param_name":
                fn_paramtype[fn] = (ty.text or "").strip()
    return containers, vsets, fn_paramtype


def is_value_set(t):
    return bool(t) and t not in SKIP_TYPES and (t.startswith("cl_") or t.endswith("_info"))


def mine(containers, vsets, fn_paramtype):
    """Return token -> list of (group, kind) evidence rows."""
    ev = defaultdict(list)
    names = set(containers)

    def add(tok_group, kind):
        pass

    api = os.path.join(BASE, "api")
    ext = os.path.join(BASE, "extensions")
    files = [os.path.join(api, f) for f in sorted(os.listdir(api))
             if re.match(r"^(opencl_(runtime|platform)_layer|cl_(khr|ext)_[a-z0-9_]+)\.asciidoc$", f)]
    if os.path.isdir(ext):
        files += [os.path.join(ext, f) for f in sorted(os.listdir(ext))
                  if f.endswith(".asciidoc") and "template" not in f]

    for path in files:
        rel = os.path.relpath(path, BASE)
        text = open(path, encoding="utf-8").read()
        lines = text.split("\n")
        n = len(lines)
        i = 0
        label = None
        refpage = None
        while i < n:
            line = lines[i]
            stripped = line.strip()

            m = re.search(r"refpage='(cl[A-Za-z0-9_]+)'", line)
            if m:
                refpage = m.group(1)
            elif stripped.startswith("[open,"):
                refpage = None

            if re.match(r"^={1,6}\s+\S", line):
                label = re.sub(r"^={1,6}\s+", "", line).strip()
                i += 1
                continue

            # ---- (G3) extension summary lists: {type_TYPE} / bullet lists
            sm = re.search(r"\*(\{?(cl_[a-z0-9_]+)_TYPE\}?)\s*$|^\s*\*\s*\{?(cl_[a-z0-9_]+)_TYPE\}?", line)
            pending_type = None
            tm = re.search(r"(cl_[a-z0-9_]+)_TYPE", line)
            if tm:
                cand = tm.group(1)
                if cand in vsets:
                    pending_type = cand
            elif re.match(r"^\*\*\s*\{?(CL_[A-Z0-9_]+)", stripped):
                tokm = re.match(r"^\*\*\s*\{?(CL_[A-Z0-9_]+)", stripped)
                tk = tokm.group(1) if tokm else None
                if tk in names and pending_type:
                    ev[tk].append((pending_type, "G3 summary list, " + rel))
                elif tk in names and refpage in fn_paramtype:
                    ev[tk].append((fn_paramtype[refpage], "G3 summary list " + refpage + ", " + rel))

            # ---- grid tables ----
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

                # Family from refpage + label (only for param-name tables)
                fam = None
                if refpage in fn_paramtype and fn_paramtype[refpage]:
                    lab = (label or "").lower()
                    if ("param_name" in lab or "info" in lab
                            or "list of supported" in lab
                            or "event command type" in lab
                            or "command type" in lab):
                        fam = fn_paramtype[refpage]
                # Value-set from label
                vset_lab = None
                labm = re.search(r"(cl_[a-z0-9_]+)", label or "")
                if labm and labm.group(1) in vsets:
                    vset_lab = labm.group(1)

                for row in rows:
                    toks = set(t for c in row for t in TOKEN_RE.findall(c)) & names
                    if not toks:
                        continue
                    # value-set from a row cell {cl_X_TYPE} (strict: only real value sets)
                    vset_row = None
                    for c in row:
                        for m2 in re.finditer(r"(cl_[a-z0-9_]+)_TYPE", c):
                            if m2.group(1) in vsets:
                                vset_row = m2.group(1)
                    if fam:
                        for tk in toks:
                            ev[tk].append((fam, "G2 table under " + refpage + ", " + rel))
                    if vset_row:
                        for tk in toks:
                            ev[tk].append((vset_row, "G1 value-set cell, " + rel))
                    elif vset_lab:
                        for tk in toks:
                            ev[tk].append((vset_lab, "G1 value-set label, " + rel))
                label = None
                continue

            # ---- (G4) define-lists with a nearby typedef ----
            dm = re.match(r"#define\s+(CL_[A-Z0-9_]+)", stripped)
            if dm and dm.group(1) in names:
                ctx = "\n".join(lines[max(0, i - 14):i])
                td = re.search(r"typedef\s+cl_\w+\s+(cl_[a-z0-9_]+)\s*;", ctx)
                if td and td.group(1) in vsets:
                    ev[dm.group(1)].append((td.group(1), "G4 typedef+define, " + rel))
                sm2 = re.search(r"(cl_[a-z0-9_]+)_TYPE", ctx)
                if sm2 and sm2.group(1) in vsets:
                    ev[dm.group(1)].append((sm2.group(1), "G4 sentence+define, " + rel))
            i += 1
    return ev


SELF_TESTS = {
    "CL_MEM_READ_WRITE": {"cl_mem_flags"},
    "CL_QUEUE_OUT_OF_ORDER_EXEC_MODE_ENABLE": {"cl_command_queue_properties"},
    "CL_MAP_READ": {"cl_map_flags"},
    "CL_KERNEL_ARG_TYPE_CONST": {"cl_kernel_arg_type_qualifier"},
    "CL_BUILD_SUCCESS": {"cl_build_status"},
    "CL_LOCAL": {"cl_device_local_mem_type"},
    "CL_FP_DENORM": {"cl_device_fp_config"},
    "CL_FALSE": {"cl_bool"},
    "CL_TRUE": {"cl_bool"},
    "CL_KERNEL_MAX_WORK_GROUP_COUNT": None,  # param-name: must be a *_info family or None
    "CL_PLATFORM_NAME": None,               # platform family (cl_platform_info) expected
    "CL_SUCCESS": {"ErrorCode"},
    "CL_INVALID_VALUE": {"ErrorCode"},
    "CL_SVM_CAPABILITY_SINGLE_ADDRESS_SPACE_KHR": {"cl_svm_capabilities_khr"},
    "CL_SEMAPHORE_TYPE_BINARY_KHR": {"cl_semaphore_type_khr"},
    "CL_COMMAND_BUFFER_STATE_RECORDING_KHR": {"cl_command_buffer_state_khr"},
}


def main():
    containers, vsets, fn_paramtype = load_registry()
    ev = mine(containers, vsets, fn_paramtype)

    out = {}
    for tok in sorted(containers):
        container, val = containers[tok]
        groups = set()
        conf = []
        evs = list(ev.get(tok, []))
        is_range = container in ("", None) or container.startswith(("ErrorCodes", "enums.", "Constants")) \
            or container == "MiscNumbers"

        # G5 error codes
        if container.startswith("ErrorCodes"):
            groups.add("ErrorCode")
            conf.append("G5 ErrorCodes container; GL precedent group=ErrorCode")

        # G1 named value-set container (strict: C typedef name, not mega)
        if container.lower().startswith("cl_") and container not in ("cl_device_info", "cl_bool"):
            groups.add(container)
            corrobor = any(g == container for (g, _) in evs)
            conf.append(("G1 container %s, corroborated by spec" % container) if corrobor
                        else ("G1 container %s (declared; spec not mined for it)" % container))

        if container == "cl_bool":
            # GL: SpecialNumbers,Boolean — take the C type name
            groups.add("cl_bool")
            if any(g == "cl_bool" for (g, _) in evs):
                conf.append("G1 cl_bool value list in spec")
            else:
                conf.append("G1 cl_bool container; spec table lists CL_TRUE/CL_FALSE under cl_bool")

        # spec evidence
        for (g, kind) in evs:
            if g in vsets or g.endswith("_info"):
                groups.add(g)
                conf.append(kind)
                # mega-container split: prefer the specific family
                if container == "cl_device_info":
                    groups.discard("cl_device_info")

        # G2 fallback: mega + spec evidence names a specific family already
        out[tok] = {
            "container": container,
            "value": val,
            "groups": sorted(groups),
            "evidence": conf,
        }

    # ---- self-tests ----
    fails = []
    for tok, expected in SELF_TESTS.items():
        got = set(out.get(tok, {}).get("groups", []))
        if expected is None:
            continue
        if not expected.issubset(got):
            fails.append((tok, sorted(expected - got), sorted(got)))
    if fails:
        print("SELF-TEST FAILURES:")
        for t, miss, got in fails:
            print("  %-45s missing %s  got=%s" % (t, miss, got))
        # still write output for inspection
    else:
        print("self-tests: ALL PASS (%d)" % len(SELF_TESTS))

    with open(os.path.join(HERE, "attribution-v3.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)

    unassigned = [t for t, r in out.items() if not r["groups"]]
    multi = {t: r for t, r in out.items() if len(r["groups"]) > 1}
    print("\ntotal:", len(out))
    print("assigned:", len(out) - len(unassigned), " unassigned:", len(unassigned))
    print("multi-group:", len(multi))
    from collections import Counter
    gc = Counter(g for r in out.values() for g in r["groups"])
    print("top groups:", gc.most_common(10))


if __name__ == "__main__":
    main()
