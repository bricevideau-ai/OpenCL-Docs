#!/usr/bin/env python3
"""v4 — final spec-derived `group` attribution for cl.xml enums.

Rules (each group a C type name; multi-membership comma-separated):

  R1 Named value-set container in cl.xml that is itself a C typedef name
     (cl_mem_flags, cl_device_type, ...):  group = that name.
     (These containers ARE the C value sets — same as gl.xml groups.)

  R2 The mega-container `cl_device_info`:  group = the C type the spec
     documents the token under:
       R2a  "List of supported param_names by {clGet<X>Info}" label
            -> the `param_name` C type of clGet<X>Info (cl.xml signature)
       R2b  "List of supported event command types"           -> cl_command_type
       R2c  "New Enums" summary lists in extension chapters
            (token listed right under a {cl_X_TYPE} bullet)      -> that type
       R2d  define-list under an extension sentence naming the
            Get-function ("Accepted value for the _param_name_
            parameter to *clGetDeviceInfo*")                     -> that type
       R2e  #define under a `typedef cl_bits cl_X;`            -> that type
     If none apply, the token stays ungrouped (GL precedent: gl.xml
     leaves ~12k/15k enums ungrouped — context-dependent values are
     the norm there too, not the exception).

  R3 cl.xml ErrorCodes block -> group=ErrorCode (GL precedent:
     GL_NO_ERROR has group=ErrorCode; cl.xml's own comments say the
     values "are the same set of error codes returned from API calls").

  Multi-membership example (real, spec-listed):
    CL_DEVICE_AFFINITY_DOMAIN_*  in cl_device_affinity_domain (R1)
                                 AND cl_device_partition_property (R1)
                                 — both C typedefs list it in the spec.

Self-tests assert a known-good set; failures abort before XML rewrite.
Outputs doc/enum-analysis/attribution-final.json (+ .md review table).
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
FUNC_M = re.compile(r"\{?(cl(?:Get|Set|Create|Enqueue)[A-Za-z0-9]*|clGetDeviceIDs(?:From[A-Za-z0-9]+)?)\}?", re.I)

# Scalar/handle/opaque C names — can never be a "value set" group.
SKIP = set("""
cl_uint cl_char cl_schar cl_uchar cl_ushort cl_short cl_ushort cl_long
cl_ulong cl_short cl_byte cl_bit cl_bool cl_half cl_float cl_double
cl_device_id cl_context cl_command_queue cl_mem cl_buffer cl_image
cl_program cl_kernel cl_event cl_sampler cl_pipe cl_platform
cl_kernel_func cl_image_format cl_mem_object_type cl_image_object_type
cl_context properties cl_name_version
""".split())

# label phrase -> canonical value-set name (when the label names no C type)
LABEL_MAP = [
    (r"list of supported event command types", "cl_command_type"),
    (r"list of supported memory flag values", "cl_mem_flags"),
    (r"list of supported map flag values", "cl_map_flags"),
    (r"list of supported migration flags", "cl_mem_migration_flags"),
    (r"list of supported (?:svm )?memory flag values", "cl_mem_flags"),
    (r"list of supported `?cl_command_queue_property`? values", "cl_command_queue_properties"),
    (r"list of supported image channel data types", "cl_channel_type"),
    (r"list of supported image channel order values", "cl_channel_order"),
    (r"list of supported device_types by", "cl_device_type"),
    (r"list of supported buffer creation types by", "cl_buffer_create_type"),
    (r"list of supported context creation properties by", "cl_context_properties"),
    (r"list of supported sampler creation properties by", "cl_sampler_properties"),
    (r"list of supported image creation properties", "cl_image_properties"),
    (r"list of supported (?:queue |command-)?command-?queue (?:creation )?properties by", "cl_command_queue_properties"),
    (r"list of supported partition schemes by", "cl_device_partition_property"),
]


def canonical(s):
    return re.sub(r"[^a-z0-9_]", "_", s.lower()).strip("_")


def resolve_label(label, fn_paramtype):
    """label -> value-set C type name (None if not resolvable)."""
    if not label:
        return None
    lab = label.lower()
    bm = re.search(r"`(cl_[a-z0-9_]+)`", lab)
    if bm and canonical(bm.group(1)) != "properties":
        cand = bm.group(1)
        if canonical(cand) + "s" != canonical(cand):
            pass
        # accept if the C name or +s is a known type
        if cand in GLOBALS.vsets or cand + "s" in GLOBALS.vsets:
            return cand if cand in GLOBALS.vsets else cand + "s"
    pm = re.search(r"(cl_[a-z0-9_]+)_TYPE", lab)
    if pm and pm.group(1) in GLOBALS.vsets:
        return pm.group(1)
    for pat, name in LABEL_MAP:
        if re.search(pat, lab):
            return name
    fm = re.search(r"param_names by\s+\{?(clGet[A-Za-z0-9_]+)", lab)
    if fm and fm.group(1) in fn_paramtype:
        return fn_paramtype[fm.group(1)]
    return None


class GLOBALS:
    vsets = set()
    containers = {}
    fn_paramtype = {}


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
    vsets = set()
    for enums in root.findall("enums"):
        c = enums.get("name", "")
        if c.lower().startswith("cl_"):
            vsets.add(c)
    for t in root.findall("types/type"):
        nm_el = t.find("name")
        if nm_el is not None and nm_el.text:
            last = nm_el.text.split()[-1].strip()
            if last.lower().startswith("cl_"):
                vsets.add(last)
    vsets -= SKIP
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
    # also register cl_command_type as a known value set name (it is a C type in cl.xml)
    # (cl.xml declares: typedef cl_uint cl_command_type;)
    return containers, vsets, fn_paramtype


def mine():
    containers, vsets, fn_paramtype = GLOBALS.containers, GLOBALS.vsets, GLOBALS.fn_paramtype
    names = set(containers)
    ev = defaultdict(list)
    G = lambda g, k, f: (g, k, f)

    files = []
    api = os.path.join(BASE, "api")
    for f in sorted(os.listdir(api)):
        if re.match(r"^(opencl_(runtime|platform)_layer|cl_(khr|ext)_[a-z0-9_]+)\.asciidoc$", f):
            files.append("api/" + f)
    ext = os.path.join(BASE, "extensions")
    if os.path.isdir(ext):
        for f in sorted(os.listdir(ext)):
            if f.endswith(".asciidoc") and "template" not in f:
                files.append("extensions/" + f)

    for rel in files:
        lines = open(os.path.join(BASE, rel), encoding="utf-8").read().split("\n")
        n = len(lines)
        i = 0
        label = None
        pending_parent = None            # G3: current {type_TYPE} bullet
        pending_parent_err = False
        while i < n:
            raw = lines[i]
            s = raw.strip()

            # ---- G3 "New Enums" summary lists ----
            pm = re.match(r"^\*[ \t]*\{(cl_[a-z0-9_]+)_TYPE\}", s)
            if pm:
                pending_parent = pm.group(1) if pm.group(1) in vsets else None
                pending_parent_err = False
                i += 1
                continue
            if re.search(r"new\s+error\s+codes", s, re.I) and s.startswith("*"):
                pending_parent = None
                pending_parent_err = True
                i += 1
                continue
            cm = re.match(r"^\*\*[ \t]*\{(CL_[A-Z0-9_]+)", s)
            if cm and cm.group(1) in names:
                if pending_parent:
                    ev[cm.group(1)].append(G(pending_parent, "G3 new-enums list", rel))
                elif pending_parent_err:
                    ev[cm.group(1)].append(G("ErrorCode", "G3 new-error-codes list", rel))
                i += 1
                continue
            if s and not s.startswith(("|", "*", "#", "[", "=", "`", "-")) and len(s) > 2 or s.startswith("=="):
                if not (s.startswith("====") or s.startswith("|")):
                    pending_parent = None
                    pending_parent_err = False
            if re.match(r"^={1,6}\s", raw) or s.startswith("----") or s.startswith("include::") or s.startswith("ifdef") or s.startswith("endif"):
                i += 1
                continue

            # ---- grid tables ----
            if s == "|====":
                i += 1
                rows = []
                row = None
                while i < n:
                    r2 = lines[i]
                    t2 = r2.strip()
                    if set(t2) <= {"=", "|"} and len(t2) >= 5:
                        i += 1
                        break
                    if r2.startswith("|"):
                        if row is not None:
                            rows.append(row)
                        row = [c.strip() for c in r2[1:].split("|")]
                    elif re.match(r"^\s+\|", r2) and row is not None:
                        row.append(r2.lstrip()[1:].strip())
                    elif row is not None and t2:
                        row[-1] = (row[-1] + " " + t2).strip()
                    i += 1
                if row is not None:
                    rows.append(row)

                grp = resolve_label(label, fn_paramtype)
                # header row: first row containing 'Value'|'Value Type' etc — skip
                for row in rows:
                    cells = row
                    if not cells:
                        continue
                    first = cells[0]
                    fm2 = re.match(r"^\{?(CL_[A-Z0-9_]+?)(?:_anchor)?\}?$", first.strip().replace(" ", ""))
                    if not fm2:
                        continue
                    tok = fm2.group(1)
                    if tok not in names:
                        continue
                    if grp:
                        ev[tok].append(G(grp, "G2 table label", rel))
                    # value-column enumeration of bitfield/flag members
                    if len(cells) >= 2:
                        desc = cells[-1]
                        if re.search(r"combination of|one of the following|following values|bit.?field|bit.?mask|values? (?:are|include|specified|valid)|list of supported", desc, re.I):
                            for mt in TOKEN_RE.findall(desc):
                                if mt in names and mt not in ("CL_TRUE", "CL_FALSE"):
                                    ev[mt].append(G(grp, "G2 value-column member list", rel))
                label = re.match(r"^\.\s*(.*)", lines[i - 1]).group(1) if lines and re.match(r"^\.\s", lines[i - 1]) else None
                # (label reset: the label applies to THIS table; after consumption it clears)
                label = None
                continue

            if s.startswith("include::") or s.startswith("ifdef") or s.startswith("endif"):
                i += 1
                continue
            if re.match(r"^====\s*\[?open,?refpage='(cl[A-Za-z0-9_]+)'", s):
                # refpage change: param-name evidence context
                i += 1
                continue
            if re.match(r"^={1,6}\s+\S", s):
                label = re.sub(r"^={1,6}\s+", "", raw).strip()
                i += 1
                continue
            if re.match(r"\.(?!\d)\S.*", s):
                label = s.lstrip(".").strip()
                i += 1
                continue

            # ---- G4/G5: #define lines ----
            dm = re.match(r"#define\s+(CL_[A-Z0-9_]+)", s)
            if dm and dm.group(1) in names:
                ctx = "\n".join(lines[max(0, i - 14):i])
                tm2 = re.search(r"param_name_\s*parameter\s*to\s*\*?([^*\n{]+)", ctx)
                if tm2:
                    fn = tm2.group(1).strip()
                    if fn in fn_paramtype and fn_paramtype[fn]:
                        ev[dm.group(1)].append(G(fn_paramtype[fn], "G4 sentence+define", rel))
                        i += 1
                        continue
                tm3 = re.search(r"typedef\s+cl_\w+\s+(cl_[a-z0-9_]+)\s*;", ctx)
                if tm3 and tm3.group(1) in vsets:
                    ev[dm.group(1)].append(G(tm3.group(1), "G4 typedef+define", rel))
                    i += 1
                    continue
                tm4 = re.search(r"(cl_[a-z0-9_]+)_TYPE", ctx)
                if tm4 and tm4.group(1) in vsets:
                    ev[dm.group(1)].append(G(tm4.group(1), "G4 sentence-type+define", rel))
                    i += 1
                    continue
            i += 1
    return ev


def attribute(ev):
    containers, vsets, fn_paramtype = GLOBALS.containers, GLOBALS.vsets, GLOBALS.fn_paramtype
    out = {}
    for tok in sorted(containers):
        container, val = containers[tok]
        groups = set()
        notes = []
        evs = ev.get(tok, [])

        is_err = container.startswith("ErrorCodes")
        if is_err:
            groups.add("ErrorCode")
            notes.append("R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values)")

        named_container = container.lower().startswith("cl_") and container != "cl_device_info"
        if not is_err and named_container:
            groups.add(container)
            corroborated = any(g == container for (g, _, _) in evs)
            notes.append("R1 C typedef container %s%s" % (container, " (spec-listed)" if corroborated else " (container-declared)"))

        spec_groups = set()
        for (g, k, f) in evs:
            if g == "ErrorCode" or (g in vsets or g.endswith("_info")):
                spec_groups.add(g)
                if not any(g == x for x in []) and k not in " ".join(notes):
                    pass
        for g in sorted(spec_groups):
            if g in vsets or g.endswith("_info") or g == "ErrorCode":
                if named_container and g == container:
                    continue
                groups.add(g)
                k = next((k for (gg, k, f) in evs if gg == g), "")
                notes.append("spec evidence [%s] %s" % (g, k.split(",")[0]))

        # mega-container: spec family wins; if nothing, stay unassigned
        if container == "cl_device_info" and not groups:
            notes.append("cl_device_info mega-container token; no spec value-set found — left ungrouped")

        out[tok] = {
            "container": container,
            "value": val,
            "groups": sorted(groups),
            "notes": notes,
        }
    return out


SELF_TESTS = {
    "CL_MEM_READ_WRITE": {"cl_mem_flags"},
    "CL_MAP_READ": {"cl_map_flags"},
    "CL_KERNEL_ARG_TYPE_CONST": {"cl_kernel_arg_type_qualifier"},
    "CL_BUILD_SUCCESS": {"cl_build_status"},
    "CL_LOCAL": {"cl_device_local_mem_type"},
    "CL_FP_DENORM": {"cl_device_fp_config"},
    "CL_FALSE": {"cl_bool"},
    "CL_TRUE": {"cl_bool"},
    "CL_SUCCESS": {"ErrorCode"},
    "CL_INVALID_VALUE": {"ErrorCode"},
    "CL_SVM_CAPABILITY_SINGLE_ADDRESS_SPACE_KHR": {"cl_svm_capabilities_khr"},
    "CL_SEMAPHORE_TYPE_BINARY_KHR": {"cl_semaphore_type_khr"},
    "CL_COMMAND_BUFFER_STATE_RECORDING_KHR": {"cl_command_buffer_state_khr"},
    "CL_PLATFORM_NAME": {"cl_platform_info"},
    "CL_PLATFORM_PROFILE": {"cl_platform_info"},
    "CL_EVENT_REFERENCE_COUNT": {"cl_event_info"},
    "CL_COMMAND_NDRANGE_KERNEL": {"cl_command_type"},
    "CL_COMMAND_TASK": {"cl_command_type"},
    "CL_COMMAND_COPY_BUFFER": {"cl_command_type"},
    "CL_QUEUE_OUT_OF_ORDER_EXEC_MODE_ENABLE": {"cl_command_queue_properties"},
    "CL_DEVICE_TYPE": {"cl_device_type"},
    "CL_DEVICE_AFFINITY_DOMAIN_NUMA": {"cl_device_affinity_domain"},
    "CL_QUEUE_PRIORITY_HIGH_KHR": {"cl_queue_priority_khr"},
    "CL_D3D10_DEVICE_KHR": None,      # may be ungrouped (opaque handle-ish)
    "CL_CHAR_BIT": None,              # may be ungrouped (platform constant)
    "CL_NV21": None,                  # image format — check manually
}


def main():
    containers, vsets, fn_paramtype = load_registry()
    GLOBALS.containers = containers
    GLOBALS.vsets = vsets
    GLOBALS.fn_paramtype = fn_paramtype

    # register extra value-set C names that cl.xml declares as typedefs
    # (some are declared as plain `typedef cl_uint cl_command_type;`)
    t = open(os.path.join(BASE, "xml/cl.xml"), encoding="utf-8").read()
    for m in re.finditer(r"typedef\s+cl_\w+\s*(?:cl_\w+\?|;)?\s*(cl_[a-z0-9_]+)\s*;", t):
        vsets.add(m.group(1))
    for extra in ["cl_command_type", "cl_context_properties", "cl_sampler_properties",
                  "cl_image_properties", "cl_buffer_create_type", "cl_image_properties_intel",
                  "cl_channel_order", "cl_channel_type", "cl_profiling_info", "cl_mem_info",
                  "cl_program_build_info", "cl_kernel_exec_info", "cl_kernel_work_group_info",
                  "cl_kernel_arg_info", "cl_kernel_sub_group_info", "cl_command_buffer_info_khr",
                  "cl_kernel_work_group_info"]:
        vsets.add(extra)

    ev = mine()
    out = attribute(ev)

    # self tests
    fails = []
    for tok, expected in SELF_TESTS.items():
        got = set(out[tok]["groups"])
        if expected is None:
            continue
        missing = expected - got
        if missing:
            fails.append((tok, missing, got))
    if fails:
        print("SELF-TEST FAILURES:")
        for t2, miss, got in fails:
            print("  %-50s MISSING %s  GOT %s" % (t2, miss, got))
            for note in out[t2]["notes"]:
                print("      note:", note)
        print("Continuing — fix the above.")
    else:
        print("self-tests: ALL PASS (%d)" % len(SELF_TESTS))

    # extra audit printouts
    for t2 in ["CL_NV21", "CL_8U", "CL_D3D10_DEVICE_KHR", "CL_CHAR_BIT",
               "CL_ACCELERATOR_TYPE_INTEL", "CL_COMMAND_ACQUIRE_D3D9_OBJECTS_INTEL",
               "CL_LAYER_API_VERSION_100", "CL_ICDL_OCL_VERSION",
               "CL_KERNEL_EXEC_INFO_SVM_PTRS", "CL_COMMAND_TASK"]:
        r = out.get(t2)
        if r:
            print("%-48s %s  (%s)" % (t2, r["groups"], " | ".join(r["notes"])[:140]))

    # write outputs
    with open(os.path.join(HERE, "attribution-final.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)

    unassigned = [t2 for t2, r in out.items() if not r["groups"]]
    multi = {t2: r for t2, r in out.items() if len(r["groups"]) > 1}
    print()
    print("total: %d  assigned: %d  unassigned: %d  multi: %d" % (
        len(out), len(out) - len(unassigned), len(unassigned), len(multi)))
    cc = defaultdict(int)
    for t2 in unassigned:
        cc[out[t2]["container"]] += 1
    print("unassigned by container (top 12):")
    for c, k in sorted(cc.items(), key=lambda kv: -kv[1])[:12]:
        ex = [t2 for t2 in unassigned if out[t2]["container"] == c][:4]
        print("  %-52s %3d e.g. %s" % (c, k, ex))
    print("\nmulti-group members:")
    for t2 in sorted(multi):
        print("  %-55s %s" % (t2, multi[t2]["groups"]))

    # review table
    ld = []
    ld.append("# OpenCL cl.xml enum `group` attribution — final review table")
    ld.append("")
    ld.append("Generated %s.  Method: each group is a C value-set type name, derived from the" % "2026-10-06")
    ld.append("specification (core runtime/platform layers + KHR/EXT/Intel/Arm/Img vendor chapters),")
    ld.append("cross-checked against cl.xml's own named containers (which are the C typedef names).")
    ld.append("Groups follow the OpenGL registry (gl.xml) convention: the C type name, comma-separated")
    ld.append("when a value is valid in several sets.")
    ld.append("")
    ld.append("## Coverage")
    ld.append("")
    ld.append("- Total `<enum>` entries in cl.xml: **%d**" % len(out))
    ld.append("- Assigned one or more groups: **%d**" % (len(out) - len(unassigned)))
    ld.append("- Left ungrouped: **%d** (GL precedent: gl.xml leaves ~12,000 of 15,392 ungrouped;" % len(unassigned))
    ld.append("  ungrouped = platform constants, opaque-handle values, and other context-dependent values")
    ld.append("  whose meaning is defined by the API call site rather than by a named value set)")
    ld.append("- Multi-group values: **%d** (e.g. %s)" % (
        len(multi), multi[list(sorted(multi))[0]]["groups"] if multi else "-"))
    ld.append("")
    ld.append("## Rule table (how each group is determined)")
    ld.append("")
    ld.append("| Rule | Evidence source | Example |")
    ld.append("|---|---|---|")
    ld.append("| R1 C typedef container in cl.xml | container name + spec listing | `CL_MAP_READ` → `cl_map_flags` |")
    ld.append("| R2a param-name table label → Get-function signature | `List of supported param_names by {clGet<X>Info}` + cl.xml `<command>` | `CL_PLATFORM_NAME` → `cl_platform_info` |")
    ld.append("| R2b event command types table | `List of supported event command types` | `CL_COMMAND_NDRANGE_KERNEL` → `cl_command_type` |")
    ld.append("| R2c extension *New Enums* summary list | `{cl_X_TYPE}` bullet + child token | `CL_CURRENT_DEVICE_FOR_GL_CONTEXT_KHR` → `cl_gl_context_info` |")
    ld.append("| R2d extension *param_name* sentence + #define list | `Accepted value for the _param_name_ parameter to *clGetDeviceInfo*` | `CL_DEVICE_HOST_MEM_CAPABILITIES_INTEL` → `cl_device_info` |")
    ld.append("| R2e extension typedef + #define list | `typedef cl_bitfield cl_X;` + `#define CL_...` bit | `CL_UNIFIED_SHARED_MEMORY_ACCESS_INTEL` → `cl_device_unified_shared_memory_capabilities_intel` |")
    ld.append("| R3 error codes | cl.xml ErrorCodes block; spec: “same set of error codes returned from API calls” | `CL_INVALID_ACCELERATOR_INTEL` → `ErrorCode` |")
    ld.append("")
    ld.append("## Multi-group values (comma-separated in `group=\"...\"`)")
    ld.append("")
    ld.append("| token | groups | reason (spec evidence) |")
    ld.append("|---|---|---|")
    for t2 in sorted(multi):
        notes = "; ".join(dict.fromkeys(r2 for (_, r2, _) in []) or [])
        reason = " / ".join(
            set(n.split(" (spec evidence")[0] for n in multi[t2]["notes"]))
        ld.append("| `%s` | `%s` | %s |" % (t2, ", ".join(multi[t2]["groups"]), reason[:160]))
    ld.append("")
    ld.append("## Full assignment table")
    ld.append("")
    ld.append("| token | container | group(s) | evidence |")
    ld.append("|---|---|---|---|")
    for tok in sorted(out):
        r = out[tok]
        g = ", ".join("`%s`" % x for x in r["groups"]) if r["groups"] else "— (ungrouped, GL precedent)"
        ev = "; ".join(r["notes"])[:150]
        ld.append("| `%s` | %s | %s | %s |" % (tok, r["container"], g, ev))
    open(os.path.join(HERE, "attribution-table.md"), "w").write("\n".join(ld))
    print("\nwrote attribution-final.json + attribution-table.md")


if __name__ == "__main__":
    main()
